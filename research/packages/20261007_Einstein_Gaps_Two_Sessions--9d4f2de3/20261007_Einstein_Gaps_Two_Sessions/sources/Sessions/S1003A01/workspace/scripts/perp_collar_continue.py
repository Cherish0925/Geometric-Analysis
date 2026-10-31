"""Continue a perpendicular CH cell to a larger exact-collar radius.

Unlike perp_collar_scan.py, the seed is the *same physical metric*: the old optimized cell is
extended by an exact CH annulus, then least-squares projected into the new Chebyshev ansatz.
This preserves the monotonicity meaning of j_{1,0}(R) and avoids stretching the old transition
across the new logarithmic interval.  The projected seed and optimized record are both saved.
"""
import argparse, json, math, time
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.optimize import minimize
from numpy.polynomial.chebyshev import chebvander, chebval
from perp_dual_cost import DualCell


def smooth(u): return u**3*(10-15*u+6*u*u)


def old_profile(rec, x):
    d=int(rec['deg']); z=np.asarray(rec['z'],float)
    cF=z[:d].copy(); cG=z[d:2*d].copy(); cW=z[2*d:3*d].copy()
    # Exact effective coefficient; raw cG[0] is a redundant coordinate and can
    # be enormous in older LM records, so avoid subtractive floating cancellation.
    cG[0] = -sum(((-1)**k)*cF[k] for k in range(d)) - sum(((-1)**k)*cG[k] for k in range(1,d))
    x0=float(rec.get('x0',.01)); X=float(rec['X']); ell=math.log(X/x0)
    x=np.asarray(x); u=np.log(x/x0)/ell; s=2*u-1
    qF=(1-u)**3*chebval(s,cF); qG=(1-u)**3*chebval(s,cG)
    S=smooth(u)
    F=(x-x0)*np.exp(qF)+x0*S
    G=((x-x0)+(x*x+x0)*S)*np.exp(qG)
    wr=u*u*(1-u)**3*chebval(s,cW)
    w=np.log1p(x)*S+wr
    return F,G,w


def physical_extension_seed(old, Xnew, deg, ns=5000):
    x0=float(old.get('x0',.01)); Xold=float(old['X']); ellnew=math.log(Xnew/x0)
    # Lobatto-like dense grid, omit endpoints in divisions; include more points around old join.
    un=np.linspace(1e-5,1-1e-5,ns); x=x0*np.exp(ellnew*un)
    F=np.empty(ns); G=np.empty(ns); w=np.empty(ns)
    m=x<Xold
    F[m],G[m],w[m]=old_profile(old,x[m])
    F[~m]=x[~m]; G[~m]=x[~m]+x[~m]**2; w[~m]=np.log1p(x[~m])
    S=smooth(un); om3=(1-un)**3
    AF=np.maximum((F-x0*S)/(x-x0),1e-300)
    AG=np.maximum(G/((x-x0)+(x*x+x0)*S),1e-300)
    qF=np.log(AF); qG=np.log(AG); wr=w-np.log1p(x)*S
    V=chebvander(2*un-1,deg-1)
    # Weight physical transition and both endpoints; equations fit q/(1-u)^3 and wr/[u^2(1-u)^3].
    # Very close to u=1 the target and ansatz both vanish to third order but division magnifies roundoff.
    good=(un<.995)
    W=np.ones(ns); uj=math.log(Xold/x0)/ellnew
    W += 8*np.exp(-((un-uj)/.035)**2) + 2*np.exp(-(un/.06)**2)
    def ls(y, denom):
        yy=y/denom
        A=V[good]*np.sqrt(W[good,None]); b=yy[good]*np.sqrt(W[good])
        return np.linalg.lstsq(A,b,rcond=1e-12)[0]
    cF=ls(qF,om3); cG=ls(qG,om3); cW=ls(wr,un*un*om3)
    cG[0]=0.0  # exact null coordinate; DualCell computes the effective value stably
    return np.r_[cF,cG,cW], uj


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('seed'); ap.add_argument('X',type=float)
    ap.add_argument('deg',type=int); ap.add_argument('out'); ap.add_argument('--nq',type=int,default=1000)
    ap.add_argument('--maxiter',type=int,default=7000); ap.add_argument('--seed-out')
    a=ap.parse_args(); old=json.loads(Path(a.seed).read_text())
    z0,uj=physical_extension_seed(old,a.X,a.deg)
    x0=float(old.get('x0',.01))   # bolt area b^2=x0 is inherited from the seed (fixed-area branch)
    c=DualCell(x0,a.X,a.deg,a.deg,a.nq); c.aligned=False; c.wpow=2
    fun=jax.jit(lambda z:c.target(z,'J')); grad=jax.jit(jax.grad(lambda z:c.target(z,'J')))
    p0,j0,q0=[float(v) for v in c.costs(jnp.asarray(z0))]
    seedrec=dict(x0=x0,X=a.X,deg=a.deg,target='J',nq=a.nq,P=p0,J=j0,scalar=q0,
                 source=a.seed,old_join_u=uj,z=z0.tolist())
    if a.seed_out: Path(a.seed_out).write_text(json.dumps(seedrec)+'\n')
    _=float(fun(jnp.asarray(z0))); _=np.asarray(grad(jnp.asarray(z0)))
    t=time.time()
    res=minimize(lambda z:float(fun(jnp.asarray(z))),z0,jac=lambda z:np.asarray(grad(jnp.asarray(z))),
                 method='L-BFGS-B',options=dict(maxiter=a.maxiter,ftol=1e-16,gtol=1e-12,maxls=80))
    p,j,q=[float(v) for v in c.costs(jnp.asarray(res.x))]
    out=dict(x0=x0,X=a.X,deg=a.deg,target='J',nq=a.nq,P=p,J=j,scalar=q,
             P_margin_over_x0sq=(p-1)/x0**2,J_margin_over_x0sq=(j-1)/x0**2,
             source=a.seed,old_join_u=uj,projected_seed_costs=dict(P=p0,J=j0,scalar=q0),
             success=bool(res.success),message=str(res.message),nit=int(res.nit),
             grad_inf=float(np.max(np.abs(res.jac))),z=[float(v) for v in res.x],sec=time.time()-t)
    text=json.dumps(out); print(text); Path(a.out).write_text(text+'\n')

if __name__=='__main__': main()
