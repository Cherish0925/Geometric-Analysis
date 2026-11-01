#!/usr/bin/env python3
"""
Step 11: Compute the self-dual Weyl tensor and calibrated defect F
on the Taub-NUT-AdS metric with Ric = -g (ell^2 = 3).

The Taub-NUT-AdS metric is U(2)-symmetric (cohomogeneity one).
For such metrics, the curvature can be computed from the warping
functions alone.

We use the orthonormal frame approach:
  e^0 = dr/sqrt(F)
  e^1 = sqrt(r^2 - nu^2) dtheta
  e^2 = sqrt(r^2 - nu^2) sin(theta) dphi
  e^3 = 2*nu*sqrt(F) (dpsi + cos(theta) dphi)

and compute the connection 1-forms, curvature 2-forms, and
decompose into W+, W-, E, s.

Key test: Does the annular band at distance ~1/2 from the NUT
have F = 0 (compatible with the calibrated near-critical sequence)?
Or F > 0 (each NUT costs calibrated defect)?
"""
import sympy as sp
from sympy import sqrt, Rational, pi, symbols, simplify, diff, Matrix
import numpy as np

print("="*70)
print("TAUB-NUT-ADS CURVATURE AND CALIBRATED DEFECT")
print("="*70)

# Parameters
nu = sp.Symbol('nu', positive=True)
r = sp.Symbol('r', positive=True)
ell2 = sp.Integer(3)  # ell^2 = 3 for Ric = -g

# F function
F_expr = (r - nu)/(r + nu) * (1 + (r - nu)*(r + 3*nu)/ell2)

print("\n--- 1. Metric functions ---")
print(f"F(r) = {F_expr}")
F_simplified = sp.simplify(sp.expand(F_expr))
print(f"     = {F_simplified}")

# Derivatives needed for curvature
Fp = sp.diff(F_expr, r)
Fpp = sp.diff(F_expr, r, 2)

# Define h(r) = r^2 - nu^2 for the base S^2 factor
h = r**2 - nu**2
hp = sp.diff(h, r)  # = 2r
hpp = sp.diff(h, r, 2)  # = 2

# For U(2)-symmetric Einstein metrics, the curvature components
# in the orthonormal frame are determined by F, h, and their derivatives.
# 
# The self-dual Weyl tensor W+ acts on Lambda^2_+ = span{e01+e23, e02-e13, e03+e12}
# where eij = e^i wedge e^j.
#
# For cohomogeneity-one metrics ds^2 = dr^2/F + h*g_S2 + F*l^2*(dpsi+A)^2
# (where l = 2*nu here), the curvature has special structure.

# Let me compute numerically at a specific point.
# Take nu = 0.01 (small, to see the collapsing regime)
# and r at distance ~1/2 from the NUT

print("\n--- 2. Numerical evaluation at nu=0.01, r=0.51 ---")
nu_val = 0.01
r_val = 0.51  # approximately distance 1/2 from NUT at r=nu

subs = {nu: nu_val, r: r_val}

F_val = float(F_expr.subs(subs))
Fp_val = float(Fp.subs(subs))
Fpp_val = float(Fpp.subs(subs))
h_val = float(h.subs(subs))
hp_val = float(hp.subs(subs))

print(f"nu = {nu_val}")
print(f"r = {r_val}")
print(f"F = {F_val:.6f}")
print(f"F' = {Fp_val:.6f}")
print(f"F'' = {Fpp_val:.6f}")
print(f"h = r^2-nu^2 = {h_val:.6f}")
print(f"h' = 2r = {hp_val:.6f}")

# For the U(2)-symmetric metric 
# g = dr^2/F + h*(dtheta^2+sin^2 theta dphi^2) + 4*nu^2*F*(dpsi+cos theta dphi)^2
# The orthonormal frame:
# e0 = dr/sqrt(F), e1 = sqrt(h)*dtheta, e2 = sqrt(h)*sin theta*dphi
# e3 = 2*nu*sqrt(F)*(dpsi + cos theta dphi)
#
# Connection and curvature via Cartan's structural equations.
# Key curvature components for the SD Weyl:

# Define auxiliary quantities
a_sq = h_val  # coefficient of g_S2
b_sq = 4 * nu_val**2 * F_val  # coefficient of (dpsi+A)^2
a = np.sqrt(a_sq)
b = np.sqrt(b_sq)

# Radial derivatives in proper distance dr/sqrt(F):
# d/ds = sqrt(F) d/dr
sqrtF = np.sqrt(F_val)
a_dot = sqrtF * hp_val / (2*a)  # d(sqrt(h))/ds = sqrt(F) * r / sqrt(h)
b_dot_raw = sqrtF * float(sp.diff(2*nu*sqrt(F_expr), r).subs(subs))

print(f"\na (base S^2 radius) = {a:.6f}")
print(f"b (fiber circle * 2nu) = {b:.6f}")
print(f"a_dot (wrt proper dist) = {a_dot:.6f}")

