# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step9_noncollapsed_finiteness_and_all_dim_structure.md",
    "Sessions/S0910A02/workspace/data/step9_finiteness_constants.json",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md",
    "Sessions/S0910A02/workspace/notes/step8_preceptor_review_positive_branch.md",
    "Sessions/S0910A02/workspace/briefing/aligned_research_goal.md"
  ]
}
```

## Task

Verify the following claims for the positive branch of Yau Problem 26, checking the chain of implications against the actual source statements.

1. THEOREM A (Noncollapsed Positive Finiteness, dim 4): If |Ric_g - g|_op ≤ δ < 1/2 and Vol(M,g) ≥ v > 0 on a closed oriented 4-manifold, then M is one of at most C(δ,v) diffeomorphism types. The proof chain is: |Ric| ≤ 1+δ < 3; Myers diam ≤ π√(3/(1-δ)); Bishop-Gromov Vol(B₁(p)) ≥ c(δ)v for ALL p; Cheeger-Naber Theorem 1.12 applies. Check: does CN 1.12 require uniform noncollapse at every point or at one point? Is the Bishop-Gromov argument for uniform noncollapse correct when diam ≤ D?

2. THEOREM B (All-dimensional structure): For n ≥ 4, a sequence with |Ric_{g_i}-g_i|_op → 0, Vol ≥ v converges (up to subsequence) in GH to a space smooth away from a set of codim ≤ n-4, with Ric = g on the regular part. Check: is the bootstrap from C^{1,α} ∩ W^{2,q} convergence to smooth Einstein on the regular set correct?

3. SHA-YANG DICHOTOMY: The claim that for #_k(S²×S²), either δ_+ is bounded below for all large k, or collapse must occur. Check: is the logical chain from Theorem A + b₂ = 2k → ∞ to the dichotomy correct? Is there a gap in the argument (e.g., could δ₀ depend on k in a way that breaks the dichotomy)?

4. ε-REGULARITY CORRECTION: The claim that CN Theorem 6.1 is an ε-regularity for bounded Ricci (not Einstein), and what genuinely fails without Einstein is pointwise regularity scale r_x, not harmonic radius r_h. Check against the CN source.

5. BLOW-UP RICCI FLATNESS: The claim that at bubble scale t, |Ric_ĝ| = t²|Ric_g| ≤ t²(1+δ) → 0, so blow-ups are Ricci-flat independent of δ. Is this scaling correct for the operator norm?

## Output

# Verification memo — positive branch: Theorems A/B, Sha–Yang dichotomy, ε-regularity erratum, blow-up scaling

Session S0910A02, against `step9_noncollapsed_finiteness_and_all_dim_structure.md`, `step9_finiteness_constants.json`, `step8_preceptor_review_positive_branch.md`, and the supplied full text of Cheeger–Naber [1406.6534].

## 0. Outcome in one view

| Item | Verification outcome |
|---|---|
| Theorem A (dim 4 finiteness) | Implication chain is sound; hypotheses of CN 1.12 are met under either Ricci-norm convention precisely because δ<1/2. Two corrections: the Remark's `b_2 ≤ N−2` does not follow; orientation counting needs one line. Theorem A is a corollary of CN 1.12/8.64 + Myers + Bishop–Gromov, with no new analysis. |
| Theorem B (a)(b)(c) | Correct, including the harmonic-coordinate bootstrap to smooth `Ric_∞ = g_∞`; two supporting facts should be cited explicitly (closedness of `S`, continuity of `r_h`). |
| Theorem B (d) | Correct only for `n = 4`. For `n ≥ 5` the cross-section `Y` need not be smooth, and `Ric_Y = (n−2)g_Y` holds only on the regular part of `Y`. CN's own reference list contains the relevant evidence ([HN14]). |
| Sha–Yang dichotomy | Contains a quantifier gap: the negation of (A) does not supply `k_j → ∞`, which is exactly what the `b_2 = 2k_j → ∞` contradiction needs. Repairable by restating with `liminf_{k→∞}`. Also `δ_+` needs its reference metric and scale-normalization stated, or the statement "Vol → 0" is not well posed. |
| §2 sharpness attribution | Sha–Yang alone does not witness that the upper Ricci bound is load-bearing (no uniform normalized noncollapse). The supplied CN text gives the correct witness in §9: "Examples of Perelman show that if the 2-sided bound on the Ricci tensor is weakened to a lower bound, then the answer is [not affirmative]." |
| ε-regularity erratum (§9) | Correct as checked against CN Theorem 6.1 and Remark 1.11. Two hypotheses must be carried along: Thm 6.1 and Thm 8.6 assume *small* Ricci (`|Ric| ≤ ε`, `≤ 3δ`), so they apply only after rescaling to small scales; Thm 8.6 additionally needs volume-ratio near-constancy, available at all but `N(v,δ)` scales (Cor 8.21). |
| Blow-up Ricci scaling | `|Ric_{ĝ}|_{op,ĝ} = t²|Ric_g|_{op,g}` for `ĝ = t^{-2}g` is correct, and identical for the Hilbert–Schmidt norm. But §4 and §6 use two different meanings of `t` (length² vs length), and §6 uses a bounded test field in the `L¹` estimate while its closing paragraph requires a quadratically growing one. That inconsistency, not the scaling, is what would break the `O(δ t)` estimate. |
| Bubble energy quantum | The text's "`≥ 8π²/|Γ|`" does not match the Gauss–Bonnet accounting nor the JSON arithmetic. Correct quantum: `∫|Rm|² = 8π²(χ(X) − 1/|Γ|) ≥ 12π²`, with equality for Eguchi–Hanson; the JSON counts already divide by `12π²`. |

---

## 1. Theorem A

### 1.1 Norm convention — the hypothesis is met under both readings, and δ<1/2 is exactly what makes it so

CN write `|Ric_{M^n}| ≤ n−1`, i.e. `|Ric_{M^4}| ≤ 3`. Two readings are in circulation.

- Operator norm: `|Ric_g|_{op} ≤ 1+δ ≤ 1.5 < 3`. ✓
- Hilbert–Schmidt: `|Ric|_{HS} ≤ √4·(1+δ) = 2(1+δ)`, and `2(1+δ) < 3 ⟺ δ < 1/2`. ✓ (at δ = 0.49, `|Ric|_{HS} ≤ 2.98`).

So the hypothesis `δ < 1/2`, chosen in Step 4 for the CGB coefficient `β(δ)`, coincides with the threshold that makes the CN hypothesis hold under the stricter norm reading. The note's phrasing "for δ_0 < 2 this gives |Ric| ≤ 3" is the operator-norm reading only; stating `δ_0 < 1/2` covers both and costs nothing. In dimension `n ≥ 5` the analogous check is `√n(1+δ) ≤ n−1`, satisfied comfortably (n=5: `2.24 < 4`).

### 1.2 Myers and Bishop–Gromov: the uniform-in-p noncollapse is genuine

Myers with `Ric ≥ (1−δ)g = 3K g`, `K = (1−δ)/3`, gives `diam ≤ π√(3/(1−δ))`. Recomputed: δ=0.1 → 5.735 76; δ=0.49 → 7.6196. Consistent with the JSON.

The uniformity question is the important one, and the argument is correct. Bishop–Gromov monotonicity of `Vol(B_r(p))/V_K(r)` in `r`, with `D = π/√K ≥ diam`, gives for **every** `p`
```
Vol(B_1(p)) ≥ Vol(B_D(p)) · V_K(1)/V_K(D) = Vol(M) · V_K(1)/V_K(D).
```
Because `B_D(p) = M`, no basepoint is privileged. Numerical check of the ratio at δ=0.1 (`R = 1/√K = 1.825742`):
```
V_K(1)/V_K(πR) = ∫_0^{1/R} sin³u du / ∫_0^π sin³u du = 0.020367/(4/3) = 0.015275,
```
against the JSON's `0.015267`. ✓

Whether CN 1.12 needs noncollapse at one point or all points is settled inside the supplied source, in CN's own proof of Theorem 8.64: "if `p ∈ M^n`, then by volume ratio monotonicity, we have for every `r ≤ 1` that `Vol(B_r(p)) ≥ (Vol_{-1}(B_r)/Vol_{-1}(B_D))·Vol(B_D(p)) ≥ C(n,D)^{-1}Vol(M^4)r^n ≥ C^{-1}v r^n`", with Theorem 8.64's hypotheses being `Vol(M) ≥ v` and `diam ≤ D`. CN therefore perform exactly the conversion the note performs, and Theorem 8.64's hypotheses are literally Theorem A's. This is the strongest available confirmation: Theorem A's hypotheses are a verbatim instance of CN 8.64, with Myers supplying `D` for free.

One further point internal to CN worth carrying: their proof of 8.64 rescales to `|Ric| ≤ 3δ` and `diam ≤ Dδ^{-2}`, so the resulting constant is `C(v',D')` with `v',D'` functions of `(v,D)`. Nothing breaks, but the constant's dependence is not explicit and cannot be extracted from the citation chain. Theorem A's `N(δ_0,v)` inherits this non-explicitness.

### 1.3 Two corrections to the statement and Remark

(i) **Orientation.** CN 1.12 counts diffeomorphism types, not oriented ones. Each unoriented type carries at most two orientations, so the oriented count is `≤ 2C`. One sentence fixes this.

(ii) **`b_2 ≤ N − 2` does not follow.** `N` counts diffeomorphism types; it is not a bound on `χ`. What is available: only finitely many diffeomorphism types occur, hence `max b_2` over that finite set is finite, i.e. `b_2 ≤ B(δ_0,v)` with `B` unrelated to `N`. The identity `χ = 2 + b_2` (from `b_1 = 0` by Bochner, since `Ric ≥ (1−δ)g > 0`, plus Poincaré duality on a closed oriented 4-manifold) is correct.

### 1.4 An independent and more robust route to the topology bound

The Sha–Yang dichotomy needs only `b_2` bounded, not diffeomorphism finiteness. That weaker conclusion follows from a shorter chain that avoids CN's deepest theorem:

1. CN Theorem 1.13 (bounded Ricci, noncollapse, dim 4, **no Einstein**): `⨍_{B_1(p)}|Rm|² ≤ C(v)`.
2. Bishop upper bound with `K=(1−δ)/3`: the model is the round sphere of radius `R=√(3/(1−δ))`, so
   `Vol(M) ≤ (8π²/3)R⁴ = 24π²/(1−δ)²` — matching the JSON's `vol_upper_over_pi2 = 29.6296` at δ=0.1.
3. Myers + Bishop–Gromov: `M` is covered by at most `N₀(δ)` unit balls (a maximal 1-separated set has disjoint half-balls, each of volume `≥ c(δ)Vol(M)`), so `∫_M|Rm|² ≤ N₀(δ)C(c(δ)v)Vol(M)`.
4. CGB in the form already established in Step 8: `8π²χ = ∫(|W|² + s²/24 − |E|²/2) ≤ ∫|Rm|² + (2/3)(1+δ)²Vol`.

Hence `χ ≤ X(δ,v)` directly. This matters scientifically: the dichotomy then rests on CN 1.13 (a local `L²` estimate) rather than on the bubble-tree finiteness of §8.4, and it is insensitive to the diameter bound in step 1 (Thm 1.13 has no `diam` hypothesis).

Consistency check of the CGB identities used here, on the sharp model `S⁴(√3)` with `Ric = g`: `|Rm|² = 24K² = 8/3`, `Vol = 24π²`, so `∫|Rm|² = 64π²`; and `8π²χ + (5/2)∫|E|² + (1/8)∫s² = 16π² + 0 + (1/8)(16)(24π²) = 16π² + 48π² = 64π²`. ✓ Step 8's (2.2) and the `δ=0` sharpness of (2.4) are both confirmed on this model.

---

## 2. Theorem B

### 2.1 Steps 1–3 verified

**Step 1.** `|Ric_{g_i}|` (either norm) below `n−1` for large `i` ✓; Myers gives a uniform diameter bound so the convergence is compact GH, not merely pointed ✓; Bishop–Gromov gives `Vol(B_1(p)) ≥ c(n,δ)v` at every point ✓ (same computation as §1.2, dimension-general).

**Step 2.** CN Theorem 1.4's hypotheses are `|Ric| ≤ n−1` and `Vol(B_1(p_j)) > v`, with **no Einstein hypothesis** — confirmed verbatim in the source. Conclusion `dim S ≤ n−4` in Hausdorff and Minkowski senses ✓.

**Step 3 — the bootstrap is correct.** The chain deserves to be recorded with its two supporting facts, both present in the source:

- `S` is closed. CN §2.1: "under the assumption of a 2-sided bound `|Ric| ≤ (n−1)`, the singular set is indeed closed; see [A90], [ChCo2]." So `X∖S` is open and exhausted by compacta.
- `r_h > 0` at each regular point (CN Thm 6.1 after rescaling, or Thm 2.11), and `r_h` behaves continuously in the limit under `C^{1,α}∩W^{2,q}` convergence (CN §5.1, citing [A90]); hence `inf_K r_h > 0` on compact `K ⊂ X∖S`.

Given that, CN's remark after Definition 2.9 supplies the a priori bounds: with `|Ric|` bounded, `g_ij` in harmonic coordinates has `C^{1,α}∩W^{2,q}` bounds for all `α<1, q<∞`. The harmonic-coordinate Ricci expression `Ric_ij = −½g^{kl}∂_k∂_l g_ij + Q_ij(g,∂g)` is the standard DeTurck–Kazdan form ✓. Passage to the limit is legitimate term by term: `g_i → g_∞` in `C^1`, so `g_i^{kl} → g_∞^{kl}` in `C^0` and `Q(g_i,∂g_i) → Q(g_∞,∂g_∞)` in `C^0`, while `∂²g_i ⇀ ∂²g_∞` weakly in `L^q`; the product converges weakly in `L^q`, so the limit equation holds a.e. Harmonicity of the coordinates passes to the limit (the condition `g^{kl}Γ^m_{kl}=0` is `C^0`-stable), so the limit metric is in harmonic coordinates for itself. Then: RHS `= −2g_∞,ij + 2Q ∈ C^{0,α}`, coefficients `∈ C^{0,α}`, `g_∞ ∈ W^{2,q}` ⇒ interior Schauder gives `C^{2,α}`; iterating with RHS now `C^{1,α}` gives `C^{3,α}`, and so on to `C^∞`. The Einstein constant is exactly `1` because no rescaling occurred and `δ_i → 0`. ✓

### 2.2 Theorem B(d) holds only in dimension 4

The stated conclusion — "every tangent cone is a noncollapsed Ricci-flat metric cone `C(Y)` with `Y` a **smooth** `(n−1)`-manifold satisfying `Ric_Y = (n−2)g_Y`" — uses an argument that is dimension-4-specific. The dimension-4 argument (CN §8.2) is: a singular point `y ∈ Y` would make the whole ray through `y` singular in `C(Y)`, a set of Hausdorff dimension 1, contradicting `dim S ≤ 0`. For `n ≥ 5`, `dim S ≤ n−4 ≥ 1`, so a 1-dimensional singular ray is permitted and the argument does not carry. CN's own reference list contains the relevant evidence in this direction: [HN14], "Isolated Einstein Singularities with Singular Tangent Cones."

Correct general statement: every tangent cone at `p ∈ S` is a noncollapsed metric cone `C(Y)` with `Y` compact, `diam(Y) ≤ π`; `C(Y)` is smooth and Ricci-flat away from its own singular set, of dimension `≤ n−4`; and `Ric_Y = (n−2)g_Y` on the smooth part of `Y`. Only at `n = 4` does this force `Y = S³/Γ` with `sec ≡ 1`.

This correction propagates: the "smooth `(n−1)`-manifold" phrasing in B(d) is what makes the note's §6 statement "the ALE bubble sees only its own geometry" look dimension-free, whereas the ALE/orbifold structure it relies on is currently available only in dimension 4.

### 2.3 Where Theorem B sits logically

Theorem B's hypothesis is `δ_i → 0`, while the target `P_n^+` asks for a fixed dimension-only threshold `δ_n`. These match only through a contradiction-plus-compactness setup: assume no `δ_n` exists, take counterexamples `(M_i,g_i)` with `δ_i → 0` and no Einstein metric on `M_i`; the theorems then produce a contradiction for large `i`. Under this reading, the note's "Regime (I) — Closed" is genuinely closed: if `S = ∅`, the limit `X` is a smooth closed Einstein manifold and CN Theorem 8.1 (harmonic radius plus GH closeness ⇒ diffeomorphism) makes `M_i ≅ X` for large `i`, contradicting non-existence. Stating the contradiction frame once removes an apparent mismatch between "sequence" statements and the fixed-threshold target.

---

## 3. Sha–Yang dichotomy

### 3.1 A quantifier gap in the proof

The proof reads: "Suppose (A) fails: for each `ε>0`, there exists `k(ε)` and `g_{k(ε)}` with `δ_+ < ε` … Since `b_2(M_{k_j}) = 2k_j → ∞`, this is a contradiction."

Failure of (A) means `inf_k δ_+(M_k) = 0`. That is compatible with two situations:

- (i) `δ_+(M_{k_j}) → 0` along `k_j → ∞` — the intended one;
- (ii) `δ_+(M_{k_0}) = 0` for a **fixed** `k_0`, i.e. metrics `g_j` on one fixed manifold with defect `→ 0` and the infimum not attained.

In situation (ii) the `b_2 → ∞` contradiction is unavailable, because `b_2(M_{k_0})` is constant, and Theorem A yields nothing (one diffeomorphism type is consistent with finiteness). So the conclusion "necessarily `Vol → 0`" is not derived in that case; instead Theorem B would apply and give a possibly singular Einstein limit — which is the substantive regime, not a contradiction. As stated, "exactly one of the following holds" is therefore not established.

Repair, with the same inputs:

> **(A′)** `liminf_{k→∞} δ_+(M_k) > 0`; or **(B′)** there are `k_j → ∞` and metrics `g_j` on `M_{k_j}` with defect `→ 0`, and for every such sequence `Vol(M_{k_j},g_j) → 0`.

The "`Vol → 0`" half of (B′) is then correct: if `limsup Vol = c > 0`, a subsequence has `Vol ≥ c/2`, and the `b_2` bound of §1.4 (or Theorem A) contradicts `b_2 = 2k_j → ∞`. ✓

### 3.2 `δ_+` needs its normalization stated, or "Vol → 0" is not well posed

Two points:

- **Reference metric.** `‖Ric_g − g‖_{L^∞,op}` must specify the metric with respect to which the operator norm is taken. Taking it with respect to `g` itself, and letting the infimum range over all metrics (hence over all rescalings `λg`), makes `δ_+` scale-invariant: `inf_{λ>0} ‖Ric_g − λg‖_{op,λg} = sup_x max_i|λ_i(x)/λ − 1|` minimized over `λ`, which equals `(P−1)/(P+1)` with `P = sup λ_max / inf λ_min` the global Ricci pinching ratio. That is the right invariant and matches the scale-invariant content of the Yau-26 hypothesis (`c g ≤ Ric ≤ C g` is only a condition on `C/c`).
- **Scale fixing for the volume statement.** Precisely because `δ_+` is scale-invariant while `Vol` is not, the conclusion "`Vol → 0`" is meaningful only for metrics already normalized so that `Ric ≈ g` (equivalently `λ = 1`). Without that sentence the collapsing alternative has no content. With it, note also the ceiling `Vol ≤ 24π²/(1−δ)²`, so the collapsing alternative concerns a bounded interval `(0, 24π²/(1−δ)²]`.

Notation: `δ_+` is defined as a manifold invariant (infimum over metrics) and then applied to metrics (`δ_+(g_j)`). Two symbols would prevent confusion.

### 3.3 Sha–Yang is not the witness for the upper bound being load-bearing; Perelman is

§2 argues that one-sided `Ric ≥ (n−1)K` does not give finiteness, citing Sha–Yang's `Ric > 0` metrics on `#_k(S²×S²)`. As an argument this is incomplete: `Ric > 0` on a compact manifold can always be normalized to `Ric ≥ 3g` by shrinking, but shrinking also shrinks the volume, so the family may be collapsing — in which case it is perfectly consistent with a finiteness theorem that assumes noncollapse. What is needed is a family with *simultaneously* normalized lower Ricci bound, bounded diameter, volume lower bound, and unbounded `b_2`.

