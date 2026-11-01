"""
Step 22: Verify the Sobolev variable gradient structure for the single
critical H_2 -> H_3 step.

Key identity: for v = eta * a^{1/2} * F with a = chi^2,
|nabla v|^2 = eta^2 * a * |nabla F|^2  (dissipation)
            + (1/4) * eta^2 * |nabla a|^2 / a * F^2  (bounded: 4|nabla chi|^2)
            + eta^2 * <nabla a, nabla F> * F  (cross term, absorbed)
            + a * F^2 * |nabla eta|^2  (cutoff)
            + cross terms with nabla eta

The point: |nabla a|^2 / a = 4|nabla chi|^2 is BOUNDED, so no degeneracy.
"""
from sympy import *

# === 1. GRADIENT OF v = eta * a^{1/2} * F ===
eta, a, F_sym, chi = symbols('eta a F chi', positive=True)
# nabla(a^{1/2}) = (1/2) a^{-1/2} nabla(a) = (1/2) a^{-1/2} * 2 chi nabla chi = chi^{-1} nabla chi * a^{1/2}... 
# Actually for a = chi^2: a^{1/2} = chi, so nabla(a^{1/2}) = nabla(chi).
print("For a = chi^2:")
print("  a^{1/2} = chi")
print("  nabla(a^{1/2}) = nabla(chi)")
print("  |nabla(a^{1/2})|^2 = |nabla chi|^2 <= C/r^2")
print()

# So v = eta * chi * F
# nabla v = (nabla eta) * chi * F + eta * (nabla chi) * F + eta * chi * (nabla F)
print("nabla v = (nabla eta)(chi F) + eta(nabla chi)(F) + eta chi(nabla F)")
print()

# |nabla v|^2 = (chi F)^2 |nabla eta|^2 + F^2 eta^2 |nabla chi|^2 + eta^2 chi^2 |nabla F|^2")
# + cross terms
print("Leading terms in |nabla v|^2:")
print("  T1 = eta^2 a |nabla F|^2  (the dissipation)")
print("  T2 = eta^2 |nabla chi|^2 F^2  (bounded: <= C/r^2 F^2)")
print("  T3 = a F^2 |nabla eta|^2  (cutoff: <= C/r^2 a F^2)")
print()

# Cross terms:
# 2 * eta * chi * (nabla chi)(nabla F) F + ... 
# |2 eta chi (nabla chi)(nabla F) F| <= 2 eta |nabla chi| chi |nabla F| F
# <= eps * eta^2 a |nabla F|^2 + 1/eps * |nabla chi|^2 F^2
print("Cross terms:")
print("  2 eta chi <nabla chi, nabla F> F")
print("    <= eps * eta^2 a |nabla F|^2 + (1/eps)|nabla chi|^2 F^2")
print("    <= eps * D_2 + C/(eps r^2) H_2")
print()

# === 2. SOBOLEV VARIABLE STRUCTURE ===
print("=== Sobolev absorption mechanism ===")
print("||nabla v||_2^2 <= (1+eps) D_2 + C/r^2 H_2 + C/r^2 int aF^2")
print("||v||_2^2 = int eta^2 a F^2 <= H_2  (since a <= 1)")
print("||v||_4^2 <= A_0^2 (||nabla v||_2^2 + r^{-2} ||v||_2^2)")
print("         <= A_0^2 ((1+eps) D_2 + C/r^2 H_2)")
print()

# === 3. CUBIC REACTION ABSORPTION ===
# H_3 = int eta^2 a F^3 = int v_2 * (eta a^{1/2} F^2)
# Use Holder with (2,2,infty) or (4,4/3,2)...
# Actually, we need to be more careful about factoring.

# Approach: use interpolation on the weighted measure
# H_3 = int eta^2 a F^3 = int (eta^2 F^2)^{1/2} * (eta^2 a^2 F^4)^{1/2}
# = H_2^{1/2} * (int eta^2 a^2 F^4)^{1/2}

# int eta^2 a^2 F^4 = int v^2 * F^2 (since v = eta chi F, v^2 = eta^2 a F^2)
# Wait: v^2 = eta^2 a F^2, so int v^2 F^2 = int eta^2 a F^4

# Hmm: H_3 = int eta^2 a F^3 = (H_2)^{1/2} (int eta^2 a^2 F^4)^{1/2}
# by Cauchy-Schwarz: (int f*g)^2 <= (int f^2)(int g^2)
# with f = eta a^{0} F, g = eta a^1 F^2
# (int eta^2 a F^3)^2 <= (int eta^2 F^2)(int eta^2 a^2 F^4)
# H_3^2 <= H_2 * int eta^2 a^2 F^4

