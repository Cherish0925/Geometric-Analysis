# Step 17: Support-scale-consistent cutoff flow architecture

Session: S0910A01. Agent2/Constructor. Phase: Execute.

> **TTCS correction (Step 17).**  Independent verification found three
> errors in the original version: (a) the plateau radius 3r_* does not
> contain all Li covering balls — must enlarge to 4r_* with support 5r_*;
> (b) the transition bootstrap does not yield unweighted |Rm| ≤ C/t —
> the natural bound is the weighted |chi^2 Rm| ≤ C/t; (c) the metric
> comparability argument was circular: |E(0)| ≤ delta does not imply
> |E(t)| ≤ delta without the curvature bound.  The support-scale
> initial-data construction (Sections 1–3) is correct after the radius
> fix.  The Sobolev-energy cancellation mechanism (Section 5.5) is
> correct as a static algebraic identity.  The joint continuation
> package (weighted curvature, weighted defect, metric comparability,
> Sobolev preservation) remains the decisive open analytical theorem.

## 0. Purpose and correction scope

This note constructs the support-scale geometry that resolves the
quantifier mismatches identified in Step 16, and formulates the
precise analytical theorem needed for the cutoff flow.  The key advance
is choosing all radii as fixed multiples of r_* (the Li scale), so that:

- every center used by the Li covering argument lies in the plateau,
- the maximal function controls the initial condition at every such center,
- different supports have disjoint plateaux.

The Sobolev-energy cancellation is a valid algebraic mechanism, but the
full transition-inclusive continuation theorem is not proved here.  The
remaining analytical object is precisely formulated in Section 9.

## 1. Setup: support geometry at the Li scale

Fix a critical LeBrun sequence (M_i, g_i) with Ric_{g_i} = -g_i + e_i,
||e_i||_infty = delta_i -> 0, A_i -> infty, k_i/A_i -> 1/3.  The Noether
energy bound gives int_{M_i} |Rm|^2 dmu <= K_1 A_i with K_1 = C(chi,tau).

### 1.1 Maximal function good set

For each i, define the good set at scale R_0 = 4r_*:

  G_i = { p in M_i : M_{R_0}(|Rm|^2)(p) <= K_0 },

where M_R denotes the centered maximal function at scale R:

  M_R(f)(p) = sup_{0 < r <= R} fint_{B_r(p)} f.

By the weak-type (1,1) inequality for the maximal function on (M_i, g_i)
with Ric >= -3g:

  Vol(G_i^c) <= C(4) / K_0 * int_{M_i} |Rm|^2 <= C(4) K_1 A_i / K_0.

Since Vol(M_i) >= c_vol A_i (from the calibrated near-equality volume),
choosing K_0 = 2 C(4) K_1 / c_vol gives:

  Vol(G_i) >= (1/2) Vol(M_i).

The constant K_0 depends only on the dimension, Noether constants, and the
calibrated volume coefficient — all dimension-only in the LeBrun laboratory.

### 1.2 Vitali selection and thinning

Apply the Vitali covering lemma: select a maximal collection of disjoint
balls {B_{r_*}(p_j)}_{j in J} with p_j in G_i.  Then:

  G_i subset Union_j B_{5r_*}(p_j).

The total disjoint volume satisfies:

  Sum_j Vol(B_{r_*}(p_j)) >= Vol(G_i) / BG(5) >= Vol(M_i) / (2 BG(5)),

where BG(s) = V_{-1}(sr_*)/V_{-1}(r_*) ~ s^4 for small r_* (Bishop-Gromov).
So BG(5) ~ 625 for small r_*.

**Thinning for disjoint supports.**  We need the supports B_{5r_*}(p_j) to
have disjoint plateaux.  Specifically, we require that for each j, the plateau
B_{4r_*}(p_j) does not intersect any other support B_{5r_*}(p_k), k != j.
This requires d(p_j, p_k) > 9r_* for all k != j.

