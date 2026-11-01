#!/usr/bin/env python3
"""
CRITICAL SIGN CHECK: nil³ orbit-volume equation for Ric = -g.

Two competing claims:
  TTCS: v'' = (3 - mu)v  where mu = a3^2/(2*a1^2*a2^2)
  A01:  v'' = (3 + mu)v  

The difference is the sign of the Heisenberg fiber Ricci contribution.
We verify using the known complex hyperbolic cusp model (CH²).
"""
import sympy as sp
from sympy import symbols, sqrt, diff, simplify, Rational, exp

s = sp.Symbol('s')

print("="*70)
print("NIL³ ORBIT-VOLUME SIGN CHECK")
print("="*70)

# Complex hyperbolic cusp model (TTCS Section 6)
# g = ds² + e^{2αs}(θ¹² + θ²²) + (2/3)e^{4αs}(θ³²)
# where α = 1/√6 and [θ¹,θ²] = θ³
alpha = 1/sqrt(sp.Integer(6))

a1 = exp(alpha * s)
a2 = exp(alpha * s)
a3 = sqrt(Rational(2,3)) * exp(2*alpha * s)

print("\n1. COMPLEX HYPERBOLIC CUSP MODEL:")
print(f"   a1 = a2 = exp(s/√6)")
print(f"   a3 = √(2/3) exp(2s/√6)")

# Compute mu = a3²/(2*a1²*a2²)
mu = simplify(a3**2 / (2*a1**2 * a2**2))
print(f"\n   mu = a3²/(2*a1²*a2²) = {mu}")

# Compute orbit volume
v = simplify(a1 * a2 * a3)
print(f"   v = a1*a2*a3 = {v}")

# Compute v''/v
v_prime = simplify(diff(v, s))
v_double_prime = simplify(diff(v, s, 2))
ratio = simplify(v_double_prime / v)
print(f"   v'' / v = {ratio}")

# Check against both formulas
check_ttcs = simplify(3 - mu)
check_a01 = simplify(3 + mu)
print(f"\n   TTCS formula: 3 - mu = {check_ttcs}")
print(f"   A01 formula:  3 + mu = {check_a01}")
print(f"   Actual v''/v = {ratio}")

if simplify(ratio - check_ttcs) == 0:
    print(f"\n   *** TTCS FORMULA IS CORRECT: v'' = (3 - mu)v ***")
elif simplify(ratio - check_a01) == 0:
    print(f"\n   *** A01 FORMULA IS CORRECT: v'' = (3 + mu)v ***")
else:
    print(f"\n   *** NEITHER MATCHES - need investigation ***")

# Now verify the Ricci tensor directly
print("\n" + "="*70)
print("2. DIRECT RICCI VERIFICATION OF CH² MODEL")
print("="*70)

f1 = simplify(diff(a1,s)/a1)  # = alpha
f2 = simplify(diff(a2,s)/a2)  # = alpha
f3 = simplify(diff(a3,s)/a3)  # = 2*alpha

print(f"\n   f1 = a1'/a1 = {f1}")
print(f"   f2 = a2'/a2 = {f2}")
print(f"   f3 = a3'/a3 = {f3}")

# Heisenberg fiber Ricci eigenvalues (Milnor):
# r1 = r2 = -mu, r3 = +mu
r1 = -mu
r2 = -mu
r3 = mu
print(f"\n   Fiber Ricci: r1 = r2 = {r1}, r3 = {r3}")
print(f"   Fiber scalar = {simplify(r1+r2+r3)} = -mu ✓")

# Full Ricci of warped product g = ds² + Σ ai²(θi)²:
# Ric(ds,ds) = -Σ(ai''/ai)
# Ric(ei,ei) = -(ai''/ai) - (ai'/ai)*Σ_{j≠i}(aj'/aj) + ri
#            (in orthonormal frame, should equal -1)

# E0: Ric(ds,ds) = -1
E0_lhs = simplify(-(diff(a1,s,2)/a1 + diff(a2,s,2)/a2 + diff(a3,s,2)/a3))
print(f"\n   Ric(ds,ds) = {E0_lhs}")
print(f"   Should be -1: {'✓' if simplify(E0_lhs + 1) == 0 else '✗ ERROR'}")

# E1: Ric(e1,e1) = -1
E1_warping = simplify(diff(a1,s,2)/a1 + f1*(f2+f3))
E1_lhs = simplify(-E1_warping + r1)
print(f"\n   Ric(e1,e1) = -(warping) + r1 = {E1_lhs}")
print(f"   Should be -1: {'✓' if simplify(E1_lhs + 1) == 0 else '✗ ERROR'}")

# E3: Ric(e3,e3) = -1
E3_warping = simplify(diff(a3,s,2)/a3 + f3*(f1+f2))
E3_lhs = simplify(-E3_warping + r3)
print(f"\n   Ric(e3,e3) = -(warping) + r3 = {E3_lhs}")
print(f"   Should be -1: {'✓' if simplify(E3_lhs + 1) == 0 else '✗ ERROR'}")

