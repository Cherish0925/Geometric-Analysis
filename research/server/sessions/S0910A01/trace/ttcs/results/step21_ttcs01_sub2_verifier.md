# TTCS Independent Branch Record

```json
{
  "step_id": 21,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step21_finite_exponent_smoothing_lemma.md",
    "Sessions/S0910A01/workspace/scripts/step21_finite_exponent_smoothing.py",
    "Sessions/S0910A01/workspace/notes/step20_closed_tensor_estimate.md",
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md"
  ]
}
```

## Task

Verify the conditional finite-exponent smoothing lemma for the four-dimensional normalized cutoff flow ∂_t g = -2χ²(Ric+g). The construction claims four steps on each Whitney ball B_ℓ(y) with ℓ=crχ₀:

1. q=2 energy estimate with critical absorption (γ = Cr²√(1+K₀) small) giving time-uniform L² and integrated gradient L².
2. Parabolic Sobolev embedding in n=4 spatial dimensions: p* = 2(n+2)/n = 3, converting L^∞_t L² ∩ L²_t H¹ to spacetime L³.
3. q=3 power inequality with a time cutoff φ(t)=0 for t<δ, φ=1 for t≥2δ: the time-cutoff source is controlled by the spacetime L³ from Step 2, producing time-uniform spatial L³ on [2δ,T].
4. Stampacchia/Moser local boundedness: since L³_spatial is supercritical (3 > n/2 = 2 for n=4), the standard parabolic regularity gives F = (1+|Rm|²)^{1/2} ≤ C on an inner ball.

Specific questions to check:
(a) Is the BG energy transfer in Section 3 correct: ℓ⁴ fint|Rm|² ≤ CK₀r⁴ with χ₀ canceling exactly?
(b) In the Sobolev absorption at q=2, does the factor a₀ cancel on both sides, making the threshold γ-independent of χ₀?
(c) For q=3, is the chain-rule coefficient (3/2)² = 9/4, and does the same γ threshold work?
(d) Is the parabolic interpolation exponent 2(n+2)/n = 3 correct for n=4?
(e) For Step D, is L³_spatial supercritical for the Stampacchia theory? The standard condition is V ∈ L^p with p > n/2 = 2 for spatial dimension n=4. Since the potential V = CaF has F ∈ L³ uniformly in time, V ∈ L³ with 3 > 2.
(f) Is the bootstrap closure in Section 13 logically consistent: does the curvature bound feed back to preserve metric comparability, Sobolev persistence, and energy bounds?

## Output

# Verification Memo: Conditional Finite-Exponent Smoothing Lemma (Step 21)

## 1. Overall Structure Assessment

The four-step chain

$$
q{=}2\;\text{energy}\;\to\;\text{4D parabolic Sobolev}\;\to\;q{=}3 + \text{time cutoff}\;\to\;\text{local boundedness}
$$

is mathematically well-structured. Each step feeds a definite analytical output into the next, and the critical absorption threshold $\gamma_W = O(r^2\sqrt{1+K_0})$ is used at only two fixed exponents. I verify each specific question below.

---

## 2. Question (a): Bishop–Gromov Energy Transfer

**Conclusion.** $\ell^4\fint_W|\mathrm{Rm}|^2 \le CK_0 r^4$ with $\chi_0$ canceling exactly: **correct in substance**, with an expositional gap in the BG step.

**Detail.** The note applies Bishop–Gromov to the pair $B_\ell(y)\subset B_{5r}(p)$ as though they were concentric. They are not: $d(y,p)<4r$ with $\ell=cr\chi_0$. The fix is a two-step comparison through concentric balls at $y$:

1. Since $B_{5r}(p)\subset B_{9r}(y)$ (triangle inequality), the BG monotonicity for balls centered at $y$ gives $\operatorname{Vol}(B_{9r}(y))/\operatorname{Vol}(B_\ell(y))\le C(9r/\ell)^4$.
2. The reverse inclusion $B_{5r}(p)\subset B_{9r}(y)$ gives $\operatorname{Vol}(B_{9r}(y))\ge\operatorname{Vol}(B_{5r}(p))$.

