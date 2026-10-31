# Rotating principal axes do not rescue the Berger spherical surgery core

22 September 2026. This note develops one previously untreated freedom in
the ordinary-point surgery proposal: arbitrary rotating axes in a
left-invariant three-sphere neck. It proves a finite-time obstruction to
that proposal, including an initial-radius-independent obstruction when
the error interval is tightened. It does not construct pointwise
near-Einstein metrics on the all-sign no-Einstein manifolds of Round 18.

## 1. What was already known, and the new statement

The installed Skill's `research/20260912.tex`, Chapter 3,
`FND:boundarymean` and `FND:varyingentropy`, already proves that a spherical
handle matching a hyperbolic ball of physical radius R, normalized by
Ric = -g, must have

\[
 \delta_-(g)>\operatorname{csch}^2(R/\sqrt3).
\]

It also already combines this with embedded hyperbolic ball volume to
obtain the necessary cover-size order chi >= const delta^(-3/2).
Neither bound is a new result of this round. Increasing the cover degree
does not solve the missing interior matching problem. The fixed-volume
AH gluing and exact free-circle obstructions in Rounds 9--10 are likewise
not constructions of that interior.

An actual proposed interior is the small Berger core of the same
Chapter 3. That manuscript excludes its biaxial and fixed-frame diagonal
triaxial continuations, and expressly leaves rotating principal axes
outside the conclusion. The theorem below closes this latter freedom.

Fix left-invariant one-forms sigma_i on SU(2), with dual fields satisfying
[E_i,E_j] = 2 epsilon_ijk E_k. Let

\[
 g=dt^2+G_{ij}(t)\,\sigma_i\sigma_j,\qquad 0\le t<L,
 \tag{1}
\]

where G is an arbitrary smooth positive-definite symmetric matrix.
No simultaneous diagonalization in a fixed frame is assumed. A
cohomogeneity-one invariant metric with a shift can be put in this
Gaussian form locally by its normal flow.

**Theorem 1 (small core, larger error interval).** Suppose 0 < A <= 1 and

\[
 G(0)=\operatorname{diag}\bigl(A^2(4+A^2),A^2,A^2\bigr),
 \qquad G'(0)=0,
 \qquad \|g^{-1}\operatorname{Ric}_g+I\|_{\infty,\mathrm{op}}
       \le\delta\le1.
 \tag{2}
\]

Let lambda_1 be the initially largest eigenvalue of G, measured relative
to the fixed bi-invariant reference form sum sigma_i^2. Then throughout
the positive-definite continuation,

\[
 \lambda_1(t)>A^2(4+A^2),\qquad
 \lambda_2(t),\lambda_3(t)<A^2\quad(t>0),
 \qquad L<\frac{11A}{5}.
 \tag{3}
\]

Here L denotes the maximal positive-definite smooth continuation; for a
metric specified only on an initial subinterval the conclusion is that
it cannot extend to time 11A/5 under the stated conditions. In particular,
rotating axes cannot connect this core to a round spherical interface
at any radius, including radii tending to infinity in larger covers.

**Theorem 2 (arbitrary initial radius).** For every A>0, the same initial
data in (2), with the tighter bound delta<=1/2, imply the same strict
long-axis growth and short-axis contraction, and

\[
 L<\frac{69}{8}.
 \tag{3a}
\]

In particular, allowing the initial radius A, the outer matching radius,
and the hyperbolic cover degree all to grow cannot rescue this precise
Berger initial family by rotating its axes. The time bound is uniform
in A. For A<=1 both theorems apply, so the smaller of their time bounds
can be used. Section 5 proves the scale-uniform extension separately.

The results allow all entries of G, all mixed Ricci components, arbitrary
bounded error fields with no derivative bounds, and eigenvalue crossings
of the two short axes. They retain left invariance and the explicit
initial data (2). Neither is an obstruction to arbitrary inhomogeneous
necks or to other initial second fundamental forms.

