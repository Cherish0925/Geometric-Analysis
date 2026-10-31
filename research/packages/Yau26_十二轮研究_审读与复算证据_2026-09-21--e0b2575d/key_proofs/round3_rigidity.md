# An intrinsic monopole Hessian estimate closes the calibration gap

19 September 2026. This note removes the full-curvature hypothesis from
the monopole application of the round-two gap. It does not prove a gap
for arbitrary metrics without monopoles, and does not settle unrestricted
Yau26. All manifolds below are smooth, closed, oriented and four-dimensional.

The complete derivation of the imported monopole deficits, spectral
inequality, smooth Weyl approximation, and weighted Hodge identities is
now contained in [the self-contained monopole input](round3_monopole_input.md).
Live-path references below record provenance rather than proof dependencies.

The key new estimate is intrinsic. The curvature of the positive-spinor
connection has an average L2 bound supplied by the monopole equations and
Chern--Weil theory. A bundle-valued integration-by-parts estimate then
bounds its spinor Hessian. No Sobolev constant, coordinate radius,
injectivity radius, Weyl-minus bound, or curvature derivative is used.

## 1. A bundle Hessian estimate with no coordinate hypothesis

Let V be a Hermitian bundle with a compatible connection B over a closed
n-manifold. All inner products below mean their real parts. Write

\[
 F_{ij}=[\nabla_i,\nabla_j],\qquad
 H_{ij}=\nabla_i\nabla_j u,
 \qquad L=\operatorname{tr}\nabla^2u=-\nabla^*\nabla u.
\]

The covariant Hessian includes the Levi-Civita correction on its second
index. In this section use the component norm
\(|F|^2=\sum_{ij}|F_{ij}|_{\rm HS}^2\); this is twice the usual
endomorphism-valued two-form norm. Suppose \(\operatorname{Ric}\ge-rg\)
and \(K=\|u\|_\infty\).

**Lemma 1.** In dimension four,

\[
 \|\nabla u\|_4^2\le4K\|\nabla^2u\|_2,                 \tag{1}
\]
\[
 \|\nabla^2u\|_2^2
 \le2\|L\|_2^2+2r\|\nabla u\|_2^2+17K^2\|F\|_2^2.  \tag{2}
\]

These estimates involve the full covariant Hessian, rather than its
symmetrization. They hold for each individual bundle and metric.

For (1), integrate the divergence of the globally defined vector field
\(|\nabla u|^2\langle u,\nabla u\rangle^\sharp\). Since
\(|\operatorname{tr}H|\le\sqrt n|H|\),

\[
 \int|\nabla u|^4
 \le(2+\sqrt n)K\int|H||\nabla u|^2
 \le(2+\sqrt n)K\|H\|_2\|\nabla u\|_4^2.
\]

Division when the last factor is nonzero proves (1). No Sobolev
inequality appears.

For (2), first note the exact integrated identity

\[
\begin{split}
 \int|H|^2={}&\int|L|^2
 -\int\operatorname{Ric}_{ij}\langle\nabla_i u,\nabla_j u\rangle\\
 &+\sum_{ij}\int\langle F_{ij}\nabla_j u,\nabla_i u\rangle
 +\frac12\sum_{ij}\int|F_{ij}u|^2.                  \tag{3}
\end{split}
\]

Indeed, put \(T=\sum_{ij}\int\langle H_{ij},H_{ji}\rangle\).
The antisymmetric Hessian is \(H_{ij}-H_{ji}=F_{ij}u\), so
\(\int|H|^2-T=\frac12\int\sum_{ij}|F_{ij}u|^2\).
Integrate T by parts once and commute derivatives on the V-valued
one-form \(\nabla u\). Its cotangent curvature contracts to Ricci;
its bundle curvature gives the third term in (3). The traced derivative
term integrates to \(\int|L|^2\). This derivation never differentiates F.
The curvature convention is fixed by the scalar specialization
\(\int|\nabla^2v|^2=\int(\Delta v)^2-\int\operatorname{Ric}(dv,dv)\).

Cauchy--Schwarz and (1) bound the third term in absolute value by
\(4K\|F\|_2\|H\|_2\). The last is at most
\(K^2\|F\|_2^2/2\). Young's inequality in the form
\(4ab\le\frac12a^2+8b^2\) proves (2).
In particular the apparently critical term \(\int|F||\nabla u|^2\)
is linear in \(\|H\|_2\), not quadratic in it. Smallness of
\(\|F\|_2\) is unnecessary.

## 2. The precise monopole data and defect conventions

Use the definitions in `round2_rigidity.md`:

\[
 E=\operatorname{Ric}+g,\quad e=s+4,\quad
 \delta=\|g^{-1}\operatorname{Ric}+I\|_{\infty,\rm op}\le1/64,
 \quad u_W=|W^+|_{\rm HS},
\]
\[
 t=s+8\sqrt6u_W,\quad q=-s+\sqrt6u_W,\quad
 a_W=\sqrt{2/3}u_W,\quad w=\lambda_{\min}(W^+),
\]
\[
 G=(2s/3-2a_W)^2-(2s/3+2w)^2\ge0,
 \quad\mathcal D=|E|^2+e^2+t^2+G,
 \quad d_{\rm cal}=\int\mathcal D.
\]

Let \(a=c_1(L)\) be an actual monopole class with
\(p=(a^+)^2>0\), and set

\[
 \Delta=\int q^2-72\pi^2p\ge0,\qquad
 B_a=\frac{(-a^2)_+}{\operatorname{Vol}M},\qquad
 \varepsilon=\delta^2+
          \frac{\Delta+d_{\rm cal}}{\operatorname{Vol}M}.           \tag{4}
\]

Here “actual monopole class” means the rescaled Seiberg--Witten equations
are solvable for every smooth positive weight f, as follows by conformal
covariance from the ordinary monopole-class condition. This condition is
essential. Arbitrary forms with the norms in round two cannot replace the
solutions.

For a smooth positive approximation \(f\to\sqrt q\), solve

\[
 D_A\Phi=0,\qquad -iF_A^+=f\sigma(\Phi),\qquad
 \psi=2\sqrt2\sigma(\Phi),\quad \rho=|\Phi|^2=|\psi|.
                                                               \tag{5}
\]

Use approximations with \(f\ge\sqrt3\). Their errors in the following
integrated statements can be made less than any prescribed
\(\eta>0\) on each individual compact manifold. The maximum principle
gives \(\rho\le5/\sqrt3<3\). The quantified monopole identities and
round-two algebra provide

\[
 \|\rho-\sqrt2\|_2^2
 \le8\Delta/27+41d_{\rm cal}/432+\eta,\qquad
 \|d\rho\|_2^2,\ \|d\psi\|_2^2\le2\Delta/27+\eta,             \tag{6}
\]
\[
 A_\psi=\frac{\rho^2}{24}I-\frac18\psi\otimes\psi,\qquad
 R=W^+-A_\psi,\qquad
 \|R\|_2^2\le\Delta+649d_{\rm cal}+\eta.                       \tag{7}
\]

Every \(o(1)\) below refers to this smooth-weight approximation with the
metric and class fixed. Its normalized size can be made at most
\(\eta/V\), simultaneously with (6)--(7), by choosing the approximation
more accurately. No convergence of the corresponding solutions is assumed.

