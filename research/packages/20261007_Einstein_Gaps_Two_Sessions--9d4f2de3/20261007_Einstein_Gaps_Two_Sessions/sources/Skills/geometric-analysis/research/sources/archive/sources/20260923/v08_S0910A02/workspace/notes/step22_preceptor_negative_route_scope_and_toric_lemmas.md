# Step 22: Preceptor audit of the negative cutoff-flow route, collapse Sobolev input, downstream scope, and reusable toric lemmas

Session S0910A02. Agent4/Preceptor. Phase Execute.

## 0. Scope relative to Yau 26

The active target is still the full statement: for every dimension `n >= 2`, some dimension-only Ricci interval should force the underlying closed smooth manifold to admit an Einstein metric, or else the statement must be strictly refuted.  The sign-normalized organization remains

\[
P_n^\sigma:\quad \|\operatorname{Ric}_g-\sigma g\|_{op}\le \varepsilon_n^\sigma
\Longrightarrow M\text{ admits an Einstein metric},\qquad \sigma=\pm1,
\]

and `Q_n` is equivalent to `P_n^+ or P_n^-`.  This step does **not** prove or disprove any branch.  It audits the current negative four-dimensional cutoff-flow route and records the toric rod identity as a reusable lemma rather than allowing it to disappear as a route verdict.

The main correction to Step 21 is interpretive: the weighted CZ heat calculation should be treated only as a failed attempt to break the weighted estimate, not as evidence for that estimate.  In four dimensions both the critical curvature energy and the schematic estimate `|a Rm| <= C beta/t` are scale invariant, so a Gaussian spike returning an `O(1)` constant is the expected dimensional behavior.  Moreover the Step-11 opposite-fiber warping keeps the determinant `w=pq` fixed and hence is not a genuinely collapsed adversary.  The right adversary is collapse.

## 1. Collapse test: why unweighted downstairs energy and dimension-only Sobolev are false

I wrote and ran

- script: `Sessions/S0910A02/workspace/scripts/step22_collapse_sobolev_and_scope_audit.py`
- data: `Sessions/S0910A02/workspace/data/step22_collapse_sobolev_and_scope_audit.json`

The model is the thin product `S^1_ell x B^3(1)` with fiber-independent test functions `u(theta,x)=f(x)`.  The norm scaling is

\[
\|u\|_{L^4(S^1_\ell\times B^3)}=\ell^{1/4}\|f\|_{L^4(B^3)},
\qquad
\|\nabla u\|_{L^2(S^1_\ell\times B^3)}=\ell^{1/2}\|\nabla f\|_{L^2(B^3)}.
\]

Thus any downstairs four-dimensional Sobolev constant for this family satisfies

\[
A_\ell\gtrsim \ell^{-1/4}.
\]

This is not a subtle unproved point; it is a direct scaling obstruction.  Therefore any proof of the A01/A03 weighted Moser theorem that inserts a dimension-only Sobolev/Poincare/isoperimetric constant on a collapsed downstairs domain is false.  This matches the source situation: Min-Oo explicitly derives the Sobolev constant from lower Ricci and an upper diameter bound, not from collapse-neutral local data (Knowledge `Almost-Einstein...`, lines 157--159), and the Wang/Yang theorem assumes a Sobolev inequality as hypothesis (Knowledge `Pseudolocality...`, lines 725--740).

The same script records the hyperbolic/cusp moral.  In a four-dimensional constant-sectional-curvature model normalized by `Ric=-g`, the sectional curvature is `-1/3`,

\[
|\operatorname{Rm}|^2=2n(n-1)K^2=\frac83,
\qquad E=\operatorname{Ric}+g=0.
\]

If the local collapsed volume is proportional to `ell`, then

\[
\int |\operatorname{Rm}|^2\sim \frac83\ell\to0,
\]

while the Sobolev product does **not** go to zero:

\[
A_\ell^2\|\operatorname{Rm}\|_{L^2}\sim
\ell^{-1/2}\cdot C\ell^{1/2}=O(1).
\]

The data file verifies this numerically from `ell=1` to `1e-8`: unweighted `L^2` energy tends to zero, but `A_lower^2 * ||Rm||_2` remains constant at about `1.63299` in the chosen normalization.  Therefore the right small parameter is not raw downstairs energy; it is the scale-adapted critical product

\[
\gamma_\alpha=A_\alpha^2\|F\|_{L^2(U_\alpha)}
\]

or an equivalent noncollapsed-cover/mean formulation.

## 2. Where noncollapsing enters the A01/A03 route

