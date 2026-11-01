"""Step 87 -- exact checks for the CSCK calibration of the A1 normal obstruction.

Output: Sessions/S1003A01/workspace/data/step87/csck_calibration.json

(a) Eguchi-Hanson: the U(2)-invariant L^2 harmonic 2-form d(f sigma_3), f=c r^{-2},
    is closed and (anti)self-dual for every V(r); period on the bolt and L^2 norm,
    check  ||theta||^2 = (int_S theta)^2 / |S.S|  with S.S=-2.
(b) Kaehler algebra at a point: |Ric0|^2 = 2|rho0|^2 ; o_I = theta o I is I-Hermitian,
    theta o J, theta o K are I-anti-Hermitian and L^2 orthogonal to o_I; |theta o I|^2 = 2|theta|^2.
(c) CSCK classes near the KE class on a smoothing: exact normalization lambda, primitivity
    of [rho0], P = -2[rho0]^2, and P/(E^2 zeta_r^2) -> -2/theta^2 (=1 when theta^2=-2).
(d) Quintic deformation numerology (39 locally trivial + 1 smoothing) and topology.
"""
import json, os
import sympy as sp

out = {}
# ---------- (a) Eguchi-Hanson harmonic form ----------
r, a, c = sp.symbols('r a c', positive=True)
V = 1 - a**4/r**4
f = c/r**2
fp = sp.diff(f, r)
# Euler-angle sigma's: d sigma3 = - sigma1^sigma2, metric dr^2/V + r^2/4(s1^2+s2^2) + r^2/4 V s3^2
# frames e0=dr/sqrt V, e1=r/2 s1, e2=r/2 s2, e3=r/2 sqrt V s3
# d(f s3) = f' dr^s3 + f ds3 = f'(2/r) e03 - f (4/r^2) e12   (V cancels)
coef03 = sp.simplify(fp*2/r)
coef12 = sp.simplify(-f*4/r**2)
out['EH_coef03'] = str(coef03); out['EH_coef12'] = str(coef12)
out['EH_selfdual_type_ratio_03_over_12'] = str(sp.simplify(coef03/coef12))  # =1 -> e12+e03 type
normsq = 2*coef12**2               # |A(e12+e03)|^2 = 2A^2
vol_density = r**3/8               # e0123 = r^3/8 dr ^ s123
int_s123_RP3 = 8*sp.pi**2          # psi in [0,2pi)
L2 = sp.integrate(normsq*vol_density*int_s123_RP3, (r, a, sp.oo))
period = sp.simplify(coef12.subs(r, a)*a**2/4*4*sp.pi)   # theta|_S = coef12 e12, e12=(a^2/4) s1^s2, int s1^s2=4pi
csol = sp.solve(sp.Eq(period, -2), c)[0]
out['EH_period_general'] = str(period)
out['EH_c_for_period_minus2'] = str(csol)
out['EH_L2norm_sq_at_period_minus2'] = str(sp.simplify(L2.subs(c, csol)))
out['EH_check_norm_equals_period2_over_2'] = str(sp.simplify(L2.subs(c, csol) - 2))
out['EH_pointwise_norm_at_period_minus2'] = str(sp.simplify(sp.sqrt(normsq.subs(c, csol))))

# ---------- (b) Kaehler algebra ----------
def form(pairs):
    M = sp.zeros(4)
    for (i, j, v) in pairs:
        M[i, j] += v; M[j, i] -= v
    return M
def fnorm2(M):  # form norm sum_{i<j}
    return sum(M[i, j]**2 for i in range(4) for j in range(i+1, 4))
I = form([(0, 1, 1), (2, 3, 1)]); J = form([(0, 2, 1), (3, 1, 1)]); K = form([(0, 3, 1), (1, 2, 1)])
Ie, Je, Ke = -I, -J, -K   # endomorphisms (sign irrelevant for norms)
th = form([(0, 1, 1), (2, 3, -1)])  # ASD (complex orientation e0123)
checks = {}
checks['I_is_complex_structure'] = (Ie*Ie == -sp.eye(4))
oI = th*Ie; oJ = th*Je; oK = th*Ke
sym = lambda M: M == M.T
checks['oI_symmetric'] = sym(oI); checks['oJ_symmetric'] = sym(oJ); checks['oK_symmetric'] = sym(oK)
checks['oI_traceless'] = (oI.trace() == 0)
herm = lambda H: sp.simplify(Ie.T*H*Ie - H) == sp.zeros(4)
anti = lambda H: sp.simplify(Ie.T*H*Ie + H) == sp.zeros(4)
checks['oI_I_Hermitian'] = herm(oI); checks['oJ_I_antiHermitian'] = anti(oJ); checks['oK_I_antiHermitian'] = anti(oK)
ip = lambda A, B: sum(A[i, j]*B[i, j] for i in range(4) for j in range(4))
checks['<oI,oJ>'] = int(ip(oI, oJ)); checks['<oI,oK>'] = int(ip(oI, oK))
checks['|oI|^2'] = int(ip(oI, oI)); checks['|theta|^2_form'] = int(fnorm2(th))
# Ricci of Kaehler metric from rho0: Ric0(X,Y) = rho0(X, I Y)
Ric0 = th*Ie
checks['|Ric0|^2 / |rho0|^2'] = sp.Rational(ip(Ric0, Ric0), fnorm2(th))
out['kaehler_algebra'] = {k: (bool(v) if isinstance(v, (bool, sp.logic.boolalg.BooleanAtom)) else str(v)) for k, v in checks.items()}

