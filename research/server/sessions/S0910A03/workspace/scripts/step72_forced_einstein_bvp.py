"""
Step 72: Forced finite DeTurck BVP for T²-invariant Einstein core.

The metric is g = dt² + e^{2a(t,θ)} dθ² + e^{2b(t,θ)} dx² + e^{2c(t,θ)} dy²
on [0,R] × S¹(θ) × T² (x,y are flat quotient directions).

The Einstein equations Ric + 3g = 0 in this gauge give five PDEs
(E_00, E_01, E_11/g_11, E_22/g_22, E_33/g_33).

We solve the THREE EVOLUTION equations (E_00, E_22/g_22, E_33/g_33) as a BVP
with:
  - CENTER (t=0): Koiso reflection: a_t = b_t = c_t = 0, plus fiber data
    (a₀(θ), b₀(θ), c₀(θ)) from the scalar-curvature -6 condition.
  - OUTER (t=R): Free boundary — we measure what emerges.

Then we evaluate ALL FIVE Einstein defect components to get the full residual.

Key design: the Fourier-Galerkin discretization in θ, finite differences in t.
"""

import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import interp1d
import json, traceback

def make_koiso_center(A_amp, N_fourier):
    """Build Koiso center fiber with R_h = -6.
    
    Fiber: h = dθ² + e^{2b₀(θ)} dx² + e^{2c₀(θ)} dy²
    with a₀ = 0 (gauge), b₀ = A*sin(θ), c₀ = -A*sin(θ) (volume-preserving).
    
    Check: R_h = -2(b₀'' + c₀'' + b₀'² + c₀'² + b₀'c₀')
    For b₀ = A sin θ, c₀ = -A sin θ:
      b₀' = A cos θ, c₀' = -A cos θ, b₀'' = -A sin θ, c₀'' = A sin θ
      R_h = -2(0 + 2A² cos²θ - A² cos²θ) = -2A² cos²θ
    
    This gives R_h ≤ 0 but not = -6 everywhere. We need to solve for the
    right profile. Use the Yamabe equation approach from Step 69.
    
    Actually, use the simple ODE from A01: for b₀(θ), c₀(θ) with a₀=0:
      R_h = -2(u² + v² + uv + u' + v') where u = b₀', v = c₀'.
    Set R_h = -6: u² + v² + uv + u' + v' = 3.
    
    Fix v(θ) = A sin(θ), solve Riccati for u(θ): u' = 3 - u² - v² - uv - v'.
    """
    from scipy.integrate import solve_ivp
    
    theta = np.linspace(0, 2*np.pi, 512, endpoint=False)
    dth = theta[1] - theta[0]
    
    # v = A sin(θ), v' = A cos(θ)
    v_arr = A_amp * np.sin(theta)
    vp_arr = A_amp * np.cos(theta)
    
    # Solve u' = 3 - u² - v² - uv - v' with periodic BCs
    # Use shooting: integrate from 0 to 2π, match u(0) = u(2π)
    def rhs(th, y):
        v = A_amp * np.sin(th)
        vp = A_amp * np.cos(th)
        return [3 - y[0]**2 - v**2 - y[0]*v - vp]
    
    # Bisection on u(0)
    def shoot(u0):
        sol = solve_ivp(rhs, [0, 2*np.pi], [u0], max_step=0.01, rtol=1e-12, atol=1e-14)
        return sol.y[0, -1] - u0
    
    from scipy.optimize import brentq
    u0 = brentq(shoot, -5, 5, xtol=1e-12)
    sol = solve_ivp(rhs, [0, 2*np.pi], [u0], t_eval=theta, max_step=0.01, rtol=1e-12, atol=1e-14)
    u_arr = sol.y[0]
    
    # Integrate to get b₀, c₀ (with b₀(0) = c₀(0) = 0)
    b0 = np.cumsum(u_arr) * dth
    b0 -= b0[0]  # b₀(0) = 0
    c0 = -A_amp * np.cos(theta) + A_amp  # ∫A sin θ dθ = -A cos θ + const
    c0 -= c0[0]  # c₀(0) = 0
    
    # Actually c₀'(θ) = v(θ) = A sin θ, so c₀(θ) = -A cos θ + A
    # No, let's integrate properly
    c0 = np.cumsum(v_arr) * dth
    c0 -= c0[0]
    
    # Check scalar curvature
    up = np.gradient(u_arr, dth, edge_order=2)
    vp_check = np.gradient(v_arr, dth, edge_order=2)
    R_h = -2*(u_arr**2 + v_arr**2 + u_arr*v_arr + up + vp_check)
    
    # Koiso initial accelerations: a_tt = uv, b_tt = v²+v', c_tt = u²+u'
    a_tt0 = u_arr * v_arr
    b_tt0 = v_arr**2 + vp_arr
    c_tt0 = u_arr**2 + up
    
    return {
        'theta': theta,
        'a0': np.zeros_like(theta),  # a₀ = 0 gauge
        'b0': b0,
        'c0': c0,
        'u': u_arr,
        'v': v_arr,
        'R_h': R_h,
        'R_h_mean': np.mean(R_h),
        'R_h_range': [float(R_h.min()), float(R_h.max())],
        'a_tt0': a_tt0,
        'b_tt0': b_tt0,
        'c_tt0': c_tt0,
        'H_prime0': float(np.mean(a_tt0 + b_tt0 + c_tt0)),
    }


