#!/usr/bin/env python3
r"""Exact angular pairing and L2 normalization for an Eguchi--Hanson insertion.

Run with Python 3 and SymPy::

    python3 research/computations/eguchi_hanson_pairing.py

All coefficients are computed over the rationals, with exact sphere moments.
The output is mathematical data in JSON; this script writes no files.

Conventions
-----------
The Cartesian orientation is dx0 ^ dx1 ^ dx2 ^ dx3.  The matrices L_i^+
represent self-dual two-forms omega_i with exterior norm squared 2; hence
zeta_i = omega_i / sqrt(2) is an orthonormal basis.  The curvature operator
has blocks [[W+ + s I/12, B], [B.T, W- + s I/12]], with arbitrary symmetric
trace-free W+, W- and arbitrary B.  Its normal-coordinate metric jet is
h2_ij = -R_iajb x_a x_b / 3.

At infinity, Omega = -d(<L_1^+ x, dx>/r^4)/2 is anti-self-dual, and the
symmetric tensors o_i = Omega composed with omega_i are transverse and
trace-free.  We compute the flat linearized-Ricci pairing of phi(r) h2
with every o_i.  After angular integration its radial density is
c0 phi/r + c1 phi' + c2 r phi''.  Here phi is zero near the origin and one
near infinity.  The Z2 quotient gives the flux (c1 - c2)/2 when c0 = 0.
This is the flux calculation for the unit-scale EH model.  At insertion
scale a, the rescaled perturbation carries an additional factor a^2.

For the radial norm calculation use d sigma_i = -sigma_j ^ sigma_k,
f = 1-a^4/r^4, e0=dr/sqrt(f), e1=r sigma1/2, e2=r sigma2/2,
e3=r sqrt(f) sigma3/2.  The form -d(sigma3/r^2)/4 is self-dual in e0123;
reverse that orientation to obtain the hyperkahler orientation, in which
it is anti-self-dual.  Its potential is defined off the bolt only: the
complete harmonic form is not globally exact.  Matrix norms are the
endomorphism/Hilbert--Schmidt norms (twice the squared exterior norm).

The computation establishes the flux coefficient, cancellation of W- and
mixed curvature blocks, and the cokernel Gram matrix.  Geometric extension
and desingularization hypotheses are stated in CURVATURE_VARIATION.md §6.5.
"""

from functools import lru_cache
import json

import sympy as sp


X = sp.symbols("x0:4", real=True)
R2 = sum(x * x for x in X)


def two_form(i, j):
    """Skew matrix of dx_i wedge dx_j."""
    matrix = sp.zeros(4)
    matrix[i, j], matrix[j, i] = 1, -1
    return matrix


LP = (
    two_form(0, 1) + two_form(2, 3),
    two_form(0, 2) - two_form(1, 3),
    two_form(0, 3) + two_form(1, 2),
)
LM = (
    two_form(0, 1) - two_form(2, 3),
    two_form(0, 2) + two_form(1, 3),
    two_form(0, 3) - two_form(1, 2),
)


def contraction(left, right):
    return sum(a * b for a, b in zip(left, right))


@lru_cache(maxsize=None)
def sphere_moment(powers):
    """Integral of x**powers over the unit S3, with its area measure."""
    if any(n % 2 for n in powers):
        return sp.S.Zero
    return sp.simplify(
        2 * sp.prod(sp.gamma(sp.Rational(n + 1, 2)) for n in powers)
        / sp.gamma(sp.Rational(sum(powers) + 4, 2))
    )


def sphere_integral(polynomial):
    return sp.factor(sum(
        coefficient * sphere_moment(powers)
        for powers, coefficient in sp.Poly(sp.expand(polynomial), *X).terms()
    ))


def trace_free_matrix(prefix):
    a, b, c, d, e = sp.symbols(f"{prefix}11 {prefix}12 {prefix}13 {prefix}22 {prefix}23")
    return sp.Matrix([[a, b, c], [b, d, e], [c, e, -a - d]])


def curvature_jet(wplus, wminus, scalar, mixed):
    """h2 = -R_iajb x_a x_b / 3 for all 20 algebraic curvature components."""
    operator = (wplus + scalar * sp.eye(3) / 12).row_join(mixed).col_join(
        mixed.T.row_join(wminus + scalar * sp.eye(3) / 12)
    )
    # L_i/sqrt(2) is orthonormal on two-forms, yielding the factor 1/6.
    columns = sp.Matrix.hstack(*(form * sp.Matrix(X) for form in LP + LM))
    return (-columns * operator * columns.T / 6).applyfunc(sp.expand)


def ricci_with_radial_cutoff_on_sphere(jet):
    """DRic_flat[phi(r) h2] at r=1, retaining phi, phi', phi'' separately.

    Evaluation at r=1 happens after the radial product rule.  The resulting
    expression is polynomial in X; no rational denominator is discarded.
    """
    p0, p1, p2 = sp.symbols("phi phi_prime phi_second")

    @lru_cache(maxsize=None)
    def second(i, j, k, ell):
        radial_hessian = p2 * X[k] * X[ell] + p1 * (
            sp.KroneckerDelta(k, ell) - X[k] * X[ell]
        )
        return (
            radial_hessian * jet[i, j]
            + p1 * X[k] * sp.diff(jet[i, j], X[ell])
            + p1 * X[ell] * sp.diff(jet[i, j], X[k])
            + p0 * sp.diff(jet[i, j], X[k], X[ell])
        )

    ricci = sp.Matrix(4, 4, lambda i, j: sp.expand(sum(
        second(j, k, k, i) + second(i, k, k, j)
        - second(i, j, k, k) - second(k, k, i, j)
        for k in range(4)
    ) / 2))
    return ricci, (p0, p1, p2)


