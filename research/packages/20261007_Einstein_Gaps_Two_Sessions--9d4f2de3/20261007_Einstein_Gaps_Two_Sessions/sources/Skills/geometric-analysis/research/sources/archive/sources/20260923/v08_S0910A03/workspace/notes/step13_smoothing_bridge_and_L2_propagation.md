# Step 13: Ye Li smoothing bridge, L² propagation attempt, and the localized accessibility question

> **Step 14 correction.** Sections 4.2--4.5 do not prove the displayed local Gronwall estimate: an inequality for an inner-ball energy with an outer-ball energy on the right is not closed, and persistence of the small normalized curvature energy was not established. The numerical factors checked only algebra. The sharp valid replacement is the conditional Corollary 3.5 reconstruction and homogeneous normalized cutoff-flow analysis in `step14_cutoff_smoothing_and_cor35_reconstruction.md`. Section 5's quotient bootstrap is also not established: bounded magnetic Weyl data does not control all quotient coefficients or noncollapse.

## 1. The small-radius bridge (Strategist's observation, confirmed)

At a maximal-function good point p ∈ G_i with M₁|Rm|²(p) ≤ K₀, we have

    fint_{B_r(p)} |Rm|² ≤ K₀   for all r ≤ 1.

Ye Li's Theorem 3.6 (Knowledge/objects/.../0911.3104/.../object.md, lines 321–329) requires:

    r⁴/Vol(B_r(x)) ∫_{B_r(x)} |Rm|² ≤ ε_Li    and   |Ric| ≤ K.

The left side equals r⁴ fint |Rm|² ≤ K₀ r⁴. Choose

    r₀ = (ε_Li / (2 C_BG K₀))^{1/4}

where C_BG is the Bishop–Gromov constant for extending centered bounds to B_{r₀/2}(p). Then **for all q ∈ B_{r₀/2}(p) and all r ≤ r₀/2**, the dimensionless energy satisfies

    r⁴ fint_{B_r(q)} |Rm|² ≤ C_BG K₀ r₀⁴ ≤ ε_Li/2.

