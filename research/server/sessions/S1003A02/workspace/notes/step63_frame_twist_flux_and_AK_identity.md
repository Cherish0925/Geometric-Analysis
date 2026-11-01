# Step 63 — The exceptional flux in the frame: a Hodge–Gauss bound, the exact almost-Kähler identity, and the empty equality locus

Agent2, Execute. The shell was blocked again for this step, so everything here is derivation. Sources read this step:
- Apostolov–Armstrong–Drăghici, *Local models and integrability of certain almost Kähler 4-manifolds* (Knowledge `Local-models-and-integrability…`): lines 30–64 and 112–236, giving conventions (6)–(25) and the canonical Chern form γ_J = R(Ω) − a∧Ja.
- The Step-62 note `step62_weyl_channel_reduction.md`.

Setting and notation.
- M = X#kCP̄², X minimal of general type, A = c₁²(X), P = ∫|Ric°|², p = P/8π².
- For a class a ∈ H²(M) and a metric g, a^± are the g-harmonic (anti-)self-dual parts and |a^-|² := −∫ a^-∧a^- ≥ 0.
- 2-form norms have |e¹∧e²| = 1, and the Kähler-type form has |Ω|² = 2.

## 1. Theorem 63.T: the frame-twist bound (any metric, no Seiberg–Witten input)

Let g be any metric and J any g-orthogonal almost complex structure inducing the orientation. Write Ω = g(J·,·), so Ω ∈ Λ⁺ with |Ω|² = 2. Choose a local gauge φ ∈ Ω^⊥ ⊂ Λ⁺ with |φ|² = 2, and write
\[
\nabla\Omega=\alpha\otimes\phi+\beta\otimes J\phi,\qquad
\nabla\phi=-\alpha\otimes\Omega+b\otimes J\phi .
\]
Then b is a connection 1-form on Ω^⊥ ≅ K_J^{-1}. Applying d^∇ to ∇φ and taking the Jφ-component of the Ricci identity gives, gauge-independently,
\[
\gamma_J:=-db=R(\Omega)+\alpha\wedge\beta ,\qquad [\gamma_J]=2\pi c_1(J).
\tag{63.1}
\]
Here R is the curvature operator on Λ². For an almost-Kähler J one has α = a and β = −Ja, and (63.1) becomes AAD (25), γ_J = R(Ω) − a∧Ja. That is the consistency check of the sign.

The Singer–Thorpe decomposition gives:
- R(Ω)^- = ½Ric̃₀(Ω) = ρ₀^J, the J-invariant primitive Ricci form, with |ρ₀^J|² = ½|Ric₀'|² ≤ ½|Ric°|²;
- α∧β is decomposable, so |(α∧β)^±| = |α∧β|/√2 ≤ |∇Ω|²/(4√2).

Hodge theory finishes the argument. Write γ_J = H + dθ with H harmonic. Then ‖γ_J^-‖² = ‖H^-‖² + ‖(dθ)^-‖², because ⟨H^-,(dθ)^-⟩ = ½(⟨H,dθ⟩ − ∫H∧dθ) = 0. Hence ‖γ_J^-‖ ≥ 2π|c₁(J)^-|. This gives:

