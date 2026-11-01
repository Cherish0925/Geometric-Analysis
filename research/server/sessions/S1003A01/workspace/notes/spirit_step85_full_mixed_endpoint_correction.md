# Spirit review after Step 85 — the full mixed inequality excludes the nominal Ricci-bound endpoint

This corrects the endpoint interpretation in §7 of `step85_coupled_center_theorem_neck_trace_and_endpoint_reduction.md` and §6 of `trace/ttcs/results/step85_ttcs01_sub1_generator.md`. It is a consequence of the already inherited one-field mixed inequality, not a new two-field obstruction or a solution of the small-blowup existence problem.

## Assumptions and conventions

Let M = X # k CPbar², A = c₁²(X) > 0, 0 < k < A/3. Suppose g is Einstein and the stated actual-field supply gives

∫(s − √6 |W⁺|)² ≥ 72π² A.

Use the Weyl operator norm, S = ∫s², W = ∫|W⁺|², and D_W = S/24 − W. The general-type scalar supply forces s < 0. Set x = S/(96π²). Since P = 0 and T₊(M) = A − k, Chern–Weil gives

W = 2π²(A − k − x),
D_W = 6π² x − 2π²(A − k).

Cauchy–Schwarz bounds the mixed integral above by (√S + √(6W))². Hence a necessary condition is

[√(8x) + √(A − k − x)]² ≥ 6A.                  (1)

This is the smooth C₊ = 0 instance of the inherited mixed-curvature screen.

## The erroneous endpoint inference

D_W = 4π²k would force

S = 32π²(A + k),
W = (4π²/3)(A − 2k).

The full mixed inequality would then require

2√(A + k) + √(A − 2k) ≥ 3√A.

Strict concavity of the square root gives the opposite strict inequality for every k > 0 in this range, since

[2(A + k) + (A − 2k)]/3 = A.

Thus the nominal endpoint D_W = 4π²k is already excluded by the full one-field mixed estimate. The positive quantity 4π²(A/3 − k) in the generator memo is slack in the weaker combination S/24 + 2W ≥ (8π²/3)A. Slack in that weaker combination does not show compatibility with the original mixed estimate.

## Correct quantitative lower edge

Solving (1) for its smallest admissible x gives the inherited value

x ≥ x_min = (A/27)[4 − √(1 − 3k/A)]².

Consequently

D_W ≥ 4π²k + (8π²A/9)[1 − √(1 − 3k/A)]².

The correction is strictly positive; for k/A → 0 it is

2π² k²/A + 3π² k³/A² + O(k⁴/A³).

The algebra was checked exactly with SymPy in shell log `Sessions/S1003A01/trace/shell/36437ee05b7243f28e5d62d183004a50/stdout.log`. The logical inequality follows from the displayed Cauchy–Schwarz and concavity arguments, not from the symbolic check.

## Scope

This sharpens the necessary deficit/volume budget for an exact Einstein candidate. It is not a positive all-metric P bound and does not exclude all Einstein candidates for 0 < k < A/3. It does not contradict the valid non-Einstein strict-saving constructions.

The relative-connection identities and the finding that the examined two-monopole bilinears supply no new estimate remain useful. The correct limited verdict is: those tested identities reduce to old balances or retain uncontrolled mixed terms. They do not prove that every multi-field or exact-Einstein argument fails. No claimed candidate should be called consistent with all known bounds until it passes the full mixed inequality (1), rather than only its weaker consequence.
