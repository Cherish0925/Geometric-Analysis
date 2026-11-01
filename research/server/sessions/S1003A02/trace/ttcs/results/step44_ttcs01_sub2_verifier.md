# TTCS Independent Branch Record

```json
{
  "step_id": 44,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md",
    "Sessions/S1003A02/workspace/scripts/step44_perturbative_ke.py",
    "Sessions/S1003A02/workspace/data/step44_perturbative_ke.json",
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md",
    "Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md"
  ]
}
```

## Task

Verify, as a careful geometric analyst, the two new results in Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md (Theorem A: cover-independent perturbative coercivity of the Einstein defect P=∫|Ric°|² and of the monopole Nijenhuis energy near compact complex-hyperbolic surfaces; Proposition Π: pocket refinement of the almost-Kähler profile inequality AKΓ). The computation is in workspace/scripts/step44_perturbative_ke.py with output workspace/data/step44_perturbative_ke.json. Check specifically: (1) the Koiso Bochner identity <L_E h,h> = ||d^∇h||² + <(-λ - R̊)h,h> for TT h on Einstein manifolds (normalization of ||d^∇ h||², sign of R̊ convention: R̊h=-h on trace-free tensors of the unit sphere), and the computed spectrum R̊ = -2 (J-invariant, dim 3), +4 (J-anti, dim 6) on CH² with holomorphic sectional curvature -4 (λ=-6), giving pointwise gap 2 = |λ|/3; whether this agrees with the known infinitesimal rigidity of ball quotients and whether the gap is genuinely Γ-independent. (2) the linearized Seiberg–Witten analysis (G4): cancellation of first-order cross terms when ∇Φ₀=0 with gauge coefficient -1/2, the potential eigenvalues (1/2 on 1-forms, 2, 1, 0,0 on spinors at s=-4), and the claim that the two zero modes on Φ₀^⊥≅Λ^{0,2}≅K^{-1} are lifted by the Kodaira/Landau identity with |iΛF|=2|λ|; check whether the use of ||d^*a||²+||d^+a||² ≥ (1/2)<Δ_d a,a> loses a needed term, and whether a spectral gap of 1/2 is really cover independent. (3) the proof sketch of Theorem A: the conformal slice g=e^{2f}(g_Γ+k), the claim that P and the monopole direction depend on f only through df (exact conformal formulas), uniform Hölder inverses via lifting along the exponential map without injectivity radius bounds, the cubic remainder bounds, and the comparability 2P ≤ R ≤ C'P using Theorem N (Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md). Identify any gap that would make the constant Γ-dependent or the theorem false, and repair it if possible. (4) Proposition Π: the two-region Jensen argument, the minimum 6D² of 2x²+(3y-2x)² on y-x=D, the identities σ̄-δ̄=(ℓ/2V)(1-θ), the final bound 2/(3-2φ), and the interpretation (tiny-area Burns spheres aligned with ω save at first order iff s*>0 since R⁺(ω̂,ω̂)=s*/4); compare with AKΓ in Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md. (5) Judge the scope paragraph: whether the stated obstacles to the blow-up/localized version (bulk monopole selection, local Einstein deformations) are the real ones, and whether some stronger statement about near-minimizers on X_Γ#k CP̄² does follow. Give corrected statements where needed; do not invent literature.

## Output

# Verification of Step 44: Theorem A (perturbative coercivity at ball quotients) and Proposition Π (pocket price)

## Summary

- **Algebra.** The Koiso Bochner identity, the CH² spectrum of R̊, the conformal and gauge identities, the Clifford computation for the Seiberg–Witten linearization, and all of Proposition Π are correct. I rechecked each by hand.
- **Item 3 of Theorem A has a sign error.** The inequality 2P ≤ R does not follow from Theorem N, and it is false in general.
- **Γ-uniformity is not proved as written.** The note says that an L² gap combined with Combes–Thomas decay gives Γ-uniform Hölder inverses. It does not.
  - Item 1 can be repaired: the slice can be taken in gauges whose linearizations have a pointwise maximum principle.
  - Item 2 (the monopole branch) is proved for each fixed Γ. Its Γ-uniformity reduces to one harmonic-analysis question on CH², stated in §3.3.
- **A stronger, field-free localized statement does follow.** It comes from Theorem W of Step 40, and it removes both obstacles listed in the closing paragraph of §2 for the purpose of pricing the saving.

