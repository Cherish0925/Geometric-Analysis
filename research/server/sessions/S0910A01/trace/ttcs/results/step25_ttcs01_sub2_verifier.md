# TTCS Independent Branch Record

```json
{
  "step_id": 25,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step25_tensor_energy_derivation.md",
    "Sessions/S0910A01/workspace/notes/step25_first_exit_formulation.md",
    "Sessions/S0910A01/workspace/notes/step24_buffered_support_energy_test.md",
    "Sessions/S0910A01/workspace/scripts/step25_tensor_energy_verification.py"
  ]
}
```

## Task

Verify the q=2 curvature energy derivation in workspace/notes/step25_tensor_energy_derivation.md. The note claims that under the buffered cutoff flow d_t g = -2 chi^2(Ric+g) on a closed 4-manifold with supp(chi) compactly inside {eta=1} and supp(grad eta) in {chi=0}, the energy H_2 = int eta^2 F^2 dmu satisfies H_2' + c D_2 <= C int(eta^2 a F^3) + C r^{-2} H_2, where D_2 = int(eta^2 a |grad Rm|^2). Check: (1) Is the term classification (Types A-D, metric variation, volume form) complete? Are there missing terms from the curvature variation formula under h = -2aE? (2) Is the integration by parts of the Hessian(a) terms correct? Does the cross term grad a . grad eta genuinely vanish? (3) Are the Young inequality absorptions correct with the coefficient |grad a|^2/a = 4|grad chi|^2? (4) Is the global defect identity Q_global(t) <= e^{C theta} Q_global(0) correct? (5) For the first-exit Approach A: is it correct that the short-time existence interval theta r^2 <= c/K_0 is compatible with the maximal-function good center hypothesis K_0 ~ r^{-2}? Identify any errors, missing terms, or logical gaps.

## Output

# Verification Memo: q=2 curvature energy derivation (Step 25)

Prepared in a clean context. I checked the five points against the tensor algebra of the normalized cutoff flow $\partial_t g=-2aE$, $a=\chi^2$, $E=\operatorname{Ric}+g$, $F=(1+|\operatorname{Rm}|^2)^{1/2}$, using the buffered geometry $\operatorname{supp}\chi\Subset\{\eta=1\}$, $\operatorname{supp}\nabla\eta\subset\{\chi=0\}^\circ$. Points 1–4 stand at the schematic level with the structure the note asserts; point 5 contains a genuine unresolved step and a mismatch in how $K_0$ is used. Details follow.

## (1) Term classification — complete at schematic level; one input is asserted, not derived

The decomposition is correct and I find no missing term.

- The time derivative splits cleanly: $\eta$ is time-independent and $\partial_t F^2=\partial_t|\operatorname{Rm}|^2$ (the constant $1$ contributes only through the volume form), so $\frac{d}{dt}H_2=$ (I) principal + (II) volume, with (I) = $2\langle\operatorname{Rm},\partial_t\operatorname{Rm}\rangle$ + metric-variation-of-norm. This is exhaustive.
- The variation formula $\partial_t\operatorname{Rm}=\tfrac12\nabla^2 h+\operatorname{Rm}*h$ with $h=-2aE$, expanded by the Leibniz rule $\nabla_i\nabla_k(aE_{jl})=a\nabla_i\nabla_kE_{jl}+(\nabla_ia)(\nabla_kE_{jl})+(\nabla_ka)(\nabla_iE_{jl})+(\nabla_i\nabla_ka)E_{jl}$, produces exactly Types A–D. I checked that the conformal part $-2ag$ contributes only $(\nabla^2a)*g$ to the second-derivative piece (since $\nabla g=0$), routed into Type C, and an algebraic $a\operatorname{Rm}*g\sim a\operatorname{Rm}$ term bounded by $Ca|\operatorname{Rm}|^2\le CaF^2\le CaF^3$. No term is orphaned.
- Every reaction term collapses to $\int\eta^2 aF^3$: volume form via $|s+n|\le C_nF$ so $F^2\cdot F$; metric-norm variation via $\partial_tg^{ij}=2aE^{ij}$ giving $Ca|E||\operatorname{Rm}|^2\le CaF^3$; Type D via $Ca|E||\operatorname{Rm}|^2$; Hamilton $\operatorname{Rm}^3$ via $CaF^3$. All consistent with the boxed (2.19).
- The algebraic bounds (1.1)–(1.3) are correct: $|E|\le C_n(|\operatorname{Rm}|+1)\le\sqrt2\,C_nF$, $|\nabla E|=|\nabla\operatorname{Ric}|\le C_n|\nabla\operatorname{Rm}|$, $|s+n|\le\sqrt n|E|$.

