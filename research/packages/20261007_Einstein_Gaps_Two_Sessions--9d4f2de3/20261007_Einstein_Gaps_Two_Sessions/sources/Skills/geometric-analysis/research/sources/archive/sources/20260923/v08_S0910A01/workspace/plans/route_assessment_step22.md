# Route assessment after Step 22

## Main correction to Step 21 and first Step 22 formulation

The available support input is

\[
\int_UF^2\le M\operatorname{Vol}(U),
\qquad M\simeq1+K_0,
\]

not a Whitney-volume-normal bound on every smaller ball.  For `U=B_{5r}(p)`, `y in B_{4r}(p)`, and `W=B_ell(y)`, the nonconcentric comparison uses `U subset B_{9r}(y)` and gives

\[
\ell^4\fint_WF^2\le CMr^4.
\]

The local mean can grow like `chi0^{-4}`.  Thus `int_W F^2 <= C M Vol(W)` should not be used unless supplied by an additional local mean or genuine cover input.

What survives is the four-dimensional critical product

\[
A_W^2\|F\|_{L^2(W)}\le Cr^2\sqrt M.
\]

A02's collapse test reinforces the same point: raw downstairs `L^2` energy may vanish in thin products/cusps while relative Sobolev constants grow, so every smoothing estimate must retain `A^2||F||_2` or work on a buffered cover where the flow and means are transported correctly.

## Correct energy variable

The first-exit energy should be carried as

\[
S_\alpha=A_\alpha^4H_{2,\alpha},
\qquad
\Gamma(t)=\sup_\alpha S_\alpha(t)^{1/2},
\]

on finite-neighbor support domains with outer cutoffs.  Neighbor Sobolev coefficients must be comparable.  The desired graph estimate is

\[
S_\alpha'\le Cr^{-2}\sum_{\beta\sim\alpha}
(A_\alpha/A_\beta)^4S_\beta.
\]

With bounded degree and comparable `A_alpha`, this gives

\[
\Gamma(t)\le e^{CN\theta/2}\Gamma(0),
\qquad 0\le t\le \theta r^2,
\]

up to fixed comparability constants.  The graph absorption must be written carefully because neighbor dissipations cannot be absorbed into a single component one by one.

## Cubic potential and positive-time moments

After the support-energy loop is established, the cubic potential should be obtained by the same graph system:

\[
A_\alpha^4H_{3,\alpha}(t)\le C\Gamma_*^3/t.
\]

Positive-time spreading is along the bounded-degree graph, so a graph semigroup or exponentially weighted local sum should replace any statement that only a fixed neighbor star enters after time `t`.

The weak nested moment estimate now uses outer cutoffs:

\[
H_q=\int\eta^2a^{q-2}F^q,
\qquad v_q=\eta a^{(q-1)/2}F^{q/2}.
\]

The reaction is controlled as

\[
R_q\le (H_3^{out})^{1/3}K_q^{2/3},
\qquad
K_q\le H_q^{1/2}\|v_q\|_4^2.
\]

This replaces the false same-cutoff equality `H_{2q}^{1/2}=||v_q||_4^2`.  Time intervals for the recurrence are now shrinking:

\[
I_k=[t/2+t(1-2^{-k})/4,t].
\]

With these corrections, the A03 `q -> 3q/2` infinite product remains a valid conditional implication from the weak time-space estimate.

## Transition and plateau use

Small metric displacement from `int |aE| dt` gives bilipschitz comparison only; it does not keep curvature close to its initial value.  No pointwise transition curvature inference should be used.  The geometric contradiction needs bounded curvature on plateau buffers and preservation of unweighted defect through the transition.

The weaker terminal estimate

\[
|a\operatorname{Rm}(T)|\le Cr^{-2},
\qquad T=\theta r^2,
\]

is still enough for finite plateau curvature where `a=1`, provided `r` is selected uniformly for the family under study.  Stronger `Gamma/t` estimates remain useful for smallness-sensitive absorption and velocity bounds.

## Current mathematical tasks

1. Write the exact tensor inequality for `H_q` under `-2a(Ric+g)` with measure terms, inverse-metric terms, regularized `F`, and all Hessian-`a` integrations by parts.
2. Prove graph absorption and current `Gamma(t)` persistence for `S_alpha=A_alpha^4H_2,alpha`.
3. Derive the graph-semigroup cubic potential `A^4H_3<=C Gamma^3/t`.
4. Prove fixed `J_6` persistence and then the weighted defect `m -> 3m/2` product.
5. Prove the unweighted triangular defect estimate `Q'_alpha<=Cr^{-2}sum Q_beta` without curvature-only sources.
6. Produce plateau curvature over a short positive time interval and use exponential-pullback averaging to connect to the Step 8 calibrated Derdzinski contradiction.

This line remains restricted to the critical four-dimensional negative LeBrun/Ishida--LeBrun laboratory.  It does not solve the positive branch, arbitrary four-dimensional no-Einstein manifolds, dimensions `n>=5`, the original all-dimensional proposition, or Lean formalization.

Files: `workspace/notes/step22_current_energy_formulation.md`, `workspace/notes/step22_weak_nested_moment_estimate.md`, `workspace/scripts/step22_energy_normalization.py`, `workspace/scripts/step22_first_exit_energy.py`, `workspace/scripts/step22_weak_moment_ledger.py`.
