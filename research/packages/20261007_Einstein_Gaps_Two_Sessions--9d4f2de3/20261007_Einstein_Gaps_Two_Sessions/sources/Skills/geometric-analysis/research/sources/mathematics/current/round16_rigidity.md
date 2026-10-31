# Product-profile propagation into collapsing Einstein regions

## 1. A quantitative extension of the product-boundary theorem

Let \(M\) be a closed oriented four-manifold with \(\tau(M)=0\),
\(A=2\chi(M)>0\), and actual monopole classes of square \(A\) in
both orientations, as in [Round 15](round15_rigidity.md).
Consider an exact Einstein metric

\[
 \operatorname{Ric}_g=-3g,\qquad
 D=9\operatorname{Vol}_g(M)-2\pi^2A\geq0.
 \tag{1}
\]

Let \(\mathscr P_3\) be the orthogonal orbit of the curvature operator
of \(\mathbb H^2_{-3}\times\mathbb H^2_{-3}\), and write

\[
 f(p)=\operatorname{dist}_{\rm HS}
              (\mathcal R_g(p),\mathscr P_3),\qquad
 v(p)=\operatorname{Vol}_g B_1(p).
 \tag{2}
\]

Curvature-operator norms are Hilbert--Schmidt norms on two-forms;
the squared full four-index curvature norm is four times the squared
operator norm.

**Theorem 1 (relative local product estimate).** There are universal
constants \(D_0,\varepsilon_0>0\) and \(C<\infty\) such that

\[
 D\leq D_0,\qquad \frac D{v(p)}\leq\varepsilon_0
 \quad\Longrightarrow\quad
 \boxed{\sup_{B_{1/4}(p)}
       \bigl(f+|\nabla\operatorname{Rm}|\bigr)
       \leq C\left(\frac D{v(p)}\right)^{1/2}.}
 \tag{3}
\]

There is no positive lower bound on \(v(p)\) among the hypotheses.
In particular, (3) remains effective on collapsing balls whenever
their volume decays more slowly than the absolute excess \(D\).
The proof takes place on the original manifold; no absolute integral
is lifted to a local cover.

The analytic statement is not specific to monopoles: on a complete
Einstein four-manifold with \(\operatorname{Ric}=-3g\) and
\(|\operatorname{Rm}|\leq K\), replace \(D\) throughout (3) by
\(E=\int f^2<\infty\), with constants depending on \(K\).
The Einstein derivative bound follows from the homothetically
expanding complete Ricci flow and the usual curvature derivative
estimate. Sections 3--6 prove this version too. Monopoles enter
the stated application through the quantitative input (7) and the
uniform curvature bound (8).

For fixed \(M\), Round 15 supplies a point \(x\) with
\(v(x)\geq v_0(M)>0\). Bishop--Gromov then gives the following.

**Corollary 2 (logarithmic propagation).** There are \(c_M,C_M>0\)
such that, whenever \(D e^{3d_g(x,p)}\leq c_M\),

\[
 \boxed{
 \sup_{B_{1/4}(p)}(f+|\nabla\operatorname{Rm}|)
 \leq C_M D^{1/2}e^{3d_g(x,p)/2}.}
 \tag{4}
\]

Consequently, for every fixed \(0<\theta<1/3\), as \(D\downarrow0\)
through positive values,

\[
 \sup_{B_{\theta\log(1/D)}(x)}
       (f+|\nabla\operatorname{Rm}|)
 \leq C_M D^{(1-3\theta)/2}\longrightarrow0.
 \tag{5}
\]

For each fixed \(\epsilon>0\), every point with
\(f(p)+|\nabla\operatorname{Rm}|(p)\geq\epsilon\) satisfies

\[
 v(p)\leq C_\epsilon D,\qquad
 d_g(x,p)\geq\frac13\log(1/D)-C_{M,\epsilon}.
 \tag{6}
\]

Thus any fixed departure from product curvature or local symmetry
must move into quantitatively small-volume regions at least
logarithmically far from the thick point. This strengthens the
previous qualitative pointed-limit statement. It does not rule out
a long, bounded-curvature, deeply collapsed region.

## 2. Inputs already established in Round 15

Two-orientation spinor calibration gives

\[
 \int_M f^2\,d\mu\leq\frac{68}{3}D.
 \tag{7}
\]

For \(D\leq D_0\), exact Einstein epsilon-regularity and
Bishop--Gromov give universal bounds

\[
 |\operatorname{Rm}|\leq C_0,\qquad
 |\nabla\operatorname{Rm}|\leq C_1.
 \tag{8}
\]

