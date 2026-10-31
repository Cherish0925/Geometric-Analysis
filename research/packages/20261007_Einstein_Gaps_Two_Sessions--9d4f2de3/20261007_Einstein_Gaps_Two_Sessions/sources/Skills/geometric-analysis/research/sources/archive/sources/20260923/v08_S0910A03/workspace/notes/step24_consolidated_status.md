# Step 24 consolidated mathematical status

## Summary of advances and corrections

### Critical correction: normalization reaction

The conformal piece $h = -2ag$ of the flow velocity **does** produce a linear
curvature reaction $-2a\operatorname{Rm}$ for the fully-lowered tensor $R_{ijkl}$.
The previous claim of zero lower-order reaction was incorrect: it applied to the
mixed tensor $R^l{}_{ijk}$ but missed the index-lowering contribution
$h_{lm}R^m{}_{ijk} = \phi R_{ijkl}$.  Decisive test: $\partial_tg=-2g$ gives
$R_{ijkl}(t)=e^{-2t}R_{ijkl}(0)$, confirming $\partial_tR=-2R$.

The linear term $-2a\operatorname{Rm}$ is a **damping** that improves the energy
estimate: it adds $+4\int\eta^2aF^2$ to the left side of the $H_2$ inequality
and only $4\operatorname{Vol}$ to the right.  Einstein stationarity holds by the
Lichnerowicz identity $\Delta\operatorname{Rm}+Q(\operatorname{Rm})=2\operatorname{Rm}$.

### Downstream chain: precise dependencies

The TTCS verification showed that the $q=2,3$ energy inequalities alone do
not suffice for the full $L^\infty$ bound on the transition.  The corrected
chain uses **interior regularity on the plateau** ($a=1$, non-degenerate) rather
than the whole support:

1. The $q=2$ inequality gives $H_2$ persistence and spacetime $H_3$.
2. The $q=3$ inequality gives $H_3(t)\le C\gamma^3/t$ (terminal bound).
3. On the plateau $\{a=1\}$, the equation is the standard normalized Ricci flow.
4. Standard interior parabolic regularity gives $|\operatorname{Rm}|\le C\sqrt{K_0}/\theta$
   on $B_{3r}$ at time $\theta r^2$, with volume-independent constants.
5. Shi estimates give uniform $|\nabla^k\operatorname{Rm}|\le C_k$ on the plateau.
6. $C^\infty$ compactness and the $7/24$ calibration inequality give the
   calibrated Einstein germ with forbidden $W^+$ spectrum.
7. The projector contradiction excludes the germ.

### Interior regularity bridge

The bridge from energy control to smooth compactness is verified:
- Scale relationships for Vitali thinning with retained positive volume.
- Volume-independent curvature bound on the plateau from the critical parameter.
- Sequence-uniform derivative bounds from Shi estimates.
- Exponential-chart compactness leading to an Einstein limit.
- Calibrated $W^+$ spectrum $(-1/6,1/12,1/12)$ with $|W^+|^2=1/24$.
- Constant-spectrum lemma forces $\nabla W^+=0$, contradicting the Lichnerowicz
  identity.  Local symmetry check: $|W^+|^2=1/24$ matches neither $H^4$ ($W^+=0$)
  nor $CH^2$ ($|W^+|^2=1/6$).

## Remaining load-bearing PDE work

T1. Exact $(0,4)$-tensor evolution for $F^2$ under $\partial_tg=-2a(\operatorname{Ric}+g)$,
    including the $-4aF^2$ damping.
T2. Separate $q=3$ tensor inequality with Sobolev variable $u=aF^{3/2}$.
T3. Homogeneous defect inequality for $Q$ and $J_6$.
T4. Interior Shi on the plateau, adapted to the normalized flow.
T5. Yang-Wang continuation for the normalized cutoff flow.

## Scope

The conditional gap theorem addresses only the critical 4D negative Ishida-LeBrun
subclass.  The positive branch (A02's toric BREAK shows integral identities
are insufficient), higher dimensions (KK collapse is Einstein-compatible in
$n\ge5$), and Lean formalization remain open.

## Files

- `step24_corrected_evolution_and_conditional_gap.md` — main corrected note
- `verify_step24_exact_curvature_variation.py` — schematic structure (corrected)
- `verify_step24_normalization_correction.py` — decisive test and correction
- `verify_step24_downstream_chain.py` — scaling and exponent checks
- `verify_step24_interior_regularity_bridge.py` — bridge verification
- `trace/ttcs/results/step24_ttcs01_verifier1_integration.md` — TTCS corrections
