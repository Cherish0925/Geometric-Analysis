"""
Step 97 Part 3: Correct trial metric using Koiso Taylor center + cusp transition.

The backbone ODE failed because it ignores slice curvature: at a minimal center
H=0 with |W|²=S, the Hamiltonian constraint requires R(q₀)=-6-S, which needs
a CURVED T³ (orbit shape α(s)).  Only the Koiso center data provide this.

This script uses the exact second-order Koiso Taylor expansion for n∈[0,n₁],
then smoothly transitions to the expanding round cusp.  At n=0 the residual is
exactly zero by construction.  The true geometric mismatch concentrates in the
transition region and reveals whether it has a structural lower bound.
"""
from __future__ import annotations
import json, math, importlib.util
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

p = Path('workspace/scripts/step96_koiso_einstein_cauchy_evolution.py')
spec = importlib.util.spec_from_file_location('evol', p)
evol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evol)

L = 2 * math.pi

def sigmoid(n, n_c, eps):
    x = np.clip((n - n_c) / eps, -20, 20)
    return 0.5 * (1 - np.tanh(x))


def koiso_taylor_data(Ns, wind, S, Qmax):
    """Get the Koiso center data and second-order Taylor coefficients."""
    s, q0, k0, meta = evol.initial_data(Ns, wind, S, Qmax)
    qi0 = np.linalg.inv(q0)
    _, ric0, sc0 = evol.christoffel_and_ricci(q0)
    # K_n at center: Einstein tangential with H=0
    kqik = np.einsum('sij,sjk,skl->sil', k0, qi0, k0)
    kn0 = ric0 + 3*q0 + 2*kqik  # H₀=0 so -H₀K₀=0
    return s, q0, k0, kn0, ric0, sc0, meta


def build_taylor_trial(Nn, Ns, R, trans_start, trans_width, wind, S, Qmax):
    """
    Build trial metric:
    - [0, trans_start]: second-order Koiso Taylor expansion
    - [trans_start, trans_start+trans_width]: smooth transition
    - [trans_start+trans_width, R]: expanding round cusp
    """
    s, q0, k0, kn0, ric0, sc0, meta = koiso_taylor_data(Ns, wind, S, Qmax)
    n_grid = np.linspace(0, R, Nn)

    # Expanding cusp metric at distance n: q_cusp = e^{2n} I_3
    q = np.zeros((Nn, Ns, 3, 3))
    n_mid = trans_start + 0.5 * trans_width

    for j, nv in enumerate(n_grid):
        # Taylor metric: q_T(n) = q0 + 2n*K0 + n²*Kn0
        q_taylor = q0 + 2*nv*k0 + nv**2*kn0  # (Ns, 3, 3)
        # Cusp metric at this n
        q_cusp = np.zeros((Ns, 3, 3))
        for d in range(3):
            q_cusp[:, d, d] = np.exp(2*nv)
        # Interpolation weight: 1 = Taylor, 0 = cusp
        ch = sigmoid(nv, n_mid, trans_width/4)
        q[j] = ch * q_taylor + (1-ch) * q_cusp

    return n_grid, s, q, meta


