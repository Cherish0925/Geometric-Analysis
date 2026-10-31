# An optimized fixed-ratio Ricci-defect obstruction

Date: 2026-09-19. Local calculation. This sharpens the algebraic use of the stated monopole and Chern--Weil inequalities; it does not establish optimal geometric attainability or settle near-Einstein existence.

## Assumptions

Let a closed oriented four-manifold satisfy the actual monopole input `MP(A)`, with `A>0`, and put

\[
 2\chi+3\tau=(1-p)A.
\]

For the blowup family this is `p=k/A`. Suppose a metric obeys

\[
 d=\|g^{-1}\operatorname{Ric}+I\|_{\infty,\mathrm{op}}<\frac12.
\]

Write its Ricci eigenvalues `-1+a_i`, `|a_i|<=d`, scalar curvature `s`, traceless Ricci tensor `E`, and

\[
 F=\frac{s^2}{24}-\frac{|E|^2}{2},\qquad w=|W^+|\ge0.
\]

The norm of `W+` is its Hilbert--Schmidt operator norm. The inputs are

\[
 \int(s-\sqrt6w)^2\ge72\pi^2A,
 \qquad \int(2w^2+F)=4\pi^2(1-p)A.
\tag{1}
\]

The exact Ricci-box minimum in `curvature_box.md` shows `F>0` for this entire defect range, so all quotients below have positive denominator. It follows already that `p<1`. Values `p>=1` cannot be assumed geometrically admissible in this range.

## 1. Exact pointwise optimization

### Proposition

For `0<=d<1/2`, the exact algebraic supremum is

\[
 C(d)=\sup_{|a_i|\le d,\ w\ge0}
 \frac{(s-\sqrt6w)^2}{2w^2+F}
 =\begin{cases}
 \displaystyle\frac{9(3-d^2)}{1-3d^2},
 &0\le d\le2-\sqrt3,\\[2mm]
 \displaystyle\frac{27(1-d)}{(1-2d)(1+d)},
 &2-\sqrt3\le d<1/2.
 \end{cases}
\tag{2}
\]

In particular `C(0)=27`.

**First optimization: the Weyl norm.** Set `S=-s>0`. For fixed Ricci eigenvalues, Cauchy--Schwarz in the two-dimensional quadratic form gives

\[
 \frac{(S+\sqrt6w)^2}{F+2w^2}\le\frac{S^2}{F}+3.
\]

This is attained at `w=sqrt(6)F/(2S)>0`. Thus it remains to maximize

\[
 \frac{|E|^2}{s^2}=R,\qquad
 C=3+\frac{24}{1-12R}.
\tag{3}
\]

**Second optimization: the correlated Ricci eigenvalues.** Put `x_i=1-a_i`, so `x_i` lies in `[1-d,1+d]` and is positive. Then

\[
 R=\frac{\sum x_i^2}{(\sum x_i)^2}-\frac14.
\]

With the other three coordinates fixed, write their sum and sum of squares as `P>0,Q>0`. The derivative of `(x²+Q)/(x+P)²` is

\[
 \frac{2(Px-Q)}{(x+P)^3}.
\]

Any interior critical point is a minimum. The maximum on each coordinate interval is therefore at an endpoint, and repeating this argument reduces the full box to its vertices. This is not a concavity assertion for the ratio.

If `m` of the four `x_i` equal `1+d`, then

\[
 R_m=\frac{m(4-m)d^2}{[4+(2m-4)d]^2}.
\]

The `m=0,4` values vanish and `R_3<=R_1`. The two remaining candidates are

\[
 R_2=\frac{d^2}{4},\qquad
 R_1=\frac{3d^2}{4(2-d)^2}.
\]

They cross at `d=2-sqrt(3)`, so

\[
 R(d)=\max\left\{\frac{d^2}{4},\frac{3d^2}{4(2-d)^2}\right\}.
\tag{4}
\]

