# TTCS Independent Branch Record

```json
{
  "step_id": 26,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A03/workspace/notes/step25_whole_support_moser_and_normalization_repair.md",
    "Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md",
    "Sessions/S0910A03/workspace/scripts/verify_step26_general_p_and_sobolev.py"
  ]
}
```

## Task

Verify the Step 26 mathematical development for the 4D negative-branch cutoff-flow program. The note claims to resolve two of three remaining obstacles: (1) the general-p weighted tensor inequality and (2) the initial Sobolev inequality on collapsed balls. Check specifically:

(a) Does the general-p derivation (Section 3) correctly extend the A01 q=2,3 template? In particular: is the boundary term d(eta^2 a^{p-1}) correctly handled (vanishing deta part for p>=3, Young for da part giving Cp^2 r^{-2} K_p)? Is the Hessian-a IBP at general p correct (no singular terms)? Is the dissipation constant c>0 uniform in p? Is the polynomial p-dependence on the RHS (at most p^3 after the full Young/Sobolev chain) sufficient for the infinite-product convergence?

(b) Does the Maheux-Saloff-Coste theorem (Section 1) genuinely resolve the initial Sobolev question? The claim is that for n=4, p=2, p*=4, the relative Sobolev inequality gives S = Cr^2 Vol^{-1/2} with C depending only on n and Kr^2, valid on any geodesic ball regardless of collapse. Is the passage from the mean-subtracted form to the compactly-supported form correct? Are the constants truly volume-independent?

(c) Is the corrected beta-bar definition (Section 2) consistent: does subtracting the collar from H_2 and using S on the active support give a self-consistent absorption? Does the additive constant from the collar spoil the Gronwall bound?

(d) Is the explicit J_6 propagation (Section 4) a genuine critical absorption argument, not just an appeal to homogeneity?

(e) Does the first-exit closure (Section 6) genuinely self-improve all conditions simultaneously, conditional on smooth existence?

Identify any hidden error or gap. Give corrected formulas if needed.

## Output

## Verification memo — Step 26 (4D negative-branch cutoff-flow program)

### Summary

The algebraic and scaling backbone of Step 26 is sound. I reproduced the exponent bookkeeping in Sections 1, 3, 4, and 5 by hand and found the weight structure, the Hölder/Sobolev absorption chain, and the Moser exponent products all consistent. The Maheux–Saloff-Coste passage genuinely delivers a volume-independent constant, and the $J_6$ argument is a real critical absorption. Two items need repair in the writeup, one of which is substantive: the control of the collar energy in Section 2, which the note justifies incorrectly and which is sharp precisely in the collapsed regime the whole program targets. Two are typos. The single genuinely unresolved analytic task (O1, smooth continuation of the degenerate normalized flow) is correctly identified as open, and its "structural exercise" description understates the degenerate-parabolicity work involved.

---

### (a) General-$p$ tensor inequality (Section 3)

The extension of the A01 $q=2,3$ template is correct. I checked each mechanism.

**IBP identity.** The weighted identity (3.4) with weight $w'=\eta^2 a^{p-1}$ and power $p$,
$$
p\!\int w' F^{p-2}\langle R,\Delta R\rangle=-p\!\int w' F^{p-2}|\nabla R|^2-p(p-2)\!\int w' F^{p-2}|\nabla F|^2-p\!\int\langle dw',F^{p-2}\langle R,\nabla R\rangle\rangle,
$$
reproduces from IBP using $\langle R,\nabla R\rangle=F\nabla F$. The two dissipation terms have coefficients $p$ (with $|\nabla R|$) and $p(p-2)$ (with $|\nabla F|$). This matters for the power count below.

**Cutoff-derivative term** $d(\eta^2 a^{p-1})=2\eta\,d\eta\,a^{p-1}+(p-1)\eta^2 a^{p-2}\,da$. The $d\eta$ piece vanishes because $a\equiv0$ on a neighborhood of $\operatorname{supp}d\eta$, so $a^{p-1}=0$ there for any $p>1$ (not merely $p\ge3$). Correct. The $da$ piece, after using $\langle R,\nabla R\rangle=F\nabla F$, contains **$\nabla F$, not $\nabla R$**:
$$
-p(p-1)\!\int\eta^2 a^{p-2}\langle da,F^{p-1}\nabla F\rangle .
$$
Absorbing this into the $p(p-2)$-weighted $|\nabla F|$ dissipation gives residual $\dfrac{(p(p-1))^2}{p(p-2)}\,r^{-2}K_p\sim p^2\,r^{-2}K_p$, so the note's $Cp^2r^{-2}K_p$ in (3.1) is defensible. Note that absorbing the same term into the $|\nabla R|$ dissipation (coefficient $p$) would instead give $p^3$; both are harmless, and Section 5 uses $p^3$ throughout, so the intermediate power is immaterial to convergence.