---

## 1. (G1) Koiso identity and the CH² spectrum

**Identity.** Regard h as a T*-valued 1-form, with (d^∇h)(X,Y,Z) = (∇_Xh)(Y,Z) − (∇_Yh)(X,Z). The norm of d^∇h is the 2-form norm (a factor ½ against the full tensor norm). For δh = 0 the Bochner formula is

‖d^∇h‖² = ⟨∇*∇h,h⟩ − ⟨R̊h,h⟩ + λ‖h‖².

Substituting into L_E = ∇*∇ − 2R̊ gives

⟨L_Eh,h⟩ = ‖d^∇h‖² + ⟨(−λ−R̊)h,h⟩.

This matches the note.

**Normalization of L_E.** For TT h one has s′(h) = 0. Then

d/dt Ric°(g+th) = ½Δ_Lh + λh − λh = ½(∇*∇h − 2R̊h) = ½L_Eh,

which agrees with step (b) of the proof.

**Sign convention for R̊.** The script uses Rm_{abcd} = c(g_{ac}g_{bd} − g_{ad}g_{bc}). This gives R̊h = c(tr h·g − h), so R̊h = −h on trace-free tensors of the unit sphere, as required.

**CH² spectrum.** With Rm = (c/4)[… + 2J_{ab}J_{cd}] and J antisymmetric:

R̊h = (c/4)(tr h·g − h − 3JhJ).

- On J-invariant h (JhJ = −h): R̊ = c/2 = −2.
- On J-anti-invariant h (JhJ = h): R̊ = −c = 4.
- The dimensions are 3 (trace-free Hermitian forms on C²) and 6.
- With λ = 3c/2 = −6, the pointwise gap is −λ − a = 2 = |λ|/3, which is 1/3 at s = −4.

**Consistency checks.**
1. The formula holds in every complex dimension n. On CH^n one has λ = −2(n+1) and R̊ = 4 on the J-anti sector, so the gap is 2n − 2. This vanishes exactly at n = 1, where the Einstein deformations are the Teichmüller deformations. It is positive for n ≥ 2, matching the infinitesimal Einstein rigidity of compact ball quotients of complex dimension ≥ 2 via Koiso's pointwise condition a < −λ.
2. The binding sector is the J-anti sector, which carries complex-structure deformations. This is consistent with Calabi–Vesentini.

**Γ-independence.** The inequality is pointwise algebraic plus one integration by parts on a closed manifold. It is therefore Γ-independent. There are no Killing fields because Ric < 0.

**Uniform H² control.** H² control from ‖L_Eh‖ is also uniform without local charts: on a locally symmetric space ∇Rm = 0, so ‖∇²h‖² = ‖∇*∇h‖² + (curvature)·‖∇h‖² globally.

**(G2) and (G3).** Both verified:
- ‖∇²f‖² = ‖Δf‖² + |λ|‖df‖², hence ‖(∇²f)°‖² = ¾‖Δf‖² + |λ|‖df‖².
- ‖(L_Xg)°‖² = 2‖∇X‖² + 2(1−2/n)‖div X‖² + 2|λ|‖X‖².
- Orthogonality of the TT and Hessian channels follows from L_E∇²u = ∇²(Δ−2λ)u together with δδk = 0. Correct.

## 2. (G4) Linearized Seiberg–Witten operator

**Normalization.** Step 44 uses c(F⁺) = (ΦΦ*)₀ and |Φ₀|² = −s = 4. Step 40 uses ρ = |Φ|² ∈ [0,2] at s = −4. The two fields differ by a constant factor (Φ₄₀ = Φ₄₄/√2). The direction n is unaffected; the weight ρ² in R changes by a factor 4. This should be stated before item 3 is combined with Theorem N.

**Hand check of the potential eigenvalues.** All agree with the JSON.

| Sector | Contributions | Total |
|---|---|---|
| 1-forms a | ½λ (from ½⟨Δ_d a,a⟩) + \|½α·Φ₀\|² = −½ + 1 | ½ |
| ψ ∥ Φ₀, real | Dirac −1 + ½(4−2) = 0; σ′ term 2 | 2 |
| ψ ∥ iΦ₀ (gauge direction) | Dirac 0; σ′ = 0; gauge (−½·Im⟨Φ₀,ψ⟩)² | 1 |
| ψ⊥ ∈ Φ₀^⊥ | Dirac −1 − 1 = −2; \|σ′\|² = 2; gauge 0 | 0 |

