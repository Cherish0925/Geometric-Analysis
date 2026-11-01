# TTCS Independent Branch Record

```json
{
  "step_id": 17,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step17_support_scale_li_bootstrap.md",
    "Sessions/S0910A01/workspace/scripts/step17_sobolev_energy_cancellation.py",
    "Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md"
  ]
}
```

## Task

Verify the support-scale-consistent cutoff-flow construction for the 4D negative LeBrun branch. The construction claims to resolve the quantifier mismatches from Step 16 by choosing ALL radii as fixed multiples of the Li scale r_*. The key mathematical claims to verify are: (1) The Vitali/thinning construction produces disjoint supports B_{4r_*}(p_j) whose plateaux B_{3r_*}(p_j) are separated, with a positive volume fraction of bootstrap domains B_{r_*}(p_j). (2) For every center y in B_{2r_*}(p_j), the maximal function at p_j controls the Li dimensionless quantity: epsilon_y(r_*) = r_*^4 * fint_{B_{r_*}(y)} |Rm|^2 <= C K_0 r_*^4 which is small for small r_*. (3) The Li covering argument (Theorem 3.4) works on the plateau B_{3r_*}(p_j) because all covering balls B_{r_*}(y_k) with y_k in B_{3r_*/2}(x) stay inside the plateau when x in B_{r_*}(p_j). (4) THE CRITICAL CLAIM: The 4D Sobolev-energy product C_S * ||Rm||_{L^2(support)} is O(r_*^2) and absorbs the cubic/defect reaction terms in BOTH the Rm energy inequality and the E energy inequality on the transition, even though |Rm| is not pointwise bounded there. This uses the 4D critical Sobolev embedding where the Sobolev constant C_S is dimensionless. (5) The modified Li bootstrap on the full support (including transition) closes because the transition terms add only a linear C r_*^{-2} growth rate, giving bounded exponential factor over time theta r_*^2. (6) Metric comparability holds because |partial_t g| = 2 chi^2 |E| <= 2 delta, and total drift over theta r_*^2 is O(delta r_*^2). Check all six claims for mathematical correctness. Identify any circularity, wrong exponent, missing hypothesis, or gap.

## Output

## Verifier memo — support-scale cutoff-flow construction (Step 17, S0910A01), six-point check

**Summary judgment.** The construction genuinely improves on the withdrawn Step 15 argument: making every radius a fixed multiple of the Li scale `r_*` makes the *plateau interior* argument close cleanly, and the final numbers for the absorption product and the terminal defect are the right order. Points (1) and (2) hold up (with two harmless constant corrections). Point (4)'s final estimate `= O(r_*^2)` is correct, but its stated *mechanism* is wrong in the collapsing regime that is the entire reason for invoking Li — the correct mechanism is a collapse-cancellation, not a dimensionless Euclidean Sobolev constant. Point (3) as literally written does not hold (the covering balls poke past the plateau by `~r_*/2`), but is repairable by a radius relabeling. Points (5) and (6) on the transition annulus are not established: they rest on a circle in which each of {absorption, Sobolev validity, metric equivalence, pointwise `χ²E` control} is asserted using the others. This is exactly the un-closed continuation package that the parallel S0910A03 Step 16 note states explicitly, and Step 17 does not break it. Below, point by point.

---

**(1) Vitali + thinning, disjoint supports, positive-fraction bootstrap set — holds.**
- The separation arithmetic is correct: `d(p_j,p_k) > 7r_*` makes any point of `B_{3r_*}(p_j)` at distance `> 4r_*` from `p_k`, so `Π_j ∩ Ω_k = ∅`. The `3+4=7` bookkeeping is right.
- Good-set volume: weak-type (1,1) gives `Vol(G_i^c) ≤ C(4)K_1 A_i/K_0`, and `K_0 = 2C(4)K_1/c_vol` yields `Vol(G_i) ≥ Vol(M_i)/2`. `K_0` is fixed from Noether energy `K_1` and calibrated `c_vol`; `r_*` is then derived. Definitional order is consistent — `K_0` is chosen before `r_*`, no self-reference.
- Because `r_* ≈ 3×10⁻³` (from `eps_Li=10⁻³`, `K_0≈1.5×10⁴`), `sinh` corrections are negligible and `BG(s)~s⁴` is justified; the thinned fraction `Vol(M)/(2·625·4096)` is a positive fixed number.
- One textual inconsistency: the note writes `BG(7)` in one line and `BG(8)` in the next for the thinning loss. Both are fixed `O(1)`; use `BG(8)=4096` consistently (an unselected center lies within `7r_*` of a selected one, so its Vitali ball sits in `B_{8r_*}`). Harmless.

