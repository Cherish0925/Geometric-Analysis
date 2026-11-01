# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A03/workspace/notes/step37_base_pair_continuation.md",
    "Sessions/S0910A03/trace/ttcs/results/step37_ttcs01_verifier1_integration.md",
    "Sessions/S0910A03/workspace/notes/step27_shifted_curvature_continuation_analysis.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Read the actual Step 38 note, the corrected Step 37 base-pair file, the Step 37 TTCS integration, the shifted-curvature evolution source notes, A01's index-level curvature tensor derivation, and Wang's printed Section 4 source. Verify the new scientific assertion at the tensor-energy level: (i) a signed term J=∫χ ∇_i∇_jχ B^{ij}(V), with |B|≤C_p|V|^p and |∇B|≤C_p|V|^{p-1}|∇V|, is controlled by weighted diffusion plus ||dχ||∞²||V||_p^p; (ii) the actual m=2 term χ∇²χ*∇²U in the differentiated U equation really has this signed contraction structure after testing, so an evolving Hessian norm is unnecessary for this term; (iii) identify precisely which remaining general-m top-cutoff/lower-curvature contractions are not covered by this lemma and what finite-exponent induction would be needed. Check whether the repaired finite-Lp base estimate is valid without hidden L-infinity or division-by-a assumptions. Give explicit corrections rather than treating the extension theorem as established.

## Output

# Verification Memo: Signed Hessian-Cutoff Lemma and the Repaired Finite-$L^p$ Base Estimate

Session S0910A03. Independent tensor-energy checking of Step 38, the corrected Step 37, the Step 27 / shifted-curvature source notes, A01 Step 35, and Wang §4.

## 1. The signed Hessian-cutoff lemma (assertion i) is correct

For $J=\int_M \chi\,\nabla_i\nabla_j\chi\,B^{ij}(V)\,d\mu$ on closed $M$, the single integration in (1.3) is exactly the divergence identity for the vector field $X^i=\chi\,\nabla_j\chi\,B^{ij}(V)$:
$$
\nabla_iX^i=\nabla_i\chi\,\nabla_j\chi\,B^{ij}+\chi\,\nabla_i\nabla_j\chi\,B^{ij}+\chi\,\nabla_j\chi\,\nabla_iB^{ij},
$$
whose integral vanishes, giving (1.3) with no residual term and no curvature commutator. The two estimates then hold:

- $\big|\int \nabla_i\chi\,\nabla_j\chi\,B^{ij}\big|\le C_p\|d\chi\|_\infty^2\int|V|^p$ from $|B|\le C_p|V|^p$.
- $\big|\int \chi\,\nabla_j\chi\,\nabla_iB^{ij}\big|\le C_p\int|\chi||d\chi||V|^{p-1}|\nabla V|$, and the factorization (1.5) has correct exponents: $\tfrac{p-2}{2}+\tfrac{p}{2}=p-1$. Young against the weighted dissipation $\int\chi^2|\nabla V|^2|V|^{p-2}$ closes it.

The structural derivative bound $|\nabla B|\le C_p|V|^{p-1}|\nabla V|$ is legitimate for $p\ge2$ under the regularization $(|V|^2+\delta^2)^{1/2}$, since $|\nabla(|V|^{p-2}V\otimes V)|\le C_p|V|^{p-1}|\nabla V|$. No quotient by $a$ and no pointwise $\nabla^2\chi$ bound enters. Assertion (i) stands.

A01 Step 35's index-level tensors are the concrete realizations: $B_{\mathrm{curv}}^{pq}=R^p{}_j{}^q{}_lE^{jl}$ with $|B|\le CF^2$, $|\nabla B|\le CF|\nabla\operatorname{Rm}|$, and $B_{\mathrm{def}}^{pq}=|E|^2g^{pq}+\tau E^{pq}-2(E^2)^{pq}$ with $B_{\mathrm{def}}|_{E=0}=0$, $|\nabla B_{\mathrm{def}}|\le Cs^{1/2}|\nabla E|$. Each satisfies the exact hypotheses of the lemma, so the lemma is the shared engine of both the continuation energies and the smoothing (Moser) power inequalities.

## 2. The $m=2$ single-Hessian term (assertion ii) is genuinely of signed form

