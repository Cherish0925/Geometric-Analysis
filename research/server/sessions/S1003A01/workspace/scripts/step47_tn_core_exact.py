"""Step 47: exact Taub-NUT core data for the O10 nut-phase question.

Ricci-flat Taub-NUT in Gibbons-Hawking form (spherical base coordinates),
    g = V (dr^2 + r^2 dth^2 + r^2 sin^2 th dph^2) + V^{-1} eta^2,
    V = 1 + ell/r,  eta = dpsi + ell cos(th) dph,   psi-period 4 pi ell.
Orientation dr^dth^dph^dpsi.

Checks / outputs (all symbolic, then exact radial integrals):
 1. closed 2-forms of the two GH types
        beta^{(-)}_h = eta ^ dh + V *_3 dh ,   beta^{(+)}_h = eta ^ dh - V *_3 dh,
    their (anti)self-duality, and closedness: beta^{(+)}_h closed iff h harmonic,
    beta^{(-)}_h closed iff div(V^2 grad h)=0.  h = x3 is the hyperkaehler/endpoint
    direction; h = x3/V is the exact closed continuation of the opposite type.
 2. |Hess fbar|^2, |nabla Hess fbar|^2 for fbar = x1 - i x2  (v_TN = sqrt(m*/2) d fbar,
    Phi_TN = sqrt(rho*) e1 + a fbar e2 with parallel e1,e2, a = sqrt(2)/3).
 3. per-core integrals: E=int|nabla v|^2, int|nabla v|^4, int|nabla^2 v|^2,
    int|nabla^3 Phi|^2, int|W^-|^2 (=8 pi^2 check), int|dm|^2, and the
    determinant-curvature mismatch int |beta_{x3/V}-beta_{x3}|^2 on B_R.
Output: workspace/data/step47/tn_core_exact.json
"""
import json, os
import sympy as sp

r, th, ph, ps, ell, R = sp.symbols('r theta phi psi ell R', positive=True)
X = [r, th, ph, ps]
V = 1 + ell/r
# metric
eta = [0, 0, ell*sp.cos(th), 1]          # components in (r,th,ph,ps)
gb = sp.diag(1, r**2, r**2*sp.sin(th)**2, 0)
g = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        g[i, j] = V*gb[i, j] + eta[i]*eta[j]/V
g = sp.simplify(g)
gi = sp.simplify(g.inv())
sqrtg = sp.simplify(sp.sqrt(sp.factor(g.det())))   # should be V r^2 sin th
print('sqrt det g =', sqrtg)

def d1(a):
    return sp.Matrix(4, 4, lambda i, j: sp.diff(a[j], X[i]) - sp.diff(a[i], X[j]))

def wedge11(a, b):
    return sp.Matrix(4, 4, lambda i, j: a[i]*b[j] - a[j]*b[i])

def d2(B):
    out = {}
    for i in range(4):
        for j in range(i+1, 4):
            for k in range(j+1, 4):
                out[(i, j, k)] = sp.simplify(sp.diff(B[j, k], X[i]) + sp.diff(B[k, i], X[j]) + sp.diff(B[i, j], X[k]))
    return out

def star3_base(a):  # flat base Hodge star of base 1-form a=(ar,ath,aph) -> 2-form matrix (4x4)
    ar, ath, aph = a
    M = sp.zeros(4, 4)
    # ar r^2 sin th dth^dph + ath sin th dph^dr + aph/sin th dr^dth
    M[1, 2] += ar*r**2*sp.sin(th); M[2, 1] -= ar*r**2*sp.sin(th)
    M[2, 0] += ath*sp.sin(th);     M[0, 2] -= ath*sp.sin(th)
    M[0, 1] += aph/sp.sin(th);     M[1, 0] -= aph/sp.sin(th)
    return M

from sympy import LeviCivita
def star4(B):
    Bup = gi*B*gi.T
    S = sp.zeros(4, 4)
    for k in range(4):
        for l in range(4):
            s = 0
            for i in range(4):
                for j in range(4):
                    e = LeviCivita(i, j, k, l)
                    if e != 0:
                        s += e*Bup[i, j]
            S[k, l] = sp.simplify(sqrtg*s/2)
    return S

def beta(h, sign):
    dh = [sp.diff(h, r), sp.diff(h, th), sp.diff(h, ph), 0]
    return sp.simplify(wedge11(eta, dh) + sign*V*star3_base(dh[:3]))

x1 = r*sp.sin(th)*sp.cos(ph); x2 = r*sp.sin(th)*sp.sin(ph); x3 = r*sp.cos(th)
res = {}
for name, h in [('x3', x3), ('x3_over_V', sp.simplify(x3/V)), ('x1', x1)]:
    for sgn, lab in [(1, 'minus_type'), (-1, 'plus_type')]:
        B = beta(h, sgn)
        dB = d2(B)
        closed = all(sp.simplify(v) == 0 for v in dB.values())
        S = star4(B)
        sd = sp.simplify(S - B) == sp.zeros(4, 4)
        asd = sp.simplify(S + B) == sp.zeros(4, 4)
        res[f'{lab}_{name}'] = dict(closed=bool(closed), self_dual=bool(sd), anti_self_dual=bool(asd))
        print(lab, name, res[f'{lab}_{name}'])

