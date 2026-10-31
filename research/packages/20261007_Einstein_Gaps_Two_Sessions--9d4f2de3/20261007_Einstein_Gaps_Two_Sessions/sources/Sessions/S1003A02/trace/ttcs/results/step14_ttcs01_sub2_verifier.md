# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/einstein_chirality_check.py",
    "Sessions/S1003A02/workspace/data/einstein_bolt_chirality.json",
    "Sessions/S1003A02/workspace/notes/step13_einstein_fillings_blown_up_ball.md",
    "Sessions/S1003A02/workspace/scripts/einstein_bolt_shoot.py"
  ]
}
```

## Task

Independently interpret the Step-14 curvature experiment on the Step-13 diagonal SU(2) Einstein O(-1) bolt branch. The coordinate/JAX curvature routine is calibrated on complex hyperbolic space: CH has WA≈0 and WB=24. Along the numerical bolt branch, Ric0≈0 and scalar≈-24, while WA is large near the bolt but decays to 10^{-12}–10^{-16} on the ACH plateau; WB remains nonzero around 23–26. Decide precisely what this establishes and what it does not: is the full metric self-dual, asymptotically self-dual, or merely approaching the CH end? Check whether any orientation or 2-jet reconstruction issue could explain the result. Then assess how this changes the proposed route through Hitchin/Biquard versus interval enclosure. Give a mathematical memo, not procedural advice.

## Output

# Memo: Weyl chirality of the diagonal SU(2) Einstein O(−1) bolt branch on D#CP̄²

## 0. Summary

The Step-14 data establish three facts.

1. The metrics are Einstein. The curvature routine, which is independent of the ODE's Ricci formula, confirms this at every sampled point.
2. Neither Weyl half vanishes. The metrics are not self-dual, not anti-self-dual, and not Kähler for either orientation.
3. The ACH end is approached with |W₋| decaying like e^{−4t}, while |W₊|² → s²/24 = 24. W₋ → 0 holds automatically for any ACH Einstein end. The informative quantities are the bulk size of W₋ and the coefficient of its e^{−4t} tail.

The branch therefore lies outside the Hitchin/Biquard self-dual Einstein class. That class remains useful only as a reference slice and as a ρ-calibration on the ball. Neither orientation nor the 2-jet reconstruction can produce the observed pattern.

## 1. What the CH calibration fixes

**Normalization.** CH² with s = −24 returns WB = 24.000, WA ≈ 10⁻²⁸ and Ric₀ ≈ 10⁻²⁸. For a Kähler surface in its complex orientation, W₊ acting on Λ⁺ has eigenvalues (s/6, −s/12, −s/12), so |W₊|² = s²/24 = 24.

The routine therefore uses the endomorphism norm on Λ±, with |e¹∧e²| = 1. In this normalization the Gauss–Bonnet and signature formulas take the form
8π²χ = ∫(|W₊|² + |W₋|² + s²/24 − ½|Ric₀|²) and 12π²τ = ∫(|W₊|² − |W₋|²).
Fubini–Study CP² with Ric = 6g and volume π²/2 reproduces χ = 3 and τ = 1 in these formulas.

**Orientation.** The three slot forms satisfy
ωᵢ∧ωᵢ = 2a₁a₂a₃ dt∧σᵢ∧σⱼ∧σₖ = 2a₁a₂a₃ dt∧σ₁∧σ₂∧σ₃
for each cyclic (i,j,k), since cyclic permutations are even. All three slot forms therefore lie in the same half Λ⁺. Consequences:

- **Same half at both ends.** The CH Kähler direction sits in slot 2 in the calibration run and in slot 1 at the bolt branch's end. It belongs to the same half in both runs.
- **The bolt-side half.** Near the bolt, ω₃ ≈ t dt∧σ₃ + b²σ₁∧σ₂. Closedness reduces to (a₁a₂)′ = 2a₃, which the Burns metric satisfies. ω₃ is thus the Kähler form of the Burns-type complex structure on O(−1). Its half Λ⁺ is the complex orientation of the blow-up, with E·E = −1, χ = 2, τ = −1.
- **Resulting labels.** Both runs use the same euler_E chart and the same function. Hence WB = |W₊|² and WA = |W₋|² in the complex orientation of Bl(B⁴), which agrees with the complex orientation of the ACH end.

A sign convention dσ = ±2σ∧σ (equivalently σ ↦ −σ) reverses dt∧σ₁σ₂σ₃. Such a reversal would swap the labels in the CH run and the bolt runs together. It cannot make a self-dual metric appear non-self-dual.

**One-sidedness of the calibration.** CH tests the zero of only one block. The A-block's normalization is inferred by symmetry. The Burns metric from Step 13 (a₁ = a₂ = √(t²+x₀), a₃ = t) is scalar-flat Kähler, so it must give WB ≡ 0 with WA ≠ 0. That would pin both blocks. The present conclusions do not need this check, because WA ≫ WB near the bolt is a large effect.

**2-jet reconstruction.** Curvature depends only on the 2-jet. The reconstruction uses a, a′ = a·y and a″ = a(y′ + y²), with y′ taken from the Einstein right-hand side. This 2-jet is exact at r = 0. Angular derivatives come only from E and are also exact. SU(2)-invariance makes the scalars independent of the base point (0.37, 1.13, 0.71), which is away from the Euler-chart singularity.

Because a″ comes from the ODE, Ric₀ ≈ 10⁻²³ is not a test of integration accuracy. It tests two things:

- the Step-13 Ricci formula against an independent coordinate computation;
- R₀₀ = −6, which holds only when the constraint is satisfied, so it confirms the constraint at the sampled points.

The Weyl blocks are genuine curvature of the numerical metric at those points.

**Roundoff floor.** At b = 4, t = 4.88, the axes reach a₁ ≈ 2.9×10⁴ and the coordinate metric is badly scaled. There |Ric₀| ≈ 1.6×10⁻¹¹, which sets the curvature noise floor. The reported |W₋| ≈ (4×10⁻¹⁶)^{1/2} = 2×10⁻⁸ is about 10³ above that floor. At b = 0.8 the margin is larger: |W₋| ≈ 9×10⁻⁷ against |Ric₀| ≈ 2×10⁻¹².

## 2. What the bolt data establish

**(a) Not self-dual, not anti-self-dual, not conformally flat.** Near the bolt, WA ranges from 8 (b = 4) through 168 (b = 0.8) to 2370 (b = 0.35). WB stays order one or larger at every sample; the smallest value is 5.07 at b = 4, t = 0.2. Neither block vanishes identically, so W₋ ≢ 0 and W₊ ≢ 0.

**(b) Not Kähler for either orientation, and not only for the slot structures.**

- Kähler in the complex orientation would force |W₊|² = 24 everywhere (Derdziński). The data give WB = 36.1 at b = 0.8, t = 0.08, and 409.5 at b = 0.35.
- Kähler in the reversed orientation would force |W₋|² = 24. The data give WA = 168.

This independently confirms the series argument of Step 13 §2, now for every compatible complex structure rather than only the slot structures.

**(c) Burns-like chirality near the bolt for small b.** The ratio WB/WA near the bolt is 0.17 (b = 0.35), 0.22 (b = 0.8) and 0.80 (b = 4). For small b the bolt region is dominated by W₋. This matches a Burns-type local geometry: Burns is scalar-flat Kähler, so W₊ = 0 and W₋ ≠ 0 in the complex orientation. The Einstein condition adds a W₊ of size set by s. This is the expected picture for a small (−1)-curve inside an Einstein metric with Ric = −6g.

**(d) Rate of decay of W₋ on the ACH end.** The effective exponents from the sample pairs are:

| b | interval | Δ ln WA / Δt |
|---|---|---|
| 0.8 | t = 2 → 3.86 | 8.13 |
| 4 | t = 2 → 4.88 | 8.05 |
| 0.35 | t = 2 → 3.43 | 8.27 |

So |W₋|² ∝ e^{−8t}, i.e. |W₋| = O(e^{−4t}). This is the order at which Step 13 locates the free (mass-type) ACH data. The sector equation u″ + 4u′ = O(e^{−2t}) for u = L₂ − L₃ has the modes {const, e^{−4t}}.

The naive leading coefficient w(b)² ≈ e^{8t}|W₋|² is about 22–28 (b = 0.8), 36–42 (b = 4) and 2.7–4.0 (b = 0.35). It drifts by 20–30 % across the window. This is consistent with subleading corrections, which may include logarithmic terms of ACH expansions. The data do not determine whether the corrections are logarithmic or exponential.

**(e) What "→ 0" means.** Every ACH Einstein metric has curvature converging to the CH curvature, and CH has W₋ = 0. So W₋ → 0 alone says only that the trajectory approaches the CH end.

The e^{−4t} rate is also expected generically, by the following argument:

- Biquard's ACH Einstein expansions are formally determined by the CR infinity up to the free order.
- Self-dual Einstein formal expansions exist for these CR structures; Biquard's ball fillings exist near the standard sphere.
- Below the free order, the general and the self-dual formal expansions therefore coincide.
- Hence W₋ = O(e^{−4t}) for any ACH Einstein end with such CR infinity.

The new information is not the rate but the nonzero coefficient w(b) together with the large bulk W₋. "Asymptotically self-dual to the free order" is automatic. "Self-dual" fails for this branch.

**(f) W₊ on the plateau.** At t_min, WB = 22.94, 23.11 and 26.16, which differ from 24 by −4.4 %, −3.7 % and +9 %. At the same points WA ≈ 10⁻¹²–10⁻¹⁶.

The re-integrated trajectories (rtol 2e−13) sit at a distance of order 10⁻² from the ACH₁ fixed point at t_min. Examples are y = (1.9925, 1.0045, 1.0081) at b = 0.8 and y = (2.0146, 0.9889, 0.9893) at b = 4. This is larger than the 10⁻³–10⁻⁴ recorded in the bisection runs.

So the ODE deviation from the fixed point is visible linearly in W₊ and invisible in W₋. Both the residual approach directions and the exit direction toward AH or singular are therefore infinitesimally self-dual: δW₋ = 0 at linear order. This is consistent with the self-dual Pedersen/Hitchin SU(2) Einstein metrics on B⁴ degenerating to CH². It suggests that the saddle's unstable direction at ACH₁ lies tangent to the self-dual invariant set.

Two consequences:

- The bulk value of W₋ is a robust invariant along the branch, insensitive to the bisection residue.
- The few-percent deviation in WB is the same effect that produces the ≈ 3 % ρ drift. It is not an asymptotic value and does not affect the statement ρ_min ≈ 2.2 ≫ 1.

**Answer to the question posed.** The full metric is neither self-dual nor anti-self-dual. It is asymptotic to CH² in curvature at the end, with |W₋| = O(e^{−4t}) and a nonzero coefficient. That rate is the generic ACH Einstein rate and is not specific self-duality information.

## 3. Global identity linking W₋, topology and the CR end

Subtracting three times the signature formula from the Gauss–Bonnet formula gives
8π²(χ − 3τ) = ∫(3|W₋|² + s²/24 − |W₊|² − ½|Ric₀|²).
The integrand vanishes identically on CH² and decays on ACH Einstein ends. The W₋ part decays like e^{−8t}, against a volume growth of e^{4t}. This is why Biquard–Herzlich chose the combination χ − 3τ.

For an ACH Einstein metric their theorem reads
χ − 3τ = (1/8π²)∫(3|W₋|² + s²/24 − |W₊|²) + μ(∂).
The exact constants and sign conventions for the end term should be matched against their paper. Normalizing by the CH² ball gives μ(standard) = 1. On D#CP̄² the topological side is χ − 3τ = 5, so along the branch
5 − μ(ρ) = (1/8π²)∫(3WA + 24 − WB) dvol.
Every quantity on the right-hand side is available from the Step-14 machinery.

**Uses of this identity.**

- **An integral check of the branch.** At fixed ρ, μ is a CR invariant, so it does not depend on the filling. The fold of b ↦ ρ(b) near ρ_min ≈ 2.2 means two bolt parameters b give the same ρ. The two right-hand sides must then agree, which is a sharp consistency test.
- **A value of μ(ρ) for Rossi spheres.** The branch yields μ(ρ) for ρ ≳ 2.2. Biquard self-dual fillings of the same Rossi spheres on B⁴ (χ − 3τ = 1, W₋ = 0) give an independent value through 1 − μ = (1/8π²)∫(24 − |W₊|²), wherever those fillings exist.
- **No obstruction from W₋ alone.** For the hypothetical total-depletion filling (ρ = 1 on D#CP̄²), the identity gives 4 = (1/8π²)∫(3|W₋|² + 24 − |W₊|²). This does not force W₋ = 0 and does not rule out existence. W₋ ≠ 0 is not an obstruction to that filling; it only excludes the self-dual class as the place to look.
- **A route into the Step-13 cost.** The cell-cost identity contains ΔW₊. The identity above converts the W₊ deficit of an Einstein filling into 3∫|W₋|² plus topology plus μ. So the W₋ integral, rather than W₊ directly, carries the variable part of the Einstein-limit cost. The exact form of ΔW₊ and of ΔS in the cost identity is not in the supplied files, so no numerical cost prediction follows yet.

## 4. Consequences for Hitchin/Biquard versus interval enclosure

**What the self-dual theory no longer provides.** Hitchin's Painlevé VI description and Tod's first-order reduction parametrize SU(2)-invariant Einstein metrics with W₋ = 0. Biquard's "Métriques autoduales sur la boule" fills CR spheres by such metrics on B⁴.

The D#CP̄² branch has W₋ ≢ 0, of size up to 10³ near the bolt. It is therefore not an orbit of the integrable first-order system. Neither classifying the ACH separatrix through Painlevé VI nor proving ρ(b) ≥ 2.1 through it is available. The relevant ODE is the full second-order diagonal Bianchi IX Einstein system with constraint, for which no integrable structure is known. The analytic home of the branch is Biquard's general ACH Einstein deformation theory (Astérisque 265), not the self-dual one.

**What the self-dual theory still provides.**

1. **An explicit slice of the end-parameter space.** ACH₁ ends are parametrized by (ρ, free e^{−4t} coefficients, t-shift). By (d)–(f), the W₋ coefficient w is a natural coordinate on this space, and w = 0 is exactly the Hitchin/Biquard locus. An interval enclosure built from the ACH asymptotic expansion inward must reproduce, at w = 0, the explicit self-dual ball fillings. This gives an exact internal test of the enclosure's asymptotic module.
2. **Calibration of ρ on B⁴.** The ball family through CH² at ρ = 1 calibrates the ρ readout (Step 13 §6 item 2). The value μ(ρ) from §3 calibrates the CR side of the matching.
3. **Structure of the saddle.** Linear modes at ACH₁ with δW₋ = 0 are tangent to the self-dual invariant set. The exit direction can thus be described by the known self-dual flow. This reduces the unknown part of the matching to the single w-direction, plus ρ and the shift.

**Prediction for the fold.** Biquard's ACH Einstein deformation theory makes the filling map Fredholm. A fold of b ↦ ρ(b) at b* ≈ 0.75–0.8, ρ_min ≈ 2.2, is equivalent to a nonzero SU(2)-invariant, decaying, infinitesimal Einstein deformation at b* that fixes the CR infinity. This is a kernel element of the linearized Einstein operator in the decaying weighted space. It is an object an enclosure can certify (a sign change of a scalar determinant along the branch), and it is the mechanism behind ρ_min > 1. A rigorous ρ_min statement amounts to enclosing this fold, together with the two-sided asymptotics ρ ≈ 1.36 b as b → ∞ and the transition near b ≈ 0.29.

**Balance between the routes.** The chirality data shift weight toward interval enclosure of the full Einstein ODE, with the end parametrized by (ρ, w, mass-type coefficient, shift). The Hitchin/Biquard theory enters as the exact w = 0 slice and as ball calibration. It does not carry the existence or non-existence question on D#CP̄².

## 5. Unresolved

- **Exact form of the W₋ tail.** The precise subleading correction to |W₋| ∼ w e^{−4t} (logarithmic or exponential) and the t-shift-invariant normalization of w are not fixed. The 20–30 % drift of e^{8t}WA leaves the form open; an asymptotic expansion of the ACH₁ end in the diagonal ansatz would fix it.
- **The linear δW₋ = 0 property.** This is inferred from two data points per run: W₊ deviates at about 10⁻², while W₋ stays near 10⁻¹². Confirming it requires the linearization of the Weyl map at the ACH₁ fixed point along each eigenmode.
- **Normalization of the Biquard–Herzlich identity.** The end term and constants in §3 come from that theorem as recalled here and need matching against the source. The values of μ on Rossi spheres are not supplied in any file.
- **Non-SU(2) fillings.** Nothing here concerns non-diagonal or non-SU(2) Einstein fillings of the standard sphere on D#CP̄². The chirality data constrain only the diagonal SU(2) branch.