Testing the differentiated $U$-equation against $|V|^{p-2}V$ with $V=\nabla^2U$: the term $\chi\nabla^2\chi*V$ contributes
$$
\int \chi\,\nabla_i\nabla_j\chi\;B^{ij}(V),\qquad B^{ij}(V)=\text{metric contraction of }|V|^{p-2}V\otimes V.
$$
Then $|B|\le C_p|V|^p$ and $|\nabla B|\le C_p|V|^{p-1}|\nabla V|$ hold, so the lemma applies and this term costs $\varepsilon D_{2,p}+C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p$. The evolving $\|\nabla^2\chi\|_4$ input of the earlier Step 32 treatment is unnecessary *for this term*. The enumeration of the three $V$-containing pieces at $m=2$ — $\chi\nabla^2\chi*V$, $\nabla\chi*\nabla\chi*V$, $\chi\nabla\chi*\nabla V$ — is complete for $\gamma\in\{2,3\}$, and the middle and last are handled directly (bounded coefficient, and diffusion via the $\chi$ factor). Assertion (ii) stands as stated.

Step 38 does not assert the whole $m=2$ level is closed, and this restraint is warranted: the $\gamma=0$ allocations at $m=2$ include $\chi\nabla^4\chi*U$ and $\nabla^2\chi*\nabla^2\chi*U$. One integration of $\chi\nabla^4\chi*U$ produces $\nabla^3\chi=\nabla^{m+1}\chi$ coupled to $\nabla^2U$. So even at $m=2$ the *full* $\nabla^2U$ estimate needs $\nabla^3\chi$, exactly the same-level coupling described next. The note's confinement of the lemma to the single term $\chi\nabla^2\chi*V$ is accurate.

## 3. What the lemma does not reach for general $m$ (assertion iii)

The lemma eliminates the cutoff Hessian only when (a) the cutoff derivative is exactly $\nabla^2\chi$ and (b) the curvature factor is the top energy $V=\nabla^mU$. The genuinely delicate terms fail both conditions:

- $\Gamma_1=\chi\nabla^{m+2}\chi*U$: the cutoff derivative is order $m+2$ and the curvature factor is $U$ (order $0$). One integration transfers a derivative and leaves $\nabla^{m+1}\chi$ coupled to $\nabla^mU$. Concretely, the descendant $\int\nabla(|V|^{p-2}V)*\chi\nabla^{m+1}\chi*U$, after Young against $D_m$, leaves the coefficient
$$
\int|\nabla^{m+1}\chi|^2|U|^2|V|^{p-2}\le K^2\|\nabla^{m+1}\chi\|_p^2\|\nabla^mU\|_p^{p-2}.
$$
This is a same-exponent coupling of $\nabla^mU$ and $\nabla^{m+1}\chi$, **not** an eliminable single-Hessian term.

- The descendant of type $\chi\nabla^{m+1}\chi*\nabla U*|\nabla^mU|^{p-2}\nabla^mU$: if the transferred derivative lands on $\nabla U$ one obtains $\nabla^m\chi*\nabla^2U$ multiplying the current power; if it lands on metric contractions or commutators, unweighted lower-order $T$-derivatives appear. These require a finite-exponent schedule for previous $U$, $T$, and cutoff-jet levels.

The induction that would close this, set out in `weighted_moser_and_continuation_repair.md` §6–§7, is:

1. Couple $(\nabla^mU,\nabla^{m+1}\chi)$ at the same exponent $p$ through the cutoff evolution $\partial_t\nabla^{m+1}\chi$, whose unique current-order product is $\nabla^mU*\nabla\chi$. The regularized norms $\mathcal X_{m,p}=(\varepsilon+\|W_m\|_p^p)^{2/p}$, $\mathcal Z_{m+1,p}=(\varepsilon+\|C_{m+1}\|_p^p)^{2/p}$ convert the coefficient terms $K^2\|C_{m+1}\|_p^2\|W_m\|_p^{p-2}$ and $K\|C_{m+1}\|_p\|W_m\|_p^{p-1}$ into linear/bilinear right-hand sides, giving the coupled Grönwall (6.19). I checked these conversions: multiplying $\frac{d}{dt}\|W_m\|_p^p$ by $\frac{2}{p}\|W_m\|_p^{2-p}$ turns the first into $C\mathcal Z$ and the second into $C\mathcal Z^{1/2}\mathcal X^{1/2}\le C(\mathcal X+\mathcal Z)$. Current-order factors stay at exponent $p$; there is no upward exponent chain in the pair.