# Now check the Einstein equations as written by A01 vs correct version
print("\n" + "="*70)
print("3. SIGN COMPARISON IN EINSTEIN EQUATIONS")
print("="*70)

# Correct form: Ric(ei,ei) = -1 means
# -(ai''/ai) - fi*Σ_{j≠i}fj + ri = -1
# (ai''/ai) + fi*Σ_{j≠i}fj - ri = 1
# Since -ri = +mu for i=1,2 and -ri = -mu for i=3:

print("\n   CORRECT Einstein equations (from Ric(ei,ei) = -1):")
print(f"   E1: (f1'+f1²) + f1*f2 + f1*f3 + mu = 1  (since -r1 = +mu)")
print(f"   E2: (f2'+f2²) + f1*f2 + f2*f3 + mu = 1  (since -r2 = +mu)")
print(f"   E3: (f3'+f3²) + f1*f3 + f2*f3 - mu = 1  (since -r3 = -mu)")
print()
print(f"   A01's WRONG equations (signs swapped):")
print(f"   E1: (f1'+f1²) + f1*f2 + f1*f3 - mu = 1  ← WRONG")
print(f"   E3: (f3'+f3²) + f1*f3 + f2*f3 + mu = 1  ← WRONG")

# Verify with actual numbers
f1_val = alpha
f2_val = alpha
f3_val = 2*alpha

# Correct E1: (f1'+f1²) + f1*f2 + f1*f3 + mu = 1
E1_correct = simplify(f1_val**2 + f1_val*f2_val + f1_val*f3_val + mu)
print(f"\n   Verify correct E1: {E1_correct} = {simplify(E1_correct)}")
print(f"   Should be 1: {'✓' if simplify(E1_correct - 1) == 0 else '✗'}")

# Wrong E1: (f1'+f1²) + f1*f2 + f1*f3 - mu = 1
E1_wrong = simplify(f1_val**2 + f1_val*f2_val + f1_val*f3_val - mu)
print(f"\n   A01's wrong E1: {E1_wrong} = {simplify(E1_wrong)}")
print(f"   Should be 1: {'✓' if simplify(E1_wrong - 1) == 0 else '✗ FAILS'}")

# Now check the orbit-volume sum
print("\n" + "="*70)
print("4. ORBIT-VOLUME FROM CORRECT EQUATIONS")
print("="*70)

print(f"\n   Correct sum E1+E2+E3:")
print(f"   [(f1'+f1²)+(f2'+f2²)+(f3'+f3²)]")
print(f"   + 2(f1*f2+f1*f3+f2*f3) + mu + mu - mu = 3")
print(f"   Using E0: Σ(fi'+fi²) = 1")
print(f"   1 + 2*Σfifj + mu = 3")
print(f"   2*Σfifj = 2 - mu")
print(f"   v''/v = 1 + 2*Σfifj = 3 - mu")
print(f"\n   *** CORRECT: v'' = (3 - mu)v ***")

# Verify numerically
cross = simplify(f1_val*f2_val + f1_val*f3_val + f2_val*f3_val)
print(f"\n   Numerical check: 2*Σfifj = {simplify(2*cross)}")
print(f"   2 - mu = {simplify(2 - mu)}")
print(f"   Match: {'✓' if simplify(2*cross - (2 - mu)) == 0 else '✗'}")

vv_ratio = simplify(1 + 2*cross)
print(f"   v''/v = 1 + 2*Σfifj = {vv_ratio}")
print(f"   3 - mu = {simplify(3 - mu)}")
print(f"   Match: {'✓' if simplify(vv_ratio - (3 - mu)) == 0 else '✗'}")

print("\n" + "="*70)
print("5. CONSEQUENCES")
print("="*70)
print(f"\n   A01 msg #238 claims v'' = (3+mu)v. THIS IS WRONG.")
print(f"   TTCS generator correctly found v'' = (3 - mu)v = (3 - rho/2)v.")
print(f"   The Heisenberg structure REDUCES the coefficient from 3 to 3-mu.")
print()
print(f"   HOWEVER: TTCS also proved mu <= 2/3 on circle base")
print(f"   (by maximum principle: at max of rho, rho'' = rho(3*rho-2);")
print(f"   rho'' <= 0 at max requires rho <= 2/3)")
print(f"   So on circle: v'' >= (3 - 1/3)v = (8/3)v > 0.")
print(f"   CIRCLE EXCLUSION STILL HOLDS even with correct sign.")
print()
print(f"   On interval/ray: CH² cusp with mu=1/3 is genuine solution.")
print(f"   Universal inequality v'' >= cv > 0 is FALSE for arbitrary intervals.")

print("\n" + "="*70)
print("SUMMARY: TTCS correct, A01 sign error confirmed, circle exclusion stands")
print("="*70)