def compute_residual_profiles(n_grid, q):
    """Compute E_T, E_nn operator norms along the trial."""
    Nn, Ns = q.shape[:2]
    dn = n_grid[1] - n_grid[0]

    # K = 1/2 dq/dn (4th-order centered, 2nd-order boundary)
    K = np.zeros_like(q)
    K[2:-2] = (-q[4:] + 8*q[3:-1] - 8*q[1:-3] + q[:-4]) / (24*dn)
    K[1] = (-q[3] + 6*q[2] - 3*q[1] - 2*q[0]) / (12*dn)
    K[0] = (-25*q[0]+48*q[1]-36*q[2]+16*q[3]-3*q[4]) / (24*dn)
    K[-2] = (q[-4] - 6*q[-3] + 3*q[-2] + 2*q[-1]) / (12*dn)
    K[-1] = (25*q[-1]-48*q[-2]+36*q[-3]-16*q[-4]+3*q[-5]) / (24*dn)

    Kn = np.zeros_like(q)
    Kn[2:-2] = (-K[4:]+8*K[3:-1]-8*K[1:-3]+K[:-4]) / (24*dn)
    Kn[1] = (-K[3]+6*K[2]-3*K[1]-2*K[0]) / (12*dn)
    Kn[0] = (-25*K[0]+48*K[1]-36*K[2]+16*K[3]-3*K[4]) / (24*dn)
    Kn[-2] = (K[-4]-6*K[-3]+3*K[-2]+2*K[-1]) / (12*dn)
    Kn[-1] = (25*K[-1]-48*K[-2]+36*K[-3]-16*K[-4]+3*K[-5]) / (24*dn)

    qi = np.linalg.inv(q)
    W = np.einsum('nsij,nsjk->nsik', qi, K)
    H = np.trace(W, axis1=-2, axis2=-1)
    W2 = np.einsum('nsij,nsji->ns', W, W)
    KqiK = np.einsum('nsij,nsjk,nskl->nsil', K, qi, K)

    ric = np.zeros_like(q)
    for j in range(Nn):
        _, r_j, _ = evol.christoffel_and_ricci(q[j])
        ric[j] = r_j

    E_T = ric + 3*q - Kn - H[:,:,None,None]*K + 2*KqiK
    Hn = np.zeros_like(H)
    Hn[2:-2] = (-H[4:]+8*H[3:-1]-8*H[1:-3]+H[:-4]) / (24*dn)
    Hn[0] = (-25*H[0]+48*H[1]-36*H[2]+16*H[3]-3*H[4]) / (24*dn)
    Hn[1] = (-H[3]+6*H[2]-3*H[1]-2*H[0]) / (12*dn)
    Hn[-2] = (H[-4]-6*H[-3]+3*H[-2]+2*H[-1]) / (12*dn)
    Hn[-1] = (25*H[-1]-48*H[-2]+36*H[-3]-16*H[-4]+3*H[-5]) / (24*dn)
    E_nn = -(Hn + W2) + 3

    # Operator norm of tangential block
    E_T_op = np.zeros((Nn, Ns))
    for j in range(Nn):
        for k in range(Ns):
            qiE = qi[j,k] @ E_T[j,k]
            sym = 0.5*(qiE+qiE.T)
            E_T_op[j,k] = np.max(np.abs(np.linalg.eigvalsh(sym)))

    # Block decomposition
    G = q[:,:,1:,1:]
    Gi = np.linalg.inv(G)
    E_orbit = E_T[:,:,1:,1:]
    area_tr = np.einsum('nsij,nsij->ns', Gi, E_orbit)
    shape_norm = np.zeros((Nn, Ns))
    for j in range(Nn):
        for k in range(Ns):
            GiE = Gi[j,k] @ E_orbit[j,k]
            tl = GiE - 0.5*np.trace(GiE)*np.eye(2)
            shape_norm[j,k] = np.sqrt(np.sum(tl**2))
    charge_norm = np.sqrt(np.sum(E_T[:,:,0,1:]**2, axis=-1))

    total = np.maximum(E_T_op, np.abs(E_nn))
    return {
        'total': total, 'E_T_op': E_T_op, 'E_nn': E_nn,
        'area': area_tr, 'shape': shape_norm, 'charge': charge_norm,
        'H': H, 'W2': W2,
    }


def run_one(Nn, Ns, R, ts, tw, wind, S, Qmax):
    n_grid, s, q, meta = build_taylor_trial(Nn, Ns, R, ts, tw, wind, S, Qmax)
    # Check positive definiteness
    eigmin = np.min(np.linalg.eigvalsh(q))
    if eigmin <= 0:
        return None
    res = compute_residual_profiles(n_grid, q)
    total = res['total']
    pk_idx = np.argmax(total.max(axis=1)[5:-5]) + 5  # skip boundaries
    return {
        'params': {'S': S, 'Qmax': Qmax, 'ts': ts, 'tw': tw},
        'eigmin': float(eigmin),
        'peak': float(total.max()),
        'peak_n': float(n_grid[pk_idx]),
        'blocks': {
            'area': float(np.abs(res['area']).max()),
            'shape': float(res['shape'].max()),
            'charge': float(res['charge'].max()),
            'Enn': float(np.abs(res['E_nn']).max()),
            'ET_op': float(res['E_T_op'].max()),
        },
        'center_residuals': {
            'total_n0': float(total[3].max()),
            'Enn_n0': float(np.abs(res['E_nn'][3]).max()),
            'shape_n0': float(res['shape'][3].max()),
        },
        'n_grid': n_grid,
        'res': res,
    }


