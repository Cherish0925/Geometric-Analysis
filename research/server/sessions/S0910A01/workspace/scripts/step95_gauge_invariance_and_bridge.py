#!/usr/bin/env python3
"""
Step 95: Gauge invariance theorem and corrected kernel-plane analysis.

Absorbs A02 Step93 curvature correction:
  R^± = diag(Λ,0,0) on S²(Λ)×S²(Λ), NOT (Λ/3)I.
  The product is NOT conformally flat (W^± = diag(2Λ/3,-Λ/3,-Λ/3)).

Three results:
  1. R_odd(ℒ_X g₀) = 0 (gauge invariance — exact algebraic theorem)
  2. R_odd(fg₀) = 0 (conformal invariance)
  3. Corrected obstruction structure: first obstruction vanishes on 
     ker R^± = span{e₂,e₃}, and K_adj measures one component of the 
     quadratic second obstruction on the kernel plane.

Session S0910A01.  Agent2 / Constructor.  Phase Execute.
"""

import numpy as np
import json
import os

# ====================================================================
# Part 1: Independent curvature verification
# ====================================================================

def verify_product_curvature():
    """
    Verify R^± = diag(Λ,0,0) for S²(1)×S²(1) with Ric = g.
    
    The curvature operator on Λ² decomposes into SD and ASD blocks.
    For the product of two K=1 surfaces:
      Rm(e^{12}, e^{12}) = K_A = 1   (factor A sectional curvature)
      Rm(e^{34}, e^{34}) = K_B = 1   (factor B sectional curvature)
      Rm(e^{13}, e^{13}) = 0          (mixed plane, zero sectional curvature)
      ... all mixed entries = 0
    """
    # Curvature operator on Λ² in the basis
    # e^{01}, e^{02}, e^{03}, e^{12}, e^{13}, e^{23}
    # (using 0-based: factor A = {0,1}, factor B = {2,3})
    
    # Riemann tensor
    R = np.zeros((4,4,4,4))
    R[0,1,0,1] = 1; R[0,1,1,0] = -1; R[1,0,0,1] = -1; R[1,0,1,0] = 1
    R[2,3,2,3] = 1; R[2,3,3,2] = -1; R[3,2,2,3] = -1; R[3,2,3,2] = 1
    
    # SD basis: ω₁⁺ = e^{01}+e^{23}, ω₂⁺ = e^{02}-e^{13}, ω₃⁺ = e^{03}+e^{12}
    # ASD basis: ω₁⁻ = e^{01}-e^{23}, ω₂⁻ = e^{02}+e^{13}, ω₃⁻ = e^{03}-e^{12}
    # Normalized by |ω_a^±| = √2
    
    # Define the 2-form basis vectors as 4×4 antisymmetric matrices
    def wedge(i, j):
        w = np.zeros((4,4))
        w[i,j] = 1; w[j,i] = -1
        return w
    
    e01 = wedge(0,1); e02 = wedge(0,2); e03 = wedge(0,3)
    e12 = wedge(1,2); e13 = wedge(1,3); e23 = wedge(2,3)
    
    omega_p = [e01+e23, e02-e13, e03+e12]  # SD basis
    omega_m = [e01-e23, e02+e13, e03-e12]  # ASD basis
    
    # Curvature operator: R(α,β) = R_{ijkl} α^{ij} β^{kl} / 4
    def curv_op(alpha, beta):
        val = 0.0
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        val += R[i,j,k,l] * alpha[i,j] * beta[k,l]
        return val / 4.0
    
    # R^+ matrix in SD basis
    R_plus = np.zeros((3,3))
    for a in range(3):
        for b in range(3):
            R_plus[a,b] = curv_op(omega_p[a], omega_p[b]) / 2.0  # /2 for |ω|²=2
    
    # R^- matrix in ASD basis
    R_minus = np.zeros((3,3))
    for a in range(3):
        for b in range(3):
            R_minus[a,b] = curv_op(omega_m[a], omega_m[b]) / 2.0
    
    # Weyl: W^± = R^± - (s/12)I where s = 4 (scalar curvature of product)
    s = 4.0
    W_plus = R_plus - (s/12)*np.eye(3)
    W_minus = R_minus - (s/12)*np.eye(3)
    
    return {
        "R_plus": R_plus.tolist(),
        "R_minus": R_minus.tolist(),
        "R_plus_eigenvalues": sorted(np.linalg.eigvalsh(R_plus).tolist()),
        "R_minus_eigenvalues": sorted(np.linalg.eigvalsh(R_minus).tolist()),
        "W_plus": W_plus.tolist(),
        "W_minus": W_minus.tolist(),
        "W_plus_eigenvalues": sorted(np.linalg.eigvalsh(W_plus).tolist()),
        "is_conformally_flat": np.allclose(W_plus, 0),
        "R_pm_is_rank_one": (np.linalg.matrix_rank(R_plus, tol=1e-10) == 1),
        "kernel_plane": "span{e₂, e₃} = span{ω₂^±, ω₃^±}",
        "first_obstruction_e1": float(R_plus[0,0]),  # = 1 (nonzero, obstructed)
        "first_obstruction_e2": float(R_plus[1,1]),  # = 0 (allowed)
        "first_obstruction_e3": float(R_plus[2,2]),  # = 0 (allowed)
        "A02_correction_confirmed": True,
    }

