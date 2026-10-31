"""Fast BVP solve for the two invariant monopoles on the certified perpendicular cell.

Uses a precomputed C^1 geometry table and scipy.solve_bvp on the logarithmic cell
coordinate u=log(x/x0)/log(X/x0).  Boundary conditions are bolt regularity and the
canonical complex-hyperbolic monopole at the exact collar x=X.
"""
import json,sys,math
from pathlib import Path
import numpy as np
import jax,jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.integrate import solve_bvp
from scipy.interpolate import CubicSpline
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'Sessions/S1003A01/workspace/scripts'));sys.path.insert(0,str(ROOT/'Sessions/S1003A02/workspace/scripts'))
from perp_dual_cost import make_cell,load_record,seed_vector
REC=ROOT/'Sessions/S1003A01/workspace/data/perp_area/x00.03_X128_d20.json';rec=load_record(REC)
x0=float(rec['x0']);X=float(rec['X']);deg=int(rec['deg']);ell=math.log(X/x0)
cell=make_cell(x0,deg,500,True,X);z=jnp.asarray(seed_vector(cell,rec));prof=cell.prof_factory(z)
def one(x):
 G,h=prof(x); A=jnp.sqrt(jnp.diag(h)); Ax=jax.jacfwd(lambda xx:jnp.sqrt(jnp.diag(prof(xx)[1])))(x); return jnp.r_[G,A,2*jnp.sqrt(G)*Ax]
vone=jax.jit(jax.vmap(one))
ug=np.unique(np.r_[np.geomspace(1e-8,1e-3,800),np.linspace(1e-3,1,3200)])
xg=x0*np.exp(ell*ug); tab=np.asarray(vone(jnp.asarray(xg)))
cs=[CubicSpline(ug,tab[:,j]) for j in range(7)]
def geo(u): return [c(u) for c in cs]
def fun(u,y):
 G,a1,a2,a3,ad1,ad2,ad3=geo(u); W=a1*a2*a3;c=(a1*a1+a2*a2+a3*a3)/(2*W)-.5*(ad1/a1+ad2/a2+ad3/a3);rho=np.exp(np.clip(y[0],-50,50));ct=np.cos(y[1]);st=np.sin(y[1]);v1=y[2]/a1;v3=y[3]/a3;fac=ell*x0*np.exp(ell*u)/(2*np.sqrt(G))
 return fac*np.vstack([2*c+v1*ct+v3*st,v3*ct-v1*st,a1*rho*ct-2*a1*y[2]/(a2*a3),a3*rho*st-2*a3*y[3]/(a1*a2)])
def bc(ya,yb,sigma):
 # Frobenius regularity: alpha1=sigma and n1=-sigma*rho; exact CH collar at X.
 thbolt=math.pi if sigma==1 else 0.
 return np.array([ya[1]-thbolt,ya[2]-sigma,yb[0]-math.log(12),yb[1]-math.pi/2])
def solve(sigma,guess=None):
 u=np.unique(np.r_[np.geomspace(1e-7,1e-3,300),np.linspace(1e-3,1,900)])
 if guess is None:
  y=np.zeros((4,u.size));y[0]=math.log(12); y[1]=(math.pi if sigma==1 else 0)+(math.pi/2-(math.pi if sigma==1 else 0))*u; y[2]=sigma*(1-u); y[3]=3*X*u*u
 else:y=guess(u)
 return solve_bvp(fun,lambda a,b:bc(a,b,sigma),u,y,tol=2e-6,max_nodes=25000,verbose=0)
sp=solve(1);sm=solve(-1)
u=np.unique(np.r_[np.geomspace(1e-7,1e-3,1000),np.linspace(1e-3,1,9000)]);yp=sp.sol(u);ym=sm.sol(u);G,a1,a2,a3,ad1,ad2,ad3=geo(u);W=a1*a2*a3; x=x0*np.exp(ell*u); dtdu=ell*x/(2*np.sqrt(G));rho=np.exp(yp[0]);th=yp[1];al1=yp[2];al3=yp[3];v1=al1/a1;v3=al3/a3;c=(a1*a1+a2*a2+a3*a3)/(2*W)-.5*(ad1/a1+ad2/a2+ad3/a3);q1=-ad1/a1+(a2*a2+a3*a3-a1*a1)/W;q2=-ad2/a2+(a3*a3+a1*a1-a2*a2)/W;q3=-ad3/a3+(a1*a1+a2*a2-a3*a3)/W;n1=rho*np.cos(th);n3=rho*np.sin(th);kin=(c*c+(v1*v1+v3*v3)/4)*rho+c*(v1*n1+v3*n3)+((q1*q1+v1*v1)*rho/4+q1*v1*n1/2)+(q2*q2*rho/4)+((q3*q3+v3*v3)*rho/4+q3*v3*n3/2); dl=2*c+v1*np.cos(th)+v3*np.sin(th);zeta2=(rho*dl)**2/4+.25*((q1*n1+v1*rho)**2+(v1*0+q2*0)**2+(q3*n3+v3*rho)**2);rot=kin-zeta2/rho
# Orbit integral is 2pi^2 int W f dt, hence normalized by 8pi^2 = (1/4) int W f dt.
def integ(f):return float(np.trapezoid(W*f*dtdu,u)/4)
def qloc(frac):
 dens=np.maximum(frac,0)*W*dtdu;cum=np.r_[0,np.cumsum((dens[1:]+dens[:-1])*np.diff(u)/2)];return float(x[np.searchsorted(cum,.5*cum[-1])]) if cum[-1]>0 else None
mirror=max(np.max(np.abs(yp[0]-ym[0])),np.max(np.abs(yp[1]+ym[1]-math.pi)),np.max(np.abs(yp[2]+ym[2])),np.max(np.abs(yp[3]-ym[3])))
out=dict(record=str(REC.relative_to(ROOT)),solver_plus=dict(success=sp.success,status=sp.status,message=sp.message,niter=sp.niter,nodes=sp.x.size,rms_max=float(np.max(sp.rms_residuals))),solver_minus=dict(success=sm.success,status=sm.status,message=sm.message,niter=sm.niter,nodes=sm.x.size,rms_max=float(np.max(sm.rms_residuals))),mirror_max=mirror,P_over_8pi2=float(rec['P']),saving=1-float(rec['P']),diag=dict(rho_bolt=float(rho[0]),rho_bolt_over_12=float(rho[0]/12),rho_min=float(rho.min()),x_rho_min=float(x[rho.argmin()]),theta_min=float(th.min()),theta_max=float(th.max()),K_over_8pi2=integ(kin),weitz_K_constscalar_over_8pi2=integ(rho*(12-rho)/2),zeta_over_rho_over_8pi2=integ(zeta2/rho),rotation_over_8pi2=integ(rot),amplitude_deficit_ricm6_units=integ(6*(12-rho)),pair_w_sq_over_8pi2=integ(n1*n1/2),half_location_K=qloc(kin),half_location_rotation=qloc(rot),half_location_pair=qloc(n1*n1/2)),profile_cols=['x','rho','theta','alpha1','alpha3','kin','rotation','pairw'],profile=np.c_[x[::100],rho[::100],th[::100],al1[::100],al3[::100],kin[::100],rot[::100],(n1*n1/2)[::100]].tolist())
path=ROOT/'Sessions/S1003A02/workspace/data/sw_perp_cell_pair_v2.json';path.write_text(json.dumps(out,indent=1)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='profile'},indent=1))
