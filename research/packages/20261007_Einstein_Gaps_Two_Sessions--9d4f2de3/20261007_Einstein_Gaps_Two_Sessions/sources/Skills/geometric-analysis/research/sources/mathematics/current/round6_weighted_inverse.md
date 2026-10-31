# A uniform inverse in the measure selected by the closed receiver

20 September 2026.

The maximum-norm inverse in a pinching collar need not be uniform. The
closed TT receiver selects a different norm. In that norm the full product
Einstein operator has a uniform inverse modulo its signed kernel, including
the fibre-transfer modes. No integration of these modes into global bundle
parameters is required.

## 1. The finite-fibre product and the estimate

Let \(F_\varepsilon\) be the closed hyperbolic fibre of the balanced
\(E_D\) construction: one nonseparating geodesic has length
\(\varepsilon\), the genus \(p\) is fixed, and the remaining marked
hyperbolic data stay in the specified compact family. Set

\[
 X_\varepsilon=(\mathbb R_t\times\mathbb R_y,
          dt^2+\cosh^2t\,dy^2)\times F_\varepsilon,
 \quad w=\operatorname{sech}t,\quad f=w^2,\quad k=\tanh t,
 \quad J=\arctan(\sinh t).
\]

Tensors below are independent of \(y\); integration is per unit coordinate
length in \(y\). Define the weighted Sobolev norm by

\[
 \|u\|_{H^j_w}^2=
 \sum_{i=0}^j\int_{\mathbb R\times F_\varepsilon}
                 |\nabla^iu|^2w(t)\,dt\,dV_F.
 \tag{1.1}
\]

All derivatives and norms are product geometric ones. The measure in (1.1)
is comparable, with absolute constants, to
\(|Q|dV_{X_\varepsilon}\), where
\(Q=fT\) and \(T=dt^2-\cosh^2t\,dy^2\). This is precisely the measure
in the beta-normalized closed receiver. Its total mass is
\(4\pi^2(p-1)\), independent of \(\varepsilon\).

Put \(2L=\nabla^*\nabla-2\mathring R\). There is a constant \(C\),
independent of \(\varepsilon\), such that every smooth invariant tensor
\(V\) with finite \(H^2_w\) norm admits

\[
 V=K+r,\qquad
 K=f(aT+bS)+A+J B,\qquad
 \|r\|_{H^2_w}\le C\|LV\|_{L^2_w}.
 \tag{1.2}
\]

Here \(S\) is the off-diagonal horizontal trace-free polarization and
\(A,B\) are TT tensors on the **actual closed** fibre
\(F_\varepsilon\). In particular

\[
 \|K\|_{H^2_w}\le\|V\|_{H^2_w}+C\|LV\|_{L^2_w}.
 \tag{1.3}
\]

There is no uniform pointwise bound asserted for the TT projection of an
arbitrary tensor. The argument needs only (1.2)--(1.3).

The fibre scalar gap used here is \(\lambda_1(F_\varepsilon)\ge\lambda_*>0\).
Here is a direct argument for this single nonseparating degeneration.
If mean-zero, unit \(L^2\) first eigenfunctions had energy tending to
zero, then on the connected thick complement and its fixed-width collar
shoulders they would converge to the same constant \(c\). The constants
are bounded by their \(L^2\) normalization. On the hyperbolic collar the
Dirichlet radial operator, conjugated by \(\sqrt{\cosh u}\), is

\[
 -\partial_u^2+\frac14+\frac14\operatorname{sech}^2u\ge\frac14;
\]