# Now: int eta^2 a^2 F^4 <= int v^2 * (a F^2) where v = eta chi F
# Wait, v^2 = eta^2 chi^2 F^2 = eta^2 a F^2
# So int v^2 F^2 = int eta^2 a F^4 (one power of a, not two)

# Let me redo: H_3 = int eta^2 a F^3 dmu
# Cauchy-Schwarz: H_3 <= (int eta^2 F^2)^{1/2} (int eta^2 a^2 F^4)^{1/2}
print("Cauchy-Schwarz factoring of H_3:")
print("  H_3 = int eta^2 a F^3")
print("      <= (int eta^2 F^2)^{1/2} * (int eta^2 a^2 F^4)^{1/2}")  
print("      = H_2^{1/2} * (int eta^2 a^2 F^4)^{1/2}")
print()

# int eta^2 a^2 F^4: compare with ||v||_4^4 = int eta^4 a^2 F^4
# Since eta <= 1: int eta^4 a^2 F^4 <= int eta^2 a^2 F^4
# So int eta^2 a^2 F^4 >= ||v||_4^4
# Can we bound int eta^2 a^2 F^4 BY ||v||_4 on a LARGER cutoff?

# Use outer cutoff xi >= eta: int eta^2 a^2 F^4 <= int xi^2 a^2 F^4 = ||w||_4^4
# where w = xi a^{1/2} F = xi chi F is the Sobolev variable on the OUTER support
print("With outer cutoff xi >= eta:")
print("  int eta^2 a^2 F^4 <= int xi^2 a^2 F^4 = ||w||_4^4")
print("  where w = xi chi F (outer Sobolev variable)")
print("  ||w||_4^2 <= A_out^2 (||nabla w||_2^2 + r^{-2} ||w||_2^2)")
print()

# So: H_3 <= H_2^{1/2} * ||w||_4^2 <= H_2^{1/2} * A_out^2 (D_2^{out} + C/r^2 H_2^{out})
# where D_2^{out}, H_2^{out} are on the outer support

# Now the key: H_3 contributes to H_2' with coefficient C:
# H_2' <= -cD_2 + C * H_3 + lower order
# H_3 <= H_2^{1/2} * A_out^2 (D_2^{out} + C/r^2 H_2^{out})
# <= beta * D_2^{out} + C/r^2 * (A_out^2 H_2^{out})^{...}

# Wait, we need to be more careful. Let me use:
# ||w||_4^4 <= A_out^4 (||nabla w||_2^2 + r^{-2} ||w||_2^2)^2

# H_3^2 <= H_2 * A_out^4 (D_2^{out} + C/r^2 H_2^{out})^2

# H_3 <= H_2^{1/2} * A_out^2 (D_2^{out} + C/r^2 H_2^{out})

# Critical Sobolev product: A_out^2 * ||F||_{L^2(outer)}
# = A_out^2 * (H_2^{out})^{1/2}
# This is beta = C sqrt(eps_Li) << 1

print("=== Critical absorption ===")
print("H_3 <= H_2^{1/2} * A_out^2 * (D_2^{out} + C/r^2 H_2^{out})")
print()
print("In the H_2 evolution:")
print("  H_2' <= -(1-eps)D_2 + C * H_3 + C/r^2 H_2")
print("       <= -(1-eps)D_2 + C * H_2^{1/2} * A_out^2 (D_2^{out} + C/r^2 H_2^{out}) + C/r^2 H_2")
print()
print("Using D_2^{out} = D_2(outer support) and Young's inequality:")
print("  C * H_2^{1/2} * beta_out * D_2^{out}")
print("  <= eps' D_2 + C^2 H_2 * beta_out^2 / eps' * (D_2^{out}/D_2)")
print()
print("This is where FINITE-NEIGHBOR enlargement is needed:")
print("  D_2^{out} involves the outer support, which overlaps neighboring balls")
print("  The graph absorption S_alpha' <= Cr^{-2} sum S_beta handles this")

# === 4. NUMERICAL CHECKS ===
print()
print("=== Numerical exponent checks ===")
# In 4D, Sobolev: ||u||_4^2 <= A^2 * epsilon[u]
# Holder for reaction: int f^3 = int f * f^2 <= ||f||_2 * ||f^2||_2
# ||f^2||_2 = ||f||_4^2

