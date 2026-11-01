# TTCS Independent Branch Record

```json
{
  "step_id": 58,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step58_critical_to_subcritical_bridge.md",
    "Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md"
  ]
}
```

## Task

Independently verify the exact-flow critical-to-subcritical curvature bridge in Step 58. Check the local relative H2 inequality (including removal of the global additive constant), the estimate Y <= C S sqrt(H)(D+r^-2 H) with the correct matched supports, the integrated Y and S^2 Y bounds without any Y(0), and the q=3 propagation. Pay special attention to the distinction w2=chi F_T versus z3=a F_T^(3/2), the Sobolev-constant convention, moving metric/measure terms, and whether the shifted tensor T introduces any unaccounted derivative or source. Give explicit corrections if any load-bearing step fails; do not assume later Moser or continuation conclusions.

## Output

## Verifier Memo — Step 58 exact-flow critical-to-subcritical curvature bridge

Session S0910A03. Independent recheck of the load-bearing algebra and analytic structure in `step58_critical_to_subcritical_bridge.md`, with the imported inputs from A01 Step 34/35 and A03 Step 57. I re-derived each numbered step by hand; the arithmetic and the support bookkeeping hold. One point in §3 is terse but not erroneous. The genuinely unresolved parts are the ones the note itself marks as premises, and I state exactly what substance they still need.

### 1. Relative H-inequality (1.1) and removal of the volume-proportional additive term — correct

Every zero-order source carries an active factor $a$ and one of the forms $\int\eta^2a,\ \int\eta^2aF,\ \int\eta^2aF^2,\ \int\eta^2aF^3$. Using $0\le a\le1$ and $F\ge1$:
$aF\le F^2$ and $aF^2\le F^2$, so the first three are $\le\int\eta^2F^2=H$, and the last is exactly $Y$. The signed integration-by-parts remainders are $\le Cr^{-2}H$. Hence a term proportional to $\operatorname{Vol}(M)$ is neither generated nor needed, and (1.1) $H'+c_0D\le C_0Y+C_1(1+r^{-2})H$ is structurally sound. The moving-measure term is included correctly: $\partial_t(d\mu)=-a(s+n)d\mu$ with $|s+n|\le\sqrt n|E|\le C_nF$ gives integrand $\le C_n\eta^2aF^3=$ cubic $\le C_nY$. This matches Step 57 (7.1) in its already-sharpened form.

### 2. The bridge Y ≤ C 𝒮 √H (D + r⁻²H) with matched supports (2.4) — correct

The matched-support identity is used correctly: $\operatorname{supp}\chi\subset B_{6r}$ and $\eta=1$ on $B_{6r}$, so $\eta=1$ wherever $\chi\ne0$ and $\eta^2a=a$ everywhere. Then $Y=\int aF^3=\int F(\chi F)^2$, Cauchy–Schwarz gives $Y\le\|F\|_{L^2(\operatorname{supp}\chi)}\|\chi F\|_4^2$ with $\|F\|_{L^2(\operatorname{supp}\chi)}\le H^{1/2}$. Sobolev on $v=\chi F$, together with
$$|\nabla(\chi F)|^2\le2|\nabla\chi|^2F^2+2\chi^2|\nabla F|^2,\quad \chi^2=a,\ |\nabla F|\le|\nabla T|,\ |d\chi|\le C/r,$$
yields $\|\nabla(\chi F)\|_2^2\le C(D+r^{-2}H)$ and $\|\chi F\|_2^2\le H$. Hence (2.4). The Kato step $|dF|\le|\nabla T|$ and the equalities $\int a|\nabla T|^2=D$, $\int|d\chi|^2F^2\le Cr^{-2}H$ (support of $d\chi\subset B_{6r}$, $\eta=1$) are all valid. The direction of the argument — bound $Y$ by $H,D$ and absorb into the $H$-equation — is the correct replacement for the Step 57 §8.1 route that required $Y(0)$.

