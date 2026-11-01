# TTCS Independent Branch Record

```json
{
  "step_id": 53,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step53_coupled_transported_coefficient_start.md",
    "Sessions/S0910A03/workspace/notes/step52_normalized_local_flow_start_repair.md",
    "Sessions/S0910A03/workspace/data/step53_coupled_grading_checks.json"
  ]
}
```

## Task

Verify the coupled transported-coefficient start theorem for the normalized cutoff flow ∂_t g = -2χ²(Ric+g). The central mathematical claim is that the coupled DeTurck system (metric equation + scalar transport for χ̂=χ∘φ⁻¹) has short-time existence through a staggered parabolic-ODE grading. Specifically verify:

1. PULLBACK IDENTITY: Does the coupled system (1.4) in the note actually pull back to give ∂_t g = -2χ²(Ric+g) with FIXED χ in geometric coordinates? Check the computation: g=φ*ĝ, â∘φ=a because χ̂=χ∘φ⁻¹.

2. PRINCIPAL STRUCTURE: The coupling matrix shows metric eq at order k needs ψ at order k (coefficient only), transport at order k needs V at order k+1 (through DeTurck vector W~∂V). Is this 'lower-triangular' description correct?

3. PARABOLIC GAIN: The note claims V∈C_t(H^s)∩L²_t(H^{s+1}) from the parabolic equation, and this extra L²_t derivative compensates the ODE for φ needing ∫||âW||_{H^s}dt, where ||W||_{H^s}≤C||V||_{H^{s+1}}. Verify this chain.

4. TRANSPORT IBP: The transport energy estimate claims ∫∂^α ψ·ψ²W·∂_k∂^α ψ = -½∫(∂^α ψ)²·∂_k(ψ²W), so the top-order ψ term is absorbed without needing ψ at order k+1. Is this correct for the SPECIFIC equation ∂_t ψ = ψ²W^k∂_kψ (note the coefficient is ψ² not just a constant)?

5. CONTRACTION: The I2 factorization â₁-â₂=(χ̂₁+χ̂₂)(χ̂₁-χ̂₂) is used to bound the coefficient difference in the contraction. Does this genuinely make the cross-terms proportional to ||χ̂₁-χ̂₂|| with bounded multipliers?

6. CRITICAL GAP: Is there any hidden derivative loss in the coupled fixed-point that the note misses? In particular, does the composition ψ=χ∘φ⁻¹ really give ψ∈H^s when φ∈H^s, for the specific Sobolev orders needed?

The flat-torus test (Step 52) permanently falsified Step 51's homogeneous energy closure. This note does NOT use energy estimates for existence; it uses Xu's fixed-point method. Confirm that these are genuinely different approaches.

## Output

# Verification Memo: Coupled Transported-Coefficient Start for ∂ₜg = −2χ²(Ric+g)

Session S0910A03, Step 53 note plus its Step 52 predecessor and the structural-check JSON. I worked each of the seven requested points at the level of the actual computations. Summary first, then the derivations.

**Overall reading.** The pullback identity (point 1) is correct and genuinely repairs the error that Step 52 §5 identified — this is the substantive advance of the note. The transport integration-by-parts (point 4), the I2 factorization (point 5), and the composition regularity (point 6) are individually sound. However, three analytic steps that the closure actually depends on are asserted rather than carried out, and one of them is exactly the place where the transported-coefficient subtlety re-enters. I give the missing computation for each so it can be completed.

---

## 1. Pullback identity — correct, and it fixes the Step 52 §5 error

I verified both halves of the pullback.

**Cutoff transport is stationary along φ.** With φ solving ∂ₜφ = −(âW)∘φ and χ̂ solving ∂ₜχ̂ = âWᵏ∂ₖχ̂,
$$
\tfrac{d}{dt}(\widehat\chi\circ\varphi)
=(\partial_t\widehat\chi)\circ\varphi+(\nabla\widehat\chi\circ\varphi)\cdot\partial_t\varphi
=(\widehat aW^k\partial_k\widehat\chi)\circ\varphi-(\widehat aW^k\partial_k\widehat\chi)\circ\varphi=0.
$$
Hence χ̂∘φ = χ̂(0)∘id = χ and therefore â∘φ = a = χ² for all t. This is the identity the note needs, and it holds precisely because χ̂ is transported by the **same** velocity âW that drives φ.

