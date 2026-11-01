# TTCS Independent Branch Record

```json
{
  "step_id": 7,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step7_positive_branch_four_constructions.md",
    "Sessions/S0910A02/workspace/notes/step1_initial_resolution_and_routes.md",
    "Sessions/S0910A02/workspace/data/step7_det_R_obstruction.json",
    "Sessions/S0910A02/workspace/notes/step6_positive_collapse_regularity_probes.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md",
    "Knowledge/objects/papers/The-Calabi-metric-and-desingularization-of-Einstein-orbifolds--3b9fd6e4b2cd--c8fe6b2cf08c/object.md",
    "Skills/qiushi-yau26/references/research/20260910.tex"
  ]
}
```

## Task

Verify the obstruction-amplitude principle for the positive branch of Yau Problem 26 in dimension 4. The claim: if a sequence (M_i, g_i) of closed oriented smooth 4-manifolds has |Ric_{g_i} - g_i|_{C^0} ≤ δ_i → 0 and is noncollapsed (Vol(B_1) ≥ v > 0), then at any orbifold singularity p of the GH limit, det R|_{Λ²_+}(p) = 0. The argument: (1) the MV Calabi region estimate gives Ric_{g_t} - Λg_t - tλχ_t o = O(t²ρ²) in g_cal-norm, where o is the first obstruction endomorphism; (2) converting to g_t-operator norm, the obstruction tλo has g_t-norm of order 1 (since g_t^{-1} ~ t^{-1} g_cal^{-1}); (3) since o is non-scalar when det R ≠ 0, it cannot be absorbed into a scalar Einstein constant; (4) therefore ||Ric - λg||_{C^0} ≥ c > 0, contradicting δ_i → 0. Check: (a) does this scaling argument apply to positive λ (the MV original is for negative Einstein orbifolds)? (b) is the conversion from g_cal-norm to g_t-norm correct in the core and transition regions? (c) does the non-scalar nature of o genuinely force a C^0 lower bound, or could cancellation between multiple singularities or between the obstruction and higher-order terms eliminate the defect? (d) Ozuch Example 1 on S^4/Z_2 shows L^p-close sequences exist without C^0 convergence when det R ≠ 0 — does this confirm or is it merely consistent with the principle? (e) What are the main gaps between this heuristic principle and a rigorous theorem?

## Output

## Verification memo: the obstruction-amplitude scaling for P₄⁺

### 1. What is actually sound: the scaling identity in the core

The load-bearing computation is correct and worth isolating precisely, because it is the part that survives scrutiny. Work in the core region $r\lesssim 1$ where $g_t = t\,h_t$ exactly, $h_t = g_{\mathrm{cal}}+th$. Since Ricci is scale-invariant as a $(0,2)$-tensor, $\mathrm{Ric}_{g_t}=\mathrm{Ric}_{h_t}$, and MV Lemma 4.1 gives

$$\mathrm{Ric}_{h_t} = t\Lambda h_t + t\lambda\, o + O_{g_{\mathrm{cal}}}(t^2\rho^2).$$

Form the endomorphism $A_{g_t}=g_t^{-1}\mathrm{Ric}_{g_t}=t^{-1}A_{h_t}$:

$$A_{g_t} = \Lambda\,\mathrm{Id} + \lambda\, h_t^{-1}o + t^{-1}h_t^{-1}\!\cdot O_{g_{\mathrm{cal}}}(t^2\rho^2)
= \Lambda\,\mathrm{Id} + \lambda\, h_t^{-1}o + O(t\rho^2).$$

The single nontrivial fact is that $h_t^{-1}o\to g_{\mathrm{cal}}^{-1}o$ has **fixed, $t$-independent, non-scalar** eigenvalues. From $o=\frac{1}{1+r^{2n}}\big(-\overline{g_{FS}}+(n-1)\,d\bar r^{\otimes2}+(n-1)\,\bar\theta^{\otimes2}\big)$ and $g_{\mathrm{cal}}=d\bar r^{\otimes2}+\overline{g_{FS}}+\bar\theta^{\otimes2}$, the endomorphism $g_{\mathrm{cal}}^{-1}o$ has eigenvalues $\tfrac{1}{1+r^{2n}}\big(-1^{(2n-2)},\,(n-1)^{(2)}\big)$, trace zero, and at $r=0$ genuine spread $n$. For the dimension-4 target ($n=2$, Eguchi–Hanson) the eigenvalues at the exceptional divisor are $(-1,-1,+1,+1)$, spread $=2$.

