"""Exact local identities for the whole-fibre receiver, not a global proof."""
import sympy as s

t = s.symbols("t", real=True)
z = s.Function("z")(t)
f = 1 / s.cosh(t) ** 2
J = s.atan(s.sinh(t))

def P(expr):
    return s.diff(expr, t, 2) + s.tanh(t) * s.diff(expr, t)

def zero(expr):
    return s.simplify(s.expand_trig(expr).rewrite(s.exp)) == 0

assert zero(-P(f) + (2 - 4*f)*f)
assert zero((-P(f*z)+(2-4*f)*f*z)/f
            - (-s.diff(z,t,2)+3*s.tanh(t)*s.diff(z,t)))
assert zero(P(J))
assert zero(s.diff(J,t)-1/s.cosh(t))
assert zero(s.diff(f,t)+2*s.tanh(t)*f)  # divergence of f T

# x=tanh(t): sech^3(t) dt = sqrt(1-x^2) dx.
x = s.symbols("x", real=True)
mass = s.integrate(s.sqrt(1-x*x),(x,-1,1))
assert mass == s.pi/2
assert -mass/4 == -s.pi/8

# The conjugated horizontal operator has an exact nonnegative ground state.
v = 1/s.cosh(t)**s.Rational(3,2)
potential = s.Rational(9,4)-s.Rational(15,4)/s.cosh(t)**2
assert zero(-s.diff(v,t,2)+potential*v)

# A noncommuting trace-free fibre path still has the same quadratic stress.
a,b,c,d,j,jp,u = s.symbols("a b c d j jp u", real=True)
A = s.Matrix([[a,b],[b,-a]])
B = s.Matrix([[c,d],[d,-c]])
V = A+j*B
H = s.eye(2)+u*V+u*u*(V*V)/2
Hinv = s.eye(2)-u*V+u*u*(V*V)/2
Ht = H.diff(j)*jp
shape = Hinv*Ht/2
quadratic = s.expand(s.trace(shape*shape)).coeff(u,2)
assert s.simplify(quadratic-jp*jp*s.trace(B*B)/4) == 0
assert s.expand(s.det(H)).coeff(u,1) == 0
assert s.expand(s.det(H)).coeff(u,2) == 0

print("PASS: ground transform, bounded harmonic profile, TT detector, exact receiver coefficient, noncommuting fibre stress")
print("Scope: algebraic and one-dimensional identities only; no compactness, gauge, or global Einstein theorem certified by this script.")
