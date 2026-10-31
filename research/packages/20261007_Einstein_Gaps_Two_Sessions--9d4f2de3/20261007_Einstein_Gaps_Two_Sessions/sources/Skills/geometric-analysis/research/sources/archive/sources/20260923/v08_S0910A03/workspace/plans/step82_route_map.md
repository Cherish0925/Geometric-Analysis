# Step 82 route map: derive and test the radial production of the reversal energy

> **Superseded by Step 83.** The sign analysis was corrected and the Bakry-Émery
> analysis showed no monotone functional excludes the K-drop. See
> `workspace/plans/step83_route_map.md` for the updated assessment.

## Current negative-side position

The graph-manifold route has:

1. topological exclusion of every Einstein metric on the intended extended graph class;
2. an explicit small-defect expanding tail that removes orbit anisotropy;
3. a rigorous collapse theorem for the fixed Bianchi VII\(_0\) core;
4. exact physical slice balances for the full OT class.

The missing module is dynamic reachability from a reflected scalar-minus-six center to an expanding, tail-compatible slice.

## New invariant target

For
\[
 K(r)=\langle |U_s|_{\mathbb H^2}^2-h^2\rangle_{\rho ds},
\]
where \(h=(\log\rho)_s\), the exact horizontal-mean equation is
\[
 x'=3-\frac12K-\langle E_{zz}\rangle-x(x+y),
 \qquad x=I/V,\quad y=J/V.
\]
At the reflected center, \(K=12\), \(x'= -3\). At any first return \(x=0,x'\ge0\), small defect forces
\[
 K\le6+2\delta.
\]
Thus the connector must lower `K` by about six after a universal initial rise.

## Exact balances already established

\[
 J'=6V-\int E_{\rm orb}d\mu,
\]
\[
 I'=3V+\int R(q_r)d\mu-\int E_{zz}d\mu,
\]
\[
 I'=\int[-3+2uv+v^2/2-|B_0|^2+E_{\rm orb}-E_{rr}]d\mu.
\]
At a first return,
\[
 2\operatorname{Cov}(u,v)+\frac12\langle v^2\rangle
 -\langle|B_0|^2\rangle\ge3-3\delta.
\]
The exact defect combination is `E_orbit-E_rr`. This corrects the intermediate `2E_rr-E_zz` formula; the coarse `3δ` threshold is unchanged.

## Universal germ behavior

Independent tensor verification gives
\[
 K'(0)=0,
\qquad
 K''(0)=72+2\langle|\tau|^2\rangle+\frac38\operatorname{Var}(k)\ge72.
\]
Therefore early center engineering cannot move `K` toward six. Reversal must be an intermediate-radius nonlinear event.

## Highest-value next work

The full radial production law is now verified in physical arclength and a fixed target normalization:
\[
 K'=-2\langle\tau,b\rangle+2\langle vc\rangle
 +\operatorname{Cov}(v-u,k)-2xK.
\]
This is kinematic; no explicit orbit-defect term is added while `tau` is retained. If the orbit equation is used to eliminate `tau`, its defect enters once with the corresponding opposite sign. The Codazzi relation is
\[
 D_sv=h(u-v/2)-\tfrac12\langle U_s,b\rangle-E_{rs}.
\]

Required work:

1. Seek a coercive estimate on the pre-return interval `x≤0`; note that `-2xK≥0` opposes a `K` drop.
2. Determine whether Codazzi plus a physical weighted Poincaré estimate controls the covariance terms without assuming noncollapse unavailable in the connector.
3. If no sign estimate exists, formulate an exact-germ spectral march that records every production term and all five Einstein components. The meaningful event is `K'<0` followed by `x=0` with `K≤6+O(δ)` before loss of regularity—not merely a favorable algebraic slice.
4. Preserve the factor convention `|b|²=2|B0|²` and do not double-count the orbit defect.

## What does not settle the route

- zero matrix Noether current;
- growth of a convex-distance functional;
- impossibility of a constant exact exit;
- a pointwise/moment profile satisfying the turning inequality;
- another extension of the already solved expanding tail.

A local exact reversal germ exists away from reflection, so no universal local Einstein sign law excludes reversal. The issue is reachability from the prescribed reflected center.

## Parallel full-goal context

The positive branch remains independent. A02 has a checked positive near-pinched input construction, but arbitrary Einstein exclusion requires positive, zero, and negative Einstein-constant legs. A01 has retracted the unconditional mixed-chirality positivity theorem: the Einstein operator has a negative TT mode and singular self-pairings defeat the positivity argument. What remains is a corrected flat principal odd identity and a matched regularized relative-response target. Neither result resolves the negative interval or all-dimensional quantifiers.

## Files

- `workspace/notes/step82_slice_balances_and_reversal_energy.md`
- `workspace/scripts/step82_slice_balance_verify.py`
- `workspace/data/step82_slice_balance.json`
- `workspace/scripts/step82_geometric_balance_check.py`
- `workspace/data/step82_geometric_balance.json`
- `workspace/scripts/step82_turning_covariance_model.py`
- `workspace/data/step82_turning_covariance_model.json`
- `workspace/scripts/step82_center_jet_invariants.py`
- `workspace/data/step82_center_jet_invariants.json`
- `trace/ttcs/results/step82_ttcs01_verifier1_integration.md`
- `trace/ttcs/results/step82_ttcs01_generator1_integration.md`
- `trace/ttcs/results/step82_ttcs02_verifier1_integration.md`
