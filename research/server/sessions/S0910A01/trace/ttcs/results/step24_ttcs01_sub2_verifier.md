# TTCS Independent Branch Record

```json
{
  "step_id": 24,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step24_buffered_support_energy_test.md",
    "Sessions/S0910A01/workspace/scripts/step24_buffered_support_algebra.py",
    "Sessions/S0910A01/workspace/notes/step20_closed_tensor_estimate.md",
    "Sessions/S0910A01/workspace/notes/step16_preceptor_review_smoothing_architecture.md",
    "Sessions/S0910A03/workspace/notes/step22_critical_energy_lemma_formulation.md"
  ]
}
```

## Task

Verify the Step 24 buffered selected-support energy formulation for the normalized cutoff flow in the Yau 26 four-dimensional negative LeBrun laboratory. Read the note and script together with the prior tensor-structure note and support-geometry correction. Focus on whether separating the physical cutoff chi from the auxiliary energy cutoff eta really avoids bad-center/all-center smallness, whether the weighted cubic moment is the right one for the q=2 and q=3 estimates, whether the time-average propagation for A^4 H3(t) is mathematically justified or needs repair, and whether the triangular Q estimate has hidden terms or unsupported assumptions. Return a direct scientific memo: valid structural points, precise mathematical gaps, corrections, and which exact inequalities remain load-bearing.

## Output

## Verifier memo — Step 24 buffered selected-support energy formulation

Read against Step 20 (closed tensor ledger), Step 16 (support-geometry correction), Step 22 (A03 lemma statement), and the Step 24 script. I reproduced the key absorptions by hand. Summary: the $\chi/\eta$ separation is a genuine structural advance and Sections 1–5 and 7 are essentially sound modulo the unproven exact tensor identities; Section 6 reaches a correct conclusion through a mis-derived reaction bound that should be replaced by a cleaner linear absorption; the single-support machinery does not by itself deliver the volume-integrated defect the topological recalibration needs.

### 1. The $\chi/\eta$ separation does remove the all-center input, for the local estimates

This is the real content and it holds. Because the energy cutoff $\eta$ is supported in $\Omega_\eta=B_{L_\eta r}(p)$ centered at the selected good point $p$ with $L_\eta r\le R_0$, the single maximal-function value $\mathcal M_{R_0}(|\operatorname{Rm}|^2)(p)\le K_0$ directly gives $\int_{\Omega_\eta}|\operatorname{Rm}|^2\le K_0\operatorname{Vol}(\Omega_\eta)$ by taking radius $\rho=L_\eta r$. No neighboring-center value and no Li all-center hypothesis enters. This is the correct repair of the Step 23 net, whose centers could lie outside the good set. The critical product then obeys $\beta_0=A_\Omega^2\|F(0)\|_{L^2(\Omega_\eta)}\le C(L_\eta)r^2\sqrt{1+K_0}$, and the volume cancellation is the standard 4D relative-Sobolev scaling $A_\Omega^2\sim\rho^2\operatorname{Vol}^{-1/2}$ (since $2/n=1/2$). Collapse-independence is correct.

The collar cancellations (1.1) are valid coefficient-support facts, not finite-propagation assertions. The note's insistence on $\operatorname{supp}\nabla\eta\subset\{\chi=0\}^\circ$ (open interior) is exactly right and matters: on that open set not only $a=0$ but $\nabla a=0$ and $\nabla^2a=0$, so the metric and the curvature are literally frozen there ($\partial_t\operatorname{Rm}$ has every term proportional to $a$ or its derivatives, all vanishing on the collar). This cleanly settles the Step 16 concern about parabolic propagation into the transition annulus without invoking any speed estimate. The boundary-of-support Hessian effects, where $\nabla a,\nabla^2a\ne0$, sit inside $\{\eta=1\}$ and are precisely the Step 20 §4 Hessian-cutoff terms captured by the energy.

### 2. $q=2$ closed estimate (Sections 3–5): sound modulo exact tensor identity