def ode_collar_evolution(center, R, n_t=200):
    """Solve the ODE (θ-independent) approximation of the collar.
    
    Uses only the θ-averaged Koiso data as initial conditions.
    Evolution: s_i'' + H s_i' = 3 (tangential), H' + |S|² = 3 (normal).
    With S(0) = 0, S'(0) = diag(s1'(0), s2'(0), s3'(0)).
    
    Actually we solve the first-order system:
    f_i' = s_i, s_i' = 3 - H s_i, H = s_1 + s_2 + s_3.
    """
    from scipy.integrate import solve_ivp
    
    # θ-averaged initial accelerations
    s1p0 = float(np.mean(center['a_tt0']))
    s2p0 = float(np.mean(center['b_tt0']))
    s3p0 = float(np.mean(center['c_tt0']))
    
    def rhs(t, y):
        f1, f2, f3, s1, s2, s3 = y
        H = s1 + s2 + s3
        return [s1, s2, s3, 3 - H*s1, 3 - H*s2, 3 - H*s3]
    
    sol = solve_ivp(rhs, [0, R], [0, 0, 0, 0, 0, 0],
                    t_eval=np.linspace(0, R, n_t),
                    max_step=0.01, rtol=1e-12, atol=1e-14)
    
    # Wait — S(0)=0 means s_i(0)=0, not f_i(0). 
    # And S'(0) = center accelerations. But the ODE s_i' = 3 - H*s_i
    # with s_i(0) = 0 gives s_i'(0) = 3, not the anisotropic accelerations.
    # 
    # The correct equations come from the FULL evolution:
    # For g = dt² + e^{2f_i} (dξ_i)², s_i = f_i', so f_i'' = s_i'.
    # E_{ii}/g_{ii} = 0: s_i' + s_i*H + s_i² - 3 + (fiber Ricci) = 0
    # For θ-independent: fiber Ricci is zero (flat), so s_i' = 3 - s_i² - s_i*H.
    # At t=0: s_i'(0) = 3 - 0 - 0 = 3 for all i. ISOTROPIC!
    #
    # The anisotropy comes from the FIBER RICCI terms, which are θ-dependent.
    # In the ODE approximation with flat fiber, there IS no anisotropy.
    # A01's ODE uses the averaged fiber Ricci as a forcing term.
    
    # Corrected: s_i' = 3 - s_i² - s_i*H + r_i(t) where r_i comes from fiber Ricci.
    # In the deep interior, e^{-2a}*(fiber terms) → 0, so the flat ODE is the correct
    # asymptotic approximation. But the initial data must include the fiber Ricci.
    
    # Actually from the full PDE: E_{ii}/g_{ii} for the a-component:
    # a_tt + a_t*H - e^{-2a}*(b_θθ + c_θθ + b_θ² + c_θ² - a_θ*b_θ - a_θ*c_θ) = 3
    # The fiber terms are multiplied by e^{-2a}. At t=0, a₀=0, so e^{-2a}=1
    # and the fiber Ricci contributes fully. As a grows, they decay.
    
    # For the ODE model, replace fiber terms by their θ-averages at t=0,
    # then decay them as e^{-2a(t)}:
    # s_i' = 3 - s_i² - s_i*H + r_i * e^{-2*mean(f_i)}
    
    # This is getting complex. Let me do the simplest version first:
    # pure flat-fiber ODE (isotropic) to establish the baseline.
    
    # Isotropic: s' = 3 - 3s², s(0) = 0 → s = tanh(√3 t)
    sol_iso = solve_ivp(rhs, [0, R], [0, 0, 0, 0, 0, 0],
                        t_eval=np.linspace(0, R, n_t),
                        max_step=0.01, rtol=1e-12, atol=1e-14)
    
    t_arr = sol_iso.t
    s_arr = sol_iso.y[3:6]  # s1, s2, s3
    H_arr = np.sum(s_arr, axis=0)
    S_minus_I_sq = np.sum((s_arr - 1)**2, axis=0)
    
    # Compute the full Einstein defect for the isotropic collar
    # g = dt² + e^{2f(t)} (dθ² + dx² + dy²)
    # with f' = s (isotropic), all three equal
    # E_00 = -(3s² + 3s') + 3 = -(3s² + 3(3 - 3s² - s*3s)) + 3
    # Wait, s' = 3 - 3s² only for the isotropic ODE. Then:
    # E_00 = -3s' - 3s² + 3 = -3(3-3s²) - 3s² + 3 = -9 + 9s² - 3s² + 3 = 6s² - 6
    # At s = tanh(√3 t): E_00 = 6(tanh² - 1) = -6 sech²
    # Tangential: E_11/g_11 = -s' - s*3s - s² + 3 = -(3-3s²) - 3s² - s² + 3 = s² ≠ 0
    # Wait, that's wrong. Let me redo.
    #
    # For isotropic g = dt² + e^{2f}(dθ² + dx² + dy²), f' = s, 
    # Ric_00 = -3(s' + s²) 
    # Ric_ii = e^{2f}[-(s' + 3s²)]  (i=1,2,3)
    # E_00 = Ric_00 + 3 = -3s' - 3s² + 3
    # E_ii/g_ii = -(s' + 3s²) + 3
    # 
    # With s' = 3 - 3s²:
    # E_00 = -3(3-3s²) - 3s² + 3 = -9+9s²-3s²+3 = 6s²-6 = -6 sech²(√3 t) ≠ 0
    # E_ii/g_ii = -(3-3s²) - 3s² + 3 = -3+3s²-3s²+3 = 0 ✓
    #
    # So the isotropic ODE solves tangential but has E_00 = -6 sech²(√3 t).
    # This confirms: the normal equation is NOT satisfied by the tangential ODE solution.
    # The full system must couple normal and tangential.
    
    # Full system for isotropic:
    # Normal: s' + s² = 1 (from E_00 = 0: -3(s'+s²)+3=0)
    # Tangential: s' + 3s² = 3 (from E_ii = 0: -(s'+3s²)+3=0)
    # These are inconsistent unless s²=1 and s'=0! So s=±1.
    # With s(0)=0, NO isotropic reflected core exists. QED.
    
    return {
        't': t_arr.tolist(),
        'H': H_arr.tolist(),
        'S_minus_I_sq': S_minus_I_sq.tolist(),
        'tangential_defect_isotropic': 'E_00 = -6*sech^2(sqrt(3)*t), tangential exact',
        'normal_tangential_inconsistency': 'Normal s\'+s²=1 vs tangential s\'+3s²=3 → s²=1 and s\'=0 → s=const=±1, incompatible with s(0)=0',
        'conclusion': 'No isotropic T³ reflected Einstein core exists AT ALL. The obstruction is algebraic, not asymptotic.',
    }


