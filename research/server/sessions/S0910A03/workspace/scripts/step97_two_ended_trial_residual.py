"""
Step 97: Two-ended trial metric with charged Koiso center.

Build a concrete piecewise trial metric on [0, R] × S¹ (symmetric about n=0),
compute its full 4D Ricci residual E = Ric + 3g in the Gaussian frame, and
analyze the residual dependence on shared center parameters.

The trial metric smoothly interpolates from the charged Koiso separator data
(Steps 92-96) at n=0 to an expanding round cusp at n=R.  The interpolation
is in quotient fields (σ, α, a, connection), not in the 3×3 matrix directly.
The transition region is where the residual concentrates.

Output: per-parameter residual profiles, block decomposition, and critical
projections.
"""
from __future__ import annotations
import json, math, importlib.util
from pathlib import Path
import numpy as np

# Import the Koiso evolution module for center data and Ricci computation
p = Path('workspace/scripts/step96_koiso_einstein_cauchy_evolution.py')
spec = importlib.util.spec_from_file_location('evol', p)
evol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evol)

L = 2 * math.pi
# =============================================================
# Transition sigmoid
# =============================================================
def sigmoid(n, n_c, eps):
    """Smooth transition: 1 at n=0, 0 at n>>n_c."""
    x = np.clip((n - n_c) / eps, -20, 20)
    return 0.5 * (1 - np.tanh(x))

def dsigmoid(n, n_c, eps):
    """First derivative of sigmoid."""
    x = np.clip((n - n_c) / eps, -20, 20)
    return -0.5 / (eps * np.cosh(x)**2)

def d2sigmoid(n, n_c, eps):
    """Second derivative of sigmoid."""
    x = np.clip((n - n_c) / eps, -20, 20)
    c = np.cosh(x)
    return np.tanh(x) / (eps**2 * c**2)

# =============================================================
# Build Koiso center data
# =============================================================
def koiso_center(Ns, wind, S, Qmax):
    """Generate center separator data and extract quotient fields."""
    s, q0, k0, meta = evol.initial_data(Ns, wind, S, Qmax)
    # Extract orbit matrix and connection rate
    G0 = q0[:, 1:, 1:]  # orbit metric (Ns, 2, 2)
    Gi0 = np.linalg.inv(G0)
    rho0 = np.sqrt(np.linalg.det(G0))
    sigma0 = np.log(rho0)
    # alpha: for diagonal orbit, G11 = exp(sigma+alpha), G22 = exp(sigma-alpha)
    alpha0 = 0.5 * (np.log(G0[:, 0, 0]) - np.log(G0[:, 1, 1]))
    # Connection rate from K: K[0,a] = k0[0,a], so dv/dn = 2*K[0,a]
    v_rate = 2 * k0[:, 0, 1:]  # (Ns, 2): rate of v_a = q_{0a}
    # Physical charge Q at center
    f0 = np.einsum('nij,nj->ni', Gi0, k0[:, 0, 1:])  # connection derivative f=An/a
    Q0 = 0.5 * np.einsum('ni,nij,nj->n', f0, G0, f0)
    return {
        's': s, 'q0': q0, 'k0': k0, 'meta': meta,
        'G0': G0, 'alpha0': alpha0, 'sigma0': sigma0,
        'v_rate': v_rate, 'Q0': Q0, 'f0': f0
    }

# =============================================================
# Build trial metric on [0, R] × S¹
# =============================================================
def build_trial(Nn, Ns, R, n_c, eps, wind, S, Qmax):
    """
    Build q(n,s) by smooth field interpolation.
    Returns: n_grid, s_grid, q[Nn,Ns,3,3], center_data dict
    """
    cd = koiso_center(Ns, wind, S, Qmax)
    n_grid = np.linspace(0, R, Nn)
    s_grid = cd['s']
    alpha0 = cd['alpha0']  # (Ns,)
    v_rate = cd['v_rate']  # (Ns, 2)

    q = np.zeros((Nn, Ns, 3, 3))
    for j, nv in enumerate(n_grid):
        ch = sigmoid(nv, n_c, eps)
        # Quotient fields
        sigma_n = 2 * nv * (1 - ch)
        alpha_n = alpha0 * ch
        log_a_n = nv * (1 - ch)
        a_n = np.exp(log_a_n)
        # Connection potential v_a = v_rate_a * n * chi(n)
        v = v_rate * nv * ch  # (Ns, 2)
        # Orbit metric G = diag(exp(sigma+alpha), exp(sigma-alpha))
        G11 = np.exp(sigma_n + alpha_n)
        G22 = np.exp(sigma_n - alpha_n)
        # Build q
        q[j, :, 0, 0] = a_n**2 + (v[:, 0]**2 / G11 + v[:, 1]**2 / G22)
        q[j, :, 1, 1] = G11
        q[j, :, 2, 2] = G22
        q[j, :, 0, 1] = v[:, 0]
        q[j, :, 1, 0] = v[:, 0]
        q[j, :, 0, 2] = v[:, 1]
        q[j, :, 2, 0] = v[:, 1]
    return n_grid, s_grid, q, cd

