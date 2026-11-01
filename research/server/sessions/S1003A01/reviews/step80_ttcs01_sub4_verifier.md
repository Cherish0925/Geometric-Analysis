# TTCS Independent Branch Record

```json
{
  "step_id": 80,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step79_second_tier_dWplus_kodaira_and_log_torsion_identity.md",
    "Sessions/S1003A01/workspace/notes/step80_regularized_torsion_transport.md",
    "Sessions/S1003A01/workspace/scripts/step79_dW_components_bianchiVIII.py",
    "Sessions/S1003A01/workspace/data/step79/dW_check.json",
    "Sessions/S1003A01/workspace/data/step79/kodaira_flux.json",
    "Sessions/S1003A01/workspace/data/step79/model_integrals_n40.json",
    "Sessions/S1003A01/workspace/data/step79/logq_check.json"
  ]
}
```

## Task

Check the Step-79 second-tier system and the Step-80 use of it as a geometric analyst. Verify or challenge E1/E2, the gradient decomposition, the identification D=24|eta|²-8 trV²+32 Im<alpha,K∂Dv>, and the scope of the complete-model negative conclusion. Pay special attention to conventions (complex form norms, trV²=2|v|², Laplacian sign) and to the fact that the Bianchi-VIII check has real eta and v only. Then assess whether common-denominator regularization reveals a plausible stronger combination with the weighted Kodaira currents, or whether a specific free jet/cross term blocks pointwise coercivity. Give a mathematical memo, not general advice.

## Output

# Memo: Step-79 second-tier system, the Step-80 regularization, and what the cross term really is

## 0. Summary

1. **Conventions.** The Step-79 conventions hold up against the data.
2. **E1 and E2.** They are verified, and the "η, v real on the model" concern is mostly removed by U(1)-weight counting.
3. **D is correct in Step 79.** The identification D = 24|η|² − 8trV² + 32 Im⟨α,K∂_Dv⟩ is numerically correct with Step-79 normalizations.
4. **Step 80's model formulas are wrong.** Its rational model formulas for |η|², D, the coupling (80.2) and the end volume density do not match the geometry. Its "the coupling cancels half the η mass" conclusion is reversed: on the complete model the coupling is nonnegative and of lower order at the end.
5. **The cross term is a divergence plus algebra.** Via E2 and the trace part of the torsion equation:
   32 Im⟨α,K∂_Dv⟩ = −32|η|² + 2|s|q − 3q² − 16 div Re(ηα).
   Integrated, this makes the Δq budget identical to (★). Under the (q+ε)⁻¹ weight, its transport combines with |dq|² into the perfect square 32|∂r − ηα|². That square is the first square in the |∇W⁺|² decomposition.
6. **What blocks coercivity.** The cross term is not the obstacle. Pointwise coercivity is blocked by the zeroth-order free data (η, v), and in the Kodaira chain by the free jet ∂_Dv entering through E2.

---

## 1. Conventions

All of the following are checked against `dW_check.json` and `logq_check.json`.

- **Torsion norm.** q = |∇ω|² = 2|∇u₁|² = 2|α|², with |ξ|² = Σ_a|ξ(e_a)|². At p = 0.5, alpha2 = 1.41691 and q = 2.83382.
  - For a (1,0)-form ξ, ξ·ξ (bilinear) = 0. Hence |Re ξ|² = |ξ|²/2, and for real f, |df|² = 2|∂f|². Both facts are used below.
- **trV² = 2|v|².** V is the trace-free part of W⁺ on ⟨u₂,u₃⟩, so trV² = 2[((W₂₂−W₃₃)/2)² + W₂₃²] = 2|v|².
  - The script's `T_AK = 2absv2 + 3q2/32` gives 32 on the model.
  - This agrees with ∫(s²/24 − |W⁺|²) = ∫(3q/2 − 3q²/32 − 2|η|² − trV²) = 96 − 16 − 48 = 32, using |W⁺|² = (3/2)r² + 2|η|² + trV².