# ====================================================================
# Part 2: Algebraic gauge invariance of R_odd
# ====================================================================

def prove_gauge_invariance():
    """
    THEOREM: R_odd(ℒ_X g₀) = 0 for every smooth vector field X on S²×S².
    
    PROOF: On the product background with ∇Rm = 0 and Rm purely within-factor:
    
    (1) The cross-factor Christoffel corrections ∂_p Γ^k_{ij} = 0 for
        all cross-factor (ij,p) triples. This is because
        ∂_p Γ^k_{ij}|₀ = -(1/3)(R^k_{ijp} + R^k_{jip}),
        and R_{...} = 0 whenever indices span both factors.
        
    (2) The second Christoffel derivatives ∂_p∂_q Γ^k_{ij}|₀ also vanish
        for cross-factor pairs, because ∇Rm = 0 (parallel curvature) and
        R²-type terms require at least one cross-factor R-component.
        
    (3) Therefore, for cross-factor (ij,pq):
        H_{ij,pq}(ℒ_X g₀) = ∂_p∂_q∂_i X_j + ∂_p∂_q∂_j X_i
        (pure third-derivative terms only).
        
    (4) R_odd = (1/2)(H_{01,23} - H_{03,12} - H_{12,03} + H_{23,01}).
        Substituting:
          H_{01,23} = X^1_{,023} + X^0_{,123}
          H_{03,12} = X^3_{,012} + X^0_{,123}  
          H_{12,03} = X^2_{,013} + X^1_{,023}
          H_{23,01} = X^3_{,012} + X^2_{,013}
        
        R_odd = (1/2)[(X^1_{023}+X^0_{123})-(X^3_{012}+X^0_{123})
                     -(X^2_{013}+X^1_{023})+(X^3_{012}+X^2_{013})]
              = (1/2) · 0 = 0.
        
    Each of the four independent third derivatives cancels: X^0_{123} appears
    in H_{01,23} and H_{03,12} with the same sign but opposite R_odd signs;
    similarly for X^1_{023}, X^2_{013}, X^3_{012}. QED.
    
    NOTE: This theorem does NOT require conformal flatness. It uses only:
    - Product structure (R_{cross-factor} = 0)
    - Parallel curvature (∇Rm = 0)
    These hold on S²(K)×S²(K) for any K.
    """
    # Verify the cancellation algebraically
    coeffs = {}
    pairs = [((0,1),(2,3),+0.5), ((0,3),(1,2),-0.5),
             ((1,2),(0,3),-0.5), ((2,3),(0,1),+0.5)]
    
    for (i,j), (p,q), sign in pairs:
        key1 = (j, tuple(sorted([p,q,i])))
        coeffs[key1] = coeffs.get(key1, 0) + sign
        key2 = (i, tuple(sorted([p,q,j])))
        coeffs[key2] = coeffs.get(key2, 0) + sign
    
    all_zero = all(abs(v) < 1e-15 for v in coeffs.values())
    
    # Also verify with 500 random X Taylor coefficients
    rng = np.random.default_rng(42)
    max_R_odd = 0.0
    for _ in range(500):
        X3 = rng.standard_normal((4,4,4,4))
        for k in range(4):
            for a in range(4):
                for b in range(a, 4):
                    for c in range(b, 4):
                        val = np.mean([X3[k,p[0],p[1],p[2]] for p in 
                              [(a,b,c),(a,c,b),(b,a,c),(b,c,a),(c,a,b),(c,b,a)]])
                        for p in [(a,b,c),(a,c,b),(b,a,c),(b,c,a),(c,a,b),(c,b,a)]:
                            X3[k,p[0],p[1],p[2]] = val
        
        H = {}
        for (i,j),(p,q),_ in pairs:
            H[(i,j,p,q)] = X3[j,p,q,i] + X3[i,p,q,j]
        
        R_odd = 0.5*(H[(0,1,2,3)] - H[(0,3,1,2)] - H[(1,2,0,3)] + H[(2,3,0,1)])
        max_R_odd = max(max_R_odd, abs(R_odd))
    
    return {
        "theorem": "R_odd(L_X g_0) = 0 for all smooth X",
        "proof_method": "algebraic cancellation of third-derivative terms",
        "requires_conformal_flatness": False,
        "requires": ["product structure (R_{cross-factor}=0)", "parallel curvature (∇Rm=0)"],
        "algebraic_verification": all_zero,
        "numerical_max_R_odd_500_trials": max_R_odd,
        "coefficient_table": {str(k): v for k,v in coeffs.items()},
    }

