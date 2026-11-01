# TTCS Independent Branch Record

```json
{
  "step_id": 70,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step70_selected_support_lemma.md",
    "Sessions/S0910A01/workspace/notes/step68_restricted_IL_canonical_assembly.md"
  ]
}
```

## Task

Verify the mathematical correctness and completeness of the selected-support lemma for the restricted IL negative-gap theorem. The note proves:

1. FULL-CURVATURE BUDGET: ∫|Rm|² ≤ C₀A_i from Chern-Gauss-Bonnet, using I-J=2A/3-q, J≤δ²Vol/(2π²), and Vol≤CA. Check that the identities are correctly applied, the volume upper bound derivation from the mixed SW inequality is valid, and equation (2.4) ∫|Rm|²=8π²χ+3/2∫|Ric°|² holds.

2. WEAK-TYPE MAXIMAL INEQUALITY: Lemma 4.1 under Ric≥-(n-1)g. Check the Vitali covering argument, the Bishop-Gromov volume doubling ratio, and the constant C(n,R₀).

3. COLLAPSE-CANCELLING PRODUCT: γ_α(0)=S_α·H_{2,α}^{1/2}≤C(r²+γ̃). The claim is that S_α~r²/Vol^{1/2} grows under collapse while H_{2,α}^{1/2}~Vol^{1/2}·(1+γ̃/r²) shrinks, so their product eliminates volume. Check each factor's scaling carefully, especially whether H₂ = ∫η²F_T² ≤ C(1+γ̃²/r⁴)Vol is correct.

4. PARAMETER ORDERING: The construction requires fixing γ̃ before r. Verify that the constraints C₁r⁴/γ̃² < c_V/2 and C(r²+γ̃) < γ*/2 are simultaneously satisfiable.

5. INTERFACE: Check that the listed outputs (7 sequence-uniform items and 5 datum-dependent items) are correctly categorized. In particular, is it true that no sequence-uniform bound on initial sectional curvature is needed?

## Output

# Verification Memo: Selected-Support Lemma (Step 70) for the IL Sign-Definite Gap Result

Session S0910A01. Independent scientific check of the five requested items, plus two additional findings inside the module. Bottom line up front: the central deliverables of the module — the integral curvature budget $\int|\mathrm{Rm}|^2\le C_0A_i$, the volume comparison $c_VA_i\le\mathrm{Vol}\le C_VA_i$, the weak-type maximal inequality, and the collapse-cancelling product $\gamma_\alpha(0)\le C(r^2+\widetilde\gamma)$ — are mathematically sound and the parameter ordering closes. However, two intermediate derivations reach correct conclusions through arithmetically wrong intermediate lines that mix norm conventions, and one load-bearing volume constant is derived from an incorrect mean value. These should be rewritten in one convention so the constants are trustworthy for downstream use.

---

## Point 1 — Full-curvature budget (Prop 2.1)

**The conclusion (2.1)/(2.9) $\int|\mathrm{Rm}|^2\le C_0A_i$ holds, but equation (2.4) is derived by combining two formulas written in different norm conventions.**

Equation (2.2) is the Gauss–Bonnet integrand with **tensor** norms: coefficient $+1$ on $|W|^2$, $-\tfrac12$ on $|\mathring{\mathrm{Ric}}|^2$, $\tfrac1{24}$ on $s^2$. This is Besse's form and is correct with $|W|^2=W_{ijkl}W^{ijkl}$, etc.

Equation (2.3), $|\mathrm{Rm}|^2=|W|^2+|\mathring{\mathrm{Ric}}|^2+\tfrac{s^2}{24}$, is instead the **operator-Frobenius** decomposition (which is the convention giving $|G|^2=2/3$ — I confirmed this: $G=\tfrac16 g\owedge g$ acts on $\Lambda^2$ as $\tfrac13\,\mathrm{Id}$, Frobenius norm$^2=6\cdot\tfrac19=\tfrac23$). In this convention the note's symbols satisfy $|W|^2=|W^+|^2_F+|W^-|^2_F=\tfrac14|W|^2_{\rm tensor}$ and $|\mathring{\mathrm{Ric}}|^2=2|\mathring{\mathrm{Ric}}_0|^2_F=\tfrac12|\mathring{\mathrm{Ric}}|^2_{\rm tensor}$.

