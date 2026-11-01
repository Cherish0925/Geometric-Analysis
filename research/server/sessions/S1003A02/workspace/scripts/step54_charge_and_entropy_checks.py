"""Step 54 checks.
(1) Topological P-cost of a smooth complete AE piece N with e ends (all Gamma=1), capped N^ (closed):
    P(N) = 4 int|W+|^2 + (1/12) int s^2 - 8 pi^2 * T+(N),  T+(N) := 2 e_GB(N) + 3 tau(N),
    e_GB(N) = chi(N) - e,  chi(N) = chi(N^) - e,  chi(N^) = 2 - 2 b1 + b2.
    => charge c(N) := -T+(N) = 4(e-1) + 4 b1 + b- - 5 b+ ; reversed orientation c(Nbar) = 4(e-1)+4b1 + b+ - 5b-.
(2) Global telescoping on X#CPbar^2 configurations (bulk V closed, bubbles at smooth points).
(3) BCG + Bishop numbers for a complex-hyperbolic target (naive entropy exclusion test).
Output: workspace/data/step54_charge_and_entropy_checks.json
"""
import json, os
import sympy as sp

out = {}
b1, bp, bm, e = sp.symbols('b1 bp bm e', integer=True, nonnegative=True)
chi_cap = 2 - 2*b1 + bp + bm
chi_N = chi_cap - e
eGB = chi_N - e
tau = bp - bm
Tplus = sp.expand(2*eGB + 3*tau)
charge = sp.expand(-Tplus)
out['charge_formula'] = str(charge)
assert sp.simplify(charge - (4*(e-1) + 4*b1 + bm - 5*bp)) == 0
examples = {
    'Burns (CPbar2 cap, e=1)': dict(b1=0, bp=0, bm=1, e=1),
    'reversed Burns (CP2 cap) in its own orientation': dict(b1=0, bp=1, bm=0, e=1),
    'Schwarzschild neck S3xR (S4 cap, e=2)': dict(b1=0, bp=0, bm=0, e=2),
    'homotopy-sphere bubble (e=1)': dict(b1=0, bp=0, bm=0, e=1),
    'S1xS3 cap (b1=1, e=1)': dict(b1=1, bp=0, bm=0, e=1),
    'S2xS2 cap (e=1)': dict(b1=0, bp=1, bm=1, e=1),
    'three-ended, S4 cap': dict(b1=0, bp=0, bm=0, e=3),
}
ex = {}
for k, v in examples.items():
    c = int(charge.subs({b1: v['b1'], bp: v['bp'], bm: v['bm'], e: v['e']}))
    cbar = int((4*(e-1) + 4*b1 + bp - 5*bm).subs({b1: v['b1'], bp: v['bp'], bm: v['bm'], e: v['e']}))
    ex[k] = {'c(N)': c, 'c(Nbar)': cbar, 'P_lower_in_8pi2_units': max(c, cbar, 0)}
out['examples'] = ex

# (2) telescoping: M = V # N^_1 # ... ; check T+(M) = T+(V) + sum T+(N_j) for one-ended bubbles
chiV, tauV = sp.symbols('chiV tauV')
chis = sp.symbols('c1:4'); taus = sp.symbols('t1:4')
chiM = chiV + sum(chis) - 2*3          # three ordinary connected sums
tauM = tauV + sum(taus)
TM = 2*chiM + 3*tauM
TV = 2*chiV + 3*tauV
TN = sum(2*((c - 1) - 1) + 3*t for c, t in zip(chis, taus))  # chi(N)=chi(N^)-1, e_GB=chi(N)-1
out['telescoping_residual'] = str(sp.simplify(TM - TV - TN))

# (3) BCG + Bishop with complex-hyperbolic target, normalization Ric = -6 (holomorphic curvature -4)
h0 = 4                      # volume entropy of CH^2 (2n, n=2)
hmax = 3*sp.sqrt(2)         # Bishop bound for Ric >= -6 = -3 kappa^2, kappa^2 = 2
ratio = sp.nsimplify((h0/hmax)**4)
# Volumes in units of Vol(X): 8pi^2 chi(X) = 48 Vol(X), A = 3 chi(X)
chiX = sp.symbols('chiX', positive=True)
volX = 1
# Einstein g on X#CPbar2 with Ric=-6: 8pi^2(2chi+3tau)(M) = 4 int|W+|^2 + 48 Vol(g) >= 48 Vol(g)
vol_upper_T = sp.simplify((3*chiX - 1)/chiX)             # Vol(g) <= (A-1)/48*8pi^2 = Vol(X)(3chi-1)/chi
vol_upper_chi = sp.simplify(2*(chiX + 1)/chiX)           # 8pi^2 chi(M) >= 24 Vol(g)
vol_if_kahler_type_Wplus = sp.simplify((3*chiX - 1)/(3*chiX))  # |W+|^2 = s^2/24 everywhere
out['BCG_Bishop'] = {
    'entropy_ratio_(h0/hmax)^4': str(ratio), 'numeric': float(ratio),
    'Vol(g)/Vol(X) lower (BCG+Bishop)': float(ratio),
    'Vol(g)/Vol(X) upper from 2chi+3tau': str(vol_upper_T),
    'Vol(g)/Vol(X) upper from chi': str(vol_upper_chi),
    'Vol(g)/Vol(X) for Kahler-type W+ Einstein (hypothetical)': str(vol_if_kahler_type_Wplus),
    'contradiction_for_chiX>=3': bool(float(ratio) > float(vol_if_kahler_type_Wplus.subs(chiX, 3))),
}
path = os.path.join(os.path.dirname(__file__), '..', 'data', 'step54_charge_and_entropy_checks.json')
with open(path, 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
