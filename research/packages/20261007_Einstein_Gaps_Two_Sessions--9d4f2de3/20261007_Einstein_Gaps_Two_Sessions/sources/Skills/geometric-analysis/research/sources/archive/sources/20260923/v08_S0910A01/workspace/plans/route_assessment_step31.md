# Route assessment after Step 31


**Step 32 superseding audit.**  This assessment overstates the status of the
Step 31 Moser and continuation work.  Use
`workspace/notes/step32_nested_moser_and_tensor_audit.md` and
`workspace/scripts/step32_nested_moser_repair.py` as the active analytic record.
The search for a collapse-independent unnormalized Dirichlet Sobolev constant is
withdrawn; the collapsed-product scaling shows it is false.  The conditional
nested-time recurrence restores the positive-time endpoints
\(\|aF\|_\infty\lesssim\beta/t\) and
\(\|aE\|_\infty\lesssim\delta(r^2/t)^{1/3}\) when the same-support seeds are
available.  The general-\(p\) tensor and regularized-defect derivations remain
unfinished estimate-level work.
## Key advances

1. **General-p tensor power inequality** proved with explicit polynomial $p^3$
   growth in the reaction coefficient.  The derivation tracks all five term
   types (Bochner, cutoff gradient, Hessian, algebraic, metric/volume) from
   the normalized cutoff flow $\partial_tg=-2\chi^2(\operatorname{Ric}+g)$.
   Verification script passes all 9 checks.

2. **Three-factor Hölder absorption** connects the reaction to the cubic
   potential $Y=K_3$ via the identity
   $a^{p-1}F^{p+1}=(aF^3)^{1/3}(a^{p-2}F^p)^{1/3}Z_p^{4/3}$.
   Young absorption converts the reaction into $\varepsilon D_p^F + Cp^3 S^4YK_p$.

3. **Moser convergence** verified: $\sum\log p_k/p_k < \infty$ for the
   geometric sequence $p_k=(3/2)^kp_0$.  Exponent sums in $n=4$: temporal
   $\sum 1/p_k = (n+2)/(2p_0)$, Sobolev $\sum 1/(\kappa p_k) = n/(2p_0)$.

4. **Time-decay correction**: The prior claims $\|aF\|_\infty \le C\beta/t$
   and $\|aE\|_\infty \le C\delta(r^2/t)^{1/3}$ are withdrawn.  The standard
   parabolic Moser output from $L^{p_0}$ on $[0,T]$ is
   $\|u\|_\infty \le C(VT)^{-1/p_0}(\int K_{p_0})^{1/p_0}$.  The
   four-dimensional critical cancellation makes this a **uniform bound**
   $\|aF\|_\infty \le C(S,K_0,\theta)$ on $[T/4,T]$.  The defect Moser from
   $J_6$ gives $\|aE\|_\infty \le C\delta$ (uniform).  Velocity
   $V(T) = O(\delta\theta r^2) \to 0$ as $\delta \to 0$.

5. **m=2 continuation analysis**: The single-$\chi$ Hessian term is NOT
   absorbed by dissipation; it's bounded by $Cr^{-2}A_2(p)^p$ (the unweighted
   $L^p$ norm), entering the Gronwall RHS.  No exact tensor cancellation or
   stronger estimate is needed.  The $a \to a+\varepsilon$ regularization is
   correctly rejected; estimates use $a=\chi^2$ directly.

## Impact on the conditional theorem

The corrections strengthen (not weaken) the conditional theorem:

- **Uniform bounds are sufficient**: $\|aF\|_\infty \le C$ and
  $\|aE\|_\infty \le C\delta$ give metric comparison $e^{-C\delta T}g_0 \le g(T) \le e^{C\delta T}g_0$
  on the support.  For small $\delta\theta$, this closes the bootstrap.

- **Continuation resolves (C1)**: The Codex/A03 shifted-curvature framework
  gives smooth extension using the unweighted $L^p$ induction with the
  weighted Moser bound $\|U\|_\infty \le C$ as the curvature hypothesis.

- **Terminal recalibration needs only $Q(T)/A \to 0$**: The global defect
  $Q_{\text{global}}(T) \le e^{C\theta}Q_{\text{global}}(0)$ combined with
  $Q(0)/A = O(\delta^2) \to 0$ gives the needed terminal calibration.

## Remaining work for the restricted negative 4D route

1. **Validate the full bootstrap/first-exit**: Write the complete closed
   theorem with: initial maximal-function selection, buffered cutoffs, q=2
   energy, q=3 time-averaging, curvature Moser (uniform), J_6 persistence,
   defect Moser (uniform), velocity/metric comparison, continuation.

2. **Macro-disjoint support construction**: formal proof with volume retention,
   coloring, plateau containment of terminal geodesics.

3. **Terminal recalibration**: recompute SW/CGB/tensor-gap on $g(T)$ using
   $Q(T)/A \to 0$ and $\operatorname{Vol}/A$ comparability.

4. **Exponential pullback + Derdziński contradiction**: select controlled
   center, extract Einstein germ, apply the forbidden calibrated profile.

Even completed, this covers only the Ishida--LeBrun near-critical negative-branch
family in dimension 4.  Not settled: positive branch, arbitrary 4-manifolds,
$n \ge 5$, full Yau 26, Lean formalization.

## A02 #328 (noncollapsed dichotomy)

A02's result is useful for the POSITIVE branch in 4D.  Under noncollapse, smooth
GH limits carry Einstein metrics (standard compactness).  The spectral obstruction
$\det R_+ = 0$ identifies where ALE bubbling can occur.  This does not help the
negative branch (which collapses) but opens a parallel positive-branch route.

## Files

- General-p inequality: `workspace/notes/step31_general_p_tensor_power_inequality.md`
- Verification: `workspace/scripts/step31_general_p_verification.py`
- m=2 analysis: `workspace/notes/step31_m2_continuation_analysis.md`
- Patched notes: `step27_unified_weak_moser_iteration.md` (time-decay correction)
