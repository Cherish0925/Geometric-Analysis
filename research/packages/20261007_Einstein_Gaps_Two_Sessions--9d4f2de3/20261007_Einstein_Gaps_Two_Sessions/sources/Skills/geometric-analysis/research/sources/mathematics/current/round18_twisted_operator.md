# Complete Einstein channels on finite-monodromy surface bundles

## 1. The geometric problem and the result

Let \(\widetilde B,F\) be connected closed oriented surfaces of curvature
\(-3\). Let a finite group \(G\) act on both by orientation-preserving
isometries, freely on \(\widetilde B\), and effectively on \(F\). The diagonal
action is free even when the fiber action has fixed points. Thus
\[
 M=(\widetilde B\times F)/G\longrightarrow B=\widetilde B/G,
 \qquad g_0=g_{\widetilde B}+g_F,\qquad \operatorname{Ric}_{g_0}=-3g_0       \tag{1}
\]
is an actual closed surface bundle with finite, possibly nontrivial,
monodromy. The notation for the metric in (1) means its descent to the
quotient. These exact Einstein metrics are classical; their existence is
not a new near-Einstein construction.

The result here is a full retained-operator description on this geometry.
Every symmetric two-tensor, not only a symmetry-preserving ansatz, is
included. The exceptional channels are Laplacians with explicit monodromy
and orbifold conditions; their orthogonal complement has a uniform inverse
even under small arbitrary metric perturbations. At each fixed quotient,
all infinitesimal Einstein deformations integrate, giving a complete local
nonlinear description and a residual-to-distance estimate. The latter
estimate is not asserted uniformly over degeneration.

The main conclusions are:

1. The low channels are flat Teichmüller coefficient bundles over \(B\)
   and the orbifold \(F/G\), not globally constant scalar coefficients.
2. The remaining full tensor operator has gap \(3\); its compressed
   \(L^2\)-to-\(H^2\) inverse remains uniformly bounded after sufficiently
   small \(C^2\) perturbations, independently of collapse and cover degree.
3. Finite monodromy can remove exact Teichmüller zero modes without removing
   arbitrarily small positive TT modes. The distinction is demonstrated on
   a specified genus-three hyperelliptic bundle.
4. Near a fixed quotient metric, every normalized Einstein metric is,
   modulo a small diffeomorphism, a quotient of deformed hyperbolic factors
   with the same actions. This is a local statement about all metrics on
   the quotient, not an assumption that a proposed correction preserves
   the displayed product structure.

