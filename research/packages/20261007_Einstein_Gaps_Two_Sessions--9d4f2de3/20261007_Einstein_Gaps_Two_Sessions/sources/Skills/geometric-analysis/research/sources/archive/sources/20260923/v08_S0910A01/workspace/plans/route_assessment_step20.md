# Route assessment after Step 20

## What changed

Step 20 tested the structural simplification suggested by the Strategist:
`E=Ric+g` is a contraction of curvature plus the metric, and `nabla E` is a
contraction of `nabla Rm`.  This changes the analytical target for the Whitney
cutoff flow.

## Established in this step

1. **Closed curvature-power ledger.**  For

   `partial_t g = -2 chi^2 (Ric+g)`, `a=chi^2`, `F=(1+|Rm|^2)^(1/2)`, testing
   against `eta^2 F^(q-2) Rm` gives after integrating Hess(a) by parts:

   `d/dt int eta^2 F^q + c q int eta^2 a F^(q-2)|nabla Rm|^2`

   `<= C q int eta^2 a F^(q+1) + C q^3 int eta^2(|da|^2/a + a)F^q + C q int a|nabla eta|^2 F^q`.

   The terms with `nabla E` close because `|nabla E| <= C|nabla Rm|`; no separate
   high-power defect-gradient energy is needed for the curvature layer.  TTCS
   added two repairs now incorporated in the note: the linear `a Rm` term belongs
   to the algebraic curvature variation rather than solely to `a nabla^2E`, and
   the regularized norm gives `beta <= C sqrt(1+K0) r^2`.  The script
   `workspace/scripts/step20_tensor_closed_curvature_energy.py` records the term
   ledger and exponent bookkeeping.

2. **Direct all-exponent critical absorption remains unproved.**  The reaction
   term can be absorbed using the 4D Sobolev product `beta <= C sqrt(1+K0) r^2`,
   but the threshold worsens with the exponent.  The better route is to create
   one finite exponent `q0>2` at positive time and then use a mean-value argument
   with a supercritical curvature potential.

3. **Correct triangular defect estimate.**  The inherited Step 19 sentence
   that `Q(T)<=C Q(0)` follows from an inequality containing `+epsilon X` was
   repaired.  At fixed smoothing scale an `O(A)` integral of `X` would leave an
   `O(epsilon A)` error, not `o(A)`.  The valid form must use the homogeneous
   equation for `E`: after integrating Hess(a) by parts, curvature appears as
   `a|Rm||E|^2` (the earlier stray `(nabla a)*Rm*E` term is removed) and can be
   absorbed into defect dissipation by the same 4D Sobolev product.  The resulting
   finite-neighbor inequality is

   `dQ_alpha/dt <= C r^{-2} sum_{beta~alpha} Q_beta`, hence
   `Q_support(theta r^2) <= exp(C theta) Q_support(0)`.

   The script `workspace/scripts/step20_triangular_defect_energy.py` records this
   and illustrates why the additive form fails to preserve `Q/A -> 0`.

4. **Patched inherited note.**  `workspace/notes/step19_whitney_tensor_estimate.md`
   now points to the Step 20 replacement for the unweighted defect estimate and
   for the all-exponent iteration wording.

## Current mathematical state

The Whitney reduction remains valuable: cutoff-level degeneracy and collapsed
volume still cancel on each adapted ball.  Step 20 improves the tensor structure:
the curvature regularity layer can be studied as one closed curvature equation,
not as a full two-field high-power system.  The remaining hard PDE problem is
more precise:

- prove the localized power inequality rigorously with all curvature variation
  contractions and evolving-measure terms;
- use it to create a fixed supercritical curvature exponent at positive time on
  Whitney cylinders, without assuming such initial data;
- derive the pointwise weighted curvature bound or an equivalent positive-time
  mean-value estimate;
- prove the triangular support-summed defect estimate for `Q/A -> 0`.

A03's `p>4` Bernstein threshold remains relevant for controlling connection and
cutoff-Hessian drift if the later first-exit argument needs those derivative
bounds, but it is no longer needed as a separate high-power input for the
curvature energy itself.

## Best next work

Agent2 should turn the Step 20 ledger into a rigorous local proposition: write
index contractions for the curvature variation under `h=-2aE`, prove the
inequality for `F^q`, and choose a fixed exponent `q0` for which the 4D Sobolev
absorption is feasible.  In parallel or afterward, Agent3 should test the
finite-exponent-plus-mean-value route by implementing a model parabolic iteration
with q-dependent constants to see what time/exponent regime is plausible.  The
unweighted `Q` estimate should be developed from the triangular identity, not
from any additive curvature-dissipation remainder.

This still addresses only the critical four-dimensional negative
LeBrun/Ishida-LeBrun laboratory.  The full Yau 26 proposition, positive branch,
higher dimensions, and Lean formalization remain open.

## TTCS verification update

TTCS verified the main structural simplification but sharpened the theorem target.
The `E` equation must not contain a `(nabla a)*Rm*E` term; curvature enters as the
potential `a Rm*E` (and `aE*E`) so the unweighted defect estimate remains
triangular.  The regularized norm changes the Sobolev product to
`C sqrt(1+K0) r^2`.  The finite-exponent route cannot assume initial `L^{q0}`;
it must create a positive-time `L^3` or fixed `L^{q0}` estimate from local `L^2`
persistence, following the pattern of Li source lines 245-255.  New script:
`workspace/scripts/step20_finite_exponent_route.py`.
