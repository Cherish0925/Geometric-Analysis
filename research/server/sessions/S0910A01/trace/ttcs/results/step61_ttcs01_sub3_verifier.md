# TTCS Independent Branch Record

```json
{
  "step_id": 61,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step58_critical_to_subcritical_bridge.md",
    "Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md"
  ]
}
```

## Task

Audit the curvature Moser endpoint for the restricted four-dimensional cutoff flow ∂_t g = -2aE, a=χ², E=Ric+g. The claimed endpoint (A03 Step 58) is ‖aF_T(t)‖_∞ ≤ CΓ/t, where F_T=(1+|T|²)^{1/2}, T=Rm+G, Γ=sup(S·H^{1/2}), H=∫η²F². Read the derivation and test for gaps: (1) The H-inequality (eq 1.1): H'+c₀D ≤ C₀Y + C₁(1+r^{-2})H. This comes from 'the tensor calculation of Step 57' — is that tensor calculation actually at proof level, or is it schematic? Check A03 Step 57 (H2_evolution_and_continuation_bridge) if available. (2) The critical absorption Y ≤ Cγ(D+r^{-2}H) uses the localized H=∫η²F² and the maximal-function good support with γ=SH^{1/2}≤Cr²√K₀. Is the smallness of γ justified from the initial data alone (maximal-function threshold), or does it need a first-exit argument? If first-exit, is the bootstrap correctly coupled to the V=∫‖aE‖_∞ metric drift? (3) The q=3 propagation (§3): Y(τ) ≤ CΓH(0)/t from a good slice, then Gronwall with coefficient ∫(1+r^{-2}+S²Y) ≤ Cγ³ + Cr^{-2}t. Verify the Gronwall exponent bound. (4) The Moser iteration (§4): check the recurrence (4.3)-(4.7) and the product convergence (4.8). Does the L_j coefficient with time-cutoff 4^j/t and the S factor give the claimed exponents -3/p₀=-1 (time) and 2/p₀=2/3 (Sobolev) for p₀=3? (5) The final estimate ‖aF(t)‖_∞ ≤ CΓ/t: verify the S^{2/3}(ΓH(0))^{1/3} → Γ reduction uses SH(0)^{1/2}≤Γ correctly. (6) CRITICAL: is this endpoint derived under assumptions that were later repaired? Specifically, the Step 55 joint (Γ,V) bootstrap replaced the assumption S(t)≤2S(0) with Ŝ=e^{8V}S₀. Does the curvature endpoint still work under the repaired bootstrap, or does it assume the old S(t)≤2S(0)? Be explicit about what is proved, what is conditional, and what needs repair.

## Output

# Verification memo: the Step 58 curvature Moser endpoint ‖aF_T(t)‖_∞ ≤ CΓ/t

**Materials read:** A03 `step58_critical_to_subcritical_bridge.md` (the endpoint derivation), A01 `step55_joint_bootstrap_background_continuation_repair.md` (the (Γ,V) repair), A01 `step34_integrated_potential_q3_and_defect.md` (q=3 propagation, defect persistence, and the most recent in-record status list for the tensor layer). **A03 Step 57 (`H2_evolution_and_continuation_bridge`) was not among the supplied files**; where its content matters I say so and use Step 34 §7 as the last inspectable status. I re-derived every algebraic identity, Hölder/Young split, exponent sum, and scaling in the endpoint chain independently of `step58_critical_subcritical_verify.py` (54/54). My computations agree with the script on everything within its reach; below I mark the points no algebra script can reach.

---

## Q1. The H-inequality (1.1): verified testing architecture, premise-level tensor source

**What checks out structurally.** The relative-form repair is correct and is the right repair. Because ∂_tg = −2aE, every term in ∂_t|T|² and in ∂_tdμ carries a, da, or ∇²a; hence every zero-order term in the tested p=2 identity has one of the forms ∫η²a, ∫η²aF, ∫η²aF², ∫η²aF³. With 0≤a≤1 and F≥1, (1.2) bounds the first three by H and the last is Y. The ∫η²a term arises concretely from measure variation on the constant part of F² = 1+|T|²: ∫η²·1·(−a·tr E) ≤ C∫η²aF ≤ CH. So no Vol(M)-additive constant is structurally possible, and Step 57's displayed constant (if present) was a bounding artifact. The shift T = Rm + G, G = g⊙g/(2(n−1)), is sound: ∇G = 0 gives ∇T = ∇Rm, ∂_tG = h⊙g/(2(n−1)) is algebraic with |∂_tG| ≤ CaF, and the Ricci-trace of T is exactly Ric + g = E, which is what couples the defect hierarchy to T without dividing by a. I also re-did the p=2 signed-Hessian absorption: with |B| ≤ CF², |∇B| ≤ CF|∇T|, one IBP on ∫η²(∇²a)B gives |∇a||∇B| ≤ (Ca^{1/2}/r)(F|∇T|) ≤ εD + C_εr^{−2}H; the dη-term vanishes because supp(∇a) ⊂ supp χ ⊂ {η = 1}. The support geometry (supp a ⊂ {η=1}, a = da = 0 on supp dη) does real work here, in (2.1), and in (4.2).

