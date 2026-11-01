# TTCS Independent Branch Record

```json
{
  "step_id": 41,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step41_corrected_restricted_defect_gap_theorem.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A01/workspace/notes/step40_preceptor_review_step39_interfaces.md"
  ]
}
```

## Task

Read the corrected restricted negative defect gap theorem note (step41_corrected_restricted_defect_gap_theorem.md), focusing on §3 (zero-order unweighted T∈L^p lemma) and §4 (structural equations for the staggered induction). Verify:

1. §3 ZERO-ORDER T LEMMA: Under |U|=|aT|≤K, does the reaction bound a|T|^{p+1} ≤ K|T|^p actually follow? Is the G-evolution term |∂_tG| ≤ Ca|T| correct given ∂_tG = -2a(E⊛g)/(n-1) and E=Ric(T)? Does the Hessian-cutoff signed IBP actually remove the ∇²χ dependence? Is the additive C'_p term genuinely harmless for the continuation application (which only needs finiteness, not multiplicative Gronwall)? Are there missing terms?

2. §4 STRUCTURAL EQUATIONS: Is it true that ∇G=0 because ∇g=0? Does ∇^jT = ∇^jRm for j≥1 follow? In the expansion of ∇^{r+1}a = Σ C_s·C_t (s+t=r+1), is it correct that only the s=0 and t=0 terms use C_{r+1}? Does the cutoff-jet evolution ∂_t C_m (equation 4.6) genuinely avoid C_m and U_m in its RHS? Does ∂_tΓ = g^{-1}*∇Ric(U) introduce at most one derivative of U? Are the dangerous terms (4.12) correctly identified?

3. INTERACTION WITH A03 INDUCTION: Does the structural analysis genuinely show that A03's staggered ordering T_0→(U_1,C_2)→T_1→... has no upward dependencies? Are there additional terms from the Kulkarni-Nomizu product, commutators, or normalization that could defeat the induction?

Provide a direct scientific memo identifying any errors, missing terms, or gaps.

## Output

## Verification memo — §3 and §4 of step41_corrected_restricted_defect_gap_theorem.md

Focus: the zero-order unweighted $T\in L^p$ lemma (§3) and the structural evolution equations feeding the A03 staggered induction (§4). I worked each requested algebraic point from the tensor definitions. Overall the two sections are mathematically sound in their load-bearing content; I found no term that defeats them, but there are two harmless missing pieces of bookkeeping, one muddled non-load-bearing paragraph, and one place where the enumeration in §4 is incomplete relative to what actually drives the argument. Details below.

---

### 1. §3 zero-order lemma

**Reaction bound $a|T|^{p+1}\le K|T|^p$ — correct.**
Because $a=\chi^2\ge0$ is a scalar, $|U|=|aT|=a|T|$, so $a|T|\le K$ pointwise everywhere (including near buffer edges, since $|U|\le K$ is a global sup bound). Then $a|T|^{p+1}=(a|T|)|T|^p=|U|\,|T|^p\le K|T|^p$, and likewise $a|T|^{p-1}=|U|\,|T|^{p-2}\le K|T|^{p-2}$. Both lines of (3.7) hold. This step also silently relies on the Hamilton quadratic $\mathcal Q$ carrying the factor $a$; that is genuine — under $\partial_t g=-2aE$ the algebraic curvature-times-curvature terms arise from $\operatorname{Rm}\star h=-2a\,\operatorname{Rm}\star E$, so the reaction is weighted by $a$ (consistent with Step 35 §2.1 Type P). Without that $a$-weight the bound would not close, so it is worth stating explicitly rather than folding into "$|Q(T-G)|\le C(|T|^2+1)$."