To compare with Round 18's normalization Ric = -3g, put h=g/3 and
a=A/sqrt(3). The physical initial radii become
(a sqrt(4+3a^2),a,a), the allowed error is
||h^(-1) Ric_h+3I|| <= 3, and the physical lifetime remains bounded by
11a/5. Rescaling the coordinate t alone would not make this conversion.
Theorem 2 instead gives error <=3/2 and physical lifetime
<69/(8 sqrt(3)), with no restriction on a>0.

## 2. The mixed equation controls the useful rotations

Let S be the shape operator of a slice, H = tr S, and write

\[
 E=\operatorname{Ric}_g+g.
\]

At any fixed time diagonalize G by an orientation-preserving
orthogonal change of the reference frame, and set

\[
 \lambda_i=a_i^2,\qquad e_i=E_i/a_i,\qquad
 [e_i,e_j]=c_k e_k,\qquad
 c_i=\frac{2a_i}{a_ja_k}.
 \tag{4}
\]

The intrinsic slice Ricci tensor is diagonal, with entries

\[
 r_i=\frac{2\bigl(a_i^4-(a_j^2-a_k^2)^2\bigr)}
              {a_1^2a_2^2a_3^2}.
 \tag{5}
\]

Codazzi and the spatially constant H give, up to the immaterial common
sign determined by the normal convention,

\[
 \operatorname{Ric}(\partial_t,e_i)=(c_k-c_j)S_{jk}.
 \tag{6}
\]

For completeness, the divergence calculation is
(div S)_i = -sum_(j,k) Gamma_(ji)^k S_(kj); the two possibly nonzero
connection coefficients sum to c_j-c_k. Thus (6) uses the physical
orthonormal mixed components, not coordinate components or a presumed
conserved charge.

Consider the cone

\[
 X:=a_1^2\ge(4+A^2)A^2,
 \qquad Y:=a_2^2\le A^2,\quad Z:=a_3^2\le A^2.
 \tag{7}
\]

Its long eigenline is uniformly separated from the short two-plane.
Let u = (S_12,S_13), let B be the restriction of S to this short plane,
and put

\[
 D=\operatorname{diag}\left(\frac{X+Y}{X-Y},
                            \frac{X+Z}{X-Z}\right).
 \tag{8}
\]

In (7),

\[
 c_1-c_\alpha\ge\frac3A\quad(\alpha=2,3),\qquad
 1<D\le\frac53 I.
\]

The entire mixed row of an operator of norm <= delta has Euclidean
norm <= delta. Applying (6) to the two long-short entries consequently
gives

\[
 |u|\le\frac{\delta A}{3}.
 \tag{9}
\]

The first inequality above follows from
2(X-A^2)/(sqrt(X) A^2) >= 3/A for X >= 4A^2. Unlike separate
entrywise estimates, (9) does not acquire a factor sqrt(2).

## 3. A matrix cone preserved despite rotating axes

In a parallel orthonormal frame along the normal,

\[
 \nabla_t S=\operatorname{Ric}_{\mathrm{slice}}+I-HS-E_T,
 \qquad H'=1-E_{00}-|S|^2.
 \tag{10}
\]

Pass to an orthonormal frame following the long eigenline of G. The
long-short frame angular velocity has components D u. This can be
checked by differentiating G's eigenvector equation: if i != j, its
contribution to the derivative of S_ii is

\[
 2\frac{\lambda_i+\lambda_j}{\lambda_i-\lambda_j}S_{ij}^2.
 \tag{11}
\]

Therefore the short block equation, apart from an internal short-frame
commutator, is

\[
 B'=\operatorname{Ric}_{\mathrm{short}}+I-HB-E_{\mathrm{short}}
            -u(Du)^T-(Du)u^T.
 \tag{12}
\]

The internal commutator has zero trace and zero quadratic form on a null
eigenvector of B. The last two terms in (12) need not be a negative
semidefinite matrix. Keeping their possible positive part is essential:
they obey

\[
 \|u(Du)^T+(Du)u^T\|_{\mathrm{op}}
 \le 2\|D\||u|^2
 \le\frac{10\delta^2A^2}{27}.
 \tag{13}
\]

