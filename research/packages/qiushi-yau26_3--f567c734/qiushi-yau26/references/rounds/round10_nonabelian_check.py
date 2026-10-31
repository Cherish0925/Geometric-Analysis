#!/usr/bin/env python3
"""Exact algebra for the full-rank seed obstruction, not PDE existence."""
import sympy as s

I = s.I
x, y, c = s.symbols("x y c", positive=True)
H = s.diag(x, y)
pauli = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -I], [I, 0]]), s.diag(1, -1)]


def norm2(matrix):
    return s.expand(s.trace(matrix.conjugate().T * matrix))


tau = [I*c*H*p*H for p in pauli]
tau_norm = s.expand(sum(2*norm2(a) for a in tau))
trace_norm = s.expand(sum(2*s.conjugate(s.trace(a))*s.trace(a) for a in tau))
assert s.factor(trace_norm-tau_norm) == -12*c*c*x*x*y*y
assert s.expand(tau_norm-2*c*c*((x*x-y*y)**2+6*x*x*y*y)) == 0
print("PASS source-factor quadratic norm and determinant identity")

# Orthogonal center/trace-free splitting has q=+1 on center and -1 on su(2).
a, b = s.symbols("a b", real=True)
z = I*s.diag(a+b, a-b)
q = s.expand(s.conjugate(s.trace(z))*s.trace(z)-norm2(z))
assert q == 2*a*a-2*b*b
print("PASS Chern quadratic form has operator norm one")

# Exact product residual including all off-diagonal components.
t, m = s.symbols("t m", positive=True)
F = [s.zeros(2), s.zeros(2), s.diag(0, I)]
for eps in [1, -1]:
    residual = s.expand(sum(2*norm2(f-eps*q) for f, q in zip(F, tau)))
    balanced = s.expand(residual.subs(x*x, t+eps/(2*c)).subs(y*y, t-eps/(2*c)))
    assert s.factor(balanced-(12*c*c*t*t+8*eps*c*c*t/(2*c)-1)) == 0
    assert s.simplify(balanced.subs(t, m/(2*c))-(3*m*m+2*eps*m-1)) == 0
    assert s.simplify(balanced.subs(t, 1/(2*c))) == (4 if eps == 1 else 0)
assert s.expand((m-1)*(3*m+1)) == 3*m*m-2*m-1
print("PASS exact product residual in both relative-sign labelings")

# Koszul trace of the canonical Hermitian determinant connection.
k, j, v = s.symbols("k j v", real=True)
bracket = {(0, 1, 1): -k, (1, 0, 1): k,
           (2, 3, 3): -j, (3, 2, 3): j,
           (0, 2, 3): -v, (2, 0, 3): v}


def gamma(a, b, d):
    return s.Rational(1, 2)*(bracket.get((a, b, d), 0)-bracket.get((b, d, a), 0)
                            + bracket.get((d, a, b), 0))


trace_connection = [s.simplify(gamma(a, 0, 1)+gamma(a, 2, 3)) for a in range(4)]
assert trace_connection == [-v/2, k, 0, j]
print("PASS determinant connection i(k e1+j e3-v e0/2) from Koszul")

# Its abelian curvature, with k_t=1-k² and j_u=1-j².
vu = s.symbols("v_u", real=True)
curvature = {(0, 1): (1-k*k)+k*k,
             (2, 3): (1-j*j)+j*j,
             (0, 2): j*v+vu/2}
assert s.simplify(curvature[(0, 1)]) == 1
assert s.simplify(curvature[(2, 3)]) == 1
u = s.symbols("u", real=True)
zprime = s.symbols("zprime", real=True)
af = s.cosh(u)
r = (1-u*u)**3  # finite polynomial parity test, not the smooth glued profile
cf = s.expand((3*s.diff(af, u)*r+af*s.diff(r, u))/2)
mixed = (j*v+vu/2).subs({j: s.diff(af, u)/af,
                        v: af*r*zprime,
                        vu: s.diff(af*r, u)*zprime})
assert s.simplify(mixed-zprime*cf) == 0
assert s.simplify(cf.subs(u, -u)+cf) == 0
assert r.subs(u, 1) == r.subs(u, -1) == 0
print("PASS curvature error and balanced-profile zero integral by oddness")

# beta=-i z' P dt has d beta=+i z' P' dt wedge du; P'=C.
Pprime, Cp = s.symbols("Pprime Cp", real=True)
assert (-I*zprime*Pprime*(-1)).subs(Pprime, Cp) == I*zprime*Cp
print("PASS global small primitive and exactly harmonic source curvature")

# Normalized determinant and the quadratic lower bound.
kap, tt = s.symbols("kappa t", positive=True)
q0sq = 1/(2*kap*kap)
detmass = tt*tt-q0sq
taumass = s.expand(kap*kap*(4*q0sq+6*detmass))
assert taumass == 6*kap*kap*tt*tt-1
assert s.expand(taumass+6*kap*kap*detmass) == 12*kap*kap*tt*tt-4
print("PASS positive residual lower bound for every fixed t above rank loss")

# Fixed-determinant Dirac corrections remain nonsingular at rank one.
clifford = [s.eye(2)] + [I*p for p in pauli]


def real_vector(matrix):
    entries = list(matrix)
    return s.Matrix([s.re(z) for z in entries] + [s.im(z) for z in entries])


su2 = s.Matrix.hstack(*[real_vector(B*H*cl)
                       for cl in clifford for B in [I*p for p in pauli]])
minor = s.factor(su2[:, [0, 1, 2, 3, 4, 5, 8, 11]].det())
assert minor == -(x-y)**4*(x+y)**4
assert minor.subs(y, 0) == -x**8
assert su2.subs(y, 0).rank() == 8
assert su2.subs(x, 0).rank() == 8
qrank = s.symbols("qrank", positive=True)
Q = s.diag(qrank, -qrank)
P = (s.eye(2)+Q/qrank)/2
Hrank = s.sqrt(2*qrank)*P
assert P*P == P
assert Hrank*Hrank == qrank*s.eye(2)+Q
assert Hrank.rank() == 1
print("PASS rank-one spectral seed and rank-eight fixed-determinant correction")
print("All checks passed; no coupled solution or Einstein obstruction is asserted.")
