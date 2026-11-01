# TTCS Independent Branch Record

```json
{
  "step_id": 31,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step31_weighted_moser_interpolation_and_first_exit.md",
    "Sessions/S0910A03/workspace/notes/step31_coupled_continuation_theorem.md",
    "Sessions/S0910A03/workspace/notes/step31_corrected_support_and_terminal_density.md",
    "Sessions/S0910A03/workspace/scripts/verify_step31_weighted_interpolation.py",
    "Sessions/S0910A03/workspace/scripts/verify_step31_coupled_continuation.py"
  ]
}
```

## Task

Verify the complete analytic chain for the four-dimensional negative-branch Ricci-pinching gap, focusing on three specific claims:

1. WEIGHTED MOSER INTERPOLATION: The parabolic step combines sup_t K_p (energy) with K_{2p} = ||Z_p||_4^4 (Sobolev on Z_p = a^{(p-1)/2}Φ^{p/2}), then K_{3p/2} ≤ K_p^{1/2} K_{2p}^{1/2} (Cauchy-Schwarz). This supposedly resolves the half-power gap by noting ||Z_p||_3^3 is never used. Critically check: does the gradient ||∇Z_p||_2^2 genuinely decompose into D_p (a-weighted curvature dissipation) plus r^{-2}K_p (cutoff gradient) without any remaining gap? Does the 4D Sobolev step for ||Z_p||_4^2 ≤ S²(||∇Z_p||_2² + r^{-2}||Z_p||_2²) truly close the Moser iteration with polynomial p-loss? Does the L^∞ limit K_p^{1/p} → ||aΦ||_∞ give the correct weighted supremum?

2. COUPLED CONTINUATION: The induction claims d/dt(X_p+Z_p)+cD ≤ C(1+X_p+Z_p) where X_p=||∇^mU||_p^p and Z_p=||∇^{m+1}χ||_p^p, closing by Grönwall without dividing by χ. Check: is the connection-change formula ∂_t(∇^{m+1}χ) = U*∇^{m+1}χ + ∇^mU*∇χ + lower correct? Does the coupling genuinely avoid circular dependence? Does the {p,2p,4p} Hölder schedule work for all products?

3. TERMINAL BRIDGE: The terminal density ∫D^loc ≤ CQ with ε=Q/Vol regularization, exponential-pullback averaging, and the projector contradiction. Check: does the eigenline density restriction to the bounded-curvature region L_i create a gap when chart geodesics extend outside L_i? Does the Q/A normalization correctly account for varying topology?

## Output

# Verification Memo: 4D Negative-Branch Ricci-Pinching Analytic Chain

## Summary of what holds and what needs repair

The three notes share one recurring mathematical pattern that determines almost everything: the degenerate flow $\partial_t g = -2a(\mathrm{Ric}+g)$ carries the factor $a=\chi^2$ into every diffusion term, so the natural energy weight for $K_p=\int a^{p-2}\Phi^p$ produces dissipation with weight $a^{p-1}$, and the test function $Z_p=a^{(p-1)/2}\Phi^{p/2}$ carries exactly that weight. When these $a$-powers are tracked faithfully, the estimates close; the several apparent "half-power" mismatches (A01's and others') come from moments where the notes replace $a^{p-1}$ by $a^{p-2}$ using $a\le1$, which moves quantities to the wrong weight. The core mechanism is sound, but the write-up commits this weight-dropping in at least three places, and one Sobolev inequality is stated in a form valid only in dimension 2. Below, each item is grounded in the specific equation.

---

## Claim 1 — Weighted Moser interpolation

**Cauchy–Schwarz interpolation (Lemma 1).** Correct and exact. $K_{2p}=\|Z_p\|_4^4$ (exponent check $2(p-1)=2p-2$ ✓), $K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}$ (factor split $a^{(p-2)/2}\Phi^{p/2}\cdot a^{(2p-2)/2}\Phi^{p}$, squares reproduce the $K_p$ and $K_{2p}$ integrands ✓), and $\|Z_p\|_2^2\le K_p$ from $a\le1$. The Python exponent checks confirm these. No issue.

