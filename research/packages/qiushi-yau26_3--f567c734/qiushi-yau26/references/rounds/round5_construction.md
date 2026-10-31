# The whole-fibre receiver excludes critical-scale exact repairs

20 September 2026. This note treats the original balanced closed metrics
G_epsilon on the fixed Dehn-twist bundle E_D, with fibre waist epsilon,
base waist beta=epsilon squared, and the remaining surface moduli fixed.
The conclusion is a stronger neighbourhood obstruction, not nonexistence
of every Einstein metric on E_D.

## 1. Statement and the actual closed equation

Write E(g)=Ric(g)+g. All C2 norms below include the tensor and its first
two covariant derivatives relative to G_epsilon.

**Theorem.** For every sequence of smooth symmetric tensors satisfying
`||h_epsilon||_C2<=C epsilon^(3/2)` for a fixed C<infinity,

\[
 \liminf_{\varepsilon\to0}
 \frac{\delta_-(G_\varepsilon+h_\varepsilon)}{\varepsilon^3}
 \ge\frac1{16\pi^4(p-1)},
 \qquad
 \delta_-(g)=\|g^{-1}(\operatorname{Ric}(g)+g)\|_{\infty,\mathrm{op}}.
 \tag{1.0}
\]

In particular, for every fixed C<infinity there is epsilon_C>0 such that
there is no smooth h_epsilon satisfying

\[
 E(G_\varepsilon+h_\varepsilon)=0,\qquad
 \|h_\varepsilon\|_{C^2(G_\varepsilon)}
       \le C\varepsilon^{3/2},\qquad 0<\varepsilon<\varepsilon_C.
 \tag{1.1}
\]

No invariance, submersion, block-diagonal, or gauge assumption is imposed
on h_epsilon. Equivalently, every sequence of exact normalized repairs
with epsilon tending to zero has
`||h_epsilon||_C2 / epsilon^(3/2) -> infinity`.
The same statements hold relative to the three-scalar corrected background,
whose displacement from G_epsilon is O(epsilon squared) in C2.

There is also no Einstein metric of any constant in such a critical ball.
Indeed, if `Ric(g)=lambda g` there, the uniform Ricci Taylor bound gives
`lambda=-1+O(epsilon^(3/2))`. Thus lambda is negative and
`g_normalized=(-lambda)g` still lies in a fixed-multiple critical ball,
while `Ric(g_normalized)=-g_normalized`, which (1.1) excludes.

The existing global real TT tensor Q_epsilon is the pullback of the
concentrated holomorphic quadratic differential on the closed base. Its
verified estimates, on the original background, are

\[
 \int\langle E(G_\varepsilon),Q_\varepsilon\rangle
   =-\frac{\varepsilon^3\beta}{2\pi^2}(1+o(1)),\qquad
 \|J_{G_\varepsilon}Q_\varepsilon\|_1\le C\varepsilon^2\beta,
 \qquad \|Q_\varepsilon\|_1\le C\beta.
 \tag{1.2}
\]

Here J is the actual self-adjoint Bianchi linearization on the non-Einstein
background. These are the manuscript's `ED-global-pairings` estimates, not
the formal double-cylinder adjoint calculation. If (1.1) held, put
`U_epsilon=epsilon^(-3/2)h_epsilon`. The exact closed TT pairing and the
uniform C2 Ricci Taylor estimate give

\[
 \mathscr R_\varepsilon(U_\varepsilon)
 :=\frac1{2\beta}\int_{E_D}
       \langle D^2E_{G_\varepsilon}[U_\varepsilon,U_\varepsilon],
                        Q_\varepsilon\rangle\,dV_{G_\varepsilon}
 \longrightarrow\frac1{2\pi^2}.
 \tag{1.3}
\]

Indeed the linear term, divided by epsilon cubed beta, is O(sqrt(epsilon));
the cubic remainder is O(epsilon to the power 3/2). Also the exact equation
itself implies, in C0,

\[
 DE_{G_\varepsilon}U_\varepsilon=O(\varepsilon^{1/2}).
 \tag{1.4}
\]

The new point is that every subsequential limit of the left side of (1.3)
is nonpositive. This evaluates the response of the actual closed test,
including the whole fibre; no exterior receiver is set to zero.

## 2. The receiver measure is tight on a whole-fibre limit

