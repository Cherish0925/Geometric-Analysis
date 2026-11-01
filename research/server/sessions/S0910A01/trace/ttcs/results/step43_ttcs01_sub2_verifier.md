# TTCS Independent Branch Record

```json
{
  "step_id": 43,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step43_H_WU_resolution_weighted_evolution.md",
    "Sessions/S0910A01/workspace/notes/step42_uniform_gap_weight_terminal_repairs.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md"
  ]
}
```

## Task

Verify the H-WU resolution for the weighted cutoff flow U_m = nabla^m(chi^2(Rm+G)) under dt g = -2 chi^2 (Ric+g). The central claim (Proposition §5) is: in the evolution equation for U_m, the UNIQUE source of the single cutoff jet C_{m+2} = nabla^{m+2}chi is from the Hessian-a contraction in the Lichnerowicz variation, giving the form 2*chi*C_{m+2} * (aE) plus products of lower jets. All other terms (commutator, G-variation, normalization, reaction, outer Leibniz j>=1) produce single jets of order <= m+1. Verify: (1) The product-rule identity nabla^k(chi^2) = sum_{s=0}^k C(k,s) C_s C_{k-s} and its top jet 2*chi*C_k. (2) The factorization a*(nabla^2 a)*E = (nabla^2 a)*(aE) and why this preserves chi weight after m derivatives. (3) The commutator bound max single jet = C_m from [dt, nabla^m]U. (4) That the chi factor in 2*chi*C_{m+2} is essential for pairing with weighted dissipation int chi^2|nabla U_m|^2|U_m|^{p-2} via Cauchy-Schwarz, and that bare C_{m+2} would fail. (5) Whether any curvature-commutator correction from reordering covariant derivatives in the Leibniz expansion could introduce an unaccounted C_{m+2} term.

## Output

# Verification Memo: H-WU cutoff-jet provenance for the weighted flow

## Summary judgment

The five sub-statements hold. Proposition §5 is a correct statement about **where the highest cutoff derivative $C_{m+2}=\nabla^{m+2}\chi$ can appear in $\partial_t U_m$ and with what $\chi$-weight**. It correctly certifies the single input that A03 Step 40 §2.2 assumes, namely that the sole $C_{m+2}$ allocation is $\Gamma_1=\chi C_{m+2}\star U$. Below I confirm each point, strengthen the one place where the note's reasoning is too terse (the commutator corrections, point 5), and describe precisely what this result does and does not deliver toward the flow argument.

One algebraic backbone worth recording, since everything downstream leans on it: with $G=\tfrac{g\owedge g}{2(n-1)}$ one has $\operatorname{Ric}(g\owedge g)=g^{jl}\cdot2(g_{ik}g_{jl}-g_{il}g_{jk})=2(n-1)g$, so $\operatorname{Ric}(G)=g$ and $\operatorname{Ric}(T)=\operatorname{Ric}+g=E$. Hence $\operatorname{Ric}(U)=\operatorname{Ric}(aT)=aE$ and $|aE|=|\operatorname{Ric}(U)|\le C_n|U|$. Every "$|aE|\le C|U|$" step in the note rests on this, and it is correct.

## (1) The scalar product identity and its top jet

$\nabla^k(\chi^2)=\sum_{s=0}^k\binom{k}{s}C_s\otimes C_{k-s}$ with top single jet $2\chi C_k$: correct **as a jet-order statement**. The iterated Leibniz rule for a scalar product is exact at each single derivative, so $\nabla_{i_1}\cdots\nabla_{i_k}(\chi\cdot\chi)=\sum_{S\subseteq\{1..k\}}(\nabla_S\chi)(\nabla_{S^c}\chi)$, each $\nabla_S\chi$ being a genuine order-$|S|$ covariant derivative with a specific index interleaving.

