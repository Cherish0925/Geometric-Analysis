# TTCS Independent Branch Record

```json
{
  "step_id": 19,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step18_simultaneous_bootstrap_and_fixed_p_defect.md",
    "Sessions/S0910A03/workspace/notes/step17_normalized_cutoff_flow_theorem.md",
    "Sessions/S0910A03/workspace/scripts/verify_step19_volume_independent_beta.py",
    "Sessions/S0910A03/workspace/scripts/verify_step19_p4_threshold_and_bernstein.py",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md"
  ]
}
```

## Task

Verify the proposed first-exit closure for the 4D normalized cutoff flow. The claim is that Wang's Theorem 6.3 can be localized to a finite-neighbor system of balls on a closed 4-manifold under the normalized cutoff flow ∂_tg = -2χ²(Ric+g), yielding the volume-independent curvature decay |χ²Rm| ≤ C√ε/t.

Specific points to check:

1. VOLUME-INDEPENDENT BETA: On a ball B_r with Ric ≥ -3g, the relative Sobolev constant is A ~ C·r·V^{-1/4}. The maximal-function selection gives ∫_{B_r}|Rm|² ≤ K₀·V. Therefore β = A²·||Rm||_{L²} = C²r²V^{-1/2}·√(K₀V) = C²r²√K₀. With the Li radius r_* = (ε/K₀)^{1/4}, this gives β = C²√ε. Does this volume cancellation hold exactly in 4D? Does it fail in other dimensions?

2. LOCALIZATION OF WANG/YANG: Wang's proof (Theorem 6.3, see context_files) uses a global Sobolev inequality and global L^{n/2} curvature energy. The localized version replaces these with relative Sobolev on each ball and local energies R_α per ball. The Moser iteration (Li Theorem 2.5) runs on each individual ball B_r(x) with nested sub-balls. The energy persistence comes from the coupled L² system dH_α/dt ≤ Cr^{-2}Σ_{β~α}H_β. Does this localization introduce any new terms or require additional hypotheses beyond the coupled energy control?

3. NORMALIZED FLOW CORRECTION: Under ∂_tg = -2χ²(Ric+g) = -2χ²Ric - 2χ²g, the curvature evolution gains additional terms from h₂ = -2χ²g. These are ∂_tRm|_{h₂} ~ Hess(χ²)·g + χ²·Rm (from the metric variation formula). In the L^{n/2} energy equation, these contribute O(r^{-2})∫|Rm|^{n/2} (lower order) and ∫χ²|Rm|^{n/2} (absorbed). Is this correct? Are there any higher-order terms from the normalization that could affect the Moser absorption?

4. FIRST-EXIT CLOSURE LOGIC: Given β small → |χ²Rm|≤Cβ/t → curvature potential for Li → |χ²E|≤C_pδ(r²/t)^{2/p} → weighted Bernstein |χ∇(χ²E)|≤C_pδt^{-1/2}(r²/t)^{2/p} → for p>4: metric drift O(δθ^{1-2/p}r²), connection drift O(δθ^{1/2-2/p}), Hessian drift O(δθ^{1/2-2/p}/r) → all provisional first-exit bounds improved for small δ. Is there any circular dependency? Does the Bernstein estimate actually follow from the weighted parabolic structure?

## Output

## Verification memo: first-exit closure for the 4D normalized cutoff flow

I checked the four points against the two source papers (Wang, arXiv:0903.2913, "Pseudolocality…"; Li, arXiv:0911.3104, "Smoothing…II") and the internal derivations in the Step 17/18 notes and the two Step 19 scripts. The arithmetic in the scripts is correct where it is arithmetic; the load-bearing analytic statements are assumed, not derived. Details below.

---

### Point 1 — Volume cancellation of β

**The algebra is correct, and it holds in every dimension, not only n = 4.** Write Wang's Sobolev constant in his normalization $\|f\|_{2n/(n-2)}\le A_0\|\nabla f\|_2$ (Wang Prop. 3.12, Thm 6.3 assumption 1). This $A_0$ is the *square root* of Li's Moser constant $A$ (Li uses $\|f\|_4^2\le A\|\nabla f\|_2^2$, so $A=A_0^2$). Gallot's relative estimate under $\mathrm{Ric}\ge-(n-1)Kg$ gives $A\sim r^2V^{-2/n}$, hence $A_0\sim rV^{-1/n}$, which is $rV^{-1/4}$ in n = 4. The note's "$A\sim rV^{-1/4}$" therefore refers to $A_0$, and is consistent with Wang. Then

