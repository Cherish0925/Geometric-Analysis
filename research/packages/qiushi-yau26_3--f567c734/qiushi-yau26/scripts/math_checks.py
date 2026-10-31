"""Bounded, standalone mathematical checks for the published Yau 26 papers.

Symbolic identities are checked with exact SymPy arithmetic. Numerical fixture
regressions are explicitly distinct from recomputing a spectral operator.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import json
import math

import numpy as np
import sympy as sp


class CheckFailure(RuntimeError):
    """A required mathematical identity or regression did not pass."""


def require(condition, message):
    # Deliberately not assert: checks must remain active under python -O.
    if not bool(condition):
        raise CheckFailure(message)


def zero(expression, label):
    residual = sp.simplify(sp.expand(expression))
    require(residual == 0, f"{label}: residual {residual}")


def matrix_equal(actual, expected, label):
    require(actual.shape == expected.shape, f"{label}: shape mismatch")
    for i in range(actual.rows):
        for j in range(actual.cols):
            zero(actual[i, j] - expected[i, j], f"{label}[{i},{j}]")


def rejected(label, operation):
    try:
        operation()
    except CheckFailure:
        return {"mutation": label, "rejected": True}
    raise CheckFailure(f"Negative control was not rejected: {label}")


def uniform_gap():
    """Check algebra used by the proof, without claiming a numerical gamma."""
    s, u, b = sp.symbols("s u b", real=True)
    f = 2*s/3 - 2*sp.sqrt(sp.Rational(2, 3))*u
    integral_density = s*s/24 + 2*u*u
    zero(27*integral_density - (s-sp.sqrt(6)*u)**2
         - (s+8*sp.sqrt(6)*u)**2/8, "LeBrun square completion")
    zero((s+8*sp.sqrt(6)*u)**2 + 18*(f*f-b*b)
         - 216*integral_density + 18*b*b, "joint calibration")
    P, Z = sp.symbols("P Z", nonnegative=True)
    Q = P + Z/4
    zero(109*Q - (Q+Z+108*P) - 26*Z, "109 coefficient slack")
    require(109*4 == 436, "pointwise Ricci defect coefficient")
    require(sp.Rational(864*25, 32) == 675, "normalized topology coefficient")
    noether_ratio = 5 + 36 + sp.Rational(1, 3)
    require(noether_ratio == sp.Rational(124, 3) < 42, "Noether L=42")
    eigenvalues = [sp.Rational(-1, 6), sp.Rational(1, 12), sp.Rational(1, 12)]
    zero(sum(eigenvalues), "forbidden Weyl trace")
    zero(sum(t*t for t in eigenvalues)-sp.Rational(1, 24), "forbidden Weyl norm")
    zero(sp.prod(eigenvalues)+sp.Rational(1, 864), "forbidden Weyl determinant")
    require(sp.Rational(1, 24) != sp.Rational(16, 24), "Kahler norm mismatch")
    # Independent closed-form simplification of the older explicit SW bound.
    A, p, delta = sp.symbols("A p delta", positive=True)
    q = A*(p-sp.Rational(1, 3))
    T = A*(1-p)
    numerator = 2*T*delta**2 - q*(sp.Rational(2, 3)*(1-delta)**2-2*delta**2)
    zero(numerator-sp.Rational(2, 3)*A*(2*delta**2
         -(p-sp.Rational(1, 3))*(1-delta)**2), "SW ratio elimination")
    zero(sp.Rational(1, 3)-(p-sp.Rational(1, 3))/2-(1-p)/2,
         "nonpositive-denominator branch already implies the weaker threshold")
    controls = [rejected("calibration 18 replaced by 17", lambda: zero(
        (s+8*sp.sqrt(6)*u)**2+17*(f*f-b*b)
        -216*integral_density+18*b*b, "mutated calibration"))]
    return {
        "scope": "exact finite algebra and constants; not the analytic compactness proof or a computed gamma",
        "provenance": ["verify_deficit_constants.py", "research/20260916_uniform_gap.tex: calibration, density budget, Noether application",
                       "research/20260912.tex: Seiberg--Witten error window"],
        "checked": ["27 square completion", "216/18 joint calibration", "109 Q bound with nonnegative 26 Z slack",
                    "436 and 675 normalized coefficients", "chi/A <= 124/3 < 42",
                    "forbidden Weyl trace, norm and determinant", "explicit SW ratio algebra"],
        "conditions": {"Einstein_gap": "MP(A), chi <= L A; analytic proof in paper; gamma is non-explicit",
                       "blowup_application": "closed minimal general-type complex surface, b_plus > 1, A=c1^2 positive integer, k>=0",
                       "SW_ratio_formula": "1/3 < p=k/A < 1 and 0<=delta_minus<1; conclusion delta_minus/(1-delta_minus)>=sqrt((p-1/3)/2). If (2/3)(1-delta)^2-2delta^2<=0, the stronger ratio bound 1/sqrt(3) applies directly."},
        "constants": {"density_Q": 109, "delta_squared": 436, "topology_d": 675, "relative_Euler_L": 42},
        "negative_controls": controls,
    }


def twoform(pairs):
    result = sp.zeros(4)
    for i, j, sign in pairs:
        result[i, j] = sign
        result[j, i] = -sign
    return result


def weyl10():
    """Construct and differentiate every Weyl direction, not one sample mode."""
    x = sp.symbols("x0:4", real=True)
    R = sum(t*t for t in x)
    eta, eta_R, eta_RR = sp.symbols("eta eta_R eta_RR", real=True)
    diagonal = [("diag_1_-1_0", sp.diag(1, -1, 0)),
                ("diag_1_1_-2", sp.diag(1, 1, -2))]
    for a, b in [(0, 1), (0, 2), (1, 2)]:
        block = sp.zeros(3)
        block[a, b] = block[b, a] = 1
        diagonal.append((f"off_{a}{b}", block))
    rows, flattened = [], []
    for chirality, sign in [("W_plus", 1), ("W_minus", -1)]:
        forms = [twoform([(0, 1, 1), (2, 3, sign)]),
                 twoform([(0, 2, 1), (3, 1, sign)]),
                 twoform([(0, 3, 1), (1, 2, sign)])]
        for name, block in diagonal:
            C = {(i, j, k, l): sp.Rational(1, 4)*sum(
                block[a, b]*forms[a][i, j]*forms[b][k, l]
                for a, b in product(range(3), repeat=2))
                for i, j, k, l in product(range(4), repeat=4)}
            flattened.append(sp.Matrix(list(C.values())))
            for i, j, k, l in product(range(4), repeat=4):
                require(C[i, j, k, l] == -C[j, i, k, l], "Weyl first antisymmetry")
                require(C[i, j, k, l] == C[k, l, i, j], "Weyl pair symmetry")
                require(C[i, j, k, l]+C[i, k, l, j]+C[i, l, j, k] == 0, "Weyl Bianchi")
            for i, j in product(range(4), repeat=2):
                require(sum(C[k, i, k, j] for k in range(4)) == 0, "Weyl Ricci trace")
            K = sp.Matrix(4, 4, lambda i, j: sp.expand(-sp.Rational(1, 3)*sum(
                C[i, k, j, l]*x[k]*x[l] for k, l in product(range(4), repeat=2))))
            require(any(v != 0 for v in K), "nonzero Weyl direction")
            zero(sp.trace(K), "trace K")
            for i in range(4):
                zero(sum(K[i, j]*x[j] for j in range(4)), "radial gauge")
                zero(sum(sp.diff(K[j, i], x[j]) for j in range(4)), "divergence K")
            for entry in K:
                zero(sum(sp.diff(entry, t, 2) for t in x), "harmonic K")

            # Compute every second derivative of h=eta(R) K, R=|x|^2.
            # eta, eta_R, eta_RR are independent radial jets. This avoids
            # singular fractional powers and checks an arbitrary radial profile.
            def d2(i, j, a, b):
                return ((2*int(a == b)*eta_R+4*x[a]*x[b]*eta_RR)*K[i, j]
                        + 2*x[a]*eta_R*sp.diff(K[i, j], x[b])
                        + 2*x[b]*eta_R*sp.diff(K[i, j], x[a])
                        + eta*sp.diff(K[i, j], x[a], x[b]))

            DR = sp.Matrix(4, 4, lambda i, j: sp.expand(sp.Rational(1, 2)*sum(
                d2(k, j, k, i)+d2(k, i, k, j)-d2(i, j, k, k)-d2(k, k, i, j)
                for k in range(4))))
            matrix_equal(DR, -(2*R*eta_RR+8*eta_R)*K, "full radial DRic")
            matrix_equal(DR.subs({eta: 1, eta_R: 0, eta_RR: 0}), sp.zeros(4), "DRic K")
            for p in [1, 2, -1]:
                exponent = sp.Rational(p, 2)
                coefficient = -(2*R*exponent*(exponent-1)*R**(exponent-2)
                                + 8*exponent*R**(exponent-1))
                zero(coefficient+sp.Rational(p*p+6*p, 2)*R**(exponent-1), "r^p coefficient")
            rows.append({"chirality": chirality, "mode": name, "status": "passed",
                         "nonzero_K_entries": sum(v != 0 for v in K)})
    require(sp.Matrix.hstack(*flattened).rank() == 10, "ten independent Weyl tensors")
    controls = [rejected("radial first-derivative coefficient 8 replaced by 7", lambda:
                         matrix_equal(DR, -(2*R*eta_RR+7*eta_R)*K, "mutated radial identity"))]
    return {
        "scope": "exact symbolic curvature symmetries and linearized Ricci on all 10 Weyl directions, with arbitrary radial jets",
        "provenance": ["step83_full_weyl_log_annulus_audit.py", "research/20260916_construction.tex: full Weyl log interpolation"],
        "normalization": "orientation 0123; unnormalized self/anti-self-dual two-forms; C=sum A_ab omega_a tensor omega_b /4; K_ij=-C_ikjl xk xl/3",
        "basis_rank": 10,
        "radial_identity": "DRic_e[eta(log r) K]=-(eta_tt+6 eta_t) K/(2 r^2), r>0",
        "checks_per_direction": ["curvature symmetries and Bianchi", "Ricci trace zero", "trace/divergence/Laplacian/radial gauge of K zero",
                                 "DRic K zero", "arbitrary eta(|x|^2) radial identity", "p=1,2,-1 coefficients"],
        "directions": rows,
        "limits": "Does not estimate nonlinear gluing remainders, solve the ALE core equation, or prove global coverage.",
        "negative_controls": controls,
    }


def frame_curvature(brackets, derivative, n=4):
    """Koszul connection and full curvature from [e_i,e_j]=c_ij^k e_k.

    R[i,j,k,l]=<R(e_i,e_j)e_k,e_l>; sphere sectional curvature is
    R[i,j,j,i]>0. Ric[j,k]=sum_i R[i,j,k,i].
    """
    def c(i, j, k):
        return brackets.get((i, j, k), sp.S.Zero)

    connection = {(i, j, k): (c(i, j, k)-c(j, k, i)+c(k, i, j))/2
                  for i, j, k in product(range(n), repeat=3)}
    curvature = {}
    for i, j, k, l in product(range(n), repeat=4):
        value = derivative(i, connection[j, k, l])-derivative(j, connection[i, k, l])
        value += sum(connection[j, k, m]*connection[i, m, l]
                     - connection[i, k, m]*connection[j, m, l]
                     - c(i, j, m)*connection[m, k, l] for m in range(n))
        curvature[i, j, k, l] = sp.expand(value)
    ricci = sp.Matrix(n, n, lambda j, k: sp.expand(sum(curvature[i, j, k, i] for i in range(n))))
    matrix_equal(ricci, ricci.T, "Ricci symmetry from Koszul computation")
    return ricci, curvature


def brackets_from_structure(entries):
    # de^k = coefficient * e^i wedge e^j implies c_ij^k=-coefficient.
    result = {}
    for k, i, j, coefficient in entries:
        result[i, j, k] = -sp.sympify(coefficient)
        result[j, i, k] = sp.sympify(coefficient)
    return result


def ed_ricci():
    j, k, v, vt, vu = sp.symbols("j k v v_t v_u", real=True)
    derivative_table = [{k: 1-k*k, v: vt}, {}, {j: 1-j*j, v: vu}, {}]

    def derivative(a, expression):
        return sum(sp.diff(expression, symbol)*value for symbol, value in derivative_table[a].items())

    brackets = brackets_from_structure([(1, 0, 1, k), (3, 2, 3, j), (3, 0, 2, v)])
    ricci, curvature = frame_curvature(brackets, derivative)
    expected = sp.Matrix([[-v*v/2, 0, 0, (vu+2*j*v)/2],
                          [0, 0, 0, 0], [0, 0, -v*v/2, -(vt+k*v)/2],
                          [(vu+2*j*v)/2, 0, -(vt+k*v)/2, v*v/2]])
    matrix_equal(ricci+sp.eye(4), expected, "ED complete Ricci defect")
    zero(sp.trace(ricci)+4+v*v/2, "ED scalar curvature")
    zero(curvature[0, 3, 3, 0]-v*v/4, "positive mixed sectional curvature")
    matrix_equal(ricci.subs({v: 0, vt: 0, vu: 0}), -sp.eye(4), "hyperbolic product baseline")
    # The non-diagonal matrix is a two-edge symmetric star; verify its full
    # characteristic polynomial rather than checking only diagonal entries.
    alpha, beta = sp.symbols("alpha beta", real=True)
    # SymPy's charpoly generator has no assumptions; use that same symbol.
    lam = sp.Symbol("lam")
    star = sp.Matrix([[0, 0, 0, alpha], [0, 0, 0, 0], [0, 0, 0, beta], [alpha, 0, beta, 0]])
    zero(star.charpoly(lam).as_expr()-lam**2*(lam**2-alpha**2-beta**2), "ED off-diagonal spectrum")
    controls = [rejected("omit ED 03 mixed component", lambda: zero(expected[0, 3], "mutated ED mixed block")),
                rejected("omit moving-frame quadratic term", lambda: zero((ricci+sp.eye(4))[3, 3], "mutated ED diagonal"))]
    return {
        "scope": "independent exact full Ricci tensor from noncoordinate structure equations via Koszul and curvature contraction",
        "provenance": ["research/20260912.tex: BUN:shape, BUN:ricci-matrix, BUN:slow-bound",
                       "research/20260916_global.tex: bundleRicci"],
        "metric": "dt^2+b(t)^2 dtheta^2+du^2+a(u)^2(ds+z(t) zeta'(u)du)^2",
        "structure_equations": ["de1=k e0 wedge e1", "de3=j e2 wedge e3+v e0 wedge e2"],
        "parameters": "j=tanh u, k=tanh t, v=a zeta' z'; j_u=1-j^2, k_t=1-k^2; v_t and v_u independent jets",
        "ricci_plus_metric": [[str(entry) for entry in expected.row(i)] for i in range(4)],
        "scalar_curvature": str(sp.trace(ricci)),
        "off_diagonal_characteristic_polynomial": "lambda^2 (lambda^2-alpha^2-beta^2)",
        "limits": "Local tensor identity and norm algebra; not a computer proof of the closed bundle gluing, derivative bounds, or Einstein nonexistence.",
        "negative_controls": controls,
    }


def cz_spike():
    X, Y = sp.symbols("X Y", real=True)
    sigma = sp.symbols("sigma", positive=True)
    R = X*X+Y*Y
    w = -X*Y*sp.log(R+sigma*sigma)/2
    derivatives = {"wx": sp.diff(w, X), "wy": sp.diff(w, Y), "wxx": sp.diff(w, X, 2),
                   "wyy": sp.diff(w, Y, 2), "wxy": sp.diff(w, X, Y)}
    lap = derivatives["wxx"]+derivatives["wyy"]
    target_lap = -2*X*Y*(3*sigma*sigma+2*R)/(R+sigma*sigma)**2
    zero(lap-target_lap, "CZ Laplacian")
    zero(derivatives["wxy"].subs({X: 0, Y: 0})+sp.log(sigma), "CZ central Hessian")
    # |2XY|<=R and t=R/sigma^2 give |Delta w|<= t(3+2t)/(1+t)^2<2.
    t = sp.symbols("t", nonnegative=True)
    zero(2-t*(3+2*t)/(1+t)**2-(2+t)/(1+t)**2, "uniform Laplacian bound")

    c1, c2, ux, uy, uxx, uxy, uyy = sp.symbols("c1 c2 ux uy uxx uxy uyy", real=True)
    table = [{c1: -(1+c1*c1), ux: uxx, uy: uxy},
             {c2: -(1+c2*c2), ux: uxy, uy: uyy}, {}, {}]

    def derivative(a, expression):
        return sum(sp.diff(expression, symbol)*value for symbol, value in table[a].items())

    brackets = brackets_from_structure([(2, 0, 2, c1+ux), (2, 1, 2, uy),
                                        (3, 0, 3, -ux), (3, 1, 3, c2-uy)])
    ricci, curvature = frame_curvature(brackets, derivative)
    expected = sp.Matrix([
        [-2*c1*ux-2*ux*ux, -c1*uy+c2*ux-2*ux*uy, 0, 0],
        [-c1*uy+c2*ux-2*ux*uy, 2*c2*uy-2*uy*uy, 0, 0],
        [0, 0, -uxx-uyy-c1*ux-c2*uy, 0],
        [0, 0, 0, uxx+uyy+c1*ux+c2*uy]])
    matrix_equal(ricci-sp.eye(4), expected, "CZ full Ricci defect")
    zero(curvature[0, 2, 2, 1]+uxy+(c1+ux)*uy, "CZ mixed curvature detects Hessian")
    center = {c1: 0, c2: 0, ux: 0, uy: 0, uxx: 0, uyy: 0}
    matrix_equal(ricci.subs(center), sp.eye(4), "CZ central Ricci exact")
    rm_center_squared = sp.expand(sum(entry.subs(center)**2 for entry in curvature.values()))
    require(rm_center_squared.subs(uxy, 0) == 8, "S2xS2 full curvature norm baseline")
    require(sp.diff(rm_center_squared, uxy, 2) > 0, "CZ genuine Riemann spike")

    # Recompute actual derivatives on a bounded grid. These diagnostics are
    # not sup-norm certificates and do not integrate an omitted cutoff collar.
    rho = 0.30
    funcs = {name: sp.lambdify((X, Y, sigma), expression, "numpy")
             for name, expression in derivatives.items()}
    samples = []
    lambdas = [5, 10, 20, 50, 100, 200, 500]
    for L in lambdas:
        sig = math.exp(-L)
        amp = L**(-2/3)
        # Preserve the historical family parameters. At large Lambda the
        # tiny core cannot be integrated in float64: retain its exact central
        # formula separately and state the numerical integration lower radius.
        lower_radius = max(sig/10, 1e-14)
        radii = np.geomspace(lower_radius, rho/2, 384)
        angles = np.linspace(0, 2*math.pi, 64, endpoint=False)
        rr, aa = np.meshgrid(radii, angles, indexing="ij")
        xx, yy = rr*np.cos(aa), rr*np.sin(aa)
        values = {name: fn(xx, yy, sig) for name, fn in funcs.items()}
        hess2 = amp*amp*(values["wxx"]**2+values["wyy"]**2+2*values["wxy"]**2)
        integral = float(np.trapezoid(hess2.mean(axis=1)*2*math.pi*radii, radii))
        require(math.isfinite(integral) and integral > 0, "CZ finite inner Hessian diagnostic")
        samples.append({"Lambda": L, "sigma": sig, "amplitude": amp,
                        "numerical_lower_radius": lower_radius,
                        "central_u_xy_exact": amp*L,
                        "central_Rm_full_squared": float(rm_center_squared.subs(uxy, amp*L)),
                        "sampled_inner_Hessian_energy_2d": integral,
                        "sampled_inner_laplacian_max": float(np.max(np.abs(values["wxx"]+values["wyy"])))})
    full_baseline_energy = 32*sp.pi**2*4
    zero(full_baseline_energy-8*(4*sp.pi)**2, "closed background curvature energy")
    controls = [rejected("mixed Hessian sign error", lambda: zero(
        derivatives["wxy"].subs({X: 0, Y: 0})-sp.log(sigma), "mutated mixed derivative")),
        rejected("closed full curvature energy claimed zero", lambda: zero(full_baseline_energy, "mutated background energy"))]
    return {
        "scope": "exact spike derivatives and independent complete Ricci/Riemann frame algebra; bounded numerical inner-disk diagnostics",
        "provenance": ["step11_cz_spike_analytical.py (derivative family only; corrected background-energy claim)",
                       "research/20260916_construction.tex: small Ricci defect and full-curvature spikes"],
        "parameters": {"rho": rho, "Lambda": lambdas, "amplitude": "Lambda^(-2/3)",
                       "sigma": "exp(-Lambda)", "radial_points": 384, "angular_points": 64,
                       "adaptation": "Historical rho and Lambda family retained; a reduced inner-disk grid replaces the old cutoff grid. Numerical lower radius is max(sigma/10,1e-14); omitted core is not included in the sampled integral."},
        "laplacian": str(sp.factor(lap)), "central_Rm_full_squared": str(rm_center_squared),
        "central_u_xy_exact_formula": "Lambda^(1/3), for sigma=exp(-Lambda) and amplitude=Lambda^(-2/3)",
        "ricci_hessian_cancellation": "all base Hessian entries cancel; fibers retain only +/-Delta u; u_xy remains in Riemann",
        "volume_density": "exp(F1+u+F2-u)=exp(F1+F2), so the perturbation preserves the local volume density",
        "background_energy": {"norm": "full four-index curvature tensor", "chi_S2xS2": 4,
                              "exact_closed_identity": "integral |Rm|_full^2 = 128*pi^2 + 4 integral |Ric^circ|^2 >= 128*pi^2",
                              "fixed_ball": "fixed-radius background energy remains; small perturbation energy is not vanishing full energy"},
        "samples": samples,
        "limits": "Grid values are not global sup bounds or interval certificates; no cutoff-collar energy is claimed here. This is not a Yau 26 counterexample.",
        "negative_controls": controls,
    }


def four_node(mutation=None):
    fixture_path = Path(__file__).with_name("data") / "four_node_fixture.json"
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    q = sp.Rational(fixture["adjacent_matrix_q"])
    K = sp.Matrix([[sp.Rational(x) for x in row] for row in fixture["compact_combined"]])
    if mutation == "four-node-zero":
        K = sp.zeros(3)
    source = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2), 0],
                        [sp.Rational(1, 2), -sp.Rational(1, 2), 0], [0, 0, 1]])
    receiver = sp.Matrix([[1, 1, 0], [1, -1, 0], [0, 0, 2]])

    def coefficients(kernel, source_transform=source):
        tda = receiver*kernel*source_transform
        P = (tda[1, 1]+tda[2, 2]+sp.I*(tda[2, 1]-tda[1, 2]))/4
        Q = (tda[1, 1]-tda[2, 2]+sp.I*(tda[2, 1]+tda[1, 2]))/4
        return tda, sp.simplify(P), sp.simplify(Q)

    def validate(kernel, source_transform=source):
        tda, P, Q = coefficients(kernel, source_transform)
        matrix_equal(tda, sp.diag(0, 2*q, -2*q), "four-node trace/double-angle fixture")
        zero(P, "holomorphic coefficient")
        zero(Q-q, "antiholomorphic coefficient")
        return tda, P, Q

    tda, P, Q = validate(K)
    isotropic = K*sp.Matrix([1, 1, 0])
    traceless = K*sp.Matrix([1, -1, 0])
    offdiag = K*sp.Matrix([0, 0, 2])  # physical offdiagonal matrix entry is 1.
    matrix_equal(isotropic, sp.zeros(3, 1), "isotropic source must vanish")
    matrix_equal(traceless, sp.Matrix([2*q, -2*q, 0]), "traceless diagonal source")
    matrix_equal(offdiag, sp.Matrix([0, 0, -2*q]), "physical offdiagonal source")
    require(any(v != 0 for v in traceless), "traceless source must not vanish")
    old_tl_cos = (isotropic[0]-isotropic[1])/2
    old_tl_sin = isotropic[2]
    old_tl_mag = sp.sqrt(old_tl_cos**2+old_tl_sin**2)
    zero(old_tl_mag, "historical isotropic-source extractor returns zero")
    bad_offdiag = source.copy()
    bad_offdiag[2, 2] = sp.Rational(1, 2)
    wrong_sign = K.copy()
    wrong_sign[2, 2] = q
    controls = [rejected("old isotropic-source estimator used as q", lambda: zero(old_tl_mag-q, "old extractor")),
                rejected("all-zero response matrix", lambda: validate(sp.zeros(3))),
                rejected("omit doubled source offdiagonal contraction", lambda: validate(K, bad_offdiag)),
                rejected("flip offdiagonal response sign", lambda: validate(wrong_sign))]

    a = sp.Rational(fixture["pattern_coefficients"]["c_adj"])
    b = -sp.Rational(fixture["pattern_coefficients"]["c_diag"])
    qa = sp.Rational(fixture["pattern_coefficients"]["q_adj"])
    require(a > b > 0 and qa > 0, "four-node coefficient signs")
    adjacent = {frozenset(pair) for pair in [(1, 2), (1, 3), (2, 4), (3, 4)]}
    patterns = [("r0_compatible", [1, 1, 1, 1]), ("r1_one_reversed", [1, 1, 1, -1]),
                ("r2_diagonal_balanced", [1, -1, -1, 1]),
                ("r2_adjacent_balanced", [1, 1, -1, -1]), ("r3_three_reversed", [1, -1, -1, -1])]
    pattern_results = []
    for name, signs in patterns:
        equations = {str(j): [{"source": i, "kind": "adjacent" if frozenset((i, j)) in adjacent else "diagonal"}
                             for i in range(1, 5) if i != j and signs[i-1] != signs[j-1]] for j in range(1, 5)}
        if name == "r0_compatible":
            require(all(not entries for entries in equations.values()), "all-compatible source graph")
            detail = {"result": "no opposite-chirality source constraint; no existence conclusion"}
        elif name == "r2_adjacent_balanced":
            interval = [(a-qa)/b, (a+qa)/b]
            reciprocal = [1/interval[1], 1/interval[0]]
            require(reciprocal[1] < interval[0], "reciprocal windows must be disjoint for fixture")
            detail = {"result": "fixture necessary windows disjoint when q_diag=0",
                      "margin": float(a-b-qa), "window": list(map(float, interval)),
                      "reciprocal_window": list(map(float, reciprocal))}
        else:
            witnesses = [node for node, entries in equations.items() if entries and all(e["kind"] == "adjacent" for e in entries)]
            require(witnesses and a > qa, "adjacent-only positive margin witness")
            detail = {"result": "fixture violates adjacent-only necessary inequality", "margin": float(a-qa), "witness_nodes": witnesses}
        pattern_results.append({"pattern": name, "signs": signs, "receiver_sources": equations, **detail})
    return {
        "scope": "regression of a published truncated numerical matrix plus exact polarization and pattern arithmetic; no spectral recomputation",
        "provenance": fixture["provenance"],
        "normalization": "physical source S has coordinates (x,y,z)=(S22+S33,S22-S33,2*S23). Compact K contracts (S22,S33,2*S23); output is (R22,R33,R23). Receiver coordinates are (X,Y,Z)=(R22+R33,R22-R33,2*R23), zeta=(Y+iZ)/2, w=y+i*z.",
        "fixture_parameters": fixture["spectral_parameters"],
        "compact_matrix": [[str(x) for x in K.row(i)] for i in range(3)],
        "trace_double_angle_matrix": [[str(x) for x in tda.row(i)] for i in range(3)],
        "isotropic_response": list(map(str, isotropic)),
        "old_extractor_tl_mag": str(old_tl_mag),
        "unnormalized_traceless_response": list(map(str, traceless)),
        "physical_offdiagonal_response": list(map(str, offdiag)),
        "P": str(P), "Q": str(Q), "Q_float": float(Q),
        "pattern_assumption": "q_diag=0 in the specified inter-node AA/BB channel; not measured by this fixture and not full geometric reduction",
        "pattern_coefficients": fixture["pattern_coefficients"], "patterns": pattern_results,
        "pattern_symmetry": "The five rows retain r0,r1,r2-diagonal,r2-adjacent,r3 relative to a fixed positive background; r4 is not listed and global reversal is not taken as a geometric equivalence. Only at the opposite-source-graph level, both all-equal assignments have empty graphs and r1/r3 are isomorphic under square symmetry. This does not identify fillings or full equations.",
        "limits": "Rounded fixture decimals are exact regression inputs, not exact spectral coefficients. No tail bound, discretization certificate, full nonlinear reduction, or global Einstein obstruction is asserted.",
        "negative_controls": controls,
    }