2. Estimate $\nabla^mT$ afterward using previous levels in $L^{4p},L^{8p}$ (finite volume covers unused exponent); the worst coefficient $\int|\nabla^{m+1}\chi|^2|T|^2|T_m|^{p-2}$ needs $\nabla^{m+1}\chi,T\in L^{4p}$, and the commutator $\int|\nabla^mU||T||T_m|^{p-1}$ needs $\nabla^mU,T\in L^{2p}$ via $\tfrac1{2p}+\tfrac1{2p}+\tfrac{p-1}{p}=1$.

This is written in outline, not as a completed per-$m$ derivation. A full extension theorem still requires the explicit verification of (6.11)–(7.5) at every $m$.

## 4. The repaired finite-$L^p$ base estimate holds without $L^\infty$ or genuine division by $a$

Both formerly mis-powered terms are now correctly of signed form:

- $I_3=R_3$-testing $=\int\chi\,\nabla_i\nabla_j\chi\,B^{ij}(W)$ with $W=\nabla U$, $B$ a contraction of $|W|^{p-2}W\otimes W$. Lemma (i) at $m=1$ gives $\varepsilon\int a|\nabla W|^2|W|^{p-2}+C\|d\chi\|_\infty^2\|W\|_p^p$ (note $a=\chi^2$ matches the $W$-diffusion weight).
- $I_{1c}$: since $\nabla U=W$, the raw integrand has total power $p$ in $|W|$ times $\chi|\Theta|$; the Step 37 (3.9) / TTCS integration correctly restores it to $\int\chi\nabla^2\chi\,B(W)$ and applies the lemma. The earlier $\|\Theta\|_p\|W\|_p^{p-1}$ power bookkeeping was inconsistent with (3.15); the second integration removes that inconsistency.

The absence of hidden pointwise coefficients is verifiable from the algebraic identities:
$$
a\nabla T=W-da*T,\quad a\nabla\operatorname{Rm}*U=(W-da*T)*U,\quad a\operatorname{Rm}*W=(U-aG)*W,\quad \partial_t\Gamma\sim\nabla\operatorname{Ric}(U)=\operatorname{Ric}(\nabla U)\sim W.
$$
Each appears only in finite $L^p$, controlled by $|U|\le K$, $\|d\chi\|_\infty$, uniform metric equivalence, and $\|T\|_{L^p}$. Neither $\|T\|_\infty$ nor $\|a\nabla\operatorname{Rm}\|_\infty$ enters. The base pair therefore closes by Grönwall for $Y_1=\|W\|_p^p+\|\Theta\|_p^p$, **conditional on** the unweighted finite-$L^p$ estimate for $T$ (Step 27 eq. 5.4).

I checked that conditioning estimate itself: testing (3.6)/(2.2) against $|\tilde R|^{p-2}\tilde R$, the sole Hessian term $\int(\nabla^2a)*\tilde R*\tilde R|\tilde R|^{p-2}$ integrates once to $C\int|\nabla a||\nabla\tilde R||\tilde R|^{p-1}$, and with $|\nabla a|=2\chi|\nabla\chi|$ factorizes to $\varepsilon\int\chi^2|\nabla\tilde R|^2|\tilde R|^{p-2}+C\|\nabla\chi\|_\infty^2\int|\tilde R|^p$. It is valid on $\sup|U|<\infty$ alone. So the conditioning is met, and the base pair is a proved finite-$L^p$ statement.

The Step 37 §6 statement that finite $L^p$ for all $p$ does not yield $L^\infty$ is correct and important: the energy controls only the degenerate $\int\chi^2|\nabla W|^2|W|^{p-2}$, i.e. $\|\chi\nabla|W|^{p/2}\|_2$, not the full $\|\nabla W\|_p$ that Sobolev $W^{1,p}\hookrightarrow L^\infty$ requires. The divergent scaling ratio (4.7) in `weighted_moser_and_continuation_repair.md` §4 (triangular bump near a regular zero of $\chi$, $\tfrac{\|w\|_4^2}{\int a|\nabla w|^2+\|w\|_2^2}=\tfrac{3}{29\sqrt{5\varepsilon}}\to\infty$) makes the obstruction concrete. Pointwise control comes only from the full unweighted derivative tower, which is precisely the induction of §3 above.

