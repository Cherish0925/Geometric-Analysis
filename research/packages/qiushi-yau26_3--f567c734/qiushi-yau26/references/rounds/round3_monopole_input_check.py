"""Exact normalization and constant checks for round3_monopole_input.md."""

import sympy as sp

R = sp.Rational
rho, q, f = sp.symbols("rho q f", real=True)
u = 3 * rho / 2
assert sp.expand(q * u**2 - f * u**3
                 - R(27, 8) * (R(2, 3) * q * rho**2 - f * rho**3)) == 0

# Exact two-Holder factorization; v=Z^(1/3), Q=integral q u^2.
X, Y, v, Q, C, J, base = sp.symbols("X Y v Q C J base", positive=True)
P, H1, H2 = Q - v**3, X * v**2 - Q, Y * v**2 - C
identity = 18 * J + H2 + Y * (X + v) / v**2 * (P + H1)
assert sp.simplify(identity.subs(C, base + 18 * J) - (Y * X**2 - base)) == 0
theta = sp.symbols("theta", positive=True)
assert sp.simplify((1 + theta) / theta**2 - 2
                   + (theta - 1) * (2 * theta + 1) / theta**2) == 0

# Hopf differential at z=(r,0); equivariance supplies every nonzero z.
r, a, b, c, d = sp.symbols("r a b c d", real=True)
hopf_differential_squared = (2 * r * a)**2 + (2 * r * c)**2 + (2 * r * d)**2
assert sp.expand(hopf_differential_squared
                 - 4 * r**2 * (a*a+b*b+c*c+d*d) + 4 * (r*b)**2) == 0

alpha, z, s = sp.symbols("alpha z s", real=True)
w = -alpha + z
G = (2*s/3 - 2*alpha)**2 - (2*s/3 + 2*w)**2
assert sp.expand(G - 2*z*(-4*s/3 + 4*alpha - 2*z)) == 0
assert sp.expand(R(3, 2)*alpha**2 + R(1, 24) + w/2
                 - (R(3, 2)*(alpha-R(1, 6))**2 + z/2)) == 0

amin, amax, zmax = R(61, 384), R(67, 384), R(1, 512)
gap = R(3, 2)*(amin-zmax) - sp.sqrt(6*amax*zmax)/2
assert sp.simplify(gap-R(1, 8)).is_positive
assert 4 + R(1, 16) + 3*amax == R(587, 128) < 5
assert R(1+81, 64) == R(41, 32)
assert 2*R(4, 9)*R(1, 12)*R(41, 32) == R(41, 432)
assert R(9, 8)*R(16, 27) + R(20, 24)*R(8, 27) == R(74, 81) < 1
assert R(1, 8) + R(9, 8)*576 + R(20, 24)*R(41, 432) < 649

# Verify the rank-one identity without dividing by the vector norm.
p = sp.Matrix(sp.symbols("p0:3", real=True))
Pi = sp.diag(1, 0, 0)
rho2 = p.dot(p)
error = p*p.T-rho2*Pi
assert sp.expand(sp.trace(error.T*error) - 2*rho2*(p[1]**2+p[2]**2)) == 0

print("Exact monopole input checks passed.")
print("Deficit normalization:", R(27, 8))
print("Good-set spectral gap lower bound:", gap.evalf())
print("Weyl approximation constants: Delta coefficient", R(74, 81),
      "; density coefficient", R(1, 8)+648+R(205, 2592))
