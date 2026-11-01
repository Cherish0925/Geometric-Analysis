# TTCS Independent Branch Record

```json
{
  "step_id": 30,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md"
  ]
}
```

## Task

Adversarially verify the claimed smooth-extension proof for the normalized fixed-cutoff flow ∂_t g=-2χ²(Ric+g), focusing only on the high-order Wang induction. Read Wang's actual Section 4 source and the Codex/A03 shifted-curvature derivations. Determine whether the grouped Γ1–Γ4 integrations really bound ∇^m U using cutoff derivatives only through order m (not m+1 or m+2), without dividing by χ or assuming hidden pointwise bounds. Expand the dangerous terms sufficiently to expose any unmatched factor, state a valid finite Hölder-exponent schedule if it closes, and classify the new G-linear terms exactly. If the source itself has a gap, identify it precisely rather than inheriting it. The scientific output should be a rigorous lemma/proof or a concrete obstruction.

## Output

## Verification memo: high-order Wang induction for ∂_t g = −2χ²(Ric+g)

### 1. Headline finding

The central technical assertion under test is the one in `shifted_curvature_continuation.md` §7.3 / eq. (7.12): that the grouped Γ₁–Γ₄ energy estimate bounds ∇ᵐU using cutoff derivatives **only through order m**, so that "neither ∇^{m+2}χ nor ∇^{m+1}χ is an input to the A_m estimate."

**This assertion is false.** The ∇ᵐU energy at level m genuinely requires ‖∇^{m+1}χ‖_{Lᵖ} (cutoff order m+1), and no reorganization of the integrations lowers it to order m without dividing by χ. The accurate bookkeeping is the one in `step27_...md` (eq. (3.6), (6.3), (6.7): "∇ᵐU ↔ ∇^{m+1}χ").

Importantly, **the theorem itself is not endangered.** With the order-(m+1) accounting the induction still closes, because ∇^{m+1}χ is controlled simultaneously with ∇ᵐU through a coupled Grönwall estimate — exactly the mechanism Wang uses at m=1 in his Lemma 4.11 and that `step27` reproduces in Move A. The two A03 notes reach the same correct extension result; `shifted_...md` §7.3 contains an incorrect tightening of the order count, in internal contradiction with its own §7.1 (which explicitly uses ∇²χ = ∇^{m+1}χ at m=1).

### 2. The decisive expansion: an unmatched ∇^{m+1}χ factor

Write V = ∇ᵐU, U = χ²T̃, D_m = ∫χ²|∇V|²|V|^{p-2}dμ (the only diffusion available at this energy level; the parabolic term supplies −c D_m). The four allocations of `(4.2)` are:

Γ₁ = χ∇^{m+2}χ*U, Γ₂ = ∇χ*∇^{m+1}χ*U, Γ₃ = χ∇^{m+1}χ*∇U, Γ₄ = χ∇χ*∇^{m+1}U.

**Γ₂ is a raw term, not created by an integration by parts**, and it is the cleanest obstruction. Testing against |V|^{p-2}V and using |U| = χ²|T̃| ≤ K (from (1.2)) and |∇χ| ≤ C:

  ∫|V|^{p-2}⟨V, ∇χ*∇^{m+1}χ*U⟩ ≲ K C ∫|V|^{p-1}|∇^{m+1}χ| ≤ C‖V‖_p^{p-1}‖∇^{m+1}χ‖_p.

There is a bare ∇^{m+1}χ and nothing to pair it against except V itself. To reduce it to ∇ᵐχ one must integrate by parts off ∇^{m+1}χ = ∇(∇ᵐχ):

  = −∫∇[|V|^{p-2}V*∇χ*U]*∇ᵐχ,

whose leading piece is ∫|V|^{p-2}(∇V)*∇χ*U*∇ᵐχ. Here ∇V is **unweighted**: the χ² of U sits on the T̃ factor, not on ∇V. To absorb ∇V into D_m one needs χ|∇V|, i.e. one must write |∇V||∇χ| = (χ|∇V|)(|∇χ|/χ). The factor |∇χ|/χ is unbounded on the zero set of χ. **Reducing Γ₂ below order m+1 therefore requires exactly the division by χ that the construction forbids.** Γ₃ = χ∇^{m+1}χ*∇U has the same structure (∇U is low order, Sobolev-bounded), and likewise supplies an irreducible ‖∇^{m+1}χ‖_p.

Γ₁ tells the same story. One integration by parts off ∇^{m+2}χ produces the piece

  Γ₁ₐ = −(p−1)∫|V|^{p-2}(∇V)*χ*U*∇^{m+1}χ,

