# TTCS Independent Branch Record

```json
{
  "step_id": 36,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/step36_cap_perp_transplant.py",
    "Sessions/S1003A01/workspace/data/step36/cap_perp_baseline_scan.json",
    "Sessions/S1003A01/workspace/data/step36/cap_perp_width_scan.json",
    "Sessions/S1003A01/workspace/data/step36/cap_perp_response_opt_pilot.json",
    "Sessions/S1003A01/workspace/data/step36/cap_perp_response_validation.json",
    "Sessions/S1003A01/workspace/notes/step35_cap_transfer_neutrality_and_cap_cells.md",
    "Sessions/S1003A01/workspace/scripts/perp_dual_cost.py",
    "Sessions/S1003A02/workspace/scripts/o11_perp_cell.py"
  ]
}
```

## Task

Independently read the corrected Step-35 note and the Step-36 transplant script/data. Check the mathematical realization and numerical interpretation of the finite-amplitude perpendicular cap trial: scale from Ric=-6 to Ric=-1; CH exponential chart reconstruction; exact Calabi cap in proper normal Cartesian coordinates; smoothness/positivity of the convex interpolation and response tensors; core-plus-annulus integration; normalization of D, P, scalar moments, and the relative chiral ledger. Identify any formula or implementation error that could change the reported conclusion. The key reported observation is that the direct baseline costs D/(8pi^2) about 2.44 at the best scanned pair (a,b)=(0.5,1.5), while three response modes lower it only to about 2.26 on independent QMC seeds, still far above both 1 and the certified CH cell 0.99567003. Also assess what this finite trial establishes about cap geometry and what it leaves open. Do not assume the withdrawn same-class Theorem N.

## Output

# Verification memo: Step‑36 finite‑amplitude perpendicular cap trial

## Summary

- **Implementation.** The construction is implemented correctly in every component I checked: the scaling from Ric = −6 to Ric = −1, the exponential‑chart reconstruction of the cell, the cap metric, the interpolation, the quadrature, and the ledger. I found no formula or code error that would move the reported D/(8π²) ≈ 2.26 by an amount comparable to its distance from 1.
- **The number is reliable for this trial.** The three out‑of‑sample QMC seeds give 2.258, 2.268 and 2.270, so the seed spread is about 0.006.
- **The number does not yet measure cap geometry.** Three things are mixed into it:
  - truncation of the certified cell inside its bolt region;
  - a cap chart that is Fermi‑type about the divisor rather than geodesic normal at p;
  - a response space that cannot reach the conformally invariant W⁺ excess the trial carries.
- **Missing control.** The same‑chart CH control is absent. `bergman()` is defined in the script but never used.
- **New structural fact.** By representation theory, the cap's W⁻ cannot enter the cost of an SU(2)₋‑invariant cell at linear order. This identifies the scientific quantity that actually decides cap‑versus‑CH: a quadratic W⁻ coefficient.

## 1. Realization checks

**(a) Rescaling.** Let g′ = 6g. Then Ric(g′) = Ric(g) = −6g = −g′. Also |T|²_{g′} = |T|²_g/36 and dV_{g′} = 36 dV_g.

- Therefore ∫|Ric′ + g′|²_{g′} dV_{g′} = J₆, so D and P are scale invariant.
- The volume, ∫s and ∫s² scale by factors 36, 6 and 1, matching `core_integrals`.
- The core density r0 + (s+24)²/4 equals |Ric + 6g|², because Ric + 6g = Ric° + (s/4 + 6)g.

**(b) CH exponential chart.** With Ric = −6, CH is dρ² + sinh²ρ(σ₁² + σ₂²) + sinh²ρ cosh²ρ σ₃². Under x = sinh²ρ this becomes dx²/(4(x+x²)) + x(σ₁² + σ₂²) + (x+x²)σ₃², which is the stored collar form.

- The volume element π²√(det h/G) dx integrates to π²x²/2, which equals the CH ball volume. This fixes the convention Σσ² = round unit S³ (σ‑volume 2π²).
- After scaling, r = √6 ρ, so x = sinh²(r/√6). The dr² coefficient becomes 6(dx/dr)²/(4G) = (x+x²)/G. This is the code's `lam[0]`.
- The angular coefficients are 6h_kk σ_k² = (6h_kk/r²) ê_k ⊗ ê_k. This is also correct.
- The frame fields iq, jq, kq are left quaternion multiplications.
  - They are orthonormal and orthogonal to the radial direction (I checked directly).
  - Their brackets are [X_i, X_j] = −2X_k, giving dσ_k = 2σ_i∧σ_j cyclically.
  - The assignment (slot 1, 2, 3) = (j, k, i) is a cyclic relabelling.
