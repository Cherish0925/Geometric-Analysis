# TTCS Independent Branch Record

```json
{
  "step_id": 48,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md",
    "Sessions/S1003A02/workspace/notes/step45_lemmaM_and_weyl_departure.md",
    "Sessions/S1003A02/workspace/notes/step47_consolidation_two_scale_program.md",
    "Sessions/S1003A02/workspace/scripts/step48_theoremY.py",
    "Sessions/S1003A02/workspace/data/step48_theoremY.json",
    "Sessions/S1003A02/workspace/data/step48_lemmaP.json",
    "Knowledge/objects/papers/math-0111228-Curvature-Connected-Sums-and-Seiberg-Witten-Theory--84e6ef833958--5b74c8864d85/object.md"
  ]
}
```

## Task

Verify the new Step-48 results in Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md §§1-2 as exact mathematics. Specifically: (1) Proposition 48.1: the algebraic simplification f(W,r,n)=r^2M(n,n)-4|M|^2+p(r) = -r^2W(n,n)-4|W|^2+p(r) with M=W-(r^2/4)(I/3-nn^T), and the explicit sup over r in [0,2] giving phi(x). (2) Lemma 48.2: Psi>=0, Psi=0 exactly on the Kähler orbit, sharp constant 10/9 for Psi>=c dist^2. (3) Theorem Y: check the exact closed identity (Y0) 8π²k−P(ĝ)=4D_W−4ΔV at s≡−4 from C_+=A−k+P/8π² (with C_+=(1/2π²)∫|W+|²+(1/96π²)∫s²), the use of Theorem W/K's averaged pointwise bound (read the step45 note §3 for the saving density and its hypotheses, r∈[0,2]), and the elimination step. (4) The LeBrun comparison (Y-LeB) derived from LeBrun's Proposition 4 ∫(s−√6|W+|)²≥72π²(a+)² with the sign choice (a+)²≥A, and the claimed period lower bound ΔV≥2π²(|K_X^-|²+Σ|E_i^+|²). (5) The three consistency checks: certified cell numbers, formal common mode (P/8π²k=h(1+h)/(2−h)², V̂=8π²A/(2−h)², axial x=2/3−h; Step-47 note gives D_K formulas), rotated cells. Decide whether Corollary Y1 (ΔV≥2π²(1−c)k for P≤8π²ck) and Corollary Y2 (tariff ⇔ D_W−ΔV≤2π²(1−c)k; fields give D_W−ΔV≤ΔV−½∫Ψ) are correct and correctly scoped, and assess honestly how much of Theorem Y is already contained in LeBrun's estimate. Report any sign, normalization or factor errors with corrected statements.

## Output

# Verification memo: Step 48 §§1–2 (Proposition 48.1, Lemma 48.2, Theorem Y, the LeBrun comparison, Corollaries Y1/Y2)

## Verdict

- **Exact algebra.** Proposition 48.1, the formula for φ, Lemma 48.2 (including the sharp 10/9), the closed identity (Y0), and the elimination giving Theorem Y are all correct as exact mathematics.
- **What is inherited.** Theorem Y takes Theorem W's averaged pointwise bound from the Step-45 note as an input. I did not re-derive it.
- **(Y-LeB) is correct and has a clean source.** It is Ishida–LeBrun's Ricci estimate (12) evaluated on the Yamabe metric, with the Cauchy–Schwarz remainder kept exactly.
- **Two substantive corrections.**
  1. As used, (Y-LeB) discards a period term, −16π²Π_g. Restoring it changes the reading of §4 item 4: opening exceptional periods reduces saving capacity.
  2. The formal common mode saturates (Y-LeB) exactly, not just to leading order. Theorem Y has O(k²/A) slack there.
- **Unsupported statement.** The rotated-cell check's "same P … to O(ψ²)" is not supported by the supplied files.
- **Corollaries.** Y1 and Y2 are correct. The leading part of Y1 follows in one line from LeBrun.

---

## 1. Proposition 48.1 and φ

**The identity.** Write P_n = I/3 − nnᵀ, so |P_n|² = 2/3, and use tr W = 0. Then:
- M(n,n) = −⟨M,P_n⟩,
- ⟨M,P_n⟩ = ⟨W,P_n⟩ − r²/6,
- |M|² = |W|² − (r²/2)⟨W,P_n⟩ + r⁴/24.

