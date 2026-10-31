# Ricci-flat rational-ball insertion: the first inner variational problem

**Result.** The ordinary Eguchi–Hanson quotient does not inherit the Burns negative logarithm. Its bolt-regular, quadratic biaxial response has a *positive square* as its exact optimized inner Einstein defect. An angular trace-free Ricci response has a negative renormalized inner contribution, but this is a boundary term and does not yet give a closed-manifold descent inequality. These calculations distinguish the two signs that must be retained in the remaining global comparison.

No assertion of smooth attainment, universal smoothing descent, or a complete fourth-order gluing expansion is made here.

## 1. Why changing scalar-flat Kähler mass cannot solve this branch

Let N be an ALE rational homology ball with an ALE scalar-flat Kähler metric. Its Ricci form is an L² harmonic two-form. ALE L² Hodge theory identifies its class with an element of the image of H²_c(N;R) in H²(N;R), which vanishes. Thus its Ricci form vanishes. In addition the scalar-flat Kähler mass formula gives mass zero, because the real first Chern class is zero.

This is classical: Wright, *Quotients of gravitational instantons*, Corollary C, explicitly proves the Ricci-flat conclusion; Hein–LeBrun, *Mass in Kähler geometry*, Theorems 4.2–4.3, give the mass formula. Therefore the useful positive/negative mass choice on O(-3) is unavailable on a rational ball within the scalar-flat Kähler class. Allowing non-Kähler or non-scalar-flat fillers is a different variational problem, whose Ricci energy must be included.

## 2. Normalized core and the permitted quotient

Put

\[
 G(r)=1-r^{-4},\qquad
 g_0=G^{-1}dr^2+r^2(\sigma_1^2+\sigma_2^2+G\sigma_3^2),\qquad r\ge1.
\]

The round three-sphere is normalized by \(g_{S^3}=\sum\sigma_i^2\), of volume \(2\pi^2\). The Eguchi–Hanson link is S³/Z₂. Divide by its free involution covering the antipodal map of the bolt. The resulting ordinary oriented rational ball B₂ has link S³/Z₄ and angular volume

\[
 L:=\operatorname{Vol}(S^3/\mathbb Z_4)=\pi^2/2.
\]

A marking is fixed. The core axis and the invariant complex axis of the Z₄ action cannot be rotated independently. The biaxial metrics below are invariant under this involution and descend. Their additional symmetry is stronger than the symmetry of an arbitrary Z₄-invariant orbifold jet.

For a perturbation set

\[
 F=G+t u+O(t^2),\quad H=G+t v+O(t^2),\quad
 g_t=H^{-1}dr^2+r^2(\sigma_1^2+\sigma_2^2+F\sigma_3^2).
\]

Bolt regularity to first order is

\[
 u(1)=v(1)=0,\qquad u'_r(1)+v'_r(1)=0.
\]

Higher order corrections can enforce the exact bolt condition \(F'(1)H'(1)=16\). Such corrections do not affect the coefficient of \(t^2\) in P on a fixed compact core, since \(\operatorname{Ric}(g_0)=0\).

## 3. Exact response to the biaxial quadratic curvature jet

Use \(x=r^2\). Fix real numbers \(\nu,\mu\) and define

\[
 u=\frac{\nu-\mu}{6}x+\frac{\nu+\mu}{2x}
                 -\frac{2\nu+\mu}{3x^2},
\]
\[
 v=u-\nu(x-x^{-1}).
\tag{1}
\]

These satisfy all three bolt conditions. The chiral curvature convention is \(R^+=W^++sI/12\), with the orientation in which the unperturbed core has R⁺=0. Direct linearization gives

\[
 D R^+_{g_0}[h]=\operatorname{diag}(\nu,\nu,\mu),
 \qquad h=\left.\frac{d}{dt}\right|_0 g_t.
\tag{2}
\]

One short verification of (2) uses d=u−v. The first chiral eigenvalue is

