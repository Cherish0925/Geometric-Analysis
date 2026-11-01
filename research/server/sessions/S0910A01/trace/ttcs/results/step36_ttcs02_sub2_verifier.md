# TTCS Independent Branch Record

```json
{
  "step_id": 36,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step37_transported_deturck_existence.md",
    "Sessions/S0910A03/workspace/notes/step37_global_Q_persistence.md",
    "Sessions/S0910A03/workspace/notes/step37_base_pair_continuation.md",
    "Sessions/S0910A03/workspace/scripts/verify_step37_interface_algebra.py",
    "Sessions/S0910A01/workspace/notes/step36_analytic_platform_and_global_Q.md",
    "Sessions/S0910A01/workspace/scripts/step36_platform_Q_verify.py",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Review A03 Step 37's three analytic-interface notes as possible proofs for the restricted four-dimensional negative cutoff-flow route, using A01's Step 36 platform note and verifier as comparison. Focus especially on the shifted-U base-pair continuation note. Check: (1) transported-DeTurck existence: does the note correctly adapt Yang's Theorem 8.2 to the normalized term, and is any claimed chi^2 weight for delta(hat a) too strong or harmless? (2) global Q persistence: are the weights, buffered K2 use, Gronwall coefficient, and independence from J6 correct? (3) base-pair continuation: does the written proof actually implement the second integration by parts for I_{1c}/I_3 that the script/message claim, or does it still rely on an invalid direct Holder bound such as ∫ chi |Theta| |W|^p <= ||Theta||_p ||W||_p^p? Are unweighted L^p(T), Sobolev upgrades, and G terms sufficiently justified, or still hidden hypotheses? Give a direct mathematical memo identifying what can be accepted now and what exact calculation remains.

## Output

# Verification Memo: A03 Step 37 Three Analytic Interfaces

Prepared against A01 Step 36 platform note, both verifier scripts, and the two Yang/Wang source objects. I read the mathematics of each interface term by term. Summary judgments and the exact remaining calculations follow.

---

## Interface 1 — Transported-coefficient DeTurck existence

**The gauge is Yang's, and this is the correct one.** Yang's Approach 1 gauge term is $\hat\delta^*\big((\chi\circ\varphi_t^{-1})^2\,S^{-1}\delta G(S)\big)$. Since $\hat\delta^*\omega=\tfrac12(\hat\nabla_j\omega_i+\hat\nabla_i\omega_j)=\tfrac12\mathcal L_{\omega^\sharp}\hat g$, this equals $\tfrac12\mathcal L_{\hat a W}\hat g$ with $\hat a=(\chi\circ\varphi_t^{-1})^2$ and $W=(S^{-1}\delta G(S))^\sharp$. A03's (2.2) reproduces exactly this operator. This coincides with A01 §1's correction that the coefficient must sit inside the Lie derivative, because $\mathcal L_{\hat aW}\hat g=\hat a\mathcal L_W\hat g+d\hat a\otimes W^\flat+W^\flat\otimes d\hat a$; the fixed-coefficient $\hat a\mathcal L_W$ drops the $d\hat a\otimes W^\flat$ pieces. Both sessions agree; the object is right.

**Pullback identity is valid.** With $g=\varphi_t^*\hat g$, the diffeomorphism ODE (2.3) is unchanged from Yang, so the cancellation between $\mathcal L_{V_t}\hat g$ ($V_t=\partial_t\varphi_t\circ\varphi_t^{-1}$) and the gauge term is Yang's verbatim and is untouched by the normalization. The residual bracket $-2\hat a(\operatorname{Ric}_{\hat g}+\hat g)$ pulls back to $-2a(\operatorname{Ric}_g+g)$ by naturality of Ricci, $\varphi_t^*\hat g=g$, and $\varphi_t^*\hat a=a$ (the last is pure composition since $\hat a=a\circ\varphi_t^{-1}$). Correct.

*One notational item.* A03's parenthetical "the transport equation $\partial_t\hat a=(\hat a W)\hat a$" is garbled. The actual transport law is $\partial_t\hat a+\mathcal L_{V_t}\hat a=0$, i.e. $\partial_t\hat a=-d\hat a(V_t)$, which follows directly from $\hat a=a\circ\varphi_t^{-1}$. This does not affect the pullback conclusion; only the written formula is wrong.

**On the $\chi^2$ weight for $\delta\hat a$ — it is stronger than the differentiation gives, and the excess is harmless.** Differentiating $\hat a=(\chi\circ\varphi_t^{-1})^2$ against the map variation $\psi=\delta\varphi$ gives
$$\delta\hat a=2(\chi\circ\varphi_t^{-1})\,\delta(\chi\circ\varphi_t^{-1})\sim (\chi\circ\varphi_t^{-1})\,(d\chi\circ\varphi_t^{-1})\,\psi,$$
which carries a **single** factor $\hat\chi=\hat a^{1/2}$, not $\chi^2=\hat a$. So A03's assertion of a $\chi^2$ weight is a stronger statement than the calculation supports. It is nonetheless harmless: $\delta\hat a$ is algebraic (order zero) in $\psi$, hence $-2(\delta\hat a)\hat g$ is a zeroth-order term in $\psi$ carrying at least a single $\hat\chi$. Yang's linearized template (1.4)–(1.5) has an $E_0\psi$ slot requiring **no** weight at all; the true single-$\chi$-weighted zeroth-order term sits comfortably in that slot. The other new piece $-2\hat a\,h$ enters $Dh$ (bounded, order zero in $h$). Neither touches the principal symbol $2\chi^2\Delta$ or the transport structure. A01's script (D4) reaches the same conclusion by describing $\delta\hat a$ as "$-d\hat a(\psi)$," which is the accurate single-derivative form.

**What this interface rests on.** The existence conclusion is contingent on Yang's smooth tame energy estimates for the linearized transported system (Yang states these "by standard arguments using energy integrals and interpolation," referencing Klainerman's appendix). A03 §6 states this dependence plainly, and correctly does not substitute plain strictly-parabolic Schauder — the error A01 §1.2 warns about, because Schauder constants degenerate as $\chi\to0$ and do not yield the $\varepsilon$-independent limit. Given Yang's estimates and their stability under bounded lower-order additions, the reduction is sound. The Approach-2 remark (coefficient-regularized normalized flow) is consistent: the extra $-2(\varepsilon^2+\chi^2)g$ produces a curvature reaction linear in $|\mathrm{Rm}|$ (the scaling test in A01 §1 gives $\partial_t|\mathrm{Rm}|^2=+4|\mathrm{Rm}|^2$ at $\operatorname{Ric}=0$ in dimension 4), handled by Grönwall without disturbing the $\varepsilon$-uniform $L^2$ curvature energies.

**Acceptable now:** the normalized transported-DeTurck system and its pullback identity, and the reduction of normalized short-time existence to Yang's tame estimates plus a genuinely lower-order perturbation.

---

## Interface 2 — Global unweighted defect $Q(t)=\int_M|E|^2\,d\mu$

**Homogeneity is the load-bearing fact and it holds.** In (2.1) every term of $(\partial_t-a\Delta)|E|^2$ carries at least one power of $E$; there is no curvature-only source, so $E=0$ (exact $\operatorname{Ric}=-g$) is stationary. The Hessian-$a$ contraction $B_0=2g|E|^2+2(\operatorname{tr}E)E-4E^2$ is the tensor A01 Step 35 §5–6 derives from the Ricci linearization (A01's $B_{\mathrm{def}}$, with $B_0=2B_{\mathrm{def}}$ — the factor-two match is confirmed in A01 §5.5). Consistent across sessions.

**Weights and Hölder checks pass.**
- $I_2$: Young on $\int|da||E||\nabla E|$ with the split $(\sqrt a|\nabla E|)(|da|a^{-1/2}|E|)$ gives $\varepsilon\int a|\nabla E|^2+C_\varepsilon\int(|da|^2/a)|E|^2$, and $|da|^2/a=4\chi^2|d\chi|^2/\chi^2=4|d\chi|^2\le Cr^{-2}$. Because $\chi\ge0$ is smooth, $d\chi=0$ at zeros of $\chi$, so the integrand extends continuously through $\{a=0\}$ and no division singularity occurs. Correct.
- $I_1$: two-factor Hölder $\|F\|_{L^2}\|\chi_jE\|_{L^4}^2$ ($\tfrac12+\tfrac14+\tfrac14=1$), then the dimension-4 Sobolev $\|\chi_jE\|_4^2\le C\mathcal S_j\|\nabla(\chi_jE)\|_2^2$ with $\chi_jE$ compactly supported in $B_{6r}$, and $\chi_j^2=a$ on the disjoint support $U_j$. This yields $I_{1,j}\le C\gamma_j(\int_{U_j}a|\nabla E|^2+r^{-2}\int_{U_j}|E|^2)$, $\gamma_j=\mathcal S_jK_{2,j}^{1/2}$. The buffered $K_{2,j}=\int\eta_j^2F^2$ with $\eta_j\equiv1$ on $\operatorname{supp}\chi_j$ correctly bounds $\|F\|_{L^2(U_j)}^2$. Correct.
- Measure term: $\int a|E|^3\le C\int aF|E|^2$ using $|E|\le CF$, i.e. it is of $I_1$-type and absorbs into $I_1$. This is terse in the note but valid.

**Grönwall coefficient — a precision difference from A01, harmless for small $r$.** A03 reaches $Q'\le Cr^{-2}Q$ hence $Q(t)\le e^{C\theta}Q(0)$ on $[0,\theta r^2]$. A01 (3.6)–(3.7) keeps $Q'\le C(1+r^{-2})Q$, hence $e^{C\theta(1+r^2)}Q(0)$, and explicitly records that the shorter $Cr^{-2}$ form needs $r\le1$. A03's bounded $O(1)$ reaction (from the "$1$" in $F^2=1+|\mathrm{Rm}|^2$ and the measure term) is folded into $Cr^{-2}$ silently. For the fixed small-radius first-exit application the two agree; A01's statement is the more precise one and should be the reference form if $r>1$ is ever contemplated.

**Independence from $J_6$ and $\|aE\|_\infty$ is correctly argued.** The power model $a=x^2,\ E\sim x^{-\alpha}$ shows $aE\sim x^{2-\alpha}\to0$ and $a^4|E|^6\sim x^{8-6\alpha}\to0$ (for $\alpha<4/3$) while $|E|^2\sim x^{-2\alpha}$ diverges, so weighted controls near $\{a=0\}$ cannot supply $Q$. The terminal $7/24$ calibration $\int(|W^+|-\tfrac1{2\sqrt6})^2\le\tfrac7{24}Q$ is genuinely a separate consumer. Correct.

**Acceptable now, conditionally.** Given the first-exit provisional geometry it invokes (smooth solution from Interface 1; disjoint buffered supports; bilipschitz metric comparability $e^{C_0\theta}$; $\gamma_j\le\gamma_0\ll1$ with the *moving* $\mathcal S_j(t),K_{2,j}(t)$), the $Q$ inequality and its exponential bound are a correct standalone lemma. The metric comparability and the moving-Sobolev/$\gamma_j$ hypotheses are supplied elsewhere in the bootstrap, not here — the note states this.

---

## Interface 3 — Base-pair continuation $(\nabla U,\nabla^2\chi)$ (focus)

**Direct answer to the central question: the current written text implements the second signed integration by parts for $I_{1c}$ and $I_3$; it does not rely on the invalid direct Hölder $\int\chi|\Theta||W|^p\le\|\Theta\|_p\|W\|_p^p$.**

*Version note first.* The supersession banner at the top says "(3.9) and (3.11) have a power-counting error … the repaired estimate uses a second signed IBP." But the body text now printed at (3.9) and (3.11) is already the repaired second-IBP estimate (3.9 is labeled "(Step 38 correction)"; 3.11 says "As for $I_{1c}$ … integrate once off the Hessian"), and §6 already refuses the $L^\infty$ upgrade. So the file has been edited in place and the banner is a stale warning about the pre-repair draft. The mathematics currently on the page is the corrected version. This is a documentation inconsistency, not a mathematical one, but it should be reconciled so the file is not read as still carrying the error.

*The second IBP, verified.* For $I_{1c}$ (and identically $I_3=\int\chi\Theta*W\cdot|W|^{p-2}W$), the dangerous quantity is $\int\chi|\Theta||W|^p$ with $\Theta=\nabla^2\chi$ and no spare $\nabla W$. Writing $\Theta_{ij}=\nabla_i(\nabla_j\chi)$ and integrating $\nabla_i$ off,
$$\int\chi\,\nabla_i(\nabla_j\chi)\,B^{ij}=-\int(\nabla_i\chi)(\nabla_j\chi)B^{ij}-\int\chi(\nabla_iB^{ij})(\nabla_j\chi),$$
with $|B|\le C_p|W|^p$, $|\nabla B|\le C_p|W|^{p-1}|\nabla W|$. The first term is $\le\|d\chi\|_\infty^2\int|W|^p$. The second, using $\chi=\sqrt a$ and Young on $(\sqrt a|\nabla W||W|^{(p-2)/2})(|d\chi||W|^{p/2})$, is $\le\varepsilon\int a|\nabla W|^2|W|^{p-2}+C_\varepsilon\|d\chi\|_\infty^2\int|W|^p$. This reproduces (3.9)/(3.11) exactly. The essential outcome is that **no $\|\Theta\|_p$ is generated**, so $I_{1c},I_3$ stay inside the $\mathscr W_p=\|W\|_p^p$ Grönwall channel — which is precisely what the direct Hölder route (needing $W\in L^{p^2/(p-1)}$, as A01's script G5b records) cannot achieve. The calculation is valid.

*Where $\|\Theta\|_p$ legitimately does appear.* $I_{1a}$ carries a spare $\nabla W$ (from differentiating the test function), so Young leaves $K^2\int|\Theta|^2|W|^{p-2}\le K^2\|\Theta\|_p^2\|W\|_p^{p-2}$ (Hölder exponents $(p/(p-2),p/2)$, sum 1 — checked). In (3.16) this Young-converts to $CK^p\|\Theta\|_p^p+C\mathscr W_p$ (exponents $2/p+(p-2)/p=1$ — checked), coupling to the $\Theta$-equation. The distinction $I_{1a}$ (has $\nabla W$, gives $\|\Theta\|_p^2$) versus $I_{1c},I_3$ (no $\nabla W$, need second IBP) is drawn correctly. $R_4=\chi\nabla\chi*\nabla^2U$ with $\nabla^2U=\nabla W$ and $\chi\le a^{1/2}$ Young-absorbs into diffusion plus $Cr^{-2}\int|W|^p$ — correct.

*The $\Theta$-equation (§4).* Since $\operatorname{Ric}(U)=aE$ as tensors, $\nabla\operatorname{Ric}(U)$ is a contraction of $\nabla U=W$, so $|\partial_t\Gamma|\le C|W|+C$; the norm/measure variation contributes $CK|\Theta|$ via $\partial_tg^{-1}\sim U$, $|U|\le K$. Hence $\partial_t|\Theta|\le CK|\Theta|+C|W||d\chi|$, and (4.2)–(4.3) close by Young. Correct. The coupled Volterra $Y_1=\|W\|_p^p+\|\Theta\|_p^p$, $Y_1'\le C_1(1+Y_1+\|T\|_p^p)$, then Grönwall (5.1)–(5.3), is valid **provided** $\|T\|_p^p$ is finite on $[0,T)$.

**The two inputs that remain external, and their status.**

1. **Unweighted $\|T\|_{L^p}<\infty$ uniformly on $[0,T)$ is imported, not established here.** This is the decisive delegated assumption. $T=\mathrm{Rm}+G$; $U=aT$; and $\sup|U|\le K$ does **not** by itself bound $T$ unweighted where $a$ is small-but-positive (the collar region). For each fixed $t<T$ smoothness gives $\|T(t)\|_p<\infty$ on compact $M$, but **uniform** finiteness as $t\uparrow T_{\max}$ is exactly the quantity A01 §2 warns can be lost at a finite maximal time ("declaring $\|T\|_\infty$ or $\|a\nabla\mathrm{Rm}\|_\infty$ finite because the solution is smooth on proper subintervals does not exclude blow-up at $T_{\max}$"). A03 §5/§7 cites "Step 27 eq. 5.4" for this. That derivation is not in the supplied files and cannot be checked here. Until it is exhibited, the base-pair lemma stands on an unverified uniform $L^p(T)$ input.

2. **The degenerate-weighted gradient does not upgrade to $L^\infty$, and the note correctly refuses that step.** The energy controls $\int a|\nabla W|^2|W|^{p-2}$ — a $\chi^2$-weighted derivative — not the unweighted $\int|\nabla W|^p$ that Sobolev embedding $W^{1,p}\hookrightarrow L^\infty$ (for $p>n$) would require. So finite $\|W\|_p$ for all $p$ gives no pointwise bound. §6 states this explicitly; there is no concealed Sobolev upgrade. This is the correct reading.

3. **$G$ terms are bounded.** $G=\tfrac{g\owedge g}{2(n-1)}$ is algebraic in $g$ with $\nabla G=0$ and $|G|\le C$ under uniform metric equivalence, so $\operatorname{Ric}(G)=g$, $\operatorname{Ric}(T)=E$, $\operatorname{Ric}(U)=aE$; the $R_6=aG*W+\text{lower}$ terms are $O(|W|+1)$. Justified. (Its time variation is absorbed into $R_7$, which itself invokes $K|T|$ — again the same imported $L^p(T)$ dependence.)

**Acceptable now:** the finite-$L^p$ base-pair inequality for $(\nabla U,\nabla^2\chi)$, in its second-IBP form, **conditional on uniform $\|T\|_{L^p}$ on $[0,T)$**. It is not an extension theorem and the note does not present it as one.

---

## What can be accepted, and the exact calculations that remain

**Can be taken as established (each with its stated dependence):**
- The normalized transported-DeTurck system, its pullback to $\partial_tg=-2a(\operatorname{Ric}+g)$, and short-time existence reduced to Yang's tame estimates plus a strictly lower-order perturbation (Interface 1). The only textual fixes needed are the transport-equation formula and the $\delta\hat a$ weight wording (single $\chi$, not $\chi^2$; harmless either way).
- The exponential persistence of $Q(t)$ on $[0,\theta r^2]$, conditional on the first-exit provisional geometry, and its logical independence from $J_6$ and $\|aE\|_\infty$ (Interface 2). Recommend adopting A01's $C(1+r^{-2})$ coefficient as the reference form.
- The second-IBP finite-$L^p$ base-pair inequality (Interface 3), conditional on uniform $\|T\|_{L^p}$; it correctly avoids the invalid direct Hölder.

**Exact calculations still owed:**
1. **Uniform $\|T\|_{L^p(M)}$ on the full $[0,T_{\max})$** for $T=\mathrm{Rm}+G$, from $\sup|U|=\sup|aT|\le K$ plus uniform metric equivalence. This is the one input the base-pair lemma cannot supply itself, and it is the quantity most exposed to loss at $T_{\max}$. The needed argument must pass from the weighted control of $U$ to unweighted control of $T$ across the collar $\{0<a\ll1\}$; write it out (the referenced "Step 27 §5" was not provided for checking).
2. **The higher induction $m\ge2$**: control of $\nabla^m U$ and the top cutoff jets $\nabla^{m+1}\chi,\nabla^{m+2}\chi$ coupled to differentiated lower-order curvature, following Wang's Lemma 4.11/Prop 4.13–4.14 pattern but with $U=a(\mathrm{Rm}+G)$ in place of $\chi^2\mathrm{Rm}$. The $m=1$ term structure (four dangerous groups, second IBP on Hessian-of-$\chi$ terms) must be shown to propagate; Wang's induction closes precisely because $\|\nabla^2\chi\|_q$ and $\|\nabla(\chi^2\mathrm{Rm})\|_q$ interplay — the analogous interplay for the shifted variable is asserted, not yet carried through.
3. **The $L^p\to L^\infty$ passage**, which requires an *unweighted* next-derivative level (an unweighted $\int|\nabla W|^p$ or a $W^{1,p}$ bound), obtainable only after step 2 supplies the missing spatial derivative. Only then does $\|aF\|_\infty$ / $\|\nabla^m(\chi^2 T)\|_\infty$ and hence smooth continuation past $T_{\max}$ follow (cf. Wang Prop 4.3/4.9/4.14).
4. **Terminal restart**: reopening the flow beyond $T_{\max}$ by the per-datum existence theorem, which needs steps 1–3 to deliver a smooth limiting metric at $T_{\max}$.

Everything above concerns only the restricted four-dimensional near-critical negative cutoff-flow laboratory; the positive branch, arbitrary four-manifold topology, dimensions $n\ge5$, dimension-only constants, and the Lean formalization are untouched by these three notes, as A01 §5 also records.