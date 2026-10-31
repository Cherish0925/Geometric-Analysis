# TTCS Independent Branch Record

```json
{
  "step_id": 30,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md",
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/notes/step29_collapsed_saturation_value_four.md",
    "Sessions/S1003A02/workspace/scripts/collapse_chiral_charge_limit.py",
    "Sessions/S1003A02/workspace/data/collapse_chiral_charge_limit.json",
    "Sessions/S1003A02/workspace/scripts/beta_pinning_identity.py",
    "Sessions/S1003A02/workspace/data/beta_pinning_identity.json",
    "Sessions/S1003A02/workspace/data/beta_pinning_threshold.json",
    "Sessions/S1003A02/workspace/data/saturation_control/step30_anisotropic_summary.json"
  ]
}
```

## Task

Independently verify the new Step-30 mathematics. In particular: (i) starting from the chiral transgression, check Lemma Q'' and the exact controlled-collapse limit b_+^{end}=-2-(C+4X)^2 under x=X z^3+o(z^3), p=Pz+o(z), chi=Cz+o(z), eta=Nz+o(z); determine whether the asymptotic assumptions really represent finite-curvature/F-structure control and whether any missing first-jet term changes the formula; (ii) check the fibre/base observable B~=log(kappa/sqrt(1+zeta))+(v-kappa^{-1})/4, its CH vanishing, the derivative B~'=F_beta-E/4, tensor coefficient P_hat >= (1/6)∫WE^2, the Cauchy-Schwarz constant, CH tail integral, and mismatch threshold 0.3702 at T=.70; (iii) interpret the raw anisotropic numerical runs without treating them as regular-bolt constructions. Give explicit corrections if needed and explain what is rigorously established for the diagonal Einstein-gap programme.

## Output

# Verification memo: Step 30 (Q″, controlled-collapse charge, fibre/base pinning, anisotropic scan)

**Summary of results**

- **Lemma Q″** is correct. Its hypothesis can be stated more precisely: convergence of the three Λ⁺ connection coefficients is what is needed.
- **The b₊ formula (5)** is algebraically correct. Its stated geometric meaning is not: the ansatz `x = Xz³` with `X ≠ 0` is not finite-curvature collapse.
- **The `bminus_limit` in the JSON is wrong.** The correct limit is `b₋ = 2 + (C−4X)²`.
- **The pinning identity (8)–(10) is correct.** The threshold 0.3702 is numerically correct as stated, but it is improvable to 0.3308, and its use of the CH tail integral needs one comparison that has not been proved.
- **The raw-η numerics follow a single law:** cost ≈ 2 − b₊(entry). With the bolt charge included, this law shows the raw runs cannot undercut the Burns threshold.

---

## 0. Closed forms for the chiral charges (independent derivation)

**Connection.** For `g = dt² + Σ aᵢ²σᵢ²` with `dσᵢ = 2σⱼ∧σₖ`, Cartan's equations give

- `ω_{i0} = pᵢσᵢ` with `pᵢ = aᵢ'`;
- `ω_{jk} = γᵢσᵢ` with `γᵢ = (aⱼ² + aₖ² − aᵢ²)/(aⱼaₖ)`.

So the Λ± connections are diagonal in the σ-gauge, with coefficients `uᵢ = pᵢ − γᵢ` and `wᵢ = pᵢ + γᵢ`.

**Curvature and Chern–Simons density.** For a connection `Σvᵢσᵢ`, the curvature is

  `F_i = vᵢ' dt∧σᵢ + (2vᵢ − vⱼvₖ) σⱼ∧σₖ`.

Since `d/dt(Σv² − Πv) = Σvᵢ'(2vᵢ − vⱼvₖ)`, the quantity `Σv² − Πv` is the Chern–Simons density.

**Charges.** With the orientation fixed by the model orbits:

  **b₊ = 2 − Σuᵢ² − u₁u₂u₃,  b₋ = Σwᵢ² − w₁w₂w₃ − 2.**

I checked both formulas against every row of the Step-27 table:

