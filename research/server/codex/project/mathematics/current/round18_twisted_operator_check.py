#!/usr/bin/env python3
"""Independent finite checks for round18_twisted_operator.md.

These checks concern algebra, representations, and one-dimensional operators.
They do not verify uniformization, global elliptic regularity, or an IFT.
No inherited checking module is imported and no source file is modified.
"""

import json

import mpmath as mp
import sympy as s


RESULTS = []


def require(condition, description):
    if not bool(condition):
        raise AssertionError(description)


def exact(expr):
    return s.simplify(s.expand(expr)) == 0


def record(name, detail):
    RESULTS.append({"name": name, "status": "passed", "detail": detail})


# 1. Diagonal invariants include negative-times-negative channels.
V = s.diag(1, 1, -1)
W = s.diag(1, -1, -1)
action = s.kronecker_product(V, W)
reynolds = (s.eye(9) + action) / 2
require(reynolds**2 == reynolds, "Reynolds projection is not idempotent")
require(reynolds.T == reynolds, "Reynolds projection is not orthogonal")
require(reynolds.rank() == 4, "Wrong diagonal invariant dimension")
require(reynolds.rank() != 2 * 1, "Separate invariants lost the mixed parity")
require(reynolds[7, 7] == 1 and reynolds[8, 8] == 1,
        "Negative-negative invariant channels were removed")
record("diagonal_invariants", "rank 4 includes both negative-negative modes")

# 2. Each product block has the expected shift before taking invariants.
lam, nu, mu, xi = s.symbols("lambda nu mu xi", nonnegative=True)
sectors = {
    "base_TT": nu / 2,
    "fiber_TT": lam / 2,
    "base_trace": 3 + (lam + nu) / 2,
    "fiber_trace": 3 + (lam + nu) / 2,
    "base_D": 3 + (mu + nu) / 2,
    "fiber_D": 3 + (lam + xi) / 2,
    "mixed": ((mu + 3) + (xi + 3)) / 2,
}
require(exact(sectors["mixed"] - 3 - (mu + xi) / 2), "Mixed shift mismatch")
require(all(v.subs({lam: 0, nu: 0, mu: 0, xi: 0}) == 3
            for key, v in sectors.items() if "TT" not in key),
        "A false high-sector zero mode appeared")
require((3 + mu / 2).subs(mu, 0) == 3, "Harmonic gauge form became zero")
record("full_sector_shifts", "two unshifted TT channels; every other branch starts at 3")

# 3. Holomorphic quadratic forms: both infinity orders and branch parity.
w = s.symbols("w")
invariant_local = (2 * w) ** 2 / w**2
odd_local = (2 * w) ** 2 / w
require(exact(invariant_local.subs(w, -w) - invariant_local), "Even local parity")
require(exact(odd_local.subs(w, -w) + odd_local), "Odd local parity")
for genus in range(2, 10):
    even_orders = [2 * genus - 2 - j for j in range(2 * genus - 1)]
    odd_orders = [genus - 3 - j for j in range(max(0, genus - 2))]
    require(all(order >= 0 for order in even_orders + odd_orders),
            "A quadratic form has a pole at infinity")
    require(len(even_orders) + len(odd_orders) == 3 * genus - 3,
            "Quadratic differential dimension mismatch")
require((2 * (2 * 3 - 1), 2 * (3 - 2)) == (10, 2), "Genus-three split")
require(2 * (2 - 2) == 0, "Genus-two hyperelliptic anti-space is not zero")
record("hyperelliptic_quadratics", "regularity/parity counts for genera 2 through 9; genus 3 gives 10+2")

# 4. The free double-cover genus and the quotient deformation count.
base_genus, fiber_genus, degree = 2, 3, 2
cover_genus = 1 + degree * (base_genus - 1)
base_tt_total = 6 * cover_genus - 6
base_tt_plus = 6 * base_genus - 6
base_tt_minus = base_tt_total - base_tt_plus
fiber_tt_plus, fiber_tt_minus = 2 * (2 * fiber_genus - 1), 2 * (fiber_genus - 2)
require((base_tt_plus, base_tt_minus) == (6, 6), "Base parity dimensions")
kernel = base_tt_plus + fiber_tt_plus
cover_kernel = base_tt_total + fiber_tt_plus + fiber_tt_minus
require((kernel, cover_kernel) == (16, 24), "Kernel dimension mismatch")
record("invariant_kernel", "actual quotient kernel 16; covering product kernel 24")