**Metric pullback.** For φ with velocity field Y = −âW (i.e. ∂ₜφ = Y∘φ),
$$
\partial_t(\varphi^*\widehat g)=\varphi^*(\partial_t\widehat g)+\varphi^*(\mathcal L_{Y}\widehat g)
=\varphi^*\!\bigl(\partial_t\widehat g-\mathcal L_{\widehat aW}\widehat g\bigr)
=\varphi^*\bigl(-2\widehat a(\mathrm{Ric}_{\widehat g}+\widehat g)\bigr).
$$
Using naturality Ric_{φ*ĝ}=φ*Ric_{ĝ} and φ*(â·T)=(â∘φ)φ*T with â∘φ = χ²,
$$
\partial_t g=-2\chi^2(\mathrm{Ric}_g+g),\qquad g=\varphi^*\widehat g .
$$
This is exactly the target flow with a **fixed** χ in geometric coordinates. The Step 52 §5 objection — that φ*(aĝ)=aφ*ĝ is false unless a∘φ=a — is now satisfied by construction, because the transport equation forces a∘φ=a. Point 1 is verified as correct and is the real content of moving from Step 52 §3 to the coupled system.

---

## 2. Principal structure — the "lower-triangular, same order" table is incomplete at one entry

The derivative counts through the principal part (ψ² as a zero-order coefficient of ∇²V) and through the transport commutator (W∼∇V, hence V at order k+1) are correct as stated. But the metric equation as written in (2.1)/(4.1) has dropped a term that carries ∇ψ.

Expanding the Lie derivative of the transported coefficient,
$$
\mathcal L_{\psi^2W}\widehat g=\psi^2\mathcal L_W\widehat g+2\,\mathrm{Sym}\!\bigl(d(\psi^2)\otimes W^\flat\bigr)
=\psi^2\mathcal L_W\widehat g+4\psi\,\mathrm{Sym}(d\psi\otimes W^\flat).
$$
The first piece combines with −2ψ²Ric into Xu's degenerate parabolic form ψ²(ĝ⁻¹*∇²ĝ + D + B). The second piece,
$$
4\psi\,\mathrm{Sym}(d\psi\otimes W^\flat)\quad(\text{schematically }\psi\,\nabla\psi\cdot\nabla V),
$$
does **not** appear in (2.1) or in the frozen equation (4.1). In Xu's fixed-χ setting this term is a fixed smooth coefficient hidden inside B, so it never mattered. Once χ̂ is dynamical it carries a live derivative of the unknown ψ. The §2.1 table row "ψ derivatives needed to affect V at order k: k (through coefficient ψ²)" therefore misses this contribution; the JSON entries `Lie_derivative_psi_order_1` and `psi_not_in_principal_part` register that ∇ψ is present but the closure check in §2.2 does not use them.

Consequently the "same order, no loss" statement for the metric equation is not automatic. Before any integration by parts, the H^{p̃+2} energy of V picks up a term wanting ψ at H^{p̃+3} — one derivative above what the note propagates. See point 3 for how it can still close.

---

## 3. Parabolic gain chain — sound at fixed ε, but the ε→0 use is not yet established

For fixed ε>0 the coefficient ψ²+ε ≥ ε>0 makes the frozen equation strictly parabolic, so V∈C_tH^s∩L²_tH^{s+1} is standard, and the chain
$$
\|\widehat aW\|_{H^s}\le C\|\psi\|_{H^s}^2\|W\|_{H^s},\quad \|W\|_{H^s}\le C\|V\|_{H^{s+1}},\quad
\int_0^T\|\widehat aW\|_{H^s}\,dt\le C\|\psi\|_{C_TH^s}^2\sqrt T\,\|V\|_{L^2_TH^{s+1}}
$$
is correct, and φ∈C_tH^s follows from the H^s-diffeomorphism-group ODE theory (need s>n/2+1, satisfied by s=p̃+2). This same L²_tH^{s+1} gain also rescues the ∇ψ Lie term from point 2: the offending contribution to the metric energy,
$$
\int \partial^\alpha V\,\psi W\,\nabla\partial^\alpha\psi
=-\int(\nabla\partial^\alpha V)\,\psi W\,\partial^\alpha\psi-\int\partial^\alpha V\,\nabla(\psi W)\,\partial^\alpha\psi,
$$
has leading term bounded by ‖V‖_{H^{s+1}}‖ψW‖_{L^∞}‖ψ‖_{H^s}, which Young's inequality absorbs into the parabolic dissipation ½c‖V‖²_{H^{s+1}} plus C‖ψ‖²_{H^s}. So ψ at H^s does suffice — **but only through this IBP + dissipation step**, which the note does not perform. The grading "closes" only with this argument made explicit.

