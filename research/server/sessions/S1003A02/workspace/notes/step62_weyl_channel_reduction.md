# Step 62 — The Weyl-channel reduction of the open-range lower bound

Agent2, Execute. The shell was unavailable for this step, so everything below is derivation. The numerics quoted are taken from existing data files: the certified cell `step49_cell_theoremY_profile_x003_X128_N1600.json` and the Step-48/49 ledger.

Setting.
- X is minimal of general type with A = c₁²(X), b⁺(X) ≥ 2 and SW(X) ≠ 0 (the sign-family hypotheses of Theorems N/W/K/Y).
- M = X#kCP̄².
- p = P/8π² with P = ∫|Ric°|².
- For every ε ∈ {±1}^k, the class a_ε = K_X + Σε_iE_i is a monopole class (blow-up formula).

Notation.
- g̃ denotes the Yamabe representative of [g], normalised to s ≡ −4.
- W₂(g) = ∫|W⁺|² dμ. This is a conformal invariant.
- Y[g] is the Yamabe constant. Note that ∫s²dμ_{g̃} = Y², and ∫s²dμ_g ≥ Y² for every g in the class (negative Yamabe class).

## 1. Two conformal invariants and an exact identity

Define the **Weyl deficit** and the **Yamabe excess** of a conformal class:
\[
\kappa[g]:=\frac A2-\frac{3}{8\pi^2}\int_M|W^+_g|^2d\mu_g ,\qquad
\upsilon[g]:=\frac{Y[g]^2}{32\pi^2}-A=\frac{\operatorname{Vol}(\tilde g)-2\pi^2A}{2\pi^2}.
\]

Calibration.
- κ = 0 exactly when ∫|W⁺|² equals the Kähler–Einstein value (4π²/3)A. For a Kähler metric |W⁺|² = s²/24 pointwise.
- υ ≥ 0 is LeBrun's scalar estimate.
- In Step-48 variables: ω := δW/2π² = 4κ/3, where δW = (4π²/3)A − ∫|W⁺|²; and υ = ΔV/2π².

**Identity 62.1.** For every metric g on M,
\[
\boxed{\;p(\tilde g)=(k-\kappa)+\tfrac13(\upsilon-\kappa),\qquad p(g)\ge p(\tilde g).\;}
\]

*Proof.*
- Chern–Weil: P = 4∫|W⁺|² + (1/12)∫s² − 8π²(2χ+3τ)(M), and (2χ+3τ)(M) = A − k.
- At g̃: ∫s² = Y² = 32π²(A+υ) and ∫|W⁺|² = (4π²/3)(A − 2κ).
- Substituting: p = (1/6)(A−2κ) + (A+υ)/3 − A + k = k − (4/3)κ + υ/3.
- For a general g, P(g) − P(g̃) = (∫s²dμ_g − Y²)/12 ≥ 0. ∎

Check on the certified perpendicular cell (x₀ = .03, X = 128; Step-49 data, per class): ω = 4·0.018784 = 0.075136 and υ = 4·0.053096 = 0.212384. The identity gives p = 1 − 0.075136 + 0.070795 = 0.995659, against the interval value 0.9956627. The difference is the rounding of the Step-49 floats. So κ_cell = 0.05635 per class.

**Reading of 62.1.** The Einstein defect is a sum of two terms:
- the *Weyl shortfall* k − κ, i.e. how much less than one unit of κ per exceptional class the conformal class has achieved;
- one third of the *Yamabe overpayment* υ − κ, i.e. how much more Yamabe excess was spent than the Weyl deficit gained.

A family with p/k → 0 must therefore make both terms small.

## 2. LeBrun's two estimates in these coordinates

LeBrun's Prop. 2 and Prop. 4 (Knowledge `math-0111228…` lines 127–149; both hold for every metric) are applied to the sign class a_ε maximising (a_ε⁺)². We have (a_ε⁺)² = A − k + |a_ε⁻|², and E_ε|a_ε⁻|² = |K⁻|² + Σ|E_i⁻|² ≥ k. Write Π := max_ε(a_ε⁺)² − A ≥ 0; then Π ≥ |K_X⁻|² + Σ|E_i⁺|², because |E⁻|² = 1 + |E⁺|².

