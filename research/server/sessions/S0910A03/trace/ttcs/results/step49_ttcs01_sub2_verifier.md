# TTCS Independent Branch Record

```json
{
  "step_id": 49,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step49_normalized_flow_existence_and_extension.md",
    "Sessions/S0910A03/workspace/notes/step49_corrected_restricted_theorem_statement.md",
    "Sessions/S0910A03/workspace/notes/step47_consolidated_negative_IL_gap_theorem.md"
  ]
}
```

## Task

Verify the mathematical correctness of the normalized cutoff Ricci flow existence and extension theorem in step49_normalized_flow_existence_and_extension.md. The flow equation is ∂_t g = -2χ²(Ric(g) + g), which differs from Yang's equation ∂_t g = -2χ²Ric by the zeroth-order term -2χ²g. The note claims:

1. The extra Christoffel variation from h = -2bg is -(δ^k_j ∂_i b + δ^k_i ∂_j b - g_ij ∇^k b) using ∇g=0. The curvature variation is -2bRm - g∧∇²b (Kulkarni-Nomizu product). Verify these formulas.

2. In the L^p energy evolution, the extra terms contribute: a dissipative -2p∫b|Rm|^p (favorable) and a source bounded by Cp·||∇²a||_∞·(∫|Rm|^p + Vol). The Grönwall coefficient is therefore ε-independent since ∇^k b_ε = ∇^k a for k≥1. Verify this is correct.

3. The coefficient-regularized existence (b_ε = χ²+ε² with ε>0) gives uniformly parabolic equations, and the ε-independent energy bounds give a common existence time T₀. The ε→0 passage uses interior C^k estimates on {χ>0}, vanishing drift on {χ=0}, and weighted estimates for regularity at ∂supp(χ). Verify this argument.

4. The extension criterion: bounded |χ²Rm| on [0,T*) implies smooth extension past T*, by adapting Wang's staggered induction. The normalization adds bounded lower-order terms at each level. Verify compatibility with Wang's framework.

5. The positive-time slab argument: if T* is a finite maximal time, the Moser endpoint |χ²Rm| ≤ Cγ/t is finite on [T*/2,T*), giving bounded |χ²Rm| there, so the extension criterion applies — contradiction. This resolves the issue that γ/t diverges at t=0 without needing a uniform bound on [0,T]. Verify this argument is sound.

Check for hidden assumptions, circular reasoning, or gaps. The note explicitly does NOT claim uniqueness, sequence-uniform estimates, or any result about Yau Problem 26.

## Output

## Verification memo: normalized cutoff flow existence and extension (step49)

I checked the five requested items by direct computation where possible and by structural analysis where the argument leans on external citations. The core algebra of the normalization perturbation is correct, one source term carries a sign that disagrees with the standard convention (immaterial to every downstream estimate), the energy structure is right, and the two logical devices (ε→0 passage and the positive-time slab) are architecturally sound but rest on inputs that are either external (Yang, Wang) or marked incomplete in the companion notes. Three concrete places in §4 are written in a form that does not follow from the stated bounds. Details below.

### 1. Christoffel and curvature variation (formulas 1.1–1.3)

**Christoffel (1.1): correct.** With $\partial_t g_{ij}=h_{ij}=-2bg_{ij}$ and $\nabla g=0$,
$$\partial_t\Gamma^k_{ij}=\tfrac12 g^{k\ell}(\nabla_i h_{j\ell}+\nabla_j h_{i\ell}-\nabla_\ell h_{ij})=-(\delta^k_j b_i+\delta^k_i b_j-g_{ij}b^k),\quad b_i=\partial_i b,$$
matching (1.1) exactly.

**Curvature reaction $-2b\,\mathrm{Rm}$: correct.** The $-2b\,R_{klij}$ piece is the metric-variation contribution $(\partial_t g_{mk})R^m{}_{lij}=-2bR_{klij}$; this is unambiguous.

