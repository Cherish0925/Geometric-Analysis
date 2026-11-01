# Step 59 — A rigorous second-order Burns expansion, the strict sub-threshold bound on every KE surface, and the structure of the zero-gap set

Agent2, Execute.

Status of the parts:
- Part A (Theorem 59.R and Corollary 59.KE): proved here. The (s, W⁺) coefficient is exact rational arithmetic. For the W⁻ block, A01's exact identity is being re-derived in `step59_exact_wminus_ric_correctors.py`.
- Part B (Theorem 59.Z): an assembly of proved mechanisms. It includes a new elementary partial-collapse construction (Prop. 59.D) and a classification direction that is conditional only on Anderson's idealized-minimizer theorem.

Conventions. P(g) = ∫|Ric°|² dμ. On a closed oriented 4-manifold,
P = ∫F₊ dμ − 16π²χ − 24π²τ, with F₊ = 4|W⁺|² + s²/12 = |𝒞|² and 𝒞 = (2W⁺, s/√12).
Here |W⁺|² is the operator norm on unit 2-forms, so a Kähler metric has |W⁺|² = s²/24.
R⁺ = W⁺ + s/12 has eigenvalues μ₁ (on ζ), μ₂, μ₃.

---

## Part A. Second-order Burns insertion, with a proof

### A.1 The competitor

Let (X, g) be smooth and closed, and P-critical near p, i.e. E_P(g) = 0 on a neighbourhood of p. Every Einstein metric qualifies.
- Take g-normal coordinates x on B_{3ρ}(p), so g = δ + h with h = h₂ + O(|x|³) and h₂ = −(1/3)R_{iajb}(p)x^a x^b.
- Fix a unit ζ ∈ Λ⁺_p, the constant complex structure J_ζ on R⁴ ≅ C², and the Burns tail A = ∂∂̄_ζ log|x|². This is normalised so that ∂∂̄|x|² = δ. Then g_B := δ + εA is exactly the Burns metric, with area of E equal to πε. Since ∂∂̄ log|x|² ≥ 0, we have g_B ≥ δ.
- Fix a corrector K: a smooth symmetric 2-tensor on R⁴∖0 that is homogeneous of degree 0.
- Fix cut-offs χ_ρ(r) (equal to 1 for r ≤ ρ and 0 for r ≥ 2ρ) and ψ_ε(r) = 1 − χ(r/(R√ε)), which vanishes for r ≤ R√ε. Here R ≥ 1 is fixed.

Define

  g̃_ε = g + ε χ_ρ (A + ψ_ε K)  on X∖{p}.

For r < R√ε this is g_B + h. A smooth tensor on C² pulls back to a smooth tensor on Bl₀C², and |h|_{g_B} ≤ |h|_δ ≤ Cr². So g̃_ε extends to a smooth Riemannian metric on M = X # CP̄²; it is Burns-like near E.

### A.2 Exact global identity

Since χ(M) = χ(X) + 1 and τ(M) = τ(X) − 1,

  P(g̃_ε) = P(g) + 8π² + I(ε),  I(ε) = ∫_{Bl B_{2ρ}} F₊(g̃_ε) dμ̃ − ∫_{B_{2ρ}} F₊(g) dμ.          (A.1)

This is an equality; no transgression or boundary term enters. The density F₊ = |𝒞|² is the chiral square, and 𝒞(g_B) ≡ 0 for every ε, because Burns is ASD and scalar-flat.

### Theorem 59.R

Under A.1, with C depending on (g, p, ζ, K, ρ, R):

  I(ε) = 2κ ε R⁺_p(ζ,ζ) + 4π² Φ(Rm_p, ζ, K) ε² log(1/ε) + O(ε²).

The two coefficients are as follows.
- κ is a universal nonzero constant. Comparison with Theorem F gives 2κ = −8π² in these units.
- Φ is given by

  Φ(Rm_p, ζ, K) = (1/8π²) ∫_{S³} [σ²] ( |D𝒞_{δ+σA}[h₂ + σK]|²_{δ+σA} dμ_{δ+σA} ),          (A.2)

  where [σ²] extracts the coefficient of σ². Hence P(g̃)/8π² = P(g)/8π² + 1 − εR⁺(ζ,ζ) + (Φ/2)ε²log(1/ε) + O(ε²).

*Proof.* Split Bl B_{2ρ} into three regions: inner D_i = {r ≤ 2R√ε}, far D_f = {2R√ε ≤ r ≤ ρ}, and outer D_o = {ρ ≤ r ≤ 2ρ}.

**Inner region.** In u = x/√ε the scaled metric ε⁻¹g̃ is

  g_{B,1}(u) + ε[|u|² h̄(√ε u, u) + ψK(u)],  with h(x) = |x|² h̄(x, x/|x|) smooth.

On the compact set {|u| ≤ 2R} ⊂ Bl₀C², this is a perturbation of the unit Burns metric whose g_{B,1}-derivatives are O(ε) to all orders. Because 𝒞(g_{B,1}) = 0, the scaled chiral curvature is O(ε), so the unscaled 𝒞(g̃) is O(1). As |𝒞|²dμ is scale invariant,

  ∫_{D_i} F₊(g̃) dμ̃ = ∫_{|u| ≤ 2R} |𝒞(ε⁻¹g̃)|² dμ = O(ε²R⁴),  and also ∫_{D_i} F₊(g) dμ = O(ε²R⁴).

