# Step 50: the W⁻ sector of the Burns–background interaction is an exact completed square, and the logarithmic sub-8π² one-blow-up construction holds on every negative Kähler–Einstein surface

Session S1003A01, Agent2, Execute. Supersedes the interpretation in §§3–5 of `step49_kernel_log_coefficient_general_background.md`. The Step-49 numbers there remain valid.

Status labels:
- [E] exact symbolic (rational-function) identity;
- [P] proof given here;
- [N] floating-point computation, recorded as evidence only;
- [C] proof outline whose remaining analytic details are routine but not yet written out line by line.

Scripts:
- `workspace/scripts/step50_wminus_compatibility.py`: CGB-form W⁻ residual over corrector classes;
- `step50_natural_corrector.py`: sparse search for the corrector;
- `step50_check_corrector_ric0.py`: check in the independent Step-49 Ric°/Laurent quadratic form;
- `step50_exact_identity.py`: exact sympy identity.

Data are in `workspace/data/step50/`: `wminus_compat_A{0,2,4,6}.json`, `natural_corrector.json`, `corrector_check_ric0form.json`, `exact_identity.json`.

## 0. Setting and notation
- (X, g_bg) is a compact negative Kähler–Einstein (KE) surface, normalized Ric = −6g as in Ch.5. Its Kähler form is ω and p ∈ X is arbitrary.
- x are g_bg-normal coordinates at p, with r = |x|.
- ζ ∈ Λ⁺_p is a unit 2-form with ζ ⊥ ω, the perpendicular kernel orientation, ker R⁺_p = ω^⊥.
- Burns tail: k_B = σ₁²+σ₂² = (v₀v₀ᵀ+v₁v₁ᵀ)/|x|⁴. Flat Burns is **exactly** δ+εk_B, and it is scalar-flat and ASD for the orientation in which ζ is self-dual (W⁺ = 0, s = 0).
- Normal-coordinate jet: g_bg = δ + h₂ + h₃ + h₄ + …, with h₂ = −(1/3)R_{ikjl}x^kx^l. Split h₂ = h_KE + h_W, where h_W is the W⁻_p part.
- Neck metric: g_bg + ε(k_B + k₀), where k₀ is a corrector whose components are homogeneous of degree 0.
- The log coefficient F is the z²y² corner coefficient (z = ε/r², y = r²) of the S³-averaged density per d log r, normalized as in Ch.5. The relevant expansion is P/8π² ⊃ (F/2)ε²log(1/ε), and Ch.5 gives F = −18 on CH.

## 1. Chern–Gauss–Bonnet form of the corner coefficient [P]
In dimension 4, pointwise:
  |Ric°|² dV = (4|W⁺|² + s²/12) dV − 16π²e − 24π²l.
Here |W⁺|² is the Frobenius norm of W⁺ as an operator on Λ², so that ∫_{CP²}|W⁺|² = 12π². The forms e and l are the Euler and **signature** densities, normalized by ∫e = χ and ∫l = τ (in terms of the first Pontryagin form, 24π²l = 8π²p₁). This correction is from the TTCS verifier.

