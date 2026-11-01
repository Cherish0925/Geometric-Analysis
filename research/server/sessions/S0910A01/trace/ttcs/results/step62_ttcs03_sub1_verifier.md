# TTCS Independent Branch Record

```json
{
  "step_id": 62,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step62_defect_moser_general_p_proof.md",
    "Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md"
  ]
}
```

## Task

Final verification of the defect Moser endpoint proof in step62_defect_moser_general_p_proof.md. The note now correctly identifies that the two-factor route fails for the Moser ladder (gamma_t <= c/p) and uses the three-factor route instead. Check: (1) Proposition 3.2: is the p-dependence of the two-factor absorption correctly derived? The reaction Cp * P_p <= Cp^3 gamma_t Q_p against c_2 p^2 Q_p requires gamma_t <= c/p. (2) Proposition 4.1: the three-factor decomposition eta^2 a^{p-1} F s^{p/2} = (aF^3)^{1/3}(eta^2 a^{p-2}s^{p/2})^{1/3} z_p^{4/3}. Verify the weight identity: LHS has a^{p-1}, RHS has a^{(p-2)/3} * a^{2(p-1)/3} = a^{(p-2+2p-2)/3} = a^{(3p-4)/3}. Is (3p-4)/3 = p-1? That requires 3p-4 = 3p-3, i.e., -4=-3, which is FALSE. Check whether the eta weights correct this: the Codex report says 'eta=1 on the support of a', so the eta factors may not help. Is the three-factor identity correct as stated? (3) Remark 4.2: the absorption epsilon p Q_p into c_2 p^2 Q_p works for p >= 2 without smallness. Verify. (4) The overall conclusion: is the defect endpoint delta(r^2/t)^{1/3} correctly established via the three-factor route?

## Output

# Verification memo: Step 62 defect Moser endpoint

Scope of review: the four items posed, checked line by line against `step62_defect_moser_general_p_proof.md` (tags (2.3) etc.), `step34_integrated_potential_q3_and_defect.md` (tagged [S34]), and `weighted_moser_and_continuation_repair.md` (tagged [CR]). Bottom line: items (1) and (3) are correct as written; in item (2) the identity is exactly correct and the suspected mismatch is an arithmetic slip in the check itself; in item (4) the endpoint conclusion is correct, but the note's own seed display (5.6)–(5.7) contains one unjustified inequality in the collapse regime, and the correct justification already exists in-session in the time-integrated formulation [CR] (5.8)–(5.12).

## 1. Proposition 3.2 — the p³-versus-p² mismatch is derived correctly

The chain is: (i) for $z_p=\eta\chi^{p-1}s^{p/4}$ (1.4), $\nabla z_p$ has three terms; the $d\eta$ term vanishes since $\operatorname{supp}d\eta\subset\{a=0\}$ and $p\ge6$; the $\chi$-derivative term $(p-1)\eta\chi^{p-2}(\nabla\chi)s^{p/4}$ contributes $Cp^2r^{-2}J_p$ via $|\nabla\chi|\le C/r$; the $s$-derivative term $(p/4)\eta\chi^{p-1}s^{p/4-1}\nabla s$ contributes exactly $(p^2/16)Q_p$. Hence $\|\nabla z_p\|_2^2\le Cp^2(Q_p+r^{-2}J_p)$, and $\|z_p\|_2^2\le J_p$ since $a\le1$. (ii) $P_p=\int\eta^2a^{p-1}Fs^{p/2}=\int Fz_p^2\le (K_2^\eta)^{1/2}\|z_p\|_4^2\le C\gamma_t p^2(Q_p+r^{-2}J_p)$ by (1.5)–(1.6). (iii) The reaction enters (2.3) as $Cp\cdot P_p$ because the chain-rule multiplier $p/2$ hits $\Sigma_s\le CaFs$; so $Cp\cdot P_p\le Cp^3\gamma_tQ_p+\cdots$. (iv) The favorable radial dissipation is $c_2p^2Q_p$ from the coefficient $p(p-2)/4$ in (2.4). Absorption requires $Cp^3\gamma_t\le(c_2/2)p^2$, i.e. $\gamma_t\le c_2/(2Cp)$ — precisely (3.3). Since $\gamma_t=\mathcal S(t)(K_2^\eta(t))^{1/2}$ is a fixed structural size ($\gamma\le Cr^2\sqrt{K_0}$, [S34] (1.4)–(1.5)) and does not decay along $p_k=6(3/2)^k$, the condition is violated for all large $k$; no $\varepsilon$-freedom remains because the reaction carries no $\varepsilon$. The seed $p=6$ is exactly the borderline case where the condition reduces to the standing smallness $\gamma_t\le c$ (Proposition 3.1 = [S34] (5.12)). Remark 3.3's accounting (multiplier $p/2$ times gradient $p^2$ gives $p^3$ against $p^2$ dissipation) is the right mechanism statement.

## 2. Proposition 4.1 — the identity (4.1) is exactly correct; the flagged discrepancy drops the first factor's $a^{1/3}$

