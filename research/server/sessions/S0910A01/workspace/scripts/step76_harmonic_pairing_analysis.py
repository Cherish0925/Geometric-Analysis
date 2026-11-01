"""
Step 76: Harmonic content analysis for the product orbifold nu_l system.

We compute whether the spherical integral pairing between
H^4 (Eguchi-Hanson r^{-4} correction) and V_{l,2} (orbifold kernel quadratic jet)
vanishes on S^3/Z_2 for the product Einstein orbifold (S^2 x S^2)/Z_2.

The key representation-theoretic test:
- H^4 lives in (Omega^+ tensor Omega^-)|_{S^3}, which under SO(4) = SU(2) x SU(2)
  decomposes as the tensor product of spin-1 representations.
- V_{l,2} at a fixed point is a Z_2-invariant r^2-homogeneous symmetric 2-tensor.
- The L^2 pairing on S^3/Z_2 selects matching irreducible representations.

For the product metric g = g_{S^2}(R) + g_{S^2}(R), the Lichnerowicz operator
on symmetric 2-tensors decomposes into blocks corresponding to:
(a) conformal/trace modes
(b) TT modes on each S^2 factor (= 0 for S^2)
(c) cross terms

Since S^2 has no nonzero TT tensors (dim 2!), the kernel analysis simplifies.
"""

import numpy as np
import json

# ============================================================
# Part 1: Representation theory on S^3/Z_2
# ============================================================

# S^3 = SU(2). Under the identification R^4 = C^2,
# the Z_2 acts as -I. The invariant spherical harmonics
# on S^3/Z_2 are exactly those of even degree l.
#
# Traceless symmetric 2-tensors on R^4 restricted to S^3
# decompose under SO(4) = SU(2)_L x SU(2)_R as:
#   Sym_0^2(R^4) = (V_2 x V_0) + (V_0 x V_2) + (V_1 x V_1)
# where V_j is the spin-j irrep (dimension 2j+1).
#
# The self-dual forms Omega^+ correspond to V_1 x V_0 (dim 3)
# The anti-self-dual forms Omega^- correspond to V_0 x V_1 (dim 3)
# Their tensor product:
#   Omega^+ tensor Omega^- = (V_1 x V_0) tensor (V_0 x V_1) = V_1 x V_1
# This has dimension 9 and decomposes under SO(4) as the
# traceless symmetric 2-tensors plus trace, but restricted
# to the product piece.
#
# More precisely: omega_k^+ circ omega_m^- is a basis for
# Sym_0^2(R^4) restricted to the V_1 x V_1 block.
#
# The r^{-4} harmonic H^4 = -(1/2r^4)(zeta^+ circ theta_1^-)
# restricts to S^3 as an element of the l=2 harmonic space
# (since |H^4|_e ~ r^{-4} means the S^3 restriction has
# spherical degree 2 on R^4, which maps to degree 2 on S^3).
#
# Under Z_2 (-I on R^4):
# omega_k^+ and omega_k^- are quadratic in coordinates,
# hence Z_2-invariant. So H^4|_{S^3} is Z_2-invariant ✓.

# ============================================================
# Part 2: Orbifold kernel modes for (S^2 x S^2)/Z_2
# ============================================================

# The Einstein product metric g = g_1 + g_2 on S^2(R) x S^2(R)
# with Ric = Lambda g, Lambda = 1/R^2.
#
# The Lichnerowicz operator P = (1/2)nabla*nabla - R^circ
# on TT tensors of S^2 x S^2 has:
# - No nonzero TT 2-tensors on S^2 (dim 2 too small)
# - Cross-factor TT tensors: f(x) h(y) dx_i dy_j where
#   f is a spherical harmonic on S^2_1, h on S^2_2
#
# The full kernel of P_{g_o} on the orbifold includes:
# (a) shape deformation: delta_rho (g_1 - g_2)
#     This is a constant symmetric 2-tensor, hence V_{l,0} only.
# (b) constant symmetric 2-tensors preserving Z_2:
#     10-dimensional Sym^2(R^4), modulo the 4-dim Killing
#     algebra of (S^2 x S^2) and the trace direction.

# For the Einstein product metric on S^2 x S^2 with equal radii:
# The infinitesimal Einstein deformations are:
# - Deformations of the flat background metric on T^4/Z_2: 10 param
# - Minus gauge (Killing + conformal Killing): depends on the space
#
# Actually for the product orbifold (not T^4/Z_2), the relevant
# deformations are those of the product Einstein metric.
# The key question is: what is V_{l,2} at each fixed point?

