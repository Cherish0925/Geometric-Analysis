# TTCS Independent Branch Record

```json
{
  "step_id": 39,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step36_analytic_platform_and_global_Q.md",
    "Sessions/S0910A01/workspace/notes/step38_continuation_repair_and_support_normalization.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md"
  ]
}
```

## Task

Verify whether the first-exit bootstrap for the normalized cutoff flow ∂_t g = -2χ²(Ric+g) actually closes when all conditional pieces are assembled. The argument is:

1. Per-datum DeTurck existence (citing Yang's Theorem 4.1 with the +g normalization as a zeroth-order perturbation) gives flow on [0,T₁).
2. Define T* = sup{T ≤ θr²: first-exit conditions (F1)-(F3) hold on [0,T]}. By smooth initial data, T* > 0.
3. On [0,T*): energy estimates from Steps 34-36 give K₂^η(t) ≤ e^{Cθ(1+1)}K₂^η(0), B(t) ≤ Cγ³, Y(t) ≤ CγK₂(0)/t, J₆(t) ≤ Ce^{Cθ}J₆(0). Weighted Moser gives ||aF(t)||_∞ ≤ Cγ/t and ||aE(t)||_∞ ≤ Cδ(r²/t)^{1/3}.
4. From (3): |U(t)| = |a(Rm+G)(t)| ≤ ||aF(t)||_∞ + C ≤ Cγ/τ + C for t ≥ τ > 0.
5. A03's all-order staggered continuation (TTCS-verified, 70/70): |U| bounded on [τ,T*) → all derivatives bounded → flow extends past T*.
6. Self-improvement: K₂^η(T*) < 2K₂^η(0) for small θ; metric drift ∫₀^{T*} ||aE||_∞ dt ≤ (3/2)δθ^{2/3}r² < Λ/2; Sobolev constant comparison.

Check specifically: (a) Is the velocity integral ∫₀^T ||aE||_∞ dt finite near t=0 given the (r²/t)^{1/3} singularity? (b) Does the Moser endpoint depend on quantities that themselves depend on (F1)-(F3), creating a circular dependency? (c) Is there a timing issue between the DeTurck existence (which may be very short) and the Moser estimates (which need positive time)? (d) Does the global Q propagation Q(T) ≤ e^{C(1+r⁻²)T}Q(0) hold through the macro-disjoint support summation? (e) Is the per-datum DeTurck existence for ∂_t g = -2χ²(Ric+g) really a trivial modification of Yang's ∂_t g = -2χ²Ric?

## Output

## Verifier memo — first-exit bootstrap for ∂_t g = −2χ²(Ric+g)

### Overall finding

The six-step assembly does not yet close as a combined existence-plus-estimate statement. The energy/Moser pieces (steps 3–4) and the global defect propagation (step d below) are internally coherent as *conditional* consequences of the first-exit conditions plus the proved Hessian-χ contraction tensors of Step 35. The chain breaks at step 5, where "|U| bounded ⇒ flow extends past T\*" rests on **two analytic links that are described but not carried out**: the shifted unweighted curvature-derivative module (with the full tensor expansion of the weighted U-equation) and the degenerate transported-DeTurck short-time existence/restart for the *normalized* equation. Neither is a bookkeeping matter; each is where the real work sits. Details per your five questions.

---

### (a) Velocity integral near t = 0 — finite

With ‖aE(t)‖_∞ ≤ Cδ(r²/t)^{1/3}, the exponent 1/3 < 1 makes the singularity integrable:
∫₀^T ‖aE‖_∞ dt ≤ Cδ r^{2/3} · (3/2)T^{2/3} = (3/2)Cδ θ^{2/3} r², matching step36 (4.4) and step34 (6.4). This is correct and the r²-clean parabolic scaling is the right homogeneity. Two points worth reconciling, neither of which endangers finiteness:

- The metric-drift closure needs ∫₀^T 2‖aE‖_∞ dt small **as a dimensionless log-bilipschitz exponent**, since ∂_t log g ≈ −2aE. In the normalization Ric→−g (target λ=−1) the units are consistent and the achieved (3/2)Cδθ^{2/3}r² is small once δ is small at fixed small r; so self-improvement of the metric comparison and of S(t) ≤ 2S(0) is available. Good.
- The single Moser step you can read off step34 (6.1), ‖af‖_∞ ≤ C S^{2/p₀} t^{−3/p₀}(∫H_{p₀})^{1/p₀}, gives for p₀=6 a t^{−1/2} single-step rate, whereas the endpoint used is t^{−1/3}. Substituting S≈r²V^{−1/2}, H₆≈δ⁶V yields Cδr^{2/3}t^{−1/2}, hence ∫ ∝ δθ^{1/2}r^{5/3} — not the r² parabolic scaling. The clean r² of (6.4) is what one expects, so the intended endpoint is the *iterated* p₀→∞ recurrence, not (6.1) as displayed. The detailed recurrence lives in files not supplied here (Step 32 / A03 Step 34), so the precise exponent cannot be confirmed from the present notes. Regardless, any exponent < 1 gives a finite drift, so (a) holds; the exponent value only affects the numerical drift constant, which controls how small δ must be.

### (b) Circular dependence of the Moser endpoint — structurally a bootstrap, not a loop

The endpoints depend on γ = S(0)K₂^η(0)^{1/2}, on S(t), and on K₂^η(t) — i.e. exactly on (F1)–(F3). This is the ordinary continuity-method structure: assume (F) on [0,T\*), derive the estimates, then show the derived bounds are strictly inside the thresholds. It is non-circular **provided** three things, all present here:

1. γ is anchored at t=0 by the support selection (step38 (5.4)), not by the running solution; under (F) it stays ≤ C·γ\* because S(t)≤2S(0), K₂^η(t)≤2K₂^η(0).
2. The one genuinely self-referential object, Y appearing in its own reaction coefficient S²Y in (2.14)/(4.4), is closed by the *a priori* integral B(t)=∫S²Y ≤ Cγ³ obtained from the q=2 energy alone (step34 (3.7)); the Gronwall factor exp(C∫S²Y) ≤ exp(Cγ³) is then a fixed constant, and the good-slice bound Y(t) ≤ CγK₂(0)/t follows without feeding Y back into itself pointwise. This is the correct resolution and it is sound.
3. Self-improvement is strict (K₂^η(T\*) < 2K₂^η(0), drift < α₀/2) for small θ, δ.

So no vicious circle in the estimate layer. The real dependency issue is not here but in whether the *interval on which (F) is assumed* can be maintained — i.e. whether the flow exists up to and past T\* (see c).

### (c) Timing between DeTurck existence and the positive-time Moser estimates

The t→0 blow-up of the smoothing estimates is **not** the problem: near t=0 the initial smooth data give |U(0)| directly, and the Moser bound is only invoked at t ≥ τ > 0 to feed |U| ≤ Cγ/τ + C into continuation. Your step-4 arithmetic is right (|U| ≤ ‖aF‖_∞ + C from U = aRm + aG, |aG| ≤ C).

The genuine timing concern is the **restart**. The maximal-time argument runs: existence on [0,T\*) ⇐ continuation past each interior time ⇐ derivatives bounded ⇐ |U| bounded ⇐ Moser ⇐ (F) ⇐ existence. This is a *joint* bootstrap of existence and estimates, and its one non-automatic link is: from the smooth terminal metric g(T\*) produced by the derivative-energy induction, one must obtain a fresh existence interval of length bounded below in terms of the controlled quantities (bilipschitz constant, curvature-derivative bounds on [τ,T\*)), so that the existence time cannot shrink to zero as t↑T\*. A03 Step 40 §5 and step36/step38 state explicitly that this restart — "a valid transported-coefficient degenerate short-time construction" — is **not proved**. Note that A03 Step 40 also states its TTCS check "concerns the derivative-energy induction only; it does not prove the terminal restart," so the "70/70" verification you cite covers the arbitrary-order derivative bookkeeping, not the extension of the solution past T\*. Consequently step 5 as phrased ("all derivatives bounded → flow extends past T\*") conflates the proved part (bounded derivatives, smooth limit g(T\*)) with the unproved part (restart). The bootstrap therefore does not yet exclude a finite maximal time.

There is also an input inside the "derivatives bounded" half: the staggered induction of A03 Step 40 requires, at the start of each stage, T_j = ∇^j Rm ∈ L^q for j<m in every finite q, seeded by T₀ = Rm ∈ L^q "from the zero-order unweighted curvature energy." That zero-order unweighted L^q curvature module (shifted Wang Lemma 4.10 / Prop 4.13, step38 §3) and the full tensor expansion of the weighted U-equation (1.2) are asserted-plausible but, by step38 §6's own statement, "not yet expanded." So even the derivative-boundedness half is conditional on an unwritten module.

### (d) Global Q propagation through macro-disjoint summation — holds conditionally

Q(t)=∫_M|E|² decomposes as (sum over active supports) + (frozen complement). The summation is clean because:

- η ≡ 1 on supp a and a = 0 on supp dη (step34 §1), so the buffer where dη ≠ 0 has a = 0 and is frozen; the per-support inequality (3.4)–(3.6) correctly carries no active buffer-derivative term, and the Hessian-χ terms are paid by the *proved* signed IBP with B_def (Step 35), not by an assumed evolving-Hessian bound.
- On the frozen complement ∂_t g = 0, so E is stationary and Q_complement(t) = Q_complement(0).
- The buffered active supports are made disjoint by the Bishop–Gromov packing + finite coloring of step38 §5, and each carries the *same* constant C from the uniform good-support selection (same Λ, r, γ\*), so Σ_α Q_{U_α}(t) ≤ e^{C(1+r^{-2})t} Σ_α Q_{U_α}(0).

Hence Q(t) ≤ e^{C(1+r^{-2})t}Q(0), and on [0,θr²] the exponent (1+r^{-2})t ≤ θ(1+r²) is bounded, giving Q(θr²)/A → 0 when Q(0)/A → 0. This is among the most solid components. Its residual dependence is only on the moving-Sobolev premise S(t) ≤ 2S(0) and the metric comparison, i.e. on (F1) itself — the same first-exit object being bootstrapped in (b)/(a). So (d) is valid *given* the first-exit geometry; it does not independently establish that geometry.

### (e) Is the normalized DeTurck existence a trivial modification of Yang's?

At the level of the linearized principal and first-order structure, yes: adding +g to Ric adds −2ag to the velocity, whose linearization is −2ah (order zero in derivatives of h) plus −2(δa)g (lower order via the diffeomorphism variation, step36 (1.7)); the parabolic symbol and Yang's triangular first-order structure are unchanged. The note also correctly insists the gauge term must be 𝓛_{âW}ĝ, i.e. with the extra dâ⊗W♭ + W♭⊗dâ (eq. (1.4)), not â𝓛_Wĝ — these first-derivative coefficient terms are part of the DeTurck cancellation. That correction is right and non-trivial.

But "citing Theorem 4.1 as a zeroth-order perturbation" is a *plan*, not a completed existence proof, for a reason the note itself states (§1.2): the coefficient a = χ² **vanishes on part of M**, so the problem is not uniformly parabolic. Yang's existence is a transported-coefficient degenerate construction with tame (Nash–Moser-type) energy estimates and ε-regularization whose limit is supplied by those estimates — "ordinary Schauder constants… do not by themselves give the required ε-uniform smooth limit." Therefore the +g contribution, even though lower order, must be threaded through a re-derivation of Yang's degenerate tame estimates, which the note says it has not done. Two concrete pieces of work remain: (i) reproduce the transported-system tame estimates including the −2â h and −2(δa)ĝ terms; (ii) the same theorem is needed again as the *restart* from g(T\*), where its existence time must depend only on the continuation-controlled bounds. Until (i)–(ii) exist, the existence citation is not a proof, and the maximal-time exclusion of (c) is open.

---

### The two load-bearing links, named

1. **Restart / degenerate short-time existence** for the normalized transported-DeTurck system (steps 1 and 5's extension). Everything downstream — the very definition of T\* on a persistent solution and the contradiction at T\* — depends on it. Structurally addressed at the symbol level; not proved because of the degenerate coefficient and the required tame estimates.
2. **Shifted unweighted curvature-derivative module** (Wang Prop 4.13 form) plus the complete tensor expansion of the weighted U-equation (1.2), which seeds the staggered derivative induction. Asserted-plausible; the full index-level expansion and the normalization/G lower terms are not written.

Given both, the estimate layer (energy, Y, J₆, Q, Moser) would deliver the first-exit self-improvement, and the bootstrap would close on [0,θr²]. Without either, "flow extends past T\*" is not established, so the first-exit interval is not shown to reach θr².

### On reach relative to Yau 26

Every note repeats, correctly, that even full completion of these links settles only the near-critical Ishida–LeBrun four-dimensional λ<0 laboratory. It would not touch the λ>0 branch, arbitrary four-manifold topology, dimensions n ≥ 5, the dimension-only interval constants c_n < C_n demanded by the proposition, or the Lean formalization. So the object under verification is one analytic engine for one family, not the theorem.

### Concrete items to resolve

- Reconcile the Moser endpoint exponent: derive the iterated recurrence explicitly so that ‖aE(t)‖_∞ ≤ Cδ(r²/t)^{1/3} (r²-clean drift) is confirmed rather than the t^{−1/2} single-step rate of (6.1); the drift constant in (a) depends on it.
- Write the degenerate transported-DeTurck tame estimate for −2χ²(Ric+g), with the −2â h and −2(δa)ĝ terms and the 𝓛_{âW}ĝ gauge, and state the restart existence time as a function of bilipschitz + curvature-derivative bounds only.
- Complete the shifted unweighted curvature L^q module and the full tensor expansion of (1.2), including the G and normalization lower terms, so that T₀,…,T_{m−1} ∈ L^q feed A03 Step 40's stage hypothesis (1.7).
- Confirm that the finite coloring in step38 §5 makes the *buffered* (η-support) sets disjoint, not merely the χ-cores, since the Q summation and per-support Sobolev constants use the buffered sets.