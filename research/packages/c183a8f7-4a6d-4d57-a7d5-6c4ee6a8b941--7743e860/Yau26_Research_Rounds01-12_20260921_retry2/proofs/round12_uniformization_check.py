#!/usr/bin/env python3
"""Exact Clifford, graded-Chern and central-curvature algebra.

This checks the explicitly defined system in round12_uniformization.md.
It neither identifies that system with an unstated source convention nor
proves existence of any nonlinear monopole solution.
"""
import sympy as s

I = s.I
eye = s.eye(2)
zero = s.zeros(2)
sigma = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -I], [I, 0]]), s.diag(1, -1)]
c = [eye, -I*sigma[2], I*sigma[0], I*sigma[1]]
pairs = [(i, j) for i in range(4) for j in range(i+1, 4)]


def adj(a):
    return a.conjugate().T


def simp(a):
    return a.applyfunc(s.simplify) if isinstance(a, s.MatrixBase) else s.simplify(a)


def sd(a):
    return [simp((a[0, 1]+a[2, 3])/2),
            simp((a[0, 2]-a[1, 3])/2),
            simp((a[0, 3]+a[1, 2])/2)]


def asd(a):
    return [simp((a[0, 1]-a[2, 3])/2),
            simp((a[0, 2]+a[1, 3])/2),
            simp((a[0, 3]-a[1, 2])/2)]


def from_sd_asd(p, m):
    return {(0, 1): p[0]+m[0], (2, 3): p[0]-m[0],
            (0, 2): p[1]+m[1], (1, 3): -p[1]+m[1],
            (0, 3): p[2]+m[2], (1, 2): p[2]-m[2]}


for i in range(4):
    for j in range(4):
        assert c[i]*adj(c[j])+c[j]*adj(c[i]) == (2*eye if i == j else zero)
rho = {(i, j): -c[i]*adj(c[j]) for i, j in pairs}
assert asd(rho) == [zero]*3
assert rho[0, 1]+rho[2, 3] == -2*I*sigma[2]
print("PASS oriented Clifford representation and self-dual source action")

v = s.symbols("v0:8", real=True)
phi = s.Matrix(2, 2, [v[2*j]+I*v[2*j+1] for j in range(4)])
theta = [phi*ci for ci in c]
upper = {(i, j): adj(theta[i])*theta[j]-adj(theta[j])*theta[i] for i, j in pairs}
lower = {(i, j): theta[i]*adj(theta[j])-theta[j]*adj(theta[i]) for i, j in pairs}
Q = [-a/2 for a in sd(lower)]
for a, q in zip(sd(upper), Q):
    assert simp(a-s.trace(q)*eye) == zero
for ij in pairs:
    assert simp(s.trace(upper[ij])+s.trace(lower[ij])) == 0
print("PASS both quadratic wedge identities and full curvature-trace cancellation")

x, y = s.symbols("x y", real=True)
H = s.diag(x, y)
QH = [simp(q.subs(dict(zip(v, [x, 0, 0, 0, 0, 0, y, 0])))) for q in Q]
assert QH[0] == -I*s.diag(x*x, -y*y)
assert QH[1] == I*x*y*sigma[0]
assert QH[2] == I*x*y*sigma[1]
assert QH[1][0, 1] == I*x*y
assert simp(QH[0]-s.trace(QH[0])*eye/2+I*(x*x+y*y)*sigma[2]/2) == zero
print("PASS anisotropic quadratic map: two off-diagonal directions survive iff xy is nonzero")

unknowns = s.symbols("z0:16")
X = [s.Matrix(2, 2, unknowns[4*i:4*i+4]) for i in range(4)]
Dirac = sum((X[i]*c[i] for i in range(4)), zero)
dtheta = {(i, j): X[i]*c[j]-X[j]*c[i] for i, j in pairs}
for k, a in enumerate(asd(dtheta)):
    assert simp(a-Dirac*c[k+1]/2) == zero
equations = [entry for ij in pairs for entry in dtheta[ij]]
matrix, _ = s.linear_eq_to_matrix(equations, unknowns)
assert matrix.rank() == 16
print("PASS graded off-diagonal equation equals Dirac; full closedness forces parallel phi")

