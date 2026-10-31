# A hyperbolic A1 resolution with no ordinary entropy to transfer

## 1. The concrete conclusion

There is a fixed closed smooth oriented four-manifold \(M\), obtained by
resolving all 122 singularities of the Davis hyperbolic orbifold with
negative Eguchi--Hanson bolts, with the following properties:

\[
\begin{gathered}
\pi_1(M)=1,\qquad \chi(M)=196,\qquad \tau(M)=-122,\\
b_2^+(M)=36,\qquad b_2^-(M)=158,\qquad
2\chi(M)+3\tau(M)=26.                                      \tag{1}
\end{gathered}
\]

The fixed marked log-Weyl construction applies to this \(M\). It produces
metrics \(g_a\) with

\[
\|g_a^{-1}\operatorname{Ric}(g_a)+I\|_\infty\longrightarrow0,
\qquad \operatorname{Vol}(g_a)\longrightarrow V_0=156\pi^2.   \tag{2}
\]

Nevertheless every smooth metric on \(M\) has **zero ordinary volume
entropy**, and \(M\) has zero ordinary simplicial volume. Its degree-one
coarse blow-down to the hyperbolic orbifold therefore does not satisfy a
BCG degree inequality with the orbifold hyperbolic volume on the right.
This gives a concrete counterexample to that proposed transfer, on an
actual topology carrying the pointwise near-Einstein construction.

Neither orientation of \(M\) admits an almost-complex structure. Thus
changing its complex structure and applying Aubin--Yau cannot furnish an
Einstein metric on this particular smooth manifold. These statements do
**not** decide whether \(M\) admits a non-Kähler Einstein metric of any sign.
In particular, failure of the entropy argument is not a counterexample to
a Ricci-minimal-volume lower bound obtained by some different method.

## 2. The orbifold and its actual resolution

