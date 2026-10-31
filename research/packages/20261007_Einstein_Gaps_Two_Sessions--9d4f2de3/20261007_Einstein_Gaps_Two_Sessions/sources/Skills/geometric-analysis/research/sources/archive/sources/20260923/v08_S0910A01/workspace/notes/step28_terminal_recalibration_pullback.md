# Step 28: terminal recalibration and exponential-pullback selection

Session: S0910A01. Agent3 / Actuator. Phase: Execute.

## 0. Purpose and correction

This note repairs the downstream part of the four-dimensional negative
LeBrun/Ishida--LeBrun route after the Step 27 analytic work.  The previous
route assessment incorrectly suggested that the post-smoothing geometric step
needed an Euler-density localization or an F-structure noncollapse argument.
It does not, provided the selected-support construction has already produced a
sequence-uniform `A_i`-normalized family of bounded-curvature plateau centers,
`Vol(P_i) >= alpha A_i` with fixed `alpha>0`.  A merely nonzero volume that may
be `o(A_i)` would not select a small pulled-back mean from an `o(A_i)` global
integral.

The right mechanism is the Step 16 exponential-pullback averaging lemma.  It
requires only:

1. a terminal closed metric on the same smooth manifold;
2. a nonnegative terminal deficit density with total integral `o(A_i)`;
3. a set `P_i` of plateau centers with `Vol(P_i) >= alpha A_i`, for one fixed
   `alpha>0`;
4. a fixed radius `rho>0` such that all length-`rho` geodesics from centers in
   `P_i` remain inside a bounded-sectional-curvature plateau buffer.

No Euler characteristic density has to be assigned to the plateaux, and no
injectivity-radius bound on the base manifold is required.

## 1. Terminal recalibration on the flowed metric

Let

\[
  M_i=X_i\#k_i\overline{\mathbb{CP}}^{2},\qquad A_i=c_1^2(X_i),
  \qquad q_i=k_i-{A_i\over3}\ge0,
\]

be the critical Ishida--LeBrun laboratory and let `g_i(T)` be the terminal
metric after the buffered cutoff flow at a fixed time `T=theta r^2`.  The
flow has not changed the smooth manifold, so all topological Seiberg--Witten
and Chern--Gauss--Bonnet inequalities from Steps 3--8 apply again to `g_i(T)`.

Write

\[
  \mathcal E_i=\operatorname{Ric}_{g_i(T)}+g_i(T),
  \qquad Q_i(T)=\int_{M_i}|\mathcal E_i|^2\,d\mu_{g_i(T)}.
\]

This `Q` is the full Einstein-defect tensor for the target normalization
`Ric=-g`, not the trace-free Ricci tensor.  In four dimensions,

\[
  \mathcal E_i=\operatorname{Ric}_{g_i(T)}^\circ+{s_i+4\over4}g_i(T),
\]

and the two summands are orthogonal.  Therefore

\[
  \int (s_i+4)^2\le4Q_i(T),\qquad
  \int |\operatorname{Ric}_{g_i(T)}^\circ|^2\le Q_i(T).
\tag{1.1}
\]

With the Step 3 notation

\[
  J_i={1\over4\pi^2}\int {|\operatorname{Ric}_{g_i(T)}^\circ|^2\over2},
\]

we have

\[
  J_i\le {Q_i(T)\over8\pi^2}.
\tag{1.2}
\]

For the selected monopole sign class, the exact identity from Steps 4--5 is

\[
  D_{a_i}=J_i-q_i-{2\over3}\bigl((a_i^+)^2-A_i\bigr),
  \qquad 0\le D_{a_i}\le J_i-q_i\le J_i,
\tag{1.3}
\]

using `q_i>=0` and `(a_i^+)^2>=A_i` for the selected sign.  Thus all terminal
calibration deficits are controlled by the terminal `Q`.

The completion-square and explicit `G`-gap estimates from Step 8 give

\[
  \int\bigl(s_i+8\sqrt6\,|W^+_i|\bigr)^2\,d\mu
  \le 864\pi^2D_{a_i}\le108Q_i(T),
\tag{1.4}
\]

and

\[
  \int \mathcal G_i\,d\mu\le48\pi^2D_{a_i}\le6Q_i(T),
\tag{1.5}
\]

where

\[
  \mathcal G_i=f_i^2-(b_i)_-^2,
  \quad
  f_i={2\over3}s_i-2\sqrt{2/3}|W_i^+|,
  \quad
  b_i={2\over3}s_i+2w_i,
\]

and `w_i` is the lowest eigenvalue of `W_i^+`.

Define the combined nonnegative terminal density

\[
  \mathfrak D_i
  =|\mathcal E_i|^2+(s_i+4)^2
   +\bigl(s_i+8\sqrt6|W_i^+|\bigr)^2+\mathcal G_i.
\tag{1.6}
\]

Combining (1.1), (1.4), and (1.5),