Full exponent bookkeeping for $\eta^2a^{p-1}Fs^{p/2}=(aF^3)^{1/3}\,(\eta^2a^{p-2}s^{p/2})^{1/3}\,z_p^{4/3}$ with $z_p=\eta a^{(p-1)/2}s^{p/4}$:

- $a$: $\tfrac13+\tfrac{p-2}{3}+\tfrac{2(p-1)}{3}=\tfrac{1+p-2+2p-2}{3}=\tfrac{3p-3}{3}=p-1$ ✓
- $s$: $0+\tfrac{p}{6}+\tfrac{p}{3}=\tfrac{p}{2}$ ✓; $\eta$: $0+\tfrac23+\tfrac43=2$ ✓; $F$: $1$ ✓.

The computation in the verification prompt, $a^{(p-2)/3}\cdot a^{2(p-1)/3}=a^{(3p-4)/3}\ne a^{p-1}$, omits the $a^{1/3}$ supplied by the first factor $(aF^3)^{1/3}$; adding it gives $(3p-4)/3+1/3=p-1$ exactly. The identity is pointwise, holds globally (both sides carry $\eta^2$), and does not lean on $\eta=1$ on $\operatorname{supp}a$. It agrees with [S34] (2.12) (the curvature version $a^{p-1}F^{p+1}$) and [CR] (5.3), and [CR] §9 records that `verify_weighted_moser_coupling.py` machine-checks the three-factor absorption weights in-session. Hölder $(3,3,3)$ on it yields (4.4), $P_p\le Y^{1/3}J_p^{1/3}\|z_p\|_4^{4/3}$, as stated.

## 3. Remark 4.2 — p-independent absorption verified

Young with exponents $(3,3/2)$ applied to (4.4) with $\|z_p\|_4^{4/3}\le Cp^{4/3}\mathcal S^{2/3}(Q_p+r^{-2}J_p)^{2/3}$ gives $P_p\le\varepsilon(Q_p+r^{-2}J_p)+C_\varepsilon p^4\mathcal S^2YJ_p$; multiplying by the chain-rule $p$ gives (4.6). The absorption $\varepsilon pQ_p\le(c_2/2)p^2Q_p$ is $\varepsilon\le c_2p/2$, which holds for every $p\ge2$ with the universal choice $\varepsilon=c_2$ — no smallness on $\gamma$ or $Y$ anywhere. The price, $C_\varepsilon p^5\mathcal S^2YJ_p$, needs no absorption at all; it enters the Gronwall coefficient, and its slab integral is uniformly bounded: from [S34] (4.4), $\sup_{s\ge\tau}\mathcal S(s)^2Y(s)\le C\gamma^3/\tau$, so on $[\tau_k,t]$ with $\tau_k\ge t/2$, $\int\mathcal S^2Y\,ds\le C\gamma^3$ — equations (4.7)–(4.8). This is exactly the $p$-independence mechanism: pointwise smallness $\gamma_t\le c/p$ is traded for an integrable coefficient. No circularity: $Y$ is produced by the curvature branch from the $q=2$ energy and Sobolev interpolation alone ([S34] §§3–4), with no defect-Moser output. Also verified en route: (2.4) by expanding $\Delta(s^{p/2})$; $c_2=1/6$ valid for all $p\ge6$; Kato $Q_p\le4D_p^E$; the time-slice weight identity $(p-2)/2+(p-1)=3p/2-2$ ([CR] (5.7)); $\sum(2/3)^j=2$, $\sum j(2/3)^j=6$; $J_p^{1/p}\to\|aE\|_\infty$ on $\{a>0\}$.

## 4. The endpoint (5.8): conclusion correct; the note's seed display (5.6)–(5.7) has one unjustified step in the collapse regime, repaired verbatim by the in-session time-integrated recurrence

