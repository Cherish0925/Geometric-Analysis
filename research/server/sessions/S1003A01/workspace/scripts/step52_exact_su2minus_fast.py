"""Step 52a (fast exact version): EXACT rational quadratic form of the perpendicular-Burns log coefficient F for an
arbitrary Einstein 2-jet with W^- = 0 (s, W+ = w general; w23 = 0 by a U(1)_+ rotation), over the full
10-dimensional SU(2)_- -invariant degree-0 corrector space.

Why exact at one point: with W^-_p = Ric0_p = 0 all ingredients are SU(2)_- -equivariant and SU(2)_- acts
transitively on S^3, so the a^2 eps^2 CGB density is constant on S^3 and F = density(x0)/4.
(Convexity + averaging: inf over any SU(2)_- -stable degree-0 corrector class = inf over the 10 invariant
tensors sym(v_i v_j^T)/u, v_0 = x, v_m = J_m x.)

F is a homogeneous quadratic form in v = (s, w11, w22, w12, w13, c_0..c_9) (jet and corrector both carry the
amplitude a). It is recovered EXACTLY by polarization, each evaluation done in exact rational arithmetic with
truncated bivariate polynomials in (a, eps) (degrees <= 2 each). Same curvature pipeline/conventions as
step51_exact_u2_locus.py (validated there against Step 49/51 numerics).
Output: workspace/data/step52/exact_su2minus_Q.json  (Q, analysis in step52_analyze_Q.py)
"""
import os, sys, json, time, itertools
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", os.environ.get("OUTDIR", "step52")); os.makedirs(OUT, exist_ok=True)

# ---------------- symbolic jets at x0 of the basis pieces (rational) ----------------
x = sp.symbols('x0:4', real=True)
X = sp.Matrix(x)
def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return [a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2, a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2]
E4 = sp.eye(4)
Jm = [sp.zeros(4, 4) for _ in range(3)]
for cc in range(4):
    for b in range(4):
        pc = [E4[cc, i] for i in range(4)]; pc = [pc[0], -pc[1], -pc[2], -pc[3]]
        prod = qmul(pc, [E4[b, i] for i in range(4)])
        for m in range(3):
            Jm[m][b, cc] = prod[m+1]
v = [Jm[m]*X for m in range(3)]
V = [X] + v
u = sum(xi**2 for xi in x)
# jet pieces: h2 = s*H_s + w11*H_11 + w22*H_22 + w12*H_12 + w13*H_13
def vv(m, n): return v[m]*v[n].T
H_s = -sp.Rational(1, 36)*sum((vv(m, m) for m in range(3)), sp.zeros(4, 4))
H_11 = -sp.Rational(1, 6)*(vv(0, 0) - vv(2, 2))
H_22 = -sp.Rational(1, 6)*(vv(1, 1) - vv(2, 2))
H_12 = -sp.Rational(1, 6)*(vv(0, 1) + vv(1, 0))
H_13 = -sp.Rational(1, 6)*(vv(0, 2) + vv(2, 0))
JET = [H_s, H_11, H_22, H_12, H_13]
COR = []; CNAMES = []
for i in range(4):
    for j in range(i, 4):
        COR.append((V[i]*V[j].T + V[j]*V[i].T)/(2*u)); CNAMES.append(f"sym(v{i}v{j})/u")
kB = (v[0]*v[0].T + v[1]*v[1].T)/u**2
x0 = {x[0]: 1, x[1]: 0, x[2]: 0, x[3]: 0}

def jets_num(M):
    g0 = np.empty((4, 4), dtype=object); d1 = np.empty((4, 4, 4), dtype=object); d2 = np.empty((4, 4, 4, 4), dtype=object)
    for i in range(4):
        for j in range(4):
            g0[i, j] = Fr(str(sp.nsimplify(M[i, j].subs(x0))))
            for k in range(4):
                dk = sp.diff(M[i, j], x[k])
                d1[i, j, k] = Fr(str(dk.subs(x0)))
                for l in range(4):
                    d2[i, j, k, l] = Fr(str(sp.diff(dk, x[l]).subs(x0)))
    return g0, d1, d2

