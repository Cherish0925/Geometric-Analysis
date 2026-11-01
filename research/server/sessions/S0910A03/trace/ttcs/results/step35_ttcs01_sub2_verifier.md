# TTCS Independent Branch Record

```json
{
  "step_id": 35,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step35_unregularized_J6_persistence_lemma.md",
    "Sessions/S0910A03/workspace/notes/step34_exact_defect_J6_lemma.md",
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md",
    "Sessions/S0910A03/workspace/scripts/verify_step35_defect_algebra.py",
    "Sessions/S0910A01/workspace/notes/step33_curvature_power_inequality.md"
  ]
}
```

## Task

Verify the unregularized J_6 defect persistence lemma in the companion note. The flow is ∂_t g = -2χ²(Ric+g) on a closed 4-manifold with a fixed smooth cutoff χ. The key claims to check:

1. REGULARITY: s = |E|² is smooth, s³ is smooth, and the Sobolev variable w₆ = ηχ⁵|E|³ = ηa^{5/2}s^{3/2} is C¹ with bounded gradient. No ε-regularization is needed.

2. EXACT CHAIN RULE: (∂_t - aΔ)s³ = 3s²(∂_t - aΔ)s - 6as|∇s|², with the extra term nonpositive.

3. HESSIAN-a TENSOR IBP: The integrated identity (Step 34 eq 2.4) is tested with q = 3η²a⁴s². The resulting tensor B^{ij} = 2g^{ij}|E|² + 2τE^{ij} - 4E^{ik}E_k^j is QUADRATIC in E (vanishes at E=0), so this is not a bare curvature source. The IBP moves one derivative from ∇²a onto the smooth test weight, producing only terms of the structure εX₆ + C r⁻²J₆. Check that this honest tensor IBP is valid (no IBP on |∇²a|) and that all three branches of the product rule land on the claimed weight exponents.

4. TWO-FACTOR HÖLDER: The defect potential P₆ = ∫Fw₆² is absorbed by P₆ ≤ ‖F‖₂‖w₆‖₄² ≤ γ(X₆ + r⁻²J₆) with γ = S·K₂^{1/2}. This uses ONLY ‖F‖₂, NOT Y = ∫aF³. Verify that this is correct because the defect reaction integrand is aF|E|² (linear in F), unlike the curvature reaction aF³ (cubic in F). Is there any hidden cubic term that would require Y?

5. FINAL GRONWALL: J₆' ≤ C(1+r⁻²)J₆ with no time-dependent coefficient. Compare with A01's route using ∫S²Y ≤ Cγ³. Which is correct? Are they compatible?

6. Are there any terms in the defect evolution that have been dropped or underbounded?

## Output

## Verifier memo — unregularized $J_6$ defect persistence lemma (Step 35)

I reproduced the algebra of the six statements against the note and the companion script. The core mechanism is mathematically sound as a term-level derivation, conditional on the flow-existence and first-exit hypotheses it explicitly does not prove. Below I give the checks, three genuine text/script exponent mismatches that would confuse a reader, and one unverified piece of the integrated Hessian identity.

### 1. Regularity (sound; this is a real simplification)
$s=|E|^2$ and $s^3=|E|^6$ are smooth integer powers of a smooth quadratic in a smooth tensor, so the functional $J_6=\int\eta^2a^4s^3$, its test weight $q=3\eta^2a^4s^2$, and every term of $\partial_t s^3$ are smooth including at $E=0$. The only fractional power is inside the Sobolev variable $w_6=\eta a^{5/2}s^{3/2}$, where $t\mapsto t^{3/2}$ is $C^1$ on $[0,\infty)$ with $\nabla w_6=\tfrac32\eta a^{5/2}s^{1/2}\nabla s+\dots$ continuous (it $\to0$ as $E\to0$). $w_6\in W^{1,2}$ is all the Sobolev step needs, so no Kato approximant $\Phi_\varepsilon$ is required. This works precisely because $m=6$ gives the integer power $s^{m/2}=s^3$; the same shortcut is unavailable for odd $m$, but the argument only needs $m=6$. The elimination of the $\varepsilon$-remainder that Step 34 §4.6 left undominated is genuine.

