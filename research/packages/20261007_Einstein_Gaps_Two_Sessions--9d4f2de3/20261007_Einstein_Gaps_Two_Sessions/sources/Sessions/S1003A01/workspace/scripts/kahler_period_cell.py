"""Exact period formula for U(2)-invariant Kaehler blow-up cells in a complex-space-form bulk.

Metric (Cartan-verified conventions of perp_cartan_verify.py, d sigma_i = 2 sigma_j^sigma_k,
int sigma_123 = 2 pi^2):
    g = dx^2/(4K) + x (s1^2 + s2^2) + K s3^2,     a = b = sqrt(x), c = sqrt(K), dt = dx/(2 sqrt K).
Collar: K = x + kappa x^2 (kappa=+1 complex hyperbolic Ric=-6g, kappa=-1 Fubini-Study Ric=+6g).
Bolt at x0: K(x0)=0, K'(x0)=1 (ordinary O(-1) bolt; Burns metric K = x - x0).

Checks symbolically, from the verified spin formulas (1.1),(1.4) of the Step-7 note:
  (i)   s = 4 (2 - (xK)'')/x ;
  (ii)  with u := xK - x^2 - kappa x^3 and lambda = -6 kappa,
        P-density - (s-4 lambda)^2-density/4 = exact x-derivative of an explicit boundary form B(x),
        so that P/(8 pi^2) = (1+3 kappa x0)^2 + (1/2) int_{x0}^{X} u''^2/x dx   for every admissible K;
  (iii) the Burns, Eguchi-Hanson and complex-space-form values of the pieces.
"""
import sympy as sp

x, kap, x0 = sp.symbols('x kappa x0', positive=True)
Kf = sp.Function('K')
K = Kf(x)


def spin_quantities(a1, a2, a3, dtdx):
    """u_i, H_i, lambda_i and P-, s-densities per dt, given a_i(x) and dt/dx."""
    D = lambda f: sp.diff(f, x) / dtdx
    A = [a1, a2, a3]
    u, H, lam = [], [], []
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        u.append(D(A[i]) - (A[j]**2 + A[k]**2 - A[i]**2) / (A[j] * A[k]))
        lam.append(A[j] * A[k] / A[i])
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        H.append(u[i] + u[j] * u[k] / 2)
    abc = A[0] * A[1] * A[2]
    r = [D(u[i]) / A[i] for i in range(3)]
    v = [2 * H[i] / (A[(i + 1) % 3] * A[(i + 2) % 3]) for i in range(3)]
    ric0sq = sum((r[i] - v[i])**2 for i in range(3))
    s = -2 * sum(r[i] + v[i] for i in range(3))
    # P/(8 pi^2) = int abc/4 |Ric0|^2 dt  (orbit volume 2 pi^2 abc dt);  same normalization for s^2
    return u, s, ric0sq, abc


def main():
    a = sp.sqrt(x); c = sp.sqrt(K)
    dtdx = 1 / (2 * sp.sqrt(K))
    u, s, ric0sq, abc = spin_quantities(a, a, c, dtdx)
    s_s = sp.simplify(s)
    s_claim = 4 * (2 - sp.diff(x * K, x, 2)) / x
    print('(i) s - 4(2-(xK)\'\')/x =', sp.simplify(s_s - s_claim))
    lam = -6 * kap
    Pdens = sp.simplify(abc / 4 * ric0sq * dtdx)          # P/(8 pi^2) per dx
    Ldens = sp.simplify(abc / 4 * (s_claim - 4 * lam)**2 * dtdx)   # L/(8 pi^2) per dx
    # claim: Pdens - Ldens/4 = d/dx B  with B to be found; Ldens/4 = (1/2) u''^2/x * ?  check
    uu = x * K - x**2 - kap * x**3
    print('    L-density/4 - (1/2)u\'\'^2/x =', sp.simplify(Ldens / 4 - sp.diff(uu, x, 2)**2 / (2 * x)))
    diff = sp.simplify(sp.expand(Pdens - Ldens / 4))
    print('    P-density minus scalar part =', sp.factor(diff))
    # find boundary form: try B = polynomial in K, K', x
    k0, k1 = sp.symbols('k0 k1')
    expr = diff.subs(sp.Derivative(K, (x, 2)), sp.Symbol('k2')).subs(sp.Derivative(K, x), k1).subs(K, k0)
    expr = sp.expand(sp.simplify(expr))
    print('    in jets:', sp.factor(expr))
    # ansatz B = sum c_ij x^i k0^? ...; guess from Kaehler theory: B = -(1/2x)(k1 x - ? )^2-type; solve generally
    cs = sp.symbols('c0:12')
    monos = [1, x, x**2, k0, k0 * x, k0 / x, k1, k1 * x, k1**2, k1 * k0 / x, k0**2 / x**2, k1 * x**2]
    B = sum(ci * m for ci, m in zip(cs, monos))
    dB = sp.diff(B, x) + sp.diff(B, k0) * k1 + sp.diff(B, k1) * sp.Symbol('k2')
    eqs = sp.Poly(sp.expand((dB - expr) * x**3), x, k0, k1, sp.Symbol('k2')).coeffs()
    sol = sp.solve(eqs, cs, dict=True)
    print('    boundary-form solutions:', sol)
    if sol:
        Bs = sp.simplify(B.subs(sol[0]).subs({ci: 0 for ci in cs}))
        print('    B =', sp.factor(Bs))
        Bbolt = sp.simplify(Bs.subs({k0: 0, k1: 1, x: x0}))
        Bcol = sp.simplify(Bs.subs({k0: x + kap * x**2, k1: 1 + 2 * kap * x}))
        print('    B(bolt)=', sp.factor(Bbolt), '  B(collar)=', sp.factor(Bcol))
        print('    B(collar)-B(bolt) =', sp.factor(sp.expand(Bcol - Bbolt)),
              ' vs (1+3 kappa x0)^2 =', sp.expand((1 + 3 * kap * x0)**2))
    # sample geometries
    for name, Kex in [('Burns', x - x0), ('EH', x - x0**2 / x), ('CSF', x + kap * x**2)]:
        sub = {K: Kex}
        sv = sp.simplify(s_claim.subs(K, Kex).doit())
        pv = sp.simplify(Pdens.subs(K, Kex).doit())
        print(name, ' s =', sv, '  P-density =', sp.factor(pv))


if __name__ == '__main__':
    main()
