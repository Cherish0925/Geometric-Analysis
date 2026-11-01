#!/usr/bin/env python3
"""Polish the Step-68 gen5, lambda=-5 order-8 finite jet.

Unknowns v=(H4,H6,H8) in the same scaled coordinates as the homotopy.
Solve the square/underdetermined reduced system
  C=(E2,E4,E6)=0, R=P8(E8)=0
with rank-revealing minimum-norm Newton and iterative refinement.  Reconstruct
H10 by a minimum-norm solve of L8 H10=-E8 and record full unreduced residuals.
This is floating verification, not interval certification.
"""
from pathlib import Path
import json,sys,time
import numpy as np
import torch
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE));sys.path.insert(0,str(HERE.parents[2]/'S1003A02'/'workspace'/'scripts'))
from step78_real_tower import Tower
from step77_gn_germ import dev,dt
from step68_scalar_compatibility import P_matrix
import step68_flat_cokernel as F
OUT=HERE.parent/'data'/'step69'; OUT.mkdir(parents=True,exist_ok=True)


def main(name='recon_F012_gen5_lam-5',maxit=20):
 lam=float(name.split('lam')[-1]); base=HERE.parents[2]/'S1003A02'/'workspace'/'data'/'step80'
 dd=np.load(base/f'{name}.npz'); T=Tower(8,lam);T.degs=list(range(2,T.N+1));T.size={e:6*len(T.mon_d[e]) for e in T.degs}
 tt=lambda a:torch.tensor(np.asarray(a),dtype=dt,device=dev)
 H2=tt(dd['H2']); sizes=[T.size[4],T.size[6],T.size[8]]; n=sum(sizes)
 vbase=torch.cat([tt(dd['H4']),tt(dd['H6']),tt(dd['H8'])])
 vf=tt(np.load(HERE.parent/'data'/'step68'/f'order8_homotopy_v_{name}.npy'))
 scale=torch.cat([torch.full((s,),float(dd[k].std()),dtype=dt,device=dev) for s,k in zip(sizes,['H4','H6','H8'])])
 x=(vf-vbase)/scale
 P8n=P_matrix(8).astype(float); P8n=P8n/np.linalg.norm(P8n,axis=1,keepdims=True);P8=tt(P8n)
 nC=10*sum(len(T.mon_d[k]) for k in (2,4,6))
 def jets(v,h10=None):
  J={2:H2,4:v[:sizes[0]],6:v[sizes[0]:sizes[0]+sizes[1]],8:v[sizes[0]+sizes[1]:]}
  if h10 is not None:J[10]=h10
  return J
 def fun(x):
  E=T.Evec(jets(vbase+scale*x),[2,4,6,8])[0]
  return torch.cat([E[:nC],P8@E[nC:]])
 eye=torch.eye(n,dtype=dt,device=dev)
 def jac(x):
  vj=torch.func.vmap(lambda e:torch.func.jvp(fun,(x,),(e,))[1])
  return torch.cat([vj(eye[s:s+64]).T for s in range(0,n,64)],dim=1)
 hist=[]; t0=time.time()
 for it in range(maxit):
  r=fun(x); nr=float(r.norm()); J=jac(x); U,s,Vh=torch.linalg.svd(J,full_matrices=False)
  keep=s>1e-12*s[0]
  dx=-(Vh[keep].T@((U[:,keep].T@r)/s[keep]))
  # backtrack only if needed
  alpha=1.0; nn=float(fun(x+alpha*dx).norm())
  while nn>=nr and alpha>2**-12:
   alpha*=.5; nn=float(fun(x+alpha*dx).norm())
  x=x+alpha*dx
  rec={'it':it,'res':nr,'next':nn,'alpha':alpha,'rank':int(keep.sum()),'sv_min_kept':float(s[keep][-1]),'sv_max':float(s[0]),'dx_norm':float(dx.norm()),'time':time.time()-t0}
  hist.append(rec);print(json.dumps(rec),flush=True)
  if nn<1e-10:break
 v=vbase+scale*x
 E8=T.Evec(jets(v),[8])[0].cpu().numpy(); L8=F.L_matrix(8).astype(float)/2
 h10=-np.linalg.lstsq(L8,E8,rcond=1e-12)[0];Jj=jets(v,tt(h10))
 unreduced={f'E{k}':float(T.Evec(Jj,[k])[0].norm()) for k in range(9)}
 coeff={str(d):float(Jj[d].norm()) for d in (2,4,6,8,10)}
 # singular spectrum at polished point
 rr=fun(x);JJ=jac(x);ss=torch.linalg.svdvals(JJ).cpu().numpy(); rank=int((ss>1e-12*ss[0]).sum())
 out={'name':name,'lam':lam,'hist':hist,'reduced_final':float(rr.norm()),'rank_final':rank,
      'sv_max_final':float(ss[0]),'sv_min_kept_final':float(ss[rank-1]),'sv_first_null_final':float(ss[rank]) if rank<len(ss) else 0.0,
      'unreduced':unreduced,'coef_norms':coeff,
      'relative_residuals':{k:unreduced[k]/max(coeff.values()) for k in unreduced}}
 np.save(OUT/f'order8_polished_v_{name}.npy',v.cpu().numpy());np.save(OUT/f'order8_polished_h10_{name}.npy',h10)
 (OUT/f'order8_polished_{name}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ['reduced_final','rank_final','sv_min_kept_final','unreduced','coef_norms']},indent=2))

if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'recon_F012_gen5_lam-5',int(sys.argv[2]) if len(sys.argv)>2 else 20)
