"""
Step 59: EXACT (rational) evaluation of the eps^2 log(1/eps) Burns coefficient in the chiral-square form.

Rigorous reduction (step59 note, Thm 59.R): with C = (2W+, s/sqrt12), Burns g_B = delta + sig*A (C(g_B) = 0 exactly),
background normal-coordinate jet h2 = -(1/3) R_{iajb} x^a x^b and degree-0 corrector sig*K, the log coefficient is
     Phi = c/4,   c = [sig^2] ( 4 tr(X^2) + s'^2/12 ) sqrt(det g_B)  integrated over S^3 / (2 pi^2),
     X = P+ R' P+ - (s'/12) P+,   R' = d/dt R(g_B + t(h2 + sig K))|_{t=0}  (curvature endomorphism of 2-forms),
     s' = 2 tr R',  P+ = (1 + *_{g_B})/2.
Mode 'inv': background with only (s, W+) is SU(2)_- invariant, as are A and the 10 invariant correctors; SU(2)_-
acts simply transitively on S^3, so the density is constant on S^3 and c is its value at x0 = (1,0,0,0).
Everything is exact rational arithmetic (sympy).  Mode 'pt': pointwise residual Y = d/dsig D C_{g_B}[h + sig K]|_0
at given points, for W- / Ric^o backgrounds (whose C-linear part vanishes at sig = 0).
Output: workspace/data/step59_exact_log_coefficient.json
"""
import sys, os, json, itertools, time
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'data', 'step59_exact_log_coefficient.json')
X = sp.symbols('x1 y1 x2 y2', real=True)
NS, NT = 2, 1   # truncation orders in sig and t


class TS:
    """truncated series sum_{i<=NS, j<=NT} c_ij sig^i t^j with sympy coefficients"""
    __slots__ = ['d']
    def __init__(self, d=None):
        self.d = {k: v for k, v in (d or {}).items() if v != 0}
    @staticmethod
    def c(v, i=0, j=0):
        return TS({(i, j): sp.sympify(v)})
    def __add__(self, o):
        if not isinstance(o, TS): o = TS.c(o)
        d = dict(self.d)
        for k, v in o.d.items(): d[k] = d.get(k, 0) + v
        return TS(d)
    __radd__ = __add__
    def __neg__(self): return TS({k: -v for k, v in self.d.items()})
    def __sub__(self, o): return self + (-o if isinstance(o, TS) else TS.c(-sp.sympify(o)))
    def __rsub__(self, o): return (-self) + o
    def __mul__(self, o):
        if not isinstance(o, TS):
            o = sp.sympify(o)
            return TS({k: sp.expand(v * o) for k, v in self.d.items()})
        d = {}
        for (i1, j1), v1 in self.d.items():
            for (i2, j2), v2 in o.d.items():
                i, j = i1 + i2, j1 + j2
                if i <= NS and j <= NT:
                    d[(i, j)] = d.get((i, j), 0) + v1 * v2
        return TS({k: sp.expand(v) for k, v in d.items()})
    __rmul__ = __mul__
    def coef(self, i, j): return self.d.get((i, j), sp.Integer(0))
    def tder(self):  # d/dt at t=0 (keeps sig dependence)
        return TS({(i, 0): v for (i, j), v in self.d.items() if j == 1})


def zeros(*shape):
    import numpy as np
    a = np.empty(shape, dtype=object)
    for idx in itertools.product(*[range(n) for n in shape]): a[idx] = TS()
    return a


# ---------------- geometry of the model ----------------
Jz = sp.Matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
r2 = sum(v ** 2 for v in X)
Hlog = sp.hessian(sp.log(r2), X)
A_field = (Hlog + Jz.T * Hlog * Jz) / 4      # ddbar log r^2, normalised so ddbar r^2 = delta

def e2(a, b):
    m = sp.zeros(4, 4); m[a, b] = 1; m[b, a] = -1; return m
