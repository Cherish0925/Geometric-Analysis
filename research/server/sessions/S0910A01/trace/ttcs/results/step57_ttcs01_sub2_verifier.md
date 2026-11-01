# TTCS Independent Branch Record

```json
{
  "step_id": 57,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step57_preceptor_deTurck_uniqueness_and_scope_review.md",
    "Sessions/S0910A01/workspace/notes/step56_common_time_and_terminal_compactness.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md",
    "Sessions/S0910A03/workspace/notes/step59_finite_regularity_continuation_and_common_time.md",
    "Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md"
  ]
}
```

## Task

Verify the Step57 repair note for the restricted Ishida--LeBrun cutoff-flow route. Focus on the load-bearing issues, not style: (1) Is the rejection of Step56's raw metric-difference uniqueness argument mathematically justified? (2) Does the proposed coupled transported-cutoff DeTurck pair uniqueness energy for H=G1-G2 and b=beta1-beta2 plausibly close on a smooth per-datum overlap, especially the metric Lie-cross term, scalar transport term, and need for averaged (beta1^2+beta2^2)|DH|^2 dissipation? Identify any missing derivative, coefficient, or gauge-reconstruction issue. (3) Does the note correctly keep finite current-pair induction as an unfinished proof dependency rather than assuming it? (4) Does the corrected scope preserve the IL-class uniform A-cancellation and avoid the old topology-shrinking threshold or a mistaken no-Einstein conclusion? Return a concise mathematical memo with any necessary repairs or confirmations.

## Output

## Verifier memo — Step 57 repair of the fixed-cutoff overlap uniqueness and the coverage statement

Session S0910A01. Independent check of `step57_preceptor_deTurck_uniqueness_and_scope_review.md` against the Step 56 (A01, A03) and Step 55/59 material supplied.

---

### 1. Rejection of the raw metric-difference estimate is well-founded

The linearization of the Ricci tensor is
$$
D\operatorname{Ric}(h)_{ij}=-\tfrac12\Delta_L h_{ij}
+\tfrac12\bigl(\nabla_i\nabla^k h_{kj}+\nabla_j\nabla^k h_{ki}-\nabla_i\nabla_j\operatorname{tr}h\bigr),
$$
the second block being $\operatorname{sym}(\nabla\mathcal B h)$ with $\mathcal B$ the Bianchi operator. Step 56 §2.6 used only $-\tfrac12\Delta_L h$, i.e. it silently discarded exactly the DeTurck gauge block. For the fixed-cutoff flow the relevant operator is $-2a\,D\operatorname{Ric}(h)-2a\,h$, so the same gauge block survives, weighted by $a$. The note's decisive point is correct: with $h=\mathcal L_X g$ one has $D\operatorname{Ric}(h)=\mathcal L_X\operatorname{Ric}$, so the operator has a large degenerate direction set and no coercive $\int a|\nabla h|^2$ dissipation can be extracted from the raw difference. The displayed $\tfrac{d}{dt}\int|h|^2\le-\int a|\nabla h|^2+C\int|h|^2$ is therefore unsupported. This is a repair of the estimate, not a statement that overlap uniqueness is false; the gauge-compatible route is the right response. Confirmed.

---

### 2. The coupled DeTurck pair energy closes on a smooth per-datum overlap

I reconstructed the energy independently. The load-bearing steps hold.

**Averaged principal coefficient is legitimately obtained, not postulated.** With $P_i=\beta_i^2G_i^{ab}$ (principal coefficient) and $F_i=D_aD_bG_i$,
$$
P_1F_1-P_2F_2=\underbrace{\tfrac12(P_1+P_2)}_{\bar A^{ab}}(F_1-F_2)
+\tfrac12(P_1-P_2)(F_1+F_2).
$$
The first term is $\bar A^{ab}D_aD_bH$ with $\bar A=\tfrac12(\beta_1^2G_1+\beta_2^2G_2)$; the remainder is (coefficient difference)$\times$(bounded $D^2G$ sum) $=\mathcal A_0*H+\mathcal B_0*b$ using the $C^3$ bound. Since $G_i\ge\lambda\bar g$, integration by parts gives $-c\!\int(\beta_1^2+\beta_2^2)|DH|^2$ with $c=\tfrac12\lambda$. So the two-sided dissipation weight is real, and the symmetric split is exactly what produces it. Good.

**Every $DH$-linear term carries at least one $\beta$-power, which is why the degenerate dissipation suffices.** I checked the origins: the drift $\int H\,D\bar A\,DH$ has $|D\bar A|\le C(\beta_1+\beta_2+\beta_1^2+\beta_2^2)$; the $Q(G,DG)$ difference contributes $\beta_i^2\cdot(\text{bounded})*DH$; the Lie term $2\operatorname{sym}(d(\beta^2)\otimes W)$ contributes $\beta_i(\text{bounded})*DH$ through $d(\beta^2)=2\beta D\beta$. In each case weighted Young against $(\beta_1^2+\beta_2^2)|DH|^2$ absorbs the derivative and leaves $C|H|^2$. No non-$\beta$-weighted $DH$ coefficient appears; on the interior of $\{\beta\equiv0\}$ the whole metric right side is stationary, so $H$ is stationary there and the degeneracy is harmless. This is the correct reason the estimate does not require full parabolicity across the collar.