The supplied CN text names exactly that witness, in §9 after Question 9.3: "Examples of Perelman show that if the 2-sided bound on the Ricci tensor is weakened to a lower bound, then the answer is [not affirmative]." So the load-bearing-ness of the upper Ricci bound should be attributed there, and Sha–Yang retained only as the source of `Ric > 0` metrics on the family whose `b_2 = 2k` supplies the topological input.

A related sentence in §2 also needs adjustment: "Cheeger–Colding theory with only lower Ricci gives codimension-2 regularity." CN's introduction is more precise: with only a lower bound one has the stratification `dim S^k ≤ k` and the singular set need not even be closed; codimension-2 *regularity* already uses the two-sided bound, via [ChCo1] combined with the [A90] ε-regularity. The upgrade supplied by CN 1.4 is from codimension 2 to codimension 4 under the same two-sided hypothesis.

### 3.4 A falsifiable consequence worth extracting

Theorem A (or the weaker `b_2` bound of §1.4) makes a testable prediction about explicit metrics: **any family of closed oriented 4-manifolds with `b_2 → ∞`, bounded diameter and uniform volume noncollapse (after normalizing `inf λ_min = 1`) must have normalized Ricci pinching bounded away from `0`.** Applied to Perelman-type noncollapsed families with `b_2 → ∞`, this forces `δ_+ ≥ δ_0(v) > 0` for those explicit metrics. Computing or estimating the Ricci eigenvalue spread in such a doubling/gluing construction would calibrate how large any dimension-only `δ_4` could possibly be, and would confirm that Theorem A is not vacuous on the family it is meant to constrain. Nothing in the current data files touches this.