**Hessian-$a$ IBP.** The quotient produced is $a^{p-3}|da|^2=a^{p-3}\cdot4a|d\chi|^2=4a^{p-2}|d\chi|^2$, a non-negative power of $a$ for all $p\ge2$. No singular term appears. Correct.

**Uniform $c$.** Since $\|\nabla Z_p\|_2^2\sim \tfrac{p^2}{4}\int\eta^2a^{p-1}F^{p-2}|\nabla F|^2+\tfrac{p^2}{4}r^{-2}K_p$ and the available $|\nabla F|$ dissipation is $p(p-2)\sim p^2$, the ratio is $p$-independent; keeping $c\|\nabla Z_p\|_2^2$ on the left with $c$ uniform (after moving $\sim p^2r^{-2}K_p$ right) is legitimate.

**Convergence.** With $L_j=Cp_j^3 4^j(t^{-1}+r^{-2})$ and $p_j=p_0(3/2)^j$, both $\sum1/p_j=3/p_0$ and $\sum(\log L_j)/p_j=\sum(3\log p_j+j\log4+\log C)/p_j$ converge geometrically. Any polynomial $p$-power (here $p^3$) is fine. I confirmed the script's numerical sums.

Verdict: (a) is correct.

---

### (b) Maheux–Saloff-Coste and the collapsed Sobolev question (Section 1)

The passage is correct. From the mean-subtracted (Neumann-type) inequality, multiplying by $V^{1/p^*}$ gives $\|u-u_B\|_{p^*}\le Ce^{C(1+\sqrt{|k|}r)}r\,V^{1/p^*-1/p}\|\nabla u\|_p$, and $|u_B|\le V^{-1/p}\|u\|_p$ by Hölder gives $\|u_B\|_{p^*}\le V^{1/p^*-1/p}\|u\|_p$. For $n=4,\ p=2,\ p^*=4$, $1/p^*-1/p=-1/4$; squaring and combining yields exactly
$$
\|u\|_4^2\le C(n,Kr^2)\,r^2 V^{-1/2}\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr),\qquad \mathsf S=C(n,Kr^2)\,r^2 V^{-1/2}.
$$
The constant $C(n,Kr^2)$ carries no volume dependence — the entire $V$-dependence is the explicit $V^{-1/2}$, because the doubling and Buser–Poincaré constants under $\operatorname{Ric}\ge kg$ depend only on $n$ and $\sqrt{|k|}\,r$. With $k=-(1+\delta)$ and $r=r_*$ fixed, $\sqrt{|k|}r$ is uniformly bounded, so $C(n,Kr^2)$ is uniform across the pinching sequence. The relative (not scale-invariant) form with the $r^{-2}\|u\|_2^2$ term is precisely what the energy absorptions consume; nothing stronger is needed. This genuinely removes any noncollapse hypothesis. (I cannot independently verify the exact constant form printed for Math. Ann. 303, but the doubling+Poincaré⟹Sobolev content is standard and correctly invoked.)

Verdict: (b) is correct; obstacle (2) is genuinely resolved.

---

### (c) The $\bar\beta$ definition and collar handling (Section 2) — substantive issue

**Identity and Gronwall absorption are correct.** The collar $\operatorname{supp}\eta\setminus\operatorname{supp}\chi$ has $a\equiv0$, hence $g$ (and $F$, $d\mu$) stationary there, so $C_{\rm col}$ is genuinely time-constant and $\widehat H_2=H_2-C_{\rm col}=\int_{\operatorname{supp}\chi}F^2\,d\mu$. Then $\widehat H_2'=H_2'$, and (2.3) is correct. The additive $Cr^{-2}C_{\rm col}$ does **not** spoil Gronwall: with constant forcing,
$$
\widehat H_2(t)\le e^{Ct/r^2}\widehat H_2(0)+C_{\rm col}(e^{Ct/r^2}-1)\le e^{Ct/r^2}\bigl(\widehat H_2(0)+C_{\rm col}\bigr)=e^{Ct/r^2}H_2(0),
$$
so (2.5) holds. Good.

