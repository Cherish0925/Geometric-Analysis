# Route assessment: Step 92

## Durable corrections

1. **Hyperbolic `X#X` continuity.**  Step 91's Sambusetti/BCG calculation is a sharpening of Step 47, not a new route.  Step 47 already contained the degree-two BCG argument, the all-sign no-Einstein proof for `X#X`, and the lower pinching threshold asymptotic to `1/(4 chi(X))` in normalized variables.  Step 91/92 preserves this with a corrected Ricci-box estimate.

2. **CGB algebra repair.**  For `Ric` eigenvalues `r_i=-3x_i`,
\[
{s^2\over24}-{ |E|^2\over2}={s^2\over6}-{ |Ric|^2\over2}
={3\over2}\left[(\sum_i x_i)^2-3\sum_i x_i^2\right],
\]
not `{3\over2}[(sum x)^2/3-sum x^2]`.  A02 #616 caught the factor error; A01 patched `workspace/notes/step91_sambusetti_bcg_quantitative_route.md` and reran `workspace/scripts/step91_sambusetti_bcg_pinching_threshold.py`.

3. **Lohkamp scaling repair.**  Negative Ricci existence alone does not fit arbitrary tight negative intervals.  If `Ric in [-b,-a]g` and the target interval is `[c,C]=[-beta,-alpha]` with `0<alpha<beta`, constant scaling fits it only when `b/a <= beta/alpha` for sharp extremal bounds.  Two-sided pinching is still substantive.

4. **A02 warped waist barrier.**  A02's warped-product waist obstruction was independently checked in `workspace/scripts/step92_warped_waist_barrier_check.py`, producing `workspace/data/step92_warped_waist_barrier_check.json`.  At a warped waist with `alpha=f''/f>=0`, `beta=2k/f^2>=0`, defect from `Ric=-3g` is
\[
\delta(\alpha,\beta)=\max(3|1-\alpha|, |3-\alpha+\beta|),
\]
with minimum `3/2+3 beta/4`.  This blocks simple flat/spherical warped turnarounds at pointwise defect `<3/2`, but does not prove a general non-warped waist theorem.

## Product-orbifold advance

Step 92 turns the Step 91 AB numerical adjacent coefficient into a sector sign theorem in the principal Step 89/91 normalization.

- The adjacent `m=2` polarizations cancel exactly mode by mode.  In 2D Hessian notation with
\[
C=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]
`JC=S`, `JS=-C`; the sparse receiver is nonzero only for off-diagonal `S`-type derivative matrices, and the adjacent south-pole sign pattern gives relative contributions `+,-,+,-`.  Exact support data: `workspace/data/step92_m2_polarization_cancellation.json`.

- The residual AB adjacent series is
\[
K_\tau^{AB}={1\over512}\sum_{\ell,k\ge1}(-1)^k{(2\ell+1)(2k+1)\mu_\ell\mu_k\over {1\over2}(\mu_\ell+\mu_k)-1}e^{-\tau[{1\over2}(\mu_\ell+\mu_k)-1]}.
\]
Equivalently,
\[
K_\tau^{AB}={1\over512}\int_\tau^\infty e^s A(s)B(s)ds.
\]
TTCS repaired the sign proof: use the dimension-raising identity for spherical heat kernels,
\[
\partial_x p_t^{S^2}(x)=2\pi e^{-2t}p_t^{S^4}(x),
\]
so
\[
B(s)=-16\pi^2 e^{-s}p^{S^4}_{s/2}(-1)<0.
\]
Since `A(s)>0`, the AB adjacent sector is strictly negative and finite:
\[
K_{adj}^{AB}<0,
\qquad K_{adj}^{AB}\approx -0.03144249732
\]
in the current convention.  Support data: `workspace/data/step92_ab_heat_sign_formula.json`; TTCS: `trace/ttcs/results/step92_ttcs01_verifier1_integration.md`.

## Strategic comparison

- The restricted Ishida--LeBrun theorem remains the most mature directly Yau-26-relevant negative result, but is restricted and still needs proof-level analytic checking.
- Hyperbolic `X#X` has the cleanest all-sign no-Einstein reservoir.  Its present bottleneck is a geometric connector mechanism with maximum defect tending to zero, or a general pointwise obstruction extending the warped waist barrier.  Existing BCG/CGB estimates are lower bounds, not constructions and not uniform because their margin is additive in Euler characteristic.
- The product-orbifold mixed-chirality branch is not global enough to settle Yau-26, but it currently has the most concrete executable new mathematics: K-reflection, receiver simplification, adjacent reduction, corrected spectrum, and now a strict AB-sector sign.  It is worth continuing only if the next work attacks the real missing coefficient components rather than proclaiming a local sector result as a global obstruction.

## Next work

Best immediate handoff: Agent2/Execute should develop the full source-compatible adjacent coefficient.

1. Turn the Step 92 AB sign theorem into a clean lemma with exact normalization, quotient factors, and pole-frame conventions.
2. Derive the actual Ozuch/Eguchi--Hanson `H^4` source normalization in this convention and compare it to the Step 89/91 principal source `S_odd=(pi^2/2)R_odd`.
3. Build the AA/BB trace-free tensor-sector computation using the corrected electric/magnetic tensor harmonics, including the `m=0` magnetic mode noted by TTCS.
4. Check Bianchi/gauge projection effects on the source side; receiver-side hidden `V0` corrections are already removed at the product linear layer.
5. Keep the hyperbolic connector route alive only through concrete non-warped connector mechanisms or a general waist theorem, not by repeating the degree-two BCG obstruction.
