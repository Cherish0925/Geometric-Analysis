#!/usr/bin/env python3
"""Step 76: formal prolongation of almost-Kaehler Einstein germs at a torsion zero.

Darboux gauge.  Omega = dx1^dx2 + dx3^dx4 is fixed, J0 e1=e2, J0 e3=e4.
Every metric compatible with Omega and close to delta is g = exp(H), H symmetric,
H J0 = -J0 H (6-dim fibre Sp(4)/U(2)); (g, Omega) is then automatically almost-Kaehler.
At a torsion zero one may gauge (quartic and lower Hamiltonian diffeos) H = O(|x|^2).
AKE  <=>  E(H) := Ric(exp H) - lam exp(H) = 0.
Order k of E:  L_k H_{k+2} + N_k(H_2..H_{k+1}) - lam [exp H]_k = 0,
L_k = flat linearized Ricci.  N_1 = 0; N_2 = Q(H_2,H_2) quadratic.
Obstructions at order k = coker(L_k) beyond the linearized Bianchi identity.

This script:
 (1) builds the 6-dim anti-J0 basis and the Hamiltonian gauge image on H_2;
 (2) solves order 0 (Ric(0) = lam delta) on H_2;
 (3) computes coker(L_2) and its Bianchi part, and the order-2 obstruction
     polynomials  <ell, Q(H_2) - lam H_2>  for ell in coker(L_2);
 (4) computes the linear torsion  a_k(x) = <nabla_k Omega, phi0>/2  from H_2 and its
     Jacobian determinant (the torsion-zero index, cf. Prop. 75.I);
 (5) saves everything needed for the analysis in step76_prolong_order2.json/.pkl
"""
import itertools, json, pickle, sys, time
from pathlib import Path
import sympy as sp

X = sp.symbols('x1:5')
lam = sp.Symbol('lam')
J0 = sp.Matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
OM = J0.T   # Omega_ij = (J^T g)_ij at g = delta;  Omega_12 = 1, Omega_34 = 1
DATA = Path(__file__).resolve().parents[1] / 'data'


def anti_basis():
    syms = sp.symbols('s0:10')
    S = sp.zeros(4, 4); k = 0
    for i in range(4):
        for j in range(i, 4):
            S[i, j] = S[j, i] = syms[k]; k += 1
    eqs = list(S*J0 + J0*S)
    sol = sp.linsolve(eqs, syms)
    (vec,) = sol
    free = sorted(set().union(*[sp.sympify(v).free_symbols for v in vec]), key=str)
    basis = []
    for f in free:
        sub = {g: (1 if g == f else 0) for g in free}
        M = S.subs(dict(zip(syms, [sp.sympify(v).subs(sub) for v in vec])))
        basis.append(M)
    return basis


def monos(d):
    out = []
    for e in itertools.product(range(d+1), repeat=4):
        if sum(e) == d:
            out.append(sp.Mul(*[X[i]**e[i] for i in range(4)]))
    return out


def trunc(expr, N):
    expr = sp.expand(expr)
    if expr == 0:
        return expr
    P = sp.Poly(expr, *X)
    return sum((c*sp.Mul(*[X[i]**m[i] for i in range(4)]) for m, c in P.terms() if sum(m) <= N), sp.Integer(0))


def homog(expr, d):
    expr = sp.expand(expr)
    if expr == 0:
        return expr
    P = sp.Poly(expr, *X)
    return sum((c*sp.Mul(*[X[i]**m[i] for i in range(4)]) for m, c in P.terms() if sum(m) == d), sp.Integer(0))


def matmul_tr(A, B, N):
    C = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            C[i, j] = trunc(sum(A[i, k]*B[k, j] for k in range(4)), N)
    return C


