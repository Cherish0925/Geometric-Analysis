"""Inspect actual ACH fate of optimized saturation endpoints.

For each optimal-control JSON, convert its scale-free terminal state to compact
ACH variables.  First report finite-section algebraic residuals.  Then integrate
the *uncontrolled Einstein compact flow* to test whether the endpoint really
lies in the standard-CR stable set.  This distinguishes necessary local
conditions (constraint, linear unstable coordinate, Phi~=0) from the nonlinear
stable manifold.
"""
from __future__ import annotations
import json, math, sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

HERE=Path(__file__).resolve().parent
OUT=HERE.parent/'data'/'saturation_control'/'endpoint_checks.json'
sys.path.insert(0,str(HERE))
from ach_projected import compact_rhs, U_and_phi  # noqa: E402


def to_compact(X,zeta=.01):
    x,z,p,chi,eta=X
    beta=x-1.5*math.log(z)
    q=-3*math.log(z)
    xi=chi+eta/2
    fac=math.sqrt(zeta)*math.exp(-beta/3)
    return np.array([fac*(p+2*xi/3),fac*(p-xi/3+eta/2),fac*(p-xi/3-eta/2),
                     math.sqrt(zeta)*math.exp(beta),q,zeta])


def constraint(W):
    yf,yg,yh,k,q,z=W
    Pf=2*k*k-8*z*z*math.sinh(q)**2/(k*k)
    Pg=-2*k*k+4*z*math.exp(-q)+4*z*z*math.sinh(2*q)/(k*k)
    Ph=-2*k*k+4*z*math.exp(q)-4*z*z*math.sinh(2*q)/(k*k)
    return yf*yg+yg*yh+yh*yf-6-(Pf+Pg+Ph)/2


def run(path):
    rec=json.loads(Path(path).read_text())
    W=to_compact(rec['terminal_state'])
    U,phi,dev=U_and_phi(W)
    def big(t,w): return 60-max(abs(v) for v in w[:4])
    big.terminal=True
    sol=solve_ivp(lambda t,w:compact_rhs(w),(0,20),W,method='DOP853',rtol=2e-12,atol=1e-14,events=big)
    wf=sol.y[:,-1]
    Uf,phif,devf=U_and_phi(wf)
    fate='SING' if sol.status==1 else ('ACH' if wf[5]<1e-10 and devf<1e-5 else 'OTHER')
    return {'path':str(path),'mode':rec.get('mode','ch'),'cost':rec['cost'],'W0':W.tolist(),
            'constraint0':constraint(W),'Ulin0':U,'phi_tilde0':phi,'dev0':dev,
            'fate':fate,'T_einstein':float(sol.t[-1]),'W_final':wf.tolist(),
            'Ulin_final':Uf,'phi_tilde_final':phif,'dev_final':devf}

if __name__=='__main__':
    rows=[run(p) for p in sys.argv[1:]]
    OUT.write_text(json.dumps(rows,indent=1)); print(json.dumps(rows,indent=1))
