# Step 14: Fixed-scale smoothing versus reduced-system reconstruction

Session: S0910A01.  Agent1/Orchestrator.  Phase: Explore.

## 1. Why this note was needed

Step 13 produced a valuable normalization-invariant rank-one reduction, but its route assessment still contained two live overstatements:

1. **Static/rank-one closure was overstated.**  The TTCS verifier and A03's reduced-equation note show that neither staticity by itself nor the condition \(H\ge 0\) supplies fixed-scale cover access.  In particular, Bishop--Gromov from a Ricci lower bound gives relative comparison, not an absolute volume anchor, and \(v>0\) for each individual metric gives no sequence-uniform lower bound on a buffered ball.

2. **The smoothing route was dismissed for the wrong scale reason.**  A03's Step 12 note objected that the calibrated bulk has nonzero background curvature, so the local energy input for smoothing is not small.  But Ye Li's Theorem 3.6 uses the dimensionless quantity
   \[
   \frac{r^4}{\operatorname{Vol} B_r(x)}
   \int_{B_r(x)} |\operatorname{Rm}(g_0)|^2\,dV_{g_0}
   \le \varepsilon,
   \]
   not the unit-scale mean itself.  A bounded unit-scale curvature mean becomes small after choosing a sufficiently small but fixed physical radius \(r\).  This is different from choosing radii that go to zero with the sequence: once \(r\) is fixed, the normalized negative Einstein scale remains nonzero.

The purpose of this note is to compare the two remaining geometry-recovery routes without treating either as solved.

## 2. What the Li/Yang/Xu smoothing sources actually say

### 2.1 Ye Li, dimension four, no noncollapse assumption

The retrieved primary object is
`Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md`.

Relevant source points:

- Lines 23--25 state the goal: bounded Ricci plus curvature having no local concentration everywhere gives smoothing to bounded sectional curvature, without assuming a local Sobolev bound, so it can apply in collapsing dimension-four settings.
- Lines 29--32 explicitly distinguish the problem from harmonic-coordinate regularity in collapsed spaces and motivate smoothing because good coordinates do not exist directly under bounded Ricci and collapse.
- Lines 41--50 describe the Cheeger--Tian/Li input: a dimension-four bounded-Ricci estimate controls the normalized local \(L^2\) curvature quantity even in collapse and can make it small after shrinking to a comparable concentric scale.
- Lines 56--70 state Theorem 1.1 in one version: on a complete noncompact 4-manifold, if \(\int_{B_r(x)}|\operatorname{Rm}|^2\le\varepsilon\) for every \(x\) and \(|\operatorname{Ric}|\le K\), then Ricci flow exists for time \(T\gtrsim\min(r^2,K^{-1})\) and \(|\operatorname{Rm}(t)|\le C/t\).
- Lines 321--329 restate it in the dimensionless collapsed form:
  \[
  \frac{r^4}{\operatorname{Vol}B_r(x)}
  \int_{B_r(x)} |\operatorname{Rm}|^2\le\varepsilon,
  \qquad |\operatorname{Ric}|\le K,
  \]
  with the same existence and curvature conclusion.
- Lines 331--335 explain that the proof uses volume comparison to compare volumes of nearby balls in \(B_{3r/2}(x)\), i.e. the all-centers condition is being used locally in the covering argument.
- Lines 337--341 state a Cheeger--Tian/Li shrinking principle: if an absolute small \(L^2\) curvature bound holds on \(B_r(x)\), a smaller concentric ball of radius \(cr\) satisfies the dimensionless smallness condition.

The theorem as written is an **all-centers smoothing theorem** on a complete manifold.  It is not yet a theorem that one selected good center alone gives a local flow on a buffered ball.  However, the proof structure suggests a local version may follow if the dimensionless smallness holds for every center in a buffered domain and one uses conformal completion/local flow.

### 2.2 Yang and Xu: local versions need Sobolev/noncollapse or a ball condition

The Yang source acquired in this step is
`Sessions/S0910A01/staging/acquired/Smoothing_metrics_on_closed_Riemannian_manifolds_through_the_Ric_fa6eb33b3e266a05/content.md`.
It gives a closed-manifold theorem with \(|\operatorname{Ric}|\le K\), a **uniform local Sobolev inequality for all centers**, and a small critical \(L^{n/2}\) curvature norm on all such balls (lines 32--48).  It records that Ye Li's four-dimensional hypotheses are weaker in dimension four (lines 49--50).  This is useful for comparison but does not by itself remove collapse.

The Wang pseudolocality source
`Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md`
uses a local ball condition including a small volume lower bound at scale \(\tau r\), small \(L^{n/2}\) curvature, and an \(L^p\) Ricci bound (lines 35--64).  It is truly local but noncollapse enters through the volume/isoperimetric hypothesis; this is not the collapsed bridge needed for Yau 26.