Because an Einstein target uses a **single** constant $\sigma$ over all of $M$, the best-$\sigma$ defect at the core center is

$$\min_\sigma\|A_{g_t}-\sigma\,\mathrm{Id}\| = \tfrac12(\lambda_{\max}-\lambda_{\min}) = \tfrac12|\lambda|\cdot\mathrm{spread} + O(t)\;\ge\; \tfrac12|\lambda|\cdot n .$$

So the sup-norm defect $\delta(g_t)\ge c|\lambda|>0$, uniformly in $t$, **for the explicit MV/Biquard approximate metric $g_t$**. This much is rigorous and is the genuine content. The rest of your questions probe how far it reaches.

### 2. (a) Sign of $\Lambda$, and the model-dimension mismatch

The scaling in §1 uses only the local expansion at a point where $\mathrm{Ric}(g_0)=\Lambda g_0$; nothing in $t^{-1}h_t^{-1}(t\lambda o)=\lambda h_t^{-1}o$ depends on $\mathrm{sign}(\Lambda)$. MV Theorem 1.1 itself is stated for $\Lambda$ of either sign, with the obstruction $n\langle\mathcal R(\omega),\omega\rangle+2(n-2)R\neq0$. So the conversion is sign-independent, and the $\Lambda>0$ instance (e.g. $\langle\mathcal R\omega,\omega\rangle=2R$, obstruction $=4(n-1)R\neq0$ for Kähler–Einstein, Non-example 1.3) is a legitimate use.

The real issue is dimensional: MV's Calabi model and their Prop. 3.5 scalar $\lambda$ are proved for **complex $n\ge3$**, precisely because Lemma 1.1 shows the attaching map has no rotational freedom there. Dimension 4 is $n=2$, the Eguchi–Hanson/Biquard setting, where the gluing carries **two rotational parameters** and the first obstruction is Biquard's $\det \mathbf R|_{\Lambda^2_+}(p)=0$, not MV's Prop. 3.5 formula. Consequently:

- The scalar $\lambda$, the tensor $o$, and the amplitude constant $c$ must be recomputed from the Eguchi–Hanson deformation, not imported from Calabi $n\ge3$.
- However, the rotational parameters act on the *alignment/matching* and higher-order terms, i.e. on the converse (existence) direction and on obstructions beyond the first. The condition $\det\mathbf R|_{\Lambda^2_+}=0$ is a rotation-invariant scalar property of the orbifold curvature (existence of a kernel on $\Lambda^2_+$). No rotation of the bubble creates a kernel that is not already there. So the *necessity* conclusion (order-one defect when $\det\mathbf R\ne0$) is plausibly preserved in dimension 4, while the quantitative amplitude and the existence direction are the parts genuinely altered.

This distinction matters and is only partly reflected in the notes: Step 6/7 correctly flag "redo the EH scaling," but the conclusion "det R = 0 is necessary" should be presented as rotation-stable, whereas the existence half (det R = 0 ⟹ desingularizable) is where the 4d rotational freedom and MV Non-example 1.3's contrast actually live.

### 3. (b) Core versus transition conversion — both regions verified

**Core** ($\rho\lesssim1$): done in §1. Obstruction term $\lambda h_t^{-1}o = O(1)$, remainder $O(t\rho^2)\to0$. Order-one defect. Correct.

**Transition/neck** ($\rho\sim t^{-1/4}$): here $g_t$ is the cutoff combination, and one must use Lemma 4.2, $\mathrm{Ric}_{g_t}-\Lambda g_t - t\lambda\chi_t(\rho)o = O_{g_{\mathrm{cal}}}(t^2\rho^2)$, with $g_t\approx t g_{\mathrm{cal}}$ still leading. Then

$$A_{g_t}-\Lambda\,\mathrm{Id} = g_t^{-1}\big(t\lambda\chi_t o + O(t^2\rho^2)\big)\approx \lambda\chi_t\, g_{\mathrm{cal}}^{-1}o + O(t\rho^2).$$