Combining: $\operatorname{Vol}(B_\ell(y))\ge \tilde c_{\mathrm{BG}}(\ell/r)^4\operatorname{Vol}(B_{5r}(p))$. The constant becomes $\tilde c_{\mathrm{BG}}$ (absorbing $9^4$ and the BG constant) instead of $c_{\mathrm{BG}}(c\chi_0/5)^4$. But the dependence on $\chi_0$ is **identical**—all through $\ell^4 = c^4r^4\chi_0^4$—so the cancellation

$$
\ell^4 \fint_W |\mathrm{Rm}|^2 \le \frac{K_0\operatorname{Vol}(B_{5r})}{\operatorname{Vol}(B_\ell)} \cdot \ell^4 = \frac{K_0}{\tilde c_{\mathrm{BG}}}\left(\frac{r}{\ell}\right)^4\ell^4 = \frac{K_0r^4}{\tilde c_{\mathrm{BG}}}
$$

is exact: $\chi_0$ drops out. The derivation should state the non-concentric two-step comparison explicitly; the final result is unchanged.

---

## 3. Question (b): $a_0$ Cancellation at $q=2$

**Conclusion: correct.**

The reaction term at $q=2$ is $\int\eta^2 a F^3$. On the Whitney ball $a\in[(1{-}Lc)^2a_0,(1{+}Lc)^2a_0]$, so:

$$
\int\eta^2 aF^3 \le (1{+}Lc)^2 a_0\int F\cdot(\eta F)^2 \le Ca_0\|F\|_{L^2(W)}\|\eta F\|_{L^4(W)}^2.
$$

Sobolev ($n=4$, $H^1\hookrightarrow L^4$):

$$
\|\eta F\|_4^2 \le A_W^2\bigl(\|\nabla(\eta F)\|_2^2 + \ell^{-2}\|\eta F\|_2^2\bigr).
$$

The gradient part must be compared against the LHS dissipation $c_2\int\eta^2 a|\nabla\mathrm{Rm}|^2$. Since $|\nabla F|\le|\nabla\mathrm{Rm}|$ and $a\ge(1{-}Lc)^2a_0$:

$$
\int\eta^2|\nabla F|^2 \le \frac{1}{(1{-}Lc)^2 a_0}\int\eta^2 a|\nabla\mathrm{Rm}|^2.
$$

Substituting back: the numerator $a_0$ from Hölder and the denominator $a_0^{-1}$ from converting unweighted-to-weighted gradient cancel, leaving the threshold

$$
\gamma_W = A_W^2\|F\|_{L^2(W)}
$$

independent of $\chi_0$. The same mechanism applies at every step where the reaction is absorbed; $a_0$ never survives into the effective smallness parameter.

---

## 4. Question (c): Chain-Rule Coefficient at $q=3$

**Conclusion: correct, coefficient is $(3/2)^2=9/4$.**

At $q=3$ the Sobolev variable is $\phi=\eta F^{3/2}$, with $\nabla(F^{3/2})=\tfrac32 F^{1/2}\nabla F$, so $|\nabla(F^{3/2})|^2=\tfrac94 F|\nabla F|^2$. When the reaction $\int aF^4=\int aF\cdot\phi^2$ is estimated by Hölder–Sobolev, the gradient part of the RHS contains

$$
\frac{9}{4}\int\eta^2 F|\nabla F|^2,
$$

which, after the $a_0$-cancellation, produces the effective threshold $(9/4)\gamma_W$. For $q=2$ the analogous coefficient is $(2/2)^2=1$. Both are absorbed under the same condition $\gamma_W<\varepsilon_0(c,L,\Lambda)$; the factor $9/4$ enlarges $\varepsilon_0$ by at most a factor of $4/9$ but does not change the structural mechanism.

The script's table confirms: at $q=2$ the coefficient is $1$, at $q=3$ it is $9/4$, and for higher $q$ it grows as $q^2/4$. Only $q=2,3$ are needed.

---

## 5. Question (d): Parabolic Interpolation Exponent

**Conclusion: correct, $p^*=2(n+2)/n=3$ for $n=4$.**

