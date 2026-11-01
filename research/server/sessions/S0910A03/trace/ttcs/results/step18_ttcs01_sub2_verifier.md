# TTCS Independent Branch Record

```json
{
  "step_id": 18,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md",
    "Sessions/S0910A03/workspace/notes/step17_normalized_cutoff_flow_theorem.md",
    "Sessions/S0910A01/workspace/notes/step17_support_scale_li_bootstrap.md",
    "Sessions/S0910A03/workspace/scripts/verify_cutoff_defect_energy.py",
    "Sessions/S0910A03/workspace/scripts/verify_step18_weighted_defect_exponents.py",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Independently derive and assess the proposed simultaneous first-exit bootstrap for the normalized cutoff flow ∂_t g=-2aE, a=χ², E=Ric+g, in dimension four. Focus on the weighted defect estimate |aE(t)| ≤ C_p δ (r²/t)^{2/p}, p>2, under provisional metric comparability, relative Sobolev control, finite-neighbor local critical curvature energies, and appropriate connection/cutoff bounds. Derive the scalar/tensor L^p energy inequality with all a, ∇a, and Hessian-a commutators accounted for; determine whether a fixed supercritical exponent can be obtained before applying a Li-type time-dependent-potential iteration, and state exactly which terms remain uncontrolled. Check that the C/t weighted curvature estimate cannot by itself preserve E because ∫dt/t diverges. Treat coupled L² propagation only as conditional on the provisional bootstrap assumptions. Provide a mathematical memo, not procedural advice.

## Output

## Verification memo: weighted defect estimate for ∂_t g = −2aE, a=χ², E=Ric+g (n=4)

I reworked the derivation independently from the tensor evolution up through the L^p energy inequality. The algebra of the identities used is correct; the load-bearing analytic passage is not yet in hand, and I can name precisely which terms leak and where the exponent p>2 becomes indispensable.

### 1. The defect square identity is correct

From ∂_t g_{ij}=−2aE_{ij} one has ∂_t g^{ij}=+2aE^{ij}, so differentiating |E|²=g^{ia}g^{jb}E_{ij}E_{ab} produces the two inverse-metric terms +4a·tr(E³). Using Δ_L E = ΔE + 2Rm(E)−Ric·E−E·Ric, the −2E damping, and Ric=E−g (so Ric(E,E)=tr(E³)−|E|²), the two ±4a·tr(E³) contributions cancel exactly:

  (∂_t − aΔ)|E|² = −2a|∇E|² + 4a·Rm(E,E) + 2⟨E, C_a(E)⟩.  (∗)

This reproduces the Step-14/Step-17 identity and the `verify_cutoff_defect_energy.py` check. The identity |∇a|²/a = 4|∇χ|² is correct (a=χ², ∇a=2χ∇χ). The script's cancellation is a **p=2 statement**: testing the tensor equation with E gives the full tensor dissipation ∫a|∇E|², into which the ∇a·∇E commutators absorb by Young with O(|∇χ|²) remainders. That is exactly why L² closes and why the supercritical case behaves differently (§4).

### 2. Weighted scalar inequality with every a, ∇a, Δa term

Put φ = a|E| = χ²|E| (a is t-independent, so |aE| = a|E| = φ). Kato in (∗) gives

  ∂_t|E| ≤ aΔ|E| + 2a|Rm||E| + ∇a·∇|E| + O(r^{−2})|E| + O(|∇a||∇E|),

where the O(r^{−2}) collects the algebraic C_a terms (Δa)E, τ a_{ij}, a_{ik}E_{kj}, and O(|∇a||∇E|) is the genuine first-derivative commutator −a_k(∇_iE_{kj}+∇_jE_{ki}) together with ½(a_iτ_j+a_jτ_i). Multiplying by a and rewriting via aΔφ = a²Δ|E| + 2a∇a·∇|E| + a(Δa)|E| and a∇|E| = ∇φ − |E|∇a:

  ∂_t φ ≤ aΔφ − ∇a·∇φ + [ 2a|Rm| + V_cut ] φ + O(a|∇a||∇E|),

  V_cut = |∇a|²/a − Δa + O(r^{−2}) = (2|∇χ|² − 2χΔχ) + O(r^{−2}) = O(r^{−2}).

Two structural facts are confirmed: (i) the cutoff potential is homogeneous and O(r^{−2})·φ — **no 1/χ blow-up** (the |∇a|²/a=4|∇χ|² identity removes it); (ii) the curvature reaction carries the **weighted** coefficient 2(a|Rm|), which is why |aRm| is the natural object. The residual O(a|∇a||∇E|) is the only term not reducible to a potential.

### 3. L^p inequality, degenerate dissipation, and the 4D volume cancellation

Testing with φ^{p−1} and integrating:

  (1/p) d/dt ∫φ^p + (4(p−1)/p²)∫a|∇(φ^{p/2})|²
   ≤ ∫[2a|Rm| + O(r^{−2})]φ^p + ∫ φ^{p−1}·O(a|∇a||∇E|).

The dissipation is **degenerate** (weight a → 0 in the transition). The curvature reaction is absorbable via a weighted Sobolev inequality: since a^{1/2}=χ is compactly supported, (∫(χ h)⁴)^{1/2} ≤ A∫|∇(χ h)|² holds under Ric≥−3g (Buser/Gallot/Saloff-Coste; A ~ r·Vol(U)^{−1/4} in norm form). With ∇(χ h)=χ∇h+h∇χ,

  ∫a|Rm|φ^p ≤ ||Rm||_{L²(U)}·A·[ 2∫a|∇(φ^{p/2})|² + O(r^{−2})∫φ^p ],

and on a support with normalized critical energy r⁴Vol^{−1}∫|Rm|² ≤ ε_*,

  A·||Rm||_{L²(U)} ~ (r Vol^{−1/4})·(ε_* Vol/r⁴)^{1/2}·… = √ε_* — **volume cancels**.

So for ε_* small the curvature reaction absorbs into the degenerate dissipation, and the O(r^{−2}) terms accumulate into the standard (t^{−1}+r^{−2}) prefactor. This mechanism is correct and is the genuine advance; I confirm the arithmetic in `verify_step18_weighted_defect_exponents.py` (v-power = 0, r-power total = 2, time exponent 2/p). It is, however, valid only while metric comparability, the relative Sobolev constant, and R_α ≤ ε_* are maintained on [0,T'] — all assumed, not produced here.

### 4. The one term that does not reduce to a potential: scalar vs. tensor gradient

The residual ∫φ^{p−1}·a|∇a||∇E| = 2∫a^{p+1/2}|E|^{p−1}|∇χ||∇E| Young-splits as

  ≤ ε∫a^{p−1}|E|^{p−2}|∇E|² + Cε^{−1} r^{−2}∫φ^p.

Absorption therefore needs the **tensor** dissipation ∫a|E|^{p−2}|∇E|². The scalar φ-Moser iteration supplies only ∫a|E|^{p−2}|∇|E||² (via Kato), which is strictly weaker: the rotational part of ∇E is lost. **Consequently a fixed supercritical p>2 cannot be obtained from the scalar reduction f=aK; the cutoff commutator −a_k(∇_iE_{kj}+∇_jE_{ki}) leaks tensor-gradient information the scalar dissipation cannot recover.** The correct vehicle is a **tensor** Moser iteration on (∗) directly; there ∫a|E|^{p−2}|∇E|² is available, the commutator absorbs by the split above, the Rm reaction absorbs by √ε_* (§3), and the ∂_t(dV) and inverse-metric contributions are O(δ)·(potential) while |E|≤O(δ) holds. This is the same architecture Li uses for |Rm|; it is conditionally viable, but only at the tensor level and only with the §3 inputs held fixed.

### 5. Ordering: the defect estimate is downstream of |aRm|≤C/t, not before it

The potential in the defect equation is 2a|Rm|. Running the defect Moser iteration (the Li-Corollary-3.5 analog) needs a time-integrable control of that potential of the form ∫(a|Rm|)^{3/2} ≤ μ³ t^{−1}, which in Li is produced from **both** the L² energy smallness **and** the pointwise |aRm|≤C/t smoothing. Therefore a supercritical defect estimate cannot be produced ahead of the curvature smoothing; it presupposes it. On the plateau {a=1} the smoothing is exactly Li Theorem 3.6 (nondegenerate). On the transition {0<a<1} the operator is ∂_t−aΔ and the required smoothing R_α≤ε_* ⟹ |aRm|≤C/t is the open object. The weighted Sobolev step is structurally compatible (§3), but the iteration must additionally carry ∇a·∇Rm cutoff commutators across infinitely many steps with step-independent constants. Wang's Theorem 6.3 (= Yang) gives |χ²Rm|_∞≤C̄ t^{−1}[…]β and |χ²Ric|_∞≤C̄ A₀^{n/p} t^{−n/2p}[…]K, with the correct 4D exponent t^{−2/p}, **but under a global Sobolev inequality, a global L^{n/2} curvature threshold, and an L^p Ricci input** (Wang Thm 6.3 conditions 1–3; Prop 4.9 needs |χ²Rm|_∞ first; Lemma 4.11 shows ∇²χ and ∇(χ²Rm) evolve coupled). These are stronger than the relative/collapsed hypotheses here, so the source cannot be cited for a collapse-uniform transition estimate; it must be reproved on relative balls.

### 6. C/t curvature cannot preserve E; p>2 is the integrability threshold

Independent check of the ∫dt/t point. The defect maximum principle from (∗) gives d/dt sup|E|² ≤ B(t) sup|E|² with B ⊃ 4||aRm||_∞ (coefficient 4 is fixed by 4a·Rm(E,E), not tunable). With ||aRm||_∞ ≤ C_L/t,

  ∫_{t₀}^{θr²} B dt = 4C_L·log(θr²/t₀) + …, so sup|E|²(θr²) ≤ sup|E|²(t₀)·(θr²/t₀)^{4C_L}.

As t₀→0 this diverges (∫_0 dt/t = ∞), and the segment [0,t₀] cannot be bridged: collapsed rough initial data give only ∫|Rm|² control, not a pointwise |Rm(0)| bound, so B(t) is not integrable near 0. Even with a fixed t₀>0 the factor (θr²/t₀)^{4C_L} is a positive power of a large ratio, not O(1). Hence **|aRm|≤C/t cannot by itself preserve E**. I note an internal inconsistency to flag: the Step-17 Proposition-1 parenthetical "the integral converges logarithmically and the defect grows only polynomially: ‖E(t)‖≤Cδ" conflates the two — the actual content is |E(t)| ≤ δ·(t/t₀)^{2C_L}, useful only for t comparable to t₀, not a uniform O(δ) bound.

Preservation must instead come from the weighted L^p defect estimate with **supercritical** p:

  |aE(t)| ≤ C_p δ (r²/t)^{2/p} ⟹ ∫_0^{θr²} |aE|_∞ dt = C_p δ · θ^{1−2/p} r² /(1−2/p),

finite iff 1−2/p>0 iff p>2, bounding metric drift by O(δr²). At p=2 the time exponent is exactly 1 (log-divergent). So p>2 is not cosmetic: it is the precise integrability threshold that turns the curvature-driven potential into finite metric motion. This route bypasses the maximum principle and is the correct mechanism for comparability; the C/t bound enters only inside the Moser machinery that manufactures the potential, never as a direct preserver of E.

### 7. Coupled L² and the unweighted-Q separation are conditional

The Step-17 §7 coupled (R,P) closure is internally consistent **given** metric comparability, R_β≤ε_* on neighbors, the relative Sobolev inequality, and the finite-overlap constant N; its absorptions reuse the same √ε_* cancellation. Treated as conditional it is sound. But two points stand: (i) the closure is at the **integral** (L²) level and does not by itself deliver the L^∞ weighted bounds (|aRm|≤C/t, |aE|≤C_pδ(r²/t)^{2/p}) that a first-exit continuation for the pointwise quantities needs, and a first-exit argument requires a **strict** improvement of each maintained bound (as in Li's e₀ < (3C₀A)^{−1}), not merely a reproduction; (ii) the weighted estimate controls only aE, which vanishes as χ→0 and gives no information on the unweighted transition defect. The unweighted Q(t)=∫|E|² needed for topological recalibration is a separate output of the energy inequality (A01 (5.2)); a perfect |aE| bound does not supply it. This separation is real and correctly noted in A01 §5.2/§6.

### 8. Exactly what remains uncontrolled

1. **Transition ε-regularity**: R_α≤ε_* ⟹ |aRm|≤C/t for ∂_t−aΔ on {0<a<1}. Plateau case = Li Thm 3.6; global-hypothesis case = Wang/Yang Thm 6.3; the relative/collapse-compatible version is not in either source and must be proved with step-uniform constants carrying ∇a·∇Rm commutators.
2. **The cutoff first-derivative commutator** a|∇a||∇E| (equivalently the C_a terms −a_k(∇_iE_{kj}+∇_jE_{ki}) and ½(a_iτ_j+a_jτ_i)): absorbable only against the tensor dissipation ∫a|E|^{p−2}|∇E|²; the scalar f=aK reduction cannot supply it, so a supercritical p must be sought at the tensor level.
3. **The maintained inputs** (metric comparability, R_α≤ε_* on neighbors, relative weighted Sobolev, finite overlap) are provisional; a non-circular first-exit needs a strict pointwise improvement, which the L²-level coupled system does not yet give.
4. **Unweighted Q(t)** control on the transition — not implied by any weighted-aE estimate.

What is solid: identity (∗); the homogeneous (no 1/χ) weighted drift-diffusion inequality; the degenerate-dissipation-compatible weighted Sobolev absorption with 4D volume cancellation (coefficient √ε_*); the p>2 integrability giving finite O(δr²) metric drift; and the demonstration that C/t cannot preserve E directly. What is not established: the transition smoothing that would make the supercritical defect estimate — and hence the whole first-exit — actually run under the collapsed, relative hypotheses.