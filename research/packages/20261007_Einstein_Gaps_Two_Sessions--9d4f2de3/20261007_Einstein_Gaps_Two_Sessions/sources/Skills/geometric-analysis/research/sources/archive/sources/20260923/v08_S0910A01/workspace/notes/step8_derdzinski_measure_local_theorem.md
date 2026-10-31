# Step 8: Derdziński source verification and measure-local rigidity (revised)

Session: S0910A01. Phase: Explore.

## Purpose

This note repairs the Step 7 local-rigidity route at the strength supported by the mathematics. The conclusion is not pointwise disappearance of every noncollapsed region. In a varying-topology LeBrun near-boundary sequence the supported statement is a volume-proportion theorem:

\[
\forall v>0,\qquad
\frac{\operatorname{Vol}\{p:\operatorname{Vol}B_1(p)\ge v\}}
     {\operatorname{Vol}M}\to0.
\]

Small noncollapsed islands of `o(Vol M)` may remain and may carry topology, curvature, or exceptional bubble geometry. This distinction is essential for the unresolved collapse problem.

The note also verifies the Derdziński conformal factor from the primary 1983 paper, replaces the unsupported Step 7 Schauder sentence by a finite-`W^{2,p}` harmonic-coordinate passage, and replaces the earlier undefined `Q,P` notation by an explicit LeBrun gap density.

## 1. Primary-source Derdziński verification

Source recovered in this step:

- PDF: `Sessions/S0910A01/workspace/data/sources/derdzinski_1983_self_dual_kahler_einstein_four.pdf`
- extracted text: `Sessions/S0910A01/workspace/notes/sources/derdzinski_1983_self_dual_kahler_einstein_four.txt`
- Numdam URL: `https://www.numdam.org/item/CM_1983__49_3_405_0.pdf`

The needed statement is Proposition 5 of Derdziński, extracted-text lines 1024--1077. In current notation, if an oriented Riemannian four-manifold satisfies

\[
\delta W^+=0,
\qquad \#\operatorname{spec}(W^+)\le 2,
\]

then on the open set where `W^+ != 0`,

\[
\widehat g=(24\,|W^+|_g^2)^{1/3}g
\]

is locally Kähler and the Kähler orientation is the prescribed orientation. The Kähler form is obtained from the eigensection of the simple eigenvalue of `W^+`. Proposition 5(ii) gives essential uniqueness of this conformal factor. Remark 4, extracted-text lines 1173--1191, states the same local relation for Einstein metrics: an Einstein metric is locally conformally Kähler exactly when `W^+` has at most two eigenvalues, with the conformal change given by the natural formula above.

For a two-eigenvalue trace-free self-dual Weyl tensor with simple eigenvalue `w` and double eigenvalue `-w/2`,

\[
|W^+|^2=w^2+2(w/2)^2={3\over2}w^2,
\]

so Derdziński's factor is equivalently a constant multiple of `|w|^{2/3}`. Thus the Step 7 TTCS insight is confirmed by the primary source: the factor is not an arbitrary positive solution of a scalar conformal equation.

For the calibrated profile from the LeBrun near-equality calculation,

\[
\operatorname{Ric}=-g,
\quad s=-4,
\quad |W^+|^2={1\over24},
\quad \operatorname{spec}(W^+)=\left(-{1\over6},{1\over12},{1\over12}\right),
\]

Derdziński's factor is `(24|W^+|^2)^{1/3}=1`, so the limiting metric itself is locally Kähler. But a Kähler-Einstein four-metric with `Ric=-g` has, in the Kähler orientation,

\[
\operatorname{spec}(W^+)=\left(-{2\over3},{1\over3},{1\over3}\right),
\qquad |W^+|^2={2\over3},
\]

which contradicts `|W^+|^2=1/24`.

There is also a direct tensor proof, independently supplied by S0910A03. If `W^+=\mu I+(\lambda-\mu)P_\omega` has two distinct constant eigenvalues and `\delta W^+=0`, retaining both product-rule terms gives

\[
(\operatorname{div}\omega)\otimes\omega+
\omega\lrcorner\nabla\omega=0.
\]

