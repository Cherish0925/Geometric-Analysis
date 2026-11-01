# TTCS Independent Branch Record

```json
{
  "step_id": 54,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step54_first_exit_continuation_derivation.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/data/step54_first_exit_verify.json"
  ]
}
```

## Task

Verify the first-exit and continuation derivation in step54_first_exit_continuation_derivation.md. Focus on three critical mathematical points:

1. AUGMENTED ENERGY vs FLAT-TORUS TEST: The derivation claims that the flat-torus test (creating curvature from zero by nonconstant cutoff) does not invalidate augmented-energy estimates H_2 = int eta^2(1+|Rm|^2), because the normalization reaction +4a|R|^2 is absorbed by the CaF^3 reaction term already present. Check: is the reaction structure in the curvature power inequality (eq 4.4 of Step 35, eq 2.6 of this note) genuinely compatible with the normalization? Specifically, does the Hamilton quadratic + normalization + Hessian-a absorption close with the available dissipation, without introducing a bare additive constant?

2. DEFECT HOMOGENEITY: The derivation separates defect energies from curvature energies by the property B_def|_{E=0} = 0. Check whether every term in the J_6 evolution (eq 4.2) and the Q propagation (eq 7.2) genuinely has E-homogeneous coefficients. In particular, verify that the volume form variation d mu contributes an E-dependent term (not a curvature-only term) in the defect energy evolution.

3. CONTINUATION ARGUMENT: The staggered hierarchy (eq 6.2-6.3) claims that the highest cutoff jet C_{m+2} always carries a chi factor from the product rule nabla^{m+2}(chi^2) = 2 chi C_{m+2} + lower. Check: does this chi factor survive integration by parts and pairing with the weighted dissipation? Is there a term where the chi weight is consumed by a different factor, leaving a bare C_{m+2} contribution?

Provide a mathematical assessment of each point, identifying any gaps or errors.

## Output

## Verifier Memo — first-exit and continuation on the transported-cutoff flow (Step 54, with Steps 34–35 support)

I read Step 54 together with the index-level tensor derivations in Step 35, the fixed-exponent analytic layer in Step 34, and the verification data in `step54_first_exit_verify.json`. The three points you flagged are the load-bearing ones; below I reconstruct the relevant algebra from first principles and state where each is sound and where substance is still owed. I also record one concrete numerical inconsistency between the note and its own verification data.

---

### Point 1 — augmented curvature energy vs. the flat-torus source

**The mechanism is genuinely consistent at the level of $F=(1+|\mathrm{Rm}|^2)^{1/2}$, for a reason more specific than "the reaction absorbs it."**

The flat-torus observation is that $\partial_t\mathrm{Rm}|_{t=0}=O(\nabla^2 a)\neq0$ while $\mathrm{Rm}=0$, so $|\mathrm{Rm}|^2$ grows like $t^2$, not $t$; correspondingly $\partial_t|\mathrm{Rm}|^2|_{t=0}=2\langle\mathrm{Rm},\partial_t\mathrm{Rm}\rangle=0$ pointwise. This already shows the Hessian-$a$ source in $\partial_t|\mathrm{Rm}|^2$ must be **linear in $\mathrm{Rm}$**, which is exactly the structure Step 35 derives:
$$
\Sigma_H^{\mathrm{Rm}}=8A_{pq}B_{\mathrm{curv}}^{pq},\qquad B_{\mathrm{curv}}^{pq}=R^p{}_j{}^q{}_l E^{jl},\qquad |B_{\mathrm{curv}}|\le|\mathrm{Rm}|\,|E|.
$$
So the source vanishes at $\mathrm{Rm}=0$ and is controlled by $|\nabla^2a|\,|\mathrm{Rm}|\,|E|$.

