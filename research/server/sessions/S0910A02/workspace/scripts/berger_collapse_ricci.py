# ERRATUM (Step 3): the computations below are only a fixed-Hopf-bundle shrinking model. They do NOT show that tight positive Ricci pinching excludes collapse; round lens spaces S^3/Z_m collapse with Ric=2g exactly. Use this script only as an anisotropy warning for fixed connection/topology shrinkage, not as evidence against quotient/orbifold-compatible collapse.

#!/usr/bin/env python3
"""
Compute Ricci eigenvalues of Berger spheres (collapsing Hopf fiber)
and generalized warped product models to test whether non-quotient
collapse creates order-1 Ricci anisotropy.

Key question: Under tight positive Ricci pinching delta_+(g) < eps,
can the manifold collapse (injectivity radius -> 0)?

If every collapsing model creates Ricci anisotropy >= eta_n > 0,
then tight positive pinching forces noncollapse, and P_n+ follows
from noncollapsed compactness + existence.

Berger sphere: S^3 with left-invariant metric
  g_eps = eps^2 * sigma_3^2 + sigma_1^2 + sigma_2^2
where sigma_i are the standard left-invariant 1-forms on SU(2).

As eps -> 0, the Hopf fiber shrinks: collapse to S^2.
As eps -> 1, we get the round S^3.
"""

import numpy as np