The two conventions are incompatible: (2.2) forces tensor weights, (2.3) forces operator weights ($\rho=\tfrac14$). No single scaling makes both true as written. Consequently the subtraction producing (2.4) mixes conventions. The honest relation, done entirely in tensor norm, is

$$
\int|\mathrm{Rm}|^2_{\rm tensor}=8\pi^2\chi+\tfrac52\int|\mathring{\mathrm{Ric}}|^2_{\rm tensor}+\tfrac18\int s^2 .
$$

The note's (2.4) has coefficient $\tfrac32$ (not $\tfrac52$) on $|\mathring{\mathrm{Ric}}|^2$ **and drops the $\tfrac18\int s^2$ term entirely**. The Weyl term does cancel correctly in tensor norm (both GB and the decomposition carry weight $1$), which is presumably why the note believed no other term survives; but the scalar terms differ ($\tfrac16$ in the decomposition versus $\tfrac1{24}$ in GB), leaving $\tfrac18\int s^2$.

**Why Prop 2.1 nonetheless survives.** Every dropped or mis-weighted term is $O(A_i)$: with $s=-4+\tau$, $|\tau|\le4\delta_i$, one has $\int s^2\approx16\,\mathrm{Vol}\le CA_i$ by the volume bound (2.8), and $\int|\mathring{\mathrm{Ric}}|^2=O(\delta_i^2A_i)$. So $\int|\mathrm{Rm}|^2=8\pi^2\chi+O(A_i)+O(\delta_i^2A_i)\le C_0A_i$ regardless of the $\tfrac32$-vs-$\tfrac52$ discrepancy and the missing scalar term. The downstream maximal-function argument is insensitive to the norm choice (it only rescales $C_0$). **Recommendation: rewrite Steps 1–5 entirely in tensor norm with the identity above, so the stated constants are defensible.**

**Two further wording problems in Step 2.** (i) The line "$8\pi^2\chi(M_i)=I_i+J_i$" is mislabeled: the standard identity is $2\chi+3\tau=I-J$, and $I+J$ is not $8\pi^2\chi$. (ii) The Euler formula uses $\sum_j(c_1^2+c_2)(X_j)$ where the topological Euler number of each surface is $\chi_{\rm top}(X_j)=c_2(X_j)$ only, not $c_1^2+c_2$. Both are harmless for the $O(A)$ conclusion, and $\chi(M_i)=O(A_i)$ has an independent confirmation via the Noether inequality: for a minimal general-type surface $c_2\le 5c_1^2+36$, hence $\chi(X_j)=O(c_1^2(X_j))$ and $\chi(M_i)=O(A_i)$. I recommend citing Noether directly rather than the garbled SW line.

**Volume upper bound (2.8) is correct.** I checked the chain: $s\ge-4-4\delta_i$ gives $I\ge\tfrac{(1-\delta_i)^2}{6\pi^2}\mathrm{Vol}$; combined with $I\le J+\tfrac{2A}{3}$ and $J\le\tfrac{\delta_i^2}{2\pi^2}\mathrm{Vol}$; rearranging with $(1-\delta_i)^2-3\delta_i^2>0$ for $\delta_i<\tfrac14$ (value $\approx0.375$ at $\delta_i=\tfrac14$) yields $\mathrm{Vol}\le CA_i$. The trace-free bound (2.6) $|\mathring{\mathrm{Ric}}|\le2\delta_i$ is correct: $\mathring{\mathrm{Ric}}=E-\tfrac{\operatorname{tr}E}{4}g$ with $|E|\le\delta_i$, $|\operatorname{tr}E|\le4\delta_i$.

---

## Point 2 — Weak-type maximal inequality (Lemma 4.1)

