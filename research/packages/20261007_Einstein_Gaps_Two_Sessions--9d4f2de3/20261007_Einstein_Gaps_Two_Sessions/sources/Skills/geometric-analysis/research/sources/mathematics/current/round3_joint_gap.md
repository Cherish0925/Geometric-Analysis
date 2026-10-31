# A uniform near-Einstein gap across the critical blow-up ratio

Let X be a closed minimal complex surface of general type with b+(X)>1,
let A=c1(X)^2>0, and give

\[
M=X\#k\overline{\mathbb{CP}}^{\,2},\qquad k\ge0,
\]

the complex orientation. For a smooth Riemannian metric g write

\[
\delta(g)=\|g^{-1}\operatorname{Ric}_g+I\|_{L^\infty,\mathrm{op}},
\qquad d=(1/3-k/A)_+.
\]

**Theorem.** There is a numerical constant c*>0, independent of X, k,
and g, such that

\[
\boxed{\delta(g)^2+(1/3-k/A)_+\ge c_*.}                 \tag{1}
\]

No full-curvature, Weyl-minus, diameter, volume, injectivity, Euler/A,
Sobolev, or curvature-derivative bound is imposed. The constant is
existential; no optimal value is asserted.

The new analytic ingredient is the intrinsic monopole calibration gap
proved in [round3_rigidity.md](round3_rigidity.md). The argument below
supplies all of its topological and curvature-budget inputs for this
family. In particular this is not an application of a smoothing theorem
or of the older exact-Einstein gap.

## 1. Actual monopole classes and their squares

The usual Seiberg--Witten blow-up classes have the form

\[
a_\epsilon=c+\sum_{i=1}^k\epsilon_i E_i,\quad
c^2=A,\quad E_i^2=-1,\quad c\cdot E_i=E_i\cdot E_j=0\ (i\ne j).
\]

They are actual monopole classes, not just formal vectors in cohomology.
Sign averaging of their self-dual harmonic squares gives

\[
\operatorname{Av}_\epsilon(a_\epsilon^+)^2
=(c^+)^2+\sum_i(E_i^+)^2\ge A.
\]

For the given metric choose one with p=(a^+)^2>=A. Its square is
a^2=A-k, independent of the choice. Write T=2chi(M)+3tau(M)=A-k.
The classical scalar and scalar--Weyl estimates for this class are

\[
\int s^2\ge32\pi^2p,\qquad
\int(-s+\sqrt6|W^+|)^2\ge72\pi^2p.
\tag{2}
\]