**Cross terms.** Cancellation at the symbol level for c_g = −½ is what one expects when the gauge slice is the L²-orthogonal complement of the infinitesimal gauge orbit. It is exact after integration by parts because ∇Φ₀ = 0. The JSON scan confirms that only (sign_σ = 1, c_g = −½) works.

**Landau lift.** On Φ₀^⊥ = Λ^{0,2} = K⁻¹ with the Chern connection, iF = λω and Λω = 2, so |iΛF| = 2|λ|.
- Either form of the Kodaira identity, ∇*∇ = 2∂̄*∂̄ + iΛF = 2∂*∂ − iΛF, gives ∇*∇ ≥ |iΛF| when iΛF is constant.
- Here K⁻¹ has iΛF = 2λ < 0, and the second form gives ∇*∇ ≥ 2|λ|.
- The splitting S⁺ = CΦ₀ ⊕ Φ₀^⊥ is parallel, so ‖∇ψ‖² splits accordingly.

**The dropped term.** The inequality ‖d*a‖² + ‖d⁺a‖² ≥ ½⟨Δ_d a,a⟩ discards exactly ½‖d*a‖² ≥ 0, which is never needed. It does not interfere with the cross-term bookkeeping: the cross pairing of d*a with the gauge zeroth-order term is already in the script's M^j.

**Error in the displayed bound.** The displayed inequality uses ‖∇ψ⊥‖² twice. On ψ⊥ the pointwise potential is 0, so the whole gradient term is consumed to produce 2|λ|‖ψ⊥‖². One cannot also keep ‖∇ψ⊥‖² + (|λ|/2)‖ψ⊥‖². Splitting ‖∇ψ⊥‖² as ¾ + ¼ gives a correct version at λ = −1:

‖𝓛(a,ψ)‖² ≥ ½‖∇a‖² + ¾‖∇ψ‖² + ½‖(a,ψ)‖²,

and in particular ‖𝓛‖² ≥ ½(‖∇(a,ψ)‖² + ‖(a,ψ)‖²). This L² gap is pointwise-plus-integration-by-parts. It is therefore Γ-independent, and it also holds on CH² for compactly supported sections.

## 3. Proof of Theorem A

### 3.1 The Hölder-inverse sentence does not hold as argued

**What works.** Lifting along exp_p (a covering by Cartan–Hadamard) gives local Schauder estimates with Γ-free constants, but only in terms of a local C⁰ (or uniformly-local L²) bound. The L² gap controls the global L² norm, which is extensive.

**What is needed.** A C⁰ bound for data that are O(ε) pointwise needs one of two things:
- a pointwise maximum principle, i.e. a Laplace-type operator ∇*∇ + V with V ≥ μ > 0 pointwise, via Kato's inequality; or
- integrability ∫_{CH²}|G̃(x,y)| dy < ∞ of the Green kernel on the universal cover. The periodized kernel on X_Γ has L¹ norm in y bounded by this integral.

**Why Combes–Thomas does not close it.** In s = −4 units, CH² has volume growth e^{2ρr} with 2ρ = 4/√6 ≈ 1.633 (ρ² = 2/3 is the bottom of the scalar spectrum). For a form ≥ c‖∇u‖² + μ‖u‖², Combes–Thomas yields decay e^{−δr} only for δ² < μ/c. For the SW linearization this gives δ < 1 < 1.633.

**Which operators have a maximum principle.**

| Operator | Laplace type? | Pointwise potential | Maximum principle |
|---|---|---|---|
| Yamabe 6Δ + 2\|s\| | yes | 2\|s\| > 0 | yes |
| DeTurck/Bianchi gauge ∇*∇ + \|λ\| on 1-forms | yes | \|λ\| > 0 | yes |
| L_E on TT | yes | −2R̊ has eigenvalues 2/3 and −4/3 at s = −4 | no |
| York operator X ↦ δ(L_Xg)° | no | — | no |
| SW L*L | no (1-form part is ½Δ_d + ½dd*) | ψ⊥ potential vanishes pointwise | no |

