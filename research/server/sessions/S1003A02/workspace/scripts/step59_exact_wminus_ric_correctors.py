"""
Step 59b (v2): exact correctors in the W^- and Ric^o sectors via pointwise LINEAR equations.

For a pure W^- or pure Ric^o jet, C' = D C_{g_B}[h2 + sig K] = sig * Y + O(sig^2) with Y linear in K.
The sector log coefficient is int |Y|^2 >= 0 and vanishes iff Y == 0.  For K = sum_n c_n T_n (explicit ansatz,
linear in h2, degree 0) we impose Y(pt) = 0 (all entries of the linearised W+ endomorphism and of s') at random
rational points, solve exactly, and verify Y = 0 at fresh points.
Usage: python step59_exact_wminus_ric_correctors.py [Wm|Rz|Rp]
Output: workspace/data/step59_exact_correctors_<mode>.json
"""
import sys, os, json, time, random, itertools
import sympy as sp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step59_exact_log_coefficient import (X, r2, A_field, riemann_from_ops, h2_field, density_sig2, Jz)

HERE = os.path.dirname(os.path.abspath(__file__))
mode = sys.argv[1] if len(sys.argv) > 1 else 'Wm'
OUT = os.path.join(HERE, '..', 'data', 'step59_exact_correctors_%s.json' % mode)
t0 = time.time()
sig = sp.Symbol('sig')

Z3 = sp.zeros(3, 3)
if mode == 'Wm':
    R = riemann_from_ops(Z3, sp.Matrix([[1, 2, 0], [2, -3, 1], [0, 1, 2]]), 0, Z3)
elif mode == 'Rz':
    B = sp.zeros(3, 3); B[0, 0] = 1; B[0, 1] = 2; B[0, 2] = -1
    R = riemann_from_ops(Z3, Z3, 0, B)
else:
    B = sp.zeros(3, 3); B[1, 0] = 1; B[2, 1] = 2; B[1, 2] = -1; B[2, 2] = 1
    R = riemann_from_ops(Z3, Z3, 0, B)
H = h2_field(R); A = A_field
xv = sp.Matrix(X); Pm = xv * xv.T
def sym(M): return (M + M.T) / 2
q = (xv.T * H * xv)[0, 0]; trH = H.trace(); trHA = (H * A).trace(); J = Jz
qJ = (xv.T * J.T * H * J * xv)[0, 0]
terms = {
    'sym(hA)': sym(H * A), 'tr(hA)d': trHA * sp.eye(4), 'tr(h)A': trH * A, 'qA/r2': q * A / r2,
    'qd/r4': q * sp.eye(4) / r2 ** 2, 'qP/r6': q * Pm / r2 ** 3, 'sym(hP)/r4': sym(H * Pm) / r2 ** 2,
    'tr(h)d/r2': trH * sp.eye(4) / r2, 'tr(h)P/r4': trH * Pm / r2 ** 2, 'tr(hA)P/r2': trHA * Pm / r2,
    'h/r2': H / r2, 'JhJt/r2': J * H * J.T / r2, 'sym(JhJtA)': sym(J * H * J.T * A),
    'sym(hJAJt)': sym(H * J * A * J.T), 'sym(hPA)/r2': sym(H * Pm * A) / r2, 'sym(AhA)r2': sym(A * H * A) * r2,
    'sym(JhJtP)/r4': sym(J * H * J.T * Pm) / r2 ** 2, 'sym(hJPJt)/r4': sym(H * J * Pm * J.T) / r2 ** 2,
    'qJ JPJt/r6': qJ * J * Pm * J.T / r2 ** 3, 'qJA/r2': qJ * A / r2, 'qJd/r4': qJ * sp.eye(4) / r2 ** 2,
    'qJP/r6': qJ * Pm / r2 ** 3, 'qJPJt/r6': q * J * Pm * J.T / r2 ** 3,
    'sym(hJ)J?': sym(H * J * Pm * J.T * A),
}
names = list(terms.keys()); cs = sp.symbols('c0:%d' % len(names))

