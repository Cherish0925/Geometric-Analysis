# Asphericity excludes half-flat ALE bubbles

23 September 2026. This note strengthens the
[bounded-geometry result](line1_allowed_branch_escape.md): for the actual aspherical shear
manifolds, the assumed bound on the opposite Weyl curvature can be
removed. Spin is not required. The key point is a compact-core embedding
obstruction which treats both negative-definite ALE cores and the
non-simply-connected rational-ball cores.

## 1. A topological obstruction to ALE cores

**Lemma 1.** Let \(M\) be a closed aspherical smooth oriented
four-manifold. No sufficiently large compact core of a nonflat smooth
Ricci-flat anti-self-dual ALE four-manifold \(X\) embeds smoothly in
\(M\).

The orientation on an ALE core is the one for which \(W^+=0\).
Reversing the orientation of an embedding does not change the
non-embedding conclusion.

**Proof.** Take a large compact core \(B\subset X\) with connected
boundary \(Y=S^3/\Gamma\) and cylindrical complement. Thus \(B\) has
the homotopy type of \(X\). Its fundamental group is finite. Since
\(M\) is a closed aspherical manifold, \(\pi_1(M)\) is torsion-free
and its universal cover \(\widetilde M\) is contractible. If
\(i:B\hookrightarrow M\) were an embedding, then \(i_*\pi_1(B)\)
would be trivial. The covering-space lifting criterion therefore lifts
\(i\) to an embedding \(\widetilde i:B\hookrightarrow\widetilde M\).
It is the core itself that lifts: no injectivity assertion about the
fundamental group of a geometrical limit is being made. The lift is
injective because its composition with the covering projection is the
original embedding.

Wright's classification gives a negative-definite rational intersection
form on \(H_2(B;\mathbb Q)\). If \(b_2(B)>0\), choose a nonzero
rational class with negative square. Represent an integral multiple by
a compact cycle and a transverse push-off in the interior of \(B\).
Their intersection number is unchanged by the embedding. In the
contractible ambient manifold both classes are zero, so their
intersection is zero. This is a contradiction.

It remains to treat \(b_2(B)=0\). Wright's theorem, combined with
Suvaina's classification of Ricci-flat Kähler ALE surfaces, gives
\[
 \pi_1(B)\cong\mathbb Z_n,\qquad
 Y\cong L(n^2,nr-1),\qquad n\ge2,\quad (n,r)=1.            \tag{1}
\]
In particular, \(H_1(B;\mathbb Z)=\mathbb Z_n\) and
\(H_1(Y;\mathbb Z)=\mathbb Z_{n^2}\). The nonflat assumption
excludes the trivial Euclidean case \(n=1\).

Put \(C=\widetilde M\setminus\operatorname{int}B\). Use small
collar enlargements to apply ordinary Mayer--Vietoris to
\(\widetilde M=B\cup_Y C\); compactness of the ambient manifold is
not required. Since its first and second homology vanish, the exact
sequence gives an isomorphism
\[
 \mathbb Z_{n^2}=H_1(Y;\mathbb Z)
       \cong H_1(B;\mathbb Z)\oplus H_1(C;\mathbb Z)
       =\mathbb Z_n\oplus H_1(C;\mathbb Z).                 \tag{2}
\]
The second factor must have order \(n\). Therefore every element on
the right is annihilated by \(n\), while the left has an element of
order \(n^2\). This is impossible for every \(n\ge2\), composite
or prime. The two cases exhaust the smooth nonflat ASD Ricci-flat ALE
classification. This proves the lemma.

### Why a spin-only argument would fail

There are spin rational-ball ALE spaces in (1). For example, take the
three-centre Gibbons--Hawking space with centres in a regular triangle
and its free cyclic quotient of order three supplied by Wright's
construction. The covering space is hyperkähler and spin. Pull-back
on mod-two cohomology is injective for an odd-degree cover (transfer
composed with pull-back is multiplication by three), so the quotient
is also spin. It has \(b_2=0\), fundamental group \(\mathbb Z_3\)
and a lens end of order nine. Lemma 1 excludes its embedding by (2),
not by a false assertion that rational-ball bubbles are non-spin.