---

## 4. ε-regularity erratum

Checked directly against the source; the erratum is correct.

- **CN Theorem 6.1** as printed: "There exists `ε(n,v)>0` such that if `M^n` satisfies `|Ric| ≤ ε`, `Vol(B_1(p)) > v > 0`, and `d_GH(B_2(p),B_2(0)) < ε` where `0` is a vertex of `R^{n−3}×C(Y)`, then `r_h(p) ≥ 1`. Consequently, if `M^n` is Einstein, `sup_{B_1}|Rm| ≤ 1`." So it is an ε-regularity theorem for bounded (indeed small) Ricci; the Einstein hypothesis enters only for the pointwise curvature conclusion. ✓
- **CN Remark 1.11** as printed: replacing Einstein by a bound on `|∇Ric|` gives the same conclusion; "if we only assume a bound on the Ricci curvature, then (1.10) holds with the regularity scale `r_x` replaced by the harmonic radius `r_h`." So the note's statement — pointwise `r_x` needs Einstein or `∇Ric`, `r_h` needs only bounded Ricci — is exactly the source's. ✓

Two hypotheses must travel with these theorems and are absent from the note's §5–6 usage:

1. **Small-Ricci rescaling.** Theorem 6.1 assumes `|Ric| ≤ ε(n,v)`, and Theorem 8.6 assumes `|Ric_{M^4}| ≤ 3δ(v,ε)`. At unit scale we only have `|Ric| ≤ 1+δ`, which is not small. The applications are therefore at scales `r ≲ √(ε/(1+δ))`, using `|Ric_{r^{-2}g}| = r²|Ric_g|`. CN do exactly this in §7.1: "by rescaling, we may regard the ε-regularity theorem as stating that if `x` is `(n−3,ε,2r)`-symmetric, then `r_h > r`."
2. **Volume-ratio near-constancy, at all but finitely many scales.** Theorem 8.6 requires `|𝒱^δ_4(p) − 𝒱^δ_{1/4}(p)| < δ`. Lemma 8.15 / Corollary 8.21 give `|T^δ|(x) ≤ N(v,δ)`: the hypothesis holds at all but `N` scales, not at a prescribed scale. Any construction that needs the annular normal form at a *chosen* scale must first select a good scale from this finite complement.