Two honest refinements the note should carry:
- The $\binom{k}{s}$ collapse of the $\binom{k}{s}$ subsets of size $s$ into one representative $C_s\otimes C_{k-s}$ is **schematic**, not a literal tensor equality: the interleavings give different index orderings of $\nabla^s\chi$. For $s\ge3$ these orderings differ by curvature commutators, e.g. $\nabla_i\nabla_j\nabla_k\chi-\nabla_j\nabla_i\nabla_k\chi=R_{ij}{}^l{}_k\,\nabla_l\chi=\mathrm{Rm}\star C_1$. These corrections carry a **lower** cutoff jet and are irrelevant to the top-jet count.
- Consequently the top single jet $2\chi C_k$ (the $s=0$ and $s=k$ terms) is robust; commutator corrections never contribute to it. For the $L^p$ energy argument, which uses magnitudes and jet orders rather than exact contractions, this schematic form is exactly what is consumed.

## (2) The factorization and $\chi$-preservation after $m$ derivatives

$a[(\nabla^2 a)\star E]=(\nabla^2 a)\star(aE)$ is exact because $\star$ is a pointwise metric contraction, $C^\infty(M)$-linear in each slot; the scalar $a$ moves freely into the second factor. Correct.

The mechanism producing the $\chi$-weight is sound and I verified it two independent ways for the unique $s=m$ term:
- **Direct:** $a\cdot\nabla^m((\nabla^2 a)\star E)$, $s=m$ term $=a\cdot(\nabla^{m+2}a)\star E$; top jet $a\cdot 2\chi C_{m+2}\star E=2\chi^3 C_{m+2}\star E$.
- **Factorized (note §4.2, 4.6):** $(\nabla^{m+2}a)\star(aE)$; top jet $2\chi C_{m+2}\star(aE)=2\chi C_{m+2}\star\chi^2E=2\chi^3C_{m+2}\star E$.

Both agree: the surviving top term is $2\chi^3 C_{m+2}\star E$. Written as $2\chi C_{m+2}\star(aE)$ with $|aE|\le C|U|$, it exhibits **one explicit $\chi$** paired to $C_{m+2}$, the remaining $\chi^2$ being absorbed into $aE=\operatorname{Ric}(U)$. This matches A03's $\Gamma_1=\chi C_{m+2}\star U$. In fact the raw term carries $\chi^3$, i.e. **more** $\chi$-weight than the argument needs; the note's framing is accurate and even a little generous.

The subtracted Leibniz remainder $-\sum_{j\ge1}\binom{m}{j}(\nabla^j a)\nabla^{m-j}((\nabla^2a)\star E)$ has, per term, max single jet $\max(j,\,m-j+2)$, which at $j=1$ is $m+1$ and never reaches $m+2$. Correct. So the identity in §4.2 is right and its purpose (routing the outer $a$ into $E$ so $\nabla^{m+2}$ lands wholly on one $\chi^2$) is achieved.

The structural input from §2 that makes all of this go through is: **the maximum cutoff-derivative order in $\partial_t T$ is two**, from $\nabla^2 h=\nabla^2(aE)=a\nabla^2E+2\nabla a\otimes\nabla E+(\nabla^2 a)E$ inside the Riemann/Lichnerowicz variation, since $\delta\Gamma\sim g^{-1}\nabla h$ and $\partial_t\mathrm{Rm}\sim\nabla\delta\Gamma\sim\nabla^2 h$. The $(\nabla^2 a)E$ piece is order 2 in $\chi$; the other two are orders 1 and 0. Confirmed. This is the load-bearing observation and it is correct.

## (3) The commutator $[\partial_t,\nabla^m]U$ gives max single jet $C_m$

Confirmed. $\partial_t\Gamma=\tfrac12 g^{-1}\nabla h=-g^{-1}\nabla(aE)=-g^{-1}[(\nabla a)E+a\nabla E]$ carries top cutoff jet $C_1$; there is no $\nabla^2 a$ in $\partial_t\Gamma$. Then $\nabla^l(\partial_t\Gamma)$ has top jet $C_{l+1}$ and the paired factor $\nabla^{m-1-l}U$ has top jet $C_{m-1-l}$. Over $0\le l\le m-1$ the maximum single jet is $\max(l+1,\,m-1-l)=m$, attained at $l=m-1$. So the commutator produces at most $C_m$, strictly below the $C_{m+1}$ of the outer-Leibniz $j=1$ term and far below $C_{m+2}$. Correct.