**Lemma 1.1.**
- (a) Compute both densities of g_bg + ε(k_B+k₀), relative to g_bg, on the annulus. After S³-averaging they are analytic functions of (y,z), the S³ average killing odd powers of r. They differ by r∂_r of an analytic function G(y,z): the averaged Chern–Weil transgression on the sphere of radius r.
- (b) At fixed ε, r∂_r = 2y∂_y − 2z∂_z multiplies y^b z^a by (2b−2a). It therefore kills every diagonal coefficient, so F computed from |Ric°|² equals F computed from f := 4|W⁺|² + s²/12.
- (c) In the f-form only Rm_p enters F. Burns is exactly ASD and scalar-flat, so every flat-Burns term in W⁺ and s vanishes identically. Degree counting then leaves exactly three contributions to the degree −4 density at order ε²:
  - (i) |W⁺₁|² and s₁², where W⁺₁ and s₁ are the order-ε parts of degree −2; they are linear in h₂ ⊗ k_B and in k₀;
  - (ii) ⟨W⁺_bg(p), W⁺₂⟩ and s_bg s₂, where W⁺₂ and s₂ are the order-ε² parts of degree −4; they are linear in h₂ or in k₀;
  - (iii) volume and norm factors multiplying background constants;
  - (iv) first-order volume and norm corrections multiplied by ⟨𝓡₀(p), 𝓡_{1,−2}⟩. This term is linear in (h₂, k₀); the verifier noted it was missing from the first version, and it does not affect the W⁻ square.
  The jets h₃, h₄, … contribute only to degrees ≥ −2 at order ε². (In the Ric°-form the 4-jet does appear, through ⟨b₁,x₂⟩. That apparent dependence is exact-form bookkeeping.)

**Corollary 1.2 (W⁻ enters only as a nonnegative square).**
Assume Rm_p is of KE type with ζ ⊥ ω, so that Ric°_p = 0 and W⁺_p = (s/12)diag(2,−1,−1) in the ω-adapted basis. Let U(2)_ζ = U(1)_+ × SU(2)_−; here SU(2)_− fixes ζ and ω and acts on W⁻ by spin 2. Then:
- Every term linear in W⁻ has zero S³ average: its other ingredients (k_B, W⁺_bg, s_bg and the SU(2)_−-equivariant correctors) are SU(2)_−-invariant or equivariant, and spin 2 has no invariant.
- The only W⁻-quadratic terms are |W⁺₁^W|² and (s₁^W)². In particular W⁺₂ carries no W⁻⊗W⁻ terms at degree −4: Rm²-terms land in degree −2.
- Hence for every corrector class 𝒦 that is invariant under SO(4):

  F_X(p) = F_CH + κ_𝒦(W⁻_p),

  κ_𝒦(W⁻) = min_{k₀∈𝒦} (1/8π²)∫_{S³} [ 4|W⁺''(h_W,k_B) + W⁺'(k₀)|² + (s''(h_W,k_B) + s'(k₀))²/12 ] dΩ ≥ 0.

  Here F_CH is the CH optimum over the same class, primes denote flat derivatives, and the two arguments of W⁺'' are the two perturbation directions.

So W⁻ can never improve the coefficient; it can only cost. The cost vanishes exactly when the W⁻ source (S_W, σ_W) := (W⁺'', s'')(h_W, k_B) lies in the range of the flat linearized (W⁺, s) operator on degree-0 tensors.

Numerical confirmation of the reduction ([N], `wminus_compat_A*.json`, all values in F units):
| corrector class | κ from (W⁺,s)-form, Step 50 | F_H²×H² − F_CH from Ric°/Laurent form, Step 49 |
|---|---|---|
| none / SU(2)_−-invariant modes | 5.6 | 20.35 − 14.75 = −12.4 + 18 = 5.6 |
| angular degree ≤ 2 | 2.1 | −15.9 + 18 = 2.1 |
| angular degree ≤ 4 | 3·10⁻²⁹ | 0 (2·10⁻¹¹) |
| angular degree ≤ 6 | 8·10⁻²⁹ | 0 (task s49_t16_tool1: −18.000000000017) |

Two further checks:
- The flat corrector quadratic blocks agree in the two forms to 2·10⁻¹⁵ (relative). This is the exact-form statement (b) at the quadratic level.
- The coupling of the W⁻ source to the SU(2)_−-invariant modes is 2·10⁻¹³, as the spin argument requires.

The degree-6 Ric°-form run stops at −18 rather than going below it, as Corollary 1.2 predicts (κ ≥ 0).

