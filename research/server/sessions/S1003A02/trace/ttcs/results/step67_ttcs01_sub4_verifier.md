# TTCS Independent Branch Record

```json
{
  "step_id": 67,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step67_cK_local_coercivity_at_cscK.md",
    "Sessions/S1003A02/workspace/notes/step66_rank_one_exceptional_ricci_rigidity.md",
    "Sessions/S1003A02/workspace/notes/step65_cell_exceptional_flux_ledger.md",
    "Sessions/S1003A02/workspace/scripts/step67_cK_symbol_check.py",
    "Sessions/S1003A02/workspace/data/step67_cK_symbol_check.json"
  ]
}
```

## Task

Check, as a careful differential geometer, the new results in step67_cK_local_coercivity_at_cscK.md, which sit on the ledger of step65 §1/§7 and step66 (whose §7 corrections are binding). Setting: compact complex surface, cscK metric g0 with Kähler form omega, primitive Ricci form rho0 = 2*pi*h_a^- != 0 (a = c1), unit exceptional harmonic ASD form hhat, ledger p = q^2(1-delta)^2 + L. Verify or correct, with exact reasons: (1) Lemma 67.1: the inequality 2*pi*q*delta <= (t_J^-, hhat) for every class-a orientation-compatible J (from 65.1 and |Omega_J|=sqrt2), the argument that delta and L have zero first variation at cscK, differentiability of 𝔉 at g0 when Z(hhat) is nonempty, and the identity p - q^2 = C_+ - |c1^+|^2_g, hence 'every cscK metric is a critical point of LeBrun's C_+ - |c1^+|^2 on all metrics'. Is this known in the literature (LeBrun's curvature functionals)? Is it consistent with the first variations of int|W+|^2 (Bach tensor of Kähler metrics) and int s^2? (2) Theorem 67.K(A): Koszul division at transversal zeros; the linearized use of Lemma 66.D (div(phi o psi)=psi(delta phi)) to make the Ricci-aligned SD form first-order closed; the J-invariance claim (J-anti-invariant tracefree symmetric tensors = Omega^perp ⊗ Lambda^-); the reference first-order Kähler deformation realizing an arbitrary class change, especially the H^{2,0} directions via the Beltrami differential omega^{-1} theta-bar; Moser; and the Blair–Ianus Hessian argument: int s dmu = 4 pi c1.[omega] - kappa int|nabla omega|^2 on omega-compatible J (check s* - s >= 0 proportional to |nabla omega|^2 and the topological integral of the Hermitian scalar curvature), first variation d(int s)(gdot) = -int<Ric'',gdot>, and Hess E = 2||(nabla omega)'||^2. (3) Theorem 67.K(B): the Douglis–Nirenberg ellipticity of (DF, s', harmonic gauge) with the principal symbol stated (numerically checked in data/step67_cK_symbol_check.json), the Rellich/finite-kernel step, the order-one upper bound d2 <= (2 pi q)^{-1} tau_ref,2 with the reference structure built from J_K on ker l2, and the exact second-order formula 2 pi q d2 = tau_ref,2 - (1/sqrt2) int |w1|^2/|v0|. Identify any gap (e.g. whether the second-order Taylor statement in C^{2,alpha} is legitimate, whether the slice/gauge handling is right, whether K finite-dimensional is correctly used). Return precise corrections and the strongest correct statements.

## Output

# Verification memo: Step 67 (Lemma 67.1 and Theorem 67.K)

**Main finding.** Lemma 67.1 is correct, and it has an elementary independent proof. Part (B) of Theorem 67.K is correct *given* part (A). Part (A) has one genuine gap, in the holomorphic 2-form (Re H^{2,0}) class directions of Step A2. The ∂̄-closedness argument given there is wrong. The gap is live on the main example Σ_g×Σ_h.

---

## 1. Lemma 67.1

### 1.1 The inequality 2πqδ ≤ (t_J⁻, ĥ)
This is correct.
- (65.1) gives (t_J⁻, ĥ) = 2πq − ∫⟨Ω_J, v⟩ with v = B^*ĥ.
- Pointwise ⟨Ω_J, v⟩ ≤ |Ω_J||v| = √2|v|, so ∫⟨Ω_J, v⟩ ≤ 𝔉 and the inequality follows.

