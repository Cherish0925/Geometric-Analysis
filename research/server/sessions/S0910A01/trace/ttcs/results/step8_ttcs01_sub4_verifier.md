# TTCS Independent Branch Record

```json
{
  "step_id": 8,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Sessions/S0910A01/workspace/notes/sources/derdzinski_1983_self_dual_kahler_einstein_four.txt",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md"
  ]
}
```

## Task

Verify the Step 8 measure-local rigidity theorem for the four-dimensional LeBrun near-boundary negative-pinching route. Check (i) the primary-source Derdziński conformal factor and orientation/eigenvalue normalization used in the local contradiction, (ii) the local averaging lemma with local means under Ricci lower/doubling, (iii) the harmonic-coordinate passage through finite W^{2,p} convergence and smoothness of the limiting Einstein metric without derivative-Ricci assumptions on the approximating metrics, and (iv) the exact strength of the conclusion Vol{p: Vol(B_1(p))>=v}/Vol(M)->0 rather than pointwise collapse. Identify any mathematical gaps, missing hypotheses, or normalization errors that could invalidate the theorem.

## Output

# Verification Memo: Step 8 Measure-Local Rigidity Theorem

## Overall assessment

The theorem `Vol E_i(v)/Vol M_i → 0` and its four supporting components are mathematically sound as stated, and the load-bearing normalizations that I initially suspected of being ad hoc turn out to be exactly the constants forced by LeBrun's Proposition 3.1. The argument is conditional on the deficit bookkeeping of Steps 3–7 (not in the supplied files), but every piece that *can* be checked against the two primary papers checks out, including the delicate `8√6` constant. Below I record the verifications, one genuine dependency that is load-bearing, and several points that are correctly handled.

## (i) Derdziński conformal factor, orientation, and eigenvalue normalization — correct

The primary-source statements are cited accurately. From the extracted text:
- Proposition 5(i): `ḡ = (24 g(W⁺,W⁺))^{1/3} g` is locally Kähler where `W⁺≠0`, orientation-compatible, given `δW⁺=0` and `#spec(W⁺)≤2`.
- Proposition 3(ii)/Proposition 2(ii): `|W⁺|² = u²/24` for Kähler (`u` = scalar curvature).
- Proposition 5(iii): `g(W⁺,W⁺)` constant ⟺ `∇W⁺=0`.

