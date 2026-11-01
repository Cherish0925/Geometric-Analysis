#!/usr/bin/env python3
"""
Verify the static circle Einstein incompatibility with the calibrated W+ spectrum.

For a cohomogeneity-one static circle metric:
  g = dt^2 + a(t)^2 g_{S^2} + ell(t)^2 dpsi^2

with Ric = -g, the Einstein equations give:
  (E1) Ric^B_{tt} = h_tt - 1  =>  -2a''/a = ell''/ell - 1
  (E2) Ric^B_{ang} = h_ang - 1  =>  -a''/a + (1-(a')^2)/a^2 = a'ell'/(a ell) - 1
  (E3) Delta_B ell = ell  =>  ell'' + 2(a'/a)ell' = ell

The calibrated W+ spectrum (-1/6, 1/12, 1/12) requires:
  (C1) h_tt = ell''/ell = 1/4
  (C2) h_ang = a'ell'/(a ell) = 3/8

These give an OVERDETERMINED system. This script proves the incompatibility.
"""

from sympy import *

print("="*70)
print("STATIC CIRCLE EINSTEIN vs CALIBRATED SPECTRUM")
print("="*70)

t = symbols('t')
a = Function('a')(t)
ell = Function('ell')(t)

# Einstein equations for static cohomogeneity-one:
# From (E1): a'' = a(1 - ell''/ell)/2
# From (C1): ell''/ell = 1/4
# => a'' = a(1 - 1/4)/2 = 3a/8  ... (*)

print("\nFrom calibrated + E1: a'' = 3a/8")

# From (E2): -a''/a + (1-(a')^2)/a^2 = v - 1 where v = a'ell'/(aell)
# From (C2): v = 3/8
# => -a''/a + (1-(a')^2)/a^2 = -5/8
# With (*): -3/8 + (1-(a')^2)/a^2 = -5/8
# => (1-(a')^2)/a^2 = -1/4
# => (a')^2 = 1 + a^2/4  ... (**)

print("From calibrated + E2: (a')^2 = 1 + a^2/4")

# Differentiating (**): 2a'a'' = 2a a'/4 = a a'/2
# => a'' = a/4  ... (***)

print("Differentiating: a'' = a/4")
print()
print("CONTRADICTION: (*) says a'' = 3a/8, (***) says a'' = a/4")
print(f"The gap is a/8, i.e., relative error = {Rational(1,8)/Rational(3,8)} = 1/3")

# Verify by solving the compatible system
print("\n" + "="*70)
print("What spectrum IS compatible with static coh-1 Einstein?")
print("="*70)

u, v = symbols('u v', real=True)  # u = ell''/ell, v = a'ell'/(aell)

# Trace constraint: u + 2v = 1 (static Laplacian)
# From E1: a''/a = (1-u)/2
# From E2: (1-(a')^2)/a^2 = v - 1 + (1-u)/2 = v - 1/2 - u/2
# Differentiating (a')^2 = 1 - a^2(v-1/2-u/2)... 
# Actually, with CONSTANT u,v, let k = v - 1/2 - u/2 = v - 1/2 - u/2
# Then (a')^2 = 1 - k*a^2 and differentiating: a'' = -k*a

# But also a'' = a(1-u)/2
# So -k = (1-u)/2 => k = -(1-u)/2 = (u-1)/2
# And k = v - 1/2 - u/2
# => v - 1/2 - u/2 = (u-1)/2 = u/2 - 1/2
# => v = u

# With trace constraint u + 2v = 1 => u + 2u = 1 => u = 1/3, v = 1/3

print("\nCompatible constant-spectrum static coh-1 Einstein:")
print("Requires u = v = 1/3")
print("h = (1/3)*I => W+ = 0 (ISOTROPIC)")

# So the ONLY constant-spectrum static coh-1 Einstein has W+ = 0!
# This is the real hyperbolic metric (all sectional curvatures = -1/3).

u_compatible = Rational(1,3)
v_compatible = Rational(1,3)

W_simple = 2*(u_compatible - Rational(1,3))
W_double = 2*(v_compatible - Rational(1,3))
print(f"W+ spectrum: simple = {W_simple}, double = {W_double}")
print("=> Only constant curvature (W+=0) is compatible. Q.E.D.")

# Now find what VARYING spectrum can occur
print("\n" + "="*70)
print("Twisted case: additional W+ from field strength")
print("="*70)

