# TTCS Independent Branch Record

```json
{
  "step_id": 52,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step52_kernel_insertion_theorem.md",
    "Sessions/S1003A01/workspace/scripts/step52_exact_su2minus_fast.py",
    "Sessions/S1003A01/workspace/scripts/step52_analyze_Q.py",
    "Sessions/S1003A01/workspace/data/step52a/exact_su2minus_analysis.json",
    "Sessions/S1003A01/workspace/notes/step50_wminus_completed_square_and_general_KE_construction.md"
  ]
}
```

## Task

Verify the mathematics of Theorem 52.A (kernel-direction Burns insertion on an arbitrary Einstein four-manifold) and Lemma 52.C in workspace/notes/step52_kernel_insertion_theorem.md. Check specifically: (1) the SU(2)_- reduction in Section 2 (is the a^2 eps^2 CGB density really constant on S^3 for SU(2)_- -invariant data, and do the 10 tensors sym(v_i v_j)/u span all SU(2)_- -invariant degree-0 symmetric 2-tensors?), and whether the exact results in data/step52a/exact_su2minus_analysis.json (F_opt = -mu(mu - s/8) - |T|^2; family F = -|T|^2 with zero gradient; mixed-block linear term) are consistent with the script step52_exact_su2minus_fast.py and the convexity/averaging argument; (2) the W^- cross-term vanishing by SU(2)_- irreducibility; (3) the two-scale remainder argument of Section 3.2: Hadamard factorization R = r^4 z^2 rho, evenness in r via the antipodal map, the claim that only h2 and k0 enter rho(0,0), and the O(eps^2) control of core and outer transition; (4) Section 3.3: that the order-eps contribution equals minus an inner-boundary flux of a transgression form, that its leading constant is a U(2)_zeta-invariant linear function of Rm_p (so alpha s + beta W+(zeta,zeta)), that the r^1 term vanishes by parity, and that the Ch.5 CH construction legitimately calibrates beta = 12 alpha (does Ch.5's Bianchi-IX neck have the same leading flux as the additive normal-coordinate neck?); (5) Lemma 52.C: delta W+ = 0 with constant eigenvalues (a,-a/2,-a/2) forcing grad u = 0, and the Kahler eigenvalue contradiction; (6) the sign correction in Section 5 and Corollary 52.B. Report errors, missing steps, and any correction that changes the theorem statement, with precise repairs.

## Output

# Verification memo: Theorem 52.A, Lemma 52.C, Corollary 52.B (Step 52)

## Bottom line

- **What holds.** The exact algebra in §2, the representation theory for W⁻, the two-scale remainder of §3.2, and Lemma 52.C are correct. The minor slips are listed under "Corrections" at the end.
- **The one real gap.** In §3.3 the proportionality θ₂ ∝ R⁺_p(ζ,ζ) is imported from Ch. 5. That import is valid only under a condition on Ch. 5's neck which the note does not verify.
- **A direct proof of θ₂ ∝ R⁺_p(ζ,ζ) exists.** It uses p₁(Λ⁺) and the Kähler property of Burns, and removes Ch. 5 from the proof (§4c below).
- **The theorem statement does not change.**
- **Corollary 52.B needs two corrections.** It must add the case R⁺_p = 0, and it must state that its "iff" is relative to the degree-0 corrector class.

---

## 1. SU(2)₋ reduction and the exact data

### Constancy on S³
- SU(2)₋ (right quaternion multiplication) lies in SO(4). It commutes with the J_m and acts trivially on Λ⁺.
- If W⁻_p = 0 and Ric°_p = 0, then Rm_p = (s/12)Id + W⁺ is SU(2)₋-fixed, so h₂ is invariant. So is k_B = (v₁v₁ᵀ+v₂v₂ᵀ)/u², because v_m = J_m x is equivariant.
- f = 4|W⁺|² + s² /12 is a natural, orientation-sensitive density, so f(φ*g) = φ*f(g) for φ ∈ SO(4).
- Invariant data therefore give an invariant density. The action on S³ is transitive, so the density is constant there.
- With vol(S³) = 2π², (8π²)⁻¹∫_{S³} = density/4. This matches `F22 = f[(2,2)]/4`.

### Spanning by the 10 tensors
- The SU(2)₋ action on S³ is free and transitive. An invariant symmetric 2-tensor field on S³ is therefore fixed by its value at one point (10 parameters).
- Degree-0 homogeneity extends it radially.
- (x, J₁x, J₂x, J₃x)/r is an invariant orthonormal frame, so the sym(v_iv_jᵀ)/u span the invariant space. The count of 10 is correct.

### Averaging
- For an invariant jet, the integrated functional of the corrector is SU(2)₋-invariant and convex quadratic.
- Its corrector Hessian equals 2·(4|W⁺'(k)|² + s'(k)²/12) ≥ 0, with eigenvalues 2, 8, 8, 4, 4, 4, 0⁴ as recorded.
- Haar-averaging a corrector therefore does not raise F. The reduction is valid.

### Independent recomputation from `F_polynomial`
- **Kernel family at CH** (s = −24, w₁₁ = 2, w₂₂ = −4, w₁₂ = 0, c₄ = 4.5, c₇ = 2.5, c₉ = 1): summing all terms gives F = −18.000. The ∂_{c₀} and ∂_{c₄} components of the gradient are 0.
- **k_B-only** (all c = 0): the jet terms sum to 12. This agrees with "CH k_B-only F = 12".
- **w₁₂ sector:** 2c₅² − (8/3)w₁₂c₅ is minimized at c₅ = 2w₁₂/3 (the family value 2T₁₂/3), contributing −8w₁₂²/9. Together with −10w₁₂²/9 this gives −2w₁₂², as in `Fopt`.
- **Closed form:** with a = w₁₁, b = w₂₂, μ₃ = s/12 − a − b,
  288[−μ₃(μ₃ − s/8) − |T|²] = s² + 12s(a+b) − 432a² − 288ab − 432b² − 576w₁₂²,
  where |T|² = (a−b)²/2 + 2w₁₂². This is exactly `Fopt`, so Theorem 2.1 agrees with the data.
- **Null directions:**
  - c₁, c₂, c₃ multiply sym(x⊗J_m x)/u = ½ L_{(log r)J_m x}δ.
  - The fourth is δ = P₀+P₁+P₂+P₃. Its quadratic value is 9 − 9 = 0, and its linear coefficient vanishes identically in (s, w): the s-coefficients sum to −1+1+1−1 = 0, and the w₁₁ (and w₂₂) coefficients sum to −1 + 5/3 + 13/3 − 5 = 0.
  - This is the scale-invariance identity: adding a multiple of δ to the corrector rescales. It is a good internal check of the pipeline.
  - The linsolve output lists "c₉" as free, rather than naming δ.
- **Mixed block:** F − F|_{w₁₃=0} = −2c₂w₁₃ + 10c₆w₁₃/3 + 14w₁₃²/9 = 2w₁₃(−9c₂ + 15c₆ + 7w₁₃)/9, as stated.
  - c₂ is a Hessian-null direction with linear coefficient −2w₁₃, so F is unbounded below when w₁₃ ≠ 0.
  - When R⁺ ≤ 0, μ_ζ = 0 forces R⁺ζ = 0, hence w₁₃ = 0. That step is correct.

### Two JSON fields carry no evidential weight
- `Fopt_w13_part = "0"` and `Fopt_in_mu` are computed after `F = F.subs(w13, 0)`, so they are vacuous. The w₁₃ statement rests only on the mixed-block line.
- The `[aε]` coefficient vanishes automatically. The a¹ε¹ part of |𝒞|² is ⟨𝒞₁₀, 𝒞₀₁⟩, and 𝒞₀₁ = 0 for flat Burns. It says nothing about the order-ε term, which sits at a²ε¹ and is in any case a flux (§4).

### Script bug in one output field
- `CH_family_coeffs` prints "−s/72 + w11/6 + 23/6" because of the substitution order (`chs` applied before `ker`).
- Substituting s = −24, w₁₁ = 2 gives 23/6 + 4/6 = 9/2, so (4.5, 2.5, 1) is right.
- The match with Step 50 also holds: k₀^{c*} = v₁v₁ᵀ/u + 2c₁v₀v₀ᵀ/u + … = (4.5, 2.5, 1) on (other kernel direction, ω, ζ), with "+1" on the ω fibre.

### Path inconsistency
- The script writes to `data/step52` unless `OUTDIR=step52a` is set; the analysis reads `step52a`.

### Pipeline conventions
- The orthonormal frame g^{−1/2}, the flat J-basis with ½ normalization, and series truncations of order 4 suffice for total degree (2,2).
- The h₄ jet cannot enter the a²ε² coefficient, since it pairs only with 𝒞₀,· = 0. Using the 2-jet alone is therefore legitimate.

## 2. W⁻ cross terms and self-term

- The integrated a²ε² coefficient is a quadratic form on jet ⊕ corrector, jointly invariant under SU(2)₋.
- The map W⁻ ↦ (h_W, k₀^W) is SU(2)₋-equivariant (k_B and δ are invariant), so its image lies in the spin-2 isotypic part.
- A bilinear pairing between invariant vectors and spin-2 vectors is an invariant functional on spin 2, hence zero. This is correct.
- **Self-term.** Expand |𝒞|² = |𝒞₁₁|² + 2⟨𝒞₁₀, 𝒞₁₂⟩ plus volume/norm factors multiplying 𝒞₁₀. Here 𝒞₁₀ contains no W⁻, since h_W is pure W⁻. So the only W⁻⊗W⁻ term is |𝒞₁₁^W|², which vanishes by the Step-50 identity.
- That identity involves only δ, h_W, k_B and ζ. It therefore holds on any background, not just KE.
- **Optimality ("iff" in Corollary 52.B).** For general non-invariant correctors c = c₀ + c_rest:
  - Q splits as Q(j₀, c₀) + ∫|𝒞₁₁(j₂, c_rest)|².
  - The second piece is ≥ 0.
  - Hence −|T|² is the infimum over all degree-0 correctors, not only invariant ones.

## 3. The two-scale remainder (§3.2)

- **Notational slip.** "G(r,x) = r⁻²(g(rx) − δ)" should read G(r,x) = g(rx) − δ.
  - The pullback supplies the factor r², so ĝ_r(x) = g(rx).
  - The expansion r²h₂ + r³h₃ + … and the terms z k_B, z r² k₀ are then correct.
- **Smoothness.** Ψ is smooth on [−T₀, T₀] × [0, 1/4] by Taylor's formula with integral remainder. Real-analyticity is not needed, which is an improvement on Step 50.
- **Evenness.** The antipodal map A has det(−I) = +1 on R⁴ and preserves the orientation of S³. It sends G(r, −x) to G(−r, x), fixes the even tensors k_B, P_m and k₀^W, and commutes with f. So Ψ(r,z) = Ψ(−r,z).
- **Order r⁴ and Hadamard factorization.** ĝ_{r,z} − ĝ_{0,z} = O(r²) with no r¹ term, and 𝒞(ĝ_{0,z}) = 0. Hence Ψ = r⁴Ψ̃ with Ψ̃ smooth and even, and R = r⁴z²ρ with ρ even and ρ(0,0) = ½∂_z²Ψ̃(0,0).
- **Only h₂ and k₀ enter ρ(0,0).** The r⁴ coefficient of |𝒞|² is |𝒞₂(z)|²_{ĝ₀,z} dV_{ĝ₀,z}, which depends on h₂, z k₀ and the exact z-dependence through k_B. h₃ enters first at r⁵. Script variables match: a = r², ε = z.
- **Neck integral.** |ρ − F| ≤ C(r² + z), and ∫(r² + ε/r²) dr/r = O(1). This gives (F/2)ε² log(1/ε) + O_T(ε²).
  - The normalization 8π²·(F/2) = 4π²F matches the theorem.
  - At CH this reproduces 8π²(−9ε² log(1/ε)).
- **Core.** In the core f = 4|R⁺|² dV is quadratic in a curvature that vanishes on Burns. With ε⁻¹Φ*_{√ε}g_ε = Burns₁ + O(ε) in C², f = O(ε²) there.
  - No P-criticality of Burns is needed; Step 50(B) needed it.
  - ∫_{B_{2√ε}} f(g) = O(ε²).
- **Outer transition.** The O_T(ε²) estimate is correct.
- **Gluing.** The two formulas for g_ε agree. Positivity holds. δ + εk_B is Burns for J₃: its Kähler potential |z|² + ε log|z|² gives εk_B on span(J₁x, J₂x), and in polar form the metric is dr² + (r² + ε)(σ₁² + σ₂²) + r²σ₃².

## 4. The order-ε flux (§3.3)

### (a) Flux identity — correct
- z∂_zΨ(r,0) = ε ∂_ε|₀ of the density of g + εk at fixed r.
- Neck plus outer region therefore give ε∫_{r ≥ 2√ε} Df_g[χ_out k].
- For Einstein g, D(|Ric°|² dV) = 0 pointwise, and the e and l variations are exact.
- Since χ_out k vanishes near r = 2T, the integral equals −Λ(2√ε), with the sign fixed by the inward orientation of the inner sphere.

### (b) Expansion of Λ — correct
- Scale invariance gives Λ(r) = (ε/r²)∮_{S³} Θ_{ĝ_r}(k_B) + ε∮_{S³} Θ_{ĝ_r}(k₀).
- Θ is linear in curvature, which is O(r²), so Λ(r) = ε[θ₂ + rθ₃ + O(r²)].
- θ₃ is linear in h₃ and odd under A, so θ₃ = 0. At r = 2√ε the remainder is O(ε²).
- The linear U(2)_ζ invariants of Rm_p are only s and W⁺(ζ,ζ):
  - W⁻ has spin 2 and Ric° has spin 1 under SU(2)₋;
  - W⁺(ζ, ζ^⊥) has U(1)₊-weight 1 and T has weight 2.

### (c) Calibration by Ch. 5, and a direct replacement
The arithmetic α(−24) + 2β = 0 ⇒ β = 12α is right. Its validity, however, requires Ch. 5's neck in g_CH-normal coordinates to be g_CH + ε(c·k_B + L_Xδ + degree ≥ 0) + O(ε²), with X of degree −1.

**Gauge terms are harmless.**
- Df_g[L_X g] = d(ι_X f(g)).
- Hence ∮_{S_ρ} Θ(L_X g) = ∮_{S_ρ} ι_X f(g) = O(ρ³·ρ⁻¹) → 0.

**A non-gauge degree −2 piece would spoil the calibration.**
- Example: the conformal mode δ/r². The factor (1 + ε/r²)² is harmonic, so it is conformally flat and scalar-flat, and it lies in the linearized kernel.
- If Ch. 5's radii perturb dt², or perturb the σ₃² coefficient at order ε/r², this must be checked against its formulas.
- The fact that Ch. 5's expansion starts at 8π² strongly suggests a Burns core. Even so, this is an unverified identification, and the note leans on it.

**Direct proof (removes Ch. 5).**
1. Hirzebruch–Hopf gives p₁(Λ⁺) = p₁ + 2e. Hence f − |Ric°|² dV = 16π²e + 8π²p₁ = 8π²p₁(Λ⁺) as forms, with f = 4|R⁺|² dV since 4|W⁺|² + s²/12 = 4|R⁺|².
2. Therefore Θ_f(h) = κ·tr(Γ̇⁺[h] ∧ F⁺). Here Γ̇⁺ is the variation of the induced connection on Λ⁺, F⁺ its curvature, and F⁺ = R⁺ for Einstein g.
3. δ + εk_B is Kähler for ζ for every ε, so ∇^ε ζ = 0. Differentiating, Γ̇⁺[k_B] annihilates ζ, so Γ̇⁺[k_B] = ζ ⊗ a with a a U(2)-invariant 1-form of degree −3.
4. Hence Θ_f(k_B) = κ a ∧ R⁺_p(ζ) to leading order, where R⁺_p(ζ) = Σ_j R⁺_p(ζ, J_j) J_j. The corrections from h₂ in Γ̇ are O(r⁻¹)·O(1), which contribute O(r²) to the sphere integral.
5. By U(1)₊ invariance, ∮ a ∧ J₁ = ∮ a ∧ J₂ = 0. Therefore
   **θ₂ = κ (∮_{S³} a ∧ ζ) · R⁺_p(ζ, ζ),**
   which is proportional to s/12 + W⁺(ζ,ζ), i.e. β = 12α, without any calibration.

This also explains the TTCS value ℓ = −R⁺_p(ζ,ζ) and A02's first-order term ⟨R⁺_p, UΦUᵀ⟩. The constant κ∮a∧ζ is a finite exact rational integral over S³ computable in the existing pipeline. It fixes both the size and the sign of β, which Corollary 52.B needs and which the note currently takes from Step 8. With this argument, Theorem 52.A becomes [P] without the [C] tag.

### (d) Reach
- The proof uses only that g is Einstein on B_{4T}(p). Closedness enters only through P(g) = 0.
- For Ric°_p ≠ 0, the extra order-ε term is ε∫⟨Ric°, DRic°[k_B]⟩. Its potential ε log(1/ε) part has zero coefficient, because the S³-average of b = (2/r⁴)(δ − 2θθ − 2JθJθ) vanishes. So Ric°_p first enters at higher order. This is relevant to open item 2.

## 5. Lemma 52.C

- W⁺ = (3a/2)u⊗u − (a/2)Id_{Λ⁺} with a constant (s is constant). Its eigenvalues are (a, −a/2, −a/2).
- δW⁺ = 0 gives (div u)_j u_{kl} + u_{ij}∇^i u_{kl} = 0.
- Contracting with u^{kl}, and using |u|² constant, gives div u = 0. Invertibility of the self-dual form u then gives ∇u = 0.
- So g is Kähler for u, which forces W⁺(u) = (s/6)u. But W⁺(u) = −(s/12)u, so s = 0, a contradiction.
- The proof is correct. A smooth local unit eigenform exists because the eigenvalue is simple.
- It is also an immediate case of Derdziński's theorem: with at most two eigenvalues, |W⁺|^{2/3} g is Kähler; here |W⁺| is constant, so g is Kähler. That gives an independent cross-check.
- The Laplacian value is (s/2)a − 6a² + 2·(3a²/2) = −9a², with s = −12a. The Weitzenböck sign is confirmed on KE, where the right-hand side vanishes on both eigenvalues. A radially parallel e has Δe(p) = 0.

## 6. Corollary 52.B and the §5 sign statement

**Missing case in Corollary 52.B.**
- R⁺_p = 0 (s = 0 and W⁺_p = 0; e.g. hyperkähler K3 or flat T⁴) is not listed.
- There every ζ is a kernel vector with T = 0, so there is no decrease at order ε or ε² log.
- The corrected list of non-decreasing cases is:
  1. R⁺_p < 0 (forces s < 0);
  2. R⁺_p ≤ 0 with spectrum (0, s/8, s/8) (forces s < 0);
  3. R⁺_p = 0.
- The garbled clause "Both require s<0 if W⁺≠0 or s≠0" should be replaced by this list.
- A two-dimensional kernel (0, 0, s/4) with s ≠ 0 gives T ≠ 0 and does decrease.

**Qualifiers the "iff" needs.**
- It refers to Burns insertions with degree-0 correctors in this two-scale ansatz.
- The positive-eigenvalue branch needs β > 0, from the explicit θ₂ above or from Step 8.

**§5 statements.**
- Correct:
  - F_opt = −μ(μ − s/8) − |T|²;
  - W⁺ = 0 gives s²/288 > 0;
  - R⁺ ≤ 0 means λ_max(W⁺) ≤ −s/12;
  - the maximum of Σλ² is attained only at (a, a, −2a), giving |W⁺|² ≤ s²/24 with equality only on two-dimensional kernels, where T ≠ 0;
  - the order-ε cost dominates in the interior of R⁺ < 0.
- Fix: positivity of the log coefficient there requires μ(μ − s/8) + |T|² < 0. The phrase "generally −μ(μ − s/8) > 0" describes only the first term.

## Corrections to the note

1. In §3.2, set G(r,x) = g(rx) − δ.
2. Replace the Ch. 5 calibration in §3.3 by the p₁(Λ⁺)/Kähler argument of §4c, and compute κ∮a∧ζ exactly. Alternatively, state the required degree −2 form of Ch. 5's neck explicitly.
3. In Corollary 52.B, add the case R⁺_p = 0 and the qualifiers of §6.
4. Weaken the hypothesis of Theorem 52.A to "g Einstein on B_{4T}(p)".
5. Rename one of the two uses of T (the radius and the trace-free matrix).
6. Fix `CH_family_coeffs`, set `OUTDIR=step52a`, and drop the vacuous w₁₃ fields as evidence.

The Theorem 52.A expansion P(g_ε) = P(g) + 8π² − 4π²|T|² ε² log(1/ε) + O(ε²) stands as written.