the angular contribution is nonnegative. Multiply the eigenfunction
minus \(c\) by a cutoff which is one in the middle collar and vanishes
on the two shoulders. Its gradient energy tends to zero, since the cutoff
derivatives lie on the fixed-width shoulders where convergence already
holds. The Dirichlet estimate forces its entire collar \(L^2\) norm to
zero. Therefore the original eigenfunctions converge globally in
\(L^2\) to \(c\); their zero means give \(c=0\), contradicting unit norm.
Connectedness of the thick complement is essential. This argument would
not apply to a separating pinch. For the corresponding classical
spectral result see [Ji--Wentworth, *Spectral convergence on degenerating
surfaces*, p. 493](https://math.umd.edu/~raw/papers/spectrum.pdf).

## 2. Tensor blocks and the weighted energy identity

Write \(P=\partial_t^2+k\partial_t\), and use the nonnegative Laplace
convention. The product connection splits \(2L\) as follows:

| Tensor block | Scalar or bundle operator |
| --- | --- |
| Horizontal and vertical traces | \(-P+\Delta_F+2\) |
| Horizontal trace-free polarizations | \(-P+\Delta_F+2-4f\) |
| Mixed one-form coefficients | \(-P+\Delta_{H,F}+2-f\) |
| Fibre trace-free tensors | \(-P+A_F\), \(A_F=2P_F\delta_F\) |

The nonzero spectrum of \(A_F\) is at least two, since
\(2\delta_FP_F=\Delta_{H,F}+2\). This identity is on the closed fibre
and does not require an injectivity-radius bound.

For a real scalar coefficient and real potential \(V_0(t)\), integration
by parts gives

\[
 \int wu(-P+V_0)u
 =\int w\{(u')^2+(V_0+2f-1)u^2\}.
 \tag{2.1}
\]

The trace, mixed, and positive fibre-TF sectors therefore have uniformly
positive real part. At high fibre eigenvalue \(\lambda\), their energy
estimates and their equations give

\[
 \lambda\|u\|_{L^2_w}
 +\sqrt\lambda\|u'\|_{L^2_w}
 +\|u''\|_{L^2_w}\le C\|F\|_{L^2_w}.
 \tag{2.2}
\]

At bounded eigenvalue the corresponding estimate uses \(1+\lambda\).
Only the horizontal zero mode and the vertical TT block require further
arguments.

## 3. Horizontal block: factorization removes the apparent resonance

On \(L^2(wdt)\) set

\[
 D_1=\partial_t+2k,\qquad D_2=-\partial_t+k=\partial_t^*.
\]

The two products are

\[
 A_\lambda:=D_2D_1+\lambda=-P+2-4f+\lambda,
 \qquad
 B_\lambda:=D_1D_2+\lambda=-P+2-f+\lambda.
 \tag{3.1}
\]

Thus the partner of the resonant horizontal operator is exactly a
coercive mixed-block operator. If \(A_\lambda z=F\) and
\(v=D_1z\), then weakly

\[
 B_\lambda v=D_1F.
\]

Testing this equation with \(v\), using (2.1) and
\(D_1^*=-\partial_t+3k\), gives

\[
 \|v'\|_{L^2_w}+\sqrt{1+\lambda}\|v\|_{L^2_w}
       \le C\|F\|_{L^2_w}.
 \tag{3.2}
\]

This is an \(H^{-1}\)-to-\(H^1\) estimate; differentiability of \(F\)
is not being assumed. Exhaustion and weak convergence justify testing.

There is also a uniform first-order estimate modulo \(f\), because

\[
 D_1D_1^*=-\partial_t^2+k\partial_t+6-3f\ge3
       \quad\text{in }L^2(wdt),
 \qquad \ker D_1=\operatorname{span}\{f\}.
 \tag{3.3}
\]

The closed-range estimate for \(D_1\), followed by
\(z'=D_1z-2kz\), gives
\(\|z-cf\|_{H^1_w}\le C\|D_1z\|_{L^2_w}\) for the orthogonal
projection coefficient \(c\). Replacing this projection with the
coefficient that makes \(\int w(z-cf)=0\) is a bounded rank-one change.

For \(\lambda=0\), retain \(cf\) in the kernel. Then (3.2), (3.3),
and the equation bound \(z-cf\) in \(H^2_w\). The range identity is
\(\int wF=0\), because the weighted adjoint kernel is the constant one.
For \(\lambda\ge\lambda_*\), the same integration gives

\[
 \lambda\int wz=\int wF,
 \tag{3.4}
\]

so the coefficient of \(f\) is controlled as well. This proves the
uniform estimate for \(\lambda\in[\lambda_*,2]\). For \(\lambda\ge2\),
(2.1) directly gives (2.2), since
\(V_0+2f-1=\lambda+1-2f\ge\lambda-1\).

All integrations at infinity can first be made with compactly supported
cutoffs. Weighted \(H^2\) bounds make the boundary terms vanish along an
exhaustion. The formal intertwining is consequently an estimate on the
full weighted domain, not only on compactly supported test functions.

## 4. Vertical TT block: the transfer mode is retained, not removed

Here the equation is \(-Pu=F\). The solution with zero value and
derivative at zero is, for \(t\ge0\),

\[
 r(t)=-\int_0^t\!\operatorname{sech}u
              \int_0^u\cosh s\,F(s)\,ds\,du.
 \tag{4.1}
\]

The same signed integrals define it for negative \(t\). On the positive
half-line its integral kernel has absolute value

\[
 \cosh s\int_s^t\operatorname{sech}u\,du\le C,
       \qquad 0\le s\le t.
\]

After conjugation by \(\sqrt w\), the kernel is bounded by
\(C e^{-(t-s)/2}\). The first-derivative kernel has still faster
decay. Young's inequality bounds \(r,r'\) in \(L^2_w\); the equation
bounds \(r''\). Reflection gives identical bounds on the other
half-line. Hence

\[
 \|r\|_{H^2_w}\le C\|F\|_{L^2_w},\qquad
 u-r=A+JB.
 \tag{4.2}
\]

This proof works for TT-Hilbert-space-valued coefficients. On a closed
hyperbolic surface, Weitzenbock identities control the first two covariant
derivatives of a TT tensor by its \(L^2\) norm with constants independent
of degeneration. Thus (4.2) also controls the full tensor \(H^2_w\) norm.

Summing the fibre spectral decompositions now proves (1.2). Mixed
derivatives are controlled by the middle term in (2.2); fibre second
derivatives follow from the constant-curvature Bochner identities. These
are global integration identities, not Sobolev embeddings whose constants
might deteriorate on collapsing fibres.

## 5. Gauge and the signed quadratic receiver

For completeness, the invariant gauge operator
\(H=\nabla^*\nabla+1\) on vector fields has horizontal blocks
\(-P+\Delta_F+2-f\) and vertical blocks
\(-P+\Delta_{H,F}+2\). Both are coercive in (2.1). The same estimates
give its weighted \(H^1\)-to-\(H^3\) inverse. This permits Bianchi
gauge removal with quantitative weighted bounds; the nonzero forcing
term in diffeomorphism covariance must still be retained.

For a kernel element in (1.2), the determinant-preserving fibre path
\(h_F\exp[s h_F^{-1}(A+JB)]\) and an exact hyperbolic cylinder path
give

\[
 \mathcal B(K,K):=\frac12\int_{X_\varepsilon}
    \langle D^2(\operatorname{Ric}+g)[K,K],Q\rangle\,dV
       =-\frac\pi8\|B\|_{L^2(F_\varepsilon)}^2\le0.
 \tag{5.1}
\]

Each fibre is closed, so its TT tensors are smooth and bounded for fixed
\(\varepsilon\). The radius of that auxiliary metric path may depend
on \(\varepsilon\); (5.1) is a derivative identity and does not require
a uniform radius or a uniform TT projection in maximum norm.

The polarized receiver obeys

\[
 |\mathcal B(U,V)|\le C\|U\|_{H^2_w}\|V\|_{H^2_w}.
 \tag{5.2}
\]

Indeed, the tensorial second Ricci variation contains only
\(U\nabla^2V\), \(V\nabla^2U\), \(\nabla U\nabla V\), and
bounded-curvature multiples of \(UV\). Multiplication by \(Q\) changes
the volume measure into a bounded multiple of (1.1), so Cauchy--Schwarz
proves (5.2). Combining it with (1.2), (1.3), and (5.1) yields

\[
 \boxed{
 \mathcal B(V,V)
 \le C\|LV\|_{L^2_w}
           \bigl(\|V\|_{H^2_w}+\|LV\|_{L^2_w}\bigr).}
 \tag{5.3}
\]

This is the useful conclusion. It retains every bounded product zero
mode and controls only the positive response needed to cancel the closed
source. A uniform maximum-norm inverse or a nonlinear parametrization of
all modes is unnecessary for this estimate. Its transfer to arbitrary
perturbations of the closed marked bundle, including angular averaging,
cutoffs, the nonzero gauge forcing, and the cubic remainder, is proved in
[the round-six construction note](round6_construction.md).