Two conditions are needed:
- J must be g-orthogonal and orientation-compatible, so that Ω_J ∈ Λ⁺ and B Ω_J = ρ₀^J.
- c₁(J) must equal a.

For J = Ĵ_t, the g_t-orthogonalization of J₀, both hold by continuity.

The twist t is quadratic in the torsion for *every* orthogonal J, not only almost-Kähler ones.
- Write Λ⁺ = ℝΩ ⊕ E with ∇Ω = α⊗φ + β⊗ψ.
- The Gauss equation for the subbundle E ≅ K⁻¹ gives F_E = (curvature component ⟨R·φ, ψ⟩, i.e. R(Ω)) ± α∧β.
- There is no term in derivatives of the torsion.

Hence τ_{Ĵ_t} = O(t²), as used in step 3 of the proof.

### 1.2 Zero first variation and differentiability of 𝔉 when Z(ĥ) ≠ ∅
The one-sided argument is valid once δ is differentiable along curves: δ(t) ≤ Ct² for both signs of t gives δ′(0) ≤ 0 and δ′(0) ≥ 0.

Differentiability of 𝔉 = √2∫|v_t| holds even when Z(ĥ) ≠ ∅.
- The functions ĥ_t, q_t and h_a⁻ depend smoothly on g (Hodge theory), so v_t = v₀ + t v₁ + O(t²) uniformly.
- Off Z, (|v_t| − |v₀|)/t → ⟨v̂₀, v₁⟩, with the bound |v₁| + O(t).
- Z has measure zero (dimension ≤ 2), so dominated convergence gives a two-sided derivative ∫_{M∖Z}⟨v̂₀, v₁⟩.

Hence δ and L are Gateaux-differentiable at g₀, and Dδ = DL = 0. The algebra is also correct:
- p − q² = q²(δ² − 2δ) + L, where the variation of q enters only multiplied by δ = 0;
- p = P/8π², so D(P − 8π²|c₁⁻|²) = 0.

### 1.3 The identity p − q² = C₊ − |c₁⁺|²
This is correct.
- Gauss–Bonnet gives ∫|Ric°|² = 2∫|W|² + ∫s²/12 − 16π²χ.
- Combining with 12π²τ = ∫(|W⁺|² − |W⁻|²) gives P/8π² = (2π²)⁻¹∫|W⁺|² + (96π²)⁻¹∫s² − (2χ+3τ) = C₊ − c₁².
- Then |c₁⁻|² = |c₁⁺|² − c₁² gives p − q² = C₊ − |c₁⁺|².

### 1.4 Independent elementary proof and consistency with the variations of ∫s² and ∫|W⁺|²
Split the functional as

C₊ − |c₁⁺|² = (2π²)⁻¹[∫|W⁺|² − (4π²/3)|c₁⁺|²] + (96π²)⁻¹[∫s² − 32π²|c₁⁺|²].

The coefficients check: 2/3 + 1/3 = 1.

**The s² part.** At a metric with s constant,
- s′ = −Δ tr ġ + δδġ − ⟨Ric, ġ⟩ and dμ′ = ½ tr ġ dμ;
- hence d∫s² dμ = −2s∫⟨Ric°, ġ⟩.

**The |c₁⁺|² part.** For the harmonic representative ψ of a fixed class, the exact part of ψ′ pairs to zero against the coclosed ψ. With form norms one gets

d∫|ψ|² = 2∫⟨ψ⁺∘ψ⁻, ġ⟩.

Hence d|c₁⁺|² = ∫⟨ψ⁺∘ψ⁻, ġ⟩. At cscK:
- ψ = ρ/2π, with ρ⁺ = (s/4)ω and ρ⁻ = ρ₀;
- with the matrix relation Ric° = −ω∘ρ₀ (from ρ = Jᵀ Ric), this gives d|c₁⁺|² = −(s/16π²)∫⟨Ric°, ġ⟩.

