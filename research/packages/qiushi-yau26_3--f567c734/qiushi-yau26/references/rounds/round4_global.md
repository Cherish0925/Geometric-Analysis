# A full-matrix Nil obstruction and the limits of radial charge escape

20 September 2026. The `qiushi-yau26` Skill was reread in full and its
existing Gaussian, torus, helical and Nil reductions were checked against
the round-two and round-three connector notes. The new result below is a
global obstruction for arbitrary time-dependent Heisenberg orbit matrices.
It uses the tangential equations and remains valid with central-direction
mixing. It does not settle the unrestricted two-dimensional twisted-T2
connector problem.

## 1. Geometry and hypotheses

Fix the three-dimensional Heisenberg Lie algebra with basis `X_1,X_2,Z`
and bracket `[X_1,X_2]=Z`. Let `sigma^1,sigma^2,sigma^3` be the dual
left-invariant coframe, descending to a fixed compact lattice quotient
`P=Gamma\Nil_3`. Consider

\[
 g=dt^2+G_{ij}(t)\sigma^i\sigma^j,
 \qquad G(t)>0,
\tag{1}
\]

where `G` is an arbitrary smooth positive-definite symmetric matrix.
There is no diagonal assumption, no reflection center, and no fixed
eigenbasis for `G(t)`.
The compact slices are locally homogeneous. The Heisenberg action is
isometric and transitive on each universal-cover slice; no transitive
global isometry action on the compact lattice quotient is asserted.

Write `q_t=G_ij sigma^i sigma^j`, and define

\[
 S=\tfrac12G^{-1}G',\quad H=\operatorname{tr}S,
 \quad v=\sqrt{\det G},\quad \ell^2=q_t(Z,Z),\quad e_Z=Z/\ell,
\]
\[
 \mu=\frac{\ell^4}{2v^2}>0,\qquad
 \chi=\log\ell^2-\log v=\tfrac12\log(2\mu).
\tag{2}
\]

The fixed lattice changes the total orbit volume by a constant factor,
which cancels from `H=v'/v` and the argument. The normalization of `mu`
uses the stated Lie bracket, not a freely adjustable physical covolume.

Fix `lambda>0`, set `E=Ric_g+lambda g`, and assume

\[
 \|g^{-1}E\|_{\infty,\mathrm{op}}\le\epsilon.
\tag{3}
\]

The connector normalization is `lambda=3`. The theorem is stated with
`lambda` to make its scaling content explicit.

## 2. The invariant slice Ricci tensor

For every positive-definite `G`, choose a `q_t`-orthonormal horizontal
pair `e_1,e_2` perpendicular to the central direction `e_Z`. Their bracket
has the form

\[
 [e_1,e_2]=\beta e_Z,
 \qquad \beta=\ell^2/v,\qquad \mu=\beta^2/2.
\]

Indeed the determinant of `(e_1,e_2,e_Z)` in the fixed Lie-algebra basis
is `1/v`, whereas its central column is `Z/ell`; hence the determinant
of the two horizontal coefficients in the bracket is `ell/v`.
The Koszul formula then gives the slice sectional curvatures

\[
 K(e_1,e_2)=-3\beta^2/4,
 \qquad K(e_1,e_Z)=K(e_2,e_Z)=\beta^2/4.
\]

Consequently, invariantly,

\[
 \operatorname{Ric}_{q_t}^{\sharp}
      =\mu(2P_Z-I),\qquad R_{q_t}=-\mu,
 \qquad P_Z=e_Z\otimes e_Z^\flat.
\tag{4}
\]

This calculation is valid for the full matrix `G`, including nonzero
entries mixing the fixed central basis vector with the other vectors.

## 3. A tangential maximum principle with the full mixing term

The Gaussian equations, in the fixed Lie-algebra frame, are

\[
 S'=\operatorname{Ric}_{q_t}^{\sharp}+\lambda I-HS-E_T^\sharp,
\qquad
 H'+H^2=3\lambda-\mu-\operatorname{tr}E_T,
\tag{5}
\]

\[
 E_{00}=\lambda-H'-|S|^2,
\qquad
 R_{q_t}=-2\lambda+H^2-|S|^2
                        +\operatorname{tr}E_T-E_{00}.
\tag{6}
\]

