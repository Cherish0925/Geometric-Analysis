# TTCS Independent Branch Record

```json
{
  "step_id": 43,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step43_terminal_density_G_lemma.md",
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/notes/step43_corrected_negative_IL_theorem.md",
    "Sessions/S0910A03/trace/ttcs/results/step42_ttcs01_verifier2_integration.md"
  ]
}
```

## Task

Verify the terminal spectral density derivation in step43_terminal_density_G_lemma.md. Check: (1) that f = -2q/3 is correct with the stated conventions (q = sqrt(6)|W+| - s, f = 2s/3 - 2*sqrt(2/3)|W+|); (2) that the integral identity int G = (4/9)E - int(b_-)^2 follows from pointwise algebra; (3) that the LeBrun conformal/Yamabe decomposition (4/9)Delta_a = D_spec + D_Yam + D_mono correctly establishes D_spec <= (4/9)Delta_a (in particular, verify from the source at quantitative_deficit_analysis.md eq 24 that D_Yam and D_mono are both nonneg); (4) that Delta_a <= 108pi^2(R - q_top) follows from K <= 3I/2, I = T_M + R, T_M = 2A/3 - q_top, and p >= A; (5) that R <= Q/(8pi^2) uses Ric^0 = E^0 correctly; (6) that the bound applies to the evolved terminal metric without pointwise Ricci pinching. Also verify the coefficient 912 = 864 + 48 in the full density. If any step contains an error, identify the exact formula and the correction.

## Output

# Verification Memo: Terminal Spectral Density Chain in `step43_terminal_density_G_lemma.md`

I worked through each of the six requested points plus the two supporting lemmas and the pointwise identity that the chain rests on. Every algebraic and arithmetic step reproduces correctly. One input is genuinely imported rather than derived here, and one passage of prose is garbled while its conclusion is right. Details below, with the explicit computations so the core agent can re-check independently.

## (1) $f = -\tfrac23 q$ — confirmed

With $q = \sqrt6\,u - s$ and $f = \tfrac23 s - 2\alpha u$, $\alpha=\sqrt{2/3}$:
$$2\alpha u = 2\sqrt{\tfrac23}\,u = \frac{2\sqrt2}{\sqrt3}u = \frac{2\sqrt6}{3}u = \frac23\sqrt6\,u.$$
Hence $f = \tfrac23 s - \tfrac23\sqrt6\,u = -\tfrac23(\sqrt6\,u - s) = -\tfrac23 q$. Correct.

## (2) $\int G = \tfrac49 E - \int(b_-)^2$ — confirmed

$q^2 = (\sqrt6 u - s)^2 = (s-\sqrt6 u)^2$, so $E := \int q^2 = \int(s-\sqrt6|W^+|)^2$ as defined. Then $\int f^2 = \tfrac49\int q^2 = \tfrac49 E$, and $\int G = \int f^2 - \int(b_-)^2 = \tfrac49 E - \int(b_-)^2$. Correct.

I also re-verified the two supporting lemmas, since the terminal contradiction depends on them:

- **Lemma 1.1** ($G\ge0$): $b = f + 2\xi$ with $\xi = w+\alpha u \ge 0$, so $b\ge f$. If $b\ge0$, $(b_-)^2=0\le f^2$. If $b<0$, then $f\le b<0$ gives $|f|\ge|b|$, so $f^2\ge b^2=(b_-)^2$. Equality iff $\xi=0$ or $f=0$. Correct.
- **Lemma 1.2** (spectrum): at $s=-4$, $u^2=1/24$ one gets $\alpha u = \sqrt{2/3}\cdot\frac{1}{2\sqrt6}=\tfrac16$, $f=-\tfrac83-\tfrac13=-3$, $\xi\in[0,\tfrac16]$, $b=-3+2\xi<0$, so $G=9-(3-2\xi)^2=4\xi(3-\xi)$; $G=0\iff\xi=0\iff w=-\tfrac16$. Then $\lambda_1+\lambda_2=\tfrac16$, $\lambda_1^2+\lambda_2^2=\tfrac1{24}-\tfrac1{36}=\tfrac1{72}$, so $(\lambda_1-\lambda_2)^2=2\cdot\tfrac1{72}-\tfrac1{36}=0$, giving $\lambda_1=\lambda_2=\tfrac1{12}$. Spectrum $(-\tfrac16,\tfrac1{12},\tfrac1{12})$. Correct.

## (3) Yamabe decomposition and $D_{\rm spec}\le\tfrac49\Delta_a$ — internally consistent; rests on an imported LeBrun spectral lower bound