def flat_modes():
    x = sp.Matrix(X)
    theta = LP[0] * x
    omega = sp.Matrix(4, 4, lambda i, j: sp.factor(
        -(sp.diff(theta[j] / R2**2, X[i])
          - sp.diff(theta[i] / R2**2, X[j])) / 2
    ))
    modes = tuple((omega * form).applyfunc(sp.factor) for form in LP)
    # The same differentiated expression evaluated on r=1 is polynomial.
    omega_unit = LP[0] + 2 * (x * theta.T - theta * x.T)
    unit_modes = tuple(omega_unit * form for form in LP)
    identities = {
        "self_dual_components": [sp.factor(contraction(omega, form)) for form in LP],
        "symmetry_residuals": [(mode - mode.T).applyfunc(sp.factor) for mode in modes],
        "traces": [sp.factor(sp.trace(mode)) for mode in modes],
        "divergences": [sp.Matrix([
            sp.factor(sum(sp.diff(mode[i, j], X[i]) for i in range(4)))
            for j in range(4)
        ]) for mode in modes],
        "gram_times_r8": sp.Matrix(3, 3, lambda i, j: sp.factor(
            contraction(modes[i], modes[j]) * R2**4
        )),
    }
    return unit_modes, identities


def angular_pairing(unit_modes):
    wplus, wminus = trace_free_matrix("wp"), trace_free_matrix("wm")
    scalar = sp.Symbol("s")
    mixed = sp.Matrix(3, 3, sp.symbols("b0:9"))
    ricci, cutoff = ricci_with_radial_cutoff_on_sphere(
        curvature_jet(wplus, wminus, scalar, mixed)
    )
    angular = tuple(sp.Poly(sphere_integral(contraction(ricci, mode)), *cutoff)
                    for mode in unit_modes)
    coefficients = sp.Matrix(3, 3, lambda i, j: sp.factor(
        angular[i].coeff_monomial(cutoff[j])
    ))
    # Integration by parts: int phi'=1 and int r phi''=-1.
    flux = ((coefficients[:, 1] - coefficients[:, 2]) / 2).applyfunc(sp.factor)
    nuisance = sorted(wminus.free_symbols | mixed.free_symbols, key=str)
    return {
        "radial_coefficients_c0_c1_c2": coefficients,
        "flux": flux,
        "Rplus_zeta": (wplus + scalar * sp.eye(3) / 12)[:, 0],
        "flux_minus_pi_squared_Rplus_zeta": (
            flux - sp.pi**2 * (wplus + scalar * sp.eye(3) / 12)[:, 0]
        ).applyfunc(sp.factor),
        "Wminus_and_mixed_coefficients": flux.jacobian(nuisance),
        "Wminus_and_mixed_variables": nuisance,
    }


def radial_normalization():
    r, a = sp.symbols("r a", positive=True)
    f = 1 - a**4 / r**4
    # Differentiate the potential using Maurer--Cartan before changing frame.
    derivative_03 = sp.simplify((-2 / r**3) * sp.sqrt(f) * 2 / (r * sp.sqrt(f)))
    derivative_12 = sp.simplify((-1 / r**2) * (2 / r)**2)
    omega_03, omega_12 = -derivative_03 / 4, -derivative_12 / 4
    omega_matrix = omega_03 * two_form(0, 3) + omega_12 * two_form(1, 2)
    # Omega is SD in this moving-frame orientation, so parallel forms are ASD.
    # Their frame may rotate within LM; the scalar Gram matrix is unchanged.
    modes = tuple(omega_matrix * form for form in LM)
    pointwise_gram = sp.Matrix(3, 3, lambda i, j: sp.factor(contraction(modes[i], modes[j])))
    frame_volume = sp.simplify((1 / sp.sqrt(f)) * (r / 2)**2 * r * sp.sqrt(f) / 2)
    angular_volume = 8 * sphere_moment((0, 0, 0, 0)) / 2  # sigma123 on RP3
    shell = sp.simplify(frame_volume * angular_volume)
    gram = pointwise_gram.applyfunc(lambda value: sp.integrate(value * shell, (r, a, sp.oo)))
    return {
        "d_potential_coefficients_e03_e12": [derivative_03, derivative_12],
        "Omega_endomorphism_norm_squared": sp.factor(contraction(omega_matrix, omega_matrix)),
        "cokernel_pointwise_gram": pointwise_gram,
        "radial_volume_density": shell,
        "cokernel_L2_gram": gram,
    }


def encode(value):
    if isinstance(value, sp.MatrixBase):
        return [[str(entry) for entry in row] for row in value.tolist()]
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(item) for item in value]
    return str(value)


def main():
    modes, flat = flat_modes()
    pairing = angular_pairing(modes)
    norm = radial_normalization()
    # These compare derived expressions; no coefficient is used as input.
    assert pairing["radial_coefficients_c0_c1_c2"][:, 0] == sp.zeros(3, 1)
    assert pairing["flux_minus_pi_squared_Rplus_zeta"] == sp.zeros(3, 1)
    assert pairing["Wminus_and_mixed_coefficients"] == sp.zeros(3, 14)
    assert flat["self_dual_components"] == [0, 0, 0]
    assert all(matrix == sp.zeros(4) for matrix in flat["symmetry_residuals"])
    assert flat["traces"] == [0, 0, 0]
    assert all(vector == sp.zeros(4, 1) for vector in flat["divergences"])
    assert flat["gram_times_r8"] == 4 * sp.eye(3)
    print(json.dumps(encode({
        "flat_cokernel": flat,
        "angular_pairing": pairing,
        "radial_normalization": norm,
    }), indent=2))


if __name__ == "__main__":
    main()
