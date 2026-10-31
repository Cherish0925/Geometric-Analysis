# Torsion-zero indices: what the first Einstein–almost-Kähler jet identities do and do not imply

## Result and precise scope

At a hypothetical zero of the intrinsic torsion of an almost-Kähler Einstein four-manifold, the first curvature identities and the fundamental-form Weitzenböck identity admit torsion derivatives of both determinant signs, with exactly the same Einstein algebraic curvature tensor and any prescribed scalar curvature `s < 0`.

This is a calculation of **necessary pointwise jet conditions**. It does not construct an almost-Kähler Einstein germ, establish prolongation to every order, or prove local analytic realization. Consequently it does not settle the negative Goldberg problem. It rules out an index-sign argument based solely on the displayed first-layer identities.

## 1. Conventions

Let `(e_1,e_2,e_3,e_4)` be a positively oriented orthonormal tangent frame at a point `p`, with

\[
Je_1=e_2,\quad Je_2=-e_1,\quad Je_3=e_4,\quad Je_4=-e_3.
\]

Write `e^{ij}=e^i\wedge e^j`, and set

\[
\Omega=e^{12}+e^{34},\qquad
\phi=e^{13}-e^{24},\qquad
J\phi=e^{14}+e^{23}.
\tag{1}
\]

All three forms are self-dual and have squared norm `2`, where the norm is the induced exterior-power norm. The action on one-forms and on the anti-invariant two-form `phi` is

\[
(Ja)(X)=-a(JX),\qquad
(J\phi)(X,Y)=-\phi(JX,Y).
\tag{2}
\]

In components,

\[
Ja=(-a_2,a_1,-a_4,a_3).
\tag{3}
\]

The local connection formulas are

\[
\begin{aligned}
\nabla\Omega&=a\otimes\phi-Ja\otimes J\phi,\\
\nabla\phi&=-a\otimes\Omega+b\otimes J\phi,\\
\nabla(J\phi)&=Ja\otimes\Omega-b\otimes\phi.
\end{aligned}
\tag{4}
\]

These agree with Apostolov–Armstrong–Drăghici, *Local Rigidity of Certain Classes of Almost Kähler 4-Manifolds*, Ann. Global Anal. Geom. **21** (2002), 151–176, formulas (7)–(8). The exterior algebra identity

\[
a\wedge\phi-Ja\wedge J\phi=0
\tag{5}
\]

expresses the almost-Kähler closure condition in this parametrization.

Assume `a(p)=0`. A local phase choice for `phi` allows `b(p)=0` as well. This is only a frame choice at one point. It does not set `db(p)=0`.

Define

\[
A_{ij}=(\nabla_{e_i}a)(e_j)\big|_p.
\tag{6}
\]

At `p`, derivatives of `J` vanish because `nabla Omega=0`. Consequently differentiation of `Ja` at `p` uses the fixed matrix (3), with no extra derivative-of-`J` term.

## 2. The family of torsion derivatives

For a real parameter `t`, prescribe

\[
A_t=\operatorname{diag}(1+t,1-t,1,1).
\tag{7}
\]

It is symmetric, so

\[
(da)_p=0.
\tag{8}
\]

Using (3),

\[
\begin{aligned}
(d(Ja))_{12}&=A_{11}+A_{22}=2,\\
(d(Ja))_{34}&=A_{33}+A_{44}=2,
\end{aligned}
\]

and its other components vanish. Thus

\[
(d(Ja))_p=2\Omega.
\tag{9}
\]

Also

\[
\operatorname{tr}A_t=4,
\qquad
\operatorname{tr}(\nabla(Ja))_p=0,
\qquad
\det A_t=1-t^2.
\tag{10}
\]

In particular, `A_0` is invertible with determinant `+1`, whereas `A_2` is invertible with determinant `-3`.

## 3. A single Einstein algebraic curvature tensor fits every member

Use the curvature-operator convention

\[
R=\frac{s}{12}\operatorname{Id}_{\Lambda^2}
   +\operatorname{Ric}_0^{\sharp}+W^++W^-.
\tag{11}
\]

With the connection convention (4), the Ricci identities are

\[
\begin{aligned}
da-Ja\wedge b&=-R(J\phi),\\
d(Ja)+a\wedge b&=-R(\phi).
\end{aligned}
\tag{12}
\]

These are formula (12) of the cited paper. At `p`, equations (8)–(9) require

\[
R(J\phi)=0,\qquad R(\phi)=-2\Omega.
\tag{13}
\]

For any prescribed real scalar `s`, including every `s<0`, choose

\[
R_+=
\begin{pmatrix}
 s/4&-2&0\\
 -2&0&0\\
 0&0&0
\end{pmatrix},
\qquad
R_-=\frac{s}{12}I_3,
\qquad
R_{+-}=R_{-+}=0.
\tag{14}
\]

The rows and columns of `R_+` are ordered by

\[
\Omega/\sqrt2,\quad\phi/\sqrt2,\quad J\phi/\sqrt2.
\]

Because the three unnormalized forms have the same norm, the same matrix also describes the coefficients of their images. Explicitly its three columns say

\[
\begin{aligned}
R(\Omega)&=\frac{s}{4}\Omega-2\phi,\\
R(\phi)&=-2\Omega,\\
R(J\phi)&=0.
\end{aligned}
\tag{15}
\]

This gives (13). It also shows why the off-diagonal entries must be symmetric: the `-2 phi` term in `R(Omega)` is not optional.

The matrix is self-adjoint and

\[
\operatorname{tr}R_+=\operatorname{tr}R_-=s/4.
\tag{16}
\]