**Curvature source: sign disagreement.** Using $\partial_t R^k{}_{lij}=\nabla_i(\partial_t\Gamma^k_{jl})-\nabla_j(\partial_t\Gamma^k_{il})$ with (1.1) and $H_{ij}=\nabla_i\nabla_j b$, I get
$$\partial_t R^k{}_{lij}\big|_N=\delta^k_i H_{jl}-\delta^k_j H_{il}+g_{jl}H_i{}^k-g_{il}H_j{}^k,$$
and after lowering $k$ and adding the metric-variation term,
$$\partial_t R_{klij}\big|_N=-2b\,R_{klij}+\big(g_{ki}H_{lj}+g_{lj}H_{ki}-g_{kj}H_{li}-g_{li}H_{kj}\big)=-2b\,\mathrm{Rm}+g\owedge\nabla^2 b.$$
I verified this two independent ways: (i) the direct connection computation above, and (ii) the trace, which must reproduce the linearized conformal Ricci formula. Contracting my Riemann result gives $\partial_t\mathrm{Ric}_{lj}|_N=(n-2)H_{lj}+(\Delta b)g_{lj}$, which is exactly the linearization of $\widetilde{\mathrm{Ric}}$ under $\tilde g=e^{2f}g$ at $\dot f=-b$. Both routes give the source with a **plus** sign, $+g\owedge\nabla^2 b$. The note's (1.2)/(1.3) write it with a **minus**. This is a convention-entangled sign slip (or an opposite Kulkarni–Nomizu convention that is not the one their traced formulas use).

**Effect on the argument: none.** Every subsequent use of this term (energy estimates §2, weighted evolution §3, extension §5) invokes only the pointwise magnitude bound $|g\owedge\nabla^2 b|\le C\|\nabla^2 a\|_\infty$, which is sign-blind. The dissipative $-2b|\mathrm{Rm}|^p$ term comes from the $-2b\,\mathrm{Rm}$ reaction, whose sign is correct. So the sign should be repaired in the written formula but changes no estimate.

### 2. $L^p$ energy evolution (§2.2)

The three contributions are computed correctly:
- Reaction: $p\int|\mathrm{Rm}|^{p-2}\langle\mathrm{Rm},-2b\,\mathrm{Rm}\rangle=-2p\int b|\mathrm{Rm}|^p\le0$. Correct and dissipative.
- Source: $\le Cp\|\nabla^2 a\|_\infty\int|\mathrm{Rm}|^{p-1}\le Cp\|\nabla^2 a\|_\infty(E_p+\mathrm{Vol})$ by Young. Correct.
- Volume form: $\partial_t\,d\mu|_N=\tfrac12\mathrm{tr}_g(-2bg)\,d\mu=-nb\,d\mu\le0$. Correct.

The metric-variation-in-the-norm term is understated: $|\mathrm{Rm}|^2$ carries four inverse-metric factors, each giving $+2b$, so $\partial_t|\mathrm{Rm}|^p|_{\text{norm}}=4p\,b|\mathrm{Rm}|^p$, i.e. $\le C n p\,|\mathrm{Rm}|^p$, not $Cn|\mathrm{Rm}|^p$ as written. The missing $p$ is harmless because the note states the Grönwall coefficient is polynomial in $p$ anyway, and this term is favorable to keep bounded.

**ε-independence: correct and the key point.** Because $b_\varepsilon=\chi^2+\varepsilon^2$ with $\varepsilon$ constant, $\nabla^k b_\varepsilon=\nabla^k(\chi^2)$ for $k\ge1$ and $\partial_t b_\varepsilon=0$. The source depends only on $\nabla^2 a$; the reaction coefficient $b_\varepsilon\in[0,1+\varepsilon^2]\le2$ is uniformly bounded and its favorable terms are dropped for the upper bound. Hence the added Grönwall coefficient $C(n,p,\chi)$ is genuinely ε-free. This is verified.

### 3. Coefficient-regularized existence and ε→0 passage (§4)

The overall architecture is the correct route for a degenerate flow: regularize to strict parabolicity, obtain ε-uniform energy, pass to the limit. Three written steps do not follow from the stated bounds and need repair.

**(a) The drift integral (4.4) diverges as written.** With the Moser endpoint $\|b_\varepsilon\mathrm{Rm}_\varepsilon\|_\infty\le C\mathcal C_S/t$, one has $b_\varepsilon|\mathrm{Ric}_\varepsilon|\le C/t$, so
$$|g_\varepsilon(t)-g_0|\le 2\int_0^t\big(C\mathcal C_S/s+n+1\big)\,ds$$
has a divergent $\int_0^t ds/s$. The subsequent "$\le C\sqrt t$" and "logarithmic $t$-integral" phrasings are mutually inconsistent and neither follows from (4.4). The correct near-$t=0$ control must use the smooth initial data: $b_\varepsilon|\mathrm{Ric}_\varepsilon(s)|\le C_0$ (ε-uniform from continuity of $\mathrm{Rm}$ at $s=0$) for small $s$, giving drift $\le C_0 t\to0$. Splitting $\int_0^t\min(C_0,C\mathcal C_S/s)\,ds$ is finite and $\to0$. The conclusion (metric equivalence for small $t$, $C^0$ initial continuity) is true; the written estimate is not.

