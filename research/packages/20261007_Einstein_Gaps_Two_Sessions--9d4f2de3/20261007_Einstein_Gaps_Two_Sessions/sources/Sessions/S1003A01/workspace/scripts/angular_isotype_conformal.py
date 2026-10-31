"""Scalar-relaxed j=1 angular Hessian for the perpendicular CH cell.

This is a construction search, not a spectral theorem.  It fixes the single angular
coefficient F=sqrt(3) Ad(q)_{00}.  On the anisotropic base this is only a compression
of the full fixed-left-row j=1 tensor space, which also contains Ad(q)_{01},Ad(q)_{02}.
It uses

  h = F * u^2 (1-u)^3 sum_m T_m(2u-1) H_m

for nine trace-free symmetric orthonormal-frame spanning tensors H_m (not an
orthonormal coefficient basis; the geometric Gram matrix is used).  It simultaneously varies a
conformal factor

  phi = F * u^2 (1-u)^4 sum_n b_n T_n(2u-1),   g -> exp(2 phi) (g+h).

The Schur complement of the full J6 Hessian in b integrates out the sampled scalar
response.  In the convergent-basis limit it is the finite-dimensional version of
solving (-6 Delta + 48)v=-Ds[h] at a scalar-normalized base.  The long exact-CH collar
of the X=512 profile is included up to x=X; phi has third-order metric contact there.
The base is only numerically scalar normalized, so conclusions are numerical and every
putative negative mode is followed on the actual two-sided metric path.

The angular quadrature is normalized Haar measure in Hopf/Euler coordinates.  The
script reports raw and scalar-relaxed generalized eigenvalues, conformal-block
conditioning, actual line tests, and Haar/base-energy calibration.

Usage:
  python angular_isotype_conformal.py RECORD --nrad 3 --nphi 8 --nqx 96 --nqa 3 --out OUT.json
"""
import argparse, json, math, time
from pathlib import Path

import numpy as np
import jax
import jax.numpy as jnp
from numpy.polynomial.legendre import leggauss
jax.config.update('jax_enable_x64', True)

from perp_dual_cost import DualCell, load_record, seed_vector
from o11_rotated_cell import euler_E, curvature_scalars
from angular_isotype_probe import ad_row0

OFFDIAG = [(i, j) for i in range(4) for j in range(i+1, 4)]
# A trace-free orthonormal-frame spanning set: six off-diagonal tensors and
# three independent diagonal differences.  The omitted pure trace direction is
# exactly redundant with the conformal variable at first order.
DIAGDIFF = [(0,3),(1,3),(2,3)]


def ad00(psi, theta, phi):
    """Ad(q)_{00}; sqrt(3)*ad00 has normalized Haar L2 norm one."""
    return jnp.cos(psi)*jnp.cos(theta)*jnp.cos(phi)-jnp.sin(psi)*jnp.sin(phi)


def cheb_values(n, z):
    vals=[jnp.ones_like(z)]
    if n > 1: vals.append(z)
    for _ in range(2, n): vals.append(2*z*vals[-1]-vals[-2])
    return jnp.stack(vals[:n])