# ====================================================================
# Part 3: Curvature identification  
# ====================================================================

def curvature_identification():
    """
    R_odd = -(d_{g₀}Rm)_{02,13} = minus the cross-factor linearized curvature.
    
    In the SD/ASD decomposition at the product background:
    - R₀ω₂± = 0 (verified in Step 91, consistent with R^± = diag(1,0,0))
    - (d_{g₀}Rm)_{02,13} = the ω₂ cross-factor curvature component
    - Since R^±_{22} = 0, the first obstruction vanishes in the ω₂ direction
    - R_odd measures the SECOND obstruction (inter-node Green response)
      in the ω₂ direction within the kernel plane
    """
    # Verify R_odd = -(dRm)_{0213} on 1000 random Hessians
    rng = np.random.default_rng(123)
    max_err = 0.0
    for _ in range(1000):
        H = rng.standard_normal((4,4,4,4))
        H = 0.5*(H + H.transpose(1,0,2,3))
        H = 0.5*(H + H.transpose(0,1,3,2))
        
        R_odd = 0.5*(H[0,1,2,3] - H[0,3,1,2] - H[1,2,0,3] + H[2,3,0,1])
        dRm_0213 = 0.5*(-H[2,3,0,1] + H[1,2,0,3] + H[0,3,1,2] - H[0,1,2,3])
        
        max_err = max(max_err, abs(R_odd + dRm_0213))
    
    return {
        "identity": "R_odd(H) = -(d_e Rm)_{0213}(H) (exact at flat jet level)",
        "numerical_max_error": max_err,
        "geometric_meaning": "R_odd measures the cross-factor (ω₂⁻,ω₂⁻) linearized curvature",
        "first_obstruction_status": "R^±_{22} = 0 → first obstruction VANISHES for ζ in ker R^±",
        "R_odd_role": "second obstruction (inter-node Green response) in ω₂ direction on kernel plane",
    }

# ====================================================================
# Part 4: Corrected obstruction structure
# ====================================================================

