# TTCS Independent Branch Record

```json
{
  "step_id": 23,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step23_cooperative_persistence_theorem.md",
    "Sessions/S0910A01/workspace/notes/step20_closed_tensor_estimate.md",
    "Sessions/S0910A01/workspace/notes/step22_current_energy_formulation.md",
    "Sessions/S0910A01/workspace/scripts/step23_cooperative_persistence.py"
  ]
}
```

## Task

Verify the central structural claim in the Step 23 cooperative persistence theorem for the four-dimensional negative LeBrun/Ishida-LeBrun cutoff-flow route. The claim: for the normalized cutoff flow ∂_t g = -2χ²(Ric+g) on a closed four-manifold, when the q=2 curvature energy H_{2,α} = ∫ η_α² F² is tested against η_α² H (the testing function), and the reaction ∫ η_α² aF³ is absorbed using the Sobolev variable v = η_α a^{1/2} F, the resulting gradient integral ||∇v||² decomposes into the α-component dissipation D_{2,α} plus r⁻² H-type localization terms, all supported within U_α. Specifically: (1) The gradient ∇(η_α a^{1/2} F) = η_α a^{1/2}∇F + η_α (∇a/(2a^{1/2}))F + a^{1/2}F ∇η_α has all three contributions supported in supp(η_α) ⊂ U_α. (2) The term η_α² a|∇F|² is bounded by C·D_{2,α}. (3) The term η_α²(|∇a|²/a)F² ≤ Cr⁻² H_{2,α}. (4) The term a|∇η_α|²F² ≤ Cr⁻² ∫_{U_α}F². (5) Therefore the Sobolev inequality ||v||₄² ≤ A_α²(CD_{2,α} + Cr⁻²∫_{U_α}F²) involves ONLY the α-component dissipation, no neighbor dissipation Z_β. (6) After Hölder R ≤ γ_α(D + r⁻²H) and absorption into cD, the vector inequality is S' + cZ ≤ (b/r²)BS with ε=0 (no εBZ term). Check whether any term was missed: inverse metric variation in F, measure evolution, Hessian-a integrations by parts, the lower-order aFq term from normalization, or overlap contributions to ∫_{U_α}F². Also check: does the cooperative comparison for the resulting S'≤(b/r²)BS give componentwise Gronwall with constants independent of component count?

## Output

## Verifier memo: dissipation locality (ε = 0) in the Step 23 cooperative persistence theorem

### Summary judgment

The central structural assertion — that the reaction absorption injects only the **α-component dissipation** D_{2,α} and no neighbor gradient Z_β, so the vector system is S′ + cZ ≤ (b/r²)BS with no εBZ term — is **mathematically sound as a statement about which gradient-quadratic quantities can appear**, and it survives every term listed in the task (measure evolution, inverse-metric variation in F, Hessian-a integration by parts, the lower-order aF^q term). None of these produces a neighbor dissipation. This is a genuine and robust structural point, and it correctly identifies why the Step 22 formulation carried an apparent neighbor-dissipation coupling.

However, the **zeroth-order (H-energy) neighbor coupling** and the smallness of the scalar γ_α — the two ingredients that turn the RHS into Σ_β B̃_{αβ}S_β with well-defined B̃ — rest on a covering/buffer property that the geometry stated in §1 does not supply. As written, the "centers separated by ≥ 10r, supp η_α = B_{4r}, U_α = B_{5r}" construction gives mutually **disjoint** inner supports and only touching U_α, which supports neither the overlap sum ∫_{U_α}F² ≤ Σ_{β∼α}H_{2,β} nor the neighbor set β∼α. This is the same load-bearing issue Step 22 raised, relocated rather than removed.

Below I check each sub-part, then the geometry, then the cooperative Gronwall.

---

### Part-by-part verification of the decomposition

**(1) Support of ∇v.** Correct, and in fact trivial: every one of the three terms in ∇(η_α a^{1/2}F) carries a factor of η_α or ∇η_α, hence is pointwise supported in supp η_α ⊂ B_{4r}(p_α) ⊂ U_α. One presentational point: the middle term is written as (∇a/2a^{1/2})F, which at points where a = χ² = 0 is a 0/0 form. The correct smooth variable is a^{1/2} = χ, so ∇(a^{1/2}) = ∇χ and |∇a|²/(4a) = |∇χ|², bounded wherever χ is a smooth cutoff. Writing χ rather than a^{1/2}/a^{1/2} removes any degeneracy worry. No structural effect.

