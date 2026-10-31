"""Non-SU(2) second-variation pilot around an O11 perpendicular cell.

Unlike o11_full_hessian.py, perturbations are specified in the geometrically
natural coframe (dx,s1,s2,s3), then converted to Euler coordinates.  The Euler
angular measure is used directly, so the quadrature reproduces the existing
cell P.  Modes are compactly supported products of radial bubbles and low
angular functions.  The output is the raw generalized Hessian spectrum of
P=int|Ric0|^2/(8pi^2); it has not yet been quotient by diffeomorphisms.
"""
import sys,json,time
import numpy as np
import jax,jax.numpy as jnp
jax.config.update('jax_enable_x64',True)
from scipy.linalg import eigh
from numpy.polynomial.legendre import leggauss
from o11_perp_cell import PerpCell
from o11_rotated_cell import euler_E,curvature_scalars,PI


def build(path,nr=1,angular='constant',nqx=26,nqa=2):
 o=json.load(open(path));x0=float(o['x0']);X=float(o.get('X',1.));du=int(o['degU']);dw=int(o['degw']);z=jnp.array(o['z'])
 c=PerpCell(x0,X,du,dw,300);c.wpow=int(o.get('wpow',1));c.beta0=np.pi/2-float(o.get('theta',np.pi/2));c.degr=max(0,len(z)-(2*du+dw));c.nparam=len(z);prof=c.prof_factory(z)
 comps=[(i,j) for i in range(4) for j in range(i,4)]
 if angular=='constant': af=[lambda q:jnp.array(1.)]
 else: af=[lambda q:jnp.array(1.),lambda q:jnp.cos(q[0]),lambda q:jnp.sin(q[0]),lambda q:jnp.cos(q[1]),lambda q:jnp.sin(q[1])*jnp.cos(q[2]),lambda q:jnp.sin(q[1])*jnp.sin(q[2])]
 nm=nr*len(af)*len(comps);ell=np.log(X/x0)
 ex,wx=leggauss(nqx);u=.5*(ex+1);xs=x0*np.exp(ell*u);wx=.5*wx*ell*xs
 ep,wp=leggauss(nqa);psis=np.pi*(ep+1);wps=np.pi*wp
 et,wt=leggauss(nqa);ths=.5*np.pi*(et+1);wts=.5*np.pi*wt
 ef,wf=leggauss(nqa);phs=np.pi*(ef+1);wfs=np.pi*wf
 pts=[]
 for ix,x in enumerate(xs):
  for i,p in enumerate(psis):
   for j,t in enumerate(ths):
    for k,f in enumerate(phs):pts.append((jnp.array([x,p,t,f]),float(wx[ix]*wps[i]*wts[j]*wfs[k])))
 def rb(k,x):
  q=jnp.log(x/x0)/ell;return (q*(1-q))**2*jnp.cos(k*jnp.pi*q)
 def C(q):
  E=euler_E(q[1:]); return jnp.block([[jnp.ones((1,1)),jnp.zeros((1,3))],[jnp.zeros((3,1)),E]])
 def B(q):
  vals=[]
  for k in range(nr):
   for f in af:
    amp=rb(k,q[0])*f(q[1:]);Cc=C(q)
    for i,j in comps:
     M=jnp.zeros((4,4)).at[i,j].set(amp)
     if i!=j:M=M.at[j,i].set(amp)
     vals.append(Cc.T@M@Cc)
  return jnp.stack(vals)
 def g0(q):
  G,h=prof(q[0]);E=euler_E(q[1:]);gm=jnp.zeros((4,4)).at[0,0].set(1/(4*G));return gm.at[1:,1:].set(E.T@h@E)
 def metric(q,a):return g0(q)+jnp.tensordot(a,B(q),axes=1)
 def dens(q,a):
  gm=metric(q,a);s,r0,wa,wb=curvature_scalars(lambda y:metric(y,a),q);return r0*jnp.sqrt(jnp.linalg.det(gm))
 def obj(a):
  v=0.
  for q,w in pts:v+=w*dens(q,a)
  return v/(8*PI**2)
 def gram():
  V=jnp.zeros((nm,nm))
  for q,w in pts:
   gm=g0(q);gi=jnp.linalg.inv(gm);bb=B(q);V+=w*jnp.einsum('mij,nkl,ik,jl->mn',bb,bb,gi,gi)*jnp.sqrt(jnp.linalg.det(gm))
  return V/(8*PI**2)
 t=time.time();a=jnp.zeros(nm);val=float(obj(a));gr=np.array(jax.grad(obj)(a));H=np.array(jax.hessian(obj)(a));G=np.array(gram());H=(H+H.T)/2;G=(G+G.T)/2
 ge,gv=np.linalg.eigh(G);keep=ge>ge.max()*1e-10;Q=gv[:,keep]/np.sqrt(ge[keep])[None,:];ee=np.linalg.eigvalsh((Q.T@H@Q+Q.T@H.T@Q)/2)
 return dict(cell=path,x0=x0,nr=nr,angular=angular,nmodes=nm,rank=int(keep.sum()),P_quad=val,P_cell=o['opt']['P'],grad_l2=float(np.linalg.norm(Q.T@gr)),min_eig=float(ee[0]),negative_count=int((ee<-1e-6).sum()),eigenvalues=ee[:40].tolist(),note='geometric-coframe raw Hessian; diffeomorphism quotient not yet imposed',sec=time.time()-t)
if __name__=='__main__':
 ans=build(sys.argv[1],int(sys.argv[3]) if len(sys.argv)>3 else 1,sys.argv[4] if len(sys.argv)>4 else 'constant');json.dump(ans,open(sys.argv[2],'w'),indent=2);print(json.dumps(ans))
