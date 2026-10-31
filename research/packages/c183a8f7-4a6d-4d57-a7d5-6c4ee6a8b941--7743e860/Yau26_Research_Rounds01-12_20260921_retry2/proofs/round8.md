# Yau 26, round 8: global restrictions on the actual candidate geometries

21 September 2026.

The unresolved question is still whether sufficiently tight pointwise Ricci
pinching, with a dimension-only threshold, forces the same closed smooth
manifold to carry some Einstein metric. The output need not resemble the
input. This round establishes restrictions on complete connectors, on every
rank-one representation of the surface-bundle candidates, and on the actual
connection required by the proposed nonabelian uniformization argument.
It does not establish either unrestricted four-dimensional branch.

## 1. Complete connectors: three ansatz classes are now excluded

The geometric object is a complete Einstein metric with `Ric=-3g` on the
interior of `[0,1] x T3`, with two smooth conformally compact ends and a
marked free isometric `T2` action extending freely to the boundary. Write

\[
 g=\gamma+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\quad
 G=\rho M,\quad\det M=1,\quad
 dA=f\,d\mu_\gamma,\quad q=\rho Gf.
\]

The exact mixed Einstein equation makes `q` constant. It is not a charge
that can be chosen independently at each end.

The [complete-connector argument](round8_global.md) proves the following.

* **No orthogonally transitive connector.** If `q=0`, the orbit-shape map
  into the curvature-minus-one hyperbolic plane has energy `e` tending to
  zero at both AH ends. Weighted Bochner gives `sup e <= 6`. A shortest
  essential loop for the auxiliary base metric `rho^2 gamma` lifts to a
  minimal torus separator. At a maximum of its orbit area, the intrinsic
  scalar and Gauss equations instead give `e >= 12`.
* **Neither Weyl half can vanish identically.** The classical
  Calderbank--Pedersen orthogonal-transitivity theorem for selfdual
  Einstein metrics with two commuting Killing fields reduces either
  half-flat case to the preceding contradiction.
* **No hypersurface-orthogonal circle, even in a charged metric.** A flat
  circle connection can be removed to obtain a locally isometric global
  static metric `V^2 dphi^2+h`. Its real Lorentzian continuation
  `-V^2 dt^2+h` has compact optical spatial completion and communicating
  timelike boundary components. This contradicts the classical
  Galloway--Schleich--Witt--Woolgar boundary noncommunication theorem.

In particular, a single constant real frame cannot diagonalize all the
fibre matrices `G`. The off-diagonal Einstein equation in such a frame is

\[
 0=\operatorname{Ric}_{12}
       =\tfrac12G_{11}G_{22}f^1f^2.
\]

Since charge is constant, one circle would be hypersurface-orthogonal.
An irrational choice of frame does not evade the argument: the principal
bundle is trivial, and replacing its constant lattice produces another
compact-fibre metric to which the same exclusion applies.

This is a genuine global restriction on the previously constructed local
charged necks. It does not contradict local Einstein existence. The
remaining exact connector must use spatially varying fibre directions,
nonzero charge and both Weyl halves. No general charged solution or
nonexistence theorem is obtained here.

### The end data carry a finite positive pairing

The [boundary calculation](round8_boundary.md) gives

\[
 \boxed{\quad
 \Delta H=C(g)q,\qquad
 C(g)=\int_B\rho^{-1}G^{-1}\,d\mu_\gamma>0,\qquad
 q\cdot\Delta H=2\int_B\rho Q\,d\mu_\gamma,
 \quad Q=\tfrac12f^{\mathsf T}Gf.\quad}
\]

Here `Delta H` is the difference of **real** end holonomy lifts in one
global marking. The matrix integral converges at the actual AH ends.
Equal torus-valued holonomies need not have equal real lifts: a complete
test metric with nonzero integer relative winding demonstrates the
distinction explicitly. It solves the mixed block but not the full Einstein
equation.

For either boundary metric, conformally normalizing the orbit determinant
gives

\[
 R_{\widehat h}=-\tfrac14\operatorname{tr}(M^{-1}M_s)^2.
\]

Its conformal Yamabe constant is zero exactly for constant orbit shape,
and negative otherwise. The Cai--Galloway theorem therefore requires
nonconstant shape at both ends of any putative connector. These conditions
survive finite fibre quotients; collapsing physical energy does not remove
the marked base equations.

There is a further obstruction even for negative-Yamabe boundaries. Align
the nonzero charge as `q=(q0,0)` and put `a=M12/M22`, `u=log M22`.
The exact shape equation gives the unforced shear current

\[
                 \operatorname{div}_\gamma(\rho e^{2u}\nabla a)=0.
\]

If both boundary shear values are the same constant, the interior maximum
principle forces that constant throughout the filling, hence a forbidden
constant-frame diagonal metric. Varying the boundary orbit sizes does not
evade this obstruction. Different end shear constants remain possible at
the level of this necessary condition.

## 2. The surface bundle: all rank-one representations can be computed

For the actual primitive single-Dehn-twist bundle `E_D`, of fibre and base
genera `p,q>=2`, the [group and volume argument](round8_construction.md)
proves that every representation into `PSL(2,R)` kills the twisting curve
`a`. The elementary reason is restrictive, not asymptotic: the twist
relations and the abelian centralizer of every nonidentity target element
force `a` to map to the identity. Thus every such representation factors
through

\[
 \pi_1(E_D)/\langle\!\langle a\rangle\!\rangle
       \cong (\Pi_{p-1}*\mathbb Z)\times\Pi_q.
\]

