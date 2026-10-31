# Step 12: toric determinant equation, twist correction, and invariant volume-gap probes

> **Step 13 Preceptor correction.** Read this note together with `workspace/notes/step13_preceptor_toric_spectral_review.md`.  The determinant identity is stronger than the original Section 8 priority list: for exact Einstein metrics it gives the Schrödinger ground-state equation `(-Delta_B + |F|^2/2) w = 2 lambda w`, and for positive `C^0` pinching it gives the Rayleigh bound `lambda_1^Dir(Omega) <= 2(1+delta)` without proving approximate orthogonal transitivity.  Exact orthogonal transitivity in the simply connected closed Einstein `T^2` case is also source-supported by the toric Einstein paper read in Step 13.  The remaining invariant-class bottleneck is the volume-gap/edge-curvature weighted inequality, not the first proof of twist vanishing.

Session S0910A02, Agent3/Actuator, Execute.

## 0. Research role of this step

Step 11 showed that pointwise Cheeger--Tian-type regularity is false under only
$C^0$ Ricci pinching: in a diagonal $T^2$-invariant ansatz on
$S^2\times S^2$, the trace-free Hessian can be hidden from Ricci while remaining
visible to Riemann.  The Strategist correctly pointed out that the same ansatz is
not only a regularity toy: it is the natural laboratory for the four-dimensional
positive volume-gap conjecture behind Proposition A.

This step therefore did exact local calculations for the general $T^2$-invariant
Einstein reduction, rather than continuing with Li smoothing or a non-executable
search for explicit Sha--Yang metrics.  The main result is a source-checkable
symbolic reduction:

* the orbit-area density $w=\sqrt{\det h}$ satisfies a scale-fixing elliptic
  equation;
* twisting modifies the equation by a positive vertical-curvature term;
* the mixed Einstein equation is exactly the conserved twist equation which, in
  the presence of a degeneration boundary and smooth closure, should force the
  twist constants to vanish (orthogonal transitivity);
* in the resulting diagonal/twist-free class the determinant equation is
  $\Delta_B w=-2w$ for $\operatorname{Ric}=g$, and the rectangular separable
  model has an explicit volume gap, but the general invariant volume gap is not
  yet proved because edge curvature/Weyl can still turn the transverse circle
  quickly.

The step also repaired the cross-session Pontryagin bookkeeping: $p_1(TM)$ and
$p_1(\Lambda^2_+)$ have different signs and magnitudes in the near-critical
LeBrun family.  The calibrated density used in the LeBrun/Derdzinski argument is
$p_1(\Lambda^2_+)$, not the tangent Pontryagin class.

## 1. General local $T^2$-invariant metric and symbolic jet calculation

Write a $T^2$-invariant metric over a two-dimensional orbit space in Kaluza--Klein
form
\[
 g=g_B+h_{IJ}(d\phi^I+A^I)(d\phi^J+A^J),\qquad I,J=1,2,
\]
where $h$ is the positive definite metric on the torus orbits and
\[
 w=\sqrt{\det h}
\]
is the orbit-area density.  At a regular orbit choose geodesic orthonormal base
coordinates $x,y$, a vertical basis with $h(0)=I$, and a gauge with $A(0)=0$.
Let
\[
 F^I=f_I\,dx\wedge dy
\]
at the point.

I wrote and ran

* `workspace/scripts/step12_toric_determinant_symbolic.py`, saving
  `workspace/data/step12_toric_vertical_trace_symbolic.json`;
* `workspace/scripts/step12_toric_mixed_ricci_symbolic.py`, saving
  `workspace/data/step12_toric_mixed_ricci_symbolic.json`;
* `workspace/scripts/step12_toric_mixed_ricci_gauge_compare.py`, saving
  `workspace/data/step12_toric_mixed_gauge_compare.json`.

The vertical-trace script computes Christoffels and Ricci from the metric jets.
It gives, exactly at the point,
\[
 \operatorname{tr}_h\operatorname{Ric}^{V}
 =h^{IJ}\operatorname{Ric}_{IJ}
 =-\frac{\Delta_B w}{w}+\frac12 |F|_h^2,                    \tag{1}
\]
where in the gauge $h=I$, $|F|_h^2=f_1^2+f_2^2$.  The raw output was
\[
\operatorname{tr}_h\operatorname{Ric}^{V}+\Delta_B w={f_1^2+f_2^2\over2}.
\]
Thus an Einstein metric $\operatorname{Ric}=\lambda g$ satisfies
\[
 \boxed{\Delta_B w=\left({1\over2}|F|_h^2-2\lambda\right)w.}       \tag{2}
\]
For the positive branch normalized by $\operatorname{Ric}=g$,
\[
 \Delta_B w=\left({1\over2}|F|_h^2-2\right)w.                    \tag{3}
\]
Therefore the Strategist's clean equation $\Delta w=-2w$ is exactly correct in
the twist-free case, but twisting does **not** disappear algebraically: it weakens
the eigenvalue by the nonnegative term $|F|^2/2$.

