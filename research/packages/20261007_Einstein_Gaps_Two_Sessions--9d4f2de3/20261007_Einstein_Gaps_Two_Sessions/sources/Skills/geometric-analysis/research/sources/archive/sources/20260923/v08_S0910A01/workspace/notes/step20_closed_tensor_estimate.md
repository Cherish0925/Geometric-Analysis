# Step 20: closed tensor curvature estimate using `E = Ric + g`

## 1. Purpose of this step

The Step 19 Whitney reduction removes the cutoff-level degeneracy of
`partial_t - chi^2 Delta`, but the previous two-field formulation treated
`E = Ric + g` and `Rm` as if their gradients were independent.  They are not.
On every smooth time-slice of the cutoff flow

\[
  \partial_t g=-2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}+g,
\]

one has, in an orthonormal frame,

\[
  E_{ij}=R_{kikj}+g_{ij},\qquad
  \nabla_pE_{ij}=\nabla_pR_{kikj}.
\]

Thus

\[
  |\nabla E|\le C_4|\nabla \operatorname{Rm}|,
  \qquad |E|\le C_4(1+|\operatorname{Rm}|^2)^{1/2}.
\]

These identities are geometric contractions.  They do not require the initial
near-Einstein pointwise bound to persist.  Their main use is in the Hessian
cutoff terms: after integrating `nabla^2 a` by parts, every `nabla E` term can
be absorbed by the same full curvature dissipation as `nabla Rm`.  This replaces
the separate high-power defect-gradient energy from Step 19 by a closed
curvature-power inequality.

This does **not** control the unweighted defect energy by itself.  The global
quantity

\[
  Q(t)=\int_M|E(t)|^2\,d\mu_t
\]

is still separate because `aE` gives no pointwise control where `a` is small.
Section 7 records the corrected triangular estimate needed for `Q`.

## 2. Index-level variation and the absence of an Einstein-independent source

Use the standard variation formula for the `(0,4)` curvature tensor.  If
`h = partial_t g`, then schematically

\[
\begin{aligned}
(\partial_t R)_{ijkl}
=&\frac12\{\nabla_i\nabla_k h_{jl}+\nabla_j\nabla_l h_{ik}
        -\nabla_i\nabla_l h_{jk}-\nabla_j\nabla_k h_{il}\}\\
&+ h*R .
\end{aligned}
\]

For the normalized cutoff flow, `h=-2aE`.  Expanding second derivatives gives

\[
  \nabla\nabla(aE)=a\nabla\nabla E
        +(\nabla a)*\nabla E+(\nabla^2a)*E .       \tag{2.1}
\]

The first term supplies the principal curvature Laplacian after applying the
Bianchi identities and commuting derivatives.  The algebraic curvature terms
also receive contributions from the `h*R` part of the variation.  The resulting
structure is

\[
  a\nabla\nabla E+h*R
  = a\Delta \operatorname{Rm}+a(\operatorname{Rm}*\operatorname{Rm})
    +a(E*\operatorname{Rm})+a\operatorname{Rm},   \tag{2.2}
\]

up to the usual sign and tensor-type conventions.  The linear `a Rm` term is
therefore not attributed solely to `a nabla nabla E`; it is part of the algebraic
variation, including the normalized-flow contribution.  It is harmless in power
energies because `a<=1` and it is lower than the quadratic reaction after using
`F=(1+|Rm|^2)^{1/2}`.

The important point is that (2.1) has no term depending only on `nabla^2 a` and
`g`.  Splitting `-2aE` as `-2a Ric -2a g` creates artificial Hessian pieces, but
in the full variation they recombine into `(nabla^2 a)*E`.  Therefore an exact
negative Einstein metric, for which `E=0`, is stationary even in the transition
where `nabla a` and `nabla^2 a` are nonzero.

## 3. Power energy with the regularized curvature norm

Set

\[
  H=\operatorname{Rm},\qquad F=(1+|H|^2)^{1/2},\qquad q\ge2,
\]

and let `eta` be a spatial cutoff supported in one Whitney ball
`B_ell(y)`, with

\[
  \ell=c r\chi_0,
  \qquad \chi_0=\chi(y)>0,
  \qquad a_0=\chi_0^2 .
\]

On this ball, the Step 19 Whitney bounds give