**Correct.** This is the standard Hardy–Littlewood argument transplanted to a manifold with $\mathrm{Ric}\ge-(n-1)g$. The Vitali $5s$-covering, disjointness of the selected $B_{s_j}$, and Bishop–Gromov doubling $\tfrac{\mathrm{Vol}(B_{5s})}{\mathrm{Vol}(B_s)}\le\tfrac{V_{-1}(5s)}{V_{-1}(s)}\le C(n,R_0)$ for $s\le R_0$ are all applied correctly. The manifolds qualify: $\mathrm{Ric}=-g+E$ with $|E|\le\delta_i$ gives $\mathrm{Ric}\ge-(1+\delta_i)g\ge-3g$, so $n-1=3$ holds comfortably.

Two cosmetic slips, neither affecting the constant's finiteness: Remark 4.2 writes the ratio as $V_{-1}(5R_0)/V_{-1}(R_0/5)$ where $V_{-1}(5R_0)/V_{-1}(R_0)$ is what the argument uses (the sup over $s\le R_0$ of $V_{-1}(5s)/V_{-1}(s)$ is attained at $s=R_0$). And in §7.2 the model parameter is written $\kappa=\sqrt3$ while $\mathrm{Ric}\ge-3g=-(n-1)\cdot1\cdot g$ corresponds to $\kappa=1$; since $R=7r$ is small, $e^{C\kappa R}$ is bounded either way and the leading constant "$\approx 5^n=625$" for small $R_0$ is right.

---

## Point 3 — Collapse-cancelling product (Prop 7.1)

**Fully correct, and this is the genuinely load-bearing insight of the module. Both factor scalings check out.**

*Energy factor (7.3).* $F_T^2=1+|T|^2\le1+2|\mathrm{Rm}|^2+2|G|^2=\tfrac73+2|\mathrm{Rm}|^2$, so $H_{2,\alpha}(0)\le C\int_{U_\alpha}(1+|\mathrm{Rm}|^2)=C(\mathrm{Vol}(U_\alpha)+\int_{U_\alpha}|\mathrm{Rm}|^2)$. The maximal-function condition (7.1) gives $\int_{U_\alpha}|\mathrm{Rm}|^2\le\tfrac{\widetilde\gamma^2}{r^4}\mathrm{Vol}(U_\alpha)$, hence $H_{2,\alpha}(0)\le C(1+\widetilde\gamma^2/r^4)\mathrm{Vol}(U_\alpha)$. Correct.

*Sobolev factor (7.5).* I reproduced this from the Saloff-Coste local Sobolev inequality under $\mathrm{Ric}\ge-(n-1)$: in averaged form on $B_R$, $\big(\fint|u|^4\big)^{1/2}\le CR^2\big(\fint|\nabla u|^2+R^{-2}\fint|u|^2\big)$. Converting the averages to $L^2/L^4$ norms multiplies the left by $\mathrm{Vol}^{-1/2}$ and the right by $\mathrm{Vol}^{-1}$, giving $\|u\|_{L^4}^2\le CR^2\mathrm{Vol}(U)^{-1/2}(\|\nabla u\|_2^2+R^{-2}\|u\|_2^2)$. With $R=7r$ this is exactly $\mathcal S_\alpha(0)\le C(L_\eta)r^2\mathrm{Vol}(U_\alpha)^{-1/2}$. Correct, including the $r^{-2}$ weight in (7.4).

*Product.* $\gamma_\alpha(0)=\mathcal S_\alpha H_{2,\alpha}^{1/2}\le Cr^2\mathrm{Vol}^{-1/2}\cdot[C(1+\widetilde\gamma^2/r^4)\mathrm{Vol}]^{1/2}=Cr^2(1+\widetilde\gamma^2/r^4)^{1/2}=C(r^4+\widetilde\gamma^2)^{1/2}\le C(r^2+\widetilde\gamma)$. The volume cancels identically; the mechanism ($\mathcal S\sim r^2\mathrm{Vol}^{-1/2}$ grows under collapse, $H^{1/2}\sim\mathrm{Vol}^{1/2}(1+\widetilde\gamma/r^2)$ shrinks) is exactly as stated. This is a clean and correct piece of analysis and is the reason the construction does not need a non-collapse hypothesis.