Two source-alignment items for §5/§8:

- **The cleanest citation for dimension-4 orbifold limits is CN Corollary 8.85**, which is in the supplied text and is not in the note's §8 list: "Let `(M_j^4,d_j,p_j) → (X,d,p)` be a GH limit of manifolds with `|Ric| ≤ n−1` and `Vol(B_1(p_j)) > v`. Then `X` is a Riemannian orbifold with at most `c(v)` singular points." Together with Theorem B Step 3 (the limit is Einstein on the regular part) and CN 1.13 (`L²` curvature), this gives Theorem C(a)(b) more directly than routing through Theorem 8.6's annuli.
- **A constant in the source's §8.2 is inconsistent, and the note is the one that is right.** CN's §8.2 proof prints "since `C(Y)` is a metric cone over `Y`, we must have `Ric_{Y³} = 3g^Y`", then immediately concludes `Y = S³/Γ` with `sec ≡ 1`. Ricci-flatness of `dr² + r²g_Y` over an `(n−1)`-manifold requires `Ric_Y = (n−2)g_Y`, i.e. `Ric_Y = 2g_Y` at `n=4`; and unit `S³` has `Ric = 2g`, whose cone is flat `R⁴`. So `3g^Y` is a misprint (or conversion artifact) and the note's `Ric_Y = 2g_Y` in Theorem C(c) and `(n−2)g_Y` in Theorem B(d) are correct. CN's parallel `n−3` computation is internally consistent (cone over a surface: `Ric_Y = g_Y`, Gauss curvature 1). This discrepancy should be recorded in the note so that a later reader does not "correct" the note toward the printed constant.

