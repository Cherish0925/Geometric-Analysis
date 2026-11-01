# TTCS Independent Branch Record

```json
{
  "step_id": 15,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex",
    "Sessions/S0910A03/workspace/notes/step4_weyl_profile_and_bubble_restriction.tex",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md",
    "Sessions/S0910A03/workspace/scripts/verify_L2_completion_square_chain.py"
  ]
}
```

## Task

Verify the following proposed L² completion-square chain for the Yau Problem 26 negative-branch program on a fixed critical Ishida-LeBrun 4-manifold M.

CHAIN CLAIM: For ANY Riemannian metric g on M (not just the original near-Einstein sequence), the following hold:
(a) Chern-Gauss-Bonnet: I - R = 2A/3 where I = (4pi²)⁻¹∫(s²/24 + 2|W⁺|²), R = (8pi²)⁻¹∫|Ric₀|².
(b) Seiberg-Witten monopole: K ≥ A where K = (72pi²)⁻¹∫(s - √6|W⁺|)².
(c) Completion square: ∫(s + 8√6|W⁺|)² ≤ 864pi²R ≤ 108∫|E|² where E = Ric + g.
(d) Consequence: ∫(|W⁺| - 1/(2√6))² ≤ C∫|E|² with C ≈ 0.41.

VERIFY EACH STEP. In particular:
1. Is (b) really metric-independent? The SW inequality involves metric data; check that the final bound K ≥ A uses only topological invariants after minimizing over metrics.
2. Does the chain from R → calibrated Weyl profile require volume control as an additional input? Or is the bound (d) truly volume-independent?
3. The CRITICAL QUESTION: After applying a normalized cutoff flow ∂_t g = -2χ²(Ric+g), the evolved metric g(t) is still on M. Does the chain apply to g(t) without additional hypotheses? What if the flow develops singularities or degeneracies?
4. For the forbidden-germ contradiction (Step 6), we need not just |W⁺| ≈ 1/(2√6) but the specific eigenvalue structure (-1/6, 1/12, 1/12). Does the L² Weyl modulus convergence suffice to extract eigenvalue information, or is additional compactness needed? What is the MINIMAL additional input beyond ∫|E|² → 0 to reach the contradiction?

## Output

## Verification Memo — L² completion-square chain on the critical Ishida–LeBrun family (D = A/3)

I reproduced every algebraic and topological step and checked the four verification questions. The chain (a)–(d) is mathematically correct and genuinely metric-independent. The two computational scripts referenced (`verify_L2_completion_square_chain.py`, and the germ computation in Step 6) are sound up to one cosmetic arithmetic slip. The substantive gaps are exactly where the notes place them, and I sharpen them below.

---

### Verification of the four steps

**(a) Chern–Gauss–Bonnet, `I − R = 2A/3`.** Correct and purely topological. With
χ = (1/8π²)∫(|W⁺|²+|W⁻|² − ½|Ric₀|² + s²/24), τ = (1/12π²)∫(|W⁺|²−|W⁻|²),
one gets 2χ+3τ = (1/4π²)∫(s²/24 + 2|W⁺|²) − (1/8π²)∫|Ric₀|² = I − R. On this family 2χ+3τ = A − D = 2A/3. This holds for every smooth metric; no analytic input.

**(c) Completion square.** The algebraic identity
27(s²/24 + 2w²) − (s−√6 w)² = ⅛(s+8√6 w)²
I expanded independently: both sides equal s²/8 + 2√6 sw + 48w². Integrated it reads ⅛∫(s+8√6|W⁺|)² = 36π²(3I − 2K), i.e. ∫(s+8√6|W⁺|)² = 288π²(3I−2K). With I = 2A/3 + R and K ≥ A, 3I − 2K = 2A + 3R − 2K ≤ 3R, so ∫(s+8√6|W⁺|)² ≤ 864π²R = 108∫|Ric₀|² ≤ 108∫|E|² (using |Ric₀| = |E₀| ≤ |E|, since E = Ric + g is a pure-trace shift of Ric). Every step checks.

