#!/usr/bin/env python3
"""Independent evaluation of A02 Step-80 reconstructed Darboux jets.

Loads only coefficient arrays and monomial indices, rebuilds the truncated
Einstein operator with the public Tower code, checks conventions, lower/order-6
residuals, torsion cone and index, closure/compatibility (automatic in Darboux
gauge), and the saved scalar reduced equation.  No optimizer is rerun.
"""
import json, os, sys
from pathlib import Path
import numpy as np
import torch
HERE=Path(__file__).resolve().parent
A02=HERE.parents[2]/'S1003A02'/'workspace'
sys.path.insert(0,str(A02/'scripts'))
import step79_general_order6 as G
from step77_gn_germ import jet_coords, anti_basis, J0
OUT=HERE.parent/'data'/'step67'; OUT.mkdir(parents=True,exist_ok=True)

def check(name):
    src=A02/'data'/'step80'/f'{name}.npz'
    meta=json.loads((A02/'data'/'step80'/f'{name}.json').read_text())
    lam=float(meta['lam']); d=np.load(src)
    T=G.TowerAll(6,lam)
    # monomial convention and anti-J basis
    mons=np.asarray(T.R.mons,dtype=int)
    mon_ok=np.array_equal(mons,d['mons']) and all(np.array_equal(np.asarray(T.mon_d[k]),d[f'mon_d{k}']) for k in T.degs)
    Bs=np.asarray(anti_basis()); anti_err=float(np.linalg.norm(np.einsum('aij,jk->aik',Bs,J0)+np.einsum('ij,ajk->aik',J0,Bs)))
    jets={k:torch.tensor(d[f'H{k}'],dtype=G.dt,device=G.dev) for k in T.degs}
    per={k:float(T.Evec(jets,[k])[0].norm()) for k in range(7)}
    allres=float(T.Evec(jets,list(range(7)))[0].norm())
    jc=jet_coords(T.torsion(jets))
    # Metric is exp(H), Omega is constant standard in this Darboux representation.
    # Verify saved scalar solution phi(z)=0 or Phi at minimizer.
    Hpi=d['Hpi']; jv=d['jv']; cp=float(d['cpi']); z=d['z']
    phi=float(cp+jv@z+0.5*z@Hpi@z)
    he=np.linalg.eigvalsh(Hpi)
    zstar=-np.linalg.solve(Hpi,jv)
    Phi=float(cp+jv@zstar+0.5*zstar@Hpi@zstar)
    # Direct reduced residual from saved basis pieces cannot recover all 35 rows
    # without c,J,H; check pi-projection and supplied ell normalization.
    out={'name':name,'lam':lam,'monomial_index_match':bool(mon_ok),'antiJ_basis_error':anti_err,
         'per_order_res_norm':per,'combined_E0_E6_norm':allres,'jet_coords':jc,
         'index_positive':bool(jc['detD']>0),'cone_abs_residual':abs(jc['quadric_A2-S2-8c2']),
         'ell_norm':float(np.linalg.norm(d['ell'])),'pi_norm':float(np.linalg.norm(d['pi'])),
         'Hpi_eig_min':float(he[0]),'Hpi_eig_max':float(he[-1]),'Phi6_recomputed':Phi,
         'phi_at_saved_z':phi,'H_norms':{str(k):float(np.linalg.norm(d[f'H{k}'])) for k in T.degs}}
    return out

def main():
    names=sys.argv[1:] or ['recon_F012_gen2_lam0','recon_F012_gen2_lam-5','recon_F012_gen5_lam-5','recon_lsA_jet0_lam-1']
    oo=[check(n) for n in names]
    (OUT/'verify_A02_step80_reconstructions.json').write_text(json.dumps(oo,indent=1)+'\n')
    print(json.dumps(oo,indent=1))
if __name__=='__main__': main()
