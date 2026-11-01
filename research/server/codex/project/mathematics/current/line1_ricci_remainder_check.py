"""Finite algebra for the non-Kahler bridge and energy-selection companion.

This checks identities and coefficient reductions, not PDE certification.
"""

import sympy as sp


def check(value, label):
    assert sp.simplify(sp.expand(value)) == 0, (label, value)
    print(f"PASS: {label}")


pi = sp.pi
p, A, T, D, P, S2, R2 = sp.symbols("p A T D P S2 R2", real=True)
R_formula = 8*pi**2*(2*p-T) + 32*pi**2*D
P_formula = R_formula-S2/4
Bp = S2-32*pi**2*p
B = S2-32*pi**2*A
check(P_formula+Bp/4-8*pi**2*(p-T)-32*pi**2*D,
      "polarized Ricci-energy identity")
check(P_formula+B/4-16*pi**2*(p-A)-8*pi**2*(A-T)-32*pi**2*D,
      "unpolarized equivalent identity")

q2, t2, qt, delta, beta = sp.symbols("q2 t2 qt delta beta", real=True)
scalar2 = (t2-4*qt+4*q2)/9
check((scalar2-32*pi**2*p).subs(q2, 72*pi**2*p+beta)
      - (4*beta-4*qt+t2)/9,
      "scalar excess from signed square decomposition")
check((4*beta+t2).subs(beta, delta-t2/2)-(4*delta-t2),
      "nonnegative scalar term estimate")

eps, A0, dtop = sp.symbols("eps A0 dtop", positive=True)
R0 = 8*pi**2*(A0+dtop)
check(R_formula.subs(T, A0-dtop)-R0
      -16*pi**2*(p-A0)-32*pi**2*D,
      "absolute Ricci excess splits into two nonnegative losses")
check(2*(sp.Rational(9, 2)*eps)
      *(72*pi**2*(A0+eps/(16*pi**2))+sp.Rational(9, 2)*eps)
      -81*eps*(8*pi**2*A0+eps),
      "square root reduction in scalar excess bound")
check(sp.Rational(4, 9)*(sp.Rational(9, 2)*eps)-2*eps,
      "linear coefficient in scalar excess bound")
check((R0+eps)-(32*pi**2*p+Bp)/4-8*pi**2*dtop
      -(eps-8*pi**2*(p-A0)-Bp/4),
      "trace-free energy difference identity")
z = sp.symbols("z", nonnegative=True)
check(eps/2-(2*eps+4*z)/4+z,
      "finite trace-free lower remainder cancellation")

V, kappa, Q, L = sp.symbols("V kappa Q L", positive=True)
check(4-16*kappa**2*V/(4*kappa**2*V+Q)
      -4*Q/(4*kappa**2*V+Q),
      "relative Einstein defect at negative mean scalar")
Cvar = sp.symbols("Cvar", positive=True)
check(32*pi**2*D+(144*pi**2*Cvar*D)/4
      -(32*pi**2+36*pi**2*Cvar)*D,
      "conditional inverse bridge coefficient")

Ws, dS = sp.symbols("Ws dS", real=True)
ricci_cw = 4*Ws+S2/3-8*pi**2*T
ricci0_cw = 4*Ws+S2/12-8*pi**2*T
lebrun = S2/(96*pi**2)+Ws/(8*pi**2)-p/2
check(ricci_cw-ricci_cw.subs(S2,S2-dS)-dS/3,
      "conformal Ricci energy difference")
check(ricci0_cw-ricci0_cw.subs(S2,S2-dS)-dS/12,
      "conformal trace-free Ricci energy difference")
check(lebrun-lebrun.subs(S2,S2-dS)-dS/(96*pi**2),
      "conformal LeBrun defect difference")

print("All 14 finite algebra checks passed; geometric inputs remain explicit.")