In particular \(f\) is uniformly Lipschitz: the model orbit is
parallel-transport invariant, so its distance has Lipschitz constant
at most a fixed multiple of \(C_1\). The derivation of (8), including
the absolute-energy Cheeger--Tian input and derivative estimates, is
in Round 15, Theorem 3. No local lower volume bound was used there.

The new issue is that (7) alone does not control a point in a very
small ball. We first use (8) and relative volume comparison to enter
a fixed algebraic neighborhood of the product orbit, and then use
the exact Einstein equation to obtain the square-root estimate (3).

## 3. A polynomial measuring the product Weyl orbit

For the algebraic calculations retain \(\kappa>0\), put
\(s=-4\kappa\), and let

\[
 \mathscr K_\kappa
 =SO(3)\cdot\operatorname{diag}(-2\kappa/3,\kappa/3,\kappa/3).
\]

For a symmetric trace-free \(3\times3\) operator \(W\), define

\[
 N(W)=W^2+\frac\kappa3W-\frac{2\kappa^2}{9}I.
 \tag{9}
\]

Its zero set on the trace-free subspace is precisely
\(\mathscr K_\kappa\). Indeed, the roots are
\(-2\kappa/3\) and \(\kappa/3\), and trace zero forces their
multiplicities to be one and two.

In a sufficiently small fixed tubular neighborhood of this orbit,

\[
 c_\kappa\operatorname{dist}(W,\mathscr K_\kappa)
 \leq |N(W)|
 \leq C_\kappa\operatorname{dist}(W,\mathscr K_\kappa).
 \tag{10}
\]

To check this directly, diagonalize \(W\), ordering its simple
negative eigenvalue first. Its three eigenvalues remain close to
the corresponding model roots. Each component of \(N\) is the
product of the eigenvalue's displacement from its nearby root and
a factor bounded above and below by positive multiples of
\(\kappa\). The nearest orbit element has the same eigenspaces
and the model roots.

For an Einstein metric, both Weyl blocks are divergence-free. Their
equation, with \(\Delta=\operatorname{tr}\nabla^2\), is

\[
 \delta W^\pm=0,\qquad
 \Delta W^\pm=Q(W^\pm),\qquad
 Q(W)=-2\kappa W-6W^2+2|W|^2I.
 \tag{11}
\]

