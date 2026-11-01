# TTCS Independent Branch Record

```json
{
  "step_id": 31,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step31_general_p_tensor_power_inequality.md",
    "Sessions/S0910A01/workspace/notes/step31_m2_continuation_analysis.md",
    "Sessions/S0910A01/workspace/scripts/step31_general_p_verification.py",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md"
  ]
}
```

## Task

Verify two critical mathematical claims from the Step 31 derivation of the general-p tensor power inequality for the normalized cutoff flow ∂_tg = -2χ²(Ric+g) on a closed 4-manifold.

**Claim 1 (Time-decay correction):** The standard parabolic Moser iteration starting from the L^{p₀} seed K_{p₀} = ∫a^{p₀-2}F^{p₀} dμ gives a UNIFORM pointwise bound ‖aF(t)‖_∞ ≤ C(S, K₀, θ) on [T/4, T], NOT the time-decaying bound ‖aF(t)‖_∞ ≤ Cβ/t claimed in earlier steps. The mechanism: the Moser output from L^{p₀} on [0,T] is ‖u‖_∞ ≤ C(VT)^{-1/p₀}(∫₀^T K_{p₀})^{1/p₀}, where V is the spatial volume. The spacetime integral ∫K₃ ≤ Cγ H₂(1+θ), and the four-dimensional critical cancellation S² = Cr⁴/V, H₂ ≤ CV(1+K₀) makes the bound independent of collapse volume V. Similarly, the defect Moser from J₆ gives ‖aE‖_∞ ≤ Cδ (uniform). The velocity V(T) = O(δθr²) → 0 as δ→0.

**Claim 2 (m=2 continuation):** In the Wang-type shifted-curvature continuation for U=a(Rm+G), the single-χ Hessian term ∫χ|∇²χ||∇²U|^p at the m=2 induction level does NOT need to be absorbed by the dissipation D_{2,p} = ∫χ²|∇³U|²|∇²U|^{p-2}. Instead, using χ≤1 and |∇²χ|≤C/r², it is bounded by Cr⁻²A₂(p)^p where A₂(p)^p = ‖∇²U‖_{L^p}^p is the UNWEIGHTED L^p norm. This enters the Gronwall RHS: A₂' + cD_{2,p} ≤ C(1+A₂^p), giving A₂(t) ≤ Ce^{Ct}(A₂(0)+Ct). No exact tensor cancellation or dissipation absorption is needed.

Check: (a) Is the Moser output truly uniform (not 1/t) given a bounded integrated coefficient? (b) Does the 4D volume cancellation work correctly? (c) Is the Gronwall treatment of the single-χ term mathematically valid? (d) Are there subtle issues with the unweighted norm A₂ including transition-region curvature?

## Output

## Verifier memo — Step 31 time-decay correction and m=2 continuation term

I checked the two mathematical statements against the internal algebra of the notes, the verification script, and the standard structure of degenerate-weight parabolic mean-value estimates. Two of the algebraic engines are correct as written; the volume-cancellation arithmetic in the first statement is inconsistent between the note and the script, and the note's derivation of the "uniform" curvature bound contains a genuine gap. The second statement is valid for the specific term it addresses, but that term is the easy member of the family, not the one flagged elsewhere as the actual obstruction.

---

### 1. Algebra that holds (independent recomputation)

Before the disputed points, the structural identities the whole chain rests on are correct.

- **Three-factor factorization (4.1).** With $Z_p=a^{(p-1)/2}F^{p/2}$, the $a$-exponent of the right side is $\tfrac13+\tfrac{p-2}{3}+\tfrac43\cdot\tfrac{p-1}{2}=p-1$ and the $F$-exponent is $1+\tfrac p3+\tfrac{2p}{3}=p+1$. Both match $a^{p-1}F^{p+1}$, and $\tfrac13+\tfrac13+\tfrac13=1$, so the Hölder $(3,3,3)$ split is legitimate.
- **Cauchy–Schwarz interpolation (5.1).** $(a^{p-2}F^p)^{1/2}(a^{2p-2}F^{2p})^{1/2}=a^{(3p-4)/2}F^{3p/2}$, which is exactly the $K_{3p/2}$ density. Correct.
- **Product convergence.** With $p_k=(3/2)^kp_0$, $\sum\log p_k/p_k$ and $\sum k/p_k$ converge (geometric $p_k$, polynomial numerator). The exponent sum $\sum 1/p_k=\tfrac1{p_0}\cdot\tfrac{\kappa}{\kappa-1}=1$ for $n=4,p_0=3,\kappa=3/2$ is arithmetically correct.
- **$p^3$ tracking.** chain-rule $p$ × Hölder $p^{4/3}$ × Young $p^{2/3}$ $=p^3$; consistent.

