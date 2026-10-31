# A linear-size exclusion neighbourhood on the actual closed bundle

20 September 2026. This note combines the uniform product estimate in
`round6_weighted_inverse.md` with a finite-collar reduction on the original
balanced metrics G_epsilon on E_D. It does not integrate nonconstant
transfer modes into fictitious global parameters. Their exact signed
receiver is retained instead.

## 1. Result

Let the fibre waist be epsilon, the base waist beta=epsilon squared, and
keep the other hyperbolic moduli in the fixed single-nonseparating-pinching
family. Put E(g)=Ric(g)+g and
`delta_-(g)=||g^(-1)E(g)||_(infinity,op)`. C2 norms of perturbations are
relative to the original G_epsilon.

**Theorem.** There are positive constants c_star,c_1,epsilon_0 such that
for every smooth symmetric tensor h with

\[
 0<\varepsilon<\varepsilon_0,\qquad
 a:=\|h\|_{C^2(G_\varepsilon)}\le c_*\varepsilon,
 \qquad g=G_\varepsilon+h,
 \tag{1.1}
\]

one has

\[
 \delta_-(g)\ge c_1\varepsilon^3.
 \tag{1.2}
\]

No symmetry, block structure, gauge condition, or support restriction is
placed on h. In particular no exact normalized Einstein metric lies in
this fixed-multiple linear-size ball. The existing three-scalar correction
lies in the ball and has defect O(epsilon cubed), so its minimum possible
defect order is exactly cubic.

For the smaller asymptotic condition a=o(epsilon), the full previous
coefficient is retained:

\[
 \liminf_{\varepsilon\to0}
 \frac{\delta_-(G_\varepsilon+h_\varepsilon)}{\varepsilon^3}
             \ge\frac1{16\pi^4(p-1)}.
 \tag{1.3}
\]

The constants c_star and c_1 are not numerically optimized. As before, a
nearby Einstein metric of any Einstein constant can be rescaled to constant
minus one; reducing c_star by a fixed factor also excludes such metrics.
The statements do not exclude distant Einstein metrics on E_D.

## 2. The closed detector and the comparison product

Retain the actual global TT tensor Q_epsilon, normalized on the central
base collar by

\[
 Q_0=f(t)T,\qquad f=\operatorname{sech}^2t,
 \qquad T=dt^2-\cosh^2t\,dy^2,
 \qquad y=\beta\theta.
\]

The established original-background estimates are

\[
 \frac1\beta\int\langle E(G_\varepsilon),Q_\varepsilon\rangle
   =-c_0\varepsilon^3(1+o(1)),\qquad c_0=\frac1{2\pi^2},
\]
\[
 \beta^{-1}\|J_GQ_\varepsilon\|_1\le C\varepsilon^2,
 \qquad
 \beta^{-1}\int|Q_\varepsilon|_*\longrightarrow
                          M_0=8\pi^2(p-1).
 \tag{2.1}
\]

Let h_F be the closed hyperbolic fibre metric at the left end of the
balanced path, and introduce the complete comparison product

\[
 g_* =dt^2+\cosh^2t\,dy^2+h_F
               \quad\hbox{on }\mathbb R\times\mathbb R_y\times F_\varepsilon.
 \tag{2.2}
\]

All integrations after angular averaging use one unit of y-length. Put

\[
 w(t)=\operatorname{sech}t,
 \qquad d\nu=w(t)\,dt\,dA_{h_F},\qquad
 \|U\|_{H^k_\nu}^2=\sum_{j=0}^k\int|\nabla_*^jU|^2\,d\nu.
 \tag{2.3}
\]

The measure has uniformly bounded total mass, since the closed fibre area
is 4 pi(p-1). The form Q_0 and each of its derivatives have norm at most
a constant times f; equivalently their natural product-volume integrals
are controlled by dnu.

This comparison respects the actual marking. The bundle over the entire
base annulus is exactly `F x (-w(beta),w(beta)) x S1`. Its angular loop
has trivial cyclic monodromy. The Dehn-twist transition occurs at the
positive t-face to the exterior, not at theta=1. Tensor components in this
trivialization are therefore exactly beta-periodic in y.

The full balanced path h_tau(t) is uniformly O(epsilon) close to h_F in
every fixed local-cover Ck norm on this whole annulus. In the fibre collar
its relative shear is
`epsilon tau(t) chi_R(u) sech(u)^2/I_R`; it vanishes outside that collar.
Its derivatives have the same bound. Thus

