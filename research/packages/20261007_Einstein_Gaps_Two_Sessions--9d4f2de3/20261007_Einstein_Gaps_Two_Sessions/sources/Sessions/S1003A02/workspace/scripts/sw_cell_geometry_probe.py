"""Probe the certified perpendicular cell geometry used by the SW boundary problem."""
import json, sys
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'Sessions/S1003A01/workspace/scripts'))
sys.path.insert(0,str(ROOT/'Sessions/S1003A02/workspace/scripts'))
from perp_dual_cost import make_cell,load_record,seed_vector
REC=ROOT/'Sessions/S1003A01/workspace/data/perp_area/x00.03_X128_d20.json'
rec=load_record(REC); x0=float(rec['x0']); X=float(rec['X']); deg=int(rec['deg'])
cell=make_cell(x0,deg,400,smooth_mode=True,X=X); z=jnp.asarray(seed_vector(cell,rec)); prof=cell.prof_factory(z)
def slots_cell(x):
 G,h=prof(x); return G,jnp.sqrt(jnp.diag(h))
def slots_ch(x): return x*(1+x),jnp.sqrt(jnp.array([x,x,x*(1+x)]))
def ev(fn,x):
 G,A=fn(jnp.array(x)); Ax=jax.jacfwd(lambda xx:fn(xx)[1])(jnp.array(x)); return float(G),np.asarray(A),np.asarray(2*jnp.sqrt(G)*Ax)
Gp=float(jax.grad(lambda x:slots_cell(x)[0])(jnp.array(x0+1e-12)))
rows=[]
for x in [x0+1e-12,x0+1e-9,x0+1e-6,.031,.1,1.,10.,127.999,128.,129.,1e3]:
 fn=slots_cell if x<=X else slots_ch
 G,A,Ad=ev(fn,x); W=np.prod(A); c=np.dot(A,A)/(2*W)-.5*np.sum(Ad/A)
 rows.append(dict(x=x,G=G,a=A.tolist(),ad=Ad.tolist(),c=c))
print(json.dumps(dict(x0=x0,X=X,Gp=Gp,rows=rows),indent=1))