Standard greedy thinning: process the Vitali centers in any order.  Include
p_j if B_{10r_*}(p_j) does not contain any previously selected center.  The
resulting subcollection S has controlled volume loss: each selected center's
B_{11r_*} can contain at most BG(11) ~ 11^4 ~ 14641 Vitali balls.  Therefore:

  Sum_{j in S} Vol(B_{r_*}(p_j)) >= Vol(M_i) / (2 * 625 * 14641)
                                    >= Vol(M_i) / (1.83 * 10^7).

This is a positive (fixed) fraction of Vol(M_i), independent of collapse.

### 1.3 Support and plateau geometry (corrected)

For each j in S, define:

  - Support:    Omega_j = B_{5r_*}(p_j),  |nabla chi_j| <= C / r_*
  - Plateau:    Pi_j   = B_{4r_*}(p_j),    chi_j = 1
  - Bootstrap:  D_j    = B_{r_*}(p_j),     interior of Li coverage
  - Buffer:     Omega_j \ Pi_j = annulus of width r_*

The thinning ensures d(p_j, p_k) > 10r_* for j != k in S, so:

  Pi_j cap Omega_k = empty   for j != k.

**Covering geometry check (corrected).**  For x in D_j = B_{r_*}(p_j),
Li's covering uses y_k in B_{3r_*/2}(x) with B_{r_*}(y_k) covering
B_{2r_*}(x).  The covering balls extend to:

  d(y_k, p_j) <= 3r_*/2 + r_* = 5r_*/2,
  B_{r_*}(y_k) subset B_{7r_*/2}(p_j).

Since 7r_*/2 = 3.5 r_* < 4r_* = plateau radius, all covering balls
lie strictly inside Pi_j.  (The original 3r_* plateau was too small
by 0.5r_*; the TTCS correction identified this.)

## 2. The cutoff flow on the closed manifold

Run the normalized cutoff flow on (M_i, g_i):

  d_t g = -2 (Sum_{j in S} chi_j^2) (Ric + g).

**On each plateau Pi_j**: chi_j^2 = 1, no other chi_k contributes, so:

  d_t g = -2(Ric + g) = -2E       (standard normalized Ricci flow).

**On each transition Omega_j \ Pi_j**: the flow involves chi_j, its gradient,
and the Einstein defect.  The homogeneous structure means E = 0 is stationary.

**On the frozen region M \ Union_j Omega_j**: d_t g = 0.

## 3. Initial Li condition on the bootstrap domains

For each j in S and any y in B_{2r_*}(p_j):

  d(y, p_j) < 2r_*,  so B_{r_*}(y) subset B_{3r_*}(p_j) subset B_{4r_*}(p_j).

Since p_j in G_i with M_{4r_*}(|Rm|^2)(p_j) <= K_0:

  fint_{B_{r_*}(y)} |Rm|^2 <= int_{B_{4r_*}(p_j)} |Rm|^2 / Vol(B_{r_*}(y))
                              <= K_0 Vol(B_{4r_*}(p_j)) / Vol(B_{r_*}(y))
                              <= K_0 BG_{r_*}(5)

where BG_{r_*}(5) = V_{-1}(5r_*)/V_{-1}(r_*) ~ 5^4 = 625 for small r_*.

The Li dimensionless quantity at scale r_*:

  epsilon_y(r_*) = r_*^4 fint_{B_{r_*}(y)} |Rm|^2 <= 625 K_0 r_*^4.

For the Li threshold epsilon_Li (a universal constant in dimension 4), choose:

  r_* = (epsilon_Li / (625 K_0))^{1/4}.

This is a FIXED physical scale depending only on dimension, Noether constants,
and calibration.

## 4. Plateau containment is only a geometric input

**Step 18 correction.**  The radius repair in Section 1.3 ensures that the
covering balls appearing in Li's local argument lie inside the region where
`chi=1`.  This does **not** by itself establish a localized Li bootstrap.
Li's theorem controls a supremum over the whole set of centers under
consideration.  If one defines

  e(t)=sup_{y in B_{2r_*}(p_j)} ( int_{B_{r_*}(y)} |Rm(t)|^2 )^{1/2},

