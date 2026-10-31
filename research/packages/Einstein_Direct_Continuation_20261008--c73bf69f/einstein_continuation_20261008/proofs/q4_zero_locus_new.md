# Q4: what the torsion-zero route actually requires

## Result of this continuation

This note isolates a precise obstruction to the proposed zero-propagation proof of the closed negative Goldberg problem. It does **not** solve that problem. It gives (i) an exact Einstein specialization of the differential equation at a torsion zero; (ii) an actual analytic Ricci-flat family with torsion zeros of arbitrarily high finite order; and (iii) a negative-scalar algebraic-jet test showing why a zero-index argument cannot be obtained from the first curvature identities alone.

The user's explicit complete negative Einstein model and its nonexistence of pair-preserving finite-volume quotients are inherited from the preceding work; they are not repeated here.

## 1. The differential source surviving at a zero

Let `(M^4,g,J,Omega)` be almost Kähler, `|Omega|^2=2`, and `Ric=lambda g`. Set

\[
T=\nabla\Omega,\qquad q=|T|^2,\qquad L=\nabla^*\nabla,
\qquad \Psi=\operatorname{pr}_{\Omega^\perp}W^+(\Omega).
\]

The harmonic-form Weitzenböck identity and constant length give

\[
L\Omega=2W^+(\Omega)-\frac{s}{3}\Omega
       =2\Psi+\frac q2\Omega. \tag{1}
\]

Here `s=4lambda` is constant. The covariant derivative commutator has the form

\[
L(\nabla\Omega)-\nabla(L\Omega)
 =\operatorname{Rm}*\nabla\Omega+\nabla\operatorname{Ric}*\Omega,
\tag{2}
\]

with the indicated universal algebraic curvature action; the derivative-curvature contraction is zero for an Einstein metric by the contracted second Bianchi identity. Consequently, at every torsion zero `p`,

\[
\boxed{(LT)_p=2(\nabla\Psi)_p.} \tag{3}
\]

Indeed, all terms in (2) vanish at `T(p)=0`; differentiating (1), the terms `qT/2` and `dq tensor Omega/2` also vanish because `dq=2<T,nabla T>`. Moreover `nabla Psi` is perpendicular to Omega at such a point, since `<Psi,Omega>=0` identically.

This is also the Einstein specialization, at a zero, of Apostolov–Armstrong–Draghici's general identity (46)/(47), with `Psi=rho_*''`. The scalar-curvature sign contributes through terms proportional to `T`; these vanish at the zero. The source `nabla Psi` does not vanish merely from `div W^+=0`.

Thus the precise missing differential information is control of the **transverse self-dual Weyl component and its derivative**, rather than a scalar estimate on `q` alone. A putative homogeneous equation for `T` must prove the removal or absorption of this source.

For comparison, the third Gray condition adds `Psi=0` and `Ric''=0`; AAD Proposition 1 then obtains a homogeneous elliptic equation and strong unique continuation. Their Remark 1 explicitly distinguishes this from the stronger one-point propagation known under the different extra condition `Ric''=0, W_3^+=0`. Neither extra curvature condition follows from Einstein alone.

## 2. An exact family disproving sign-independent finite-jet propagation

Let `zeta=x+iy`, choose any integer `m>=1`, and set

\[
h(\zeta)=1+\zeta^{m+1}=w+iv.
\]

On a sufficiently small disk `D`, `w>0`. On `D x R^2`, with coordinates `(x,y,z,t)`, define

\[
\eta=dt+v\,dz,
\qquad
 g=w(dx^2+dy^2+dz^2)+w^{-1}\eta^2,
\qquad
 \Omega=w\,dx\wedge dy-dz\wedge dt. \tag{4}
\]

**Proposition.** The data in (4) are real analytic, positive definite and Ricci-flat almost Kähler. They are non-Kähler on every neighborhood meeting `zeta=0`. Their torsion vanishes precisely on `{zeta=0}`, and at every point of this two-dimensional set it has finite vanishing order `m`. In particular there is no universal finite order of torsion vanishing that forces local Kählerity for the full Einstein almost-Kähler class.

**Proof.** Cauchy–Riemann gives `dv=-w_y dx+w_x dy`, hence, for the Euclidean orientation `(x,y,z)`,

\[
 d\eta=*_{\mathbb R^3}dw.
\]

The standard Gibbons–Hawking triple

\[
 \eta\wedge dx-w\,dy\wedge dz,\qquad
 \eta\wedge dy-w\,dz\wedge dx,\qquad
 \eta\wedge dz-w\,dx\wedge dy
\]

is closed and orthonormal with norm squared two. It defines a hyperkähler metric, hence `Ric=0`. The form Omega in (4) has the opposite orientation, is closed, and has constant norm squared two, so it defines a second, almost-Kähler structure.

The coordinate Levi-Civita calculation gives exactly

\[
 |\nabla\Omega|^2
 =\frac{4(w_x^2+w_y^2)}{w^3}
 =\frac{4(m+1)^2|\zeta|^{2m}}
        {(1+\operatorname{Re}\zeta^{m+1})^3}. \tag{5}
\]