## 2. The explicit corrector and the exact completed square [E]+[P]
**Theorem 2.1 (first-order W⁻ compatibility of the Burns tail).** For every algebraic W⁻ (pure anti-self-dual Weyl jet h_W in the ζ-orientation), the degree-0 tensor

  k₀^W = (3/2)·sym(h_W k_B) − (1/4)·tr(h_W k_B)·δ,  with sym(M) = (M+Mᵀ)/2 (matrix products in normal coordinates),

solves

  W⁺''_flat(h_W, k_B) + W⁺'_flat(k₀^W) = 0,  s''_flat(h_W, k_B) + s'_flat(k₀^W) = 0.

Here tr(h_W k_B) = −v₂ᵀh_W v₂/|x|⁴, because h_W x = 0 by the Gauss lemma and tr h_W = 0.

Proof.
- For W⁻ equal to the W⁻-jet of H²(−6)×H²(−6), all entries are rational functions. `step50_exact_identity.py` verifies all ten components (five of W⁺ in the J-basis and s) to be identically 0 in sympy rational arithmetic, using the exact bilinear curvature formula R = ½∂²g + Σ_e(Γ_{ebc}Γ_{ead} − Γ_{ebd}Γ_{eac}) with first-order frame corrections.
- The same run checks exactly that h_W is pure W⁻ (W⁺'(h_W) = s'(h_W) = Ric°'(h_W) = 0), that W⁺'(k_B) = s'(k_B) = 0, and that the source without corrector is nonzero.
- General W⁻: both sides of the identity are SU(2)_−-equivariant and linear in W⁻, because k₀^W is built naturally from h_W, k_B and δ. The set of W⁻ for which the identity holds is therefore an invariant linear subspace of the irreducible spin-2 representation. It contains a nonzero element, so it is everything. ∎

Interpretation.
- The trace term only corrects s, since W⁺ is conformally invariant.
- The coefficient 3/2 is the factor by which the "metric product" sym(h_W k_B) must be amplified for the composite metric δ + h_W + εk_B to stay ASD and scalar-flat to first order in (W⁻ × ε).
- Geometrically, the perpendicular Burns tail can be coupled to an arbitrary background W⁻ field at first order with no W⁺ or scalar response. W⁻ is the curvature the Burns bubble itself carries, so this compatibility has a natural ASD-deformation flavour; the exact identity is what is proved.

**Completed square in the independent Ric°/Laurent form** ([N], `corrector_check_ric0form.json`, Step-49 quadratic forms, angular degree ≤ 4):
- F_H²×H²(c* + t·k₀^W) = −18 + 5.6(1−t)²: values −12.4, −16.6, −18.000000000019, −16.6 at t = 0, ½, 1, 3/2.
- The cross term with the Ch.5 c*-ansatz is −5.6 and the quadratic term is +5.6.
- On CH the same tensor (built from the H²×H² h_W) has zero cross term (5·10⁻¹⁵) and costs +5.6t², as it must, since CH has no W⁻ to cancel.

This is exactly the completed-square structure seen in the saved matrices (Spirit #59): identical corrector blocks, an extra 5.6 in the constant term, a negligible pairing with the CH source, and a Schur complement recovering 5.6.

**Corollary 2.2 [P, given Ch.5's symbolic F_CH(c*) = −18].** At every point of every negative KE surface, the corrector k₀ = k₀^{c*} + k₀^W gives corner coefficient F = −18. Here k₀^{c*} is the degree-0 part of the Ch.5 neck: v₁v₁ᵀ/u + 2c₁v₀v₀ᵀ/u + 2c₂v₁v₁ᵀ/u + 2c₃v₂v₂ᵀ/u with c* = (9/4, 3/4, 1/2), written in the ω,ζ-adapted frame at p. No CH region, symmetry, or Bianchi-IX structure of the background is used.

When the corrector class is a linear, SO(4)-stable space 𝒦, isotypic decomposition gives inf_𝒦 F_X = inf_𝒦 F_CH + κ_𝒦 with κ_𝒦 ≥ 0. This is **not** zero for every such class: the degree-≤2 class gives κ = 2.1. It is zero whenever the W⁻ source lies in L(𝒦). That happens for the degree-≤4 class, for every larger class, and for unrestricted smooth degree-0 correctors. For those classes W⁻ is invisible to the optimal logarithmic coefficient.

## 3. The construction on an arbitrary negative KE surface [P/C]
**Theorem 3.1.** Let (X, g_bg) be a compact negative KE surface (Ric = −6g), p ∈ X, ζ ⊥ ω. Then for every sufficiently small T > 0 there exist ε_T > 0 and smooth metrics g_ε on X#CP̄² (0 < ε < ε_T) with the following properties:
- g_ε = g_bg outside the normal ball B_{2T}(p);
- g_ε is exactly a flat-scale Burns metric on r ≤ √ε;
- P(g_ε)/8π² = 1 − 9ε²log(1/ε) + O_{X,p,T}(ε²).

In Ric = −g units, with x = Area(E)/π: P/8π² = 1 − ¼x²log(1/x) + O(x²).

Construction (additive form of Ch.5 (5.1.1)). Let χ_in(r) = χ(r/√ε) and χ_out(r) = 1 − χ(r/T), with χ as in Ch.5. Set
- r ≤ √ε: g_ε = δ + εk_B (Burns, smooth across the bolt);
- otherwise g_ε = (1−χ_in)(δ+εk_B) + χ_in·[g_bg + χ_out·ε(k_B + k₀)], with k₀ = k₀^{c*} + k₀^W(W⁻_p) from Corollary 2.2.

Proof structure. Three facts make the general case work like Ch.5, though the background has no symmetry.

(A) Analytic two-scale representation [C].
- KE metrics are real-analytic in normal coordinates (DeTurck–Kazdan, together with analyticity of exp).
- On the neck 2√ε ≤ r ≤ T, write g_ε(x) = G(ω; r, z) = δ + Σ_{n≥2} rⁿG_n(ω) + zK_B(ω) + z r²k₀(ω), which is analytic in (r, z) on [0,T]×[0,1/4].
- The |Ric°|² density per d log r dΩ, S³-averaged, is ψ(r, z). It is even in r, because (ω, r) ↦ (−ω, −r) fixes x and z. So ψ = ψ(y, z) is analytic.
- Exact boundary data: ψ(y, z) = O(z²), since Ric°(g_bg) = 0; and ψ(0, z) = ψ_B(z), the flat-Burns density.
- Hence ψ − ψ_B = z²y·φ(y, z) with φ analytic. Writing φ = φ(0, z) + y·φ₃(y, z) gives the density z²y·φ(0, z) + ε²φ₃(y, z).
- The second piece gives ε²φ₃(0,0)·log(T/2√ε) + O_T(ε²) by the mean-value bound of Ch.5 (5.3.2), with φ₃(0,0) = F/2-normalized, i.e. the corner coefficient.
- The first piece is (ε/2)∫_{ε/T²}^{1/4} φ(0, z) dz = ε·ℓ_N + O(ε²/T²). This is a pure order-ε bucket, linear in (h₂, k₀).

(B) Core and transitions.
- r ≤ √ε: exact Burns.
- √ε ≤ r ≤ 2√ε: in ξ = x/√ε the metric is ε·(Burns + η), where η = ε(h₂(ξ)+k₀) + O(ε^{3/2}) in C^k on 1 ≤ |ξ| ≤ 2.
- Burns is P-critical: it is Bach-flat and scalar-flat, so ∇P = 0. The P-change is therefore ε·(flux bilinear in Burns and the asymptotic form of η₁) + O(ε²).
- The ε^{3/2} term is odd under the isometry −I ∈ U(2) of Burns, so its linear contribution vanishes.
- Outer transition T ≤ r ≤ 2T: g_ε − g_bg = O_T(ε) in C², with Ric°(g_bg) = 0, so the cost is O_T(ε²). There is no first-order term because the background is Einstein.

(C) Vanishing of the order-ε bucket [P].
- The total order-ε coefficient ℓ = ℓ_core + ℓ_N is a U(2)_ζ-invariant linear functional of (Rm_p, k₀).
- It is independent of the inner blending and of the precise neck form: compactly supported changes of η₁ pair to zero with the P-critical Burns metric.
  - The same holds for decaying changes (for example additive versus Ch.5's multiplicative radii, which differ by ε·O(|ξ|⁻²) in scaled variables). The boundary flux against the Burns tail is O(|ξ|⁻⁷)·|ξ|³ → 0.
  - So ℓ depends only on the non-decaying asymptotics: the growth ε h₂(ξ) and the constants ε k₀.
- Direct flux evaluation (TTCS verifier, `trace/ttcs/results/step50_ttcs01_verifier1_integration.md` §4; supersedes the CH-comparison argument of the first version):
  - Burns has s = W⁺ = 0, so for variations vanishing near the bolt DP_{g_B}(q) = 𝓑_R(q), the outer boundary flux of the first variation.
  - Bounded degree-0 correctors k₀ give 𝓑_R = O(R⁻²) → 0. So the bucket is independent of **every** degree-0 corrector, and of the blending.
  - The growing jet h₂ = −(1/3)R_{ikjl}x^kx^l is evaluated against the leading Burns Ricci tensor b = (2/r⁴)(δ − 2θ⊗θ − 2J_ζθ⊗J_ζθ), with θ = x/r. The S³ average uses ⨍R(J_ζθ,θ,J_ζθ,θ) = s/12 + ½W⁺(ζ,ζ). The result is
    𝓑_∞(h₂) = −8π²(W⁺(ζ,ζ) + s/12) = −8π²R⁺_p(ζ,ζ),  so  ℓ = −R⁺_p(ζ,ζ)  (in P/8π² and Burns-ε units).
  - At a KE point with ζ ⊥ ω, W⁺(ζ,ζ) = −s/12, so ℓ = 0.
  - This agrees in form with A02's first-order Burns term −8λ²⟨R⁺_p, UΦUᵀ⟩, and with Ch.5 (5.A), which has no O(ε) term on CH.
  - Status: the derivation is from the verifier; this session has not yet rechecked the constant independently. Only the vanishing in the kernel orientation is used.

Combining (A)–(C) with F = −18 from Corollary 2.2 gives the theorem. ∎

What still has to be written in full: the analytic-representation details of (A), the divisibility statements, and the precise flux formula for ℓ. These follow Ch.5 §§5.3–5.5 verbatim, with "radial ODE" replaced by "S³-averaged analytic density"; no estimate beyond Ch.5's mean-value bound is needed. Constants depend on (X, p, T). No uniformity over different KE surfaces is claimed or needed.

## 4. Closed upper bounds via the Yamabe shortcut [P]
On a closed four-manifold, conformal invariance of ∫|W⁺|² gives P(ĝ) − P(g) = [S(ĝ) − S(g)]/12 for conformal metrics. If Y(M) < 0, the constant-scalar-curvature (Yamabe) representative ĝ of [g] minimizes S in [g]. Hence P(ĝ) ≤ P(g) and L_s(ĝ) = 0, so

  E(ĝ) = 4P(ĝ)/(P(ĝ) + S(ĝ)/4) ≤ 4P(g)/(P(g) + 8π²A),  A = c₁²(X),

whenever the actual Seiberg–Witten supply gives S(ĝ) ≥ 32π²A. This is LeBrun's estimate on X#kCP̄² with X minimal of general type (b⁺ ≥ 2, or the stated b⁺ = 1 chamber), and on the inherited connected-sum families under their stated supply. No local J_6 expansion or conformal normalization of the new cells is needed.

**Corollary 4.1.** Let X₀ be any fixed compact negative KE surface and X_j → X₀ unramified covers of degree d_j → ∞, with A_j = d_jA₀. Fix T and a ball B_{2T}(p₀). Theorem 3.1 gives a fixed cell with P = 8π²(1 − δ_{X₀}), δ_{X₀} > 0, which is then frozen. Replicate it in the lifted balls, together with the inherited shrinking handles. Then for the balanced families (Q_j = k_j + 4ℓ_j, h_j → 0, θ_j = k_j/Q_j → θ):

  limsup α(M_j)/h_j ≤ 4(1 − δ_{X₀}θ).

For θ = 2/9 this is 4 − (8/9)δ_{X₀} < 4. For pure blow-ups (θ = 1) it is 4(1 − δ_{X₀}).

Order of limits: first T, then a fixed ε, then j → ∞. This extends Ch.5 (5.6.1) from compact CH surfaces to covers of every negative KE base. It is an upper construction only; it does not extend the all-metric lower window. A single blow-up already gives α(X#CP̄²) ≤ 4P/(P+8π²A) < 4/(1+A) under the supply hypothesis.

## 5. Consequences for the peer programme (A02 Thm 53.B/D, 54.A) [P given Theorem 3.1]
- p_*(X#CP̄²) < 8π² = p_*(X) + 8π² for every negative KE surface X.
- Consider an Anderson case-(I) energy-equality configuration whose bulk is (X, g_KE) and which carries one Burns-type bubble.
  - For the bubble orientation at the bubble point, an aligned insertion pays +8λ²|s|/4 at first order.
  - A perpendicular insertion is first-order neutral and strictly saves at log order.
  - Bubble movement (A02 53.B) together with Theorem 3.1 then contradicts minimality.
  - So such a configuration cannot occur.
- This excludes a KE bulk carrying a Burns bubble. It does **not** exclude non-KE Einstein bulk, prove attainment, or give p_*(M_k) < p_*(M_{k−m}) + 8π²m at non-KE bulk minimizers. Those need F for non-KE R⁺ ≤ 0 shapes and for Ric°_p ≠ 0 (§6).

## 6. What the CGB form makes computable next
The degree count of Lemma 1.1(c) holds for any background, Einstein or not. For a non-Einstein background there is, however, an additional first-order bulk variation ε·DP_{g_bg}[χ(k_B + k₀)]. It reduces to the pointwise ℓ = −R⁺_p(ζ,ζ) only when the bulk is P-critical, as it is for A02's minimizers; otherwise it needs separate control. Hence F(Rm_p, ζ) is a U(2)_ζ-invariant quadratic form in Rm_p alone, independent of higher jets. The invariants are:
- W⁻: only |W⁻|², with κ = 0 (Theorem 2.1);
- Ric° ∈ Λ⁺⊗Λ⁻: |Ric°(ζ)|² and |Ric°_{ζ^⊥}|², each entering as a nonnegative minimized square, with no cross terms with s or W⁺ (SU(2)_− spin 1);
- (s, W⁺) under U(1)_+: s², s·W⁺_{ζζ}, W⁺_{ζζ}², |W⁺_{ζ⊥}|² (weight 1) and |W⁺_{⊥⊥,0}|² (weight 2).

So 5 + 2 coefficients determine the log coefficient at every point of every background. They can be computed as the a²ε² coefficient of the f-density of δ + a h₂ + ε(k_B + a k₀). That coefficient is homogeneous of degree −4, so no Laurent extraction is needed, and the computation fits directly into `step50_wminus_compatibility.py`. For non-Einstein bulk there is also an order-ε flux term ℓ ∝ R⁺_p(ζ,ζ), which A02's R⁺ ≤ 0 selects to vanish on ker R⁺. This is the input to A02's general-k comparison and to the Problem-3 attainment chain.
