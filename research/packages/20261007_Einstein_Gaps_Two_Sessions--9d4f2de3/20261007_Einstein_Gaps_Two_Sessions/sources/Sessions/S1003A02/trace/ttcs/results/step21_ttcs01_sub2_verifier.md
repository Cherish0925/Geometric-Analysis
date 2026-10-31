# TTCS Independent Branch Record

```json
{
  "step_id": 21,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/ENTROPIES-VOLUMES-AND-EINSTEIN-METRICS--0ee1eb110f9d--94203f883336/originals/ENTROPIES__VOLUMES__AND_EINSTEIN_METRICS.pdf"
  ]
}
```

## Task

Read the actual Kotschick PDF and verify the exact Sambusetti/BCG statement relevant to a closed oriented real-hyperbolic four-manifold Y and X=Y#k CPbar. Extract the precise topological calculation showing whether an Einstein metric on X is excluded for each k>=1. Distinguish existence obstruction from any quantitative lower bound on the L2 Einstein defect or near-Einstein sequences. Also assess whether the PDF gives any result about Yamabe invariants of these blow-ups.

## Output

# Verification memo: Sambusetti/BCG obstruction for X = Y # k CP̄², with Y a closed oriented real-hyperbolic 4-manifold

## 1. The relevant statements in the PDF

**Corollary 3, eq. (14), p. 8 (attributed to Sambusetti [36]).** Let X be a closed oriented Einstein 4-manifold. If X admits a map of non-zero degree d to a real hyperbolic manifold Y, then
$$\chi(X)\ \ge\ \tfrac32|\sigma(X)| + |d|\,\chi(Y),$$
with equality only if X is also real hyperbolic.

**Proof on p. 9.** It combines Theorem 1, eq. (5),
$$\chi(X)\ \ge\ \tfrac32|\sigma(X)| + \frac{\lambda(X)^4}{108\pi^2},$$
with the BCG inequality [9]
$$\lambda(X)^4 \ \ge\ d\,\lambda(Y)^4 = d\cdot 3^4\,\mathrm{Vol}(Y,g_0), \qquad K_{g_0}=-1.$$
It then uses Gauss–Bonnet to get $\mathrm{Vol}(Y,g_0)=\tfrac{4\pi^2}{3}\chi(Y)$, so that $3^4\,\mathrm{Vol}(Y,g_0)=108\pi^2\chi(Y)$. The proof writes d where |d| is meant. This is immaterial here because d = 1.

**Constants, checked independently.**
- For K = −1 in dimension 4: s = −12, W = 0, Ric₀ = 0. Eq. (6) gives χ = (1/8π²)(144/24)Vol = 3Vol/(4π²), which matches.
- The hyperbolic volume entropy is n − 1 = 3. At unit volume, λ(Y,ĝ)⁴ = 81·Vol(Y,g₀), and BCG [9] says this metric minimizes entropy. So λ(Y)⁴ = 108π²χ(Y).
- In Kotschick's normalization Ric = −g/3, we have s = −4/3 and s²/24 = 2/27. Then (1/8π²)(2/27) = 1/(108π²), which matches eq. (9).

## 2. Topological calculation for X = Y # k CP̄², k ≥ 1

**Topological data.**
- χ(X) = χ(Y) + k, since each summand adds χ(CP̄²) − 2 = 1.
- σ(Y) = 0, because the hyperbolic metric is conformally flat (eq. (7) with W± = 0). Hence σ(X) = −k.
- χ(Y) = 3Vol/(4π²) > 0.

**The map.** The collapse map X → Y, pinching each CP̄² summand to a point, has degree d = 1. Moreover π₁(X) = π₁(Y), and the classifying map of X factors through the collapse, so f_*[X] = f_*[Y] in H₄(Bπ₁). Brunnbauer's homological invariance (PDF pp. 4 and 6) then gives
$$\lambda(X)^4=\lambda(Y)^4=108\pi^2\chi(Y)$$
exactly, not merely as an inequality.

**Evaluating (14) or (5).**
$$\chi(X)-\tfrac32|\sigma(X)|-\chi(Y) \;=\; \chi(Y)+k-\tfrac32 k-\chi(Y)\;=\;-\tfrac k2\;<\;0 .$$
So (14) is violated by exactly k/2 for every k ≥ 1, independently of χ(Y). No Einstein metric exists on Y # k CP̄² for any k ≥ 1.

**The other branches of Theorem 1's proof.**
- s > 0 is excluded by Myers, since π₁ is infinite.
- s = 0 is excluded because π₁ is infinite and χ(X) > 0, so the metric is not flat (Cheeger–Gromoll step, p. 7).
- Only the s < 0 branch remains, and the computation above excludes it.