**(b) The zero-set claim "$|g_\varepsilon(t)-g_0|\le C\varepsilon^2$ on $\{\chi=0\}$" is not derived.** On $\{\chi=0\}$, $b_\varepsilon=\varepsilon^2$, and the Moser endpoint gives $\varepsilon^2|\mathrm{Ric}_\varepsilon|\le C/t$ — the $\varepsilon^2$ is already consumed by the endpoint, so $\int_0^t 2\varepsilon^2|\mathrm{Ric}_\varepsilon|\,ds\le\int_0^t 2C/s\,ds$, which is $O(1)$ at best (divergent as stated) and carries **no** $\varepsilon^2$ smallness. To obtain $O(\varepsilon^2)$ one needs an ε-uniform bound $|\mathrm{Ric}_\varepsilon|\le C_0$ on the zero set over the whole interval, then $\int 2\varepsilon^2 C_0\,ds=O(\varepsilon^2)$. That ε-uniform curvature bound on $\{\chi=0\}$ is plausible (the metric is nearly static there) but is not established; near $\partial\mathrm{supp}(\chi)$ the second derivatives feel the fast evolution in $\{\chi>0\}$, so it is not automatic. The limit statement $g(t)=g_0$ on $\{\chi=0\}$ is believable but presently rests on an unproved ε-uniform curvature bound rather than the stated $\varepsilon^2$ multiplication.

**(c) Regularity of the limit across the interface $\{\chi>0\}\!\to\!\{\chi=0\}$ is asserted.** The step "$\nabla^m(a\,\mathrm{Rm}_g)\in L^p$ for all $m,p$, combined with $g=g_0$ on $\{a=0\}$, gives $g(t)\in C^\infty(M)$" is the genuinely hard part of degenerate flows and is stated rather than proved. Smoothness of the weighted quantity $a\,\mathrm{Rm}$ does not directly yield smoothness of $\mathrm{Rm}$ where $a\to0$ (this is a division-by-$a$ issue), and the matching of interior derivatives from $\{\chi>0\}$ to the frozen data on $\{\chi=0\}$ across the interface is exactly where a degenerate flow can lose regularity. This gap recurs in §5.

Beyond these, the interior part (Schauder on $K_k=\{\chi\ge1/k\}$ with parabolicity $\eta=\inf_K\chi^2>0$, Arzelà–Ascoli, diagonal subsequence) is standard and correct for positive times.

**External dependence.** The ε-uniform existence time (4.2) and Moser endpoint (4.3) are "Yang Thm 9.2 (adapted)." Whether Yang 1992 in fact supplies short-time existence and the smoothing endpoint for the degenerate flow $\partial_t g=-2\chi^2\mathrm{Ric}$ with ε-uniform constants is the load-bearing input for the entire existence statement and cannot be verified from the material here. The normalization increments to those bounds are ε-free (item 2), but the base degenerate theory is taken on citation.

### 4. Extension result (§5) and Wang compatibility

