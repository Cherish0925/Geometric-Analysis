# TTCS Independent Branch Record

```json
{
  "step_id": 60,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step60_base_pair_proof.md",
    "Sessions/S0910A01/workspace/notes/step59_induction_ledger_repair.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md"
  ]
}
```

## Task

Verify the base-pair continuation proof in step60_base_pair_proof.md. The critical mathematical claims to check:

1. **C₂ evolution (§3):** The note claims ∂ₜC₂ = g^{-1}*U₁*C₁ with no U₂ term. The derivation: ∂ₜΓ = g^{-1}*∇(aE), and ∇(aE) = ∇(Ric(U)) = g^{-1}*U₁. Then [∂ₜ,∇²]χ = (∂ₜΓ)*∇χ = g^{-1}*U₁*C₁. Is this correct? In particular: (a) Is ∇(aE) really g^{-1}*U₁ without any U₀ or B₁ terms? The Ricci contraction of ∇U involves only U₁? (b) When computing [∂ₜ,∇²]χ, does ∂ₜΓ acting on ∇χ really give only U₁*C₁, not U₂? Note that ∇²χ involves Γ acting on ∇χ, and ∂ₜΓ = g^{-1}*U₁, so the commutator should be g^{-1}*U₁*C₁. But could there be a ∇(∂ₜΓ) term? Since ∇²χ = ∇(∇χ), and ∂ₜ∇ = ∂ₜΓ, the commutator [∂ₜ,∇] acting on ∇χ gives (∂ₜΓ)*∇χ. No derivative of ∂ₜΓ appears because ∇²χ = ∇(∇χ) and ∂ₜ only hits the connection once.

2. **m=1 signed-Hessian resolution (§2.3–2.6):** The note claims that the B₃*U₀ term, after integration by parts of C₃=∇C₂, produces a signed contraction ∫χ∇ᵢ∇ⱼχ B^{ij}(V) that the A03 lemma handles. Check: (a) After ∫χ|V|^{p-2}V*C₃*U₀ and IBP, the third term is -2∫χ|V|^{p-2}V*V*C₂. Is this really of the signed form ∫χ∇ᵢ∇ⱼχ B^{ij}(V) where B^{ij}(V) is a contraction of |V|^{p-2}V⊗V? (b) The note says 'This IS of the signed form (1.1)' — verify that the tensor indices work out: C₂ = ∇²χ = ∇ᵢ∇ⱼχ, and |V|^p*C₂ means a specific contraction. Can every such contraction be written as B^{ij}(V) with the required bounds |B|≤C|V|^p, |∇B|≤Cp|V|^{p-1}|∇V|?

3. **m=1 Hessian terms (§2.6):** The B₂*V terms from the principal operator and drift give ∫χ C₂*V*|V|^{p-2}V. The note claims this is also of the signed-Hessian form. Verify.

4. **Base order non-circularity:** The proof uses U₁ (from the base pair) in the C₂ evolution and in the T₁ derivation. But the U₁ estimate itself is coupled to C₂. Is the coupled Grönwall argument (4.1)–(4.3) free of circularity?

5. **Derivative-reordering lemma (§7):** The note claims C_{m+2} is paired only with U₀. Verify from the Leibniz expansion ∇^m(B₂*U) = Σ C(m,k) B_{k+2}*U_{m-k}. For k=m: B_{m+2}*U₀. For k=m-1: B_{m+1}*U₁. Could any term B_{m+2}*U_j with j≥1 arise from a different source (e.g., differentiating the principal operator div(a∇U) m times)?

Be specific: identify any mathematical error, any missing term, or any unjustified step. If the proof is correct, confirm it explicitly.

## Output

# Verification memo: base-pair continuation at m=1 (step60_base_pair_proof.md)

**Overall finding.** The proof's five load-bearing assertions are mathematically correct. The C₂ evolution identity is exact as stated; the m=1 signed-Hessian resolution is genuine (the apparent circular term is, before absolute values, exactly of the A03 Step 38 form (1.1)); the coupled Grönwall is free of circularity; and the derivative-reordering bookkeeping is right. I found no error in any conclusion. I did find five ledger-level defects — a missing (controllable) commutator descendant in §2.1, a mislabeled term in the T₁ display (5.2), an unnecessary and partially defective IBP mechanism in §2.7.1, suppressed metric/volume time variation, and a normal-form inconsistency with Step 59's (4.1) — each of which is repairable in one or two lines using mechanisms already in the note, with no change to any estimate. Details below, item by item.