\[
 \dot\lambda_1=\frac{d'_r}{4r}+\frac d{2r^2}=\nu.
\]

For d=νxG, the remaining chiral equation simplifies to

\[
 \dot\lambda_3=-xu_{xx}-4u_x-2u/x+\nu=\mu.
\]

The homogeneous quadratic asymptotic has

\[
 F=1+t\frac{\nu-\mu}{6}r^2+\cdots,
 \qquad H=1-t\frac{5\nu+\mu}{6}r^2+\cdots.
\]

Its Ricci tensor at the cone vertex is \((2\nu+\mu)g\). In particular, this entire biaxial sector has \(\operatorname{Ric}^\circ(p)=0\). This also follows from the irreducibility of the U(2) isotropy representation at the vertex. A general Z₄-invariant trace-free Ricci tensor is not covered by this sector.

The full linearized Ricci tensor of (1), expressed in the g₀-orthonormal frame, is

\[
 D\operatorname{Ric}[h]
 =\operatorname{diag}\left(2\nu+\mu+\mu r^{-4},\,
 2\nu+\mu-\mu r^{-4},\,
 2\nu+\mu-\mu r^{-4},\,
 2\nu+\mu+\mu r^{-4}\right).
\]

Consequently

\[
 D\operatorname{Ric}^\circ[h]=\mu o,\qquad
 o=r^{-4}\operatorname{diag}(1,-1,-1,1),\qquad
 Ds[h]=4(2\nu+\mu).
\tag{3}
\]

The volume form is exactly \(r^3dr\,d\omega\). Hence

\[
 \boxed{\int_{B_2}|D\operatorname{Ric}^\circ[h]|^2=L\mu^2
 =\frac{\pi^2}{2}\mu^2.}
\tag{4}
\]

There is no logarithmic divergence in this inner integral. This is a direct calculation of the Ricci defect, not a deduction from a renormalized chiral density.

For completeness the sectional formulas used to verify (3), with subscripts x denoting derivatives, are

\[
 K_{01}=K_{02}=-H_x,\quad K_{12}=(4-3F-H)/x,
\]
\[
 K_{13}=K_{23}=(F-H)/x-HF_x/F,
\]
\[
 K_{03}=-H(3F_x/F+2xF_{xx}/F-xF_x^2/F^2)
          -H_x(1+xF_x/F).
\]

Taking the usual sums of sectional curvatures yields (3). The attached program verifies the rational identities symbolically.

## 4. The square is the sharp inner minimum for this asymptotic jet

The tensor o in (3) is smooth across the bolt, trace-free, divergence-free and in the L² kernel of the Einstein operator

\[
 \mathcal A=\nabla^*\nabla-2\mathring R.
\]

One way to check the kernel assertion is to differentiate the Ricci-flat family \(G_b=1-br^{-4}\), and add the Lie derivative by \(\tfrac14r^{-3}\partial_r\); the resulting smooth tensor is −o/2. This is the standard scale Jacobi field described in Biquard's Einstein desingularization analysis. Its squared norm is \(\|o\|_2^2=L\).

Let \(\widehat h=h+k\) be any smooth, quotient-invariant linear response with the same homogeneous quadratic asymptotic. Suppose \(k=O(r^{2-\delta})\), with differentiated estimates, for some δ>0, and \(D\operatorname{Ric}^\circ[k]\in L^2\). At a Ricci-flat metric, pairing the linearized Ricci tensor with a TT tensor removes the gauge and trace terms. Green's identity therefore gives

\[
 \int\langle D\operatorname{Ric}^\circ[k],o\rangle
 =\tfrac12\int\langle k,\mathcal A o\rangle=0.
\]

There is no boundary at the smooth bolt, and the boundary at radius R is O(R^{-δ}). Therefore

\[
 \boxed{\int|D\operatorname{Ric}^\circ[\widehat h]|^2
 =L\mu^2+\int|D\operatorname{Ric}^\circ[k]|^2\ge L\mu^2.}
\tag{5}
\]

This is an exact least-squares obstruction for the prescribed quadratic jet, allowing corrections without biaxial symmetry. Equality is attained by (1), but not asserted unique modulo possible zero modes and gauge. The result does not classify all allowed asymptotic jets.

## 5. A non-biaxial trace-free Ricci sector has a negative inner boundary term

This is an additional exact computation, included because dropping this sector would obscure the sign problem.

Use Euler-angle conventions

\[
 \sigma_1^2+\sigma_2^2=\tfrac14(d\theta^2+\sin^2\theta\,d\phi^2),
 \qquad\sigma_3=\tfrac12(d\psi+\cos\theta\,d\phi).
\]

One perpendicular Gibbons–Hawking moment coordinate is

\[
 f=\sqrt{r^4-1}\,\sin\theta\cos\psi.
\tag{6}
\]

Choose the free involution whose action on the Gibbons–Hawking base is a rotation by π around this coordinate axis; it exchanges the two centers and f is invariant. Thus it descends to B₂. At infinity

\[
 f=f_0-\tfrac12r^{-2}\sin\theta\cos\psi+O(r^{-6}),
 \qquad f_0=r^2\sin\theta\cos\psi.
\]

The function is harmonic. Explicitly, with A=√(r⁴−1), the radial Laplacian is
\(r^{-3}(r^3GA')'\), and the angular term is
\(-[8+4(G^{-1}-1)]A/r^2\); they cancel. The squashed-angle term must be retained: replacing ψ by φ in (6) does not give this harmonic function.

Its averaged gradient square is

\[
 \fint_{S^3/\Gamma}|df|^2=4r^2-\frac4{3r^2}.
\]

Since Ric(g₀)=0 and Δf=0, Bochner's identity yields

\[
 \int_{r\le R}|\nabla^2 f|^2
 =\tfrac12\int_{r=R}\partial_n|df|^2
 =L\left(4R^4-\frac83-\frac4{3R^4}\right).
\]

The corresponding Euclidean cone integral for f₀ is 4LR⁴. For the conformal variation \(h_f=2fg_0\),

\[
 D\operatorname{Ric}^\circ[h_f]=-2\nabla^2f.
\]

Thus the **renormalized inner difference** is

\[
 \boxed{\lim_{R\to\infty}\left[
 \int_{r\le R}|D\operatorname{Ric}^\circ[h_f]|^2
 -\int_{r\le R}|D\operatorname{Ric}^\circ_{\rm flat}[2f_0g_{\rm flat}]|^2
 \right]=-\frac{32L}{3}=-\frac{16\pi^2}{3}.}
\tag{7}
\]

The constant flat trace-free Ricci tensor in this normalization has squared norm 64, so (7) can also be written as −L|E₀|²/6 for this one-dimensional sector.

However both the core and flat chiral first variations in this conformal harmonic direction vanish: W⁺ stays zero to first order by conformal invariance, and Ds=−6Δf=0. Formula (7) is entirely a boundary transgression. It must be matched to the exterior correction arising from the r⁻² term of f−f₀. It is **not** by itself a negative complete insertion coefficient.

## 6. What is and is not determined at physical scale a

If an actual two-scale matched metric has inner expansion

\[
 g_a=a^2(g_0+a^2h+O(a^4)),
\]

then on every fixed rescaled compact core the P contribution is a⁴ times the quadratic expression above, up to o(a⁴). In the biaxial sector this is the positive square (4). In the angular conformal sector the finite *difference* after subtraction is (7).

Neither statement permits exchanging the a→0 and R→∞ limits without a matching estimate. The smooth exterior contributes first-variation boundary terms at order a⁴. Criticality removes the interior Euler–Lagrange pairing; it does not erase those boundary terms for a singular asymptotic perturbation. Fourth-order bulk jets and the subleading inner terms must be matched together. A negative chiral inner constant or the negative number (7) cannot be quoted as a closed-manifold descent.

The order −4 Ricci-flat tail therefore has a different structure from the order −2 Burns mass tail. For the bolt-regular response (1) the Ricci defect is square integrable and produces no a⁴ log term. This restricted calculation does not claim a no-log theorem in all angular sectors and does not determine the complete a⁴ coefficient on a general P-critical orbifold.

The substantive target is now the complete finite coefficient, including both the positive obstruction square and the angular/exterior transgression. No universal sign follows from the existence of a zero-P ALE filler alone.

## Primary references

- O. Biquard, *Désingularisation de métriques d'Einstein. I*, Sections 1–3, https://arxiv.org/pdf/1105.4904 . The classical Jacobi fields and curvature obstruction are used; no new general Einstein desingularization theorem is claimed.
- E. Wright, *Quotients of gravitational instantons*, Corollary C, https://arxiv.org/pdf/1102.2442 .
- H.-J. Hein and C. LeBrun, *Mass in Kähler geometry*, Theorems 4.2–4.3 in the arXiv version, https://arxiv.org/pdf/1507.08885 .

The explicit rational response, Ricci coefficients, and the harmonic-moment Bochner integral are verified by `check_eh_inner.py`. The exterior gluing comparison is not verified by that algebra script and remains unproved.
