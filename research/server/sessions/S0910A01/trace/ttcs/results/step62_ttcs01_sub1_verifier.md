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
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md"
  ]
}
```

## Task

Verify the general-p two-factor defect inequality and nested Moser recurrence for the restricted 4D cutoff flow. The claimed results are in the attached note step62_defect_moser_general_p_proof.md. Check adversarially: (1) Proposition 3.2: the general-p defect energy inequality J_p' + c'p^2 D_p^E <= Cp^N(1+r^{-2})J_p + Cp P_p. Is the chain rule dissipation computation correct for s^alpha with alpha=p/2? Is the integration by parts of the a^{p-2} weight correct, including the favorable dissipation and the error Cp^2 r^{-2} J_p? (2) Proposition 3.3: the two-factor absorption P_p = int F w_p^2 <= C gamma_t (D_p^E + r^{-2} J_p). Is the gradient computation for w_p = eta a^{(p-1)/2} s^{p/4} correct? The nabla s term gives a^{p-1} s^{p/2-2} |nabla s|^2 <= 4 D_p^E — verify this uses |nabla s|^2 <= 4s|nabla E|^2 correctly. (3) Proposition 4.1: the recurrence Lambda_k <= C_k Lambda_{k-1}^{3/2} with C_k = C S p_k^N 4^k t^{-1}. Is the time-cutoff argument correct? (4) Proposition 4.2: the endpoint ||aE||_inf^2 <= C Lambda_0^{1/p_0} S^{2/p_0} t^{-2/p_0}. Is the product convergence correct? The sums sum_j (2/3)^j = 2 and sum_j (2/3)^j j = 6 — verify. (5) The volume cancellation: S ~ r^2 V^{-1/2}, J_6(0) <= C delta^6 V, giving ||aE||_inf^2 <= C delta r^{2/3} t^{-1/3}, hence ||aE||_inf <= C delta^{1/2} (r^2/t)^{1/6}. Is this correct, and does it contradict or correct the Step 34 claim ||aE||_inf <= C delta (r^2/t)^{1/3}?

## Output

# Verification memo: Step 62 general-$p$ defect inequality and nested Moser recurrence

**Scope of check:** the five items posed, against `step62_defect_moser_general_p_proof.md`, cross-read with Step 34 (`step34_integrated_potential_q3_and_defect.md`) and the A03 report (`weighted_moser_and_continuation_repair.md`). All computations below were redone independently.

**Headline:** The analytic skeleton (two-factor absorption, mixed recurrence, product convergence, volume cancellation) is sound and repairable where defective, but there are four genuine defects: (i) Lemma 3.1's "favorable weight dissipation" does not exist as written and its error term is justified by a wrong-direction inequality; (ii) the dissipation prefactor $c'p^2$ on $D_p^E$ in (3.11)/(3.24) is not available — $p^2$ attaches only to the *radial* dissipation, and the closure as written forces $p$-dependent smallness $\gamma\lesssim p^{-2}$, which cannot hold over the ladder $p_k\to\infty$; (iii) Proposition 4.2's (4.28) drops a square, mislabeling $\|aE\|_\infty$ as $\|aE\|_\infty^2$; (iv) the resulting "corrected exponent" $\delta^{1/2}(r^2/t)^{1/6}$ (Remark 4.3) is spurious — the correct endpoint is Step 34's $\delta(r^2/t)^{1/3}$, which the note's own (4.20) already states.

---

## 1. Chain rule and the $a^{p-2}$ weight IBP (Proposition 3.2 / Lemma 3.1)

**(3.1) is correct.** For $\alpha=p/2$, $(\partial_t-a\Delta)s^\alpha=\alpha s^{\alpha-1}(\partial_t-a\Delta)s-\alpha(\alpha-1)a s^{\alpha-2}|\nabla s|^2$ — standard. With (2.3), the principal term tested against $\eta^2a^{p-2}$ gives exactly $2\alpha D_p^E=pD_p^E$ ✓ (3.3).

**(3.4) is not produced by the IBP and is algebraically garbled.** Since the test function $\eta^2a^{p-2}$ contains no $s$, integration by parts gives only
$$
-\int\eta^2a^{p-1}\Delta s^\alpha=(p-1)\alpha\int\eta^2a^{p-2}s^{\alpha-1}\nabla a\cdot\nabla s,
$$
a signed cross term. No $|\nabla s^\alpha|^2$ term arises. The displayed expression $\int\eta^2a^{p-1}|\nabla s^\alpha|^2\cdot\frac{1}{\alpha^2s^{\alpha-1}}\cdot\alpha^2s^{\alpha-1}$ collapses to $\int\eta^2a^{p-1}|\nabla s^\alpha|^2$ and the inequality asserted around it is false as written. The genuine favorable term is the **chain-rule term** $-\alpha(\alpha-1)as^{\alpha-2}|\nabla s|^2$ in (3.1), which the note discards in (3.2) — equivalently, test the $s$-equation against $\eta^2a^{p-2}\alpha s^{\alpha-1}$ and the IBP on the $s^{\alpha-1}$ factor produces it.

**(3.8)–(3.10) contain a wrong-direction inequality.** The note's direct Young split of the cross term produces the remainder $Cp^4\int\eta^2a^{p-2}|\nabla\chi|^2s^{\alpha-1}$, and (3.10) then asserts $\int\eta^2a^{p-2}s^{p/2-1}\le CJ_p$ "for $s\le1$". This goes the wrong way: for $0<s\le1$ and $p\ge6$, $s^{p/2-1}\ge s^{p/2}$ (e.g. $s=\delta^2=10^{-4}$, $p=6$: $s^2=10^{-8}\gg s^3=10^{-12}$). Moreover the $\varepsilon$-piece of (3.8), $\varepsilon\int a^{p-1}s^{\alpha-1}|\nabla s|^2$, matches *no* available favorable term: $D_p^E$ carries $s^{\alpha-1}|\nabla E|^2$, the chain-rule term carries $s^{\alpha-2}|\nabla s|^2$.

**Repair (clean, no pointwise $s$-bound needed).** Apply Kato $|\nabla s|\le2\sqrt s\,|\nabla E|$ to the cross term *before* Young:
$$
(p-1)\alpha\,a^{p-2}s^{\alpha-1}|\nabla a||\nabla s|
\le4(p-1)\alpha\,a^{p-3/2}s^{\alpha-1/2}|\nabla\chi||\nabla E|
\le\varepsilon\,a^{p-1}s^{\alpha-1}|\nabla E|^2+C_\varepsilon p^4r^{-2}a^{p-2}s^{p/2},
$$
using $|\nabla a|^2=4a|\nabla\chi|^2\le4ar^{-2}$ ✓ (identity verified). The $\varepsilon$-piece is now exactly $D_p^E$; the error is $Cp^4r^{-2}J_p$ (the note's $Cp^2$ undercounts the $p$-power, immaterial inside $p^N$).

**The dissipation prefactor.** The correct statement is
$$
J_p'+pD_p^E+\tfrac{p(p-2)}{4}\tilde D_p^s\le Cp^4(1+r^{-2})J_p+CpP_p,\qquad
\tilde D_p^s:=\int\eta^2a^{p-1}s^{p/2-2}|\nabla s|^2 .
$$
The coefficient on $D_p^E$ is exactly $p$ (from $2\alpha$); the $p^2$-sized coefficient $\alpha(\alpha-1)=p(p-2)/4$ attaches only to the **radial** dissipation $\tilde D_p^s$. Since $\tilde D_p^s\le4D_p^E$ (Kato) but not conversely, the boxed (3.11) with $c'p^2D_p^E$ is not available. All other terms in Proposition 3.2 verify: first-derivative cutoff terms $\le\varepsilon D_p^E+Cp^2r^{-2}J_p$ ✓ (3.13); the signed Hessian term (2.6) — tensor $\tau E^{ij}+g^{ij}s-2(E^2)^{ij}$ assembled from $(\Delta a)E$, $\tau a_{ij}$, and $-a_i{}^kE_{kj}-a_j{}^kE_{ki}$ in (2.2), consistent with Step 34's (5.8) up to the factor 2 from $\partial_ts=2\langle E,\partial_tE\rangle$ — after signed IBP gives $\varepsilon(D_p^E+\tilde D_p^s)+Cp^2r^{-2}J_p$ ✓ (I recomputed all three IBP descendant types: the $a^{p-2}$-derivative piece gives $a^{p-3}|\nabla a|^2=4a^{p-2}|\nabla\chi|^2$, nonsingular ✓; the $s^{\alpha-1}$-derivative piece splits as $[a^{(p-1)/2}s^{(\alpha-2)/2}|\nabla s|]\cdot[a^{p/2-1}s^{p/4}|\nabla\chi|]$, absorbing into $\tilde D_p^s$ ✓; the $\nabla Q$ piece into $D_p^E$ ✓). Reaction: $\alpha s^{\alpha-1}\cdot aFs$ tests to $CpP_p$ ✓, and $|E|\le CF$ absorbs the metric-variation cubic $as^{3/2}\le aFs$ ✓.

## 2. Two-factor absorption (Proposition 3.3)

The gradient computation is **correct**: $\nabla a$-piece $=\frac{(p-1)^2}{4}a^{p-3}|\nabla a|^2s^{p/2}=(p-1)^2a^{p-2}|\nabla\chi|^2s^{p/2}\le Cp^2r^{-2}J_p$ ✓ (3.20); $\nabla s$-piece $=\frac{p^2}{16}a^{p-1}s^{p/2-2}|\nabla s|^2\le\frac{p^2}{4}a^{p-1}s^{p/2-1}|\nabla E|^2$, integrating to $\frac{p^2}{4}D_p^E$ ✓ — (3.21) uses $|\nabla s|^2=|2\langle E,\nabla E\rangle|^2\le4s|\nabla E|^2$ correctly ✓. Hence $\|\nabla w_p\|_2^2\le Cp^2(D_p^E+r^{-2}J_p)$ ✓ (3.22), $\|w_p\|_2^2\le J_p$ ($a\le1$) ✓, support argument $\operatorname{supp}w_p\subset\{\eta=1\}$ ✓, and Hölder $(2,4,4)$ + Sobolev give
$$
P_p=\int Fw_p^2\le(K_2^\eta)^{1/2}\mathcal S\,Cp^2\bigl(D_p^E+r^{-2}J_p\bigr)\quad(3.23)\ ✓.
$$
Two problems: the boxed (3.16) **drops the $p^2$** (contradicting (3.22)–(3.23)); and the closure in Corollary 3.4 absorbs $Cp^2\gamma_tD_p^E$ against a $c'p^2D_p^E$ that does not exist (§1). Taken with the true dissipation $pD_p^E$, absorption would need $\gamma_t\lesssim 1/p$ — fatal on the ladder $p_k=6(3/2)^k\to\infty$.

**Repair ($p$-independent).** Do *not* Kato the $\nabla s$-piece away: it equals $\frac{p^2}{16}\tilde D_p^s}$, and the chain rule supplies $\frac{p(p-2)}{4}\tilde D_p^s$. Absorption condition:
$$
C\gamma_t\cdot\tfrac{p^2}{16}\le\tfrac12\cdot\tfrac{p(p-2)}{4}
\iff \gamma_t\le c_0\ \text{independent of }p
$$
(worst case $p=6$: $\gamma_t\le 4/(3C)$). The $\nabla a$-piece $Cp^2\gamma_tr^{-2}J_p$ joins the Gronwall side. Repaired Corollary 3.4:
$$
J_p'+c_1pD_p^E+c_2p^2\tilde D_p^s\le Cp^4(1+r^{-2})J_p,\qquad
J_p(t)\le e^{Cp^4(1+r^{-2})t}J_p(0),
$$
valid for all real $p\ge6$ under the single $p$-independent smallness $\sup_t\gamma_t\le c_0$ — which the first-exit premises supply ($\gamma_t\le2\mathcal S(0)(CK_2^\eta(0))^{1/2}\le Cr^2\sqrt{K_0}$, Step 34 (1.5)). The bridge for the recurrence becomes $\|z_p\|_4^2\le\mathcal S\bigl(\frac{p^2}{8}\tilde D_p^s+Cp^2r^{-2}J_p\bigr)$, pairing exactly with the $c_2p^2$ dissipation. Remark 3.5 (no $Y$, no three-factor decomposition; $P_p$ linear in $F$ absorbed by the $L^2$ seed alone) is structurally correct ✓ — the homogeneity of (2.1)–(2.2) in $E$ (no curvature-only source, since $D\operatorname{Ric}[-2aE]$ is linear in its argument) is what makes this work ✓.

## 3. The recurrence (Proposition 4.1)

Verified in structure. The time-slice identity (4.1) is exact Cauchy–Schwarz: $\eta^2a^{3p/2-2}s^{3p/4}=[\eta a^{(p-2)/2}s^{p/4}][\eta a^{p-1}s^{p/2}]$ with weight split $\frac{p-2}{2}+(p-1)=\frac{3p}{2}-2$ ✓ (4.2). The time-cutoff device is the right one — the note itself correctly rejects its own good-slice detour (4.7)–(4.10) (mean value gives a good slice $\sigma_k\ne\tau_k$) before switching to $\zeta_k$. Testing with $\eta^2a^{p_k-2}\zeta_k$ and integrating from $\zeta_k(\tau_{k-1})=0$:
$$
\sup_{[\tau_k,t]}J_{p_k}+\int_{\tau_k}^t\mathrm{diss}\le\frac{C2^k}{t}\int_{\tau_{k-1}}^tH_{p_k}+Cp_k^N(1+r^{-2})\int_{\tau_{k-1}}^tH_{p_k},
$$
and every $\int H_{p_k}$ is recycled through (4.1) as $A_{k-1}^{1/2}B_{k-1}$ ✓ (4.12)–(4.13). This recycling is also what avoids a circularity the note does not mention: bounding $\int_{\tau_k}^tJ_{p_k}$ by $tA_k$ instead would put $\mathcal Sp_k^2\theta\cdot A_k$ on the right, requiring $\theta\lesssim p_k^{-2}$; the (4.1)-route keeps everything at level $k-1$ ✓. The step $A_{k-1}^{1/2}B_{k-1}\le\Lambda_{k-1}^{3/2}$ is universal (no smallness needed, contra the note's "on small energies" framing). With $t\le\theta r^2$, $r^{-2}\le\theta t^{-1}$, so $C_k=C\mathcal Sp_k^N4^kt^{-1}$ is an admissible constant (for $N\ge2$ the base $4$ becomes $2(3/2)^N$; $\log C_j$ stays affine in $j$, convergence unaffected). The $p$-count in (4.3) shifts by one power under the §1 repair ($\int D_{p_k}^E\le Cp_k^{-1}[\ldots]$, $\int\tilde D_{p_k}^s\le Cp_k^{-2}[\ldots]$); the bridge uses $\tilde D^s$, so (4.5) survives unchanged in form.

## 4. Product convergence (Proposition 4.2)

The iteration algebra is correct: $\Lambda_k\le\Lambda_0^{(3/2)^k}\prod_{j=1}^kC_j^{(3/2)^{k-j}}$ ✓ (4.22); dividing by $p_k=p_0(3/2)^k$ gives exponents $1/p_0$ on $\Lambda_0$ and $(2/3)^j/p_0$ on $C_j$ ✓ (4.23). The sums verify: $\sum_{j\ge1}(2/3)^j=\frac{2/3}{1/3}=2$ ✓ and $\sum_{j\ge1}j(2/3)^j=\frac{2/3}{(1/3)^2}=6$ ✓, so $\prod C_j^{(2/3)^j/p_0}=C'\mathcal S^{2/p_0}t^{-2/p_0}$ ✓ (4.26)–(4.27).

**The dropped square is in (4.28).** Since $H_p=\int\eta^2a^{-2}(a|E|)^p$, one has $H_p^{1/p}\to\|aE\|_\infty$ on $\{\eta=1\}$ — the *first* power (upper bound via $H_p\le M^{p-2}\int\eta^2|E|^2$; lower bound via the set $\{a|E|>M-\varepsilon\}$, on which $a$ is bounded below). Therefore (4.23) controls $\|aE(t)\|_\infty$, not $\|aE(t)\|_\infty^2$:
$$
\boxed{\ \|aE(t)\|_\infty\le C\,\Lambda_0^{1/p_0}\,\mathcal S^{2/p_0}\,t^{-2/p_0}\ }
$$
— the note's (4.28) writes the left side squared while keeping the right side unsquared. Squaring the correct version gives $\|aE\|_\infty^2\le C\Lambda_0^{2/p_0}\mathcal S^{4/p_0}t^{-4/p_0}$, which matches A03's independently derived (5.10) after substituting $\int_{t/2}^tH_{p_0}\le tA_0$ ($t^{-6/p_0}\cdot t^{2/p_0}=t^{-4/p_0}$ ✓).

## 5. Volume cancellation and the endpoint: Step 34 is confirmed, not corrected

The algebra in (4.33) is internally consistent given (4.28): $J_6(0)^{1/6}\le C\delta V^{1/6}$ cancels $\mathcal S^{1/3}\simeq r^{2/3}V^{-1/6}$ ✓, $(1+\mathcal S)^{1/6}\le C$ in the noncollapsed regime ✓. But because (4.28) mislabels the left side, the conclusion (4.34)–(4.35) and Remark 4.3 are artifacts. Substituting correctly:
$$
\|aE(t)\|_\infty\le C\bigl[(1+\mathcal S)J_6(0)\bigr]^{1/6}\mathcal S^{1/3}t^{-1/3}
\le C\delta r^{2/3}t^{-1/3}=C\delta\Bigl(\frac{r^2}{t}\Bigr)^{1/3}.
$$
This is exactly Step 34's (6.3) and A03's (5.12) (the latter script-checked by `verify_weighted_moser_coupling.py`). Three independent routes agree; Step 62's Remark 4.3 is the outlier, and it contradicts the note's own Proposition 4.2 statement (4.20) — $\|aE(t)\|_\infty\le C\mathcal S^{1/3}t^{-1/2}(J_6(0)t)^{1/6}=C\delta(r^2/t)^{1/3}$ — which is correct as written. The drift consequently remains Step 34's (6.4):
$$
\int_0^T\|aE\|_\infty dt\le C\delta r^{2/3}T^{2/3}=C\delta\theta^{2/3}r^2,
$$
with smallness scale $\delta\le V_*/(C\theta^{2/3}r^2)$. The note's "more restrictive" scale $\delta\le(V_*/(C\theta^{5/6}r^2))^2$ in (4.37) and its propagation into the $(\Gamma,V)$ bootstrap (§7, §8 item 1) should be reverted; for small $\delta$ that scale is far stronger than needed and would weaken the final theorem's $\delta$-range.

## 6. Secondary items

- **Even $p$ vs the ladder:** §1 restricts to even $p$, but $p_k=6(3/2)^k$ is non-integer from $k=2$ ($9,\ 27/2,\ \ldots$). Harmless — the lowest $s$-power appearing is $s^{p/2-2}$ with exponent $\ge1$, so a one-line Kato regularization $s_\varepsilon=s+\varepsilon$ (as A03 states explicitly) closes it; the note should say so.
- **Seed conventions are mixed:** (4.19) writes $\Lambda_0\le C\mathcal SJ_6(0)\,t$ (the integrated-seed convention of A03's (5.10)) while (4.31) correctly gives $\Lambda_0=A_0+B_0\le C(1+\mathcal S)J_6(0)$ (sup-based, no $t$). Both feed the same endpoint; the note should pick one.
- §5's resolution of the seed question ($\Lambda_0=A_0+B_0$, energy-based, controlled by $J_6(0)$) is correct in substance; its remark about "the squared norm" inherits the (4.28) confusion.
- The status table (§6) rows stand after the repairs above, but displayed equations (3.4), (3.8)–(3.10), (3.11), (3.16), (3.24), (4.19), (4.28), (4.34)–(4.37) and Remark 4.3 need the corrections itemized here.

## 7. Net assessment

The two structural items this note set out to supply do go through: the general-$p$ two-factor defect inequality in the repaired form $J_p'+c_1pD_p^E+c_2p^2\tilde D_p^s\le Cp^4(1+r^{-2})J_p$ with $p$-independent smallness $\gamma_t\le c_0$ (the chain-rule radial dissipation is load-bearing — it is the only $p^2$-sized favorable term and it matches the $\nabla s$-piece of $\|\nabla w_p\|^2$ exactly), and the nested Moser recurrence with product constant $C'\mathcal S^{2/p_0}t^{-2/p_0}$. The endpoint is $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$ — unchanged from Step 34 and A03 — so the defect-Moser input to the first-exit closure is the original drift $\delta\theta^{2/3}r^2$, and no revised $\delta$-scale needs to be propagated into the bootstrap or downstream modules.