The spectral inputs are the classical product identities, as in
Kröncke, [*On infinitesimal Einstein deformations*, Proposition 4.1 and
§4](https://arxiv.org/pdf/1508.00721). Their complete surface specialization
and uniform perturbation proof are in
[Round 17](round17_product_operator.md), §§2–6. The local deformation
argument is the integrable-kernel slice argument associated with Koiso's
[Einstein deformation theory](https://link.springer.com/article/10.1007/BF01393826);
we give the required integration and implicit-function argument below.
The contribution to the present project is the actual equivariant
transmission problem, its exact retained channels, and its degeneration
and nonlinear consequences, rather than a new classification of products.

## 2. Descent preserves the complete operator, not just selected modes

Use \(\delta h=-\nabla^ih_{ij}\),
\(\mathcal B h=\delta h+\frac12d\operatorname{tr}h\), and nonnegative
Laplacians. The full gauged normalized Einstein operator is
\[
 P_0=D(\operatorname{Ric}+3g)_{g_0}+\delta^*\mathcal B
     =\tfrac12\Delta_L+3
     =\tfrac12\nabla^*\nabla-\mathring R .                    \tag{2}
\]
Here \(\mathring Rg=\operatorname{Ric}\). Put
\[
 T_\Sigma=\{q\in C^\infty(S^2T^*\Sigma):\operatorname{tr}q=0,\ \delta q=0\}.
\]
This real vector space has dimension \(6\operatorname{genus}(\Sigma)-6\).
For the trace-free conformal-Killing operator
\(D_\Sigma\alpha=\delta^*\alpha+\frac12(\delta\alpha)g_\Sigma\), the surface
identities are
\[
 P_\Sigma|_{S^2_0}=D_\Sigma\delta,\qquad
 \delta D_\Sigma=\tfrac12\Delta_H+3,\qquad
 P_\Sigma(ug_\Sigma)=(\tfrac12\Delta u+3u)g_\Sigma.             \tag{3}
\]
All maps in (2)–(3) commute with isometries. So do the surface orthogonal
projections onto trace, \(T_\Sigma\), and \(\operatorname{ran}D_\Sigma\).

Lifting a tensor from \(M\) identifies it with a \(G\)-invariant tensor on
the product. This covers every tensor on \(M\). For every integer \(j\ge0\),
\[
 \|\nabla^jh\|_{L^2(\widetilde B\times F)}^2
      =|G|\|\nabla^jh\|_{L^2(M)}^2,                         \tag{4}
\]
while pointwise derivative norms are unchanged. The Reynolds projection
\(|G|^{-1}\sum_{\gamma\in G}\gamma^*\) is orthogonal and commutes with
\(P_0\) and all these factor projections.

For a scalar eigenvalue \(\lambda\), let \(E_\Sigma(\lambda)\) be the
scalar eigenspace, with its actual \(G\) representation. Write
\(H_\Sigma(\mu)\) for Hodge one-form eigenspaces, including harmonic forms
when \(\mu=0\). A superscript \(G\) in the following table means the
invariant part of the tensor-product representation, not a product of
separately invariant eigenspaces.

| Complete quotient sector | Eigenvalue of \(P_0\) |
| --- | --- |
| \((T_{\widetilde B}\otimes E_F(\nu))^G\) | \(\nu/2\) |
| \((E_{\widetilde B}(\lambda)\otimes T_F)^G\) | \(\lambda/2\) |
| \((E_{\widetilde B}(\lambda)\otimes E_F(\nu))^Gg_{\widetilde B}\), and the corresponding \(g_F\) copy | \(3+(\lambda+\nu)/2\) |
| \((D_{\widetilde B}H_{\widetilde B}(\mu)\otimes E_F(\nu))^G\) | \(3+(\mu+\nu)/2\) |
| \((E_{\widetilde B}(\lambda)\otimes D_FH_F(\xi))^G\) | \(3+(\lambda+\xi)/2\) |
| \((H_{\widetilde B}(\mu)\odot H_F(\xi))^G\) | \(3+(\mu+\xi)/2\) |

For orthonormal identifications in the fourth and fifth rows, use
\(D(\frac12\Delta_H+3)^{-1/2}\); for mixed tensors use
\(\alpha\odot\gamma=(\alpha\otimes\gamma+\gamma\otimes\alpha)/\sqrt2\).
The direct sum over the displayed eigenvalues is complete. Indeed the
product tensor bundle splits into the two pure blocks and the mixed block;
(3) splits each pure block. Restriction of this commuting orthogonal
decomposition to invariants preserves completeness.

In particular, mixed harmonic one-forms have eigenvalue \(3\), not zero.
The relative scaling mode also has eigenvalue \(3\). There are no missing
gauge zero modes: on the quotient the gauge operator is
\[
 \mathcal B\delta^*=\tfrac12\Delta_H+3\ge3.                 \tag{5}
\]

## 3. The retained operator as an actual transmission problem

The full low subspace is
\[
 \mathcal L_G=
 (T_{\widetilde B}\widehat\otimes L^2(F))^G
 \ \widehat\oplus\
 (L^2(\widetilde B)\widehat\otimes T_F)^G .                 \tag{6}
\]
Every tensor in (6) is TT. This is generally infinite dimensional, even
after the true kernel has been removed.

An isometry acts on \(T_\Sigma\) orthogonally for its \(L^2\) inner product.
Fix the coefficient representations by requiring that a coefficient map
\(u\) satisfy \(u(\gamma x)=\rho(\gamma)u(x)\), so that its associated
two-tensor is diagonally invariant. Using inverse pullbacks instead of
pushforwards gives precisely this convention. Define
\[
 \mathcal E_F=\widetilde B\times_G T_F\longrightarrow B,
 \qquad
 \mathcal E_B=(F\times T_{\widetilde B})/G\longrightarrow\mathcal O=F/G.
                                                               \tag{7}
\]
The first is an ordinary orthogonal flat bundle. The second is a flat
**orbifold** bundle if the fiber action has fixed points. Its sections are
equivariant smooth maps on \(F\); the underlying topological quotient
surface does not by itself specify their domain.

With the coefficient inner products induced by the factor \(L^2\) norms,
equations (4) and (6) identify the low operator exactly as
\[
 \boxed{P_0|_{\mathcal L_G}
   =\tfrac12\nabla^*\nabla_{\mathcal E_B}
        \oplus\tfrac12\nabla^*\nabla_{\mathcal E_F}.}       \tag{8}
\]
There is no curvature potential in these flat coefficient equations.

For example, cut the ordinary base along a system of loops. Across paired
faces, the coefficients and conormals satisfy
\[
 u_+=\rho(\gamma)u_-,\qquad
 \nabla_{n_+}u_+=-\rho(\gamma)\nabla_{n_-}u_- .             \tag{9}
\]
These are the full value and flux conditions; one cannot solve separate
Dirichlet problems and omit their matching. The minus sign uses the two
outward normals. At an orbifold point with stabilizer \(G_y\), the lift
obeys the full equivariance condition in a smooth disk. In particular
\(u(y)\in(T_{\widetilde B})^{G_y}\), and all jets obey the corresponding
equivariance. For an order-two rotation and a sign coefficient, the lift
is an odd function; its value vanishes at the fixed point, but merely
imposing value zero would not impose the correct smooth domain.

Integration by parts with (9), or equivalently on the finite cover, gives
\(\ker\nabla^*\nabla=\{\text{parallel sections}\}\). Thus
\[
 \boxed{\ker P_0=K=T_{\widetilde B}^{G}\oplus T_F^{G}.}     \tag{10}
\]
Let \(\lambda_*^B,\lambda_*^F\) denote the smallest positive eigenvalues
of the two coefficient Laplacians in (8). The eigenvalue \(3\) occurs in
the invariant constant trace sector. Hence the full optimal gap after
removing only \(K\) is
\[
 \gamma_G=\min\{3,\lambda_*^B/2,\lambda_*^F/2\}.           \tag{11}
\]
For a zero-rank coefficient bundle its entry is omitted. For each fixed
quotient this is positive. The low inverse is exactly twice the flat or
orbifold Laplacian inverse with parallel sections removed; the high inverse
is given by the positive shifted sectors in the table. This solves the
complete linear transmission problem, including its global constraints.

## 4. Uniform high-complement control survives the quotient and perturbation

Write \(\Pi\) for the projection onto (6), \(Q=I-\Pi\), and
\(\mathcal H_G=\operatorname{ran}Q\). The table gives
\[
 \langle P_0h,h\rangle\ge3\|h\|_2^2\quad(h\in\mathcal H_G),
 \qquad
 \|(P_0|_{\mathcal H_G})^{-1}f\|_{H^2}\le C\|f\|_2.       \tag{12}
\]
The constant is independent of injectivity radius, genera, diameter and
\(|G|\). For clarity, the uniform elliptic input is a global covariant
estimate, not an injectivity-radius assumption:
\[
 \|h\|_{H^2}\le C(\|P_0h\|_2+\|h\|_2).                  \tag{13}
\]
It follows by integration by parts from bounded parallel product
curvature, \(\nabla^*\nabla h=2P_0h+2\mathring Rh\), and one covariant
derivative commutation. Equation (4) cancels the cover degree on both
sides. Since \(\Pi\) commutes with \(P_0\), (13) also gives uniform
\(H^2\) bounds for \(\Pi,Q\).

Let \(g\) now be **any** smooth quotient metric with
\(\|g-g_0\|_{C^2(g_0)}\le\epsilon\), not necessarily locally product or
Einstein. Set \(P_g=\frac12\Delta_{L,g}+3\). For
\(C_0=g_0^{-1}g\), the unitary comparison is
\[
 (Uh)(X,Y)=(\det C_0)^{-1/4}
                 h(C_0^{1/2}X,C_0^{1/2}Y),\qquad
 \widetilde P_g=U^{-1}P_gU .                              \tag{14}
\]
On the cover this map is \(G\)-equivariant, because both metrics are.
The tensor connection and curvature formulas give
\[
 \|\widetilde P_g-P_0\|_{H^2\to L^2}\le C\epsilon,
\quad
 |\langle(\widetilde P_g-P_0)h,h\rangle|
      \le C\epsilon(\|\nabla h\|_2^2+\|h\|_2^2).         \tag{15}
\]
No derivatives of \(g\) beyond order two occur. The constants again
descend by (4). Since
\(\|\nabla h\|_2^2\le2\langle P_0h,h\rangle+6\|h\|_2^2\),
(12) and (15), with a universal sufficiently small \(\epsilon\), imply
\[
 \boxed{
 \langle Q\widetilde P_gQh,h\rangle\ge\tfrac32\|h\|_2^2,
 \qquad
 \|(Q\widetilde P_gQ)^{-1}f\|_{H^2}\le C\|f\|_2.}        \tag{16}
\]
The \(L^2\)-operator norm is at most \(2/3\). Surjectivity and the
\(H^2\) bound also follow by a Neumann series about the high inverse
in (12). It preserves invariants, so it is an actual operator on \(M\).

The low equation is not removed by this argument. For blocks
\(A=\Pi\widetilde P_g\Pi\), \(B=\Pi\widetilde P_gQ\),
\(C=Q\widetilde P_g\Pi\), \(D=Q\widetilde P_gQ\), it is exactly
\[
 (A-BD^{-1}C)u=f_L-BD^{-1}f_H,\qquad
 v=D^{-1}(f_H-Cu).                                        \tag{17}
\]
Here \(u\) is a section of both bundles in (7), with the actual matching
conditions (9), and \(v\) is the full high tensor response. The feedback
\(BD^{-1}C:H^2\cap\mathcal L_G\to L^2\cap\mathcal L_G\)
is \(O(\epsilon^2)\). It must nevertheless be retained if a twisted
Laplacian eigenvalue is of that order. Neither (16) nor (17) asserts an
injectivity-independent maximum-norm inverse.

## 5. An explicit nonproduct quotient and its exact channels

Choose a genus-two base \(B\) and a nonzero character
\(\chi:\pi_1(B)\to\mathbb Z_2\). Its connected unramified double cover
\(\widetilde B\) has genus three; let \(\tau\) be the deck involution.
Choose a genus-three hyperelliptic curve
\[
 F:\quad y^2=\prod_{j=1}^{8}(x-a_j),\qquad a_j\ne a_k\ (j\ne k),
 \qquad \iota(x,y)=(x,-y),                                \tag{18}
\]
with its unique curvature \(-3\) metric. Then
\[
 M_\chi=(\widetilde B\times F)/\langle(\tau,\iota)\rangle   \tag{19}
\]
is smooth, and has monodromy \(\iota^{\chi(\gamma)}\). The eight fixed
points of \(\iota\) do not create singularities in (19), because \(\tau\)
has no fixed points.

### The fiber representation is genuinely nontrivial

For a genus \(g\ge2\) hyperelliptic curve of degree \(2g+2\), holomorphic
quadratic differentials split explicitly as
\[
 \begin{array}{c|c|c}
 \iota\text{-parity}&\text{basis}&\text{complex dimension}\\\hline
 +&x^j\,dx^2/y^2,\quad 0\le j\le2g-2&2g-1\\
 -&x^j\,dx^2/y,\quad 0\le j\le g-3&g-2.
 \end{array}                                             \tag{20}
\]
At a branch point, set \(x-a=w^2\); the two forms behave as \(dw^2\)
and \(w\,dw^2\). At either point at infinity their orders are respectively
\(2g-2-j\) and \(g-3-j\). Thus all displayed forms are regular, are
independent, and exhaust dimension \(3g-3\). Taking real parts yields
\[
 \dim T_F^+=10,\qquad \dim T_F^-=2\qquad(g=3).             \tag{21}
\]
Using a genus-two hyperelliptic fiber would not demonstrate twisted
Teichmüller directions: its negative space in (20) is zero.

On the base cover, invariant TT tensors descend to the genus-two base.
Thus \(\dim T_{\widetilde B}^+=6\), and
\(\dim T_{\widetilde B}^-=6\). Write \(L_\chi\to B\) for the sign
flat line bundle. The two low operators in (8) become
\[
 \begin{split}
 &\tfrac12\Delta_B\text{ on ten trivial copies},\qquad
       \tfrac12\Delta_{L_\chi}\text{ on two sign copies};\\
 &\tfrac12\Delta_{F,+}\text{ on six even copies},\qquad
       \tfrac12\Delta_{F,-}\text{ on six odd copies}.
 \end{split}                                             \tag{22}
\]
The second line is equivalently over a sphere with eight cone points of
order two; \(\Delta_{F,\pm}\) denotes the Laplacian on smooth even or odd
lifts. The odd coefficients have no constants. Consequently
\[
 \dim K=10+6=16,
 \qquad\text{whereas the covering product has kernel dimension }24.
                                                               \tag{23}
\]

The topology confirms that this is not merely a product in disguise.
The involution acts by \(-1\) on \(H^1(F;\mathbb R)\), as seen from the
basis \(x^jdx/y\), \(0\le j\le2\). Finite-cover transfer gives
\[
 \chi(M_\chi)=8,\quad\tau(M_\chi)=0,\quad b_1=4,
 \quad b_2=14,\quad b_+=b_-=7.                            \tag{24}
\]
The signature is zero because it is zero on the degree-two product
cover. The quotient is aspherical. A product of two oriented surfaces
with Euler characteristic eight cannot have a torus factor; asphericity
excludes a sphere factor. Two factors of genera at least two would have
\(b_1\ge8\), contradicting (24). Thus (19) is not diffeomorphic to any
product of closed oriented surfaces.

## 6. Removing constants does not remove degeneration

For a fixed \(B\), the nontrivial line bundle \(L_\chi\) has no nonzero
parallel section, and hence \(\lambda_0(\Delta_{L_\chi})>0\). There is
nevertheless no uniform positive lower bound as the hyperbolic metric
degenerates.

Split the genus-two base along a separating curve into two punctured
tori. Choose \(\chi\) nontrivial on the first and trivial on the second.
It is trivial on the separating curve. Pinch that curve; an embedded
collar has metric
\[
 dt^2+a(t)^2d\phi^2,\quad a(t)=c\cosh(kt),\quad k=\sqrt3,
 \quad\phi\in\mathbb R/2\pi\mathbb Z,
 \quad R_c\asymp k^{-1}\log(1/c).                         \tag{25}
\]
The line bundle is trivial on the collar and the second thick piece.
Take a unit constant section on that piece, zero on the first, and the
energy-minimizing radial interpolation across the collar. Its energy is
\[
 \int|\nabla u|^2
       =\frac{2\pi}{\int_{-R_c}^{R_c}a(t)^{-1}dt}
       =2kc+o(c),\qquad \|u\|_2^2\ge c_0>0.              \tag{26}
\]
The piecewise smooth function is an admissible \(H^1\) section; smooth
approximations give the same bound. No subtraction of a constant section
is needed or possible in the nontrivial bundle. The Rayleigh principle
therefore gives
\[
 \boxed{\lambda_0(\Delta_{L_\chi})\le Cc\longrightarrow0.} \tag{27}
\]
By (22), this produces at least two actual positive TT eigenvalues of
the full four-dimensional operator tending to zero, even though the
corresponding constant fiber deformations did not descend. Twisting has
removed their kernel, not their near-kernel.

There is a complementary local effect when the character around a
pinched curve is nontrivial. Then
\(u(t,\phi+2\pi)=-u(t,\phi)\), so the angular frequencies are
\(n+\frac12\). For sections supported in a collar region where
\(a\le a_0\), angular Poincaré gives
\[
 \langle\tfrac12\Delta_{L_\chi}u,u\rangle
             \ge\frac1{8a_0^2}\|u\|_2^2.                 \tag{28}
\]
Thus sign holonomy eliminates the angular zero mode on that neck.
It is not a global spectral-gap theorem.

Both behaviors follow from the exact radial conjugation. For angular
frequency \(n+\theta\), \(\theta=0\) or \(1/2\), multiplication by
\(\sqrt a\) transforms the low operator into
\[
 \frac12\left[-\partial_t^2+\frac34+
       \frac34\operatorname{sech}^2(\sqrt3t)
                 +\frac{(n+\theta)^2}{a(t)^2}\right].     \tag{29}
\]
Where the collar holonomy is trivial, compactly supported radial sine
tests on \([T,R_c]\) give arbitrarily many low-channel eigenvalues below
any fixed \(\sigma>3/8\), as in Round 17. They remain legitimate
twisted-bundle test sections: the bundle is trivial on their support and
they vanish at the support boundary. If genus varies, the invariant
Teichmüller kernel can also grow without bound. Neither nontrivial finite
monodromy nor removing the kernel justifies a fixed-dimensional reduction
over all degenerating bundles.

## 7. Full nonlinear local closure at each fixed quotient

**Theorem.** Fix the metric \(g_0\) in (1) and \(0<\alpha<1\). There is
a \(C^{2,\alpha}\) neighborhood in which, modulo sufficiently small
diffeomorphisms, all metrics satisfying \(\operatorname{Ric}=-3g\) are
quotients of \(G\)-invariant hyperbolic deformations of the two factors.
The Einstein family in a local Bianchi slice is smooth of dimension
\(\dim T_{\widetilde B}^G+\dim T_F^G\). A residual-to-distance estimate
holds in a fixed Bianchi slice:
\[
 \inf_{\widehat g\in\mathscr E_0}
       \|g-\widehat g\|_{C^{2,\alpha}(g_0)}
       \le C(g_0,\alpha)
       \|\operatorname{Ric}_g+3g\|_{C^{0,\alpha}(g_0)}.    \tag{30}
\]
Here \(\mathscr E_0\) is that local Einstein family placed in the slice,
and the neighborhood and constant may depend on the fixed geometry.
The statement allows all tensor perturbations of the quotient metric.

**Proof: integration of the entire kernel.** A \(G\)-invariant TT tensor
on a surface corresponds to a \(G\)-invariant Beltrami differential.
Small linear combinations define nearby \(G\)-invariant complex
structures on the same smooth surface. Uniformizing each to curvature
\(-3\) gives a smooth family of hyperbolic metrics. Uniqueness of the
uniformized metric in its conformal class makes every fixed element of
\(G\) an isometry throughout the family. After the usual surface slice
adjustment, its derivative is the prescribed TT tensor. Taking the two
families together and then the quotient integrates every vector in (10),
simultaneously, in a family whose parameter dimension is \(\dim K\).
This argument uses the actual fixed actions, not only a numerical count
of invariant tangent vectors.

**Proof: there are no other local branches.** On the fixed smooth quotient
use the gauged map
\[
 \Phi(g)=\operatorname{Ric}_g+3g+\delta_g^*\mathcal B_{g_0}g,
 \qquad D\Phi_{g_0}=P_0.                                 \tag{31}
\]
The projection onto \(K\) is defined in \(L^2(g_0)\). Ellipticity and the
positive gap (11) give an isomorphism
\[
 P_0:K^\perp\cap C^{2,\alpha}
                   \longrightarrow K^\perp\cap C^{0,\alpha}            \tag{32}
\]
for this fixed metric. The implicit-function theorem uniquely solves
\((I-\Pi_K)\Phi(g_0+k+w)=0\) for \(w=w(k)\in K^\perp\) near zero.

The actual Einstein family just constructed can be put in the slice
\(\mathcal B_{g_0}g=0\) by small diffeomorphisms. Its derivative is \(K\),
because the kernel is TT and the gauge operator (5) is invertible. Its
projection onto the coordinate \(k\) is a local diffeomorphism. It must
therefore fill the whole graph \(g_0+k+w(k)\). Consequently its remaining
finite-dimensional obstruction map vanishes identically. There are no
additional nearby gauged solutions.

For completeness, gauged zeros are Einstein: applying \(\mathcal B_g\)
to (31), the contracted Bianchi identity gives
\(\mathcal B_g\delta_g^*\mathcal B_{g_0}g=0\). The one-form operator is
\(\frac12(\nabla_g^*\nabla_g-\operatorname{Ric}_g)\); it is positive
when \(\operatorname{Ric}_g<0\), as holds sufficiently close to \(g_0\).
Thus \(\mathcal B_{g_0}g=0\) and \(\operatorname{Ric}_g+3g=0\).
Every nearby Einstein metric can also be placed in this slice, so the
conclusion concerns all nearby Einstein metrics modulo diffeomorphism.

**Proof of (30).** Write an arbitrary nearby slice metric as
\(g=g_0+k+w\) and compare it to \(\widehat g=g_0+k+w(k)\). The derivative
of the complementary equation with respect to \(w\) remains an
isomorphism near the fixed origin. Its integral along the short segment
between these two tensors is also an isomorphism with a common local
bound, by a Neumann-series estimate about (32). Hence
\[
 \|w-w(k)\|_{2,\alpha}
       \le C\|(I-\Pi_K)\Phi(g)\|_{0,\alpha}.
\]
On the slice \(\Phi(g)=\operatorname{Ric}_g+3g\), proving (30).

One may also formulate this modulo diffeomorphisms by first taking the
local slice representative. This proof is the classical integrable-kernel
mechanism, with the complete kernel and its integration explicitly
established for the finite-monodromy geometry. It is not a claim that
all negative Einstein kernels in other geometries are integrable.

Equation (27) forces the \(L^2\) inverse norm of the transverse linear
problem to diverge at least as the inverse positive eigenvalue. The
theorem proves (30) only for each fixed metric; it supplies no
thin-parameter-uniform neighborhood or Hölder estimate. The uniform high
estimate (16) does not control these low directions or the nonlinear
Hölder constants.

## 8. What this establishes for the construction program

This closes a genuine linear and local nonlinear test case beyond the
trivial product: nontrivial monodromy, a specified nonproduct closed
four-manifold, complete transmission conditions, all tensor sectors, and
all nearby normalized Einstein metrics. It also isolates two independent
effects of twisting: elimination of some parallel deformation parameters
and holonomy-dependent neck coercivity. The former does not imply the
latter uniformly, as (27) shows.

The finite-monodromy condition is essential to this proof. An infinite
Dehn twist cannot act isometrically on a fixed closed hyperbolic fiber,
whose isometry group is finite. On a slowly varying \(E_D\) geometry,
fiber TT projections vary with the base; their covariant derivatives,
commutators with the Einstein operator, and actual seam matching must be
estimated. Equations (8), (12), and (17) do not by themselves provide
those estimates. They specify the full operator that a future adiabatic
extension must recover, including the low PDE and its high feedback.

The quotient in (19) already carries an exact negative Einstein metric,
so it is not a counterexample to Yau 26. Its role is a solved nontrivial
control geometry: a complete perturbative argument can succeed after
the monodromy and integrable kernel are handled, while thin parameters
still obstruct uniform inversion. This is materially different from
assuming an inverse for a new shear construction.

## 9. Reproduction

Run
```bash
/data/qiushi/qiushi_engine_v09/.venv/bin/python round18_twisted_operator_check.py
```
The independent script checks the representation projection, the full
sector shifts, local parity domains, hyperelliptic differential orders and
dimensions, the example's topology, cover-normalization cancellation,
the exact collar conjugation and capacity asymptotics, and the Schur
feedback identity with a nonzero-coupling negative control. These finite
checks do not substitute for the global decomposition, hyperbolic
uniformization, or the nonlinear implicit-function argument above.
