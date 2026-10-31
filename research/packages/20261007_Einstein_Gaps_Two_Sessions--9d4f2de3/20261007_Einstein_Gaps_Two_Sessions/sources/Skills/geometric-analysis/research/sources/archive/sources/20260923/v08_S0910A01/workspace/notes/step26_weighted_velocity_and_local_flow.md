# Step 26: support-wide weighted velocity and local-flow continuation

Session: S0910A01. Agent3 / Actuator. Phase: Execute.

## 1. Correction to the Step 25 first-exit reduction

The buffered support tensor calculation from Steps 24--25 remains useful, and
Codex independently rederived the same three slice-wise energy inequalities in
`workspace/codex_loop/work/tensor_energy_derivation.md`.  The Step 25
first-exit note nevertheless made one invalid simplification: it used plateau
regularity to replace stability on the transition.

The terminal Derdzinski contradiction only needs bounded curvature on plateau
balls where `a=chi^2=1`.  The flow estimates, however, use a current-time
Sobolev constant, current-time cutoff-gradient bounds, and the current critical
product

\[
  \beta_a(t)=A(t)^2\|F(t)\|_{L^2(\operatorname{supp}\chi,g(t))}.
\]

These quantities persist under a bilipschitz comparison between `g(t)` and
`g(0)` on the whole active support, including the transition.  The correct
metric displacement identity is

\[
  e^{-2V(t)}g_0\le g(t)\le e^{2V(t)}g_0,
  \qquad
  V(t)=\int_0^t\|aE(s)\|_{L^\infty(\operatorname{supp}\chi)}\,ds .
\tag{1.1}
\]

At a transition point the displacement is controlled by `a(x)|E(x,t)|`, not by
`a(x)` alone.  If `|E|` grows like `a^{-1}` near the transition, the small
coefficient can disappear.  Thus the support-wide target is

\[
  \boxed{\int_0^{\theta r^2}\|aE(t)\|_{L^\infty(\operatorname{supp}\chi)}dt
  \le \varepsilon_{\rm met}.}
\tag{1.2}
\]

This does not require unweighted transition curvature or transition curvature
closeness to the initial metric.  It requires the weighted defect estimate that
the earlier support-local formulation separated from plateau curvature.

## 2. Fixed-p defect energy: the correct transition-sensitive quantity

For a fixed exponent `p>2`, define

\[
  J_p(t)=\int \eta^2 a^{p-2}|E|^p\,d\mu_t,
\]

and

\[
  Z_p(t)=\int \eta^2 a^{p-1}|E|^{p-2}|\nabla E|^2\,d\mu_t,
  \qquad
  z_p=\eta a^{(p-1)/2}|E|^{p/2}.
\]

The power `a^{p-2}` is essential.  It keeps the initial datum controlled by the
global Ricci pinching while retaining two powers of `a` beyond the velocity:

\[
  |aE|^p = a^p|E|^p = a^2\,a^{p-2}|E|^p\le a^{p-2}|E|^p.
\tag{2.1}
\]

Since the initial pinching gives `|E(0)|<=C delta` everywhere,

\[
  J_p(0)\le C\delta^p\operatorname{Vol}(\Omega_\eta,g_0).
\tag{2.2}
\]

No initial high-power curvature bound is used.

Testing the exact defect equation

\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E)
\]

against `eta^2 a^{p-2}|E|^{p-2}E` gives the fixed-p analogue of the Step 25
`Q` inequality:

\[
\boxed{
  J_p' + c_p Z_p
  \le C_p r^{-2}J_p + C_p\int \eta^2 a^{p-1}F|E|^p .}
\tag{2.3}
\]

The weights in (2.3) are forced as follows.

* The principal term has coefficient `a` from the equation and testing weight
  `a^{p-2}`, hence the dissipation weight is `a^{p-1}`.
* After integrating Hessian-a terms once, the worst transition term has density
  `a^{p-3}|da|^2|E|^p`.  Because `a=chi^2`,

  \[
  a^{p-3}|da|^2|E|^p
  =4|d\chi|^2a^{p-2}|E|^p
  \le Cr^{-2}a^{p-2}|E|^p .
  \tag{2.4}
  \]

* The curvature reaction is homogeneous in `E` and has the exact form

  \[
  \int\eta^2 a^{p-1}F|E|^p=\int F z_p^2 .
  \tag{2.5}
  \]

The Sobolev absorption uses the same critical product as the curvature energy:

\[
\int Fz_p^2\le \|F\|_{L^2(\operatorname{supp}\chi)}\|z_p\|_4^2 .
\tag{2.6}
\]

The gradient of `z_p` satisfies

\[
\begin{aligned}
 \|\nabla z_p\|_2^2
 &\le C_p\int\eta^2a^{p-1}|E|^{p-2}|\nabla E|^2
      +C_pr^{-2}\int\eta^2a^{p-2}|E|^p \\
 &= C_p Z_p+C_pr^{-2}J_p .
\end{aligned}
\tag{2.7}
\]

Here the `d eta` term vanishes because `supp d eta` lies in the stationary
collar where `a=0`, hence `z_p=0`.  Therefore a current Sobolev inequality gives

\[
  \int\eta^2 a^{p-1}F|E|^p
  \le C_p\beta_a(t)\bigl(Z_p+r^{-2}J_p\bigr).
\tag{2.8}
\]

For one fixed p, choose the physical scale r so that the first-exit bound on
`beta_a` makes `C_p beta_a<c_p/2`.  Then

\[
  \boxed{J_p'(t)\le C_pr^{-2}J_p(t),\qquad
  J_p(t)\le e^{C_p\theta}J_p(0).}
\tag{2.9}
\]

This is the first transition-sensitive defect result needed for support-wide
metric stability.  The script
`workspace/scripts/step26_fixed_p_defect_velocity.py` checks the powers
(2.1)--(2.8) and the resulting scaling.

A useful concrete choice is `p=6`, because then the expected heat exponent is
`2/p=1/3`, matching earlier plateau estimates while keeping constants finite.
It also avoids smoothness ambiguity in the cutoff power: `a^4=chi^8` is smooth.
The tensor norm factor `|E|^3` is treated in the usual weak/Kato way by replacing
it with `(|E|^2+eps)^{3/2}` and passing to the limit, so no proof should rely on
`|E|^3` being smooth at `E=0`.  Nothing in (2.3)--(2.9) requires a hierarchy of
all exponents.

## 3. From fixed p to the weighted velocity bound: what remains

The fixed-p estimate itself gives only an `L^p` bound for the weighted velocity:

\[
  \|aE(t)\|_{L^p}\le J_p(t)^{1/p}\le C_p\delta\operatorname{Vol}(\Omega_\eta)^{1/p}.
\tag{3.1}
\]

To improve this to the support-wide pointwise bound needed in (1.2), one still
needs a positive-time Moser or mean-value argument for the weighted defect
variable.  The algebra predicts the following scale in dimension four:

\[
  \boxed{
  \|aE(t)\|_{L^\infty(\operatorname{supp}\chi)}
  \le C_p\delta\left({r^2\over t}\right)^{2/p},
  \qquad 0<t\le\theta r^2 .}
\tag{3.2}
\]

Indeed, the relative Sobolev coefficient has the collapse-cancelling form
`A^2 ~ r^2 Vol^{-1/2}`.  A parabolic `L^p`-to-`L^infty` estimate in four
space dimensions would contribute `A^{4/p}t^{-2/p}`; multiplying by
`J_p(0)^{1/p}~delta Vol^{1/p}` cancels the volume and yields (3.2).  The script
verifies this exact cancellation.  For `p=6`, (3.2) is

\[
  \|aE(t)\|_\infty\le C\delta r^{2/3}t^{-1/3}
  =C\delta\left({r^2\over t}\right)^{1/3}.
\tag{3.3}
\]

This is exactly aligned with Yang's local heat-flow Moser theorem in Appendix B
of `Convergence of Riemannian manifolds with integral bounds on curvature I`:
lines 1127--1136 state that, under a current Sobolev inequality, metric
comparison, and a potential condition
`(int chi^{q-n} u^{q/2})^{2/q}<=mu`, the output is `|chi^2 f|` controlled by
the spacetime input `int chi^{2p0-n} f^{p0}`.  Taking `n=4`, `p0=6`, and
`f=|E|` gives the input weight `chi^8=a^4`, exactly `J_6`; taking the potential
`u=F` and `q=6` gives the curvature input `(int chi^2 F^3)^{1/3}`, exactly the
positive-time weighted `Y` bound from the q=3 curvature layer.  Thus (3.3) is a
Yang-type weighted Moser target, not merely dimensional bookkeeping.

This is integrable at zero:

\[
  \int_0^{\theta r^2}\|aE(t)\|_\infty dt
  \le {p\over p-2}C_p\delta\,r^2\theta^{1-2/p}.
\tag{3.4}
\]