---

## Item 1: the C₂ evolution ∂ₜC₂ = g⁻¹*U₁*C₁ — correct, both (a) and (b)

**(a) ∇(aE) = g⁻¹*U₁ with no U₀ or B₁ remnant.** The identity rests on aE = Ric(U), which holds because contraction is tensorial in the scalar factor: Ric(U) = Ric(aT) = a·Ric(T) = a(Ric(Rm) + Ric(G)) = a(Ric + g) = aE, using Ric(G) = g for G = (g∧g)/(2(n−1)) with the matching Kulkarni–Nomizu convention. Then, since the evolving covariant derivative is metric-compatible, ∇(aE) = ∇(g^{ik}U_{ijkl}) = g^{ik}∇U_{ijkl} = g⁻¹*U₁. The scalar a is already inside U, so no B₁ appears; the contraction commutes with ∇, so no zero-order term survives. As a cross-check, expanding the other way gives B₁E + a∇E = Ric(B₁⊗T + a∇T) = Ric(∇(aT)) = Ric(U₁), the same object. The clean form used in (3.1) is exact, not schematic.

**(b) The commutator [∂ₜ,∇²]χ has exactly one ∂ₜΓ insertion and no ∇(∂ₜΓ).** This is settled by the coordinate formula, which the note should perhaps display:
∇²_{ij}χ = ∂_i∂_jχ − Γ^k_{ij}∂_kχ.
Γ appears once, algebraically, undifferentiated. Since χ is a fixed spatial function (consistent with the stationary-support setup (1.2)),
∂ₜ(∇²_{ij}χ) = −(∂ₜΓ^k_{ij})∂_kχ = g⁻¹*U₁*C₁.
No second covariant derivative ever acts on the connection, so no U₂ can arise. The task's reasoning on this point is exactly right, and the boxed (3.4) is correct. The same coordinate-level count confirms Step 59's general (3.13): writing ∂ₜ(∇^{m+1}χ) = Σ_{j=0}^{m−1} ∇^j((∂ₜΓ)*C_{m−j}) and using ∇^j(g⁻¹*U₁) = g⁻¹*U_{j+1} (again metric compatibility kills derivatives of g⁻¹), the full expansion is Σ_{i=0}^{m−1} c_i U_{1+i}*C_{m−i} — top term C₁*U_m, next C_m*U₁, and **no U_{m+1} and no C_{m+1} anywhere**, matching (3.13) exactly.

**(3.5)–(3.6)** are Hölder (exponents p, p/(p−1)) then Young; correct.

One suppressed term: d/dt∫|C₂|^p dμ also picks up (∂ₜg^{-1})(C₂,C₂) norm variation and tr_g(∂ₜg) = −a·tr E volume variation. Both carry |∂ₜg| = 2|aE| = 2|Ric(U)| ≤ C‖U₀‖_∞, hence absorb into the existing C‖Z‖_p^p. Same remark applies to the V-energy in (4.1)–(4.3) and to (5.5). This is Step 59's remaining obligation (a); structurally harmless here because (I1) supplies the pointwise U₀ bound.

## Item 2: the B₃*U₀ resolution — correct, and the signed form is genuine

**Leibniz coefficient.** ∇³(χ²) = 2χC₃ + 2(C₂⊗C₁) + 4(C₁⊗C₂) = 2χC₃ + 6C₁*C₂. The "6" in the note is right.