\[
  (1-Lc)^2a_0\le a\le (1+Lc)^2a_0,
\]

and

\[
  \frac{|\nabla a|^2}{a}=4|\nabla\chi|^2\le 4L^2r^{-2},
  \qquad
  a|\nabla\eta|^2\lesssim c^{-2}r^{-2}.          \tag{3.1}
\]

Test the curvature equation against `eta^2 F^(q-2) H`, including the metric and
volume variations.  The principal `a Delta H` term gives

\[
\begin{aligned}
q\int\eta^2F^{q-2}\langle H,a\Delta H\rangle
\le&-c q\int\eta^2aF^{q-2}|\nabla H|^2 \\
&+Cq\int a|\nabla\eta|^2F^q
 +Cq\int\eta^2\frac{|\nabla a|^2}{a}F^q .       \tag{3.2}
\end{aligned}
\]

The last term in (3.2) is one of the regular first-derivative cutoff remainders.
The variable coefficient does not create an inverse power of `chi` because of
(3.1).

The quadratic curvature reaction, the normalized `aH` term, norm variation and
volume variation have the schematic bound

\[
  Cq\int\eta^2 a F^{q+1}+Cq\int\eta^2 aF^q .     \tag{3.3}
\]

## 4. Hessian-cutoff terms close with curvature dissipation

A representative Hessian term is

\[
  I=q\int\eta^2F^{q-2}\,H*(\nabla^2a)*E .        \tag{4.1}
\]

Integrating by parts once,

\[
\begin{aligned}
I=&-q\int \nabla a * \nabla(\eta^2F^{q-2}H*E) \\
=&-q\int\eta^2\nabla a*F^{q-2}(\nabla H)*E
  -q\int\eta^2\nabla a*F^{q-2}H*(\nabla E)       \\
&-q(q-2)\int\eta^2\nabla a*F^{q-3}(\nabla F)*H*E
  -2q\int\eta\nabla\eta*\nabla a*F^{q-2}H*E .   \tag{4.2}
\end{aligned}
\]

Using

\[
  |E|\le C_4F,
  \qquad |\nabla E|\le C_4|\nabla H|,
  \qquad |\nabla F|\le |\nabla H|,
\]

every nonlocalization term in (4.2) is bounded by

\[
  Cq^2\int\eta^2|\nabla a|F^{q-1}|\nabla H|.
\]

Young's inequality gives, for any small `epsilon`,

\[
\begin{aligned}
|I|\le& \epsilon q\int\eta^2aF^{q-2}|\nabla H|^2 \\
&+C_\epsilon q^3\int\eta^2\frac{|\nabla a|^2}{a}F^q
 +Cq\int a|\nabla\eta|^2F^q .                  \tag{4.3}
\end{aligned}
\]

The direct `(nabla a)*nabla E` terms from (2.1) satisfy the same bound, again
because `nabla E` is a contraction of `nabla H`.

Thus the Hessian cutoff has been removed in the weak energy sense without
introducing a separate high-power defect-gradient energy.  What remains is a
larger `q`-dependent coefficient in the regular cutoff potential
`(|nabla a|^2/a)F^q`.

## 5. Closed curvature-power inequality on one Whitney ball

Combining (3.2), (3.3), and (4.3), and absorbing a small portion of the gradient
term, yields

\[
\boxed{
\begin{aligned}
\frac{d}{dt}\int\eta^2F^q
&+c q\int\eta^2aF^{q-2}|\nabla H|^2 \\
&\le C q\int\eta^2aF^{q+1} \\
&\quad + C q^3\int\eta^2\left(\frac{|\nabla a|^2}{a}+a\right)F^q
      +C q\int a|\nabla\eta|^2F^q .             \tag{5.1}
\end{aligned}}
\]

The exact powers of `q` can be improved by a more careful tensor calculation,
but (5.1) is enough to reveal the structure:

* it is closed in curvature;
* it contains no term `a|nabla E|^2 F^(q-2)`;
* it contains no inverse power of `chi`;
* all cutoff contributions are measured by `r^{-2}` and `c^{-2}r^{-2}` on a
  Whitney ball.

The execution script

`workspace/scripts/step20_tensor_closed_curvature_energy.py`

records the same term ledger and the exponent bookkeeping.