Let (F_infinity,h) be the complete finite-area hyperbolic surface obtained
by pinching the single nonseparating fibre curve. It is connected, of genus
p-1 with two cusps, and has area 4 pi(p-1). In the central base collar
unwrap `y=beta theta`. On bounded t intervals and compact subsets of
F_infinity the backgrounds converge smoothly, on local covers, to

\[
 X=\mathbb R_t\times\mathbb R_y\times F_\infty,
 \qquad g_* =dt^2+\cosh^2t\,dy^2+h.
 \tag{2.1}
\]

Limit tensors will be y-independent; their integrals use one unit of
y-length. Write

\[
 f=\operatorname{sech}^2t,\quad
 J(t)=\arctan(\sinh t),\quad
 T=dt^2-\cosh^2t\,dy^2,\quad
 S=dt\otimes\cosh t\,dy+\cosh t\,dy\otimes dt,
 \qquad Q_*=fT.
 \tag{2.2}
\]

The limit of Q_epsilon is Q_star. Its norm and every fixed covariant
derivative are bounded by a constant times f. Thus all those derivatives
are L1 on the unit-y quotient of X, since
`integral_R f cosh(t) dt=pi` and F_infinity has finite area.

Here is the needed uniform tightness, rather than a pointwise assertion
about an escaping collar. On the shearing base subcollar,
`q_beta=q0+O_C2(beta^2)`, with `q0=fT`; outside it the tensor is O(beta
squared). Fibre area forms are independent of the path parameter. Hence
the beta-normalized Q mass outside `|t|<=T` is at most

\[
 C e^{-T}+O(\beta).
 \tag{2.3}
\]

For the fibre, truncate the two limiting cusps at depth R. The omitted
area of F_epsilon is bounded by `C exp(-R)+O(epsilon)`. This follows
directly by integrating `epsilon cosh(u)du ds` over the middle of its
collar, with angular period one and collar width
`w(epsilon)=log(1/epsilon)+O(1)`. Its contribution to the same normalized
receiver mass is at most

\[
 C e^{-R}+O(\varepsilon)+O(\beta).
 \tag{2.4}
\]

The remaining thick-base part contributes O(beta). In particular the
double-thin centre has vanishing receiver mass, but the limiting entire
punctured fibre must be retained. The original shear tends to zero with
all fixed derivatives on these compact sets: in a fixed cusp chart its
fibre radial coordinate is `|u|=w(epsilon)-O(1)`, and the balanced shear
factor is `O(epsilon sech(u)^2)`.

## 3. Compactness does not assume symmetry of the proposed repair

The original construction trivializes the bundle over the entire pinched
base annulus as `F x (-L,L) x S1`. The Dehn-twist transition to the exterior
is at its positive t-face, not at `theta=1`: its fibre path runs from h0
to `D^*h0` as t traverses the annulus. Equivalently the angular loop of this
collar lies in the kernel of the cyclic monodromy homomorphism. Thus an
arbitrary global tensor, not just the background metric, has exactly
beta-periodic components in this annular trivialization. No approximate
trivialization or division of a monodromy error by beta is involved.

On each compact subset of (2.1), components of U_epsilon therefore have
period beta in y and uniform coordinate C2 bounds. For a periodic function with those
bounds, its y derivative is O(beta), by the zero mean of that derivative
and the bound on its derivative. Its other first derivatives differ from
their angular averages by O(beta), using the mixed second-derivative
bounds. Thus U_epsilon minus its angular average tends to zero in C1 on
each such compact subset. After diagonal subsequence extraction the
averages converge in C1 to a y-independent U. It has globally bounded
covariant derivatives through order two in the weak sense; in particular
`U in W^(2,infinity)_loc` with uniform bounds. Equation (1.4) gives

\[
 DE_{g_*}U=0
 \tag{3.1}
\]

distributionally.

It is important not to interchange averaging and a quadratic expression
without this C1 estimate. Locally the second Ricci variation is a sum of
terms of types

\[
 U*\nabla^2U,\qquad \nabla U*\nabla U,\qquad
 \operatorname{Rm}*U*U.
 \tag{3.2}
\]

For a compactly supported smooth test, integrate the first type once by
parts. The resulting quadratic pairing depends continuously on C1
convergence with a uniform C2 bound. In the periodic direction the boundary
terms cancel, so this argument also applies to the average over the actual
shrinking y-period. The nonzero Fourier modes therefore contribute o(1),
not an uncomputed quadratic source.