**(d) Weyl-modulus bound.** Setting Δs = s+4 = tr_g E = τ and Δw = |W⁺| − 1/(2√6), the shift 8√6·1/(2√6)=4 gives s+8√6|W⁺| = Δs + 8√6 Δw exactly. From 384∫Δw² = ∫(Δs+8√6Δw)² − ∫Δs² − 16√6∫ΔsΔw and |τ| ≤ 2|E| (so ∫Δs² ≤ 4∫|E|²), the quadratic 384t² − 32√6 t − 108 ≤ 0 in t = (∫Δw²/∫|E|²)^½ gives t ≤ (32√6 + √172032)/768 ≈ 0.6421, hence C = t² ≈ **0.4123**. This matches the stated C ≈ 0.41. **The bound is a pure ratio of two L² integrals — no volume enters.**

*Cosmetic issue:* an in-code comment prints the discriminant as “6144 + 166272 = 172416,” but the executed variable is `32**2*6 + 4*384*108 = 6144 + 165888 = 172032`. The mis-typed 166272/172416 never feeds the result; the reported C is computed from 172032 and is correct. Fix the comment so the source reads consistently.

---

### Q1 — Is (b) `K ≥ A` metric-independent?

**Yes, and the mechanism is worth stating precisely.** The primitive LeBrun estimate K ≥ (a⁺)² is metric-dependent on both sides: K = (72π²)⁻¹∫(s−√6|W⁺|)² and (a⁺)² = ‖a⁺‖²_g (self-dual projection of the class a in the metric's period point). Three facts convert this into a metric-independent A:

1. **`(a⁺)² ≥ a²` always.** a·a = ‖a⁺‖² − ‖a⁻‖², so ‖a⁺‖² = a² + ‖a⁻‖² ≥ a².
2. **Sign-averaging cancellation.** For a_{ε,η} = Σε_j c_j + Ση_ℓ E_ℓ with c_i·c_j = 0 (disjoint summands) and c_j·E_ℓ = 0, averaging over independent signs kills cross terms: Av(a⁺)² = Σ‖c_j⁺‖² + Σ‖E_ℓ⁺‖² = A + Σ‖c_j⁻‖² + Σ‖E_ℓ⁺‖² ≥ A, with A = Σc_j²(X_j) purely topological. This is equation (3) of Step 3, and I confirm the intersection-orthogonality is what forces the cross terms to vanish.
3. Hence for **every** metric there is a sign vertex with (a⁺)² ≥ Av ≥ A, so K ≥ max_signs(a⁺)² ≥ A.

The one non-elementary input this rests on is that each a_{ε,η} is a genuine monopole class, i.e. **Bauer–Furuta stable-cohomotopy nonvanishing for the connected sum** #X_j # N. Monopole classes are defined by nonvanishing SW/BF invariants and are diffeomorphism-invariant, so they persist for all metrics. Provided that source input holds (and b⁺ ≥ 2, so LeBrun's Weitzenböck estimate is valid), K ≥ A holds uniformly over the space of smooth metrics on M. This is the correct reading: (b) is metric-independent as a consequence per-metric, not because K itself is topological.

---

### Q2 — Does R → calibrated profile need volume as extra input?

**Bound (d) is volume-free.** It is a homogeneous ratio ∫Δw² ≤ C∫|E|²; both integrals scale identically, so no volume normalization is required.

**The numerical profile is a two-tier statement, and only the second tier uses volume.**
- Tier 1 (volume-free): from K ≤ (3/2)I (completion-square nonnegativity), K ≥ A, and I = 2A/3 + R, one gets A ≤ K ≤ A + (3/2)R, so R → 0 forces K → A, I → 2A/3, and the residual ∫(s+8√6|W⁺|)² → 0. The **split** S → 16A/27, W → 2A/27 then follows from the L² relation s ≈ −8√6|W⁺| alone (giving S ≈ 8W and S + W = I → 2A/3). All of this needs only ∫|E|² → 0.
- Tier 2 (the numerical volume, eq. (6) Vol → 32π²A/9): this is *derived*, but the derivation implicitly uses ∫|E|² → 0 **absolutely** on fixed A. Concretely ∫(s+4)² = ∫τ² ≤ 4∫|E|² → 0 and S = (96π²)⁻¹∫s²; the quadratic 16 Vol ≤ ∫s² + 8(∫(s+4)²)^½ Vol^½ then bounds Vol and pins it. On fixed A this closes with no circularity. **If topology varies (A_i → ∞), one needs ∫|E|² = o(A) and all statements become A-normalized**, exactly as Step 3 and Step 6 §"varying topology" record. The distinction is real and correctly flagged.

So: (d) never needs volume; the profile magnitude needs only ∫|E|²→0; only the explicit constant 32π²A/9 uses absolute (fixed-A) smallness.

---

### Q3 — Does the chain apply to the cutoff-flow metric g(t)?

**The chain itself imposes no flow hypothesis whatsoever.** (a)–(d) hold for *any* smooth Riemannian metric on M: (a) is topological, (b) holds for every metric via Q1, (c)–(d) are algebraic. If g(t) is a smooth metric on the closed M, the chain applies verbatim. Where g(t) is not a smooth metric — a singular time, or the degeneracy locus χ = 0 of ∂_t g = −2χ²(Ric+g) — the chain conclusions are simply not asserted there, because there is no smooth metric to feed in.

**But the framing in Part 6 over-attributes work to the flow.** The profile already holds at t = 0: ∫|E(0)|² ≤ δ_i² Vol = O(Aδ_i²) → 0, so (d) gives ∫(|W⁺|−1/(2√6))² → 0 for the original sequence with **no flow at all**. Therefore the flow does *not* exist to improve the L² profile — that is already optimal. Whatever the flow is for, it is not the chain.

The genuinely unresolved analytic object is exactly what Part 6 admits: **propagating a small ∫|E(t)|² through the flow is not established.** The Kato subsolution (∂_t−Δ)|E|² = −2|∇E|² + 4R_{ikjl}E_{ij}E_{kl} has reaction ≤ |Rm||E|², and |Rm| on a Ric ≈ −g metric is only L²-bounded (‖Rm‖₂ = O(A^½) via ∫|W|² = O(A)), not L^∞. A Gronwall with C/t (from Li's |Rm(t)| ≤ C/t) diverges as recorded. The three-region decomposition (plateau via Cor. 3.5, frozen exterior, transition) leaves the transition-region L² growth as the open item, and this is stated correctly. My independent point: since the profile is already established at t = 0, the flow's only legitimate purpose is **regularity for the pointwise/eigenvalue argument of Q4** — and there its need collides with the collapse conclusion (below).

---

### Q4 — Minimal input beyond ∫|E|² → 0 to reach the forbidden-germ contradiction

**L² convergence of |W⁺| controls only the magnitude Σλ² = |W⁺|², never the eigenvalue splitting.** Many trace-free spectra on Λ⁺ give |W⁺|² = 1/24. The germ contradiction needs the specific spectrum (−1/6, 1/12, 1/12), which is fixed by three data: (i) trace-free (automatic for W⁺), (ii) magnitude 1/24, and (iii) a **double top eigenvalue with a simple lowest eigenvalue**. From (i)+(iii), a = −2b, and 6b² = 1/24 gives b = 1/12, a = −1/6 uniquely. Item (iii) is not visible to ∫|W⁺| data; it is precisely the almost-Kähler / lowest-eigenline structure of LeBrun Prop. 3.8.

So the minimal additional inputs beyond ∫|E|² → 0 are:

1. **A volume lower bound at some fixed scale at a point (noncollapse).** Combined with the *already-available* |Ric| ≤ 3, Cheeger–Naber gives a harmonic-radius lower bound and hence C^{1,β}_loc / W^{2,p}_loc convergence to a smooth limit g_∞ with Ric = −g_∞, and (from the absolutely-vanishing deficits restricted to the chart) the pointwise values s_∞ = −4, |W⁺_∞| = 1/(2√6). Note this uses bounded Ricci, **not** bounded Rm — so a flow is not needed to obtain the smooth Einstein limit *if* a noncollapsed ball exists.

2. **Convergence of the selected SW monopole harmonic self-dual form to a nonzero limit H_∞ in the lowest W⁺-eigenline.** This is the carrier of item (iii): via the amplitude/projection defects → 0 and elliptic compactness, H_∞ ≠ 0 sits in the lowest eigenline and the trace-free 3×3 equality case forces the double eigenvalue. The specific limiting amplitude |H_∞| = 3/(4√2 π) depends on the SW normalization and is not independently checkable from the supplied material; that constant should be traced to its source, though only H_∞ ≠ 0 is logically load-bearing.

Given 1 and 2, the germ contradiction is internally correct. I verified the Einstein Weitzenböck arithmetic: for the endomorphism identity ∇*∇W⁺ = −(s/2)W⁺ + 6(W⁺)² − 2|W⁺|²I (trace consistent: −6|W⁺|² + 6|W⁺|² = 0), the scalar identity Δ|W⁺|² = 2|∇W⁺|² + s|W⁺|² − 36 det W⁺ follows from ⟨(W⁺)²,W⁺⟩ = tr(W⁺³) = 3 det W⁺. At s = −4, |W⁺|² = 1/24, det W⁺ = −1/864 (and tr(W⁺³) = −1/288 checks against Σλ³), constancy of |W⁺|² forces |∇W⁺|² = 1/16. The projector Lemma independently forces ∇W⁺ = 0 (I confirm equation (3) ω_{ab}∇^aω_{cd} = 0 with ω_a{}^cω_c{}^b = −δ, hence ∇ω = 0). 1/16 ≠ 0 is the contradiction. Solid.

**The decisive point for the program.** Step 6 equation (10) concludes that on a fixed critical manifold noncollapse *fails everywhere at unit scale*: sup_p Vol B₁(p) → 0. Input 1 above therefore cannot be supplied directly — the manifold collapses everywhere while retaining Vol → 32π²A/9, forcing diameter divergence. The germ contradiction is then reachable only after **unwrapping collapsed regions to noncollapsed harmonic charts on local covers while preserving the small pulled-back LeBrun deficit**. That collapse-unwrapping theorem — separating maximal-rank Naber–Zhang collapse, constant-fibre circle models, and singular/fixed strata — is the genuine unresolved geometric object. It is *not* the chain, and it is *not* the 2/3-exponent estimate; it is the same "curvature bootstrap / unwrapping" that Steps 6 and 14 both isolate. This is where the flow route (Step 14) and the collapse route (Step 6) must join, and neither yet closes it.

---

### Summary of the standing of the material

- The completion-square chain (a)–(d) is correct, metric-independent, and volume-free; I reconstructed every identity and constant.
- (b)'s metric-independence rests on Bauer–Furuta nonvanishing plus the sign-averaging cancellation; that dependency should be stated explicitly wherever K ≥ A is used.
- The numerical volume 32π²A/9 is derived under fixed-A absolute smallness; the A-normalized version is the correct form when topology varies.
- The chain transfers to any smooth g(t) trivially; the flow does not improve the (already optimal) L² profile, and propagating small ∫|E(t)|² through the reaction term |Rm||E|² (|Rm| only L²) is unresolved.
- The germ contradiction is arithmetically correct but needs, beyond ∫|E|² → 0, (i) noncollapse at a point and (ii) nonvanishing SW form in the lowest eigenline to pin the double-eigenvalue spectrum. Step 6 shows (i) is unavailable (universal collapse), so the operative unresolved object is a collapse-unwrapping theorem preserving the pulled-back deficit — the single item on which the four-dimensional Ric = −g branch of this program now turns.

One item to fix mechanically: the discriminant comment (166272/172416) in `verify_L2_completion_square_chain.py`; the executed value 172032 and C ≈ 0.412 are right.