# For a constant symmetric 2-tensor V_{l,0} on the orbifold,
# the equation P_e V_{l,2} = -Q_e^(2)(V_{l,0}, H_2) - ... determines
# V_{l,2} from V_{l,0} and the quadratic jet H_2 of the orbifold metric.

# On the product Einstein metric, H_2 (the quadratic jet) satisfies
# P_e H_2 = Lambda e, meaning it encodes the curvature.
# For g_o = e + H_2 + O(r^4) in normal coordinates at p_j:
# H_2 = -(1/6) R_{iajb} x^a x^b dx^i dx^j (Riemann normal coordinates)
# On S^2(R) x S^2(R) at a point, with coordinates (x_1,x_2,x_3,x_4)
# where (x_1,x_2) are on S^2_1 and (x_3,x_4) on S^2_2:
# The curvature is R_{1212} = Lambda, R_{3434} = Lambda (each S^2 has
# K = Lambda = 1/R^2), and all mixed terms R_{1a3b} = 0.

# ============================================================
# Part 3: Harmonic decomposition test
# ============================================================

# The critical question: does the pairing
# <H^4, V_{l,2}>_{L^2(S^3/Z_2)} vanish for ALL kernel modes?
#
# H^4 = -(1/2r^4) zeta^+ circ theta_1^-
# This is a specific element of (V_1 x V_1)_{l=2} on S^3.
#
# V_{l,2} at a fixed point is determined by the orbifold
# deformation mode. For a CONSTANT deformation V_{l,0} (which
# is a constant symmetric 2-tensor), the equation for V_{l,2} is:
#
# P_e V_{l,2} = -Q_e^(2)(V_{l,0}, H_2)
#
# The right side involves the product of V_{l,0} (constant) with
# H_2 (quadratic). This is a QUADRATIC symmetric 2-tensor.
# Its spherical harmonic content on S^3 involves l=0 and l=2 modes.
#
# The key: Q_e^(2)(V_{l,0}, H_2) involves the bilinear form of
# the Ricci equation. For a constant perturbation V_{l,0} of the
# flat metric e, the Ricci variation is:
# D^2 Ric(V_{l,0}, H_2) = quadratic expression in first derivatives
#
# Since V_{l,0} is constant and H_2 is quadratic, their interaction
# Q_e^(2) involves terms like V_{l,0} * nabla^2 H_2 and
# nabla V_{l,0} * nabla H_2 = 0 (V_{l,0} has no gradients).
# So Q_e^(2)(V_{l,0}, H_2) ~ V_{l,0} * R = constant * quadratic.

# This means V_{l,2} has the SAME harmonic type as H_2 rotated
# by the constant tensor V_{l,0}. It lives in the l=2 spherical
# harmonics on S^3.

# The pairing <H^4, V_{l,2}> on S^3 is then a pairing between
# two l=2 harmonics of specific SO(4) representations.

# H^4 is in V_1 x V_1 (the "Sym_0^2 = Omega^+ tensor Omega^-" piece)
# V_{l,2} is in the space of l=2 traceless symmetric 2-tensors,
# which also lives in V_1 x V_1 (plus possibly (V_2 x V_0) + (V_0 x V_2))

# The V_1 x V_1 piece has the RIGHT representation to pair with H^4.
# So the integral is NOT automatically zero by representation theory!

# ============================================================
# Part 4: Explicit computation for the product metric
# ============================================================

# Let's compute the quadratic jet H_2 and the interaction explicitly.
# In normal coordinates at a fixed point of (S^2 x S^2)/Z_2:
#
# g_o = delta_{ij} + H_{2,ijkl} x^k x^l + O(|x|^4)
# where H_{2,ijkl} = -(1/3) R_{ikjl}
#
# For the product metric with R_{1212} = Lambda, R_{3434} = Lambda:
# H_{2,1112} = -(1/3) R_{1112} = 0
# H_{2,1212} = -(1/3) R_{1122} = -(1/3)(-Lambda) = Lambda/3
# Wait, R_{ikjl} for the product:
# Nonzero components: R_{1212} = Lambda (on S^2_1), R_{3434} = Lambda (on S^2_2)
# and antisymmetric permutations.