---

## Point 4 — Parameter ordering

**Satisfiable, no circularity.** The two constraints are $C(r^2+\widetilde\gamma)\le\gamma_*/2$ (initial absorption below the bootstrap threshold) and $C_1r^4/\widetilde\gamma^2<c_V/2$ (good-set retains an $A$-proportional fraction). Fixing $\widetilde\gamma$ first at $\widetilde\gamma=\min(\gamma_*/(4C),\,c_{\rm abs}/(2C))>0$, then choosing $r$ small enough that $r^2<\gamma_*/(4C)$ **and** $r^4<c_V\widetilde\gamma^2/(2C_1)$, satisfies both. The second constraint pushes $r\ll\widetilde\gamma^{1/2}$, which is compatible because $\widetilde\gamma$ is already a fixed positive number when $r$ is chosen. The ordering is well-posed.

One dependency to keep in view: this closure presumes $\gamma_*,V_*,\theta,c_{\rm abs}$ are universal (dimension-only) and do **not** secretly depend on $r$ or $\widetilde\gamma$. The factor $C_H(1+r^{-2})$ in the bootstrap (6.4) is neutralized by the short horizon $T\le\theta r^2$, since $C_H(1+r^{-2})\theta r^2=C_H\theta(1+r^2)$ is bounded — the correct parabolic scaling. The universality of these constants lives in the bootstrap modules (assembly §6), not this note, and the assembly itself lists the real-exponent defect-Moser recurrence and simultaneous first-exit closure as not yet written in independent proof text.

---

## Point 5 — Interface categorization

**Correct as stated for this module.** The seven sequence-uniform items (integral curvature budget, shifted budget, two-sided volume comparison, good-set volume, retained colored volume, disjoint supports, absorption product, support identities, cutoff gradient, $Q(0)/A_i\to0$) genuinely depend only on $n=4$, the universal parameters $r,\widetilde\gamma,\theta,\gamma_*,V_*$, and the Chern–Weil/SW constants — not on $i$ or the individual $X_j$/topology. The five datum-dependent items (higher cutoff jets $m\ge2$, per-datum existence time, $\mathcal S_\alpha(0)$, $H_{2,\alpha}(0)$, initial sectional curvature) are correctly identified as tied to local geometry and possible collapse.

The assertion that **no sequence-uniform initial sectional-curvature bound is needed** is true *within this module*: the only curvature inputs used are the integral budget $\int|\mathrm{Rm}|^2\le C_0A_i$ and the mean bound $\fint_{U_\alpha}|\mathrm{Rm}|^2\le\widetilde\gamma^2/r^4$, both integral/averaged, plus the product $\gamma_\alpha(0)$ whose smallness holds even though $\mathcal S_\alpha$ and $H_{2,\alpha}$ individually are uncontrolled. The pointwise sectional curvature at $t=0$ is genuinely unused here.

What this module does **not** establish, and correctly defers, is that these averaged inputs suffice to run the smoothing flow into positive-time pointwise curvature under possible collapse. That conversion is the crux of the whole program; the assembly (§6.4, §6.5) flags the positive-time Moser endpoints and the real-exponent recurrence as still to be displayed independently. So the interface is stated coherently, but its usefulness rests on downstream work not contained here.

---

## Additional finding A — Volume lower bound (Prop 3.1): correct constant, wrong intermediate mean

The boxed result $\mathrm{Vol}\ge\tfrac{32\pi^2}{9}A_i(1-C\delta_i)$ is the correct value, but the derivation states the wrong mean and the displayed division does not produce the boxed number.

