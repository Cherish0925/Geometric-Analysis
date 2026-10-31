# An explicit almost-kernel of the full gauged Einstein operator

21 September 2026.

## 1. Statement and operator

Use the fixed closed product-block metrics \(G_\ell\) of Round 11,
with \(k=\sqrt3\),

\[
 a_\ell(t)=c_\ell\cosh(kt),\quad c_\ell=\ell/(2\pi),\qquad
 L_\ell=\frac1{2k}\operatorname{arsinh}
                  \bigl(1/\sinh(k\ell/2)\bigr).
\]

Choose one edge collar. The smooth profile \(\zeta\) in that
construction is constant one on a neighborhood of one. Fix
\(0<\vartheta<1\) such that
\(\zeta=1\) on \([1-\vartheta,1]\). The fiber metric has consequently
finished its change before a collar of length proportional to \(L_\ell\)
about the central throat. The connection changes only on \([0,1]\).

Use the Bianchi convention

\[
 \mathcal B_g h=\delta_g h+\tfrac12d\operatorname{tr}_g h,
 \quad (\delta h)_j=-\nabla^i h_{ij},\quad
 (\delta^*v)_{ij}=\tfrac12(\nabla_i v_j+\nabla_j v_i).
\]

The full gauged linearization, acting on all symmetric tensors, is

\[
 P_g h=D(\operatorname{Ric}+3g)_g[h]+\delta_g^*\mathcal B_g h
       =\tfrac12\Delta_{L,g}h+3h. \tag{1}
\]

Here \(\Delta_L=\nabla^*\nabla+\operatorname{Ric}\circ(\cdot)
+(\cdot)\circ\operatorname{Ric}-2\mathring R\). This fixes curvature
signs through the standard Ricci variation identity in (1).

**Theorem.** There are smooth tensors \(H_\ell\), supported in that
edge collar and extended by zero to the fixed closed manifold, and
constants independent of small \(\ell\), such that

\[
 \begin{aligned}
 1&\le\|H_\ell\|_{C^2(G_\ell)}\le C,\\
 \|P_{G_\ell}H_\ell\|_{C^0(G_\ell)}
       +\|\mathcal B_{G_\ell}H_\ell\|_{C^0(G_\ell)}
       &\le C\ell^\vartheta,\\
 \|H_\ell\|_{L^2(G_\ell)}&\asymp\ell^{1/2},\\
 \frac{\|P_{G_\ell}H_\ell\|_{L^2(G_\ell)}}
      {\|H_\ell\|_{L^2(G_\ell)}}
       &\le C\ell^{3\vartheta/4}.
 \end{aligned} \tag{2}
\]

The geometric \(C^2\) norm includes orders zero, one, and two. The
theorem does not require an inverse or any assertion about the kernel.
It produces an actual test tensor for the complete operator, rather
than an eigenvalue of a separately truncated scalar equation.
The same residual bound holds in every fixed geometric \(C^j\) norm,
with its own constant. In particular, for \(0<\alpha<1\),

\[
 \|P_{G_\ell}H_\ell\|_{C^{0,\alpha}}
   \le C_\alpha\ell^\vartheta,\qquad
 1\le\|H_\ell\|_{C^{2,\alpha}}\le C_\alpha. \tag{2a}
\]

Here a geometric Hölder norm compares tensors by parallel transport
along short minimizing paths. Uniform first-derivative bounds imply
the required Hölder estimates even when injectivity radius collapses.

## 2. The exact product-neck tensor

On

\[
 g_0=dt^2+a_\ell(t)^2d\phi^2+h_F,
 \qquad \operatorname{Ric}_{h_F}=-3h_F,
\]

put

\[
 f(t)=\operatorname{sech}^2(kt),\qquad
 H_0=f(t)\bigl(dt^2-a_\ell(t)^2d\phi^2\bigr). \tag{3}
\]

This is trace-free. Its only possible divergence component is

\[
 (\delta H_0)_t=-f'-2(a_\ell'/a_\ell)f=0.
\]

The variation is confined to the two-dimensional hyperbolic factor.
On a surface, \(\operatorname{Ric}=K g\), so

\[
 D(\operatorname{Ric}+3g)[H_0]=(DK[H_0])g.
\]

The scalar-curvature variation of a transverse trace-free tensor
on an Einstein surface vanishes; hence \(DK[H_0]=0\). Thus
\(P_{g_0}H_0=0\) exactly. The untouched hyperbolic fiber contributes
no mixed or fiber variation. The same statement holds with
\(d\phi\) replaced by a closed connection \(d\phi+\beta\): it is
locally a change of circle coordinate, and both tensors are globally
defined whether or not \(\beta\) has a real-valued primitive.

This is the infinitesimal hyperbolic-waist deformation in transverse
trace-free gauge. Its use here is not a claim that hyperbolic neck
deformations are a new phenomenon.

## 3. Locating a genuine product plateau

The Round-11 fiber path on \([-L_\ell,-1]\) has parameter