I checked the critical cubic absorption (4.1) directly. With $\eta=1$ on $\operatorname{supp}a$, $R_2=\int(\chi F)^2F\le\|F\|_{L^2(\Omega_\eta)}\|\chi F\|_{L^4}^2$, and $\|\nabla(\chi F)\|_2^2\le C(D_2+r^{-2}H_2)$ using $\int\chi^2|\nabla F|^2=D_2$ and $\int|\nabla\chi|^2F^2\le Cr^{-2}H_2$. This gives $R_2\le C\beta(t)(D_2+Cr^{-2}H_2)$ exactly as written. The first-exit self-improvement of $\beta(t)\le2\beta_0$ and the closed inequality (4.2) then follow. The integrated cubic (5.1) uses only the easy comparability $H_2(0)\le\|F\|_{L^2(\Omega_\eta)}^2$: $\int_0^TR_2\le C\beta_*H_2(0)\le C\beta_*\|F\|_2^2=C\beta_*^3A_\Omega^{-4}$, so $A_\Omega^4\int_0^TR_2\le C\beta_*^3$. Correct.

The one item not yet established is (3.1) itself — the whole-support $H_2$ tensor inequality. The Step 20 ledger makes it plausible: at $q=2$ the $q^3$-type coefficient degeneration is absent, the $-q(q-2)$ term vanishes, and $|\nabla a|^2/a=4|\nabla\chi|^2\le Cr^{-2}$ carries no inverse power of $\chi$ (the apparent $1/a$ is compensated by the factor $a$ inside $|\nabla a|^2=4a|\nabla\chi|^2$). This is exact-constant bookkeeping, not a structural obstruction, but it is load-bearing and not yet written.

### 3. Section 6: the conclusion (6.5) is correct, the reaction bound (6.2) is mis-derived

I identified the $q=3$ reaction correctly: differentiating $Y=\int\eta^2aF^3$ and inserting the cubic term $CaF^3$ from $\partial_tF^2$ gives $\tfrac32\int\eta^2a\cdot F\cdot CaF^3=C\int\eta^2a^2F^4$, and the additive $Cr^{-2}F^2$ normalization term gives $Cr^{-2}Y$. So (6.1) has the right reaction. But (6.2) is not the natural bound. Two problems:

- **$D_3$ is never defined**, and its correct weight is $a^2$: the dissipation produced is $\int\eta^2a^2F|\nabla F|^2\sim\int\eta^2a^2|\nabla F^{3/2}|^2$. The moment $Y$ carries weight $a$, the dissipation carries weight $a^2$; this is exactly the weight mismatch the note warns about in Section 5, and it must be reconciled explicitly.

- **The absorption is linear in $Y$, not the quadratic Riccati form.** Take the Sobolev variable $u=\eta\chi^2F^{3/2}$, so $u^2=\eta^2a^2F^3$ and $\|u\|_2^2\le Y$ (using $a^2\le a$). Then
$$
\int\eta^2a^2F^4=\int u^2F\le\|u\|_4^2\|F\|_{L^2(\Omega_\eta)},\qquad
\|u\|_4^2\le A_\Omega^2\big(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\big).
$$
The $\nabla\eta$ part of $\nabla u$ vanishes on the collar ($\chi^2=0$ there); the $\nabla(\chi^2)$ part is $\le Cr^{-2}Y$; the interior part is $D_3$. Hence
$$
\int\eta^2a^2F^4\le C\beta(t)\big(D_3+r^{-2}Y\big),\qquad \beta=A_\Omega^2\|F\|_{L^2(\Omega_\eta)}.
$$
This is **linear in $Y$ with the small critical coefficient $\beta$**, not $C(r^{-2}+A_\Omega^4Y)Y$ with the $A_\Omega^4Y^2$ term of (6.2)–(6.3).

Consequence: the correct $q=3$ inequality is $Y'+cD_3\le Cr^{-2}Y+C\beta(D_3+r^{-2}Y)$; absorbing $C\beta D_3<\tfrac c2D_3$ gives the linear $Y'\le C'r^{-2}Y$. From the good starting time $s_0$ produced by (5.1), $Y(t)\le e^{C'\theta}Y(s_0)$ and the time-average $A_\Omega^4Y(s_0)\le2C\beta_*^3/t$ deliver (6.5) directly. So (6.5) is valid and is in fact reached more simply than the note's route; the Riccati differential inequality (6.3), the Gronwall-against-a-solution-dependent-coefficient step, and the associated non-blow-up worry are unnecessary. The written Section 6 should be replaced by the linear absorption above. (For completeness: the Riccati route the note wrote is also non-circular — the a priori integral bound (5.1) prevents blow-up on $[s_0,t]$ since $\log Z(t)-\log Z(s_0)\le C\theta+C\beta_*^3$ — so (6.5) would survive either way. But the linear derivation is the correct and cleaner one.)

