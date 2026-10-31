# Route assessment after Step 8

## Main correction and advance

Step 8 confirms the Derdziński local mechanism from the primary source and repairs the analytic and measure-theoretic strength of the negative LeBrun route.

The primary source `derdzinski_1983_self_dual_kahler_einstein_four.txt` verifies that if `delta W^+=0` and `W^+` has at most two eigenvalues, then `(24|W^+|^2)^{1/3}g` is locally Kähler on `{W^+ != 0}`, with an essentially unique conformal factor. At the calibrated near-equality spectrum `(-1/6,1/12,1/12)`, this factor is constant, hence the smooth Einstein limit would itself be locally Kähler, contradicting the `Ric=-g` Kähler-Einstein Weyl norm `|W^+|^2=2/3` versus the calibrated `1/24`. The independent projector argument from S0910A03 gives the same contradiction through `nabla W^+=0` versus the Einstein-Weyl identity `|nabla W^+|^2=1/16`.

The theorem now supported is measure-local:

\[
\forall v>0,\quad
\frac{\operatorname{Vol}\{p:\operatorname{Vol}B_1(p)\ge v\}}
     {\operatorname{Vol}M_i}\to0
\]

for varying-topology LeBrun near-boundary negative-pinching sequences satisfying the established mixed-SW bookkeeping. It does not imply `sup_p Vol B_1(p)->0`; noncollapsed islands with `o(Vol M_i)` volume remain possible. For fixed `A` critical boundary manifolds, absolute deficit vanishing gives the stronger `sup_p Vol B_1(p)->0`, as A03 noted.

## Repaired proof objects

- `workspace/notes/step8_derdzinski_measure_local_theorem.md`: revised theorem, primary-source Derdziński verification, explicit LeBrun gap density, local averaging, finite `W^{2,p}` harmonic-coordinate passage, collapse-unwrapping route.
- `workspace/scripts/step8_gap_density_algebra.py`: verifies the completion identity, explicit gap-density algebra, calibrated spectrum recovery, and Kähler-Einstein normalization.
- Source PDF/text: `workspace/data/sources/derdzinski_1983_self_dual_kahler_einstein_four.pdf`, `workspace/notes/sources/derdzinski_1983_self_dual_kahler_einstein_four.txt`.
- TTCS verification: `trace/ttcs/results/step8_ttcs01_verifier1_integration.md` supports the theorem after replacing undefined `Q,P` by explicit `mathcal G`; `step8_ttcs01_generator1_integration.md` gives the local-cover/deck-transport route.

## Current best negative-branch route

The next mathematical object is a local unwrapping theorem, not a global collapse classification. Starting from the volume-proportion collapse regime and small global mean of the explicit deficit density `F_i`, show that a positive-volume family of collapsed balls satisfying Naber-Zhang maximal-rank hypotheses cannot occur because:

1. local mean averaging selects base balls with small maximal mean of `F_i`;
2. a local normal/universal cover restores noncollapse and harmonic radius;
3. a deck-orbit counting estimate transfers small base mean to small cover mean;
4. finite `W^{2,p}` convergence on the cover gives the forbidden calibrated Einstein germ.

The central new lemma to prove is the deck-averaged transport estimate

\[
\fint_{B_a(\hat p)}\pi^*\phi\le C\,\mathcal M_R\phi(p)
\]

under uniform model geometry and maximal fibered nilpotency rank. It should first be tested in flat torus bundle collapse and Heisenberg/nilmanifold collapse, then related to Naber-Zhang graded short-generator constructions. The failure modes that remain meaningful are rank drop, singular fibers, degenerating lower-dimensional models, residual four-dimensional bubbles, and cover-ball multiplicity concentrating on high-deficit sets.

## Relation to the positive branch

S0910A02's new positive calibration family `#_k(S^2 x S^2)` is important. These manifolds have `chi=2+2k`, `tau=0`, known positive Ricci metrics by Sha-Yang, and unknown Einstein status for `k>=2`. If `P_4^+` is true, it would produce Einstein metrics on all of them, a major implication. No current negative LeBrun near-equality inequality directly bounds positive pinching on `#_k(S^2 x S^2)`: the Seiberg-Witten monopole input and general-type blow-up topology are absent, while the sign is opposite. The useful transfer is methodological: tight positive pinching should also be studied through algebraic curvature selection at orbifold/concentration points and through local unwrapping of collapse. A direct quantitative test of achievable `delta_+` in Sha-Yang/Burdick connected-sum metrics would be valuable, but it is a different route.

## Scope

The work remains in Explore. The four-dimensional negative analysis now gives a strong family-level reduction and a precise local contradiction, but it does not resolve `P_4^-` for all closed four-manifolds, does not settle `P_4^+`, and is far from the all-dimensional proposition and Lean formalization. Next work should construct or refute the local-cover transport mechanism rather than write final results.
