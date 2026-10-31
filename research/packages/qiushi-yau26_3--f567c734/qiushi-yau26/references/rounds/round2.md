# Yau26: weak curvature transfer, complete model corrections, and twisted connectors

19 September 2026. This round develops three specific mathematical connections
left open by the preceding round. It produces conditional theorems,
complete calculations in a declared model, and explicit tests of proposed
global deductions. Neither unrestricted Yau26 branch is settled.

## 1. Rigidity: retain the global calibration without a global eigenline

The [rigidity derivation](round2_rigidity.md) starts with the manuscript's
actual monopole classes and quantified Seiberg--Witten deficit. Let
\(\mathcal D\) be its nonnegative curvature-calibration density,
\(d=\int\mathcal D\), and \(\Delta\) the deficit of one monopole class.
For \(\delta_-(g)\le1/64\), it constructs a measurable projection \(P\)
of rank at most one and proves

\[
 \|(I-P)H\|_2^2\le\frac{\Delta+37d}{\pi^2}.
\]

The essential step is control of harmonic mass on the bad set, not simply
control of that set's volume. The amplitude estimate already places
\(|H|\) close to a fixed positive constant in L2. It therefore bounds the
mass lost when the lowest Weyl eigenline is undefined or its gap is small.
Walsh averaging gives global phase-separation estimates for the actual
monopole sign cube, with constants independent of its size. No global
spectral gap, pointwise harmonic-form bound, or noncollapse is added.

A smooth version uses the spinor quadratic form \(\psi\), without dividing
by its norm:

\[
 A_\psi=\frac{|\psi|^2}{24}I-\frac18\psi\otimes\psi,
 \qquad
 \|W^+-A_\psi\|_2^2\le\Delta+649d+\eta.
\]

For every \(\eta>0\), the construction also gives

\[
 \|A_\psi\|_\infty\le\frac9{4\sqrt6},\qquad
 \int|\nabla A_\psi|^2\le10\operatorname{Vol}M+\Delta+d+\eta.
\]

Weyl-operator norms here are Hilbert--Schmidt; the Ricci pinching norm is
the spectral operator norm. Spinor zeros cause no singularity in this
quadratic tensor. Its divergence is small in the intrinsic negative
Sobolev norm when the normalized deficits tend to zero.

The same argument identifies a necessary derivative-energy defect. For
a hypothetical critical sequence with vanishing normalized calibration
and monopole deficits, the selected smooth models satisfy

\[
 \fint|\nabla A_\psi|^2\longrightarrow\frac18,
 \qquad \fint|\operatorname{div}W(A_\psi)|^2
                      \longrightarrow\frac1{16},
\]

even though their divergence tends to zero in intrinsic H-1. These constants
follow from the weighted two-form Hodge identity, not from a numerical
experiment. Testing the model against its own Weitzenböck equation does
not contradict this: that energy identity reproduces the weighted Hodge
identity exactly. A further argument must control or interpret this
surviving derivative energy, rather than silently discard it.

### A separate local transfer theorem

The [weak-curvature note](round2_weak_curvature.md) proves that the
divergence restricted to a single Weyl half has injective symbol

\[
 |\sigma_D(\xi)A|^2=|\xi|^2|A|_{\rm HS}^2.
\]

On a fixed coordinate ball, assume uniform ellipticity, uniform
\(C^{1,\alpha}\) metric bounds, C1 convergence, and Ricci residual tending
to zero in L2. Then the Weyl operators converge **strongly in L2 locally**.
A separate L2 curvature bound is unnecessary: a localized negative-order
elliptic estimate first supplies it by absorption. Harmonic-coordinate
regularity is applied only to the resulting weak Einstein limit.

This allows the forbidden calibration spectrum to pass to a smooth local
Einstein limit without a Cotton L2 estimate.

### Closing that connection under a full-curvature bound

The final argument of this round does produce the required patches under
one explicit additional hypothesis. For every finite K, all closed oriented
four-metrics satisfying \(|\mathrm{Rm}|\le K\) obey

\[
 \fint_M\left(|\operatorname{Ric}+g|^2+
       \operatorname{dist}_{\rm HS}(W^+,\mathcal O_0)^2\right)
       \ge c_0(K)>0,
\]

where \(\mathcal O_0\) is the orbit of
\(\operatorname{diag}(-1/6,1/12,1/12)\). Neither base injectivity,
volume, diameter, nor Cotton is bounded. Ricci doubling selects a ball
with small average defect in a hypothetical violating sequence. Exponential
pullback supplies a noncollapsed source with a boundary buffer. A
path-lifting multiplicity argument transfers the average without treating
the exponential map as a global cover. Controlled harmonic coordinates
and the weak-curvature theorem then produce the forbidden Einstein germ.

Combining this with the stated monopole budget gives, in the specified
blow-up family and pinched regime,

\[
 \delta_-^2+\left(\frac13-\frac{k}{A}\right)_+
       \ge\frac{c_0(K)}{675}.
\]

The constant is existential and depends on the extra full-curvature bound.
This proves a conditional version of the desired joint gap, not its
unrestricted form.

There is a sharper description of the remaining degeneration: if the Ricci
defect and average spectral defect tend to zero, then for every fixed K,R
the proportion of centers whose R-ball has \(|\mathrm{Rm}|\le K\) tends
to zero. Thus curvature concentrations must approach almost every center
at every fixed observation scale. This does not say that the high-curvature
set itself occupies positive volume or that curvature diverges pointwise.

## 2. Construction: solve the whole model equation and account for its end flux