The step sequence is the standard Shi/Wang continuation and the normalization additions are genuinely lower order:
- Metric equivalence from $|\chi^2\mathrm{Rm}|\le K$: the flow speed is $\chi^2|\mathrm{Ric}+g|\le c\chi^2|\mathrm{Rm}|+n\chi^2\le cK+n$, so drift over $[0,T^*)$ is bounded. Correct (the note's step-1 phrasing bounding $|\mathrm{Ric}|$ only on $\{\chi\ge\varepsilon_0\}$ is sufficient because the extra factor is $\chi^2$).
- The quadratic reaction in the $L^p$ curvature evolution is controlled precisely because $b\,\mathrm{Rm}=\chi^2\mathrm{Rm}$ is bounded by $K$, exactly Wang's mechanism.
- The staggered hierarchy $\nabla^m(\chi^2\mathrm{Rm})\to\nabla^{m+1}\chi\to\nabla^m\mathrm{Rm}$ receives, from the normalization, a current-level reaction $-2b\nabla^m\mathrm{Rm}$ (bounded coefficient) and a source $\nabla^m(g\owedge\nabla^2 a)$ built from fixed smooth functions plus cutoff-jet corrections (3.4) at previous levels. These fit the same algebraic pattern; §3 classifies them correctly.

Compatibility with Wang's framework is coherent as an adaptation. Two reservations: (i) Wang's Theorem 4.1 and Lemmas 4.4–4.13 for the degenerate flow are external and unverifiable here; (ii) the smooth extension "on $M$" again passes through the interface regularity of item 3(c) — on $\{\chi=0\}$ the exact flow is static so $g(T^*)=g_0$ is smooth there, and on $\{\chi>0\}$ Shi applies, but the joining across $\partial\mathrm{supp}(\chi)$ is the same soft spot. The staggered induction is the tool intended to close this, but the companion notes (step49_corrected §6.1, step47 §6) mark the arbitrary-order induction with all constants as "structurally classified but not carried through." So the extension result is complete modulo that induction and the interface regularity, both currently open.

### 5. Positive-time slab argument (§6)

**Internally sound.** If the exact flow has finite maximal time $T^*$, the extension result forces $\limsup_{t\to T^*}\|\chi^2\mathrm{Rm}\|_\infty=\infty$. On the slab $[T^*/2,T^*)$ (with $T^*\le T=\theta r^2$) the endpoint (6.1) gives $|\chi^2\mathrm{Rm}|\le C\gamma/t\le 2C\gamma/T^*<\infty$. Combined with the automatic bound on the compact initial piece $[0,T^*/2]$ (where the flow is smooth by maximality), $\|\chi^2\mathrm{Rm}\|_\infty$ is uniformly bounded on all of $[0,T^*)$, so the extension result applies and contradicts maximality. The logic that only $t$ near $T^*>0$ matters, so the $t\to0$ divergence of $\gamma/t$ is irrelevant, is correct and clean. This is the right way to use a smoothing estimate that blows up at the initial time.

**No circularity in the continuation itself.** The endpoint (6.1) is an a-priori estimate valid on whatever existence interval the flow occupies (it is a first-exit estimate, conditional on existence and on the exit conditions holding). Using it on $(0,T^*)\subset(0,\tau)$ to prove extension past $T^*$ is the standard continuation-by-a-priori-estimate method, not circular.

**Conditional input.** The soundness of the slab step is entirely inherited from the endpoint (6.1), i.e. from the first-exit bootstrap of the companion Steps 35–47 applied to the exact $\varepsilon=0$ flow. The notes themselves record that bootstrap as not fully closed (step47 §6, step49_corrected §6: the sequence-uniform observation time and the arbitrary-order localized $K_2/J_m/Q$ estimates on the exact flow are "structurally clear but require the complete staggered estimates to be formally closed"). So the slab argument is a valid conditional deduction whose premise is presently unestablished at full rigor.

### Hidden assumptions, circularity, and open points

- **Two external theorems carry the existence and extension backbone:** Yang 1992 (degenerate short-time existence + smoothing endpoint, ε-uniform constants) and Wang 2015 (extension under bounded $\chi^2\mathrm{Rm}$). Neither is verifiable from the supplied files; the note is explicit about invoking them.
- **Interface regularity across $\partial\mathrm{supp}(\chi)$** is the single recurring unproved point, appearing in the ε→0 limit (§4.4), the zero-set drift, and the smooth extension of §5. It is the characteristic difficulty of degenerate parabolic flows and is currently asserted via weighted $L^p$ bounds without the division-by-$a$ / matching argument being completed.
- **The slab argument depends on the first-exit endpoint**, which the companion material marks incomplete; the argument's own logic is valid.
- The sign of the Kulkarni–Nomizu source in (1.2)/(1.3) should be corrected to $+g\owedge\nabla^2 b$; this does not touch any estimate.
- The note's disclaimers (no uniqueness, no sequence-uniform estimates, nothing about Yau 26, no positive branch, no $n\ge5$, no Lean) are consistent with what is actually supported.

**What would make items 3–5 fully solid, concretely:** (i) an ε-uniform short-time curvature bound near $t=0$ and on $\{\chi=0\}$, replacing the divergent (4.4) and the unjustified $O(\varepsilon^2)$; (ii) a completed regularity argument for $\mathrm{Rm}_g$ (not just $a\,\mathrm{Rm}_g$) across $\partial\mathrm{supp}(\chi)$, or a demonstration that the frozen-collar structure makes the interface smooth; (iii) the arbitrary-order staggered induction with explicit constants, which both §5 and the slab premise require. Items 1 and 2 are verified as stated (modulo the noted sign and the $p$-power bookkeeping).