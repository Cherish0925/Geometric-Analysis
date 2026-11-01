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

# Scientific verification memo

## 1. Homogeneous-mode classification

Let
\[
K_\ell(r\theta)=r^\ell Y_\ell(\theta),\qquad
o_\ell=r^{-(d+2\ell-2)}K_\ell
      =r^{-(d+\ell-2)}Y_\ell(\theta).
\]
Thus, with norms taken in the Euclidean metric,
\[
\|o_\ell(r,\theta)\|_*
=r^{-(d+\ell-2)}\|Y_\ell(\theta)\|_*.
\]
Since \(dV=r^{d-1}dr\,d\theta\),
\[
\int_A\|o_\ell\|_*\,dV
=J_{K_\ell}\int_b^R r^{1-\ell}\,dr,
\]
where
\[
J_{K_\ell}
=\int_{S^{d-1}/\Gamma}\|K_\ell\|_{*,r=1}\,d\theta.
\]
The radial integral is exactly
\[
H_\ell(b,R)=
\begin{cases}
\log(R/b),&\ell=2,\\[1mm]
\dfrac{b^{2-\ell}-R^{2-\ell}}{\ell-2},&\ell>2.
\end{cases}
\]

The supplied Wronskian computation is also correct. With the convention
\[
D\operatorname{Ric}_e u=-\frac12\Delta u+\text{gauge terms},
\]
the trace-free, divergence-free, and radial-null properties of \(o_\ell\) remove the gauge pairing. On the outer sphere,
\[
\partial_rK_\ell=\frac{\ell}{r}K_\ell,\qquad
\partial_ro_\ell=-\frac{d+\ell-2}{r}o_\ell,
\]
so Green’s identity gives
\[
\int_A\langle D\operatorname{Ric}_e u,o_\ell\rangle
=-\frac{d+2\ell-2}{2}I_{K_\ell},
\qquad
I_{K_\ell}
=\int_{S^{d-1}/\Gamma}|K_\ell|_{r=1}^2\,d\theta.
\]

Operator–nuclear norm duality therefore yields
\[
\boxed{
\|D\operatorname{Ric}_e u\|_{\mathrm{op},\infty}
\ge
\frac{(d+2\ell-2)I_{K_\ell}}
{2J_{K_\ell}H_\ell(b,R)}.
}
\]

Consequently:

- For \(\ell=2\),
  \[
  \|D\operatorname{Ric}_e u\|_{\mathrm{op},\infty}
  \ge \frac{(d+2)I_K}{2J_K\log(R/b)}.
  \]
- For fixed \(R\) and \(b/R\to0\), \(\ell>2\) gives
  \[
  H_\ell(b,R)\sim \frac{b^{2-\ell}}{\ell-2},
  \qquad
  \|D\operatorname{Ric}_e u\|_{\mathrm{op},\infty}
  \gtrsim b^{\ell-2}\longrightarrow0.
  \]

Thus \(\ell=2\) is indeed the unique logarithmic case among the pure homogeneous polynomial modes considered here. Two qualifications matter:

1. This is a theorem about the linearized Ricci tensor. Passing to the Ricci defect of a nonlinear interpolated metric requires endpoint \(C^1\) control and bounds for the nonlinear remainder.
2. The classification does not include resonant \(r^\ell\log r\) terms or establish that every higher Biquard–Ozuch obstruction corresponds to one of these \(\ell>2\) modes.

Even the quadratic mode is not forced to vanish by \(\delta_i\to0\) alone: \(\delta_i\asymp1/L_i\) with \(L_i\to\infty\) is compatible with a nonzero quadratic coefficient. Its special feature is the rate relation \(\delta_iL_i\gtrsim1\), not a scale-independent positive lower bound.

---

## 2. Higher-obstruction scaling and what it establishes

Suppose the scaled ALE core metric satisfies
\[
g_t\sim t\,g_{\mathrm{ALE}},
\]
and an obstruction residual is a covariant two-tensor
\[
E_t=O(t^k)
\]
when measured relative to the fixed \(g_{\mathrm{ALE}}\) coordinates. Then
\[
E_t^{\sharp_{g_t}}
=g_t^{-1}E_t
=O(t^{-1})O(t^k)
=O(t^{k-1}).
\]
This tensor-to-endomorphism conversion is correct under that norm convention.

If \(t\asymp a^2\), then for every \(k\ge2\),
\[
\frac{t^{k-1}}{|\log a|^{-1}}
\asymp a^{2(k-1)}|\log a|
\longrightarrow0.
\]
More generally, the same conclusion holds for \(t\asymp a^q\) with any fixed \(q>0\). Thus a residual of order \(t^{k-1}\) is asymptotically smaller than the supplied FND:A1construction estimate
\[
\delta(g_a)\le \frac{C}{|\log a|}.
\]

### What follows rigorously from this comparison

An estimate of the form
\[
\delta_i\ge c\,|\mathcal O_k|\,t_i^{k-1}
\]
cannot imply \(\mathcal O_k=0\) when all that is known is
\[
\delta_i\to0,\qquad t_i\to0.
\]
A fixed nonzero coefficient \(\mathcal O_k\) remains compatible with both sides tending to zero. The logarithmic construction masks every fixed positive power of \(t\).

