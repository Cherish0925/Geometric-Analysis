# TTCS Independent Branch Record

```json
{
  "step_id": 58,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step58_critical_to_subcritical_bridge.md",
    "Sessions/S0910A03/workspace/notes/step31_weighted_moser_interpolation_and_first_exit.md",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md"
  ]
}
```

## Task

Independently verify the curvature all-p and Moser part of Step 58, distinct from the Step 39 defect ladder. Starting from the exact weighted curvature inequality K_p'+dissipation <= C p^N(1+r^-2+S^2 Y)K_p and the positive-slab bound S^2Y<=C Gamma^3/t, check the time-slab recurrence, correct use of z_p, all powers of S,t,H(0),Gamma, and the conclusion ||a F_T(t)||_infty <= C Gamma/t. Determine whether the displayed recurrence M_{3p/2} <= C S (L M_p)^(3/2) is actually justified by the available sup K_p and integrated gradient terms, including any missing square roots or time factors. State a corrected recurrence and endpoint if needed.

## Output

## Verification Memo — curvature all‑p / Moser branch of Step 58

**Task result up front.** The recurrence (4.6) $\mathcal M_{p_{j+1},j+1}\le C\mathcal S(L_j\mathcal M_{p_j,j})^{3/2}$ **is** justified by the available $\sup K_p$ and the integrated gradient term, with no missing square root and no missing time factor. The normalized iteration (4.7), the two convergent exponent sums, and the endpoint $\|aF_T(t)\|_\infty\le C\Gamma/t$ are all internally consistent. I reconstructed each power below. There is one thing the displayed constant $L_j$ silently absorbs (a bounded $\Gamma^3/t$ reaction contribution) that changes the honest small‑$\Gamma$ rate but not the validity of the stated inequality. Details follow.

---

### 1. The energy step produces two outputs from one estimate

Starting from (3.4) written as $K_p'+cD_p\le\Lambda_pK_p$ with $D_p=pD_p^T+p(p-2)D_p^F$ and $\Lambda_p=Cp^N(1+r^{-2}+\mathcal S^2Y)$, a time cutoff $\zeta_j$ ($\zeta_j=1$ on $I_{j+1}$, supp in $I_j$, $|\zeta_j'|\le C4^j/t$) gives simultaneously
$$
\sup_{I_{j+1}}K_{p_j}\ \le\ L_j\mathcal M_{p_j,j},\qquad
\int_{I_{j+1}}\|\nabla z_{p_j}\|_2^2\,ds\ \le\ L_j\mathcal M_{p_j,j},
$$
the second using (4.2) $\|\nabla z_p\|_2^2\le Cp^2(D_p^T+D_p^F+r^{-2}K_p)$, with $r^{-2}\int K_p\le L_j\mathcal M$ absorbed because $L_j\ge Cr^{-2}$. Both the sup and the integrated gradient come from the **same** inequality, so using them together in one recurrence is legitimate. I checked (4.2): $\nabla z_p$ splits into the $\nabla\eta$ piece (zero since $a=0$ on supp $\nabla\eta$), the $a^{(p-3)/2}\nabla a$ piece giving $Cp^2r^{-2}K_p$ via $|\nabla a|^2/a\le Cr^{-2}$, and the $F^{p/2-1}\nabla F$ piece giving $Cp^2D_p^F$ with $|\nabla F|\le|\nabla T|$. Correct.

### 2. The recurrence, power by power

$$
\mathcal M_{3p/2,j+1}=\int_{I_{j+1}}K_{3p/2}\ \le\ \int_{I_{j+1}}K_p^{1/2}K_{2p}^{1/2}
\ \le\ (\sup_{I_{j+1}}K_p)^{1/2}\int_{I_{j+1}}K_{2p}^{1/2}.
$$
The interpolation $K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}$ is exact Cauchy–Schwarz (exponents: $a$‑side $(p-2)/2+(p-1)=3p/2-2$, $F$‑side $p/2+p=3p/2$). The **slice** Sobolev in the squared‑norm form $\|z_p\|_4^2\le\mathcal S(\|\nabla z_p\|_2^2+r^{-2}K_p)$ gives $K_{2p}^{1/2}=\|z_p\|_4^2\le\mathcal S(\|\nabla z_p\|_2^2+r^{-2}K_p)$, hence
$$
\int_{I_{j+1}}K_{2p}^{1/2}\ \le\ \mathcal S\Big(\int_{I_{j+1}}\|\nabla z_p\|_2^2+r^{-2}\!\int K_p\Big)\ \le\ \mathcal S\,L_j\mathcal M_{p_j,j}.
$$
Combining with $(\sup K_p)^{1/2}\le(L_j\mathcal M)^{1/2}$:
$$
\mathcal M_{3p/2,j+1}\ \le\ (L_j\mathcal M)^{1/2}\cdot\mathcal S L_j\mathcal M\ =\ \mathcal S(L_j\mathcal M)^{3/2}.
$$
This is exactly (4.6). **The single power of $\mathcal S$ is correct, and there is no missing square root.** The reason the single $\mathcal S$ survives — and the reason the whole route is clean — is that the interpolation extracts $K_{2p}^{1/2}$ (linear in the Sobolev bound), so only one time‑integral of the *linear* Sobolev inequality is taken; one never integrates $K_{2p}$ itself (which would force a second sup and a second $\mathcal S$). This is the same structural point argued in Step 31 §2–3 against the $\|Z_p\|_3^3$ route, and it is used correctly here.

