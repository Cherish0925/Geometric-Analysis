# Step 18: weighted cutoff-flow system and the remaining degenerate smoothing problem

Session: S0910A01. Agent3/Actuator. Phase: Execute.

## 1. Purpose

This note records the execution work that followed the Step 17 handoff and the
new Strategist correction.  The aim is to remove the last residual wording that
treated a plateau Li bootstrap as already proved, and to replace it by the
actual analytical object: a full-support coupled estimate for

\[
  \partial_t g=-2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}+g .
\]

The important separation is:

- weighted curvature, such as `a Rm`, is the natural object for transition
  smoothing and continuation;
- weighted defect, such as `aE`, controls the metric speed;
- unweighted defect energy `Q(t)=\int |E(t)|^2` is required for the LeBrun
  topological recalibration.

These estimates interact, but none of the three can be silently substituted for
another.

## 2. Correction to the Step 17 plateau section

The radius repair in Step 17 is useful but limited.  With a plateau
`B_{4r_*}(p)` and bootstrap center `x in B_{r_*}(p)`, the covering balls
appearing in Li's argument lie inside the plateau.  This only fixes the
geometric containment.  Li's proof controls a supremum over centers.  If the
supremum is taken over centers in `B_{2r_*}(p)`, then the evolution estimate
written only for centers in `B_{r_*}(p)` does not control the derivative of the
same supremum.  Enlarging the plateau does not by itself close this inequality.

I patched `workspace/notes/step17_support_scale_li_bootstrap.md` and
`workspace/plans/route_assessment_step17.md` so later agents inherit this
corrected status.  The downstream Derdzinski chain is now explicitly conditional
on a genuine full-support continuation theorem producing bounded-curvature
plateaux and unweighted `Q(t_0)/A_i -> 0`.

## 3. Weighted scalar algebra for `f=aK`

Let `K=|Rm|` and suppose, schematically,

\[
  \partial_t K\le a\Delta K+c aK^2+T,
\]

where `T` denotes the cutoff-derivative and coupled-defect terms.  Since `a` is
time-independent and `f=aK`, direct product-rule calculation gives

\[
\boxed{
  \partial_t f\le a\Delta f-2\langle\nabla a,\nabla f\rangle
    +\left(\frac{2|\nabla a|^2}{a}-\Delta a\right)f
    +c f^2+aT .
}
\tag{3.1}
\]

Thus the quadratic reaction is `c f^2`, not `c f^2/a`.  For `a=chi^2`,

\[
  \frac{|\nabla a|^2}{a}=4|\nabla\chi|^2,
\]

so the artificial inverse-cutoff singularity is absent.  This is a real
improvement in the formulation, but the principal operator remains degenerate.
The transition problem is not solved by this algebra.

Execution evidence: `workspace/scripts/step18_weighted_cutoff_algebra.py` checks
(3.1), the reaction term, and the integrated one-dimensional principal energy
identity.  The run output was:

- scalar weighted identity residual `0`;
- reaction `a^2 cK^2 = c f^2`;
- `|grad(chi^2)|^2/chi^2 = 4|grad chi|^2`;
- after integrating the principal energy by parts, no second derivative of `a`
  remains in the displayed principal density.

The one-dimensional energy identity after integrating the `Delta a` term by
parts has the schematic form

\[
\begin{aligned}
\frac d{dt}\int \eta^2 f^2 + c\int \eta^2 a|\nabla f|^2
  \le{}& C\int (a|\nabla\eta|^2+\eta^2 |\nabla\chi|^2) f^2\\
       &+C\int \eta^2 f^3+C\int \eta^2 f\,aT .
\end{aligned}
\tag{3.2}
\]

Formula (3.2) indicates the correct variables.  It also exposes the hard point:
the dissipation is weighted by `a`, so the usual Moser iteration must be adapted
to a degenerate operator and to the terms in `T`.

## 4. Coupled defect energy and unweighted `Q`

A03's tensor calculation gives

\[
  \partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E),
\]

with all terms homogeneous in `E` and its first derivatives.  After testing by
`eta E`, integrating by parts, and using the contracted Bianchi identity, the
useful inequality is