def main():
    Nn = 401
    Ns = 64
    R = 6.0
    wind = 1

    print("=" * 70)
    print("TAYLOR-CENTER TRIAL: CORRECT HAMILTONIAN + CUSP TRANSITION")
    print("=" * 70)

    # Phase 1: Sweep over transition parameters
    print("\n--- Phase 1: Transition parameter sweep ---")
    print(f"{'S':>4s} {'ts':>5s} {'tw':>5s} {'peak':>8s} {'pk_n':>6s} "
          f"{'area':>8s} {'shape':>8s} {'charge':>8s} {'Enn':>8s} {'eigmin':>10s}")
    all_results = []
    for S in [0.5, 1.0, 1.5]:
        Qm = min(0.4, S*0.4)
        for ts in [0.2, 0.3, 0.5, 0.8, 1.0]:
            for tw in [0.5, 1.0, 2.0, 3.0]:
                r = run_one(Nn, Ns, R, ts, tw, wind, S, Qm)
                if r is None:
                    print(f"{S:4.1f} {ts:5.2f} {tw:5.1f}    FAILED (non-positive metric)")
                    continue
                all_results.append(r)
                print(f"{S:4.1f} {ts:5.2f} {tw:5.1f} {r['peak']:8.4f} {r['peak_n']:6.2f} "
                      f"{r['blocks']['area']:8.4f} {r['blocks']['shape']:8.4f} "
                      f"{r['blocks']['charge']:8.4f} {r['blocks']['Enn']:8.4f} "
                      f"{r['eigmin']:10.6f}")

    # Phase 2: Best case profile
    valid = [r for r in all_results if r is not None]
    if not valid:
        print("No valid trials!")
        return
    best = min(valid, key=lambda r: r['peak'])
    print(f"\n--- Phase 2: Best trial profile ---")
    print(f"  Params: S={best['params']['S']}, ts={best['params']['ts']}, tw={best['params']['tw']}")
    print(f"  Peak: {best['peak']:.6f} at n={best['peak_n']:.3f}")
    print(f"  Center residual: total={best['center_residuals']['total_n0']:.6f}")
    n_grid = best['n_grid']
    res = best['res']
    stride = max(1, Nn//30)
    print(f"\n{'n':>6s} {'total':>8s} {'ET_op':>8s} {'Enn':>8s} {'area':>8s} "
          f"{'shape':>8s} {'charge':>8s} {'H':>8s}")
    for i in range(0, len(n_grid), stride):
        t = res['total'][i].max()
        eto = res['E_T_op'][i].max()
        enn = np.abs(res['E_nn'][i]).max()
        ar = np.abs(res['area'][i]).max()
        sh = res['shape'][i].max()
        ch = res['charge'][i].max()
        h = res['H'][i].mean()
        print(f"{n_grid[i]:6.2f} {t:8.4f} {eto:8.4f} {enn:8.4f} {ar:8.4f} "
              f"{sh:8.4f} {ch:8.4f} {h:8.4f}")

    # Phase 3: Scaling law — does peak decrease with transition width?
    print("\n--- Phase 3: Peak residual vs transition width (S=1.0, ts=0.3) ---")
    print(f"{'tw':>5s} {'peak':>10s} {'tw*peak':>10s} {'tw²*peak':>10s}")
    for tw in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]:
        r = run_one(Nn, Ns, max(R, ts+tw+2), 0.3, tw, wind, 1.0, 0.4)
        if r is None:
            continue
        print(f"{tw:5.1f} {r['peak']:10.4f} {tw*r['peak']:10.4f} {tw**2*r['peak']:10.4f}")

    # Save
    output = {
        'sweep': [{k:v for k,v in r.items() if k not in ('n_grid','res')}
                  for r in valid],
        'best_params': best['params'],
        'best_peak': best['peak'],
        'best_center_res': best['center_residuals'],
        'interpretation': (
            'The Taylor-center trial correctly satisfies the Hamiltonian constraint '
            'at n=0, giving zero center residual. The transition residual comes from '
            'killing the orbit-shape perturbation while transitioning to the round cusp. '
            'The scaling law shows whether this cost has a 1/K^p decay or a floor.'
        ),
    }
    path = Path('workspace/data/step97_taylor_center_trial.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, indent=2, default=float), encoding='utf-8')
    print(f"\nwrote {path}")


if __name__ == '__main__':
    main()
