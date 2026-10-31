"""Large-collar U(2) blow-up-cell scan over real hyperbolic 4-space.

The peer implementation ``u2_general_cell.py`` uses the normalization
Ric(g_H)=-6 g_H, hence sectional curvature -2 and scalar curvature s_H=-24.
Its energies P,J are already divided by 8*pi^2.

Besides optimizing P or J, this script resolves the exact relative identity

 P-1 = 4 int_U |W+|^2/(8*pi^2)
       + [int_U s^2/12 - 48 Vol(B_X)]/(8*pi^2),

and, for J=P+int(s+24)^2/4,

 J-1 = 4 int_U |W+|^2/(8*pi^2)
       + int_U (s+18)^2/3/(8*pi^2)
       + 36 Vol(U)/(8*pi^2) - 48 Vol(B_X)/(8*pi^2).

The formulas are the scalar -24 versions of the scalar -12 identities in
which the coefficients are 9 and 12 and the optimal scalar is -9.
They distinguish Weyl cost, scalar-shape cost, and the volume-saving channel.
This is an exploratory optimizer, not a rigorous enclosure.
"""
from pathlib import Path
import argparse, json, sys, time
import numpy as np
import jax.numpy as jnp
from scipy.optimize import minimize

ROOT = Path(__file__).resolve().parents[4]
PEER = ROOT / "Sessions/S1003A01/workspace/scripts"
sys.path.insert(0, str(PEER))
from u2_general_cell import GeneralCell


def h4_ball_volume_norm(X):
    """Vol(B_X)/(8*pi^2) for peer RSF coordinates, Ric=-6g."""
    y = np.sqrt(1.0 + 2.0*X)
    return y**3/48.0 - y/16.0 + 1.0/24.0


def channels(cell, z, P, J):
    Pd, s, wd, dx, F, G = cell.fields(jnp.asarray(z))
    # u2_general_cell.wd=abc/(8 sqrt(G)) is already dV/(8*pi^2) per dx.
    V = float(jnp.sum(wd*dx))
    VB = h4_ball_volume_norm(cell.X)
    scalar_rel = float(jnp.sum(wd*(s*s/12.0)*dx)) - 48.0*VB
    four_Wp = P - 1.0 - scalar_rel
    sq18 = float(jnp.sum(wd*((s+18.0)**2/3.0)*dx))
    rhsJ = four_Wp + sq18 + 36.0*V - 48.0*VB
    # Volume-weighted scalar summaries.
    mean_s = float(jnp.sum(wd*s*dx)/V)
    rms_s18 = float(jnp.sqrt(jnp.sum(wd*(s+18.0)**2*dx)/V))
    frac_s_near18 = float(jnp.sum(wd*(jnp.abs(s+18.0) <= 3.0)*dx)/V)
    return dict(V_norm=V, VB_norm=VB, V_over_VB=V/VB,
                scalar_rel_norm=scalar_rel, four_Wplus_norm=four_Wp,
                square_splus18_over3_norm=sq18,
                Jminus1_rhs=rhsJ, J_identity_residual=(J-1.0)-rhsJ,
                mean_scalar=mean_s, rms_scalar_plus18=rms_s18,
                volume_frac_abs_splus18_le3=frac_s_near18,
                minF=float(jnp.min(F)), minG=float(jnp.min(G)))


def optimize_one(x0, X, deg, target, nq, starts=1, seed=0):
    cell = GeneralCell('RSF', 1.0, x0, X, deg, nq)
    idx = 0 if target == 'P' else 1
    f = lambda z: cell.energies(jnp.asarray(z))[idx]
    g = __import__('jax').grad(f)
    rng = np.random.default_rng(seed)
    trials = []
    init = np.zeros(cell.nparam)
    for j in range(starts):
        z0 = init.copy() if j == 0 else rng.normal(scale=0.03, size=cell.nparam)
        res = minimize(lambda z: float(f(z)), z0,
                       jac=lambda z: np.asarray(g(z), dtype=float),
                       method='L-BFGS-B',
                       options=dict(maxiter=8000, ftol=2e-15, gtol=3e-11, maxls=100))
        P, J, scalar = [float(v) for v in cell.energies(jnp.asarray(res.x))]
        rec = dict(P=P, J=J, scalar_part=scalar, objective=P if idx == 0 else J,
                   success=bool(res.success), message=str(res.message), nit=int(res.nit),
                   grad_inf=float(np.max(np.abs(res.jac))), z=[float(v) for v in res.x])
        rec.update(channels(cell, res.x, P, J))
        trials.append(rec)
    best = min(trials, key=lambda r:r['objective'])
    return dict(bulk='RSF', k=1.0, Ric=-6.0, scalar_bulk=-24.0,
                x0=x0, X=X, deg=deg, target=target, nq=nq,
                starts=starts, best=best, trials=trials)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--grid', action='store_true')
    ap.add_argument('--x0', type=float, default=0.03)
    ap.add_argument('--X', type=float, default=16.0)
    ap.add_argument('--deg', type=int, default=14)
    ap.add_argument('--target', choices=['P','J'], default='J')
    ap.add_argument('--nq', type=int, default=900)
    ap.add_argument('--starts', type=int, default=1)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    t0=time.time()
    rows=[]
    if args.grid:
        cases=[]
        for x0 in [0.003, 0.01, 0.03, 0.1]:
            for X in [4.0, 16.0, 64.0]:
                for target in ['P','J']:
                    cases.append((x0,X,target))
        for i,(x0,X,target) in enumerate(cases):
            print(f'case {i+1}/{len(cases)} x0={x0} X={X} {target}', flush=True)
            rows.append(optimize_one(x0,X,args.deg,target,args.nq,args.starts,1000+i))
    else:
        rows=[optimize_one(args.x0,args.X,args.deg,args.target,args.nq,args.starts,0)]
    out=dict(normalization='Ric=-6, s=-24, sectional curvature -2',
             rigorous=False, elapsed=time.time()-t0, rows=rows)
    Path(args.out).write_text(json.dumps(out,indent=1)+'\n')
    for r in rows:
        b=r['best']
        print(json.dumps(dict(x0=r['x0'],X=r['X'],target=r['target'],P=b['P'],J=b['J'],
                              Vratio=b['V_over_VB'],fourWp=b['four_Wplus_norm'],
                              sq18=b['square_splus18_over3_norm'],res=b['J_identity_residual'],
                              grad=b['grad_inf'])),flush=True)

if __name__=='__main__':
    main()