**(2) Maximal function controls the Li dimensionless energy on `B_{2r_*}(p_j)` — holds, one constant off.**
- `y∈B_{2r_*}(p_j) ⟹ B_{r_*}(y)⊂B_{3r_*}(p_j)⊂B_{4r_*}(p_j)`, and `p_j∈G_i` gives `fint_{B_{4r_*}(p_j)}|Rm|² ≤ K_0`, hence `∫_{B_{4r_*}}|Rm|² ≤ K_0 Vol(B_{4r_*})`.
- The volume-ratio factor is stated as `BG(5)≈625`, but `B_{4r_*}(p_j)⊂B_{6r_*}(y)` (since `d(p_j,y)<2r_*`), so relative Bishop–Gromov gives `BG(6)≈1296`. Factor-of-two constant, does not affect the conclusion `ε_y(r_*)=r_*⁴ fint_{B_{r_*}(y)}|Rm|² ≤ C K_0 r_*⁴`, small. The definition matches Li's Theorem 3.6 scale-invariant quantity `r⁴/Vol·∫|Rm|²`. Fine.

**(3) Li covering stays inside the plateau — as written, does not hold; repairable.**
- The bootstrap quantity `∫_{B_{r_*}(x)}|Rm|²` for `x∈D_j=B_{r_*}(p_j)` is over `B_{r_*}(x)⊂B_{2r_*}(p_j)⊂Π_j` — that part is fine.
- But the *evolution* uses Li's covering `B_{2r_*}(x)⊂∪B_{r_*}(y_k)` with `y_k∈B_{3r_*/2}(x)`, and the reaction is re-expressed as `∫_{B_{r_*}(x)}|Rm|³ ≤ Σ∫_{B_{r_*}(y_k)}φ_k⁴|Rm|³`. The *centers* `y_k` lie in `B_{5r_*/2}(p_j)⊂Π_j` ✓, but the covering *balls* `B_{r_*}(y_k)` reach distance `d(y_k,p_j)+r_* ≤ 7r_*/2 = 3.5r_*` from `p_j`, i.e. they enter the transition annulus `(3r_*,4r_*)` where `χ<1` and the Kato inequality `∂_t|Rm| ≤ Δ|Rm|+C|Rm|²` acquires the `∇²(χ²)*E + ∇(χ²)*∇E` terms of §5.6.
- So the §4 statement "all of Li's covering balls are inside `Π_j`, where the flow is standard" is not correct: interiors leak `~r_*/2` into the transition. This is a small residue of the same inner/outer quantifier issue Step 16 flagged. It is fixable trivially: set `χ=1` on `B_{4r_*}` (larger plateau) with the transition in `[4r_*,5r_*]` and support `B_{5r_*}`, so that for `x∈B_{r_*}(p_j)` the covering stays inside `B_{3.5r_*}⊂{χ=1}`. With the note's stated radii (bootstrap 1, plateau 3, support 4) containment misses by half a Li radius. Recommend re-fixing the radii and re-checking that the thinned separation (§1.2) tracks the enlarged support.

**(4) The critical absorption product — right number, wrong mechanism in the collapsing regime.**
This is the important scientific correction. The final estimate `(Sobolev)·||Rm||_{L²(support)} = O(r_*²)` is correct and *is* collapse-independent, but not for the reason given.