### 2. Exact chain rule (verified)
For time-independent spatial $a$, $\Delta s^3=3s^2\Delta s+6s|\nabla s|^2$ and $\partial_t s^3=3s^2\partial_t s$ give
$(\partial_t-a\Delta)s^3=3s^2(\partial_t-a\Delta)s-6as|\nabla s|^2$, extra term $-6as|\nabla s|^2\le0$ since $a=\chi^2\ge0$. Script check (C) confirms $k=1..4$ symbolically. The coercive term is then $3s^2(-2a|\nabla E|^2)$ weighted by $\eta^2a^4$, i.e. $-6X_6$ with $X_6=\int\eta^2a^5s^2|\nabla E|^2$. Correct.

### 3. Hessian-$a$ tensor IBP (identity verified; RHS of (2.4) partly asserted)
The contraction
$2E^{ij}[(\Delta a)E_{ij}+\tau a_{ij}-a_i{}^kE_{kj}-a_j{}^kE_{ki}]=a_{ij}B^{ij}$, $B^{ij}=2g^{ij}|E|^2+2\tau E^{ij}-4E^{ik}E_k{}^j$, I reproduced by hand (the $\Delta a$ term $\to 2g^{ij}|E|^2$, the $\tau$ term $\to 2\tau E^{ij}$, the two mixed terms $\to -4E^{ik}E_k{}^j$) and script (A1)–(A3) confirms it in flat and generic metrics with $B$ homogeneous degree 2 in $E$, vanishing at $E=0$. So this is not a curvature-only source.

The move $\int(\nabla_i\nabla_j a)\,\Psi^{ij}=-\int(\nabla_j a)\,\nabla_i\Psi^{ij}$ with $\Psi^{ij}=qB^{ij}$ is a valid divergence identity on the closed manifold (the total divergence integrates to zero), operating on the actual $\nabla^2a$, not on $|\nabla^2a|$. This is the correct repair of the invalid absolute-value integration that A01 Step 33 §2.6 flagged. The three product-rule branches then land as:
- derivative on $a^4$: $a^3|da|^2s^3=4a^4|d\chi|^2s^3\le 4r^{-2}\cdot(\text{$J_6$ integrand})$;
- derivative on $s^2$: $a^4|da|s^{5/2}|\nabla E|\to \varepsilon X_6+C r^{-2}J_6$ by Young;
- derivative on $B$ ($|\nabla B|\le Cs^{1/2}|\nabla E|$): same structure.

Script (D5a–c) confirms all three sit on the weight structure $(a^{m-3}s^{m/2})$ and $(a^{m-2}s^{(m-1)/2}|\nabla E|)$ that Young sends to $\varepsilon X_6+Cr^{-2}J_6$. Valid.

**Unverified piece:** the script checks only the *pointwise* contraction identity giving $B^{ij}$. The full integrated identity Step 34 (2.4) also carries the first-derivative pieces $q[-\tau\langle da,d\tau\rangle+2E(da,d\tau)]$ produced by the IBP. These are asserted, not machine-checked. They have the $I_1/I_2$ form ($|da|\,s^{5/2}|\nabla E|$ after $|d\tau|\le C|\nabla E|$) and absorb correctly, but a constructor-level write-up should display the IBP that generates them so (2.4) is fully grounded, not just its principal contraction.

### 4. Two-factor Hölder (correct; no hidden cubic in $F$)
$P_6=\int\eta^2a^5Fs^3=\int F w_6^2$ with $w_6^2=\eta^2a^5s^3$ (script E1). Hölder $\int Fw_6^2\le\|F\|_2\|w_6^2\|_2=\|F\|_2\|w_6\|_4^2$ uses exponents $\tfrac12+\tfrac24=1$ (F1). I checked the reaction census: the Lichnerowicz term $aR_{ikjl}E^{ij}E^{kl}$ and the metric-variation term $aE^{ip}R_{ijkl}E^{jkl}{}^p$ each carry exactly **one** Riemann factor and two $E$'s, i.e. $\sim aFs$; testing with $q\sim a^4s^2$ gives $\int a^5Fs^3=P_6$. There is no term with two curvature factors in the $E$-evolution, because $E$'s equation is degree one in $\mathrm{Rm}$ (the Lichnerowicz curvature coupling $\mathrm{Rm}*E$). Hence the reaction is genuinely linear in $F$, and only $\|F\|_2$ (i.e. $K_2^{1/2}$) is needed — not $Y=\int aF^3$. This is the essential structural difference from the curvature energy, whose reaction $\mathrm{Rm}*\mathrm{Rm}*\mathrm{Rm}\sim aF^3$ forces the three-factor split.

