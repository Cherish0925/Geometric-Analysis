# TTCS Independent Branch Record

```json
{
  "step_id": 73,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step73_global_positive_proof_allocation.md",
    "Sessions/S0910A02/workspace/plans/step73_general_higher_flux_necessity_plan.md",
    "Skills/qiushi-yau26/references/research/20260912.tex",
    "Sessions/S0910A02/workspace/notes/step70_necessity_flux_dichotomy.md",
    "Sessions/S0910A02/workspace/data/step53_crepant_wall_and_stratum_probe.json"
  ]
}
```

## Task

Read the Step 73 allocation note and the higher-mode flux plan. Check the mathematical plausibility and risks of the proposed general cone higher-obstruction flux identity: the homogeneous degree-l tensor K_l, dual o_l=r^{-(d+2l-2)}K_l, expected Wronskian coefficient -(d+2l-2)/2, TT/radial-gauge cancellation of linearized Ricci gauge terms, operator-norm lower bound, nonlinear/weighted extension cautions, and the decision to prove an isolated cone lemma first while only stating a stratified obstruction-bundle extension. Identify any sign/scaling mistakes or hidden assumptions that Agent2 must fix before treating it as a theorem. Do not decide the whole Yau26 problem; focus on making the next theorem statement correct and useful.

## Output

## Verifier memo — Step 73 general higher-mode cone flux identity

### Summary verdict

The algebraic core of the plan is correct: the dual tensor $o_\ell=r^{-(d+2\ell-2)}K_\ell$, its trace/divergence/harmonicity/radial-null properties, and the Wronskian coefficient $-\tfrac{d+2\ell-2}{2}I_{K_\ell}$ all check out and reduce to the proved $\ell=2$ manuscript identity. However, the **operator-norm lower bound as written is valid only at $\ell=2$**. For $\ell\ge3$ the nuclear-norm mass of $o_\ell$ concentrates at the inner edge $r=b$, the denominator is not $LJ_{K_\ell}$, and the resulting universal lower bound carries a factor $b^{\ell-2}$ that vanishes in the bubbling limit. Consequently the §5 "necessity" statement $\delta_i L\gtrsim c(K_\ell,d,\ell)$ does not hold for higher modes and must be rewritten. Below I show the computations and list what Agent2 must fix before this is treatable as a theorem.

### 1. What is correct and can be used as stated

**Dual tensor properties.** With $K_\ell=r^\ell Y(\theta)$ one gets $o_\ell=r^{-(d+\ell-2)}Y$, the conjugate indicial root: $\alpha=-(d+\ell-2)$ satisfies $\alpha(\alpha+d-2)=\ell(\ell+d-2)$, so $o_\ell$ is componentwise harmonic. Trace-free is inherited (scalar multiple). Divergence-free holds precisely through the radial-null property:
$$
\operatorname{div}(o_\ell)_j=(\partial_i f)K_{ij}=-(d{+}2\ell{-}2)\,r^{-(d+2\ell)}\,(K_\ell(x,\cdot))_j=0,\qquad f=r^{-(d+2\ell-2)}.
$$
So $o_\ell$ is genuinely TT and radial-null for every $\ell$, not only $\ell=2$. ✓

**Wronskian coefficient (verified).** For TT radial-null $u$, $D\operatorname{Ric}_e u=-\tfrac12\Delta u$ exactly (with $\Delta=\operatorname{div}\nabla$; the interpolation $u=\chi K_\ell$ stays trace-free and divergence-free because $K_\ell(x,\cdot)=0$). Green's identity leaves only the outer-edge contribution ($u=0$ near $r=b$). With $\partial_r K_\ell=\tfrac{\ell}{r}K_\ell$, $\partial_r o_\ell=-\tfrac{d+\ell-2}{r}o_\ell$, the integrand is $\tfrac{d+2\ell-2}{r}\langle K_\ell,o_\ell\rangle$, all $R$-powers cancel, and
$$
\int_A\langle D\operatorname{Ric}_e u,o_\ell\rangle=-\tfrac{d+2\ell-2}{2}\,I_{K_\ell}.
$$
At $\ell=2$ this is exactly $-\tfrac{d+2}{2}I_K$ (FND:flux). Sign and coefficient are sound. ✓

**Gauge-term cancellation mechanism (verified).** For a perturbation that is only approximately TT (the physical/Bianchi case), the trace-Hessian and divergence pieces of $D\operatorname{Ric}_e$ integrate away against $o_\ell$: the bulk pieces need $\operatorname{div}o_\ell=0$, and the edge pieces at $r=R,b$ vanish because they contract $o_\ell$ with the radial direction, i.e. use $o_\ell(\nu,\cdot)=0$. The $-\tfrac12\Delta u$ Wronskian edge terms are the ones retained. This is correct and generalizes cleanly. One clarification for Agent2: for the clean model $u=\chi K_\ell$ there are **no** gauge terms at all (the interpolation is exactly TT), so the identity is exact; the gauge-cancellation argument is only needed for the physical $q$ that is TT only in a chosen gauge.

