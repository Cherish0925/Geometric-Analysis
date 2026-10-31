# Step 9: Noncollapsed finiteness, all-dimensional structure, and the Sha-Yang dichotomy

Session: S0910A02. Agent2/Constructor. Phase: Explore.

## 0. Target fidelity

The active target is Yau Problem 26: for every n ≥ 2, decide whether dimension-only constants c_n < C_n force any closed connected smooth n-manifold carrying c_n g ≤ Ric_g ≤ C_n g to admit some Einstein metric.  The branch reduction reduces this to proving P_n^+ or P_n^- for each n.  This note constructs new theorems for the positive branch P_n^+ from Cheeger–Naber [arXiv:1406.6534], combined with Myers and Bishop–Gromov, under the hypothesis |Ric_g - g|_op ≤ δ with δ < 1/2.

**These theorems do not assume Einstein metrics on the sequence.  They use only two-sided Ricci bounds, which is exactly the Yau-26 hypothesis.**

---

## 1. Theorem A: Noncollapsed Positive Finiteness (dimension 4)

**Theorem A.**  For every δ_0 ∈ (0, 1/2) and v > 0, there exists N = N(δ_0, v) ∈ ℕ such that the set of oriented diffeomorphism types of closed connected oriented smooth 4-manifolds (M, g) satisfying

    |Ric_g - g|_op ≤ δ_0,    Vol(M, g) ≥ v,

contains at most N elements.

In particular, b_2(M) ≤ B(δ_0, v) := max{b_2(M') : M' in the finite set} and χ(M) ≤ X(δ_0, v).

**Proof.**  The hypotheses give:

(i) |Ric_g|_op ≤ 1 + δ_0.  Under operator norm, this gives |Ric| ≤ 3 for δ_0 < 2; under Hilbert–Schmidt norm in dim 4, |Ric|_HS ≤ 2(1+δ_0) < 3 precisely when δ_0 < 1/2.  So δ_0 < 1/2 covers both conventions.

(ii) Myers diameter bound: Ric ≥ (1−δ_0) g ≥ 0, so Ric ≥ (n−1)K g with K = (1−δ_0)/3.  Hence
$$\operatorname{diam}(M,g) \le \frac{\pi}{\sqrt{K}} = \pi\sqrt{\frac{3}{1-\delta_0}} =: D(\delta_0).$$

(iii) Bishop–Gromov volume comparison: since Ric ≥ (1−δ_0) g and diam ≤ D, for every p ∈ M:
$$\operatorname{Vol}(B_1(p)) \ge \operatorname{Vol}(M) \cdot \frac{V_K(1)}{V_K(D)} \ge v \cdot c(\delta_0)^{-1} =: v'(\delta_0, v) > 0,$$
where V_K(r) is the volume of a ball of radius r in the 4-dim space form of curvature K, and c(δ_0) = V_K(D)/V_K(1).  See the companion script for explicit values.

Now apply Cheeger–Naber Theorem 1.12:

> *If M^4 satisfies |Ric| ≤ 3, Vol(B_1(p)) > v' > 0, and diam(M) ≤ D, then M^4 can have one of at most C(v', D) diffeomorphism types.*

**This theorem does not assume Einstein.**  It follows from the codimension-4 regularity (Theorem 1.4), quantitative stratification, and the bubble-tree decomposition (Theorem 8.64) of §8.4.

