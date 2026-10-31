# TTCS Independent Branch Record

```json
{
  "step_id": 21,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/h4_cell_channel_analysis.py",
    "Sessions/S1003A02/workspace/data/h4_cell_channels.json",
    "Sessions/S1003A01/workspace/scripts/h4_perp_cell.py",
    "Sessions/S1003A01/workspace/notes/step18_corrected_riccati_and_H4_comparison.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md"
  ]
}
```

## Task

Check the hyperbolic-cell channel identities and numerical interpretation. The normalization is Ric=-6, scalar -24, sectional curvature -2. Verify algebraically that for an exact-H4-collar one-blow-up cell, P/(8pi^2)-1 = 4 int W+^2/(8pi^2) + [int s^2/12 - 48 Vol(B)]/(8pi^2), and J/(8pi^2)-1 = that Weyl term + int(s+18)^2/3/(8pi^2) + [36 Vol(U)-48 Vol(B)]/(8pi^2). Read the script/data and assess whether the reported X=64 cells support the claim that no volume-saving/scalar-near--18 mechanism appears in the tested diagonal family. Identify any normalization or volume-factor error.

## Output

# Hyperbolic-cell channel identities: verification memo

## Summary

Both identities are correct for the stated normalization (Ric = −6g, s = −24, sectional curvature −2), with one condition: **W⁺ must be the Weyl half for the orientation in which the bolt is a (−1)-sphere, i.e. τ(U) = −1.**

The script's volume factor, ball volume and collar matching are correct. The comment saying chirality is "fixed by W⁺ = 0 on the collar" does not fix anything, because both W⁺ and W⁻ vanish on H⁴.

The X = 64 data reproduce the Theorem F first-order law exactly in the scalar–volume channel. The W⁺ channel is O(x₀²) and positive. The cells pay for extra volume rather than save it.

The "s ≈ −18" statistics are not evidence in either direction:
- the cells were optimized for P, not J;
- J ≥ P holds pointwise;
- the pointwise scalar attractor of the P-identity is s = 0, not −18.

All data lie at x₀ ≤ 0.03. This is the perturbative corner, where the outcome is already fixed by first-order theory.

## 1. Derivation of the identities

With endomorphism norms, the closed-manifold Chern–Weil formulas are

- 8π²χ = ∫(|W|² − ½|Ric°|² + s²/24),
- 12π²τ = ∫(|W⁺|² − |W⁻|²).

The combination 2χ + 3τ eliminates W⁻:

  8π²(2χ + 3τ) = ∫(4|W⁺|² − |Ric°|² + s²/12).

The normalization was checked against CH²: |W⁺|² = 16 + 4 + 4 = 24 and s²/24 = 24, giving Gauss–Bonnet density 6/π², as in Lemma R.

**Comparison of U with the H⁴ ball B.** Both carry the same metric 2-jet on ∂U = ∂B, so the Gauss–Bonnet and signature transgression terms cancel in the difference. Then

  P(U) − P(B) = 4Δ∫|W⁺|² + Δ∫s²/12 − 8π²(2Δχ + 3Δτ).

The ingredients are:
- B is Einstein and conformally flat, so P(B) = 0 and W⁺(B) = 0.
- ∫_B s²/12 = 48 Vol(B).
- One blow-up gives (Δχ, Δτ) = (1, −1), so 2Δχ + 3Δτ = −1.

This yields the first identity:

  P/8π² − 1 = 4∫_U|W⁺|²/8π² + [∫_U s²/12 − 48 Vol(B)]/8π².

**Second identity.** We have J = P + ¼∫(s+24)², since |Ric + 6g|² = |Ric°|² + (s+24)²/4. The pointwise identity

  (s+24)²/4 = (s+18)²/3 − s²/12 + 36

(both sides equal s²/4 + 12s + 144) then gives

  J/8π² − 1 = 4W⁺ + ∫(s+18)²/3 + 36 Vol(U) − 48 Vol(B).

This holds exactly, for every metric on the cell with the exact collar.

**Chirality.** H⁴ has W⁺ = W⁻ = 0, so the collar cannot select a chirality. The identity holds only in the orientation with τ(U) = −1.

In the opposite orientation one must use 2χ − 3τ, with 2Δχ − 3Δτ = 5:

  4∫|W⁻|²/8π² = P/8π² + 5 − (scalar-volume) ≈ 6.

That large W⁻ is the anti-self-dual Weyl curvature carried by the bolt.