Prop. 2 gives υ ≥ Π ≥ 0.

Prop. 4 gives ∫(s − √6|W⁺|)² ≥ 72π²(A+Π). Since s < 0 somewhere is all that is used, the cross term satisfies ∫(s−√6|W⁺|)² ≤ (‖s‖₂ + √6‖W⁺‖₂)², by Cauchy–Schwarz on ∫|s||W⁺|. At g̃ this becomes
\[
\boxed{\;2\sqrt{A+\upsilon}+\sqrt{A-2\kappa}\ \ge\ 3\sqrt{A+\Pi}\;}\tag{62.2}
\]
This is the "envelope 2x + y ≥ 3" of the Step-61 plan, with x² = 1 + υ/A and y² = 1 − 2κ/A. **So Target 2 of Route 2 is not a new inequality: it is LeBrun's Prop. 4 plus Cauchy–Schwarz.** For Π = 0 it is sharp exactly when |W⁺| = λ|s| pointwise with s constant and LeBrun's equality structure holds (a special almost-Kähler metric).

Solving (62.2) for υ at fixed κ, with Π = 0 (Π ≥ 0 only helps), and writing y = √(1 − 2κ/A):
\[
\upsilon\ \ge\ \upsilon_{\rm L}(\kappa):=A\Bigl[\bigl(\tfrac{3-y}{2}\bigr)^2-1\Bigr]=\kappa+\frac{3\kappa^2}{4A}+O(\kappa^3/A^2).
\]
LeBrun therefore says exactly this: **one unit of Weyl deficit costs at least one unit of Yamabe excess**. The Yamabe overpayment υ − κ ≥ 3κ²/4A is a pure second-order effect.

## 3. Theorem 62.A (the Weyl-channel bound)

**Theorem 62.A.** Under the sign-family hypotheses, for every metric g on M = X#kCP̄² whose Weyl deficit satisfies κ = κ[g] ≤ 4A/9,
\[
\boxed{\;\frac{P(g)}{8\pi^2}\ \ge\ L_A(k,\kappa):=(k-\kappa)+\tfrac12\Bigl(A-\kappa-\sqrt{A^2-2A\kappa}\Bigr)
=(k-\kappa)+\frac{\kappa^2}{4A}+\frac{\kappa^3}{4A^2}+\cdots\;}
\]
For κ ≥ 4A/9, LeBrun's unconditional bound p ≥ k − A/3 is the minimum.

*Proof.* Use 62.1 together with υ ≥ υ_L(κ). Then
p ≥ k − (4/3)κ + (A/3)[((3−y)/2)² − 1] = k − κ + ½(A − κ − Ay),
since (A/3)·[(10 − 2κ/A − 6y)/4 − 1] = (A/12)(6 − 6y) − κ/6. The constraint κ ≤ 4A/9 is the condition y ≥ 1/3. Below that, the unconstrained LeBrun optimum t = c/9 of Step 36 is interior and gives k − A/3. ∎