# For Einstein Ric = -g on 4-manifold with U(2) symmetry,
# the curvature tensor in the ON frame {e0,e1,e2,e3} has specific form.
# The self-dual 2-forms are:
# omega1 = e0^e1 + e2^e3
# omega2 = e0^e2 - e1^e3 (or + depending on orientation)
# omega3 = e0^e3 + e1^e2
#
# W+ is a trace-free symmetric 3x3 matrix in this basis.

# For a cohomogeneity-one biaxial Bianchi IX metric
# (which includes Taub-NUT-AdS), the W+ matrix is DIAGONAL
# in the SD basis, with eigenvalues determined by the metric functions.
#
# From Dancer-Wang or Hitchin's classification:
# The SD Weyl eigenvalues for the orthogonal frame
# can be expressed as:
#
# Using the standard formulas for a metric
# g = ds^2 + a(s)^2 sigma_1^2 + a(s)^2 sigma_2^2 + c(s)^2 sigma_3^2
# (left-invariant frame on S^3)
# where a1=a2=a, a3=c (biaxial).
#
# For Taub-NUT-AdS with the standard SU(2) frame,
# a = sqrt(h) (the S^2 factor), c = 2*nu*sqrt(F) (the fiber).

# Actually, let me just compute the full Riemann tensor numerically.
# It's easier and more reliable than tracking sign conventions.

# I'll use a slightly different approach: compute the metric components,
# then use automatic differentiation to get Christoffel and Riemann.

print("\n--- 3. Full numerical curvature computation ---")

# Use a coordinate patch: (t, theta, phi, psi) where t = proper distance from NUT
# The metric in these coordinates is diagonal at theta=pi/2:
# g = dt^2 + h(r(t))*dtheta^2 + h(r(t))*sin^2(theta)*dphi^2 
#     + 4*nu^2*F(r(t))*(dpsi+cos(theta)*dphi)^2
# where r = r(t) satisfies dr/dt = sqrt(F).

# At theta=pi/2, the metric tensor in (t,theta,phi,psi) has off-diagonal
# terms from the (dpsi+cos theta dphi)^2 cross-term.
# At theta=pi/2: cos(theta) = 0, so g_psi_phi = 0 and the metric IS diagonal:
#   g_tt = 1
#   g_theta_theta = h
#   g_phi_phi = h + 0 = h  (since sin^2(pi/2) = 1 and cos^2(pi/2) = 0)
#   g_psi_psi = 4*nu^2*F

# For the curvature at this point, I need derivatives.
# But the cross-term d(cos theta)/dtheta = -sin(theta) at theta=pi/2 is -1.
# This generates the Hopf connection curvature.

# Let me use a cleaner computational approach with sympy and finite differences.
# I'll compute the Riemann tensor at a specific point numerically.

# For a biaxial cohomogeneity-1 metric on S^3 x R:
# g = ds^2 + a(s)^2*(sigma_1^2 + sigma_2^2) + c(s)^2*sigma_3^2
# where sigma_i are left-invariant 1-forms on SU(2) with d sigma_i = sigma_j ^ sigma_k.
#
# The curvature of such metrics is well-known. In the ON frame
# e^0=ds, e^1=a*sigma_1, e^2=a*sigma_2, e^3=c*sigma_3:
#
# R_{0101} = R_{0202} = -a''/a
# R_{0303} = -c''/c
# R_{1212} = -(a')^2/a^2 + c^2/(4a^4)
# R_{0312} = (a')c'/(ac) - c^2/(4a^4) ... no, this isn't right.

# Let me use the standard formulas from Berger or Besse.
# For the metric g = ds^2 + a^2(s)(sigma_1^2+sigma_2^2) + c^2(s)sigma_3^2:
#
# Connection 1-forms:
# omega^0_1 = a'/a * e^1
# omega^0_2 = a'/a * e^2
# omega^0_3 = c'/c * e^3
# omega^1_2 = (1/(2a^2) - c/(4a^2)) * e^3 ... hmm, signs depend on convention

# Let me just use the Berard-Bergery / Page / Dancer formulas directly.
# For Bianchi IX biaxial (a1=a2=a, a3=c):
# We use f_i = a_i'/a_i as Hubble-type variables.
# f = a'/a, g_h = c'/c (avoiding name clash with metric g)

# The non-zero curvature components in ON frame are:
# R_{0101} = R_{0202} = -f' - f^2
# R_{0303} = -g_h' - g_h^2
# R_{1212} = -f^2 + mu  (where mu = c^2/(4a^4))
# R_{0312} = -(f*g_h - 2*mu + mu)  # this needs careful derivation
# R_{1313} = R_{2323} = -f*g_h + mu

# Actually, the correct formulas for left-invariant metrics on S^3 bundles are:
# (from O'Neill or Besse, Chapter 9)
# 
# Sectional curvatures for the biaxial case:
# K(e0,e1) = K(e0,e2) = -a''/a
# K(e0,e3) = -c''/c
# K(e1,e2) = -(a'/a)^2 + c^2/(4a^4)
# K(e1,e3) = K(e2,e3) = -(a'c')/(ac) + c/(4a^4) * ??? 