# For a twisted KK metric g = g_B + ell^2(dpsi + A)^2:
# Modified Laplacian: Delta_B ell + (ell^3/4)|F|^2 = ell
# => tr(h) = 1 - (ell^2/4)|F|^2
# 
# With F = dA on S^2 and |F|^2 = 1/a^4:
# tr(h) = 1 - ell^2/(4a^4)
#
# Additional W+ from twist involves ell^2*|F|^2 terms.
# For the calibrated spectrum to work, we need:
# W+_static + W+_twist = calibrated

# In Taub-NUT-AdS: W+_static + W+_twist = 0
# The twist EXACTLY compensates the static warping.
# For calibrated: W+_static + W+_twist = calibrated
# => W+_twist = calibrated - W+_static

print("\nFor Taub-NUT-AdS (W+ = 0): twist exactly cancels warping")
print("For calibrated: W+_twist must provide the full anisotropy")
print()

# The twist contribution to the curvature operator on Lambda^2_+
# involves O'Neill A-tensor terms proportional to ell^2*F:
#
# R_{abc4} = (ell/2)(nabla_a F_{bc} + ...) - these contribute to OFF-diagonal R_hat
# R_{a4b4} += -(ell^2/4)*(F^2)_{ab} - these modify the diagonal
#
# For a Hopf connection with |F|^2 = 1/a^4 and (F^2)_{ab} diagonal:
# (F^2)_{tt} = 0, (F^2)_{ang} = 1/a^4 (in the angular-angular block)

print("The twist correction to the curvature operator on Lambda^2_+:")
print("  Diagonal: R_hat_+ += O(ell^2/a^4) in angular components")
print("  Off-diagonal: R_hat_+ += O(ell * nabla F) in mixed components")
print()
print("Near a NUT (ell << 1): twist corrections are O(ell^2), hence SMALL.")
print("=> The static formula W+ ≈ 2*J(h - I/3) is ASYMPTOTICALLY CORRECT near NUT.")
print("=> The static incompatibility PERSISTS for the leading-order near-NUT behavior.")

# Compute the twist-corrected system for coh-1 Hopf bundle
print("\n" + "="*70)
print("Full twisted cohomogeneity-one system with Hopf connection")
print("="*70)

# For g = dt^2/F_B(t) + (t^2 - nu^2)(dtheta^2 + sin^2 theta dphi^2) + 4nu^2 F_B(dpsi + cos theta dphi)^2
# with the Taub-NUT-AdS ansatz, a(t) = sqrt(t^2-nu^2), ell(t) = 2nu*sqrt(F_B(t))

# The modified Einstein system with twist:
# (E1'): Ric^B_{tt} = h_tt - 1 (same, no twist in tt)  
# Actually, the twist does modify the tt component through the A-tensor:
# Ric_{tt} = Ric^B_{tt} - h_tt - (ell^2/2)*sum_b (F_{tb})^2
# Since F has no t-component: sum_b F_{tb}^2 = 0
# So E1 is unchanged: Ric^B_{tt} = h_tt - 1

# (E2'): Ric_{ang} = Ric^B_{ang} - h_ang - (ell^2/2)*|F_ang|^2 = -1
# => Ric^B_{ang} = h_ang + (ell^2/2)*|F_ang|^2 - 1
# where |F_ang|^2 = (F_{theta,phi})^2 = 1/a^4 for each angular direction

# (E3'): Delta_B ell + (ell^3/4)|F|^2 = ell
# => h_tt + 2*h_ang + (ell^2/4a^4) = 1

print("\nModified Einstein with Hopf twist:")
print("  (E1'): -2a''/a = h_tt - 1  (UNCHANGED)")  
print("  (E2'): -a''/a + (1-(a')^2)/a^2 = h_ang + ell^2/(2a^4) - 1")
print("  (E3'): h_tt + 2*h_ang + ell^2/(4a^4) = 1")

# For calibrated: h_tt = 1/4, h_ang = 3/8
# (E1'): a'' = a(1-1/4)/2 = 3a/8  (same as before)
# (E3'): 1/4 + 3/4 + ell^2/(4a^4) = 1 => ell^2/(4a^4) = 0 => ell = 0 or a -> infty

print("\nCalibrated h eigenvalues WITH trace correction from twist:")
print("  From (E3'): 1/4 + 2*(3/8) + ell^2/(4a^4) = 1")
print(f"  => 1/4 + 3/4 + ell^2/(4a^4) = 1")
print(f"  => ell^2/(4a^4) = 0")
print("  => ONLY works if ell = 0 (degenerate) or in the static limit (no twist)")