| orbit | u | b₊ | w | b₋ |
|---|---|---|---|---|
| smooth centre (`aᵢ = t`) | 0 | 2 | (2,2,2) | 2 |
| O(−1) bolt (`p = (0,0,1)`, `γ = (0,0,2)`) | (0,0,−1) | 1 | (0,0,3) | 7 |
| CH, radius t | (0,0,3sinh²t) | 2 − 9sinh⁴t | (2cosh t, 2cosh t, sinh²t + 2) | 2 − 3sinh⁴t |
| biaxial Berger, any U | (−2,U,U) | −2 | (2,U,U) | 2 |
| Burns | (0,0,−m/r²) | 1 → 2 | — | — |

The CH and Burns rows show the expected U(1)-reduced (Kähler) form of A⁺.

**Consequences used below.**

1. b₊ depends only on u, and b₋ only on w.
2. Writing `u_h = −2 + δ` gives the exact identity
  **b₊ = −2 − (u_f − u_g)² + δ(4 − u_f u_g) − δ².**  (★)
3. **Period of the invariant.** Every non-trivial left-invariant flat Λ⁺ connection, such as `u = (−2,2,2)` or `(−2,−2,−2)`, has `b₊ = −2`. So the difference 4 between the round value (2) and the Berger value (−2) is exactly one period of the Λ⁺ Chern–Simons invariant (π₃(SO(3)) shift). This suggests that the "value four" of Step 29 is quantized. Whether the collapsed A⁺ is gauge-equivalent to the unit-winding flat connection on general F-structure necks has not been established.

## 1. Lemma Q″

The proof is correct: integrate (1.1)₊ and drop the terms that are ≥ 0.

**Hypothesis.** "Convergence of the scale-free first jet" is ambiguous at a collapsed end. In the variables (x, z, p, χ, η), the jets all converge to the same point, yet u depends on the rates x/z³ and χ/z. The exact hypothesis is convergence of the coefficients u (for b₊) or w (for b₋).

**Rigorous form for paths that never become round.** The usable statement is

  `P̂[t₀, t₁] ≥ sup_{t₀ ≤ s ≤ t₁} b₊(s) − b₊(t₀)`.

## 2. The controlled-collapse formula

**Algebra (verified).** The script's u-limits are reproduced:

- `γ_f → −2X`, `γ_g → 2X`, `γ_h → 2`;
- `p_f → P + 2C/3 + N/3`, `p_g → P − C/3 + N/3`, `p_h → 0`.

Since `u_f − u_g = C + 4X`, (★) with δ = 0 gives `b₊ = −2 − (C + 4X)²`. The terms `o(z³)` and `o(z)` do not contribute. P and N cancel exactly.

**Correction to the JSON b₋.** The script computes `bm` from the u-limits with a flipped product sign. The correct w-limits are

  `(P + 2C/3 + N/3 − 2X, P − C/3 + N/3 + 2X, 2)`,

which give **b₋^end = 2 + (C − 4X)².** The JSON expression returns −2 at C = X = 0, contradicting the table value 2. It follows that:

- N enters neither limiting charge, so the Step-30 sentence saying N "enters the opposite chiral charge" is incorrect.
- The Euler flux is `b = −8CX`.
- The signature transgression is `s = 2 + C² + 16X²`.

**Is this finite-curvature collapse? Not for X ≠ 0.**

- *Intrinsic curvature.* The orbit Ricci tensor is `Ric⁽³⁾ᵢᵢ = 2γⱼγₖ/(aⱼaₖ)`; this is exactly `Pot_i`, and I checked it against `Pf`, `Pg`, `Ph`. With `a_h = ε` and `a_f ≈ a_g ≈ R`:
  `Ric⁽³⁾_ff ≈ 4/R² + 8X/(Rε)`,  `Ric⁽³⁾_gg ≈ 4/R² − 8X/(Rε)`.
  Only `Ric_hh = O(X²/R²)` is bounded. Bounded orbit curvature requires `γ_f, γ_g = O(ε/R)`, that is **x = O(z⁶)**, so X = 0.
- *Ambient curvature.* By the Gauss equation with bounded `R kᵢ`, the 4D curvature is of order `8|X|/(Rε)`.
- *Consistency signal.* The nonzero Euler flux `−8CX` is the trace of this unbounded curvature. Under bounded geometry the Euler transgression must vanish (Cheeger–Tian mechanism), and it does when X = 0.

