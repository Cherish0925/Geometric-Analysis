# Step 85 route map: Bochner comparison and the forced stability frontier

> **Step 86 supersession.** The exact Bochner theorem remains valid, but the forced ordinary-Moser program below omitted a superlevel interface term and used the wrong functional-inequality premise. The corrected finite-dimensional curvature, Caccioppoli estimate, concentration mechanism, and new weighted-resolvent direction are in `workspace/plans/step86_route_map.md` and `workspace/notes/step86_forced_bochner_superlevel_and_localization.md`. Do not use the claimed universal \(C'\) or graph-route closure below as established.

## Current position

The Bochner comparison theorem eliminates exact reflected OT Einstein connectors (sup e ≤ 6 contradicts ⟨e⟩ ≥ 12). A02's warped waist barrier eliminates warped-product turnarounds (δ ≥ 3/2 for k ≥ 0). Combined, the only remaining avenue for the negative graph-manifold branch is **non-warped forced (approximate) connectors**.

## What is established

### This step
- **Exact Bochner comparison:** ½Le ≥ ½e(e−6) for the orbit-map energy density e on a 2D Einstein base. TTCS-verified.
- **Center identity (corrected):** ⟨e(0,·)⟩_μ = 12 + ⟨h²⟩ ≥ 12, where h = (log ρ)_s is the tangential orbit-area derivative (not H = u+v).
- **Exact connector impossibility:** sup_{exit} e ≥ 12 for any exact reflected OT connector. No exact connector reaches the Step 73 expanding tail (e → 0).
- **Tension identity:** ⟨dU, Dτ_σ⟩ = div_σ(V) − |τ_σ|², converting forced Bochner to integrated form without differentiating E.
- **Step 83 corrections:** Ric−Hess (not +Hess), cusp benchmark (not cosh), no closed H² geodesic.

### Peer results absorbed
- **A02 #614:** Warped waist barrier δ ≥ 3/2 for k ≥ 0, pointwise, non-amortizable.
- **A02 #615:** Exact Sambusetti theorem via Kotschick Corollary 3. BCG+CGB threshold δ ~ 3/(4χ(N)).
- **A02 #616:** Additive deficit means no uniform δ₀ from BCG alone for N#N.
- **A01 #617:** Independent warped waist check. AB-sector adjacent sign K_adj^AB < 0.

## The decisive remaining question

**Can the integrated Bochner + De Giorgi–Moser iteration on the 2D weighted base (Ric_σ ≥ −3) give a universal bound sup e ≤ 6 + C'δ?**

If YES (with C' independent of connector length and geometry):
- 12 − 8δ ≤ ⟨e⟩ ≤ sup e ≤ 6 + C'δ forces δ ≥ 6/(8+C') > 0.
- The graph-manifold T³ route has a universal defect threshold.
- Combined with warped waist (3/2 for warped constructions), the entire negative graph route fails for δ < min{3/2, 6/(8+C')}.

If NO (the constant depends on geometry):
- Some graph geometries might allow δ → 0 through non-warped forced connectors.
- The K-production analysis becomes relevant again for forced non-warped evolution.

## Technical path for the forced estimate

The div_σ(V) divergence term is the obstacle to a pointwise maximum principle. The integrated approach:

1. **Caccioppoli inequality.** Test the forced Bochner with η²(e−k)+ for k ≥ 6:
   ∫ρη²|∇u_k|² ≤ C[∫ρ u_k²|∇η|² + δ²∫ρη² + δ∫ρη²(k+u_k)u_k]
   The div_σ(V) integrates away; the cross term |V(∇η)| ≤ √e·Cδ|∇η| is absorbed by Young.

2. **Weighted Sobolev.** On (B², γ_B, ρ dA) with Ric_σ ≥ −3 and dim = 2:
   ||ηu_k||_{L^q} ≤ C_S(3,2,R)[||∇(ηu_k)||_{L²} + ||ηu_k||_{L²}] for any q < ∞.

3. **Moser iteration.** Standard L²→L^{2(1+ε)}→...→L^∞ gives:
   ||u_k||_{L∞(B_r)} ≤ C_M(3,2,R,r) · ||u_k||_{L²(B_R)}

4. **Energy bound.** The L² norm of u_6 is controlled by the forcing terms, giving ||u_6||_{L²} ≤ C₃δ · √(Area).

5. **Conclusion.** sup e ≤ 6 + C'δ with C' = C_M · C₃ · (universal geometric constants).

The constant C_M depends on the Sobolev constant C_S, which depends on Ric_σ ≥ −3 and ball radius R ≤ 1. These are UNIVERSAL (dimension 2, curvature −3). So C' is universal.

## Parallel routes

### Negative branch — N#N
- BCG gives necessary scale δ ≳ 1/χ(N), but this is additive (not uniform).
- Warped S³ waist costs δ ≥ 3/2, blocking symmetric necks.
- Non-warped S³ neck is open; the Bochner analysis needs extension to collapsing T² orbits.
- If graph route is killed by universal threshold, N#N with varying χ remains the only negative candidate.

### Positive branch (A01)
- K-symmetry reduces to off-diagonal odd-odd Green kernel.
- AB adjacent sign K_adj^AB < 0 (Step 92).
- Full Ozuch coefficient requires all sectors + nonlinear chart.
- Independent from negative-branch work.

### Higher dimensions
- A02 reduction: Yau-26 false in dim n ≥ 3 requires no-Einstein manifold in dim n.
- For n ≥ 5: no certified no-Einstein manifold, but this is absence of knowledge, not impossibility.
- All 4D work feeds into the universal problem.

## Priority allocation

1. **Highest:** Complete the forced Moser estimate (Steps 1-5 above). This would establish a universal graph-connector threshold and resolve the T³-fiber negative branch.
2. **High:** Investigate whether the Bochner comparison extends to the S³-neck geometry (N#N route). The collapsing T² orbits at axis points require careful treatment.
3. **Medium:** Monitor A01's positive-branch progress; absorb and verify any complete sector theorem.
4. **Low:** Higher-dimensional no-Einstein search (complementary but not currently accessible).

## Files

- `workspace/notes/step85_bochner_comparison_theorem.md` — main theorem and derivation
- `workspace/scripts/step85_bochner_comparison.py` — algebraic verification
- `workspace/scripts/step85_bochner_numerical.py` — numerical test on expanding tail
- `workspace/data/step85_bochner_comparison.json` — algebraic results
- `workspace/data/step85_bochner_numerical.json` — numerical results
- `trace/ttcs/results/step85_ttcs01_verifier1_integration.md` — TTCS verification