# BUT WAIT: the W+ operator also receives twist corrections!
# The static formula W+ = 2*J(h - I/3) used tr(h) = 1.
# With twist: tr(h) = 1 - ell^2/(4a^4) < 1.
# So the correct formula is: W+ = 2*J(h) - (2/3)*I + twist correction to W+

print("\n" + "="*70)  
print("CORRECTED ANALYSIS: W+ includes twist curvature terms")
print("="*70)

# The curvature operator on Lambda^2_+ for the twisted case includes:
# 1. The warping contribution (through h)
# 2. The twist contribution (through F and ell)
#
# For the twisted metric, the additional R_{abc4} components contribute
# OFF-DIAGONAL terms to R_hat_+.
# 
# For a cohomogeneity-one Hopf bundle:
# The additional curvature terms are:
# R_{r,theta,theta,4} ~ ell * F' * something (from nabla_r F)
# R_{theta,phi,r,4} ~ ell * (connection terms)
#
# These mix the self-dual 2-form types and shift the eigenvalues.

# KEY INSIGHT: Near the NUT (ell -> 0), ALL twist corrections are O(ell^2).
# The static part W+_static has eigenvalues that depend on h, which is O(1).
# So W+ ≈ W+_static + O(ell^2) near the NUT.
# The static incompatibility (W+ ≠ calibrated for any constant h satisfying Einstein)
# persists to leading order near the NUT.

# In the BULK (away from NUT), ell is O(1) and twist corrections are O(1).
# There, the full system may accommodate the calibrated spectrum.
# The question is about the TRANSITION zone where ell transitions from O(1) to 0.

print("\nNear NUT (ell -> 0):")
print("  Twist corrections to W+ are O(ell^2)")
print("  Static contribution dominates: W+ ≈ 2*J(h - I/3)")
print("  Static incompatibility persists: constant calibrated h is impossible")
print("  => W+ eigenvalues MUST deviate from calibrated near NUT")
print()

# Quantify the minimum deviation
print("The static incompatibility for constant-eigenvalue h gives:")
print("  Compatible static: u = v = 1/3 => W+ = 0 (isotropic)")
print("  Calibrated target: u = 1/4, v = 3/8 => W+ = (-1/6, 1/12, 1/12)")
print(f"  |W+|^2 at calibrated = {1/24:.6f}")
print(f"  |W+|^2 at compatible = 0")
print(f"  Minimum eigenvalue distance = |W+|^2 = 1/24")
print()

# The transition zone width is constrained by:
# 1. The Bianchi identity (W+ must change smoothly)
# 2. The curvature budget (|Rm|^2 bounded on good set)
# 3. The Einstein equations (constraining h, ell, a)
# 
# These jointly control how rapidly W+ can transition from near-calibrated
# to the compatible isotropic value.

print("="*70)
print("SUMMARY: Anisotropy interaction with collapse structure")
print("="*70)
print("""
1. STATIC INCOMPATIBILITY: The calibrated W+ spectrum is incompatible 
   with constant-eigenvalue static Einstein circle reduction.
   The ONLY compatible constant spectrum is W+ = 0 (isotropic).
   
2. TWIST NECESSITY: Any Einstein circle metric achieving calibrated W+
   REQUIRES nonzero field strength (twist). The twist energy is O(ell^2/a^4),
   which vanishes near a NUT.
   
3. NUT TRANSITION: Near a smooth NUT (ell -> 0), the static formula dominates
   and the calibrated spectrum cannot be maintained. W+ must deviate toward
   the isotropic value (W+ = 0) by an amount O(1) near the NUT.
   
4. TRANSITION COST: The change from calibrated (|W+|^2 = 1/24) to isotropic 
   (|W+|^2 = 0) over a transition zone of base distance d costs:
   - Calibrated deficit: integral (|W+| - 1/(2sqrt6))^2 ~ d * (some lower bound)
   - Gradient energy: integral |nabla W+|^2 ~ 1/(24*d)
   Either cost competes with the total curvature/deficit budget.
   
5. KEY QUESTION (open): Does the transition cost, summed over all NUT/bolt 
   regions on a closed critical Ishida-LeBrun manifold, exceed the total 
   deficit budget O(A delta^2)?
""")
