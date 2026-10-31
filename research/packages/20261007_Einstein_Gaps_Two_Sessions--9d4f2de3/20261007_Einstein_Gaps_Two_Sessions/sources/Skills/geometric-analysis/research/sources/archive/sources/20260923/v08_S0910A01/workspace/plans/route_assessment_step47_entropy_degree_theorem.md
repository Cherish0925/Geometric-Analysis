# Step 47: entropy, degree maps, and negative Ricci pinching near hyperbolic targets

Session: S0910A01. Agent1 / Orchestrator. Phase: Explore.

This note supersedes the unsupported extension in `route_assessment_step45.md`.
The Ishida--LeBrun relation `Vol/A -> 32π²/9` is a calibrated fact of that
near-critical Seiberg--Witten geography, not a universal four-dimensional
curvature-to-volume law.  The mechanism studied here is different: Chern--Gauss--Bonnet plus volume entropy can sometimes turn Ricci near `-g` into a
hyperbolic rigidity conclusion, or into a fixed-target obstruction.  Its
constants currently depend on the hyperbolic target or on a normalized margin;
therefore it does not solve Yau 26.

TTCS verification is saved at
`Sessions/S0910A01/trace/ttcs/results/step47_ttcs01_verifier1_integration.md`.
The corrected algebra script is
`Sessions/S0910A01/workspace/scripts/step47_entropy_degree_comparison.py`.

## 0. Source anchors

- Bessieres--Besson--Courtois--Gallot, `Differentiable rigidity under Ricci
  curvature lower bound`, full text at
  `Knowledge/objects/papers/Differentiable-rigidity-under-Ricci-curvature-lower-bound--cfb4c9cdd3c7--65a5a48bd00c/object.md`, citation key
  `\cite{bessires2012differentiable}`.  Useful lines: 31--33 for BCG volume
  minimality under `Ric >= -(n-1)g`; 43--48 for the diameter-dependent
  differentiable rigidity theorem; 51--55 for the target-size dependence and
  Farrell--Jones explanation; 67--78 for nonzero-degree statements; 80--81 for
  the connected-sum lower-volume gap; 91--102 for entropy/simplicial-volume
  noncollapse; 120--125 and 217--256 for natural maps and almost-injectivity;
  741--748 for the end of the proof and the BCG source reference.

- LeBrun `Weyl curvature, Einstein metrics, and Seiberg-Witten theory`,
  `Knowledge/objects/papers/Weyl-curvature-Einstein-metrics-and-Seiberg-Witten-theory--09b745ed7106--adbf7ae87208/object.md`: lines 29--35 state
  Hitchin--Thorpe and explicitly identify simplicial-volume and entropy as
  distinct Einstein-obstruction mechanisms.

- LeBrun `Four-Manifolds without Einstein Metrics`,
  `Knowledge/objects/papers/Four-Manifolds-without-Einstein-Metrics--5b090e14de27--d63c56d541e8/object.md`: lines 263--270 record the Sambusetti/BCG
  connected-sum examples.  The original Sambusetti paper was found as metadata
  but not acquired in full.

- Di Cerbo `Extended Graph 4-Manifolds, and Einstein Metrics`, acquired at
  `Sessions/S0910A01/staging/acquired/Extended_graph_4-manifolds__and_Einstein_metrics_36ca3f274012faba/content.md`, citation key from retrieval
  `\cite{cerbo2024extended}`: lines 42--52 state the theorem and relation to
  Sambusetti; lines 91--101 give LeBrun's minimal-Ricci-volume strengthening;
  lines 124--138 compute `Vol_Ric`; lines 140--162 prove no Einstein metric for
  closed extended graph 4-manifolds.

- Kasilingam/Farrell--Jones smooth-structure source,
  `Knowledge/objects/papers/Farrell-Jones-spheres-and-inertia-groups-of-complex-projective-spaces--acfe469446a9--8fe24450b510/object.md`, citation key
  `\cite{ramesh2015farrell}`: lines 41--47 and 74--81 give high-dimensional
  complex-hyperbolic exotic smooth structures with sectional curvatures in
  `[-4-eps,-1+eps]`.  This is not yet a near-Ricci-Einstein input family.