**G-evolution bound $|\partial_t G|\le Ca|T|$ — correct.**
$\partial_tG=\dfrac{\partial_tg\owedge g+g\owedge\partial_tg}{2(n-1)}=\dfrac{-2a\cdot2(E\owedge g)}{2(n-1)}=-\dfrac{2a}{n-1}E\owedge g$ (Kulkarni–Nomizu symmetry $E\owedge g=g\owedge E$). Then $|E\owedge g|\le C|E|$ and $|E|=|\operatorname{Ric}(T)|\le C|T|$, giving $|\partial_tG|\le Ca|T|$. The identification $\mathcal N=-2a(T-G)-\frac{2a}{n-1}E\owedge g$ in (3.5) is consistent with Step 35 (Type N gives $-2a\operatorname{Rm}=-2a(T-G)$ into $\partial_t\operatorname{Rm}$, plus $\partial_tG$ into $\partial_tT$). Both pieces of $\mathcal N$ obey $|\mathcal N|\le Ca|T|+Ca$, as stated.

**Hessian-cutoff signed IBP removes $\nabla^2\chi$ — valid, but the (3.9) text imports a spurious object.**
$\nabla^2a=2\chi\nabla^2\chi+2\nabla\chi\otimes\nabla\chi$; the $\nabla^2\chi$ piece is $\nabla(\nabla\chi)$, and integrating by parts on the closed manifold moves that derivative onto the factors $|T|^{p-2}$, $T$, $E$ (giving $\nabla T$, and $\nabla E=\nabla\operatorname{Rm}=\nabla T$ since $\nabla G=0$), or $\chi$ (giving $\nabla\chi$). Every resulting term carries $\nabla\chi$, never $\nabla^2\chi$, and Young against the diffusion $\int a|T|^{p-2}|\nabla T|^2$ leaves $\varepsilon D+C r^{-2}\int|T|^p$. So the mechanism works. **However**, the sentence in (3.9) — "the derivative hits $\eta=1$ (vanishing on $\operatorname{supp}\nabla\eta$ by the collar)" — is copied from the *weighted* Step 35 setting. In the unweighted §3 lemma there is no $\eta$ cutoff at all; the IBP is clean precisely because $M$ is closed and $\int_M\nabla(\cdots)=0$ identically. The $\eta$-collar reference should be deleted here to avoid the false impression that a second cutoff is doing the work.

**A missing (harmless) term: the inverse-metric variation of the norm.**
Step A only records the volume-form variation $\partial_t(d\mu)=-a\tau\,d\mu$. But $\frac{d}{dt}|T|^2$ also picks up $\partial_t g^{-1}=2aE^{\bullet\bullet}$ from raising the four indices in $|T|^2=g^{-1}\!\otimes\!\cdots\!\otimes\!g^{-1}(T,T)$. This contributes $\sim a\,E\star T\star T\le Ca|T|^3=C|U|\,|T|^2\le CK|T|^2$, i.e. after $\tfrac p2|T|^{p-2}\partial_t|T|^2$ a term $\le CpK\int|T|^p$. It is absorbed into the RHS coefficient of (3.10) and does not change the result, but it is a genuine contribution not displayed in Step A or Step B and should be listed for completeness. Testing (3.4) with $p|T|^{p-2}T$ captures only $\langle T,\partial_t T\rangle$, not this metric-of-the-inner-product variation.

**Additive $C'_p(K)$ is genuinely harmless for the continuation use.**
The application needs only finiteness of $\|T\|_p$ on $[\tau,T_*)$. Under $|U|\le K$ one has $|\partial_t g|=2|\operatorname{Ric}(U)|\le CK$, hence bilipschitz comparison on any finite interval and bounded $\operatorname{Vol}(g(t))$; therefore $C'_p(K)$ stays finite up to $T_*$ even if $T_*<\infty$. Gronwall (3.2) with the additive term then gives $\|T(t)\|_p<\infty$ throughout, which is exactly what excluding a finite maximal time requires. The reasoning here is correct.

**One non-load-bearing paragraph should be cleaned.**
The "Homogeneity at $E=0$" discussion (asserting $a\Delta T$ and $aQ$ "cancel when $T$ is parallel and the curvature is that of a space form") is at best imprecise: $E=0$ holds at points, not identically, so there is no pointwise freezing argument, and the stated cancellation is not demonstrated. The note itself then says the relevant fact "is not algebraic homogeneity but the bound." Since nothing downstream uses this paragraph, it is best removed; as written it could be read as an argument that is not actually made.

