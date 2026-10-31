"""Odd/triaxial w-sector gradient and Hessian at an H4 biaxial cell."""
import argparse,json,sys
from pathlib import Path
import numpy as np
import jax,jax.numpy as jnp
jax.config.update('jax_enable_x64',True)
sys.path.insert(0,str(Path(__file__).resolve().parent))
from h4_perp_cell import Cell

def main():
 p=argparse.ArgumentParser();p.add_argument('record');p.add_argument('out');a=p.parse_args()
 r=json.loads(Path(a.record).read_text());d=int(r['deg']);c=Cell(float(r['x0']),float(r['X']),d,int(r['nq']));z=np.asarray(r['z'])
 base=jnp.asarray(z[:2*d]);
 def fun(w):return c.costs(jnp.concatenate([base,w]))[0]
 w0=jnp.zeros(d);g=np.asarray(jax.grad(fun)(w0));H=np.asarray(jax.hessian(fun)(w0));ev=np.linalg.eigvalsh(H)
 # regular inverse on positive eigenspace; this predicts local unconstrained gain if H positive.
 sol=np.linalg.lstsq(H,g,rcond=1e-10)[0]; pred=.5*float(g@sol)
 out=dict(record=a.record,P_biaxial=float(fun(w0)),grad_w=g.tolist(),grad_w_norm=float(np.linalg.norm(g)),
          hessian_eigenvalues=ev.tolist(),min_eigenvalue=float(ev[0]),max_eigenvalue=float(ev[-1]),
          newton_predicted_gain=pred,newton_w=(-sol).tolist(),newton_w_norm=float(np.linalg.norm(sol)))
 Path(a.out).write_text(json.dumps(out,indent=1)+'\n');print(json.dumps(out,indent=1))
if __name__=='__main__':main()