After reading A03 `step20_weighted_wang_hierarchy_and_whitney_correction.md`, A03 `step21_derivative_free_first_exit_and_plateau_regularity.md`, A01 `step21_finite_exponent_smoothing_lemma.md`, and A01 `route_assessment_step21.md`, the current route can be stated accurately.

### 2.1 What survives the collapse test

The latest A01/A03 formulation does **not** literally use a dimension-only downstairs Sobolev constant.  It keeps a relative Sobolev factor `A` and the critical product `gamma=A^2||F||_2`.  A01's corrected note explicitly warns that metric rescaling made a curvature scaling error and replaces the old Stampacchia step by A03's original-metric weighted moments.  A03's recurrence is also explicitly conditional: equation (11.1), lines 316--323, is assumed before the infinite-product endpoint is proved.

This means the thin-product/cusp probe does **not** refute the corrected weighted formulation.  It does refute any shortcut that says "small unweighted local `L^2` curvature energy on the collapsed base implies pointwise curvature control with dimension-only constants."  Wang's source confirms that the critical threshold has the form `A_0^2 |Rm|_{n/2}` (lines 681--703 and 725--740), exactly the factor that remains constant in the collapsed hyperbolic product model.

### 2.2 The exact noncollapsing/scale hypotheses that must be carried

The remaining theorem must state one of the following, not blur them:

1. **Downstairs relative-Sobolev version.**  For every finite-neighbor component `U_alpha`, there is a relative Sobolev constant `A_alpha` (allowed to degenerate like `Vol(U_alpha)^(-1/4)` in dimension four) and a small product
   \[
   \gamma_\alpha=A_\alpha^2\|F\|_{L^2(U_\alpha)}\le\varepsilon_0.
   \]
   All local energy inequalities, time cutoffs, and neighbor leakage must retain `A_alpha` until the four-dimensional cancellation is used.  No dimension-only downstairs Sobolev constant is available in collapse.

2. **Accessible-cover version.**  Work on a genuine buffered local cover where noncollapse is restored.  Then `chi`, `eta`, the weight `a=chi^2`, and the flow
   \[
   \partial_tg=-2a(\operatorname{Ric}+g)
   \]
   must all be pulled back equivariantly.  Smallness must be transported as a local mean, not as a total integral.  A03 Step 8's cover-mean lemma requires a genuine normal cover of a buffered domain and an interior `3r` cover ball; arbitrary truncated patches do not qualify.

3. **Exponential-pullback endpoint.**  After the zero-order smoothing has produced bounded curvature on a positive-volume plateau, A03's exponential-pullback averaging lemma can choose a noncollapsed chart in the tangent ball without injectivity-radius control.  This is an endpoint selection tool; it does not replace the Sobolev input needed to produce the bounded-curvature plateau.

This is the precise form of the Step-16 domain mismatch: either Sobolev is asserted downstairs and fails under collapse, or it is restored upstairs/on pullbacks and the cutoff/flow/local-mean structure must be carried honestly.

## 3. Downstream deduction if the weighted Moser lemma is granted

The strategist asked for the cheap downstream check before a heavy term-by-term audit.  The result is:

### 3.1 A pure Chern-Weil/Hitchin-Thorpe endpoint would buy nothing

Tight four-dimensional Ricci pinching already implies strict Hitchin--Thorpe for `delta < 1/(1+sqrt(3))`, by the sign-blind Chern-Weil accounting recorded in A02 Steps 4 and 18.  Therefore an argument whose endpoint is merely

\[
2\chi>3|\tau|
\]

or an equivalent sign-blind topological inequality would not advance Yau 26.  It would only reprove an obstruction the pinched input already satisfies.  Similarly Min-Oo cannot be the endpoint: exact large-diameter closed hyperbolic manifolds have `Ric=-g`, `delta=0`, and unbounded diameter-curvature scale while already being Einstein.  The negative branch requires a nonperturbative same-diffeotype Einstein-existence conclusion or a gap for all no-Einstein manifolds, not a Min-Oo-type bounded-diameter stability statement.

### 3.2 The A03/A01 endpoint is stronger but very narrow

The nontrivial downstream part of the A03/A01 route is not ordinary Hitchin--Thorpe.  It uses the critical Ishida--LeBrun/Seiberg--Witten reservoir and the metric-by-metric `7/24` calibration inequality: on the critical four-manifold, small global `L^2` defect `E=Ric+g` forces a calibrated Weyl profile, schematically