On the cone (7), formula (5) gives

\[
 r_1>0,\qquad
 r_2\le-\frac{4+2A^2}{Y},\qquad
 r_3\le-\frac{4+2A^2}{Z}.
 \tag{14}
\]

Here is an algebraic verification of the middle inequality. Set q=4+A^2.
After multiplication by the positive factor XYZ/2 it is equivalent to

\[
 X^2-qXZ+Z^2-Y^2\ge0.
\]

The left side increases with X on (7), and is bounded below by
(A^2-Z)(q^2 A^2-A^2-Z) >= 0 after setting X=q A^2 and Y=A^2.
The other short-axis inequality is identical with Y and Z interchanged.

Write x_1=S_11. At a boundary x_1=0, equations (10)--(11) give

\[
 x_1'=r_1+1-E_{11}+2u^TDu>0.
 \tag{15}
\]

At a first null eigenvector w of B, equations (12)--(14) instead give

\[
 \langle B'w,w\rangle
 \le-\frac{4+2A^2}{A^2}+1+\delta
            +\frac{10\delta^2A^2}{27}
 \le-\frac4{A^2}+\frac{10A^2}{27}<0.
 \tag{16}
\]

Initially S=0; the same strict inequalities show that x_1>0 and B<0
immediately for positive time. Equations (15)--(16) prevent a first
exit. They in turn imply that the long eigenvalue increases and both
short eigenvalues decrease, so (7) itself cannot fail. This is a
closed barrier argument; no assumption on the smallness of a rotation
rate is substituted for the mixed equation.

The short eigenvalues may coincide. The long spectral projection and
its complementary two-plane remain smooth, so B and the matrix barrier
are well-defined through such coincidences. A choice of individual
short eigenvectors is used only to evaluate invariant expressions at
one time.

## 4. A smooth scalar collapse estimate

Use the geometric mean of the two short radii,

\[
 b=\sqrt{a_2a_3}
   =\left(\frac{\det G}{\lambda_1}\right)^{1/4},
 \qquad z=\frac{b'}b=\frac12\operatorname{tr}B.
 \tag{17}
\]

This quantity is smooth even at crossings of the short eigenvalues.
It satisfies 0 < b <= A and b'<0 for positive time. Taking the trace
in (12) is particularly effective: the rotation term is now exactly
-2u^TDu <= 0. The arithmetic-geometric mean inequality and (14) give

\[
 z'\le-\frac{4+2A^2}{b^2}+1+\delta-Hz.
\]

Consequently, since delta<=1 and b<=A,

\[
 b''\le-\frac4b-Hb'+\frac{(b')^2}{b}.
 \tag{18}
\]

The normal equation in (10) gives

\[
 H'\le2-H^2/3,\qquad H(0)=0,
 \qquad H<\sqrt6.
 \tag{19}
\]

Putting v=-b'>0 in (18) yields

\[
 v'\ge\frac{4-v^2}{b}-\sqrt6\,v.
 \tag{20}
\]

As long as v<=1/2,

\[
 v'\ge\frac{15}{4A}-\frac{\sqrt6}{2}
      >\frac{5}{2A}.
\]

Thus, unless positive-definite continuation ends earlier, v reaches
1/2 at some tau<A/5. Equation (20) prevents a subsequent crossing
back below 1/2. Since b(tau)<A, positivity of b ends before another
2A units of time. This proves L<11A/5 and the theorem.

All three types of Ricci equation have a distinct role: the mixed
equation bounds harmful rotation, the tangential equation preserves
the short-block cone, and the normal equation bounds H. Omitting any
one of them would leave the proposed rotating escape untested.

## 5. A uniform obstruction when the initial radius grows

We now allow every A>0 and assume delta<=1/2. Retain q=4+A^2 and
the cone (7). The geometric and algebraic identities (4)--(12) and
(14)--(15) do not require A<=1. Replace the small-core estimate (9)
by the sharper scale-uniform observation

