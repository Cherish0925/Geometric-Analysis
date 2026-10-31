# Monopole classes and the topology of the actual constructions

This note makes two connections. The integral gap extends uniformly to
the convex hull, and more strongly to the polarization minimum, of all
special monopole classes. Separately, the actual hyperbolic A1 resolution
construction bounds the invariant of **all** monopole classes: its
topological ratio is at least 3/4, not near the critical value 2/3.
For the Dehn-twist surface bundle the ratio is exactly 1, while sufficiently
large negative-definite connected-sum modifications have a uniform Ricci
energy gap. Thus these modifications cannot preserve the original
near-Einstein construction while adding a monopole nonexistence obstruction.

The new statements below are deductions from the integral analytic theorem
and explicit construction data, not a solution of the general Yau26
question. In particular no all-metrics Einstein nonexistence theorem on
the unmodified surface bundle or a general hyperbolic resolution is claimed.

## 1. Analytic input and conventions

Let M be a closed, connected, oriented smooth four-manifold with b+ >= 2,
and put T=2 chi(M)+3 tau(M). A monopole class means the real image of the
first Chern class of a spin-c structure whose unperturbed Seiberg--Witten
equations have solutions for every smooth metric. In particular it supplies
the rescaled equations by conformal covariance. Torsion classes have zero
real image and do not supply a positive projection bound.

For a metric g write V=Vol(g), S=integral s, and R2=integral |Ric|^2. When
R2>0 define

\[
 \mathcal E(g)=4-\frac{S^2}{V R2}
 =\frac{4\int|\operatorname{Ric}^{\circ}|^2
              +\int(s-S/V)^2}{\int|\operatorname{Ric}|^2}.       \tag{1}
\]

This is the infimum over nonzero real lambda of
integral |Ric-lambda g|^2/(lambda^2 V). It is invariant under constant
rescaling, and vanishes precisely for a non-Ricci-flat Einstein metric.
The scalar monopole inequality makes R2=0 impossible whenever a selected
monopole has (a+)^2 >= A > 0.

The input from [the integral theorem](round4_rigidity.md), Sections 7--8,
and [its positive-branch corollary](round4_all_sign_gap.md), is:

* If a metric has an actual monopole a with (a+)^2 >= A > 0 and
  a^2 >= T, then

  \[
   \mathcal E(g)+(T/A-2/3)_+\ge\varepsilon_0>0.            \tag{2}
  \]

  The same numerical epsilon_0 works for all M, A, a and g.
* If instead a^2 >= -C_A A, (2) holds with a positive constant
  epsilon(C_A) depending only on C_A.

One may take epsilon_0=min{1/4,c/1215}, where c is the universal constant
in round4 Theorem 1. Shrinking it is harmless. There are no pointwise
curvature, noncollapse, Euler-ratio or Sobolev hypotheses. The required
monopole inequalities and rescaling are proved in
[the self-contained input note](round3_monopole_input.md).

## 2. Which classes supply the square hypothesis?

Call a monopole class special when a^2 >= T. Call it generic when solutions
exist for every pair consisting of a metric and a smooth self-dual
curvature perturbation. For generic perturbations the irreducible moduli
space is regular, of dimension

\[
                         d(a)=\frac{a^2-T}{4}.             \tag{3}
\]