# Christoffel symbols
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(4))/2)
         for c in range(4)] for b in range(4)] for a in range(4)]

def hess(f):
    df = [sp.diff(f, x) for x in X]
    return sp.Matrix(4, 4, lambda b, c: sp.diff(df[c], X[b]) - sum(Gam[a][b][c]*df[a] for a in range(4)))

def cov3(H):  # nabla of a (0,2) tensor: T_{a b c} = d_a H_bc - Gam^e_ab H_ec - Gam^e_ac H_be
    T = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                T[(a, b, c)] = sp.diff(H[b, c], X[a]) - sum(Gam[e][a][b]*H[e, c] + Gam[e][a][c]*H[b, e] for e in range(4))
    return T

def norm2_2(H):
    return sp.simplify(sum(gi[a, b]*gi[c, d]*H[a, c]*H[b, d] for a in range(4) for b in range(4) for c in range(4) for d in range(4)))

def norm2_3(T):
    # gi diagonal except (ph,ps) block; do generic contraction efficiently
    s = 0
    idx = range(4)
    nz = [(a, b) for a in idx for b in idx if gi[a, b] != 0]
    for (a, a2) in nz:
        for (b, b2) in nz:
            for (c, c2) in nz:
                s += gi[a, a2]*gi[b, b2]*gi[c, c2]*T[(a, b, c)]*T[(a2, b2, c2)]
    return sp.simplify(s)

H1, H2 = hess(x1), hess(x2)
hess2 = sp.simplify(norm2_2(H1) + norm2_2(H2))
print('|Hess fbar|^2 =', sp.factor(hess2))
T1, T2 = cov3(H1), cov3(H2)
n3 = sp.simplify(norm2_3(T1) + norm2_3(T2))
print('|nabla Hess fbar|^2 =', sp.factor(n3))

vol = sqrtg  # dr dth dph dpsi density
def core_int(fdens, upper=sp.oo):
    ang = sp.integrate(sp.integrate(sp.simplify(fdens*vol), (th, 0, sp.pi)), (ph, 0, 2*sp.pi))
    ang = sp.simplify(ang*4*sp.pi*ell)   # psi period
    return sp.simplify(sp.integrate(sp.simplify(ang), (r, 0, upper)))

mstar = sp.Rational(128, 81); a2 = sp.Rational(2, 9)
E = sp.simplify(mstar/2*core_int(hess2, R))
E4 = sp.simplify((mstar/2)**2*core_int(sp.simplify(hess2**2)))
H2v = sp.simplify(mstar/2*core_int(n3))
H3phi = sp.simplify(a2*core_int(n3))
print('E(R)=', E, '\n int|grad v|^4=', E4, '\n int|grad^2 v|^2=', H2v, '\n int|grad^3 Phi|^2=', H3phi)

# m = |v|^2 = mstar/V, |dm|^2
m = mstar/V
dm2 = sp.simplify(sum(gi[a, b]*sp.diff(m, X[a])*sp.diff(m, X[b]) for a in range(4) for b in range(4)))
Idm = sp.simplify(core_int(dm2))
# determinant ASD mismatch: beta_{x3/V}-beta_{x3}, minus type, on B_R
Bd = sp.simplify(beta(sp.simplify(x3/V), 1) - beta(x3, 1))
mis = sp.simplify(norm2_2(Bd)/2)   # tensor norm^2/2 = form norm^2
Imis = sp.simplify(core_int(mis, R))
Imis_lead = sp.limit(Imis/(ell**3*R), ell, 0) if True else None
print('int|dm|^2 =', Idm, '\n mismatch int_BR =', Imis, '\n lead coeff/(ell^3 R)=', Imis_lead)

out = dict(
    conventions='GH Taub-NUT, V=1+ell/r, eta=dpsi+ell cos th dph, psi period 4 pi ell, orientation dr dth dph dpsi',
    two_form_types=res,
    hess_fbar_sq=str(sp.factor(hess2)), nabla_hess_fbar_sq=str(sp.factor(n3)),
    E_R=str(E), int_grad_v_4=str(E4), int_grad2_v_sq=str(H2v), int_grad3_Phi_sq=str(H3phi),
    int_dm_sq=str(Idm), det_ASD_mismatch_BR=str(Imis), det_ASD_mismatch_lead_over_ell3R=str(Imis_lead),
    mstar=str(mstar), a_sq=str(a2))
here = os.path.dirname(os.path.abspath(__file__))
od = os.path.join(here, '..', 'data', 'step47'); os.makedirs(od, exist_ok=True)
with open(os.path.join(od, 'tn_core_exact.json'), 'w') as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
