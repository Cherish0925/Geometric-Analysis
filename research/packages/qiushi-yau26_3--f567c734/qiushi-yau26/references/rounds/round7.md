# Global compatibility, gauge detectors, and harmonic separation

20 September 2026. This continuation changes the focus from the size of
a local repair neighbourhood to restrictions on complete geometries and
the actual smooth manifolds carrying the inputs. It does not settle a
Yau26 branch. All work is local to this research worktree; no live Session,
service, shared environment or installed Skill was changed.

## 1. A compatibility law beyond A1 and Eguchi--Hanson

[The concentration theorem](round7_endpoint.md) applies whenever a fixed
closed smooth manifold admits genuine pointwise near-negative-Einstein
metrics converging off vanishing-volume replacement regions to a fixed
Einstein orbifold, with the stated exterior curvature-moment convergence.
It does not assume an ALE model for the replacement.

Write T=2 chi+3 tau, let V0 denote bulk volume, and set

\[
 J_0=\frac1{72\pi^2}\int_{\mathcal O}(4+\sqrt6|W^+|)^2.
\]

If E is the limiting concentrated self-dual Weyl energy and alpha^2
the all-monopole minimax invariant, then

\[
 T=T_0+\frac E{2\pi^2},\qquad
 \alpha^2\le\min\left\{\frac{V_0}{2\pi^2},
                         J_0+\frac E{12\pi^2}\right\}.
\]

The decisive identity, with D=J0+E/(12 pi^2), is

\[
 \boxed{T-\frac23D=
 \frac4{9\pi^2}\left[
   \int_{\mathcal O}\left(|W^+|-\frac1{2\sqrt6}\right)^2+E
 \right].}
\]

Concentrated energy enters the topology and the monopole upper bound
with ratio six. Thus it cannot push the standard locally symmetric
sources toward the critical ratio 2/3. When alpha^2>0, every such
resolution of a negative locally symmetric four-orbifold has
T/alpha^2>=3/4, in either orientation. In the complex orientation of
negative Kähler--Einstein bulk the stronger bound is 1+E/V0.

This eliminates a broad proposed connection, not merely a few node
configurations. Opposite-oriented nonsymmetric Kähler--Einstein bulk
has a more precise necessary locus: its Chern slope would have to tend
to 32/11, its Weyl modulus variance and concentrated-energy fraction
would have to vanish, and actual monopole capacity would have to
saturate. The already derived integral gap forbids this with sufficient
special classes or a uniform class-square bound. Therefore the slope
is not a recipe for violating that theorem or a constructed counterexample.

## 2. What the actual Davis resolutions cannot be detected by

[The topology note](round7_topology.md) concerns the marked resolutions
of the 122-node Davis orbifold. With m positive bolts,

\[
 \chi=196,\quad\tau=2m-122,\quad b^+=36+m.
\]

The inherited log-Weyl construction and the classical scalar--Weyl
bound force each monopole class to satisfy a^2<=104/3+m. A special
class also has a^2>=26+6m. These two conditions and characteristic
parity leave only

\[
 (m,a^2,d,\operatorname{ind}_{\mathbb C}D_a)
       =(0,30,1,19)\quad\hbox{or}\quad(1,32,0,19).
\]

For the all-negative resolution, the possible ordinary Bauer--Furuta
target is pi^35(CP18)=0, by the standard odd-index computation.
For every positive-bolt resolution the known BF adjunction inequality
already gives vanishing. Thus all ordinary numerical SW and ordinary
S1-equivariant BF invariants vanish on these fillings, in both
orientations. The additional deduction is the all-negative case and
the restriction on special classes; the positive-bolt consequence is
not claimed as a new adjunction theorem.

This concerns the actual smooth types, not hypothetical intersection
forms. It shows why simply replacing SW by its ordinary stable
cohomotopy refinement cannot complete their Einstein nonexistence
argument. It does not show that every monopole class, every refined
invariant, or every Einstein metric is absent. The nonsymplectic and
noncomplex conclusions have simpler existing topological proofs and
are identified as such in the note.