The Huang--Wang local collapsing paper
`Knowledge/objects/papers/Ricci-flow-smoothing-for-locally-collapsing-manifolds-arXiv--fd31dbed4f1f--11306ef80968/object.md`
provides a different source-grounded local smoothing route.  Its Theorem 1.1 is purely local (lines 48--62), but assumes every point in \(B_g(K,R)\) is Gromov--Hausdorff close to a lower-dimensional Euclidean model and the pseudo-local fundamental group has maximal nilpotency rank.  Lemma 2.4 then gives almost Euclidean volume/isoperimetric estimates on local normal covers (lines 174--214), and the flow has curvature control on \(B_g(K,R/4)\) (lines 53--54, 278--280).  This is very close to the existing Naber--Zhang accessibility package: it is powerful when model/rank information is available, but it is not a replacement for proving such information on the calibrated bulk.

## 3. The fixed-small-radius calculation

Suppose a four-dimensional region has Ricci bounded below and a local mean curvature bound
\[
\fint_{B_R(p)} |\operatorname{Rm}|^2 \le K_0
\]
on a ball of radius \(R\) in the normalized negative Einstein scale.  If \(q\in B_{R/4}(p)\) and \(0<r\le R/4\), then \(B_r(q)\subset B_{R/2}(p)\).  More locally, if
\[
\fint_{B_{2r}(p)} |\operatorname{Rm}|^2\le K_0,
\]
then for every \(q\in B_r(p)\), Bishop--Gromov under \(\operatorname{Ric}\ge -3g\) gives
\[
\frac{\operatorname{Vol}B_{2r}(p)}{\operatorname{Vol}B_r(q)}
\le
\frac{V_{-1}(3r)}{V_{-1}(r)}
\]
(up to the chosen normalization of the lower Ricci bound), because \(B_{2r}(p)\subset B_{3r}(q)\).  Therefore
\[
\fint_{B_r(q)} |\operatorname{Rm}|^2
\le
C_{BG}(r) K_0,
\]
and the Li smallness quantity obeys
\[
\frac{r^4}{\operatorname{Vol}B_r(q)}\int_{B_r(q)}|\operatorname{Rm}|^2
\le r^4 C_{BG}(r)K_0.
\]
For \(r\le1\), \(C_{BG}(r)\) is bounded by a dimensional constant.  Hence if
\[
r \le r_*(K_0):=\left(\frac{\varepsilon_{Li}}{2C_{BG}K_0}\right)^{1/4},
\]
the Li smallness input holds at every center in the smaller buffered ball.

This calculation is the important scale distinction: a nonzero calibrated background with \(K_0=O(1)\) does not block Li's hypothesis.  One just chooses \(r_*\) small once, independent of the sequence.  The Einstein scale has not disappeared, because \(r_*>0\) is fixed before passing to \(i\to\infty\).

In the LeBrun near-critical regime the global Noether/Chern--Weil estimate gives a uniform global mean bound for the full curvature operator in the adopted normalization.  A local Hardy--Littlewood/maximal selection therefore gives a positive-volume set of points with such a bound on all radii up to a fixed macroscopic \(R\), after discarding a controlled fraction by choosing the maximal threshold.  Intersecting with the small calibrated-defect set is compatible with the already established global \(o(A)\) defect estimates.

## 4. What smoothing would give if localized correctly

A successful local smoothing application would give, on a buffered region around a selected point:

1. a Ricci-flow or local-flow metric \(g_i(t)\) for \(0<t\le T\sim r_*^2\);
2. full curvature bound \(|\operatorname{Rm}(g_i(t))|\le C/t\), hence \(|\operatorname{Rm}(g_i(\theta r_*^2))|\le C(\theta)/r_*^2\);
3. metric/distance distortion estimates or at least uniform bilipschitz comparability between \(g_i(0)\) and \(g_i(t)\) on a smaller buffer;
4. a bounded-sectional-curvature collapsed-geometry setting where Cheeger--Fukaya--Gromov/Naber--Zhang/Huang--Wang type structure can be applied to obtain actual normal covers or nilpotent fibrations on regular pieces.

This would be a source-grounded way to get the fixed-scale chart/accessibility object used in Steps 8--11, without assuming an exact circle action in the original metric.

## 5. The two main bridges still missing

### 5.1 Localizing Li's all-centers theorem

Li's Theorem 3.6, as stated in the retrieved source, assumes the small dimensionless curvature quantity for every center in the complete manifold.  The selected-good-ball calculation supplies it for every center only in a buffered subdomain.  To use it rigorously, one needs one of:

- a local/conformal-completion version of Li's proof where the smallness condition is imposed on every center in a buffer and the conclusion holds on an interior sub-ball;
- Yang/Xu local Ricci-flow estimates with a collapsed replacement for Sobolev constants in dimension four;
- Huang--Wang local smoothing, but then one must first verify its GH-model and maximal-rank assumptions on the selected bulk.