The one thing that is asserted rather than computed is the Type-A reduction: "$\nabla^2\operatorname{Ric}$ combines through Bianchi to $\Delta\operatorname{Rm}+\operatorname{Rm}^2$." With variable $a$, pulling $a$ outside the second derivatives leaves the residual $a(\Delta\operatorname{Rm}+Q(\operatorname{Rm}))$, and the Bianchi commutations generate additional $\operatorname{Rm}*\operatorname{Rm}$ pieces — all of which land inside the cubic reaction. The *structure* (principal $a\Delta$, dissipation $-2a|\nabla\operatorname{Rm}|^2$ with correct sign, cubic reaction) is right, but the exact index-level Bianchi computation with the $a$-weight and the precise constant in front of $D_2$ is not written out. The note itself flags this ("a complete proof still requires writing the exact tensor variation"). For a schematic energy inequality with unnamed constants this is acceptable; for the eventual formalization it is real work, because the coefficient of $D_2$ (here $2$) must survive the three Young subtractions with margin, and that margin is only meaningful once the true principal constant is pinned.

## (2) Integration by parts of the Hessian(a) terms — correct; the cross term vanishes pointwise

The IBP $I_C=\int\eta^2(\nabla_i\nabla_ka)T^{ik}=-\int 2\eta(\nabla_i\eta)(\nabla_ka)T^{ik}-\int\eta^2(\nabla_iT^{ik})(\nabla_ka)$ is the correct product-rule expansion, no boundary term on closed $M$.

The cross term vanishes for a reason stronger than an inner-product identity: it always carries the factor $\nabla_k a=2\chi\nabla_k\chi$, which has an explicit $\chi$ factor and therefore vanishes on the whole set $\{\chi=0\}\supset\operatorname{supp}\nabla\eta$. So the product $(\nabla_i\eta)(\nabla_ka)T^{ik}$ is zero pointwise regardless of the tensor structure $T^{ik}$ — it is not merely $g^{ik}(\nabla_ia)(\nabla_k\eta)=0$. This is robust and does not even require the interior condition $\{\chi=0\}^\circ$; the interior is used for the other cancellations $a|\nabla\eta|^2=0$ and for the collar being stationary. All of (0.1) check out.

The main term $-\int\eta^2(\nabla_iT^{ik})(\nabla_ka)$ with $\nabla T\sim\nabla\operatorname{Rm}\cdot F$ (using $|\nabla E|\le C|\nabla\operatorname{Rm}|$, $|E|\le CF$, $\nabla g=0$), then Young, gives $\varepsilon''D_2+\tfrac{C}{\varepsilon''r^2}H_2$. Correct.

## (3) Young absorptions — correct, including the removable-singularity coefficient

The coefficient $|\nabla a|^2/a=4\chi^2|\nabla\chi|^2/\chi^2=4|\nabla\chi|^2\le 4C_\chi^2/r^2$ is the standard fact; the apparent singularity at $a=0$ is removable because $\nabla a=2\chi\nabla\chi$ vanishes there together with $a$. Each Young split $|\nabla a|\,|\cdot|\,|\nabla\operatorname{Rm}|=(\sqrt a|\nabla\operatorname{Rm}|)(\tfrac{|\nabla a|}{\sqrt a}|\cdot|)\le\tfrac\varepsilon2 a|\nabla\operatorname{Rm}|^2+\tfrac1{2\varepsilon}\tfrac{|\nabla a|^2}{a}|\cdot|^2$ is valid. The dissipation bookkeeping is consistent: principal $-(2-\varepsilon)$, Type B $+\varepsilon'$, Type C $+\varepsilon''$, with $\varepsilon=\varepsilon'=\varepsilon''=\delta_0/3$ summing to net $-(2-\delta_0)D_2$, matching (2.19) and the verification script's $c=2-3\varepsilon$. The residual counter-terms all take the form $Cr^{-2}H_2$. No error here.