The script never evaluates the Weyl tensor; four_Wplus_rel_norm is defined as a residual. Its positivity is therefore a consistency test of the topological constant. A wrong constant would make it ≈ −4. A direct coordinate evaluation of |W⁺|² and |W⁻|² would turn this residual into an independent measurement and settle the chirality explicitly.

## 2. Code and normalization

**Volume factor.** The metric is dx²/(4G) + Fσ₁² + xσ₂² + xe^w σ₃², with ∫σ₁₂₃ = 2π² (unit S³ for dσᵢ = 2σⱼ∧σₖ).
- Since dt = dx/(2√G), dV/8π² = abc/(8√G) dx with abc = √F·x·e^{w/2}. This is exactly `v8`.
- `vol` in `h4_perp_cell.py` is abc/(2√G) = 4·v8. Hence P-density = vol·|Ric°|²/4 and scalar density = vol·(s+24)²/16, both correctly normalized by 8π².

**J residual (~10⁻¹³).** Algebraically, this residual equals scalar_part − ∫v8 (s+24)²/4. It therefore independently confirms that `v8` agrees with the SymPy volume factor and that `SC` is the same s used in `SD`. It does not test the topological constant or Vol(B).

**Ball volume.** In the H⁴ collar, dV/8π² = x/(8√(1+2x)) dx. Substituting y = √(1+2x) gives ∫(y²−1)/16 dy, so

  Vol(B)/8π² = Y³/48 − Y/16 + 1/24, Y = √(1+2X).

At X = 64 this is 29.85594, matching VB_norm. The collar itself satisfies (dx/dt)² = 4x(1+2x) = 4G for a = sinh(√2 t)/√2.

**Collar matching at u = 1.**
- The (1−u)³ factors kill qF, qG, w and their first two derivatives.
- S(u) = u³(10 − 15u + 6u²) has S(1) = 1 and S′(1) = S″(1) = 0.
- So the metric 2-jet at x = X equals that of H⁴, which is what the transgression cancellation requires.

**Bolt.** At the bolt, F′(x₀)G′(x₀) = e^{q_F(0)+q_G(0)} = 1.

**Dead code.** The line `vol_density=...*0` is unused and harmless.

**Sensitivity of the inferred W⁺.** The inferred 4W⁺ is a difference of quantities of size ~1433. A relative error of 10⁻⁶ in `v8` would shift it by ~1.4×10⁻³, comparable to the reported values. The smooth x₀² scaling seen below is therefore a nontrivial sign that the volume factor and Vol(B) are correct.

## 3. A sharper reading of the data

**The J decomposition is uninformative.** Its split into ∫(s+18)²/3 ≈ +358 and 36V − 48VB ≈ −358 cancels to O(10⁻²). Because s ≈ −24, the term (s+18)²/3 ≈ 12, so these two pieces are just 48V and −48VB in disguise. The "volume channel" being −358 is an artifact of the reference value −18; it is not a saving.

**A better expansion about s = −24.** Writing s²/12 − 48 = (s+24)²/12 − 4(s+24):

  P/8π² − 1 = 4W⁺ + 48ΔV − 4∫(s+24) + ∫(s+24)²/12,  ΔV = V − VB.

All terms are in units of 8π².

| row | 48ΔV | −4∫(s+24) | ∫(s+24)²/12 | scalar-vol | 4W⁺ | P − 1 |
|---|---|---|---|---|---|---|
| x₀ = .003, X = 64 | .02404 | −.01807 | 4.3e−5 | .006012 | 4.48e−5 | .006056 |
| x₀ = .01, X = 64 | .06877 | −.04913 | 3.95e−4 | .02004 | 4.29e−4 | .02047 |
| x₀ = .03, X = 64 | .16991 | −.11307 | 3.03e−3 | .05986 | 3.21e−3 | .06307 |
| x₀ = .01, X = 8 | .02602 | −.00643 | 3.91e−4 | .01998 | 5.76e−4 | .02056 |

**Mechanism behind the first-order term.**
- The combination 48ΔV − 4∫(s+24) equals −4Δ∫s − 48ΔV. This is the first variation of the Einstein–Hilbert action with cosmological constant at Ric = −6g. With δs = 6 tr k + div and δdV = ½ tr k dV, its interior variation is 24∫tr k − 24∫tr k = 0.
- So only the singular Burns flux at the core survives: −4·(−4π²x₀)/8π² = 2x₀.
- This equals Theorem F's (1/12)ΔS = −2x₀ s_p F_s/12 = 16π²x₀, the R⁺ = −2I prediction.

