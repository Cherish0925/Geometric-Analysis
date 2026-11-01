"""Step 52b: closed-form trace-free-Ricci corrector for the perpendicular Burns tail (A02 request #832(1)).

Background quadratic jet of pure Ric0 type: R = (1/2) E (Kulkarni-Nomizu) delta with E trace-free,
  h_R = -(1/3) R_ikjl x^k x^l = -(1/6)(E u + (x.Ex) delta - Ex x^T - x (Ex)^T),   h_R x = 0.
Seek a degree-0 natural tensor k0^R, linear in E, with
  W+''_flat(h_R, kB) + W+'_flat(k0^R) = 0   and   s''_flat(h_R, kB) + s'_flat(k0^R) = 0
identically in x (the Step-50 W^- analogue). Ansatz: linear combination of natural tensors built from
h = h_R, x, v2 = J3 x (zeta = J3), the projectors Pr, P3, K, and J3. The coefficients are solved from exact
evaluations at random rational points, then the identity is re-verified symbolically for two independent E.
Output: workspace/data/step52/ric0_corrector.json
"""
import os, json, itertools, time, random
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "step52"); os.makedirs(OUT, exist_ok=True)
x = sp.symbols('x0:4', real=True)
X = sp.Matrix(x)
u = sum(xi**2 for xi in x)

def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return [a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2, a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2]
E = sp.eye(4)
Jm = [sp.zeros(4, 4) for _ in range(3)]
for c in range(4):
    for b in range(4):
        pr = qmul([E[0, c], -E[1, c], -E[2, c], -E[3, c]], [E[0, b], E[1, b], E[2, b], E[3, b]])
        for m in range(3):
            Jm[m][b, c] = pr[m+1]
v = [Jm[m]*X for m in range(3)]
J3 = Jm[2]; v2 = v[2]
kB = (v[0]*v[0].T + v[1]*v[1].T)/u**2
Pr = X*X.T/u; P3 = v2*v2.T/u; K = (v[0]*v[0].T + v[1]*v[1].T)/u
Xm = (X*v2.T + v2*X.T)/(2*u)
I4 = sp.eye(4)
PAIRS = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
Jv = []
for m in range(3):
    vec = sp.Matrix([Jm[m][a, b] for (a, b) in PAIRS]); Jv.append(vec/vec.norm())
Jv = sp.Matrix.hstack(*Jv).T

def d(f, i): return sp.diff(f, x[i])
def chris(p):
    return [[[sp.Rational(1, 2)*(d(p[e, b], c) + d(p[e, c], b) - d(p[b, c], e)) for c in range(4)] for b in range(4)] for e in range(4)]
