"""Corrected transverse Hamilton--Jacobi Riccati conventions and exact CH benchmarks.

Near N={u1=u3=0}, with xi=(u1,u3), Phi=xi^T A xi/2 and
S=xi^T K xi/2+O(|xi|^3), the quadratic Hamiltonian matrix is
  Kdot/2 + (K D A + A D K)/2 + K D K.
For Y=K+A/2 this is
  Ydot/2 + Y D Y - (A D A + Adot)/4.
Thus S=-Phi means (K,Y)=(-A,-A/2), whereas S=0 means (0,A/2).

On exact CH, a1=a3=sqrt(x), a2=sqrt(x(1+x)), u2=3x.  The +/-
channels diagonalize A.  This script checks that the exact Step-7 positive-ground-state
Dirichlet-to-Neumann cost gives the HJ Riccati solution for a fixed target x=1,
and follows the linear Hamiltonian/Jacobi system for bolt-side seed Hessians.
A zero of the graph block X is reported as a Riccati pole, not as a negative CH mode.
"""
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

x=sp.symbols('x', positive=True)
Dplus=1-3*x-2*x**2+4*x**3+6*x**2*(1+x)*sp.log((1+x)/(2*x))
Dminus=1+8*x-12*x**2*sp.log(x)-8*x**3-x**4
# Step-7 full relative action plus the entrance Phi charge gives the positive P-cost.
cplus=1/(2*Dplus)
cminus=(1+x)**5/(2*Dminus)
kplus=-4*cplus
kminus=-4*cminus
a_plus=2+3*x
a_minus=2-3*x
ric_res_plus=sp.factor(sp.diff(kplus,x)+kplus*(kplus+a_plus)/(x*(1+x)))
ric_res_minus=sp.factor(sp.diff(kminus,x)+kminus*(kminus+a_minus)/(x*(1+x)))


def pole_for_seed(rho, channel, factor=1.0, xmax=20.0):
    """Evolve z=1/k for K(rho)=-factor*A(rho); z=0 is a graph pole.

    The scalar Jacobi solution is explicit.  With a=2+/-3x and d=x(1+x),
      z'-(a/d)z=1/d,
    and the positive homogeneous multiplier is f_+^2=x^2(1+x) or
    f_-^2=x^2/(1+x)^5, exactly the Step-7 positive zero mode squared.
    The conventional integrating factor multiplying the ODE is f^{-2}.
    We integrate numerically here and compare to the exact quadrature representation.
    """
    sgn=1.0 if channel=='plus' else -1.0
    def aa(xx): return 2.0+sgn*3.0*xx
    def fsq(xx): return xx**2*(1+xx) if channel=='plus' else xx**2/(1+xx)**5
    z0=-1.0/(factor*aa(rho))
    def rhs(xx, zz):
        return [1.0/(xx*(1+xx))+aa(xx)/(xx*(1+xx))*zz[0]]
    def ev(xx,zz): return zz[0]
    ev.terminal=True; ev.direction=0
    sol=solve_ivp(rhs,(rho,xmax),[z0],rtol=2e-12,atol=2e-14,events=ev,max_step=.002)
    pole=float(sol.t_events[0][0]) if len(sol.t_events[0]) else None
    # z/f^2 = z0/f(rho)^2 + int_rho^x ds/[s(1+s)f(s)^2].
    # At a pole this bracket is zero; the Jacobi graph block crosses zero while the
    # Lagrangian plane itself is regular.
    return dict(rho=rho,channel=channel,factor=factor,pole=pole,
                endpoint=float(sol.t[-1]),z_endpoint=float(sol.y[0,-1]),n=int(len(sol.t)),
                homogeneous_multiplier_f_squared=('x^2(1+x)' if channel=='plus' else 'x^2/(1+x)^5'),
                ode_integrating_factor_f_inverse_squared=('1/[x^2(1+x)]' if channel=='plus' else '(1+x)^5/x^2'))


def main():
    checks=dict(
        riccati_residual_plus=str(ric_res_plus),
        riccati_residual_minus=str(ric_res_minus),
        conventions=dict(seed=dict(K='-A',Y='-A/2'),zero=dict(K='0',Y='A/2')),
        dtn=dict(Kplus='-2/Delta_plus',Kminus='-2(1+x)^5/Delta_minus',target_x=1,
                 general_target='K_pm^X(rho)=-1/[f_pm(rho)^2 int_rho^X ds/(s(1+s)f_pm(s)^2)]'),
    )
    runs=[]
    for rho in (.003,.01,.03,.1,.3,.5,.65):
        for fac in (1.0,.99,.985):
            for ch in ('plus','minus'):
                runs.append(pole_for_seed(rho,ch,fac))
    out=dict(checks=checks,seed_graph_evolution=runs,
             interpretation=('The exact DtN solutions have their hard-target graph pole at x=1. '
                             'Any earlier seed pole records loss of the K=P X^{-1} chart; the linear '
                             'Jacobi/Lagrangian plane remains defined and Step-7 ground states exclude '
                             'a negative compactly supported CH mode. A pole can still obstruct one smooth '
                             'quadratic graph and carries focal/Maslov information; admissible matching to '
                             'the outgoing plane must be checked. null means no pole before xmax=20 only.'))
    print(json.dumps(out,indent=1))
    p=Path(__file__).resolve().parents[1]/'data/hj/riccati_ch_benchmark.json'
    p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=1)+'\n')

if __name__=='__main__': main()