## (4) Essentiality of the $\chi$ factor for pairing with the weighted dissipation

Correct, and it holds with room to spare. The natural dissipation is the $\chi^2$-weighted one because the principal diffusion is $a\Delta U_m=\chi^2\Delta U_m$; integrating $\int\chi^2\Delta U_m:P(U_m)$ produces $-c\int\chi^2|\nabla U_m|^2|U_m|^{p-2}=-cD^U_{m,p}$. In the integration-by-parts of the top term, term (III) is $\sim\int\chi|C_{m+1}||aE||U_m|^{p-2}|\nabla U_m|$. Cauchy–Schwarz splitting off the dissipation density $\chi|\nabla U_m||U_m|^{(p-2)/2}$ gives
$$
|\mathrm{(III)}|\le\varepsilon\!\int\!\chi^2|\nabla U_m|^2|U_m|^{p-2}+C_\varepsilon\!\int\!|C_{m+1}|^2|aE|^2|U_m|^{p-2}=\varepsilon D^U_{m,p}+C_{\varepsilon,K}\!\int\!|C_{m+1}|^2|U_m|^{p-2}.
$$
The one $\chi$ is exactly the pairing factor: it converts $|\nabla U_m|$ into $\sqrt{D^U_{m,p}}$-density. With a bare $C_{m+2}\star(aE)$ (no $\chi$), term (III) would carry $|\nabla U_m|$ unweighted; absorbing it into $\varepsilon\int\chi^2|\nabla U_m|^2|U_m|^{p-2}$ would force a $\chi^{-2}$ factor on the remainder, which is unbounded as $\chi\to0$ across the transition annulus. So the weight is genuinely required, and it is present (indeed $\chi^3$ is available). Correct.

Where the closure actually depends on more than H-WU: the residual $C_{\varepsilon,K}\int|C_{m+1}|^2|U_m|^{p-2}\le C_{p,K}(\|C_{m+1}\|_p^p+\|U_m\|_p^p)$ needs the **current** jet $C_{m+1}\in L^p$, which is the coupled unknown of A03 Step 40's staggered pair, closed by adjoining the $C_{m+1}$-evolution (Step 40 eq. 2.10–2.11). H-WU certifies the dissipation-absorbable part (the single $\chi$); the completion of the pair is a separate matter carried by Step 40, not by this note. The division of labor is clean and correctly stated.

## (5) Curvature-commutator corrections cannot produce an unaccounted $C_{m+2}$

This is the sharpest point and the note's justification ("involve lower derivative orders of both factors plus curvature, hence strictly less than $C_{m+2}$") is correct but too terse to be self-contained. Here is the reason it is definitive, which the ledger should state explicitly.

First, the Leibniz expansion of $\nabla^m((\nabla^2 a)\star(aE))$ into $\sum_s\binom{m}{s}(\nabla^{s+2}a)\star\nabla^{m-s}(aE)$ is itself **exact** (no curvature terms): iterated Leibniz for a contraction commutes with the single covariant derivative at each step. Curvature enters only when one standardizes the interleaved derivative $\nabla_S(\nabla^2 a)$ (a genuine order-$(s+2)$ derivative of $a$) into $\nabla^{s+2}a$ plus corrections.

