"""Test the scalar-channel escape E=Ric_22-Ric_11=0 inside the cell ansatz (Step 16).

Freeze F and G of a stored perpendicular cell and vary only the anisotropy w.  Minimize
int W E^2/8 (the exact contribution of this Ricci-difference channel to P/(8pi^2))
with the same smooth bolt/collar envelope.  This tests whether one scalar shape channel
can be cancelled without making the full trace-free Ricci cost small.

Numerical variational experiment only; the output is not a lower theorem.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
import jax
import jax.numpy as jnp
from scipy.optimize import minimize
jax.config.update('jax_enable_x64',True)
sys.path.insert(0,str(Path(__file__).resolve().parent))
from perp_spin_diagnostics import cell_record


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--out'); ap.add_argument('--maxiter',type=int,default=1200); ap.add_argument('--mu',type=float,default=0.0)
    a=ap.parse_args(); c,z0,r=cell_record(a.record,nq=800); z0=np.asarray(z0); d=c.degU
    def spin_at(z,x):
        # Curvature channel in bolt-adapted axes.  With z_i=r_i-v_i, the shape
        # difference Ric(old2)-Ric(old1) equals z3-z1 after cyclic relabeling.
        from perp_spin_diagnostics import point
        vals=point(c,z,x); uu,C,s1,s2,s3,cub,psq,scal,lam,H,udot=vals
        zv=udot/jnp.array([jnp.nan,jnp.nan,jnp.nan]) if False else None
        # Recover radii from axes_u and form z=udot/a-2H/(a_j a_k).
        from perp_spin_diagnostics import axes_u
        GG,aa,_=axes_u(c,z,x)
        zz=udot/aa-2*H/(jnp.roll(aa,-1)*jnp.roll(aa,-2))
        return zz[2]-zz[0]
    # Fixed high-order Gauss grid already stored on cell.
    def ecost_only(cw):
        z=jnp.concatenate([jnp.asarray(z0[:2*d]),cw])
        E=jax.vmap(lambda x: spin_at(z,x))(c.xx)
        prof=c.prof_factory(z)
        dv=jax.vmap(lambda x: jnp.pi**2*jnp.sqrt(jnp.linalg.det(prof(x)[1])/prof(x)[0]))(c.xx)
        return jnp.sum(E*E*c.wx*dv)/(64*jnp.pi*jnp.pi)
    def obj(cw):
        reg=a.mu*jnp.sum((cw-jnp.asarray(z0[2*d:]))**2)
        return ecost_only(cw)+reg
    vg=jax.jit(jax.value_and_grad(obj))
    fun=lambda x:(lambda y:(float(y[0]),np.asarray(y[1],float)))(vg(jnp.asarray(x)))
    beforeE=float(ecost_only(jnp.asarray(z0[2*d:])))
    beforeRep=c.full_report(jnp.asarray(z0))
    res=minimize(fun,z0[2*d:],jac=True,method='L-BFGS-B',options={'maxiter':a.maxiter,'ftol':1e-14,'gtol':1e-9,'maxls':50})
    za=jnp.concatenate([jnp.asarray(z0[:2*d]),jnp.asarray(res.x)])
    afterE=float(ecost_only(jnp.asarray(res.x))); afterRep=c.full_report(za)
    out=dict(record=a.record,x0=float(r['x0']),X=float(r['X']),deg=d,
             before=dict(Ecost=beforeE,P=float(beforeRep['P_direct']),J=float(beforeRep['J'])),
             after=dict(Ecost=afterE,P=float(afterRep['P_direct']),J=float(afterRep['J'])),
             mu=float(a.mu),coefficient_displacement=float(np.linalg.norm(res.x-z0[2*d:])),
             success=bool(res.success),message=str(res.message),nit=int(res.nit),grad_inf=float(np.max(np.abs(res.jac))),cw=[float(q) for q in res.x])
    print(json.dumps(out,indent=1));
    if a.out: Path(a.out).write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__': main()