---

## 5. Blow-up Ricci scaling, and a power-of-`t` inconsistency in the bridge sketch

### 5.1 The scaling is correct, in both norms

`Ric` is invariant as a `(0,2)`-tensor under constant rescaling: `Ric_{cg} = Ric_g`. Hence for `ĝ = t^{-2}g`,
```
|Ric_ĝ|_{op,ĝ} = sup_v |Ric_g(v,v)| / (t^{-2} g(v,v)) = t² |Ric_g|_{op,g},
|Ric_ĝ|_{HS,ĝ}² = ĝ^{ik}ĝ^{jl}Ric_{ij}Ric_{kl} = t⁴ |Ric_g|²_{HS,g}.
```
So `|Ric_ĝ| ≤ t²(1+δ) → 0` in either norm ✓, and the `δ`-dependent part of that is `t²δ`, so the smallness at bubble scale survives even for `δ` of order `1/2`. The note's structural point is correct.

One distinction to keep explicit, because the bridge design depends on it: the rescaled metric is close to being *Ricci-flat*, but far from Einstein-with-constant-1, since `Ric_ĝ − ĝ = Ric_g − t^{-2}g` has `|·|_{op,ĝ} = |t²Ric_g − g|_{op,g} ≈ 1`. The `δ`-information therefore lives at the original scale, which is where §6 correctly places the pairing `∫⟨Ric(g_i) − g_i, φ_j⟩`.