$$\beta=A_0^2\|Rm\|_{L^{n/2}}=\big(rV^{-1/n}\big)^2\big(K_0V\big)^{2/n}=r^2K_0^{2/n},$$

with volume cancelling identically for **all** n (both scripts' n = 4 computation is the special case $2/n=1/2$). This is expected: $\beta$ is a scale- and volume-invariant dimensionless energy, so its volume-independence is a scaling fact, not a four-dimensional phenomenon.

Consequently the script's framing "crucial 4D volume cancellation" conflates a scaling identity with the genuinely four-dimensional inputs, which are elsewhere:
- $\bar K=V^{-1}\int|Rm|^2$ is bounded through Chern–Gauss–Bonnet ($\int|Rm|^2\le 8\pi^2\chi+\dots$), giving the uniform lower bound on the Li radius $r_*$. There is no such topological control of $\int|Rm|^{n/2}$ for $n\ge5$.
- Li's collapse-independent smoothing ($\|Rm\|_\infty\le C/t$ without a volume lower bound) rests on the Cheeger–Tian volume-ratio estimate $\frac{\mathrm{Vol}(B_r(\underline x))}{\mathrm{Vol}(B_r(x))}\int|Rm|^2\le C$, which uses Gauss–Bonnet–Chern and is, in Li's own words, "not known… to generalize to higher dimensions."

The relation $\beta=\sqrt\varepsilon$ then uses $r_*^4\bar K=\varepsilon_{\mathrm{Li}}$: $\beta=r_*^2K_0^{1/2}=(\varepsilon/\bar K)^{1/2}\bar K^{1/2}=\sqrt\varepsilon$. Correct. So the answer to "does it fail in other dimensions" is: the volume cancellation of $\beta$ does **not** fail; what is unavailable for $n\ge5$ is the topological energy bound and the collapse-independent smoothing theorem itself.

---

### Point 2 — Localization of Wang/Yang is not a restatement of either source

The two sources sit on opposite sides of the needed hybrid:

- **Li** proves a *local* Moser iteration (Thm 2.5, 3.4, Cor 3.5) for the **non-degenerate** global Ricci flow $\partial_t g=-2\,Ric$. The cutoff enters only as a test function $\phi$; the operator is $\partial_t-\Delta$ with a genuine (non-degenerate) Laplacian, and the finite-neighbor coupling is already handled by the covering $B_{2r}(x)\subset\cup_{i=1}^NB_r(y_i)$ with $e_0=\sup_x(\int_{B_r(x)}f^2)^{1/2}$ (Li, proof of Thm 3.4).
- **Wang** carries the degenerate weight $\chi^2$ inside the energy (Thm 6.3, Section 5, quantities $\int\chi^2|Rm|^{n/2}$) but the Moser iteration is **global** — global Sobolev on $M$, global $\|Rm\|_{n/2[M]}$, global $\|Ric\|_{p[M]}$.

The proposed object is neither: a **degenerate** operator $\partial_t-\chi^2\Delta$ (as in Wang) but with **per-ball relative Sobolev + finite-neighbor coupling** (as in Li). This introduces genuine additional requirements beyond the coupled $L^2$ control:

1. **Two independent cutoff scales.** The flow weight $a=\chi^2$ (degenerate coefficient) and the localization functions $\eta_\alpha$ (Moser test functions) are distinct; their cross terms $da*d\eta*w^p$ appear in Step 18 (8) and must be integrated by parts each level.
2. **Level-dependent neighbor coupling.** Li's covering constant reappears at every iteration exponent $p_k=p_0\nu^k$. Step 18 Section 4 correctly records that the reaction-to-dissipation coefficient scales like $p\sqrt{\varepsilon_*}$, so a fixed $\varepsilon_*$ cannot absorb all $p_k$. This is why the single-shot absorption cannot run to $p\to\infty$ and forces the two-stage strategy (fixed-$p_0$ spatial $L^p$ propagation, then curvature-as-potential — matching Li's Thm 2.5 which starts from a fixed $p_0>2$ and $\|u\|_{L^3}\lesssim t^{-1/3}$).
3. **The load-bearing input is the degenerate curvature-potential estimate**, Step 18 (13): $K_{3,\alpha}(t)=\int a|Rm|^3\le C/(A_\alpha^4t)$ under $\partial_t-a\Delta$ on the transition annulus. This is the local/degenerate analog of Li Thm 3.4 (or Wang Thm 6.3 conclusion 1) and is explicitly listed as open. It is exactly the implication "energy smallness $R_\alpha\le\varepsilon_*$ ⟹ weighted pointwise decay $|aRm|\le C/t$" that the whole chain needs.