def R_lin(p):
    return [[[[sp.Rational(1, 2)*(d(d(p[a, dd], b), c) + d(d(p[b, c], a), dd) - d(d(p[a, c], b), dd) - d(d(p[b, dd], a), c))
               for dd in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
def R_bil(p, q):
    Gp, Gq = chris(p), chris(q)
    return [[[[sum(Gp[e][b][c]*Gq[e][a][dd] + Gq[e][b][c]*Gp[e][a][dd] - Gp[e][b][dd]*Gq[e][a][c] - Gq[e][b][dd]*Gp[e][a][c] for e in range(4))
               for dd in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
def frame_corr(p, R1):
    out = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a, b, c, dd in itertools.product(range(4), repeat=4):
        out[a][b][c][dd] = -sp.Rational(1, 2)*sum(p[i, a]*R1[i][b][c][dd] + p[i, b]*R1[a][i][c][dd]
                                                  + p[i, c]*R1[a][b][i][dd] + p[i, dd]*R1[a][b][c][i] for i in range(4))
    return out
def Wp_s(R):
    Ric = [[sum(R[a][b][a][dd] for a in range(4)) for dd in range(4)] for b in range(4)]
    s = sum(Ric[i][i] for i in range(4))
    dl = lambda i, j: 1 if i == j else 0
    def W(a, b, c, dd):
        return (R[a][b][c][dd] - sp.Rational(1, 2)*(dl(a, c)*Ric[b][dd] - dl(a, dd)*Ric[b][c] - dl(b, c)*Ric[a][dd] + dl(b, dd)*Ric[a][c])
                + s/6*(dl(a, c)*dl(b, dd) - dl(a, dd)*dl(b, c)))
    M = sp.Matrix(6, 6, lambda I, J: W(*PAIRS[I], *PAIRS[J]))
    return Jv*M*Jv.T, s
def add(*Rs):
    return [[[[sum(R[a][b][c][dd] for R in Rs) for dd in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
def vec_out(R):
    Wt, st = Wp_s(R)
    return [Wt[i, j] for i in range(3) for j in range(i, 3)] + [st]

def hR_of(Em):
    Ex = Em*X; xEx = (X.T*Em*X)[0, 0]
    return -sp.Rational(1, 6)*(Em*u + xEx*I4 - Ex*X.T - X*Ex.T)

def candidates(h):
    hv = h*v2; tr = h.trace(); q = (v2.T*h*v2)[0, 0]
    Jh = J3*h*J3.T
    sy = lambda A: (A + A.T)/2
    c = {
        "h/u": h/u,
        "sym(h v2 v2^T)/u^2": sy(hv*v2.T)/u**2,
        "J3 h J3^T/u": Jh/u,
        "sym(J3 h)/u": sy(J3*h)/u,
        "sym(x (J3 h v2)^T)/u^2": sy(X*(J3*hv).T)/u**2,
        "sym(v2 (J3 h v2)^T)/u^2": sy(v2*(J3*hv).T)/u**2,
        "sym(x hv2^T)/u^2": sy(X*hv.T)/u**2,
    }
    for nm, Bm in [("delta", I4), ("Pr", Pr), ("P3", P3), ("K", K), ("X", Xm)]:
        c[f"(tr h/u) {nm}"] = (tr/u)*Bm
        c[f"(v2.h.v2/u^2) {nm}"] = (q/u**2)*Bm
    return c

def build(Em):
    h = hR_of(Em)
    Rh = R_lin(h); RK = R_lin(kB)
    src = add(R_bil(h, kB), frame_corr(h, RK), frame_corr(kB, Rh))
    cands = candidates(h)
    lins = {nm: R_lin(Bm) for nm, Bm in cands.items()}
    return h, Rh, src, cands, lins

def main():
    t0 = time.time()
    random.seed(1)
    E1 = sp.Matrix([[1, 3, 0, 2], [3, -5, 4, 0], [0, 4, 7, -1], [2, 0, -1, -3]])/10
    E2 = sp.Matrix([[2, -1, 1, 0], [-1, 0, 2, 3], [1, 2, -1, 1], [0, 3, 1, -1]])/7
    res = {}
    h, Rh, src, cands, lins = build(E1)
    Wh, sh = Wp_s(Rh)
    res["pure_Ric0_check"] = all(sp.simplify(z) == 0 for z in list(Wh) + [sh])
    names = list(cands)
    S = vec_out(src)
    Ls = {nm: vec_out(lins[nm]) for nm in names}
    print("built", time.time()-t0, flush=True)
    rows = []; rhs = []
    pts = [[sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for _ in range(4)] for _ in range(14)]
    for p in pts:
        sb = dict(zip(x, p))
        if sum(pi**2 for pi in p) == 0: continue
        for k in range(len(S)):
            rows.append([sp.nsimplify(Ls[nm][k].subs(sb)) for nm in names]); rhs.append(-S[k].subs(sb))
    import numpy as np
    from fractions import Fraction
    An = np.array([[float(z) for z in r] for r in rows]); bn = np.array([float(z) for z in rhs])
    print("system", An.shape, time.time()-t0, flush=True)
    xs, *_ = np.linalg.lstsq(An, bn, rcond=None)
    resid = float(np.linalg.norm(An@xs - bn)); res["lstsq_residual"] = resid; res["rhs_norm"] = float(np.linalg.norm(bn))
    res["rank"] = int(np.linalg.matrix_rank(An)); res["ncand"] = len(names)
    res["lstsq_coef"] = dict(zip(names, map(float, xs)))
    print("residual", resid, "rank", res["rank"], flush=True)
    if resid > 1e-8*max(1.0, res["rhs_norm"]):
        res["solvable"] = False
        print(json.dumps(res, indent=1))
        json.dump(res, open(os.path.join(OUT, "ric0_corrector.json"), "w"), indent=1)
        return
    res["solvable"] = True
    sol = [sp.Rational(Fraction(float(z)).limit_denominator(1000)) for z in xs]
    coef = {nm: str(sol[i]) for i, nm in enumerate(names) if sol[i] != 0}
    res["coefficients"] = coef
    print(coef, flush=True)
    # symbolic verification for E1 and E2
    for tag, Em in [("E1", E1), ("E2", E2)]:
        h, Rh, src, cands, lins = build(Em)
        k0 = sp.zeros(4, 4)
        for i, nm in enumerate(names):
            k0 += sol[i]*cands[nm]
        tot = vec_out(add(src, R_lin(k0)))
        res[f"identity_holds_{tag}"] = all(sp.simplify(sp.together(sp.expand(z))) == 0 for z in tot)
        print(tag, res[f"identity_holds_{tag}"], time.time()-t0, flush=True)
    res["time_s"] = time.time()-t0
    print(json.dumps(res, indent=1))
    json.dump(res, open(os.path.join(OUT, "ric0_corrector.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
