"""Euler Chern--Gauss--Bonnet flux for diagonal Bianchi-IX O(-1) metrics.

For g=dt^2+sum a_i^2 sigma_i^2, d sigma_i=2 sigma_j^sigma_k, define
  b_E = W [ y1 K23^(3)+y2 K31^(3)+y3 K12^(3)-y1 y2 y3 ], W=a1 a2 a3.
The boundary Gauss--Bonnet term is 4*pi^2 b_E in the session convention.
This script:
  * verifies symbolically b_E=2 for Euclidean space and
    b_E=2-6 sinh(t)^4 for normalized complex hyperbolic space;
  * evaluates b_E along the floating b=.8 Einstein separatrix;
  * encloses b_E on every CAPD endpoint box in wazewski_T2.75.json using Arb.
It writes workspace/data/ach_capd/euler_flux_b0.8.json.
"""
from pathlib import Path
import json, math, sys
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from flint import arb

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from ach_projected import init_md, rhs_md, md_to_Ly, to_compact  # noqa: E402


def k3(a, i, j, k):
    """Intrinsic sectional curvature K_jk, with i the complementary index."""
    return ((a[j]**2-a[k]**2)**2 + 2*a[i]**2*(a[j]**2+a[k]**2)-3*a[i]**4) / \
           (a[i]**2*a[j]**2*a[k]**2)


def euler_flux(a, y):
    W = a[0]*a[1]*a[2]
    return W*(y[0]*k3(a, 0, 1, 2) + y[1]*k3(a, 1, 2, 0) +
              y[2]*k3(a, 2, 0, 1) - y[0]*y[1]*y[2])


def symbolic_checks():
    t = sp.symbols('t', positive=True)
    eu = sp.simplify(euler_flux([t,t,t], [1/t,1/t,1/t]))
    A = sp.sinh(t); B = sp.sinh(t)*sp.cosh(t)
    ch = sp.simplify(sp.trigsimp(euler_flux([B,A,A],
        [sp.diff(B,t)/B, sp.diff(A,t)/A, sp.diff(A,t)/A])))
    target = 2-6*sp.sinh(t)**4
    assert sp.simplify(sp.trigsimp(ch-target)) == 0, (ch, target)
    return {'euclidean': str(eu), 'CH': str(ch), 'CH_target': str(target)}


def float_profile():
    b = 0.8; d = 0.286999618893
    t0 = 0.002
    sol = solve_ivp(rhs_md, (t0, 3.2), init_md(b,d,t0), method='DOP853',
                    rtol=2e-13, atol=1e-30, dense_output=True)
    rows=[]
    for t in [0.02,0.05,0.1,0.2,0.35,0.5,0.75,1.0,1.5,2.0,2.5,2.75,3.0]:
        z = md_to_Ly(sol.sol(t)); L=z[:3]; y=z[3:]; a=np.exp(L)
        Wc=to_compact(z,0)
        phi=Wc[4]+(Wc[1]-Wc[2])/4-Wc[5]*math.sinh(Wc[4])
        rows.append(dict(t=t, bE=float(euler_flux(a,y)), phi=float(phi), rho=float(math.exp(phi)),
                         zeta=float(Wc[5]), kappa=float(Wc[3]), W=float(np.prod(a)),
                         y=[float(v) for v in y]))
    return rows


def box(lo, hi):
    # Inputs are already outward binary64 endpoints.  Enclose them with a tiny
    # additional radius before Arb operations.
    m=0.5*(lo+hi); r=0.5*(hi-lo)*(1+1e-12)+1e-300
    return arb(m,r)


def arb_bounds(x):
    return float(x.lower()), float(x.upper())


def reconstruct_from_compact(c):
    k=box(*c['kappa']); q=box(*c['q']); z=box(*c['zeta'])
    ub=box(*c['ub']); s1b=box(*c['s1b']); s2b=box(*c['s2b']); ab=box(*c['ab'])
    ch=q.cosh(); sh=q.sinh()
    u=z*ub; s1=z*s1b; s2=z*s2b
    # Exact inverse of A [[1,-1,6],[1,-1,-2],[2,3,2]].
    # Use rational formulas obtained by symbolic inversion.
    A=sp.Matrix([[1,-1,6],[1,-1,-2],[2,3,2]])
    Ai=A.inv()
    rhs=[u+2*ch*z, s1-2*ch*z, s2+4*ch*z]
    v=[]
    for i in range(3):
        v.append(sum(arb(int(Ai[i,j].p))/arb(int(Ai[i,j].q))*rhs[j] for j in range(3)))
    dyf,ds,dk=v
    ad=z*ab-4*sh*z
    y=[arb(2)+dyf, arb(1)+(ds+ad)/2, arb(1)+(ds-ad)/2]
    # a_g a_h=1/z, a_g/a_h=e^q, a_f=k/z.
    a=[k/z, (q/2).exp()/z.sqrt(), (-q/2).exp()/z.sqrt()]
    return a,y


def interval_endpoint_flux():
    src=ROOT/'data'/'ach_capd'/'wazewski_T2.75.json'
    raw=json.loads(src.read_text())
    rows=[]; glo=math.inf; ghi=-math.inf
    for c in raw['checks']:
        a,y=reconstruct_from_compact(c)
        val=euler_flux(a,y); lo,hi=arb_bounds(val)
        glo=min(glo,lo); ghi=max(ghi,hi)
        rows.append(dict(d=c['d'],bE=[lo,hi],phi=c['phi'],zeta=c['zeta']))
    return {'source':str(src),'global_bE':[glo,ghi],'tiles':rows}


def main():
    out={'symbolic':symbolic_checks(),'floating_profile':float_profile(),
         'validated_endpoint':interval_endpoint_flux()}
    path=ROOT/'data'/'ach_capd'/'euler_flux_b0.8.json'
    path.write_text(json.dumps(out,indent=1)+'\n')
    print(json.dumps({'symbolic':out['symbolic'],
                      'validated_bE':out['validated_endpoint']['global_bE'],
                      'profile':out['floating_profile']},indent=1))


if __name__=='__main__':
    main()
