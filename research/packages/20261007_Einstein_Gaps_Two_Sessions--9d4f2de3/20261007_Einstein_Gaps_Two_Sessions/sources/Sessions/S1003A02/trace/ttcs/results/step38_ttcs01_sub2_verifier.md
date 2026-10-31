# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/paired_cross_field_algebra.py",
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Knowledge/objects/papers/Algebraic-surfaces-and-Seiberg-Witten-invariants--d573804ced34--70869ee25818/object.md",
    "Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md"
  ]
}
```

## Task

Check the mathematical correctness and normalization of the proposed paired-monopole identities and the Kähler lower theorem in the session. In particular: (i) for a Kähler metric on M=X#k CPbar^2 with X minimal general type, derive explicitly whether C_+=(2pi^2)^-1∫|W+|^2+(96pi^2)^-1∫s^2 equals ∫s^2/(32pi^2), and prove or correct C_+>=A=c1^2(X) using the Hodge index with canonical class and exceptional areas; determine what additional assumptions are needed for inf_Kähler P=8pi^2 k and nonattainment; (ii) verify the cross-line bundle classes for u=<Phi_e',Phi_e> and w=Phi_e wedge Phi_e' when the determinant classes differ by flipping exceptional signs, including factor-of-two conventions and whether c1(u)=E_i or 2E_i; (iii) verify the amplitude identity and lower inequality P>=8pi^2 Q-4 E∫(2-rho)_+ under the stated s=-4 normalization. Give exact corrected statements, not procedural advice.

## Output

# Verification memo: paired-monopole identities and the Kähler lower theorem

## Summary of results

- **(i) Kähler theorem.** C₊ = ∫s²/(32π²) holds exactly for every Kähler metric. The bound C₊ ≥ A is correct but weak: for k ≥ 1 it is strict, with an explicit first-order excess. That excess matches the slope of Theorem F (the Burns-gluing law in the package) in the Kähler-aligned direction exactly.
- **(ii) Cross-line bundles.** The bundle carrying u has class ε_iE_i, not 2E_i. The bundle carrying w has the large class (a_ε + a_ε′)/2. The pointwise cost |f⁺ − f′⁺|² is carried by w.
- **(iii) Amplitude identity.** I re-derived the identity independently; it is correct. The lower inequality is correct, and its constant 4 is optimal. The inequality uses only the kinetic term, not the rest of the cost 𝒜.

Conventions: curvature and Weyl norms are Hilbert–Schmidt norms on Λ², as in LeBrun's block form; Ricci norms are tensor norms. With these, Gauss–Bonnet plus signature give, for every metric,

P/(8π²) = C₊ − (2χ+3τ)(M), where 2χ+3τ = A − k − 4ℓ = A − Q.

The coefficient (2π²)⁻¹ on ∫|W⁺|² is tied to the Hilbert–Schmidt norm. With tensor norms (|W|²_tensor = 4|W|²_HS) it becomes (8π²)⁻¹.

---

## (i) Kähler metrics on M = X # k CP̄²

### 1. C₊ for a Kähler metric

The Kähler metric must induce the given orientation. For any Kähler metric, constant s or not, W⁺ has eigenvalues s/6 on ω and −s/12, −s/12 on ω^⊥. Hence pointwise |W⁺|² = s²/36 + 2s²/144 = s²/24, and

C₊ = ∫s² (1/48 + 1/96)/π² = ∫s²/(32π²).

This is exact. Equivalently, P = ∫s²/4 − 8π²c₁²(M) = ∫s²/4 − 8π²(A−k). The same formula follows from ∫ρ∧ρ = ∫s²/8 − P/2 for the Ricci form ρ.

If the complex orientation were the reverse of the given one, W⁺ and W⁻ would swap and this computation would not apply.

### 2. Hodge-index bound, corrected to a strict exact form

Let Ω = [ω]. Let K denote the pullback of K_X, which is nef with K² = A. Let e_i = E_i·Ω = area(E_i) > 0. Then

- c₁(M)·Ω = −(K·Ω + Σe_i),
- ∫s dμ = 4π c₁·Ω,
- V = Ω²/2.

Splitting ∫s² = (∫s)²/V + ∫(s − s̄)² gives the exact identity

  **P/(8π²) − k = [(K·Ω + Σe_i)²/Ω² − A] + (1/32π²)∫(s − s̄)².**

K and Ω lie in the closure of the same component of the positive cone, so the reverse Cauchy–Schwarz (Hodge index) inequality gives K·Ω ≥ √(AΩ²). Therefore

  P/(8π²) − k ≥ [(K·Ω)²/Ω² − A] + 2√A·Σe_i/√(Ω²) + (Σe_i)²/Ω² + (1/32π²)∫(s − s̄)².

Every bracket is ≥ 0, and the second term is > 0 whenever k ≥ 1. Thus C₊ ≥ A is true, and for k ≥ 1 it is strict:

  C₊ ≥ A + 2√A·Σe_i/√(Ω²) > A.

No hypothesis on b₊ and no Seiberg–Witten input is used: only ∫s = 4πc₁·Ω, Hodge index, and positivity of exceptional areas.

### 3. First-order consistency with Theorem F

Take KE bulk with s = −4. Then V = 2π²A, so √(Ω²) = 2π√A. A Burns curve of area πx₀ gives the bound

  P/(8π²) ≥ k + x₀ + O(x₀²).

Theorem F predicts 1 − x₀𝐑⁺(ω̂,ω̂) per blow-up, with 𝐑⁺(ω̂,ω̂) = s/6 + s/12 = s/4 = −1. That is 1 + x₀, the same slope.

So the Hodge-index bound is first-order sharp exactly in the Kähler-aligned direction ζ = ω̂. The free directions ker 𝐑⁺ = ω^⊥ and the certified subthreshold cells are therefore necessarily non-Kähler. This identifies, at the level of an exact identity, the Weyl-alignment mechanism exploited by the subthreshold cells.

### 4. Comparison with arbitrary metrics

For arbitrary metrics, LeBrun's estimate ∫(s − √6|W⁺|)² ≥ 72π²A can be combined with the pointwise inequality (s − √6|W⁺|)² ≤ (9/8)(s² + 48|W⁺|²), obtained from Young's inequality with weight 1/8. This gives

C₊ ≥ 2A/3, hence P ≥ 8π²(k − A/3).

This is exactly the package's classical lower interval. So the Kähler hypothesis raises the bound on C₊ from 2A/3 to A, and the gap A/3 is the room available to non-Kähler competitors.

### 5. Hypotheses needed for inf_Kähler P = 8π²k and nonattainment

**Lower bound and nonattainment.** P > 8π²k for every Kähler metric. This needs:

- k ≥ 1;
- the complex orientation equals the given one;
- the minimal model of (M, J) is of general type, with K₀² = A, blown up exactly k times.

For the standard blow-up structure this holds by construction. For an arbitrary complex structure J on M, Friedman–Morgan supply it:
- Cor. 1.4: the plurigenera are smooth invariants, so the surface is of general type;
- Thm 1.1: the number of blow-ups agrees (ℓ = m), so K₀′² = A.

In the case p_g > 0 these rest on the Witten / Kronheimer–Mrowka arguments cited there. Nonattainment within the Kähler class then follows immediately, because Σe_i > 0.

For k = 0 the bound is P ≥ 0, with equality iff the metric is KE. That requires K_X ample, so the infimum is not attained when K_X is nef but not ample.

**Upper bound.** One needs Kähler metrics with all three excess terms → 0: Ω_j tends projectively to K, Σe_i/√(Ω_j²) → 0, and the L²-oscillation of s tends to 0. Equivalently, ∫s² → 32π²A.

- *K_X ample.* Glue scaled Burns potentials |z|² + ε² log|z|² into the KE potential |z|² + O(|z|⁴) on an annulus of radius r. The metric error is O(ε²/r² + r²) and the curvature error O(ε²/r⁴ + 1) on volume r⁴. Hence the added ∫s² is O(ε⁴/r⁴ + r⁴), which tends to 0 for r = ε^{1/2}. The core contributes O(r⁴).
- *K_X nef, not ample.* Additionally glue Kronheimer's Kähler ALE metrics into the orbifold KE metric at the ADE points. This must be done at the level of Kähler potentials. LeBrun's 2001 recovery metrics are not stated to be Kähler in the supplied material, so they do not supply this.

These gluings are standard but not written in the supplied files. With them, inf_Kähler P = 8π²k for every minimal general-type X, and the infimum is never attained for k ≥ 1.

### 6. Separation from the full infimum

The certified cell with P/(8π²) ≈ 0.99585 has an exact CH outer collar. It transplants exactly into any compact ball quotient X containing an embedded CH ball of the collar's radius; residual finiteness provides such X on finite covers. Then

  inf_g P ≤ 0.9959·8π²k < 8π²k = inf_Kähler P.

The Kähler infimum is strictly above the unrestricted infimum, for exactly the reason in §3.

---

## (ii) Classes of the cross fields

**Setup.** Write V_ε = S⁺ ⊗ L_ε^{1/2} with c₁(L_ε) = a_ε = c + Σε_iE_i. Let F be the set of flipped indices, so ε′_i = −ε_i for i ∈ F. Then V_ε′ = V_ε ⊗ Ξ with

c₁(Ξ) = (a_ε′ − a_ε)/2 = −Σ_{i∈F} ε_iE_i.

This class is integral, consistent with Friedman–Morgan's difference δ(ξ₁, ξ₂) = (c₁(L₁) − c₁(L₂))/2. If H²(X; ℤ) has 2-torsion, c₁(Ξ) is determined only up to torsion; real classes are unaffected.

**The field u = ⟨Φ_ε′, Φ_ε⟩.** The inner product is antilinear in the first slot, as in the script (psi.H·phi). u is a section of L_ε^{1/2} ⊗ L_ε′^{−1/2}, with

  **c₁ = (a_ε − a_ε′)/2 = Σ_{i∈F} ε_iE_i.**

For a single flip this is ε_iE_i, **not 2E_i**. The class 2ε_iE_i belongs to Hom(L_ε′, L_ε), the difference of determinant lines, or equivalently to u².

The induced connection is (A_ε − A_ε′)/2, with −i·curvature (f_ε − f_ε′)/2. Averaging gives

E_ε[ε_i(f_ε − f_{ε^{(i)}})/2] = f_{{i}},

so the Walsh singleton forms are averaged curvatures of the u-bundles. This is consistent with [f_{{i}}/2π] = E_i and with Chern–Weil ‖f_{{i}}⁻‖² − ‖f_{{i}}⁺‖² = 4π².

**The field w = Φ_ε ∧ Φ_ε′.** Since Λ²S⁺ is trivial, w is a section of (L_ε ⊗ L_ε′)^{1/2}, with

  **c₁ = (a_ε + a_ε′)/2 = c + Σ_{j∉F} ε_jE_j,**  of square A − k + |F|.

Its double a_ε + a_ε′ is not characteristic when F ≠ ∅. This is the same parity fact behind the paper's remark on f_∅.

**Conjugate partners.** If the partner is taken from the conjugate family (−a_ε′, solution Φ̄_ε′), the two classes exchange roles. As a check, the full conjugate partner gives w-class 0 (Φ ∧ jΦ = |Φ|²) and u-class a_ε.

**Geometric consequence.** Both bundles are nontrivial, so u and w must each vanish somewhere. A generic zero set of u is a surface representing PD(Σ_{F}ε_iE_i), of self-intersection −|F|. On that surface the two Bloch vectors anti-align (n′ = −n), so there

|f⁺ − f′⁺|² = (ρ + ρ′)²/2.

The Fierz relations |u|² + |w|² = ρρ′ and

|f⁺ − f′⁺|² = (ρ − ρ′)²/2 + 2|w|²

hold with f⁺ = (ρ/√2)n. They need the same σ for both solutions, which holds because σ is insensitive to the line-bundle twist.

The pointwise cost is therefore carried by the large-class field w. The exceptional class is localized by the zeros of the small-class field u. A zero surface carries no volume, so it yields no direct lower bound by itself.

---

## (iii) Amplitude identity and the lower inequality

### 1. Normalization check

Take s ≡ −4 and F⁺ = 2iσ(Φ), so f⁺ = ψ/√2 with ψ = 2√2σ(Φ), |ψ| = ρ, and |f⁺|² = ρ²/2.

LeBrun's Weitzenböck formula then reads

0 = ½Δρ + |∇Φ|² − ρ + ρ²/2.

- The maximum principle gives ρ ≤ 2, so (2 − ρ)₊ = 2 − ρ.
- Integration gives K = ½∫ρ(2 − ρ).
- Using ∫ρ² = 8π²p + 2J, the slack identity Σ = 16K + 4∫(ρ−2)² + 8J is this integrated Weitzenböck formula, with no further content.
- J is the L²-norm of (dβ)⁺. It equals ‖f⁺ − (f⁺)_H‖² because (f⁺)_H = h⁺, by Lemma 2.1 of the LeBrun paper.

### 2. Independent derivation of the single-solution remainder

The paper derives the remainder from its D-decomposition, which is not supplied. I derived it directly from four ingredients:

1. **Weitzenböck for ψ ∈ Λ⁺:**
 ∫(|dψ|² + |d*ψ|²) = ∫|∇ψ|² − 2∫W⁺(ψ,ψ) − (4/3)∫ρ².
2. **ρ-weighted spinor Weitzenböck:**
 ∫ρ|∇Φ|² = ∫(ρ² − ρ³/2) − ½‖dρ‖².
3. **Kinetic split** (computed in a frame with Φ = (√ρ, 0)):
 |∇ψ|² = 4ρ|∇Φ|² − 4|Im ζ|², and |ζ|² = |dρ|²/4 + |Im ζ|².
4. **Maxwell/current identity:** the Clifford identity Σ_j (e_j ∧ X)·∇_jΦ = −X·DΦ − ∇_XΦ shows that on Dirac-harmonic Φ, d*σ(Φ) is a fixed multiple of Im ζ. A Kähler vortex calibrates the constant: there b = 0 and |Im ζ| = |dρ|/2. The result is
 |d*f|² = 2|d*ψ|² = 4|Im ζ|².

Two further pointwise facts enter: |W₀|² = ρ⁴/24 and ⟨W⁺, W₀⟩ = −W⁺(ψ,ψ)/4.

Substituting, the gradient terms cancel (+2‖dρ‖² − 2‖dρ‖²), and the current terms cancel (8 − 4 − 4 = 0). The polynomial part collapses exactly:

(14/3)ρ² − 2ρ³ + ρ⁴/6 − 4ρ + b(ρ)(ρ−2)² = 4/3 − ρ².

This gives

4W₊ + 4V/3 − ∫ρ² = 8‖ζ‖² + 4‖W⁺ − W₀‖² + ∫b(ρ)(ρ−2)² − 4K.

The paper's b = 2C − 1 = (−t² + 8t + 2)/6 agrees, as does the substitution 2D/9 − Σ/4 − 2J. A KE test (ρ = 2, W⁺ = W₀) gives 0 = 0.

The single-cost formula P = 32π²ℓ + 2‖f_ε⁻‖² + 4W₊ + 4V/3 − ∫ρ² is correct, using P = 4W₊ + 4V/3 − 8π²(A − Q) and a_ε² = A − k. The determinant part is consistent: E_ε p_ε ≥ (c⁺)² ≥ A by convexity on H⁺_g, matching 2‖f_∅⁻‖² + 2Σ‖f_I⁺‖² ≥ 0.

### 3. Exact corrected statement

This requires an actual solution for every class a_ε at the same metric g. That supply needs b₊(M) ≥ 2. For p_g(X) = 0 it holds only while the period point stays in Friedman–Morgan's chamber 𝒞₀.

Under that supply, with s ≡ −4:

  P − 8π²Q + E_ε∫m(ρ_ε) = 2‖f_∅⁻‖² + E_{ε,ε′}∫[(ρ_ε − ρ_ε′)²/2 + 2|w_{εε′}|²] + E_ε[8‖ζ_ε‖² + 4‖W⁺ − W_{0,ε}‖²] ≥ 0,

where

  m(ρ) = 2ρ(2−ρ) − b(ρ)(2−ρ)² = (2−ρ)·q(ρ),  q(ρ) = (−ρ³ + 10ρ² − 2ρ − 4)/6.

The Walsh variance step uses E|F_ε − F_ε′|² = 2Σ_{I≠∅}|F_I|².

Properties of m:
- m < 0 on [0, ρ₀) with ρ₀ ≈ 0.7758, and m ≥ 0 on [ρ₀, 2].
- m(0) = −4/3 and m′(2) = −4.
- q is increasing on (0.10, 2] with q(2) = 4.

### 4. The lower inequality and its constant

From the identity,

  **P ≥ 8π²Q − E_ε∫m₊(ρ_ε) ≥ 8π²Q − 4E_ε∫(2 − ρ_ε).**

The constant 4 is optimal for a bound linear in (2 − ρ), because m ≈ 4(2 − ρ) as ρ → 2.

The weaker form P − 8π²Q ≥ −4E K_ε = −2E∫ρ(2−ρ) already gives the same constant 4. Its only use of 𝒜 is 𝒜 ≥ 0. The b-term, the Weyl term and the ζ-term improve the bound only where ρ < ρ₀; there m < 0, so that region contributes no deficit at all.

Thus the substance lies in the exact identity. The inequality then says the following: a saving 8π²Q − P = 8π²δQ forces an averaged amplitude-deficit volume

E∫(2 − ρ_ε) ≥ 2π²δQ,

which is a fraction of order δh of the volume V ≈ 2π²A. This is compatible with fixed-size subthreshold cells, which deplete ρ on volume O(1) each. It does not decide the open question. That question would be closed by showing E∫m₊(ρ_ε) ≤ 𝒜 + o(Q) on selected near-minimizers.