# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step40_m2_coupled_continuation_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step27_shifted_curvature_continuation_analysis.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A01/workspace/notes/step37_continuation_theorem_and_first_exit.md",
    "Sessions/S0910A01/trace/ttcs/results/step37_ttcs01_verifier1_integration.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Verify the independent unweighted shifted-curvature derivative ordering needed before the m=2 pair. Determine whether ∇T∈L^q for all finite q follows from the actual T equation under |U| bounded, the m=1 base pair (∇U,∇²χ) finite in all L^q, and T finite in all L^q. Explicitly inspect the Hessian-a and high-cutoff terms, remembering ∇²a=2χ∇²χ+2dχ⊗dχ and that no division by a or fictitious χ factor is allowed. Assess A01's alternative split {χ≥δ}/{χ<δ}: does small C0 metric drift on {χ<δ} imply C^k curvature control there? If not, state the valid integrated route and its exact inputs. The useful output is a rigorous order-one lemma or an exact unresolved term, not a broad summary.

## Output

# Verification memo: order-one unweighted shifted-curvature bound ∇T∈L^q

## Result

The estimate is genuine and provable at order m=1 from exactly the stated inputs. Below is the lemma, its term-by-term derivation showing where every top derivative acquires a χ factor, the two residual products that are bounded by the assumed high-L^q data, and the exact induction ordering. I then show why A01's {χ≥δ}/{χ<δ} split does not deliver ∇^kT control and give the integrated substitute with its precise inputs.

Throughout: closed M^n (empty edge, so one integration by parts leaves no surface contribution), a=χ², U=aT, T=Rm+G, ∇G=0 hence ∇^kT=∇^kRm for k≥1, and the shifted evolution
$$(\partial_t-a\Delta)T=a(T*T+G*T)+(\nabla a)*(\nabla T)+(\nabla^2 a)*T \tag{★}$$
from the shifted note (3.6), with the m=1 differentiated form (3.8):
$$\partial_t V=a\Delta V+\underbrace{\nabla^3a*T}_{F_a}+\underbrace{\nabla^2a*V}_{F_b}+\underbrace{\nabla a*\nabla V}_{F_c}+\text{(reaction)}+\text{(G-terms)},\quad V:=\nabla T. \tag{★★}$$

---

## 1. The order-one lemma

**Lemma.** Let g(t), t∈[τ,T), solve ∂_t g=−2χ²(Ric+g) on closed M^n with χ∈C₀^∞ fixed. Suppose
- (a) sup_{M×[τ,T)}|U|≤K,
- (b) ‖T(t)‖_{L^q} bounded on [τ,T) for every finite q,
- (c) ‖∇²χ(t)‖_{L^q} bounded on [τ,T) for every finite q.

Then ‖∇T(t)‖_{L^q}=‖∇Rm(t)‖_{L^q} is bounded on [τ,T) for every finite q, with constants depending on (g(τ),χ,τ,T,q,K) and the finite norms in (b),(c). No division by a and no inserted χ factor is used.

**Why (a) suffices for the analytic setting.** |aE|=|Ric(U)|≤C_n|U|≤C_nK, so |∂_t g|_g≤CK and e^{−CK(t−τ)}g(τ)≤g(t)≤e^{CK(t−τ)}g(τ). Volumes, L^q norms, |dχ|_{g(t)} and the Sobolev constant are uniformly equivalent to those of g(τ). Also a|T|=|U−aG|≤K+C.

**Test (★★) against P(V)=|V|^{p−2}V.** The only smoothing is the degenerate dissipation D=∫a|∇V|²|V|^{p−2}=∫χ²|∇²T|²|V|^{p−2}, vanishing where χ=0. The decisive structural fact:

> **Every term carrying the top derivative ∇V=∇²T carries a compensating χ.** Such terms arise only from ∇a=2χ∇χ (one χ) and from a=χ² (two χ), and from the single integration by parts of the χ∇³χ*T term which leaves χ∇²χ*∇²T. The Hessian piece dχ⊗dχ of ∇²a=2χ∇²χ+2dχ⊗dχ multiplies only V (order-zero in ∇V), never ∇V. This is exactly what makes the χ²-weighted D sufficient.

Term accounting:

- **Diffusion IBP remainder** ∫P(V)∇a·∇V=∫|V|^{p−2}V·2χ∇χ·∇V ≤ εD+C_ε∫|∇χ|²|V|^p (using |∇a|²/a=4|∇χ|²). Absorbed.
- **F_c=2χ∇χ*∇V**: same form, ≤ εD+C_ε∫|∇χ|²|V|^p. Absorbed.
- **F_b=(2χ∇²χ+2dχ⊗dχ)*V**. The dχ⊗dχ part gives ∫|dχ|²|V|^p≤C∫|V|^p (order-zero in ∇V, bounded coefficient — the missing χ is harmless here). The χ∇²χ part is the signed form ∫χ∇_i∇_jχ·B^{ij}(V), |B|≲|V|^p, |∇B|≲|V|^{p−1}|∇V|; one IBP gives ≤ εD+C_ε‖dχ‖_∞²∫|V|^p.
- **F_a=∇³a*T ⊃ 2χ∇³χ*T** (the only ∇³χ). Write ∇³χ=∇(∇²χ) and integrate once:
$$\int|V|^{p-2}V\,\chi\,\nabla^3\chi\,T=-\int(\nabla P(V))\chi T\nabla^2\chi-\int P(V)\nabla\chi\,T\nabla^2\chi-\int P(V)\chi(\nabla T)\nabla^2\chi.$$
  - First: χ|∇V||V|^{p−2}·|T||∇²χ| ≤ εD + C_ε∫|∇²χ|²|T|²|V|^{p−2}. (See §2.)
  - Second: ∫|V|^{p−1}|∇χ||T||∇²χ| ≤ C(1+‖V‖_p^p) by Hölder. (See §2.)
  - Third: ∇T=V, so this is ∫χ∇²χ|V|^p in signed form again ≤ εD+C∫|∇χ|²|V|^p.
- **Reaction ∇(aT*T)=∇a*T*T+a*∇T*T+a*T*∇T**. Top curvature derivative is only ∇T=V (order 1), never ∇²T. Each term: χ∇χ*T² gives ∫|∇χ||T|²|V|^{p−1} bounded; a*V*T gives ∫a|T||V|^p≤(K+C)∫|V|^p. The [∇,∂_t] commutator (∂_tΓ=∇U schematically) produces ∇U*T=(2χ∇χ*T+aV)*T, both handled identically.
- **G-terms ∇a*G*T+a*G*∇T**: 2χ∇χ*G*T order-zero bounded; χ²G*V gives ∫χ²|G||V|^p≤C∫|V|^p.

Assembling: d/dt∫|V|^p + cD ≤ C(1+∫|V|^p) with C depending on the finite norms in (a),(b),(c). Grönwall on [τ,T) gives the conclusion. Where χ=0 the metric is stationary and ∇T is frozen at its smooth initial value, so nothing grows off supp χ. ∎

---

## 2. The exact terms that are bounded, not absorbed

Two residual products carry the entire dependence on (b),(c). They are:
$$\int_M|\nabla^2\chi|^2\,|T|^2\,|\nabla T|^{p-2}\,d\mu,\qquad \int_M|\nabla\chi|\,|\nabla^2\chi|\,|T|\,|\nabla T|^{p-1}\,d\mu.$$
By Hölder with the running family of large exponents, the first is ≤ ‖∇²χ‖_{2q₁}²‖T‖_{2q₂}²‖V‖_p^{p−2} and the second ≤ ‖∇χ‖_∞‖∇²χ‖_{q₃}‖T‖_{q₄}‖V‖_p^{p−1}, both finite by (b),(c) and bounded by C(1+‖V‖_p^p). These are the shifted analogues of the single residual term Wang leaves in Proposition 4.14 (his ∇²χ*∇^mχ*χ²Rm), specialized to m=1. No term requires ‖∇²T‖ in L^q, and no term requires a prior ‖∇U‖ bound; ∇U=2χ∇χ*T+aV is a posteriori controlled by (b) and the conclusion.

---

## 3. Exact inputs and the induction ordering

The order-one estimate uses only (a),(b),(c). Cutoff jet (c) at order m+1=2 is itself produced one level down: ∂_t∇²χ=g^{-1}*∇U*∇χ, so ‖∇²χ‖ closes with ‖∇U‖ through the coupled base pair (shifted note (7.4)–(7.5)). Hence the operative order-m triple is Wang's Remark 4.2 with χ²Rm→U, Rm→T:
$$\nabla^{m-1}T \Rightarrow \nabla^m\chi,\qquad \nabla^m\chi \Rightarrow \nabla^{m-1}U,\qquad (\nabla^{m+1}\chi,\ \nabla^{m-1}T)\Rightarrow \nabla^mU,$$
and the general unweighted arrow **(∇^{m-1}T needs ∇^mχ and lower ∇T)** is exactly the order-one lemma above at its base m=1: ∇T needs ∇²χ (=∇^{m+1}χ) and T (=∇^0). The general-m version repeats §1 verbatim: the χ∇^{m+2}χ*T term integrates once to χ∇^{m+1}χ*∇^{m+1}T (absorbed by D) plus ∇^{m+1}χ and ∇²χ*∇^mχ*T residuals bounded by high-L^q cutoff jets and lower ∇T. Inputs for order m: (a) sup|U|≤K; (b) ‖∇^jT‖_{L^q}<∞, j≤m−1; (c) ‖∇^jχ‖_{L^q}<∞, j≤m+1; closed M.

