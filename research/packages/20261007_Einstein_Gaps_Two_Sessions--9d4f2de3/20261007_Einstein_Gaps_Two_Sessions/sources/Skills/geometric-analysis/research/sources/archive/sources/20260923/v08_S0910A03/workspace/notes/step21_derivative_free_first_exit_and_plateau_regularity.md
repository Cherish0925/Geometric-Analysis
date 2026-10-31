# Step 21: Derivative-free first-exit theorem and interior plateau regularity

## 1. Structural advance

This step introduces a two-layer separation that simplifies the cutoff-flow program and eliminates the need for derivative estimates from time zero.

**Layer A (Zero-order weighted bootstrap):** Run the cutoff flow $\partial_tg=-2\chi^2(\operatorname{Ric}+g)$ on the closed manifold. Use the first-exit framework with conditions involving only metric comparability, relative Sobolev, neighboring $L^2$ energy, and the weighted curvature bound $|\chi^2\operatorname{Rm}|\le C\gamma/t$. These are all zero-order quantities. The first-exit cycle self-improves for small enough $\delta$ and flow time $\theta r^2$.

**Layer B (Interior regularity at positive time):** On the plateau $\{\chi=1\}$, the flow is the standard normalized Ricci flow $\partial_tg=-2(\operatorname{Ric}+g)$. The weighted curvature bound gives $|\operatorname{Rm}|\le C\gamma/t$ there. Standard Shi interior estimates at any $t_0>0$ give $|\nabla^k\operatorname{Rm}|\le C_k$ with constants depending only on $n$, $k$, and $\gamma/t_0$. These are uniform along the pinching sequence.

The p>4 connection-drift threshold (Step 19) and the global weighted Bernstein target are mathematically correct but no longer load-bearing for the first-exit closure. The hard PDE work is concentrated on the zero-order weighted Moser iteration (the exact nested finite-neighbor recurrence), not on derivative propagation.

## 2. Qualitative smooth continuation

**Proposition 1** (Extension criterion). Let $(M^4,g_0)$ be closed with smooth cutoff $\chi$, $a=\chi^2$. The flow $\partial_tg=-2a(\operatorname{Ric}+g)$ has a unique smooth solution on $[0,T_{\max})$. If $T<T_{\max}$ and $\sup_{M\times[0,T]}|a\operatorname{Rm}|<\infty$, then $T_{\max}>T$.

*Mechanism.* Short-time existence: DeTurck gauge applied to the degenerate system with smooth coefficients. On $\{a>0\}$ the principal symbol is $-a\Delta$ plus gauge terms, strictly parabolic. On $\{a=0\}$ the metric is stationary. Standard theory (Friedman/Lieberman, smooth degenerate parabolic) gives $T_{\max}>0$.

Extension: bounded $|a\operatorname{Rm}|$ on $[0,T)$ implies bounded $|\operatorname{Rm}|$ on every compact subset of $\{\chi>0\}$ (since $a\ge\chi_{\min}^2>0$ there). On $\{a=0\}$ the metric is constant, so $|\operatorname{Rm}|$ equals its initial value. Wang's induction (Propositions 4.13, 4.14 in \cite{wang2009pseudolocality}) then gives all weighted derivative bounds $|\nabla^m(\chi^2\operatorname{Rm})|_p<\infty$. The normalization contributes lower-order terms to each induction step (Section 3).

**Note.** The constants in Proposition 1 depend on $(g_0,\chi)$, not uniformly on a sequence. Sequence-uniform bounds come from the first-exit argument.

## 3. Normalization is lower-order in the Wang hierarchy

Under $\partial_tg=-2a(\operatorname{Ric}+g)$, the normalization $-2ag$ changes the curvature evolution relative to the unnormalized $-2a\operatorname{Ric}$ by:

### Volume form
$$
\partial_t(d\mu)=-a(s+4)d\mu,\qquad |s+4|=|\operatorname{tr}(E)|\le 4\delta.
$$
Over time $T_0=\theta r^2$: multiplicative growth factor $e^{4\delta T_0}\approx1$ for $\delta\to0$.

### Curvature evolution
The $-2ag$ velocity contributes $\partial_t\operatorname{Rm}\big|_{\mathrm{norm}}=-(\nabla^2a)\mathbin{\bigcirc\hspace{-10pt}\wedge}g+O(|\nabla a||\operatorname{Rm}|)$.

