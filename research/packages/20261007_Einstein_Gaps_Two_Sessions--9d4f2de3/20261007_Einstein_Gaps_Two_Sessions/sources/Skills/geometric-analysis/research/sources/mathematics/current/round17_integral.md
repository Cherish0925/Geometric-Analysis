# Scalar-energy stability on the original metric

## 1. Question and result

The product-boundary estimate in [Round 15](round15_rigidity.md) assumed
constant negative scalar curvature. That hypothesis supplied a pointwise
bound for the monopole spinor; it was not a harmless normalization of an
arbitrary metric. Here it is removed. A smooth radial truncation gives a
bounded global two-form while retaining its first-order energy and its
relation to an actual Chern class. Hodge theory then controls the Weyl
profile without a conformal change, a scalar-curvature upper bound, a
Sobolev constant, or a geometric compactness assumption.

This concerns a **realizable** calibration: negative Kähler--Einstein
geometry in one orientation, and the product of two hyperbolic surfaces
in two orientations. It is different from the forbidden calibration at
topological ratio \(2/3\) in [Round 4](round4_rigidity.md) and
[Round 5](round5_rigidity.md).

Let \(g\) be any smooth metric on a closed connected oriented
four-manifold \(M\).
Assume a specified spin-c structure with first Chern class \(a\) has an
actual unperturbed Seiberg--Witten solution for this metric, and write

\[
 A=a^2>0,\qquad T=2\chi(M)+3\tau(M),\qquad V=\operatorname{Vol}(M,g).
 \tag{1}
\]

An actual monopole class supplies this hypothesis for every metric.
A formal cohomology class or a convex combination of classes does not
supply the spinor used below. For any constant \(\kappa>0\), define

\[
 B=\int_M s^2\,d\mu-32\pi^2 A,\qquad
 P=\int_M|\operatorname{Ric}^{\circ}|^2\,d\mu,\qquad
 L=\int_M(s+4\kappa)^2\,d\mu.
 \tag{2}
\]

Two-form norms are exterior-algebra norms. Weyl and curvature operators
use Hilbert--Schmidt norms on two-forms; Ricci uses the ordinary
two-tensor norm. Let \(\mathscr K_\kappa\) be the Weyl-operator orbit with
eigenvalues \((-2\kappa/3,\kappa/3,\kappa/3)\).

**Theorem 1 (arbitrary-scalar calibration).** One has \(B\ge0\).
There is a globally smooth self-dual two-form \(\varphi\) such that

\[
 \begin{split}
 |\varphi|&\le8\kappa,\\
 \int|\nabla\varphi|^2&\le4\kappa B,\\
 \int\bigl(|\varphi|-4\kappa\bigr)^2&\le2(B+L).
 \end{split}
 \tag{3}
\]

If \(\mathcal F=iF_{\mathfrak A}\) is the real determinant curvature
of the monopole solution, with the quadratic-map sign chosen so that
\(\mathcal F^+=\psi/(2\sqrt2)\), then

\[
 d\mathcal F=0,\qquad [\mathcal F/(2\pi)]=a,\qquad
 \left\|\mathcal F-\frac{\varphi}{2\sqrt2}\right\|_2^2
 \le\frac38B+\frac14L .
 \tag{4}
\]

Moreover,

\[
 \boxed{\;
 \int\operatorname{dist}_{\rm HS}(W^+,\mathscr K_\kappa)^2
 \le\frac12P+\frac{39}{8}B+\frac{14}{3}L
                  +4\pi^2(T-A)_+ .
 \;}
 \tag{5}
\]

The topological remainder is absent whenever \(a^2\ge2\chi+3\tau\).
In particular, \(a^2=T>0\) is sufficient, but is not needed for the
exact identity in Section 4.

All constants are absolute. These are integral estimates on the
original metric; they do not assert pointwise curvature bounds, a
nowhere-zero \(\varphi\), or that \(\varphi\) is closed.

## 2. The scalar defect controls the actual connection

Use the conventions in [Round 3](round3_monopole_input.md). For the
solution \((\Phi,\mathfrak A)\), set

\[
 \rho=|\Phi|^2,\qquad
 \psi=-2\sqrt2\,\sigma(\Phi),\qquad
 |\psi|=\rho,\qquad
 K=\int|\nabla_{\mathfrak A}\Phi|^2.
\tag{6}
\]

