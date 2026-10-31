# TTCS Independent Branch Record

```json
{
  "step_id": 6,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step5_slice_charge_and_zero_flux.md",
    "Sessions/S1003A01/workspace/scripts/transgression_triaxial.py",
    "Sessions/S1003A01/workspace/scripts/perp_dual_cost.py",
    "Sessions/S1003A02/workspace/scripts/o11_perp_cell.py",
    "Sessions/S1003A02/workspace/notes/step8_first_order_cell_law_ASD_Qprinciple.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md"
  ]
}
```

## Task

Develop the strongest viable analytic mechanism for the perpendicular fixed-slot diagonal Bianchi-IX O11 cell. The bolt-adapted transgression has T/8π²=Y²+Pi, with Y=-1 and Pi=0 at the O(-1) bolt, while on the complex-hyperbolic collar the charge transfers to Pi and Y=0. Numerical near-minimizers make T dip close to zero before Pi grows to the collar charge, and P and J remain slightly above 8π². Seek an exact boundary/interior decomposition or variational inequality that controls this charge transfer by trace-free Ricci energy P or by J; include the scalar-deviation distinction J=P+(1/4)∫(s+24)^2. Use cohomogeneity-one geometry, Chern–Weil transgression, flux/defect variables, Hamiltonian completion of squares, or calibration ideas as appropriate. Formulate explicit candidate inequalities and say which can plausibly be proved from the existing variables, rather than generic suggestions.

## Output

# The perpendicular O11 cell as a three-channel Chern–Simons transfer problem

The main result is an exact decomposition of P and J for every perpendicular diagonal Bianchi-IX cell. It yields a provable threshold P ≥ 8π² whenever one sign condition holds. The same decomposition isolates a single term of indefinite sign: a cubic, non-abelian term that transfers charge from the bolt channel to a transverse channel.

A second-order analysis of the scale-invariant middle region, x₀ ≪ x ≪ 1, then predicts that this term grows like x₀² log(1/x₀). The existing peer data already show this logarithm with the predicted coefficient. Above a computable small x₀ the threshold therefore appears to hold; below it, the analysis predicts subthreshold P and J. That is the opposite of a universal lower bound. The prediction rests on a round-weight model of the middle region and on three-figure data, so it needs the computations described in §6.

Conventions follow `perp_dual_cost.py`: Ric_CH = −6g, x = sinh²ρ, and bolt-adapted labels (a, b, c) = (transverse, CH fibre, bolt).

## 1. Exact variables: the slice charge is a symmetric cubic

Define the components of the self-dual Levi-Civita connection in the frame ω_i = e⁰∧eⁱ + eʲ∧eᵏ:

  α_i = (a_j² + a_k² − a_i²)/(a_j a_k) − a_i′.

α_i = 0 means Λ⁺ is parallel along e_i. Two facts follow:
- α_i ≡ 0 in flat space.
- α_1 = α_2 = 0 exactly when ω_3 is Kähler.

The Step-5 variables are these connection components in disguise:

  p₊ = −e^{−w} α_1,  p₋ = −e^{w} α_2,  Y = −α_3 + ½ α_1 α_2.

Substituting gives

  **T/8π² = CS(α) = α_1² + α_2² + α_3² − α_1α_2α_3.**

This is the Chern–Simons functional of the SU(2)-invariant Λ⁺ connection, which is consistent with p₁(Λ⁺) = 2χ + 3τ.

Consequences of this form:
- **Y² + Π is one of three square completions.** It completes the square in channel 3.
- **Endpoint and model values check out:**
  - O(−1) bolt: α = (0, 0, 1), so CS = 1.
  - Exact perpendicular CH collar (a = c = sinh ρ, b = sinh ρ cosh ρ): α = (0, −3x, 0), so CS = 9x². At X = 1 this is the `expected_T_collar = 9`.
  - Aligned CH: α_3 = −3x, which reproduces Y = R²/2.
  - Burns metric: α = (0, 0, x₀/x), so CS = (x₀/x)².
  - Taub–NUT slice: α = (−1, −1, 2), so CS = 4, giving 32π².
  - On Kähler slices, α_3 is the Ricci-form potential, which explains Y = −A.
