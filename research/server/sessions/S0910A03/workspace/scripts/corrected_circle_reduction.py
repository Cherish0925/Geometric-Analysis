#!/usr/bin/env python3
"""
CORRECTED circle reduction of W+ for Einstein 4-manifolds.

Corrections from TTCS verification:
1. R_hat_+ = -J(h), NOT 2J(h) - I  
2. Spec(W+) = {1/3 - eta_i} where eta_i = eigenvalues of h
3. Calibrated h = (1/2, 1/4, 1/4), NOT (3/8, 3/8, 1/4)
4. Twist makes tr(h) > 1 (not < 1)
5. Near NUT, twist corrections are NOT O(ell^2); both h and twist diverge

The verified formula: for static g = g_B + ell^2 dpsi^2 with Ric = -g,
  h = Hess(ell)/ell, tr(h) = 1
  R_hat_+(omega_a, omega_b) = curvature operator on Lambda^2_+
  
  In adapted SD basis:
    R_hat_+ = [[-h33, h23, -h13],
               [h23, -h22, h12],
               [-h13, h12, -h11]]
  
  Equivalently: Spec(R_hat_+) = -Spec(h) = {-eta_1, -eta_2, -eta_3}
  And: W+ = R_hat_+ + (1/3)I
  
  So: Spec(W+) = {1/3 - eta_1, 1/3 - eta_2, 1/3 - eta_3}
"""
from sympy import *

print("="*70)
print("CORRECTED STATIC CIRCLE REDUCTION")
print("="*70)

# Check 1: constant curvature h = I/3
h_iso = Rational(1,3) * eye(3)
Rhat = Matrix([[-h_iso[2,2], h_iso[1,2], -h_iso[0,2]],
               [h_iso[1,2], -h_iso[1,1], h_iso[0,1]],
               [-h_iso[0,2], h_iso[0,1], -h_iso[0,0]]])
print(f"h = I/3 => R_hat_+ = {Rhat}")
print(f"R_hat_+ eigenvalues: {Rhat.eigenvals()}")
Wplus = Rhat + Rational(1,3)*eye(3)
print(f"W+ = {Wplus}")
assert Wplus == zeros(3), "Should be zero for constant curvature!"
print("W+ = 0 for constant curvature. ✓\n")

# Check 2: calibrated spectrum requires h = (1/2, 1/4, 1/4)
print("Calibrated W+ = (-1/6, 1/12, 1/12):")
print("Requires 1/3 - eta = -1/6 => eta = 1/2")
print("         1/3 - eta = 1/12 => eta = 1/4")
print(f"So h eigenvalues = (1/2, 1/4, 1/4), sum = {Rational(1,2)+Rational(1,4)+Rational(1,4)}")

h_cal = diag(Rational(1,2), Rational(1,4), Rational(1,4))
Rhat_cal = Matrix([[-h_cal[2,2], 0, 0],
                   [0, -h_cal[1,1], 0],
                   [0, 0, -h_cal[0,0]]])
Wplus_cal = Rhat_cal + Rational(1,3)*eye(3)
print(f"W+ eigenvalues: {sorted(Wplus_cal.eigenvals().keys(), reverse=True)}")
print(f"= (1/12, 1/12, -1/6) ✓\n")

# Check 3: Cohomogeneity-one incompatibility
print("="*70)
print("CORRECTED COHOMOGENEITY-ONE ANALYSIS")
print("="*70)

print("""
For g = dt^2 + a(t)^2 g_{S^2} + ell(t)^2 dpsi^2 with Ric = -g:

h = diag(u, v, v) where u = ell''/ell, v = a'ell'/(a ell)

W+ spectrum = (1/3-v, 1/3-v, 1/3-u)

Calibrated: u = 1/2, v = 1/4

Einstein equations:
  (E1): -2a''/a = u - 1  =>  a'' = a(1-u)/2 = a(1-1/2)/2 = a/4
  (E2): -a''/a + (1-(a')^2)/a^2 = v - 1 = -3/4
  (E3): u + 2v = 1  (trace)

From E1: a'' = a/4
From E2: -1/4 + (1-(a')^2)/a^2 = -3/4  =>  (a')^2 = 1 + a^2/2

Differentiating: 2a'a'' = a a'  =>  a'' = a/2

CONTRADICTION: E1 gives a'' = a/4, differentiation gives a'' = a/2.
""")