The norm convention is used consistently: `|W⁺|²` = sum of squares of the three `W⁺` eigenvalues (Derdziński's `|W⁺|² = λ²+μ²+ν²`). For the calibrated spectrum `(1/12,1/12,-1/6)`: trace `= 0`, `|W⁺|² = 2/144+4/144 = 1/24` ✓. For Kähler-Einstein `Ric=-g` (`s=-4`): spectrum `(s/6,-s/12,-s/12)=(-2/3,1/3,1/3)`, `|W⁺|² = s²/24 = 2/3` ✓.

Orientation is consistent between the two profiles: for negative scalar curvature the simple `W⁺`-eigenvalue is the lowest, and the (almost-)Kähler form sits in that lowest eigenspace in both the calibrated and the Kähler-Einstein case. There is no orientation or normalization error.

The local contradiction is airtight given its inputs: since `|W⁺_∞|²=1/24` is constant, the Derdziński factor `(24·1/24)^{1/3}=1`, so `ḡ=g_∞` is itself locally Kähler on the chart; Proposition 2(ii) then forces `|W⁺|²=s²/24=2/3`, contradicting `1/24`. The `#spec≤2` and `W⁺≠0` hypotheses hold at the calibrated spectrum, and `δW⁺=0` is automatic for the smooth Einstein limit (Derdziński's remark after Proposition 3, via his (9),(14)).

## (ii) Local averaging lemma — correct, no missing hypotheses

The Fubini identity and the doubling estimate are both right. With `p` uniform by volume,
`E_p[(1/Vol B_R(p))∫_{B_R(p)}F] = (1/Vol M)∫_M F(x)[∫_{B_R(x)} dμ(p)/Vol B_R(p)] dμ(x)`.
For `p∈B_R(x)` one has `B_R(x)⊂B_{2R}(p)`, so Bishop-Gromov doubling gives `Vol B_R(x) ≤ Vol B_{2R}(p) ≤ D(n,K,R) Vol B_R(p)`, hence the inner bracket is `≤ D`. The constant `D = V_{-K}(2R)/V_{-K}(R)` depends only on `n,K,R`. The conclusion `E_p[local mean] ≤ D·(global mean)` is exact. The interpretation that local means retain content in the collapsed regime (where absolute local integrals are small merely because balls are small) is valid.

## (iii) Harmonic-coordinate passage — the correction over Step 7 is valid

The replacement of the erroneous "approximating-Schauder" step by finite `W^{2,p}` is correct and uses only bounded Ricci, not `∇Ric`:
- Cheeger-Naber Theorem 1.13 (`Vol T_r{r_h≤r} ≤ Cr⁴` in dim 4, `|Ric|≤3`, noncollapsed) is quoted correctly and produces `q_i∈B_{1/2}(p_i)` with `r_h(q_i)≥r_0(v)` once `Cr_0⁴ < Vol B_{1/2}(p_i)`. The sequence has `Ric_{g_i}≈-g_i`, so `|Ric|` stays within the required bound for large `i`.
- In harmonic coordinates with `r_h≥r_0`, bounded Ricci yields uniform `C^{1,α}∩W^{2,p}` bounds for all finite `p` (Cheeger-Naber, Definition 2.9 discussion). Their own text stresses that `C^{2,α}` would require `∇Ric`; the note correctly avoids that.
- The elliptic identity `g^{ab}∂_a∂_b g_{ij} = -2Ric_{ij} + Q_{ij}(g^{-1},∂g)` is the standard harmonic-coordinate Ricci formula (the flagged sign convention is harmless).
- Extract a subsequence of pulled-back metric components on a fixed `B_{r_0}(0)⊂ℝ⁴` converging in `C^{1,β}` and weakly in `W^{2,p}`. Since `-2Ric_{g_i}→2g_∞` uniformly (global `L^∞` Ricci-error `δ_i→0`) and `Q` converges uniformly (`C^{1}` control of `∂g`), the right side converges strongly in `L^p`; interior elliptic estimates for the uniformly elliptic operators `g_i^{ab}∂_a∂_b` upgrade to strong `W^{2,p}` convergence. Only the limit is bootstrapped: `g_∞` solves `Ric=-g_∞` weakly, then standard Schauder/DeTurck-Kazdan elliptic regularity for Einstein metrics makes `g_∞` smooth. Applying Schauder to the exact Einstein limit (not the approximants) is exactly the correct repair.
- Strong `W^{2,p}`, `p>2`, gives `L^p` convergence of second derivatives, hence `L^{p/2}` (`p/2>1`) convergence of curvature-squared densities; the deficit terms `|Ric+g|²`, `(s+8√6|W⁺|)²`, `ξ(Q+P)` are curvature-quadratic, so they pass to the limit in `L¹` on the bounded chart. `|W⁺|`, `w`, `ξ` are Lipschitz functions of `W⁺` and pass as well.

No independent error here; the passage is the standard Anderson/Cheeger-Naber blow-up compactness with the appropriate finite-`p` strength.

## (iv) Strength of the conclusion — correctly identified

The averaging step is logically tight. Global mean `(1/Vol M_i)∫F_i→0`; if `Vol E_i(v)≥η Vol M_i` on a subsequence, then the conditional mean over `E_i(v)` is `≤ (1/η)·D·(global mean)→0`, producing points `p_i∈E_i(v)` with local mean `→0`. Bishop-Gromov gives `Vol B_{1/2}(p_i)≥c(n,K)v`, the harmonic-radius estimate gives `q_i`, and `∫_{B_{r_0/2}(q_i)}F_i ≤ (local mean)·Vol B_1(p_i) → 0` since `Vol B_1(p_i)` is bounded above (Bishop-Gromov upper bound). The `W^{2,p}` limit is a smooth Einstein `g_∞` with `∫_{chart}F_∞=0`, so `F_∞≡0`, producing the Derdziński contradiction.

Crucially, the contradiction is powered by the *positive-fraction* hypothesis: if `Vol E_i(v)=o(Vol M_i)`, the averaging cannot produce good points, so `o(Vol)` noncollapsed islands survive. The note states exactly this — stronger than a single conditional local statement, weaker than pointwise disappearance of all noncollapsed regions. This is the honest strength. §6–§7 correctly leave the collapse regime and the topological accounting open (the free-circle model excludes only one collapse architecture; singular-fiber/exceptional-strata collapse is not excluded).

The eigenvalue pinning is complete, not partial: `F_∞=0` gives `s=-4`, `|W⁺|²=1/24`, and `ξ=0` (i.e. `w=-1/6`). Solving `λ_2+λ_3=1/6`, `λ_2²+λ_3²=1/72` gives discriminant zero, forcing `λ_2=λ_3=1/12`. So the full spectrum `(1/12,1/12,-1/6)` and `#spec=2` are forced, not assumed.

## Verified resolution of the two constants I flagged as suspect

**The `8√6` and `|W⁺|²=1/24` are exactly LeBrun's Proposition 3.1, not a normalization error.** In LeBrun's Proposition 3.1 the Cauchy-Schwarz split is `(2/3, 1/(3√2))·(‖s‖, ‖√48|W⁺|‖)`. Equality requires `(‖s‖,‖√48|W⁺|‖) ∝ (2/3,1/(3√2))`, i.e. `‖√48|W⁺|‖/‖s‖ = 1/(2√2)`, giving `|s| = 8√6|W⁺|`, hence `|W⁺|² = s²/384 = 1/24` at `s=-4`. Proposition 3.1's equality case is precisely "almost-Kähler of the type in Proposition 2.4" — **not** Kähler. By contrast, the Ricci estimate Proposition 4.1 uses the split `(2/3,√2/3)`, whose equality forces `|s|=2√6|W⁺|`, `|W⁺|²=s²/24=2/3`, and its equality case is Kähler CSC. Since the Einstein-obstruction Theorem 3.3 runs through Proposition 3.1 (weight `2` on `|W⁺|²`), the near-threshold saturating profile is the almost-Kähler one with `|W⁺|²=1/24`, while Derdziński independently forces Kähler with `|W⁺|²=2/3`. The two saturations differ by the factor `8√6` vs `2√6`, and that difference is exactly what makes the Derdziński contradiction genuine. This is the mechanism LeBrun himself points to ("the new estimate is apparently saturated by a larger class of almost-Kähler metrics"). This constant is therefore verified from the supplied LeBrun paper.

**The `ξ(Q+P)≥0` and strict positivity are supported by reconstruction.** The `w`-version (Proposition 2.1, `(2/3 s+2w)_-²`) and the `|W⁺|`-version (Theorem 2.3, `(2/3 s-2√(2/3)|W⁺|)²`) differ pointwise by `2ξ·[-(4/3 s+2w-2√(2/3)|W⁺|)]` with `ξ=w+√(2/3)|W⁺|≥0`. At `s=-4` the bracket `Q+P := -(4/3 s+2w-2√(2/3)|W⁺|) = 16/3 - 2w + 2√(2/3)|W⁺| ≥ 16/3 > 0` for all admissible spectra (`w≤0`, `|W⁺|≥0`). Thus `Q+P>0` uniformly on the constraint set `{s=-4}`, so `ξ_∞(Q_∞+P_∞)=0 ⟹ ξ_∞=0` robustly — resolving the concern that `Q+P` might vanish at some non-target spectrum. The reconstruction reproduces the note's positivity assertion; the exact Step-7 definitions should confirm the numerical factor, but the sign and strict positivity are forced by the LeBrun structure.

**The `32π²/9` volume asymptotic is consistent with LeBrun Prop 3.1.** At the calibrated profile `s²/24+2|W⁺|² = 16/24+2/24 = 3/4`; with `(c_1^+)²≈A_i` and near-saturation, `(1/4π²)(3/4)Vol_i ≈ (2/3)A_i` gives `Vol_i/A_i → 32π²/9` ✓. The `k_i/A_i→1/3` is the LeBrun Theorem 3.3 threshold `k=c_1²/3`, and `(2χ+3τ)(M)=A_i-k_i→2A_i/3` meeting the Proposition 3.2 lower bound `(2/3)A_i` is exactly what forces near-saturation of Proposition 3.1. All internally consistent.

## Load-bearing dependency on unsupplied Steps 3–7

The theorem is conditional on the following, which are not in the supplied files and cannot be independently confirmed here:
- the full deficit density `F_i` and that a hypothetical near-Einstein, near-threshold sequence produces `(1/Vol M_i)∫F_i → 0`;
- the estimate `∫ξ_i(Q_i+P_i) ≤ 24π²D_i = o(A_i)` (the constant `24π²` in particular is from that algebra; the *structure* — control by the gap between the two LeBrun estimates — is sound, but the coefficient is not reconstructible from the supplied text);
- `D_i/A_i→0`, `k_i/A_i=1/3+O(δ_i²)`, and the monopole sign convention `(a_i^+)²≥A_i`;
- the secondary `|∇W⁺|²=1/16` "corrected Einstein-Weyl Weitzenböck" route in §1. This is *not* load-bearing (the main §5 proof uses the Kähler `|W⁺|²=2/3` contradiction, which via Derdziński Prop 5(iii) also follows from constant nonzero `|W⁺|`⟹`∇W⁺=0`⟹Kähler CSC). The `1/16` value is unverifiable from the supplied material but its correctness is not needed for the theorem.

Given that the two most delicate constants (`8√6`, `1/24`) and the volume/threshold asymptotics are all consistent with — and in the case of `8√6` directly derived from — the supplied LeBrun and Derdziński texts, the conditional structure is well founded. A complete verification of the theorem as an unconditional statement about the near-threshold family requires the Step 3–7 establishment of `(1/Vol M_i)∫F_i → 0` and the `∫ξ(Q+P)` bound.

## Summary of findings

- Parts (i)–(iv) are mathematically correct; no normalization, orientation, or eigenvalue error.
- The `8√6` constant, initially suspicious, is verified as LeBrun's Proposition 3.1 Cauchy-Schwarz equality condition; it is precisely what distinguishes the almost-Kähler saturation (`|W⁺|²=1/24`) from Kähler saturation (`|W⁺|²=2/3`) and thereby makes the Derdziński contradiction real.
- The eigenvalue spectrum is fully pinned by `F_∞=0` (discriminant computation), so `#spec=2` and Derdziński's hypotheses hold.
- The averaging argument produces exactly the volume-fraction conclusion, no more; `o(Vol)` noncollapsed islands and the collapse regime are correctly left unresolved.
- The remaining dependencies are the Steps 3–7 deficit design and the near-saturation of the global mean, together with the coefficient `24π²`. These are internally consistent with the LeBrun estimates but are the items to confirm to make the theorem unconditional for the family.