- $(\nabla^2a)\mathbin{\bigcirc\hspace{-10pt}\wedge}g$: bounded by $C/r^2$, an additive source
- $|\nabla a||\operatorname{Rm}|$: bounded by $C|\operatorname{Rm}|/r$, linear in curvature

In the $H_q$ energy inequality (equation (2.1) of Step 20), these contribute:
- Multiplicative: $C\cdot H_q$ (from the linear $|\operatorname{Rm}|$ term)
- Additive: $C\cdot\operatorname{Vol}/r^{2q}$ (from the $\nabla^2a$ source)

Both are lower order than the critical cubic reaction $H_{q+1}$, which is absorbed by the Sobolev product $\beta=A_0^2\|\operatorname{Rm}\|_2$. Over flow time $\theta r^2$, Grönwall growth is $e^{C\theta r^2}\le2$ for small $\theta$.

### Inverse metric variation
$\partial_tg^{ij}=2aE^{ij}$ contributes $O(a\delta|\operatorname{Rm}|^2)$ to $\partial_t|\operatorname{Rm}|^2$. This is absorbed by the multiplicative Grönwall factor.

### Critical parameter $\beta$
$$
\beta=A_0^2\cdot\|\operatorname{Rm}\|_{L^2(B_r)}=C^2r^2\sqrt{K_0}
$$
is a property of the initial geometry and is completely unchanged by the normalization.

### Defect $|E|^2$ equation
The $-2aE$ linear reaction from the normalization exactly cancels with the $+2aE^{ij}$ inverse metric variation in $\partial_t|E|^2$. The normalization is neutral for the defect $L^2$ budget. (Verified: Step 14.)

**Conclusion.** The normalization modifies Wang's hierarchy only through: (i) an exponential growth factor $e^{CT_0}\le2$; (ii) a bounded additive energy. Neither affects the critical Sobolev absorption or the volume-independent $\beta$.

## 4. Derivative-free first-exit framework

### Exit conditions

On $[0,T^*]$ with $T^*>0$ (supremum of times where all hold with doubled constants):

**(F1)** Metric comparability: $|g(t)-g_0|_{g_0}\le\tfrac1{10}$ on $M$.

**(F2)** Relative Sobolev: $A_0^2(B_r(p),g(t))\le 2A_0^2(B_r(p),g_0)$ for all covering centers.

**(F3)** Neighboring $L^2$ energy: $H_2(B_{2r}(p_\alpha),g(t))\le 2H_2(B_{2r}(p_\alpha),g_0)$ for all covering centers.

**(F4)** [Derived] Weighted curvature: $|\chi^2\operatorname{Rm}|(x,t)\le C_{\mathrm{exit}}\gamma/t$ on $M\times(0,T^*]$.

### Self-improvement cycle

**Step I** [(F1)+(F2)+(F3)$\Rightarrow$(F4)]: The Wang-type weighted Moser iteration, adapted to the normalized flow with Section 3 adjustments, gives $|\chi^2\operatorname{Rm}|\le C_1\gamma/t$ with $C_1<C_{\mathrm{exit}}$. This uses the $H_q$ hierarchy with $q=2\to3\to\cdots$ and the volume-independent $\beta$ (Step 19). The normalization exponential factor is absorbed into $C_1$.

**Step II** [(F1)–(F4)$\Rightarrow$defect bound]: The $J_m$ hierarchy with $H_3$ as curvature potential (Step 20, equation (3.2)) gives
$$
|\chi^2E|(t)\le C\delta(r^2/t)^{1/3}.
$$

**Step III** [Defect$\Rightarrow$(F1) improved]: Metric drift:
$$
|g(T^*)-g_0|_{g_0}
\le2\int_0^{T^*}|\chi^2E|\,dt
\le3C\delta(\theta r^2)^{2/3}r^{2/3}
=3C\delta\theta^{2/3}r^2.
$$
For $\delta_i\to0$ this is $<\tfrac1{20}$, strictly improving (F1).

**Step IV** [(F1)$\Rightarrow$(F2) improved]: Metric perturbation of order $\varepsilon<1/20$ changes $A_0^2$ by factor $(1+C\varepsilon)^{n/2}<1.5<2$.

