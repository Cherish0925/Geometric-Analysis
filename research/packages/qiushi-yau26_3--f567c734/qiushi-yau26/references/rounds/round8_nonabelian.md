# A convention-independent obstruction to the reducible nonabelian bridge

Let M be a closed oriented Riemannian four-manifold and put
T=2 chi(M)+3 tau(M). This note proves a quantitative obstruction for
the actual graded connection used in nonabelian uniformization, without
identifying the ambiguous quadratic-map sign from round 7.

For T>0, a rank-one construction that leaves a line in the target spinor
bundle uncoupled cannot produce the projectively anti-self-dual connection
required by that argument. The obstruction also controls approximately
uncoupled lines. It is not an obstruction to all rank-two solutions and
does not decide whether E_D carries an Einstein metric.

## 1. The connection whose curvature must vanish projectively

Fix a spin-c structure with determinant L, write a=c1(L), and let
E=S_L^+. The relevant rank-four bundle is

\[
                  V=S_L^-\oplus E,\qquad c_1(V)=2a.
                                                               \tag{1}
\]

Give V its positive direct-sum Hermitian metric h_0 and the indefinite
metric H=h_{S^-}-h_E. Let Gamma=diag(I_2,-I_2). A connection of the
form used in Leung's construction is

\[
 D=\begin{pmatrix}\nabla^-&\Theta^*\\ \Theta&A\end{pmatrix},
 \qquad \Theta\in\Omega^1\operatorname{Hom}(S_L^-,E),
                                                               \tag{2}
\]

where the diagonal connections are unitary. It preserves H. In the
spinor construction, Theta is obtained from
phi in Hom(S_L^+,E) by Clifford multiplication. Scalar factors and a
consistent interchange of the off-diagonal adjoint notation make no
difference to the argument below.

For End(V)-valued two-forms define

\[
 *_\Gamma F=\Gamma(*F)\Gamma,\qquad
 Y=\frac12(F_D+*_\Gamma F_D),\qquad
 Z=Y-\frac14(\operatorname{tr}Y)I_V.                     \tag{3}
\]

Thus diagonal blocks are projected onto ordinary self-dual forms and
off-diagonal blocks onto ordinary anti-self-dual forms. The positive norm
of Z is the Hilbert--Schmidt norm from h_0, not the indefinite form H.
The connection is projectively anti-self-dual in this graded sense
exactly when Z=0.

