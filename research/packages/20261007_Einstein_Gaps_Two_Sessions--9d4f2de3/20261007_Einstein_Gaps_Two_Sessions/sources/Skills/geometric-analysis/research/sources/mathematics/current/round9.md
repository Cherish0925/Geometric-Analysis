# Round 9: excluding the full free-torus connector and separating approximate inputs from exact solutions

21 September 2026.

The principal advance is a global nonexistence argument for the entire
previously open **free-torus, two-AH-end exact Einstein connector class**.
Nonzero twist and rotating orbit shape no longer evade the obstruction.
Two proofs are given: a Lorentzian construction with nonnegative null
Ricci curvature, and a four-dimensional minimal-surface argument using
the conserved torus charge.

The other two investigations make actual forward constructions and
variational distinctions on the fixed surface bundles. They solve two
blocks of a nonabelian system exactly and identify a harmonic-energy
quantity that separates the constructed inputs from any hypothetical
negative Einstein output. Neither supplies all-Einstein nonexistence
on those bundles. The unrestricted Yau26 problem remains open in this
work.

## 1. A global theorem beyond the OT and diagonal ansatz

Consider a complete four-metric on the interior of `[0,1] x T^3`, with

\[
\operatorname{Ric}_g=-3g,
\]

smoothly conformally compact at both boundary components. Suppose a
marked free isometric `T^2` action extends freely through the
compactification, with quotient an annulus.

**There is no such metric.** The conclusion now includes arbitrary
connection curvature and nonconstant, nondiagonal fibre shape. It does
not require flat conformal infinity or a nonnegative Yamabe conformal
class.

### Proof mechanism A: convert the twist into nonnegative null curvature

Choose a primitive circle. Its quotient metric `h`, lapse `V` and
connection curvature `F` are global, even when its principal bundle is
nontrivial. Instead of requiring a vacuum Lorentzian continuation of the
original metric, form a different, globally defined auxiliary metric

\[
\mathfrak g_0=-V^2dt^2+h\quad\hbox{on }\mathbb R\times N.
\]

For a null vector `Z=a E_0+X`, where `E_0` is timelike unit and
`|X|_h^2=a^2`, the full circle-reduction formulas give

\[
\boxed{
\operatorname{Ric}_{\mathfrak g_0}(Z,Z)
=V^2\left(
\frac{a^2}{4}|F|_{\rm tens}^2+
\frac12|\iota_XF|^2\right)\ge0.}
\tag{1}
\]

No twist is discarded from the original Einstein equations: it remains
on the right of (1), with favorable sign. The auxiliary metric is not
asserted to be vacuum Einstein. It needs only the null energy inequality.