The mixed-Ricci gauge computation identifies the twist equation.  In the gauge
$A_x^I=0$, $A_y^I=f_I x$ to first order, put
\[
 C_I=w\,h_{IJ}f_J.
\]
The script gives
\[
 \operatorname{Ric}_{xI}=\frac12\partial_y C_I,
 \qquad
 \operatorname{Ric}_{yI}=-\frac12\partial_x C_I.                 \tag{4}
\]
Equivalently,
\[
 \boxed{d\bigl(w h_{IJ} *_B F^J\bigr)=0.}                       \tag{5}
\]
This is the Riemannian Weyl--Papapetrou/twist conservation law.  It also explains
why free collapse and collapse with fixed points differ.  If the orbit space has
no degeneration boundary, the constants $C_I$ may be nonzero.  If a smooth
compact action has a degeneration edge, then smooth closure forces the twist flux
$C_I=w h_{IJ}*_BF^J$ to vanish at the edge (finite curvature and one vertical
eigenvalue collapsing), hence the constants should vanish on the connected
regular orbit space.  In the interior, $w>0$ and $h$ is invertible, so
\[
 F=0.                                                            \tag{6}
\]
This is the exact mathematical point to turn into a lemma: **for a smooth
Einstein four-manifold with effective $T^2$ symmetry and fixed points, the
orthogonal complement to the orbits should be integrable.**  In that case the
clean determinant equation survives twisting because twisting has first been
forced to zero.  In a free quotient such as the odd-dimensional lens/Sasaki
collapse mechanism there is no boundary condition, so no Dirichlet eigenfunction
and no such vanishing.

For a $C^0$-pinched metric rather than an exact Einstein metric, (1) becomes
\[
 \Delta_B w=\left({1\over2}|F|_h^2-2+O(\delta)\right)w            \tag{7}
\]
in the positive branch, and (4)--(5) becomes an approximate twist-conservation
equation.  Stability of the boundary-forces-twist-zero argument is therefore a
real quantitative issue, not a formal corollary.

## 2. Twist-free diagonal equations and the determinant eigenfunction

In the twist-free diagonal case
\[
 g=g_B+p^2d\theta^2+q^2d\varphi^2,
 \qquad w=pq,
\]
the standard warped-product Ricci formulas give
\[
 \operatorname{Ric}_B=K_Bg_B-{\nabla^2p\over p}-{\nabla^2q\over q},              \tag{8}
\]
\[
 \Delta_Bp=(K_B-\lambda)p,
 \qquad
 \Delta_Bq=(K_B-\lambda)q,
 \qquad
 \langle\nabla p,\nabla q\rangle=-K_Bpq                         \tag{9}
\]
when $\operatorname{Ric}=\lambda g$; the displayed Strategist equations are the
case $\lambda=1$.  Taking the determinant combination cancels $K_B$:
\[
 \boxed{\Delta_B(pq)=-2\lambda pq.}                              \tag{10}
\]
For $\lambda=1$, $w=pq$ is a positive first Dirichlet eigenfunction with
eigenvalue $2$, vanishing precisely on the degeneration locus.

The divergence form is useful:
\[
 \operatorname{div}(q\nabla p)=-\lambda pq,
 \qquad
 \operatorname{div}(p\nabla q)=-\lambda pq.                      \tag{11}
\]
If $p=e^v\sqrt w$ and $q=e^{-v}\sqrt w$, then (11) and (10) imply
\[
 \operatorname{div}(w\nabla v)=0.                                \tag{12}
\]
For an exact smooth diagonal Einstein metric with bounded $v$ and ordinary
boundary behavior, integrating (12) gives
\[
 \int_\Omega w|\nabla v|^2=0,
\]
so the Step-11 opposite-warping freedom is not an exact Einstein deformation.  It
is a $C^0$-Ricci/CZ regularity counterexample precisely because finite warping can
hide large Hessian from Ricci without satisfying the full exact reduced Einstein
system.

## 3. Volume and boundary flux