**C ≠ 0 is compatible with bounded curvature on one orbit only, not on a collar.**

- *Single orbit.* `C = lim χ/z = R x' = R(k_f − k_g)`. On a single orbit this is bounded base shear and is allowed.
- *Collar.* On a collar of width ≫ ε with `|Rm| ≤ K/R²` and `|k| ≤ K/R`:
  - the identity `Ric_ff − Ric_gg = −(x'' + θx') + 16x/ε² + …` gives `|x| ≲ Kε²/R²` and `|x'' + θx'| ≲ K/R²`;
  - interpolation over length ε then gives `R|x'| = O(ε/R)`, hence χ = O(z⁴) and C = 0.
- *Along a trajectory.* With η ~ Nz, one has `dx/dz = −3C/(Nz)`. This is incompatible with x = O(z³) unless C = 0.

**What is rigorous (diagonal adiabatic-charge statement).** Suppose an orbit has:

- `a_h/R → 0`;
- `R²|Ric⁽³⁾| ≤ K`;
- `R|kᵢ| ≤ K`.

Then `δ = a_h k_h + (2 − γ_h) → 0`, the coefficients u_f, u_g stay bounded, and `u_f − u_g = R(k_f − k_g) + o(1)`. Hence

  **b₊ = −2 − (R(k_f − k_g))² + o(1) ≤ −2 + o(1),  b₋ ≥ 2 − o(1).**

Equality holds under collar control. By Q″, any later rise to a round orbit costs at least 4 − o(1). No expansion ansatz is needed. This is the correct form of (5)–(6); the X-terms belong to unbounded-curvature jets.

**The first-jet term that can change the formula.** The term is δ = u_h + 2, the opening rate of the collapsing circle. Equation (★) shows that b₊ can exceed −2 only through δ > 0 with `δ(4 − u_f u_g) > δ² + (u_f − u_g)²`. The ansatz forces δ → 0. This is exactly the term carried by raw η (§4).

## 3. Fibre/base pinning

**Identity.** The control part of `B̃'` is `−e_f/4 + (e_g + e_h)/8 = −E/4`. Since F is affine in e, (8) is exact, and the CH vanishing of both B̃ and `F_β` checks out.

**λ = 1/4 is not forced by CH geometry.** For every λ, the family

  `B_λ = log(κ/√(1+ζ)) + λ(v − κ⁻¹)`

vanishes on CH and satisfies `B_λ' = F_λ − λE`. Linearizing at the ACH equilibrium (ζ = 0, q = 0, y = (2,1,1) + (a,b,c), κ = 1 + k) gives

  `F_λ ≈ (1 − 4λ)a − (b + c) + 8λk`.

So λ = 1/4 is the value that removes the fibre velocity a from the linear drift. In general one gets the rigorous family

  `P̂ ≥ C_λ² / (6λ² ∫dt/W)`,

which can be optimized in λ on the saturation band.

**Tensor coefficient and constant.** In the orthogonal basis h = (3,−1,−1,−1), e = (0,2,−1,−1), d = (0,0,1,−1):

- `|Ric°|² = (3/4)H² + (2/3)E² + (1/2)D²`, which is correct;
- `P̂ ≥ (1/6)∫WE²`;
- `(1/4)|∫E| ≤ (1/4)√(6P̂ ∫dt/W)`, which gives (9) and (11).

**CH tail integral.** With s = sinh t, partial fractions give `1/(s³(1+s²)) = s⁻³ − s⁻¹ + s/(1+s²)`. This confirms (10), with `I(0.70) = 0.365314`.

**Threshold values.**

- **At the exact X3 junction.** The junction is at sinh⁴τ = 1/3, τ = 0.70103. There `I = √3/2 − ½ln(1+√3) = 0.36350` and `C_* = 0.36921`. The note's 0.3702 is the value at τ = 0.70.
- **Improved threshold: 0.3308.** X3 and pinning act on disjoint intervals, so their bounds add rather than serving as alternatives:
  `P̂ ≥ max(0, 4 − 9sinh⁴τ) + 8C²/(3I(τ))`.
  The required mismatch is therefore `C² ≥ (3I/8)·min(1, max(0, 9sinh⁴τ − 3))`. This is maximal at **sinh²τ_J = 2/3 (τ_J = 0.7455)**, where
  **C_*² = 9/32 − (3/16)ln(5/2) = 0.10945, C_* = 0.3308.**

