#!/usr/bin/env python3
"""Reconstruct selected Step80 fields and report radial residual/stress profiles."""
import importlib.util,json,sys
from pathlib import Path
import numpy as np
import jax.numpy as jnp
root=Path(__file__).resolve().parents[1]
old=sys.argv[:];sys.argv=[sys.argv[0],'pilot']
spec=importlib.util.spec_from_file_location('s80',root/'scripts'/'step80_joint_base_response.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);sys.argv=old
rows=[]
for R in [2.,4.,6.]:
  for variant in ['shape_only','joint']:
    p=m.make_problem(R,.2,variant,m.W_ENTRY)
    x=np.load(root/'data'/'step80_joint_coefficients_pilot'/f'R{R:g}_{variant}_entry.npy')
    E=np.asarray(p['components'](jnp.asarray(x))[0]);L,Lr,Lrr,Lz,Lzz,Lrz=[np.asarray(q) for q in p['components'](jnp.asarray(x))[1]]
    op=m.exact_op(E); stress=.5*(Lr[2]**2+np.exp(-2*L[0])*Lz[2]**2)
    prof=[]
    for i,r in enumerate(p['r']):
      prof.append({'r':float(r),'op_max_z':float(op[i].max()),'op_mean_z':float(op[i].mean()),
        'stress_max_z':float(stress[i].max()),'Ezz_maxabs_z':float(np.abs(E[2,i]).max()),
        'Err_maxabs_z':float(np.abs(E[0,i]).max()),'Erz_maxabs_z':float(np.abs(E[1,i]).max())})
    rows.append({'R':R,'variant':variant,'profile':prof})
out={'source_coefficients':'step80_joint_coefficients_pilot/*_entry.npy','rows':rows}
p=root/'data'/'step80_residual_atlas.json';p.write_text(json.dumps(out,indent=2));print('wrote',p)
for row in rows:
  top=sorted(row['profile'],key=lambda q:q['op_max_z'],reverse=True)[:5]
  print(row['R'],row['variant'],[(round(q['r'],3),round(q['op_max_z'],3),round(q['stress_max_z'],3)) for q in top])