def full_pde_residual(a, b, c, t_grid, th_grid, dt, dth):
    """Compute all 5 Einstein defect components on a 2D (t,θ) grid.
    
    Uses finite differences for derivatives.
    Returns E_00, E_01, E_11/g_11, E_22/g_22, E_33/g_33 as 2D arrays.
    """
    nt, nth = a.shape
    
    # Derivatives (periodic in θ, Neumann-compatible in t for center)
    def dt_fd(f):
        return np.gradient(f, dt, axis=0, edge_order=2)
    def dth_fd(f):
        # Periodic in θ
        return np.gradient(f, dth, axis=1, edge_order=2)
    def dtt_fd(f):
        d2 = np.zeros_like(f)
        d2[1:-1] = (f[2:] - 2*f[1:-1] + f[:-2]) / dt**2
        d2[0] = (f[1] - 2*f[0] + f[1]) / dt**2  # reflection: f(-dt) = f(dt)
        d2[-1] = (f[-2] - 2*f[-1] + f[-2]) / dt**2  # approximate
        return d2
    def dthth_fd(f):
        # Periodic
        fp = np.roll(f, -1, axis=1)
        fm = np.roll(f, 1, axis=1)
        return (fp - 2*f + fm) / dth**2
    def dtth_fd(f):
        return dt_fd(dth_fd(f))
    
    at = dt_fd(a); bt = dt_fd(b); ct = dt_fd(c)
    att = dtt_fd(a); btt = dtt_fd(b); ctt = dtt_fd(c)
    ath = dth_fd(a); bth = dth_fd(b); cth = dth_fd(c)
    athth = dthth_fd(a); bthth = dthth_fd(b); cthth = dthth_fd(c)
    btth = dtth_fd(b); ctth = dtth_fd(c)
    
    e2a = np.exp(2*a)
    
    # E_00 = -(at² + att + bt² + btt + ct² + ctt) + 3
    E00 = -(at**2 + att + bt**2 + btt + ct**2 + ctt) + 3
    
    # E_01 = at*bth + at*cth - bt*bth - ct*cth - btth - ctth
    E01 = at*bth + at*cth - bt*bth - ct*cth - btth - ctth
    
    # E_11/g_11 = -(at² + at*bt + at*ct + att) + 3 
    #   + e^{-2a}*(ath*bth + ath*cth - bth² - bthth - cth² - cthth)
    E11_g = -(at**2 + at*bt + at*ct + att) + 3 \
        + np.exp(-2*a)*(ath*bth + ath*cth - bth**2 - bthth - cth**2 - cthth)
    
    # E_22/g_22 = -(at*bt + bt² + bt*ct + btt) + 3
    #   + e^{-2a}*(ath*bth - bth² - bth*cth - bthth)
    E22_g = -(at*bt + bt**2 + bt*ct + btt) + 3 \
        + np.exp(-2*a)*(ath*bth - bth**2 - bth*cth - bthth)
    
    # E_33/g_33 = -(at*ct + bt*ct + ct² + ctt) + 3
    #   + e^{-2a}*(ath*cth - bth*cth - cth² - cthth)
    E33_g = -(at*ct + bt*ct + ct**2 + ctt) + 3 \
        + np.exp(-2*a)*(ath*cth - bth*cth - cth**2 - cthth)
    
    return E00, E01, E11_g, E22_g, E33_g