Absorption is legitimate: on the provisional interval with $C_0C\gamma\le c_0/2$, (1.1)+(2.4) give (2.5) $H'+\tfrac{c_0}{2}D\le C(1+r^{-2})H$, and for $t\le\theta r^2$, $r\le1$, $(1+r^{-2})t\le2\theta$, so $H(t)\le e^{C\theta}H(0)$ and $\int_0^tD\le CH(0)$. No circularity: (2.4) is pointwise-in-time and its integral uses only the already-bounded $\int D$, $\int H$.

### 3. Integrated Y and 𝒮²Y without Y(0) (2.7)–(2.8) — correct

$\int_0^tY\le C\Gamma(\int_0^tD+r^{-2}\int_0^tH)\le C\Gamma H(0)$ with $\Gamma=\sup_s\gamma(s)$. With $\mathcal S(s)\le C\mathcal S(0)$, $\int_0^t\mathcal S^2Y\le C\mathcal S(0)^2\Gamma H(0)=\Gamma^3$, since $\mathcal S(0)^2\Gamma H(0)=\mathcal S(0)^3H(0)^{3/2}=(\mathcal S(0)H(0)^{1/2})^3$ and $\Gamma\simeq\mathcal S(0)H(0)^{1/2}$ (from $\gamma(0)\le\Gamma\le C\mathcal S(0)(e^{C\theta}H(0))^{1/2}$). The volume cancellation $\gamma(0)\lesssim r^2\sqrt{K_0}$ follows from $\mathcal S(0)\asymp r^2V^{-1/2}$ and $H(0)\lesssim K_0V$, matching Step 34 (1.5). $Y(0)$ appears nowhere; this is the substantive correction over Step 57. Verified.

### 4. w₂ = χF versus z₃ = a F^{3/2}, and the weight matching — correct and load-bearing

The distinction is real and is used correctly. The critical $H\to\int Y$ step uses $w_2=\chi F=a^{1/2}F$; note $w_2=z_2=\eta a^{1/2}F$ (equal because $\eta=1$ on $\operatorname{supp}\chi$ and both vanish off it). The $q=3$ evolution uses $z_3=\eta aF^{3/2}$, with $z_3^2=\eta^2a^2F^3$. This matches the $a^2$-weighted dissipation $D_3^F=\int\eta^2a^2F|\nabla F|^2$ in the $K_3$ equation. The rejected variable $\eta a^{1/2}F^{3/2}$ squares to weight $a$, not $a^2$, and would not pair with the $K_3$ dissipation. The general check $z_p=\eta a^{(p-1)/2}F^{p/2}$ gives at $p=2$ the weight $a^{1/2}$ (critical) and at $p=3$ the weight $a$ (the $q=3$ variable) — internally consistent with the two Sobolev variables.

The gradient identity (4.2) $\|\nabla z_p\|_2^2\le Cp^2(D_p^T+D_p^F+r^{-2}K_p)$ checks out term by term: the $\nabla\eta$ contribution vanishes ($a=0$ there), the $\nabla(a^{(p-1)/2})$ term gives $Cp^2r^{-2}K_p$ via $|\nabla a|^2/a\le Cr^{-2}$, and the $\nabla F$ term gives $Cp^2D_p^F$.

### 5. The three-factor reaction identity (3.5) — terse but sound, one clarification

As written, $a^{p-1}F^{p+1}=(aF^3)^{1/3}(a^{p-2}F^p)^{1/3}(z_p^2)^{2/3}$ omits the $\eta$ distribution: $z_p$ carries $\eta$, so the literal right side equals $\eta^{4/3}a^{p-1}F^{p+1}$. The correct integral procedure distributes $\eta^{2/3}$ to each Hölder factor:
$$u_1=\eta^{2/3}(aF^3)^{1/3},\quad u_2=\eta^{2/3}(a^{p-2}F^p)^{1/3},\quad u_3=\eta^{2/3}(a^{(p-1)/2}F^{p/2})^{4/3},$$
giving $\int u_1^3=Y$, $\int u_2^3=K_p$, and $\int u_3^3=\int\eta^2a^{2(p-1)}F^{2p}=\|z_p\|_4^4$ exactly (the last equality uses $\eta^4a^{2(p-1)}=\eta^2a^{2(p-1)}$ since $\eta=1$ on $\operatorname{supp}a$). The exponent counts are exact: $a$-power $\tfrac13+\tfrac{p-2}{3}+\tfrac{2(p-1)}{3}=p-1$, $F$-power $1+\tfrac p3+\tfrac{2p}3=p+1$. Alternatively keeping $u_3=(z_p^2)^{2/3}$ with its $\eta^{4/3}$ bounds $\eta^2\le\eta^{4/3}$ in the favorable direction. Either reading yields a valid bound; the note's phrasing is shorthand, not an error. I recommend the even $\eta^{2/3}$ distribution be written out so the $\|z_p\|_4^4$ identity is manifestly exact.