Raising (4.6) to $1/p_{j+1}$ with $p_{j+1}=\tfrac32p_j$ (so $(3/2)/p_{j+1}=1/p_j$ and $1/p_{j+1}=2/(3p_j)$):
$$
m_{j+1}\le(C\mathcal S)^{2/(3p_j)}L_j^{1/p_j}m_j,\qquad m_j=\mathcal M_{p_j,j}^{1/p_j}.
$$
This reproduces (4.7) exactly.

### 3. Exponent sums and endpoint algebra

For $p_j=3(3/2)^j$: $\sum_j p_j^{-1}=\dfrac{1/p_0}{1-2/3}=3/p_0=1$, and $\sum_j\frac{\log p_j+j}{p_j}<\infty$ (geometric decay). Hence
- $\mathcal S$ total exponent $=\sum_j 2/(3p_j)=(2/3)\cdot1=2/3=2/p_0$;
- time‑cutoff exponent: each $L_j\propto t^{-1}$, giving $t^{-\sum p_j^{-1}}=t^{-1}$;
- polynomial‑in‑$p_j$ and $4^j$ factors converge into a finite constant.

Seed: $\mathcal M_{3,0}=\int_{t/2}^tK_3\,ds=\int_{t/2}^tY\,ds\le C\Gamma H(0)$ (since $K_3=\int\eta^2aF^3=Y$ and (2.7)). Thus
$$
\|aF_T(t)\|_\infty=\lim_j m_j\ \le\ C\,\mathcal S^{2/3}\,t^{-1}\,(\Gamma H(0))^{1/3},
$$
which is (4.10). The closing identity is exact: with $\Gamma=\mathcal S H(0)^{1/2}$,
$$
\mathcal S^{2/3}(\Gamma H(0))^{1/3}=\mathcal S^{2/3}\mathcal S^{1/3}H(0)^{1/6}H(0)^{1/3}=\mathcal S\,H(0)^{1/2}=\Gamma
$$
(powers $2/3+1/3=1$ on $\mathcal S$, $1/6+1/3=1/2$ on $H(0)$). So (4.11) $\|aF_T(t)\|_\infty\le C\Gamma/t$ is the correct consequence.

I also confirm the collapse cancellation as an independent check. With $\mathcal S\sim r^2V^{-1/2}$, $H(0)\sim K_0V$, $\Gamma\sim r^2\sqrt{K_0}$: $\mathcal S^{2/3}=r^{4/3}V^{-1/3}$, $(\Gamma H(0))^{1/3}=r^{2/3}K_0^{1/2}V^{1/3}$, product $=r^2K_0^{1/2}=\Gamma$, with $V$‑powers cancelling ($-1/3+1/3=0$). The endpoint is genuinely volume‑uniform.

### 4. The one substantive nuance: $\Gamma^3$ inside $L_j$

$L_j$ in (4.4) is written as $Cp_j^{N+2}4^j(t^{-1}+r^{-2})$, dropping the reaction term. But the reaction coefficient in (3.4) is $Cp^N(1+r^{-2}+\mathcal S^2Y)$, and on the slab $\mathcal S^2Y(s)\le C\Gamma^3/s\le 2C\Gamma^3/t$ for $s\in[t/2,t]$ (from (3.8)). So $L_j$ honestly contains a $\Gamma^3/t$ term. This is suppressed by treating $\Gamma\le\gamma_*$ as a bounded first‑exit constant. Two consequences to state plainly:

