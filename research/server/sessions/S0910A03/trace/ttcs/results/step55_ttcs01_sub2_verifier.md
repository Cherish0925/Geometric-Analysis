# TTCS Independent Branch Record

```json
{
  "step_id": 55,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step55_direct_nonlinear_flow_construction.md",
    "Sessions/S0910A03/workspace/notes/step54_exact_synchronized_output_ledger.md",
    "Sessions/S0910A03/workspace/notes/step54_route_reassessment_and_joint_weighted_iteration.md"
  ]
}
```

## Task

Verify the direct nonlinear construction for the normalized cutoff flow ∂_tg = -2χ²(Ric+g) presented in the attached note. The construction uses ε-regularization of the coupled DeTurck metric equation + transported cutoff β, standard quasilinear parabolic theory for ε>0, ε-uniform joint H^s energy estimates, and compactness for ε→0.

Focus on these load-bearing mathematical claims:

1. JOINT H^s ENERGY (Proposition 3.1): The cross-coupling between metric and transport equations closes. Specifically, the transport top term β²·D^sW(G)·Dβ (which involves D^{s+1}G) when tested against D^sβ gives ∫β|D^sβ|·β|D^{s+1}G|·|Dβ|, claimed to be absorbed by the metric dissipation (β²+ε)|D^{s+1}G|². Check: does Cauchy-Schwarz work here? Is the β² factor correct or do we need β²+ε?

2. DIFFERENCE ESTIMATE (Proposition 4.1): At r=s-2, the coefficient difference (β₁²-β₂²)G₁⁻¹D²G₁ is bounded in H^r by C_R‖ω‖_{H^r} using the individual H^s ball. Check: at the top level, the product ω·D^sG₁ needs ‖ω‖_∞·‖D^sG₁‖_2; does Sobolev embedding H^r ↪ L^∞ hold for r>n/2? Is the Q-type antisymmetric identity ∫h·a·Dh = -½∫|h|²·Da correctly applied to the actual DeTurck Q-tensor?

3. PULLBACK IDENTITY (Proposition 7.1): The claim is β₀(t,φ(t,x))=χ(x) from f'(t)=0. Then the Lie derivative cancellation β₀²=χ_E² on the image of φ. Check: is the Eulerian velocity formula correct? Does the pullback of the scalar-weighted tensor -2β²(Ric+G) correctly give -2χ²(Ric(g)+g)?

4. ε→0 PASSAGE: ε·G_ε⁻¹D²G_ε → 0 as ε→0. The all-order ε-uniform hierarchy gives C^∞ compactness. Check: is the uniqueness argument for ε=0 valid? The Grönwall holds without the dissipation term, but the equation is degenerate; does the H^r framework still apply to non-uniformly-parabolic equations?

5. ZERO-SET REGULARITY: The solution is claimed smooth across ∂{χ>0} because it's a C^∞ limit of smooth functions. Check: is this sufficient? Could the limit develop singularities at the zero-set boundary despite C^k convergence?

## Output

## Verification memo: direct nonlinear construction of the normalized cutoff flow (Step 55)

### Overall reading

The architecture — regularize the degenerate coefficient β² ↦ β²+ε in the principal metric term only, obtain ε‑independent energy bounds because ε enters additively and positively (never as ε⁻¹ in a source), then take a compactness limit — is the natural and correct way to handle a Ricci‑type equation degenerating on {χ=0}. Four of the five load‑bearing pieces hold as stated; one (Proposition 7.1) reaches a correct final identity through an intermediate computation whose evaluation‑point convention is inconsistent and must be rewritten. Two pieces (the ε→0 passage and interface smoothness) are genuinely valid but rest entirely on one item that the note asserts by analogy rather than derives: the all‑order ε‑uniform hierarchy of Proposition 5.1. I detail each below.

### Claim 1 — joint H^s energy, transport cross‑coupling (Proposition 3.1): holds

