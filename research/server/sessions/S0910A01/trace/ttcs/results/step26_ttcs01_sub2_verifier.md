# TTCS Independent Branch Record

```json
{
  "step_id": 26,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step26_weighted_velocity_and_local_flow.md",
    "Sessions/S0910A01/workspace/scripts/step26_fixed_p_defect_velocity.py",
    "Sessions/S0910A01/workspace/scripts/step26_p6_defect_energy_ledger.py",
    "Sessions/S0910A01/workspace/notes/step25_first_exit_formulation.md",
    "Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Sessions/S0910A03/workspace/notes/step24_corrected_evolution_and_conditional_gap.md"
  ]
}
```

## Task

Verify the Step 26 correction to the buffered selected-support cutoff-flow route for Yau Problem 26. Focus on: (1) whether the Step 25 plateau-only metric-displacement argument is indeed insufficient and whether support-wide integral control of ||aE||_infty is the right metric-comparability target; (2) whether the fixed-p defect energy J_p=int eta^2 a^(p-2)|E|^p, especially p=6, has the claimed weights, Hessian/cutoff remainders, curvature potential F z_p^2, and initial bound from pointwise Ricci pinching without curvature high integrability; (3) whether the proposed p=6 positive-time weighted velocity estimate ||aE||_infty <= C delta (r^2/t)^(1/3) is a plausible next Moser target or hides a Hardy/degenerate-parabolic obstruction; (4) whether the reading of Yang local Ricci flow source correctly handles DeTurck transported coefficient and shows that short-time existence is only a starting point while uniform continuation to theta r^2 requires weighted curvature/velocity estimates; (5) identify any exact missing hypotheses or wrong weights. Do not decide the overall Yau problem; give a scientific verification memo for the analytic route.

## Output

## Verification memo — Step 26 weighted-velocity route for the buffered cutoff flow

Session context: normalized local Ricci flow $\partial_t g=-2\chi^2(\operatorname{Ric}+g)$, $a=\chi^2$, $E=\operatorname{Ric}+g$, $h=\partial_t g=-2aE$. I checked the five requested points against the tensor-energy derivation, the two Yang/Wang source papers, and the fixed-$p$ exponent scripts. Overall the correction is mathematically coherent, the exponents and weights are right, and — importantly — the p=6 velocity target and the metric-comparability target are not speculative new PDE statements: they are the exact analogues of estimates that Yang and Wang already prove. The genuine remaining work is narrower than the note states in one place and broader in another; both are identified below.

---

### 1. The metric-displacement target is the correct one, and it matches proven machinery

The metric-displacement identity (1.1)/(8.2) is the sharp Gronwall solution of $\partial_t\log g(v,v)=h(v,v)/g(v,v)=-2\,aE(v,v)/g(v,v)$; the pointwise driver at a point $x$ is $a(x)|E(x,t)|$, not $a(x)$ alone. The Step 25 assertion that the transition displacement is proportionally smaller because $a=\chi^2<1$ is genuinely unsound: if $|E|$ grows like $a^{-1}$ where the cutoff decays, $a|E|$ carries no small factor. So plateau control ($a=1$) cannot transfer the current-time Sobolev constant $A(t)$, the current gradient bound $|d\chi|_{g(t)}$, or the critical product $\beta_a(t)=A(t)^2\|F\|_{L^2(\operatorname{supp}\chi)}$ across the transition annulus $0<\chi<1$, where those quantities are evaluated.

This is exactly the mechanism Yang and Wang use. Yang's Theorem 9.2 runs a maximal-interval argument carrying $\tfrac12 g_0\le g(t)\le 2g_0$ on the whole support $\Omega$, and Wang's Proposition 3.12 obtains tensor-Lipschitz (bilipschitz) comparability precisely from $2\int_0^{t_0}\|\chi^2 \operatorname{Rc}\|_\infty\,ds\le\varepsilon/2$, then converts it to isoperimetric/Sobolev-constant comparability via Wang Proposition 3.6. Replacing $\operatorname{Rc}$ by the normalized defect $E$, the note's target
$$V(t)=\int_0^t\|aE\|_{L^\infty(\operatorname{supp}\chi)}\,ds\le\varepsilon_{\rm met}$$
is identical in form to Wang's driver. So point (1) is verified: support-wide integral control of $\|aE\|_\infty$ is the right object, and it is the same object the existing local-flow proofs control.

