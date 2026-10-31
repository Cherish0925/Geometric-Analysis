"""Least-squares optimization of the actual Einstein defect Ric+6g.

This repairs a conceptual/implementation error in the Step-19 residual optimizer:
the vector (r_i-v_i, s+24) reconstructs P+(s+24)^2/4 algebraically, but its
sample residuals are not the four orthonormal components of Ric+6g.  Gauss--Newton
must minimize the actual component residuals to be a valid nonlinear least-squares
method for J6.

For diagonal Bianchi IX define r_i=u_i'/a_i, v_i=2H_i/(a_j a_k).  From
s=-2 sum(r_i+v_i), z_i=r_i-v_i and z_i=-(Ric00^o+Ricii^o),
  Ric00 = (s - 2 sum z_i)/4,
  Ricii = (s + 2 sum z_i)/4 - z_i.
The residual uses sqrt(W dt quadrature)/2 * (Ric_aa+6), after the orbit factor
2 pi^2 and normalization 8 pi^2 are cancelled; its squared norm is J6/(8 pi^2).

Usage: python direct_ricci_lm.py SEED OUT [--nq 2200 --max_nfev 1000]
"""
import argparse,json,time
from pathlib import Path
import numpy as np
import jax,jax.numpy as jnp
jax.config.update('jax_enable_x64',True)
from scipy.optimize import least_squares
from perp_dual_cost import DualCell,load_record,seed_vector


def residual_fn(cell):
    def res(z):
        prof=cell.prof_factory(z)
        def radii(x):
            G,h=prof(x);return jnp.sqrt(jnp.array([h[1,1],h[2,2],h[0,0]])),G
        def state(x):
            a,G=radii(x);da=jax.jacfwd(lambda xx:radii(xx)[0])(x)*2*jnp.sqrt(G)
            a1,a2,a3=a
            u=jnp.array([da[0]-(a2*a2+a3*a3-a1*a1)/(a2*a3),
                         da[1]-(a3*a3+a1*a1-a2*a2)/(a3*a1),
                         da[2]-(a1*a1+a2*a2-a3*a3)/(a1*a2)])
            return u,a,G
        def at(x,wx):
            u,a,G=state(x);ud=jax.jacfwd(lambda xx:state(xx)[0])(x)*2*jnp.sqrt(G)
            u1,u2,u3=u;H=jnp.array([u1+u2*u3/2,u2+u3*u1/2,u3+u1*u2/2])
            r=ud/a;v=2*H/jnp.array([a[1]*a[2],a[2]*a[0],a[0]*a[1]])
            zc=r-v; s=-2*jnp.sum(r+v); zsum=jnp.sum(zc)
            # Exact inversion of z_i=-(Ric00^o+Ricii^o), together with trace s.
            Ric0=(s-2*zsum)/4
            Rico=(s+2*zsum)/4-zc
            E=jnp.concatenate([jnp.array([Ric0+6]),Rico+6])
            # dV = 2 pi^2 W dt and dt=dx/(2 sqrt G), normalized by 8 pi^2.
            wt=jnp.sqrt(wx*jnp.prod(a)/(8*jnp.sqrt(G)))
            return wt*E
        return jax.vmap(at)(cell.xx,cell.wx).reshape(-1)
    return res


def direct_cost(cell,R,z):
    rr=np.asarray(R(jnp.asarray(z)));return float(rr@rr)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('seed');ap.add_argument('out');ap.add_argument('--nq',type=int,default=2200);ap.add_argument('--max_nfev',type=int,default=1200)
    a=ap.parse_args();old=load_record(a.seed);x0=float(old['x0']);X=float(old['X']);deg=int(old['deg'])
    c=DualCell(x0,X,deg,deg,a.nq);c.aligned=False;c.wpow=2
    z0=np.asarray(seed_vector(c,old),float);redundant=deg;active=np.array([i for i in range(len(z0)) if i!=redundant]);z0[redundant]=0
    def pack(y):
        z=np.zeros(len(z0));z[active]=y;return z
    R=jax.jit(residual_fn(c));Jac=jax.jit(jax.jacfwd(residual_fn(c)))
    j0=direct_cost(c,R,z0);print('seed direct J',j0,flush=True);t=time.time()
    sol=least_squares(lambda y:np.asarray(R(jnp.asarray(pack(y)))),z0[active],jac=lambda y:np.asarray(Jac(jnp.asarray(pack(y))))[:,active],
                      method='trf',x_scale='jac',ftol=1e-15,xtol=1e-15,gtol=1e-15,max_nfev=a.max_nfev)
    z=pack(sol.x);rr=np.asarray(R(jnp.asarray(z)));J=float(rr@rr);jac=np.asarray(Jac(jnp.asarray(z)));g=2*jac.T@rr
    out=dict(x0=x0,X=X,deg=deg,nq=a.nq,target='J',method='direct_ricci_least_squares_trf',J=J,J_seed=j0,
             grad_inf=float(np.max(np.abs(g[active]))),grad_inf_full=float(np.max(np.abs(g))),nfev=int(sol.nfev),status=int(sol.status),
             message=str(sol.message),redundant_index=redundant,source=a.seed,sec=time.time()-t,z=[float(v) for v in z])
    print(json.dumps({k:v for k,v in out.items() if k!='z'}));Path(a.out).write_text(json.dumps(out)+'\n')
if __name__=='__main__':main()
