# TTCS Independent Branch Record

```json
{
  "step_id": 55,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md",
    "Sessions/S0910A01/workspace/data/step55_finite_restart_threshold_verify.json",
    "Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md",
    "Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md"
  ]
}
```

## Task

Verify the Step 55 finite restart threshold and next cutoff-jet exchange. Read the new finite-restart note plus A03 Step56 base pair and Step57 H2/continuation note. Focus on the actual mathematics of the positive-time collar continuation: starting from T,T1,U1,C2 in all finite Lp and |T|_infty, does the derivation of the (U2,C3) estimate correctly handle the dangerous chi*C4*U term and the evolution partial_t C3 ~ C1*U2? Are the Hölder exponents and weighted Sobolev absorption in I31 valid for p>=2? Is the claimed finite restart package through (U_s0,C_{s0+1}) and T_0..T_{s0-1} sufficient to obtain fixed-background H^{s0} restart data via A=∇^{g(t)}-∇bar? Identify any false term, missing counterterm, or weaker assumption needed. Do not review the whole Yau 26 route; only this finite continuation bridge.

## Output

# Verification Memo: Step 55 finite restart threshold and the (U₂,C₃) exchange

## Overall

The core analytical content of Step 55 — the integration-by-parts treatment of the top cutoff jet χC₄∗U, the Hölder/weighted-Sobolev absorption of the genuine counterterm I₃₁, the evolution ∂ₜC₃ ~ C₁∗U₂, and the coupled Grönwall (2.22) — is mathematically correct as written for p ≥ 2 in dimension four. The finite package (1.5)–(1.6) and the fixed-background A-system route to H^{s₀} data are structurally sound. Below I record the term-level checks, one place where the note's wording under-describes a principal term (repairable, and in fact already correct once read as divergence form), and the external dependencies the sufficiency rests on.

## 1. The χC₄∗U integration by parts (2.4)–(2.7) — correct

C₄ = ∇C₃ is an exact tensor identity (∇⁴χ = ∇(∇³χ)); the parenthetical "+ connection contractions" in the note is spurious but harmless, since no correction term arises. Moving ∇ off C₃ and applying Leibniz to (|U₂|^{p−2}U₂ · χ · U) reproduces exactly the three lines of (2.5):

- diffusive line → ε D₂,ₚ^U + C(‖C₃‖ₚ^p + ‖U₂‖ₚ^p + 1), using |U|≤K and the split χ|U₂|^{(p−2)/2}|∇U₂| · |U₂|^{(p−2)/2}|C₃| with a=χ² inside D. Verified (2.6). ✓
- middle line → same-exponent Young with C₁, U bounded. Verified (2.7). ✓
- I₃₁ = ∫ χ|C₃||U₁||U₂|^{p−1}: the true next-exchange term.

## 2. The counterterm I₃₁ (2.8)–(2.13) — correct, and the exponent algebra checks

Writing the integrand as f·|C₃|·|U₁|·|U₂|^{p/2−1} with f = χ|U₂|^{p/2}, the Hölder tuple (4, p, 4, 2p/(p−2)) satisfies Σ1/qⱼ = 1, and the last factor evaluates to ‖U₂‖ₚ^{p/2−1} because (p/2−1)·2p/(p−2) = p exactly. This reproduces (2.10). The p=2 degeneration to (4,2,4) with the last factor absent is correct.

The weighted Sobolev bound (2.11) is valid **specifically because n = 4**: 2\* = 2n/(n−2) = 4, so W^{1,2} ↪ L⁴ gives ‖f‖₄² ≤ C_S‖f‖_{W^{1,2}}². Expanding ∇f = (∇χ)|U₂|^{p/2} + (p/2)χ|U₂|^{p/2−1}∇|U₂| and using Kato (|∇|U₂|| ≤ |∇U₂|) yields the stated p²D₂,ₚ^U + C(p,r)‖U₂‖ₚ^p structure, including the correct O(p²) growth of the diffusive coefficient. ✓ Young-absorbing ‖f‖₄ then gives (2.12), and the final ‖C₃‖ₚ²‖U₂‖ₚ^{p−2} ≤ C(1+‖C₃‖ₚ^p+‖U₂‖ₚ^p) is Young with exponents (p/2, p/(p−2)). Verified (2.13). The JSON Hölder table (inverse sums = 1 for p = 3,4,8,16) is arithmetically correct.