---

### 2. The fixed-$p$ defect energy has the stated weights; the p=6 ledger is correct

I recomputed each weight rather than trusting the scripts.

- Testing $\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E)$ against $\eta^2a^{p-2}|E|^{p-2}E$: the diffusion term integrates to effective weight $\nabla(a\cdot a^{p-2})=\nabla(a^{p-1})$, so the dissipation is $Z_p=\int\eta^2a^{p-1}|E|^{p-2}|\nabla E|^2$. Correct.
- Curvature potential: $z_p^2=\eta^2a^{p-1}|E|^p$, so $\int\eta^2a^{p-1}F|E|^p=\int Fz_p^2$. Correct (2.5).
- Cutoff remainder: the derivative on $a^{p-1}$ produces $a^{p-2}\,da\,|E|^{p-1}\nabla E$; Young against $Z_p$ leaves exactly $a^{p-3}|da|^2|E|^p=4|d\chi|^2a^{p-2}|E|^p\le Cr^{-2}a^{p-2}|E|^p$ using $|da|^2=4a|d\chi|^2$. Correct (2.4), and the p=6 `young_remainder` bookkeeping reproduces it.
- $\|\nabla z_p\|_2^2\le C(Z_p+r^{-2}J_p)$: the three pieces of $\nabla z_p$ are (i) the $d\eta$ term, which vanishes because $\operatorname{supp}d\eta\subset\{a=0\}$; (ii) the $da$ term, $=Cr^{-2}J_p$-density; (iii) the $\nabla E$ term, $=Z_p$-density. Correct (2.7).
- Sobolev absorption in $n=4$ ($L^4$ critical): $\|z_p\|_4^2\le A^2(\|\nabla z_p\|_2^2+r^{-2}\|z_p\|_2^2)$ with $\|z_p\|_2^2\le J_p$ (since $a\le1$), giving $\int Fz_p^2\le C\beta_a(Z_p+r^{-2}J_p)$. Correct (2.8), same critical product as the curvature energy.
- Weighted-velocity domination: $|aE|^p=a^2\,a^{p-2}|E|^p\le a^{p-2}|E|^p$ because $a=\chi^2\le1$. Correct (2.1), hence $\|aE\|_{L^p(\operatorname{supp}\chi)}\le J_p^{1/p}$ (using $\eta\equiv1$ on $\operatorname{supp}\chi$).
- Initial datum: $J_p(0)\le\int\eta^2a^{p-2}|E(0)|^p\le C\delta^p\operatorname{Vol}(\Omega_\eta)$ uses only pointwise pinching $|E(0)|\le C\delta$ and $a^{p-2}\le1$. Correct (2.2), and no high-power curvature integrability enters the initial datum.

A precise reading of "without curvature high integrability" is warranted: the *initial datum* needs only $C^0$ pinching; the *absorption* needs $\beta_a=A^2\|F\|_{L^2(\operatorname{supp}\chi)}$ small, and in dimension four $L^2=L^{n/2}$ is the critical curvature norm. So the route does require local critical ($L^2$) curvature smallness through $\beta_a$; it does not require any supercritical $\int|\operatorname{Rm}|^{p/2}$ input for the defect datum. The note's phrasing is consistent with this once one separates datum from absorption. The p=6 smoothness observation ($a^4=\chi^8$, $z_6=\chi^5|E|^3$) is a valid reason to prefer an even integer over generic $p$, avoiding non-smooth weight powers in the integrations by parts. Point (2) checks out.

A structural point worth recording: the defect equation (6.2)–(6.3) has every term of $\mathcal C_a(E)$ homogeneous in $E$, $\nabla E$, or $\tau=\operatorname{tr}E$, with no bare $(\nabla^2a)\!*\!g$ source. This is what makes $J_p$ carry the $\delta$-smallness rather than an $O(1)$ curvature size, and is forced by $\operatorname{div}E=\tfrac12 d\tau$. This triangular structure is the reason the defect must be Moser-iterated instead of directly quoting a Ricci bound (see point 3).

---

### 3. The p=6 velocity estimate is a plausible target because it is Yang's own estimate specialized

This is the point where the note under-states the strength of its position, and also where I found the sharpest confirmation.