**Step V** [Energy evolution$\Rightarrow$(F3) improved]: The triangular system (Step 20, equation (4.1)) gives
$$
Q_\alpha(T^*)\le e^{CN\theta}Q_\alpha(0)<2Q_\alpha(0)
$$
for $\theta\le\theta_0(n,N)=\ln2/(CN)$.

**Conclusion.** All exit conditions are strictly improved. Hence $T^*\ge T_0=\theta r^2$.

### Conditional status

Steps I and II are conditional on the localized finite-neighbor Moser iteration for the degenerate normalized flow. The exponent products (Step 20) and the critical $\beta$ cancellation (Step 19) are established; the remaining work is the exact nested time-space energy recurrence with evolving measure and finite-neighbor outer terms.

## 5. Interior regularity on the plateau

This is the key new structural contribution.

**Proposition 2** (Plateau Shi estimates). On the plateau $P=\{\chi=1\}$, the flow restricts to
$$
\partial_tg=-2(\operatorname{Ric}+g)
$$
which is a normalized Ricci flow with $\lambda=-1$. From (F4) with $a=1$:
$$
|\operatorname{Rm}|(x,t)\le\frac{C\gamma}{t},
\qquad x\in P,\quad t\in(0,T_0].
$$

For any $p\in P_{\mathrm{inner}}=\{x:\operatorname{dist}_{g_0}(x,\partial P)\ge\rho/16\}$, the ball $B_{\rho/32}(p)$ lies entirely within $P$. On $[T_0/2,T_0]\times B_{\rho/32}(p)$:

- $|\operatorname{Rm}|\le2C\gamma/T_0$ (from the curvature bound at $T_0/2$)
- Standard Shi interior estimates for the normalized Ricci flow give, for every $k\ge0$,
$$
|\nabla^k\operatorname{Rm}|(p,T_0)\le\frac{C_k}{(T_0/2)^{k/2}}
$$
where $C_k$ depends only on $n$, $k$, and the curvature bound $2C\gamma/T_0$.

**Corollary.** For the hypothetical pinching sequence $g_i$ at time $T_0$:
$$
|\nabla^k\operatorname{Rm}_{g_i(T_0)}|(p)\le C_k
\qquad\text{for all }p\in P_{\mathrm{inner}},\quad\text{uniformly in }i,
$$
because $T_0=\theta r^2$, $\gamma\lesssim r^2\sqrt{1+K_0}$, and $K_0$ is uniformly bounded by Chern–Weil on the critical family.

**Principle.** Qualitative smooth continuation uses individual-metric constants (Proposition 1). Quantitative uniform bounds come from the first-exit (Section 4). Interior regularity converts zero-order uniform bounds into all-derivative uniform bounds on the plateau at positive time. No Bernstein estimate from time zero, no global derivative propagation, and no cutoff-Hessian evolution tracking is needed.

## 6. Smooth compactness and calibrated contradiction

At time $T_0$, on $P_{\mathrm{inner}}$:
- $g_i(T_0)$ has uniformly bounded $|\nabla^k\operatorname{Rm}|$ for all $k$ (Proposition 2)
- $g_i(T_0)$ is comparable to $g_i(0)$ with perturbation $O(\delta_i)$ (Step III)

**Exponential chart selection.** For a good center $p_i\in P_{\mathrm{inner}}$ chosen by the averaging lemma (Step 16), set $h_i=\exp_{p_i}^*g_i(T_0)$ on $B_R(0)\subset T_{p_i}M\cong\mathbb R^4$. By Rauch comparison:
$$
\operatorname{Vol}(B_R,h_i)\ge c_4R^4>0
$$
independent of collapse on $M$. By the bounded exponential map (all curvature derivatives controlled), $|\nabla^k\operatorname{Rm}_{h_i}|\le C_k$ on $B_R$.

**Arzelà–Ascoli extraction.** A subsequence $h_i\to h_\infty$ in $C^\infty(B_{R/2})$.

**Einstein limit.** $|\operatorname{Ric}_{h_\infty}+h_\infty|=\lim|\chi^2E_i(T_0)|\le\lim C\delta_i(r^2/T_0)^{1/3}=0$.
Hence $\operatorname{Ric}_{h_\infty}=-h_\infty$.

**Calibration.** From $Q(T_0)\le 2Q(0)=2\delta_i^2\operatorname{Vol}\to0$ and the 7/24 inequality:
$$
\int\left(|W^+|-\frac1{2\sqrt6}\right)^2d\mu_{h_\infty}=0,
$$
so $|W^+_{h_\infty}|\equiv\frac1{2\sqrt6}$ on $B_{R/2}$.

