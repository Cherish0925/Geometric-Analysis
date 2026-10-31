# Step 16: Preceptor review of the cutoff-smoothing architecture

Session: S0910A01. Agent4/Preceptor. Phase: Execute.

## 1. Immediate correction

The Step 15 route must not be treated as a completed four-dimensional negative-branch proof.  The smoothing program remains one of the best live routes, but the argument that Li's published proof automatically localizes to the plateau is invalid as written.

Two mathematical errors are decisive.

First, Ricci flow is parabolic and has no finite propagation speed.  The phrase that a parabolic propagation distance of order `sqrt(t)` prevents boundary influence is not a theorem.  Freezing the exterior of a cutoff flow does not make the transition annulus invisible to the interior unless one proves quantitative estimates showing how the transition terms enter and remain controlled.  The current notes do not supply such estimates.

Second, the localized supremum in Li's Theorem 3.4 cannot be closed by simply restricting attention to an inner plateau.  Li's proof uses

\[
 e_0(t)=\sup_x \left(\int_{B_r(x)} f^2\right)^{1/2}
\]

simultaneously over all centers under consideration.  If the supremum is taken over the working region `Omega_work`, then centers near the boundary require covering balls outside `Omega_work`.  If the supremum is restricted to an inner region, the evolution estimate for an inner ball uses adjacent outer balls and returns to the unclosed inner/outer problem that A03 had already corrected in Step 14.  This is not an exposition gap; it is a quantifier mismatch in the proof.

A related scale mismatch is present in the Step 15 plateau construction.  The comparable-ball Bishop--Gromov calculation is valid for centers within `5 r_*/2` of a selected maximal-function good point.  It does not, as written, control all centers throughout a much larger ball such as `B_{rho/4}(p)` when `r_* << rho`.  Either the support must be chosen at the same scale as the controlled covering, or one must use a stronger maximal-function condition covering all centers in the support.

Therefore the group statement that the four-dimensional negative-branch chain is complete should be withdrawn.  Agreement among sessions based on the same locality argument is not independent verification.

## 2. What remains valid and valuable

The following parts of the Step 15 architecture are still mathematically useful.

### 2.1 Comparable-ball initial smallness

If

\[
\mathcal M_R(|\operatorname{Rm}|^2)(p)\le K_0,
\qquad 4r_*\le R,
\]

and `d(p,y) <= 5r_*/2`, then

\[
B_{r_*}(y)\subset B_{7r_*/2}(p)\subset B_{4r_*}(p)
\]

and

\[
B_{4r_*}(p)\subset B_{13r_*/2}(y).
\]

Under `Ric >= -3g`, Bishop--Gromov gives

\[
r_*^4\fint_{B_{r_*}(y)}|\operatorname{Rm}|^2
\le r_*^4 K_0\,{V_{-1}(13r_*/2)\over V_{-1}(r_*)}.
\]

Taking `r_*` small after fixing a bounded comparison range makes Li's initial dimensionless quantity small independently of collapse.  This calculation is sound but local in the precise sense above.

### 2.2 Sobolev--energy volume cancellation

On a ball with Ricci lower bound, the relative Sobolev coefficient has the form

\[
A_r\lesssim {r^2\over \operatorname{Vol}(B_r)^{1/2}}.
\]

Thus

\[
A_r\,\|\operatorname{Rm}\|_{L^2(B_r)}
\lesssim r^2\left(\fint_{B_r}|\operatorname{Rm}|^2\right)^{1/2},
\]

so collapsed volume cancels in the critical four-dimensional product.  This is the main reason the smoothing route remains worth developing.

### 2.3 Homogeneity of the cutoff defect equation

For the cutoff normalized flow

\[
\partial_t g=-2\chi^2E,
\qquad E=\operatorname{Ric}+g,
\]

the variation formula checked in A03's Step 14 note and script has the form

\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E),\qquad a=\chi^2,
\]

where all terms in `C_a(E)` contain `E`, `nabla E`, or their traces.  Hence exact negative Einstein metrics are stationary even through the transition.  This removes an additive source at `E=0`; it does not by itself bound amplification of a small nonzero defect.

### 2.4 Topological recalibration, with the right input

The LeBrun mixed Seiberg--Witten estimate and Chern--Weil identities apply to any smooth metric on the same closed oriented smooth four-manifold.  Therefore, if a smoothed terminal metric `h_i` satisfies

\[
J_i(h_i)= {1\over 4\pi^2}\int {|
\mathring{\operatorname{Ric}}_{h_i}|^2\over2}=o(A_i),
\]

then the near-saturation computation can be rerun for `h_i` without transporting `W^+` along the flow.  For the varying LeBrun laboratory the needed target is `J_i(h_i)/A_i -> 0`, not necessarily absolute `J_i(h_i)->0` and not necessarily pointwise `|E|=O(delta_i)` everywhere.

To recover the full calibrated spectrum, use the Step 8 tensor-deficit route.  The nonnegative density

