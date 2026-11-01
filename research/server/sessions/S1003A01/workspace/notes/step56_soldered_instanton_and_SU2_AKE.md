# Step 56: the AK-Einstein system as a soldered Λ⁺ instanton, the sourced U(1) current, h-tested identities, and SU(2)-invariant exclusions

Session S1003A01, Agent2. Labels: [P] proved here by hand, [C] exact computer algebra (Singular/sympy), [N] numerical, [K] cited.

## 1. Soldered-instanton formulation  [P]

On an oriented Riemannian four-manifold, g is Einstein exactly when the Levi-Civita connection A⁺ on Λ⁺ has self-dual curvature (Atiyah–Hitchin–Singer). An almost-Kähler structure is a unit section σ = Ω/√2 of Λ⁺ that is closed, hence harmonic. Use the AAD frame (Ω, φ, Jφ) and write the connection as the so(3)-vector A = (A₁, A₂, A₃) = (b, Ja, a). Then

  F = dA + ½ A×A,
  F₁ = db − a∧Ja = −R(Ω),  F₂ = d(Ja) + a∧b = −R(φ),  F₃ = da − Ja∧b = −R(Jφ),

which are exactly AAD's Ricci identities (3.2)–(3.3) of the Step-55 note. Write L = σ^⊥, a complex line bundle with connection b, and α for the L-valued 1-form encoded by (a, Ja). The second fundamental form ∇σ = α has three properties:

* The AK condition puts α in Λ^{0,1}_J ⊗ L, which is half of Ω¹(L). The complex structure J is the one determined by σ itself; this is the soldering.
* The Einstein condition says the off-diagonal curvature d_bα is self-dual: (d_bα)⁻ = 0. These are three complex equations for two complex unknowns, so the system is overdetermined.
* Harmonicity of σ gives the Weitzenböck relation ∇*∇Ω = 2η + (q/2)Ω, whose L-component is d_b^*α = 2η. This is AAD's η = −½ div¹(A).

Hence

  (d_b^* + d_b^-) α = (2η, 0),   α ∈ Ω^{0,1}(L).   (1.1)

The pair (d^*, d^-) on Ω¹(L) is the ASD deformation operator. Its Bochner formula has Ricci term s/4 < 0, and it reproduces Step-55 identity (7.1). The only information beyond ordinary instanton deformation theory is the type restriction α ∈ Ω^{0,1} together with the soldering of J to σ. Any proof or counterexample must use these two features.

## 2. Sourced Maxwell equation for the canonical U(1) curvature  [P]

Write the instanton Bianchi identity d_AF = 0 in its σ-component, using that F₁ is self-dual:

  d^*F₁ = ι_{Ja}F₃ − ι_aF₂.

For a 1-form θ and a self-dual 2-form ψ, *(θ∧ψ) = ι_θψ. Expand F₂ and F₃ in the R⁺ matrix of the AAD frame, and use I₁ = J, I₁I₂ = I₃. The charged current then depends only on (a, η, W₃⁺), with no derivatives:

  j := d^*F₁ = −(R₂₁ + R₃₁J)a + [(R₃₃ − R₂₂)I₂ − 2R₂₃I₃]a   (frame signs convention-dependent),

where (R₂₁, R₃₁) are the components of η and (R₂₂ − R₃₃, R₂₃) are those of W₃⁺. The canonical form is β = −F₁ − a∧Ja − (s/4)Ω. Since s is constant and d^*Ω = 0,

  δβ = −j(η, W₃⁺; a) − d^*(a∧Ja).   (2.1)

This is the "sourced U(1) equation". The canonical connection b is not Yang–Mills: its current is the η- and W₃⁺-weighted charge density of the Nijenhuis field. Because d d q = 0, it yields the neutral identity ∫⟨j, dq⟩ = 0.

## 3. Hodge remainder of β  [P, check of Spirit #66]

Let H be the harmonic representative of [β] and write β = H + dξ. From β⁺ = η + (q/8)Ω, β⁻ = −(q/8)ω̂ and ∫β∧β = ∫|η|² = ‖H⁺‖² − ‖H⁻‖², we get

  ‖dξ‖² = ‖β‖² − ‖H‖² = ∫q²/16 − 2‖H⁻‖² = ∫q²/16 − 8π²‖c₁^{−,h}‖².