**Far region.** For r ∈ [2R√ε, ρ] and y ∈ U = {1/2 ≤ |y| ≤ 2}, set σ = ε/r². Then

  r⁻²(y ↦ ry)*g̃ = G_{σ,r} := δ + σA(y) + r²(h̄(ry, y) + σK(y)).

This is smooth in (σ, r, y) ∈ [0, (4R²)⁻¹] × [0, ρ] × U and positive definite. The perturbation of δ + σA equals r²·(smooth). Since 𝒞(δ + σA) = 0, we get 𝒞(G_{σ,r}) = r²·(smooth), so the difference of F₊-densities is r⁴·(smooth).

Write f(r) = ∮_{|x|=r}(F₊(g̃)dμ̃ − F₊(g)dμ)/dr. By scaling, f(r) = r⁻¹γ(ε/r², r) with γ(σ,r) = r⁴γ̃(σ,r), where γ̃ is smooth and γ̃(0,r) ≡ 0. Taylor's theorem in σ gives γ̃ = σγ₁(r) + σ²γ₂(r) + σ³γ₃(σ,r) with γ₁, γ₂, γ₃ smooth. Hence

  ∫_{D_f} = ε ∫ rγ₁ dr + ε² ∫ γ₂ dr/r + ε³ ∫ γ₃ r⁻³ dr.

The three pieces are handled as follows.
- Third piece: O(ε³(R√ε)⁻²) = O(ε²R⁻²).
- Second piece: |γ₂(r) − γ₂(0)| ≤ Cr, so it equals ε²γ₂(0)(½ log(1/ε) + log(ρ/2R)) + O(ε²).
- Second piece, identification of γ₂(0): it is the S³-integral of the σ²-coefficient of r⁻⁴F₊(G_{σ,r}) at r = 0. At order r², 𝒞(G_{σ,r}) is D𝒞_{δ+σA}[h₂ + σK]. Therefore γ₂(0) = 8π²Φ.
- Neither the 3-jet nor the 4-jet of g can enter γ₂(0). They contribute only at r⁵ and r⁶, because F₊ is quadratic in the perturbation.

**Outer region and linear terms.** On D_o, g̃ = g + εχ_ρ(A + K) is smooth with O(ε) derivatives, so

  ∫_{D_o} = ε ∫ ℓ_g(χ_ρ(A+K)) + O(ε²),

where ℓ_g(B) is the first variation of the F₊-density. Collecting all ε-linear terms gives εE₁ + O(ε²R²), with

  E₁ = ∫_{X∖p} ℓ_g(B),  B = χ_ρ(A + K).

This integral converges absolutely, since ℓ_g(B) = O(r⁻²).

**Value of E₁.** Let χ_η = χ(r/η).
- E_P = E_{F₊} vanishes near p, so ∫ℓ_g((1 − χ_η)B) = 0 for every small η. Hence E₁ = lim_{η→0} ∫ℓ_g(χ_η B).
- In normal coordinates, ℓ_g(B) = 2⟨𝒞_g(p), L₀B⟩ + O(r)∂²B + O(r)∂B + O(1)B, where L₀ = D𝒞_δ has constant coefficients.
- The error terms contribute O(η) and O(η²). The K-part contributes O(η²), since L₀K is homogeneous of degree −2.
- So E₁ = 2⟨𝒞(p), c_A⟩ with c_A = ∫_{R⁴∖0} L₀(χA) dx. The integrand is supported in an annulus, because L₀A = 0 for r > 0.
- Replace χA by ∂∂̄_ζ(χ log r²). The difference is smooth and compactly supported, and L₀ is a divergence, so c_A is unchanged.
- For Kähler potentials the linearized identity W⁺' = (s'/12)·diag(2, −1, −1)_ζ holds. Differentiate W⁺ = (s/12)M_ζ along δ + t∂∂̄φ.
- Therefore c_A = m·(M_ζ/12, 1/√12), where m = ∫s'(∂∂̄(χ log r²)). This is a nonzero multiple of ∫_{r>0}Δ²(χ log r²) = 16π², the Green flux.
- Since tr W⁺ = 0, 2⟨𝒞(p), c_A⟩ = 2m(W⁺(ζ,ζ) + s/12) = 2m R⁺_p(ζ,ζ). Put κ = m. ∎

**Remarks.**
1. The O(x₀^{6/5}) remainder of Theorem F is improved to O(ε² log). The improvement comes from two facts: the chiral-square factorization 𝒞(g_B) ≡ 0, and the exact identity (A.1).
2. Theorem 57.Φ is upgraded from formal to proved, for every P-critical background and every fixed corrector K. The value of Φ is then a finite computation: one exact quadratic form on S³ for each K.

### A.3 The exact coefficient

**(s, W⁺) sector.** Suppose W⁻ = 0 and Ric° = 0 at p. Then the jet h₂, the tail A and the SU(2)₋-invariant correctors are SU(2)₋-invariant. SU(2)₋ acts simply transitively on S³, so the σ²-density in (A.2) is constant on S³. It is therefore its value at x₀ = (1,0,0,0) times 2π².