Hence a proof of (3.2) would self-improve the metric comparison, Sobolev
persistence, cutoff-gradient bounds, and beta persistence on the entire active
support.  This is the correct replacement for the Step 25 plateau-only drift
argument.

The open analytic point is not the exponent arithmetic.  It is to prove the
weighted Moser step for the degenerate support equation without assuming
unweighted transition curvature.  Two possible routes remain:

1. derive a finite hierarchy for weighted defect exponents starting from the
   fixed `J_p` estimate, with variables
   `a^{(q-1)/2}|E|^{q/2}` and constants controlled for a finite jump to
   pointwise control at positive time; or
2. prove a scalar weighted mean-value theorem for the degenerate operator
   `partial_t-a Delta` with the potential absorbed by the critical product
   `beta_a`.

The Hardy-potential failure recorded by A03 rules out replacing this by an
abstract unweighted critical Nash argument.  The cutoff powers in `J_p` are the
information that the transition needs.

## 4. Curvature bound on the plateau

The first bounded-curvature plateau cannot be obtained by citing Shi estimates
from `L^2` data.  The logical order is:

1. use the q=2 and q=3 curvature energies to obtain a positive-time weighted
   finite-exponent bound, for example

   \[
     A^4Y(t)=A^4\int\eta^2aF^3\le {C\beta^3\over t};
   \]

2. on plateau balls where `a=1`, this is an ordinary supercritical spatial
   `L^3` curvature bound at positive time;
3. apply standard local parabolic Moser/regularity for the normalized Ricci
   flow on a smaller plateau ball to obtain

   \[
     |\operatorname{Rm}|\le C/t;
   \]

4. only after this point do Shi estimates provide derivative bounds.

Thus plateau regularity remains part of the downstream route, but it is an
output of the finite-exponent energy/Moser mechanism, not a substitute for it.

For continuation of the local flow, a support-wide weighted curvature estimate
`|a\operatorname{Rm}|<=C/t` is still relevant if one uses Yang's extension
result for local Ricci flow, because that theorem extends a solution under a
uniform bound for `|chi^2 Rm|`.  This bound is weighted and does not assert
unweighted transition regularity.

## 5. Local Ricci flow existence and the fixed-cutoff equation

The source `Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md`
contains Yang's local Ricci flow construction.  The exact passages needed here
are:

* lines 787--823: for a smooth metric and fixed compactly supported `chi`, Yang
  states short-time existence for
  `partial_t g=-2 chi^2 Rc`; the DeTurck construction solves a hatted equation
  with coefficient `(chi o phi_t^{-1})^2` and then sets
  `g=phi_t^* hat g`.  This is exactly how the pulled-back equation recovers the
  fixed spatial coefficient `chi^2` rather than a different transported-cutoff
  flow.
* lines 835--878: Yang's uniform-time theorem at the critical exponent is a
  first-exit argument carrying a Sobolev inequality, metric comparison, and
  current curvature energy; it obtains the weighted pointwise bound
  `||chi^2 Rm||_infty <= C C_S (t||nabla chi||^2+1)t^{-1}`.
* lines 1067--1109: Yang's Theorem A.7 and Corollary A.10 give the scalar
  critical and linear-potential Moser estimates used for curvature and Ricci-type
  tensors.
* lines 1127--1136: Yang's Appendix B theorem gives the supercritical local
  heat-flow estimate with output `|chi^2 f|` from input
  `int chi^{2p0-n} f^{p0}` and potential condition
  `(int chi^{q-n}u^{q/2})^{2/q}<=mu`; the choice `n=4,p0=q=6` matches
  `J_6` and `Y=int chi^2F^3`.
* lines 396--412 of the Wang/Yang pseudolocality source record the extension
  mechanism: a local Ricci flow extends if the weighted curvature tensor
  `|chi^2 Rm|` (or all weighted derivatives, then obtained by induction) remains
  uniformly bounded up to the terminal time.

These passages support two conclusions and one remaining adaptation.

First, smooth existence for each smooth input is available, but its initial
interval may depend on uncontrolled pointwise curvature.  It is only the
starting interval for the energy method.

Second, the desired uniform continuation to `theta r^2` must be proved by a
simultaneous argument: assume the solution exists up to a maximal time below
`theta r^2` while metric comparison, Sobolev control, beta smallness, weighted
curvature, and weighted velocity hold; use the energy/Moser estimates to improve
all of them; then Yang's extension mechanism rules out terminal breakdown.

Third, our normalized equation