**(2) η_α²a|∇F|² ≤ C·D_{2,α}.** Correct with C = 1. F = (1+|Rm|²)^{1/2} gives ∇F = ⟨Rm,∇Rm⟩/(1+|Rm|²)^{1/2}, so |∇F| ≤ |Rm||∇Rm|/(1+|Rm|²)^{1/2} ≤ |∇Rm|. Hence ∫η_α²a|∇F|² ≤ ∫η_α²a|∇Rm|² = D_{2,α}. The companion contractions |E| ≤ C_4F and |∇E| = |∇Ric| ≤ |∇Rm| (since ∇g = 0) are also correct; these are the Step 20 §1 identities and they are the reason no separate defect-gradient energy is needed.

**(3) η_α²(|∇a|²/a)F² ≤ Cr⁻²H_{2,α}.** Correct given |∇χ| ≤ Cr⁻¹: |∇a|²/a = 4|∇χ|² ≤ Cr⁻², then integrate against η_α²F². Depends only on the flow-cutoff gradient bound, which is the standing Whitney/cutoff input.

**(4) a|∇η_α|²F² ≤ Cr⁻²∫_{U_α}F².** Correct as an inequality (a ≤ 1, |∇η_α| ≤ Cr⁻¹). Note the right side is the **unweighted** integral of F² over the support of ∇η_α (the annulus B_{4r}\B_{3r}), not an η²-weighted energy. This is the precise place where the neighbor coupling enters, and where the geometry question below bites.

**(5) The Sobolev product contains only D_{2,α}.** Correct. Expanding |∇v|² ≤ 3(three squares) and using (2)–(4),

  ∫|∇v|² ≤ C·D_{2,α} + Cr⁻²H_{2,α} + Cr⁻²∫_{U_α}F².

There is no η_β²a|∇F|² term. There is no geometric mechanism to produce one: the α-tested equation only ever multiplies |∇F|² by η_α² or by (∇η_α)²·(bounded), both supported in U_α, and any such |∇F|² is by definition counted as D_{2,α}, not as D_{2,β}. Minor arithmetic: the note writes coefficient 2 for three squared terms; it should be 3 by |x+y+z|² ≤ 3(x²+y²+z²). Absorbed into C, no consequence.

**(6) The absorbed inequality and ε = 0.** Correct, and importantly the absorption is legitimate because the reaction dissipation Cγ_α D_{2,α} and the good LHS dissipation c₂D_{2,α} carry the **same η_α² weight**, so (c₂ − Cγ_α)D_{2,α} ≥ (c₂/2)D_{2,α} once γ_α < c₂/(2C). The residual RHS is C(γ_α+1)r⁻²∫_{U_α}F², which is a zeroth-order term. So the vector inequality genuinely has no εBZ. This is the real content and it is sound.

---

### Direct answer to "was any term missed?"

Every term the task names was checked against whether it can produce a neighbor gradient Z_β:

- **Measure evolution** ∂_t dμ = −a tr(E) dμ contributes ∫η_α²F²·(−a tr E), of size ≤ ∫η_α²aF²·|E| ≤ C∫η_α²aF³. This is a **cubic reaction of the same type as R_{2,α}**, absorbed identically. No new gradient.
- **Inverse-metric variation in F.** |Rm|² carries four inverse-metric contractions; ∂_t g^{ij} = 2aE^{ij} makes each contribute ~ aE∗Rm∗Rm ~ aF³. Again a cubic reaction inside R_{2,α}. No new gradient.
- **Hessian-a integration by parts** (Step 20 §4, (4.2)–(4.3)): after one IBP the terms are bounded by ε·(α-dissipation) + C_ε r⁻²(|∇a|²/a)F^q + C·(a|∇η|²F^q). The derivative can land on η²F^{q-2}, on ∇F, on F^{q-3}∇F, or on η∇η — in every case the result is weighted by η_α or ∇η_α and stays in U_α. No neighbor dissipation is generated. This is the one place a hidden gradient could plausibly have appeared, and it does not.
- **Lower-order aF^q normalization term.** This is O(1)·H_{2,α} with no r⁻². Since r is small, it is dominated by the r⁻²H localization; it contributes only a +C·I shift to the cooperative matrix (a uniform diagonal), which changes the row sum from bL/r² to bL/r² + C ≈ bL/r². Harmless.
- **Overlap contributions to ∫_{U_α}F².** This is the sole genuine neighbor coupling, and it is **zeroth order** (H-energy), exactly the intended BS term. It does not carry a gradient.

