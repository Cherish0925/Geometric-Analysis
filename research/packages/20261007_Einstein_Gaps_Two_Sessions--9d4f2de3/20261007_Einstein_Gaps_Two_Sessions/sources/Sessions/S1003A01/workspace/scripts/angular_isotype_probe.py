"""Focused non-SU(2) angular-isotype probe for the perpendicular CH cell.

This is deliberately a small construction test, not a spectral theorem.
It evaluates the J6 Hessian on globally smooth fixed-row j=1 functions
    F_r(q)=sqrt(3) Ad(q)_{0r}, r=0,1,2,
multiplied by one C-infinity radial bump supported away from bolt and collar and
all ten symmetric tensors of the background orthonormal coframe. The affine
metric family avoids second-parameterization terms at a nonstationary base.

The angular integral uses normalized Haar measure in Hopf coordinates
  z1=e^{i alpha} cos eta, z2=e^{i beta} sin eta,
  dmu=(2 pi)^{-2} d alpha d beta d(cos 2 eta),
which is nonsingular for interior Gauss nodes. The orbit integral is 2*pi^2 times
this normalized average. Modes are compactly supported, so no bolt/collar
smoothness convention is needed.

A negative finite-basis eigenvalue must subsequently be projected against exact
Lie derivatives and followed by a two-sided metric line test. A positive value
only concerns this sampled block.

Usage:
  python angular_isotype_probe.py RECORD --nqx 18 --nqa 2 --out OUT.json
"""
import argparse, json, math, sys, time
from pathlib import Path

import numpy as np
import jax
import jax.numpy as jnp
from numpy.polynomial.legendre import leggauss
jax.config.update('jax_enable_x64', True)

from perp_dual_cost import DualCell, load_record, seed_vector
from o11_rotated_cell import euler_E, curvature_scalars

PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]


def hopf_to_euler(alpha, beta, eta):
    """Hopf coordinates adapted directly to the euler_E convention.

    euler_E uses (psi,theta,phi) with the round Haar density proportional to
    sin(theta)dpsi dtheta dphi.  We sample psi=alpha, phi=beta,
    cos(theta)=cos(2 eta); this is exactly normalized Haar measure.
    """
    return jnp.array([alpha, 2*eta, beta])


def ad_row0(alpha, beta, eta):
    """First row of the SO(3) Euler rotation, a global fixed-row j=1 multiplet."""
    ps = alpha; th = 2*eta; ph = beta
    cp, sp = jnp.cos(ps), jnp.sin(ps)
    ct, st = jnp.cos(th), jnp.sin(th)
    cf, sf = jnp.cos(ph), jnp.sin(ph)
    return jnp.array([cp*ct*cf-sp*sf, -cp*ct*sf-sp*cf, cp*st])


def smooth_bump(u, lo, hi):
    q = (u-lo)/(hi-lo)
    inside = (q > 0) & (q < 1)
    # Peak one at q=1/2; all jets vanish at the support endpoints.
    val = jnp.exp(4.0 - 1.0/(q*(1-q)))
    return jnp.where(inside, val, 0.0)