whose ∇V **does** carry a χ (good for absorption). Young gives ε D_m + C∫|U|²|∇^{m+1}χ|²|V|^{p-2} ≤ ε D_m + CK²‖∇^{m+1}χ‖_p²‖V‖_p^{p-2}. The residual is order m+1. A second integration by parts to reach ∇ᵐχ would move the derivative onto ∇V, producing ∇²V = ∇^{m+2}U, which the |V|ᵖ energy does not control (only ∇V is controlled, via D_m). So no legitimate route lowers Γ₁ₐ to order m either.

Conclusion: Γ₂, Γ₃, and the ∇V-piece of Γ₁ each independently force cutoff order m+1. This is robust to any cancellation among the Γ's, since Γ₂ alone is decisive.

### 3. Reading of the source (Wang Prop. 4.14 vs. Lemma 4.11)

Wang's Prop. 4.14 states that after integrating Γ₁,Γ₂,Γ₃ the only surviving term is ∇²χ*∇ᵐχ*(χ²Ric) (order m), with everything else "controlled in the way we control Γ₄" (i.e. absorbed by diffusion). The expansion above shows this prose is **incomplete**: Γ₂ and Γ₃ are raw ∇^{m+1}χ terms that are neither of order m nor absorbable like Γ₄, and Γ₁ₐ leaves a |∇^{m+1}χ|² residual. Prop. 4.14's stated induction inventory (|∇ᵏχ|_q for k≤m only) does not supply ∇^{m+1}χ.

The correct mechanism is visible in Wang's **Lemma 4.11 itself** (the m=1 instance): his I₁ estimate keeps the residual C∫|∇²χ|²|χ²Ric|²|∇(χ²Rm)|^{p-2}, i.e. |∇^{m+1}χ|² with m=1, and Lemma 4.11's conclusion bounds ∇²χ **jointly with** ∇(χ²Rm) as a coupled pair. So Wang's real argument is coupled at order m+1; Prop. 4.14's summary sentence understates the cutoff order actually used. This is a write-up imprecision in the source, correctly resolved by the coupling, not a defect in the theorem. `shifted_...md` §7.3 inherited and amplified the understatement into a false order-m assertion; `step27` corrected it.

### 4. Corrected lemma and closing of the induction

For large q set A_m(q)=sup_{t<T}‖∇ᵐU‖_q, B_m(q)=sup‖∇ᵐT̃‖_q, C_m(q)=sup‖∇ᵐχ‖_q. The accurate dependency at level m is

  B_{m−1} ⟶ { A_m together with C_{m+1} } ⟶ B_m,

with A_m and C_{m+1} solved **simultaneously**. The two coupled inequalities are, for fixed p>max(n,2):

(I)  d/dt‖∇ᵐU‖_p^p + c D_m ≤ C(1 + ‖∇ᵐU‖_p^p + ‖∇^{m+1}χ‖_p^p),

obtained by bounding Γ₂,Γ₃ and the Γ₁ₐ residual via Young (each ≤ C(‖V‖_p^p + ‖∇^{m+1}χ‖_p^p)), Γ₄ via ε D_m, and all reaction terms via §5 below;

(II) d/dt‖∇^{m+1}χ‖_p^p ≤ C(1 + ‖∇^{m+1}χ‖_p^p + ‖∇ᵐU‖_p^p),

from the cutoff evolution ∂_t|∇^{m+1}χ| ≤ CK|∇^{m+1}χ| + C∑_{s=1}^{m}|∇ˢU||∇^{m+1−s}χ|, whose highest-current input is |∇ᵐU||∇χ| (Hölder with ‖∇χ‖_∞), all lower cutoff orders ∇ᵏχ (k≤m) being already fixed at the previous level.

Adding (I)+(II) with y = ‖∇ᵐU‖_p^p + ‖∇^{m+1}χ‖_p^p gives y′ + c D_m ≤ C(1+y); on a finite interval [0,T) Grönwall bounds y. Then B_m is bounded from (3.1) using C_{m+1} (now available) and B_{≤m−1}; its raw top term χ∇^{m+2}χ*T̃ likewise reduces to a controllable ∇^{m+1}χ residual (T̃ in high L^q from the base Lᵖ estimate) — consistent with Wang Prop. 4.13's stated inventory ∇ⁱχ, i≤m+1. Sobolev then upgrades to the pointwise bound. The ordering is acyclic; no ∇^{m+1}U or ∇^{m+2}χ is ever an input, and χ is never inverted.

The critical structural point: C_{m+1}'s evolution needs only A_m (current) and lower, so the A_m–C_{m+1} coupling is genuinely closed rather than circular; this is what makes order m+1 harmless.

### 5. A valid finite Hölder-exponent schedule

