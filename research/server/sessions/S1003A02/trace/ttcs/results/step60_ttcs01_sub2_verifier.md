# TTCS Independent Branch Record

```json
{
  "step_id": 60,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step59_rigorous_burns_expansion_and_zero_gap_structure.md",
    "Sessions/S1003A02/workspace/scripts/step59_exact_log_coefficient.py",
    "Sessions/S1003A02/workspace/data/step59_exact_log_coefficient.json",
    "Sessions/S1003A02/workspace/scripts/step60_jax_check.py",
    "Sessions/S1003A02/workspace/scripts/step60_jax_check_Wplus.py",
    "Sessions/S1003A01/workspace/notes/step52_kernel_insertion_theorem.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md"
  ]
}
```

## Task

Verify Part A of the Step-59 note (Theorem 59.R, the rigorous second-order Burns expansion, and Corollary 59.KE, p_*(X#k CPbar^2) < 8 pi^2 k for every minimal surface of general type), as corrected by Part C. Check specifically and give corrected statements where needed: (1) smoothness in (sigma, r, y) of the rescaled far-annulus metric G_{sigma,r} and of the density difference, the claimed factorization r^4 * gamma~(sigma,r) with gamma~(0,r)=0, and the Taylor/log bookkeeping that yields 4 pi^2 Phi eps^2 log(1/eps) + O(eps^2) including the cutoff psi_eps for K and the inner region O(eps^2 R^4); whether 'F+ quadratic in the perturbation of a C-null model' really excludes 3-jets/4-jets from the log term. (2) The distributional evaluation of the order-eps term E_1 = 2 kappa R+(zeta,zeta): validity of reducing to lim_{eta->0} int ell_g(chi_eta B) using only E_P=0 near p (P-critical, not Einstein), the replacement chi A -> ddbar(chi log r^2), the linearized Kahler identity W+' = (s'/12) diag(2,-1,-1), the Green flux, and the sign/normalization 2 kappa = -8 pi^2 (compare A01's independent flux theta_2 = 8 pi^2 mu_zeta in Sessions/S1003A01/workspace/notes/step52_kernel_insertion_theorem.md). (3) The Schur argument that W- cross terms with the SU(2)_- invariant block vanish after S^3 integration, and the W- self-term killed by k0^W (Part C.1 reports an exact pointwise check and a representation artifact in the exact script; judge the artifact explanation using step60_jax_check.py and step60_jax_check_Wplus.py). (4) The order of limits for canonical models with ADE points (Kronheimer gluing at scale lambda, then lambda -> 0 at fixed eps), whether the error constants in 59.R are uniform in lambda given g_lambda = g_KE near the p_i, and whether the conclusion 'strict inequality for every minimal surface of general type' is correctly obtained (note p_* is an infimum so a sequence suffices). (5) Whether the eigenvector hypothesis on zeta and the kernel/interior sign scope (Part C.2) are stated correctly everywhere in Parts A-C. Return a direct scientific memo: what is proved, what must be repaired, and exact corrected wording.

## Output

# Verification memo: Step 59, Part A (Theorem 59.R, §A.3, Corollary 59.KE) as corrected by Part C

## Summary

- **Theorem 59.R is correct.** One hypothesis needs sharpening: E_P(g) = 0 must hold on the whole support B_{2ρ}(p) of the insertion.
- **The constant κ can be computed directly, and should be.** The written formula for c_A has a factor-2 slip. The direct computation gives κ = −4π², so 2κ = −8π² with no calibration. This agrees with Step 20 and with A01's θ₂.
- **The far-annulus bookkeeping and the log coefficient are correct.** The reason the 3-jets and 4-jets drop out is slightly different from the stated one; see §1.4.
- **The Schur argument for the W⁻ cross terms is correct.**
- **The script artifact of Part C.1 has a structural explanation.** The correction term it omits is a skew commutator. This explains the C.1 numbers. It also shows the (s,W⁺) script values are exact precisely on the eigenvector locus, which is why A.3 stands.
- **The order of limits in Corollary 59.KE is valid.** The strict inequality for every minimal surface of general type follows.
- **Several statements need corrected wording:**
  - the eigenvector hypothesis is placed on Theorem 59.R itself instead of on §A.3;
  - Remark 2 is too broad;
  - the s₁s₂ coefficient of K* is off by a factor 2;
  - the `leak_solvable` flag in the JSON is in tension with C.2.

---

## 1. Far annulus, inner region, and the ε² log(1/ε) coefficient

### 1.1 The rescaled metric

Use x = ry and three facts:
- A is homogeneous of degree −2 in components;
- K is homogeneous of degree 0;
- h(x) = Σ_{m≥2} h_m(x) in normal coordinates.

Pulling back gives

r⁻²Φ_r*g̃ = δ + σA(y) + r⁻²h(ry) + σr²K(y), with r⁻²h(ry) = h₂(y) r² + h₃(y) r³ + ….

So G_{σ,r} − (δ + σA) = r²(h₂ + σK) + r³h₃ + …. This is smooth in (σ, r, y) on [0, (4R²)⁻¹] × [0, ρ] × U by Hadamard's lemma in r, and in fact for r ∈ (−ρ, ρ). It is positive definite for ρ small, since δ + σA ≥ δ and the remaining terms are O(ρ²) + O(ε).

**Precision needed.** G_{σ,r} on the whole shell U = {½ ≤ |y| ≤ 2} is not the rescaled g̃ near the two ends of D_f:
- ψ_ε ≠ 1 for |x| < 2R√ε;
- χ_ρ ≠ 1 for |x| > ρ.

What the proof needs is narrower. The sphere density f(r) at radius r depends only on the 2-jet of g̃ along |x| = r. For r ∈ [2R√ε, ρ], ψ_ε ≡ 1 and χ_ρ ≡ 1 on {|x| ≥ 2R√ε} ∩ {|x| ≤ ρ}, and both cutoffs are constant there to infinite order. So on D_f the metric is exactly g + ε(A + K), and its jets on |y| = 1 agree with those of G_{σ,r}.

### 1.2 The factorization

- Since 𝒞(δ + σA) ≡ 0 and the perturbation is r²·(smooth), we get 𝒞(G) = r²𝒞₂(σ, y) + r³𝒞₃ + …. Hence F₊(G)dμ_G = r⁴·(smooth).
- The background density r⁻⁴F₊(δ + r⁻²h(ry))dμ is σ-independent.
- So the difference is r⁴γ̃(σ, r), with γ̃ smooth and γ̃(0, r) ≡ 0. ✓

### 1.3 Integration in r

With f = r³γ̃ and σ = ε/r²:

∫_{D_f} f dr = ε∫rγ₁ dr + ε²∫γ₂ dr/r + ε³∫γ₃ r⁻³ dr.

- The third term is ≤ Cε³(8R²ε)⁻¹ = O(ε²/R²).
- The second term is γ₂(0)·(½log(1/ε) + log(ρ/2R))ε² + O(ε²ρ).
- The first term is ε∫₀^ρ rγ₁ dr − O(ε²R²). This is the far-region part of εE₁.

Identification of γ₂(0): r⁻⁴F₊(G)dμ_G → |𝒞₂(σ)|²_{δ+σA}dμ_{δ+σA}, with 𝒞₂(σ) = D𝒞_{δ+σA}[h₂ + σK]. The background contributes nothing at σ². Hence γ₂(0) = 8π²Φ. Then ½γ₂(0)ε²log(1/ε) = 4π²Φε²log(1/ε) ✓, and P/8π² acquires (Φ/2)ε²log(1/ε) ✓.

### 1.4 Why the 3-jets and 4-jets do not enter

The correct mechanism is not "F₊ is quadratic" alone. It is:

- the model is 𝒞-null, so |𝒞|² starts at r⁴|𝒞₂|²;
- h₃ enters only through 2r⁵⟨𝒞₂, 𝒞₃⟩;
- h₄ and the second-order term D²𝒞[h₂, h₂] enter only at r⁶.

These make γ₂(r) − γ₂(0) = O(r), and ∫O(r)dr/r converges at r = 0. So they change only the O(ε²) term. A nonzero 3-jet would matter only if 𝒞 had an r¹ term, and it has none, because G − (δ + σA) = O(r²).

**Suggested wording.** "The ε²log coefficient equals the r⁰-value of r⁻⁴·(σ²-density), which sees only the r²-coefficient 𝒞₂ = D𝒞_{δ+σA}[h₂ + σK]. Higher jets enter |𝒞|² at order r⁵ or higher, which is integrable against dr/r."

### 1.5 Inner region

In u = x/√ε:
- ε⁻¹g̃ = g_{B,1} + ε(|u|²h̄ + ψ(|u|/R)K(u));
- the K part vanishes for |u| ≤ R;
- the h part is the pullback of a smooth tensor that vanishes at 0, so it is smooth on Bl₀C².

On the compact set {|u| ≤ 2R}, the perturbation is O(ε) in C^k(g_{B,1}), with constants polynomial in R. Hence 𝒞 = O(ε) in the rescaled picture, and the inner contribution is O(ε²R⁴) ✓.

The linear contribution missing on r < 2R√ε is ε∫₀^{2R√ε}ℓ_g(B) = O(ε²R²), using ℓ_g(B) = O(r⁻²) (§2). It is absorbed correctly.

---

## 2. The order-ε term E₁

### 2.1 Reduction to lim_{η→0}∫ℓ_g(χ_η B)

- The topological densities have exact first variations. So ℓ_g(φ) = ⟨E_P(g), φ⟩dμ + d(·) for compactly supported φ.
- φ = (1 − χ_η)B is smooth and supported in {η ≤ r ≤ 2ρ}.
- Therefore ∫ℓ_g((1 − χ_η)B) = ∫⟨E_P, (1 − χ_η)B⟩. This vanishes only if E_P = 0 on B_{2ρ}(p).

**Required wording.** "Choose ρ so that E_P(g) = 0 on B_{2ρ}(p)." Only the integrated Euler–Lagrange equation is used, not pointwise vanishing of D(|Ric°|²dV). So the P-critical class is genuinely covered. This is a real gain over A01 §3.3, which needs Einstein.

### 2.2 Error terms

Normal coordinates give g − δ = O(r²) and ∂g = O(r). Hence D𝒞_g − L₀ = O(r²)∂² + O(r)∂ + O(1), and 𝒞_g − 𝒞(p) = O(r).

- The note writes O(r)∂²B. That is correct after combining with ⟨𝒞_g − 𝒞(p), L₀B⟩.
- Applied to χ_ηA (with ∂^jA ~ r^{−2−j}), the errors are O(η).
- The K part: L₀(χ_ηK) ~ r⁻², contributing O(η²). In fact it contributes exactly 0, since L₀ is a double divergence and the flux of ∂K ~ r⁻¹ through small spheres vanishes.
- ℓ_g(B) = O(r⁻²) is absolutely integrable ✓.
- c_A = ∫L₀(χ_ηA) is η-independent by homogeneity, and is supported in the annulus ✓.

### 2.3 Replacement χA → ∂∂̄(χ log r²)

The difference is (∂χ terms + log r²·∂∂̄χ). It is smooth and compactly supported away from 0, and ∫L₀(compactly supported) = 0 ✓.

### 2.4 Linearized Kähler identity

Along the J_ζ-Kähler family δ + t∂∂̄ψ, one has W⁺_t = (s_t/12)M_{ζ_t} with M = diag(2, −1, −1). Since s₀ = 0 and W⁺₀ = 0, the derivative is frame-independent: W⁺′ = (s′/12)M_ζ ✓. This holds pointwise on r > 0 for ψ = χ log r².

**Factor slip.** With 𝒞 = (2W⁺, s/√12):

L₀(∂∂̄ψ) = s′·(M_ζ/6, 1/√12),

not (M_ζ/12, 1/√12). With M/6:

2⟨𝒞(p), c_A⟩ = 2m[(1/3)⟨W⁺_p, M_ζ⟩ + s/12] = 2m[W⁺_p(ζ,ζ) + s/12] = 2mR⁺_p(ζ,ζ),

using ⟨W⁺, M⟩ = 3W⁺(ζ,ζ). With the written M/12 one would get W⁺(ζ,ζ)/2 + s/12. So the stated conclusion is right and the displayed c_A is wrong.

### 2.5 Direct value of m (the calibration is unnecessary)

Take h = ∂∂̄φ = (Hess φ + JᵀHess φ J)/4. Then:
- tr h = Δφ/2;
- ∂_i∂_j h_ij = Δ²φ/4, because the J-term gives Σ J_ki J_lj ∂⁴_{klij}φ = 0 by antisymmetry of J;
- so s′ = ∂_i∂_j h_ij − Δ tr h = −Δ²φ/4.

Next, Δ log r² = 4/r² and Δ(r⁻²) = −4π²δ₀ in R⁴. So Δ²log r² = −16π²δ₀, and hence ∫_{r>0}Δ²(χ log r²) = +16π².

Therefore m = −4π², κ = −4π², and E₁ = −8π²R⁺_p(ζ,ζ).

Cross-checks:
- Step 20's scalar flux F_s = −∫s^lin(χh) = 4π² is the same number. Step 20's h equals A.
- A01's θ₂ = 8π²μ_ζ gives the order-ε term −εθ₂.
- The parameters match: x₀ = ε, with area πε.

---

## 3. W⁻ sector: Schur argument and the script artifact

### 3.1 Schur argument

SU(2)₋ acts trivially on Λ⁺, isometrically on (R⁴, δ), and fixes J_ζ, A, the (s,W⁺)-jet h₂^inv and K*.

- The map W⁻ ↦ (h_W, k₀^W) is SU(2)₋-equivariant, because k₀^W = (3/2)sym(h_W A) − ¼tr(h_W A)δ with A invariant.
- So the integrated bilinear cross term B(v_inv, v_W(W⁻)) is an invariant linear functional on S²₀Λ⁻ ≅ spin 2. It therefore vanishes ✓. This includes the ⟨X₀^inv, X₂^W⟩ pieces.
- The same argument kills the Ric°–inv cross terms (Ric° is spin 1 under SU(2)₋).
- It also kills the Ric°–W⁻ cross terms, since 1 ⊗ 2 contains no trivial summand.

Consequence for a general P-critical jet with ζ an eigenvector:

Φ = −μ_ζ(μ_ζ − s/8) − |T|² + min_K Q_Ric(Ric°_p), with Q_Ric ≥ 0.

### 3.2 The artifact has a structural cause

The script forms X = P₊R′P₊ − (s′/12)P₊ with P₊ frozen at t = 0, in the coordinate pair basis. The true derivative is

W′ = X + P₊′R₀P₊ + P₊R₀P₊′ (using s₀ = 0).

At leading order in the pair basis, P₊′ = ½[P₊, G′] with G′ the Λ²-action of h₂ + σK. Use two facts:
- P₊R₀P₊ = 0 for Burns;
- Burns is Kähler, so R₀ kills Λ^{2,0}, which gives P₋R₀P₊ = |ρ₀⟩⟨ζ̂|.

Then the ++ block of the correction is

E = ½(Z − Zᵀ), Z = P₊G′P₋R₀P₊.

So E is skew. Since W′ is self-adjoint, W′ = sym X and tr X² = |W′|² − |E|².

At order σ¹, R₀ = O(σ). So E₁ involves only h₂ and is K-independent. This is exactly the C.1 pattern:
- the deficit 13.2440 − 13.131 ≈ 0.113;
- the same −0.113 with K = k₀^W.

The C.1 explanation is therefore correct in every sector, not just the sectors with X₀ = 0.

### 3.3 Consequence for the (s,W⁺) sector

At x₀ the following hold:
- ρ₀ ∝ dr∧s₃ − s₁∧s₂ is the U(2)-invariant ASD form;
- under the e₀-identification Λ⁻ ≅ Λ⁺ it maps to ζ;
- by SO(3)_{e₀}-equivariance, P₊h₂°P₋ = αI + βR⁺₀.

Hence Z ∝ |αζ + βR⁺₀ζ⟩⟨ζ|, and E₁ ∝ (R⁺ζ)^⊥ ∧ ζ. So E₁ = 0 exactly when ζ is an eigenvector of R⁺ (w₁₂ = w₁₃ = 0).

This predicts the 15-digit agreement in `step60_jax_check_Wplus.py`, whose test W⁺ = [[2,0,0],[0,−3,1],[0,1,1]] has w₁₂ = w₁₃ = 0. It also shows that the §A.3 formula, derived on that locus, is exact. Off the locus, the script's `c2l` carries a K-independent error of about −c(w₁₂² + w₁₃²).

The step "α, β via SO(3)_{e₀}-equivariance; ρ₀ ↦ ζ under the e₀-identification" should be written out. It is a short exact computation.

### 3.4 Completing the W⁻ self-term

- Y = sym X₁ (with s₁) is linear in W⁻ once K = k₀^W(W⁻).
- By equivariance, the S³-integrated self-term vanishes iff Y(x₀) = 0 for the five basis jets of S²₀Λ⁻.
- A single generic point and a single W⁻ (the JAX value −5·10⁻¹⁶) is one sample, not a proof. The five-jet check at x₀ in exact arithmetic is.
- A01's Step-50 symbolic identity may already cover this, but its formula should be confirmed to be the symmetric (true) part.

### 3.5 Corrector coefficient and the `leak_solvable` flag

- **K\* coefficient.** In the script's convention K = Σ k_ij sym(f_i⊗f_j), the coefficient of the monomial s₁s₂ is k₅ = 2w₂₃/3, not 4w₂₃/3. The KE⊥ corrector K* = s(dr²/24 − s₁²/16 − 7s₂²/48) is correct.
- **The `leak_solvable: true` flag.** It sits uneasily with A01's statement that the mixed block makes the log coefficient unbounded below. On the eigenvector locus the dr·s_i directions (k₁, k₂, k₃) are absent from c₂, i.e. they are Hessian-null. Unboundedness requires a linear coupling of these to (w₁₂, w₁₃); in that case the gradient system is inconsistent. Printing the k₁–k₃ coefficients of `c2l` settles which reading is correct, independently of the skew error, which is K-independent.

---

## 4. Canonical models with ADE points

Every constant in 59.R depends only on g|_{B_{3ρ}(p)}:
- the inner, far and outer regions are local;
- E₁ uses ℓ_g on B_{2ρ} and E_P = 0 there;
- E_P vanishes where Ric° = 0, since it is built from Ric° and its derivatives.

Since g_λ = g_KE on fixed balls about p_i away from the orbifold points, and the identity (A.1) is exact:

P(g̃_{λ,ε}) = P(g_λ) + 8π²k + kI(ε), with I(ε) independent of λ.

The argument then runs:
1. Fix ε with I(ε) = −(s²/8)π²ε²log(1/ε) + O(ε²) < 0.
2. Choose one λ with P(g_λ) < k|I(ε)|.

So p_*(X#kCP̄²) < 8π²k. No limit interchange is involved. The inputs are:
- every minimal surface of general type either has K ample, giving KE with s < 0, or has a canonical model with only rational double points;
- that canonical model carries an orbifold KE metric;
- the Kronheimer ALE gluing of Prop. 59.N.

The phrase "strictly below the Kähler tariff" additionally needs Theorem K∞, which I have not seen. Since P(g̃) < 8π²k = inf over Kähler metrics, the competitors are automatically non-Kähler.

---

## 5. Eigenvector hypothesis and where the sign of Φ holds

- **Theorem 59.R itself needs no eigenvector hypothesis.** It holds for any unit ζ and any fixed degree-0 K. C.2's sentence "Theorem 59.R/§A.3 assumes ζ is an eigenvector" should read: "§A.3 (the minimized formula) assumes ζ is an eigenvector of R⁺_p. Theorem 59.R holds for every unit ζ ∈ Λ⁺_p and every fixed K."
- **Minimum over K in §A.3.** "Minimum over K" means the minimum over all degree-0 correctors. This follows from three facts:
  1. the integrated functional is convex in K (its Hessian is |[σ¹]D𝒞[σK]|² ≥ 0);
  2. it is SU(2)₋-invariant in the (s,W⁺) sector;
  3. SU(2)₋ is compact, so averaging over it reduces to invariant K.

  This sentence should be added.
- **Remark 2.** Replace with: "Φ is a proved coefficient for every P-critical background and fixed K. Its minimized closed form −μ_ζ(μ_ζ − s/8) − |T|² holds for ζ an R⁺-eigenvector when Ric°_p = 0. For Ric°_p ≠ 0 the minimized coefficient is that value plus min_K Q_Ric(Ric°_p) ≥ 0."
- **Where Φ ≤ 0 holds.** C.2 is correct as stated:
  - Φ ≤ 0 holds on the kernel μ_ζ = 0;
  - Φ = s²/288 > 0 when W⁺ = 0;
  - Φ > 0 is possible for s/8 < μ_ζ < 0;
  - μ_ζ = 0 with R⁺ζ ≠ 0 forces R⁺ to be indefinite.

  The value Φ_Kähler∥ = −s²/32 in A.3 is the aligned direction μ_ζ = s/4. There the first-order term dominates, so it should not be read as a kernel value.
- **Corollary 59.Rig.** Replace "where |Ric°_p|² is small relative to (μ₂ − μ₃)²" by "where (μ₂ − μ₃)²/2 > min_K Q_Ric(Ric°_p)". This follows from the Schur decoupling in §3.1. The step "R⁺ ≤ 0" now rests on the proved sign 2κ = −8π², and is otherwise conditional on 53.B and the Anderson configuration.

---

## Corrected statement of Theorem 59.R

> Let (X, g) be smooth, p ∈ X, and ρ > 0 with E_P(g) = 0 on B_{3ρ}(p). Let ζ ∈ Λ⁺_p be any unit vector and K any smooth degree-0 symmetric tensor on R⁴∖0. Then
>
> P(g̃_ε) = P(g) + 8π² − 8π²εR⁺_p(ζ,ζ) + 4π²Φ(Rm_p, ζ, K)ε²log(1/ε) + O(ε²),
>
> with Φ given by (A.2). The O(ε²) constant depends only on g|_{B_{3ρ}(p)}, ζ, K, ρ and R. If ζ is an R⁺_p-eigenvector and Ric°_p = 0, then
>
> min_K Φ = −μ_ζ(μ_ζ − s/8) − |T|²,
>
> attained by K* + k₀^W.