- **Completion adapted to the perpendicular cell** (in channel 1):

  CS = Y₁² + Π₁,  Y₁ = α_1 − ½α_2α_3,  Π₁ = α_2² + α_3² − ¼α_2²α_3².

  Here Y₁ = 0 at both ends, so no intermediate-value slice exists. This is why the zero-flux certificate has no perpendicular analogue.
- **The depth of the T-dip measures u = α_2α_3.** Since Π₁ ≥ 2|u| − u²/4,

  T/8π² ≥ Y₁² + 2|u| − u²/4.

**Curvature in these variables.** The Λ⁺ curvature is

  Fⁱ = α_i′ dt∧σ_i + ∂_iCS σ_j∧σ_k.

Set V = a_1a_2a_3, dV = 2π² V dt, and

  X_i = α_i′/a_i,  Z_i = ∂_iCS/(a_j a_k),  λ_i = ½(X_i + Z_i),  μ_i = ½(X_i − Z_i).

Here λ_i are the R⁺ eigenvalues and μ_i the Λ⁻→Λ⁺ (trace-free Ricci) block. These normalizations are pinned by three checks: CH gives λ = (0, −6, 0), Burns gives λ = 0, and Chern–Weil holds. The energy densities are

- |Ric°|² = 4Σμ_i²,
- 4|W⁺|² + s²/12 = 4Σλ_i²,
- s = 4Σλ_i,
- |Ric + 6g|² = 4Σμ_i² + 4(Σλ_i + 6)².

With weights m_i = a_j a_k/a_i, the energies take a Bogomolny form:

  P = 2π² ∫ Σ m_i (α_i′ − m_i⁻¹ ∂_iCS)² dt,
  4∫|R⁺|² = 2π² ∫ Σ m_i (α_i′ + m_i⁻¹ ∂_iCS)² dt.

So **Einstein means upward m-gradient flow of CS, which is free in P. Scalar-flat with W⁺ = 0 means downward flow, which costs exactly 8π² times the descent.** Each channel can independently be in either mode. The minimal P is therefore a minimal-descent (Floer/instanton-type) path problem in α-space.

## 2. Exact decomposition for perpendicular cells (provable now)

The relevant end data are:
- α_3 runs from 1 at the bolt to 0 at the collar;
- α_1 α_2 → 0 at both ends.

Use the identity α_3′ = 2a_3λ_3 − m_3⁻¹∂_3CS and complete the square in λ_3. The two quartic terms cancel exactly, leaving

  **P − 8π² = 8π² ∫ V λ̃_3² dt + P_1 + P_2 − 16π² ∫ m_3⁻¹ α_1 u dt,**

where
- λ̃_3 = ½[α_3′/a_3 + (2α_3 + α_1α_2)/(a_1a_2)] is the channel-3 self-dual combination with the cubic sign reversed,
- P_i = 4∫μ_i² dV,
- u = α_2α_3.

Adding the scalar term gives the J version:

  **J − 8π² = (same right side) + 4∫(Σλ_i + 6)² dV.**

An equivalent cruder form is P = 8π²(1 + K_3) + 4∫λ_3² + P_1 + P_2, with K_3 = ∫α_1α_2 dα_3.

**Theorem shape.** Every perpendicular diagonal cell with α_1 u ≤ 0 throughout satisfies P ≥ 8π², and hence J ≥ 8π². Equality would force λ̃_3 = μ_1 = μ_2 = 0 together with α_1 u ≡ 0. Proposition-2-type unique continuation should exclude this; that step remains to be written. The theorem is pure algebra plus end values. It contains the case α_1 ≡ 0, in which channels 2 and 3 decouple and the bolt charge α_3² must be paid in full.