\[
\begin{aligned}
 \frac d{dt}\int\eta^2|E|^2+c\int\eta^2a|\nabla E|^2
 \le{}& C\int(a|d\eta|^2+\eta^2|d\chi|^2+
          \eta^2a)|E|^2\\
      &+C\int\eta^2a|\operatorname{Rm}|\,|E|^2 .
\end{aligned}
\tag{4.1}
\]

The reaction should be estimated through `chi E`:

\[
\begin{aligned}
 \int a|\operatorname{Rm}|\,|E|^2
   &=\int |\operatorname{Rm}|\,|\chi E|^2\\
   &\le \|\operatorname{Rm}\|_2\|\chi E\|_4^2\\
   &\le A_U\|\operatorname{Rm}\|_2
      \int |\nabla(\chi E)|^2 .
\end{aligned}
\tag{4.2}
\]

In dimension four, if `U` is a support at scale `r` and
`fint_U |Rm|^2 <= K_0`, then

\[
  A_U\sim \frac{r^2}{\operatorname{Vol}(U)^{1/2}},\qquad
  \|\operatorname{Rm}\|_{L^2(U)}\le (K_0\operatorname{Vol}(U))^{1/2},
\]

hence

\[
  A_U\|\operatorname{Rm}\|_{L^2(U)}\le C\sqrt{K_0}\,r^2 .
\tag{4.3}
\]

The collapsed volume cancels.  `workspace/scripts/step17_sobolev_energy_cancellation.py`
was overwritten so it now records only this scale fact and no longer turns it
into a completed flow estimate.  Its corrected run showed the product
`sqrt(K0) r_*^2 = 1.264911e-03` unchanged over volumes from `1` to `1e-24`.

A second script, `workspace/scripts/step18_energy_absorption_terms.py`, checks
the normalized powers in the coupled local system:

\[
  R_\alpha'=O(r^{-2}\sum_{\beta\sim\alpha}(R_\beta+P_\beta))+
      \text{absorbable terms},
\qquad
  P_\alpha'=O(r^{-2}\sum_{\beta\sim\alpha}P_\beta)+
      \text{absorbable terms}.
\]

The run verified

\[
  A_U\|K\|_2=\sqrt{K_0}r^2,
\]

and the normalized cutoff-gradient remainders scale as `r^{-2}`.

The unweighted `Q(t)=\int|E|^2` remains essential.  A bound on `aE` gives metric
speed, but gives no unweighted information where `a` is small.  The energy
estimate must therefore prove a support-summed or global growth bound for
`Q(t)` directly from (4.1), rather than deriving it from a weighted pointwise
estimate.

## 5. Status after A03 Step 17

A03's new message and note sharpen the state of the analytical bridge.  The
coupled `L^2` layer appears to close at the level of normalized local energies:

\[
\begin{aligned}
 \dot R_\alpha+cX_\alpha
    &\le Cr^{-2}\sum_{\beta\sim\alpha}(R_\beta+P_\beta)+\varepsilon_1Y_\alpha,\\
 \dot P_\alpha+cY_\alpha
    &\le Cr^{-2}\sum_{\beta\sim\alpha}P_\beta,
\end{aligned}
\]

and therefore, for `H_alpha=R_alpha+kappa P_alpha`,

\[
  \dot H_\alpha+c'(X_\alpha+Y_\alpha)
      \le Cr^{-2}\sum_{\beta\sim\alpha}H_\beta .
\]

This is consistent with the Step 18 scaling checks and with the A03 script
`verify_L2_sobolev_absorption.py`, which I ran.  The useful conclusion is
curvature-energy persistence, not transition pointwise smoothing.

A03 also corrected the defect maximum-principle scope: the cubic defect term
cancels in the squared-norm evolution, but a maximum-principle estimate driven
by `|a Rm|<=C/t` is not by itself uniformly useful from time zero, because
`int_0^T dt/t` diverges.  The metric-speed estimate should instead come from a
fixed supercritical, time-integrable bound for `aE`, while the unweighted
`Q(t)` estimate should come from the energy inequality.  Weighted curvature
regularity remains the missing transition input.

## 6. The remaining degenerate epsilon-regularity problem

The hard estimate is now sharply isolated:

> From small normalized local critical energy `R_alpha(t) <= epsilon` under the
> cutoff-flow curvature equation with degenerate operator `partial_t-aDelta`,
> prove a weighted pointwise estimate
> \[
>   |a\operatorname{Rm}(x,t)|\le C/t
> \]
> on the active support for `0<t<=theta r^2`, with constants independent of
> collapsed volume.

On the plateau `a=1`, this is Li's theorem after the full-support continuation
has supplied the relevant all-center energy and Sobolev persistence.  On the
transition `0<a<1`, Li's proof does not directly apply.  Formula (3.1) shows
why the problem is better than feared: the reaction is `f^2`, not `f^2/a`.
But the diffusion is degenerate, and the real tensor equation contains the
cutoff-gradient and `E`-coupling terms.

## 7. Model computations for the degenerate transition

I ran two toy computations to test whether the weighted target is compatible
with basic degenerate diffusion.

### 7.1 Constant-diffusivity model

If `a` is locally constant, heat smoothing from `L^{n/2}` to `L^infty` gives

\[
  \|K(t)\|_\infty\lesssim (at)^{-1}\|K(0)\|_{L^{n/2}},
\]

hence

\[
  \|aK(t)\|_\infty\lesssim t^{-1}\|K(0)\|_{L^{n/2}},
\]

independent of `a`.  `workspace/scripts/step18_constant_diffusivity_weight_scaling.py`
checks this for dimensions `3,4,5,6,8`; for every tested `a` from `1` to
`1e-6`, the weighted factor was `1/t`.

### 7.2 Normal cutoff model `a=x^2`

Near a regular cutoff boundary, the linear model `K_t=x^2 K_xx` becomes, under
`y=log x`,

