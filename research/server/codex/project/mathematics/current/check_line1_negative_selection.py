"""Exact local algebra for the variable negative-calibration argument.

This checks algebra and conformal weights, not global PDE hypotheses.
"""

import sympy as s


checks = []


def zero(name, expression):
    assert s.simplify(expression) == 0, (name, s.simplify(expression))
    checks.append(name)


u, c, t, e, lap, zeta = s.symbols("u c t e lap zeta", positive=True)
f = (u-c)/u
zero("test derivative", s.diff(f, u)-c/u**2)
zero("potential factor", u*(u**3-c**3)*(u-c)
     -u*(u**2+u*c+c**2)*(u-c)**2)
zero("scalar-test conversion",
     f*u**4*(u**(-3)*(6*lap+(-8*c**3+e)*u)+8*u)
     -(u-c)*(6*lap+(-8*c**3+e)*u+8*u**4))
zero("coercive scalar potential",
     (u-c)*((-8*c**3+e)*u+8*u**4)
     -8*u*(u**3-c**3)*(u-c)-e*u*(u-c))
zero("Weyl error transfer", 3*f*u**4*u**(-2)*zeta-3*u*(u-c)*zeta)
zero("cross-term conformal weight", u**2*s.diff(f,u)-c)
zero("opposite-sign scalar test",
     u**(-2)*u**4*(u**(-3)*(6*lap+(-4+e)*u)-8*u)
     -(6*lap/u-4+e-8*u**3))
zero("opposite-sign cross factor", u**2*s.diff(u**(-2),u)+2/u)
zero("opposite-sign Weyl error weight", u**(-2)*u**4*u**(-2)-1)
zero("connection energy conformal weight", u**4*u**(-6)*u**4-u**2)
zero("exterior energy conformal weight", u**4*u**(-6)*u**4-u**2)
zero("conformal Weyl eigenvalue", u**(-2)*(-8*u**3/3)+8*u/3)

l2, l3 = s.symbols("l2 l3", real=True)
l1 = -l2-l3
calibration = s.diag(l1, -l1/2, -l1/2)
w = s.diag(l1, l2, l3)
zero("eigenline residual", s.trace((w-calibration)**2)-(l2-l3)**2/2)
zero("model norm", s.trace(s.diag(-4*t/3,2*t/3,2*t/3)**2)-8*t**2/3)

# In an oriented orthonormal frame omega=e12+e34 has norm sqrt(2).
# Verify |xi wedge omega|^2=|xi|^2 directly in exterior coordinates.
x = s.symbols("x0:4", real=True)
omega = {(0, 1): 1, (2, 3): 1}
three = {}
for i in range(4):
    for pair, coefficient in omega.items():
        indices = (i,)+pair
        if len(set(indices)) < 3:
            continue
        inversions = sum(indices[j] > indices[k]
                         for j in range(3) for k in range(j+1, 3))
        key = tuple(sorted(indices))
        three[key] = three.get(key, 0)+(-1)**inversions*x[i]*coefficient
zero("normalized self-dual wedge isometry",
     sum(v**2 for v in three.values())-sum(v**2 for v in x))

print(f"Passed {len(checks)} exact checks")
for name in checks:
    print("PASS", name)
