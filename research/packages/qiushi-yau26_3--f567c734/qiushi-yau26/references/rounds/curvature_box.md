# Sharp Ricci-box control in the four-dimensional Chern–Gauss–Bonnet formula

Let a Riemannian four-manifold satisfy
`||g^{-1} Ric + I||_op <= d`, with `0 <= d <= 1`.
Write its Ricci eigenvalues as `-1+a_i`, `|a_i|<=d`, and put
`t=sum a_i`. With `E=Ric-(s/4)g`, the Ricci part of the CGB density is

\[
F=\frac{s^2}{24}-\frac{|E|^2}{2}
=\frac23-\frac t3+\frac{t^2}{6}-\frac12\sum_i a_i^2.
\]

## Exact algebraic minimum

Each coordinate has second derivative `-2/3`. Holding the other coordinates
fixed, the minimum is at an endpoint. Repeating this reduction proves that
the global minimum on the entire box is attained at a vertex. If `m` of
the four coordinates are `+d`, its value is

\[
F_m(d)=\frac23-\frac{(2m-4)d}{3}
+\left(\frac{(2m-4)^2}{6}-2\right)d^2.
\]

Exact comparison of the five polynomials gives

\[
F\ge f(d):=
\begin{cases}
\dfrac23(1-d)^2,&0\le d\le1/3,\\[2mm]
\dfrac23(1+d)(1-2d),&1/3\le d\le1.
\end{cases}
\]

For `0<d<1/3` the minimizing vertices have four positive coordinates;
for `1/3<d<1` they have three. At `d=1/3` both patterns minimize;
at `d=1` the two-positive pattern also minimizes. At `d=0` the box is one point.
These are sharp algebraic bounds. They do not assert existence of a closed
metric realizing the minimizing curvature pattern everywhere. The same
bound holds for Ricci eigenvalues near `+1` by reversing all eigenvalues.

The independent exact script `curvature_box.py` proves separate concavity,
enumerates all sixteen vertices, and checks each polynomial comparison on
the stated rational interval by endpoints and interior critical points.

## Topological consequence

For a closed oriented four-manifold, use the Hilbert–Schmidt operator norm
for the Weyl halves. Then

\[
4\pi^2(2\chi\pm3\tau)
=\int_M\left(2|W^\pm|^2+F\right)dV
\ge f(d)\operatorname{Vol}(M,g).
\]

Consequently `d<1/2` implies `2 chi > 3|tau|`. This improves the
`d<=1/4` sufficient compatibility check in the initial preparation document.
It is an optimized consequence of the classical identities, not a claim
of a new general Einstein existence theorem or established literature novelty.
At `d=1/2` it gives the non-strict inequality only.

For the connector normalization `||g^{-1} Ric+3I||_op<=epsilon`, substitute
`d=epsilon/3` and multiply the pointwise density by nine. Thus

\[
F\ge
\begin{cases}
\dfrac23(3-\epsilon)^2,&0\le\epsilon\le1,\\[2mm]
6-2\epsilon-\dfrac43\epsilon^2,&1\le\epsilon\le3.
\end{cases}
\]

In particular, for `epsilon<=1`,

\[
\operatorname{Vol}(M,g)\le
\frac{12\pi^2\chi(M)}{(3-\epsilon)^2}.
\]

The older coefficient `6-4 epsilon-(4/3)epsilon^2` bounds scalar and
traceless Ricci terms separately. The sharper coefficient retains their
dependence on the same four eigenvalues; its gain is `2 epsilon^2` on
this interval. The unchanged limiting budget is
`Vol <= (4/3) pi^2 chi` when `epsilon -> 0`.

## Quantitative cost of preserving an expanding core

Suppose a closed candidate retains, without rescaling, an AH end segment
`[T,R] x T^3` of the form `dt^2+e^{2t}q(t)`, and
`Vol(T^3,q(t))>=v_min>0` there. Its retained volume is at least

\[
\frac{v_{\min}}3(e^{3R}-e^{3T}).
\]

If the entire closed metric satisfies the defect bound with `epsilon<=1`,
the preceding estimate forces

\[
\chi(M)\ge
\frac{v_{\min}(3-\epsilon)^2}{36\pi^2}
(e^{3R}-e^{3T}).
\]

Thus allowing topology to vary removes the fixed-topology contradiction
only if its Euler characteristic can pay this exponential volume cost
(or the actual retained covolume changes). A coordinate shift cannot pay
the cost. This necessary condition does not solve the two-end metric and
lattice matching problem, nor does it prove its impossibility.

## A sharper cover-independent connector threshold

Assume the exact hyperbolic exterior is unchanged and the reference Euler
budget is the sum of its hyperbolic blocks. If a connector of volume `V_N`
replaces reference cusp volume `V_rem`, subtraction of the two CLOSED CGB
identities gives the exact relation

\[
w+\fint_N F=6r,\qquad
w=\fint_N|W|^2,\quad r=V_{\rm rem}/V_N.
\]

No assertion is made for an unmatched domain without its boundary terms.
Suppose geometric information supplies

\[
w\ge w_0,\qquad r\le1+w_0/6-\kappa,
\qquad0<\kappa\le1.
\]

Then `f_3(epsilon)<=6(1-kappa)`, where `f_3` is the piecewise density
bound above. Its two branches are decreasing for `0<=epsilon<=3`.
Their explicit inverses give

\[
\epsilon\ge
\begin{cases}
3(1-\sqrt{1-\kappa}),&0<\kappa\le5/9,\\[1mm]
(\sqrt{9+72\kappa}-3)/4,&5/9\le\kappa\le1.
\end{cases}
\]

If the actual defect exceeds three, these lower bounds hold trivially;
thus the conclusion does not require a hidden upper-bound assumption.
For normalized `Ric≈-g`, divide the bound by three. In particular the
volume hypothesis `V_N>=(1+c)V_rem` permits `w_0=0` and
`kappa=c/(1+c)`. Neither changing cover degree nor scaling the common
reference volumes alters this threshold.

This strengthens the coarser threshold in `global.md`, but it still
requires the geometric volume/Weyl hypothesis. The algebraic concentration
model in that note does not satisfy a fixed positive `kappa`, and is not
excluded by the improvement.

## Scope of the conclusions

Input: classical four-dimensional Chern–Weil identities and the full Ricci
eigenvalue box. This note contains an exact algebraic optimization and its
direct consequences. It neither assumes the unpublished uniform-gap theorem
nor implies the Yau26 conclusion.
