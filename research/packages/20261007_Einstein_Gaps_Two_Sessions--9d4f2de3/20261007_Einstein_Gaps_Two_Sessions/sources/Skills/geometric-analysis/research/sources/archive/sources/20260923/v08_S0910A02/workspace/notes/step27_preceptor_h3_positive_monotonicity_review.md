# Step 27: Preceptor review of the H3 positive-collapse algebra

Session `S0910A02`. Agent4/Preceptor. Phase Explore.

## 0. Target fidelity

The active Yau-26 target is unchanged: prove or strictly refute the all-dimensional
statement that a dimension-only two-sided Ricci interval forces the underlying closed
smooth manifold to admit some Einstein metric, with eventual Lean verification for a
complete final result.  The work reviewed here is **not** such a proof or refutation.
It is a structural positive-branch lemma family for one explicit nonabelian nilpotent
collapse model:

g = dt^2 + a(t)^2(\theta_1^2+\theta_2^2) + c(t)^2\theta_3^2, \qquad [E_1,E_2]=E_3,
\]
with
\[
b=c/a^2,\qquad k_1=a'/a,\qquad k_3=c'/c,\qquad H=2k_1+k_3.
\]
The model is diagonal, cohomogeneity-one, has no horizontal twist \(A\), and has
active shape operator/second fundamental form.  It therefore tests one real
nonabelian-collapse mechanism but does not cover general infranil submersions, toric
fixed strata, non-maximal-rank Ricci-limit strata, or arbitrary positive Ricci
pinching.

The main Step-27 correction to Step 26 is that the relative-rate inequalities are not
merely a warning against pointwise Milnor forcing.  For positive Einstein constant
they imply strict monotonicity of the normalized Heisenberg bracket, exclude bracket
plateaux, and rule out several natural closed diagonal \(H_3\) compactifications.  The
same algebra also explains why the mechanism is sign-asymmetric: it fails in the
negative branch, with the complex-hyperbolic horosphere model as an exact witness.

## 1. Restored Einstein constant and exact algebra

For \(\operatorname{Ric}=\Lambda g\), the verified moving-frame formulas become
\[
\begin{aligned}
\operatorname{Ric}_{00}&=-2(k_1'+k_1^2)-(k_3'+k_3^2),\\
\operatorname{Ric}_{11}=\operatorname{Ric}_{22}&=-\frac{b^2}{2}-k_1'-Hk_1,\\
\operatorname{Ric}_{33}&=+\frac{b^2}{2}-k_3'-Hk_3.
\end{aligned}
\]
Imposing the three vertical equations gives
\[
k_1'=-\Lambda-\frac{b^2}{2}-Hk_1,
\qquad
k_3'=-\Lambda+\frac{b^2}{2}-Hk_3,
\qquad
(\log b)'=k_3-2k_1.
\]
The remaining \(00\)-equation is the constraint
\[
C_\Lambda=b^2+4k_1^2+8k_1k_3+4\Lambda=0,
\]
and the script verifies
\[
C_\Lambda'=-2H C_\Lambda.
\]
Thus the constraint is preserved by the vertical ODE.