The proof writes "$\tfrac{s^2}{24}+2|W^+|^2\to\tfrac29$ in $L^1$-normalized mean" and then "$\mathrm{Vol}=\tfrac{4\pi^2I}{\langle\cdot\rangle}\ge\tfrac{8\pi^2A/3}{2/9}=\tfrac{32\pi^2}9A$." But $\tfrac{8\pi^2A/3}{2/9}=12\pi^2A$, not $\tfrac{32\pi^2}9A\approx3.56\pi^2A$.

The correct mean is $\tfrac34$, not $\tfrac29$. In the pinching limit the calibration $\int(s+8\sqrt6|W^+|)^2\le108Q\to0$ forces $|W^+|^2\to\tfrac1{24}$ (with $s\to-4$), so $\tfrac{s^2}{24}+2|W^+|^2\to\tfrac{16}{24}+\tfrac2{24}=\tfrac{18}{24}=\tfrac34$. Then $\mathrm{Vol}=\tfrac{4\pi^2I}{3/4}=\tfrac{4\pi^2\cdot(2/3)A}{3/4}=\tfrac{32\pi^2}{9}A$, matching the box. So: replace "$2/9$" with "$3/4$" and correct the division. This is worth fixing precisely because the constant $\tfrac{32\pi^2}{9}$ is load-bearing for $c_V$; note, though, that the good-set argument in §4 only needs *some* universal $c_V>0$, which is secure independent of the exact numerology.

---

## Additional finding B — coloring and packing (§5)

The degree bound and greedy coloring are correct. $D_0\le V_{-1}(15r)/v_{-1}(r/2)\approx30^4$ for small $r$ under $\mathrm{Ric}\ge-3g$; greedy coloring with $D_0+1$ colors, then pigeonhole. The plateau-volume retention is valid because within one color class the $B_{7r}$ (hence $B_r$) are disjoint, so $\mathrm{Vol}(\bigcup_{\rm class}B_r)=\sum_{\rm class}\mathrm{Vol}(B_r)\ge\tfrac1{D_0+1}\sum_{\rm all}\mathrm{Vol}(B_r)\ge\tfrac{\alpha_1A}{D_0+1}$, using $\sum_{\rm all}\mathrm{Vol}(B_r)\ge\mathrm{Vol}(\bigcup B_r)\ge\alpha_1A$. Correct.

---

## Consolidated assessment

The module's structural mathematics is sound: the maximal-function selection, the packing/coloring, the disjoint-support cutoff architecture with the identity $a_i|\nabla\eta_\alpha|^2=0$, and above all the collapse-cancelling product are correct and well-argued. The three errors are all in the **numerical bookkeeping of constants and conventions**, and in each case the qualitative conclusion (an $O(A)$ curvature budget, a positive $A$-proportional volume lower bound, a uniformly small absorption product) is unaffected:

1. (2.2)–(2.4) silently switch between tensor and operator-Frobenius norms; the honest tensor identity carries a $\tfrac52$ Ricci coefficient and an extra $\tfrac18\int s^2$, both $O(A)$.
2. "$8\pi^2\chi=I+J$" and the Euler formula using $c_1^2+c_2$ are mislabeled; Noether gives $\chi=O(A)$ cleanly.
3. Prop 3.1's intermediate mean should read $\tfrac34$; the boxed $\tfrac{32\pi^2}{9}A$ is correct.

For downstream reliability the single most valuable rewrite is to fix one norm convention (tensor throughout §2 is simplest) and re-derive the constants $C_0$, $c_V$, $C_V$ from it, so that the sequence-uniform table in §8 rests on internally consistent numerology. The convention-audit table in the companion assembly (step68 §12) suggests these norm identifications were flagged as fragile before; the specific tensor/operator conflation in (2.2)/(2.3) is a concrete instance still to be reconciled.

Unresolved beyond this module (and correctly deferred): whether the averaged, product-form initial data delivered here suffice to run the cutoff flow to positive-time pointwise curvature under possible collapse — the positive-time Moser endpoints and real-exponent defect recurrence of assembly §6 are the substance needed, and are stated there as not yet written in full.