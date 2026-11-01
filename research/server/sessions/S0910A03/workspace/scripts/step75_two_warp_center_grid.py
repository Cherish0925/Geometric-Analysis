#!/usr/bin/env python3
"""Two-warp scalar-minus-six center grid: p=A sin z, q=B sin z."""
from __future__ import annotations
import importlib.util,json,sys,time
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution,minimize
p=Path(__file__).resolve().parent/'step75_general_center_shape_search.py'
old=sys.argv[:];sys.argv=[sys.argv[0],'pilot']
s=importlib.util.spec_from_file_location('gc',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);sys.argv=old
m.K=1;m.cache={}

def ev(A,B,dense=False):return m.evalc(np.array([A,B]),dense)
def main():
 t0=time.time(); vals=[]
 grid=np.linspace(-8,8,9)
 for A in grid:
  for B in grid:
   if abs(A)+abs(B)<.2:continue
   r=ev(A,B,False);vals.append(r);print(f"A={A:g} B={B:g} E={r.get('E_op_sup',1e5):.5g}",flush=True)
 good=sorted([r for r in vals if r.get('success')],key=lambda r:r['objective_smooth'])
 starts=good[:6];ref=[]
 for r in starts:
  x=np.array([r['coeff_p'][0],r['coeff_q'][0]])
  z=minimize(lambda y:m.obj(y),x,method='Nelder-Mead',options={'maxiter':180,'xatol':2e-5,'fatol':2e-5})
  ref.append({'start':x.tolist(),'x':z.x.tolist(),'fun':float(z.fun),'dense':ev(*z.x,True),'message':str(z.message)})
 best=min(ref,key=lambda x:x['dense']['E_op_sup'])
 out={'scope':'p=A sin z, q=B sin z finite grid/local search; not an infimum','topological_lower_bound':1,
  'grid':grid.tolist(),'top_grid':good[:20],'refinements':ref,'best':best,'wall_s':time.time()-t0}
 path=Path(__file__).resolve().parents[1]/'data'/'step75_two_warp_center_grid.json';path.write_text(json.dumps(out,indent=2),encoding='utf-8')
 print('BEST',json.dumps(best,indent=2));print('wrote',path)
if __name__=='__main__':main()
