# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step19_exterior_null_line_LM_stationary_cells.md",
    "Sessions/S1003A01/workspace/scripts/perp_conformal_lm.py",
    "Sessions/S1003A01/workspace/scripts/conformal_stationarity_check.py",
    "Sessions/S1003A01/workspace/scripts/perp_lm.py",
    "Sessions/S1003A01/workspace/scripts/exterior_null_line.py",
    "Sessions/S1003A01/workspace/data/perp_tail/area/lm_x00.038_X128_d24.json",
    "Sessions/S1003A01/workspace/data/perp_tail/area/lm_x00.038_X512_d28.json",
    "Sessions/S1003A01/workspace/data/perp_conformal/scalar_solve_x00.038_X128_d24_p12.json",
    "Sessions/S1003A01/workspace/data/perp_conformal/scalar_solve_x00.038_X512_d28_p12.json",
    "Sessions/S1003A01/workspace/data/perp_tail/independent_x00.038_X512_d28.json",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md"
  ]
}
```

## Task

Read the Step-19 core–exterior result, the inherited exact conformal stationarity argument, and the new Step-20 radial-conformal scripts/results. Check the mathematics and scientific interpretation. In particular: (i) does g -> e^{2phi}g implemented as G->e^{-2phi}G, h->e^{2phi}h preserve the O(-1) bolt geometry and exact CH endpoint contact? (ii) Are the component residual sums and scalar-solve experiments meaningfully testing the Euler equation, given the fixed spectral ansatz and exact cG[0] redundancy? (iii) Is the conclusion justified that J-P tends rapidly to zero while the nonzero trace-free tail charge lambda can remain, but no smooth full critical exact-collar cell can exist? Identify any formula/sign/normalization or optimization flaw, and state the strongest supported mathematical conclusion and the most consequential next finite-interface computation.

## Output

# Verification memo: Step 19 core–exterior result and the Step-20 radial-conformal tests

## Summary

- **(i) The conformal map is correct.** g → e^{2φ}g, implemented as G → e^{−2φ}G and h → e^{2φ}h, preserves the O(−1) bolt and gives C² contact with CH at X. It also moves the bolt area, because φ(x₀) ≠ 0 in the stored runs.
- **(ii) The scalar-solve runs do not test the Euler equation of J₆.** They minimize ∫(s+24)² over φ with the shape coefficients frozen. Their J changes (−2.1×10⁻⁸ at X=128, −1.3×10⁻⁹ at X=512) are below the size of the evaluator discrepancies. An exact conformal-class identity, derived in §2, shows that the radial-conformal direction cannot move J by more than about the scalar energy, i.e. ≲ 10⁻⁷.
- **(iii) The three parts have different status.** "No smooth full critical exact-collar cell" is a theorem. "J−P → 0" is a theorem at any exact critical point, but only a two-point numerical trend for the cells. "λ ≠ 0 can persist" is consistent with an exact linear analysis, and the value λ ≈ 0.18 is a finite-X observation.
- **Several numerical inconsistencies need fixing.** They are listed in §4.

## 1. The conformal map: bolt and collar

**Bolt invariants.** At the bolt, F(x₀) = G(x₀) = 0 and w(x₀) = 0, with smoothness condition F′G′ = 1. Under the map, F̃ = e^{2φ}F and G̃ = e^{−2φ}G. At x₀ the terms in φ′ multiply F or G, which vanish there, so F̃′G̃′ = F′G′ = 1.

Geometrically, a₃ = √F → e^φ a₃ and dt → e^φ dt. Hence da₃/dt at the bolt is unchanged, so the normal circle period is unchanged.

**Smoothness at the bolt.** In the base, x − x₀ is a smooth even function of t. φ is smooth in x for x > 0, so e^φ is smooth and even in t. Therefore:
- a₃ stays odd in t;
- a₁ and a₂ stay even, and are rescaled by the same factor;
- w(x₀) = 0 survives, so the bolt remains a round S².

The O(−1) bolt is preserved exactly.

**The bolt area changes.** The bolt area becomes e^{2φ(x₀)}x₀, and φ(x₀) = Σ(−1)^k c_k. From the stored coefficients:
- X=128: φ(x₀) = −3.11×10⁻⁵, which equals the reported phi_min. The effective bolt area is 0.038(1 − 6.2×10⁻⁵) = 0.0379976.
- X=512: φ(x₀) ≈ −9.0×10⁻⁶.

So these runs mix an x₀-shift into the conformal direction. The X=512 area scan gives dJ/dx₀ ≈ 3.5×10⁻³ and d²J/dx₀² ≈ 11, i.e. the parabola minimum is near x₀ ≈ 0.0377, not 0.038. Including e^{2φ}x₀ as the bolt area makes this explicit. If a pure interior test is wanted, impose Σ(−1)^k c_k = 0.

**Collar contact.** The factor (1−u)³ makes φ, φ′ and φ″ vanish at X. The base record matches G, F, w and their first derivatives at X (independent check file). The glued metric is therefore at least C^{1,1}, curvature is bounded, and the quadrature on [x₀, X] gives the full J with no distributional term at X.

The same contact makes the relative Chern–Gauss–Bonnet and signature transgression terms cancel. This is needed for the identity in §2.

**The script's description of the conformal direction is not accurate.** The docstring says the gauge a₁² = x "does not contain compactly supported conformal variations". In the full diagonal class this is not true. Every radial conformal variation equals a shape variation plus a radial reparametrization x̃ = e^{2φ}x (monotone for small φ). When φ(x₀) ≠ 0 it also changes x₀. Since J is diffeomorphism-invariant, the gauge-fixed problem already contains these variations; only the finite Chebyshev truncation omits them.

So the conformal block tests completeness of the degree-24/28 ansatz, not a missing physical direction.

**Side effect on Step-19 tools.** After the map, a₁² = e^{2φ}x ≠ x. The tail-mode decomposition and exterior fit assume the x-gauge, so any conformal record must be re-gauged before λ is extracted. At |φ| ≤ 3×10⁻⁵ the effect is negligible.

## 2. Conformal Euler equation and what the experiments measure

**The variation formula is correct.** In Ric = −6g normalization:
- s̃ = e^{−2f}(s + 6Δ₊f − 6|df|²) and dṼ = e^{4f}dV;
- in four dimensions, δ∫|Ric|² = (1/3)δ∫s², because W is conformally invariant and χ is fixed;
- with e = s + 24, this gives

  δJ₆[2fg] = 4∫f(Δ₊s + 6s + 144) = 4∫f(Δ₊+6)e.

  Taking λ = 1 instead of 6 recovers (8.1) of the relative-cell note.
- The radial operator L e = −(e_tt + (W_t/W)e_t) + 6e in conformal_stationarity_check.py is (Δ₊+6)e, as stated.

**Exact conformal-class identity.** Use P = ½∫|W|² + (1/12)∫s² − 16π²χ, applied relative to the fixed collar. Then, for every conformal factor equal to 1 on the collar,

  **J₆(e^{2φ}g) = C_g + (1/3)∫(s̃+18)² dṼ + 36 Vol(g̃),**

where C_g depends only on the conformal class and the collar. Its Euler equation is (Δ₊+6)(s̃+24) = 0. Because Δ₊+6 is positive and e vanishes on the collar, this forces s̃ ≡ −24.

Consequences:
- The radial-conformal subproblem is a quadratic Yamabe problem.
- Its possible saving is J(g) minus its minimum over the conformal class.
- A quadratic model gives a saving of order ‖e‖², roughly half of J − P or less. That is about 1.5×10⁻⁸ at X=512 and 1.7×10⁻⁷ at X=128.
- The observed changes, 1.3×10⁻⁹ and 2.1×10⁻⁸, are consistent with this. The radial-conformal completion cannot change η at any precision that matters.

**What scalar-solve actually minimizes.** The same computation gives

  δ∫e² dV = 12∫f(Δ₊+8)e,  while δJ = 4∫f(Δ₊+6)e  and  δP = ∫fΔ₊e.

So the scalar-solve stationarity condition is the projection of (Δ₊+8)e, not of the J-Euler operator (Δ₊+6)e. It is also computed with the shape frozen.

The outputs show that this moves the point off joint stationarity:

| X | shape gradient (seed) | shape gradient (after) | conformal gradient of full J (after) |
|---|---|---|---|
| 128 | 1.6×10⁻⁵ | 1.4×10⁻³ | 3.5×10⁻⁵ |
| 512 | 1.5×10⁻⁶ | 4.1×10⁻⁴ | 2.6×10⁻⁵ |

The growth of the shape gradient by two orders comes from a stiff shape–φ cross-Hessian near the bolt, where φ is largest. Its small effect on J is a quadratic-model statement, not a measurement. The full-J conformal gradient at the seed (c = 0) is not reported in the supplied data.

**The meaningful versions of the test** are already present in the script but have no supplied outputs:
- the default joint least-squares branch (shape + φ, minimizing J);
- the `--phi-only` branch with the full residual;
- direct L e profiles from the stationarity check.

The quantity to report is the joint-LM decrease of J, together with ⟨(1−u)³T_k, (Δ₊+6)e⟩ at the seed.

**The cG[0] redundancy.** In the current script, z0[deg] is set to 0 before every branch. The stored scalar-solve records still contain z[24] = −1.117×10⁹ (X=128) and z[28] = 5.46×10⁴ (X=512), copied from the LM seeds. The data therefore came from a different code version.

The Hessian null eigenvalue shows the coordinate drops out algebraically. However, the docstring says it "cancels identically". If that is a float subtraction, a 10⁹ coefficient injects about 10⁻⁷ relative roundoff into G and its derivatives. A one-line test settles it: compare R(z) with R(z with cG[0] = 0).

**Normalization error in conformal_stationarity_check.py.** The script uses dv = π²W/(2√G) dx, i.e. π²W dt. The residual normalization in perp_lm.py, P/8π² = ¼∫W|z|²dt with |E|² = |z|², requires dV = 2π²W dt (∫σ₁σ₂σ₃ = 2π²).

As a result, `scalar_energy_over_8pi2` is half the residual `scalar` channel. The rms ratios are unaffected because they are normalized by the same weight.

Two smaller points in the same scripts:
- The "interior" sup excludes u < 0.01, i.e. x < 1.1x₀, which is the region where φ and the saving are concentrated.
- `sample_geometry`'s min_G ≈ 3×10⁻⁹ only reflects G(x₀) = 0. The meaningful positivity quantity is G/(x−x₀), as in the independent check, where it is 1.117.

## 3. J−P, λ and nonattainment

**(a) No smooth critical exact-collar cell: a theorem.** Two arguments apply.
- **General argument.** Proposition 2 of the relative-cell note uses the conformal Euler equation to get e = 0, then the tensor equation (8.2) and unique continuation from the open collar to get E = 0. The glued metric would be locally CH, which contradicts π₂ ≠ 0 from the exceptional sphere.
- **Direct argument in the diagonal class.** Diagonal SU(2)-invariant metrics are the fixed set of the compact group SU(2) × (quaternion group). The quaternion group normalizes the collapsing U(1), so it extends over the bolt. By Palais' principle, a critical point in this class is a full critical point. The radial Euler system is an ODE, and exact CH Cauchy data at X then propagate CH down to the bolt. The CH/Calabi family G = x + x² + m/x with m = 0 has no bolt. (The m ≠ 0 members are excluded by their forced cone angle.)

**How nonattainment appears at finite X.** The Euler equations can hold on (x₀, X) while their transmission conditions at X fail. The Step-19 finite-X exterior solution shows this explicitly: μw′ = ν − λG_X, so w′(X⁻) = ν/μ(X) ≠ 0. That is a jump of z, the trace-free Ricci, across the matching sphere.

The LM cells are critical points of "metric equal to CH beyond X, C¹ match". They are not smooth critical points, and must not be. The measurable form of Proposition 2 is z(X⁻) or ν; this is not yet reported.

**(b) J−P → 0: theorem at critical points, two-point trend for the cells.**
- At any smooth critical point (Δ₊+6)e = 0. With e regular at the bolt and decaying on the collar, positivity gives e ≡ 0. This holds for an exact collar and also for an infinite asymptotically-CH collar, given the decay.
- Separately, s ≡ −24 is attainable with an exact collar in the full diagonal class. In x-gauge, s is first-order linear in G, so one ODE fixes G from the bolt and leaves a single matching condition on (F, w). Hence J = P costs nothing structurally.
- Numerically, J−P is 3.46×10⁻⁷ at X=128 and 3.35×10⁻⁸ at X=512, roughly X^{−1.7}. Two points support "decreasing", not a rate.

**(c) λ ≠ 0: consistent at linear order, observed at one X.** In the antisymmetric exterior, kθ enters only through its derivative. The shift θ → θ + C/k is the non-decaying squashing mode. λ is the conserved costate of that shift, which is why it is constant.

The profile μw′ = −λG solves the linearized Euler equation of P exactly. The scalar curvature vanishes identically in this sector, so a decaying exterior with any λ is consistent with e = 0. λ measures the first-order force toward squashing the conformal infinity, which the exact collar forbids.

Proposition 2 does not exclude a smooth critical point of the infinite-collar asymptotically-CH problem with λ ≠ 0. The note's distinction between that problem and the exact-collar problem is the correct one.

What the data do not yet show is λ_X converging: only X=512 is fitted, on [4, X/8]. λ at X = 128, 256 and 512 for x₀ = .038 is needed.

## 4. Numerical inconsistencies in the Step-19 tables

1. **Two evaluators are mixed.** The table and the X=512 area scan quote DualCell J = 0.9951812 (X=512, x₀=.038). The residual sum and the independent evaluator, converged across nq = 200/400/800, give 0.99517819. The DualCell offset is 3.0×10⁻⁶ at X=512 versus 3.9×10⁻⁷ at X=128, so it grows with X.
   - The quoted agreement j(256)−j(512) = 1.85×10⁻⁵ (observed) versus 1.89×10⁻⁵ (predicted) is within this offset, so it is good to about 15%, not 2%.
   - With the correct evaluator, j∞ ≈ 0.995166 instead of 0.995169. η changes only negligibly.
2. **Sign of λ in exterior_null_line.py.** The optimal ψ′ = (δ/I)G/μ, so μw′ = −λG gives λ = −δ/I, as in the note. The script sets `lam_pred = delta/Iinf`, and its docstring says "lam = delta/I". With δ < 0 the script's λ_from_trace is negative while λ_fit is positive. The table entries (0.1833 vs 0.1827) agree only after a sign flip.
3. **Predicted exterior costs check out.** The predicted cost of 1.531×10⁻⁴ is the finite-X value λ²I + 1.2×10⁻⁵ = 1.41×10⁻⁴ + 1.2×10⁻⁵. This is consistent.

## 5. Strongest supported conclusion

1. In the perpendicular diagonal class, every smooth critical metric with an exact CH collar is excluded. Every smooth critical metric, with exact or asymptotic CH collar, has s ≡ −24.
2. The radial-conformal subproblem is the quadratic Yamabe functional (1/3)∫(s̃+18)² + 36Vol. Its maximal saving on the Step-19 cells is ≲ 10⁻⁷. The Step-19 values j(X) are therefore insensitive to the conformal completion, with float η ≈ 4.8×10⁻³ at X=512.
3. The infinite-collar minimizer appears to be asymptotically CH with an off-null antisymmetric far field. Its constant costate λ ≈ 0.18 is conjugate to the squashing of the conformal infinity, and it carries zero scalar defect.
4. Finite-X nonattainment takes the form of a trace-free Ricci jump at X, of size ν/μ(X).

Through the relative-cell formula, j < 1 gives a balanced coefficient 4 − 8η/9 < 4. This depends on certified j. The Arb runs are still pending, and the evaluator discrepancy in §4 must be resolved first.

## 6. Most consequential finite-interface computation

**Main computation.** Minimize J_core[x₀, ρ] + δ(ρ)²/I(ρ) over cells with free data at ρ, at ρ = 5, 10 and 20, including the x₀ scan.

- The terminal penalty imposes natural transversality conditions at ρ: μw′(ρ⁻) = −λG(ρ), and θ-costate equal to λ. The core minimizer then satisfies the Euler system across ρ to linear exterior accuracy, i.e. it is the actual smooth critical candidate of the infinite-collar problem.
- **Expected outputs:**
  - j∞ independent of ρ up to cubic corrections in v₋(ρ);
  - λ independent of ρ, to be compared with 0.1827;
  - removal of the (log X)²/X² truncation altogether.
- **Required extension below ρ ≈ 10.** The symmetric U(2) sector needs its own transparent penalty. It has a null line given by the Calabi mass m, which is exactly Kähler–Einstein, plus a squashing mode. This should be derived as δ₊²/I₊ before using ρ = 5, where v₊ is no longer negligible.

**Two cheap cross-checks on the same records:**
1. Report z(X⁻) or ν for the X = 128, 256, 512 cells. This is the numerical signature of Proposition 2, and it should decay with X.
2. Compute N from (6.4) of the relative-cell note via r = ua. Under the identification a² = x²e^w, the geometric mean of the two non-collapsing slots, the Step-19 metric is a diagonal triaxial cell of §6.1. Then verify identity (6.5) and the window (6.7), including N > 4πt_E. These are evaluator-independent identities that any j < 1 cell must satisfy, so they give an independent test of the residual code.