**Recurrence and product are correct.** The time-cutoff testing of (4.3), the time-slice recycling $\int J_{p_k}\le A_{k-1}^{1/2}B_{k-1}\le\Lambda_{k-1}^{3/2}$, and $B_k\le C\mathcal Sp_k^N4^kt^{-1}\int J_{p_k}$ give (5.3) with $C_k=C\mathcal Sp_k^N4^kt^{-1}$ (one $\mathcal S$ from the Sobolev step, $4^k/t$ from $|\zeta_k'|$ and the slab coefficient $\gamma^3/t+r^{-2}\le C4^k/t$ for $t\le\theta r^2$). The product (5.5) converges with $\mathcal S$-exponent $\sum(2/3)^j/p_0=1/3$ and $t$-exponent $-1/3$, yielding (5.4): $\|aE(t)\|_\infty\le C\Lambda_0^{1/6}\mathcal S^{1/3}t^{-1/3}$.

**The seed display (5.7) loses a factor $\mathcal S^{1/6}$ when $\mathcal S\gg1$.** From (5.6), $A_0\le CJ_6(0)$ and $B_0\le C\mathcal S J_6(0)$ (Sobolev on $z_6$ plus $\int Q_6\le CJ_6(0)$ from integrating [S34] (5.14)), so $\Lambda_0\le C(1+\mathcal S)J_6(0)$. The middle inequality of (5.7) then reads $[(1+\mathcal S)\delta^6V]^{1/6}\mathcal S^{1/3}\le C\delta V^{1/6}\mathcal S^{1/3}$, i.e. it uses $(1+\mathcal S)^{1/6}\le C$. Since $\mathcal S\simeq r^2V^{-1/2}\ge c>0$ and $\mathcal S\to\infty$ as $V/r^4\to0$, the bound the preceding line actually justifies for $\mathcal S\ge1$ is $(1+\mathcal S)^{1/6}\mathcal S^{1/3}\le2^{1/6}\mathcal S^{1/2}$, giving $\|aE(t)\|_\infty\le C\delta V^{1/6}\mathcal S^{1/2}t^{-1/3}=C\delta rV^{-1/12}t^{-1/3}$ — volume does not cancel. So (5.7) as displayed is valid only when $\mathcal S\lesssim1$ (non-collapse at the support scale). This matters materially: the endpoint feeds the metric drift (5.9) that closes the first-exit bootstrap, and a bound proportional to $V^{-1/12}$ is not uniform as the family collapses — the very role the volume-cancellation theme plays in [S34] (1.5).

**The repair is already derived in-session.** Run the recurrence on the time-integrated quantities $X_k=\int_{\tau_k}^tJ_{p_k}(s)\,ds$, exactly as in [CR] (5.8) and [S34] (6.1): $X_{k+1}\le Cp_k^N\mathcal S(L_kX_k)^{3/2}$ with $L_k=Cp_k^N4^k(t^{-1}+r^{-2})$. The seed $X_0=\int_{t/2}^tJ_6\le(t/2)e^{C(1+r^{-2})t}J_6(0)\le Ct\,\delta^6V$ carries **no** Sobolev factor; each recurrence constant carries exactly one $\mathcal S$, and the product gives $\mathcal S^{2/p_0}=\mathcal S^{1/3}$ ([CR] (5.9)–(5.10)). Hence [CR] (5.12):
$$
\|aE(t)\|_\infty\le C\mathcal S^{1/3}t^{-1/2}\bigl(t\delta^6V\bigr)^{1/6}
=C\delta\,V^{1/6}\bigl(r^2V^{-1/2}\bigr)^{1/3}t^{-1/3}
=C\delta\Bigl(\frac{r^2}{t}\Bigr)^{1/3},
$$
with $V^{1/6}V^{-1/6}$ cancelling exactly for all $\mathcal S$. The drift (5.9) follows: $\int_0^T\|aE\|_\infty dt\le C\delta r^{2/3}\cdot\tfrac32T^{2/3}=C\delta\theta^{2/3}r^2$. The note's Proposition 5.1 machinery (time-cutoff testing, time-slice identity) is precisely what the $X$-recurrence consumes; only the seed object changes ($X_0$ in place of $\Lambda_0$), so the repair is local to §5.3. The alternative justification — that the Step 55 $(\Gamma,V)$ bootstrap forces $\mathcal S\lesssim1$ on the macro-supports — would validate (5.7) as written, but nothing in the supplied files establishes that, and in the IL collapse laboratory the time-integrated formulation is the regime-independent derivation.

**Conditionality inventory** (unchanged by the repair): the defect equation is derived at index level ([CR] (2.7)–(2.8)); the general-$p$ dissipation structure and Kato-first cross-term absorption (2.3)–(2.4) check out (the Young placement gives $p^3$ or $p^4$ on the $r^{-2}J_p$ remainder depending on Kato placement, immaterial under $p^N$); Hessian-cutoff handling follows [S34] (5.8)–(5.9) ($B$ quadratic in $E$, $|\nabla B|\le Cs^{1/2}|\nabla E|$); $J_6$ persistence is [S34] (5.10)–(5.15). The $Y$-input (4.7) inherits the fixed-$p$ curvature premise [S34] (2.14), whose index-level variation ([S34] (2.3), (2.10)) is listed as open in [S34] §7 item 1 — so the defect endpoint currently rests on that curvature premise through $Y$, plus the Step 55 uniformity $\mathcal S(t)\le2\mathcal S(0)$, $K_2^\eta(t)\le CK_2^\eta(0)$, and the standard Kato regularization for $p_k=6(3/2)^k\notin2\mathbb Z$ (note §8).

**Summary per item:** (1) correct; (2) correct — the prompt's exponent sum omitted the first factor's $a^{1/3}$; (3) correct; (4) the three-factor mechanism, recurrence, product convergence, and final scaling are correct, and the endpoint $\delta(r^2/t)^{1/3}$ stands — but the justification of the volume cancellation must come from the time-integrated seed $X_0\le Ct\delta^6V$ of [CR] (5.8)–(5.12) / [S34] (6.1), not from the note's $\Lambda_0$-display (5.6)–(5.7), whose middle inequality drops $(1+\mathcal S)^{1/6}$ and is justified only for $\mathcal S\lesssim1$.