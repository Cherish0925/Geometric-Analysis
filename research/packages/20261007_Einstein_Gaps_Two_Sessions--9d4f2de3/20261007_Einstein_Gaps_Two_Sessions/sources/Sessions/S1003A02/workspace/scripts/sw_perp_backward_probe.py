"""Backward integration of the invariant SW equations from the exact CH collar."""
import json,sys,math
from pathlib import Path
import numpy as np
import jax,jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'Sessions/S1003A01/workspace/scripts')); sys.path.insert(0,str(ROOT/'Sessions/S1003A02/workspace/scripts'))
from perp_dual_cost import make_cell,load_record,seed_vector
REC=ROOT/'Sessions/S1003A01/workspace/data/perp_area/x00.03_X128_d20.json'; rec=load_record(REC)
x0=float(rec['x0']); X=float(rec['X']); deg=int(rec['deg']); cell=make_cell(x0,deg,400,True,X); z=jnp.asarray(seed_vector(cell,rec)); prof=cell.prof_factory(z)
def base(x): G,h=prof(jnp.array(x)); return G,jnp.sqrt(jnp.diag(h))
def geom(x):
 G,A=base(x); Ax=jax.jacfwd(lambda xx:base(xx)[1])(jnp.array(x)); return float(G),np.asarray(A),np.asarray(2*jnp.sqrt(G)*Ax)
def rhs(x,y):
 lr,th,al1,al3=y; G,a,ad=geom(x); W=a.prod(); c=(a@a)/(2*W)-.5*(ad/a).sum(); v1=al1/a[0];v3=al3/a[2];rho=math.exp(np.clip(lr,-700,700)); ct=math.cos(th);st=math.sin(th); dtdx=1/(2*math.sqrt(G))
 return np.array([2*c+v1*ct+v3*st,v3*ct-v1*st,a[0]*rho*ct-2*a[0]*al1/(a[1]*a[2]),a[2]*rho*st-2*a[2]*al3/(a[0]*a[1])])*dtdx
yX=np.array([math.log(12),math.pi/2,0,3*X],float)
sol=solve_ivp(rhs,(X,x0+1e-10),yX,method='Radau',rtol=3e-10,atol=[1e-11,1e-11,1e-11,1e-9],dense_output=True,max_step=1.)
rows=[]
for x in [128,32,8,2,1,.3,.1,.05,.031,.0301,.030001,.0300000001]:
 if x>=sol.t[-1] and x<=sol.t[0]:
  y=sol.sol(x); rows.append([x,*map(float,y),float(math.exp(np.clip(y[0],-700,700)))])
out=dict(success=sol.success,message=sol.message,nfev=sol.nfev,last_x=float(sol.t[-1]),last_y=sol.y[:,-1].tolist(),rows_cols=['x','logrho','theta','alpha1','alpha3','rho'],rows=rows)
print(json.dumps(out,indent=1)); (ROOT/'Sessions/S1003A02/workspace/data/sw_perp_backward_probe.json').write_text(json.dumps(out,indent=1)+'\n')
