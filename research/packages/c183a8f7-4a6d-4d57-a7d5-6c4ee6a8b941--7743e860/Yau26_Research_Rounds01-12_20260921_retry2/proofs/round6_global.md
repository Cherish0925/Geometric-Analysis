# Charged Einstein necks and actual collapse mechanisms

20 September 2026.

The general complete two-ended connector problem remains open. This note
constructs an actual analytic, charged, two-variable Einstein neck on a
neighborhood of T³, with a strictly stable minimal central torus and positive
sectional curvature. It also constructs complete one-ended metrics with an
exact expanding hyperbolic end and uniformly vanishing Ricci error, whose
Weyl and twist peaks collapse in physical volume. Both constructions solve
all Ricci blocks in their stated domains.

The first is a local existence theorem, not a formal Taylor solution. The
second is a global metric construction on D²×T², not on R×T³. Neither is
asserted to supply the missing complete two-ended connector. Together they
exclude purely local curvature/support-volume arguments for closing the
round-5 gap.

## 1. An analytic charged neck on the correct local topology

We use the convention K=(1/2)∂_t h_t for the second fundamental form of
the slices of g=dt²+h_t. Thus the outward mean curvature on t>0 is
H=tr K. Fix a>0 and a nonzero constant covector q∈R². For θ modulo π set

\[
 R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\
                         \sin\theta&\cos\theta\end{pmatrix},\qquad
 M(\theta)=R_\theta
             \begin{pmatrix}e^a&0\\0&e^{-a}\end{pmatrix}R_\theta^T,
 \qquad Q_0(\theta)=\tfrac12q^TM(\theta)^{-1}q.
 \tag{1.1}
\]

This is a closed analytic loop of positive determinant-one matrices. Let

\[
 b(\theta)=\frac{2\sinh a}{\sqrt{12+2Q_0(\theta)}}.
 \tag{1.2}
\]

On the actual product T³=(R/πZ)×(R/Z)² prescribe

\[
 h=b^2d\theta^2+M_{ab}d\xi^a d\xi^b,
 \qquad K_{\theta a}=K_{a\theta}=\tfrac12 b q_a,
 \qquad K_{\theta\theta}=K_{ab}=0.
 \tag{1.3}
\]

These coefficients are periodic in fixed coordinates. The rotating real
matrix in (1.1) is a varying metric, not a lattice change or a nonintegral
identification of the torus.

**Theorem 1.1.** The data (1.3) extend to an analytic metric

\[
 g=dt^2+h_t\quad\text{on }(-\tau,\tau)\times T^3,
 \qquad \operatorname{Ric}(g)=-3g,
 \tag{1.4}
\]

for some τ>0. The metric admits a free isometric T² action in the ξ
coordinates. Its quotient is a genuine annular neighborhood, its conserved
coordinate charge is q, and at the central torus:

\[
 \rho=1,\quad d\rho=0,\quad Q=Q_0,\quad
 |dU|^2=12+2Q_0,
 \tag{1.5}
\]

\[
 H=0,\quad \partial_tH=3-Q_0,\quad
 K_g(T\!\cdot T^2)=3+\tfrac12Q_0>0.
 \tag{1.6}
\]

Here K_g(T·T²) means the sectional curvature of the orbit tangent plane.
If max Q_0<3, the central T³ is strictly stable minimal, and all sufficiently
nearby slices on both sides have positive outward mean curvature.

### Proof: every constraint, followed by actual analytic existence

Use local arclength ds=b dθ on the base circle. Then h=ds²+M(s)dξ² and
K_{sa}=q_a/2. The determinant-one condition gives tr(M^{-1}M_s)=0. For
the shape normalization e=(1/2)tr((M^{-1}M_s)²), direct differentiation of
(1.1) gives

\[
 e=4\sinh^2(a)/b^2=12+2Q_0.
 \tag{1.7}
\]

The flat torus slices inside (T³,h) have shape
S=(1/2)M^{-1}M_s, with tr S=0 and |S|²=e/2. Their scalar Gauss formula
therefore gives

\[
 R_h=-|S|^2=-e/2=-6-Q_0.
 \tag{1.8}
\]

Meanwhile, the tensor K in (1.3) satisfies