def berger_ricci_3d(eps):
    """
    Ricci eigenvalues of the 3D Berger sphere with fiber scale eps.
    
    The left-invariant metric on S^3 = SU(2) is:
    g = a^2 e^1⊗e^1 + b^2 e^2⊗e^2 + c^2 e^3⊗e^3
    
    For Berger: a = b = 1, c = eps.
    
    Structure constants: [e_1, e_2] = 2*e_3, etc.
    The Milnor frame sectional curvatures for a left-invariant
    metric on S^3 with eigenvalues (a^2, b^2, c^2):
    
    K_12 = (a^2+b^2-c^2)^2/(4a^2b^2) - (a^2-b^2+c^2)(a^2+b^2-c^2)/(2a^2b^2) 
    ...this is getting complicated. Let me use standard formulas.
    
    For Berger sphere (a=b=1, c=eps), the Ricci eigenvalues are:
    r_1 = r_2 = (2*eps^2 - eps^4 + 2) / (2)  ... actually let me derive carefully.
    
    Standard result: For the Berger metric g_eps on S^3 with
    g_eps = eps^2 sigma_3^2 + sigma_1^2 + sigma_2^2:
    
    Ric(e_1, e_1) = Ric(e_2, e_2) = 2*eps^2 (in the e_i frame where g(e_i,e_i)=1)
    wait no...
    
    Actually the standard Ricci tensor of the Berger sphere is:
    In an orthonormal frame {e_1, e_2, e_3} where e_3 is the Hopf direction:
    
    Ric(e_1, e_1) = Ric(e_2, e_2) = 2 - eps^2/2
    Ric(e_3, e_3) = eps^2/2
    
    Wait, that doesn't look right for eps=1 (round sphere should have Ric = 2g).
    
    Let me recalculate from first principles using the Milnor formula.
    """
    # Use the general formula for left-invariant metrics on S^3
    # With orthonormal basis (a,b,c) = (1, 1, eps) for Berger
    # Milnor's formula for SU(2):
    # Structure constants: [e1,e2] = 2*e3, [e2,e3] = 2*e1, [e3,e1] = 2*e2
    # For the metric with a = b = 1, c = eps:
    #
    # Sectional curvatures:
    # K_12 = (4eps^2 - (1 - 1 + eps^2)^2) / (1 * 1) ...
    
    # Actually, for SU(2) with left-invariant metric g_ij = diag(a^2, b^2, c^2):
    # The Ricci eigenvalues (in the orthonormal frame) are:
    # r_1 = 2/a^2 [a^4 - (b^2-c^2)^2] / (2*b^2*c^2)
    # 
    # Hmm, let me just use the known formula. For S^3 = SU(2) with
    # left-invariant metric g = e^1⊗e^1 + e^2⊗e^2 + t^2 e^3⊗e^3
    # (where e^i are the standard left-invariant 1-forms with
    # de^1 = -2e^2∧e^3, etc.)
    #
    # The Ricci tensor is (in the orthonormal frame):
    # Ric(E_1,E_1) = Ric(E_2,E_2) = 2*t^2
    # Ric(E_3,E_3) = 2/t^2 - 2 + 2*t^2 ??? 
    # Hmm this doesn't match at t=1.
    
    # Let me use a more careful derivation.
    # For SU(2) with structure constants [e_i, e_j] = 2*epsilon_{ijk}*e_k
    # and metric g = diag(a1^2, a2^2, a3^2) in the frame e_1, e_2, e_3:
    #
    # mu_1 = a1/(a2*a3), mu_2 = a2/(a1*a3), mu_3 = a3/(a1*a2)
    # Sectional curvatures (Milnor):
    # K_23 = mu_2*mu_3 - mu_1*(mu_2 + mu_3 - mu_1)
    # ... actually Milnor's formula for SU(2) (all structure constants = 1):
    # K_23 = [(mu_2+mu_3-mu_1)^2 - 4*mu_2*mu_3 + 4*mu_1*(mu_2+mu_3-mu_1)] / 4

    # This is getting complicated. Let me use a direct SageMath-style computation.
    # For the metric g = sigma_1^2 + sigma_2^2 + t^2*sigma_3^2 on S^3:
    # where sigma_i are left-invariant 1-forms with d(sigma_i) = 2*sigma_j∧sigma_k
    
    # The connection 1-forms in the orthonormal basis {e^1=sigma_1, e^2=sigma_2, e^3=t*sigma_3}:
    # omega^1_2 = -(2t - 1/t)*sigma_3 = -(2t - 1/t)/t * e^3
    # omega^1_3 = (1/t)*sigma_2 = (1/t)*e^2  [wait, need to be more careful]
    
    # Actually, I'll just use the known result for Berger spheres.
    # Reference: Besse, "Einstein Manifolds", Chapter 9, or many differential
    # geometry textbooks.
    
    # For the Berger metric g_t on S^3 with Hopf fiber scaled by t:
    # g_t = (standard round metric on CP^1) + t^2*(Hopf fiber)^2
    # In the orthonormal frame:
    # Ric = diag(2-t^2, 2-t^2, 2t^2-2+2t^{-2}) ... hmm
    
    # Let me just compute numerically for a few values and interpolate.
    # Round S^3 (t=1): Ric = 2g, so all eigenvalues = 2. CHECK.
    # Berger (t→0): horizontal Ricci → ?, vertical Ricci → ?
    
    # Standard result from Besse p. 255:
    # Berger sphere (S^{2n+1}, g_t) with fiber parameter t:
    # Horizontal Ricci = 2n+2 - 2t^2 (for unit sphere, n=1: 4 - 2t^2... no)
    
    # OK I'll just use the 3D formula directly.
    # For S^3 with metric g_t having Hopf fiber scaled by t:
    # Using Berger's computation (see e.g. Petersen, Riemannian Geometry, Example 4.4.4):
    
    # Sectional curvatures:
    # K(horizontal plane) = 4 - 3t^2  (for t ∈ (0, 2/√3))
    # K(vertical plane) = t^2
    
    # Wait, this is for a different normalization. Let me be precise.
    
    # The Berger metric on S^3: Start with the round metric g_1 of constant
    # curvature 1. The Hopf fibration π: S^3 → S^2 has fiber S^1. The Berger 
    # metric g_t is obtained by scaling the vertical (fiber) component by t^2:
    # g_t = g_H + t^2 * g_V where g_H is the horizontal part and g_V = η⊗η
    # (η being the connection 1-form of the Hopf bundle).
    
    # For g_t with this convention:
    # Sectional curvature of horizontal plane: K_H = 4 - 3t^2
    # Sectional curvature of mixed plane: K_V = t^2
    
    # Ricci eigenvalues in dimension 3:
    # r_H = K_H + K_V = 4 - 3t^2 + t^2 = 4 - 2t^2
    # r_V = K_V + K_V = 2t^2 (there are two vertical planes... wait no)
    
    # In dim 3: Ric(X,X) = K(X,Y) + K(X,Z) for orthonormal {X,Y,Z}
    # For horizontal X: Ric(X,X) = K(X, other horizontal) + K(X, vertical) = K_H + K_V
    # For vertical X: Ric(X,X) = K(X, horiz1) + K(X, horiz2) = K_V + K_V = 2K_V
    
    # So: Ric_horizontal = 4 - 3t^2 + t^2 = 4 - 2t^2
    # Ric_vertical = 2t^2
    
    # At t=1: Ric_H = 4-2 = 2, Ric_V = 2. CHECK (round S^3 of curvature 1).
    
    t = eps
    ric_h = 4 - 2*t**2  # horizontal
    ric_v = 2*t**2       # vertical (Hopf fiber direction)
    
    return ric_h, ric_v

print("=" * 70)
print("Berger sphere S^3: Ricci eigenvalues vs. fiber parameter t")
print(f"{'t':>8} {'Ric_horiz':>10} {'Ric_vert':>10} {'s/3':>8} {'delta_+':>10} {'delta_-':>10}")
print("-" * 62)

