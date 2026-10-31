# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md",
    "Sessions/S1003A01/workspace/scripts/step28_ak_nu_structure.py",
    "Sessions/S1003A01/workspace/scripts/step28_chern_stokes_check.py",
    "Sessions/S1003A01/workspace/scripts/step28_ak_gap_identity.py",
    "Sessions/S1003A01/workspace/data/step28/ak_nu_structure.json",
    "Sessions/S1003A01/workspace/data/step28/ak_hatted_structure.json",
    "Sessions/S1003A01/workspace/data/step28/gap_lm3_x00.038_X128_d24.json",
    "Knowledge/objects/papers/Local-rigidity-of-certain-classes-of-almost-Kahler-4-manifolds--c0d51aa8ffb7--68f3db154d35/object.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md"
  ]
}
```

## Task

Check the mathematical correctness and scope of Theorem A and its supporting identities in the note step28_AK_gap_identity_nijenhuis_transport.md, for smooth diagonal Bianchi-IX O(-1) cells with an exact complex-hyperbolic collar (perpendicular class), in the units P/(8pi^2) with W dt volume units. Specifically: (1) the claim that g is conformal via u^2=phi/(a_g a_h) to a diagonal almost-Kahler metric with A_f=(A_gA_h)_T/2, and the symbolic formulas for the Nijenhuis scalar nu, kappa-shat=6nu^2, the linear transport lambda=nu_T/2+beta*nu, and the Chern identity as the exact Stokes formula (shat+2nu^2)w=d/dT[4P cosh q - P P'' - P'^2/2] (scripts step28_ak_nu_structure.py and step28_chern_stokes_check.py; compare with Apostolov-Armstrong-Draghici formulas (10),(13) in the supplied paper, including normalization of Omega, kappa, W3 eigenvalue lambda); (2) the four-step proof of Theorem A, especially the U(2) splitting |W+|^2=(3/2)W_ww^2+(1/2)(W_gg-W_hh)^2, the conformal weights (Wff/u^2, |W+|^2 dV invariance), boundary terms at the conical bolt (u^2~ct, phi~ct^2) and at the CH collar, and the use of the inherited relative identity 1-Phat=D_+-36Vexc-Sexc; (3) the bolt Nijenhuis charge law and the asymptotics nu~-1/(2ut), mu~t^{3/2}, and the leading-order cancellation of the 6G and (3/2)N densities at the bolt; (4) the far-field Hardy lemma and the CH Hardy radius x_H=3+(3/4)sqrt(15), including whether the stated inequality and the condition Lambda>=4sqrt3 are correctly derived, and whether the conclusion 'all gain is generated inside sinh^2 R<~6' is supported by the data or needs qualification; (5) the section-5 claims about non-diagonal extension (uniqueness of the relative SD harmonic form when b_+=0, the modulus a=int_E omega, near-symplectic zero sets, expected a-dependence of pinning and Chern terms). Identify any error, hidden assumption, or overstatement, and state the corrected mathematics precisely. Also say what in Theorem A is genuinely new structural information versus a rewriting of the inherited relative Weyl-volume identity.

## Output

# Verification memo: Theorem A (Step 28) and its supporting identities

## Summary

Theorem A is algebraically correct. I checked it line by line from the inherited relative identity, and that inherited identity is itself the relative 2χ+3τ = −1 for one blowup. I found five minor errors in the note: a factor-2 normalization slip, one misstated connection relation, a mislabelled scalar curvature, an unproved converse, and a defective numerical transport check.

The term Σ is not a separate sign-indefinite piece. It combines with 12H into one perfect square, so "only −(3/2)N carries a minus sign" holds without assuming s ≡ −24.

The same Stokes bracket, evaluated at an aligned bolt, gives the a-dependent pinning and Chern terms that §5 anticipates. This produces one exact identity covering both aligned and perpendicular diagonal cells, and it reproduces the inherited Kähler cost (3.2).

The Hardy lemma is correct but crude. The Nijenhuis sector has an exact one-dimensional weighted quadratic-form representation, which also gives a rigorous lower bound on Q_A from the bolt charge K.

---

## 1. Conformal almost-Kähler structure and the symbolic formulas

**Self-duality and pinning.** These are correct.
- In the frame e⁰ = dt, eⁱ = aᵢσᵢ, one has ω = d(φσ_f) = (φ′/a_f)e^{0f} + (2φ/(a_g a_h))e^{gh}. This is self-dual iff φ′/φ = 2a_f/(a_g a_h).
- In hatted variables the same condition reads A_f = P_T/2 with P = A_gA_h, and ω = d((P/2)σ_f).
- Pinning follows because w = A_fA_gA_h = (P²/4)_T.

**Factor-2 slip in u².** The CH Kähler form is d((sinh²t/2)σ_f), so φ = a_ga_h/2 on CH. With φ normalized to the Kähler form, the conformal factor must be u² = 2φ/(a_ga_h). The note's "u² = φ/(a_ga_h) (=1 on CH)" therefore needs a factor 2.
- The script normalizes φ(X) = X = a_ga_h, i.e. φ_script = 2φ_Kähler, so its u is correct.
- The docstring "Pm = 2φ" agrees with the Kähler normalization, not with the note's formula.

**Misstated connection relation.** I re-derived it by hand, substituting A_f = m/2 with m = (A_gA_h)′:

v_g = 𝒩/(2mA_h), v_h = −𝒩/(2mA_g), where 𝒩 = A_h²A_g′² − A_g²A_h′² + 4A_g² − 4A_h².

- Hence v_g/A_g = −v_h/A_h, which is the definition of ν. Equivalently A_h v_g = −A_g v_h.
- The note's "A_g v_g = −A_h v_h" is wrong. The JSON entry `v_g_times_Ag_plus_v_h_times_Ah` is ∝ (A_g−A_h)(A_g+A_h) ≠ 0, confirming this.
- Substituting A_{g,h} = √P e^{±q/2} gives ν = −(q_T + 4 sinh q/A_f)/2 exactly as stated.

**κ − ŝ = 6ν² and the AAD normalizations.**
- With |Ω|² = 2 (AAD's convention), W₁⁺ = (κ/8)Ω⊗Ω − (κ/12)Id has eigenvalue κ/6 on Ω. So κ = 6Ŵ_ωω, and on CH κ = −24, Ŵ_ωω = −4.
- The W₃⁺ eigenvalues are ±λ_AAD. So the note's λ = (Ŵ_gg − Ŵ_hh)/2 is AAD's λ in the gauge μ = 0, which holds automatically by diagonal symmetry.
- Then |W⁺|² = κ²/24 + 2λ². This equals the note's (3/2)W_ωω² + (1/2)(W_gg − W_hh)², and also equals the sum of squared eigenvalues W_ff² + W_gg² + W_hh² with W_gg + W_hh = −W_ff.
- The CH value |W⁺|² = 24 confirms the eigenvalue-norm convention used in D₊.
- AAD (10) gives ν² = |a|², so N = 4∫|a|² dV̂ = ∫|∇ω|²_ĝ.
- The inherited note's N (§6.1) is ½∫|∇ω|² in the scale Ric = −g with physical volumes. The two N's differ by a factor 2 plus unit conversion and must not be compared directly.
- The note's sentence "the |a|² term of AAD (13) cancels" is an interpretive comparison I could not check. The linear law λ = ν_T/2 + βν comes directly from the Cartan computation (JSON entry `lambda`), which I matched term by term: −p₂/(2p₁) = −(A_f)_T/(2A_f) and 4cosh q/p₁ = 2cosh q/A_f.

**ŝ\* is mislabelled.** From AAD (16), ⟨−db, Ω⟩ = s/2 + |a|². So the Chern-relevant integrand is s + 2ν², which is the Hermitian (Chern-connection) scalar curvature (s + s\*)/2. The star-scalar curvature 2⟨R(Ω),Ω⟩ = s/3 + 2κ/3 equals s + 4ν².
- The note's formulas are internally consistent with its own definition ŝ\* = ŝ + 2ν² and κ = ŝ\* + 4ν². Only the name is off.
- ∫(s + 2|a|²) = 4πc₁·[ω] is exactly the identity the inherited §6.1 uses.

**Stokes formula.** The file `chern_stokes_check.json` was not supplied, so I checked independently.
- Flat space, P = T²: the bracket is 0. ✓
- Fubini–Study, P = sin²T: the bracket is 6 sin⁴T, whose derivative is 24w. ✓
- CH, P = sinh²T: the bracket is −6 sinh⁴T. ✓
- At the perpendicular bolt, u ≈ k√t gives P ~ ct², P P_TT ~ cbt, 4P cosh q ~ 2cbt, P_T² ~ t. All tend to 0, so the bracket's bolt value is 0.
- The Theorem A residual of 10⁻¹⁰, which needs both pinning and Chern–Stokes, is an independent numerical confirmation.

**Hidden geometric fact: ω vanishes on the bolt.** Since |ω|_g ∝ u² ∝ t, the canonical form ω vanishes on E. This zero set is two-dimensional, which is not the generic near-symplectic situation.
- ĝ = u²g collapses the whole bolt S² to a point: A_f, A_g ~ √t, A_h ~ t^{3/2}, T ~ t^{3/2}.
- J = ω/|ω| is undefined on E.
- This is also why a = ∫_E ω = 0 trivially, since ω pulls back to zero on E.
- Consequently the Chern term involves no relative first-Chern-class hypothesis: c₁·[ω] sees only the CH background. That is why "the bolt contributes nothing" holds without the hypothesis the inherited §6.1 needed.

**Unproved converse.** "D̂ and Ric₀₀ − Ric_ff both vanish iff ν = 0" is proved only in the "if" direction. Ric₀₀ − Ric_ff = −ν(2ν + 8 sinh q/A_f) also vanishes on ν = −4 sinh q/A_f. Whether that branch is compatible with D̂ = 0 is not settled.

**Interpretation of the Kähler flow at the bolt.** The Kähler squashing flow would require q_t ≈ −2/t. A smooth perpendicular bolt has q_t ≈ −1/t. The forced Nijenhuis term ν ≈ −1/(2ut) is exactly this slope mismatch.

## 2. Proof of Theorem A

**Inherited identity.** I derived 1 − P̂ = D₊ − 36V_exc − S_exc from the relative 2χ+3τ = −1, with Vol = 2π²∫W dt and P̂ = (8π²)⁻¹∫|Ric°|². It is equivalent to

P̂ − 1 = ∫W|W⁺|² dt + ∫W s²/48 dt − 36V_CH.

The second inherited identity, with −5 and ∫|W⁻|², follows from Δτ = −1. Both are correct.

**Streamlined proof (V_exc not needed).**
- Conformal invariance gives ∫W|W⁺|² = ∫|Ŵ⁺|² dV̂. Note Ŵ_ff = W_ff/u², as in the script.
- The U(2) splitting gives (3/2)Q_δ + (1/2)Q_A − 12∫δ dV̂ + 24V̂.
- Expanding the square gives ∫Ws²/48 = 12∫W(u² + s/24)² − 12V̂ − ∫su²W.
- Then use V̂ = V_CH, ∫δ dV̂ = N/6, and ∫su²W = −24V_CH − N/2 − 6G.

**Correction: Σ is absorbed into a square.** Write H_s = ∫W(u² + s/24)² dt. Since 12(u²−1)² + (s+24)(u²−1) + (s+24)²/48 = 12(u² + s/24)², one has 12H + Σ = 12H_s. Therefore

P̂ − 1 = 12H_s + 6G + (3/2)Q_δ + (1/2)Q_A − (3/2)N, exactly, for every smooth perpendicular diagonal cell.

- Check against the data: at x₀ = .07, 12H + Σ = .00829 − .00060 = .00769 ≥ 0.
- The note's sentence "an integrable structure would give P̂ ≥ 1 + 12H" needs s ≡ −24. The correct statement is P̂ ≥ 1 + 12H_s + 6G > 1.

**Endpoint terms and integrability.**
- At the bolt, uu′W ~ t → 0. On the collar, u′ = 0.
- The densities u′²W, ν² dV̂ and δ² dV̂ are respectively ~1, ~1 and ~t, so all are integrable.
- I recomputed the volume formula. In the records its scalar term is not small: ∫(s+24)W ≈ −0.0102 at x₀ = .038, inferred from the inherited identity with the tabulated D₊ and V_exc. So the reading "V_exc = H + G/2 + N/24" omits about 11% of V_exc there.
- The D₊ table checks: 24(.00677) + 2(.0651) − .0340 = .2587 ✓.

**Unified aligned/perpendicular identity.** At an aligned bolt (f collapses, a_f ~ t, a_g = a_h, u smooth and positive):
- P₀ = P(bolt) > 0, P_T → 0, P_TT → 2, q → 0, so the bracket's bolt value is 2P₀.
- On E, ω = P₀σ_g∧σ_h. With ∮σ_f = 2π, ∫_{S²}σ_gσ_h = π, so a = πP₀.
- Hence V̂ = V_CH − a²/(4π²) and ∫ŝ\* dV̂ = −24V_CH − 2a/π.

The same algebra then gives

**P̂ = (1 + 3a/π)² + 12H_s + 6G + (3/2)Q_δ + (1/2)Q_A − (3/2)N.**

- For a Kähler cell (u = 1, ν = λ = δ = 0, s = −24) this reduces to P̂ − 1 = 6a/π + 9a²/π², which is the inherited (3.2) cost 8πt + 2t² converted to Ric = −6g.
- In this formula a enters as ε·a with ε = ⟨c₁(J),E⟩. The diagonal aligned class has εa > 0. A non-Kähler J with εa < 0 would make the linear term sign-indefinite: min over a of (1+3a/π)² − 1 is −1. Whether such a structure exists with an exact collar is open.

## 3. Bolt charge

**Asymptotics.** The note's asymptotics are correct.
- q_t + 4 sinh q/a_f ≈ −1/t + 2/t, so ν ≈ −1/(2ut) ~ t^{−3/2}.
- μ = (ua_f)⁻¹ exp∫4cosh q/a_f ~ t^{−1/2}·t² = t^{3/2}.
- The t^{−3} terms in ν_T/2 + βν cancel at leading order (β ≈ 3/(4ut)), consistent with μν → K.
- λ ~ −0.27/t in the data, so μλ dT ~ t dt is integrable.
- The densities 6u′²W and 6ν²dV̂ both tend to (3/2)k²b² with k² = c.

**Numerical confirmation needs a coordinate correction.** The profile's t is `np.cumsum(dtdx*wxs)`, a cumulative quadrature-weight sum, which runs about 1×10⁻⁶ ahead of the node's actual t near the bolt. After correcting for this, the first three profile points give u²/t = 5.906, 5.906, 5.906 and ν·2ut = −1. This confirms both u² ∝ t and the ν asymptotic.

**New rigorous consequence.** Put ψ = μν and ρ = w/μ². Then λ = ψ_T/(2μ), and therefore:
- Q_A = ∫ρψ_T² dT and (3/2)N = 6∫ρψ² dT;
- ψ(bolt) = K ≠ 0 and ψ(collar) = 0;
- Q_A ≥ K²/∫ρ⁻¹ dT, which is finite since ρ⁻¹dT ~ t dt at the bolt.

This makes "the charge must be unwound by W₃⁺" a capacity inequality.

## 4. Hardy lemma and "all gain inside sinh²R ≲ 6"

**Derivation.** The derivation and constant are correct: (log ρ)_T = Λ, with Λ given by the script's formula.
- On CH, ρ ∝ cosh¹¹T/sinh³T, so Λ = 11 tanh − 3 coth = (8x−3)/√(x(1+x)).
- Solving 16x² − 96x + 9 = 0 gives x_H = 3 + (3/4)√15 ≈ 5.905. The other root has Λ < 0 and is spurious.

**Wording correction.** "Wherever Λ ≥ 4√3" must read "on a terminal interval [T₀, T_collar] on which Λ ≥ 4√3", because ψ(T_collar) = 0 is used.

**Exact representation of the Nijenhuis sector.** The sector is exactly ∫ρ(ψ_T²/2 − 6ψ²) dT. So its sign on a tail is decided by the first eigenvalue of −ρ⁻¹(ρψ′)′, with a natural condition at T₀ and Dirichlet at the collar, compared with 12. Hardy is a sufficient bound, and x_H overestimates the sharp radius.

**Data support (x₀ = .038 record only).** The decomposition is reproduced: near sector .0601 − .0707, far sector .00588, ratio .175. However:
- The cumulative total has two gain windows, t ≈ 0.15–0.55 (−.0167) and t ≈ 1.1–1.6 (−.0024).
- It has two cost windows, 0.55–1.1 and beyond x_*, and the bolt zone is about +.00065 by t ≈ 0.12.
- So "gain in 0.1 ≲ t ≲ 0.7" is incomplete.
- Localization depends on the density representation; for example, 6u²a_f v_g v_h redistributes it.
- x is the cell coordinate, equal to sinh²R only on the collar.
- The other two records appear only through summary numbers.

**Script defects.**
- `transport_rel_residual_max = 2×10⁷` is an artefact: `np.gradient` is applied with the biased `tt` across Gauss panels, where ν ~ t^{−3/2}. It is not evidence against the exact symbolic law.
- `law_residual` is hard-coded to 0 (`if False`).
- The integrated charge law (10⁻¹²) is the valid check.

## 5. Non-diagonal extension (§5)

**Uniqueness.** This is correct. A difference η of two closed self-dual forms that agree on the collar is compactly supported, and ∫η∧η = ∫|η|² ≥ 0 while the H²_c intersection form is (−1). Hence η = 0. Unique continuation for d + d\* gives the same conclusion.

**Existence is the real issue.** The system dω = 0 on Λ⁺ (rank 3 → 4) with exact Cauchy data on the collar is overdetermined. Existence holds in the diagonal class by integrating an ODE, and generically does not hold otherwise. So a(g) is not defined on all metrics. The alternative is the global harmonic self-dual plane on the closed manifold, where a becomes a period-map coordinate.

**Near-symplectic genericity.** The generic one-dimensional zero set is a closed-manifold genericity result. It does not transfer automatically to forms with prescribed collar data. The diagonal perpendicular zero set is two-dimensional. The Chern and pinning contributions of zero circles remain unresolved.

**W₂⁺ norm.** With W⁺ written in block form [[κ/6, wᵀ],[w, W₃−κ/12]], one has |W⁺|² = κ²/24 + 2|w|² + |W₃|². "2|W₂⁺|²" is correct only if |W₂⁺| means |w|.

**§5.1 restriction.** The condition "v = u⁻¹ solves 6Δ̂v + ŝv + 24v³ = 0" restricts to s ≡ −24. With ℓ = log u⁻¹, the full diagonal problem has conformal sector

(1/48)∫(6Δ̂ℓ − 6|dℓ|² + ŝ + 24)² dV̂ + 6∫|dℓ|² dV̂,

with ℓ free subject to the bolt and collar asymptotics. The bolt neutrality ν ≈ ℓ_T is the coupling a sharp bound must exploit.

## 6. What is new versus rewritten

**Equivalent to inherited material.** Theorem A, as an equality, is equivalent to the relative 2χ+3τ identity. In particular it gives no inequality.

**Genuinely new structural information:**
1. Every perpendicular diagonal cell carries a canonical conformal almost-Kähler structure, degenerate exactly along E. Its pinning and Chern integrals are exact, with zero contribution from E and no c₁ hypothesis. This is the a = 0 counterpart of the inherited §6.1 balance, but as an equality with pointwise squares rather than Cauchy–Schwarz remainders.
2. The square form shows that the only term with a minus sign is (3/2)∫|∇ω|²_ĝ.
3. The linear transport law, the forced charge K ≠ 0, and the exact ψ-representation together give Q_A ≥ K²/∫ρ⁻¹ and reduce the Nijenhuis sector to a weighted one-dimensional spectral problem.
4. The same bracket gives the unified a-dependent identity.

**What a lower bound still needs.** A near-zone inequality coupling ψ (equivalently ν) with ℓ and δ for x ≲ 6.