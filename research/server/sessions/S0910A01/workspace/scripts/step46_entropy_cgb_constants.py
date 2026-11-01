"""
Step 46: constants for entropy/Chern--Gauss--Bonnet comparison.

This script is not a proof.  It records the scale-normalized numerical
relations used in the Step 46 mechanism comparison.
"""
import math

pi2 = math.pi**2

# Closed real-hyperbolic 4-manifold X, starting with K=-1 metric:
# Vol_{K=-1}(X) = (4*pi^2/3) chi(X).  Scaling by 3 gives Ric=-g.
real_hyp_norm_vol_over_chi = 9 * (4*pi2/3)

# Product of closed hyperbolic surfaces, each with K=-1 already has Ric=-g
# in real dimension 2, hence the product has Ric=-g in dimension 4.
# Area(Sigma_g)=4*pi(g-1), chi(Sigma_g)=2-2g, so Vol/chi=4*pi^2.
product_surface_norm_vol_over_chi = 4*pi2

# Ishida--LeBrun near-critical route uses a different calibrated variable A.
il_calibrated_vol_over_A = 32*pi2/9

# Entropy vs CGB for Y=X#X, where X is real-hyperbolic and normalized by Ric=-g.
# If an Einstein metric on Y has negative constant, scale to Ric=-g.
# Since tau(X)=0, tau(Y)=0 and chi(Y)=2 chi(X)-2.
# Bessieres/BCG-Sambusetti gives, after normalizing Ric=-g, lower
# Vol(Y) >= 2(1+eps) Vol_norm(X).  CGB for Einstein with tau=0 gives
# Vol(Y) <= 12*pi^2 chi(Y) = 2 Vol_norm(X) - 24*pi^2.
# The formal difference lower - upper is 24*pi^2*(eps*chiX + 1).
def entropy_cgb_gap(chi_x, eps):
    vol_x_norm = real_hyp_norm_vol_over_chi * chi_x
    lower = 2*(1+eps)*vol_x_norm
    upper = 12*pi2*(2*chi_x - 2)
    return lower - upper

print("normalized real hyperbolic Vol/chi =", real_hyp_norm_vol_over_chi)
print("normalized product of hyperbolic surfaces Vol/chi =", product_surface_norm_vol_over_chi)
print("IL calibrated Vol/A =", il_calibrated_vol_over_A)
print("ratios divided by pi^2:")
print("  real hyperbolic:", real_hyp_norm_vol_over_chi/pi2)
print("  product surfaces:", product_surface_norm_vol_over_chi/pi2)
print("  IL Vol/A:", il_calibrated_vol_over_A/pi2)
for chi_x in [2, 10, 100]:
    for eps in [0.0, 0.01, 0.1]:
        print(f"gap/(pi^2) for chiX={chi_x}, eps={eps}: {entropy_cgb_gap(chi_x, eps)/pi2:.6g}")

assert abs(real_hyp_norm_vol_over_chi/pi2 - 12) < 1e-12
assert abs(product_surface_norm_vol_over_chi/pi2 - 4) < 1e-12
assert abs(il_calibrated_vol_over_A/pi2 - 32/9) < 1e-12
assert entropy_cgb_gap(2, 0.0) > 0
print("constant checks passed")
