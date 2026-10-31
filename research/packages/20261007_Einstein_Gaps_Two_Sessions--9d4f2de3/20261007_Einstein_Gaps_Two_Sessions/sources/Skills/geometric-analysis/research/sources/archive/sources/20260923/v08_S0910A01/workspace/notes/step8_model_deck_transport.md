# Step 8: model deck-averaged deficit transport for collapsed unwrapping

## Purpose

The measure-local theorem in `step8_derdzinski_measure_local_theorem.md` reduces the LeBrun negative near-boundary route to collapse in volume proportion. The next obstruction mechanism requires a local cover that restores noncollapse and also transports small **mean** LeBrun deficit from the collapsed base ball to the cover ball. This note proves the transport estimate in model situations and isolates the exact general lemma needed in the Naber-Zhang setting.

The target estimate is: for a local covering map

\[
\pi:(\widehat U,\hat g)\to(U,g),
\]

and a cover ball `\hat B=B_a(\hat p)`, prove for every nonnegative measurable `\phi` on `U`

\[
\fint_{\hat B}\pi^*\phi\,d\hat\mu
\le C\,\mathcal M_R\phi(p),
\tag{T}
\]

where `\mathcal M_R` is the supremum of base-ball averages over radii up to a fixed multiple of the model scale. If this holds for the explicit deficit density `F_i`, a volume-random basepoint with small base maximal mean yields a noncollapsed cover chart with small pulled-back mean, and the Derdziński/projector contradiction applies on the cover.

## 1. Exact multiplicity identity

For any local Riemannian covering and any measurable cover region `\hat\Omega`, define

\[
m_{\hat\Omega}(x)=\#(\pi^{-1}(x)\cap\hat\Omega).
\]

Then

\[
\int_{\hat\Omega}\pi^*\phi\,d\hat\mu
=
\int_{\pi(\hat\Omega)}\phi(x)m_{\hat\Omega}(x)\,d\mu(x).
\tag{1}
\]

Thus (T) is equivalent to a pushforward density bound

\[
{m_{\hat B}(x)\over \operatorname{Vol}\hat B}
\le C\,{1_{B_R(p)}(x)\over\operatorname{Vol}B_R(p)}
\tag{2}
\]

or a dyadic version controlled by normalized indicators of balls. The sheet count may diverge in a collapsed sequence; what must remain bounded is the **relative** normalized multiplicity.

## 2. Flat torus collapse

Model:

\[
U=B_{2R}^k(0)\times(\mathbb R^m/\varepsilon\mathbb Z^m),
\qquad \hat U=B_{2R}^k(0)\times\mathbb R^m,
\quad n=k+m,
\]

with the product flat metric and `0<epsilon<<R`. Let `\hat B=B_a((0,0))` with `a<=R`.

For a point `x=(y,[z])` in the base, the multiplicity inside `\hat B` is

\[
m_{\hat B}(y,[z])
=
\#\{\ell\in\varepsilon\mathbb Z^m:
|y|^2+|z+
\ell|^2<a^2\}.
\]

The elementary lattice counting bound gives

\[
m_{\hat B}(y,[z])
\le C_m\left(1+{\sqrt{a^2-|y|^2}_+\over\varepsilon}\right)^m
\le C_m'(a/\varepsilon)^m
\tag{3}
\]

when `a>=epsilon` (the nontrivial collapsed case; if `a<epsilon`, multiplicity is uniformly bounded and the estimate is easier). Meanwhile

\[
\operatorname{Vol}\hat B=\omega_n a^n,
\qquad
\operatorname{Vol}B_a^U(0)\asymp \omega_k a^k\varepsilon^m
\]

for `epsilon<<a`, because the base ball contains all fiber directions over a comparable `k`-ball except for harmless boundary effects. Hence

\[
{m_{\hat B}(x)\over \operatorname{Vol}\hat B}
\le {C\over a^k\varepsilon^m}
\le C'{1_{B_a^U(0)}(x)\over\operatorname{Vol}B_a^U(0)}.
\tag{4}
\]

Consequently

\[
\fint_{\hat B}\pi^*\phi\le C\fint_{B_a^U(0)}\phi.
\]

This verifies (T) in the basic regular collapse model. The bound captures exactly why unbounded sheet number is harmless after normalization: the number of lifted sheets and the inverse collapsed fiber volume scale together.

## 3. Bounded-geometry principal circle collapse

Consider a local principal circle model

\[
g=g_B+
ho^2\theta^2
\]

on `U` over a base ball `B_B(2R)`, with `0<rho<<R`, bounded curvature connection on the chosen scale, and fiber length comparable to `rho`. Let `\hat U` be the local cover unwrapping the circle fiber. In a cover ball of radius `a<=R`, a point over a base point `y` has at most `C a/rho` fiber translates inside the cover ball; the cover ball has volume comparable to `a^{k+1}`, while the projected base ball in `U` has volume comparable to `a^k rho`. Therefore