Finally the absolute value of the second variation is uniformly bounded,
and (2.3)--(2.4) bound all omitted receiver tails. It follows that

\[
 \mathscr R_\varepsilon(U_\varepsilon)
 \longrightarrow
 \mathscr R_*(U):=rac12\int_{(\mathbb R\times S^1)\times F_\infty}
          \langle D^2E_{g_*}[U,U],Q_*\rangle\,dV_{g_*}.
 \tag{3.3}
\]

The integral has unit y-period. For nonsmooth U it has the weak meaning
just described; its integrand is also bounded almost everywhere.

## 4. A bounded gauge, and why its receiver contribution vanishes

Use `b U=-div U+(1/2)d tr U`. For the Lie derivative of the metric,

\[
 b(\mathcal L_Xg_*)=(\nabla^*\nabla+1)X^\flat.
 \tag{4.1}
\]

There is a bounded solution to
`(nabla*nabla+1)X^flat=b U`. To construct it, solve the Dirichlet problems
on an exhaustion and use the Kato maximum principle to obtain
`||X||_infinity<=||b U||_infinity`. Interior estimates on fixed-size
hyperbolic-product local covers give uniform first-derivative bounds and
local compactness; pass to a subsequence. Average over the unit y-circle
to make X y-independent. The source is bounded and locally Lipschitz,
so the same estimates supply the regularity used below. This construction
does not need an injectivity-radius lower bound in the cusps.

Set `V=U-L_X g_star`. Then bV=0 and, by naturality of E and (3.1),

\[
 LV=0,\qquad L=\tfrac12(\nabla^*\nabla-2\mathring R).
 \tag{4.2}
\]

V is bounded. Uniform local-cover elliptic regularity makes V smooth with
all fixed derivatives bounded. The identity for a vector field's second
derivative in terms of the first derivative of its symmetrized gradient
and curvature, applied to `L_Xg_star=U-V`, then supplies bounded weak
derivatives of X through order three. This also gives a direct regularity
justification if the initial limit U is only C1,1.

The receiver is unchanged by this bounded gauge. For a smooth field X,
differentiate the naturality identity for
`phi_s^*(g_star+sV)` twice. As `E(g_star)=DE(V)=0`, one obtains

\[
 D^2E[U,U]-D^2E[V,V]
   =-DE[W],\qquad W=2\mathcal L_XV+\mathcal L_X^2g_*
                    =\mathcal L_X(U+V).
 \tag{4.3}
\]

The same formula follows distributionally by local smooth approximation
in the C1,1 case. W is bounded. The tensor Q_star is TT and LQ_star=0,
so `(DE)^*Q_star=0`. Choose exhaustion cutoffs with uniformly bounded
first two derivatives, on both the cylinder and the finite-area cusps.
Pair DE W with cutoff times Q_star and transfer both derivatives to the
test. All commutator integrals tend to zero, because W is bounded and
Q_star and its derivatives are L1. Thus

\[
 \mathscr R_*(U)=\mathscr R_*(V).
 \tag{4.4}
\]

No assertion that a bounded tensor has zero pointwise cusp flux is used.
It is the integrable test and its derivatives that justify this passage.

## 5. Full bounded Jacobi classification on the receiver limit

Let `P_t=partial_t^2+tanh(t)partial_t`, let Delta_F be the nonnegative
scalar Laplacian, and Delta_H,F the nonnegative Hodge Laplacian on
one-forms. Decompose symmetric tensors into the two factor traces,
horizontal trace-free tensors, mixed tensors, and fibre trace-free tensors.
For y-independent tensors the product connection gives the following
operators for 2L:

| Tensor sector | Operator |
| --- | --- |
| The two factor traces | `-P_t+Delta_F+2` |
| Coefficients of T and S | `-P_t+Delta_F+2-4f` |
| Each horizontal one-form times a fibre one-form | `-P_t+Delta_H,F+2-f` |
| Fibre trace-free symmetric tensors | `-P_t+A_F`, with `A_F=Delta_E,F` |

For completeness, the mixed potential includes `tanh(t)^2` from the
horizontal one-form and `+1` in the identity
`nabla_F*nabla_F=Delta_H,F+1`. Thus it is bounded below by one; products
of harmonic one-forms are not overlooked zero modes.

The surface identities on trace-free symmetric tensors are

\[
 A_F=2P_F\delta_F,\qquad
 \delta_FP_F=\tfrac12(\Delta_{H,F}+2),
 \tag{5.1}
\]