\[
  \boxed{\int_{M_i}\mathfrak D_i\,d\mu_{g_i(T)}\le119\,Q_i(T).}
\tag{1.7}
\]

The constant is not important; its explicit value was checked in
`workspace/scripts/step28_terminal_pullback_constants.py`.  The point is that
terminal calibration is regenerated from topology and the terminal Einstein
energy.  It is not transported from the initial curvature tensor by `C^0`
metric comparison.

If the triangular global defect identity from the selected-support flow gives

\[
  Q_i(T)\le e^{C\theta}Q_i(0),
\tag{1.8}
\]

then the original pinching and `Vol(g_i(0))/A_i=O(1)` imply

\[
  {1\over A_i}\int_{M_i}\mathfrak D_i\,d\mu_{g_i(T)}\longrightarrow0.
\tag{1.9}
\]

## 2. Exponential-pullback selection on bounded-curvature plateaux

Assume that the analytic selected-support theorem has produced, at time `T`,
a measurable set `P_i` of inner plateau centers such that

\[
  \operatorname{Vol}_{g_i(T)}(P_i)\ge \alpha A_i
\tag{2.1}
\]

for one fixed `alpha>0`.  Assume also that there are fixed `rho>0` and `K<\infty`
such that for every `p in P_i`, every radial geodesic of length at most `rho`
from `p` remains inside the plateau buffer and satisfies

\[
  |\sec_{g_i(T)}|\le K,
  \qquad K\rho^2<\pi^2/4.
\tag{2.2}
\]

These are exactly the geometric outputs sought from the buffered cutoff flow:
on `a=1`, the support-wide bound `|aRm|<=C beta/T` becomes an ordinary
sectional-curvature bound, and the buffer condition is arranged by choosing
inner centers and `rho` smaller than the plateau-buffer width after metric
comparison.

For any nonnegative density `D`, the Step 16 exponential-pullback lemma gives

\[
  \int_{P_i} A_\rho D(p)\,d\mu(p)
  \le C(4,K,\rho)\int_{M_i}D\,d\mu,
\tag{2.3}
\]

where

\[
 A_\rho D(p)=
 {\int_{S_pM}\int_0^\rho D(\exp_p(t\xi))J_p(t,\xi)\,dt\,d\xi
  \over
  \int_{S_pM}\int_0^\rho J_p(t,\xi)\,dt\,d\xi}.
\]

Rauch comparison supplies the constant

\[
 C(4,K,\rho)=
 {\int_0^\rho s_{-K}(t)^3\,dt\over\int_0^\rho s_K(t)^3\,dt},
\]

and Liouville invariance of the geodesic flow gives the Fubini step.  Multiple
visits to a base point are harmless because `D>=0`; injectivity radius on
`M_i` is not used.

Apply (2.3) to `D=mathfrak D_i`.  Equations (1.9) and (2.1) imply

\[
  {1\over \operatorname{Vol}(P_i)}\int_{P_i}A_\rho\mathfrak D_i(p)\,d\mu(p)
  \le {C(4,K,\rho)\over\alpha A_i}
      \int_{M_i}\mathfrak D_i\,d\mu
  \longrightarrow0.
\tag{2.4}
\]

Hence there exists `p_i in P_i` with

\[
  A_\rho\mathfrak D_i(p_i)\longrightarrow0.
\tag{2.5}
\]

This is simultaneous selection for all four nonnegative components in
(1.6), because their sum has vanishing pullback mean.

## 3. Why base collapse is harmless here

Let

\[
  \widehat g_i=(\exp^{g_i(T)}_{p_i})^*g_i(T)
\]

on the tangent ball `B_rho(0) subset T_{p_i}M_i`.  Because `rho<pi/(2 sqrt K)`
and the radial sectional curvatures are bounded above by `K`, there are no
radial conjugate points on this domain, and `widehat g_i` is a smooth
Riemannian metric.  It may cover its image in `M_i` with multiplicity, but the
tangent-space points are not identified.

Rauch comparison gives two uniform controls on the tangent domain:

1. the pullback density is nondegenerate,
   `J_i(t,xi) >= s_K(t)^3`, so metric balls around the origin in the pullback
   domain have a positive lower volume bound depending only on `K` and `rho`;
2. curvature is uniformly bounded on a fixed ball, since every radial geodesic
   stays in the plateau buffer.

Thus the pullback domain supplies the noncollapsed local geometry needed for
harmonic-coordinate compactness even if the original base manifold is
arbitrarily collapsed.  No F-structure classification and no Euler-density
localization are involved.

The standard local regularity passage should be written with one shrink in
radius.  The Rauch lower Jacobian gives a center-ball volume lower bound in
`(B_rho(0),hat g_i)`, and the sectional-curvature bound gives the usual
center injectivity/harmonic-radius lower bound after passing to a smaller ball.
Shrinking once more propagates controlled harmonic coordinates on a fixed
subball.  This center-to-neighborhood step is ordinary bounded-curvature
local geometry, but it must be included in a full proof.