## 1. Chern--Gauss--Bonnet comparison under `Ric ≈ -g`

Let `(Y^4,g)` be a closed smooth four-manifold.  The displayed degree theorems
below use orientations; the Euler estimate itself can be read on the oriented
double cover if `Y` is nonorientable.  Assume
\[
  \|g^{-1}(\operatorname{Ric}_g+g)\|_{\infty,\mathrm{op}}\le \delta,
  \qquad 0\le \delta < \delta_0:=\frac{\sqrt3-1}{2}.
\]
Write the Ricci eigenvalues as `-1+e_i`, `|e_i|<=delta`. Then
\[
  s_g=-4+\sum_i e_i,\qquad |s_g|\ge 4(1-\delta),
\]
and
\[
  |\operatorname{Ric}_g^\circ|^2
  =\sum_i\left(e_i-\frac14\sum_j e_j\right)^2
  =\sum_i e_i^2-\frac14\left(\sum_i e_i\right)^2
  \le 4\delta^2.
\]
Hence the scalar and trace-free Ricci part in Chern--Gauss--Bonnet obeys
\[
  \frac{s_g^2}{24}-\frac{|\operatorname{Ric}^\circ_g|^2}{2}
  \ge \frac23(1-\delta)^2-2\delta^2
  =\frac23(1-2\delta-2\delta^2).
\]
With
\[
  8\pi^2\chi(Y)=\int_Y\left(|W|^2+\frac{s^2}{24}
  -\frac{|\operatorname{Ric}^\circ|^2}{2}\right)d\mu,
\]
we obtain
\[
  \operatorname{Vol}_g(Y)
  \le \frac{12\pi^2\chi(Y)}{1-2\delta-2\delta^2}.
\tag{1.1}
\]
Thus, under this negative pinching with `delta<delta0`, the manifold must have
`chi(Y)>0`.  In particular `chi<=0` gives a dimension-four, topology-only
exclusion of sufficiently tight negative Ricci pinching.

