# TTCS Independent Branch Record

```json
{
  "step_id": 47,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/plans/route_assessment_step47_entropy_degree_theorem.md",
    "Sessions/S0910A01/workspace/scripts/step47_entropy_degree_comparison.py",
    "Knowledge/objects/papers/Differentiable-rigidity-under-Ricci-curvature-lower-bound--cfb4c9cdd3c7--65a5a48bd00c/object.md",
    "Sessions/S0910A01/staging/acquired/Extended_graph_4-manifolds__and_Einstein_metrics_36ca3f274012faba/content.md"
  ]
}
```

## Task

Verify the mathematical substance of the Step 47 entropy/degree-map note for Yau Problem 26. Check the Chern--Gauss--Bonnet derivation from ||Ric+g||_op<=delta, the scaling g'=(1+delta)g/3, the boxed degree comparison, the degree-one hyperbolic existence theorem using the actual Bessieres--Besson--Courtois--Gallot theorem, and the X#X threshold asymptotic delta~1/(4 chi(X)). Identify any hidden orientation, sign, quantifier, or theorem-statement issue. Also assess the extended-graph near-equality interpretation and the claim that the argument is target-dependent rather than dimension-uniform. Give exact mathematical corrections, not generic review prose.

## Output

# Verification memo: Step 47 entropy / degree-map note

I reproduced every displayed computation. The core derivations are correct. Below I give the line-by-line confirmations, the small refinements they invite, and the structural points (extra hypothesis, theorem-dependency, one genuinely dimension-uniform sub-result) that sharpen how the note should be read.

## 1. The Chern–Gauss–Bonnet pinching chain is correct

Starting from $\|g^{-1}(\operatorname{Ric}_g+g)\|_{\infty,\mathrm{op}}\le\delta$, the $g$-self-adjoint endomorphism $g^{-1}\operatorname{Ric}_g$ has eigenvalues in $[-1-\delta,-1+\delta]$, i.e. $-1+e_i$ with $|e_i|\le\delta$. This is exactly the Ricci pinching $(-1-\delta)g\le\operatorname{Ric}_g\le(-1+\delta)g$, the $\operatorname{Ric}\approx -g$ regime. Each step checks:

- $s_g=-4+\sum e_i\in[-4-4\delta,-4+4\delta]$, so $s_g<0$ and $s_g^2\ge 16(1-\delta)^2$. Correct.
- Trace-free Ricci eigenvalues $e_i-\tfrac14\sum_j e_j$; then $|\operatorname{Ric}^\circ|^2=\sum_i(e_i-\bar e)^2=\sum e_i^2-4\bar e^2\le\sum e_i^2\le 4\delta^2$ (variance decomposition with $n=4$). Correct.
- $\dfrac{s_g^2}{24}-\dfrac{|\operatorname{Ric}^\circ|^2}{2}\ge\dfrac{16(1-\delta)^2}{24}-2\delta^2=\dfrac23(1-\delta)^2-2\delta^2$. The algebraic identity $\dfrac23(1-\delta)^2-2\delta^2=\dfrac23(1-2\delta-2\delta^2)$ is exact.
- Positivity threshold: $2\delta^2+2\delta-1=0$ gives $\delta=\tfrac{\sqrt3-1}{2}\approx0.366$. Matches the stated interval.
- Dropping $|W|^2\ge0$ in $8\pi^2\chi(Y)=\int(|W|^2+\tfrac{s^2}{24}-\tfrac{|\operatorname{Ric}^\circ|^2}{2})$ yields $\operatorname{Vol}_g(Y)\le\dfrac{12\pi^2\chi(Y)}{1-2\delta-2\delta^2}$. Correct.

The Gauss–Bonnet–Chern integrand used matches Di Cerbo's convention (here $|W|^2=|W^+|^2+|W^-|^2$, and "Ric" in his formula is already the trace-free part). Note the volume bound does **not** need orientation — the Pfaffian Gauss–Bonnet holds for any closed 4-manifold; orientation enters only through the degree maps, which are correctly restricted to oriented $Y,X$.

## 2. The scaling $g'=\tfrac{1+\delta}{3}g$ is correct

