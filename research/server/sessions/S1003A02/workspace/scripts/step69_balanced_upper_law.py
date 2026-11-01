#!/usr/bin/env python3
"""Step 69: arithmetic and symbolic checks for the P-form upper law (Lemma 69.Y, Theorems 69.B/69.KE).

Input : Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_P_exact.json  (Arb P/(8pi^2) enclosure)
        Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_J_exact.json  (Arb J/(8pi^2) enclosure)
Output: Sessions/S1003A02/workspace/data/step69_balanced_upper_law.json

Checks
 (1) Lemma 69.Y algebra: for constant scalar curvature s<0, int|Ric - lam g|^2 at lam=s/4 equals P, and
     P/(lam^2 V) = 16 P / (s^2 V) = 16 P / Y^2.
 (2) Balanced topology over a compact ball quotient X (Delta = 3chi - A = 0): M = X # 8n CP2bar # 7n (S1xS3):
     T+ = A - Q with Q = 36 n, 3T-/A = 1 + h, slope sigma = 4.
 (3) Exact rational coefficient 28/9 + (8/9) p_cell with the dyadic upper endpoint of P, compared with the J route.
 (4) (reference only) the eps^2 log coefficient of the scalar-variance term for the Burns-perp cell in a KE
     background, i.e. the D = int|Ric+g|^2 route, computed with the Step-59 exact machinery.
"""
import json, os, sys
from fractions import Fraction as F
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
A01 = os.path.join(ROOT, 'S1003A01', 'workspace', 'data', 'step33')
OUT = os.path.join(HERE, '..', 'data', 'step69_balanced_upper_law.json')
res = {}

# (1) Lemma 69.Y algebra (pointwise: |Ric - lam g|^2 = |Ric0|^2 + 4 (s/4 - lam)^2)
s, lam, P, V = sp.symbols('s lam P V')
num = P + 4 * (s / 4 - lam) ** 2 * V
val = sp.simplify((num / (lam ** 2 * V)).subs(lam, s / 4))
res['lemmaY_value_at_lam_s_over_4'] = str(val)
res['lemmaY_equals_16P_over_s2V'] = bool(sp.simplify(val - 16 * P / (s ** 2 * V)) == 0)
# Step-71 repair: the defect is the infimum over lam != 0, not the value at lam = s/4.
f_lam = num / (lam ** 2 * V)
crit = sp.solve(sp.diff(f_lam, lam), lam)
true_min = [sp.simplify(f_lam.subs(lam, c)) for c in crit]
res['lemmaY_true_lambda_minimizer'] = [str(c) for c in crit]
res['lemmaY_true_minimum'] = [str(t) for t in true_min]
res['lemmaY_true_minimum_equals_16P_over_(4P+s2V)'] = any(
    sp.simplify(t - 16 * P / (4 * P + s ** 2 * V)) == 0 for t in true_min)
res['lemmaY_note'] = ('E(g_hat)=16P/(4P+Y^2) with Y^2=s^2 V at a constant-scalar Yamabe metric; '
                      'the lam=s/4 value 16P/Y^2 is only an upper bound for E.')

# (2) topology of the balanced ball-quotient family
A, n = sp.symbols('A n', positive=True)
chiX = A / 3; tauX = A / 9          # ball quotient: c1^2 = 3 c2, tau = (c1^2 - 2 c2)/3 = A/9
k, l = 8 * n, 7 * n
chi = chiX + k - 2 * l; tau = tauX - k
Q = k + 4 * l
Tp = sp.simplify(2 * chi + 3 * tau); Tm = sp.simplify(2 * chi - 3 * tau)
h = Q / A
res['Q'] = str(Q); res['T_plus_minus_(A-Q)'] = str(sp.simplify(Tp - (A - Q)))
res['3Tminus_over_A_minus_(1+h)'] = str(sp.simplify(3 * Tm / A - (1 + h)))
res['sigma'] = str(sp.simplify(18 * F(8, 36)))

# (3) coefficients
def load(name):
    with open(os.path.join(A01, name)) as f:
        return json.load(f)
