"""
Step 60: exact cokernel pairing for an Eguchi-Hanson insertion at an R^4/Z2 point (Target 58.Q, leading order).

EH in its hyperkahler orientation (Kahler forms omega_I, omega_J, omega_K self-dual).  L^2 harmonic ASD form
Omega = (e^03 - e^12)/r^4 (exact on EH; = -1/2 d(theta_I / r^4) with theta_I = <I x, dx>);
cokernel (L^2 infinitesimal Einstein deformations, TT):  o_i = Omega o omega_i  (symmetric trace-free).

For any smooth extension hh on EH of the background quadratic jet h2 = -(1/3) R_{iajb} x^a x^b,
   B_i = int_EH < DRic_EH[hh], o_i > dmu   (DRic* o_i = 0, so this is the flux at infinity)
       = int_{R^4/Z2} < DRic_flat[phi(r) h2], o_i^flat > dx      (phi = 0 near 0, 1 near infinity),
and with phi-derivatives p1 = phi'(r), p2 = phi''(r):  radial density = c2 r phi'' + c1 phi' (+ c0 phi / r, c0 = 0),
so B_i = (1/2)(c1 - c2)  (factor 1/2 for the Z2 quotient).
Output: workspace/data/step60_EH_obstruction_pairing.json
"""
import sys, os, json, itertools
import sympy as sp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step59_exact_log_coefficient import riemann_from_ops, h2_field, X, Lp, Lm, r2

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'data', 'step60_EH_obstruction_pairing.json')
x = sp.Matrix(X)

I = Lp[0]
theta = I * x
Om = sp.zeros(4, 4)
for a, b in itertools.product(range(4), repeat=2):
    Om[a, b] = sp.simplify(-sp.Rational(1, 2) * (sp.diff(theta[b] / r2 ** 2, X[a]) - sp.diff(theta[a] / r2 ** 2, X[b])))
sd = [sp.simplify(sum(Om[a, b] * L[a, b] for a in range(4) for b in range(4))) for L in Lp]
asd = [sp.simplify(sum(Om[a, b] * L[a, b] for a in range(4) for b in range(4)) * r2 ** 2) for L in Lm]
print('Omega SD components (must be 0):', sd, ' ASD comps * r^4:', asd)
os_ = [sp.simplify(Om * L) for L in Lp]
print('o_i symmetric:', [sp.simplify(o - o.T) == sp.zeros(4, 4) for o in os_], ' traces:', [sp.simplify(o.trace()) for o in os_])
print('|o_i|^2 r^8:', [sp.simplify(sum(v ** 2 for v in o) * r2 ** 4) for o in os_])
# divergence-free and harmonic checks (flat)
print('div o_i:', [sp.simplify(sp.Matrix([sum(sp.diff(o[a, c], X[a]) for a in range(4)) for c in range(4)])).T for o in os_])

def mom(alpha):
    if any(a % 2 for a in alpha): return sp.Integer(0)
    return 2 * sp.prod([sp.gamma(sp.Rational(a + 1, 2)) for a in alpha]) / sp.gamma(sp.Rational(sum(alpha) + 4, 2))

def dric_flat_phi(h):
    """DRic_flat[phi h] on the unit sphere r = 1, as p0*A0 + p1*A1 + p2*A2 (p_k = phi^(k)(1))."""
    p0, p1, p2 = sp.symbols('p0 p1 p2')
    r = sp.sqrt(r2)
    dphi = [p1 * X[a] / r for a in range(4)]
    ddphi = [[p2 * X[a] * X[b] / r2 + p1 * ((1 if a == b else 0) / r - X[a] * X[b] / r ** 3) for b in range(4)] for a in range(4)]
    # phi h_ij ; derivatives by product rule
    def d1(i, j, k): return dphi[k] * h[i, j] + p0 * sp.diff(h[i, j], X[k])
    def d2(i, j, k, l):
        return ddphi[k][l] * h[i, j] + dphi[k] * sp.diff(h[i, j], X[l]) + dphi[l] * sp.diff(h[i, j], X[k]) + \
            p0 * sp.diff(h[i, j], X[k], X[l])
    R = sp.zeros(4, 4)
    for i, j in itertools.product(range(4), repeat=2):
        R[i, j] = sp.Rational(1, 2) * sum(d2(j, k, k, i) + d2(i, k, k, j) - d2(i, j, k, k) for k in range(4)) \
            - sp.Rational(1, 2) * sum(d2(k, k, i, j) for k in range(4))
    return R, (p0, p1, p2)

w = sp.symbols('wp11 wp12 wp13 wp22 wp23'); m = sp.symbols('wm11 wm12 wm13 wm22 wm23')
s = sp.Symbol('s'); b = sp.symbols('b0:9')
Wp = sp.Matrix([[w[0], w[1], w[2]], [w[1], w[3], w[4]], [w[2], w[4], -w[0] - w[3]]])
Wm = sp.Matrix([[m[0], m[1], m[2]], [m[1], m[3], m[4]], [m[2], m[4], -m[0] - m[3]]])
Bm = sp.Matrix(3, 3, list(b))
R = riemann_from_ops(Wp, Wm, s, Bm)
h2 = h2_field(R)
DR, (p0, p1, p2) = dric_flat_phi(h2)
res = {}
for i, o in enumerate(os_):
    integrand = sum(DR[a, c] * o[a, c] for a in range(4) for c in range(4))
    integrand = sp.expand(sp.together(integrand).subs(r2, 1))
    num, den = sp.fraction(sp.together(integrand))
    # on the unit sphere den is a power of r2 -> 1 ; replace sqrt(r2) too
    num = sp.expand(num.subs(sp.sqrt(r2), 1)); den = sp.simplify(den.subs(sp.sqrt(r2), 1).subs(r2, 1))
    cs = {}
    for pk in (p0, p1, p2):
        coeff = sp.expand(num).coeff(pk)
        Pc = sp.Poly(coeff, *X)
        cs[str(pk)] = sp.simplify(sum(c * mom(mon) for mon, c in Pc.terms()) / den)
    Bi = sp.factor(sp.Rational(1, 2) * (cs['p1'] - cs['p2']))
    res['o%d' % i] = {k: str(v) for k, v in cs.items()}
    res['B%d' % i] = str(Bi)
    print('o_%d: c0 = %s, c1 = %s, c2 = %s ;  B_%d = %s' % (i, cs['p0'], cs['p1'], cs['p2'], i, Bi), flush=True)
Rp_zeta = (Wp + s / 12 * sp.eye(3))[:, 0]
res['Rplus_zeta'] = [str(v) for v in Rp_zeta]
res['B_over_Rplus_zeta'] = [str(sp.simplify(sp.sympify(res['B%d' % i]) / Rp_zeta[i])) for i in range(3)]
print('B_i / (R+ zeta)_i:', res['B_over_Rplus_zeta'])
json.dump(res, open(OUT, 'w'), indent=1)
print('saved', OUT)
