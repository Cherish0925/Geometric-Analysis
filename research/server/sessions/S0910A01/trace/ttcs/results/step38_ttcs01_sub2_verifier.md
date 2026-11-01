# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step38_continuation_repair_and_support_normalization.md",
    "Sessions/S0910A01/workspace/scripts/step38_continuation_support_verify.py",
    "Sessions/S0910A01/trace/ttcs/results/step37_ttcs01_verifier1_integration.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A03/workspace/notes/step39_general_p_defect_power_inequality.md"
  ]
}
```

## Task

Verify the mathematical content of `step38_continuation_repair_and_support_normalization.md` in the restricted four-dimensional negative Yau-26 route. Focus on four questions: (1) Does the note correctly identify the failure of Step 37 Lemma 1.2a from the degeneracy of a=chi^2 and the fact that |U| only gives |aE|, not chi^2-small drift? (2) Is the proposed repair direction faithful to Wang Lemmas 4.5, 4.6, Proposition 4.13, and Proposition 4.14: weighted shifted equation for U=a(Rm+G), separate unweighted curvature-derivative module, finite Hölder exponents, and smooth terminal recovery via dt g=-2 Ric(U)? (3) Are there hidden derivative, cutoff, G/normalization, or exponent gaps in the sketched estimates that would still block a continuation theorem? (4) Is the support-selection normalization correct: volume-average maximal function, large threshold for retained volume, small fixed radius for r^4 average smallness, Sobolev-volume cancellation, and Vol/A lower from calibration rather than Euler upper bound? Give a scientific verification/critique and concrete repairs, not a route decision.

## Output

# Verification Memo — Step 38 continuation repair and support normalization (four-dimensional Ishida–LeBrun setting, $\lambda<0$ branch)

## Summary judgment

The note's central corrections are mathematically sound. The identification of why the Step 37 Lemma 1.2a is withdrawn is correct and I reproduce it below. The proposed repair direction is a faithful reading of Wang's actual induction order. The support-selection normalization is algebraically and structurally correct, and is a genuine improvement over the earlier $r^{-4}\int$/$r^4\int$ constructions. The unfinished analytic content is real but is smaller and more concrete than the note's cautious phrasing suggests: at level $m=2$ the delicate $\Gamma_3$ term is in fact closeable with tools already in hand, and I give the closure explicitly. The genuinely open analytic objects are the full tensor expansion of (1.2) with commutators and shift/normalization terms, the shifted terminal-recovery statement, and the transported-coefficient short-time existence for restart.

---

## Q1 — Withdrawal of Step 37 Lemma 1.2a: correct

$U=aT$, $T=\operatorname{Rm}+G$, and $\operatorname{Ric}$ is a linear contraction, so
$$\operatorname{Ric}(U)=\operatorname{Ric}(aT)=a\operatorname{Ric}(T)=aE,\qquad |\operatorname{Ric}(U)|\le C|U|\le CK .$$
This gives $|aE|\le CK$, **not** $|aE|\le CaK=C\chi^2K$. The model $a=\varepsilon^2$, $T\sim a^{-1}$, $U=1$, $aE\sim1$ while $aK=\varepsilon^2$ makes the point sharp: in $\{\chi<\delta\}$ the flow velocity $|aE|=|\partial_t g|/2$ is bounded but not quadratically small in $\chi$. A bounded $C^0$ metric displacement therefore cannot recover $\nabla^k\operatorname{Rm}$ from $\nabla^kU$ in the transition region by dividing by $a$. The companion point — that fixed coordinate derivatives of $\chi$ do not control the evolving covariant jets $\nabla^j\chi$, because $\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)$ couples the connection — is also correct and is exactly Wang's Lemma 4.6 mechanism. The surviving facts (metric bilipschitz control by the logarithmic estimate $|\tfrac{d}{dt}\log g_t(v,v)|\le CK$, and zero-order $L^p(\operatorname{Rm})$ propagation by the Lemma 4.10 mechanism) are consistent with the step37 integration memo.

---

## Q2 — Faithfulness to Wang 4.5, 4.6, 4.13, 4.14: direction is correct

The staggered order stated in §1,
$$\text{weighted }\nabla^mU \;\Longleftrightarrow\; \text{cutoff jets }\nabla^j\chi \;\Longleftrightarrow\; \text{unweighted }\nabla^j\operatorname{Rm},$$
matches Wang Remark 4.2 exactly. The decisive structural fix relative to Step 37 is visible in (1.2): the high-cutoff line carries $\nabla^kU$, not unweighted $\nabla^k\operatorname{Rm}$ — the shifted image of Wang Lemma 4.5's $\nabla^k(\chi^2\operatorname{Rm})$. Because $\nabla G=0$ ($G=\tfrac{g\owedge g}{2(n-1)}$, $\operatorname{Ric}(G)=g$, so $\operatorname{Ric}(T)=\operatorname{Ric}+g=E$; the $n=4$ form $G=g\owedge g/6$ is consistent), the shift and normalization enter only as cutoff-jet times parallel $G$ and lower curvature times $a$. The dependency graph
$$\text{Prop 4.13}(m{-}1)\to Y_m\ (\nabla^mU,\nabla^{m+1}\chi)\to\text{Prop 4.13}(m)\to Y_{m+1}$$
has no circularity: $Y_m$'s reaction (1.2) contains $\nabla^k\operatorname{Rm}$ only for $k\le m-1$, and Prop 4.13$(m)$ consumes $\nabla^{m+1}\chi$ (from $Y_m$) together with $\nabla^{m-1}\operatorname{Rm}$. The separation of the unweighted curvature-derivative module from the weighted equation, the insistence that it cannot be obtained by division by $a$, and the recovery of the terminal metric through $\partial_t g=-2\operatorname{Ric}(U)$ are all correct in intent.

One item is stated rather than proved: the smooth-terminal recovery in §4/§6 is the shifted analogue of Wang Proposition 4.3. From $\{\|\nabla^mU\|_\infty\}_m$ bounded plus $\partial_t g=-2\operatorname{Ric}(U)$, $\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)$, smooth convergence of $g(t)$ in fixed charts to a positive-definite limit is plausible and the normalization terms are lower-order, but the shifted Proposition 4.3 has not been written.

---

## Q3 — Hidden derivative/cutoff/exponent structure

**(a) The $\Gamma_3$ term at $m=2$ is closeable — the note's stated justification can be strengthened.** The note bounds $\Gamma_3=\chi\nabla^{m+1}\chi*\nabla U$ for $m\ge2$ by asserting $\|\nabla U\|_\infty$ is a lower-level quantity. That $L^\infty$ bound is not directly available at $m=2$, since Sobolev embedding of $\nabla U$ needs $\nabla^2U=V_2$, the current level. But the term does not require it. Testing against $|V_2|^{p-2}V_2$ and integrating one derivative off $\nabla^3\chi=\nabla(\nabla^2\chi)$ leaves the level-1 jet $\nabla^2\chi=Z_1$, not $\nabla^3\chi$:

- derivative on $|V_2|^{p-2}V_2$: $\displaystyle\int|V_2|^{p-2}\nabla V_2\,\chi\,\nabla U\,\nabla^2\chi \le \varepsilon\!\int a|\nabla V_2|^2|V_2|^{p-2}+C\!\int|V_1|^2|Z_1|^2|V_2|^{p-2}$, and $\int|V_1|^2|Z_1|^2|V_2|^{p-2}\le\|V_1\|_{2p}^2\|Z_1\|_{2p}^2\|V_2\|_p^{p-2}$ with $\tfrac{2}{2p}+\tfrac{2}{2p}+\tfrac{p-2}{p}=1$. Both $\|V_1\|_{2p}$, $\|Z_1\|_{2p}$ are finite for all finite exponents from the §2 base pair;
- derivative on $\nabla U$: $\nabla^2U=V_2$ (current), surviving cutoff $\nabla^2\chi=Z_1$, giving $\int\chi\,\nabla_i\nabla_j\chi\,B^{ij}(V_2)$ with $B=|V_2|^{p-2}V_2*V_2$, $|B|\le|V_2|^p$, $|\nabla B|\le|V_2|^{p-1}|\nabla V_2|$ — exactly the A03 Step 38 signed Hessian form, bounded by $\varepsilon\int a|\nabla V_2|^2|V_2|^{p-2}+Cr^{-2}\|V_2\|_p^p$;
- derivative on $\chi$: $d\chi*Z_1$, lower.

So $m=2$ closes on the base pair (all finite exponents) plus the signed Hessian lemma, without $\|\nabla U\|_\infty$. For $m\ge3$ the surviving cutoff is $\nabla^m\chi=Z_{m-1}$ (level $m-1$, all exponents) and the $\nabla^2U$ sub-term is genuinely lower-level. This makes the note's $\Gamma_3$ statement rigorous and removes the one place where an unweighted pointwise quantity looked necessary.

**(b) Exponent inflation is consistent but must be scheduled.** Prop 4.13$(m)$ uses $\|\nabla^{m+1}\chi\|_{2p}$ and $\|\operatorname{Rm}\|_{2p}$ (see (3.4): $\tfrac{2}{2p}+\tfrac{2}{2p}+\tfrac{p-2}{p}=1$), and $Y_m$ closure at exponent $2p$ feeds back into higher exponents. This $p\to2p$ inflation is absorbed only if every level is proved for all finite exponents simultaneously, precisely as Wang runs "$\forall q>100$." The §3 hypotheses ("for all finite exponents needed") are compatible with this; the explicit per-term exponent table is the bookkeeping that remains, and it is believed routine given (a) and the base pair.

**(c) The full expansion of (1.2) is the real remaining analytic content.** The note has verified the finite-exponent estimates *conditional on* the top structures being exactly $\Gamma_1$–$\Gamma_4$ (with $U$, not unweighted $\operatorname{Rm}$) and the reaction not exceeding $\nabla^{m-1}\operatorname{Rm}$. It has not expanded (1.2) from the linearized-curvature variation of the shifted normalized flow $\partial_t g=-2aE=-2a\operatorname{Ric}-2ag$. Two mechanisms must be tracked and shown lower-order: the $-2ag$ shift contributes $\nabla^2(a)\,g$ (a cutoff Hessian jet) and $a\,\operatorname{Rm}*g$; and the non-commuting covariant derivatives generate commutator terms $\operatorname{Rm}*\nabla^{m-1}(\cdot)$ that A03 Step 38 §3 flags as possible sources of "unweighted lower $T$-derivatives." Until (1.2) is derived term by term, the closure is a dependency pattern, not a theorem — as the note itself states in §6.

**(d) Zero-order input.** The $\|\operatorname{Rm}\|_q^q$ term in (2.5) enters genuinely, from the $\nabla a*U*\operatorname{Rm}=2\chi\,d\chi*U*\operatorname{Rm}$ contraction (weight only $\sqrt a$, so $\sqrt a\,\operatorname{Rm}$ is uncontrolled where $a\to0$ and one needs finite $L^q(\operatorname{Rm})$). This confirms the correct order: shifted Lemma 4.10 first, then the base pair. The shifted Lemma 4.10 with the $+g$ shift split (the step37 memo's Ric/g Hessian-$a$ splitting) should be written out; it is plausible but not fully recorded here.

**(e) Downstream dependencies.** The continuation theorem still rests on the shifted Proposition 4.3 (Q2) and on the normalized transported-DeTurck short-time existence needed to restart from the terminal metric (Step 36's tame estimates), neither proved.

---

## Q4 — Support-selection normalization: correct

- **Volume-average maximal function and retention.** $\mathcal M_Rf(x)=\sup_{s\le R}\fint_{B_s(x)}f$; the weak inequality $\operatorname{Vol}\{\mathcal M_R(|\operatorname{Rm}|^2)>\Lambda K_0\}\le\tfrac{C_D(R)}{\Lambda}\operatorname{Vol}M$ is the Hardy–Littlewood weak-$(1,1)$ bound with $\|{|\operatorname{Rm}|^2}\|_{L^1}=K_0\operatorname{Vol}M$ and local doubling $C_D(R)$ from Bishop–Gromov under $\operatorname{Ric}\ge-2g$. Correct. A large $\Lambda$ retains $G_R(\Lambda)$ of volume $\ge(1-C_D/\Lambda)\operatorname{Vol}M\ge\eta_0\operatorname{Vol}M$.
- **Critical smallness.** For $x\in G_R(\Lambda)$, $r\le R/10$, $\fint_{B_r}|\operatorname{Rm}|^2\le\Lambda K_0$, so $r^4\fint_{B_r}|\operatorname{Rm}|^2\le r^4\Lambda\overline K_0\le\varepsilon_{\mathrm{Li}}$. Note $r^4\fint_{B_r}|\operatorname{Rm}|^2=\tfrac{r^4}{\operatorname{Vol}B_r}\int_{B_r}|\operatorname{Rm}|^2$; this equals the scale-invariant dimension-four energy $\int_{B_r}|\operatorname{Rm}|^2$ only when $\operatorname{Vol}B_r\sim r^4$. The maximal-function selection plus the calibration volume ratio below supply exactly the non-collapsing that identifies $r^4\fint$ with Wang's $\varpi(n,\eta)$-type threshold; this identification should be stated where the $\digamma$ assumption is invoked.
- **Sobolev–volume cancellation.** With $\mathcal S\sim Cr^2/\operatorname{Vol}(B_{R_0r})^{1/2}$ and $K_2^\eta\le(1+\Lambda\overline K_0)\operatorname{Vol}(B_{R_0r})$, $\mathcal S(K_2^\eta)^{1/2}\le Cr^2(1+\Lambda\overline K_0)^{1/2}$, independent of the (possibly collapsing) volume. Algebraically exact.
- **Volume/topology ratio from calibration.** The terminal identities $\int(s+4)^2=o(A)$, $\int(s+8\sqrt6|W^+|)^2=o(A)$ force $s\to-4$, $|W^+|\to\tfrac{1}{2\sqrt6}$, hence $\tfrac{s^2}{24}+2|W^+|^2\to\tfrac23+\tfrac1{12}=\tfrac34$ in average, giving $\tfrac34\operatorname{Vol}(M_i)=4\pi^2I_i+o(A_i)=\tfrac{8\pi^2}{3}A_i+o(A_i)$ and $\operatorname{Vol}(M_i)/A_i\to\tfrac{32\pi^2}{9}$. Correct. The insistence on a two-sided calibrated identity (rather than an Euler-characteristic upper bound) is the right point: $\chi(M)$ bounds curvature combinations but does not bound $\operatorname{Vol}$ from below, and it is the lower bound $\operatorname{Vol}\gtrsim A$ that converts retained good volume into $A$-proportional plateau volume.
- **Coloring.** The net + Bishop–Gromov packing + finite coloring into a macro-disjoint color with $\sum\operatorname{Vol}(P_\alpha)\ge\alpha A_i$ is structurally sound; the color number $N(n)$ (Besicovitch/Vitali under $\operatorname{Ric}\ge-2g$) and the packing constant should be named explicitly, since the script lists "real covering constants" as unfinished.

---

## Concrete repairs

1. Replace the $\Gamma_3$ justification for $m\ge2$ by the IBP-lowering argument in Q3(a): the surviving jet is $\nabla^m\chi$ (level $m-1$, all exponents), the $|V_2|^{p-2}V_2$-branch pairs level-1 quantities in $L^{2p}$, and the $\nabla^2U$-branch at $m=2$ is the signed Hessian form. This removes any appeal to $\|\nabla U\|_\infty$.
2. Derive (1.2) explicitly from the curvature variation of $\partial_t g=-2a\operatorname{Ric}-2ag$, tracking (i) the $-2ag$ contributions $\nabla^2(a)g$ and $a\,\operatorname{Rm}*g$, and (ii) the $[\nabla^m,\Delta]$ commutators, and confirm the top line is exactly $\Gamma_1$–$\Gamma_4$ in $U$ and the reaction stops at $\nabla^{m-1}\operatorname{Rm}$.
3. Write the shifted Proposition 4.3: from $\{\|\nabla^mU\|_\infty\}$ bounded, smooth convergence of $g(t)$ in fixed charts via $\partial_t g=-2\operatorname{Ric}(U)$, $\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)$.
4. Record the shifted Lemma 4.10 with the Ric/g Hessian-$a$ split so the zero-order $\|\operatorname{Rm}\|_q$ input in (2.5) is a proved module.
5. Supply the normalized transported-DeTurck short-time existence for restart.
6. In §5, state $r^4\fint$ vs. scale-invariant $\int_{B_r}|\operatorname{Rm}|^2$ matching through the calibrated non-collapsing, and name $N(n)$, $c_{BG}$ explicitly.

## What remains open

The finite-exponent estimates, the Hölder/Young arithmetic (base pair $2/p+(p-2)/p=1$; Prop 4.13 model $2/(2p)+2/(2p)+(p-2)/p=1$; $N$-factor $N/(Np)+(p-1)/p=1$), the Sobolev–volume cancellation, and the calibrated ratio $32\pi^2/9$ are all internally consistent. The continuation theorem is not yet a theorem: item 2 (term-by-term expansion with commutators and shift terms) is the substantive analytic content, and items 3–5 are the downstream analytic inputs. Even a complete continuation theorem here addresses only the four-dimensional $\lambda<0$ Ishida–LeBrun setting, not the full Yau-26 proposition, the $\lambda>0$ branch, $n\ge5$, dimension-only constants, or the Lean formalization.