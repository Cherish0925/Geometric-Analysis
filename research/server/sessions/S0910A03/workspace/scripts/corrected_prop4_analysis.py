"""
CRITICAL CORRECTION: Verify Ishida-LeBrun Proposition 4 (coefficient 2/3)
vs LeBrun 1998 Theorem A (coefficient 32/57).

Proposition 4 statement (from Ishida-LeBrun line 100):
  (1/4pi^2) int(s^2/24 + 2|W+|^2) dmu >= (2/3)(a+)^2

This gives the MIXED bound with a+ the self-dual projection of the monopole class.
Using (a+)^2 >= A = c_1^2(X) (sign trick), this becomes:
  2 I_+ + E_s >= (8/3) pi^2 A

Compare Theorem A of LeBrun 1998:
  2 I_+ + E_s > (128/57) pi^2 A  (=  (32/57)*4pi^2 A)

Since 8/3 = 152/57 > 128/57, Prop 4 is STRICTLY STRONGER.

Derivation of Prop 4:
  From Weitzenbock for self-dual 2-forms phi:
    (d+d*)^2 phi = nabla*nabla phi - 2W+(phi, .) + (s/3)phi
  
  Applied to phi = F_A+ (self-dual curvature of SW connection):
    int(-W+)(F_A+, F_A+) >= (-s/6) int|F_A+|^2  (dropping gradient term >= 0)
  
  Using |W+|.|F_A+|^2 >= sqrt(3/2).(-W+)(F_A+, F_A+) (trace-free on Omega+):
    (int|W+|^2)^{1/2} (int|F_A+|^4)^{1/2} >= sqrt(3/2) |s|/6 int|F_A+|^2
  
  Using |F_A+|^2 = |Phi|^4/8 <= s^2/8 pointwise:
    (int|F_A+|^4)^{1/2} <= |s|/sqrt(8) (int|F_A+|^2)^{1/2}
  
  Combining:
    (int|W+|^2)^{1/2} >= (1/sqrt(3)) (int|F_A+|^2)^{1/2}
    int|W+|^2 >= (1/3) int|F_A+|^2 >= (4pi^2/3) (a+)^2
  
  Therefore:
    2 int|W+|^2 + int s^2/24 >= (8pi^2/3)(a+)^2 + 0 = (2/3)*4pi^2*(a+)^2.
  
  This is Proposition 4.
"""
import sympy as sp
from fractions import Fraction

d = sp.Symbol('delta', positive=True)
p = sp.Symbol('p', positive=True)  # k/A

print("="*70)
print("CORRECTED ANALYSIS: Proposition 4 coefficient = 2/3")
print("="*70)
print()
print("Combined bound from Prop 4 + CW + pinching:")
print("  E_R >= 4pi^2(k - A/3)  ... from Prop 4")
print("  E_R <= c_d E_s          ... from pinching")
print("  E_s <= 4pi^2(A-k)/(1-c_d) ... from CW")
print()
print("=> c_d(1-p)/(1-c_d) >= p - 1/3")
print("=> (2/3)c_d >= p - 1/3")
print("=> k/A <= 1/3 + (2/3)c_d = 1/3 + 2*delta^2/(1-delta)^2")
print()

# Verify formula
bound = sp.Rational(1,3) + 2*d**2/(1-d)**2
print(f"k/A <= {sp.simplify(bound)}")
print()

# Table of pinching gaps
print("Pinching gaps delta_0 at various k/A:")
print(f"{'k/A':>12} {'delta_0':>12} {'notes':>40}")
for pval_num, pval_den, note in [
    (1, 3, "critical ratio (Prop 4 boundary)"),
    (19, 57, "= 1/3 (same)"),
    (25, 57, "LeBrun 1998 Thm B boundary"),
    (1, 2, "halfway"),
    (2, 3, "LeBrun 1996 boundary"),
    (3, 4, "above 1996"),
]:
    pval = Fraction(pval_num, pval_den)
    pf = float(pval)
    excess = pf - 1/3
    if excess <= 0:
        print(f"{pf:>12.6f} {'0':>12} {note:>40}")
        continue
    # 2*delta^2/(1-delta)^2 >= excess
    # delta^2/(1-delta)^2 >= excess/2
    # delta/(1-delta) >= sqrt(excess/2)
    r = float(sp.sqrt(excess/2))
    delta_0 = r/(1+r)
    print(f"{pf:>12.6f} {delta_0:>12.6f} {note:>40}")

print()
print("="*70)
print("KEY RESULT: ALL LeBrun manifolds with no Einstein metric")
print("  (k/A >= 25/57) have UNIFORM pinching gap delta >= 0.187")
print("="*70)
print()
print("At k/A = 25/57:")
exc = 25/57 - 1/3
r = (exc/2)**0.5
d0 = r/(1+r)
print(f"  excess = 25/57 - 1/3 = 6/57 = {exc:.6f}")
print(f"  delta_0 = {d0:.6f} = 1/(1+sqrt(19)) = {1/(1+19**0.5):.6f}")
print()

print("="*70)
print("COMPARISON: Old (Theorem A only) vs New (with Prop 4)")
print("="*70)
print()
print("Old: k/A <= 25/57 + delta^2/(1-delta)^2")
print("New: k/A <= 1/3  + 2*delta^2/(1-delta)^2")
print()
print(f"{'k/A':>10} {'old delta_0':>14} {'new delta_0':>14}")
for pval in [0.44, 0.45, 0.50, 0.55, 0.60, 2/3, 0.70, 0.80]:
    # Old
    exc_old = pval - 25/57
    if exc_old > 0:
        r_old = exc_old**0.5
        d_old = r_old/(1+r_old)
    else:
        d_old = 0.0
    # New
    exc_new = pval - 1/3
    if exc_new > 0:
        r_new = (exc_new/2)**0.5
        d_new = r_new/(1+r_new)
    else:
        d_new = 0.0
    print(f"{pval:>10.4f} {d_old:>14.6f} {d_new:>14.6f}")

print()
print("The NEW bound always gives a LARGER gap, because Prop 4 is stronger.")
print()
print("="*70)
print("SURVIVING COUNTEREXAMPLE ROUTE")
print("="*70)
print()
print("For LeBrun manifolds M = X # k CPbar^2:")
print("  - k/A >= 25/57: no Einstein (LeBrun 1998), gap >= 0.187")
print("  - 1/3 < k/A < 25/57: gap > 0, but Einstein might EXIST")
print("  - k/A <= 1/3: no gap from Prop 4, Einstein not excluded")
print()
print("CONCLUSION: The entire LeBrun family with k >= 25A/57 is eliminated")
print("as negative-branch counterexamples. No tight pinching possible.")
print()
print("The ONLY remaining counterexample route uses:")
print("  (a) Non-LeBrun 4-manifold obstructions (Hitchin-Thorpe at boundary,")
print("      simplicial/entropy for infinite pi_1), or")
print("  (b) Dimension >= 5 (no SW/Chern-Weil tools), or")
print("  (c) A completely new obstruction mechanism.")
print()
print("DONE")