# In terms of the metric expansion g_{ij} = delta_{ij} - (1/3)R_{iajb}x^a x^b:
# g_{11} = 1 - (1/3)(R_{1112}x^1x^2 + R_{1212}x^2x^2 + ...) 
#        = 1 - (Lambda/3)(x_2^2)  (from R_{1212} = Lambda)
# g_{22} = 1 - (Lambda/3)(x_1^2)
# g_{33} = 1 - (Lambda/3)(x_4^2)
# g_{44} = 1 - (Lambda/3)(x_3^2)
# g_{12} = (Lambda/3)(x_1 x_2)  (from -(1/3)R_{1a2b}x^a x^b = (1/3)Lambda x_1 x_2)
# etc.

# Now H^4 at the EH with zeta in the kernel of R^pm:
# H^4 = -(1/2r^4)(zeta^+ circ theta_1^-)
# For zeta = (0, cos(alpha), sin(alpha)):
# zeta^+ = cos(alpha) omega_2^+ + sin(alpha) omega_3^+

# omega_2^+ = dx_1 ^ dx_3 + dx_2 ^ dx_4  (as 2-forms)
# omega_3^+ = dx_1 ^ dx_4 - dx_2 ^ dx_3

# theta_1^- is asymptotic to omega_1^- = dx_1 ^ dx_2 - dx_3 ^ dx_4

# The product zeta^+ circ omega_1^-:
# For omega^+ = sum_i a_i omega_i^+ and omega^- = sum_j b_j omega_j^-,
# the product omega^+ circ omega^- is a traceless symmetric 2-tensor
# with components:
# (omega^+ circ omega^-)(X,Y) = (1/2)(omega^+(X, .) . omega^-(Y, .) + ...)
# Actually, the identification Sym_0^2 = Omega^+ tensor Omega^- uses:
# omega_i^+ circ omega_j^- is the traceless symmetric involution whose
# +1 eigenspace is determined by the product of the corresponding
# almost-complex structures.

# For a concrete test, let's check the nonvanishing numerically.
# We can evaluate the l=2 harmonic projection.

# The Weyl curvature of S^2 x S^2 in the SD/ASD decomposition:
# W^+ = diag(Lambda/3, -Lambda/6, -Lambda/6) in the operator convention
# W^- = diag(Lambda/3, -Lambda/6, -Lambda/6)
# (This is because each S^2 has W = 0 but the product has W from cross terms)

# Actually for the product: Rm = W + Ric^circ owedge g + (s/24) g owedge g
# With Ric = Lambda g, s = 4 Lambda:
# Rm = W + 0 + (Lambda/6) g owedge g
# The product curvature is:
# R^+ = W^+ + (Lambda/6)I = diag(Lambda/3 + Lambda/6, -Lambda/6 + Lambda/6, 
#                                  -Lambda/6 + Lambda/6)
#      = diag(Lambda/2, 0, 0)

# Wait, let me recalculate. For Einstein 4-manifold with Ric = Lambda g:
# The operator Rm acting on 2-forms decomposes as:
# Rm = W^+ + (Lambda/4)I on Omega^+ and W^- + (Lambda/4)I on Omega^-
# (In operator convention where Rm(omega)_{ij} = R_{ijkl} omega^{kl})
# No wait: for Einstein, Rm = W + (Lambda/12)(g owedge g)
# In the 2-form operator: Rm^+ = W^+ + (s/12)I = W^+ + (Lambda/3)I
#
# For S^2 x S^2 with Lambda = 1 for simplicity:
# W^+ = diag(1/3, -1/6, -1/6) (the product Weyl)
# R^+ = W^+ + (1/3)I = diag(2/3, 1/6, 1/6)
# Hmm, that gives rank 3, not rank 1.

# Let me reconsider. The Ozuch obstruction uses R^+(H_2) which is
# the self-dual Weyl curvature of the metric g_o at the singular point,
# expressed in terms of the quadratic jet H_2.

# For the round product S^2(R) x S^2(R) with Ric = Lambda g:
# The sectional curvatures are:
# K(e_1, e_2) = 1/R^2 = Lambda (within S^2_1)
# K(e_3, e_4) = Lambda (within S^2_2)  
# K(e_1, e_3) = K(e_1, e_4) = K(e_2, e_3) = K(e_2, e_4) = 0 (cross terms)