Substituting into f, the r⁴ terms cancel and f = r²⟨W,P_n⟩ − 4|W|² + p = −r²W(n,n) − 4|W|² + p. The script's symbolic residual is 0, consistent with this.

**The supremum.** Maximising over unit n gives −r²μ_min = r²x, where x = −μ_min ≥ 0 because W is traceless.

Set g(r) = xr² − r³ + (7/3)r² − 4/3. Then g′ = r(2x + 14/3 − 3r).
- The unique interior maximum is at r_* = (6x+14)/9. It satisfies r_* ≤ 2 exactly when x ≤ 2/3.
- Using x + 7/3 = 3r_*/2, the value there is g(r_*) = r_*³/2 − 4/3.
- For x ≥ 2/3, g increases on [0,2], so the maximum is g(2) = 4x.
- At x = 2/3, φ = 8/3 and φ′ = r_*² = 4, so φ is C¹ there.
- The expansion of φ_low matches the JSON: 4x³/27 + 28x²/27 + 196x/81 + 400/729.

**Global form of Theorem K.** Proposition 48.1 gives Theorem K globally, not only near the orbit:
- For x < 2/3: sup f ≤ 4h ≤ (4/√(3/2))·dist, using dist ≥ √(3/2)·h with h = 2/3 − x.
- For x ≥ 2/3: sup f = 4x − 6x² − 8σ² ≤ 0.

So C_𝒦 = 4√6/3 holds everywhere, with the extremal direction being magnitude deficit.

## 2. Lemma 48.2: exact closed forms

Parametrise the spectrum as (−x, x/2 − σ, x/2 + σ), so |W|² = (3/2)x² + 2σ². The Hoffman–Wielandt distance is dist² = (3/2)(x − 2/3)² + 2σ². The two regimes then give exact formulas, sharper than the note states:

- **x ≥ 2/3.** Ψ = 3(x − 2/3)² + 4σ² = **2·dist²** identically. The ratio is exactly 2, not merely asymptotic to 2.
- **x ≤ 2/3.** Ψ is cubic in r_* = 2 − 2h/3, so the stated series is exact: **Ψ = (5/3)h² + (4/27)h³ + 4σ²**.

Consequences:
- Ψ ≥ (5/3)h² + 4σ² ≥ (10/9)·dist², because (10/9)(3/2) = 5/3 and (10/9)·2 < 4.
- Along σ = 0 the ratio is 10/9 + 8h/81. So 10/9 is a strict infimum, approached only as h ↓ 0 and never attained off the orbit.
- Ψ = 0 forces h = 0 and σ = 0, which is exactly the orbit 𝒦.
- The value at W = 0 is 572/729 = 0.7846, matching the JSON.

**Data notes.** The scan is not needed once these exact forms are available.
- In `step48_lemmaP.json`, the ratio of −2 at radii 0.001–0.03 comes from r-grid resolution. At r = 2 exactly the axial ratio is −2; the true optimum r_* = 2 − 2h/3 is not resolved.
- Some argmax values have r > 2 (for example 2.033), so that search did not impose ρ ≤ 2. It is not an independent confirmation of the constrained formula. The exact algebra above is.

## 3. (Y0) and Theorem Y

**Derivation of (Y0).** The signature-type Gauss–Bonnet formula in the LeBrun file,
2χ + 3τ = (1/4π²)∫(s²/24 + 2|W₊|² − |r̊|²/2),
gives C₊ = 2χ + 3τ + P/8π² = A − k + P/8π².

The norm conventions match. A Kähler metric with s = −4 has endomorphism spectrum (−2/3, 1/3, 1/3), so |W₊|² = 2/3 = s²/24, and √6|W₊| = −s.

At s ≡ −4, with ∫|W⁺|² = (2/3)V̂ − D_W:
- C₊ = (V̂ − D_W)/2π².
- Multiplying by 8π² gives 4V̂ − 4D_W = 8π²(A − k) + P.
- Hence 8π²k − P = 4D_W − 4ΔV, with ΔV = V̂ − 2π²A.

Also Y² = 16V̂. P(g) ≥ P(ĝ) holds because Y[g] < 0 and the constant-scalar metric minimises ∫s² in its conformal class, while ∫|W⁺|² is conformally invariant.