**The metric $\mathcal B_1*Db$ (scalar-derivative) term.** $\mathcal B_1\sim(\beta_1+\beta_2)W(G_2)$, i.e. it carries a $\beta$-power. One integration by parts (note (2.6)) sends the derivative off $b$: $-\int b\,D(H\mathcal B_1)=-\int b(\,DH\,\mathcal B_1+H\,D\mathcal B_1)$. The first piece is $(\beta_1+\beta_2)|b||DH|\le\varepsilon(\beta_1^2+\beta_2^2)|DH|^2+C|b|^2$; the second needs $D\mathcal B_1\sim D^2G_2$ bounded ($C^2$ of $G$). Both close. Confirmed.

**Scalar transport energy.** $\partial_tb=\beta_1^2W(G_1)\!\cdot\!Db+(\beta_1^2W(G_1)-\beta_2^2W(G_2))\!\cdot\!D\beta_2$ is exactly the subtraction of the two $\beta$-equations. The advective term gives $-\tfrac12\int\operatorname{div}(\beta_1^2W(G_1))\,b^2$, bounded because $\operatorname{div}(\beta_1^2W)\sim D^2G_1$ is bounded — there is no scalar diffusion and none is needed. The cross term, via $W(G_1)-W(G_2)=A_1*DH+A_0*H$ and $\beta_1^2-\beta_2^2=b(\beta_1+\beta_2)$, splits into $\beta_1^2|DH||b|$ (absorbed by the metric dissipation) plus $|H||b|+b^2$. The note's remark that the $DH$-in-scalar term can appear with weight $\beta_2^2$ under a different grouping is the correct motivation for carrying the **averaged** $(\beta_1^2+\beta_2^2)|DH|^2$ rather than $\beta_1^2|DH|^2$ alone; both groupings are then covered. Consistent.

**Coupling structure is complete.** The metric equation contains $b,Db$ but no $D^2b$ (the scalar enters the metric equation only through $\beta^2$ and $d(\beta^2)$); the scalar equation contains $H,DH$ but no $D^2H$ (through $W\sim DG$). So the highest cross-couplings are first order both ways, the metric supplies $D^2H$ dissipation, the scalar is pure transport, and the two first-order couplings are handled respectively by the one integration by parts and by absorption. No derivative is missing. The regularity in (2.2) ($C^3$ on $G_i$, $C^2$ on $\beta_i$) is comfortably sufficient — the estimate uses at most $D^2G$; nowhere $D^3G$. Adding $A\times$(scalar) to (metric) and Grönwall gives $H\equiv b\equiv0$. The pair uniqueness itself is sound.

**One piece is stated but not written: the gauge reconstruction.** The matched initial data is fine — both geometric solutions on the restart slab share $g(\tau)=g(t_j)$, and gauging each with $\varphi_i(\tau)=\mathrm{id}$ gives $G_i(\tau)=g(\tau)$ (equal) and $\beta_i(\tau)=\chi$ (equal), so $H(\tau)=b(\tau)=0$. The clean direction also holds: once $(G,\beta)$ agree, the transport ODE $\partial_t\varphi=-\beta^2W(G)\circ\varphi$ depends only on $(G,\beta)$, so $\varphi_1=\varphi_2$ and $g_i=\varphi_i^*G_i$ agree. What is not written is the **forward gauging existence**: that each given smooth geometric solution actually arises from a pair $(G_i,\beta_i)$ through a gauge map $\varphi_i$ solving the coupled relation $G_i=(\varphi_i^{-1})^*g_i$, $\partial_t\varphi_i=-\beta_i^2 W(G_i)\circ\varphi_i$ on the full overlap. On a compact manifold with smooth data and $\beta^2$ vanishing on an open collar (where $\varphi$ is stationary) this is expected, but the note itself says the correspondence "still has to be written carefully," and this is the remaining analytic content of the repair. A robustness alternative worth noting is a Kotschwar-type energy method (a single coercive energy in the difference of metric, connection, and curvature) that proves uniqueness without a gauge-reconstruction step; adapting it to the $a=\chi^2$ normalization and the scalar $\beta$ would remove dependence on the gauging existence entirely.

---

### 3. Finite current-pair induction is correctly held as unproved

§3 states the target evolution (3.2)–(3.3) and lists the five tensor facts a proof must exhibit — in particular that no $C_{m+2}*U$ or $C_{m+2}*T$ term appears without the leading $\chi$, and that time-connection commutators produce at most $C_1*U_m$ rather than requiring $U_{m+1}$ before the current pair is controlled. That last property is the one that separates a closing finite-triangular induction from an infinite derivative ascent, and it is named explicitly. The note states plainly that until the commutator expansion is written the common-time continuation depends on more than per-datum existence, and that the allocation scripts (14,002,305 partitions in Step 56 A03) check only integer allocation and interpolation exponents, not the tensor identities or the PDE argument. This bookkeeping is accurate and matches Step 56 §6.2 Module D and Step 59 §9. Confirmed as an open dependency, not assumed.

