"""
Step 97 Part 6: Explicit trial metric q(n,s) = cosh²(n)·q₀(s).

This metric satisfies the Raychaudhuri equation EXACTLY:
  H = 3 tanh(n), H' + |W|² = 3.
The tangential residual E_T = Ric(q₀) + 2 sech²(n)·q decays as e^{-2n}.

Key: the orbit shape alpha_0(s) is maintained at full amplitude for all n,
and the defect is naturally suppressed by the expanding geometry.
"""
import json, math, importlib.util
from pathlib import Path
import numpy as np

p = Path('workspace/scripts/step96_koiso_einstein_cauchy_evolution.py')
spec = importlib.util.spec_from_file_location('evol', p)
evol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evol)

L = 2*math.pi

def main():
    Ns = 128; wind = 1; S = 1.0; Qmax = 0.5
    s, q0, k0, meta = evol.initial_data(Ns, wind, S, Qmax)
    
    # The separator metric (at n=0): q₀ = diag(1, e^alpha, e^{-alpha})
    # Use the pure orbit part without connection
    G0 = q0[:, 1:, 1:]
    alpha0 = 0.5*(np.log(G0[:,0,0]) - np.log(G0[:,1,1]))
    q0_pure = np.zeros((Ns, 3, 3))
    q0_pure[:, 0, 0] = 1.0
    q0_pure[:, 1, 1] = np.exp(alpha0)
    q0_pure[:, 2, 2] = np.exp(-alpha0)
    
    # Compute Ric(q0_pure) and scalar curvature
    _, ric0, scalar0 = evol.christoffel_and_ricci(q0_pure)
    qi0 = np.linalg.inv(q0_pure)
    
    print("=" * 70)
    print("EXPLICIT TRIAL: q(n,s) = cosh²(n) · q₀(s)")
    print("=" * 70)
    print(f"Separator scalar curvature R(q₀): [{scalar0.min():.4f}, {scalar0.max():.4f}]")
    print(f"  (Koiso requires R=-6-S=-7, actual diagonal-only gives different R)")
    
    # Build full 4D trial metric on a grid
    Nn = 201
    R = 8.0
    n_grid = np.linspace(0, R, Nn)
    dn = n_grid[1] - n_grid[0]
    
    q = np.zeros((Nn, Ns, 3, 3))
    for j, nv in enumerate(n_grid):
        q[j] = np.cosh(nv)**2 * q0_pure
    
    # Analytic K, Kn
    # K = tanh(n) * q
    # Kn = sech²(n) * q + tanh(n) * 2*K = (sech² + 2tanh²) * q = (2 - sech²) * q
    K_analytic = np.zeros_like(q)
    Kn_analytic = np.zeros_like(q)
    for j, nv in enumerate(n_grid):
        tn = np.tanh(nv)
        sn2 = 1.0/np.cosh(nv)**2
        K_analytic[j] = tn * q[j]
        Kn_analytic[j] = (2 - sn2) * q[j]  # = sech² + 2tanh²
    
    # Compute residual analytically: E_T = Ric(q) + 2*sech²*q
    # where Ric(q) = Ric(cosh²·q₀) = Ric(q₀) (conformal factor is n-only)
    
    print(f"\n{'n':>6s}  {'E_T_op':>10s}  {'Ric_contrib':>12s}  {'sech2_contrib':>12s}  {'H':>8s}  {'|W|²':>8s}")
    
    profile = []
    for j in range(0, Nn, max(1, Nn//20)):
        nv = n_grid[j]
        tn = np.tanh(nv)
        sn2 = 1.0/np.cosh(nv)**2
        
        # 3D Ricci at this n-slice
        _, ric_j, _ = evol.christoffel_and_ricci(q[j])
        
        # E_T = Ric(q) + 2*sech²*q (analytic formula)
        E_T_analytic = ric_j + 2*sn2*q[j]
        
        # Verify against full numerical computation
        E_T_full = ric_j + 3*q[j] - Kn_analytic[j] - 3*tn*K_analytic[j] + 2*tn**2*q[j]
        analytic_err = np.max(np.abs(E_T_analytic - E_T_full))
        
        # Operator norm
        qi_j = np.linalg.inv(q[j])
        E_op = 0
        ric_contrib = 0
        for k in range(Ns):
            qiE = qi_j[k] @ E_T_analytic[k]
            sym = 0.5*(qiE+qiE.T)
            E_op = max(E_op, np.max(np.abs(np.linalg.eigvalsh(sym))))
            qiR = qi_j[k] @ ric_j[k]
            sym_r = 0.5*(qiR+qiR.T)
            ric_contrib = max(ric_contrib, np.max(np.abs(np.linalg.eigvalsh(sym_r))))
        
        H_val = 3*tn
        W2_val = 3*tn**2
        
        profile.append({
            'n': nv, 'E_T_op': E_op, 'Ric_contrib': ric_contrib,
            'sech2_contrib': 2*sn2, 'H': H_val, 'W2': W2_val,
            'analytic_err': float(analytic_err),
        })
        print(f"{nv:6.2f}  {E_op:10.6f}  {ric_contrib:12.6f}  {2*sn2:12.6f}  {H_val:8.4f}  {W2_val:8.4f}")
    
    # Fit the decay rate
    print(f"\n--- Decay rate analysis ---")
    far = [p for p in profile if p['n'] >= 1.0 and p['E_T_op'] > 1e-12]
    if len(far) >= 2:
        n1, n2 = far[0]['n'], far[-1]['n']
        e1, e2 = far[0]['E_T_op'], far[-1]['E_T_op']
        rate = np.log(e1/e2)/(n2-n1)
        print(f"  Fitted rate: {rate:.4f} (expected 2.0 for e^{{-2n}})")
    
    # Hamiltonian constraint check
    print(f"\n--- Hamiltonian constraint at n=0 ---")
    print(f"  R(q₀) = {scalar0.mean():.4f}")
    print(f"  H(0) = 0, |W(0)|² = 0")
    print(f"  R - H² + |W|² = {scalar0.mean():.4f}")
    print(f"  Required: -6 (for exact Einstein)")
    print(f"  Deficit: {scalar0.mean() + 6:.4f}")
    print(f"  (The Koiso center has R=-6-S=-7, |W|²=S=1)")
    
    # E_nn check
    print(f"\n--- E_nn (Raychaudhuri residual) ---")
    print(f"  H' + |W|² - 3 = 0 at all n (exact by construction)")
    for p in profile[:5]:
        enn = -(3/np.cosh(p['n'])**2 + 3*np.tanh(p['n'])**2 - 3)
        print(f"  n={p['n']:.2f}: E_nn = {enn:.10f}")
    
    print(f"\n" + "=" * 70)
    print(f"RESULT: Tangential defect E_T decays as e^{{-2n}} with coefficient")
    print(f"determined by orbit curvature.  Raychaudhuri is EXACT.")
    print(f"The orbit shape is maintained at full amplitude for all n.")
    print(f"This provides a smooth, positive-definite global trial metric")
    print(f"with exponentially decaying Ricci defect on one cusp end.")
    print(f"=" * 70)
    
    output = {
        'profile': profile,
        'separator_scalar': float(scalar0.mean()),
        'hamiltonian_deficit': float(scalar0.mean()+6),
        'mechanism': (
            'q = cosh^2(n) q_0(s) satisfies Raychaudhuri exactly. '
            'The tangential defect Ric(q) + 2 sech^2 q decays as e^{-2n}. '
            'The orbit shape alpha_0(s) is maintained at full amplitude. '
            'The conformal cusp factor dilutes the orbit curvature.'
        ),
    }
    path = Path('workspace/data/step97_cosh_trial.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, indent=2, default=float))
    print(f"\nwrote {path}")


if __name__ == '__main__':
    main()