Projection along `\omega` gives `div omega=0`; the orthogonal projection then gives `\omega_{ab}\nabla^a\omega_{cd}=0`. A nonzero self-dual two-form in dimension four is nondegenerate, so `\nabla\omega=0` and hence `\nabla W^+=0`. This agrees with Derdziński Proposition 5(iii), which states that constant `|W^+|` under the same hypotheses is equivalent to `\nabla W^+=0`. At the calibrated Einstein spectrum, however, the scalar Einstein-Weyl identity

\[
\Delta|W^+|^2=2|\nabla W^+|^2+s|W^+|^2-36\det W^+
\]

requires `|nabla W^+|^2=1/16`. This is another local contradiction.

## 2. Explicit LeBrun gap density

Let

\[
\alpha=\sqrt{2/3},
\qquad u=|W^+|,
\qquad f={2\over3}s-2\alpha u,
\qquad a={2\over3}s+2w,
\]

where `w` is the lowest eigenvalue of `W^+`, and set

\[
\xi=w+\alpha u\ge0.
\]

Then `a=f+2xi`. Define the explicit nonnegative pointwise gap

\[
\mathcal G=f^2-(a_-)^2,
\qquad a_-:=\min(a,0).
\]

Nonnegativity is exactly LeBrun's pointwise comparison: if `a<0`, then `f<=a<0`, hence `f^2>=a^2`; if `a>=0`, the second term vanishes.

The completion identity checked in `workspace/scripts/step8_gap_density_algebra.py` is

\[
{s^2\over24}+2u^2
={1\over12}f^2+{1\over216}(s+8\sqrt6u)^2.
\]

If

\[
D_i={1\over4\pi^2}\int_{M_i}\left({s_i^2\over24}+2|W_i^+|^2\right)d\mu_i
-{2\over3}(a_i^+)^2
\]

is the mixed LeBrun deficit for the selected monopole class, then LeBrun's theorem gives

\[
\int (a_i)_-^2\,d\mu_i\ge 32\pi^2(a_i^+)^2.
\]

The completion identity gives

\[
\int f_i^2\,d\mu_i
=32\pi^2(a_i^+)^2+48\pi^2D_i
-{1\over18}\int(s_i+8\sqrt6|W_i^+|)^2d\mu_i,
\]

and therefore

\[
0\le \int\mathcal G_i\,d\mu_i\le48\pi^2D_i.
\]

At the calibrated values `s=-4`, `u=1/(2sqrt6)`, one has `f=-3` and

\[
\mathcal G=4\xi(3-\xi).
\]

Since `0<=xi<=1/6` at this `u`, `mathcal G=0` forces `xi=0`, hence

\[
w=-\sqrt{2/3}|W^+|=-{1\over6}.
\]

The trace-free condition and `|W^+|^2=1/24` then force the remaining eigenvalues to be `1/12,1/12`. Thus the zero set of the explicit gap density, together with the completion-square zero set, gives the full calibrated spectrum without using the undefined `Q,P` notation from the first version of this note.

## 3. Local averaging uses means

Let `(M^n,g)` have `Ric >= -(n-1)K g`, and let `F >= 0` be measurable. For fixed `R`, choose `p` uniformly by Riemannian volume. Then Bishop-Gromov doubling gives

\[
\mathbb E_p\left[{1\over \operatorname{Vol}B_R(p)}\int_{B_R(p)}F\,d\mu\right]
\le C(n,K,R)\,{1\over \operatorname{Vol}M}\int_M F\,d\mu .
\]

Indeed, by Fubini the expectation equals

\[
{1\over \operatorname{Vol}M}\int_M F(x)\left[\int_{B_R(x)}{d\mu(p)\over \operatorname{Vol}B_R(p)}\right]d\mu(x).
\]

If `d(p,x)<=R`, then `B_R(x) subset B_{2R}(p)`, and doubling bounds the inner bracket by a constant depending only on `n,K,R`.

This is the right statement for collapse. Absolute local integrals can be small just because a ball is tiny; local means retain curvature and spectral information.

## 4. Deficit density for the LeBrun near-boundary route

For the LeBrun blow-up sequence, assume

\[
\delta_i=\|g_i^{-1}\operatorname{Ric}_{g_i}+I\|_{L^\infty,op}\to0,
\quad A_i=c_1^2(X_i),
\quad M_i=X_i\#k_i\overline{\mathbb{CP}}^{2},
\]

with the Step 3--5 monopole sign choice and near-boundary bookkeeping:

\[
D_i/A_i\to0,
\qquad \operatorname{Vol}(M_i,g_i)/A_i\asymp1,
\]

and in the fully calibrated boundary regime, `Vol/A -> 32 pi^2/9`. Define

\[
F_i=|\operatorname{Ric}_{g_i}+g_i|^2
 +(s_i+8\sqrt6|W_i^+|)^2
 +\mathcal G_i.
\]

The first term is uniformly `O(delta_i^2)`. The second is bounded by the Step 5 completion-square remainder `864 pi^2 D_i`. The third is bounded by `48 pi^2 D_i`. Since `Vol_i` is comparable to `A_i`,

\[
{1\over \operatorname{Vol}M_i}\int_{M_i}F_i\,d\mu_i\to0 .
\]

## 5. Harmonic-coordinate passage: finite `W^{2,p}`, not approximating Schauder smoothness

Cheeger-Naber Theorem 1.13 and Remark 1.11 give the needed regularity source. In dimension four, if `|Ric|<=3` and `Vol(B_1(p))>=v`, then

\[
\operatorname{Vol}\bigl(T_r\{x\in B_1(p): r_h(x)\le r\}\bigr)
\le C(v)r^4.
\]

Harmonic coordinates with radius bounded below give uniform `C^{1,\alpha}\cap W^{2,p}` bounds for every finite `p`; Cheeger-Naber state this near Definition 2.9 and use it again around lines 1060--1068.

In harmonic coordinates the metric components satisfy

\[
g^{ab}\partial_a\partial_b g_{jk}
= -2\operatorname{Ric}_{jk}+Q_{jk}(g^{-1},\partial g),
\]

up to the sign convention for the coordinate Laplacian. From bounded harmonic radius, a subsequence converges in `C^{1,beta}` and weakly in `W^{2,p}`. Since

\[
\operatorname{Ric}_{g_i}=-g_i+e_i,
\qquad \|e_i\|_{L^\infty}\to0,
\]

and the quadratic term `Q(g_i^{-1},partial g_i)` converges strongly in finite `L^q` after choosing a large finite exponent, the right-hand side converges strongly in finite `L^q`. Interior estimates for uniformly elliptic operators with coefficients converging in `C^0` then give strong `W^{2,q}` convergence on a smaller chart. The limit first satisfies `Ric(g_infty)=-g_infty` weakly; elliptic regularity for the limit Einstein equation in harmonic coordinates makes the limit smooth. No derivative-Ricci bound and no uniform `C^{2,alpha}` control of the approximating metrics is used.

Strong finite-`W^{2,p}` convergence for `p>2`, together with fixed orientation on the chart, is enough in four dimensions to pass `W^+`, `s`, eigenvalue functions, and the nonnegative density `mathcal G_i` in `L^1` to the smooth limit.

## 6. Volume-proportion theorem

Let

\[
E_i(v)=\{p\in M_i:\operatorname{Vol}_{g_i}(B_1(p))\ge v\}.
\]

**Theorem.** Under the LeBrun near-boundary hypotheses above, for every fixed `v>0`,

\[
{\operatorname{Vol}E_i(v)\over \operatorname{Vol}M_i}\longrightarrow0 .
\]

Proof. Suppose for some `v,eta>0` a subsequence satisfies `Vol E_i(v)>=eta Vol M_i`. Apply the local-mean averaging lemma to `F_i`; some `p_i in E_i(v)` has

\[
{1\over \operatorname{Vol}B_1(p_i)}\int_{B_1(p_i)}F_i\,d\mu_i\to0.
\]

Bishop-Gromov gives a lower bound for `Vol B_{1/2}(p_i)` and an upper bound for `Vol B_1(p_i)`, depending only on the Ricci bounds and `v`. Choose `r_0(v)>0` small enough that Cheeger-Naber's harmonic-radius bad set cannot cover `B_{1/2}(p_i)`. Then there exists `q_i in B_{1/2}(p_i)` with `r_h(q_i)>=r_0`. On a smaller harmonic chart around `q_i`, the finite-`W^{2,p}` argument gives a smooth Einstein limit `g_infty` with `Ric=-g_infty`.

The local integral of `F_i` over this chart tends to zero. Passing to the limit gives

\[
s_\infty=-4,
\quad s_\infty+8\sqrt6|W^+_\infty|=0,
\quad \mathcal G_\infty=0.
\]