This is verified. The nonharmonic part satisfies ‖dξ‖² = ⟨δβ, ξ⟩, and (2.1) supplies δβ. With Ric = s/4 < 0 on 1-forms there is no spectral lower bound, so no estimate follows without new input.

## 4. h-tested Bianchi identity (answer to A02 #836)  [P]

Pair the transverse Bianchi equation (7.4) of the Step-55 note with T_{h(Z)}, where h is a harmonic ASD form and T = ∇Ω, and sum over Z = e_i. A02's algebraic identity Σ⟨T_{Je_i}, T_{he_i}⟩ = −4⟨t⁻, h⟩ turns the κ-term into −κ⟨t⁻, h⟩. With κ = s + 3q/2 = s + 6u this is exactly A02's

  s⟨H⁻(t⁻), h⟩ = F_h − 6∫u⟨t⁻, h⟩,

with

  F_h = ∫[ ¼Σ⟨(dq∧e_i)'', T_{he_i}⟩ + 2Σ⟨(δW₃⁺)_{e_i}, T_{he_i}⟩ + Σ⟨∇_{η(e_i)}Ω, T_{he_i}⟩ + Σ⟨(∇_{Je_i}η)'', T_{he_i}⟩ ].

Integrating the W₃⁺ term by parts gives ∫⟨W₃⁺, (∇T)∘h⟩ + ∫⟨W₃⁺, T∘∇h⟩. Compare the J-test that produced Step-55 identity (7.5):

* In the J-test, W₃⁺(e_j, Je_k) stays self-dual, i.e. skew in (j, k). It therefore pairs only with the skew part of ∇T, which is the curvature term R(e_j, e_k)Ω. The pairing is algebraic and gives the exact value 2∫|W₃⁺|².
* In the h-test, W₃⁺(e_j, h e_k) lies in Λ⁺⊗Λ⁻, i.e. it is trace-free symmetric in (j, k). It pairs with Sym₀∇²Ω, which is not determined algebraically by the AAD system.
* The second term involves ∇h. Since dh = d^*h = 0, ∇h lies in the 8-dimensional twistor component of Λ¹⊗Λ⁻, which is also free.

Hence equations (3.6), (3.8), (7.4) and (7.5) give no intrinsic cancellation of F_h. The h-test brings in exactly two new derivative components: Sym₀∇²Ω contracted through W₃⁺∘h, and the twistor part of ∇h. Any cancellation would need an equation for Sym₀∇²Ω, i.e. the next prolongation of (3.8). That is where an intrinsic relation, if one exists, must appear.

## 5. SU(2)-invariant AK-Einstein metrics (diagonal Bianchi IX)  [C]

Ansatz. g = dt² + a²σ₁² + b²σ₂² + c²σ₃² with dσ_i = 2σ_j∧σ_k; the round metric H⁴ corresponds to a = b = c = sinh t, which was checked. Take an invariant self-dual form Ω = Σx_i w_i, with w_i = e⁰∧e^i + ε e^j∧e^k, ε = ±1 covering both orientations, and Σx_i² = 1. For Bianchi IX the momentum constraint makes the diagonal form the general Einstein case, so this covers SU(2)-invariant metrics with three-dimensional orbits.

* Closure is exactly x_i' = μ_i x_i with μ_i = 2εa_i/(a_ja_k) − (a_ja_k)'/(a_ja_k).
* Unit length requires K₁ = ΣX_iμ_i = 0, where X_i = x_i².
* The script computes q = |∇Ω|² exactly; it is a sum of squares (file `data/step56/setup_eps±1.json`).

Constraint tower. K_{n+1} = D_t K_n along the Einstein flow, with second derivatives eliminated by Ric_ii = λ. The Hamiltonian constraint H = G₀₀ + λ is included. Scripts: `scripts/step56_bianchiIX_ake.py` (frame curvature), `step56_ake_propagate.py` (flow, μ, q), `step56_ake_tower.py` (numerical sampling), `step56_ake_singular.py` (exact Gröbner saturation).

Results:

* **Single direction (Ω = w₁)**, ε = ±1, λ kept symbolic. Take the ideal (H, K₁, …, K₄) in ℚ[a, b, c, A, B, C, λ], saturated by abc. It has Krull dimension 3: the Kähler–Einstein locus. Saturating further by either Kähler defect gives the unit ideal (files `data/step56/sing_single_*`, logs `run_single_*`). **Every solution, complex or real, for every λ, is Kähler.** This does not go beyond AAD. In the diagonal frame W⁺ is diagonal, so w₁ is a W⁺-eigenform and η = 0 automatically; AAD's third-Gray-condition rigidity [K] then applies. The run serves as a consistency check: it exactly reproduces the cited theorem, including the absence of λ = 0 strict solutions in this symmetric class.
* **Two or three directions.** Here Ω is generically not a W⁺-eigenform, so η ≠ 0 a priori. This is the regime beyond the known rigidity.
  - [N] at λ = −3, ε = 1, two directions: imposing (ΣX = 1, H, K₁, …, K₄), every converged Levenberg–Marquardt point with abc bounded away from 0 has X ∈ {0, 1} and q ≈ 10⁻¹⁴, i.e. a Kähler single-direction point. One near-degenerate point, with X₂ = 0.997, rank 6 and next residual 4×10⁻⁶, is isolated, does not lie on an invariant set, and is not a solution curve.
  - [C] The exact saturations for two directions (K₅, λ = −3, both ε) were running at the close of this note; their logs are `data/step56/run_two_eps±1.log`.
* **Other class-A cohomogeneity-one types** (Bianchi I, II, VI₀, VII₀, VIII, all positions of the distinguished direction), single direction, λ symbolic: submitted, with outputs `data/step56/runA_*`. Bianchi II with the centre direction paired with t contains the Bergman CH² as KE control.

**Results (end of Step 56).**
* [C] **Single direction, Bianchi IX, λ symbolic, ε = ±1.** The ideal J has Krull dimension 4 in ℚ[a,b,c,A,B,C,λ], i.e. a KE locus of dimension 3 for each λ. Both strict saturations equal (1). So every solution is Kähler for every λ (files `sing_single_eps±1_lamlam_K4*`).
* [C] **Single direction, all class-A types**, ε = ±1, λ symbolic, distinguished direction in every position (task s56_t20; files `data/step56/singA_*`, logs `runA_*`):
  - the strict saturation is (1), i.e. Kähler only, for (n₁,n₂,n₃) = (1,1,1), (1,1,−1), (−1,1,1), (1,1,0), (1,−1,0), (1,0,0) and (0,0,0);
  - for n₁ = 0 with (n₂,n₃) ≠ (0,0), namely (0,1,0), (0,1,1), (0,1,−1), the strict saturation is a proper ideal containing λ. Example for Bianchi II, ε = 1: ⟨λ, aC + b, cB + bC⟩. Strict solutions therefore exist **only for λ = 0**: these are Ricci-flat, Tod/Gibbons–Hawking-type strictly AK metrics.
  - This reproduces exactly the cited dichotomy "Einstein + η = 0 ⇒ Kähler or Ricci-flat" [K]. The engine detects the known Ricci-flat strict branch and shows it does not deform to λ ≠ 0. This is a strong correctness control for the whole tower method.
* **Two directions (η ≠ 0), Bianchi IX, λ = −3.** The Gröbner saturations did not finish within 3300–3500 s: K₄ and K₅, over ℚ and 𝔽₃₂₀₀₃, both ε, tasks s56_t17 and s56_t29; inputs are `data/step56b/sing_two_*.sing`. The status is therefore [N] only. Every LM-converged point of {ΣX = 1, H, K₁..K₄} with abc bounded below is a Kähler point with X ∈ {0,1}. An exact proof needs a better formulation. Concretely:
  - dehomogenize by scaling (keep λ symbolic and set a = 1, or use the dimensionless variables A, B, C, b/a, c/a);
  - replace X₁ by the rotation angle θ, using θ' = (μ₂ − μ₁) sin θ cos θ and the relation μ₂ sin²θ = −μ₁ cos²θ;
  - eliminate one of B, C linearly using K₁;
  - or certify numerically with homotopy continuation (all isolated solutions of a square subsystem) rather than a Gröbner basis.

Interpretation. The symmetry reduction is a finite exact test of local negative AK Einstein existence with η ≠ 0. If the two- and three-direction saturations are the unit ideal, there is **no SU(2)-invariant strictly almost-Kähler Einstein metric with invariant AK structure, for any λ**. The tower with η ≠ 0 would close on the Kähler locus. That is an exclusion within a natural ansatz, not the general local Goldberg problem.
