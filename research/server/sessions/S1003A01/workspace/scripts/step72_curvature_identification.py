#!/usr/bin/env python3
"""Identify the five-dimensional degree-2 physical quotient with one Weyl chirality.

For a homogeneous quadratic anti-J metric variation h in Darboux/normal-at-the-point gauge,
compute the flat linearized Riemann tensor at 0 and its trace-free curvature-operator blocks on
Lambda^+ and Lambda^-.  Reconstruct X = ker(dE0,dN1) orthogonal to quartic-Hamiltonian gauge at the
gen5 lambda=-5 point, then record ranks/norms of W+ and W- on X and on gauge.
"""
from pathlib import Path
import sys,json,itertools,numpy as np,torch
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE));sys.path.insert(0,str(HERE.parents[2]/'S1003A02'/'workspace'/'scripts'))
from step78_real_tower import Tower
from step77_gn_germ import dev,dt,J0,anti_basis
from step71_fibre_test import expH,nijenhuis
from step71_fibre_split import gauge_basis
OUT=HERE.parent/'data'/'step72';OUT.mkdir(parents=True,exist_ok=True)

def curvature_maps(T):
 Bs=anti_basis(); mons=[T.R.mons[i] for i in T.mon_d[2]]; n=6*len(mons)
 dd=np.zeros((4,4,4,4,n)) # h_ij,pq
 for a,B in enumerate(Bs):
  for r,m in enumerate(mons):
   c=a*len(mons)+r
   for p in range(4):
    for q in range(4):
     mm=list(m)
     if mm[p]==0:continue
     fac=mm[p];mm[p]-=1
     if mm[q]==0:continue
     fac*=mm[q];mm[q]-=1
     if sum(mm)==0:dd[:,:,p,q,c]=B*fac
 R=np.zeros((4,4,4,4,n))
 for i,j,k,l in itertools.product(range(4),repeat=4):
  R[i,j,k,l]=.5*(dd[i,l,j,k]+dd[j,k,i,l]-dd[i,k,j,l]-dd[j,l,i,k])
 pairs=[(0,1),(0,2),(0,3),(2,3),(3,1),(1,2)] # oriented basis e01,e02,e03,e23,e31,e12
 C=np.zeros((6,6,n))
 for a,(i,j) in enumerate(pairs):
  for b,(k,l) in enumerate(pairs):C[a,b]=R[i,j,k,l]
 # With standard orientation, SD=(first+last corresponding)/sqrt2 and ASD=(first-last)/sqrt2.
 Sp=np.zeros((6,3));Sm=np.zeros((6,3))
 for a in range(3):Sp[a,a]=Sp[a+3,a]=1/np.sqrt(2);Sm[a,a]=1/np.sqrt(2);Sm[a+3,a]=-1/np.sqrt(2)
 TB=[]
 TB.append(np.diag([1,-1,0])/np.sqrt(2));TB.append(np.diag([1,1,-2])/np.sqrt(6))
 for a,b in [(0,1),(0,2),(1,2)]:
  M=np.zeros((3,3));M[a,b]=M[b,a]=1/np.sqrt(2);TB.append(M)
 def project(S):
  B=np.einsum('pa,pqn,qb->abn',S,C,S)
  return np.array([np.einsum('ab,abn->n',Q,B) for Q in TB])
 return project(Sp),project(Sm),float(np.max(abs(C-C.transpose(1,0,2))))

def main(name='recon_F012_gen5_lam-5'):
 lam=-5.;T=Tower(6,lam);T.degs=list(range(2,T.N+1));T.size={e:6*len(T.mon_d[e]) for e in T.degs};tt=lambda a:torch.tensor(np.asarray(a),dtype=dt,device=dev)
 base=HERE.parents[2]/'S1003A02'/'workspace'/'data'/'step80';ddat=np.load(base/f'{name}.npz');H2=tt(ddat['H2']);z=torch.zeros(T.size[4]+T.size[6],dtype=dt,device=dev);J0t=tt(J0);iu=[(i,j) for i in range(4) for j in range(i+1,4)];idx1=torch.tensor(T.mon_d[1],device=dev)
 def jets(h):return {2:h,4:z[:T.size[4]],6:z[T.size[4]:]}
 def fE(h):return T.Evec(jets(h),[0])[0]
 def fN(h):
  g=expH(T.R,T.H(jets(h)));Jm=torch.einsum('ab,bjp->ajp',J0t,g);N=nijenhuis(T.R,Jm);return torch.stack([N[a,i,j][idx1] for a in range(4) for (i,j) in iu]).reshape(-1)
 I=torch.eye(T.size[2],dtype=dt,device=dev)
 def jac(f):
  vs=torch.func.vmap(lambda e:torch.func.jvp(f,(H2,),(e,))[1]);return torch.cat([vs(I[s:s+64]).T for s in range(0,T.size[2],64)],1)
 A=torch.cat([jac(fE),jac(fN)],0);u,s,vh=torch.linalg.svd(A,full_matrices=True);r=int((s>1e-10*float(s[0])).sum());Z=vh[r:].T
 G,resid,rg=gauge_basis(T,2);G=tt(G);W=(torch.eye(T.size[2],dtype=dt,device=dev)-G@G.T)@Z;uw,sw,vw=torch.linalg.svd(W,full_matrices=False);rw=int((sw>1e-9*float(sw[0])).sum());X=uw[:,:rw]
 Kp,Km,sym=curvature_maps(T);Kp=tt(Kp);Km=tt(Km)
 def rec(K,V):
  M=K@V;sv=torch.linalg.svdvals(M)
  # Use an absolute threshold: a self-relative threshold would falsely label roundoff-sized zero matrices full rank.
  return {'norm':float(M.norm()),'rank_abs_1e-10':int((sv>1e-10).sum()),'singular_values':[float(a) for a in sv]}
 out={'physical_dim':rw,'gauge_dim':rg,'R_operator_symmetry_error':sym,'Wplus_on_physical':rec(Kp,X),'Wminus_on_physical':rec(Km,X),'Wplus_on_gauge':rec(Kp,G),'Wminus_on_gauge':rec(Km,G),'Ricci_N1_kernel_residual':float((A@X).norm()),'gauge_kernel_residual':float((A@G).norm()),'projected_kernel_singular_values':[float(a) for a in sw[:10]],'gauge_projection_residual':resid}
 (OUT/'curvature_identification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