## (4) Global defect identity — correct, with the clean argument being the frozen-collar cancellation

The boxed conclusion $Q_{\rm global}(t)\le e^{C\theta}Q_{\rm global}(0)$ is right, but the cleanest justification uses the frozen collar explicitly, which I confirmed by recomputation. Let $Q_j(t)=\int\eta_j^2|E|^2\,d\mu_t$ (the quantity the support estimate (3.6)/(7.4) actually controls), split $Q_j=Q_j^{\rm act}+Q_j^{\rm collar}$ where the active part is over $\operatorname{supp}a_j$ (there $\eta_j=1$) and the collar is $\{\eta_j<1\}$. On the collar $a_j=0$, so the metric is stationary and $Q_j^{\rm collar}(t)=Q_j^{\rm collar}(0)$ is constant. The exact global identity is
$$Q_{\rm global}(t)-Q_{\rm global}(0)=\sum_j\big[Q_j^{\rm act}(t)-Q_j^{\rm act}(0)\big].$$
Because the collar is constant, $Q_j^{\rm act}(t)-Q_j^{\rm act}(0)=Q_j(t)-Q_j(0)\le(e^{C\theta}-1)Q_j(0)$ from $Q_j(t)\le e^{C\theta}Q_j(0)$. Summing and using disjoint $\Omega_{\eta,j}$ (so $\sum_j\eta_j^2\le1$ pointwise, hence $\sum_jQ_j(0)\le Q_{\rm global}(0)$) gives exactly the note's (4.1). The subtlety I want to record: if one instead bounds the *unweighted* active integral by the *full weighted* $Q_j(t)$ and subtracts only the active initial part, one appears to over-count the collar; the collar being genuinely frozen is what makes the amplification factor $(e^{C\theta}-1)$ multiply the full $Q_j(0)$ rather than something larger. So the result holds, but it rests on the collar-stationary property, and it is only as strong as (3.6)/(7.4), which themselves rest on $\beta_a$-smallness and metric comparability. The note correctly presents (4.1) as a conditional consequence.

## (5) First-exit Approach A — genuine unresolved step and an inconsistent use of $K_0$

This is where I see the real problem. Two distinct issues.

**(5a) The good-center hypothesis is $L^2$-averaged and does not supply the pointwise bounds Approach A uses.** The hypothesis is $\mathcal M_{R_0}(|\operatorname{Rm}_{g_0}|^2)(p)\le K_0$, i.e. $\fint_{B_\rho}|\operatorname{Rm}|^2\le K_0$ for $\rho\le R_0$. Short-time existence of the modified flow and the estimate on $|E(s)-E(0)|=|\int_0^s\partial_t E|$ both require a *pointwise* curvature bound (and, for $\partial_t E\sim a\Delta_L E+\dots$, second-derivative/Shi control). An $L^2$ average of $|\operatorname{Rm}|^2$ does not bound $\sup_{\Omega_\eta}|\operatorname{Rm}|$; pointwise curvature can spike where the average stays bounded. So the sentence "the $E$-variation is controlled by the smoothness of the flow, but its bound depends on initial curvature $K_0$" silently upgrades an averaged bound to a pointwise one. The only standard bridge in 4D is $\varepsilon$-regularity: $\int_{B_r}|\operatorname{Rm}|^2<\varepsilon_0\Rightarrow|\operatorname{Rm}|\lesssim r^{-2}$. But the good-center bound gives $\int_{B_r}|\operatorname{Rm}|^2\le K_0\,\mathrm{Vol}(B_r)\sim K_0r^4$, which is a *smallness* only if $K_0r^4<\varepsilon_0$, i.e. a genuine additional input, not automatic. This is the load-bearing step Approach A does not establish, and it is the same critical scale-invariant quantity that shrinking $r$ does not obviously improve.

