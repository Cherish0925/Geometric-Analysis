# TTCS Independent Branch Record

```json
{
  "step_id": 5,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step5_positive_branch_all_dimensions.md",
    "Sessions/S0910A02/workspace/notes/step4_preceptor_energy_accounting_and_route_review.md",
    "Sessions/S0910A02/workspace/briefing/aligned_research_goal.md"
  ]
}
```

## Task

Verify the noncollapsed positive convergence theorem (Theorem 2) stated in the Step 5 note for Yau Problem 26. The theorem claims: for each n≥2 and v>0, there exists ε(n,v)>0 such that any closed connected smooth Riemannian n-manifold with δ_+(g)≤ε and Vol(M,g)≥v admits an Einstein metric. The proof uses: (1) two-sided Ricci bounds from δ_+(g)≤δ giving (1-δ)g≤Ric≤(1+δ)g; (2) Myers diameter bound giving diam≤D(n,δ); (3) harmonic radius lower bound r_h(n,Λ,D,v)>0 from Ricci bounds + noncollapse + bounded diameter; (4) C^{1,α} Arzelà-Ascoli convergence in harmonic coordinate atlases; (5) passing Ric→g to the limit in distributional sense; (6) elliptic regularity bootstrapping from C^{1,α} Einstein to C^∞; (7) diffeomorphism M_i≅M_∞ for large i from global C^{1,α} convergence. Check: are all steps valid? Are there gaps in the argument (e.g., does step 3 require Anderson's specific theorem or can it be derived from elementary Ricci bounds? Is the elliptic regularity in step 6 standard? Does the global convergence in step 7 really give diffeomorphism?). Is the constant dependence ε=ε(n,v) correct, or does ε also depend on other geometric data? Does the theorem correctly identify that the gap to P_n^+ is exactly the volume dependence?

## Output

## Verification memo: Theorem 2 (noncollapsed positive convergence), Step 5 note

### Summary judgment

Steps 1, 2, and 6 are correct and standard. Steps 4, 5, 7 are correct **only if** Step 3 holds. Step 3 — the uniform harmonic radius lower bound `r_h ≥ r_0(n,Λ,D,v)` from two‑sided Ricci bounds plus a global volume lower bound plus bounded diameter — is not a valid implication. As written it is circular, and the implication it needs is false in dimension ≥ 4 by the known Einstein‑degeneration theory. Consequently Theorem 2 is not established with the stated constant dependence `ε(n,v)`. The correct precise statement requires an added full‑curvature bound `|Rm| ≤ K`, giving `ε(n,v,K)`. The Section‑4 assertion that "collapse is the only remaining enemy" is therefore not right: a second unresolved regime — noncollapsed curvature concentration (bubbling) — sits inside the very case Theorem 2 asserts it can handle.

Below I go step by step, then give the precise mechanism defeating Step 3, then the constant‑dependence and gap‑identification consequences.

---

### Steps that hold

**Step 1 (two‑sided Ricci).** This is the normalization of `δ_+`. Fine. Eigenvalues of `Ric` relative to `g` lie in `[1-δ, 1+δ] ⊂ [0,2]`, so the operator bound `|Ric|_g ≤ 2 =: Λ` used later is correct.

**Step 2 (Myers).** `Ric ≥ (1-δ)g = (n-1)κ g` with `κ = (1-δ)/(n-1)` gives `diam ≤ π/√κ = π√(n-1)/√(1-δ)`. Correct; `D(n,δ)` is right.

**Volume comparison inside Step 2.1.** The relative Bishop–Gromov step is valid: with `Ric ≥ (n-1)κ g`, `κ>0`, and `Vol(M)=Vol(B(p,D)) ≥ v`, relative volume comparison gives `Vol(B(p,r)) ≥ v · V_κ(r)/V_κ(D) ≥ c(n,δ,v)\, r^n` for small `r`. So every small ball is volume‑noncollapsed with a definite ratio. This part is sound.

**Step 6 (elliptic bootstrapping).** In harmonic coordinates the Einstein condition `Ric_{ij}=λ g_{ij}` reads `Δg_{ij}+Q(g,∂g) = -2λ g_{ij}`, a quasilinear elliptic system. A `C^{1,α}` weak solution has `C^α` right‑hand side (since `∂g∈C^α`), so Schauder gives `C^{2,α}`, then `C^{3,α}`, and by induction `C^∞` (indeed real‑analytic in harmonic coordinates). This is DeTurck–Kazdan (Ann. Sci. ENS 1981) and is exactly standard. Step 6 is correct.

**Steps 4, 5, 7 conditionally.** Given a genuine uniform harmonic radius and uniform `W^{2,p}` harmonic‑coordinate control (which the harmonic‑radius machinery supplies when it applies): finitely many charts cover (bounded volume ÷ definite chart volume), Arzelà–Ascoli gives `C^{1,α'}` subconvergence (`α'<α`) of the atlases, the elliptic equation passes to a weak `W^{2,p}` Einstein limit `Ric_{g_∞}=g_∞` (the quadratic term `Q` passes because `∂g_i→∂g_∞` strongly in `C^0`; the source `-2Ric_i = -2(1+o(1))g_i → -2g_∞`), Step 6 upgrades `g_∞` to smooth, and `C^{1,α}` convergence of closed manifolds is by definition realized through diffeomorphisms `φ_i` with `φ_i^*g_i → g_∞`, so `M_i ≅ M_∞` for large `i`. All of this is genuine — **but every piece of it is downstream of Step 3.** Step 5 is worth noting only insofar as passing `Ric` to the limit needs the `W^{2,p}` harmonic‑coordinate bounds, not merely `C^{1,α}`; the harmonic‑radius framework provides them, so this is not an independent gap.

---

### The central defect: Step 3 has no valid basis and its implication is false in dim ≥ 4

The note reasons: small balls are volume‑noncollapsed (ratio `≥ c > 0`), therefore harmonic coordinates of definite size exist and `|Ric|≤Λ` plus "`C^0` metric control" yields uniform `C^{1,α}` estimates. Two problems:

**(i) Circularity.** "`C^0` metric control in harmonic coordinates on a ball of definite radius" *is* the harmonic radius bound. Producing harmonic coordinates of definite size from `|Ric|≤Λ` requires either a lower injectivity‑radius bound (Cheeger's lemma, which itself needs a two‑sided *sectional* bound) or almost‑Euclidean volume ratios (Anderson's `ε`‑regularity). A merely positive volume ratio supplies neither. The argument assumes what it must prove.

**(ii) The implication is false.** Under two‑sided Ricci bounds + global volume + bounded diameter, there is no uniform harmonic radius. This is the content, in the exact‑Einstein subcase, of Anderson (Invent. Math. 1990) and Bando–Kasue–Nakajima: sequences of **Einstein** 4‑manifolds (so `δ_+ = 0` exactly) with bounded volume, bounded diameter, and volume bounded below can have curvature concentrating at points, harmonic radius `→ 0` there, and Gromov–Hausdorff limits that are Einstein **orbifolds** with isolated singularities, off which Ricci‑flat ALE spaces bubble. More generally Cheeger–Colding and Cheeger–Naber (Ann. 2015) show that noncollapsed bounded‑Ricci limits carry a singular set of codimension 4; the regular‑set harmonic radius bound is only an `ε`‑regularity statement away from that singular set, not a global lower bound.

Why the volume noncollapse does not rescue this: `ε`‑regularity needs the small‑ball volume ratio to be close to the *Euclidean* value `ω_n`. Positive Ricci pinching gives ratios close to the round‑*sphere* profile, which at small scales tends to `ω_n` only at regular points; at orbifold/bubble points the ratio stays bounded strictly below `ω_n` (`= ω_n/|Γ|`), and precisely there the harmonic radius degenerates. So Cheeger–Colding volume convergence is consistent with — does not exclude — the concentration.

**Why almost‑pinching does not prevent the bubbling.** The bubble models are complete Ricci‑flat ALE spaces (Eguchi–Hanson and relatives). Rescaling at a concentration point sends `Ric → 0`, fully compatible with `|Ric - g| ≤ δ → 0` on the unrescaled sequence: the trace‑free Ricci is uniformly small while the **Weyl** part concentrates. The note's own Step‑4 CGB accounting (Section 3, points 3–4, and the Step 4 Preceptor note) states exactly this — that dim‑4 concentration spends quantized Weyl energy from the `8π²χ` budget and that Cheeger–Naber/ABKN are "regularity/finiteness tools, not an Einstein‑existence theorem." That understanding contradicts Theorem 2's assertion that the noncollapsed case converges cleanly to a smooth Einstein metric. There is an internal inconsistency between the two notes; the Step‑4 reading is the correct one.

**Consequence for Step 7.** Because the limit can be a singular orbifold, `M_∞` need not be a smooth manifold and the `M_i` need not be diffeomorphic to any fixed Einstein manifold. Under Ricci + noncollapse there is no manifold diffeomorphism finiteness (finiteness holds only in the orbifold sense, or under an added injectivity/curvature bound). So Step 7 does not deliver "M carries an Einstein metric" in the concentration regime.

---

### Constant dependence

With the added hypothesis `|Rm| ≤ K`: Cheeger's lemma gives `inj ≥ i_0(n,K,v,D)`, Anderson–Cheeger `C^{1,α}` convergence applies, the limit is smooth, and Theorem 2's conclusion follows. The threshold is then `ε = ε(n,v,K)` — it genuinely depends on the curvature bound `K`, not only on `(n,v)`. The stated `ε(n,v)` silently omits exactly the hypothesis (`|Rm|≤K`) that makes Step 3 true. So the answer to the posed question is: `ε` must carry a third argument `K` (or an injectivity‑radius bound `i_0`); with only `(n,v)` the theorem is not established.

---

### Does the note correctly identify the gap to `P_n^+` as "just the volume dependence"?

No — this is the most important correction. Section 4 reduces `P_n^+` to preventing collapse (`Vol ≥ v`), asserting that the noncollapsed case is settled by Theorem 2. But Theorem 2 does not settle the noncollapsed case; it settles only the noncollapsed **bounded‑curvature** subcase. The correct trichotomy is:

- **(I) Noncollapsed, `|Rm|` bounded** → smooth Einstein limit → Einstein metric on the same `M`. (Clean; this is the true content of Theorem 2.)
- **(II) Noncollapsed, `|Rm| → ∞` (Weyl/curvature concentration, bubbling)** → singular orbifold/ALE‑bubble limit → needs a gluing/obstruction analysis; possible non‑diffeomorphism of the `M_i`. **Open.**
- **(III) Collapsed** (`Vol → 0`) → lower‑dimensional limit. **Open.**

So the distance from Theorem 2 to `P_n^+` is *not* only regime (III) (volume). Regime (II) is also unresolved and lives entirely inside the noncollapsed hypothesis Theorem 2 asserts it covers. The lens‑space example in Section 5 belongs to (III) and is unrelated to the (II) issue. In dim 4, the Step‑4 CGB accounting already localizes both (II) and (III) as "curvature concentration filling the `8π²χ` budget," which is the honest statement of what remains.

---

### What a correct version reads like

> **Theorem 2′.** For each `n≥2`, `v>0`, `K>0` there is `ε(n,v,K)>0` such that if `(M^n,g)` is closed with `δ_+(g) ≤ ε`, `Vol(M,g) ≥ v`, and `|Rm_g| ≤ K`, then `M` admits a smooth Einstein metric with `Ric = +h`, `λ>0`, and moreover `M` is diffeomorphic to the smooth `C^{1,α}` limit.

This is provable by the note's Steps 1,2,4,5,6,7 with Cheeger's lemma inserted at Step 3. Removing `|Rm|≤K` returns you to the two genuine unknowns: whether noncollapsed almost‑pinched sequences can concentrate curvature onto a topology admitting no Einstein metric (II), and whether collapse can (III). Both are open and are precisely the substance of the remaining `P_n^+` problem — not the single volume gap the note names.

### Unresolved items I could not close from the supplied material

- Whether regime (II) can actually produce a `δ_+→0` sequence of manifolds admitting no Einstein metric (this is the live open question; nothing in the notes decides it).
- The exact quantitative form of `ε(n,v,K)` (depends on the Sobolev/injectivity constants in Cheeger's lemma and Anderson–Cheeger, not spelled out).
- The source texts of Anderson (1990) Cor. B and Ye (1993) are still not in hand per the Step‑4 note; the harmonic‑radius statements above rest on the standard Anderson/Cheeger–Colding/Cheeger–Naber results, which should be pinned to primary text before any formalization of Theorem 2′.