Let \(D\) be the Davis closed oriented hyperbolic four-manifold. Its cell
counts are \(1,60,144,60,1\), so \(\chi(D)=26\); this value is also recorded
in [Davis, *A hyperbolic 4-manifold*, p. 328](https://people.math.osu.edu/davis.12/old_papers/4-mfld.pdf).
The central involution \(\iota\) has 122 isolated fixed points, each with
tangent action \(-I\), and the coarse quotient
\(Q=|\mathcal O|=D/\iota\) is simply connected. These are precisely
[Fine--Panov, §4.1, Lemma 26](https://msp.org/gt/2010/14-3/gt-v14-n3-p08-s.pdf),
not a claim about the fundamental group of their six-dimensional twistor
space. Their proof kills the 60 side-pairing generators: each generating
closed geodesic is folded by the involution to an interval in the quotient.

Normalize the hyperbolic orbifold metric by \(\operatorname{Ric}(g_0)=-g_0\).
Its sectional curvature is \(-1/3\), and

\[
\chi_{\rm orb}(\mathcal O)=\tfrac12\chi(D)=13,
\qquad V_0=12\pi^2\chi_{\rm orb}(\mathcal O)=156\pi^2.       \tag{3}
\]

Remove disjoint small singular balls and attach the oriented disc bundles
of \(\mathcal O(-2)\to\mathbb{CP}^1\) using fixed standard orthogonal end
markings. Call the resulting smooth manifold \(M\), and its disjoint zero
sections \(E_1,\ldots,E_{122}\). Thus \(E_j^2=-2\).

Here the local hypotheses of the log-Weyl theorem are available, not an
extra unresolved condition. The construction proof's explicit biaxial
family supplies a smooth tensor \(\widetilde h\) on this very disc bundle,
with

\[
D\operatorname{Ric}_{g_{\rm EH}}\widetilde h=g_{\rm EH},
\qquad \widetilde h=H_*+O_2(\rho^{-2}),\qquad
H_*(x,\cdot)=0.                                           \tag{4}
\]

For the negative sign one uses \(-\widetilde h\). Transport through any
of the fixed orthogonal end markings preserves (4). Both the ambient
normal jet and the transported core jet have the same linearized Ricci
contraction and radial gauge; their difference is an algebraic Weyl jet.
The log cutoff treats all ten Weyl directions, not only a special matching
chirality. Its three scales are
\(b=a^{1/2}\), \(R=a^{1/4}\), and
\(L=\log(R/(8b))\); the full Ricci-endomorphism bound is
\(C(L^{-1}+a^{1/2})\). Finitely many fixed disjoint nodes cause no additional
interaction term in this approximate construction.

These are the precise inputs and proof of Theorem `thm:A1` and §`sec:A1-proof`
in the local construction manuscript. The volume assertion in (2) follows
from the actual estimates: the metric equals \(g_0\) off the node balls
of radius \(R\), the annular metrics are uniformly comparable to Euclidean
ones, and the scaled EH cores have volume \(O(b^4)\). Thus the entire
replacement volume is \(O(122R^4)\to0\). GH convergence alone is not used
as a volume theorem. The curvature-energy bookkeeping for this precise
shrinking-support construction is retained in
[round5_rigidity.md, §6](round5_rigidity.md).

## 3. Fundamental group, Euler characteristic, and signature

More generally, write \(\mathcal O=\mathbb H^4/\Gamma\) for an oriented
hyperbolic orbifold with only isolated A1 singularities. Let \(X\) be its
truncated regular part, and let \(t_j\in\Gamma\) denote generators of its
point stabilizers. The deleted-point subset of \(\mathbb H^4\) is simply
connected: a bounding disk can be moved off a locally finite collection
of points by general position. Consequently \(\pi_1(X)=\Gamma\), and
each boundary \(\mathbb{RP}^3\) maps its fundamental group injectively to
\(\langle t_j\rangle\cong\mathbb Z/2\).

Both a cone over \(\mathbb{RP}^3\) and either EH disc bundle are simply
connected. Van Kampen therefore gives

\[
\pi_1(M)=\pi_1(|\mathcal O|)
=\Gamma/\langle\!\langle t_1,\ldots,t_n\rangle\!\rangle.    \tag{5}
\]

For the Davis orbifold the last quotient is trivial. The topological Euler
characteristic of its coarse quotient is
\(\chi(Q)=(26+122)/2=74\). Replacing each contractible cone by a disc
bundle retracting to \(S^2\) increases Euler characteristic by one, so
\(\chi(M)=74+122=196\).

There is a useful smooth branched double cover which also computes the
signature without confusing an orbifold cover with an ordinary cover.
Blow up \(D\) smoothly in orientation-compatible complex coordinate charts
at its 122 fixed points. This gives

\[
Y=D\#122\,\overline{\mathbb{CP}}{}^2.
\]

The involution lifts. Locally it is multiplication by \(-1\) on the fibres
of \(\mathcal O(-1)\); taking its quotient squares those fibres, producing
\(\mathcal O(-2)\). Thus its smooth quotient is exactly the specified \(M\),
and

\[
p:Y\longrightarrow M
\]

is a double cover branched over \(B=\coprod E_j\), not an unbranched cover.
The signature of the hyperbolic \(D\) is zero. Hence \(\tau(Y)=-122\).
The smooth branched-cover signature formula gives

\[
\tau(Y)=2\tau(M)-\tfrac12 B^2,
\qquad B^2=-244,
\]

so \(\tau(M)=-122\). The exact smooth hypotheses and four-dimensional
formula are in [Viro, §2.2, equation (18)](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/viro3.pdf).
This proves all of (1). As an independent consistency check,
\(\chi(Y)=26+122=148=2\chi(M)-\chi(B)\).

An almost-complex closed four-manifold necessarily has
\((\chi+\tau)/4\in\mathbb Z\): this is the index of its canonical
spin-c Dirac operator, equivalently its Todd genus. Here

\[
\chi(M)+\tau(M)=74,\qquad \chi(M)-\tau(M)=318,
\]

neither divisible by four. The obstruction applies in both orientations,
hence also excludes symplectic structures and integrable complex
structures in both orientations. No diffeomorphism classification from
the intersection form is being asserted.

## 4. What BCG does and does not say here

The primary [BCG paper, principal theorem and its real-hyperbolic corollary,
p. 734](https://www.aimath.org/WWN/entropyrigidity/papers/BessonCourtoisGallot.pdf)
assumes an ordinary continuous map of nonzero degree between closed
oriented manifolds of the same dimension, with the target carrying a
negatively curved locally symmetric metric. For a real-hyperbolic target
\((N,h_0)\) normalized by \(\operatorname{Ric}(h_0)=-h_0\) in dimension four,
it gives

\[
h_{\rm vol}(g)^4\operatorname{Vol}(M,g)
\ge9\,|\deg f|\operatorname{Vol}(N,h_0).                    \tag{6}
\]

If \(\operatorname{Ric}(g)\ge-g\), Bishop comparison gives
\(h_{\rm vol}(g)\le\sqrt3\), and therefore
\(\operatorname{Vol}(M,g)\ge|\deg f|\operatorname{Vol}(N,h_0)\).
Equality forces a locally isometric covering in the normalized metrics.

For the \(M\) of (1), however, its ordinary universal cover is \(M\) itself,
and every sufficiently large metric ball is all of \(M\). Consequently

\[
h_{\rm vol}(g)=
\lim_{r\to\infty}\frac1r\log\operatorname{Vol}_{\widetilde g}B(x,r)
=0                                                        \tag{7}
\]

for every smooth metric. The coarse blow-down has degree one on oriented
fundamental classes, but replacing \(N\) in (6) by \(\mathcal O\) would yield
\(0\ge9V_0>0\). Thus the proposed coarse-map inequality is false, including
on the actual metrics (2). This is not just a failure to locate a version
of BCG in the literature.

The group-level obstruction is equally explicit. On the regular part the
blow-down is the identity and induces the identity on \(\Gamma\). Any
orbifold-compatible extension producing the usual equivariant map between
universal covers would have to factor this identity through the quotient
in (5). That is impossible: the quotient kills the nontrivial \(t_j\).
In the Davis case every homomorphism \(\pi_1(M)\to\Gamma\) is trivial.
Similarly every ordinary map from \(M\) to a closed aspherical manifold
is null-homotopic: lift it to the contractible universal cover of the
target. In particular it has degree zero. Replacing the target by a smooth
hyperbolic finite cover, or using an ordinary finite cover of \(M\), does
not rescue (6); \(M\) has no nontrivial connected ordinary covers.

The same distinction defeats an ordinary simplicial-volume replacement.
The mapping/vanishing theorem gives \(\|M\|=0\) because \(\pi_1(M)=1\);
see [Gromov, *Volume and bounded cohomology*](https://www.numdam.org/item/PMIHES_1982__56__5_0/).
Pushing its fundamental class through the degree-one blow-down even gives
zero ordinary simplicial seminorm of the coarse quotient fundamental
class. Positive hyperbolic **orbifold** volume concerns the orbifold
covering structure, which this coarse map does not preserve. Finally,
(7) concerns volume entropy, not the topological entropy of the geodesic
flow; those should not be identified for these metrics.

## 5. The branched-cover repair has a concrete curvature defect

The branched cover \(Y\to M\) does admit an ordinary degree-one blow-down
to the smooth hyperbolic \(D\), so BCG is applicable to smooth metrics on
\(Y\). It does not follow that one may pull an Einstein metric on \(M\)
back to a smooth Einstein metric on \(Y\).

In normal complex coordinates the branch map is \(w=z^2\). Pulling the
normal Euclidean metric back gives

\[
|dw|^2=4\rho^2(d\rho^2+\rho^2d\phi^2)
=dR^2+4R^2d\phi^2,\qquad R=\rho^2.                        \tag{8}
\]

This is degenerate in smooth \(z\)-coordinates at the branch locus; in
distance coordinates it is a cone of angle \(4\pi\), not a smooth metric.
A naive local product smoothing necessarily develops unbounded negative
Ricci curvature. Indeed, smooth rotational normal disks
\(dR^2+f_\epsilon(R)^2d\phi^2\) have
\(f_\epsilon(0)=0\), \(f_\epsilon'(0)=1\). Matching (8) at an outer radius
\(\epsilon\) requires \(f_\epsilon'(\epsilon)=2\). Their Gaussian
curvature and area satisfy exactly

\[
\int K\,dA=-2\pi\int_0^\epsilon f_\epsilon''(R)\,dR=-2\pi.
                                                               \tag{9}
\]

If the smoothing disk area tends to zero, (9) rules out any uniform
curvature lower bound. In the product with the bolt this is also a Ricci
lower-bound obstruction. This calculation does not prohibit every possible
nonproduct global construction; it exhibits the precise defect in the
ordinary pullback-and-smooth argument.

The topology upstairs reinforces the distinction:

\[
\chi(Y)=148,\quad\tau(Y)=-122,\quad2\chi(Y)+3\tau(Y)=-70.
\]

Thus \(Y\) itself violates Hitchin--Thorpe and has no Einstein metric.
An Einstein metric downstairs is not ruled out by nonexistence upstairs
under a branched, rather than unbranched, covering.

## 6. The valid conditional entropy obstruction

For clarity the missing hypothesis can be isolated as a genuine theorem.
Let \(M'\) be an all-negative A1 resolution of any closed oriented
real-hyperbolic four-orbifold \((\mathcal O',g_0)\), with at least one
node, normalized by \(\operatorname{Ric}(g_0)=-g_0\), and write its volume
as \(V_0'\). Suppose there exists an **ordinary** map of nonzero degree

\[
f:M'\longrightarrow (N,h_0),\qquad
\operatorname{Ric}(h_0)=-h_0,
\qquad |\deg f|\operatorname{Vol}(N,h_0)\ge V_0',           \tag{10}
\]

where \(N\) is a closed real-hyperbolic manifold. Then \(M'\) has no
Einstein metric of any sign.

To prove this, nonnegative Ricci curvature would imply zero volume entropy,
contradicting (6). For a negative Einstein metric normalize
\(\operatorname{Ric}(g)=-g\). The A1 signature/Euler accounting gives
\(2\chi(M')+3\tau(M')=V_0'/(6\pi^2)\). Chern--Gauss--Bonnet and signature
then give

\[
\operatorname{Vol}(M',g)+3\int_{M'}|W_g^+|^2\,dV_g=V_0'.  \tag{11}
\]

BCG and (10) force equality in the volume inequality, hence make \(M'\)
a hyperbolic manifold. This is impossible: any exceptional sphere has
self-intersection \(-2\), so represents a nonzero class in \(H_2(M')\)
and a non-null-homotopic sphere, whereas a hyperbolic manifold is
aspherical. Notice that equality in (11) **alone** only gives
\(W^+=0\), not full hyperbolicity; the BCG equality theorem is essential.

For the concrete \(M\) in (1), (10) is impossible by simple connectivity.
Thus this correct all-sign theorem does not complete its Einstein
determination. Its unresolved negative-Einstein range is

\[
0<\operatorname{Vol}(M,g)\le156\pi^2,
\qquad \operatorname{Vol}(M,g)=156\pi^2-3\int|W^+|^2.
\]

Its trivial fundamental group also prevents Myers or the usual
virtually-abelian Ricci-flat fundamental-group restriction from excluding
nonnegative signs. Neither these facts nor absence of an almost-complex
structure is being promoted to nonexistence of arbitrary Einstein metrics.

## 7. Verification and research boundary

`python3 round6_entropy_check.py` verifies the exact rational topology,
covering, signature, parity, entropy-normalization and Chern--Weil
arithmetic, including all 123 chirality counts as a consistency check.
It does not verify Fine--Panov's geometric construction, the analytic
log-Weyl theorem, BCG, or the existence/nonexistence of an Einstein metric.

The new conclusion is a same-object obstruction to two tempting completion
routes: ordinary entropy cannot retain the original orbifold volume, and
complex-structure variation cannot produce a Kähler--Einstein metric here.
The all-sign Einstein question for this explicit \(M\) remains open in
this work. The existing near-Einstein construction is genuine input, not
an Einstein nonexistence theorem.