# This is getting complicated with conventions. Let me use the known
# result for Taub-NUT-AdS and just compute the defect.

# SIMPLER APPROACH: Since Ric = -g is exact, we know s = -4 and E = 0.
# The curvature decomposition gives:
# |Rm|^2 = |W+|^2 + |W-|^2 + s^2/24 = |W+|^2 + |W-|^2 + 2/3
#
# Also: |W+|^2 + |W-|^2 = |W|^2, and for the Taub-NUT-AdS metric,
# the total |W|^2 can be computed from the known curvature formulas.

# For a self-dual metric (W- = 0), which Taub-NUT-AdS is known to be:
# |W-|^2 = 0, so |W+|^2 = |W|^2

# KEY QUESTION: Is Taub-NUT-AdS self-dual?
# 
# YES: The Pedersen metric (Taub-NUT-AdS) is HALF-CONFORMALLY-FLAT.
# For the standard orientation, W- = 0 (self-dual).
# This is proven in Pedersen (1986) and Hitchin (1995).
#
# For the OPPOSITE orientation: W+ = 0, W- = old W+.
# The F defect in this orientation would be HUGE since |W+| = 0.
#
# For the standard (self-dual) orientation: W+ = W ≠ 0.
# Need to compute |W+|^2 and spectrum.

print("Taub-NUT-AdS is SELF-DUAL (W- = 0) in the standard orientation.")
print("In this orientation: |W|^2 = |W+|^2.")
print()

# For the self-dual orientation, on an Einstein manifold with W- = 0:
# |Rm|^2 = |W+|^2 + 0 + 0 + 2/3
# So we need |W+|^2 to determine |Rm|^2.

# For Taub-NUT-AdS, the W+ eigenvalues are known to be of the form:
# w1 = w2 = w, w3 = -2w (trace-free, two equal eigenvalues)
# This is because the U(2) symmetry forces W+ to have a preferred 
# direction (the Kähler direction in the SD bundle).

# At the NUT (r -> nu): the metric approaches flat R^4, so W+ -> 0.
# Far from the NUT (r -> infinity): the metric approaches AdS_4,
# which has |W+|^2 = |W-|^2 = s^2/24 = 2/3 (each) ... 
# wait, AdS_4 is conformally flat, so W = 0!

# Hmm, but Taub-NUT-AdS is NOT asymptotically AdS_4 in the usual sense
# when nu > 0. For nu -> 0, it degenerates.

# Let me just compute |W+|^2 numerically for a specific (nu, r).
# I'll use the formula: |W+|^2 = |Rm|^2 - 2/3 (since W- = 0, E = 0).
# And |Rm|^2 can be computed from the sectional curvatures.

# For the biaxial Bianchi IX metric in proper distance s:
# g = ds^2 + a(s)^2(sigma_1^2+sigma_2^2) + c(s)^2*sigma_3^2
# 
# a = sqrt(r^2 - nu^2), c = 2*nu*sqrt(F(r))
# ds = dr/sqrt(F(r))
#
# So: a' = da/ds = sqrt(F)*da/dr = sqrt(F)*r/sqrt(r^2-nu^2)
#     c' = dc/ds = sqrt(F)*dc/dr
#     a'' = d(a')/ds = sqrt(F)*d(a')/dr

# Let me compute a' and c' symbolically
a_sym = sp.sqrt(r**2 - nu**2)
c_sym = 2*nu*sp.sqrt(F_expr)
sqrtF_sym = sp.sqrt(F_expr)

# Derivatives with respect to proper distance: d/ds = sqrt(F) * d/dr
a_prime = sp.simplify(sqrtF_sym * sp.diff(a_sym, r))  # da/ds
c_prime = sp.simplify(sqrtF_sym * sp.diff(c_sym, r))  # dc/ds

# Second derivatives: d^2a/ds^2 = sqrt(F) * d(a')/dr
a_dprime = sp.simplify(sqrtF_sym * sp.diff(a_prime, r))  # d^2a/ds^2
c_dprime = sp.simplify(sqrtF_sym * sp.diff(c_prime, r))  # d^2c/ds^2

# Hubble-type variables
f_sym = a_prime / a_sym  # a'/a
g_sym = c_prime / c_sym  # c'/c

# For Bianchi IX biaxial metric, the mu parameter:
mu_sym = c_sym**2 / (4 * a_sym**4)

# Einstein condition Ric = -g gives specific ODEs.
# The key Riemann components in ON frame {e0=ds, e1=a*s1, e2=a*s2, e3=c*s3}:
# 
# For the standard Berger/O'Neill formulas on S^3 fibration:
# R0101 = R0202 = -a''/a
# R0303 = -c''/c
# R1212 = -(a'/a)^2 + c^2/(4*a^4) = -f^2 + mu
# R1313 = R2323 = -(a'/a)(c'/c) + c^2/(4*a^4) = -f*g + mu
# R0312 = a'c/(2a^3) - c'/(2a) ... hmm, the off-diagonal term
#
# Actually, for Bianchi IX with left-invariant 1-forms:
# [sigma_1, sigma_2] = sigma_3 (standard SU(2) convention)
# The connection forms and curvature require careful treatment.
# 
# Let me use the result from Dancer-Wang (2009) or similar references.
# For biaxial (a1=a2=a, a3=c) Bianchi IX:
#
# R_{0101} = -a''/a
# R_{0202} = -a''/a  
# R_{0303} = -c''/c
# R_{1212} = -f^2 + mu
# R_{1313} = R_{2323} = -f*g_h + mu
# R_{0312} = f_3 * something ... 
# 
# The tricky part is R_{0312} and similar mixed components.
# For biaxial case, by SU(2) symmetry, R_{0312} must have a specific form.