**Gradient decomposition — genuine, no residual mismatch.** The computation
$$
\nabla Z_p=\tfrac{p-1}{2}a^{(p-3)/2}(\nabla a)\Phi^{p/2}+a^{(p-1)/2}\tfrac p2\Phi^{p/2-1}\nabla\Phi
$$
is correct, and the two resulting terms carry exactly the weights that appear in $K_p$ and $D_p$:
- cutoff term: $a^{p-3}|\nabla a|^2=4a^{p-2}|\nabla\chi|^2\le 4C_\chi^2 r^{-2}a^{p-2}$, integrates to $Cr^{-2}K_p$;
- curvature term: $a^{p-1}\Phi^{p-2}|\nabla\Phi|^2\le a^{p-1}\Phi^{p-2}|\nabla\mathrm{Rm}|^2=D_p$ integrand (using $|\nabla\Phi|\le|\nabla\mathrm{Rm}|$ since $\Phi=F\ge|\mathrm{Rm}|$).

So $\|\nabla Z_p\|_2^2\le Cp^2(D_p+r^{-2}K_p)$ holds with no leftover term. The physical reason it works: the degenerate diffusion $a\Delta$ times the test weight $a^{p-2}$ produces dissipation weight $a^{p-1}$, which is precisely the weight on the $\nabla\Phi$ part of $\nabla Z_p$. This matching is real and is the genuine content of the note.

**The Sobolev step is stated in a dimension-2 form in §6.** The first displayed inequality in §6,
$$
\int_B u^4\le S^2\Big(\int|\nabla u|^2\Big)\Big(\int u^2\Big)+Cr^{-2}S^2\Big(\int u^2\Big)^2,
$$
is a Ladyzhenskaya inequality valid in dimension 2, not 4. Scaling $u_\lambda(x)=u(\lambda x)$ on $\mathbb R^4$ gives LHS $\sim\lambda^{-4}$ but RHS $\sim\lambda^{-6}$; the two sides do not balance, so this inequality is not true as a scale-free statement in 4D. The correct 4D critical embedding is the second form the note also writes, $\|u\|_4^2\le C_S(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2)$, which is **linear** in $\|\nabla u\|_2^2$ (the exponent $\theta=1$ in Gagliardo–Nirenberg for $n=4$, $p=4$, with **no** $\|u\|_2$ interpolation factor).

**Consequence for §2/§3 step 3.** The step "$\int_0^T K_{2p}\le(\sup K_p)\cdot CS^2\int_0^T(D_p+r^{-2}K_p)$" follows from the dimension-2 Ladyzhenskaya form, not the true 4D embedding. With the correct linear embedding one gets only a per-slice bound $K_{2p}(t)^{1/2}\le C_S\,Cp^2(D_p(t)+r^{-2}K_p(t))$, hence
$$
\int_0^T K_{2p}^{1/2}\,dt\le C_S\,Cp^2\Big(\int_0^T D_p+r^{-2}\int_0^T K_p\Big)\lesssim \sup_t K_p .
$$
This is a bound on $\int_0^T K_{2p}^{1/2}$, **not** $\int_0^T K_{2p}$. So step 3 as printed is not the correct 4D statement.

**But the target survives by reordering.** The correctly-weighted next level is still reachable:
$$
\int_0^T K_{3p/2}\,dt\le\int_0^T K_p^{1/2}K_{2p}^{1/2}\,dt\le(\sup_t K_p)^{1/2}\int_0^T K_{2p}^{1/2}\,dt\lesssim(\sup_t K_p)^{3/2}.
$$
Here Cauchy–Schwarz (Lemma 1(ii)) is applied to $K_{3p/2}$ **directly**, fed by the correct-embedding bound on $\int K_{2p}^{1/2}$. This produces the correctly $a$-weighted $K_{3p/2}$ (weight $a^{(3p-4)/2}$), which is what the next iteration level needs. So the note's conclusion — the iteration runs on $K_{3p/2}$, not on $\|Z_p\|_3^3$ — is attainable, but the printed derivation route (through $\int K_{2p}$) is not the one that works. A clean re-derivation should replace step 3 by "$\int K_{2p}^{1/2}$ from the linear 4D embedding, then Cauchy–Schwarz on $\int K_{3p/2}$."

