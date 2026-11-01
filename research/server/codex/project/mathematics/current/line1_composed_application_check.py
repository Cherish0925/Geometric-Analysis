"""Exact finite checks for the composed application, not PDE validation."""

import sympy as sp


checks = []


def identity(name, expression):
    assert sp.simplify(expression) == 0, (name, sp.simplify(expression))
    checks.append(name)


def nonnegative(name, expression):
    assert bool(sp.simplify(expression) >= 0), (name, expression)
    checks.append(name)


s, w, z, e = sp.symbols("s w z e", real=True)
q = -s + w
identity("deficit completed square", sp.Rational(3, 2) * (s**2 + 2*w**2)
         - q**2 - (s + 2*w)**2 / 2)
identity("q target relation", (q - 6) - ((s + 2*w) - 3*(s + 4))/2)
identity("w target relation", (w - 2) - ((s + 2*w) - (s + 4))/2)
identity("q-distance Young remainder", z**2/2 + 9*e**2/2
         - (z - 3*e)**2/4 - (z + 3*e)**2/4)
identity("w-distance Young remainder", z**2/2 + e**2/2
         - (z - e)**2/4 - (z + e)**2/4)

x = sp.Matrix(sp.symbols("x0:3", real=True))
v = sp.Matrix(sp.symbols("v0:3", real=True))
a, b, c, d, f = sp.symbols("a b c d f", real=True)
W = sp.Matrix([[a, c, d], [c, b, f], [d, f, -a-b]])
I = sp.eye(3)
norm = lambda matrix: sp.trace(matrix.T * matrix)
rho2 = x.dot(x)
omega = sp.sqrt(3) * x / 2
model = (omega.dot(omega)*I/3 - omega*omega.T)/2
identity("actual normalization", omega.dot(omega) - sp.Rational(3, 4)*rho2)
identity("Weyl model normalization", norm(model - (rho2*I/8 - 3*x*x.T/8)))
Elambda = (x.T*W*x)[0] + w*rho2/3
weyl_remainder = norm(W-model) - (w-sp.Rational(3, 4)*rho2)**2/6 - 3*Elambda/4
identity("trace-free Weyl fit identity", weyl_remainder - norm(W) + w**2/6)

nonnegative("amplitude coefficient below 4800", 4800 - (234*(1+2*sp.sqrt(3))**2+36))
nonnegative("total defect coefficient below 720", 720 - (1+sp.Rational(2, 3)
            +sp.Rational(4800, 27)+sp.Rational(13, 2)+sp.Rational(4800, 9)))
identity("full-gradient linear coefficient", sp.Rational(3, 4)*sp.Rational(4, 27)*117 - 13)
identity("full-gradient square-root coefficient", sp.Rational(3, 4)*sp.Rational(16, 3)-4)
identity("exterior derivative coefficient", sp.Rational(3, 4)*sp.Rational(2, 27)*117-sp.Rational(13, 2))

denom = (sp.sqrt(3)+sp.sqrt(6))**2
nonnegative("weight bound Ricci coefficient", 9-(sp.Rational(9, 2)+36/denom))
nonnegative("weight bound deficit coefficient", 9-2/denom)
identity("harmonic alignment coefficient", 4*9+sp.Rational(117, 9)-49)

P = x*x.T/2
A = (rho2*I/3-x*x.T)/2
identity("approximate projection Weyl identity", norm(W+P-I/3)
         - norm(W-A) - (rho2-2)**2/12)
identity("projection idempotence remainder", norm(P*P-P)-rho2**2*(rho2-2)**2/16)
dP = (x*v.T+v*x.T)/2
identity("projection derivative identity", norm(dP)-(rho2*v.dot(v)+x.dot(v)**2)/2)
dPi = (x*v.T+v*x.T)/rho2 - 2*x.dot(v)*x*x.T/rho2**2
identity("normalized projection derivative identity", norm(dPi)
         - 2*(rho2*v.dot(v)-x.dot(v)**2)/rho2**2)
identity("projection idempotence bound coefficient", 12**2/sp.Integer(16)-9)
identity("smallness normalization", 720*sp.Rational(1, 2880)-sp.Rational(1, 4))

lap_f, grad_f2 = sp.symbols("lap_f grad_f2", real=True)
identity("conformal scalar energy identity", (-4+6*lap_f-6*grad_f2)**2-16
         - 36*(lap_f-grad_f2)**2-48*grad_f2+48*lap_f)

for index, name in enumerate(checks, 1):
    print(f"PASS {index:02d}: {name}")
print(f"All {len(checks)} exact finite checks passed; PDE and spectral arguments are not tested here.")
