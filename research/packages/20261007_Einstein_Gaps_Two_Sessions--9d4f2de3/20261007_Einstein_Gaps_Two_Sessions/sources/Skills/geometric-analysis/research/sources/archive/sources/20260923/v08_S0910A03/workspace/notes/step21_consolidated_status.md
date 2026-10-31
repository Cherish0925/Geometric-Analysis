# Step 21 consolidated mathematical status

## Architecture established

The derivative-free first-exit theorem separates the cutoff-flow program into two independent layers. Layer A provides zero-order weighted bounds through the Wang-type Moser hierarchy, requiring only metric comparability, relative Sobolev persistence, neighboring curvature energy, and neighboring defect energy. Layer B recovers smooth compactness through interior Shi estimates on the plateau at positive time, eliminating the need for derivative estimates from time zero.

The p > 4 connection-drift threshold (Step 19) and the quantitative weighted Bernstein target are correct but not load-bearing. All derivative bounds come from interior regularity on the normalized Ricci flow $\partial_tg=-2(\operatorname{Ric}+g)$ restricted to $\{\chi=1\}$.

## What is proved

1. **Normalization lower-order structure.** The $-2\chi^2g$ term modifies the curvature hierarchy only through: (a) a volume-form reaction absorbed into the curvature reaction at lower exponent; (b) a Grönwall factor $e^{C_q(\theta+\theta r^2)}$ bounded by 2 for small $\theta$. The critical parameter $\beta=A_0^2\|\operatorname{Rm}\|_2$ is unchanged. (TTCS corrections: use $|a\operatorname{tr}(E)|\le CaF$ during the flow, not $4a\delta$; Grönwall rate includes $r^{-2}$ term.)

2. **Volume-independent critical product.** $\beta=Cr^2\sqrt{K_0}$ and is independent of collapsed volume. This survives the collapse probe of A02 #298: individual Sobolev constants degenerate, but the Sobolev-curvature product does not. (Verified Step 19.)

3. **Uniform work scale.** On a fixed critical Ishida-LeBrun topology with near-Einstein metrics, $K_0\le C(M)$ from Chern-Weil and $\operatorname{Vol}\to32\pi^2A/9$. Hence $r_*=({\varepsilon_{\rm Li}}/{K_0})^{1/4}\ge c>0$ and $T_0=\theta r_*^2>0$ are uniform in the sequence index.

4. **First-exit self-improvement.** With corrected exit conditions (F1) metric, (F2) Sobolev, (F3a) curvature energy, (F3b) defect energy, and derived (F4) curvature, (F5) defect: if the localized Moser iteration holds, all conditions are strictly improved for $\delta$ small enough. Metric drift is $O(\delta\theta^{2/3}r^2)\to0$.

5. **Interior Shi estimates.** On $\{\chi=1\}\times[T_0/2,T_0]$, the normalized Ricci flow satisfies standard Shi estimates via the conformal rescaling $\hat g=e^{2t}g$. All derivative bounds are uniform in $i$. (TTCS confirms: $C_k$ absorbs $K$, buffer width, and time scale.)

6. **Exponential chart and smooth compactness.** Rauch comparison gives noncollapsed chart $h_i=\exp_{p_i}^*g_i(T_0)$ on $B_R(0)$. With all derivative bounds, Arzelà-Ascoli gives $h_i\to h_\infty$ in $C^\infty$.

7. **Projector contradiction.** Einstein $+$ calibrated spectrum $(-1/6,1/12,1/12)$ forces $\nabla W^+=0$ by projector argument, but Einstein-Weyl gives $|\nabla W^+|^2=1/16$. (TTCS confirms the numerical identity.)

8. **Exponent products.** The $q\to3q/2$ Moser recurrence has convergent infinite products (Step 20 script). Endpoint: $|aF|\le C\gamma/t$ from $q_0=2$, $|aE|\le C\delta(r^2/t)^{1/3}$ from $m_0=6$.

9. **A01's corrected nested estimate.** Inner/outer cutoff distinction, shrinking time intervals $I_k\downarrow[3t/4,t]$, Hölder $R_q\le(H_3^{\rm out})^{1/3}K_q^{2/3}$, and the same endpoint powers. (A01 Step 22.)

## What remains to prove

**(U1) Exact tensor inequality.** Equation (2.1) of A01's Step 22 note: the term-by-term derivation from $\partial_tg=-2a(\operatorname{Ric}+g)$ for the curvature moment $H_{q,k}$, including measure evolution, $F$ regularization, inverse-metric variation, all Hessian-$a$ integrations by parts, and contraction structures. This is the ground-truth PDE calculation.

**(U2) Graph absorption for support energy.** $S_\alpha=A_\alpha^4H_{2,\alpha}$ must be propagated by graph absorption: $S_\alpha'\le Cr^{-2}\sum_{\beta\sim\alpha}(A_\alpha/A_\beta)^4S_\beta$. This replaces the invalid assumption that component energy implies Whitney-volume energy.

**(U3) Current cubic potential.** $A^4H_3(t)\le C\Gamma^3/t$ from the graph-semigroup argument on the current support energy. A01's equation (3.5).

**(U4) Fixed $J_6$ persistence.** Before the defect $m\to3m/2$ product, prove that $J_{6,k}(t)$ stays controlled on the positive-time slab $[t/2,t]$ using the same critical absorption.

**(U5) Triangular unweighted $Q$.** $Q_\alpha'\le Cr^{-2}\sum_{\beta\sim\alpha}Q_\beta$ without curvature-only additive source. Absorbs $\int a|\operatorname{Rm}||E|^2$ by Sobolev product.

**(U6) Full joint density selection.** Step 16 framework with nonzero monopole limit $H_\infty\ne0$, eigenline saturation, and platform volume denominator.

## Alternative route: Nash semigroup

TTCS generator identified a potentially simpler path: compress the infinite Moser iteration into a single abstract Nash $L^2\to L^\infty$ estimate on the conformal measure $d\nu=a^{-2}d\mu$. The softer defect rate $|aE|\lesssim\delta(r^2/t)^{1/2}$ (from $J_4$ base instead of $J_6$) still suffices for metric drift. This requires verifying the non-autonomous form conditions. Could replace U1-U4 by a single abstract lemma.

## Scope

Even if all U1-U6 are proved, the result addresses only the critical 4D negative Ishida-LeBrun laboratory: $\inf_g\|\operatorname{Ric}_g+g\|_\infty>0$ on each such $M$. The unrestricted $P_4^-$, the positive branch $P_4^+$, dimensions $n\ge5$, and Lean formalization remain entirely open.

## Evidence

- Main note: `workspace/notes/step21_derivative_free_first_exit_and_plateau_regularity.md`
- Corrections: `workspace/notes/step21_corrections_from_ttcs_and_peers.md`
- Script: `workspace/scripts/verify_step21_derivative_free_first_exit.py` (passed)
- TTCS: `trace/ttcs/results/step21_ttcs01_generator1_integration.md`, `step21_ttcs01_verifier1_integration.md`
- A01 nested estimate: `Sessions/S0910A01/workspace/notes/step22_weak_nested_moment_estimate.md`
- A01 current energy: `Sessions/S0910A01/workspace/notes/step22_current_energy_formulation.md`
