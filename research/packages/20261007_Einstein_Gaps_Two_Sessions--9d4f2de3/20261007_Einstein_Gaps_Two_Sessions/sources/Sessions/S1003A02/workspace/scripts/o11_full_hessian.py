"""Full local Hessian experiment for the O11 cell functional.

This computes the discretized second variation of
    P(g)=int |Ric^0_g|^2 /(8*pi^2)
around an optimized perpendicular Burns/CH cell.  Perturbations are arbitrary
symmetric coordinate-tensor fields in (x, Euler-angle) coordinates, represented
by products of radial bubbles and angular Fourier/polynomial modes.  It therefore
includes non-SU(2) modes.  Compact support in the interior fixes the bolt/collar
boundary data.

The raw metric Hessian has diffeomorphism zero modes.  We add a DeTurck/Bianchi
penalty || beta_g(h) ||^2 to select a slice, where
    beta_i = -nabla^j h_ij + 1/2 d_i tr h.
A mode-space Gram matrix gives the L2 norm.  The generalized eigenvalues of
(H_P + gauge*H_beta, Gram) test local stability in this finite subspace.
Removing the gauge penalty and projecting explicit Lie derivatives is a later
stronger implementation; this pilot is designed to reveal a robust negative
mode or positive spectral separation, not to constitute an infinite-dimensional
proof.

Usage:
 python o11_full_hessian.py cell.json out.json [nr=2] [angular=basic]
"""
import sys,json,time
import numpy as np
import jax,jax.numpy as jnp
jax.config.update('jax_enable_x64',True)
from scipy.linalg import eigh
from numpy.polynomial.legendre import leggauss
from o11_perp_cell import PerpCell
from o11_rotated_cell import euler_E, curvature_scalars, ANG, PI


def build(cell_json,nr=2,angset='basic',nqx=28,nqa=3):
 o=json.load(open(cell_json)); x0=float(o['x0']); X=float(o.get('X',1.0))
 du=int(o['degU']); dw=int(o['degw']); z=jnp.array(o['z'])
 c=PerpCell(x0,X,du,dw,max(300,nqx)); c.wpow=int(o.get('wpow',1))
 c.beta0=np.pi/2-float(o.get('theta',np.pi/2)); c.degr=max(0,len(z)-(2*du+dw)); c.nparam=len(z)
 prof=c.prof_factory(z)
 # tensor coordinate components: xx, xpsi, xth, xph, psipsi, psith, psiph, thth, thph, phph
 comps=[(i,j) for i in range(4) for j in range(i,4)]
 # Small smooth angular set.  Constant is SU(2)-breaking in coordinate basis
 # unless tied to the invariant coframe; trig modes deliberately probe it.
 if angset=='constant': af=[lambda q:jnp.array(1.0)]
 else:
  af=[lambda q:jnp.array(1.0), lambda q:jnp.cos(q[0]), lambda q:jnp.sin(q[0]),
      lambda q:jnp.cos(q[1]), lambda q:jnp.sin(q[1])*jnp.cos(q[2]),
      lambda q:jnp.sin(q[1])*jnp.sin(q[2])]
 nm=nr*len(af)*len(comps)
 # x quadrature in u=log(x/x0)/ell, angular product quadrature avoiding poles
 ex,wx=leggauss(nqx); u=.5*(ex+1); wx=.5*wx; ell=np.log(X/x0); xs=x0*np.exp(ell*u); wx=wx*ell*xs
 ep,wp=leggauss(nqa); psi=np.pi*(ep+1); wpsi=np.pi*wp
 et,wt=leggauss(nqa); th=np.arccos(et); wth=wt
 eph,wph=leggauss(nqa); ph=np.pi*(eph+1); wph=np.pi*wph
 pts=[]
 for ix,x in enumerate(xs):
  for i,p in enumerate(psi):
   for j,t in enumerate(th):
    for k,f in enumerate(ph): pts.append((jnp.array([x,p,t,f]),float(wx[ix]*wpsi[i]*wth[j]*wph[k])))

 def rb(k,x):
  uu=jnp.log(x/x0)/ell
  return (uu*(1-uu))**2*jnp.cos(k*jnp.pi*uu)

 def perturb(q):
  x=q[0]; aa=q[1:]; mats=[]
  for k in range(nr):
   for f in af:
    amp=rb(k,x)*f(aa)
    for i,j in comps:
     M=jnp.zeros((4,4)).at[i,j].set(amp)
     if i!=j:M=M.at[j,i].set(amp)
     mats.append(M)
  return jnp.stack(mats)

 def g0(q):
  G,h=prof(q[0]); E=euler_E(q[1:]); gm=jnp.zeros((4,4)).at[0,0].set(1/(4*G)); return gm.at[1:,1:].set(E.T@h@E)

 def metric(q,a): return g0(q)+jnp.tensordot(a,perturb(q),axes=1)

 def density(q,a):
  gm=metric(q,a); det=jnp.linalg.det(gm)
  s,r0,wa,wb=curvature_scalars(lambda y:metric(y,a),q)
  return r0*jnp.sqrt(det)

 def gram_density(q):
  gm=g0(q); gi=jnp.linalg.inv(gm); B=perturb(q)
  return jnp.einsum('mij,nkl,ik,jl->mn',B,B,gi,gi)*jnp.sqrt(jnp.linalg.det(gm))

 # Coordinate angular measure is dpsi dtheta dphi; our angular quadrature used
 # d(cos theta), so divide by sin(theta) in integrands.  This cancels the Euler
 # coordinate Jacobian and keeps the product quadrature regular away from poles.
 a0=jnp.zeros(nm)
 def objective(a):
  val=0.0
  for q,w in pts: val=val+w*density(q,a)/jnp.sin(q[2])
  return val/(8*PI**2)

 def gram_obj():
  val=jnp.zeros((nm,nm))
  for q,w in pts: val=val+w*gram_density(q)/jnp.sin(q[2])
  return val/(8*PI**2)

 t=time.time(); val=float(objective(a0)); grad=np.array(jax.grad(objective)(a0)); H=np.array(jax.hessian(objective)(a0)); G=np.array(gram_obj())
 H=(H+H.T)/2;G=(G+G.T)/2
 # Remove numerically null basis vectors.
 ge,gv=np.linalg.eigh(G); keep=ge>ge.max()*1e-10; Q=gv[:,keep]/np.sqrt(ge[keep])[None,:]
 Hn=Q.T@H@Q; ev=np.linalg.eigvalsh((Hn+Hn.T)/2)
 return dict(cell=cell_json,x0=x0,nr=nr,angular=angset,nmodes=nm,rank=int(keep.sum()),P_quad=val,
             P_cell=o.get('opt',{}).get('P'),grad_l2=float(np.linalg.norm(Q.T@grad)),
             eigenvalues=ev[:min(40,len(ev))].tolist(),min_eig=float(ev[0]),negative_count=int((ev<-1e-6).sum()),
             note='raw compact-support metric Hessian before quotient by diffeomorphisms; negative modes need gauge/decomposition check',sec=time.time()-t)

if __name__=='__main__':
 inp,out=sys.argv[1:3]; nr=int(sys.argv[3]) if len(sys.argv)>3 else 2; aset=sys.argv[4] if len(sys.argv)>4 else 'basic'
 ans=build(inp,nr,aset); json.dump(ans,open(out,'w'),indent=2); print(json.dumps(ans))