**Elimination.** Inheriting 8π²k − P(ĝ) ≤ 𝔼∫f ≤ ∫sup f (sign-family average, ζ and Walsh terms dropped, ρ ≤ 2 from the maximum principle):
- ∫sup f = 2D_W − ∫Ψ.
- (Y0) gives 2D_W = ½(8π²k − P) + 2ΔV.
- Therefore 8π²k − P ≤ 4ΔV − 2∫Ψ ≤ (Y² − 32π²A)/4 − (20/9)∫dist².

Every factor checks.

## 4. The LeBrun comparison and the period term

**(Y-LeB) is correct.** Put u = √6|W⁺| − 2. Then:
- D_W = −∫(4u + u²)/6.
- ∫(s − √6|W⁺|)² = ∫(6 + u)² = 36V̂ − 18D_W − 2∫u².

LeBrun's Proposition 4 then gives
**36ΔV − 18D_W − 2∫u² ≥ 72π²Π_g**, where Π_g := (a⁺)² − A ≥ 0.
Dropping Π_g gives (Y-LeB) exactly.

**Identification.** At s = −4:
- s²/3 + 4|W₊|² − (2/9)(s − √6|W₊|)² = (8/3)(|W₊| − √(2/3))² = (4/9)u².
- ∫|r|² = 4V̂ + P.

So "saving ≤ 4ΔV" is precisely Ishida–LeBrun (12)/Proposition 15, ∫|r|² ≥ 8π²(A + k), on ĝ. Their Corollary 16 shows this bound is sharp for ∫|r|². The term (4/9)∫u² is the Cauchy–Schwarz slack in that derivation.

**Correction 1: the period term.** Restoring Π_g gives
**8π²k − P(ĝ) ≤ 4ΔV − 16π²Π_g − (4/9)∫u²,** alongside Proposition 2's ΔV ≥ 2π²Π_g.

Two lower bounds on Π_g follow from the sign family:
- **Averaged sign choice.** 𝔼|a_ε⁻|² = |K_X⁻|² + Σ|E_i⁻|², and |E_i⁻|² = 1 + (E_i⁺)². Hence Π_g ≥ |K_X⁻|² + Σ(E_i⁺)². This verifies the note's ΔV ≥ 2π²(|K_X⁻|² + Σ|E_i⁺|²).
- **LeBrun's actual sign choice** (proof of Corollary 11). This gives the stronger, linear-in-periods bound
  Π_g ≥ |K_X⁻|² + 2Σ_i|K_X⁺·E_i| + ((ΣÊ_i)⁺)².
  The note's displayed formula is the averaged one, not this one.

These change the reading of §4 item 4. Periods enter the saving bound subtractively, at rate 16π² per unit Π_g. Proposition 2's ΔV ≥ 2π²Π_g alone does not offset this. Opening exceptional periods therefore reduces saving capacity at fixed ΔV. It does not "make saving possible."

It is still true that this alone gives no tariff: nothing here forces Π_g ≳ k.

**Correction 1, second part: what Theorem Y lacks.** Theorem Y, as derived from Theorem W with the ζ and Walsh terms dropped, carries no Π_g term. Whether Theorem W contains an analogous period term cannot be decided from the supplied files.

**Hypotheses.** (Y-LeB) needs only the monopole classes K_X + Σ±E_i. With one summand these come from the ordinary SW invariant of K_X and the blow-up formula. Ishida–LeBrun's Bauer–Furuta parity conditions (b₁ = 0, b₊ ≡ 3 mod 4) are needed for their multi-summand case, not here. Theorem Y needs all of Theorem W's hypotheses.

## 5. Consistency checks

**Formal common mode: arithmetic verified.** Take h = k/A, V̂ = 8π²A/(2−h)², x = 2/3 − h, σ = 0, and work in units of 8π²k/(2−h)²:

| Quantity | Value |
|---|---|
| LHS (saving) | 4 − 5h |
| 4ΔV | 4 − h |
| 2∫Ψ | (10/3)h + (8/27)h² |
| Slack in Theorem Y | (2/3)h − (8/27)h² |

(Y0) is consistent: 4D_W = 8 − 6h, and 4D_W − 4ΔV = 4 − 5h. The Step-47 Theorem-K ratio 4/(4 − 5h) and its slack 5P/(1+h) also check.