The telescoping of Codex eq. (24) is exact:
$$\tfrac49\Delta_a=\underbrace{(\tfrac49 E - G(g))}_{D_{\rm spec}}+\underbrace{(G(g)-G(g_\gamma))}_{D_{\rm Yam}}+\underbrace{(G(g_\gamma)-32\pi^2 p)}_{D_{\rm mono}},$$
where $G(g)=\int(\tfrac23 s+2w_{\min})_-^2 = \int(b_-)^2$. The sum reduces to $\tfrac49 E - 32\pi^2 p = \tfrac49(E-72\pi^2 p)=\tfrac49\Delta_a$, and $32\pi^2 = \tfrac49\cdot72\pi^2$ is the correct coefficient linking the density normalization to the $72\pi^2$ of the mixed estimate (3.2). So the identity closes.

$D_{\rm spec}\le\tfrac49\Delta_a$ then follows **iff** $D_{\rm Yam}\ge0$ and $D_{\rm mono}\ge0$. The nonnegativity of these two is exactly two published LeBrun statements: $g_\gamma$ minimizes $G(\cdot)$ over its conformal class ($D_{\rm Yam}\ge0$), and $G(g_\gamma)\ge32\pi^2 p$ (the spectral lower bound at the minimizer, $D_{\rm mono}\ge0$).

Point worth flagging for the core agent, because it is the true load-bearing import: the rearranged form $\int(b_-)^2\ge32\pi^2 p$ does **not** follow from the mixed monopole inequality (3.2) alone. From (3.2), $\int f^2=\tfrac49 E\ge32\pi^2 p$, but $(b_-)^2\le f^2$ pointwise (Lemma 1.1), so the mixed estimate only gives the *wrong-direction* bound $\int(b_-)^2\le\tfrac49 E$. The needed inequality is a genuine lower bound on the smaller quantity $\int(b_-)^2$, which is LeBrun's separate spectral/generalized-Yamabe theorem (older paper, Thm 2.3 / Prop 2.4). The file cites it correctly, but the entire Step C is only as strong as that imported theorem. This should be understood as the single external analytic pillar of the $\int G$ bound, distinct from the mixed estimate.

## (4) $\Delta_a\le108\pi^2(R-q_{\rm top})$ — confirmed

$\Delta_a=72\pi^2(K-p)$, $p\ge A\Rightarrow\Delta_a\le72\pi^2(K-A)$. From (3.3), $K\le\tfrac32 I$; from (3.1), $I=T_M+R$; and $T_M=A-D=2A/3-q_{\rm top}$ (connected-sum count: $m+1$ summands, $m$ operations, $-4m$; with $D=4m-(2\chi+3\tau)(N)$ this gives $T_M=A-D$ — verified). Then $K\le A-\tfrac32 q_{\rm top}+\tfrac32 R$, so $K-A\le\tfrac32(R-q_{\rm top})$ and $\Delta_a\le108\pi^2(R-q_{\rm top})$. Correct.

I re-derived the two feeder identities:
- Identity (18): $27(\tfrac{s^2}{24}+2u^2)-(s-\sqrt6 u)^2=\tfrac18 s^2+48u^2+2\sqrt6 su=\tfrac18(s+8\sqrt6 u)^2$. Correct.
- (3.3): integrating (18), $\tfrac18\int t^2 = 108\pi^2 I - 72\pi^2 K\ge0\Rightarrow K\le\tfrac32 I$. Correct.

A structural remark: since $\Delta_a\ge0$, the inequality forces $R-q_{\rm top}\ge0$ automatically. So even when $q_{\rm top}>0$ one necessarily has $R\ge q_{\rm top}$, and the subsequent split $R-q_{\rm top}\le R+(-q_{\rm top})_+$ is consistent. There is no regime where the bound asserts $\int G\le(\text{negative})$.

## (5) $R\le Q/(8\pi^2)$ via $\operatorname{Ric}^\circ=E^\circ$ — result correct, prose in Step A is garbled

The algebra is right: with $E=\operatorname{Ric}+g$, $\operatorname{tr}E=s+4$, so
$$E^\circ=E-\tfrac{s+4}{4}g=\operatorname{Ric}+g-\tfrac{s+4}{4}g=\operatorname{Ric}-\tfrac s4 g=\operatorname{Ric}^\circ.$$
Hence $R=\tfrac1{8\pi^2}\int|E^\circ|^2\le\tfrac1{8\pi^2}\int|E|^2=Q/(8\pi^2)$, using $|E^\circ|^2\le|E|^2$.

