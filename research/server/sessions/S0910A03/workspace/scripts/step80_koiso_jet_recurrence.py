#!/usr/bin/env python3
"""Compute/check even Einstein jets for diagonal reflected Koiso data.

For l=(a,b,c) and q_r=diag(e^{2l_i}), exact Gaussian Einstein equations are
  l_i,rr = Ric_i(q_r)+3-H l_i,r.
At r=0: p_i=l_i,rr=Ric_i(q0)+3.  Differentiating twice gives
  w_i=l_i,rrrr = D Ric_i[q''_0] - 2 H_r p_i
                 = D Ric_i[2 diag(p) q0] - 6 p_i,
since H_r=sum p_i=3.  We compute D Ric by centered finite differences in
log-metric variables and test sum w_i=-2 sum p_i^2 from the normal equation.
The output provides a high-order germ target for later inner-layer solvers.
"""
from __future__ import annotations
import importlib.util,json,sys
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parents[1]
old=sys.argv[:];sys.argv=[sys.argv[0],'pilot']
spec=importlib.util.spec_from_file_location('s80',root/'scripts'/'step80_joint_base_response.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);sys.argv=old
# Work on the same projected Fourier center as the pilot so recurrence and run compare exactly.
L0=np.stack((m.center[0],(m.center[1]+m.center[2])/2,(m.center[1]-m.center[2])/2))
# Utilities spectral derivatives on pilot basis.
def proj_derivs(L):
  co=np.stack([np.linalg.lstsq(m.Z_np,q,rcond=None)[0] for q in L])
  return co@m.Z1_np.T,co@m.Z2_np.T
def ric(L):
  Lz,Lzz=proj_derivs(L)
  return m.intrinsic_ric_np(L[0],L[1]+L[2],L[1]-L[2],Lz[0],Lz[1]+Lz[2],Lz[1]-Lz[2],Lzz[0],Lzz[1]+Lzz[2],Lzz[1]-Lzz[2])
R0=ric(L0);p=R0+3
rows=[]
for eps in [1e-2,3e-3,1e-3,3e-4,1e-4,3e-5]:
  # l(eps)=l0+eps*p corresponds metric variation dq/d eps=2p q.
  DR=(ric(L0+eps*p)-ric(L0-eps*p))/(2*eps)
  w=DR-6*p
  normal_rhs=-2*np.sum(p*p,axis=0)
  rows.append({'eps':eps,'w_component_ranges':[[float(x.min()),float(x.max())] for x in w],
    'trace_w_range':[float(w.sum(0).min()),float(w.sum(0).max())],
    'normal_recurrence_sup':float(np.abs(w.sum(0)-normal_rhs).max()),
    'w_sup':float(np.abs(w).max())})
out={'center_projection':{'Kz':m.KZ,'scalar_minus6_sup':float(np.abs(R0.sum(0)+6).max()),
  'trace_p_minus3_sup':float(np.abs(p.sum(0)-3).max())},
  'recurrence':'p=Ric(q0)+3; w=D_Ric[2 p^flat]-6p; sum w=-2 sum p^2',
  'rows':rows}
pth=root/'data'/'step80_koiso_jet_recurrence.json';pth.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2));print('wrote',pth)
