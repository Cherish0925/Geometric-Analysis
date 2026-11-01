# TTCS Independent Branch Record

```json
{
  "step_id": 66,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step65_cell_exceptional_flux_ledger.md",
    "Sessions/S1003A02/workspace/notes/step66_rank_one_exceptional_ricci_rigidity.md",
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md",
    "Sessions/S1003A02/workspace/scripts/step66_rank1_bianchi_check.py",
    "Sessions/S1003A02/workspace/data/step66_rank1_bianchi_check.json"
  ]
}
```

## Task

Verify, as a careful differential geometer, the identities and theorems in two notes about the Einstein-defect ledger on M = X#kCP̄² (X minimal general type). (1) Step-65 identities 65.1–65.3 (file step65_cell_exceptional_flux_ledger.md §1): the claim that for every orthogonal J the ASD part of R(Ω) equals B_gΩ (B_g the Ric° block Λ⁺→Λ⁻), the metric-only pairing ⟨t_J⁻,h⟩ = 2π⟨a,h⟩ − ∫⟨Ω,B*h⟩, the definition 𝔉_h=√2∫|B*h|, the Cauchy–Schwarz bound P/2 ≥ 𝔉²/‖h‖² (check the constant using |Ric°|²=4|B|²), and the ledger p=(1−δ)²/‖h‖²+L. (2) Step-66 (file step66_rank_one_exceptional_ricci_rigidity.md): Prop 66.Y (WLOG constant scalar curvature since P(g)−P(ĝ)=(1/12)(∫s²−Y²)≥0 for Y<0); Lemma 66.D div(φ∘ψ)=ψ(δφ) for SD φ and closed ASD ψ (symbolic check JSON supplied); the splitting L = L_rank + L_amp and the equality characterization B = cΩ̂₀⊗h; Theorem 66.R (constant s ⇒ Ω₀ closed hence almost-Kähler with J-invariant Ricci, ρ₀ ∝ h harmonic; extension across Z(h) via H³(Z)=0; converse via AAD (26) dρ=*(JδRic'')); Theorem 66.EM (L_rank=0 with constant s ⇔ Riemannian Einstein–Maxwell Ric°=φ∘h=½(F∘F)₀ with F=φ+h harmonic; check the factor ½ and the boundedness hypothesis near Z(h)); identities (66.3)–(66.5) obtained by inserting γ⁻=ρ₀+t⁻ into Prop 63.AK P=2‖γ⁻‖²+∫u(5u+s)+2‖ρ*''‖²+4‖W₃‖² with |t⁻|²=u²/2 and P=2‖ρ₀‖² when Ric''=0; Corollary 66.S (s≥0 ⇒ δ_b∈[−½,0], Kahler tariff p≥|b⁻|²); Prop 66.W weak estimate. Report precisely any sign, factor, quantifier, or regularity error, whether each statement is proved as written, and the corrected statement where needed. Also judge whether the interpretation in §5 (equality class = Einstein ∪ cscK ∪ strictly-AK J-invariant-Ricci with [ρ₀]∥a⁻; strictly-AK part = the open 4D Blair–Ianus problem at negative constant s) is accurate.

## Output

# Verification memo: the Einstein-defect ledger, Steps 65–66

## Summary

The core mathematics holds. The following are correct:

- the frame identity 65.1 and the bound 65.2, including the constant;
- Lemma 66.D;
- the regularity argument in 66.R;
- the algebra behind (66.3)–(66.5) and 66.S;
- the Einstein–Maxwell reformulation.

The problems are of five kinds:
1. One inequality in 65 §1 points the wrong way.
2. The normalization of δ is not invariant under rescaling h, and the Step-65 table columns do not reconcile under any normalization I can reconstruct.
3. One description of the amplitude condition is wrong.
4. The stated reason for Y < 0 does not cover p_g = 0 surfaces.
5. The §5 interpretation calls the equality class "precisely" the Blair–Ianus problem and gives δ_b ∈ (0,1). Both readings go beyond what was proved.

Details follow.

---

## 1. Step 65, §1

**ASD part of R(Ω).** The curvature operator has block form [[W⁺ + s/12, Bᵀ],[B, W⁻ + s/12]]. For Ω ∈ Λ⁺ this gives R(Ω)⁻ = BΩ, for every orthogonal J, with no integrability needed.

**Norm of B.** In the form norm |e¹∧e²| = 1:
- The Ricci part of Rm is Z = ½ Ric°⊙g, with |Ric°⊙g|² = 8|Ric°|². So the tensor norm is |Z|² = 2|Ric°|².
- As an operator on Λ² with unit basis, its norm is ¼·2 = ½|Ric°|². This is shared between the blocks B and Bᵀ.
- Hence |B|² = |Ric°|²/4 and ‖B‖² = P/4. ✓

