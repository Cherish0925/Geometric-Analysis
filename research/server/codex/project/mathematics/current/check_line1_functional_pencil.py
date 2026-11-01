"""Exact finite checks; no claim to verify the gauge/PDE existence arguments."""

import json
import sympy as sp


checks = []


def zero(name, expression):
    value = sp.factor(expression)
    assert value == 0, (name, value)
    checks.append(name)


b = sp.symbols("beta", positive=True)
s, w, p, volume = sp.symbols("s w p V", real=True)
pi = sp.pi
q = -s + w
zero("full functional square split", (b+1)/b*(s*s+b*w*w)-q*q-(s+b*w)**2/b)
e, z = sp.symbols("e z", real=True)
sub = {s: e-4, w: (z-e+4)/b}
qstar = 4*(b+1)/b
zero("raw norm fit", (w-4/b).subs(sub)-(z-e)/b)
zero("raw amplitude fit", (q-qstar).subs(sub)-z/b+(1+1/b)*e)

rho, uu = sp.symbols("rho u", real=True)
c2 = 9*b/(8*(b+1))
alpha = 9/(8*(b+1))
zero("tensor normalization", c2/b-alpha)
zero("norm-squared target", c2*4*qstar/9-2)
zero("Weyl norm coefficient", (2*alpha*rho*rho).subs(rho, 2*uu/3)-uu*uu/(b+1))
zero("raw angular error factor", (w-uu*uu/(b+1))-(s+b*w+q-uu*uu)/(b+1))

# Orthogonal invariance lets psi=(rho,0,0); W is otherwise arbitrary.
x, y, a12, a13, a23 = sp.symbols("x y a12 a13 a23", real=True)
weyl = sp.Matrix([[x, a12, a13], [a12, y, a23], [a13, a23, -x-y]])
psi = sp.Matrix([rho, 0, 0])
model = alpha*(rho*rho*sp.eye(3)/3-psi*psi.T)
norm = lambda matrix: sp.trace(matrix.T*matrix)
elambda = (psi.T*weyl*psi)[0] + w*rho*rho/3
lhs = norm(weyl-model)
rhs = (w-2*alpha*rho*rho)**2/6 + 2*alpha*elambda
zero("full angular polynomial identity", lhs-rhs-norm(weyl)+w*w/6)
zero("parameter gap factor", (1/b)**2*(1-2/b)**2-(b-2)**2/b**4)

T, P, S2, W2 = sp.symbols("T P S2 W2", real=True)
d8 = sp.Rational(9, 8)*(S2+48*W2)-72*pi*pi*p
cw_s2 = 96*pi*pi*T-48*W2+12*P
zero("beta eight Chern-Weil identity", d8.subs(S2,cw_s2)-108*pi*pi*(T-sp.Rational(2,3)*p)-sp.Rational(27,2)*P)
dlb = (S2/24+W2/2)/(4*pi*pi)-p/2
d2 = sp.Rational(3,2)*(S2+12*W2)-72*pi*pi*p
zero("beta two LeBrun normalization", d2-144*pi*pi*dlb)
zero("KE endpoint exact deficit", (b+1)/b*(16+4*b)-36-4*(b-2)**2/b)
zero("classical lower-side excess", 8*(4+b)-72*b/(b+1)-8*(b-2)**2/(b+1))

# Formal moment data, not an assertion of metric realization.
p_per_v = 2*(b+1)**2/(9*pi*pi*b*b)
formal_d8 = sp.Rational(9,8)*(16+8*(4/b)**2)-72*pi*pi*p_per_v
zero("old functional at formal new calibration", formal_d8-2*(8/b-1)**2)
T_per_v = (sp.Rational(2,3)+sp.Rational(16,3)/b**2)/(4*pi*pi)
ratio = 3*(b*b+8)/(4*(b+1)**2)
zero("formal topology ratio", T_per_v/p_per_v-ratio)
zero("formal ratio derivative", sp.diff(ratio,b)-3*(b-8)/(2*(b+1)**3))

# Cauchy-Schwarz plus old scalar inequality: constrained minimization.
# Units: sqrt(8*pi^2*p); x >= 2 and x+y >=3.
xx = sp.symbols("xx", nonnegative=True)
zero("classical feasible quadratic", xx*xx+b*(3-xx)**2-(1+b)*(xx-3*b/(1+b))**2-9*b/(1+b))
zero("classical boundary selection", sp.diff(xx*xx+b*(3-xx)**2,xx).subs(xx,2)-(4-2*b))

zero("harmonic target normalization squared", 32*pi*pi*c2/qstar-(3*pi*b/(b+1))**2)
zero("endpoint differential coefficient", sp.Rational(3,4)*sp.Rational(4,27)*117-13)
zero("endpoint canonical alignment", 4*9+sp.Rational(117,9)-49)
# The safe weight coefficient in (29) is strictly below nine.
assert sp.Rational(9,2)+36/(sp.sqrt(3)+sp.sqrt(6))**2 < 9
checks.append("endpoint weight coefficient below nine")

print(json.dumps({"status": "passed", "count": len(checks), "checks": checks,
                  "scope": "exact finite algebra only; no PDE, topology or novelty certification"}, indent=2))