So the general-$p$ power inequality (3.1)/(4.5) and the Moser recurrence are structurally sound. The trouble is confined to how the terminal bound depends on time and volume.

---

### 2. Assertion 1(a): does the integrable coefficient transmit a $1/t$ factor?

The mechanism you state is **half right and stated too strongly**.

Correct part: the coefficient $L_p(t)$ carrying $S^4Y(t)\le C\gamma^2/t$ enters the energy inequality $K_p'+cD_p\le L_p K_p$ only through the Gronwall exponential $\exp(\int L_p)$. On a dyadic slab the note's own computation is the key fact: 
$$\int_{t/2}^t S^4Y(s)\,ds\le CS^4\gamma H_2\log 2=C\gamma^3\log 2,$$
scale-invariant in $t$ (the $1/s$ integrates against $ds/s$ to a constant). For small $\gamma$ this is a bounded multiplicative constant. So the $1/t$ singularity of the coefficient genuinely does **not** propagate as a $1/t$ factor. That reasoning is valid.

Overstated part: the Moser output still carries the parabolic mean-value prefactor, which is a **separate** source of time-dependence. The note's own (5.7) gives temporal-localization exponent $\sum 1/p_k=1$, i.e. the output obeys
$$\|aF\|_\infty^3\le \frac{C}{\,\cdot\, T}\int_0^T K_3 ,\qquad \|aF\|_\infty\propto T^{-1/3}.$$
This $T^{-1/3}$ comes from the prefactor $|Q|^{-1/p_0}$, not from the coefficient, and it is real. Evaluated at the fixed terminal $T=\theta r^2$ it is a constant, so "uniform on $[T/4,T]$ for fixed $T$" is a fair statement. But "uniform, not $1/t$" as a general phrase conflates the two mechanisms: the output does scale as $t^{-1/3}$ if one evaluates at time $t$ with slab $[0,t]$. Notably the earlier defect form $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$ is exactly the honest mean-value $t^{-1/3}$ scaling; at $t=T=\theta r^2$ it reads $C\delta\theta^{-1/3}$, differing from the "uniform" $C\delta$ only by $\theta^{-1/3}$. Both feed a convergent velocity integral $\int_0^T\|aE\|_\infty\,dt=O(\delta\,\mathrm{poly}(\theta)\,r^2)$ (the exponent $-1/3>-1$ integrates), so the downstream metric comparison is insensitive to which form is used. The reframing therefore does not change the conclusion, but the phrase "the prior $\beta/t$ claim is withdrawn" is not accurate as stated — the two forms coincide at fixed $T$.

---

### 3. Assertion 1(b): the 4D volume cancellation — an internal inconsistency

Here the note and the verification script use **different prefactors**, and only one is dimensionally correct.

- Note (5.8)/(6.9): $\|aF\|_\infty^3\le \frac{C}{t}\int_0^t K_3$ — divides by time only.
- Script §5/§6: $\|aF\|_\infty^3\le \frac{C}{VT}\int_0^T K_3$ — divides by the parabolic measure $V\cdot T$.

The standard degenerate/parabolic mean-value inequality has prefactor equal to the inverse parabolic measure $=(V T)^{-1/p_0}$ (spatial volume times time). The script form is the correct one; the note's (5.8) is missing the spatial factor $V^{-1/3}$.

Tracking the two through the same inputs $S^2=Cr^4/V$, $H_2\le CV(1+K_0)$, $\int_0^T K_3\le C\gamma H_2(1+\theta)$, $\gamma=S^2H_2^{1/2}$, $T=\theta r^2$:

**Script form (correct normalization):**
$$\|aF\|_\infty^3\le\frac{C}{VT}\gamma H_2=\frac{CS^2H_2^{3/2}}{VT}=\frac{Cr^4V^{-1}\cdot V^{3/2}(1+K_0)^{3/2}}{V\,\theta r^2}=\frac{CS(1+K_0)^{3/2}}{\theta}.$$
So $\|aF\|_\infty\sim S^{1/3}(1+K_0)^{1/2}\theta^{-1/3}\sim r^{2/3}V^{-1/6}(1+K_0)^{1/2}\theta^{-1/3}$.