Second, the corrections obey **differential-order conservation**. Every commutator correction contains at least one curvature factor. Writing a generic correction as $\nabla^{t_1}\mathrm{Rm}\star\nabla^{r'}a$ (times bounded metric contractions), the total differential order is conserved: counting $\mathrm{Rm}$ as order 2, $(t_1+2)+r'=(m+2)$ at the top ($s=m$), so
$$
r'=m-t_1\le m.
$$
The cutoff jet lives only on the $a$-factor, so it is $C_{r'}\le C_m$. There is no way to reach $r'=m+1$ or $m+2$ (that would need $t_1=-1$ or $-2$). Equivalently: forming one curvature factor consumes two differentiation orders that would otherwise be available to load onto a single $\chi$, so **every commutator correction drops the cutoff-jet order by at least two**. Corrections to the clean $C_{m+2}$ term are therefore at most $C_m$ — not $C_{m+1}$, not $C_{m+2}$. And for $s<m$ the clean term is already $\le C_{m+1}$, so its corrections are even lower.

Combined with the uniqueness of the $s=m$ term (the only way to place $m+2$ derivatives on one $\chi$ is all $m$ outer derivatives on the $\nabla^2 a$ factor's $\chi^2$; any derivative diverted to the $aE$ factor lowers that factor's jet to $\le C_{m-s}\le C_m$), this confirms there is **no unaccounted $C_{m+2}$**. Point (5) holds, and its justification is the order-conservation/drop-by-two mechanism above.

## What is established, and what this does not reach

Established by the note, and confirmed here:
- In $\partial_t U_m$ the single cutoff jet $C_{m+2}$ appears **uniquely** in the Hessian-$a$/Lichnerowicz term, as $2\chi C_{m+2}\star(aE)$ (magnitude $\le 2\chi C_{m+2}\cdot C|U|$), carrying at least one $\chi$.
- All other sources are $\le C_{m+1}$ (outer Leibniz $j\ge1$, at $j=1$) or $\le C_m$ (commutator, principal/Lichnerowicz, quadratic reaction, normalization, $G$-variation).
- The single $\chi$ is precisely the factor the weighted dissipation $D^U_{m,p}$ requires.

Accordingly, "H-WU resolved" means: the input structure that A03 Step 40 §2.2 postulates is verified as correct and complete. That is a well-defined, bounded conclusion and the note is right to phrase it that way.

What this note does **not** deliver (and does not assert to):
1. A precise index-level ledger. The Proposition tracks derivative order and $\chi$-count through $\star$-notation; it does not exhibit the exact index contractions of each term. This is adequate for the $L^p$ magnitude absorption (which uses $|C_{m+2}|$, $|aE|\le C|U|$), so the phrase "arbitrary-order index-level tensor ledger" in §0 is more precisely a jet-order-and-weight ledger. This is a communicative point, not an error.
2. The $L^p$ closure itself. That is A03 Step 40's staggered induction (eqs. 2.5–2.11, 3.4–3.6), which needs its own control of the current $C_{m+1}$ jet at exponent $p$; H-WU supplies only the top-term structure that makes the dissipation-absorbed part work.
3. The transported-coefficient DeTurck restart (H-DT), stated as independent and unproved.
4. Anything beyond the restricted four-dimensional Ishida–LeBrun negative-pinching program of Step 42: the positive branch, dimensions $n\ge5$, dimension-only constants for all manifolds, and the Lean 4 formalization demanded by Yau Problem 26 are all untouched. Step 42 §6 and Step 40 §6 both say this plainly.

## Minor textual items

- §4.3, gradient-$a$ term: "$(\nabla^{m+1}a)(aE)\star(\nabla E)$" reads as a stray insertion of $(aE)$. The intended object is $a(\nabla^{m+1}a)\star(\nabla E)=(\nabla^{m+1}a)\star(a\nabla E)$, top jet $C_{m+1}$. The order count is unaffected.
- The $\binom{m}{s}$ (and $\binom{k}{s}$) coefficients throughout are schematic representatives of index interleavings; safe for magnitude/jet accounting, not literal tensor identities. Worth one sentence in the note so the "ledger" is unambiguous.
- The referenced verification script `workspace/scripts/step43_weighted_evolution_verify.py` was not available to me; the algebraic content above was checked by hand and is independent of it. If that script tests the identity $\nabla^k(\chi^2)$ top jet, the factorization, and the order-conservation bound of point (5), it would be worth confirming it encodes the drop-by-two argument rather than only sampling small $m$.

## One suggestion that would materially strengthen the ledger

Add the explicit order-conservation line from point (5) — "$\nabla^{t_1}\mathrm{Rm}\star\nabla^{r'}a$ with $t_1+2+r'=m+2$, hence $r'\le m$" — to §4.2/§4.6. It converts the terse "strictly less than $C_{m+2}$" into a proof, closes the only place a skeptical reader would look for a hidden $C_{m+2}$, and makes the Proposition self-contained without reference to the companion script.