# 5. Independent Euler, signature, and Betti bookkeeping.
euler_cover = (2 - 2 * cover_genus) * (2 - 2 * fiber_genus)
euler = euler_cover // degree
b1 = 2 * base_genus  # fiber invariant H1 vanishes under hyperelliptic involution
signature = 0
b2 = euler - 2 + 2 * b1
bplus, bminus = (b2 + signature) // 2, (b2 - signature) // 2
require((euler, b1, b2, bplus, bminus) == (8, 4, 14, 7, 7), "Topology mismatch")
require(not any((2 - 2 * p) * (2 - 2 * q) == euler and 2 * p + 2 * q == b1
                for p in range(2, 10) for q in range(2, 10)),
        "Example might have the Betti data of a hyperbolic surface product")
record("quotient_topology", "Euler 8, signature 0, b1=4, b2=14, b+=b-=7")

# 6. Cover normalization does not introduce a degree-dependent coercivity constant.
d, H, E, rhs, C = s.symbols("d H E rhs C", positive=True)
require(exact((d * E) / (d * H) - E / H), "Rayleigh quotient changes on finite cover")
require(exact(s.sqrt(d) * H / (s.sqrt(d) * rhs) - H / rhs),
        "Sobolev inverse norm changes on finite cover")
record("cover_norms", "cover degree cancels from quadratic and inverse ratios")

# 7. Smooth equivariant disk sections obey more than value-zero at the cone point.
x, y = s.symbols("x y")
odd_polynomial = x + 2 * y + x**3 - x * y**2
fake_odd = x**2 + y**2
require(exact(odd_polynomial.subs({x: -x, y: -y}, simultaneous=True) + odd_polynomial),
        "Odd equivariant polynomial does not transform correctly")
require(fake_odd.subs({x: 0, y: 0}) == 0, "Negative control must vanish at origin")
require(not exact(fake_odd.subs({x: -x, y: -y}, simultaneous=True) + fake_odd),
        "Value zero incorrectly accepted as full orbifold parity")
record("orbifold_domain", "odd jets retained; vanishing even negative control rejected")

# 8. Exact conjugation, derived from an arbitrary radial density first.
t = s.symbols("t", real=True)
a = s.Function("a", positive=True)(t)
v = s.Function("v")(t)
m = s.symbols("m", real=True)
u = v / s.sqrt(a)
conjugated = s.sqrt(a) * (-s.diff(u, t, 2) - s.diff(a, t) / a * s.diff(u, t)
                         + m**2 / a**2 * u)
potential = s.diff(a, t, 2) / (2 * a) - s.diff(a, t)**2 / (4 * a**2)
expected = -s.diff(v, t, 2) + (potential + m**2 / a**2) * v
require(exact(conjugated - expected), "General radial conjugation mismatch")
c, k = s.symbols("c k", positive=True)
actual_a = c * s.cosh(k * t)
actual_potential = s.diff(actual_a, t, 2) / (2 * actual_a) \
    - s.diff(actual_a, t)**2 / (4 * actual_a**2)
require(s.simplify(actual_potential - k**2 / 4 - k**2 / (4 * s.cosh(k * t)**2)) == 0,
        "Hyperbolic radial potential mismatch")
require((k**2 / 8).subs(k, s.sqrt(3)) == s.Rational(3, 8), "Wrong low cusp threshold")
record("radial_operator", "arbitrary-density conjugation; exact threshold 3/8")