**Note (6.9):** the note writes $\|aF\|_\infty^3\le\frac Ct\int_0^t K_3\le C\gamma H_2$, i.e. $\|aF\|_\infty\le CS^{2/3}H_2^{1/2}\sim r^{4/3}V^{1/6}(1+K_0)^{1/2}$.

These two disagree by exactly $(VT)^{1/3}$ — the omitted parabolic-measure normalization. Two concrete points follow:

1. **The step $\frac Ct\int_0^t K_3\le C\gamma H_2$ in (6.9) is not valid.** The available bound is $\int_0^t K_3\le\int_0^T K_3\le C\gamma H_2(1+\theta)$, a constant, so $\frac1t\int_0^t K_3\le \frac{C\gamma H_2(1+\theta)}{t}$, which grows as $t\to0$. The note replaced $\frac1t\cdot(\text{const})$ by $(\text{const})$, dropping the $1/t$ without justification, and only then declared the result uniform. The rigorous route to a fixed-$T$ constant is the mean-value form with the $(VT)^{-1/p_0}$ prefactor, not this substitution.

2. **The note's (6.9) is not volume-independent**: $S^{2/3}H_2^{1/2}\sim r^{4/3}V^{1/6}$ grows with the region volume. Only the script's $(VT)^{-1}$ form removes that growth. So the two files do not agree on the central bound, and the one that appears in the note's boxed conclusion does not achieve what the correction section states.

**Deeper point on "independent of collapse volume."** Even the correct script bound is expressed through $S$, and $S^2=Cr^4/V$ diverges as $V\to0$ (collapse). So $\|aF\|_\infty\sim S^{1/3}$ blows up under collapse; the phrase "independent of collapse volume $V$" is only true in the sense that $V$ and $r$ have been repackaged into $S$, not that the estimate survives collapse. This is precisely the Sobolev-constant persistence item (C3). Since the Ricci pinching hypothesis $c_ng\le\operatorname{Ric}\le C_ng$ does not by itself prevent collapse, this repackaging leaves the collapsing case genuinely uncontrolled by the present argument, and the note's own §10 (C3) is where that dependence lives. The volume-cancellation language should not obscure it.

---

### 4. Assertion 2(c): Gronwall treatment of the single-$\chi$ term

This is **valid for the term it addresses**. The $(\alpha,\beta,\gamma)=(0,2,2)$ contribution $\chi\,\nabla^2\chi*\nabla^2U$ tested against $|\nabla^2U|^{p-2}\nabla^2U$ produces $\int\chi|\nabla^2\chi||\nabla^2U|^p$. Its cutoff order is $\beta=2=m$ and its weighted-curvature order is $\gamma=2=m$; it is genuinely diagonal, sitting below $\Gamma_1=\chi\nabla^{m+2}\chi*U$ (cutoff order $m+2=4$). Bounding $\chi\le1$ and $|\nabla^2\chi|\le C/r^2$ gives $Cr^{-2}A_2(p)^p$, and the resulting $y'\le C(1+y)$ with $y=A_2(p)^p$ integrates to a finite bound on $[0,T)$ for smooth $g_0$. No dissipation absorption and no exact tensor cancellation is needed. The note is also correct that attempting Young-absorption into $D_{2,p}$ would force a negative power of $\chi$ that diverges at the transition, so that route would be wrong.

One point to make explicit: $\nabla^2\chi$ and $|\cdot|$ are taken with respect to the evolving $g(t)$, not $g_0$. The bound $|\nabla^2\chi|_{g(t)}\le C/r^2$ is not a standalone fact about the fixed cutoff; $\nabla^2_{g(t)}\chi=\nabla^2_{g_0}\chi-(\Gamma(t)-\Gamma(0))\nabla\chi$ with $\Gamma(t)-\Gamma(0)=\int\partial_t\Gamma=\int\nabla U$. Its uniform control comes from metric equivalence (5.3) and the lower-order $A_{\le1}$ estimates, i.e. it is the first arrow $A_{\le m-1}\Rightarrow C_m$ of the triangle (7.2). Within the induction this is consistent, but the phrase "the cutoff has uniformly bounded second derivatives on a fixed support" understates this metric dependence.

---

### 5. Assertion 2(d): the unweighted norm and transition-region curvature

