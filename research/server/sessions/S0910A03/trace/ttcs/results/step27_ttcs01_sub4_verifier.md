# TTCS Independent Branch Record

```json
{
  "step_id": 27,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step27_shifted_curvature_continuation_analysis.md",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Check the logical interface between a normalized local-flow extension theorem and the existing Step 26 first-exit chain. Determine whether a terminal-time assumption sup|a Rm|<∞ really supplies all hypotheses needed for the shifted-curvature Wang induction on a closed manifold, with constants allowed to depend on the individual smooth initial metric/cutoff, and whether bounds for all ∇^m(a(Rm+G)) suffice for smooth extension. Identify any overlooked issue involving zeros of a, unweighted L^p curvature, evolving contraction Ric(aT)=a Ric(T), transported DeTurck coefficient, or support collar. Also assess whether the claimed whole-support Moser bound is strong enough near a terminal time despite its C/t form.

## Output

## Verification memo: normalized-flow extension ↔ Step 26 first-exit interface

### Bottom line

The shifted-curvature construction is algebraically correct and the transfer mechanism it describes is genuinely plausible. On a closed manifold with $T<\infty$ and constants permitted to depend on $(g_0,\chi,T)$, the single tensor bound $\sup_{M\times[0,T)}|a\operatorname{Rm}|<\infty$ does supply the structural ingredients Wang's induction needs, and bounds on all $\nabla^m U$, $U=a\widetilde R=a(\operatorname{Rm}+G)$, would suffice for smooth extension. But the interface has one load-bearing step that is asserted rather than executed, and one logical-order issue between the extension statement and the first-exit closure that must be arranged so the two do not assume each other.

### What the hypothesis verifiably supplies

I checked each ingredient the induction rests on and each survives the normalization:

1. **Shift identities (eq. 1.1–1.5).** $G=\tfrac1{n-1}(g_{ik}g_{jl}-g_{il}g_{jk})$ gives $g^{ik}G_{ijkl}=g_{jl}$, hence $\operatorname{Ric}(\widetilde R)=\operatorname{Ric}+g=E$; correct. $\nabla G=0$ (metric compatibility), so $\nabla^k\widetilde R=\nabla^k\operatorname{Rm}$ for $k\ge1$ and $\Delta\operatorname{Rm}=\Delta\widetilde R$; correct. $\partial_tG=\tfrac1{n-1}(h_{ik}g_{jl}+\dots)$ with $h=-2aE$ is algebraic in $E$ with **no** $\nabla a$ or $\nabla E$; correct and important. $|a\widetilde R|\le|a\operatorname{Rm}|+C_n$ since $a\le1$ and $|G|$ is dimension-set; so (0.2) is equivalent to a bound on $a\widetilde R$. All verified.

2. **Metric equivalence and cutoff/Sobolev bounds (eq. 4.1).** $|aE|=|\operatorname{Ric}(U)|\le C_n|U|=C_n|a\widetilde R|\le C_n(|a\operatorname{Rm}|+C_n)$. With $T<\infty$, $\int_0^t|\partial_tg|\le CT$, so $e^{-CT}g_0\le g(t)\le e^{CT}g_0$ and $|\nabla\chi|_{g(t)}$, the Sobolev constant, are uniformly controlled. This is the Proposition 4.9 analogue and it holds; the extra $ag$ piece of $aE$ is bounded by $a\le1$, making equivalence even more direct than in Wang. The dependence of the constant on $T$ is consistent with the stated permission for $(g_0,\chi)$-dependent constants.

3. **Unweighted $L^p$ base estimate (eq. 4.2).** Testing (2.1) against $|\widetilde R|^{p-2}\widetilde R$ and integrating $(\nabla^2a)*\operatorname{Ric}(\widetilde R)$ by parts once, the surviving $|da|\,|\nabla\widetilde R|\,|\widetilde R|^{p-1}$ absorbs via Young with the recurring saving $|da|^2/a=4|\nabla\chi|^2$ bounded; the cubic $\int a|\widetilde R|^{p+1}\le|a\widetilde R|_\infty\int|\widetilde R|^p$ is tamed by the zeroth-order bound; the $G$-generated linear/constant terms integrate over compact $M$ to an additive constant. So $\tfrac{d}{dt}\int|\widetilde R|^p\le C_p(1+\int|\widetilde R|^p)$ closes, giving the Lemma 4.10 analogue. Verified.

4. **Cutoff evolution (eq. 3.5–3.6).** $\partial_t\Gamma=\nabla(aE)=\nabla\operatorname{Ric}(U)$. Because $\nabla g=0$, $\nabla^q(aE)=\nabla^q\operatorname{Ric}(U)=\operatorname{Ric}(\nabla^qU)$ **exactly** at fixed time, so the $ag$ part is absorbed and no separate $\nabla^q(ag)$ source remains. This is the Lemma 4.6 analogue with $\chi^2\operatorname{Ric}\mapsto aE=\operatorname{Ric}(U)$, and it is the strongest correct point of the note: the whole velocity is one curvature-type contraction.

5. **Sufficiency of $\nabla^mU$ bounds for extension.** $\nabla^m(aG)=(\nabla^ma)*G$ is smooth and bounded, so $\nabla^mU$ bounds $\Leftrightarrow$ $\nabla^m(a\operatorname{Rm})$ bounds. Spatial jets of the velocity $aE=\operatorname{Ric}(U)$ equal $\operatorname{Ric}(\nabla^mU)$; time derivatives reduce to spatial $\nabla^{m+2}U$ through $\partial_ta=0$, $\partial_t\Gamma=\nabla\operatorname{Ric}(U)$, $\partial_tG=\operatorname{Ric}(U)*g$. Hence all space-time jets of the compactly supported velocity are controlled and Hamilton's reconstruction (Proposition 4.3 analogue) applies. Verified.

6. **Transported DeTurck coefficient (eq. 6.1–6.2).** Adding $-2\widehat a\,\widehat g$ to the hatted equation is zeroth order in $\widehat g$; the second-order operator $-2\widehat a\operatorname{Ric}(\widehat g)+\widehat\delta^*(\cdots)$ is unchanged, so short-time existence transfers from Yang. Under $\varphi_t^*$ with $\varphi_t^*\widehat a=\chi^2$, $\varphi_t^*\widehat g=g$, the added term pulls back to $-2ag$ and the Lie term recovers (0.1). Correct; no coupling beyond Yang's own $(\chi\circ\varphi_t^{-1})^2$.

### The one load-bearing step that is asserted, not executed

The dependency cycle in Section 3 (items 1–3) closes at each level $m$ only through the coupling
$$
\|\nabla^{m+1}\chi\|_p \ \longleftrightarrow\ \|\nabla^{m}U\|_p ,
$$
which in Wang is resolved by the coupled differential inequality of Lemma 4.11 fed into Lemma 4.8 ($y'\le a\int_0^t y+by+1$), after integrating by parts the top term $\chi\nabla^{m+2}\chi*U$ (eq. 3.3, eq. 2.4). The note states this is "structurally the same," and eq. (3.6) does match Lemma 4.6 with $aE=\operatorname{Ric}(U)$, which makes the transfer credible. But the coupled Gronwall for the shifted, normalized system is not written. This is precisely where the cyclic $\nabla^{m+1}\chi/\nabla^mU$ interplay is actually broken; asserting structural sameness is not the same as producing the two-variable integral inequality with the shifted reaction and showing its solution stays finite on $[0,T)$. Until that is carried out (and Lemma 4.11, Propositions 4.13–4.14 rewritten with $\mathcal L_{G,m}$ present), the statement is a mechanism, matching the note's own Section 5. The commutator term $\operatorname{Ric}(\nabla^mU)*\widetilde R$ from $\partial_t\Gamma=\nabla\operatorname{Ric}(U)$ (top order $\times$ zeroth order $\widetilde R$, with $\widetilde R$ only in $L^p$, not $L^\infty$) is the specific piece that must be shown to land in the same three families via the Wang Lemma 4.4/4.13 $L^p$ reaction handling, not merely folded into $\mathcal L_{G,m}$.

### Logical order between extension and first-exit closure

Step 26 §6.2 states its first-exit closure is "conditional on smooth existence of the flow to time $\theta r^2$," and Step 27 §7 offers the extension theorem to supply that existence. These must not each assume the other. The clean arrangement is a continuity argument on the **maximal** existence interval $[0,T_{\max})$: derive the first-exit estimates and the Moser bound using only quantities controlled on $[0,T_{\max})$; conclude $\sup_{[0,T_{\max})}|a\operatorname{Rm}|<\infty$ whenever $T_{\max}<\infty$; then the extension theorem forces $T_{\max}\ge\theta r^2$. The estimates are forward-integrated differential inequalities and appear compatible with this, but the present wording ("conditional on smooth existence to $\theta r^2$") reads as though the full slab is presupposed when the Moser/first-exit chain is run. Recasting eq. (5.1)–(5.7) and the (F1)–(F4) improvement on $[0,T_{\max})$ removes the mutual assumption.

### The $C/t$ bound near a terminal time

The whole-support bound $|a\operatorname{Rm}(t)|\lesssim\bar\beta/t$ (eq. 5.6, $0<t\le r^2$) is adequate to feed the extension near a **positive** terminal time: on $[t_0,T)$ it is $\le C\bar\beta/t_0<\infty$, and short-time existence covers $[0,t_0]$ where the initial data is smooth. So the $C/t$ form causes no difficulty at $t=0$ (it is a regularization estimate improving for $t>0$), and its finiteness on $[t_0,T)$ is exactly Wang's terminal-time hypothesis, as §8 notes ("starting from any positive time $t_0$"). The only thing this rests on is the bootstrap of the previous paragraph — the $C/t$ bound must itself be valid on $[0,T_{\max})$.

### Zeros of $a$, unweighted $L^p$, evolving contraction

- **Zeros of $a$ / noninteger weight (Step 26 §3.4).** The $\chi^{2(p-2)}$ smoothness issue lives only in the Moser iteration with $p_j=3(3/2)^j$; the extension induction (Step 27) uses integer $m$ and the $C^\infty$ weight $a=\chi^2$, so it is untouched. For $p\ge3$ the weight is at least $C^1$ and only its first derivative enters the energy estimates; $a_\varepsilon=\chi^2+\varepsilon$ with dominated convergence, or a $\chi$ infinitely flat at $\partial\operatorname{supp}\chi$, closes it. The unifying fact $|da|^2/a=4|\nabla\chi|^2$ has a bounded extension across $\{\chi=0\}$. This is manageable and kept separate from the higher-derivative extension argument.
- **Unweighted $L^p$ curvature.** Verified in item 3 above; runs on $|a\widetilde R|_\infty$ and $|\nabla\chi|_\infty$ alone.
- **Evolving contraction $\operatorname{Ric}(aT)=a\operatorname{Ric}(T)$.** Spatially exact because $\nabla g=\nabla g^{-1}=0$, so $\nabla^m(aE)=\operatorname{Ric}(\nabla^mU)$ with no spatial lower terms. The genuinely time-dependent piece is $\partial_tg^{ik}=2aE^{ik}=2\operatorname{Ric}(U)^{ik}$, which is itself a bounded curvature contraction and introduces no cutoff derivative; together with $\partial_tG=\operatorname{Ric}(U)*g$ this is why $\mathcal L_{G,m}$ carries no new highest-order cutoff source. The residual obligation is only to display each $\mathcal L_{G,m}$ term in one of the three families, per the previous section.

### Distance to the stated top goal

Even a fully written extension theorem plus the first-exit closure serves only the four-dimensional $\lambda<0$ Ishida–LeBrun critical family, with the geometric endpoint being the Step 6 projector / Einstein–Weyl contradiction (Step 27 §7). The $\lambda\ge0$ situations, arbitrary topology, dimensions $\ge5$, the existence of the dimensional constants $c_n<C_n$ in the general statement, and the Lean 4 formalization are entirely outside what this chain addresses. The analytic work here is a self-consistent piece of one conditional route, not a segment that by itself moves the full Yau-26 statement.

### Concrete items to resolve

1. Write the two-variable integral inequality (shifted Lemma 4.11 + Lemma 4.8) that breaks the $\|\nabla^{m+1}\chi\|_p\leftrightarrow\|\nabla^mU\|_p$ cycle, with $\mathcal L_{G,m}$ explicit, and confirm the commutator term $\operatorname{Ric}(\nabla^mU)*\widetilde R$ is absorbed by the weighted diffusion plus lower families.
2. State the first-exit and Moser estimates on $[0,T_{\max})$ and the continuity step $T_{\max}<\infty\Rightarrow$ extension, so the extension theorem and the closure are not mutually presupposed.
3. Verify the $a_\varepsilon$-regularized weight passage for the Moser powers $p_j$ separately, confirming it does not feed back into the integer-$m$ extension induction.

The remaining verifications (shift algebra, base $L^p$, metric equivalence, DeTurck transport, sufficiency of $\nabla^mU$) I was able to confirm from the supplied Wang and Yang texts and the internal derivations; the reproducibility scripts named in §8/§9 were not executed here, so the algebraic bookkeeping of $\mathcal Q_G$ and $\mathcal L_{G,m}$ rests on the hand derivation above rather than on independent code output.