So the exact TT slice and the monopole branch are not covered by the note's argument.

### 3.2 Repair of item 1 (Γ-independent)

1. **Yamabe normalization.** Replace g by its s = −4 Yamabe representative ĝ = e^{−2f}g. The linearization 6Δ + 8 has L^∞ inverse norm ≤ 1/8. Together with exp-lift Schauder estimates, this makes ĝ and f Cε-close in C^{2,α} uniformly.
   - P(g) = ∫|Ric°(ĝ) − 2(∇̂²f − df⊗df)°|² exactly. Scale invariance and dimension four make |·|²dμ conformally invariant.
   - So P(g) depends on f only through df and ∇²f, as the note states.
2. **Bianchi gauge.** Choose φ with β_{g_Γ}(φ*ĝ) = 0, where β(h) = δh + ½d tr h. The linearization is β(L_Xg) = ∇*∇X + |λ|X, which is Laplace type with positive potential. It is uniformly invertible in C^{2,α} with no injectivity-radius input. Set k = φ*ĝ − g_Γ, which satisfies |k|_{C^{2,α}} ≤ Cε.
3. **L² York decomposition only.** Write k = k_TT + L_Xg_Γ + u g_Γ.
   - **Scalar normalization pins u.** s′(ug) = 3Δu + 4u and s′(k_TT) = s′(L_Xg) = 0. Since s(ĝ) = s(g_Γ), u solves an equation with mass term 4 and quadratic right side, so ‖u‖_{H²} ≤ Cε‖k‖_{H²}. No Poincaré inequality is used. This matters, because λ₁(X_Γ) is not a pointwise quantity and no Γ-uniform lower bound for it is available here.
   - **Gauge controls X.** β(ug) = du, so ∇*∇X + |λ|X = −du and ‖X‖_{H³} ≲ ‖du‖_{H¹}.
   - Hence ‖k‖_{H²} ≤ 2‖k_TT‖_{H²} for small ε.
4. **Expansion.** DRic°(L_Xg_Γ) = 0, and the pointwise quadratic remainder is |k||∇²k| + |∇k|². This gives
   P(g) ≥ (1−η)(¼‖L_Ek_TT‖² + 4‖(∇̂²f)°‖²) − Cε‖k‖²_{H²} − Cε‖k‖_{H²}‖df‖_{H¹}.

**Conclusion.** P(g) ≥ κ(‖k‖²_{H²} + ‖df‖²_{H¹}) with κ depending only on CH². Only maximum-principle operators enter at the Hölder level.

### 3.3 Item 2: proved for each Γ; Γ-uniformity reduces to one computation

**The conformal ansatz is correct.**
- σ_{g̃}(e^{−f}Φ) = σ_ĝ(Φ) as 2-forms, because c_{g̃} = e^{−2f}c_ĝ on 2-forms.
- The Dirac error is D_{g̃}(e^{−f}Φ) = ½e^{−2f}df·_ĝΦ. The note's e^{−5f/2} is a harmless exponent slip.
- The L² linear response gives ∫|∇n|² ≲ ‖k‖²_{H¹} + ‖df‖²_{L²}.

**Where Γ enters.** Existence and uniqueness of the branch in a C⁰ neighbourhood need the L^∞ (or uniformly-local) inverse discussed in §3.1. For fixed Γ this holds by compactness, with C = C(Γ).

**The Γ-free condition.** Item 2 becomes Γ-free exactly when the gauge-fixed L*L at the canonical solution on CH² has an L¹-integrable Green kernel. Equivalently, in each homogeneous sector of the U(2)-reduced radial system the kernel decays faster than e^{−(4/√6)r}. This is a finite computation: one ODE per K-type, or the spherical transform on PU(2,1)/U(2).

**Margins.** The L² margins look favourable. The ψ⊥ sector has L² bottom 2, the 1-form sector ½ with gradient coefficient ½, and both exceed (coefficient)·ρ². This is not a proof. In the ψ⊥ sector the lowest Landau level is an L² eigenvalue whose Bergman-type projection has a non-integrable kernel, so the decisive quantity is whether 0 lies in the L^∞ spectrum.

### 3.4 Item 3: 2P ≤ R is false

At Q = 0, Theorem N reads −P = ½R − N₊, where N₊ is the sum of the subtracted terms (each ≥ 0). That is, R = 2(N₊ − P). This gives R ≤ 2N₊ and nothing of the form R ≥ 2P.

