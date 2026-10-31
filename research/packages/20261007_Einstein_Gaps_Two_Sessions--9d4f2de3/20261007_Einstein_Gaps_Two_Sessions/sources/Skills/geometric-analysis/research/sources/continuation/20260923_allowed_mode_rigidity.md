# An averaged Weyl test for exact allowed-mode rigidity

23 September 2026. Status: manuscript proofs, not an independent certification
or priority claim. All manifolds in the statements are connected and oriented.
The curvature normalization is \(\operatorname{Ric}=-g\); the scalar Laplacian
is nonnegative. Weyl tensors are regarded as self-adjoint endomorphisms of
\(\Lambda^+\).

## 1. The mathematical advance and its scope

The main result below gives an exact conclusion on a genuine allowed family:
for each diameter bound, a sufficiently small **averaged upper-eigenvalue
splitting** forces an Einstein metric on a product of closed hyperbolic
surfaces to be locally a hyperbolic product. It does not assume proximity to
a prescribed product metric, pointwise Weyl pinching, a lower Weyl amplitude,
or a preselected complex structure. It is uniform over the genera.

The new compactness step is that small splitting itself prevents curvature
bubbles. A putative Ricci-flat bubble has zero splitting. The Weyl equation
then forces that bubble to be anti-self-dual, and its compact core is
topologically forbidden. This differs from the earlier argument, which first
used pointwise relative pinching to bound \(W^+\).

Classical deformation theory is still essential: compactness identifies the
possible limits, and an unobstructed local moduli space rules out a nearby
non-Kähler Einstein branch. An integral estimate alone does not make its
right-hand side vanish.

**Dependencies and extensions.** The argument uses the compact-core proof in
[the inherited aspherical note](../mathematics/current/line1_aspherical_no_bubbles.md),
the Weyl eigenvalue calculation in
[the exact spectral application](../mathematics/current/line1_einstein_spectral_application.md),
and the classical inputs identified below. Section 8 removes the relative
pinching assumption from the exact-output shear theorem in that aspherical
note. The local product deformation result was already present in
[Round 18](../mathematics/current/round18_twisted_operator.md); it is not
claimed as new here. The compact realization theorem in
[the preceding continuation](20260923_compact_realization.md) has different
inputs: it treats approximate Einstein metrics, whereas the present exact
equation provides smooth curvature blow-ups.

Write
\[
 b_g=\lambda_3(W_g^+)-\lambda_2(W_g^+)\ge0,
 \qquad \mathscr S(g)=\frac1{V_g}\int_M b_g^2\,d\mu_g.       \tag{1}
\]
Ordered eigenvalues, including collisions and zeros, are allowed in (1).

## 2. The topological input does not require full asphericity

Use the following condition:
\[
 \pi_1(M)\text{ is torsion-free},\qquad \pi_2(M)=0.           \tag{TF2}
\]
Every closed aspherical manifold satisfies (TF2).

**Lemma 2.1 (compact-core exclusion).** No sufficiently large compact core
of a smooth nonflat Ricci-flat anti-self-dual ALE four-manifold embeds in
a closed oriented manifold satisfying (TF2).

**Proof.** The inherited core proof needs only the following facts about the
ambient universal cover: \(H_1=H_2=0\). These follow here from simple
connectivity, \(\pi_2=0\), and Hurewicz. A core \(B\) has finite fundamental
group, so an embedding into \(M\) lifts to an embedding into its universal
cover by torsion-freeness. If \(b_2(B)>0\), its negative-definite rational
intersection form is incompatible with \(H_2\) of the ambient cover being
zero. If \(b_2(B)=0\), the smooth ASD Ricci-flat ALE classification gives
\[
 H_1(B;\mathbb Z)=\mathbb Z_n,\quad
 H_1(\partial B;\mathbb Z)=\mathbb Z_{n^2},\quad n\ge2.
\]
Mayer--Vietoris in the ambient cover would identify
\(\mathbb Z_{n^2}\) with \(\mathbb Z_n\oplus H_1(C;\mathbb Z)\), where
\(C\) is the exterior and the second factor has order \(n\). Its exponent
is at most \(n\), a contradiction. The classification and rational-ball
case are precisely those detailed in the inherited proof; no assumption
that every bubble is simply connected or non-spin is used. \(\square\)