It is consistent with 63.T. If B = Ω̂⊗ψ, then |BΩ|² = 2|ψ|² = ½|Ric₀′|².

**65.1.** For harmonic ASD h, ∫⟨γ_J, h⟩ = ∫⟨γ_J⁻, h⟩. The exact part of γ_J is L²-orthogonal to h, so ⟨γ_J⁻, h⟩ = 2π⟨h_a, h⟩. Then ⟨ρ₀, h⟩ = ∫⟨BΩ, h⟩ = ∫⟨Ω, B*h⟩, and the sign t = α∧β matches 63.1. Here ⟨a,h⟩ must mean the L² pairing of the harmonic representative of a with h, i.e. −a·[h]. **Correct.**

**65.2.** Pointwise |⟨Ω, B*h⟩| ≤ √2|B*h|. Then

  𝔉 ≤ √2∫|B||h| ≤ √2‖B‖‖h‖ = ‖h‖√(P/2).

So P/2 ≥ 𝔉²/‖h‖². **The constant is correct.**

**65.3 and the definition of δ.** The ledger identity that holds for any h is

  p = 𝔉²/(4π²‖h‖²) + L.

- With the note's δ := 1 − 𝔉_h/(2π⟨a,ĥ⟩), the δ-term is not homogeneous of degree 0 in h, because 𝔉 is built from h but the pairing uses ĥ.
- The scale-invariant definition is **δ := 1 − 𝔉_h/(2π⟨a,h⟩)**. With it:
  - p = ⟨a,ĥ⟩²(1−δ)² + L, the same form as 66.4;
  - every class-a J satisfies ⟨t⁻,ĥ⟩ ≥ 2π⟨a,ĥ⟩δ.
- The written form (1−δ)²/‖h‖² is this identity under the normalization ⟨a,h⟩ = 1. The cell's ∫_E h = 1 gives exactly that.
- The note should state this definition and normalization explicitly.

**Misalignment description.** Equality in both Cauchy–Schwarz steps means B = λΩ̂⊗h with |B| = c|h|, c constant. So the amplitude part of L vanishes iff **|B|/|h|, equivalently |B*h|/|h|², is constant**. The note's "|B*h|/|h| constant" is wrong. 66 §2bis states it correctly as |φ_h| constant.

**The saving inequality is reversed.** The exact identity, under ⟨a,h⟩ = 1, is

  1 − p = 2δ − δ² − L − (1−δ)²(‖h‖⁻² − 1).

- Since (1−δ)² ≤ 1 and ‖h‖⁻² − 1 ≥ 0, the exact value is ≥ the note's 2δ − δ² − L + (1 − ‖h‖⁻²).
- So the stated "≤" fails whenever 0 < δ < 2 and ‖h‖ < 1. The excess is δ(2−δ)(‖h‖⁻² − 1).
- The correct statements are the exact identity above, or 1 − p ≤ 2δ − δ² − L when ‖h‖ ≤ 1.
- At x₀ = .03 the difference is about 1e-5, below table rounding, so the numerics do not expose it.

**Table consistency (unresolved).** With ⟨a,h⟩ = 1, δ should equal 1 − 𝔉/2π.

| x₀ | 1 − δ (table) | 𝔉/2π (table) |
|---|---|---|
| .03 | 0.99451 | 0.99459 |
| .07 | 0.99124 | 0.99153 |
| .15 | 1.0039 | 1.00469 |

- No other normalization reconciles these: using ‖h‖ in place of 1 gives δ = 0.00592 at x₀ = .03.
- Recomputing from the 𝔉 column gives Hodge 0.99023 and L 0.00543. The table has 0.99008 and 0.00558.
- The mismatch is about 1.5% of δ at the certified cell and 3% at .07. It does not change the structural readings (L/δ ≈ 1), but the ratios sav/δ and L/δ are uncertain at that level.
- Resolving it requires the script's exact definition of 𝔉 (integration domain) and of ‖h‖_{supp Ric°}.

**§5′.** The minimization is correct. p ≥ (1−δ)² + cδ has minimum c − c²/4 at δ = 1 − c/2 for c < 2, and minimum 1 at δ = 0 for c ≥ 2.

---

## 2. Step 66

### 66.Y (reduction to constant s)

