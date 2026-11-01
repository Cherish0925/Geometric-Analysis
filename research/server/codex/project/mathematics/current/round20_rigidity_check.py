"""Exact finite identities for round20_rigidity.md, not a gauge-theory proof."""

import sympy as sp

R = sp.Rational
e, T, r2, P, w2 = sp.symbols("e T r2 P w2", real=True)

# Chern--Weil after eliminating scalar energy via |Ric|^2=P+s^2/4.
chern = 2*w2 + (4*(r2-P))/24-P/2
assert sp.expand(chern-(2*w2+r2/6-2*P/3)) == 0
classical = R(3, 2)*T + 3/(16*sp.pi**2)*e/4*(24*sp.pi**2*T/(1-e))
assert sp.simplify(classical-3*(4-e)*T/(8*(1-e))) == 0

# A genuinely non-diagonal positive graph: Q=(++--), H=graph(X).
X = sp.Matrix([[R(1, 5), R(1, 7)], [R(1, 11), -R(1, 6)]])
I = sp.eye(2)
Q = sp.diag(1, 1, -1, -1)
B = I.col_join(X)
Gram = B.T*Q*B
assert Gram == I-X.T*X
assert Gram[0, 0] > 0 and Gram.det() > 0
Proj = B*Gram.inv()*B.T*Q
assert Proj*Proj == Proj
assert Proj.T*Q == Q*Proj
U = I.col_join(sp.zeros(2))
assert sp.simplify(U.T*Proj.T*Q*Proj*U-Gram.inv()) == sp.zeros(2)

# Associated Hodge norm and the exact p / negative-part identities.
J = 2*Proj-sp.eye(4)
Hodge = Q*J
assert J*J == sp.eye(4)
assert Hodge == Hodge.T
z = sp.Matrix([1, 2, -1, 3])
p = (Proj*z).dot(Q*Proj*z)
n = -((sp.eye(4)-Proj)*z).dot(Q*(sp.eye(4)-Proj)*z)
assert sp.simplify(p-n-z.dot(Q*z)) == 0
assert sp.simplify(z.dot(Hodge*z)-(2*p-z.dot(Q*z))) == 0

# Null-radical escape: arbitrary fixed hodge plane can be reduced to this
# Witt basis. Scaling the null line shrinks every vector in l+Z while the
# dual null line grows. This checks the exact algebra, not compactness.
t = sp.symbols("t", positive=True)
Qw = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
Aw = sp.diag(1/t, t, 1)
assert Aw.T*Qw*Aw == Qw
c, zz = sp.symbols("c zz", real=True)
wv = sp.Matrix([c, 0, zz])
assert (Aw*wv).dot(Aw*wv) == c*c/(t*t)+zz*zz
dual = sp.Matrix([0, 1, 0])
assert (Aw*dual).dot(Aw*dual) == t*t

# Ric=-g product KE normalization; V=2*pi^2*T and s=-4.
V = 2*sp.pi**2*T
scalar = -4
W = sp.diag(-R(2, 3), R(1, 3), R(1, 3))
W0 = sp.diag(-R(1, 6), R(1, 12), R(1, 12))
assert sp.trace((W-W0)**2) == R(3, 8)
assert sp.trace(W**2) == R(2, 3)
assert sp.simplify(scalar**2*V-32*sp.pi**2*T) == 0
q = -scalar + sp.sqrt(6)*sp.sqrt(sp.trace(W**2))
assert q == 6
assert sp.simplify(q*q*V-72*sp.pi**2*T) == 0
assert sp.simplify((scalar**2/24+2*sp.trace(W**2))*V-4*sp.pi**2*T) == 0

# Product topology and b+ = b- = 1+2gh.
g, h = sp.symbols("g h", integer=True, positive=True)
chi = (2-2*g)*(2-2*h)
b1 = 2*g+2*h
b2 = 2+4*g*h
assert sp.expand(2-2*b1+b2-chi) == 0
assert sp.expand(2*chi-8*(g-1)*(h-1)) == 0
assert b2/2 == 1+2*g*h

print("Round 20 rigidity: 6 exact identity groups passed.")
print("Scope: radius, graph projection, Hodge norm, null escape, KE calibration, topology.")
print("Not checked by finite computation: monopole existence, collar and quotient arguments.")
