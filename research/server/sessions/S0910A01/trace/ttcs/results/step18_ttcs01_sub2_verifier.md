# TTCS Independent Branch Record

```json
{
  "step_id": 18,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step18_weighted_cutoff_system.md",
    "Sessions/S0910A01/workspace/notes/step17_support_scale_li_bootstrap.md",
    "Sessions/S0910A03/workspace/notes/step17_normalized_cutoff_flow_theorem.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Sessions/S0910A01/workspace/scripts/step18_weighted_cutoff_algebra.py",
    "Sessions/S0910A01/workspace/scripts/step18_energy_absorption_terms.py",
    "Sessions/S0910A01/workspace/scripts/step18_degenerate_model_heat_kernel.py",
    "Sessions/S0910A01/workspace/scripts/step18_constant_diffusivity_weight_scaling.py"
  ]
}
```

## Task

Verify the Step 18 refined cutoff-flow analysis for the four-dimensional negative LeBrun route. Please read the corrected Step 18 note, the patched Step 17 support-scale note, the A03 Step 17 cutoff-flow note, Li's source theorem passages, and the Step 18 scripts. Check: (1) the weighted scalar identity for f=a|Rm| and the conclusion that the quadratic reaction is f^2 rather than f^2/a; (2) whether the integrated principal energy can avoid pointwise Hessian cutoff assumptions at least in the scalar model and what remains tensorially; (3) whether the coupled L2 layer is legitimately separated from the remaining pointwise smoothing problem; (4) whether unweighted Q(t) is correctly kept distinct from weighted aE; (5) whether the model computations support but do not prove degenerate epsilon-regularity. Give a direct scientific memo with corrections or a sharper theorem target; do not turn this into final-route control.

## Output

# Verification Memo: Step 18 Weighted Cutoff-Flow Analysis (λ<0 LeBrun Route)

Prepared after reading the Step 18 note (S0910A01), the patched Step 17 support-scale note (S0910A01), the A03 Step 17 cutoff-flow note, Li's paper [0911.3104] Theorems 3.1/3.4/3.6 and Corollary 3.5, and the four Step 18 scripts.

## 1. Weighted scalar identity for f = a|Rm| — correct

I reproduced the identity by hand. With $a=\chi^2$ time-independent, $K=f/a$,
$$
\Delta(f/a)=a^{-1}\Delta f-2a^{-2}\langle\nabla a,\nabla f\rangle+2fa^{-3}|\nabla a|^2-fa^{-2}\Delta a,
$$
so
$$
a^2\Delta K=a\Delta f-2\langle\nabla a,\nabla f\rangle+\Big(\tfrac{2|\nabla a|^2}{a}-\Delta a\Big)f,
$$
matching (3.1)/(5.1) exactly. Since $a$ is time-independent, $\partial_t f=a\partial_t K$ turns $caK^2$ into $c(aK)^2=cf^2$. The reaction is genuinely $cf^2$, not $cf^2/a$, and $|\nabla a|^2/a=4|\nabla\chi|^2$ removes the inverse-cutoff singularity. This is a real structural improvement and the sympy check in `step18_weighted_cutoff_algebra.py` is a faithful confirmation of the product rule.

One point to keep visible: the starting inequality $\partial_t K\le a\Delta K+caK^2+T$ is a scalar reduction of a tensor evolution. Under $\partial_t g=-2aE$ the true curvature evolution carries commutator terms $\nabla a*\nabla Rm$ and $\nabla^2 a*Rm$ inside $T$ (A03 Section 6 confirms the induced Riemann change is $O(\nabla^2\chi^2)$). Passage from the tensor Bochner identity for $\partial_t|Rm|^2$ to a scalar inequality for $f=a|Rm|$ needs the Kato step, and the constant $c$ and the composition of $T$ are only established on the plateau ($a=1$); on the transition they must be read off the actual tensor equation. The scripts do not touch this — they verify the formal product rule and the reaction scaling only.

## 2. Integrated principal energy without pointwise Hessian — verified in the scalar model; a tensor source remains