NV = 15

# ---------------- truncated bivariate polynomial tensors: dict {(i,j): ndarray(object)} ----------------
TR = 2
def tp_add(*As):
    out = {}
    for A in As:
        for k, val in A.items():
            out[k] = out[k] + val if k in out else val
    return out
def tp_scale(A, c): return {k: val*c for k, val in A.items()}
def tp_dot(A, B, axes):
    out = {}
    for (i1, j1), a_ in A.items():
        for (i2, j2), b_ in B.items():
            i, j = i1+i2, j1+j2
            if i > TR or j > TR: continue
            val = np.tensordot(a_, b_, axes=axes)
            out[(i, j)] = out[(i, j)] + val if (i, j) in out else val
    return out
def tp_mul_scalar(A, B):   # elementwise product of same-shape tensors
    out = {}
    for (i1, j1), a_ in A.items():
        for (i2, j2), b_ in B.items():
            i, j = i1+i2, j1+j2
            if i > TR or j > TR: continue
            val = a_*b_
            out[(i, j)] = out[(i, j)] + val if (i, j) in out else val
    return out
def tp_T(A, perm): return {k: np.transpose(val, perm) for k, val in A.items()}

def zeros(shape): return np.full(shape, Fr(0), dtype=object)

PRE = None
def setup():
    global PRE
    if PRE is None:
        PRE = dict(jet=[jets_num(M) for M in JET], cor=[jets_num(M) for M in COR], kB=jets_num(kB))
    return PRE

PAIRS = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
Jv = np.empty((3, 6), dtype=object)
for m in range(3):
    row = [Jm[m][a_, b_] for (a_, b_) in PAIRS]
    nrm2 = sum(r**2 for r in row)          # = 2
    for i in range(6):
        Jv[m, i] = Fr(int(row[i]))
