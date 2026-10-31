"""Exact reduced resistance for the asymptotic ACH Rossi neutral mode.

The peer Einstein shooting gives q=log(a2/a3) with asymptotic forced equation
    q''+4q'=f.
In a noncollapsed ACH end the trace-free-Ricci action has the model weight e^{4t} f^2.
This script solves the finite-horizon minimum
    min int_0^T e^{4t}(q''+4q')^2 dt,
    q(0)=0, q(T)=Delta, q'(0)=q'(T)=0.
It contrasts the ACH weight with an unweighted long transition.  The model is an exact
one-dimensional calculation, but applying its constant to the full metric requires comparison
between f and the actual Ricci defect and control of the asymptotic volume coefficient.
"""
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp, simpson


def ach_closed(T,Delta):
    e=math.exp(-4*T); den=1-e
    # y=e^{4t}(v'+4v)=C e^{4t}+mu/4; v(0)=v(T)=0.
    # C=-mu*T*e^{-4T}/(1-e^{-4T}); integral v = Delta determines mu.
    Cper=-T*e/den
    # v/mu = Cper/4*(1-e^-4t)+t e^-4t/4
    int1=T-(1-e)/4
    int2=(1-e*(1+4*T))/16
    D=Cper*int1/4+int2/4
    mu=Delta/D; C=Cper*mu
    # f=C+mu/4 e^-4t; exact energy integral
    E=C*C*(math.exp(4*T)-1)/4 + 2*C*(mu/4)*T + (mu/4)**2*(1-e)/4
    return dict(T=T,Delta=Delta,mu=mu,C=C,energy=E,resistance=Delta*Delta/E,
                limiting_energy=64*Delta*Delta,energy_over_limit=E/(64*Delta*Delta))


def unweighted_numeric(T,Delta,n=1200):
    # First-order BVP for Euler-Lagrange with L=(v'+4v)^2 and integral state q.
    # solve directly as a linear-quadratic optimal control BVP: q'=v, v'=f-4v,
    # costates p_q'=0, p_v'=-p_q+4p_v, f=-p_v/2.
    x=np.linspace(0,T,n)
    y=np.zeros((4,n)); y[0]=Delta*x/T
    def fun(t,Y):
        q,v,pq,pv=Y
        f=-pv/2
        return np.vstack((v,f-4*v,np.zeros_like(t),-pq+4*pv))
    def bc(ya,yb): return np.array([ya[0],ya[1],yb[0]-Delta,yb[1]])
    sol=solve_bvp(fun,bc,x,y,tol=1e-9,max_nodes=10000)
    Y=sol.sol(x); f=-Y[3]/2
    E=simpson(f*f,x=x)
    return dict(T=T,energy=float(E),resistance=float(Delta*Delta/E),success=bool(sol.success))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--T',default='.5,1,2,4,8,16')
    ap.add_argument('--Delta',type=float,default=math.log(2.196)); ap.add_argument('--out')
    a=ap.parse_args(); Ts=[float(s) for s in a.T.split(',')]
    out=dict(delta=a.Delta,ACH_weighted=[ach_closed(T,a.Delta) for T in Ts],
             unweighted=[unweighted_numeric(T,a.Delta) for T in Ts])
    text=json.dumps(out,indent=1); print(text)
    if a.out: Path(a.out).write_text(text+'\n')
if __name__=='__main__': main()
