# Finite-cover integral rigidity beyond ordinary Seiberg--Witten detection

## 1. Main conclusions

The integral Ricci-defect theorem descends through finite coverings with
**no loss in its constant**. This gives a concrete new family of applications:
blow-ups of free diagonal orientation-reversing quotients of products of
hyperbolic surfaces. All ordinary Seiberg--Witten invariants of these
oriented blow-ups vanish, but the covering-space integral obstruction still
applies to every metric on them.

There is also a precise limitation for the new closed shear constructions.
Every finite cover has the same normalized full-monopole budgets as the
original manifold. Its critical ratio remains exactly one, not two-thirds.
Thus passage to finite covers cannot turn those existing near-Einstein
examples into examples excluded by the current critical monopole inequality.

These are deductions using the integral theorem from rounds 4--5, not a
new proof of that theorem or a claim that covering arguments themselves are
new. The quotient application goes beyond the base-manifold ordinary-SW
hypothesis used in round 13. The finite-cover saturation argument extends
the earlier round-5 observation for the surface bundles to the new shear
family.

## 2. Exact descent, including metric-dependent cover classes

For a closed four-manifold define

\[
 \mathcal E_M(g)=\inf_{\lambda\ne0}
 \frac{\int_M|\operatorname{Ric}_g-\lambda g|_g^2\,d\mu_g}
      {\lambda^2\operatorname{Vol}_g(M)}.
\]

Let \(\pi:\widetilde M\to M\) be an orientation-preserving connected
cover of degree \(d\). For every metric \(g\), every real nonzero
\(\lambda\), and either normalized sign \(\sigma\),

\[
 \begin{split}
 \operatorname{Ric}_{\pi^*g}&=\pi^*\operatorname{Ric}_g,\\
 \operatorname{Vol}_{\pi^*g}(\widetilde M)&=d\operatorname{Vol}_g(M),\\
 \int_{\widetilde M}|\operatorname{Ric}_{\pi^*g}
                         -\lambda\pi^*g|^2&=
             d\int_M|\operatorname{Ric}_g-\lambda g|^2,\\
 \mathcal E_{\widetilde M}(\pi^*g)&=\mathcal E_M(g),\qquad
 \delta_\sigma(\pi^*g)=\delta_\sigma(g).
 \end{split}                                                    \tag{2.1}
\]

All identities follow from the local-isometry property and integration
over sheets; taking the infimum in \(\lambda\) preserves equality.
No limit or compactness assertion is involved.

**Cover criterion.** Put \(T_M=2\chi(M)+3\tau(M)\). Suppose the cover
admits a number \(\widetilde A>0\) such that, for every metric of the
form \(\pi^*g\), one can select an actual weighted-solvable monopole
class \(a\) with

\[
 (a^+_{\pi^*g})^2\ge\widetilde A,
 \qquad a^2\ge T_{\widetilde M}=dT_M.                  \tag{2.2}
\]

Here weighted solvability is precisely round 13, equation (2): the same
spin-c structure works for every positive scalar weight on the given
conformal class. There is a universal \(c_*>0\), supplied by the
existing integral theorem, such that every metric on the base satisfies

\[
 \boxed{\displaystyle
 \mathcal E_M(g)+\left(\frac{T_M}{\widetilde A/d}
                                  -\frac23\right)_+\ge c_* .}
                                                               \tag{2.3}
\]

**Proof.** Apply the polarized integral theorem to \(\pi^*g\) and the
selected class, use (2.1), and divide both topological quantities by
\(d\). Euler characteristic and signature are multiplicative under
oriented finite coverings. QED.

One can use several qualifying covers and take the strongest resulting
lower bound; the constants do not deteriorate with degree. A fixed
negative-square cost bound on cover classes similarly retains the same
constant after descent: divide the upstairs class square and budget by
degree, leaving their ratio unchanged. This is bookkeeping, not an
assertion that the class is pulled back from the base.