Hence `|W^+_infty|=1/(2sqrt6)` and the explicit gap density forces

\[
\operatorname{spec}(W^+_\infty)=\left(-{1\over6},{1\over12},{1\over12}\right).
\]

Since `g_infty` is Einstein, `delta W^+_infty=0`. Derdziński Proposition 5 applies and its conformal factor is constant; equivalently, the direct projector lemma gives `nabla W^+_infty=0`. Both routes contradict the calibrated Einstein-Weyl identity, or the Kähler-Einstein norm `|W^+|^2=2/3`. The contradiction proves the theorem.

For a fixed critical boundary manifold, where `A` is fixed and the same deficits vanish absolutely rather than only after dividing by `A`, the stronger statement

\[
\sup_p \operatorname{Vol}B_1(p)\to0
\]

follows by the same regular-patch contradiction. This fixed-topology statement must not be imported into the varying-`A_i` problem.

## 7. Collapse and local unwrapping

The remaining negative-branch regime is collapse in volume proportion:

\[
\forall v>0,\qquad \operatorname{Vol}E_i(v)/\operatorname{Vol}M_i\to0.
\]

The local averaging lemma still says that volume-random collapsed balls have small mean `F_i`. The question is whether their hidden local geometry can be unwrapped without losing this small mean.

A useful conditional mechanism is:

1. Select a typical collapsed ball with small local mean of `F_i`.
2. Pass to a local normal cover or universal cover of a slightly larger ball.
3. Obtain a noncollapsed cover ball with bounded harmonic radius, for example through Naber-Zhang maximal nilpotency rank and a controlled low-dimensional model.
4. Prove a deck-orbit counting estimate: for the relevant cover ball,
   \[
   \fint_{B_a(\hat p)}\pi^*\phi
   \le C\,\mathcal M_R\phi(p)
   \]
   for all nonnegative `phi`, where `mathcal M_R` is a local maximal mean on the base. This transfers small base mean of `F_i` to small cover mean.
5. Apply the same finite-`W^{2,p}` and local Derdziński/projector contradiction on the cover.

Naber-Zhang supplies the regularity framework under additional hypotheses. Their Theorem 1.1 says that if a bounded-Ricci ball is close to a `k`-dimensional Ricci-limit model with residual dimension at most `3` and the fibered fundamental group has maximal nilpotency rank `4-k`, then a lower weak harmonic/conjugate radius bound is obtained; for exact Einstein metrics this upgrades to curvature bounds, while for the present near-Einstein inputs the harmonic-radius part is the relevant input. The constants depend on the lower-dimensional model through a noncollapsing radius, and maximal rank by itself has not yet been shown to imply the deck-averaged deficit transport estimate.

Thus the next mathematical object is not a classification of all thin geometries. It is a precise transport lemma for maximal-rank local covers, first in flat torus and nilmanifold collapse models and then in the Naber-Zhang setting. Failure modes to separate are rank drop, singular fibers, model degeneration, residual four-dimensional bubbles, and cover-ball multiplicity concentrating on a small high-deficit set.

## 8. Topological accounting remains measure-local

For the LeBrun blow-ups,

\[
2\chi(M_i)+3\tau(M_i)=A_i-k_i,
\qquad \chi(M_i)=\chi(X_i)+k_i.
\]

Near the boundary `k_i/A_i -> 1/3`, `A_i-k_i` is approximately `2A_i/3`. A global free circle action forces `chi=0`, but this excludes only a global regular free-circle action. It does not exclude collapse in volume proportion with singular fibers, fixed strata, exceptional regions, or curvature concentration. Any Euler-characteristic argument must locate where the Chern-Weil representative of `chi` lives and connect that concentration either to failure of controlled unwrapping or to non-vanishing normalized local deficits.

## 9. Current research significance

The Derdziński source link is now solid, and the local theorem has been repaired. The result is a family-level measure-local theorem for the near-boundary LeBrun negative route; it does not prove `P_4^-`, `P_4^+`, or Yau 26. It sharply describes any surviving LeBrun-family negative counterexample sequence: almost all of its volume must be locally collapsed at unit scale, while typical collapsed neighborhoods still have small mean LeBrun deficits. Extending the contradiction through local unwrapping of maximal-rank collapsed balls is the most concrete next route.
