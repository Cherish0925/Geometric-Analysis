# Yau26: an intrinsic near-Einstein gap and exact model completion

19 September 2026.

The principal advance in this round is a uniform **near-Einstein** gap,
not merely an obstruction to exact Einstein metrics. A spinor Hessian
estimate closes the critical monopole argument without a full-curvature
bound. In parallel, the complete double-cylinder construction is extended
from a quadratic repair to an exact Einstein family, and the connector
problem acquires a sharp physical-width constraint.

The working Yau26 question remains whether, in every dimension, some
dimension-only Ricci interval forces the same closed smooth manifold to
carry an Einstein metric. The results below concern explicit four-dimensional
classes and models. They do not settle either unrestricted four-dimensional
sign branch or the all-dimensional question.

## 1. A uniform gap across the critical blow-up ratio

Let \(X\) be a closed minimal complex surface of general type with
\(b_+(X)>1\), let \(A=c_1^2(X)>0\), and let
\[
M=X\#k\overline{\mathbb{CP}}^{\,2},\qquad k\ge0.
\]
For every smooth metric set
\[
\delta_-(g)=\|g^{-1}\operatorname{Ric}_g+I\|_{L^\infty,\mathrm{op}}.
\]
The [family theorem](round3_joint_gap.md) proves that a universal \(c_*>0\)
satisfies
\[
\boxed{\delta_-(g)^2+
       \left(\frac13-\frac{k}{A}\right)_+\ge c_* .}
\tag{1}
\]
The constant is independent of the topology, metric, volume, diameter,
injectivity radius, full curvature, curvature derivatives and Sobolev
constant. No bound on \(\chi(M)/A\) is used. Its optimal value is not
computed.

In particular, if \(k/A\ge1/3-c_*/2\), then every metric has
\(\delta_-(g)\ge\sqrt{c_*/2}\). Thus these near-critical blow-ups cannot
provide negatively Ricci-pinched counterexample sequences. This is
stronger than proving that they have no exact Einstein metric.

### Why the formerly missing estimate now closes

The rescaled Seiberg--Witten solution supplies a bounded spinor \(\Phi\)
and a self-dual form \(\psi\), with \(\rho=|\Phi|^2=|\psi|\). Near the
critical curvature budget,
\[
A_\psi=\frac{\rho^2}{24}I-\frac18\psi\otimes\psi
\]
approximates \(W^+\) in normalized \(L^2\). The preceding round had
proved two facts about \(J_\psi=\operatorname{div}W(A_\psi)\):
its weak norm tends to zero, while its average squared norm must tend to
\(1/16\). These facts alone do not contradict one another.

The [intrinsic proof](round3_rigidity.md) supplies the extra derivative.
The [monopole input derivation](round3_monopole_input.md) supplies the
rescaling, quantitative deficits, amplitude and spectral estimates in
full, without requiring access to the live Skill.
For a compatible connection on a Hermitian bundle over a closed
four-manifold, with curvature \(F\), \(\operatorname{Ric}\ge-rg\), and
\(K=\|u\|_\infty\),
\[
\|\nabla u\|_4^2\le4K\|\nabla^2u\|_2,\qquad
\|\nabla^2u\|_2^2
\le2\|\nabla^*\nabla u\|_2^2+
2r\|\nabla u\|_2^2+17K^2\|F\|_2^2 .
\tag{2}
\]
These follow by integration by parts, with neither a Sobolev inequality
nor a derivative of \(F\). In the positive-spinor connection the
anti-self-dual Weyl block acts trivially. Its remaining curvature is
controlled in average \(L^2\) by the monopole equation and the determinant
line's Chern--Weil identity. The actual class square, not its positive
projection, enters this last identity.

Consequently \(\nabla^2A_\psi\), and hence \(\nabla J_\psi\), is controlled
in average \(L^2\). The weak Bianchi equation may now be tested against
\(J_\psi\) itself. It forces
\[
\fint |J_\psi|^2\longrightarrow0,
\]
contradicting the weighted Hodge identity's value \(1/16\). This
argument occurs on each original metric. It does not require coordinate
compactness, noncollapse, smoothing, or passage to a geometric limit.

Quantitatively, for an actual monopole class \(a\), define its
scalar--Weyl deficit \(\Delta\) and calibration integral \(d_{\rm cal}\)
as in the intrinsic proof. It obtains
\[
\left(1+\frac{(-a^2)_+}{V}\right)
\left[\delta_-^2+\frac{\Delta+d_{\rm cal}}{V}\right]\ge c>0.
\tag{3}
\]
For the blow-up family, sign averaging selects a class with
\((a^+)^2\ge A\), while \(a^2=A-k>0\) follows from sufficiently small
Ricci defect. The topological budgets give
\[
\delta_-^2+\frac{\Delta+d_{\rm cal}}V
\le760\left[\delta_-^2+(1/3-k/A)_+\right],
\]
which proves (1), including varying topology.

The [general monopole extension](round3_general_monopole.md) states
the exact additional class-square hypothesis needed for other families.
It also gives a universal gap in the eligible connected-sum sign-class
setting; class existence remains a genuine hypothesis, not a consequence
of the intersection numbers alone.

## 2. An exact complete Einstein family, not just a small residual

On \((\mathbb R\times S^1)^2\), start with
\[
g_0=dt^2+\cosh^2t\,dy^2+du^2+\cosh^2u\,dx^2 .
\]
The [construction theorem](round3_construction.md) integrates all eight
bounded invariant Jacobi directions under consideration into a small
real-analytic family
\[
G[z]=g[z]+k[z],\qquad
\operatorname{Ric}_{G[z]}=-G[z],\qquad k[z]=O(|z|^2).
\tag{4}
\]
The metrics are smooth, complete and uniformly equivalent to \(g_0\).
Their asymptotic cylinder data and marked shears are specified explicitly.
The theorem does not claim that all eight parameters are inequivalent
under unrestricted diffeomorphisms.