The rescaled monopole equations used below exist for every positive
smooth weight on the original metric; this follows by conformal covariance.
These classical inputs, including the blow-up selection, are given in
[LeBrun, Ricci Curvature, Minimal Volumes, and Seiberg--Witten Theory](https://arxiv.org/abs/math/0003068)
and [Four-Manifolds, Curvature Bounds, and Convex Geometry, Lemma 3.7 and Proposition 3.8](https://arxiv.org/abs/math/0611450).

## 2. The budgets are uniform and use no Euler-characteristic estimate

It suffices first to consider delta<=1/64. Put

\[
u=|W^+|_{\rm HS},\quad w=\lambda_{\min}(W^+),\quad
q=-s+\sqrt6u,\quad t=s+8\sqrt6u,
\]
\[
E=\operatorname{Ric}+g,\quad e=s+4,\quad
P=\int|\operatorname{Ric}^{\circ}|^2,\quad V=\operatorname{Vol}(M,g),
\]
\[
G=(2s/3-2\sqrt{2/3}u)^2-(2s/3+2w)^2,
\quad \mathcal D=|E|^2+e^2+t^2+G,
\quad d_{\rm cal}=\int\mathcal D.
\]

The Weyl norm here is the Hilbert--Schmidt norm as an operator on
self-dual two-forms. The Ricci defect uses the spectral operator norm.
Since s<0 and w>=-sqrt(2/3)u, G>=0.

The scalar estimate gives

\[
V\ge\frac{32\pi^2}{25}A,\qquad P\le4\delta^2V.       \tag{3}
\]

We also use the lowest-eigenvalue form

\[
\int(2s/3+2w)^2\ge32\pi^2p\ge32\pi^2A.              \tag{4}
\]

For clarity, (4) follows by the same rescaled-spinor argument as (2),
retaining <W+psi,psi>>=w|psi|^2 instead of bounding w by the Weyl norm.
Set q_w=-s-3w>0 and choose the weight sqrt(q_w), by smooth approximation.
The spinor and self-dual-form Weitzenbock identities give
int q_w |varphi|^2 >= int sqrt(q_w)|varphi|^3. Two applications of
Holder and harmonic projection give int q_w^2>=72 pi^2 p.
Multiplication by 4/9 proves (4). Thus the eigenvalue estimate does not
add a hypothesis on the selected class.

Chern--Weil and two elementary pointwise identities are

\[
\int(s^2/24+2u^2)=4\pi^2 T+P/2,
\]
\[
t^2+18G=216(s^2/24+2u^2)-18(2s/3+2w)^2,
\]
\[
t^2=216(s^2/24+2u^2)-8q^2.                           \tag{5}
\]

Equations (3)--(5), and |E|^2=|Ric^circ|^2+e^2/4, yield

\[
\frac{d_{\rm cal}}V\le436\delta^2+675d.              \tag{6}
\]

In detail int(t^2+18G)<=108P+864 pi^2 A d. Since G>=0,
adding int(|E|^2+e^2) bounds dcal by 109 int|E|^2+864 pi^2 A d.
Using (3) gives (6).

For the same chosen class define Delta=int q^2-72 pi^2p>=0. The
last identity in (5) gives

\[
0\le\Delta\le\frac{27}{2}P+108\pi^2Ad,
\qquad
\frac\Delta V\le54\delta^2+\frac{675}{8}d.             \tag{7}
\]

Finally the required nonnegative self-intersection is automatic in this
regime, not an extra condition on k. Pointwise,

\[
\frac{s^2}{24}-\frac{|\operatorname{Ric}^{\circ}|^2}{2}
\ge\frac23(1-\delta)^2-2\delta^2>0.
\]

Its integral plus the nonnegative Weyl term equals 4 pi^2 T, so
a^2=T=A-k>0. If k>=A, no metric with such small delta exists in
the first place.

## 3. The intrinsic estimate completes the proof

For this actual class, define

\[
\varepsilon=\delta^2+(\Delta+d_{\rm cal})/V.
\]

Theorem 2 of the intrinsic proof, since a^2>=0, gives epsilon>=c>0
with a universal constant. The preceding bounds give

\[
\varepsilon\le491\delta^2+\frac{6075}{8}d
\le760(\delta^2+d).
\]

Hence (1) holds in the small-delta regime with c/760. For delta>1/64
it holds trivially with 1/4096. Taking
c*=min(c/760,1/4096) proves the all-metrics statement.

The decisive analytic step is not a passage to a local geometric limit:
the rescaled spinor has a uniformly bounded amplitude and a controlled
average rough Laplacian; its positive-spin connection curvature has a
controlled average L2 norm. The bundle Hessian estimate controls the
H1 norm of J=div W(A_psi). Integration by parts in the actual Bianchi
identity forces int|J|^2/V to zero in a hypothetical critical sequence,
while the weighted two-form identity forces it to 1/16. Both conclusions
use the same metric and normalized measure, including in collapsed cases.

## 4. Mathematical consequences and the remaining Yau26 problem

Set gamma=c*/2 and epsilon*=sqrt(c*/2). If

\[
k/A\ge1/3-\gamma,
\]

then every metric on that member of the family has delta>=epsilon*.
In particular it admits no negative Einstein metric. Positive or zero
Einstein constants are also excluded by the nonzero monopole class and
the spinor maximum principle. This recovers a uniform exact-Einstein
forbidden band and strengthens it to a uniform near-negative-Einstein
band on the same family.

This rules out using critical or sufficiently near-critical blow-ups in
this family as arbitrarily tightly negatively Ricci-pinched counterexamples.
It does not prove that every nearly negative Einstein four-manifold is
Einstein, cover all non-Einstein smooth topologies, or address the positive
branch or all higher dimensions. The surface-bundle and marked A1-resolution
constructions are not identified with this blow-up regime by this argument.

The complete analytic proof and family specialization are new deductions
of this research round. Their relationship to the full published literature
still requires a dedicated comparison; the calculation is not labelled
a solution of Yau26 or a confirmed first-in-literature result.