With $2\pi$-periodic torus coordinates,
\[
 \operatorname{Vol}_4(M)=4\pi^2\int_\Omega w\,dA_B.              \tag{13}
\]
Integrating (10) gives the flux identity
\[
 2\lambda\int_\Omega w\,dA_B
 =-\int_{\partial\Omega}\partial_{\nu_{out}}w\,ds_B.             \tag{14}
\]
On an edge where the primitive circle corresponding to $p$ collapses,
$p=0$ and smooth closure gives $|\nabla p|=1$, hence
\[
 -\partial_{\nu_{out}}w=q
\]
(up to the primitive lattice normalization).  Thus
\[
 2\lambda\int_\Omega w
 =\sum_{p\text{-edges}}\int q\,ds_B
  +\sum_{q\text{-edges}}\int p\,ds_B.                            \tag{15}
\]
The right side is proportional to the total area of the fixed two-spheres.  In
the positive Einstein normalization, collapse in this invariant class is exactly
collapse of these fixed-sphere areas.  This is the precise version of the
Strategist's observation.

## 4. Rectangular/separable sanity check: exact scale pinning and a gap

I tested the simplest exact family: a rectangle with flat base and separated
closure functions
\[
 p={L_x\over\pi}\sin {\pi x\over L_x},
 \qquad
 q={L_y\over\pi}\sin {\pi y\over L_y}.
\]
Then $p_x(0)=1$, $q_y(0)=1$, and
\[
 -\Delta(pq)=\left({\pi^2\over L_x^2}+{\pi^2\over L_y^2}\right)pq.
\]
The Einstein determinant equation requires
\[
 {\pi^2\over L_x^2}+{\pi^2\over L_y^2}=2.                      \tag{16}
\]
The four-volume is
\[
 \operatorname{Vol}_4=(2\pi)^2{4L_x^2L_y^2\over\pi^4}.            \tag{17}
\]
By AM--GM under (16), $L_x=L_y=\pi$ minimizes the volume and
\[
 \operatorname{Vol}_4\ge16\pi^2,                                \tag{18}
\]
with equality at the product $S^2\times S^2$ metric.  The script
`workspace/scripts/step12_rectangular_toric_volume_gap.py` verifies this and
records samples in `workspace/data/step12_rectangular_toric_volume_gap.json`.
Aspect-ratio degeneration increases the volume rather than producing collapse.

This is not a theorem for all toric metrics, but it is a useful calibration: when
unit closure and eigenvalue $2$ are both enforced in the most elementary class,
there is no hidden way to shrink $p$ and $q$ uniformly.

## 5. Why the general invariant volume gap is not yet closed

The determinant equation and unit closure are strong, but this step did not prove
that they alone give a uniform lower bound for $\int w$ on an arbitrary smooth
orbit space.  A local expansion near a $p=0$ edge shows where the remaining
freedom sits.

Use Gaussian base coordinates
\[
 g_B=dr^2+a(r,s)^2ds^2,
 \qquad a(0,s)=1,
\]
with a geodesic edge so $a_r(0,s)=0$.  Write
\[
 a=1+{a_2(s)\over2}r^2+O(r^3),
 \quad p=r+p_3(s)r^3+O(r^4),
 \quad q=Q(s)+q_2(s)r^2+O(r^3).
\]
Substituting into the twist-free exact equations (9) gives
\[
 p_3={-2a_2-1\over6},
 \qquad
 2q_2=a_2Q,
 \qquad
 Q''+(1+2a_2)Q=0.                                                \tag{19}
\]
For $S^2\times S^2$, $a_2=0$ and $Q(s)=\sin s$.  In general, however, the edge
coefficient $a_2=-K_B|_{edge}$ is a Weyl/sectional-curvature degree of freedom,
not controlled by the Ricci tensor alone.  Large positive or negative $a_2$ could
make the transverse circle turn over on a shorter scale.  This is exactly the
kind of hidden-Hessian/sectional freedom exposed by the Step-11 CZ spike.

Therefore the honest conclusion is:

* in the exact smooth $T^2$-invariant Einstein class with fixed points, the twist
  should vanish and $w$ obeys the scale-pinning Dirichlet equation;
* rectangular and separable models have an explicit volume gap;
* a full invariant volume-gap proof still needs a global control mechanism for
  edge curvature/rod geometry, or else an explicit counterexample exploiting that
  freedom.

This is already sharper than the previous Li-smoothing target: the volume-gap
question has been reduced to concrete reduced Einstein equations and their
boundary/rod behavior.

## 6. Characteristic-class bookkeeping repair for the negative branch

