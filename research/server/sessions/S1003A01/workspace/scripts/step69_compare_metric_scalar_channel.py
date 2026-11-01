#!/usr/bin/env python3
"""Step 69: compare the exact torsion-polarization map with the full Darboux metric channel.

For d=4,6,8 at the rational strict-cone first jet, form
 M_metric = P_d [ B(H2,k)-lambda k ], k in ker L_{d-2}
using A02's exact nonlinear metric engine (floating evaluation), and compare its
row/column space with the exact map obtained by
 ker L_{d-2} -> principal torsion v=z h(bar z)+g(bar z) -> DR(f1)[v].

Equality is tested up to one global nonzero normalization.  Since P_d is an
exact coefficient extraction but the metric engine is float64, residuals are
reported relative to ||M_metric||.
"""
from pathlib import Path
import json,sys
import numpy as np
import torch
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE)); sys.path.insert(0,str(HERE.parents[2]/'S1003A02'/'workspace'/'scripts'))
from step78_real_tower import Tower
from step77_gn_germ import dev,dt
from step68_scalar_compatibility import P_matrix
import step68_flat_cokernel as F
import step69_top_channel_exact as X

OUT=HERE.parent/'data'/'step69'; OUT.mkdir(parents=True,exist_ok=True)
A02=HERE.parents[2]/'S1003A02'/'workspace'/'data'/'step80'


def null_right(A,tol=1e-10):
 U,s,Vt=np.linalg.svd(A,full_matrices=True); r=int((s>tol*s[0]).sum()); return Vt[r:].T


def metric_map(d,H2,lam,K):
 T=Tower(d,lam); T.degs=list(range(2,T.N+1)); T.size={e:6*len(T.mon_d[e]) for e in T.degs}
 h2=torch.tensor(H2,dtype=dt,device=dev); z=torch.zeros(T.size[d],dtype=dt,device=dev)
 f=lambda k:T.Evec({2:h2,d:k},[d])[0]
 Kt=torch.tensor(K,dtype=dt,device=dev)
 cols=[]
 for s in range(0,K.shape[1],128):
  blk=Kt[:,s:s+128].T
  val=torch.func.vmap(lambda v:torch.func.jvp(f,(z,),(v,))[1])(blk).T
  cols.append(val)
 DK=torch.cat(cols,dim=1).cpu().numpy()
 return P_matrix(d).astype(float)@DK


def main():
 name='recon_F012_gen5_lam-5'; dd=np.load(A02/f'{name}.npz'); H2=dd['H2']; lam=-5.0
 recs=[]
 c=1+0j; B=np.array([[2,3+2j],[-1-2j,1+1j]])
 # The selected rational (c,B) does not equal gen5 H2.  Build its exact H2 by
 # solving E0 and torsion constraints in A02 coordinates, keeping the minimum-norm W- part.
 # We use step79_general_order6.make_H2 for the established dictionary.
 import step79_general_order6 as G
 for d in (4,6,8):
  T0=Tower(d,lam)
  H2r=G.make_H2(T0,'jet',lam,np.random.default_rng(0),jet=(c,np.array([[2,1],[1,1+1j]],complex),np.array([[0,2+2j],[-2-2j,0]],complex)),scale=1.0,wscale=0.0)
  H2r=H2r.cpu().numpy()
  K=null_right(F.L_matrix(d-2).astype(float))
  Mm=metric_map(d,H2r,lam,K)
  ex=np.load(OUT/f'top_channel_d{d}.npz'); Mt=ex['induced']
  # rows in both are ordinary x-monomial order from F.mons_deg, columns use the
  # same nullspace only up to basis.  Recompute exact torsion map on floating K:
  Ttor=np.array(X.torsion_matrix(d)).astype(float)
  Hht=ex['H']; A=ex['Aform']
  coords=np.linalg.lstsq(Hht,Ttor@K,rcond=1e-12)[0]
  Mt=A@coords
  alpha=float(np.vdot(Mt,Mm).real/np.vdot(Mt,Mt).real)
  rel=float(np.linalg.norm(Mm-alpha*Mt)/np.linalg.norm(Mm))
  # compare row/column ranges independent of scale
  sm=np.linalg.svd(Mm,compute_uv=False); st=np.linalg.svd(Mt,compute_uv=False)
  rm=int((sm>1e-9*sm[0]).sum()); rt=int((st>1e-9*st[0]).sum())
  Um=np.linalg.svd(Mm,full_matrices=False)[0][:,:rm]; Ut=np.linalg.svd(Mt,full_matrices=False)[0][:,:rt]
  cos=np.linalg.svd(Um.T@Ut,compute_uv=False)
  rec={'d':d,'rank_metric':rm,'rank_torsion_formula':rt,'best_scale':alpha,'relative_matrix_error_after_scale':rel,
       'principal_angle_cosines_min':float(cos.min()),'principal_angle_cosines_max':float(cos.max()),
       'metric_sv_top':float(sm[0]),'metric_sv_first_null':float(sm[rm]) if rm<len(sm) else 0.0}
  recs.append(rec); print(json.dumps(rec),flush=True)
 (OUT/'metric_vs_torsion_channel.json').write_text(json.dumps({'records':recs},indent=2)+'\n')

if __name__=='__main__':main()