# Let me instead compute the sectional curvatures and the full curvature tensor
# using the Ricci equation to fill in the gaps.
#
# We know Ric = -g, so:
# R_{00} = R_{0101} + R_{0202} + R_{0303} = -1
# R_{11} = R_{0101} + R_{1212} + R_{1313} = -1
# R_{33} = R_{0303} + R_{1313} + R_{2323} = -1
# R_{01} = R_{02} = R_{03} = 0 (by symmetry)
# R_{12} = 0 (by biaxial symmetry)
# R_{13} = R_{23} = 0 (by symmetry)

# From R_{00} = -1:
# -a''/a - a''/a - c''/c = -1
# => 2a''/a + c''/c = 1  ... (*)

# Evaluate numerically
f_val = float(f_sym.subs(subs))
g_val = float(g_sym.subs(subs))
mu_val = float(mu_sym.subs(subs))
a_d_val = float(a_dprime.subs(subs))
c_d_val = float(c_dprime.subs(subs))
a_val = float(a_sym.subs(subs))
c_val = float(c_sym.subs(subs))

print(f"a = {a_val:.6f}")
print(f"c = {c_val:.6f}")
print(f"a' = {float(a_prime.subs(subs)):.6f}")
print(f"c' = {float(c_prime.subs(subs)):.6f}")
print(f"a'' = {a_d_val:.6f}")
print(f"c'' = {c_d_val:.6f}")
print(f"f = a'/a = {f_val:.6f}")
print(f"g = c'/c = {g_val:.6f}")
print(f"mu = c^2/(4a^4) = {mu_val:.6f}")

# Curvature components
R0101 = -a_d_val / a_val
R0303 = -c_d_val / c_val
R1212 = -f_val**2 + mu_val
R1313 = -f_val * g_val + mu_val

print(f"\nCurvature components:")
print(f"R0101 = R0202 = {R0101:.6f}")
print(f"R0303 = {R0303:.6f}")
print(f"R1212 = {R1212:.6f}")
print(f"R1313 = R2323 = {R1313:.6f}")

# Check Ricci: R00 = R0101 + R0202 + R0303 should be -1
R00 = 2*R0101 + R0303
R11 = R0101 + R1212 + R1313
R33 = R0303 + 2*R1313
print(f"\nRicci check (should be -1):")
print(f"R00 = {R00:.6f}")
print(f"R11 = R22 = {R11:.6f}")
print(f"R33 = {R33:.6f}")

# Scalar curvature
s_val = R00 + 2*R11 + R33
print(f"s = {s_val:.6f} (should be -4)")

# Now compute W+ eigenvalues
# Self-dual basis: omega_1 = e01+e23, omega_2 = e02-e13, omega_3 = e03+e12
# W+ matrix in this basis:
# W+_{11} = (R0101 + R2323 + 2*R0123)/2 - s/12
# Actually, for biaxial Bianchi IX, R0123 = 0 by symmetry.
# The SD Weyl components are:
# W+_{ij} = R+(omega_i, omega_j) - (s/12)*delta_{ij}
# where R+ is the self-dual curvature operator.

# The curvature operator R: Lambda^2 -> Lambda^2 has the following 
# entries in the basis {e01, e02, e03, e23, e13, e12}:
# For biaxial Bianchi IX, by SU(2) symmetry, the self-dual block is:
# R+(omega_1, omega_1) = R0101 + R2323 + 2*R0123
# For biaxial: R0123 = R_{0123} = 0 (no mixed terms by U(2) symmetry)

# Wait, for Bianchi IX with structure constants [sigma_1,sigma_2]=sigma_3:
# there IS a non-zero R0312 component related to the O'Neill curvature.
# For a biaxial metric, by symmetry:
# R_{0312} = R_{0321} = some function of a, c and derivatives
#
# The general formula for Bianchi IX is:
# R0312 = (ac'/2a^2 - a'c/2a^2) * (structure constant contribution)
# This comes from the connection form omega^1_2 having a vertical component.

# For the biaxial SU(2) fibration, the connection forms are:
# omega^1_2 = (c^2/(4a^2) + 1 - 1/(2a^2)*c^2) * e^3 / ? ...
# I'm getting confused. Let me use a different approach.