Three consistency checks.
- (a) **Kähler metrics have κ ≤ 0.** For a Kähler ω on any complex structure of M (all are blow-ups of the minimal model by SW), ∫|W⁺|² = ∫s²/24 ≥ (4π²/3)(c₁·ω)²/ω². On the Kähler cone ω = π*ω_X − Σe_iE_i with e_i > 0, (c₁·ω)²/ω² = (K·ω_X + Σe_i)²/(ω_X² − Σe_i²) ≥ (K·ω_X)²/ω_X² ≥ A, the last step by Hodge index. So L_A ≥ k: **Theorem K∞'s Kähler tariff P ≥ 8π²k is the κ ≤ 0 case of 62.A.** Equality in the limit corresponds to κ → 0⁻ and υ → 0, which is the Arezzo–Pacard recovery.
- (b) **Certified cell:** κ = 0.0564 per class, so the bound is p ≥ 0.944 per class; the actual value is 0.9957. The slack (υ − υ_L)/3 ≈ (0.2124 − 0.0564)/3 = 0.052 is the Yamabe overpayment. The cell spends 3.77 times the Yamabe excess that LeBrun requires for its Weyl deficit. Its *LeBrun efficiency* is κ/υ = 0.265.
- (c) **Formal common mode** (h = k/A; Step 48 §2: axial W⁺ of magnitude x = 2/3 − h at s = −4, V̂ = 8π²A/(2−h)²):
  - ∫|W⁺|² = (4π²A/3)(2−3h)²/(2−h)² = (4π²A/3)(1 − 2h + h³/2 + …), so κ = k − k³/4A² + ….
  - υ = A[4/(2−h)² − 1] = k + 3k²/4A + k³/2A² + …, which equals υ_L(κ) through order k³/A². The formal mode is LeBrun-extremal with Π = 0.
  - p = k²/4A + k³/2A² + …, which equals L_A(k,κ) through order k³/A².
  - **The formal common mode lies on the equality locus of Theorem 62.A**, to the order computed. Its κ is k up to O(k³/A²).
  - Comparison: L_A(k,k) = ½(A − k − √(A²−2Ak)) = k²/4A + k³/4A² + …. This is the value of the bound at κ exactly equal to k, and it lies below the formal mode, as it must.

## 4. Corollaries: one conformal invariant governs the lower bound in the open range

Let κ_*(M) := sup_g κ[g] = A/2 − (3/8π²)·inf_g ∫|W⁺|². This is the conformal Weyl infimum, in normalised form.

**Corollary 62.B (sharp conditional k²/A law).** If inf_g ∫_M|W⁺|² ≥ (4π²/3)(A − 2k), i.e. κ_* ≤ k, then
\[
\alpha(M)\ \ge\ 4\pi^2\bigl(A-k-\sqrt{A^2-2Ak}\bigr)=\frac{2\pi^2k^2}{A}\Bigl(1+\frac kA+\cdots\Bigr).
\]
The leading constant 2π²/A (that is, p ≥ k²/4A) is the formal-common-mode constant, so it would be optimal among laws of this shape if the common mode could be realised. More generally, α(M)/8π² ≥ L_A(k, κ_*) whenever κ_* ≤ 4A/9. This gives a positive per-class tariff p ≥ ck as soon as κ_* ≤ (1−c)k.

**Corollary 62.C (coupled form; what a proof must establish).** Pointwise in g, Identity 62.1 makes the following three statements equivalent:
- (i) κ[g] ≤ k + βp(g̃);
- (ii) υ[g] ≤ k + (3+4β)p(g̃) (affine Yamabe susceptibility);
- (iii) ∫|W⁺|² + (β/3)P(g̃) ≥ (4π²/3)(A − 2k).

If any of them holds for all g with a uniform β ≥ 0, then α/8π² ≥ k²/((4+4β)A)(1 + O(k/A)).

*Proof.*
- κ = (3k + υ − 3p)/4 by 62.1.
- Let κ_max = k + βp. Since L_A is decreasing in κ for κ < 2A, we get p ≥ L_A(k, k+βp) ≥ −βp + (k+βp)²/4A.
- The strategist's linear version υ ≤ γp (no k term) gives instead κ ≤ (3k + (γ−3)p)/4, and hence the *tariff* p ≥ k/(γ+1). ∎

In the coupled form, with γ = 3 + 4β:
- The formal mode saturates (ii) with γ = 3: υ = k + 3k²/4A and 3p = 3k²/4A.
- The certified cell satisfies (ii) for every γ ≥ 0, since its υ = 0.212 < k.
- Kähler recovery has υ → 0.

So **every known object satisfies the affine susceptibility υ ≤ k + 3p, and the only object saturating it is the formal common mode.** The strategist's sup ΔV/P is unbounded along the formal mode (≈ A/k). The scale-free number that separates "positive tariff" from "k²/A law" is therefore **the Weyl deficit per class, κ/k**:
- κ/k < 1 − c for a tariff c;
- κ/k ≤ 1 + O(p/k) for the k²/A law.