\[
 c_1-c_\alpha\ge\frac{2(q-1)}{A\sqrt q}>2,
 \qquad (q-1)^2-A^2q=2A^2+9>0.
 \tag{21}
\]

The mixed equation and the still-valid D<=5I/3 now give

\[
 |u|\le\frac\delta2,\qquad
 \|u(Du)^T+(Du)u^T\|_{\mathrm{op}}
       \le\frac{5\delta^2}{6}.
 \tag{22}
\]

Consequently, at a first null eigenvector of the short block,

\[
 \langle B'w,w\rangle
 \le-2-\frac4{A^2}+1+\delta+\frac{5\delta^2}{6}
 \le-\frac4{A^2}-\frac7{24}<0.
 \tag{23}
\]

The long-axis barrier (15) is again strict. The same first-exit argument
therefore preserves x_1>0, B<0 and the cone for every A>0. This alone
already excludes a round interface. To get a uniform time bound, keep
the improved normal estimate and the unused intrinsic-curvature term:

\[
 H<\sqrt{3(1+\delta)}\le\frac3{\sqrt2},
 \qquad
 b''\le-\frac{C_A}{b}-Hb'+\frac{(b')^2}{b},
 \quad C_A=4+\frac{A^2}{2}.
 \tag{24}
\]

Indeed, before simplifying the tangential equation, its numerator is
4+2A^2-(1+delta)b^2, which is at least C_A since b<=A.
Thus v=-b'>0 satisfies

\[
 v'\ge\frac{C_A-v^2}{b}-\frac3{\sqrt2}v.
 \tag{25}
\]

For v<=A/8, the numerator is positive, so b<=A yields

\[
 v'\ge\frac4A+
 \left(\frac{31}{64}-\frac3{8\sqrt2}\right)A
 >\frac A5.
 \tag{26}
\]

The strict coefficient comparison follows, for example, from
(91/320)^2-9/128=1081/102400>0. Unless continuation ends earlier,
v reaches A/8 before time 5/8; (25) prevents crossing back below this
value. Since b<A thereafter, positivity ends within fewer than eight
further units of physical t-time. This proves L<69/8. No attempt to
optimize this universal constant is needed for the stated exclusion.

## 6. Consequence for the growing-cover proposal

One concrete proposal was to take the Einstein-compatible Berger
throat, rotate its principal axes to avoid the fixed-frame singularity,
then match to increasingly large round hyperbolic spheres in finite
covers. Theorems 1--2 rule out its middle step, with a gap uniform in
the cover degree and the proposed outer radius. For A<=1, continuation
in the Ricci interval [-2,0] ends before time 11A/5. For arbitrary A>0,
continuation in [-3/2,-1/2] ends before time 69/8. In either case a
successful construction must change the stated initial family or leave
the homogeneous setting; increasing the waist size within this family
does not furnish an escape.

This is a failure of a specific expanded geometric construction, not
a new necessary-condition list for arbitrary Yau26 inputs. Its initial
data are compatible with an exact Einstein germ; the conclusion is a
global continuation obstruction for that germ and all the indicated
bounded-error rotating continuations.

The all-sign obstructions for N_j#(S^1 x S^3) and N#N remain valid.
No pointwise near-Einstein input on those smooth types is constructed
here. A different throat or an inhomogeneous construction remains
unresolved. The generalized Dehn-filling theorems do not fill this
specific gap: they attach D^2 x T^(n-2) at torus cusp boundaries, rather
than the spherical handle in this note; see the topology specified at
the start of [Bamler's primary paper](https://arxiv.org/abs/0911.4730).
Likewise [Mazzeo--Pacard](https://arxiv.org/abs/math/0211099) proves a
boundary connected-sum theorem for conformally compact metrics, not
this compact interior spherical surgery theorem.

`round19_surgery_check.py` checks the Codazzi coefficient, intrinsic
Ricci formula, rotating-frame correction, invariant-cone algebra and
constants, including the arbitrary-radius extension. These are exact
finite algebraic checks. The barrier and
finite-time proof above, not test output, establish the theorem.
