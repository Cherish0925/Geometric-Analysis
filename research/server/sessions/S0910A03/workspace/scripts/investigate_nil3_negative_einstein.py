#!/usr/bin/env python3
"""
Investigate the nil³ (Heisenberg) fiber case for negative Einstein 
collapse over a 1D base.

For a 4-manifold with nil³ local symmetry over a 1D base:
- Fiber = Heisenberg nilmanifold with left-invariant metric
- Base = circle or interval with coordinate s
- Structure: [e1, e2] = e3

The total metric in adapted frame is:
  g = ds^2 + a1(s)^2 (theta1)^2 + a2(s)^2 (theta2)^2 + a3(s)^2 (theta3)^2

where theta1 = dx, theta2 = dy, theta3 = dz + x dy are left-invariant forms.

The Ricci curvature includes both the s-derivatives and the structure constant 
contributions. We compute whether Ric = -g is possible on a circle.
"""

import sympy as sp
from sympy import symbols, Function, diff, simplify, solve, sqrt, pi, cos, sin, exp, S

s = symbols('s')
a1 = Function('a1')(s)
a2 = Function('a2')(s)
a3 = Function('a3')(s)

print("="*70)
print("NIL³ EINSTEIN EQUATIONS OVER 1D BASE")
print("="*70)

# For a product metric g = ds^2 + h(s) on a 1D base with
# left-invariant nilmanifold fiber, the Ricci curvature formulas are:
#
# Using Milnor's conventions for 3D Lie groups with frame {e_1, e_2, e_3}
# and structure constants c^3_{12} = 1 (Heisenberg):
#
# The fiber metric is diag(a1^2, a2^2, a3^2) in the left-invariant frame.
# The full 4D metric is g = ds^2 + a1^2 theta1^2 + a2^2 theta2^2 + a3^2 theta3^2
#
# Ricci components (standard computation, see e.g., Dunajski-Tod 2017):

# Define shorthand
a1p = diff(a1, s)
a2p = diff(a2, s)
a3p = diff(a3, s)
a1pp = diff(a1, s, 2)
a2pp = diff(a2, s, 2)
a3pp = diff(a3, s, 2)

# Volume function
v = a1 * a2 * a3

# The Ricci tensor of the total space (from O'Neill/warped product + structure constants):
# For nil^3 with [e1,e2] = e3, structure constant mu_3 = a3/(2*a1*a2)
mu3 = a3 / (2 * a1 * a2)

# Ric(ds, ds) = -(a1''/a1 + a2''/a2 + a3''/a3)
Ric_ss = -(a1pp/a1 + a2pp/a2 + a3pp/a3)

# Ric(e1, e1) = -a1''/a1 - a1'*(a2'/a2 + a3'/a3) - mu3^2
# Actually, the full formula for nil^3 fiber over 1D base:
# Ric(e_i, e_i) = -(a_i'' a_i + a_i' * (v'/v - a_i'/a_i)) / a_i^2 + (fiber Ricci)_ii
# 
# For the Heisenberg group with diagonal metric (a1, a2, a3):
# (fiber Ricci)_11 = -a3^4/(2*a1^2*a2^2) * (1/a1^2)
# Wait, let me use the standard Milnor formula.
#
# For a unimodular 3D Lie group with structure constants:
# [e1,e2] = lambda3 e3, [e2,e3] = lambda1 e1, [e3,e1] = lambda2 e2
# Heisenberg: lambda1 = 0, lambda2 = 0, lambda3 = 1
# With metric diag(a1^2, a2^2, a3^2):
# mu_i = lambda_i * a_i / (2 * a_j * a_k) (cyclic)
# Milnor Ricci: r_i = 2*mu_i^2 - 2*mu_j*mu_k (summation convention adjusted)
# Actually the standard formula is:
# r_1 = 2 mu_1 (mu_1 - mu_2 - mu_3) where indices are cyclic
# For Heisenberg: mu_1 = 0, mu_2 = 0, mu_3 = a3/(2*a1*a2)
# r_1 = 0  -- no, that's not right either.

# Let me use the standard result for nilmanifold fiber Ricci:
# For Heisenberg with [e1,e2]=e3:
# Static fiber Ricci eigenvalues:
# Ric_fiber(e1,e1) = -(1/2)(a3/(a1*a2))^2 = -a3^2/(2*a1^2*a2^2) * a1^2 
# Wait, I need to be more careful. Let me use definite formulas.