**What is not inspectable at proof level.** The pointwise curvature identity behind (1.1) — the all-lower variation ∂_tR_{ijkl} under ∂_tg = −2aE with correct normalization bookkeeping, the cubic reaction aT*T*T feeding Y, and the derivative-structure bound |∇B| ≤ CF|∇T| — is cited from "A01 Steps 34–35 together with the shifted T calculation in A03 Step 57." The supplied Step 34 note, §7 items 1–2, lists exactly these as **unproved** ("complete the index-level all-lower curvature variation … including the normalization coefficients and the derivative-structure bound (2.10)"). Step 57 postdates Step 34 and may have closed this, but no supplied artifact displays that closure; the 54/54 script covers algebra/exponent identities only. The same status applies to (3.3)/(3.4) for p ≥ 3 (including "N ≤ 5," which affects constants only — any finite N survives the Moser products).

**A concrete checksum for the missing computation** (Step 34 §2 already identified the trap): substituting aE = g (pure scaling on the plateau) must return ∂_tR_{ijkl} = −2R_{ijkl} exactly, and in dimension 4 the tested identity must reproduce the exact invariance of ∫|Rm|²dμ (|Rm|² gains 4|Rm|² from four inverse metrics, dμ loses 4dμ). Any sign error in the normalization/conformal terms surfaces here in one line. The defect side needs the analogous Bianchi-based identity (Step 34 (5.4)) with the signed contraction (5.8), |B^E| ≤ Cs, |∇B^E| ≤ Cs^{1/2}|∇E|.

**Verdict on (1):** (1.1) is a precisely specified premise whose testing architecture, signed-IBP absorption, and relative-form repair I verified end-to-end; its proof-level status rests entirely on Step 57, which is not in the supplied record.

## Q2. Smallness of γ: initial scale choice, then a correctly coupled first-exit

The absorption (2.1)–(2.4) itself I verified in full: Y = ∫F(χF)² on the matched support (η=1 on supp χ), Cauchy–Schwarz, Sobolev on w₂ = χF (Lipschitz, |dF| ≤ |∇T|), giving **Y ≤ Cγ(t)(D + r^{−2}H) pointwise in time, no smallness needed**. Smallness is needed only to absorb the D-term into c₀D, i.e., γ(t) ≤ c₀/(2C₀C) at *every* time.

- **At t = 0:** γ(0) ≲ r²√K₀ from S(0) ≲ r²V^{−1/2} and H(0) ≲ K₀V; the V-cancellation (2.9) is arithmetically correct. Both inputs are selection-layer outputs (maximal-function good support), not proved in the supplied notes. The S-scaling is the load-bearing geometric premise: the lower bound S ≳ r²V^{−1/2} is forced by test functions, so the premise is the *matching upper bound* on a collapsed support — it deserves dedicated verification in the selection layer, since both (2.9) and the defect-seed volume cancellation rest on it.
- **For t > 0:** persistence is exactly the provisional half of a first-exit argument. Initial data alone do not give it. Step 55 supplies the coupling, and I verified its mechanics: the bilipschitz transport (1.5)–(1.8) is correct (‖u‖_{4,t}² costs L^{n−2}, the gradient term L^{n+2} is dominant, hence S(t) ≤ L^{2n}S(0) = e^{8V}S(0) in n=4); the γ-improvement (1.11)–(1.13) arithmetic is correct (exponent (2n + C_V/2)V* + C_Hθ ≤ log(3/2), γ(0) ≤ γ*/2 ⟹ Γ ≤ 3γ*/4); and I independently re-derived the defect endpoint scaling used for the V-leg: from J₆ ≤ Cδ⁶V and (6.1) with p₀ = 6, S^{1/3}t^{−1/2}(δ⁶Vt)^{1/6} = δS^{1/3}V^{1/6}t^{−1/3} = δ(r²/t)^{1/3} — the V^{±1/6} cancellation checks — giving V(T) ≤ (3/2)C_Eδθ^{2/3}r² and the condition (1.17).