def build(record, nrad=3, nphi=8, nqx=96, nqa=3, fullmult=False):
    rec=load_record(record); x0=float(rec['x0']); X=float(rec['X']); deg=int(rec['deg'])
    cell=DualCell(x0, X, deg, deg, max(200,nqx)); cell.aligned=False; cell.wpow=2
    z=jnp.asarray(np.asarray(seed_vector(cell,rec),float)); prof=cell.prof_factory(z)
    ell=math.log(X/x0)

    ex,wx=leggauss(nqx); us=.5*(ex+1); wx=.5*wx*ell*x0*np.exp(ell*us); xs=x0*np.exp(ell*us)
    alphas=2*math.pi*(np.arange(nqa)+.37)/nqa; wa=np.ones(nqa)/nqa
    betas=2*math.pi*(np.arange(nqa)+.11)/nqa; wb=np.ones(nqa)/nqa
    ec,wc=leggauss(nqa); wc=.5*wc
    pts=[]
    for ix,x in enumerate(xs):
        for ia,aa in enumerate(alphas):
            for ib,bb in enumerate(betas):
                for ic,cc in enumerate(ec):
                    th=math.acos(float(cc))
                    y=jnp.array([x,float(aa),th,float(bb)])
                    pts.append((y,float(wx[ix]*wa[ia]*wb[ib]*wc[ic])))

    def base_metric(y):
        G,h=prof(y[0]); E=euler_E(y[1:]); gm=jnp.zeros((4,4)).at[0,0].set(1/(4*G))
        return gm.at[1:,1:].set(E.T@h@E)

    def data_at(y):
        x=y[0]; psi,th,phi=y[1:]
        Fs=(jnp.sqrt(3.0)*ad_row0(psi,phi,0.5*th) if fullmult
            else jnp.array([jnp.sqrt(3.0)*ad00(psi,th,phi)]))
        G,h=prof(x); E=euler_E(y[1:])
        # C maps coordinate covectors to (dx,sigma_i); L turns this into the
        # background orthonormal coframe used for the ten tensor components.
        C=jnp.zeros((4,4)).at[0,0].set(1.0).at[1:,1:].set(E)
        L=jnp.diag(jnp.concatenate([jnp.array([1/(2*jnp.sqrt(G))]),jnp.sqrt(jnp.diag(h))]))
        u=jnp.log(x/x0)/ell; Tm=cheb_values(nrad,2*u-1); Tp=cheb_values(nphi,2*u-1)
        envm=u*u*(1-u)**3; envp=u*u*(1-u)**4
        modes=[]
        for F in Fs:
            for m in range(nrad):
                for A,B in OFFDIAG:
                    S=jnp.zeros((4,4)).at[A,B].set(1.0).at[B,A].set(1.0)
                    modes.append(F*envm*Tm[m]*(C.T@L@S@L@C))
                for A,B in DIAGDIFF:
                    S=jnp.zeros((4,4)).at[A,A].set(1.0).at[B,B].set(-1.0)
                    modes.append(F*envm*Tm[m]*(C.T@L@S@L@C))
        phis=jnp.concatenate([F*envp*Tp for F in Fs])
        return jnp.stack(modes),phis

    nmult=3 if fullmult else 1; na=9*nrad*nmult; nb=nphi*nmult
    def metric(y,c):
        a=c[:na]; b=c[na:]
        B,V=data_at(y); phi=jnp.dot(b,V)
        return jnp.exp(2*phi)*(base_metric(y)+jnp.tensordot(a,B,axes=1))

    def dens(y,c):
        gm=metric(y,c); s,r0,_,_=curvature_scalars(lambda yy:metric(yy,c),y)
        # normalized Haar uses dc=d cos(theta), whereas coordinate volume uses dtheta
        return (r0+(s+24.0)**2/4)*jnp.sqrt(jnp.linalg.det(gm))/jnp.sin(y[2])

    def gram_dens(y):
        gm=base_metric(y); gi=jnp.linalg.inv(gm); B,_=data_at(y)
        return jnp.einsum('mij,nkl,ik,jl->mn',B,B,gi,gi)*jnp.sqrt(jnp.linalg.det(gm))/jnp.sin(y[2])

    ys=jnp.stack([p[0] for p in pts]); pws=jnp.asarray([p[1] for p in pts])
    dens_v=jax.vmap(dens,in_axes=(0,None)); gram_v=jax.vmap(gram_dens)
    def obj(c): return 2*jnp.sum(pws*dens_v(ys,c))  # 16pi^2/(8pi^2)
    def gram(): return 2*jnp.einsum('p,pij->ij',pws,gram_v(ys))

    # Haar checks for the fixed F and its full triplet, independent of x.
    favg=np.zeros(3); fgram=np.zeros((3,3))
    for ia,aa in enumerate(alphas):
        for ib,bb in enumerate(betas):
            for ic,cc in enumerate(ec):
                eta=.5*math.acos(float(cc)); ff=np.sqrt(3)*np.asarray(ad_row0(float(aa),float(bb),eta)); ww=wa[ia]*wb[ib]*wc[ic]
                favg += ww*ff; fgram += ww*np.outer(ff,ff)
    meta=dict(x0=x0,X=X,deg=deg,nrad=nrad,nphi=nphi,nqx=nqx,nqa=nqa,fullmult=fullmult,nmult=nmult,na=na,nb=nb,
              haar_mean=favg.tolist(),haar_gram=fgram.tolist())
    return obj,gram,rec,meta