At positive time, plateau interior parabolic estimates provide curvature
derivative bounds on a smaller buffer once `|Rm|<=K` is known.  Equivalently,
for the weaker Step 8 passage, bounded curvature, Ricci-defect control, and
harmonic-radius estimates give strong finite-`W^{2,p}` convergence on a
smaller tangent ball; the `L^2` pullback smallness of `E` plus uniform curvature
bounds upgrades to any finite `L^p` by interpolation.  After passing to a
subsequence,

\[
  (B_{\rho'}(0),\widehat g_i)\longrightarrow(B_{\rho'}(0),g_\infty)
\]

smoothly or at least strongly in the finite-`W^{2,p}` sense required by Step 8.
The pullback mean (2.5) implies that, on the limit,

\[
  \operatorname{Ric}_{g_\infty}=-g_\infty,
  \qquad s_\infty=-4,
  \qquad s_\infty+8\sqrt6|W^+_\infty|=0,
  \qquad \mathcal G_\infty=0.
\tag{3.1}
\]

The first equation also gives `delta W^+_infty=0` by the four-dimensional
Bianchi identity for Einstein metrics.

From (3.1),

\[
  |W^+_\infty|^2={1\over24}.
\]

The Step 8 gap-density algebra then forces

\[
  \operatorname{spec}(W^+_\infty)=\left(-{1\over6},{1\over12},{1\over12}\right).
\tag{3.2}
\]

Derdziński's local theorem applies on the open set where `W^+` is nonzero: an
Einstein four-metric has harmonic `W^+`, and a harmonic self-dual Weyl tensor
with at most two eigenvalues is locally conformal to Kähler by the factor
`(24|W^+|^2)^{1/3}`.  In (3.2) this factor is constant, so the metric itself
is locally Kähler.  But a locally Kähler Einstein four-metric with `s=-4`
has

\[
  |W^+|^2={s^2\over24}={2\over3},
\]

contradicting `|W^+|^2=1/24`.  This is the same Step 8 forbidden germ, now
reached without base noncollapse.

## 4. Logical status

The terminal recalibration and pullback selection close the **downstream**
geometry of the restricted four-dimensional negative route, conditional on the
analytic selected-support theorem producing (2.1)--(2.2) and (1.8).  They do
not prove the full Yau Problem 26 proposition.

The remaining analytic consolidation is separate:

- the A03 general-`p` inequality and the Step 27/A03 time-cutoff recurrence
  should be used with polynomial `p`-dependence inside the Moser recurrence;
- fixed `J_6` persistence starts at time zero by fixed-exponent critical
  absorption, not by integrating the positive-time `Y ~ 1/t` coefficient;
- the normalized smooth continuation should be based on the shifted curvature
  `U=a(Rm+G)` induction, not on a generic statement that `-2ag` is lower order.

Even if these analytic pieces and the present terminal selection are completed,
the result excludes only the critical four-dimensional LeBrun/Ishida--LeBrun
negative laboratory.  It does not settle the positive branch, arbitrary
four-dimensional topologies, dimensions `n>=5`, or the all-dimensional Yau 26
statement and its Lean formalization.

## 5. Script evidence

- `workspace/scripts/step28_terminal_pullback_constants.py` checks the terminal
  constants `108`, `6`, and `119`, and the pullback-selection implication
  `(int D <= eps A, Vol P >= alpha A) => selected pullback mean <= C eps/alpha`.
- `workspace/scripts/step28_moser_recurrence_verify.py` checks the Step 28
  correction to the Moser exponent bookkeeping: `sum 1/p_k=(n+2)/(2p0)` but
  the net Sobolev power is `n/(2p0)`.

## 6. TTCS verification and Step 28 repairs

TTCS (`trace/ttcs/results/step28_ttcs01_verifier1_integration.md`) supports the
three central conclusions at their stated level: the corrected Moser recurrence
avoids the reciprocal-exponent and per-`p` Gronwall errors; the shifted
curvature `U=a(Rm+G)` removes the normalization/cutoff-jet obstruction at the
schematic Wang-mechanism level; and terminal recalibration plus exponential
pullback bypasses base noncollapse and Euler-density localization once a
quantitative plateau family exists.

The verification also sharpened the exact assumptions and remaining work:
`Vol(P_i)>=alpha A_i`, `rho`, and `K` must be sequence-uniform; the pullback
regularity proof should shrink once from the center-ball volume lower bound to
a controlled harmonic-coordinate subball; and the upstream selected-support
flow must still supply the simultaneous estimates `S^2Y<=C beta^3/t`, fixed
`J_6` persistence from time zero, active `H_2` control, global `Q(T)/A->0`, and
bounded-curvature plateau buffers in the same construction.  These have been
incorporated above.
