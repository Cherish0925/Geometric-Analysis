# Step 16: Exponential-pullback averaging as a replacement for normal-cover accessibility

## 1. Statement at the strength currently supported

**Step 28 clarification for varying-`A_i` applications.**  The lemma below is a raw integral estimate for any measurable positive-volume set `P`.  To use it when only `A_i^{-1}\int F_i ->0` is known, the selected center set must have fixed normalized volume, e.g. `Vol(P_i) >= alpha A_i`; a merely nonzero volume possibly `o(A_i)` is insufficient.

Let `(M^n,g)` be closed and let `P` be a measurable positive-volume set.  Assume that for every `p in P` and every radial geodesic of length at most `r` from `p`,

\[
-K\le \sec_g\le K,
\qquad 0<r<\pi/(2\sqrt K)
\]

with the evident interpretation when `K=0`.  Let `F>=0` be measurable.  Write polar coordinates on `T_pM` and let

\[
J_p(t,\xi)=\det(d\exp_p)_{t\xi}
\]

be the radial Jacobian.  Define the pulled-back exponential average

\[
A_rF(p)=
{\int_{S_pM}\int_0^r F(\exp_p(t\xi))J_p(t,\xi)\,dt\,d\xi
 \over
 \int_{S_pM}\int_0^r J_p(t,\xi)\,dt\,d\xi}.
\]

Then

\[
\int_P A_rF(p)\,d\mu(p)
\le
C(n,K,r)\int_M F\,d\mu,
\]

where one may take

\[
C(n,K,r)=
{\int_0^r s_{-K}(t)^{n-1}\,dt
 \over
 \int_0^r s_K(t)^{n-1}\,dt},
\quad
s_K(t)=K^{-1/2}\sin(\sqrt Kt),\quad
s_{-K}(t)=K^{-1/2}\sinh(\sqrt Kt).
\]

For small `r`, this constant tends to `1`; for fixed bounded `Kr^2`, it is finite and depends only on `n,K,r`.

## 2. Proof

Rauch comparison under `sec <= K` gives

\[
J_p(t,\xi)\ge s_K(t)^{n-1}
\]

for `t<pi/sqrt(K)`, while `sec >= -K` gives

\[
J_p(t,\xi)\le s_{-K}(t)^{n-1}.
\]

Therefore

\[
A_rF(p)
\le
{1\over |S^{n-1}|\int_0^r s_K(t)^{n-1}dt}
\int_{S_pM}\int_0^r
F(\exp_p(t\xi))s_{-K}(t)^{n-1}\,dt\,d\xi.
\]

Integrate over `p in P` and enlarge `P` to all of `M`.  For each fixed `t`, the geodesic flow on the unit tangent bundle preserves Liouville measure, hence

\[
\int_M\int_{S_pM}F(\exp_p(t\xi))\,d\xi\,d\mu(p)
=|S^{n-1}|\int_M F\,d\mu.
\]

Integrating this identity against `s_{-K}(t)^{n-1}dt` gives the displayed estimate.  No injectivity radius, cut-locus decomposition, deck group, or nilpotent rank enters the argument.  Multiple visits to the same point are counted in the Liouville integral and are harmless because `F` is nonnegative.

## 3. How it interfaces with the Derdziński route

If the unresolved smoothing theorem eventually supplies a positive-volume set `P_i` of centers such that a fixed radius `r` exponential ball has `|sec|<=K` and small pulled-back Ricci defect, then the lemma can replace the previous CFG/normal-cover access step as follows.

Take the explicit Step 8 nonnegative density

\[
F_i=|E_i|^2+(s_i+8\sqrt6|W_i^+|)^2+\mathcal G_i,
\]

where

\[
\mathcal G_i=f_i^2-(a_i)_-^2,
\qquad
f_i={2\over3}s_i-2\sqrt{2/3}|W_i^+|,
\qquad
a_i={2\over3}s_i+2w_i.
\]

If the terminal smoothed closed metric has

\[
{1\over A_i}\int_{M_i}F_i\to0
\]

and the smoothed centers satisfy a fixed normalized lower bound such as `Vol(P_i) >= alpha A_i`, then the averaging lemma selects `p_i in P_i` for which the pulled-back exponential average of `F_i` tends to zero.  The pulled-back metric on `B_r(0) subset T_{p_i}M_i` has uniform curvature bounds.  Rauch lower bounds also give a uniform volume lower bound for smaller metric balls around the origin in the pulled-back domain; standard bounded-curvature/noncollapse estimates then provide harmonic coordinates on a still smaller ball.

On this smaller harmonic chart, the finite-`W^{2,p}` passage from Step 8 applies.  The limit is Einstein with `Ric=-g`, and the pulled-back densities give

\[
s=-4,
\qquad
s+8\sqrt6|W^+|=0,
\qquad
\mathcal G=0.
\]

Thus

\[
|W^+|^2=1/24,
\qquad
\operatorname{spec}(W^+)=(-1/6,1/12,1/12),
\]

and Derdziński Proposition 5 gives the existing local contradiction.

## 4. Advantages over CFG at this stage

The exponential-pullback method bypasses several unresolved pieces of the previous accessibility route:

- no need to identify a nilpotent fibered fundamental group;
- no need to verify maximal rank or residual-dimension hypotheses;
- no deck-transform counting;
- no need for injectivity radius on the base manifold.

It uses only bounded sectional curvature on a buffer and positive center-set volume.  Because the pulled-back domain lives in `T_pM`, local multiple covering is not an obstruction.  The price is that the smoothing theorem must genuinely give sectional-curvature control on radius-`r` geodesics from a positive-volume set of centers; without that, the Rauch constants and smooth pulled-back harmonic-chart passage are unavailable.

## 5. Remaining dependencies

This lemma does not solve the main analytic bridge.  The route still needs a transition-inclusive cutoff-flow theorem producing:

\[
Q_i(t_0)/A_i\to0,
\qquad
|\operatorname{Rm}_{g_i(t_0)}|\le K
\]

on a family of buffered exponential balls whose center set has fixed normalized volume in the varying-`A_i` sequence, with enough metric comparability to retain that volume from the maximal-function selection.  If that theorem is obtained, the post-smoothing geometric step can use this exponential-pullback averaging instead of the heavier CFG normal-cover machinery.
