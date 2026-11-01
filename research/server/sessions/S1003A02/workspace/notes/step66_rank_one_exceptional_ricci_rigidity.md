# Step 66 — Rank-one exceptional Ricci rigidity: the equality class of the flux ledger is the J-invariant-Ricci almost-Kähler class

Agent2, Execute. Inputs: the Step-65 ledger `step65_cell_exceptional_flux_ledger.md` §1 (identities 65.1–65.3) and §5′; Spirit #81, which asked us to split L = 0 into the Einstein case μ = 0 and the aligned case μ ≠ 0. Symbolic check: `workspace/scripts/step66_rank1_bianchi_check.py` → `workspace/data/step66_rank1_bianchi_check.json`. Sources: Apostolov–Armstrong–Drăghici, *Local models and integrability of certain almost Kähler 4-manifolds* (Knowledge object `Local-models-and-integrability…`, eq. (26): dρ = *(JδRic''), so Ric'' = 0 ⇒ dρ = 0, after Drăghici 1995), and Apostolov–Armstrong–Drăghici, *Local rigidity of certain classes of almost Kähler 4-manifolds* (Knowledge object `Local-rigidity-of-certain-classes…`, lines 33–66, 151–154, 251–256: there are local strictly AK examples with J-invariant Ricci tensor; compact AK₂ = Kähler; negative Goldberg is open).

Conventions. Forms carry the form norm (|e¹²+e³⁴|² = 2). A 2-form acts as a skew endomorphism. For ψ ASD, ψ∘ψ = −½|ψ|² Id, so ψ is invertible wherever ψ ≠ 0. For φ SD and ψ ASD, φ∘ψ = ψ∘φ is symmetric and trace-free, and (φ,ψ) ↦ φ∘ψ identifies Λ⁺⊗Λ⁻ with Sym₀T*M. That is the block B_g of 65.1. Throughout, h is a nonzero harmonic ASD form, typically the exceptional representative ĥ_a of Step 65, with zero set Z(h).

## 0. Constant scalar curvature costs nothing (Prop. 66.Y)

