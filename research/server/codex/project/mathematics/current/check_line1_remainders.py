"""Exact algebra for the Sept 23 remainder notes; not a PDE verifier."""

import json
import sympy as s


def zero(expression):
    assert s.simplify(expression) == 0, expression


def main():
    pi = s.pi
    scalar, w, p, topology = s.symbols("scalar w p topology", real=True)
    density = (scalar**2 / 24 + w**2 / 12) / (4 * pi**2)
    defect = density - p / 2
    split = (w - scalar)**2 - 72 * pi**2 * p + (scalar + 2 * w)**2 / 2
    zero(144 * pi**2 * defect - split)

    # Tracefree symmetric operator, with the quadratic form on its first axis.
    a, b, u, v, z, rho = s.symbols("a b u v z rho", real=True)
    W = s.Matrix([[a, u, v], [u, b, z], [v, z, -a-b]])
    model = s.diag(-rho**2 / 4, rho**2 / 8, rho**2 / 8)
    hs2 = lambda matrix: s.trace(matrix.T * matrix)
    rhs = (w - 3 * rho**2 / 4)**2 / 6 + s.Rational(3, 4) * rho**2 * (a + w/3)
    zero(s.expand(rhs).subs(w**2, 6 * hs2(W)) - hs2(W-model))

    # Kähler Hodge identities and optimized nonzero-Einstein-ray defect.
    D, A, V, variance = s.symbols("D A V variance", positive=True)
    R = 8*pi**2*(2*p-A) + 32*pi**2*D
    P = 8*pi**2*(p-A) + 16*pi**2*D
    L = 64*pi**2*D
    zero((4*P+L)/R - 4*(p-A+4*D)/(2*p-A+4*D))
    zero(R - P - (L+32*pi**2*p)/4)

    # Unequal products: exact cscK equality does not imply Einstein.
    alpha, beta, H = s.symbols("alpha beta H", positive=True)
    product_V = 16*pi**2*H/(alpha*beta)
    product_s = -2*(alpha+beta)
    product_R = 2*(alpha**2+beta**2)*product_V
    product_P = (alpha-beta)**2*product_V
    product_p = product_s**2*product_V/(32*pi**2)
    product_A = 8*H
    zero(product_P - 8*pi**2*(product_p-product_A))
    product_E = 4-product_s**2*product_V/product_R
    zero(product_E - 2*(alpha-beta)**2/(alpha**2+beta**2))
    assert product_E.subs({alpha: 1, beta: 2}) == s.Rational(2, 5)

    # Fixed blow-up topology: energy-minimizing Kähler sequences.
    base_A, k, excess = s.symbols("base_A k excess", positive=True)
    blow_R = 8*pi**2*(base_A+k)+excess
    blow_P = 8*pi**2*k+excess/2
    blow_E = (4*blow_P+variance)/blow_R
    zero(blow_E.subs({excess: 0, variance: 0}) - 4*k/(base_A+k))
    zero(blow_P - (blow_R-8*pi**2*(base_A-k))/2)

    # Exact cohomological limit for an actual cscK blow-up class.
    eps, bsum, bsquare = s.symbols("eps bsum bsquare", positive=True)
    omega_square = 4*pi**2*base_A - eps**4*bsquare
    c_omega = -2*pi*base_A - eps**2*bsum
    p_eps = c_omega**2/omega_square
    zero(s.limit(p_eps, eps, 0) - base_A)

    # Wrong coefficients and omitted terms must fail these controls.
    mutations = {
        "cscK_implies_Einstein": product_E.subs({alpha: 1, beta: 2}),
        "omit_primitive_period": product_P.subs({alpha: 1, beta: 2}),
        "omit_blowup_term": 4*k/(base_A+k),
        "wrong_Weyl_amplitude": hs2(W-model)-hs2(W-s.diag(-rho**2/2,rho**2/4,rho**2/4)),
    }
    for name, nonzero in mutations.items():
        assert s.simplify(nonzero) != 0, name
    print(json.dumps({
        "status": "pass",
        "groups": 6,
        "rejected_wrong_variants": list(mutations),
        "scope": "exact finite algebra; no PDE existence, limiting compactness or novelty certification",
    }, indent=2))


if __name__ == "__main__":
    main()
