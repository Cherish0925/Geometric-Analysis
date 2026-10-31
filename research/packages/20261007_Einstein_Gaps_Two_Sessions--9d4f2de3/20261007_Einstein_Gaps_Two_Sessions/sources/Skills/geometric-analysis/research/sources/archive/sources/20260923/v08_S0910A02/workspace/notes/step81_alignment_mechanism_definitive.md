# Step 81: Definitive analysis of the harmonic-form alignment mechanism

> **Status:** The mechanism is alive but unproved. The gap is exactly √(3/2) ≈ 22.5%.

## 1. The exact chain

**Conventions** (all pinned to Wu/LeBrun and Gursky–LeBrun sources):
- W⁺: endomorphism of Λ⁺, eigenvalues α ≥ β ≥ γ, α+β+γ = 0.
- |W⁺|² = α²+β²+γ² ≥ (3/2)α² (Wu/LeBrun Lemma 2; equality iff β = −α/2).
- Weitzenböck on SD 2-forms: (d+d*)²ω = ∇*∇ω − 2W⁺(ω) + (s/3)ω.
- CGB for Einstein (E=0), χ=8, τ=0, Ric=3g, s=12:
  ∫|W⁺|² = 32π² − 3V.  Bishop: V ≤ 8π²/3 (strict for M ≠ S⁴).

**Q-orthonormal basis.** For self-dual harmonic forms, the intersection form coincides with the L² inner product. A Q-orthonormal basis {ω₁,ω₂,ω₃} satisfies ∫⟨ωₐ,ωᵦ⟩ = δₐᵦ. Define T = Σₐ ωₐ⊗ωₐ (nonneg symmetric endomorphism of Λ⁺). Then ∫trT = b₊ = 3.

**Summed Weitzenböck:**
$$\int|\nabla\Omega|^2 + \frac{s}{3}b_+ = 2\int\langle W^+, T\rangle, \qquad |\nabla\Omega|^2 := \sum_a|\nabla\omega_a|^2.$$

**Von Neumann / Ky Fan bound:** ⟨W⁺, T⟩ ≤ α t₁ + β t₂ + γ t₃ where t₁ ≥ t₂ ≥ t₃ ≥ 0 are eigenvalues of T in the W⁺-eigenbasis. At θ = t₂/trT = 0 (rank-1 T): ⟨W⁺,T⟩ ≤ α·trT.

**Cauchy–Schwarz:**
$$\int\alpha\cdot\text{tr}\,T \le \sqrt{\frac{2}{3}}\left(\int|W^+|^2\right)^{1/2}\left(\int(\text{tr}\,T)^2\right)^{1/2}.$$

**Concentration factor:** κ² = V·∫(trT)²/(∫trT)² ≥ 1 (Jensen).

**Full chain:** Dropping ∫|∇Ω|² ≥ 0:
$$\frac{s}{3} \le 2C_\theta\cdot\kappa\cdot\sqrt{A}, \qquad A := \int|W^+|^2/V, \qquad C_0 = \sqrt{2/3}.$$

**b₊ cancels.** At θ = 0 and κ = 1, the chain reads:
$$4 \le 2\sqrt{\frac{2}{3}}\sqrt{A}, \qquad\text{i.e.,}\quad A \ge 6, \quad\text{i.e.,}\quad \int|W^+|^2 \ge 6V = \int\frac{s^2}{24}.$$
This is **exactly** the Gursky–LeBrun theorem (Theorem 1 of the positive-sectional source, line 207). The dimension of the harmonic SD space plays no role.

**Margin for χ=8, τ=0 rows.** At Bishop volume V = 8π²/3: A = 9, and the chain gives 4 ≤ 2√6 ≈ 4.899. The deficit factor is √(3/2) ≈ 1.2247, i.e., the upper bound exceeds the lower bound by 22.5%.

**Convention check:** on Kähler–Einstein CP² (χ=3, τ=1, V = 2π², A = 6), the chain is exact equality (verified numerically).

## 2. Why the gap cannot be closed by existing tools

### 2.1. The degeneracy defect

Wu/LeBrun Lemma 2: |W⁺|² ≥ (3/2)α² with equality iff β = −α/2 (Kähler eigenvalue pattern). By Derdziński, this holds everywhere iff ∇W⁺ = 0 (locally symmetric/Kähler). On b₊ ≥ 2 Einstein manifolds, ∇W⁺ ≠ 0, so β ≠ −α/2 on a set of positive measure.

This means the Cauchy–Schwarz factor C₀ = √(2/3) is not tight: the actual ratio α/|W⁺| < √(2/3) on the set where β ≠ −α/2. But the quantitative improvement requires:
- A measure-theoretic lower bound on the set {β ≠ −α/2}
- A pointwise gap: how far β is from −α/2 on this set