## 6. Consequence for pointwise curvature: finite exponent before mean value

In dimension four the reaction term in (5.1) is controlled by the critical
Sobolev product.  With `phi=eta F^(q/2)`,

\[
\begin{aligned}
\int\eta^2 aF^{q+1}
&\lesssim a_0\|F\|_{L^2(B_\ell)}\|\eta F^{q/2}\|_{L^4(B_\ell)}^2 \\
&\le \beta_\ell
\left(\int a|\nabla(\eta F^{q/2})|^2
      +\ell^{-2}\int a\eta^2F^q\right),          \tag{6.1}
\end{aligned}
\]

where the Step 19/A03 cancellation gives

\[
  \beta_\ell=S_\ell\|F\|_{L^2(B_\ell)}
   \le C\sqrt{1+K_0}\,r^2,
  \qquad\text{independent of }\chi_0\text{ and collapsed volume.}       \tag{6.2}
\]

The additional `1` comes from the regularized norm `F=(1+|Rm|^2)^{1/2}`: the
constant part contributes `S_ell Vol(B_ell)^{1/2} <= C ell^2 <= C r^2`.

Absorbing (6.1) into the gradient term in (5.1) requires smallness of the form

\[
  C(q)\beta_\ell<c .                              \tag{6.3}
\]

The script table shows the important feature: in a direct power iteration the
threshold worsens with `q`.  Therefore the Whitney scaling by itself should not
be read as an all-exponent Li iteration.  A better route is:

1. use (5.1), time integration, and critical smallness to create at positive
   time one fixed exponent `q_0>2`, for instance `q_0=3` or `q_0=4`, without
   assuming such an initial `L^{q_0}` bound;
2. use this supercritical curvature integrability on nested positive-time
   Whitney cylinders to run a De Giorgi/Moser mean-value argument in which the
   potential is now spatially supercritical;
3. only then derive a pointwise estimate of the form

\[
   |a\operatorname{Rm}|\le C/t
\]

or an integrated substitute strong enough for the later defect estimate.

Failure of all-exponent critical absorption would not invalidate the Whitney
approach; it would only select this finite-exponent-plus-mean-value route.

## 7. Correct triangular estimate for unweighted defect energy

The previous Step 19 note inherited an unsafe inference.  An inequality of the
form

\[
  Q'(t)\le C r^{-2}Q(t)+\varepsilon X(t),
  \qquad X(t)=\int a|\nabla\operatorname{Rm}|^2,
\]

does **not** imply `Q(T) <= C Q(0)` at fixed smoothing scale, because
`int_0^T X(t)dt` may be `O(A)` in the LeBrun sequence.  This would leave an
`O(epsilon A)` error, not `o(A)`.

The correct defect estimate must use the triangular structure of the flow.  Since
`h=-2aE`, the equation for `E` has no curvature-only source:

\[
  \partial_tE=a\Delta_LE-2aE+(\nabla a)*\nabla E+(\nabla^2a)*E
             +a(\operatorname{Rm}*E)+a(E*E).      \tag{7.1}
\]

Testing by `eta^2E` and integrating the Hessian cutoff term by parts gives

\[
\boxed{
\begin{aligned}
\frac{d}{dt}\int\eta^2|E|^2
&+c\int\eta^2a|\nabla E|^2 \\
&\le C\int\eta^2\left(\frac{|\nabla a|^2}{a}+a+a|\operatorname{Rm}|\right)|E|^2
   +C\int a|\nabla\eta|^2|E|^2 .                \tag{7.2}
\end{aligned}}
\]

The algebraic curvature and quadratic-defect terms are potentials multiplying
`E^2`; using `|E| <= C F`, they are bounded by `C a(1+|Rm|)|E|^2`.  In dimension
four the curvature part is absorbed exactly as in the curvature estimate:

\[
\begin{aligned}
\int a|\operatorname{Rm}|\,|\eta E|^2
&=\int |\operatorname{Rm}|\,|\chi\eta E|^2 \\
&\le \|\operatorname{Rm}\|_2\,\|\chi\eta E\|_4^2 \\
&\le \beta_\ell\left(\int\eta^2a|\nabla E|^2
      +r^{-2}\int\eta^2|E|^2\right).            \tag{7.3}
\end{aligned}
\]