## 3. Why zero splitting kills the self-dual curvature of a bubble

**Lemma 3.1.** A complete Ricci-flat ALE four-manifold satisfying
\(\lambda_3(W^+)=\lambda_2(W^+)\) has \(W^+\equiv0\).

**Proof.** Put \(t=-3\lambda_1(W^+)/4\ge0\). Where \(t>0\), the lowest
eigenvalue is simple and
\[
 \operatorname{spec}(W^+)
   =\left(-\frac{4t}{3},\frac{2t}{3},\frac{2t}{3}\right),
 \qquad |W^+|^2=\frac83t^2.                                \tag{2}
\]
There is no need to orient its eigenline globally. At such a point the
Ricci-flat Weyl equation and the lowest-eigenvalue second derivative formula
give
\[
 \nabla^*\nabla W^+=6(W^+)^2-2|W^+|^2I,
\]
\[
 \Delta\lambda_1
 =6\lambda_1^2-2|W^+|^2
 -2\sum_{a=2}^3
 \frac{|\langle\nabla W^+ e_1,e_a\rangle|^2}
      {\lambda_1-\lambda_a}
 \ \ge\ \frac{16}{3}t^2.
\]
Multiplication by \(-3/4\) therefore yields
\[
                         \Delta t\le-4t^2.                 \tag{3}
\]
ALE curvature decay implies \(t\to0\) at infinity. If \(t\) were positive
somewhere, it would attain a positive global maximum. It is smooth there,
and the nonnegative Laplacian has \(\Delta t\ge0\) at a maximum, contrary
to (3). Thus \(t=0\), and (2) gives the assertion. \(\square\)

This is the decisive distinction between the negative Einstein scale and
the bubble scale. The negative Einstein equation allows the nonzero
Kähler root; at the Ricci-flat scale the restoring linear term disappears
and (3) eliminates that root on an ALE space.

## 4. Spectral no-bubbling, without pointwise spectral hypotheses

**Theorem 4.1.** Given \(D,v>0\), there are \(\varepsilon_0(D,v)>0\) and
\(K(D,v)<\infty\) such that every closed oriented four-manifold satisfying
(TF2), equipped with
\[
 \operatorname{Ric}_g=-g,\qquad
 \operatorname{diam}_gM\le D,\qquad V_g\ge v,
 \qquad \mathscr S(g)\le\varepsilon_0(D,v),                 \tag{4}
\]
satisfies \(\|\mathrm{Rm}_g\|_\infty\le K(D,v)\).
Consequently any such sequence with \(\mathscr S(g_j)\to0\) has a smooth
subsequence, modulo diffeomorphisms, on a fixed closed smooth manifold.

There is no Euler-characteristic bound, pointwise \(W^\pm\) bound,
eigenvalue simplicity, relative pinching or lower eigenvalue amplitude in
the hypotheses.

**Proof.** Bishop comparison gives
\[
 V_g\le V_D:=\operatorname{Vol}_{\mathbb H^4_{-1/3}}B_{D+1},
 \qquad \operatorname{Vol}_g B_r(x)\ge c(D,v)r^4
 \quad(0<r\le1).                                          \tag{5}
\]
The local bounded-Ricci, noncollapse curvature theorem of Jiang--Naber,
applied to a uniformly finite covering, gives
\[
                       \int_M|\mathrm{Rm}_g|^2\le E(D,v).  \tag{6}
\]
The number of covering balls is bounded using (5) and \(V_D\). Thus (6)
does not silently require a topological bound. One can instead assume a
full curvature-energy bound and omit this classical input, obtaining the
corresponding version with an additional constant dependency.