**On A01's observation.** A01 is correct that the natural parabolic quantity in 4D is $\int_0^T\|Z_p\|_3^3=\int_0^T\int a^{3(p-1)/2}\Phi^{3p/2}$ (since $2(n+2)/n=3$ at $n=4$), whose $a$-weight $a^{(3p-3)/2}$ is exactly $a^{1/2}$ heavier than $K_{3p/2}$'s $a^{(3p-4)/2}$, hence smaller and unable to bound $K_{3p/2}$ from above. The note is right that the iteration does not need $\|Z_p\|_3^3$; but the reason is not that it is "irrelevant," it is that the Cauchy–Schwarz route above reaches the correctly-weighted $K_{3p/2}$ through $\int K_{2p}^{1/2}$. The two facts are compatible; the note conflates "$\|Z_p\|_3^3$ is not used" with "step 3 gives $\int K_{2p}$," and only the former is true.

**$L^\infty$ endpoint — correct.** $K_p^{1/p}=\|a^{1-2/p}\Phi\|$ with $a^{1-2/p}\to a$ uniformly on $\{a>0\}$ (since $a|a^{-2/p}-1|\le C/p$ using boundedness of $a\ln a$), so $K_p^{1/p}\to\|a\Phi\|_\infty$. The momentary "$a^{1/2}F$ vs $aF$" hesitation in §7.5 resolves correctly to $\|aF\|_\infty$. On the plateau $\{a=1\}$ this is the honest $\|\mathrm{Rm}\|_\infty$ bound needed downstream; off-plateau it is only a weighted bound, which is all the chart construction uses.

**§7.3 critical $q=2\to3$ step — wrong power on $D_2$, correct outcome.** The line
$$
\int aF^3\le\hat H_2^{1/2}\,S_j(D_2+r^{-2}\hat H_2)^{1/2}
$$
carries a square root on $D_2$. From the linear 4D embedding, $K_4^{1/2}=\|Z_2\|_4^2\le S_j(D_2+r^{-2}\hat H_2)$ is **linear** in $D_2$, so the correct statement is $\int aF^3\le K_3\le\hat H_2^{1/2}K_4^{1/2}\le \gamma_j(D_2+r^{-2}\hat H_2)$ with $\gamma_j=S_j\hat H_2^{1/2}$, no square root. The subsequent Young step (written for a $(D_2)^{1/2}$ term) is then unnecessary; absorption is direct, $\gamma_j D_2\le\tfrac c2 D_2$ provided $\gamma_j\le c/2$. The qualitative outcome ($\hat H_2$ persistence, spacetime $H_3$ control under $\gamma_j$ small) is unchanged.