\[
 z(t)=\zeta\bigl((t+L_\ell)/(L_\ell-1)\bigr).
\]

Consequently the fiber is fixed whenever

\[
 t\ge-\vartheta L_\ell-(1-\vartheta).
\]

Set \(R_\ell=\vartheta(L_\ell-1)\). For small \(\ell\),
\(R_\ell>3\). The interval \([-R_\ell,R_\ell]\) lies entirely
inside the fixed-fiber region and away from the physical collar faces.
Its left edge is one full unit beyond the displayed start of the
plateau. The only departure from a locally exact product on this
support is the electric-shear strip \(0\le t\le1\).

Let \(\chi_\ell\) be a smooth cutoff equal to one on
\(|t|\le R_\ell-1\), zero for \(|t|\ge R_\ell\), with derivatives
of every fixed order bounded independently of \(\ell\). Such a
cutoff is obtained by translating two fixed endpoint profiles, not
by changing the gluing family. Write
\(\theta=d\phi+z_s(t)\beta\) on this support, and define

\[
 H_\ell=\chi_\ell(t) f(t)
             \bigl(dt^2-a_\ell(t)^2\theta^2\bigr). \tag{4}
\]

It is globally defined on the collar and vanishes smoothly before
both faces. It is trace-free for the actual metric. At \(t=0\),
its two nonzero endomorphism eigenvalues are \(1\) and \(-1\),
which proves the norm lower bound.

## 4. Error on the shear strip and cutoff bands

On \([0,1]\), \(a_\ell=O(\ell)\), while the closed one-form
\(\beta\), its derivatives, and \(z_s\) are fixed. Relative to the
product metric with connection \(d\phi\), the actual metric and
the uncut tensor (4) differ in geometric \(C^2\) by \(O(\ell)\).
Indeed the mixed metric term has size \(a_\ell z_s\beta=O(\ell)\)
in a unit frame, its square has size \(O(\ell^2)\), and all required
covariant derivatives involve bounded \(a_\ell'/a_\ell\), fixed
profiles, and fixed fiber derivatives. No coordinate estimate with
an unaccounted factor \(a_\ell^{-1}\) is used.

The coefficients of (1) depend on the metric through two derivatives.
The exact product identity therefore gives

\[
 |P_{G_\ell}H_\ell|+|\mathcal B_{G_\ell}H_\ell|
       \le C\ell\quad\hbox{on }[0,1]. \tag{5}
\]

Everywhere else on the support the uncut tensor is an exact product
kernel. The commutator with the cutoff has size at most
\(C(|\chi_\ell''|f+|\chi_\ell'|(|f'|+f))\). On its two unit-width
bands this is

\[
 |P_{G_\ell}H_\ell|+|\mathcal B_{G_\ell}H_\ell|
       \le C e^{-2kR_\ell}. \tag{6}
\]