\[
  \partial_tg=-2\chi^2(\operatorname{Ric}+g)
\tag{5.1}
\]

adds the compactly supported lower-order term `-2chi^2 g`.  In the DeTurck
construction the hatted equation should therefore use `(chi o phi^{-1})^2` in
front of both `Ric(hat g)` and `hat g`, plus the usual DeTurck term; pulling back
then gives (5.1) with the original fixed `chi`.  Since `-2chi^2 g` contains no
second derivatives, it should not change the parabolic estimates except through
lower-order constants, but this adaptation must be written explicitly before
T5 is regarded as inherited from Yang.

## 6. Revised simultaneous first-exit package

For each selected buffered support, the working interval should carry:

* metric comparison on the whole active support, controlled by (1.1);
* current Sobolev inequality and cutoff-gradient bounds transferred from the
  initial selected support through the metric comparison;
* curvature critical product smallness `beta_a(t)<=2 beta_0`;
* q=2 and q=3 curvature energy persistence and positive-time finite-exponent
  curvature bounds;
* fixed-p defect persistence (2.9);
* support-wide weighted velocity (3.2), giving (1.2);
* support-wide weighted curvature if Yang's extension theorem is used;
* plateau unweighted curvature only after the finite-exponent curvature step.

The buffered support geometry still removes the bad-center problem: all
Sobolev variables are supported inside the selected good support, and the
stationary collar kills auxiliary localization terms.  The global defect
identity from Step 25 also remains valid after the support estimates close.

## 7. Current status after this step

Established in this step:

1. The Codex report confirms the Step 24--25 tensor-energy weights and
   explicitly identifies the same missing weighted-velocity bootstrap.
2. The Step 25 first-exit note is corrected: plateau drift does not replace
   support-wide metric stability.
3. The fixed-p defect estimate (2.3)--(2.9) has the right cutoff powers and
   uses only initial pointwise pinching plus the same critical curvature product.
4. Source reading shows that Yang's local Ricci flow construction solves the
   fixed-cutoff equation by transporting the coefficient in DeTurck gauge and
   pulling back, while uniform continuation requires the energy/Moser package,
   not mere short-time existence.

Still open:

* prove the fixed-p energy inequality with full index constants, beyond the
  currently reliable schematic derivation;
* prove the weighted positive-time `L^p`-to-`L^infty` estimate (3.2) for `aE`;
* prove or adapt a support-wide weighted curvature bound sufficient for Yang
  extension;
* write the normalized DeTurck/Yang adaptation carefully;
* then return to the terminal calibrated-Derdzinski contradiction.

The full Yau 26 proposition remains open; this work concerns only the critical
four-dimensional negative LeBrun/Ishida--LeBrun route.

## 8. TTCS verification and Yang B.1 instantiation

TTCS (`trace/ttcs/results/step26_ttcs01_verifier1_integration.md`) independently
checked the correction and found it scientifically sound.  Its most useful
sharpening is that the `p=6` choice is not arbitrary: Yang Appendix B uses the
input weight `chi^{2p0-n}f^{p0}` and outputs `chi^2 f`.  With `n=4,p0=6` this
is exactly

\[
  \int\chi^8|E|^6=J_6,
  \qquad \chi^2|E|=a|E|.
\]

For the potential condition in Yang B.1, taking `q=6` and `u=F` requires

\[
  \left(\int\chi^{q-n}F^{q/2}\right)^{2/q}
  =\left(\int\chi^2F^3\right)^{1/3},
\]

which is precisely the positive-time weighted curvature moment supplied by the
q=3 curvature layer.  The smallness appearing in Yang's coefficient is
`S^2 mu^3`, and the q=3 output gives `S^2 mu^3 <= C beta^3/t` on a forward
time slab, so the product with `t` is controlled by the critical small parameter
`beta^3`.

The script `workspace/scripts/step26_yang_b1_instantiation.py` checks the
exponents:

\[
  S^{1/3}t^{-1/2}\left(t\delta^6V\right)^{1/6}
  =\delta r^{2/3}t^{-1/3},
  \qquad S\sim r^2V^{-1/2}.
\]

Thus the desired support-wide estimate

\[
  \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}
\]

has an exact Yang-template source once the scalar/Kato inequality for `|E|`, the
fixed `J_6` persistence, and the positive-time `Y` potential bound are proved.
TTCS also noted that `z_6=chi^5|E|^3` should be treated through
`(|E|^2+eps)^{3/2}` regularization or weak Kato estimates; the scripts and the
main note have been patched accordingly.