### 2. Central correction — the operator-norm lower bound is $\ell=2$-special

The duality step divides the flux by the nuclear-norm mass of $o_\ell$:
$$
\int_A\|o_\ell\|_*\,dV=J_{K_\ell}\int_b^R r^{1-\ell}\,dr=
J_{K_\ell}\cdot\begin{cases}\;\log(R/b)=L,&\ell=2,\\[4pt]\;\dfrac{b^{2-\ell}-R^{2-\ell}}{\ell-2},&\ell\ge3.\end{cases}
$$
The radial integrand $r^{1-\ell}$ is log-critical **only at $\ell=2$**. For $\ell\ge3$ it is $r$-integrably singular toward $r=b$, so the mass is dominated by the inner edge and $\int_A\|o_\ell\|_*\approx \tfrac{b^{2-\ell}}{\ell-2}J_{K_\ell}$. The corrected universal lower bound is therefore
$$
\|D\operatorname{Ric}_e u\|_{op,\infty}\ \ge\ \frac{(d+2\ell-2)(\ell-2)}{2\,(b^{2-\ell}-R^{2-\ell})}\,\frac{I_{K_\ell}}{J_{K_\ell}}\ \approx\ \frac{(d+2\ell-2)(\ell-2)}{2}\,\frac{I_{K_\ell}}{J_{K_\ell}}\;b^{\ell-2}\quad(b\ll R).
$$
This $\to0$ as $b\to0$ for every $\ell>2$. The plan's formula $\dfrac{(d+2\ell-2)I_{K_\ell}}{2LJ_{K_\ell}}$ is thus only the $\ell=2$ instance and must not be written for general $\ell$.