# =============================================================
# Compute Ricci residual in Gaussian frame
# =============================================================
def compute_residual(n_grid, q):
    """
    Compute E_T, E_nn, and E_mom for g = dn² + q(n,s).
    Uses centered finite differences in n and spectral in s.
    Returns dicts with residual fields.
    """
    Nn, Ns = q.shape[0], q.shape[1]
    dn = n_grid[1] - n_grid[0]

    # K = 1/2 dq/dn by centered FD
    K = np.zeros_like(q)
    K[1:-1] = (q[2:] - q[:-2]) / (4 * dn)
    K[0] = (-3*q[0] + 4*q[1] - q[2]) / (4*dn)
    K[-1] = (3*q[-1] - 4*q[-2] + q[-3]) / (4*dn)

    # K_n = dK/dn
    Kn = np.zeros_like(q)
    Kn[1:-1] = (K[2:] - K[:-2]) / (2*dn)
    Kn[0] = (-3*K[0] + 4*K[1] - K[2]) / (2*dn)
    Kn[-1] = (3*K[-1] - 4*K[-2] + K[-3]) / (2*dn)

    qi = np.linalg.inv(q)
    W = np.einsum('nsij,nsjk->nsik', qi, K)
    H = np.trace(W, axis1=-2, axis2=-1)   # (Nn, Ns)
    W2 = np.einsum('nsij,nsji->ns', W, W)  # |W|²
    KqiK = np.einsum('nsij,nsjk,nskl->nsil', K, qi, K)

    # 3D Ric at each n-slice
    ric = np.zeros_like(q)
    scalar = np.zeros((Nn, Ns))
    for j in range(Nn):
        _, r_j, sc_j = evol.christoffel_and_ricci(q[j])
        ric[j] = r_j
        scalar[j] = sc_j

    # Tangential residual E_T = Ric(q) + 3q - K_n - H*K + 2*K*qi*K
    E_T = ric + 3*q - Kn - H[:,:,None,None]*K + 2*KqiK

    # Normal residual E_nn = -(H_n + |W|²) + 3
    Hn = np.zeros_like(H)
    Hn[1:-1] = (H[2:] - H[:-2]) / (2*dn)
    Hn[0] = (-3*H[0] + 4*H[1] - H[2]) / (2*dn)
    Hn[-1] = (3*H[-1] - 4*H[-2] + H[-3]) / (2*dn)
    E_nn = -(Hn + W2) + 3

    # Operator norms: tangential block
    E_T_op = np.zeros((Nn, Ns))
    for j in range(Nn):
        for k in range(Ns):
            qiE = qi[j, k] @ E_T[j, k]
            E_T_op[j, k] = np.max(np.abs(np.linalg.eigvalsh(
                0.5*(qiE + qiE.T))))

    return {
        'K': K, 'Kn': Kn, 'W': W, 'H': H, 'W2': W2,
        'ric3': ric, 'scalar': scalar,
        'E_T': E_T, 'E_nn': E_nn, 'Hn': Hn,
        'E_T_op': E_T_op,
    }

# =============================================================
# Extract quotient-level residual decomposition
# =============================================================
def quotient_decomposition(n_grid, q, res):
    """Decompose residual into area, orbit-shape, base, and charge blocks."""
    Nn, Ns = q.shape[:2]
    qi = np.linalg.inv(q)
    # Extract orbit and base blocks from E_T
    E_orbit = res['E_T'][:, :, 1:, 1:]  # (Nn, Ns, 2, 2)
    E_base  = res['E_T'][:, :, 0, 0]    # (Nn, Ns) scalar
    E_mixed = res['E_T'][:, :, 0, 1:]   # (Nn, Ns, 2) charge-related

    # Orbit trace = area residual component, orbit traceless = shape residual
    G = q[:, :, 1:, 1:]
    Gi = np.linalg.inv(G)
    E_area_trace = np.einsum('nsij,nsij->ns', Gi, E_orbit)  # tr(G⁻¹ E_orbit)
    E_shape_norm = np.zeros((Nn, Ns))
    for j in range(Nn):
        for k in range(Ns):
            GiE = Gi[j, k] @ E_orbit[j, k]
            traceless = GiE - 0.5 * np.trace(GiE) * np.eye(2)
            E_shape_norm[j, k] = np.sqrt(np.sum(traceless**2))

    E_charge_norm = np.sqrt(np.sum(E_mixed**2, axis=-1))

    return {
        'E_area_trace': E_area_trace,
        'E_shape_norm': E_shape_norm,
        'E_base_scalar': E_base,
        'E_charge_norm': E_charge_norm,
        'E_nn': res['E_nn'],
    }

