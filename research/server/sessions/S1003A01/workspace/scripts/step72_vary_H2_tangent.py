#!/usr/bin/env python3
"""Step 72: vary the admissible torsion-free H2/W^- directions on the full lower AKE solution variety.

This repairs a limitation of Step 71, where H2 was frozen.  At the polished even gen5, lambda=-5 jet,
let x=(H2,H4,H6,H8) and
    C_K=(E0,E2,...,E_{K-2}),       R_K=P_K(E_K).
Compute Tan=ker dC_K.  The first-torsion map is the degree-one Nijenhuis coefficient N1; its H2-kernel
contains Hamiltonian coordinate gauge and the five physical W^-(0) directions.  We compare dR_K on:
  top              : H2,...,H_{K-2} frozen;
  H2_torsionfixed  : only H2 and H_K vary, with dN1=0;
  H2_physical      : as above, modulo the homogeneous Hamiltonian-gauge H2 span;
  N1_fixed         : arbitrary lower motion with dN1=0.
We also record the U(2)-radial component.  This is a first-order calculation in fixed Darboux coordinates;
it does not identify coordinate N_j with covariant torsion jets modulo a genuine nonlinear pullback.

Output: workspace/data/step72/vary_H2_tangent_K{K}.json
"""
from pathlib import Path
import json, sys, time, itertools
import numpy as np
import torch
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[2] / 'S1003A02' / 'workspace' / 'scripts'))
from step78_real_tower import Tower
from step77_gn_germ import dev, dt, J0, OM, anti_basis
from step68_scalar_compatibility import P_matrix
from step71_fibre_test import expH, nijenhuis
from step71_fibre_split import gauge_basis
OUT = HERE.parent / 'data' / 'step72'; OUT.mkdir(parents=True, exist_ok=True)