**(5b) The scaling "$K_0\sim r^{-2}$" is dimensionally inconsistent and conflicts with the smallness used in Step 24 §2.** $K_0$ is an average of $|\operatorname{Rm}|^2$, so dimension (length)$^{-4}$. Then $t_0\le c/K_0$ has dimension (length)$^4$, not a time (length$^2$), and "$K_0\sim r^{-2}$" would be (length)$^{-2}$. The dimensionally coherent version is $\sqrt{K_0}\sim r^{-2}$ (pointwise curvature scale), $t_0\le c/\sqrt{K_0}\sim cr^2$, giving $\theta r^2\le t_0\Leftrightarrow\theta\le c$. More importantly, in Step 24 (2.3) the construction needs $\beta_0\sim r^2\sqrt{1+K_0}$ *small*, which for a fixed good-center $K_0$ is achieved by taking $r\to0$. If instead one sets $K_0\sim r^{-4}$ (the dimensionally correct reading of "$K_0\sim r^{-2}$" as a curvature scale), then $\beta_0\sim r^2\sqrt{K_0}\sim r^2\cdot r^{-2}=O(1)$, i.e. no longer small — this would break the very absorption threshold $C_*\beta_0<c/4$ that the whole q=2 closure depends on. So the two places treat $K_0$'s relation to $r$ in mutually incompatible ways: fixed-$K_0$-with-$r\to0$ in §2 versus $r$-dependent-$K_0$ in Approach A.

**(5c) The "$O(\delta)$ displacement" label is inaccurate.** From $|\partial_t g|\le2|E|$ one gets $|g(t_0)-g_0|\le2\delta t_0+2\int_0^{t_0}|E(s)-E(0)|ds$. Since $C^0$-smallness of $E(0)$ does not give $C^2$-smallness, $|\partial_tE|$ is a curvature-scale quantity $\sim\Lambda$, not $\sim\delta$; the second integral is $\sim\Lambda t_0^2$. With $\Lambda\sim r^{-2}$, $t_0\sim cr^2$, this is $\sim r^2$, which does tend to $0$, but it is $O(r^2)$, not $O(\delta)$ — the flow-variation displacement, not the initial defect, dominates. So the interval on which (F3) holds is governed by $r^2$ (if the pointwise bound existed), and the initial-defect $\delta$ is not what makes the displacement small. The conclusion "for $\delta$ small, (F3) holds on $[0,c/K_0]$" attributes the smallness to the wrong quantity.

Net for point 5: Approach A does not close (F3) from the stated hypothesis. The missing substance is a pointwise curvature bound (with derivative control) on the active support, obtained from an $\varepsilon$-regularity-type input that requires $\int_{B_r}|\operatorname{Rm}|^2$ to be genuinely below a threshold — a critical 4D quantity that the maximal-function bound $K_0$ alone does not deliver, and whose smallness under $r\to0$ must be reconciled with the smallness $\beta_0\to0$ used in §2. This is consistent with the note's own listing of "smooth existence" and "metric comparability" as unproved inputs, but Approach A presents (F3) as derivable from the good-center hypothesis, and that presentation is where the reasoning outruns what is established.

## Summary of what is solid versus what needs substance

- Solid at schematic level: the A–D/metric/volume inventory (1); the Hessian IBP and the pointwise vanishing of the cross term via the explicit $\chi$ factor (2); the Young absorptions and the removable coefficient $|\nabla a|^2/a=4|\nabla\chi|^2$ (3); the global defect identity, correctly resting on the frozen collar and disjoint supports (4).
- Needs actual computation before it becomes a theorem: the exact Bianchi reduction of the Type-A term with variable $a$, pinning the principal $D_2$ constant so the three Young subtractions retain positive margin (item 1).
- Unresolved reasoning: the pointwise-curvature/derivative control that Approach A needs is not implied by the $L^2$ maximal-function hypothesis; the $K_0$–$r$ scaling is dimensionally incoherent and incompatible with the §2 smallness; the displacement is $O(r^2)$, not $O(\delta)$ (item 5).

The concrete input that would resolve point 5 is an $\varepsilon$-regularity statement for the modified flow $\partial_t g=-2\chi^2(\operatorname{Ric}+g)$ turning $\int_{B_r}|\operatorname{Rm}_{g_0}|^2<\varepsilon_0$ into $\sup_{\operatorname{supp}\chi}|\operatorname{Rm}(t)|\lesssim r^{-2}$ with Shi-type derivative bounds on $[0,\theta r^2]$, together with an explicit statement of whether $K_0r^4<\varepsilon_0$ is available at the selected good centers or is an added hypothesis. Until that is in hand, (F3) via Approach A, and hence the first-exit closure it feeds, remains open in exactly the way the note's own "remaining analytic bottleneck" line indicates.