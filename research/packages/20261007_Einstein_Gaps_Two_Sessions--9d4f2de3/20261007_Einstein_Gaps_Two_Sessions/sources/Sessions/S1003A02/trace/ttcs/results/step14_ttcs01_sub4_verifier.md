# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/einstein_nut_series.py",
    "Sessions/S1003A02/workspace/data/einstein_nut/series.json",
    "Sessions/S1003A02/workspace/scripts/einstein_nut_shoot.py",
    "Sessions/S1003A02/workspace/data/einstein_nut_runs.json",
    "Sessions/S1003A02/workspace/scripts/einstein_bolt_shoot.py"
  ]
}
```

## Task

Read the exact nut-series and nut-shoot artifacts as an independent calibration of the Step-13 ACH classifier. The nut series has two free cubic coefficients and recovers complex hyperbolic space at (c1,c2,c3)=(1/6,2/3,1/6), where the shoot reaches ACH slot 2 with kappa≈0.999998 and rho=1. Nearby perturbations display the expected AH/singular saddle behavior while rho remains near one at closest approach. Determine what this validates, any numerical-instability caveats, and whether the ball test supports the interpretation of rho on the O(-1) bolt branch. Also comment on the failed attempt to interpret generic ball parameters as a continuum of ACH fillings; distinguish what is actually shown from Biquard's local deformation theory.

## Output

# The ball shoot as an independent calibration of the Step-13 ACH classifier

## Summary

The nut runs give a sharp test of three things:

- the ODE system,
- the regular nut series,
- the slot/κ readout of the ACH classifier.

They do not test the ρ readout at any value other than ρ = 1. Every ball trajectory computed so far has ρ ≡ 1 by symmetry. The run data also contain a quantitative signature of the ACH saddle that can be derived exactly. That signature explains the numerical horizon at t ≈ 6–7. It also supplies the mechanism that makes the ρ readout on the bolt robust. That mechanism, not the ball runs, is the real support for the bolt interpretation.

---

## 1. The series and the exact models

I checked `series.json` (and the copy hard-coded in `init`) by hand against two exact metrics. Recall that dσ_i = 2σ_j∧σ_k makes Σσ_i² the unit round S³.

**Complex hyperbolic space, Ric = −6g, fibre slot 2.**
- a₁ = a₃ = sinh t = t + t³/6 + t⁵/120.
- a₂ = ½ sinh 2t = t + (2/3)t³ + (2/15)t⁵.
- Substituting (q, r) = (2/3, 1/6) into the three c₅ formulas gives exactly (1/120, 2/15, 1/120).

**Real hyperbolic space H⁴, K = −2.**
- a_i = sinh(√2 t)/√2 = t + t³/3 + t⁵/30, so (q, r) = (1/3, 1/3).
- The c₅ formula returns 1/30.

**Cyclic covariance.** Substituting (q, r) → (r, 1 − q − r) into c₁₋₅ reproduces c₂₋₅ term by term.

**Cubic constraint.** The relation c₁ + c₂ + c₃ = 1 is the scalar-curvature constraint at the nut. Both exact models satisfy it.

**Smoothness.** Odd series with a_i = t + O(t³) are smooth at the nut. The correction terms are 2c_i t⁴σ_i² = 2c_i (t²σ_i)², and t²σ_i is a smooth 1-form.

So the regular nut family is genuinely two-dimensional, and the series is correct through t⁵. The truncation error at t₀ = 2·10⁻³ is O(t₀⁶) ≈ 6·10⁻¹⁷ relative, which is below double precision.

**Initial constraint residual.** The value `constraint0` ≈ 3·10⁻¹⁰ is not a series error. Each term of y_i y_j − 6 − ½ΣPot is about t₀⁻² ≈ 2.5·10⁵, so this residual is the roundoff of a cancellation among such terms. It decays to about 10⁻¹⁴ (see §2: the off-shell mode has rate −8).

---

## 2. Linearization at the ACH fixed point (derived; it explains the data)

Take fibre slot k and horizontal slots i, j. In the ACH regime (a_i, a_j ~ eᵗ, a_k ~ e²ᵗ), the potentials are:

- Pot_k = 2κ² + O(e⁻⁴ᵗ),
- Pot_i = Pot_j = −2κ² + 4e^{−2L_i} + …,

where κ = a_k/(a_i a_j) and ρ = a_i/a_j. The leading terms are independent of ρ.

**Fixed point.** At y = (1, 1, 2), the equation y_k′ = 0 reads 6 − 4 − 4 + 2κ² = 0. This forces κ = 1 for every ρ. The ACH fixed set is therefore a curve parametrized by ρ.

**Linearized system.** Use the variables

- s = δy_i + δy_j,
- m = δy_i − δy_j,
- v = δy_k,
- w = log κ.

They satisfy

- s′ = −6s − 2v − 8w
- v′ = −2s − 6v + 4w
- w′ = −s + v
- m′ = −4m + ΔPot
- (log ρ)′ = m

The characteristic polynomial of the (s, v, w) block is −(λ + 6)(λ + 8)(λ − 2).

**Constraint.** The linearized constraint is C = 3s + 2v + 2w, and C′ = −8C. So λ = −8 is the off-shell mode.

**Spectrum on the constraint surface:**

| Mode | Rate |
|---|---|
| (s, v, w) block | −6 |
| Unstable mode | +2 |
| Anisotropy m | −4 |
| log ρ (the CR modulus) | 0 |

The approach to the fixed point is set by the forcing 4e^{−2L_i} ~ e⁻²ᵗ. This is the coth t − 1 ≈ 2e⁻²ᵗ tail of exact complex hyperbolic space.

**Unstable eigenvector (λ = 2).** It is (δy_i, δy_j, δy_k, w) ∝ (−0.6, −0.6, 0.8, 1), with no m or ρ component. It gives a sign rule for the exit:

- w < 0 (κ < 1): y_k drops and y_i, y_j rise, so the trajectory heads to AH.
- w > 0 (κ > 1): the trajectory heads to the blow-up seen at r = 0.8 and r = 1.2, where y₃ → 60 and y₁,₂ → −52.

---

## 3. What the exact complex-hyperbolic runs actually show

In fibre-slot ordering, the exact solution has y_i = y_j = coth t and y_k = coth t + tanh t = 2 + O(e⁻⁴ᵗ).

**Slot-2 run (q, r) = (2/3, 1/6), at t = 6.2342.**
- Exact values: coth t − 1 = 7.69·10⁻⁶ and κ_exact = coth t.
- Measured deviations: δy_i = +5.62·10⁻⁶, δy_k = −7.49·10⁻⁶, w = −9.36·10⁻⁶.
- The eigenvector prediction from w is (−0.6w, 0.8w) = (5.62, −7.49)·10⁻⁶. This is exact to the printed digits.

**Slot-1 copy (q, r) = (1/6, 1/6), at t = 6.8558.**
- Measured: w = +2.70·10⁻⁶, δy_i = −1.62·10⁻⁶, δy_k = +2.16·10⁻⁶.
- This again matches the eigenvector, now on the κ > 1 side. The end state y = (2.07, 0.947, 0.947) is heading toward blow-up.

**Interpretation.**

1. The RHS and potentials are correct. If they were wrong, exact complex hyperbolic space would leave the fixed point at O(1) early on, not along the unstable eigenvector at the 10⁻⁵ level.

2. The integrator error is negligible against the seeded unstable mode. Extrapolating back, the seed amplitude is w e^{−2t} ≈ 3.6·10⁻¹¹ (slot 2) and 3.0·10⁻¹² (slot 1). This matches the effective cubic-coefficient error from roundoff at the initial radius, δc ~ ε_mach/t₀² ≈ 2.5·10⁻¹¹.

3. The horizon follows t_min ≈ ¼ ln(C/δ).
   - With δ = 3.6·10⁻¹¹, this gives t ≈ 6.0 + O(1), against the observed 6.23.
   - The two runs differ by Δt = 0.62. That corresponds to a seed ratio e^{4Δt} ≈ 12, matching 9.36/0.77 at a common time.

4. `min_dev` depends on the exit side and is not a precision measure.
   - On the κ > 1 side, the −0.6w shift cancels the exact +2e⁻²ᵗ excess in y_i, y_j. This is why slot 1 reaches 2.3·10⁻⁶.
   - On the κ < 1 side the two add, which is why slots 2 and 3 reach 2.0·10⁻⁵.
   - Better indicators are w and m measured relative to the exact tails.

5. The exit side for exact complex hyperbolic space is set by the sign of the roundoff. So the classifier "recovers" this space only up to the shadowing horizon. This is a property of the saddle, not a classifier error.

**Ways to extend the horizon.**
- Higher-precision integration.
- Variables a_i = t(1 + t²f_i), which remove the O(t⁻²) cancellation.
- Starting at larger t₀ with N ≈ 11. Since δ ∝ t₀⁻², this gains only ¼ ln of the ratio, about 1.7 in t.

---

## 4. The biaxial "nearby perturbations"

The biaxial line c₁ = c₂ contains:
- H⁴ at r = 1/3,
- complex hyperbolic space with fibre slot 3 at r = 2/3.

The sampled points r ∈ {−1, −0.3, 0, 0.1, 1/6, 0.25} are not near any complex-hyperbolic point. The comment "varying r around CH" conflates the slot-2 coordinate c₃ = 1/6 with the slot-3 point. For example, r = 1/6 gives c = (5/12, 5/12, 1/6), which is an AH solution.

The only perturbations of complex hyperbolic space in the data are r = 0.5 and r = 0.8. They lie at distances 1/6 and 2/15, with `min_dev` 0.71 and 0.61, so they never enter the saddle regime. What they do show:

- A transition AH → singular lies in r ∈ (0.5, 0.8).
- The exit sign rule already holds far from the saddle: κ = 0.66 at r = 0.5 (AH), and κ = 1.93 at r = 0.8 (singular).

On this line, ρ₃ = a₁/a₂ ≡ 1 exactly, because a₁ and a₂ obey identical ODEs with identical data. The value 1.0000000000018 is roundoff. The slot-2 point has ρ = a₃/a₁ = 1 for the same reason (c₁ = c₃). No perturbation of the slot-2 point was run.

**A cheap quantitative test the data still lack.** Bisect in r on the biaxial line.
- r* should converge to 2/3 down to the floor of about 10⁻¹¹.
- t_min should grow with slope ¼ in ln(1/|r − 2/3|).
- The AH-side end ratio a₃/a₁ should diverge as r → 2/3⁻. The ratio is not currently recorded in `einstein_nut_runs.json`.

---

## 5. Does this support the ρ reading on the O(−1) bolt?

### What transfers

- The slot indexing is identical in both scripts: `rho = exp(L[i]-L[j])` with i = k+1, j = k+2, so slot 1 gives a₂/a₃.
- κ → 1 holds as the fixed-point value.
- AH/singular separatrices pass through ACH via the +2 mode, with the side determined by sign(κ − 1).
- ρ = 1 corresponds to the standard CR structure on ker σ_k.

### What does not transfer

Any nontrivial value of ρ. On the bolt, a₂(0) = b while a₃(0) = 0, so nothing forces a₂/a₃ → 1. The bolt ρ is a genuine output, and the ball test never exercised such a value.

### What supports the bolt ρ instead

The derivation in §2:
- The unstable mode carries no m or ρ component at linear order.
- ΔPot = Pot_i − Pot_j is exponentially small both in the ACH regime and during the transit out of it.

Hence:
- ρ at closest approach equals ρ_∞ + O(e^{−2t_min}) + O(δ²).
- The AH-side terminal ratio a_i/a_j of near-separatrix trajectories converges to the same ρ_∞, while a_k/a_i → ∞.

This gives a second, independent readout of ρ. The bisection output does not record a₂/a₃ at the end of the `lo` (AH) side, so this second readout is not yet available.

The window dev < 0.05 used for `rossi_plateau_range` includes entry-tail times where the e⁻²ᵗ corrections are at the 0.05 level. A tighter error bar comes from fitting ρ(t) = ρ_∞ + A e⁻²ᵗ on the incoming branch.

### A concrete issue in `bisect` revealed by the ball runs

The slot-2 run exits the saddle at t ≈ 6.2 and at t = 12 is still at y = (1.25, 1.66, 1.25), about 0.25 from √2. `classify` labels a run AH only if it is within 2·10⁻² of √2 at T. Deeply bisected AH-side trajectories therefore become `other`, and `other` is lumped with "non-AH".

Once the bisection depth δ satisfies ¼ ln(1/δ) + τ_AH ≳ T, both endpoints can lie on the AH side of the true separatrix. The interval then no longer brackets it.

- **Check from stored output:** whether `hi_end` shows AH transit (y_k falling, y_i rising) rather than blow-up.
- **More robust side indicator:** the sign of κ − 1 just after closest approach. By the eigenvector, it determines the side immediately.

### The cross-check that would turn plausibility into calibration

Compute the ball separatrix Γ₃ through c = (1/6 + u, 1/6 − u, 2/3 + v). For each u, bisect in v and read ρ_∞(u) = a₁/a₂.

The u ↔ −u reflection maps ρ → 1/ρ, and the Rossi structures with ρ and 1/ρ are CR-equivalent. So:
- v(u) should be even,
- log ρ_∞(u) should be odd,
- Γ₃ should cross the biaxial line transversally. The data show it is not contained in that line, since r = 0.5 is AH and r = 0.8 is singular.

The ball map ρ_∞(u), checked by both readouts, is the calibration of nontrivial ρ against which the bolt values a₂/a₃ can be compared.

---

## 6. Generic ball parameters versus a continuum of ACH fillings, and Biquard

### Generic (q, r) are not ACH

The data show two open regions: AH (all r ≤ 0.5 on the biaxial line) and singular (r ≥ 0.8). ACH is codimension one, because of the single +2 mode.

The dimension count is consistent:
- Nut data form two parameters.
- Left-invariant diagonal conformal classes at AH infinity also form two parameters (the ratios a₂/a₁ and a₃/a₁).
- CR infinity data form one parameter (ρ).

So the ACH solutions form at most curves Γ_k through the three complex-hyperbolic points. They sit on the frontier where the AH conformal infinity degenerates (a_k/a_i → ∞ with a_i/a_j → ρ). Reading the whole (q, r) plane as ACH fillings does not hold, and the runs themselves contradict it.

### What Biquard's local deformation theory provides

For CR structures on S³ near the standard one, Biquard's theory gives ACH Einstein (self-dual) fillings of B⁴ near complex hyperbolic space, unique in that neighbourhood up to diffeomorphism. This includes the non-embeddable Rossi spheres, ρ ≠ 1. For a left-invariant Rossi datum, uniqueness makes the filling SU(2)-invariant. The sign-flip symmetries of the pairs (σ_i, σ_j) make it diagonal. So each such filling is a nut solution lying on Γ_k.

This predicts that Γ_k exists as a smooth curve near each complex-hyperbolic point, with ρ_∞ covering a neighbourhood of 1. It is a local statement:
- It does not give the global extent of Γ_k.
- It does not say whether ρ_∞ is monotone or saturates along Γ_k.
- It says nothing about the bolt topology.

### What is actually shown

- Exact complex hyperbolic space is shadowed to 10⁻⁵ up to t ≈ 6 in all three slots.
- The AH → singular transition on the biaxial line brackets r = 2/3.

No ball trajectory off the lines c_i = c_j was integrated near the separatrix. So the runs neither confirm nor test Biquard's curve, and they give no ρ ≠ 1 data.

### Unresolved items and what each needs

1. **Existence and shape of Γ₃.** This needs the transverse bisection described in §5, with ρ_∞ extrapolated in e⁻²ᵗ.

2. **Whether bolt ρ values coincide with ball ρ values.** This tells whether the same Rossi sphere has ACH Einstein fillings on both B⁴ and O(−1). It needs the two ρ maps computed with the same readout.

3. **Whether bisection limits are true ACH trajectories rather than horizon artefacts.** This needs plateau length versus ln|d − d*| with slope ¼, and endpoints that bracket correctly by the κ-sign test.