I recomputed the scalar energy test against $\eta^2 f$. Collecting all $\langle\nabla a,\nabla f\rangle\,\eta^2 f$ contributions: $-1$ (from $\int\eta^2 f\,a\Delta f$), $+2$ (from integrating $-\int\eta^2 f^2\Delta a$ by parts), $-2$ (from the drift $-2\langle\nabla a,\nabla f\rangle$), summing to a single $-\int\eta^2 f\langle\nabla a,\nabla f\rangle$, exactly the residual in the script's `energy_density`. No $\Delta a$ survives; the residual is bounded by Young against the dissipation $\int\eta^2 a|\nabla f|^2$ and the potential $\int\eta^2 f^2|\nabla a|^2/a=4\int\eta^2 f^2|\nabla\chi|^2\le Cr^{-2}\int\eta^2 f^2$. So in the scalar model the integrated principal energy needs only $|\nabla\chi|$, never $|\nabla^2\chi|$. Confirmed.

Tensorially there is still a genuine $\nabla^2 a*E*Rm$ source (and, in the curvature energy, $\nabla^2 a*Rm*Rm$). I checked the curvature case explicitly: integrating $\int\eta^2\,\nabla^2 a*Rm*Rm$ by parts produces $\int\eta^2|\nabla a||\nabla Rm||Rm|$ plus $\int\eta|\nabla\eta||\nabla a||Rm|^2$. Because $|\nabla a|=2\sqrt a\,|\nabla\chi|$, the first term pairs $\sqrt a|\nabla Rm|$ (the weighted dissipation density $\sqrt{X_\alpha}$) with $|\nabla\chi||Rm|$, giving $\varepsilon X_\alpha+Cr^{-2}R_\alpha$; the second is $\le Cr^{-2}\sqrt a|Rm|^2\le Cr^{-2}R_\alpha$. So the pointwise Hessian can be avoided at the $L^2$ level for the tensor as well — but this is not what any of the four scripts verify. They confirm only the scalar product rule and the dimensional scaling. The tensor integration-by-parts producing absorbable first-derivative products is asserted (Section 5.3, Section 7) and is plausible per my hand check, yet it is the piece that a symbolic or careful written derivation should certify before it is treated as settled.

## 3. Separation of the coupled L² layer from the pointwise smoothing problem — conceptually sound, but the "unconditional" labeling of the L² layer overstates the coupling

The distinction between (i) $L^2$ energy persistence $\sup_\alpha R_\alpha(t)\le2\varepsilon_*$ and (ii) the pointwise weighted bound $|a\,Rm|\le C/t$ is legitimate: (ii) is strictly stronger and is correctly isolated as the open degenerate $\varepsilon$-regularity object. I checked the critical absorptions and they are internally coherent:

- $\int a|Rm||E|^2=\int|Rm||\chi E|^2\le\|Rm\|_2\|\chi E\|_4^2\le A_U\|Rm\|_2\int|\nabla(\chi E)|^2$, with $A_U\|Rm\|_{L^2(U)}=O(\sqrt{K_0}\,r^2)$. With $r_*=(\varepsilon_{Li}/cK_0)^{1/4}$ this equals $\sqrt{\varepsilon_{Li}/c}$, small and volume-independent. The A01 scripts (`step18_energy_absorption_terms.py`, `step18_sobolev_scaling.py`) confirm $A_U\|K\|_2=\sqrt{K_0}\,r^2$ is unchanged from volume $1$ to $10^{-24}$, and the general-dimension version $A_U\|Rm\|_{L^{n/2}}\sim K_0^{2/n}r^2$. This collapse cancellation is real.
- The cubic $\int a|Rm|^3$ absorbs identically with the same smallness.
- The cross term $\int|\nabla a||\nabla E||Rm|$: using $|\nabla a|=2\sqrt a|\nabla\chi|\le C\sqrt a/r$, Young gives $\varepsilon\int a|\nabla E|^2+Cr^{-2}\int|Rm|^2=\varepsilon Y_\alpha+Cr^{-2}R_\alpha$. Clean, and it needs no Hessian.

So the coupled system (C) closing to $\dot H_\alpha+c'(X_\alpha+Y_\alpha)\le Cr^{-2}\sum_\beta H_\beta$ with Gronwall persistence is structurally believable.

