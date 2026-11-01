"""Step 85: exact algebra behind the coupled AKE second-order center theorem and the
neck/core form analysis.

Checks (all exact, SymPy):
 A1  d/dt |w|^2_{g+th} = -tr h  (form norm |w|^2 = 1/2 w_ab w^ab, |w1|^2 = 2).
 A2  cross term d/ds d/dt |w1 + t b|^2_{g+s h} = 0 for every symmetric h and b in span(w2,w3).
 A3  first variation of the ASD projection of w1: zero for J-anti-invariant h, nonzero for
     J-invariant trace-free h; trace part never contributes.
 A4  mixed source: first variation of ASD projection of b in span(w2,w3) along anti-J h is
     generically nonzero (so a transport correction is genuinely needed).
 A5  Nagy compatibility: with g^{-1}g_t = 1 + t H1 + t^2/2 H2, H1 anti-J, H2^+ = H1^2,
     the fixed w1 is self-dual for g_t and |w1|^2_{g_t} = 2 through O(t^2).
 B1  homogeneous closed self-dual forms on R^4\\0 with harmonic components:
     dimensions for degrees k>=0 and -2-k, with parity under x -> -x.
 B2  Eguchi-Hanson: the r^-4 tail of the resolution Kaehler form w_1 is flat-ASD;
     the holomorphic-symplectic forms w_2, w_3 have no tail.
Output: workspace/data/step85/center_algebra.json
"""
import itertools, json, os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'data', 'step85')
os.makedirs(OUT, exist_ok=True)
res = {}

x = sp.symbols('x1:5', real=True)
t, s = sp.symbols('t s', real=True)

def form(pairs):
    F = sp.zeros(4, 4)
    for (a, b, c) in pairs:
        F[a, b] += c; F[b, a] -= c
    return F

w1 = form([(0, 1, 1), (2, 3, 1)])
w2 = form([(0, 2, 1), (3, 1, 1)])
w3 = form([(0, 3, 1), (1, 2, 1)])
eps = sp.LeviCivita

def hodge(F, G):
    Gi = G.inv(); dG = sp.sqrt(G.det())
    Fup = Gi * F * Gi.T
    S = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            S[a, b] = sp.Rational(1, 2) * dG * sum(eps(a, b, c, d) * Fup[c, d]
                                                  for c in range(4) for d in range(4))
    # lower indices already: (*F)_{ab} = 1/2 sqrt|G| eps_{abcd} F^{cd}
    return S

def norm2(F, G):
    Gi = G.inv()
    return sp.Rational(1, 2) * sum(F[a, b] * F[c, d] * Gi[a, c] * Gi[b, d]
                                   for a in range(4) for b in range(4) for c in range(4) for d in range(4))

I4 = sp.eye(4)
for F in (w1, w2, w3):
    assert sp.simplify(hodge(F, I4) - F) == sp.zeros(4, 4)
J = w1  # endomorphism with J^2=-1 (up to sign convention, irrelevant for commutation)
assert J * J == -I4

hs = sp.symbols('h0:10', real=True)
H = sp.Matrix([[hs[0], hs[1], hs[2], hs[3]], [hs[1], hs[4], hs[5], hs[6]],
               [hs[2], hs[5], hs[7], hs[8]], [hs[3], hs[6], hs[8], hs[9]]])
Hplus = (H - J * H * J) / 2      # commutes with J
Hminus = (H + J * H * J) / 2     # anticommutes with J
assert sp.simplify(Hplus * J - J * Hplus) == sp.zeros(4, 4)
assert sp.simplify(Hminus * J + J * Hminus) == sp.zeros(4, 4)