def main(K=6, name='recon_F012_gen5_lam-5'):
    t0=time.time(); lam=float(name.split('lam')[-1])
    base=HERE.parents[2]/'S1003A02'/'workspace'/'data'/'step80'; dd=np.load(base/f'{name}.npz')
    T=Tower(K,lam); T.degs=list(range(2,T.N+1)); T.size={e:6*len(T.mon_d[e]) for e in T.degs}
    tt=lambda a: torch.tensor(np.asarray(a),dtype=dt,device=dev)
    pv=HERE.parent/'data'/'step69'/f'order8_polished_v_{name}.npy'; v8=np.load(pv)
    s4,s6,s8=6*35,6*84,6*165
    parts={2:dd['H2'],4:v8[:s4],6:v8[s4:s4+s6],8:v8[s4+s6:s4+s6+s8]}
    degs=list(range(2,K+1,2)); sizes=[T.size[d] for d in degs]
    off={d:o for d,o in zip(degs,np.cumsum([0]+sizes[:-1]).tolist())}
    x0=torch.cat([tt(parts[d]) for d in degs]); n=x0.numel()
    orders=list(range(0,K-1,2)); PK=tt(P_matrix(K).astype(float)/2.0); J0t=tt(J0)
    iu=[(i,j) for i in range(4) for j in range(i+1,4)]
    idx1=torch.tensor(T.mon_d[1],device=dev)
    def jets(x): return {d:x[off[d]:off[d]+T.size[d]] for d in degs}
    def funC(x): return T.Evec(jets(x),orders)[0]
    def funR(x): return PK@T.Evec(jets(x),[K])[0]
    def funN1(x):
        g=expH(T.R,T.H(jets(x))); Jm=torch.einsum('ab,bjp->ajp',J0t,g); N=nijenhuis(T.R,Jm)
        return torch.stack([N[k,i,j][idx1] for k in range(4) for (i,j) in iu]).reshape(-1)
    eye=torch.eye(n,dtype=dt,device=dev)
    def jac(f):
        vs=torch.func.vmap(lambda e:torch.func.jvp(f,(x0,),(e,))[1])
        return torch.cat([vs(eye[s:s+64]).T for s in range(0,n,64)],dim=1)
    JC,JR,JN1=jac(funC),jac(funR),jac(funN1)
    sC=torch.linalg.svdvals(JC); tolC=1e-9*float(sC[0]); U,s,Vh=torch.linalg.svd(JC,full_matrices=True); rC=int((s>tolC).sum()); Tan=Vh[rC:].T
    sRT=torch.linalg.svdvals(JR@Tan); ref=float(sRT[0]); tolR=1e-8*ref
    # radial row on scalar polynomials of degree K-2
    from math import factorial
    import step68_flat_cokernel as F
    mons=F.mons_deg(K-2); m=(K-2)//2
    ell=np.array([factorial(m)*np.prod([factorial(a) for a in mm])/np.prod([factorial(a//2) for a in mm]) if all(a%2==0 for a in mm) else 0. for mm in mons])
    ell=tt(ell/np.linalg.norm(ell))
    def selector(d):
        M=torch.zeros(T.size[d],n,dtype=dt,device=dev); M[:,off[d]:off[d]+T.size[d]]=torch.eye(T.size[d],dtype=dt,device=dev); return M
    def null_in_tan(constraints):
        A=torch.cat([q@Tan for q in constraints],0) if constraints else torch.zeros(0,Tan.shape[1],dtype=dt,device=dev)
        if not A.shape[0]: return Tan
        ua,sa,vha=torch.linalg.svd(A,full_matrices=True); ra=int((sa>1e-9*max(float(sa[0]),1e-300)).sum()); return Tan@vha[ra:].T
    out={'K':K,'name':name,'n_unknowns':n,'orders_C':orders,'rank_C':rC,'dim_Tan':int(Tan.shape[1]),'rank_R_Tan':int((sRT>tolR).sum()),'radial_Tan':float((ell@(JR@Tan)).norm()),'spaces':{}}
    def record(label,sub):
        if sub.shape[1]==0: out['spaces'][label]={'dim':0,'rank_R':0}; return
        M=JR@sub; sv=torch.linalg.svdvals(M); out['spaces'][label]={'dim':int(sub.shape[1]),'rank_R':int((sv>tolR).sum()),'radial_norm':float((ell@M).norm()),'sv_head':[float(a) for a in sv[:3]],'sv_tail':[float(a) for a in sv[-3:]],'block_norms':{str(d):float(sub[off[d]:off[d]+T.size[d]].norm()) for d in degs}}
        print(label,out['spaces'][label],flush=True)
    # top: freeze every block below H_K
    record('top',null_in_tan([selector(d) for d in degs if d<K]))
    # only H2,H_K move; fix intermediate H4..H_{K-2}; retain first torsion
    cs=[selector(d) for d in degs if 2<d<K]+[JN1]
    SH2=null_in_tan(cs); record('H2_torsionfixed',SH2)
    # remove the flat homogeneous Hamiltonian-gauge component of H2; this leaves physical W^- directions plus top freedom
    G2,resid,rg=gauge_basis(T,2); G2=tt(G2)
    proj2=(torch.eye(T.size[2],dtype=dt,device=dev)-G2@G2.T)@selector(2)
    SH2phys=null_in_tan(cs+[proj2]); record('H2_gauge_only_plus_top',SH2phys)
    # To isolate physical rather than gauge H2, constrain H2 to be orthogonal to gauge and leave its complement free:
    gauge_coords=G2.T@selector(2)
    SH2nogauge=null_in_tan(cs+[gauge_coords]); record('H2_no_gauge_plus_top',SH2nogauge)
    # all lower data may move but N1 fixed
    record('N1_fixed_all_lower',null_in_tan([JN1]))
    out['H2']={'rank_N1_H2':int((torch.linalg.svdvals(JN1[:,off[2]:off[2]+T.size[2]])>1e-9*float(torch.linalg.svdvals(JN1[:,off[2]:off[2]+T.size[2]])[0])).sum()),'gauge_rank':rg,'gauge_projection_residual':resid,'N1_on_gauge_norm':float((JN1[:,off[2]:off[2]+T.size[2]]@G2).norm())}
    out['time']=time.time()-t0
    (OUT/f'vary_H2_tangent_K{K}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'H2':out['H2'],'time':out['time']},indent=2),flush=True)

if __name__=='__main__': main(int(sys.argv[1]) if len(sys.argv)>1 else 6)