The point that needs correction is the A03 status table entry "Coupled L² energy propagation — **Proved** (unconditional on smooth flow existence)" together with Section 2 and Section 9's assertion that metric equivalence is a free INPUT. Running (C) presupposes: short-time smooth existence, a fixed-geometry background with metric equivalence over $[0,t]$, and preserved Sobolev/volume constants. Metric equivalence in A03 Section 2 is derived from $|E(t)|\le\sqrt2\,\delta$, which is itself the OUTPUT of the corrected Proposition 1 (conditional on $\int_0^t\|a\,Rm(g(s))\|_\infty\,ds<\infty$). Even on the plateau, the defect reaction $4a\,Rm(E,E)$ in the identity $(*)$ needs $\|a\,Rm\|_\infty$; there is no route to $|E(t)|\le\sqrt2\delta$ that bypasses a curvature bound. So metric equivalence, weighted curvature control, weighted defect control, Sobolev persistence, and $L^2$ persistence are one entangled system, not a proved base plus one open apex.

A01's Step 17/18 framing — "the joint continuation package remains the decisive open analytical theorem" and the whole downstream chain marked explicitly conditional — is the defensible statement. The A01/A03 discrepancy on this point should be reconciled toward A01. The correct summary is: (C) closes *given* short-time existence and metric equivalence on the interval; those are coupled to the very weighted pointwise bounds that remain open.

## 4. Unweighted Q(t) versus weighted aE — the distinction is correct and one route to Q is stronger than stated

Metric speed is $|\partial_t g|_g=2a|E|$, so metric comparability integrates the weighted quantity $\int_0^t\|aE\|_\infty$; the LeBrun–Chern–Gauss–Bonnet recalibration $I(h_i)-J(h_i)=A_i-k_i$ integrates the *unweighted* $Q(t)=\int_M|E|^2$ over the whole manifold, including the frozen region ($a=0$, $g=g_0$, $|E|=|e_i|\le\delta_i$) and the transition. A weighted pointwise bound for $aE$ gives no unweighted information where $a\to0$. Keeping these two objects separate (A01 Sections 4, 6.1) is correct and necessary.

An additional observation worth developing: A01's defect energy inequality (5.2) controls $Q$-growth through $\int a|Rm||E|^2$ absorbed by $\|Rm\|_{L^2}$ smallness (the Sobolev cancellation), i.e. through the coupled $L^2$ curvature bound, **not** through pointwise $\|Rm\|_\infty$. This is the right route and it could deliver unweighted $Q(t)\le CQ(0)$ (hence $Q(t)/\mathrm{Vol}\to0$) from the $L^2$ layer alone. By contrast A03 Section 8 derives the same $Q$-bound from $\frac{d}{dt}Q\le C(r^{-2}+K_0)Q$ with "$K_0=\sup|Rm|$ bounded on the transition because the metric barely moves" — this reuses the pointwise curvature control and the metric-equivalence loop of Section 3, so it is circular for the transition. The A01 $L^2$ route is the one to pursue for $Q$; if it holds on a metric-equivalent background, unweighted $Q$ persistence is closer to reach than the pointwise smoothing object, and this difference in status should be recorded.

## 5. Model computations — support without proof, and one drift-sign to correct

**Constant-diffusivity model** (`step18_constant_diffusivity_weight_scaling.py`): the heat kernel for $\partial_t=a\Delta$ has $L^{n/2}\!\to\!L^\infty$ norm $(at)^{-1}$, so $\|aK\|_\infty\lesssim t^{-1}\|K_0\|_{L^{n/2}}$ independent of $a$. Correct, but this checks only the homogeneity of the target $|aRm|\le C/t$ with the degeneracy switched off; it is a consistency check, not evidence for the degenerate operator.

**Normal cutoff model** $a=x^2$ (`step18_degenerate_model_heat_kernel.py`): the reduction is right — with $y=\log x$, $x^2K_{xx}=K_{yy}-K_y$, so $K_t=K_{yy}-K_y$. But the heat-drift kernel in the script has the drift reversed. Solving $u_t=u_{yy}-u_y$ (Fourier: $\tilde u_t=(-k^2-ik)\tilde u$, so $\tilde u=\tilde u_0 e^{-ikt}e^{-k^2t}$) gives $u(y,t)=\int(4\pi t)^{-1/2}e^{-(y-z-t)^2/(4t)}u_0(z)\,dz$, kernel centered at $z=y-t$. The script uses `exp(-((y-z+t)**2)/(4t))`, centered at $z=y+t$ — the opposite drift, corresponding to $u_t=u_{yy}+u_y$.