- **Laplacian.** `lap_q` is (vol√G)⁻¹ ∂_p(vol/√G · ∂_p q), the analyst Laplacian. It is negative near the bolt, where q is maximal. Closed form:
  vol√G = 64p(1+3p²)/(3(1−p²)³), vol/√G = 16p(9p²−1)/(3(1−p²)),
  Δq = −432(1−p²)³(27p⁶ − 87p⁴ + 29p² − 1)/(1+3p²)⁶,
  which gives −37.117 at p = 0.4, matching the data.
- **Normalizations.** ∫q = 384∫_{1/9}^{1}(1+3x)⁻² dx = 64 reproduces Step 77's normalization. Because s is constant, ∂r = ∂q/4.

## 2. E1, E2, the gradient decomposition, and the real-η issue

**Weights.** η has weight +1, v has +2, α has −1 (since ∇u₁ = Re(α⊗ψ) is invariant), and K(ξ) has weight 1 − w(ξ).

**E1.** The left side has weight 1.
- Admissible right-hand terms bilinear in W-data and torsion are vα, η̄Kα and K∂r.
- v̄α (weight −3) and ηKα (weight 3) are excluded.
- Since K is quaternionic (K² = −1, antiunitary), we have ⟨Kξ, ξ⟩ = 0. So α and Kα span Λ^{1,0} where α ≠ 0.
- Each point therefore gives two complex equations for the complex coefficients. Residuals of order 10⁻⁴⁰ at five points with independently varying real η and v fix those coefficients, phases included.
- The real-η restriction therefore does not leave E1 undetermined. The same argument fixes E2 (all terms have weight −1) and the torsion equation (weight −1).

**Cleaner form of E1.** Using K(ηα) = η̄Kα:

  ∂_Dη = vα + iK(Y),  Y := ∂r − ηα. (2.1)

Expanding with ⟨α,Kα⟩ = 0 and ⟨α, K(ηα)⟩ = 0:

  |∂_Dη|² = |Y|² + (q/2)|v|² + 2 Im(v⟨α,KY⟩).

**E2 cross-check.** Expanding E2 gives

  |∂̄_Dη|² = 9r²q/8 + 4|∂_Dv|² + 6r I,  I := Im⟨α,K∂_Dv⟩.

- p = 0.5: 5.318 + 3.723 − 8.283 = 0.758, against `n_dbeta` = 0.75817.
- p = 0.4: 0.9306 + 3.0009 − 3.2801 = 0.6514, against 0.651317.

This independently confirms the sign with which I enters.

**What the real model does not test.**
- **Squares in |∇W⁺|².** For 5|∂r − c ηα|² and 2|∂̄v + c′ηᾱ|², the data constrain |c| and Re(c·⟨·,·⟩). If the cross pairings are real on the model, c and c̄ cannot be distinguished. The phases there rest on the derivation.
- **Δq formula.** Two weight-0 real terms vanish identically on the model: Re⟨α,K∂_Dv⟩ (the real part of `X1` is about 10⁻⁴¹) and Im(v̄η²). Their coefficients in Δq are untested.
  - By E2 and §4 below, Re⟨α,K∂_Dv⟩ = ±½ div Im(ηα), a pure divergence.
  - So a coefficient error there is invisible in every unweighted budget.
  - It would enter the (q+ε)⁻¹-weighted identities as an extra transport ⟨dq, Im(ηα)⟩/(q+ε)².
  - A test requires a configuration with Im(ηα) ≠ 0.

## 3. The identification of D, and the errors in Step 80's model formulas

**D from the data.** From (80.1), D = −Δq + 18q − (9/4)q².
- p = 0.4: D = 58.116 = 11.741 − 2.972 + 49.347, i.e. 24|η|² − 8trV² + 32I with I = 1.5421.
- p = 0.5: 40.773 from both sides.
- p = 0.9: 0.073226 from both sides.

So Step 79's D is right.