then the evolution estimate written for centers `x in B_{r_*}(p_j)` does not
control the time derivative of the same supremum at centers near the edge of
`B_{2r_*}(p_j)`.  Enlarging the plateau to `B_{4r_*}(p_j)` fixes the
containment of the immediate covering balls, but it does not close the
supremum inequality.  Restricting the supremum to the smaller center set
recreates the inner/outer problem identified in Steps 16--17.

The plateau equation is the standard normalized Ricci flow where `chi=1`.
The unresolved problem is not an extra local tensor term entering that
equation; it is that parabolic energy estimates require controlled adjacent
regions and Ricci flow has no finite propagation boundary.  Subsequent use of
Li's Corollary 3.5 is therefore conditional on a genuine full-support
continuation theorem, not a consequence of the radius bookkeeping alone.

## 5. Correct weighted full-support starting point

Let

  a=chi^2,        E=Ric+g,        K=|Rm|,

and suppose schematically that the cutoff-flow curvature inequality has the
form

  partial_t K <= a Delta K + c a K^2 + T,

where `T` contains the cutoff-derivative and coupled-defect terms.  Since `a`
is time-independent and `f=aK`, on `{a>0}` one has

  partial_t f <= a Delta f - 2 <nabla a,nabla f>
                 + ( 2|nabla a|^2/a - Delta a ) f
                 + c f^2 + aT.                       (5.1)

Thus the quadratic reaction is `c f^2`, not `c f^2/a`.  Also

  |nabla a|^2/a = 4 |nabla chi|^2.

This removes the artificial inverse-cutoff reaction that appeared in the
previous weighted-Moser discussion.  It does not solve the smoothing problem:
the principal operator in (5.1) is still degenerate, and the real terms in
`T` include

  |nabla a| |nabla E| |Rm|,       |nabla^2 a| |E| |Rm|,
  a |E| |Rm|^2,                  a |Rm| |E|^2,

up to dimension-dependent contractions and lower-order normalized-flow terms.
These terms must be controlled in a coupled curvature/defect energy estimate.
One cannot assume that `f` is initially small in the transition merely because
`chi` is small; the unweighted curvature may depend on the sequence.

### 5.1 Integrated scalar structure for `f=aK`

Testing (5.1) against `eta^2 f` and integrating by parts gives the schematic
inequality

  d/dt int eta^2 f^2 + c int eta^2 a |nabla f|^2
     <= C int (a|nabla eta|^2 + eta^2 |nabla chi|^2) f^2
        + C int eta^2 f^3 + C int eta^2 f aT,

where the `Delta a` term is not a pointwise Hessian requirement: after
integration by parts it combines with the drift term and is bounded using
`|nabla a|^2/a=4|nabla chi|^2`.  The remaining difficulty is the degenerate
factor `a` in the dissipation.  A standard four-dimensional Sobolev absorption
of `int f^3` would require a dissipation comparable to `int |nabla f|^2`, or a
weighted Sobolev inequality adapted to `a`; this is not yet available.

### 5.2 Defect energy and unweighted `Q`

For the same flow, A03's tensor calculation gives

  partial_t E = a(Delta_L E - 2E) + C_a(E),

where every term in `C_a(E)` is homogeneous in `E` and its first derivatives.
After contraction with `E` and integration by parts, the Hessian of `a` cancels
from the global energy identity.  With a localization cutoff `eta`, the target
estimate has the form

  d/dt int eta^2 |E|^2 + c int eta^2 a |nabla E|^2
     <= C int (a|nabla eta|^2 + eta^2 |nabla chi|^2 + eta^2 a) |E|^2
        + C int eta^2 a |Rm| |E|^2.                   (5.2)

The reaction in the last term should be tested through `chi E`:

  int a |Rm| |E|^2 = int |Rm| |chi E|^2
     <= ||Rm||_2 ||chi E||_4^2
     <= A_U ||Rm||_2 int |nabla(chi E)|^2.