# =============================================================
# Run trial for multiple parameter choices
# =============================================================
def run_trial(Nn, Ns, R, n_c, eps, wind, S, Qmax):
    """Run one trial and return summary."""
    n_grid, s_grid, q, cd = build_trial(Nn, Ns, R, n_c, eps, wind, S, Qmax)
    res = compute_residual(n_grid, q)
    qd = quotient_decomposition(n_grid, q, res)

    # Profile: max over s at each n
    ET_profile = res['E_T_op'].max(axis=1)
    Enn_profile = np.abs(res['E_nn']).max(axis=1)
    total_profile = np.maximum(ET_profile, Enn_profile)

    # Block profiles
    area_profile = np.abs(qd['E_area_trace']).max(axis=1)
    shape_profile = qd['E_shape_norm'].max(axis=1)
    base_profile = np.abs(qd['E_base_scalar']).max(axis=1)
    charge_profile = qd['E_charge_norm'].max(axis=1)

    # Peak location and value
    peak_idx = np.argmax(total_profile[2:-2]) + 2
    peak_n = float(n_grid[peak_idx])
    peak_val = float(total_profile[peak_idx])

    # Integrated L² residual (volume-weighted)
    dn = n_grid[1] - n_grid[0]
    det_q = np.linalg.det(q)
    vol_density = np.sqrt(np.maximum(det_q, 1e-30))  # sqrt(det q)
    L2_integrand = res['E_T_op']**2 * vol_density  # simplified
    L2_total = float(np.sum(L2_integrand) * dn * (2*math.pi/Ns))

    return {
        'params': {'S': S, 'Qmax': Qmax, 'n_c': n_c, 'eps': eps,
                   'R': R, 'wind': wind, 'Nn': Nn, 'Ns': Ns},
        'residual_sup': {
            'total_max': float(total_profile.max()),
            'ET_max': float(ET_profile.max()),
            'Enn_max': float(Enn_profile.max()),
            'peak_n': peak_n,
            'peak_value': peak_val,
        },
        'block_peaks': {
            'area': float(area_profile.max()),
            'shape': float(shape_profile.max()),
            'base': float(base_profile.max()),
            'charge': float(charge_profile.max()),
        },
        'profiles': {
            'n': [float(x) for x in n_grid[::10]],
            'total': [float(x) for x in total_profile[::10]],
            'area': [float(x) for x in area_profile[::10]],
            'shape': [float(x) for x in shape_profile[::10]],
            'base': [float(x) for x in base_profile[::10]],
            'charge': [float(x) for x in charge_profile[::10]],
            'Enn': [float(x) for x in Enn_profile[::10]],
        },
        'L2_total': L2_total,
        'center_data': {
            'Q_range': [float(cd['Q0'].min()), float(cd['Q0'].max())],
            'alpha0_range': [float(cd['alpha0'].min()), float(cd['alpha0'].max())],
        }
    }