I checked the $p=2$ signed integration by parts explicitly, because that is the case the note relies on for $H_2$ and it is the one where the radial dissipation coefficient $p(p-2)$ vanishes. With test factor $\tfrac{p}{2}\eta^2a^{p-2}F^{p-2}=\eta^2$ at $p=2$, routes (ii) and (iii) of Step 35 §3.3 are **identically zero** (derivatives of $a^0$ and $F^0$), route (i) vanishes because $\nabla a=0$ on $\operatorname{supp}\nabla\eta$, and only route (iv) survives:
$$
|T_H^{\mathrm{Rm}}|\le C\!\int|\nabla a|\,\eta^2 F|\nabla\mathrm{Rm}|
\le \varepsilon\!\int\eta^2 a|\nabla\mathrm{Rm}|^2+C_\varepsilon r^{-2}\!\int\eta^2F^2
=\varepsilon D_2^\eta+C_\varepsilon r^{-2}H_2 .
$$
This uses $|\nabla a|=2\chi|\nabla\chi|\le Ca^{1/2}r^{-1}$ and the derivative-structure bound $|\nabla B_{\mathrm{curv}}|\le CF|\nabla\mathrm{Rm}|$ (Step 35 (3.6)), and it produces **no collapse-dependent additive constant** — only $C r^{-2}H_2$, absorbed by the Bochner dissipation and the $H_2$ energy itself. The essential feature is that the "$+1$" in $F^2$ supplies a volume floor: $\operatorname{Vol}(\operatorname{supp}\eta)\le H_2$, so a source that is linear in curvature (hence bounded, after volume, by $H_2$) closes multiplicatively. This is exactly the distinction the note draws from the defect energies, and it holds up.

The cubic reaction $CaF^3$ (Hamilton quadratic + normalization $+4a|R|^2\le CaF^2\le CaF^3$ + volume term) is **not** absorbed by pointwise domination; it becomes the additive term $CY$ in $(K_2^\eta)'+cD_2^\eta\le CY+Cr^{-2}K_2^\eta$ (Step 34 (3.1)) and is then Sobolev-interpolated, $Y\le C\gamma(D_2^\eta+r^{-2}K_2^\eta)$ (Step 34 (3.4)), so for $C\gamma$ small it folds into the dissipation and $r^{-2}K_2^\eta$. This is multiplicative in the energy through the integrated potential $B(T)\le C\gamma^3$ with collapse-independent $\gamma\sim r^2\sqrt{1+\kappa_0^2}$; no bare volume constant enters. The note's remark after (2.14) ("all lower-order contributions from the $1$ in $F$ carry an active weight … not by a separate unweighted volume constant") is the correct bookkeeping and I confirm it.

The "$+1$" that appears in the Step 54 rate $C(1+r^{-2})H_2$ (versus the pure $r^{-2}$ of Step 34) traces to the volume-form variation $\partial_t d\mu=-a\tau\,d\mu$ giving $\int\eta^2F^2(-a\tau)\le C|E|_\infty H_2$, an $O(1)$ **multiplicative** rate, harmless over $[0,\theta r^2]$.

**What is still owed (as the note states in §9.2.1).** All of the above is on $F=(1+|\mathrm{Rm}|^2)^{1/2}$. The energy actually used is $F_T=(1+|T|^2)^{1/2}$, $T=\mathrm{Rm}+G$. Two things need explicit index-level redoing, not just norm equivalence (2.2):

- The diffusion/dissipation structure does carry through, because $\nabla G=0$ ($G$ is parallel), so $\Delta T=\Delta\mathrm{Rm}$, $|\nabla T|^2=|\nabla\mathrm{Rm}|^2$, and $\langle T,a\Delta\mathrm{Rm}\rangle=\tfrac a2\Delta|T|^2-a|\nabla T|^2$. This part I verified is benign.
- The **reaction coefficients** are not automatic. $\partial_t|T|^2$ picks up $2\langle T,\partial_t G\rangle$ with $\partial_t G=\tfrac{-2a}{2(n-1)}(E\owedge g+g\owedge E)$, an algebraic $O(a|E|\,|T|)\le CaF_T^2$ term, plus the cross term $2\langle\mathrm{Rm},G\rangle$ inside $|T|^2$. These are plausibly $\le CaF_T^3$ and absorbable, but the signed IBP contraction tensor should be re-derived as $B_{\mathrm{curv},T}^{pq}=T^p{}_j{}^q{}_l E^{jl}$ and its $|\nabla B_{\mathrm{curv},T}|\le CF_T|\nabla\mathrm{Rm}|$ bound written out. This is the one component of Point 1 that is asserted rather than derived.

