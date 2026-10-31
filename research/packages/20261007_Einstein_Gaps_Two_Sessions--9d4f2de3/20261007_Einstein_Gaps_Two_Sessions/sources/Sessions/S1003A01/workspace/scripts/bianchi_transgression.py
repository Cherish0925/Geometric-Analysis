"""Chern--Weil transgression for diagonal Bianchi-IX metrics.

Metric  g = dt^2 + a^2 s1^2 + b^2 s2^2 + c^2 s3^2,  d s_i = 2 s_j ^ s_k (cyclic),
int_{S^3} s1 s2 s3 = 2 pi^2 (round unit S^3 = a=b=c=1).
Orthonormal coframe e0=dt, e1=a s1, e2=b s2, e3=c s3; orientation e0123.

Computes the Levi-Civita connection and curvature by Cartan's equations, then
the 4-form density
    Theta = 8 pi^2 (2 e + 3 p) dV = (1/2) eps_{abcd} Om_ab ^ Om_cd + sum_{a,b} Om_ab ^ Om_ab
(sum over ordered indices), where e, p are the Euler and (signature) densities,
chi = int e, tau = int p.  Theta = f(t) e0123 = f abc dt ^ s123.
It then finds G(a,b,c,a',b',c') with dG/dt = f abc and prints
    T(slice) = 2 pi^2 (G(slice) - G(flat round slice)),
so that for any region between slices t1<t2,
    int |Ric+g|^2 dV = int F dV - (T(t2)-T(t1)),
    F = (s+3)^2/3 + 1 + 4|W^+|^2   (tensor norms),
with the orientation that gives tau = -1 on O(-1).
Both orientations are reported; the choice is fixed by the Burns check.
Output: printed formulas and checks; writes data/transgression/G_formula.txt.
"""
import itertools, os
import sympy as sp

t = sp.symbols('t', real=True)
A, B, C = [sp.Function(n)(t) for n in 'abc']
fun = [A, B, C]
idx = range(4)


def d_coframe():
    # de_a as dict {(i,j): coeff} for e_i^e_j, i<j
    de = {0: {}}
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        ai, aj, ak = fun[i], fun[j], fun[k]
        jj, kk = j + 1, k + 1
        key = (min(jj, kk), max(jj, kk))
        sgn = 1 if jj < kk else -1
        de[i + 1] = {(0, i + 1): sp.diff(ai, t) / ai, key: sgn * 2 * ai / (aj * ak)}
    return de


def wedge11(u, v):
    out = {}
    for i, x in u.items():
        for j, y in v.items():
            if i == j:
                continue
            key = (min(i, j), max(i, j))
            s = 1 if i < j else -1
            out[key] = out.get(key, 0) + s * x * y
    return out


def wedge22(u, v):
    # returns coefficient of e0123
    tot = 0
    for (i, j), x in u.items():
        for (k, l), y in v.items():
            p = (i, j, k, l)
            if len(set(p)) < 4:
                continue
            perm = list(p)
            sgn = 1
            for m in range(4):
                for n in range(m + 1, 4):
                    if perm[m] > perm[n]:
                        sgn = -sgn
            tot += sgn * x * y
    return tot


def add(u, v, s=1):
    out = dict(u)
    for k, x in v.items():
        out[k] = out.get(k, 0) + s * x
    return out