Yang's local parabolic Theorem A.1 takes as its spacetime input exactly
$$\Big(\int_0^t\!\!\int_{B_0}\chi^{2p_0-n}f^{p_0}\Big)^{1/p_0},\qquad n=4\Rightarrow \chi^{2p_0-4}=a^{p_0-2},$$
i.e. $\int_0^t\!\int a^{p-2}|E|^p=\int_0^tJ_p\,ds$ with $f=|E|$, $p_0=p$. The fixed-$p$ defect energy is therefore precisely the quantity Yang's degenerate-operator Moser consumes, not a new construction. Its conclusion bounds $|\chi^2f|=|aE|$ with the leading time factor $t^{-(1+n/2)/p_0}$; combining with a bounded-in-time $J_p$ (so $\int_0^tJ_p\sim t$, contributing $t^{1/p_0}$) gives net $t^{-(n/2)/p_0}=t^{-2/p}$ in $n=4$. For $p=6$ this is $t^{-1/3}$, exactly (3.2)/(3.3). The A-power/volume cancellation in the script ($A^2\sim r^2\operatorname{Vol}^{-1/2}$, $A^{4/p}\cdot J_p^{1/p}\sim\delta$, times $t^{-2/p}$ gives $\delta(r^2/t)^{2/p}$) is arithmetically consistent and reproduces the same exponent independently.