The Gagliardo–Nirenberg parabolic interpolation: for $u\in L^\infty_tL^2_x\cap L^2_tH^1_x$ on an $n$-dimensional Riemannian domain,

$$
\|u\|_{L^q_{t,x}}^q \le C\bigl(\sup_t\|u\|_2^2\bigr)^{q/2-1}\|\nabla u\|_{L^2_{t,x}}^2, \qquad q=\frac{2(n+2)}{n}.
$$

For $n=4$: $q=3$, and the power on $\sup_t\int u^2$ is $q/2-1=1/2$. Thus:

$$
\int_0^T\!\!\int|u|^3 \le C\bigl(\sup_t\textstyle\int u^2\bigr)^{1/2}\int_0^T\!\!\int|\nabla u|^2.
$$

This matches equation (6.1) of the note. The exponent $1/2$ acts on $\int u^2$ (equivalently, power $1$ on $\|u\|_2$), consistent with $q(1-\alpha)=q-2=1$ for the GN interpolation with $\alpha=2/q$.

---

## 6. Question (e): Supercritical Condition for Stampacchia

**Conclusion: correct. $L^3_x$ potential with $3>n/2=2$ is supercritical for $n=4$.**

In the rescaled Whitney cylinder $\tilde B_{1/8}\times[2\tilde\delta,\tilde T]$, the operator $\partial_{\tilde t}-\tilde a\tilde\Delta$ is uniformly parabolic ($\tilde a\in[\lambda,\Lambda_W]$). The subsolution structure for $w=F^2$ is

$$
\partial_{\tilde t}w \le \tilde a\,\tilde\Delta w + Vw,
$$

where $V=C\tilde aF+\text{(lower-order constants)}$. Since $F\in L^3_x$ uniformly for $\tilde t\ge2\tilde\delta$ (Step C output), we have $V\in L^\infty_tL^3_x$.

The Serrin-type/Kato condition for the standard parabolic local-boundedness theorem is $\frac{n}{2p}+\frac{1}{q}<1$ with $V\in L^q_tL^p_x$. Here $p=3$, $q=\infty$: $\frac{4}{6}+0=\frac{2}{3}<1$. ✓

**Technical refinement needed.** The pointwise subsolution requires handling the gradient term $(\nabla a)\cdot(\nabla E)\cdot\mathrm{Rm}$ that appears in $\partial_t|\mathrm{Rm}|^2$. This term involves $|\nabla\mathrm{Rm}|$ (not just zeroth order) and does not immediately fit the $Vw$ format. The resolution: on the Whitney ball where $\tilde a\ge\lambda>0$, Young's inequality gives

$$
|\tilde\nabla a|\,|\tilde\nabla\mathrm{Rm}|\,|\mathrm{Rm}|\le\frac{\epsilon}{2}\tilde a|\tilde\nabla\mathrm{Rm}|^2 + \frac{C_\epsilon}{2\tilde a}|\tilde\nabla a|^2|\mathrm{Rm}|^2.
$$

The first part is absorbed into the dissipation $-2\tilde a|\tilde\nabla\mathrm{Rm}|^2$; the second is $\le C_\epsilon\lambda^{-1}(cL)^2 F^2$, a zeroth-order potential. After this absorption, the subsolution becomes a genuine $\partial_{\tilde t}w\le\tilde a\tilde\Delta w + \tilde Vw$ with $\tilde V\in L^\infty_tL^3_x$. The note should state this absorption explicitly.

---

## 7. Question (f): Bootstrap Closure

**Conclusion: logically consistent for positive-time continuation, with one gap requiring explicit treatment.**

The bootstrap loop is:

| Hypothesis | Self-improvement mechanism | Status |
|---|---|---|
| (H2) Metric comparability | Curvature bound $\Rightarrow$ metric drift $\int_0^T\|aE\|dt$ small | See below |
| (H3) Sobolev persistence | Follows continuously from (H2) | ✓ |
| (H4) Small critical product | $\gamma_W=Cr^2\sqrt{1+K_0}$, depends only on initial data and $r$ | ✓ |
| Energy persistence | $K_0$ preserved by curvature bound + metric comparability | ✓ |

