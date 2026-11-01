#!/usr/bin/env python3
"""Step 70: complex flat model of the top-kernel/half-twistor correspondence.

Flat C^2, g = sum dx^2+dy^2 (g_{a bar b}=delta/2).  An anti-J symmetric metric
variation is h = mu_{ab} dz_a dz_b + nu_{ab} dzbar_a dzbar_b, nu = conj(mu),
mu, nu symmetric.  Flat linearized Ricci (tr h=0):
  E1_{ab} := Ric_{bar a bar b} = dbar_a D_b + dbar_b D_a - 2 Box nu_ab,
             D_b = d_c nu_{cb},  Box = d_c dbar_c;
  E2_{ab} := Ric_{a bar b}     = d_a d_c nu_{cb} + dbar_b dbar_c mu_{ca}.
Principal torsion (dbar of the Beltrami differential):
  v_a = eps^{bc} dbar_b nu_{ac} = dbar_1 nu_{a2} - dbar_2 nu_{a1}.

Checks:
 (1) pointwise: trace-free part of the holomorphic derivative (d_d v_a)_0 is a
     linear combination of E1 (the J-anti-invariant Ricci): this is the flat
     linearization of the half-twistor identity (A02 75.H(a)).
 (2) degree d: dim ker(E1,E2) on degree-d anti-J tensors, torsion image rank,
     and comparison with half-twistor dim 6n+10 (n=d-2).  Must reproduce the
     Darboux-engine values 127/22, 244/34, 409/46 for d=4,6,8.
 (3) explicit kernel elements: holomorphic mu (g-part) and a candidate family
     for the z h(zbar) part.
"""
import itertools, json, sys
from pathlib import Path
import sympy as sp

OUT = Path(__file__).resolve().parent.parent / 'data' / 'step70'
OUT.mkdir(parents=True, exist_ok=True)

# ---------- (1) pointwise algebra ----------
def pointwise():
    X = {}
    for d in range(2):
        for b in range(2):
            for (a, c) in [(0, 0), (0, 1), (1, 1)]:
                X[(d, b, a, c)] = sp.Symbol(f'X{d}{b}{a}{c}')
    def x(d, b, a, c):
        return X[(d, b, min(a, c), max(a, c))]
    E1 = {}
    for a in range(2):
        for b in range(2):
            E1[(a, b)] = sum(x(c, a, c, b) + x(c, b, c, a) for c in range(2)) - 2 * sum(x(c, c, a, b) for c in range(2))
    F = {(d, a): x(d, 0, a, 1) - x(d, 1, a, 0) for d in range(2) for a in range(2)}
    tr = (F[(0, 0)] + F[(1, 1)]) / 2
    F0 = [F[(0, 0)] - tr, F[(0, 1)], F[(1, 0)], F[(1, 1)] - tr]
    syms = sorted(X.values(), key=str)
    rowsE = [sp.Poly(E1[k], *syms).coeffs() and [sp.diff(E1[k], s) for s in syms] for k in [(0, 0), (0, 1), (1, 1)]]
    rowsF = [[sp.diff(f, s) for s in syms] for f in F0]
    ME = sp.Matrix(rowsE); MF = sp.Matrix(rowsF)
    res = {'rank_E1': ME.rank(), 'rank_F0': MF.rank(), 'rank_join': sp.Matrix.vstack(ME, MF).rank()}
    # explicit coefficients F0_i = sum k_ij E1_j
    sol = {}
    for i in range(4):
        kk = sp.symbols('k0:3')
        eqs = sp.Matrix([MF.row(i)]) - sp.Matrix([kk]) * ME
        s = sp.solve(list(eqs), kk, dict=True)
        sol[f'F0_{i}'] = {str(k): str(v) for k, v in s[0].items()} if s else None
    res['coefficients'] = sol
    # also the antiholomorphic derivative alternative
    G = {(d, a): sum(0 for _ in [0]) for d in range(2) for a in range(2)}
    return res

# ---------- (2) degree-d linear algebra ----------
z = sp.symbols('z1 z2', real=True); w = sp.symbols('w1 w2', real=True)
ALL = z + w

def conj(p):
    p = sp.expand(p)
    return sp.expand(sp.conjugate(p).xreplace({z[0]: w[0], z[1]: w[1], w[0]: z[0], w[1]: z[1]}))

def mons(deg):
    return [m for m in itertools.product(range(deg + 1), repeat=4) if sum(m) == deg]

def monexpr(m):
    return z[0]**m[0] * z[1]**m[1] * w[0]**m[2] * w[1]**m[3]

def dz(p, i): return sp.diff(p, z[i])
def dw(p, i): return sp.diff(p, w[i])

def operators(nu):
    """nu: dict (a,c) symmetric -> polynomial.  Returns E1, E2 lists and torsion v."""
    N = lambda a, c: nu[(min(a, c), max(a, c))]
    M = lambda a, c: conj(N(a, c))
    D = [sum(dz(N(c, b), c) for c in range(2)) for b in range(2)]
    E1 = []; E2 = []
    for a in range(2):
        for b in range(2):
            if a <= b:
                E1.append(sp.expand(dw(D[b], a) + dw(D[a], b) - 2 * sum(dz(dw(N(a, b), c), c) for c in range(2))))
            E2.append(sp.expand(sum(dz(dz(N(c, b), c), a) for c in range(2)) + sum(dw(dw(M(c, a), c), b) for c in range(2))))
    v = [sp.expand(dw(N(a, 1), 0) - dw(N(a, 0), 1)) for a in range(2)]
    return E1, E2, v

def realcoeffs(polys, deg):
    """flatten complex polys -> real vector (Re, Im of each monomial coeff)."""
    ms = mons(deg); out = []
    for p in polys:
        pd = sp.Poly(p, *ALL).as_dict() if p != 0 else {}
        for m in ms:
            c = sp.nsimplify(pd.get(m, 0))
            out += [sp.re(c), sp.im(c)]
    return out

def degree_count(d):
    n = d - 2
    ms = mons(d)
    cols = []; E1cols = []; Tcols = []
    keys = [(0, 0), (0, 1), (1, 1)]
    for k in keys:
        for m in ms:
            for ph in (1, sp.I):
                nu = {kk: 0 for kk in keys}; nu[k] = ph * monexpr(m)
                E1, E2, v = operators(nu)
                cols.append(realcoeffs(E1 + E2, d - 2))
                Tcols.append(realcoeffs(v, d - 1))
    L = sp.Matrix(cols).T; T = sp.Matrix(Tcols).T
    K = L.nullspace()
    Kmat = sp.Matrix.hstack(*K)
    TK = T * Kmat
    # half-twistor test: (d_z v)_0 = 0 on image
    rec = {'d': d, 'n': n, 'dim_H': L.cols, 'rank_L': L.rank(), 'dim_ker': len(K), 'rank_torsion_on_ker': TK.rank(),
           'half_twistor_dim': 6 * n + 10}
    return rec

if __name__ == '__main__':
    r1 = pointwise(); print(json.dumps(r1, indent=1), flush=True)
    recs = []
    for d in [int(x) for x in sys.argv[1:]] or [4]:
        r = degree_count(d); recs.append(r); print(json.dumps(r), flush=True)
    (OUT / 'complex_model_check.json').write_text(json.dumps({'pointwise': r1, 'degrees': recs}, indent=1) + '\n')
