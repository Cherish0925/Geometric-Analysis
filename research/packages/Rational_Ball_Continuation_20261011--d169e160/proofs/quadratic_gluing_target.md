# The exact quadratic functional and the invisible leading ALE interaction

This note addresses the proposed use of quadratic-curvature gluing to produce a smooth global minimizer of
\[
P(g)=\int_M|\operatorname{Ric}^{\circ}_g|^2\,dV_g
\]
which is not Bach-flat. It contains an exact functional conversion, an explicit descent test, and a vanishing calculation for the Ricci-flat ALE boundary channel.

## 1. The parameter cannot be varied

Use the norm of the Weyl tensor as a `(0,4)` tensor. Put
\[
W(g)=\int|W_g|^2,\qquad S(g)=\int s_g^2,
\qquad B_t(g)=W(g)+tS(g).
\]
The Chern--Gauss--Bonnet identity is
\[
32\pi^2\chi(M)=W(g)-2P(g)+\frac16S(g).
\]
Consequently
\[
2P=B_{1/6}-32\pi^2\chi(M).
\]
In the alternative convention \(F_\tau=\int|\operatorname{Ric}|^2+\tau S\), the target is \(\tau=-1/4\). These are the same target parameter, not two different problems.

Gursky--Viaclovsky, *Critical metrics on connected sums of Einstein four-manifolds*, arXiv:1303.0827, Theorem 1.2, produces \(B_t\)-critical metrics for a parameter near the particular negative values listed in Tables 1.1--1.3. The adjustment of \(t\) is what solves the final scalar obstruction. It does not produce a critical metric for the prescribed positive parameter \(t=1/6\).

There is an exact way to see why their non-Einstein examples do not become candidates by reinterpreting the functional. Write \(E=\operatorname{Ric}^{\circ}\). Their first-variation tensors are
\[
\nabla B_t=B+tC,\quad
C=2\nabla^2s-2(\Delta s)g-2s\operatorname{Ric}+\frac12s^2g.
\]
At a closed \(B_t\)-critical metric with \(t\ne0\), tracing gives constant scalar curvature, hence
\[
C=-2sE,\qquad B=2tsE.
\]
Thus
\[
\boxed{\nabla P=(t-1/6)sE.}
\]
If \(s\ne0\), \(E\not\equiv0\), and \(t\ne1/6\), the genuine metric variation
\[
h=-(t-1/6)sE
\]
satisfies
\[
DP_g[h]=-(t-1/6)^2s^2P(g)<0.
\]
The variation is trace-free; a unit-volume requirement, if imposed, changes nothing because \(P\) is scale invariant in dimension four. Thus these metrics are not even local minima of the target functional.

## 2. Why strict Weyl subadditivity does not settle the target

Malchiodi--Malizia, *Weyl energy and connected sums of four-manifolds*, arXiv:2505.17752v1, proves strict Weyl subadditivity for two closed factors which are not locally conformally flat and not both self-dual or both anti-self-dual. It constructs competitors, not critical metrics. Its introduction discusses the use of this construction against minimizing degenerations, including the loss of basepoint freedom for ALE compactifications.

On a fixed smooth closed manifold, comparison of two metrics gives exactly
\[
2\Delta P=\Delta W+\frac16\Delta S.
\]
Therefore a saving in \(W\) proves a saving in \(P\) only if the scalar-square contribution is also controlled at the same order. Conformal normalization is not a replacement for that estimate.

There is a sharper limitation for the currently surviving zero-\(P\) bubbles. Suppose an ALE core has coordinates at infinity with
\[
g_N=\delta+O_k(r^{-4}),\qquad k\ge2.
\]
Then
\[
|W_{g_N}|=O(r^{-6}).
\]
Set \(\bar g=r^{-4}g_N\) and use inverted coordinates \(y=x/|x|^2\), \(\rho=|y|=r^{-1}\). The Euclidean term transforms exactly into the Euclidean metric, and
\[
\bar g=\delta+O_2(\rho^4).
\]
In particular, the curvature of the compactified metric tends to zero at the added point. Equivalently, the conformal transformation law yields
\[
|W_{\bar g}|_{\bar g}=r^4|W_{g_N}|_{g_N}=O(\rho^2),
\qquad W_{\bar g}(p)=0.
\]
This calculation applies to the order-four Ricci-flat ALE metrics and finite free quotients used for the rational-ball channel. It is local on the uniformizing cover, so the quotient introduces no change.

The leading interaction in Malchiodi--Malizia equation (1.6) is a multiple of
\[
W_{\bar g}(p)\circledast W_{g_O}(q).
\]
For these cores it is identically zero. In a genuine ALE desingularization the point \(p\) is the compactifying end, not an arbitrarily movable point where \(W_{\bar g}\ne0\). Thus the leading interaction mechanism in the closed connected-sum theorem does not itself give strict energy reduction for this degeneration.

This does not prove that all higher-order interactions vanish, nor that the singular limit minimizes \(P\). It identifies which asymptotic information is actually absent from the existing gluing theorem: one must calculate beyond the vanishing curvature two-jet and simultaneously control the scalar-square contribution.

## 3. The equation satisfied by a target bubble

At a closed \(P\)-critical metric the exact equation is
\[
s=\text{constant},\qquad B=\frac{s}{3}E.
\]
Under a curvature blowup with uniformly bounded original scalar curvature, the scalar curvature of the rescaled metrics tends to zero. A smooth ALE limit is therefore scalar-flat and Bach-flat. It need not be Ricci-flat. Ricci-flatness requires an additional argument, such as vanishing \(P\)-energy on that bubble.

For the zero-\(P\) rational-ball channel, Ricci-flatness is already part of the specified model, so the vanishing calculation in Section 2 directly applies. For a general compactness theorem, non-Ricci-flat scalar-flat Bach-flat cores must still be included.

## Sources

1. M. J. Gursky and J. A. Viaclovsky, *Critical metrics on connected sums of Einstein four-manifolds*, Advances in Mathematics 292 (2016), 210--315. Primary preprint: https://arxiv.org/abs/1303.0827 ; equations (1.5)--(1.10), Theorems 1.1--1.2, Tables 1.1--1.3.
2. J. A. Viaclovsky, *Critical Metrics for Riemannian Curvature Functionals*, IAS/Park City Mathematics Series 22 (2016), 195--274. Author's version: https://webapps.math.uci.edu/~jviaclov/lecturenotes/PCMI_Lectures_Final.pdf ; Lectures 8 and 10.
3. A. Malchiodi and F. Malizia, *Weyl energy and connected sums of four-manifolds*, https://arxiv.org/abs/2505.17752 ; Theorem 1.1, equations (1.6)--(1.7), discussion of ALE compactifications after equation (1.8).

The descent calculation and the specialization of the compactification estimate above are elementary consequences of these identities and the displayed ALE order. They are not being claimed as new general existence or compactness theorems.
