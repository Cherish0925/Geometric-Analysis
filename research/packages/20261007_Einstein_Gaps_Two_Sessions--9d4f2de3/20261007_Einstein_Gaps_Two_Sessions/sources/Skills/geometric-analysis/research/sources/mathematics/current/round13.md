# Round 13: broader integral obstructions and a concrete obstruction to tame repair

21 September 2026.

This round advances the mathematics from the twelve-round baseline. It does
not reorganize the Skill, change running Sessions, or assign a journal level.
The question remains whether dimension-only pointwise Ricci pinching forces
some Einstein metric on the same closed smooth manifold.

## 1. Integral rigidity: the conformal class is the necessary scope of solvability

The previous integral proof used an actual monopole to solve all its positive
weighted equations. Its analysis never compares solutions on different
polarizations: on a fixed metric it varies only the conformal factor. This
allows the metric-dependent **polarized** monopoles in the classical blow-up
and handle-addition formulas to supply the complete required input.

The resulting extension is as follows. Suppose a closed oriented base
\(N\) has \(T_0=2\chi(N)+3\tau(N)>0\) and a nonzero ordinary
Seiberg--Witten invariant with Chern class \(c\), in the small-perturbation
chamber when \(b_+=1\). Set \(A=c^2\ge T_0\). On

\[
 M=N\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)
\]

the existing integral theorem now implies

\[
 \mathcal E(g)+
 \left(\frac{T_0-k-4\ell}{A}-\frac23\right)_+\ge c_* >0.
 \tag{1}
\]

The constant is universal within these assumptions. For every minimal
general-type complex surface this gives

\[
 \mathcal E(g)+
 \left(\frac13-\frac{k+4\ell}{c_1^2(N)}\right)_+\ge c_* ,
 \tag{2}
\]

including \(b_+=1\). The proof retains one selected spin-c structure
through all conformal rescalings, its square, the actual chamber, and the
holonomy insertions. It does not pretend that every sign choice is an
all-metric monopole.

A critical example is the single blow-up of a simply connected
\(p_g=0,K^2=3\) surface of Park--Park--Shin: its ratio is exactly
\(k/A=1/3\), and (2) yields \(\mathcal E(g)\ge c_*\). Passing to a
finite cover cannot put this simply connected example inside the old
high-\(b_+\) statement.

This is a new domain consequence of the preceding integral theorem and
classical polarized gauge theory, not another proof of the integral
self-test. [Full argument and primary sources](round13_chamber.md).

## 2. Closed constructions: identify the mode that makes direct repair singular

The round-11 collar contains a long region with fixed hyperbolic fibre and
radius \(a(t)=c_\ell\cosh(\sqrt3t)\). Its local product Einstein
equation has the explicit trace-free, divergence-free kernel

\[
 H=\operatorname{sech}^2(\sqrt3t)
       (dt^2-a(t)^2d\phi^2).
 \tag{3}
\]

It changes the waist-circle length. Its integral pairing with that closed
geodesic vanishes for every infinitesimal diffeomorphism but is nonzero for
\(H\), so it is a geometric deformation, not a coordinate artifact.

Because the mapping-class cutoff has a fixed constant plateau, this tensor
can be localized strictly inside that plateau. Outside the fixed shear
strip it is an exact local kernel. The shear-strip error is suppressed by
\(\ell\), and the cutoff error by exponential decay in the collar length.
Consequently the **full** Bianchi-gauged Einstein linearization has an
explicit approximate kernel, with error a positive power of \(\ell\).
One obtains one such independent tensor on every disjoint gluing collar.

For a fixed plateau fraction \(0<\vartheta<1\), the precise bounds are

\[
 \|P_\ell H_\ell\|_{C^{0,\alpha}}\le C\ell^\vartheta,
 \quad \|H_\ell\|_{C^{2,\alpha}}\ge1,
 \quad
 \frac{\|P_\ell H_\ell\|_2}{\|H_\ell\|_2}
          \le C\ell^{3\vartheta/4}.
 \tag{3a}
\]

Thus a full Hölder inverse, if it exists, has norm at least
\(c\ell^{-\vartheta}\). On a graph with \(m\) collars the full
self-adjoint operator has at least \(m\) eigenvalues in
\([-C\ell^{3\vartheta/4},C\ell^{3\vartheta/4}]\), with multiplicity.
The actual shear residual has the exact projection

