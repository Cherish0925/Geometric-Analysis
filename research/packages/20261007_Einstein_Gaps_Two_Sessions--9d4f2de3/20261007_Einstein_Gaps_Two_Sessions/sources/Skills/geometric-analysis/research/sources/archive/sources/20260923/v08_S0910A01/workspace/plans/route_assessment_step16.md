# Route assessment after Step 16

## What changed

Step 16 withdrew the Step 15 completed-proof wording for the four-dimensional negative LeBrun/Ishida--LeBrun route.  The local smoothing program remains valuable, but the argument that Li's published proof directly localizes to a plateau is not valid as written.

The correction is mathematical, not stylistic:

- Ricci flow has no finite propagation speed; a distance of order `sqrt(t)` is not a shield from transition geometry.
- Li's energy-bootstrap supremum over a working region requires neighboring covering balls for centers near the boundary.  These balls leave the region unless the region is enlarged; restricting the supremum to an inner region recreates an unclosed inner/outer system.
- A maximal-function good point controls nearby centers only at the comparable `r_*` scale.  It does not control every center in a much larger plateau when `r_* << rho`.
- Homogeneity of the cutoff defect equation removes additive forcing at `E=0`, but does not bound amplification of small nonzero `E` without a weighted energy estimate.

The live correction note is `workspace/notes/step16_preceptor_review_smoothing_architecture.md`; the patched Step 15 route file is `workspace/plans/route_assessment_step15.md`.

## Reliable pieces retained

1. **Comparable-scale initial smallness.**  If `p` is a maximal-function good point and `y` lies within a fixed multiple of `r_*`, then Bishop--Gromov gives
   \[
   r_*^4\fint_{B_{r_*}(y)}|Rm|^2
   \le C(L)K_0r_*^4.
   \]
   Choosing `r_*` fixed and small gives Li-scale initial smallness independently of collapse.

2. **Four-dimensional Sobolev--energy cancellation.**  The product
   \[
   A_r\|Rm\|_{L^2(B_r)}
   \lesssim r^2(\fint_{B_r}|Rm|^2)^{1/2}
   \]
   cancels the collapsed volume factor.  This is the main analytic reason to continue the smoothing route.

3. **Homogeneous cutoff defect equation.**  For `a=chi^2`,
   \[
   \partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E)
   \]
   and all transition terms in `C_a(E)` are proportional to `E`, `nabla E`, or traces.  A03's integrated formula removes Hessian-cutoff terms and leaves an energy inequality of the schematic form
   \[
   {d\over dt}\int\eta^2|E|^2+c\int\eta^2a|\nabla E|^2
   \le Cr^{-2}\int_{supp\eta}|E|^2
   +C\int\eta^2a|Rm||E|^2.
   \]

4. **Topological recalibration after global integral defect control.**  For a terminal closed smooth metric on the same critical topology, `J/A -> 0` is enough to rerun Chern--Weil and LeBrun mixed Seiberg--Witten near-saturation.  The full spectrum should be recovered using Step 8's explicit nonnegative density `G`, not by relying on harmonic-form local mass.

5. **Derdziński forbidden germ.**  Once controlled local charts or pulled-back exponential charts have `F_i -> 0` for
   \[
   F_i=|E_i|^2+(s_i+8\sqrt6|W_i^+|)^2+\mathcal G_i,
   \]
   Step 8 gives a smooth Einstein limit with the calibrated `W^+` spectrum, contradicting Derdziński's local conformal-Kähler theorem.

## TTCS Step 16 result

The TTCS verifier supported the Step 16 correction.  It judged the weighted-energy route viable in scale and sign, but not closed by existing sources.  Its main guidance:

- Choose support radii as fixed multiples of the Li scale `r_*` so initial smallness holds for all centers actually used.
- A support-total curvature energy bound is not enough; one must prevent local re-concentration and keep each relevant `r_*` ball below the critical absorption threshold during the flow.
- The `E`-energy inequality likely closes if the curvature energy persistence is available, yielding `Q_i(t_0)/A_i -> 0` without needing global pointwise `E=O(delta_i)`.
- Li supplies global all-centers Ricci-flow smoothing; Yang/Wang supply local Ricci-flow frameworks; neither directly gives the required normalized cutoff-flow theorem with collapsed supports and transition terms retained.

Saved TTCS result: `trace/ttcs/results/step16_ttcs01_verifier1_integration.md`.

## Refined analytic theorem to attempt

Use a support scale comparable to `r_*`.  Select disjoint or uniformly overlapping supports around maximal-function good centers, with

\[
B_{2r_*}(p_j)\subset B_{8r_*}(p_j)\subset \{\chi_j=1\}\subset \operatorname{supp}\chi_j\subset B_{16r_*}(p_j),
\qquad |d\chi_j|\le Cr_*^{-1}.
\]

For the cutoff normalized flow

\[
\partial_tg=-2\chi^2(\operatorname{Ric}+g)
\]

on the original closed manifold, prove with constants independent of collapse and of the number of supports:

1. existence for `0 <= t <= theta r_*^2` and metric/volume comparability on the active supports;
2. persistence of the local normalized curvature energy on every relevant `r_*` ball, not just support-total energy;
3. interior curvature control `|Rm| <= C/t` on the inner plateaux;
4. support-summed or global defect control
   \[
   Q_i(t_0)/A_i\to0,
   \qquad Q_i(t)=\int |E_i(t)|^2,
   \]
   sufficient for `J_i(t_0)/A_i -> 0`;
5. compatibility with the Step 8 tensor-deficit density on the terminal smoothed metric.

A proof should retain the `chi` transition terms rather than treating the plateau as isolated.  The key estimates to close are the coupled local curvature-energy and defect-energy inequalities.

## Post-smoothing geometric layer

A03 message #276 gives a promising alternative to the prior CFG/rank route.  Under bounded sectional curvature on radius-`r` geodesics from a positive-volume center set `P`, the exponential-pullback averaging lemma gives

\[
\int_P A_rF(p)\,dp\le C(n,K,r)\int_MF.
\]

A01 wrote an independent derivation and interface note at `workspace/notes/step16_exponential_pullback_averaging_review.md`.  This method uses Rauch Jacobian bounds and Liouville invariance, not normal covers or nilpotent rank.  If the smoothing theorem produces bounded-curvature buffered exponential balls on a positive-volume center set, this averaging can select pulled-back balls with small Step 8 tensor-defect mean and then produce the Derdziński contradiction through local harmonic-coordinate compactness.

Thus the old CFG accessibility layer may be replaceable after bounded-curvature plateaux are obtained.  This does not affect the main analytic missing bridge: transition-inclusive cutoff-flow stability.

## Scope

Even if the refined smoothing theorem and exponential-pullback layer are proved, the resulting theorem would exclude the current critical LeBrun/Ishida--LeBrun negative counterexample laboratory.  It would not by itself prove the full four-dimensional negative branch for arbitrary no-Einstein smooth four-manifolds, would not settle the positive branch, and would not address dimensions `n >= 5`.

## Best next work

The next agent should construct or refute the refined analytic theorem.  The most useful route is to write the coupled local energy system explicitly for `Rm` and `E` under the normalized cutoff flow, including all `d chi` terms, and determine whether the four-dimensional Sobolev--energy cancellation closes both local curvature-energy persistence and `Q/A` defect control on a family of separated supports.  If this becomes too source-dependent, compare it against Yang/Wang local-flow hypotheses to see whether an existing theorem can be adapted with the same support-scale choices.