The existing source quotations strongly suggest that local versions are natural, but they do not by themselves prove the exact local theorem needed here.

### 5.2 Preserving or recovering the near-Einstein and calibrated data

A curvature estimate \(C/t\) alone does not produce the Derdziński contradiction.  We still need the original small Einstein error and calibrated \(W^+\) defect to be available on a controlled chart/cover.  There are two possible uses of smoothing:

**Use smoothing only to find geometry for the original metric.**  If the flow gives bounded-curvature nilpotent charts/covers and the metric distortion is controlled, perhaps those covers can be transferred back to \(g_i(0)\).  Then the original defects are used directly, and the Step 8 finite-\(p\) harmonic-coordinate passage supplies the forbidden germ.  This avoids proving that calibration survives the flow, but it requires a robust backward-transfer of harmonic or controlled coordinates from the smoothed metric to the original bounded-Ricci metric.

**Use the smoothed metrics themselves.**  Then one must show that under a normalized Ricci flow (or after correcting the unnormalized scaling) the tensor
\[
E_i(t)=\operatorname{Ric}_{g_i(t)}+g_i(t)
\]
remains \(o(1)\) on the interior for fixed small time, and that the calibrated \(W^+\) residual remains small enough.  The normalized Einstein defect satisfies a homogeneous parabolic equation with coefficients involving \(\operatorname{Rm}\); a bound \(|\operatorname{Rm}|\le C/t\) may amplify \(\delta_i\) only polynomially in \(t\), so \(\delta_i\to0\) could still survive at each fixed \(t>0\), but this must be proved in the local-flow setting.  The \(W^+\) calibration is harder: for a fixed positive time, the flow can change Weyl data by an amount depending on the chosen time.  One may need a two-parameter argument: choose \(r_*,\theta>0\) fixed but very small relative to the forbidden-germ gap, then let \(i\to\infty\), and only afterwards let \(\theta\downarrow0\) if necessary.

Either use requires real analysis beyond the statement \(|\operatorname{Rm}(t)|\le C/t\).

## 6. Comparison with the reduced-system route

The Step 13 reduced equations remain valuable, but their target should be weakened.

The identity
\[
H=\frac13I+\frac14(|z|^2I-z\otimes z)-\frac12(W^++W^-)
\]
shows that calibrated \(W^+\) does not force \(H\ge0\).  A negative eigenvalue of \(H\) costs order-one \(W^-\) energy, but the Noether/Chern--Weil budget supplies only an order-one mean bound, not a vanishing bound.  This is not fatal: the chart contradiction only needs a positive volume proportion of points with uniform reconstruction constants, not semipositivity everywhere.  The reduced-system route should therefore seek:

- a coercive estimate that produces a positive-measure regular/reconstructible set from bounded \(|W^-|^2\) mean and vanishing calibrated \(W^+\) defect;
- or a genuine differential countermodel, not merely a compatible pointwise jet, in which the reconstruction scale tends to zero on most volume while Ricci pinching, \(W^+\) calibration, and curvature-energy budgets are all respected.

A compatible jet does not establish a collapsed sequence; it lacks differential compatibility on a fixed scale, topology, and quantitative control.  Conversely, controlling \(W^-\) tails would not alone complete rank-one collapse because base collapse, fiber homotopy survival, and reconstruction remain separate issues.

## 7. Current route judgment

The smoothing route should now be compared seriously with the normalized reduction route.

- **Smoothing advantage:** it is tied to existing theorems for bounded Ricci curvature and critical \(L^2\) curvature in dimension four; the fixed-small-radius scaling overcomes the nonzero-background objection; it does not assume an exact circle action.
- **Smoothing gaps:** the needed theorem must be localized to buffered good regions; the flow must either transfer geometry back to the original metric or preserve enough near-Einstein/calibrated data; collapsed bounded-curvature structure after smoothing still requires cover/noncollapse/fiber-rank information.
- **Reduction advantage:** it directly exposes the mechanisms (twist, \(W^-\), weighted quotient) that can defeat naive accessibility and gives algebraic identities useful for model tests.
- **Reduction gaps:** exact symmetry is not available for general Ricci-pinched sequences; \(H\ge0\), static closure, and pointwise jets are insufficient; weighted \(RCD(-1,4)\) does not automatically reconstruct a four-dimensional cover.

The next high-value mathematical work is therefore not another exact-profile exclusion.  It is to formulate and test a **localized Li-smoothing accessibility theorem**: from bounded Ricci, bounded local curvature mean on a maximal-function good ball, and small original Einstein/calibrated defects, obtain either a fixed-scale controlled normal-cover chart for the original metrics or a precise obstruction concentrated in the bad localization/flow-transfer set.  In parallel, keep the reduced equations as the language for any obstruction that smoothing exposes.