The genuine concern is the ε→0 passage in §4.5. The φ- and ψ-regularity above rests entirely on the L²_tH^{s+1} parabolic gain, whose constant is the ellipticity floor and degenerates as ε→0 and as inf_{supp}ψ²→0 near the interface {ψ=0}. Xu's own ε-independent bounds are C_tH^s bounds coming from the frozen-map ball structure, **not** from the L²_tH^{s+1} smoothing; and in his metric-only problem the diffeomorphism is reconstructed after the limit, so no ε-uniform φ-regularity is needed. Here φ (equivalently χ̂) is part of the coupled unknown, so its ε-uniform high-Sobolev control is required for the coupled Arzelà–Ascoli argument, and that control currently flows through the non-uniform gain. The velocity ψ²W is weighted by ψ², which does vanish on {ψ=0}, so a weighted estimate localizing the gain to {ψ>0} is plausible; but that weighted bound is not in the note. §4.5 as written does not yet justify ε-independent coupled compactness.

---

## 4. Transport integration by parts — correct for the ψ²-coefficient equation

For ∂ₜψ = bʲ∂ⱼψ with velocity b = ψ²W, the top-order energy term is
$$
2\!\int \partial^\alpha\psi\,b^j\partial_j\partial^\alpha\psi
=\int b^j\partial_j(\partial^\alpha\psi)^2
=-\int(\partial_j b^j)(\partial^\alpha\psi)^2,
$$
so the order-(k+1) derivative of ψ is eliminated and only div(ψ²W)∈L^∞ is needed. The ψ² coefficient (rather than a constant) is immaterial: it is part of the velocity b, and IBP only asks that div b be bounded. This matches Proposition 3.1 exactly and (3.1) in the note. The commutator [∂^α, bʲ∂ⱼ]ψ has top term ∂^k(ψ²W)·∂ψ ∼ ψ²∂^{k+1}V·∂ψ, which needs V at order k+1 — again the parabolic gain — consistent with the table's "transport needs V at order k+1." Point 4 is correct.

---

## 5. Contraction and I2 — algebra correct, but one difference term is omitted

The factorization â₁−â₂=(χ̂₁+χ̂₂)(χ̂₁−χ̂₂) is trivially true, and with 0≤χ̂≤1 it gives ‖â₁−â₂‖_{H^{p̃}}≲‖χ̂₁−χ̂₂‖_{H^{p̃}} with multiplier ≤ C(‖χ̂ᵢ‖_{H^{p̃}}) bounded in the ball (Sobolev multiplication, p̃>n/2). Terms (a),(b),(c) in §4.4 are then genuinely proportional to ‖α₁−α₂‖ and ‖U₁−U₂‖ as stated.

The omission is the same Lie term as in point 2. The difference of metric equations contains
$$
4\bigl[\alpha_1\,\mathrm{Sym}(d\alpha_1\otimes W_1^\flat)-\alpha_2\,\mathrm{Sym}(d\alpha_2\otimes W_2^\flat)\bigr]
\ \ni\ \alpha_1\,d(\alpha_1-\alpha_2)\,W_1 ,
$$
i.e. ∇(α₁−α₂) at first order. Measured in the contraction norm H^{p̃}, this ostensibly wants ‖α₁−α₂‖_{H^{p̃+1}} — one derivative above the contraction space. As in point 3 it can be moved by IBP onto ∇𝒲 (the metric difference at order p̃+1) and absorbed into the fixed-ε parabolic dissipation, giving ‖𝒲‖_{H^{p̃+1}}‖α₁−α₂‖_{H^{p̃}} → Young. So the contraction can close **at fixed ε**, where the ε→0 limit is handled separately by compactness rather than by contraction. But §4.4 lists only (a),(b),(c) and does not display this term; the contraction estimates (4.3)–(4.4) are therefore not yet complete as written. This is the "cross-term absorption" that §8 item 1 asks a verifier to confirm — and it needs the extra Lie-difference term added and the IBP shown.