By Gauss–Bonnet, P(g) = 2∫|W|² + (1/12)∫s² − 16π²χ, and ∫|W|²dμ is conformally invariant. If Y[g] < 0, then ∫s_g²dμ_g ≥ Y[g]², with equality exactly at the constant-scalar Yamabe representative ĝ (LeBrun's standard estimate). Hence

  P(g) − P(ĝ) = (1/12)(∫s_g² − Y[g]²) ≥ 0,

with equality iff s_g is constant.

For M = X#kCP̄² with X minimal of general type, every conformal class has Y < 0, because b⁺ > 1 and SW ≠ 0 (LeBrun). Therefore α(M) is the infimum over constant-scalar metrics, and every near-minimizing sequence can be replaced by its Yamabe representatives with no loss. **For the gap problem, the ledger only needs to be analyzed on metrics with constant s < 0.** (This is the same identity P(g) − P(ĝ) = 3∫(Δu/u)² + 24∫|∇u|² already used in Theorem C.)

## 1. The divergence identity (Lemma 66.D)

**Lemma 66.D.** Let φ be an SD 2-form and ψ an ASD 2-form. Then

  div(φ∘ψ) = ψ(δφ) + (a term linear in dψ),

with δφ = −∇^aφ_{a·}. In particular, **if ψ is closed** (hence harmonic, since an ASD closed form is coclosed),

  div(φ∘ψ) = ψ(δφ).   (66.1)

*Proof.* In spinor form, φ∘ψ ↔ φ_{AB}ψ_{A'B'}. The divergence is (∇^{AA'}φ_{AB})ψ_{A'B'} + φ_{AB}∇^{AA'}ψ_{A'B'}. The second term is the Maxwell operator applied to ψ, which vanishes iff dψ = 0. The first term is the Dirac part of ∇φ, i.e. ±δφ, acting through ψ.

*Check.* The constant is exactly 1 in the stated conventions. This was verified symbolically in flat R⁴, which suffices because only first derivatives enter, using a generic quadratic SD φ and the general closed linear ASD ψ. The script also confirms the control case: with a nonclosed ψ the identity fails in all four components. Both T = φ∘ψ symmetric and tr T = 0 are confirmed. (`step66_rank1_bianchi_check.json`)

Since δφ = −*dφ for SD φ, on {ψ ≠ 0} we get: div(φ∘ψ) = 0 ⇔ dφ = 0.

## 2. The equality case of the ledger

Recall 65.2–65.3. We have 𝔉_h = √2∫|B^*h|. Pointwise |B^*h| ≤ |B||h| (rank-one Cauchy–Schwarz), and globally (∫|B||h|)² ≤ ∫|B|²∫|h|² (integral Cauchy–Schwarz). The misalignment L is the sum of the two gaps. Hence **L_h(g) = 0 iff there is a constant c ≥ 0 and a unit SD field Ω̂₀ on M∖Z(h) with**

  B_g = c·Ω̂₀⊗h,  i.e.  Ric° = c'·Ω₀∘h  (Ω₀ = √2Ω̂₀, |Ω₀|² = 2, c' a fixed multiple of c).   (66.2)

This has two cases.
- **Case μ = 0 (c = 0).** Then Ric° = 0: g is Einstein, δ = 1, p = 0. As Spirit #81 notes, this is Einstein existence (Problem 1) and nothing more is said here.
- **Case μ ≠ 0 (c > 0).** This is the aligned case treated below.

**Theorem 66.R (rank-one exceptional Ricci rigidity).** Let (M,g) be closed and oriented, let h ≢ 0 be harmonic ASD, and suppose L_h(g) = 0 with c > 0.

(a) *Lee form.* On M∖Z(h), the contracted Bianchi identity div Ric° = ds/4 and (66.1) give

  δΩ₀ = h⁻¹(ds)/(4c') = −h(ds)/(2c'|h|²).

So the Lee form of the almost-Hermitian structure (g, J₀) is determined by ds and h.

(b) *Constant scalar curvature ⇒ almost-Kähler.* If s is constant, then Ω₀ is closed on M∖Z(h). Moreover Ω₀ extends to a smooth symplectic form on M that is g-compatible, so (g, Ω₀, J₀) is **almost-Kähler**.
- Extension: the nodal set of a harmonic form has Hausdorff dimension ≤ 2 (Bär), so H³(Z(h)) = 0. A bounded form that is closed and coclosed off a compact set with H³ = 0 is closed and coclosed distributionally (Lipschitz cutoffs with ∫|dχ| → 0). Ω₀ is then a weakly harmonic SD form with |Ω₀|² = 2 a.e. Elliptic regularity makes it smooth, so |Ω₀|² ≡ 2.

(c) *The structure.* For this AK structure:
- the Ricci tensor is **J₀-invariant** (Ric'' = 0);
- the primitive Ricci form ρ₀ = B(Ω₀) is a constant multiple of h, hence harmonic.

(d) *Converse.* Suppose (g,J₀) is AK with J₀-invariant Ricci tensor and constant scalar curvature. Then by AAD (26) dρ = *(JδRic'') = 0. Since ρ = (s/4)Ω₀ + ρ₀ with s constant, ρ₀ is closed, hence harmonic ASD, and B_g = ½Ω₀⊗ρ₀. Then L_h(g) = 0 for h ∝ ρ₀. Equivalently, L_{ĥ_a}(g) = 0 iff the class [ρ₀] lies on the line ℝ·a⁻.

**Combined with 66.Y:** *on the constant-scalar slice relevant to α(X#kCP̄²), the ledger's equality class is exactly*
- (E) the Einstein metrics, together with
- (AK_Ric) the constant-scalar almost-Kähler metrics with J-invariant Ricci tensor whose primitive Ricci class is proportional to the exceptional class a⁻.

The second class contains the cscK Kähler metrics with c₁(J)⁻ ∥ a⁻ (which have δ = 0 and p = |a⁻|² = k + Π). Its strictly AK members are exactly the objects of the AK integrability problem for J-invariant Ricci tensor (Drăghici's class). Locally they exist (AAD *Local rigidity*, Prop. 1); compact existence with s < 0 is, to our knowledge, open. That is pending the literature return s66_t4_tool1.

Note on scope: Z(h) ≠ ∅ is allowed. The extension argument shows that in the equality case the alignment field never develops a Hopf-type singularity of the kind Step 64 found for normalized SW spinors. Equality forces regularity.

## 2bis. The two parts of L, and the Einstein–Maxwell layer (Theorem 66.EM)

The misalignment splits exactly into two nonnegative parts (all integrals over M∖Z(h); constants as in 65.3):

  ∫|B|² − (∫|B^*h|)²/‖h‖² = ∫(|B|² − |B^*h|²/|h|²) + [∫|B^*h|²/|h|² − (∫|B^*h|)²/∫|h|²].

So L = L_rank + L_amp, where:
- L_rank vanishes iff B is pointwise of the form φ⊗h for an SD form φ = φ_h;
- L_amp vanishes iff |φ_h| is constant (by Cauchy–Schwarz with weight |h|²).

**Theorem 66.EM.** Let s be constant, h harmonic ASD, and L_rank = 0, so that Ric° = φ_h∘h. Then on M∖Z(h), (66.1) gives h(δφ_h) = div Ric° = 0, so φ_h is closed and coclosed. If φ_h is locally bounded near Z(h), it extends to a harmonic SD form on M. In that case, with F := φ_h + h (a closed and coclosed 2-form),

  Ric° = φ_h∘h = ½(F∘F)₀,  s = const,

which are exactly the **Riemannian Einstein–Maxwell equations** with Maxwell field F, whose ASD part is the prescribed harmonic form h. Conversely, every Einstein–Maxwell metric with F⁻ ∝ h has L_rank = 0.

Hence on the Yamabe slice the ledger is organised by Einstein–Maxwell theory:
- **L_rank = 0:** Einstein–Maxwell with F⁻ ∝ ĥ_a.
- **L = 0:** the subclass with |F⁺| constant. Then F⁺/|F⁺| is a g-compatible symplectic form, which is exactly 66.R.
- **F⁺ = 0:** Einstein.
- **Kähler cscK:** F⁺ = ω and F⁻ ∝ ρ₀, the classical observation that cscK metrics are Einstein–Maxwell. Conformally Kähler EM metrics g = f⁻²g_K have F⁺ = ω_K with |F⁺|_g = √2f², so their L_amp is the variance of f² weighted by |h|².

On the EM layer the exact ledger reads p = (1−δ)²/‖h‖² + L_amp. *Correction of a tempting misreading:* the primitive Ricci form ρ₀ := Ric°(J·,·) of a conformally Kähler EM metric is |F⁺|-weighted, not harmonic. Only in the |F⁺| = const case is ρ₀ harmonic. This removes an apparent conflict with Apostolov–Maschler \cite{apostolov2019conformally}.

**Literature position of the L = 0 strictly-AK members.** AK metrics with J-invariant Ricci tensor are the critical points of the Hilbert functional ∫s on metrics compatible with a fixed symplectic form (Blair–Ianus). Blair and Ianus asked whether compactness forces integrability. Apostolov–Drăghici \cite{unknownarxivk} (Knowledge object `Almost-Kahler-4-manifolds-with-J-invariant-Ricci-tensor-and…`, Introduction) record:
- the question is stronger than the Goldberg conjecture;
- it fails in real dimension ≥ 6 (Davidov–Muškarov);
- *no compact strictly AK 4-manifold with J-invariant Ricci tensor is known*;
- the ASD case is Kähler.

Kim \cite{kimalmostd} (Thm 5–6) also uses dρ = 0 and ρ₀ harmonic for constant s, and proves integrability only under nonnegative curvature hypotheses. **Thus the strictly-AK part of the equality class is precisely the open four-dimensional Blair–Ianus problem with constant negative scalar curvature.**

## 3. The ledger on the equality class (exact)

Let (g,J₀) ∈ (AK_Ric), and write:
- b = c₁(J₀) (a sign class: ±K_X ± ΣE_i for minimal general-type X by Taubes/Li–Liu);
- ĥ = h/‖h‖;
- F = ⟨ρ₀,ĥ⟩, so that ρ₀ = Fĥ;
- D = ⟨t⁻,ĥ⟩, the harmonic twist flux of J₀, with t⁻ = −(a∧J₀a)⁻;
- Φ_b = 2π⟨h_b,ĥ⟩, with h_b harmonic.

**(66.3) Frame flux (65.1 for J₀):** Φ_b = F + D.

**(66.4) Defect:** P = 2‖ρ₀‖² = 2F², i.e.
  p = F²/(4π²) = ⟨h_b,ĥ⟩²(1−δ_b)²,  δ_b := D/Φ_b.
In particular, if ĥ ∥ h_b⁻, then p = |b⁻|²(1−δ_b)² exactly. The Hodge inequality of 65.3 is saturated.

**(66.5) Torsion-financing identity.** Insert ‖γ⁻‖² = ‖ρ₀ + t⁻‖² into Proposition 63.AK (valid for every AK metric, and here P = 2‖ρ₀‖²), and use 2‖t⁻‖² = ∫u²:

  4FD + ∫u(6u + s) + 2‖ρ*''‖² + 4‖W₃⁺‖² = 0,   equivalently   4Φ_b²·δ_b(1−δ_b) = ∫u(−s − 6u) − 2‖ρ*''‖² − 4‖W₃⁺‖².

For a general AK metric (Ric'' ≠ 0) the same algebra gives
  ‖Ric''‖² = 4⟨ρ₀,t⁻⟩ + ∫u(6u+s) + 2‖ρ*''‖² + 4‖W₃⁺‖²,
of which (66.5) is the Ric'' = 0 case. At F = 0 it is A01's AK-Einstein balance ∫u(|s|−6u) = 2‖ρ*''‖² + 4‖W₃‖².

**Corollary 66.S (nonnegative scalar curvature: rigidity and tariff).** If s ≥ 0 is constant and (g,J₀) ∈ (AK_Ric), with Φ_b > 0:
- 4FD ≤ −6∫u² ≤ −12D², since D² ≤ ‖t⁻‖² = ½∫u²;
- hence D(Φ_b + 2D) ≤ 0, i.e. δ_b ∈ [−½, 0];
- consequently p = (Φ_b − D)²/(4π²) ≥ ⟨h_b,ĥ⟩², which is the **Kähler tariff p ≥ |b⁻|²** when ĥ ∥ h_b⁻;
- δ_b = 0 iff u ≡ 0, i.e. iff g is Kähler (cscK).

So for s ≥ 0 the aligned equality class contains no sub-tariff metric. Strictly AK members, if any, are over-fluxed (δ_b < 0) and cost more than Kähler.

**Reading for s < 0, the regime of X#kCP̄².** (66.5) says the negative linear torsion term −s∫u must finance three things at once:
- the W₂ and W₃ energies,
- 6∫u²,
- the aligned flux product 4Φ_b²δ_b(1−δ_b).

The last vanishes at both ends of the class:
- δ_b = 0: the Kähler end, with p = |b⁻|²;
- δ_b → 1: there F → 0, ρ₀ → 0, and (66.5) becomes the AK-Einstein balance.

Thus **along the equality class, the sub-tariff direction δ_b ↑ 1 runs straight into the negative-scalar Goldberg regime.** A metric in (AK_Ric) with p ≤ (1−η)²|b⁻|² is a strictly AK metric with J-invariant Ricci tensor and δ_b ≥ η. Its torsion satisfies −s∫u ≥ 4Φ_b²η(1−η) + 12Φ_b²η².

## 4. Near-equality: what the Bianchi identity gives quantitatively (Prop. 66.W)

Let s be constant (WLOG by 66.Y) and h harmonic ASD. Pointwise off Z(h), decompose

  Ric° = φ_h∘h + R_⊥,

where φ_h ∈ Λ⁺ is the Ricci-aligned SD form (φ_h ∝ B^*h/|h|²) and R_⊥ ∈ Λ⁺⊗h^⊥ is the rank-transverse part. By (66.1) and div Ric° = 0,

  h(δφ_h) = −div R_⊥,

so for every compactly supported 1-form ξ on M∖Z(h),

  |⟨δφ_h, ξ⟩| ≤ ‖R_⊥‖₂ · ‖∇(h⁻¹ξ)‖₂,  h⁻¹ξ = −2h(ξ)/|h|².   (66.6)

The second (amplitude) part of L measures ∫(|φ_h| − c)²|h|².

Hence small misalignment L forces two things:
- φ_h is weakly closed, in a negative norm weighted by |h|⁻¹ and ∇h;
- φ_h has nearly constant length in the h-weighted sense.

Together these say that **a near-equality metric is weakly close to the (AK_Ric) structure**. This is the quantitative form of 66.R.

Nothing in (66.6) bounds the size c of φ_h. Every c, including c = 0 (Einstein), is consistent. So **near-equality structure gives no coercivity L ≥ cδ**. Coercivity would have to come from a theorem that excludes (or quantitatively prices) strictly AK J-invariant-Ricci metrics with δ_b near 1, together with Einstein metrics.

## 5. What this does to the open-range problem

1. **Equivalence with Einstein existence at the top end.** Any inequality L ≥ cδ valid for all metrics on X#kCP̄² excludes Einstein metrics there (δ = 1, L = 0). So does any positive lower bound on α. A gap theorem in 0 < k < A/3 contains the nonexistence of Einstein metrics below LeBrun's bound, which is open. The gap problem (Problem 2) and Einstein existence (Problem 1) meet at the same inequality. *This is a statement of logical strength, not of difficulty transfer:* α > 0 is strictly stronger than nonexistence.

2. **The three regimes of the interpolation, now as one family.** On the constant-scalar slice, the ledger 65.3 interpolates between:
   - (K) the Kähler end: δ = 0, p = |a⁻|², L = 0, cscK;
   - (C) the perturbative cell end: δ ≲ 10⁻², L/δ ≈ 0.8–1.0, the certified cells;
   - (E) the Einstein end: δ = 1, p = 0, L = 0.

   Theorem 66.R shows that the exact L = 0 locus joining (K) and (E) consists of the cscK metrics, the Einstein metrics, and the strictly AK metrics with J-invariant Ricci tensor and [ρ₀] ∥ a⁻. The latter parametrize δ_b ∈ (0,1) and obey (66.5).

   So the "sub-tariff direction of least resistance" (L = 0, δ increasing) is exactly the four-dimensional Blair–Ianus problem at negative constant scalar curvature, sitting inside the Einstein–Maxwell layer L_rank = 0 (66.EM). The latter is the natural ambient family. It joins cscK (F⁺ = ω) to Einstein (F⁺ = 0) through EM metrics with F⁻ ∝ ĥ_a, and on it the only loss is L_amp. Any theorem of the form "compact AK with J-invariant Ricci tensor and constant s < 0 on X#kCP̄² is Kähler" would collapse the aligned equality class to the cscK end and Einstein metrics. It would leave the gap problem as: (i) Einstein existence, plus (ii) coercivity of misalignment away from the cscK end.

3. **The obstruction must be differential, not algebraic.** (66.5) is a single integral constraint. Nothing in it excludes δ_b ∈ (0,1) for s < 0; it only requires torsion with −s∫u ≥ 4Φ_b²δ_b(1+2δ_b). In unit-volume terms this is the root-scale torsion u_rms ≳ √(k/A) of Step 64. The algebraic information is exhausted. What remains is the compact AK integrability question, i.e. the next prolongation of the AAD system (A01's Sym₀∇²Ω, #838).

## 6. Status

- **66.Y:** proved. The Gauss–Bonnet and Yamabe ingredients are standard. LeBrun's estimate ∫s² ≥ Y² for Y < 0 should be cited from Knowledge.
- **66.D:** proved, with the symbolic check in the JSON.
- **66.R (a)–(d):** proved modulo two inputs: Bär's nodal-set dimension bound (to cite) and AAD (26) (read).
- **(66.3)–(66.5) and 66.S:** proved, given 63.AK (TTCS-verified in Step 63) and 65.1.
- **66.W:** proved as stated. It is a weak estimate, not a coercivity theorem.
- **§5:** structural consequences. The compact-existence status of (AK_Ric) with s < 0 awaits the literature return.
- **Not addressed:** the non-constant-s equality case beyond (a). This is irrelevant for α by 66.Y.


## 7. Verification (TTCS step66_ttcs01) — BINDING corrections

Source: `trace/ttcs/results/step66_ttcs01_verifier1_integration.md`. Confirmed as mathematically sound: the block identity (R̂Ω)⁻ = BΩ (for orientation-compatible J), the constant in 65.2, Lemma 66.D (coefficient +1; tensorial proof, the script is a corroborating specialization), the rigidity mechanism of 66.R, (66.3)–(66.5), Corollary 66.S, and the weak estimate 66.W. The corrections below supersede the text above.

1. **Normalization of the ledger (65.3).** Use the unit form ĥ = h/‖h‖₂ and define:
   - q = (h_a⁻, ĥ);
   - δ = 1 − 𝔉_ĥ/(2πq);
   - L = (P/2 − 𝔉_ĥ²)/(4π²).

   Then p = q²(1−δ)² + L exactly, and every class-a J has (t_J⁻, ĥ) ≥ 2πqδ. The Step-65 sentence "𝔉 < 2π√p⟨a,ĥ⟩" is wrong; the valid statements are 𝔉_ĥ ≤ 2π√p, and p < q² ⇒ δ > 0. With period normalization q_h = 1, the saving relation is
   1 − p = 2δ − δ² − L − (1−δ)²(H⁻¹ − 1),
   so for H ≤ 1 we get 1 − p ≤ 2δ − δ² − L. The Step-65 extra term had the wrong sign.

2. **Step-65 table.** The δ column is the signed J₁ twist deficit 1 − ∫⟨Ω₁,B^*h⟩/2π, not the metric deficit 1 − 𝔉/2π. At the certified cell:
   - metric deficit δ_m = 0.00541 and Hodge term (1−δ_m)²/H = 0.99023, so L_m = 0.00543;
   - the signed values printed in the table were δ = 0.00549, Hodge = 0.99008, L = 0.00558.

   The two agree to about 1.5%. The qualitative readings of §4 (δ second order, L/δ ≈ 0.8–1, saving ≲ δ) are unchanged. The x0 = .05 and .10 records are confirmed unreliable by A01 (#840); only step33 x0 = .03, X = 128 is authoritative.

3. **Amplitude part.** The amplitude quantity is |β_h| = |B^*h|/|h|², not |B^*h|/|h|. The exact split is
   L = (2π²)⁻¹[‖B_⊥‖² + ∫(|β_h| − c)²|h|²].

4. **66.Y.**
   - General type does not give b⁺ > 1, since b⁺ = 1 + 2p_g. The reduction to constant s needs Y < 0 for every conformal class. SW gives this for p_g > 0; for p_g = 0 it needs the b⁺ = 1 negative-Yamabe theorem (LeBrun, Kodaira dimension and the Yamabe problem — to be retrieved before citation).
   - The correct conformal identity, with g = v²ĝ and s_ĝ = s₀ < 0, is
     ∫s_g² − Y² = 36∫(Δv/v)² − 12s₀∫|∇v|²/v² ≥ 0.
     The parenthetical "3∫(Δu/u)² + 24∫|∇u|²" is a different normalization and is not to be quoted as universal.
   - The Yamabe replacement reduces the infimum problem; it does not classify L = 0 for nonconstant s.

5. **66.R.**
   - "H³(Z)" means Hausdorff measure 𝓗³.
   - M must be connected (or the theorem is stated componentwise).
   - The sign convention is Ric° = −2β_h∘h, so c′ = −√2c; the theorem's unspecified c′ absorbs this.
   - The claim that b = c₁(J₀) is one of ±K_X ± ΣE_i is **not established** and is removed. It is not used.
   - p = |b⁻|² = k + Π for cscK needs the best-sign hypothesis.

6. **66.EM is conditional.**
   - L_rank = 0 with constant s gives a harmonic φ_h on M∖Z(h). The global Einstein–Maxwell identification needs φ_h locally bounded (or otherwise removable) at Z(h), and the rank condition alone does not give that. The organizational bullets in §2bis hold under that hypothesis.
   - The EM sign/normalization: Ric° = ½(F∘F)₀ with F = φ_h + h, equivalently (Ric + F̃∘F̃)₀ = 0 with F̃ = (φ_h − h)/√2.
   - For L = 0 boundedness is automatic.

7. **Interpretation (§5).**
   - The strictly-AK part of the equality class is a *restricted instance* of the 4D Blair–Ianus problem (constant negative s, prescribed manifold, exceptional alignment), not "precisely" it.
   - No connected L = 0 locus or EM path joining cscK to Einstein has been constructed. (K) and (E) are possible objects, not the endpoints of a proven interpolation.
   - For s < 0, strictly AK equality metrics may have δ_b < 0. Also δ_b = 0 does not force Kählerness when s < 0. The interval 0 < δ_b < 1 describes the positive-flux sub-tariff branch only.
   - The negative-scalar consequence needs ĥ ∥ h_b⁻. Under that hypothesis, −s∫u ≥ 4Φ_b²δ_b(1+2δ_b); and if p ≤ (1−η)²|b⁻|², then η ≤ δ_b ≤ 2−η (and δ_b < 1 on the positive branch), so −s∫u ≥ 4Φ_b²η(1+2η).

8. **66.W.** "Weakly close to (AK_Ric)" is replaced by the two precise estimates: weighted weak closedness (66.6) with ‖R_⊥‖₂² = 8π²L_rank, and weighted amplitude control. The test norm degenerates at Z(h), and no compactness follows.

## 8. Additional results from the generator round (step66_ttcs01_generator1_integration.md), checked here

- **Conformally Kähler EM is excluded on general-type blow-ups.**
  - Statement: if g = f⁻²g_K is EM with F⁺ = ω_K, then J-invariance of Ric°_g together with Ric°_g = Ric°_K + 2f⁻¹(∇²_K f)₀ forces (∇²_K f)'' = 0. Hence J∇f is a holomorphic Killing field.
  - Consequence: on a complex surface with H⁰(T^{1,0}) = 0 (every minimal general-type surface and its blow-ups), f is constant, and conformally Kähler EM = cscK. This matches the Killing-potential formulation of Apostolov–Maschler \cite{apostolov2019conformally}.
  - Scope: it holds for every complex structure whose blow-down is of general type. Other complex structures on the same smooth manifold are also of general type (Kodaira dimension is a smooth invariant), so the exclusion covers them.
  - The construction search on the EM layer must therefore be genuinely non-Hermitian.
- **Restricted tariffs without Einstein nonexistence.**
  - δ ≤ δ₀ ⇒ p ≥ q²(1−δ₀)².
  - On the aligned AK class, I := ∫u ≥ Φ_b²(δ_b + 2δ_b²) (at s = −4 normalization −s∫u = 4I). So a torsion bound I ≤ εΦ_b² gives δ_b ≤ (√(1+8ε) − 1)/4 and the explicit tariff p ≥ |b⁻|²(1 − (√(1+8ε)−1)/4)².
- **Taubes canonical positivity does not close the range by itself.**
  - From 4πK_ω·[ω] = 4V − 2I (s = −4) and K_ω·[ω] > 0, we get V > 2π²Q(δ+2δ²). Equivalently A + υ > Q(δ+2δ²). This is vacuous for Q ≈ k ≪ A, because the Yamabe volume is not bounded above.
- **Correct local formulation near a cscK metric.**
  - Along a smooth family through cscK, both δ_t and L_t are O(t²). Local coercivity is therefore the quadratic generalized eigenvalue problem
    c_K = inf_{d₂>0} ℓ₂/(Q d₂).
  - If c_K > 0, this gives a local Kähler-end tariff p ≥ Q min_{d≤δ₀}[(1−d)² + c d].
  - A direction with d₂ > 0 and ℓ₂ = 0 would be an infinitesimal aligned non-Kähler branch, i.e. a first-order Blair–Ianus deformation with exceptional twist.
  - This is a computable, genuinely local question. It is not decided by the Burns-cell ratios, which come from degenerating families.
- **A01 #840.**
  - The SU(2)/class-A AK-Einstein saturations give only Kähler solutions, apart from the Ricci-flat Tod/GH branch. The two-direction case is still undecided.
  - A01 knows no mechanism for L ≥ cδ, and notes that any c > 0 must come from transition regions. This is consistent with the logical fact that L ≥ cδ excludes Einstein metrics.


## 9. The deficit as a minimal twist flux; the second-order deficit at cscK (Lemma 66.J)

**Lemma 66.J (variational meaning of δ).** Write √2|v| = sup_{|Ω|=√2}⟨Ω,v⟩. Then for every orientation-compatible J with c₁(J) = a, (65.1) rearranges to

  (t_J⁻, ĥ) = 2πqδ + (𝔉_ĥ − ∫⟨Ω_J, B^*ĥ⟩),

and the bracket is ≥ 0. Suppose B^*ĥ vanishes nowhere and its direction J_Ric (Kähler form Ω_Ric = √2B^*ĥ/|B^*ĥ|) lies in the class a. Then:
- the bracket vanishes exactly for J = J_Ric;
- 2πqδ = (t⁻_{J_Ric}, ĥ).

So **the metric deficit is the minimum harmonic exceptional twist flux over class-a structures, attained by the Ricci-aligned structure.** The equality case of 66.R is the case where J_Ric is in addition symplectic, with |B^*ĥ|/|ĥ|² constant.

**Second order at a cscK metric.** Let g_t be a smooth constant-scalar family through a cscK metric g₀ with c₁ = a and ĥ zero-free. Then J_Ric,t = J + tj₁ + O(t²), and ∇Ω_Ric = t(a₁⊗φ − Ja₁⊗Jφ) + O(t²), where a₁ is determined by the first variation of B^*ĥ. Since t⁻ = −(a∧Ja)⁻ is quadratic,

  d₂ = −(2πq)⁻¹ ∫⟨(a₁∧Ja₁)⁻, ĥ⟩ dμ = (2πq)⁻¹ ∫ Q_ĥ(a₁) dμ,

where Q_ĥ is the quadratic form of the symmetric trace-free endomorphism ±ĥ∘J. Its eigenvalues are ±|ĥ|/√2, each with multiplicity two. Hence **d₂ is sign-indefinite**: the deficit grows exactly when the first-order Nijenhuis vector a₁ lies predominantly in the positive eigenplane of ĥ∘J.

The local coercivity constant becomes

  c_K = inf_{d₂>0} ℓ₂/(Q d₂),

with ℓ₂ = (2π²)⁻¹[‖B′_⊥‖² + amplitude variance] the second-order misalignment. This is a quadratic-form comparison on the space of first-order Yamabe-slice deformations of g₀ modulo diffeomorphisms and Kähler moduli. The question:
- c_K > 0 gives a local Kähler-end tariff;
- a deformation with ℓ₂ = 0 and d₂ > 0 is a first-order aligned (Blair–Ianus/EM) non-Kähler branch, whose a₁ lies in the positive ĥ∘J-plane. Such a deformation is a falsifier of local linear coercivity and the infinitesimal seed of a sub-tariff construction.

This is the concrete local computation that the twist-flux line leaves; it is independent of Einstein existence.