Including the transition region in $A_2(p)=\|\nabla^2U\|_{L^p(M)}$ is **not itself problematic**, but the reason deserves stating precisely. On $\{\chi=0\}$, $U=\chi^2\widetilde R=0$; near the transition, $\nabla^2U$ contains the term $2|\nabla\chi|^2\widetilde R$ (from $\nabla^2(\chi^2)\widetilde R$), which carries the full curvature $\widetilde R=\operatorname{Rm}+G$ weighted by $|\nabla\chi|^2\sim r^{-2}$ rather than by $\chi^2$. So $A_2$ genuinely sees transition-region curvature that the continuation hypothesis $\sup|\chi^2\operatorname{Rm}|<\infty$ does not directly control pointwise. This is acceptable because the energy inequality (7.15) for $A_2$ is closed — it does not require an independent pointwise bound on $\widetilde R$ in the transition; the reaction terms are paid by lower-order $A,B,C$ nodes and the diffusion $D_{2,p}$, and finiteness propagates from the finite smooth initial datum $A_2(p)(0)<\infty$ by Gronwall. The transition curvature is thus tracked, not assumed bounded. No inconsistency here.

---

### 6. The term this does and does not resolve

Assertion 2 answers a real but **secondary** question. The supersession header on `shifted_curvature_continuation.md` and A03's repair memo flag a different member of the family: integrating $\Gamma_1=\chi\nabla^{m+2}\chi*U$ by parts leaves a term with $\nabla^{m+1}\chi$ that must be closed as a current-order pair with $\nabla^mU$ — the $(\nabla^m U,\nabla^{m+1}\chi)$ coupling, not the diagonal $(0,2,2)$ term. Section 7.3's residual product (7.11) $\nabla^2\chi*\nabla^m\chi*U*V|V|^{p-2}$ is exactly where that coupling lives, and it is handled there by "Hölder and Young … bounded by $C(1+\|V\|_p^p)$" invoking Wang's Proposition 4.14 by substitution. The present note verifies the easy diagonal term and correctly separates it from $\Gamma_1$, but it does not itself close the $\Gamma_1$/$\nabla^{m+1}\chi$ pairing that A03 identified as the point needing repair. So Assertion 2, while correct, should not be read as resolving the continuation obstruction; the load-bearing step remains the Proposition-4.14 IBP grouping and its current-order pairing, which lives in the separate repair memo and is not reproduced in the material supplied here.

---

### 7. What remains unresolved

- **Reconcile the two prefactors.** Fix whether the terminal bound is $\frac1T\int K_3$ (note) or $\frac1{VT}\int K_3$ (script). The degenerate parabolic mean-value inequality gives $(VT)^{-1/p_0}$; the note's boxed (6.9) uses the former and consequently grows like $V^{1/6}$. One of the two files needs to be brought into line, and the corrected §6/§8 statements should replace (6.9), because the step $\frac1t\int_0^t K_3\le C\gamma H_2$ is not derivable from the finite spacetime bound.
- **State the $S$-dependence openly.** The corrected bound is controlled by $S$, and $S\to\infty$ under collapse. Because the pinching hypothesis alone does not preclude collapse, the argument as it stands controls the non-collapsed regime (bounded $S$); the collapsing regime needs a separate mechanism (this is (C3), and it is essential for the full problem over all closed 4-manifolds).
- **The degenerate-weight identification.** The seed $K_{p_0}=\int a^{p_0-2}F^{p_0}$ is not literally $\iint u^{p_0}$ for $u=aF$ (a weight mismatch of $a^2$); the passage from the weighted moments to $\|aF\|_\infty$ is via $K_p^{1/p}\to\|aF\|_\infty$ as $p\to\infty$ with the volume factors distributed through $\prod C_k$. A clean write-up should show the $(VT)^{-1/p_0}$ prefactor emerging from that product rather than asserting the standard mean-value form for a genuinely degenerate weight; this is where a hidden $V$-power can enter and is the likely origin of the note/script discrepancy.
- **The primary continuation step.** For the $m=2$ level to be settled, the $\Gamma_1/\nabla^{m+1}\chi$ current-order pairing (Proposition 4.14 substitution, and residual (7.11)) needs to be exhibited at the same level of explicitness as the diagonal term treated here; the supplied files defer it to the repair memo.

Net: the general-$p$ algebra and the m=2 diagonal-term Gronwall are correct; the coefficient/output distinction in Assertion 1(a) is real but overstated; the volume cancellation in Assertion 1(b) works only under the $(VT)^{-1/p_0}$ normalization, disagrees with the note's boxed bound, and repackages rather than removes the Sobolev/collapse dependence.