**Counterexample.** Suppose h^{1,1}(X_Γ) ≥ 2, i.e. b⁻ ≥ 1.
- A constant-scalar-curvature Kähler metric in a nearby, non-canonical Kähler class exists by the implicit function theorem, since there are no holomorphic vector fields.
- Normalized to s = −4, it is its own Yamabe representative.
- It is Kähler but not Einstein, so P > 0.
- Its canonical solution has ∇Φ₀ = 0, so R = 0.

**Correct statement.** Only R(ĝ) ≤ C′P(ĝ) holds, and it carries the same Γ-uniformity status as item 2.

**Consequence for the common-mode remark.** The deduction "a common mode with P ≪ A cannot sit within ε₀ of KE" uses only R ≤ C′P. It is unaffected by the error but inherits item 2's status.

## 4. Proposition Π

**Verified steps.**
- **AKΓ density.** G = [2σ² + (3δ−2σ)²]/192π², from |W⁺|² ≥ (3/2)W⁺(u,u)² with W⁺(u,u) = (3δ − 2σ)/12.
- **Two-region identity.** φG(v₁) + (1−φ)G(v₂) = G(v̄) + φ(1−φ)G(u). This is exact for homogeneous quadratics; the mixed terms cancel.
- **Constraint.** The pocket mean constraint is u_δ − u_σ ≥ D := (σ̄ − δ̄)/(1−φ). Dropping the complementary constraint keeps a lower bound.
- **Minimum.** With y = x + D, 2x² + (3y−2x)² = 3x² + 6Dx + 9D² has minimum 6D² at x = −D. For D > 0 the minimum on y − x ≥ D sits on the line y − x = D.
- **Blair.** ∫(2σ − δ) = ℓ, so σ̄ = (1+θ)ℓ/2V, δ̄ = θℓ/V, and σ̄ − δ̄ = (1−θ)ℓ/2V.
- **Excess.** 6Vφ(σ̄−δ̄)²/((1−φ)·192π²) = (ℓ²/128π²V)(φ/(1−φ))(1−θ)².
- **Optimization.** Write ψ = φ/(1−φ). Then θ* = (1+ψ)/(3+ψ) = 1/(3−2φ), with minimum 2(1+ψ)/(3+ψ) = 2/(3−2φ). For θ ≥ 1, Γ ≥ 2 ≥ 2/(3−2φ).
- **Numerics.** The brute-force samples lie above the formula, as a lower bound requires. The 0.5% excess at φ = 0.3 is sampler coarseness.

**The optimum sits at s* = 0 exactly.** At the minimizer u = (−D, 0), so σ₁ = δ₁ = δ̄. The cheapest pocket in the relaxation sits at s* = 0, where the Burns first-order saving x₀s*/4 vanishes. The relevant price is for pockets {s* ≥ s₀}. The same computation with D = (σ̄ − δ̄ + s₀)/(1−φ) gives

C₊ ≥ (ℓ²/128π²V)[Γ(θ) + (φ/(1−φ))(1 − θ + 2Vs₀/ℓ)₊²].

Against a total first-order saving of 2π²x₀s₀ per aligned sphere, a pocket of 4-volume v costs ≈ v(σ̄+s₀)²/4 in P. For v ~ r⁴ with r ≳ √x₀ the cost is O(x₀²) against a saving O(x₀). So Π confirms reading (b): convexity does not exclude small aligned pockets.

**Correction to (d).** Under H_L (η ≥ 1),

P/8π² ≥ k − A(1−2φ)/(3−2φ).

This improves LeBrun's threshold A/3 for every φ > 0, by roughly (4/9)Aφ for small φ. It is not informative "only near φ = 1/2". Since aligned Burns pockets have φ → 0, the improvement is O(φ), consistent with (b).

**(c) holds pointwise without Theorem A or monopoles.** For any almost-Kähler form, s* = 4W⁺(u,u) + s/3. At s = −4 a Kähler-type W⁺ has spectrum (−2/3, 1/3, 1/3), so s* ≤ 4λ_max(W⁺) − 4/3 ≤ 0 at exact Kähler curvature. Hence:
- pockets {s* ≥ s₀} lie in {λ_max(W⁺) ≥ 1/3 + s₀/4};
- they are excluded wherever the metric is C²-close to Kähler geometry with s = −4.

