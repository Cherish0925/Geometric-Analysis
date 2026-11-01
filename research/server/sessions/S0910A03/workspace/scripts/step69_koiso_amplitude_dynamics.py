"""Exploratory amplitude sweep for the T2-invariant Koiso Einstein Cauchy germ."""
from __future__ import annotations
import json, sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
import step69_koiso_galerkin as kg


def summarize(run):
    rec=run['records']
    # Ignore t=0 when locating return of H_min to nonpositive values.
    cross=None
    for x in rec[1:]:
        if x['H_min'] <= 0:
            cross=x['t']; break
    admiss=[x for x in rec if x['ham_sup']<1e-2 and x['mom_cov_sup']<1e-2]
    return {
        'success':run['success'],'last_time':run['last_time'],
        'H_return_nonpositive_time':cross,
        'last_constraint_1e-2_time':admiss[-1]['t'] if admiss else None,
        'max_Hmin_before_return':max(x['H_min'] for x in rec),
        'record_final':rec[-1],
    }


def main():
    out=[]
    for A in [0.5,0.75,1.0,1.25,1.5,2.0,2.5,3.0,4.0]:
        kg.A=A
        print('A',A,flush=True)
        sol=kg.yamabe_solution()
        run=kg.run_mode(sol,16,t_end=0.8)
        row={'A':A,'modes':16,**summarize(run)}
        out.append(row); print(row,flush=True)
    result={'scope':'Galerkin pilot; resolution checks required for any selected amplitude','rows':out}
    path=Path(__file__).resolve().parents[1]/'data'/'step69_koiso_amplitude_dynamics.json'
    path.write_text(json.dumps(result,indent=2),encoding='utf-8')

if __name__=='__main__': main()