**The gap is the early-time interval $[0,3\delta)$.** The curvature bound from Step D holds only for $t\ge3\delta$. The metric drift decomposes as:

$$
|g(T)-g(0)|\le 2\int_0^{3\delta}|aE|\,dt + 2\int_{3\delta}^T|aE|\,dt.
$$

The second integral is $\le 2C_4\cdot T$ (using the Step D bound). The first integral requires initial-data control: $|aE(0)|\le|E_0|$ is bounded by the initial near-Einstein condition $|E_0|\le\delta_0\ll 1$. On $[0,3\delta)$ with smooth initial data, a short-time existence/continuation argument bounds $\sup_{[0,3\delta]}|aE|$ in terms of $|E_0|$ and $\delta$. The total early drift is $O(\delta\cdot f(\delta_0,K_0))$.

For the specific LeBrun application where $|E_0|\le\delta_0\to 0$, this is doubly small. For the abstract conditional lemma, the note should state: *metric comparability on $[0,3\delta]$ is assumed as part of (H2) and is maintained by short-time existence from smooth initial data; the lemma's output then extends it to $[0,T]$ for appropriate parameter choices.*

---

## 8. Intermediate Formula Correction (Section 6.2)

The note's equation (6.2) states

$$
\int_0^T\!\!\int_{W_3}F^3 \le C_B(1+K_0)^{3/2}\frac{\operatorname{Vol}(W)^2}{a_0}.
$$

From the parabolic interpolation applied to Step A outputs:

$$
\int_0^T\!\!\int F^3 \le C\bigl(\sup_t\textstyle\int F^2\bigr)^{1/2}\!\cdot\int_0^T\!\!\int|\nabla F|^2 \le C\bigl[C_A(1{+}K_0)\operatorname{Vol}(W)\bigr]^{1/2}\!\cdot\frac{C_A(1{+}K_0)\operatorname{Vol}(W)}{a_0},
$$

giving $C(1+K_0)^{3/2}\operatorname{Vol}(W)^{3/2}/a_0$. The volume power should be $\mathbf{3/2}$, **not** $2$.

**Impact on the rescaled bound (6.3):** Converting to rescaled variables ($d\tilde\mu=\ell^{-4}d\mu$, $dt=(\ell^2/a_0)d\tilde t$):

$$
\int_0^{\tilde T}\!\!\int_{\tilde B_{1/4}}F^3\,d\tilde\mu\,d\tilde t = \frac{a_0}{\ell^6}\int_0^T\!\!\int F^3\,d\mu\,dt \le \frac{C(1+K_0)^{3/2}\operatorname{Vol}(W)^{3/2}}{\ell^6}.
$$

By BG upper bound ($\operatorname{Ric}\ge-(n-1)g$ implies $\operatorname{Vol}(B_\ell)\le C\ell^4$ for $n=4$):

$$
\frac{\operatorname{Vol}(W)^{3/2}}{\ell^6}\le\frac{(C\ell^4)^{3/2}}{\ell^6}=C.
$$

The rescaled bound $\tilde C_B$ is finite and **independent of $\chi_0$ and collapsed volume**. The note's final rescaled result (6.3) is correct; only the intermediate unrescaled formula (6.2) has the wrong volume exponent. The paragraph after (6.3) attempting to trace the cancellation with $\operatorname{Vol}^2\sim\ell^8$ should use $\operatorname{Vol}^{3/2}\sim\ell^6$ instead.

---

## 9. Rescaled-Variable Consistency Audit

Three key rescaled quantities that must be $\chi_0$-independent:

| Quantity | Rescaled form | $\chi_0$-dependence |
|---|---|---|
| Flow time $\tilde T=a_0T/\ell^2$ | $\theta/c^2$ | None ✓ |
| Sobolev product $\tilde\gamma=A_W^2\|F\|_{L^2(\tilde B_1,\tilde\mu)}$ | $A_W^2\cdot\ell^{-2}\|F\|_{L^2(W)}$ | Cancels via BG (Section 3) ✓ |
| Cutoff potential $|\tilde\nabla^2\tilde a|$ | $\ell^2|\nabla^2(a/a_0)|$ | $= O(c^2)$ ✓ |