The geometric derivatives of (4) are uniformly bounded: in the
product pieces all connection coefficients acting on the displayed
invariant tensors involve bounded \(a_\ell'/a_\ell\); (5) handles
the remaining compact strip. Differentiating the strip and cutoff
arguments any fixed number of times gives the same \(O(\ell)\) and
\(O(e^{-2kR_\ell})\) orders: all profiles have uniformly bounded
fixed-order derivatives and \(|\partial_t^jf|\le C_j f\).
Thus the corresponding first-derivative residual bound proves (2a).
Finally,

\[
 e^{-2kL_\ell}\asymp\ell,
 \qquad e^{-2kR_\ell}\asymp\ell^\vartheta.
\]

This proves the first two lines of (2).

For the \(L^2\) estimates the volume element on the entire plateau is
\(a_\ell\,dt\,d\phi\,d\mu_{h_F}\), including the shear strip.
Since the uncut tensor has squared norm \(2f^2\),

\[
 \|H_\ell\|_2^2\asymp
 \ell\int_{\mathbb R}\cosh(kt)\operatorname{sech}^4(kt)\,dt
 \asymp\ell.
\]

The strip in (5) contributes \(O(\ell^3)\) to the squared residual.
Each cutoff band contributes
\(O(\ell e^{kR_\ell}e^{-4kR_\ell})\). Therefore

\[
 \frac{\|P_{G_\ell}H_\ell\|_2}{\|H_\ell\|_2}
 \le C\bigl(\ell+e^{-3kR_\ell/2}\bigr)
 \le C\ell^{3\vartheta/4},
\]

as claimed.

## 5. Full-operator consequences and their scope

If \(P_{G_\ell}\) is invertible on its full Hölder realization,
(2a) forces the genuine Schauder-space inverse bound

\[
 \boxed{\|P_{G_\ell}^{-1}\|_{C^{0,\alpha}\to C^{2,\alpha}}
                     \ge c\ell^{-\vartheta}.} \tag{7}
\]

If the operator has a kernel, no full inverse exists. A complement
inverse is a different problem: the almost-kernel may project mainly
into the excluded kernel, and the remaining obstruction equation must
still be solved. The estimate does not assert a lower bound for every
choice of complemented inverse.

The operator (1) is elliptic and formally self-adjoint on the closed
manifold. Its self-adjoint \(L^2\) realization has discrete real
spectrum. The spectral theorem and (2) give

\[
 \boxed{\operatorname{dist}(0,\operatorname{spec}P_{G_\ell})
                     \le C\ell^{3\vartheta/4}.} \tag{8}
\]

This concerns the full gauged operator. It is not a claim about the
sign of the small eigenvalue, nor a proof of an exact Einstein
deformation. The Bianchi defect of the explicit tensor is small, not
identically zero after cutoff and shear.
The small spectral sector is trace-free: taking the trace of (1)
gives \(\operatorname{tr}(PT)=(\tfrac12\nabla^*\nabla+3)
\operatorname{tr}T\). Thus an eigenvector with eigenvalue less than
three has zero trace. This does not also establish divergence freedom
at the non-Einstein background.

The mode nevertheless has a uniform physical meaning modulo
diffeomorphisms. At \(t=0\), fix any fiber point and let \(\gamma\)
be its circle orbit. Its length is \(\ell\), and it is a closed
geodesic because the Killing-field length \(a_\ell\) has zero
gradient there. With \(U\) its unit tangent, define

\[
 \mathcal L(T)=\ell^{-1}\int_\gamma T(U,U)\,ds.
\]

For every smooth vector field \(V\),
\(\mathcal L(\mathcal L_VG_\ell)=0\): its integrand is
\(2\,d\langle V,U\rangle/ds\). But \(\mathcal L(H_\ell)=-1\).
Consequently

\[
 \inf_V\|H_\ell-\mathcal L_VG_\ell\|_{C^0,\mathrm{op}}\ge1.
 \tag{9}
\]

Thus the tensor is not a disguised pure gauge. This conclusion does
not identify the exact small eigenvectors with a transverse
trace-free quotient, which would require another projection argument.

There is also one independent mode per edge collar. Their tensors
and their images under \(P\) have disjoint supports. For a graph
with \(m\) edges and a common plateau fraction \(\vartheta\), every
tensor in their \(m\)-dimensional span satisfies the same \(L^2\)
residual-to-norm bound in (2). Apply the min--max principle to
\(P^2\), using \(\langle P^2T,T\rangle=\|PT\|_2^2\). It gives
at least \(m\) eigenvalues of the full \(P\), counted with
multiplicity, in

\[
 [-C\ell^{3\vartheta/4},C\ell^{3\vartheta/4}]. \tag{10}
\]

The \(m\) waist functionals are dual to these tensors (with sign
minus) and annihilate all pure gauges, so this multiplicity reflects
independent physical waist variations before solving the complete
equations.

For a chosen profile constant one on \([3/4,1]\), one may take
\(\vartheta=1/4\). Then (7) gives \(c\ell^{-1/4}\), while (8)
gives \(C\ell^{3/16}\). These convenient powers are not asserted
optimal. What matters is that the degeneracy is polynomial in the
pinching length, much faster than any power of \(|\log\ell|\).

## 6. The actual residual forces a sheared waist

Let \(E_\ell=\operatorname{Ric}_{G_\ell}+3G_\ell\). Outside the
electric-shear strip, the metric is exactly Einstein wherever
\(H_\ell\) is supported. On the strip the cutoff equals one and
Round 11 gives

\[
 E_{tt}=-\tfrac12a_\ell^2(z_s')^2|\beta|^2,\qquad
 E_{UU}=+\tfrac12a_\ell^2(z_s')^2|\beta|^2.
\]

All other residual entries are orthogonal to \(H_\ell\). Using
the actual volume element, not the product-coordinate density, gives
the exact pairing

\[
 \boxed{
 \int_M\langle E_\ell,H_\ell\rangle\,d\mu
 =-2\pi c_\ell^3\|\beta\|_{L^2(F,h_F)}^2
       \int_0^1\cosh(kt)(z_s'(t))^2\,dt.} \tag{11}
\]

It is strictly negative for a nonzero shear form and a nonconstant
connection profile. Its order is \(\ell^3\); pairing with the
unit \(L^2\) version of the mode has order \(\ell^{5/2}\).
There is no contribution from the slow mapping-class region because
the tensor has already been cut off within the fixed-fiber plateau.

This identifies a concrete analytic failure in the naive small-residual
argument: the complete gauged operator is nearly singular, the mode
changes a physical waist length, and the actual shear residual has
a nonzero pairing with it. The tensor is only an almost-eigenmode;
(11) is not an exact finite-dimensional obstruction equation.
Projection to the actual small spectral space, response from the
complement, and nonlinear cancellation remain to be analyzed. The
global continuous-branch volume obstruction in `round13_global.md`
does not need these operator estimates, but the two results now
connect an abstract obstruction to a visible neck-scale mechanism.

`round13_neck_kernel_check.py` checks the exact product tensor directly
using coordinate Gaussian curvature and divergence, including a
deliberately wrong profile that must fail. The localization and norm
estimates are established analytically above.
