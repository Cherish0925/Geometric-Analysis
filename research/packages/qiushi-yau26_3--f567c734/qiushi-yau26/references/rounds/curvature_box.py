"""Exact Ricci-box minimization for the four-dimensional CGB integrand.

Run with: qiushi-yau26 env numeric python curvature_box.py
The calculation is an algebraic certificate, not a metric realization.
"""
from itertools import product
import json
import sympy as s


def main():
    d = s.symbols('d', nonnegative=True)
    a = s.symbols('a0:4', real=True)
    t = sum(a)
    f = s.Rational(2, 3) - t / 3 + t*t / 6 - sum(x*x for x in a) / 2
    # Ricci eigenvalues are -1+a_i. Separate concavity reduces the
    # box minimum to its vertices without a sampling assumption.
    assert all(s.diff(f, x, 2) == -s.Rational(2, 3) for x in a)
    by_count = {}
    for signs in product((-1, 1), repeat=4):
        n = signs.count(1)
        value = s.factor(f.subs(dict(zip(a, [v*d for v in signs]))))
        if n in by_count:
            assert s.expand(value - by_count[n]) == 0
        by_count[n] = value
    small = s.Rational(2, 3)*(1-d)**2
    large = s.Rational(2, 3)*(1+d)*(1-2*d)
    assert s.expand(by_count[4] - small) == 0
    assert s.expand(by_count[3] - large) == 0
    # Exact symbolic nonnegativity certification on each interval.
    # For each quadratic difference, evaluate endpoints and any critical
    # point in the interval. Rational arithmetic only.
    certificates = []
    for lo, hi, minimum in [(s.S(0), s.Rational(1, 3), small),
                             (s.Rational(1, 3), s.S(1), large)]:
        for n, v in by_count.items():
            diff = s.expand(v-minimum)
            points = [lo, hi]
            points += [q for q in s.solve(s.diff(diff, d), d)
                       if q.is_real and lo <= q <= hi]
            values = [s.simplify(diff.subs(d, q)) for q in points]
            assert all(v >= 0 for v in values), (n, lo, hi, values)
            certificates.append({'positive_vertices': n,
                'interval': [str(lo), str(hi)], 'difference': str(s.factor(diff)),
                'minimum_difference': str(min(values))})
    assert s.simplify(large.subs(d, s.Rational(1, 2))) == 0
    # Simultaneous scalar/traceless saturation cannot be freely combined.
    coarse = s.Rational(2, 3)-4*d/3-4*d*d/3
    assert s.expand(small-coarse) == 2*d*d
    kap = s.symbols('kap', positive=True)
    r1 = 3*(1-s.sqrt(1-kap))
    r2 = (s.sqrt(9+72*kap)-3)/4
    assert s.simplify(s.Rational(2,3)*(3-r1)**2 - 6*(1-kap)) == 0
    assert s.simplify(6-2*r2-s.Rational(4,3)*r2*r2 - 6*(1-kap)) == 0
    assert r1.subs(kap, s.Rational(5,9)) == r2.subs(kap, s.Rational(5,9)) == 1
    assert r2.subs(kap, 1) == s.Rational(3,2)
    print(json.dumps({'passed': True, 'normalization': 'Ric=-g+A',
        'vertex_polynomials': {str(n): str(v) for n,v in sorted(by_count.items())},
        'minimum_0_to_one_third': str(small),
        'minimum_one_third_to_one': str(large),
        'positive_for': '0 <= d < 1/2',
        'sharpness_scope': 'algebraic curvature tensors, not closed metrics',
        'connector_inverse_checks': 'PASS; two branches meet at kappa=5/9',
        'certificates': certificates}, indent=2))


if __name__ == '__main__':
    main()