---

### Point 2 — defect homogeneity, including the volume-form term

**Every coefficient in the $J_6$ and $Q_\alpha$ evolutions is genuinely $E$-homogeneous, and the volume-form variation is $E$-dependent because it is governed by $\tau=\operatorname{tr}E$, which is linear in $E$.** This is the correct and decisive fact.

The volume form varies as $\partial_t d\mu=\tfrac12 g^{ij}\partial_t g_{ij}\,d\mu=-a\tau\,d\mu$ with $\tau=\operatorname{tr}E$. The key pointwise algebraic inequality is
$$
|\tau|=|\operatorname{tr}E|\le\sqrt n\,|E|=\sqrt n\,s^{1/2}.
$$
This holds regardless of how large $\mathrm{Ric}$ or $R$ are, because $\tau$ is literally the trace of $E$, not the scalar curvature in isolation. Consequently:

- In $J_6=\int\eta^2a^4 s^3$ the volume term is $-\int\eta^2 a^5\tau s^3$, bounded by $C\int\eta^2 a^5 s^{7/2}$. Since $s^{1/2}=|E|\le CF$, this is $\le C\int\eta^2 a^5 F s^3=CP_6$, folded into the linear-in-$F$ potential $P_6\le C\gamma(X_6+r^{-2}J_6)$ (Step 34 (5.12)). It carries the full $s^3$ and thus vanishes at $E=0$.
- In $Q_\alpha=\int\eta^2 s$ the volume term is $-\int\eta^2 a\tau s\le C\int\eta^2 a s^{3/2}\le C\|E\|_\infty\,Q_\alpha$, again proportional to $s$.

I also checked the other reaction terms. The non-cutoff reaction in $(\partial_t-a\Delta)s\le -2a|\nabla E|^2+\Sigma_s$ has $|\Sigma_s|\le CaFs+Cas$: the factor $F$ is a curvature coefficient, but the whole term carries $s=|E|^2$, so it vanishes at $E=0$ and enters as $P_6$ (in $J_6$) or as $CK\,Q_\alpha$ under a curvature bound $K$ (in $Q$). The Hessian-$a$ contraction $B_{\mathrm{def}}^{pq}=|E|^2g^{pq}+(\operatorname{tr}E)E^{pq}-2(E^2)^{pq}$ is manifestly quadratic in $E$ with $B_{\mathrm{def}}|_{E=0}=0$ and $|\nabla B_{\mathrm{def}}|\le Cs^{1/2}|\nabla E|$; the signed IBP gives $|T_H^E|\le\varepsilon X_6+Cr^{-2}J_6$. Nothing here is curvature-only. This is exactly the property that keeps $E=0$ an exact stationary point of every energy in the defect tower, so $Q/A\to0$ propagates.

**One structural coupling to record.** The $Q_\alpha$-Grönwall coefficient in (7.2) is $C(1+r^{-2})$ only after using a curvature bound $K$ to control $\int\eta^2 aFs\le CK\,Q_\alpha$. So the defect branch consumes the curvature endpoint (§3), while the curvature branch (§2.3) uses $|E|$ smallness to bound the volume rate. This is a **simultaneous** first-exit bootstrap, which the note itself lists as unclosed (§9.2.3–5; Step 34 §7.3). I note that the circularity is likely loosenable: the curvature energy $H_2$ tolerates the volume term via $|E|\le CF$ (folding it into $Y$) rather than genuinely needing $|E|\le\delta$, so the two branches need not be tightly interlocked. But the coupled continuity argument with explicit constants is not written, and the a-posteriori Sobolev-constant closure ($\mathcal S(t)\le2\mathcal S(0)$, §5.2) depends on it.