The mixed Codazzi components of Ricci need not vanish for a general
matrix. They are not set to zero here: the theorem is a necessary
consequence of the normal and tangential components of the full bound
(3), so an additional mixed equation cannot invalidate the obstruction.

Put

\[
 r=(\log\ell)'=\langle Se_Z,e_Z\rangle,
 \qquad W=Se_Z-r e_Z.
\]

Differentiating the moving normalized central vector is essential. Since
`G'=2GS` and the coordinate derivative of `e_Z` is `-r e_Z`,

\[
 r'=\langle S'e_Z,e_Z\rangle
          +2\bigl(|Se_Z|^2-r^2\bigr)
    =\langle S'e_Z,e_Z\rangle+2|W|^2.
\tag{7}
\]

Equivalently, in the four-dimensional connection
`nabla_(partial_t)e_Z=W`, giving the same formula. Equations (4)--(5)
therefore imply

\[
 r'+Hr=\lambda+\mu-E_{ZZ}+2|W|^2.
\]

Because `chi'=2r-H`, subtracting the trace equation gives the new identity

\[
 \boxed{\quad
 \chi''+H\chi'
 =-\lambda+3\mu+
     (\operatorname{tr}E_T-2E_{ZZ})+4|W|^2.
 \quad}
\tag{8}
\]

Here `E_ZZ=E(e_Z,e_Z)`. In an orthonormal frame containing `e_Z`,

\[
 \operatorname{tr}E_T-2E_{ZZ}=E_{11}+E_{22}-E_{ZZ},
\qquad |\operatorname{tr}E_T-2E_{ZZ}|\le3\epsilon.
\]

Thus at any interior positive maximum of `mu` (equivalently, a maximum
of `chi`),

\[
 \mu\le\lambda/3+\epsilon-\tfrac43|W|^2
       \le\lambda/3+\epsilon.
\tag{9}
\]

Off-diagonal central mixing has a favorable sign. Dropping it weakens
the estimate; introducing it cannot provide an escape from this maximum
principle.

## 4. A finite-band obstruction and its complete two-end consequence

**Theorem 1 (full-matrix Nil band).** Suppose (1)--(3) hold on `[a,b]`,
and `H(a)<0<H(b)`. Write `mu_boundary=max(mu(a),mu(b))`. Then

\[
 \boxed{\quad
 2\lambda-4\epsilon
       \le\max\{\mu_{\rm boundary},\lambda/3+\epsilon\}.
 \quad}
\tag{10}
\]

**Proof.** The maximum of `mu` is either on the boundary or is subject
to (9). On the other hand, `H` has a zero `t_0`. At this same actual
metric's zero, (4) and the scalar constraint (6) give

\[
 \mu(t_0)=2\lambda+|S(t_0)|^2
                       -\operatorname{tr}E_T(t_0)+E_{00}(t_0)
             \ge2\lambda-4\epsilon.
\]

Combining the two inequalities proves (10). There is no bound on the
length of the interval, on the orbit volume, or on the variation of its
lattice-normalized shape. QED.

**Corollary 2 (two expanding ends).** Suppose (1)--(3) hold on the whole
line, with

\[
 v(t)\longrightarrow\infty,\qquad
 \mu(t)\longrightarrow0\qquad(t\to\pm\infty).
\tag{11}
\]

Then

\[
 \boxed{\epsilon\ge\lambda/3.}
\tag{12}
\]

In particular the defect from `Ric=-3g` is at least `1`.

Indeed `v` has an interior global minimum, so `H=0` there. The positive
function `mu` attains its global maximum in the interior because of (11).
The two inequalities in the preceding proof yield
`2lambda-4epsilon<=lambda/3+epsilon`, which is (12).

The hypotheses follow, for example, from isotropically expanding Nil
ends `G(t)=e^{2c|t|}G_+-` outside a compact interval, for any `c>0`:
`v` grows like `e^{3c|t|}` and `mu` decays like `e^{-2c|t|}`.
The same conclusions hold under comparable asymptotic limits. The
end hypotheses are explicitly about both orbit volume and bracket scale;
volume expansion alone does not imply the second limit.

The fixed-center diagonal periodic obstruction in the existing Skill did
not give this result: it integrated `(v f_3)'` on a circle. Here the
interval may be arbitrarily long, there is no periodic time variable,
and both full orbit matrices and nonzero central mixing are allowed.
The mechanism combines an upper bound for physical slice curvature from
the tangential equation with its lower bound at a volume minimum.