The transport commutator term at order k is
∫ D^kβ · β² D^kW(G) · Dβ, with D^kW(G) carrying D^{k+1}G. Splitting β²=β·β and applying Cauchy–Schwarz as
[β|D^{k+1}G|]·[β|D^kβ||Dβ|] gives
η∫β²|D^{k+1}G|² + C_η‖Dβ‖_∞²∫β²|D^kβ|². This is exactly (3.9)–(3.10). The Cauchy–Schwarz step is correct, and ‖Dβ‖_∞ is finite because s>n/2+4.

On the β² versus β²+ε question you raise: the term being absorbed genuinely carries β² (the transport velocity is β²W(G)); the available dissipation carries β²+ε. Since β²|D^{k+1}G|² ≤ (β²+ε)|D^{k+1}G|² pointwise, the β²‑weighted term is dominated by the β²+ε dissipation, so absorption is legitimate with η<c. Using β² on the produced term is not only acceptable, it is the correct structural feature: every ε‑dependent contribution sits inside β²+ε on the dissipation side and never appears as a source, which is precisely why C_R is ε‑independent. The metric commutators (3.3)–(3.4) and the transport advective identity (3.7) are the standard skew‑adjointness of β²W·D up to div(β²W)∈L^∞, all controlled at s>n/2+4. One minor bookkeeping point: the Grönwall solution gives E_s(t)≤2E_s(0)+1 on [0,T₀], not the ≤2E_s(0) written in (3.2); this changes nothing.

### Claim 2 — difference estimate at r=s−2 (Proposition 4.1): holds

Sobolev embedding H^r↪L^∞ for r>n/2 is correct, and more usefully H^r is a Banach algebra for r>n/2; here r=s−2>n/2+2 satisfies this comfortably. The coefficient‑difference term (β₁²−β₂²)G₁⁻¹D²G₁ = (β₁+β₂)ω·G₁⁻¹·D²G₁ is a product of three H^r factors, since D²G₁∈H^{s−2}=H^r and (β₁+β₂)G₁⁻¹∈H^s⊂H^r. The algebra property yields ‖·‖_{H^r} ≤ C_R‖ω‖_{H^r} directly, giving (4.5). The essential structural point is correct: the highest derivative of the difference Z that ever appears is D^{r+1}Z=D^{s−1}Z, while D^{r+2}=D^s falls only on the individual G_i controlled by the H^s balls — no interpolation of a difference is invoked. The two‑order‑lower grading is exactly what makes this work.

The antisymmetric identity ∫h·a·Dh = −½∫|h|²·div a is applied with h=D^rZ and a=β₂²G₂⁻¹DG₂. This is the correct top‑order structure: the DeTurck Q_{ij}(G,DG) is quadratic in DG with G⁻¹ coefficients, so the difference Q(G₁,·)−Q(G₂,·) linearizes at top order to β₂²·G⁻¹(DG₁+DG₂)·D^{r+1}Z; the residual (β₁²−β₂²)Q₁ is a lower‑order H^r product. Because all norms use the fixed background ḡ and D=∇̄ is ḡ‑compatible, the identity ∫a^μD_μ(½|h|²_ḡ)=−½∫|h|²_ḡ div a holds exactly. One item the note leaves schematic: peeling a single derivative off D^{r+1}G to match a^μD_μ(D^rG) produces curvature‑commutator terms (covariant derivatives do not commute, and the contracted index is innermost). These are lower order (Riem(ḡ) times ≤r derivatives) and bounded at s>n/2+4, but a fully rigorous writeup should exhibit them rather than absorb them silently.

Crucially, I checked that every D^{r+1}Z appearing in the difference estimate carries a β₂ or β₂² weight (or is fully removed by the antisymmetric IBP): the Q‑difference is converted entirely to ‖Z‖²_{H^r}; the Lie‑difference leftover β₂D^{r+1}Z pairs with β₂²‑dissipation; the transport leftover β₂²D^{r+1}Z likewise. No unweighted D^{r+1}Z survives against a coefficient that fails to vanish on {β₂=0}. This is what makes the estimate valid at ε=0 (see Claim 4).