Suppose the theorem fails. Select metrics satisfying the first three
conditions of (4), with \(\mathscr S(g_j)\le1/j\), and with
\(Q_j=\max|\mathrm{Rm}_{g_j}|\to\infty\). At a maximum point rescale by
\(h_j=Q_jg_j\). Then
\[
 |\mathrm{Rm}_{h_j}|\le1,\quad
 |\mathrm{Rm}_{h_j}|(p_j)=1,\quad
 \operatorname{Ric}_{h_j}=-Q_j^{-1}h_j.                     \tag{7}
\]
Equation (5), rescaled at radii \(R/\sqrt{Q_j}\), gives all-center
noncollapse on every fixed radius of the rescaled sequence. Bounded
curvature, injectivity control and the exact Einstein equation give a
smooth pointed limit \((X,h,p)\). It is complete, Ricci-flat and nonflat,
has Euclidean lower volume growth, and has finite curvature energy by
(6) and four-dimensional scale invariance. The
Bando--Kasue--Nakajima asymptotic theorem therefore makes it ALE.

The splitting energy has the same scale invariance:
\[
 b_{Q_jg_j}=Q_j^{-1}b_{g_j},\qquad
 \int_M b_{h_j}^2\,d\mu_{h_j}
   =\int_M b_{g_j}^2\,d\mu_{g_j}
   \le V_D\mathscr S(g_j)\longrightarrow0.                 \tag{8}
\]
Smooth convergence on compact subsets and continuity of ordered
eigenvalues show \(b_h=0\). Lemma 3.1 forces \(W_h^+=0\). A sufficiently
large ALE core embeds in \(M_j\) by the actual smooth convergence maps,
contradicting Lemma 2.1. This proves the curvature bound.

Finally (5), the curvature bound and the diameter bound yield a uniform
injectivity radius and global smooth Einstein compactness. The limiting
manifold is diffeomorphic to the late members, not merely homeomorphic to
an orbifold limit. \(\square\)

## 5. Passing from compactness to an exact equality mode

The following formulation separates the global coverage statement from
the classical local deformation input.

**Proposition 5.1 (unobstructed allowed-mode criterion).** Let \(\mathcal C\)
be a collection of closed oriented smooth four-manifolds satisfying (TF2).
Fix \(D,v>0\). Assume that, whenever \(M\in\mathcal C\) admits a normalized
negative Einstein metric with \(b=0\) and \(W^+\not\equiv0\), its
lowest-eigenline orientation cover carries a negative Kähler--Einstein
structure whose infinitesimal complex deformations are all integrable.
Then there is \(\varepsilon(\mathcal C,D,v)>0\) such that every normalized
negative Einstein metric on a member of \(\mathcal C\), of diameter at
most \(D\) and volume at least \(v\), satisfies
\[
 \mathscr S(g)<\varepsilon(\mathcal C,D,v)
                         \quad\Longrightarrow\quad b_g=0. \tag{9}
\]
Such a metric is ASD or Kähler--Einstein on a cover of degree at most two.

It suffices more generally that each non-ASD zero-splitting limit have a
fixed finite cover on which it is KE with unobstructed complex
deformations. No uniform degree bound on these auxiliary covers is needed
for this qualitative contradiction argument.

**Proof.** Otherwise take nonzero-splitting metrics with \(\mathscr S\to0\).
Theorem 4.1 supplies smooth convergence on a fixed \(M\in\mathcal C\) to
\(g_\infty\) with \(b=0\). Derdziński's Proposition 5(iv) and Theorem 2
give the following alternatives for this compact negative Einstein limit:
\(W^+\equiv0\), or KE on the orientation cover of the lowest eigenline.
The nonparallel conformal-Kähler alternative produces a nonzero Killing
field on that compact cover, which negative Ricci curvature excludes by
Bochner.

In the ASD case, the chiral curvature operator is
\(R_+=W^++sI/12=-I/3\). Fine--Krasnov--Singer Theorem 1.2 gives local
Einstein rigidity. Late metrics, already known to converge smoothly, are
isometric to the limit and hence have \(b=0\).