I also checked the one term that is cubic *in $E$* (metric variation of the norm, $\sim a|E|^3=as^{3/2}$, no curvature): testing gives $\int a^5s^{7/2}=\int a^5 s^{1/2}\cdot s^3\le C\int a^5Fs^3=P_6$ via $|E|\le C(1+|\mathrm{Rm}|)\le CF$ (script D9). So even this folds into the single potential $P_6$. No cubic-in-$F$ quantity appears anywhere. The Sobolev gradient decomposition (5.4)–(5.5) I verified term by term: the $d\eta$ branch vanishes on $\{a=0\}$; the $da$ branch gives $25\eta^2a^4|d\chi|^2s^3\le Cr^{-2}J_6$; the $\nabla s$ branch gives $\tfrac94\eta^2a^5s|\nabla s|^2\le 9X_6$ via $|\nabla s|^2\le4s|\nabla E|^2$; $\|w_6\|_2^2\le J_6$ since $a\le1$. Thus $P_6\le C\gamma(X_6+r^{-2}J_6)$, $\gamma=\mathcal SK_2^{1/2}$, with the volume cancellation $\gamma=r^2\sqrt{K_0}$ (script F2). Correct.

### 5. Final Gronwall vs. A01's route (both correct, compatible)
Choosing $C\gamma_0<c/2$ absorbs the $X_6$ part of $P_6$ into $-6X_6$, leaving $J_6'+\tfrac c2X_6\le C_0(1+r^{-2})J_6$ with $C_0$ time-independent. Over $T=\theta r^2$ the exponent is $C_0\theta(r^2+1)$, bounded. A01 Step 33 §4.1 instead absorbs the same reaction through the three-factor split, producing a Gronwall coefficient $Cp^N(r^{-2}+1+\mathcal S^2Y(t))$ and needing $\int_0^T\mathcal S^2Y\le C\gamma^3$. I checked A01's split algebraically: $(aF^3)^{1/3}(a^{p-2}f^p)^{1/3}\tilde z_p^{4/3}$ reconstructs $a^{p-1}Ff^p$ exactly, so A01 is bounding the single power of $F$ in an $L^3$-weighted norm ($Y=\int aF^3$) where the two-factor route uses $L^2$ ($K_2$). Both are legitimate Hölder applications for a reaction linear in $F$; the $L^2$ route is the economical one and removes the dependence on the separate $q=3$ seed. The two conclusions are compatible; the Step 35 route is the simpler and its Gronwall coefficient is honestly constant in time. Note that both routes still rest on the *same* first-exit control of $\mathcal S(t)$ and $K_2(t)$ (so that $\gamma(t)\le\gamma_0$); the two-factor route removes the $Y$-seed dependence but not the $K_2$-persistence dependence, and the note states this correctly (§0.2, §6).

