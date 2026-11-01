# TTCS Independent Branch Record

```json
{
  "step_id": 43,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step43_routeA_orientation_and_global_allocation.md",
    "Sessions/S0910A02/workspace/data/step43_orientation_obstruction_bookkeeping.json",
    "Sessions/S0910A02/workspace/notes/step42_mode_projection_bridge_resolution.md",
    "Sessions/S0910A02/workspace/data/step42_det_R_plus_computation.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds--8fe1aa31deb8--5b19d560b771/object.md",
    "Knowledge/objects/papers/Conformal-Kähler-rigidity-of-Einstein-four-manifolds--ee41ec8c511e--4518ab125268/object.md"
  ]
}
```

## Task

Verify the Step-43 correction to Route A. Read the new Step-43 note, Step-42 mode-projection note/data, the orientation bookkeeping data, and the cited Ozuch/LeBrun-Ozuch/Catino-Dameno source objects. The scientific question is: is the correction sound that det R_+=0 for KE limits is not a ceiling but the orientation-compatible side, while b_+>1 over a KE limit forces reversed EH bubbles testing R_-? Check source fidelity, orientation dictionary, topology/betti bookkeeping for A1/EH bubbles, the claim that Derdzinski-type rigidity does not follow from finitely many singular-point constraints, and the route allocation away from immediate high-order Lambda>0 obstruction theory. Identify any overclaim that would mislead the next research step.

## Output

## Verification memo: Step-43 correction to Route A

### Overall assessment

The central correction is sound and well grounded in the cited sources. The statement that `det R_+ = 0` for a positive Kähler–Einstein limit is the orientation-compatible side of the Biquard/Ozuch first obstruction being automatically satisfied — rather than a ceiling that makes all Kähler–Einstein bubbling first-order compatible — is correct. The orientation dictionary, the Kähler determinant computation, and the intersection-form bookkeeping check out. There is one genuine logical step between "reversed bubbles are forced by topology" and "an obstruction is obtained" that the note treats less sharply than it should, and it interacts badly with the very family the route targets. I detail this below, together with source-fidelity confirmations and the load-bearing unproven derivation inside the Step-42 mode projection.

### Source fidelity is high

**Orientation dictionary.** Ozuch's introduction gives the dichotomy `det R⁺_{g_o}(p)=0` or `det R⁻_{g_o}(p)=0` depending on gluing orientation (object.md, the two-block display after eq. (3)), and the coefficient formula `λ_k(ζ^±) = c⟨R^±(ψ_*H₂)ζ^±, ζ_{(k)}^±⟩` (eq. (28)/(29)). The asymptotic forms `eh_{ζ^+}=e−(ρ(ζ)^−∘ζ^+)/(2r⁴)` (Prop. 1.16(1)) and `eh_{ζ^−}=e−(ζ^−∘ρ(ζ)^+)/(2r⁴)` (eq. (17)) are quoted correctly. The identification "ζ⁺ tests R₊, ζ⁻ tests R₋" follows directly from these. No misreading here.

**Kähler determinant.** For Ric = Λg in dimension 4, s = 4Λ and R₊ = W₊ + (s/12)Id = W₊ + (Λ/3)Id, matching the note. The Kähler eigenvalues W₊ ~ (2Λ/3, −Λ/3, −Λ/3) give R₊ ~ (Λ, 0, 0), det R₊ = 0, kernel dimension 2. This is independently confirmed by LeBrun–Ozuch, who state R⁺(g_∞) has eigenvalues (0,0,s/4)=(0,0,λ) at the singular point of a conformally Kähler limit (Corollary 8.4 region computation). The universal statement over all positive KE surfaces is correct.

**Intersection-form bookkeeping.** EH is Ricci-flat and anti-self-dual in the usual orientation (Ozuch §1.2.1), so its compactly-supported class has negative square, giving the orientation-compatible bubble a (b₊,b₋)=(0,1) contribution and the reversed bubble (1,0). For M=#_k(S²×S²) with intersection form kH (b₊=b₋=k, τ=0), a limit with b₊(O)=1 forces N₋ = k−1 reversed and N₊ = k−b₋(O) compatible bubbles. I checked the JSON table arithmetically against b₂(M)=b₂(O)+#bubbles and τ(M)=τ(O)+N₋−N₊: every row is internally consistent, and the rows flagged `admissible_counts:false` are exactly those with a computed negative bubble count. The signature relation N₊−N₋ = b₊(O)−b₋(O) holds throughout.

