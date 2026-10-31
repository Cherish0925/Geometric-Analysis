# Step 99 route map — superseded by the Step 100 global-topology correction

> The former finite-defect target near `1.098` is withdrawn. A negative-branch counterexample to Yau 26 still requires a fixed-dimensional sequence with normalized Ricci defect tending to zero on manifolds carrying no Einstein metric. A positive lower bound for a particular topology cannot refute an existential universal interval, and a single finite-defect metric cannot do so.

## Retained local information

1. For a Gaussian half-cylinder joining a minimal center to an exactly expanding attachment at length `R`, the normal block obeys the Raychaudhuri floor `delta_min(R) ~ 12 exp(-2R)`. Hence any vanishing-defect family needs `R -> infinity`.
2. In the tested full-matrix quintic, the tangential block dominates: about `28.7` versus normal `10.7`; spatial Ricci of intermediate slices is the largest term. This evaluates that interpolant only.
3. The conformal expansion is an exterior benchmark, not a charged-center connector.

## Correct global bridge

For a closed graph gluing made from pure finite-volume real-hyperbolic four-pieces, the Euler characteristic is positive and equals the sum of piece Euler characteristics; torus boundaries contribute zero. Local free-`T^2` symmetry on a replacement collar does not imply a global free torus action.

If `N` is the union of replacement regions, `V_removed` is the volume removed from the exact hyperbolic cusps, the complement remains exactly hyperbolic, and `E = Ric + 3g`, then the exact relative Chern–Gauss–Bonnet identity is

`2∫_N |W|² + 12(Vol(N)-V_removed) = ∫_N (|E°|² + 2 tr E - (tr E)²/12)`.

The coarse consequence under `||E||_op <= delta` is

`|2∫_N |W|² + 12(Vol(N)-V_removed)| <= (8 delta + 4 delta²) Vol(N)`.

This is a volume/Weyl balance, not a standalone obstruction. It becomes consequential only if the faithful connector family forces a relative mismatch that does not vanish as lattice and truncation parameters vary.

## Continuing mathematical work

Use the explicit one-cusped orientable 24-cell double-cover piece `24cdc1.1` (or a verified equivalent) as a concrete laboratory. It has a torus cusp, `chi=2`, hyperbolic volume `8 pi²/3`, and maximum-cusp volume `16` by double covering. Its reported homology has `b1=1`, `b3=0`, so the peripheral image has positive rational rank; the cyclic cover theorem then gives degree-`N` one-cusp covers with peripheral type `(N,1,1)` for suitable coprime `N`.

For a depth `T` in such a cover, record on the same normalization:

- piece degree and Euler characteristic;
- boundary flat-lattice covolume `A_T`;
- removed volume `V_removed = A_T/3`;
- actual connector volume `Vol(N)`;
- `∫_N |W|²`;
- the signed relative CGB balance and the complete invariant Ricci defect;
- any approximate-exterior contribution if the complement is not exactly hyperbolic.

Under the earlier rank-one degree-`N`, depth `log N` matching, `A_T` scales like `N exp(-3 log N)=N^{-2}`. The rank-two quotient charged Koiso connector has the same `N^{-2}` volume scaling because it is locally isometric before quotienting. Thus every term in the relative identity naturally scales by `N^{-2}`; collapse alone does not create a contradiction. A useful obstruction must survive after division by connector volume, while a compatible balance sends the effort back to the unresolved full-matrix inner transition.

Canonical derivation: `workspace/notes/step100_relative_cgb_graph_budget.md`.