**Unproved step in (11).** The rigorous denominator is `∫_J dt/W` over the actual correction interval J. Replacing it by I(T) requires W ≥ W_CH on J under the identification of the opening orbit, and that comparison has not been proved.

In the exact-CH-terminal frame of Lemma S, B̃ = 0 at t_ch. Any mismatch is therefore removed before opening, where W is smaller, and (11) does not bound it. The late-opening e^{4T} law is rigorous only for mismatch carried on CH-sized orbits.

**ACH Taylor coefficient.** `F_b1` checks against the JSON. Its sign is indefinite, as the note says.

## 4. The anisotropic scan

**The gap law is universal in η.** For every η run, `cost − (2 − b₊⁰)` lies in [−0.0086, +0.005], except η = +1 (+0.071, with t_ch at the 0.701 edge). The small values below the gap are consistent with two facts:

- the rigorous bound uses sup b₊, not 2;
- collocation underestimates the true cost (0.5454 by collocation versus 0.5745 from the actual metric).

So raw η does not break the value law. It moves the entry charge.

**Mechanism.** Raw Δη = O(1) means:

- the base velocities shift by `Δa_{f,g}' ≈ Δη/(3z)`, which is unbounded in units of R;
- the circle opens with `Δa_h' ≈ −2z²Δη/3`, so δ > 0.

By (★), b₊ rises when the entry phase A is placed where the neck's base expansion cancels the imposed contraction, so that `u_f u_g < 4`. The data show exactly this: the optimal A grows monotonically with |Δη|:

| Δη | 0 | −1 | −2 | −4 | −6 | −8 |
|---|---|---|---|---|---|---|
| optimal A | 0.80 | 0.94 | 1.34 | 2.43 | 3.59 | 4.77 |

(★) is directly testable at the stored entry nodes.

**Constrained runs.** Two runs sit at the edges of the box:

- ε = 1/32, Δη = −8: cost 2.9425, A = 5.00000005, t_ch = 0.7010;
- Δη = −12: A = 5, t_ch at its lower limit.

These are box-constrained values, not unconstrained minima. At ε = 1/32 the required compensation scales like 1/z, which pushes A past 5. So the evidence that "cheapness disappears at smaller ε" comes from the box limits and does not reflect intrinsic behaviour.

**Why no raw run can undercut the threshold for an O(−1)-bolt cell.** The bound `P̂[bolt, entry] ≥ b₊(entry) − 1` is exact. For the cheapest run this gives:

- total ≥ 0.4519 + 0.5454 = 0.9973 with the collocation cost;
- total ≥ 1.026 with the actual-metric cost.

Both exceed the certified 0.99585. More generally, if V_sat ≈ 2 − b₊(entry), then every bolt-core route through saturation costs ≈ ≥ 1. Equality is Burns-type.

**Other runs.**

- Large x (X ≈ 4) and the regular C = 4 run sit far from the asymptotic regime, and t_ch is at its limit. Their costs exceed the gap by 0.59–10.3.
- The η = +0.25 run has success = false.

## 5. Status for the diagonal programme

**Rigorous:**

- the closed forms of b±;
- Lemma Q″, with the u/w hypothesis;
- the bounded-geometry adiabatic charge b₊ ≤ −2 + o(1), which gives a decollapse price ≥ 4 − o(1);
- the B_λ identities and the bounds (9)/(10) with the actual ∫dt/W;
- the additive junction threshold 0.3308.

**Algebraic only:** the X, C formulas (5)–(6), which describe curvature-unbounded jets (and C on collars).

**Unresolved:**

- the W-comparison needed to use I(T) in (11);
- a mismatch lower bound ≥ 0.3308 on CH-sized orbits for τ ≥ 0.7455;
- trajectories whose sup b₊ stays below 2 and that correct their mismatch before reaching CH size. This is where the Step-29 subsolution G is still the missing object.