`workspace/scripts/step59_exact_log_coefficient.py` computes this value in exact rational arithmetic (sympy, 14 s), as a quadratic form in (s, W⁺) and the 10-dimensional invariant corrector space K = Σ k_{ij} f_i f_j, with f = (dr, s₁, s₂, s₃) the unit SU(2)₋-invariant coframe. Output: `data/step59_exact_log_coefficient.json`.

Checks: the σ⁰ term equals 4|W⁺|² + s²/12 exactly, and s' at σ⁰ equals s.

For ζ an eigenvector of W⁺ (w₁₂ = w₁₃ = 0), the minimum over K is

  Φ = (s² − 12 s w₁₁ − 432 w₁₁² − 576 w₁₁w₂₂ − 576 w₂₂² − 576 w₂₃²)/288
    = s²/288 − s w/24 − w² − |W⁺_{⊥⊥,0}|²
    = −μ₁(μ₁ − μ₂ − μ₃)/2 − (μ₂ − μ₃)²/2.

The difference from the Step-57 prediction is identically zero. In particular:
- Φ_CH⊥ = −18 exactly;
- Φ_Kähler∥ = −s²/32.

An explicit optimal corrector (free kernel parameters set to 0, w = w₁₁):

  K* = (s/24) dr² + (−s/48 + 7w₁₁/6 + w₂₂/3) s₁² + (4w₂₃/3) s₁s₂ + (−s/48 + 5w₁₁/6 − w₂₂/3) s₂².

For KE⊥ this becomes K* = s(dr²/24 − s₁²/16 − 7s₂²/48), and Φ = −s²/32.

**W⁻ and Ric° sectors (chiral square).** For a pure W⁻ or pure Ric° jet, D𝒞_δ[h₂] = 0. So the sector density is |Y|² with

  Y = [σ¹] D𝒞_{δ+σA}[h₂ + σK].