- Tracked honestly, $\prod_j(\Gamma^3)^{1/p_j}=\Gamma^{3\sum p_j^{-1}}=\Gamma^3$ accumulates into the product, so the honest small‑$\Gamma$ scaling of the endpoint is $\lesssim\Gamma^{3}\cdot\Gamma/t=\Gamma^4/t$, **not** linear $\Gamma/t$. Because $\Gamma\le\gamma_*\le1$ gives $\Gamma^4\le\Gamma$, the stated $C\Gamma/t$ remains a valid upper bound; it is simply not the sharp rate as $\Gamma\to0$, and the constant $C$ carries the normalization $\gamma_*\le1$. If the later ladder ever needs the *linear* dependence on $\Gamma$ (e.g. to iterate smallness), this distinction is real and should be carried, not absorbed.

- This also requires that (3.8) hold uniformly for every $s\in[t/2,t]$, not only at the single terminal time. It does — (3.8) is a per‑observation‑time statement (each $s$ has its own good slice $\tau\in[s/4,s/2]$) — but the note should make explicit that the slab‑uniform version $\mathcal S^2Y(s)\le 2C\Gamma^3/t$ is what feeds $L_j$.

### 5. Minor points that are correct but worth pinning

- **$\eta^2$ vs $\eta^4$.** (4.5) uses $K_{2p}=\|z_p\|_4^4$, but $K_{2p}$ carries $\eta^2$ while $\|z_p\|_4^4$ carries $\eta^4$. Because $a=\chi^2$ is supported inside $\{\eta=1\}$ and all integrands ($p\ge3$) carry a positive power of $a$, both weights equal $1$ on the support of the integrand, so the identity is genuine. This uses $p\ge3$ and would need care only if the ladder were started at $p=2$ (where $a^0$ appears); it starts at $p_0=3$, so it is safe.

- **Sobolev‑constant convention.** Step 58 uses $\mathcal S$ as the first‑power constant, $\|v\|_4^2\le\mathcal S(\|\nabla v\|_2^2+r^{-2}\|v\|_2^2)$ with $\mathcal S\sim r^2V^{-1/2}$, matching the Maheux–Saloff‑Coste derivation in Step 26 §1.3 (squaring $\|u\|_4\le CrV^{-1/4}\|\nabla u\|_2+CV^{-1/4}\|u\|_2$). This is consistent throughout Step 58 and is the value that makes the collapse cancellation in §3 exact. Note that Step 31 §6 at one point writes the *same* squared‑norm inequality with constant "$S^2=Cr^4/V$", i.e. the square of the correct constant; in collapse ($V\ll r^4$) that overstates the constant and would spoil the $V$‑cancellation if propagated. Step 58 does not inherit that; the two notes should be reconciled to the $r^2V^{-1/2}$ value.

### 6. What this branch establishes and what it does not

Given (i) the weighted curvature inequality (3.4), (ii) the positive‑slab bound $\mathcal S^2Y\le C\Gamma^3/t$, and (iii) the first‑exit smallness $\Gamma\le\gamma_*$, the curvature Moser endpoint $\|aF_T(t)\|_\infty\le C\Gamma/t$ on a positive dyadic slab is correctly derived, free of $Y(0)$ and volume‑uniform. The three inputs are themselves used as hypotheses here — in particular (3.4) rests on the Step 34–35 tensor calculation plus the shifted‑$T$ terms of Step 57, and (2.7)/(3.8) rest on the earlier absorption steps; this memo checks only the passage from those to the endpoint, which is sound. As the note itself records in §5, this does not yet close the common observation time (the metric/Sobolev first‑exit pair and the small‑$a$ collar continuation with the $\chi C_4*U$ / $\partial_tC_3\ni U_2$ staggered terms remain), and even the completed analytic mechanism concerns only the restricted four‑dimensional negative Ishida–LeBrun setting, not the all‑dimensional Problem 26 statement.

**Bottom line:** no correction to the recurrence or endpoint is required. The recurrence is genuinely of the form $\mathcal S(L_j\mathcal M)^{3/2}$ with the single $\mathcal S$ justified, all $\mathcal S$, $t$, $H(0)$, $\Gamma$ powers reconcile, and (4.11) holds. The only item to carry forward explicitly is that the linear $\Gamma$ in (4.11) is an upper bound obtained after absorbing a bounded $\Gamma^3$ from $L_j$; the honest rate is $\Gamma^4/t$, coincident with $\Gamma/t$ only because $\Gamma\le1$.