# Step 26 consolidated mathematical status

## Advances this step

### R1: General-$p$ weighted tensor inequality — PROVED

The inequality $K_p' + c\|\nabla Z_p\|_2^2 \le Cp^2 r^{-2}K_p + Cp\int\eta^2
a^{p-1}F\Phi^p$ holds for all $p \ge 3$, for both $\Phi = F$ (curvature)
and $\Phi = |E|$ (defect, via $\varepsilon$-regularization).  The derivation
extends A01's index-level $q=2,3$ template.  Key elements:
- Buffer vanishing: $a^{p-1} = 0$ on $\operatorname{supp}d\eta$ for $p \ge 3$
- Transition regularity: $a^{p-3}|da|^2 = 4a^{p-2}|d\chi|^2$
- Uniform dissipation: $c > 0$ independent of $p$ from $p(p-2) \ge p^2/3$
- Polynomial growth: $Cp^3$ after the full Young/Sobolev chain
- Moser convergence: $\sum(j + \log p_j)/p_j < \infty$
- Noninteger exponents: infinitely flat cutoff or $W^{1,\infty}$ approximation

### R2: Initial Sobolev on collapsed balls — RESOLVED

Maheux–Saloff-Coste (Math. Ann. 303, 1995, Theorem 1.1) gives
$$
\mathsf S = C(n, Kr^2) \cdot r^2 \cdot \operatorname{Vol}(B_r)^{-1/2}
$$
on any geodesic ball, requiring only $\operatorname{Ric} \ge kg$.  The
constant $C$ is independent of volume.  For pinching with $K = 1+\delta$ and
the Li radius $r = r_*$, $Kr^2$ is uniformly bounded, so $C$ is uniform.
No noncollapse hypothesis is needed.

### R3: $\bar\beta$ definition and collar — CORRECTED

Active-region energy inequality:
$\widehat H_2' + cD_2 \le C\int\eta^2 aF^3 + Cr^{-2}\widehat H_2$
(no collar additive constant).  Critical absorption:
$\int\eta^2 aF^3 \le \bar\beta(D_2 + r^{-2}\widehat H_2)$ (no $\mathsf S^{-1}$).

### R4: $J_6$ propagation — EXPLICIT CRITICAL ABSORPTION

$p = 6$ critical absorption at the $\bar\beta$ scale, not merely homogeneity.

### R5: First-exit closure — CONDITIONAL ON SMOOTH EXISTENCE

All five first-exit conditions self-improve simultaneously when $\delta$ and
$\bar\beta(0)$ are small enough.  (F3a) uses $\widehat H_2(t) \le 2\widehat H_2(0)$.

## TTCS corrections applied

1. Absorption formula: no extra $\mathsf S^{-1}$ (both in $H_2$ and $J_6$)
2. Collar: active-region inequality has no additive $C_{\rm col}$
3. Defect regularization: correct chain rule for $\Phi_\varepsilon$
4. Noninteger powers: infinitely flat cutoff or $W^{1,\infty}$ approximation
5. (F3a): uses $\widehat H_2(0)$ not $H_2(0)$
6. Dissipation uniformity: from $p(p-2) \ge p^2/3$ for $p \ge 3$

## Single remaining obstacle

### O1: Normalized Yang–Wang smooth continuation

Wang's Theorem 6.3 extends the unnormalized cutoff flow $\partial_tg = -2aRic$
when $|aRm|$ is bounded.  The normalized flow adds $-2ag$, changing:

- Curvature evolution: adds $-2aRm$ (bounded by the existing $|aRm|$ bound)
- Connection variation: adds $\nabla(ag)$ terms (bounded by $C|da| + Ca$)
- Higher derivatives: $\nabla^m(ag)$ involves fixed cutoff derivatives and
  the same metric, all controlled

The structural argument is: Wang's induction couples $|aRm|$, unweighted $L^p$
curvature, derivatives $\nabla^m(aRm)$, and derivatives $\nabla^m\chi$.  At
each level, the new $-2ag$ terms are controlled by the same quantities already
present.  Short-time existence follows from the standard DeTurck/strictly
parabolic approximation since $-2ag$ doesn't change the principal symbol.

This adaptation must still be written as a complete proof.

## Convergence with A01

A01 Step 26 independently derives:
- $J_6 = \int\chi^8|E|^6$ as the starting defect energy
- Yang Appendix B instantiation at $n=4$, $p_0=6$
- Same endpoint $|aE| \le C\delta(r^2/t)^{1/3}$
- Same integrable drift and metric comparison

Both sessions agree that the single remaining analytic task is the
normalized continuation theorem.

## Position relative to Yau 26

Even if the continuation is proved, this establishes only:

> A pinching gap for critical four-dimensional negative Ishida–LeBrun
> manifolds: there exists $\delta_0 > 0$ such that any metric $g$ on such $M$
> with $\|\operatorname{Ric}_g + g\|_\infty \le \delta_0$ satisfies... (contradiction).

This does NOT establish:
- The unrestricted negative branch for arbitrary 4-manifolds
- The positive branch in any dimension
- Dimensions $n \ge 5$
- The full dimension-by-dimension Yau 26 statement
- Lean 4 formalization

## Files

- Main note: `workspace/notes/step26_general_p_and_sobolev_resolution.md`
- Verification: `workspace/scripts/verify_step26_general_p_and_sobolev.py` (exit 0)
- TTCS record: `trace/ttcs/results/step26_ttcs01_verifier1_integration.md`
- Prior notes: `step25_whole_support_moser_and_normalization_repair.md` (superseded
  by this step's corrections)