\[
\mathcal G=f^2-(a_-)^2,
\qquad
f={2\over3}s-2\sqrt{2/3}|W^+|,
\qquad
a={2\over3}s+2w
\]

satisfies

\[
0\le\int \mathcal G\le48\pi^2D.
\]

Together with the modulus/completion remainder and strong curvature convergence on a chart, `G -> 0` gives the spectrum

\[
\operatorname{spec}(W^+)=(-1/6,1/12,1/12).
\]

This is stronger and cleaner than the new harmonic-form unique-continuation passage.  A nonzero global harmonic form can have vanishing local mass along a chosen sequence of charts; unique continuation has no uniform mass content.  Also, the harmonic representative of a monopole class is not literally the self-dual form in the Seiberg--Witten spinor proof, and one eigenspace condition alone does not force equality of the other two eigenvalues.

### 2.5 Derdziński forbidden germ

The Step 8 local theorem remains the right final local contradiction.  If a controlled chart or cover limit is Einstein with `Ric=-g` and the explicit Step 8 defects vanish locally, then the limit has the calibrated two-eigenvalue `W^+` spectrum.  Derdziński Proposition 5 makes the natural conformal metric locally Kähler, and at constant `|W^+|^2=1/24` the conformal factor is constant.  This contradicts the Kähler--Einstein `Ric=-g` value `|W^+|^2=2/3`.

## 3. Correct repair target for the smoothing route

The productive next mathematical object is not another assertion that the plateau equation is ordinary Ricci flow.  It is a closed stability estimate on the whole support, with cutoff weights and transition terms included.

A useful target theorem should have this shape.

Let `U=B_L(p)` be a buffered support, with cutoff `chi` supported in `U` and equal to one on a smaller region.  Choose the Li scale `r_*` and the support scale consistently, for example by covering the entire support with centers for which the comparable-ball maximal-function bound is known.  Under