Now $|o|_{g_{\mathrm{cal}}}\sim\rho^{-2n}=\rho^{-4}$ in dim 4, so at $\rho\sim t^{-1/4}$ the obstruction contribution is $\sim|\lambda|\rho^{-4}\sim|\lambda|t$ and the remainder is $O(t^{1/2})$. Both are small. So the order-one defect is confined to the core, and the neck contributes $o(1)$. The notes' statement that the residual is $O(t)$ in the transition while the obstruction is order one in the core is thus correct, and the $\sup_x$ is realized at the exceptional divisor. This is exactly the concentration structure that makes the next point work.

### 4. (c) Does non-scalar $o$ force a $C^0$ lower bound? Cancellation analysis

**Across singularities: no cancellation is possible.** The defect is $\sup_x\min_\sigma\|A_{g_x}-\sigma\mathrm{Id}\|$, a pointwise supremum. Distinct singularities occupy disjoint core regions, each producing its own order-one endomorphism. The supremum therefore bounds below by the maximum single-singularity amplitude; there is no channel for one core's defect to offset another's. Cancellation between singularities is structurally excluded.

**Against higher-order terms: no cancellation as $t\to0$.** The competing terms in $A_{g_t}$ are $O(t\rho^2)$ in the core, vanishing with $t$, so they cannot annul the $O(1)$ obstruction endomorphism for small $t$. Also, since $\sigma$ must be a single global constant, no pointwise re-centering can absorb the eigenvalue spread. Both potential cancellations are ruled out *for the gluing family*.

The substantive worry that survives is different: it is not cancellation but **applicability**. The order-one bound is derived for metrics that possess the Calabi/EH core expansion. A general $C^0$-pinched $g_i$ need not be (or be close to) such a gluing, in which case its Ricci defect need not "see" the tensor $o$ at all, and $\delta\ge c|\lambda|$ cannot be asserted. This is the true content of the missing step, taken up in (e).

### 5. (d) Ozuch Example 1: consistent and illustrative, not a proof

Ozuch Example 1 on the desingularization of $S^4/\mathbb Z_2$ produces $g_i$ with $\mathrm{Ric}(g_i)\ge 3g_i$ and $\|\mathrm{Ric}(g_i)-3g_i\|_{L^p}\to0$, yet no exact Einstein sequence with the same GH limit. Since $S^4/\mathbb Z_2$ has constant curvature, $\det\mathbf R|_{\Lambda^2_+}=(1/3)^3\neq0$ (and this is rotation-invariant, so the §2 rotational freedom cannot help here).

The relation to the principle is precisely the concentration mechanism of §3: on the core, $g_t\approx t g_{\mathrm{cal}}$, $\mathrm{Vol}_{g_t}(\text{core})\sim t^{2}$ in real dimension 4, while $|\mathrm{Ric}-3g_t|_{C^0}\sim c$. Hence

$$\|\mathrm{Ric}-3g_t\|_{L^p}^p \sim c^p\, t^{2}\to0,\qquad \|\mathrm{Ric}-3g_t\|_{C^0}\sim c\not\to0.$$

So Ozuch's $L^p$ smallness is exactly what the principle predicts must coexist with an order-one $C^0$ defect. This makes Example 1 **consistent with and strongly illustrative of** the principle, and it independently confirms the exact-Einstein obstruction. It does **not** confirm the $C^0$ statement itself: Ozuch never asserts $C^0\to0$, and the impossibility of some cleverer $C^0$-small construction is a separate matter the example does not settle. In short: same phenomenon, one direction (exact-Einstein nonexistence) proved by Ozuch, the other ($C^0$ lower bound) predicted by the scaling but not established by the example.

A decisive cheap computation is available and would move this from "consistent" toward "verified in the target case": for the explicit $S^4/\mathbb Z_2 \,\#\,$Eguchi–Hanson naive gluing $g_t$, compute $\mathrm{Ric}_{g_t}$ in the core and evaluate $\sup_x\min_\sigma\|g_t^{-1}\mathrm{Ric}_{g_t}-\sigma\mathrm{Id}\|_{op}$ as a function of $t$, checking convergence to $\tfrac12|\lambda|\cdot\mathrm{spread}$ rather than $0$; alongside $\|\mathrm{Ric}-3g_t\|_{L^2}\to0$. This uses the correct dimension and sign (unlike the Calabi $n\ge3$ input), directly tests the rigorous kernel, and numerically exhibits the $L^p$/$C^0$ separation.