\[
\int \left(|W^+|-\frac1{2\sqrt6}\right)^2\le C\int |E|^2.
\]

With a positive-volume bounded-curvature plateau and a chart-selection density, a smooth local limit would be Einstein with calibrated `W^+` spectrum; the Step-6 projector/Derdzinski obstruction then rules out such a germ.  This is a real four-dimensional gauge-theoretic obstruction, not just sign-blind CGB.

But the exact conclusion, even granting all analytic bridges, is only:

- for a **fixed critical Ishida--LeBrun four-manifold**, a gap
  \[
  \inf_g\|\operatorname{Ric}_g+g\|_\infty>0;
  \]
- with additional uniform volume-normalized chart selection and Noether-type topology bounds, possibly a uniform gap across the standard critical subclass.

It does **not** prove unrestricted `P_4^-`, because not every no-Einstein 4-manifold is known to be in this critical Ishida--LeBrun subclass or detected by the same Seiberg--Witten calibration.  It does not prove `P_4^+`.  It does not prove any dimension `n>=5`.  It does not provide the Lean formalization required by the active goal.

### 3.3 Fixed-topology versus varying-topology normalization

A03 Step 21's compactness paragraph phrases one line as `Q(T0)<=2 delta_i^2 Vol ->0`.  That is legitimate only in a fixed-topology setting where the relevant volume is uniformly bounded.  For varying topology with `Vol_i` possibly growing, the right statement must be volume-normalized:

\[
\frac{Q(T_0)}{\operatorname{Vol}(M_i)}\lesssim \delta_i^2\to0.
\]

The exponential-pullback averaging lemma can use this normalized form only if the plateau set has a fixed positive fraction of the total volume.  Thus standard-subclass uniformity needs more than Noether's `chi/A` bound: it also needs a uniform good-set/plateau fraction and the nonnegative calibration density divided by volume.  This repair is plausible in the A03 maximal-function/Vitali architecture, but it must be stated explicitly; absolute `Q->0` is not available in varying topology.

## 4. High-dimensional scope gap

The cutoff-flow route is intrinsically four-dimensional at two load-bearing places:

1. the parabolic Sobolev exponent gives a spacetime `L^3` potential because `2(n+2)/n=3` when `n=4`, and the critical curvature energy is `L^2`;
2. the topological recalibration uses four-dimensional Chern-Weil plus Seiberg--Witten/monopole estimates.

For `n>4`, the critical curvature exponent is `L^{n/2}`, while the current Chern-Weil/Weyl budgets are four-dimensional `L^2` statements.  The existing argument supplies no `L^{n/2}` control and no high-dimensional analogue of the Seiberg--Witten calibration.  A knowledge request in this step found useful already-known desingularization sources (Ozuch; Morteza--Viaclovsky) but did not uncover any broad source-grade reservoir of closed `n>=5` manifolds known to admit no Einstein metric of any sign.  LeBrun's 2025 note in Knowledge shows high-dimensional sign-coexistence and special-holonomy incompatibilities, not a general no-Einstein reservoir.

Consequently, all three sessions are still heavily four-dimensional.  Since the original target is every `n>=2`, A02 should soon devote an Explore step to `n>=5`: either find a genuine high-dimensional obstruction/counterexample reservoir, or develop an all-dimensional proof route.  The only reusable all-dimensional structure currently produced by A02 is the `T^k` determinant trace identity for invariant metrics; it is not a general-to-arbitrary bridge.

## 5. Reusable toric lemmas to preserve

The toric line is paused as a quick proof route, not discarded.  The following lemmas should be reused by later agents.

### Lemma A: diagonal rod identity

For a diagonal twist-free `T^2` metric near a rod, let `Q` be the surviving fiber length along the rod and `K_edge` the base Gaussian curvature restricted to the rod.  The edge equation is

\[
Q''+(1-2K_{edge})Q=0,
\qquad Q(0)=Q(L)=0,
\qquad Q'(0)=1,
\qquad Q'(L)=-1.
\]

Integrating gives

\[
\boxed{\int_{rod}(1-2K_{edge})Q\,ds=2.}
\]

Thus for rod flux `Phi_i=int Q_i ds`,

\[
\boxed{\Phi_i=2+2\int_{rod_i}K_{edge}Q_i\,ds.}
\]

If `K_edge=-A` is constant, then

\[
Q(s)=\frac{\sin(\sqrt{1+2A}\,s)}{\sqrt{1+2A}},
\qquad L=\frac\pi{\sqrt{1+2A}},
\qquad
\Phi_i=\frac{2}{1+2A}=\frac{2L_i^2}{\pi^2}.
\]