Substitution in (3) gives (2). At the first branch, the maximizing Ricci spectrum has two eigenvalues `-1-d` and two `-1+d`; on the second it has one `-1-d` and three `-1+d`. Choosing the indicated `w` realizes the algebraic quotient. This does not construct closed metrics realizing those patterns, equality in the monopole estimate, or the differential Einstein identities.

## 2. The resulting quantitative gap

Combining the pointwise upper bound with (1) gives

\[
 1-p\ge\frac{18}{C(d)},\qquad
 p\le P(d):=
 \begin{cases}
 \displaystyle\frac{1+5d^2}{3-d^2},
 &0\le d\le2-\sqrt3,\\[2mm]
 \displaystyle\frac13+\frac{4d^2}{3(1-d)},
 &2-\sqrt3\le d<1/2.
 \end{cases}
\tag{5}
\]

Both branches are strictly increasing away from zero, join continuously, and tend to `1` as `d` tends to `1/2`. Their joining ratio is

\[
 p_*=P(2-\sqrt3)=2\sqrt3-3.
\]

Therefore, for `1/3<p<1`, every such near-negative-Einstein metric satisfies the explicit lower bound

\[
 \boxed{d\ge d_*(p):=
 \begin{cases}
 \displaystyle\sqrt{\frac{3p-1}{p+5}},
 &\frac13<p\le2\sqrt3-3,\\[2mm]
 \displaystyle\frac{\sqrt{(3p-1)(3p+15)}-(3p-1)}8,
 &2\sqrt3-3\le p<1.
 \end{cases}}
\tag{6}
\]

Since `d_*(p)<1/2`, the same inequality holds trivially for metrics with defect at least `1/2`; hence it is an all-metrics lower bound on `e_-(M)` for each topology obeying these hypotheses and this fixed ratio. For `p>=1`, the positive CGB integrand instead gives the separate statement `e_-(M)>=1/2`. Neither statement supplies candidate metrics or proves optimality.

## 3. Comparison with the separated estimate

The earlier estimate

\[
 \frac d{1-d}\ge\sqrt{\frac{p-1/3}{2}}
\]

is equivalent, for `d<1`, to

\[
 p\le P_{\rm old}(d)=\frac13+\frac{2d^2}{(1-d)^2}.
\]

The improvement is strict for every `0<d<1/2`. Indeed

\[
 P_{\rm old}-P=
 \begin{cases}
 \displaystyle\frac{2d^2(1+16d-11d^2)}{3(3-d^2)(1-d)^2}>0,
 &0<d\le2-\sqrt3,\\[2mm]
 \displaystyle\frac{2d^2(1+2d)}{3(1-d)^2}>0,
 &2-\sqrt3\le d<1/2.
 \end{cases}
\]

The reason is that the optimized inequality retains the dependence of scalar curvature and traceless Ricci on the same four eigenvalues. It does not combine their separately worst values.

For `q=p-1/3` tending to zero from above,

\[
 d_*(p)=\frac34\sqrt q+O(q^{3/2}),\qquad
 d_{\rm old}(p)=\frac1{\sqrt2}\sqrt q+O(q).
\]

Equivalently, the small-defect ratio excess changes from the old upper coefficient `2d²` to `(16/9)d²`. The square-root scale remains: this calculation cannot create a positive defect gap as `p` approaches `1/3`.

## 4. Scope relative to the original problem

This supplies an explicit stronger obstruction for each fixed blowup ratio *above* `1/3`. The unpublished exact-Einstein uniform-gap manuscript instead aims to exclude Einstein metrics even for some ratios *below* `1/3`; (5) does not enter that band. Nor does it construct small-defect metrics on a non-Einstein smooth type.

The result is a new calculation in this local work, not a claim of literature novelty. It uses the stated monopole mixed inequality and classical Chern--Weil identity, independently of the unpublished exact-Einstein gap theorem. `fixed_ratio_check.py` verifies the algebra, maximizing parameters, joining values, inverses, and comparison formulas exactly.
