# Rank-one curvature equations: a mixing identity and a sharp seed obstruction

21 September 2026.

The rank-one endpoint left by round 10 is not automatically reducible.
Its complementary Dirac equation instead constrains the second
fundamental form of the image line. Combining that constraint with the
complementary curvature equation gives an exact cohomological identity.
On the actual closed slow-twist manifolds it has two consequences:

* a rank-one image line with zero real first Chern class requires a
  definite amount of connection mixing; partial seeds with small mixing
  have normalized curvature residual at least `2-o(1)`;
* in the opposite canonical branch, an exact solution with the indicated
  source-line angle must decouple and have a flat complementary line.

These conclusions use the actual Dirac equation and the target support
of the source-factor quadratic projection. They do not depend on its
overall Clifford sign. The absolute identification of the published
uniformization system remains unresolved for the specific reason in
Section 6. No Einstein nonexistence theorem is asserted.

## 1. Bundles and the rank-one block equations

Let `(X,g)` be closed and oriented, let `W=S_L^+`, and let `E` be a
Hermitian rank-two bundle. Fix the source spin-c connection. Suppose
`phi:W->E` has rank one everywhere and satisfies

\[
                         D_A\phi=0.                         \tag{1}
\]

Set `R=im(phi)`, `K=R^perp`, and `M=(ker(phi))^perp` in the source.
All three are smooth complex line bundles. The restriction `phi:M->R`
is an isomorphism, so `c_1(M)=c_1(R)`. Relative to `E=R plus K`, write

\[
 A=\begin{pmatrix}a&-b^*\\ b&c\end{pmatrix},\qquad
 b\in\Omega^1\operatorname{Hom}(R,K).                   \tag{2}
\]

Here `a,c` are the induced unitary line connections and `b` is the
second fundamental form of `R`. The adjoint in (2) is pointwise; products
below include exterior multiplication of one-forms.

