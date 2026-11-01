"""Sweep the explicit analytic Yamabe T^3 centers over seed amplitude A.
Reports the negative part of P=Ric_q^#+3I=S'(0), which equals the
maximum positive sectional curvature of q in dimension three when R_q=-6.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp

TWOPI=2*np.pi


def solve_A(A, prev=None):
    def fp(x): return A*np.cos(x)
    def fpp(x): return -A*np.sin(x)
    def ode(x,y):
        u,up=y
        return np.vstack((up,0.75*u**5-0.25*fp(x)**2*u))
    def bc(ya,yb): return np.array([ya[0]-yb[0],ya[1]-yb[1]])
    x=np.linspace(0,TWOPI,1001)
    u0=(A*A/6.0)**0.25
    guess=np.vstack((u0*(1+0.02*np.cos(2*x)),-0.04*u0*np.sin(2*x)))
    sol=solve_bvp(ode,bc,x,guess,tol=2e-10,max_nodes=50000)
    if not sol.success: return {'A':A,'success':False,'message':sol.message}
    x=np.linspace(0,TWOPI,8001); u,up=sol.sol(x); upp=ode(x,np.vstack((u,up)))[1]
    phip=2*up/u; phipp=2*(upp/u-(up/u)**2)
    ric=np.vstack((
        -2*fp(x)**2-2*phipp,
        -fpp(x)-fp(x)*phip-phipp-phip**2,
        fpp(x)+fp(x)*phip-phipp-phip**2,
    ))/u**4
    P=ric+3
    scalar=ric.sum(axis=0)
    # In R=-6 dimension 3, sectional curvatures are - complementary P eigenvalues.
    return {
        'A':A,'success':True,'nodes':int(sol.x.size),
        'u_min':float(u.min()),'u_max':float(u.max()),
        'volume':float(np.trapezoid(u**6,x)),
        'P_min_global':float(P.min()),'P_max_global':float(P.max()),
        'P_component_min':[float(z.min()) for z in P],
        'P_component_max':[float(z.max()) for z in P],
        'max_positive_sectional':float(-P.min()),
        'scalar_error':float(np.abs(scalar+6).max()),
        'trace_P_error':float(np.abs(P.sum(axis=0)-3).max()),
    }


def main():
    As=[0.03,0.05,0.08,0.12,0.2,0.35,0.5,0.75,1.0,1.5,2.0,3.0]
    rows=[]
    for A in As:
        row=solve_A(A); rows.append(row); print(row,flush=True)
    out={'statement':'P=Ric+3I=Sprime(0); for scalar -6, K_ij=-P_k', 'rows':rows}
    path=Path(__file__).resolve().parents[1]/'data'/'step69_center_amplitude_sweep.json'
    path.write_text(json.dumps(out,indent=2),encoding='utf-8')

if __name__=='__main__': main()
