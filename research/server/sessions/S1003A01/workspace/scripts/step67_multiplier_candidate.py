#!/usr/bin/env python3
"""Compare A02's universal E6 cokernel row ell with an explicit U(2)-scalar symbol.

Candidate: for a symmetric degree-6 tensor polynomial E_ij(x), set
  P2(E) = J^i_a J^j_b d_a d_b E_ij - (1/2) Delta tr(E),
a homogeneous quartic scalar, then ell_cand(E)=Delta^2 P2(E)(0).
The saved ell acts on the 10 symmetric components, each with all degree-6
monomials.  Compare normalized vectors directly (both annihilate the flat H8
operator; Bianchi rows already disappear on the actual E6 coefficient space).
"""
import json, sys
from pathlib import Path
import numpy as np
import sympy as sp
HERE=Path(__file__).resolve().parent
A02=HERE.parents[2]/'S1003A02'/'workspace'
OUT=HERE.parent/'data'/'step67'; OUT.mkdir(parents=True,exist_ok=True)
TRI=[(i,j) for i in range(4) for j in range(i,4)]
J=np.array([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]],dtype=int)

def dcoef(m, inds):
    a=list(m); c=1
    for k in inds:
        c*=a[k]; a[k]-=1
        if a[k]<0:return 0,None
    return c,tuple(a)

def candidate(mons, mon6, alpha=1.0, beta=-0.5):
    pos6={int(global_i):q for q,global_i in enumerate(mon6)}
    n=len(mon6); v=np.zeros(10*n)
    # Apply all ordered indices a,b,c,c,d,d at x=0; nonzero only if derivative multiset equals m.
    # First term J^i_a J^j_b d_a d_b Delta^2 E_ij.
    for q,gi in enumerate(mon6):
        m=tuple(int(x) for x in mons[int(gi)])
        fac=np.prod([sp.factorial(x) for x in m])
        for t,(i,j) in enumerate(TRI):
            coeff=0
            # sum a,b,c,d with derivative count m
            for a in range(4):
              for b in range(4):
               jij=J[i,a]*J[j,b]
               if jij==0: continue
               for c in range(4):
                for d in range(4):
                 cnt=[0]*4
                 for k in (a,b,c,c,d,d):cnt[k]+=1
                 if tuple(cnt)==m: coeff+=jij
            # offdiagonal stored once but contraction sums E_ij and E_ji
            mult=1 if i==j else 2
            v[t*n+q]+=alpha*float(fac*coeff*mult)
            # -1/2 Delta^3 tr E: only diagonal components
            if i==j:
             coeff2=0
             for a in range(4):
              for c in range(4):
               for d in range(4):
                cnt=[0]*4
                for k in (a,a,c,c,d,d):cnt[k]+=1
                if tuple(cnt)==m: coeff2+=1
             v[t*n+q]+=beta*float(fac*coeff2)
    return v

def main():
    d=np.load(A02/'data'/'step80'/'recon_F012_gen5_lam-5.npz')
    ell=d['ell']; mons=d['mons']; mon6=d['mon_d6']
    c1=candidate(mons,mon6,1.0,0.0); c2=candidate(mons,mon6,0.0,1.0)
    B=np.stack([c1,c2],axis=1); coef=np.linalg.lstsq(B,ell,rcond=None)[0]; cand=B@coef
    en=ell/np.linalg.norm(ell); cn=cand/np.linalg.norm(cand)
    cos=float(en@cn); err=min(np.linalg.norm(en-cn),np.linalg.norm(en+cn))
    out={'ell_dim':len(ell),'candidate_dim':len(cand),'candidate_nonzero':int(np.count_nonzero(cand)),
         'fit_coefficients_[JJdd,DeltaTrace]':coef.tolist(),'coefficient_ratio_beta_over_alpha':float(coef[1]/coef[0]),
         'cosine':cos,'abs_cosine':abs(cos),'sign_adjusted_norm_error':float(err)}
    (OUT/'multiplier_candidate.json').write_text(json.dumps(out,indent=1)+'\n')
    np.savez(OUT/'multiplier_candidate.npz',ell=ell,candidate=cand,c1=c1,c2=c2)
    print(json.dumps(out,indent=1))
if __name__=='__main__':main()