# General target rank r and block parameter lambda.  The source has rank two.
r, lam2, f, q = s.symbols("r lam2 f q", real=True)
central = f/2 + lam2*q
target_trace = 2*lam2*q + r*central
assert s.expand(target_trace-r*f/2-(r+2)*lam2*q) == 0
assert s.expand(target_trace.subs({r: 2, lam2: s.Rational(1, 2)})-f-2*q) == 0
assert s.simplify((f+target_trace)/(r+2)-central) == 0
print("PASS corrected central coefficient and rank-dependent trace equation")

# Direct algebra for a general u(2,2)-valued graded-ASD two-form.
# A basis calculation suffices because the trace and HS quadratic forms have
# no cross terms between these matrix/form basis vectors.
u2_basis = [I*eye] + [I*a for a in sigma]
complex_basis = []
for a in range(2):
    for b in range(2):
        elementary = s.zeros(2)
        elementary[a, b] = 1
        complex_basis.extend([elementary, I*elementary])
graded_basis = []
for k in range(3):
    for a in u2_basis:
        m = [s.zeros(4) for _ in range(3)]
        m[k] = s.diag(a, zero)
        graded_basis.append(from_sd_asd([s.zeros(4)]*3, m))
        m = [s.zeros(4) for _ in range(3)]
        m[k] = s.diag(zero, a)
        graded_basis.append(from_sd_asd([s.zeros(4)]*3, m))
    for a in complex_basis:
        p = [s.zeros(4) for _ in range(3)]
        p[k] = zero.row_join(adj(a)).col_join(a.row_join(zero))
        graded_basis.append(from_sd_asd(p, [s.zeros(4)]*3))


def wedge_trace(a, b):
    return s.trace(a[0, 1]*b[2, 3]+a[2, 3]*b[0, 1]
                   -a[0, 2]*b[1, 3]-a[1, 3]*b[0, 2]
                   +a[0, 3]*b[1, 2]+a[1, 2]*b[0, 3])


for a in graded_basis:
    for b in graded_basis:
        hs = sum(s.re(s.trace(adj(a[ij])*b[ij])) for ij in pairs)
        assert simp(wedge_trace(a, b)-hs) == 0
print("PASS graded-ASD u(2,2) Chern pairing is the positive Hilbert-Schmidt norm")

a2, chi, tau = s.symbols("a2 chi tau", real=True)
c2plus = (a2-2*chi-3*tau)/4
c2minus = (a2+2*chi-3*tau)/4
c2total = s.expand(c2plus+c2minus+a2)
chern_integral = s.expand(8*s.pi**2*c2total-3*s.pi**2*(4*a2))
assert chern_integral == -12*s.pi**2*tau
assert s.expand(a2-4*c2plus) == 2*chi+3*tau
print("PASS graded energy -12 pi^2 tau and parallel-line discriminant obstruction")

# Ordinary dual-spinor comparison: rho_dual(eta)=-rho_source(eta)^T.
# phi has one target row. Qtrace=-i*x²*omega, and the dual spinor is (x,0).
rho_dual_omega = -(rho[0, 1]+rho[2, 3]).T
mu = s.diag(x*x/2, -x*x/2)
assert simp(-I*x*x*rho_dual_omega-4*mu) == zero
print("PASS Qtrace = 4 q_std for rho_dual(q_std)=(psi psi*)_0")

# Constant sectional curvature k: spin curvature is -k*rho/2.
# At phi=f0 Id, both full block diagonals cancel exactly when k=-2 f0².
f0 = s.symbols("f0", positive=True)
theta_iso = [f0*ci for ci in c]
for i, j in pairs:
    rho_minus = -adj(c[i])*c[j]
    source = f0*f0*rho_minus
    target = f0*f0*rho[i, j]
    uu = (adj(theta_iso[i])*theta_iso[j]-adj(theta_iso[j])*theta_iso[i])/2
    ll = (theta_iso[i]*adj(theta_iso[j])-theta_iso[j]*adj(theta_iso[i]))/2
    assert simp(source+uu) == zero
    assert simp(target+ll) == zero
print("PASS hyperbolic model: k=-2 f0^2 gives projectively flat block connection")
print("All exact checks passed; no existence or published-system identification is assumed.")
