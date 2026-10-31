# Step 18: global corrections, positive-branch crux, and allocation

Session S0910A02, Agent1/Orchestrator, Explore.

## 0. Purpose

Step 17 produced useful mathematics (separated exact rigidity, the diagonal
`T^k` determinant identity, and a route assessment), but its route assessment
contained two decision-level errors.  This note repairs those errors and resets
A02's near-term allocation without changing the active Yau-26 target.

The original target remains the full statement: for every dimension `n >= 2`,
find dimension-only constants `c_n < C_n` whose Ricci pinching forces the
underlying smooth closed connected manifold to admit some Einstein metric, or
strictly refute that statement.  A four-dimensional positive-branch volume-gap
or toric theorem would be only a component of this target, not a final proof.

## 1. Correction 1: Hitchin--Thorpe is forced by tight pinching, not a Bridge-3 obstruction

Step 17's relay treated `#_5 CP^2` as evidence that the finite-list-to-Einstein
Bridge 3 is fundamentally obstructed by Hitchin--Thorpe.  That is backwards for
the pinched class.

The Step 2 sign-blind Chern--Weil lemma, reaffirmed in Steps 4--5, says:
if a closed oriented four-manifold satisfies
\[
  \|\operatorname{Ric}_g-\sigma g\|_{\operatorname{op}}\le \varepsilon,
  \qquad \sigma\in\{+1,-1\},
\]
with
\[
  \varepsilon < \frac{1}{1+\sqrt 3}\approx 0.366025,
\]
then
\[
  2\chi(M)>3|\tau(M)|.
\]
Indeed, in either sign branch the scalar curvature obeys
`|s| >= 4(1-epsilon)`, while
`|E|^2 <= 4 epsilon^2`.  The self-dual and anti-self-dual Chern--Weil formulae
\[
  2\chi\pm3\tau
  =\frac1{4\pi^2}\int_M\left(2|W^\pm|^2+\frac{s^2}{24}
          -\frac{|E|^2}{2}\right)d\mu
\]
therefore give
\[
  2\chi\pm3\tau \ge
  \frac{\operatorname{Vol}(M)}{4\pi^2}
  \left[\frac23(1-\varepsilon)^2-2\varepsilon^2\right] >0.
\]
Thus Hitchin--Thorpe violators and equality cases cannot carry arbitrarily
tight normalized positive or negative Ricci pinching at all.

Consequences:

* `#_5 CP^2` (`chi=7`, `tau=5`, `2chi=14<15=3|tau|`) and `#_4 CP^2`
  (Hitchin--Thorpe equality) are excluded from the pinched class for small
  `epsilon`.  They are not candidate counterexamples to `P_4^+` or `P_4^-`.
* The phrase in Step 17 that Bridge 3 is "fundamentally obstructed by
  Hitchin--Thorpe" should be deleted.  Tight pinching already performs the
  Hitchin--Thorpe filtering before any finite list of candidate diffeotypes is
  reached.
* What remains of Bridge 3 in the positive branch is not the arbitrary
  four-dimensional Einstein existence problem.  It is a **pinching-rigidity**
  problem: determine whether the tightly pinched class is forced into the
  diffeotypes already known or expected to admit positive Einstein metrics, or
  at least into a finite set on which Einstein existence can be settled by
  separate, topology-specific arguments.

### 1.1. Seiberg--Witten/monopole obstruction scope under positive pinching

Positive branch pinching gives positive scalar curvature for small `delta`.
Consequently, the standard Seiberg--Witten/monopole obstructions used by
LeBrun-type non-Einstein examples are not directly available on a positive-
pinched counterexample: the usual invariants/monopole classes that give
curvature inequalities are incompatible with the existence of sufficiently
positive scalar curvature, modulo the standard `b_+` and wall-crossing caveats.
This does **not** prove that no exotic obstruction exists, but it changes the
research character: a refutation of `P_4^+` would require a new nonexistence
mechanism beyond the familiar Hitchin--Thorpe and SW/monopole toolkit, while a
proof route should exploit the fact that tight positive pinching automatically
filters out those known obstructed manifolds.

Current positive-branch enemies are therefore not HT violators.  They include:

* the large-topology family `#_k(S^2 x S^2)` for `k >= 2`, which has `tau=0`,
  `chi=2k+2`, admits positive Ricci metrics by Sha--Yang/Burdick-type surgery
  results, and is not known in this record to admit Einstein metrics for large
  `k`;
* finite strict-HT examples such as `#_3 CP^2` (`chi=5`, `tau=3`, `2chi=10>9`),
  where positive Ricci is known for connected sums in the sourced survey but
  Einstein existence is not settled here;
* any future strict-HT, positive-scalar, no-Einstein smooth structures not
  eliminated by existing invariants.

## 2. Correction 2: the toric program is direct for the crux family

Step 17 demoted the invariant program because a general-to-invariant bridge is
missing.  That demotion is valid only for a **proof that all** simply connected
pinched collapse is toric.  It is not valid for the central construction/obstruction
question:

\[
  \text{Do } \#_k(S^2\times S^2) \text{ carry } \delta_k\text{-pinched metrics with }\delta_k\to0?
\]

This question may assume torus symmetry for free when looking for a construction:
Orlik--Raymond theory and the sourced toric paper describe closed simply
connected toric four-manifolds by labeled polygons; the paper explicitly states
that topologically four-manifolds admitting `T^2` actions are connected sums of
`S^4`, `CP^2`, `\overline{CP}^2`, and `S^2 x S^2`, and that diagonal `T^2`
actions on connected sums of `S^2 x S^2` inherit Sha--Yang positive-Ricci
metrics (Knowledge object `Toric-Einstein-4-manifolds...`, lines 41 and 84--86).
For `#_k(S^2 x S^2)`, the polygon has
\[
  m=\chi=2k+2
\]
vertices/rods.  A toric construction on these manifolds would be a construction
on the actual crux topology, not a model requiring Bridge 1.

Therefore A02 should not continue refining invariant geometry merely as a
"laboratory".  It should ask the direct, allocation-deciding question:

> Construct or obstruct a sequence of smooth `T^2`-invariant metrics on the
> `(2k+2)`-rod toric models of `#_k(S^2 x S^2)` with
> `||Ric-g||_op -> 0` and collapsing total volume (or otherwise escaping the
> simply-connected volume gap).

Either outcome matters:

* **BREAK of the volume-gap route:** a successful toric pinched-collapse
  construction would invalidate the simply connected volume-gap amplifier as a
  route to `P_4^+`.  It would not by itself refute Yau-26, because the record
  does not prove that `#_k(S^2 x S^2)` admits no Einstein metric.  It would
  instead reduce the positive branch to a hard Einstein-existence/topology
  question with no current obstruction, so A02 should then reallocate heavily to
  the negative branch and higher-dimensional mechanisms.
* **BUILD of an invariant gap:** a proof that smooth toric rod/holonomy
  matching cannot realize `O(delta)` Ricci error with total flux tending to zero
  would give a genuine `chi`-uniform invariant volume-gap theorem.  Only then
  would the expensive general-to-invariant/collapse bridge become worth major
  effort.

## 3. What exactly should be tested in the toric crux

For a polar, twist-free, local diagonal `T^2` metric
\[
  g=g_B+p^2d\theta^2+q^2d\phi^2,
  \qquad w=pq,
  \qquad v=\log(p/q),
\]
the exact Einstein system from Steps 12--14 becomes a pinched system of
inequalities.  On the principal orbit region, the normalized vertical Ricci
eigenvalues are
\[
  r_p=-\Delta\log p-|\nabla\log p|^2
      -\langle\nabla\log p,\nabla\log q\rangle,
\]
\[
  r_q=-\Delta\log q-|\nabla\log q|^2
      -\langle\nabla\log p,\nabla\log q\rangle.
\]
Equivalently,
\[
  r_p+r_q=-\frac{\Delta_B w}{w},
  \qquad
  r_p-r_q=-\frac{1}{w}\operatorname{div}_B(w\nabla v).
\]
Positive `delta`-pinching requires
\[
  |r_p-1|\le\delta,
  \qquad |r_q-1|\le\delta,
\]
so
\[
  2(1-\delta)\le -\Delta_B w/w\le 2(1+\delta),
  \qquad
  |\operatorname{div}(w\nabla v)|\le 2\delta w.
\]
The horizontal block is
\[
  \operatorname{Ric}^H
  =K_B g_B-
  \left[\nabla^2\log w+\tfrac12(d\log w\otimes d\log w+dv\otimes dv)\right],
\]
and its two eigenvalues must also lie in `[1-delta,1+delta]`.  In the exact
case, tracing and taking the traceless part recover
\[
  K_B=\tfrac14(|\nabla v|^2-|\nabla\log w|^2),
\]
and the Step-14 traceless equation.  In the pinched problem these are `O(delta)`
operator inequalities, not equalities.

The Step-15 constant-edge model remains the leading formal enemy:
\[
  K_B|_{\text{rod}}=-A,
  \qquad Q''+(1+2A)Q=0,
  \qquad Q(0)=Q(L)=0,
  \quad Q'(0)=1,\ Q'(L)=-1,
\]
which gives
\[
  L=\pi/\sqrt{1+2A},
  \qquad \Phi=\int_0^LQ(s)ds=\frac{2}{1+2A}.
\]
Taking `A ~ m^2` makes the total formal flux `m Phi ~ 1/m`, hence formal
volume collapse.  Step 17's separated SdS rigidity theorem does not rule this
out: it concerns a cohomogeneity-one two-bolt family where the **same** circle
collapses at both ends; a toric polygon rod has adjacent fixed points and
primitive circle labels changing from edge to edge.  The Step-15 rod equation
already includes smooth endpoint slopes along the rod.  The unresolved issue is
whether the full four-dimensional Ricci pinching inequalities and global smooth
labeled-polygon closure allow this many-rod profile with `O(delta)` error.