The same conclusion appears as Yang Theorem 6.3(2) / Wang's appendix: $\|\chi^2\operatorname{Rc}\|_\infty\le \bar C A_0^{n/p}t^{-n/2p}[\cdots]K$, integrable in $t$ for $p>n/2$, which is exactly the integrable positive-time weighted bound Wang integrates for metric comparability. So the Hardy/degenerate-parabolic concern is answered structurally: Yang's iteration uses $\chi^{2p'}$ cutoff powers on the *degenerate* operator $\chi^2\Delta$ and closes. The Hardy obstruction the parallel note recorded arises only if one attempts an *unweighted* Nash/Moser scheme on $\Delta$, which would manufacture a $\chi^{-2}$ potential; the weighted $J_p$ formulation is precisely the correct framework and matches Yang's design.

Consequently the "weighted Moser step" listed as an open PDE theorem is, for a single fixed $p$, essentially Yang's Theorem A.1 / Corollary A.10, provided two inputs are supplied:

(a) **A scalar reduction.** Yang A.1 is for a scalar $f\ge0$ obeying inequality (A.2). One must derive from the pointwise identity (6.4),
$(\partial_t-a\Delta)|E|^2=-2a|\nabla E|^2+4aR_{ikjl}E_{ij}E_{kl}+2\langle E,\mathcal C_a(E)\rangle$,
a Kato inequality for $|E|$ whose first-order part matches Yang's $2a\chi|\nabla\chi||\nabla f|$ (the $a^k\nabla_kE$ terms, coefficient $\nabla a=2\chi\,d\chi$, do match) and whose zeroth-order cutoff part matches $b(|\nabla\chi|^2-\chi\Delta\chi)f$ (the $\tau a_{ij}$, $a_i{}^kE_{kj}$ terms). The measure hypothesis $\partial_t d\mu\le c\chi^2u\,d\mu$ holds with $u\sim F$ since $|\partial_td\mu|=|a\tau|d\mu\le CaF\,d\mu$. This reduction is routine but must be written; the tensor energy alone gives the $L^p$ persistence, not the $L^\infty$ step.

(b) **The potential is the q=3 curvature bound, not free.** Yang A.1 requires the potential $u\sim F$ to satisfy $(\int\chi^{q-n}u^{q/2})^{2/q}\le\mu\,t^{-(q-n)/q}$ with $q>n=4$. For $q=6$ this is a positive-time weighted $L^3$ curvature bound — exactly the note's $A^4\int\eta^2aF^3\le C\beta^3/t$. So the defect velocity estimate is downstream of a curvature Moser/mean-value step (upgrading $q=3$ spacetime integrability to a $t^{-1}$-type positive-time bound), which is itself a Moser step of the same character. The route therefore involves **two** coupled positive-time estimates, not one, and the coupling direction (curvature $L^3$ → defect potential) should be explicit in the first-exit package.

Net finding on point (3): (3.2) is not merely plausible; its exponent, weighted input, and $t$-decay coincide with proven Yang/Wang estimates. No fundamental Hardy obstruction is visible for the weighted formulation. The load-bearing items are the scalar Kato reduction (a) and the explicit curvature-potential coupling (b).

The integrability tail (3.4) is arithmetically correct: $\int_0^{\theta r^2}C\delta(r^2/t)^{2/p}dt=\frac{p}{p-2}C\delta\theta^{1-2/p}r^2$ (the $r$-powers combine to $r^2$), integrable at $0$ for $p>2$, and small for $\delta$ small independently of $r\le1$. Consistent with the parallel note's p=6 form $\tfrac32C\delta\theta^{2/3}r^2$.

---

### 4. The Yang source reading is accurate, with one correction that should be cited explicitly

Checked against the two source files:

- **DeTurck transported coefficient (Yang §8, Theorem 8.2, Approach 1).** The hatted system carries $(\chi\circ\varphi_t^{-1})^2$ in front of $\operatorname{Rc}(\hat g)$ and the DeTurck vector field, and $g=\varphi_t^*\hat g$ recovers $\partial_tg=-2\chi^2\operatorname{Rc}$ with the **fixed spatial** cutoff $\chi$. The note's reading is correct and this is a genuinely non-obvious point: naive DeTurck would transport the cutoff; Yang's construction is arranged so the pulled-back flow has the fixed $\chi^2$.
- **Uniform-time first-exit (Yang Theorem 9.2, (9.3)–(9.6)).** Correctly summarized: a maximal-interval argument carrying Sobolev (9.4), $\tfrac12g_0\le g\le2g_0$ (9.5), $L^{n/2}$ curvature (9.6), yielding $\|\chi^2\operatorname{Rm}\|_\infty\le CC_S(t\|\nabla\chi\|^2+1)t^{-1}$. Short-time existence (8.2) is indeed only the interval starter; the uniform bound is a bootstrap output.
- **Extension by weighted curvature (Wang §4, Theorem 4.1 / Prop 4.3).** Correctly read: the flow extends past $T$ under a uniform bound for $|\chi^2\operatorname{Rm}|_\infty$ (and, by induction, weighted derivatives), which is a weighted statement, not unweighted transition regularity.

One item to make explicit rather than implicit: Wang's paper states that Yang's own higher-derivative argument (the last paragraph of Theorem 9.2 invoking $\int|\nabla^m\operatorname{Rm}|^2$) is not reliable — "It is unlikely to directly get bounds for $\int|\nabla^mRm|^2$ … as claimed in Theorem 9.2 … Our method use induction which is based on $L^p$ estimate." So the correct citation for smooth extension/derivative control is Wang's induction (Lemmas 4.4–4.14, Prop 4.13–4.14), not Yang's direct $L^2$-derivative claim. The note already leans on Wang for the extension mechanism, which is right, but the memo record should say plainly that Wang repairs this specific part of Yang and that the derivative-bound propagation is Wang's, not Yang's.

- **Normalized-flow adaptation (note §5).** The extra $-2\chi^2 g$ is genuinely zeroth-order in $g$: under DeTurck it becomes $-2(\chi\circ\varphi^{-1})^2\hat g$ and pulls back to $-2\chi^2 g$; it enters only the $Dh$ (zeroth-order) coefficient of Yang's linearized system and is absorbed by Gronwall. Short-time existence, energy estimates, and the Moser structure survive with modified lower-order constants. The note's insistence that this be written before Theorem-9.2-type existence is inherited for the normalized flow is appropriate. There is no obstruction here, only routine transcription.

---

### 5. Missing hypotheses, couplings, and one thing that is stronger than stated

No wrong weight was found in the fixed-$p$ ledger; all exponents in (2.1)–(2.9), (3.1)–(3.4) reproduce under independent recomputation. The items that must be added or made explicit:

1. **Sobolev-constant scaling $A^2\sim r^2\operatorname{Vol}^{-1/2}$ is asserted, not derived.** This "collapse-cancelling" form is the crux of the volume cancellation in (3.2). It must be pinned to Yang's Theorem 7.4 (Croke isoperimetric bound → local Sobolev constant on the selected good ball) and the buffered good-set selection. A consistency check supports it: with this scaling, the constant part of $\|F\|_{L^2}$ contributes $A^2\sqrt{\operatorname{Vol}}\sim r^2$ to $\beta_a$ (small for small $r$), and the curvature part reduces to a scale-invariant local energy that the good-set choice makes small. But this is an input to be proved, and if $A^2$ scales otherwise, (3.2) carries a residual volume factor.

2. **Defect Moser potential = curvature $L^3$ bound.** As in point (3b), the first-exit package must carry the ordering: q=2/q=3 curvature energy persistence → positive-time weighted $L^3$ curvature bound (a curvature Moser/mean-value step) → this serves as the potential $u$, $q=6$, in the defect Moser → $J_6$ spacetime input → $\|aE\|_\infty\le C\delta(r^2/t)^{1/3}$. Two positive-time estimates, coupled in this direction.

3. **Tensor-to-scalar Kato reduction** for the defect (point 3a) — not supplied by the energy inequality, needed for the $L^\infty$ step.

4. **Why the defect variable and not $\operatorname{Ric}$.** Yang's $\|\chi^2\operatorname{Rc}\|_\infty\le CKt^{-n/2p}$ uses $K=\|\operatorname{Rc}\|_{L^p}=O(1)$ for a pinched metric — no smallness. The $\delta$-smallness lives only in $E=\operatorname{Ric}+g$. Running the Moser on the homogeneous defect equation (6.2) with datum $J_p(0)\le C\delta^p\operatorname{Vol}$ is the necessary reformulation that carries $\delta$ through. This is the genuine and correct innovation over quoting Yang; it should be stated as such, because it also explains why the triangular structure of (6.2)–(6.3) (no $(\nabla^2a)*g$ source) is load-bearing.

5. **Homothety-term insensitivity.** The parallel Step 24 note's "net damping" from $-2a\operatorname{Rm}$ was miscounted (the four inverse metrics give $+8a|Rm|^2$, tensor $-4a|Rm|^2$, measure $-4a$; net on $|Rm|^2d\mu$ is not coercive). The Step 26 route survives because the tensor-energy derivation never uses a damping sign — it bounds all algebraic/norm/measure reactions by $C\int\eta^2aF^3$ and $C\int\eta^2a^2F^4$ and absorbs them through $\beta_a$. So the earlier miscount does not propagate into any Step 26 estimate. This should be recorded as a consistency observation, since it means the surviving inequalities are the ones with no reliance on homothety coercivity.

6. **What the whole route addresses.** Every estimate above concerns the critical four-dimensional negative Ishida–LeBrun/LeBrun class, and the terminal step (calibrated Derdziński projector contradiction) is separate from the analytic package. The dimension-only quantifier of the full problem is not touched by this route; the note states this, and it is accurate.

---

### Summary of the verification

- Point (1): confirmed — plateau drift is insufficient, and support-wide $\int\|aE\|_\infty$ is the correct and proven-in-form comparability target (matches Wang Prop 3.12 with $E$ for $\operatorname{Rc}$).
- Point (2): confirmed — all weights, the Hessian/cutoff remainder $a^{p-3}|da|^2|E|^p$, the potential $Fz_p^2$, and the $C^0$-pinching initial bound are correct; p=6 is a valid smoothing choice.
- Point (3): confirmed as plausible and, more strongly, backed by Yang Theorem A.1 / Corollary A.10 / Theorem 6.3(2) with matching time exponent $t^{-2/p}=t^{-1/3}$; the weighted formulation avoids the Hardy obstruction; the open items are the scalar Kato reduction and the curvature-potential coupling, not a novel degenerate-parabolic theorem.
- Point (4): the DeTurck transported-coefficient reading, the first-exit uniform-time reading, and the weighted-curvature extension reading are all accurate; add the explicit note that Wang's induction (not Yang's $\int|\nabla^m\operatorname{Rm}|^2$ paragraph) is the reliable source for smooth extension, and that the normalized $-2\chi^2g$ term is a zeroth-order Gronwall-absorbable modification.
- Point (5): the four inputs above (Sobolev scaling, curvature-potential coupling, Kato reduction, normalized-flow transcription) plus simultaneous first-exit closure are the exact remaining analytic obligations; no wrong weight was found, and the defect-variable reformulation is the correct reason the route can carry $\delta$-smallness.