\[
 \|G_\varepsilon-g_*\|_{C^k(g_*)}\le C_k\varepsilon.
 \tag{2.4}
\]

This is a metric comparison within a marked annular trivialization, not
a trivialization of E_D over the closed base.

## 3. Finite-collar cutoff and the actual linear forcing

It suffices to prove (1.2) when delta_-(g)<=epsilon cubed; if the reverse
inequality holds there is already a stronger lower bound. For (1.3) take
a subsequence on which delta_-(g)/epsilon cubed is bounded. Write delta
for this defect and set

\[
 \eta=\delta+\varepsilon^2+\varepsilon a+a^2.
 \tag{3.1}
\]

The exact Ricci Taylor formula, (2.4), and E(G)=O(epsilon squared) give
on the base annulus

\[
 \|DE_{g_*}h\|_\infty\le C\eta.
 \tag{3.2}
\]

Choose a fixed-width cutoff chi_L(t), equal to one for |t|<=L-1 and zero
for |t|>=L, where `L=w(beta)-c` with one fixed safe margin c. Extend
`chi_L h` by zero to the entire product (2.2), and average it in the
actual beta-periodic angular variable. Call the resulting y-independent
tensor H. Covariant norms relative to the product satisfy

\[
 \|H\|_{C^2(g_*)}\le Ca,
 \qquad \|H\|_{H^2_\nu}\le Ca.
 \tag{3.3}
\]

The product linearized equation commutes with angular translations.
Its cutoff commutator is O(a) and supported where dnu has mass O(exp(-L))
=O(beta). Consequently, for F=DE_(g_star)H,

\[
 \|F\|_{L^2_\nu}\le C(\eta+a\sqrt\beta)\le C\eta.
 \tag{3.4}
\]

The last inclusion uses sqrt(beta)=epsilon. Neither a boundary value nor
a boundary flux is set to zero. The actual values at the two collar faces
enter the commutator in (3.4).

Freezing the t-dependent fibre operator in (3.2) also retains its TT
transport error: it is part of the O(epsilon a) term. No parallel or
globally invariant identification of the fibre TT spaces is presumed.
For a<=c epsilon, every term in (3.1) is O(epsilon squared).

## 4. Quantitative angular reduction of the quadratic receiver

Define the product quadratic pairing on invariant tensors by

\[
 \mathcal B_*(U,U)=\frac12\int
        \langle D^2E_{g_*}[U,U],Q_0\rangle\,dV_{g_*},
 \tag{4.1}
\]

with one unit y-period. The corresponding bilinear form obeys

\[
 |\mathcal B_*(U,V)|\le C\|U\|_{H^2_\nu}\|V\|_{H^2_\nu}.
 \tag{4.2}
\]

Indeed the second Ricci variation consists of contractions of
`U nabla^2 V`, `V nabla^2 U`, `nabla U nabla V`, and curvature times UV.
The background curvature is uniformly bounded and Q_0 supplies the weight
f. Cauchy--Schwarz proves (4.2) independently of the fibre injectivity radius.

One integration by parts also gives

\[
 |\mathcal B_*(U,U)|\le C\|U\|_{H^1_\nu}^2
 \tag{4.3}
\]

for compactly t-supported fields; derivative terms on Q_0 have the same
weight. The identity remains valid when integrating over the actual short
y-period, with that period divided out.

Let V_osc=chi_L h-H. On each y-circle its mean is zero, as is the mean
of its covariant derivative, since translation is a product isometry.
The physical circle length is beta cosh t. Periodic Poincare, applied in
translation-invariant orthonormal frames to V_osc and its first covariant
derivative, gives

\[
 \fint_y\bigl(|V_{\rm osc}|^2+|\nabla V_{\rm osc}|^2\bigr)
               \le Ca^2\beta^2\cosh^2t.
\]

Integrating against w on |t|<=L yields

\[
 \|V_{\rm osc}\|_{H^1_\nu}^2
       \le Ca^2\beta^2\int_{-L}^L\cosh t\,dt
       \le C\beta a^2.
 \tag{4.4}
\]

Here the norm includes averaging over y. This argument uses the given C2
bound; it does not assume that second angular derivatives tend pointwise
to zero. Bilinear cross terms between H and V_osc vanish after angular
integration. Equations (4.3)--(4.4) therefore bound the omitted Fourier
response by C beta a squared.