**The three IBP descendants.** Starting from 2∫χ(|V|^{p−2}V)*C₃*U₀ with C₃ = ∇C₂ exact (C₃ := ∇(∇²χ) by definition; no symmetry of ∇³χ is needed, only the derivative placement):
1. −2∫C₁*(|V|^{p−2}V)*U₀*C₂ — Young with ‖C₁‖_∞, ‖U₀‖_∞: ≤ C(‖C₂‖_p^p + ‖V‖_p^p). ✓
2. −2∫χ∇(|V|^{p−2}V)*U₀*C₂ — the note says "absorbed by diffusion," which compresses one step: the integrand is ≤ C_p χ|C₂|‖U₀‖_∞|V|^{p−2}|∇V| = (χ|∇V||V|^{(p−2)/2})(C|C₂||V|^{(p−2)/2}) ≤ εD_{1,p}^U + C_ε|C₂|²|V|^{p−2}, and then |C₂|²|V|^{p−2} ≤ (2/p)|C₂|^p + ((p−2)/p)|V|^p for p ≥ 2. So the true output is εD + C(‖C₂‖_p^p + ‖V‖_p^p) — the χ travels with the diffusion factor, so the absorption is legitimate. This is also precisely where the +C‖C₂‖_p^p on the right of (4.1) line one comes from; the note's ledger is consistent, just compressed.
3. −2∫χ(|V|^{p−2}V)*(∇U₀)*C₂ = −2∫χ(|V|^{p−2}V)*V*C₂, since ∇U₀ = ∇U = V exactly.

**(2a) The third descendant is genuinely of signed form (1.1).** The integrand is a complete metric contraction of χ ⊗ (∇²χ) ⊗ |V|^{p−2}V ⊗ V. Relabel the two slots where ∇²χ's indices sit as i,j and define B^{ij}(V) := |V|^{p−2}·(contraction of V⊗V against the dual metric slots). This is always possible for a complete contraction, regardless of tensor rank or index placement; the A03 lemma does not require symmetry of B^{ij}, only the two bounds in its (1.2).

**(2b) The bounds hold.** |B| ≤ C|V|^p and |∇B| ≤ C_p|V|^{p−1}|∇V| for any fixed contraction of |V|^{p−2}V⊗V, with the |V|^{p−2} factor handled by the standard regularization √(|V|²+ε²) → ε↓0 that A03 Step 38 explicitly allows ("after the standard tensor-norm regularization if necessary"). The diffusion on the right of A03 (1.4) is ∫χ²|∇V|²|V|^{p−2} = D_{1,p}^U exactly, and ‖dχ‖_∞ = C_cut is (I4). So (2.16) is a valid application, and the m=1 "circular" remnant is closed by the signed lemma, not by the forbidden absolute-value form (2.13).

The note's structural diagnosis of *why* m=1 closes differently is also correct: at m=1 the top-cutoff IBP remnant is χ(|V|^{p−2}V)*C₂*(∇U₀) with ∇U₀ = V the tested unknown itself, producing a pure-V bilinear against a Hessian; at m ≥ 2 the remnant is χ(|U_m|^{p−2}U_m)*C_{m+1}*U₁, where C_{m+1} (m+1 ≥ 3 derivatives) is not a Hessian and U₁ is not the tested unknown, so only the Hölder residual I_m with U₁ as base data is available. The distinction is real and correctly exploited.

## Item 3: the B₂*V Hessian terms — correct

From §2.1, the term is B_{2,jk}∇^jU^I contracted against the test function's k-index: with B₂ = 2χC₂ + 2C₁*C₁, the χ-part of the energy integrand is 2χ(∇_j∇_kχ)·|V|^{p−2}V^{kI}V^j{}_I, i.e. B̃^{jk}(V) = 2|V|^{p−2}V^{kI}V^j{}_I with |B̃| ≤ C|V|^p, |∇B̃| ≤ C_p|V|^{p−1}|∇V|. Signed form (1.1) verbatim; the C₁*C₁*V half is bounded by ‖C₁‖²_∞‖V‖_p^p. Same for the drift copy in §2.2. ✓