for t in [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.01]:
    rh, rv = berger_ricci_3d(t)
    s = 2*rh + rv  # scalar curvature (3 eigenvalues: rh, rh, rv)
    
    # For positive branch: normalize so that center is +1
    # eigenvalues are rh, rh, rv. We want delta_+ = max|r_i - 1|/1
    # But first need to rescale: if we want Ric ≈ +1·g, set g' = sigma*g
    # where sigma = s/3 (average Ricci eigenvalue / 1)
    # Then Ric_{g'} = Ric_g, eigenvalues of g'^{-1}Ric_{g'} = eigenvalues of g^{-1}Ric_g / sigma
    # Wait no: Ric_{cg} = Ric_g as (0,2) tensor. (cg)^{-1}Ric_{cg} = c^{-1}g^{-1}Ric_g = c^{-1}A_g.
    
    # The normalized defect delta_sigma is the operator norm of (A_g - sigma*Id):
    # For positive branch: we want to minimize delta_+(g) over all constant rescalings
    # delta_+(cg) = max|c^{-1}*a_i - 1| where a_i are eigenvalues of g^{-1}Ric
    
    # The eigenvalues of g_t^{-1}Ric_{g_t} are: rh (multiplicity 2) and rv (multiplicity 1)
    # For positive branch: delta_+ = min over c>0 of max(|rh/c - 1|, |rv/c - 1|)
    # Optimal c = (rh + rv)/2 (midpoint of the interval [min, max])
    
    if rh > 0 and rv > 0:
        # Optimal c for positive branch: c = (rh + rv)/2
        c_opt = (rh + rv) / 2
        d_p = max(abs(rh/c_opt - 1), abs(rv/c_opt - 1))
        
        # For negative branch: delta_-(cg) = max|c^{-1}*a_i + 1|
        # Need c^{-1}*a_i ≈ -1, so c = -a_i (impossible since a_i > 0 and c > 0)
        # So delta_- ≥ 1 when all eigenvalues are positive
        d_m = float('inf')  # can't approach -1 with positive eigenvalues
    else:
        d_p = float('inf')
        d_m = float('inf')
    
    print(f"{t:8.4f} {rh:10.4f} {rv:10.4f} {s/3:8.4f} {d_p:10.4f} {'inf':>10}")

print()
print("KEY OBSERVATION:")
print("As t -> 0 (Berger collapse), Ric_horiz -> 4, Ric_vert -> 0.")
print("The Ricci anisotropy (rh - rv)/rh -> 1, delta_+ -> 1.")
print("Therefore Berger collapse creates ORDER-1 Ricci anisotropy.")
print()

# Now higher-dimensional Berger spheres S^{2n+1}
print("=" * 70)
print("Higher-dimensional Berger spheres S^{2n+1}")
print()

for n in [1, 2, 3, 4, 10]:
    dim = 2*n + 1
    print(f"--- S^{dim} (n={n}) ---")
    print(f"{'t':>8} {'Ric_H':>10} {'Ric_V':>10} {'delta_+':>10}")
    print("-" * 45)
    
    for t in [1.0, 0.5, 0.1, 0.01]:
        # For S^{2n+1} with Berger metric (fiber scaled by t):
        # Standard formulas (see Besse, Einstein Manifolds, or Ziller):
        # Horizontal Ricci = 2n + 2 - (2n+2)*t^2 + 2n*t^2  
        # Wait, that doesn't work for n=1.
        
        # Actually, for S^{2n+1} -> CP^n with Fubini-Study base:
        # K(horizontal, horizontal) = 1 + 3t^2 * (something)... 
        # This depends on whether the horizontal vectors are in the same complex line.
        
        # For S^{2n+1}, the sectional curvatures of the Berger metric g_t are:
        # K(X,Y) = 1 for horizontal X,Y (perpendicular to complex structure J)
        #         ... actually this is complicated for general n.
        
        # Standard result from Ziller:
        # Ric(X,X) = 2n + 2 - 2t^2 for horizontal X (in S^{2n+1})
        # Ric(V,V) = 2n*t^2 for vertical V
        
        # CHECK for n=1, t=1: Ric_H = 2+2-2 = 2, Ric_V = 2*1 = 2. 
        # That gives Ric = 2g on round S^3. CHECK.
        
        ric_h = 2*n + 2 - 2*t**2
        ric_v = 2*n*t**2
        
        # Positive branch delta:
        if ric_h > 0 and ric_v > 0:
            c_opt = (ric_h + ric_v) / 2
            d_p = max(abs(ric_h/c_opt - 1), abs(ric_v/c_opt - 1))
        else:
            d_p = float('inf')
        
        print(f"{t:8.4f} {ric_h:10.4f} {ric_v:10.4f} {d_p:10.4f}")
    print()

print("CONCLUSION:")
print("In all dimensions, Berger sphere collapse (t -> 0) creates")
print("Ric_V -> 0 while Ric_H -> 2(n+1). The Ricci anisotropy ratio")
print("delta_+ -> 1 as t -> 0. Therefore:")
print()
print("HOPF-FIBER COLLAPSE IS INCOMPATIBLE WITH TIGHT POSITIVE RICCI PINCHING.")
print()
print("This is one piece of the 'no bad collapse' argument for P_n+.")
print("It must be generalized from Hopf to all possible collapsing models.")
print("The key structural ingredient: O'Neill formulas for Riemannian submersions")
print("show that fiber shrinking always creates Ricci splitting between")
print("horizontal and vertical directions, unless the fiber is totally geodesic")
print("and flat (= quotient by isometry group), which preserves Einstein.")