When b+>0, the perturbation can also avoid the reducible wall. Thus a
generic monopole class has a nonempty regular moduli space and d(a)>=0.
Nonzero chamber-independent ordinary SW invariants and nonzero
Bauer--Furuta invariants supply generic classes. These are precisely the
implications recorded in [Kotschick, Definitions 3 and 7, Lemma 8 and the
paragraph following Proposition 9](https://arxiv.org/abs/math/0306022).
No simple-type or zero-dimensional hypothesis is necessary here.

An ordinary monopole class is not defined by persistence under curvature
perturbation. Consequently generic-pair transversality cannot be applied
to it without another input. The general metric-only transversality claim
is not proved by [Scala's theorem](https://arxiv.org/abs/0902.4690), which
treats Hermitian perturbations near a Kahler metric. We do not infer
a^2>=T for every nonzero ordinary monopole class, and do not claim an
example with positive projection disproves that possible strengthening.

Let C denote the set of real monopole classes and C_sp its special subset.
For b+>=2 the full C, not only C_sp, is finite; this follows from
[LeBrun, Proposition 3.6](https://arxiv.org/abs/math/0611450).
The finiteness proof bounds pairings with a cohomology basis whose elements
are self-dual for finitely many chosen metrics, and then uses lattice
discreteness. It does not use a lower bound on a^2 and does not establish
(3) with d>=0 for an arbitrary class.

## 3. Uniform convex-hull and polarization versions

For any nonempty finite set C_0 of actual monopole classes, define

\[
 \beta_0^2=\max_{v\in\operatorname{Hull}(C_0)}v^2,
 \qquad
 \alpha_0^2=\inf_{H\in\operatorname{Gr}_{b+}^{+}}
                         \max_{a\in C_0}(a_H^+)^2.         \tag{4}
\]

Here H ranges over all maximal positive subspaces of the intersection
form, not just those known to be realized by a metric. The square on H
is positive definite. For v=sum t_i a_i, convexity gives

\[
 v^2\le(v_H^+)^2\le\sum_i t_i(a_{i,H}^+)^2
                           \le\max_i(a_{i,H}^+)^2.        \tag{5}
\]

Therefore beta_0^2 <= alpha_0^2, and every metric admits a selected
a in C_0 with (a+)^2 >= alpha_0^2. Finiteness makes the maximum over
classes attained; the infimum over H need not be attained.

**Theorem 1 (all special classes).** Suppose alpha_sp^2>0, where (4)
is applied to C_sp. Every smooth metric satisfies

\[
 \boxed{\quad
 \mathcal E(g)+\left(\frac{T}{\alpha_{\rm sp}^2}
                                      -\frac23\right)_+
                    \ge\varepsilon_0 .\quad}            \tag{6}
\]

The same conclusion holds with any positive A<=alpha_sp^2, in
particular A=beta_sp^2 when that number is positive. Thus the theorem
applies to all collections detected by nonzero SW or BF invariants,
without requiring a specified blow-up or connected-sum presentation.

**Proof.** Select a special class maximizing its projected square for
the given metric. Equations (4)--(5) give p>=A and its definition gives
a^2>=T. Apply (2). This also excludes a Ricci-flat metric by the scalar
bound. The constant is independent of the number of classes and b+. QED.

For example if T/alpha_sp^2 <= 2/3+epsilon_0/2, every metric has
E(g)>=epsilon_0/2. This excludes all Einstein signs and even vanishing
scale-invariant integral Ricci defect, not just exact Einstein metrics.

There is also an all-ordinary-class version, with an honest dependence:
if A=alpha_all^2>0 and

\[
             C_M=\max_{a\in C}\frac{(-a^2)_+}{A},
\]

then finiteness and (5) imply

\[
 \mathcal E(g)+(T/A-2/3)_+\ge\varepsilon(C_M)>0.            \tag{7}
\]

The same assertion works with A=beta_all^2>0. This is a fixed-manifold
gap; it is not a universal estimate for all ordinary monopole classes.

The missing uniform square bound cannot be supplied by convex geometry
alone. On R^(2,1) with Q=x^2+y^2-z^2 consider

\[
 C_L=\{\pm(1,0,L),\ \pm(1,0,-L)\}.
\]

Its convex hull has beta_L^2=1, all vertices have square 1-L^2, and
alpha_L^2=1: the xy-plane gives the upper bound 1 and (5) gives the
opposite bound. The negative vertex squares are unbounded as L grows.
This is a counterexample to a proposed *convex-geometric inference*,
not a claim that these sets are realized by monopole classes.

## 4. A larger connected-sum theorem, including the surface bundle

Here is a concrete application that does not require a complex surface.
Let X have b+(X)>=2 and a nonzero ordinary SW invariant with class c
such that A=c^2>0. Let N be a closed oriented smooth manifold with
b+(N)=0. Put k=b2(N), ell=b1(N), D=k+4 ell, and M=X#N.

The gauge-theoretic connected-sum input is the actual set of monopoles

\[
                      a_{\boldsymbol\epsilon}
                         =c+\sum_{i=1}^k\epsilon_i e_i,
                         \qquad\epsilon_i\in\{\pm1\},     \tag{8}
\]

where the negative-definite generators of N have e_i e_j=-delta_ij.
This is [Ishida, Proposition 6 and its proof, equation (7)](https://msp.org/pjm/2012/258-2/pjm-v258-n2-p05-s.pdf), using the
Bauer--Furuta gluing theorem. The standard choice
N=k CPbar^2 # ell(S^1 x S^3) also follows from
[LeBrun, Proposition 3.2](https://arxiv.org/abs/math/0003068).
This is an invariant-theoretic input, not an inference from Betti numbers.

**Theorem 2.** Under these hypotheses, every metric on M satisfies

\[
 \boxed{\quad
 \mathcal E(g)+
     \left(\frac{T_X-D}{A}-\frac23\right)_+
                        \ge\varepsilon_0 .\quad}          \tag{9}
\]

**Proof.** The virtual dimension gives A>=T_X. Direct connected-sum
topology gives T_M=T_X-D, while every class in (8) has

\[
              a_{\boldsymbol\epsilon}^2=A-k
                        \ge T_X-k=T_M+4\ell\ge T_M.
\]

Averaging the positive projected squares over all signs cancels the
cross terms:

\[
 2^{-k}\sum_{\boldsymbol\epsilon}(a_{\boldsymbol\epsilon}^+)^2
      =(c^+)^2+\sum_i(e_i^+)^2\ge c^2=A.
\]

At least one class has projected square >=A. Apply (2). QED.

If X is symplectic with b+>=2 and c1^2(X)>0, its canonical class is a
nonzero SW class with A=T_X. Thus

\[
 \mathcal E(g)+\left(\frac13-
                   \frac{4b_1(N)+b_2(N)}{c_1^2(X)}\right)_+
                         \ge\varepsilon_0.               \tag{10}
\]

In particular take X to be any finite connected cover of E_D, with
either orientation and A=2 chi(X)>0. The surface-bundle construction
supplies E(g_j)->0 on X itself. But for

\[
       4b_1(N)+b_2(N)\ge(1/3-\varepsilon_0/2)\,2\chi(X),
\]

every metric on X#N has E(g)>=epsilon_0/2. Any proposed gluing that
preserves arbitrarily tight near-Einstein input through such a surgery
is therefore impossible. This is a compatibility obstruction on the
precisely modified smooth object, independent of the gluing ansatz.

## 5. Why the unmodified E_D does not enter the critical band

We record the proof rather than relying on a list of basic classes.
For a degree-d connected cover X of E_D, write V*=d V0. The actual
fixed-fibre construction and topology give

\[
 \tau(X)=0,\qquad T_X=2\chi(X)=V_*/(2\pi^2),\qquad
 \operatorname{Vol}(g_j)=V_*,\qquad
 \|g_j^{-1}\operatorname{Ric}_{g_j}+I\|_\infty\longrightarrow0.
                                                               \tag{11}
\]

Both orientations are symplectic and have a canonical monopole K with
K^2=T_X. Thus beta_sp^2>=T_X. For *every* monopole class a, scalar
curvature gives the uniform bound

\[
 (a_{g_j}^+)^2\le\frac1{32\pi^2}\int s_{g_j,-}^2
                       \le T_X(1+\delta_j)^2.
\]

Taking the maximum over all classes and then the infimum over positive
planes, while using (5) and C_sp subset C, yields

\[
 \boxed{\quad
 \beta_{\rm sp}^2=\alpha_{\rm sp}^2
   =\beta_{\rm all}^2=\alpha_{\rm all}^2=T_X.
 \quad}                                                      \tag{12}
\]

Hence T_X/A=1 even with the strongest invariant in (12). New classes in
covers, or classes unknown individually, do not change this conclusion.
For the opposite orientation use the same g_j and its complementary
Hodge plane; therefore both orientations saturate simultaneously.
Nonnegative weighted sums or maxima of the two numerical projection
bounds do not remove the slack.

The geometric inputs (11) are the actual fixed-fibre construction and
the symplectic canonical classes: the source derivations are
`20260916_construction.tex`, Theorem `thm:ED-slow`, and
`20260912.tex`, `BUNTOP:object`, `BUNTOP:all-monopoles`.
Equation (12) is already present there for all classes. Its use here is
to delimit the new theorem and prove the surgery incompatibility (10),
not to relabel that earlier saturation calculation as a new discovery.

## 6. Hyperbolic A1 resolutions: a sharper all-monopole separation

Let (O,g0) be a closed oriented real-hyperbolic four-orbifold with isolated
A1 points only, normalized by Ric(g0)=-g0. Let V0=Vol(O,g0), let n be
the number of nodes, and fix a marked smooth resolution M obtained by
Eguchi--Hanson fillings. In the chosen orientation let m of the bolt
spheres have square +2 and n-m have square -2. Set

\[
                     B=\frac{V_0}{6\pi^2}>0.              \tag{13}
\]

Suppose the marked data satisfy the hypotheses of the log-Weyl
construction, with its actual output properties:

1. smooth metrics g_j on this fixed M have Ricci endomorphism defect
   delta_j->0 relative to -I;
2. outside sets U_j they agree isometrically with the hyperbolic
   orbifold with shrinking node balls removed;
3. Vol(U_j,g_j)->0 and Vol(M,g_j)->V0.

These are not consequences of GH convergence alone. For the explicit
construction, the outer radius R_j tends to zero; annular metrics are
uniformly comparable to the Euclidean cone and the core volume is
O(b_j^4). Therefore Vol(U_j)=O(R_j^4)->0, proving item 3 directly.
The exterior equality is in the construction's outer-cutoff paragraph.

**Theorem 3.** If b+(M)>=2, then

\[
 T_M=B+6m,\qquad
 \boxed{\quad \alpha_{\rm all}^2(M)\le\frac43 B+m.\quad}   \tag{14}
\]

Consequently, whenever alpha_all^2>0,

\[
 \boxed{\quad
 \frac{T_M}{\alpha_{\rm all}^2(M)}
       \ge\frac{B+6m}{4B/3+m}\ge\frac34,
 \qquad
 \frac{T_M}{\alpha_{\rm all}^2(M)}-\frac23
       \ge\frac1{12}.\quad}                              \tag{15}
\]

The same ratio bound holds for beta_all^2 or any smaller positive
projection lower bound, including the special-class invariants.

**Proof of the topology formula.** Hyperbolic orbifold Chern--Gauss--
Bonnet gives chi_orb(O)=V0/(12 pi^2). Removing n orbifold balls subtracts
n/2 from orbifold Euler characteristic, and each EH disc bundle has
Euler characteristic 2. Its boundary RP^3 has Euler characteristic
zero. Therefore

\[
             \chi(M)=\chi_{\rm orb}(O)+3n/2.              \tag{16}
\]

The truncated hyperbolic exterior has signature zero. To see this without
assuming a signature formula for the singular space, alter its round
warped-product boundary collars to product collars, keeping them
conformally flat. The signature density remains zero everywhere.
The round RP^3 boundary has zero odd-signature eta invariant, since
reflection of S^3 descends to an orientation-reversing isometry of RP^3.
The [APS signature formula](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/aps001.pdf)
therefore gives zero signature for the exterior. Signature additivity and
the one-dimensional forms (+2) or (-2) of the fillings give

\[
                         \tau(M)=2m-n.                    \tag{17}
\]

Equations (13), (16), and (17) imply T_M=B+6m. This calculation uses
the actual filling orientation, not an assumed smooth connected-sum
classification.

**Proof of the monopole bound.** Since delta_j->0 and V_j->V0,

\[
 \int s_j^2\longrightarrow16V_0,\qquad
 \int|\operatorname{Ric}^{\circ}_{g_j}|^2\longrightarrow0.
\]

The smooth Chern--Weil identity on the fixed M yields

\[
 \int|W^+_{g_j}|^2
 =2\pi^2 T_M-\frac1{48}\int s_j^2
                  +\frac14\int|\operatorname{Ric}^{\circ}_{g_j}|^2
 \longrightarrow12\pi^2m.                               \tag{18}
\]

Our Weyl norm is the operator Hilbert--Schmidt norm on Lambda+. The
number 12 pi^2 is not the full four-index curvature-tensor energy.
There is no need to prove an independent bubble-energy identity: (18)
follows from topology, volume, and the Ricci bound.

W+ is zero outside U_j. By Cauchy--Schwarz and (18),

\[
 \int|W^+_{g_j}|
 \le \operatorname{Vol}(U_j)^{1/2}
                  \left(\int|W^+_{g_j}|^2\right)^{1/2}
                           \longrightarrow0.             \tag{19}
\]

Scalar curvature is uniformly bounded. Hence, for
q_j=-s_j+sqrt(6)|W+_j|, which is positive for large j,

\[
 \begin{split}
 \int q_j^2
 &=\int s_j^2+6\int|W_j^+|^2
                         -2\sqrt6\int s_j|W_j^+|\\
 &\longrightarrow16V_0+72\pi^2m.                         \tag{20}
 \end{split}
\]

The mixed monopole inequality applies to every a in C(M) for this same
metric. Consequently

\[
 \max_{a\in C(M)}(a_{g_j}^+)^2
                 \le\frac1{72\pi^2}\int q_j^2,
\]

and the infimum in (4) gives alpha_all^2<=2V0/(9 pi^2)+m=4B/3+m.
If C contains no nonzero classes, its invariant is taken to be zero
and this inequality is automatic. Finally

\[
 \frac{B+6m}{4B/3+m}-\frac34
                 =\frac{21m}{4(4B/3+m)}\ge0,             \tag{21}
\]

which proves (15). QED.

**General negative Einstein exterior.** The same argument also gives an
exact compatibility formula for any fixed negative Einstein orbifold
with only A1 nodes, whenever the same literal shrinking-support
construction applies. Normalize Ric(g0)=-g0 and put

\[
 T_0=\frac1{4\pi^2}\int_O(s_0^2/24+2|W_0^+|^2),\qquad
 C_0=\frac1{72\pi^2}\int_O(-s_0+\sqrt6|W_0^+|)^2.
\]

The signature boundary corrections still vanish at A1 points. Subtracting
the exterior integrals in (18)--(20) gives

\[
                 T_M=T_0+6m,\qquad
                 \alpha_{\rm all}^2(M)\le C_0+m.          \tag{22}
\]

Indeed the excess W+ energy is 12 pi^2 m, while its contribution linear
in |W+| on the shrinking region vanishes. The completed-square identity
27(s^2/24+2|W+|^2)-(-s+sqrt(6)|W+|)^2
=(s+8 sqrt(6)|W+|)^2/8 gives C0<=3T0/2. We assert only the resulting
ratio bound 2/3 in this generality. Equality of that algebraic bound
fixes a norm, not the forbidden Weyl eigenvalue pattern; it does not
justify a strict general improvement. The real-hyperbolic specialization
has C0=4B/3 and gives the stronger explicit separation (15).

This is a numerical obstruction to combining the *actual* hyperbolic
log-Weyl construction with the critical monopole-band obstruction. It
does not prove that those resolutions have Einstein metrics. Their
known GH separation from normalized exact Einstein metrics has a
different conclusion and is not converted here into all-metrics
nonexistence.

## 7. Positive A1 inputs and the remaining boundary

For a positive-normalized A1 input, delta_+(g_j)<1 eventually implies
positive scalar curvature. If b+>0, no nonzero real ordinary monopole
class can persist for all metrics: the Weitzenbock identity forces a
reducible solution at every positive-scalar-curvature metric, whereas
a generic nearby metric makes a fixed nonzero class non-anti-self-dual.
Thus the positive input cannot lie in any positive-A monopole band.

In particular this method does not decide the all-sign Einstein problem
on the standard positive filling CP^2#CP^2. The other standard two-pole
filling S^2 x S^2 already has its product Einstein metric; b+=1 also
falls outside the chamber-independent theorem used above.

For the two complex-oriented algebraic A1 resolutions explicitly
smoothed in the construction source, negative Kahler--Einstein metrics
exist on the same smooth objects, so they are not nonexistence
candidates. The Campedelli example has b+=1 and must not be inserted
silently into the b+>=2 theorem. No claim about mixed-chirality fillings
follows from those complex smoothing arguments.

The connections established here are therefore exact but limited:
special/generic classes enlarge the uniform rigidity family; arbitrary
ordinary classes give a fixed-object version; the unmodified E_D and
the real-hyperbolic A1 resolutions stay away from the critical band;
and negative-definite connected sums that enter that band cannot retain
arbitrarily tight Ricci inputs. A same-object Yau26 counterexample still
requires an Einstein obstruction outside these numerical monopole bounds.

## 8. Verification scope

`round5_rigidity_check.py` checks the connected-sum and chirality
identities, the exact mixed-energy limit coefficients, the separation
in (21), sign averaging, and the elementary convex counterexample.
These are algebra checks, not proofs of gauge-theoretic gluing,
transversality, APS theory, or existence of the construction. Those
inputs and the precise hypotheses under which they are used are given
in the text above.