In dimension four the relative Sobolev coefficient satisfies
`A_U ~ r^2/Vol(U)^{1/2}`, while `||Rm||_{L^2(U)} <= (K_0 Vol(U))^{1/2}` on a
maximal-function support.  The product is `O(sqrt(K_0) r^2)`, independent of
collapse, and can absorb part of the available `int a|nabla E|^2` dissipation
plus a controlled `r^{-2} int |E|^2` remainder.  This is the correct use of the
Sobolev-energy cancellation.

The unweighted support-summed defect

  Q(t)=int_M |E(t)|^2

is a separate output required for topological recalibration.  A weighted
pointwise estimate for `aE` controls metric speed but gives no information in
the transition where `a` approaches zero.  The continuation theorem must
therefore provide a collapse-uniform growth estimate for `Q(t)` jointly with
curvature-energy persistence; it cannot be replaced by homogeneity alone.

### 5.3 Cutoff derivatives

A pointwise assumption `|nabla^2 chi| <= C/r_*^2` is not automatic from a
Ricci lower bound.  The integrated defect estimate above avoids this by
cancelling Hessian terms.  The curvature energy still contains schematic
`nabla^2 a * E * Rm` terms; these should also be integrated by parts to move
derivatives from `a` onto `E`, `Rm`, and the localization functions, producing
only gradient-cutoff terms.  If a proof ultimately needs pointwise Hessian
control, then constructing such cutoffs under the actual sequence hypotheses is
part of the theorem, not an innocuous choice.

Sections 6--7 below describe why a successful full-support theorem would feed
into topological recalibration and the Derdzinski contradiction.  They should
be read with the replacement theorem target in Section 9 and the Step 18 note,
not as consequences of an already established plateau bootstrap.
## 6. Global defect control and topological recalibration

### 6.1 The smoothed metric on the closed manifold

At time t_0 = theta r_*^2, the closed manifold carries the terminal metric
h_i = g_i(t_0).  On each D_j:

  |Rm_{h_i}| <= C_3/t_0   (bounded curvature),
  |Ric_{h_i} + h_i| <= C' delta_i -> 0.

On the frozen region M \ Union Omega_j:

  h_i = g_i,   |Ric_{h_i} + h_i| = |e_i| <= delta_i.

On the transition Omega_j \ Pi_j: h_i is some evolved metric with
homogeneous-in-E evolution.  Without a quantitative transition estimate,
we cannot bound |E| pointwise there.  However, the transition volume is:
## 6. Conditional downstream use after a full-support theorem

The following downstream chain is valid only if a separate full-support
weighted continuation theorem supplies the two analytical outputs below at
some fixed time `t_0=theta r_*^2`:

1. bounded curvature on a positive-volume set `P_i` contained in the plateaux
   where `chi=1`, for example `|Rm_{h_i}| <= C/t_0` on `P_i`; and
2. unweighted global/support-summed defect control

   `Q_i(t_0)=int_{M_i}|Ric_{h_i}+h_i|^2 = o(A_i)`.

A pointwise estimate for `chi^2 E` alone is insufficient for (2), because it
vanishes as `chi -> 0` and gives no direct control of unweighted transition
energy.  The support-summed defect estimate must be proved by an energy
inequality such as (5.2) together with curvature-energy persistence.

### 6.1 Recalibration on the terminal metric

If the terminal smooth closed metric `h_i=g_i(t_0)` satisfies `Q_i(t_0)/A_i ->
0`, then the LeBrun mixed Seiberg-Witten estimate and Chern-Gauss-Bonnet apply
to `h_i` on the same smooth oriented four-manifold:

  I(h_i) = (4pi^2)^{-1} int (s^2/24 + 2|W^+|^2) >= (2/3)(a^+)^2,
  I(h_i) - J(h_i) = A_i - k_i.

Together with the critical topology `k_i/A_i -> 1/3`, this recovers the Step
4--8 near-equality analysis for `h_i`: the modulus remainder and the explicit
nonnegative tensor-defect density force the calibrated profile in the averaged
sense,

  s -> -4,       |W^+| -> 1/(2 sqrt 6),
  Spec(W^+) -> (-1/6, 1/12, 1/12)