Since v' = v'(δ_0, v) and D = D(δ_0), we get N = C(v'(δ_0, v), D(δ_0)), completing the proof.  □

**Remark.**  Finite diffeomorphism types implies bounded Betti numbers: take B(δ_0,v) = max{b_2(M') : M' in the finite type set}.  Since b_1 = 0 (Bochner) and M is oriented, χ = 2 + b_2.  Note: N types does not imply b_2 ≤ N−2 (a single type can have large b_2); the bound is B = max b_2 over the finite set, which is itself finite.

---

## 2. The upper Ricci bound is load-bearing

The finiteness in Theorem A requires the **two-sided** Ricci bound.  This is not a technical artifact:

- Sha–Yang (1991) construct metrics with Ric > 0 on #_k(S^2 × S^2) for every k ≥ 1.
- These have b_2 = 2k, which grows without bound.
- One-sided Ric ≥ (n−1)K gives Myers, Bishop, Bochner b_1 = 0, but NOT finite diffeomorphism types: Cheeger–Colding theory with only lower Ricci gives codimension-2 regularity for noncollapsed limits, not codimension-4 or finiteness.
- It is precisely the UPPER bound |Ric| ≤ C that, via Cheeger–Naber Theorem 1.4, upgrades regularity to codimension 4 and enables the bubble-tree decomposition.

Therefore the Yau-26 two-sided condition is the active mathematical ingredient, and Sha–Yang's family is the sharpness witness.

---

## 3. Corollary: the Sha–Yang Dichotomy

**Corollary (Sha–Yang Dichotomy).**  Let M_k = #_k(S^2 × S^2), k ≥ 1.  Define
$$\delta_+(M_k) := \inf\left\{\|Ric_g - g\|_{L^\infty,\mathrm{op}} : g \text{ Riemannian metric on } M_k\right\}.$$
Then exactly one of the following holds for the family {M_k}:

**(A') Tail pinching rigidity:**  liminf_{k→∞} δ_+(M_k) > 0.

**(B') Collapsing regime:**  There exist k_j → ∞ and metrics g_j on M_{k_j} with ||Ric_{g_j} - g_j||_op → 0, and necessarily Vol(M_{k_j}, g_j) → 0.

Note: S²×S² itself has δ_+ = 0 (the product of unit round metrics has Ric = g), so (A) as originally stated with "for all k ≥ 1" is false.  The correct formulation uses liminf as k → ∞.

**Proof.**  Suppose (A') fails.  Then there exist k_j ≥ j with k_j → ∞ and normalized metrics g_j on M_{k_j} with ||Ric_{g_j} - g_j||_op < 1/j → 0.  If the volumes do not tend to zero, a subsequence satisfies Vol(M_{k_j}, g_j) ≥ v_0 > 0.  Fix δ_0 = 1/4.  For large j, ||Ric_{g_j} - g_j||_op ≤ δ_0.  Theorem A gives at most N(δ_0, v_0) diffeomorphism types.  But b_2(M_{k_j}) = 2k_j → ∞, contradiction.  Here δ_0 = 1/4 is completely independent of k.  □

**Clarification on Vol → 0:** The volume statement is meaningful only for the metrics normalized to Ric ≈ g.  A different normalization would change the volume scale; the claim is that no normalization simultaneously achieves both ||Ric - g||_op → 0 and Vol ≥ v > 0 on the large-k tail.

**Quantitative stress test from the Weyl lower bound:**  If (B) holds, the Step 8 CGB identity gives

$$\int_{M_k} |W|^2 \ge 8\pi^2\left[\chi(M_k) - 2\left(\frac{1+\delta}{1-\delta}\right)^2\right] = 8\pi^2\left[2 + 2k - 2\left(\frac{1+\delta}{1-\delta}\right)^2\right],$$

which for small δ gives ∫|W|² ≥ 16π²k − O_δ(1), inside Vol ≤ 24π²/(1−δ)² → 24π².  

In regime (B'), both Vol → 0 and ∫|W|² → ∞.  The mean Weyl curvature |W|²_mean = ∫|W|²/Vol → ∞, and the curvature scale is forced down to ~ k^{−1/4}.  Each nontrivial ALE bubble has quantized curvature energy ∫|Rm|² = 8π²(χ(ALE) − 1/|Γ|) ≥ 12π² (with equality for Eguchi–Hanson, where χ = 2 and |Γ| = 2).  However, individual bubbles can absorb more energy if χ(ALE) is large, so the number of concentration regions need not be exactly O(k); what is forced is that total curvature energy ∫|W|² grows linearly in k while volume shrinks, making any candidate collapsing construction extremely constrained.

---

## 4. Theorem B: All-dimensional noncollapsed structure

**Theorem B (All-dimensional).**  Let n ≥ 4 and let (M_i^n, g_i) be a sequence of closed connected smooth n-manifolds with
$$\|Ric_{g_i} - g_i\|_{L^\infty,\mathrm{op}} \le \delta_i \to 0, \qquad \operatorname{Vol}(M_i, g_i) \ge v > 0.$$
Then:

(a) A subsequence converges in pointed Gromov–Hausdorff to a compact metric space (X, d).

(b) X is smooth away from a closed singular set S with dim_H(S) ≤ n − 4 (also Minkowski dimension ≤ n − 4).

(c) On X \ S, the limit metric g_∞ is a smooth Einstein metric with Ric_{g_∞} = g_∞.

(d) At each singular point p ∈ S, every tangent cone is a noncollapsed Ricci-flat metric cone C(Y).  On the regular part of Y, Ric_Y = (n−2)g_Y.

**Dimension-dependent refinement:**  For n = 4, Y is necessarily S³/Γ (smooth, constant curvature 1) by CN §8.2.  For n ≥ 5, Y itself may have a singular set; the statement Ric_Y = (n−2)g_Y holds only on its regular part (CN Theorem 1.4 applied recursively).

**Proof.**

*Step 1 (Compactness):*  |Ric_{g_i}| ≤ 1 + δ_i.  For i large, |Ric_{g_i}| ≤ 2 < n − 1 (n ≥ 4).  Myers: diam ≤ D(n).  Bishop–Gromov as in Theorem A: Vol(B_1(p)) ≥ c(n)v for all p ∈ M_i.  Gromov's precompactness theorem gives a GH-convergent subsequence.

*Step 2 (Codimension-4 regularity):*  The hypotheses |Ric_{g_i}| ≤ n − 1 and Vol(B_1(p_i)) > v' > 0 are exactly those of Cheeger–Naber Theorem 1.4.  Hence dim(S) ≤ n − 4.

*Step 3 (Einstein on the regular set):*  On X \ S, r_h > 0 uniformly on compact subsets (Theorem 1.4 + standard ε-regularity).  Therefore the convergence is C^{1,α} ∩ W^{2,q} in harmonic coordinates for every α < 1, q < ∞.  In harmonic coordinates, the Ricci tensor satisfies the quasilinear elliptic system:
$$\operatorname{Ric}_{ij} = -\frac{1}{2} g^{kl}\partial_k\partial_l g_{ij} + Q_{ij}(g, \partial g)$$
where Q is quadratic in ∂g.  Since Ric_{g_i} = g_i + E_i with |E_i| ≤ δ_i → 0, in the C^{1,α} ∩ W^{2,q} limit:
$$-\frac{1}{2} g_\infty^{kl}\partial_k\partial_l g_{\infty,ij} + Q_{ij}(g_\infty, \partial g_\infty) = g_{\infty,ij}.$$
By Schauder theory: g_∞ ∈ C^{2,α}, bootstrap to C^∞.  Hence Ric_{g_∞} = g_∞ smoothly on X \ S.

*Step 4 (Tangent cones):*  At a singular point p ∈ S, take a blow-up sequence: ĝ_i = r_i^{-2} g_i for some r_i → 0.  Then |Ric_{ĝ_i}| = r_i^2 |Ric_{g_i}| ≤ r_i^2(1 + δ_i) → 0.  The noncollapse carries over: Vol_{ĝ_i}(B_1^{ĝ_i}(p)) ≥ c(n)v/c'.  By steps 2–3, the tangent cone C(Y) is smooth Ricci-flat on the regular set, so Ric_Y = (n−2)g_Y.  □

**Key observation for the projection bridge:**  The blow-up at singular points is **Ricci-flat** with defect O(r_i²), independent of δ_i.  The Einstein constant scales away at the bubble scale.  This is the structural reason that the obstruction-amplitude principle can work: the ALE bubble sees only its own geometry, not the ambient Einstein constant.

---

## 5. Dimension 4: singular structure from §8.2

In dimension 4, Theorem B strengthens dramatically via Cheeger–Naber §8.2 (Theorem 8.6):

**Theorem C (4-dim singular structure).**  Under the hypotheses of Theorem B with n = 4, at each singular point p ∈ S:

(a) S consists of isolated points (codim ≥ 4 in dim 4 means dim ≤ 0).

(b) The tangent cone is R^4/Γ for a finite subgroup Γ ⊂ O(4) with |Γ| ≤ N(v).

(c) Y = S³/Γ has constant sectional curvature 1.  (In dim 3, Ric_Y = 2g_Y with constant Ricci implies constant sectional curvature, by CN §8.2 line 1177.)

(d) Near p, the annular region A_{ε,2}(p) is diffeomorphic to the standard annulus in R^4/Γ, and
$$\Phi_j^* g_j \xrightarrow{C^{1,\alpha} \cap W^{2,q}} dr^2 + r^2 g_{S^3/\Gamma}.$$

**This is the precise annular convergence that the projection bridge needs.**

More precisely, §8.2 shows: if the volume ratio is almost constant across a range of scales (which holds for all but finitely many scales by Lemma 8.15/Corollary 8.21), then the annulus has positive harmonic radius bounded below by r_0(v)ε, and is diffeomorphic to the model annulus in R^4/Γ with C^0-metric closeness < ε and C^0 first-derivative closeness < ε.

---

## 6. Consequences for the projection bridge

The §8.2 annular convergence provides exactly the inputs for the Step 8 projection-bridge template:

**Available structure at each ALE concentration point p_j:**
1. A group Γ_j ⊂ O(4) with |Γ_j| ≤ N(v).
2. Annular diffeomorphism Φ_j: A_{ε,2}(0) → A_{ε,2}(p_j) ⊂ M_i with
   ||Φ_j* g_i − g_{flat/Γ}||_{C^0} + ||∂(Φ_j* g_i − g_{flat/Γ})||_{C^0} < ε_j → 0.
3. At the inner scale t_j (bubble scale), ĝ_i = t_j^{-2} g_i → R^4/Γ_j in C^{1,α} ∩ W^{2,q}.
4. |Ric_{ĝ_i}| ≤ t_j^2(1 + δ_i) → 0: the Ricci defect at bubble scale is O(t_j^2), independent of δ_i.

**Scaling of the test field (TTCS-corrected scale convention):**  Let ℓ_j denote the LENGTH scale (so ĝ = ℓ_j^{-2} g and τ_j = ℓ_j² is the metric scale).  Let φ_0 be a bounded symmetric (0,2)-tensor on R^4/Γ_j.  Transport to M_i via Φ_j and cutoff.  Then:
- g_i ~ ℓ_j² g_{flat}, so g_i^{-1} ~ ℓ_j^{-2} g_{flat}^{-1}
- |φ_j|_{g_i} ~ ℓ_j^{-2} |φ_0|_{flat}  (raising one index with g_i^{-1})
- dμ_{g_i} ~ ℓ_j^4 dμ_{flat}  (4-dim volume element)
- ||φ_j||_{L^1(g_i)} = O(ℓ_j²) = O(τ_j)

Note: if the test field grows quadratically at infinity (as suggested by the ρ^{-4} pairing with W⁺), the outer annulus dominates L¹ mass and the O(δτ) estimate requires a boundary/flux formulation rather than a bulk L¹ bound.  This is a genuine analytic difficulty for the bridge.

Combined with the C^0 pinching:
$$\left|\int_M \langle Ric(g_i) - g_i, \phi_j\rangle\right| \le \delta_i \cdot \|\phi_j\|_{L^1} = O(\delta_i \cdot t_j).$$

If the bridge identity gives ∫ = t_j · Obstruction(R_+(p), Γ, rotation) + o(t_j), then dividing by t_j:
$$\text{Obstruction} = O(\delta_i) + o(1) \to 0.$$

**What the bridge must actually prove** (the remaining mathematical work):
- Define the precise ALE obstruction mode φ_0 on R^4/Γ (from Biquard–Ozuch theory)
- Show the cutoff + transport error is o(t_j) (this requires the C^{1,α} convergence of §8.2 and the decay rate of φ_0)
- Extract the leading-order obstruction coefficient through integration by parts (Bianchi identity moves derivatives onto the smooth test field)
- Identify the obstruction with det R_+|_{Λ²_+} or the appropriate first-obstruction tensor

The C^{1,α} annular convergence is sufficient for the transport: derivatives of the metric error are controlled, and they pair with first derivatives of the smooth test field.  The decay rate of the Eguchi–Hanson obstruction mode is r^{-4} (the ADM mass vanishes), so the relevant coefficient is at the ρ^{-4} level and the test field must be quadratic in cone coordinates.

---

## 7. What remains for the full positive-branch argument

Using Theorems A, B, C, the positive branch P_n^+ now has the following structure:

**Regime (I): Noncollapsed, smooth convergence.**  
If a sequence with δ_i → 0, Vol ≥ v has S = ∅ (no singular points in the limit), then for large i the manifolds are diffeomorphic to the limit Einstein manifold.  **Closed.**

**Regime (II): Noncollapsed, orbifold concentration.**  
The limit has isolated orbifold points (Theorem C).  Need:
(a) Projection bridge to show first obstruction vanishes at each singular point.
(b) Higher-order obstruction analysis (Biquard–Ozuch–LeBrun–Ozuch theory).
(c) Topology recovery: smooth manifold structure from the orbifold resolution.
The bridge input is §8.2; the main construction is the integration-by-parts identity.

**Regime (III): Collapse (Vol → 0).**
This is the genuinely open regime.  **The Sha–Yang dichotomy shows that either collapse doesn't occur for tight pinching (which closes P_4^+), or collapse with enormous Weyl concentration occurs.**  The collapse regime is the single remaining hypothesis carrying the entire positive-branch argument.

**For n ≥ 5:**  Theorem B gives the structural result.  The finiteness analogue requires L^{n/2} curvature bounds (not available from CGB in higher dimensions) or new ideas.  Yao's general-dimensional resolution theory (arXiv:2603.14929) may supply the obstruction-amplitude principle in dimension-free form.  The dim-4 CGB budget (∫|W|², χ > 0) has no direct higher-dimensional analogue.

---

## 8. Source verification

- **Cheeger–Naber Theorem 1.4**: Knowledge/objects/papers/1406.6534-..., line 83.  Assumes |Ric| ≤ n−1 and Vol(B₁) > v > 0.  Conclusion: dim S ≤ n−4 (Hausdorff and Minkowski).  **No Einstein assumption.**
- **Cheeger–Naber Theorem 1.12**: Same file, line 103.  Assumes |Ric| ≤ 3, Vol(B₁) > v, diam ≤ D in dim 4.  Conclusion: at most C(v,D) diffeomorphism types.  **No Einstein assumption.**
- **Cheeger–Naber Theorem 1.13**: Same file, line 107.  |Ric| ≤ 3, Vol(B₁) > v in dim 4 gives ∫_{B₁}|Rm|² ≤ C(v).  **No Einstein for the L² bound.**  Regularity scale needs Einstein or |∇Ric|.
- **Cheeger–Naber §8.2, Theorem 8.6**: Same file, line 1163.  Annular convergence to R⁴/Γ in C^{1,α} ∩ W^{2,q} under almost-constant volume ratio + bounded Ricci.
- **Sha–Yang**: Knowledge/objects/papers/Ricci-positive-metrics-on-connected-sums-of-projective-spaces--17bdbf22f9bb.  Ric > 0 on #_k(S²×S²) for all k.
- **Step 8 Weyl lower bound**: workspace/notes/step8_preceptor_review_positive_branch.md, workspace/data/step8_weyl_budget_positive4.json.

---

## 9. Erratum on prior notes

The Step 5 note and Step 7 note recorded an "ε-regularity unknown" as the single named unknown.  This is corrected: Cheeger–Naber Theorem 6.1 **is** an ε-regularity theorem for bounded Ricci (not Einstein), keyed to GH closeness to R^{n−3} × C(Y).  What actually fails without Einstein is:

- **Pointwise regularity scale** r_x (Definition 1.6): requires Einstein or ∇Ric (Remark 1.11)
- **Harmonic radius** r_h: controlled by bounded Ricci alone (Theorem 1.13 in dim 4; Theorem 1.4 + 6.1 in all dim)

The correct statement of the remaining analytic unknown is: **whether the orbifold singularities of the noncollapsed limit are actually realized by the converging sequence, or whether the C^0 Ricci pinching forces the limit to be smooth.**  This is the projection-bridge question, not a general ε-regularity question.

The second remaining unknown is **uniform noncollapse**: this is the single hypothesis carrying the entire noncollapsed program.  It is not one gap among six — it IS the gap.