def whiten(H,G):
    ge,gv=np.linalg.eigh((G+G.T)/2); keep=ge>ge.max()*1e-10
    Q=gv[:,keep]/np.sqrt(ge[keep])[None,:]
    Hn=(Q.T@H@Q); Hn=(Hn+Hn.T)/2
    ev,V=np.linalg.eigh(Hn)
    return ev,Q@V,ge,keep


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--nrad',type=int,default=3)
    ap.add_argument('--nphi',type=int,default=8); ap.add_argument('--nqx',type=int,default=96)
    ap.add_argument('--nqa',type=int,default=3); ap.add_argument('--fullmult',action='store_true'); ap.add_argument('--out'); a=ap.parse_args(); t=time.time()
    obj,gram,rec,meta=build(a.record,a.nrad,a.nphi,a.nqx,a.nqa,a.fullmult)
    n=meta['na']+meta['nb']; c0=jnp.zeros(n)
    oj=jax.jit(obj); gj=jax.jit(jax.grad(obj)); hj=jax.jit(jax.hessian(obj)); grj=jax.jit(gram)
    J0=float(oj(c0)); grad=np.asarray(gj(c0)); H=np.asarray(hj(c0)); H=(H+H.T)/2; G=np.asarray(grj()); G=(G+G.T)/2
    na=meta['na']; Haa=H[:na,:na]; Hab=H[:na,na:]; Hbb=H[na:,na:]
    eb=np.linalg.eigvalsh(Hbb)
    # Stable symmetric solve.  A negative Hbb would itself be a conformal descending direction.
    BinvHa=np.linalg.solve(Hbb,H[na:,:na])
    Hrel=Haa-Hab@BinvHa; Hrel=(Hrel+Hrel.T)/2
    eraw,Vraw,ge,keep=whiten(Haa,G); erel,Vrel,_,_=whiten(Hrel,G)
    araw=Vraw[:,0]; arel=Vrel[:,0]; brel=-BinvHa@arel
    # Split metric directions by the sampled first-order scalar coupling.  At an
    # exactly scalar-normalized base Hab is the Galerkin matrix of A Ds[h], with
    # A=-4 Delta+24; ker(Hab^T) therefore means orthogonality against the sampled
    # conformal test space, not the pointwise equation Ds[h]=0.
    Uc,sc,Vhc=np.linalg.svd(Hab.T,full_matrices=True)
    tol_sc=(sc[0] if len(sc) else 1.0)*1e-9
    rsc=int(np.sum(sc>tol_sc)); Nsc=Vhc.T[:,rsc:]
    if Nsc.shape[1]:
        Gsc=Nsc.T@G@Nsc; Hsc=Nsc.T@Haa@Nsc
        esc,Vsc,gesc,ksc=whiten(Hsc,Gsc); asc=Nsc@Vsc[:,0]
    else:
        esc=np.array([]); asc=np.zeros(na)
    draw=np.concatenate([araw,np.zeros(meta['nb'])]); drel=np.concatenate([arel,brel]);
    dsc=np.concatenate([asc,np.zeros(meta['nb'])])
    lines={}
    for name,d in [('raw',draw),('relaxed',drel),('scalar_kernel',dsc)]:
        rr=[]
        for eps in [1e-3,5e-4,2.5e-4,1.25e-4]:
            jp=float(oj(jnp.asarray(eps*d))); jm=float(oj(jnp.asarray(-eps*d)))
            rr.append(dict(eps=eps,Jplus=jp,Jminus=jm,even=(jp+jm-2*J0)/eps**2,odd=(jp-jm)/(2*eps)))
        lines[name]=rr
    out=dict(record=a.record,**meta,J0=J0,stored_J=rec.get('J'),grad_metric_norm=float(np.linalg.norm(grad[:na])),
             grad_conformal_norm=float(np.linalg.norm(grad[na:])),gram_rank=int(keep.sum()),
             gram_eig_min=float(ge[keep].min()),gram_eig_max=float(ge.max()),
             conformal_hessian_min=float(eb.min()),conformal_hessian_max=float(eb.max()),
             scalar_coupling_singular_values=[float(x) for x in sc],scalar_coupling_rank=rsc,
             raw_min=float(eraw[0]),raw_eigenvalues=[float(x) for x in eraw],
             relaxed_min=float(erel[0]),relaxed_eigenvalues=[float(x) for x in erel],
             scalar_kernel_min=(float(esc[0]) if len(esc) else None),scalar_kernel_eigenvalues=[float(x) for x in esc],
             scalar_lowering=float(eraw[0]-erel[0]),lowest_metric_mode=[float(x) for x in arel],
             optimal_conformal_mode=[float(x) for x in brel],line_tests=lines,sec=time.time()-t,
             interpretation='finite j=1 scalar-relaxed construction block at a nearly scalar-normalized numerical base; signs require basis convergence and actual path tests')
    text=json.dumps(out,indent=1); print(text)
    if a.out: Path(a.out).write_text(text+'\n')

if __name__=='__main__': main()