Neither is controlled by any known estimate.

### 2.2. The isotropy of T

For b₊ = 3, by Aronszajn unique continuation, each ωₐ vanishes on a set of measure zero. So at a.e. point, at least one form is nonzero, and T has rank ≥ 1. For b₊ ≥ 2, T has rank ≥ 2 at a.e. point where two forms are simultaneously nonzero (which is a.e., since two independent analytic forms on a 4-manifold have codimension-4 intersection of zero sets).

With rank T ≥ 2: θ = t₂/trT > 0, and the C_θ bound improves. But the improvement requires a **lower** bound on the pointwise isotropy θ, which depends on the Weitzenböck PDE and is not controlled by topology.

### 2.3. The θ-threshold

At A = 9 (Bishop volume), the chain closes at θ* ≈ 0.127. This means the (|W⁺|·trT)-weighted average isotropy must exceed ~12.7% for a contradiction. At smaller V (larger A):

| A  | θ*     | Comment |
|----|--------|---------|
| 6  | 0      | Gursky–LeBrun exact |
| 9  | 0.127  | Bishop bound for χ=8 |
| 12 | 0.211  | V ≈ 2/3 V_Bishop |
| 18 | 0.333  | Equals max possible θ = 1/3 |
| >18| impossible | Chain cannot close even with isotropic T |

For V < V_Bishop/2 (i.e., A > 18), the alignment mechanism fails completely regardless of isotropy.

### 2.4. The CLR / spectral reformulation (TTCS-corrected)

The Weitzenböck operator L = ∇*∇ − 2W⁺ + (s/3) = H − Q on Γ(Λ⁺), where H = ∇*∇ + (s/6) and Q = 2W⁺ − (s/6)Id.

**Two TTCS corrections:**
(i) The potential can have TWO negative eigenvalues simultaneously (when both α > s/6 and β > s/6).
(ii) Standard CLR counts strictly negative eigenvalues, NOT zero modes. Since our b₊ zero modes sit at the threshold λ = 0, a coercive shift is needed: apply CLR to H − Q₊ using the Yamabe–Sobolev inequality ⟨Hφ,φ⟩ ≥ (Y/6)‖φ‖₄².

The corrected formulation:
$$b_+ \le \frac{C_{\rm CLR}}{Y^2}\int\operatorname{tr}\bigl(2W^+-\tfrac{s}{6}I\bigr)_+^2\,dV.$$

On Kähler–Einstein CP²: Q₊ = diag(2,0,0) is 1D, ∫tr Q₊² = 4V, Y² = 144V, giving C_CLR ≥ 36 (accommodates b₊ = 1). For b₊ = 3 and tr Q₊² ≤ 4|W⁺|²: need C_CLR < 12 to get f(3) > 9.

The compact-manifold constant is expected to be much larger than 12.

### 2.5. The T-equation and anisotropy (TTCS generator)

T satisfies the exact PDE (from summing ωₐ Weitzenböck):
$$\nabla^*\nabla T = BT + TB - 2S, \qquad S = \sum_i(\nabla_i\Omega)(\nabla_i\Omega)^* \ge 0.$$

Defining u = trT, P = T/u, K = ∫|∇Ω|², and Θ_T = (V/9)∫u²·tr(P−I/3)², the precise target is:
$$(K+12)^2 / (36\Theta_T) > 9.$$

This is the **strongest known formulation**: it uses the gradient energy K (dropped from the crude chain), the concentration of u (via κ), and the anisotropy of P. The decisive question: does three-lump concentration pay enough K to compensate the growth of Θ_T?

### 2.6. Gram degeneracy and p₁(Λ⁺) (TTCS generator)

p₁(Λ⁺)[M] = 2χ + 3τ = 16 ≠ 0 for (χ,τ) = (8,0). If Ω: ℝ³ → Λ⁺ were everywhere invertible, Λ⁺ would be trivial and p₁ = 0. So det Ω must vanish somewhere. A quantitative "transgression theorem" controlling Chern–Simons boundary terms at the degeneracy set would convert the topological charge 16 into Weyl energy.

### 2.7. The maximum principle constraint

At the maximum of |ωₐ|², the Bochner formula gives α(p_max) ≥ s/6 = 2. On b₊ ≥ 2: no harmonic SD form can have constant norm (would force Kähler). So max|ωₐ|² > 1/V strictly, but no universal quantification of the gap.

## 3. The frontier

### What is proved:
1. **b₊ cancels from the crude Weitzenböck chain.** The chain at θ=0, κ=1 is exactly Gursky–LeBrun: ∫|W⁺|² ≥ 6V, independent of b₊.
2. **The margin is 22.5%** for χ=8, τ=0 at Bishop volume. Exact, verified against CP² calibration.
3. **The equality case is topologically excluded:** Kähler forces b₊ = 1, excluded on the mixed rows.
4. **The strict inequality is guaranteed** but not quantified.