- Gauss–Bonnet in the form P = 2∫|W|² + ∫s²/12 − 16π²χ is correct.
- The conformal invariance of ∫|W|² and the inequality ∫s² ≥ Y² for Y < 0 (equality iff s is constant) are correct. Both sides are scale-invariant in dimension 4.
- **Correction to the stated reason.** "b⁺ > 1 and SW ≠ 0" does not cover minimal general-type X with p_g = 0, where b⁺ = 1 (Godeaux, Barlow, …). The needed input is σ(M) < 0, LeBrun's Yamabe invariant of general-type surfaces and their blow-ups. That forces Y[g] ≤ σ(M) < 0 for every conformal class. The source citation should be checked in Knowledge.
- The parenthetical identity 3∫(Δu/u)² + 24∫|∇u|² was not checked here. Its measure and normalization need stating.

### 66.D (divergence of φ∘ψ)

Write T_ab = φ_ac ψ_cb. Then

  ∇_a T_ab = (∇_a φ_ac) ψ_cb + φ_ac ∇_a ψ_cb.

- The first term is (ψ(δφ))_b, using δφ_c = −∇_aφ_ac and the skewness of ψ.
- The second term is φ_{AB}∇^{AA′}ψ_{A′B′}. It vanishes for closed ASD ψ by the spinor Maxwell equation.
- The identity is first order and tensorial, so the flat check transfers to curved metrics at a point.
- The script does the following:
  - tests one random SD φ (quadratic) against one random closed linear ASD ψ;
  - fixes κ₁ = 1 from one component and confirms it in the other three;
  - runs the non-closed ψ control.
  
  This is strong evidence for an identity that is bilinear in (φ, ψ). The spinor argument is the proof.
- The JSON entry for δφ = −*dφ is a string, not a computation. The fact itself is standard: δ = −*d* on 2-forms in dimension 4, and *φ = φ.

**Proved.**

### Equality characterization and the L split

- The algebra of L_rank + L_amp is correct. The second bracket is ≥ 0 by Cauchy–Schwarz with weight |h|².
- The relation to 65.3 is L = (1/2π²)(L_rank + L_amp).
- The equality case is B = cΩ̂₀⊗h on M∖Z(h), with c constant and Ω̂₀ = B*h/|B*h| (smooth, no sign ambiguity).
- The conversion to Ricci is Ric° = c′Ω₀∘h with c′ = √2c up to sign, using |φ∘ψ|_Frob = |φ||ψ|.

### 66.R (rank-one rigidity)

**(a)** The relation div Ric° = ds/4 is correct. With h⁻¹ = −2h/|h|²,

  δΩ₀ = h⁻¹(ds)/(4c′) = −h(ds)/(2c′|h|²). ✓

**(b) Extension across Z(h).**
- Bär's theorem applies because d + d* is of Dirac type and h ≢ 0, so dim_H Z(h) ≤ 2.
- Then H³(Z) = 0, so Lipschitz cutoffs with ∫|dχ| → 0 exist.
- A bounded SD form that is closed off Z is weakly closed and weakly coclosed, hence smooth harmonic, and |Ω₀|² ≡ 2.

**Correct.**

**(c)**
- Ω₀∘h commutes with Ω₀ (SD and ASD forms commute), so Ric is J₀-invariant.
- ρ₀ = B(Ω₀) = √2c·h is harmonic.

✓

**(d)** AAD (26) with Ric″ = 0 gives dρ = 0. With s constant, ρ₀ is closed, hence harmonic ASD. Two refinements:
- The condition is a statement about forms, ρ₀ ∈ ℝ·h_a⁻ (g-dependent), not about classes.
- The case ρ₀ = 0 is Einstein. Strictly-AK Einstein metrics (a counterexample to the negative Goldberg conjecture) would lie in both (E) and the AK_Ric class.

**cscK remark.** For Kähler metrics p = |c₁(J)⁻|². Writing "= k + Π" assumes c₁(J) is the best-sign class. The Kähler canonical class c₁(X) − ΣE_i need not be.

**66.R is proved as written,** modulo citing Bär and AAD (26).

### 66.EM (Einstein–Maxwell layer)

- **Factor ½.** φ and h commute, and φ∘φ, h∘h are scalar. So (F∘F)₀ = 2φ∘h and ½(F∘F)₀ = φ∘h. ✓
- **Normalization relative to LeBrun's convention** (Ric + F∘F)₀ = 0:
  - take F = (φ_h − h)/√2;
  - the sign is absorbed by h → −h, which changes nothing in the ledger;
  - so the factor ½ is a normalization of F, not a separate equation.