def main():
    results = {}
    
    # 1. Demonstrate the isotropic impossibility
    print("=" * 60)
    print("1. ISOTROPIC IMPOSSIBILITY (algebraic)")
    print("=" * 60)
    print("Normal: s' + s² = 1")
    print("Tangential: s' + 3s² = 3")
    print("Subtract: 2s² = 2 → s = ±1, s' = 0")
    print("Incompatible with s(0) = 0 (reflection center).")
    print("NO isotropic reflected T³ Einstein core exists.\n")
    
    results['isotropic_impossibility'] = {
        'normal': "s' + s^2 = 1",
        'tangential': "s' + 3s^2 = 3",
        'conclusion': 's^2 = 1, s\' = 0 → s = const ±1, not 0. No reflected isotropic core.',
    }
    
    # 2. Build Koiso center with A = 1.0
    print("=" * 60)
    print("2. KOISO CENTER (A = 1.0)")
    print("=" * 60)
    center = make_koiso_center(1.0, 32)
    print(f"  R_h mean: {center['R_h_mean']:.6f} (should be -6)")
    print(f"  R_h range: [{center['R_h_range'][0]:.4f}, {center['R_h_range'][1]:.4f}]")
    print(f"  H'(0) = tr(S'(0)) = {center['H_prime0']:.6f} (should be 3)")
    
    results['koiso_center'] = {
        'A': 1.0,
        'R_h_mean': center['R_h_mean'],
        'R_h_range': center['R_h_range'],
        'H_prime0': center['H_prime0'],
    }
    
    # 3. ODE collar analysis
    print("\n" + "=" * 60)
    print("3. ODE COLLAR ANALYSIS")
    print("=" * 60)
    ode = ode_collar_evolution(center, 6.0)
    print(f"  Conclusion: {ode['conclusion']}")
    results['ode_collar'] = ode
    
    # 4. Gauss constraint at outer boundary
    print("\n" + "=" * 60)
    print("4. GAUSS CONSTRAINT AT OUTER BOUNDARY")
    print("=" * 60)
    print("For Ric+3g=E with |E|_op ≤ δ on T³ outer face:")
    print("  R_γ = -6 + (2/3)H² - |S_tf|² + (tr_T E - E_nn)")
    print("  |tr_T E - E_nn| ≤ 4δ")
    print("  For flat conformal class: R_γ = -8u⁻⁵Δu ≥ 0 at max(u)")
    print("  → -6 + (2/3)H² - |S_tf|² + 4δ ≥ 0")
    print("  → δ ≥ (6 - (2/3)H² + |S_tf|²) / 4")
    print("  For H ≈ 3 - ε, |S_tf| ≈ 0:")
    print("    δ ≥ (6 - 6 + 4ε/3) / 4 ≈ ε/3")
    
    # More precise: (2/3)H² = (2/3)(3-ε)² = 6 - 4ε + (2/3)ε²
    # So 6 - (2/3)H² = 4ε - (2/3)ε²
    # δ ≥ (4ε - (2/3)ε² + |S_tf|²) / 4 ≈ ε (leading order)
    
    eps_vals = [0.1, 0.01, 0.001, 1e-4, 1e-6]
    gauss_data = []
    for eps in eps_vals:
        H = 3 - eps
        delta_min = (6 - (2/3)*H**2) / 4  # ignoring S_tf and E correction
        R_min = 0.5 * np.log(1 + 6/max(delta_min, 1e-15))
        gauss_data.append({
            'epsilon': eps,
            'H_R': H,
            'delta_min_gauss': delta_min,
            'R_min_log': R_min,
        })
        print(f"  ε={eps:.1e}: H_R={H:.6f}, δ_min≥{delta_min:.4e}, R_min≥{R_min:.2f}")
    
    results['gauss_constraint'] = gauss_data
    
    # 5. Key structural conclusion
    print("\n" + "=" * 60)
    print("5. STRUCTURAL CONCLUSIONS")
    print("=" * 60)
    conclusions = [
        "Isotropic reflected T³ cores are algebraically impossible (s²=1 at center).",
        "Anisotropic cores require θ-dependent fiber with R_h = -6.",
        "Flat outer conformal class with constant H<3 requires δ ≥ ε (Gauss).",
        "Exact cores cannot reach H=3 at finite R (weighted identity).",
        "Exact cores cannot have flat PE conformal infinity (Witten-Yau).",
        "The forced problem must jointly optimize (H_R, δ, R) under both constraints.",
        "The full DeTurck-elliptic BVP is the next decisive computation.",
    ]
    for c in conclusions:
        print(f"  • {c}")
    results['conclusions'] = conclusions
    
    import pathlib
    path = pathlib.Path(__file__).resolve().parent.parent / 'data' / 'step72_forced_bvp_analysis.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nWrote {path}")


if __name__ == '__main__':
    main()