Conclusion on the task's central question: **no listed term injects a neighbor dissipation.** The ε = 0 structure is robust to all of them and to the precise, still-schematic coefficients of the underlying tensor inequality (2.1). This robustness argument (the support of the testing function forces the answer regardless of coefficients) is valid.

---

### The point that is not yet supported: γ_α control and the ∫_{U_α}F² overlap step

The εBZ-free statement is only half of the vector inequality. The other half is that the RHS reads as Σ_β B̃_{αβ}S_β with a well-defined nonneg matrix B̃, which requires two conversions of **bare local integrals** into **component energies**:

1. The Hölder scalar factor γ_α = A_α²‖F‖_{L²(supp η_α)} = A_α²(∫_{B_{4r}(p_α)}F²)^{1/2} must be ≤ CΓ_*. But ∫_{B_{4r}(p_α)}F² ≥ ∫η_α²F² = H_{2,α}, with the annular part B_{4r}\B_{3r} (where η_α < 1) contributing extra mass that H_{2,α} does not bound from above. So γ_α is **not** controlled by the first-exit quantity Γ_* = sup_α A_α²H_{2,α}^{1/2} from inner cutoffs alone.

2. The localization ∫_{U_α}F² in (4) must equal Σ_{β∼α}H_{2,β}. This needs a covering lower bound Σ_β η_β² ≥ 1 on U_α.

Step 22 handled (1) with a **nested outer cutoff** ξ_α ≡ 1 on supp η_α, so ‖F‖_{L²(supp η_α)} ≤ ‖ξ_α F‖_{L²} = (H_{2,α}^{outer})^{1/2}. That device is precisely what Step 23 discarded, and §2 of Step 23 instead invokes ∫_{U_α}F² ≤ Σ_{β:U_β∩U_α≠∅}H_{2,β} — an overlapping-cover estimate. So the two notes trade one requirement for another; neither is unnecessary.

A clean route that keeps both properties: use the nested pair, but let ξ_α appear **only undifferentiated** in the scalar Hölder factor (so ‖F‖_{L²(supp η_α)} ≤ (H_{2,α}^{outer})^{1/2}, no ∇ξ_α, hence still no neighbor dissipation) while the L⁴ factor uses the inner v = η_α a^{1/2}F (giving α-local dissipation). This simultaneously delivers ε = 0 and a γ_α bounded by a single-component (outer) energy. The cost is that the controlling energy is then the outer energy, whose own evolution reaches one buffer further out; where the buffer chain terminates is where the true graph coupling appears. The note has not exhibited a **single finite, non-regenerating cutoff hierarchy** that at once (a) keeps the dissipation α-local, (b) bounds the reaction scalar factor by a component energy, and (c) closes the localization term. Resolving this bookkeeping is the concrete analytic content still missing behind (3.1).

---

### Geometry inconsistency in §1

The stated construction is internally inconsistent for the neighbor picture it then uses:

- "Centers separated by at least 10r" with supp η_α = B_{4r}(p_α) makes the inner supports **mutually disjoint** (4r + 4r = 8r < 10r), and U_α = B_{5r} only touch (5r + 5r = 10r). With disjoint supports the neighbor set β∼α is empty, the overlap number is N = 1, and Σ η_β² ≥ 1 on U_α does **not** hold on the annulus B_{5r}\B_{4r} (no cutoff is nonzero there). Then ∫_{U_α}F² ≤ Σ_{β∼α}H_{2,β} does not hold, and the matrix B̃ is not defined.
- The rest of the note needs the opposite: a bounded-overlap **cover** (centers ~cr apart, overlap number N > 1 from a dimensional packing count, covering lower bound Σ η_β² ≳ 1). 

