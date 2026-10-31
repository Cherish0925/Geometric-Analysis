"""Radial-conformal completion of the perpendicular CH cell ansatz.

The Step-19 least-squares search fixes the radial gauge a1^2=x and therefore does not
contain compactly supported conformal variations.  This script adds

    g(z,c) = exp(2 phi_c) g_base(z),
    phi_c(u) = (1-u)^3 sum_{k<dphi} c_k T_k(2u-1),
    u=log(x/x0)/log(X/x0).

In x gauge this is represented by G -> exp(-2 phi)G and h -> exp(2 phi)h.
It preserves bolt smoothness because it rescales the radial and orbit metrics together;
phi has third-order contact with zero at the CH endpoint.  Minimization uses the exact
Cartan spin residual sum for J6/(8 pi^2), as in perp_lm.py.

This tests the inherited conformal Euler equation
    delta J6[2 f g] = 4 int f (Delta_+ + 6)(s+24)
which is absent from the gauge-fixed Step-19 coefficient gradient.

Usage:
  python perp_conformal_lm.py BASE.json OUT.json --dphi 12 --nq 1800
The output z stores [base shape coefficients, conformal coefficients].
"""
import argparse, json, time
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.optimize import least_squares

from perp_dual_cost import DualCell, load_record, seed_vector
from direct_ricci_lm import residual_fn


def cheb(n, y):
    vals = [jnp.ones_like(y)]
    if n > 1:
        vals.append(y)
    for _ in range(2, n):
        vals.append(2*y*vals[-1]-vals[-2])
    return jnp.stack(vals[:n])


class ConformalCell(DualCell):
    def __init__(self, x0, X, deg, dphi, nq):
        super().__init__(x0, X, deg, deg, nq)
        self.aligned = False
        self.wpow = 2
        self.dphi = dphi
        self.shape_nparam = self.nparam
        self.nparam += dphi

    def prof_factory(self, z):
        zshape = z[:self.shape_nparam]
        cp = z[self.shape_nparam:]
        base = super().prof_factory(zshape)
        x0, ell, dphi = self.x0, self.ell, self.dphi
        def prof(x):
            G, h = base(x)
            u = jnp.log(x/x0)/ell
            phi = (1-u)**3*jnp.dot(cp, cheb(dphi, 2*u-1))
            e2 = jnp.exp(2*phi)
            return G/e2, e2*h
        return prof


def component_costs(cell, R, z):
    # Direct residual columns are the four orthonormal components of Ric+6g.
    # Reconstruct s+24 as their trace; J-P=(1/4)int(s+24)^2.  With the
    # normalized residual weight, scalar channel = (sum columns)^2/4.
    rr = np.asarray(R(jnp.asarray(z))).reshape((-1,4))
    J = float(np.sum(rr**2)); scalar = float(np.sum(np.sum(rr,axis=1)**2)/4)
    return J-scalar, J, scalar