**Ledger gap found in §2.1 (flag A).** The divergence-form rewriting is not quite as clean as "div(a∇V) plus connection corrections of type aT*V." Writing ∇_j(a∇_k∇^jU^I) = div(a∇V) requires ∇_k∇^jU^I = ∇^j(∇_kU^I) + [∇_k,∇^j]U^I, and the commutator is Rm*U (zero order in U). Differentiating it: ∇_j(aRm*U) = B₁*Rm*U + a∇Rm*U + aRm*V. Since ∇G = 0 (G is parallel), ∇Rm = ∇T, so the middle term is **aT₁*U₀ — a first-order curvature factor paired with U₀**, which is not of the type "aT*V" that §2.1 displays, and it is absent from the §2.8 table. It is nonetheless controllable with the note's own tools: aT₁ = U₁ − B₁*T₀ (the m=1 case of (5.3)) turns it into V*U₀ (bounded coefficient via (I1)) plus B₁*T₀*U₀ (≤ C(‖T₀‖_p^p + ‖V‖_p^p) via (I2) and (I4)). The B₁*Rm*U piece is the same shape. So the estimate stands, but the ledger should list this descendant and its conversion explicitly; it is also the same mechanism that disposes of the aT₁*T₀ term hidden in the "⋯" of (5.2). Related minor omission: [∂ₜ,∇]U = (∂ₜΓ)*U₀ = g⁻¹*V*U₀ (bounded coefficient, Step 59's (2.12) at m=1) is not in the §2.8 table either.

**Mechanism defect in §2.7.1 (flag B).** For ∫C₁*C₂*U₀*|V|^{p−2}V the note integrates C₂ = ∇C₁ once. As sketched this is problematic twice over: the IBP reproduces a C₂*C₁*U₀*ψ term of the same type (near-circular), and the descendant C₁*C₁*U₀*∇(|V|^{p−2}V) carries no χ factor, so its |∇V| cannot be absorbed by the χ²-weighted diffusion D_{1,p}^U (one would need an extra |C₁|² ≤ Cχ cutoff hypothesis, which (I4) does not state). The repair is to do nothing at all: direct Young with exponents (p, p/(p−1)) gives ∫|C₁||C₂||U₀||V|^{p−1} ≤ ‖C₁‖_∞‖U₀‖_∞(‖C₂‖_p^p + ‖V‖_p^p) immediately. The same direct bound treats the 6C₁*C₂*U₀ half of B₃*U₀ in §2.3. Conclusion unchanged; the stated mechanism should be replaced.

## Item 4: non-circularity of the base order — confirmed

I re-derived the full right-hand side of the V-energy and the Z-energy:

- **V-equation sources and their requirements:** principal (diffusion, sign favorable); B₁*∇V drift → no-division Young using B₁ = 2χC₁ *pointwise* (so no quotient by a is ever formed — consistent with A03's correction of the Step 37 quotient error); B₂*V and the C₃-descendant three → signed-Hessian lemma (needs ‖C₁‖_∞, D_{1,p}^U); C₃-descendants one, two and §2.7.1 → Young producing ‖Z‖_p^p + ‖V‖_p^p; reaction V*U₀, linear B₁*U₀ + aV, curvature commutators aRm*V + aRic*V = U₀*V + O(aV) → all bounded coefficient via aT = U; the flag-A descendant aT₁*U₀ → V*U₀ + B₁*T₀*U₀ via (5.3). **Every input is (I1), (I2) with finite q = p, or (I4). In particular, no step in the V-energy uses T₀ ∈ L^∞, and no right-hand side is superlinear in ‖Z‖_p^p.** ✓
- **Z-equation:** needs only ‖V‖_p (Hölder–Young (3.5)–(3.6)) plus absorbable norm/volume variation via ‖U₀‖_∞. ✓

Hence f = ‖V‖_p^p + ‖Z‖_p^p satisfies the scalar ODI f′ + cD ≤ C_{p,τ}(1+f) with f(τ) finite (smooth per-datum data at τ > 0). Scalar Grönwall bounds both components simultaneously; neither component is ever assumed bounded in order to bound the other. The coupling is genuinely two-way (V-energy needs Z, Z-energy needs V), which is exactly why the pair formulation is necessary and sufficient here. (4.3) is correct, with e^{C(t−τ)} finite on any finite slab — adequate for the IL observation time T = θr².

The chain (6.1) is then respected in order: pair output → T₁ (§5, using (I2) and the pair) → T₀ ∈ L^∞ via W^{1,p} ↪ L^∞ for p > 4 in dimension four with Sobolev constants from (I3) (§5.3 correctly states the p > 4 condition). No later output feeds back into an earlier step. Non-circular. ✓

**Mislabeled term in §5.2 (flag C) — the one genuine repair needed in the T₁ step.** Differentiating the drift B₁*∇T of (5.1) gives ∇(B₁*W) = **B₂*W** + B₁*∇W — B₂ paired with the *current* unknown W = T₁ — not "B₂*T₀" as displayed in (5.2). Nothing in the expansion of (5.1) produces B₂*T₀. The note then bounds the non-arising term by ‖B₂‖_{2p}‖T₀‖_{2p} and never treats the arising one. The repair is available in the same note: B₂*W = 2χC₂*W + 2C₁*C₁*W, and the χC₂*W*ψ(W) energy term is precisely the m=1 signed-Hessian term for the T-equation, closed by the A03 lemma with D_{1,p}^T = ∫a|∇W|²|W|^{p−2} and ‖C₁‖_∞ — the verbatim analog of §2.6. The remaining genuine terms all check out: B₁*T₂ = B₁*∇W (diffusion absorption, including the B₁*ΔT piece of [∇,aΔ]T); aW = V − B₁*T₀ via (5.3)–(5.4) (this substitution is used at the *source* level, which is legitimate since the diffusion aΔW is untouched); aW*T₀ = W*U₀ and aT*W = U₀*W (bounded coefficients); B₁*T₀*T₀ (≤ ‖T₀‖²_{2p}‖W‖^{p−1}_p by Hölder, exponents p and p/(p−1)); a∇Rm*T = aT₁*T₀ → V*T₀ + B₁*T₀*T₀ via (5.3). So (5.5) survives with the ledger corrected.

Two subsidiary points on §5.2: (i) "B₂ is a fixed spatial function" is imprecise — B₂ = ∇²a with the evolving connection — but the needed finiteness holds anyway: ‖B₂‖_{2p} ≤ C(‖χ‖_∞‖C₂‖_{2p} + ‖C₁‖²_{4p}) < ∞ per-datum via (I4) and the pair output at exponent 2p. (ii) **Normal-form inconsistency with Step 59 (flag D):** Step 59's unweighted equation (4.1) carries a χC_{m+2}*T₀ top-cutoff source, i.e. a B₂*T term in the zero-order T-equation, whereas Step 60's (5.1) has no B₂*T source. If the B₂*T source is present, differentiating once also gives B₃*T₀ ⊃ 2χC₃*T₀, whose IBP third descendant is χ|W|^{p−2}W*(∇T₀)*C₂ = χ|W|^{p−2}W*W*C₂ — again signed form (T₁ = W is the tested unknown), closed by the same lemma. Either normal form closes at m=1, but §5.2 should state which one is in force and list the corresponding terms; this is the same class of omission as flag C.

## Item 5: the derivative-reordering lemma — correct, with one clarification

The Leibniz bookkeeping checks out completely. Sources of cutoff jets at level m:

- ∇^m(B₂*U) = Σ_k C(m,k)B_{k+2}*U_{m−k}: k = m gives B_{m+2}*U₀ — the **only** occurrence of B_{m+2}, paired with U₀; k = m−1 gives B_{m+1}*U₁ ⊃ 2χC_{m+1}*U₁ (the next-cutoff current term, correctly extracted in Step 59 (2.3b)).
- ∇^m(aΔU) = Σ_k B_k*U_{m+2−k}: max cutoff index m (B_m*U₂). ∇^m(B₁*∇U): max B_{m+1}*U₁. **So differentiating the principal operator m times cannot produce B_{m+2}*U_j for any j** — answering the question directly: no such term arises, because div(a∇U) contains at most one derivative of a. The divergence-form rewriting aU_{m+2} → div(a∇U_m) only costs B₁*U_{m+1} (absorbable drift) and Rm*U_m = T₀*U_m commutators (bounded coefficient once the base T₀ ∈ L^∞ is in place, which it is for m ≥ 2).
- ∇^m((C₁C₁)*U): max jet C₁*C_{m+1}*U₀. ∇^m(aU): max B_m*U₀. Time commutator [∂ₜ,∇^m]U: max U-index m (Item 1 expansion), no new cutoff jets.
- B_{m+2} = 2χC_{m+2} + Σ_{i=1}^{m+1}c_iC_i*C_{m+2−i} is an *exact* Leibniz identity on the product χ·χ, and C_{m+2} = ∇C_{m+1} is exact by definition. Consequently the IBP on the top term needs no reordering at all; the commutators the lemma mentions live elsewhere — in the U-side divergence-form rewriting (T₀*U_m) and in index-collision re-expansions (T₀*C_{≤m}) — all with T₀ bounded after the base layer and all cutoff indices ≤ m. The lemma's conclusion ("C_{m+2} paired only with U₀; reordering commutators involve only T_{≤m−1}, C_{≤m}") is correct; its proof sketch is loose about where the commutators actually sit, and tightening that location is part of the "genuine tensor lemma still to be written with indices" that Step 59 already flags.

For completeness I also checked the m ≥ 2 residual mechanics in Step 59 §3.3 that this base note feeds: the Hölder exponents (4, p, 4, 2p/(p−2)) sum to 1 ✓; the Sobolev step ‖f‖₄² ≤ C_S(p²D_{m,p}^U + C‖V‖_p^p) for f = χ|V|^{p/2} is standard in dimension four ✓; and the closing Young is two-stage (first ε‖f‖₄² + C_ε‖Z‖²‖U₁‖₄²‖V‖^{p−2}, then X²Y^{p−2} ≤ (2/p)X^p + ((p−2)/p)Y^p), producing a linear Grönwall with the bounded time-dependent coefficient ‖U₁(t)||₄² supplied by this note's base pair. The single-stage "Young therefore yields (3.9)" in Step 59 compresses exactly this and is fine. The same line at m=1 would require ‖U₁‖₄ with U₁ = V current — confirming again why the m=1 level must close by the signed lemma instead, as this note does.

## Consolidated repair list (ledger-level; no estimate changes)

- **A (§2.1, §2.8 table):** add the divergence-form descendant aT₁*U₀ (= a∇Rm·U, using ∇G = 0) and the time commutator g⁻¹*V*U₀; both are controlled by (5.3), (I1), (I2).
- **B (§2.7.1 and the 6C₁*C₂*U₀ half of §2.3):** replace the IBP mechanism (near-circular and producing an absorbable-looking but unweighted |∇V| descendant) with the direct Young bound (p, p/(p−1)).
- **C (§5.2, display (5.2)):** the arising term is B₂*W, not B₂*T₀; treat its χC₂*W part by the signed-Hessian lemma against D_{1,p}^T (one line, mirroring §2.6). Also correct "B₂ fixed spatial function" to the per-datum bound via ‖C₂‖_{2p}, ‖C₁‖_∞.
- **D (interface):** reconcile the T-equation normal form with Step 59 (4.1); if a B₂*T source is present, its m=1 top-cutoff descendant χC₃*T₀ also closes by IBP plus the signed lemma, since ∇T₀ = W.
- **E ((3.5), (4.1)–(4.3), (5.5)):** restore metric- and volume-variation terms; all carry |∂ₜg| ≤ 2|Ric(U)| ≤ C‖U₀‖_∞ and absorb into existing right-hand sides. This is Step 59's standing obligation (a).

## Interface status

The note is internally consistent with its two cited inputs: the A03 Step 38 lemma is applied only to genuine signed contractions (never to the absolute-value form (2.13)), its hypotheses (closed manifold / buffered stationary collar per (1.2), χ²-weighted diffusion, ‖dχ‖_∞, regularized power bounds) all match, and the discredited ‖∇²χ‖₄ fallback and the χ²/a pointwise quotient are nowhere used. The base-layer output (6.1)–(6.2) is exactly the input Step 59's general induction consumes at (3.9) and (4.4)–(4.6), and Step 59's remaining obligations (a)–(d) are unaffected — flags A–E sit inside obligation (a)/(b) territory rather than adding new ones. Nothing in this note bears on the λ<0 Ishida–LeBrun geometry inputs (curvature budget, terminal density) or on the general Yau 26 statement; the note's own closing paragraph states that division of labor accurately.

**Bottom line:** the base-pair continuation is proved correctly at tensor-index level. The C₂ evolution is exact with no U₂; the m=1 signed-Hessian closure of both the B₃*U₀ remnant and the B₂*V terms is valid under the A03 lemma as stated; the coupled Grönwall and the order (6.1) are non-circular; and no source at any level pairs C_{m+2} with anything but U₀. The five ledger repairs above should be folded into the write-up, but each is settled by mechanisms the note itself establishes, and none alters a single estimate.