# The gap
print(f"Gap: a/2 - a/4 = a/4")
print(f"Relative error: {Rational(1,4)/Rational(1,2)} = 1/2")

# Compatible constant spectrum
print(f"\nOnly compatible constant-eigenvalue static: u = v = 1/3 (W+ = 0)")
print(f"This is the unique solution: differentiating (a')^2 = 1 - k a^2")
print(f"gives a'' = -k a, and E1 gives a'' = (1-u)/2 a, so k = -(1-u)/2.")
print(f"Also k = v - 1/2 - u/2, equating: u = v, and trace: u + 2v = 1 => u = v = 1/3.\n")

# Check 4: Twist sign correction
print("="*70)
print("TWIST SIGN CORRECTION")
print("="*70)
print("""
For twisted g = g_B + ell^2(dpsi + A)^2:

Ric(e_4, e_4) = -(Delta_B ell)/ell + (ell^2/4)|F|^2_{raw}

where |F|^2_{raw} = F_{ab}F_{ab} (not the 2-form norm).

Setting Ric(e_4,e_4) = -1:
  tr(h) = Delta_B(ell)/ell = 1 + (ell^2/4)|F|^2_{raw}

So tr(h) > 1 under nonzero twist. (CORRECTED from earlier < 1.)

For Taub-NUT-AdS at nu=0.01, r=0.5:
  tr(h) ≈ 1.003 (consistent with > 1)
""")

# Check 5: Near-NUT behavior  
print("="*70)
print("NEAR-NUT BEHAVIOR (CORRECTED)")
print("="*70)
print("""
Near a smooth NUT (ell -> 0):
  - h = Hess(ell)/ell can DIVERGE (since ell -> 0)
  - Twist: ell^2 |F|^2 can also DIVERGE (F diverges in base-ONB)
  - They CANCEL in the total curvature (total space is smooth)
  
  For Taub-NUT-AdS at r = nu + x with x << nu:
    h_ang ~ 1/(8 nu x) -> infinity
    ell^2 F^2 ~ 1/(4x nu) -> infinity  
    But Ric = -g exactly (smooth total curvature)
    
  CONSEQUENCE: The static formula W+ ≈ (1/3)I - h does NOT dominate
  near the NUT. Both static and twist terms are large and cancel.
  The net W+ depends on the precise balance, not just on h.
  
  This invalidates the claim that "near a NUT, W+ must be isotropic."
  In principle, a NUT could have calibrated W+ if the cancellation
  produces the right eigenvalue structure.
""")

# Summary
print("="*70)  
print("CORRECTED SUMMARY")
print("="*70)
print("""
VERIFIED FORMULAS:
1. Static: Spec(W+) = {1/3 - eta_i}, eta_i = eigenvalues of h = Hess(ell)/ell
2. Calibrated requires h = (1/2, 1/4, 1/4)
3. Coh-1 contradiction: a'' = a/4 (E1) vs a'' = a/2 (E2+diff), gap = a/4
4. ONLY compatible constant static spectrum: u=v=1/3, W+=0 (isotropic)
5. Twist: tr(h) = 1 + ell^2|F|^2/4 > 1 (sign corrected)
6. Near NUT: both h and twist diverge; static formula does NOT dominate

VALID CONCLUSIONS (from TTCS generator):
- ell(p) can be arbitrarily small at a good point; curvature mean 
  controls h = Hess(ell)/ell, not ell itself
- Harnack: in a regular region with controlled base geometry and 
  bounded twist, positive ell stays positive (fiber survival)
- Static incompatibility: calibrated + low twist is incompatible 
  with Einstein on constant-eigenvalue circles
- High twist costs energy: ell^2|F|^2 >= c_Q > 0 is needed
  if the fiber dies at a fixed buffer scale
- The remaining possibility: diffuse high twist with ell^2|F|^2 ~ 1
  carrying the calibrated anisotropy through persistent scaled holonomy
""")