This equals d[(32π²)⁻¹∫s²]. So **∫s² − 32π²|c₁⁺|² is critical at every cscK metric, for any sign of s.** This is the variational shadow of LeBrun's estimate ∫s² ≥ 32π²(c₁⁺)², whose equality case is cscK for s < 0 under SW ≠ 0; that reference should be retrieved before citing.

**The Weyl part.** Lemma 67.1 is therefore equivalent to criticality of W(g) := ∫|W⁺|² − (4π²/3)|c₁⁺|²_g at cscK.
- The standard Kähler-surface Bach formula (Derdziński; retrieve with constants) has tracefree part a combination of sRic° and (∇²s)₀. So at cscK the gradient of ∫|W⁺|² is c·sRic° for a universal c.
- W vanishes identically on cscK metrics, since ∫|W⁺|² = ∫s²/24 on Kähler metrics.
- Take any cscK curve with ∫⟨Ric°, ġ⟩ ≠ 0, for example factor scaling g₁ ↦ λg₁ on Σ_g×Σ_h with K₁ ≠ K₂, where Ric° ∝ (K₁ − K₂)(g₁ − g₂). This forces c = −1/12.

All three gradients are multiples of sRic°, and the coefficients cancel. This confirms Lemma 67.1 independently of the ledger. It also shows the lemma holds at *every* cscK metric on any compact Kähler surface: s of either sign, Kähler–Einstein included (trivially, since Ric° = 0).

**Literature.** I find no exact statement of "cscK is critical for C₊ − |c₁⁺|²" in the supplied material. Its content is the classical ∫s² computation above plus the Kähler Bach formula. The new information is the coefficient match, which the scaling argument settles.

The "Checks" bullets in the note are correct:
- On Kähler metrics, C₊ − |c₁⁺|² = (32π²)⁻¹∫s² − |c₁⁺|² ≥ 0 by Cauchy–Schwarz with ∫s dμ = 4πc₁·[ω].
- The conformal-direction check is also correct.

### 1.5 Second-order consequences
- (p − q²)₂ = ℓ₂ − 2q²d₂ is correct, because (δ²)₂ = (δ′)² = 0.
- "Local minimizer ⇔ c_K ≥ 2" holds on 𝒮, and transfers to all metrics through the Yamabe map only when s₀ < 0, because 66.Y uses ∫s² ≥ Y² with Y < 0.
- The displayed bound p ≥ q²[1 − (2 − c_K)₊δ] + O(δ²) is not what the expansion gives. The remainder is O(‖ġ‖³), not O(δ²): along K the quantity δ vanishes to second order while the remainder does not. See §3.5 for the correct local form.

---

## 2. Theorem 67.K(A)

### 2.1 Step A1 (Bianchi)

**Linearization of B_⊥.** B_⊥ is taken relative to h_t, which varies with t. The first-order condition DF(g₀)k = 0 therefore reads

π_⊥(B′ − c₀ω⊗h′) = 0, equivalently B′ = φ′⊗h + c₀(Ω′⊗h + ω⊗h′).

It is not "B′ ∈ Λ⁺⊗ℝh", as the note states.
- The later ansatz Ric°_t = Φ_t∘h_t + O(t²) uses h_t and is consistent with the corrected form.
- Koszul division should be applied to B′ − c₀(ω⊗h)′.

**Validity of ℓ₂ = ‖DF k‖² at a transversal Z.** This holds.
- F(g_t) is bounded; |B_⊥| ≤ |B|, and the amplitude term carries the factor |h|.
- The Taylor remainder is O(t²/|h|), which is square-integrable across a codimension-3 Z.
- The region {|h| < t} has volume O(t³).

**Koszul division.** The smooth-germ ring is not Noetherian, so the algebraic Koszul theorem does not apply directly. A Hadamard argument works instead. At a transversal zero take h_i = x_i as coordinates. The rank-one condition v_i x_j = v_j x_i gives:
- v_i = 0 on {x_i = 0}, hence v_i = x_i f_i;
- x_i x_j(f_i − f_j) = 0, hence f_i = f_j by continuity.

So the coefficient f is smooth. Transversal zero sets are curves, of codimension 3.

