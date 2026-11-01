# TTCS Independent Branch Record

```json
{
  "step_id": 74,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step74_ell_classification_tower_impossibility_and_hardness_propagation.md",
    "Sessions/S0910A02/workspace/data/step74_product_propagation.json",
    "Sessions/S0910A02/workspace/plans/step73_general_higher_flux_necessity_plan.md",
    "Sessions/S0910A02/workspace/notes/step73_global_positive_proof_allocation.md",
    "Sessions/S0910A02/trace/ttcs/results/step73_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Verify three structural results that reshape the noncollapsed P₄⁺ proof architecture for Yau Problem 26.

1. ELL-CLASSIFICATION: The claim is that among homogeneous degree-ℓ TT/radial-null modes on a cone R^d/Gamma (d≥4), the unweighted nuclear-norm mass integral ∫r^{1-ℓ}dr gives H₂=log(R/b) for ℓ=2 (logarithmic) and H_ℓ=b^{2-ℓ}/(ℓ-2)→∞ power-scale for ℓ>2. Check the radial integral, the resulting lower bound on operator-norm defect, and the conclusion that ℓ=2 is the unique unweighted log-critical mode.

2. STRUCTURAL IMPOSSIBILITY: The argument combines two inputs: (a) Ozuch's scaling hierarchy showing the k-th Biquard obstruction creates O(t^k) error in the (0,2)-form on the ALE core, hence O(t^{k-1}) in operator norm after raising index; and (b) the near-pinched construction FND:A1construction with dominant error O(1/|log a|). Since t~a^2 and O(a^{2(k-1)}) << O(1/|log a|) for k≥2, the claim is that no C⁰ Ricci-endomorphism pinching theorem can force higher obstructions to vanish. Check whether this argument is valid, whether there is a logical gap or hidden assumption, and whether any additional sequence-level mechanism could circumvent it.

3. PRODUCT PROPAGATION: If (O⁴,g_O) is a positive Einstein 4-orbifold with Ric=σg and isolated A₁ points, and M⁴ carries near-pinched metrics g_a with δ(g_a)≤C/|log a|, then for n≥6, the product M⁴×S^{n-4}(Ric=σg) has δ(product)=δ(g_a) because Ric is block-diagonal on a product. Check the product Ricci formula, the operator-norm equality, and the gap at n=5 (S¹ has Ric=0, incompatible with σ>0).

## Output

# Verification Memo: Three Structural Results for the Noncollapsed P₄⁺ Architecture

Session S0910A02, Step 74. I checked the three results against the differential geometry, the cited flux identity, the Ozuch scaling reading, and the earlier TTCS integration. Two results (ℓ-classification, product Ricci block structure) are mathematically correct as stated. The third (product propagation) has a correct geometric core but carries two higher-level assertions about dimensional reduction that do not follow from the construction and should be restated. Details below.

---

## Part 1 — ℓ-mode classification: correct

**Radial integral.** With Cartesian-component homogeneity $K_\ell(rx)=r^\ell K_\ell(x)$, the pointwise Euclidean norm satisfies $|K_\ell|(r,\theta)=r^\ell|K_\ell|(1,\theta)$, so the dual $o_\ell=r^{-(d+2\ell-2)}K_\ell$ has $\|o_\ell\|_*(r,\theta)=r^{-(d+\ell-2)}\|K_\ell\|_{*}(1,\theta)$. With $dV=r^{d-1}dr\,d\theta$,
$$
\int_A\|o_\ell\|_*\,dV=J_{K_\ell}\int_b^R r^{-(d+\ell-2)+(d-1)}\,dr=J_{K_\ell}\int_b^R r^{1-\ell}\,dr .
$$
The exponent reduces correctly to $1-\ell$. Then $\int_b^R r^{1-\ell}dr=\log(R/b)$ at $\ell=2$ and $\dfrac{b^{2-\ell}-R^{2-\ell}}{\ell-2}$ otherwise, so $H_2=L$ and $H_\ell\sim b^{2-\ell}/(\ell-2)\to\infty$ as $b\to0$ for $\ell>2$. The table is right.

**Lower bound.** The Hilbert–Schmidt pairing bound $\big|\int_A\langle D\mathrm{Ric}_e u,o_\ell\rangle\big|\le \|D\mathrm{Ric}_e u\|_{op,\infty}\int_A\|o_\ell\|_*\,dV$ combined with the flux value $-\tfrac{d+2\ell-2}{2}I_{K_\ell}$ gives exactly
$$
\|D\mathrm{Ric}_e u\|_{op,\infty}\ge \frac{(d+2\ell-2)I_{K_\ell}}{2J_{K_\ell}H_\ell(b,R)} .
$$
So $\ell=2$ gives the inverse-log bound $\sim c/L$; $\ell>2$ gives $\sim b^{\ell-2}\to0$. The direct test tensor $u_b=\chi(r/b)K_\ell$ with $\|D\mathrm{Ric}_e u_b\|_\infty=O(b^{\ell-2})$ confirms the power-scale, matching the TTCS integration that already rejected the earlier uniform $c/L$ statement. The conclusion "$\ell=2$ is the unique unweighted log-critical mode" holds within this homogeneous-mode setting.

**Three points to keep attached to the statement so it is not read more broadly than proved:**
1. This is a classification of *pure homogeneous integer modes*. Resonant components of type $r^\ell\log r$, if present in a real obstruction expansion, change the boundary flux ($\partial_r(r^\ell\log r)=r^{\ell-1}(\ell\log r+1)$) and are not covered by the clean Wronskian.
2. Even the critical $\ell=2$ bound is only $\delta\gtrsim 1/L$, which is compatible with $\delta\to0$ when $L\to\infty$. Entering the exponential-neck argument requires the additional sequence input $\delta_i L_i\to0$ or bounded-annulus control; the flux identity alone does not supply it. The note's own wording is consistent with this.
3. The bound controls the *linear model* $D\mathrm{Ric}_e$. Application to the nonlinear Ricci-endomorphism norm still needs the nonlinear and endpoint remainders that the Step-73 plan lists.

None of these contradict Part 1; they are the correct reading.

---

## Part 2 — Structural impossibility: valid, with one load-bearing input and one heuristic input

**Arithmetic.** With first-obstruction magnitude $O(t)$ in the (0,2)-form measured in $g_{\mathrm{ALE}}$ and $g_t\sim t\,g_{\mathrm{ALE}}$, the endomorphism $g_t^{-1}E$ scales by $t^{-1}$, giving $O(t^{k-1})$ operator-norm defect for the $k$-th obstruction; $k=1\Rightarrow O(1)$ (the order-one detectability principle), $k\ge2\Rightarrow O(t^{k-1})\le O(t)$. With $t\sim a^{\,p}$ ($p>0$) and dominant near-pinched defect $O(1/|\log a|)$, the comparison $a^{\,p(k-1)}|\log a|\to0$ for $k\ge2$ is correct: a positive power beats the logarithm. So the higher-obstruction contribution sits strictly below the log-Weyl term, and $\delta\to0$ is achievable with a nonvanishing $k\ge2$ obstruction. The impossibility of forcing higher-obstruction vanishing from $\delta\to0$ alone follows. This is internally coherent and the arithmetic is robust to the exact power $p$ relating $t$ and $a$ — a genuine strength, since the conclusion does not hinge on the precise gluing scale.

**Two arguments are not equally firm.** Argument B (Ozuch amplitude scaling) is the load-bearing one and does not need any identification between homogeneity degree $\ell$ and obstruction order $k$: it reads the $O(t^k)$ scaling directly from Ozuch's tower. Argument A (flux scaling from Part 1) implicitly assumes that higher Biquard obstructions manifest as $\ell>2$ homogeneous flux modes. That degree↔order identification is exactly the mode-identification statement flagged as unestablished in the TTCS integration (item 5 there: obstruction order, ALE Jacobi decay order, and cone-mode degree are not automatically equal). So Argument A is heuristic pending that identification, while Argument B stands on its own. The structural conclusion should be presented as resting on B, with A as corroboration.

**Dependencies that carry the result and are assumed rather than reproduced here:**
- The reading of Ozuch (arXiv:2012.13316, lines 142–147) that the $k$-th obstruction produces $O(t^k)$ in the (0,2)-form. The whole impossibility turns on this power; the index-raising convention ($t^{-1}$ per raised index, so first obstruction $O(t)\to O(1)$) should be pinned to Ozuch's own normalization to be sure the exponent is $t^k$ and not $t^{k}$ in a differently scaled norm. The internal consistency check (first obstruction $O(1)$) is satisfied, which is reassuring but not a substitute for the source normalization.
- FND:A1construction producing $\delta(g_a)\le C/|\log a|$ *for insertion directions carrying a nonvanishing higher obstruction*, i.e. across all chirality/insertion patterns. This uses the Step-68 reflection $c(z,w)=(\bar z,w)$ to assert pattern-independence of the near-pinched construction. That reflection argument is cited, not reproduced; it is the second essential input for the witness family to exist.

**On whether a sequence-level mechanism can circumvent.** The impossibility is precisely a statement that no argument deriving higher-obstruction vanishing *purely from smallness of $\delta$* can succeed, because an explicit witness family exists. It does not block the two other logical shapes:
- Route A (tower rigidity) derives higher-obstruction vanishing from the *algebraic first-obstruction condition* $R^\pm\zeta=0$ on the orbifold, not from $\delta$. This is a different implication and is not touched by the impossibility.
- Route B (global existence) bypasses the desingularization tower entirely.

So "no additional sequence-level mechanism circumvents it" is correct only for mechanisms whose sole input is $\delta\to0$; it is not a statement that P₄⁺ is undecidable. The note frames this correctly. One further point worth making explicit: the witness family lives on the fixed resolution $M^4$, and its existence with $\delta\to0$ says nothing about whether $M^4$ carries a *far* Einstein metric — the impossibility rules out the *local desingularization* route, not existence itself. The note's §4(B) says this; it is the correct reading and should be preserved verbatim in any downstream use.

---

## Part 3 — Product propagation: geometry correct; two dimensional-reduction assertions overstated

**Product Ricci and operator-norm max — correct.** For any Riemannian product the mixed Christoffel symbols vanish, so $\mathrm{Ric}_{g_1\times g_2}=\mathrm{Ric}_{g_1}\oplus\mathrm{Ric}_{g_2}$ regardless of whether either factor is Einstein. The endomorphism $g^{-1}(\mathrm{Ric}-\sigma g)=\big(g_1^{-1}E_1\big)\oplus\big(g_2^{-1}E_2\big)$ is block-diagonal and symmetric, so its operator norm is $\max(\|g_1^{-1}E_1\|,\|g_2^{-1}E_2\|)$. With $\mathrm{Ric}_{g_N}=\sigma g_N$ exactly, $E_2=0$ and $\delta_\sigma(\text{product})=\delta_\sigma(g_a)$. The proof is right. (Minor notational point: the displayed equation writes $\|\mathrm{Ric}-\sigma g\|_{op}$ for what is the $g$-induced endomorphism norm $\|g^{-1}\mathrm{Ric}-\sigma I\|_{op}$; these agree, so no numerical consequence.)

**Scaling — correct.** For $S^{m}$, $m=n-4$, the (0,2) Ricci is scale-invariant, $\mathrm{Ric}_{g_N}=(m-1)g_{\mathrm{unit}}$; requiring $\mathrm{Ric}_{g_N}=\sigma g_N$ forces $g_N=\frac{m-1}{\sigma}g_{\mathrm{unit}}=\frac{n-5}{\sigma}g_{\mathrm{round}}$. The JSON entries $c=1/\sigma$ ($n=6$), $2/\sigma$ ($n=7$), $3/\sigma$ ($n=8$) all equal $(m-1)/\sigma$. Correct.

**n=5 — correct.** $S^1$ is flat, $E_2=\mathrm{Ric}_{g_N}-\sigma g_N=-\sigma g_N\neq0$, block norm $\sigma$, so $\delta(\text{product})=\max(\delta(g_a),\sigma)=\sigma$. The construction does not extend to $n=5$, and no 1-manifold is positively Einstein. Correct.

**The two assertions that must be restated.** The note (and the JSON `transfer_theorem`) states "a resolution of $P_4^+$ automatically resolves $P_n^+$ for all $n\ge6$" and "an all-dimensional proof of $P_n^+$ cannot avoid the four-dimensional crux," with "dimension four is genuinely the bottleneck." These do not follow from the construction, for two independent reasons:

1. **Quantifier mismatch.** $P_n^+$ ranges over *all* closed $n$-manifolds with tight positive pinching, whereas the product construction only produces the special manifolds $M^4\times S^{n-4}$. Proving $P_4^+$ yields Einstein metrics on $M^4$, hence product Einstein metrics on those specific products — but says nothing about the many pinched $n$-manifolds that are not such products. So $P_4^+\Rightarrow P_n^+$ is not established.

2. **Einstein metrics on products need not be products.** Product manifolds routinely carry Einstein metrics that are not Riemannian products. Hence proving $P_n^+$ could produce a non-product Einstein metric on $M^4\times S^{n-4}$ without ever yielding a 4-dimensional Einstein metric on $M^4$. So "$P_n^+$ cannot avoid the 4D crux" also does not follow: a higher-dimensional existence argument could resolve the product instance without resolving the 4D factor.

**What is rigorously true and should replace those assertions:**
- The product metric $g_a\times g_N$ is a genuine near-pinched family on the closed connected smooth $n$-manifold $M^4\times S^{n-4}$ with $\delta=\delta(g_a)\to0$ (fully proven). Two-sided pinching around $\sigma>0$ holds: all eigenvalues lie in $[\sigma-\delta,\sigma+\delta]$.
- Therefore near-pinched families with $\delta\to0$ exist in every $n\ge6$, generated from 4-dimensional data; the analytic difficulty of "producing an Einstein metric from near-pinched input" is present in all $n\ge6$ as an inherited phenomenon.
- If $P_4^+$ produces an Einstein metric on $M^4$ with constant $\sigma$, then the product with $g_N$ is Einstein — so 4D existence transfers to existence on those *specific* product manifolds (not to the universal $P_n^+$).

The word "bottleneck/reduction" should be reserved for this product-family statement, not for the universal dimensional quantifier. The propagation is a real embedding of 4D near-pinched input into higher dimensions; it is not a logical equivalence of the dimension-$n$ existence problems.

---

## Summary of what is verified and what needs restating

- **Part 1:** radial integral, operator-norm lower bound, and $\ell=2$ uniqueness are correct. Keep the homogeneous-mode setting, the resonant-log exclusion, and the fact that even $\ell=2$ gives only $\delta\gtrsim1/L$ attached to the statement.
- **Part 2:** arithmetic and the impossibility of forcing higher obstructions from $\delta\to0$ alone are correct. Rest the conclusion on Argument B (Ozuch amplitude); treat Argument A as corroboration pending the degree↔order mode-identification. Confirm the Ozuch $O(t^k)$ exponent against the source normalization, and note the dependence on FND:A1construction achieving $1/|\log a|$ for all insertion directions via the Step-68 reflection. Routes A and B are different implications, not circumventions.
- **Part 3:** all differential geometry (block-diagonal Ricci, operator-norm max, scaling $c=(m-1)/\sigma$, $n=5$ gap) is correct. The "resolution of $P_4^+$ resolves $P_n^+$" and "$P_n^+$ cannot avoid the 4D crux" assertions do not follow — because $P_n^+$ quantifies over all manifolds and Einstein metrics on products need not be products. Restate as an inherited near-pinched family on the specific product manifolds and as transfer of 4D existence to those products.

Unresolved and needed for the mixed-row program to become more than a reduction: the finite second-obstruction computation on $(S^2\times S^2)/\mathbb Z_2$ (does the $O(t^2)$ obstruction vanish for all $\zeta\in\ker R^\pm$), which is what decides whether tower rigidity (Route A) holds in the product geometry or the mixed rows become the sharpest local-desingularization-blocked candidates. That computation, not the three structural results, is where the next decisive information lies.