The Laplacian has nonpositive eigenvalues on a closed manifold.
The product orbit consists of zeros of \(Q\).
The operator identity is also displayed directly in
Biquard--Gauduchon--LeBrun,
[*Gravitational Instantons, Weyl Curvature, and Conformally Kähler
Geometry*, equation (2)](https://arxiv.org/pdf/2310.14387).
The full tensor formula and its covariant-derivative version are
given in Catino--Mastrolia,
[*Bochner type formulas for the Weyl tensor on four dimensional
Einstein manifolds*, Lemma 4.1, Proposition 5.1, Theorem 1.1](
https://cvgmt.sns.it/media/doc/paper/3250/Einstein4D_final.pdf).
These are classical inputs, used with the norm convention above.

## 4. Full first-jet coercivity from the divergence equation

The derivative of \(N\) annihilates tangent directions to the model
orbit. It is therefore essential to use all components of
\(\delta W=0\), not just ellipticity for jets of the form
\(\xi\otimes H\).

At

\[
 W_0=\operatorname{diag}(-2\kappa/3,\kappa/3,\kappa/3),
\]

the tangent space consists of symmetric matrices whose only
possibly nonzero entries are \(12,21,13,31\).
On its orthogonal complement in the trace-free symmetric matrices,

\[
 |DN_{W_0}H|=\kappa|H|,\qquad
 DN_W(H)=WH+HW+\frac\kappa3H.
 \tag{12}
\]

Take an arbitrary four-direction tangent jet \(T=(T_i)_{i=1}^4\).
Write its eight free components as
\((x_1,y_1,\ldots,x_4,y_4)\).
Using an orthonormal self-dual basis
\(\omega_a/\sqrt2\), with

\[
 \omega_1=e^{12}+e^{34},\quad
 \omega_2=e^{13}+e^{42},\quad
 \omega_3=e^{14}+e^{23},
\]

its four-index divergence is

\[
 (\mathcal DT)_{jkl}
 =\frac12\sum_{i,a,b}(T_i)_{ab}(\omega_a)_{ij}(\omega_b)_{kl}.
 \tag{13}
\]

The \(64\times8\) matrix in (13) has Gram matrix

\[
 G=\operatorname{diag}(B,B),\qquad
 B=
 \begin{pmatrix}
  2&0&0&1\\
  0&2&-1&0\\
  0&-1&2&0\\
  1&0&0&2
 \end{pmatrix}.
\]

Thus its Gram eigenvalues are
\(1,1,1,1,3,3,3,3\), whereas
\(|T|^2=2\sum_i(x_i^2+y_i^2)\). Thus

\[
 \boxed{|\mathcal DT|^2\geq\tfrac12|T|^2
       \quad\text{for every tangent jet}.}
 \tag{14}
\]

This exact finite-dimensional identity is independently evaluated
by [the accompanying check](round16_rigidity_check.py).
An orientation-reversing orthogonal map gives the identical result
on \(\Lambda^-\).

For any full jet \(T=T_{\rm tan}+T_{\rm nor}\) with
\(\mathcal DT=0\), the elementary contraction estimate is
\(|\mathcal DT_{\rm nor}|\leq4|T_{\rm nor}|\).
Here four-index conversion has norm factor two, and contraction
of a four-direction jet has norm at most two. Therefore

\[
 |T_{\rm tan}|\leq4\sqrt2|T_{\rm nor}|,\qquad
 |T|\leq\frac{\sqrt{33}}{\kappa}|DN_{W_0}T|.
 \tag{15}
\]

If \(|W-W_0|\leq\kappa/(4\sqrt{33})\), then

\[
 |(DN_W-DN_{W_0})T|\leq2|W-W_0||T|
\]

can be absorbed in (15). Pointwise application to
\(T=\nabla W\), using \(\delta W=0\), proves

\[
 \boxed{|\nabla W|^2
      \leq\frac{132}{\kappa^2}|\nabla N(W)|^2.}
 \tag{16}
\]

The comparison is pointwise. No differentiable choice of a nearest
orbit element is required in this argument.

## 5. A scalar subsolution and a local derivative-energy estimate

On the same tube, the chain rule for the actual matrix polynomial
gives

\[
 \Delta N(W)=DN_W[Q(W)]+2\sum_i(\nabla_iW)^2.
 \tag{17}
\]

Since \(Q\) vanishes on the orbit, (10) and boundedness of \(DN\)
give
\(|DN_WQ(W)|\leq C_\kappa|N(W)|\).
Writing \(u_W=|N(W)|^2\), it follows that

\[
 \Delta u_W
 \geq2|\nabla N(W)|^2-C_\kappa u_W
                  -4|N(W)|\,|\nabla W|^2.
 \tag{18}
\]

Shrink the fixed tube once more. Equation (16) absorbs the last
term, yielding

\[
 \Delta u_W\geq|\nabla N(W)|^2-C_\kappa u_W.
 \tag{19}
\]

For \(u=|N(W^+)|^2+|N(W^-)|^2\), with \(\kappa=3\), this gives

\[
 \Delta u\geq
  |\nabla N(W^+)|^2+|\nabla N(W^-)|^2-Cu.
 \tag{20}
\]

If the tube condition holds on \(B_1(p)\), choose a Lipschitz
cutoff supported there, equal to one on \(B_{3/4}(p)\), with
uniformly bounded gradient. Multiply (20) by its square and
integrate by parts. The inequality

\[
 |\nabla u|\leq2\sqrt u\,
       (|\nabla N(W^+)|^2+|\nabla N(W^-)|^2)^{1/2}
\]

and Young's inequality absorb half the derivative term. By (16),

\[
 \int_{B_{3/4}(p)}|\nabla\operatorname{Rm}|^2
 \leq C\int_{B_1(p)}u\leq CD.
 \tag{21}
\]

The last step uses (7), (10), and the exact Einstein curvature
decomposition. This argument requires only first derivatives of
the distance cutoff, not an injectivity radius or a smooth radial
coordinate system.

The Einstein derivative Bochner identity and the global curvature
bound (8) also give, for \(z=|\nabla\operatorname{Rm}|^2\),

\[
 \Delta z\geq-Cz.
 \tag{22}
\]

For example, the cited Catino--Mastrolia Theorem 1.1 has
\(\tfrac12\Delta|\nabla W|^2=
|\nabla^2W|^2+\tfrac{13}{12}s|\nabla W|^2
-10W_{ijkl}W_{ijpq,t}W_{klpq,t}\).
Bound the cubic term by \(C|W||\nabla W|^2\);
\(\nabla\operatorname{Rm}=\nabla W\) because the metric is Einstein.

## 6. Entering the tube and proving the relative estimate

Fix the tube radius \(a_0>0\) required above, and let \(L\) be a
universal Lipschitz constant for \(f\) from (8). Suppose some
\(y\in B_1(p)\) has \(f(y)\geq a_0\). Set

\[
 r_0=\min\{1/2,a_0/[2(L+1)]\}.
\]

Then \(f\geq a_0/2\) on \(B_{r_0}(y)\).
Since \(B_1(p)\subset B_2(y)\), relative Bishop--Gromov gives

\[
 \operatorname{Vol}B_{r_0}(y)
 \geq\frac{\mathcal V_{-1}(r_0)}{\mathcal V_{-1}(2)}
                  \operatorname{Vol}B_2(y)
 \geq c(a_0)v(p),
 \tag{23}
\]

where \(\mathcal V_{-1}\) is the ball volume in hyperbolic
four-space of sectional curvature \(-1\).
Combining with (7) contradicts \(D/v(p)\leq\varepsilon_0\)
when \(\varepsilon_0\) is sufficiently small.
Consequently the entire ball \(B_1(p)\) lies in the required tube.
This preliminary step uses only the already-established derivative
bound, and so does not assume the desired refined estimate.

The needed analytic input is the **normalized** local mean-value
inequality: under a fixed Ricci lower bound, a nonnegative function
satisfying \(\Delta h\geq-Ch\) on a fixed-radius ball obeys

\[
 \sup_{B_{r/2}(p)}h
 \leq\frac{C'}{\operatorname{Vol}B_r(p)}
                          \int_{B_r(p)}h.
 \tag{24}
\]

No lower volume assumption occurs. This follows from the local
subharmonic mean-value inequality of Li--Schoen,
[*\(L^p\) and mean value properties of subharmonic functions on
Riemannian manifolds*, Theorem 2.1 and equation (2.3)](
https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6362-11511_2006_Article_BF02392380.pdf).
For the zeroth-order term, apply their subharmonic estimate on
\(M\times\mathbb R\) to \(h(q)e^{\sqrt C\,t}\). Its Laplacian is
nonnegative. Product-ball volumes are comparable to
\(r\,\operatorname{Vol}B_r(p)\), by inclusions and
Bishop--Gromov; integration over the real coordinate costs only a
fixed factor. Use smaller concentric balls if needed to supply the
buffer in the local form of their theorem.

Apply (24) first to \(u\), using (20), and then to \(z\) on a
smaller ball, using (21)--(22). Bishop--Gromov compares every
fixed-fraction concentric ball volume with \(v(p)\). This proves

\[
 \sup_{B_{1/4}(p)}(u+z)\leq C D/v(p).
\]

Equation (10), the two Weyl blocks, and zero trace-free Ricci
complete the proof of (3).

## 7. Distance, volume, and the remaining thin region

For \(d=d_g(x,p)\), the inclusion \(B_1(x)\subset B_{d+1}(p)\)
and Bishop--Gromov give

\[
 v(p)\geq
 v_0(M)\frac{\mathcal V_{-1}(1)}{\mathcal V_{-1}(d+1)}
 \geq c_M e^{-3d}.
 \tag{25}
\]

Substitution in (3) proves (4)--(5). If the defect at \(p\) is
at least \(\epsilon\), either \(D/v(p)>\varepsilon_0\), or (3)
implies \(v(p)\leq C\epsilon^{-2}D\). This proves the first
part of (6); (25) proves the second.

The conclusion includes regions that are collapsing, but not so
fast that their unit-ball volumes become comparable to \(D\).
It identifies the unresolved scale: \(v(p)=O(D)\).
The calculation supplies no uniform propagation through all of
that deepest thin part, and no identification of its ends with the
original shear collars.

Nor can one obtain a global positive-potential argument merely by
dropping terms from (17). At the model, \(DQ\) has eigenvalue
\(2\kappa\) on the amplitude normal direction,
\(-6\kappa\) on each of the other two normal directions, and zero
on the two orbit-tangent directions. The exact sign check is in
the accompanying program. These mixed signs do not prove that
global rigidity is impossible; they show why the local propagation
argument does not already establish it.

## 8. Relation to the original problem and reproducibility

The result concerns every exact Einstein output approaching the
sharp scalar-volume bound on the stated smooth types, not just an
Einstein metric preserving a chosen shear or circle symmetry.
Its new content is a quantitative bridge from global monopole
calibration to product geometry over a growing region, with an
explicit remaining volume scale.

It does not turn a near-Einstein input into an exact output, rule
out all Einstein outputs, or settle a Yau 26 sign branch. A further
global argument would have to control what can occur in the
\(v(p)=O(D)\) region or show that the topology forces a defect
before that depth.

Run the exact finite-dimensional checks with:

    /data/qiushi/qiushi_engine_v09/.venv/bin/python round16_rigidity_check.py

They verify the product polynomial, its normal derivative, the
full eight-variable tangent-jet divergence and its singular values,
and the mixed signs of the Einstein polynomial's derivative.
The geometric proof above separately supplies the tube entry,
PDE absorption, local integration, and normalized mean-value steps.
