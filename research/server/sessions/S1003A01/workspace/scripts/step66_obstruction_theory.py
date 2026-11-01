"""Step 66: derive the degree-2 Taylor coefficient of Delta q at a nondegenerate torsion zero.

Goal: show that the Step-65 exact scalar equation
  Delta q = 8 tr V^2 - 24|eta|^2 - (3s/2)q - (9/4)q^2 + 16 sum <(nabla_i W+) nabla_i u, u>
differentiated twice at q=0, dq=0, yields a quadratic form in nabla^3 Omega whose
sign on the admissible third jets decides A02's Phi6.

Method: expand each term to degree 2 in normal coordinates, using:
  - the second jet (nabla^2 Omega, nabla^2 g) from the D=6 solution
  - the third jet (nabla^3 Omega, nabla^3 g) as unknowns
  - Ric = lam g through degree 4 (fixes nabla^2 g from nabla^2 omega)

The degree-2 part of Delta q(x) at x=0 is Hess(Delta q)/2. We need:
  [Delta q]_2 = 8 [tr V^2]_2 - 24 [|eta|^2]_2 - (3s/2)[q]_2 - (9/4)[q^2]_2 + 16 [source]_2

where [f]_2 means the degree-2 homogeneous part of f's Taylor expansion.

Key observation: [q]_2 = (Hess q) = 2 sum_i |nabla^2_{.i} Omega|^2 >= 0 (from the second jet).
So (3s/2)[q]_2 is a known contribution from the second jet only (s < 0 makes it positive).
Similarly [q^2]_2 = 0 since q = O(|x|^2) implies q^2 = O(|x|^4).

[source]_2 involves nabla_i W+ and nabla_i u terms; at the zero, nabla u = 0, so the
source term starts at degree 1 (nabla^2 u times nabla W+) and its degree-2 part
involves the THIRD jet of Omega.

The critical question: does [source]_2 contain a definite quadratic in the third jet?
"""
import numpy as np
import sympy as sp

# Just compute the degree-2 structure symbolically for orientation

# At a torsion zero with first jet f = c z + B zbar:
# q(x) = ||nabla Omega(x)||^2 = 4|a(x)|^2 where a is the torsion 1-form
# a(x) = M x + (1/2) M2(x,x) + ... where M = nabla a(0) (4x4 matrix)
# M2[k,l,m] = nabla_k nabla_l a_m (three-index tensor, symmetric in k,l)

# q(x) = 4|M x|^2 + 4 (M x . M2(x,x)) + O(|x|^4)
# [q]_0 = 0 (at the zero)
# [q]_1 = 0 (dq = 0)
# [q]_2 = 4 |M x|^2 = 4 x^T M^T M x  (known from second jet, positive semidefinite)

# Delta q = laplacian of q:
# [Delta q]_0 = 4 tr(M^T M) = 4 ||M||_F^2  (the cone identity)
# [Delta q]_1 = 8 tr(M^T partial_k M2) summed over k... 
# Actually at the zero the laplacian of |Mx|^2 gives a degree-0 term (the cone)
# and a degree-1 term from the variation of M2 (the third jet).

# The Weyl-curvature terms:
# tr V^2 at degree 0: 4||A||^2 (Step 62 dictionary)
# |eta|^2 at degree 0: 4|c|^2
# At degree 1: partial_k(tr V^2) and partial_k(|eta|^2) depend on nabla W+ which
#   for Einstein is controlled by the Derdzinski equation.

# The key observation from A02: at degree 2 (their Ricci-degree 6),
# the scalar equation produces a definite quadratic in the portion of
# the 4-jet (i.e., nabla^4(g, Omega)) that remains free after the 
# Einstein/AK equations through degree 4 are imposed.

# This translates to: after substituting the Einstein equations for 
# nabla^2 Ric = 0 (at degree 4), nabla Ric = 0 (at degree 3), etc.,
# the remaining freedom in the 4-jet of (g, Omega) is a finite-dimensional
# space, and the scalar equation imposes a definite quadratic on it.

# The theoretical explanation would come from the structure of 
# Delta q - 8 tr V^2 + 24|eta|^2 + (3s/2)q at degree 2:

# (3s/2)[q]_2 = (3s/2) * 4 * ||M||^2 * (unit quadratic in x)
# For s < 0, this is a negative contribution to [Delta q]_2

# But [Delta q]_2 must equal the degree-2 coefficient of the RHS,
# which involves [tr V^2]_2, [|eta|^2]_2, and [source]_2.

# The "source" = sum <(nabla_i W+) nabla_i u, u> has degree-2 part
# involving nabla^2 W+ (from the Ricci curvature at the zero) and
# nabla^2 u (from the second torsion jet). Since W+ at the zero is
# s/6*I + V (known), nabla W+ involves the third jet of the metric,
# which is controlled by Ric = lam g at degree 1 (through Christoffel).

print("Structural analysis of the order-6 identity:")
print("  [Delta q]_2 = 8[trV^2]_2 - 24[|eta|^2]_2 - (3s/2)[q]_2 + 16[source]_2")
print("  [q]_2 = 4||M||^2 (positive semidefinite, from second jet)")
print("  [q^2]_2 = 0 (q = O(|x|^2))")
print("  [source]_2 depends on nabla^3 Omega (the NEW information)")
print("")
print("The solvability condition Phi6 > 0 means:")
print("  The total degree-2 identity cannot be satisfied for any choice")
print("  of nabla^3 Omega (and related 4-jet), because the positive")
print("  definite contribution from certain squares exceeds the")
print("  negative contribution from the source term.")
print("")
print("This would prove: no real AKE germ has a nondegenerate torsion zero.")