**LeBrun–Ozuch usage.** Admissible/expected topology = all Ricci-flat ALE bubbles anti-self-dual in the reference orientation (Definitions 1, 8), and admissible + Hermitian limit ⟹ del Pezzo with b₊=1 (Theorem 4.1). A reversed EH bubble is self-dual in the reference orientation, hence non-admissible, and therefore genuinely outside the LeBrun–Ozuch classification. The note's inference — that b₊(M)>1 topologies escape the del Pezzo conclusion precisely by requiring reversed bubbles — is a correct and substantive reading, not an artifact.

### The refinement that most affects the next step: forced count ≠ obstruction

The topology forces a *count* N₋ ≥ k−1 of reversed bubbles, but it does not fix *which* singular points host them. Ozuch's obstruction says only that a reversed bubble sitting at p imposes `det R₋(p)=0`. To convert "N₋ ≥ 1 reversed bubbles are required" into an actual obstruction, one needs `det R₋ ≠ 0` at *every* singular point available to host a reversed bubble (or a counting argument that too few `det R₋=0` points exist). If the KE limit has some points with `det R₋=0` and enough of them, the reversed bubbles can be placed there and the first-order data closes.

This is decisive for the target family, and the note's own model computations show why. The standard product Einstein metric on S²×S² is Kähler for both orientations, so `det R₋=0` everywhere (JSON `S2xS2_product_equal_spheres`). The natural noncollapsed orbifold limit for a #_k(S²×S²) stress family is product-like, i.e. exactly the geometry where the R₋ lever vanishes identically. So the mechanism, as stated, correctly identifies where an obstruction *could* live (CP²-type points, where R₋=(Λ/3)Id and `det R₋ = (Λ/3)³ ≠ 0`), but for the family it is meant to attack the most natural limit is the one where the lever is void. The note gestures at this ("Any use of the R₋ lever must therefore analyze actual KE/orbifold models"), yet its strategic conclusion still reads as though forced reversed bubbles are close to yielding an obstruction. The unresolved substance is precisely: for a product-like or mixed KE del Pezzo limit, is there a configuration of k−1 reversed bubbles all sitting at `det R₋=0` points? If yes, the first-order pair obstruction is empty for the target and the decision moves to higher order — which §2 recommends deferring. This tension between "defer higher order" and "first order is void where it matters" should be visible to whoever picks up the route.

### One assumption carried silently: b₊(O)=1

The bookkeeping fixes b₊(O)=1 while varying b₋(O). For the reversed (non-admissible) scenario, b₊(O)=1 cannot be imported from LeBrun–Ozuch's del Pezzo theorem, which applies only to admissible limits. The JSON does phrase it as a hypothesis ("for a KE orbifold limit with b₊(O)=1"), and the note flags that orbifold cohomology statements "still need source-level statement." Good that it is marked; but the whole finite table inherits this hypothesis, so its conclusions are conditional on an orbifold intersection-theory input not present in the supplied objects.

### Mode-projection algebra: internally correct; one load-bearing derivation unproven

I re-derived the Step-42 pieces:

- l=2 indicial equation α²+2α−8=0, roots 2, −4 ✓
- Wronskian of (ρ², ρ⁻⁴): W = −6ρ⁻³, so ρ³W = −6 constant ✓
- extraction formula: with a=Aρ²+Bρ⁻⁴, a(2R)−a(R)/16 = (63/16)A R², giving A=(16a(2R)−a(R))/(63R²) ✓

These are correct, and the constant-Wronskian scale-independence of the pairing is a real structural feature. The Λ-source growing coefficient Λt²c₋₄/24 being O(t²) subleading is consistent with the first obstruction being the t→0 limit condition α₊^orbifold=0.