# ---------- (c) CSCK classes ----------
E, eps, c1sq, t2 = sp.symbols('E epsilon c1sq theta2', real=True)
pi = sp.pi
# classes as coordinates in span{c1, theta}, with c1.theta = 0, c1^2=c1sq, theta^2=t2
def dot(x, y):
    return x[0]*y[0]*c1sq + x[1]*y[1]*t2
lam = sp.symbols('lam', positive=True)
omega = (lam*2*pi/E, lam*eps)            # [omega] = lam(2 pi c1/E + eps theta)
sbar = 8*pi*dot((1, 0), omega)/dot(omega, omega)
lam_sol = sp.solve(sp.Eq(sbar, 4*E), lam)
lam_sol = [L for L in lam_sol if sp.simplify(L.subs({eps: 0})) == 1][0]
out['csck_lambda'] = str(sp.simplify(lam_sol))
om = tuple(sp.simplify(x.subs(lam, lam_sol)) for x in omega)
rho0 = (sp.simplify(2*pi - E*om[0]), sp.simplify(-E*om[1]))   # [rho0] = 2 pi c1 - E[omega]
out['rho0_primitive_check'] = str(sp.simplify(dot(rho0, om)))
P = sp.simplify(-2*dot(rho0, rho0))
zeta_r = sp.simplify(om[1]*t2)          # [omega].delta = lam eps theta.delta, theta.delta=theta^2
out['P_exact'] = str(P)
ratio = sp.simplify(P/(E**2*zeta_r**2))
out['P_over_E2_zeta2_exact'] = str(ratio)
out['P_over_E2_zeta2_eps0'] = str(sp.simplify(sp.limit(ratio, eps, 0)))
out['P_over_E2_zeta2_eps0_theta2=-2'] = str(sp.simplify(sp.limit(ratio, eps, 0).subs(t2, -2)))
ser = sp.series(ratio.subs({t2: -2}), eps, 0, 3).removeO()
out['P_over_E2_zeta2_series_theta2=-2'] = str(sp.simplify(ser))

# ---------- (d) quintic numerology ----------
d = 5
h0 = sp.binomial(d+3, 3)
Jd = 16
q = {}
q['h0_O(5)'] = int(h0); q['dim_J_5'] = Jd
q['embedded_T1 = h0 - J5'] = int(h0 - Jd)
q['(I/J)_5 locally trivial (one node imposes one condition)'] = int(h0 - 1 - Jd)
q['smoothing directions = T1 - (I/J)_5'] = int(h0 - Jd - (h0 - 1 - Jd))
H = sp.symbols('H')
# smooth quintic: K = O(1), c1^2 = 5, c2 = 55, chi(O)=5, p_g=4, b2=53, h11=45, tau=-35
c1sq_q = d*(d-4)**2; c2_q = d*(d*d - 4*d + 6)
q['c1^2'] = int(c1sq_q); q['c2=chi'] = int(c2_q)
q['chi(O)'] = int(sp.Rational(c1sq_q + c2_q, 12)); q['p_g'] = int(sp.binomial(d-1, 3))
q['b2'] = int(c2_q - 2); q['h11'] = int(c2_q - 2 - 2*sp.binomial(d-1, 3))
q['tau'] = int(sp.Rational(c1sq_q - 2*c2_q, 3))
q['h1(Theta)=10chi(O)-2c1^2 (h0=h2=0)'] = int(10*sp.Rational(c1sq_q + c2_q, 12) - 2*c1sq_q)
q['nodal orbifold V: b2, chi_top'] = [int(c2_q - 3), int(c2_q - 1)]
q['bubble N: chi, b2, tau'] = [int(c2_q - (c2_q - 1) + 1), 1, -1]
out['quintic'] = q

os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'data', 'step87'), exist_ok=True)
path = os.path.join(os.path.dirname(__file__), '..', 'data', 'step87', 'csck_calibration.json')
with open(path, 'w') as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
