# Step 53 — The trace-free-Ricci compatibility of the perpendicular Burns tail is conformal–diffeomorphism covariance plus harmonicity

Session S1003A01, Agent2. Inputs: Spirit #62 (candidate formula), Step 50 (W⁻ corrector), Step 52 (Theorem 52.A, `step52_kernel_insertion_theorem.md`).
Script: `workspace/scripts/step53_ric0_geometric_corrector.py`; output `workspace/data/step53/ric0_geometric_corrector.json`, log `ric0_geo_log.txt`.

## Setting
Flat chart ℝ⁴∖0, ζ = J = J₃, Burns g_ε = δ + εk_B, k_B = (v₀v₀ᵀ+v₁v₁ᵀ)/u², v_m = J_m x, u = |x|². The Burns metric is exactly ASD and scalar-flat: W⁺(g_ε) = 0 and s(g_ε) = 0 for every ε.
For E trace-free symmetric, q = xᵀEx, E_H = (E + JᵀEJ)/2, q_H = xᵀE_Hx. The pure-Ric° normal 2-jet is
 h_E = −(1/6)(E u + q δ − Ex xᵀ − x (Ex)ᵀ)  (Kulkarni–Nomizu ½E∧δ, h_E x = 0).

## Lemma 53.1 (geometric Ric° corrector)
With f = −q/4, V = −uEx/12 + qx/6, f_ε = f − ε q_H/(8u), and
 k₀^E = L_V k_B − (q/2) k_B − (q_H/(4u)) δ,
the following hold identically on ℝ⁴∖0:
 W⁺''_δ(h_E,k_B) + W⁺'_δ(k₀^E) = 0,  s''_δ(h_E,k_B) + s'_δ(k₀^E) = 0.
k₀^E is homogeneous of degree 0, so it belongs to the same corrector class as the Step-50 W⁻ corrector k₀^W.

Proof. (i) Exactly h_E = 2fδ + L_Vδ (checked symbolically). (ii) Consider G_t = φ_t^*(e^{2tf_ε}g_ε) with φ_t the flow of V. W⁺ is conformally covariant and natural, so W⁺(G_t) = 0 for all t. In dimension four s(e^{2u}g) = e^{−2u}(s − 6Δu − 6|du|²), hence d/dt|₀ s(G_t) = −6Δ_{g_ε}f_ε (s(g_ε) = 0). (iii) f_ε is g_ε-harmonic to first order in ε: Δ_δ f = −½ tr E = 0, and the ε-coefficient −k_B^{ij}∂_{ij}f − (div k_B − ½d tr k_B)·df + Δ_δ(−q_H/(8u)) vanishes identically (checked exactly; the same expression for the uncorrected f is nonzero). (iv) Therefore DW⁺_{g_ε}[L_Vg_ε + 2f_εg_ε] = 0 and Ds_{g_ε}[L_Vg_ε + 2f_εg_ε] = O(ε²). The ε⁰ coefficient is the statement W⁺'(h_E) = s'(h_E) = 0 (pure Ric° jet). The ε¹ coefficient is D²(W⁺,s)_δ[k_B,h_E] + D(W⁺,s)_δ[L_Vk_B + 2fk_B + 2f₁δ] = 0 with f₁ = −q_H/(8u), which is the lemma. Vanishing of W⁺ is frame independent, so the orthonormal-frame expansion used by the curvature engine vanishes order by order. ∎

Independent exact check (curvature engine of `step52_ric0_corrector.py`, two unrelated E, all 7 components (6 of W⁺, 1 of s) at 5 random rational points each): all zero; the uncorrected source is nonzero. Control: dropping the q_H term leaves all W⁺ components zero and only the scalar component nonzero (12/1285, …), exactly as conformal covariance predicts.

## Meaning
- The Ric° coefficient of the logarithmic Burns corner term vanishes because the Ric° jet is pure gauge-plus-conformal at the 2-jet level (h_E = L_Vδ + 2fδ), and Burns admits the conformal continuation f_ε. The ε²log(1/ε) cross term between Ric°_p and Burns is a completed square with zero minimum, just as for W⁻. The floating least-squares solutions of Step 52 (rank 12 in a 17-tensor span) were non-unique because of this gauge/conformal redundancy; the rationalized coefficients were spurious.
- Together with Step 50 (W⁻) and Step 52 (exact (s,W⁺) sector), the formal corner coefficient at any point of any metric, in the CGB form 4|W⁺|²+s²/12, is
 F = −μ_ζ(μ_ζ − s/8) − |T|²  (ζ an R⁺-eigenvector),
 with no W⁻ or Ric° contribution. The Gauss–Bonnet/signature reduction P = 2∫(2|W⁺|² + s²/24) − const holds for every metric, so the corner computation itself needs no Einstein hypothesis.
- What still differs for non-Einstein (e.g. P-critical) bulk is not the corner coefficient but (a) the order-ε bulk variation DP_g[χk], absent only when g is P-critical; (b) whether higher jets still enter only through exact forms (proved via Einstein in Step 50). A02's Part A (P-critical remainder) is the place where (a)–(b) are handled; Lemma 52.C (no open degenerate stratum) still requires δW⁺ = 0 and does not transfer.
