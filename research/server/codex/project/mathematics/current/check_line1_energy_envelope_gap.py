"""Exact transfer checks; not a gauge/PDE proof or a metric construction."""

import json
import sympy as sp


checks = []


def equal(name, lhs, rhs=0):
    remainder = sp.factor(lhs - rhs)
    assert remainder == 0, (name, remainder)
    checks.append(name)


b, z = sp.symbols("beta z", positive=True)
R, P, T, p, A, V = sp.symbols("R P T p A V", real=True)
pi = sp.pi
S2 = 4*(R-P)
W2 = 2*pi**2*T-R/12+P/3
K = (b+1)*(8-b)/(2*b)
L = 2*(b+1)*(b-2)/b
D = (b+1)/b*(S2+6*b*W2)-72*pi**2*p
equal("exact Chern-Weil identity", D,
      K*R+L*P+12*pi**2*(b+1)*T-72*pi**2*p)
equal("parameter eight loses energy", K.subs(b, 8))
equal("parameter eight coefficient", L.subs(b, 8), sp.Rational(27, 2))
equal("K decreases on positive parameters", sp.diff(K, b), -sp.Rational(1, 2)-4/b**2)
equal("L increases on positive parameters", sp.diff(L, b), 2+4/b**2)
equal("maximum K on two to eight", K.subs(b, 2), sp.Rational(9, 2))
equal("minimum L on two to eight", L.subs(b, 2), 0)

h = (1-z**2)/3
bstar = (8-2*z)/(1+2*z)
F = (4-z)**2/9
f_b = (9-sp.Rational(3, 2)*(b+1)*(1-h))/K
equal("selected parameter reaches envelope", f_b.subs(b, bstar), F)
equal("exact nonnegative optimization loss", F-f_b,
      2*((2*z+1)*b+2*z-8)**2/(9*(8-b)*(b+1)))
equal("envelope exceeds all-metrics infimum", F-(1+h), 4*(1-z)**2/9)
equal("energy excess h-squared form", F-(1+h), 4*h**2/(1+z)**2)
equal("parameter distance to endpoint", bstar-2, 18*h/((1+z)*(1+2*z)))
equal("parameter distance at least three h", bstar-2-3*h,
      (1-z)**2*(2*z+5)/(2*z+1))
equal("classical envelope scalar coordinate", (2*(4-z)/3)**2/4, F)
equal("classical boundary ellipse", (2*(4-z)/3)**2+8*((1+2*z)/3)**2,
      12*(1-h))

ee = sp.symbols("e", real=True)
D_selected = D.subs({R:8*pi**2*A*ee, T:A*(1-h), b:bstar})
equal("retained actual projection loss", D_selected,
      8*pi**2*A*K.subs(b, bstar)*(ee-F)+L.subs(b, bstar)*P-72*pi**2*(p-A))
assert 1+sp.Rational(27, 2) <= sp.Rational(81, 2)
assert 9*sp.Rational(9, 2) == sp.Rational(81, 2)
checks.append("uniform transfer coefficients")
equal("final h-squared coefficient", sp.Rational(2, 81)*9, sp.Rational(2, 9))

# Formal constant moments, deliberately not a realized metric.
b0 = sp.Rational(7, 2)
V0 = 2*pi**2*A*sp.Rational(49, 36)
formal = {R:4*V0, P:0, T:sp.Rational(3, 4)*A, p:A}
equal("witness Weyl norm", (6*W2/V0).subs(formal), sp.Rational(64, 49))
equal("witness all classical functional deficits", (D/V0).subs(formal),
      16*(b-b0)**2/(b*b0**2))
equal("witness new functional vanishes", (D/V0).subs(formal).subs(b, b0))
equal("witness old functional positive", (D/V0).subs(formal).subs(b, 8),
      sp.Rational(162, 49))
assert 16-32*pi**2*A/V0 > 0
checks.append("witness classical scalar constraint")

# Actual KE rescalings limit the strongest possible beta-eight coefficient.
t = sp.symbols("t", positive=True)
ke_old = 4*(1-1/t)**2+18/t**2
equal("actual KE old-functional minimum", ke_old-sp.Rational(36, 11),
      2*(2*t-11)**2/(11*t**2))
equal("witness clears every possible beta-eight coefficient",
      sp.Rational(162, 49)-sp.Rational(36, 11), sp.Rational(18, 539))

# Four-dimensional homothety: R is invariant and V_t=t^2 V.
I, lam = sp.symbols("I lambda", real=True)
quotient = (R-2*lam*I+4*lam**2*V)/(lam**2*V)
rescaled_error = R/(t*t*V)+2*I/(t*V)+4
equal("negative-scale quotient becomes normalized error", quotient.subs(lam, -t),
      rescaled_error)
equal("relative minimizer", quotient.subs(lam, R/I), 4-I*I/(R*V))
equal("positive-target signed scalar lower bound", 4-(4*R-32*pi*pi*A)/R,
      4/(R/(8*pi*pi*A)))
equal("envelope upper endpoint", F.subs(z, 0), sp.Rational(16, 9))
assert 4/sp.Rational(25, 9) == sp.Rational(36, 25) > 1
checks.append("positive-target case is harmless below frontier plus one")

rejected = []
for name, false_expression in [
    ("parameter eight controls the energy coordinate", K.subs(b, 8)),
    ("classical envelope equals the absolute infimum", F-(1+h)),
    ("formal witness is excluded by maximal beta-eight bound",
     sp.Rational(36, 11)-sp.Rational(162, 49)),
]:
    if name.startswith("parameter"):
        assert false_expression == 0
    elif name.startswith("classical"):
        assert sp.factor(false_expression) != 0
    else:
        assert false_expression < 0
    rejected.append(name)

print(json.dumps({
    "status": "passed", "exact_checks": len(checks), "checks": checks,
    "rejected_false_variants": rejected,
    "scope": "finite exact algebra; no metric realization or inherited PDE certification",
}, indent=2))