The two properties actually needed together are (i) Σ_α η_α² ≤ N (bounded overlap, for summing) and (ii) Σ_α η_α² ≥ 1 on each U_α (covering, for ∫_{U_α}F² ≤ Σ H_{2,β}). A 10r-separated family provides neither. The geometric input should be restated as a Whitney/partition cover with both bounds, and it should be verified that the same cover is compatible with the relative-Sobolev comparability (3.2) A_α/A_β ≤ C_A for β∼α and with the volume-comparison (1.3)-type step that is collapse-stable.

---

### Cooperative Gronwall and count-independence

The final question — does S′ ≤ (b/r²)BS give componentwise Gronwall with constants independent of the number of components — is **correct**, given a well-defined nonneg B with row sums ≤ L = NC_A⁴:

- B ≥ 0 entrywise makes M = (b/r²)B a Metzler (cooperative/quasimonotone) matrix, so the comparison principle gives componentwise S(t) ≤ (e^{tM}S(0))_α.
- Row sums of e^{tM} obey the sharp bound e^{tR} with R = bL/r²: with v(t) = e^{tM}𝟙 ≥ 0, v′_α = Σ_β M_{αβ}v_β ≤ R‖v‖_∞, hence ‖v(t)‖_∞ ≤ e^{Rt}. Therefore S_α(t) ≤ e^{Rt}max_β S_β(0), i.e. Γ(T) ≤ e^{bLθ/2}Γ(0) over T = θr².
- The bound depends only on N (overlap) and C_A (comparability), both dimension/geometry constants — **independent of the component count**. This matches (4.2) and the script's amplification e^{bLθ} and spike control.

Two provisos. First, M is constant only while the first-exit condition Γ(t) ≤ Γ_* holds (the absorption γ_α < c₂/(2C) requires it), so the correct logic is a continuity/bootstrap on the first-exit interval with b uniform there, not an unconditional linear ODE; the note treats this as "provisional" in §11, which is consistent. Second, the O(1) diagonal term from the aF^q normalization shifts R to bL/r² + C; over T = θr² this multiplies the amplification by e^{Cθr²} ≈ 1, so it does not disturb count-independence.

---

### On the verification script

`step23_cooperative_persistence.py` verifies the **arithmetic of the cooperative comparison** with placeholder constants (K0 = 15100, b = 12, C_A = 1.3, N = 8): it confirms amplification < 4, spike control on a ring graph, and the resolvent reduction. It does **not** test the analytic content ε = 0 — CHECK 3 prints the assertion in text without evaluating any tensor quantity — and it cannot, since ε = 0 is a statement about the integration-by-parts structure, not about a finite matrix. The numeric confirmation is therefore a consistency check on the ODE step, not on the persistence theorem's load-bearing input. The constants b and K0 are not derived from the tensor computation; the true b enters R = bL/r² and hence the amplification, so the "amplification ≈ 1.18" figure is illustrative rather than established.

---

### What would make (3.1) fully rigorous

1. A single cutoff hierarchy (inner η_α for the dissipation variable, an outer ξ_α appearing only undifferentiated in the Hölder scalar factor, and possibly a covering partition) that simultaneously gives ε = 0, γ_α ≤ CΓ_* from a component energy, and closure of the r⁻²∫_{U_α}F² localization, with a finite non-regenerating buffer.
2. A restated cover geometry providing both bounded overlap N and the covering lower bound Σ η_β² ≥ 1 on each U_α, compatible with (3.2) and with the collapse-stable volume comparison.
3. The exact q = 2 tensor inequality (2.1) with its coefficients — currently schematic per §11 — written with measure evolution, inverse-metric variation, and Hessian-a IBP included, confirming the term ledger already sketched in Step 20 (5.1). The structural conclusion ε = 0 is coefficient-independent, so this step affects only the values of c₂, b, and the absorption threshold, not the persistence structure.

The dissipation-locality insight is correct and worth keeping as the backbone; the remaining work is the cutoff/cover bookkeeping that converts the honest bare-integral RHS into the neighbor-energy matrix, which is exactly the point Step 22 flagged and which is not yet closed by Step 23.