The essential structural fact is confirmed: I₃₁ uses **only the fixed base datum U₁ ∈ L⁴**, never a growing curvature requirement. This is what makes the whole induction closable at finite order rather than propagating a rising demand.

## 3. Evolution of C₃ (2.15)–(2.21) — correct

Since χ is a fixed scalar, C₁ = dχ is time-independent while C₂, C₃ evolve through the connection. The chain ∂ₜ(∇²χ) = −(∂ₜΓ)∗C₁ and ∂ₜΓ = g⁻¹∗∇Ric(U) ~ g⁻¹∗U₁, ∇∂ₜΓ ~ g⁻¹∗U₂ + lower, give ∂ₜC₃ = C₁∗U₂ + C₂∗U₁ + lower. Verified (2.17). The Lᵖ energy: the C₁∗U₂ term → same-exponent Young (2.19); the C₂∗U₁ term → Hölder (p/(p−1), 2p, 2p) with C₂, U₁ ∈ L^{2p} from the base pair (2.20). Metric/volume variation of ‖C₃‖ₚ^p carries a coefficient ≲ |U| ≤ K, absorbed. Result (2.21) is correct, and the coupled system (2.22) is triangular (D₂,ₚ^U never appears on the C₃ side), so Grönwall closes and delivers U₂, C₃ ∈ L^∞_t L^p for all finite p. ✓

## 4. One principal term the note lists as "remaining" — read it as divergence form

The note writes ∂ₜU₂ = aΔU₂ + 2χC₁∗∇U₂ + … and then states "all remaining terms in (2.3) are lower." The transport term 2χC₁∗∇U₂ is **not** a remaining term to be bounded by Young. If one integrated it by parts alone, one would produce ∫ χ(tr C₂)|U₂|^p, and since C₂ ∈ ⋂_q L^q but **not** L^∞ (Step 57 §9 explicitly does not give C₂ in L^∞), that would require the weighted-Sobolev machinery, not same-exponent Young. The clean reading — and, I believe, the intended one — is that

  aΔU_k + 2χC₁·∇U_k = div(a∇U_k),  because ∇a = ∇(χ²) = 2χ∇χ = 2χC₁,

so the two together are the self-adjoint degenerate operator whose energy is exactly −(p−1)D_{k,p}^U with no cutoff-Hessian remainder. Under this reading the note's conclusion is correct and there is no gap. I recommend the enumeration state ∇a = 2χC₁ and the divergence-form identity explicitly, because the phrase "remaining terms are lower" is true only after the transport term is removed from that category and placed with the principal diffusion. This is bookkeeping, not a defect, but it is the one place a reader could wrongly conclude a stray ∫χ(tr C₂)|U_k|^p term escapes.

## 5. General induction (Sec. 4) and T-stage (Sec. 3) — pattern consistent

- The top jet χC_{k+2}∗U integrates to current C_{k+1} plus the boxed I₃₁-type term, controlled with the same fixed U₁ ∈ L⁴ and the Sobolev on χ|U_k|^{p/2}. ✓
- ∂ₜC_{k+1} = C₁∗U_k + Σ_{j<k} C_{k+1−j}∗U_j + lower → (4.4). ✓
- The intermediate sum Σ_{j=1}^{k} C_{k+2−j}∗U_j: for 2 ≤ j ≤ k both factors are previously-established ⋂_q L^q quantities, so these are genuine lower forcing by Hölder (‖C‖_{2p}‖U_j‖_{2p}‖U_k‖ₚ^{p−1}). ✓ The only top-derivative term is the diffusion (item 4), so nothing with ∇U_k escapes.
- The T-stage top jet ∇⁴a∗T = 2χC₄∗T + (C_j, j≤3)∗T is correct: ∇⁴(χ²) = 2χC₄ + 8C₁C₃ + 6C₂C₂, highest jet 2χC₄. Verified (3.1). The IBP (3.2) and aT_j = U_j − Σ(∇^ℓa)∗T_{j−ℓ} (no division by a) close T_k using the just-obtained C_{k+1} and base T₁ ∈ L⁴. ✓

