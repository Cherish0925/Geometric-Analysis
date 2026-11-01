# TTCS Independent Branch Record

```json
{
  "step_id": 55,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step54_first_exit_continuation_derivation.md",
    "Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md",
    "Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md",
    "Sessions/S0910A01/workspace/data/step55_bootstrap_continuation_verify.json",
    "Sessions/S0910A03/workspace/data/step57_H2_verification.json"
  ]
}
```

## Task

Verify the combined analytic interface for the restricted Ishida--LeBrun negative-gap route after Step 55 and A03 Step57. Read the Step55 repair note, the patched Step54 derivation, and A03 Step57 H2/continuation note. Focus on scientific correctness of: (i) the coupled first-exit bootstrap using Gamma(t)=S(t)H2(t)^{1/2} and V(t)=int||aE||_inf rather than an evolving unweighted |E|<=delta; (ii) H2 evolution/absorption with shifted curvature T, including whether the bounded source C0=O(Vol) is compatible with the small gamma/Whitney cancellation and does not destroy sequence-uniform first exit; (iii) the W^{1,p}->L^infty continuation bridge and whether the fixed-background connection difference A is needed to obtain smooth restart data; (iv) terminal local compactness on exponential pullback balls rather than base image balls. Identify any remaining mathematical gaps precisely and suggest the next proof object to write, but do not treat this as a complete Yau 26 proof.

## Output

## Verification memo: combined analytic interface for the restricted Ishida–LeBrun contradiction route (post Step 55 / A03 Step 57)

I read `step55_joint_bootstrap_background_continuation_repair.md`, the patched `step54_first_exit_continuation_derivation.md`, `step57_H2_evolution_and_continuation_bridge.md`, the `step56_positive_time_base_pair.md` supplement, and both verification JSONs. Below I check the four requested interfaces, re-deriving the parts that carry the argument, and I state precisely what is not yet written and the single object I would write next. This covers one direction of the dimension‑4 restricted route only; it is not a resolution of Problem 26.

---

### (i) Coupled first-exit bootstrap with $(\Gamma,V)$

The replacement of an evolving unweighted $|E(t)|\le\delta$ by $V(t)=\int_0^t\|aE\|_\infty\,ds$ is the correct move: the degenerate cutoff flow creates curvature from a flat datum (Step 54 §1.4 flat-torus benchmark), so there is no preserved pointwise Ricci defect bound. The metric velocity is genuinely $2a|E|$, so $V$ is the right distortion variable. I checked the mechanics:

- **Bilipschitz/Sobolev transport (1.5)–(1.8).** $|\tfrac{d}{dt}\log g(\xi,\xi)|\le 2\|aE\|_\infty$ gives $e^{-2V}g_0\le g(t)\le e^{2V}g_0$ correctly (interpreting $\|aE\|_\infty$ as a $g(t)$-pointwise norm, which dominates the quadratic-form eigenvalue). The Sobolev exponent is right at the critical embedding: with $p=2n/(n-2)$ the left side transports by $L^{n-2}$, the gradient term by $L^{n+2}$, giving $\mathcal S(t)\le L^{2n}\mathcal S(0)=e^{2nV}\mathcal S(0)$, i.e. $e^{8V}$ in $n=4$. (Note the written Sobolev inequality (1.2) uses $L^4$, which is critical only at $n=4$; the general-$n$ exponent $2n$ is correct precisely because the underlying embedding is the critical one, not the fixed $L^4$.)
- **Multiplicative $H_2$ Gronwall (1.9)–(1.13).** The transport into $\gamma(t)\le\gamma(0)\exp\{2nV+\tfrac12C_VV+C_H\theta\}$ and the closure (1.12)–(1.13) are algebraically correct, and the JSON sample reproduces them: with $C_H=10,C_V=6,n=4,\theta=10^{-3},V_*=9.09\times10^{-4}$ the factor $\exp\{11V_*+C_H\theta\}=e^{0.02}=1.0202\le\tfrac32$, and $\gamma$ improves from $\gamma_*/2$ to $0.00510\le\tfrac34\gamma_*$.
- **Defect endpoint and $V$-improvement (1.14)–(1.17).** $\int_0^T t^{-1/3}dt=\tfrac32T^{2/3}$ is integrable, and (1.16) $V(T)\le\tfrac32C_E\delta\theta^{2/3}r^2$ is dimensionally correct ($r^{2/3}\cdot r^{4/3}=r^2$). The JSON `defect_integral` entries match $\int_0^T(r^2/t)^{1/3}dt$ to the digit.

