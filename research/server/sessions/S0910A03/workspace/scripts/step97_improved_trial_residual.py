"""
Step 97 Part 2: Improved trial metric using the radial ODE backbone.

The radial (s-independent, round-orbit, zero-twist) Einstein system on [0,R]:
  sigma'' = 6 - sigma'^2 - sigma'*u     [area ODE]
  u' = 3 - u^2 - sigma'*u              [base ODE, u=a'/a]
  sigma(0)=0, sigma'(0)=0, u(0)=0

is a 2D autonomous system whose cusp equilibrium (sigma'=2, u=1, H=3) is
a stable attractor.  Solving it exactly removes the dominant area/base
interpolation error and isolates the genuine s-dependent geometric mismatch.

On top of this backbone, the s-dependent Koiso perturbation (orbit shape
alpha(s), charge Q(s)) is smoothly added and the residual is measured.
"""
from __future__ import annotations
import json, math, importlib.util
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

# Import Koiso evolution module
p = Path('workspace/scripts/step96_koiso_einstein_cauchy_evolution.py')
spec = importlib.util.spec_from_file_location('evol', p)
evol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evol)

L = 2 * math.pi

# =============================================================
# Radial backbone ODE
# =============================================================
def radial_backbone(R, npts=2001):
    """Solve the round-orbit radial ODE from center to R."""
    def rhs(n, y):
        sp, u = y  # sigma', a'/a
        return [6 - sp*sp - sp*u,
                3 - u*u - sp*u]
    sol = solve_ivp(rhs, [0, R], [0, 0], method='DOP853',
                    dense_output=True, rtol=1e-12, atol=1e-14)
    n_dense = np.linspace(0, R, npts)
    y_dense = sol.sol(n_dense)
    sp = y_dense[0]  # sigma'
    u  = y_dense[1]  # a'/a
    # Integrate sigma, log a
    dn = n_dense[1] - n_dense[0]
    sigma = np.cumsum(sp) * dn  # trapezoidal is fine at this resolution
    sigma[0] = 0
    sigma = np.concatenate([[0], np.cumsum(0.5*(sp[:-1]+sp[1:])) * dn])
    log_a = np.concatenate([[0], np.cumsum(0.5*(u[:-1]+u[1:])) * dn])
    a = np.exp(log_a)
    H = sp + u  # mean curvature
    return n_dense, sigma, sp, u, a, H

# =============================================================
# Smooth sigmoid for orbit perturbation
# =============================================================
def sigmoid(n, n_c, eps):
    x = np.clip((n - n_c) / eps, -20, 20)
    return 0.5 * (1 - np.tanh(x))

