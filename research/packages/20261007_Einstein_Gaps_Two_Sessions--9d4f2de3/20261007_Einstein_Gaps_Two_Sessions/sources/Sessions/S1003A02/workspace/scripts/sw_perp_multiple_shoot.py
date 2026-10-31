"""Multiple-shoot the invariant SW monopole from the bolt to the CH stable manifold.

The bolt regular family has parameters (log rho0,beta).  The ACH stable family is
started at r=R in its two decaying linear modes, scaled to order-one amplitudes at
r=rmatch, and integrated backward.  Four states are matched at rmatch.
"""
import json,sys,math
from pathlib import Path
import numpy as np
import jax,jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
from scipy.interpolate import CubicSpline
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'Sessions/S1003A01/workspace/scripts'));sys.path.insert(0,str(ROOT/'Sessions/S1003A02/workspace/scripts'))
from perp_dual_cost import make_cell,load_record,seed_vector
REC=ROOT/'Sessions/S1003A01/workspace/data/perp_area/x00.03_X128_d20.json';rec=load_record(REC);x0=float(rec['x0']);X=float(rec['X']);deg=int(rec['deg'])
cell=make_cell(x0,deg,500,True,X);z=jnp.asarray(seed_vector(cell,rec));prof=cell.prof_factory(z);r0=math.asinh(math.sqrt(x0));rX=math.asinh(math.sqrt(X))
def one(r):
 x=jnp.sinh(r)**2;G,h=prof(x);A=jnp.sqrt(jnp.diag(h));Ax=jax.jacfwd(lambda xx:jnp.sqrt(jnp.diag(prof(xx)[1])))(x);return jnp.r_[G,A,2*jnp.sqrt(G)*Ax]
# Dense geometric table on [rL,rX].
Gp=float(jax.grad(lambda xx:prof(xx)[0])(jnp.array(x0+1e-12))); eps_t=2e-5;xL=x0+Gp*eps_t**2;rL=math.asinh(math.sqrt(xL))
rg=np.unique(np.r_[r0+(rX-r0)*np.geomspace((rL-r0)/(rX-r0),1e-3,1000),np.linspace(r0+(rX-r0)*1e-3,rX,5000)])
tab=np.asarray(jax.jit(jax.vmap(one))(jnp.asarray(rg)));cs=[CubicSpline(rg,tab[:,j]) for j in range(7)]
def geo(r):
 if r<=rX:return [float(c(r)) for c in cs]
 x=math.sinh(r)**2;return x*(1+x),math.sinh(r),math.sinh(r),math.sinh(r)*math.cosh(r),math.cosh(r),math.cosh(r),math.cosh(2*r)
def rhs(r,y):
 lr,th,al1,al3=y;G,a1,a2,a3,d1,d2,d3=geo(r);W=a1*a2*a3;c=(a1*a1+a2*a2+a3*a3)/(2*W)-.5*(d1/a1+d2/a2+d3/a3);rho=math.exp(np.clip(lr,-40,40));ct=math.cos(th);st=math.sin(th);fac=math.sqrt((math.sinh(r)**2)*(math.cosh(r)**2)/G)
 return fac*np.array([2*c+(al1/a1)*ct+(al3/a3)*st,(al3/a3)*ct-(al1/a1)*st,a1*rho*ct-2*a1*al1/(a2*a3),a3*rho*st-2*a3*al3/(a1*a2)])
rmatch=1.15;R=5.2;lamS=2+math.sqrt(13)
def bolt(par,dense=False):
 lam,beta=par;rho0=math.exp(lam);b=math.sqrt(x0);t=eps_t;sig=1.;y=np.array([lam,math.pi-beta*t,sig*(1-(rho0/2+1/x0)*t*t),b*rho0*beta*t*t/4]);return solve_ivp(rhs,(rL,rmatch),y,method='DOP853',rtol=2e-10,atol=2e-12,dense_output=dense,max_step=.02)
def stable(par,dense=False):
 qL,qT=par;d=R-rmatch;L=qL*math.exp(-6*d);delta=qT*math.exp(-lamS*d);x=math.sinh(R)**2;B=-6*L;A=(math.sqrt(13)-1)*delta;y=np.array([math.log(12)+L,math.pi/2+delta,A*math.sinh(R),3*x+B*math.sinh(R)*math.cosh(R)]);return solve_ivp(rhs,(R,rmatch),y,method='DOP853',rtol=2e-10,atol=2e-12,dense_output=dense,max_step=.02)
def residual(p,verbose=False):
 try:
  f=bolt(p[:2]);s=stable(p[2:]);
  if not f.success or not s.success:return np.ones(4)*1e3
  yf=f.y[:,-1];ys=s.y[:,-1];sc=np.array([1.,1.,1.,1/max(1,3*math.sinh(rmatch)**2)]);res=(yf-ys)*sc
  if not np.all(np.isfinite(res)):return np.ones(4)*1e3
  if verbose:print('p',p,'yf',yf,'ys',ys,'res',res,flush=True)
  return res
 except Exception:return np.ones(4)*1e3
starts=[]
for lam in [math.log(.5),math.log(2),math.log(6),math.log(12)]:
 for beta in [.2,1,3,6]:starts.append([lam,beta,0,0])
best=None
for p0 in starts:
 rr=least_squares(residual,p0,bounds=([-8,-20,-100,-100],[4,20,100,100]),xtol=2e-11,ftol=2e-11,gtol=2e-11,max_nfev=500,x_scale='jac')
 print('start',p0,'ans',rr.x,'cost',rr.cost,'opt',rr.optimality,flush=True)
 if best is None or rr.cost<best.cost:best=rr
residual(best.x,True)
out=dict(record=str(REC.relative_to(ROOT)),r0=r0,rL=rL,rX=rX,rmatch=rmatch,R=R,parameters=best.x.tolist(),cost=float(best.cost),residual=residual(best.x).tolist(),success=bool(best.cost<1e-10),nfev=int(best.nfev),message=best.message)
path=ROOT/'Sessions/S1003A02/workspace/data/sw_perp_multiple_shoot.json';path.write_text(json.dumps(out,indent=1)+'\n');print(json.dumps(out,indent=1))