**One bookkeeping mismatch to correct.** The stated smallness requirement (1.17), $\delta\le V_*/(3C_E\theta^{2/3})$, drops the $r^2$ that is present in (1.16). The correct requirement is
$$\delta\le \frac{V_*}{3C_E\theta^{2/3}r^2}.$$
The verification data uses the corrected version: $\delta=0.0303$ passes $V(T)=2.27\times10^{-4}\le V_*/2$ via (1.16) but would fail (1.17) as literally written ($V_*/(3C_E\theta^{2/3})=3.79\times10^{-3}$). Since $r\le1$, the written (1.17) is merely stronger than needed, so nothing downstream breaks, but the note and the passing sample presently disagree; (1.17) should carry the $r^2$.

**One dependence to record.** The defect endpoint constant $C_E$ and the curvature Gronwall constants implicitly use Sobolev constants that drift by $e^{2nV_*}$. Because $V_*$ is a fixed small number this is a uniform bounded factor, but the coupled bootstrap is only genuinely closed once it is stated that $C_E$ is taken uniform over $V\le V_*$. The two provisional bounds ($\Gamma\le\gamma_*$ enters the defect endpoint; $V\le V_*$ enters the $H_2$ transport) each feed the other's strict improvement, so the joint first-time argument is valid.

---

### (ii) Shifted-curvature $H_2$ evolution, the source $C_0=O(\mathrm{Vol})$, and Whitney cancellation

The Step 57 term-by-term derivation is internally consistent with A01's unshifted derivation, and I verified the structural identities it rests on:

- $\mathrm{Ric}(g\owedge g)=2(n-1)g$, hence $\mathrm{Ric}(G)=g$ and $\mathrm{Ric}(T)=E$; $|G|^2=n/(2(n-1))=2/3$ at $n=4$. $\nabla G=0$ gives $|\nabla T|=|\nabla\mathrm{Rm}|$, so $D_2$ is exactly A01's dissipation. All consistent.
- The zero-order conformal cancellation $(4-n)a|\mathrm{Rm}|^2=0$ at $n=4$ is correct: four inverse-metric raisings $+8a|\mathrm{Rm}|^2$, tensor reaction $-4a|\mathrm{Rm}|^2$, volume $-na|\mathrm{Rm}|^2$ sum to $(4-n)a|\mathrm{Rm}|^2$. The note correctly states this is an algebraic zero-order identity, not conformal invariance of $\int|\mathrm{Rm}|^2$.
- The Hessian-of-$a$ terms (Type C) are removed by one signed integration by parts using only $|d\chi|$, with the buffer-collar cancellation $\nabla a\cdot\nabla\eta=0$; no $\|\nabla^2\chi\|_\infty$ enters. Verified against Step 57 §5 and the JSON checks.

**The compatibility question you asked (does $C_0$ ruin sequence-uniform first exit?) resolves affirmatively, and the resolution is a sentence both notes omit.** Step 57 (7.1) carries an additive source $C_0\le C_n\mathrm{Vol}$ (from the constant $1$ in $F_T^2=1+|T|^2$), while Step 55 (1.9) writes a purely multiplicative Gronwall with no additive term. These reconcile because the augmented energy has a matching volume floor:
$$H_2(t)=\int\eta^2 F_T^2\,d\mu_t\ \ge\ \int\eta^2\,d\mu_t\ \ge\ e^{-nV}\!\int\eta^2\,d\mu_0\ \ge\ c\,\mathrm{Vol}(\operatorname{supp}\eta),$$
using $F_T^2\ge1$ and the bilipschitz volume control from $V$. Hence $C_0\le C\,H_2(t)$, and the additive source folds into the "$+1\cdot H_2$" part of the multiplicative coefficient $C_H(1+r^{-2})H_2$. This is exactly why Step 55's source-free Gronwall (1.10) is legitimate. It is also why the additive source cannot destroy the collapse-independence: the same $\mathrm{Vol}$ that bounds $C_0$ appears in $H_2(0)\le C(1+\kappa_0^2)\mathrm{Vol}$, and cancels in $\gamma$.

I re-checked the Whitney cancellation itself: with the Maheux–Saloff-Coste local constant $\mathcal S(0)\asymp r^2\mathrm{Vol}(B_r)^{-1/2}$ (valid from the initial lower Ricci bound of the pinched datum) and $H_2(0)\le C(1+\kappa_0^2)\mathrm{Vol}$,
$$\gamma(0)=\mathcal S(0)H_2(0)^{1/2}\le C r^2\sqrt{1+\kappa_0^2},$$
collapse-independent. Crucially the repaired route transports $\mathcal S(t)$ by bilipschitz comparison from $\mathcal S(0)$ (which needs the lower Ricci bound only at $t=0$), rather than re-applying M–SC at time $t$ (which would need a time-$t$ lower Ricci bound that the argument deliberately no longer assumes). This is internally coherent.