## 5. Explicit corrections to record

1. **Recurring cosmetic division.** `shifted_curvature_continuation.md` (6.3) still writes $|\nabla a|^2/a=4|\nabla\chi|^2$ as a pointwise identity on $\{a=0\}$, and the analogous $\chi^2/a=1$ appeared in the superseded Step 37 (3.6). Neither is defined on $\{a=0\}$. The rigorous route uses $|\nabla a|=2\chi|\nabla\chi|$ and $|\chi|=\sqrt a$ directly, which holds everywhere. Rewording is cosmetic and does not alter any result, but should be made uniformly.

2. **Source of the $CK\|\Theta\|_p^p$ coefficient.** Step 37 §4 attributes it to a spatial "$U*\Gamma$" term in $\nabla\operatorname{Ric}(U)$. That term does not exist: $\nabla\operatorname{Ric}(U)=\operatorname{Ric}(\nabla U)\sim W$ because the contraction metric is parallel. The $CK\|\Theta\|_p^p$ comes from the evolving norm and volume element under $\partial_tg=-2\operatorname{Ric}(U)$. Inequality (4.3) is unchanged.

3. **Wang Proposition 4.14, printed text.** Read literally, its surviving uncontrolled term is $\nabla^2\chi*\nabla^m\chi*\chi^2\operatorname{Rm}$ (cutoff orders $\le m$), and its induction-hypothesis consequences list $|\nabla^k\chi|_p$ only for $k\le m$. The direct integration of $\Gamma_1=\chi\nabla^{m+2}\chi*\chi^2\operatorname{Rm}$ produces a $\nabla^{m+1}\chi$ descendant, so the $\nabla^m(\chi^2\operatorname{Rm})$ estimate genuinely requires $\|\nabla^{m+1}\chi\|_p$. Wang's Proposition 4.13 hypothesis does assume $\nabla^i\chi$ for $i\le m+1$, so the global scheme is repairable; the A03 same-exponent coupled pair $(\nabla^mU,\nabla^{m+1}\chi)$ makes the dependency explicit and removes the apparent circularity. This is a real strengthening of the printed bookkeeping, not merely a re-statement.

4. **The extension theorem is not established.** The lemma repairs the single-Hessian current terms and the $m=2$ instance of that term. The coupled-pair Grönwall (6.19) and the $\nabla^mT$ finite-exponent estimate (7.6) are outlines; a written per-$m$ induction through (6.11)–(7.5) remains to be produced, and the transported-coefficient existence theorem in `shifted_curvature_continuation.md` §8 must be secured for the terminal restart. Step 27 cannot be cited as already proving the induction.

5. **Reach of even a completed continuation/smoothing principle.** As the notes state, the K2–Y–Moser outputs (5.5), (5.7) remain conditional on a smooth first-exit interval, moving Sobolev comparison, and the $H_3,J_6$ seeds. Even the full smoothing mechanism addresses the restricted four-dimensional Ishida–LeBrun family in the sign regime studied; the arbitrary-topology, dimension $\ge5$, positive-sign branch, dimension-only constants, and Lean formalization of the Yau 26 statement are not touched by this line.

## 6. Net position

The tensor-energy content of Step 38 is sound: the signed Hessian-cutoff lemma is proved, its $m=2$ application is exact, and the finite-$L^p$ base pair is a genuine theorem under the stated hypotheses and the independently valid $T$-estimate, using no $L^\infty$ curvature and no true division by $a$. The remaining mathematical substance is a written induction closing the same-exponent $(\nabla^mU,\nabla^{m+1}\chi)$ pair together with the $\nabla^mT$ finite-exponent estimate for all $m$, plus the transported-coefficient existence and the terminal geometric passage — none of which the present notes present as complete, and which the notes correctly keep separate from the proven base estimate.