The script's Section-6 block hard-codes the Riccati amplification $\exp(\dots+C\!\int Z)$ and fixed sample constants; it is scale/monomial bookkeeping only and gives no independent evidence on the reaction structure. It does not distinguish the linear from the quadratic form.

### 4. Triangular $Q$ estimate (Section 7): structurally clean, no hidden curvature-only source

I verified each term. The homogeneity of (7.1) in $E$ is the decisive structural fact — every term carries $E$, $\nabla E$, or a trace, so $E\equiv0$ is stationary and there is no curvature-only source. Testing by $\eta^2E$:
- the $a\Delta_LE$ principal term gives $-cX$ plus $Cr^{-2}Q$ (the $a\nabla\eta$ collar terms vanish by (1.1));
- the $(\nabla^2a)*E$ term integrates by parts to $\epsilon X+Cr^{-2}Q$, again with the $\nabla a\cdot\nabla\eta$ collar term killed by (1.1);
- $a(\operatorname{Rm}*E)$ and $a(E*E)$ both give $\le C\int\eta^2aF|E|^2$ (using $|\operatorname{Rm}|\le F$, $|E|\le CF$);
- the volume-form and metric-contraction variations are each $\le C\int\eta^2aF|E|^2$.

So (7.2) has no term beyond those listed. The absorption (7.3) with $w=\eta\chi E$ reproduces $\int aF|E|^2\le C\beta(t)(X+r^{-2}Q)$ exactly (again $\int\chi^2|\nabla E|^2=X$ because $\eta=1$ on $\operatorname{supp}\chi$), giving $Q'\le Cr^{-2}Q$ for small $\beta$. This is correct on one support, and it correctly replaces the additive $\varepsilon X$ inference that Step 20 §7 identified as insufficient at the topology scale.

### 5. What the single-support machinery does not reach

Summing (7.4) over disjoint selected supports controls $Q$ only on the union of good supports. The Ishida–LeBrun recalibration needs $\tfrac1{A_i}\int_{M_i}|\mathring{\operatorname{Ric}}_{h_i}|^2\to0$ over all of $M_i$. The selected good set $G_i=\{\mathcal M_{R_0}(|\operatorname{Rm}|^2)\le K_0\}$ has definite relative volume only if the total curvature energy is controlled relative to volume; on the varying laboratory $\int|\operatorname{Rm}|^2\sim A_i$, and whether $\operatorname{Vol}(G_i)/\operatorname{Vol}(M_i)$ stays bounded below along the sequence is exactly the unresolved density question the note flags in Sections 7–8. The un-selected region carries uncontrolled defect. This bridge from single-support control to $Q_{M_i}/A_i\to0$ is the real remaining structural object for the topological conclusion; the $\chi/\eta$ separation does not touch it.

### 6. Load-bearing inequalities that remain

1. Exact tensor proof of (3.1) — the $q=2$ closed curvature-power inequality with pinned constant $c$ and cutoff remainders (Step 20 ledger, not yet written out).
2. Exact tensor proof of (6.1) with an explicitly weighted $D_3=\int\eta^2a^2|\nabla F^{3/2}|^2$, and the corrected **linear** absorption $\int\eta^2a^2F^4\le C\beta(D_3+r^{-2}Y)$ replacing (6.2)–(6.3).
3. Exact tensor proof of (7.2) — the homogeneous defect energy with the $\Delta_L$, Hessian-cutoff, and volume-form terms fully expanded.
4. The volume-fraction statement connecting the summed single-support $Q$ control to $\tfrac1{A_i}\int_{M_i}|\mathring{\operatorname{Ric}}|^2\to0$.

Everything else in the note (localization to a single good center, collar freezing, volume cancellation, $q=2$ absorption, integrated cubic, time-average propagation mechanism, triangular $Q$ closure on one support) is mathematically sound as reconstructed here. The work stays inside the four-dimensional Ishida–LeBrun laboratory with Einstein sign $\lambda<0$; it does not address the $\lambda>0$ branch, arbitrary 4-manifold topology, $n\ge5$, or the full Yau-26 proposition, and the note states this correctly.