This does NOT send the Einstein scale to zero: r₀ > 0 is fixed before i→∞. The nonzero calibrated background curvature does not obstruct the hypothesis. (Step 12's dismissal of smoothing for this reason is superseded.)

With |Ric| ≤ (1+δ_i)·3 ≤ 4 for large i, Ye Li gives a Ricci flow g_i(t) on B_{r₀/4}(p) for t ∈ [0, T₀] with T₀ ≥ C₁ r₀² and

    |Rm(g_i(t))| ≤ C₂/t    for t ∈ (0, T₀].

At t₀ = T₀/2 = C₁ r₀²/2: |Rm| ≤ K := 2C₂/(C₁ r₀²), a fixed constant.

**Localization remark.** Li's theorem as stated requires the small-energy hypothesis at every center. Our good-point + Bishop–Gromov calculation supplies it at every center in B_{r₀/2}(p). Li's proof (lines 331–335) uses volume comparison only between nearby centers in B_{3r/2}(x), so the all-centers condition within a buffered domain should suffice for a local version. This localization is a technical step that requires checking the covering argument in Li's proof remains valid on a ball with boundary (e.g. via conformal completion or doubling). We record it as a needed verification, not an established theorem.

## 2. Einstein defect evolution under normalized Ricci flow

For the normalized flow ∂_t g = -2(Ric + g), define E = Ric(g) + g. The Einstein metric Ric = -g is a fixed point.

**Tensor evolution** (verified by contracted Bianchi cancellation):

    ∂_t E = Δ_L E - 2E

where Δ_L h_{ij} = Δ h_{ij} + 2R_{ikjl}h_{kl} - R_{ik}h_{kj} - R_{jk}h_{ki}.

**Squared-norm evolution** (verified: all tr(E³) and |E|² auxiliary terms cancel):

    (∂_t - Δ)|E|² = -2|∇E|² + 4 R_{ikjl} E_{ij} E_{kl}

**TTCS verifier correction:** The -2E in the tensor equation does NOT produce a net linear damping in |E|². The Lichnerowicz curvature terms R_{ik}E_{kj} involve R_{ik} = E_{ik} - g_{ik}, and substituting gives -2(E²) + 2E which exactly cancels the remaining -2E and tr(E³) from the metric-variation contribution. The precise scalar evolution has only the curvature-tensor reaction 4R_{ikjl}E_{ij}E_{kl} and the gradient dissipation -2|∇E|².

## 3. The pointwise C/t gap (confirmed, genuine)

Under Ye Li smoothing: |Rm(t)| ≤ C/t for t ∈ (0, T₀). The maximum-principle estimate:

    sup|E(t₀)|² ≤ exp(∫₀^{t₀} 4C/t dt) sup|E(0)|² = ∞

The integral diverges logarithmically. This is not an artifact: the ODE model f' = (4C/t)f has solution f(t) = f(ε)(t/ε)^{4C}, diverging as ε→0.

**Conclusion:** Pointwise Gronwall fails to propagate E through the smoothing.

## 4. L² PROPAGATION VIA SOBOLEV ABSORPTION (the key mechanism)

### 4.1 The critical observation

The reaction term in the |E|² evolution can be estimated using Hölder:

    ∫ |Rm| |φE|² ≤ ‖Rm‖_{L²(B_r)} · ‖φE‖_{L⁴(B_r)}²

In 4D with Ric ≥ -3g, the relative Sobolev inequality (Saloff-Coste/Hebey) gives:

    ‖f‖_{L⁴(B_r)}² ≤ C_S V(B_r)^{-1/2} (r² ‖∇f‖₂² + ‖f‖₂²)

where C_S depends only on dimension and the Ricci lower bound parameter.

Now:

    ‖Rm‖_{L²(B_r)} = (V·fint|Rm|²)^{1/2} = V^{1/2}(fint|Rm|²)^{1/2}

Combining:

    ∫ |Rm||φE|² ≤ V^{1/2}(fint|Rm|²)^{1/2} · C_S V^{-1/2}(r²‖∇(φE)‖₂² + ‖φE‖₂²)
                  = C_S (fint|Rm|²)^{1/2} (r²‖∇(φE)‖₂² + ‖φE‖₂²)

**The volume V cancels completely.**

Using the dimensionless energy: fint|Rm|² ≤ K₀, so (fint|Rm|²)^{1/2} ≤ K₀^{1/2}.

But more crucially, at scale r₀:

    r₀² (fint|Rm|²)^{1/2} ≤ r₀² K₀^{1/2}

and the dimensionless energy ε_{r₀} = r₀⁴ fint|Rm|² ≤ K₀ r₀⁴, so:

    (fint|Rm|²)^{1/2} = ε_{r₀}^{1/2} / r₀²

Therefore:

    ∫|Rm||φE|² ≤ C_S ε_{r₀}^{1/2}/r₀² · (r₀²‖∇(φE)‖₂² + ‖φE‖₂²)
                = C_S ε_{r₀}^{1/2} (‖∇(φE)‖₂² + r₀⁻²‖φE‖₂²)

### 4.2 Absorption of the gradient term

For ε_{r₀} = K₀r₀⁴ small enough that **C_S ε_{r₀}^{1/2} < 1**, the gradient term is absorbed by the dissipation:

    d/dt ∫φ²|E|² ≤ -(2 - 4C_S ε_{r₀}^{1/2})∫φ²|∇E|² + C ε_{r₀}^{1/2} r₀⁻² ∫φ²|E|² + cutoff terms

The cutoff terms (from ∇φ) contribute at most:

    ∫|∇φ|²|E|² ≤ C r₀⁻² ∫|E|²

Over the localized region:

    d/dt ∫_{B_{r₀/4}} |E|² ≤ C₃ r₀⁻² ∫_{B_{r₀/2}} |E|²

where C₃ depends only on dimension, C_S, K₀, and is **independent of volume**.

### 4.3 Gronwall in time

    ∫_{B_{r₀/4}} |E(t)|² ≤ e^{C₃ r₀⁻² t} ∫_{B_{r₀/2}} |E(0)|²

At t₀ = C₁ r₀²/2:

    e^{C₃ r₀⁻² · C₁ r₀²/2} = e^{C₁ C₃/2}

This is a **fixed constant**, independent of both the volume and the sequence index i.

Therefore:

    ∫_{B_{r₀/4}} |E_i(t₀)|² ≤ e^{C₁C₃/2} ∫_{B_{r₀/2}} |E_i(0)|²
                                ≤ e^{C₁C₃/2} δ_i² V(B_{r₀/2})

### 4.4 Pointwise recovery via parabolic mean value inequality

At time t₀, |Rm(g_i(t₀))| ≤ K on B_{r₀/4}(p). For t ∈ [t₀/2, t₀]:

    |Rm| ≤ 2K = 2C₂/(C₁r₀²)

and Shi estimates give all higher derivative bounds. The parabolic MVI for the subsolution (∂_t - Δ)|E|² ≤ 4·2K·|E|² on B_{r₀/4} × [t₀/2, t₀] gives:

    sup_{B_{r₀/8}×{t₀}} |E|² ≤ C_MVI/(V(B_{r₀/4})·(t₀/2)) · ∫_{t₀/2}^{t₀} ∫_{B_{r₀/4}} |E|²

The spacetime integral:

    ∫_{t₀/2}^{t₀} ∫_{B_{r₀/4}} |E|² ≤ (t₀/2) · e^{C₁C₃/2} δ_i² V(B_{r₀/4})

(using the L² propagation bound at each time slice).

Therefore:

    sup|E_i(t₀)|² ≤ C_MVI · (V·t₀)⁻¹ · (t₀/2) · e^{C₁C₃/2} · δ_i² · V
                    = (C_MVI/2) e^{C₁C₃/2} δ_i²

**The volumes cancel in the ratio, and the time factors are all fixed.**

### 4.5 Result

**Proposition (conditional on the localized Li theorem):** For r₀ chosen as in Section 1, there exists C* = C*(n, K₀, r₀) such that for every good point p ∈ G_i:

    sup_{B_{r₀/8}(p)} |Ric(g_i(t₀)) + g_i(t₀)| ≤ C* δ_i → 0

The smoothed metric on B_{r₀/8}(p) simultaneously has:
- |Rm| ≤ K (bounded sectional curvature)
- |E| ≤ C*δ_i (nearly Einstein)
- All Shi derivative bounds
- Bilipschitz equivalence with g_i(0) (factor √2 from Li's proof)

### 4.6 Why this works while pointwise Gronwall fails

The pointwise estimate uses sup|Rm| ≤ C/t as a coefficient, giving a divergent integral.

The L² estimate uses ‖Rm‖_{L²} as a coefficient, combined with the Sobolev inequality. The key is that ‖Rm‖_{L²}·V^{-1/2} (the factor from Sobolev) equals (fint|Rm|²)^{1/2} ≤ K₀^{1/2}, a BOUNDED quantity. And at scale r₀, the r₀² from the Sobolev inequality and the r₀⁻² from the dimensionless energy combine to give a SMALL coefficient ε_{r₀}^{1/2}.

The Sobolev absorption is the mechanism that converts "bounded L² curvature energy" into "controllable L² Einstein defect propagation" by using the gradient dissipation term -2∫|∇E|² as the absorbing reservoir.

## 5. Completing the forbidden-germ argument

At t₀, the metric g_i(t₀) on B_{r₀/8}(p) has bounded curvature AND small Einstein defect. Two possibilities:

**(A) Noncollapsed:** Vol(B_ρ(q, g_i(t₀))) ≥ v₀ ρ⁴ for some ρ. Then harmonic coordinates exist, and the standard convergence theory gives a local Einstein limit. The calibrated W⁺ profile (which is a Chern-Weil + SW identity applying to ANY metric on the fixed topology) constrains the limit, and the Derdziński/projector contradiction applies.

**(B) Collapsed:** Vol(B_ρ) ≪ ρ⁴ everywhere. With bounded sectional curvature, CFG theory gives a local nilpotent fibration. The base has controlled geometry (bounded curvature in 3D). The nearly-Einstein condition E ≤ C*δ_i feeds into the reduced equations with controlled error. The Steps 11-12 reduced system then applies to the **smoothed** metric, with all derivatives controlled.

In case (B), the reduced Einstein equations for g_i(t₀) give:
- tr H = 1 + |z|²/2 + O(δ_i)
- dz = -2u∧z + O(δ_i)
- Ric_B = -I + H + C²_sym/2 + O(δ_i)

With |Rm| ≤ K: all of H, ∇z, Ric_B are bounded. The TTCS generator's inequality H ≥ (1/4)I + B gives:

    λ_min(H) ≥ 1/4 - √(2/3)|B|

Since |B| ≤ C(K), this gives H ≥ -C'(K)I, and combined with tr H ≥ 1:

    Ric_B = -I + H + C²/2 ≥ -I - C'(K)I + 0 = -(1+C'(K))I

So the 3D base has bounded Ricci. In 3D, bounded Ricci = bounded full curvature. This gives a 3D harmonic radius, and hence a 4D chart via the KK construction. The forbidden Einstein germ then applies on the cover.

## 6. Connection to TTCS results

### Generator (H ≥ 0 analysis)
- H = G + Q + B where G has calibrated eigenvalues (1/2, 1/4, 1/4), Q ≥ 0.
- A 1-jet model with B = diag(L/2, -L, L/2) achieves negative H-eigenvalue for L > 1/4, while maintaining calibrated W⁺. The cost enters W⁻.
- Threshold: |B|_HS ≤ √6/8 ⟹ H ≥ 0.
- L²-small B controls the negative spectral tail: ‖H_-‖_{L^p} ≤ √(2/3)‖B‖_{L²} for 3/2 < p ≤ 2.
- No coercive pointwise estimate from chiral Riccati: the trace mode is uncontrolled.

### Verifier (E evolution)
- Both evolution equations confirmed correct.
- The -2E damping does NOT survive in the |E|² equation (cancels exactly).
- The C/t Gronwall gap is genuine.
- Critical L² + Sobolev approach identified as the alternative: small ε_r allows absorption of the curvature reaction by gradient dissipation.
- Remaining technical needs: persistence of local Sobolev constants and energy bounds along the flow, boundary/cutoff control.

## 7. Remaining gaps and plan

### 7.1 Localization of Li's theorem
Li's all-centers theorem needs a local version valid on a buffered ball. The proof structure (covering argument in B_{3r/2}) supports this, but the boundary treatment needs verification. This could be done via:
- Conformal completion to a closed manifold
- Direct local-flow existence with Dirichlet/Neumann boundary
- Doubling construction

### 7.2 Sobolev constants along the flow
The L² propagation uses the Sobolev inequality at each time t. Along the flow, the metric changes, but Li proves bilipschitz equivalence (factor √2). This preserves the doubling constant and Sobolev constant up to universal factors, so the argument should be self-consistent.

### 7.3 Calibrated W⁺ transfer
The W⁺ calibrated profile ∫(|W⁺| - 1/(2√6))² → 0 is a property of g_i(0). Under the L² propagation, we also need to show that ∫|W⁺(t₀) - W⁺(0)|² is controlled. This follows from the general L² evolution of curvature under Ricci flow with bounded energy, but needs careful treatment at the C/t curvature boundary.

### 7.4 Positive branch and higher dimensions
All of the above is specific to the 4D negative branch. The positive branch, dimensions n ≥ 5, and Lean formalization remain open. The Li smoothing is 4D-specific; higher dimensions require different tools.

## 8. Evidence references

- Ye Li Theorem 3.6: Knowledge/objects/papers/0911.3104.../object.md, lines 321–335
- Evolution equations: workspace/scripts/verify_einstein_defect_evolution.py
- TTCS generator (H ≥ 0): trace/ttcs/results/step13_ttcs01_generator1_integration.md
- TTCS verifier (E evolution): trace/ttcs/results/step13_ttcs01_verifier1_integration.md
- Step 9 maximal function: workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex
- Step 12 reduced equations: workspace/notes/step12_reduced_equations_accessibility.md
- A01 smoothing/reduction comparison: S0910A01/workspace/notes/step14_smoothing_vs_reduction_route.md