---

### 4. The coverage statement, the $A$-cancellation, and a cross-note discrepancy

**$A$-cancellation is correct.** Step 56 §5 supplies $\int\Phi_i\le119\,e^{C\theta}Q_i(0)$ with $Q_i(0)\le\delta_i^2\operatorname{Vol}(M)$ and $\operatorname{Vol}(M)/A_i\le C$, hence $\int\Phi_i\le C\delta_i^2A_i$; the proportional-volume selection gives $\operatorname{Vol}(P_i^{\rm in})\ge c_0A_i$; averaging $\mathcal A_\rho\Phi$ over $P_i^{\rm in}$ then yields a center with $\mathcal A_\rho\Phi(p_i)\le C c_0^{-1}\delta_i^2$. Both the integral upper bound and the selection volume scale linearly in $A_i$, so $A_i$ genuinely cancels. If $C,c_0,K,\rho,\eta$ and the ratio $\operatorname{Vol}/A$ are uniform over the stated Ishida–LeBrun class, the resulting pinching gap $\varepsilon_{\rm IL}>0$ is uniform over that class. This is a correct improvement over the earlier shrinking-with-topology accounting, and it is contingent on those constants being uniform — which itself rests on the still-open analytic modules (per-datum existence + overlap uniqueness, curvature/defect Moser endpoints, finite current-pair induction, terminal density). The forbidden-germ lower bound $\eta>0$ is not vacuous: I checked the calibrated density arithmetic ($s=-4\Rightarrow|W^+|^2=1/24$, spectrum $(-\tfrac16,\tfrac1{12},\tfrac1{12})$) is incompatible with the Ric$=-g$ Kähler value $|W^+|^2=2/3$, spectrum $(-\tfrac23,\tfrac13,\tfrac13)$, so the Derdziński obstruction fires.

**The no-Einstein misstatement is correctly avoided.** §4 states the theorem excludes arbitrarily tight $\lambda=-1$ Ricci-pinched *input* metrics on the Ishida–LeBrun topologies, and observes those topologies already obstruct exact Einstein metrics by separate gauge-theoretic arguments. That distinction is the right one for Yau 26: its hypothesis is a two-sided Ricci interval and its output sign is free, so the logical value of a completed restricted theorem is the removal of candidate $\lambda=-1$ counterexamples from that geography, not a proof of existence and not a dimension-only statement. The note's own summary that $n\ge5$, the positive branch, arbitrary four-manifold topology, dimension-only constants, and Lean formalization all remain untouched is accurate.

**Discrepancy to reconcile.** Step 59 (A03) §7, "Note on $\delta_0$," still asserts $\delta_0\le c/\sqrt{A}$, i.e. the gap shrinks as topological complexity $A$ grows, and calls this structural. This directly contradicts the $A$-cancellation in Step 57 §4 and Step 56 §5.4. The two accountings differ in the terminal lower bound: the $c/\sqrt A$ version corresponds to a *fixed* positive lower bound on $\int\Phi$ (one forbidden germ, one ball volume), while the cancellation version uses $\eta\cdot\operatorname{Vol}(P^{\rm in})\sim\eta A$. The proportional-volume averaging in Step 56 §5.3 is the stronger argument and, if its constants are uniform, supersedes the $1/\sqrt A$ remark. This is load-bearing: the entire point of the corrected coverage is a gap uniform over the class. If instead the uniformity of $C,c_0,K,\eta,\operatorname{Vol}/A$ over the class does not hold, the $A$-cancellation does not deliver a class-uniform gap and Step 57 §4 would be stronger than the analysis supports. The unresolved item the core work needs is an explicit statement of which of the constants $C,c_0,K,\rho,\eta,\operatorname{Vol}/A$ are proved uniform over the Ishida–LeBrun family independent of the summand count entering $A$; the two notes cannot both stand as written until that is settled.

---

### Summary of what is confirmed and what remains to be supplied

- The rejection of the raw uniqueness estimate is mathematically justified (correct gauge block, diffeomorphism degeneracy).
- The coupled pair energy closes on a smooth per-datum overlap; the averaged $(\beta_1^2+\beta_2^2)|DH|^2$ dissipation is correctly derived, every $DH$-linear term carries a $\beta$-power, the Lie cross term and scalar transport are handled correctly, and the regularity hypotheses suffice.
- The remaining analytic content of the repair is the forward gauge-correspondence existence (constructing each $(G_i,\beta_i)$ from the given geometric solution), which the note states but does not write; a Kotschwar-type direct energy method is an alternative that avoids it.
- The finite current-pair induction is correctly carried as an open dependency, with the crucial no-$U_{m+1}$-ascent property named.
- The $A$-cancellation and the "excludes tight input, not existence" framing are correct; but the $\delta_0\le c/\sqrt A$ remark in Step 59 §7 contradicts it, and the class-uniformity of the terminal constants is the specific fact whose proof would make the cancellation stand.