# =============================================================
# Build improved trial metric
# =============================================================
def build_improved_trial(Nn, Ns, R, n_c_pert, eps_pert, wind, S, Qmax):
    """
    Build trial using radial backbone + s-dependent Koiso perturbation.
    """
    # Radial backbone
    n_grid, sigma_r, sp_r, u_r, a_r, H_r = radial_backbone(R, Nn)

    # Koiso center data
    s, q0, k0, meta = evol.initial_data(Ns, wind, S, Qmax)
    G0 = q0[:, 1:, 1:]
    Gi0 = np.linalg.inv(G0)
    alpha0 = 0.5 * (np.log(G0[:, 0, 0]) - np.log(G0[:, 1, 1]))  # orbit shape
    f0 = np.einsum('sij,sj->si', Gi0, k0[:, 0, 1:])  # connection at center
    Q0 = 0.5 * np.einsum('si,sij,sj->s', f0, G0, f0)  # physical charge
    v_rate = 2 * k0[:, 0, 1:]  # dv/dn at center

    # Build q on grid
    q = np.zeros((Nn, Ns, 3, 3))
    for j, nv in enumerate(n_grid):
        ch = sigmoid(nv, n_c_pert, eps_pert)
        # Area: backbone sigma + Q-correction
        # sigma(n,s) = sigma_r(n) + chi(n) * delta_sigma(n,s)
        # where delta_sigma accounts for the Q(s) variation in sigma_nn
        # At center: sigma_nn = 6+Q(s), backbone has sigma_nn=6.
        # Correction: delta_sigma ≈ 0.5*Q(s)*n^2 for small n, dying with chi
        delta_sigma = 0.5 * Q0 * nv**2 * ch * np.exp(-nv)  # bounded
        sigma_n = sigma_r[j] + delta_sigma
        # Orbit shape: alpha(n,s) = alpha0(s) * chi(n)
        alpha_n = alpha0 * ch
        # Base scale: from backbone a(n)
        a_n = a_r[j]
        # Connection: v_a = v_rate_a * n * chi(n)
        v = v_rate * nv * ch  # (Ns, 2)

        # Orbit metric G = diag(exp(sigma+alpha), exp(sigma-alpha))
        G11 = np.exp(sigma_n + alpha_n)
        G22 = np.exp(sigma_n - alpha_n)
        # Slice metric
        q[j, :, 0, 0] = a_n**2 + (v[:, 0]**2 / G11 + v[:, 1]**2 / G22)
        q[j, :, 1, 1] = G11
        q[j, :, 2, 2] = G22
        q[j, :, 0, 1] = v[:, 0]
        q[j, :, 1, 0] = v[:, 0]
        q[j, :, 0, 2] = v[:, 1]
        q[j, :, 2, 0] = v[:, 1]

    return n_grid, s, q, {
        'meta': meta, 'alpha0': alpha0, 'Q0': Q0,
        'backbone': {'sigma': sigma_r, 'sp': sp_r, 'u': u_r, 'a': a_r, 'H': H_r},
    }

# =============================================================
# Compute residual (reuse logic from part 1)
# =============================================================
def compute_residual(n_grid, q):
    Nn, Ns = q.shape[:2]
    dn = n_grid[1] - n_grid[0]

    K = np.zeros_like(q)
    K[1:-1] = (q[2:] - q[:-2]) / (4 * dn)
    K[0] = (-3*q[0] + 4*q[1] - q[2]) / (4*dn)
    K[-1] = (3*q[-1] - 4*q[-2] + q[-3]) / (4*dn)

    Kn = np.zeros_like(q)
    Kn[1:-1] = (K[2:] - K[:-2]) / (2*dn)
    Kn[0] = (-3*K[0] + 4*K[1] - K[2]) / (2*dn)
    Kn[-1] = (3*K[-1] - 4*K[-2] + K[-3]) / (2*dn)

    qi = np.linalg.inv(q)
    W = np.einsum('nsij,nsjk->nsik', qi, K)
    H = np.trace(W, axis1=-2, axis2=-1)
    W2 = np.einsum('nsij,nsji->ns', W, W)
    KqiK = np.einsum('nsij,nsjk,nskl->nsil', K, qi, K)

    ric = np.zeros_like(q)
    scalar = np.zeros((Nn, Ns))
    for j in range(Nn):
        _, r_j, sc_j = evol.christoffel_and_ricci(q[j])
        ric[j] = r_j
        scalar[j] = sc_j

    E_T = ric + 3*q - Kn - H[:,:,None,None]*K + 2*KqiK
    Hn = np.zeros_like(H)
    Hn[1:-1] = (H[2:] - H[:-2]) / (2*dn)
    Hn[0] = (-3*H[0] + 4*H[1] - H[2]) / (2*dn)
    Hn[-1] = (3*H[-1] - 4*H[-2] + H[-3]) / (2*dn)
    E_nn = -(Hn + W2) + 3

    E_T_op = np.zeros((Nn, Ns))
    for j in range(Nn):
        for k in range(Ns):
            qiE = qi[j, k] @ E_T[j, k]
            E_T_op[j, k] = np.max(np.abs(np.linalg.eigvalsh(
                0.5*(qiE + qiE.T))))
    return E_T, E_nn, E_T_op, H, W, W2, ric, scalar