**Exact rational model formulas.** Derived from q and the metric:
- |η|² = 9(1−p²)³(9p²−1)/(1+3p²)⁴. This is 0.4892 at p = 0.4, matching the data.
- D = 108(1−p²)³(297p⁶ − **267**p⁴ + **251**p² − 25)/(1+3p²)⁶.
- 32 Im⟨α,K∂_Dv⟩ = 432(1−p²)⁴(9p²−1)(3p²+5)/(1+3p²)⁶. This gives 49.35 at p = 0.4, matching.
- The coupling integrates to 512 = ∫D − ∫(24|η|² − 8trV²) = 768 − 256. Explicitly, ∫ = 512∫_{4/3}^{4}(4−y)(3y−4)(y+4)y⁻⁵ dy = 512.

**Step-80 discrepancies.**

| Quantity | Step 80 | Correct |
|---|---|---|
| \|η\|² | 2 × the value above | as above (e.g. p = 0.9: 0.005611 vs 0.0028053) |
| D at p = 0.4 | 38.47 | 58.12 |
| D difference | — | true − Step 80 = 2592p²(1−p²)⁴/(1+3p²)⁶ |
| D polynomial | −243p⁴ + 227p² | −267p⁴ + 251p² |
| (80.2) at p = 0.9 | −0.0529 | +0.0162 |
| (80.2) sign | carries (p−1)³(p+1)³ (sign changes) | (1−p²)⁴(9p²−1)(3p²+5) ≥ 0 |
| End volume density | (16√2/3) t⁻³ dt | vol√G → (32/3) t⁻³ (factor √2) |

The coupling therefore vanishes at the bolt (p = 1/3) and is ≥ 0 on the whole model.

**What survives and what does not.**
- At p = 1 both D polynomials equal 256. So D ≈ 54t³, q ≈ (9/2)t³ and |dq|² ≈ (729/2)t⁶ are correct to leading order.
- Consequently the layer scale t ≍ ε^{1/3}, u_peak ≈ (1/3)log(1/ε) and the ε^{−2/3} peak growth survive.
- The tabulated values in Step 80 §3 do not describe the geometric model:
  - The gradient, D/(q+ε) and RHS columns are affected.
  - The ε = 10⁻⁸ split (1.28 × 10⁸, −1.25 × 10⁵, −6.41 × 10⁷) is affected.
  - Agreement of (80.R) to 4 × 10⁻¹² only shows that the script's own Laplacian/measure pair is internally consistent.
- Correct end behaviour: 24|η|²/q → 12 = |s| (Step 79 Remark 2), while 32I/q ≈ 24t → 0. In ∫·/(q+ε) the coupling is smaller than the η term by a factor ε^{1/3}.
- Step 80's sentence "the complete model realizes the adverse cancellation exactly" has no basis.

## 4. The cross term is a divergence plus algebra

**Step 1 (E2).** Taking real parts of E2 paired with α:

  Re(α·∂̄_Dη) = −(3r/2)|α|² − 2I,

where α·∂̄_Dη = ⟨α, \overline{∂̄_Dη}⟩ is the bilinear contraction. Since α is (1,0), α·Dη = α·∂̄_Dη.

**Step 2 (torsion trace).** For any 1-form ξ, ⟨dξ, ω⟩ = ±div(Jξ) − ⟨ξ, δω⟩. Here δω = 0, so no Nijenhuis correction enters. For α of type (1,0) this gives ⟨d_bα, ω⟩ = ±i div_b α.

**Step 3 (structure equation).** The torsion structure equation gives ⟨d_bα, ω⟩ = −2iη̄. Hence div_b α = κη̄ with κ = ±2.

**Step 4 (product rule).** ηα has weight 0, and div(ηα) = α·Dη + η div_bα. Therefore

  Re(α·∂̄_Dη) = div Re(ηα) − κ|η|².

**Step 5 (fixing κ).** The model integrals fix κ = −2:
- With κ = −2: ∫Re(α·∂̄η) = 32 = 2·16. This is consistent with ∫32I = 512 and 12∫rq = 2sQ + 3∫q² = −1024.
- The flux of ηα is O(t) → 0.
- With κ = +2, (★) is contradicted.

**Result.**

  32I = −32|η|² − 12rq − 16 div Re(ηα),
  D = −8|η|² − 8trV² + 2|s|q − 3q² − 16 div Re(ηα), (4.1)
  Δq − 16 div Re(ηα) = 8|η|² + 8trV² − (|s|/2)q + (3/4)q².

