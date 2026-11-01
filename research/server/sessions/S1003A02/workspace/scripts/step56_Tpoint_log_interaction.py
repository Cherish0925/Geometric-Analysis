"""
Step 56: the lambda^4 log(1/lambda) interaction between a P-critical orbifold bulk at a Wahl point 1/n^2(1,na-1)
and the Ricci-flat Kaehler ALE Milnor fibre B_{n,a} = (Z_n-symmetric A_{n-1} Gibbons-Hawking space)/Z_n.

Setup (on the universal cover C^2 of the cone, real coords Y1..Y4, y1=Y1+iY2, y2=Y3+iY4, orientation dY1234):
  bulk     g0 = delta + q,  q_ij = -(1/3) R_ikjl Y^k Y^l   (normal coords, R_1212 = sectional curvature),
           R = Gamma-invariant curvature operator, 4 parameters (s, wp, wm, b):
               R = [[s/12 I + wp D, b e1 e1^T],[b e1 e1^T, s/12 I + wm D]],  D = diag(2,-1,-1),
           in the orthonormal bases Lambda^+ = (e12+e34, e13-e24, e14+e23)/sqrt2, Lambda^- = (e12-e34, e13+e24, e14-e23)/sqrt2.
  tail     GH form: K = generator of (e^{it}y1, e^{-it}y2), x = moment map ((|y1|^2-|y2|^2)/2, Re y1y2, Im y1y2),
           V0 = 1/(2|x|) gives delta exactly; the Z_n-symmetric centre configuration contributes, at leading order,
           dV = sigma * c_n * (-P2(u)/r^3), u = x1/r, c_n = n^2 R_c^2/4 > 0, and A2 with dA2 = *dV (orientation fixed
           by the flat structure, checked by linearized Ricci-flatness).  t = -dV Kflat^2 + 2 Kflat (.) A2 + dV dx^2.
  energy   F(e,m) = |Ric^o_g|_g^2 sqrt(det g) for g = delta + e q + m t; the e^2 m coefficient c(Y) is homogeneous of
           degree -4, and the lambda^4 log(1/lambda) coefficient of P is  Lcoef = (1/|Gamma|) * int_{S^3} c.
Gauge invariance: changing the tail by a Lie derivative of degree -3 changes the density by a divergence of degree -3,
whose annular integral has no log. So Lcoef is intrinsic.
Output: workspace/data/step56_Tpoint_log_interaction.json
"""
import json, os, itertools, math
import numpy as np
import sympy as sp

here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, '..', 'data', 'step56_Tpoint_log_interaction.json')

Y = sp.symbols('Y1:5', real=True)
Y1, Y2, Y3, Y4 = Y
rho2 = sum(v ** 2 for v in Y)
x1 = (Y1 ** 2 + Y2 ** 2 - Y3 ** 2 - Y4 ** 2) / 2
x2 = Y1 * Y3 - Y2 * Y4
x3 = Y1 * Y4 + Y2 * Y3
r = rho2 / 2
K = [-Y2, Y1, Y4, -Y3]
dx = [[sp.diff(xx, v) for v in Y] for xx in (x1, x2, x3)]

def sym2(a, b):
    return sp.Matrix(4, 4, lambda i, j: (a[i] * b[j] + a[j] * b[i]) / 2)

Kf2 = sym2(K, K)
dx2 = sum((sym2(d, d) for d in dx), sp.zeros(4, 4))
V0 = 1 / (2 * r)

# GH flat:  V0^{-1} eta0^2 + V0 dx^2 with eta0 = Kflat/|K|^2, V0^{-1}=|K|^2
K2 = sum(k ** 2 for k in K)
gflat = Kf2 / K2 + V0 * dx2
flat_ok = sp.simplify(gflat - sp.eye(4)) == sp.zeros(4, 4)

def tail(sign):
    dV = -(3 * x1 ** 2 - (x1**2+x2**2+x3**2)) / (2 * r ** 5)      # = -P2(u)/r^3   (r^2 = |x|^2 = rho^4/4)
    # A2 = sign * (3 x1 / (2 r^5)) (x2 dx3 - x3 dx2)
    A2 = [sign * 3 * x1 / (2 * r ** 5) * (x2 * dx[2][i] - x3 * dx[1][i]) for i in range(4)]
    return -dV * Kf2 + 2 * sym2(K, A2) + dV * dx2

# note |x| = r = rho^2/2 identically
assert sp.simplify(x1**2 + x2**2 + x3**2 - r**2) == 0