- Consequences of this assignment:
  - The CH slot 3 is carried by the Hopf field iz, so the asymptotic Kähler form is ω_i.
  - The bolt collapses the j‑orbits. Left multiplication by a unit quaternion p with p i p⁻¹ = j lies in SO(4) and carries the i‑fibration to the j‑fibration. So the bolt is O(−1) in the ξ‑orientation, τ = −1, and b − a = +12π².
  - J_j is ⊥ ω_i inside Λ⁺, so the realized cell really is the perpendicular branch.
  - Right Sp(1) is the complex‑linear SU(2). It commutes with all left multiplications, so the cell's symmetry acts trivially on Λ⁺ and by SO(3) on Λ⁻. This is SU(2)₋. U(1)₋ = {(e^{iθ}z₁, e^{−iθ}z₂)} ⊂ SU(2)₋ is a common symmetry of the cell, the cap, χ and S, exactly as Step 35 §6 requires.

**(c) Cap metric.** I checked the formulas symbolically.

- du/dn = √(2/3)·cosh^{−1/3}·sinh = √q.
- The normal block reduces as dn² + q dΨ² = (q/ss)I + ((1 − q/ss)/ss) v_r v_rᵀ.
- In the horizontal block, (dΨ + A)² with A = v_h·(dX, dY) produces exactly the `hh`, `hn` and `nn` blocks.
- The gauges agree: Ψ′ = Ψ + XY/2 turns dΨ + X dY into dΨ′ + (X dY − Y dX)/2.
- The connection satisfies dA = dX∧dY = ω_D, which is the Kähler closure condition for the Calabi ansatz.
- Smooth closing at the divisor: q′(1) = 2 gives Ψ‑period 2π.
- At p, ω = dX∧dY + dZ∧dW and e^{0123} = dX dY dZ dW. These coincide with the CH ω_i and orientation under z₁ = X + iY, z₂ = Z + iW.

The numerical Einstein smoke test is weak: both test points have ss = 0.25, so only one normal radius is sampled. The symbolic check above covers the gap.

**(d) Interpolation and responses.**

- `smoother7` and `response_bump` vanish to fourth order at the junctions, so the trial is C³ rather than C^∞. This is harmless because D is C²‑continuous, so the trial can be approximated by smooth metrics with arbitrarily small change in D.
- Positivity:
  - With c₀ = 0.112, the effective weight ch + c₀·fb stays below 1. I found 0.986 at t = 0.8, 0.9992 at t = 0.9 and 0.99996 at t = 0.95. The m₀ mode therefore remains a convex combination.
  - The m₁ conformal factor is 1 − 0.005·fb > 0.
  - The m₂ coefficient of 0.012 is small, consistent with the sampled minimum eigenvalue of 0.27.

**(e) Integration.**

- The core runs over x ∈ [x₀, x_a], which is the whole blown‑up region, and its integrand is smooth at the bolt (functions of s²).
- The annulus sampling is correct: r = (a⁴ + (b⁴ − a⁴)U)^{1/4}, Hopf coordinates with |z₁|² uniform, and shell volume π²(b⁴ − a⁴)/2.
- There is neither a gap nor an overlap at r = a.
- The cap reference volume 2π²∫₀ᵇ (b² − n²) u √q dn follows from det = u²q in (X, Y, n, Ψ) together with dZ dW = n dn dΨ.

**(f) Ledger.** Relative Gauss–Bonnet and signature with δχ = 1, δτ = −1 give b = a + 12π² and P = 8π² + 4a + δS/12. Here δS is the relative ∫s², and it is meaningful because the trial equals the cap beyond b. The output b − a ≡ 1.5 is a tautology, not a check.

## 2. Numerical points that do not change the number

- **Near‑axis cancellation.** `cc = (1−ff)/ss` loses precision as ss → 0. Forward‑mode second derivatives scale like ε_mach/ss³, but this only affects Sobol nodes with very small ss and is negligible in the integral. A Taylor branch would make the evaluator robust for reuse.
- **Misleading docstring.** "Radial distance is rr" is true only for the CH profile. For the cell, the proper radial factor is √((x+x²)/G).
- **Optimizer cost.** `jax.jit(jax.value_and_grad(obj))` is rebuilt on every L‑BFGS call. This explains the 101 s for 128 nodes; it does not affect correctness.
- **In‑sample bias.** The 128‑node objective is 2.208, against an out‑of‑sample mean of 2.265. The gain over the baseline (2.441 at seed 0, 512 nodes) is about 0.17–0.18, well above the seed spread.
- **Untested link 1: chart versus `metric_from`.** Nothing in the data compares the ξ‑chart Ricci with the `metric_from` curvature. Evaluating `fields` with χ ≡ 0 at a few radii, and comparing pointwise |Ric + g|² and the volume density with the core integrand at the same x, would close this. The frame and normalization derivation above predicts agreement.
- **Untested link 2: full‑length core.** `core_integrals` run out to x = X with log‑spaced nodes should reproduce 0.995670. This has not been shown.