The discarded base ends and exterior have beta-normalized detector mass
O(beta). The actual differential differs from Q_0 by O(beta squared),
giving the same total error. Finally changing the background from G to
g_star in the second Ricci variation costs C epsilon a squared by (2.4).
Altogether the actual global quadratic pairing satisfies

\[
 \left|\frac1{2\beta}\int_{E_D}
   \langle D^2E_G[h,h],Q_\varepsilon\rangle\,dV_G
                  -\mathcal B_*(H,H)\right|
       \le C(\varepsilon+\beta)a^2.
 \tag{4.5}
\]

## 5. Bounded gauge removal has a controlled nonzero error

The product is Einstein, with Ric=-g_star. For
`b=-div+(1/2)d tr`, one has

\[
 b(\mathcal L_Xg_*)=(\nabla^*\nabla+1)X^\flat.
 \tag{5.1}
\]

Solve `(nabla*nabla+1)X^flat=bH` by Dirichlet exhaustion. Kato's maximum
principle gives `||X||_infinity<=||bH||_infinity<=Ca`; uniform local-cover
estimates give `||X||_C2<=Ca`. Average X in y. Weighted covariant elliptic
estimates also give

\[
 \|X\|_{H^3_\nu}\le C\bigl(\|bH\|_{H^1_\nu}
                            +\|X\|_{L^2_\nu}\bigr)\le Ca.
 \tag{5.2}
\]

These constants are independent of the fibre waist. One can prove (5.2)
by commuting the rough Laplacian, integrating against f dV, and absorbing
the lower derivative terms: the curvature is parallel and bounded, and
all derivatives of log f are bounded. This is a covariant weighted L2
estimate, not a use of a uniform injectivity radius.

Set V=H-L_Xg_star. Then

\[
 bV=0,\qquad LV=F,\qquad
 L=\tfrac12(\nabla^*\nabla-2\mathring R),
 \qquad \|V\|_{H^2_\nu}\le Ca.
 \tag{5.3}
\]

The quadratic receiver is not exactly gauge invariant here, because F
need not vanish. Differentiating the naturality identity for
`phi_s^*(g_star+sV)` gives

\[
 D^2E[H,H]-D^2E[V,V]
       =2\mathcal L_XF-DE[W],
 \qquad W=2\mathcal L_XV+\mathcal L_X^2g_*
                         =\mathcal L_X(H+V).
 \tag{5.4}
\]

The tensor W belongs to L2_nu, with norm O(a squared). Since Q_0 is TT
and LQ_0=0, its pairing with DE W vanishes by exhaustion: transfer the
derivatives to cutoff times Q_0, and use the integrability of f dV and
the corresponding derivative bounds. For the remaining term transfer
the Lie derivative from F to the test. Its coefficient is bounded by
`Ca f`, because X and its first derivative are O(a). Thus

\[
 |\mathcal B_*(H,H)-\mathcal B_*(V,V)|
                      \le Ca\|F\|_{L^2_\nu}\le Ca\eta.
 \tag{5.5}
\]

This explicitly retains the non-Jacobi gauge term. No small bound on a
third derivative of the original correction or on a derivative of F is
required.

## 6. Weighted projection, with every transfer direction retained

The uniform estimate proved in `round6_weighted_inverse.md` applies to
the closed F_epsilon: its scalar first eigenvalue is uniformly positive
for this fixed nonseparating degeneration, and its trace-free Einstein
operator has the exact gap two off the fibre TT space. It supplies

\[
 V=K+r,\qquad
 \|r\|_{H^2_\nu}\le C\|LV\|_{L^2_\nu}\le C\eta,
 \qquad
 \|K\|_{H^2_\nu}\le C(a+\eta),
 \tag{6.1}
\]

where the complete weighted product kernel is

\[
 K=f(a_0T+b_0S)+A+J(t)B,\qquad
 J(t)=\arctan(\sinh t),\qquad A,B\in\mathcal T(F_\varepsilon).
 \tag{6.2}
\]

Here S is the horizontal off-diagonal trace-free polarization. The field
B is **not** discarded or asserted to integrate to a global closed
deformation. For each epsilon the fibre is compact, so A and B are smooth
and bounded; a uniform maximum-norm bound on their TT projection is not
needed in (6.1).

