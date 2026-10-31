# Step 25: First-exit formulation for the buffered cutoff flow

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## Purpose

This note formulates the precise first-exit bootstrap for the buffered
selected-support cutoff flow `\partial_tg=-2\chi^2(\operatorname{Ric}+g)`.
It identifies what is proved, what self-improves, and what remains.

## First-exit conditions

On one selected good support with the buffered geometry from Step 24
(`\operatorname{supp}\chi\Subset\{\eta=1\}`,
`\operatorname{supp}\nabla\eta\subset\{\chi=0\}`), define

\[
T^*=\sup\{t\in[0,\theta r^2]:\text{conditions (F1)--(F3) hold on }[0,t]\},
\]

where:

**(F1) Curvature energy persistence:**
`H_2(t)\le 2H_2(0)`.

**(F2) Absorption parameter smallness:**
`\beta_a(t)=A_\Omega^2\|F(t)\|_{L^2(\operatorname{supp}\chi)}\le 2\beta_0`.

**(F3) Metric comparability on the active support:**
`\tfrac12 g_0\le g(t)\le 2g_0` on `\operatorname{supp}\chi`,
as quadratic forms on each tangent space.

## Self-improvement chain

### (F1) from (F2)+(F3)

Under (F2) and (F3), the tensor energy derivation (Step 25 note) gives

\[
H_2'+cD_2\le C_{\rm react}\int aF^3+C_{\rm loc}r^{-2}H_2.
\]

The reaction absorption (Step 24 eq. (4.1)) requires `C\beta_a<c/4`, which
holds under (F2) for `\beta_0` sufficiently small.  Substitution yields

\[
H_2'\le C_1r^{-2}H_2,\qquad H_2(t)\le e^{C_1\theta}H_2(0).
\]

For `\theta\le\ln2/C_1`: `H_2(t)\le 2H_2(0)`.  **(F1) self-improves.**

### (F2) from (F1)+(F3)

Under (F3), the relative Sobolev constant satisfies
`A_\Omega^2(t)\le C_{\rm met}A_\Omega^2(0)` with
`C_{\rm met}=C(n,L_\eta)` (since metric comparability preserves volume
and Poincaré up to universal factors).  Then

\[
\beta_a(t)\le C_{\rm met}A_\Omega^2(0)\sqrt{H_2(t)}
\le C_{\rm met}\sqrt{2}\,\beta_0.
\]

For `C_{\rm met}\sqrt{2}<2`: **(F2) self-improves from (F1)+(F3).**

### (F3) — Step 26 correction: support-wide weighted velocity is required

**Step 26 supersession.**  The plateau interior regularity discussion below is
useful only for the terminal bounded-curvature plateau and the Derdziński
contradiction.  It does **not** by itself give the metric comparability needed
by the support energy estimates.  The unsupported Step 25 statement that the
transition displacement is proportionally smaller because `a=chi^2<1` is
withdrawn: `|E|` may grow as the cutoff decreases, so `a|E|` must be controlled
directly.

The correct whole-support first-exit condition is the weighted-velocity bound

\[
  V(t)=\int_0^t\|aE(s)\|_{L^\infty(\operatorname{supp}\chi)}\,ds
  \le \varepsilon_{\rm met} .
\]

Then

\[
  e^{-2V(t)}g_0\le g(t)\le e^{2V(t)}g_0,
\]

which transfers the Sobolev constant, cutoff-gradient bounds, and the
smallness of the current critical product `beta_a(t)` on the entire active
support, including the transition.  This weighted estimate does not require an
unweighted transition curvature bound or transition curvature closeness to the
initial metric.

The Step 26 note `workspace/notes/step26_weighted_velocity_and_local_flow.md`
formulates the fixed-p route.  For one fixed `p>2`, set

\[
  J_p=\int\eta^2a^{p-2}|E|^p,
  \qquad z_p=\eta a^{(p-1)/2}|E|^{p/2}.
\]

The expected energy inequality is

\[
  J_p'+c_pZ_p\le C_pr^{-2}J_p+C_p\int\eta^2a^{p-1}F|E|^p,
\]

where the curvature potential is exactly `F z_p^2`.  The same critical
curvature product absorbs it:

\[
  \int Fz_p^2\le C_p\beta_a(t)(Z_p+r^{-2}J_p).
\]

Initial pinching gives `J_p(0)<=C delta^p Vol(Omega)` without any initial
high-power curvature input.  After fixed-p persistence, the remaining analytic
work is a weighted positive-time Moser/mean-value estimate of the form

\[
  \|aE(t)\|_\infty\le C_p\delta(r^2/t)^{2/p},
\]

which is integrable at zero and would improve the whole-support metric
comparison.  For `p=6` this is the earlier integrable exponent
`C delta (r^2/t)^{1/3}`.

Plateau curvature remains downstream: the q=2/q=3 curvature energies first
produce a positive-time finite-exponent bound on plateau balls; then standard
local parabolic regularity gives `|Rm|<=C/t`, and only then do Shi estimates
supply derivative bounds.  The first-exit problem is therefore not reduced to
mere short-time existence; it requires simultaneous continuation carrying
metric comparison, Sobolev control, beta smallness, weighted curvature, and
weighted velocity.

## Current status

| Condition | Self-improvement status |
|-----------|----------------------|
| (F1) H₂ persistence | from (F2)+(F3), conditional on the tensor inequality and current Sobolev/metric control |
| (F2) β_a smallness | from (F1)+(F3), with Sobolev constant control |
| (F3) metric comparability | requires support-wide weighted velocity `int ||aE||_inf dt`, not plateau drift |
| Fixed-p defect persistence | Step 26 exponent ledger supports the route; full index-level proof still needed |
| Plateau bounded curvature | follows only after finite-exponent curvature/Moser, not directly from Shi |

The corrected first-exit argument closes only if the weighted-velocity and
weighted-curvature continuation estimates are proved together with local Ricci
flow existence/extension.

## Files

- Tensor derivation: `workspace/notes/step25_tensor_energy_derivation.md`
- Buffered support: `workspace/notes/step24_buffered_support_energy_test.md`
- Verification: `workspace/scripts/step25_tensor_energy_verification.py`
