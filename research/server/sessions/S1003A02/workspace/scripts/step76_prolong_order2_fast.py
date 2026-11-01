#!/usr/bin/env python3
"""Step 76: order-2 prolongation of AKE germs at a torsion zero (Darboux gauge, exact).

See step76_ake_prolong.py docstring for the formulation.  Uses step76_polyseries (Fractions).
Output: workspace/data/step76_prolong_order2.json (+ .pkl with exact objects)
"""
import json, pickle, sys, time
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from step76_polyseries import *

DATA = Path(__file__).resolve().parents[1] / 'data'
J0 = [[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]]
OM = [[J0[j][i] for j in range(4)] for i in range(4)]   # Omega = J0^T ; Omega_12 = 1
PHI0 = [[0]*4 for _ in range(4)]
PHI0[0][2] = 1; PHI0[2][0] = -1; PHI0[1][3] = -1; PHI0[3][1] = 1   # dx13 - dx24
JPHI0 = [[0]*4 for _ in range(4)]
JPHI0[0][3] = 1; JPHI0[3][0] = -1; JPHI0[1][2] = 1; JPHI0[2][1] = -1   # dx14 + dx23


def anti_basis():
    s = sp.symbols('s0:10'); S = sp.zeros(4, 4); k = 0
    for i in range(4):
        for j in range(i, 4):
            S[i, j] = S[j, i] = s[k]; k += 1
    J = sp.Matrix(J0)
    sol = sp.solve(list(S*J + J*S), s, dict=True)[0]
    Sg = S.subs(sol)
    free = sorted(Sg.free_symbols, key=str)
    out = []
    for f in free:
        M = Sg.subs({g: (1 if g == f else 0) for g in free})
        out.append([[int(M[i, j]) for j in range(4)] for i in range(4)])
    return out


def basis_H(Bs, d):
    out = []
    for B in Bs:
        for m in monos(d):
            Z = zero()
            for i in range(4):
                for j in range(4):
                    if B[i][j]:
                        Z[i][j] = {m: F(B[i][j])}
            out.append(Z)
    return out


def comb(vecs, coeffs):
    Z = zero()
    for v, c in zip(vecs, coeffs):
        if c != 0:
            Z = madd(Z, mscale(v, F(c)))
    return Z


def torsion_lin(H2):
    """a_k(x) linear part from H2: returns 4x4 matrix D[k][m] = d a_k / d x_m, and the Jphi0 analogue."""
    g, gi = exp_series(H2, 3)
    G = christoffel(g, gi, 3)
    D = [[F(0)]*4 for _ in range(4)]; D2 = [[F(0)]*4 for _ in range(4)]
    for k in range(4):
        for i in range(4):
            for j in range(4):
                T = {}
                for l in range(4):
                    T = padd(T, pscale(phom(G[l][k][i], 1), F(OM[l][j])), -1)
                    T = padd(T, pscale(phom(G[l][k][j], 1), F(OM[i][l])), -1)
                for m in range(4):
                    e = [0]*4; e[m] = 1
                    D[k][m] += T.get(tuple(e), F(0))*PHI0[i][j]/4
                    D2[k][m] += T.get(tuple(e), F(0))*JPHI0[i][j]/4
    return D, D2


