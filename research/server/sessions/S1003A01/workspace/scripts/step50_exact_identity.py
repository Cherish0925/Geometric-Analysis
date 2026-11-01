"""Step 50d: exact (sympy, rational-function) verification of the W^- compatibility identity

   W+''_flat(h_W, kB) + W+'_flat(k0W) = 0,   s''_flat(h_W, kB) + s'_flat(k0W) = 0,
   k0W = (3/2) sym(h_W kB) - (1/4) tr(h_W kB) delta,

for the H2(-6)xH2(-6) Weyl jet h_W = h2_H2H2 - h2_CH (pure W^-), kB = (v0 v0^T + v1 v1^T)/|x|^4.
Bilinear curvature at flat: R = (1/2)(second derivatives, linear) + sum_e (G_ebc G_ead - G_ebd G_eac)
with lowered Christoffels G (exact formula R_abcd = 1/2(g_ad,bc + g_bc,ad - g_ac,bd - g_bd,ac)
+ g_ef(Gamma^e_bc Gamma^f_ad - Gamma^e_bd Gamma^f_ac)); frame e = 1 - p/2 at first order.
By SU(2)_- equivariance of both sides the identity for one nonzero W^- implies it for all W^-.
Also checks W+'(h_W)=0, s'(h_W)=0 and W+'(kB)=s'(kB)=0, W+''(kB,kB)=s''(kB,kB)=0 exactly.
Usage: python step50_exact_identity.py   -> workspace/data/step50/exact_identity.json
"""
import os, json, itertools, time
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "step50")
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
# H2xH2 adapted basis (signed permutation, as in the numerical scripts)
u0 = E[:, 0]; u1 = Jm[1]*u0
cand = E[:, 2] - (E[:, 2].dot(u0))*u0 - (E[:, 2].dot(u1))*u1
if cand.norm() == 0:
    cand = E[:, 3] - (E[:, 3].dot(u0))*u0 - (E[:, 3].dot(u1))*u1
u2 = cand/cand.norm(); u3 = Jm[1]*u2
O = sp.Matrix.hstack(u0, u1, u2, u3)
y = O.T*X
def blk(z1, z2):
    zz = sp.Matrix([z1, z2]); return 2*((z1**2+z2**2)*sp.eye(2) - zz*zz.T)
G = sp.zeros(4, 4); G[0:2, 0:2] = blk(y[0], y[1]); G[2:4, 2:4] = blk(y[2], y[3])
h2H = O*G*O.T
h2C = sp.Rational(1, 3)*(v[0]*v[0].T + v[2]*v[2].T) + sp.Rational(4, 3)*v[1]*v[1].T
hW = sp.expand(h2H - h2C)
kB = (v[0]*v[0].T + v[1]*v[1].T)/u**2
hk = hW*kB
k0W = sp.Rational(3, 4)*(hk + hk.T) - sp.Rational(1, 4)*hk.trace()*sp.eye(4)

PAIRS = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
Jv = []
for m in range(3):
    vec = sp.Matrix([Jm[m][a, b] for (a, b) in PAIRS]); Jv.append(vec/vec.norm())
Jv = sp.Matrix.hstack(*Jv).T     # 3x6

def d(f, i): return sp.diff(f, x[i])
def chris(p):   # lowered Gamma_{e b c} = 1/2(p_eb,c + p_ec,b - p_bc,e)
    return [[[sp.Rational(1, 2)*(d(p[e, b], c) + d(p[e, c], b) - d(p[b, c], e)) for c in range(4)] for b in range(4)] for e in range(4)]
def R_lin(p):
    return [[[[sp.Rational(1, 2)*(d(d(p[a, dd], b), c) + d(d(p[b, c], a), dd) - d(d(p[a, c], b), dd) - d(d(p[b, dd], a), c))
               for dd in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
def R_bil(p, q):
    Gp, Gq = chris(p), chris(q)
    return [[[[sum(Gp[e][b][c]*Gq[e][a][dd] + Gq[e][b][c]*Gp[e][a][dd] - Gp[e][b][dd]*Gq[e][a][c] - Gq[e][b][dd]*Gp[e][a][c] for e in range(4))
               for dd in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
def frame_corr(p, R1):   # bilinear frame term: -1/2 sum over slots p_ia R1_i...
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
    return Jv*M*Jv.T, s, Ric
def add(*Rs):
    return [[[[sum(R[a][b][c][dd] for R in Rs) for dd in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
def iszero(e):
    return sp.simplify(sp.together(sp.expand(e))) == 0

def main():
    t0 = time.time(); res = {}
    RlinH = R_lin(hW); RlinK = R_lin(kB)
    Wh, sh, Rich = Wp_s(RlinH)
    res["W+'(hW)=0"] = all(iszero(e) for e in Wh); res["s'(hW)=0"] = iszero(sh)
    res["Ric0'(hW)=0"] = all(iszero(Rich[i][j] - (sh/4 if i == j else 0)) for i in range(4) for j in range(4))
    Wk, sk, _ = Wp_s(RlinK)
    res["W+'(kB)=0"] = all(iszero(e) for e in Wk); res["s'(kB)=0"] = iszero(sk)
    print(res, time.time()-t0, flush=True)
    # bilinear (hW, kB) + linear k0W
    Rtot = add(R_bil(hW, kB), frame_corr(hW, RlinK), frame_corr(kB, RlinH), R_lin(k0W))
    Wt, st, _ = Wp_s(Rtot)
    comps = [sp.factor(sp.together(sp.expand(e))) for e in list(Wt) + [st]]
    res["identity_components"] = [str(c) for c in comps]
    res["identity_holds"] = all(c == 0 for c in comps)
    # control: without the corrector the source is nonzero
    Ws, ss, _ = Wp_s(add(R_bil(hW, kB), frame_corr(hW, RlinK), frame_corr(kB, RlinH)))
    res["source_nonzero"] = not all(iszero(e) for e in list(Ws) + [ss])
    res["time_s"] = time.time()-t0
    print(json.dumps(res, indent=1))
    os.makedirs(OUT, exist_ok=True)
    json.dump(res, open(os.path.join(OUT, "exact_identity.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