### Claim 3 — pullback identity (Proposition 7.1): final result correct, intermediate computation has an evaluation‑point inconsistency

The final identity ∂_tg=−2χ²(Ric(g)+g) is correct, and the scalar‑weighted pullback φ*(β₀²(Ric(G₀)+G₀)) = (β₀∘φ)²·(Ric(φ*G₀)+φ*G₀) = χ²(Ric(g)+g) is valid, using φ*(f·T)=(f∘φ)(φ*T) and φ*Ric(G₀)=Ric(φ*G₀). But the route to it, as written, is inconsistent about where β₀ is evaluated.

The ODE (7.1) is written ∂_tφ(t,x)=−β₀(t,x)²W(G₀)(t,φ(t,x)), with the weight at the Lagrangian label x. Feeding this into Step 1 gives
f′(t) = ∂_tβ₀|_φ + Dβ₀|_φ·∂_tφ = [β₀(t,φ)² − β₀(t,x)²] W·Dβ₀|_φ,
which is zero only if β₀(t,φ(t,x))²=β₀(t,x)² — the very identity being proved. As literally written, f′=0 is circular. The same confusion recurs in Step 2: V(t,y)=−β₀(t,φ⁻¹(y))²W is then set equal to −χ_E²W with χ_E=χ∘φ⁻¹, which would require β₀(t,φ⁻¹(y))=χ(φ⁻¹(y)), i.e. β₀(t,·)=χ everywhere — false, since β₀ evolves.

The repair is clean and standard, and gives the same final V and the same geometric equation. The transport equation ∂_tβ₀=β₀²W(G₀)·Dβ₀ is a quasilinear transport whose characteristics ψ_x satisfy ψ_x′(t)=−β₀(t,ψ_x)²W(G₀)(t,ψ_x), ψ_x(0)=x, along which β₀ is constant. These characteristics are exactly φ. Hence the correct diffeomorphism ODE uses the Eulerian velocity with the weight at the current point:
∂_tφ(t,x) = −β₀(t,φ(t,x))²W(G₀)(t,φ(t,x)),  V(t,y)=−β₀(t,y)²W(G₀)(t,y).
With this, Step 1 gives f′ = β₀(φ)²W·Dβ₀|_φ − β₀(φ)²W|_φ·Dβ₀|_φ = 0 non‑circularly, so β₀(t,φ(t,x))=χ(x). Then β₀(t,y)=χ(φ⁻¹(t,y))=χ_E(t,y), so V=−χ_E²W as intended, and Step 3’s Lie cancellation and Step 3’s scalar pullback go through unchanged. So: correct theorem, but Eq. (7.1), Step 1, and Step 2 need the weight evaluated at φ (equivalently, phrased through the characteristic ODE) rather than at the label x / at φ⁻¹.

### Claim 4 — ε→0 passage and ε=0 uniqueness: valid, contingent on the all‑order hierarchy

The elementary point ε·G_ε⁻¹D²G_ε→0 is correct once G_ε→G₀ in C² and ε→0.

The ε=0 uniqueness argument is valid, and your specific concern about degeneracy is answered by the weight structure. The difference estimate (4.13) is an energy estimate, not a maximal‑regularity/Schauder argument, so non‑uniform parabolicity is not itself an obstruction. What matters is that at ε=0 the dissipation is ∫β₂²|D^{r+1}Z|², which vanishes on {β₂=0}; but as noted under Claim 2, every term requiring absorption also carries the same β₂ (or β₂²) weight, so the absorption η∫β₂²|D^{r+1}Z|² ≤ (dissipation) is consistent pointwise, including on {β₂=0} where both sides are zero. The Grönwall then closes on ‖Z‖²_{H^r}+A‖ω‖²_{H^r} with C independent of ε, and the dissipation is only a bonus. So uniqueness holds for the degenerate ε=0 system, and this also promotes subsequence convergence to full‑sequence convergence. The limit G₀ is a classical smooth solution of the degenerate (1.4): each term is C^∞ and converges in C^k, and where β₀=0 all terms (including 2 sym(d(β₀²)⊗W), since d(β₀²)=2β₀Dβ₀) vanish, giving ∂_tG₀=0 there — consistent with the frozen exterior.