where P is the trace-free symmetrized derivative and delta is its adjoint.
They follow by commuting two covariant derivatives at curvature minus one.
On the complete finite-area surface these identities extend from compactly
supported sections to the Friedrichs forms by cutoff. Since
`P_F^* P_F>=1`, P has closed range. Consequently

\[
 \mathcal H_F:=\ker A_F=\ker\delta_F
 \quad\hbox{on trace-free }L^2\hbox{ tensors},\qquad
 A_F\ge2\quad\hbox{on }\mathcal H_F^\perp.
 \tag{5.2}
\]

This argument includes the cusp domain; no compact-surface spectral theorem
is being applied to a noncompact surface without checking its domain.
Bounded tensors with bounded derivatives on F have finite L2 norm, since
the area is finite, and lie in the relevant maximal/Friedrichs domains by
the same cutoffs.

The trace and mixed sectors vanish. For example, the squared L2(F) norm
w(t) of a mixed component satisfies `P_t w>=2w`; it is bounded and
nonnegative. The bounded maximum principle for `-P_t+2` gives w=0.
The trace argument has the stronger potential two.

For a horizontal coefficient z, bounded comparison on each half-cylinder,
where `2-4f>=1`, using the positive solution f gives `|z|<=C f`.
This comparison is valid uniformly in F: use its complete bounded maximum
principle, or a proper cusp exhaustion with bounded gradient and Laplacian.
Write z=fa. The bounded function a solves

\[
 -\frac1m\partial_t(m\partial_t a)+\Delta_Fa=0,
 \qquad m=\operatorname{sech}^3t.
 \tag{5.3}
\]

Both m dt and dA_F have finite total mass. Test with cutoff squared times
a; boundedness and cutoff exhaustion make the energy of both derivatives
zero. Connectedness therefore makes a constant.

For a fibre trace-free component, project in L2(F) onto
`H_F` and its orthogonal complement. For the latter, its squared norm
satisfies `P_t w>=4w`, by (5.2), so it vanishes. The kernel component
solves `P_t V_F=0` as a Hilbert-valued equation. Its general solution is
`A+J(t)B`. Evaluating at two finite t-values shows that A and B, together
with every fixed derivative, are bounded on F. Both are L2 TT tensors.

We have proved, without a fibre-invariance assumption,

\[
 \boxed{\quad V=f(aT+bS)+A+J(t)B,
       \qquad A,B\in\mathcal H_F\hbox{ bounded},\quad a,b\in\mathbb R.
       \quad}
 \tag{5.4}
\]

This is a classification on the whole-fibre receiver limit, not a claim
about the entire finite-epsilon kernel on E_D.

## 6. The actual quadratic response and its sign

The horizontal component `f(aT+bS)` is the tangent to the exact
curvature-minus-one cylinder family already used in round three:

\[
 c_s=\frac{\cosh^2t}{\sinh^2t+e^{-sa}}dt^2
       +(\sinh^2t+e^{-sa})(dy+sb\operatorname{sech}^3t\,dt)^2.
 \tag{6.1}
\]

Its area form is fixed. Let `H(t)=h^(-1)(A+J(t)B)` and use the explicit
positive fibre path

\[
 h_s(t)(v,w)=h(\exp(sH(t))v,w),\qquad k_s=c_s+h_s(t).
 \tag{6.2}
\]

As H is trace-free, the fibre area form is independent of both s and t.
No claim that h_s is hyperbolic is required. The full block metric formula
for horizontal Ricci is

\[
 (\operatorname{Ric}_{k_s})_{ij}
  =(\operatorname{Ric}_{c_s})_{ij}
          -\operatorname{tr}(S_iS_j),\qquad
  S_i=\tfrac12h_s^{-1}\partial_i h_s.
 \tag{6.3}
\]

The usual Hessian of the logarithmic fibre volume vanishes identically.
Only the t derivative is present, and to first order
`S_t=(s/2)J'(t)h^(-1)B`. Since `Ric(c_s)+c_s=0`,

\[
 \left.\frac{d^2}{ds^2}\right|_0 E(k_s)_{\rm horizontal}
        =-\tfrac12J'(t)^2|B|_h^2\,dt^2.
 \tag{6.4}
\]

The acceleration k_second is bounded, so its linearized contribution
`DE(k_second)` has zero pairing with Q_star by the same L1 cutoff
argument as in Section 4. Therefore (6.4) is exactly the receiver of
the affine second variation, not merely the second variation along a
convenient path. It follows that

