# TTCS Independent Branch Record

```json
{
  "step_id": 50,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step50_wminus_completed_square_and_general_KE_construction.md",
    "Sessions/S1003A01/workspace/notes/step49_kernel_log_coefficient_general_background.md",
    "Sessions/S1003A01/workspace/scripts/step50_wminus_compatibility.py",
    "Sessions/S1003A01/workspace/scripts/step50_exact_identity.py",
    "Sessions/S1003A01/workspace/scripts/step50_check_corrector_ric0.py",
    "Sessions/S1003A01/workspace/data/step50/exact_identity.json",
    "Sessions/S1003A01/workspace/data/step50/wminus_compat_A4.json",
    "Sessions/S1003A01/workspace/data/step50/wminus_compat_A2.json",
    "Sessions/S1003A01/workspace/data/step50/natural_corrector.json",
    "Sessions/S1003A01/workspace/data/step50/corrector_check_ric0form.json",
    "Sessions/S1003A01/workspace/scripts/step49_kernel_log_coefficient.py"
  ]
}
```

## Task

Verify the mathematics of the Step-50 note (Sessions/S1003A01/workspace/notes/step50_wminus_completed_square_and_general_KE_construction.md), which claims: (1) Lemma 1.1/Cor 1.2: via pointwise Chern–Gauss–Bonnet, the eps^2 log(1/eps) corner coefficient F of a perpendicular Burns insertion g_bg+eps(k_B+k_0) can be computed from 4|W+|^2+s^2/12 instead of |Ric0|^2 (exact-form terms change only off-diagonal z^a y^b coefficients), so F depends only on Rm_p, and the W^- dependence is a nonnegative minimized square kappa(W^-) >= 0; (2) Theorem 2.1: the explicit corrector k0^W = (3/2)sym(h_W k_B) - (1/4)tr(h_W k_B) delta cancels the first-order W+ and s source for all W^- (exact sympy check for one W^- plus SU(2)_- equivariance/irreducibility); (3) Theorem 3.1: hence on every compact negative KE surface, at every point, P(g_eps)/8pi^2 = 1 - 9 eps^2 log(1/eps) + O(eps^2), with the order-eps bucket ell shown to vanish by an invariance + CH-comparison + Burns P-criticality/flux argument; (4) the Yamabe shortcut E(ĝ) <= 4P(g)/(P(g)+8pi^2 A) and Corollary 4.1. Check especially: the degree counting in Lemma 1.1(c) (are there any W^- ⊗ W^- terms at degree -4 besides |W+_1|^2, s_1^2? any 4-jet terms?); the analyticity/parity claims and whether the transgression G(y,z) is analytic so that diagonal coefficients agree; whether the order-eps bucket ell can be nonzero for a general KE point (is ell truly a U(2)_zeta-invariant LINEAR functional of (Rm_p,k0) only, blending-independent; is the CH comparison with Ch.5 (5.A) legitimate); the representation theory (SU(2)_- fixes zeta and omega; W^- spin 2; Ric0 spin 1); the equivariance argument for general W^-; the sign/convention of the CGB identity; the Yamabe inequality P(ĝ)-P(g)=(S(ĝ)-S(g))/12 and S minimized by the Yamabe metric when Y<0. Identify any gap that could invalidate the theorem and say precisely what extra argument would fill it. Read the scripts and data to see what was actually computed.

## Output

# Verification memo: Step 50 (CGB form, W⁻ completed square, construction on Ric = −6g KE surfaces, Yamabe shortcut)

## Summary

The central mathematics holds:

- The CGB reduction is correct.
- The degree counting in Lemma 1.1(c) is correct. The f-form contains no W⁻⊗W⁻ terms and no jets beyond h₂ at degree −4. The enumeration in (iii) is incomplete, but the omitted terms vanish by the spin argument.
- The identity of Theorem 2.1 is verified exactly, and the equivariance extension to all W⁻ is valid.
- The order-ε bucket argument is sound.
- The Yamabe inequality is correct.

Three textual points need repair:

1. The last sentence of Corollary 2.2 is false as written for corrector classes that do not contain k₀^W.
2. "ℓ = c·s with a universal constant" is the wrong formulation of a correct argument.
3. Lemma 1.1(b) needs one sentence stating why G(y,z) has no log r term.

Theorem 3.1 rests on three Ch.5 inputs that are cited, not re-derived here:

- the symbolic value F_CH(c*) = −18;
- the absence of an O(ε) term for CH (5.A);
- the fact that the Ch.5 neck has asymptotic data exactly (h_CH, k₀^{c*}) up to decaying and degree-2 terms.

No gap was found that would invalidate the theorem, given those inputs.

---

## 1. CGB identity, exactness, and analyticity of the transgression

**Convention.** With |W|² equal to the Frobenius norm of the operator on Λ² (entries W_abcd with a<b, c<d, as in the script's `M` matrix), the standard formulas are 8π²χ = ∫(|W|² − |Ric°|²/2 + s²/24) and 12π²τ = ∫(|W⁺|² − |W⁻|²). Adding them gives

8π²(2χ+3τ) = ∫(4|W⁺|² + s²/12 − |Ric°|²),

so |Ric°|² = 4|W⁺|² + s²/12 − 16π²e − 24π²p. The CP² check (∫|W⁺|² = 12π², τ = 1, W⁻ = 0) fixes the normalization. The sign and coefficients are correct.

**A global form that sharpens §3.** Integrating over the closed manifold gives

P(g_ε) − P(g_bg) = ∫f(g_ε) − ∫f(g_bg) + 8π²·[−(2Δχ + 3Δτ)],

with Δχ = 1 and Δτ = −1 for #CP̄². Hence

P(g_ε)/8π² = 1 + (∫f(g_ε) − ∫f(g_bg))/8π²,

and the integrand is supported in B_{2T}. The leading "1" is then topological, which makes the core bookkeeping of (B) more transparent.

**Exactness.** e and p are Chern–Weil forms. Their difference between g_ε and g_bg is dT, where T is a local transgression built from the connection difference A = Φ*∇_{g_ε} − ∇_{g_bg}. Here Φ is an analytic isometry such as (g_bg⁻¹g_ε)^{1/2}, needed for the Euler form, and T also involves the curvatures.

**Why diagonal coefficients agree.** The note asserts that G(y,z) = ∫_{S_r}T is analytic, but does not justify it. The required argument is this:

- A carries one derivative of g and the curvature carries two.
- With g = G(ω; r, z) analytic in (r,z), we have r·A and r²·Rm analytic in (ω; r, z). The same homogeneity argument gives r⁴|Ric°|² analytic for ψ.
- So r³·T|_{S_r} is analytic in (r,z), and G has no log r term.
- The pair (ω,r) ↦ (−ω,−r) makes G even, so G = G(y,z).
- Then r∂_r = 2y∂_y − 2z∂_z annihilates z²y².

Without the no-log statement, a diagonal coefficient in r∂_rG would be possible: r∂_r log r = 1. This sentence should be added to Lemma 1.1(a).

**Background subtraction.** f(g_bg) is ε-independent, so it touches only z⁰ coefficients. Subtracting it does not affect F.

**Numerical confirmation is stronger than the note states.** `wminus_compat_A4.json` gives:

- `Ric0form_SW_norm2_over_8pi2` = 3.9556, the square of Ric°''(h_W,k_B) alone;
- `S_W_norm2_over_8pi2` = 5.6, the f-form value.

Step 49's Ric°-form W⁻ cost is also 5.6, but there it includes ⟨b₁, x₂(h_W,h_W,k_B)⟩. So the difference 1.644 is W⁻⊗W⁻ material that, in the Ric° form, sits in the exact-form term ⟨b₁,x₂⟩ and the norm factors. The agreement of the totals (5.6 and 2.1 across classes) is therefore a check of Lemma 1.1(b) at the W⁻⊗W⁻ level, beyond the corrector-block agreement `cgb_block_rel_diff` ≈ 2·10⁻¹⁵.

## 2. Degree counting in Lemma 1.1(c)

Write g = δ + h₂ + h₃ + … + ε(k_B + k₀), with k_B of degree −2. Curvature costs −2 in degree. Burns δ + εk_B is ASD and scalar-flat to all orders in ε, so every pure-k_B term in W⁺ and s vanishes.

**Lowest degrees of each order:**

| Quantity | Degrees present |
|---|---|
| W⁺₁ (order ε) | W⁺'(k₀) and W⁺''(h₂,k_B) at degree −2; h₃k_B at −1; h₂h₂k_B and h₄k_B at 0. No degree −3 or −4 piece. |
| W⁺₂ (order ε²) | Flat k_Bk_B at degree −6, which is zero. h₂k_Bk_B and k₀k_B at degree −4. h₃k_Bk_B at −3. h₂h₂k_Bk_B at −2. No degree −5 piece, since normal coordinates have no h₁. |
| W⁺₀ (background) | Degree ≥ 0. |

**Degree −4 contributions at order ε²:**

- **|W⁺₁|²:** only (−2)×(−2).
- **⟨W⁺₀, W⁺₂⟩:** only W⁺_p·W⁺₂^{(−4)}. The pairing ∇W⁺·W⁺₂^{(−5)} is absent, and ∇²W⁺·W⁺₂^{(−6)} is zero.
- **Volume and norm factors:**
  - ε²(k_B⊗k_B)·|W⁺_p|², which is W⁻-free.
  - The terms (ε k_B)·⟨W⁺_p, W⁺₁^{(−2)}⟩. These are not "background constants": they are linear in h₂ and k₀, including h_W and k₀^W. They are linear in W⁻ with SU(2)_−-invariant partners, so their S³ average is zero.

  Item (iii) of the note should list them.
- **s-terms:** identical in structure.

**Conclusions.**

- **W⁻⊗W⁻ terms at degree −4.** None occur outside |W⁺₁^W|² and (s₁^W)². The only candidate, h_W h_W k_B inside W⁺₁, has degree 0. In W⁺₂, the term h_W h_W k_B k_B has degree −2.
- **4-jet terms.** None occur in the f-form, because they would need W⁺₂^{(−6)} ≠ 0 or W⁺₁^{(−4)} ≠ 0.

This is a real strengthening over Step 49, where ∇²Rm entered via ⟨b₁,x₂⟩.

**Non-Einstein backgrounds.** The counting also holds there, which supports §6's statement that F depends only on Rm_p. As a consistency check, the coefficient of zy (an ε log ε term) is the order-ε, raw-degree −4 density 2⟨W⁺₀, W⁺'_flat(k_B)⟩ + (s-term) = 0. So no ε log(1/ε) term appears for any background.

## 3. Representation theory and Corollary 1.2

**Stabilizer and isotypic types.**

- The stabilizer of ζ ∈ Λ⁺ in SO(4) = (SU(2)_+ × SU(2)_−)/Z₂ is U(1)_+ × SU(2)_−.
- SU(2)_− acts trivially on Λ⁺, so it fixes both ζ and ω.
- The Burns isometry group U(2)_ζ contains SU(2)_−, so k_B is SU(2)_−-invariant.
- U(2)_ω ⊃ SU(2)_−, so h_CH is SU(2)_−-invariant.
- W⁻ ∈ S²₀Λ⁻ is the real spin-2 representation, which is irreducible.
- Ric° ∈ Λ⁺⊗Λ⁻ is three copies of spin 1.

All of these statements are correct.

**Splitting F_X = F_CH + κ.** Write the f-form as

F(k₀) = ∫|A₀ + S_W + Lk₀|²_w + λ(k₀) + c,

where:

- A₀ is the KE source, identical to CH because h₂ = h_CH + h_W in the (ω,ζ)-adapted frame;
- λ is the linear term from ⟨W⁺_p, W⁺₂(k₀,k_B)⟩ and the norm factors.

A₀ and λ are spin 0, S_W lies in the spin-2 isotypic component, and L*L is equivariant. If the class 𝒦 is SU(2)_−-invariant, Schur's lemma decouples the minimization into a spin-0 problem (the CH problem), a spin-2 problem (κ), and other isotypic types (no source, so minimizer zero). The splitting is correct.

**Correction needed in Corollary 2.2.** The last sentence, "inf_𝒦 F_X(p) = inf_𝒦 F_CH for every SO(4)-invariant corrector class", is false for the angular-degree ≤ 2 class, where κ = 2.1. The correct statement is: equality holds iff 𝒦 contains the spin-2 span {k₀^W(W⁻)}, or more generally iff S_W ∈ L(𝒦). The components of k₀^W are of the form x⁴/u², so the angular-degree ≤ 4 class qualifies, consistent with κ = 3·10⁻²⁹.

## 4. Theorem 2.1

**What the exact script computes.** `step50_exact_identity.py` uses:

- R_abcd = ½(g_ad,bc + g_bc,ad − g_ac,bd − g_bd,ac) + Γ_ebcΓ_ead − Γ_ebdΓ_eac at flat. The index placement in `R_lin` and `R_bil` was checked against this formula.
- The first-order frame e = 1 − p/2, applied to each slot in `frame_corr`.
- The flat Λ⁺ basis J_m, with ω = J₂ and ζ = J₃.

It reports exact zeros for:

- W⁺'(h_W), s'(h_W), Ric°'(h_W), so h_W is pure W⁻;
- W⁺'(k_B) and s'(k_B);
- all ten components of the identity.

It also confirms that the uncorrected source is nonzero.

**Sign of the bilinear term.** A sign error in the bilinear term relative to the linear term would not be detected by the linear checks. It is independently excluded by two results:

- The JAX script computes curvature by the full nonlinear Christoffel route, the same routine whose Einstein residual Ric = −6g was ≤ 5·10⁻¹⁵ in Step 49. Its unconstrained least-squares search recovers the same corrector (`natural_corrector.json`: coefficients 1.5000 and 0.2500, with κ = 9·10⁻³⁰).
- The Ric°/Laurent form gives F = −18.000000000019 at t = 1, with the exact completed-square profile −18 + 5.6(1−t)².

**h_W is a genuine W⁻ jet.** H²×H² with the aligned product complex structure J₂ and CH have the same s, the same ω, Ric° = 0, and hence the same KE-type W⁺. So h_W = −(1/3)W⁻_{ikjl}x^kx^l is the normal-coordinate jet of a nonzero W⁻.

**Equivariance.** The map W⁻ ↦ residual is linear and SU(2)_−-equivariant, because it is built from h_W (SO(4)-natural), the invariant k_B, and δ by natural operations. Its kernel is therefore an invariant subspace of an irreducible real representation that contains a nonzero vector, so the kernel is all of S²₀Λ⁻. The argument is complete.

**Corollary 2.2 at a KE point.** S_W + Lk₀^W = 0 pointwise, so the cross term with A₀ + Lk₀^{c*} vanishes. All remaining k₀^W- and h_W-linear terms (λ(k₀^W), W⁺_p·W⁺₂(h_W,k_B,k_B), and the norm factors) are spin-2-linear and average to zero. Hence F_X(k₀^{c*} + k₀^W) = F_CH(k₀^{c*}) exactly.

## 5. Theorem 3.1

**(A) Analytic two-scale representation.**

- Real-analyticity of Einstein metrics (DeTurck–Kazdan) and of exp gives analytic normal coordinates for T below the radius of convergence. A finite Taylor expansion with C^N remainder would suffice instead.
- The neck metric δ + zK_B + … is positive definite for z ≤ ¼: on the unit sphere its eigenvalues are 1 and 1+z.
- k₀^{c*} and k₀^W are even in ω, because v_mv_mᵀ/u is even and h_W·k_B is degree 2 times even. So ψ is even in r and ψ = ψ(y,z).
- ψ = O(z²), because Ric°_bg = 0 and every Ric° factor carries at least one power of z.
- The mean-value bound gives ε²φ₃(0,0)·log(T/2√ε) + O_T(ε²), since ∫(y+z) d log r is bounded.

**Degree-2 correctors at order ε.** A term εr²·(…) is the monomial zy². Paired with Ric°_B ~ z, it does reach the diagonal z²y². Step 49 shows its contribution is a radius-independent flux, which is zero. This is needed because the Step-49 c*-ansatz modes carry sinh²t factors, so Ch.5's neck contains such terms. The paragraph citing it should be kept in the written proof.

**Order-ε² terms of degree −2.** These are the multiplicative-versus-additive differences ε²/r² = z²y. They produce Ric° factors of order z²y. Paired with factors of order ≥ z they give z³y, which is never diagonal, so they enter only the ε-bucket.

**(C) The ε-bucket is legitimate.** To first order, the bucket equals DP_Burns[η], with η = ε(h₂(ξ) + k₀ + …) on scaled space up to |ξ| ~ T/√ε.

- **Convergence.** Ric°_B ~ |ξ|⁻⁴. Ric°'_B(εh₂) = ε[Ric°'_δ(h₂) + O(|ξ|⁻²)], and Ric°'_δ(h₂) = 0 because the background is Einstein. So the integrand is O(ε|ξ|⁻⁴)·|ξ|³ d|ξ|, which converges.
- **Dependence on asymptotic data only.** The functional depends only on the growth data (h₂, k₀):
  - compact changes of η pair to zero with the critical Burns metric (Bach-flat with W⁺ = 0, and s = 0, give EL = 0);
  - decaying changes ε·O(|ξ|⁻²) leave a flux of order |ξ|⁻⁷·|ξ|³ → 0.