def build(record, nqx=18, nqa=2, ulo=0.12, uhi=0.72):
    rec = load_record(record); x0=float(rec['x0']); X=float(rec['X']); deg=int(rec['deg'])
    cell=DualCell(x0, X, deg, deg, max(200, nqx)); cell.aligned=False; cell.wpow=2
    z=jnp.asarray(np.asarray(seed_vector(cell, rec), float)); prof=cell.prof_factory(z)
    ell=math.log(X/x0)

    ex, wx = leggauss(nqx); us=0.5*(ex+1); wx=0.5*wx*ell*x0*np.exp(ell*us); xs=x0*np.exp(ell*us)
    # Uniform trapezoidal nodes are exact for the low Fourier frequencies used here.
    alphas=2*math.pi*(np.arange(nqa)+0.37)/nqa; wa=np.ones(nqa)/nqa
    betas=2*math.pi*(np.arange(nqa)+0.11)/nqa; wb=np.ones(nqa)/nqa
    ec, wc = leggauss(nqa); cs=ec; wc=0.5*wc       # c=cos(2 eta), normalized dc/2
    pts=[]
    for ix,x in enumerate(xs):
        for ia,a in enumerate(alphas):
            for ib,b in enumerate(betas):
                for ic,c in enumerate(cs):
                    eta=0.5*math.acos(float(c)); ang=hopf_to_euler(float(a),float(b),eta)
                    # normalized Haar weight; orbit volume factor 2*pi^2 is inserted below
                    pts.append((jnp.concatenate([jnp.array([x]),ang]),
                                float(wx[ix]*wa[ia]*wb[ib]*wc[ic])))

    def base_metric(y):
        G,h=prof(y[0]); E=euler_E(y[1:]); gm=jnp.zeros((4,4)).at[0,0].set(1/(4*G))
        return gm.at[1:,1:].set(E.T@h@E)

    def modes(y):
        x=y[0]; psi,th,phi=y[1:]; eta=0.5*th
        F=jnp.sqrt(3.0)*ad_row0(psi,phi,eta)
        G,h=prof(x); E=euler_E(y[1:])
        C=jnp.zeros((4,4)).at[0,0].set(1.0).at[1:,1:].set(E)
        L=jnp.diag(jnp.concatenate([jnp.array([1/(2*jnp.sqrt(G))]), jnp.sqrt(jnp.diag(h))]))
        u=jnp.log(x/x0)/ell; bump=smooth_bump(u,ulo,uhi)
        out=[]
        for r in range(3):
            for A,B in PAIRS:
                S=jnp.zeros((4,4)).at[A,B].set(1.0)
                if A!=B: S=S.at[B,A].set(1.0)
                out.append(bump*F[r]*(C.T@L@S@L@C))
        return jnp.stack(out)

    nm=3*len(PAIRS)
    def metric(y,a): return base_metric(y)+jnp.tensordot(a,modes(y),axes=1)
    def dens(y,a):
        gm=metric(y,a); s,r0,_,_=curvature_scalars(lambda yy:metric(yy,a),y)
        # Our angular quadrature uses normalized Haar dc dpsi dphi. Coordinate
        # integration uses dtheta dpsi dphi, so remove the Euler sin(theta).
        return (r0+(s+24.0)**2/4)*jnp.sqrt(jnp.linalg.det(gm))/jnp.sin(y[2])
    def gram_dens(y):
        gm=base_metric(y); gi=jnp.linalg.inv(gm); B=modes(y)
        return jnp.einsum('mij,nkl,ik,jl->mn',B,B,gi,gi)*jnp.sqrt(jnp.linalg.det(gm))/jnp.sin(y[2])
    ys=jnp.stack([p[0] for p in pts]); pws=jnp.asarray([p[1] for p in pts])
    dens_v=jax.vmap(dens,in_axes=(0,None)); gram_v=jax.vmap(gram_dens)
    # With psi and phi each sampled over a 2pi period, the normalized Haar
    # average of sqrt(det g_coord)/sin(theta) must be multiplied by 16pi^2.
    def obj(a):
        return (16*math.pi**2)*jnp.sum(pws*dens_v(ys,a))/(8*math.pi**2)
    def gram():
        return (16*math.pi**2)*jnp.einsum('p,pij->ij',pws,gram_v(ys))/(8*math.pi**2)
    # Haar calibration of the chosen j=1 functions on the actual angular nodes.
    favg=np.zeros(3); fgram=np.zeros((3,3))
    for ia,aa in enumerate(alphas):
        for ib,bb in enumerate(betas):
            for ic,cc in enumerate(cs):
                eta=0.5*math.acos(float(cc)); ff=np.sqrt(3)*np.asarray(ad_row0(float(aa),float(bb),eta)); ww=wa[ia]*wb[ib]*wc[ic]
                favg += ww*ff; fgram += ww*np.outer(ff,ff)
    return obj, gram, rec, dict(x0=x0,X=X,deg=deg,nqx=nqx,nqa=nqa,ulo=ulo,uhi=uhi,nmodes=nm,
                                haar_mean=favg.tolist(),haar_gram=fgram.tolist())


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--nqx',type=int,default=18)
    ap.add_argument('--nqa',type=int,default=2); ap.add_argument('--ulo',type=float,default=.12); ap.add_argument('--uhi',type=float,default=.72)
    ap.add_argument('--out'); a=ap.parse_args(); t=time.time()
    obj, gram, rec, meta=build(a.record,a.nqx,a.nqa,a.ulo,a.uhi); z=jnp.zeros(meta['nmodes'])
    obj_jit=jax.jit(obj); grad_jit=jax.jit(jax.grad(obj)); hess_jit=jax.jit(jax.hessian(obj)); gram_jit=jax.jit(gram)
    J0=float(obj_jit(z)); grad=np.asarray(grad_jit(z)); H=np.asarray(hess_jit(z)); G=np.asarray(gram_jit())
    H=(H+H.T)/2; G=(G+G.T)/2
    ge,gv=np.linalg.eigh(G); keep=ge>ge.max()*1e-10; Q=gv[:,keep]/np.sqrt(ge[keep])[None,:]
    Hn=(Q.T@H@Q); Hn=(Hn+Hn.T)/2; ev,V=np.linalg.eigh(Hn); vraw=Q@V[:,0]
    # amplitude relative to |g^{-1}k|_F on the quadrature points is not yet available;
    # tiny coefficient line tests at least test AD consistency and even/odd behavior.
    lines=[]
    for eps in [1e-6,5e-7,2.5e-7]:
        jp=float(obj_jit(jnp.asarray(eps*vraw))); jm=float(obj_jit(jnp.asarray(-eps*vraw)))
        lines.append(dict(eps=eps,even=(jp+jm-2*J0)/eps**2,odd=(jp-jm)/(2*eps),Jplus=jp,Jminus=jm))
    out=dict(record=a.record,**meta,J0=J0,stored_J=rec.get('J'),rank=int(keep.sum()),grad_norm=float(np.linalg.norm(Q.T@grad)),
             gram_eig_min=float(ge[keep].min()),gram_eig_max=float(ge.max()),min_eig=float(ev[0]),negative_count=int((ev<-1e-6).sum()),
             eigenvalues=[float(v) for v in ev],lowest_mode=[float(v) for v in vraw],line_tests=lines,sec=time.time()-t,
             interpretation='raw j=1 affine J6 block; Lie-derivative projection is required before treating a negative value as geometric')
    text=json.dumps(out,indent=1); print(text)
    if a.out: Path(a.out).write_text(text+'\n')

if __name__=='__main__': main()