**Bootstrap logic:** the absorption at time s uses γ(s) within the provisional region; the defect endpoint feeding the V-leg is itself derived under the same provisional Γ (Step 34 (5.12) needs Cγ < c/2); the improvements then show the exit time is not reached before θr². No vicious circle. Constant ordering is consistent: c₀, C₀ fix γ*; C_H, C_V fix V*, θ via (1.12); then initial conditions r²√K₀ ≤ γ*/2 and δ ≤ V*/(3C_Eθ^{2/3}r²). What remains conditional: the defect tensor identities, the *simultaneity* of H(0) ≤ K₀V ∧ ‖E(0)‖_∞ ≤ δ ∧ cutoff quality on one support, and smooth existence of the degenerate flow on the provisional interval.

## Q3. q=3 propagation: correct and non-circular

The three-factor identity (3.5) is exact (a-exponents (1 + p−2 + 2(p−1))/3 = p−1; F-exponents (3 + p + 2p)/3 = p+1); the Hölder (3,3,3) yields Y^{1/3}K_p^{1/3}‖z_p‖_4^{4/3} with all η-bookkeeping harmless since supp a ⊂ {η=1}; Young (3, 3/2) gives εX + C_εS²YK_p. The z₃ = ηaF^{3/2} correction is right: z₃² = η²a²F³ matches the a²-weighted D₃^T, D₃^F; the a^{1/2}F^{3/2} variable genuinely mismatches. The good slice (3.7) is a mean over [t/4, t/2] (length t/4) ✓. The Gronwall exponent is ∫_τ^t(1+r^{−2}+S²Y) ≤ 2θ + CA²Γ³ for t ≤ θr², r ≤ 1 — matching the task's stated Cγ³ + Cr^{−2}t form since r^{−2}t ≤ θ. **Non-circularity confirmed:** the integrability of S²Y is established at the q=2 level ((2.7)–(2.8)) before (3.4) is ever integrated; no q=3 pointwise information feeds its own coefficient.

## Q4. The Moser iteration: recurrence, products, and exponents all verify

- **(4.2):** ∇z_p has three terms; the middle one costs p·a^{(p−2)/2}/r via |∇a| = 2a^{1/2}|∇χ|; the p² coefficient and the r^{−2}K_p term are correct; the dη-term vanishes on supp a.
- **(4.3):** time-cutoff slope |φ′| ≤ C2^{j+2}/t ≤ 4·4^j/t ✓; the extra p^{+2} in L_j absorbs (4.2)'s p² ✓.
- **(4.5):** interpolation exponents exact ((p−2)/2 + (2p−2)/2 = 3p/2 − 2); K_{2p} = ‖z_p‖_4⁴ ✓.
- **(4.6):** re-derived independently: ∫_{I_{j+1}}K_{3p/2} ≤ (sup_{I_{j+1}}K_p)^{1/2}·∫_{I_{j+1}}‖z_p‖_4² ≤ (L_jM_j)^{1/2}·CS(L_j + r^{−2})M_j ≤ 2CS(L_jM_j)^{3/2} using L_j ≥ r^{−2} — matches both the "precise" and simplified displays.
- **(4.7):** 3/(2p_{j+1}) = 1/p_j and 1/p_{j+1} = 2/(3p_j) ✓.
- **(4.8):** ∑p_j^{−1} = (1/3)·3 = 1 = 3/p₀; ∑j/p_j = (1/3)·(2/3)/(1/3)² = 2, so the 4^j factor costs exactly 4² = 16; ∑(log p_j)/p_j < ∞. **Time exponent −∑1/p_j = −1 = −3/p₀ ✓; Sobolev exponent (2/3)∑1/p_j = 2/3 = 2/p₀ ✓** — the stated exponents are correct.
- **Parenthesis:** t^{−1} + 1 + r^{−2} + A²Γ³t^{−1} ≤ C(θ, Γ*, A)/t on the provisional interval (1 ≤ r^{−2} ≤ θ/t, Γ ≤ Γ*) ✓, so the enlargement below (4.4) is valid.
- **Seed (4.9):** ∫_{t/2}^t Y ≤ CΓH(0) from (2.7) ✓.
- **Endpoint identification:** K_{p_j}(t)^{1/p_j} ≤ L_{j−1}^{1/p_j}m_{j−1} → m_∞. The limit K_p(t)^{1/p} → ‖aF(t)‖_∞ is cleanest run through the *finite* measure η²dμ with a^{1−2/p}F ↑ aF on {a>0} — this avoids the singular a^{−2}-weight framing and is the form worth recording for later formalization.
- **Robustness:** any ratio in (1,2) would converge; 3/2 is not tight; the Hölder chain (2.1) at the seed level is exactly L²-critical in both factors, so the absorption is sharp and no premise in the chain has slack.

## Q5. The final reduction: correct