For sufficiently small `beta_ell`, (7.2)--(7.3) yield the finite-neighbor system

\[
  \frac{d}{dt}Q_\alpha(t)
     \le C(c,L,N)r^{-2}\sum_{\beta\sim\alpha}Q_\beta(t).  \tag{7.4}
\]

Summing unnormalized local energies over a bounded-overlap family gives

\[
  Q_{\mathrm{support}}(T)
     \le \exp(C_NT/r^2)Q_{\mathrm{support}}(0).  \tag{7.5}
\]

Outside the support, `a=0` and the metric is stationary.  Therefore (7.5), not an
additive `epsilon X` inequality, is the route that can preserve
`Q(T)/A -> 0` from `Q(0)/A -> 0`.

The execution script

`workspace/scripts/step20_triangular_defect_energy.py`

records this correction and shows numerically why the discarded additive form is
insufficient at the scale of the LeBrun topology parameter.

## 8. Revised PDE targets after this step

The Step 19 pair of targets should be reformulated.

**Curvature target.**  Prove a localized Whitney-cylinder estimate from (5.1):
small critical `L^2` curvature energy gives either

\[
  |a\operatorname{Rm}|\le C/t,
\]

or first gives a fixed supercritical `L^{q_0}` bound strong enough to obtain the
same pointwise bound by a positive-time mean-value argument.  The constants must
be independent of `chi_0` and collapsed volume, while their dependence on the
fixed exponent is allowed.

**Derivative target.**  If a later Bernstein estimate is still needed, derive it
from the curvature-controlled equation for `U=aE`.  A03's `p>4` threshold remains
relevant for connection and cutoff-Hessian drift, but the high-power
curvature estimate itself no longer needs a separate defect-gradient energy.

**Unweighted defect target.**  Prove the triangular local and support-summed
estimate (7.2)--(7.5).  This is the only form currently capable of preserving
`Q/A -> 0` at a fixed smoothing scale.

This step therefore changes the analytic structure: the curvature-power layer is
more closed than the two-field Step 19 description, while direct all-exponent
critical iteration is less secure than the Step 19 wording suggested.  The
central unfinished work is now a rigorous localized parabolic theorem based on
(5.1), plus the triangular defect estimate (7.5).  The broader Yau 26 problem
remains open; this is still only the critical four-dimensional negative
LeBrun/Ishida-LeBrun laboratory.

## 9. TTCS verification and repairs incorporated

TTCS independently supported the main Step 20 change: because all contractions
and covariant derivatives are taken with respect to the current metric, `nabla E`
is controlled by `nabla Rm`, and high-power curvature energies can close without
separate high-power defect-gradient energies.  It also supported the triangular
unweighted defect estimate as the correct replacement for the old additive
`epsilon X` inference.

The verification required several repairs, now inserted above:

1. The linear `a Rm` term in the curvature equation should not be attributed
   solely to `a nabla nabla E`; it also comes from the algebraic `h*Rm` part of
   the curvature variation.
2. The schematic `E` equation should not contain a stray `(nabla a)*Rm*E` term.
   The curvature terms are `a Rm*E` (as part of, or adjacent to, `a Delta_L E`)
   and `a E*E`, so (7.2) has the potential `a(1+|Rm|)|E|^2`.
3. Since `F=(1+|Rm|^2)^{1/2}`, the Whitney Sobolev product is
   `S_ell ||F||_2 <= C sqrt(1+K0) r^2`; the constant part contributes `O(r^2)`.
4. A fixed `L^{q0}` input at `t=0` is not available from critical `L^2`; the
   finite-exponent route must create such integrability at positive time, as in
   Li's proof where local `L^2` persistence yields an `L^3` potential before a
   linear Moser step.
5. Final constants still depend on the tensor type, evolving metric comparison,
   local support budget, Whitney neighbor count, cutoff constants, and precise
   `q` bookkeeping.  No pointwise `|a Rm| <= C/t` theorem has yet been proved.

The additional script `workspace/scripts/step20_finite_exponent_route.py` records
this finite-exponent logic.  It shows schematically that unlimited critical
absorption would require a threshold deteriorating with `q`, while reaching a
single exponent such as `q0=3` or `4` remains compatible with fixed small beta and
matches the structure of Li's source proof.