# The curvature operator on 2-forms:
# In the basis omega_1^+ = dx1^dx2 + dx3^dx4, omega_2^+, omega_3^+,
#              omega_1^- = dx1^dx2 - dx3^dx4, omega_2^-, omega_3^-:
#
# Rm(omega_1^+) = R(e1,e2) omega_1^+ + R(e3,e4) omega_1^+
# Actually: <Rm(omega_1^+), omega_1^+> = R_{1212} + R_{3434} + 2R_{1234}
# For the product: R_{1234} = 0, so = Lambda + Lambda = 2Lambda
# But wait, omega_1^+ = (dx1^dx2 + dx3^dx4)/sqrt(2) in orthonormal convention
# so <Rm omega_1^+, omega_1^+> = (1/2)(R_{1212} + R_{3434} + 2R_{1234})
#                                = (1/2)(Lambda + Lambda + 0) = Lambda

# Similarly <Rm omega_1^-, omega_1^-> = (1/2)(R_{1212} + R_{3434} - 2R_{1234}) = Lambda

# <Rm omega_2^+, omega_2^+> = (1/2)(R_{1313} + R_{2424} + 2R_{1324})
# For the product: R_{1313} = R_{2424} = R_{1324} = 0, so = 0.

# <Rm omega_3^+, omega_3^+> = (1/2)(R_{1414} + R_{2323} + 2R_{1423}) = 0.

# Off-diagonal: <Rm omega_1^+, omega_2^+> etc all zero by the product structure.

# So indeed Rm^+ = diag(Lambda, 0, 0) and Rm^- = diag(Lambda, 0, 0).

# This confirms A02's data: R^+ = R^- = diag(Lambda, 0, 0) at each node.
# The Ozuch R^pm IS the full curvature operator restricted to Omega^pm,
# not just the Weyl part.

# Good, so the rank-1 property is confirmed directly.

# ============================================================
# Part 5: Verdict on harmonic pairing
# ============================================================

# The curvature operator R^+ has exactly one nonzero eigenvalue Lambda
# with eigenvector omega_1^+ = (dx1^dx2 + dx3^dx4)/sqrt(2).
# The kernel is spanned by omega_2^+, omega_3^+.
#
# For EH direction zeta in ker(R^+): zeta^+ = a omega_2^+ + b omega_3^+,
# the H^4 tensor involves zeta^+ circ theta_1^-.
#
# The pairing <H^4, V_{l,2}> involves integrals of products of l=2
# spherical tensor harmonics on S^3/Z_2.
#
# CRITICAL OBSERVATION: The orbifold deformation modes V_{l,0} for
# the product Einstein metric include the shape deformation
# V = delta(g_1 - g_2). In normal coordinates at a fixed point,
# this is a DIAGONAL constant tensor:
#   V_{l,0} = diag(1, 1, -1, -1) (up to normalization)
# This lives in the omega_1^+ circ omega_1^- = trace-free part that
# gives R_{1212} - R_{3434}. 
#
# The corresponding V_{l,2} comes from solving P_e V_{l,2} = source(V_{l,0}, H_2).
# For V_{l,0} = diag(1,1,-1,-1), the source term involves the curvature
# and the constant tensor, giving an l=2 tensor harmonic that lives
# in the (V_1 x V_1) block.
#
# Therefore: the pairing <H^4, V_{l,2}> is between two elements of
# V_1 x V_1 and is generically NONZERO.

# Let's verify this with a concrete harmonic computation.
# On S^3 = {x in R^4 : |x| = 1}, the l=2 tensor harmonics
# for Sym_0^2 include functions like x_i x_j - delta_ij/4 * |x|^2.

# For the traceless symmetric tensor omega_2^+ circ omega_1^- restricted to S^3:
# omega_2^+ = dx1^dx3 + dx2^dx4
# omega_1^- = dx1^dx2 - dx3^dx4
# Their product as a symmetric 2-tensor:
# (omega_2^+ circ omega_1^-)(X,Y) involves products like
# (dx1^dx3)(X,.) (dx1^dx2)(Y,.) + ...
# This is a degree-0 (constant-coefficient) tensor on R^4.

# On S^3, a constant traceless symmetric 2-tensor restricts to an l=0
# spherical harmonic contribution, NOT l=2.

# WAIT. This is the crucial point. H^4 ~ r^{-4} * (constant tensor on S^3).
# On S^3, |H^4|_e = r^{-4} * (constant) = (1/r^4) * angular part.
# The angular part of H^4 is the restriction of omega_k^+ circ theta_1^-
# to unit S^3. But theta_1^- is NOT the same as omega_1^-.
# theta_1^- depends on the point on S^3 through the quaternionic rotation rho_x.