def main():
    Nn = 201
    Ns = 64
    R = 4.0
    wind = 1

    print("=" * 70)
    print("STEP 97: TWO-ENDED TRIAL METRIC WITH CHARGED KOISO CENTER")
    print("=" * 70)

    # Phase 1: Baseline trial
    print("\n--- Phase 1: Baseline trial (S=1, Qmax=0.5, n_c=1.5, eps=0.6) ---")
    baseline = run_trial(Nn, Ns, R, 1.5, 0.6, wind, 1.0, 0.5)
    print(f"  Total residual sup: {baseline['residual_sup']['total_max']:.6f}")
    print(f"  Peak at n = {baseline['residual_sup']['peak_n']:.3f}")
    print(f"  Blocks: area={baseline['block_peaks']['area']:.4f}, "
          f"shape={baseline['block_peaks']['shape']:.4f}, "
          f"base={baseline['block_peaks']['base']:.4f}, "
          f"charge={baseline['block_peaks']['charge']:.4f}")

    # Phase 2: Parameter sweep over S
    print("\n--- Phase 2: Center energy sweep (S varies) ---")
    S_vals = [0.3, 0.5, 1.0, 1.5, 2.0, 2.5]
    S_results = []
    for S in S_vals:
        Qm = min(0.5, S * 0.5)  # keep Q < S
        r = run_trial(Nn, Ns, R, 1.5, 0.6, wind, S, Qm)
        S_results.append(r)
        print(f"  S={S:.1f}, Qmax={Qm:.2f}: peak={r['residual_sup']['total_max']:.4f} "
              f"at n={r['residual_sup']['peak_n']:.2f}, "
              f"area={r['block_peaks']['area']:.4f}, shape={r['block_peaks']['shape']:.4f}")

    # Phase 3: Transition parameter sweep
    print("\n--- Phase 3: Transition sweep (n_c, eps vary) ---")
    trans_results = []
    for n_c in [0.8, 1.2, 1.5, 2.0, 2.5]:
        for eps_v in [0.3, 0.5, 0.8]:
            r = run_trial(Nn, Ns, R, n_c, eps_v, wind, 1.0, 0.5)
            trans_results.append(r)
            print(f"  n_c={n_c:.1f}, eps={eps_v:.1f}: peak={r['residual_sup']['total_max']:.4f} "
                  f"at n={r['residual_sup']['peak_n']:.2f}")

    # Phase 4: Sensitivity analysis
    print("\n--- Phase 4: Sensitivity (dF/dS, dF/dQmax at baseline) ---")
    dS = 0.05
    r_plus  = run_trial(Nn, Ns, R, 1.5, 0.6, wind, 1.0+dS, 0.5)
    r_minus = run_trial(Nn, Ns, R, 1.5, 0.6, wind, 1.0-dS, 0.5)
    dF_dS = (r_plus['residual_sup']['total_max'] - r_minus['residual_sup']['total_max']) / (2*dS)
    print(f"  dF_sup/dS ≈ {dF_dS:.6f}")

    dQ = 0.02
    r_pQ = run_trial(Nn, Ns, R, 1.5, 0.6, wind, 1.0, 0.5+dQ)
    r_mQ = run_trial(Nn, Ns, R, 1.5, 0.6, wind, 1.0, 0.5-dQ)
    dF_dQ = (r_pQ['residual_sup']['total_max'] - r_mQ['residual_sup']['total_max']) / (2*dQ)
    print(f"  dF_sup/dQmax ≈ {dF_dQ:.6f}")

    # Which block is most sensitive?
    dArea_dS = (r_plus['block_peaks']['area'] - r_minus['block_peaks']['area']) / (2*dS)
    dShape_dS = (r_plus['block_peaks']['shape'] - r_minus['block_peaks']['shape']) / (2*dS)
    dBase_dS = (r_plus['block_peaks']['base'] - r_minus['block_peaks']['base']) / (2*dS)
    dCharge_dS = (r_plus['block_peaks']['charge'] - r_minus['block_peaks']['charge']) / (2*dS)
    print(f"  Block sensitivities to S: area={dArea_dS:.4f}, shape={dShape_dS:.4f}, "
          f"base={dBase_dS:.4f}, charge={dCharge_dS:.4f}")

    # Phase 5: Best achievable residual with optimization
    print("\n--- Phase 5: Grid search for minimum peak residual ---")
    best = None
    for n_c in np.linspace(0.5, 3.0, 11):
        for eps_v in np.linspace(0.2, 1.0, 5):
            for S in [0.5, 1.0, 1.5, 2.0]:
                Qm = min(0.5, S*0.5)
                r = run_trial(Nn, Ns, R, n_c, eps_v, wind, S, Qm)
                pk = r['residual_sup']['total_max']
                if best is None or pk < best['residual_sup']['total_max']:
                    best = r
    print(f"  Best peak: {best['residual_sup']['total_max']:.6f}")
    print(f"  At S={best['params']['S']}, Qmax={best['params']['Qmax']}, "
          f"n_c={best['params']['n_c']:.2f}, eps={best['params']['eps']:.2f}")
    print(f"  Blocks: area={best['block_peaks']['area']:.4f}, "
          f"shape={best['block_peaks']['shape']:.4f}, "
          f"base={best['block_peaks']['base']:.4f}, "
          f"charge={best['block_peaks']['charge']:.4f}")

    # Save results
    output = {
        'baseline': baseline,
        'S_sweep': S_results,
        'transition_sweep': trans_results[:6],  # keep compact
        'sensitivity': {
            'dF_sup_dS': dF_dS, 'dF_sup_dQmax': dF_dQ,
            'block_sens_S': {'area': dArea_dS, 'shape': dShape_dS,
                            'base': dBase_dS, 'charge': dCharge_dS},
        },
        'best_found': best,
        'interpretation': (
            "The trial metric interpolates between a charged Koiso center and "
            "an expanding round cusp via a smooth sigmoid in quotient fields. "
            "The residual concentrates in the transition region. The block "
            "decomposition shows which geometric mismatches dominate. "
            "Parameter sensitivities indicate which shared center data affect "
            "the residual and which blocks resist parameter variations."
        ),
    }
    path = Path('workspace/data/step97_two_ended_trial_residual.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, indent=2), encoding='utf-8')
    print(f"\nwrote {path}")


if __name__ == '__main__':
    main()
