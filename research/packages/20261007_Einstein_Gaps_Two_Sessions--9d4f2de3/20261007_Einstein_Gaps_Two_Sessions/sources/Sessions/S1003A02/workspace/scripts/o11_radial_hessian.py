"""High-resolution second variation in the full SU(2)-invariant symmetric-h sector.

The base is an optimized perpendicular fixed-slot cell.  Perturbations are
arbitrary compactly supported variations of G and all six entries of h(x),
expanded in radial Chebyshev bubbles.  This contains the earlier diagonal and
rotating-eigenframe families simultaneously.  The raw generalized Hessian of
P is computed with an L2 Gram matrix.  It is a finite radial spectral test;
diffeomorphism modes are not quotient explicitly, so a negative value would
need a gauge check while a positive value is evidence only in this sector.
"""
import sys,json,time
import numpy as np
import jax,jax.numpy as jnp
jax.config.update('jax_enable_x64',True)
from scipy.linalg import eigh
from numpy.polynomial.legendre import leggauss
from o11_perp_cell import PerpCell
from o11_rotated_cell import metric_from,curvature_scalars,ANG,PI,cheb


def run(path,nmode=6,nq=400):
 o=json.load(open(path));x0=float(o['x0']);X=float(o.get('X',1));du=int(o['degU']);dw=int(o['degw']);z=jnp.array(o['z'])
 c=PerpCell(x0,X,du,dw,nq);c.wpow=int(o.get('wpow',1));c.beta0=np.pi/2-float(o.get('theta',np.pi/2));c.degr=max(0,len(z)-(2*du+dw));c.nparam=len(z);base=c.prof_factory(z);ell=np.log(X/x0)
 e,w=leggauss(nq);u=.5*(e+1);x=x0*np.exp(ell*u);wx=.5*w*ell*x;x=jnp.array(x);wx=jnp.array(wx)
 pairs=[(i,j) for i in range(3) for j in range(i,3)];nd=1+len(pairs);nm=nd*nmode
 def B(xv):
  q=jnp.log(xv/x0)/ell;T=cheb(nmode,2*q-1);b=q*q*(1-q)**3*T
  return b
 def pert(a,xv):
  aa=a.reshape(nd,nmode);b=B(xv);d=jnp.dot(aa[0],b);dh=jnp.zeros((3,3))
  for k,(i,j) in enumerate(pairs):
   v=jnp.dot(aa[1+k],b);dh=dh.at[i,j].set(v)
   if i!=j:dh=dh.at[j,i].set(v)
  return d,dh
 def prof_a(a):
  def f(xv):
   G,h=base(xv);d,dh=pert(a,xv);return G*jnp.exp(d),h+dh
  return f
 def P(a):
  f=prof_a(a);g=metric_from(f)
  def at(xv):
   s,r0,wa,wb=curvature_scalars(g,jnp.concatenate([jnp.array([xv]),ANG]));G,h=f(xv);return r0*PI**2*jnp.sqrt(jnp.linalg.det(h)/G)
  return jnp.sum(jax.vmap(at)(x)*wx)/(8*PI**2)
 def Gram():
  GG=np.zeros((nm,nm))
  for xv,ww in zip(np.array(x),np.array(wx)):
   G,h=base(jnp.array(xv));hi=np.linalg.inv(np.array(h));vol=PI**2*np.sqrt(np.linalg.det(np.array(h))/float(G));b=np.array(B(jnp.array(xv)))
   # radial dG/G variation contributes one scalar square; angular h norm h^{-1}dh h^{-1}dh
   for p in range(nmode):
    GG[p,p:0] # no-op
   qforms=[]
   qforms.append(None)
   for A in range(nd):
    for p in range(nmode):
     if A==0:qforms.append(('g',p))
   # direct pair assembly
   for A in range(nd):
    for p in range(nmode):
     ia=A*nmode+p
     for C in range(nd):
      for r in range(nmode):
       ic=C*nmode+r
       if A==0 and C==0:inn=1.0
       elif A==0 or C==0:inn=0.0
       else:
        M=np.zeros((3,3));i,j=pairs[A-1];M[i,j]=M[j,i]=1 if i!=j else 1
        N=np.zeros((3,3));i,j=pairs[C-1];N[i,j]=N[j,i]=1 if i!=j else 1
        inn=np.einsum('ij,kl,ik,jl',M,N,hi,hi)
       GG[ia,ic]+=ww*vol*b[p]*b[r]*inn/(8*PI**2)
  return GG
 t=time.time();a=jnp.zeros(nm);val=float(P(a));grad=np.array(jax.grad(P)(a));H=np.array(jax.hessian(P)(a));G=Gram();H=(H+H.T)/2;G=(G+G.T)/2;ge,gv=np.linalg.eigh(G);keep=ge>ge.max()*1e-11;Q=gv[:,keep]/np.sqrt(ge[keep])[None,:];Hn=(Q.T@H@Q+Q.T@H.T@Q)/2
 ev,V=np.linalg.eigh(Hn)
 vraw=Q@V[:,0]
 # Follow the lowest normalized mode to distinguish an actual descending
 # direction from a nonstationary-base/Hessian artifact.
 def safeP(tt):
  try:
   vv=float(P(jnp.array(tt*vraw)))
   return vv if np.isfinite(vv) else None
  except Exception:return None
 curve=[(float(tt),safeP(tt)) for tt in [-0.02,-0.01,-0.005,0.0,0.005,0.01,0.02]]
 return dict(cell=path,x0=x0,nmode=nmode,nmodes=nm,rank=int(keep.sum()),P=val,Pcell=o['opt']['P'],grad_l2=float(np.linalg.norm(Q.T@grad)),min_eig=float(ev[0]),negative_count=int((ev<-1e-6).sum()),eigenvalues=ev[:50].tolist(),lowest_mode=vraw.tolist(),lowest_curve=curve,note='all SU(2)-invariant symmetric h and G radial modes; raw before diffeomorphism quotient',sec=time.time()-t)
if __name__=='__main__':
 ans=run(sys.argv[1],int(sys.argv[3]) if len(sys.argv)>3 else 6,int(sys.argv[4]) if len(sys.argv)>4 else 400);json.dump(ans,open(sys.argv[2],'w'),indent=2);print(json.dumps(ans))