# 9. Sign holonomy gives half-integer modes and the exact local angular bound.
phi = s.symbols("phi", real=True)
for n in range(-4, 5):
    omega = s.Rational(2 * n + 1, 2)
    wave = s.exp(s.I * omega * phi)
    require(s.simplify(wave.subs(phi, phi + 2 * s.pi) + wave) == 0,
            "Mode not antiperiodic")
    require(omega**2 >= s.Rational(1, 4), "Incorrect antiperiodic gap")
a0 = s.symbols("a0", positive=True)
require(exact(s.Rational(1, 2) * s.Rational(1, 4) / a0**2 - 1 / (8 * a0**2)),
        "Angular barrier coefficient mismatch")
record("sign_neck_barrier", "half-integer angular frequency; low-operator barrier 1/(8 a0^2)")

# 10. Capacity is derived from the Euler-Lagrange minimizer, not a chosen cutoff.
R = s.symbols("R", positive=True)
primitive = 2 * s.atan(s.exp(k * t)) / (k * c)
require(s.simplify((s.diff(primitive, t) - 1 / actual_a).rewrite(s.exp)) == 0,
        "Capacity primitive is not an antiderivative")
I = (4 * s.atan(s.exp(k * R)) - s.pi) / (k * c)
cap = 2 * s.pi / I
require(s.limit(cap / c, R, s.oo) == 2 * k, "Wrong complete-collar capacity coefficient")
# With fixed end radius, the numerical check only corroborates the exact limit.
mp.mp.dps = 60
kv = mp.sqrt(3)
capacity_ratios = []
for cv in [mp.mpf("1e-2"), mp.mpf("1e-4"), mp.mpf("1e-6")]:
    Rv = mp.acosh(1 / cv) / kv
    Iv = (4 * mp.atan(mp.exp(kv * Rv)) - mp.pi) / (kv * cv)
    capacity_ratios.append(2 * mp.pi / Iv / (2 * kv * cv))
require(all(capacity_ratios[j] > capacity_ratios[j + 1] > 1
            for j in range(len(capacity_ratios) - 1)), "Capacity asymptotics fail")
record("sharp_capacity", "energy 2*pi/I; at fixed end radius capacity/(2*k*c) tends to 1")

# 11. Flux transmission cancels the boundary pairing with the correct normal sign.
rho = s.diag(1, -1, -1)
um = s.Matrix(s.symbols("u0:3"))
wm = s.Matrix(s.symbols("w0:3"))
up, wp = rho * um, -rho * wm
require(exact((up.T * wp)[0] + (um.T * wm)[0]), "Boundary flux does not cancel")
wrong_wp = rho * wm
require(not exact((up.T * wrong_wp)[0] + (um.T * wm)[0]),
        "Missing outward-normal minus sign not detected")
record("transmission_flux", "orthogonal holonomy cancels boundary term; wrong normal sign rejected")

# 12. The high response must feed back into the genuine low equation.
A = s.Matrix([[4, 1], [1, 5]])
B = s.Matrix([[1, 2], [0, 1]])
D = s.Matrix([[7, 1], [1, 6]])
Cmat = B.T
fL, fH = s.Matrix([2, 3]), s.Matrix([1, -2])
Schur = A - B * D.inv() * Cmat
u_sol = Schur.inv() * (fL - B * D.inv() * fH)
v_sol = D.inv() * (fH - Cmat * u_sol)
require(A * u_sol + B * v_sol == fL, "Low Schur equation failed")
require(Cmat * u_sol + D * v_sol == fH, "High back substitution failed")
wrong_u = A.inv() * fL
wrong_v = D.inv() * (fH - Cmat * wrong_u)
require(A * wrong_u + B * wrong_v != fL, "Omitted feedback incorrectly passes")
eps = s.symbols("epsilon")
require((eps * B) * D.inv() * (eps * Cmat) == eps**2 * B * D.inv() * Cmat,
        "Feedback scaling not quadratic")
record("schur_feedback", "full block solution verified; omitted-coupling negative control rejected")

print(json.dumps({"status": "passed", "groups": len(RESULTS), "checks": RESULTS,
                  "scope": "Finite identities only; no numerical PDE or nonlinear theorem certification."},
                 indent=2, ensure_ascii=False))