### 6. The q=3 propagation (3.8) and the Moser exponents (§4) — arithmetic consistent

$Y(\tau)\le\tfrac4t\int_{t/4}^{t/2}Y\le C\Gamma H(0)/t$ from (2.7). Integrating (3.4) at $p=3$ from $\tau$ to $t$ with $\int_\tau^t(1+r^{-2})\le2\theta$ and $\int_\tau^t\mathcal S^2Y\le\Gamma^3$ gives $Y(t)\le CY(\tau)\le C\Gamma H(0)/t$. The self-coefficient $\mathcal S^2Y$ is not circular because its time-integral is a priori bounded (Bihari/Grönwall). The Moser ladder exponents check: $\sum p_j^{-1}=3/p_0=1$, $\tfrac23\sum p_j^{-1}=2/3$, and $\sum(\log p_j+j)/p_j<\infty$; the recurrence reduction $m_{j+1}\le(C\mathcal S)^{2/(3p_j)}L_j^{1/p_j}m_j$ uses $(3/2)/p_{j+1}=1/p_j$ correctly; the interpolation $K_{2p}=\|z_p\|_4^4$ and $K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}$ are exact (I verified the integrand geometric-mean split). The final collapse $\mathcal S^{2/3}(\Gamma H(0))^{1/3}=\Gamma$ under $\Gamma=\mathcal S H(0)^{1/2}$ is algebraically exact, giving (4.11) $\|aF_T(t)\|_\infty\le C\Gamma/t$. As the task requests, I do not treat this endpoint as independently secured: the note itself records that the full term-by-term Moser iteration is inherited from the $H_2$–$Y$–Moser chain, not re-derived in Step 58; what Step 58 supplies and I confirmed is the seed $\mathcal M_{3,0}=\int_{t/2}^tY\le C\Gamma H(0)$ and the recurrence bookkeeping.

### 7. The shifted tensor T introduces no unaccounted derivative or source — verified

$T=\operatorname{Rm}+G$, $G=\tfrac{g\owedge g}{2(n-1)}$, gives $\operatorname{Ric}(T)=E$, $|G|\le C_n$, and at each fixed time $\nabla G=0$, so $\nabla T=\nabla\operatorname{Rm}$ and $D=\int\eta^2a|\nabla T|^2$ equals A01's dissipation exactly. The only genuinely new terms are:
- $\partial_tG=-\tfrac{2a}{n-1}(E\owedge g)$, purely algebraic, $|\partial_tG|\le C_naF$; contracted with $2T$ it is $\le C_naF^2\le Y$-region, into the reaction.
- The Hessian-$a$ contraction in the $|T|^2$ evolution picks up a $\langle G,(\nabla^2a)\owedge E\rangle$ piece beyond the A01/Step 35 $B_{\rm curv}=\operatorname{Rm}*E$. Because $\nabla G=0$, its derivative is $G*\nabla E$ with $|G*\nabla E|\le C_n|\nabla E|\le C_n|\nabla T|\le C_nF|\nabla T|$, so the derivative structure $|\nabla\mathcal T|\le C|\nabla T|F_T$ used in Step 57 §5 survives, and signed integration by parts still yields $\varepsilon D+Cr^{-2}H$.
- The rough-Laplacian principal part: $\partial_tT=a\Delta T+\text{algebra}$ because $\Delta G=0$ and $\Delta_LG-\Delta G=\operatorname{Rm}*G$ is algebraic; the Bochner pair $2\langle T,a\Delta T\rangle=a\Delta|T|^2-2a|\nabla T|^2$ is therefore the correct principal identity.