# A1
G = I4 + t * H
res['A1_dnorm_plus_trace'] = str(sp.simplify(sp.diff(norm2(w1, G), t).subs(t, 0) + H.trace()))
# A2
b2, b3 = sp.symbols('b2 b3', real=True)
B = b2 * w2 + b3 * w3
Gs = I4 + s * H
expr = norm2(w1 + t * B, Gs)
res['A2_cross_term'] = str(sp.simplify(sp.diff(expr, t, s).subs({t: 0, s: 0})))
# A3
def asd_first_var(F, Hm):
    Gt = I4 + t * Hm
    return sp.simplify(sp.diff((F - hodge(F, Gt)) / 2, t).subs(t, 0))
res['A3_antiJ_var_of_w1_ASD'] = str(asd_first_var(w1, Hminus))
Hp0 = Hplus - (Hplus.trace() / 4) * I4
res['A3_Jinv_tracefree_var_of_w1_ASD_is_zero'] = bool(asd_first_var(w1, Hp0) == sp.zeros(4, 4))
res['A3_trace_var'] = str(asd_first_var(w1, I4))
# A4
res['A4_mixed_source_antiJ_on_b_is_zero'] = bool(asd_first_var(B, Hminus) == sp.zeros(4, 4))
# A5 Nagy compatibility, with a concrete random-rational anti-J H1 and H2 = H1^2 + (anti-J part)
import random
random.seed(7)
def rand_sym():
    M = sp.zeros(4, 4)
    for a in range(4):
        for b in range(a, 4):
            M[a, b] = M[b, a] = sp.Rational(random.randint(-5, 5), random.randint(1, 4))
    return M
R1 = rand_sym(); H1 = (R1 + J * R1 * J) / 2
R2 = rand_sym(); H2 = H1 * H1 + (R2 + J * R2 * J) / 2
A = I4 + t * H1 + t**2 / 2 * H2          # g^{-1} g_t as endomorphism; g = I
Gt = A                                   # metric matrix g_t = g A (g = I, A symmetric)
asd = (w1 - hodge(w1, Gt)) / 2
asd_ser = [sp.simplify(sp.series(asd[a, b], t, 0, 3).removeO()) for a in range(4) for b in range(4)]
nrm_ser = sp.simplify(sp.series(norm2(w1, Gt), t, 0, 3).removeO())
res['A5_ASD_part_through_t2'] = [str(e) for e in asd_ser if e != 0]
res['A5_norm_through_t2'] = str(nrm_ser)
# control: H2^+ != H1^2 breaks it
H2bad = H2 + sp.diag(1, 1, 0, 0) - sp.diag(0, 0, 1, 1)  # J-invariant trace-free change
nrm_bad = sp.simplify(sp.series(norm2(w1, I4 + t * H1 + t**2 / 2 * H2bad), t, 0, 3).removeO())
asd_bad = (w1 - hodge(w1, I4 + t * H1 + t**2 / 2 * H2bad)) / 2
res['A5_control_ASD_nonzero'] = any(sp.simplify(sp.series(asd_bad[a, b], t, 0, 3).removeO()) != 0
                                    for a in range(4) for b in range(4))
res['A5_control_norm'] = str(nrm_bad)

# B1 homogeneous closed SD forms
def harmonic_basis(k):
    mons = [m for m in itertools.combinations_with_replacement(range(4), k)]
    cs = sp.symbols('c0:%d' % len(mons))
    p = sum(c * sp.Mul(*[x[i] for i in m]) for c, m in zip(cs, mons)) if k > 0 else cs[0]
    lap = sp.expand(sum(sp.diff(p, xi, 2) for xi in x))
    eqs = sp.Poly(lap, *x).coeffs() if lap != 0 else []
    sol = sp.solve(eqs, cs, dict=True)
    p = p.subs(sol[0]) if sol else p
    free = sorted(p.free_symbols - set(x), key=str)
    return [sp.expand(p.diff(f)) for f in free]

def dform(Wf):
    # Wf: 4x4 antisymmetric matrix of functions; returns list of independent 3-form components
    comps = []
    for (a, b, c) in itertools.combinations(range(4), 3):
        comps.append(sp.diff(Wf[b, c], x[a]) + sp.diff(Wf[c, a], x[b]) + sp.diff(Wf[a, b], x[c]))
    return comps