---

## 6. Composition ψ=χ∘φ⁻¹∈H^s — correct by standard diffeomorphism-group theory

With χ smooth and φ an H^s diffeomorphism, s=p̃+2>n/2+1, the inverse φ⁻¹ is H^s and the Moser/Faà-di-Bruno composition estimate gives χ∘φ⁻¹∈H^s, with the leading term (∇χ∘φ⁻¹)∇^sφ⁻¹ controlled by ‖φ⁻¹‖_{H^s}. This is exactly the regularity the table assigns to ψ. The one dependency to keep in view is that φ⁻¹∈H^s comes from φ∈H^s, which comes from ∫‖âW‖_{H^s}dt via the L²_tH^{s+1} gain — so point 6 is correct but inherits the ε-uniformity question of point 3, not an independent difficulty.

---

## 7. The fixed-point method is genuinely distinct from the falsified energy closure

Confirmed. Step 51 attempted existence through a homogeneous inequality E′(t)≤CE(t) on an unshifted critical curvature energy. The flat four-torus test refutes that: with χ=(1+cos x₁)/2 the spatially varying cutoff produces the forcing g⊛Hess a with |g⊛Hess a|²=12(a″)². I reproduced the arithmetic: a″=−(cos x₁+cos 2x₁)/2, ∫₀^{2π}(a″)²=π/2, and ∫_{T⁴}|Rm(t)|² = 12·(2π)³·(π/2)·t² = 48π⁴t², so E′/E=2/t+O(1) — incompatible with E′≤CE. Both the JSON entries and the note match this.

The Xu fixed-point method never invokes such a nonlinear energy closure. It solves an ε-regularized strictly parabolic **linear** frozen problem, iterates via Banach contraction in a lower Sobolev norm inside a bilipschitz high-Sobolev ball, and takes ε→0 by compactness. The g⊛Hess a forcing that broke Step 51 is, in this framework, a bounded inhomogeneity for fixed smooth χ — not an obstruction. So the two approaches are genuinely different, and the flat-torus refutation does not touch the fixed-point route. This part of the note's reasoning is well-founded.

---

## What is established versus what still needs to be written

Established and correct: the pullback identity (1), the transport IBP (4), the I2 coefficient-difference algebra (5), the composition regularity (6), and the separation from the falsified energy closure (7). Together these make the coupled DeTurck system the right object and give a coherent architecture.

Three steps are asserted but not carried out, and each is a place where the transported-coefficient character bites:

- **The ∇ψ Lie term** 4ψ Sym(dψ⊗W♭) is missing from the written metric equation (2.1)/(4.1) and from the §2.2 closure check and §4.4 contraction. It can be handled by transferring its derivative onto V through IBP and absorbing into the parabolic dissipation, but that computation must be added; otherwise the "same order, no loss" grading and estimates (4.3)–(4.4) are not complete.
- **The ε→0 uniformity of φ, χ̂** in high Sobolev norms. The note's diffeomorphism/transport regularity uses the L²_tH^{s+1} parabolic gain, whose constant degenerates as ε→0 and near {ψ=0}. A weighted estimate exploiting that the velocity ψ²W vanishes on {ψ=0} is the natural route, but §4.5's assertion of ε-independent coupled bounds is not yet supported by it.
- **The contraction cross-term** flagged by the note's own §8 item 1: the Lie-difference term needs displaying and its absorption shown at fixed ε.

Finally, the note's §6 already records that even a complete Theorem 5.1 is a per-datum local building block: the terminal spectral density inequality forces δ₀ ≤ c/√A → 0 as topology grows, so the restricted four-dimensional obstruction program does not yield dimension-only constants c₄,C₄, and the positive branch, arbitrary topology, n≥5, and the Lean formalization remain untouched. That structural statement is consistent with the material and is the correct reading of where a proven start theorem would and would not carry the top research target. The JSON's own note that it performs "structural and algebraic checks only" and does not verify PDE existence, Sobolev multiplication, or compactness is accurate — the 19 passed checks confirm bookkeeping, not the analytic closure of the three points above.