Verdict on Point 2: correct, including the specific point you asked about — the volume-form contribution is $E$-dependent through $\operatorname{tr}E$, not curvature-only.

---

### Point 3 — the staggered continuation and the surviving $\chi$

**The algebraic identity is correct and, if anything, understated; the deeper reason continuation works is that the top cutoff jet has the bounded defect $E$ as its coefficient — a point the note's §6.2 phrasing does not make explicit.**

The Leibniz expansion is exactly as stated: in $\nabla^{m+2}(\chi^2)=\sum_k\binom{m+2}{k}\nabla^k\chi\otimes\nabla^{m+2-k}\chi$, the top jet $C_{m+2}=\nabla^{m+2}\chi$ occurs only at $k=0,m+2$, giving $2\chi C_{m+2}$; all other terms pair two jets of order $\le m+1$. So the top jet carries one $\chi$.

However, the term in which $C_{m+2}$ actually appears in $\partial_t U_m$, $U_m=\nabla^m(aT)$, arises from $\nabla^m$ acting on the Hessian-cutoff source $a\,(\nabla^2a)\!*\!E$ (Step 35 Type H, $(H_a)\sim(\nabla^2a)*E$), and putting all $m$ derivatives on $\nabla^2a$ gives
$$
a\,(\nabla^{m+2}a)\!*\!E\;\sim\;\chi^2\cdot 2\chi C_{m+2}\!*\!E\;=\;2\chi^3\,C_{m+2}\!*\!E .
$$
So the surviving weight is $\chi^3$, and — decisively — **the coefficient of $C_{m+2}$ is the defect $E$, not bare curvature $T$.** I traced the integration by parts (moving one derivative off $C_{m+2}=\nabla C_{m+1}$) through its landing sites:

- derivative onto $|U_m|^{p-2}U_m$: yields $\int|U_m|^{p-2}\nabla U_m\,\chi^3 E\,C_{m+1}$; a single $\chi$ pairs with the weighted dissipation via $(\chi\nabla U_m)\!\cdot\!X\le\varepsilon\chi^2|\nabla U_m|^2+C_\varepsilon X^2$, and this needs only **one** $\chi$ against $\int\chi^2|\nabla U_m|^2|U_m|^{p-2}$ — so even the note's minimal counting suffices;
- derivative onto $\chi^3$: yields $\int|U_m|^{p-1}\chi^2 C_1 E\,C_{m+1}$, still carrying $\chi^2$ and a bounded $E$, hence $\le Cr^{-(m+2)}\int|U_m|^{p-1}$;
- derivative onto $E$: yields $\chi^3\nabla E$, i.e. $\chi\cdot a\nabla E$, and $a\nabla E=\nabla(aE)-(\nabla a)E$ is a weighted first-order defect quantity, controlled.

This is why the answer to your precise question ("is there a term where the $\chi$ weight is consumed by a different factor, leaving a bare $C_{m+2}$?") is: even when the derivative differentiates $\chi$, the resulting term is not dangerous, because its coefficient is the **bounded** defect $E$ and multiplies the zeroth-order energy $\|U_m\|_p^p$. Had the coefficient been bare curvature $T$ (which degenerates like $1/a$ on the collar, since $|aT|\le C\gamma/t$ only bounds the weighted quantity), such a term would be uncontrolled. So the correctness rests on the Type-H coupling to $E$, which the note relies on implicitly but does not state as the reason.

**What remains genuinely unproved here (as flagged in §9.2.3, §6.3, Step 34 §7.4).**