All coefficients are analytic and their denominators stay positive. Formula (5) proves both the exact zero set and the vanishing order, and positivity off the zero set proves nonintegrability there. The explicit coordinate check also independently computes the full Ricci tensor as zero. QED.

The executable `q4_gh_zero_check.py` derives Ricci and the covariant derivative of Omega from the coordinate metric with symbolic Cauchy–Riemann and harmonicity relations; all identities passed. This is an independent check, not the source of the proof.

This family belongs to the classical translation-invariant Gibbons–Hawking/AAD construction. Its use here is to test the proposed propagation mechanism, not a novelty claim for these metrics. It does not disprove a theorem that genuinely uses `s<0`, nor does it produce a complete or closed counterexample.

For `m=1`, (5) has a nonzero positive Hessian in the two normal directions at the zero set. For arbitrary `m`, all derivatives of `T` of orders below `m` vanish at a zero. Therefore:

* analyticity and a zero do not suffice;
* an arbitrary but fixed finite jet does not suffice uniformly over Einstein metrics;
* even a homogeneous elliptic equation has only the appropriate infinite-order unique-continuation consequence, not automatic one-point propagation.

## 3. A first-jet obstruction even with a prescribed negative Einstein scalar

Use an oriented orthonormal coframe and put

\[
 \Omega=e^{12}+e^{34},\quad
 \phi=e^{13}-e^{24},\quad
 \psi=J\phi=e^{14}+e^{23}.
\]

A standard almost-Kähler local expression is

\[
 \nabla\Omega=a\otimes\phi-Ja\otimes\psi.
\]

At a zero of `a`, choose

\[
 A_t=(\nabla_i a_j)
 =\operatorname{diag}(1+t,1-t,1,1). \tag{6}
\]

Then, for every `t`,

\[
 da=0,\qquad d(Ja)=2\Omega,\qquad \operatorname{tr}A_t=4.
\]

The Ricci identities for Omega are compatible with the same curvature operator

\[
 R_+=\begin{pmatrix}s/4&-2&0\\-2&0&0\\0&0&0\end{pmatrix},
 \quad R_-=\frac{s}{12}I,\quad R_{+-}=0, \tag{7}
\]

where `s<0` is arbitrary. Both chiral blocks have trace `s/4`, so this is an algebraic Riemann curvature tensor satisfying Bianchi; its zero mixed block is exactly the Einstein condition. Its action on Omega is

\[
 R(\Omega)=\frac{s}{4}\Omega-2\phi,
\]

so the harmonic-form equation at the zero gives `L Omega=-4phi`, matching the trace of (6). Nevertheless

\[
 \det A_t=1-t^2.
\]

Thus nondegenerate torsion-zero models with both signs survive these **necessary first-jet equations**, at the same negative scalar and the same algebraic curvature. A fixed fiber-orientation convention may reverse all signs, but cannot turn the two signs into one. The calculation even has `W_3^+(p)=0`; vanishing at one point is not the additional neighborhood identity used by the known theorem.

This is not a local existence assertion for the prolonged negative Einstein system. It proves that the first curvature identities cannot establish a fixed sign for all torsion-zero indices. The higher-order equations are exactly where a genuine obstruction would have to arise. Further details and an additional example with `W_3^+(p)!=0` are in `q4_zero_index_algebra.md`.

## 4. What remains a legitimate route to the closed problem

For a closed nonzero-scalar Einstein almost-Kähler four-manifold, Armstrong's Euler-class argument forces a torsion zero. The three computations above show precisely why this is not yet a contradiction.

A new zero-locus proof would have to establish at least one of the following genuinely new facts using the negative Einstein equation and compactness:

1. A homogeneous finite-type system for the coupled torsion/transverse-Weyl fields, whose admissible initial data are forced to vanish at the topologically required zero.
2. A sign or global count for torsion zeros derived from prolonged equations, rather than from (6)–(7).
3. A global integral or holonomy constraint that rules out the surviving zero configurations without asserting point propagation.

No such connection is established in this note. In particular, compactness cannot be replaced by completeness: the inherited complete negative example already excludes that replacement.

## Sources and exact scope

- Apostolov–Armstrong–Draghici, *Local models and integrability of certain almost Kähler 4-manifolds*, arXiv:math/0109098v2, §2.5, Proposition 1, equations (39)–(47), Remark 1; §3 for the classical local family. https://arxiv.org/pdf/math/0109098
- Apostolov–Armstrong–Draghici, *Local Rigidity of Certain Classes of Almost Kähler 4-Manifolds*, Ann. Global Anal. Geom. 21 (2002), 151–176, local connection/Ricci identities. https://faculty.fiu.edu/~draghici/research/paperfiles/AGAG2.pdf
- Armstrong, *Almost-Kähler Geometry*, doctoral thesis, Proposition 1.2.6 (printed pp18–19) and Theorem 2.2.4 (pp45–46). The former has an extra curvature hypothesis; the latter supplies a zero, not its propagation. https://johnarmstrongmaths.com/publications/resources/thesis.pdf

These sources establish the comparison theorems. Formulae (3), (5), and the explicit jet stress test are fully displayed so the remaining inference can be checked without appealing to a generic “unique continuation” label.