# For the 3D Heisenberg group with left-invariant frame {f1,f2,f3}
# where [f1,f2] = f3 and metric g_3 = sum a_i^2 (theta^i)^2,
# the Ricci curvature is (from direct computation or Milnor's paper):
#
# Ric(f1,f1) = -a3^4/(2 a1^2 a2^4)    # = -1/(2) * (a3/a2)^2 * (a3/a1a2)^2 / (a3/a2)^2 
# 
# Actually, let me just compute this properly using the structure equations.

# For the Heisenberg group: theta1 = dx, theta2 = dy, theta3 = dz + x dy
# d(theta1) = 0, d(theta2) = 0, d(theta3) = dx ∧ dy = theta1 ∧ theta2
#
# Orthonormal frame: e_i = (1/a_i) partial_i (where partial_i dual to theta_i)
# Connection 1-forms omega^i_j from structure equations:
# d(theta_i) = -omega^i_j ∧ theta_j + T^i
# For left-invariant forms, torsion-free connection:
#
# This is getting complex. Let me use a known result directly.

# From Isenberg-Jackson (1992) or standard references:
# For metric g = ds^2 + a1^2 dx^2 + a2^2 dy^2 + a3^2 (dz + x dy)^2
# on the Heisenberg nilmanifold bundle over R:
#
# Define alpha = a3^2 / (a1^2 * a2^2)  (the "twist" parameter)

alpha = a3**2 / (a1**2 * a2**2)

# The Ricci components are:
# Ric(ds,ds) = -(a1''/a1 + a2''/a2 + a3''/a3)
# Ric(e1,e1) = -a1*(a1'' + a1'*(a2'/a2 + a3'/a3)) / a1^2 - alpha/2
#            = -(a1''/a1 + a1'*a2'/(a1*a2) + a1'*a3'/(a1*a3)) - alpha/2

# Actually, using the standard warped product + nilmanifold formula:
# Ric(partial_s, partial_s) = -(a1''/a1 + a2''/a2 + a3''/a3)

# For the fiber directions, combining the warping contribution and the 
# intrinsic nilmanifold Ricci:

# Ric(e1,e1)/a1^2 = -a1''/a1 - a1'*(v'/(a1*v) - a1'/a1^2) - alpha/2
# Let me just use a clean formulation.

# Following Lott's adapted metric formulation for nil^3:
# With G = diag(a1^2, a2^2, a3^2) and the Heisenberg structure,
# the connection A has components determined by the structure constants.
# The effective curvature F includes the structure constant contribution.

# For Heisenberg: the connection curvature effectively has
# |F_eff|^2 = a3^4 / (a1^2 * a2^2) = alpha * a3^2

# The orbit-volume equation for nil^3 would be modified:
# Delta v = (|F_eff|^2/4 - lambda*N + correction) * v

# But this requires careful derivation. Let me instead check the 
# Einstein equations directly for specific ansätze.

print("\nChecking if Ric = -g is possible on a nil³ bundle over S¹:")
print()

# Try a constant-coefficient ansatz: a_i = const
# Then all derivatives vanish, Ric(ds,ds) = 0, but we need Ric(ds,ds) = -1.
# So constant a_i doesn't work.

print("1. Constant fiber metric (a_i = const):")
print("   Ric(ds,ds) = 0, but need -1. IMPOSSIBLE.")

# Try exponential ansatz: a_i(s) = b_i * exp(p_i * s)
b1, b2, b3, p1, p2, p3 = symbols('b1 b2 b3 p1 p2 p3', real=True)

print("\n2. Exponential ansatz a_i = b_i exp(p_i s):")
print("   Ric(ds,ds) = -(p1² + p2² + p3²)")
print("   Need: -(p1² + p2² + p3²) = -1")
print("   So: p1² + p2² + p3² = 1")
print()
print("   But on a CIRCLE S¹ of length L, a_i(s+L) = a_i(s)")
print("   requires exp(p_i L) = 1, so p_i = 2πn_i/L for integer n_i.")
print("   Then p1² + p2² + p3² = (2π/L)²(n1² + n2² + n3²) = 1")
print("   requires L = 2π√(n1² + n2² + n3²).")
print("   If all n_i = 0: p_i = 0, Ric(ds,ds) = 0 ≠ -1. IMPOSSIBLE.")
print("   If any n_i ≠ 0: a_i is periodic but the fiber metric")
print("   changes around the circle. This gives a non-trivial monodromy.")
print("   The fiber Ricci components also need checking.")

# The key observation: on a compact base (circle), the integral
# of Ric(ds,ds) over the base must equal the integral of -1:
# integral_0^L Ric(ds,ds) ds = -L
# But Ric(ds,ds) = -(a1''/a1 + a2''/a2 + a3''/a3)
# and integral(a_i''/a_i) = integral d(a_i'/a_i) + integral (a_i'/a_i)^2
# = [a_i'/a_i]_0^L + integral (a_i'/a_i)^2
# = 0 + integral (a_i'/a_i)^2  (periodic)
# = integral (a_i'/a_i)^2 >= 0