**Correction 2: exact saturation of (Y-LeB).** On this mode, s − √6|W⁺| = −3(2 − h), so ∫(s − √6|W⁺|)² = 9(2−h)²V̂ = 72π²A *exactly*. Also u = −3h, so (4/9)∫u² = 4h in the same units, and the (Y-LeB) right side equals 4 − 5h. The formal mode therefore lies exactly on LeBrun's Proposition 4 equality locus with Π_g = 0.

The averaged bound then forces K_X⁻ = 0 and all E_i⁺ = 0, i.e. null exceptional periods. That is precisely Lemma T's excluded configuration.

So §2's sentence "the formal common mode saturates both" should read: **it saturates (Y-LeB) exactly, and Theorem Y only to O(k), with O(k²/A) slack.**

The structural content is a three-ledger statement. Any admissible near-copy of the formal mode must pay through at least one of:
- Π_g > 0,
- the u-variance,
- Ψ,
- or departure of ΔV.

Improving the leading 4ΔV requires input beyond Proposition 4 together with (Y0).

**Certified cell.** The quoted values 4D_W ≈ 0.07513 and 4ΔV ≈ 0.07080 are not in the supplied files. Their difference, 0.00433, matches 1 − c = 0.0043373, so the pair is consistent with (Y0). This tests (Y0) only if both numbers were computed independently on a scalar-(−4) representative.

The per-cell use also needs:
- relative-volume definitions;
- exact-CH collars, so that the closed identity localises.

Testing Theorem Y needs the cell's ∫Ψ, which must satisfy ∫Ψ/(8π²) ≤ 0.0332. Testing (Y-LeB) needs ∫u², with (4/9)∫u²/(8π²) ≤ 0.0665. Neither value is reported, so the stated "large slack" is not yet a computed fact.

**Rotated cells.** Theorem Y involves only [g], through ĝ and P(g) ≥ P(ĝ). Its insensitivity to the almost-Kähler representative is therefore correct.

"Same P … to O(ψ²)" is not supported: Step 47 item 9 says the rotated cost is not enclosed by the diagonal certificate and gives only continuity. Rotated cells have Π_g > 0 (tiny nonzero exceptional periods). The −16π²Π_g term is the ledger entry that distinguishes them from diagonal cells. A quantitative check needs the periods and ΔV on the rotated ĝ.

## 6. Corollaries Y1 and Y2

**Y1 is correct.** P ≤ 8π²ck gives ΔV ≥ 2π²(1−c)k + ½∫Ψ ≥ 2π²(1−c)k + (5/9)∫dist². Then:
- Y² ≥ 32π²(A + (1−c)k) + (80/9)∫dist².
- 2π²(1−c) = 0.085614, matching the depletion constant.

The leading inequality ΔV ≥ 2π²(1−c)k is exactly Ishida–LeBrun (12): 4V̂ + P ≥ 8π²(A+k).

The LeBrun route gives the parallel form ΔV ≥ 2π²(1−c)k + 4π²Π_g + (1/9)∫u². Both forms hold. Y1 is stated with its hypotheses only if the reader is told which of the two needs Theorem W.

**Y2 is correct.** The steps:
- From W⁺ = W_* + E: 4E(ω̂,ω̂) = 2(2/3 − |W⁺|²) + 2|E|².
- By (Y0), P ≥ 8π²ck is equivalent to D_W − ΔV ≤ 2π²(1−c)k. Applied to ĝ, this is equivalent at the level of inf_g P.
- Theorem Y gives D_W ≤ 2ΔV − ½∫Ψ.
- LeBrun gives D_W ≤ 2ΔV − 4π²Π_g − (1/9)∫u².

## 7. What in Theorem Y goes beyond LeBrun

**Already contained in LeBrun:**
- the leading factor 4ΔV;
- Corollary Y1's leading bound;
- the stronger penalty on the deficit side, where (4/9)u² = 4h² exceeds 2Ψ ≈ (10/3)h²;
- the period term, which Theorem Y lacks.

**New in Theorem Y:**
- the splitting penalty 8σ², to which LeBrun is blind at quadratic order since u = O(σ²);
- the excess-side coefficient: 2Ψ = 4·dist² exactly, versus LeBrun's (4/9)(3x−2)², i.e. 6/9 against 4/9.

Both bounds hold, so any convex combination of them holds too. A pointwise maximum of the two penalties is not obtained by these arguments.