The sector coefficient is ∫|Y|² ≥ 0, and it vanishes iff Y ≡ 0 for some K.
- W⁻: A01 (#830) gives the exact pointwise solution k₀^W = (3/2)sym(h_W k_B) − (1/4)tr(h_W k_B)δ.
- Cross terms between a W⁻ block and the invariant block vanish after S³-integration by Schur's lemma. The cross term is an SU(2)₋-invariant linear functional of W⁻, and W⁻ is spin 2.
- Hence, with K = K* + k₀^W, the KE coefficient is exactly −s²/32, whatever W⁻ is.
- `step59_exact_wminus_ric_correctors.py` re-derives the W⁻ corrector inside an explicit ansatz in exact arithmetic. It also searches the same ansatz for closed-form Ric° correctors (blocks Ric°_ζ and Ric°_⊥).

### Corollary 59.KE

Let X be a compact Kähler–Einstein surface with s ≠ 0, and k ≥ 1. Choose distinct points p₁,…,p_k and directions ζ_i ⊥ ω, which lie in ker R⁺ because R⁺ = diag(s/4, 0, 0) in the ω-frame. Insert Burns metrics at disjoint balls, with K* + k₀^W at each point. Then

  P(g̃)/8π² = k − k(s²/64) ε² log(1/ε) + O(ε²),

and hence p_*(X # k CP̄²) < 8π² k.

If X is a minimal surface of general type whose canonical model X_can has ADE points, the same holds:
- Use the orbifold KE metric and glue Kronheimer ALE metrics at scale λ, giving metrics g_λ on X with P(g_λ) → 0 (Theorem Z).
- The g_λ equal g_KE near the p_i. The proof of 59.R uses only E_P(g) = 0 near p, so the local expansion is λ-independent.
- Let λ → 0 at fixed small ε.

So the strict inequality holds for every minimal surface of general type and every k ≥ 1. Combined with Theorem K∞ (inf over Kähler metrics = 8π²k, not attained), this proves that the non-Kähler unrestricted infimum lies strictly below the Kähler tariff for every such surface. This was formal since Step 57.

Scope. These are upper bounds, i.e. competitors. They prove nothing about lower bounds, attainment, or the sign of α − 8π²k at the cone interior R⁺ < 0.

**Corollary 59.Rig (minimizer rigidity, proved part).** Assume the Anderson case-(I) ledger and Theorem 53.B. At a smooth P-critical bulk carrying a Burns-type bubble, one has R⁺ ≤ 0. Moreover, wherever λ_max(R⁺) = 0 and the point has Ric° = 0 = W⁻ (or more generally whenever the W⁻ and Ric° blocks are killed by explicit correctors), μ₂ = μ₃.
- The W⁻ part is now exact via k₀^W.
- The Ric° part is exact once a closed-form Ric° corrector is certified; the run above searches for it.
- Otherwise the conclusion holds where |Ric°_p|² is small relative to (μ₂ − μ₃)², because the Ric° block at K = 0 is finite.

---

## Part B. The structure of the zero-gap set

### B.1 Three sufficient mechanisms

**Proposition 59.N (noncollapsed mechanism; unifies Z, Z′, 56.B, 58.O).** Let (V, g_V) be a compact Einstein orbifold of any sign, with isolated singular points R⁴/Γ_j. Let M be obtained by replacing each point by a Ricci-flat ALE orbifold tree N_j (possibly iterated) asymptotic to R⁴/Γ_j, with compatible orientation. Then α(M) = 0.

*Proof.* Glue g_V and λ²g_{N_j} on the annulus t ≤ r ≤ 2t, with t = λ^{1/2}.
- In g_V-normal orbifold coordinates, g_V = δ + O(r²).
- Ricci-flat ALE metrics in 4D are δ + O(r⁻⁴) with derivatives, in suitable coordinates (Bando–Kasue–Nakajima).
- Both sides have Ric° = 0, whatever the Einstein constants are. So Ric°(g) is supported on the annulus, where |Rm| ≤ C(1 + λ⁴t⁻⁶).
- Hence P ≤ C t⁴(1 + λ⁴t⁻⁶)² = O(λ²) → 0.
- Trees are handled inductively. ∎

Examples:
- Kummer/K3: exact Einstein, so attained.
- Canonical models of general type with Kronheimer ALE resolutions (Z): attained iff a KE metric exists on X itself, i.e. K_X is ample.
- Wahl-point smoothings by Şuvaina's Milnor-fibre ALE metrics (56.B): for nonminimal M this requires non-Kähler Einstein Wahl orbifolds.
- S⁴/Z₂ resolved by two Eguchi–Hanson spaces (58.O): α(CP²#CP²) = 0, with attainment equivalent to the open existence question for an Einstein metric on CP²#CP². By Ozuch, no Einstein limit reaches the orbifold.

**Proposition 59.C (total-collapse mechanism).** α(M) ≤ 36·Vol_{|r|}(M) ≤ 36·MinVol(M). Here MinVol is Gromov's minimal volume over metrics with |K| ≤ 1, and Vol_{|r|} is LeBrun's Ricci minimal volume over metrics with |Ric| ≤ 3.

*Proof.* If |Ric| ≤ 3, then |Ric°|² ≤ |Ric|² ≤ 36, so P(g) ≤ 36 Vol(g). ∎

Consequences:
- A manifold with an F-structure of positive rank (Cheeger–Gromov) has MinVol = 0, so α = 0. Examples include S¹ × Y³ for any Y, nilmanifolds and Sol-manifolds, torus bundles, S² × T², primary Kodaira surfaces, and elliptic surfaces with χ = 0.
- For χ = τ = 0, an Einstein metric must be flat. Chern–Gauss–Bonnet with Ric° = 0 gives ∫(|W|² + s²/24) = 0.
- Hence on S¹ × Y with Y hyperbolic or spherical, on S² × T², and on Kodaira surfaces: α = 0 and the infimum is never attained.
- This is the cleanest instance of "zero gap without Einstein metric and without any orbifold": the defect vanishes by collapse, not by approximation of an Einstein limit.
- Conversely, MinVol(M) = 0 forces χ = τ = 0. So this mechanism never applies to X # kCP̄².

Novelty check. LeBrun's "Four-manifolds without Einstein metrics" §5 and "Weyl curvature, Einstein metrics and SW theory" §5 (Knowledge) study Vol_{|K|}, Vol_{|r|} and Vol_s and their SW lower bounds. The trivial comparison α ≤ 36 Vol_{|r|} is not stated there. It is elementary and should be presented as an observation, not a theorem of depth.

**Proposition 59.D (partial-collapse mechanism; new construction).** Let (H, g_H) be a complete finite-volume hyperbolic 4-manifold with cusps, or a complex-hyperbolic surface with cusps. Truncate along cusp cross-sections N, which are compact flat or infranil 3-manifolds respectively. Then:
- (a) the double D(H) = H_T ∪_N H̄_T satisfies α(D(H)) = 0;
- (b) for a real-hyperbolic cusp with N = T³ and any primitive slope γ ∈ H₁(T³), the Dehn filling H_T ∪ (D² × T²) (with γ bounding) satisfies α = 0.

*Proof.*

(a) Real case. The cusp metric is dt² + e⁻²ᵗ g_N with g_N flat. On N × [T, T+2] use dt² + e^{−2f(t)} g_N, where f(t) = t for t ≤ T and f(t) = 2T + 2 − t for t ≥ T + 2, with |f'| ≤ 1 and |f''| ≤ C. The sectional curvatures of the warped product are −(f'² − f'') and −f'², which are bounded. The volume is O(e⁻³ᵀ) and |Ric°| ≤ C. Elsewhere the metric is hyperbolic, so P = O(e⁻³ᵀ).

(a) Complex case. The cusp metric is dt² + e⁻²ᵗ g_base + e⁻⁴ᵗ θ² on a Heisenberg nilmanifold. Use the same f, with base factor e^{−2f} and fibre factor e^{−4f}. The ratio fibre/base² stays 1, so the Nil curvature stays bounded. The volume is O(e⁻⁴ᵀ).

(b) Write T³ = S¹_γ × T² with a flat product metric. A path of flat metrics on T³ costs bounded curvature and O(e⁻³ᵀ) volume. Then use dt² + a(t)²dθ² + e⁻²ᵀ g_{T²}, in four stages:
1. a shrinks like the cusp;
2. a turns around (bounded a''/a);
3. a grows like e^{t − 2T} up to size 1; this stage is H² × (tiny T²), with bounded curvature;
4. a caps off as a round disc of size 1.
The total volume is O(e⁻²ᵀ) and the curvature is bounded. So P = O(e⁻²ᵀ) → 0. ∎

Remarks.
- χ(D(H)) = 2χ(H) > 0. The simplicial volume is ‖D(H)‖ = 2Vol(H)/v₄ > 0 (amenable boundary), so MinVol(D(H)) > 0. Thus (ii) cannot apply, and (i) would need a compact Einstein orbifold associated to D(H); no such orbifold is known.
- The Einstein region is a cusped complete Einstein manifold, and the complement collapses along an F-structure: exactly Anderson's case-(III) geometry.
- Whether D(H) or the small-slope fillings carry Einstein metrics is open in general. For large slopes, Einstein Dehn-filling theorems in the literature are expected to apply, but they are not used and not cited here. Gromov's simplicial-volume inequality and Hitchin–Thorpe do not obstruct them, since τ = 0.
- So this is a third, independent zero-gap mechanism with attainment open. It is constructed with no Ricci-flat ALE pieces and no orbifold.

### B.2 The converse (conditional only on Anderson's theorem)

**Theorem 59.Z (structure of the zero-gap set).** Let M be closed and oriented. Assume Anderson's Theorem 4.10 for ℛ² = 32π²χ + 4P (Knowledge: *Canonical metrics on 3-manifolds and 4-manifolds*, Thm 1.1/4.10). If α(M) = 0, then M carries one of the following three configurations:
- (I) a compact Einstein orbifold (V, g₀) associated to M, i.e. V is obtained from M by collapsing cycles (and possibly reducible);
- (III) a nonempty maximal Einstein orbifold domain (Ω, g₀) with 0 < vol ≤ 1. It is complete with finite volume, weakly embedded in M, and has s < 0. Outside a compact set, M carries an F-structure along which the sequence collapses with locally bounded curvature, off finitely many shrinking balls;
- (II) collapse everywhere with locally bounded curvature along F-structures, off finitely many shrinking balls.

Conversely:
- every (I)-configuration whose singular points admit Ricci-flat ALE resolutions or smoothings realizing M gives α(M) = 0 (Prop. 59.N);
- MinVol(M) = 0 gives α(M) = 0 (Prop. 59.C), which is a special (II);
- the doubles and Dehn fillings of 59.D realize (III).

In every case, α(M) is attained iff M carries an Einstein metric.

*Proof of the forward direction.* Anderson's minimizers g_ε of Z_ε = P + ε∫(1+|Ric|²)^p satisfy P(g_ε) → α = 0. On the regular part they converge smoothly on compact sets in cases (I) and (III). Lower semicontinuity on compact sets gives ∫_K|Ric°(g₀)|² ≤ liminf P(g_ε) = 0 for every compact K in the regular set. So g₀ is Einstein.

In (III), Ω cannot be Ricci-flat: complete noncompact Ricci-flat manifolds have at least linear volume growth, so they cannot have finite volume. If the scalar curvature were positive, Ω would be compact by Myers. So s < 0. ∎

Notes.
1. Anderson's inequality F(g₀) ≤ inf F is for ℛ² and carries a χ_orb shift, so it is not used. Only the smooth convergence of the regular part is used.
2. The bubble structure in (I) (Ricci-flat ALE bubble trees with P = 0, and M diffeomorphic to the resolution) needs the no-neck and topology ledger H_sm of Step 58. With it, (I) is exactly "M is a Ricci-flat-ALE-tree resolution of an Einstein orbifold".

### B.3 Consequences for X # kCP̄²

Let M = X # kCP̄² with X minimal of general type and k ≥ 1.
- χ > 0, so MinVol > 0. Prop. 59.C never applies.
- Kähler orbifolds in (I) are excluded: their smoothings or resolutions are minimal, which leads to 56.B and 55.6.
- So α(M) = 0 would need one of: a non-Kähler Einstein orbifold associated to M (Wahl/T points, or more generally points with Ricci-flat ALE fillings); a type-(III) cusp domain whose F-structure complement carries the exceptional classes; or type-(II) collapse whose bad balls carry all of χ.

Corollary 59.KE says only that α(M) < 8π²k. The gap between 0 and this bound is exactly the unresolved O11 problem: the open-range inequality C₊ ≥ A and the k²/A law.

The common principle behind the three mechanisms: P vanishes in the limit iff M is exhausted by Einstein regions, up to transition regions whose volume vanishes in the natural curvature scale. The three ways such a transition can disappear give the trichotomy:
- shrinking scale: Ricci-flat ALE necks;
- collapsing fibres along part of M: cusps;
- collapsing fibres along all of M: F-structures.

---

## Part C (Step 60). Corrections and independent confirmations now in force

**C.1 W⁻ sector, independently confirmed; a representation artifact in the exact script.**
- The exact script `step59_exact_log_coefficient.py` returns a pair-basis 6×6 matrix X for the linearised W⁺ operator. In sectors with X₀ = 0 (pure W⁻ or pure Ric° jets), its σ¹ part X₁ contains a spurious antisymmetric piece N. N does not depend on K.
- The script's signed density 4 tr X₁² + s₁²/12 is therefore wrong in those sectors by −4|N|². A true |W⁺|² must be ≥ 0, so a negative value cannot be correct.
- `step60_jax_check.py` makes an independent JAX evaluation with orthonormal-frame W⁺ (Cholesky frame) of the σ²t² coefficient of F₊(δ + σA + t(h₂ + σK)) at a rational point. It gives:
  - Wm, K = 0: JAX 13.2439633 = sym-only 13.2439633; the script's signed value is 13.131.
  - Wm, K = k₀^W: JAX −5·10⁻¹⁶; sym-only exactly 0; the script's signed value is −0.113.
  - Rz, K = 0: JAX 0.95193 = sym-only.
  - Rz, K = k₀^W: JAX 0.27206 = sym-only.
- So the true coefficient is 4|sym X₁|² + s₁²/12.
- A01's k₀^W = (3/2)sym(h_W k_B) − (1/4)tr(h_W k_B)δ kills the W⁻ chiral residual pointwise (sym X₁ = 0 and s₁ = 0 exactly in rational arithmetic). This independently confirms A01's Theorem 2.1. It also shows that k₀^W does not solve the Ric°_ζ residual.
- The (s, W⁺) sector, where X₀ ≠ 0, is unaffected. `step60_jax_check_Wplus.py` matches script and JAX to 15 digits, for K = 0 and for a generic invariant K. So the exact Φ of §A.3 stands.
- Corrector searches now use `step60_corrector_columns.py`, which solves sym X₁ = 0 and s₁ = 0 exactly. The older `step59_exact_wminus_ric_correctors.py` is superseded.

**C.2 Sign scope of Φ (A01 #833).**
- Φ ≤ 0 is a statement on the kernel μ₁ = 0 only. In the interior R⁺ < 0 the logarithmic coefficient can be positive: W⁺ = 0 gives Φ = s²/288 > 0, and −μ₁(μ₁ − s/8) > 0 for s/8 < μ₁ < 0. There it is subordinate to the positive first-order cost.
- So "Φ ≤ 0 on the whole cone" is withdrawn wherever it appeared. The strictly negative cone, e.g. real hyperbolic, is a genuine survivor, not a remainder.
- Theorem 59.R/§A.3 assumes ζ is an eigenvector of R⁺ (w₁₂ = w₁₃ = 0). If μ_ζ = R⁺(ζ,ζ) = 0 but R⁺ζ ≠ 0, the mixed block makes the degree-0 log coefficient unbounded below (A01: null corrector direction L_{(log r)J₂x}δ). That case has R⁺ indefinite, which already gives a first-order saving.
- On R⁺ ≤ 0 a kernel vector is automatically an eigenvector, so 59.Rig is unaffected.

**C.3 Independent remainder (A01 Theorem 52.A).**
- A01 proves, for Einstein backgrounds with arbitrary W⁻ and uniformly in (p, ζ):
  P(g_ε) = P(g) + 8π² − 4π²|T|²ε²log(1/ε) + O(ε²).
- Their order-ε flux computation, with f − |Ric°|²dV = 8π²p₁(Λ⁺), gives the order-ε term −8π²εR⁺(ζ,ζ) exactly.
- This agrees with our normalisation 2κ = −8π² in 59.R, now obtained independently, without calibration by Ch. 5 or Theorem F.
- Our 59.R covers the larger class of P-critical backgrounds (E_P = 0 near p).
- A01's Lemma 52.C (no open degenerate stratum (a, −a/2, −a/2) when s < 0) uses δW⁺ = 0, so it needs an Einstein bulk.
- The Anderson case-(I) bulk of 53.B is only P-critical. Lemma 52.C must therefore be replaced there, or the bulk shown to be Einstein (e.g. by the Bach-flat route of Step 54).

**C.4 Prop. 59.D: literature position, which changes how it is stated (sources requested this Step; citation keys pending).**
- Anderson (Dehn filling and Einstein metrics in higher dimensions) and Bamler (generalized Dehn filling) construct, for all but finitely many slopes per T³ cusp, Einstein metrics of negative scalar curvature on the fillings. These are GH-close to the cusped hyperbolic metric.
- For such long slopes our α = 0 is therefore attained. This confirms 59.Z: the Einstein metric is an unconditional instance, and our collapsing sequence converges to the regime-(III) configuration, while the Einstein metrics themselves are a regime-(I) family converging to it.
- The finitely many short slopes form a finite test family. There α = 0 holds by our interpolation, and 59.Z makes attainment equivalent to Einstein existence, which no filling theorem decides.
- The doubles D(H) along T³ (or flat, or Nil) necks are the cleaner new examples. A warped Einstein neck dt² + φ(t)²g_flat requires φφ'' = φ'², i.e. φ = e^{ct}, a cusp. So no Einstein T³ × I neck exists, and no filling theorem applies. To our knowledge Einstein existence on D(H) is open.
- Existence of hyperbolic 4-manifolds with T³ cusp sections is to be cited from the requested sources before use.

## Part D (Step 61). Verification of Parts A–C (TTCS s60_t24_tool1). These corrections are binding and override A–C.

Sources: `trace/ttcs/results/step60_ttcs01_verifier1_integration.md` (Part A) and `step60_ttcs01_verifier2_integration.md` (Part B, C.4).

**D.1 Theorem 59.R survives, with these repairs.**
- The insertion support B_{2ρ}(p) must lie entirely inside the region where E_P(g) = 0. Without that, an extra bulk first-variation term remains.
- Rescaling. Write h(ry) = r²q(r,y) with q smooth on the shell (Taylor with integral remainder). The rescaled family is G_{σ,r} = B_σ + r²(q(r,y) + σK). It agrees with the cut-off metric only up to two-jets on |y| = 1 for 2R√ε ≤ r ≤ ρ, which is all the density needs.
- Why 3-jets and 4-jets cannot enter the log term: 𝒞(B_σ) = 0 and F₊ = |𝒞|², so 𝒞(G) = r²C₂ + r³C₃ + …. The r⁴ coefficient is |C₂|² alone. The third jet first appears at r⁵, the fourth jet and nonlinear terms at r⁶, and these give a finite ∫dr/r. No parity assumption on K is needed.
- The inner region contributes O_R(ε²). The phrase "O(ε²R⁴)" is withdrawn, since no uniformity in R is needed or proved.
- Order ε: a factor-two error in the distributional flux is corrected. With M_ζ = 3ζ⊗ζ − I and 𝒞 = (2W⁺, s/√12), c_A = m(M_ζ/6, 1/√12), not M_ζ/12. Also s'(∂∂̄φ) = −¼Δ²φ and ∫Δ²(χ log r²) = 16π², so m = −4π² and E₁ = −8π²R⁺(ζ,ζ). Hence κ = −4π², matching Step 20 and A01's θ₂ = 8π²μ_ζ independently. The displayed final formula of 59.R was already right; only the intermediate c_A changes.
- Corrected statement. Under the hypotheses above, for every unit ζ and every fixed degree-0 K, with **no eigenvector hypothesis**:
  P(g̃_ε) = P(g) + 8π² − 8π²εR⁺_p(ζ,ζ) + 4π²Φ(Rm_p,ζ,K)ε²log(1/ε) + O(ε²).
  The explicit optimised value Φ_opt = −μ₁(μ₁ − s/8) − |T|² needs two further assumptions: Ric°_p = 0, and ζ an eigenvector of R⁺_p. It is attained by K* + k₀^W. Here T is the trace-free part of R⁺ restricted to ζ^⊥.

**D.2 Corrected optimal corrector.** With u⊙v = ½(u⊗v + v⊗u), as in the script, the mixed coefficient in K* is 2w₂₃/3:
K* = (s/24)dr² + (−s/48 + 7w₁₁/6 + w₂₂/3)s₁² + (2w₂₃/3)s₁⊙s₂ + (−s/48 + 5w₁₁/6 − w₂₂/3)s₂².
The printed 4w₂₃/3 is withdrawn. The KE⊥ specialisation, where w₂₃ = 0, is unchanged.

**D.3 The W⁻ artifact, explained.** The old script used the frozen projector P₊ at t = 0. The true derivative includes a projector-variation term
½(H'₊₋R₋₊ − R₊₋H'₋₊),
which is skew-adjoint and cancels exactly the skew part of X. At order σ this defect depends on h₂ but not on K. Hence the geometric coefficient is 4|sym X₁|² + s₁²/12.
- The defect vanishes on the eigenvector locus, so the exact (s,W⁺) computation at w₁₂ = w₁₃ = 0 is unaffected.
- C.1's unrestricted sentence is replaced by: "the exact (s,W⁺) coefficient of §A.3, restricted to w₁₂ = w₁₃ = 0, is unaffected; the JAX check tests this locus only."
- The `leak_solvable` flag in `step59_exact_log_coefficient.json` records only that `sympy.solve` returned a dictionary. It says nothing about the mixed block. A01's Hessian-null direction is the authoritative statement there.
- Schur cancellation of the W⁻ cross terms is proved for the **whole** integrated σ² coefficient. The polarised invariant linear functional on the spin-2 representation vanishes, and this covers the metric-dependent norm and volume terms as well.

**D.4 Sign scope (replaces C.2 and C.3 openings).** Theorem 59.R holds for every unit ζ and fixed K. The optimised formula assumes ζ is an eigenvector. On R⁺ ≤ 0, a zero Rayleigh direction is automatically a kernel eigenvector.
- On the kernel, Φ_opt = −|T|² ≤ 0. This holds for the optimised coefficient with the W⁻ sector cancelled. It is not a statement about arbitrary K, nor about general P-critical jets whose Ric° residual is uncancelled.
- 59.Rig in the Ric° sector must be stated quantitatively: the strict conclusion holds when |T|² > Q_Ric(Ric°_p) for an explicit Ricci residual, sufficiently when |T|² > C|Ric°_p|².
- C.3 opening: "For Einstein backgrounds, unit directions with R⁺ζ = 0, and arbitrary W⁻, A01 proves the expansion uniformly on compact families of insertion data."

**D.5 Corollary 59.KE: order of limits.** Choose the insertion balls in the regular locus, inside fixed neighbourhoods where g_λ = g_KE. Then the insertion difference I(ε) is independent of λ, not merely uniform in it. Fix ε first so that the logarithmic saving dominates the remainder, then choose λ so that P(g_λ) is smaller than that saving. This produces an actual smooth competitor below 8π²k. It is an upper bound only. The comparison with K∞ uses Step 51/52.

**D.6 Prop. 59.N (corrected).**
- The annulus estimate is P_ann ≤ C(t⁴ + (λ/t)^{2τ}) for derivative-controlled ALE order τ > 0.
- Order τ ≥ 2 gives O(λ²) with t = √λ. Any τ > 0 gives zero gap with t = λ^{τ/(τ+2)}.
- Order-4 decay gives a metric error λ⁴r⁻⁴, not λ⁶r⁻⁴.
- Trees: perform each insertion at its parent's native scale.
- Compatible orientation means a cone-end identification through an orthogonal conjugacy, with induced boundary orientations reversed.
- Statement: a smooth closed manifold obtained from a compact Einstein orbifold with isolated irreducible cone points by compatible finite Ricci-flat ALE-tree replacements has α = 0. Reducible vertices are not covered.
- For canonical models, "attained iff K ample" is withdrawn. Only "attained iff the smooth manifold admits an Einstein metric" is kept.
- (Step 61 sharpens the rate for EH points to Θ(a⁴); see `step61_EH_quantitative_obstruction.md`.)

**D.7 Prop. 59.C (corrected).**
- Under the spectral bound −3g ≤ Ric ≤ 3g one has |Ric°|² ≤ 36 (equality at eigenvalues (3,3,−3,−3)). Hence α ≤ 36 Vol_{|r|} ≤ 36 MinVol. The proof's "|Ric| ≤ 3" mixed two norms and is replaced.
- MinVol = 0 ⇒ χ = τ = 0 (Chern–Weil).
- For F-structures, use a polarised positive-rank F-structure or an explicit bounded-curvature collapsing sequence.
- Nonattainment needs only χ = 0, since Einstein with χ = 0 is flat. The examples S¹×Y (Y hyperbolic or spherical), S²×T² and primary/secondary Kodaira surfaces are confirmed: none is flat.

**D.8 Prop. 59.D (corrected and completed).**
- Real-hyperbolic doubles: |Ric°|² = 3(f'')² exactly for dt² + e^{−2f}g_flat, so P_neck = 3Vol(N)∫(f'')²e^{−3f} = O(e^{−3T}).
- Complex-hyperbolic Heisenberg doubles: the full coframe calculation (dω³ = −2f'ω⁰³ + κω¹²) shows that all curvature coefficients are polynomials in f'', f', κ. This gives a full curvature bound, P = O(e^{−4T}).
- T³ fillings: every primitive slope works. Two steps are added: a flat-metric transition G(s) to a product adapted to γ, and the turnaround/growth/round-cap sequence. Together they give P ≤ C_γ e^{−2T}.
- C.4 corrections:
  - "finitely many short slopes" is finite only per cusp, not for slope tuples;
  - "no Einstein T³×I neck exists" is false (exponential segments exist); the correct statement is that there is no **turning** isotropic warped Einstein neck;
  - the openness of Einstein existence on doubles is not source-supported and is withdrawn as a claim;
  - the simplicial-volume formula is real-hyperbolic only.
- Source keys: Anderson \cite{anderson2003dehn} (ODE gluing, "sufficiently large fillings", Ric = −(n−1)g, smooth convergence to the cusp manifold); Bamler \cite{bamler2009construction} (metadata only); Kolpakov–Martelli \cite{kolpakov2013hyperbolic} (one-cusped hyperbolic 4-manifolds with T³ cusp).

**D.9 Theorem 59.Z (corrected statement).** Assume Anderson Thm 4.10 together with Einstein removable-singularity regularity. If α(M) = 0, there **exists a selected minimizing sequence** exhibiting one of three configurations:
1. a compact, possibly reducible, Einstein orbifold V of volume 1;
2. a nonempty maximal orbifold domain Ω, Einstein and complete componentwise (completeness follows from the Einstein lower Ricci bound via Anderson Rem. 4.12), with s < 0 on every **noncompact** component and F-collapse outside compact sets;
3. total collapse.
Further points:
- Thm 4.10 itself has only cases (I) and (II); the three labels are those of Thm 1.1.
- The alternatives belong to selected sequences and are not mutually exclusive properties of M. The long-slope fillings show both (1) and (2) on one M.
- Zero-P bubbles are Ricci-flat only under bubble-scale convergence.
- The ALE-tree reconstruction must cite Anderson's discussion around (4.65). Lower semicontinuity and H_sm do not supply it.
- Attainment ⇔ M admits an Einstein metric. This is immediate from P = 0 ⇔ Ric° = 0.
- The "common principle" is a **sufficient construction principle**, with Anderson supplying a selected reverse decomposition. It is not a classification of every zero-gap sequence.

## Files

- `workspace/scripts/step59_exact_log_coefficient.py` → `data/step59_exact_log_coefficient.json`: exact (s, W⁺) sector, quadratic form, optimal K.
- `workspace/scripts/step59_exact_wminus_ric_correctors.py` → `data/step59_exact_correctors_{Wm,Rz,Rp}.json`.