print("\n3. INTEGRAL OBSTRUCTION on circle base (key argument):")
print("   On circle S¹ of length L:")
print("   ∫ Ric(∂s,∂s) ds = -∫(a1''/a1 + a2''/a2 + a3''/a3) ds")
print()
print("   For periodic a_i:")
print("   ∫ a_i''/a_i ds = ∫ d(a_i'/a_i) + ∫ (a_i'/a_i)² ds")
print("   = [a_i'/a_i]₀ᴸ + ∫ (a_i'/a_i)² ds")
print("   = 0 + ∫ (a_i'/a_i)² ds ≥ 0")
print()
print("   Therefore: ∫ Ric(∂s,∂s) ds ≤ 0")
print("   But need: ∫ Ric(∂s,∂s) ds = ∫(-1) ds = -L < 0")
print()
print("   So ∫(a_i'/a_i)² ds = L, which is compatible.")
print("   The Ric(∂s,∂s) condition alone does NOT exclude nil³ on a circle!")

# However, the fiber Ricci conditions add more constraints.
# For the full Einstein system Ric = -g:
# Ric(e_i, e_i) = -a_i^2 (in the frame, or -1 in orthonormal frame)
#
# The fiber Ricci includes the nilmanifold curvature term -alpha/2 in certain directions.
# The TRACE of all Ricci = -4 (scalar curvature s = -4*lambda = 4... wait, s = n*lambda = 4*(-1) = -4)
#
# Scalar curvature: s = -(a1''/a1 + a2''/a2 + a3''/a3) + ...
# For Ric = -g: s = 4*(-1) = -4.

print("\n4. ORBIT VOLUME on circle base:")
print("   v = a1*a2*a3. On a circle:")
print("   ∫ v'' ds = 0 (periodic)")
print()
print("   From Lott's generalized equation (if applicable to nil³):")
print("   v'' ≥ (|F_eff|²/4 + N)v for some effective F")
print("   Then ∫ v'' = 0 but ∫ (|F_eff|²/4 + N)v > 0. CONTRADICTION.")
print()
print("   The question is whether v'' ≥ cv holds for c > 0 in nil³ case.")

# Direct computation of v'' for nil³
# v = a1*a2*a3
# v' = a1'*a2*a3 + a1*a2'*a3 + a1*a2*a3'
# v'' = a1''*a2*a3 + a1*a2''*a3 + a1*a2*a3'' + 2*(a1'*a2'*a3 + a1'*a2*a3' + a1*a2'*a3')
# v''/v = (a1''/a1 + a2''/a2 + a3''/a3) + 2*(a1'/a1*a2'/a2 + a1'/a1*a3'/a3 + a2'/a2*a3'/a3)
# = tr(G^{-1}G'') + 2*sum_{i<j}(a_i'/a_i)(a_j'/a_j)
# Wait, that's tr(G^{-1}G'') = sum(a_i''/a_i + (a_i'/a_i)^2) for diagonal G?
# No: G = diag(a1^2, ...), G' = diag(2*a1*a1', ...), G^{-1}G' = diag(2*a1'/a1, ...)
# tr(G^{-1}G') = 2*(a1'/a1 + a2'/a2 + a3'/a3) = 2*v'/v
# tr(G^{-1}G'') = 2*(a1''/a1 + (a1'/a1)^2 + a2''/a2 + (a2'/a2)^2 + a3''/a3 + (a3'/a3)^2)

# Actually, let me just compute v''/v directly:
print("\n5. Direct computation of v''/v:")
x1 = sp.Symbol('x1')  # = a1'/a1
x2 = sp.Symbol('x2')  # = a2'/a2  
x3 = sp.Symbol('x3')  # = a3'/a3
y1 = sp.Symbol('y1')  # = a1''/a1
y2 = sp.Symbol('y2')  # = a2''/a2
y3 = sp.Symbol('y3')  # = a3''/a3

v_ratio = y1 + y2 + y3 + 2*(x1*x2 + x1*x3 + x2*x3)
print(f"   v''/v = Σ(a_i''/a_i) + 2*Σ_{{i<j}}(a_i'/a_i)(a_j'/a_j)")
print(f"         = (y1+y2+y3) + 2*(x1*x2 + x1*x3 + x2*x3)")

# From Ric(ds,ds) = -1:
# -(y1 + y2 + y3) = -1, so y1+y2+y3 = 1

