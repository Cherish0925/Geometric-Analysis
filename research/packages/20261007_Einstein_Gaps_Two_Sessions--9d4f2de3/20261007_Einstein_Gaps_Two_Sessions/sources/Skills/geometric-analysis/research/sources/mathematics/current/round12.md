# Round 12: exact global gauge data and compulsory symmetry breaking

21 September 2026.

The fixed closed manifolds constructed in Round 11 now have two further
global descriptions: their ordinary Seiberg--Witten basic classes can
be computed completely, and any Einstein metric on them must have no
continuous local symmetry anywhere. A separate nonlinear collar
identity measures the boundary change required by a marked mapping
class. These statements concern the same smooth objects that already
carry a sequence with vanishing pointwise Ricci defect.

## 1. The object and the Einstein question

Self-glue the two boundary components of
\(F_{h,2}\times\Sigma_g\), \(h\ge1\), \(g\ge2\), by
\[
(\phi,x)\longmapsto(-\phi+u(x),f(x)),
\qquad [u]\in H^1(\Sigma_g;\mathbb Z)\setminus\{0\}.
\]
The resulting manifold \(M(h,g;u,f)\) is closed and aspherical, with
\(\chi=4h(g-1)>0\) and \(\tau=0\). Round 11 constructs metrics
\[
\|G_\ell^{-1}\operatorname{Ric}_{G_\ell}+3I\|_\infty\to0,
\qquad \operatorname{Vol}(G_\ell)=4\pi^2\chi/9.
\]
Rescaling by three gives the negative normalized Yau26 input.
No finite cover is Kähler. Positive Einstein and Ricci-flat metrics
are excluded, but a general negative Einstein metric is not.

## 2. Complete ordinary basic-class calculation

The two symplectic orientations come from a splitting
\(TM=E\oplus F\). Write \(x=e(E)\), \(y=e(F)\),
\(a=x+y\), \(b=x-y\). The
[global calculation](round12_global.md) proves
\[
x^2=y^2=0,\quad xy=\chi,
\qquad a^2=2\chi,\quad a\cdot b=0,\quad b^2=-2\chi,
\]
where products use the positive symplectic orientation, and
\[
\boxed{\mathcal B(M)=\{a,-a\},\qquad
       \mathcal B(-M)=\{b,-b\}.}
\tag{1}
\]
These are the full ordinary basic first-Chern sets, not merely two
known elements of larger uncomputed sets. No invertibility assumption
on \(I-f_*\) is used.

The proof couples geometric saturation to the actual gluing topology.
The constructed sequence has scalar energy tending to
\(64\pi^2\chi\). Monopole estimates and the expected dimension
therefore force every ordinary basic class \(c\) to satisfy
\(c^2=2\chi\), and harmonic projection gives
\(|a\cdot c|\le2\chi\). Embedded product tori eliminate its mixed
block components. Mayer--Vietoris writes \(c=ta+r\), where the neck
subspace containing \(r\) is isotropic. The intersection inequalities
force \(t=\pm1\) and \(a\cdot r=0\). The symplectic form has the
same proportional restriction to the neck as \(a\), so also
\(r\cdot[\Omega]=0\). Taubes's equality theorem then removes \(r\)
integrally.

The same energy sequence also determines LeBrun's monopole minimax
and convex-hull quantities:
\[
\boxed{\alpha^2(M)=\beta^2(M)=2\chi(M)}
\tag{2}
\]
in both orientations. Thus merely searching for a larger ordinary
basic-class square or a larger value of these two monopole invariants
cannot strengthen the obstruction for this family. Other gauge data
are not classified by (1)--(2).

## 3. Every exact Einstein output must break all local symmetries

The [symmetry theorem](round12_symmetry.md) gives
\[
\boxed{\operatorname{Isom}(\widetilde M,\widetilde g)
       \text{ is discrete for every Riemannian metric }g.}
\tag{3}
\]
For an Einstein metric, it follows that
\[
\boxed{\text{there is no nonzero local Killing field on any open set}.}
\tag{4}
\]
The conclusion applies to arbitrary metrics of the indicated kind on
every finite cover as well.