- The note treats `C_S` as the dimensionless Euclidean critical constant (`C_S≈2`), "approaching the Euclidean value for small balls," and multiplies by `||Rm||_{L²}~K_0^{1/2}(4r_*)²` using `Vol(B_{4r_*})≈ω₄(4r_*)⁴`. Both inputs are the *non-collapsed* values. But the LeBrun laboratory here is precisely the *collapsing* case (that is why Li's collapse-free smoothing is invoked at all). Li's own statement is the opposite: the local Sobolev constant `A=C_s(B_r)≤C(r⁴/Vol(B_r))^{1/2}` **grows without bound as `Vol(B_r)→0`.** So on a collapsed ball, `C_S` is not `O(1)`; it is large.
- The correct 4D mechanism is the cancellation, in Li's normalization `(∫f⁴)^{1/2}≤A∫|∇f|²`:
  `∫|Rm||E|² ≤ ||Rm||_{L²} ||E||_{L⁴}² ≤ ||Rm||_{L²}·A·||∇E||_{L²}²`.
  The absorbing quantity is `||Rm||_{L²}·A`, and
  `||Rm||_{L²}·A ≤ (K_0 Vol(B_{4r_*}))^{1/2}·C((4r_*)⁴/Vol(B_{4r_*}))^{1/2} = 16 C K_0^{1/2} r_*²`,
  with `Vol(B_{4r_*})` cancelling *exactly*. So the product is `O(r_*²·K_0^{1/2})` independent of collapse — this is (up to a dimensional constant) the square root of Li's scale-invariant energy `r_*⁴ fint|Rm|²`. The volume shrinks and `A` grows in exact compensation.
- Consequence: the assertion survives, but the write-up and `step17_sobolev_energy_cancellation.py` must be redone with Li's collapse form. The script obtains the right number only because it silently substitutes the non-collapsed volume `ω₄(4r_*)⁴` while holding `C_S=2` fixed; under genuine collapse those two factors move and the product stays put — but the script's stated reasoning does not model that.
- The 4D specialness is real, and worth stating correctly: `n=4` is where the critical exponent `2*=2n/(n-2)=4` coincides with `L^{n/2}=L²`, so Li's scale-and-collapse-invariant `r²(fint|Rm|^{n/2})^{2/n}` reduces to `r⁴ fint|Rm|²`. The script's `n≥5` remarks ("L⁴ supercritical") are muddled: for `n≥5` one uses `|Rm|∈L^{n/2}` and `|E|²∈L^{2*/2}`, not `L⁴`; the honest statement is that the clean cancellation is specific to `2*=L²` at `n=4`. Since the SW/`W^+`/Derdzinski machinery is 4D anyway, restricting to `n=4` is fine, but the dimensional reasoning should be rephrased.
- The same collapse-cancellation, correctly, underlies §5's Corollary 3.5 step: `A^{2/3}Vol(B_{3r_*})^{1/3} ~ r_*^{4/3}` (not `O(1)` as the note says), and at `t=θr_*²` the `r_*` powers cancel to give `|E| ≤ C'δ` on `D_j`. The `δ→0` conclusion is right; the "`~O(1)`" label is the same mis-identification as in (4).

**(5) Full-support bootstrap closure — energy inequality plausible, closure not established.**
- The per-step algebra (extra terms `Cr_*^{-2}δ∫|Rm|` and `Cr_*^{-1}∫|∇E||Rm|`, Young-absorbed into the `E`-dissipation, leaving a linear `Cr_*^{-2}` growth so `e^{Cθ}` over `θr_*²`) is structurally consistent with the coupled system `(C)` in the S0910A03 Step 16 note.
- But closing this over `[0,θr_*²]` on the transition needs the coupled continuation theorem to run: metric equivalence, preservation of the relative Sobolev inequality and finite-overlap constants *along the evolving metric*, and control of `|∇χ|` and the covariant `|∇²χ|` — all simultaneously with `sup R_α ≤ 2ε`. The S0910A03 note states plainly that this package is not proved and, in its §6, that Wang's local-flow paper does not supply it: Proposition 4.9 needs an assumed weighted pointwise `|χ²Rm|_∞`, Lemma 4.11 shows `∇²χ` and `∇(χ²Rm)` evolve coupled, and Theorem 6.3 uses a *global* Sobolev inequality and *global* full-support `L^{n/2}` threshold, which are stronger than the collapsed relative-ball hypotheses here. Step 17's "closes by homogeneity and Gronwall with bounded exponential constant" asserts the conclusion of the missing theorem. Not established.

**(6) Metric comparability on the transition — holds on the plateau, not shown on the transition.**
- On `Π_j` (`χ=1`), once `|Rm|≤C₃/t` is in hand, Corollary 3.5 gives `|E|≤C'δ`, so `|∂_t g|=2|E|≤2C'δ`, and drift over `θr_*²` is `O(δr_*²)→0`. Fine.
- On the transition, §6.1 itself concedes there is no pointwise `|E|` bound; only `L²` control is offered (§5.5, §6.2). But `g_0/2 ≤ g(t) ≤ 2g_0` is a `C⁰` statement, and `|∂_t g|=2χ²|E|` needs at least an `L^∞` (or integrable-in-time pointwise) bound on `χ²E`. An `L²` bound on `E` does not control pointwise metric drift. So (6) is not established on the transition. This is exactly the item S0910A03 §7 isolates and proposes to attack via a Deane-Yang/Moser weighted estimate `‖aE(t)‖_∞ ≤ C_p δ (r²/t)^{2/p}, p>2`, which it states is a *construction target*, not yet derived for the normalized cutoff equation.

---

**The central circle (why (4)+(5)+(6) do not yet stand on the transition).**
The four transition statements depend on one another with no independent entry point:
1. Absorption (4)/(5) needs the relative Sobolev inequality `(∫f⁴)^{1/2}≤A∫|∇f|²` to hold on transition balls *during* the flow.
2. That Sobolev inequality, in Li's Theorem 3.4/3.6, is a hypothesis valid only under metric equivalence `g_0/2≤g(t)≤2g_0` (used for the covering, volume comparison, and constant `A`).
3. Metric equivalence (6) on the transition needs a pointwise/`L^∞` bound on `χ²E`.
4. A pointwise `χ²E` bound needs the `|Rm|≤C/t` bootstrap and Sobolev-type Moser estimates — i.e. (4)/(5) again.

Step 17 asserts each link using the others. The plateau interior escapes the circle (there `χ=1`, the flow is standard, and §4/§5 + Cor 3.5 give `|Rm|≤C₃/t` and `|E|≤C'δ` cleanly — modulo the (3) radius fix). The transition annulus, which necessarily has positive volume wherever `χ` moves `1→0`, does not, and the global `Q_i(h_i)/A_i→0` estimate in §6.2 routes through it. So the "no critical-topology counterexample" conclusion of §8 remains conditional on precisely the un-proved coupled continuation theorem, consistent with S0910A03's more cautious §5 status list and *not* with the confident parentheticals in Step 17 §8.

**What would settle the open items.**
- A relative-Sobolev, finite-overlap version of a Yang/Wang/Fei-He local-flow continuation theorem that jointly outputs, from the collapsed initial data: metric equivalence on the whole active support, preservation of the relative Sobolev constant and overlap number, control of `|∇χ|`,`|∇²χ|` along `g(t)`, `sup_α R_α ≤ 2ε`, and an integrable-in-time pointwise bound on `χ²E`. This is a genuine theorem to prove, not a citation; the source (0911.3104 here, plus Wang) provides the tensor structure but under global Sobolev/`L^{n/2}` hypotheses.
- The `(M_p)` weighted Moser inequality `‖aE(t)‖_∞ ≲ δ(r²/t)^{2/p}, p>2` (S0910A03 §7) would supply the pointwise metric-drift control that link (6) needs and is the most economical way into the circle.
- Rewriting (4) and the verification script in Li's collapse-form `A~(r⁴/Vol)^{1/2}` (not a fixed Euclidean `C_S`), showing the `A·||Rm||_{L²}=O(r_*²)` cancellation explicitly, would make the one genuinely finished mechanism state its own reason correctly.

**Corrections that are immediate and cheap:** enlarge the plateau so the Li covering for `D_j` stays inside `{χ=1}` (fixes (3)); replace `BG(5)` by `BG(6)` in §3 and standardize `BG(8)` in §1.2 (harmless constants); relabel the "`~O(1)`" factors in §5 and §5.5 as the correct `r_*`-powers arising from volume cancellation.