**Comparison with Hitchin–Thorpe alone.** Hitchin–Thorpe requires χ(Y) + k ≥ 3k/2, that is, k ≤ 2χ(Y). It therefore excludes only k > 2χ(Y). The entropy term is what closes the range 1 ≤ k ≤ 2χ(Y).

## 3. Existence obstruction versus quantitative Einstein defect

The PDF proves only non-existence. The step that uses the Einstein equation is eq. (6), where the term −|Ric₀|² is discarded. Two features prevent the argument from passing to arbitrary metrics:

1. **The Bishop step (eq. (9)) needs a pointwise bound Ric ≥ −g/3.** This bound converts λ(X,g) ≤ 1 into ∫s² ≥ (16/9)Vol ≥ (16/9)λ(X)⁴. For a non-Einstein metric, Ric ≥ −g/3 bounds s from below but gives no lower bound on ∫s².
2. **Integral replacements are critical.** Integral Bishop-type comparison with ‖Ric₋‖_{L^p} (Petersen–Wei; this is outside the PDF) requires p > n/2 = 2. The scale-invariant quantity ∫|Ric₀|² sits exactly at the critical exponent, where curvature can concentrate.

**What the PDF's identities give for an arbitrary metric g.** Equations (6)–(8) without the Einstein assumption give
$$\frac{1}{8\pi^2}\int|\mathrm{Ric}_0|^2 \;=\;\frac{1}{192\pi^2}\int s^2+\frac{1}{8\pi^2}\int|W|^2-\chi(X)\;\ge\;\frac{1}{192\pi^2}\int s^2+\frac k2-\chi(Y).$$
Here ∫|W⁻|² ≥ 12π²k holds for every metric, by (7). This yields two consequences:

- **Unconditional bound for large k.** Using only ∫s² ≥ 0:
  $$\int|\mathrm{Ric}_0|^2\,d\mu_g\ \ge\ 4\pi^2\,(k-2\chi(Y)) \quad\text{for every } g,$$
  which is positive for k > 2χ(Y). This is a genuine positive gap for the scale-invariant functional ∫|Ric₀|², but it is a Hitchin–Thorpe-level statement only.
- **Conditional bound for small k.** For 1 ≤ k ≤ 2χ(Y), a positive bound would follow from the scalar-curvature estimate
  $$\int s_g^2\,d\mu_g\ \ge\ 192\pi^2\chi(Y)\quad\text{for all } g \text{ on } X.$$
  Note that 192π²χ(Y) is exactly ∫s² of the hyperbolic metric: 144 · (4π²/3)χ(Y). If this estimate held, it would give
  $$\int|\mathrm{Ric}_0|^2\ \ge\ 4\pi^2 k,$$
  with the defect constant 4π² per blow-up matching the k/2 deficit in §2.

The PDF contains no such scalar estimate for hyperbolic blow-ups. The entropy λ(X) controls ∫s² only through the pointwise Ricci bound. Whether near-Einstein sequences with ∫|Ric₀|² → 0 exist on Y # k CP̄² for 1 ≤ k ≤ 2χ(Y) is not addressed anywhere in the PDF.

## 4. Yamabe invariants in the PDF

The PDF gives no result on the Yamabe invariants of Y # k CP̄².

- The only scalar-curvature estimate it contains is the monopole-class bound c² ≤ (1/32π²)∫s² on pp. 10–11. That bound is applied to Y_k = Z_k # (1+k)(S¹ × S³), where Z_k is symplectic, to prove MinVol > 0. Hyperbolic manifolds are not treated there.
- The PDF says explicitly that the entropy obstruction is homological (Remark 1, p. 6; p. 2: it "subsumes all the known obstructions which are homotopy invariant"). It refers to [22, 24] for obstructions that depend on the smooth structure. Such homological input cannot by itself see ∫s².

**Translation of §3 into Yamabe language (standard facts, not from the PDF).** For a 4-manifold with Yamabe invariant 𝒴(X) ≤ 0, inf_g ∫s² = 𝒴(X)². The needed estimate is therefore
$$\mathcal Y(Y\#k\overline{\mathbb{CP}}{}^2)\ \le\ -\sqrt{192\pi^2\chi(Y)} = s_{g_0}\,\mathrm{Vol}(Y,g_0)^{1/2}.$$
- The reverse inequality 𝒴(X) ≥ 𝒴(Y) is expected from Kobayashi's connected-sum inequality, because 𝒴(CP̄²) > 0.
- The required direction would say that the hyperbolic metric realizes 𝒴(Y) and that blowing up does not lower it. This is the analogue of LeBrun's Seiberg–Witten results, but hyperbolic Y supplies no basic classes from the PDF.

This scalar-curvature statement is the independent piece of information separating "no Einstein metric" from "positive L² Einstein gap" for 1 ≤ k ≤ 2χ(Y). It is unresolved by the supplied material.