Integrated on a closed manifold, the third line is exactly |s|Q = 16∫|η|² + 16∫trV² + (3/2)∫q², i.e. (★). The δW⁺ coupling therefore carries no information in the unweighted budget beyond (★).

**Regularized form (80.R′).** In (80.R), ∫ div X/(q+ε) = ∫⟨X, dq⟩/(q+ε)² for the smooth field X = Re(ηα). Then use

  |dq|² − 16⟨dq, Re ηα⟩ = |dq − 8 Re ηα|² − 64|Re ηα|²,

with |dq − 8 Re ηα|² = 32|Y|² and 64|Re ηα|² = 16q|η|². This gives, for every ε > 0, with no zero-set hypothesis:

  32∫|Y|²/(q+ε)² + (|s|/2)∫q/(q+ε) = ∫(8|η|² + 8trV²)/(q+ε) + 16∫q|η|²/(q+ε)² + (3/4)∫q²/(q+ε). (80.R′)

Properties:
- **ε → ∞.** Multiplying by ε recovers (★), as it must.
- **No indefinite term.** Every term is nonnegative. The only derivative is Y = ∂r − ηα, the same quantity as in E1 (2.1) and the first square 5|Y|² of |∇W⁺|².
- **Formal ε → 0 version.** Under the Step-79 integrability assumptions, and using s²V = 32π²c₁² + 16T_AK together with (★):
  ∫(24|η|² + 8trV²)/q − 32∫|Y|²/q² = (|s|/2)V − (3/4)Q = (16π²c₁² − 4T_AK − 12∫|η|²)/|s|.
  On codimension-two strata the 4πm residue now sits in 32|Y|²/(q+ε)² and in |η|²/(q+ε), since η and v are first derivatives of α at zeros.
- **Pointwise check available.** On the model, Re(ηα)(E₀) is computable from the existing `analyse` output (α[0], η). At p = 0.5, Re⟨∂r, ηα⟩ = 1.0755 and dr(E₀) = −2.0528, so Re(ηα)(E₀) = −0.524. The predicted divergence is div Re(ηα) = −0.405 at p = 0.5 and +0.00255 at p = 0.9. Radial differentiation, using the unimodularity of SL₂ so that only the E₀ part contributes, would test (4.1) and the sign κ = −2 pointwise rather than through one integral.

## 5. What Proposition 79.1 actually covers

**What is correct.** Flux vanishing needs only |X| = o(t²), because vol ∝ t⁻² and the level-set flux is vol·X(E₀). Decay rates are |α|, |η| ~ t^{3/2}, |v| ~ t², |dr| ~ t³.
- The stated reason "at least two decaying factors" is not literally correct: dr alone is an admissible current with one factor.
- The conclusion still holds for all gauge-invariant currents polynomial in (r, η, v, α, Dr, Dη, Dv).

**Uses of closedness outside the class.** The class excludes arguments that use:
- finite V (as in 79.L, the ε → 0 limit of 80.R′, and L^p interpolation with V);
- attained minima of functions whose infimum on the model is reached only at the end (q > 0 ⇒ min q > 0);
- spectral or Poincaré data;
- topological input (c₁², SW).

Maximum-principle arguments at max q do transfer, since q is maximal at the bolt on the model.

**Fixed ε.** (80.R), (80.K) and (80.R′) at fixed ε all have zero end flux on the model, so they lie inside the no-go class. Only the nonuniform limit ε → 0 escapes it.

In (80.R′) the escape is explicit. On {q ≫ ε} at the model end:
- the right side has density 8|η|²/q + 16|η|²/q → 4 + 8 = 12;
- the left side has 32|Y|²/q² + 6.

Sampled values of 32|Y|²/q² are 4.86 at t = 0.25 and 3.51 at t = 0.1. If ∂r and ηα become asymptotically parallel, the limit is 32(3.375 − 2.25)²/20.25 = 2. This limit is not yet determined; it needs α(E₀) as t → 0. The deficit of about 4 per unit volume is carried by the moving layer t ≍ ε^{1/3}.