# =============================================================
# Block decomposition
# =============================================================
def block_decomp(q, E_T, E_nn):
    Nn, Ns = q.shape[:2]
    G = q[:, :, 1:, 1:]
    Gi = np.linalg.inv(G)
    # Area trace
    E_orbit = E_T[:, :, 1:, 1:]
    area_tr = np.einsum('nsij,nsij->ns', Gi, E_orbit)
    # Shape norm
    shape_norm = np.zeros((Nn, Ns))
    for j in range(Nn):
        for k in range(Ns):
            GiE = Gi[j, k] @ E_orbit[j, k]
            tless = GiE - 0.5*np.trace(GiE)*np.eye(2)
            shape_norm[j, k] = np.sqrt(np.sum(tless**2))
    # Base
    base_sc = E_T[:, :, 0, 0]
    # Charge
    charge_norm = np.sqrt(np.sum(E_T[:, :, 0, 1:]**2, axis=-1))
    return area_tr, shape_norm, base_sc, charge_norm

# =============================================================
# Main
# =============================================================
def main():
    Nn = 301
    Ns = 64
    R = 6.0

    print("=" * 70)
    print("IMPROVED TRIAL: RADIAL BACKBONE + KOISO PERTURBATION")
    print("=" * 70)

    # Phase 1: Backbone characterization
    n_b, sigma_b, sp_b, u_b, a_b, H_b = radial_backbone(R, 1001)
    print(f"\nBackbone cusp approach: at n=R={R}")
    print(f"  sigma'={sp_b[-1]:.8f} (target 2)")
    print(f"  u=a'/a={u_b[-1]:.8f} (target 1)")
    print(f"  H={H_b[-1]:.8f} (target 3)")
    # Find n where H reaches 2.9
    idx_29 = np.searchsorted(H_b, 2.9)
    print(f"  H reaches 2.9 at n={n_b[idx_29]:.3f}")
    idx_1 = np.searchsorted(H_b, 1.0)
    print(f"  H reaches 1.0 at n={n_b[idx_1]:.3f}")

    # Phase 2: Sweep over perturbation transition
    print("\n--- Phase 2: Perturbation transition sweep ---")
    results = []
    for S in [0.5, 1.0, 1.5, 2.0]:
        for n_c in [0.5, 1.0, 1.5, 2.0]:
            eps = 0.5
            Qm = min(0.4, S*0.4)
            n_grid, s, q, cd = build_improved_trial(Nn, Ns, R, n_c, eps, 1, S, Qm)
            E_T, E_nn, E_T_op, H, W, W2, ric, sc = compute_residual(n_grid, q)
            area, shape, base, charge = block_decomp(q, E_T, E_nn)

            total = np.maximum(E_T_op, np.abs(E_nn))
            peak_idx = np.argmax(total.max(axis=1))
            peak_n = float(n_grid[peak_idx])
            peak_val = float(total.max())

            r = {
                'S': S, 'Qmax': Qm, 'n_c': n_c, 'eps': eps,
                'peak': peak_val, 'peak_n': peak_n,
                'area_peak': float(np.abs(area).max()),
                'shape_peak': float(shape.max()),
                'base_peak': float(np.abs(base).max()),
                'charge_peak': float(charge.max()),
                'Enn_peak': float(np.abs(E_nn).max()),
            }
            results.append(r)
            print(f"  S={S:.1f} n_c={n_c:.1f}: peak={peak_val:.4f} at n={peak_n:.2f}, "
                  f"area={r['area_peak']:.3f}, shape={r['shape_peak']:.3f}, "
                  f"charge={r['charge_peak']:.3f}, Enn={r['Enn_peak']:.3f}")

    # Phase 3: Best case detailed profile
    print("\n--- Phase 3: Detailed profile of best case ---")
    best = min(results, key=lambda r: r['peak'])
    print(f"  Best: S={best['S']}, n_c={best['n_c']}, peak={best['peak']:.6f}")

    n_grid, s, q, cd = build_improved_trial(
        Nn, Ns, R, best['n_c'], best['eps'], 1, best['S'], best['Qmax'])
    E_T, E_nn, E_T_op, H, W, W2, ric, sc = compute_residual(n_grid, q)
    area, shape, base, charge = block_decomp(q, E_T, E_nn)
    total = np.maximum(E_T_op, np.abs(E_nn))

    # Profile at subsampled n values
    stride = max(1, Nn//30)
    profile_n = n_grid[::stride]
    profile_total = total.max(axis=1)[::stride]
    profile_area = np.abs(area).max(axis=1)[::stride]
    profile_shape = shape.max(axis=1)[::stride]
    profile_charge = charge.max(axis=1)[::stride]
    profile_Enn = np.abs(E_nn).max(axis=1)[::stride]
    profile_H = H.mean(axis=1)[::stride]

    print(f"\n  n      total   area    shape   charge  Enn     H_mean")
    for i in range(min(20, len(profile_n))):
        print(f"  {profile_n[i]:.2f}   {profile_total[i]:.4f}  {profile_area[i]:.4f}  "
              f"{profile_shape[i]:.4f}  {profile_charge[i]:.4f}  {profile_Enn[i]:.4f}  "
              f"{profile_H[i]:.4f}")

    # Phase 4: Sensitivity to S at best (n_c, eps)
    print("\n--- Phase 4: Sensitivity to S at best transition ---")
    dS = 0.02
    for pm in [+1, -1]:
        S_test = best['S'] + pm*dS
        Qm_test = min(0.4, S_test*0.4)
        n_grid2, s2, q2, cd2 = build_improved_trial(
            Nn, Ns, R, best['n_c'], best['eps'], 1, S_test, Qm_test)
        E_T2, E_nn2, E_T_op2, _, _, _, _, _ = compute_residual(n_grid2, q2)
        total2 = np.maximum(E_T_op2, np.abs(E_nn2))
        print(f"  S={S_test:.3f}: peak={total2.max():.6f}")

    # Phase 5: Residual as function of R (domain length)
    print("\n--- Phase 5: Residual scaling with R ---")
    for R_test in [2.0, 3.0, 4.0, 5.0, 6.0, 8.0]:
        Nn_test = max(101, int(R_test * 50) + 1)
        n_grid_t, s_t, q_t, cd_t = build_improved_trial(
            Nn_test, Ns, R_test, best['n_c'], best['eps'], 1,
            best['S'], best['Qmax'])
        E_T_t, E_nn_t, E_T_op_t, _, _, _, _, _ = compute_residual(n_grid_t, q_t)
        total_t = np.maximum(E_T_op_t, np.abs(E_nn_t))
        # Also get residual at the expanded end (n=R)
        end_res = float(total_t[-3:].max())
        print(f"  R={R_test:.1f}: peak={total_t.max():.4f}, end={end_res:.6f}")

    # Save
    output = {
        'backbone_cusp': {
            'sigma_prime_at_R': float(sp_b[-1]),
            'u_at_R': float(u_b[-1]),
            'H_at_R': float(H_b[-1]),
            'H_29_n': float(n_b[idx_29]),
            'H_10_n': float(n_b[idx_1]),
        },
        'sweep': results,
        'best': best,
        'best_profile': {
            'n': [float(x) for x in profile_n],
            'total': [float(x) for x in profile_total],
            'area': [float(x) for x in profile_area],
            'shape': [float(x) for x in profile_shape],
            'charge': [float(x) for x in profile_charge],
            'Enn': [float(x) for x in profile_Enn],
            'H_mean': [float(x) for x in profile_H],
        },
        'interpretation': (
            'Using the radial ODE backbone eliminates the dominant area/base '
            'interpolation error. The remaining residual comes from: '
            '(1) s-dependent orbit-shape perturbation dying into the cusp, '
            '(2) charge/connection perturbation dying into the cusp, '
            '(3) Q-dependent area correction. '
            'The residual profile shows where the mismatch concentrates and '
            'which blocks resist parameter optimization.'
        ),
    }
    path = Path('workspace/data/step97_improved_trial_residual.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, indent=2), encoding='utf-8')
    print(f"\nwrote {path}")


if __name__ == '__main__':
    main()