**What to write explicitly:** the one-line lemma $H_2\ge c\,\mathrm{Vol}(\operatorname{supp}\eta)\Rightarrow C_0\le C H_2$, with the constant's dependence on $V_*$ and the initial doubling constant recorded. Presently Step 55 silently drops $C_0$ and Step 57 silently keeps it; the bridging sentence is the missing piece, not a defect in either estimate.

---

### (iii) The $W^{1,p}\to L^\infty$ continuation and whether the fixed-background $A$ is needed

There is **no genuine conflict** between A03's finite-order Proposition 9.1 and A01's fixed-background connection difference; they are the same mechanism at two levels of explicitness, and the $A$-object is genuinely required for the final step.

- **Prop 9.1(i) — the pointwise curvature bound — is solid and is the valuable reduction.** From $\|aF_T\|_\infty\le C\gamma/t$ one gets bilipschitz equivalence on $[\tau,T^*]$, then the unweighted seed $T\in L^\infty_tL^q_x$ (Step 56 (1.1), whose proof uses $|da|^2\le4a|d\chi|^2$ and $a|T|^{q+1}=|U||T|^q$ and never divides by $a$), then the coupled pair $(V,Z)$ and $X=\nabla T$ in every $L^p$ (Step 56 (3.8),(4.5)), then Kato + Sobolev with $p>4$ giving $\|T\|_\infty<\infty$, hence $|\mathrm{Rm}|<\infty$. I verified the two non-circularity identities that make the base pair work: $a\nabla T=V-da*T$ (from $V=\nabla(aT)=da*T+a\nabla T$), and $(da*da)*T=4C_1C_1U$, $\nabla[\cdots]=C_1C_2U+C_1C_1V$. I also confirmed the essential expansion $\nabla^3a=2\chi C_3+6C_1C_2$ and that only the $\chi$-weighted piece $\chi C_3\,T$ is integrated by parts, the unweighted $C_1C_2\,T$ being kept as finite-exponent forcing — this is what avoids a bare $C_1C_1T$ term hitting the top derivative of $X$ with no matching weight. This first-derivative collar block is correct.

- **The fixed-background $A$ is genuinely needed for smooth restart data, and it equals A03's own connection velocity.** A01's point that $\nabla^{g(t)}g(t)\equiv0$ makes moving-covariant metric derivatives vacuous is correct: bounding $\|\nabla^m T\|$ does not by itself produce $\|g\|_{H^s}$ in a fixed chart. The object $A=\nabla^{g(t)}-\bar\nabla$ is precisely $\Gamma(t)-\Gamma(\tau)$ as a tensor, and A01's $\partial_tA=g^{-1}*\nabla^{g(t)}(aE)$ (2.2) is identical to A03's $\partial_t\Gamma=g^{-1}*\nabla\mathrm{Ric}(U)$ used in Step 57 §9.2(6b). So A03's step 6(b) and A01's §2 are the same construction; A01 adds the triangular structure (2.6)–(2.10) showing $\bar\nabla^mA$ is controlled by the current top term $U_{m+1}$ and only lower $\bar\nabla A$, then $\bar\nabla^{m+1}g=(\bar\nabla^mA)*g+P_m$ delivers fixed-background $W^{m+1,p}$ bounds. The JSON `connection_conversion_triangular_A`, `metric_restart_uses_background_derivatives`, and the `metric_restart_orders_sample` (order $m+1$ metric derivative requires $A$-order $m$) all confirm the triangular pattern with no top-order $\bar\nabla^m A$ on the right.

- **The real remaining analytic object.** Only the first block $T_0\to(U_1,C_2)\to T_1$ is written (Step 56). A03 §9.2(6c) asserts higher orders "close trivially once $|T|$ is bounded" — this is true on the plateau $\{a=1\}$, where the flow is uniformly parabolic and standard Bando–Bernstein–Shi gives $|\nabla^m\mathrm{Rm}|\le C_m t^{-m/2}$. On the degenerate collar $\{0<\chi<1\}$ it is not automatic: parabolicity degenerates as $a\to0$, and the whole point of Step 56 is that each absorbed derivative carries an explicit $\chi$ matching $\int a|\nabla\cdot|^2$. So the unwritten piece is the finite induction $T_m,(U_{m+1},C_{m+2})\to T_{m+1}$ on the collar, up to the order needed to feed Step 56's local existence theorem. That order is finite: the restart theorem uses $H^{s_0}$ with $s_0>n/2+4=6$ in $n=4$, so one needs the collar current-pair estimates only to order $\sim s_0+1\approx 8$, then A01's triangular $A$-integration converts them to $g(T^*)\in H^{s_0}$. Both sessions correctly identify this as the outstanding item; it is finite and patterned on the block already written, not open-ended.

