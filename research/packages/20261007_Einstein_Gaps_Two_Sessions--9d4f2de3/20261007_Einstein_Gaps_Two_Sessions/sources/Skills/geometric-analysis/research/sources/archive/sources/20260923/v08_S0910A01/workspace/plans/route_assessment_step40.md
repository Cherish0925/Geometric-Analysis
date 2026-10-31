# Route assessment after Step 40

## Main outcome

Agent4 reviewed the Step 39 assembled defect-gap theorem and A03's Step 41 reply.  The result is not yet a rigorous theorem.  It is a strong restricted proof architecture for the four-dimensional negative Ishida--LeBrun near-critical laboratory, and several pieces are genuinely valuable, but Step 39 silently used assumptions that are not supplied by the existing evidence.

The review is saved in `workspace/notes/step40_preceptor_review_step39_interfaces.md`.  TTCS independently supported the same assessment in `trace/ttcs/results/step40_ttcs01_verifier1_integration.md`.

## Preserved scientific value

- The near-critical SW/Chern--Weil calibration and Derdziński forbidden germ remain the strongest four-dimensional negative-family mechanism.
- Step 35's Hessian-a tensor contractions are usable and explain why sequence-uniform cutoff Hessian bounds should not be required.
- Step 34's homogeneous fixed-exponent chain and Moser endpoints remain a coherent smoothing mechanism under the correct first-exit hypotheses.
- A03 Step 40's staggered derivative-energy induction is a real repair of the cutoff-jet finite-exponent loop, once the structural U/T/cutoff equations are actually derived.
- Step 28's terminal recalibration and Liouville--Rauch pullback passage remain the correct downstream geometry.

## Interfaces requiring repair before the restricted theorem is established

1. **Support lemma.**  Lemma 3.1 must not assert `||∇²χ||≤Cr⁻²` from only Ricci lower bound and averaged curvature.  Use smooth gradient-controlled cutoffs with higher jets finite per datum, choose `7r≤R`, arrange disjoint outer buffers, run one global cutoff flow `a=sum χ_α²`, and use inner center sets for terminal geodesic buffers.

2. **Homogeneous K₂ propagation.**  Replace the Step 39 inequality containing a bare `C₀T` by the Step 34 multiplicative estimate
   `K₂' + cD₂ ≤ CY + Cr⁻²K₂`, `Y≤Cγ(D₂+r⁻²K₂)`, hence `K₂(t)≤exp(C(1+r⁻²)t)K₂(0)`.  A naked additive term cannot be absorbed uniformly when support volume collapses unless its volume dependence is shown.

3. **Shifted evolution formulae.**  Derive the normalized weighted-U and unweighted-T equations, including `∂tG`, `∂tΓ`, Bianchi/commutator terms, all derivatives of `a=χ²`, and normalization terms, before applying A03's staggered induction.

4. **Zero-order unweighted T.**  Step 35 supplies the signed Hessian-a mechanism but not the full unweighted `T∈L^q` lemma with G, normalization, stationary-region terms, and `|U|`-bounded reactions.  This lemma must be written.

5. **Transported DeTurck.**  A03's gauge architecture is correct and likely adaptable from Yang, but the proof still needs the actual ε-independent tame estimates, regularization limit, local uniqueness, and restart theorem stated against the exact source theorem.

6. **Topology/sign assumptions.**  The terminal `D_a≤J` and `119Q` bound require either the above-critical regime `q=k-A/3≥0` and terminal selection of a monopole class with `(a⁺)²≥A`, or an explicit `q_-` error carried through the density estimate.

7. **Terminal pullback compactness.**  Replace Step 39 §7 by the Step 28 version: inner centers, Liouville--Rauch averaging over the whole center set, one or more radius shrinks, and strong finite-`W^{2,p}` convergence (or smooth convergence from plateau derivative bounds).  Weak `W^{2,p}` convergence and Lipschitz-in-metric language do not pass Weyl spectra.

## Relation to peer updates

A03 #355 says H1 is discharged.  Step 40's review does not accept that as a completed theorem, because A03 Step 37 and Step 41 still rely on schematic tame-estimate and structural-equation interfaces.  Their work is useful and should be absorbed into the next constructive repair.

A02 #357 reports a promising positive noncollapsed four-dimensional Route A based on Cheeger--Naber harmonic-radius control and mode projection/Ozuch obstruction.  It remains conditional on noncollapse and on verifying the Bianchi-gauge radial ODE.  It is complementary but does not alter the negative-flow repair task.

## Logical correction for the full proposition

For each fixed dimension, the original interval proposition is equivalent to `P_n^+ or P_n^-`: a proof needs one forcing sign branch in that dimension, not both.  A refutation in one fixed dimension must defeat both sign branches.  The Step 39 route assessment was patched to remove the stronger-than-needed proof wording.

## Best next work

The next agent should be Agent2 in Execute.  The most valuable action is to write a corrected restricted-theorem note that incorporates the Step 40 repairs and begins turning the architecture into a proof: revised support lemma, global cutoff flow, homogeneous K₂ propagation, explicit zero-order unweighted T lemma, arbitrary-order shifted U/T/cutoff structural proposition, normalized Yang start/restart theorem, and corrected terminal passage.  This is still research-facing proof construction, not final expression.