# For the ON frame, the structure equations give:
# d(e^1) = -omega^1_0 wedge e^0 - omega^1_2 wedge e^2 - omega^1_3 wedge e^3
# But e^1 = a*sigma_1, so d(e^1) = a'*ds wedge sigma_1 + a*d(sigma_1)
# = a'/a * e^0 wedge e^1 + a * sigma_2 wedge sigma_3  (since dsigma_1 = sigma_2^sigma_3)
# = f * e^0 wedge e^1 + (a/c) * e^2 wedge e^3
# Wait: a*sigma_2 = e^2 and sigma_3 = e^3/c, so a*sigma_2^sigma_3 = e^2 wedge (e^3/c) = (1/c)*e^2^e^3.
# So d(e^1) = f*e^0^e^1 + (1/c)*e^2^e^3

# Similarly:
# d(e^2) = f*e^0^e^2 - (1/c)*e^1^e^3
# d(e^3) = g*e^0^e^3 + (c/(2a^2))*e^1^e^2

# (The last one: d(e^3) = d(c*sigma_3) = c'*ds^sigma_3 + c*d(sigma_3)
# d(sigma_3) = sigma_1^sigma_2, c*sigma_1^sigma_2 = c*(e^1/a)^(e^2/a) = (c/a^2)*e^1^e^2)

# Comparing with d(e^i) = -omega^i_j ^ e^j:
# From d(e^1):
# omega^1_0 = -f*e^1  (coeff of e^0)
# omega^1_2 = ? From e^2^e^3 term: need -omega^1_2 ^ e^2 - omega^1_3 ^ e^3 to give (1/c)*e^2^e^3
# Write omega^1_2 = alpha*e^0 + beta*e^1 + gamma*e^3 (by antisymmetry in index 1,2 no e^2)
# -omega^1_2 ^ e^2 = -alpha*e^0^e^2 - beta*e^1^e^2 - gamma*e^3^e^2
# -omega^1_3 ^ e^3 = 0 if omega^1_3 has no e^3 component... 
# This is getting unwieldy. Let me use the key result that for biaxial Bianchi IX:

# omega^1_2 = -kappa * e^3  where kappa = c/(2a^2) - ... I need the exact formula.
# From Besse Chapter 9 or Dancer-Wang:
# For the biaxial case with [sigma_1,sigma_2]=sigma_3:
# omega^1_2 = (1 - c^2/(2a^2)) * e^3 / c = (1/(c) - c/(2a^2)) * e^3

# Let me just define: from structure equations,
# d(e^1) + omega^1_0 ^ e^0 + omega^1_2 ^ e^2 + omega^1_3 ^ e^3 = 0
# We found: d(e^1) = f*e^0^e^1 + (1/c)*e^2^e^3
# omega^1_0 = f*e^1 => omega^1_0 ^ e^0 = f*e^1^e^0 = -f*e^0^e^1
# So the rest must cancel the (1/c)*e^2^e^3:
# omega^1_2 ^ e^2 + omega^1_3 ^ e^3 = (1/c)*e^2^e^3

# Write omega^1_2 = p*e^3 (by symmetry, only e^3 component)
# omega^1_3 = q*e^2 (by symmetry, only e^2 component)
# Then: p*e^3^e^2 + q*e^2^e^3 = (q-p)*e^2^e^3 = (1/c)*e^2^e^3
# => q - p = 1/c

# From d(e^3) = g*e^0^e^3 + (c/(2a^2))*e^1^e^2:
# omega^3_0 = g*e^3, omega^3_1 ^ e^1 + omega^3_2 ^ e^2 = (c/(2a^2))*e^1^e^2
# omega^3_1 = -q*e^2 (from omega^1_3 = q*e^2 => omega^3_1 = -q*e^2)
# omega^3_2 = -p'*e^1 (similarly from omega^2_3)
# By biaxial symmetry, omega^2_3 = p*e^1 (same p as omega^1_2 = p*e^3)
# => omega^3_2 = -p*e^1
# -q*e^2^e^1 - p*e^1^e^2 = (q-p)*e^1^e^2 = (c/(2a^2))*e^1^e^2
# => q - p = c/(2a^2)

# But we also got q - p = 1/c from above. So: 1/c = c/(2a^2), i.e., c^2 = 2a^2.
# This can't be right in general! Let me recheck.

# Actually, I made an error. From d(e^1):
# d(e^1) = (a'/a)*e^0^e^1 + (1/c)*e^2^e^3
# Wait, let me redo: e^2 = a*sigma_2, e^3 = c*sigma_3
# a*d(sigma_1) = a*sigma_2^sigma_3 = a*(e^2/a)^(e^3/c) = (1/c)*e^2^e^3.
# OK so d(e^1) = f*e^0^e^1 + (1/c)*e^2^e^3. Correct.

# From d(e^3) = g*e^0^e^3 + ...
# d(e^3) = c'*ds^sigma_3 + c*d(sigma_3)
# d(sigma_3) = sigma_1^sigma_2
# c*sigma_1^sigma_2 = c*(e^1/a)*(e^2/a) = (c/a^2)*e^1^e^2
# So d(e^3) = g*e^0^e^3 + (c/a^2)*e^1^e^2. Correct.