---

### (iv) Terminal local compactness on exponential pullback balls

This interface is correct and is the right way to run the density argument under collapse.

- **Pullback noncollapse.** With bounded curvature $|\mathrm{Rm}|\le K$ on the plateau and $\rho<\pi/\sqrt K$ (conjugate radius from the upper bound alone), $\exp_p$ is a conjugate-point-free immersion on $\mathcal B_\rho(0)\subset T_pM$, so $\tilde g_p=\exp_p^*g(T)$ is a genuine metric and Günther/Rauch gives $\mathrm{Vol}(\mathcal B_\rho,\tilde g_p)\ge c\rho^n$ with $c$ collapse-independent. This needs **no injectivity-radius lower bound**, which is exactly what fails under collapse. The JSON confirms $\rho\sqrt K=0.316<\pi$ and pullback volume ratio $0.967$ to Euclidean. The refusal to claim a base image-ball lower bound is the correct call.
- **Liouville averaging without folding multiplicity.** I checked the mechanism: geodesic-flow invariance of Liouville measure on $S^*M$ gives
$$\int_{p}\!\int_{|v|<\rho}\Phi(\exp_p v)\,d\mu_{\tilde g_p}\,d\mu(p)=\Big(\!\int_0^\rho s^{n-1}ds\Big)\mathrm{Vol}(S^{n-1})\!\int_M\Phi,$$
with no multiplicity factor even where $\exp_p$ folds. Dividing by the per-center normalization $\mathrm{Vol}(\mathcal B_\rho,\tilde g_p)\asymp\rho^n$ gives $\int_{P^{\rm in}}A_\rho\Phi(p)\,d\mu\le C\int_M\Phi$ (8.1). This is a clean and correct route around collapse; the "$C$" is the uniform pullback-volume comparison constant.
- **Prop 3.2 lower bound** $A_\rho\Phi\ge\eta'>0$ requires $C^\infty$ subconvergence of the pointed pullback balls, which needs bounded $|\nabla^m\mathrm{Rm}|$ at the terminal time. On the plateau this is the uniformly-parabolic Shi estimate, consistent with the requirement that the center $p$ have its geodesic buffer inside the plateau. This closes provided the terminal metric's higher-derivative bounds on $\{a=1\}$ are recorded (they follow from plateau Shi and are compatible with the continuation module).

---

### Minor items for the record

- **Step 57 (2.2) typo.** It defines $s=\operatorname{tr}(E)-n=\operatorname{scal}+n$; correctly $\operatorname{tr}(E)=\operatorname{scal}+n$, so $s=\operatorname{tr}(E)-n=\operatorname{scal}$, and then $s+n=\operatorname{tr}E$, making $\partial_t d\mu=-a(s+n)d\mu=-a\,\operatorname{tr}(E)\,d\mu$ correct. The final formula and the bound $|s+n|\le\sqrt n|E|$ are right; only the intermediate identification "$=\operatorname{scal}+n$" is off by $n$.
- The $|G|^2=2/3$ convention is used consistently across Step 54 §2.1/§9.2 and Step 57; $\mathrm{Ric}(G)=g$ checks out and underlies $E$ being the Ricci contraction of $T$.

---

### Next proof object to write

Write the **finite-order collar current-pair induction to order $s_0+1$ ($\approx 8$ in $n=4$)** and couple it to the triangular fixed-background integration:
$$\{(U_j,C_{j+1})\}_{j\le s_0+1}\ \text{finite in every }L^p\ \xRightarrow{\ \bar\nabla^m A\ \text{triangular}\ }\ g(T^*)\in H^{s_0},$$
proving the smooth restart that both notes leave as the one unwritten analytic step. It should (a) carry the explicit $\chi$-weight at each order as Step 56 does at first order, (b) show the highest cutoff jet $C_{m+2}$ pairs with weighted dissipation, and (c) invoke A01 §2.3's $\bar\nabla^{m+1}g=(\bar\nabla^mA)*g+P_m$ to convert to fixed-chart metric bounds. Alongside it, record the two one-line reconciliations that make the assembled interface airtight: the volume-floor lemma $C_0\le C H_2$ (item ii), and the corrected smallness bound (1.17) with the $r^2$ factor restored to match (1.16) and the verification sample.

None of this establishes the plateau/positive branch, arbitrary 4-topology, $n\ge5$, dimension-only constants, the terminal spectral-density mechanism (Steps 43/47), or any Lean formalization; the present material is one direction of the dimension-4 restricted route with the analytic interface now consistent modulo the finite collar induction identified above.