\[
\sup_{y\in U'} r_*^4\fint_{B_{r_*}(y)}|\operatorname{Rm}_{g_0}|^2\le\varepsilon,
\qquad
|\operatorname{Ric}_{g_0}+g_0|\le\delta,
\]

prove for the cutoff flow on the closed manifold, on a time interval `0<=t<=theta r_*^2`, all of the following with constants independent of collapse:

1. existence and metric equivalence on the support;
2. persistence of the local normalized curvature energy needed for Li/Moser absorption;
3. interior curvature bound `|Rm(t)| <= C/t` on the plateau;
4. transition-inclusive defect control sufficient for
   \[
   {1\over A_i}\int_{M_i}|\mathring{\operatorname{Ric}}_{g_i(t_0)}|^2\to0.
   \]

The energy estimate should retain the transition terms.  A03's integrated identity is a good starting point:

\[
\begin{aligned}
{d\over dt}\int\eta^2|E|^2
+c\int\eta^2a|\nabla E|^2
\le{}&C\int(a|d\eta|^2+\eta^2|d\chi|^2+\eta^2a)|E|^2\\
&+C\int\eta^2a|\operatorname{Rm}|\,|E|^2.
\end{aligned}
\]

The last term can be attacked by the same collapse-canceling Sobolev product.  Homogeneity in `E` is valuable here because every transition contribution is proportional to small defect quantities after integration by parts; it is not a substitute for the estimate.

For the global topological recalibration, it may be enough to prove a weaker normalized integral statement

\[
Q_i(t_0)/A_i\to0,
\qquad Q_i(t)=\int|E_i(t)|^2,
\]

rather than pointwise `O(delta_i)` everywhere.  This matters because the transition annuli may occupy a fixed proportion of the total volume in the varying-topology sequence.

## 4. Cover reconstruction remains a separate problem

Bounded curvature on the smoothed plateaux would be a substantial improvement.  It does not automatically produce the exact chart-accessible normal covers used in the Step 9--11 mean-transport theorem.

The needed geometric statement must supply, on a fixed proportion of the smoothed plateau volume, a genuine buffered normal Riemannian cover with:

- uniform lifted ball noncollapse;
- uniform harmonic-radius control;
- enough domain buffer for the deck-averaging lemma;
- constants depending only on curvature and chosen scales;
- explicit handling of rank drop, singular strata, and contractible short orbits.

Citing Naber--Zhang or CFG by name is not enough unless the required residual-dimension/rank or local fibration hypotheses are verified.  If such a theorem is proved or sourced precisely, the Step 8 Derdziński mechanism can be applied after pulling back the explicit tensor-defect densities by the normal-cover mean lemma.

## 5. Actual scope of the prospective result

The current smoothing route is tied to the LeBrun/Ishida--LeBrun critical topology.  The calibration and energy budget use the specific four-dimensional Seiberg--Witten and Chern--Weil structure.  Closing this route would exclude an important family of negative-branch counterexample sequences near `k/A -> 1/3`; it would not prove the full four-dimensional negative sign branch for arbitrary no-Einstein four-manifolds, and it would not address dimensions `n >= 5`.

The route remains high-value because a collapse-uniform, defect-preserving local smoothing theorem could become a transferable tool beyond the current laboratory.  But the next work must establish that mechanism or expose its obstruction, not turn the Step 15 architecture into a finished proof.

## 6. Files reviewed

- `Sessions/S0910A01/workspace/notes/step15_cutoff_smoothing_architecture.md`
- `Sessions/S0910A03/workspace/notes/step15_L2_chain_and_separated_demands.md`
- `Sessions/S0910A01/trace/ttcs/results/step15_ttcs01_verifier1_integration.md`
- `Sessions/S0910A01/workspace/plans/route_assessment_step15.md`
- Ye Li source lines 219--278 in `Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md`
- `Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md`
- `Sessions/S0910A03/workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md`
- `Sessions/S0910A03/workspace/scripts/verify_cutoff_defect_energy.py`

## 7. Scale-consistent support choice for the next construction

A clean way to remove the `rho >> r_*` mismatch is to make the smoothing support itself a fixed multiple of the Li scale.

Fix constants

\[
1<\ell_{\rm in}<\ell_{\rm work}<\ell_{\rm supp}<R_0/r_*
\]

with all ratios independent of the sequence, for instance inner radius `2 r_*`, working radius `8 r_*`, support radius `16 r_*`.  Let the maximal-function good set be

\[
G_i=\{p: \mathcal M_{R_0}(|\operatorname{Rm}|^2)(p)\le K_0\}.
\]

Apply Vitali at radius `r_*` to choose disjoint balls `B_{r_*}(p_j)` with centers in `G_i`, so that `G_i` is covered by `B_{5r_*}(p_j)`.  Bishop--Gromov then gives a positive lower bound for the total volume of the selected disjoint balls, and hence also for smaller/larger fixed-multiple subfamilies after adjusting constants.

For any center `y` lying in `B_{L r_*}(p_j)`, the maximal-function bound at `p_j` controls

\[
\int_{B_{r_*}(y)}|\operatorname{Rm}|^2
\le
K_0\operatorname{Vol}(B_{(L+1)r_*}(p_j)),
\]

and Bishop--Gromov compares `Vol(B_{(L+1)r_*}(p_j))` to `Vol(B_{r_*}(y))` by a constant depending only on `L` and the Ricci lower bound.  Thus every center required by the support-scale covering has the initial Li smallness if `r_*` is chosen small enough.

This support-scale choice does not solve the parabolic or transition estimates.  It only repairs the static quantifiers in the initial smallness input.  The real theorem remains a weighted local-flow stability theorem on the whole support, using the cutoff equation and summing over the separated supports.

## 8. A03 exponential-pullback averaging route

A03 message #276 proposes a useful replacement for the still-conditional CFG/rank accessibility layer.  Suppose a smoothed region has sectional curvature bound `|sec| <= K` along all radius-`r` geodesics from a positive-volume center set `P`, with `r < pi/(2 sqrt(K))`.  For a nonnegative density `F`, A03 states

\[
\int_{p\in P}\fint_{B_r(0)\subset T_pM} F(\exp_p v)\,J_p(v)\,dv\,dp
\le C(n,K,r)\int_M F,
\]

where

\[
C(n,K,r)=
{\int_0^r \sinh(\sqrt K t)^{n-1}\,dt
 \over
 \int_0^r \sin(\sqrt K t)^{n-1}\,dt}
\]

(up to the precise normalization of the pulled-back average).  This uses Rauch Jacobian bounds and Liouville invariance of the geodesic flow, not injectivity radius, sheet counts, or nilpotent rank.  If correct, it is a significant improvement: once the smoothing theorem gives bounded-curvature buffered plateaux of positive volume, one can select exponential-chart pullbacks with small mean of the explicit Step 8 tensor-defect density even in the presence of conjugate/multiple covering, avoiding the need for a CFG normal cover at this stage.

This new route still needs exact formulation.  The selected exponential pullback balls are not injective coordinate charts on the manifold; the pulled-back metric on a tangent ball is smooth with bounded curvature, but the relation to harmonic-radius compactness and to the Derdziński germ must be written.  A plausible path is: use the pullback metric on the Euclidean ball, bounded sectional curvature and bounded Ricci defect to obtain harmonic charts on smaller tangent balls by standard local elliptic smoothing, pass the pulled-back tensor defects by the averaged inequality, and apply the Step 8 forbidden germ.  The averaging must include all nonnegative densities needed for the contradiction: `|E|^2`, the completion-square modulus defect, and the explicit lowest-eigenvalue gap `G`.  It should not rely on harmonic-form unique continuation or local monopole-form mass.

Thus A03's lemma may remove the separate CFG sheet/rank problem after bounded-curvature plateaux exist.  It does not address the analytic cutoff-flow stability theorem; that remains the central missing bridge.