def main():
    t0 = time.time()
    Bs = anti_basis(); assert len(Bs) == 6
    B2 = basis_H(Bs, 2); n2 = len(B2)
    # order-0 linear map and torsion map on H2
    L0cols = []; Torcols = []
    for e in B2:
        R, g, G = ricci_exp(e, 2)
        L0cols.append([R[i][j].get((0, 0, 0, 0), F(0)) for i in range(4) for j in range(i, 4)])
        D, D2 = torsion_lin(e)
        Torcols.append([D[k][m] for k in range(4) for m in range(4)])
    L0 = sp.Matrix(L0cols).T; Tor = sp.Matrix(Torcols).T
    delta = sp.Matrix([1 if i == j else 0 for i in range(4) for j in range(i, 4)])
    print('L0 rank', L0.rank(), 'Tor rank', Tor.rank(), time.time()-t0, flush=True)
    # gauge image on H2: f quartic
    Gcols = []
    for f in monos(4):
        Xv = [{} for _ in range(4)]
        # iota_X Omega = df: X^i Omega_ij = d_j f  -> X = (Omega^T)^{-1} grad f ; Omega^T = J0 ; J0^{-1} = -J0
        grad = [pdiff({f: F(1)}, j) for j in range(4)]
        for i in range(4):
            acc = {}
            for j in range(4):
                if J0[i][j]:
                    acc = padd(acc, pscale(grad[j], F(-J0[i][j])))
            Xv[i] = acc
        h = zero()
        for i in range(4):
            for j in range(4):
                h[i][j] = padd(pdiff(Xv[j], i), pdiff(Xv[i], j))
        Gcols.append(sym_vec(h, 2))
    Gm = sp.Matrix(Gcols).T
    Bm = sp.Matrix([sym_vec(e, 2) for e in B2]).T
    Gco = (Bm.T*Bm).inv()*Bm.T*Gm
    assert (Bm*Gco - Gm).is_zero_matrix
    print('gauge rank', Gco.rank(), 'L0*gauge zero', (L0*Gco).is_zero_matrix, 'Tor*gauge zero', (Tor*Gco).is_zero_matrix, flush=True)
    # particular torsion-free solution of L0 h = delta
    A = L0.col_join(Tor); rhs = delta.col_join(sp.zeros(16, 1))
    sol, params = A.gauss_jordan_solve(rhs)
    hp = sol.subs({p: 0 for p in params})
    # kernel of L0 modulo gauge: complement inside ker L0 orthogonal to gauge image
    K0 = L0.nullspace()
    Gsp = Gco.columnspace()
    M = sp.Matrix.hstack(*K0)
    # vectors v in ker L0 with v . g = 0 for all gauge g
    Gt = sp.Matrix.hstack(*Gsp).T
    coef = (Gt*M).nullspace()
    C = [M*c for c in coef]
    print('ker L0', len(K0), 'complement dim', len(C), time.time()-t0, flush=True)
    vecs = [hp] + C
    Hv = [comb(B2, list(v)) for v in vecs]
    nv = len(Hv)
    # quadratic Ricci at degree 2, polarization
    def ric2(H):
        R, g, G = ricci_exp(H, 4)
        return sp.Matrix(sym_vec([[phom(R[i][j], 2) for j in range(4)] for i in range(4)], 2))
    Qd = {}
    for a in range(nv):
        Qd[(a, a)] = ric2(Hv[a])
    for a in range(nv):
        for b in range(a+1, nv):
            Qd[(a, b)] = (ric2(madd(Hv[a], Hv[b])) - Qd[(a, a)] - Qd[(b, b)])/2
    print('Q computed', time.time()-t0, flush=True)
    # L2 and coker
    B4 = basis_H(Bs, 4)
    L2 = sp.Matrix([ric2(e).T.tolist()[0] for e in B4]).T
    cok = L2.T.nullspace()
    print('L2', L2.shape, 'rank', L2.rank(), 'coker', len(cok), time.time()-t0, flush=True)
    # Bianchi part of coker
    bcols = []
    for i in range(4):
        for j in range(i, 4):
            for m in monos(2):
                r = zero(); r[i][j] = {m: F(1)}; r[j][i] = {m: F(1)}
                tr = {}
                for k in range(4):
                    tr = padd(tr, r[k][k])
                b = []
                for l in range(4):
                    acc = {}
                    for k in range(4):
                        acc = padd(acc, pdiff(r[k][l], k))
                    acc = padd(acc, pscale(pdiff(tr, l), F(1, 2)), -1)
                    b += [acc.get(mm, F(0)) for mm in monos(1)]
                bcols.append(b)
    Bi = sp.Matrix(bcols).T          # 16 x 100
    # the coker vectors are expressed w.r.t. sym_vec coordinates with r_ij for i<=j (off-diagonal stored once)
    # Bianchi functional on stored coords must weight off-diagonals: r_ij appears twice in div; our bcols already set both entries.
    cokM = sp.Matrix.hstack(*cok)
    bi_rank = Bi.rank(); joint = sp.Matrix.vstack(cokM.T, Bi).rank()
    print('Bianchi rank', bi_rank, 'joint rank coker+Bianchi', joint, flush=True)
    # extra coker: complement of Bianchi rows inside coker span
    lam = sp.Symbol('lam'); t = sp.symbols('t1:%d' % nv)
    var = [lam] + list(t)
    obs = []
    for ell in cok:
        expr = 0
        for (a, b), q in Qd.items():
            val = (ell.T*q)[0]
            if val == 0:
                continue
            mult = 1 if a == b else 2
            expr += mult*val*var[a]*var[b]
        # linear term -lam*H2 at degree 2:  H2 = lam*hp + sum t C
        H2vec = sum((var[a]*sp.Matrix(sym_vec(Hv[a], 2)) for a in range(nv)), sp.zeros(100, 1))
        expr -= lam*(ell.T*H2vec)[0]
        obs.append(sp.expand(expr))
    # torsion of the complement directions
    TorC = [[sp.Rational(x) for x in (Tor*v)] for v in vecs]
    res = {'L0_rank': int(L0.rank()), 'Tor_rank_full': int(Tor.rank()), 'gauge_rank': int(Gco.rank()),
           'kerL0': len(K0), 'complement': len(C), 'L2_rank': int(L2.rank()), 'coker': len(cok),
           'bianchi_rank': int(bi_rank), 'coker_plus_bianchi_rank': int(joint),
           'obstructions': [str(o) for o in obs], 'torsion_of_vecs': [[str(x) for x in r] for r in TorC],
           'time': time.time()-t0}
    (DATA/'step76_prolong_order2.json').write_text(json.dumps(res, indent=1)+'\n')
    with open(DATA/'step76_prolong_order2.pkl', 'wb') as fh:
        pickle.dump({'Bs': Bs, 'vecs': vecs, 'obs': obs, 'TorC': TorC, 'cok': cok, 'Bi': Bi, 'L0': L0, 'Tor': Tor}, fh)
    print(json.dumps({k: v for k, v in res.items() if k not in ('obstructions', 'torsion_of_vecs')}, indent=1))
    for o in obs:
        print('OBS', o)


if __name__ == '__main__':
    main()