_JCACHE = {}
def _jet_funcs(M):
    key = id(M)
    if key not in _JCACHE:
        idx0 = [(i, j) for i in range(4) for j in range(4)]
        e0 = [M[i, j] for (i, j) in idx0]
        e1 = [sp.diff(M[i, j], X[k]) for (i, j) in idx0 for k in range(4)]
        e2 = [sp.diff(M[i, j], X[k], X[l]) for (i, j) in idx0 for k in range(4) for l in range(4)]
        f = sp.lambdify(X, e0 + e1 + e2, modules='sympy')
        _JCACHE[key] = (M, f)   # keep M alive so id stays unique
    return _JCACHE[key][1]

def jets(M, pt):
    vals = [sp.nsimplify(v) if not isinstance(v, sp.Basic) else sp.simplify(v)
            for v in _jet_funcs(M)(*[sp.Rational(p) for p in pt])]
    n0, n1 = 16, 64
    J0 = [[vals[4 * i + j] for j in range(4)] for i in range(4)]
    J1 = [[[vals[n0 + 16 * i + 4 * j + k] for k in range(4)] for j in range(4)] for i in range(4)]
    J2 = [[[[vals[n0 + n1 + 64 * i + 16 * j + 4 * k + l] for l in range(4)] for k in range(4)] for j in range(4)]
          for i in range(4)]
    return J0, J1, J2

random.seed(3)
def rpt():
    return tuple(sp.Rational(random.randint(-7, 7), random.randint(1, 5)) for _ in range(4))

def residual(pt, coeffs):
    Aj = jets(A, pt); Hj = jets(H, pt)
    Tj = [jets(terms[n], pt) for n in names]
    def comb(level, idx):
        v = 0
        for c, T in zip(coeffs, Tj):
            e = T[level]
            for i in idx: e = e[i]
            v += c * e
        return v
    Pj = [[[Hj[0][i][j] + sig * comb(0, (i, j)) for j in range(4)] for i in range(4)],
          [[[Hj[1][i][j][k] + sig * comb(1, (i, j, k)) for k in range(4)] for j in range(4)] for i in range(4)],
          [[[[Hj[2][i][j][k][l] + sig * comb(2, (i, j, k, l)) for l in range(4)] for k in range(4)]
            for j in range(4)] for i in range(4)]]
    dens, spr = density_sig2(Aj, Pj)
    Xm = density_sig2.last_X
    eqs = [sp.expand(Xm[I, Jn].coef(1, 0)) for I in range(6) for Jn in range(6)] + [sp.expand(spr.coef(1, 0))]
    zero0 = [sp.expand(Xm[I, Jn].coef(0, 0)) for I in range(6) for Jn in range(6)] + [sp.expand(spr.coef(0, 0))]
    assert all(z == 0 for z in zero0), 'sector has nonzero C at sig^0'
    return [e for e in eqs if e != 0]

eqs = []
for n in range(5):
    eqs += residual(rpt(), cs)
    print('point', n, len(eqs), time.time() - t0, flush=True)
sol = sp.linsolve(eqs, cs)
res = dict(mode=mode, names=names, n_eq=len(eqs))
if not sol:
    print('NO SOLUTION in ansatz', flush=True); res['solution'] = None
else:
    s0 = list(sol)[0]
    free = sorted(set().union(*[e.free_symbols for e in s0]) & set(cs), key=str)
    s0 = [sp.simplify(e.subs({f: 0 for f in free})) for e in s0]
    res['solution'] = {names[i]: str(v) for i, v in enumerate(s0) if v != 0}
    res['free_params'] = [str(f) for f in free]
    print('solution', res['solution'], 'free', len(free), flush=True)
    chk = []
    for _ in range(3):
        r_ = residual(rpt(), s0)
        chk.append(all(sp.simplify(e) == 0 for e in r_))
    res['fresh_points_Y_zero'] = chk
    print('fresh points Y==0:', chk, flush=True)
res['time'] = time.time() - t0
json.dump(res, open(OUT, 'w'), indent=1)
print('saved', OUT, res['time'])