**The substantive issue is the propagated smallness.** The conclusion of §2.3, $\bar\beta(t)\le C\bar\beta(0)e^{Ct/r^2}$, does not follow from the above. Gronwall gives
$$
\bar\beta(t)=\mathsf S(t)\widehat H_2(t)^{1/2}\le 2\mathsf S(0)\,e^{Ct/2r^2}\,H_2(0)^{1/2},
$$
which controls $\bar\beta(t)$ by the **full-support** quantity $\mathsf S(0)H_2(0)^{1/2}=\mathsf S(0)(\widehat H_2(0)+C_{\rm col})^{1/2}$, not by $\bar\beta(0)=\mathsf S(0)\widehat H_2(0)^{1/2}$. The two agree only if $\mathsf S(0)C_{\rm col}^{1/2}$ is itself small.

The note justifies this by "$C_{\rm col}\le H_2(0)\le CV$". This step is where the argument breaks in the very regime the program targets. $H_2(0)=\int\eta^2(1+|\operatorname{Rm}_0|^2)$ is **not** $\le CV$ on a collapsed ball: $|\operatorname{Rm}|$ is not controlled by the Ricci pinching (the Weyl part is free), and on a closed 4-manifold $\int_M|\operatorname{Rm}|^2$ carries a topological lower bound through Gauss–Bonnet and signature ($\int|W^+|^2$ fixed modulo the bounded $\int|\mathring{\rm Ric}|^2,\int s^2$ terms). Hence as $V\to0$,
$$
\mathsf S(0)H_2(0)^{1/2}=Cr^2\Bigl(\tfrac{H_2(0)}{V}\Bigr)^{1/2}\longrightarrow\infty,
$$
so the full-support quantity is large exactly when collapsing. Only the maximal-function-selected $\bar\beta(0)$ is small.