**Theorem 63.T.** For every metric g and every orthogonal almost complex structure J on a closed oriented 4-manifold,
\[
\Bigl(\tfrac12\int|\operatorname{Ric}_0'|^2\Bigr)^{1/2}\ \ge\ 2\pi|c_1(J)^-|_g-\|(\alpha\wedge\beta)^-\|_{L^2},
\qquad\text{so}\qquad
P\ \ge\ 2\bigl(2\pi|c_1(J)^-|-\mathcal T_J\bigr)_+^2 ,
\]
where 𝒯_J := ‖(α∧β)^-‖_{L²} ≤ (1/4√2)‖∇Ω‖²_{L⁴} is the **ASD frame twist** of J.

**Choice of class on M.**
- For ε ∈ {±1}^k put a_ε = c₁(X) + Σε_iE_i. Each a_ε is characteristic with a_ε² = c₁²(M), so (Wu) a_ε = c₁(J) for some orthogonal J.
- Averaging over ε gives max_ε(a_ε^+)² ≥ (c₁(X)^+)² + Σ(E_i^+)² ≥ A + |c₁(X)^-|² + Σ(E_i^+)².
- So the best sign has |a_ε^-|² = (a_ε^+)² − (A−k) ≥ k + Π.

Hence, with no Seiberg–Witten hypothesis,
\[
\boxed{\ \sqrt{P/2}\ \ge\ 2\pi\sqrt{k+\Pi}-\inf_{J:\,c_1(J)=a_\varepsilon}\mathcal T_J\ }
\tag{63.2}
\]

Readings.
- (i) **Kähler tariff.** For a Kähler metric, J itself has 𝒯_J = 0 and Ric₀'' = 0. With (a^+)² ≥ A from Hodge index on the blow-up Kähler cone, (63.2) is P ≥ 8π²k. This is Theorem K∞ without Seiberg–Witten.
- (ii) **Where the exceptional flux goes.** For every J, the ASD part of the Chern form must carry flux 2π|c₁^-| ≥ 2π√k. Only two carriers exist: the J-invariant tracefree Ricci tensor, which costs P, and the ASD frame twist 𝒯_J. This is the exact form of the Step-40s observation that "charge can reside in anti-self-dual relative curvature".
- (iii) **Necessary condition for every sub-tariff family.** If p ≤ c·k, then *every* orthogonal J in the best class has
  \[
  \mathcal T_J\ge 2\pi\sqrt k\,(1-\sqrt c).
  \]
  - Certified CH cell (c = 0.995663): 𝒯_J ≥ 0.01365 for every J.
  - A family with p/k → 0: 𝒯_J ≥ 2π√k(1 − o(1)) for every J. The twist of every almost complex structure must carry the whole exceptional flux.
- (iv) **Local consistency with Theorem F and Theorem 59.R.**
  - In a Burns insertion of scale ε in a kernel direction ζ ⊥ ω, the natural J equals J_ζ in the core and J_ω outside. The rotation by π/2 across the logarithmic collar √ε ≲ r ≲ ρ has |∇Ω| ~ (r log(ρ/√ε))^{-1}, so 𝒯_J² ≲ (log 1/ε)^{-3}.
  - (63.2) therefore permits a saving of at most O((log 1/ε)^{-3/2}). The actual savings, ε (first order) and ε²log (second order), lie far inside this.

## 2. Proposition 63.AK: the exact almost-Kähler identity

Now let (g, J, Ω) be almost-Kähler. AAD conventions:
- ∇Ω = a⊗φ − Ja⊗Jφ;
- u := |a|² = |∇Ω|²/4;
- s* − s = |∇Ω|² = 4u;
- W⁺ = W₁ + W₂ + W₃, with conformal scalar curvature κ_J = 3⟨W⁺Ω, Ω⟩ = s + 6u;
- |W₁|² = κ_J²/24;
- W₂ = ½(ρ_*''⊗Ω + Ω⊗ρ_*''), so |W₂|² = |ρ_*''|².

From (63.1), γ_J^+ = ((s + s*)/8)Ω + ρ_*'', so |γ_J^+|² = (s+2u)²/8 + |ρ_*''|²; and γ_J^- = ρ₀ − (a∧Ja)^-.

Combine three exact relations:
- Chern–Weil: P = 4∫|W⁺|² + ∫s²/12 − 8π²c₁²(M);
- ∫|γ_J^+|² − ∫|γ_J^-|² = 4π²c₁(J)² = 4π²c₁²(M);
- the pointwise identity (s+6u)²/6 + s²/12 − (s+2u)²/4 = su + 5u².

They give:

**Proposition 63.AK.** For every almost-Kähler metric on a closed 4-manifold,
\[
\boxed{\ P=2\|\gamma_J^-\|^2+\int u\,(5u+s)\,d\mu+2\int|\rho_*''|^2+4\int|W_3^+|^2\ }
\tag{63.3}
\]
with ‖γ_J^-‖² ≥ 4π²|c₁(J)^-|². Hence
\[
P\ \ge\ 8\pi^2|c_1(J)^-|^2-\int u\,(|s|-5u)_+ .
\]

Checks.
- Kähler (u = 0): (63.3) is P = ∫|Ric₀'|². This is correct because Ric'' = 0.
- **Sekigawa's theorem is (63.3) at P = 0, s ≥ 0.** Every term is then nonnegative, so u ≡ 0.
- AK Einstein with s < 0. Here γ^- = −(a∧Ja)^- and ‖γ^-‖² = ½∫u². Then (63.3) gives
  \[
  \int u\,(|s|-6u)=2\int|\rho_*''|^2+4\int|W_3^+|^2,\qquad
  \tfrac12\int u^2\ge4\pi^2|c_1(J)^-|^2 .
  \]
  A strictly AK Einstein metric therefore needs ‖∇Ω‖⁴_{L⁴} = 16∫u² ≥ 128π²|c₁^-|², and also u ≤ |s|/6 on average in the weighted sense above. These are two integral constraints for A01's Goldberg problem. Novelty against the literature (Armstrong's and Drăghici's integral formulas) is not yet checked.
- Saving against 8π²|c₁^-|² requires torsion in the window 0 < u < |s|/5. The pointwise maximum is s²/20. Optimizing (63.3) and Chern–Weil pointwise over (s, u) reproduces exactly LeBrun's k − A/3, with multiplier λ = 4/3. So **(63.3) by itself sits at the LeBrun barrier.** New information comes only from the ASD-side split γ^- = ρ₀ − t^- (Theorem 63.T) together with the moments of u.

## 3. The equality locus of Theorem 62.A is empty for every k ≥ 1

Equality in 62.A requires three things:
- LeBrun equality (Prop. 2.4): AK at the Yamabe metric, Ω on the lowest eigenspace of W⁺, W₂ = W₃ = 0;
- the Cauchy–Schwarz step: s and |W⁺| constant;
- Π = 0.

Then κ_J = s + 6u is constant, so **u = |∇Ω|²/4 is constant**. Two independent arguments exclude this unless k = 0 and the metric is Kähler.

- **(a) Chern classes (Armstrong; LeBrun; AAD Lemma 2).** If u ≡ const > 0, the Nijenhuis tensor never vanishes. Then c₁(I) = 3c₁(J), which forces 5χ + 6τ = 0. But N is a section of Λ^{0,1}⊗Λ^{0,2} ≅ T^{1,0}⊗K^{-1}, whose c₂ is c₂ + 2c₁². On M this is
  \[
  5\chi+6\tau=c_2(X)+2A-k>0
  \]
  for every k < c₂(X) + 2A, so in particular in the whole open range. If u ≡ 0, J is Kähler and κ ≤ 0 (Step 62 §3a).
- **(b) Periods (Taubes; Li–Liu).** Π = 0 forces E_i^+ = 0, hence E_i·[Ω] = 0 because [Ω] ∈ H⁺_g. But Ω is symplectic, and ±E_i is represented by a symplectic (−1)-sphere, which has positive area.

Answer to the scope question on AAD. Their Theorem 2 is stated for the *third* Gray condition, i.e. Ric'' = 0 together with W(Ω) = (κ/6)Ω (lines 54–62). The 62.A locus has W(Ω) = (κ/6)Ω and W₃ = 0 with constants, but not Ric'' = 0. Argument (a) makes AAD unnecessary. **So rigidity on the locus holds and is cheap. The whole content of the open-range problem is stability.**

## 4. What the combined system allows: the saturating "ASD-patch" configuration

The integral system available so far consists of:
- Chern–Weil (Euler and signature);
- LeBrun's Prop. 4 for the best sign;
- Yamabe;
- the flux bound 63.T.

All four are evaluated in the AK model at s ≡ −4, with W₂ = W₃ = 0 and the torsion density u a function. Write the volume as V = 2π²(A + υ), and set h = k/A.

**(A) Constant torsion (u ≡ ū).** Here 63.AK and 63.T, with ρ₀ = 0 allowed, give exactly
\[
(A+\upsilon)\,\bar u(4-3\bar u)\ge4(A-k),\qquad
p\ \ge\ (A-k)\frac{(2-3\bar u)^2}{\bar u(4-3\bar u)} .
\]
- The bound vanishes only at ū = 2/3 = |s|/6, which is the ASD point W⁺ = 0. Its value there is κ = A/2, the Taubes regime.
- In the formal-common-mode regime ū ≈ 2k/3A it gives p ≳ 3A²/2k ≫ k.
- **The formal common mode, which is LeBrun-extremal with nearly constant torsion, is therefore excluded as a p ≪ k state by the flux bound 63.T**, independently of Taubes' periods. Its 1/(4A) coefficient came from an algebra that never imposed the ASD flux 2π|c₁^-| ≥ 2π√k.
- Directly: with uniform torsion and κ ≈ k, 𝒯² = 4π²κ²/(9A). So 63.T gives p ≥ k(1 − κ/(3√(kA)))² ≈ k.

**(B) Variable torsion.**
- *Variance enters the 62.A slack.* The variance of u enters the Cauchy–Schwarz slack of 62.A with an explicit constant. To leading order the slack in p is σ = ¼A·Var(u), i.e.
  \[
  \int(u-\bar u)^2=8\pi^2\sigma .
  \]
- *What flux transport by twist requires.* Carrying the flux by twist needs ½∫u² ≈ 4π²k when p ≈ 0. That forces σ ≈ k, then κ ≈ 2k and υ ≈ 5k.
- *The extreme distribution saturates everything.* The extreme distribution is u = 2/3 (W⁺ = 0) on patches of total volume 18π²k and u = 0 elsewhere. It saturates **all** constraints simultaneously:
  - LeBrun Prop. 4 gives υ = 5k exactly, since 36V − 20V_p = 72π²A;
  - the flux bound holds with ½∫u² = 4π²k;
  - and p = υ − 5k = 0.
- *Per-patch data.* Each patch is an Einstein, s = −4, W⁺ = 0 region of volume 18π², with 2χ + 3τ = Vol/6π² = 3. These are **exactly the numbers of an orientation-reversed fake projective plane**: χ = 3, τ = −1, ASD Einstein, Vol = 2π²c₁² = 18π², and rational intersection form ⟨−1⟩, the same as CP̄².

**Interpretation (changes a global judgement).**
- Every integral constraint used in Steps 36–63 — Chern–Weil, the SW sign family, Hodge flux, Yamabe and Weitzenböck — depends only on rational cohomology and Chern numbers. None can distinguish a CP̄² summand from a rational-homology CP̄² such as \overline{FPP}.
- We expect the SW blow-up formula to extend to negative-definite summands with b₁ = 0. This needs a source.
- Within that information, the saturating configuration is X ⊔ k·\overline{FPP} with p = 0. What it ignores is the **joining**. A two-ended AE neck (χ(S³×ℝ) = 0) has P = 2∫|W|² + ∫s²/12 + 32π² ≥ 32π², i.e. 4 units, by Gauss–Bonnet with two Euclidean ends.
- So a positive tariff on X#kCP̄², or even the k²/A law, cannot come from such inequalities alone. It must price one of two things:
  - **the transition between twist-carrying (W⁺ ≈ 0) and W⁺-carrying (Kähler-type) regions**, which in the degenerate limit costs at least a neck;
  - or the smooth/homotopy type of the summand: CP̄²∖B is simply connected, whereas an ASD Einstein s < 0 piece with χ = 3, τ = −1 is a ball-quotient type.
- This is the precise version of Step 62's remark that "k must enter the Weyl channel itself". Conjecture 62.W/62.G now has a concrete competitor geometry to defeat.

## 5. Consequences for the target choice (strategist #78)

- **62.W and 62.G.** The flux bound excludes the formal-mode mechanism (diffuse torsion, κ ≈ k) for p ≪ k. What remains for p ≪ k is the patch mechanism, which needs κ ≈ 2k > k. So the surviving low-cost scenario violates 62.W (κ ≤ k) itself. Either 62.W fails or the patch mechanism is too expensive.
- **Plausible lower-bound mechanism.** A Kähler-type ↔ ASD-type transition cost, i.e. a quantitative "domain-wall" estimate for the frame twist, plausibly gives a positive per-class tariff (62.G-type). It would also explain why every known object has p/k ≥ 0.9957.
- **Next decisive questions.**
  - (Q1) A local wall estimate. In a region where the twist 𝒯 carries flux 2π, must the transition from u ≈ 0 to u ≈ |s|/6, i.e. from |W⁺| ≈ |s|/√24 to W⁺ ≈ 0, cost P ≳ c > 0, uniformly in the shape? The relevant quantity is the Euler/signature balance on the wall: the Gauss–Bonnet neck bound is the degenerate limit.
  - (Q2) A test of the competitor. Is α(X#k\overline{FPP}) < 8π²k? Equivalently, can negative Einstein pieces be joined more cheaply than a 4-unit neck through a fat transition? If yes, the CP̄²-versus-\overline{FPP} distinction is essential to any tariff on X#kCP̄².
  - (Q3) Make 63.T effective for non-AK near-minimisers. Use J := σ(ψ)/|σ(ψ)| from the SW spinor of the best class, modified near zeros of ψ. Control 𝒯_J by the SW slack in L⁴ of ∇ψ/|ψ|, as in the AK model where the slack controls ∫(u − ū)².

## Status

| Item | Status |
|---|---|
| 63.T | Proved: Hodge theory plus the Gauss formula (63.1). Sign cross-checked against AAD (25); a symbolic check is still owed. |
| 63.AK | Proved, given AAD's formulas, by exact algebra. Sekigawa is recovered. Independent verification pending. |
| §3 emptiness | Proved, modulo LeBrun Prop. 2.4's exact equality statement and the Taubes/Li–Liu (−1)-sphere theorem (cite). |
| §4 | Model computations: AK, s constant, W₂ = W₃ = 0, linearized slack. The \overline{FPP} identification is exact numerology. The neck bound is Gauss–Bonnet. Nothing here is a theorem about general metrics. |


## 6. Verification (TTCS step63_ttcs01, verifier + generator) — BINDING corrections

Source: `trace/ttcs/results/step63_ttcs01_verifier1_integration.md` and `…generator1_integration.md`.

**Confirmed in full:**
- 63.T, including (63.1) γ_J = R(Ω) + α∧β. The sign, the absence of any factor 2, and gauge invariance are all correct, and (63.1) holds without dΩ = 0. R(Ω)^- = ρ₀ with |ρ₀|² = ½|Ric₀'|². The Hodge step and the Wu existence step hold.
  - Sharpening: for the maximising sign, |a_ε^-|² = k + Π holds with *equality*.
  - Scope: the Kähler reduction must be applied to the actual parallel J.
- 63.AK: every coefficient is correct.
  - The Sekigawa check holds.
  - The AK-Einstein identities hold: ∫u(|s| − 6u) = 2∫|ρ_*''|² + 4∫|W₃|² and ∫|∇Ω|⁴ ≥ 128π²|c₁(J)^-|². The first is a weighted integral identity, *not* a pointwise bound u ≤ |s|/6.
  - The algebraic LeBrun barrier is confirmed (minimum k − A/3 at u = 1/2).
- §3, emptiness of the equality locus for k ≥ 1.
  - The period argument is already contained in LeBrun Prop 3.2 (Taubes), so Li–Liu is not needed.
  - The Chern-class argument needs only 5χ + 6τ ≠ 0, i.e. k ≠ c₂(X) + 2A.
- The constant-positive-torsion bound p ≥ (A−k)(2−3u)²/(u(4−3u)) is valid for 0 < u ≤ 2/3.
- The two-ended AE neck bound P ≥ 32π² is correct for complete two-ended AE limits. It is sharp, attained by (1 + a/r²)²g_{ℝ⁴}.

**Corrected:**
1. **Step 62.**
   - The intermediate coefficient is (2/3)(A − 2κ), not (1/6)(A − 2κ). The final identity 62.1 is unchanged.
   - 62.A holds for every 0 ≤ κ ≤ A/2. The function L_A *decreases* only up to 4A/9 and then increases; its minimum is k − A/3. The phrase "decreasing for κ < 2A" is wrong.
   - For κ < 0, use p ≥ k − (4/3)κ.
2. **Corollary 62.D is withdrawn as stated.** The term k − κ can be negative and cancel (υ − κ)/3. So p/k → 0 implies only κ ≥ k − p and υ = 4κ − 3k + 3p, together with (62.2). It does not imply κ/k → 1, nor Π = o(k), nor convergence to the equality locus. The patch densities (κ, υ) = (2k, 5k) with p = 0 are exactly such a cancellation.
3. **Formal-mode torsion is u = h = k/A, not 2k/(3A).** It follows from the eigenvalues (−x, x/2, x/2) with x = 2/3 − h, so κ_J = −4 + 6h. Consequently:
   - the constant-torsion bound gives p ≳ A²/k;
   - the best-class twist bound gives p ≥ k(1 − ½√(k/A) + …)².
   Both exclude the formal mode *as an exact AK model with these hypotheses*. Neither excludes non-AK near-minimisers.
4. **Variance and slack.** The relation ∫(u − ū)² = 8π²σ is only leading order, valid as m → 0, B/A → 1, Π = 0 and with saturated LeBrun. LeBrun slack contributes to σ independently.
5. **The patch model is a formal density only.**
   - It needs k ≤ A/4, since the residual Kähler volume is 2π²(A − 4k).
   - It does *not* saturate the Cauchy–Schwarz step.
   - With p = 0, W₂ = W₃ = 0 and Ric'' = 0, AAD (37) gives d^J u = 0. So u is constant, and no smooth AK-Einstein two-phase metric exists; any transition must activate W₃, ρ_*'' or Ric''. The governing identity is
     2d^Ju = 2⟨δW₃,Ω⟩ + 2δρ_*'' − ⟨ρ_*'', ∇_JΩ⟩ + ⟨A^+, Ω⟩, with A_Z = (d^∇Ric'')_Z + ι_{JZ}dρ.
   - \overline{FPP} has b⁺ = 0 and no orientation-compatible ACS. It is an ASD-Einstein competitor, not an AK patch.
   - For the full pieces: X ⊔ k\overline{FPP} has 2χ + 3τ = A + 3k, and with full-volume pieces κ = 0 and υ = 9k. The connected-sum identity then gives p = 4k: four units per join, consistent with the neck bound. The patch model has silently removed four units of host volume per class.
   - **The "blindness to CP̄² versus \overline{FPP}" sentence of §4 is downgraded.** The cap estimates below do not distinguish the two summands, since both punctures have (χ, τ) = (2, −1). But no low-cost competitor has been exhibited, and the SW extension to negative-definite summands is unsourced.
6. **The §1(iv) collar-twist estimate is withdrawn.** A one-parameter rotation of Ω in a parallel frame has α∧β = 0. Twist and frame rotation are different: the latter can cost nothing, with ∫|∇Ω|⁴ = 8π²Δθ⁴/L³ → 0.
7. **Arbitrary-J twist coercivity ‖t‖ ≤ √(CP) + r is false.** On Σ×Σ' with equal Einstein constants, P = 0, yet a J in a characteristic class with c₁^- ≠ 0 carries all its flux by twist. Any coercivity must use a *canonically selected* J, e.g. from the SW spinor; the obstacle there is the unweighted ∫|∇(ψ/|ψ|)|⁴ near the zeros of ψ.

**New rigorous wall estimate (generator; proved by localized Chern–Weil).** Let U ≅ (#_m CP̄²)∖B⁴ be a compact region with boundary. Define 𝔟(∂U) as the Gauss–Bonnet plus signature (APS-corrected) boundary terms and Q(U) = ∫_U(4|W⁺|² + s²/12). Then
\[
P(U)=Q(U)+8\pi^2(m-2)+2\mathfrak b(\partial U).
\]
Suppose U replaces a ball B of a reference metric h with boundary data matched up to |𝔟_g − 𝔟_h| ≤ δ. Then
\[
P_g(U)\ \ge\ 8\pi^2m-Q_h(B)-2\delta,\qquad
\text{and for a KE reference with } s=-4:\ \ P_g(U)\ge8\pi^2m-4\operatorname{Vol}_h(B)-2\delta .
\]
- This holds for arbitrarily fat interiors.
- With exact matching (δ = 0) and Vol_h(B) ≤ π², it gives a tariff of ½ per cap.
- A one-ended AE exceptional bubble has P ≥ 8π²m, with equality for Burns. The same holds for a punctured \overline{FPP}.
- It is the region form of the Step-54 Lemma 54.1′ charge bound, now with an explicit replaced-bulk term.
- **The only escape in this formulation is a large replaced host volume or a large boundary-transgression error.** The quantitative target that would close the open range is a transgression–coercivity inequality
  (8π² − 𝔟(∂U))₊ ≤ q·P(U ∪ collar) + ε,
  which gives P ≥ (8π²m − 2ε)/(1 + 2q).
- Cheap joinings exist only through collapsed interfaces (CH-cusp collars give P = O(e^{−4T})). That is the familiar collapse channel, not an exceptional S³ cap.

**Revised reading of the step.** The frame-twist theorem and the AK identity are solid tools, and the equality locus is empty. The quantitative content now sits in two places:
- (i) a canonically selected J, which arbitrary J cannot provide;
- (ii) the transgression/replaced-volume ledger of exceptional caps, which needs a coercivity estimate for 𝔟(∂U) against P on the collar.

Item (ii) is the cleanest formulation of the open-range problem obtained so far. Its Bianchi-IX restricted version, an exceptional bolt with CH-type outer boundary data, is computable with existing diagonal tools: compute I_U(h, L) = 8π²(m−2) + 2𝔟(h, L) + inf Q.