Pd = load('rigorous_x00.03_X128_d20_P_exact.json')['P']
Jd = load('rigorous_x00.03_X128_d20_J_exact.json')['J'] if 'J' in load('rigorous_x00.03_X128_d20_J_exact.json') else None
pup = F(int(Pd['upper_dyadic'][0]), int(Pd['upper_dyadic'][1]))
coefP = F(28, 9) + F(8, 9) * pup
res['p_cell_upper_dyadic'] = [str(pup.numerator), str(pup.denominator)]
res['coef_P_route_exact'] = [str(coefP.numerator), str(coefP.denominator)]
res['coef_P_route_decimal'] = f"{sp.Rational(coefP.numerator, coefP.denominator).evalf(30)}"
res['coef_P_route_below_3.9961447'] = coefP < F(39961447, 10 ** 7)
if Jd is not None and 'upper_dyadic' in Jd:
    jup = F(int(Jd['upper_dyadic'][0]), int(Jd['upper_dyadic'][1]))
    coefJ = F(28, 9) + F(8, 9) * jup
    res['coef_J_route_decimal'] = f"{sp.Rational(coefJ.numerator, coefJ.denominator).evalf(30)}"
    res['P_route_improvement'] = f"{sp.Rational((coefJ - coefP).numerator, (coefJ - coefP).denominator).evalf(12)}"
# general theta law with P route: 4 - 4 theta (1 - p)
res['eta_P'] = f"{sp.Rational((1 - pup).numerator, (1 - pup).denominator).evalf(20)}"

# (4) scalar-variance log coefficient for the KE-perp Burns cell (reference)
if '--no-variance' not in sys.argv:
    sys.path.insert(0, HERE)
    import step59_exact_log_coefficient as S59
    sig = sp.Symbol('sig')
    ss, w11, w22, w23 = sp.symbols('s w11 w22 w23')
    ks = sp.symbols('k0:10')
    Wp = sp.Matrix([[w11, 0, 0], [0, w22, w23], [0, w23, -w11 - w22]])
    R = S59.riemann_from_ops(Wp, sp.zeros(3, 3), ss, sp.zeros(3, 3))
    H2 = S59.h2_field(R); K = S59.invariant_K(ks)
    x0 = (1, 0, 0, 0)
    Aj = S59.jets_at(S59.A_field, x0); Hj = S59.jets_at(H2, x0); Kj = S59.jets_at(K, x0)
    Pj = [[[Hj[0][i][j] + sig * Kj[0][i][j] for j in range(4)] for i in range(4)],
          [[[Hj[1][i][j][a] + sig * Kj[1][i][j][a] for a in range(4)] for j in range(4)] for i in range(4)],
          [[[[Hj[2][i][j][a][b] + sig * Kj[2][i][j][a][b] for b in range(4)] for a in range(4)]
            for j in range(4)] for i in range(4)]]
    dens, spr = S59.density_sig2(Aj, Pj)
    KE = {w11: -ss / 12, w22: ss / 6, w23: 0}
    cF = sp.expand(dens.coef(2, 0).subs(KE))
    s1 = sp.expand(spr.coef(1, 0).subs(KE))            # sigma-linear scalar curvature coefficient
    cD = sp.expand(cF + s1 ** 2 / 4)                   # density of int|Ric+g|^2-type at sigma^2 (|Ric0|^2 + ds^2/4)
    def minimize(c):
        sol = sp.solve([sp.diff(c, kk) for kk in ks], ks, dict=True)
        return sp.factor(sp.expand(c.subs(sol[0]))) / 4, sol[0]
    PhiF, solF = minimize(cF)
    PhiD, solD = minimize(cD)
    res['Phi_F_KEperp'] = str(PhiF)
    res['Phi_D_KEperp'] = str(sp.factor(PhiD))
    res['s1_at_P_optimal_corrector'] = str(sp.factor(s1.subs(solF)))
    res['Phi_D_negative'] = bool(sp.simplify(PhiD.subs(ss, -4)) < 0)
json.dump(res, open(OUT, 'w'), indent=1)
print(json.dumps(res, indent=1))