def ricci(H, N, lowdeg=2):
    """Ric of g = exp(H), H = O(x^lowdeg), truncated at degree N-2 (g needed to deg N)."""
    g = sp.eye(4) + H; ginv = sp.eye(4) - H
    Hp = H; fact = 1; sign = -1
    kmax = N // lowdeg
    for k in range(2, kmax+1):
        Hp = matmul_tr(Hp, H, N); fact *= k; sign = -sign
        g = g + Hp/fact
        ginv = ginv + sign*Hp/fact
    g = g.applyfunc(lambda e: trunc(e, N)); ginv = ginv.applyfunc(lambda e: trunc(e, N))
    dg = [[[trunc(sp.diff(g[i, j], X[k]), N-1) for k in range(4)] for j in range(4)] for i in range(4)]
    Gam = [[[None]*4 for _ in range(4)] for _ in range(4)]
    for k in range(4):
        for i in range(4):
            for j in range(i, 4):
                v = 0
                for l in range(4):
                    if ginv[k, l] != 0:
                        v += ginv[k, l]*(dg[l][i][j] + dg[l][j][i] - dg[i][j][l])
                v = trunc(v/2, N-1)
                Gam[k][i][j] = Gam[k][j][i] = v
    Ric = sp.zeros(4, 4)
    for i in range(4):
        for j in range(i, 4):
            v = 0
            for k in range(4):
                v += sp.diff(Gam[k][i][j], X[k]) - sp.diff(Gam[k][i][k], X[j])
                for l in range(4):
                    v += Gam[k][k][l]*Gam[l][i][j] - Gam[k][j][l]*Gam[l][i][k]
            Ric[i, j] = Ric[j, i] = trunc(v, N-2)
    return Ric, g, Gam


def coeff_vec(expr, d):
    expr = sp.expand(expr)
    ms = monos(d)
    if expr == 0:
        return [0]*len(ms)
    P = sp.Poly(expr, *X)
    dct = {m: c for m, c in P.terms()}
    out = []
    for mo in ms:
        e = sp.Poly(mo, *X).monoms()[0]
        out.append(dct.get(e, 0))
    return out


def sym_vec(M, d):
    v = []
    for i in range(4):
        for j in range(i, 4):
            v += coeff_vec(M[i, j], d)
    return v


def linear_ricci_matrix(basis, d):
    """Matrix of flat linearized Ricci: H_d (anti-J basis x monomials deg d) -> Ric deg d-2."""
    cols = []
    for B in basis:
        for m in monos(d):
            h = B*m
            R = sp.zeros(4, 4)
            for i in range(4):
                for j in range(4):
                    R[i, j] = sp.Rational(1, 2)*sum(sp.diff(h[k, j], X[k], X[i]) + sp.diff(h[k, i], X[k], X[j]) - sp.diff(h[i, j], X[k], X[k]) for k in range(4))
            cols.append(sym_vec(R, d-2))
    return sp.Matrix(cols).T


def bianchi_matrix(d):
    """Linearized contracted Bianchi on symmetric r of degree d: div r - 1/2 d tr r (deg d-1)."""
    cols = []
    for i in range(4):
        for j in range(i, 4):
            for m in monos(d):
                r = sp.zeros(4, 4); r[i, j] = r[j, i] = m
                b = [sum(sp.diff(r[k, l], X[k]) for k in range(4)) - sp.Rational(1, 2)*sp.diff(r.trace(), X[l]) for l in range(4)]
                v = []
                for l in range(4):
                    v += coeff_vec(b[l], d-1)
                cols.append(v)
    return sp.Matrix(cols).T


