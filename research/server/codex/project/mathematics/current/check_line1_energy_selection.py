"""Exact algebra checks for the energy-selection manuscript.

These verify formulas and finite countermodels, not SW or the Yamabe theorem.
Run with Python and SymPy; no local file mutation.
"""
import json
import sympy as s

checks = []


def equal(name, left, right=0):
    assert s.simplify(left - right) == 0, name
    checks.append(name)


q, t, ss, w = s.symbols("q t ss w", real=True)
equal("pointwise defect split",
      ss**2 / 24 + w**2 / 12,
      (-ss + w)**2 / 36 + (ss + 2*w)**2 / 72)
equal("scalar inversion", ((ss + 2*w) - 2*(-ss + w))/3, ss)

pi = s.pi
p, A, d, D, Bp, L = s.symbols("p A d D Bp L", real=True)
T = A - d
R = 8*pi**2*(2*p - T) + 32*pi**2*D
S2 = 32*pi**2*p + Bp
P = R - S2/4
J = R - 8*pi**2*(A+d)
equal("exact energy excess", J, 16*pi**2*(p-A)+32*pi**2*D)
equal("projected scalar loss", P+Bp/4, 8*pi**2*(p-T)+32*pi**2*D)
equal("tracefree energy selection",
      P, 8*pi**2*d+J-8*pi**2*(p-A)-Bp/4)
equal("relative defect numerator", 4*P+L, 4*R-S2+L)
equal("relative minimizer profile",
      ((4*P+L)/R).subs({p:A,D:0,Bp:0}),
      (32*pi**2*d+L)/(8*pi**2*(A+d)))

delta, Delta, U, qt = s.symbols("delta Delta U qt", real=True)
S2_expansion = (4*(72*pi**2*p+Delta)+U-4*qt)/9
equal("scalar surplus from q,t", 9*(S2_expansion-32*pi**2*p),
      4*Delta+U-4*qt)
equal("retained scalar surplus", (4*Delta+U-4*qt).subs(Delta,delta-U/2),
      4*delta-U-4*qt)

C, H, jj = s.symbols("C H jj", positive=True)
threshold = (s.sqrt(C**2+4*H**2)-C)/2
equal("Einstein energy threshold", threshold*(C+threshold), H**2)

sg, sh, Weyl, top = s.symbols("sg sh Weyl top", real=True)
Rg, Rh = 4*Weyl+sg/3-8*pi**2*top, 4*Weyl+sh/3-8*pi**2*top
equal("conformal Ricci energy drop", Rg-Rh, (sg-sh)/3)
equal("conformal tracefree energy drop", (Rg-sg/4)-(Rh-sh/4), (sg-sh)/12)
equal("conformal LeBrun defect drop",
      sg/(96*pi**2)-sh/(96*pi**2), (sg-sh)/(96*pi**2))

# Equal bulk volumes, conformal multipliers 1 and 2. This checks the
# limiting moment formula, not the existence of its geometric realization.
v1, v2, c1, c2 = s.symbols("v1 v2 c1 c2", positive=True)
v0 = v1+v2
vf = v1*c1**4+v2*c2**4
sf = -4*(v1*c1**2+v2*c2**2)
r0 = 4*v0
ef = 4-sf**2/(vf*r0)
lf = 16*v0-sf**2/vf
equal("two-scale variance and relative defect", ef, lf/r0)
equal("two-scale moment numerator",
      v0*vf-(v1*c1**2+v2*c2**2)**2,
      v1*v2*(c1**2-c2**2)**2)
equal("two-scale exact example", ef.subs({v1:1,v2:1,c1:1,c2:2}), s.Rational(18,17))

# Reject false simplifications rather than checking only identities.
rejected = []
for name, false_claim in [
    ("D and primitive cost force zero Einstein defect", ef == 0),
    ("Yamabe drop factor is one quarter", s.simplify((Rg-Rh)-(sg-sh)/4) == 0),
    ("every minimizing sequence has no variance contribution", s.simplify(
        (32*pi**2*d+L)/(8*pi**2*(A+d))-4*d/(A+d)) == 0),
]:
    assert not false_claim, name
    rejected.append(name)

print(json.dumps({"exact_checks": len(checks), "checks": checks,
                  "rejected_false_variants": rejected}, indent=2))