### 6. (e) What separates the heuristic from a theorem

The rigorous kernel is: *for the explicit MV/Biquard approximate metrics $g_t$, $\det\mathbf R\ne0 \Rightarrow \delta(g_t)\ge c>0$.* Turning this into "every noncollapsed $C^0$-pinched sequence with an orbifold GH limit forces $\det\mathbf R=0$" requires several distinct pieces that are not yet in hand.

1. **Structural theorem for pinched (not exact) sequences.** The order-one bound needs $g_i$ to be close, in the weighted norms, to a gluing of models. Ozuch Theorem 0.2 supplies exactly this — but only for **exact** Einstein metrics ($\mathrm{Ric}=\Lambda g$, $|\mathrm{Ric}|\le3$). There is no analogue known for $C^0$-pinched metrics. Without it, the principle constrains only sequences already of gluing type.

2. **Regularity of the limit and the bubble models.** To even define $\det\mathbf R(p)$ one needs the GH limit to be a smooth Einstein orbifold off a finite set, with Ricci-flat ALE blow-ups. The bubbling analysis (Bando, BKN, Cheeger–Naber $\varepsilon$-regularity) uses the exact Einstein equation, and the harmonic-radius-to-curvature upgrade needs $\nabla\mathrm{Ric}$ or Einstein. As Step 6 correctly stresses, $C^0$ pinching gives $\mathrm{Ric}=g+E$, $\|E\|_{op}\le\delta$, with no control on $\nabla\mathrm{Ric}$ and no Weyl equation. So under $C^0$ pinching alone the limit is a priori a metric/RCD space, and the singularity models are not established.

3. **Model dimension recomputation.** As in (a), the dimension-4 amplitude and deformation tensor must come from Eguchi–Hanson, not Calabi $n\ge3$.

4. **Uniformity of $|\lambda|$.** If the limit orbifold varies along the sequence, one needs a uniform lower bound on $|\lambda|$ (equivalently a quantitative $\det\mathbf R$ bound) over the compact family of possible limits.

5. **The converse (existence) is a separate theorem.** Even granting $\det\mathbf R=0$, producing an Einstein metric on $M_i$ needs Biquard/Ozuch desingularization with nondegeneracy and vanishing higher obstructions (Ozuch 2020, 2021), plus matching of the diffeomorphism type. The obstruction-amplitude principle is intrinsically a nonexistence instrument; it does not by itself yield Einstein metrics, so Construction 3's use of it to *close* the positive branch imports this entire existence apparatus as an additional hypothesis.

A fair summary: the scaling argument is internally correct, sign-independent, correctly localized to the core, and immune to the two cancellation mechanisms — as a statement about the constructed gluing family. Its extension to arbitrary pinched sequences rests on structural and regularity inputs currently available only under the exact Einstein equation. The single sharpest unresolved point is item 1–2: whether $C^0$ Ricci pinching (without $\nabla\mathrm{Ric}$ or an elliptic equation for the metric) forces proximity to an exact-Einstein gluing at all. Until that is established, the principle rigorously governs the MV/Biquard approximate metrics and remains a well-supported prediction, illustrated by Ozuch Example 1 through volume concentration, for general pinched sequences.

### 7. Two grounded checks that would change judgment

- The dimension-4 core computation of §5/§6 above ($S^4/\mathbb Z_2\,\#\,$Eguchi–Hanson): directly verifies or refutes the rigorous kernel in the actual target setting and produces the $L^p$/$C^0$ separation numerically, at low cost.
- A precise statement, with Eguchi–Hanson input, of how the two 4d rotational parameters act: confirming that they leave $\det\mathbf R|_{\Lambda^2_+}=0$ invariant (necessity direction stable) while affecting only the second-order matching (existence direction). This would settle whether the MV $n\ge3$ rigidity transfers, and would sharpen the boundary between the necessity result and the existence result inside Construction 3.