This lemma is precisely the object called "normalized Wang Proposition 4.13 analogue at order one, ∇T∈L^q" and listed as an unfilled dependency in the Step 40 note (1.1) and the Step 27 note (§5, item 2). It is now supplied, and it is an independent integrated estimate — it is **not** obtained from the incorrect assertion (1.2) that every derivative of a=χ² carries a χ.

---

## 4. A01's {χ≥δ}/{χ<δ} split does not give ∇^kT control

Lemma 1.2a (Step 37) is not valid on the degenerate region, for two independent reasons.

**(i) The drift bound has no δ smallness.** A01 writes |g(t)−g(τ)|≤2∫|aE|ds≤2χ²K(T−τ)≤2δ²K(T−τ) on {χ<δ}, treating K as a bound on the unweighted |E|. But K bounds the weighted |U|=|χ²(Rm+G)|, and |aE|=|Ric(U)|≤C_n|U|≤C_nK uniformly on all of M, with no extra χ² factor. On {χ<δ} the unweighted |Rm| can be as large as δ^{−2}K, so |E|~δ^{−2}K and χ²|E|~K, not δ²K. The δ² is fictitious — the same "missing χ" the Step 27/40 notes warn against, and the same error already withdrawn in A01's own "Step 38 superseding correction" at the head of the file ("|aE|=|Ric(U)|≤CK, not an extra χ²K factor"). Lemma 1.2a reintroduces exactly that withdrawn δ²K drift.

**(ii) C⁰ metric closeness does not bound curvature.** Even granting small pointwise |g(t)−g(τ)|, curvature depends on two spatial derivatives of g and ∇^kRm on k+2 derivatives. Control of ‖g(t)−g(τ)‖_{C⁰} says nothing about ∇^j(g(t)−g(τ)) for j≥1. To conclude ‖∇^kRm(t)‖ close to ‖∇^kRm(τ)‖ one would need ‖g(t)−g(τ)‖_{C^{k+2}}, i.e., bounds on the top spatial derivatives of the perturbation, which the velocity −2χ²E does not supply on {χ<δ} (its own spatial derivatives there involve ∇²a=2χ∇²χ+2dχ⊗dχ contracted with unweighted E, again without a saving χ). So the {χ<δ} branch does not hold.

**Correct integrated route.** Do not split space and do not divide by a. Prove ‖∇^mT‖_{L^q} by the whole-manifold energy estimate on (3.8) exactly as in §1/§3: the single χ²-weighted dissipation absorbs every top-derivative term because each such term carries a χ, the lone ∇^{m+2}χ integrates once down to ∇^{m+1}χ, and the residuals are bounded by high-L^q cutoff jets and lower curvature derivatives. Exact inputs are (a),(b),(c) of §3; the order-one instance is the Lemma of §1.

---

## 5. Status of adjacent pieces (for placement)

- The Section 6 base estimate ‖T‖_{L^q}<∞ (input (b)) is the m=0 analogue and is derived by the same χ-bookkeeping on (★): the sole ∇²a*T term integrates once, |∇a|²/a=4|∇χ|² absorbs, giving d/dt∫|T|^p+cD≤C∫|T|^p. This one is sound as written and is the correct starting point.
- Input (c), the base pair (∇U,∇²χ), is assumed here. Its own derivation in Step 37 (1.14)/shifted (7.1) still has the internal wording matter flagged in the A01 integration memo (§2.2): the top cutoff line is written with ∇^kRm where the shifted structure requires ∇^kU. That must be settled independently; it does not affect the order-one unweighted lemma once (c) is in hand, but the whole tower rests on it.
- With the order-one lemma established, the m=2 coupled mechanism of the Step 40 note has its stated prerequisite (1.1) filled. The remaining unfilled objects for a full continuation statement are unchanged: the arbitrary-m residual exponent schedule, the shifted Proposition 4.3 smooth terminal reconstruction, and normalized transported-DeTurck short-time existence.

**Net.** The requested order-one object exists and is proved from (a),(b),(c) with no division by a and no inserted χ; its two load-bearing residual integrals are the ones displayed in §2. The A01 spatial split is not a valid substitute — both its δ² drift and its C⁰→C^k curvature inference break — and the integrated energy route above is the correct replacement.