So the shift moves only bounded algebraic terms; the dissipation and the reaction cubic are preserved. This part of Step 57 §§2–6 is consistent, and Step 35's index-level tensor reductions ($B_{\rm curv}=R^p{}_j{}^q{}_lE^{jl}$ via pair symmetry and first-pair antisymmetry; $B_{\rm def}$ quadratic-vanishing at $E=0$; the $\int|R|^2$-invariance scaling test at $n=4$) reproduce cleanly when I redo the contractions.

### 8. What the chain rests on and what substance is still needed

The Step 58 curvature branch $H(0)\Rightarrow H(t),\int(D+Y)\Rightarrow Y(t)\lesssim\Gamma H(0)/t\Rightarrow\|aF_T(t)\|_\infty\lesssim\Gamma/t$ is valid on any smooth provisional first-exit interval, conditional on the following inputs, each of which the note marks and none of which Step 58 proves:

1. **Moving Sobolev and metric comparability** $\mathcal S(s)\le C\mathcal S(0)$ and metric comparison on the interval. These enter (2.8), (3.8), and the choice of $\gamma_*$. The substance needed is a self-contained estimate that the metric drift $\int_0^t\|aE\|_\infty\,ds$ stays below the comparability threshold; Step 34 (6.3)–(6.4) provides $\|aE(t)\|_\infty\lesssim\delta(r^2/t)^{1/3}$ and $\int_0^T\|aE\|_\infty\lesssim\delta\theta^{2/3}r^2$, but this itself uses the $J_6$ persistence and the same first-exit premises, so the joint first-exit fixed point carrying $(\mathcal S,H,J_6,\text{support geometry})$ has not yet been closed.

2. **Smooth flow existence and continuation across the small-$a$ collar** (Step 56). Step 57 §9 is explicit that pointwise bounded curvature does not bound $C_3=\nabla^3\chi$ or higher cutoff jets, and that the next coupled pair contains $\chi C_4*U$ while $\partial_tC_3$ contains $U_2$; a finite coupled staggered hierarchy converting to fixed-background $H^{s_0}$ restart data ($s_0>n/2+4$) remains to be supplied. Until that finite hierarchy is proved, the common observation time $\theta r^2$ for the whole sequence is open.

3. **Dimension.** The energy analysis it feeds (Step 57 §6) uses the $4-n$ zero-order conformal cancellation, so it is a four-dimensional module; the shift constant $\tfrac{1}{2(n-1)}$ being written for general $n$ does not extend the energy cancellation. Correctly, Step 58 §5 states this concerns only the $\lambda<0$ Ishida–LeBrun four-dimensional setting and is not a resolution of the all-dimensional Yau Problem 26.

4. **The imported $K_p$ inequality (3.4).** Its correctness is inherited from A01 Step 34 (2.14)/Step 35 (4.4). I checked the tensor reductions and derivative-structure bounds there structurally and they are consistent, including the polynomial power $N\le5$ feeding the convergent product (4.8). The one place worth a written cross-reference in Step 58 is that (3.4) for $F_T$ (not $F_{\rm Rm}$) relies on the §7 shift argument above; that transfer is sound but is spread across Step 57 rather than restated in Step 58.

### Bottom line

Within its stated conditional setting, the Step 58 bridge is internally correct: the relative $H$-inequality, the matched-support estimate (2.4), the $Y(0)$-free integrated bounds (2.7)–(2.8), and the $q=3$ slice (3.8) all hold, and the $w_2$ vs $z_3$ weight distinction is handled correctly. The shifted tensor $T$ produces only bounded algebraic terms with preserved dissipation. The single item I would tighten in exposition is (3.5): distribute $\eta^{2/3}$ across the three Hölder factors so the $\int u_3^3=\|z_p\|_4^4$ identity reads exactly. The mathematical substance that the endpoint and the eventual common observation time still require is the joint first-exit fixed point (metric/Sobolev/$J_6$ comparability closed simultaneously), the finite coupled cutoff-jet continuation with fixed-background $H^{s_0}$ restart, degenerate-flow existence, and the fact that the entire module is four-dimensional and $\lambda<0$ Ishida–LeBrun.