def main():
    de = d_coframe()
    # unknown connection: om[a][b] = sum_c G[a,b,c] e_c, antisymmetric
    Gs = {}
    unknowns = []
    for a in idx:
        for b in idx:
            if a < b:
                for c in idx:
                    s = sp.Symbol(f'G_{a}{b}{c}')
                    Gs[(a, b, c)] = s
                    unknowns.append(s)

    def om(a, b):
        if a == b:
            return {}
        if a < b:
            return {c: Gs[(a, b, c)] for c in idx}
        return {c: -Gs[(b, a, c)] for c in idx}

    eqs = []
    for a in idx:
        lhs = dict(de[a])
        rhs = {}
        for b in idx:
            rhs = add(rhs, wedge11(om(a, b), {b: 1}), -1)
        diff = add(lhs, rhs, -1)
        for k in itertools.combinations(idx, 2):
            eqs.append(sp.simplify(diff.get(k, 0)))
    sol = sp.solve(eqs, unknowns, dict=True)[0]

    def omv(a, b):
        return {c: sp.simplify(sp.sympify(v).subs(sol)) for c, v in om(a, b).items()}

    def dform1(u):
        out = {}
        for c, x in u.items():
            out = add(out, wedge11({0: sp.diff(x, t)}, {c: 1}))
            if c > 0:
                out = add(out, {k: x * v for k, v in de[c].items()})
        return out

    Om = {}
    for a in idx:
        for b in idx:
            if a == b:
                Om[(a, b)] = {}
                continue
            w = dform1(omv(a, b))
            for c in idx:
                w = add(w, wedge11(omv(a, c), omv(c, b)))
            Om[(a, b)] = {k: sp.simplify(v) for k, v in w.items()}

    eul = 0
    for a, b, c, d in itertools.permutations(idx):
        perm = [a, b, c, d]
        sgn = 1
        for m in range(4):
            for n in range(m + 1, 4):
                if perm[m] > perm[n]:
                    sgn = -sgn
        eul += sgn * wedge22(Om[(a, b)], Om[(c, d)])
    pon = 0
    for a in idx:
        for b in idx:
            if a != b:
                pon += wedge22(Om[(a, b)], Om[(a, b)])
    eul = sp.simplify(eul)
    pon = sp.simplify(pon)
    vol = A * B * C
    res = {}
    for orient in (+1, -1):
        f = sp.Rational(1, 2) * eul + orient * pon
        dens = sp.expand(sp.simplify(f * vol))
        res[orient] = dens
    # find antiderivative: dens is linear in second derivatives
    a1, b1, c1, a2, b2, c2, x, y, z = sp.symbols('a1 b1 c1 a2 b2 c2 x y z')
    rep2 = {sp.diff(A, t, 2): a2, sp.diff(B, t, 2): b2, sp.diff(C, t, 2): c2}
    rep1 = {sp.diff(A, t): a1, sp.diff(B, t): b1, sp.diff(C, t): c1}
    rep0 = {A: x, B: y, C: z}
    out = {}
    for orient, dens in res.items():
        D = sp.expand(dens.subs(rep2).subs(rep1).subs(rep0))
        ca, cb, cc = [sp.expand(D.coeff(v)) for v in (a2, b2, c2)]
        rest = sp.expand(D - ca * a2 - cb * b2 - cc * c2)
        G = sp.integrate(ca, a1)
        r1 = sp.simplify(cb - sp.diff(G, b1))
        G = G + sp.integrate(r1, b1)
        r2 = sp.simplify(cc - sp.diff(G, c1))
        G = G + sp.integrate(r2, c1)
        # remaining: rest - (G_x a1 + G_y b1 + G_z c1) must be d/dt of h(x,y,z)
        rem = sp.simplify(rest - (sp.diff(G, x) * a1 + sp.diff(G, y) * b1 + sp.diff(G, z) * c1))
        hx, hy, hz = [sp.simplify(sp.expand(rem).coeff(v)) for v in (a1, b1, c1)]
        h = sp.integrate(hx, x)
        h = h + sp.integrate(sp.simplify(hy - sp.diff(h, y)), y)
        h = h + sp.integrate(sp.simplify(hz - sp.diff(h, z)), z)
        G = sp.simplify(G + h)
        # verify
        chk = sp.simplify(sp.diff(G, x) * a1 + sp.diff(G, y) * b1 + sp.diff(G, z) * c1
                          + sp.diff(G, a1) * a2 + sp.diff(G, b1) * b2 + sp.diff(G, c1) * c2 - D)
        Gflat = sp.simplify(G.subs({x: 1, y: 1, z: 1, a1: 1, b1: 1, c1: 1}))
        Gbolt = sp.simplify(G.subs({c1: 1, z: 0, a1: 0, b1: 0, y: x}))
        out[orient] = (G, chk, Gflat, Gbolt)
        print('orientation', orient)
        print('  G =', sp.factor(G))
        print('  check (should be 0):', chk)
        print('  G_flat =', Gflat, ' G_bolt(a=b,c=0,c\'=1) =', Gbolt,
              ' T_bolt = 2pi^2 (G_bolt-G_flat) =', sp.simplify(2 * sp.pi**2 * (Gbolt - Gflat)))
    here = os.path.dirname(os.path.abspath(__file__))
    od = os.path.join(here, '..', 'data', 'transgression')
    os.makedirs(od, exist_ok=True)
    with open(os.path.join(od, 'G_formula.txt'), 'w') as fh:
        for orient, (G, chk, Gf, Gb) in out.items():
            fh.write(f'orientation {orient}\nG = {sp.factor(G)}\ncheck = {chk}\nGflat = {Gf}\nGbolt = {Gb}\n\n')


if __name__ == '__main__':
    main()