**Why the slice-dip route cannot close.** For any slice, the in-region identity gives

  J − 8π² ≥ ∫_in [4|W⁺|² + (s+18)²/3 + 36] − T(t).

Near the superposition the dip occurs at x_* ≈ √(x₀/3), where T ≥ 8π²(2|u|) ≈ 48π²x₀. The floor 36·Vol(in) ≈ 6π²x₀ is smaller by a factor of 8. The channel decomposition above is the correct replacement.

**Exact calibration form.** P ≥ 8π²[Φ(bolt) − Φ(collar)] holds for all cells if and only if Φ(a, α) satisfies a Hamilton–Jacobi inequality, which is itself exact:

  Σ_i m_i⁻¹ [∂_{α_i}Φ ∂_iCS − (∂_{α_i}Φ)²] + Σ_i ∂_{a_i}Φ · a_i′(a, α) ≥ 0,

with a_i′ = (a_j² + a_k² − a_i²)/(a_j a_k) − α_i and scale invariance reducing the state space to five dimensions.
- For J, add 8π² V (ΣZ_i + 6 + Σβ_i/2a_i)² to the integrand, where β_i = α_i′ − m_i⁻¹∂_iCS.
- Φ = α_3² fails this inequality by exactly −2 m_3⁻¹ α_1 u. The cubic term is the only obstruction to the abelian calibration.

## 3. The logarithmic cubic drain

In the middle region x₀ ≪ x ≪ 1, take round weights and s = log x. Then

  P_i ≈ π² ∫ (2α̇_i − ∂_iCS)² ds,
  drain = −8π² ∫ α_1 u ds.

The base profiles are α_3 = x₀e^{−s} (Burns, λ_3 = 0) and α_2 = −3e^{s} (CH, μ_2 = 0). Two facts make the drain grow with log(1/x₀):

- **u is an adiabatic invariant equal to −3x₀.** With channel 3 in ASD mode and channel 2 in Einstein mode,

  u′ = 2u(m_2⁻¹ − m_3⁻¹) − α_1(α_3² m_2⁻¹ − α_2² m_3⁻¹),

  which is negligible in the middle region. The bubble tail (∝ r⁻²) and the background (∝ r²) multiply to a scale-free constant.
- **The non-abelian bracket feeds channel 1 at a constant rate.** The bracket [A_2, A_3] ∝ T_1 forces channel 1 uniformly in log scale. Per unit s, the α_1-dependent energy is

  (2α̇_1 − 2α_1 + u)² − 8uα_1 + O(α_1²(α_2² + α_3²)).

  The Euler–Lagrange equation α̈_1 = α_1 − 3u/2 locks α_1 to 3u/2 over the middle region, with O(1) ramps at each end. The resulting rate is −8π²u² per unit s.

This gives the prediction

  P_min/8π² = 1 + x₀²(C − 9η² log(1/x₀)) + …,

where η = u/(−3x₀) ≈ 1 and C collects the end costs. Partial locking at α_1 = u/2 is the channel-1 CS-critical point Y₁ = 0. There channel 1 costs nothing (λ_1 = μ_1 = 0), and the rate is −u²/2, i.e. −4.5 x₀² per unit log(1/x₀).

**Comparison with the peer data.** The reported values give (P/8π² − 1)/x₀² + 4.5 log(1/x₀) = 41.1, 40.5, 40.7 at x₀ = 10⁻³, 3·10⁻³, 10⁻². These are constant to within the two-digit precision of the inputs. The larger x₀ deviate (36.9 at 0.03, 25.8 at 0.1), as expected from higher-order terms.
- **Half-locking at C ≈ 41** predicts a sign change at log(1/x₀) ≈ 9.1, i.e. x₀ ≈ 1.1·10⁻⁴. The minimal deficit is about 10⁻⁸ near x₀ ≈ 7·10⁻⁵.
- **Full locking** doubles the slope. If its end constant is similar, the sign change moves to x₀ ≈ 10⁻², with a deficit of order 10⁻⁴. The full-locking end constant is not known yet.