Using the classical Milnor--Wood bounds on these factors, one obtains the
sharp identity

\[
 \boxed{\quad
 \sup_{\varrho:\pi_1(E_D)\to\operatorname{PSL}(2,\mathbb R)^2}
      |\operatorname{Vol}(\varrho)|
 =16\pi^2(p-2)(q-1)
 =\frac{p-2}{p-1}V_0,
 \quad V_0=16\pi^2(p-1)(q-1).\quad}
\]

The supremum is attained; when `p=2` all these representation volumes
vanish. The vertical tangent Euler class is consequently not the Euler
class of a `PSL(2,R)` representation, although it does arise from the
nonlinear circle action of the fibre-group boundary.

The same centralizer argument proves that **every** map from `E_D` to a
closed strictly negatively curved four-manifold has degree zero, for all
fibre and base genera. This goes beyond the old smallest-genus entropy
calculation, but it uses classical group theory; independent discovery is
not a claim of literature priority.

These conclusions explain why the suggested representation and ordinary
nonzero-degree routes cannot decide the remaining Einstein question on
this actual candidate. An arbitrary negative Einstein metric supplies
neither a flat product-hyperbolic representation nor negative sectional
curvature. None of these statements may be converted into an arbitrary
Einstein-volume bound.

### Actual constructed families on which representations lose the fibre

The [multiple-twist synthesis](round8_multitwist.md) combines the Skill's
existing free-quotient slow-interpolation construction with the preceding
group argument. For `r` independent disjoint single twists on a fibre of
genus `p`, realized on distinct base handles, it gives a fixed smooth
bundle `E_{p,q,r}` with

\[
 \delta_-(G_L)\le C/L,\qquad \operatorname{Vol}(G_L)=V_0,
 \qquad
 \sup_{\varrho}|\operatorname{Vol}(\varrho)|
       =16\pi^2\max(p-r-1,0)(q-1).
\]

All fixed-order curvature derivatives stay bounded, and all fixed-order
Ricci-defect derivatives tend to zero. The proof gives the entire Ricci
matrix and a continuous operator-norm estimate; no error is hidden in a
shrinking volume or a sampled maximum. The global degeneration is in the
long thin base collars, not in curvature blow-up.

There is a stronger example when `q>=2p`: assign separate base handles the
twists around every standard fibre generator `a_i,b_i`. These monodromies
do not commute, but the base free quotient and disjoint interpolation
regions still give the same complete construction. On this actual fixed
bundle `E_full`, every representation into `PSL(2,R)` factors through the
base alone. Thus every product-hyperbolic representation volume vanishes
while the metric volume remains the positive constant `V0`.

The constructed metrics are inherited applications of the existing
method, not a second discovery of slow interpolation. The additional
calculation determines exactly what these proposed global invariants see
on the same objects. Their negative-Einstein existence question remains
open; the representation statements do not answer it.

## 3. A sharp obstruction to reducible nonabelian uniformization

The previous round could not justify transferring an ordinary-monopole
quadratic-map convention into the published rank-two equations. The new
[connection-level proof](round8_nonabelian.md) bypasses that sign issue.

Let `T=2 chi+3 tau>0`, fix a spin-c structure, and put
`V=S_L^- plus S_L^+`. For the actual indefinite-unitary block connection
`D`, let `Z` be its graded self-dual trace-free curvature. If `K` is a
smooth line subbundle of `S_L^+` and `P` its orthogonal projection, then

\[
 \boxed{\quad
 \pi\sqrt T\le\frac{\sqrt3}{2}\|Z\|_{L^2}
                              +2\|DP\|_{L^4}^{,2}.
 \quad}
\]

The proof is the projection-curvature identity, harmonic projection and
the exact spinor Chern identity `(2c1(K)-c1(L))^2=T`. There is no
noncollapse or Sobolev assumption. In particular,

\[
 DK\subset K\quad\Longrightarrow\quad
       \int|Z|^2\ge\frac{4\pi^2}{3}T.
\]

The constant is attained by an explicit construction on a compact
complex-ball quotient using the classical rank-three uniformization
connection. If `Z=0`, every such line instead requires

\[
 \int|DP|^4\ge\frac{\pi^2}{4}T.
\]

Thus adjoining an unused line to an ordinary-monopole construction cannot
provide the required rank-four connection. Changing the unused line's
curvature does not fix the problem, and a perturbation small in the
critical `L4` connection distance cannot fix it either. This excludes a
specific proposed bridge on `E_D`; it does not exclude genuinely coupled
rank-two solutions or settle their existence.

## 4. What the results change about the next research step

The surface-bundle construction already produces genuine pointwise
near-Einstein inputs. Its missing implication is still a restriction on
**every possible Einstein metric** on that smooth manifold. Flat
rank-one representations discard part of its topology, while the naive
ordinary-to-nonabelian insertion has a positive critical-energy cost.
Neither can be treated as the missing implication.

The graph-manifold route has the opposite difficulty: the exact global
connector must use charged, varying-shape geometry. Local charged germs,
one-ended completions, diagonal ansätze and relative boundary-translation
modes do not supply it. The end holonomy, shape equations, the preceding
round's spectral restriction and the fixed-closed-topology volume budget
must hold together.

These are sharper mathematical questions, not a proof that the remaining
possibilities are empty. The positive branch, higher-dimensional
affirmative coverage, and all-sign Einstein nonexistence for the constructed
closed candidates remain unresolved.

Full arguments and reproduction commands are in the linked notes and
[the verification record](round8_verification.md). All work is local to
this isolated research worktree. No active Session, installed Skill,
service or shared environment was modified.