# The discrepancy: from e^1 we got q-p = 1/c, from e^3 we got q-p = c/a^2.
# But e^3 gives omega^3_1^e^1 + omega^3_2^e^2 = (c/a^2)*e^1^e^2
# omega^3_1 = -omega^1_3, omega^3_2 = -omega^2_3
# By biaxial symmetry: omega^1_3 = q*e^2 and omega^2_3 = -q*e^1 (antisymmetric in 1,2)
# No wait: omega^2_3 should have similar structure to omega^1_3 by the biaxial symmetry.
# By the biaxial (a1=a2) symmetry, omega^1_2 has only e^3, omega^1_3 has e^2 and maybe e^0,
# omega^2_3 has e^1 and maybe e^0.

# Let me use a more systematic approach.
# omega^i_j = A^i_j_k e^k, antisymmetric in i,j.
# From biaxial symmetry: A^1_2_3 = p, A^1_3_2 = q, A^2_3_1 = -p' (by SU(2) rotation)
# Actually the biaxial symmetry means rotation in the (1,2) plane:
# omega^1_2 is a connection form on the (1,2)-plane, and by symmetry only has e^3 component
# omega^1_3 has e^2 and possibly e^0 components (mixing radial and angular)
# omega^2_3 has e^1 and possibly e^0 components
# By the equivariance under (e^1,e^2) -> (-e^2,e^1):
# omega^1_3 = q*e^2 + s'*e^0
# omega^2_3 = q*e^1 + t'*e^0
# Hmm, this isn't quite right either.

# OK let me just compute the curvature from known results.
# For biaxial Bianchi IX Einstein metrics, there's a standard result:

# The 6 independent curvature components (in the ON frame, using symmetry) are:
# R_{0101} = -a''/a
# R_{0303} = -c''/c  
# R_{1212} = -(a')^2/a^2 + c^2/(4a^4)
# R_{1313} = -(a'c')/(ac) + c/(2a^2) * (... correction from curvature of S^3)
# R_{0312} = (mixed term from the fibration)
# R_{2323} = R_{1313} (by biaxial symmetry)
# R_{0102} = R_{0103} = 0 (by symmetry)

# For the fibration S^3 -> S^2 with standard SU(2) structure:
# The O'Neill A-tensor contributes to R_{0312} and modifies R_{1313}.
# 
# From Berard-Bergery-Bourguignon or the standard Riemannian submersion formulas:
# For the Hopf fibration sigma_3 with total space metric
# g = ds^2 + a^2(sigma_1^2+sigma_2^2) + c^2*sigma_3^2:
#
# The curvature tensor picks up corrections from the structure constants.
# Specifically, using [sigma_1,sigma_2] = sigma_3:
#
# R_{1313} = -(a'c')/(ac) + c^2/(4a^4) - c/(2a^2) * (something)
# 
# Actually, I found a reliable source: Gibbons-Pope (1979) or
# Berger (2003) "A panoramic view", Chapter 9.

# Let me use the final result instead:
# For Einstein Ric = -g, we have the constraint equations that determine
# a(s) and c(s). The curvature can be computed from these.

# Actually, the simplest approach is: since we know Ric = -g,
# and we know some curvature components from the warping functions,
# we can use the Ricci equations to determine the remaining components.

# We have:
# Ric(e_0, e_0) = R_{0101} + R_{0202} + R_{0303} = -1
# => -2*(a''/a) - c''/c = -1
#
# Ric(e_1, e_1) = R_{0101} + R_{1212} + R_{1313} = -1
# Ric(e_3, e_3) = R_{0303} + R_{1313} + R_{2323} = -1

# From Ric(e_0, e_0): already verified numerically above.

# For the W+ eigenvalues, the self-dual curvature operator acts on
# the SD basis omega_i. For a diagonal curvature (which biaxial isn't 
# quite), W+ would be:
# W+_{11} = (R_{0101} + R_{2323})/2 - s/12  (on omega_1 = e01+e23)
# W+_{22} = (R_{0202} + R_{1313})/2 - s/12  (on omega_2 = e02-e13, approximately)
# W+_{33} = (R_{0303} + R_{1212})/2 - s/12  (on omega_3 = e03+e12)
# But there could be off-diagonal terms from R_{0312}.

# For biaxial Bianchi IX, there is a key additional component:
# The curvature R(omega_1, omega_2) involves R_{0312}.
# By the U(1) x SU(2) symmetry (actually U(2)):
# W+ is DIAGONAL in the SD basis with eigenvalues
# lambda_1 = (R0101 + R1313 + R0312)/... no

# I think the cleanest way is to note that for the Pedersen metric (Taub-NUT-AdS),
# which is KNOWN to be self-dual (W- = 0), the W+ eigenvalues can be
# computed from the formula:
# W+ = curvature operator restricted to Lambda^2_+ minus (s/12)*Id

# For a SELF-DUAL metric (W- = 0), the full curvature operator has
# the block structure:
# Rm = [[W+ + s/12, 0], [0, s/12]] + [[0, 0], [0, 0]] (E = 0)
# in the (Lambda^2_+, Lambda^2_-) decomposition.