def gauge_image(basis, d):
    """Image of Hamiltonian fields X_f, f of degree d+1, on the H_d coefficient space."""
    # coordinates of H_d: sum_a sum_m c_{a,m} B_a m
    Bmat = []
    for B in basis:
        for m in monos(d):
            Bmat.append(sym_vec(B*m, d))
    Bmat = sp.Matrix(Bmat).T   # columns = basis elements in sym coordinates
    cols = []
    for f in monos(d+1):
        grad = sp.Matrix([sp.diff(f, xi) for xi in X])
        Xv = (OM.T).inv()*grad
        h = sp.zeros(4, 4)
        for i in range(4):
            for j in range(4):
                h[i, j] = sp.expand(sp.diff(Xv[j], X[i]) + sp.diff(Xv[i], X[j]))
        cols.append(sym_vec(h, d))
    G = sp.Matrix(cols).T
    # express in H-coordinates
    sol = Bmat.solve_least_squares(G) if False else None
    coords = (Bmat.T*Bmat).inv()*Bmat.T*G
    assert (Bmat*coords - G).is_zero_matrix, 'gauge field not anti-J'
    return coords


def main():
    t0 = time.time()
    basis = anti_basis()
    assert len(basis) == 6
    m2 = monos(2)
    nH2 = 6*len(m2)
    c = sp.symbols('c0:%d' % nH2)
    H2 = sp.zeros(4, 4)
    for a, B in enumerate(basis):
        for mi, m in enumerate(m2):
            H2 += c[a*len(m2)+mi]*B*m
    H2 = H2.applyfunc(sp.expand)
    Ric, g, Gam = ricci(H2, 4)
    # order 0
    eq0 = []
    for i in range(4):
        for j in range(i, 4):
            eq0.append(sp.expand(homog(Ric[i, j], 0) - lam*(1 if i == j else 0)))
    # order 1 must vanish identically (N_1 = 0, H_3 absent here)
    for i in range(4):
        for j in range(4):
            assert homog(Ric[i, j], 1) == 0
    # order-2 nonlinear part
    Q2 = sp.zeros(4, 4)
    for i in range(4):
        for j in range(i, 4):
            Q2[i, j] = Q2[j, i] = sp.expand(homog(Ric[i, j], 2) - lam*H2[i, j])
    L2 = linear_ricci_matrix(basis, 4)
    Bi = bianchi_matrix(2)
    print('L2 shape', L2.shape, 'rank', L2.rank(), 'time', time.time()-t0, flush=True)
    cok = L2.T.nullspace()     # left null vectors: ell^T L2 = 0
    print('coker dim', len(cok), flush=True)
    bianchi_rows = Bi.rank()
    print('Bianchi rank', bianchi_rows, flush=True)
    q2vec = sp.Matrix(sym_vec(Q2, 2))
    obstr = [sp.expand((ell.T*q2vec)[0]) for ell in cok]
    # linear torsion a_k(x)
    phi0 = sp.zeros(4, 4); phi0[0, 2] = 1; phi0[2, 0] = -1; phi0[1, 3] = -1; phi0[3, 1] = 1
    a = []
    for k in range(4):
        tot = 0
        for i in range(4):
            for j in range(4):
                T = -sum(homog(Gam[l][k][i], 1)*OM[l, j] + homog(Gam[l][k][j], 1)*OM[i, l] for l in range(4))
                tot += T*phi0[i, j]
        a.append(sp.expand(tot/4))   # <T_k, phi0> = 1/2 sum_ij ; a_k = <.,.>/2
    Ja = sp.Matrix([[sp.diff(a[k], X[m]) for m in range(4)] for k in range(4)])
    # also the Jphi0 component should give J-rotated a (sanity): skip
    gimg = gauge_image(basis, 2)
    res = {'nH2': nH2, 'eq0': [str(e) for e in eq0], 'coker_dim': len(cok), 'bianchi_rank_on_deg2': bianchi_rows,
           'L2_rank': L2.rank(), 'n_obstr': len(obstr), 'time': time.time()-t0}
    with open(DATA/'step76_prolong_order2.pkl', 'wb') as fh:
        pickle.dump({'basis': basis, 'c': c, 'eq0': eq0, 'obstr': obstr, 'cok': cok, 'Bi': Bi,
                     'a': a, 'Ja': Ja, 'gimg': gimg, 'Q2': Q2}, fh)
    (DATA/'step76_prolong_order2.json').write_text(json.dumps(res, indent=1)+'\n')
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