Let `tau` be the quadratic map that projects the source factor to its
trace-free part and retains the full target factor, as in the definition
on printed p. 21 of
[Leung, *Non-Abelian Seiberg--Witten equations on Einstein manifolds*](https://archive.ymsc.tsinghua.edu.cn/pacm_download/60/582-2000_Leung_NonAbelian_SW_eqt_on_Einstein_mfd_Crelle_Journal.pdf).
Its target image is supported on `R` at a rank-one field. Thus

\[
 \tau(\phi)=\begin{pmatrix}q(\phi)&0\\0&0\end{pmatrix}.\tag{3}
\]

The sign and scale of the scalar self-dual two-form `q(phi)` will not
be used. Curvature expansion gives the full rank-one reduction

\[
\begin{gathered}
 D_a\phi=0,\qquad \sum_j b_j\phi c_j=0,\\
 (F_a-b^*\wedge b)^+=q(\phi),\qquad
 (F_c-b\wedge b^*)^+=0,\qquad
 (d_{a,c}b)^+=0.                                      \tag{4}
\end{gathered}
\]

The matrices `c_j` are the right Clifford maps from negative to positive
source spinors. In the first equation `phi` is regarded as a section of
`Hom(W,R)`. The second equation is exactly the `K` component of (1):
all source-connection terms still have target in `R` and disappear under
projection to `K`. In particular, derivatives of the source line have
not been mistaken for the target second fundamental form.

For a pair satisfying only (1), define its curvature residual

\[
                    \mathcal R=F_A^+-\tau(\phi).
\]

Then the complementary curvature equation in (4) is replaced by

\[
 F_c^+=(b\wedge b^*)^++\mathcal R_{KK}.                \tag{5}
\]

## 2. The complementary Dirac equation fixes the sign of the mixing term

There is a canonical real self-dual form `omega_M`, of squared norm two,
associated to the source line `M`. Fix its sign by

\[
 \rho_W(\omega_M)|_M=-2i,\qquad
 \rho_W(\omega_M)|_{M^\perp}=2i.                       \tag{6}
\]

This uses the Clifford action on the original source `W`, not the
quadratic-map identification left open in Section 6. For the canonical
splitting `W=C plus K_J^{-1}`, the trivial source line corresponds to
the fundamental form of `J`, and the other source line to its negative.

**Lemma 1.** Equation (1) implies

\[
             (b\wedge b^*)^+=\frac{i}{2}|b|^2\omega_M.\tag{7}
\]

**Proof.** At a point choose an oriented orthonormal coframe with
`omega_M=e01+e23`, put `M=C(1,0)`, and choose right Clifford matrices

\[
 c_0=I,\qquad c_1=-i\sigma_3,\qquad
 c_2=i\sigma_1,\qquad c_3=i\sigma_2.                  \tag{8}
\]

They give `rho_W(e01+e23)=-2i sigma_3`. The complementary Dirac equation
is `b_0-i b_1=0`, `i b_2+b_3=0`. Therefore

\[
                b=z(e^0-i e^1)+w(e^2-i e^3).          \tag{9}
\]

In particular `|b|²=2(|z|²+|w|²)`. Its wedge with its complex conjugate
has self-dual part `i(|z|²+|w|²)(e01+e23)`. This proves (7).
Changes of source spin frame and target line frame preserve the formula.
Equivalently, `b` has type `(0,1)` for the almost-complex structure
specified by (6). QED.

The conclusion is not `b=0`. The annihilator in (9) has complex
dimension two. Automatic decoupling would incorrectly discard these
genuine differential degrees of freedom.

## 3. An exact cohomological mixing identity

Suppose `omega` is any fixed closed real self-dual two-form with
`|omega|²=2`. No closedness of `omega_M` is assumed. Let `k=c_1(K)` and
use `c_1(K)=[iF_c/(2pi)]`.

**Theorem 2.** Every everywhere rank-one Dirac field satisfies

\[
 \boxed{\quad
 2\pi k\cdot[\omega]
 =-\frac12\int_X |b|^2\langle\omega_M,\omega\rangle\,d\mu_g
       +\int_X i\mathcal R_{KK}\wedge\omega.
 \quad}                                                \tag{10}
\]

**Proof.** Multiply (5) by `i`, use (7), and wedge with the self-dual
form `omega`. Integrating its left side gives the stated Chern pairing
because `omega` is closed. This proves the identity. QED.

If the full curvature equation holds, the last term is zero. In the
special case `omega_M=omega`, (10) becomes

\[
                       \|b\|_2^2=-2\pi k\cdot[\omega].\tag{11}
\]

Thus a positive pairing is impossible, a zero pairing forces
decoupling, and a negative pairing fixes the entire mixing energy.
These alternatives are derived from the differential equations, not a
choice of sign for `q(phi)`.

If `tr mathcal R=0`, then the trace-free matrix estimate
`|mathcal R_KK|<=|mathcal R|/sqrt(2)` and `|omega|=sqrt(2)` give

\[
 \left|\int_X i\mathcal R_{KK}\wedge\omega\right|
           \le\sqrt{\operatorname{Vol}(g)}\,\|\mathcal R\|_2.
                                                               \tag{12}
\]

This coefficient is sharp: use a residual proportional to
`i omega diag(-1,1)` in the target splitting. Without the exact trace
equation, the right side of (12) has the additional factor `sqrt(2)`.

## 4. Consequences on the actual closed slow-twist metrics

Use the almost-Kähler metrics `G_L` on `E_D` or `E_full` and their
canonical bundle `W=C plus L_can`, with compatible form `omega_L`.
To avoid confusion, the subscript `L` on a family denotes its long
interpolation parameter; `L_can` is a line bundle. The explicit
harmonic-source construction in [round10_nonabelian.md](round10_nonabelian.md),
Sections 4--5, gives

\[
 c_1(L_{\rm can})=-[\omega_L]/(2\pi),\qquad
 |\omega_L|^2=2,\qquad d\omega_L=0.                   \tag{13}
\]

For the quantitative seed application we retain the balanced profiles
used there. The two assertions below only require (13), not its proof
by a small harmonic-source correction.

Write `||u||_{p,av}=(Vol^{-1} integral |u|^p)^{1/p}`.

**Corollary 3 (sharp obstruction for the trivial-image branch).**
Let `phi` be an everywhere rank-one Dirac field with `c_1(R)=0` in
real cohomology and exact determinant-curvature equation
`tr mathcal R=0`. Then

\[
 \boxed{\qquad
       2\le\|b\|_{2,av}^2+\|\mathcal R\|_{2,av}.
 \qquad}                                                \tag{14}
\]

Consequently an exact solution must satisfy `fint |b|²>=2`. A family
of such partial seeds with `||b||_{2,av}->0` has
`liminf ||mathcal R||_{2,av}>=2`. In particular, the uniformly
`O(L^{-1})` rank-one correction from round 10 cannot close this branch.

**Proof.** Here `k=c_1(L_can)`, so by (13)
`2pi k·[omega_L]=-integral omega_L²=-2Vol`. Rearranging (10), using
`<omega_M,omega_L><=2`, and applying (12) gives (14).
This argument does not require the source line to be pointwise close
to the trivial canonical line. QED.

If in addition `omega_M->omega_L` uniformly and the pair is an exact
solution, (10) shows `fint |b|²->2`. Thus the mixing is of fixed size,
not merely nonzero. In the product limit the positive-residual rank-one
branch of round 10 has residual norm exactly two, so (14) has the
correct sharp residual constant for the small-mixing test.

**Corollary 4 (flat complement in the opposite branch).** Suppose the
full curvature equation holds, `c_1(K)=0` in real cohomology, and

\[
                     \langle\omega_M,\omega_L\rangle<0
                     \quad\hbox{everywhere}.           \tag{15}
\]

Then `b=0`, `A=a plus c`, and `F_c=0`. Thus the complementary line is
flat and the remaining equations are the scalar, source-twisted system

\[
                        D_a\phi=0,\qquad F_a^+=q(\phi).
                                                               \tag{16}
\]

**Proof.** The left side of (10) vanishes, whereas the integrand in
its first term is nonnegative and strictly positive wherever `b!=0`.
Hence `b=0`. Equation (5) gives `F_c^+=0`. Since the real Chern class
of `K` is zero, the exact imaginary two-form `F_c` has zero square
integral. Anti-self-duality then forces `F_c=0`. QED.

Condition (15) holds for all source projectors sufficiently close to
the anticanonical source line. If the image line is also homotopic to
`L_can`, its complement has the required zero real Chern class.
Consequently this decoupling applies to a whole rank-one neighborhood
of the opposite partial seed, not just an exactly diagonal ansatz.
It still does not assert a solution of (16).

## 5. Why this does not provide an invariant-based Einstein bridge

The first branch has an explicit non-small mixing requirement and a
residual lower bound. The second branch reduces to a line equation,
but its determinant is not automatically the connection of an ordinary
unperturbed Seiberg--Witten problem. For example, when `R=L_can`,
the positive spinor bundle in (16) is `S^+_{L_can^{-1}} tensor L_can`;
its determinant connection is `2a-C`, where `C` is the prescribed
background connection on `L_can`. Its curvature is `2F_a-F_C`.
Dropping this source-curvature term changes the equation. An ordinary
monopole-class existence theorem therefore cannot be substituted for
existence of (16) without matching both its quadratic map and that
fixed term.

An arbitrary hypothetical Einstein metric on the same closed manifold
is not known to be compatible with `omega_L`. Nor do (1) and rank one
force `omega_M` to be closed. The theorem can be applied whenever a
closed self-dual constant-length form satisfying the stated pairing or
angle conditions is supplied, but this is additional geometry, not a
consequence of the smooth type. Rank-changing fields with zeros are
also outside the everywhere-rank-one hypotheses used to define `R,K`.

## 6. Exact status of the published convention calibration

The actual source pages were rechecked, including the published
pp. 18, 21--25, the wedge identities on p. 22, and the predecessor
[*Uniformization of four manifolds*, arXiv:dg-ga/9705001v3, pp. 8--10](https://arxiv.org/pdf/dg-ga/9705001).
The remaining difficulty is not resolved by selecting one of the
product signs. There is a test independent of every Clifford sign:

* the displayed block connection on p. 23 acts on
  `V=S_L^- plus E`, and for `E=S_L^+` one has `c_1(V)=2c_1(L)`;
* the displayed Einstein curvature on p. 24 is `-F_L^+ I_V`, with
  `F_L` explicitly called the curvature of the fixed connection on `L`.

Taking harmonic self-dual traces, the first item represents `2a^+`
and the second represents `-4a^+`. They cannot hold for that same
connection when `a^+!=0`. A consistent simultaneous reversal of the
Chern or curvature convention does not change this mismatch.
The predecessor repeats the same formulas and later introduces the
notation `D_{A,L}` without a bundle/connection replacement sufficient
to settle this comparison.

This test locates a missing normalization, twist, or displayed formula;
it does not by itself disprove the main uniformization theorem. In
particular, using its displayed block curvature to choose a favorable
rank-one branch would be circular. A corrected explicit connection and
quadratic-map identification is needed before identifying (16) with
the intended uniformization system. No such correction is asserted in
this note, and no moduli-emptiness claim is drawn from the mismatch.

The new results (7), (10), (14), and (15)--(16) avoid that unresolved
step entirely. The accompanying [checker](round11_rankone_check.py)
verifies the Clifford annihilators, the self-dual mixing term, the
block-curvature sign, the sharp residual constant, and the Chern
normalizations. It is not an existence theorem for (16).