**Linearized use of 66.D.** This is correct.
- First-order coefficient: h₀((δΦ)′) + h′(δΦ₀) = 0 with δΦ₀ = c₀δω = 0, so (δΦ)′ = 0 off Z, and everywhere by continuity.
- Since δ_tΦ_t = −*_t dΦ_t and dΦ₀ = 0, we get (dΦ)′ = 0.

**Amplitude.** |Φ₀| = √2c₀ ≠ 0 everywhere, Z included, so Ω_t = √2Φ_t/|Φ_t| is smooth with (dΩ)′ = 0.

**J-invariance.** This is correct.
- Sym₀ ≅ Λ⁺⊗Λ⁻ = (ℝΩ⊗Λ⁻) ⊕ (Ω^⊥⊗Λ⁻), of dimensions 3 + 6.
- Ω∘ψ commutes with J ∝ Ω, because SD and ASD forms commute.
- σ∘ψ with σ ⊥ Ω anticommutes with J, by the quaternion relations in Λ⁺.

Hence Ric''_t = O(t²).

### 2.2 Step A2: the Re H^{2,0} directions — this is the gap

**What is correct.**
- The decomposition of [Ω̇] as λω + H₀ + Re θ is correct.
- The real (1,1) part is realized by the Kähler curve ω + t(λω + H₀) at fixed J₀.
- Moser is correct: ι_Xω = −ϑ gives L_Xω = −dϑ.
- The differential of Ric'' vanishes on first-order-Kähler directions. The reason is not "Ric'' ≡ 0 on the Kähler locus", since a first-order Kähler vector need not be tangent to an actual Kähler curve. The correct reason: if (∇J)′ ≡ 0 as a tensor field, its derivatives vanish too, so [R, J]′ = 0 and (Ric'')′ = 0.

**The Re θ realization is wrong.**
1. The relevant integrability operator is ∂̄ on T^{1,0}-valued (0,1)-forms. Applied to μ = g⁻¹θ̄ it uses ∇^{0,1}θ̄ = conj(∇^{1,0}θ). This is not the de Rham ∂̄θ̄, which is a (0,3)-form and vanishes trivially in complex dimension 2.
2. For holomorphic θ, ∇θ = β⊗θ with β = ∂ log|θ|² ≠ 0 unless |θ| is constant. A direct index computation gives (∂̄μ)^i ∝ g^{i l̄} β̄_{l̄} θ̄₁₂ ≠ 0.
3. Gray–Hervella gives an independent check. In dimension 4, ∇ω ∈ W₂ ⊕ W₄, where dω = 0 kills W₄ and N = 0 kills W₂. At fixed metric (∇ω_t)′ = ∇Re θ ≠ 0 while d Re θ = 0, so N′ ≠ 0.

The correct realizability question is cohomological.
- A first-order Kähler deformation with [Ω̇]^{0,2} = [θ̄] exists iff [θ̄] lies in the image of the cup map H¹(T) → H^{0,2}, [μ] ↦ [μ⌟ω].
- On Σ_g×Σ_h (g, h ≥ 2) this map is **zero**: H¹(T) = H¹(TΣ_g) ⊕ H¹(TΣ_h), and μ from one factor contracted with ω₁ + ω₂ vanishes by type.
- Meanwhile p_g = gh > 0.

So on the very example cited for (B), no Re θ class direction is realizable by a first-order Kähler deformation.

**Correct form (A′).** The conclusion of (A) holds for k ∈ ker ℓ₂ whose induced class change has (0,2)-component in the image of H¹(T)⌟[ω]. In particular it holds whenever p_g = 0, or for k whose induced [Ω̇] has no Re H^{2,0} component.