## 2. Half-Weyl bounds give full curvature control on aspherical types

**Theorem 2.** Fix \(v>0,D>0,\Lambda>0\) and \(\chi_0<\infty\).
There is a constant \(C(v,D,\Lambda,\chi_0)\) such that every closed
aspherical oriented Einstein four-manifold satisfying
\[
 \operatorname{Ric}=-g,\quad V\ge v,\quad
 \operatorname{diam}(g)\le D,\quad \|W^+\|_\infty\le\Lambda,
 \quad \chi(M)\le\chi_0                                    \tag{3}
\]
has \(\|\operatorname{Rm}\|_\infty\le C\).

**Proof.** Suppose a sequence violates the conclusion and set
\(Q_j=\max|\operatorname{Rm}_{g_j}|\to\infty\), attained at \(p_j\).
Rescale by \(\widehat g_j=Q_jg_j\). Then
\[
 |\operatorname{Rm}_{\widehat g_j}|\le1,\quad
 |\operatorname{Rm}_{\widehat g_j}|(p_j)=1,\quad
 \operatorname{Ric}_{\widehat g_j}=-Q_j^{-1}\widehat g_j,
 \quad |W^+_{\widehat g_j}|\le\Lambda/Q_j.                  \tag{4}
\]
Relative Bishop comparison, using \(V\ge v\) and diameter \(D\),
gives \(\operatorname{Vol}_{g_j}B_r(x)\ge c(v,D)r^4\) for
\(0<r\le D\). After rescaling this holds on every fixed finite
radius for all sufficiently large \(j\). The curvature bound in (4)
and this noncollapse give injectivity-radius control and smooth pointed
Einstein compactness. The limit \((X,g_\infty,p)\) is complete,
Ricci-flat, anti-self-dual, has Euclidean lower volume growth, and is
nonflat because \(|\operatorname{Rm}|(p)=1\).

Einstein Chern--Gauss--Bonnet and \(\chi\le\chi_0\) give a uniform
full \(L^2\) curvature bound, unchanged by rescaling. The limit
therefore has finite curvature energy. The classical
Bando--Kasue--Nakajima asymptotic theorem makes it an ALE space.
Equivalently this is the smooth deepest-bubble case of Einstein
compactness. Choosing a global curvature maximum ensured a smooth
limit; an unproved classification of intermediate orbifold bubbles is
not needed.

Smooth pointed convergence embeds every fixed compact subset of \(X\)
into \(M_j\) for sufficiently large \(j\). Choose a large ALE core.
Lemma 1 forbids precisely this embedding. This contradiction proves
the theorem. No spin, simply-connected-bubble or global complex-gluing
assumption has entered the proof.

## 3. A diameter-only spectral gap on the actual shear family

Let \(M=M(q,g;u,f)\) be the self-gluing of
\(F_{q,2}\times\Sigma_g\), with \(q\ge1\), \(g\ge2\), under
\[
 (\phi,x)\longmapsto(-\phi+u(x),f(x)),
 \qquad f\in\operatorname{Diff}^+(\Sigma_g),\qquad
 0\ne[u]\in H^1(\Sigma_g;\mathbb Z).
\]
These are the explicit self-gluings covered by the complete virtual
Kähler and actual monopole arguments of Rounds 11--12; no arbitrary
multi-block assembly is included by implication. No order condition on
the mapping class of \(f\) is imposed. The inherited results give:

- \(M\) is aspherical and \(\tau(M)=0\);
- no finite cover is Kähler;
- \(\pi_1(M)\) contains \(\mathbb Z^2\);
- \(\chi(M)=4q(g-1)\), and an actual monopole class has square
  \(A=2\chi(M)>0\).

As before, write
\[
 t=-3\lambda_1(W^+)/4,\quad b=\lambda_3(W^+)-\lambda_2(W^+),
 \quad\mathscr S(g)=\fint b^2.
\]