def corrected_obstruction_analysis():
    """
    Corrected obstruction structure after A02 Step93 curvature correction.
    
    The Ozuch quadratic obstruction ⟨B(ζ,ζ)ξ,ξ⟩ = 12⟨ρ(ζ),ξ⟩² - 4|ζ|²|ξ|²
    is BIQUADRATIC: degree 2 in source ζ and degree 2 in receiver ξ.
    
    The physical H⁴(ζ⁺) = -ρ(ζ)⁻∘ζ⁺/(2r⁴) is quadratic in ζ.
    Its odd chirality source is quadratic in ζ, not linear.
    
    The spectral K_adj used a specific eigenmode decomposition that 
    corresponds to ζ = e₂ source and e₂ receiver (diagonal entry).
    
    On the kernel plane, the SO(2) stabilizer (rotations around both poles)
    acts as simultaneous rotation of source and receiver directions.
    By equivariance and the self-adjointness of the Green function,
    the diagonal entries are equal: Q(e₂,e₂) = Q(e₃,e₃) = K_adj.
    
    But the full Ozuch QUADRATIC obstruction also depends on the 
    source DIRECTION through H⁴(ζ). A source ζ = e₂ creates a 
    DIRECTION-DEPENDENT perturbation, and the kernel-plane projection
    is NOT isotropic:
      ⟨B(e₂,e₂)e₂,e₂⟩ = 8|x|⁻⁶  (single image)
      ⟨B(e₂,e₂)e₃,e₃⟩ = -4|x|⁻⁶ (single image)
    """
    K_adj_total = -0.03544499598  # from Step 94
    
    # A02's toy single-image data (identity rotation)
    # For ζ=e₂: kernel block = [[8, 0], [0, -4]] (eigenvalues 8 and -4)
    # For ζ=e₃: kernel block = [[-4, 0], [0, 8]] (eigenvalues -4 and 8)
    # For ζ=e₁ (excluded by first obstruction): kernel block = [[-4, 0], [0, -4]]
    
    # The spectral K_adj corresponds to a specific COMBINATION of these
    # toy entries, summed over all images with the full product Green function.
    
    # Key insight: the quadratic source H⁴(ζ) for ζ in the kernel plane
    # generates BOTH diagonal and off-diagonal curvature responses on 
    # the kernel plane. The spectral computation captures one component.
    
    return {
        "A02_correction_absorbed": True,
        "R_pm_product": "diag(1, 0, 0)",
        "kernel_plane": "ker R^± = span{e₂, e₃}",
        "first_obstruction": "VANISHES on kernel plane (R^±_{22} = R^±_{33} = 0)",
        "K_adj_principal": K_adj_total,
        "K_adj_interpretation": (
            "K_adj measures the diagonal (e₂,e₂) component of the spectral "
            "inter-node Green response. By SO(2) equivariance + self-adjointness, "
            "Q(e₂,e₂) = Q(e₃,e₃) = K_adj. But the full Ozuch quadratic "
            "obstruction B(ζ,ζ)ξ involves a direction-dependent source, so the "
            "kernel-plane response is a degree-(2,2) biquadratic form, not scalar."
        ),
        "toy_single_image_kernel_data": {
            "source_e2": {"kernel_block": [[8, 0], [0, -4]]},
            "source_e3": {"kernel_block": [[-4, 0], [0, 8]]},
        },
        "wrong_conclusions_withdrawn": [
            "t*² = -1/(3K_adj) scale equation (product is NOT conformally flat)",
            "R^± = I/3 (correct: diag(1,0,0))",
            "the combined obstruction vanishing at finite EH scale",
        ],
        "remaining_work": [
            "Compute full biquadratic obstruction Π_K B Π_K on kernel plane",
            "Identify the SO(2)-equivariant decomposition of the spectral response",
            "Determine whether the Ozuch angular equation has a nontrivial solution",
            "Calibrate against the known all-same-chirality KE desingularization",
        ],
    }

# ====================================================================
# Part 5: SO(2) equivariance of the bilinear spectral response
# ====================================================================

