# Global gauge-theoretic restrictions on the actual Davis resolutions

## 1. Statement and mathematical role

Let \(D\) be the closed Davis hyperbolic four-manifold and let \(\iota\)
be its central involution. Its quotient has 122 isolated \(A_1\) points
and simply connected underlying space. Resolve these points using fixed
standard Eguchi--Hanson end markings. Write \(M_m\) for any such marked
resolution having \(m\) bolt spheres of square \(+2\) and \(122-m\) of
square \(-2\), in the specified orientation. The subscript records a
chirality count, not a classification of all markings up to diffeomorphism.

The existing fixed-marking log-Weyl theorem supplies metrics on every one
of these actual smooth manifolds with

\[
 \|g_j^{-1}\operatorname{Ric}_{g_j}+I\|_\infty\longrightarrow0,
 \qquad \operatorname{Vol}_{g_j}M_m\longrightarrow156\pi^2. \tag{1}
\]

The present deduction uses the literal shrinking-support version of that
construction. It does not infer volume convergence from GH convergence.

**Theorem.** For every fixed marked \(M_m\):

1. Every ordinary numerical Seiberg--Witten invariant and every ordinary
   \(S^1\)-equivariant Bauer--Furuta invariant vanishes, in both orientations.
2. In the specified orientation, there are no special monopole classes
   if \(m\ge2\). If \(m=0\), every special monopole class, should one
   exist, has square 30 and expected dimension 1. If \(m=1\), its square
   must be 32 and expected dimension 0.
3. None of these smooth manifolds admits a symplectic structure in either
   orientation, and none admits a complex-surface structure.

Here a special monopole class means an actual monopole class \(a\) with
\(a^2\ge2\chi+3\tau\), not an arbitrary characteristic lattice vector.
The statement concerns ordinary absolute invariants. It makes no claim
about all possible families, equivariant, relative or other refinements.

The added deduction is the BF vanishing for the all-negative filling:
the analytic curvature ceiling leaves one possible index, and its stable
cohomotopy group is zero. For any filling with a positive bolt, BF
vanishing already follows from the known BF adjunction inequality.
Nonsymplecticity also has a topology-only proof, given below; it should
not be counted as a further analytic advance.

This is a global restriction on the constructed objects. In particular,
searching for a nonzero ordinary Bauer--Furuta invariant on one of these
resolutions cannot supply the missing Einstein obstruction. The theorem
does **not** prove that all ordinary monopole classes vanish; it does not
prove existence or nonexistence of an Einstein metric. Its novelty relative
to the literature has not been established.

## 2. Topology and curvature concentration

The calculations in [round6_entropy.md](round6_entropy.md), with mixed
chirality included as in [round5_rigidity.md, Section 6](round5_rigidity.md),
give

\[
 \pi_1(M_m)=1,\quad \chi(M_m)=196,\quad \tau(M_m)=2m-122,
 \quad b^+(M_m)=36+m,\quad b^-(M_m)=158-m.                 \tag{2}
\]

In particular \(b^+>1\) in either orientation. Put

\[
             T_m=2\chi+3\tau=26+6m.                    \tag{3}
\]

All the assertions below concern smooth invariants of these actual
resolutions; no diffeomorphism classification from intersection forms
is required.