The first: $a_0T/\ell^2=\chi_0^2\theta r^2/(c^2r^2\chi_0^2)=\theta/c^2$. ✓

The third: $|\nabla^2 a|=|2\chi\nabla^2\chi+2|\nabla\chi|^2|\le C/r^2$ (assuming $|\nabla^2\chi|\le C/r^2$), so $\ell^2|\nabla^2(a/a_0)|=(\ell^2/a_0)|\nabla^2 a|\le c^2r^2\cdot C/r^2=c^2C$. ✓

The cutoff gradient term: $|\tilde\nabla\tilde a|=(\ell/a_0)|\nabla a|=(\ell/a_0)\cdot 2\chi|\nabla\chi|\le(cr\chi_0/\chi_0^2)\cdot 2(1{+}Lc)\chi_0\cdot L/r=2c(1{+}Lc)L$. ✓

All rescaled data are controlled by $c,L$ alone—no $\chi_0$ dependence survives.

---

## 10. Compatibility with A03's Weighted-Moment Hierarchy

The A03 note (Section 2) uses the weighted moments $H_q=\int\eta^2 a^{q-2}F^q$ and obtains the time-decay result $A^4H_3(t)\le C\gamma^3/t$. The note's Section 11 correctly identifies the equivalence:

- A03's backwards-averaging to find a good intermediate time $t_1$ with $H_3(t_1)\le C\gamma H_2(0)/t_1$, followed by forward propagation,
- is equivalent to the time-cutoff mechanism in Step C (using $\varphi=0$ for $t<\delta$).

The two formulations differ in presentation but produce the same analytical output: time-uniform spatial $L^3$ at positive time, with constants independent of the cutoff level.

One point of alignment: A03's equation (2.3) gives $A^4 H_3(t)\le C\gamma^3/t$, while Step 21's (7.2) gives $\int F^3 \le C_C/\tilde\delta$ in rescaled variables. These are consistent: $H_3\sim a_0\int F^3$ (since $a^{q-2}=a$ for $q=3$), and the time-decay $1/t$ maps to $1/\tilde\delta$ after rescaling.

---

## 11. Summary of Required Corrections

1. **Section 3 (BG comparison):** State the two-step concentric-ball comparison explicitly. The constant changes from $(c\chi_0/5)^4$ to $\tilde c_{\mathrm{BG}}(\ell/r)^4$; the $\chi_0$-cancellation and final bound are unaffected.

2. **Equation (6.2) (unrescaled spacetime $L^3$):** Replace $\operatorname{Vol}(W)^2$ by $\operatorname{Vol}(W)^{3/2}$. The rescaled bound (6.3) is already correct.

3. **Step D subsolution:** Make explicit the Young-inequality absorption of the gradient term $|\tilde\nabla a||\tilde\nabla\mathrm{Rm}||\mathrm{Rm}|$ into the dissipation, producing a zeroth-order remainder.

4. **Early-time metric drift (Section 13):** State that metric comparability on $[0,3\delta)$ either follows from the smooth initial data and short-time existence, or is part of the provisional hypothesis (H2) that is then extended by the lemma's output.

None of these corrections invalidate the lemma's conclusion. Items 1, 3, 4 are expositional gaps; item 2 is an arithmetic error in an intermediate formula whose final output is unaffected.

---

## 12. Verification of the Python Script

The script `step21_finite_exponent_smoothing.py` correctly verifies:

- $p^*=2(n+2)/n=3$ for $n=4$ (Section 1). ✓
- Supercritical condition $3>n/2=2$ (Section 2). ✓
- $\chi_0$-independence of the BG transfer $\ell^4\fint F^2$ (Section 3 loop). ✓
- $\gamma=c^2r^2\sqrt{1+K_0}\approx 1.1\times 10^{-6}$ for the stated parameters (Section 3). ✓
- Absorption thresholds $q^2\gamma/4<0.1$ for $q=2,3$ (Section 4). ✓
- Rescaled time $a_0T/\ell^2=\theta/c^2$ independent of $\chi_0$ (Section 5 loop). ✓

The script is a sound numerical sanity check of the exponent and scaling arithmetic. It does not verify the PDE estimates themselves (those are analytical).