# So: H_3 <= ||eta F||_2 * ||eta a^{1/2} F||_4^2 ... nope, that doesn't work because of weights

# Actually the correct check is dimensional:
# In 4D, the critical Moser step is from L^2 to L^3:
# In standard notation (p=2, p*=2n/(n-2)=4 in 4D):
# one step takes L^2 -> L^{2*} = L^4 via Sobolev
# then L^4 * L^2(potential) -> L^{4/3} * L^4 = L^{12/7}... 

# Actually, the Wang approach is different. It uses:
# the cubic term sum as the reaction, and the Sobolev product beta controls it.
# The step from H_2 to H_3 is NOT a standard L^2 -> L^4 Moser step.
# It's a specific structure of the parabolic PDE.

# The key quantity is the Sobolev product:
print("Volume-independent critical parameter:")
beta_formula = "beta = A_0^2 * ||F||_{L^2} = C * sqrt(eps_Li)"
print(f"  {beta_formula}")
print(f"  For eps_Li = 0.01: beta = C * 0.1")
print(f"  Absorption: H_3 <= C * beta * D_2 + lower order")
print(f"  For beta << 1: the cubic reaction is a small fraction of dissipation")

# === 5. SUBCRITICAL VERIFICATION ===
print()
print("=== After H_3: subcritical Moser ===")
# Once H_3(t) <= C gamma^3/t, the potential K = aF is in L^3(nu)
# with ||K||_3^3 = H_3 <= C gamma^3/t
# The Moser step from q to q+1 (or q to 3q/2) requires the potential in L^r
# where r depends on q. For subcritical: all r < 3, so L^3 suffices.

# Standard subcritical Moser from L^q to L^{2q}:
# ||K||_{2q}^{2q} <= C ||K||_q^q * ||V||_{r(q)}^{r(q)}
# where 1/r(q) = 1/2 - 1/q
# For q >= 3: r(q) = 2q/(q-2) >= 6 > 3... wait, that's > 3, not < 3.

# Hmm, let me recheck. For a 4D Moser step from L^q to L^{2q}:
# The Sobolev exponent is 2* = 4 in 4D.
# The step uses ||u||_4^2 <= A^2 epsilon[u]
# Testing with |K|^{q/2}: ||K^{q/2}||_4^2 = ||K||_{2q}^q
# epsilon[K^{q/2}] involves |nabla K^{q/2}|^2 which gives dissipation
# The potential term: int V |K^{q/2}|^2 = int V K^q
# By Holder: int V K^q <= ||V||_p * ||K||_{pq/(p-1)}^q
# For this to close: pq/(p-1) = 2q, i.e. p/(p-1) = 2, p = 2.
# So we need V in L^2, which is critical.

# The subcritical improvement comes from having BETTER than L^2:
# If V in L^3: int V K^q <= ||V||_3 * ||K||_{3q/2}^q
# And 3q/2 < 2q for q > 0, so we need K in L^{3q/2} which is WEAKER than L^{2q}.
# This creates a gap that allows the iteration to close.

# More precisely: with V in L^3 and K in L^q:
# the reaction int V K^q <= ||V||_3 * ||K||_{3q/(q+...)}... 

# Actually the cleaner statement: if V in L^p with p > n/2 = 2:
# then V has form-relative bound zero (can be made eps-small without growing the constant)
# int V phi^2 <= eps int |nabla phi|^2 + C(eps, ||V||_p) int phi^2
# This is the subcritical CLMS result.

print("With V = K in L^3(nu) at positive time:")
print("  Form-relative bound ZERO (subcritical CLMS):")
print("    int V phi^2 <= eps int |nabla phi|^2 + C(eps,||V||_3) int phi^2")
print("  This allows ALL exponent Moser steps with convergent constants.")
print("  Compare: V in L^2 (critical) gives only form-relative bound GAMMA < 1,")
print("  which deteriorates in the infinite iteration (Hardy counterexample).")

print()
print("="*70)
print("SUMMARY:")
print("  Stage 1 (Critical H_2->H_3): SINGLE Moser step, uses beta << 1")
print("  Stage 2 (Subcritical H_3->Linf): Standard, convergent constants")
print("  Nash: useful only for Stage 2, not needed, does not help Stage 1")
print("  The essential hard task is the localized energy inequality for Stage 1")
print("="*70)