Here the new application joins three ingredients. The Bass--Serre
description excludes every normal abelian subgroup by a common-axis
argument. Positive Euler characteristic and the virtual Kähler
obstruction exclude every finite-cover product decomposition. The
Farb--Weinberger theorem then converts nondiscrete universal-cover
symmetry into a locally symmetric geometry, all four-dimensional
possibilities being excluded by the same topology. Finally Einstein
analyticity and Nomizu extension convert a local Killing field into
a global one on the universal cover, contradicting (3).

This is stronger than excluding one invariant neck formula: no exact
closed Einstein completion can preserve even an open part of the
circle symmetry. The near-Einstein inputs do have such open symmetric
regions, since their smooth local symmetries need not continue
analytically through the whole manifold. The argument does not give
a positive distance to nonsymmetric Einstein metrics.

## 4. A quantitative mapping-class obstruction on a collar

For an abstract circle-invariant collar
\[
g=dt^2+h_t+a^2\theta^2,\qquad
S=\tfrac12h_t^{-1}\partial_t h_t,\quad H=\operatorname{tr}S,
\quad d\theta=dt\wedge\beta+B,
\]
the [full Ricci calculation](round12_repair.md) gives
\[
\operatorname{Ric}(U,U)-\operatorname{Ric}(T,T)
=H'-a_tH/a+|S|^2-\Delta_{h_t}a/a
 +a^2\bigl(|\beta|^2+|B|^2_{\rm tensor}/4\bigr).
\tag{5}
\]
When \(a=a(t)\) and the metric is Einstein, \(H/a\) is
nonincreasing. The weighted energy in this identity controls marked
Teichmüller displacement. If \(a\) is within a factor \(\Lambda\)
of the round11 cosh radius and both face mean curvatures are at most
\(\eta\), then
\[
\boxed{\eta\ge\frac{\sqrt3}{4\Lambda^2}
     d_{\mathcal T}([h_-],[h_+])^2.}
\tag{6}
\]
The lower bound is independent of the shrinking circle radius. For
pseudo-Anosov self-gluing, the displacement is bounded below by the
logarithm of its stretch factor. The result permits arbitrary fibre
metrics and both electric and magnetic connection curvature within
its stated normal form.

If the orbit radius varies over the fibre, the Laplacian term in (5)
cannot be discarded. Nevertheless, in the pointwise common-area
sector \(H=0\), integration over the closed fibre forces
\(S=d\theta=0\) for any Einstein solution, even with such a variable
radius. The remaining geometry is locally a product of two equal
negative-curvature surfaces.

Equation (6) remains useful on collars without the topology of our
closed examples. For our examples, (4) already excludes all exactly
invariant closed completions, and the next repair problem must retain
the full nonsymmetric tensor equation.

## 5. What this changes in the Yau26 research

There is now a fixed family for which pointwise near-Einstein inputs,
the full ordinary basic set, and strong restrictions on every possible
exact output are all described on the same smooth manifold. The two
most direct remaining approaches are different:

* construct a fully nonsymmetric negative Einstein metric on one of
  these manifolds, using the actual degenerating inverse and all
  coupled angular modes;
* obtain a global obstruction that applies to nonsymmetric negative
  Einstein metrics, using information not exhausted by (1)--(2).

Neither the nonattainment of the scalar-energy infimum nor the absence
of local Killing fields excludes the latter metrics by itself. The
full-curvature infimum from Round 11 is attained exactly when such an
Einstein metric exists. Deciding that attainment, or the full equation
directly, would settle the negative branch on this concrete object.
A negative-branch counterexample alone would not negate the original
two-sign interval statement.

The [exact Schoen-surface control](round12_control.md) also shows why
ordinary monopole existence and zero signature cannot automatically
be promoted to locally symmetric Einstein uniformization. The
nonabelian route has to satisfy its additional curvature equations,
not just inherit an ordinary invariant.

The [explicit Clifford-block calculation](round12_uniformization.md)
now supplies those equations for one precisely specified ansatz. It
derives the central curvature term and the positive graded Chern
identity directly. On a closed Einstein four-manifold with
\(\chi>0\), \(\tau=0\), this particular system admits a solution
exactly in the constant-negative-sectional-curvature case. Ordinary
positive-square monopoles cannot be inserted into it unchanged:
their harmonic trace violates its exact determinant equation. This
settles the proposed transfer for this ansatz, without asserting
that all other nonabelian formulations have the same solution set.

Proof checks, coordinate recomputations and their precise scope are
recorded in [the verification note](round12_verification.md).