**Content of the remaining case.** A k ∈ ker ℓ₂ with [Ω̇]^{0,2} outside that image would have nonzero first-order torsion. If its torsion vanished it would be first-order Kähler with a non-realizable class, which is impossible. Such a k is then exactly a first-order strictly almost-Kähler, J-invariant-Ricci, aligned deformation: the seed of step 66 §9. Deciding it is a linear Fredholm problem:
- Linearize Ric''(J) = 0 on 𝒥_{ω + t Re θ} at J₀.
- The linear operator is proportional to the Hessian operator (∇ω)′*(∇ω)′. It is self-adjoint, and its kernel is the first-order Kähler J̇ at fixed ω.
- A first-order Blair–Ianus deformation exists iff the source term is orthogonal to that finite-dimensional kernel.
- One must add constant-s′ and [ρ₀] ∥ a⁻ conditions (66.R(d)).

On Σ_g×Σ_h with θ = α⊗β (α, β holomorphic 1-forms on the factors), this is an explicit computation in eigenmodes of the two factors.

### 2.3 Step A3 (Blair–Ianus Hessian)
This is correct, given the reduction to Ω̇ = 0.
- For an AK structure, s* − s = ½|∇ω|² ≥ 0 (norm convention aside).
- The Hermitian scalar curvature (s + s*)/2 integrates to 4πc₁·[ω] with dμ = ω²/2.
- Hence ∫s = 4πc₁·[ω] − κE with κ > 0; only κ > 0 is used.
- Compatible variations at fixed ω are J-anti-invariant, hence tracefree, so d∫s dμ = −∫⟨Ric − ½sg, ġ⟩ = −∫⟨Ric'', ġ⟩.
- At J₀ we have E = 0 and dE = 0, so Hess E depends only on J̇. It equals 4∫⟨(Ric'')′, ġ⟩, the term Ric''₀·g̈ vanishing, and also 2∫|(∇ω)′|².
- The step from the vanishing torsion of the reference and Moser parts to the vanishing torsion of k uses linearity of the first-order torsion at a Kähler point. This is correct.

### 2.4 "ker ℓ₂ ⊂ radical of d₂"
This is not proved within (A) alone.
- (A) gives only d₂(k) ≤ 0, through τ = O(t⁴).
- d₂(k) = 0 follows from the exact formula of §3.4: w₁ = 0, because the Ricci-aligned structure coincides with the reference to first order, and τ_ref,2 = 0.
- The radical property then follows from d₂(k + εv) ≤ Cε²‖v‖², by (B2).

It belongs to (B) and inherits the A2 gap.

---

## 3. Theorem 67.K(B)

### 3.1 Symbol and ellipticity
The hand check agrees with the JSON output.

**Symbol.** In harmonic gauge Ric′ = ½∇*∇ġ + lower-order terms. The harmonic-form variation h′ is of order 0 in ġ (h′ = dG(first-order expression in ġ) plus a harmonic projection), so it is not principal.

**Kernel computation.** If the symbol of ġ vanishes:
- ġ° = σ∘ĥ with σ ⊥ Ω;
- the gauge row gives ġξ = ½τξ, so ġ(ξ,ξ) = τ/2;
- the scalar row gives τ − τ/2 = 0, so τ = 0;
- then (σ∘ĥ)ξ = 0, and since (σ∘ĥ)² is a positive multiple of |σ|²|ĥ|² Id, σ = 0.

**Role of the scalar row.** It is indispensable. Without it the gauge row reduces to (σ∘ĥ)ξ = (τ/4)ξ, which has solutions for ξ an eigenvector of σ∘ĥ. So the Gårding inequality genuinely lives on the constant-scalar slice.

**Estimate and kernel.** With Douglis–Nirenberg weights (rows of order 2, 2, 2, 1), an injective symbol gives

‖ġ‖_{H²} ≤ C(√ℓ₂ + ‖ġ‖_{L²}) on 𝒮,

where |s′| ≤ C‖ġ‖_{L²}. Rellich then gives that K is finite-dimensional and that (67.2) holds. This is correct for Z = ∅.

### 3.2 Step B2
This is correct, given (A) on K.
- J̇_K is linear on the finite-dimensional K.
- Θ′(ġ) = Θ′_⊥(ġ − π_K ġ).
- Inequality (67.1) along the curve g₀ + tġ gives d₂ ≤ τ_ref,2/(2πq) ≤ C‖Θ′_⊥η‖²_{L²} ≤ C‖η‖²_{H¹}.