Two algebraic identities are the kernel:
\[
2|T|^2-(b^2+4\Lambda)=2(2k_1+k_3)^2-C_\Lambda,
\qquad |T|^2=2k_1^2+k_3^2,
\]
and
\[
4\big((\log b)'\big)^2-5(b^2+4\Lambda)
=4(3k_1+k_3)^2-5C_\Lambda.
\]
Hence on \(C_\Lambda=0\),
\[
|T|^2\ge \frac{b^2+4\Lambda}{2},
\qquad
\big|(\log b)'\big|^2\ge \frac54(b^2+4\Lambda).
\]
These identities are reproduced in
`workspace/scripts/step27_lambda_monotonicity_and_closure_audit.py` and
`workspace/data/step27_lambda_monotonicity_and_closure_audit.json`.

### Pinched version

If the diagonal Ricci components obey \(|\rho_i-\Lambda|\le\delta\) and one uses the
same derivative elimination, then
\[
S:=b^2+4k_1^2+8k_1k_3=2\rho_0-4\rho_1-2\rho_3\le -4\Lambda+8\delta.
\]
Consequently
\[
|T|^2\ge \frac{b^2+4\Lambda-8\delta}{2},
\qquad
\big|(\log b)'\big|^2\ge \frac54(b^2+4\Lambda-8\delta),
\]
whenever the right hand side is meaningful.  In the normalized positive branch
\(\Lambda=1\), every \(\delta<1/2\) still gives a uniform nonzero lower bound for
\(|(\log b)'|\), even when \(b\to0\):
\[
|(\log b)'|\ge\sqrt{5(1-2\delta)}.
\]

This is stronger than Step 26's conservative phrasing and is exactly the content that
Agent4 should preserve for future theorem-building.

## 2. Sign asymmetry and the CH2 witness

For \(\Lambda>0\), the lower bound
\[
\big|(\log b)'\big|^2\ge 5\Lambda
\]
already at \(b=0\) forbids a normalized bracket plateau.  The bracket is strictly
monotone wherever the diagonal model is regular.

For \(\Lambda<0\), the term \(b^2+4\Lambda\) may be negative, so the inequality becomes
vacuous for small or moderate bracket.  The complex-hyperbolic horosphere data
\[
\Lambda=-\frac32,
\qquad b=1,
\qquad k_1=-\frac12,
\qquad k_3=-1,
\]
exactly satisfy
\[
C_\Lambda=0,
\qquad (\log b)'=k_3-2k_1=0,
\qquad k_1'=k_3'=0.
\]
The computed sectional curvatures are
\[
K_{01}=K_{13}=K_{23}=-\frac14,
\qquad K_{03}=K_{12}=-1,
\]
which is the expected complex-hyperbolic curvature range under the chosen
normalization.  This is a useful calibration: stable nonabelian nilpotent horosphere
geometry is natural in the negative branch, while positive Einstein constant destroys
such a bracket plateau through the single term \(4\Lambda\).  This also clarifies why
negative-branch cusps/tubes keep reappearing in the session as obstructions to
Min--Oo-style or smoothing shortcuts.

## 3. Closure consequences that are actually justified

### Theorem A: no positive periodic diagonal H3 model

Let \(b>0\) be a \(C^1\) periodic function arising in this diagonal model and suppose
the diagonal Ricci components are \(\delta\)-pinched around \(\Lambda>0\) with
\(\delta<\Lambda/2\), so that the eliminated algebra above applies.  Then
\(|(\log b)'|\ge\sqrt{5(\Lambda-2\delta)} >0\).  Since \((\log b)'\) is continuous and
never vanishes, it has constant sign; \(\log b\) is strictly monotone, contradicting
periodicity.  Equivalently, a positive periodic \(C^1\) function has a critical point.

This proves there is no closed mapping-torus/orbit-space-circle version of the
positive-pinched diagonal \(H_3\) model.

### Theorem B: standard two-center-bolt diagonal closure is excluded

If the compact interval closes at both endpoints by collapsing the central circle while
\(a\to a_0>0\), then \(b=c/a^2\to0\) at both endpoints.  A positive \(b\) on the open
interval then has an interior maximum, where \((\log b)'=0\), contradicting the same
positive lower bound.  Thus the standard two-center-bolt diagonal closure is also
excluded.

### Large-bracket shell interpretation

For exact \(\Lambda\ge0\), on \(\{b\ge B\}\)
\[
\left|\frac{d}{dt}\frac1b\right|
=\frac{|(\log b)'|}{b}\ge\frac{\sqrt5}{2},
\]
so the portion of a monotone component between \(b=B\) and \(b=\infty\) has thickness at
most \(2/(\sqrt5 B)\).  Also
\[
K_{12}=-\frac{3b^2}{4}-k_1^2,
\]
so \(|\operatorname{Rm}|\ge 3b^2/4\).  Large nonabelian bracket in the positive model is
therefore a thin high-curvature shell, not a persistent collapsed plateau.

This is the precise model-level version of "abelian forcing": persistent, first-scale,
ungraded nonabelian collapse is not compatible with positive pinching in this diagonal
codimension-one setting.

## 4. What would be overclaiming

The strategist suggested an unconditional statement "no closed manifold with
\(\delta\)-pinched positive Ricci carries a diagonal cohomogeneity-one structure with
nonabelian nilpotent principal orbit."  The algebra strongly supports this, but Agent4
should not record it as proved without an endpoint/singular-orbit classification.
The verified closure arguments cover:

1. periodic base/orbit-space circle;
2. interval with central circle collapse at both ends;
3. any compactification that forces a positive interior critical point of \(b\).

They do **not** yet cover every conceivable singular closure of a nilmanifold fibration
over an interval.  A different primitive circle collapse, a lower-dimensional infra-nil
singular stratum, or a non-smooth/edge model could make \(b\to\infty\), \(b\to0\), or
change the regular-coordinate interpretation at an endpoint.  Such models may be
impossible, but that is a separate topological/smoothness theorem.  The honest next
mathematical task is therefore to classify smooth diagonal \(H_3\) cohomogeneity-one
closures or to prove directly that any smooth closed closure gives an interior critical
point of \(b\).

Similarly, the codimension-one model has no horizontal twist.  It does not settle the
general regular infranil-submersion problem, where twist and mean curvature can enter
vertical Ricci with different rank and sign patterns.  Step 26's twist-only rank bound
and the present \(T\)-active monotonicity lemma are complementary tests, not a full
O'Neill-system theorem.

## 5. Machine-checked algebra kernels

Because several previous analytic shortcuts in this session were retracted, this step
also formalized the purely real-algebra kernels in Lean 4.  The file

`workspace/proofs/Step27H3Algebra.lean`

contains theorem statements for:

- the two exact identities;
- the exact \(C_\Lambda=0\) lower bounds;
- the pinched \(8\delta\)-loss lower bounds from component inequalities;
- nonvanishing of the rate in the positive pinched regime \(2\delta<\Lambda\).

The source compiles with `lean_check` and no source axioms/placeholders.  The stricter
`qiushi-yau26 lean` dependency checks succeeded for:

- `Yau26Step27.both_lower_pinched_from_rho_bounds`, current certificate
  `workspace/proofs/step27_h3_algebra_both_check_v2.json` (the earlier
  `step27_h3_algebra_both_check.json` was for the pre-insertion source hash and is
  superseded);
- `Yau26Step27.rate_ne_zero_pinched_from_rho_bounds`, certificate
  `workspace/proofs/step27_h3_algebra_rate_ne_zero_pinched_check.json`.

Both checks report only the standard permitted Mathlib axioms
`propext`, `Classical.choice`, and `Quot.sound`.  This is genuine formal verification
of the algebraic inequalities, not of the Ricci moving-frame derivation or of Yau-26.
The formal file should be treated as a reusable kernel for later proof notes.

## 6. Updated positive-collapse theorem suite

The currently justified positive-collapse suite is now:

1. **Step 6 (4D, constant-length free circle, 3D base):** the Bochner/O'Neill equations
   obstruct exact positive Einstein collapse in that special model.
2. **Step 24 (higher-dimensional KK/product):** constant-length circle collapse over
   higher-dimensional bases exists and is Einstein-compatible; examples
   \((S^3(\sqrt2)/\mathbb Z_q)\times N^d\) show positive collapse cannot be forbidden
   in general.
3. **Step 26/27 (nonabelian H3 diagonal model):** positive Einstein/pinched Ricci
   forbids a persistent nonabelian bracket plateau; large bracket is a monotone thin
   curvature shell, and standard closed diagonal closures are excluded.
4. **Step 25/26 toric correction:** the four-dimensional toric \(\alpha\)-family is not
   killed by the coarse integral identities; any BUILD obstruction must use the mixed
   eigenvalue problem and corner-to-interior cancellation, not the false identity
   \(\int K_Bw=\int w\).

Together these results classify several explicit collapse mechanisms by sign and by
fiber type, but they still do not prove \(P_n^+\).  The missing bridges are (i)
from arbitrary \(C^0\) positive Ricci pinching to a controlled regular collapse model,
(ii) from regular infranil data with twist and singular strata to an iterated abelian
KK/toric description, and (iii) from any such description to Einstein existence on the
same smooth topology.

## 7. Side-branch peer updates

A01 message #311 and A03 message #312 report substantial progress on the conditional
four-dimensional negative cutoff-flow route: corrected transition velocity,
fixed-\(p\) defect energies, a general \(p\ge3\) inequality, Maheux--Saloff-Coste local
Sobolev constants with explicit volume factor, and convergence toward the
Yang/Wang-type endpoint.  These messages do not affect the positive \(H_3\) theorem
review above.  They should be handled by a later negative-branch verification step if
that side route becomes central.  They still describe a conditional special 4D
negative gap program, not the all-dimensional Yau-26 solution.

## 8. Recommended next work

The best next step is constructive rather than another broad review.  Agent2 should
turn the Step-27 model result into a rigorous theorem note with explicit hypotheses and
proofs:

- exact and pinched diagonal \(H_3\) monotonicity theorem;
- periodic and two-center-bolt nonexistence corollaries;
- explicit CH2 negative-sign witness;
- precise statement of what endpoint/singular-orbit classification remains open.

If time permits, Agent2 should begin the endpoint classification for smooth diagonal
\(H_3\) cohomogeneity-one compactifications.  In parallel or in the following step,
Agent3 can extend the moving-frame computation to the simplest twist-active model over
a 2- or 3-dimensional base to test whether twist can create a positive-branch bracket
plateau despite the codimension-one monotonicity.  The general infranil theorem should
not be claimed until that twist computation and endpoint/singular-stratum analysis are
available.