\[
 \boxed{\quad
 \mathscr R_*(U)=\mathscr R_*(V)
  =-\frac14\int_\mathbb R f(t)J'(t)^2\cosh t\,dt\,
                         \|B\|_{L^2(F)}^2
  =-\frac\pi8\|B\|_{L^2(F)}^2\le0.
 \quad}
 \tag{6.5}
\]

Here `J'=sech(t)` and `integral sech(t)^3 dt=pi/2`.
Constant fibre deformations, both horizontal polarizations, arbitrary
mixed/gauge components of the original limit, and all fibre TT modes
have been accounted for. The nonzero response has the sign of the negative
horizontal fibre-shape stress.

Equations (1.3), (3.3), and (6.5) contradict one another, proving the exact
repair exclusion.

To obtain the stronger quantitative statement (1.0), it is enough to
consider subsequences on which the defect divided by epsilon cubed remains
bounded. On such a subsequence, the residual term in the analogue of (1.4)
is O(epsilon to the power 3/2), so the same Jacobi limit and sign calculation
apply. The full closed Taylor pairing is now

\[
 \frac1{\varepsilon^3\beta}
 \int\langle E(G_\varepsilon+h_\varepsilon),Q_\varepsilon\rangle
 =-\frac1{2\pi^2}+\mathscr R_\varepsilon(U_\varepsilon)+o(1).
 \tag{6.6}
\]

Its limiting value is at most `-1/(2 pi^2)`. The nuclear norm of the
actual global test satisfies

\[
 \beta^{-1}\int|Q_\varepsilon|_*\,dV_{G_\varepsilon}
       \longrightarrow8\pi^2(p-1).
 \tag{6.7}
\]

Comparison between the metrics in the operator norm costs only 1+o(1).
The dual operator/nuclear norm inequality proves (1.0). This argument
retains the full residual tensor; it does not presume exactness when
proving the quantitative bound.

For each fixed C>0, the existing O(epsilon squared) three-scalar correction
lies in this critical ball for small epsilon and has defect O(epsilon
cubed). Consequently

\[
 \inf_{\|h\|_{C^2(G_\varepsilon)}\le C\varepsilon^{3/2}}
               \delta_-(G_\varepsilon+h)=\Theta(\varepsilon^3).
 \tag{6.8}
\]

The lower-bound constant in (1.0) is retained; no claim that it is the
optimal leading coefficient in (6.8) is needed.

## 7. Meaning, limitations, and verification

The old C2 estimate only forced an exact correction to be at least a
constant times epsilon to the power 3/2. The present theorem excludes every
fixed multiple at that scale and extends the cubic quantitative lower bound
to the entire critical C2 ball. It uses the leading Jacobi equation supplied
by an exact or cubic-residual sequence, rather than assigning a sign to the
quadratic form on arbitrary bounded tensors. In particular it does not
claim that the unrestricted Ricci quadratic form is nonpositive.

For corrections much larger than epsilon to the power 3/2, the normalized
source in (1.3) can tend to zero; (6.5) then permits B=0. Removing those
integrable directions with estimates at the next scale is a further
problem. This argument neither performs that nonlinear reduction nor
excludes a distant or differently degenerating Einstein metric on E_D.

The prior nonlinear charge and exact-open-core obstruction remain useful
but are not used to suppress an exterior term here. The beta-normalized
whole-fibre measure, the bounded-gauge calculation, and the all-sector
Jacobi classification are the additional ingredients.

The supporting script `round5_construction_check.py` independently checks
the horizontal Ricci formula for an arbitrary determinant-preserving
two-dimensional fibre matrix, the full surface operator identity (5.1),
the Jacobi scalar identities, the receiver coefficient, and elementary
tail integrals. These finite computations do not replace the compactness,
gauge, and noncompact-domain arguments above.

For primary context, [Kröncke's product-deformation
paper](https://arxiv.org/abs/1508.00721) establishes compact Einstein-product
spectral decompositions; Section 5 supplies the finite-area version needed
here. The closed detector used in (1.2) is based on the concentrated
quadratic-differential estimate in [Rupflin--Topping, Lemma
4.4](https://arxiv.org/abs/1403.3195), as normalized and proved in the
existing construction manuscript. No new assertion about the original
unrestricted Yau26 problem is made.