### 5.2 `t` means two different things in §4 and §6

- §4 Step 4: `ĝ_i = r_i^{-2}g_i`, `|Ric_{ĝ_i}| ≤ r_i²(1+δ)` — here `r` is a length.
- §6 item 4: `|Ric_{ĝ_i}| ≤ t_j²(1+δ_i)`, while §6's metric convention is `g_i ~ t_j g_flat` and `dμ_{g_i} ~ t_j² dμ_flat` — the latter two are consistent with `t = (length)²` in dimension 4 (Step 8 also used `g_t = t(g_{EH} + …)`). Under that convention the correct statement is `|Ric_ĝ| ≤ t_j(1+δ)`, not `t_j²`.

The conclusion `Obstruction = O(δ)` is unaffected because it comes from dividing an `O(δ t)` pairing by an assumed `O(t)` leading term, but any actual derivation of the flux identity will be sensitive to these powers, so the convention should be fixed once and used everywhere.

### 5.3 A substantive inconsistency in the test-field design

§6 computes `‖φ_j‖_{L¹(g_i)} = O(t_j)` from "`φ_0` a **bounded** symmetric `(0,2)`-tensor on `R⁴/Γ_j`" transported and cut off. Its closing paragraph then states "the test field must be **quadratic** in cone coordinates" (paired against the `ρ^{-4}` Eguchi–Hanson deviation). These two are incompatible, and the difference is not cosmetic: with `|φ_0|_flat ~ ρ²` the `L¹` mass is dominated by the outer part of the annulus and is `O(1)`, not `O(t)`, so the estimate `|∫⟨Ric−g,φ⟩| ≤ δ‖φ‖_{L¹}` no longer scales like `δ t` and dividing by `t` yields nothing.

