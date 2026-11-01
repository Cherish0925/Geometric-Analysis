# TTCS Independent Branch Record

```json
{
  "step_id": 76,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step75_Q4_half_twistor_torsion_and_zero_index.md",
    "Sessions/S1003A02/workspace/notes/step76_Q4_chern_weil_density_and_prolongation.md",
    "Sessions/S1003A02/workspace/scripts/step75_torsion_symbol_checks.py",
    "Sessions/S1003A02/workspace/data/step75_torsion_symbol_checks.json",
    "Sessions/S1003A02/workspace/scripts/step76_cw_density_on_pair.py",
    "Sessions/S1003A02/workspace/data/step76_cw_density_on_pair.json",
    "Sessions/S1003A01/workspace/notes/step59_chiral_completion_and_zero_charge.md",
    "Knowledge/objects/papers/Local-rigidity-of-certain-classes-of-almost-Kahler-4-manifolds--c0d51aa8ffb7--68f3db154d35/object.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Verify, as a careful differential geometer, the almost-Kaehler torsion results in the Step-75 note and Section 1 of the Step-76 note, using AAD's conventions (the two Knowledge papers) and A01's Step-59 data. Context: closed negative Goldberg problem (does a closed almost-Kaehler Einstein 4-manifold with s<0 have to be Kaehler?). Check concretely: (A) eq (75.2) d_b alpha = -R(J phi + i phi) for alpha=a+iJa from AAD (26); the identification of the Lambda^- part of d_b alpha with the J-anti-invariant Ricci tensor Ric'' (Theorem 75.H(a)); injectivity of the principal symbol of the primitive (1,1) projection P (75.H(b)); the five-piece U(2) splitting of nabla^b alpha and which pieces correspond to W_2^+ (eta) and W_3^+ (75.H(c)), including whether the extra |a|^2 term really appears where claimed; the sharp refined Kato constant k^2=3/4 (75.H(d)). (B) Proposition 75.I: det_R Df = |c|^4 - |c|^2(||S||^2-||A||^2) + |det B|^2 for f = cz + B zbar with B=S+A, and the stated sign consequences; whether index is correctly the sign of this determinant with orientation conventions of E. (C) Section 3 of the Step-75 note: is the 'decay principle' argument logically valid as stated, and is the claim that weighted Bochner arguments are index-blind correct? (D) Step-76 Section 1: the claim that the Lambda^- (su(2)) part of the canonical Hermitian connection curvature equals the Levi-Civita one because [m,m] lies in R Omega; formula (76.1) db = R(Omega) - a^Ja and its sign; formula (76.2) c2(E) = (9/4) p1(Lambda^+) - (1/4) p1(Lambda^-); the density (76.3) 4pi^2 c2(E) = 42 - 27q/8 + 9|eta|^2/4 + |W^-|^2/2 at s=-12, and the transgression identity (76.4) relating it to the AAD balance |eta|^2+2|W3|^2+3q^2/16-3q/2. The script/JSON confirm (76.4) identically on A01's pair, given the stated normalizations; judge whether that confirmation actually pins down the sign in (76.1) or whether an alternative sign could also be consistent. State corrections with exact replacement formulas. Do not invent literature.

## Output

# Verification memo: Steps 75–76 (almost-Kähler torsion, zero index, Chern–Weil density)

Conventions throughout are those of AAD: ∇Ω = a⊗φ − Ja⊗Jφ, ∇φ = −a⊗Ω + b⊗Jφ, R_{X,Y} = ∇_{[X,Y]} − [∇_X,∇_Y], and the form norm with |Ω|² = 2. Equation numbers "AAD-LR" and "AAD-LM" refer to the two Knowledge papers.

**Summary of outcomes**

- **Correct as stated:** (75.2); 75.H(a); 75.H(b); the Kato constant 3/4; the determinant formula in 75.I; the c₂(E) decomposition (76.2); the density (76.3); the transgression identity (76.4); the conclusion that the Λ⁻ connection is unchanged.
- **Corrections needed:**
  - 75.H(c) has four pieces, not five, and the |a|² term sits in the Nijenhuis component, not with W₃⁺.
  - The strictness condition for index −1 in 75.I.
  - The orientation sentence in Step 76 §2.
  - The overall sign of (76.1).
  - The wording of §3(ii).
  - The precise hypotheses of §3(iii).
- **On the sign question:** the script cannot fix the sign in (76.1). The relative sign is fixed by AAD (24) and independently by Blair's integral formula. The overall sign is irrelevant to every c₂ quantity.

---

## A. The half-twistor equation (Theorem 75.H)

### (75.2) is correct

Put α = a + iJa. Expand d_bα = dα − ib∧α, then substitute da = −R(Jφ) + Ja∧b and d(Ja) = −R(φ) − a∧b from AAD (23)/(12):

- The real part is −R(Jφ) + Ja∧b + b∧Ja = −R(Jφ).
- The imaginary part is −R(φ) − a∧b − b∧a = −R(φ).

Hence d_bα = −R(Jφ + iφ).

Gauge covariance also checks out:

- Using J(Ja) = −a, one gets a′ + iJa′ = e^{iθ}α.
- Under b′ = b + dθ, d_{b′}α′ = e^{iθ}d_bα.
- Jφ′ + iφ′ = e^{iθ}(Jφ + iφ).

Type: Jα = −iα in AAD's action (Jα)(X) = −α(JX). So α satisfies α(JX) = iα(X), i.e. it is of standard type (1,0). The script and A01 instead write α = f₁dz̄₁ + f₂dz̄₂. These are complex conjugate conventions; both are internally consistent (see B for why orientation is unaffected).

### 75.H(a) is correct

Ric₀~ maps Λ⁺ → Λ⁻ and is the only part of R doing so. Under U(2), Λ⁺⊗Λ⁻ = (Ω⊗Λ⁻) ⊕ ([[Λ^{0,2}]]⊗Λ⁻) corresponds to (Ric₀′, Ric″), with real dimensions 3 and 6.

Ric″~(Jφ + iφ) = Ric″~(Jφ) + i·Ric″~(φ) is a complex Λ⁻-valued object with 6 real components, and it recovers Ric″ completely. Therefore (d_bα)⁻ = −Ric″~(Jφ + iφ), and Ric″ = 0 ⇔ 𝒫α = 0, since Λ⁻ = Λ^{1,1}_0.

### 75.H(b) is correct

The symbol is ξ ↦ (ξ^{0,1}∧α)_0. The form ξ^{0,1}∧α is decomposable, of rank 2, and nonzero, because ξ^{0,1} and α are of different types. Ω has rank 4, so ξ^{0,1}∧α can never be a multiple of Ω; hence its primitive part never vanishes.

### 75.H(c) needs two corrections

**(i) Piece count.** For the canonical Hermitian connection, Λ¹⊗Λ^{1,0} = (Λ^{0,1}⊗Λ^{1,0}) ⊕ (Λ^{1,0}⊗Λ^{1,0}) = CΩ ⊕ Λ^{1,1}_0 ⊕ Λ^{2,0} ⊕ S^{2,0}, of complex ranks 1 + 3 + 1 + 3 = 8. That is **four** irreducible pieces, not five.

**(ii) Location of the |a|² term.** Decompose d_bα by type, with α of type (1,0):

| Component of d_bα | Content |
|---|---|
| (1,1) | ∂̄-part of the gradient, plus b^{0,1}∧α |
| (2,0) | antisymmetric part of the (1,0)-derivative, plus b^{1,0}∧α |
| (0,2) | the purely algebraic Nijenhuis term N(α) = ¼α(N), quadratic in a, containing no derivatives |

The (0,2) row has no b-term, and it does not come from ∇̄α. For an almost-Kähler structure the first canonical connection is the Chern connection, whose torsion is of type (0,2). So alt(∇̄α) and dα differ only in the (0,2) component.

The right-hand side splits into three lines:

- **Ω-line:** W₂⁺ (that is, η).
- **The line of Jφ + iφ itself:** the term ((s − κ)/12)(Jφ + iφ) = −½|a|²(Jφ + iφ), using κ − s = 6|a|² from AAD (10).
- **The conjugate line:** W₃⁺(Jφ + iφ) = (−λ + iμ)(Jφ − iφ). This follows from W₃⁺φ = λφ + μJφ and W₃⁺Jφ = μφ − λJφ.

So the |a|² term and W₃⁺ lie in *complementary* type lines. They can never form one rank-one piece, as 75.H(c) asserts.

Exactly one of the two lines is Λ^{0,2}:

- **If Jφ + iφ ∈ Λ^{0,2}:** the (0,2) component reads N(α) = ½|a|²(Jφ + iφ), an algebraic tautology. The (2,0) piece is then exactly ∂_bα = −W₃⁺(Jφ + iφ), with no quadratic correction.
- **If instead Jφ + iφ ∈ Λ^{2,0}:** then W₃⁺ would equal an algebraic quadratic expression in the 1-jet. That contradicts AAD-LR (13), where λ contains ⟨da, Jφ⟩. It is also incompatible with the 3-symmetric space, which has W₃⁺ = 0, |a| a nonzero constant, and N(α) ≠ 0.

The first alternative is therefore the consistent one.

Replacement text for 75.H(c):

> ∇^bα ∈ Λ¹⊗Λ^{1,0}⊗𝓛 splits into four U(2)-pieces: Λ^{1,1}_0 (rank 3) = 𝒫α ↔ Ric″; CΩ (rank 1) ↔ W₂⁺; Λ^{2,0} (rank 1), with ∂_bα = −W₃⁺(Jφ + iφ) exactly; and S^{2,0} (rank 3), free at first order. The term −½|a|²(Jφ + iφ) is matched by the Nijenhuis component N(α) = (d_bα)^{0,2}, which is algebraic in the torsion.

AAD's real formula λ = −½(|a|² − ⟨da, Jφ⟩ + φ(a,b)) is consistent with this. The real projection ⟨da, Jφ⟩ mixes the (2,0) and (0,2) components, and the |a|² there is the N-part.

A direct pointwise computation of N(α) in AAD's conventions would confirm the type assignment. It is short and worth recording.

### 75.H(d) is correct

The kernel is K = CΩ ⊕ Λ^{2,0} ⊕ S^{2,0}, of complex dimension 5. For a real unit ξ and a unit v:

- The part ξ^{1,0}⊗v has norm² ½ and lies entirely in K.
- The part ξ^{0,1}⊗v is a rank-one element of End(C²) with Frobenius norm² ½. Its trace projection has norm² |⟨u, v̄⟩|²/2 ≤ ¼ by Cauchy–Schwarz.

So k² = ¾, attained, and γ = 2/3 is where (1 − (2 − γ)k²) = 0.

Two requirements, both met:

- The Kato argument needs a metric connection; ∇̄ ⊗ (−ib) is unitary.
- K must be defined for ∇̄α rather than ∇α. This is exactly right by the torsion-type remark in (ii).

The script's docstring item 2 (the singular-value formula) is not correct in general, since the eigenvalues of BB̄ are not the squared singular values unless B is symmetric. The code tests the correct determinant formula, so the JSON is unaffected.

---

## B. Proposition 75.I

### The determinant formula is correct

In (z, z̄) coordinates the real Jacobian determinant equals

det [[cI, B], [B̄, c̄I]] = det(|c|²I − BB̄),

because the lower blocks commute. Then:

- det(tI − BB̄) = det(tI − B̄B).
- tr(BB̄) = Σ B_ij B̄_ji = ‖S‖² − ‖A‖², because the symmetric–antisymmetric cross pairings vanish.
- det(BB̄) = |det B|².

### One strictness correction in the sign consequences

Write t = |c|² and σ = ‖S‖² − ‖A‖². The positive cases are correct whenever the zero is nondegenerate: t = 0, or σ ≤ 0. In particular S = 0 and ‖S‖ ≤ ‖A‖ give index +1.

Index −1 requires t > 0 and t² − σt + |det B|² < 0. This needs σ > 2|det B| **strictly**, together with t strictly between the two roots (σ ± √(σ² − 4|det B|²))/2. At σ = 2|det B| the quadratic is a perfect square, and the zero at t = σ/2 is degenerate.

Replace "≥" by ">" and add the root interval.

A01's example (c = 1, B = diag(2, 0)) gives 1 − 4 + 0 = −3, so index −1, as stated.

### Orientation: the conclusion holds, one sentence is wrong

The Euler class giving 5χ + 6τ uses the complex orientation of E. The map T ↦ a (gauge fixed) is a real isomorphism [[E]] → T*M. The phase rotation on E corresponds to ∓J on a, and a ↦ α is J-antilinear. All identifications are therefore C-linear or C-antilinear. In complex rank 2 both preserve orientation, since conjugation on C² has real determinant +1.

Hence the index equals sign det(∂a_k/∂x^m) in Ω²-oriented coordinates on source and target, and the script's (0,1)-convention gives the same sign.

Step 76 §2 says "every complex structure on E induces the same real orientation." That is false in general: a rank-4 real bundle carries complex structures of both orientations. Replace with:

> J and −J (conjugate complex structures) induce the same orientation in complex rank 2, and every identification used here is C-linear or C-antilinear.

The source coordinates must also be J-holomorphic at p, which A01's normal form provides.

---

## C. Step 75 §3

### (i) The inequality is correct

Δf^γ = γf^{γ−2}[|∇α|² − (2 − γ)|df|² − Re⟨∇*∇α, α⟩] for 0 < γ < 2. The remark about the s/4 term from the twisted Lichnerowicz formula is qualitatively right:

- The SD part of the twisting curvature acts trivially on S⁻.
- The ASD part is −(a∧Ja)⁻, quadratic in the torsion.

This is a statement about this particular inequality, not a theorem excluding all Kato-type arguments. The [P] label should be read that way.

### (ii) The conclusion stands, but the stated mechanism is wrong

Δ_x|Lx|⁻² is not a pure Dirac mass when L is not conformal; it has a principal-value part. Its δ-coefficient is the sphere flux

−2∮ xᵀLᵀLx / (|Lx|⁴|x|) dS,

which depends on LᵀL, not only on |det L|.

The correct invariant statement is:

> Any expression built from |α| depends on Df(p) only through Df(p)ᵀDf(p). That is invariant under Df ↦ R∘Df for an orientation-reversing isometry R of E_p, so sign det Df is invisible to it.

This invariance concerns the zero-localized terms only. R is not a symmetry of the AKE system, so this does not by itself exclude global arguments that couple |α|-weights to other terms.

### (iii) The decay principle is valid, provided its inputs are stated exactly

The logic is sound if every step of a putative closed proof is one of the following:

1. **A universal local divergence identity** div V = Ψ. Here V is a polynomial in jets of (g, Ω) and curvature, smooth and *gauge-independent*, so that it is globally defined on the disk bundle. Its flux through the level sets must tend to 0 at the ACH end. Chern–Simons-type V built from b need not be global on the pair.
2. **A pointwise inequality** valid for all AKE germs.

Then the strict pair satisfies the same conclusion. For Φ ≥ 0 this means Φ ≡ 0 on the pair.

Two refinements:

- **A cheaper test than the flux check.** For a given Φ ≥ 0, evaluating Φ pointwise on A01's exact data decides it: if Φ ≢ 0 on the pair, the flux of that V cannot decay.
- **Sign-indefinite integrands, such as the AAD balance.** The pair shows only that such an identity cannot be the sole input.

The remark that the Euler-class "charge escapes to infinity" needs restating. On the pair both the Levi-Civita and canonical c₂(E) densities tend to 42/(4π²) while the volume is infinite, so their integrals diverge. Only the transgression (difference) forms, and Mathai–Quillen-type forms localized at zeros, have meaningful integrals there.

---

## D. Step 76 §1

### Λ⁻ part: correct, with a sharper reason available

The difference tensor of the first canonical connection, A_X = −½J(∇_XJ), takes values in 𝔪 = [[Λ^{0,2}]] ⊂ Λ⁺. Λ⁺ acts trivially on Λ⁻. So the induced **connections** on Λ⁻ coincide, not merely their curvatures.

The note's formula R_𝔲 = R̄ + (A∧A)_𝔲 omits d^{∇̄}A. That term is harmless because it is 𝔪-valued, and [𝔪, 𝔪] = RΩ.

### (76.1): overall sign error, relative sign correct

AAD-LR (16) and AAD-LM (24)–(25) give

db = a∧Ja − R(Ω),  with γ_J = −db = R(Ω) − a∧Ja,  [γ_J/2π] = c₁(J).

Hence ⟨db, Ω⟩ = |a|² − s*/2 = −(s + s*)/4, using ⟨R(Ω), Ω⟩ = (s + 2κ)/6 = s*/2 and |a|² = q/4.

Replacement:

> −db = γ_J = R(Ω) − a∧Ja,  ⟨γ_J, Ω⟩ = (s + s*)/4.

Every c₂ quantity is quadratic in db, so (76.2)–(76.4) are unaffected.

### Does the pair confirmation fix the sign? No

The script's check "LC − D − (9/4)·balance = 0" is an algebraic identity in (q, η, W₃) once two substitutions are made: κ = s + 3q/2 and |W⁺|² = κ²/24 + |η|² + |W₃⁺|². It carries no geometric information about (76.1), because the formula D already contains the chosen sign.

To see what the alternative would do, take db_alt = R(Ω) + a∧Ja:

- 4π²c₁²_alt = 18 − 9q/2 + q²/4 + |η|².
- LC − canonical would become (9/4)(|η|² + 2|W₃⁺|² − q²/16 + 3q/2).

Its pair integral, per unit orbit volume, is 32 + 32 − 32/3 + 96 = 448/3 ≠ 0. This discriminates the two signs only if one already knows that the correct transgression flux decays, which is circular.

What genuinely fixes the relative sign:

1. **AAD (24) directly.**
2. **Blair's formula**, quoted in the AAD-LM introduction: ∫(s + ¼|∇J|²) = 4πc₁·[Ω]. With |∇J|² = 2|∇Ω|² = 2q (tensor norm = 2 × AAD form norm), this gives ∫⟨γ_J, Ω⟩ = ½∫(s + q/2) = ∫(s + s*)/4. The alternative sign gives ∫(s/2 + 3q/4) instead.
3. **A pointwise test on the pair:** only R(Ω) − a∧Ja is closed. At the bolt the two signs give ⟨·, Ω⟩ = −10/3 versus 2, using q = 32/3.

### (76.2) is correct, at the level of forms

- The roots of E are 2x₁ + x₂ and x₁ + 2x₂, so c₂(E) = c₂ + 2c₁².
- e = ¼(p₁(Λ⁺) − p₁(Λ⁻)) holds for any SO(4) connection.
- c₁² = p₁(Λ⁺) holds as forms, because ∇̄ preserves RΩ ⊕ K⁻¹.

### (76.3) is correct

At s = −12:

- **Self-dual part of γ_J:** (s/12 + κ/6 − q/8)Ω + η = (s/4 + q/8)Ω + η.
- **Anti-self-dual part:** (a∧Ja)⁻ has norm² q²/32.

So 4π²c₁² = 2(−3 + q/8)² + |η|² − q²/32 = 18 − 3q/2 + |η|². Kähler–Einstein check: 2·6 + 6 = 18.

For the Λ⁻ term, −¼·4π²p₁(Λ⁻) = ½|W⁻|² + 3/2. Assembling:

(9/4)(18 − 3q/2 + |η|²) + ½|W⁻|² + 3/2 = 42 − 27q/8 + (9/4)|η|² + ½|W⁻|².

The norm conventions are consistent: |W₂⁺|²_HS = |Ψ|²/4 = |η|² with η = −Ψ/2.

### (76.4) is correct

The difference LC − canonical equals

(9/4)[κ²/12 + |η|² + 2|W₃⁺|² − 12 + 3q/2] = (9/4)(|η|² + 2|W₃⁺|² + 3q²/16 − 3q/2).

The pair values follow: density 6 at the bolt (q = 32/3) and 42 at the ACH end. Positivity is immediate whenever q ≤ 112/9, and the maximum q on the pair is 32/3.