- **Linearity.** It is linear in (h₂, k₀) and U(2)_ζ-equivariant, because the cutoffs are radial and Burns is U(2)_ζ-invariant.
- **h₃ and h₄.** The h₃ pairing has an integrand that grows like |ξ|³ but is odd under −I, so its sphere average vanishes. The h₄ terms appear only via Ric°''(h₂,h₂) + Ric°'(h₄) = 0, consistent with the absence of a zy² coefficient in ψ.
- **Outer transition.** It costs O_T(ε²) because Ric°_bg = 0.

**Correct formulation of the vanishing.** "ℓ = c·s" is vacuous, since s = −24 on every surface with Ric = −6g. The argument that actually works is:

ℓ(h_CH + h_W, k₀^{c*} + k₀^W) = ℓ(h_CH, k₀^{c*}) + ℓ(h_W, k₀^W).

The second term is an SU(2)_−-invariant linear functional on spin 2, hence zero. The first term is literally the CH bucket, which (5.A) gives as 0. This needs only that SO(4) acts transitively on orthonormal pairs (ω,ζ) in Λ⁺, which it does, so frames can be aligned.

**Where the CH comparison needs explicit support.** It is legitimate exactly when the Ch.5 neck has degree-0 part k₀^{c*}, including the v₁v₁ᵀ/u piece from (C²−1)σ₂². The other differences must be decaying or of degree 2. The Step-49 basis supports this: named modes 1–4 equal the degree-0 terms plus higher powers of u. The written proof should state this matching as a lemma.

