# TTCS Independent Branch Record

```json
{
  "step_id": 27,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md",
    "Sessions/S0910A03/workspace/notes/step27_shifted_curvature_continuation_analysis.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Resolve one exact derivative-index discrepancy that emerged after the prior review. Wang Proposition 4.14 assumes cutoff derivatives only through order m when proving an L^p bound for ∇^m(χ²Rm), even though its raw Γ1,Γ2,Γ3 terms contain χ∇^{m+2}χ·U, ∇χ∇^{m+1}χ·U, and χ∇^{m+1}χ·∇U. The Step 27 theorem draft instead introduced a current-order pair ∇^mU ↔ ∇^{m+1}χ after only one integration by parts. Read Wang lines 622–659 and the shifted-curvature equations. Determine which dependency is actually justified. Reconstruct the grouped integration-by-parts reduction of Γ1–Γ3 far enough to show whether all ∇^{m+1}χ terms reduce to diffusion-controlled terms plus ∇²χ·∇^mχ·U (as Wang states), or whether Wang implicitly needs ∇^{m+1}χ/current Volterra closure. Then state the correct induction order for shifted T=Rm+G, U=aT, and identify any exact coefficient/cancellation needed rather than relying only on schematic stars.

## Output

# Verification Memo — Wang Prop. 4.14 cutoff-index vs. Step 27 shifted-curvature pair

## Bottom line

The two descriptions are not describing the same residual, and once the integration by parts is done explicitly the arithmetic decides cleanly in favor of the Step 27 draft. The current-order pair **∇^mU ↔ ∇^{m+1}χ** is the dependency that the energy estimate actually produces. Wang's Prop. 4.14 phrase "leftover = ∇²χ\*∇^mχ\*χ²Rm" names only *one* of the residuals (the one born from the `∇χ*∇^{m+1}χ` piece); the residual born from the genuine top term `χ∇^{m+2}χ*U` is order m+1 in χ and requires the coupled Volterra closure that Wang writes out fully only in his base case (Lemma 4.11 with the pair {∇(χ²Rm), ∇²χ} closed by Lemma 4.8). So Wang implicitly needs the ∇^{m+1}χ current closure at every level; his Prop. 4.14 prose compresses it. The draft's own §3.5–3.6 is the correct exhibition.

## Reconstruction of the top-term reduction

Write W = ∇^m(χ²Rm) (Wang) or W = ∇^mU (draft). The dangerous source is the k=0 monomial of Wang Lemma 4.5's first sum,
Γ₁ = ∫|W|^{p-2}⟨W, χ∇^{m+2}χ · χ²Rm⟩,
which is `χ∇^{m+2}χ*U` in the draft (eq. 3.3). One integration by parts on ∇^{m+2}χ = ∇(∇^{m+1}χ) gives exactly the draft's eq. (3.5), three terms:

- (a) ∇(|W|^{p-2}W) · χ∇^{m+1}χ · U → the derivative on W yields ∇^{m+1}(χ²Rm)=∇W. Cauchy–Schwarz against the diffusion ∫a|∇W|²|W|^{p-2} (the matching single χ = √a is essential here) leaves
  **ε·diffusion + C∫|U|²|∇^{m+1}χ|²|W|^{p-2}** — an order-(m+1) cutoff residual, quadratic in ∇^{m+1}χ. This is draft eq. (3.6).
- (b) |W|^{p-2}W · ∇χ · ∇^{m+1}χ · U and (c) |W|^{p-2}W · χ∇^{m+1}χ · ∇U — both linear in ∇^{m+1}χ, order m+1.

None of (a)–(c) is ∇²χ\*∇^mχ. That structure appears instead when one integrates by parts the *separate* Γ₂ = ∫|W|^{p-2}⟨W, ∇χ·∇^{m+1}χ·U⟩ (Wang's Γ₂): its middle residual is precisely `∇²χ*∇^mχ*U`. So Wang's named leftover is real but is the Γ₂ residual, not the Γ₁ residual. The base case confirms the reading exactly: for m=1 Wang writes I₁ out in full, and its first post-IBP term is ⟨∇²(χ²Rm), χ∇²χ\*(χ²Ric)⟩, i.e. |∇²χ|² = |∇^{m+1}χ|² for m=1, kept as a coupled unknown through Lemma 4.8. The same |∇^{m+1}χ|² residual is present for every m; there is no algebraic move turning ∇^{m+1}χ (one factor, order m+1) into ∇²χ⊗∇^mχ (two factors, orders 2 and m). A single integration by parts cannot descend from order m+2 to order m without producing ∇²W, which the first-order diffusion energy does not control. Hence order m+1 is unavoidable, and the coupling is genuine.

That the coupling closes: |∇^{m+1}χ| evolves (Lemma 4.6 analog, draft 4.4–4.5) with top input |∇^m(χ²Ric)| = |Ric(∇^mU)|, i.e. the current ∇^mU; and the ∇^mU energy feeds on |∇^{m+1}χ|² with coefficient |U|²≤K². The pair {|∇^mU|_p², |∇^{m+1}χ|_p²} satisfies Wang's Lemma 4.8 Volterra inequality Y' ≤ C(1+Y+∫₀ᵗY), closing on [0,T) with (g₀,χ,T,p,K)-dependent constants. This is exactly the draft's Move A (eq. 6.4). So the current-order pair is both forced and sufficient.

## Correct induction order (shifted T = Rm+G, U = aT, a = χ²)

Per level m, with lower levels (|∇^ℓU|, |∇^ℓT| for ℓ≤m−1, |∇^rχ| for r≤m) already bounded in the required finite-p spaces, plus the two global facts |U|≤K and sup_t‖T(t)‖_{L^p}<∞ for every finite p (draft eq. 5.4):

1. **Unweighted ∇^{m-1}T first.** Its top cutoff source χ∇^{m+1}χ\*T loses one derivative under the energy IBP and uses only ∇^mχ, available from the previous level's step 3. Connection-commutator terms Ric(∇^{m-1}U)\*T are Hölder-controlled by |∇^{m-1}U|_{p₁} and ‖T‖_{p₂} (eq. 5.4); no unweighted L^∞ curvature is used.
2. **Current coupled pair {∇^mU, ∇^{m+1}χ}.** The Γ₁ reduction above plus the ∇^{m+1}χ evolution close by Lemma 4.8. All G-monomials contribute either a bounded-linear coefficient times the current ∇^mU or previously bounded lower derivatives.
3. **Current unweighted ∇^mT**, then Sobolev upgrade (exponents >n) to the L^∞ bounds.

Wang's Remark 4.2 chain ("∇^m(χ²Rm) ← ∇^{m-1}Rm ← ∇^mχ ← ∇^{m-1}(χ²Rm)") is the same cycle read one notch lower; the honest cutoff order entering the ∇^mU estimate is m+1, coupled, not m. The draft's §3 dependency triangle and §6.7 statement "∇^mU ↔ ∇^{m+1}χ, ∇^{m-1}T uses only ∇^mχ" are the correct rendering.

## Exact ingredients that must not stay schematic

These are the places where the shift earns its keep, verified beyond the stars:

- **∇G = 0 exactly** (metric compatibility) ⇒ ∇^rT = ∇^rRm for r≥1 with no lower-order corrections (draft 1.3, 2.3). This is why the differentiated shifted system (3.1/2.3) has Wang's exact cutoff placement.
- **Ric(G) = g exactly.** In the full-velocity source ∇²a\*E with E = Ric+g, writing E = Ric(T) makes the potential ∇²a\*g piece cancel: ∇²a\*Ric = ∇²a\*(Ric(T)−g), so ∇²a\*E = ∇²a\*Ric(T). There is no independent ∇²a\*G source. Equivalently, at T=0 one has Rm=−G, Ric=−g, E=0, flow stationary, so the algebraic reaction vanishes at T=0 and is bounded by C_n(|T|+|T|²) (draft 2.7) with **no forced constant**. I checked this cancellation both ways; it is the analytic content of the shift.
- **a = χ² exactly** ⇒ √a = χ smooth, and ∇^{m+2}(χ²) = 2χ∇^{m+2}χ + 2∇χ\*∇^{m+1}χ + Σ_{2≤i≤m}∇^iχ\*∇^{m+2−i}χ. Only the leading **2χ∇^{m+2}χ** (single χ) matches the diffusion weight for the clean Γ₁ Cauchy–Schwarz. The identities da⊗da/a = 4dχ⊗dχ and |da|²T = 4|dχ|²U extend across {a=0} with no division by a (draft 2.8, 5.2).
- **The no-χ residuals** (from the 2∇χ\*∇^{m+1}χ term and the dχ⊗dχ part of ∇²a) carry the weighted factor U = χ²Rm and are estimated in L^p using the global finite-p bound (5.4), never by a pointwise 1/χ. A naive pointwise Cauchy–Schwarz here would produce |∇χ|²/χ² and appear singular; the correct estimate keeps everything in L^p, where ‖Rm‖_{L^p}<∞ globally (including the stationary region outside supp χ, where Rm is the fixed initial curvature). This is Wang's staggered-exponent device and is load-bearing.
- **Coupling coefficient |U|² = |aT|² ≤ K² finite exactly by hypothesis (1.2)**, and the reaction regrouping aT\*T = U\*T (coefficient |U|≤K) keeps the reaction linear in the remaining T. Eq. (5.4) itself closes by Gronwall because both diffusion weight a and reaction coefficient a vanish together on {χ=0}, where the flow is stationary.

## What remains to make the transfer a theorem rather than a mechanism

The draft states (both notes, §5/§9) that the full carry-through of the G-monomials 𝓛_{G,m} through Wang Lemmas 4.11 and 4.13–4.14 is still at the level of "same three families." The stationarity argument pins the zeroth-order reaction (no forced constant) and the exact contraction Ric(∇^qU) = ∇^q(aE), but an explicit per-order accounting that each 𝓛_{G,m} monomial is (i) a bounded-linear coefficient times the current derivative or (ii) a strictly lower derivative already in (6.1) would remove the last schematic step, especially for the ∇^{m+1}χ linear residuals (b),(c) whose exponents must be assigned from the m=1 base and its Sobolev upgrades. This is a bookkeeping task, not a mechanism question; the mechanism is sound.

Two orientation points, from the draft's own closing sections and consistent with the material: the Volterra constants depend on (g₀,χ,T,K) and are not uniform across a pinching sequence, so this per-flow continuation feeds sequence-uniform higher jets only on the a=1 plateau (draft §8, §7); and the whole extension result addresses the four-dimensional continuation subproblem, not the dimension-only interval quantifiers of the Yau-26 statement.

I did not re-derive Wang's Perelman-pseudolocality Sections 1–3 or the Yang short-time construction; the present question lives entirely in Section 4's derivative induction and the shifted-tensor algebra, and those are what I checked.