h = sp.Rational(1, 2)
# unnormalised basis with |L|^2 = 2 entries +-1 ; Rop basis uses L/sqrt2 -> products carry 1/2
Lp = [e2(0, 1) + e2(2, 3), e2(0, 2) - e2(1, 3), e2(0, 3) + e2(1, 2)]
Lm = [e2(0, 1) - e2(2, 3), e2(0, 2) + e2(1, 3), e2(0, 3) - e2(1, 2)]

def riemann_from_ops(Wp, Wm, s, Bmix):
    """R_abcd from Rop = [[Wp + s/12, Bmix],[Bmix^T, Wm + s/12]] in the orthonormal Lambda^+/- basis L/sqrt2."""
    import numpy as np
    Rop = sp.zeros(6, 6)
    Rop[:3, :3] = Wp + s / 12 * sp.eye(3); Rop[3:, 3:] = Wm + s / 12 * sp.eye(3)
    Rop[:3, 3:] = Bmix; Rop[3:, :3] = Bmix.T
    L = Lp + Lm
    R = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a, b, c, d in itertools.product(range(4), repeat=4):
        R[a][b][c][d] = sp.expand(h * sum(Rop[I, J] * L[I][a, b] * L[J][c, d] for I in range(6) for J in range(6)))
    return R

def h2_field(R):
    return sp.Matrix(4, 4, lambda i, j: -sp.Rational(1, 3) * sum(R[i][a][j][b] * X[a] * X[b]
                                                                 for a in range(4) for b in range(4)))

def invariant_forms():
    r = sp.sqrt(r2); x1, y1, x2, y2 = X
    dr = sp.Matrix([x1, y1, x2, y2]) / r
    s1 = sp.Matrix([-x2, y2, x1, -y1]) / r
    s2 = sp.Matrix([-y2, -x2, y1, x1]) / r
    s3 = sp.Matrix([-y1, x1, -y2, x2]) / r
    return [dr, s1, s2, s3]

def invariant_K(ks):
    f = invariant_forms(); K = sp.zeros(4, 4); n = 0
    for i in range(4):
        for j in range(i, 4):
            K += ks[n] * (f[i] * f[j].T + f[j] * f[i].T) / 2; n += 1
    return K


def jets_at(M, pt):
    sub = dict(zip(X, pt))
    J0 = [[sp.simplify(M[i, j].subs(sub)) for j in range(4)] for i in range(4)]
    J1 = [[[sp.simplify(sp.diff(M[i, j], X[k]).subs(sub)) for k in range(4)] for j in range(4)] for i in range(4)]
    J2 = [[[[sp.simplify(sp.diff(M[i, j], X[k], X[l]).subs(sub)) for l in range(4)] for k in range(4)]
           for j in range(4)] for i in range(4)]
    return J0, J1, J2


