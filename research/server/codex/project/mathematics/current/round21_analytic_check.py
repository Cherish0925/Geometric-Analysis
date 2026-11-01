"""Independent finite contractions for round21_analytic.md; no PDE certification."""
from itertools import combinations
import sympy as s


def zero(expr):
    assert s.expand(expr) == 0, s.factor(expr)


# Noncommuting SO(3) connection on a trivial bundle over a flat four-torus.
# Constant sections test both the signed curvature-gradient term and F u term.
a, b, c, x, y, z = s.symbols("a b c x y z", real=True)
conn = [
    a * s.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
    b * s.Matrix([[0, 0, -1], [0, 0, 0], [1, 0, 0]]),
    c * s.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    s.zeros(3),
]
u = s.Matrix([x, y, z])
curv = [[ai * aj - aj * ai for aj in conn] for ai in conn]
hess = sum((ai * aj * u).dot(ai * aj * u) for ai in conn for aj in conn)
lap = sum((ai * ai * u for ai in conn), s.zeros(3, 1))
fg = sum((curv[i][j] * conn[j] * u).dot(conn[i] * u)
         for i in range(4) for j in range(4))
fu = sum((curv[i][j] * u).dot(curv[i][j] * u)
         for i in range(4) for j in range(4)) / 2
zero(hess - lap.dot(lap) - fg - fu)
assert s.expand(fg) != 0 and s.expand(fu) != 0
print("PASS: Hessian identity signs and coefficients on a nonabelian connection")


# Orthonormal self-dual two-forms epsilon_a = omega_a / sqrt(2).
omega = []
for pairs in [((0, 1), (2, 3)), ((0, 2), (3, 1)), ((0, 3), (1, 2))]:
    matrix = s.zeros(4)
    for i, j in pairs:
        matrix[i, j], matrix[j, i] = 1, -1
    omega.append(matrix)
rho = s.symbols("rho", positive=True)
cc = s.symbols("c0:4", real=True)
aa = s.symbols("a0:4", real=True)
bb = s.symbols("b0:4", real=True)
dpsi = [(cc[m] * omega[0] + aa[m] * omega[1] + bb[m] * omega[2])
        / s.sqrt(2) for m in range(4)]
dA = [rho * s.Matrix([
    [-cc[m] / 6, -aa[m] / 8, -bb[m] / 8],
    [-aa[m] / 8, cc[m] / 12, 0],
    [-bb[m] / 8, 0, cc[m] / 12],
]) for m in range(4)]
norm_dA = sum(v ** 2 for mat in dA for v in mat)
norm_J = 0
for j in range(4):
    for k in range(4):
        for l in range(4):
            val = sum(dA[i][v, w] * omega[v][i, j] * omega[w][k, l]
                      for i in range(4) for v in range(3) for w in range(3)) / 2
            norm_J += val ** 2
three = {}
star = s.zeros(4, 1)
for i, j, k in combinations(range(4), 3):
    val = dpsi[i][j, k] + dpsi[j][k, i] + dpsi[k][i, j]
    three[i, j, k] = val
    l = next(v for v in range(4) if v not in (i, j, k))
    star[l] = s.LeviCivita(i, j, k, l) * val
norm_dpsi = sum(v ** 2 for v in three.values())
norm_gradpsi = sum(v ** 2 for row in (cc, aa, bb) for v in row)
norm_drho = sum(v ** 2 for v in cc)
psi = rho * omega[0] / s.sqrt(2)
interior = s.Matrix([sum(cc[i] * psi[i, j] for i in range(4)) for j in range(4)])
cross = interior.dot(star)
zero(norm_dA - rho ** 2 * norm_gradpsi / 32 - rho ** 2 * norm_drho / 96)
zero(norm_dA - norm_J - rho ** 2 * (norm_gradpsi - 2 * norm_dpsi) / 64
     - rho ** 2 * norm_drho / 32 + rho * cross / 16)
print("PASS: full twelve-variable Weyl-divergence contraction")


# New pivotal pointwise coercivity: no closedness or spinor equations enter.
# Divide the homogeneous expression by rho^2 by setting rho=1, then form
# its exact symmetric coefficient matrix on all twelve derivative entries.
coercive = (64 * norm_J + s.Rational(4, 3) * 4 * rho**2 * norm_drho
            - rho**2 * (norm_gradpsi + norm_dpsi))
variables = list(cc) + list(aa) + list(bb)
matrix = s.hessian(s.expand(coercive.subs(rho, 1)), variables) / 2
eigenvalues = matrix.eigenvals()
assert sum(eigenvalues.values()) == 12
assert all(eigen.is_nonnegative is True for eigen in eigenvalues), eigenvalues
print("PASS: zero-order divergence coercivity, full twelve-variable PSD matrix:",
      eigenvalues)


# Polynomial rewriting of the integrated weighted identity, including zeros.
q, scalar, rpair, d, dq, cq = s.symbols("q scalar rpair d dq cq", real=True)
old = (-scalar * q ** 2 / 192 - q ** 3 / 384 + q * rpair / 32
       + q * d / 16 - s.Rational(5, 96) * dq / 4 + cq / 16)
new = (-scalar * q ** 2 / 192 - q ** 3 / 384 + q * rpair / 32
       + q * d / 16 - s.Rational(5, 384) * dq + cq / 16)
zero(old - new)
zero(new.subs({scalar: -4, q: 2, rpair: 0, d: 0, dq: 0, cq: 0})
     - s.Rational(1, 16))
print("PASS: polynomial weighted identity and calibrated constant 1/16")


# General calibration t: use R_old = R_t + (8t-1) A_old, not an independent
# replacement of W by its target. A_old acts on psi by -q/12.
t = s.symbols("t", real=True)
scaled = 64 * t ** 2 * new.subs({rpair: rpair - (8*t - 1) * q**2 / 12})
general = (-t**2 * scalar*q**2/3 - 4*t**3*q**3/3
           + 2*t**2*q*rpair + 4*t**2*q*d - s.Rational(5, 6)*t**2*dq
           + 4*t**2*cq)
zero(scaled - general)
zero(general.subs({scalar: -4, q: 2, rpair: 0, d: 0, dq: 0, cq: 0})
     - s.Rational(16, 3)*t**2*(1 - 2*t))
zero(general.subs(t, s.Rational(1, 8)) - new)
zero((scalar*q/3 + 4*t*q**2/3 - 2*rpair).subs(
    {scalar: -4, q: 2, rpair: 0}) - s.Rational(8, 3)*(2*t-1))
print("PASS: general-amplitude identity, both calibration branches, and Hodge endpoint")

# The same proof has scalar target 4*sigma for either Einstein sign.
for sigma in (-1, 1):
    calibrated = general.subs(
        {scalar: 4*sigma, q: 2, rpair: 0, d: 0, dq: 0, cq: 0})
    zero(calibrated + s.Rational(16, 3)*t**2*(sigma+2*t))
    endpoint = -s.Rational(sigma, 2)
    zero(calibrated.subs(t, endpoint))
    zero(-4*endpoint/3 - s.Rational(2*sigma, 3))
print("PASS: both Einstein signs and the signed Kahler calibration")