Its optical completion is exactly `-dt^2+k`, with `k=V^{-2}h` smooth
on the compact quotient. This supplies global hyperbolicity, compact
causal diamonds, and compact spacelike cuts of both timelike conformal
boundaries. A finite optical path between them has a future timelike
lift, contradicting
[Galloway--Schleich--Witt--Woolgar, Theorem 2](https://arxiv.org/pdf/hep-th/9912119).

The full proof in [round9_connector.md](round9_connector.md) gives the
stronger statement: a conformally compact negative Einstein manifold
of dimension at least three, with a free isometric circle action
extending freely to the compactification, has connected boundary.
Bundle triviality, a global connection potential and torus symmetry
are unnecessary. Freeness throughout the compactification and the
dimension restriction remain substantive hypotheses.

### Proof mechanism B: a different minimal separator detects the charge

For the charged four-dimensional case, take a primitive circle with
nonzero conserved charge component `q_1`. Its quotient metric `h` has a
compact stable minimal surface `Sigma` between the two AH ends. The
circle lapse is a valid test function for its Jacobi operator, and

\[
\boxed{
J_\Sigma V=-V\left(
|\mathrm{II}|^2+\frac{V^2}{4}|F|_{\rm tens}^2
+\frac{V^2}{2}|\iota_nF|^2\right).}
\tag{2}
\]

Stability forces `F=0` on the separator. But its component on the
two-dimensional torus quotient is `q_1/(rho G_11)`, nowhere zero.
This is a contradiction. The charge-free case was already excluded
in round 8 by the shape-energy maximum principle.

[round9_riemannian.md](round9_riemannian.md) contains the complete
variational argument and its small-Ricci-error version:

\[
\frac{\int_\Sigma V^2\left(
|\mathrm{II}|^2+V^2|F|_{\rm tens}^2/4
+V^2|\iota_nF|^2/2\right)}{\int_\Sigma V^2}
\le2\epsilon,
\qquad\epsilon=\|g^{-1}(\operatorname{Ric}+3g)\|_\infty.
\tag{3}
\]

This controls an actual separator quantity for approximate connectors;
it is not yet a positive uniform lower bound for `epsilon`.

### Consequence for the research route

Trying additional rotating matrices, torus holonomies or charged local
necks cannot produce an **exact** complete connector within this whole
class. The analytic local charged germs remain valid: a stable
three-torus in a four-dimensional germ is not the globally obtained
stable two-surface in its circle quotient.

For the graph-manifold program, remaining possibilities include genuinely
small-error rather than exact connectors, loss of the free isometric
action, singular orbits, different end structures, and nonsymmetric
geometries. The theorem does not decide these possibilities and does not
assert nonexistence of every Einstein metric on a closed candidate.

## 2. Full-rank nonabelian seeds solve two equations exactly

Use the full unitary equation on `E=W=S_L^+`, with fixed background
spin-c connection on the source:

\[
F_A^+=\tau(\phi),\qquad D_A\phi=0.
\]

The trace of the quadratic map defines an intrinsic real isomorphism
`T:Herm_0(W)->i Lambda^+`. If a target determinant connection `B`
has nowhere-vanishing self-dual curvature, choose

\[
H=\big(tI+\mathcal T^{-1}(F_B^+)\big)^{1/2}>0.
\]

The algebraic map from traceless connection changes to the Dirac
equation is surjective wherever `H` has distinct positive eigenvalues.
A smooth global right inverse therefore constructs a unitary `A` with

\[
\boxed{
\det A=B,\qquad D_AH=0,\qquad
\operatorname{tr}(F_A^+-\tau(H))=0.}
\tag{4}
\]

For the actual almost-Kähler slow-twist metrics, the canonical Hermitian
determinant curvature is uniformly close to the nonzero product form.
Thus (4) applies on the same fixed surface bundles used in the
near-Einstein construction, including the noncommuting-twist examples.

The remaining equation is explicit:

\[
\big(F_{A_H+k}^+-\tau(H)\big)_0=0,
\qquad k\in\Gamma\ker(\mathcal L_H|_{\mathfrak{su}(2)}).
\tag{5}
\]

The kernel has real rank four. This is an actual partial solution of the
coupled system, not a parameter count. The full deformation index is
`-5 chi-7 tau`, negative on the candidate bundles, so a generic
regular-solution or ordinary-monopole persistence argument is unavailable.
Negative index alone does not prove nonexistence.

[round9_nonabelian.md](round9_nonabelian.md) proves the construction,
rank formulas, trace lower bound and index. It does not solve (5), bound
its residual uniformly, or transfer the construction to an arbitrary
hypothetical Einstein metric on the same manifold. Its separate source-
compatibility appendix is not used in any theorem in this summary.

## 3. A calibrated input family and an exact-output energy gap

Let `pi:E->B` be one of the fixed infinite-monodromy surface bundles,
and `b=pi^*e(TB)`. For a source metric `G`, minimize the energy of its
harmonic projection over all marked hyperbolic target structures:

\[
\Gamma(G)=\min_h\frac12\int_E|df_h|^2
                 -4\pi^2\|\mathsf H_G b\|_2^2.
\]

The actual area-preserving slow-twist metrics satisfy `Gamma(G_L)=0`
**exactly**: the global closed fibre area form calibrates the energy
minimum, and the pulled-back base area form is harmonic. There is no
remaining target-optimization problem for these inputs.

For any hypothetical `Ric_G=-G` metric on the same smooth bundle,
Bochner and Hodge decomposition instead give

\[
\frac12\int_E|df_h|^2-4\pi^2\|\mathsf H_G b\|_2^2
=\|f_h^*\omega_h+2\pi\mathsf H_G b\|_2^2
+\frac12\|\nabla df_h\|_2^2.
\tag{6}
\]

Equality would force finite monodromy, contrary to the actual Dehn
twist. Properness of target energy for each fixed source ensures that
the minimum is attained; hence `Gamma(G)>0`. The source dependence is
essential. This does not yield a positive lower bound over all source
metrics, or force all source metrics into the calibrated zero locus.

[round9_bundle.md](round9_bundle.md) also gives explicit two-orientation
monopole bounds on the Hodge term and exhibits the exact Ricci-error
cancellation on the input family. An auxiliary exact product-Einstein
example shows why uniformizing the fibres of a fixed projection cannot
silently be substituted for the intrinsic harmonic-map problem.

## 4. What now changes, and what remains decisive

The complete exact free-torus connector is no longer an unresolved
ansatz to keep extending. Its exclusion has two compatible proofs.
The global counterexample program must confront the approximate,
symmetry-breaking or other geometric alternatives explicitly.

On the closed surface bundles, the new exact seeds and calibrated
functional give concrete equations to investigate. The decisive
question is still whether **any** negative Einstein metric exists on
the same smooth manifold. A metric elsewhere in its space of metrics
is allowed by Yau26; neither small residual nor a gap from the current
input family excludes it.

All proofs, calculations and changes are local in this isolated
research worktree. [round9_verification.md](round9_verification.md)
records the checks and their scope. No installed Skill, active Session,
GUI service, shared environment or external repository was changed.