The chain order is internally consistent with the Step 56 base block: T_{k−1} → (U_k, C_{k+1}) → T_k. The last U-pair (U_{s₀}, C_{s₀+1}) needs T_{s₀−1} as input, so the package requires T through T_{s₀−1} (not T_{s₀}) and U-pairs through (U_{s₀}, C_{s₀+1}). The highest cutoff jet appearing as a coefficient is C_{s₀+2} = C₉, but it enters only inside χC₉ = χ∇C₈ and is integrated away; only C₈ needs an independent L^p bound. This matches package (1.6) exactly. ✓

## 6. Package sufficiency for fixed-background H^{s₀} data (Sec. 1) — structurally sound

∂ₜA = g⁻¹∗∇(aE), and aE = Ric(U) (since Ric(aT) = a Ric(T) = aE), so ∇(aE) ~ U₁ and the triangular form (1.2) ∇̄^m ∂ₜA = g⁻¹∗U_{m+1} + P_m(A_{≤m−1}; U_{≤m}) has no top ∇̄^m A on the right. Integrating in time, A_m bounded for m ≤ s₀−1 requires U₁,…,U_{s₀} (1.4). With ∇̄^{m+1}g = (∇̄^m A)∗g + lower (1.3), boundedness of A₀,…,A_{s₀−1} gives g ∈ H^{s₀}. Terminal convergence follows from ∂ₜg = −2U ∈ L^∞_t H^{s₀} on the finite slab ⇒ L¹_t H^{s₀}, with positivity from ∫‖U‖_∞ dt ≤ K_τ(T\*−τ) < ∞. All arrows are correct, and U ∈ H^{s₀} needs U_{s₀}, consistent with the package. ✓

The conceptual separation is handled correctly: these restart constants (Sobolev constant of g(τ), Grönwall factors) are **per-datum and τ-dependent**, and the note keeps them out of the sequence-uniform first-exit chain. This is the right distinction; nothing here contaminates the collapse-independent γ used earlier.

## 7. Dependencies and remaining substance

1. **Step 56 local existence threshold.** Sufficiency of the package hinges on the referenced Step 56 theorem needing exactly s₀ > n/2 + 4 = 6 (hence integer s₀ = 7). The +4 (rather than the +2 typical of Rm ∈ L^∞ for Ricci-type systems) is not reproduced here; the whole H^{s₀} package size is calibrated to it. This should be confirmed against the actual Step 56 statement, since 7 versus a smaller integer changes the number of induction stages.

2. **Full tensor enumeration.** The note itself states the remaining work: writing (4.1)–(4.6) with every commutator and lower product explicit. The next-exchange check strongly supports survival of the collar mechanism but is not the completed finite-order proof. In particular the exact bookkeeping that (U_k, C_{k+1}) needs only T_{k−1} (not T_k) as forcing — via the χ-weighting aT_j = U_j − Σ(∇^ℓa)∗T_{j−ℓ} — must be verified term by term, since it is what keeps the T-tower at T_{s₀−1}.

3. **Dimension specialization.** The I₃₁ absorption is genuinely tied to n = 4: the critical exponent 2\* = 4 matches the base integrability U₁, T₁ ∈ L⁴ and the Sobolev on χ|U_k|^{p/2}. For general n this bridge needs U₁, T₁ ∈ L^n and 2\* = 2n/(n−2) rescaling of the Hölder tuple; the present argument does not yet cover n ≠ 4.

## Summary of findings

No false term or missing counterterm in the (U₂,C₃) exchange: the χC₄∗U IBP, the I₃₁ Hölder tuple and exponent p/2−1, the weighted Sobolev with p²-growth, and ∂ₜC₃ = C₁∗U₂ + C₂∗U₁ are all correct for p ≥ 2 at n = 4. The one wording matter is the transport term 2χC₁∗∇U_k, which is correct only when combined with aΔU_k into div(a∇U_k) (∇a = 2χC₁); the enumeration should state this rather than grouping it with "remaining lower terms." The package (U_k,C_{k+1})_{k≤s₀}, T_{0..s₀−1} does yield fixed-background H^{s₀} data through the triangular A-system, contingent on the Step 56 threshold s₀ > n/2+4 and on completing the full tensor enumeration the note flags as outstanding.