If a configuration with vanishing first obstruction and a demonstrably nonzero higher obstruction exists, and FND:A1construction applies to the same markings and insertion data, it supplies a concrete sequence with \(\delta\to0\) while that higher obstruction remains nonzero. At present, the supplied record does not exhibit such a computed configuration: the mixed-row second obstruction is still unresolved. Hence the scale comparison establishes that the proposed pinching/flux inference cannot force higher coefficients to vanish; it does not by itself establish that a nonzero higher coefficient actually occurs in the mixed rows.

### Two source issues requiring separation

1. The quoted Ozuch passage explicitly distinguishes behavior through orders \(t\) and \(t^2\). The general sentence “the \(k\)-th obstruction produces \(O(t^k)\)” needs the precise formal expansion and its norm convention from the source. “Desingularization up to \(o(t^k)\)” could refer to a metric expansion rather than directly to the Einstein residual.
2. The cone calculation classifies radial homogeneity \(\ell\). The supplied Step-73 plan explicitly states that obstruction order \(k\), ALE Jacobi decay, and cone degree \(\ell\) have not been identified with one another. Therefore “\(\ell=2\) is the unique logarithmic homogeneous mode” is proved, while “the first Biquard obstruction is the unique obstruction detectable by this norm” additionally needs a mode-identification theorem or the separate \(t\)-expansion argument.

The phrase “structural impossibility” is mathematically accurate only in the following precise sense: convergence of the unweighted scalar quantity \(\delta_i\) supplies no rate comparison with \(t_i^{k-1}\), so the displayed scale estimate cannot yield \(\mathcal O_k=0\).

Additional sequence information can change that inference. Examples include
\[
\delta_i=o(t_i^{k-1}),
\]
a weighted residual estimate, a uniform lower bound for the relevant bubble scale, normalized convergence of \(t_i^{1-k}(\operatorname{Ric}-\sigma g)\), or an algebraic tower identity forcing higher coefficients to vanish once the first one vanishes. Exact Einstein metrics converging through the specified gluing model also impose the complete local obstruction equations. These are all stronger data than unweighted \(C^0\) pinching with no scale relation.

---

## 3. Product transfer

Let \(m=n-4\) and
\[
G_a=g_a\oplus g_N
\]
on \(M^4\times S^m\). The Levi-Civita connection splits, so
\[
\operatorname{Ric}_{G_a}
=\operatorname{Ric}_{g_a}\oplus\operatorname{Ric}_{g_N}.
\]
If \(\operatorname{Ric}_{g_N}=\sigma g_N\), then
\[
(\operatorname{Ric}_{G_a}-\sigma G_a)^{\sharp_{G_a}}
=
(\operatorname{Ric}_{g_a}-\sigma g_a)^{\sharp_{g_a}}
\oplus 0.
\]
For a self-adjoint block-diagonal endomorphism,
\[
\|A\oplus B\|_{\mathrm{op}}
=\max(\|A\|_{\mathrm{op}},\|B\|_{\mathrm{op}}).
\]
Hence, pointwise and after taking the global supremum,
\[
\boxed{
\delta_\sigma(G_a)=\delta_\sigma(g_a).
}
\]

For the unit round \(S^m\),
\[
\operatorname{Ric}_{g_{\mathrm{round}}}=(m-1)g_{\mathrm{round}}.
\]
Taking
\[
g_N=\frac{m-1}{\sigma}g_{\mathrm{round}}
=\frac{n-5}{\sigma}g_{\mathrm{round}}
\]
gives \(\operatorname{Ric}_{g_N}=\sigma g_N\) whenever \(m\ge2\), namely \(n\ge6\).

For \(n=5\), the auxiliary factor is one-dimensional. Every one-dimensional Riemannian metric has identically zero Ricci tensor, so the circle block contributes
\[
(0-\sigma g_{S^1})^{\sharp}=-\sigma I.
\]
Its norm is \(\sigma\), not a quantity tending to zero. Thus the direct positive-Einstein product construction does not cover dimension five.

### Exact architectural consequence

The product calculation transfers the near-pinched four-dimensional families to all \(n\ge6\), and the limiting isolated \(A_1\) points become codimension-four strata \(A_1\times S^{n-4}\). It therefore shows that high-dimensional noncollapsed analysis must accommodate these product-type strata.

It does **not** prove that solving \(P_4^+\) proves \(P_n^+\) for arbitrary \(n\)-manifolds. Nor does nonexistence of an Einstein metric on \(M^4\) imply nonexistence on \(M^4\times S^{n-4}\), since an Einstein metric on the product manifold need not split. Conversely, if \(M^4\) carries a positive Einstein metric with constant matching the scaled sphere, the product family itself carries a product Einstein metric. The verified transfer concerns the near-pinched input metrics; a general dimension-reduction theorem for Einstein existence is not supplied by the product formula alone.