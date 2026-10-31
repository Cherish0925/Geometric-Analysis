# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step11_subthreshold_perpendicular_cell.md",
    "Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md",
    "Sessions/S1003A02/workspace/scripts/o11_collar_independent_verify.py",
    "Sessions/S1003A02/workspace/scripts/o11_collar_arb_certificate.py",
    "Sessions/S1003A02/workspace/data/o11_collar_independent_x001_X8.json",
    "Sessions/S1003A02/workspace/data/o11_collar_arb_x001_X8.json",
    "Sessions/S1003A01/workspace/data/perp_collar/x0.01_X8_J_d8.json",
    "Skills/geometric-analysis/research/paper/sections/variational_geometry.tex"
  ]
}
```

## Task

Read the fixed perpendicular complex-hyperbolic cell record and both independent verification notes/scripts. Check the mathematical chain needed for a strict same-metric cell J_6<8π²: normalization, Cartan/relative identities, bolt smoothness, positivity, CH attachment and smoothing, numerical integral, residual-finite cover supply, and inherited global transfer. Identify any substantive error that would invalidate the candidate, and distinguish what is proved from what remains numerical. In particular inspect the 160-bit Arb script: say exactly what it encloses and whether its Richardson-inflated result is or is not a rigorous quadrature certificate. Give a direct scientific memo aimed at completing O11, not generic review.

## Output

# Verification memo: the fixed perpendicular CH cell (x₀ = 0.01, X = 8, degree 8) and the O11 transfer

## 0. Result

I found no error that invalidates the candidate. With one exception, every link in the chain is either proved analytically or can be closed by a short argument given below:

- normalization,
- bolt smoothness and topology,
- positivity,
- C² attachment to CH,
- passage to smooth metrics,
- large-ball supply,
- transfer coefficient.

The exception is the value of the frozen integral. It is supported by four mutually consistent quadratures. None of them is yet a proof.

The 160-bit Arb script rigorously encloses the Simpson sums only. It does not enclose the integral. Its Richardson×1000 radius is a heuristic, not a quadrature certificate.

Two further points matter for completing O11:

- **No explicit smoothing estimate is needed.** Continuity of the curvature energy under C² approximation removes that item.
- **The coefficient can also be obtained from P alone.** The paper's own inequality α_j ≤ 4P/(8π²A_j+P) does this. It needs only P_cell < 8π² (margin 8.91×10⁻⁴, coefficient 3.9992077) rather than J₆ < 8π².

## 1. Normalization: checked by hand

**CH profile.** The collar values are
- G = X + X²,
- F = X,
- w = log(1+X).

These give dx²/(4x(1+x)) + xσ₁² + xσ₂² + x(1+x)σ₃². With x = sinh²r this becomes dr² + sinh²r(σ₁²+σ₂²) + sinh²r cosh²r σ₃². That is CH² with holomorphic curvature −4 and Ric = −6g, in the unit-sphere convention dσ_i = 2σ_j∧σ_k. In this convention ∫_{S³}σ₁₂₃ = 2π².

**Spin formula vanishes on CH.** In the script's bolt-adapted axes, a = (sinh r, sinh r cosh r, sinh r). This gives:
- u₀ = cosh r − cosh r = 0,
- u₂ = 0,
- u₁ = 3 sinh²r, H₁ = u₁, λ₁ = tanh r.

Then u̇₁ − 2H₁/λ₁ = 6 sinh r cosh r − 6 sinh r cosh r = 0, so P_pos = 0 pointwise. Also Σ = u̇₁/a₁ + 2H₁/(a₂a₀) = 6 + 6 = 12, so the scalar term (Σ−12)² vanishes. This matches s = −2Σ = −24.

The S₂ form and the cubic term also vanish identically on CH. So the integrands are correctly normalized to the Einstein constant −6.

**Scale invariance.** ∫|Ric_{6g}+6g|²_{6g} dV_{6g} = ∫|Ric+6g|² dV. This holds because Ric is scale-invariant, |·|² scales by 1/36 and dV by 36.

The decomposition |Ric+6g|² = |Ric°|² + (s+24)²/4 is correct.

**Why J₆ is the right cell cost.** Write E(g) = inf_λ ∫|Ric−λg|²/(λ²V). Taking λ = −1 at Ric = −g scale gives E ≤ ∫|Ric+g|²/V. So J₁ := J₆(cell) is exactly the per-cell contribution to E (see §5).

## 2. Bolt: smoothness, topology, positivity (all proved)

**Exact factorization at the bolt.** Put y = x − x₀. Then:
- u = log(1+y/x₀)/ℓ is analytic, with ℓ = log 800.
- The smoothstep S(u) = 10u³ − 15u⁴ + 6u⁵ is O(y³).

Hence F = y e^{q_F(0)} + O(y²) and G = y e^{q_G(0)} + O(y²). The shift added to c_G[0] makes q_F(0) + q_G(0) = 0 exactly, since (1−u)³ = 1 at u = 0. Therefore F′G′ = 1 holds by construction, not merely to rounding. The JSON value FpGp = 1.0 is a floating confirmation of this identity.

To make the certificate unambiguous, the metric should be *defined* by the formula with the shift and by fixed exact coefficients. One can use either the decimal strings (as in the Arb script) or the binary doubles (as in JAX); the energy difference is about 10⁻¹⁶.

**Smoothness conditions.** Let ρ be the normal distance, ρ = ∫dy/(2√G). Then ρ = √y·(analytic), so y = ρ²c(ρ²) with c analytic. Consequently:

| Slot | Behaviour near bolt | Requirement |
|---|---|---|
| F (collapsing σ₁ slot) | ρ²(1 + ρ²·analytic(ρ²)) | no-cone, weight 1 |
| ½(h₂+h₃) | x₀ + O(ρ²) | analytic in ρ² |
| h₂ − h₃ = x(1−e^w) | O(y²) = ρ⁴·analytic(ρ²) | anisotropy has charge 4 |

The charge-4 statement follows because Ad of the collapsing circle rotates σ₂ + iσ₃ at rate 2. So w = u²(…) + log(1+x)S(u) = O(y²) is exactly the needed condition, and the metric is real-analytic across the bolt.

**Topology.** With dσ₃ = 2σ₁∧σ₂, the Bergman form is ω = d(½ sinh²r σ₃). Then ω² = 2 sinh³r cosh r dr∧σ₁₂₃. So the complex orientation is dr∧σ₁₂₃, and collapsing the e₃-circle is the complex blow-up (Euler number −1).

Right multiplication by a unit quaternion u with Ad_{u⁻¹}e₃ = e₁ maps e₃-orbits to e₁-orbits. It preserves dr∧σ₁₂₃. Hence the σ₁-collapse disc bundle is orientation-preservingly the same O(−1) bundle, and the cell is (CH ball) # CP̄².

**Positivity.** On u ∈ [0,1], S′ = 30u²(1−u)² ≥ 0 and 0 ≤ S ≤ 1. Therefore
- F = y e^{q_F} + x₀S > 0 for y > 0,
- G = (y + (x²+x₀)S) e^{q_G} > 0 for y > 0.

The sampled minima are conditioning data only. The A01 value min G/y = 1.0321422 sits slightly above g₁ = 1.0321405. That reflects the sampling grid, not the geometry.

## 3. CH attachment and smooth metrics

**C² attachment.** We have 1 − S(u) = (1−u)³(6u²+3u+1); I verified this by expansion. Combined with the (1−u)³ factors in q_F, q_G and w_r, it gives F − x, G − (x+x²), w − log(1+x) = O((1−u)³). So the glued metric is C², with continuous curvature. On [x₀, X] the cell has J₆ equal to the computed integral, and the CH exterior contributes zero.

**Smoothing needs no cutoff estimate.** J₆ depends continuously on the metric in C² on a compact set. Mollifying the global C² metric on M_j gives smooth metrics with J → J(C² metric). Since α is an infimum and the inequality is strict, this suffices.

The O(δ³) cutoff lemma is also correct. With deviation D = O(s³), (χD)″ = O(δ); the defect is O(δ) on volume O(δ), giving a change of O(δ³). If an explicit smooth cell is wanted, blend the profile functions convexly with the CH values, F_new = χF + (1−χ)x and similarly for G. Positivity is then automatic.

## 4. Identities versus numerics

**What is proved.**
- Exact jets at the bolt and the collar.
- Positivity.
- The scaling identity.
- Vanishing of the spin integrands on CH.

**What rests only on agreement of computations.**

(i) *The formulas themselves.* These are the Cartan identity P/(8π²) = ∫Σλ_i/4(u̇_i − 2H_i/λ_i)² dt, the identity s = −2Σ, and the relative calibration P/(8π²) − 1 = ∫(S₁+S₂+S₃+C₃).

The A02 "independent" script reuses the same spin formula. The only formula-level cross-check is A01's coordinate-curvature code. It agrees to about 10⁻¹⁰ at 600 nodes and drifts by 1.4×10⁻⁷ at 2400 nodes, from conditioning near the bolt.

P_pos and the relative form agree to 4×10⁻¹⁵ on this profile. This confirms that the relative identity's endpoint terms are bolt = 1 and CH collar = 0 here, but it is not a proof of the identity.

(ii) *The integral value.* Four quadratures agree:

| Method | J₆/(8π²) |
|---|---|
| A02 JAX split Gauss, 200/400/800 | 0.9991162431353243 |
| A02 Arb Simpson + Richardson | 0.999116243135327 |
| A01 split spin quadrature | 0.99911624313525 |
| A01 coordinate code, 600 nodes | 0.9991162433 |

The Arb Richardson value is S₂₀₀₀ + (S₂₀₀₀ − S₁₀₀₀)/15 = −8.83756864673×10⁻⁴; it matches Gauss to 3×10⁻¹⁵. The Simpson differences are −2.405×10⁻¹⁰ and −1.517×10⁻¹¹, ratio 15.86 ≈ 16. So the h⁴ regime is reached.

The optimizer's stored J = 0.99911624282 differs by 3×10⁻¹⁰ (nq = 600 inside the optimizer); this is immaterial. The mechanism split (S₁, S₂, S₃, C₃) and the five-range sum (−88.37×10⁻⁵) are internally consistent.

**Parity check.** All component integrands are analytic at the bolt in the u-measure. In ρ:
- a₀, a₁ are even and a₂ is odd;
- u₀, u₁ are odd and u₂ is even;
- every λ_i is odd.

So S₁, S₂, S₃, C₃, the scalar term and P_pos are all odd in ρ per dt. Multiplied by dt/dx = 1/(2√G), they become analytic functions of y. Gauss convergence is therefore legitimate, and no √u endpoint singularity hides in the data.

## 5. What `o11_collar_arb_certificate.py` actually encloses

**Rigorously enclosed.** For the metric with exact decimal coefficients, the script encloses the three composite-Simpson sums of the relative-plus-scalar density f = (s₁+s₂+s₃+cub+scal)·dt/dx·ℓx on [10⁻¹², 1] in u, for n = 500, 1000, 2000.

The J2 jet algebra is correct for what is used:
- U.d = d(2√G a′ − …)/dx needs only a″ and G′;
- the deliberately wrong .dd slot of J2(a.d, a.dd, 0) is never read.

The point balls (radius about 10⁻²⁹) survive the 0/0 cancellation at y ≈ 7×10⁻¹⁴ because 160 bits suffice at isolated points.

**Not enclosed.**

(a) *The Simpson remainder.* The radius 1000·|S₂₀₀₀ − S₁₀₀₀|/15 is an observed-convergence estimate. No bound on f⁽⁴⁾ enters. The docstring's phrase "rigorous global fourth-derivative remainder" describes code that does not exist.

(b) *The interval [0, 10⁻¹²].* The comment says it is "enclosed separately in the returned tail", but no tail term is added anywhere in `simpson` or `main`.

(c) *The formulas.* The script integrates the relative form, so its output assumes the calibration identity P/(8π²) = 1 + ∫(S + C₃).

The JSON fields `J_enclosure` and `below_one: true` therefore label a heuristic, not an enclosure. The printed radius 4.15×10⁻⁹, rather than 1.01×10⁻⁹, is Arb's decimal display absorbing the truncated midpoint. J_upper = 0.9991162441474 is center + 1.011×10⁻⁹.

## 6. Global transfer: direct derivation and two strengthenings

### 6.1 J-route, without I54 or SW

Take λ = −1 at Ric = −g scale on M_j. Place k_j cells and ℓ_j shrinking handle insertions in disjoint balls; for the handles use Prop. vg-recovery with k = 0. Then:
- the handle P → 32π² each, and ∫(s+4)² over insertions → 0 (from S → 32π²A, I → −8π²A, V → 2π²A);
- V = 2π²A_j(1 + O(k_j/A_j)).

So

α_j ≤ ∫|Ric+g|²/V ≤ [k_j J₁ + 32π²ℓ_j + o(1)] / [2π²A_j(1+o(1))].

Dividing by h_j = Q_j/A_j, with k/Q → 2/9 and ℓ/Q → 7/36, gives

limsup α_j/h_j ≤ 28/9 + J₁/(9π²) = 3.9992144383.

This reproduces the inherited formula exactly.

### 6.2 P-route, sharper and only P_cell needed

For large j, Prop. vg-conformal-infimum and R ≥ 8π²A + P give, for every metric g,

α_j = inf J ≤ 4P(g)/(8π²A_j + P(g)).

Hence

limsup α_j/h_j ≤ 4(7/9 + (2/9)·P_cell/8π²) = 3.9992077.

This needs P_cell < 8π², with margin 8.913×10⁻⁴. It is the same-metric P of the frozen cell, so the scalar square of 7.54×10⁻⁶ drops out. The price is reliance on the SW scalar estimate and the Yamabe comparison, both proved in the paper for these M_j.

### 6.3 Ball supply

The cell fills the CH ball of radius r = arsinh√8 = 1.7627 at Ric = −6g scale, which is 4.318 at Ric = −g scale. No buffer is needed after C²-mollification.

The supply argument is correct as written:
- Γ is discrete, so only finitely many γ have d(p, γp) ≤ 2r.
- A finite-index Γ_* avoiding them gives an embedded ball in X_*, because CH² is a Hadamard manifold.
- Every cover of X_* then has deg-many disjoint lifts, far more than k_j ∼ (2/9)h_jA_j = o(A_j).

**Uniformity over cover sequences.** This yields a balanced family, not every balanced family. Some cover sequences, for example abelian ones, may keep injectivity radius bounded at every point. The fix is clean: Theorem vg-balanced-family allows any fixed base. Taking the base to be X_* (inj > 4.32), every balanced sequence of its covers satisfies the bound, since inj of a cover ≥ inj of its base pointwise. The SW lower bound c_*h_j still holds on these M_j, so

0 < c_* ≤ liminf α_j/h_j ≤ limsup α_j/h_j ≤ 3.99921.

A statement for every base would require a subthreshold cell inside a ball smaller than inj(X₀). The Step-10 shrinking family (deficit 9x₀² log(1/x₀)) is the natural candidate, but that expansion is asymptotic and uncertified.

## 7. A certificate route that avoids the bolt dependency problem

The obstruction found by both sessions is real. Interval boxes near y = 0 make the 1/y-size terms cancel only up to box width/y, which forces about 1/y_min boxes. Two workable routes follow.

### Route A: Gauss quadrature with Bernstein-ellipse bounds; no new symbolic work

1. **Analyticity at the bolt.** f is analytic in u on a complex neighborhood of [0,1], including u = 0. The metric is real-analytic across the bolt (§2), so the invariant density is analytic in ρ², hence in y. The raw formula agrees with it for y > 0, so it is its continuation.
2. **Branch choice.** Write √G := √F·√(G/F). Then G/F = Ĝ/F̂ ≈ 1.065 near the bolt, with no branch issue. The formula is formally invariant under √F → −√F, because (a₂, √G) → (−a₂, −√G) is the ρ → −ρ parity of §4. So the principal branch of √F is harmless.
3. **Error bound.** On each existing split interval, n-point Gauss satisfies |I − I_n| ≤ (half-length)·(64/15)·M·ρ^{−2n}/(ρ²−1), where M = sup|f| on the Bernstein ellipse E_ρ.
   - The nodes are already computed; recompute them in Arb.
   - Bound M by evaluating the J2 density in `acb` on coarse boxes covering ∂E_ρ, with analytic flags on sqrt/log. Boxes touching a zero of F, G or x e^w, or a branch cut, return non-finite values.
   - The ellipse boundary stays at |y| ≳ x₀ℓ·(semi-minor axis) away from the bolt, so dependency inflation there is mild.
   - With n = 200 and ρ = 1.2, ρ^{−400} ≈ 10⁻³². So even M ∼ 10²⁰ leaves an error far below the 8.8×10⁻⁴ margin.
4. **Integrand to certify.** Integrate P_pos + scalar, not the relative form, so the calibration identity is not needed.

python-flint's `acb.integral` (Petras algorithm) can handle [u_b, 1] automatically. On [0, u_b] a fixed Gauss rule is needed, because adaptive bisection toward u = 0 never terminates with raw boxes.

### Route B: factored rational density (as A02 §3 proposes)

Compute Ric of dx²/(4G) + Σh_iσ_i² in Wolfram. Its components are rational in h_i, h_i′, h_i″, G, G′ with no radicals, and the volume factor is x e^{w/2}√(F̂/Ĝ)/2.

Then substitute F = yF̂, G = yĜ, w = y²ŵ. The 1/y terms cancel identically, without using the no-cone relation; for example, G′h₁′/h₁ − Gh₁′²/h₁² has a vanishing 1/y part. Evaluate F̂, Ĝ, ŵ through log1p(z)/z series with explicit tails. Plain interval Simpson with an f⁽⁴⁾ enclosure then works everywhere, since h = 1/2000 tolerates sup|f⁽⁴⁾| up to about 10¹².

### Formula correctness, either route

A Wolfram Cartan computation should confirm, as algebraic identities in (a, ȧ, ä):
- |Ric°|²·a₁a₂a₃/4 = Σλ_i/4(u̇_i − 2H_i/λ_i)², with the appropriate measure factor;
- s = −2Σ.

Route B makes this automatic, because its integrand is computed from the metric directly.

## 8. Status

**Proved.** Every geometric and topological link is closed:
- Ric = −6g normalization and scale invariance;
- analytic bolt smoothness with exact F′G′ = 1 and weight-4 anisotropy;
- the identification of the cell as CH-ball # CP̄²;
- analytic positivity;
- the C² CH attachment and passage to smooth metrics;
- residual-finite ball supply, including all balanced families over a base X_* with inj > 4.32;
- the transfer coefficient 28/9 + J₁/(9π²), and the sharper P-route 28/9 + (8/9)P_cell/(8π²).

**Numerical only.**
- J₆/(8π²) = 0.99911624313532 and P/(8π²) = 0.99910870273359.
- The Cartan/relative formulas as implemented.

The Arb output encloses Simpson sums, not the integral, and its 1000× Richardson radius is not a remainder bound.

Once P_pos + scalar (or P_pos alone) is enclosed by Route A or B with its formula confirmed symbolically, the result follows: balanced surgery families exist on which limsup α_j/h_j ≤ 3.99921 < 4. The exact first-order coefficient then becomes the infimal blow-up-cell cost, which remains to be determined, together with the matching lower analysis.