So the localization does require additional hypotheses beyond the coupled $L^2$ energy: the finite-neighbor **degenerate** weighted Moser iteration and its curvature-potential estimate. The script's assertion in the "remaining verification" list — "the iteration is inherently local; coupling only through $L^2$ energy" — is true for Li's non-degenerate iteration but is precisely the point at issue for the degenerate transition region and the level-dependent coupling.

**Relevant concrete reality check from the sources.** Wang Section 2 (the Angenent–Knopf 4D neckpinch, his Prop. 2.4 / Claim 2.5) shows that assumptions 2 ($|Rm|_{n/2}$ small) and 3 ($|Ric|_p\le Kr^{n/p-2}$, $p>n/2$) **cannot be simultaneously weakened**: there is a 4D family with $|Rm|_{L^2}$ bounded but $|Ric|_{L^p}\to\infty$ (p>2) that becomes singular before a fixed time. The program controls the $L^2$ curvature energy $R_\alpha$, but this example demonstrates that curvature energy smallness alone does not produce the smoothing — the $L^p$ Ricci/defect bound (p>2) must be propagated independently. Step 18 (12) aims at exactly such a fixed-$p$ propagation for $aE$, so the program is aware; the example is a sharp indicator that this second bound is not optional and must survive along the flow.

---

### Point 3 — Normalization term $-2\chi^2 g$

The structural statement is essentially right, with one distinction worth making explicit.

Under $\partial_t g=-2\chi^2 g$ (the localized part of the normalization), $\delta\Gamma^k_{ij}=-(\partial_i\chi^2)\delta^k_j-(\partial_j\chi^2)\delta^k_i+g_{ij}\partial^k\chi^2=O(r^{-1})$ (Step 17 Section 6, correct — for a genuinely constant conformal shift $\delta\Gamma=0$ since $\nabla g=0$, but $\chi$ is not constant). The induced Riemann change is $O(r^{-2})$ from $\nabla^2\chi^2$. In the $|Rm|^{n/2}$ energy these fall into two groups:

- **Multiplicative:** $\chi^2|Rm|^{n/2}$-type terms, absorbed into a Gronwall factor $e^{Ct}$ over $t\le\theta r_*^2$. Correct.
- **Additive source:** the term $\nabla^2(\chi^2)*g$ does **not** vanish at $Rm=0$; it is a genuine forcing that seeds curvature of order $r^{-2}$ on the transition annulus. It is not "absorbed" multiplicatively — it enters as $\int_{\text{transition}}|\nabla^2\chi^2|\,|Rm|^{n/2-1}\le\varepsilon\int|Rm|^{n/2}+C_\varepsilon r^{-n}\mathrm{Vol}(\text{transition})$, i.e. it produces the additive baseline that Step 17 Section 6 estimates as $O(\theta r_*^4\bar K^{1/2})$. Calling it "lower order" is correct in the dimensionless normalized energy for small $\theta$, but it is a forcing term, not a term the dissipation swallows.

The derivative structure is no worse than Wang's Lemma 4.4 ($\nabla^i\chi*\nabla^j\chi*\nabla^kRm$ with $i+j+k=m+2$), so the normalization introduces no new high-order interaction. The important asymmetry: for the **defect** $E=Ric+g$ the homogeneity $\mathcal C_a(0)=0$ (Step 14/17) removes the analog source, but for **$Rm$** — which is what must serve as the time-dependent potential — the source persists. This is exactly the transition-region curvature difficulty that the notes identify as open; the normalization does not create it, but it does not remove it for the potential either.

---

### Point 4 — First-exit logic

**No circular dependency at the logical level.** The structure is a continuity/first-exit argument: on $[0,T_*)$ assume provisional metric comparability, relative Sobolev/cover bounds, local energies $\le2\varepsilon_*$, and connection/Hessian bounds; then show each is *strictly* improved for small $\delta$, so a saturated bound at $T_*$ is contradicted and the interval extends. The classical loop (metric equivalence → Sobolev → curvature → Li → Sobolev → metric equivalence) is genuinely broken because the improvement constants are all $O(\delta)\times$(bounded), uniform as $\delta\to0$. The drift-integrability bookkeeping is correct:
- metric drift $\int_0^{\theta r^2}|aE|\,dt=\frac{p}{p-2}\,\delta\,\theta^{1-2/p}r^2$, finite iff $p>2$ (log-divergent endpoint at $p=2$);
- connection drift $\int_0^{\theta r^2}|a^{1/2}\nabla U|\,dt\sim\frac{2p}{p-4}\,\delta\,\theta^{1/2-2/p}$, finite iff $p>4$.