def density_sig2(Aj, Pj, verbose=False):
    """returns (dens TS in sig, t-derivative structure) ; Aj jets of A (numbers), Pj jets of P = h + sig K (exprs in sig)"""
    import numpy as np
    sig = sp.Symbol('sig')
    def ts_of(e):
        # e polynomial in sig (deg<=2); P part carries t^1
        e = sp.expand(e); out = {}
        for i in range(NS + 1):
            ci = e.coeff(sig, i)
            if ci != 0: out[(i, 0)] = ci
        return out
    g = zeros(4, 4); dg = zeros(4, 4, 4); ddg = zeros(4, 4, 4, 4)
    for i, j in itertools.product(range(4), repeat=2):
        g[i, j] = TS({(0, 0): sp.Integer(1 if i == j else 0), (1, 0): Aj[0][i][j]}) + \
            TS({(k[0], 1): v for k, v in ts_of(Pj[0][i][j]).items()})
        for k in range(4):
            dg[i, j, k] = TS({(1, 0): Aj[1][i][j][k]}) + TS({(kk[0], 1): v for kk, v in ts_of(Pj[1][i][j][k]).items()})
            for l in range(4):
                ddg[i, j, k, l] = TS({(1, 0): Aj[2][i][j][k][l]}) + \
                    TS({(kk[0], 1): v for kk, v in ts_of(Pj[2][i][j][k][l]).items()})
    # inverse: g = I + E, gi = I - E + E^2 - ... (E = O(sig, t)) ; need up to total order NS+NT = 3
    E = zeros(4, 4)
    for i, j in itertools.product(range(4), repeat=2):
        E[i, j] = g[i, j] - (1 if i == j else 0)
    def mm(Aa, Bb):
        C = zeros(4, 4)
        for i, j in itertools.product(range(4), repeat=2):
            acc = TS()
            for k in range(4): acc = acc + Aa[i, k] * Bb[k, j]
            C[i, j] = acc
        return C
    gi = zeros(4, 4); term = zeros(4, 4)
    for i in range(4): gi[i, i] = TS.c(1); term[i, i] = TS.c(1)
    for n in range(1, NS + NT + 1):
        term = mm(term, E); term = -1 * term if False else term
        sgn = (-1) ** n
        for i, j in itertools.product(range(4), repeat=2): gi[i, j] = gi[i, j] + sgn * term[i, j]
    # Christoffel Gam^k_ij = 1/2 g^kl (d_i g_jl + d_j g_il - d_l g_ij)
    T = zeros(4, 4, 4)
    for l, i, j in itertools.product(range(4), repeat=3):
        T[l, i, j] = dg[j, l, i] + dg[i, l, j] - dg[i, j, l]
    Gam = zeros(4, 4, 4)
    for k, i, j in itertools.product(range(4), repeat=3):
        acc = TS()
        for l in range(4): acc = acc + gi[k, l] * T[l, i, j]
        Gam[k, i, j] = acc * h
    # d_m g^kl = - g^ka d_m g_ab g^bl
    dgi = zeros(4, 4, 4)
    for k, l, m in itertools.product(range(4), repeat=3):
        acc = TS()
        for a in range(4):
            for b in range(4):
                if dg[a, b, m].d: acc = acc + gi[k, a] * dg[a, b, m] * gi[b, l]
        dgi[k, l, m] = -1 * acc
    dGam = zeros(4, 4, 4, 4)  # d_m Gam^k_ij
    for k, i, j, m in itertools.product(range(4), repeat=4):
        acc = TS()
        for l in range(4):
            dT = ddg[j, l, i, m] + ddg[i, l, j, m] - ddg[i, j, l, m]
            acc = acc + dgi[k, l, m] * T[l, i, j] + gi[k, l] * dT
        dGam[k, i, j, m] = acc * h
    # R^l_{ijk} = d_i Gam^l_jk - d_j Gam^l_ik + Gam^l_im Gam^m_jk - Gam^l_jm Gam^m_ik ; R_ijkl = -g_lm R^m_ijk
    Rup = zeros(4, 4, 4, 4)
    for l, i, j, k in itertools.product(range(4), repeat=4):
        acc = dGam[l, j, k, i] - dGam[l, i, k, j]
        for m in range(4): acc = acc + Gam[l, i, m] * Gam[m, j, k] - Gam[l, j, m] * Gam[m, i, k]
        Rup[l, i, j, k] = acc
    Rl = zeros(4, 4, 4, 4)
    for i, j, k, l in itertools.product(range(4), repeat=4):
        acc = TS()
        for m in range(4): acc = acc + g[l, m] * Rup[m, i, j, k]
        Rl[i, j, k, l] = -1 * acc
    pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]
    # curvature endomorphism on 2-forms: (R w)_ab = 1/2 R_abcd g^ce g^df w_ef ; column = basis E_ef
    Rend = zeros(6, 6)
    gg = zeros(4, 4, 4, 4)  # g^ce g^df - g^cf g^de
    for c, d, e, f in itertools.product(range(4), repeat=4):
        gg[c, d, e, f] = gi[c, e] * gi[d, f] - gi[c, f] * gi[d, e]
    for I, (a, b) in enumerate(pairs):
        for Jn, (e, f) in enumerate(pairs):
            acc = TS()
            for c in range(4):
                for d in range(4):
                    if Rl[a, b, c, d].d: acc = acc + Rl[a, b, c, d] * gg[c, d, e, f]
            Rend[I, Jn] = acc * h
    # Hodge star at g_B (t=0 part only), with sqrt det
    def t0(x): return TS({k: v for k, v in x.d.items() if k[1] == 0})
    import numpy as np
    G0 = sp.Matrix(4, 4, lambda i, j: sum(v * sp.Symbol('sig') ** k[0] for k, v in t0(g[i, j]).d.items()))
    sig = sp.Symbol('sig')
    det = sp.expand(G0.det())
    a1 = det.coeff(sig, 1); a2 = det.coeff(sig, 2)
    sq = TS({(0, 0): sp.Integer(1), (1, 0): a1 / 2, (2, 0): a2 / 2 - a1 ** 2 / 8})
    eps = {}
    for p in itertools.permutations(range(4)):
        eps[p] = sp.Matrix(4, 4, lambda i, j: 1 if p[j] == i else 0).det()
    Star = zeros(6, 6)
    gi0 = zeros(4, 4)
    for i, j in itertools.product(range(4), repeat=2): gi0[i, j] = t0(gi[i, j])
    for I, (a, b) in enumerate(pairs):
        for Jn, (e, f) in enumerate(pairs):
            acc = TS()
            for c in range(4):
                for d in range(4):
                    if c in (a, b) or d in (a, b) or c == d: continue
                    acc = acc + eps[(a, b, c, d)] * (gi0[c, e] * gi0[d, f] - gi0[c, f] * gi0[d, e])
            Star[I, Jn] = acc * sq * h
    Pp = zeros(6, 6)
    for I, Jn in itertools.product(range(6), repeat=2):
        Pp[I, Jn] = (Star[I, Jn] + (1 if I == Jn else 0)) * h
    Rp = zeros(6, 6)
    for I, Jn in itertools.product(range(6), repeat=2): Rp[I, Jn] = Rend[I, Jn].tder()
    sp_ = TS()
    for I in range(6): sp_ = sp_ + Rp[I, I]
    sp_ = sp_ * 2
    def mm6(Aa, Bb):
        C = zeros(6, 6)
        for i, j in itertools.product(range(6), repeat=2):
            acc = TS()
            for k in range(6): acc = acc + Aa[i, k] * Bb[k, j]
            C[i, j] = acc
        return C
    Xm = mm6(mm6(Pp, Rp), Pp)
    for I, Jn in itertools.product(range(6), repeat=2): Xm[I, Jn] = Xm[I, Jn] - sp_ * Pp[I, Jn] * sp.Rational(1, 12)
    X2 = mm6(Xm, Xm)
    trX2 = TS()
    for I in range(6): trX2 = trX2 + X2[I, I]
    dens = (trX2 * 4 + sp_ * sp_ * sp.Rational(1, 12)) * sq
    density_sig2.last_X = Xm   # linearised W+ endomorphism (P+ R' P+ - s'/12 P+), for pointwise residuals
    return dens, sp_


