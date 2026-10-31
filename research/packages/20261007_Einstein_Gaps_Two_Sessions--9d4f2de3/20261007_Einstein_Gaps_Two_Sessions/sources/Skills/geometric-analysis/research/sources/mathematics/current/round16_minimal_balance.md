# Minimal surfaces give isotropic integral shear balance

## 1. A distinction not visible in the rank-two calculation

Round 15 characterized balance of two integral shear forms by a
holomorphic map to a flat two-torus. Their cup product cannot vanish.
For three forms this restriction fails: there are three linearly
independent integral classes whose pairwise cup products all vanish,
but whose stresses cancel exactly.

The example comes from the classical Schwarz P minimal surface, not
from a newly claimed construction of a minimal surface. Its application
here supplies a different set of admissible closed shear data and
determines the sign of a fiber-moduli second variation.

For a hyperbolic metric \(h\) on a closed surface \(F\), and fixed
classes \(b_j\in H^1(F;2\pi\mathbb Z)\), let \(\beta_j(h)\) be their
harmonic representatives and put
\[
 \mathcal H(h)=\sum_{j=1}^3\|\beta_j(h)\|_2^2,\qquad
 S(h)=\sum_{j=1}^3
       \left(\beta_j\otimes\beta_j-\tfrac12|\beta_j|_h^2h\right).
 \tag{1}
\]
The exact variation from [Round 15](round15_shear_balance.md) is
\[
 D\mathcal H_h[Q]=-\int_F\langle S(h),Q\rangle_h\,d\mu_h
 \tag{2}
\]
for every hyperbolic TT variation \(Q\). Thus \(S=0\) is a
critical point, but need not be a minimum.

**Proposition 1.** There are a genus-three surface \(F\), a
curvature-\(-3\) metric \(h_0\), and three independent integral classes
\(b_1,b_2,b_3\) such that
\[
 \int_F b_i\wedge b_j=0\quad\hbox{for every }i,j,\qquad
 S(h_0)=0.
 \tag{3}
\]
Their span is a Lagrangian subspace of \(H^1(F;\mathbb R)\).
Moreover, \(\mathcal H\) has a strictly negative second variation
along a smooth path in the marked hyperbolic metric space through
\(h_0\). Consequently exact cancellation is not the same as
minimization of the shear potential.

## 2. From a minimal torus immersion to harmonic integral data

