# Superseded scope note (Step 8)

Step 8 verified the Derdziński factor but repaired the strength of the conclusion. For varying-topology LeBrun near-boundary sequences, the supported result is only
\[
\operatorname{Vol}\{p:\operatorname{Vol}B_1(p)\ge v\}/\operatorname{Vol}M\to0
\]
for every fixed `v>0`, not `sup_p Vol B_1(p)->0` and not pointwise disappearance of every noncollapsed island. The explicit gap density in `step8_derdzinski_measure_local_theorem.md` also replaces the undefined `Q,P` notation. For fixed `A` critical-boundary manifolds, absolute defect vanishing can give the stronger sup statement. The original Step 7 content below should be read through this Step 8 correction.

# Step 7 CORRECTED: Derdziński Local Contradiction and Noncollapsed Exclusion

## Critical Corrections (from TTCS verifier + S0910A03 #224)

### Correction 1: Bochner coefficients
The correct scalar Bochner formula on an Einstein 4-manifold is:
$$
\frac12 \Delta|W^+|^2 = |\nabla W^+|^2 + \frac{s}{2}|W^+|^2 - 6\,\mathrm{tr}(W^+)^3.
$$
(Confirmed by S0910A03 msg #224: Δ|W⁺|² = 2|∇W⁺|² + s|W⁺|² − 36 det W⁺.)

The earlier coefficients (s/3, −4) were wrong but passed ℂℍ² and ℂP² checks because
both have the same ratio b/a = −12. The corrected |∇W⁺|² at the calibrated target
(1/12, 1/12, −1/6) with s = −4 is **1/16** (not 1/24). The qualitative conclusion
is unchanged: |∇W⁺|² > 0, the calibrated profile is Bochner-consistent but not parallel.

### Correction 2: Derdziński conformal factor (KEY)
**The initial Step 7 analysis was WRONG about the local/global distinction.**

The Derdziński conformal factor is NOT an arbitrary positive function satisfying the
scalar curvature equation Δf = −f/2. It is **uniquely determined** by the Kähler
integrability condition and equals:
$$
g_K = C\,|w|^{2/3}\,g
$$
where w is the lowest eigenvalue of W⁺. (TTCS verifier; requires primary-source
verification against Derdziński 1983, Compositio Math. 49, 405–433.)

When the eigenvalues of W⁺ are constant (as on the calibrated Einstein limit where
w = −1/6), the factor |w|^{2/3} is constant. Therefore g_K ∝ g, and **g itself is
locally Kähler**.

For Kähler-Einstein with Ric = −g: |W⁺|² = s²/24 = 2/3. But the calibrated
|W⁺|² = 1/24. **This is a LOCAL contradiction.** No compactness or Stokes theorem
is needed.

**The initial note's conclusion that "the argument is inherently global" was wrong.**

---

## Corrected Structural Picture

### The complete noncollapsed-exclusion argument

1. **Near-equality**: D_a/A → 0 for a hypothetical near-boundary LeBrun sequence
   with k/A → 1/3, δ → 0.

2. **Cauchy-Schwarz remainder**: ∫(s+8√6|W⁺|)² ≤ 864π²D_a forces s → −4 and
   |W⁺| → 1/(2√6) in A-normalized L² sense.

3. **Tensor slack estimate**: The integral ∫ξ(Q+P) ≤ 24π²D_a where ξ = w +
   √(2/3)|W⁺| ≥ 0 is the tensor slack and Q+P ≈ 6 at the target. So
   ∫ξ ≤ 4π²D_a in the A-normalized sense.

4. **Volume-random basepoint** (Strategist): For fixed R > 0:
   E[∫_{B_R(p)} ξ_i] ≤ C(R)/Vol · ∫ξ_i → 0.
   Typical R-balls have arbitrarily small total tensor slack.

5. **Cheeger-Naber harmonic radius** (Thm 1.13): On a noncollapsed ball
   (Vol(B₁(p)) ≥ v > 0) with |Ric| ≤ 3: the harmonic radius satisfies
   Vol(T_r({r_h ≤ r}) ∩ B₁) ≤ C(v)r⁴. Most of the ball has controlled
   harmonic radius.

6. **W²,p convergence** (Strategist): In harmonic coordinates with r_h ≥ r₀:
   C^{1,α} convergence from Arzelà-Ascoli; Ric(g_i)+g_i → 0 plus Schauder
   estimates give C^{2,α} convergence; the limit is smooth Einstein with Ric = −g.

7. **Pointwise passage**: On the smooth limit ball, s_∞ = −4 (Einstein) and
   the Cauchy-Schwarz remainder gives |W⁺_∞| = 1/(2√6) constant. The tensor
   slack ξ_∞ = 0 (from L¹ vanishing + continuity + nonnegativity). Therefore
   W⁺_∞ has exactly the two-eigenvalue profile (1/12, 1/12, −1/6).

8. **Derdziński local contradiction**: Two-eigenvalue W⁺ + constant |W⁺| on an
   Einstein manifold → Derdziński factor |w|^{1/3} = const → g is locally Kähler
   → |W⁺|² = 2/3. But |W⁺|² = 1/24. **CONTRADICTION.**

9. **Conclusion**: Every noncollapsed smooth region of a near-boundary LeBrun
   sequence leads to a contradiction. Any surviving sequence must be **entirely
   collapsed** (Vol(B₁(p)) → 0 for all p).

### The remaining gap

The negative-branch four-dimensional argument is now reduced to:

> **Can a closed 4-manifold M = X#k C̄P² with k/A → 1/3 carry a metric with
> Ric ≈ −g and Vol(B₁(p)) → 0 for ALL p?**

Constraints on collapsed geometry under Ric ≈ −g:
- Volume bound: Vol(M) ≥ cA from CGB, so the manifold has large total volume
- No diameter bound (unlike positive branch, no Myers)
- Large total volume + collapsed at all points → manifold is "spread thin"
  over a large-diameter base with thin fibers
- S0910A03 (msg #218): product hyperbolic surface collapse has |W⁺| = 2/√6,
  excluded by the calibrated profile |W⁺| ≈ 1/(2√6)
- All known collapse models under Ric = −g are excluded by the Weyl profile
- S0910A02 (msg #225-226): chi-obstruction for free S¹ collapse (chi = 0 vs
  tight pinching requires chi > 0 in 4D)

The Weyl profile filter + Euler characteristic constraints may suffice to exclude
all possible collapse modes, but this remains to be proved.

---

## Caveat on the Derdziński factor

The claim g_K = C|w|^{2/3}g is from the TTCS verifier. It is consistent with:
- ℂℍ² (parallel W⁺, f = const, Kähler-Einstein) ✓
- Page metric (non-constant |W⁺|, non-constant f, conformally Kähler) ✓
- The conformal weight analysis (eigenvalue matching) ✓

But it requires verification against the original Derdziński 1983 paper or
the Oliveira-Sena-Dias "Einstein metrics via Derdziński duality" construction.
The Numdam issue page for Compositio 49(3) was accessible; the paper should be
downloaded and checked.

If the claim is incorrect (i.e., the Derdziński factor is not |w|^{1/3} but
some other function), the local contradiction would need to be re-evaluated.
The GLOBAL Armstrong argument on compact manifolds remains valid regardless.

---

## Files
- Corrected script: `workspace/scripts/step7_corrected_bochner_derdzinski.py` (all checks pass)
- Original (superseded) script: `workspace/scripts/step7_bochner_conformal_kahler.py`
- Original (superseded) note: `workspace/notes/step7_local_vs_global_rigidity.md`
- TTCS results: `trace/ttcs/results/step7_ttcs01_*_integration.md`