on regions selected by small defect density.

### 6.2 Exponential-pullback and Derdzinski contradiction

If the continuation theorem also gives a positive-volume set `P_i` with
bounded sectional curvature at time `t_0`, A03's exponential-pullback averaging
lemma can replace the earlier normal-cover/CFG layer.  For nonnegative

  F_i = |E_i|^2 + (s_i + 8 sqrt(6)|W_i^+|)^2 + G_i

augmented as needed by the amplitude/eigenline density from A03's positive-part
monopole repair, the global `int F_i/A_i -> 0` selects pulled-back exponential
balls with vanishing average of `F_i`.  Bounded curvature and Rauch lower
volume on these pulled-back balls yield controlled harmonic charts.  The Step
8 finite-`p` harmonic-coordinate passage then gives a smooth local Einstein
limit with the calibrated two-eigenvalue `W^+` spectrum.

Derdzinski Proposition 5, verified in Step 8, forbids such a germ: an Einstein
four-metric with `Ric=-g`, harmonic `W^+`, `W^+ != 0`, and the calibrated
constant two-eigenvalue profile would be locally Kahler with constant conformal
factor, while a four-dimensional Kahler-Einstein metric with scalar `-4` has
`|W^+|^2=s^2/24=2/3`, not `1/24`.

## 7. Present mathematical status

The support-scale geometry and the Sobolev-energy cancellation are useful
inputs.  The LeBrun critical-family contradiction is not established until the
weighted full-support continuation theorem supplies both bounded-curvature
plateaux and unweighted defect energy `Q_i(t_0)/A_i -> 0`.

This prospective result would exclude the critical LeBrun/Ishida-LeBrun
negative laboratory.  It would not prove the full four-dimensional negative
sign branch, the positive branch, dimensions `n>=5`, or the Lean 4 formalization
required by the highest research goal.

## 8. Corrected continuation theorem target

Let `(M^4,g_0)` be closed with `|Ric+g_0|<=delta`.  Let `chi` be supported in a
scale-`r` region `Omega`, equal to one on an interior plateau, and suppose the
initial support has collapse-compatible curvature energy control at the fixed
scale.  Seek a smooth solution of

  partial_t g = -2 chi^2 (Ric+g)

on `[0,theta r^2]` satisfying a coupled package:

- metric comparability on the active support;
- persistence of relative Sobolev inequalities and finite-overlap covers;
- weighted curvature control for `a Rm` or `chi^2 Rm`, with unweighted
  curvature bound on the plateau where `a=1`;
- weighted pointwise defect control for `aE`, sufficient to integrate metric
  speed;
- unweighted support-summed growth control for `Q(t)=int |E(t)|^2`;
- curvature-energy persistence at the fixed scale.

The scalar transformation

  f=aK,   a=chi^2,   K=|Rm|

turns `partial_t K <= a Delta K + c a K^2 + T` into

  partial_t f <= a Delta f - 2<nabla a,nabla f>
                 +(2|nabla a|^2/a-Delta a)f + c f^2 + aT.

The quadratic term is `c f^2`, not `c f^2/a`.  The hard terms are the degenerate
diffusion, cutoff-gradient remainders, possible Hessian-cutoff terms in the
curvature equation, and the coupled `E` terms.  Integrated estimates should
avoid assuming pointwise `|Hess chi|` when possible; if such a bound is needed,
its construction under the actual hypotheses is part of the theorem.

### Files

- This corrected note: `workspace/notes/step17_support_scale_li_bootstrap.md`
- Step 18 note: `workspace/notes/step18_weighted_cutoff_system.md`
- Step 18 scripts: `workspace/scripts/step18_weighted_cutoff_algebra.py`,
  `workspace/scripts/step18_sobolev_scaling.py`
- TTCS: `trace/ttcs/results/step17_ttcs01_verifier1_integration.md`