**Remaining effects in this model.** Metric back-reaction of constant α_1 is a steady anisotropic cone, δ_1 = −c/2, δ_2 = δ_3 = −c/4, which can be ramped smoothly. The bulk weight corrections (1 + O(x)) alter only O(x₀²) terms. No source of log(1/x₀)-scale cost was found. Bolt-side corrections, ramp costs and the collar cutoff of the Burns tail enter only C.

**The aligned case has no drain.** There the bubble and CH charges share one abelian channel, and α_3 crossing zero is the zero-flux slice.

## 4. J and the scalar-deviation distinction

At first order J and P agree in the perpendicular orientation. The quantity s + 24 is O(x₀) in the middle region plus a core of volume O(x₀²), so J − P = ¼∫(s+24)² is O(x₀²) up to logarithms. At second order the two differ:

- **Half-locking:** λ_1 = 0, so there is no 1/x scalar term and J inherits slope −4.5.
- **Full locking:** λ_1 = u/x gives s + 24 = 4u/x, which adds +u²/2 per unit s.
- **Optimizing J** over constant modes α_1 = c and α_2 shift d_2 gives
  - per-unit-s energy 6c² − 14cu + 1.5u² after minimizing over d_2,
  - minimizers c = 7u/6 and d_2 = −u/3,
  - rate −(5/6)u², i.e. −7.5 η² x₀² per unit log(1/x₀).

So J is predicted to drain as well. By (2.3) of the relative-cell note, a single-bubble cell with J₁ < 8π² gives

  E/h → 4 − (8/9)(1 − J₁/8π²).

## 5. Orientation dependence and links

Since Λ⁺ ≅ so(3), the drain term is u·⟨α_⊥, ζ × ω_CH⟩. For a general relative angle θ, the predicted cell law is

  8π²[1 + 6x₀ cos²θ + x₀²(C − κ sin²θ log(1/x₀))],

which is minimized at θ = π/2. Consequently a lower-bound theorem for fillings would have to be second-order sharp and non-abelian.

The log(1/x₀) arises because the product of the bubble's r⁻² tail and the background's r² growth is scale-free. The same mechanism should underlie logarithmic second-order terms in the literature on the second obstruction to Einstein desingularization of orbifolds; the relevant sources are Biquard and Ozuch.

## 6. Computations that distinguish the scenarios

1. **Decomposition on existing records.** From `adapted_slice`, the α_i follow directly:
   - α_1 = −√(e2w)·pp,
   - α_2 = −pm/√(e2w),
   - α_3 = −Y + ½·pp·pm.

   Evaluate all four terms of §2 on the stored perpendicular near-minimizers. Computing P − 8π² as this sum of small integrals avoids cancelling against 8π², which makes x₀ down to about 10⁻⁵ accessible.
2. **Locking profile.** Plot α_1(s)/u(s) and u(s)/(−3x₀) across log x. A plateau of α_1/u at 1/2 versus 3/2 identifies partial versus full locking. Also compare min T with 8π²(2|u| − u²/4).
3. **Seeded optimizations.** Seed full locking, α_1 ≈ −4.5x₀, at x₀ = 10⁻² and 3·10⁻³. Use both targets P and J and higher anisotropy degree. Read off the slope of (P/8π² − 1)/x₀² against log(1/x₀): −9 for P at full locking, −7.5 for J at the optimal constant modes. Check whether the sign changes.
4. **Value function.** If a log(1/x₀)-scale cost appears that the round model misses, it will show up as a Hamilton–Jacobi subsolution with Φ(bolt) − Φ(collar) = 1, computable numerically on the reduced five-dimensional state space. Such a subsolution would prove the diagonal-class threshold.