## 3. Exact decomposition of the trial value

Write σ = s + 4. Then ∫s² = ∫σ² − 8∫σ + 16V, and the cap has σ = 0. For any modification with an exact Ric = −g collar, adding k blow‑ups and ℓ handles:

$$
D=8\pi^2(k+4\ell)+4a+\tfrac43\,\delta V+\tfrac13\!\int\sigma(\sigma-2).
$$

**Check against the optimized trial, seed 1.** All terms in units of 8π²:

| Term | Value |
|---|---|
| 4a | 0.284 |
| (4/3)δV, with δV = −1.070 | −0.018 |
| (1/3)∫σ(σ−2), with ∫σ = δ∫s + 4δV = −9.32 and ∫σ² = 216.2 | 0.992 |
| **Total excess over 1** | **1.258** |

The total excess of 1.258 matches the reported 2.258 − 1. In the baseline the same three terms are 0.368, −0.020 and 1.093.

**Two consequences.**

1. **The scalar term dominates and the conformal mode hardly moves it.** About 1.0 of the excess is scalar, yet a single fixed‑profile conformal mode barely changes it. The scalar part is therefore not obstructed by anything structural in this trial; the response family is too thin to reach it.
2. **The W⁺ term cannot be reached by conformal changes.** ∫|W⁺|² dV is conformally invariant, so 4a ≈ +0.28 is a property of the trial's conformal class. Under conformal deformations, D moves only through δV and σ. Note also that σ(σ−2) ≥ −1, so modest positive scalar excess can lower D; this is the content of the Step‑36 remark that δS is not a residual.

**Comparison with the CH cell.** Step 35 states that the certified CH cell has 4a ≈ −0.34. If that figure is in the same 8π²‑normalized units as `fourdWp` in `o11_perp_cell.report`, then the transplant has swung the conformally invariant self‑dual energy by about +0.6. That swing would remove the W⁺ depletion through which the CH cell gets below 1.

Both backgrounds have pointwise identical, parallel W⁺ relative to ω. An annulus that is well matched should therefore generate little δW⁺. A direct pointwise |W⁺|² integration, split into core and annulus, would show whether:
- the depletion was cut off along with the outer profile of the cell, or
- it is generated by the interpolation.

The current ledger cannot separate these, since it is reconstructed rather than integrated.

## 4. Why 2.26 is not yet a statement about the cap

**Cell truncation.** The bolt sits at r_b = √6·arsinh√0.03 ≈ 0.422, so a = 0.5 cuts just outside the bolt neighbourhood.

- The core up to a = 0.5 carries 0.459 of the cell's 0.9957.
- At these radii the cell is far from CH in the ξ chart: (x+x²)/G and 6F/r² differ from 1 by O(1). The sampled minimum eigenvalue 0.27 matches 6F/r² at x ≈ 0.042.
- The certified profile reaches CH only at x = 128, i.e. r ≈ 7.6.

The interpolation therefore mainly cuts through the cell, not through a CH‑like collar.

**Chart mismatch.** (X, Y, Z, W) are Fermi coordinates about the flat, totally geodesic divisor with symmetric gauge. Only Z and W are exponential. These coordinates differ from geodesic normal coordinates at p by an O(r²) diffeomorphism.

- Example: g_XX = 1 + n²/2 exactly, whereas normal coordinates give a 1/6 coefficient on the mixed‑plane term.
- At larger radius, the Heisenberg term q(X² + Y²)/4 and u ≈ 3.2 at n = 2 differ from the CH chart by factors of 3–7.

The baseline scan grows rapidly with a: 3.1, 7.9, 24, 72, 483, 1909. For fixed a = 0.5, the width scan grows with b: 2.44, 2.79, 4.12, 7.00. A cutoff‑gradient cost would decrease with width. This one increases, which marks it as bulk metric mismatch rather than gradient cost. Part of that mismatch is pure gauge.

**The proper reference quantity.** In geodesic normal coordinates of both metrics at p, aligned so that ω agrees, the difference is −⅓(R_cap − R_CH)xx + O(r³). That curvature difference is exactly W⁻_cap = ⅔ diag(2, −1, −1), since W⁺ and s coincide and CH has W⁻ = 0. Holomorphic normal (Bochner) coordinates do the same job: the Bochner tensor is W⁻.