What is actually needed: the good-support selection must control the curvature energy over the **entire buffer support** $\operatorname{supp}\eta$, so that $\mathsf S(0)C_{\rm col}^{1/2}$ is comparable to $\bar\beta(0)$ and small. This is achievable by choosing $\eta$ supported in a slightly larger concentric ball still inside the maximal-function-good region (a maximal function controlled at scale $r$ typically controls a band of scales), but it must be stated and used; the printed justification does not deliver it, and the intermediate inequality $H_2(0)\le CV$ is not true in collapse. Every downstream use of "$\bar\beta$ smallness propagates" (including §6's (F3a) improvement, which also silently compares $\widehat H_2(t)$ to $H_2(0)$) inherits this dependence.

**Typo.** Eq. (2.4) as printed carries an extra $/\mathsf S$: the correct bound is
$$
\int\eta^2 aF^3\le\|F\|_{L^2(\operatorname{supp}\chi)}\|\chi F\|_4^2\le C\bar\beta\bigl(D_2+r^{-2}\widehat H_2\bigr),
$$
since $\|F\|_{L^2}\|\chi F\|_4^2\le(\bar\beta/\mathsf S)\cdot\mathsf S(D_2+r^{-2}\widehat H_2)=\bar\beta(D_2+r^{-2}\widehat H_2)$. This matches A01 eq. (4.6) with $\beta_a=\mathsf S\|F\|_{L^2}=\bar\beta$. The subsequent absorption "for $\bar\beta\le\bar\beta_*\ll1$" is correct with this corrected form (and would be inconsistent with the printed $/\mathsf S$).

---

### (d) $J_6$ propagation (Section 4)

This is a genuine critical absorption, not homogeneity. From (3.1) at $p=6$, $\Phi=|E|$, the reaction is $\int\eta^2 a^5 F|E|^6=\int F\,Z_6^2$ with $Z_6=\eta a^{5/2}|E|^3$. Hölder gives $\le\|F\|_{L^2(\operatorname{supp}\chi)}\|Z_6\|_4^2$; Sobolev gives $\|Z_6\|_4^2\le\mathsf S(\|\nabla Z_6\|_2^2+r^{-2}\|Z_6\|_2^2)$ with $\|Z_6\|_2^2=\int\eta^2a^5|E|^6\le J_6$; and $\mathsf S\|F\|_{L^2}=\bar\beta$. So the reaction is $\le\bar\beta(\|\nabla Z_6\|_2^2+r^{-2}J_6)$ and the gradient is absorbed for small $\bar\beta$, giving $J_6(t)\le e^{Ct/r^2}J_6(0)$. This uses the same curvature smallness $\bar\beta$ (the potential $F$ multiplies $|E|^6$, the triangular structure with no curvature-only source), exactly parallel to the $q=2$ curvature absorption but at level 6. The initial bound $J_6(0)\le C\delta^6V$ from pointwise pinching is correct. Verdict: (d) is correct — subject to the same $\bar\beta$-smallness whose propagation is affected by item (c).

I also confirmed the volume cancellation in the endpoint: with $\mathcal M_{6,0}\le Ct\delta^6V$ and $\mathsf S=Cr^2V^{-1/2}$, eq. (5.10) gives $\|aE\|_\infty\le C\mathsf S^{1/3}t^{-1/3}\delta V^{1/6}=C\delta r^{2/3}V^{-1/6}\cdot V^{1/6}t^{-1/3}=C\delta(r^2/t)^{1/3}$. The $V$ cancels exactly; this is what makes the defect bound collapse-independent, and it hinges on the $V^{-1/2}$ from (b). The curvature endpoint $\|aF\|_\infty\le C\beta_*/t$ likewise reproduces.

---

### (e) First-exit closure (Section 6)

The self-improvement structure is valid conditional on smooth existence. Key checks:

- **Integrable drift.** $\int_0^{\theta r^2}(r^2/s)^{1/3}ds=\tfrac32 r^{2/3}(\theta r^2)^{2/3}=\tfrac32\theta^{2/3}r^2$ is finite because the exponent $1/3<1$; the $t\to0$ blow-up of $\|aE\|_\infty$ is integrable. So $I(\theta r^2)\le\tfrac32C\delta\theta^{2/3}r^2$, small for small $\delta$ (with $r\le1$, consistent with A01 §8.7). This is the mechanism that yields metric comparability across the whole interval including $t=0$.
- **Consistency of the loop.** (5.7)→$I$ small→(F1) strict; (F1)→(F2) Sobolev, cutoff bound; (2.5)→(F3a); Step 25 (3.1)→(F3b); (4.2)→(F4). The continuity/first-exit logic (assume on $[0,T)$, improve strictly, so $T$ is not an exit) is applied correctly. The improvement factors ($<1/10$, $<2$) are attained for $\theta,\delta$ small.
- **Dependence on (c).** Both the (F3a) step and the $\bar\beta$-preservation compare hatted active-support quantities to $H_2(0)$; the closure's smallness therefore inherits the collar-control requirement of item (c). Fix (c) and the loop closes.
- **Open item O1.** The note correctly isolates smooth continuation of the degenerate normalized cutoff flow as the remaining analytic task. The description "structural exercise, no new geometric quantity" understates it: the flow $\partial_t g=-2aE$ with $a=\chi^2$ vanishing on the collar is **degenerate parabolic**, so DeTurck/approximation and the Wang-type continuation induction are not automatic adaptations of the uniformly-parabolic case. The $-2ag$ term is indeed lower order in the induction, but the degeneracy of the principal part where $a\to0$ is the real content and is unwritten. This is where the negative-branch chain is genuinely incomplete.

---

### Consolidated

- Correct and reproduced: the general-$p$ inequality (a), the MSC collapsed Sobolev (b), the $J_6$ critical absorption (d) with its $V$-cancellation, the Moser exponent products and endpoints (Section 5), and the first-exit self-improvement structure (e) conditional on existence.
- Substantive repair needed (c): the collar energy $C_{\rm col}$ enters the propagated smallness through $\mathsf S(0)H_2(0)^{1/2}$; the justification $H_2(0)\le CV$ is not valid in collapse (topological lower bound on $\int|\operatorname{Rm}|^2$ against $V\to0$), so the maximal-function selection must be arranged to control energy over the full buffer support $\operatorname{supp}\eta$, giving $\mathsf S(0)C_{\rm col}^{1/2}$ small. State and use this; then §2.3's propagation and §6's (F3a) improvement stand.
- Typos: (2.4) has a spurious $/\mathsf S$ (correct form $C\bar\beta(D_2+r^{-2}\widehat H_2)$); (3.3) chain rule should read $\partial_t\Phi_\varepsilon=\tfrac1{2\Phi_\varepsilon}\partial_t|E|^2$ (the printed $\tfrac{|E|^2}{2\Phi_\varepsilon^2}$ carries an extra factor). Neither affects conclusions.
- The remaining genuine analytic obligation is O1; its degenerate-parabolic character deserves explicit treatment rather than being labeled a lower-order adaptation.

What remains unresolved that the supplied material cannot settle: (i) the explicit maximal-function selection statement that controls $\|F\|_{L^2}$ over $\operatorname{supp}\eta$ (needed to close item c) is not in these notes and must be produced or cited; (ii) the degenerate normalized-flow existence/continuation to $\theta r^2$ (O1) is not derived here.