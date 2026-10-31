# Step 22 — Conformal reduction for every smooth exact-CH-ended cell

Normalization: the complex-hyperbolic end has \(\operatorname{Ric}=-6g\), scalar curvature \(s=-24\), and
\[
J_6(g)=\int |\operatorname{Ric}_g+6g|^2=P(g)+\frac14\int(s_g+24)^2.
\]
The Laplacian is \(\Delta=\operatorname{div}\nabla\), so \(\int f\Delta f=-\int|df|^2\) and on \(\mathbf{CH}^2\), for distance from a point,
\[
\Delta r=3\coth r+\tanh r\ge4.
\]

## Theorem

Let \((C,g)\) be a smooth complete connected four-dimensional cell whose marked end is isometric to the exterior distance-sphere end of normalized \(\mathbf{CH}^2\) (or the corresponding finite spherical quotient) outside a compact set. No sign condition on \(s_g\) is imposed. Then:

1. There is a unique smooth positive function \(u\) such that
   \[
   -6\Delta_g u+s_gu+24u^3=0,\qquad u\longrightarrow1
   \]
   on the CH end. Thus \(\widehat g=u^2g\) is complete, asymptotic to the same normalized CH metric, and \(s_{\widehat g}=-24\).
2. For every \(m\) with
   \[
   4<m<2+2\sqrt3,
   \]
   the solution satisfies \(|\nabla^k(u-1)|=O(e^{-mr})\) for every fixed \(k\).
3. The noncompact conformal energy identities have no limiting boundary term:
   \[
   P(g)-P(\widehat g)=24\int_C|\nabla u|^2+3\int_C(\Delta u/u)^2,
   \]
   \[
   J_6(g)-J_6(\widehat g)=\int_C\left[24|\nabla u|^2+3(\Delta u/u)^2+\frac{(s_g+24)^2}{4}\right].
   \]
   Since \(s_{\widehat g}=-24\), \(J_6(\widehat g)=P(\widehat g)\). Equality in the second identity forces \(u=1\) and \(s_g=-24\). In the first identity, constant rescalings give equality on closed manifolds; the end normalization \(u\to1\) removes that freedom here.
4. Let \({\cal C}_{\mathrm{exact}}\) be the smooth exact-CH-ended cell class. For fixed \(\mu>2\), let \({\cal C}_{-24}^{\mathrm{aCH},\mu}\) consist of complete metrics \(h\) on the same marked cell such that \(s_h=-24\) and \(|\nabla_{\mathrm{CH}}^k(h-g_{\mathrm{CH}})|=O(e^{-\mu r})\) for every fixed \(k\). Then
   \[
   \inf_{g\in{\cal C}_{\mathrm{exact}}}P(g)
   =\inf_{g\in{\cal C}_{\mathrm{exact}}}J_6(g)
   =\inf_{h\in{\cal C}_{-24}^{\mathrm{aCH},\mu}}P(h),
   \qquad 2<\mu<2+2\sqrt3.
   \]
   The result is not restricted to an SU(2), diagonal, or Kähler ansatz. The stronger rate \(m>4\) is used to remove the linear transgression in the selection identity for the normalized image of an exact-ended metric; only \(\mu>2\) is needed for direct splicing because its squared residual decays as \(e^{(4-2\mu)R}\). The observed \(r e^{-4r}\) tail belongs to every such class with \(2<\mu<4\). Equality of the infima does not imply attainment. Equality for a class defined by \(\mu\ge2+2\sqrt3\), or for arbitrary \(\mu>2\) without the upper qualification, needs an additional scalar-curvature-preserving gluing or improved decay theorem and is not asserted.

The same existence and selection statement applies inside a symmetry class when the symmetry group preserves the input metric and the CH end: uniqueness makes \(u\) invariant.

## Proof

### 1. Ordered global weak barriers