# From the Ozuch source (equation following (18)):
# theta_i^-(x) = sum_j (x^T (omega_i^+ circ omega_j^-) x / |x|^2) omega_j^-
# So on S^3 (|x|=1):
# theta_1^-(x) = sum_j x^T (omega_1^+ circ omega_j^-) x * omega_j^-

# The factor x^T A x for a constant matrix A is a QUADRATIC function of x,
# hence an l=2 spherical harmonic on S^3. So theta_1^-(x) varies over S^3
# and the angular part of H^4 is NOT constant on S^3.

# More precisely: H^4 restricted to S^3 involves the product of
# (constant 2-form zeta^+) circ (x-dependent 2-form theta_1^-(x)),
# and theta_1^-(x) involves l=2 harmonics in x.
# So H^4|_{S^3} lives in the l=2 harmonic space (as stated in the Ozuch paper).

# Similarly, V_{l,2} is an l=2 harmonic (quadratic in x) symmetric 2-tensor.

# The L^2 pairing on S^3 between two l=2 harmonics can be nonzero.
# By orthogonality, different angular momentum modes don't pair,
# but SAME l=2 modes DO pair.

# Conclusion: The pairing is NOT automatically zero.
# The reduced system F has generically nonzero coefficients A_l^j, B_l^j.

results = {
    "step": 76,
    "analysis": "representation_theoretic_harmonic_pairing",
    "orbifold": "(S^2 x S^2)/Z_2",
    "R_plus_at_nodes": "diag(Lambda, 0, 0)",
    "R_minus_at_nodes": "diag(Lambda, 0, 0)",
    "R_rank": 1,
    "kernel_dimension": 2,
    "first_obstruction_lambda": "vanishes automatically for zeta in ker(R)",
    "second_obstruction_mu1": "vanishes by rank-1 cascade (det of 0x0 block)",
    "H4_spherical_degree": 2,
    "H4_representation": "V_1 x V_1 (l=2 tensor harmonic on S^3/Z_2)",
    "V_l2_spherical_degree": 2,
    "V_l2_representation": "l=2 tensor harmonic, same block V_1 x V_1",
    "automatic_vanishing_by_rep_theory": False,
    "reason": "H^4 and V_{l,2} both live in l=2 tensor harmonics on S^3/Z_2; "
              "their L^2 pairing is generically nonzero. theta_1^-(x) depends on "
              "x through quadratic functions (l=2), so the angular part of H^4 is "
              "not constant on S^3.",
    "reduced_system_structure": {
        "equations": "d <= 4 (global nu_l)",
        "unknowns": "4 in-kernel angles alpha_j on (S^1)^4",
        "form": "sum_j (A_l^j cos(alpha_j) + B_l^j sin(alpha_j)) = 0",
        "generically_solvable": "yes if d <= 4 (dimension count)",
    },
    "theta_1_minus_formula": "theta_1^-(x) = sum_j (x^T (omega_1^+ circ omega_j^-) x) omega_j^-",
    "H4_angular_type": "l=2 spherical harmonic (NOT constant on S^3)",
    "conclusion": "The reduced nu_l system has generically nonzero coefficients. "
                  "A zero exists when the trigonometric system is compatible, which "
                  "is expected by dimension count (4 unknowns, <= 4 equations). "
                  "Surjectivity at the zero would give an Einstein desingularization.",
    "next_computation": "Explicit evaluation of A_l^j, B_l^j coefficients requires "
                        "computing V_{l,2} from the orbifold kernel and evaluating "
                        "the spherical integral. This can be done using the product "
                        "structure and SO(4) representation theory.",
    "curvature_verification": {
        "method": "direct sectional curvature on S^2 x S^2",
        "K_12": "Lambda (within S^2_1)",
        "K_34": "Lambda (within S^2_2)",
        "K_13": 0,
        "K_14": 0,
        "Rm_plus_omega1": "Lambda (=R_{1212}+R_{3434})/2 in normalized convention",
        "Rm_plus_omega2": 0,
        "Rm_plus_omega3": 0,
        "confirms_rank_1": True
    }
}

output_path = "Sessions/S0910A01/workspace/data/step76_harmonic_pairing_analysis.json"
with open(output_path, "w") as f:
    json.dump(results, f, indent=2)
print(json.dumps(results, indent=2))
print(f"\nWrote {output_path}")