print(f"\n   From Ric(∂s,∂s) = -1: y1 + y2 + y3 = 1")
print(f"   (This is the same for BOTH abelian and nil³!)")
print(f"   So: v''/v = 1 + 2*Σ_{{i<j}} x_i x_j")
print(f"        = 1 + (Σ x_i)² - Σ x_i²")
print(f"        = 1 + (v'/v)² - Σ(a_i'/a_i)²")

# The cross term can be negative. But on a circle:
# ∫ v''/v * v ds = ∫ v'' ds = 0
# ∫ [1 + (v'/v)² - Σ(a_i'/a_i)²] * v ds = 0
# ∫ v ds + ∫ (v')²/v ds = ∫ Σ(a_i'/a_i)² * v ds

print(f"\n6. CRUCIAL: Integrating v'' = [1 + (v'/v)² - Σ(a_i'/a_i)²]*v over circle:")
print(f"   ∫ v'' ds = 0 (periodic)")
print(f"   So: ∫ v ds + ∫ (v')²/v ds = ∫ v * Σ(a_i'/a_i)² ds")
print(f"")
print(f"   But v > 0 and (v')²/v ≥ 0, so:")
print(f"   ∫ v ds ≤ ∫ v * Σ(a_i'/a_i)² ds")
print(f"   i.e.: ∫ v * [Σ(a_i'/a_i)² - 1] ds ≥ 0")
print(f"")
print(f"   By Cauchy-Schwarz on (x1,x2,x3) with x1+x2+x3 = v'/v:")
print(f"   Σ x_i² ≥ (Σ x_i)²/3 = (v'/v)²/3")
print(f"   But this doesn't give Σ x_i² ≥ 1 in general.")

# Key insight: the Ric(ds,ds) = -1 gives y1+y2+y3 = 1, but the
# fiber Ricci conditions give additional constraints on the y_i.
# For the ABELIAN case: Lott's formula absorbs all terms into
# Delta v = (|F|^2/4 + 3)v, so v'' >= 3v > 0.
#
# For nil³: the structure constant contributes to the fiber Ricci.
# The full system of Einstein equations is needed.
#
# But here's the key: the Ric(ds,ds) = -1 constraint ALONE
# gives v''/v = 1 + cross_terms, which integrates to
# ∫v ds = ∫(Σx_i² - 1)v ds + ∫(v')²/v ds.
# This doesn't immediately give a contradiction.

print(f"\n7. For the ABELIAN case, Lott's equation gives v'' = 3v on circle:")
print(f"   ∫ v'' = 0 vs ∫ 3v > 0. Direct contradiction.")
print(f"")
print(f"   For nil³: the relationship between v'' and v involves the")
print(f"   nilmanifold structure constants. The effective coefficient")
print(f"   might be reduced from N=3 to something smaller.")
print(f"   Need the full Einstein system to determine this.")

# Let me check: for Lott's abelian equation on 1D base with N=3, F=0:
# v'' = 3v (from Delta v = (0/4 + 3)v = 3v)
# But v''/v = (y1+y2+y3) + 2*cross = 1 + 2*cross
# So 3 = 1 + 2*cross, meaning cross = 1.
# i.e., Σ_{i<j} x_i x_j = 1 for the abelian Einstein solution.

print(f"\n8. Consistency check for abelian case:")
print(f"   Lott gives v'' = 3v, so v''/v = 3.")
print(f"   Direct formula: v''/v = 1 + 2*Σ x_i x_j")
print(f"   So Σ_{{i<j}} x_i x_j = 1 for abelian Einstein.")
print(f"   This means (Σ x_i)² = Σ x_i² + 2 = (y1+y2+y3) + 2 = 3")
print(f"   Wait: ∫(a_i'/a_i)² = y_i + x_i²?  No: y_i = a_i''/a_i")
print(f"   and x_i² = (a_i'/a_i)², these are different.")
print(f"")
print(f"   The abelian coefficient 3 comes from Lott's full equation")
print(f"   which includes the Einstein trace properly.")

print(f"\n9. CONCLUSION:")
print(f"   - Abelian collapse on circle base: EXCLUDED by ∫v''=0 vs ∫3v>0")
print(f"   - Nil³ collapse on circle base: requires full Einstein ODE system")
print(f"   - The Ric(∂s,∂s) = -1 condition alone gives v''/v = 1 + 2*cross")
print(f"     where cross = Σ_{{i<j}}(a_i'/a_i)(a_j'/a_j) can be negative")
print(f"   - The REMAINING fiber Einstein equations constrain cross further")
print(f"   - A complete nil³ exclusion needs all 4 Einstein equations simultaneously")

print("\n" + "="*70)
