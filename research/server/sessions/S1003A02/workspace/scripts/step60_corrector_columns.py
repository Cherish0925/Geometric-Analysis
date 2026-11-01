"""
Step 60: exact W^- / Ric^o correctors by the COLUMN method (fast replacement of step59_exact_wminus_ric_correctors.py).

Y(K) = [sig^1] (linearised chiral curvature C' of g_B along h2 + sig K) is affine in the ansatz coefficients c.
Column n = Y(pt; c = e_n) - Y(pt; 0) is computed with all-rational numeric input (no symbolic c), at several
random rational points; then M c = -Y0 is solved exactly over Q.  A solution with Y == 0 at fresh points means the
sector's eps^2 log coefficient |Y|^2 vanishes identically (chiral-square argument, step59 note A.3).
Usage: python step60_corrector_columns.py [Wm|Rz|Rp] [npts]
Output: workspace/data/step60_correctors_<mode>.json
"""
import sys, os, json, time, random
from multiprocessing import Pool
import sympy as sp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step59_exact_log_coefficient import (X, r2, A_field, riemann_from_ops, h2_field, density_sig2, Jz)

HERE = os.path.dirname(os.path.abspath(__file__))
mode = sys.argv[1] if len(sys.argv) > 1 else 'Wm'
NPTS = int(sys.argv[2]) if len(sys.argv) > 2 else 5
OUT = os.path.join(HERE, '..', 'data', 'step60_correctors_%s.json' % mode)
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
    'sym(hJPJtA)': sym(H * J * Pm * J.T * A),
    'sym(JhP)/r4': sym(J * H * Pm) / r2 ** 2, 'sym(JhA)': sym(J * H * A), 'sym(hJ)': sym(H * J) / r2,
    'sym(JhJ)': sym(J * H * J) / r2, 'sym(JhPJt)/r4': sym(J * H * Pm * J.T) / r2 ** 2,
}
names = list(terms.keys())

def jets(M, pt):
    sub = dict(zip(X, pt))
    D1 = [[[sp.diff(M[i, j], X[k]) for k in range(4)] for j in range(4)] for i in range(4)]
    J0 = [[M[i, j].subs(sub) for j in range(4)] for i in range(4)]
    J1 = [[[D1[i][j][k].subs(sub) for k in range(4)] for j in range(4)] for i in range(4)]
    J2 = [[[[sp.diff(D1[i][j][k], X[l]).subs(sub) for l in range(4)] for k in range(4)] for j in range(4)]
          for i in range(4)]
    return J0, J1, J2

def Yvec(Aj, Hj, Tj):
    """Tj: jets of the corrector K (or None)."""
    def add(a, b): return a if b is None else a + sig * b
    P0 = [[add(Hj[0][i][j], None if Tj is None else Tj[0][i][j]) for j in range(4)] for i in range(4)]
    P1 = [[[add(Hj[1][i][j][k], None if Tj is None else Tj[1][i][j][k]) for k in range(4)] for j in range(4)]
          for i in range(4)]
    P2 = [[[[add(Hj[2][i][j][k][l], None if Tj is None else Tj[2][i][j][k][l]) for l in range(4)]
            for k in range(4)] for j in range(4)] for i in range(4)]
    dens, spr = density_sig2(Aj, [P0, P1, P2])
    Xm = density_sig2.last_X
    z0 = [sp.expand(Xm[I, Jn].coef(0, 0)) for I in range(6) for Jn in range(6)] + [sp.expand(spr.coef(0, 0))]
    assert all(z == 0 for z in z0), 'sector has nonzero C at sig^0'
    # In sectors with X0 = 0 the pair-basis X1 of density_sig2 carries a spurious antisymmetric part; the true
    # linearised W+ operator is the symmetric part (verified against the independent JAX orthonormal-frame density,
    # step60_jax_check.py: true sig^2 t^2 coefficient == 4|sym X1|^2 + s1^2/12).  Use sym X1 (upper triangle).
    X1 = [[sp.expand(Xm[I, Jn].coef(1, 0)) for Jn in range(6)] for I in range(6)]
    Ys = [sp.nsimplify((X1[I][Jn] + X1[Jn][I]) / 2) for I in range(6) for Jn in range(I, 6)]
    return Ys + [sp.nsimplify(sp.expand(spr.coef(1, 0)))], sp.expand(dens.coef(2, 0))

def work(args):
    pt, n = args
    Aj = jets(A, pt); Hj = jets(H, pt)
    Tj = None if n < 0 else jets(terms[names[n]], pt)
    return n, Yvec(Aj, Hj, Tj)

random.seed(3)
def rpt():
    return tuple(sp.Rational(random.randint(-7, 7), random.randint(1, 5)) for _ in range(4))

if __name__ == '__main__':
    t0 = time.time()
    rows_M, rows_b, pts = [], [], []
    with Pool(min(25, len(names) + 1)) as pool:
        for ip in range(NPTS + 2):
            pt = rpt(); pts.append(pt)
            out = dict(pool.map(work, [(pt, n) for n in range(-1, len(names))]))
            Y0, d0 = out[-1]
            cols = [[out[n][0][e] - Y0[e] for e in range(len(Y0))] for n in range(len(names))]
            if ip < NPTS:
                for e in range(len(Y0)):
                    rows_M.append([cols[n][e] for n in range(len(names))]); rows_b.append(-Y0[e])
            else:
                if ip == NPTS:
                    Mfull = sp.Matrix(rows_M); bfull = sp.Matrix(rows_b)
                    rM = Mfull.rank(); rMb = Mfull.row_join(bfull).rank()
                    print('rank M', rM, 'rank [M|b]', rMb, flush=True)
                    params = []
                    if rM == rMb:
                        csym = sp.symbols('c0:%d' % len(names))
                        sl = sp.linsolve((Mfull, bfull), *csym)
                        s0 = list(sl)[0]
                        params = sorted(set().union(*[sp.sympify(e).free_symbols for e in s0]), key=str)
                        sol = [sp.sympify(e).subs({p: 0 for p in params}) for e in s0]
                        print('solution found; free params', len(params), flush=True)
                    else:
                        sol = None; print('NO SOLUTION in ansatz', flush=True)
                if sol is not None:
                    resid = [Y0[e] + sum(sol[n] * cols[n][e] for n in range(len(names))) for e in range(len(Y0))]
                    print('fresh point', ip, 'Y==0:', all(sp.simplify(r_) == 0 for r_ in resid), flush=True)
            print('point', ip, 'time', time.time() - t0, flush=True)
    res = dict(mode=mode, names=names, n_eq=len(rows_b), time=time.time() - t0)
    if sol is not None:
        res['solution'] = {names[i]: str(sol[i]) for i in range(len(names)) if sol[i] != 0}
        res['free_params'] = len(params)
    else:
        res['solution'] = None
        # least-squares residual norm (float) to see how far the ansatz is
        import numpy as np
        Mf = np.array(Mfull.evalf(), dtype=float); bf = np.array(bfull.evalf(), dtype=float).ravel()
        x, *_ = np.linalg.lstsq(Mf, bf, rcond=None)
        res['lstsq_residual'] = float(np.linalg.norm(Mf @ x - bf)); res['b_norm'] = float(np.linalg.norm(bf))
        print('lstsq residual', res['lstsq_residual'], 'b norm', res['b_norm'])
    json.dump(res, open(OUT, 'w'), indent=1)
    print('saved', OUT, res['time'])