The Yamabe excess is slaved to κ by LeBrun (υ ≥ κ + 3κ²/4A), so it is not an independent channel.

**Corollary 62.D (necessary structure of any family with p/k → 0).** Along such a family, 62.1 and 62.2 force:
- κ/k → 1, i.e. ∫|W⁺|² = (4π²/3)(A − 2k) + o(k): every exceptional class must remove (8π²/3) of self-dual Weyl energy;
- υ − κ = o(k): asymptotic equality in LeBrun's Prop. 4 with Cauchy–Schwarz, i.e. |W⁺| ≈ |s|/√6·const with s ≈ const, which is LeBrun's special almost-Kähler equality structure;
- Π = o(k): almost all exceptional periods |E_i⁺|² and |K⁻|² vanish.

The last condition is exactly what Taubes' period constraint (Lemma T, Step 47) prevents for an exact closed common mode. **The obstruction to P/k → 0 therefore lies in the joint smallness of κ-shortfall, LeBrun slack and periods, not in any single one.** This sharpens Step-48 Cor. Y1 (Δ V ≥ 2π²(1−c)k) to the statement that the Yamabe excess must be matched one-for-one by Weyl deficit.

## 5. The ASD-side reformulation and what is known

Since ∫|W⁺|² − ∫|W⁻|² = 12π²τ(M) = 12π²(τ_X − k), Cor. 62.B's hypothesis reads
\[
\inf_g\int_M|W^-|^2\ \ge\ \tfrac{4\pi^2}{3}(A-9\tau_X)+\tfrac{28\pi^2}{3}k .
\]
For a ball quotient (A = 9τ_X) this is **inf ∫|W⁻|² ≥ (28π²/3)k = (7/9)·12π²·k**: every exceptional class must carry at least 7/9 of the anti-self-dual Weyl energy of a Fubini–Study CP̄² summand.

Values of the per-class anti-self-dual Weyl energy:
- conformal CP̄² connected sums and Burns cells (Burns is conformal to CP̄² minus a point): ≈ 12π²;
- certified cell: 12π² − δW = (12 − 0.150)π² per class;
- formal mode: (28/3)π², i.e. the bound is saturated.

For a positive per-class tariff it suffices that inf ∫|W⁻|² ≥ λ·12π²k with λ > 7/9 + (something); precisely, the tariff is c = 1 − (9/2)(1−λ). For ball quotients, the trivial signature bound ∫|W⁺|² ≥ 12π²τ_M gives only κ ≤ 9k/2, which is useless.