\[
 H=0,\qquad |K|_h^2=\tfrac12q^TM^{-1}q=Q_0.
 \tag{1.9}
\]

The momentum constraint is also exact. The horizontal component of div K
is zero because K has only horizontal–vertical entries. For a torus
translation X_a=∂_{ξ^a}, its Killing identity gives

\[
 (\operatorname{div}K)(X_a)
  =\operatorname{div}(K(X_a,\cdot)^\sharp)
  =\partial_s(q_a/2)=0,
\]

where det M=1 supplies the constant s-volume density. Equivalently, in
the θ coordinate the flux is b K^θ{}_a=q_a/2. Thus

\[
 \operatorname{div}(K-Hh)=0,\qquad
 R_h+|K|^2-H^2=-6.
 \tag{1.10}
\]

These are precisely the Riemannian contracted Codazzi and Gauss constraints
for Ric_g=−3g in dimension four. All data are real analytic. Koiso's
analytic Einstein Cauchy theorem, Proposition 6, or its formulation in
Ammann–Moroianu–Moroianu, Theorem 2.1, therefore gives a unique actual
analytic germ in Gaussian coordinates. Their Weingarten convention is
W=−h^{-1}K (Koiso's bilinear form is α=−K), so the sign of
the prescribed first derivative agrees after that substitution. Compactness
of the initial T³ gives one positive τ on the whole torus. Uniqueness
preserves the ξ-translations and their free action.

This theorem is analytic and local. No well-posedness claim for arbitrary
smooth Riemannian Cauchy data, nor any continuation to infinite distance,
is being used.

In fact this charged germ cannot extend as an exact Einstein metric to even
one exact hyperbolic end for the same free T² action: the mixed equation
forces q to be constant on the connected quotient, whereas such an end
has q=0. A successful global near-Einstein construction must therefore
introduce a nonzero mixed Ricci residual somewhere and control the entire
transition, not just continue the analytic solution.

### Charge, curvature and stability of the resulting metric

Put the resulting metric in the full Kaluza–Klein form

\[
 g=\gamma+G_{ab}(d\xi^a+\mathcal A^a)(d\xi^b+\mathcal A^b),
 \quad G=\rho M,\quad \det M=1.
\]

The Gaussian gauge has A_t=0. Initially A_θ=0 and

\[
 \partial_t\mathcal A_\theta=bM^{-1}q.
\]

With base orientation dt∧dθ and area density b at t=0, its curvature
coefficient is f=M^{-1}q. Hence the geometric charge ρGf equals exactly
q, and Q=(1/2)f^TGf equals Q_0. The Einstein mixed equation conserves
this same charge throughout the connected local cylinder. Thus the mixed
block is not merely a constraint imposed at one slice.

The initial vertical block K_ab=0 gives ∂_tρ=0 and ∂_tU=0; det M=1
gives ∂_θρ=0. Consequently the full vertical trace equation yields

\[
 \partial_t^2\log\rho=6+Q_0.
\]

The normal Ricci equation Ric(∂_t,∂_t)=−∂_tH−|K|² gives H'=3−Q_0.
In particular the quotient base curvature at the central circle is
K_γ=3+2Q_0, in agreement with the horizontal Ricci block. No orbit-shape
or connection term has been discarded.

The orbit is intrinsically flat. Inside h its two principal curvatures
are opposite, and −det S=e/4. Moreover K vanishes on two vertical
arguments, so the hypersurface Gauss equation introduces no further
correction on that plane. Therefore

\[
 K_g(T\!\cdot T^2)=-\det S=e/4=3+Q_0/2.
\]

Finally the second variation of the central minimal T³ is

\[
 I(\varphi,\varphi)
   =\int_{T^3}\bigl(|\nabla\varphi|^2+(3-Q_0)\varphi^2\bigr)dV_h.
 \tag{1.11}
\]

If max Q_0<3, it is uniformly positive. The expansion statement follows
from H(0)=0 and H'(0)>0; the outward normal on t<0 is −∂_t.

### A fully explicit periodic choice

Take a=log 2 and q=(1,0). Then

\[
 M(\theta)=\tfrac14
  \begin{pmatrix}5+3\cos2\theta&3\sin2\theta\\
                  3\sin2\theta&5-3\cos2\theta\end{pmatrix},
 \quad Q_0=\frac{5-3\cos2\theta}{8},\quad
 b^2=\frac9{53-3\cos2\theta}.
 \tag{1.12}
\]

Thus 1/4≤Q_0≤1, the stability potential is at least 2, and the orbit
sectional curvature lies between 25/8 and 7/2. The twist peak already
exceeds the limiting necessary threshold from round 2. The shape loop is
nonconstant on the actual base circle, so this is not a disguised radial
flat-slice ansatz.

## 2. What local support-volume control cannot say

Shrink τ in Theorem 1.1 once, if necessary. For the fixed data (1.12),
there is a fixed closed collar |t|≤τ_0 on which the orbit sectional
curvature is at least 2 and Q is bounded below by a positive constant.
All curvature derivatives on that collar are bounded. Divide the two
fibre circles by the free order-N subgroup in each factor. The resulting
metric g_N is a smooth exact Einstein metric on the same local smooth
type [−τ_0,τ_0]×T³. It has the same local curvature, charge equations,
normal width and stability bound, but

\[
 \operatorname{Vol}(g_N)=N^{-2}\operatorname{Vol}(g_1)\longrightarrow0.
 \tag{2.1}
\]

This is a real finite quotient, with its actual changed physical period
lattice; it is not an affine-coordinate dilation. A ball of any sufficiently
small fixed radius centered on the middle torus lies in the collar and has
volume at most the right side of (2.1), while Ric=−3g and the positive
sectional/twist conditions hold there.

Therefore exact Einstein equations, bounded curvature and its derivatives,
positive sectional curvature, nonzero charge, local annular topology and
a stable minimal torus do not give a positive, cover-independent physical
support-volume bound. A proof for complete exact-ended connectors must use
global end information or a scale-/orbit-normalized quantity. This result
does not exclude such a genuinely global support theorem.

## 3. A complete one-ended, all-block redshift construction

The following separate construction realizes small-defect charge removal
and concentration globally, while explicitly retaining the wrong end
topology for the main question.

Let χ:[0,∞)→[0,1] be smooth, equal to 1 on [0,1], equal to 0 on [2,∞),
and nonincreasing. For R≥2 and r≥1 define

\[
 m_R(r)=\chi(r/R),\quad V_R(r)=r^2-\frac{m_R(r)}r,
 \quad g_R=\frac{dr^2}{V_R}+V_Rd\vartheta^2+r^2(dx^2+dy^2).
 \tag{3.1}
\]

Take ϑ and x to have period P=4π/3 and y to have period 1. At r=1 the
ϑ-circle closes smoothly, since V_R'(1)=3. The result is complete on
D²×T², with a free T² action below. For r≥2R it is exactly hyperbolic,
with outward coordinate t=log r. For 1≤r≤R it is the exact toral
Einstein black hole of mass one.

**Proposition 3.1.** The full Ricci-error eigenvalues of (3.1) are

\[
 p_R=\frac{m_R''}{2r}\quad\text{twice},\qquad
 z_R=\frac{m_R'}{r^2}\quad\text{twice}.
 \tag{3.2}
\]

Consequently ||Ric+3g||_op≤C_χ R^{-3} globally, with error supported in
R≤r≤2R. This is an unweighted pointwise estimate for the entire Ricci
endomorphism.

**Proof.** The two normal/ϑ Ricci eigenvalues are −V''/2−V'/r, and the
two x/y eigenvalues are −V'/r−V/r². Substitution of V=r²−m/r gives (3.2).
Smoothness at the bolt and exactness of the exterior are unchanged by the
cutoff. In particular no seam or unspecified Einstein repair is involved.

For an integer c≥1, choose the free torus generators ∂_x+c∂_ϑ and ∂_y.
The x and ϑ periods are both P, so this is an integral, closed torus
subgroup; an arbitrary irrational slope is not being used.
Set ϑ=s+cξ, x=ξ. In the full quotient variables,

\[
 D=r^2+c^2V_R,\quad G=\operatorname{diag}(D,r^2),\quad
 \rho=r\sqrt D,\quad
 \gamma=\frac{dr^2}{V_R}+\frac{V_Rr^2}{D}ds^2,
 \quad \mathcal A_s=(cV_R/D,0).
 \tag{3.3}
\]

Direct calculation gives

\[
 q=(c(3m_R-rm_R'),0),\qquad
 Q=\frac{c^2(3m_R-rm_R')^2}{2r^2D^2}.
 \tag{3.4}
\]

Thus q=(3c,0) on the Einstein core and q=0 on the exact hyperbolic end.
Even the mixed Ricci identity can be checked without an asymptotic estimate:

\[
 q_1'=-2cr^2(p_R-z_R),\qquad
 |E_{\rm mix}|^2
   =\frac{c^2r^2V_R}{D^2}(p_R-z_R)^2
   =\tfrac14\frac{V_R(q_1')^2}{r^2D^2}.
 \tag{3.5}
\]

The last expression is exactly one quarter of
|ρ^{-3/2}M^{-1/2}dq|². Here the mixed norm denotes one rectangular
horizontal--vertical block, not the doubled norm of both symmetric blocks.
This supplies an actual full-block realization of
the redshift mechanism, not merely compatible area and Maxwell equations.

The quotient is a disk: the s-circle closes at the bolt. It is not the
cylinder of the main question, despite the free T² action.

## 4. Quantified curvature and energy concentration

For the variable-mass metric the Weyl operator has two sectional entries
ω and four entries −ω/2, where

\[
 \omega=\frac{m_R}{r^3}+\frac{m_R''}{6r}
                          -\frac{2m_R'}{3r^2},\qquad |W|^2=3\omega^2.
 \tag{4.1}
\]

On the Einstein core |W|²=3/r⁶, so its peak at the bolt is 3. For large
R the transition values are O(R^{-6}), uniformly for a fixed χ. With
C=P², the coordinate-cell volume factor, dV=C r²dr after angular integration.
Therefore

\[
 \int|W|^2dV=C(1+O(R^{-3})),\qquad
 \int Q\,dV=C\left(\frac{3c^2}{2(1+c^2)}+O(R^{-3})\right)
 \tag{4.2}
\]

for each fixed c. For the twist integral on the uncut exact black hole,
one can differentiate the primitive

\[
 Vr+\frac{Vr^2D'}{2D}-2(r^3-1),\qquad
 V=r^2-r^{-1},\quad D=r^2+c^2V.
\]

Its derivative is 9c²/(2D²), its value at r=1 is zero, and its limit at
infinity is 3c²/(2(1+c²)). The tail and cutoff transition cost O(R^{-3}).

Now divide the two free fibre circles by N in each factor. This action is
free even at the bolt, where its ξ generator has nonzero x component.
It preserves smoothness, pointwise Ricci and Weyl, and all equations
(3.3)–(3.5), while dividing every physical integral by N². The flat
exterior torus carries the corresponding actual helical quotient lattice.
Choose N=ceil(R^{3/2}). Then the active region Ω_R={r≤2R} has

\[
 \operatorname{Vol}(\Omega_R)
   =\frac{C(8R^3-1)}{3N^2}\longrightarrow\frac{8C}3,
\]

\[
 \|\operatorname{Ric}+3g\|_\infty\longrightarrow0,
 \qquad \sup|W|=\sqrt3,
 \qquad \int|W|^2=O(R^{-3}),\quad \int Q=O(R^{-3}).
 \tag{4.3}
\]

For any fixed 0<w_0<√3, the physical volume of {|W|≥w_0} is O(N^{-2}).
The Weyl peak is therefore lost by an L²-to-L∞ inference even though
the full Ricci error tends uniformly to zero and the active volume stays
bounded. This is a complete one-ended example, not a hypothetical profile.

There is a separate warning about twist blowups. On the same unchanged
Einstein core, changing the integral slope c gives

\[
 Q(1)=\tfrac92c^2,\qquad |W|^2(1)=3.
 \tag{4.4}
\]

For a fixed fraction of this Q peak, its support has r-coordinate
thickness O(c^{-2}) because D=1+3c²(r−1)+O(r−1)+O(c²(r−1)²) near the bolt.
Its proper radial thickness is O(c^{-1}), since V=3(r−1)+O((r−1)²).
The ambient metric and curvature do not change when c changes. Thus a
blowup of the orbit twist Q need not be an ambient curvature blowup at all.
Any argument passing from Q peaks to an Einstein curvature bubble must
control the marked action, not just the ambient Ricci tensor.

## 5. Why the round-5 identities do not close the extension problem

For the truncated one-ended metric, Ω_R is D²×T² and χ(Ω_R)=0, just as
χ(T³×[0,1])=0. Its exact outer section has volume C(2R)³/N², so

\[
 V_{\rm ren}=-\frac{C}{3N^2}.
 \tag{5.1}
\]

The same four-dimensional Gauss–Bonnet/vertical-flux balance as in round 5
therefore applies. For example

\[
 \int\operatorname{tr}E\,dV=-C/N^2,\qquad
 \int\operatorname{tr}E_V\,dV=\int Q\,dV-2C/N^2.
 \tag{5.2}
\]

The trace formula follows by integrating r m_R''+2m_R'; the vertical
formula is the exact volume flux. Small pointwise errors acting through
the large unquotiented transition volume account for the finite energy
imbalance, and after the quotient all these terms shrink together.

The full physical-volume identities alone do not distinguish the disk
quotient from the cylinder quotient. The unweighted base Gauss–Bonnet
identity does: its right-hand side has the additional term 8πχ(B), equal
to 8π for the disk and zero for the cylinder. Likewise, a disk needs only
an isolated orbit-volume minimum, whereas the local annular neck in
Theorem 1.1 has the entire critical middle circle and nonconstant shape
energy (1.7).

The actual construction tasks that remain are now concrete:

* continue the charged analytic neck far enough to obtain two regions
  whose geometry permits controlled charge removal;
* make that removal and the shape/lapse evolution solve every Ricci block
  with a uniform small error, while retaining the same annular base and
  physical torus lattice;
* reach two exact outward hyperbolic end sections without a curvature
  singularity, loss of positive definiteness or a cap that changes the
  quotient into a disk.

The local neck proves that charge, positive sectional curvature, a stable
minimal T³ and initial two-sided expansion are mutually compatible with
the exact Einstein equation. The one-ended family proves that charge can
be removed by small full Ricci error in an actual complete metric and
that the relevant energy peaks can collapse. These are separate facts;
no gluing theorem has been proved to combine them. In particular,
Cauchy–Kowalevskaya existence supplies no estimates for the required global
extension or for smooth cutoff errors.

## 6. A precise asymptotically hyperbolic continuation target

The neck has the germ isometry

\[
 (t,\theta,\xi)\longmapsto(-t,\theta,-\xi).
 \tag{6.1}
\]

Indeed ξ↦−ξ preserves h and reverses K in (1.3); reversal of t reverses
the prescribed first derivative again. Analytic uniqueness proves (6.1).
Thus a suitable complete one-sided extension of this germ could be doubled
using this involution, with no new matching condition at the middle torus.
This observation does not supply such an extension.

The distinction between exact and asymptotically hyperbolic ends is useful
here. On an asymptotically hyperbolic end, ρ grows like e^{2t}, while a
fixed nonzero coordinate charge can have Q=O(e^{-6t}). Charge conservation
therefore does not itself exclude an Einstein AH end. It excludes an
*exact* hyperbolic end, where F, and hence q, vanish identically.

**Proposition 6.1 (conditional reduction to an Einstein AH cylinder).**
Suppose a complete free-T² Einstein metric g with Ric=−3g exists on
R×T³, with both ends admitting invariant geodesic gauges

\[
 g=dt^2+e^{2t}\gamma_\pm(t),\qquad
 \gamma_\pm(t)=h_\pm+O_{C^2}(e^{-2t}),
 \tag{6.2}
\]

where h_± are fixed smooth invariant metrics on the respective marked
T³. The remainder estimate includes up to two t and spatial derivatives
in fixed boundary charts. Then there are complete metrics g_j on the same
free-T² cylinder, unchanged on expanding compact subsets, with two exact
outward hyperbolic ends and

\[
 \|g_j^{-1}(\operatorname{Ric}(g_j)+3g_j)\|_\infty\longrightarrow0.
 \tag{6.3}
\]

**Proof.** Choose an invariant flat metric h_{0,±} on each actual marked
boundary torus. On T≤t≤T+L replace γ_±(t) by

\[
 \widetilde\gamma_\pm(t)
  =(1-\beta((t-T)/L))\gamma_\pm(t)
       +\beta((t-T)/L)h_{0,\pm},
 \tag{6.4}
\]

where β is a smooth step constant near its endpoints. Keep the original
metric before T and set γ=h_0 after T+L. For large T these are positive
metrics with uniform inverse and spatial C² bounds. They retain the same
torus lattice, invariant action, topology and smooth joins. Moreover

\[
 |\partial_t\widetilde\gamma|
       \le C(L^{-1}+e^{-2T}),\qquad
 |\partial_t^2\widetilde\gamma|
       \le C(L^{-2}+e^{-2T}),
 \tag{6.5}
\]

and the same first-derivative bound holds after one spatial derivative.
For the full three-dimensional slices write
S=I+(1/2)\widetilde\gamma^{-1}\partial_t\widetilde\gamma and H=tr S.
The Gaussian Ricci identities give

\[
 \begin{aligned}
 \operatorname{Ric}_{tt}&=-\partial_tH-|S|^2,\\
 (\operatorname{Ric}_T)^\#
    &=e^{-2t}\operatorname{Ric}_{\widetilde\gamma}^{\#}
          -\partial_tS-HS,\\
 \operatorname{Ric}_{tT}&=\operatorname{div}S-dH
          \quad\text{up to the sign convention for Codazzi}.
 \end{aligned}
\]

In the last line the physical slice norm adds a factor e^{-t} to a
boundary-coordinate spatial derivative. Thus the *full* Ricci endomorphism
error, including the mixed components, is bounded by

\[
 C(L^{-1}+e^{-2T}).
 \tag{6.6}
\]

Take T,L→∞ on both ends. The metric is unchanged on the core, and beyond
the transition it is exactly dt²+e^{2t}h_0. This proves (6.3).

The physical flat sections at T+L have metric e^{2(T+L)}h_0; their large
covolumes are not removed by a coordinate change. This proposition does
not infer a metric on a fixed closed graph manifold by matching them to
shrinking cusp sections.

The familiar connected-conformal-boundary results for Einstein metrics
with a nonnegative-Yamabe boundary component obstruct that sign of AH
continuation. They do not supply the same conclusion when both prescribed
conformal boundary classes have negative Yamabe constant. T³ can carry
such classes: for instance (1.3) has R_h=−6−Q_0<0, so its conformal
Laplacian has a negative Rayleigh quotient on constants. This does not
identify h with an actual conformal infinity or prove that one can prescribe
it there.
The precise nonnegative-boundary statement used here is Cai–Galloway,
*Boundaries of zero scalar curvature in the AdS/CFT correspondence*,
Theorem 1:
[primary author-hosted text](https://www.math.miami.edu/~galloway/papers/zero2.pdf).

Consequently, a sharper constructive target is a complete one-sided AH
extension of the charged neck, compatible with (6.1), whose boundary class
is negative Yamabe. Proposition 6.1 would then perform charge removal and
exact flattening through actual metrics, with a controlled full Ricci error.
The existence of that AH extension is unresolved. Conversely, a global
obstruction to such AH continuations would not alone rule out all
near-Einstein cylinders: an approximate family need not have an exact
Einstein limit with retained ends.

## Verification and primary sources

`round6_global_check.py` computes the full three-dimensional Ricci scalar
and every momentum component for the explicit neck data, in the rational
chart z=tan θ. It checks the shape energy, norm and positive orbit curvature,
then independently checks all variable-mass Ricci eigenvalues, the mixed
charge equation, the Weyl parameter and the exact twist primitive.

Actual analytic existence, as distinct from the verified constraints, uses
N. Koiso, *Hypersurfaces of Einstein manifolds*, Annales scientifiques de
l'École Normale Supérieure 14 (1981), 433–443, Proposition 6 and its
constraint-propagation proof on page 438:
[original primary article](https://www.numdam.org/article/ASENS_1981_4_14_4_433_0.pdf).
The modern formulation is B. Ammann, A. Moroianu and S. Moroianu,
*The Cauchy problems for Einstein
metrics and parallel spinors*, Communications in Mathematical Physics 320
(2013), Theorem 2.1 and equations (2.9)–(2.10):
[primary author-hosted text](https://moroianu.perso.math.cnrs.fr/tex/2013cmp.pdf).
Only analytic local existence and uniqueness are used. The paper explicitly
distinguishes this theorem from the generally false smooth Cauchy assertion.