# Hmm wait, for Einstein: Rm = W + (s/12)*Id on Lambda^2.
# For W- = 0: Rm|_{Lambda^2_-} = (s/12)*Id|_{Lambda^2_-}
# and Rm|_{Lambda^2_+} = W+ + (s/12)*Id|_{Lambda^2_+}

# The eigenvalues of Rm on Lambda^2_- are all s/12 = -1/3.
# This means K(sigma) = -1/3 for every anti-self-dual 2-plane.

# Now, R_{0101} = K(e_0 wedge e_1) = (1/2)(K(e01+e23) + K(e01-e23))
# where e01+e23 is self-dual and e01-e23 is anti-self-dual.
# K(e01-e23) = -1/3 (since it's anti-self-dual and W-=0).
# So R_{0101} = (1/2)(K(omega_1) + (-1/3)) = (1/2)(lambda_1 + s/12 - 1/3)
# = (1/2)(lambda_1 + (-1/3) - 1/3)
# Hmm, let me be more careful.

# For a 2-form alpha in Lambda^2, the sectional curvature of the 
# corresponding 2-plane is <Rm(alpha), alpha>/<alpha, alpha>.
# 
# Rm(omega_1) = (W+ + s/12)*omega_1 = (lambda_1 + s/12)*omega_1
# where lambda_1 is the W+ eigenvalue.
# So K(omega_1) = lambda_1 + s/12 = lambda_1 - 1/3.

# The anti-self-dual companion of omega_1 = e01+e23 is omega_1' = e01-e23.
# Rm(omega_1') = (0 + s/12)*omega_1' = (-1/3)*omega_1'
# So K(omega_1') = -1/3.

# Now: R_{0101} = <Rm(e0^e1), e0^e1> = (1/2)<Rm(omega_1+omega_1'), omega_1+omega_1'>
# = (1/2)(K(omega_1) + K(omega_1')) 
# = (1/2)(lambda_1 - 1/3 + (-1/3))
# = (1/2)(lambda_1 - 2/3)

# Similarly for R_{0303}:
# omega_3 = e03+e12, omega_3' = e03-e12
# R_{0303} = (1/2)(K(omega_3) + K(omega_3')) = (1/2)(lambda_3 - 2/3)

# And R_{1212} (from omega_3 = e03+e12... wait, e12 is part of omega_3):
# Actually e^1^e^2 is part of omega_3 = e^0^e^3 + e^1^e^2.
# R_{1212} = <Rm(e^1^e^2), e^1^e^2> = (1/2)<Rm(omega_3-omega_3''), ...>
# Hmm, this decomposition doesn't work simply for individual 2-forms.

# Let me use the simpler formula. For a self-dual Einstein metric:
# R_abcd = W+_{abcd} - (1/3)(g_ac*g_bd - g_ad*g_bc)
# (using the convention that Rm = W + (s/12)*Kulkarni-Nomizu of g)

# In the ON frame:
# R_{0101} = W+_{0101} - 1/3
# R_{0303} = W+_{0303} - 1/3
# R_{1212} = W+_{1212} - 1/3
# R_{1313} = W+_{1313} - 1/3
# R_{0312} = W+_{0312}

# The W+ eigenvalues can then be extracted from the curvature operator
# restricted to Lambda^2_+.
# 
# For the basis omega_1=e01+e23, omega_2=e02-e13, omega_3=e03+e12:
# <Rm(omega_1), omega_1> = R_{0101} + R_{2323} + 2*R_{0123}
# For biaxial: R_{0123} = 0 (no such component by U(2) symmetry... or is there?)
# Actually, for the SU(2) Hopf fibration, R_{0123} need not be zero.

# But in the SD-ASD decomposition for a SELF-DUAL metric:
# R_{0123} contributes only to the SD part.
# And by biaxial symmetry, the SD curvature operator is diagonal!
# (because U(2) acts transitively on the unit sphere in Lambda^2_+)
# No wait, U(2) doesn't act transitively on the SD forms. 
# The U(1) factor distinguishes omega_3 from omega_1, omega_2.

# For Taub-NUT-AdS, W+ has eigenvalues of the form (w, w, -2w)
# where the double eigenvalue is on the plane perpendicular to the
# preferred direction (the Kähler form of the quaternionic Kähler structure).

# This means: W+ has TWO distinct eigenvalues: a double and a simple.
# The simple eigenvalue is -2w, the double is w.

# At the calibrated spectrum: (-1/6, 1/12, 1/12).
# So simple = -1/6 and double = 1/12.
# If Taub-NUT-AdS has (w, w, -2w), we need w = 1/12, -2w = -1/6.
# This matches! Could Taub-NUT-AdS actually achieve the calibrated spectrum?

# But Derdzinski says: calibrated spectrum + Einstein Ric=-g => locally Kahler.
# And Taub-NUT-AdS IS locally Kahler... it's quaternionic Kahler, which in 4D
# means Einstein and locally conformal to Kahler!