The Strategist warned that A01's Pontryagin budget could mix two different
classes.  I wrote and ran
`workspace/scripts/step12_characteristic_class_bookkeeping.py`, saving
`workspace/data/step12_characteristic_class_bookkeeping.json`.  For
\[
 M=X\#k\overline{\mathbb{CP}}^{\,2},
 \qquad A=c_1^2(X)=2\chi(X)+3\tau(X),
\]
we have
\[
 \chi(M)=\chi(X)+k,
 \qquad
 \tau(M)=\tau(X)-k={A-2\chi(X)\over3}-k.                         \tag{20}
\]
Thus
\[
 \int_M p_1(TM)=3\tau(M)=A-2\chi(X)-3k,                          \tag{21}
\]
which is typically negative in the near-critical regime $k\sim A/3$:
\[
 {1\over A}\int p_1(TM)=-2{\chi(X)\over A}+o(1).
\]
But the LeBrun/Derdzinski calibrated Chern--Weil density used by A01/A03 is the
one for $\Lambda^2_+$:
\[
 \int_M p_1(\Lambda^2_+)=2\chi(M)+3\tau(M)=A-k\sim{2A\over3}>0.  \tag{22}
\]
The magnitude statement survives, but the sign and even the bundle are
sign-sensitive.  Any NUT/bolt residue comparison must therefore say explicitly
whether it is measuring $p_1(TM)$, $p_1(\Lambda^2_+)$, or $p_1(\Lambda^2_-)$.
This session has already lost time to a coefficient/bookkeeping error, so this
normalization should be fixed before further Taub--NUT or diffuse-flux tests are
used as evidence.

The peer computations in messages #252--#254 also change the negative-branch
execution target: standard Taub--NUT--AdS is not a finite-residue calibrated-bulk
model.  It is either inaccessible because a core-containing ball has divergent
mean curvature energy, or accessible on smaller annuli with a hyperbolic limit and
macroscopic calibrated defect.  The remaining issue is diffuse non-basic mixed
curvature in the $\Lambda^2_+$ connection, not counting $O(A)$ NUT residues.

## 7. Consequences for the Yau-26 program

1. **Positive branch, invariant class.**  The first truly geometric collapse
   mechanism in the session is now explicit: positive Einstein scale forces the
   orbit-area determinant to solve an elliptic equation with nonzero eigenvalue,
   while Ricci-flat collapse has $\Delta w=0$ and no absolute scale.  This explains
   why K3 semi-flat/Ooguri--Vafa collapse does not contradict the positive branch.

2. **Free collapse escape.**  Lens/Sasaki-type quotients escape because there is
   no degeneration boundary, hence no Dirichlet eigenfunction and no boundary
   forcing of twist constants.  Simple connectivity/fixed points enter exactly at
   this boundary condition.

3. **Twist caveat.**  Twisting does not magically preserve $\Delta w=-2w$; it
   contributes $+|F|^2w/2$.  The way to recover the clean equation is to prove
   orthogonal transitivity from the mixed equation and smooth degeneration.  For
   $\delta$-pinched metrics this becomes a quantitative approximate-transitivity
   problem.

4. **Regularity in proportion.**  The $L^p$ regularity program remains useful for
   chart passage and Chern--Weil localization, but it should not displace the
   determinant/rod geometry.  If the volume gap is true in the invariant class, it
   is visible on the two-dimensional orbit space before any CFG smoothing theorem
   is invoked.

5. **Still far from the full proposition.**  This is not a proof of $P_4^+$, not a
   refutation, and not all-dimensional.  It provides a concrete reduced system and
   exact symbolic checks that can now be attacked by Agent2/Agent4 or by peer
   sessions.

## 8. Immediate next mathematical work

The strongest continuation is not another pointwise-regularity lemma.  It is:

* prove the orthogonal-transitivity lemma carefully for smooth compact Einstein
  four-manifolds with $T^2$ fixed points, using (5) and rod boundary behavior;
* derive the stable $C^0$-pinched version of (2) and (5), including how much twist
  can remain when $\operatorname{Ric}=g+E$ with $\|E\|_\infty\le\delta$;
* attack the edge/rod volume lower bound: either prove that (10), unit primitive
  closure, and the reduced Einstein equations force a positive lower bound for
  $\int w$, or construct a reduced solution sequence where edge curvature $a_2$
  turns the transverse lengths over at arbitrarily small scale;
* compare the reduced system with known toric Einstein classifications and with
  higher-dimensional $T^k$ determinant equations.