\[
  u_t=u_{yy}-u_y,
and the weighted output is `x^2K=e^{2y}u`.  TTCS noticed that my first script
used the opposite drift sign in the heat kernel.  I corrected
`workspace/scripts/step18_degenerate_model_heat_kernel.py` and reran it.  With
the corrected kernel, the weighted operator norm still stayed bounded in the
tested window and behaved like a mild power near small time; `C(t)t^{1/4}` lay
around `0.36--0.42` for `t=1e-4` to `1e-1` and remained finite at later tested
times.  Normalized Gaussian spikes placed closer and closer to the cutoff
boundary produced smaller weighted outputs, not larger ones.
Gaussian spikes placed closer and closer to the cutoff boundary produced
smaller weighted outputs, not larger ones.

This model supports the plausibility of a weighted epsilon-regularity theorem,
but it is not a proof.  The geometric transition has tangential variables,
nonlinear curvature reaction, tensor cutoff terms, and the coupled defect
system.

## 8. Cutoff construction and Hessian terms

The proposed theorem should avoid assuming pointwise `|nabla^2 chi|<=C/r^2`
whenever possible.  Bounded Ricci alone gives distance cutoffs with controlled
gradient after smoothing/regularization, but not uniform pointwise Hessian at
the strength used in formal tensor estimates.  The defect energy already
cancels Hessian terms after integration by parts.  The curvature energy should
be handled similarly: terms of the schematic form

\[
  \nabla^2a*E*\operatorname{Rm}
\]

should be integrated by parts into terms involving `nabla a`, `nabla E`,
`nabla Rm`, and localization gradients, then absorbed through the coupled
`X_alpha,Y_alpha` dissipations and `r^{-2}(R_alpha+P_alpha)` remainders.  If a
pointwise Hessian bound remains necessary, constructing such cutoffs under the
actual sequence hypotheses becomes part of the smoothing theorem.

## 9. Dimension-general scaling and four-dimensional input

The collapse cancellation is not intrinsically four-dimensional.  In dimension
`n`, the relative Sobolev coefficient scales like

\[
  A_U\sim r^2/\operatorname{Vol}(U)^{2/n},
\]

and the critical curvature norm under `fint_U |Rm|^{n/2}<=K_0` is

\[
  \|Rm\|_{L^{n/2}(U)}=(K_0\operatorname{Vol}(U))^{2/n}.
\]

Thus

\[
  A_U\|Rm\|_{L^{n/2}(U)}\sim K_0^{2/n}r^2,
\]

with volume cancellation in every dimension at the critical exponent.  The
script `workspace/scripts/step18_sobolev_scaling.py` verifies this numerically
for volumes down to `1e-24`.  What is special to the current LeBrun route is
not this scaling, but the four-dimensional supply of an `L^2` curvature budget
from Chern-Weil/Noether and the calibrated `W^+` obstruction.  Higher
dimensions would need an independent `L^{n/2}` input and a replacement for the
Seiberg-Witten/Derdzinski mechanism.

## 10. Relation to peer work

A02's Step 18 correction is important for the positive branch.  Hitchin-Thorpe
violators such as `#_5 CP^2` are not examples against tight positive pinching,
because tight four-dimensional pinching itself forces strict Hitchin-Thorpe by
the earlier Chern-Weil lemma.  The positive branch should instead look at
strict-Hitchin-Thorpe positive-Ricci families such as `#_k(S^2 x S^2)` and
possibly `#_3 CP^2`, with A02's toric crux providing a direct ansatz laboratory.
This is independent of the negative LeBrun smoothing bridge.

For the negative route, A03's Step 17 work supports the `L^2` layer and leaves
the same remaining object: degenerate epsilon-regularity from the coupled
energy persistence to `|a Rm|<=C/t`.

## 11. Current theorem target after Step 18

A transferable smoothing theorem worth proving is:

Let `(M^n,g_0)` have bounded Ricci and local critical curvature energy
`r^n average_U |Rm|^{n/2}` small on a controlled support.  For the normalized
cutoff flow `partial_t g=-2chi^2(Ric+g)`, prove short-time existence and a
full-support estimate which, in dimension four, specializes to:

1. coupled normalized `L^2` curvature/defect energy persistence;
2. weighted pointwise curvature `|chi^2 Rm|<=C/t` from that energy;
3. weighted pointwise defect `|chi^2 E|` sufficient for metric comparability;
4. unweighted support-summed `Q(t)<=C Q(0)`.

Item 2 is the remaining unproved mathematical core.  Items 1 and 4 are now much
better supported by the coupled `L^2` system, while item 3 follows once item 2
is available through the corrected defect maximum principle and parabolic
estimates.

## 12. Refinements after TTCS and A03 Step 18

TTCS independently checked this note and A03 then supplied a more precise
fixed-`p` defect calculation.  The following refinements supersede the looser
phrasing above.

### 12.1 Coupled `L^2` layer as a first-exit lemma

The coupled local `L^2` system should be treated as a lemma inside a
simultaneous first-exit argument, not as a standalone theorem.  Its derivation
uses provisional metric comparability, along-flow Sobolev constants, finite
neighbor overlap, local energy smallness, and cutoff control.  Within such an
interval, the Sobolev-energy cancellation supports an improvement of the
curvature/defect energy thresholds.  What remains to be written is the complete
tensor derivation of all `nabla^2 a` contractions and their integration by parts.

The initial maximal-function radius must control the whole active support if
the full-support theorem uses all centers there.  If the support is
`B_{5r_*}(p)`, a centered maximal-function bound at `p` must be taken at least
up to `6r_*`, since `y in B_{5r_*}(p)` implies `B_{r_*}(y) subset B_{6r_*}(p)`.
The earlier `4r_*` radius is enough for the inner plateau geometry but not for
full support.

### 12.2 Fixed-supercritical weighted defect propagation

Set

\[
  U=aE,\qquad w=|U|.
\]

A03's tensor calculation gives, after cancellation of the commutator terms,

\[
  \partial_t U=a(\Delta_LU-2U)+\mathcal B_a(U),
\]

where the apparent quotients in `B_a` are regular for `a=chi^2` because
`da\otimes da/a=4d\chi\otimes d\chi`.  Testing before scalarizing gives, for
one fixed `p>2`,

\[
\begin{aligned}
 \frac d{dt}\int\eta^2 w^p+c_p\int\eta^2a|\nabla w^{p/2}|^2
 \le{}& C_p\int\left(a|d\eta|^2+
     \eta^2\frac{|da|^2}{a}\right)w^p\\
 &+C_p\int\eta^2a|\operatorname{Rm}|w^p
  +C_p\int\eta^2w^{p+1} .
\end{aligned}
\tag{12.1}
\]

The reactions in (12.1) can be absorbed for one fixed `p` using the same
relative Sobolev and small critical-energy cancellation; the coefficient grows
like `p sqrt(epsilon)`, so this cannot be iterated all the way to `p=infinity`
with a fixed threshold.  The A03 script
`Sessions/S0910A03/workspace/scripts/verify_step18_weighted_defect_exponents.py`
checks the volume cancellation, the endpoint `p=2` logarithmic divergence, and
this high-exponent obstruction; I ran it successfully.

The expected pointwise metric-speed estimate therefore needs a second stage
with curvature as a time-dependent potential.  A sufficient form is a weighted
supercritical curvature-potential estimate, for example

\[
  A_U^4\int_{\widetilde U} a|\operatorname{Rm}|^3\le C/t,
\]

which would allow a Li-type iteration from the fixed `L^p` bound to

\[
  |aE(x,t)|\le C_p\delta\left(\frac{r^2}{t}\right)^{2/p},
  \\qquad p>2.
\]

This estimate is integrable in time exactly when `p>2`, and it would provide
metric comparability without relying on the nonintegrable `C/t` coefficient in
the defect maximum principle.

### 12.3 Topology-uniformity correction

The earlier shorthand that BMY bounds `chi/A` above was wrong: BMY gives the
opposite direction for `c_2/c_1^2`.  The useful upper bound in the standard
Ishida-LeBrun minimal-general-type subclass comes from Noether plus the
connected-sum arithmetic.  A03's calculation gives, for `m=2,3` and standard
`b_+(N)=0` input at the critical relation `D=A/3`,

\[
  \chi(M)/A\le 65/6
\]

(with `28/3` for `m=3`).  Arbitrary symplectic summands or broader variants
need their own explicit upper bound before one can assert uniform constants.

### 12.4 Refined current target

The most precise current target is a simultaneous theorem that proves, on a
first-exit interval:

1. complete tensor local-energy inequalities using only first cutoff
derivatives after integration by parts;
2. short-time persistence of local critical curvature/defect energies;
3. weighted curvature-potential regularity strong enough to imply either
`|a Rm|<=C/t` or `A_U^4 int a|Rm|^3<=C/t`;
4. fixed-supercritical weighted defect propagation and the integrable
`|aE|` estimate;
5. unweighted support-summed/global defect control `Q(t)<=C Q(0)`.

This is now the actual mathematical bridge between the LeBrun near-equality
obstruction and the Derdzinski local contradiction.

## 13. Whitney-scale route for the remaining weighted curvature estimate

I added `workspace/scripts/step18_whitney_scaling.py` to test the natural local
rescaling near a regular cutoff boundary.  If `|nabla chi|<=L/r` and
`chi(x_0)=chi_0>0`, use a Whitney ball of radius

\[
  \ell=c r\chi_0 .
\]

For `c` small enough, `chi/chi_0` and `a/a(x_0)` stay uniformly comparable on
that ball.  After rescaling space by `ell` and time by `r^2`, the dimensionless
principal coefficient, drift coefficient, and potential coefficient in the
weighted scalar operator are bounded independently of `chi_0`:

\[
  a/a(x_0)=O(1),\qquad
  r^2|\nabla a|/\ell=O(1),\qquad
  r^2|\nabla a|^2/a=O(1).
\]

The script output showed, for example with `L=2` and `c=0.1`,
`a/a0 in [0.640,1.440]`, drift coefficient at most `40`, and potential
coefficient at most `16`, all independent of the cutoff level.  Diffusion
length containment requires `sqrt(theta)<=c/2`; for `c=0.1`, this allows
`theta=1e-3`.

This gives a concrete next mathematical route: cover the transition by Whitney
balls adapted to the level of `chi`, prove a finite-neighbor parabolic Moser or
mean-value estimate for `aRm` on these intrinsic scales, and couple it with the
fixed-scale support energy and the `U=aE` estimates.  The computation does not
handle the tensor nonlinearities or the collapsed Sobolev constants by itself,
but it removes the fear that the degeneracy alone forces nonuniform coefficients
as `chi_0 -> 0`.
