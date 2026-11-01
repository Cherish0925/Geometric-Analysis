# TTCS Independent Branch Record

```json
{
  "step_id": 87,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step87_csck_calibration_and_nodal_endpoint_rigidity.md",
    "Sessions/S1003A01/workspace/data/step87/csck_calibration.json",
    "Sessions/S1003A01/workspace/scripts/step87_csck_calibration.py",
    "Knowledge/objects/papers/Smoothing-singular-extremal-Kähler-surfaces-and-minimal-Lagrangians--76bcf086d1fb--80cf6934cc4e/object.md",
    "Knowledge/objects/papers/2603.09028-Einstein-deformations-of-Kähler-Einstein-metrics--062c0a015de6--2a0f3c1e029d/object.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the mathematics of the Step-87 note (Sessions/S1003A01/workspace/notes/step87_csck_calibration_and_nodal_endpoint_rigidity.md) on Einstein rigidity near a negative Kähler–Einstein orbifold with one A1 node (generic nodal quintic surface). Research context: closed negative almost-Kähler Einstein (Goldberg) problem and Einstein metrics near KE orbifold endpoints; earlier work reduced the question to a scale-uniform C^1 estimate of Ozuch's normal obstruction Lambda_I. The note claims to replace that derivative estimate by (i) an exact eigenvalue statement (Prop 87.2, from Nagy eq. (17): harmonic primitive (1,1) forms give Hermitian TT eigentensors of the Einstein operator with eigenvalue -2E), (ii) an exact secant along the Biquard–Rollin CSCK family varying the real Kronheimer period zeta_r: Ric-Eg=rho_0(.,J.) with rho_0 harmonic ASD in class 2 pi c1 - E[omega], giving Lambda_I = E zeta_r (1+o(1)) and P=-2(2pi c1-E[omega])^2 (§3, Lemma 87.3), and (iii) a C^0 degree argument (Theorem 87.4) showing the corrected CSCK family fills Ozuch's reduced Einstein-modulo-obstruction family, so every nearby Einstein metric is KE; plus Lemma 87.5 (bubble is orientation-matched EH, no trees) and Cor 87.6 (no strict AKE nearby via the length obstruction). Please check carefully and write a direct scientific memo: (1) correctness of the cohomological identities and normalizations (|Ric0|^2=2|rho0|^2, period int_delta rho_0 = -E zeta_r, theta^2 -> -2, EH L2 form normalization ||theta||^2=2, A=E i.e. c0=1) — compare with the JSON data; (2) whether Prop 87.2 is correct including the claim that no small nonzero TT eigenvalue arises from the degeneration (are o_J, o_K really exact kernel at KE smoothings? is the count 78+2 correct?); (3) the logic of Theorem 87.4: is the EmO correction estimate ||k|| <= C|zeta_r| o(1) justified given Ozuch-type uniform inverses, is uniqueness used correctly, does the degree argument on shells really give surjectivity onto the reduced family (and is the reduced family a graph over parameters so that 'hitting the parameter' identifies the metric), and is anything circular; (4) whether the weighted hypothesis (Hp-w) is plausible with the stated rates, and whether CSCK metrics in classes with zeta_r != 0 on smoothings (and resolutions, Theorem C) really exist uniformly over all directions on S^2 under Biquard–Rollin non-degeneracy for A1; (5) Lemma 87.5's proof (Bishop–Gromov exclusion of trees, Gauss–Bonnet/signature comparison with EH, pi_1 argument); (6) any hidden gap that would invalidate Corollary 87.6, and what is genuinely new versus standard. Separate proved, conditional, and false statements; propose repairs where something fails.

## Output

# Verification memo: Step 87 (CSCK calibration, A1 normal obstruction, Einstein rigidity near a one-node quintic orbifold)

## Summary

- **Algebra and normalizations.** Every algebraic identity and normalization in §§1–3 checks out against the script and JSON, and against independent recomputation.
- **Prop. 87.2.** Correct, and a direct consequence of Nagy's eq. (17).
- **Lemma 87.3.** Correct. A shorter exact identity proves it (§2 below).
- **Lemma 87.5.** Proved from standard inputs. The orientation matching it asserts is in fact a consequence of the topology, not an assumption.
- **Corollary 87.6.** Follows from Theorem 87.4.
- **Theorem 87.4.**
  - The architecture is sound and non-circular: one scalar obstruction (Λ_I) that is exactly proportional to ζ_r on a calibrated comparison family, plus a C⁰ degree argument.
  - As written, Step (4) applies Ozuch's uniqueness to a metric Ξ(p) that was corrected with respect to a *different* gauge base and cokernel. That step needs a precise redefinition, given in §3 below.
  - (Hp-w) and (BR-u) are plausible and can be extracted from Biquard–Rollin §3. (BR-u) needs one recentering not mentioned in the note: uniformity in v.

No statement in the note is false in a way that breaks the chain. A few wording slips are listed in §8.

---

## 1. Identities and normalizations (proved)

**Pointwise Kähler algebra.**
- For a J-invariant symmetric h with associated 2-form, |h|²_tensor = 2|form|²_{i<j}.
- The JSON gives |o_I|² = 4 and |θ|² = 2, so |Ric°|² = 2|ρ₀|² and |θ∘I|² = 2|θ|².
- θ∘J and θ∘K are I-anti-Hermitian and pointwise orthogonal to θ∘I. Hence Λ_J and Λ_K of a J-Hermitian defect vanish at leading order (up to J ≈ I on the core).

**CSCK cohomology.**
- In complex dimension 2, ρ∧ω = (s/4)ω². So ρ₀ = ρ − (s/4)ω is primitive (1,1), hence ASD.
- ρ₀ is closed because s is constant, hence harmonic.
- From s·dvol = 2ρ∧ω one gets s̄ = 8π c₁·[ω]/[ω]². Imposing s ≡ 4E gives [ρ₀] = 2πc₁ − E[ω].
- P = 2‖ρ₀‖² = −2∫ρ₀∧ρ₀ = −2[ρ₀]².
- At ζ_r = 0 one has [ρ₀] = 0, and a harmonic exact form vanishes. So CSCK = KE without invoking any CSCK uniqueness theorem.
- The class 2πc₁/E is Kähler because E < 0 and K is ample.

**Periods.**
- c₁·δ = 0 because K is trivial on the Milnor fibre.
- c₁·θ = 0 because c₁ is (1,1) and pairs to zero with η := δ^{2,0+0,2}.
- θ·δ = θ², so ζ_r = λεθ² and ∫_δ ρ₀ = −Eζ_r exactly. The script encodes exactly this.

**Sign of θ².**
- η is self-dual, so δ² = θ² + η² gives θ² = −2 − η² < −2 whenever ζ_c ≠ 0. Hence P/(E²ζ_r²) → −2/θ² < 1, approaching 1 from below.
- The periods ∫_δ Ω_a of global holomorphic 2-forms are O(|ζ_c|), so |η| = O(|ζ_c|).

**Eguchi–Hanson form.** All four EH entries in the JSON were recomputed by hand and agree:
- The bolt has area πa², so the period is −4πc/a².
- ‖θ‖² = ∫_a^∞ (32c²/r⁸)(r³/8)(8π²) dr = 8π²c²/a⁴, which equals 2 at c = a²/(2π).
- The pointwise norm is 2√2 a²/(πr⁴).
- The relation ‖θ‖² = (period)²/|S·S| = 4/2 is the statement that θ is the L²-harmonic ASD representative of PD(S).

**Calibration.** Write c = Eζ_r/2 and õ_I = θ^cut∘I with ‖õ_I‖ = √2·√2 = 2. Then:
- Λ_I = c‖θ∘I‖²/‖θ∘I‖ = 2c = Eζ_r.
- P = 2c²‖θ‖² = 4c² = Λ_I².

So |A| = |E|, i.e. c₀ = 1 in this normalization. The overall sign depends on the orientation of δ and on the composition convention, which is irrelevant for the argument.

**Comparison with Ozuch.** At a KE point R⁺ = W⁺ + s/12 = diag(s/4, 0, 0) = E ω̂⊗ω̂. This matches Ozuch's form diag(0, 0, Λ) in Theorem 0.2, and λ_k = c⟨R⁺ζ, ζ_(k)⟩ vanishes exactly on ζ_r = 0.
- Ozuch's c > 0 is unspecified, so "c₀ = 1" refers only to the note's L²-unit normalization.

**Decomposition of [ρ₀].** Recomputing gives

y := [ρ₀] − (Eζ_r/2)δ = 2πc₁(1−λ) + Eλε[(η²/2)θ + (1 + η²/2)η] = O(ε²) + O(ε|ζ_c|).

This confirms the size stated in Lemma 87.3.

## 2. Lemma 87.3: a cleaner exact proof

Let α be any closed form in [ρ₀]. Since ρ₀ is harmonic, α − ρ₀ is exact and orthogonal to ρ₀, so ‖α‖² = ‖ρ₀‖² + ‖α−ρ₀‖². Since ρ₀ is ASD, ‖ρ₀‖² = −∫α∧α = ‖α⁻‖² − ‖α⁺‖². Together these give

**‖α − ρ₀‖² = 2‖α⁺‖²** (exact).

Take α = cθ^cut + (harmonic representative of y). Then ‖α⁺‖ ≤ |c|·O((a/R)² + ‖g − g_EH,scaled‖_{C⁰, neck}) + O(‖y‖).

- All relative errors are uniform in the ratio ζ_r/|ζ|.
- This uniformity is the real advance over Ozuch's Prop. 2.19. There, λ+μ is controlled only by the absolute error O(|ζ|^{5/2}), which is useless near the sheet ζ_r ≪ |ζ|^{3/2}.

Consequence (proved, given BR's C⁰ closeness on the neck): Λ_I(g^CSCK) = Eζ_r(1+o(1)) in the L² pairing. This needs no differentiation in ζ: Ric° vanishes at ζ_r = 0 and is bounded by (norm of the harmonic-representative operator) × |[ρ₀]|.

## 3. Prop. 87.2 and the spectral count

**Correctness.**
- Nagy (17) conjugates Δ_E on Sym^{2,+} to Δ_d − 2E on Ω^{1,1}. This covers the whole Hermitian sector, trace parts included.
- Hence Δ_E ≥ −2E there, with equality exactly on harmonic (1,1) forms.
- Removing Rω (the trace direction) leaves the primitive harmonic forms, i.e. H⁻.
- The multiplicity in the Hermitian TT sector is therefore **exactly** b⁻ = 44, not "at least". "At least" applies only to the full TT spectrum.
- Signature check: b⁺ = 2p_g + 1 = 9 and b⁻ = 53 − 9 = 44.
- In Ozuch's normalization P = ½Δ_E, the eigenvalue is −E > 0.

**Count 78 + 2 = 80.**
- h²(Θ_M) = h⁰(Ω¹_M(1)) = 0, using h⁰(Ω_{P³}(1)) = 0, H¹(O_X(−4)) = 0 and Bott vanishing. So h¹(Θ_M) = 10χ(O) − 2c₁² = 40, and Koiso's E(g_t) is the 80-dimensional KS space, which is integrable.
- On the orbifold, the sequence 0 → H¹(T_V) → Ext¹(Ω_V, O) (dim 40) → H⁰(T¹) = ℂ → … gives h¹(T_V) = 39. Hence the 78 in Lemma 87.1.

**Are o_J and o_K exact kernel?** Not individually. The exact 80-dimensional kernel on g_t converges, in L² and with relative o(1) error, to span(o_J, o_K) ⊕ (78 exterior modes).
- The neck pair is the KS class of ∂_c with c = ζ_c², rescaled by 1/(2ζ_c).
- The sentence "every approximate kernel element is either an exact kernel element or an exact eigenmode" should read "is L²-close to".
- §2 contains the typo "the remaining 3+78"; it should be 2+78.

**Consistency check.** b⁻(V) = 52 − 9 = 43. The 44 Hermitian (−E)-modes on g_t are therefore 43 orbifold modes plus one neck mode θ_t. This matches spectral convergence.

**Sign item to check (does not affect 87.4).** The proof of Ozuch's Thm 0.2, point (2), quotes Biq17: ⟨P o_k, o_k⟩ = (a_k + o(1))‖o_k‖, where a_k are the R^± eigenvalues.
- With R⁺ = diag(E, 0, 0), this would give a Rayleigh quotient of size about E < 0 on o_I.
- Prop. 87.2 gives the exact value −E > 0.
- Magnitudes agree; the sign must come from Ozuch/Biquard's R̊ or Rm convention. Record the convention before quoting either result.
- Only A ≠ 0 enters 87.4.

## 4. Theorem 87.4: logic

**What works.**
- *Degree argument.* Boundary checks on the shell: if |v − v*| = 2η, the homotopy stays at distance ≥ η; if |ζ| = |ζ*|/2, then |H_s ζ| ≤ (1+η)|ζ*|/2 < |ζ*|; if |ζ| = 2|ζ*|, then |H_s ζ| ≥ 2(1−η)|ζ*| > |ζ*| for η < 1/2.
  - R³∖0/± ≅ ℝ⁺ × ℝP² is non-orientable. Run the argument on the ±-equivariant lift to ℝ³, or use degree mod 2.
- *Accuracy needed.* Only |ζ|-relative C⁰ accuracy is required; no ζ_r accuracy is needed, since Λ_I supplies ζ_r. This is the right design.
- *Correction estimate.* The structure of ‖k‖ ≤ C‖π^⊥Φ‖ is exactly the template of the supplied Ozuch Lemma 3.23. The pairing ⟨Pk, ô_I⟩ is bounded as in Ozuch Lemma 2.18, by C|ζ|·o(|ζ_r|). Scaling check on the quadratic term: ⟨Q(k), ô_I⟩ = O(‖k‖²) with ‖k‖ = o(|Eζ_r|) dimensionless, so it is ≪ |Eζ_r|.
- *Non-circularity.* The Λ_I calibration uses only cohomology and harmonic minimization.

**Gap (needs repair, not false).** Ξ(p) = g^CSCK_p + k_p is Einstein-modulo an 81-dimensional space attached to its *own* base: its own Bianchi gauge and its own Õ. Ozuch's uniqueness at q = π(Ξ(p)) requires instead:
- B_{g^D_q}(Ξ) = 0,
- Ξ − g^D_q ⊥ Õ(g^D_q), and
- Φ_{g^D_q}(Ξ) ∈ Õ(g^D_q).

After a gauge diffeomorphism φ, Φ = φ*Ric°(Ξ) lies in φ*Õ_CSCK, not in Õ(g^D_q). Repair:

1. Define π(p) by jointly solving the gauge condition B_{g^D_q}(φ* g^CSCK_p) = 0 and the orthogonality condition φ* g^CSCK_p − g^D_q ⊥ Õ(g^D_q). Use the implicit function theorem in q. Its Jacobian is the Gram matrix of the explicit family ∂_q g^D, which is uniformly invertible. Continuity of π then follows; this is the only derivative information used, and it concerns explicit naive objects.
2. Let g_q be Ozuch's EmO metric and set k' := g_q − φ* g^CSCK_p. It is ⊥ Õ(g^D_q) by construction. Projecting the EmO equation onto Õ^⊥ gives ‖k'‖ ≤ C‖π^⊥ φ*Ric°‖ = o(|ζ_r|) by (Hp-w). Hence Λ_I(q) = Eζ_r(p)(1+o(1)).
3. The degree argument makes π surjective. If g_q is Einstein, then ζ_r(p) = 0, so g^CSCK_p is KE. It then satisfies Ozuch's conditions at q, and uniqueness gives g_q = KE.

**Alternative repair.** Perform the reduction with the CSCK family itself as the base (Õ_CSCK = span ∂_p g^CSCK). Its uniform inverse follows from Ozuch's by perturbation using (M). This route also needs a degree argument, to solve the orthogonality condition for p.

**Graph structure.** Ozuch's EmO family is a graph q ↦ g_q, so "hitting q" identifies the metric once Step 2 holds. Injectivity of π is not needed.

**Remaining conditional inputs.**
- *(O1)* must be read in Ozu19a,b.
- *Uniqueness-ball compatibility.* The CSCK metric must lie in Ozuch's C^{2,α}_{β,*} uniqueness ball, including the constant-tensor parts H_k. BR give pointwise relative closeness O(ε^{(1−β)(δ+2)}); the weighted derivative version must be written out.

## 5. (Hp-w) and (BR-u)

**(Hp-w)** is plausible and can be derived from BR §3.5–3.7.
- *Scaling.* BR Prop. 29 gives ‖γ‖_{C_δ} ≍ ‖Ξ‖_{δ,t} = ε^{−2−δ}‖Ξ_A‖ + ‖Ξ_B‖ for harmonic forms. With the class [ρ₀] = O(ζ_r), this yields the linear bound.
- *Concentration.* BR Cor. 23 gives ‖γ − P_tγ‖ = O(ε^{β₁})‖P_tγ‖, with P_tγ in the cut-off EH ⊕ orbifold approximate kernel. This gives relative o(1) in BR's form norms.
- *Translation to Ozuch's norms.* Use Ric° = ρ₀(·, J·) and |J − J₀| = O(ε⁴r⁻⁴) (BR Lemma 15) to pass to symmetric tensors in Ozuch's r_D^{-2} C^α_β norm.
- *Exterior tail.* In the exterior, Ric° ≈ c·(harmonic ASD form with an a²r⁻⁴ singularity)∘J. By Nagy (17) this is a Δ_E-eigentensor with eigenvalue −2E. Ozuch's extension ō⁴_I satisfies instead P ō ≈ 0 modulo O(g_o).
  - Their leading singular terms agree; the difference is lower order, of size c·a²·O(r⁻²).
  - In the weighted norm the difference is relatively O(a²) at r ~ 1 and small at r ~ b.
  - This, not the note's "a²b⁻² against b⁻⁴" sketch, is the term to estimate.
- The ν_l components vanish at leading order because Hermitian and KS anti-Hermitian modes are pointwise orthogonal.

**(BR-u).** For A1 the wall is {0}, so Definition 2 holds for every ζ̂ ∈ S².
- *Uniformity over S².* Every tangent graviton is EH rotated by SO(3), which acts isometrically (BR §2.2(4)). The ALE constants are therefore uniform over S².
- *Exterior complex structure.* The deviation is |c| = |ζ_c|², which is ≪ ε² ~ |ζ|.
- *The gap: uniformity in v.* BR Lemma 15 needs |J_t − J₀| = O(ε²) on the compact part, which fails if |v| ≫ |ζ|. Repair: recentre at the orbifold KE metric g_v of X_v. Parametrize the 40-dimensional smooth deformation space as (v, c), with c a submersion; this is possible because T¹_emb → T¹_p is onto. Then use the smooth dependence of g_v.
- *Resolution directions (Theorem C).* For ζ_c = 0, Kählerness requires ζ_r > 0 on the holomorphic (−2)-curve. The opposite sign is the Weyl image (ζ ↦ −ζ), so all of ℝ³/± is covered.
- *Continuity across ζ_c = 0.* This comes from Brieskorn's simultaneous resolution over the Weyl cover. It has to be built into the uniform construction.

## 6. Lemma 87.5 (proved)

**Volume and tree structure.**
- Volume continuity (Colding) and Anderson / Bando–Kasue–Nakajima give a noncollapsed orbifold limit.
- Bubbles at smooth points have Euclidean volume ratio 1 at infinity, so they are flat.
- For an intermediate bubble, Bishop–Gromov monotonicity on the orbifold gives 1/|Γ'| ≥ 1/2, with equality only for the flat cone. So there are no orbifold points and no trees. The same argument excludes secondary bubbles at smooth points of the root bubble.

**Topology of the bubble N.**
- Euler characteristic additivity gives χ(N) = 55 − 54 + 1 = 2.
- RP³ is a rational homology sphere, so Mayer–Vietoris gives b₁(N) = 0 and b₂(N) = 53 − 52 = 1.
- Novikov additivity with τ(V) = 9 − 43 = −34 gives τ(N) = −1 in M's orientation.

**Orientation matching is automatic.** RP³ has an orientation-reversing isometry (quaternion conjugation commutes with ±1), so η(RP³) = 0. The APS boundary terms then vanish in either orientation, and:
- 2 = (1/8π²)∫(|W⁺|² + |W⁻|²) + 1/2, and
- −1 = (1/12π²)∫(|W⁺|² − |W⁻|²)

together force ∫|W⁺|² = 0. Matching is therefore a consequence of τ(N) = −1, i.e. of δ² = −2.

**Fundamental group and identification.**
- R⁺ = 0 makes Λ⁺ flat.
- Euclidean volume growth with Ric ≥ 0 forces π₁ finite.
- On the universal cover, |π₁|/2 ≤ 1, with equality only for flat ℝ⁴ → ℝ⁴/±1, which is excluded. So π₁ = 1.
- N is therefore hyperkähler, and Kronheimer's classification identifies it as EH.

## 7. Corollary 87.6

Given 87.4, the argument is correct:
- ω is self-dual harmonic, so it lies in ℝω_{J'} ⊕ Re H^{2,0}_{J'}, a pointwise-orthogonal splitting.
- |ω| constant forces |Re β| = |β|/√2 constant.
- β ≠ 0 would then trivialize K, contradicting c₁² = 5 and K ample.
- So ω = ±ω_{J'} and J = ±J' is integrable.

The only gaps are those inherited from 87.4: (O1), (BR-u), (M), (Hp-w), and the π-definition repair in §4.

Two quantities in §5 cannot be checked from the supplied material: D_W and the identity 8π²k − P = 4D_W − (S − 32π²A)/4. They are not defined in any supplied file.

## 8. What is new vs standard; transfer claims; status

**Standard.**
- P = −2[ρ₀]², Prop. 87.2 (immediate from Nagy (17)), and the quintic numerology.
- Lemma 87.5, which combines Bishop–Gromov, APS and Kronheimer.
- Lemma 87.1, a direct orbifold adaptation of Koiso/Nagy. Its analytic-continuation step is valid: the Kuranishi map vanishes on an open set, hence on the connected ball.

**New.**
- The use of the CSCK family as an exact secant whose Einstein defect is the harmonic ASD representative of a class proportional to ζ_r. This gives a relatively uniform calibration of the normal obstruction without any C¹ input.
- The resulting one-equation rigidity: once completed, Einstein metrics GH-near a generic one-node negative KE orbifold are KE.
- Neither Ozuch's Thm 0.2 nor his Prop 0.4 gives this, since g_V already satisfies obstruction (4).

**Transfer claims (§6 of the note).**
- *Multi-node:* the vanishing classes δ_x must be linearly independent in H₂(M; ℝ) so that the (ζ_r)_x can be prescribed independently. State this explicitly.
- *E > 0 (del Pezzo):* Δ_d − 2E is not ≥ 0, so Hermitian infinitesimal Einstein deformations of the orbifold are not excluded. The analogue of Lemma 87.1, and with it Ozuch's integrability hypothesis, then needs a separate argument; §3 of the note is unaffected.

**Status.**

| Status | Items |
|---|---|
| Proved | §1 identities; Lemma 87.3 in L², hence Λ_I(g^CSCK) = Eζ_r(1+o(1)); Prop. 87.2 (Hermitian multiplicity exactly 44); 80-dimensional KS count; Lemma 87.5; Cor. 87.6 ⇐ 87.4 |
| Conditional | Theorem 87.4, on (O1), (BR-u) with v-recentering, (M) in C^{2,α}_{β,*}, and (Hp-w) via BR Prop 29 / Cor 23 plus the exterior-tail comparison |
| Needs reformulation | Step (4) of 87.4: define π by joint gauge plus orthogonality at the base g^D_q, then compare via k' (§4 repair) |
| Wording slips | "3+78" → "2+78"; "at least 44" → exactly 44 in the Hermitian TT sector; "is an exact kernel element" → "is L²-close to the exact kernel" |
| Convention to fix | Sign of the limiting EH Rayleigh quotient (Biq17 a_k) vs the exact −E of Prop. 87.2 |