For a self-adjoint operator on `Lambda^2` in dimension four, equality of these two traces is the algebraic first Bianchi identity. Thus (14) is an algebraic Riemann curvature tensor, not just an arbitrary block matrix. Its off-diagonal chiral block vanishes, which is precisely the Einstein algebraic condition; its Ricci tensor is

\[
\operatorname{Ric}=\frac{s}{4}g.
\tag{17}
\]

The remaining connection-curvature formula also fits at this order. Formula (16) of the cited paper is

\[
db=a\wedge Ja-R(\Omega).
\]

At `p`, this prescribes

\[
(db)_p=-\frac{s}{4}\Omega+2\phi.
\tag{18}
\]

One may prescribe the antisymmetric part of the first derivative of `b` accordingly. Again, this checks the pointwise relation; derivatives of (18) belong to the still-unchecked prolonged system.

## 4. Independent Weitzenböck check

At `p`, the terms involving `a` or `b` in a second differentiation of (4) vanish. Therefore

\[
\begin{aligned}
(\nabla^*\nabla\Omega)_p
&=-\sum_i(\nabla_{e_i}a)(e_i)\,\phi
  +\sum_i(\nabla_{e_i}(Ja))(e_i)\,J\phi\\
&=-4\phi.
\end{aligned}
\tag{19}
\]

From (14)–(15),

\[
W^+(\Omega)
=R(\Omega)-\frac{s}{12}\Omega
=\frac{s}{6}\Omega-2\phi.
\tag{20}
\]

The harmonic self-dual two-form identity, with nonnegative rough Laplacian, is

\[
0=\Delta_d\Omega
=\nabla^*\nabla\Omega+\frac{s}{3}\Omega-2W^+(\Omega).
\tag{21}
\]

Substitution gives, exactly,

\[
-4\phi+\frac{s}{3}\Omega
-2\left(\frac{s}{6}\Omega-2\phi\right)=0.
\tag{22}
\]

Thus the full vector-valued Weitzenböck relation, not merely its scalar contraction, is satisfied. The scalar contraction is also consistent with

\[
|\nabla\Omega|^2(p)=0,
\qquad |\Omega|^2=2.
\]

In this family, the trace-free part of the restriction of `W^+` to `Omega^perp` is zero. In the notation of the cited paper,

\[
W_3^+(p)=0.
\tag{23}
\]

This is a pointwise statement only. It does not meet hypotheses requiring `W_3^+=0` on an open set or everywhere.

## 5. Relation to the Nijenhuis zero index

On an almost-Kähler four-manifold, the intrinsic torsion and the Nijenhuis tensor determine one another by a fiberwise real-linear isomorphism. After choosing `phi`, formula (4) identifies the intrinsic-torsion fiber with the real four-dimensional space of one-forms `a`. Let

\[
\mathcal T_p:T_p^*M\longrightarrow E_p
\]

be the resulting isomorphism to whichever standard rank-two complex Nijenhuis bundle convention is used. If `a(p)=0`, then

\[
(\nabla N)_p=\mathcal T_p\circ(\nabla a)_p;
\tag{24}
\]

the derivative of `mathcal T` contributes no term because it multiplies `a(p)=0`.

For a realized transverse zero, its local index is the sign of the real determinant of `nabla N`, with the chosen base and bundle orientations. Accordingly

\[
\operatorname{ind}_p(N)
=\varepsilon_{\mathcal T}\,\operatorname{sgn}(1-t^2),
\qquad
\varepsilon_{\mathcal T}=\operatorname{sgn}\det_{\mathbb R}\mathcal T_p\in\{+1,-1\}.
\tag{25}
\]

The fixed sign `epsilon_T` depends on precise conventions for identifying the Nijenhuis bundle and its complex orientation. No value for that sign is needed here: the same fiber identification is used for `t=0` and `t=2`, so their formal indices are opposite regardless of that convention. A frame/gauge change likewise cannot remove the occurrence of both signs.

Equation (25) is conditional on realization when interpreted as an actual index. What the calculation itself proves is that both determinant signs pass the necessary first-layer jet identities.

## 6. What this establishes

The Euler-class obstruction `c_2(E)[M]=5 chi(M)+6 tau(M)` can force a zero of `N`, but a contradiction based on the signs of its zeros needs more than the first curvature and Weitzenböck identities. The family (7) leaves those identities and the scalar curvature unchanged while reversing the torsion derivative's determinant.

This calculation does not show that both signs occur in actual negative Einstein almost-Kähler germs. Such a statement would require compatibility at higher order and a local existence argument. It also does not rule out a global index theorem incorporating additional differential information.

## Primary references

1. V. Apostolov, J. Armstrong, T. Drăghici, *Local Rigidity of Certain Classes of Almost Kähler 4-Manifolds*, Annals of Global Analysis and Geometry **21** (2002), 151–176. Formulas (7)–(16), printed pp. 156–157. Full text: https://faculty.fiu.edu/~draghici/research/paperfiles/AGAG2.pdf . Retrieved browser source `turn803view0`, lines 228–311.
2. J. Armstrong, *Almost-Kähler Geometry*, Oxford DPhil thesis (1998), Proposition 1.2.6, printed pp. 18–19. Its zero-set invariance statement has an additional Weyl-component hypothesis; Einstein alone does not supply that hypothesis. Full text: https://johnarmstrongmaths.com/publications/resources/thesis.pdf . Retrieved browser source `turn805view0`, lines 1104–1198.

Prepared as an internal research calculation, 8 October 2026.