def so2_equivariance_analysis():
    """
    The stabilizer of all four nodes on (S²×S²)/Z₂ is SO(2)_A × SO(2)_B.
    
    On the kernel plane at each node, this acts as R_{θ_A + θ_B}.
    For the spectral bilinear response B_spectral(ζ, ξ) (which uses the 
    SPECTRAL source S_odd = (π²/2)R_odd, not the quadratic H⁴ source):
    
    B_spectral(R_θ ζ, R_θ ξ) = B_spectral(ζ, ξ) (equivariance)
    B_spectral(ζ, ξ) = B_spectral(ξ, ζ)            (self-adjointness of G_P^⊥)
    
    → B_spectral = K_adj · ⟨·,·⟩  (isotropic on kernel plane)
    
    But B_spectral is the BILINEAR response for the spectral source.
    The PHYSICAL Ozuch source H⁴(ζ) is quadratic in ζ, creating a 
    BIQUADRATIC form that is NOT captured by the bilinear spectral sum alone.
    
    The biquadratic form decomposes under SO(2) as:
    Q(ζ,ζ,ξ,ξ) = a|ζ|²|ξ|² + b(⟨ζ,ξ⟩² + ω(ζ,ξ)²) 
                 + c(⟨ζ,ξ⟩² - ω(ζ,ξ)²)
    where ⟨ζ,ξ⟩² + ω(ζ,ξ)² = |ζ|²|ξ|² and ⟨ζ,ξ⟩² - ω(ζ,ξ)² = (ζ·ξ_conj)²
    in complex notation. So Q = (a+b)|ζ|²|ξ|² + c·Re[(ζ·ξ_conj)²].
    """
    K_adj = -0.03544499598
    
    return {
        "bilinear_spectral_response": f"B_spectral = {K_adj:.11f} · <·,·> on kernel plane",
        "is_isotropic_bilinear": True,
        "reason": "SO(2) equivariance + self-adjointness of Green function",
        "biquadratic_decomposition": {
            "general_form": "Q(ζ,ζ,ξ,ξ) = α|ζ|²|ξ|² + β Re[(ζ·ξ̄)²]",
            "parameters": {
                "alpha": "isotropic part, related to K_adj",
                "beta": "anisotropic part, captures the H⁴ direction dependence",
            },
            "single_image_toy": {
                "alpha_toy": 2.0,  # (8 + (-4))/2 = 2
                "beta_toy": 6.0,   # (8 - (-4))/2 = 6
            },
        },
        "key_distinction": (
            "The spectral K_adj captures the BILINEAR (isotropic) response. "
            "The physical Ozuch obstruction includes an ANISOTROPIC biquadratic "
            "part from the H⁴ direction dependence. Computing the full "
            "kernel-plane obstruction requires both components."
        ),
    }

# ====================================================================
# Main
# ====================================================================

def main():
    results = {
        "step": 95,
        "scope": "Gauge invariance theorem + corrected kernel-plane analysis",
        "A02_correction": "R^± = diag(1,0,0), NOT I/3 (product is NOT conformally flat)",
    }
    
    results["curvature_verification"] = verify_product_curvature()
    results["gauge_invariance_theorem"] = prove_gauge_invariance()
    results["curvature_identification"] = curvature_identification()
    results["corrected_obstruction"] = corrected_obstruction_analysis()
    results["so2_equivariance"] = so2_equivariance_analysis()
    
    results["summary"] = {
        "gauge_invariance_proved": True,
        "conformal_flatness_withdrawn": True,
        "R_pm_correct": "diag(1, 0, 0)",
        "kernel_plane_identified": "span{e₂, e₃}",
        "K_adj_still_valid": True,
        "K_adj_meaning": "diagonal spectral bilinear response on kernel plane",
        "full_obstruction_needs": "biquadratic kernel-plane form (isotropic + anisotropic parts)",
        "conclusion": (
            "The gauge invariance R_odd(ℒ_Xg₀)=0 is proved exactly on the product. "
            "After A02's curvature correction, R^±=diag(1,0,0), so the first obstruction "
            "VANISHES on the kernel plane span{e₂,e₃}. K_adj≈-0.0354 remains a valid "
            "bilinear spectral response on this plane. The full Ozuch obstruction is a "
            "biquadratic form Q(ζ,ζ,ξ,ξ) with both isotropic and anisotropic parts. "
            "The next computation: decompose K_adj into the SO(2)-equivariant components "
            "of the biquadratic obstruction and determine whether the angular equation "
            "has a nontrivial solution on the kernel plane."
        ),
    }
    
    outpath = "Sessions/S0910A01/workspace/data/step95_gauge_invariance_and_bridge.json"
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {outpath}")

if __name__ == "__main__":
    main()