This statement makes no claim that a monopole on the base pulls back to an
all-metric monopole on the cover. Such a claim would be unjustified: lifting
solutions produces solutions only for lifted metrics. Conversely the class
used upstairs need not descend, and its spinor need not be deck invariant.
The theorem merely tests a lifted metric against genuine equations upstairs.

Taking infima over metrics gives only

\[
 \inf_{\widetilde g}\mathcal E_{\widetilde M}(\widetilde g)
       \le\inf_g\mathcal E_M(g),                       \tag{2.4}
\]

not equality: most cover metrics need not descend. This distinction is
essential when trying to construct, rather than obstruct, metrics downstairs.

## 3. An explicit family with vanishing ordinary SW invariants

### 3.1 The smooth quotients and their topology

For integers \(p,q\ge2\), take closed nonorientable hyperbolic surfaces
of crosscap genera \(p+1,q+1\). Their orientation double covers are
oriented hyperbolic surfaces \(\Sigma_p,\Sigma_q\), with free
orientation-reversing isometric involutions \(\iota_p,\iota_q\).
Normalize the two surface metrics to curvature \(-1\). Define

\[
 X=\Sigma_p\times\Sigma_q,\qquad
 Q_{p,q}=X/\langle\iota_p\times\iota_q\rangle.          \tag{3.1}
\]

The diagonal involution is free and orientation preserving in real
dimension four. The product metric descends to a smooth metric \(q_0\)
with \(\operatorname{Ric}_{q_0}=-q_0\). Set
\(D=(p-1)(q-1)\). Direct topology and Gauss--Bonnet give

\[
 \begin{gathered}
 \chi(Q_{p,q})=2D,\qquad \tau(Q_{p,q})=0,\qquad
 T_Q=4D,\\
 b_1(Q_{p,q})=p+q,\qquad b_2(Q_{p,q})=2pq,\qquad
 b_+(Q_{p,q})=b_-(Q_{p,q})=pq,\\
 \operatorname{Vol}(Q_{p,q},q_0)=8\pi^2D,\qquad
 s_{q_0}=-4,\qquad
 \frac1{32\pi^2}\int_Qs_{q_0}^2=T_Q.                 \tag{3.2}
 \end{gathered}
\]

For the Betti calculation, the invariant part of
\(H^1(\Sigma_p;\mathbb R)\) has dimension \(p\), since it is the
first cohomology of the nonorientable quotient. The anti-invariant part
also has dimension \(p\). Neither factor area class survives the
diagonal action on \(H^2(X)\); the invariant part of
\(H^1(\Sigma_p)\otimes H^1(\Sigma_q)\) has dimension \(2pq\).
The displayed signature follows also from multiplicativity under the
two-fold cover. In particular no chamber qualification is needed.

### 3.2 Why the quotient has no special monopoles

The metric \(q_0\) has no nonzero parallel two-form in either orientation.
Indeed, on \(X\) the restricted holonomy is
\(SO(2)\times SO(2)\), so every parallel two-form is a linear
combination of the two factor area forms. The deck transformation acts
as minus the identity on their span. A parallel form downstairs would
lift to a deck-invariant member of this span, which must vanish.

Suppose a spin-c class \(c\) with \(c^2\ge T_Q\) has an unperturbed
monopole solution for \(q_0\). Write \(V=\operatorname{Vol}(q_0)\),
\(X_4=\int|\Phi|^4\), and \(Y_2=\int|\Phi|^2\). With the conventions
of the existing monopole-input proof,

\[
 X_4\ge32\pi^2(c^+)^2\ge32\pi^2c^2\ge32\pi^2T_Q=16V.
                                                               \tag{3.3}
\]

The integrated Weitzenbock identity with \(s=-4\) gives

\[
 X_4+4\int|\nabla_A\Phi|^2=4Y_2
                    \le4\sqrt{VX_4},
 \qquad X_4\le16V.                                    \tag{3.4}
\]

All inequalities are equalities. Thus \(\Phi\) is parallel and nonzero,
and its quadratic self-dual two-form is nonzero and parallel. This
contradicts the preceding holonomy calculation. Consequently \(Q\)
has no special monopole class, namely no all-metric monopole with
square at least \(T_Q\). The identical proof applies with the opposite
orientation because \(\tau=0\).