# normalization 1/sqrt(2) per row -> factor 1/2 overall in Jv M Jv^T
def evaluate(vec):
    P = setup()
    vec = [Fr(z) for z in vec]
    jet = P["jet"]; cor = P["cor"]; kb = P["kB"]
    def comb(idx, lst, coefs):
        return sum((c*lst[k][idx] for k, c in enumerate(coefs)), zeros(lst[0][idx].shape))
    g = {(0, 0): np.array([[Fr(int(i == j)) for j in range(4)] for i in range(4)], dtype=object),
         (1, 0): comb(0, jet, vec[:5]), (0, 1): kb[0], (1, 1): comb(0, cor, vec[5:])}
    dg = {(1, 0): comb(1, jet, vec[:5]), (0, 1): kb[1], (1, 1): comb(1, cor, vec[5:])}
    ddg = {(1, 0): comb(2, jet, vec[:5]), (0, 1): kb[2], (1, 1): comb(2, cor, vec[5:])}
    I = g[(0, 0)]
    H = {k: val for k, val in g.items() if k != (0, 0)}
    # inverse
    gi = {(0, 0): I}; Hp = {(0, 0): I}
    for n in range(1, 5):
        Hp = tp_dot(Hp, H, ([1], [0])); gi = tp_add(gi, tp_scale(Hp, (-1)**n))
    BIN = [Fr(1), Fr(-1, 2), Fr(3, 8), Fr(-5, 16), Fr(35, 128)]
    ef = {(0, 0): I}; Hp = {(0, 0): I}
    for n in range(1, 5):
        Hp = tp_dot(Hp, H, ([1], [0])); ef = tp_add(ef, tp_scale(Hp, BIN[n]))
    # lowered Christoffel Gl[d][b][c] = 1/2(dg[d,c,b] + dg[d,b,c] - dg[b,c,d])   (dg[i,j,k] = d_k g_ij)
    Gl = {}
    for k, val in dg.items():
        A = zeros((4, 4, 4))
        for d_, b_, c_ in itertools.product(range(4), repeat=3):
            A[d_, b_, c_] = Fr(1, 2)*(val[d_, c_, b_] + val[d_, b_, c_] - val[b_, c_, d_])
        Gl[k] = A
    Gam = tp_dot(gi, Gl, ([1], [0]))                       # Gam[A,b,c]
    # dgi[A,d,k] = - gi[A,m] dg[m,n,k] gi[n,d]
    t1 = tp_dot(gi, dg, ([1], [0]))                        # [A,n,k]
    dgi = tp_scale(tp_T(tp_dot(t1, gi, ([1], [0])), (0, 2, 1)), -1)   # t1·gi -> [A,k,d] -> [A,d,k]
    dGl = {}
    for k, val in ddg.items():
        A = zeros((4, 4, 4, 4))
        for d_, b_, c_, E_ in itertools.product(range(4), repeat=4):
            A[d_, b_, c_, E_] = Fr(1, 2)*(val[d_, c_, b_, E_] + val[d_, b_, c_, E_] - val[b_, c_, d_, E_])
        dGl[k] = A
    # dGam[A,b,c,E] = dgi[A,d,E] Gl[d,b,c] + gi[A,d] dGl[d,b,c,E]
    tA = tp_T(tp_dot(dgi, Gl, ([1], [0])), (0, 2, 3, 1))   # [A,E,b,c] -> [A,b,c,E]
    tB = tp_dot(gi, dGl, ([1], [0]))
    dGam = tp_add(tA, tB)
    # Rup[A,b,c,d] = dGam[A,d,b,c] - dGam[A,c,b,d] + Gam[A,c,E]Gam[E,d,b] - Gam[A,d,E]Gam[E,c,b]
    GG = tp_dot(Gam, Gam, ([2], [0]))                       # [A,c,d,b] = Gam[A,c,E]Gam[E,d,b]
    Rup = {}
    keys = set(dGam) | set(GG)
    for k in keys:
        A = zeros((4, 4, 4, 4))
        dG = dGam.get(k); G2 = GG.get(k)
        for A_, b_, c_, d_ in itertools.product(range(4), repeat=4):
            val = Fr(0)
            if dG is not None:
                val += dG[A_, d_, b_, c_] - dG[A_, c_, b_, d_]
            if G2 is not None:
                val += G2[A_, c_, d_, b_] - G2[A_, d_, c_, b_]
            A[A_, b_, c_, d_] = val
        Rup[k] = A
    Rl = tp_dot(g, Rup, ([1], [0]))                         # lower first index
    Rf = Rl
    for pos in range(4):
        # contract slot pos with ef[i, new]
        perm_back = list(range(4))
        Rf = tp_dot(Rf, ef, ([pos], [0]))                   # moves contracted slot to end
        order = list(range(3)); order.insert(pos, 3)
        Rf = tp_T(Rf, order)
    Ric = {k: np.einsum('abad->bd', val) if False else sum(val[a_, :, a_, :] for a_ in range(4)) for k, val in Rf.items()}
    sc = {k: sum(val[i, i] for i in range(4)) for k, val in Ric.items()}
    # Weyl and W+
    Wp = {}
    for k in Rf:
        R = Rf[k]; Rc = Ric[k]; s_ = sc[k]
        M = zeros((6, 6))
        dl = lambda i, j: 1 if i == j else 0
        for I_, (a_, b_) in enumerate(PAIRS):
            for J_, (c_, d_) in enumerate(PAIRS):
                M[I_, J_] = (R[a_, b_, c_, d_] - Fr(1, 2)*(dl(a_, c_)*Rc[b_, d_] - dl(a_, d_)*Rc[b_, c_] - dl(b_, c_)*Rc[a_, d_] + dl(b_, d_)*Rc[a_, c_])
                             + s_/6*(dl(a_, c_)*dl(b_, d_) - dl(a_, d_)*dl(b_, c_)))
        Wp[k] = Fr(1, 2)*np.dot(np.dot(Jv, M), Jv.T)
    W2 = tp_mul_scalar(Wp, Wp); W2 = {k: sum(val.flat) for k, val in W2.items()}
    S2 = tp_mul_scalar(sc, sc)
    dens = tp_add({k: 4*val for k, val in W2.items()}, {k: val/12 for k, val in S2.items()})
    # sqrt det g
    def entry(i, j): return {k: val[i, j] for k, val in g.items()}
    det = {}
    for perm in itertools.permutations(range(4)):
        sgn = 1
        p = list(perm)
        for i in range(4):
            for j in range(i+1, 4):
                if p[i] > p[j]: sgn = -sgn
        term = entry(0, perm[0])
        for i in range(1, 4):
            term = tp_mul_scalar(term, entry(i, perm[i]))
        det = tp_add(det, tp_scale(term, sgn))
    D = {k: val for k, val in det.items() if k != (0, 0)}
    sq = {(0, 0): Fr(1)}; Dp = {(0, 0): Fr(1)}
    for n, bc in enumerate([Fr(1, 2), Fr(-1, 8), Fr(1, 16), Fr(-5, 128)], start=1):
        Dp = tp_mul_scalar(Dp, D); sq = tp_add(sq, tp_scale(Dp, bc))
    f = tp_mul_scalar(dens, sq)
    F22 = Fr(f.get((2, 2), 0))/4
    F11 = Fr(f.get((1, 1), 0))
    F02 = Fr(f.get((0, 2), 0))
    Wa = Wp.get((1, 0)); sa = sc.get((1, 0))
    return F22, F11, F02, Wa, sa