Choose \(R\) beyond the arbitrary compact core, so \(g\) is exactly CH for \(r\ge R\). Fix any \(a\in(0,4)\). Since \(s_g\) is bounded below on the compact core, choose \(M\ge1\) such that
\[
s_g+24M^2\ge0
\]
everywhere. Define continuous piecewise smooth functions
\[
u_-=\begin{cases}0,&r\le R,\\1-e^{-a(r-R)},&r\ge R,\end{cases}
\qquad
u_+=\begin{cases}M,&r\le R,\\1+(M-1)e^{-a(r-R)},&r\ge R.\end{cases}
\]
They satisfy \(0\le u_-\le u_+\), and both tend to one. Put
\[
F(v)=-6\Delta v+s_gv+24v^3.
\]
On the CH end, writing \(H=\Delta r\ge4\),
\[
\Delta(1-e^{-at})=a(H-a)e^{-at}\ge0,
\]
so
\[
F(u_-)=-6a(H-a)e^{-at}+24u_-(u_-^2-1)\le0.
\]
Similarly
\[
\Delta(1+(M-1)e^{-at})=a(a-H)(M-1)e^{-at}\le0,
\]
and both terms in
\[
F(u_+)=-6\Delta u_++24u_+(u_+^2-1)
\]
are nonnegative. On the core, \(F(u_-)=0\) and \(F(u_+)=M(s_g+24M^2)\ge0\). At \(r=R\), the outward normal derivative of \(u_-\) jumps from \(0\) to \(a\), so the singular part of \(-6\Delta u_-\) is nonpositive. The derivative of \(u_+\) jumps from \(0\) to \(-a(M-1)\), so the singular part of \(-6\Delta u_+\) is nonnegative. Hence these are ordered weak sub- and supersolutions.

On the exhaustion \(\Omega_L=\{r<L\}\), impose \(u=1\) at \(r=L\). Standard ordered sub/supersolution iteration applies after adding a fixed large multiple of \(u\) to make the scalar nonlinearity monotone on \([0,M]\). It gives a smooth solution \(u_L\) with \(u_-\le u_L\le u_+\). Interior elliptic estimates and a diagonal subsequence give a smooth global solution \(u\) with the same bounds. Thus \(u\to1\). It is not identically zero because it is positive on the end. Since it is a nonnegative solution of the linear equation
\[
-6\Delta u+(s_g+24u^2)u=0
\]
with bounded coefficient, the strong maximum principle/Harnack theorem propagates strict positivity through the compact core.

This argument is why the spectral threshold of \(-6\Delta+s_g\) at the zero solution is not an obstruction: the lower barrier is zero only on the compact core and becomes strictly positive on the end.

### 2. Decay and derivatives

Put \(v=u-1\). On the exact CH end,
\[
-6\Delta v+48v+72v^2+24v^3=0.
\]
The first barriers give \(v=O(e^{-ar})\) for each initially chosen \(a<4\). Once \(|v|\) is small, compare with \(Ce^{-mr}\). Since
\[
(-6\Delta+48)e^{-mr}
=6\bigl[-m^2+m(3\coth r+\tanh r)+8\bigr]e^{-mr},
\]
the coefficient is eventually positive for every \(m<2+2\sqrt3\), the positive root of \(m^2-4m-8=0\). A two-sided maximum-principle comparison for the equation with potential \(48+72v+24v^2\) therefore improves the decay to \(|v|=O(e^{-mr})\) for every such \(m\). Interior Schauder estimates on uniformly controlled CH annuli then give \(|\nabla^k v|=O(e^{-mr})\) for every fixed \(k\).

We deliberately use only \(4<m<2+2\sqrt3\). No sharp endpoint asymptotic is needed.

### 3. Boundary terms and exact energy identities

For \(\widehat g=u^2g\) in dimension four,
\[
s_{\widehat g}^2dV_{\widehat g}=(s_g-6\Delta u/u)^2dV_g.
\]
Conformal invariance of \(|W|^2dV\), together with the Chern–Gauss–Bonnet identity on \(C_R\), gives the finite-domain conformal comparison used in Step 21, with a boundary Pfaffian transgression. The difference of the Levi-Civita connections is \(O(|\nabla\log u|)=O(e^{-mr})\), while both background curvature and the second fundamental form of CH coordinate spheres are bounded. The transgression is therefore \(O(e^{-mr})\) pointwise. CH sphere area grows as \(O(e^{4r})\), so its integral is \(O(e^{(4-m)r})\to0\).