**Cross-check by direct computation.** The log-cutoff interpolation gives, mode-by-mode,
$$
D\operatorname{Ric}_e(\chi K_\ell)=-\tfrac12\Big(\chi''+\tfrac{d-1+2\ell}{r}\chi'\Big)K_\ell,\qquad
\|D\operatorname{Ric}_e(\chi K_\ell)\|_{op}\sim\frac{d+2\ell-2}{2L}\,|\psi'|\,r^{\ell-2}\|Y\|_{op}.
$$
(At $d=4,\ell=2$ the coefficient $\tfrac{d+2\ell-2}{\cdot}=6$ reproduces FND:logoperator's $6\psi'/L$.) The factor $r^{\ell-2}$ is the key: a degree-$\ell$ mode contributes $O(r^{\ell-2})$ to the pointwise pinching. Only $\ell=2$ is scale-invariant ($r^0$) and matches the $C^0$ operator-norm pinching; for $\ell>2$ the contribution is polynomially small at the bubble scale and concentrated at the outer edge. This is the same structural fact as the nuclear-mass concentration, seen from the metric side.

**Consequence for §5.** The intended necessity statement "if a nonzero degree-$\ell$ mismatch persists across log-length $L$ then $\delta_i L\gtrsim c$" is a genuine $\ell=2$ theorem (it is exactly why the manuscript's log-Weyl construction has $\delta\le C|\log a|^{-1}$ and cannot beat it). For $\ell\ge3$ the correct universal statement is $\delta_i\gtrsim c\,b^{\ell-2}$ (equivalently the mode contributes $O(R^{\ell-2})$), which is compatible with $\delta_i\to0$ while the mode is present. Agent2 should either restrict the necessity lemma to $\ell=2$, or state the higher-$\ell$ version with the correct $b^{\ell-2}$/$R^{\ell-2}$ factor and its weaker consequence, and note explicitly that higher modes are subleading relative to the degree-2 Weyl obstruction.

### 3. Weighted-energy weight needs rederivation, and degrades for $\ell>2$

The plan's proposed weight $r^{-d-2\ell+4}$ makes the fixed-model energy $\int w|Dq_\ell|^2dV\sim R^2$ for all $\ell$ (a reasonable design), and reduces to the manuscript $r^{-d}$ at $\ell=2$. But whether it controls the nonlinear pairing error is the real question. The nonlinear remainder $\int_A\langle A(q)*D^2q,\;o_\ell\rangle$, after one integration by parts, produces $\int|Dq|^2\,r^{-(d+\ell-2)}$. To dominate this by $\int|Dq|^2\,r^{-d-2\ell+4}$ one needs $-(d+\ell-2)\le-(d+2\ell-4)$, i.e. $\ell\le2$. So the weighted energy controls the error term uniformly only at $\ell=2$; for $\ell>2$ the pairing weight is heavier near $r=b$ and the energy does not dominate the inner-edge contribution. This is the same inner-edge concentration reappearing. Agent2 should rederive the weight from the actual $o_\ell$-pairing (not from a scale-normalization guess) and expect that for $\ell>2$ an additional inner-edge/$b$-power term is unavoidable. The plan's own caution ("Do not overgeneralize until the exact scaling is rederived") is warranted; the dimension count above shows why.

### 4. Hidden assumptions Agent2 must make explicit

- **Existence and $\Gamma$-invariance of $K_\ell$.** The space of homogeneous degree-$\ell$ symmetric 2-tensors that are simultaneously componentwise-harmonic, trace-free, divergence-free, and radial-null is strongly constrained. At $\ell=2$, $d=4$ it is the Weyl normal tensor $K_{ij}=-\tfrac13C_{ikjl}x^kx^l$ (nonzero when Weyl $\ne0$). For $\ell>2$ the nonvanishing of the $\Gamma$-invariant subspace is a representation-theoretic fact that is not automatic; the lemma is vacuous without it. State $K_\ell\ne0$ as a hypothesis and record for which $(d,\ell,\Gamma)$ it is realized (in particular for ADE groups in $d=4$ and for codimension-four normal cones in the stratified target).
- **Resonance / log terms.** Degree $\ell$ is one of the two indicial roots ($\ell$ and $-(d+\ell-2)$). The interpolation is at resonance, so $r^\ell\log r$ terms can appear. At $\ell=2$ this resonance is exactly what produces the $1/L$ behavior. Agent2 must verify that no additional resonant $r^\ell\log r$ piece alters the Wronskian coefficient for $\ell>2$, or record precisely how it enters the edge terms and the interpolation error.
- **Biquard obstruction order $\leftrightarrow$ $\ell$.** The plan assumes a clean correspondence between mode degree $\ell$ and Biquard/Ozuch obstruction order. This is not established. Higher obstructions in the desingularization theory involve higher curvature and may not correspond to single homogeneous degree-$\ell$ TT modes; the map from "obstruction order $k$" to "mode degree $\ell$" (and whether it skips degrees or mixes with quartic curvature) should be pinned down before the necessity interface in §5 is stated.

### 5. Items the plan handles correctly

- **Two-tier strategy** (prove the isolated cone lemma for $d\ge4$, only state the stratified obstruction-bundle version) is the right order. The isolated lemma's algebra is sound modulo the corrections above.
- **Gauge/pullback sensitivity** is correctly flagged: the CZ-type spike $\Phi_s(x)=x+s^{9/4}\chi(x/s)\sin(s^{-5/4}x_1)e_1$ from FND:flux shows that weak norms and arbitrary pullbacks can fake or destroy the pairing; harmonic/Bianchi coordinates are essential and cannot be dropped.
- **Stratified deferral.** Step 53's point is correct and must survive into the target statement: the pinching is a pointwise $C^0$ operator norm, so a nonzero obstruction coefficient at one stratum point produces an $O(1)$ core Ricci-endomorphism defect that stratum-integration cannot cancel; the toy $dy^2+a(y)^2dx^2$ with $K=-a''/a$ shows tangential parameter variation itself generates $O(1)$ curvature. The stratified condition should therefore be pointwise/elliptic along the stratum with quantified normal-connection and tangential-derivative control, exactly as the plan states, and marked unproved.

### 6. Concrete statements Agent2 should adopt

1. Prove the isolated cone identity with the exact coefficient $-\tfrac{d+2\ell-2}{2}I_{K_\ell}$ (correct as verified), for all $\ell\ge2$.
2. Replace the single lower bound by the two regimes:
$$
\|D\operatorname{Ric}_e u\|_{op,\infty}\ge \frac{(d+2\ell-2)I_{K_\ell}}{2LJ_{K_\ell}}\ (\ell=2),\qquad
\ge \frac{(d+2\ell-2)(\ell-2)I_{K_\ell}}{2(b^{2-\ell}-R^{2-\ell})J_{K_\ell}}\ (\ell\ge3),
$$
and record that the second $\to0$ like $b^{\ell-2}$.
3. State the necessity consequence only at $\ell=2$ in the clean $\delta L\gtrsim c$ form; for $\ell\ge3$ give the weaker $\delta\gtrsim c\,b^{\ell-2}$ form and the observation that a degree-$\ell$ mode contributes $O(r^{\ell-2})$ to the scale-invariant pinching, hence is subleading to the degree-2 obstruction.
4. Rederive the nonlinear/weighted weight from the $o_\ell$-pairing rather than from energy normalization, expecting inner-edge $b$-powers for $\ell>2$.
5. Carry $K_\ell\ne0$, its $\Gamma$-invariance, the resonance check, and the Biquard-order correspondence as explicit hypotheses.

None of this decides any branch of Yau-26; it fixes the next lemma so that the $\ell=2$ result stays exact and the higher-$\ell$ generalization is stated with the correct scaling rather than an over-general $1/L$ form.