# Wait. In 4D, "quaternionic Kähler" means the holonomy is in Sp(1)·Sp(1),
# which is the same as SO(4). That's not a restriction. Actually, in 4D,
# all orientable Riemannian manifolds are "quaternionic Kähler" vacuously.
# The interesting condition is that the metric is self-dual (W- = 0).

# For a self-dual Einstein metric in 4D: Derdzinski's theorem says that
# if W+ has at most 2 eigenvalues and delta(W+) = 0, then it's locally
# conformally Kahler. For Einstein, delta(W+) = 0 automatically.
# And if W+ has the two-eigenvalue structure (w, w, -2w) everywhere,
# then by Derdzinski, (24|W+|^2)^{1/3} g is locally Kahler.

# For Taub-NUT-AdS: |W+|^2 = 6w^2 (trace-free: 2w^2 + 4w^2 = 6w^2).
# The conformal factor is (24*6w^2)^{1/3} = (144w^2)^{1/3}.
# If this is constant, then the metric itself is locally Kähler.
# If w varies (as it does along the radial direction), the factor varies.

# KEY: w varies with r on Taub-NUT-AdS! So the conformal factor is NOT constant,
# and the metric is locally CONFORMALLY Kähler, not locally Kähler.

# The Derdzinski contradiction requires: conformal factor = constant AND 
# Ric = -g AND locally Kähler => |W+|^2 = s^2/24 = 2/3.
# But our calibrated value is |W+|^2 = 1/24.
# Conformal factor = (24*1/24)^{1/3} = 1 only when |W+|^2 = 1/24.

# For Taub-NUT-AdS: w varies, so |W+|^2 = 6w^2 varies.
# At some radius r*, it COULD be that |W+|^2 = 1/24, i.e., w = ±1/(2√6).
# At that specific radius, the conformal factor would be 1 and the metric
# would be locally Kähler AT THAT POINT. But Kähler-Einstein with Ric=-g
# requires |W+|^2 = 2/3, contradicting 1/24.

# So: the calibrated spectrum (1/12, 1/12, -1/6) can be achieved at most
# at ISOLATED RADII on Taub-NUT-AdS, not on an open set.
# On an open set, the metric is conformally Kähler with varying conformal factor,
# and the W+ spectrum doesn't match the calibrated one.

print("\n--- 4. W+ spectrum of Taub-NUT-AdS (self-dual orientation) ---")
print("Since Taub-NUT-AdS is self-dual (W- = 0), W+ has eigenvalues")
print("of the form (w(r), w(r), -2w(r)) by SU(2) symmetry.")
print()
print("From R_{0101} = (1/2)(lambda_1 - 2/3) = (1/2)(w(r) - 2/3):")
wp_eigenvalue = 2*R0101 + Rational(2,3) if isinstance(R0101, sp.Basic) else 2*R0101 + 2/3
print(f"w(r) = 2*R0101 + 2/3 = {2*R0101 + 2/3:.6f}")
w_val = 2*R0101 + 2/3
w2_val = -2*w_val
print(f"W+ eigenvalues: ({w_val:.6f}, {w_val:.6f}, {w2_val:.6f})")
print(f"|W+|^2 = 6*w^2 = {6*w_val**2:.6f}")
print(f"Calibrated |W+|^2 = 1/24 = {1/24:.6f}")
print()

# Calibrated defect F
s_num = -4.0  # exact for Ric = -g
Wp_norm = np.sqrt(6*w_val**2)
F_cs = (s_num + 8*np.sqrt(6)*Wp_norm)**2  # Cauchy-Schwarz term
f_term = (2/3)*s_num - 2*np.sqrt(2/3)*Wp_norm
a_term = (2/3)*s_num + 2*w2_val  # lowest eigenvalue is -2w
a_minus = min(a_term, 0)
G_term = f_term**2 - a_minus**2
F_total = 0 + F_cs + max(G_term, 0)  # |E|^2 = 0

print(f"|W+| = {Wp_norm:.6f}")
print(f"s + 8*sqrt(6)*|W+| = {s_num + 8*np.sqrt(6)*Wp_norm:.6f}")
print(f"F_CS = (s+8sqrt(6)|W+|)^2 = {F_cs:.6f}")
print(f"f = (2/3)s - 2*sqrt(2/3)*|W+| = {f_term:.6f}")
print(f"a = (2/3)s + 2*w_min = {a_term:.6f} (w_min = {w2_val:.6f})")
print(f"G = f^2 - (a-)^2 = {f_term**2:.6f} - {a_minus**2:.6f} = {G_term:.6f}")
print(f"F_total = {F_total:.6f}")
print()

if abs(F_total) < 0.01:
    print("F ≈ 0: Taub-NUT-AdS is COMPATIBLE with calibrated spectrum!")
    print("This would mean NUT regions have vanishing defect cost!")
else:
    print(f"F = {F_total:.6f} > 0: Taub-NUT-AdS is NOT calibrated!")
    print(f"Each NUT annular region carries positive F-cost density.")

print("\n" + "="*70)
print("COMPUTATION COMPLETE")
print("="*70)