In the KE case, fix the limit's eigenline cover (or the finite cover in the
generalized hypothesis) once and pull back every metric in the smoothly
identified sequence to it. There is no need to assert that the eigenlines
of the approximating metrics are orientable, or even simple. The lifted
metrics converge smoothly to the KE metric. By Koiso's local deformation
theory, in the form of Dai--Wang--Wei Theorem 3.3, every sufficiently close
Einstein metric is KE when all infinitesimal complex deformations of the
limit integrate. Its complex orientation agrees with that of the limit.
Thus the lifted late metrics have \(b=0\), and this local tensor identity
descends to \(M\), a contradiction. \(\square\)

The conclusion does not assume closeness to a chosen moduli neighborhood:
Theorem 4.1 and zero-splitting classification prove that every violating
sequence enters one. The integrability hypothesis is genuine. No theorem
here says that every negative KE surface is unobstructed or that a
second-order deformation calculation controls the full Einstein germ.

## 6. A concrete exact classification on products of curves

**Theorem 6.1.** For every \(D>0\) there is \(\varepsilon(D)>0\) such that,
for all \(g,h\ge2\), every Einstein metric \(k\) on the oriented smooth
product \(M=\Sigma_g\times\Sigma_h\) satisfying
\[
 \operatorname{Ric}_k=-k,\quad \operatorname{diam}_kM\le D,
 \quad\fint_M(\lambda_3(W_k^+)-\lambda_2(W_k^+))^2
       <\varepsilon(D)                                    \tag{10}
\]
is locally isometric to
\(\mathbb H^2_{-1}\times\mathbb H^2_{-1}\).
In particular, the spectral splitting is exactly zero. No claim that the
given marking is an isometric product marking is needed.

**Proof.** The canonical class of the product is an actual monopole class
with square
\(a^2=2\chi(M)=8(g-1)(h-1)\). Its self-dual projection has square at
least \(a^2\). The classical scalar monopole estimate, with scalar
curvature \(-4\), gives
\[
 16V_k\ge32\pi^2a^2,\qquad
                  V_k\ge4\pi^2\chi(M)\ge16\pi^2.          \tag{11}
\]
All these products are aspherical. If (10) did not imply the conclusion,
Theorem 4.1 and (11) would give smooth convergence of a violating sequence
with \(\mathscr S\to0\), modulo diffeomorphisms, on a fixed smooth product
\(M\). Its limiting Einstein metric \(k_\infty\) has \(b=0\).

An ASD limit is impossible. Since \(\tau(M)=0\), the signature formula
would then also force \(W^-=0\). The Einstein limit would have constant
sectional curvature \(-1/3\), contrary to Preissmann's theorem because
\(\pi_1(M)\) contains \(\mathbb Z^2\). Hence the limit is KE on its
lowest-eigenline orientation cover.

Here is the cover argument with the topology and marking retained. Identify
\(\pi_1(M)=\Pi_g\times\Pi_h\) using the smooth product. The orientation
character of the limit eigenline is
\[
 \xi:\Pi_g\times\Pi_h\longrightarrow\mathbb Z_2,
 \qquad \xi(a,b)=\xi_1(a)+\xi_2(b).
\]
Let \(K_i=\ker\xi_i\), allowing \(K_i=\Pi_i\). The subgroup
\(K_1\times K_2\subset\ker\xi\) defines a product cover
\[
 P=\Sigma_{g'}\times\Sigma_{h'}\longrightarrow M
                      \quad\text{of degree at most four}. \tag{12}
\]
It dominates the eigenline double cover; when \(\xi=0\), take \(P=M\).
Use precisely this one cover of the smoothly identified limiting manifold
for every member of the sequence. Thus the pulled-back metrics converge
smoothly on one fixed product \(P\) to a global negative KE metric.

The limit complex surface on \(P\) has ample canonical bundle, and is
projective. Catanese's Theorem 3.4, specifically its degree-one case proved
in Steps I--II on pages 16--18, applies because
\[
 \pi_1(P)=\Pi_{g'}\times\Pi_{h'},\qquad
 \chi(P)=4(g'-1)(h'-1).
\]
It identifies this complex surface biholomorphically with a product of
curves. Both the group and Euler conditions are used; a group-only
characterization is not being asserted. Uniqueness of the negative KE
metric then makes the lifted limit the normalized hyperbolic product.