The unproven step is the one on which the whole "read the obstruction from a C⁰-Ricci-pinched noncollapsed sequence" program rests: that the Bianchi-gauged Ricci equation projects onto the scalar l=2 ODE with source obeying |S_i| ≤ Cδ_i. The source involves second derivatives of the metric, so bounding it needs the C^{1,α}∩W^{2,q} regularity (from Cheeger–Naber Thm 1.13/2.11) *plus* a genuine derivation that the angular l=2 projection closes into that ODE with commutator and nonlinear terms controlled. The note states a₁(ρ) is well-defined from metric values alone under C^{1,α} convergence, which is fine for the *left-hand* mode function, but the *equation* it satisfies and the smallness of its source are asserted, not derived. This is the interface whose verification would determine whether the pair-obstruction lemma is available at all, independent of the topology discussion above.

### Derdziński / Catino–Dameno gap: correctly identified

The note's §4 statement — that finitely many singular-point spectral constraints do not trigger the global conformal-Kähler classification — is faithful. Catino–Dameno Theorem 1.1 requires α_h > β_h *on all of M*; Theorem 1.4 requires the uniform bound β_h ≤ ρ₀α_h *on M*; LeBrun–Ozuch Theorem 3.1(iv) requires det W⁺ > 0 *at every point*. All are everywhere/uniform pointwise conditions. Moreover `det R₊=0` (a zero eigenvalue of R₊, i.e. −Λ/3 ∈ spec W₊) is not even the same spectral condition as "largest eigenvalue simple," so point data of the Ozuch type does not feed these theorems even locally. The proposed upgrade route (a global harmonic self-dual form with positivity surviving degeneration, matching LeBrun–Ozuch 3.1(iii)) is the right shape of the missing input. No misuse here.

### Coverage points the next step should not silently cross

1. **A₁/EH only.** The betti tables and the R₊/R₋ dictionary are specific to R⁴/Z₂ → T*S² (single EH). Cheeger–Naber gives isolated singularities with tangent cones C(S³/Γ) for general finite Γ ⊂ SO(4) acting freely; A_k, D_k, E_k and non-SU(2) cyclic bubbles carry different obstruction structures (Ozuch Remark 2.21: A_k obstructions involve curvature derivatives) and more complex intersection contributions. The finite bookkeeping does not yet address these, and a full noncollapsed positive-sign theorem must.

2. **First obstruction vs. the sharper and higher ones.** "Reversed bubble forces det R₋=0" is the weaker Biquard form (one zero eigenvalue). Ozuch Theorem 0.2 gives, under stability or single-rigid-singularity hypotheses, the rank-one form diag(0,0,Λ) (two zero eigenvalues), and the second obstruction μ₁ = C·det[R₂₂ R₂₃; R₃₂ R₃₃] (eq. after Lemma 2.14) is a further condition. The KE self-dual side already satisfies the rank-one form; the reversed side, if it is to obstruct, may need the sharper statement, and the higher μ_k obstructions remain live.

3. **Retained Step-42 data phrasing.** The `step42_det_R_plus_computation.json` still carries `universal_statement`: "The Ozuch obstruction is ALWAYS satisfied for KE orbifolds — they can always be desingularized in principle," and `obstruction_trivial: ... desingularization possible in principle`. Even after the Step-43 correction, this remains an overstatement on two counts: it concerns only the first self-dual obstruction (not the reversed side, and not the higher μ_k), so "desingularization possible in principle" does not follow. A reader consulting that data file without Step-43 would be misled in exactly the direction Step-43 sets out to correct.

### What remains unresolved

- Whether, for a product-like or mixed KE del Pezzo limit of #_k(S²×S²), the forced k−1 reversed bubbles can all be placed at points with `det R₋=0`, which would empty the first-order pair obstruction for the target.
- The Bianchi-gauge → l=2 radial-ODE derivation with a source bound |S_i|≤Cδ_i valid on merely C^{1,α}∩W^{2,q} sequences, and the precise definition/continuity of the mode function along a GH-converging family — the single interface controlling whether the pair-obstruction lemma exists.
- An orbifold-cohomology statement fixing b₊(O) for non-admissible (reversed-bubble) positive KE orbifold limits, since the LeBrun–Ozuch del Pezzo b₊=1 result does not cover that case.
- Extension of the orientation dictionary and intersection bookkeeping beyond A₁/EH to general Γ, and to the sharper (rank-one and second-order) obstructions.

The correction itself does not overstate; the risk to the next step is instead in reading the forced reversed-bubble count as already an obstruction, and in the persistence of the earlier "desingularization possible in principle" phrasing in the Step-42 data.