What this indicates about the object to be constructed: the leading obstruction coefficient should be extracted as a surface term across the neck sphere (the Komar/flux route already sketched in Step 8 §4), with the test tensor *decaying* at the neck so that its `L¹` mass concentrates at the bubble scale, while the ambient curvature `R_+(p)` enters through the flux rather than through a growing test field. Reconciling §6's two statements is a prerequisite for the identity (4.1) of Step 8 to have the stated error size.

### 5.4 The per-bubble energy quantum in the JSON

`step9_finiteness_constants.json` carries the note `"ALE bubble energy ≥ 8π²/|Γ|; EH gives 12π²"`, but the arithmetic in the same records divides the Weyl lower bound by `12π²` (`k=5`: `72.0988π²/12π² = 6.0 → 6`; `k=100`: `1592.1/12 = 132.7 → 132` ✓). The correct accounting supports the divisor, not the stated inequality. Gauss–Bonnet for a Ricci-flat ALE 4-manifold `X` asymptotic to `R⁴/Γ` gives
```
χ(X) = (1/8π²)∫_X |Rm|² + 1/|Γ|  ⟹  ∫_X|Rm|² = 8π²(χ(X) − 1/|Γ|).
```
Eguchi–Hanson: `χ(T^*S²) = 2`, `|Γ| = 2`, so `∫|Rm|² = 8π²(3/2) = 12π²` ✓, matching the JSON's parenthetical. For minimal resolutions, `χ = 1 + r` with `r ≥ 1`, so every nontrivial bubble carries `∫|Rm|² ≥ 12π²`; the only zero-energy case is flat `R⁴`. So the text's `8π²/|Γ|` should be replaced by `8π²(χ − 1/|Γ|) ≥ 12π²`, and the bubble counts stated as "at least `⌈lower bound / 12π²⌉` bubbles if all bubbles are Eguchi–Hanson-type", i.e. an upper estimate of the count's sharpness.