Let
\[
 U:F\longrightarrow \mathbb T^3
        =\mathbb R^3/(2\pi\mathbb Z)^3
 \tag{4}
\]
be the Schwarz P embedding, after an ambient rescaling. It is a
closed orientable, separating, genus-three minimal surface. These
classical properties are described in Ros,
[*Index one minimal surfaces in positively curved 3-manifolds*,
Section 4 and page 538](https://wpd.ugr.es/~aros/wp-content/uploads/2025/02/Ros-JDG.pdf).
No assertion about its index is needed below.

Write \(I=U^*g_{\rm flat}\), and let \(h_0\) be the curvature-\(-3\)
metric in the conformal class of \(I\). Set
\[
 \beta_j=U^*(dx_j),\qquad b_j=[\beta_j].
 \tag{5}
\]
The forms have periods in \(2\pi\mathbb Z\). Minimality says the
local coordinate functions of \(U\) are harmonic for \(I\);
harmonicity of one-forms on a surface is conformally invariant.
Hence (5) are precisely the harmonic representatives for \(h_0\).
Since \(U\) is conformal for \(h_0\),
\[
 \sum_j\beta_j\otimes\beta_j=I=e^{2u}h_0,
 \tag{6}
\]
which proves \(S(h_0)=0\).

The surface is the oriented boundary of one component of
\(\mathbb T^3\setminus U(F)\). Each \(dx_i\wedge dx_j\) is closed, so
Stokes' theorem gives
\[
 \int_F\beta_i\wedge\beta_j=0.
 \tag{7}
\]
The three classes are independent over \(\mathbb R\). Otherwise a
nonzero constant vector \(a\in\mathbb R^3\) would give an exact
harmonic form \(\sum a_j\beta_j\), hence the zero form. Every tangent
plane of the immersion would then equal \(a^\perp\). Its second
fundamental form would vanish identically, contradicting Gauss–Bonnet
on a genus-three surface. Since \(H^1(F;\mathbb R)\) has dimension six,
(7) makes their three-dimensional span Lagrangian.

In particular no choice of a pair from these three classes can
balance by itself: each pair has degree zero in the Round-15 torus
criterion. The cancellation uses all three components.

## 3. The negative second variation is a global argument

More generally let \(U:F_p\to\mathbb T^3\) be any closed orientable
minimal immersion of genus \(p\geq2\), without branch points.
Let \(\nu\) be a global unit normal and let \(L\) be its shape operator.
For small real \(t\), the parallel immersion
\[
 U_t(x)=U(x)+t\nu(x)\pmod{2\pi\mathbb Z^3}
 \tag{8}
\]
is smooth, immersed, and homotopic to \(U\). Choose a smooth
curvature-\(-3\) metric \(h_t\) conformal to \(I_t=U_t^*g_{\rm flat}\).
Smooth uniformization supplies this path; there is no need to keep
the original induced area form.

The eigenvalues of \(L\) are \(\lambda,-\lambda\), and
\(K_I=-\lambda^2\). Before any focal point,
\[
 dA_t=\det(I-tL)\,dA=(1+t^2K_I)\,dA,
 \qquad
 \operatorname{Area}(U_t)
       =\operatorname{Area}(U)+2\pi\chi(F_p)t^2.
 \tag{9}
\]
This is an exact formula for the parallel immersions, not an
asymptotic from numerical sampling.

Because \(U_t\) is homotopic to \(U\), its three coordinate
differentials represent the same classes \(b_j\). Harmonic
representatives minimize the energy within each class. Their summed
energy therefore satisfies
\[
 \begin{split}
 \mathcal H(h_t)
 &\leq\int_{F_p}|dU_t|_{h_t}^2\,d\mu_{h_t}\\
 &=2\operatorname{Area}(U_t)
  =\mathcal H(h_0)+4\pi\chi(F_p)t^2.
 \end{split}
 \tag{10}
\]
Equality holds at \(t=0\), since \(U\) is conformal and harmonic.
It follows that
\[
 \boxed{\frac{d^2}{dt^2}\mathcal H(h_t)\bigg|_{0}
       \leq 8\pi\chi(F_p)=-16\pi(p-1)<0.}
 \tag{11}
\]
In particular this path has a nonzero tangent in Teichmüller space:
at a critical point a path with zero Teichmüller tangent would have
zero second variation. No volume-preserving condition is imposed
on (8). Volume-preserving stability of a minimal surface would not
contradict this variation.

Energy/area comparisons and the role of conformal variations are
classical; see Ejiri–Micallef,
[*Comparison between Second Variation of Area and Second Variation
of Energy of a Minimal Surface*, Section 2](https://arxiv.org/pdf/0708.2188).
Here the harmonic minimization and the exact parallel-surface formula
give (10) directly.

The rank-two branched torus example from Round 15 instead satisfies
an energy-minus-degree identity with a nonnegative square and hence
has nonnegative Hessian at balance. There is no conflict: a branched
map to a two-torus is not an unbranched minimal immersion into a
three-torus. Equation (11) proves a negative direction, not a count
of all positive and negative eigenvalues.

## 4. Realization by a fixed closed three-shear construction

Take a compact hyperbolic surface \(B_{r,6}\), \(r\geq0\), with six
geodesic boundary circles, and the fixed genus-three \(F\) above.
Pair the boundary components into three self-edges. On edge \(j\)
use the integral circle-valued map supplied by \(\beta_j\), with
identity fiber mapping class. This is a particular fixed smooth
manifold in the [Round-11 construction](round11_closed_gluing.md).
Its Euler characteristic is
\[
 \chi(M)=\chi(B_{r,6})\chi(F)=(-2r-4)(-4)=8r+16.
 \tag{12}
\]

Give the three collars identical radius and smooth connection
profiles. Their common capacity is
\[
 q=\int a^3(z')^2\,dt>0.
 \tag{13}
\]
The optimized full-collar profiles of
[Round 14](round14_global.md) give a fixed-topology family
\(G_c\) with
\[
 \|\operatorname{Ric}_{G_c}+3G_c\|_{\infty,\mathrm{op}}=O(c^2),
 \qquad \operatorname{Vol}(G_c)=V_*=\frac{4\pi^2}{9}\chi(M).
 \tag{14}
\]
The integer classes and gluing maps do not change with \(c\).
For local variations of \(h\), changes of its harmonic representatives
are exact and are absorbed by boundary isotopies, as in Round 15.

Including every exterior product contribution, the normalized scalar
functional is exactly
\[
 \mathscr S(G_{c,h})
       =-12\sqrt{V_*}-\frac{\pi q}{\sqrt{V_*}}\mathcal H(h).
 \tag{15}
\]
At \(h=h_0\) all simultaneous fiber TT forces cancel. This cancellation
holds for each \(c\), not just in a limiting coefficient. Along (8),
\[
 \mathscr S(G_{c,h_t})\geq\mathscr S(G_{c,h_0})
       +\frac{8\pi^2q(p-1)}{\sqrt{V_*}}\,t^2.
 \tag{16}
\]
Thus the balanced point has an increasing scalar-functional direction
within this fixed closed family, whereas the rank-two balanced
potential had the opposite Hessian sign.

Each separate nonzero shear retains its waist force. Neither (3)
nor (16) solves the waist equations or the nonsymmetric exterior
problem. The example removes a proposed obstruction based only on
pairwise cup products or on unavoidable nonzero fiber stress; it is
not an Einstein existence or nonexistence theorem.

## 5. What is new here and what is inherited

The minimal surface, conformal harmonic-map mechanism, parallel-surface
area formula, and energy comparison are established mathematics.
The present deduction supplies integral, pairwise isotropic rank-three
data to the fixed closed near-Einstein construction, and carries
their nonminimizing equilibrium into its exact scalar functional.
It expands the available matching configurations; no literature
priority for this application has been established.

The accompanying check verifies the local Weierstrass stress identity,
harmonicity, the parallel-area polynomial, and the four-dimensional
normalizations. Existence, separation, and genus of the Schwarz P
surface are the stated classical input, not outcomes of that program.