For completeness, the topology uses \(\chi(D)=26\), the fixed-point
count 122, and simple connectivity of the coarse quotient. The last two
inputs are proved in [Fine--Panov, Lemma 26](https://msp.org/gt/2010/14-3/gt-v14-n3-p08-s.pdf).
Resolving a point increases the coarse Euler characteristic by one; the
two fillings have signature \(\pm1\). Van Kampen identifies the
resolution's fundamental group with the coarse quotient's group.

Let \(s_j\) denote scalar curvature and \(E_j\) trace-free Ricci.
From (1),

\[
 \int s_j^2\longrightarrow16(156\pi^2),\qquad
 \int|E_j|^2\longrightarrow0.
\]

The self-dual Chern--Weil formula then yields

\[
 \int|W^+_{g_j}|^2\longrightarrow12\pi^2m.              \tag{4}
\]

Our Weyl norm is the Hilbert--Schmidt norm as an operator on two-forms.
The construction agrees with the hyperbolic metric outside replacement
sets \(U_j\) of volume tending to zero. Hence \(W^+=0\) outside \(U_j\)
and

\[
 \int|W^+|\le\operatorname{Vol}(U_j)^{1/2}
                   \left(\int|W^+|^2\right)^{1/2}\to0.  \tag{5}
\]

The mixed scalar--Weyl monopole estimate, applied to the same actual
class \(a\) for each \(g_j\), gives

\[
 72\pi^2(a_{g_j}^+)^2
       \le\int(s_j-\sqrt6|W^+_{g_j}|)^2.
\]

Since \(a^2\le(a_{g_j}^+)^2\), (4)--(5) prove the classwise ceiling

\[
                    \boxed{a^2\le\frac{104}{3}+m.}       \tag{6}
\]

The mixed estimate is classical; its application to the literal
shrinking-support metrics is the content of the existing round5 proof.
The current use of (6) is an index restriction, not another optimization
of its constant.

## 3. Only two expected-dimension cases survive

For a spin-c structure with characteristic class \(a\), set

\[
 d(a)=\frac{a^2-T_m}{4},\qquad
 k(a)=\operatorname{ind}_{\mathbb C}D_a
                   =\frac{a^2-\tau(M_m)}8.              \tag{7}
\]

The intersection pairing of a closed simply connected oriented
four-manifold is unimodular. The characteristic congruence is

\[
                        a^2\equiv\tau(M_m)\pmod8.       \tag{8}
\]

For a special monopole class, combining (3) and (6) gives

\[
 26+6m\le a^2\le\frac{104}{3}+m,
 \qquad 0\le d(a)\le\frac{13}{6}-\frac54m.             \tag{9}
\]

If \(m\ge2\), the interval for \(a^2\) is empty. If \(m=0\),
the interval is \([26,104/3]\) and (8) requires \(a^2\equiv6\pmod8\).
The only possibility is

\[
                   a^2=30,\quad d(a)=1,\quad k(a)=19.   \tag{10}
\]

If \(m=1\), the interval is \([32,107/3]\) and (8) requires
\(a^2\equiv0\pmod8\). Therefore

\[
                   a^2=32,\quad d(a)=0,\quad k(a)=19.   \tag{11}
\]

These conclusions include all special monopole classes, whether or not
an invariant detects them. Ordinary metricwise monopole classes of
negative expected dimension have not been eliminated.

## 4. Vanishing of the ordinary Bauer--Furuta invariants

A nonzero ordinary Bauer--Furuta invariant supplies a generic monopole
class, hence a special one. The distinction and implication are explicit
in [Kotschick, Definition 7, Lemma 8 and the paragraph following
Proposition 9](https://arxiv.org/pdf/math/0306022).
The analytic argument below is needed only for \(m=0\); a positive
bolt gives an existing, stronger vanishing argument for every \(m\ge1\).

### All-negative filling: the remaining stable cohomotopy group is zero

For \(m=0\), the only possible nonzero invariant would have the data
(10). When \(b_1=0\), \(b^+>1\), the ordinary Bauer--Furuta invariant
belongs to

\[
                \pi^{b^+-1}(\mathbb{CP}^{k-1}).          \tag{12}
\]

This is [Bauer--Furuta I, Proposition 3.4](https://arxiv.org/pdf/math/0204340).
For (10), the group is

\[
                         \pi^{35}(\mathbb{CP}^{18})=0.   \tag{13}
\]

One can use the standard expected-dimension-one computation: the group
is \(\mathbb Z/2\) when the complex Dirac index is even, and zero when
it is odd. Here \(k=19\). The exact statement appears in
[Nakamura, equation (2.4)](https://arxiv.org/pdf/0705.1595).

There is also a short check of the relevant parity. In the stable
cohomotopy Atiyah--Hirzebruch spectral sequence, the only term that can
contribute to \(\pi^{35}(\mathbb{CP}^{18})\) is
\(H^{36}(\mathbb{CP}^{18};\mathbb Z/2)\). The incoming \(d_2\) is
\(\mathrm{Sq}^2\) after mod-two reduction from \(H^{34}(-;\mathbb Z)\).
For the degree-two generator \(x\),

\[
                    \mathrm{Sq}^2(x^{17})=17x^{18}=x^{18}.
\]

It is surjective, so the term dies. There are no other contributing
terms in these dimensions. This verifies why odd index, rather than
merely odd expected dimension, matters.

### Any positive bolt: the known BF adjunction theorem applies

For \(m\ge1\), let \(S\) be a bolt sphere of square \(+2\).
The BF-basic adjunction inequality gives

\[
         \chi_-(S)\ge S^2+|\langle a,[S]\rangle|.
\]

Here \(\chi_-\) sums \(2g-2\) over positive-genus components, so
\(\chi_-(S^2)=0\). The right-hand side is at least 2, a contradiction.
The statement and proof for ordinary \(S^1\)-equivariant BF are in
[Kato--Kishimoto--Nakamura--Yasui, Corollary 2.21 and Proposition 2.22](https://arxiv.org/pdf/2512.14183):
BF blowup nonvanishing makes the required blown-up classes monopole
classes, to which Kronheimer's inequality applies. Thus these mixed
and all-positive BF vanishings require neither (1) nor (6).

For comparison, a second proof in the exceptional analytic case \(m=1\)
uses \(\pi^{36}(\mathbb{CP}^{18})\cong\mathbb Z\): top-dimensional
stable cohomotopy maps isomorphically to cohomology, so the BF invariant
is its zero-dimensional SW number. Positive-sphere SW vanishing then
suffices. This longer proof is unnecessary once BF adjunction is used.

### Other spin-c structures and opposite orientation

On the all-negative filling, a spin-c structure outside (10) cannot
have nonzero BF: it would be a special monopole class and contradict
Section 3. With the positive-bolt argument, all spin-c structures
are covered, including those of negative expected dimension.

Changing orientation replaces \(m\) by \(122-m\), and the exact same
proof applies. Consequently all ordinary BF invariants vanish in both
orientations. Their numerical SW images vanish as well. This proves
parts 1 and 2 of the theorem.

## 5. Consequences for global geometric constructions

Nonsymplecticity does not require the log-Weyl input or the new
all-negative BF deduction. For \(m\ge1\), the positive bolt already
forces numerical SW vanishing by ordinary adjunction; see
[Manolescu, Proposition 7](https://stanford.edu/~cm5/glu.pdf).
Taubes's nonvanishing theorem then excludes symplectic structures.
For \(m=0\), \(b_1=0\) and \(b^+=36\), so an almost-complex structure
would have nonintegral complex Dirac index
\((\chi+\tau)/4=74/4\), impossible. Reversing orientation covers the
opposite orientation of every filling. Taubes's theorem is
[Taubes, *The Seiberg--Witten invariants and symplectic forms*](https://www.intlpress.com/site/pub/files/_fulltext/journals/mrl/1994/0001/0006/MRL-1994-0001-0006-a015.pdf).

Every compact complex surface with even first Betti number is Kähler;
see [Buchdahl, *On compact Kähler surfaces*](https://www.numdam.org/article/AIF_1999__49_1_287_0.pdf).
Here \(b_1=0\), so a complex-surface structure would supply a symplectic
form, contradicting the preceding conclusion. This proves part 3.
This is a standard consequence of the topology and embedded spheres,
not a new conclusion obtained by detecting the BF invariant.

It follows that changing chirality or complex structure within this
family cannot turn the present input construction into a negative
Kähler--Einstein existence proof. A successful Einstein existence result
would have to produce a metric not Kähler for any complex structure on
the smooth manifold. A nonexistence result would have to use information
not supplied by a nonzero ordinary SW or ordinary BF invariant here.

For \(2\le m\le120\), both orientations have no special monopole classes
at all, a stronger conclusion than the vanishing of these two invariants.
For \(m\in\{0,1,121,122\}\), special classes not detected by these
invariants remain a logically separate possibility. Metricwise monopole
classes are not identified with invariant-detected classes.

## 6. Spin does not automatically restore a nonzero index

There is a useful independent check against replacing the vanished
spin-c invariants with an uncomputed spin index. The fully symmetric
spin structure of \(D\) admits an order-two lift of the central
involution. [Ratcliffe--Tschantz, Theorem 3.2 and Table 6](https://arxiv.org/pdf/2106.04642)
give zero equivariant Dirac index for its class, the class with 122
fixed points.

At each fixed point the local spin contribution is \(+1/4\) or
\(-1/4\). Their sum zero forces 61 of each sign. Resolving with the
locally spin-compatible EH chirality consequently uses 61 bolts of
each chirality. The resulting spin resolution has signature zero,
so its ordinary \(\widehat A\)-genus is zero. Thus this particular
canonical spin construction provides no nonzero Dirac index obstructing
positive scalar curvature. Other invariant spin structures have not
been computed here.

This observation is not needed in the BF-vanishing proof. It prevents
an unsupported inference from the harmonic spinors on the hyperbolic
Davis manifold to a nonzero ordinary index on the resolved quotient.

## 7. Exact verification and remaining Einstein problem

`python3 round7_topology_check.py` checks, using rational arithmetic,
the topology, opposite orientations, characteristic congruences,
expected dimensions and Dirac indices for all 123 chirality counts.
It also checks the parity of the spectral-sequence differential in
(13). It does not prove the external index theorems, SW nonvanishing,
the fixed-point calculation, or the log-Weyl construction.

The added global deduction is all-negative BF vanishing on the actual
object carrying the near-Einstein input, together with the full
special-monopole index restriction. Positive-bolt BF vanishing and
nonsymplecticity are consequences of existing topology and adjunction.
None of these is a Yau26 branch counterexample.
The full question of Einstein existence on these smooth manifolds is
still open in this work. No conclusion here rules out methods using
minimal surfaces, full curvature equations, distinct smooth structures,
new invariants, or constructions outside this family.
