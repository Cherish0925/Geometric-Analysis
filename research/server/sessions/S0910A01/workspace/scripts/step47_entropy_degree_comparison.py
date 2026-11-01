"""
Step 47: elementary algebra for the entropy/Chern--Gauss--Bonnet degree-map route.

The script records scale constants and finite-dimensional inequalities only.
It does not verify the BCG theorem, the BBCG differentiable-rigidity theorem,
Sambusetti's theorem, or any Einstein existence/nonexistence result.
"""
import math

pi2 = math.pi**2

# Closed real-hyperbolic 4-manifold X with sectional curvature -1:
# Ric=-3g, scalar=-12, W=0, Ric^o=0, hence
#   chi(X)=(1/(8*pi^2))*int(s^2/24)=(1/(8*pi^2))*6*Vol.
VOL_HYP4_OVER_CHI = 4*pi2/3

# For ||g^{-1}(Ric_g+g)||_op <= delta, scaling g'=(1+delta)g/3 gives Ric(g')>=-3g'.
# Chern--Gauss--Bonnet yields Vol(g')/(|k|Vol(X)) <= chi(Y)/(abs(k)chi(X))*F(delta).
def F(delta: float) -> float:
    return (1 + delta)**2 / (1 - 2*delta - 2*delta*delta)

DELTA_DENOM_ROOT = (math.sqrt(3)-1)/2

# Taylor: F=1+4d+11d^2+O(d^3). Verify numerically at tiny d.
for d in [1e-6, 2e-6, 5e-6]:
    approx = 1 + 4*d + 11*d*d
    # The omitted cubic term is O(d^3), while double precision also contributes rounding.
    assert abs(F(d) - approx) < 1e-13

# Conservative small-delta bound useful for mental estimates: F(delta) <= 1 + 8 delta for delta <= 0.05.
for j in range(0, 51):
    d = j * 0.001
    assert F(d) <= 1 + 8*d + 1e-12

def cgb_upper_ratio(delta: float, chi_y: float, degree_abs: int, chi_x: float) -> float:
    return (chi_y/(degree_abs*chi_x))*F(delta)

# Connected sum X#X with degree-two map to X has chi=2chi(X)-2.
# The BCG lower bound is contradicted if (1-1/m)F(delta)<1, m=chi(X).
# Endpoint equality is also impossible for m>1 because BCG equality would force a twofold Riemannian covering,
# while chi(X#X)=2m-2 != 2m. The equation has positive root below.
def delta_threshold_connected_sum(m: float) -> float:
    assert m > 1
    return 2 / (4*m - 2 + math.sqrt(16*m*m - 4*m))

def delta_threshold_connected_sum_bisect(m: float) -> float:
    assert m > 1
    eta = 1 - 1/m
    lo, hi = 0.0, min(0.25, DELTA_DENOM_ROOT*0.99)
    for _ in range(100):
        mid = (lo + hi)/2
        if eta*F(mid) < 1:
            lo = mid
        else:
            hi = mid
    return lo

for m in [2, 3, 4, 10, 100, 1000, 10000]:
    exact = delta_threshold_connected_sum(m)
    bis = delta_threshold_connected_sum_bisect(m)
    assert abs(exact - bis) < 1e-14
    asymp = 1/(4*m) + 5/(64*m*m)
    if m >= 100:
        assert abs(exact - asymp) < 1/(m**3)

# Hyperbolic product surface ratio from Step 46: not universal for Vol/chi.
PRODUCT_SURFACE_RIC_MINUS_ONE_VOL_OVER_CHI = 4*pi2
IL_CALIBRATED_VOL_OVER_A = 32*pi2/9
REAL_HYP_RIC_MINUS_ONE_VOL_OVER_CHI = 9 * VOL_HYP4_OVER_CHI  # rescale sec=-1 by factor 3 to Ric=-g

print("Vol_hyp4(sec=-1)/chi =", VOL_HYP4_OVER_CHI, "=", VOL_HYP4_OVER_CHI/pi2, "pi^2")
print("Vol_hyp4(Ric=-g)/chi =", REAL_HYP_RIC_MINUS_ONE_VOL_OVER_CHI/pi2, "pi^2")
print("Vol_product_surfaces(Ric=-g)/chi =", PRODUCT_SURFACE_RIC_MINUS_ONE_VOL_OVER_CHI/pi2, "pi^2")
print("IL calibrated Vol/A =", IL_CALIBRATED_VOL_OVER_A/pi2, "pi^2")
print("denominator positive for delta <", DELTA_DENOM_ROOT)
print("F(delta) examples:")
for d in [0, 0.001, 0.01, 0.05, 0.1]:
    print(f"  delta={d:.3g}: F={F(d):.12g}, F-1={F(d)-1:.12g}")
print("X#X degree-two BCG-only thresholds (endpoint also impossible for chi>1):")
for m in [2, 4, 10, 100, 1000, 10000]:
    th = delta_threshold_connected_sum(m)
    print(f"  chi(X)={m:5d}: delta_*={th:.12g}, 4 chi delta_*={4*m*th:.8g}")

for delta in [0.0, 0.01, 0.03]:
    for m in [5, 50]:
        chi_y = 2*m - 2
        ratio = cgb_upper_ratio(delta, chi_y, 2, m)
        assert abs(ratio - (1 - 1/m)*F(delta)) < 1e-12

print("elementary entropy/CGB algebra checks passed")