All infinitesimal complex deformations of this product integrate. Indeed,
\(H^0(C_i,TC_i)=0\), and Künneth gives
\[
 H^1(C_1\times C_2,T(C_1\times C_2))
       =H^1(C_1,TC_1)\oplus H^1(C_2,TC_2).                 \tag{13}
\]
The product of the two smooth Teichmüller deformation families has
Kodaira--Spencer map equal to (13), and supplies all infinitesimal
directions. This proves unobstructedness; it does not use the generally
false assertion that \(H^2(TP)=0\).

Dai--Wang--Wei Theorem 3.3 now makes every sufficiently late lifted Einstein
metric KE. Applying Catanese's same degree-one statement to its complex
structure, and negative KE uniqueness, makes each such metric a hyperbolic
product as well. Local product geometry descends through (12), contradicting
the choice of sequence. Constants depend only on \(D\): the volume lower
bound in (11) is uniform, and the compactness contradiction selects its
own limit and local deformation neighborhood. \(\square\)

This proves an exact conclusion for the metric under test, not merely the
existence of some Einstein metric on its underlying manifold. The latter
was already known for products. It does not classify all Einstein metrics
on products without a small-splitting or bounded-diameter hypothesis, and
does not assert a globally oriented complex eigenline on the quotient.

## 7. The other allowed endpoint: a uniform ASD isolation statement

**Corollary 7.1.** For every \(D,v>0\) there is \(\eta(D,v)>0\) such that
a closed oriented four-manifold satisfying (TF2), with
\(\operatorname{Ric}=-g\), \(\operatorname{diam}\le D\), \(V\ge v\), obeys
\[
                \fint|W^+|^2<\eta(D,v)
                         \quad\Longrightarrow\quad W^+=0. \tag{14}
\]

**Proof.** Since \(b^2\le2|W^+|^2\), a counterexample sequence with the
left side tending to zero is smoothly precompact by Theorem 4.1. The
limit is ASD. Fine--Krasnov--Singer local rigidity at
\(R_+=-I/3\) makes all late normalized Einstein metrics isometric to the
limit, contradicting \(W^+\not\equiv0\). \(\square\)

This is a uniform integral criterion in a global bounded regime. The local
chiral rigidity theorem used to prove it is classical, not a new
infinitesimal rigidity theorem.

## 8. The same compactness removes pinching from the shear output gap

For the actual self-gluings \(M(q,g;u,f)\) of
\(F_{q,2}\times\Sigma_g\), take \(q\ge1\), \(g\ge2\), nonzero
\([u]\in H^1(\Sigma_g;\mathbb Z)\), and the precise marked gluing
\((\phi,x)\mapsto(-\phi+u(x),f(x))\) of the inherited theorem. Its
topological and monopole conclusions are inputs: asphericity,
\(\tau=0\), a subgroup \(\mathbb Z^2\subset\pi_1\), no finite Kähler
cover, and an actual class of square \(2\chi>0\).

**Corollary 8.1.** For each \(D>0\), all exact \(\operatorname{Ric}=-g\)
metrics on these actual self-gluings with diameter at most \(D\) satisfy
\[
                              \mathscr S(g)\ge\eta_D>0.    \tag{15}
\]
In particular the previous hypothesis \(b\le4\theta t\),
\(\theta<1/\sqrt3\), is no longer required.

**Proof.** The inherited monopole estimate supplies
\(V\ge4\pi^2\chi\ge16\pi^2\). A sequence violating (15) converges
smoothly by Theorem 4.1 to a zero-splitting Einstein metric on the same
smooth manifold as each sufficiently late term. Its KE-cover alternative
contradicts the virtual Kähler obstruction. Its ASD alternative gives
constant negative sectional curvature by \(\tau=0\), contradicting
\(\mathbb Z^2\subset\pi_1\). \(\square\)

This covers every exact negative Einstein output in the bounded-diameter
regime, not only metrics near the explicit gluing construction. It still
allows hypothetical outputs with definite spectral splitting or unbounded
diameter. It is not global Einstein nonexistence or a Yau26 counterexample.

