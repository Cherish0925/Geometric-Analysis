# TTCS Independent Branch Record

```json
{
  "step_id": 37,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step37_continuation_theorem_and_first_exit.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A01/workspace/notes/step36_analytic_platform_and_global_Q.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Verify the shifted continuation theorem (Theorem 1.1) and first-exit closure (Section 3) in the Step 37 note. The central claim is: if sup|U| = sup|chi^2(Rm+G)| is bounded on [tau, T_max) for some tau > 0, then the smooth degenerate flow dt g = -2 chi^2(Ric+g) extends past T_max. The proof adapts Wang's staggered induction (Lemma 4.10, Remark 4.2) to the normalized shifted variable. Check specifically:

1. L^p(Rm) propagation (Lemma 1.2): Is the reaction term correctly bounded by (K+C) int|Rm|^p using a|Rm|^{p+1} <= |aRm||Rm|^p <= (|U|+C)|Rm|^p? Does the signed IBP (0.4) correctly absorb the Hessian-a term into the degenerate diffusion int a|nabla Rm|^2|Rm|^{p-2}? Are there any terms where the degenerate weight 'a' in the diffusion is insufficient to absorb the cutoff terms?

2. Staggered induction: Does the Wang triple (nabla^m U, nabla^{m-1} Rm, nabla^m chi) correctly generalize to the normalized equation? At level m=1, does the base-pair Y_1 Gronwall use L^p(Rm) from level 0? At higher levels, does the signed IBP handle all chi nabla^2 chi * nabla^m U terms, and does the top-jet integration by parts correctly reduce nabla^{m+2} chi to the current-level coupled pair?

3. First-exit closure (Section 3.2): The Moser endpoint ||aF(t)||_inf <= C gamma/t gives K(tau) = C gamma/tau < inf for tau > 0. Does the continuation theorem then extend the flow past T*? Does the energy self-improvement (K_2 Gronwall) and metric drift (delta theta^{2/3} r^2) correctly give strict improvement of (F1)-(F3)? Is the contradiction at T* logically complete?

4. Are there any hidden inputs not stated as hypotheses, any circularity between the continuation theorem and the first-exit quantities, or any terms in the staggered induction that require unweighted sup|Rm| (which would be circular)?

## Output

## Verification memo: Step 37 shifted continuation theorem and first‑exit closure

I checked the four items against the Step 37 note, the supporting Step 35/36 notes, the parallel A03 Step 38 note, and the Wang source (Lemmas 4.4–4.6, 4.10, Prop. 4.3, Rem. 4.2). Summary first, then item‑by‑item substance.

**Bottom line.** The Level‑0 propagation (Lemma 1.2) and the base‑pair (Level 1) are structurally correct and faithfully adapt Wang's degenerate‑flow mechanism, with one genuinely valuable feature: the whole induction is engineered around $U$‑derivatives plus cutoff jets and never needs unweighted $\sup|\mathrm{Rm}|$, so there is no circularity at the point where one would most expect it. The first‑exit logic (§3.2) is non‑circular and its contradiction structure is complete **conditional on Theorem 1.1 being a theorem and on the Moser endpoints**. The two places where the argument is asserted rather than established are (i) the Level‑$m\ge2$ induction inside Theorem 1.1, and (ii) the per‑datum short‑time existence input; both are exactly the points the companion notes (A03 Step 38 §3, Step 36 §1) already isolate as not yet written. This makes Theorem 3.1's statement in §3.3 that the principle is "not a conditional theorem with unverified external hypotheses" stronger than what the supporting material supports.

---

### 1. $L^p(\mathrm{Rm})$ propagation (Lemma 1.2) — sound

The reaction bound is correct. $U=a\mathrm{Rm}+aG$ gives $a\mathrm{Rm}=U-aG$, so $|a\mathrm{Rm}|\le|U|+|aG|\le K+C$ with $a=\chi^2\le1$, $|G|\le C$. Testing the quadratic $a(\mathrm{Rm}*\mathrm{Rm})$ against $|\mathrm{Rm}|^{p-2}\mathrm{Rm}$ yields $\int a|\mathrm{Rm}|^{p+1}=\int(a|\mathrm{Rm}|)|\mathrm{Rm}|^{p}\le(K+C)\int|\mathrm{Rm}|^{p}$ (1.6). This is the exact analog of Wang 4.10, where $|\chi^2\mathrm{Rm}|_\infty$ controls the reaction; here the finite quantity is $\sup|U|$, which is the stated hypothesis. Correct, and — importantly — only $\sup|a\mathrm{Rm}|$ is used, never $\sup|\mathrm{Rm}|$.

The degenerate diffusion absorbs all cutoff terms. The decisive structural fact is that every error term needing the diffusion carries the weight $a$:
- gradient term (1.7): $|da||\nabla\mathrm{Rm}||\mathrm{Rm}|^{p-1}=(|da|/\sqrt a)(\sqrt a|\nabla\mathrm{Rm}||\mathrm{Rm}|^{(p-2)/2})|\mathrm{Rm}|^{p/2}$, and $|da|^2/a=4|\nabla\chi|^2\le Cr^{-2}$ is finite where $\chi>0$ and the integrand vanishes where $\chi=0$. Young gives $\varepsilon\int a|\nabla\mathrm{Rm}|^2|\mathrm{Rm}|^{p-2}+Cr^{-2}\int|\mathrm{Rm}|^p$. Correct.
- Hessian term (1.8): here I verified the key decomposition $\nabla^2 a=2\chi\nabla^2\chi+2\nabla\chi\otimes\nabla\chi$. The second piece is bounded ($|\nabla\chi|^2$) and gives $C\|d\chi\|_\infty^2\int|\mathrm{Rm}|^p$ directly; the first piece is genuinely of the signed form (0.3) with a single $\chi$, so (0.4) applies. The IBP in the signed lemma uses $|\chi||d\chi||V|^{p-1}|\nabla V|$ and Young, **not** division by $a$ — this is the corrected form, and Step 37 uses it correctly (unlike the earlier draft flagged in A03 Step 38 §0(2)).

Thus the degenerate weight is sufficient everywhere: no cutoff term is left needing a non‑degenerate Laplacian. (1.10) and the Gronwall on the finite interval $[\tau,T_{\max})$ are valid. Minor bookkeeping: (1.2) writes the drift bound with $2K(\tau)$, but the correct pointwise bound is $|aE|=|a\mathrm{Ric}+ag|\le C(K+C)$, not $|U|$; harmless, since the constant stays finite.

### 2. Staggered induction — correct at Levels 0–1, asserted at $m\ge2$

The variable substitution $\chi^2\mathrm{Rm}\mapsto U$ is legitimate: since $\nabla G=0$, $\nabla^m U=\nabla^m(\chi^2\mathrm{Rm})+\nabla^m(\chi^2)\,G$, so controlling $\nabla^m U$ and the cutoff jets $\nabla^m\chi$ is equivalent to controlling $\nabla^m(\chi^2\mathrm{Rm})$. The connection variation (1.11), $\partial_t\Gamma=-g^{-1}*\nabla\mathrm{Ric}(U)$, and hence (1.12) $\partial_t\nabla^2\chi=g^{-1}*\nabla U*\nabla\chi$, are correct because $\chi$ is fixed as a function while $\nabla^2\chi$ moves through $\Gamma$. The base pair $Y_1$ (1.16) correctly draws its inhomogeneity $\|\mathrm{Rm}\|_{p'}$ from Level 0. This is faithful to Wang's three‑way interlock (Rem. 4.2), and the driver of the cutoff‑jet equation (1.19) is correctly $\nabla^k\mathrm{Ric}(U)$ with $|\nabla^k\mathrm{Ric}(U)|\le C|\nabla^k U|$.

The Level‑$m\ge2$ step is where the note asserts more than it shows. The four top allocations $\Gamma_1$–$\Gamma_4$ (1.18) are the right list, and $\Gamma_4$ (with $\nabla^{m+1}U$) is correctly absorbed by diffusion. The trouble is the descendants of $\Gamma_1$ and $\Gamma_3$ after IBP off the top jet. Take $\Gamma_1=\chi\nabla^{m+2}\chi*U$ tested against $|\nabla^mU|^{p-2}\nabla^mU$; IBP produces, among others, a term $\int\chi\nabla^{m+1}U\,|\nabla^mU|^{p-2}\,\nabla^{m+1}\chi*U$. Young against the diffusion leaves $C_\varepsilon\int|\nabla^{m+1}\chi|^2|U|^2|\nabla^mU|^{p-2}$ — the top cutoff jet **squared** coupled to the current curvature power. Whether this closes into $Y_m$ depends on the exact Hölder exponents at that level, and, as A03 Step 38 §3 spells out for the $\Gamma_3$ descendant $\chi\nabla^{m+1}\chi*\nabla U*|\nabla^mU|^{p-2}\nabla^mU$, some IBP branches ("if it falls on metric contractions or commutators") leak **unweighted lower $T$‑derivatives** that are only controlled if one simultaneously runs the parallel unweighted $\nabla^m\mathrm{Rm}$ induction (Wang's Prop. 4.13 interlocked with Prop. 4.14). The Step 37 note's phrase "$\Gamma_2$ and $\Gamma_3$ are paid by the coupled cutoff‑jet equation" and the resulting clean Gronwall (1.21) $Y_m'\le C(Y_m+C_{m-1})+C$ presuppose exactly the finite‑exponent schedule that A03 Step 38 §3 states is not yet written ("Step 27 cannot be cited as already proving that induction"). Because Theorem 1.1's extension needs bounds at **all** $m$, this open point is load‑bearing for the theorem, not decorative. The mechanism is the correct one; the exponent‑by‑exponent verification is the missing substance.

A separate framing point in Step D: the note concludes it "controls $\nabla^m\mathrm{Rm}$ on any open set where $a\ge a_0>0$." That is the weaker and slightly misleading reading. Solving $\nabla^m T=a^{-1}[\nabla^mU-\sum_{j\ge1}\binom mj\nabla^j a\,\nabla^{m-j}T]$ requires dividing by $a$ and says nothing in the transition region $0<a<a_0$, where $|\mathrm{Rm}|\le a^{-1}(K+C)$ can be large. The correct input for extension is control of $\nabla^m(\partial_t g)$: since $\partial_t g=-2aE=-2\mathrm{Ric}(U)+(\text{lower, bounded})$, controlling $\nabla^mU$ + cutoff jets controls $\nabla^m(\partial_t g)$ **globally**, which is what makes the metric extend smoothly. This is exactly the quantity Wang Prop. 4.3 uses ($\nabla^m(\chi^2\mathrm{Rm})$, not $\nabla^m\mathrm{Rm}$). Two consequences: (a) the note's Step D wording should be replaced by the $\partial_t g$/$U$‑derivative statement, which is both correct and stronger; (b) the invocation of "Wang Proposition 4.3" is for the **un‑normalized** flow with quantity $\chi^2\mathrm{Rm}$; the normalized shifted analog (extra $+g$ and $-2ag$ terms) is cited but not re‑derived. Those terms are algebraic, bounded, and smooth, so the extension principle plausibly survives, but this adaptation is currently unstated.

### 3. First‑exit closure (§3.2) — logic complete, conditional on §1–§2 inputs

The continuity/bootstrap structure is correct and I find no circularity within it. On $[0,T^*)$ the flow is smooth and (F1)–(F3) hold by the definition of $T^*$; the conditional Moser endpoints then give $\|aF\|_\infty\le C\gamma/t$, hence $|U|\le\|aF\|_\infty+C\le C\gamma/t+C$ (the bound $|U|\le aF+C$ is correct since $F\ge|\mathrm{Rm}|$), so $K(\tau)\le C\gamma/\tau+C<\infty$ for each $\tau>0$ (3.3). Theorem 1.1 then extends past $T^*$. The self‑improvements are dimensionally and quantitatively consistent: (F1) via $K_2(T^*)\le e^{Cr^{-2}t}K_2(0)\le e^{C\theta}K_2(0)<2K_2(0)$ for small $\theta$ (using $r^{-2}t\le\theta$); (F3)/(F2) via the metric‑drift integral, which I recomputed: $\int_0^{\theta r^2}C\delta(r^2/t)^{1/3}dt=\tfrac32 C\delta\theta^{2/3}r^2$, matching (3.5). Strict improvement of all three, plus smooth extension past $T^*$, contradicts $T^*<\theta r^2$. The contradiction is logically closed.

One hidden normalization sits inside (3.5): the drift bound $\tfrac32C\delta\theta^{2/3}r^2<\Lambda_*/2$ requires $r\lesssim1$ (equivalently the fixed‑scale normalization behind $E=\mathrm{Ric}+g$, which pins the target Einstein constant to $-1$). Step 36 §3 already flags that the compact $Cr^{-2}$ form "is available only after fixing a scale normalization such as $r\le1$." For the intended fixed‑radius application this is harmless, but since §4 applies Theorem 3.1 along a near‑critical collapsing family ($\delta_i\to0$, $A_i\to\infty$), the $r$‑regime must be pinned explicitly; otherwise the $r^2$ factor is not obviously small. This should appear as a stated condition of Theorem 3.1, not only inside Step 36.

### 4. Hidden inputs, circularity, and unweighted $\sup|\mathrm{Rm}|$

- **No unweighted‑$\sup|\mathrm{Rm}|$ circularity.** I checked each level: Level‑0 reaction uses $\sup|a\mathrm{Rm}|=\sup|U-aG|$; Lemma 1.2 outputs only $\|\mathrm{Rm}\|_{L^p}$ (integral); higher levels use $\|\nabla^kU\|_p,\|\nabla^k\chi\|_p$ and Sobolev on $U$‑derivatives ($p>4$) to reach $\sup|\nabla^mU|$. Unweighted pointwise curvature is never invoked. This is a real design strength and is the correct way to run a degenerate‑flow continuation.
- **No circularity between continuation and first‑exit quantities.** The Moser endpoints depend only on the a‑priori (F1)–(F3) that hold on $[0,T^*)$ by definition, and Theorem 1.1 depends only on $\sup|U|$ furnished by those endpoints. The two feed forward, not in a loop.
- **Genuine unproven inputs.** (i) Layer A: per‑datum transported‑DeTurck short‑time existence for the normalized system is formulated in Step 36 §1 but not proved; Step 36 §1.1–1.2 states plainly that ordinary strictly‑parabolic Schauder constants do not deliver the required $\varepsilon$‑uniform smooth limit, and Yang‑type degenerate/tame energy estimates are needed. (ii) Layer B beyond the base pair: the $m\ge2$ induction of item 2. Therefore Step 37 §3.3's statement that layers A and B are "per‑datum consequences of the flow equation itself" and that the assembled principle is "not a conditional theorem with unverified external hypotheses" overstates the established content: Layer A is precisely an unverified input, and Layer B's higher‑order induction is open. The candid status is the one A03 Step 38 §4–§6 records — a conditional smoothing mechanism resting on a smooth first‑exit interval, existence, and the written higher induction.

### Supporting‑note checks (used by §1)

I verified the two derivative structures Step 37 imports. Step 35 (6.4) $|\nabla B_{\rm def}|\le Cs^{1/2}|\nabla E|$ is correct: with $B_{\rm def}=|E|^2g+\tau E-2E^2$ and $\tau=\mathrm{tr}\,E$, every term is $\le Cs^{1/2}|\nabla E|$ because $|\tau|\le C|E|=Cs^{1/2}$ and $|\nabla\tau|=|\mathrm{tr}\,\nabla E|\le C|\nabla E|$; the removal of the spurious $+C|\nabla E|$ is justified (the trace is not an independent $O(1)$ quantity). Step 35 (3.6) $|\nabla B_{\rm curv}|\le CF|\nabla\mathrm{Rm}|$ is likewise correct, with $F$ replacing $s^{1/2}$ because curvature has no analogous vanishing. The scaling test (§1, $\int|R|^2$ rate $=4-4=0$ in dimension 4 under $\partial_t g=-2g$) is a correct consistency check that the $+g$ normalization introduces no spurious pointwise damping. These do support the seed $J_6\le C\delta^6V$ and hence the defect Moser endpoint used in §3.2.

---

### What would make Theorem 1.1 a completed theorem

The concrete substance still to be written, in decreasing order of how much it changes the status:
1. The finite‑exponent induction schedule for $m\ge2$: carry Wang's interlocked double induction (unweighted $\|\nabla^m\mathrm{Rm}\|_p$ à la Prop. 4.13 together with $\|\nabla^mU\|_p$, $\|\nabla^{m+1}\chi\|_p$), tracking each Hölder exponent, and show explicitly that the $\Gamma_1$/$\Gamma_3$ descendants (top jet coupled to differentiated curvature; commutator‑generated unweighted lower $T$‑derivatives) close into $Y_m$ plus strictly lower levels plus diffusion. The single‑Hessian $\chi\nabla^2\chi*\nabla^mU$ terms are already handled by (0.4); the untreated part is the top‑jet/differentiated‑curvature coupling.
2. Re‑derivation of Wang Prop. 4.3 for the normalized shifted flow, phrased as: uniform bounds on $\{\nabla^mU\}$ and $\{\nabla^m\chi\}$ (equivalently $\nabla^m(\partial_t g)$) imply smooth extension — replacing the imprecise "$\nabla^m\mathrm{Rm}$ on $\{a\ge a_0\}$" wording in Step D and confirming the $+g$/$-2ag$ terms do not disturb the extension argument.
3. The Layer‑A existence theorem (transported‑coefficient DeTurck with Yang‑type degenerate energy estimates), currently only formulated.
4. Making the $r\lesssim1$ normalization an explicit condition of Theorem 3.1 and reconciling it with the collapsing‑sequence application in §4.

Items 1–2 are internal to the continuation argument and are the difference between "strong plausibility transcription of Wang" and "proved theorem." Items 3–4 are inputs the note itself elsewhere marks as pending; §3.3's self‑contained phrasing is the one statement in the note that runs ahead of the supporting material.