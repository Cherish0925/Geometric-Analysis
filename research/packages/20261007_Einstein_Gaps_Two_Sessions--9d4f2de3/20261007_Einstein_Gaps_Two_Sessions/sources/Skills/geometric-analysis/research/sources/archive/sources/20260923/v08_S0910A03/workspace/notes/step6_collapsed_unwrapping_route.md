# Step 6: collapsed unwrapping route after the local calibrated-germ exclusion

## Mathematical starting point

The corrected local theorem is in `step6_local_projector_obstruction_and_collapse_reduction.tex`: a smooth Einstein four-dimensional germ with

\[
\operatorname{Ric}=-g,\qquad
\operatorname{Spec}(W^+)=(-1/6,1/12,1/12)
\]

cannot exist. The full projector divergence equation forces the simple self-dual eigenform parallel, while the Einstein--Weyl equation requires \(|\nabla W^+|^2=1/16\). Hence, on a fixed exact-boundary Ishida--LeBrun manifold, any hypothetical sequence with \(\|\operatorname{Ric}+g\|_{L^\infty}\to0\) must satisfy

\[
\sup_p\operatorname{Vol}B_1(p)\to0.
\]

For varying topology, only a vanishing *volume fraction* of noncollapsed unit balls is presently established because the curvature/SW errors are normalized by \(A_i\).

## What Naber--Zhang actually contributes

The relevant source is

`Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md`.

Their Theorem 1.1 assumes a two-sided Ricci bound, local relative compactness, Gromov--Hausdorff closeness

\[
B_2(p)\simeq B_2(0^{k-\ell},z^\ell)\subset\mathbb R^{k-\ell}\times Z^\ell,
\qquad \ell\le3,
\]

and maximal nilpotency rank

\[
\operatorname{rank}\Gamma_\delta(p)=n-k,
\qquad
\Gamma_\delta(p)=\operatorname{Image}[\pi_1(B_\delta(p))\to\pi_1(B_2(p))].
\]

It then supplies a lower conjugate/weak harmonic radius bound; for exact Einstein inputs it upgrades to curvature control, while for merely bounded Ricci the harmonic-radius conclusion is the relevant one. Its proof also gives noncollapse on a local universal cover. The residual-dimension restriction \(\ell\le3\) is sharp; a four-dimensional Eguchi--Hanson factor defeats the conclusion. Constants depend on the lower-dimensional Ricci-limit model through a noncollapsing radius.

This does not automatically settle the collapsed LeBrun sequence. The following must all be supplied at the same collapsed ball:

1. a controlled lower-dimensional GH model;
2. maximal fibered nilpotency rank;
3. a cover ball of fixed geometric size with a harmonic chart;
4. preservation of the small *mean* calibrated deficit after lifting.

The last point was resolved in Step 8 for normal covers of buffered domains whose relevant cover balls remain interior: disjoint deck translates and Bishop--Gromov comparison give a sheet-independent bound of the cover-ball mean by the corresponding base-ball mean. See `step8_cover_mean_transport_and_model_scope_corrections.md`. The remaining issue is obtaining fixed-scale Naber--Zhang cover regularity on a positive-volume set, not deck multiplicity itself.

## A precise conditional extension

Let \(F_i\ge0\) collect the completion-square and sharp spectral defects whose zero set yields the calibrated spectrum. Suppose a sequence of collapsed balls \(B_2(p_i)\) has:

- bounded Ricci and the Naber--Zhang GH/rank hypotheses with uniform model constants;
- normal covers \(\pi_i:\widehat B_2(p_i)\to B_2(p_i)\) containing fixed-size noncollapsed harmonic charts \(U_i\);
- a transport estimate
  \[
  \fint_{U_i}\pi_i^*F_i\to0.
  \]

Then the same harmonic-coordinate \(W^{2,p}\) passage used in the noncollapsed case gives a smooth Einstein germ with the forbidden calibrated spectrum. Therefore no positive-volume family of collapsed balls can satisfy all three properties simultaneously.

This conditional statement turns the remaining geometry into two alternatives:

- **uniformly modeled maximal-rank collapse:** complete local universal covers expose a forbidden calibrated germ; Step 8's mean-transfer lemma closes the multiplicity issue;
- **inaccessible collapse:** on almost all relevant volume, at least one of GH model control, maximal rank, or uniform model scale fails, or unwrapping exists only at radii tending to zero. The failure can be associated with rank drop, singular fibers, residual four-dimensional bubbles, or concentration regions.

The K3 example in Naber--Zhang is structurally instructive: regular torus fibers have maximal rank, while singular Kodaira fibers have rank drop and curvature concentration. For Yau 26 this suggests locating the Euler/signature and monopole topology specifically on the rank-drop/concentration set, rather than trying to forbid collapse abstractly.

## Relation to the positive branch

S0910A02's constant-length principal-circle calculation excludes one regular free-circle model under tight positive pinching, while \(\chi=0\) excludes a global free circle action on the relevant positive four-manifolds. Those results do not cover warped fibers or singular strata. The shared mechanism is now clear: both signs require distinguishing collapse that unwraps to controlled smooth geometry from collapse whose singular/rank-drop regions carry the essential topology. The negative critical route has the additional forbidden calibrated germ, which provides a sharp target once a cover chart and deficit transport are available.

## Next high-value work

1. Prove a volume-distribution theorem for points satisfying the uniform Naber--Zhang hypotheses: fixed-scale low-dimensional GH model, maximal fibered nilpotency rank, and model noncollapsing radius bounded below.
2. Quantify the complementary regions: rank drop, degeneration of the lower-dimensional model scale, residual four-dimensional cores, and unwrapping only at radii tending to zero.
3. Relate those failures to Euler/signature and monopole curvature budgets without invoking an Einstein-only curvature decomposition.
4. Keep varying-topology and fixed-topology error scales separate. Absolute deficit vanishing is available only for fixed \(A\); normalized smallness does not exclude isolated noncollapsed/concentrated islands.

This remains a four-dimensional negative-branch reduction, not a solution of either normalized branch in all dimensions.