With the angle normalization used in A02,

\[
\operatorname{Vol}_4=2\pi^2\sum_i\Phi_i=4\sum_iL_i^2
\]

in the constant-edge-curvature diagonal case.  Step 21 verified this against `S^4`, `CP^2`, and `S^2 x S^2` in `workspace/data/step21_toric_rod_identity_alpha_audit.json`.

### Lemma B: twisted determinant/flux identity

For a general local `T^2`-invariant metric

\[
g=g_B+h_{IJ}(d\phi^I+A^I)(d\phi^J+A^J),
\qquad w=\sqrt{\det h},
\]

Step 12 verified the vertical trace identity

\[
\operatorname{tr}_h\operatorname{Ric}^V
=-\frac{\Delta_B w}{w}+\frac12|F|_h^2.
\]

If the exact positive Einstein equation `Ric=g` holds, then

\[
(-\Delta_B+\tfrac12|F|_h^2)w=2w,
\qquad w|_{\partial\Omega}=0.
\]

Let

\[
\Phi_\partial:=\int_{\partial\Omega}-\partial_\nu w\,ds,
\]

where `nu` is the outward normal and the unit-slope rod normalization identifies the boundary integrand with the surviving fiber length in the diagonal case.  Integrating gives

\[
\boxed{\Phi_\partial+\frac12\int_\Omega |F|_h^2w\,dA_B=2\int_\Omega w\,dA_B.}
\]

Since

\[
\operatorname{Vol}_4=4\pi^2\int_\Omega w\,dA_B,
\]

one obtains

\[
\boxed{\operatorname{Vol}_4=2\pi^2\Phi_\partial+\pi^2\int_\Omega |F|_h^2w\,dA_B.}
\]

Thus twist contributes with a definite sign in the exact determinant identity: for fixed boundary flux it increases volume, while for fixed volume it can reduce boundary flux.  In a merely pinched metric this identity gains error terms from `tr_h Ric^V-2`, so later work must keep the sign and size of the error visible.  The one-dimensional rod ODE Lemma A should not be blindly transferred to twisted or non-diagonal matrix-fiber settings without deriving the corresponding boundary equation.

### Alpha-family as collapsed adversary

The formal alpha-family

\[
A_m=m^\alpha,
\qquad 1<\alpha\le2,
\qquad L_m=\pi/\sqrt{1+2m^\alpha},
\qquad \sum_i\Phi_i\sim m^{1-\alpha}
\]

is more than a paused toric BREAK candidate.  It supplies a library of collapsed, curvature-concentrated geometries that pass scalar rod, corner, Gauss--Bonnet, and Bishop-scale necessary tests.  This is exactly the type of adversary that any collapse-uniform Sobolev/Moser or determinant-volume argument should be tested against.  It remains only formal/local until a smooth global metric is constructed.

## 6. Current resolution-state update

The negative cutoff-flow route remains mathematically interesting but should be described as follows:

- **Valid assets:** four-dimensional critical Sobolev scaling with the product `A^2||F||_2`; the weighted moment algebra; the abstract `q -> 3q/2` endpoint once weak estimate (11.1) is granted; homogeneity of the defect equation; the 7/24 metric-by-metric calibration; exponential-pullback and positive-part chart-selection ideas; source evidence that Wang/Yang require Sobolev and critical-product hypotheses.
- **Material gaps:** derivation of the weak nested time-space estimate (A03 eq. 11.1) with finite-neighbor leakage and evolving measures; maintenance of current-time `gamma_alpha`; explicit scale/noncollapse hypothesis (downstairs relative Sobolev vs accessible cover); volume-normalized chart selection for varying topology; adaptation from `-2a Ric` to `-2a(Ric+g)`; and the fact that the downstream result covers only a special four-dimensional family.
- **No Yau26 closure:** no sign branch in dimension four is solved; no branch in dimensions `n>=5` has a credible mechanism; Lean formalization has not begun.

The next work should not spend a heavy step merely rechecking algebraic exponent products.  Either Agent2/Agent3 should write the actual weak estimate (11.1) with the relative Sobolev constants and cover/mean assumptions explicit, or Agent1 should return to Explore to open the high-dimensional `n>=5` problem and compare all-dimensional mechanisms.  Given the all-dimensional target and the four-dimensional narrowness of the current route, the best next move is an Agent1 Explore reallocation unless A01/A03 specifically ask A02 to verify a finished (11.1) derivation.