def ev_task(vec):
    F22, F11, F02, Wa, sa = evaluate(vec)
    return F22, F11, F02

def main():
    t0 = time.time()
    setup()
    print("setup", time.time()-t0, flush=True)
    # normalization check: s = -24, w = CH (2,-4,2) -> w11=2, w22=-4 ; jet amplitude check
    vec = [Fr(-24), Fr(2), Fr(-4), Fr(0), Fr(0)] + [Fr(0)]*10
    F22, F11, F02, Wa, sa = evaluate(vec)
    print("CH kB-only F =", F22, " (expect 12)  [a eps]=", F11, " W+[a]=", Wa.tolist(), " s[a]=", sa, time.time()-t0, flush=True)
    basis = []
    for i in range(NV):
        e_ = [0]*NV; e_[i] = 1; basis.append(e_)
    pairs = [(i, j) for i in range(NV) for j in range(i+1, NV)]
    vecs = basis + [[basis[i][k] + basis[j][k] for k in range(NV)] for (i, j) in pairs]
    nproc = int(os.environ.get("NPROC", "32"))
    with Pool(nproc) as pool:
        outs = pool.map(ev_task, vecs, chunksize=1)
    diag = [outs[i][0] for i in range(NV)]
    Q = [[Fr(0)]*NV for _ in range(NV)]
    for i in range(NV): Q[i][i] = diag[i]
    for n, (i, j) in enumerate(pairs):
        val = (outs[NV+n][0] - diag[i] - diag[j])/2
        Q[i][j] = Q[j][i] = val
    aeps = [str(o[1]) for o in outs]
    res = {"vars": ["s", "w11", "w22", "w12", "w13"] + [f"c{i}:{nm}" for i, nm in enumerate(CNAMES)],
           "Q": [[str(z) for z in row] for row in Q],
           "a_eps_all_zero": all(o[1] == 0 for o in outs),
           "pure_burns_eps2_all_zero": all(o[2] == 0 for o in outs),
           "CH_check": {"F_kB_only": str(F22), "W+_[a]": [[str(z) for z in r] for r in Wa.tolist()], "s_[a]": str(sa)},
           "time_s": time.time()-t0}
    json.dump(res, open(os.path.join(OUT, "exact_su2minus_Q.json"), "w"), indent=1)
    print(json.dumps({k: v_ for k, v_ in res.items() if k != "Q"}, indent=1))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        setup()
        t0 = time.time()
        print(evaluate([Fr(-24), Fr(2), Fr(-4), Fr(0), Fr(0)] + [Fr(0)]*10)[:3], time.time()-t0)
    else:
        main()