The [construction derivation](round2_construction.md) treats all ten
symmetric-tensor components on the product of two complete hyperbolic
cylinders. Within the angularly invariant class it classifies **every
bounded Jacobi field**, including jointly radial, nonseparable candidates.
The kernel is eight-dimensional: two TT polarizations on either factor,
multiplied by a constant or by the other factor's bounded harmonic function
\(J(v)=\arctan(\sinh v)\). There are no bounded trace or mixed modes in
this class. The proof combines exterior comparison, a ground-state
transform, and an explicit one-dimensional spectral factorization.

An actual nonlinear metric family realizes all eight tangent directions.
The complete quadratic Ricci source includes the mixed blocks and the
interaction between the two factors. If \(b_1,B_1\) are the two twist-transfer
coefficients, its two length projections satisfy

\[
 \int\langle D,Q_1+Q_2\rangle
       =-\frac{\pi^2}{2}(b_1^2+B_1^2).
\]

A length transfer can cancel one detector but not both when a twist
transfer remains. Nevertheless this is **not** a nonexistence theorem:
the full invariant L2 operator has gap \(L\ge1/8\), and

\[
 K=-L^{-1}D
\]

solves all second-order tensor equations. The Bianchi identity removes
the gauge term, giving an actual complete-model correction with
\(\operatorname{Ric}(g_s+s^2K)+(g_s+s^2K)=O(s^3)\).

The correction necessarily exports the nonzero projected source as end
flux. The detectors are not L2, so L2 decay of the correction cannot be
used to discard their boundary terms. The next global question is whether
that compulsory flux can be received by the rest of the same marked
surface bundle while satisfying the remaining equations.

### Why a global scalar spectral gap does not settle the matching

On a degenerating collar, \(v_\ell(u)=J(u)\chi(u/R_\ell)\), with
\(R_\ell\) proportional to \(|\log\ell|\), can vanish near both thick
mouths while keeping the nonconstant limit \(J(u)\) in its thin core.
Its global L2 Laplacian tends to zero because that core has vanishing
area. Thus a uniform positive scalar eigenvalue and matching thick-end
values do not eliminate the model transfer. The derivation records the
stronger volume-normalized residual condition actually needed. This
corrects a tempting, but false, passage from global L2 information to a
pointed collapsed limit.

## 3. Global determination: twisting has a compulsory physical cost

The [global derivation](round2_global.md) goes beyond the orthogonally
transitive connector model. Assume a complete free isometric T2 action,
cylindrical quotient, and two exactly hyperbolic expanding ends outside a
compact set. Interior connection twist is allowed. Put

\[
 \epsilon=\|g^{-1}\operatorname{Ric}+3I\|_\infty,
 \qquad Q_*=\sup Q,
\]

where \(Q\) is the physical twist energy. The charged Bochner estimate,
weighted heat-kernel calculation, and minimal separator imply, for small
\(\epsilon\),

\[
 Q_*\ge q_*(\epsilon):=
 \sqrt{3+\epsilon}
  \bigl(\sqrt{54-42\epsilon}-2\sqrt{12-8\epsilon}\bigr)-2\epsilon.
\]

In particular every hypothetical vanishing-defect sequence in this class
must satisfy

\[
 \liminf Q_*\ge9\sqrt2-12>0.
\]

The mixed Ricci equation also bounds the transport of conserved torus
charge. With the orbit-area- and shape-weighted path quantity \(H_*\)
defined in the proof,

\[
 Q_*\le4\epsilon^2H_*^2,
 \qquad H_*\ge\frac{\sqrt{q_*(\epsilon)}}{2\epsilon}.
\]

Thus bounded weighted transport gives a positive gap even with twist;
without that bound, vanishing Ricci defect requires order-one twist and
transport diverging at least as \(1/\epsilon\). A coordinate collar
length alone is not the transport quantity. Orbit-area excursions and
changing physical covolumes cannot be omitted.

An exact calculation on a classical toral AdS metric also distinguishes
flat conformal infinity from an exact hyperbolic open end. The former can
carry nonzero conserved charge, visible in its cubic asymptotic coefficient;
the latter forces zero charge for an exact Einstein metric. The example
is one-ended and does not construct a two-ended connector.

## Consequences for the next mathematical work

The remaining connections are more specific than before:

1. Remove the full-curvature bound from the new joint gap, using the
   spinor-induced Weyl model and the specific derivative-energy defect,
   or construct geometry realizing the required fixed-scale curvature
   concentrations. Average L2 curvature bounds alone cannot be substituted
   for the pointwise bound used in the proof.
2. Match the complete-model correction and its compulsory end flux on the
   fixed marked surface bundle; retain noninvariant modes and globally
   compatible end data when passing beyond the present model.
3. Couple the charged transport escape to physical lattice data and the
   closed-manifold curvature/volume budget, or construct a connector that
   satisfies all those conditions simultaneously.

These are alternatives to investigate, not assumptions that they must all
yield rigidity. A successful global construction or exact Einstein
existence result could change the direction of the argument.

## Files and verification

- [Rigidity proof](round2_rigidity.md), [independent review](round2_rigidity_review.md).
- [Weak-curvature proof](round2_weak_curvature.md), [independent review](round2_weak_review.md).
- [Complete-model construction](round2_construction.md), [independent review](round2_construction_review.md).
- [Charged connector proof](round2_global.md).
- [Commands, checks, and scope](round2_verification.md).

The new calculations and notes remain in this isolated local research
repository. Running Qiushi Sessions, services, environments, and the live
Skill have not been changed. The theorem-level deductions are distinguished
from model computations in their statements; comprehensive publication
novelty has not been established.
