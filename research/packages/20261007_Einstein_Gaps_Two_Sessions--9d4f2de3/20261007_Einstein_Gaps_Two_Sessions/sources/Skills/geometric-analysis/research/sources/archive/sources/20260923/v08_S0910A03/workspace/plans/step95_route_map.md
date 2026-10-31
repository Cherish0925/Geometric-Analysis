# Step 95 route map: after the Bochner cancellation correction

## Corrected this step

1. **K_X identity** (new, verified): ∫ m_q(X)dμ_σ = -(1/2)∫ q^T K_X q dμ_σ,
   K_X = (divX-2X(σ))A - e^{-3σ}M^{-1}X(M)M^{-1}.
   Connects charge to horizontal defect via a matrix quadratic form.

2. **Bochner cancellation** (TTCS-identified, symbolically verified):
   The drift curvature's +Qe is exactly cancelled by the twist tension
   derivative's -Qe. The net twist Bochner contribution is:
   \[
   3Q\langle\nabla\sigma, d(\beta\circ U)\rangle
   = -3Q\langle\nabla\alpha,\nabla\sigma\rangle
   \quad(\text{diagonal constant charge}).
   \]
   This has NO fixed sign. It is small on a redshifted cusp (Q→0). The
   separator statement |∇σ|=0 holds only for special seeds, not for a general
   minimal invariant separator; no bounded transition region follows.

3. **Withdrawn claims**: the "charged connector obstruction theorem"
   from the initial Step 95 computation. The OT resolvent ceiling cannot
   be used for Q>0 because the tension estimates |τ_σ|≤Q+Cδ are
   Q-dependent.

## What remains valid

- OT obstruction (δ<0.246) for charge-free connectors (Steps 85-88).
- Separator floor ≥ 12-8δ+2⟨|II|²⟩ ≥ 12-8δ (TTCS confirmed).
- CD(-(3+δ),4) holds with twist (TTCS confirmed).
- Charged Koiso germs: local Q>0 with stability (Steps 92, 94).
- Redshift taper: area+Maxwell cannot bound Q_+ (Step 94).
- K_X identity and area-charge coupling (this step).

## The real remaining structure

The corrected forced Bochner with twist is:
\[
\frac12Le \ge \frac12e(e-6) - 3Q\langle\nabla\alpha,\nabla\sigma\rangle
- C\delta^2 - (3+\delta)e + \text{nonneg}.
\]

The net twist term -3Q⟨∇α,∇σ⟩ has no fixed sign. It is small on a redshifted cusp where Q→0. A general minimal invariant separator does **not** imply |∇σ|=0; that vanishing holds only for special seeds such as the Step 94 center.

**Step 96 correction.** Nothing above localizes the twist contribution to a transition of uniformly bounded extent. The area equation is elliptic and does not bound normal travel time, and a resolvent on an exterior subdomain retains entrance data. The proposed one-dimensional curved-base BVP is also excluded: its level `T^3` metrics have constant coefficients and remain intrinsically flat, so the δ≥3/2 barrier applies.

## Continuing object after Step 96

Use the genuinely `s`-dependent charged-Koiso center. Step 96 derived its full Gaussian Einstein evolution and center Taylor coefficients, then formulated the gauge-fixed all-block two-end residual map. The next work is to compute that mixed-order operator's indicial roots, Fredholm index, and smallest left/right singular fields on a compactified cylinder. See `workspace/plans/step96_route_map.md`. A nonlinear two-end solve should not precede this linear matching analysis.