**Orientation.** ζ ∈ Λ⁺_X defines an orientation-compatible complex structure at p. Burns is Kähler for ζ with W⁺ = 0, so gluing produces X#CP̄². This is correct.

**Remaining details to write out.** The divisibility ψ − ψ_B = z²yφ and the mean-value bound for an S³-averaged analytic density. Both follow from (A) as stated, so no new estimate is required.

## 6. Yamabe shortcut and Corollary 4.1

**The identity.** By the global CGB form, P = 4∫|W⁺|² + S/12 − 8π²(2χ+3τ). Since ∫|W⁺|² is conformally invariant, P(ĝ) − P(g) = (S(ĝ) − S(g))/12, as stated.

**Minimization of S.** If Y([g]) < 0, the inequality ∫s²dV ≥ Y([g])² holds on [g], with equality exactly for the constant-scalar-curvature Yamabe metric (Gursky; LeBrun). This requires only Y([g]) < 0, which follows from Y(M) < 0. The Seiberg–Witten estimate ∫s² ≥ 32π²c₁²(X) holds for every metric on X#kCP̄², and in particular for ĝ.

**Monotonicity.** The map (P,S) ↦ 4P/(P + S/4) decreases in S and increases in P. Hence E(ĝ) ≤ 4P(ĝ)/(P(ĝ) + 8π²A) ≤ 4P(g)/(P(g) + 8π²A), which is correct.