r2 = sum(xi**2 for xi in x)
dims = {}
for k in range(0, 4):
    basis = harmonic_basis(k)
    for kind in ('growing', 'decaying'):
        coeffs = []
        W = sp.zeros(4, 4)
        for i, wi in enumerate((w1, w2, w3)):
            for j, Y in enumerate(basis):
                c = sp.Symbol('a_%d_%d' % (i, j)); coeffs.append(c)
                f = Y if kind == 'growing' else Y * r2**(-1 - k)
                W += c * f * wi
        comps = dform(W)
        eqs = []
        for cpt in comps:
            e = sp.expand(sp.simplify(cpt * (1 if kind == 'growing' else r2**(k + 2))))
            if e != 0:
                eqs += sp.Poly(e, *x).coeffs()
        Mx = sp.Matrix([[sp.diff(e, c) for c in coeffs] for e in eqs]) if eqs else sp.zeros(0, len(coeffs))
        nsol = len(coeffs) - (Mx.rank() if eqs else 0)
        deg = k if kind == 'growing' else -2 - k
        dims[str(deg)] = {'dim_closed_SD': int(nsol), 'even_under_minus1': (deg % 2 == 0)}
res['B1_homogeneous_closed_SD_dims'] = dims

# B2 Eguchi-Hanson tail: Kaehler potential phi(u), u=|z|^2, resolution form w_1 = (i/2) dd^c-type
a = sp.symbols('a', positive=True)
u = sp.symbols('u', positive=True)
phi = sp.sqrt(u**2 + a**4) + a**2 * sp.log(u / (a**2 + sp.sqrt(u**2 + a**4)))
phi_ser = sp.series(phi, u, sp.oo, 3).removeO()
res['B2_EH_potential_large_u'] = str(sp.simplify(phi_ser))
# i ddbar (1/u) on C^2 with z1=x1+ix2, z2=x3+ix4: compute as real 2-form and test ASD
z = [(x[0], x[1]), (x[2], x[3])]
def iddbar(f):
    # i d dbar f as real 2-form matrix: (i ddbar f) = sum f_{j kbar} i dz_j ^ dzbar_k
    W = sp.zeros(4, 4)
    dz = []
    for (p, q) in z:
        dz.append((p, q))
    def dzj(f, j):  # d/dz_j = 1/2 (d/dx - i d/dy)
        p, q = z[j]; return (sp.diff(f, p) - sp.I * sp.diff(f, q)) / 2
    def dzbj(f, j):
        p, q = z[j]; return (sp.diff(f, p) + sp.I * sp.diff(f, q)) / 2
    # i dz_j ^ dzbar_k as real matrix
    def one(j, conj):
        v = sp.zeros(4, 1); p = 2 * j
        v[p] = 1; v[p + 1] = (-sp.I if conj else sp.I)
        return v
    for j in range(2):
        for k in range(2):
            coef = dzbj(dzj(f, j), k)
            A_ = one(j, False); B_ = one(k, True)
            W += sp.I * coef * (A_ * B_.T - B_ * A_.T)
    return W.applyfunc(sp.simplify)
tail = iddbar(1 / r2)
res['B2_tail_is_real'] = bool(sp.simplify(tail - tail.conjugate()) == sp.zeros(4, 4))
res['B2_tail_selfdual_part_zero'] = bool(sp.simplify(tail + hodge(tail, I4)) == sp.zeros(4, 4))
w0 = iddbar(r2 / 2)
res['B2_flat_kahler_form_is_SD'] = bool(sp.simplify(w0 - hodge(w0, I4)) == sp.zeros(4, 4))
res['B2_note'] = ('phi = u - a^4/(2u) + O(u^-3): the r^-4 tail of the resolution form is '
                  '-(a^4/2) i ddbar(1/r^2), primitive (1,1), hence flat-ASD; dz1^dz2 (w2+i w3) is untouched.')

with open(os.path.join(OUT, 'center_algebra.json'), 'w') as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