1. The full finite-order induction over **all** commutator terms $[\nabla^m,a\Delta]$ and mixed jets $C_j\otimes C_{m+2-j}$ is not carried out. In particular the intermediate family $(\nabla^m a)\,\nabla^2 T\sim\chi C_m\,T_2$ pairs a moderate cutoff jet with a bare high curvature derivative $T_2=\nabla^2T$ on the collar; these must be re-expressed through the weighted variables $U_k=\nabla^k(aT)$ rather than through bare $\nabla^kT$, and that rewriting is asserted, not shown.

2. The recovery statement in §6.3 — "$|\nabla^m T|$ on the collar is recovered from $U_m$ using $a\ge0$" — is loose. Inverting $U_m=\nabla^m(aT)$ for $\nabla^mT$ involves a $1/a$ recursion that is singular where $a\to0$. The logic only works because bounded $\nabla^mT$ is needed where $a$ is bounded below (the plateau $\{a=1\}$, where $\nabla^mT=U_m$ directly, and the inner buffer), not on the collar edge where $a\to0$ (which is decoupled/stationary). The conclusion is plausible under the buffer geometry ($a=0$ on $\operatorname{supp}\nabla\eta$), but the note should state where curvature control is actually required and confine the recovery there.

3. The Grönwall coefficients in (6.3) are said to come "from the curvature endpoint (3.4)" but are not computed; the restart-at-maximal-time argument (§6.3) depends on these being finite and independent of the datum index.

---

### Internal inconsistency in the verification data

There is a concrete factor-of-4 discrepancy between the note and its own script:

- Step 54 §2.1 states $|G|^2=\dfrac{2n}{n-1}$, i.e. $8/3\approx2.667$ at $n=4$.
- `step54_first_exit_verify.json`, check `G_norm_squared_n4`, records $|G|^2=\dfrac{n}{2(n-1)}=0.6667$.

These are two different formulas differing by exactly $4$, reflecting different normalizations of the Kulkarni–Nomizu product $g\owedge g$ (or of the curvature norm). It does not break the norm equivalence (2.2), which holds with order-one constants either way — but the JSON's `norm_equivalence_constants` ($c_n\ge0.333$, $C_n\le3.30$) are consistent with neither value cleanly ($C_n=1+2|G|^2$ gives $6.3$ for $8/3$ and $2.3$ for $2/3$; the sharp lower constant $c_n=1/(1+|G|^2)$ gives $0.27$ and $0.60$). The $\owedge$/norm convention should be fixed once and propagated to §2.1, the equivalence constants, and any estimate quantitative in $|G|$; otherwise the definition of $F_T$ itself is ambiguous between the analytic note and the checked identities. By contrast, the JSON's `B_def_flat_torus` value $6\,g^{pq}$ (at $E=g$) and `B_def_size_bound` $|B_{\mathrm{def}}|\le8|E|^2$ both reproduce Step 35 §6 correctly, so the defect side is self-consistent.

---

### Summary of the state of the three points

- **Point 1:** The absorption of the flat-torus normalization source into the augmented energy is sound on $F$; the linear-in-$\mathrm{Rm}$ Hessian source closes through signed IBP with the $F^2$ volume floor and produces no collapse-dependent additive constant. The remaining substance is the explicit $F\to F_T$ recomputation of the reaction coefficients and the contraction tensor $B_{\mathrm{curv},T}$; the diffusion side transfers cleanly because $\nabla G=0$.
- **Point 2:** Fully $E$-homogeneous, including the volume-form term, which is $E$-linear through $\tau=\operatorname{tr}E$ with $|\tau|\le\sqrt n\,|E|$. The one open item is the coupled curvature–defect first-exit continuity closure (constants and $\mathcal S(t)$ control).
- **Point 3:** The $\chi$-weight identity is correct and one $\chi$ suffices to pair with the dissipation; the actual survival is stronger because the top jet's coefficient is bounded $E$. The full finite-order induction, the treatment of intermediate bare-curvature-derivative terms, and the collar recovery statement are asserted and need to be written out.

The note is internally coherent as an architecture, and its own §9 correctly enumerates the five components still needing derivation. The specific mathematical hinges are exactly the three you named plus the $|G|^2$ normalization reconciliation.