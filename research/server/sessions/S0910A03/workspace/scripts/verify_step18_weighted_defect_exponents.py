#!/usr/bin/env python3
"""
Exact scaling checks for the Step 18 transition-inclusive weighted-defect plan.

This does not prove the geometric Moser estimate.  It verifies the exponent and
volume arithmetic needed by the proposed first-exit bootstrap:

  |aE(t)| <= C_p A_U^(4/p) t^(-2/p) ||E_0||_{L^p(U)}, p>2,

where in dimension four the norm-form relative Sobolev coefficient scales as
A_U ~ r Vol(U)^(-1/4).  Hence collapsed volume cancels and the drift is
integrable exactly for p>2.

It also records two obstructions corrected in Step 18:
  (i) a C/t curvature coefficient has divergent time integral;
  (ii) the direct critical-energy absorption coefficient at power m grows like
       m, so a fixed small energy cannot support m -> infinity.
"""
from fractions import Fraction
import math

# 1. Collapse-volume cancellation.
r = Fraction(3, 1000)
delta = Fraction(1, 10**6)
for p in (Fraction(5,2), Fraction(3,1), Fraction(4,1), Fraction(6,1)):
    # Track powers of V and r symbolically:
    # A_U^(4/p): r^(4/p) V^(-1/p), ||E0||_p: delta V^(1/p).
    v_power = -Fraction(1, 1) / p + Fraction(1, 1) / p
    r_power = Fraction(4, 1) / p
    assert v_power == 0
    print(f"p={p}: volume power={v_power}, r power={r_power}, time exponent={Fraction(2,1)/p}")

# 2. Integrability and scale-correct drift.
# Integral_0^(theta r^2) delta r^(4/p) t^(-2/p) dt
# = delta * theta^(1-2/p)/(1-2/p) * r^2.
theta = Fraction(1,100)
for p in (Fraction(5,2), Fraction(3,1), Fraction(4,1), Fraction(6,1)):
    alpha = Fraction(2,1)/p
    assert alpha < 1
    r_total = Fraction(4,1)/p + 2*(1-alpha)
    assert r_total == 2
    coeff = float(theta)**float(1-alpha) / float(1-alpha)
    print(f"p={p}: drift exponent in r={r_total}; dimensionless coefficient={coeff:.8g}")

# Critical endpoint p=2 is logarithmically divergent.
pcrit = Fraction(2,1)
assert Fraction(2,1)/pcrit == 1
print("p=2: time exponent=1 -> logarithmic divergence (excluded).")

# 3. C/t maximum-principle coefficient is not uniformly integrable at zero.
T = 1e-2
for eps in (1e-1, 1e-2, 1e-4, 1e-8):
    lower = eps**2
    integral = math.log(T/lower) if lower < T else 0.0
    print(f"Integral_[eps^2,T] dt/t, eps={eps:g}: {integral:.8g}")
assert math.log(T/(1e-16)) > math.log(T/(1e-8))

# 4. Fixed-energy direct absorption fails at arbitrarily high iteration power.
# If the reaction contributes c*m*sqrt(epsilon) times the gradient energy,
# absorption requires epsilon < const/m^2.
epsilon = 1e-6
c = 1.0
for m in (2, 3, 10, 100, 1000, 10000):
    reaction_ratio = c*m*math.sqrt(epsilon)
    print(f"m={m:5d}: model absorption ratio m*sqrt(eps)={reaction_ratio:g}")
assert 10000*math.sqrt(epsilon) > 1

print("PASS: weighted-defect scaling, p>2 drift integrability, C/t divergence, and high-power absorption obstruction verified.")