However, the parenthetical derivation in Step A is textually broken: it opens "(the trace-free parts agree because the traces differ by $s+4$…" and never closes the parenthesis, mixes an incorrect intermediate ("$E^\circ = E-(s+4)g/4$" stated alongside "$\operatorname{Ric}^\circ=E-(1+s/4)g$" which are the same object but presented as if in tension), and reads as circular. The end statement $\operatorname{Ric}^\circ=E^\circ$ is correct; the intervening sentence should be rewritten as the two-line computation above. This is expository, not mathematical, but it obscures a step that is otherwise clean.

## (6) Applicability to the evolved terminal metric — sound

The chain invokes only: Chern–Gauss–Bonnet / Hirzebruch (topological, metric-independent), the pointwise identity (18), the SW mixed inequality (3.2) (valid for any smooth metric carrying the monopole class), sign-averaging $p\ge A$ (topological), the LeBrun spectral lower bound (any smooth metric), and $\operatorname{Ric}^\circ=E^\circ$ (algebra). None requires pointwise Ricci pinching. The genuine content of (6) is that Step A replaces the Codex pinching route (eq. 25–26, $R\le\kappa S$ with $\kappa=3\delta^2/(1-\delta)^2$) by the global $L^2$ substitution $R\le Q/(8\pi^2)$, which needs only the terminal defect $Q(T)=\int_{g(T)}|E(T)|^2$ and not any $L^\infty$ pinching on $M$. This is valid. The evolved metric carries the same Ishida–LeBrun classes because the flow preserves the smooth closed topology; correct.

Two dependencies are external to this file and remain the responsibility of the flow analysis, not this derivation: that $Q(T)\lesssim A_i\delta_i^2$ (so $\int G/A_i\to0$) and that the monopole family survives the evolution. This file establishes the metric-level inequality $\int G\le6Q+48\pi^2(-q_{\rm top})_+$; whether $Q(T)$ is actually small is imported from the flow steps (H-DT, H-AO, H-UT are still open per the companion file).

## Coefficient arithmetic $912=864+48$ and $119=1+4+108+6$ — confirmed

- $\int|E|^2=Q$ → coefficient $1$.
- $(s+4)^2=(\operatorname{tr}E)^2\le n|E|^2=4|E|^2$ in $n=4$ → $\int(s+4)^2\le4Q$, coefficient $4$.
- $\int(s+8\sqrt6 u)^2$: integrating (18), $\int t^2=864\pi^2 I-576\pi^2 K$. With $I=T_M+R$, $K\ge p\ge A$, and $864\pi^2 T_M=864\pi^2(2A/3-q_{\rm top})=576\pi^2 A-864\pi^2 q_{\rm top}$, the $576\pi^2 A$ terms cancel, giving $\int t^2\le864\pi^2(R-q_{\rm top})\le108Q+864\pi^2(-q_{\rm top})_+$ (using $864\pi^2 R\le864\pi^2\cdot Q/(8\pi^2)=108Q$, $864/8=108$). Coefficients $108$ and $864$.
- $\int G\le48\pi^2(R-q_{\rm top})\le6Q+48\pi^2(-q_{\rm top})_+$ (since $48/8=6$). Coefficients $6$ and $48$.

Sum: $119=1+4+108+6$ and $912=864+48$. Both correct.

## Summary of what stands and what is imported

Every derivation internal to this file — the pointwise identity (18), (3.3), the two lemmas, the CW/Hirzebruch bookkeeping, Steps A–D, and all coefficient arithmetic through (5.5) — reproduces exactly. No formula error found in the six checks or the two lemmas.

The one substantive matter for the core agent to keep visible: Step C's inequality $\int(b_-)^2\ge32\pi^2 p$ is **not** a consequence of the mixed monopole estimate (3.2) used elsewhere in the chain; it is LeBrun's separate spectral lower bound, entering through eq. (24)'s $D_{\rm mono}\ge0$. The coefficient $32\pi^2=\tfrac49\cdot72\pi^2$ is internally consistent, and the file cites the source, but the strength of the entire $\int G$ estimate is inherited from that imported theorem. If an independent reconstruction of LeBrun's spectral bound is wanted, that is the passage to reproduce line-by-line from `Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory` Thm 2.3 / Prop 2.4; the present file does not rebuild it.

The only expository repair needed is the unclosed, muddled parenthetical in Step A, whose stated result ($\operatorname{Ric}^\circ=E^\circ$, hence $R\le Q/(8\pi^2)$) is correct and can be replaced by the two-line trace computation given above.