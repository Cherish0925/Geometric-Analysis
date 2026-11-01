"""Extend: check W- and Ric0 dependence of the EH obstruction pairing.  If B_i depends only on R+(zeta),
the W-, Ric0 parts should vanish.  Test: pure W- and pure Ric0 jets."""
import sys, os, json, itertools
import sympy as sp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step59_exact_log_coefficient import riemann_from_ops, h2_field, X, Lp, Lm, r2

def mom(alpha):
    if any(a % 2 for a in alpha): return sp.Integer(0)
    return 2 * sp.prod([sp.gamma(sp.Rational(a + 1, 2)) for a in alpha]) / sp.gamma(sp.Rational(sum(alpha) + 4, 2))

I = Lp[0]
theta = I * sp.Matrix(X)
Om = sp.zeros(4, 4)
for a, b in itertools.product(range(4), repeat=2):
    Om[a, b] = sp.simplify(-sp.Rational(1, 2) * (sp.diff(theta[b] / r2 ** 2, X[a]) - sp.diff(theta[a] / r2 ** 2, X[b])))
os_ = [sp.simplify(Om * L) for L in Lp]

def dric_flat_phi(h):
    p0, p1, p2 = sp.symbols('p0 p1 p2')
    r = sp.sqrt(r2)
    dphi = [p1 * X[a] / r for a in range(4)]
    ddphi = [[p2 * X[a] * X[b] / r2 + p1 * ((1 if a == b else 0) / r - X[a] * X[b] / r ** 3) for b in range(4)] for a in range(4)]
    def d2(i, j, k, l):
        return ddphi[k][l] * h[i, j] + dphi[k] * sp.diff(h[i, j], X[l]) + dphi[l] * sp.diff(h[i, j], X[k]) + \
            p0 * sp.diff(h[i, j], X[k], X[l])
    R = sp.zeros(4, 4)
    for i, j in itertools.product(range(4), repeat=2):
        R[i, j] = sp.Rational(1, 2) * sum(d2(j, k, k, i) + d2(i, k, k, j) - d2(i, j, k, k) for k in range(4)) \
            - sp.Rational(1, 2) * sum(d2(k, k, i, j) for k in range(4))
    return R, (p0, p1, p2)

Z3 = sp.zeros(3, 3)
cases = {
    'Wm': riemann_from_ops(Z3, sp.Matrix([[1, 2, 0], [2, -3, 1], [0, 1, 2]]), 0, Z3),
    'Rz': (lambda: riemann_from_ops(Z3, Z3, 0, sp.Matrix([[1, 2, -1], [0, 0, 0], [0, 0, 0]])))(),
    'Rp': (lambda: riemann_from_ops(Z3, Z3, 0, sp.Matrix([[0, 0, 0], [1, 0, -1], [0, 2, 1]])))(),
    'Rmix': riemann_from_ops(Z3, sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]), 0,
                             sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])),
}
for lab, R in cases.items():
    h2 = h2_field(R)
    DR, (p0, p1, p2) = dric_flat_phi(h2)
    Bs = []
    for i, o in enumerate(os_):
        integrand = sum(DR[a, c] * o[a, c] for a in range(4) for c in range(4))
        integrand = sp.expand(sp.together(integrand).subs(r2, 1))
        num, den = sp.fraction(sp.together(integrand))
        num = sp.expand(num.subs(sp.sqrt(r2), 1)); den = sp.simplify(den.subs(sp.sqrt(r2), 1).subs(r2, 1))
        cs = {}
        for pk in (p0, p1, p2):
            coeff = sp.expand(num).coeff(pk)
            Pc = sp.Poly(coeff, *X)
            cs[str(pk)] = sp.simplify(sum(c * mom(mon) for mon, c in Pc.terms()) / den)
        Bs.append(sp.Rational(1, 2) * (cs['p1'] - cs['p2']))
    print(lab, ': B = ', Bs, flush=True)