Ŝ^{2/3}(ΓH(0))^{1/3} = Γ^{1/3}(ŜH(0)^{1/2})^{2/3} ≤ Γ^{1/3}(Aγ(0))^{2/3} ≤ A^{2/3}Γ, using only Ŝ ≤ AS(0) and γ(0) ≤ Γ. Dimensionally consistent (S·H^{1/2} is dimensionless in n=4; Γ/t has curvature units). A useful arithmetic observation: since the improvement gives Γ ≤ (3/2)γ(0) ≲ r²√K₀, the plateau bound at t = θr² is |Rm| ≲ Γ/(θr²) + 1 ≲ √K₀/θ + 1 — the working scale r cancels, which is the designed collapse-uniformity, and it survives the algebra. Downstream consumers may prefer the endpoint stated with the fixed threshold γ* (Γ ≤ 3γ*/4) rather than the running Γ.

## Q6. Compatibility with the repaired (Γ,V) bootstrap: the endpoint survives verbatim

This is the cleanest part of the reading. **Step 58 never uses A = 2 or S(t) ≤ 2S(0).** It writes (2.8) as "if S(s) ≤ CS(0)," introduces a generic transport factor A in (3.8), and carries A²Γ³/t in (4.4). Substituting A = e^{8V*} from Step 55 (1.8) leaves every display structurally unchanged; all A-dependence is a fixed number once V* is frozen by (1.12). The only places the old "≤ 2S(0)" convention appears in the supplied record are Step 34 (0.4) and the B(t) ≤ Cγ³ display (3.7); under the repair these read CA²γ³ — same content, fixed constant. The slab reaction sup in (4.4) is legitimate because (3.8) applied at each s ∈ [t/2, t] gives S(s)²Y(s) ≤ 2CA²Γ³/t. **No circular use:** the curvature endpoint is not an input to the V-improvement (which uses only the defect endpoint); it is consumed downstream (plateau curvature (1.19), terminal pullback geometry).

One **display-alignment item**: Step 58 (2.6) integrates the H-equation without the C_V‖aE‖_∞H term that Step 55 (1.9)–(1.10) retains (Step 58 §1 explicitly defers it). Inside the joint bootstrap the H-growth factor is exp{2C_Hθ + C_VV*}, not e^{Cθ}. Constants only, but the assembled proof should cite (1.10), not (2.6).

## Status summary

**Verified here at algebra/architecture level** (independent of the script, agreeing with it): the relative-form repair of (1.1); the critical absorption (2.4) and absorbed estimates (2.5)–(2.8); the collapse cancellation (2.9); the q=3 slice/Gronwall (3.7)–(3.8) and its non-circularity; the full Moser recurrence (4.2)–(4.7) with convergent products (4.8) and the stated exponents −1 (time) and 2/3 (Sobolev); the seed (4.9); the endpoint (4.10) and the Γ-reduction (4.11); compatibility of the entire chain with A = e^{8V*}.

**Conditional on premises not demonstrated in the supplied record:** (i) the index-level tensor identities behind (1.1) and (3.4) — all-lower Rm variation with correct normalization (pure-scaling checksum), |∇B| ≤ CF|∇T|, cubic reaction into Y — cited from Step 57, not inspectable here, last in-record status "open" (Step 34 §7 items 1–2); (ii) the defect-side Bianchi identity behind the V-leg; (iii) the selection-layer outputs: one support carrying H(0) ≤ K₀V, S(0) ≲ r²V^{−1/2}, ‖E(0)‖_∞ ≤ δ, and buffered cutoffs simultaneously; (iv) smooth existence of the degenerate flow on the provisional interval; (v) N ≤ 5 (constants only).

**Alignment items for assembly:** cite (1.10) rather than (2.6) for H-growth inside the bootstrap; record A = e^{8V*} explicitly in (2.8)–(4.11); record the finite-measure ess-sup identification; the three non-algebraic analytic steps a formalization would need as lemmas are the good-slice mean-value step, the continuity of t ↦ (Γ(t), V(t)) on smooth segments for the first-time argument, and that ess-sup identification.

**Position of the result:** even with (i)–(iv) closed, (4.11) is an a priori estimate on one selected support of the restricted four-dimensional Ishida–LeBrun σ<0 laboratory, under near-critical initial smallness (γ(0), δ). The common observation time, positive-time continuation across the small-a collar with coupled cutoff jets (the χC₄*U versus ∂_tC₃ ⊃ U₂ pairing noted in Step 58 §5), recovery of the restart norm, terminal calibration and forbidden-germ selection all remain upstream of any theorem — and the positive branch, arbitrary 4-topology, dimensions n ≥ 5, and dimension-only constants of the Yau 26 statement remain outside what this module addresses.