**The absorption parameter is genuinely collapse-independent.** This is the one place where getting the Sobolev constant's dimension right matters. The correct 4D constant in $\|u\|_4^2\le C_S(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2)$ has dimension $L^2\mathrm{Vol}^{-1/2}$, i.e. $C_S\sim r^2/\mathrm{Vol}(B_r)^{1/2}$ — this is exactly the note's $S_j$ (§7.1), and the embedding is **linear** in $S_j$, not $S_j^2$. Then
$$
\gamma_j=S_j\hat H_{2}^{1/2}\le \frac{Cr^2}{\mathrm{Vol}^{1/2}}\,(\Lambda\bar K\,\mathrm{Vol})^{1/2}=Cr^2(\Lambda\bar K)^{1/2},
$$
and the volume cancels, so $\gamma_j$ does not degenerate under collapse. (Had one used $S_j^2\sim r^4/\mathrm{Vol}$ as the embedding constant, as the "$CS^2$" notation in §2/§6 suggests, the absorption parameter would be $\sim r^4/\mathrm{Vol}^{1/2}\to\infty$ under collapse and the step would break. The physically correct constant is the linear one, and with it the note's collapse-independence is right.) The residual condition is that $\gamma_j=Cr^2(\Lambda\bar K)^{1/2}$ be below a fixed threshold, achievable by small $r$; this couples to the existence time $T$ and to the Rauch condition $Kr^2$ small (see below), a quantitative tension that the notes do not resolve.

**Reaction Hölder in §7.2 — same weight-dropping, correctable.** The text bounds the reaction $\int a^{p-1}F^{p+1}$ up to $\int a^{p-2}F^{p+1}$ using $a\le1$, then Hölders to $K_p^{(p-1)/p}(\int a^{p-2}F^{2p})^{1/p}$. The second factor $\int a^{p-2}F^{2p}$ has weight $a^{p-2}$ and is $\ge K_{2p}=\int a^{2p-2}F^{2p}$, so it is **not** controlled by the Sobolev output $K_{2p}$. Keeping the correct reaction weight $a^{p-1}$ instead, the Hölder split solves to
$$
\int a^{p-1}F^{p+1}\le K_p^{(p-1)/p}\Big(\int a^{2p-2}F^{2p}\Big)^{1/p}=K_p^{(p-1)/p}K_{2p}^{1/p},
$$
which is exactly $K_{2p}$. So the reaction is controlled if and only if one refrains from the $a^{p-1}\to a^{p-2}$ downgrade. This is the same $a$-power discipline as everywhere else; the note's printed reaction estimate loses it and should be re-stated.

**Net on Claim 1.** The mechanism (degenerate-diffusion weight $a^{p-1}$ matches $Z_p$'s gradient, $K_{3p/2}$ via Cauchy–Schwarz, collapse-independent $\gamma_j$, $L^\infty$ at $\|a\Phi\|_\infty$) is correct and the iteration can be made to close with polynomial $p$-loss. Three write-up items must be corrected before it is a proof: (i) the §6 first displayed inequality is a 2D statement, replace by the linear 4D embedding; (ii) §2/§3 step 3 and §7.3 carry inconsistent powers of $S$ and of $D$, replace by the $\int K_{2p}^{1/2}$-then-Cauchy–Schwarz route; (iii) §7.2 reaction must retain weight $a^{p-1}$ to reach $K_{2p}$. None of these is fatal, but each currently substitutes a false or mismatched inequality for a true one, so the iteration is not yet demonstrably closed as written.

---

## Claim 2 — Coupled continuation

**Connection-change formula — correct after careful derivative counting.** The assertion $\partial_t(\nabla^{m+1}\chi)=U*\nabla^{m+1}\chi+\nabla^m U*\nabla\chi+\text{lower}$ has the right top order. Key point: $\nabla^{m+1}\chi$ (for a scalar, $\chi$ time-independent) contains Christoffel derivatives only up to $\partial^{m-1}\Gamma$ (by induction $\nabla^k\chi$ contains up to $\partial^{k-2}\Gamma$; verify $\nabla^2\chi\ni\Gamma$, $\nabla^3\chi\ni\partial\Gamma$). Hence $\partial_t\nabla^{m+1}\chi$ contains $\partial^{m-1}(\partial_t\Gamma)\sim\nabla^m(\partial_t g)\sim\nabla^m(aE)\sim\nabla^m U$ as its highest curvature term — order $m$ in $U$, **not** $m+1$. This is the crucial fact that prevents derivative loss: had $\nabla^{m+1}\chi$ contained $\partial^{m}\Gamma$, the coupling would require $\nabla^{m+1}U$ and be circular. It does not. The $m=1$ check ($\partial_t\nabla^2\chi=-(\partial_t\Gamma)*\nabla\chi\sim\nabla U*\nabla\chi$, no $\nabla^2 U$) confirms this directly. So the coupled system genuinely closes at consistent order.

**No circular dependence.** The $\nabla^m U$-equation needs $\nabla^{m+1}\chi$ (via $\Gamma_1$–$\Gamma_4$ after one integration by parts reducing $\nabla^{m+2}\chi\to\nabla^{m+1}\chi$), and the $\nabla^{m+1}\chi$-equation needs $\nabla^m U$ (top term above). This is a genuine two-way coupling at the **same** order pair $(\nabla^m U,\nabla^{m+1}\chi)$; the Grönwall sum $\tfrac{d}{dt}(X_p+Z_p)+cD_{m,p}\le C(1+X_p+Z_p)$ is the correct closure, and the "$U*\nabla^{m+1}\chi$" self-term, if present at all, only contributes $\|U\|_\infty Z_p$ inside the Grönwall — harmless. The integration-by-parts bookkeeping in §2.1 ($\Gamma_1$ reduced by one order, $\Gamma_4$ absorbed by $D_{m,p}$) is the correct fix to the $m$-only bookkeeping the note attributes to Wang Prop. 4.14.

**Hölder schedule.** The arithmetic $1/(2p)+1/(2p)+1/(4p)+(p-2)/p=1-3/(4p)\le1$ is correct, and on compact $M$ (finite measure) the slack is admissible. The genuine point needing statement: to avoid exponent regression, the induction hypothesis $I_k$ should read "$\nabla^j U,\nabla^{j+1}\chi,\nabla^j T$ bounded in $L^q$ for **all** $q<\infty$, $j\le k$," not for a single fixed $p$. With the all-$q$ hypothesis, using lower orders in $L^{4p}$ at level $m$ needs no further regression. As written, $I_k$ fixes one $p$ and the "no infinite regression" assertion is not justified; the fix is standard (prove all $L^q$ at each order) but must be made explicit.

**Dependence on Claim 1 and on uniform $\varepsilon$-estimates.** The base case $k=0$ uses $\|U\|_\infty$ from the zero-order first-exit theorem, so the entire continuation is conditional on Claim 1 actually closing. Separately, §5 asserts short-time existence via regularization $a\to a+\varepsilon$ with "uniform estimates as $\varepsilon\to0$, standard for porous-medium type." The uniform-in-$\varepsilon$ estimates for a degenerate diffusion with the specific tensorial reaction here are precisely the hard analytic content (A1), not a citation; this is asserted, not derived, and is where the notes themselves locate the open point.

---

## Claim 3 — Terminal bridge

**Chart geodesics stay in the bounded-curvature plateau — correct.** With $P_j=B_r(p_j)$, chart radius $3r$, and plateau $L_j=B_{4r}(p_j)$ on which $\chi_j\equiv1$ so $a\equiv1$: for $p\in P_j$, $\exp_p(B_{3r}(0))\subset B_{4r}(p_j)=L_j$, and the averaging ball $B_r(0)$ lands in $B_{2r}(p_j)\subset L_j$. So the eigenline density $\mathfrak G_i$ (defined only where curvature is bounded) is defined throughout the averaging region, and the restriction-and-extend-by-zero does not create a hole. Moreover on $L_j$, $a=1$, so the curvature bound $|a\mathrm{Rm}|\le K$ is the honest $|\mathrm{Rm}|\le K$, consistent with Rauch. The nested $r/4r$ design does exactly the job intended. No gap here.

**Rauch condition.** $(1\pm C\sqrt K r)$ comparison needs $Kr^2$ small, with $K=C\beta/T$ from the Moser output. This couples back to the same $r$–$T$–$\beta$ tension noted in Claim 1: small $r$ helps $\gamma_j$ but $Kr^2=C\beta r^2/T$ needs $T$ not too small relative to $r^2$, and $\beta$ (a Moser constant) is not evidently small. The quantitative simultaneous satisfaction of $\gamma_j$ small, $Kr^2$ small, $T$ large enough, and volume retention $\alpha$ bounded below is not worked out.

**Normalization — operative bound is correct; a side inequality points the wrong way.** The operative conclusion in §2.5 is
$$
\alpha\,\mathrm{Vol}_i\cdot\min_p\bar{\mathfrak D}_i\le C\!\int_M\mathfrak D_i^{\text{loc}}\le CQ_i\quad\Rightarrow\quad \bar{\mathfrak D}_i(p_i)\le \frac{CQ_i}{\alpha\,\mathrm{Vol}_i}\le C\delta_i^2\to0,
$$
using $Q_i/\mathrm{Vol}_i\le\delta_i^2$. This is dimensionally consistent — the volume cancels — and does not need the $A_i$ normalization at all. The §2.4 chain, by contrast, writes "$\mathrm{Vol}_i\ge cA_i$" and then "$Q_i\le C\delta_i^2\mathrm{Vol}_i\le C\delta_i^2 A_i$": the second inequality needs $\mathrm{Vol}_i\le CA_i$ (an upper bound), the opposite direction to what is stated. For collapsing sequences with topological $A_i$ fixed, $\mathrm{Vol}_i/A_i\to0$ makes the intended $\tfrac1{A_i}\int\mathfrak D^{\text{loc}}\to0$ true anyway, but the printed inequality direction is inconsistent and should be corrected to $\mathrm{Vol}_i\le CA_i$. The germ contradiction does not use §2.4, so this does not affect the final step.

**$\int\mathfrak D^{\text{loc}}\le CQ$ with $\varepsilon=Q/\mathrm{Vol}$.** The eigenline bound $\int_{L_i}\mathfrak G_i\le C(Q_i+\varepsilon_i^2\mathrm{Vol}_i)=C(Q_i+Q_i^2/\mathrm{Vol}_i)\le C'Q_i$ uses $Q_i\le\delta_i^2\mathrm{Vol}_i$, $\delta_i\le1$, so $Q_i^2/\mathrm{Vol}_i\le\delta_i^2 Q_i\le Q_i$. Arithmetic is consistent. The global terms $\int(s+4)^2\le4Q$, $\int(s+8\sqrt6|W^+|)^2\le864\pi^2R\le CQ$ depend on the identities and signed-Weyl estimate from Steps 6/16, which are not in the supplied files; their internal use here is dimensionally consistent but not independently checkable from this material.

**Projector contradiction — structurally sound, sub-inputs external.** The germ limit $\mathrm{Ric}_{g_\infty}=-g_\infty$, $s_\infty=-4$, $\mathrm{Spec}(W^+_\infty)=(-1/6,1/12,1/12)$, forcing $\nabla W^+_\infty=0$ while the Einstein–Weyl identity gives $|\nabla W^+_\infty|^2=1/16\ne0$, is a clean local differential contradiction (a nonzero constant against a forced zero), and being pointwise it is legitimate on a germ $B_{r/2}(0)$ from Cheeger–Gromov smooth convergence. The two sub-facts (spectrum forces parallel $W^+$; Einstein–Weyl gives $1/16$) come from Steps 6 and 16 and cannot be verified from the provided files. If both hold, the contradiction is valid.

---

## What remains genuinely unresolved

1. **Claim 1 must be re-derived with consistent $a$-powers and the true 4D embedding.** Replace the 2D Ladyzhenskaya display, the "$\int K_{2p}$" step, the §7.3 square root, and the §7.2 reaction downgrade. Each is a place where a false or wrongly-weighted inequality currently stands in for a true one. The corrected route ($\int K_{2p}^{1/2}$ linear-embedding bound → Cauchy–Schwarz for $K_{3p/2}$; reaction kept at weight $a^{p-1}$) appears to work, and the collapse-independent $\gamma_j=Cr^2(\Lambda\bar K)^{1/2}$ is correct, but the closed iteration with uniform polynomial $p$-loss and uniformly absorbed reaction across all levels has not been assembled from the corrected pieces.

2. **The quantitative simultaneous satisfaction** of $\gamma_j\le c/2$ (small $r$), Rauch $Kr^2$ small with $K=C\beta/T$, existence time $T$, and volume retention $\alpha$ bounded below is not exhibited. These pull on $r$ and $T$ in competing directions and need a single consistent choice.

3. **The degenerate short-time existence with uniform-in-$\varepsilon$ estimates (A1)** is asserted "standard, porous-medium type" but is the actual open analytic content; the continuation theorem (Claim 2) is otherwise structurally correct and non-circular, but rests on this and on Claim 1's $\|U\|_\infty$.

4. **External Steps 6/16** (Weyl-spectrum rigidity, positive-part monopole eigenline density, the $|\nabla W^+|^2=1/16$ identity) are used but not present; the terminal contradiction is conditional on them.

The encouraging structural finding is that the derivative bookkeeping in Claim 2 is genuinely closed at order $(\nabla^m U,\nabla^{m+1}\chi)$ with no hidden loss, and the nested support geometry in Claim 3 correctly keeps chart geodesics inside the bounded-curvature region. The vulnerable material is concentrated in Claim 1's Sobolev/interpolation write-up, where consistent tracking of the $a^{p-1}$ dissipation weight is the single discipline that turns the apparent half-power obstructions into closed estimates.