The $p>4$ separation between metric comparability and connection/Hessian stability is a correct and clean piece of arithmetic.

**But the chain rests on two unestablished PDE statements of the same difficulty as the target:**

1. The localized degenerate curvature-potential $|\chi^2Rm|\le C\beta/t$ (Point 2). Wang's Thm 6.3 conclusion 1 gives exactly $|\chi^2Rm|_\infty\le\bar C(n)t^{-1}(t|\nabla\chi|^2+1)^{4/n+2}\beta$, which for n = 4 is $(1+\theta)^3\bar C\beta/t\le 8\bar C\beta/t$ — but under *global* Sobolev and *global* $L^{n/2}$ smallness. The finite-neighbor degenerate version is not in either source.
2. The **weighted tensor Bernstein** $|\chi\nabla(\chi^2E)|\le C_p\delta\,t^{-1/2}(r^2/t)^{2/p}$. The script's justification is a WKB-type "effective diffusion scale $\chi\sqrt t$" heuristic: standard $|\nabla u|\le C\sup|u|/\sqrt t$ becomes $|\nabla u|\le C\sup|u|/(\chi\sqrt t)$, so $\chi|\nabla u|\le C\sup|u|/\sqrt t$. This is plausible for a scalar degenerate heat equation, but it is asserted, not derived, and for the *tensor* equation Step 18 (3)–(4) it must control the drift $\mathcal B_a(U)$ (terms $a^k\nabla U$, $a_i\nabla_j\sigma$, regularized to $d\chi$-coefficients). A Bernstein estimate for a degenerate tensor equation with this drift near $\chi=0$ is not standard and is not established. It is a second open input, not a corollary.

So the logic is *conditional*, not circular: everything follows once "$R_\alpha\le\varepsilon_*$ (+ provisional geometry) ⟹ weighted pointwise curvature decay under $\partial_t-a\Delta$ on the transition region" and the weighted tensor Bernstein are granted. Both are the local/degenerate analogs of the very theorems (Li Thm 3.4, Wang Thm 6.3) that exist only globally or non-degenerately.

**On the script framing.** `verify_step19_volume_independent_beta.py` and `..._p4_threshold_and_bernstein.py` print "ALL VERIFICATIONS PASSED." What they actually verify is: (i) the β volume-cancellation algebra, (ii) the p>2 and p>4 drift-integrability exponents, (iii) numerical inequalities for a sample $(\theta,\delta,p)=(0.1,0.01,6)$ (e.g. metric drift $\approx3.2\times10^{-3}$, connection drift $\approx2.0\times10^{-2}$, both under threshold). All three are correct arithmetic/exponent checks. None of them exercises the two PDE statements in Point 2 and Point 4 above; those are entered as premises. The scripts' own "REMAINING VERIFICATION" bullets ("Wang Theorem 6.3 localization to finite-neighbor system"; "normalized flow lower-order terms"; "short-time existence") name precisely the parts that are not verified.

---

### Summary of what is solid and what remains

- Volume cancellation of β (Point 1): correct, and true in all dimensions; the four-dimensional content is Gauss–Bonnet control of $\bar K$ and Cheeger–Tian collapse-independence, not the cancellation itself.
- Drift-exponent arithmetic (Point 4): correct; p>2 for metric comparability, p>4 for connection/Hessian, with the stated $\theta$-powers.
- Normalization terms (Point 3): correctly typed; the one item to state plainly is the $Rm$-independent additive source $\nabla^2(\chi^2)*g$ on the transition annulus, which is a forcing controlled only in the small-$\theta$ integrated energy, and which survives for $Rm$ even though homogeneity removes its analog for $E$.
- Localization and closure (Points 2, 4): the argument is conditional on two estimates that are the degenerate/finite-neighbor analogs of Li Thm 3.4 and Wang Thm 6.3 — (a) $|\chi^2Rm|\le C\beta/t$ from local energy smallness under $\partial_t-a\Delta$, and (b) the weighted tensor Bernstein — neither of which is present in the sources or derived in the notes. The Angenent–Knopf 4D example in Wang Section 2 is a concrete indicator that the accompanying $L^p$ Ricci/defect bound (p>2) must be propagated in tandem and cannot be replaced by $L^2$ curvature energy alone.

The material that would move this from conditional to established is exactly the derivation of (13) and the tensor Bernstein estimate under the degenerate localized operator, together with the level-dependent neighbor-coupling control that keeps $\varepsilon_*$ effective across all Moser exponents.