Any nonzero ordinary SW invariant has nonnegative expected dimension,
so its Chern class satisfies \(c^2\ge T_Q\), and nonvanishing supplies
an unperturbed solution for \(q_0\). Hence **all ordinary SW invariants
of \(Q_{p,q}\), with arbitrary allowed insertions, vanish in both
orientations**. Taubes nonvanishing then also excludes a symplectic
structure in either orientation.

This proof uses the standard SW curvature identity, available in
[LeBrun, Section 2](https://arxiv.org/pdf/math/0003068), but spells out
the equality argument rather than presuming that this particular
non-Kahler quotient has a vanishing invariant for another reason.

### 3.3 The descended integral obstruction after blow-up

Let

\[
 N_{p,q,k}=Q_{p,q}\#k\overline{\mathbb{CP}}^{\,2},\quad k\ge0.
\]

Blow up the two lifts of each base point. The resulting cover is

\[
 \widetilde N_{p,q,k}
       = (\Sigma_p\times\Sigma_q)\#2k\overline{\mathbb{CP}}^{\,2}
        \longrightarrow N_{p,q,k}.                       \tag{3.5}
\]

This is an actual smooth covering, not merely matching intersection forms:
the original cover is unchanged outside the chosen balls, and the two
standard oriented blow-up pieces over each ball are exchanged by the deck
action. Equivalently, choose complex blow-ups at paired points; the free
antiholomorphic deck map lifts. The complex surface \(X\) is minimal of
general type with \(A=c_1^2(X)=8D\), so the established blow-up gap applies
upstairs with \(2k/A=k/(4D)\). Equation (2.1) proves

\[
 \boxed{\displaystyle
 \mathcal E_{N_{p,q,k}}(g)+
       \left(\frac13-\frac{k}{4(p-1)(q-1)}\right)_+
                 \ge c_*\quad\hbox{for every smooth }g.}       \tag{3.6}
\]

The universal constant is unchanged. In particular, if

\[
 \frac{k}{4(p-1)(q-1)}\ge\frac13-\frac{c_*}{2},
\]

then every metric has \(\mathcal E(g)\ge c_*/2\), and every normalized
input satisfies \(\delta_\sigma(g)\ge\sqrt{c_*/8}\). Ricci-flat
Einstein metrics are separately impossible because their lift violates
the positive monopole scalar bound on the cover. Thus the band excludes
all Einstein signs, not only nonzero Einstein constants.

The ordinary SW invariants of \(N_{p,q,k}\) in the indicated orientation
still all vanish by the full blow-up formula:
[Ozsvath--Szabo, Theorem 3.2](https://arxiv.org/pdf/math/0005268).
That formula covers arbitrary spin-c structures and insertions, not just
the two classes with exceptional coefficient \(\pm1\). Thus (3.6)
cannot be obtained by applying round 13's ordinary-SW-base hypothesis
directly to \(Q_{p,q}\). It is a genuine enlargement of the project’s
demonstrated application class, obtained from equations on a cover.

For \(p=q=2\), the base has
\((\chi,\tau,b_1,b_+,b_-)=(2,0,4,4,4)\), \(T_Q=4\),
and \(N_{2,2,2}\) has zero positive-part term in (3.6). Larger genera
make the denominator unbounded, so the uniform width is not an artifact
of a fixed integer denominator. At \(k=0\), the descended product
Einstein metric gives \(\mathcal E=0\); accordingly the theorem only
requires \(c_*\le1/3\), consistent with the inherited constant.

The example \((p,q)=(2,3)\) has
\((\chi,\tau,b_1,b_+,b_-)=(4,0,5,6,6)\) and \(T_Q=8\).
Here the elementary almost-complex parity condition
\(1-b_1+b_+\in2\mathbb Z\) is satisfied. The SW-vanishing argument
is therefore not merely repackaging that parity obstruction.
The three-point blow-up already has zero positive-part term in (3.6).

No claim of worldwide priority for these quotient manifolds is made.
The new content here is their quantitative integral obstruction under
the previously established theorem, with the downstairs SW vanishing
and the actual covering identification both proved.

## 4. Why finite covers do not bridge the shear family to the critical band

Let \(M\) be a closed shear manifold from rounds 11--12, and let
\(\pi:\widetilde M\to M\) be any connected degree-\(d\) finite cover.
Write \(Q=2\chi(M)>0\). The existing construction gives metrics with

\[
 \frac1{32\pi^2}\int_Ms_{g_j}^2\longrightarrow Q,
 \qquad \tau(M)=0,
\]

and symplectic structures in both orientations. Pulling these structures
and the metrics up yields

\[
 \tau(\widetilde M)=0,\qquad T_{\widetilde M}=dQ,
 \qquad
 \frac1{32\pi^2}\int_{\widetilde M}s_{\pi^*g_j}^2\longrightarrow dQ.
                                                               \tag{4.1}
\]

Transfer makes \(H^1(M;\mathbb R)\to H^1(\widetilde M;\mathbb R)\)
injective, so \(b_1(\widetilde M)\ge1\). Since \(\chi(M)\ge4\),
the identity \(b_+=\chi/2+b_1-1\) implies
\(b_+(\widetilde M)\ge2\) in both orientations. The pulled-back
symplectic form therefore has a Taubes basic class \(K\) with
\(K^2=dQ\).

For **every actual monopole class** \(c\) on \(\widetilde M\), even
one undetected by ordinary invariants, the scalar estimate gives

\[
 (c^+_{\pi^*g_j})^2\le
 \frac1{32\pi^2}\int_{\widetilde M}s_{\pi^*g_j}^2.       \tag{4.2}
\]

For a convex combination \(v=\sum t_ic_i\), the norm triangle
inequality bounds \((v^+)^2\) by the same right side. Hence
\(v^2\le dQ\) in the limit. The actual Hodge planes in (4.2) are
admissible for the period-plane infimum defining \(\alpha^2\).
The positive-square actual class \(K\) supplies the reverse bound.
Consequently

\[
 \boxed{\displaystyle
 \alpha^2(\widetilde M)=\beta^2(\widetilde M)
   =\alpha_{\mathrm{sp}}^2(\widetilde M)
   =\beta_{\mathrm{sp}}^2(\widetilde M)=dQ.}              \tag{4.3}
\]

The assertion holds in either orientation. It does not classify all
monopole classes on the cover; none is needed to compute these budgets.
Definitions and the projection inequality are those of
[round 5](skill/references/rounds/round5_rigidity.md), Section 3.

In particular, any refinement that only takes the supremum of these
budgets divided by covering degree still equals \(Q\). The ratio is

\[
 \frac{2\chi(\widetilde M)+3\tau(\widetilde M)}
      {\alpha^2(\widetilde M)}=1                         \tag{4.4}
\]

on every cover. The same ceiling applies to a uniform budget obtained
by selecting conformally solvable polarized monopoles only for lifted
metrics: (4.2), applied along the lifted construction, forces any such
uniform budget to be at most \(dQ\).

Thus neither extra basic classes on large covers, nor replacing their
list by the full actual-monopole convex hull, can reach the critical
ratio \(2/3\) on this family. This is a conclusion about the numerical
monopole mechanism, not about all possible covering-space methods or
Einstein existence. A useful next mechanism must exploit more than
increasing this one topological budget: equivariant PDE information,
nonlocal marked geometry, or full nonlinear repair are not tested by
(4.3).

## 5. Mathematical role and reproducibility

The quotient construction shows how the integral theorem can see a
smooth topology whose ordinary invariants on the base vanish. The shear
calculation answers the complementary question: this same maneuver does
not silently solve the existing global candidate, because the actual
input sequence bounds every covering-space monopole budget.

`round14_rigidity_check.py` checks the exact normalization under covers,
the quotient cohomology character count, the blow-up ratio, the scalar
energy value, and the cover-stable shear ratio. These finite algebra
checks supplement, and do not replace, the covering construction,
Weitzenbock argument, Taubes input, or inherited integral theorem above.
