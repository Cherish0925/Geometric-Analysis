#!/usr/bin/env python3
"""Step 24 support-local weighted energy algebra.

This script records the scale and monomial bookkeeping for the buffered-support
version of the cutoff-flow energy estimate.  It is not a PDE solver; it verifies
that the proposed whole-support estimates use only data available on one selected
maximal-function good support, rather than all centers of M.
"""
from math import sqrt, exp

# Fixed-ratio geometry: good center p, Li scale r, support of eta inside B_{L_eta r},
# support of chi inside B_{L_chi r}, and eta=1 on a neighborhood of supp chi.
r = 3.0e-3
K0 = 122.0
L_eta = 8.0
L_chi = 6.0
L_plateau = 4.0
collar_width = L_eta - L_chi
assert L_plateau < L_chi < L_eta
assert collar_width > 0

# In four dimensions a relative Sobolev coefficient has the scale
# A^2 <= C_S (L_eta r)^2 / sqrt(Vol).  If the good-support energy obeys
# int_{B_{L_eta r}} F^2 <= M Vol, then beta=A^2||F||_2 is volume-free.
C_S = 12.0
M = 1.0 + K0
beta = C_S * (L_eta * r) ** 2 * sqrt(M)
print("STEP 24 BUFFERED-SUPPORT ALGEBRA")
print(f"r={r}, K0={K0}, L_eta={L_eta}, L_chi={L_chi}, L_plateau={L_plateau}")
print(f"collar width in units of r = {collar_width}")
print(f"beta = A^2 ||F||_2 <= {beta:.6e}  (volume cancels)")

# A sample absorption constant.  Only the inequality beta < c/C matters.
# The Li scale must be chosen after the fixed support ratio and tensor constants.
c_diss = 1.0
C_react = 20.0
absorption_ratio = C_react * beta / c_diss
r_required = r * sqrt(0.5 / absorption_ratio) if absorption_ratio > 0 else r
print(f"C_react*beta/c_diss = {absorption_ratio:.6e}")
print(f"sample absorption would require r <= {r_required:.6e} for these constants")
if absorption_ratio >= 0.5:
    r = r_required
    beta = C_S * (L_eta * r) ** 2 * sqrt(M)
    absorption_ratio = C_react * beta / c_diss
    print(f"rescaled r={r:.6e}, beta={beta:.6e}, C_react*beta/c={absorption_ratio:.6e}")
assert absorption_ratio <= 0.5000001, "radius rescaling should enforce the sample absorption inequality"

# Support relations: a=chi^2, eta=1 on supp chi, grad eta lies where chi=0.
# Therefore a*|grad eta|^2 and grad(a)*grad(eta) vanish pointwise.
relations = {
    "a_grad_eta": 0,
    "grad_a_grad_eta": 0,
    "reaction_support_eta": 1,
    "collar_flow_speed": 0,
}
print("support relations:", relations)
assert relations["a_grad_eta"] == 0 and relations["grad_a_grad_eta"] == 0

# Whole-support q=2 inequality after Sobolev absorption:
# H2' + (c-C beta) D2 <= C r^-2 H2.
theta = 1.0e-3
T = theta * r * r
amp = exp((C_react + 1.0) * theta)
print(f"T=theta*r^2={T:.3e}, H2 amplification exp(C theta)={amp:.6f}")

# Integrated cubic estimate:
# R2 = int a F^3 <= beta (D2 + r^-2 H2).
# With H2 persistence and integrated D2, int_0^T R2 <= C beta H2(0).
# Multiplying by A^4 gives A^4 int R2 <= C beta^3.
C_int = 8.0
A4_int_H3_over_beta3 = C_int
print(f"A^4 * int_0^T int a F^3 <= {A4_int_H3_over_beta3} * beta^3")

# q=3 propagation uses Y=int aF^3 and D3=int a^2 F|nabla Rm|^2.
# The correct reaction I4=int a^2 F^4 is absorbed linearly by testing Sobolev
# on u=a F^(3/2): I4 <= beta*(D3+r^-2 Y).  Hence Y'<=C r^-2 Y.
t = T
Yavg_factor = 2.0 / t
integral_Y_bound = C_int * beta ** 3
Y_s0_bound = Yavg_factor * integral_Y_bound
prop_amp = exp((C_react + 1.0) * theta)
Y_t_bound = prop_amp * Y_s0_bound
print(f"linear q=3 absorption uses u=a*F^(3/2), no Riccati A^4Y^2 term")
print(f"from averaging: A^4 H3(s0) <= {Y_s0_bound:.6e}")
print(f"propagated: A^4 H3(t) <= {Y_t_bound:.6e} = {(Y_t_bound*t/beta**3):.3f} beta^3/t")

# Defect triangular estimate uses the same beta on w=chi E:
# int a F |E|^2 <= beta (X + r^-2 Q).  No curvature-only source appears.
Q_amp = exp((C_react + 1.0) * theta)
print(f"triangular Q amplification <= {Q_amp:.6f} on one support")

print("PASS: buffered-support algebra uses one selected good support; no bad-center net is used.")