**Theorem 3.** For every \(D>0\) and \(0\le\theta<1/\sqrt3\)
there is \(\varepsilon(D,\theta)>0\) such that every normalized
negative Einstein metric on any member of this actual shear family
with
\[
                  b\le4\theta t,
                  \qquad\operatorname{diam}(g)\le D         \tag{5}
\]
satisfies \(\mathscr S(g)\ge\varepsilon(D,\theta)\).
Zeros of \(W^+\) are allowed. There is no lower amplitude, opposite
Weyl, full-curvature, injectivity-radius or separately assumed
noncollapse bound.

**Proof.** The previously established maximum principle, applied at a
positive maximum of \(t\), gives
\(t\le[2(1-3\theta^2)]^{-1}\) and hence a uniform bound on
\(W^+\). At such a maximum the lowest eigenvalue is simple since
\(\lambda_2-\lambda_1\ge2(1-\theta)t>0\). The case \(t\equiv0\)
needs no maximum argument.

The actual monopole scalar inequality gives
\[
                       V\ge4\pi^2\chi(M).                  \tag{6}
\]
In this family \(\chi(M)\ge4\), so \(V\ge16\pi^2\).
Bishop comparison gives a diameter-dependent upper volume bound.
Consequently (6) also bounds \(\chi(M)\) in terms of \(D\).
All constants in Theorem 2 are thus controlled by \(D,\theta\),
uniformly across the family. Full curvature is bounded, and the
geometric compactness used in the preceding note follows.

If splitting energies tended to zero, the smooth limit would be exact
negative Einstein with at most two self-dual Weyl eigenvalues.
Derdziński's classification gives a KE metric on a cover of degree
at most two, or an ASD metric. The first contradicts the inherited
virtual Kähler obstruction. The second, together with the preserved
signature zero, has \(W^-=0\), so is real hyperbolic; Preissmann's
theorem excludes its \(\mathbb Z^2\) subgroup. This proves the
uniform gap.

**Corollary 4.** Every exact Einstein sequence on these manifolds with
fixed \(\theta<1/\sqrt3\) and \(\mathscr S(g_j)\to0\) satisfies
\[
                          \operatorname{diam}(g_j)\to\infty.
\]
This replaces the former alternative "diameter escape or opposite-Weyl
blow-up" by diameter escape alone, in this actual aspherical family.
It still permits arbitrary exact Einstein metrics outside the relative
pinching class, or with a splitting bounded away from zero, and it does
not establish their nonexistence.

## 4. Sources and precise status

1. Wright, *Quotients of gravitational instantons*, Theorem A,
   Remark 3 and Corollary C:
   <https://arxiv.org/pdf/1102.2442>.
2. Suvaina, *ALE Ricci-flat Kähler metrics and deformations of quotient
   surface singularities*, Theorem B, Theorem 2.2, Proposition 3.3 and
   its classification proof: <https://arxiv.org/pdf/1102.2672>.
   These give the cyclic fundamental group and the lens boundary in
   (1), not merely the existence of one chosen rational ball.
3. Bando--Kasue--Nakajima, *On a construction of coordinates at
   infinity on manifolds with fast curvature decay and maximal volume
   growth*, Invent. Math. 97 (1989), 313--349:
   <https://doi.org/10.1007/BF01389045>.
4. Derdziński, Proposition 5 and Theorem 2:
   <https://www.numdam.org/article/CM_1983__49_3_405_0.pdf>.
5. Actual objects: `round11_graph_topology.md`, `round11_kahler.md`,
   `round12_global.md`; spectral calculation and initial escape proof:
   `line1_einstein_spectral_application.md`,
   `line1_allowed_branch_escape.md`.

The classification and compactness inputs are classical. The compact-core
exclusion is proved explicitly above, including the rational-ball case
that a sphere-only or spin-only argument misses. No exhaustive
publication-priority assertion is made. The result removes an actual
curvature assumption from the preceding all-output spectral application;
it does not claim to solve the unrestricted negative Einstein problem.