The integration-by-parts term \(\int u\Delta u\) has boundary contribution \(\int_{S_r}u\partial_\nu u\), also \(O(e^{(4-m)r})\to0\). Terms quadratic in \(u-1\) or its derivatives decay faster, as \(O(e^{(4-2m)r})\). Letting \(r\to\infty\) in the finite-domain identity proves the two displayed energy formulas. This corrects the overly optimistic Step-21 statement that every boundary term is quadratic: some are linear and require \(m>4\).

The final quadratic energy integrals are already finite for \(m>2\); the stronger choice \(m>4\) is used to remove the linear finite-domain boundary and transgression terms.

### 4. Uniqueness

If \(u_1^2g\) and \(u_2^2g\) both have scalar curvature \(-24\) and \(u_i\to1\), put \(w=u_1/u_2\). Relative to \(g_2=u_2^2g\),
\[
-6\Delta_{g_2}w-24w+24w^3=0,
\qquad w\to1.
\]
If \(w\) has a maximum larger than one, it is achieved in a compact set and at that point both \(-6\Delta w\) and \(24w(w^2-1)\) are positive, a contradiction. A minimum below one gives the opposite contradiction. Thus \(w\equiv1\).

### 5. Equality of infima and exact-collar truncation

The energy identity maps every exact-CH-ended metric to a scalar-normalized complete metric with no greater cost. Conversely, for \(\widehat g=u^2g\) produced above, choose a cutoff \(u_R\) equal to \(u\) inside \(r\le R\) and one outside \(r\ge R+1\), with derivatives uniformly controlled by those of \(u-1\). Then \(g_R=u_R^2g\) is exactly CH outside a compact set, and direct evaluation of the squared Einstein residual gives
\[
J_6(g_R)=P(\widehat g)+O(e^{(4-2m)R}).
\]
No Pfaffian transgression is needed for this cutoff estimate. More intrinsically, for any \(h\in{\cal C}_{-24}^{\mathrm{aCH}}\), splice \(h\) to \(g_{\mathrm{CH}}\) across \([R,R+1]\). The curvature residual in the annulus and discarded tail is \(O(e^{-\mu R})\), so the exact-ended spliced metric has \(J_6=P(h)+O(e^{(4-2\mu)R})\). The selection image of every exact-ended metric decays at every rate \(m<2+2\sqrt3\), so it lies in each fixed class \({\cal C}_{-24}^{\mathrm{aCH},\mu}\) with \(2<\mu<2+2\sqrt3\). Conversely, direct splicing works for every fixed \(\mu>2\). These two directions give equality with the normalized class exactly in the stated range \(2<\mu<2+2\sqrt3\). For larger \(\mu\), splicing still gives only
\(\inf_{{\cal C}_{\mathrm{exact}}}P\le\inf_{{\cal C}_{-24}^{\mathrm{aCH},\mu}}P\); class inclusion does not reverse this inequality. Finally, \(P\le J_6\) on exact-ended metrics, while conformal normalization followed by exact-collar recovery converts any exact-ended \(P\)-competitor into exact-ended metrics with \(J_6\to P(\widehat g)\le P(g)\). Hence the two exact-ended infima are equal.

## Consequences for the Einstein-gap programme

* The scalar channel is eliminated for **all** smooth exact-CH-ended cells, including cells whose scalar curvature is positive somewhere and nonsymmetric cells. The earlier pointwise hypothesis \(s<0\) is unnecessary.
* The unrestricted local upper/lower problem can therefore be posed as minimizing \(P\) on the nonlinear hypersurface \(s=-24\), without assuming diagonal or SU(2) symmetry. A rigorous exact-ended \(P\)-saving is now sufficient for the \(J_6\) transfer after normalization and exact-collar recovery.
* This is an infimum reduction, not existence of a minimizer and not a lower bound for the unrestricted cell value. It does not turn the diagonal numerical value into the global optimum.
* For asymptotically, rather than exactly, CH input metrics, one must additionally state decay of the metric and of the scalar forcing \(s+24\); the theorem above does not silently cover that larger class.