## 9. What has and has not been connected

The actual implication proved here is
\[
 \begin{gathered}
 \text{exact negative Einstein + (TF2) + diameter/volume bounds}\\
 +\ \text{small averaged upper Weyl splitting}\\
 \Longrightarrow\ \text{smooth compactness}\\
 \Longrightarrow\ \text{ASD or KE-covered limit}\\
 +\ \text{an exhausted local Einstein germ}\\
 \Longrightarrow\ \text{exact allowed geometry}.
 \end{gathered}                                             \tag{16}
\]
The product application verifies the local-germ condition on an actual
family; the ASD application uses classical chiral rigidity. Neither
replaces a missing integrability assumption by a small-error estimate.
For a general obstructed negative KE surface, whether a nearby non-Kähler
Einstein branch exists is not decided here. Likewise, the diameter and
volume regime is not supplied for arbitrary Yau26 inputs. These are the
remaining mathematical arrows, not conclusions to be inserted into (16).

The contribution relative to the inherited project is the spectral
no-bubbling bridge and its uniform exact-output consequences. The Weyl
identity, ALE classification, local moduli exhaustion, and complex product
characterization are external or inherited ingredients. The uniform
constants are qualitative; no sharpness or global novelty is claimed.

## 10. Primary-source register

- W. Jiang and A. Naber, *L2 Curvature Bounds on Manifolds with Bounded
  Ricci Curvature*: [arXiv:1605.05583](https://arxiv.org/abs/1605.05583).
  The local curvature-energy theorem supplies (6).
- S. Bando, A. Kasue and H. Nakajima, *On a construction of coordinates at
  infinity on manifolds with fast curvature decay and maximal volume
  growth*: [Inventiones 97 (1989)](https://doi.org/10.1007/BF01389045),
  Theorem 1.5, supplies ALE asymptotics of the complete Ricci-flat limit.
- E. P. Wright, *Quotients of gravitational instantons*:
  [arXiv:1102.2442](https://arxiv.org/abs/1102.2442), and I. Suvaina,
  *ALE Ricci-flat Kähler metrics and deformations of quotient surface
  singularities*: [arXiv:1102.2672](https://arxiv.org/abs/1102.2672).
  These are the classification inputs of the inherited compact-core proof.
- A. Derdziński, *Self-dual Kähler manifolds and Einstein manifolds of
  dimension four*: [Compositio 49 (1983)](https://www.numdam.org/article/CM_1983__49_3_405_0.pdf),
  Proposition 5(iv) and Theorem 2. The eigenline may require a double cover.
- X. Dai, X. Wang and G. Wei, *On the stability of Kähler--Einstein
  metrics*: [author PDF](https://web.math.ucsb.edu/~wei/paper/dww3.pdf),
  Theorems 3.2--3.3. Theorem 3.3, not Theorem 3.6, contains the local
  assertion that all nearby Einstein metrics are KE under integrability.
- F. Catanese, *Fibred surfaces, varieties isogenous to a product and
  related moduli spaces*: [American Journal of Mathematics 122 (2000)](https://www.mathe8.uni-bayreuth.de/de/team/prof-fabrizio-catanese-old/pdf/066.pdf),
  Theorem 3.4 and its degree-one proof, pp. 16--18. No general claim about
  irreducibility of the full moduli space is used.
- J. Fine, K. Krasnov and M. Singer, *Local rigidity of Einstein
  4-manifolds satisfying a chiral curvature condition*:
  [arXiv:1910.09790](https://arxiv.org/abs/1910.09790), Theorem 1.2.
- C. LeBrun, *Ricci curvature, minimal volumes, and Seiberg--Witten
  theory*: [original paper](https://arxiv.org/abs/math/0003068).
  The scalar monopole inequality gives (11); no new SW existence statement
  is being proved in this note.

The [exact algebra check](check_allowed_mode_algebra.py) verifies the
curvature-operator normalization and the change from the negative Einstein
amplitude equation to the Ricci-flat one. It does not verify the
eigenvector-derivative term, compactness, or deformation theory.