Thus \(-iF_{\mathfrak A}^+=\sigma(\Phi)\), as in Round 3, and
\(\mathcal F^+=\psi/(2\sqrt2)\). The sign of \(\psi\) is immaterial
to its norm, derivative estimates, and quadratic Weyl surrogate.

The integrated spinor Weitzenböck formula and the determinant
Chern--Weil formula are

\[
 4K+\int s\rho+\int\rho^2=0,\qquad
 \int\rho^2=32\pi^2 A+8\|\mathcal F^-\|_2^2.
 \tag{7}
\]

Expanding \((s+\rho)^2\) proves the exact identity

\[
 \boxed{\;
 B=\|s+\rho\|_2^2+8K+8\|\mathcal F^-\|_2^2.
 \;}
 \tag{8}
\]

Consequently \(B\ge0\), \(K\le B/8\), and
\(\|\mathcal F^-\|_2^2\le B/8\). In addition,

\[
 \|\rho-4\kappa\|_2^2
 =\|(s+\rho)-(s+4\kappa)\|_2^2\le2(B+L).
 \tag{9}
\]

The use of the *full* determinant connection matters: (8) controls its
anti-self-dual curvature, not just the harmonic anti-self-dual
projection of \(a\). No derivative of scalar curvature is involved.

The Seiberg--Witten equations, the scalar-energy lower bound, and the
negative Kähler--Einstein equality case are classical inputs. See
LeBrun, [*Ricci Curvature, Minimal Volumes, and Seiberg--Witten
Theory*, Section 2](https://arxiv.org/pdf/math/0003068), and
[*Four-Manifolds, Curvature Bounds, and Convex Geometry*,
Proposition 3.2](https://arxiv.org/pdf/math/0611450).
Identity (8) keeps all the nonnegative losses needed for stability.

## 3. A bounded smooth calibration with controlled derivative

A scalar \(L^2\) estimate does not bound \(\rho\) pointwise. Directly
using the quartic Weyl surrogate of \(\psi\) would therefore require
an uncontrolled \(\int\rho^4\). The following truncation avoids it.

Choose once and for all a smooth function
\(\chi:\mathbb R\to[0,1]\), equal to \(1\) on \((-\infty,0]\) and
to \(0\) on \([1,\infty)\). Define, for \(r\ge0\),

\[
 \beta_\kappa(r)=
 \int_0^r\chi\!\left(\frac{t-4\kappa}{4\kappa}\right)\,dt.
 \tag{10}
\]

Then

\[
 \begin{gathered}
 \beta_\kappa(r)=r\quad(0\le r\le4\kappa),\qquad
 0\le\beta_\kappa'\le1,\qquad
 \beta_\kappa'=0\quad(r\ge8\kappa),\\
 0\le\beta_\kappa(r)\le\min(r,8\kappa),\qquad
 \beta_\kappa(r)\ge4\kappa\quad(r\ge4\kappa).
 \end{gathered}
 \tag{11}
\]

Put

\[
 \varphi=\frac{\beta_\kappa(\rho)}{\rho}\,\psi ,
 \tag{12}
\]

using multiplier \(1\) near \(\rho=0\). This is globally smooth:
\(\rho=|\Phi|^2\) is smooth, and the multiplier is identically \(1\)
on a neighborhood of its only potentially singular denominator.
Write \(\beta=\beta_\kappa(\rho)=|\varphi|\).

The inequalities
\[
 |\beta-4\kappa|\le|\rho-4\kappa|,\qquad
 |\rho-\beta|\le|\rho-4\kappa|
 \tag{13}
\]
follow separately on \(r\le4\kappa\) and \(r\ge4\kappa\).
They prove the amplitude part of (3) and give
\(\|\psi-\varphi\|_2^2\le2(B+L)\).
Because the two terms in
\[
 \mathcal F-\frac{\varphi}{2\sqrt2}
 =\mathcal F^-+\frac{\psi-\varphi}{2\sqrt2}
\]
have opposite duality, their squared norms add. Equations (8)--(9)
now prove (4).

For the derivative, the quadratic spinor map satisfies

\[
 |\nabla\psi|^2\le4\rho|\nabla_{\mathfrak A}\Phi|^2.
 \tag{14}
\]

This is the differential estimate for the Hopf map with the
determinant gauge direction retained. On the set \(\rho>0\), write
\(\psi=\rho n\), \(|n|=1\). Orthogonality yields

\[
 \begin{split}
 |\nabla\psi|^2&=|d\rho|^2+\rho^2|\nabla n|^2,\\
 |\nabla\varphi|^2
 &=\beta_\kappa'(\rho)^2|d\rho|^2
                       +\beta_\kappa(\rho)^2|\nabla n|^2.
 \end{split}
 \tag{15}
\]

Both coefficients after multiplication by \(\rho\) are bounded:

\[
 \rho\,\beta_\kappa'(\rho)^2\le8\kappa,\qquad
 \frac{\beta_\kappa(\rho)^2}{\rho}
                  \le\beta_\kappa(\rho)\le8\kappa.
 \tag{16}
\]

Combining (14)--(16) gives
\[
 |\nabla\varphi|^2
 \le32\kappa|\nabla_{\mathfrak A}\Phi|^2 .
 \tag{17}
\]
At spinor zeros this holds by smooth continuation. Integrating and
using \(K\le B/8\) proves the derivative bound in (3).
There is no derivative bound on \(s\), no maximum principle with a
uniform scalar minimum, and no rescaling-weight derivative hidden
in this argument.

## 4. An exact Hodge--Chern--Weil identity

Define the smooth trace-free symmetric endomorphism of \(\Lambda^+\)

\[
 \mathsf A_\varphi=
 \frac{\beta^2}{48\kappa}I-\frac{\varphi\otimes\varphi}{16\kappa},
 \qquad \mathsf R=W^+-\mathsf A_\varphi.
 \tag{18}
\]

Its squared norm is \(\beta^4/(384\kappa^2)\). The self-dual Hodge
formula and Chern--Weil identity read

\[
 2\|d\varphi\|_2^2
 =\|\nabla\varphi\|_2^2+\frac13\int s\beta^2
                       -2\int\langle W^+\varphi,\varphi\rangle ,
 \tag{19}
\]
\[
 \|W^+\|_2^2=2\pi^2T-\frac1{48}\int s^2+\frac14P.
 \tag{20}
\]

Expanding (18), using trace-freeness, and substituting (19)--(20)
gives

\[
 \boxed{
 \begin{split}
 \|\mathsf R\|_2^2+\frac1{8\kappa}\|d\varphi\|_2^2
 ={}&2\pi^2(T-A)+\frac14P-\frac1{16}B
                    +\frac1{16\kappa}\|\nabla\varphi\|_2^2\\
 &+\frac1{384\kappa^2}
                       \int(\beta^2+4\kappa s)^2 .
 \end{split}}
 \tag{21}
\]

This identity holds before imposing \(A\ge T\), and does not discard
the exterior-derivative term. In particular, the topology cannot be
silently removed when a class of the wrong square is substituted.

To estimate its last term, note that \(\beta\le8\kappa\) and (3) give

\[
 \begin{split}
 \int(\beta^2-16\kappa^2)^2
 &\le144\kappa^2\int(\beta-4\kappa)^2\\
 &\le288\kappa^2(B+L).
 \end{split}
 \tag{22}
\]

Since
\(\beta^2+4\kappa s=(\beta^2-16\kappa^2)+4\kappa(s+4\kappa)\),

\[
 \int(\beta^2+4\kappa s)^2
 \le576\kappa^2B+608\kappa^2L.
 \tag{23}
\]

Thus (21) implies the useful intermediate estimate

\[
 \boxed{
 \|\mathsf R\|_2^2+\frac1{8\kappa}\|d\varphi\|_2^2
 \le2\pi^2(T-A)+\frac14P+\frac{27}{16}B+\frac{19}{12}L.}
 \tag{24}
\]

Where \(\varphi\ne0\), choose the element of
\(\mathscr K_\kappa\) whose simple eigenspace is
\(\mathbb R\varphi\). Its squared distance from
\(\mathsf A_\varphi\) is

\[
 \frac{(\beta^2-16\kappa^2)^2}{384\kappa^2}.
 \tag{25}
\]

At \(\varphi=0\) the same distance holds for every choice of line.
The pointwise triangle inequality squared, (22), and (24) give

\[
 \int\operatorname{dist}(W^+,\mathscr K_\kappa)^2
 \le4\pi^2(T-A)+\frac12P+\frac{39}{8}B+\frac{14}{3}L.
 \tag{26}
\]

Replacing the signed topological term by its positive part proves
(5). Keeping the signed version (26) is sometimes sharper.
This completes the proof of Theorem 1.

## 5. Two orientations: the full product curvature profile

**Theorem 2.** Suppose \(\tau(M)=0\), \(A=2\chi(M)>0\), and the
two orientations each have a specified actual monopole class of
square \(A\). For every smooth metric and every \(\kappa>0\), let
\(B,P,L\) be as in (2). If \(\mathscr P_\kappa\) is the full
curvature-operator orbit of
\(\mathbb H^2_{-\kappa}\times\mathbb H^2_{-\kappa}\), then

\[
 \boxed{
 \int\operatorname{dist}_{\rm HS}
                (\mathcal R_g,\mathscr P_\kappa)^2
 \le\frac32P+\frac{39}{4}B+\frac{75}{8}L.}
 \tag{27}
\]

There are two globally smooth forms
\(\varphi_\pm\in\Gamma(\Lambda^\pm)\), each satisfying (3)--(4)
with its corresponding actual determinant connection.

**Proof.** Apply Theorem 1 in both orientations. The curvature
operator decomposes as

\[
 \mathcal R=
 \begin{pmatrix}
 W^++sI/12 & \operatorname{Ric}^{\circ}_{\Lambda}\\
 (\operatorname{Ric}^{\circ}_{\Lambda})^* & W^-+sI/12
 \end{pmatrix}.
 \tag{28}
\]

The two off-diagonal blocks have total squared norm
\(|\operatorname{Ric}^{\circ}|^2/2\). The scalar displacement from
\(-4\kappa\) has squared norm \((s+4\kappa)^2/24\); this is
orthogonal to the two trace-free Weyl displacements. The action
\(\mathrm{SO}(4)\to\mathrm{SO}(3)\times\mathrm{SO}(3)\) on the
two Weyl blocks is onto. Consequently their two orbit minimizations
can be realized simultaneously by a product curvature operator.
Adding the two instances of (5), \(P/2\), and \(L/24\) proves (27).
\(\square\)

This hypothesis is not a shear-specific geometric ansatz. Products
of hyperbolic surfaces supply exact equality tests. The closed shear
examples are additional applications once their two actual classes
have been established by [Round 12](round12_global.md); a new
manifold must supply its own class-existence argument.

## 6. Mean-scalar normalization and the Yau26 input

Suppose only that the mean scalar curvature is negative, and choose

\[
 \kappa=-\frac1{4V}\int s,\qquad
 D=\kappa^2V-2\pi^2A .
 \tag{29}
\]

Then \(L=\int(s-\fint s)^2\) is the scalar variance and

\[
 \boxed{B=16D+L\ge0.}
 \tag{30}
\]

Unlike in the constant-scalar theorem, \(D\) need not be nonnegative:
the exact restriction is \(D\ge-L/16\). Substituting (30) in (27)
gives

\[
 \int\operatorname{dist}(\mathcal R,\mathscr P_\kappa)^2
 \le\frac32P+156D+\frac{153}{8}L
 \le\frac32P+156D_++\frac{153}{8}L.
 \tag{31}
\]

Thus any sequence in this actual-monopole category with

\[
 \frac{P+L+D_+}{\kappa^2V}\longrightarrow0
 \tag{32}
\]

has a relative \(L^2\) product-curvature profile on its **original**
metrics. At the same time,
\(\int|\nabla\varphi_\pm|^2/(\kappa^3V)\to0\), their amplitudes
approach \(4\kappa\) in normalized \(L^2\), and (4) retains their
actual topological representatives. No conformal scalar-curvature
repair or pullback from another metric occurs.

The pointwise near-Einstein input directly controls two errors:
if
\(\delta_\kappa=\|g^{-1}\operatorname{Ric}+\kappa I\|_{\infty,\rm op}\),
then

\[
 P+\frac14L
 =\int|\operatorname{Ric}+\kappa g|^2
 \le4\delta_\kappa^2 V
 \tag{33}
\]

whenever \(L\) is measured against this same \(\kappa\). A
near-Einstein sequence whose normalized volume also approaches the
sharp scalar-energy value therefore satisfies the hypotheses of
(32). If one first fixes the input normalization rather than the
mean normalization, the difference between the two \(\kappa\)'s is
at most \(\delta_\kappa\).

This is a necessary geometric structure theorem near a realizable
boundary, not an Einstein-existence theorem. Negative product
Einstein metrics meet all estimates with zero right side. In
particular, this calibration cannot itself furnish the contradiction
used at the forbidden \(2/3\) boundary.

## 7. What topological and spectral information survives

The cap does not merely produce a small vector in an unrelated
bundle. It produces a bounded almost-parallel self-dual form close
to the curvature of an actual line bundle. Two elementary
consequences make that content explicit.

First,
\[
 \operatorname{Vol}\{|\varphi|<2\kappa\}
 \le\frac{B+L}{2\kappa^2}.
 \tag{34}
\]
This gives an amplitude-exceptional volume estimate, not a
pointwise nonvanishing theorem.

Second, let \(\mu_+(g)\) be the bottom eigenvalue of the connection
Laplacian \(\nabla^*\nabla\) on self-dual two-forms. When
\(4\kappa\sqrt V>\sqrt{2(B+L)}\), its Rayleigh principle and (3)
give

\[
 \mu_+(g)\le
 \frac{4\kappa B}
 {\bigl(4\kappa\sqrt V-\sqrt{2(B+L)}\bigr)^2}.
 \tag{35}
\]

For example, if \(B+L\le2\kappa^2V\), then
\(\mu_+(g)\le B/(\kappa V)\).
The opposite-orientation conclusion is analogous. No uniform lower
bound for \(\mu_\pm\) has been assumed or deduced from topology.

At exact scalar saturation \(B=0\), (8) forces a parallel,
nonzero spinor, \(\mathcal F^-=0\), and \(s=-\rho<0\).
Its parallel two-form gives the classical negative
Kähler--Einstein equality case. In the two-orientation category,
both chiral parallel forms split the tangent bundle into parallel
two-planes, giving the local product model. This is an equality
check, not a new classification theorem.

## 8. Relation to the earlier integral method

The removed assumption is constant scalar curvature in the
realizable calibration estimate. Round 4 bounded a rescaled spinor
by changing the monopole equation and then proved second-order
control for a weak-Bianchi self-test. Here the unweighted solution
already has the exact loss decomposition (8); a smooth cap is
enough for the first-order Hodge identity. This avoids demanding
weighted solvability when it is not used.

The cap does **not** automatically solve a rescaled monopole
equation. Nor does (17) give the second-order bounds required for
Round 4's self-test. This argument therefore does not remove that
theorem's negative-square cost or extend its forbidden orbit to
arbitrary topologies. Its separate conclusion is (27) for arbitrary
scalar curvature at a realizable boundary.

Similarly, \(L^2\) profile control for arbitrary metrics cannot be
inserted into Cheeger--Tian's *exact Einstein* regularity theorem.
Curvature spikes remain possible. The exact-Einstein no-bubbling
and thin-part propagation arguments of Rounds 15--16 keep their
original hypotheses.

The useful next question is now precise: when (3)--(4) provide two
global bounded almost-parallel forms on an original near-Einstein
metric, what additional equation or topological mechanism prevents
their collapse into small connection-Laplacian eigenmodes without
an exact parallel limit? Proving a suitable spectral or topological
statement would strengthen the original Yau26 connection; (35)
alone does not supply it.

## 9. Verification and novelty scope

[The independent symbolic check](round17_integral_check.py) verifies
the scalar-loss expansion, the quadratic spinor differential with
its gauge direction retained, the radial derivative formula, both
model norms, the exact identity (21), the constants in (5) and
(27), and the signed mean-scalar identity (30). Run:

    /data/qiushi/qiushi_engine_v09/.venv/bin/python round17_integral_check.py

These checks test finite algebra. The actual monopole input,
smoothness at spinor zeros, global Hodge identity, derivative
estimate, and limiting scope are supplied by the proof above.

The classical scalar-energy estimate and its equality theorem are
not new. The project-level advance is the quantitative smooth-cap
argument and its arbitrary-scalar, two-orientation product estimate
on the original metric. This note makes no claim of a completed
literature-priority audit, nor of a new Yau26 sign-branch solution.