These are the bundle, block connection, and modified Hodge operator
in [Leung, J. reine angew. Math. 519 (2000), pp. 23--25,
Proposition 2.4](https://archive.ymsc.tsinghua.edu.cn/pacm_download/60/582-2000_Leung_NonAbelian_SW_eqt_on_Einstein_mfd_Crelle_Journal.pdf).
The cited implication needed for uniformization is that a solution of
the paper's nonabelian system on an Einstein metric supplies Z=0.
We use this implication, not its displayed central-curvature coefficient
or an identification of its quadratic map with an ordinary SW convention.

## 2. A line-curvature inequality

The following estimate holds in any rank r. Suppose V has a Hermitian
grading Gamma, D is compatible with the corresponding indefinite metric,
and K is a smooth line subbundle contained in one grading summand.
Let P be its h_0-orthogonal projection. Write c=c1(V), k=c1(K), and
define Y and Z as in (3), replacing 1/4 by 1/r.
Use the Chern convention c1=[i tr(F)/(2 pi)]. For a real cohomology
class x, (x^+)^2 denotes the squared norm of its harmonic self-dual part.

**Lemma 1.** The induced unitary connection on K satisfies

\[
 2\pi\sqrt{((k-c/r)^+)^2}
 \le\sqrt{\frac{r-1}{r}}\,\|Z\|_{L^2}
                              +2\|D P\|_{L^4}^2.       \tag{4}
\]

If K is D-parallel, this specializes to

\[
 \int_M|Z|^2\ge
 \frac{4\pi^2}{r(r-1)}\,((rk-c)^+)^2.                 \tag{5}
\]

Here DP is the covariant derivative in End(V) for the connection D.
It measures mixing by both the diagonal connection and Theta; it is
not merely the derivative of the topological line field in a fixed gauge.

**Proof.** The connection induced on K is P D. For sections of K,
the curvature identity for a projection is

\[
 F_K=\operatorname{tr}(P F_D)
                     +\operatorname{tr}(P(DP\wedge DP)).        \tag{6}
\]

It follows directly by expanding (P D)^2 and using P(DP)P=0.
The induced connection is unitary because K is definite for H and P
is also the H-orthogonal projection onto K.

Since P commutes with Gamma, taking the ordinary self-dual part of
the first term of (6) gives tr(PY). Also
tr Y=(tr F_D)^+. Consequently

\[
 F_K^+-\frac1r(\operatorname{tr}F_D)^+
       =\operatorname{tr}(PZ)+\beta,
 \qquad \beta=\big[\operatorname{tr}(P(DP\wedge DP))\big]^+.
                                                               \tag{7}
\]

The trace-free matrix P-I/r has norm sqrt((r-1)/r), so

\[
 |\operatorname{tr}(PZ)|
       \le\sqrt{(r-1)/r}\,|Z|.
\]

Furthermore |beta|<=2|DP|^2. For example in an orthonormal tangent
frame, its unprojected ij component is
tr(P[(D_iP),(D_jP)]). Matrix Cauchy--Schwarz bounds its absolute value
by 2|D_iP||D_jP|, and summing over i<j gives the stated bound (with
room to spare). Self-dual projection does not increase the norm.

Harmonic projection of the left side of (7) has norm
2 pi sqrt(((k-c/r)^+)^2), by Chern--Weil theory. Harmonic projection
is an L2 contraction. Applying it to (7), then the triangle inequality
and the two pointwise estimates, proves (4). Setting DP=0 and squaring
gives (5). No elliptic estimate or noncollapse hypothesis is used. QED.

For a parallel line the same sharp coefficient in (5) can be seen
directly: if z is the K block of a trace-free matrix, the trace of the
complementary block is -z, and its squared norm is at least
|z|^2/(r-1). This also explains why the coefficient is not obtained
by keeping the line block alone.

## 3. The spinor characteristic classes force a positive defect

Assume now that E=S_L^+ has a smooth line subbundle K. Its orthogonal
complement R is another line bundle. The spinor characteristic identity is

\[
           a^2-4c_2(E)=2\chi(M)+3\tau(M)=T.            \tag{8}
\]

For completeness, the real bundle su(E) is Lambda^+;
p1(su(E))=c1(E)^2-4c2(E) and
p1(Lambda^+)=p1(TM)+2e(TM). Integrating p1(TM)=3 tau and e(TM)=chi
proves (8). Since c2(E)=k(a-k), the class

\[
                             b=2k-a
\]

satisfies b^2=T, independently of the chosen spin-c structure or
line splitting. In particular (b^+)^2>=T.

**Theorem 2 (critical-energy obstruction to reducibility).** If T>0,
every connection (2) and every smooth line K in E satisfy

\[
 \boxed{\quad
 \pi\sqrt T\le\frac{\sqrt3}{2}\|Z\|_{L^2}
                                  +2\|DP\|_{L^4}^2.
 \quad}                                                   \tag{9}
\]

In particular:

* If D preserves K, then

  \[
     \boxed{\quad\int_M|Z|^2\ge\frac{4\pi^2}{3}T>0.\quad}
                                                               \tag{10}
  \]

* If Z=0, then every such line has

  \[
                     \int_M|DP|^4\ge\frac{\pi^2}{4}T.  \tag{11}
  \]

**Proof.** Apply (4) with r=4 and c=2a. Then k-c/r=b/2.
Its harmonic self-dual norm is at least sqrt(T)/2. Equations
(9)--(11) follow. QED.

Both norms in (9) have the critical scaling in dimension four:
integral |Z|^2 and integral |DP|^4 are unchanged by constant metric
rescaling. The theorem imposes no scalar or Ricci bound. It is an
estimate for the connection built on the actual spinor bundles, not a
curvature-profile model.

## 4. The specific rank-one transfer is excluded at the connection level

Suppose the proposed pair is reducible in the following precise sense:

\[
 E=R\oplus K,\qquad A=A_R\oplus A_K,\qquad
              \operatorname{image}\phi\subset R.        \tag{12}
\]

Clifford multiplication acts on the source of phi, so the associated
Theta also has image in R. Hence Theta* vanishes on K. The connection
(2) preserves K, and (10) applies.

**Corollary 3.** On an Einstein four-manifold with T>0, no pair of
the form (12) can supply the projectively anti-self-dual connection
required by Leung's nonabelian uniformization argument. This statement
is independent of the ordinary/nonabelian quadratic-map sign.

The earlier direct proposal E=L plus C, phi=(j psi,0), and
A=A_1 plus flat is a special case. Changing A_K to a nonflat unitary
connection does not fix it. Nor does replacing the trivial complementary
line by another line splitting: (8) keeps the same positive lower bound.
This is stronger than observing that the unused flat line has zero
curvature while the other block has nonzero central curvature.

For the canonical spin-c structure of E_D there is a smooth splitting
E=C plus L, T=2 chi(E_D)>0. The result therefore closes this reducible
transfer route on that actual topology, not just on complex surfaces.
For its genuine Ric approximately -g family, whose volume tends to
V*=2 pi^2 T, (10) gives the actual metric-dependent bound

\[
 \fint_M|Z|^2\ge\frac{4\pi^2 T}{3\operatorname{Vol}(g)},
 \qquad \liminf\fint_M|Z|^2\ge\frac23.                  \tag{13}
\]

for every reducible ansatz (12). Thus the actual approximate Einstein
construction does not turn these connections into small projective-ASD
seeds. More generally (9) excludes a family for which both
||Z||2/sqrt(T) and ||DP||4^2/sqrt(T) tend to zero. It does not exclude
a genuinely coupled family with the mixing required by (11).

There is an exact perturbative formulation. If D_0 preserves such a
line K and D=D_0+B is projectively ASD, then DP=[B,P]. For an
orthogonal projection the Hilbert--Schmidt inequality
|[B,P]|<=|B| follows in a frame with P=diag(1,0,0,0): the commutator
keeps only off-diagonal entries joining K to its complement. Thus

\[
                    \int_M|D-D_0|^4\ge\frac{\pi^2}{4}T.\tag{14}
\]

This holds for every such D_0, not just a fixed reference connection.
It is also unchanged by simultaneous h_0-unitary, grading-preserving
gauge transformations. In this precise critical L4 distance, the
required projectively ASD connections are uniformly separated from
the reducible ones.

## 5. Complex-ball quotients provide a geometric sharpness check

Let M be a compact complex-hyperbolic surface, with its complex
orientation and its canonical spin-c structure L=K_M^(-1). Let B be the
Chern connection on L. It has harmonic self-dual curvature F_B and
a^2=T>0. The ordinary SW construction in
[Leung, Math. Ann. 306 (1996), Theorem 2, printed p. 43](https://archive.ymsc.tsinghua.edu.cn/pacm_download/60/591-1996_Leung_SW_inv__Uniformization_Math_Annalen.pdf)
gives a projectively flat U(2,1) connection D_0 on

\[
                         V_0=S_L^-\oplus\mathbb C.
\]

The bundle and canonical-line convention are on printed p. 40; the
connection with symmetric off-diagonal coefficient 1/sqrt(6) is on
p. 41. The curvature calculation on p. 42 gives central self-dual
curvature -F_A^+/3, where the author's A is on K_M. Our B is the
dual connection on L=K_M^(-1), so F_B=-F_A. The equality assertion in
Theorem 2 on p. 43 makes this connection projectively flat for the
complex-ball quotient (3 tau=chi). Thus its full, not merely self-dual,
curvature is central. These precise connection and curvature statements
are the external input to the sharpness example.

The two diagonal determinant connections are B and the trivial
connection, so trace F_{D_0}=F_B. Projective flatness therefore fixes
its full central curvature without any quadratic-map convention:

\[
                          F_{D_0}=\frac13F_B I_3.       \tag{15}
\]

Dualize D_0 and twist by (L,B). The resulting rank-three bundle is

\[
 V_0^*\otimes L
   =((S_L^-)^*\otimes L)\oplus L
   \simeq S_L^-\oplus L,
\]

using the canonical rank-two identity W* tensor det(W) isomorphic to W.
Its curvature is (2/3)F_B I_3. Append a flat trivial line. The resulting
rank-four bundle is precisely S_L^- plus S_L^+, its connection has
the form (2) with an uncoupled line, and its curvature is

\[
              F_D=\operatorname{diag}
                   (2F_B/3,2F_B/3,2F_B/3,0).
\]

Since F_B is self-dual, the modified projection leaves it unchanged.
Its trace-free part has diagonal entries

\[
                         (F_B/6,F_B/6,F_B/6,-F_B/2).
\]

Consequently

\[
 \int|Z|^2=\frac13\int|F_B|^2
                      =\frac{4\pi^2}{3}a^2
                      =\frac{4\pi^2}{3}T.               \tag{16}
\]

Thus (10) is sharp on actual geometry. This calculation also pinpoints
what goes wrong with adjoining an unused line to the rank-three
uniformization connection: its central curvature no longer agrees
with that of the added line. A sign convention cannot repair that
determinant-curvature mismatch.

This is consistent with positive-signature complex-ball quotients:
their ordinary canonical solutions supply the rank-three construction,
not a reducible rank-four projectively ASD connection. No contradiction
with the nonabelian signature theorem is being asserted.

## 6. What is resolved, and what remains open

The obstruction in Corollary 3 is a proved statement about the
connection-level compatibility needed by the published theorem. It no
longer depends on identifying tau(j psi) with either plus or minus the
ordinary quadratic map. The precise absolute sign of the printed
quadratic notation remains unassigned here; neither a sign guess nor
the round-7 literal-projection model is used as a premise.

The distinction from a general rank-one assertion is important:
pointwise rank(phi)<=1 does not imply that its image extends to an
A-parallel line bundle. The theorem treats (12), and its quantitative
extension (9), not every possible rank-one field with zeros and a
non-splitting connection.

For E_D the unresolved global bridge remains a genuinely coupled
rank-two solution satisfying all of Leung's hypotheses for every
putative Einstein metric. The conditional uniformization reduction in
round7_rigidity.md remains valid. This note neither supplies such a
solution nor excludes one; it proves that a reducible ordinary-monopole
insertion, including a small critical-energy perturbation of it, cannot
provide the required connection.

The independent [representation calculation](round8_construction.md)
now obstructs factor-preserving product-hyperbolic holonomy and
nonzero-degree maps to negatively curved four-manifolds on the same
E_D. It does not supply the missing coupled rank-two solution either.

[round8_nonabelian_check.py](round8_nonabelian_check.py) checks the
finite-dimensional inequalities, projection identities, characteristic
class cancellation and sharp curvature blocks. It does not verify the
existence theorem for the cited rank-three connection or solve a PDE.