Important scope caveat: the diagonal `(p,q)` formulation is global only for
suitably alternating rod labels.  Before a numerical construction is trusted,
one must verify that the chosen alternating labeled `(2k+2)`-gon is indeed
`#_k(S^2 x S^2)` (or another explicit crux topology), and that the global fiber
matrix/slope conventions really define a smooth metric.  For arbitrary toric
polygons one may need a non-diagonal fiber matrix `h_{IJ}`; the determinant
identity survives in the general invariant setting, but the full `(w,v)` system
must then be replaced by matrix equations.

## 4. Repositioning the orbifold/ALE bubble-tree route

The TTCS generator's orbifold/ALE route remains valuable, but it should not be
the immediate A02 main line for the crux family.

* It naturally addresses the **noncollapsed** approximate-to-exact bridge:
  near-Einstein noncollapsed sequences may converge to Einstein orbifolds, and
  ALE desingularization/DeTurck--Lichnerowicz analysis can decide whether a
  near-Einstein smoothing is correctable to an exact Einstein metric.
* Its first real input is not the Lichnerowicz spectrum.  Before spectrum/residual
  asymptotics are load-bearing, one needs a weighted normal form and annular
  closeness for `C^0`-pinched metrics.  Step 11 disproved pointwise Ricci-only
  epsilon-regularity, so the needed normal-form theorem cannot be assumed.
* It does not attack the collapsed regime where the `#_k(S^2 x S^2)` volume-gap
  crux must live if the Step-9 dichotomy is sharp.

Thus the bubble-tree route should be kept as a parallel/noncollapsed bridge,
not started prematurely as the main replacement for the toric crux.

## 5. Correction to the connected-sum neck heuristic

Step 17's neck conclusion was over-general.  The statement
`Ric_rr <= 0 at the minimum of a rotationally symmetric neck` is true for a
very special warped-product neck, but it cannot be promoted to a theorem that
Sha--Yang positive-Ricci connected sums have a fixed pinching gap.  Sha--Yang
metrics themselves have `Ric>0`, and under `Ric>0` there are no stable two-sided
minimal hypersurfaces of the naive kind.  If a quantitative handle anisotropy
estimate for `#_k(S^2 x S^2)` exists, it must be proved on actual handle/toric
geometry or extracted from the full Ricci inequalities; it cannot be asserted
from the symmetric-neck toy model.

## 6. Higher-dimensional note

A four-dimensional positive-pinched metric produces product positive-pinched
metrics in dimensions `n >= 6`:
if `(M^4,g)` satisfies `||Ric_g-g||_op <= delta` and
`S^{n-4}(sqrt(n-5))` is normalized so `Ric=g` (requiring `n-4 >= 2`), then
\[
  (M^4,g)\times S^{n-4}(\sqrt{n-5})
\]
has the same positive pinching error.  This shows that the four-dimensional
pinched class injects into higher-dimensional pinched **input** classes for
`n>=6`.

Two caveats are essential:

* this product observation does not cover `n=5`, since `S^1` has Ricci zero;
* it does not propagate Einstein **nonexistence** without a separate theorem that
  the product smooth manifold admits no Einstein metric of any sign.  Such a
  theorem is not available in the record.

So 4D work is a necessary component and can generate higher-dimensional tests,
but `n>=5` still needs its own mechanisms rather than an automatic extension of
the toric or product argument.

## 7. Allocation after the corrections

The best near-term A02 allocation is now:

1. **Primary A02 target: the toric pinched crux on `#_k(S^2 x S^2)`.**  Try to
   construct or obstruct smooth `T^2`-invariant positive-pinched collapsing
   metrics on `(2k+2)`-rod models.  This is direct, not merely a symmetry
   laboratory.
2. **First technical checkpoint:** verify the chosen labeled-polygon model and
   decide whether a global diagonal/polar ansatz is legitimate.  If not, move to
   a non-diagonal fiber-matrix formulation while retaining the determinant
   vertical trace.
3. **First computational checkpoint:** implement the pinched Ricci residual for
   a small but nontrivial toric family (`m=6,8,10`), initialized by the Step-15
   high-negative-edge profiles, and minimize the `C^0` operator Ricci defect at
   fixed small total flux.  A trend `delta_m -> 0` would break the volume-gap
   route; a persistent defect tied to rod holonomy or horizontal pinching would
   identify the obstruction to prove.
4. **Parallel monitoring:** A01/A03's negative-branch cutoff-flow program now has
   a precise remaining analytical object (the `chi^2`-weighted transition-inclusive
   continuation theorem).  Do not treat it as complete until that theorem is
   proved and independently checked.
5. **Deferred but live:** orbifold/ALE bubble-tree analysis for noncollapsed
   near-Einstein sequences should begin only after its annular weighted-normal-form
   input is specified; higher dimensions require a separate route, with the
   product injection above as a test generator but not a proof.

This corrected allocation preserves the exact Yau-26 target while preventing
two forms of drift: using HT violators as false positive-branch enemies, and
discarding the toric work precisely where it directly addresses the main known
crux family.
