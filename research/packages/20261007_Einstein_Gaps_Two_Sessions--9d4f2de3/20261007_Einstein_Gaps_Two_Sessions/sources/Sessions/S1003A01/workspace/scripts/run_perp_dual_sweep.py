"""Run a reproducible dual-cost O11 perpendicular-cell sweep.

Uses perp_dual_cost.py as a library.  For each x0 and smoothness mode:
1. import the peer's P-optimized degree-6 profile when available;
2. reoptimize P and J at degrees 6 and 8 (degree 8 warm-started from degree 6);
3. save one JSON record per run and a compact CSV.

Usage:
  python run_perp_dual_sweep.py --out-dir ../data/perp_dual --x0 0.003 0.01 0.03 0.1
"""
from pathlib import Path
import argparse, csv, json, sys, time
import numpy as np
import jax
import jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from perp_dual_cost import make_cell, load_record, seed_vector, profile_report

ROOT = HERE.parents[3]
PEER = ROOT / 'Sessions' / 'S1003A02' / 'workspace' / 'data' / 'o11perp'


def optimize(x0, target, deg, nq, wpow, seed_rec, maxiter=4500, profile=False):
    c = make_cell(x0, deg, nq, smooth_mode=(wpow == 2))
    z0 = seed_vector(c, seed_rec)
    fun = jax.jit(lambda z: c.target(z, target)); gr = jax.jit(jax.grad(lambda z: c.target(z, target)))
    ini = c.full_report(jnp.asarray(z0)); _ = float(fun(jnp.asarray(z0))); _ = np.asarray(gr(jnp.asarray(z0)))
    t0 = time.time()
    r = minimize(lambda z: float(fun(jnp.asarray(z))), z0,
                 jac=lambda z: np.asarray(gr(jnp.asarray(z))), method='L-BFGS-B',
                 options=dict(maxiter=maxiter, ftol=2e-15, gtol=2e-11, maxls=80))
    z = jnp.asarray(r.x)
    out = dict(x0=x0, target=target, deg=deg, nq=nq, wpow=wpow,
               initial=ini, final=c.full_report(z), success=bool(r.success),
               message=str(r.message), nit=int(r.nit), grad_inf=float(np.max(np.abs(r.jac))),
               sec=time.time()-t0, z=[float(q) for q in r.x])
    if profile:
        out['profile'], _ = profile_report(c, z, n=501)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out-dir', required=True)
    ap.add_argument('--x0', nargs='+', type=float, default=[.003,.01,.03,.1])
    ap.add_argument('--nq6', type=int, default=400); ap.add_argument('--nq8', type=int, default=500)
    ap.add_argument('--maxiter', type=int, default=4500)
    args = ap.parse_args()
    outdir = Path(args.out_dir); outdir.mkdir(parents=True, exist_ok=True)
    records = []
    for x0 in args.x0:
        # smooth peer files exist at x0=.01; otherwise start with rough peer profile and
        # reimpose the smooth wpow=2 endpoint behavior before optimization.
        xs = f'{x0:g}'
        sr = PEER / f'perp_smooth_x{xs}.json'
        rr = PEER / f'perp_rough_x{xs}.json'
        seed_path = sr if sr.exists() and sr.stat().st_size else rr
        peer = load_record(seed_path)
        for target in ('P','J'):
            r6 = optimize(x0, target, 6, args.nq6, 2, peer, args.maxiter, profile=False)
            r6['seed_path'] = str(seed_path)
            p6 = outdir / f'x{x0:g}_{target}_d6.json'; p6.write_text(json.dumps(r6)+'\n')
            records.append(r6)
            r8 = optimize(x0, target, 8, args.nq8, 2, r6, args.maxiter, profile=True)
            r8['seed_path'] = str(p6)
            p8 = outdir / f'x{x0:g}_{target}_d8.json'; p8.write_text(json.dumps(r8)+'\n')
            records.append(r8)
            print(json.dumps({k:r8[k] for k in ('x0','target','deg','success','message','nit','grad_inf')}
                             | {'P':r8['final']['P_direct'],'J':r8['final']['J'],
                                'qscalar':r8['final']['scalar_deviation'],
                                'minT':r8['profile']['min_T']}), flush=True)
    fields = ['x0','target','deg','wpow','P','J','qscalar','P_slope','J_slope','nit','success','grad_inf','minT','x_minT','T_collar','Y_collar','Pi_collar']
    with (outdir/'summary.csv').open('w', newline='') as fh:
        w = csv.DictWriter(fh, fields); w.writeheader()
        for r in records:
            f=r['final']; p=r.get('profile',{})
            w.writerow(dict(x0=r['x0'],target=r['target'],deg=r['deg'],wpow=r['wpow'],
                            P=f['P_direct'],J=f['J'],qscalar=f['scalar_deviation'],
                            P_slope=(f['P_direct']-1)/r['x0'],J_slope=(f['J']-1)/r['x0'],
                            nit=r['nit'],success=r['success'],grad_inf=r['grad_inf'],
                            minT=p.get('min_T'),x_minT=p.get('x_at_min_T'),T_collar=p.get('T_collar'),
                            Y_collar=p.get('Y_collar'),Pi_collar=p.get('Pi_collar')))


if __name__ == '__main__':
    main()
