# TTCS Independent Branch Record

```json
{
  "step_id": 54,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step54_exact_synchronized_output_ledger.md",
    "Sessions/S0910A03/workspace/notes/step54_route_reassessment_and_joint_weighted_iteration.md",
    "Sessions/S0910A03/staging/processing/xu_local_ricci_flow.txt",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Verify the exact synchronized-output fixed-background ledger in the new Step 54 supplement as a mathematician working on degenerate quasilinear parabolic systems. Reconstruct the frozen inner system from the exact DeTurck identity and check every top-order family in the single-solution H^s estimate and the branch-2-oriented H^{s-2} difference estimate. Focus on whether any term produces an unweighted D^{r+1}(U1-U2), an unweighted D^{r+1}omega, a missing derivative of V or beta, or an epsilon-dependent constant. Check the product estimates (4.4)-(4.5), integrations (4.8),(4.12)-(4.13), and transport (4.14)-(4.16). Also assess whether standard Galerkin/parabolic-transport construction plus the stated uniform tame hierarchy can pass epsilon to zero smoothly across the zero set, or identify the exact missing estimate. Do not accept the theorem merely because the schematic ledger looks plausible; return explicit corrected formulas and status.

## Output

## Verification memo: synchronized-output fixed-background ledger (Step 54 supplement)

### Overall finding

The tensor ledger is structurally coherent and the two-order grading $r=s-2$ is the correct mechanism; I reconstructed the frozen inner system from Xu's exact terms and traced every top-order family. The single-solution $H^s$ estimate (9.1)/(3.1) and the branch-2-oriented $H^{r}$ difference estimate (4.17)/(9.8) close as written, and the constants are genuinely $\varepsilon$-independent — this is the substantive content and it is real. However, (4.17) is a candidate a priori estimate, not a start theorem, for two reasons that the schematic ledger does not resolve: the coupled fixed-$\varepsilon$ inner solve is asserted, not built; and the $\varepsilon\to0$ passage to a smooth solution across the degenerate transition locus $\{\beta=0\}$ is the deepest unproven step, made genuinely delicate by the transported (non-prescribed) cutoff. I also found one imprecise statement in §4.3 that must be corrected, and one load-bearing discipline that must be promoted to an explicit lemma.

### 1. Reconstruction against Xu's exact terms — correspondence confirmed

Xu's frozen linear system (his (2.4)) has, at fixed background $\tilde g=\bar g$:
- $D_{ij}(U,V)=-\chi^2[(u^{\alpha\beta}\tilde g^{pq}\tilde R_{j\alpha q\beta})v_{ip}+(\dots)v_{jp}]$ — algebraic, linear in $V$: this is the ledger's $\beta^2R(U,V)$. The frozen linear term is the correct one (check 1 of §5).
- $E_{ij}=\tfrac12\chi^2 u^{\alpha\beta}u^{pq}(\nabla u\,\nabla u)$ — quadratic in $DU$, coefficient $\chi^2$: this is $\beta^2Q(U,DU)$.
- $F_{ij}=\chi\chi_i\,u^{pq}(\nabla u)$ — coefficient $\chi\nabla\chi$, i.e. $\tfrac12 d(\chi^2)$: this is exactly the transported-cutoff Lie cross $2\operatorname{sym}(d(\beta^2)\otimes W(U)^\flat_U)$, since $d(\beta^2)=2\beta D\beta$.

So the ledger's three families $\{R,Q,\text{Lie cross}\}$ are the complete image of Xu's $\{D,E,F\}$ under $\chi\to\beta$; no $Q$-family is dropped. The one element with no Xu analogue is the transport line $\partial_t\beta=\beta^2W(V)\cdot D\beta$ (Xu's $\chi$ is prescribed). Its single-solution and difference estimates are the ledger's own construction and are where the new coupling lives. The normalization term $-2\beta^2V$ is not tabulated but is algebraic and harmless: its difference is $-2\beta_2^2Z-2(\beta_1+\beta_2)\omega V_1$, controlled by $C_R(\|Z\|_{H^r}+\|\omega\|_{H^r})$.

### 2. Single-solution $H^s$ estimate — sound and $\varepsilon$-uniform

I checked each row of §3's table against $\int D^sV\cdot D^s\partial_tV$ and $\int D^s\beta\cdot D^s\partial_t\beta$:

- Principal: $D^{s+2}V\to$ dissipation $-(\beta^2+\varepsilon)|D^{s+1}V|^2$; the Leibniz remainder $D^j[(\beta^2+\varepsilon)U^{-1}]D^{s+2-j}V$ for $j\ge2$ is Moser-controlled by $\mathcal E_s$ using $D^2V\in L^\infty$ ($s>n/2+4$).
- Frozen $Q$: the top $\beta^2 A\,D^{s+1}U$ is integrated once, $-\!\int(\beta D^{s+1}V)(\beta A\,D^sU)$, and $D^sU$ sits inside the $H^s$ ball. No $D^{s+1}U$ survives; the estimate therefore needs $U$ only in $H^s$, not $H^{s+1}$. Correct.
- Lie cutoff/input tops ($\beta W(U)D^{s+1}\beta$, $\beta D\beta\,D^{s+1}U$): each carries a $\beta$, integrates onto $\beta D^{s+1}V$, absorbed.
- Transport top $\beta^2W(V)D^{s+1}\beta$ is the advective term; $\tfrac12\int\beta^2W(V)\!\cdot\!D(|D^s\beta|^2)$ integrates to $\|D(\beta^2W(V))\|_\infty\|D^s\beta\|^2$, finite because $DW(V)\sim D^2V\in L^\infty$. The $\beta^2 D^{s+1}V\,D\beta$ commutator carries $\beta$ and is absorbed.

Every absorption uses only $\beta^2|D^{s+1}V|^2\le(\beta^2+\varepsilon)|D^{s+1}V|^2$, so the constant is $\varepsilon$-independent. The large-$A$ symmetrizer is standard bookkeeping. This estimate is a genuine advance over the Step 53 product map.

### 3. Difference estimate — verified, with one correction and one required lemma

**Algebra of (4.3)–(4.5).** The decomposition
$(\beta_1^2+\varepsilon)U_1^{-1}-(\beta_2^2+\varepsilon)U_2^{-1}=(\beta_1^2-\beta_2^2)U_1^{-1}+(\beta_2^2+\varepsilon)(U_1^{-1}-U_2^{-1})$
is exact. In (4.4)/(4.5) the top $V_1$-derivative is $D^{r}(D^2V_1)=D^{s}V_1$, which lies in the $H^s$ ball ($r+2=s$), multiplied by $\omega$ or $H\in L^\infty$; no difference is interpolated, so both bounds hold and are $\varepsilon$-uniform ($\beta_2^2+\varepsilon\le 1+R^2$). This is exactly the half-Hölder error of Step 53 removed.

**(4.7)–(4.8).** $Q(U,DU)$ quadratic in $DU$ gives top $\beta_2^2A\,D^{r+1}H$; the integration
$$\int D^rZ\,\beta_2^2AD^{r+1}H=-\!\int(\beta_2D^{r+1}Z)(\beta_2A\,D^rH)-\!\int D^rZ\,D(\beta_2^2A)D^rH$$
is correct, uses only $\|H\|_{H^r}$, and lands the surviving derivative on the branch-2 dissipation with weight $\beta_2$. So the contraction genuinely closes in $H^r$ (not $H^{r+1}$).

**(4.16).** $W(V_1)-W(V_2)\sim A\,DZ$, so the transport top is $\int D^r\omega\,\beta_2^2A\,D^{r+1}Z\,D\beta_2=\int(\beta_2D^{r+1}Z)(\beta_2A\,D\beta_2\,D^r\omega)$, Cauchy–Schwarz into the same $Z$-dissipation. Note both the metric cross term (4.11)→(4.12) and this transport term draw on the single dissipation $\int(\beta_2^2+\varepsilon)|D^{r+1}Z|^2$; with the $A$-weight and small splitting parameters the borrowed shares sum below $c$. Consistent.

**Correction to §4.3.** The exact Lie-difference, oriented to branch 2, is
$$d(\beta_1^2)W(U_1)-d(\beta_2^2)W(U_2)=\underbrace{d(\beta_2^2)\,\Delta W}_{\beta_2}\;+\;\underbrace{\big(d(\beta_1^2)-d(\beta_2^2)\big)W(U_2)}_{\beta_2\ \text{via (4.10)}}\;+\;\big(d(\beta_1^2)-d(\beta_2^2)\big)\Delta W,\quad \Delta W=W(U_1)-W(U_2).$$
I confirm the identity used in (4.10):
$$d(\beta_1^2)-d(\beta_2^2)=2\beta_2\,d\omega+2\omega\,d\beta_1\qquad(\text{exact, since }2\omega\,d\beta_1=2\omega\,d\beta_2+2\omega\,d\omega).$$
Piece one gives (4.13) ($D^{r+1}H$ with $\beta_2$); piece two gives (4.11) ($D^{r+1}\omega$ with $\beta_2$, since $W(U_2)$ appears — the ledger's $W(U_2)$ is right). But the ledger's sentence "any coefficient-difference terms without $D^{r+1}\omega$ are ordinary $H^r$ products" is not accurate: the third piece $(d(\beta_1^2)-d(\beta_2^2))\Delta W$ still contains a top $D^{r+1}H$ (through $\Delta W\sim A\,DH$), and the $2\omega\,d\beta_1$ subpiece of piece two contains $\omega\,W(U_2)\,D^{r+1}\beta_1$. These are not $H^r$ products. They do close, but by a different mechanism than (4.8):

**Required lemma (must be explicit).** *Keep every full-branch high derivative intact; never split it into branch-2 plus difference.* Concretely, $\int D^rZ\,\omega\,W(U_2)\,D^{r+1}\beta_1$ is bounded directly by $\|D^rZ\|_2\|\omega\|_\infty\|W(U_2)\|_\infty\|D^{r+1}\beta_1\|_2\le C_R\|Z\|_{H^r}\|\omega\|_{H^r}$, using $\|D^{r+1}\beta_1\|_2\le\|\beta_1\|_{H^{r+1}}\le R$ (because $r+1\le s-1<s$). If one instead writes $\beta_1=\beta_2+\omega$ and treats $D^{r+1}\omega$ as an unknown, one produces after integration by parts an **unweighted** $\int D^{r+1}Z\,\omega\,W(U_2)\,D^r\omega$, whose $D^{r+1}Z$ carries no $\beta_2$ and is controllable only by $\varepsilon|D^{r+1}Z|^2$ — i.e. it would break $\varepsilon$-uniformity. The ledger's use of $d\beta_1$ (not $d\beta_2+d\omega$) in (4.10) implicitly obeys this discipline, but since it is exactly the line between a uniform and a non-uniform estimate, it should be stated and proved, not left implicit. The two-order margin $r=s-2$ exists precisely to give $D^{r+1}(\cdot)=D^{s-1}(\cdot)$ and $D^{r+2}V=D^sV$ inside the ball for full-branch factors.

**Enumeration of dangerous tops (all resolved under the lemma).** Unweighted $D^{r+1}Z$: only the principal dissipation ($+$ sign) and IBP images of (4.8),(4.11),(4.13),(4.16), all carrying $\beta_2$; none unweighted. Unweighted $D^{r+1}\omega$: only advective (removed by transport IBP) and the metric Lie cross (4.11) (moved onto $\beta_2 D^{r+1}Z$); none unweighted. Unweighted $D^{r+1}H$: only $Q$ (4.8) and Lie (4.13), both $\beta_2$-weighted onto $Z$-dissipation, both leaving $D^rH$. No missing derivative of $V$ or $\beta$ appears. So, modulo the explicit commutator work of check 2 (§5) and the lemma above, (4.17) holds with an $\varepsilon$-independent $C_R$.

### 4. $\varepsilon$-uniformity of the estimates — confirmed

Every product bound uses $L^\infty$ norms of $U,V,\beta,\omega,H$ derivatives controlled by the $H^s$ ball ($\varepsilon$-free), and every absorption uses $\beta_2^2|D^{r+1}Z|^2$ with $(\beta_2^2+\varepsilon)\le 1+R^2$. The $C_R$ in (9.1) and (4.17) does not depend on $\varepsilon$. This is the hard part and it is in place.

### 5. The two genuinely unresolved pieces

**(a) Fixed-$\varepsilon$ inner coupled solve (check 4).** For frozen $U$ the $V$-line is linear strictly parabolic and the $\beta$-line is scalar quasilinear transport with velocity $\beta^2W(V)$; the two are coupled through $\beta^2$ (in the parabolic coefficient/forcing/Lie term) and through $W(V)$ (in the velocity). The joint energy (9.1) is the symmetrizer estimate, but existence requires: uniform Galerkin bounds from (9.1); Aubin–Lions compactness for $V$ (from parabolic smoothing) and for $\beta$ (from $\partial_t\beta=\beta^2W(V)D\beta$ bounded in $L^\infty_tH^{s-1}$, giving $\beta_N\to\beta$ in $C_tH^{s-1}$); and strong convergence of $D\beta,DV$ to pass $\beta^2W(V)D\beta$. This is plausible for $s-2>n/2$ but is not written; it is standard-but-substantial and should be produced before (5.2) is used.

**(b) $\varepsilon\to0$ across the degenerate transition locus (check 5) — the deepest step.** The $\varepsilon$-uniform bounds give weak-$*$ limits, and since $\|\varepsilon D^2V_\varepsilon\|\le\varepsilon\|V_\varepsilon\|_{H^2}\to0$ and $\partial_t V_\varepsilon$ is uniformly bounded in $L^\infty_tH^{s-2}$, Aubin–Lions yields $V_\varepsilon\to V$ in $C_tH^{s-1}$ solving the degenerate ($\varepsilon=0$) system. What is *not* established is $C^\infty$ regularity of the limit across the transition locus $\{\beta=0\}\cap\overline{\{\beta>0\}}$. Two features make this harder than Xu:
   - The velocity $\beta^2W(V)$ vanishes on $\{\beta=0\}$, so the support of $\beta$ is stationary and matches $\operatorname{supp}\chi$ — this is favorable and Xu-like. On the transition locus all $\beta^2$-terms and the Lie term $\beta\,D\beta\,W$ vanish (the $\beta$ factor kills it even where $D\beta\ne0$), so the limit obeys $\partial_tV=0$ there, i.e. $V=g_0$, again as in Xu.
   - Unlike Xu, $\beta$ is not prescribed: it solves a degenerate transport near the transition locus. Its smoothness up to that locus, and the matching of the interior parabolic-smooth solution with the frozen $V=g_0$ across it, is a free-interface-type regularity question that Xu's Theorem 2.9 (prescribed $C^\infty$ $\chi$) does not cover. The weighted dissipation $\beta^2|D^{s+1}V|^2$ degenerates exactly there and supplies no interior control on the transition locus. This is the precise missing estimate: an $\varepsilon$-uniform, all-orders regularity statement for $(V_\varepsilon,\beta_\varepsilon)$ up to and across $\{\beta=0\}$, or an argument that the transported $\beta$ retains $C^\infty$ regularity there and that Xu's local parabolic regularity on $\{\beta>0\}$ plus $V=g_0$ on $\{\beta=0\}$ glue smoothly.

### 6. The §1 reduction to the geometric flow

The assertion "the pullback by $\partial_t\varphi=-\beta^2W(G)\circ\varphi$ has $\beta\circ\varphi=\chi$ and solves the fixed-cutoff geometric equation" is stated without derivation. Since Xu already gives short-time existence of the fixed-$\chi$ local Ricci–DeTurck flow, the value of the synchronized construction is the Einstein-normalized, transported-cutoff, gauge-fixed common-time flow needed downstream (§7.1). It should be verified that the coupled fixed point $U=V,\ \alpha=\beta$ genuinely yields $\partial_t g=-2\beta^2(\operatorname{Rc}+\dots)$ pulled back to the intended geometric flow with the *original* $\chi$, including that $\{\beta=0\}=\{\chi=0\}$ throughout (which the vanishing velocity argument supports) and that the normalization constant is the one targeting $\operatorname{Ric}=\lambda h$. Without this, the analytic start theorem, even if completed, is not yet tied to the quantities the terminal mechanism consumes.

### 7. Status

- Single-solution $H^s$ estimate (9.1): verified, $\varepsilon$-uniform.
- Difference estimate (4.17)/(9.8): verified to close in $H^{r}$, $\varepsilon$-uniform, provided (i) the explicit commutator computation of check 2 is carried out on the exact expansion (not the schematic $R,Q,W$), and (ii) the "keep full-branch high derivatives intact" lemma of §3 above is proved and used; the §4.3 sentence about "ordinary $H^r$ products" must be corrected as in §3.
- Fixed-$\varepsilon$ inner existence: not constructed; standard-but-unwritten.
- $\varepsilon\to0$ smoothness across the degenerate transition locus with a transported cutoff: the genuinely hard, unresolved point; the exact missing object is an $\varepsilon$-uniform all-orders regularity of $(V_\varepsilon,\beta_\varepsilon)$ up to $\{\beta=0\}$, or an interface-gluing argument replacing Xu's prescribed-$\chi$ regularity.
- §1 geometric reduction: asserted, needs derivation and normalization-constant verification.

The ledger is a correct and useful candidate that removes the Step 53 half-Hölder error by the synchronized output plus two-order grading; the a priori estimates are the right ones and are uniform. What remains before (5.1)–(5.3) become a theorem is the coupled construction and, above all, the transported-cutoff interface regularity in the $\varepsilon\to0$ limit.