- The constant-s requirement is automatic for EM metrics: the stress tensor is trace-free and divergence-free.
- **The boundedness hypothesis is genuinely needed.** L_rank = 0 controls only ∫|φ_h|²|h|². Since |φ_h| = |B|/|h|, it may blow up at Z(h). The cutoff argument needs at least ∫|φ_h||dχ_ε| → 0, which holds for bounded φ_h.
- The theorem as written ("if φ_h is locally bounded …") is correct. Without that hypothesis, the "L_rank = 0 ⇔ EM" equivalence holds only on M∖Z.
- The converse (EM with F⁻ ∝ h has L_rank = 0) holds.
- The conformally-Kähler remarks are consistent: SD harmonic forms are conformally invariant, and |ω_K|_g = √2f² for g = f⁻²g_K.

### (66.3)–(66.5)

- (66.3) Φ_b = F + D follows from 65.1 applied to J₀.
- (66.4) Since ρ₀ = F·ĥ exactly with F = √2c‖h‖, we get P = 2F² and p = F²/4π².
- (66.5)
  - Decomposability of a∧Ja gives |t⁻|² = u²/2.
  - Inserting this into 63.AK gives 0 = 4FD + ∫u(6u+s) + 2‖ρ*″‖² + 4‖W₃‖².
  - With D = δΦ this becomes 4Φ²δ(1−δ) = ….
  - The general Ric″ ≠ 0 version follows from P = 2‖ρ₀‖² + ‖Ric″‖².
- The §3 inequality −s∫u ≥ 4Φ²η(1+2η) holds. It also uses D² ≤ ½∫u² and the hypothesis ĥ ∥ h_b⁻, which the sentence should state.

**All correct.**

### 66.S (s ≥ 0)

- From 4FD ≤ −6∫u² ≤ −12D² we get D(Φ + 2D) ≤ 0, so δ ∈ [−½, 0] when Φ > 0.
- Φ > 0 is automatic once F > 0.
- p ≥ ⟨h_b,ĥ⟩², and δ = 0 ⇔ u ≡ 0.

**Proved.** Two remarks:
- s ≥ 0 never occurs on X#kCP̄². The corollary is a structural consistency check.
- The result should be compared with the Apostolov–Drăghici introduction and Drăghici (1999). If the s ≥ 0 Blair–Ianus case is already known to be Kähler, 66.S is weaker than the literature.

### 66.W (weak near-equality estimate)

- The relations h(δφ_h) = −div R_⊥ and ⟨δφ_h, ξ⟩ = ⟨div R_⊥, h⁻¹ξ⟩ are correct. The second uses skewness of h⁻¹.
- Integration by parts then gives (66.6).
- ‖R_⊥‖² ∝ L_rank.
- The weights |h|⁻² and ∇h blow up at Z, so the estimate is genuinely weak.
- The remark that c is unconstrained, including c = 0, is right. The estimate gives no coercivity.

---

## 3. The §5 interpretation

**Equality class on the constant-s slice.** (E) ∪ (cscK with ρ₀ ∝ h_a⁻) ∪ (strictly AK, Ric J-invariant, ρ₀ ∈ ℝh_a⁻) is correct for L_{ĥ_a} = 0, with the overlap noted in (d).

**"Precisely the open 4D Blair–Ianus problem at negative constant s" is inaccurate.**
- The class is a subclass. It requires constant s < 0, which is not part of the Blair–Ianus question, and the rank-one alignment ρ₀ ∥ h_a⁻.
- On X#kCP̄², b⁻ = b⁻(X) + k is large, so this alignment is a real restriction.
- What holds is one-directional: a Kähler theorem for compact AK J-invariant-Ricci metrics with constant s < 0 empties the strictly-AK part. Nonexistence in the subclass is weaker than Blair–Ianus.
- Accurate phrasing: "contained in the 4D Blair–Ianus class, constant s < 0, with harmonic ρ₀ aligned to a⁻."

**"Parametrize δ_b ∈ (0,1)" is not supported.**
- F > 0 forces δ_b < 1.
- For s < 0, (66.5) allows δ_b < 0: its right side ∫u(|s| − 6u) − … can be negative when u > |s|/6 on average.
- Only for s ≥ 0 is δ_b ≤ 0 forced.
- Nothing shows the L = 0 locus forms a connected family joining (K) and (E). The (K)–(C)–(E) "one family" reading is heuristic, and the cells (C) are not in the L = 0 class.

**§5.1 is correct.** L ≥ cδ for all metrics excludes Einstein metrics, because Einstein metrics have δ = 1 and L = 0. So that inequality contains Einstein nonexistence below LeBrun's bound.

**§5.3 is correct.** (66.5) is one scalar constraint and leaves δ_b free. The remaining information is differential, i.e. the next prolongation of the AAD system.