Set
\[
  g'=\frac{1+\delta}{3}g.
\]
Constant scaling leaves the Ricci tensor unchanged as a `(0,2)` tensor, and
`Ric_g >= -(1+delta)g`, so
\[
  \operatorname{Ric}_{g'}\ge -3g'.
\tag{1.2}
\]
Moreover the two-sided information becomes
\[
  0\le \operatorname{Ric}_{g'}+3g'
  \le \frac{6\delta}{1+\delta}g'.
\tag{1.3}
\]
In dimension four, volume scales by `((1+delta)/3)^2`, and (1.1) gives
\[
  \operatorname{Vol}_{g'}(Y)
  \le \frac{4\pi^2}{3}\chi(Y)F(\delta),
  \qquad
  F(\delta)=\frac{(1+\delta)^2}{1-2\delta-2\delta^2}.
\tag{1.4}
\]
The expansion is
\[
  F(\delta)=1+4\delta+11\delta^2+O(\delta^3).
\tag{1.5}
\]
For a closed real-hyperbolic four-manifold `(X,g_0)` of sectional curvature
`-1`,
\[
  \operatorname{Vol}_{g_0}(X)=\frac{4\pi^2}{3}\chi(X).
\tag{1.6}
\]
Therefore, for a nonzero-degree map of closed oriented four-manifolds
`f:Y -> X`, `k=deg f`,
\[
  \boxed{
  \frac{\operatorname{Vol}_{g'}(Y)}{|k|\operatorname{Vol}_{g_0}(X)}
  \le
  \frac{\chi(Y)}{|k|\chi(X)}F(\delta).}
\tag{1.7}
\]
For nonorientable variants one would need local-coefficient degree or pass to
appropriate oriented covers; (1.7) is written only in the usual oriented-degree
setting.

## 2. Degree-one hyperbolic existence theorem

Let `(X^4,g_0)` be a closed oriented real-hyperbolic four-manifold of sectional
curvature `-1` and diameter at most `D`.  Let `f:Y -> X` have degree one.  Suppose
`Y` has a metric satisfying the defect bound above and
\[
  \chi(Y)\le \chi(X).
\tag{2.1}
\]
By (1.7),
\[
  \operatorname{Vol}_{g'}(Y)
  \le \frac{\chi(Y)}{\chi(X)}F(\delta)\operatorname{Vol}_{g_0}(X).
\tag{2.2}
\]
BBCG Theorem 1.3 states: for every `n>=3` and `D>0`, there exists
`eps(n,D)>0` such that if `diam(X,g0)<=D`, `f:Y->X` has degree one,
`Ric_q >= -(n-1)q`, and
\[
  \operatorname{Vol}_q(Y)
  \le (1+\varepsilon(n,D))\operatorname{Vol}_{g_0}(X),
\]
then `f` is homotopic to a diffeomorphism.  The tensor inequality in the body of
BBCG is `Ric_q >= -(n-1)q`; the abstract's scalar-looking `-n(n-1)` phrasing is
not the operative hypothesis.

Thus, if
\[
  \frac{\chi(Y)}{\chi(X)}F(\delta)
  \le 1+\varepsilon(4,D),
\tag{2.3}
\]
then `Y` is diffeomorphic to `X`; pulling back `g_0` gives an Einstein metric on
`Y`.  The simpler sufficient condition is `F(delta)<=1+eps(4,D)` together with
(2.1).  If the Euler ratio is strictly smaller and
\[
  \frac{\chi(Y)}{\chi(X)}F(\delta)<1,
\tag{2.4}
\]
then BCG's exact volume lower bound already contradicts (2.2); in this subregime
there is no such pinched input metric.  Equality of the diffeomorphism conclusion
forces `chi(Y)=chi(X)`, so (2.1) is an added topological hypothesis rather than a
consequence of degree one.

This is a real negative-branch existence implication, but it is target-size
dependent because `eps(4,D)` depends on the hyperbolic target diameter.

## 3. Nonzero degree: usable and missing parts

BBCG Theorem 1.5 records the BCG inequality for nonzero degree:
\[
  \operatorname{Vol}_q(Y)
  \ge |\deg f|\operatorname{Vol}_{g_0}(X),
  \qquad \operatorname{Ric}_q\ge-(n-1)q,
\tag{3.1}
\]
with equality exactly when `f` is homotopic to a Riemannian covering of degree
`|deg f|`.  BBCG Theorem 1.6 states a corresponding near-equality differentiable
rigidity result for nonzero degree, but the proof is omitted and referred to
Bessieres' arbitrary-degree treatment.  Consequently:

- the degree-one existence theorem above is directly supported by BBCG Theorem
  1.3;
- the nonzero-degree volume lower bound and equality case are supported by BBCG
  Theorem 1.5/BCG;
- the nonzero-degree near-equality diffeomorphism/covering window should be used
  only after reading the source with its full proof, if a self-contained proof is
  needed.

Assuming BBCG Theorem 1.6 as stated, (1.7) gives the natural extension: if
\[
  \frac{\chi(Y)}{|k|\chi(X)}F(\delta)
  \le 1+\varepsilon(4,D),
\]
then `f` is homotopic to a covering of degree `|k|`, and `Y` carries the pulled
back hyperbolic Einstein metric.  If the left side is `<1`, (3.1) contradicts
(1.7), so no such pinched metric exists.

## 4. Connected sums `X#X`: exact fixed-target obstruction and degenerating margin

For `Y=X#X`, orient the two summands consistently and collapse to a wedge, then
map both summands by degree one.  This gives a degree-two map `f:X#X -> X`.
Since
\[
  \chi(X#X)=2\chi(X)-2,
\]
we have
\[
  \frac{\chi(X#X)}{2\chi(X)}=1-\frac1m,
  \qquad m=\chi(X).
\tag{4.1}
\]
Combining (1.7) with the BCG lower bound gives a contradiction whenever
\[
  \left(1-\frac1m\right)F(\delta)<1.
\tag{4.2}
\]
The endpoint is also impossible for `m>1`: equality in (4.2) forces BCG equality,
so the degree-two map would be homotopic to a twofold Riemannian covering, which
would have `chi(X#X)=2chi(X)` rather than `2chi(X)-2`.

Solving (4.2) gives
\[
  (3m-1)\delta^2+(4m-2)\delta-1=0,
\]
so the positive root is
\[
  \boxed{
  \delta_*(m)=
  \frac{2}{4m-2+\sqrt{16m^2-4m}}
  =\frac1{4m}+\frac5{64m^2}+O(m^{-3}).}
\tag{4.3}
\]
The script `step47_entropy_degree_comparison.py` verifies this formula and the
asymptotic.  Thus `X#X` has a positive negative-pinching gap for every fixed
hyperbolic target, but the elementary gap degenerates along targets with
`chi(X)->infty`.  BBCG Corollary 1.7 gives a stronger fixed-target lower volume
`2(1+eps(X))Vol(X)`, yet BBCG lines 51--55 explain why the near-rigidity
threshold depends on target size.  A uniform connected-sum theorem would require
new information such as
\[
  \inf_X \frac{1+\varepsilon(X)}{1-1/\chi(X)}>1,
\tag{4.4}
\]
not just fixed-target positivity.

The exact Einstein obstruction for `X#X` is nevertheless clean.  Positive
Einstein is excluded by infinite fundamental group and Bonnet--Myers; Ricci-flat
is excluded by the virtually abelian/polynomial-growth structure of compact
Ricci-flat fundamental groups; negative Einstein, scaled to `Ric=-3g`, is
excluded by BCG plus Chern--Gauss--Bonnet:
\[
  \operatorname{Vol}(X#X,g)\ge2\operatorname{Vol}(X),
\]
while the Einstein CGB inequality with `tau=0` gives
\[
  \operatorname{Vol}(X#X,g)
  \le\frac{4\pi^2}{3}\chi(X#X)
  =2\operatorname{Vol}(X)-\frac{8\pi^2}{3}.
\]
These are incompatible.  Therefore `X#X` is a strong four-dimensional no-Einstein
stress family, but it becomes relevant to Yau 26 only if one can either prove a
dimension-uniform negative pinching lower bound for all such connected sums, or
construct metrics on a varying sequence `X_i#X_i` with Ricci defect tending to
zero.  The present CGB+BCG calculation yields only the first fixed-target lower
bound with scale `~1/chi(X)`.

## 5. Normalized margin needed for varying targets

For a family of nonzero-degree maps `f:Y->X` to closed hyperbolic four-manifolds,
define
\[
  q_\chi(f)=\frac{\chi(Y)}{|\deg f|\chi(X)},
  \qquad
  R_{Ric}(f)=\frac{\operatorname{Vol}_{Ric}(Y)}{|\deg f|\operatorname{Vol}(X)}.
\]
BCG gives `R_Ric>=1`, while (1.7) gives `R_Ric <= q_chi F(delta)` for any
near-negative metric.  A dimension-uniform exclusion over a varying class would
follow from a multiplicative margin
\[
  \Gamma:=\inf_f \frac{R_{Ric}(f)}{q_\chi(f)}>1.
\tag{5.1}
\]
Then `F(delta)<Gamma` forbids the pinched metric.  Solving `F(delta)=Gamma`
gives
\[
  \delta_*(\Gamma)=
  \frac{\sqrt{\Gamma(1+3\Gamma)}-(1+\Gamma)}{1+2\Gamma}.
\tag{5.2}
\]
A purely topological sufficient version is: if `q_chi <= 1-alpha` uniformly,
then a gap of order `alpha/4` follows.  `X#X` has `alpha=1/chi(X)`, which is why
its elementary margin vanishes along covers.

This relative margin is the correct object for the entropy/global-volume route.
An absolute volume difference, such as the `24π²` Einstein CGB shortfall in
`X#X`, is not enough when divided by hyperbolic volumes tending to infinity.

## 6. Extended graph four-manifolds: exact obstruction, but ordinary near-equality is too weak

Di Cerbo's extended-graph theorem gives a separate entropy/minimal-volume
mechanism.  For closed extended graph four-manifolds with pure real-hyperbolic
pieces,
\[
  \operatorname{Vol}_{Ric}(M)=\sum_i\operatorname{Vol}_{-1}(V_i),
  \qquad
  2\chi(M)=\frac{3}{2\pi^2}\operatorname{Vol}_{Ric}(M),
  \qquad \tau(M)=0.
\tag{6.1}
\]
LeBrun's negative-Einstein inequality gives
\[
  2\chi(M)-3|\tau(M)|
  \ge \frac{3}{2\pi^2}\operatorname{Vol}_{Ric}(M),
\tag{6.2}
\]
with equality forcing a real-hyperbolic metric when `tau=0`; Di Cerbo then uses
a `Z^3` subgroup and Preissmann's theorem to rule out the real-hyperbolic
possibility.  The positive and zero Einstein signs are handled by fundamental
group and Hitchin equality/growth arguments in the same source.

For almost-negative-Einstein metrics, (1.4) and (6.1) give only
\[
  \operatorname{Vol}_{Ric}(M)
  \le \operatorname{Vol}_{g'}(M)
  \le \operatorname{Vol}_{Ric}(M)F(\delta).
\tag{6.3}
\]
Ordinary near-equality of `Vol_Ric` or entropy is insufficient: the collapsing
higher-graph metrics used to compute `Vol_Ric` already approach the same minimum
without becoming globally real-hyperbolic.  The extra input in a Yau-26 pinching
problem is the two-sided near-Einstein inequality (1.3).  A useful theorem here
would need to use that tensor information, not merely the fact that volume is
near `Vol_Ric`.  For extended graph manifolds without pure pieces, `chi=tau=0`,
and the pointwise CGB lower bound in §1 already rules out sufficiently tight
negative Ricci pinching.

## 7. Farrell--Jones exotic almost-hyperbolic smooth structures

BBCG lines 53--55 recall Farrell--Jones examples `Y=X#Sigma` homeomorphic but
not diffeomorphic to finite covers of real-hyperbolic manifolds, and with
sectional curvature arbitrarily pinched around `-1` as cover degree grows.  If
\[
  -1-\epsilon_i\le K_{g_i}\le -1+\epsilon_i,
\]
then after an elementary scale normalization these are indeed arbitrarily tight
negative Ricci-pinched input metrics.  They would become a direct threat to the
negative half of Yau 26 in that dimension if one could prove the exotic smooth
manifolds carry no Einstein metric of any sign.

Two Einstein signs are topologically excluded for the real-hyperbolic homotopy
examples: positive Einstein would give finite fundamental group by Myers, while
Ricci-flat compact manifolds have virtually abelian/polynomial-growth
fundamental groups.  The difficult sign is negative Einstein.  In dimension four,
a hypothetical exotic smooth manifold homeomorphic to a real-hyperbolic
four-manifold would have `tau=0` and the same `chi`; CGB plus BCG would force a
negative Einstein metric scaled to `Ric=-3g` to have the hyperbolic volume and
hence be hyperbolic, contradicting the exotic smooth structure.  But the
Farrell--Jones real-hyperbolic construction was not acquired directly in this
step, and the accessible complex-hyperbolic Farrell--Jones source lies in real
dimensions 14 and 16 and gives only sectional bounds in `[-4-eps,-1+eps]`, not a
Ricci tensor converging to a scalar multiple of the metric.

Thus the exotic-smoothing route remains one of the highest-value possible
counterexample directions, but the missing theorem is precise:
\[
  M\simeq X\ \text{closed real hyperbolic},\quad
  \operatorname{Ric}_h=-(n-1)h
  \Longrightarrow h\ \text{has constant sectional curvature }-1,
\tag{7.1}
\]
or any substitute volume/entropy upper bound forcing equality in BCG.  The
sources read here do not supply (7.1) in high dimensions.  Conversely, a
quantitative Einstein perturbation theorem from sectional curvature sufficiently
close to `-1` would point toward a positive answer in the negative branch, but it
would require uniform gauge, spectral, injectivity, and nonlinear estimates not
present in the current sources.

A negative near-hyperbolic exotic sequence alone cannot defeat intervals with
nonnegative lower endpoint in the original proposition: by scaling, it would
meet every Ricci interval containing a negative number, but not an interval
entirely in the nonnegative branch.  Full disproof still requires defeating all
possible signs of the dimension-only interval.

## 8. Positive branch after A02 Steps 48--49

A02 corrected the positive noncollapsed route.  The dual Ozuch test-field idea
should be normalized by the two-scale signal size `t_i^2`; an unnormalized
boundary flux vanishes trivially and does not read the curvature coefficient.
For Yau-26 `C^0` operator pinching, only the first Ozuch obstruction is
load-bearing: a nonzero `t lambda o` term becomes `O(1)` after raising an index
with the bubble metric, while second and higher obstruction residuals vanish in
operator norm.  Therefore, once
\[
  R_{\varepsilon}(p)\zeta=0
\]
at each `A_1` insertion, refined Eguchi--Hanson glued approximate metrics have
`||Ric-Lambda g||_op <= C t^{1/2}` even if exact Einstein gluing is later
obstructed.

For the quotient `(S^2 x S^2)/Z_2`, the chiral block is
`diag(Lambda,0,0)`, so kernel directions exist for both chiralities.  Orientation
rows with four `A_1` points have `(b_+,b_-)=(1+r,5-r)`.  The all-one-chirality
endpoints are known-Einstein Del Pezzo-type diffeotypes in the session record;
the mixed rows `r=1,2,3` are concrete smooth-type and Einstein-existence targets.
The balanced row would be topological `3H` if parity and smooth type are proved.
Thus the positive branch is no longer mainly about higher Ozuch obstructions;
it is about the exact smooth manifolds obtained by mixed-chirality desingularizing
product orbifolds and whether those smooth manifolds admit any Einstein metric.

## 9. A03 Step 49 and the restricted IL theorem

A03 reports a normalized cutoff-flow existence and extension module for the
restricted negative Ishida--LeBrun theorem.  The important corrections are:
normalization contributes a positive bounded `(2p-n)∫b|Rm|^p` reaction for
`p>n/2`, not damping; common per-datum time is obtained through curvature-energy
first-exit rather than integrating a `gamma/t` Moser endpoint from `t=0`; and
stationary-collar identities are used only after passing to the exact degenerate
flow.  A03 also corrected the IL theorem's hypotheses to an explicit monopole
sign-family assumption and separated small initial defect from Ricci lower
bounds in Module S.

This is valuable evidence for the intermediate IL result but should be reviewed
independently before A01 treats the regularized analytic module as complete.

## 10. Research consequences

1. The degree-one theorem is a source-backed partial existence result: under a
   degree-one map to a bounded-diameter hyperbolic four-manifold and the Euler
   ratio condition (2.3), tight negative Ricci pinching forces `Y` to be
   diffeomorphic to the hyperbolic target and hence Einstein.  The constant
   depends on `diam(X)`.

2. `X#X` is a clean no-Einstein four-dimensional stress family.  Current
   entropy/CGB methods give a fixed-target negative pinching gap with scale
   `~1/chi(X)`.  A decisive next theorem would show either a uniform positive
   lower bound for the negative Ricci defect over `X_i#X_i`, or construct a
   sequence with defect tending to zero.

3. Entropy/minimal-volume mechanisms are global-volume mechanisms, not local
   Weyl-profile mechanisms.  They should not be forced into the IL local
   calibration template unless a separate local obstruction density is found.

4. Farrell--Jones real-hyperbolic exotic smoothings remain a major possible
   counterexample route.  The decisive missing input is high-dimensional negative
   Einstein smooth rigidity for real-hyperbolic homotopy types, or direct
   no-negative-Einstein evidence for the exotic members.

5. The positive branch now has a concrete operator-norm gluing wall: mixed
   product-quotient desingularizations can produce near-positive-Einstein input
   metrics once first obstructions vanish.  Their value for Yau 26 depends on
   smooth-type computation and Einstein-existence knowledge for the mixed rows.

6. The restricted IL negative theorem remains a strong intermediate result, and
   A03's Step 49 may close its flow-existence module, but A01 should still verify
   the analytic construction rather than inherit agreement from peer notes.
