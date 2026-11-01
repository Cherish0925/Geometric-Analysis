#!/usr/bin/env python3
"""Step 72b: test the five admissible torsion-free H2/W^-(0) directions with lower corrections.

The Step-72a full-tangent null basis displayed no visible H2 motion after one set of constraints, but that
basis-dependent observation does not decide the degree-two quotient.  Here we answer the intended question
directly by computing ker(dE0,dN1) on H2 and quotienting Hamiltonian gauge.

At the gen5 lambda=-5 H2, compute ker(dE0,dN1) and quotient the degree-2 Hamiltonian gauge.  For each
remaining physical H2 direction a, solve the lower linearized Einstein equations successively by allowing
H4,...,H_K corrections, then evaluate dR_K=P_K dE_K.  We report whether the physical space has the expected
five W^-(0) directions and whether its image, especially the radial row, survives.  This remains a
first-order fixed-Darboux calculation; finite nonlinear motion and covariant torsion modulo pullback are
separate questions.
"""
from pathlib import Path
import sys,json,time,numpy as np,torch
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE));sys.path.insert(0,str(HERE.parents[2]/'S1003A02'/'workspace'/'scripts'))
from step78_real_tower import Tower
from step77_gn_germ import dev,dt,J0
from step68_scalar_compatibility import P_matrix
from step71_fibre_test import expH,nijenhuis
from step71_fibre_split import gauge_basis
OUT=HERE.parent/'data'/'step72';OUT.mkdir(parents=True,exist_ok=True)

def null(M,rtol=1e-9):
 u,s,vh=torch.linalg.svd(M,full_matrices=True); r=int((s>rtol*max(float(s[0]),1e-300)).sum()); return vh[r:].T,s,r

def main(K=6,name='recon_F012_gen5_lam-5'):
 t0=time.time();lam=float(name.split('lam')[-1]);base=HERE.parents[2]/'S1003A02'/'workspace'/'data'/'step80';dd=np.load(base/f'{name}.npz')
 T=Tower(K,lam);T.degs=list(range(2,T.N+1));T.size={e:6*len(T.mon_d[e]) for e in T.degs};tt=lambda a:torch.tensor(np.asarray(a),dtype=dt,device=dev)
 v=np.load(HERE.parent/'data'/'step69'/f'order8_polished_v_{name}.npy');s4,s6=6*35,6*84;parts={2:dd['H2'],4:v[:s4],6:v[s4:s4+s6],8:v[s4+s6:]}
 degs=list(range(2,K+1,2));sizes=[T.size[d] for d in degs];off={d:o for d,o in zip(degs,np.cumsum([0]+sizes[:-1]).tolist())};x0=torch.cat([tt(parts[d]) for d in degs]);n=x0.numel();J0t=tt(J0)
 iu=[(i,j) for i in range(4) for j in range(i+1,4)];idx1=torch.tensor(T.mon_d[1],device=dev);PK=tt(P_matrix(K).astype(float)/2)
 def jets(x):return {d:x[off[d]:off[d]+T.size[d]] for d in degs}
 def Eorder(k):return lambda x:T.Evec(jets(x),[k])[0]
 def N1(x):
  g=expH(T.R,T.H(jets(x)));Jm=torch.einsum('ab,bjp->ajp',J0t,g);N=nijenhuis(T.R,Jm)
  return torch.stack([N[a,i,j][idx1] for a in range(4) for (i,j) in iu]).reshape(-1)
 eye=torch.eye(n,dtype=dt,device=dev)
 def jac(f):
  vs=torch.func.vmap(lambda e:torch.func.jvp(f,(x0,),(e,))[1]);return torch.cat([vs(eye[s:s+64]).T for s in range(0,n,64)],1)
 JE={k:jac(Eorder(k)) for k in range(0,K+1,2)};JN=jac(N1);JR=PK@JE[K]
 sl=lambda d:slice(off[d],off[d]+T.size[d])
 # raw H2 solutions of dE0=0 and dN1=0
 A2=torch.cat([JE[0][:,sl(2)],JN[:,sl(2)]],0); Z2,sa,rA=null(A2)
 G2,resid,rg=gauge_basis(T,2);G2=tt(G2)
 # gauge subspace within Z2 and its orthogonal complement in coefficient space
 # Remove projections onto the flat gauge span. SVD of (I-GG')Z2 yields physical coefficient directions.
 Pperp=torch.eye(T.size[2],dtype=dt,device=dev)-G2@G2.T; W=Pperp@Z2; Uw,sw,Vw=torch.linalg.svd(W,full_matrices=False); rw=int((sw>1e-9*max(float(sw[0]),1e-300)).sum()); Wphys=Uw[:,:rw]
 # ensure each Wphys direction satisfies A2 (it should: projection can perturb if gauge not in ker A2; record residual)
 # For each prescribed H2 direction, find all higher corrections solving dE0..dE_{K-2}=0, minimum norm.
 lower=list(range(0,K,2)); A=torch.cat([JE[k] for k in lower],0); Ah=A[:,sl(4).start:] if K>=4 else torch.zeros(A.shape[0],0,dtype=dt,device=dev)
 responses=[]
 for q in range(rw):
  a=Wphys[:,q]; rhs=-(A[:,sl(2)]@a)
  if Ah.shape[1]:
   # CPU NumPy SVD is more stable here than CUDA gelsd and exposes inconsistency explicitly.
   h_np=np.linalg.lstsq(Ah.detach().cpu().numpy(),rhs.detach().cpu().numpy(),rcond=1e-12)[0]
   h=tt(h_np)
  else:h=torch.zeros(0,dtype=dt,device=dev)
  dx=torch.cat([a,h]);responses.append(dx)
 Resp=torch.stack(responses,1) if responses else torch.zeros(n,0,dtype=dt,device=dev)
 resA=float((A@Resp).norm()) if rw else 0.; im=JR@Resp if rw else torch.zeros(PK.shape[0],0,dtype=dt,device=dev);sv=torch.linalg.svdvals(im) if rw else torch.zeros(0,dtype=dt,device=dev)
 from math import factorial
 import step68_flat_cokernel as F
 mons=F.mons_deg(K-2);m=(K-2)//2;ell=np.array([factorial(m)*np.prod([factorial(a) for a in mm])/np.prod([factorial(a//2) for a in mm]) if all(a%2==0 for a in mm) else 0. for mm in mons]);ell=tt(ell/np.linalg.norm(ell))
 relcorr=resA/max(float((A[:,sl(2)]@Wphys).norm()) if rw else 1.,1e-300)
 out={'K':K,'name':name,'rank_constraints_H2':rA,'dim_ker_E0_N1_H2':int(Z2.shape[1]),'gauge_rank_degree2':rg,'physical_H2_rank_after_gauge':rw,'gauge_projection_residual':resid,'A2_on_gauge_norm':float((A2@G2).norm()),'A2_on_Wphys_norm':float((A2@Wphys).norm()) if rw else 0.,'lower_corrected_residual_norm':resA,'lower_corrected_relative_residual':relcorr,'rank_R_physical_H2':int((sv>1e-8*max(float(sv[0]) if len(sv) else 0.,1e-300)).sum()) if rw else 0,'sv_R_physical_H2':[float(a) for a in sv],'radial_norm_physical_H2':float((ell@im).norm()) if rw else 0.,'response_block_norms':{str(d):float(Resp[sl(d)].norm()) for d in degs} if rw else {},'time':time.time()-t0}
 (OUT/f'vary_H2_free_K{K}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 6)