**Numerical confirmation.**
- (−4Δ∫s − 48ΔV)/x₀ = 1.990, 1.964, 1.895 for x₀ = .003, .01, .03.
- The scalar-volume channel divided by x₀ is 2.004, 2.004, 1.995.
- The individual pieces are strongly cutoff-dependent: 48ΔV is .069 at X = 64 but .026 at X = 8 for the same x₀. Their sum is not.
- This also explains why Theorem F's flux persists at X = 64, far outside its r₀ → 0 setting: the cancellation holds for any cutoff profile on an Einstein bulk.

**Second order.**
- (P − 1 − 2x₀)/x₀² = 6.3, 4.67, 3.41.
- The W⁺ part, 4W⁺/x₀² = 4.98, 4.29, 3.56, carries essentially all of it. The scalar part is +1.3, +0.4, −0.15.
- The W⁺ trend is consistent with x₀²(A log(1/x₀) + B), with A ≈ 0.6. This matches the |W⁺| ~ x₀/r² cross-term on √x₀ < r < O(1).
- Since this channel is a square, the H⁴ second order is a cost. In CH², by contrast, the kernel of R⁺ lets a signed cross-term save.
- Raising X from 8 to 64 lowers 4W⁺ (5.8 → 4.3 ×10⁻⁴), but the degree also changed (12 → 16), so this is not a clean collar-dependence measurement.

**Direction of the volume term.** ΔV > 0 in every row. The Burns-like core adds volume (det = 1 + x₀/r²), and the linear scalar term only partially compensates. There is no volume deficit anywhere.

## 4. What the data do and do not show about volume saving or s ≈ −18

1. **The s ≈ −18 measures are mis-targeted.**
   - s = −18 is the pointwise minimizer of (s+24)²/4 + s²/12, i.e. the J-integrand at fixed volume.
   - For the P-identity the analogous minimizer of s²/12 is s = 0.
   - The cells are P-optimized (`target='P'`).
   - `rms_scalar_plus18` ≈ 6.0 just restates s ≈ −24, and `volume_frac_abs_splus18_le3` measures J's attractor on P-optimal metrics.

2. **J adds nothing beyond P for subthreshold questions.** Since J = P + ¼∫(s+24)² ≥ P, any cell with J < 8π² already has P < 8π². Within a fixed family, inf J ≥ inf P. A J-specific scalar mechanism cannot produce a subthreshold cell that P misses. The relevant scalar question is whether a region with |s| well below 24 can lower ∫s²/12 below 48VB more cheaply than the Ric° it forces through div Ric° = ds/4.

3. **The tested corner is fixed by first-order theory.**
   - x₀ ≤ 0.03 means the exceptional curve is small compared with the curvature radius 1/√2.
   - There, Theorem F and the criticality above force P − 1 = 2x₀ + O(x₀² log) for any cutoff.
   - Lemma Q′ also applies, because the neck around the bolt is almost flat.
   - So "no volume saving or scalar-plateau mechanism at X = 64, x₀ ≤ 0.03" is what perturbation theory predicts; it is not an independent test.
   - A mechanism able to beat 8π² over a hyperbolic bulk would have to be nonperturbative: x₀ = O(1) or larger, so that the bolt sees the curvature scale and the first-order term 2x₀ no longer dominates. No cell in this regime has been computed.

4. **Ansatz rigidity in the large-volume region.**
   - With x₀ = .003, the region x ∈ [1, 64], which contains almost all of VB, is only u ∈ [0.58, 1].
   - There the corrections are multiplied by (1−u)³ and limited to degree-16 Chebyshev modes in u.
   - A deformation that shrinks the hyperbolic region, or holds |s| below 24 on a plateau with a thin transition layer, may be poorly represented.
   - Only two random restarts exist, both at (x₀, X) = (.01, 8). No degree or quadrature sweep was made at X = 64, though nq-recomputation agrees to ~10⁻¹⁰.

**Supported conclusion.** In the diagonal O(−1) family at x₀ ≤ 0.03, P-optimized cells with exact H⁴ collars up to X = 64 show:
- the scalar-volume channel equal to the Burns flux 2x₀ to within 2–5%;
- ΔV > 0;
- s within ~10⁻³ of −24 on average;
- an O(x₀²) positive W⁺ channel.

**Still unresolved.** Whether P^{H⁴}_{1,0} = 8π² requires two further pieces of work:
- cells with x₀ = O(1) or larger (and J-optimized cells, if J is the functional of interest), together with a direct W^± evaluation;
- a lower-bound argument converting the Einstein–Hilbert criticality plus the Burns flux into an inequality at finite x₀.