## 6. Weighted Kodaira currents and the obstruction to coercivity

**The cross term is not the obstruction.** Section 4 absorbs it exactly. The terms that remain are as follows.

(a) **Zeroth-order free data.** At a point, r = s/6 + q/4 is fixed, but η and v are free. So the integrand of (80.R′) has no pointwise sign.
- A contradiction from (80.R′) requires the averaged inequality
  ∫(24|η|² + 8trV²)/q + (3/4)Q < (|s|/2)V.
- The model end violates the corresponding local ratio by a factor of 2 (12 versus 6). An upper bound for η and v must therefore come from elliptic information that sees compactness, not from local algebra.

(b) **Orientation of the Kodaira chain.**
- (Kη) bounds (|s|/2)∫|η|²/(q+ε) by ∫|∂̄η|²/(q+ε). By E2, |∂̄η|² = 9r²q/8 + 4|∂v|² + 6rI.
- The leading term alone gives 24∫|η|²/(q+ε) ≲ (3/2)|s|V, three times the needed (|s|/2)V, before the free jet ∂v is even counted.
- (Kv) bounds |∂v|² only through |∂̄v|² = |Z − ηᾱ|², with Z = ∂̄v + ηᾱ.
- Each identity controls a section by the next jet. The chain closes only in the combination (Kη) + 4(Kv), where ∂_Dv cancels:
  4|∂̄v|² − |∂η|² + 9r²q/8 + 6rI − (|s|/2 − q/4)|η|² − 4(|s| − q/2)|v|² = div(j_η + 4j_v).
- Inserting (2.1) for |∂η|² and §4 for 6rI, this involves only Y, Z, η, v, q. The term 6rI becomes −6r|η|² − (9/4)r²q − 3 div(r Re ηα) + 3⟨dr, Re ηα⟩, which again feeds the Y-square. This is the only combination in which the second tier closes on the |∇W⁺|² variables (Y, ∂v, Z). Its sign content is not yet computed; the model integrals in Step 79 §3 give exact values against which to test it.

(c) **Power mismatch in the weighted transports.**
- ⟨dq, j_f⟩/(q+ε)² is bounded by (|dq|/(q+ε))·(|f||Df|/(q+ε)).
- Young's inequality closes against the available terms only if |f|² ≲ q + ε.
- At a zero of α, however, η̄ and v̄ are the (1,1) and (2,0) parts of ∇α, by the torsion equation with α = 0. So |η|²/q ~ ρ⁻² near nondegenerate zeros.
- This is the precise jet-level reason why weighted Kodaira transports are not controlled by (80.R′). They are integrable in four dimensions at isolated zeros, but they carry one extra power of (q+ε)⁻¹ relative to the |∂v|²/(q+ε) terms available from (Kη).

## 7. Unresolved, and what would resolve it

- **Sign of κ pointwise.** Confirmed only through one exact integral. The radial-divergence computation in §4 would settle it.
- **Untested Δq coefficients.** The coefficients of Re⟨α,K∂_Dv⟩ = ±½ div Im(ηα) and Im(v̄η²) in Δq. These affect (80.R′) only through ⟨dq, Im ηα⟩/(q+ε)² and an algebraic term. They need a non-real (η, v) configuration, for example a direct symbolic derivation in a general adapted frame.
- **The limit lim 32|Y|²/q² on the model end.** It decides the exact layer deficit.
- **The sign structure of (Kη) + 4(Kv).** Under the (q+ε)⁻¹ weight, its remaining transport is ⟨dq, j_η + 4j_v⟩/(q+ε)². The open question is whether its integral combined with (80.R′) yields an upper bound on ∫(24|η|² + 8trV²)/(q+ε). Item (c) of §6 shows any such bound must use the vanishing of η and v relative to √q at zeros, which is not available pointwise.
- **Step 80's model formulas.** They need replacing by those in §3, and the Step-80 §3 table needs recomputing with vol√G = 64p(1+3p²)/(3(1−p²)³).