\[
{m_{\hat B}(x)\over \operatorname{Vol}\hat B}
\le {C(a/\rho)\over a^{k+1}}
={C\over a^k\rho}
\asymp {C\over \operatorname{Vol}B_a^U(p)}.
\]

So (T) holds. Controlled mean curvature/warping terms should not change this as long as the fibration is uniformly bilipschitz to the product model on the selected scale and the fiber length is comparable on the base ball. This is exactly the condition that fails near singular fibers or severe warping, and thus provides a useful test rather than a hidden assumption.

## 4. Nilpotent regular collapse model

A natural abstraction for maximal-rank Naber-Zhang collapse is a nilpotent local model. Let `N` be an `m`-dimensional simply connected nilpotent Lie group with a left-invariant metric on the unit scale, and let `\Gamma_\varepsilon` be a lattice whose fundamental domain has volume `v_f(\varepsilon)`. Locally the collapsed fiber is `N/\Gamma_\varepsilon`, and the cover unwraps to `N`.

If the deck orbit satisfies a uniform polynomial counting comparison

\[
\#\{\gamma\in\Gamma_\varepsilon:d_N(z,\gamma z_0)\le r\}
\le C{\operatorname{Vol}_N B_N(r+C\varepsilon)
       \over v_f(\varepsilon)}
\tag{5}
\]

for `r<=a`, and if product/quasi-product volume comparison holds between the base and fiber directions, then the same proof as the flat torus case gives

\[
{m_{\hat B}(x)\over\operatorname{Vol}\hat B}
\le C{1_{B_{Ca}(p)}(x)\over\operatorname{Vol}B_{Ca}(p)}.
\tag{6}
\]

In Mal'cev coordinates (5) is a lattice point estimate in a nilpotent ball. The constant should depend on the step and the bilipschitz control of the chosen graded coordinates, not on the collapsing fundamental-domain volume. This is the deck-counting content one should extract from Naber-Zhang's graded short-generator machinery.

## 5. Conditional lemma for the Yau 26 negative route

**Deck-transport lemma needed.** Suppose a collapsed four-dimensional ball `B_{2R}(p)` with bounded Ricci is close to a `k`-dimensional model with residual dimension at most `3`, the fibered fundamental group has maximal nilpotency rank `4-k`, and the Naber-Zhang construction gives a local normal cover with uniform weak harmonic radius on a ball `B_a(\hat p)`. If, in addition, the associated deck orbit satisfies the normalized counting estimate (6), then for the explicit LeBrun deficit density `F_i`,

\[
\fint_{B_a(\hat p)}\pi^*F_i
\le C\mathcal M_R F_i(p).
\]

A volume-random selection gives `\mathcal M_R F_i(p_i)->0` on any positive-volume family of such points. The cover chart then converges in finite `W^{2,p}` to a smooth Einstein germ with the forbidden calibrated spectrum. Therefore maximal-rank, uniformly modeled, deck-counting-controlled collapse can occupy only vanishing volume fraction.

## 6. What remains outside the model proof

The model proof does not address:

1. **Rank drop.** The local cover may not recover all missing dimensions; Naber-Zhang noncollapse does not apply. Singular torus fibers in K3 collapse are the guiding example.
2. **Model degeneration.** Constants in Naber-Zhang depend on the lower-dimensional model through a noncollapsing radius; if this radius tends to zero, the cover harmonic-radius scale can vanish.
3. **Residual four-dimensional cores.** The residual-dimension `ell<=3` hypothesis is sharp; Eguchi-Hanson-type four-dimensional bubbles are outside the theorem.
4. **Multiplicity concentration.** Without a deck-counting bound, a cover ball could overweight a small high-deficit subset of the base even though the base mean is small.
5. **Vanishing scale.** If the only accessible cover charts occur after rescaling by `R_i->0`, the original calibrated `Ric=-g`, `s=-4`, `|W^+|^2=1/24` profile rescales toward Ricci-flat scale and the same contradiction no longer applies directly.

The next rigorous advance should therefore be to prove the nilpotent deck-counting estimate from Naber-Zhang's graded generators, and then identify whether positive-volume collapsed regions in a hypothetical LeBrun sequence must have maximal rank on a uniform scale or instead force their topology/curvature into the listed failure modes.

## 7. Relation to positive branch calibration

The same transport issue appears in S0910A02's positive-branch program. Tight positive pinching on `#_k(S^2\times S^2)` would have major consequences, but the LeBrun negative inequalities do not directly apply: the Seiberg-Witten general-type monopole input and the sign are absent. What transfers is the mechanism: if positive collapse unwraps to noncollapsed harmonic charts with small mean positive-branch defects, then any special algebraic curvature condition selected by positive pinching should appear on the cover. Conversely, rank-drop and singular strata are where topology can hide.
