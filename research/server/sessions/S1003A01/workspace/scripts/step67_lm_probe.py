#!/usr/bin/env python3
"""Probe real zeros of A02's complete 35-row reduced order-6 polynomial.
Saves only Session-A01 artifacts.  Negative Phi6 predicts existence but the
high-dimensional nonconvex reconstruction still requires an actual zero.
"""
import os, sys, json, time
from pathlib import Path
import numpy as np
import torch
HERE=Path(__file__).resolve().parent
A02=HERE.parents[2]/'S1003A02'/'workspace'/'scripts'
sys.path.insert(0,str(A02)); os.environ.setdefault('STEP79_OUT','step80')
import step79_general_order6 as G
from step80_F012_scan import random_cone_jet
OUT=HERE.parent/'data'/'step67'; OUT.mkdir(parents=True,exist_ok=True)

def run(tag,lam,nstarts=120):
    rng=np.random.default_rng(42); jets={}
    for i in range(8): jets[f'gen{i}']=random_cone_jet(rng,'generic')
    T=G.TowerAll(6,lam); c,S,A=jets[tag]
    jt=(complex(c),[[complex(S[i,j]) for j in range(2)] for i in range(2)],[[complex(A[i,j]) for j in range(2)] for i in range(2)])
    H2=G.make_H2(T,'jet',lam,np.random.default_rng(0),jt,1.0,0.0)
    H3=torch.zeros(T.size[3],dtype=G.dt,device=G.dev)
    rec,cr,Jr,Hr=G.reduce_general(T,H2,H3)
    an=G.analyse(cr,Jr,Hr,np.random.default_rng(1),nlm=nstarts)
    out={'tag':tag,'lam':lam,'rows':rec['n_rows_nontrivial'],'lin_resid':rec['lin_resid'],
         **{k:an.get(k) for k in ('joint_quad_rank','rank_J_on_common_kernel','n_scalar','definite','H_eig','c','Phi6','lm_min','|c|')},'time':rec['time']}
    print(json.dumps(out,indent=1,default=float),flush=True)
    (OUT/f'lm_probe_{tag}_lam{lam}.json').write_text(json.dumps(out,indent=1,default=float)+'\n')
if __name__=='__main__': run(sys.argv[1],float(sys.argv[2]),int(sys.argv[3]) if len(sys.argv)>3 else 120)