**The missing CH control.** Running the identical pipeline with the cap replaced by exact CH in the exponential chart (G = x + x², h = diag(x, x, x+x²), scaled) at the same (a, b) and response modes is the experiment that isolates the cap‑specific cost.
- If that control also gives values near 2, the excess is a truncation artifact.
- Only the difference between the two runs measures cap geometry.

A second separating experiment is to use a cell re‑optimized with a short collar, exactly CH at r ≈ a (the `PerpCell` X parameter allows this), followed by a CH‑to‑cap transition. This splits the two confounders.

## 5. Structural facts about cap cells

**(i) Identical R⁺ at p.** At p, R⁺ = W⁺ + s/12 = diag(−1, 0, 0) for both CH and the cap. In particular R⁺ vanishes on ω^⊥ in both. Any mechanism that is linear in R⁺, including the glued‑Burns first variation, is identical for the two backgrounds on both the aligned and perpendicular branches.

**(ii) No linear W⁻ coupling for SU(2)₋‑invariant cells.** The background difference enters through W⁻ ∈ Sym²₀Λ⁻, which is the representation (0, 2) of SU(2)₊ × SU(2)₋.

- A cell invariant under SU(2)₋ pairs linearly only with SU(2)₋‑invariant components. Since (0, 2) contains none, the linear W⁻(p) coupling vanishes.
- −1 ∈ SU(2)₋ kills the ∇W⁻ terms by parity.
- Sym²T*⊗(0, 2) contains no (·, 0) component.
- The first linear invariant appears only through Sym⁴T*⊗(0, 2) ⊃ (2, 0), i.e. ∇⁴W⁻ paired with the cell's Λ⁺ direction.
- At quadratic order, (0, 2)⊗(0, 2) contains exactly one invariant, |W⁻|². Its coefficient is the same for every orientation of W⁻, so the type‑D axis ω̄ is irrelevant at that order.

**(iii) Small‑cell expansion.** For an SU(2)₋‑invariant cell of size ρ ≪ |W⁻|^{−1/2}, and assuming an SU(2)₋‑invariant optimal cell and envelope differentiability (neither is proved here):

$$
D_{\rm cap}=D_{\rm CH}+\kappa\,|W^-(p)|^2\rho^4+\dots,\qquad |W^-(p)|^2=8/3 .
$$

Here κ is a direct quadratic cost minus the gain from U(1)₋‑equivariant symmetry‑breaking responses. The buffered transfer of Step 35 §3 bounds the direct part by C ρ⁴|W⁻|². The sign of κ is the open object. It is computable as a single U(1)₋‑equivariant linear response of the CH cell to the source −⅓W⁻xx.

**(iv) Finite‑size regime and placement.** The certified cell's action extends to r ~ 2, where |W⁻|^{1/2} r is O(1). So (iii) indicates mechanism but does not settle the finite cell; that needs direct U(1)₋ optimization in cohomogeneity three. Moving off the divisor, |W⁻|² = 8/(3u⁶) falls about elevenfold by distance 1. Placement is therefore a second continuous parameter.

## 6. Arithmetic in Step 35 §2

- **b < 0 case.** From P = 8π² + 4a + δS/12 and a < −12π² one gets δS > 12P + 480π², not 576π².
- **Volume excess.** With the identity of §3, D ≤ 8π² and b < 0 force (4/3)δV + (1/3)∫σ(σ−2) > 40π². When σ ≈ 0 and D ≈ 8π², this gives δV ≳ 36π². The "≈36π² volume excess" statement is therefore correct only under s ≈ −4, consistent with the Step‑36 correction.

## 7. What the trial establishes and what remains open

**Established, as a floating‑point QMC upper bound.**
- There is an explicit C³, U(1)₋‑invariant metric on B_b#\overline{CP}² that equals the Calabi cap outside b, with D/(8π²) ≈ 2.265 ± 0.01.
- Its excess over 1 decomposes as roughly 1.0 scalar + 0.28 conformally invariant W⁺ − 0.02 volume.

**Not established.**
- Any lower bound for cap cells.
- Any comparison of cap cells with CH cells. The trial is dominated by cell truncation and Fermi‑chart mismatch, and the CH control is missing.
- Anything about the toric or aligned class.

**Open.**
- The sign of κ, i.e. the quadratic W⁻ susceptibility of the perpendicular cell.
- The finite‑size U(1)₋ cap‑cell infimum relative to 0.995670 and to 1.
- Whether a transition matched in normal or Bochner coordinates, applied to a short‑collar cell, keeps the CH cell's W⁺ depletion. A direct W⁺ integration would show this.