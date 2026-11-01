# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md",
    "Sessions/S0910A03/workspace/notes/step35_unregularized_J6_persistence_lemma.md",
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/notes/step25_whole_support_moser_and_normalization_repair.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A01/workspace/notes/step32_nested_moser_and_tensor_audit.md",
    "Sessions/S0910A01/workspace/notes/step33_curvature_power_inequality.md"
  ]
}
```

## Task

Independently verify the conditional K2–Y–Moser smoothing layer in the Step 38 note against A01's fixed-exponent and index-level notes and A03's restored state. Check exact Sobolev convention, weights, q=2 absorption, q=3 good-slice propagation, the coefficient S^2Y on dyadic slabs, the p→3p/2 spacetime recurrence, and endpoint scalings ||aF||∞≲γ/t and ||aE||∞≲δ(r²/t)^(1/3). Determine which estimates are genuinely established conditional PDE lemmas and which still depend on unproved moving first-exit, regularized defect general-p, or continuation inputs. Pay special attention to whether the defect high-p inequality follows from the fixed unregularized J6 lemma, and whether any additive regularization source would destroy the δ scaling.

## Output

# Verification Memo: the conditional K2–Y–Moser layer in Step 38

Session S0910A03, Step 38, cross-read against A01 Step 34 (integrated potential / q=3 / two-factor J6), A01 Step 35 (index-level tensor variation), A01 Step 33 (curvature power inequality, superseded parts), A01 Step 32 (nested Moser), and A03 Step 34/25/23. I reworked the algebra of each requested link independently. Below, "established conditional lemma" means correct given the stated first-exit geometry and the two index-level tensor inequalities; "assumed" means the note itself inserts it as a premise.

## 1. Sobolev convention, weights, γ — consistent and correct

The squared convention $\|u\|_4^2\le\mathcal S(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2)$, $\mathcal S\simeq r^2/\sqrt V$, is used identically in Step 38 §4, A01 Step 34 (0.4), A03 Step 34 (1.1). The single-symbol discipline (never write an unsquared $S$ with $S^2=\mathcal S$ and then square again) is the resolution of the A03 #330/#332 episode and is respected throughout. I confirm the collapse cancellation: $\gamma=\mathcal S K_2^{1/2}\le (r^2/\sqrt V)\sqrt{K_0V}=r^2\sqrt{K_0}$, volume-free. One point to keep visible: this requires the **localized** seed $K_2^{\eta}=\int\eta^2F^2$, not $\int F^2$ (A01 Step 34 §1.1). Step 38 §4 writes $K_{2,j}=\int_{U_j}\eta_j^2F^2$, so it is on the correct side of that correction.

## 2. q=2 absorption — established conditional lemma

Step 38 (4.3)–(4.5): $K_2'+cD_2\le CY+Cr^{-2}K_2$, with $Y=\int aF^3=\int F(\chi F)^2\le\|F\|_2\|\chi F\|_4^2\le C\gamma(D_2+r^{-2}K_2)$, then $C\gamma<c/2$ gives $\sup K_2+\int D_2\le CK_2(0)$ and $\int_0^tY\le C\gamma K_2(0)$. I reproduced the Hölder split $(2,4,4)$ and the gradient bound $\|\nabla(\chi F)\|_2^2\le CD_2+Cr^{-2}K_2$; both are exact. This matches A01 Step 34 (3.1)–(3.6). It is a genuine PDE lemma once the q=2 tensor energy inequality holds, and that inequality is now derived at index level in A01 Step 35 §4 (Besse variation, all-lower curvature, the normalization cancellation §2.1/§2.3, and the signed Hessian tensor $B_{\rm curv}^{pq}=R^p{}_j{}^q{}_lE^{jl}$ with $|\nabla B_{\rm curv}|\le CF|\nabla\mathrm{Rm}|$). The scaling test $\partial_t\int|R|^2d\mu=0$ in $n=4$ is verified and confirms no spurious pointwise damping was used.

## 3. q=3 good-slice propagation and $\mathcal S^2Y$ on dyadic slabs — correct given the q=3 inequality and first-exit

Step 38 (4.6)–(4.9): $Y'+cD_3\le Cr^{-2}Y+C\int a^2F^4$, absorb $\int a^2F^4=\int Fu^2\le C\gamma(D_3+r^{-2}Y)$ ($u=aF^{3/2}$), giving $Y'\le Cr^{-2}Y$, then a good slice $\tau\in[t/4,t/2]$ with $Y(\tau)\le(4/t)\int_0^{t/2}Y\le C\gamma K_2(0)/t$ propagated forward yields $Y(t)\le C\gamma K_2(0)/t$ and $\mathcal S^2Y(t)\le C\gamma^3/t$. I verified the arithmetic; it matches A01 Step 34 (4.1)–(4.4).

Two structural facts are worth naming for the record. First, the forward propagation is only bounded because $\int_\tau^t\mathcal S^2Y\le C\gamma^3$ (A01 Step 34 (3.7), the integrated potential $B(t)\le C\gamma^3$), which in turn uses $\mathcal S(s)\le2\mathcal S(0)$ — a first-exit premise, not a theorem. Step 38's compressed "$Y'\le Cr^{-2}Y$" (4.8) is legitimate only after that self-coupling term is absorbed by $B(t)$. Second, the note correctly uses the **pointwise ess-sup** dyadic bound $\mathcal S^2Y(t)\le C\gamma^3/t$ as the Moser coefficient, not a time-average. This is the exact A03 Step 34 §4 correction: a time-average of $\mathcal S^2Y$ does not control $\int_I(\mathcal S^2Y)K_p$ because the coefficient can correlate with $K_p$. Step 38 §5 respects this.

## 4. $p\mapsto 3p/2$ recurrence and endpoint arithmetic — verified

The interpolation $H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2$ checks by Cauchy–Schwarz with the weight identity $(p-2)/2+(p-1)=3p/2-2$ (a-exponent) and $p/2+p=3p/2$ (f-exponent). The product converges: $p_k=p_0(3/2)^k$, $\sum 1/p_k=3/p_0$, polynomial $p_k$ and dyadic $4^k$ losses summable. Both endpoints are arithmetically exact:

- Curvature $p_0=3$: $\mathcal S^{2/3}t^{-1}(\gamma K_2)^{1/3}$; using $K_2=\gamma^2/\mathcal S^2$ this collapses to $\|aF\|_\infty\lesssim\gamma/t$. Confirmed.
- Defect $p_0=6$: $\mathcal S^{1/3}t^{-1/2}(\delta^6Vt)^{1/6}$ with $\mathcal S\simeq r^2V^{-1/2}$ gives $\delta r^{2/3}t^{-1/3}=\delta(r^2/t)^{1/3}$, volume cancelling exactly; the time integral $\int_0^{\theta r^2}=C\delta\theta^{2/3}r^2$. Confirmed.

Note the asymmetry the note states plainly: $\|aF\|_\infty\lesssim\gamma/t$ is **not** integrable at $t=0$, so it does not bound metric drift; only the integrable defect endpoint feeds $\partial_tg=-2aE$. The first-exit closure therefore hinges entirely on the defect endpoint, which routes back to §6–7 below.

## 5. The unregularized $J_6$ lemma — the strongest solid piece, but only a seed

A01 Step 35 §5–6 reproduces A03 Step 35 from first principles: the defect Hessian tensor $B_{\rm def}^{pq}=|E|^2g^{pq}+(\mathrm{tr}E)E^{pq}-2(E^2)^{pq}$ with $B_{\rm def}|_{E=0}=0$, $|B_{\rm def}|\le Cs$, $|\nabla B_{\rm def}|\le Cs^{1/2}|\nabla E|$, and the factor-2 match to A03's $q=3\eta^2a^4s^2$ test function. I checked the internal algebra of Step 35 independently:
- chain rule (2.3) for $s^3$ with the favorable $-6as|\nabla s|^2\le0$;
- §5.4 third term $=9X_6$ via $|\nabla s|^2\le4s|\nabla E|^2$;
- the Young split of the cutoff cross term using $a^3|da|^2=4a^4|d\chi|^2\le4r^{-2}a^4$;
- the two-factor absorption $P_6=\int Fw_6^2\le\|F\|_2\|w_6\|_4^2\le C\gamma(X_6+r^{-2}J_6)$.

All are exact. The resulting inequality $J_6'+cX_6\le C(1+r^{-2})J_6$ is genuinely **homogeneous** — no additive source, no $Y$, no $\varepsilon$. This is the cleanest established conditional lemma in the whole layer and gives $J_6(t)\le e^{C(1+r^{-2})t}J_6(0)\le C\delta^6V$. It correctly avoids the nonintegrable $1/t$ curvature coefficient.

**But it is only the $p_0=6$ seed.** Step 35 §7.2 item 1 says so explicitly: the Moser endpoint (7.1) "uses the curvature Moser chain, not the $J_6$ lemma itself."

## 6. Does the defect high-p inequality follow from the $J_6$ lemma? — No

This is the crux you asked about. Step 38 §5 (5.2) **assumes** the general-p defect power inequality $H_p'(f)+c\|\nabla z_p\|_2^2\le Cp^N(r^{-2}+1+\mathcal S^2Y)H_p$ "with no curvature-only source." The $J_6$ lemma does not supply this; it fixes only $p=6$. The Moser ladder is $p_k=6(3/2)^k=6,9,13.5,\dots$

The subtle mathematical point: Step 35's unregularized trick worked because $s^3=|E|^6$ is a genuine polynomial in the components of $E$, hence smooth, so no Kato approximant was needed. For the ladder one needs $s^{q_k}$ with $q_k=p_k/2=3,4.5,6.75,\dots$. Here is the balance the notes do not resolve in writing:

- $s=|E|^2$ is itself a smooth polynomial for **every** $q$. For $q\ge1$, $s^q$ is $C^1$, and the chain-rule identity $(\partial_t-a\Delta)s^q=qs^{q-1}(\partial_t-a\Delta)s-aq(q-1)s^{q-2}|\nabla s|^2$ has $s^{q-2}|\nabla s|^2\le4s^{q-1}|\nabla E|^2$ bounded for $q\ge1$, with the favorable sign $q(q-1)\ge0$. Structurally this suggests Step 35's $s$-power method **does** extend to the whole ladder $q_k\ge3$ in unregularized homogeneous form, which would give (5.2) with no additive source.
- No note actually writes this general-$q$ derivation. The only written general-p defect inequality is A01 Step 33 §4 (4.4), which uses the Kato regularization $f_\varepsilon=(|E|^2+\varepsilon^2)^{1/2}$ and carries an additive source $C_0'p$.

So the answer is definite: the defect high-p inequality is currently an **assumed** premise, not a consequence of the $J_6$ lemma, and its cleanest completion is the (still unwritten) unregularized $s^{q}$-power derivation.

## 7. Would an additive regularization source destroy the $\delta$ scaling?

In principle yes: an additive term in $J_p'$ that is proportional to a pure-curvature integral like $\int a^{p-1}F^{p+1}$ and independent of $E$ would give a $\delta$-independent floor in $\|aE\|_\infty$, breaking the $\delta(r^2/t)^{1/3}$ endpoint and hence the metric-drift-driven first-exit closure.

Whether it actually does depends on the exact source. The evidence points to survival of $\delta$ scaling, but the argument is complete only at $p=6$:
- The exact $s$-equation (Step 35 (2.2), A01 Step 35 §5.3) reads $(\partial_t-a\Delta)s=-2a|\nabla E|^2+\Sigma_s$ with $|\Sigma_s|\le CaFs+$(cutoff), and the Hessian source vanishes quadratically ($B_{\rm def}|_{E=0}=0$). **Every** term carries a factor $s$ or $|\nabla E|^2$; there is no bare $E$-independent source at the differential level, for any power. This is the structural reason A01 Step 33 §4.1 gives ("$E=0$ is preserved by the flow").
- The regularized route's additive $C_0'p$ comes only from $f_\varepsilon^p\to\varepsilon^p$ on $\{E=0\}$; it scales as $\varepsilon^p$ and vanishes as $\varepsilon\to0$. A01 Step 33 §4.1 asserts this for $p=6$; Step 35 removes even that by never regularizing.

What is not written anywhere is the interchange of $\varepsilon\to0$ with the infinite Moser ladder: one must obtain an $\varepsilon$-uniform endpoint and then pass to the limit, verifying the accumulated $\varepsilon$-sources along $p_k\to\infty$ do not sum to a $\delta$-independent constant. Because the unregularized $s$-power method (§6) appears to make regularization unnecessary in the first place, the most reliable path is to write (5.2) unregularized rather than to control the $\varepsilon\to0$ limit of an infinite iteration. Until one of these is written, the $\delta$-linearity of (5.7) — and therefore the entire metric-drift closure — is credible on homogeneity grounds but not a finished lemma.

## 8. What is genuinely established (conditional) versus still open

Established as conditional PDE lemmas (given first-exit geometry + the two index-level tensor inequalities of A01 Step 35):
- q=2 curvature persistence and $\int_0^tY\le C\gamma K_2(0)$;
- integrated potential $B(t)\le C\gamma^3$ and the q=3 good-slice endpoint $\mathcal S^2Y\lesssim\gamma^3/t$;
- the $p\mapsto3p/2$ spacetime recurrence, its convergent product, and the endpoint arithmetic $\|aF\|_\infty\lesssim\gamma/t$, $\|aE\|_\infty\lesssim\delta(r^2/t)^{1/3}$ **once the corresponding power inequality is granted**;
- the unregularized $J_6$ persistence lemma with $\delta^6$ seed and no additive source (the firmest single result);
- the signed Hessian-cutoff lemma §1 (I verified the IBP $J=-\int\nabla_i\chi\nabla_j\chi B^{ij}-\int\chi\nabla_j\chi\nabla_iB^{ij}$ and the Young step (1.5)) and its m=2 application (2.6).

Still resting on unproved inputs:
- **Moving first-exit bootstrap**: $\mathcal S(t)\le2\mathcal S(0)$, $K_2(t)\le2K_2(0)$, metric comparability, support geometry, closed simultaneously. Everything in §3–5 is conditional on it. The closure is meant to be self-improving via the integrable defect drift, but that drift itself depends on §6–7.
- **General-p defect power inequality (5.2)**: assumed, not derived; the honest completion is the unwritten unregularized $s^{q}$-power derivation (§6).
- **Degenerate cutoff-flow existence / short-time / continuation**: assumed. The higher shifted-curvature continuation induction is explicitly open (Step 38 §3): the signed Hessian lemma handles single-Hessian terms $\chi\nabla^2\chi*\nabla^mU$, but the top-jet/lower-curvature couplings (3.2), $\chi\nabla^{m+1}\chi*\nabla U*|\nabla^mU|^{p-2}\nabla^mU$ after IBP, need a finite-exponent induction schedule that is not written.

The note's own §6 states all of this and states that even full completion addresses only the restricted four-dimensional Ishida–LeBrun family, not the positive branch, $n\ge5$, dimension-only constants, or Lean formalization. That framing is accurate.

## 9. Minor textual items affecting reading, not the result

- Step 35 §3.6a displays $I_2\le C\int\eta^2a^4|da|s^{3/2}|\nabla E|$; the surrounding structure (matching §3.4a and the $(2,2)$ Young step to $\varepsilon X_6+C_\varepsilon r^{-2}J_6$) requires $s^{5/2}$. A01 Step 34 §5 already records this as a typo with the intended $s^{5/2}$. The final estimate is unaffected — I verified the split $a^4s^{5/2}|da|\to(a^{5/2}s|\nabla E|)(a^{3/2}s^{3/2}|da|)$ gives exactly $X_6$-density and $r^{-2}J_6$-density.
- Step 38 §0 says the old I_{1c}, I_3 had "total power $p+1$" whereas the m=2 single-Hessian term $\int|V|^{p-2}V*(\chi\nabla^2\chi*V)$ has V-power $p-1+1=p$. The m=2 accounting in §2 is internally correct (power $p$); the "$p+1$" remark refers to a different Step 37 grouping and should not be read as applying to (2.6).
- A01 Step 33 §2.6 and §2.6 "TTCS correction" correctly retract the invalid "IBP on $|\nabla^2a|$" and replace it by either the pointwise evolving-Hessian route or the signed tensor IBP; Step 38's signed lemma is the same repair. These are consistent; a reader should treat A01 Step 33 (3.1) with the $-p(p-3)D_p^F$ coefficient as superseded by A01 Step 34/35's $-p(p-2)D_p^F$.

## Bottom line for the requested question

The K2–Y–Moser chain is algebraically sound and its two endpoints are arithmetically exact. The defect high-p endpoint (5.7) does **not** follow from the fixed $J_6$ lemma — it requires the general-p defect power inequality (5.2), which is presently a premise. An additive regularization source, if it were a pure-curvature $E$-independent term, would break the $\delta$ scaling; the exact $|E|^2$-equation is homogeneous for all powers (every source term carries $s$ or $|\nabla E|^2$, and $B_{\rm def}|_{E=0}=0$), so the source should carry an $\varepsilon^p\!\to\!0$ factor and the cleanest resolution is to write (5.2) unregularized using powers of the smooth quantity $s=|E|^2$ — an extension of Step 35 that the notes have not yet produced. Until that derivation and the simultaneous first-exit/existence/continuation inputs are written, the endpoints $\|aF\|_\infty\lesssim\gamma/t$ and $\|aE\|_\infty\lesssim\delta(r^2/t)^{1/3}$ are conditional consequences, with the $\delta$-linearity of the defect endpoint the single most load-bearing unfinished element.