The original rescaled equations, quadratic-map normalization, and
quantified deficits are in the live manuscript
`research/20260916_rigidity.tex`, equations `quantSW` and
`eigenline-deficit`, read with their derivations. The rescaled-solvability
input is also [LeBrun, Lemma 3.7 and Proposition 3.8](https://arxiv.org/abs/math/0611450).
The spin-c Weitzenbock formula and determinant-connection convention are
consistent with [Okonek--Teleman, Section 1](https://library.slmath.org/books/Book37/files/okonek.pdf).

## 3. The positive-spinor connection has the needed L2 curvature budget

Write \(\mathscr F_A\) for the curvature of the connection on \(S^+\),
distinguishing it from the determinant curvature \(F_A\). The curvature
representation is

\[
 (\mathscr F_A)_{ij}
 =\left.\frac14\sum_{k,l}R_{ijkl}c(e_k)c(e_l)\right|_{S^+}
        +\frac12(F_A)_{ij}I.
\]

Anti-self-dual two-forms act trivially on \(S^+\), with the orientation
convention of (5). In the Riemann-curvature block matrix

\[
 \mathcal R=
 \begin{pmatrix}
 W^++sI/12&\operatorname{Ric}^{\circ}_{+-}\\
 \operatorname{Ric}^{\circ}_{-+}&W^-+sI/12
 \end{pmatrix},
\]

the output projection to \(\Lambda^+\) therefore removes the \(W^-\)
block. With a numerical dimensional constant,

\[
 |\mathscr F_A|^2\le C\bigl(|W^+|^2+s^2+
                   |\operatorname{Ric}^{\circ}|^2+|F_A|^2\bigr).
                                                               \tag{8}
\]

The determinant curvature is controlled without estimating its
anti-self-dual part pointwise. Equation (5) and Chern--Weil give

\[
 |F_A^+|^2=f^2\rho^2/8,\qquad
 \|F_A^+\|_2^2-\|F_A^-\|_2^2=4\pi^2a^2,
\]
\[
 \|F_A\|_2^2=2\|F_A^+\|_2^2-4\pi^2a^2
 \le\frac94\int f^2+4\pi^2(-a^2)_+.                         \tag{9}
\]

Moreover
\(\int|W^+|^2\le(d_{\rm cal}+25\operatorname{Vol}M)/192\)
and \(q\le5+\sqrt6|W^+|\). Therefore, writing \(V=\operatorname{Vol}M\),

\[
 \fint|\mathscr F_A|^2\le C(1+d_{\rm cal}/V+B_a)+o(1).         \tag{10}
\]

No bound on \(a^2\) from above is required. In particular \(a^2\ge0\)
is sufficient with a universal right-hand side when the calibration
defect is bounded in average.

The spinor rough-Laplacian equation is

\[
 4\nabla_A^*\nabla_A\Phi+(s+f\rho)\Phi=0.                    \tag{11}
\]

Since \(|s|\le5\), \(\rho\le3\), and \(\fint f^2\) is bounded by
\(C(1+d_{\rm cal}/V)\), it yields

\[
 \fint|\nabla_A^*\nabla_A\Phi|^2\le C(1+d_{\rm cal}/V)+o(1),
 \qquad\fint|\nabla_A\Phi|^2\le15/4.                       \tag{12}
\]

The second inequality follows by pairing (11) with \(\Phi\) and
discarding the nonnegative \(f\rho^2\) term.
Lemma 1, \(\operatorname{Ric}\ge-2g\), and (10)--(12) now give

\[
 \fint\left(|\nabla_A^2\Phi|^2+|\nabla_A\Phi|^4\right)
       \le C(1+d_{\rm cal}/V+B_a)+o(1).                     \tag{13}
\]

Both sides are extensive before division by V: the use of Young's
inequality does not introduce a factor of V or require V to be bounded.

The quadratic map \(\Phi\mapsto\psi\) is parallel, and
\(\Phi\mapsto A_\psi\) is a parallel polynomial of degree four.
Consequently

\[
 |\nabla^2A_\psi|
 \le C\bigl(|\Phi|^3|\nabla_A^2\Phi|
                  +|\Phi|^2|\nabla_A\Phi|^2\bigr).
\]

The U(1) phase cancels from this associated-bundle map. Thus

\[
 \boxed{\quad\fint|\nabla^2A_\psi|^2
       \le C(1+d_{\rm cal}/V+B_a)+o(1).\quad}                \tag{14}
\]

This is the missing estimate. No limiting gauge or common coordinate
space has been constructed or used.

## 4. The weak Bianchi source can now be tested against itself

Let \(J_\psi=\operatorname{div}W(A_\psi)\), where
\(W(A)_{ijkl}=\frac12A_{ab}(\omega_a)_{ij}(\omega_b)_{kl}\)
in the self-dual frame of round two. The norm of J is the ordinary
three-index norm; A has operator Hilbert--Schmidt norm.
Because this identification and all metric contractions are parallel,

\[
 \|\nabla J_\psi\|_2\le C\|\nabla^2A_\psi\|_2.              \tag{15}
\]

For every smooth test tensor T of the same type, contracted Bianchi
and one covariant integration by parts give

\[
 \left|\int\langle J_\psi,T\rangle\right|
 \le C(\|E\|_2+\|R\|_2)\|\nabla T\|_2.                    \tag{16}
\]

Indeed, \(J_\psi=\operatorname{div}W^+-\operatorname{div}W(R)\);
the first term is a fixed contraction of \(\nabla E\) and
\(\nabla\operatorname{tr}E\). This is an intrinsic calculation.
There are no derivatives of coordinate coefficients or frame choices.
Set \(T=J_\psi\), and use (7), (14), and (15):

\[
 \fint|J_\psi|^2
 \le C\sqrt{\varepsilon+\eta/V}\,
       \sqrt{1+d_{\rm cal}/V+B_a}+o(1).                    \tag{17}
\]

The former H-minus-one obstruction is resolved by proving an H1 bound
for this very test tensor. No inference from small H-minus-one norm
alone to small L2 norm is made.

## 5. The surviving divergence energy supplies a contradiction

Round two proved that if \(\varepsilon_j\to0\), with approximation
errors \(\eta_j=o(V_j)\), then

\[
 \fint|J_{\psi_j}|^2\longrightarrow1/16.                    \tag{18}
\]

For completeness this has a quantitative version not requiring a
compactness argument. Put
\(B_\psi=(s/3)\rho^2-2\langle W^+\psi,\psi\rangle\).
The first-jet and weighted Hodge identities from round two combine to

\[
\begin{split}
 \int|J_\psi|^2={}&-\frac1{64}\int\rho^2B_\psi
 +\frac1{16}\int\rho^2|d\psi|^2
 -\frac5{96}\int\rho^2|d\rho|^2\\
 &+\frac18\int\rho\langle\iota_{\nabla\rho}\psi,*d\psi\rangle.
                                                               \tag{19}
\end{split}
\]

All weighted expressions extend over the zero set of \(\psi\); for the
actual spinor used here, \(\rho=|\Phi|^2\) is already smooth everywhere.
Using \(W^+=A_\psi+R\), the first integrand becomes

\[
 -\rho^2B_\psi/64
 =-s\rho^4/192-\rho^6/384
                   +\rho^2\langle R\psi,\psi\rangle/32.
\]

At \(s=-4\), \(\rho=\sqrt2\) this is \(1/16\).
The amplitude bound, (6), (7), and Cauchy--Schwarz therefore give

\[
 \fint|J_\psi|^2
 \ge1/16-C\left(\sqrt{\varepsilon+\eta/V}
                         +\varepsilon+\eta/V\right).       \tag{20}
\]

The two derivative-error factors in the last term of (19) are both
bounded by the monopole deficit; no derivative-energy uniform
integrability is assumed. Formula (19) and the scalar value 1/16 are
checked algebraically in `round3_rigidity_check.py`, using the previously
verified first-jet identity.

Combining (17) and (20), and then making the smooth-weight approximation
arbitrarily accurate, proves the following.

**Theorem 2 (intrinsic monopole calibration gap).** There is a universal
constant \(c>0\) such that every metric and actual monopole class satisfying
the hypotheses of Section 2 obey

\[
 \boxed{\quad
 \left(1+\frac{(-a^2)_+}{\operatorname{Vol}M}\right)
 \left[\delta^2+\frac{\Delta+d_{\rm cal}}{\operatorname{Vol}M}\right]
 \ge c.\quad}                                               \tag{21}
\]

To see the universal product form, first restrict to
\(\varepsilon\le\varepsilon_0\), where the right side of (20) is
at least 1/32. Then (17) gives
\(\varepsilon(1+B_a+\varepsilon)\ge c_1\).
Since \(\varepsilon\le\varepsilon_0\le1\), this implies
\((1+B_a)\varepsilon\ge c_1/2\). If
\(\varepsilon>\varepsilon_0\), the conclusion is automatic after
decreasing c. The constant is not numerically optimized here.

In particular \(a^2\ge0\) removes the first factor. More generally,
vanishing calibration and monopole defects require
\((-a^2)_+/V\) to diverge at least on the reciprocal-defect scale.

## 6. Scope and proof obligations for topological applications

For the exact critical connected-sum class in the manuscript,
\(a^2=2A/3+4m-4+4b_1(N)>0\), and the supplied budgets give
\(\varepsilon\le C\delta^2\). Theorem 2 therefore supplies a
universal positive lower bound on \(\delta\), with no full-curvature,
collapse, diameter, volume, or Cotton assumption.

For a nearby topological family one must additionally verify its
actual-monopole existence, the selected projection bound, and the
calibration and monopole deficit budgets. A mere sign cube of cohomology
classes is insufficient. Those checks belong to the precise family
statement, not to Lemma 1 or Theorem 2. The root round-three synthesis
records the blow-up-family specialization separately.

The theorem is narrower than an arbitrary geometric calibration gap:
without the actual spinor PDE and the determinant Chern--Weil budget,
the Hessian estimate (14) has not been established. It proves no
Einstein-existence theorem, constructs no all-sign counterexample, and
does not contradict the functional endpoint counterexample in round
two, which deliberately lacked the monopole equations.

## 7. Verification and provenance

The proof was developed in the isolated round-three worktree after
reading the live `qiushi-yau26/SKILL.md` and the round-two notes. The
bundle Hessian commutator and the absence of W-minus from positive
spinor curvature were independently checked by the root agent.

The accompanying exact checker verifies (3) on a nonconstant unitary
connection over a flat four-torus, including its nonzero curvature
cross-term; checks the Clifford chirality projection on all three
anti-self-dual generators; and verifies the coefficient elimination in
(19). These checks support the displayed algebra. The general analytic
statements are proved above, not certified by examples. No live Skill,
Session, service, environment, or external repository has been changed.