def main(mode='inv'):
    t0 = time.time()
    sig = sp.Symbol('sig')
    s, w11, w22, w12, w13, w23 = sp.symbols('s w11 w22 w12 w13 w23')
    ks = sp.symbols('k0:10')
    res = {}
    if mode == 'inv':
        Wp = sp.Matrix([[w11, w12, w13], [w12, w22, w23], [w13, w23, -w11 - w22]])
        R = riemann_from_ops(Wp, sp.zeros(3, 3), s, sp.zeros(3, 3))
        H2 = h2_field(R)
        K = invariant_K(ks)
        x0 = (1, 0, 0, 0)
        Aj = jets_at(A_field, x0)
        Hj = jets_at(H2, x0)
        Kj = jets_at(K, x0)
        Pj = [[[Hj[0][i][j] + sig * Kj[0][i][j] for j in range(4)] for i in range(4)],
              [[[Hj[1][i][j][k] + sig * Kj[1][i][j][k] for k in range(4)] for j in range(4)] for i in range(4)],
              [[[[Hj[2][i][j][k][l] + sig * Kj[2][i][j][k][l] for l in range(4)] for k in range(4)]
                for j in range(4)] for i in range(4)]]
        print('jets done', time.time() - t0, flush=True)
        dens, spr = density_sig2(Aj, Pj)
        print('density done', time.time() - t0, flush=True)
        c0 = sp.factor(dens.coef(0, 0)); c2 = sp.expand(dens.coef(2, 0))
        Fp = sp.expand(4 * (w11 ** 2 + w22 ** 2 + (w11 + w22) ** 2 + 2 * (w12 ** 2 + w13 ** 2 + w23 ** 2)) + s ** 2 / 12)
        print('sig^0 check (should be 4|W+|^2+s^2/12):', sp.simplify(c0 - Fp), flush=True)
        print('scalar check s\' at sig^0:', sp.simplify(spr.coef(0, 0) - s))
        res['sig0_minus_Fplus'] = str(sp.simplify(c0 - Fp))
        # minimise over k (zeta eigenvector: w12 = w13 = 0)
        c2e = sp.expand(c2.subs({w12: 0, w13: 0}))
        grad = [sp.diff(c2e, k) for k in ks]
        sol = sp.solve(grad, ks, dict=True)
        print('solutions', len(sol), flush=True)
        cmin = sp.factor(sp.expand(c2e.subs(sol[0])))
        Phi = sp.factor(cmin / 4)
        print('Phi(s, W+) =', Phi, flush=True)
        mu1 = w11 + s / 12
        # W+ restricted to zeta-perp: [[w22, w23],[w23, -w11-w22]]
        tr_perp = -w11; mu23 = sp.sqrt(((w22 - (-w11 - w22)) / 2) ** 2 + w23 ** 2)
        pred = sp.expand(s ** 2 / 288 - s * w11 / 24 - w11 ** 2 - 2 * (((2 * w22 + w11) / 2) ** 2 + w23 ** 2))
        print('Phi - prediction(1/288,-1/24,-1,-1):', sp.simplify(Phi - pred), flush=True)
        # unbounded direction check: with w12 != 0
        c2l = sp.expand(c2)
        grad_l = [sp.diff(c2l, k) for k in ks]
        soll = sp.solve(grad_l, ks, dict=True)
        res['leak_solvable'] = len(soll) > 0
        PhiCH = Phi.subs({s: -24, w11: 2, w22: -4, w23: 0})
        PhiKEpar = Phi.subs({w11: s / 6, w22: -s / 12, w23: 0})
        print('Phi_CH_perp =', PhiCH, ' Phi_Kahler_par =', sp.factor(PhiKEpar), flush=True)
        kappa = {str(k): str(sp.simplify(v)) for k, v in sol[0].items()}
        res.update(dict(Phi=str(Phi), Phi_minus_pred=str(sp.simplify(Phi - pred)), Phi_CH_perp=str(PhiCH),
                        Phi_Kahler_parallel=str(sp.factor(PhiKEpar)), optimal_k=kappa,
                        c2_quadratic_form=str(c2e), time=time.time() - t0))
        # KE perp explicit corrector value check
        kke = {k: sp.simplify(v.subs({w11: -s / 12, w22: s / 6, w23: 0})) for k, v in sol[0].items()}
        res['optimal_k_KEperp'] = {str(k): str(v) for k, v in kke.items()}
        print('KE perp optimal k:', kke, flush=True)
    json.dump(res, open(OUT, 'w'), indent=1)
    print('saved', OUT, time.time() - t0)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'inv')