def sample_geometry(cell, z, n=2001):
    prof = cell.prof_factory(jnp.asarray(z))
    xs = cell.x0*np.exp(cell.ell*np.linspace(1e-8,1,n))
    vals = jax.vmap(prof)(jnp.asarray(xs))
    G = np.asarray(vals[0]); h = np.asarray(vals[1])
    ev = np.linalg.eigvalsh(h)
    # Recover phi from the determinant ratio against the base profile.
    cp = np.asarray(z[cell.shape_nparam:])
    us = np.linspace(1e-8,1,n)
    B = np.polynomial.chebyshev.chebvander(2*us-1, cell.dphi-1)
    phi = (1-us)**3*(B@cp)
    return dict(min_G=float(G.min()), min_orbit_eigenvalue=float(ev.min()),
                phi_min=float(phi.min()), phi_max=float(phi.max()),
                conformal_factor_min=float(np.exp(2*phi).min()),
                conformal_factor_max=float(np.exp(2*phi).max()))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('seed'); ap.add_argument('out')
    ap.add_argument('--dphi',type=int,default=12); ap.add_argument('--nq',type=int,default=1800)
    ap.add_argument('--max_nfev',type=int,default=250); ap.add_argument('--phi-only',action='store_true')
    ap.add_argument('--scalar-solve',action='store_true', help='vary phi only to minimize the scalar residual channel')
    ap.add_argument('--joint-outer',type=int,default=0, help='alternate full-shape LM and exact scalar conformal solves')
    ap.add_argument('--project-phi',action='store_true', help='if changing dphi, project the seed conformal profile')
    a=ap.parse_args(); old=load_record(a.seed)
    x0=float(old['x0']); X=float(old['X']); deg=int(old['deg'])
    c=ConformalCell(x0,X,deg,a.dphi,a.nq)
    # A conformal output can be used as its own seed; ordinary LM records contain only shape z.
    oz=np.asarray(old['z'],float)
    if len(oz)==c.nparam:
        z0=oz.copy()
    else:
        base=DualCell(x0,X,deg,deg,a.nq); base.aligned=False; base.wpow=2
        odphi=int(old.get('dphi',0))
        if odphi>0 and len(oz)==3*deg+odphi:
            zshape=oz[:3*deg].copy()
        else:
            zshape=np.asarray(seed_vector(base,old),float)
        cp=np.zeros(a.dphi)
        if a.project_phi and odphi>0 and len(oz)==3*deg+odphi:
            us=np.linspace(0,1,4001); Vold=np.polynomial.chebyshev.chebvander(2*us-1,odphi-1)
            Vnew=np.polynomial.chebyshev.chebvander(2*us-1,a.dphi-1)
            target=Vold@oz[3*deg:]
            cp=np.linalg.lstsq(Vnew,target,rcond=1e-13)[0]
        z0=np.r_[zshape,cp]
    # cG[0] cancels identically in PerpCell.prof_factory; remove this exact null coordinate.
    redundant=deg
    active=np.array([i for i in range(c.nparam) if i!=redundant],dtype=int)
    z0[redundant]=0.0
    def pack_active(y, ref):
        zz=ref.copy(); zz[active]=y; zz[redundant]=0.0; return zz
    R=jax.jit(residual_fn(c)); Jac=jax.jit(jax.jacfwd(residual_fn(c)))
    r0=np.asarray(R(jnp.asarray(z0))); p0,j0,q0=component_costs(c,R,z0)
    print('seed',dict(P=p0,J=j0,scalar=q0,resid=float(r0@r0)),flush=True)
    t=time.time()
    if a.joint_outer > 0:
        z=z0.copy(); total_nfev=0; status=0; message='alternating shape/scalar solve'
        for outer in range(a.joint_outer):
            # Full J solve with the exact redundant cG[0] coordinate removed.
            ref=z.copy(); y0=z[active].copy()
            def pfull(y): return pack_active(y,ref)
            sf=least_squares(lambda y:np.asarray(R(jnp.asarray(pfull(y)))),y0,
                             jac=lambda y:np.asarray(Jac(jnp.asarray(pfull(y))))[:,active],method='trf',x_scale='jac',
                             ftol=1e-15,xtol=1e-15,gtol=1e-15,max_nfev=a.max_nfev)
            z=pfull(sf.x); total_nfev += int(sf.nfev)
            zs=z[:c.shape_nparam].copy(); cp=z[c.shape_nparam:].copy()
            def pack(cc): return np.r_[zs,cc]
            def target(cc): return np.asarray(R(jnp.asarray(pack(cc)))).reshape((-1,4)).sum(axis=1)/2
            def target_jac(cc): return np.asarray(Jac(jnp.asarray(pack(cc)))).reshape((-1,4,c.nparam)).sum(axis=1)[:,c.shape_nparam:]/2
            ss=least_squares(target,cp,jac=target_jac,method='trf',x_scale='jac',
                             ftol=1e-15,xtol=1e-15,gtol=1e-15,max_nfev=a.max_nfev)
            z=pack(ss.x); total_nfev += int(ss.nfev); status=int(ss.status)
            pp,jj,qq=component_costs(c,R,z); print('outer',outer,dict(P=pp,J=jj,scalar=qq),flush=True)
        rr=np.asarray(R(jnp.asarray(z))); jacfull=np.asarray(Jac(jnp.asarray(z)))
        gfull=2*jacfull.T@rr; gopt=gfull
        class Sol: pass
        sol=Sol(); sol.nfev=total_nfev; sol.status=status; sol.message=message; sol.x=z
    elif a.phi_only or a.scalar_solve:
        zs=z0[:c.shape_nparam].copy(); cp0=z0[c.shape_nparam:].copy()
        def pack(cp): return np.r_[zs,cp]
        if a.scalar_solve:
            def target(cp): return np.asarray(R(jnp.asarray(pack(cp)))).reshape((-1,4)).sum(axis=1)/2
            def target_jac(cp): return np.asarray(Jac(jnp.asarray(pack(cp)))).reshape((-1,4,c.nparam)).sum(axis=1)[:,c.shape_nparam:]/2
        else:
            def target(cp): return np.asarray(R(jnp.asarray(pack(cp))))
            def target_jac(cp): return np.asarray(Jac(jnp.asarray(pack(cp))))[:,c.shape_nparam:]
        sol=least_squares(target,cp0,jac=target_jac,
                          method='trf',x_scale='jac',ftol=1e-15,xtol=1e-15,gtol=1e-15,max_nfev=a.max_nfev)
        z=pack(sol.x); jacfull=np.asarray(Jac(jnp.asarray(z))); rr=np.asarray(R(jnp.asarray(z)))
        gfull=2*jacfull.T@rr; gopt=2*target_jac(sol.x).T@target(sol.x)
    else:
        ref=z0.copy(); y0=z0[active].copy()
        def pfull(y): return pack_active(y,ref)
        sol=least_squares(lambda y:np.asarray(R(jnp.asarray(pfull(y)))),y0,
                          jac=lambda y:np.asarray(Jac(jnp.asarray(pfull(y))))[:,active],method='trf',x_scale='jac',
                          ftol=1e-15,xtol=1e-15,gtol=1e-15,max_nfev=a.max_nfev)
        z=pfull(sol.x); rr=sol.fun; jacfull=np.asarray(Jac(jnp.asarray(z))); gfull=2*jacfull.T@rr
        gopt=2*sol.jac.T@rr
    p,j,q=component_costs(c,R,z)
    out=dict(x0=x0,X=X,deg=deg,dphi=a.dphi,nq=a.nq,target='J',method='conformal_least_squares_trf',
             phi_only=bool(a.phi_only),scalar_solve=bool(a.scalar_solve),joint_outer=int(a.joint_outer),P=p,J=j,scalar=q,J_resid=float(rr@rr),
             grad_inf_optimized=float(np.max(np.abs(gopt))),grad_inf_full=float(np.max(np.abs(gfull))),
             grad_inf_shape=float(np.max(np.abs(gfull[:c.shape_nparam]))),
             grad_inf_conformal=float(np.max(np.abs(gfull[c.shape_nparam:]))),
             nfev=int(sol.nfev),status=int(sol.status),message=str(sol.message),source=a.seed,
             seed_costs=dict(P=p0,J=j0,scalar=q0),geometry=sample_geometry(c,z),
             phi_coeff=[float(v) for v in z[c.shape_nparam:]],sec=time.time()-t,
             z=[float(v) for v in z])
    print(json.dumps({k:v for k,v in out.items() if k!='z'})); Path(a.out).write_text(json.dumps(out)+'\n')

if __name__=='__main__': main()