**Projector obstruction (Step 6).** Einstein with $|W^+|=\frac1{2\sqrt6}$ and $s=-4$ forces $\operatorname{Spec}(W^+)=(-\tfrac16,\tfrac1{12},\tfrac1{12})$. The simple eigenform is parallel (projector argument), giving $\nabla W^+=0$. But the Einstein–Weyl identity requires $|\nabla W^+|^2=\frac1{16}$. Contradiction.

**Therefore:** no such sequence exists, and $\inf_g\|\operatorname{Ric}_g+g\|_\infty>0$ on each critical Ishida–LeBrun 4-manifold $M$.

## 7. What the conditional result would establish

If the localized zero-order Moser iteration (Steps I–II of Section 4) is proved, the above chain gives:

- **Fixed-topology gap:** For each critical Ishida–LeBrun 4-manifold $M$, $\inf_g\|\operatorname{Ric}_g+g\|_\infty>0$.
- **Standard-subclass uniformity:** The Noether bound $\chi(M)/A\le65/6$ (Step 18) makes analytic constants uniform across the standard subclass (minimal general-type summands with negative-definite $N$).
- **This does not prove Yau 26.** The unrestricted negative branch, positive branch, dimensions $n\ge5$, dimension-only quantifiers, and Lean formalization remain entirely open.

## 8. What remains to prove

**(U1)** Localized curvature $\varepsilon$-regularity: the Wang-type Moser iteration from $H_2$ persistence to $|\chi^2\operatorname{Rm}|\le C\gamma/t$ on finite-neighbor domains with spatial cutoffs, normalized flow, and evolving measure.

**(U2)** Localized defect Moser iteration: the $J_m$ hierarchy from initial $J_6$ and the curvature potential $A^4H_3\le C\gamma^3/t$ to $|\chi^2E|\le C\delta(r^2/t)^{1/3}$.

**(U3)** Triangular $Q$ system: the global $L^2$ defect amplification $Q(T_0)\le CQ(0)$ under the Whitney-level decomposition.

The normalization is lower-order (Section 3). The volume-independent $\beta$ controls the critical absorption (Step 19). The exponent products converge (Step 20). A02's CZ spike audit (message #296) confirms that the zero-order weighted estimate is not broken by standard singular-kernel transplants.

The remaining obstacle is purely PDE localization: deriving the exact time-space energy recurrence with finite-neighbor outer terms, evolving measures, and regularization at $a=0$, managing nested-cutoff domains through infinitely many Moser exponents. This is a standard-type but technically substantial parabolic regularity problem.

## 9. Corrections (TTCS + peer review)

See `step21_corrections_from_ttcs_and_peers.md` for full details. Summary:

1. **Volume form**: $|s+4|\le4\delta$ holds only at $t=0$; during flow use $|a\operatorname{tr}(E)|\le CaF$
2. **Exit conditions**: (F3) split into (F3a) curvature energy and (F3b) defect energy
3. **Uniform scale**: $r_*\ge c>0$ for fixed topology (Chern–Weil bounds $K_0$)
4. **Collapse Sobolev** (A02 #298): individual $A_0^2$ degenerates under collapse, but $\beta=A_0^2\|\operatorname{Rm}\|_2$ is volume-independent and small at Li radius
5. **Spectrum**: $|W^+|=1/(2\sqrt6)$ alone does not determine $\operatorname{Spec}(W^+)$; need full joint density selection with nonzero monopole (Step 16)
6. **Nash alternative** (TTCS generator): single $L^2\to L^\infty$ Nash bound may replace infinite Moser exponents
7. **A01 correction**: Stampacchia rescaling error; corrected to use $q\to3q/2$ iteration

## Evidence

- Verification script: `workspace/scripts/verify_step21_derivative_free_first_exit.py` (passed)
- Step 20 hierarchy: `workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md`
- Step 19 volume-independent $\beta$: `workspace/notes/step19_p4_threshold_and_degenerate_moser.md`
- Wang source: `Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md`
- Calibrated local obstruction: `workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex`
- 7/24 calibration: `workspace/scripts/verify_L2_completion_square_chain.py`
- Exponential chart: `workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md`