The exact determinant-preserving fibre calculation, valid on every closed
hyperbolic F, gives

\[
 \mathcal B_*(K,K)=-\frac\pi8\|B\|_{L^2(F)}^2\le0.
 \tag{6.3}
\]

For clarity, realize its horizontal part by the exact cylinder family and
its vertical part by `h_s=h_F exp(s h_F^(-1)(A+JB))`. The fibre determinant
is fixed. The second horizontal Ricci variation is
`-(1/2)J'(t)^2|B|^2 dt^2`; the path acceleration has zero linear pairing
with Q_0. Since `integral sech(t)^3 dt=pi/2`, this gives (6.3).
It does not require a small parameter interval uniform in epsilon.

Using (4.2) and (6.1),

\[
 \mathcal B_*(V,V)
   \le C\eta(a+\eta).
 \tag{6.4}
\]

Thus the signed receiver can be controlled without a uniform global
parameter modulation theorem and without imposing any end compatibility
on J(t)B.

## 7. The complete error ledger and the conclusion

The closed TT identity, Taylor expansion, (4.5), (5.5), and (6.4) imply

\[
 \begin{split}
 \frac1\beta\int\langle E(G+h),Q_\varepsilon\rangle
 \le{}&-c_0\varepsilon^3(1+o(1))\\
 &+C\bigl[\varepsilon^2 a
           +a\eta+\eta^2
           +(\varepsilon+\beta)a^2+a^3\bigr].
 \end{split}
 \tag{7.1}
\]

Every term has a specified source: the actual adjoint defect, product
forcing and gauge, the weighted remainder, background/angular comparison,
and the cubic Ricci remainder. In particular the exterior contribution is
estimated rather than declared zero.

If a<=c_star epsilon and delta<=epsilon cubed, then
`eta<=C(1+c_star+c_star^2)epsilon^2`. The bracket in (7.1), divided by
epsilon cubed, is bounded by
`C(c_star+c_star^2+c_star^3)+O(epsilon)`. Choose c_star small once.
For sufficiently small epsilon the right side of (7.1) is at most
`-c_0 epsilon^3/2`. Duality with the nuclear norm in (2.1), with the
1+O(a) norm comparison, proves (1.2).

If a=o(epsilon) and delta=O(epsilon cubed), then eta=O(epsilon squared)
and every term in the bracket is o(epsilon cubed). The same duality gives
the full coefficient c_0/M_0 in (1.3). Subsequence selection handles an
arbitrary finite liminf; an infinite liminf already satisfies the claim.

An Einstein metric in this small ball necessarily has
`lambda=-1+O(epsilon^2+a)`. Scaling it by -lambda changes its distance
from G by at most a fixed multiple of a+epsilon squared. Shrinking the
radius in (1.1) by that fixed factor excludes all Einstein constants.
The O(epsilon squared) displacement to the corrected background is also
absorbed in the same way.

## 8. What was proved, and what remains open

The receiver-weighted *modulation* estimate from round five was stronger
than needed. The proof instead uses a uniform weighted inverse modulo the
full product kernel, then retains the sign of every transfer direction.
The actual clutching survives as a controlled forcing term and boundary
cutoff term; there is no change of the underlying smooth bundle.

This excludes repairs with sufficiently small fixed linear coefficient,
and in particular all o(epsilon) repairs. It does not exclude corrections
of size C epsilon with an arbitrary large fixed C, arbitrary o(1)
corrections, or Einstein metrics outside this degenerating neighbourhood.
No assertion of a solution of unrestricted Yau26 is made.

The linear-size ball reaches a fixed fraction of the original O(epsilon)
shear. Extending the conclusion to an arbitrary fixed multiple is not
merely an improvement of the inverse constant: at a=C epsilon the terms
epsilon squared times a, epsilon times a squared, and a cubed in (7.1)
are all of the same order as the negative epsilon-cubed source. They
include the actual-background forcing and cubic response, whose signs
this estimate does not determine. A further exclusion needs their
combined signed contribution together with the genuine monodromy and
face matching, or a nonlinear energy identity controlling the same data.
The uniform weighted inverse alone does not provide this information.

`round6_construction_check.py` checks the finite-period weighted mass,
angular Poincare scale, gauge naturality bookkeeping, and the asymptotic
error ledger. The companion weighted inverse proof and its checker supply
the separate analytic operator input.