### What would close the gap:
A **b₊-dependent Weyl energy inequality**: ∫|W⁺|² ≥ f(b₊)·V for positive Einstein, with f(3) > 9.

Equivalently:
- (A) A quantitative Derdziński defect for non-conformally-Kähler Einstein metrics
- (B) A quantitative isotropy bound θ̄ > 0.127 from the Weitzenböck PDE
- (C) A compact-manifold CLR bound with C_CLR < 12 (corrected threshold after TTCS coercive shift)

Each would be a theorem about positive Einstein 4-manifolds in its own right. None follows from known techniques.

### Evidence for the conjecture:
- All known compact positive Einstein 4-manifolds have min(b₊, b₋) ≤ 1.
- The equality case is characterized (conformally Kähler/locally symmetric).
- The gap is moderate (22.5%), not orders of magnitude.
- The asymmetry between near-pinching (C⁰ sequences) and exact Einstein (real-analytic, ε-regularity, fixed ∫|Rm|²) strongly favors the nonexistence side.

### Evidence against the conjecture:
- No technique gives any quantitative improvement from Gursky–LeBrun for b₊ ≥ 2.
- The three-lump concentration defeats the isotropy parameter θ and the concentration parameter κ simultaneously.
- The CLR approach requires spectral constants far beyond what is known.

## 4. Connection to Yau–26 (Step 82 correction)

The mixed positive-mirror rows have near-pinched metrics δ(g_a) = O(1/|log a|) → 0. If **any one** such row admits no Einstein metric of any sign, P₄⁺ is refuted. A fixed-row refutation is therefore a three-leg conjunction: exclude λ > 0, λ = 0, and λ < 0 on the same smooth manifold.

**λ > 0:** the alignment/Gram/T-anisotropy mechanisms are sign-locked to this leg, because their starting inequality uses the positive scalar term in the harmonic self-dual Weitzenböck formula. The crude summed chain and the naive CLR reformulation do not close; they reduce to Gursky–LeBrun plus the TTCS-corrected thresholds recorded above.

**λ = 0 (Ricci-flat):** Step 82 source-checks show that this leg cannot be banked as closed. Known/special-holonomy cases are excluded on the χ=8 simply connected rows: flat holonomy gives χ=0, reducible Ricci-flat products cannot occur on a compact simply connected 4-manifold with χ=8, and SU(2)/hyperkähler compact 4-manifolds are flat tori or K3 surfaces (χ=24 for K3). However, the general existence of compact irreducible Ricci-flat metrics with generic SO(4) holonomy is a known open problem; sources explicitly state that classification of closed Ricci-flat 4-manifolds is unsolved and that only examples finitely covered by T⁴ or K3 are known. Thus χ=8 excludes all currently known Ricci-flat mechanisms but not a theorem-level generic-SO(4) loophole.

**λ < 0:** the Chern–Weil formulas depend on λ², not on the sign of λ:
\[
\int|W^\pm|^2=2\pi^2(2\chi\pm3\tau)-\frac13\lambda^2V,\qquad
\int|W|^2=8\pi^2\chi-\frac23\lambda^2V.
\]
The earlier statement that negative Einstein gives \(\int|W|^2>64\pi^2\) was wrong. Existing negative-Einstein nonexistence tools again require monopole/symplectic/algebraic input absent on these PSC, SW-void, non-Kähler mixed rows. The alignment mechanism is vacuous for s≤0.

## 5. Files and verification

- Exact chain data: `workspace/data/step81_alignment_chain_exact.json`
- Spectral analysis: `workspace/data/step81_spectral_analysis.json`
- Convention checks: S⁴ CGB ✓, CP² volume ✓, CP² Weitzenböck ✓
- Numerical: C₀ = √(2/3) = 0.8165, argmax at β/α = −1/2 (Kähler) ✓
- θ* = 0.127 at A=9, monotone increasing, reaches 1/2 at A=24 (TTCS-corrected from θ_max=1/3, A=18)

## 6. Source references

- Wu/LeBrun, "Einstein Manifolds, Self-Dual Weyl Curvature, and Conformally Kähler Geometry": Lemma 2 (line 134), Weitzenböck (line 141), Theorem 2.1 (line 148), Proposition 2.2 (line 181), Proposition 2.3 (line 191)
- Gursky–LeBrun, "On Einstein Manifolds of Positive Sectional Curvature": Theorem 1 (line 207), refined Kato (line 189), Derdziński Bochner (line 192)
- Gursky, "The Weyl Functional on 4-Manifolds of Positive Yamabe Invariant": positive-Yamabe bound (lines 88–102)
- Derdziński: conformally Kähler classification (via Wu/LeBrun line 174)