This is a stronger fact than d₂ ≤ Cℓ₂: d₂ is H¹-bounded while ℓ₂ is H²-coercive on K^⊥. The pencil ℓ₂ − λq²d₂ is therefore compact-relative. Consequences:
- **c_K is attained** by an eigenvector whenever d₂ > 0 somewhere;
- the spectrum on the side d₂ > 0 is discrete.

This makes c_K a computable minimum on Σ_g×Σ_h.

### 3.3 Exact second-order formula
I rederived it.
- Subtract (65.1) for J^ref from 2πq_tδ_t = 2πq_t − √2∫|v_t|.
- Expand with Ω_ref = Ω₀ + tΩ₁ + t²Ω₂, where Ω₁ ⊥ Ω₀ and ⟨Ω₂, Ω₀⟩ = −½|Ω₁|².
- The t² coefficient completes to a square:

2πq d₂ = τ_ref,2 − (1/√2)∫|w₁|²/|v₀|,  with w₁ = v₁^{⊥Ω₀} − (|v₀|/√2)Ω₁.

This w₁ is exactly the first-order component of v_t orthogonal to Ω_ref,t, as stated.

For a transversal Z the formula extends:
- v₀ ∝ |ĥ|²ω;
- B₀^*ĥ′ lies along ω, and B′^*ĥ = O(|ĥ|);
- hence |w₁|²/|v₀| = O(1), which is integrable.

### 3.4 Taylor statement, slice and gauge
**Taylor expansion.** For Z = ∅ both L and δ are integrals of smooth functions of the 2-jet of g and of ĥ_g (with |v₀| > 0 everywhere). They are therefore C³ in C^{2,α}, and C² already suffices.

**Applying it to actual constant-scalar metrics.** For g near g₀, write g = φ*(g₀ + ġ + O(‖ġ‖²)) with ġ ∈ 𝒮, using the Ebin slice and diffeomorphism invariance of L and δ. Because DL = Dδ = 0, the quadratic correction enters only at cubic order. So the slice handling is right.

**What the remainder does along K.** The statement L ≥ cq²δ − C′‖ġ‖³ carries no information along K, where ℓ₂ = d₂ = 0.

**Strongest correct local statement.** Assume (A′) covers K, H⁰(T) = 0 and the Kuranishi family is unobstructed; on Σ_g×Σ_h with g, h ≥ 2, deformations are products. Then:
- K is the tangent space at g₀ of the cscK manifold 𝒞 (LeBrun–Simanca);
- L = δ = 0 on 𝒞;
- L ≥ c·dist²_{H²}(·, 𝒞) and δ ≤ C·dist²_{H¹}(·, 𝒞);
- by Morse–Bott, L ≥ c′q²δ holds with no remainder on a C^{2,α} neighbourhood of g₀ in the constant-scalar metrics, for every c′ < c_K.

### 3.5 Corrected local tariff
p ≥ q²[1 − (2 − c_K)₊δ] − C‖ġ‖³, or, under the Morse–Bott hypotheses of §3.4, without the remainder.

---

## 4. Summary of corrected statements

- **Lemma 67.1:** true at every cscK metric on any compact Kähler surface. It is equivalent to criticality of ∫|W⁺|² − (4π²/3)|c₁⁺|² at cscK, the ∫s² part being classical.
- **(A):**
  - A1 holds with the corrected linearization B′ − c₀(ω⊗h)′.
  - A3 is correct.
  - A2 fails for Re H^{2,0} class directions outside image(H¹(T)⌟[ω]); on Σ_g×Σ_h this is all of them.
  - (A′) holds for p_g = 0, or for k with no such component.
- **(B):** correct conditional on (A) on K. c_K is an attained eigenvalue of a compact pencil. The remainder form is legitimate. Under the Morse–Bott hypotheses, the remainder-free form holds.
- **Unresolved:** the linear Fredholm solvability of the Blair–Ianus equation on 𝒥_{ω + t Re θ} at J₀, with the constant-s and alignment constraints, on Σ_g×Σ_h. If it is solvable, the infinitesimal seed exists there. If not, (A) and (B) hold on the product and c_K reduces to a modal computation.