The single load‑bearing dependency: C^∞ compactness requires the all‑order ε‑uniform bounds E_m ≤ C_m on [0,T₀] for every m (Proposition 5.1). The note derives this in one paragraph as “identical to §3,” and Step 54 §6.3 itself records that this hierarchy “has not yet been written.” The induction E_m′+c_mD_m ≤ C(E_s)E_m+C_m(E_{m−1}) is the standard Moser tame structure, and the mechanism that made §3 close (transport cross‑coupling β²D^mW(G)·Dβ still carrying β², metric commutators bounded by lower norms, no ε⁻¹) repeats verbatim at order m, so I judge it very likely to hold — but it is asserted rather than exhibited, and it is the item that actually carries Claims 4 and 5. Writing the order‑m tensor bookkeeping explicitly (in particular verifying at each m that no cross‑coupling term escapes the β² weight and that C_m depends only on E_{m−1} and E_s) is the substantive remaining derivation.

### Claim 5 — smoothness across the interface ∂{χ>0}: valid as a corollary of the global uniform bounds

“C^∞ limit of smooth functions ⇒ smooth” is sufficient here precisely because the estimates are global on M with the fixed background ḡ and never localize near {χ=0} nor divide by β. The all‑order energies control ‖G_ε‖_{C^k(M×[0,T₀])} ε‑uniformly across the whole manifold, including through the interface; the degeneracy only weakens the dissipation there, but the a priori E_m bound does not use dissipation strength. Since the C^k bounds do not blow up as ε→0, Arzelà–Ascoli gives C^∞ convergence on the fixed compact M×[0,T₀], so G₀ is globally smooth and in particular smooth across ∂{χ>0}; there is no mechanism for a singularity at the moving zero‑set edge on [0,T₀]. Two supporting facts worth confirming in the writeup: (i) the moving set {β₀(t,·)=0} stays regular because ‖β₀‖_{H^s} is controlled on [0,T₀], preventing gradient blow‑up of the quasilinear transport; (ii) the transport preserves the zero set along characteristics and contains no division by β, so no inverse‑β power is created. Thus Claim 5 is genuinely valid, but it is the same corollary of the all‑order hierarchy as Claim 4 — not an independent assertion — and it inherits that hierarchy as its one prerequisite.

### Summary of what is solid and what to complete

- Claims 1 and 2 are correct as derivations, modulo making explicit the curvature‑commutator terms in the antisymmetric IBP and the minor constant in (3.2).
- Claim 3’s theorem is correct; Eq. (7.1), Step 1, and Step 2 must be rewritten with the Eulerian weight β₀(t,φ)² (equivalently, phrased via the characteristic ODE of the transport equation), otherwise f′=0 is circular.
- Claims 4 and 5 are valid and their delicate points (degenerate uniqueness at ε=0; interface smoothness) are correctly handled by the β₂‑weight matching between absorbed terms and dissipation — but both rest on the all‑order ε‑uniform hierarchy of Proposition 5.1, which is currently asserted by analogy. Producing the explicit order‑m estimate (with the same β²‑weight matching at every order and confirmed absence of ε⁻¹) is the one remaining derivation that converts Theorem 9.1 from structurally‑supported to fully established.

None of these touch the delineation the note itself records in §10.2 (per‑datum versus sequence‑uniform existence time, the first‑exit quantities, the terminal spectral question, and the full Yau‑26 statement remain outside this construction).