---

### 2. §4 structural equations

**$\nabla G=0$ from $\nabla g=0$ — correct.** $\nabla(g\owedge g)=(\nabla g)\owedge g+g\owedge(\nabla g)=0$ by metric compatibility, so $\nabla G=0$, $\Delta G=0$.

**$\nabla^jT=\nabla^j\operatorname{Rm}$ for $j\ge1$ — correct**, immediate from $\nabla^jG=0$.

**Expansion $\nabla^{r+1}a=\sum_{s+t=r+1}\binom{r+1}{s}C_sC_t$, only $s=0$/$t=0$ carry $C_{r+1}$ — correct.** $C_{r+1}$ appears only in $(s,t)=(r+1,0)$ and $(0,r+1)$, combining to $2\chi C_{r+1}$; every other summand has $s,t\le r$. This is the key fact that keeps $C_{r+1}$ (the current jet) isolated, and it holds.

**Cutoff-jet evolution (4.6) avoids $C_m$ — correct; note that it does reach $U_m$.** $\partial_tC_m=-\sum_{j=1}^{m-1}\nabla^{j-1}(\partial_t\Gamma)\star C_{m-j}$: the highest cutoff index is $C_{m-1}$ (at $j=1$), so no $C_m$. Its highest curvature content, at $j=m-1$, is $\nabla^{m-2}(\partial_t\Gamma)\star C_1\sim\nabla^{m-1}\operatorname{Ric}(U)\star C_1\sim U_{m-1}\star C_1$ — so $\partial_tC_m$ reaches $U_{m-1}$, and correspondingly $\partial_tC_{m+1}$ reaches $U_m$ (the current variable). This is why $(U_m,C_{m+1})$ must be closed as a *coupled* pair via A03 (2.10)–(2.11) rather than sequentially; the note's grouping is consistent with this.

**$\partial_t\Gamma=g^{-1}\star\nabla\operatorname{Ric}(U)$ gives one derivative of $U$ — correct.** $\operatorname{Ric}(U)$ is a trace contraction of $U$ (no derivatives), so $\nabla\operatorname{Ric}(U)=\operatorname{Ric}(\nabla U)$ carries exactly one derivative; equivalently $\nabla(aE)=\nabla a\cdot E+a\nabla E$, whose curvature order is $U_1$.

**Dangerous-term enumeration (4.12) is incomplete as stated.** The listed "only terms containing $C_{m+2}$ or higher cutoff jets" are $\chi C_{m+2}U_0$ and $C_1C_{m+1}U_0$. That statement about $C_{m+2}$ (strictly above the current jet) is correct. But the term that actually broke Step 39 and forces A03's extra integration by parts is $\chi\,C_{m+1}\star U_1$ — the *current* jet $C_{m+1}$ against $U_1$ — which is not in the (4.12) list. It is present: from the degenerate diffusion $a\Delta U_m$ acting on the $C_m\!\cdot\!T$ piece of $U_m=\nabla^m(aT)$, one gets $\Delta(C_mT)=C_{m+2}T+2C_{m+1}T_1+C_mT_2$, so $aC_{m+1}T_1$ (equivalently the $\chi C_{m+1}U_1$ term of A03 (2.6)) appears. The note does acknowledge it obliquely — §4.4's closing sentence mentions "the single dangerous current-cutoff-jet term handled by one additional integration by parts," and §4.5 refers to A03 Prop 3.1 — so this is not a mathematical omission, but the self-contained accounting in (4.12) surfaces the $C_{m+2}$ pieces while leaving the genuinely critical current-jet term to a cross-reference. Anyone reading §4.4 in isolation would miss the term that is the whole point of the A03 repair.

