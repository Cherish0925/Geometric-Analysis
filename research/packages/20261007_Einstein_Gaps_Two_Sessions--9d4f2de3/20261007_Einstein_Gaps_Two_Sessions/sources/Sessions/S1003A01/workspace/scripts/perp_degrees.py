"""High-degree/restart study for one perpendicular O11 cell and one target.

Warm-start degree sequence and random perturbed restarts test whether the positive margin is
a basis artifact.  Smooth fixed-slot profiles only (wpow=2).  Uses exact Gauss quadrature.
"""
from pathlib import Path
import argparse,csv,json,sys,time
import numpy as np
import jax
import jax.numpy as jnp
jax.config.update('jax_enable_x64',True)
from scipy.optimize import minimize
HERE=Path(__file__).resolve().parent; sys.path.insert(0,str(HERE))
from perp_dual_cost import make_cell,load_record,seed_vector,profile_report


def run(c,target,z0,maxiter):
    fun=jax.jit(lambda z:c.target(z,target)); gr=jax.jit(jax.grad(lambda z:c.target(z,target)))
    _=float(fun(jnp.asarray(z0)));_=np.asarray(gr(jnp.asarray(z0))); t=time.time()
    r=minimize(lambda z:float(fun(jnp.asarray(z))),z0,jac=lambda z:np.asarray(gr(jnp.asarray(z))),
               method='L-BFGS-B',options=dict(maxiter=maxiter,ftol=1e-15,gtol=1e-11,maxls=80))
    return r,c.full_report(jnp.asarray(r.x)),time.time()-t


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--x0',type=float,required=True);ap.add_argument('--target',choices=['P','J'],required=True)
    ap.add_argument('--seed',required=True);ap.add_argument('--degrees',nargs='+',type=int,default=[8,10,12]);ap.add_argument('--nq',type=int,default=650)
    ap.add_argument('--restarts',type=int,default=3);ap.add_argument('--kick',type=float,default=.03);ap.add_argument('--maxiter',type=int,default=7000);ap.add_argument('--out',required=True)
    a=ap.parse_args(); seed=load_record(a.seed); rows=[]; rng=np.random.default_rng(1907)
    for d in a.degrees:
        c=make_cell(a.x0,d,a.nq,True); zbase=seed_vector(c,seed)
        starts=[zbase]+[zbase+a.kick*rng.normal(size=c.nparam)/np.sqrt(1+np.arange(c.nparam)) for _ in range(a.restarts)]
        best=None
        for k,z0 in enumerate(starts):
            r,f,sec=run(c,a.target,z0,a.maxiter)
            rec=dict(x0=a.x0,target=a.target,deg=d,restart=k,P=f['P_direct'],J=f['J'],qscalar=f['scalar_deviation'],
                     success=bool(r.success),message=str(r.message),nit=int(r.nit),grad_inf=float(np.max(np.abs(r.jac))),sec=sec,z=[float(q) for q in r.x])
            rows.append(rec); print(json.dumps({q:rec[q] for q in ('deg','restart','P','J','qscalar','success','nit','grad_inf')}),flush=True)
            val=rec[a.target]
            if best is None or val<best[a.target]:best=rec
        seed=best
    # Profile and save only final best, but preserve all restart rows.
    c=make_cell(a.x0,int(seed['deg']),a.nq,True); z=jnp.asarray(seed_vector(c,seed)); prof,_=profile_report(c,z,601)
    out=dict(rows=rows,best=seed,profile=prof)
    Path(a.out).write_text(json.dumps(out)+'\n')

if __name__=='__main__':main()