### 6. Dropped or underbounded terms — census
I walked $\Sigma_s$ term by term: Lichnerowicz reaction ($\to P_6$), normalization $(-4a+8a)|E|^2\sim as$ ($\to CJ_6$), metric variation ($\to P_6$; cubic-in-$E$ piece $\to P_6$ via $|E|\le CF$), cutoff transport $\langle E,\mathcal C_a(E)\rangle$ ($da$-branch $\to I_2$, $\nabla^2a$-branch $\to$ §3.5), measure term ($\to P_6$). Nothing is dropped. The chain-rule term $-6\int\eta^2a^5s|\nabla s|^2\le0$ is discarded, which only strengthens the inequality. The homogeneity of the whole $E$-evolution in $E$ (so $E\equiv0$ is stationary — this flow's fixed point is $\mathrm{Ric}=-g$, $\lambda=-1$) means there is no curvature-only additive source, consistent with $J_6(0)\le\delta^6V$ propagating.

### Three exponent mismatches between prose and the (correct) script
These do not change any conclusion — the script's bookkeeping is internally consistent and gives the stated closures — but they should be corrected before the note is cited, because a reader following the prose alone would not reach $r^{-2}J_6$:

1. **§3.5(i)**: text writes the branch as "$a^3|da|^2\cdot s\cdot s=4a^4|d\chi|^2s^2$" and then "$\le Cr^{-2}J_6/\text{density}$". Since $q\sim a^4s^2$ and $B\sim s$, the product carries $s^3$, so the correct integrand is $a^3|da|^2s^3=4a^4|d\chi|^2s^3\le4r^{-2}\cdot(\text{$J_6$ integrand})$. Script (D5a) has $(m-3,m/2)=(3,3)$, i.e. $s^3$, which is right. The stray "$/\text{density}$" and the $s^2$ should read $s^3$.

2. **§3.6(a)**: text writes $I_2\le C\int\eta^2a^4|da|s^{3/2}|\nabla E|$ and says it has "the same structure as $I_1$", but $I_1$ in (3.4a) is $s^{5/2}$. The correct power is $s^{5/2}$: the term $\langle E,2a^k\nabla_kE\rangle=\langle\nabla a,\nabla s\rangle$ tested with $q\sim a^4s^2$ gives $a^4|da|s^2\cdot s^{1/2}|\nabla E|=a^4|da|s^{5/2}|\nabla E|$. Only $s^{5/2}$ Young-closes to $r^{-2}J_6$; $s^{3/2}$ would leave $\int a^4 s$, which is not $J_6$. Script (D6) has $(m-2,(m-2)/2+1/2)=(4,5/2)$, i.e. $s^{5/2}$, confirming the text digit is a typo.

3. **§2.2 schematic $|\Sigma_s|$** writes "$C(|\nabla a||\nabla E|+|\nabla^2a|)s$"; the $|\nabla a||\nabla E|$ piece originates as $\langle E,(\nabla a)\nabla E\rangle\sim s^{1/2}|\nabla a||\nabla E|$, so the natural weight on that piece is $s^{1/2}$, not $s$. The detailed §3.4–3.6 estimates use the correct powers; the summary line is loose.

Minor: §3.1 writes $\partial_t d\mu=a\tau\,d\mu$, whereas Step 34 (3.3) has $\partial_t d\mu=-a\tau\,d\mu$. Under $\partial_t g=-2aE$, $\partial_t d\mu=\tfrac12\mathrm{tr}_g(\partial_t g)\,d\mu=-a\tau\,d\mu$, so the sign in §3.1 is the wrong one; it is immaterial because the term enters only under $|\cdot|\le CP_6$.

### What remains open for this to be a proved lemma
The note is explicit (§7.2–7.3) and correct that it establishes none of: existence/smoothness of the degenerate cutoff flow; the first-exit control keeping $\mathcal S(t)\le2\mathcal S(0)$, $K_2(t)\le2K_2(0)$, $\gamma(t)\le\gamma_0$; the moving-metric/Sobolev comparability; any $J_p$ Moser recurrence; and no Yau-26 statement. The $J_6$ persistence (6.2) is a conditional implication given those inputs, and the "self-contained relative to the $q=3$ seed" statement is accurate — it still consumes the $q=2$ ($K_2$) persistence and the first-exit regime. The one internal item worth tightening for citation is the full IBP-generated RHS of Step 34 (2.4) (the $\langle da,d\tau\rangle$ pieces), which is currently asserted rather than displayed/verified.

Net: statements 1–6 hold as verified above. The two-factor absorption and the constant-in-time Gronwall coefficient are the correct and simpler counterpart to A01's $Y$-route, and they are compatible with it. Correct the three $s$-power digits and the $d\mu$ sign, and write out the first-derivative terms of (2.4), and the term-level derivation is clean.