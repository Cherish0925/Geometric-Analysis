# TTCS Independent Branch Record

```json
{
  "step_id": 36,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step36_analytic_platform_and_global_Q.md",
    "Sessions/S0910A01/workspace/scripts/step36_platform_Q_verify.py",
    "Sessions/S0910A03/workspace/notes/step36_preceptor_interface_review.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Verify the Step 36 analytic-platform note for the restricted four-dimensional negative Ishida--LeBrun cutoff-flow route. Read the new note and script, A03's Step 36 Preceptor review, the Step 35 tensor identity note, and the Yang/Wang source objects. Please check: (i) whether the transported-coefficient normalized DeTurck formulation correctly pulls back to the fixed-cutoff flow and whether the linearized lower-order normalization discussion is sound; (ii) whether the quantifier separation between per-datum short-time existence, maximal-time extension, and sequence-uniform bootstrap quantities is mathematically appropriate; (iii) whether the separate global Q propagation estimate is correctly weighted and genuinely independent of J6/aE; (iv) whether the shifted-U extension target is stated without smuggling in unweighted curvature or pointwise cutoff-Hessian control; and (v) what concrete analytic calculation would most strengthen the route next. Do not treat the note as a completed proof of existence or of Yau Problem 26; identify exact hidden assumptions or equation-level gaps.

## Output

## Verification memo — Step 36 analytic platform (restricted 4D negative Ishida–LeBrun cutoff-flow route)

I read the Step 36 note and its script, A03's Step 36 review, the Step 35 tensor note, and the Yang (local Ricci flow, Section 8 / Appendix A) and Wang (pseudolocality, §3–4) source objects. Verdicts on the five requested points, with the exact equation-level content and hidden assumptions.

### (i) Transported DeTurck pullback and linearized normalization — sound

The pullback identity (1.5) is correct and internally consistent. With $g=\varphi_t^*\hat g$ and the standard transport formula $\tfrac{d}{dt}\varphi_t^*\hat g=\varphi_t^*(\partial_t\hat g+\mathcal L_{X_t}\hat g)$ where $X_t=\partial_t\varphi_t\circ\varphi_t^{-1}=-\hat aW$ (eq. 1.3), the gauge term $+\mathcal L_{\hat aW}\hat g$ in (1.2) cancels $\mathcal L_{-\hat aW}\hat g$, leaving $\varphi_t^*(-2\hat a(\operatorname{Ric}_{\hat g}+\hat g))$. Naturality of Ricci gives $\varphi_t^*\operatorname{Ric}_{\hat g}=\operatorname{Ric}_g$, and $\varphi_t^*\hat a=(a\circ\varphi_t^{-1})\circ\varphi_t=a$ (script D3), so the result is exactly $-2aE$. This works for **any** DeTurck field $W$; the specific $W$ is needed only to make (1.2) parabolic, not for the cancellation. So the pullback is robust and matches Yang's Section 8 structure.

The product-rule correction (1.4) $\mathcal L_{\hat aW}\hat g=\hat a\mathcal L_W\hat g+d\hat a\otimes W^\flat+W^\flat\otimes d\hat a$ is verified: $\nabla_i(\hat aW_j)+\nabla_j(\hat aW_i)=\hat a(\mathcal L_W\hat g)_{ij}+(d\hat a\otimes W^\flat+W^\flat\otimes d\hat a)_{ij}$ (script D1 is a genuine symbolic check). This confirms the central repair over the Step 35 formulation: a fixed coefficient $a\mathcal L_W\hat g$ omits the two first-derivative coefficient terms and does not pull back to (0.1); the transported $\hat aW$ does. A03's §2 reaches the same conclusion independently.

The normalization discussion (1.6)–(1.7) is sound at the schematic level. Linearizing the added $+\hat g$ gives $-2\hat a h$ (zeroth order in $h$) and $-2(\delta\hat a)(\operatorname{Ric}_{\hat g}+\hat g)$; since $\hat a\circ\varphi_t=a$ is fixed, $\delta\hat a=-d\hat a(\psi)$ carries $\psi$ undifferentiated, so both contributions land in Yang's zeroth-order $Dh$ and $E_0\psi$ slots and add no second derivatives of $h$. The principal $2\chi^2\Delta h$ and the first-order triangular structure are preserved.

Two things to pin down when the estimates are actually written, not defects of the note: (a) Yang's leading coefficient $2\chi^2$ in (1.6) should be reconciled with the DeTurck Ricci-linearization factor when the tame estimates are reproduced (the note quotes Yang faithfully, but the numerical constant on $\Delta h$ needs verification in the transported normalized system); (b) the note correctly states this is not closed by ordinary strictly-parabolic Schauder theory — Yang's degenerate energy/tame estimates must be redone for the transported system with the extra lower-order terms. This is an unproved analytic interface, correctly identified as such.

### (ii) Quantifier separation — appropriate and matches Yang/Wang

The three-layer split (per-datum existence on $[0,T_0(g_0,\chi))$; per-datum extension excluding finite $T_{\max}<\theta r^2$; sequence-uniform bootstrap of $Q$, drift, plateau curvature, Sobolev) is the correct logical structure and mirrors Yang Theorem 9.2: Theorem 8.2 supplies a nonempty (non-uniform) starting interval, and the maximal-interval energy argument then forces $T_{\max}\ge T_0$. The note's allowance that per-datum extension constants depend on $g(\tau),\chi,\tau,T_{\max}$ and need not be sequence-uniform is legitimate: for a single fixed input, extension needs finiteness of higher derivatives on $[\tau,T_{\max})$, not uniformity.

The coupling of existence and bound-propagation through the maximal-interval bootstrap is non-circular **provided** the two isolated interfaces hold: a nonempty starting interval (transported existence) and the statement "bounds up to $T_{\max}$ ⟹ smooth extension past $T_{\max}$" (shifted-$U$ extension). The note is explicit that without extension, self-improvement of the energy bounds alone does not prevent termination of the smooth solution. This is the honest state of affairs. The metric-drift input (2.1) uses $\int_0^t\|aE\|_\infty\,ds<\infty$, which is consistent: (4.3) gives $\|aE\|_\infty\le C\delta(r^2/t)^{1/3}$ with $t^{-1/3}$ integrable at $0$ (script G6 confirms the endpoint integral $=\tfrac32\delta\theta^{2/3}r^2$); the $\|aF\|_\infty\le C\gamma/t$ bound is used only for positive-time plateau curvature, not integrated from $0$.

### (iii) Global $Q$ propagation — correctly weighted and genuinely separate

The estimate closes as stated, and I reproduced the decisive step. The Hessian-$a$ contribution to $\partial_t Q_U$, via the Step 35 tensor $B_{\rm def}$ with $|B_{\rm def}|\le C|E|^2$ and $|\nabla B_{\rm def}|\le C|E|\,|\nabla E|$, after signed integration by parts produces terms $\sim\int|\nabla a|\,|E|\,|\nabla E|$, and Young gives
$$
|\nabla a|\,|E|\,|\nabla E|\le\varepsilon\,a|\nabla E|^2+C_\varepsilon\tfrac{|\nabla a|^2}{a}|E|^2=\varepsilon\,a|\nabla E|^2+C_\varepsilon r^{-2}|E|^2,
$$
using $|\nabla a|^2/a=4|\nabla\chi|^2\le Cr^{-2}$. This is exactly $\varepsilon X_U+C_\varepsilon r^{-2}Q_U$, so (3.3) closes without any pointwise evolving-Hessian bound. The quadratic vanishing of $B_{\rm def}$ at $E=0$ is genuinely used: it is what yields $\int\tfrac{|\nabla a|^2}{a}|E|^2$ rather than a worse scaling. The Hölder split $(2,4,4)$ and the dimension-4 critical Sobolev $H^1\hookrightarrow L^4$ in (3.5) are correct, and the reaction is linear in curvature ($\int aF|E|^2$), with **no curvature-only source** — the property that lets $Q$ close via Gronwall $Q(t)\le e^{Cr^{-2}t}Q(0)$, giving $e^{C\theta}$ at $t=\theta r^2$ (script S3).

Independence from $J_6$ and $\|aE\|_\infty$ is real. The toy model $a=x^2,\,E\sim x^{-1}$ has $aE=x$ bounded and $a^4|E|^6=x^2$ integrable while $|E|^2=x^{-2}$ has divergent integral (script Q6). The mathematical content is that near the zero set of $a$ the weighted quantities discard information the terminal calibration needs, so $Q$ must be carried as its own quantity; this is not asserting $Q$ actually diverges in the geometric flow (near $a=0$ the metric is frozen and $E$ is the finite initial defect). One shared dependence to keep visible: $Q$-propagation still assumes the moving Sobolev comparison $\mathcal S(t)\le2\mathcal S(0)$, the bilipschitz metric control, and $C\gamma\le c/2$ on the interval — the same platform hypotheses as $J_6$. $Q$ is independent of $J_6$ as a quantity, not independent of the shared existence/geometry hypotheses. The input $Q(0)/A\to0$ is an assumption on the initial Ishida–LeBrun sequence, external to this note.

### (iv) Shifted-$U$ extension target — stated without smuggling unweighted curvature

The target (2.5), $\sup_{M\times[\tau,T_{\max})}|U|<\infty\Rightarrow$ extension with $U=a(\operatorname{Rm}+G)$, is the correct object. Since $G=\tfrac{g\owedge g}{2(n-1)}$ is algebraic in $g$ and bounded under bilipschitz control, $\sup|U|<\infty$ is essentially Wang's extension condition $\sup|\chi^2\operatorname{Rm}|<\infty$ (Theorem 4.1) plus a bounded $G$-term, and Wang's Prop. 4.9 shows the metrics stay uniformly equivalent so $|\nabla\chi|_\infty$ and the Sobolev constant persist. I verified the algebraic support: $\operatorname{Ric}(G)=g$ and $\operatorname{Ric}(\operatorname{Rm})=\operatorname{Ric}$ give $\operatorname{Ric}(T)=E$, $\operatorname{Ric}(U)=aE$, hence $\partial_t g=-2\operatorname{Ric}(U)$ (2.3) and $\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)$ (2.4). The cutoff-jet equation (2.7) $\partial_t\nabla^2\chi=-(\partial_t\Gamma)*\nabla\chi$ is correct because $\chi$ is fixed on $M$ while $\nabla$ evolves; it matches Wang's Lemma 4.6.

The note does **not** smuggle unweighted control: it explicitly rejects declaring $\|T\|_\infty$ or $\|a\nabla\operatorname{Rm}\|_\infty$ finite from smoothness on subintervals, and states the remaining work is not a pointwise cutoff-Hessian estimate. A03's §3 independently identifies the same defect in the Step 35 continuation note. The base-pair schematic (2.8) mirrors Wang's $I_1,\dots$ in Lemma 4.11, and the signed-group IBP prescription (move the derivative off $\nabla^3\chi$, use the surviving $\chi$ to absorb $\nabla^2U$ into the weighted dissipation) is Wang's technique. The honest statement "this term-level base-pair proof is not present" is accurate.

**Exact equation-level gap in (iv):** the note asserts "all $G$-terms from the normalization must be written through this induction" but does not carry them. Wang's IBP absorption relies on $\chi^2\operatorname{Rm}$ having a curvature weight; in $U=a(\operatorname{Rm}+G)$, the $aG$ part is not curvature, and $\nabla^m G$ is controlled by metric jets/Christoffel data, not by curvature derivatives. It is not yet shown that the $\nabla^m(aG)$ contributions to $\partial_t\nabla^m U$ are absorbed by already-available metric-drift and lower cutoff-jet quantities rather than introducing a new curvature-derivative source. This is the concrete hidden assumption behind the "$G$-terms written through the induction" phrase.

### (v) The calculation that would most strengthen the route next

Derive $\partial_t U$ (equivalently $\partial_t T$) **explicitly and completely**, including every normalization and $G$ contribution, as the analog of Wang's Lemma 4.4/4.5 for the shifted normalized variable — then execute the coupled $L^p$ base-pair estimate for $(\nabla U,\nabla^2\chi)$, producing a closed inequality of Wang's Volterra form
$$
\tfrac{d}{dt}\big(\|\nabla U\|_p^2+\|\nabla^2\chi\|_p^2\big)\le a\!\int_0^t(\cdots)\,ds+b(\cdots)+1
$$
so Lemma 4.8 gives finiteness on $[\tau,T_{\max})$. This is the pivotal, most self-contained missing piece: it converts the extension roadmap into a checkable estimate and simultaneously confirms or corrects the schematic term list (2.8). The lowest-cost precursor is just the explicit $\partial_t U$ computation, because it feeds both the extension base pair and the transported-existence linearization, and it will immediately reveal whether the $G$-normalization introduces terms outside (2.8). Verifying that $\nabla^m(aG)$ closes on metric-drift + lower cutoff jets is the specific sub-computation to settle first.

### Note on the script's status

The verifier script mixes genuine symbolic checks (D1 Lie product rule; Q2 Hölder exponents; Q4 $\gamma=r^2\sqrt{K_0}$; Q6 toy exponents; S1/S3 algebra; G1–G4 graph reachability; G6 the drift integral) with structural assertions recorded as `check(tag, True, …)` (D2, D3, D4, Q1, Q3, Q5, S2, G5). The "all passed" count therefore does not certify the transported existence, the extension, or any Yau-26 content — the script's own closing text says exactly this. Reading the pass count as mathematical verification of D3/D4/Q3/Q5 would over-read it; those are premises the note states, not results the script computes.

### Overall

The note is a correct and useful consolidation: the transported DeTurck pullback and the separate $Q$ estimate are mathematically sound, the quantifier layering is appropriate, and the extension target avoids the errors A03 flagged in Step 35. It is not a proof of short-time existence or extension, and it does not decide Yau Problem 26. The two unproved analytic interfaces (transported normalized tame estimates; shifted-$U$ base-pair extension with full $G$-term accounting) are correctly isolated, and even their completion would concern only the near-critical 4D negative Ishida–LeBrun setting, leaving the positive branch, general 4-manifold topology, $n\ge5$, dimension-only constants, and Lean formalization untouched.