Three steps turn the previous quadratic correction into (4):

1. In the compactified radial square, the **entire** Ricci residual
   vanishes on every face. It factors as
   \(\operatorname{sech}t\,\operatorname{sech}u\,R[z]\),
   where \(R[z]\) is smooth and \(O(|z|^2)\). Higher nonlinear terms
   therefore remain in the inverse's target space.
2. The invariant linearized operator has an inverse in weighted
   \(H^{m+2}_{1/4}\to H^m_{1/4}\). Conjugation retains a coercive
   \(L^2\) margin \(1/16\). A moving background gauge avoids a
   nonintegrable gauge residual from the nondecaying parameters.
3. A Banach-space contraction produces the correction. Contracted
   Bianchi and the negative Ricci bound eliminate the gauge term,
   giving the actual Einstein equation.

This establishes exact nonlinear solvability of the complete local model.
It is not yet an Einstein metric on the closed surface bundle \(E_D\).

### What its second variation requires of a global construction

The correction has explicit fluxes against the two length receivers.
For slopes \(a_1,b_1,A_1,B_1\),
\[
I_1=\frac{\pi^2}{8}(a_1^2-3b_1^2-A_1^2-B_1^2),\qquad
I_2=\frac{\pi^2}{8}(A_1^2-3B_1^2-a_1^2-b_1^2).
\tag{5}
\]
The four outward receiver fluxes of the quadratic correction sum to
\[
-I_1-I_2=\frac{\pi^2}{2}(b_1^2+B_1^2).
\tag{6}
\]
Bounded homogeneous Jacobi corrections can redistribute the two end
fluxes of a receiver, but cannot change their sum. The
[matching lemma](round3_matching_next.md) gives the resulting necessary
equations with prescribed exterior fluxes and end-modulus shifts.
Zero exterior response is a special case, not an assumption available
for an arbitrary closed \(E_D\) construction.

These are second-variation statements. Passing a finite-parameter
nonlinear flux through an infinite-boundary limit requires additional
decay estimates not supplied by the present weighted inverse.

For the original balanced closed \(E_D\) family, the same investigation
identifies a further necessary equation at the first potentially
admissible larger correction scale. If an exact correction is
\(h_\varepsilon=\varepsilon^{3/2}U_\varepsilon\), with uniformly bounded
geometric \(C^2\) norm of \(U_\varepsilon\), then its actual global
horizontal TT detector \(Q_\varepsilon\) must satisfy
\[
\frac1{2\beta}\int_{E_D}
\left\langle D^2(\operatorname{Ric}+g)_{G_\varepsilon}
 [U_\varepsilon,U_\varepsilon],Q_\varepsilon\right\rangle
\longrightarrow\frac1{2\pi^2}.
\tag{6a}
\]
The exterior response and this global quadratic form must be evaluated;
neither is determined by the bounded kernel on the thin local model.

## 3. A sharp connector-width obstruction and its exact limitation

Consider a complete four-manifold with two exact expanding flat ends,
joined by a compact bridge of physical width \(L\). If
\(\operatorname{Ric}\ge-(3+\epsilon)g\), the
[index-form argument](round3_global.md) proves
\[
\boxed{
L>
\frac{2}{\sqrt{1+\epsilon/3}}\,
\operatorname{artanh}\!\frac1{\sqrt{1+\epsilon/3}}
=\log(12/\epsilon)+O(\epsilon|\log\epsilon|).
}
\tag{7}
\]
The strict inequality uses smooth attachment to the exact ends.
The estimate needs no torus symmetry and no boundary noncollapse.
For \(\epsilon=10^{-6}\), it requires \(L>16.3004146581\).
At zero defect no finite bridge of this end type exists.

The same argument gives signed Ricci-source moment conditions along an
actual minimizing geodesic. Thus it constrains where the negative
directional defect must occur, not just its absolute size.

A smooth warped-product family approaches equality in (7) under the
one-sided Ricci bound. Its tangential Ricci defect, however, remains
of order one. This proves that the width argument cannot by itself
exclude all connectors with a sufficiently long bridge. A uniform gap
for the full two-sided Ricci condition must use the remaining Ricci
equations or a genuinely global matching constraint.

## 4. What has changed in the research

The strongest previously open connection closed here is the intrinsic
monopole argument: the near-critical family gap no longer depends on a
full-curvature bound. The construction result also advances in kind,
from a formal quadratic repair to a complete exact solution family.

These two conclusions do not automatically combine into a Yau26
counterexample or an unrestricted existence theorem. The protected
monopole topologies, the noncompact double-cylinder model, the closed
surface bundles and the marked orbifold resolutions are different
objects. A solution of the original problem must still connect the
pointwise pinching and global Einstein question on the same closed
smooth manifold, or establish a dimension-only principle covering
all admissible manifolds.

The resulting next mathematical questions are concrete:

- Determine the exterior adjoint receiver terms and the finite-parameter
  matching map for a specified closed \(E_D\). The newly computed
  interior charges cannot be set to zero by fiat.
- Determine which topological families outside the present monopole
  regime admit a replacement for the bounded auxiliary-field estimate
  (2), or construct pinched metrics on a topology with a global
  Einstein obstruction.
- For graph connectors, address the tangential and mixed Ricci equations
  together with physical end lattices and volume budgets. Lower Ricci
  and an increasingly long neck alone are insufficient.

The detailed [verification record](round3_verification.md) distinguishes
analytic proofs, independent derivations and executable algebra checks.
All work is local to this research branch. The existing Skill and live
research Sessions are unchanged.