**Corollary 4.1.**

- c₁² is multiplicative under unramified covers.
- Lifts of B_{2T}(p₀) are disjoint and the metric is Einstein outside them, so P is additive over cells.
- The order of limits (T, then fixed ε, then j) is sound.
- The number of cells per cover must stay compatible with k_j ≲ (number of disjoint lifted balls). This bookkeeping and the handle supply are inherited from the cited families and cannot be checked from the supplied files.

## 7. Remarks on §5–§6

**§5.** Theorem 3.1 gives a competitor with P/8π² < 1 for any ζ ⊥ ω, independent of the bubble's own orientation. So p_*(X#CP̄²) < P(g_KE) + 8π² rules out energy equality with a KE bulk carrying one bubble.

**§6, invariant count.** The count is right:

- five U(1)_+-invariant quadratics on (s, W⁺) (weight 0 pair: three; weight 1: one; weight 2: one);
- two on Ric°, because the antisymmetric U(1)_+ invariant on the weight-1 part drops out of a quadratic form;
- no Ric°×(s, W⁺) or W⁻×Ric° cross terms.

**§6, non-Einstein bulk.** Here the ε-bucket is no longer local. The term ε∫⟨Ric°_bg, Ric°'(χk)⟩ over the whole ball is the first variation DP_{g_bg}[χk]. It reduces to a pointwise invariant at p (∝ R⁺_p(ζ,ζ) per A02) only when g_bg satisfies the Euler–Lagrange equation of P. That criticality of the bulk is the extra hypothesis the non-Einstein extension requires.