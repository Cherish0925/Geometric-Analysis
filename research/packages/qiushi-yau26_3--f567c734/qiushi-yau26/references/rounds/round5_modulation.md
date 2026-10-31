# Global modulation: a logarithmic obstruction, but not at polynomial accuracy

20 September 2026. The whole-fibre theorem in `round5_construction.md`
excludes every fixed O(epsilon to the power 3/2) C2 neighbourhood of an
exact Einstein repair. This note tests the next proposed step: remove the
semidefinite receiver kernel by global Teichmüller and waist parameters,
then improve the size of the remaining correction.

There is a concrete obstruction to a **uniform** maximum-norm modulation
estimate on the actual E_D backgrounds. It persists after every reference
parameter direction and every smooth infinitesimal diffeomorphism have
been allowed. Its loss is logarithmic, however. It is much too inaccurate
to be an exact-repair candidate at the polynomial scales in question.
A fixed-power logarithmic inverse remains sufficient for the proposed
o(epsilon) exclusion; that full inverse has not been established here.

## 1. What is and is not globally integrable

In the receiver classification, its zero set B=0 consists, after bounded
gauge, of a horizontal cylinder length/twist variation and a constant
bounded TT deformation of the complete finite-area fibre. These are
ordinary infinitesimal hyperbolic-surface deformations. At the limiting
level they integrate in the cylinder and punctured-surface Teichmüller
spaces. Persistent fibre deformations can be realized in closed pinching
surfaces by varying the remaining Fenchel--Nielsen parameters, keeping the
pinched length fixed. The persistent holomorphic-differential subspace and
its cusp convergence are treated in [Rupflin--Topping--Zhu, Section
2](https://arxiv.org/abs/1209.3783).

This does not produce a family of exact closed Einstein product metrics
on E_D. The global Dehn-twist gluing remains in place. What can be varied
globally is the actual **approximate** reference family: the two surface
metrics, their waist lengths and twists, and the balanced shear profiles.
In its annular trivialization, every such parameter derivative has a
horizontal metric block depending on base position alone; the additional
profile derivatives are vertical. Changing the trivialization adds an
infinitesimal diffeomorphism, which will be included below.

Thus there is no new local Teichmüller integrability obstruction for B=0.
The missing step is quantitative global control of everything not removed
by these actual parameter changes. Replacing the actual family by a
fictitious exact global product would remove the topology being studied.

## 2. An actual closed TT tensor invisible to the receiver limit

Retain beta=epsilon squared and the genuine global horizontal TT tensor
Q_epsilon on E_D. Let `w=w(epsilon)` be the full fibre collar half-width,
and set

\[
 \Lambda_\varepsilon=\log\cosh w
                  =\log(1/\varepsilon)+O(1).
 \tag{2.1}
\]

Choose one fixed smooth cutoff chi(x), zero for x near zero, one for x>=1,
with values in [0,1]. On the fibre collar define

\[
 a_\varepsilon(u)=\frac{\chi(w-|u|)}{\Lambda_\varepsilon}
       \bigl(\Lambda_\varepsilon-\log\cosh u\bigr),
 \qquad U_\varepsilon=a_\varepsilon Q_\varepsilon,
 \tag{2.2}
\]

and extend a_epsilon by zero outside the fibre collar. The cutoff is
constant near u=0, so the absolute-value notation causes no nonsmoothness.
The function depends only on u and is invariant under the Dehn twist.
It therefore defines a smooth global function on E_D. Its gradient is
vertical, while Q_epsilon is horizontal and TT. The product rule gives

\[
 \operatorname{tr}U_\varepsilon=0,
 \qquad \operatorname{div}U_\varepsilon
       =a_\varepsilon\operatorname{div}Q_\varepsilon
          +Q_\varepsilon(\nabla a_\varepsilon,\cdot)=0.
 \tag{2.3}
\]

This is an exact closed TT tensor, not a formal model mode. It has
`a_epsilon(0)=1`, vanishes on the thick fibre, and satisfies for every fixed
k>=1

\[
 \|\nabla^k a_\varepsilon\|_\infty\le C_k/\Lambda_\varepsilon,
 \qquad \|U_\varepsilon\|_{C^k}\le C_k.
 \tag{2.4}
\]

For the nonnegative scalar Laplacian, the uncut function in (2.2) obeys

\[
 \Delta_G a_\varepsilon
 =-a_\varepsilon''-\tanh u\,a_\varepsilon'
 =\Lambda_\varepsilon^{-1}.
 \tag{2.5}
\]

The formula remains valid in the sheared fibre coordinates: the gradient
is `a'(partial_u-tau zeta' partial_s)`, and the common volume density is
epsilon cosh u. The cutoff bands contribute only O(1/Lambda).

Let J_G be the actual self-adjoint operator from the global TT identity.
Its scalar product rule is

\[
 J_G(aQ)=aJ_GQ+\tfrac12(\Delta_Ga)Q-\nabla_{\nabla a}Q.
 \tag{2.6}
\]

The original reference estimates give `||J_GQ||_Ck=O(epsilon)` and
`||nabla_vertical Q||_Ck=O(epsilon)`; the latter comes from the vertical
shape operator. Thus

\[
 \|DE_GU_\varepsilon\|_{C^k}
  =\|J_GU_\varepsilon\|_{C^k}
  \le C_k/\Lambda_\varepsilon.
 \tag{2.7}
\]

There is also a matching lower bound. At t=u=0, a=1 and da=0. The bound
`||J_GQ||_infinity=O(epsilon)` and the exact product rule imply

\[
 (J_GU_\varepsilon)_{\rm horizontal}
        =\frac1{2\Lambda_\varepsilon}Q_\varepsilon+O(\varepsilon)
                       \quad\hbox{at }t=u=0.
 \tag{2.8}
\]

Since Q is its unit-sized cylinder mode there, up to O(beta squared), and
`epsilon Lambda_epsilon -> 0`,
`||DE_GU_epsilon||_infinity` is bounded above and below by positive
constants times `1/Lambda_epsilon`.

On every fixed truncated compact subset of the whole-fibre receiver limit,
a_epsilon and its derivatives are O(1/Lambda). Hence U_epsilon tends to
zero there, although its global maximum does not tend to zero. Its limit
has A=B=0 in the previous classification.

More quantitatively, for each fixed r<infinity,

\[
 \int_{F_\varepsilon}|a_\varepsilon|^r\,dA
              \le C_r\Lambda_\varepsilon^{-r}.
 \tag{2.9}
\]

To see this put x=w-|u|. The numerator in (2.2) is at most x, and
`epsilon cosh(w-x)<=C(exp(-x)+epsilon)`. Integrate x to w and divide by
Lambda to the power r; the additional `epsilon w^(r+1)` is bounded.
The same estimate and (2.4), with the integrable base detector weight,
bound the actual quadratic receiver by

\[
 |\mathscr R_\varepsilon(U_\varepsilon)|
              \le C\Lambda_\varepsilon^{-2}.
 \tag{2.10}
\]

This estimate does not assign its finite-epsilon sign. It shows that the
semidefinite receiver and its limiting kernel do not control the global
maximum norm.

## 3. Global parameters and arbitrary infinitesimal gauge cannot remove it

The obstruction can be read directly at the central base waist t=0.
In the original annular trivialization

\[
 G_{\theta\theta}=\beta^2\cosh^2t,\qquad
 G_{\theta t}=G_{\theta F}=0.
\]

For every smooth vector field X on E_D, regardless of its size, at t=0

\[
 \beta^{-2}(\mathcal L_XG)_{\theta\theta}
                      =2\partial_\theta X^\theta.
 \tag{3.1}
\]

Its average over the unit theta-circle is exactly zero. The transverse
monodromy is at the t-face, so this is an ordinary periodic coordinate
calculation, not an assumption about the unknown diffeomorphism.

Let B be any smooth tensor whose averaged normalized theta-theta component
at t=0 is independent of fibre position. This class includes every linear
combination of derivatives of the actual reference Teichmüller/waist
parameters, together with arbitrary vertical or mixed tensors. On the
other hand, the same average for U_epsilon is

\[
 a_\varepsilon(u)(-1+O(\beta^2)).
 \tag{3.2}
\]

It takes values `-1+O(beta^2)` at the fibre waist and zero on the thick
fibre. Subtracting one fibre-independent number cannot approximate both
within less than half their difference. Equations (3.1)--(3.2) prove

\[
 \boxed{\quad
 \inf_{B,X}\|U_\varepsilon-B-\mathcal L_XG_\varepsilon\|_{C^0}
                      \ge\tfrac12-O(\beta^2).
 \quad}
 \tag{3.3}
\]

Thus no estimate with an epsilon-independent constant of the form

\[
 \operatorname{dist}_{C^0}
       (U,\{\hbox{reference tangents}\}+\{\mathcal L_XG\})
                  \le C\|DE_GU\|_{C^k}
 \tag{3.4}
\]

can hold, for any fixed finite k. Any such inverse constant must grow at
least like log(1/epsilon). This is a failure of linear uniform coercivity,
including gauge and the actual closed reference parameters. It is not
merely a deficiency of a selected basis of TT test tensors.

## 4. The logarithmic example is too inaccurate at exact-repair scales

Scale the tensor by a positive eta_epsilon tending to zero. The global
Ricci Taylor estimate, (2.8), and `||E(G_epsilon)||_infinity=O(epsilon^2)`
give

\[
 \delta_-(G_\varepsilon+\eta_\varepsilon U_\varepsilon)
 \ge c\frac{\eta_\varepsilon}{\Lambda_\varepsilon}
                 -C\varepsilon^2-C\eta_\varepsilon^2.
 \tag{4.1}
\]

For `eta_epsilon=epsilon^q`, with `1<q<3/2`,

\[
 \frac{\eta_\varepsilon/\Lambda_\varepsilon}{\varepsilon^2}
                  \longrightarrow\infty,\qquad
 \frac{\eta_\varepsilon^2}{\eta_\varepsilon/\Lambda_\varepsilon}
                  =\eta_\varepsilon\Lambda_\varepsilon\longrightarrow0.
 \tag{4.2}
\]

These perturbations are o(epsilon), and larger than the critical
epsilon-to-the-3/2 scale, but their defect is much larger than epsilon
squared. They are not prospective exact repairs. Equivalently exactness
at amplitude eta would require

\[
 \|DE_GU\|_\infty
       =O(\varepsilon^2/\eta+\eta),
 \tag{4.3}
\]

which is polynomially smaller than `1/log(1/epsilon)` in this range.
For forcing of size epsilon squared, the tested logarithmic loss gives
amplitude `epsilon^2 log(1/epsilon)`, which is itself o(epsilon to the
power 3/2). Therefore (3.3) does **not** refute the desired stronger
exclusion. It specifies a loss that a correct argument must allow and
shows that the loss is harmless at these polynomial scales.

## 5. The exact missing estimate for an o(epsilon) exclusion

Here is a sufficient non-tautological target, with its required accuracy.
Work in a fixed Bianchi slice and uniform local-cover Hölder spaces
`X_epsilon=C^(2,alpha)`, `Y_epsilon=C^(0,alpha)`; include uniform control
of the coordinate/gauge change if starting only with a C2-small exact
metric. Let V_epsilon consist of derivatives of the **actual** global
reference family, including profile responses when waist parameters vary,
not just bare product Jacobi tensors.

One needs a controlled splitting with parameter coefficients O(||h||_X),
and, for some fixed finite m,

\[
 \operatorname{dist}_{X_\varepsilon}
       (h,V_\varepsilon+\{\mathcal L_XG_\varepsilon\})
   \le C\log(1/\varepsilon)^m
                           \|DE_{G_\varepsilon}h\|_{Y_\varepsilon}.
 \tag{5.1}
\]

The counterexample proves that m=0 is impossible; it does not disprove
(5.1) with m>=1. A formulation using projected equations or an explicit
finite-rank remainder is equivalent only if that remainder is integrated
by the same controlled global reference parameters. An extra near-zero
mode cannot simply be projected away without a realizable parameter.

To see why this estimate would suffice, suppose an exact perturbation
has norm a_epsilon=o(epsilon) in this slice. Then

\[
 \|DE_Gh\|_Y\le C(\varepsilon^2+a_\varepsilon^2)
                                      =O(\varepsilon^2).
 \tag{5.2}
\]

After the controlled parameter and diffeomorphism modulation, the remainder
would have norm

\[
 O(\varepsilon^2\log(1/\varepsilon)^m+a_\varepsilon^2)
                              =o(\varepsilon^{3/2}).
 \tag{5.3}
\]

The quadratic term includes integrating the linear parameter/gauge
directions. Applying the critical-scale theorem at the modulated
background would contradict exactness. Its estimates persist for small
changes of the other moduli and relative waist changes tending to zero:
the whole-fibre limits and source coefficient vary continuously, and the
source coefficient remains negative. If the two waist lengths are varied
independently, the ratio `beta/epsilon^2` remains 1+o(1), which leaves
the normalized estimates unchanged to leading order.

What is not yet proved is (5.1), with controlled splitting and nonlinear
parameter realization, for the entire closed E_D operator. Neither the
bounded receiver-limit classification nor the positive spectrum of a
closed hyperbolic product supplies it. The non-product clutching and all
small eigenvalue sectors must be treated in that global estimate. The
bare horizontal Q is not itself an exact Jacobi field on G_epsilon:
varying a waist includes vertical profile terms, as the existing
`J_GQ` formula explicitly demonstrates.

Thus this bounded trial has a definite outcome: uniform modulation is
false on the actual candidate; logarithmic modulation remains both
mathematically possible and quantitatively sufficient for o(epsilon).
No o(epsilon) or o(1) exclusion is asserted without that remaining estimate.

## 6. A weaker weighted target and a finite-collar way to attack it

A full maximum-norm estimate such as (5.1) is stronger than the receiver
argument needs. For the actual detector define

\[
 \|r\|_{\mathcal W_\varepsilon}^2
  =\frac1\beta\int|Q_\varepsilon|
          (|r|^2+|\nabla r|^2+|\nabla^2r|^2)\,dV_G.
 \tag{6.1}
\]

It would suffice to choose controlled *actual global reference parameters*
and gauge so that an exact perturbation of size a=o(epsilon) has remainder
r with global C2 norm O(a) and

\[
 \|r\|_{\mathcal W_\varepsilon}
       \le C\log(1/\varepsilon)^m(\varepsilon^2+a^2).
 \tag{6.2}
\]

Indeed, at the modulated background the linear receiver term is bounded
by `C epsilon^2 a=o(epsilon^3)`. The nonlinear term is bounded by
`C ||r||_W^2=O(epsilon^4 log(1/epsilon)^(2m))=o(epsilon^3)`, using the
pointwise quasilinear Ricci remainder and Cauchy--Schwarz in (6.1).
Neither can cancel the negative source coefficient. This supplies a
specific receiver-weighted alternative to (5.1), not an assertion of its
validity. The ramp above has W norm O(1/Lambda), so its maximum-norm failure
does not also refute a uniform estimate in this weaker norm.

A concrete way to seek (6.2) is to retain the finite base collar and the
entire **closed** F_epsilon, rather than first pass to F_infinity. On each
hyperbolic fibre the exact identity `A_F=2P delta` gives gap two off the TT
space. The scalar Laplacian on these single-nonseparating-pinching fibres
has a uniform positive first eigenvalue when the remaining moduli stay in
the specified compact set. This last hypothesis is essential: a separating
pinch has additional small scalar modes.

The background shear is O(epsilon) in local-cover coefficient norms, so
the full operator can be compared with these fibrewise blocks while
retaining the variation of the fibre TT projection along t. Cutoff errors
at `|t|=log(1/beta)+O(1)` have detector mass O(beta), which is usable in
(6.1). The scalar collar equation has the explicit maximum-norm barrier
`log cosh L-log cosh t`, explaining rather than hiding a logarithmic loss.

The unresolved terms are the transport of the full fibre TT subspace,
its matching to the connected exterior, and the identification of every
remaining small mode with an actual global parameter. In particular a
coefficient J(t)B with B nonzero cannot simply be called a global
Teichmüller parameter; it is a transfer mode whose receiver is negative.
It must either be estimated with its sign retained or matched through
the exterior equation. The finite-collar proposal does not assume this
matching or the desired estimate in advance.

`round5_modulation_check.py` checks the radial forcing, weighted-ramp
integrals, waist gauge-average identity, and the polynomial/logarithmic
scale comparisons. It does not certify the missing global inverse.