def curv_tensor(s, wp, wm, b):
    e = lambda i, j: (i, j)
    def form(pairs):
        M = np.zeros((4, 4))
        for (i, j), c in pairs:
            M[i, j] += c; M[j, i] -= c
        return M / math.sqrt(2)
    Om = [form([((0, 1), 1), ((2, 3), 1)]), form([((0, 2), 1), ((1, 3), -1)]), form([((0, 3), 1), ((1, 2), 1)]),
          form([((0, 1), 1), ((2, 3), -1)]), form([((0, 2), 1), ((1, 3), 1)]), form([((0, 3), 1), ((1, 2), -1)])]
    D = np.diag([2., -1, -1])
    Rm = np.zeros((6, 6))
    Rm[:3, :3] = s / 12 * np.eye(3) + wp * D
    Rm[3:, 3:] = s / 12 * np.eye(3) + wm * D
    Rm[0, 3] = Rm[3, 0] = b
    T = np.einsum('AB,Aij,Bkl->ijkl', Rm, np.array(Om), np.array(Om))
    return T

def q_matrix(T):
    # q_ij = -(1/3) R_{ikjl} Y^k Y^l
    return sp.Matrix(4, 4, lambda i, j: -sp.Rational(1, 3) * sum(sp.nsimplify(T[i, k, j, l]) * Y[k] * Y[l]
                                                                  for k in range(4) for l in range(4) if abs(T[i, k, j, l]) > 1e-14))

def make_evaluator(H):
    """returns f(point) -> (H, dH, ddH) numeric arrays"""
    Hs = [H[i, j] for i in range(4) for j in range(4)]
    dH = [[sp.diff(h, v) for v in Y] for h in Hs]
    ddH = [[[sp.diff(h, v, w) for w in Y] for v in Y] for h in Hs]
    f0 = sp.lambdify(Y, Hs, 'numpy'); f1 = sp.lambdify(Y, dH, 'numpy'); f2 = sp.lambdify(Y, ddH, 'numpy')
    def ev(p):
        return (np.array(f0(*p), float).reshape(4, 4), np.array(f1(*p), float).reshape(4, 4, 4),
                np.array(f2(*p), float).reshape(4, 4, 4, 4))
    return ev

def ricci(g, dg, ddg):
    gi = np.linalg.inv(g)
    # Gamma^a_{bc} = 1/2 g^{ad}(d_b g_dc + d_c g_db - d_d g_bc); dg[i,j,k] = d_k g_ij
    Gl = 0.5 * (np.einsum('dcb->dbc', dg) + np.einsum('dbc->dbc', dg) - np.einsum('bcd->dbc', dg))  # Gamma_{d,bc}
    G = np.einsum('ad,dbc->abc', gi, Gl)
    # d_e Gamma_{d,bc}
    dGl = 0.5 * (np.einsum('dcbe->dbce', ddg) + np.einsum('dbce->dbce', ddg) - np.einsum('bcde->dbce', ddg))
    dgi = -np.einsum('ap,pqe,qd->ade', gi, dg, gi)
    dG = np.einsum('ade,dbc->abce', dgi, Gl) + np.einsum('ad,dbce->abce', gi, dGl)  # d_e Gamma^a_bc
    # Ric_bc = d_a G^a_bc - d_c G^a_ba + G^a_ad G^d_bc - G^a_cd G^d_ba
    Ric = (np.einsum('abca->bc', dG) - np.einsum('abac->bc', dG)
           + np.einsum('aad,dbc->bc', G, G) - np.einsum('acd,dba->bc', G, G))
    return Ric, gi

def F_density(g, dg, ddg):
    Ric, gi = ricci(g, dg, ddg)
    s = np.einsum('ij,ij', gi, Ric)
    R0 = Ric - s / 4 * g
    val = np.einsum('ia,jb,ij,ab', gi, gi, R0, R0)
    return val * math.sqrt(np.linalg.det(g)), Ric, s

