"""Shoot diagonal SU(2)-invariant Ric=-6 Einstein metrics from a smooth nut.

The exact nut series is parametrized by q=c2_3 and r=c3_3, with
c1_3=1-q-r.  We first test the biaxial Pedersen/Taub-NUT-AdS family q=c1_3
(i.e. q=(1-r)/2).  It must contain complex hyperbolic space and provide
ACH fillings with standard CR ratio rho=1, calibrating the Step-13 asymptotic readout.
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from einstein_bolt_shoot import rhs, constraint, ev_small, ev_big

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'data'/'einstein_nut_runs.json'


def init(q,r,t0=2e-3):
    c=[1-q-r,q,r]
    c5=[3*(8*q*q+28*q*r-13*q+8*r*r-13*r+4)/20,
        3*(8*q*q-12*q*r-3*q-12*r*r+12*r-1)/20,
        -3*(12*q*q+12*q*r-12*q-8*r*r+3*r+1)/20]
    a=np.array([t0+c[i]*t0**3+c5[i]*t0**5 for i in range(3)])
    ap=np.array([1+3*c[i]*t0**2+5*c5[i]*t0**4 for i in range(3)])
    return np.concatenate([np.log(a),ap/a])


def shoot(q,r,T=12.0):
    z0=init(q,r)
    s=solve_ivp(rhs,(2e-3,T),z0,method='DOP853',rtol=2e-13,atol=2e-14,
                events=[ev_small,ev_big],dense_output=True)
    tt=np.linspace(0.05,s.t[-1],3000); Z=s.sol(tt); L=Z[:3]; y=Z[3:]
    rows=[]
    for k in range(3):
        i,j=(k+1)%3,(k+2)%3
        dev=np.sqrt((y[k]-2)**2+(y[i]-1)**2+(y[j]-1)**2)
        im=int(np.argmin(dev))
        rows.append(dict(slot=k+1,min_dev=float(dev[im]),t_min=float(tt[im]),
                         kappa=float(np.exp(L[k]-L[i]-L[j])[im]),
                         rho=float(np.exp(L[i]-L[j])[im]),
                         y=[float(v) for v in y[:,im]]))
    return dict(q=q,r=r,c1=1-q-r,status=int(s.status),tend=float(s.t[-1]),
                constraint0=float(constraint(z0)),constraint_end=float(constraint(s.y[:,-1])),
                y_end=[float(v) for v in s.y[3:,-1]],slots=rows)


def main():
    # CH in slot 2: sinh t has c=1/6; sinh t cosh t=(sinh 2t)/2 has c=2/3.
    # Thus (c1,c2,c3)=(1/6,2/3,1/6): q=2/3,r=1/6.
    params=[(2/3,1/6)]
    # Biaxial slots 1=2: c1=c2=(1-r)/2, varying r around CH.
    for r in [-1.0,-0.3,0.0,0.1,1/6,0.25,0.5,0.8,1.2]:
        params.append(((1-r)/2,r))
    # cyclic copies test all readouts.
    params += [(1/6,2/3),(1/6,1/6)]
    out=[shoot(float(q),float(r)) for q,r in params]
    OUT.write_text(json.dumps(out,indent=1)+'\n')
    print(json.dumps(out,indent=1))

if __name__=='__main__': main()