Run the induction simultaneously for all exponents q ∈ [p₀, ∞), p₀ > max(n,2). At level m the reaction terms are ∑_{i+j+k=m, k≤m−1}∇ⁱa*∇ʲU*∇ᵏT̃ plus U*∇ᵐU and the G-terms. The single term with a top curvature derivative is U*∇ᵐU = U*V (|U|≤K, linear ⇒ C‖V‖_p^p). Every other reaction factor has order ≤ m−1, hence lies in every L^q by the previous levels plus Sobolev. Testing against |V|^{p-2}V, place V in Lᵖ (exponent (p−1)/p on |V|^{p-1}) and each lower factor in L^{3p}; Hölder with 1/p = (p−1)/p·1/p + 3·(1/(3p)) closes and yields C(1+‖V‖_p^p). Because only finitely many product templates occur at each m, a finite descending family of exponents (all > p₀) suffices per level, and "finite in every L^q, q≥p₀" is preserved through the m-induction and the Sobolev upgrade. This is precisely Wang's staggered-exponent device with unchanged principal structure; only coefficients differ.

### 6. Exact classification of the G-linear terms

The normalization contributes, in the T̃ equation (3.1), ∑_{i+k=m}∇ⁱa*G*∇ᵏT̃, and in the U equation (4.1) the set 𝒩_m = ∑_{i+j=m}∇ⁱa*G*∇ʲU plus the aG*U reaction of (2.8). Every such monomial factors as (cutoff jet ∇ⁱa of order ≤ m)·(the parallel bounded tensor G)·(∇ʲU or ∇ᵏT̃ of order ≤ m).

- **j = m (or k = m):** coefficient aG with |aG| ≤ C_n‖a‖_∞, linear in the current derivative ⇒ contribution C‖V‖_p^p. No derivative to absorb, no new node in the dependency graph.
- **j < m (or k < m):** ∇ⁱa (i ≥ 1, cutoff order ≤ m, available) × G × lower U/T̃ derivative (available) ⇒ Hölder+Young ≤ C(1+‖V‖_p^p).

They are strictly benign because **∇G = 0** (2.5): differentiating G yields nothing, so all derivatives fall on a or on the curvature variable, preserving Wang's triangular derivative dependence. They never demand ∇^{m+2}χ, never require the χ²-diffusion for absorption, and never raise the highest derivative order.

The related algebraic point (2.5)–(2.7) is correct and load-bearing: because E = Ric(T̃) and ∂_tG = −(2a/(n−1))E⋏g, every right-hand term of the shifted evolution (2.6) contains T̃ or its derivative; there is **no bare (∇²a)*G source**. Equivalently, T̃ = 0 ⇔ Ric = −g is stationary, so the reaction vanishes there and is bounded by C_n(|T̃|+|T̃|²), not by a forced constant.

### 7. On the shift's necessity

The parallel shift T̃ = Rm + G, U = aT̃ makes ∂_t g = −2Ric(U) (2.11), so ∂_tΓ = g⁻¹*∇Ric(U) ∼ ∇U is a first derivative of U with no separate branch. This keeps the cutoff evolution exactly triangular and lets Wang's contraction-preserving integrations transfer verbatim. The device is sound. It is a clarity/triangularity convenience rather than a strict necessity: in the unshifted normalized flow the extra +g in the velocity injects a (∇²a)*g source into ∂_t Rm (from ∇²(ag) = (∇²a)*g), whose curvature factor is the bounded tensor g — this would still absorb after one integration by parts, but would add ∇a*g branches to the cutoff evolution that obscure the count. The shift removes them at the cost only of the benign G-terms of §6.

### 8. What remains

The corrected lemma establishes: if sup_{M×[0,T)}|χ²Rm|_g < ∞ then every ∇ᵐ(χ²Rm) is bounded, g(t) has a smooth positive-definite limit at T, and the flow restarts (the transported-coefficient DeTurck restart of §8/§7 changes only the zeroth-order part of Yang's regularized parabolic system and is unaffected by this analysis). Constants depend on (M,g₀,χ,T) and on the bound in (1.2); this is what the first-exit continuation uses.

Two items are worth stating precisely as unresolved at the level of this memo:

1. The restart's short-time construction for the degenerate coefficient a = χ² (a vanishing on part of M) is asserted to follow Yang's regularization "changing only the zeroth-order part." This memo verified only the a priori derivative induction; the degenerate-coefficient existence/limit passage of (8.4)–(8.7) was not re-derived here and should be read against Yang §8 in its own right.

2. As `step27` §9 itself records, this extension result is one component; the surrounding Ricci-pinching gap argument (selected-support construction, terminal calibration, smooth-limit passage, the positive branch, n≥5, the dimension-only quantifiers, and the Lean formalization) is not addressed by the induction verified here.

The narrow question posed is settled: the grouped Γ₁–Γ₄ integrations do **not** close at cutoff order m; they close at order m+1, without inverting χ, via the A_m–C_{m+1} coupled Grönwall. `shifted_...md` §7.3 should be reconciled with `step27` §3/§6 and with Wang's Lemma 4.11 before any downstream chain relies on the order-m statement.