def run():
    res = {"doc": __doc__, "flat_GH_reproduces_delta": bool(flat_ok)}
    # sanity: curvature tensor -> Ricci at origin for q alone
    T = curv_tensor(1.0, 0.3, -0.2, 0.4)
    q = q_matrix(T)
    evq = make_evaluator(q)
    p0 = np.array([1e-3, 2e-3, -1e-3, 0.5e-3])
    gq, dgq, ddgq = evq(p0)
    Ric, gi = ricci(np.eye(4) + gq, dgq, ddgq)
    Ric_alg = np.einsum('ikil->kl', T)
    res["normal_coord_check"] = {"Ric_numeric_origin": Ric.round(6).tolist(), "Ric_from_R": Ric_alg.round(6).tolist(),
                                 "scalar": float(np.trace(Ric_alg))}
    # choose tail orientation by linearized Ricci-flatness
    pts = [np.array(v) / np.linalg.norm(v) for v in ([0.7, 0.2, -0.4, 0.5], [0.1, -0.8, 0.3, 0.2], [0.5, 0.5, 0.5, -0.1])]
    lin = {}
    evs = {}
    for sign in (1, -1):
        t = tail(sign)
        evs[sign] = make_evaluator(t)
        m = 1e-5
        vals = []
        for p in pts:
            gt, dgt, ddgt = evs[sign](p)
            Rp, _ = ricci(np.eye(4) + m * gt, m * dgt, m * ddgt)
            Rm_, _ = ricci(np.eye(4) - m * gt, -m * dgt, -m * ddgt)
            vals.append(float(np.max(np.abs((Rp - Rm_) / (2 * m)))))
        lin[sign] = vals
    res["linearized_Ricci_of_tail"] = {str(k): v for k, v in lin.items()}
    sign = min(lin, key=lambda k: max(lin[k]))
    res["chosen_sign"] = sign
    evt = evs[sign]
    # sanity: tail magnitude
    gt, _, _ = evt(pts[0]); res["tail_norm_sample"] = float(np.linalg.norm(gt))

    # e^2 m coefficient
    def coef(params, p, h=4e-3, k=2e-4):
        qe = make_cached_q(params)
        gq, dgq, ddgq = qe(p)
        gt, dgt, ddgt = evt(p)
        def F(e, m):
            return F_density(np.eye(4) + e * gq + m * gt, e * dgq + m * dgt, e * ddgq + m * ddgt)[0]
        def a21(h, k):
            Gf = lambda e: (F(e, k) - F(e, -k)) / (2 * k)
            return (Gf(h) + Gf(-h) - 2 * Gf(0)) / (2 * h * h)
        # Richardson in k (error a23 k^2) and in h (error a41 h^2)
        rk = lambda h: (4 * a21(h, k / 2) - a21(h, k)) / 3
        return (4 * rk(h / 2) - rk(h)) / 3

    cache = {}
    def make_cached_q(params):
        if params not in cache:
            cache[params] = make_evaluator(q_matrix(curv_tensor(*params)))
        return cache[params]

    # S^3 integral: T^2-invariance -> only chi matters; check invariance numerically at one chi
    def point(chi, a=0.37, bb=1.21):
        return np.array([math.cos(chi) * math.cos(a), math.cos(chi) * math.sin(a), math.sin(chi) * math.cos(bb), math.sin(chi) * math.sin(bb)])
    test = (1.0, 0.5, -0.7, 0.9)
    inv = [coef(test, point(0.6, a, bb)) for a, bb in [(0.37, 1.21), (2.0, -0.5), (4.1, 3.3)]]
    res["T2_invariance_check"] = inv
    # Gauss-Legendre in chi
    xg, wg = np.polynomial.legendre.leggauss(48)
    chis = (xg + 1) * math.pi / 4; wch = wg * math.pi / 4
    def S3int(params):
        vals = np.array([coef(params, point(c)) for c in chis])
        return float(4 * math.pi ** 2 * np.sum(wch * vals * np.sin(chis) * np.cos(chis)))
    basis = {"s": (1.0, 0, 0, 0), "wp": (0, 1.0, 0, 0), "wm": (0, 0, 1.0, 0), "b": (0, 0, 0, 1.0)}
    names = list(basis)
    diag = {nm: S3int(basis[nm]) for nm in names}
    Qmat = np.zeros((4, 4))
    for i, a in enumerate(names):
        Qmat[i, i] = diag[a]
    for i, j in itertools.combinations(range(4), 2):
        v = tuple(np.array(basis[names[i]]) + np.array(basis[names[j]]))
        Qmat[i, j] = Qmat[j, i] = (S3int(v) - diag[names[i]] - diag[names[j]]) / 2
    res["quadratic_form_names"] = names
    res["Q_S3_integral_matrix"] = Qmat.tolist()
    res["note"] = ("Lcoef(R_p) = (c_n/|Gamma|) * v^T Q v, v=(s,wp,wm,b); c_n = n^2 R_c^2/4 > 0. "
                   "P(glued) = P(V,g0) + lambda^4 log(1/lambda) Lcoef + O(lambda^4).")
    with open(out, 'w') as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: res[k] for k in res if k != 'doc'}, indent=1))

run()