\[
 \int\langle\mathrm{Ric}_{G_\ell}+3G_\ell,H_\ell\rangle
 =-2\pi c_\ell^3\|\beta\|_2^2
      \int_0^1\cosh(\sqrt3t)(z_s')^2dt<0
 \tag{3b}
\]

when the shear form is nonzero. This supplies both a genuine low mode
and its forcing on the actual closed geometry.

This gives a concrete cause of inverse degeneration and identifies modes
that a full nonlinear reduction must keep. It does not assert that an
inverse after deleting these modes is uniformly bounded. Nor does a
nonzero projection of the initial residual alone decide the nonlinear
obstruction equation.

[Collar kernel, quantitative estimates, and residual pairing](round13_neck_kernel.md).
[Independent curvature-variation and gauge review](round13_neck_review.md).

## 3. Global determination: continuous nonsymmetric repair is impossible

On the specified nonzero-shear manifolds, the earlier construction has
exact volume

\[
 V_* =\frac{4\pi^2}{9}\chi(M)
\]

in the \(\mathrm{Ric}\approx-3g\) normalization. The scalar monopole
equality case and non-Kähler topology imply that any exact normalized
Einstein metric, if one exists, has volume **strictly larger** than
\(V_*\).

Meanwhile, fixed-normalization Einstein volume is locally constant on
its moduli space. For a smooth path this follows directly by integrating
the scalar-curvature variation; the local analytic premoduli statement
extends the conclusion to connected components.

It follows that there is no continuous family of exact Einstein metrics
\(Q_\ell\), including completely nonsymmetric ones, with

\[
 \mathrm{Ric}_{Q_\ell}=-3Q_\ell,\qquad
 \|G_\ell^{-1}(Q_\ell-G_\ell)\|_{C^0,\mathrm{op}}\to0.
 \tag{4}
\]

More precisely, each fixed normalized Einstein component \(\mathcal C\)
stays at relative \(C^0\) distance at least

\[
 \sqrt{V_{\mathcal C}/V_*}-1>0
\]

from the entire constructed family, even after arbitrary diffeomorphisms.
Any vanishing-size repair **sequence** would have to visit infinitely many
components with distinct volumes decreasing to \(V_*\). Such an
accumulation has not been excluded.

This connects global nonattainment to the actual repair problem. In
particular, a continuously parameterized, unique-root Newton construction
with shrinking corrections cannot work on the whole small-\(\ell\) tail.
The collar calculation in Section 2 gives an explicit linear mechanism
consistent with this global obstruction.

[Proof, componentwise distance, and precise Newton assumptions](round13_global.md).

## 4. A second route to all-mode obstructions: averaging followed by optical flow

There are two complementary analytic steps.

First, on a collapsing circle-invariant background, a geometrically
\(C^2\)-small perturbation \(q\), of size \(\eta\), has nonzero
circle modes \(k=q-\mathsf A q\) bounded by

\[
 |k|\le Ca^2\eta,\qquad |\nabla k|\le Ca\eta.
\]

The averaged linearized equation vanishes on \(k\). If \(q\) is
exact Einstein, its circle average therefore has Ricci error only
\(O(a^2\eta^2)\), not merely \(O(\eta^2)\).
[Tensor proof and a sharp coordinate example](round13_averaging.md).

Second, for a circle-invariant metric with **spatially varying** radius,
move the quotient surfaces with normal speed equal to that radius.
Writing the quotient as \(a^2ds^2+h_s\), the exact equation is

\[
 \partial_s(H/a)=D-|S|^2-a^2Q,
 \qquad Q\ge0,
 \tag{5}
\]

where \(D\) is the vertical-minus-normal Ricci component. The lapse
variation cancels the spatial radius Laplacian. This yields a marked
Teichmüller boundary estimate with the actual accumulated error.
[Optical receiver, stable-surface test, and local splitting](round13_radius.md).

Combining these two steps gives an obstruction to small repairs in all
tensor modes **if the averaged quotient has the stated global optical
foliation and endpoint bounds**. That global foliation is not supplied
by smallness alone. Focal points and mismatched arrival faces remain
specific geometric alternatives, rather than an omitted regularity
assumption.

The optical method has classical static-potential antecedents; the
calculation here retains connection energy, Ricci error, and marked
boundary data. The circle Fourier suppression is a local analytic
estimate, not a new global compactness theorem.

## 5. What these results change, and the next exact question

The rigidity extension removes an unnecessary restriction on the
monopole input. The closed-collar calculation identifies explicit
geometric near-kernels and their forcing. The global argument rules
out a continuous exact repair branch without imposing symmetry.
Together these replace the vague assertion that “small residual may
not imply a nearby exact solution” by concrete analytic and moduli
constraints on this fixed family.

The most direct next calculation is the **complete reduced equation**
for the waist modes: solve the complement with controlled constants,
retain its Schur feedback, include the other low modes and exterior
response, and evaluate the nonlinear obstruction. The signed initial
shear projection is one input to that equation, not its solution.

The global alternative is equally precise: can normalized Einstein
volumes on these particular smooth manifolds accumulate at \(V_*\)
through infinitely many distinct components? Even a negative answer
would exclude nearby repairs, not automatically every distant Einstein
metric. A Yau26 branch counterexample still requires excluding **all**
Einstein metrics on the constructed smooth type; full negation of the
working problem still requires both signs in one dimension.

## 6. Verification

The proof notes contain their complete assumptions and derivations.
This round also supplies four executable exact checks:

- `round13_averaging_check.py`: coordinate Ricci calculation and the
  radius-squared averaging commutator.
- `round13_radius_check.py`: five rational coordinate jets with variable
  spatial radius and electric/magnetic connection curvature.
- `round13_global_check.py`: volume normalization, first variation,
  determinant comparison, and contraction constants.
- `round13_neck_kernel_check.py`: product kernel and associated exact
  collar identities.

These finite checks accompany the written analytic arguments; they
do not prove global PDE existence or certify originality. Prior
twelve-round theorems used in Sections 1 and 3 remain explicit inputs.

All four programs were executed in this round with
`/data/qiushi/qiushi_engine_v09/.venv/bin/python` and exited successfully.
The deliberately incorrect neck profile was rejected. Separate proof
reviews checked the chamber input, averaging estimates, optical
cancellation, volume/continuity argument, and collar localization;
the continuity hypothesis and Hölder inverse spaces were corrected
before recording the final statements.