A quantitative addition that strengthens the Weyl stress test: combining Step 8's identity `∫|Rm|² = 8π²χ + (5/2)∫|E|² + (1/8)∫s²` with `|E|² ≤ 4δ²`, `s² ≤ 16(1+δ)²` and `Vol ≤ 24π²/(1−δ)²` gives `∫|Rm|² = 8π²χ + O_δ(1)`, while (2.4) gives `∫|W|² ≥ 8π²χ − O_δ(1)`. So for tightly pinched positive metrics with large `χ`, *essentially all* curvature energy is Weyl: `∫|W|² = 8π²χ(1 + O(1/χ))`. For `#_k(S²×S²)`, signature `τ = 0` forces `∫|W^+|² = ∫|W^-|² = 4π²χ + O_δ(1) = 8π²(1+k) + O_δ(1)`. That is a sharper benchmark for candidate constructions than the total-Weyl bound alone, and it is a self-dual/anti-self-dual balance condition that any bubble-tree accounting must respect.

---

## 6. What the positive branch still lacks, stated as scientific substance

1. **A mechanism forbidding collapse under positive pinching.** Nothing in Theorems A/B, the CGB budget, or the CN toolkit touches this. The relevant source-level facts are: CN Example 2.16 (Anderson [A93]) exhibits `M_j^4 → T³` with `diam ≤ 1`, `|Ric| ≤ ε_j → 0`, `Vol → 0`, `b_2 → ∞` — collapse with bounded Ricci and unbounded topology does occur in dimension 4, though those metrics are almost Ricci-flat and their scale-invariant pinching ratio does not go to 1. So the only additional input available in the positive branch is that `Ric ≈ +g` forces `diam ≤ D`, `Ric > 0`, `b_1 = 0`, `χ ≥ 2`, finite `π_1`. Whether pinching itself yields a volume lower bound is the load-bearing unknown, and the note's §9 assessment of this is accurate. A concrete discriminating computation: exhibit or exclude a sequence with global Ricci pinching ratio `→ 1` and `Vol → 0` after normalization; Berger-type collapses are ruled out precisely because one Ricci eigenvalue degenerates, so the question is whether pinching-preserving collapse models exist at all in dimension 4.
2. **Exclusion of bubbling needs more than first-obstruction vanishing.** The bridge, if built, yields "first obstruction `= 0`", e.g. `det R_+ = 0` at each concentration point. Step 8 §3 already established that `det R_+ = 0` is strictly weaker than Kähler-Einstein (the trace-free spectrum `(1/3,0,−1/3)` also satisfies it), so vanishing is not by itself contradictory. Getting from vanishing to "the limit is smooth, hence Regime (I) applies" requires the higher-order obstructions and the Hermitian/Kähler rigidity results, all of which are exact-Einstein statements. This is the honest shape of Regime (II), and it means the bridge is necessary but visibly not sufficient.
3. **For `n ≥ 5` the topological-finiteness route is unavailable in principle, not merely unproved.** The supplied CN §9 states: finite diffeomorphism type "in higher dimensions … is too much to hope for; see [HN14] where noncollapsed Calabi-Yau manifolds of real dimension `≥ 6` are constructed with unbounded third Betti number", and CN's Question 9.3 (is `b_2` bounded under `|Ric| ≤ n−1`, `diam ≤ D`, `Vol(B_1) > v`?) is posed as open. So any all-dimensional positive-branch mechanism must be independent of both finiteness and `b_2` bounds; the dimension-4 CGB budget (`χ`, `∫|W|²`, signature) has no counterpart. Theorem B(a)–(c) remains the correct all-dimensional structural statement, with B(d) restricted as in §2.2 above.
4. **What Theorem A does and does not add.** It is a corollary of CN 1.12/8.64 plus Myers and Bishop–Gromov, with no new analysis and non-explicit constants. Its scientific value is in the translation — the two-sided Yau-26 hypothesis is *exactly* CN's hypothesis, with no Einstein assumption anywhere in the chain (verified for Theorems 1.4, 1.12, 1.13, 6.1, 8.1, 8.4, 8.6, 8.64, 8.79 against the source text) — and in the falsifiable prediction of §3.4. Presenting it as a corollary with that emphasis is both accurate and more useful than presenting it as an independent theorem.