This does not rule out all complete negative Einstein Nil models. The
retained exact cusp, in normalization `lambda=1`, is

\[
 a_1=a_2=e^{t/\sqrt6},\qquad
 a_3=\sqrt{2/3}\,e^{2t/\sqrt6},\qquad \mu=1/3.
\]

It has one shrinking and one expanding volume direction, and constant
`mu`; it fails both two-ended hypotheses (11). Substitution verifies all
its Ricci components and is included as a sign check.

## 5. Every purely radial torus-charge ansatz is already excluded

For comparison, consider the most general radial Kaluza--Klein form on
an interval times a fixed marked three-torus:

\[
 g=N(r)^2dr^2+a(r)^2(ds+B(r)dr)^2
 +G_{ab}(r)(d\xi^a+A_s^a(r)ds+A_r^a(r)dr)
                  (d\xi^b+A_s^b(r)ds+A_r^b(r)dr).
\tag{13}
\]

All coefficients depend only on `r`; the two torus fibre directions may
mix fully. The change

\[
 \widetilde s=s+\int B(r)dr,
\qquad
 \widetilde\xi^a=\xi^a+\int(A_r^a-A_s^aB)dr,
\qquad dt=N(r)dr
\]

preserves the fixed torus lattice and yields `g=dt^2+q_ij(t)dy^i dy^j`.
Every three-dimensional slice is flat. This class includes nonzero
connection curvature `F^a=(A_s^a)'dr wedge ds` and changing flat
holonomies. Twist alone does not take a radial ansatz outside the
flat-slice class.

At a volume minimum the scalar constraint becomes

\[
 0=-2\lambda-|S|^2+\operatorname{tr}E_T-E_{00}.
\]

Consequently any such two-expanding-end model has

\[
 \epsilon\ge\lambda/2,
\tag{14}
\]

or at least `3/2` in the connector normalization. This is the existing
flat-slice obstruction applied to the complete radial charge class,
rather than a new constant. It shows that the earlier scalar redshift
countermodel cannot be completed merely by adding arbitrary radial
orbit shape, base circumference, lapse, or off-diagonal connection data.
Any successful free-T2 connector must use genuine dependence on both
quotient variables, or leave that symmetry/topology class.

## 6. Physical lattice and topology boundaries

A compact Heisenberg lattice quotient is not a three-torus. Its lattice
contains generators `x,y,z` with `z` central and `[x,y]=z^m`, `m!=0`.
Every finite-index subgroup contains positive powers of `x` and `y`;
their commutator is a nonzero power of the infinite-order element `z`.
Thus no such subgroup is abelian, whereas every finite cover of `T^3`
has fundamental group `Z^3`. A finite cover cannot identify these end
manifolds. Taking the physical bracket scale `mu` to zero by collapse
does not change this integral obstruction.

The Nil theorem is therefore a restriction on a potential homogeneous
degeneration model, not a replacement of a torus end by a Nil end. It
also excludes any finite full-matrix Nil band with expanding volume in
both outward directions and boundary bracket scales below the threshold
in (10). A passage through more general inhomogeneous transition regions
is additional mathematics and is not prohibited by this proof alone.

Both obstructions are independent of cover degree, interval length and
lower covolume. Neither produces a positive connector-volume bound, and
neither licenses closing an expanding end into a fixed closed manifold.
The fixed-topology volume and peripheral matching restrictions from the
prior rounds remain in force.

## 7. Verification and remaining question

`round4_global_check.py` derives the intrinsic Heisenberg Ricci tensor
from the Koszul formula, verifies the full moving-central-direction
identity with arbitrary symmetric shape and shape-derivative matrices,
checks the scalar constraint and both gap constants, and verifies the
known exact Nil cusp. The general theorem is proved by the invariant
calculation above; symbolic checks are not promoted to an existence or
classification theorem.

The full twisted free-T2 cylinder with two exact hyperbolic torus ends
remains unresolved here. There is no constructed vanishing-defect family
and no cover-independent gap for all such metrics. The new conclusion
is that neither a full radial charge transport completion nor a full
matrix homogeneous Nil band provides the required escape. The permitted
two-variable orbit geometry remains a real possibility to investigate.