**A power-of-$\chi$ bookkeeping point to confirm.** The diffusion source of the top jet is $a\,C_{m+2}\,T=\chi^2 C_{m+2}T$, whereas the note writes it as $\chi C_{m+2}\cdot U_0$. Since $U_0=aT=\chi^2T$, "$\chi C_{m+2}U_0$" reads as $\chi^3C_{m+2}T$, one power of $\chi$ higher than the $\chi^2C_{m+2}T$ actually produced by $a\Delta$. This is exactly the delicate accounting A03 explicitly warns against ("no derivative of $a=\chi^2$ assigned a nonexistent $\chi$ factor"). The IBP still closes either way (an extra bounded $\chi\le1$ only helps), but the exact weight should be written correctly, because the whole difference between the working staggered scheme and the discarded $L^{2p}$ loop lives in these powers.

---

### 3. Interaction with the A03 staggered ordering

**No upward dependency — established at the derivative-counting level.** The counting (4.11), together with the isolation of $C_{r+1}$ in (4.5d) and the fact that $\partial_tC_{m+1}$ reaches at most the current $U_m$, does show that stage $m$ never calls a variable above the current pair $(U_m,C_{m+1})$ and current $T_m$. That structural conclusion is correct.

**Kulkarni–Nomizu introduces no new derivative branch — correct.** For $j\ge1$, $\nabla^j(aG)=\sum_s\binom js\nabla^sa\,\nabla^{j-s}G=(\nabla^jа)G$ since $\nabla^{j-s}G=0$ unless $s=j$; so $G$ enters only as a cutoff jet times the bounded constant tensor $G$. No derivative of curvature comes from $G$.

**Commutator curvature terms are controlled — but by the §3 lemma, and this dependency is real.** Spatial commutators $[\nabla_i,\nabla_j]$ generate $\operatorname{Rm}\star(\cdot)$, i.e. $T_0\star U_{m-1}$-type products. $T_0=\operatorname{Rm}$ is only in $L^q$ (not $L^\infty$), so these are handled by Hölder with enlarged exponents *using* the zero-order $T\in L^q$ conclusion of §3. This is a genuine forward dependency: §4/A03 cannot close without the §3 lemma supplying $T_0\in L^q$ for all finite $q$. The two sections are correctly chained, but the reader should see that the "reactions bounded by previously established lower levels" in §4.4 include curvature factors whose finiteness is exactly the §3 output.

**Normalization introduces no new branch — correct.** $-2a(T-G)$ and $\partial_tG$ are algebraic in $T,a$; their $\nabla^m$ produces $\nabla^sa\star\nabla^{m-s}T$ with cutoff order $\le m$ and $T$-order $\le m$, all current-or-lower.

---

### 4. Standing of §3–§4 and what still needs explicit derivation

The load-bearing algebra of §3 (reaction, G-evolution, Hessian IBP, finiteness under the additive term) is correct, subject to inserting the inverse-metric norm term and removing the stray $\eta$-collar wording. The structural facts of §4 (parallelism of $G$, jet isolation, single-derivative $\partial_t\Gamma$, no upward dependency by counting) are correct.

What §4 supplies is a *derivative-counting* verification that the A03 schematic evolutions (1.4)–(1.5) have no upward dependency. It does not by itself carry the explicit coefficients, and in one place ((4.12) versus the actual $\chi C_{m+1}U_1$ term, and the $\chi^2$ vs $\chi^3$ weight) it is looser than the A03 note it defers to. The estimability of each classified term — in particular that the current jet occurs only at exponent $p$ and never at $2p$ after the extra IBP — is proved in A03 §2.2–§4, not reproduced here. So §4's function is to certify the *shape* of the equations that A03 assumes; the quantitative closure remains A03's, and the exact evolution formulae with correct coefficients (the object the earlier interface review asked for) are given schematically rather than derived term-by-term. The chain §3 → §4 → A03 is internally consistent, and I found no term that overturns (3.10), the staggered ordering, or the A03 inequalities (2.9), (2.11), (3.6); the items above are corrections of exposition and one incomplete enumeration, not defeats of the mathematics.

Everything in §3–§4 is conditional on a smooth solution existing on the positive-time slab, i.e. on the transported-coefficient degenerate short-time construction of §5.1, which the note marks as not yet written. That conditioning sits outside §3–§4 but bounds what these two sections can be said to establish on their own.