The note's quantitative version has two problems:
- it mixes the almost-Kähler form ω with the monopole direction n_g, which need not coincide;
- with |ω|² = 2 one has |∇ω|² = 2|∇u|², so the bound is ∫|∇u|² ≥ 2 Vol rather than 4 Vol.

## 5. The closing paragraph of §2 and a stronger localized statement

**The two stated obstacles are real for localizing the Nijenhuis energy.**
- **Bulk selection.** The Weitzenböck L² bound is extensive. It applies already on X_Γ itself, where it is precisely the uniform-branch question of §3.3.
- **Outer layer.** Local Einstein deformations of CH² form an infinite-dimensional family, so a collar term is unavoidable in any local coercive estimate.

**Neither obstacle affects pricing the saving.** The reason is that Theorem W's integrand is pointwise in (W⁺, ρ, n). Write W⁺ = W_* + E′, where W_* = K_ω̂ = I/3 − ω̂ω̂ is the Kähler-type tensor of amplitude 1 at s = −4, and c = ⟨n, ω̂⟩.

**Computation at Kähler-type W⁺.**
- x = M(n,n) = 1/3 − c² + ρ²/6.
- |M|² = (2/3)(a² + 1) − 2a(c² − 1/3), with a = ρ²/4.
- The Theorem-W density is f = ρ²x − 4|M|² + (2−ρ)(ρ−1)(3ρ+2)/3 = ρ²c² − ρ²/3 − 8/3 + (2−ρ)(ρ−1)(3ρ+2)/3.
- Maximizing at c² = 1:
  **f ≤ −(2−ρ)²(ρ+1) ≤ 0**, with equality only at ρ = 2, n = ±ω̂.

**Lipschitz extension.** f is concave in W⁺. Its gradient at W_* is ρ²(nn)₀ − 8M_*, with |M_*| ≤ √2. Hence f ≤ C₀|E′| with C₀ ≤ 4√(2/3) + 8√2 < 15.

**Proposition (field-free localized bound).** Under the quantifiers of Theorem N (b⁺ ≥ 2, the stated basic classes, A − k > 0, scalar −4 representative ĝ):

8π²k − P(g) ≤ 8π²k − P(ĝ) ≤ C₀ ∫_M dist(W⁺_ĝ, 𝒦) dμ_ĝ,

where 𝒦 is the SO(3)-orbit of spectrum (−2/3, 1/3, 1/3). By Hoffman–Wielandt, dist(W⁺, 𝒦) is the Euclidean distance between sorted spectra. This uses no choice of solution, no elliptic estimate and no collar.

**Consequences.**
1. In regions where ĝ is Kähler, or has Kähler-type W⁺ at s = −4, the saving density is ≤ −(2−ρ)²(ρ+1). Depletion there is strictly costly. The note's alternative "or field depletion" is therefore closed in such regions. The correct reading is: saving lives where W⁺_ĝ leaves 𝒦. The same set contains every s* > 0 pocket (§4).
2. Near-minimizers with P/8π²k ≤ c satisfy ∫dist(W⁺_ĝ, 𝒦) ≥ 8π²(1−c)k/C₀. If ĝ is ε-close in curvature to KE outside a set of volume v, then 8π²(1−c)k ≤ C₀εV + 0.85·v. Here 0.85 is the maximum over ρ of ρ⁴/24 + (2−ρ)(ρ−1)(3ρ+2)/3, attained near ρ ≈ 1.72, and V ≥ 2π²A by LeBrun's minimal-model scalar estimate.

**What remains unresolved.** The term C₀εV is linear in the Weyl deviation and extensive. At ρ = 2, n = ω̂ the bound reads f ≤ 4E′(ω̂,ω̂) − 4|E′|², so first-order Weyl deletion along the Kähler direction is genuinely available locally.

Converting this into a per-class statement for KE-close bulk needs input that makes ∫E′(ω̂,ω̂) second order. On X_Γ this happens through Bach-flatness: ∫|W⁺|² is stationary at Einstein metrics. On M, the gluing regions break this stationarity. Pricing that mechanism, rather than the bulk monopole selection, is the substantive missing step for the near-KE part of near-minimizers.