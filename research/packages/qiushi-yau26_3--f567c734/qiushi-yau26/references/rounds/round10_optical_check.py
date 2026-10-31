"""Exact algebra checks for the optical Ricci-deficit identity.

These check local curvature and one-dimensional identities, not the
existence of a small-error complete connector.
"""
import sympy as s


def zero(expr):
    assert s.simplify(s.trigsimp(expr)) == 0, expr


# Recompute the full four-dimensional conformal-flat Ricci tensor from
# coordinate Christoffel symbols, independently of the warped formulas.
x = s.symbols("x0:4", real=True)
omega = s.Function("omega")(x[0])
g = s.eye(4) / omega**2
gi = s.eye(4) * omega**2
christoffel = [[[sum(gi[i, l] * (
    s.diff(g[l, k], x[j]) + s.diff(g[l, j], x[k])
    - s.diff(g[j, k], x[l])) / 2 for l in range(4))
    for k in range(4)] for j in range(4)] for i in range(4)]
ric = s.zeros(4)
for i in range(4):
    for j in range(4):
        ric[i, j] = s.simplify(sum(
            s.diff(christoffel[k][i][j], x[k])
            - s.diff(christoffel[k][i][k], x[j])
            + sum(christoffel[k][k][l] * christoffel[l][i][j]
                  - christoffel[k][j][l] * christoffel[l][i][k]
                  for l in range(4)) for k in range(4)))
err = s.simplify(gi * ric + 3 * s.eye(4))
wp = s.diff(omega, x[0])
wpp = s.diff(omega, x[0], 2)
zero(err[0, 0] - 3 * (1 - wp**2 + omega*wpp))
for i in range(1, 4):
    zero(err[i, i] - (3 * (1-wp**2) + omega*wpp))
for i in range(4):
    for j in range(4):
        if i != j:
            zero(err[i, j])
zero(err[1, 1] - err[0, 0] + 2*omega*wpp)
print("PASS: coordinate Ricci, both error blocks, and signed anisotropy")

t = s.symbols("t", real=True)
m = s.symbols("m", positive=True)
w = s.sin(t)
# Flat optical cylinder: positive Neumann ground state f=1, lambda=0.
d = -m*w*s.diff(w, t, 2)
zero(s.integrate(d/w, (t, 0, s.pi)) - 2*m)
zero(s.integrate(m*s.diff(w, t)**2, (t, 0, s.pi))
     - m*s.pi/2)
print("PASS: complete cosh-cylinder identity and endpoint cost")

# A nonconstant exact Neumann ground state, with an operator having
# nonnegative quadratic form by its ground-state factorization.
f = 2 + s.cos(2*t)
lam = s.Rational(3, 2)
rk = -lam - m*s.diff(f, t, 2)/f
aw = -m*s.diff(w, t, 2) - rk*w
boundary = m*(f.subs(t, 0)+f.subs(t, s.pi))
lhs = s.integrate(s.expand_trig(s.simplify(f*aw)), (t, 0, s.pi))
rhs = lam*s.integrate(f*w, (t, 0, s.pi)) + boundary
zero(lhs-rhs)
zero(s.diff(f, t).subs(t, 0))
zero(s.diff(f, t).subs(t, s.pi))
print("PASS: nonconstant ground state and Green boundary signs")

# Conformal null-Ricci identity: u=-log(Omega), so the null conformal
# correction -m(u''-(u')^2) equals m Omega''/Omega.
u = -s.log(omega)
zero(-m*(s.diff(u, x[0], 2)-s.diff(u, x[0])**2)
     - m*wpp/omega)
print("PASS: auxiliary null Ricci conformal correction")

# At an optical maximum, small anisotropy need not mean small full error.
epsilon = s.symbols("epsilon", positive=True)
jet = {wp: 0, wpp: -epsilon/(2*omega)}
zero(err[1, 1].subs(jet) - (3-epsilon/2))
zero((err[1, 1]-err[0, 0]).subs(jet) - epsilon)
print("PASS: scalar necessary condition does not solve both Ricci blocks")

bad = [lhs-(lam*s.integrate(f*w, (t, 0, s.pi))-boundary),
       err[1, 1]-err[0, 0]-2*omega*wpp]
for mutation in bad:
    assert s.simplify(mutation) != 0
print("PASS: reversed endpoint sign and reversed anisotropy rejected")