I checked whether this overturns the conclusion. The Cauchy–Schwarz operator-norm weight $e^{-z}$ in `norm_bound_at_y` and the $L^2(dx)$ spike normalization $e^{+z}$ are mutually consistent (both correct for $\|K_0\|_{L^2(dx)}^2=\int u_0^2 e^z dz$). Recomputing $I=\int G^2 e^{-z}dz$ with the correct drift replaces the script's $t$-factor $e^{-y-t/2}$ by $e^{-y+3t/2}$; the $\sup_y$ is still attained at $y=0$ (the $x=1$, plateau side) with $\sqrt I\sim e^{-y/2}$ giving $e^{2y}\sqrt I\sim e^{3y/2}$, and a spike at $z_0\to-\infty$ still yields weighted output $\sim e^{3z_0/2}\to0$. So the qualitative message — bounded weighted output from unit $L^2(dx)$ curvature, near-edge spikes damped, maximum away from where $\chi$ vanishes — is stable under the correction. The specific numbers ($C(t)\sim t^{-1/4}$, the spike-decay table) should be regenerated with the correct kernel before being cited. As the note itself states, this frozen linear one-dimensional model omits tangential variables, nonlinear reaction, tensor cutoff terms, and the coupled $E$ system, so it supports plausibility only.

## Sharper theorem target

The pieces above point to a cleaner formulation of the single load-bearing object. State the transition estimate as a **joint** short-time result rather than a proved-base-plus-one-apex, because metric equivalence, weighted curvature, weighted defect, Sobolev persistence, and $L^2$ persistence close together:

> Let $(M^4,g_0)$ be closed with $|Ric_{g_0}+g_0|\le\delta$ and $\bar K=\mathrm{Vol}^{-1}\int|Rm|^2$ bounded. Let $\chi$ be the good-set cutoff at the fixed Li scale $r_*=(\varepsilon_{Li}/c\bar K)^{1/4}$. For $\partial_t g=-2\chi^2(Ric+g)$ on $[0,\theta r_*^2]$, prove **simultaneously**: (a) smooth existence on $\{a>0\}$ with frozen exterior; (b) metric comparability from $\int_0^t\|aE\|_\infty<\infty$; (c) coupled normalized $L^2$ persistence $\sup_\alpha R_\alpha\le2\varepsilon_*$; (d) the degenerate weighted $\varepsilon$-regularity $R_\alpha\le\varepsilon_*\Rightarrow\|a\,Rm\|_\infty\le C/t$ under $\partial_t-a\Delta$, with constants independent of collapsed volume; and (e) unweighted $Q(t)\le CQ(0)$ from (c) via the Sobolev-cancellation defect inequality, *not* from a pointwise $\|Rm\|_\infty$ bound.

Item (d) is the true remaining mathematical core; on $\{a=1\}$ it is Li's Theorem 3.4, but its use there still requires closing Li's all-centers supremum when covering balls of plateau-edge centers sample the transition dynamics (A01 Section 4 states this correctly; A03 Section 9(B)'s "trivial on both regions" understates it, since the buffer secures the initial energy condition but not the dynamical supremum under the cutoff flow). Items (b), (c), (e) are coupled to (d) and to each other and should be proved as one package.

## What remains unresolved

- The tensor integration-by-parts that removes $\nabla^2 a*E*Rm$ and $\nabla^2 a*Rm*Rm$ into absorbable first-derivative products is plausible by my hand check but is not certified in the artifacts; a written or symbolic tensor derivation would settle it.
- The degenerate weighted $\varepsilon$-regularity (item d) is genuinely open; the two toy models indicate compatibility with $|aRm|\le C/t$ but give different exponents ($t^{-1}$ constant-coefficient, $t^{-1/4}$ in the 1D log model), neither of which is the four-dimensional answer.
- Closing Li's all-centers supremum on a finite plateau under the cutoff flow (no finite propagation) is the concrete reason the plateau smoothing is not a corollary of the radius bookkeeping.
- Everything here concerns only the critical Ishida–LeBrun $\lambda<0$ four-dimensional families; the $\lambda>0$ branch, dimensions $n\ge5$, and the Lean 4 formalization are untouched by this step.