$\operatorname{Ric}$ as a $(0,2)$ tensor is invariant under constant rescaling (Levi-Civita connection unchanged), so $\operatorname{Ric}_{g'}=\operatorname{Ric}_g\ge(-1-\delta)g=-3g'$ since $g=\tfrac{3}{1+\delta}g'$. Volume scales by $\lambda^2=((1+\delta)/3)^2$ in dimension 4. The resulting
$$\operatorname{Vol}_{g'}(Y)\le\frac{4\pi^2}{3}\chi(Y)\,\frac{(1+\delta)^2}{1-2\delta-2\delta^2}$$
and the hyperbolic normalization $\operatorname{Vol}_{g_0}(X)=\tfrac{4\pi^2}{3}\chi(X)$ (from $\chi=\tfrac{1}{8\pi^2}\int\tfrac{144}{24}=\tfrac{3}{4\pi^2}\operatorname{Vol}$) are both correct, so boxed inequality (1) holds. $F(\delta)=1+4\delta+O(\delta^2)$ is correct (the quadratic term is $+11\delta^2$).

## 3. The degree-one existence statement is valid, with one hypothesis worth naming explicitly

The note applies BBCG Theorem 1.3 ($n=4$, $n-1=3$) in the correct direction: existence of a metric with $\operatorname{Ric}_{g'}\ge-3g'$ and $\operatorname{vol}_{g'}(Y)\le(1+\varepsilon(4,D))\operatorname{vol}_{g_0}(X)$ forces $f$ homotopic to a diffeomorphism, hence $Y\cong X$ and $Y$ carries the pulled-back hyperbolic Einstein metric. Combining with the CGB upper bound under $\chi(Y)\le\chi(X)$ gives $\operatorname{vol}_{g'}(Y)\le F(\delta)\operatorname{vol}_{g_0}(X)$, so $F(\delta)\le1+\varepsilon(4,D)$ suffices. All correct.

Point to make explicit: **$\chi(Y)\le\chi(X)$ is a genuine extra assumption**, not implied by domination. A degree-one map gives $\|Y\|\ge\|X\|$ and $\operatorname{vol}_{g'}(Y)\ge\operatorname{vol}_{g_0}(X)$ (Gromov isolation + BCG), but no ordering of Euler characteristics. In the diffeomorphism conclusion one necessarily has $\chi(Y)=\chi(X)$; therefore the two sub-cases are: strict $\chi(Y)<\chi(X)$ combined with the exact BCG lower bound $\operatorname{vol}_{g'}(Y)\ge\operatorname{vol}_{g_0}(X)$ (Theorem 1.1) excludes tight pinching once $\tfrac{\chi(Y)}{\chi(X)}F(\delta)<1$; equality $\chi(Y)=\chi(X)$ admits the diffeomorphism route. Both are handled consistently. The "existence" content is a rigidity implication — it certifies that a tightly $(-g)$-pinched dominating $Y$ was already the hyperbolic $X$; it does not manufacture Einstein metrics on new manifolds. The note states this plainly.

The essential quantifier is correct and correctly flagged: $\varepsilon(4,D)$ depends on $\operatorname{diam}(X)$, so the admissible $\delta$ is target-dependent. BBCG's own text (the $Y=X\#\Sigma$ Farrell–Jones discussion) proves this dependence is unavoidable: large-degree covers with sectional curvature pinched near $-1$ would otherwise contradict a diameter-free $\varepsilon$. This is exactly why the mechanism cannot yield the dimension-only constants Yau 26 demands.

## 4. The $X\#X$ threshold is correct, and rests only on the proved volume inequality

$\chi(X\#X)=2\chi(X)-2$ (dim 4, $\chi(S^4)=2$), so $\tfrac{\chi(Y)}{2\chi(X)}=1-\tfrac1{\chi(X)}$. There is a degree-2 map $X\#X\to X$ (pinch to $X\vee X$, fold by identity on each compatibly oriented summand; local degrees $1+1$), so BBCG **Theorem 1.5** — the pure volume inequality $\operatorname{vol}_{g'}(Y)\ge2\operatorname{vol}_{g_0}(X)$ under $\operatorname{Ric}_{g'}\ge-3g'$ — applies. Combined with the CGB upper bound, contradiction when $(1-\tfrac1{\chi(X)})F(\delta)<1$, and solving $F(\delta)=\tfrac{\chi}{\chi-1}=1+\tfrac1{\chi-1}$ against $F\approx1+4\delta$ gives $\delta_{\max}(X)\sim\tfrac{1}{4\chi(X)}$ and $4\chi\delta\to1$. Verified numerically for $\chi=10^4$ ($\delta\approx2.5\times10^{-5}$, $4\chi\delta\to1$).

Worth recording: this fixed-target gap uses **only Theorem 1.5**, which is fully proved in Besson–Courtois–Gallot [5]; it does **not** depend on Theorem 1.6. By contrast, BBCG Corollary 1.7 (the strengthened $\operatorname{vol}(X\#X,g)\ge2(1+\varepsilon(X))\operatorname{vol}(X)$) is stated as a consequence of Theorem 1.6, whose proof BBCG omit ("we shall omit this proof … and leave it to the reader," referring to Bessières [1]). So when the note calls Corollary 1.7 "the stronger fixed-target statement," that strengthening carries the same unproved-in-this-paper dependency as the degree-$k$ rigidity in the note's Section 3. The degree-one theorem and the elementary $X\#X$ threshold are on solid, fully-referenced footing; the degree-$k$ existence statement and Corollary 1.7 share the Theorem 1.6 dependency, which the note already isolates as a "next theorem after reading Bessières." That reading of the source is accurate.

## 5. Extended-graph near-equality reading is correct

For extended graph 4-manifolds with $k\ge1$ pure real-hyperbolic pieces, Di Cerbo gives $\operatorname{Vol}_{Ric}(M)=\sum_i\operatorname{Vol}_{-1}(V_i)$ (Lemma 9), $\tau(M)=0$, $\chi(M)>0$, and $2\chi(M)=\tfrac{3}{2\pi^2}\operatorname{Vol}_{Ric}(M)$. From the last relation, $\tfrac{4\pi^2}{3}\chi(M)=\operatorname{Vol}_{Ric}(M)$, so the CGB upper bound reads $\operatorname{Vol}_{g'}(M)\le\operatorname{Vol}_{Ric}(M)F(\delta)$, while $\operatorname{Vol}_{g'}(M)\ge\operatorname{Vol}_{Ric}(M)$ by definition of the infimum (since $\operatorname{Ric}_{g'}\ge-3g'$). The residual width $F(\delta)-1\approx4\delta$ is real, and the exact-equality argument (equality $\Rightarrow$ half-conformally-flat $\Rightarrow$ hyperbolic, then the $\mathbb Z^3$ subgroup contradicts Preissmann) does not carry to the approximate regime without a near-equality rigidity theorem for $\operatorname{Vol}_{Ric}$ or the entropy inequality. The note's assessment is exactly right; the missing analytic input is a stability version of Lemma 7's equality case.

## 6. A genuinely dimension-uniform sub-result hiding in §1 and §5

The pointwise CGB lower bound gives more than the note extracts, and this piece is target-**independent**. Since
$$8\pi^2\chi(Y)\ge\tfrac23(1-2\delta-2\delta^2)\operatorname{Vol}_{g'}(Y)>0\quad(\delta<\tfrac{\sqrt3-1}{2}),$$
**any** closed 4-manifold carrying a metric with $\operatorname{Ric}$ pinched in $[-1-\delta,-1+\delta]\,g$ for $\delta<\tfrac{\sqrt3-1}{2}$ must have $\chi>0$. Equivalently, every closed 4-manifold with $\chi\le0$ admits no such tightly-$(-g)$-pinched Ricci metric — a clean, dimension-4, target-free statement (the approximate-Einstein analog of the classical $\chi\ge0$ Einstein fact). This is the one part of the note that does not degenerate with target size. It applies directly to the no-pure-piece extended graph case ($\chi=\tau=0$) as the note observes, but it deserves to be stated as a standalone regime result rather than only as a remark. It concerns solely the $\operatorname{Ric}\approx-g$ window, so it is not itself a Yau-26 exclusion (those $\chi\le0$ manifolds may still admit Ricci-flat or positive Einstein metrics); it should be phrased as "no metric in this pinching window," not "no Einstein metric."

## 7. Items I could not verify from the supplied files

The Farrell–Jones / Kasilingam route (§6): the assertion of real dimensions 14, 16 manifolds homeomorphic-but-not-diffeomorphic to complex-hyperbolic quotients with sectional curvature in $[-4-\varepsilon,-1+\varepsilon]$ is present only as a metadata reference, not full text, in the provided material. The note's own statement — that the decisive missing input is a no-Einstein theorem for the exotic members in dimension $\ge5$, and that neither the retrieved sources nor Di Cerbo (who states the $n\ge5$ graph-Einstein question is open) supply it — is consistent with what is in front of me. The high value of this route rests on that unproved exclusion; the note does not assert it.

## Summary of exact corrections

- No computational errors. Every displayed equation, the $\tfrac{\sqrt3-1}{2}$ threshold, the $F(\delta)=1+4\delta+O(\delta^2)$ expansion, and the $\delta_{\max}\sim\tfrac1{4\chi}$ asymptotic reproduce correctly, including the script's $F(\delta)\le1+8\delta$ bound on $[0,0.05]$ ($F(0.05)=1.2318$).
- Name $\chi(Y)\le\chi(X)$ as an explicit restricting hypothesis in the degree-one theorem; equality is forced in the diffeomorphism conclusion.
- Distinguish dependencies: the degree-one theorem and the $X\#X$ threshold use only proved results (Theorems 1.1, 1.3, 1.5); the degree-$k$ statement and Corollary 1.7 both inherit the unproved-in-BBCG Theorem 1.6. Corollary 1.7 should not be presented as more established than the elementary threshold.
- Confirm the degree-2 map $X\#X\to X$ and its orientation-compatible construction; the factor-2 lower bound is legitimate.
- Elevate the $\chi\le0\Rightarrow$ no tight $(-g)$-pinching statement to a standalone dimension-uniform result within the pinching window, explicitly not a Yau-26 exclusion.
- The overall reading — target-dependent rather than dimension-uniform for the hyperbolic-comparison mechanism — is correct and is exactly what BBCG's Farrell–Jones argument forces.