**Gursky analogy (positive Yamabe).**
- Gursky: for b⁺ > 0 and Y > 0, ∫|W⁺|² ≥ (4π²/3)(2χ+3τ). On a blow-up this permits a reduction of at most (4π²/3) per CP̄² summand, which is *half* the (8π²/3) that Cor. 62.B needs to exclude.
- On CP²#kCP̄² this per-point bound is nearly sharp. 12π²/(4π²/3) = 9, and scalar-flat Kähler (hence ASD) metrics exist on CP²#kCP̄² for k ≥ 10 (Kim–LeBrun–Pontecorvo, Rollin–Singer), giving an average of 1.2π² per point.
- **Conjecture 62.G** (the negative-Yamabe, SW analogue of Gursky's per-point law): on X#kCP̄²,
  inf ∫|W⁺|² ≥ (4π²/3)(A − k) = (4π²/3)(2χ+3τ)(M).
  This would give κ_* ≤ k/2, hence the per-class tariff α ≥ 4π²k(1 + O(k/A)), i.e. c = ½.
- The weaker Conjecture 62.W (κ_* ≤ k) gives the sharp k²/A law.
- Both conjectures predict that the Taubes threshold for ASD metrics on X#kCP̄² is at least A (resp. A/2).

Every Seiberg–Witten consequence used so far points the same way: each is a lower bound on the Yamabe excess in terms of the Weyl deficit.
- Theorem Y, rewritten with 62.1, reads κ ≤ υ − (3/16π²)∫Ψ.
- LeBrun reads υ ≥ υ_L(κ).
- Theorems N/W/K are saving upper bounds, which is the same direction.

None of them bounds κ itself. Neither conjecture can come from SW and the Weitzenböck formulas alone, because Taubes' ASD metrics exist on X#kCP̄² for k ≫ 1 while SW ≠ 0. **Any proof must see the exceptional classes, i.e. k, in the Weyl channel itself**, not only through the sign family's (a⁺)² ≥ A. This explains structurally why every field-theoretic attempt (Steps 36–48) stopped at LeBrun's 2/3: those identities constrain only (υ, κ) through (62.2), never κ alone.

Sources to check (knowledge request s62): Gursky's inequality and its negative-Yamabe status; whether KE minimises ∫|W|² on general-type surfaces; explicit Taubes thresholds; ASD metrics on blow-ups of general-type surfaces; LeBrun's equality analysis in Prop. 4 [27].

## 6. What this changes

1. The open-range problem C₊ ≥ A − (1−c)k is equivalent to a bound on κ along near-minimisers, and the coupled form 62.C is exactly what is needed. The Yamabe-susceptibility route (Route 2) and the strategist's ΔV/P are the same statement as 62.C(ii). Its natural sharp constant γ = 3 is the formal mode; its natural tariff version is a bound on κ/k.
2. The K+Y+Cauchy–Schwarz combination proposed by the strategist gives δ − d ≥ (5/6)d²/(A+δ) (in δ = υ, d = k − p). Together with 62.C(ii) at γ = 3 this yields only p ≥ (5/24)d²/(A+υ). **The sharp 1/(4A) comes from LeBrun's Prop. 4, not from Theorem K/Y**: Theorem K's Cauchy–Schwarz loses the factor 5/6.
3. Decisive computations, chosen to change judgement:
   - (a) **κ-capacity of cells.** For the CH-collared Burns/perpendicular family (A01 data) and the rotated cells, compute (κ, υ, p) per class and the two efficiencies κ/k and κ/υ. Ask whether any local cell has κ ≥ 1 per class at bounded p. If not, find what bounds κ locally; a local Weyl-capacity bound would be the first piece of a proof of 62.W.
   - (b) **Local susceptibility near KE.** Near the KE host, κ ≈ Q_W(h) and p ≈ ‖Lh‖² are both quadratic in the TT/conformal deformation (KE is Bach-flat, hence critical for ∫|W⁺|²). Is Q_W ≤ βQ_P with β explicit (Koiso gap / A_C)? That would give 62.C(i) in the A_C neighbourhood with explicit β.
   - (c) **Construction side.** Configurations violating 62.W need κ > k: conformal structures that remove more than (8π²/3) of W⁺ energy per CP̄² summand. ASD-gluing (Taubes, Donaldson–Friedman) is the natural mechanism. Counting how many CP̄² summands an unobstructed ASD gluing on X needs is the decisive question.

## 7. Two efficiencies, the Burns breakeven 1/4, and the equality locus

Define per exceptional class two quantities:
- the Weyl capacity κ̂ = κ/k;
- the LeBrun efficiency η = κ/υ. LeBrun gives η ≤ 1 + O(κ/A).

Identity 62.1 then reads
\[
p/k = 1-\hat\kappa\,\frac{4-1/\eta}{3}.
\]
So a configuration saves against the unit tariff **iff η > 1/4**, and the saving is linear in κ̂.

**Cell family data.** The values below are read from the existing ledgers `workspace/data/cell_yamabe_rv_ch_x*.json`, using the larger-N rows. In each, ω = −fourWplus_rel, υ = 3·scalar_channel and κ = 3ω/4. All are floats, not interval values.

| x₀ (X) | κ | υ | η = κ/υ | p from 62.1 | p ledger |
|---|---|---|---|---|---|
| 0.003 (64) | 0.0047945 | 0.018563 | 0.2583 | 0.9997952 | 0.9997952 |
| 0.01 (64) | 0.017247 | 0.065087 | 0.2650 | 0.9987004 | 0.9987004 |
| 0.03 (128) | 0.056351 | 0.212390 | 0.2653 | 0.9956627 | 0.9956627 |
| 0.05 (128) | 0.093971 | 0.364746 | 0.2576 | 0.9962875 | 0.9962875 |

In the same table, the Kähler blow-up family has κ = −Π/2 ≤ 0 and υ = Π, and the formal common mode has κ̂ ≈ 1, η ≈ 1.

The table gives an exact reading of the CH-cell family: **the cells have LeBrun efficiency barely above the breakeven 1/4.** As x₀ grows, η falls back toward 1/4. That is why the saving changes sign near x₀ ≈ 0.065.

**Theorem F reinterpreted.** From the first-order chiral split c_A = −4π²(M_ζ/6, 1/√12) (59.R), a Burns insertion in direction ζ changes the two channels as follows:
- ∫4|W⁺|² by −8π²εW⁺(ζ,ζ);
- ∫s²/12 by +8π²ε|s|/12.

Hence its first-order efficiency is η_B(ζ) = 3W⁺(ζ,ζ)/|s|, and R⁺(ζ,ζ) = (|s|/3)(η_B − 1/4). So "Burns saves at first order" is the same statement as "its efficiency exceeds 1/4", and the minimizer rigidity R⁺ ≤ 0 says that no Burns direction exceeds efficiency 1/4. On CH the perpendicular direction has η_B = 1/4 exactly (the kernel). The second-order log term raises η slightly above 1/4, which is the small saving in the data. To go from efficiency 1/4 (local Burns) to the efficiency 1 permitted by LeBrun, one needs diffuse reduction of the |W⁺| magnitude, which is the formal mode.

**Equality locus of 62.A.** Equality requires two things:
- equality in LeBrun's Prop. 4. By LeBrun's Prop. 2.4 (Knowledge `Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory…`, lines 243–257), g is then almost-Kähler, ω lies in the lowest eigenspace of W⁺, s + s* is constant, c₁ is of type (1,1), and W⁺ is J-invariant;
- the Cauchy–Schwarz step, which forces s and |W⁺| to be constant.

At s = −4 this gives W⁺ = (−2a, a, a) constant with ω on the eigenvalue −2a, s* = s/3 − 8a, and s* − s = 8/3 − 8a ∝ |∇ω|² ≥ 0. Hence a ≤ 1/3, with κ > 0 exactly when J is strictly almost-Kähler: κ = A/2 − (3/8π²)·6a²·Vol.

**So a family with p/k → 0 must approach compact strictly almost-Kähler metrics with constant s, constant J-invariant degenerate W⁺ and harmonic J (Ω an eigenform of W).** LeBrun (2001) left open whether any compact strictly almost-Kähler metric saturates the estimate. Apostolov–Armstrong–Drăghici (Knowledge `Local-models-and-integrability…`, Thm 2) prove that a compact almost-Kähler metric satisfying the third Gray condition (harmonic J together with J-invariant Ricci) is Kähler. Our locus has harmonic J and J-invariant W⁺, but J-invariance of Ricci has not been checked.

**Proof route opened.** Proceed in three steps:
1. Determine whether the equality conditions together with constant s and constant |∇J| force J-invariant Ricci, or integrability directly. The relevant tools are the Apostolov–Armstrong "Hermitian Weyl tensor" results and Blair's formula.
2. If the equality locus is Kähler only, it has κ ≤ 0.
3. A quantitative stability of that rigidity would then bound κ by the LeBrun slack, which turns 62.A into a genuine lower bound.

The formal common mode is a pointwise algebraic solution of these equality conditions that no compact metric realises. Taubes' period constraint and AAD-type integrability are the two candidate obstructions, and comparing them is decisive.
