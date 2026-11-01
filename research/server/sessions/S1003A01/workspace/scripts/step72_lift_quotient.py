#!/usr/bin/env python3
"""Step 72c: quotient the Step-72 H2 response by all admissible fixed-H2 lower corrections.

Let A=[Ap Ah] be d(E0,...,E_{K-2}) and J=[Jp Jh]=P_K dE_K.  X is the five-dimensional
physical H2 subspace ker(dE0,dN1) modulo quartic-Hamiltonian gauge.  A minimum-norm lift H0 solves
Ah H0=-Ap X, but another lift is H0+Nh C with Nh=ker Ah.  Therefore only the class of
Y=Jp X+Jh H0 modulo B=Jh Nh is correction-independent.  This script records rank B, incremental
rank [B,Y]-rank B, residual projection of Y modulo im B, and radial ambiguity.  It also repeats the
quotient after requiring coordinate N3,...,N_{K-1} to remain fixed, with their H2 contributions included.
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

def svd_null(A,rtol=1e-10):
 u,s,vh=torch.linalg.svd(A,full_matrices=True);r=int((s>rtol*max(float(s[0]),1e-300)).sum());return vh[r:].T,s,r

def main(K=6,name='recon_F012_gen5_lam-5'):
 t0=time.time();lam=float(name.split('lam')[-1]);base=HERE.parents[2]/'S1003A02'/'workspace'/'data'/'step80';dd=np.load(base/f'{name}.npz')
 T=Tower(K,lam);T.degs=list(range(2,T.N+1));T.size={e:6*len(T.mon_d[e]) for e in T.degs};tt=lambda a:torch.tensor(np.asarray(a),dtype=dt,device=dev)
 v=np.load(HERE.parent/'data'/'step69'/f'order8_polished_v_{name}.npy');s4,s6=6*35,6*84;parts={2:dd['H2'],4:v[:s4],6:v[s4:s4+s6],8:v[s4+s6:]};degs=list(range(2,K+1,2));sizes=[T.size[d] for d in degs];off={d:o for d,o in zip(degs,np.cumsum([0]+sizes[:-1]).tolist())};x0=torch.cat([tt(parts[d]) for d in degs]);n=x0.numel();J0t=tt(J0);iu=[(i,j) for i in range(4) for j in range(i+1,4)]
 def jets(x):return {d:x[off[d]:off[d]+T.size[d]] for d in degs}
 def E(k):return lambda x:T.Evec(jets(x),[k])[0]
 def Nodd(q):
  idx=torch.tensor(T.mon_d[q],device=dev)
  def f(x):
   g=expH(T.R,T.H(jets(x)));Jm=torch.einsum('ab,bjp->ajp',J0t,g);N=nijenhuis(T.R,Jm)
   return torch.stack([N[a,i,j][idx] for a in range(4) for (i,j) in iu]).reshape(-1)
  return f
 eye=torch.eye(n,dtype=dt,device=dev)
 def jac(f):
  vs=torch.func.vmap(lambda e:torch.func.jvp(f,(x0,),(e,))[1]);return torch.cat([vs(eye[s:s+64]).T for s in range(0,n,64)],1)
 JE={k:jac(E(k)) for k in range(0,K+1,2)};JN={q:jac(Nodd(q)) for q in range(1,K,2)};JR=tt(P_matrix(K).astype(float)/2)@JE[K]
 sl2=slice(off[2],off[2]+T.size[2]);hsl=slice(off[4],n)
 A2=torch.cat([JE[0][:,sl2],JN[1][:,sl2]],0);Z2,_,_=svd_null(A2,1e-10);G2,_,_=gauge_basis(T,2);G2=tt(G2);W=(torch.eye(T.size[2],dtype=dt,device=dev)-G2@G2.T)@Z2;Uw,sw,Vw=torch.linalg.svd(W,full_matrices=False);rw=int((sw>1e-9*float(sw[0])).sum());X=Uw[:,:rw]
 lower=torch.cat([JE[k] for k in range(0,K,2)],0);Ap=lower[:,sl2];Ah=lower[:,hsl];Jp=JR[:,sl2];Jh=JR[:,hsl]
 from math import factorial
 import step68_flat_cokernel as F
 mons=F.mons_deg(K-2);m=(K-2)//2;ell=np.array([factorial(m)*np.prod([factorial(a) for a in mm])/np.prod([factorial(a//2) for a in mm]) if all(a%2==0 for a in mm) else 0. for mm in mons]);ell=tt(ell/np.linalg.norm(ell))
 def analyse(label,Ahe, rhs_extra=None, Jhe=None):
  # Ahe constraints on higher blocks; RHS is corresponding response to X. Default lower equations.
  rhs=-Ap@X if rhs_extra is None else rhs_extra
  H0=tt(np.linalg.lstsq(Ahe.detach().cpu().numpy(),rhs.detach().cpu().numpy(),rcond=1e-12)[0]); Nh,sh,rAh=svd_null(Ahe,1e-10); JJ=Jh if Jhe is None else Jhe
  Y=Jp@X+JJ@H0;B=JJ@Nh
  ub,sb,vhb=torch.linalg.svd(B,full_matrices=False);tol=1e-8*max(float(sb[0]) if len(sb) else 0.,1e-300);rb=int((sb>tol).sum());UB=ub[:,:rb] if rb else torch.zeros(B.shape[0],0,dtype=dt,device=dev);Yq=Y-UB@(UB.T@Y)
  sj=torch.linalg.svdvals(torch.cat([B,Y],1));rj=int((sj>tol).sum());sy=torch.linalg.svdvals(Yq)
  radialB=float((ell@B).norm()); radialY=float((ell@Y).norm()); radialQ=float((ell@Yq).norm())
  # explicit cancellation of all Y if possible
  C=tt(np.linalg.lstsq(B.detach().cpu().numpy(),(-Y).detach().cpu().numpy(),rcond=1e-12)[0]) if B.shape[1] else torch.zeros(0,X.shape[1],dtype=dt,device=dev)
  dHcan=Nh@C; Ycan=Y+B@C
  liftres=float((Ahe@H0-rhs).norm()); rhsnorm=float(rhs.norm())
  return {'rank_Ah':rAh,'dim_ker_Ah':int(Nh.shape[1]),'rhs_norm':rhsnorm,'lower_lift_residual':liftres,'lower_lift_relative_residual':liftres/max(rhsnorm,1e-300),'rank_B':rb,'rank_joint_BY':rj,'incremental_rank':rj-rb,'quotient_Y_norm':float(Yq.norm()),'quotient_Y_singular_values':[float(a) for a in sy],'radial_B_norm':radialB,'radial_Y_selected':radialY,'radial_quotient':radialQ,'cancelled_Y_norm':float(Ycan.norm()),'cancel_correction_norm':float(dHcan.norm()),'cancel_kernel_residual':float((Ahe@dHcan).norm()),'cancelled_lower_residual':float((Ahe@(H0+dHcan)-rhs).norm()),'selected_lift_norm':float(H0.norm()),'sv_B_tail':[float(a) for a in sb[max(rb-2,0):rb+2]]}
 out={'K':K,'name':name,'physical_H2_rank':rw,'W_singular_values':[float(a) for a in sw[:min(10,len(sw))]],'unrestricted':analyse('unrestricted',Ah)}
 # Add covariant-coordinate torsion constraints N3,...,N_{K-1}: higher correction must cancel H2 contribution.
 odds=list(range(3,K,2))
 if odds:
  TNp=torch.cat([JN[q][:,sl2] for q in odds],0);TNh=torch.cat([JN[q][:,hsl] for q in odds],0)
  Ae=torch.cat([Ah,TNh],0);rhs=torch.cat([-Ap@X,-TNp@X],0)
  out['coordinate_higher_torsion_fixed']=analyse('torsion',Ae,rhs_extra=rhs)
  out['coordinate_higher_torsion_fixed']['odd_degrees']=odds
 out['time']=time.time()-t0;(OUT/f'lift_quotient_K{K}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 6)