## 3. A global test for a charged two-ended continuation

[The spectral note](round7_spectral.md) retains the defect in the
classical harmonic-function argument for complete manifolds with two
AH ends. Let u separate the ends, h=|du|, and let nu be the probability
measure proportional to h^(4/3)dV. For E=Ric+3g and ||E||op<=epsilon,

\[
 \lambda_0+\frac23\int\left(
 |\mathrm{II}^{\circ}|^2+
 \frac23|\nabla_{\{u=\mathrm{const}\}}\log h|^2
 \right)d\nu
 \le2+\frac23\epsilon.
\]

For a free isometric T2 action, the level-set defect contains the full
physical twist Q. Consequently

\[
 \boxed{\lambda_0+\frac23\int Q\,d\nu
                   \le2+\frac23\epsilon.}
\]

This is an interaction between both ends, a harmonic function on the
complete metric, the full Ricci equation and the scalar spectrum. It is
not a pointwise test at the local throat. The normalized defect and
the bottom of the spectrum are unchanged by finite fibre quotients,
so those collapse operations cannot erase it.

The unweighted threshold lambda_0<=2 and its equality classification
are classical. The explicit retained twist term is the part useful
for this connector problem. A nonzero charged Einstein continuation
requires lambda_0<2. No independent lower bound on lambda_0, or lower
bound on the harmonic mass in the twist region, has been established
here; this is a necessary condition, not a no-connector theorem.

## 4. A separate global uniformization possibility, with its missing input

[The nonabelian note](round7_rigidity.md) examines Leung's precise
nonabelian Seiberg--Witten uniformization theorem. On a signature-zero
Einstein four-manifold the required rank-two system would force a
nonpositively curved locally symmetric universal cover. This would
contradict the known nonpositive-curvature obstruction for E_D.

The missing input is an actual solution of that coupled rank-two system,
not merely a nonzero ordinary monopole invariant. The wedge-dual matrix
identity and determinant charge 2A-D_L have been checked. However, the
relative quadratic sign must also match the published Clifford and
determinant conventions. The author's earlier paper writes curvature on
the canonical line while the spinor determinant is its inverse; a matrix
identity alone does not settle that conversion. The explicit-convention
rank-one calculation is therefore not accepted here as an obstruction
to solutions of Leung's system. Neither the required existence theorem
nor a convention-independent failure theorem has been obtained.

## What has changed in the research problem

The main gain is a sharper separation of viable tasks:

* Standard locally symmetric orbifold fillings cannot be joined to the
  current critical monopole obstruction just by adding concentrated
  curvature or changing chirality.
* The actual Davis fillings need a different Einstein detector than
  ordinary SW/BF, or an Einstein existence construction not based on
  making the smooth manifold Kähler.
* A charged complete connector must create a quantitatively compatible
  low spectral mode, not merely solve the local constraint equations.
* A nonabelian uniformization argument needs the actual coupled system;
  ordinary monopole persistence is not that missing theorem.

These are restrictions and necessary conditions, not four new solutions
to Yau26. They reduce repeated searches along incompatible connections.
The remaining decisive target is still a global existence or all-sign
nonexistence theorem on an actual input manifold, or a general mechanism
covering the original Ricci-pinching quantifiers.

## Reproduction

Run from this worktree:

```bash
qiushi-yau26 env numeric python round7_endpoint_check.py
qiushi-yau26 env numeric python round7_topology_check.py
qiushi-yau26 env numeric python round7_spectral_check.py
qiushi-yau26 env numeric python round7_rigidity_check.py
```

These checks cover exact coefficients, all 123 chirality counts, index
parity, the harmonic Hessian decomposition, an actual twisted complete
test metric, and the finite-dimensional rank-one calculation. Analytic
proofs and primary theorems are stated in the corresponding notes; the
checks do not certify literature novelty or complete geometric existence.
