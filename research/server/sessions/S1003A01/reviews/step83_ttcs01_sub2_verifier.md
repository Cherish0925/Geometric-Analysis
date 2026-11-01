# TTCS Independent Branch Record

```json
{
  "step_id": 83,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step83_normalized_action_weyl_deficit_and_AKE_degenerations.md",
    "Sessions/S1003A01/workspace/notes/step77_goldberg_first_tier_collapse_and_canonical_curve_identity.md",
    "Sessions/S1003A01/workspace/scripts/step83_weyl_deficit_algebra.py",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md"
  ]
}
```

## Task

Verify the mathematics of the Step-83 note on closed four-manifolds (Einstein gaps programme, closed negative-scalar Goldberg problem Q4 and Einstein existence on nonminimal general-type surfaces Q1). Check, with attention to hypotheses and quantifiers: (1) Theorem 83.1: local constancy of the normalized Einstein-Hilbert action on the set of Einstein metrics via Koiso's real-analytic premoduli and Lojasiewicz stratification; is the C^1/critical-point argument on each stratum correct, are there topology subtleties (C^{k,alpha} vs C^infinity, slice vs moduli, finite isometry quotient), and is the finiteness of values on compact subsets of the moduli correct? (2) Identities (0.1) D=Shat^2/16-2pi^2(2chi+3tau) for Einstein metrics and (0.2) D=T_AK for almost-Kahler Einstein metrics (using the Step-77 AAD balance), and Theorem 83.2 (a),(b) including the reversed-orientation value T_AK=12 pi^2 tau and the ball-quotient and product checks. (3) Lemma 83.3 (deficit transfer without energy identity) under noncollapsed bounded-diameter orbifold convergence: volume convergence, the concentrated energy m>=0, and the formula for T_+. (4) Theorem 83.5: extension of the limiting almost-Kahler form across orbifold points, the no-concentration argument m=m_T=0 (does it really follow from Fatou plus D=T_AK on both the smooth manifolds and the orbifold?), bubbles Ricci-flat with W+=0 and parallel limiting forms (Weitzenbock), and (d). Are bubble-tree intermediate scales and neck regions correctly covered by 'concentrated energy'? (5) Corollaries 83.4, 83.6, Proposition 83.7 (finitely many connected components of Einstein metrics GH-near V implies Shat constant there; nested finite value sets argument), and Corollary 83.8 for M = X # k CP2bar using LeBrun's estimate int s^2 >= 32 pi^2 c1(X)^2 for all metrics (check that this estimate indeed holds for every b+ for minimal general type X, from the LeBrun 2001 file). Identify any error, missing hypothesis, or overstatement, and give corrected statements. Also assess whether Theorem 83.2 and Corollary 83.8 are likely already known in the literature (LeBrun, Koiso), so the note's novelty is stated accurately.

## Output

# Step 83 verification memo: Weyl deficit, normalized action, and AKE degenerations

**Bottom line.** The analytic core of Step 83 is correct:

- local constancy of Ŝ (83.1),
- the deficit identities (0.1) and (0.2),
- Theorem 83.2(a),
- the transfer Lemma 83.3,
- the no-concentration Theorem 83.5,
- Corollary 83.8.

One computation is wrong. The ball-quotient "consistency check" r4 uses a factor-2 error. When corrected, it gives no contradiction. A correct replacement exists: Armstrong's theorem, as quoted in the LeBrun 2001 file.

Several statements need quantifier repairs:

- Cor. 83.4: m = 0 is unconditional as written.
- Cor. 83.6(b): "decreases strictly".
- Prop. 83.7: "reduced exactly".
- Cor. 83.8: orientation of the Kähler orbifold, and a mis-cited equation.

Theorem 83.1 is classical, and 83.2(a) is very likely known.

---

## 1. Theorem 83.1 (local constancy of Ŝ)

**Variation formula.** With s̄ = ∫s/Vol,

DŜ_g(h) = Vol^{-1/2}∫⟨−Ric + (s/2)g − (s̄/4)g, h⟩.

Tracing the critical equation gives s = s̄, hence Ric = (s/4)g. Scale invariance holds in dimension 4: the factors scale as λ^{-1}·λ²·λ^{-1} = 1. Both are correct.

**Stratum argument.** Each Łojasiewicz stratum Σ_i is a C^∞ submanifold of the finite-dimensional analytic manifold Z. Z is itself a submanifold of the slice, so Ŝ|Σ_i is smooth. Its differential is DŜ_x restricted to T_xΣ_i. That vanishes because x is a critical point of Ŝ on the full space of metrics, not merely on Z. The argument is correct.

One point needs a sentence. "Each stratum has g in its closure" is not true for an arbitrary stratification; it is obtained by shrinking the neighbourhood. Local conic structure of semianalytic germs (Łojasiewicz) does this. Alternatively, use the curve selection lemma: every Einstein x ∈ P_g near g is joined to g by a piecewise real-analytic arc in P_g, and d/dt Ŝ(γ(t)) = DŜ(γ′) = 0 on each piece. This version is cleaner and avoids stratum bookkeeping.

**Topology.**

- *C^{k,α} versus C^∞.* C^{k,α} Einstein metrics are real-analytic in harmonic coordinates (DeTurck–Kazdan). A C^∞ neighbourhood is contained in the C^{k,α} neighbourhood where Koiso's slice theorem applies. Local constancy in C^{k,α} therefore implies it in C^∞.
- *Slice versus moduli.* The local moduli near [g] is P_g/Isom(g). Ŝ is Isom(g)-invariant, so it descends. The finite isometry quotient affects nothing.
- *Finiteness on compact sets.* Ŝ descends to a continuous, locally constant function on 𝔈(M) with the quotient topology. A compact set is covered by finitely many sets on which Ŝ is constant. Correct.

**Useful reformulation.** For Einstein metrics, Gauss–Bonnet gives Ŝ² = 24(8π²χ − ∫|W|²). With the signature formula, 83.1 is the same statement as local constancy of ∫|W^±|² on 𝔈(M).

**Novelty.** "The total scalar curvature is constant on connected components of the Einstein moduli" follows from Koiso's analyticity. It is presented in the standard literature (Koiso; Besse, Chapter 12, around the premoduli theorem 12.49). Theorem 83.1 should be labelled a recalled standard result. The exact locus should be pinned down against the pending retrieval s83_t9_tool1.

## 2. Identities (0.1), (0.2) and Theorem 83.2

**(0.1).** Using 4π²T₊ = ∫(2|W⁺|² + s²/24),

Ŝ²/16 − 2π²T₊ = s²V/16 − ∫|W⁺|² − s²V/48 = s²V/24 − ∫|W⁺|² = D.

Correct. Note that D = 0 for every Kähler metric, since |W⁺|² = s²/24 pointwise; constant scalar curvature is not needed.

**(0.2).** Integrate the pointwise formula

|W⁺|² − s²/24 = 2|η|² + trV² + sq/8 + 3q²/32.

The AAD balance −sQ/16 = E + T_AK gives sQ/8 = −2E − 2T_AK. Substituting:

∫(|W⁺|² − s²/24) = 2E + T_AK − 2E − 2T_AK = −T_AK.

So D = T_AK. The pointwise formula is consistent with q = 4r − 2s/3: indeed (3/2)r² = 3q²/32 + sq/8 + s²/24.

**Theorem 83.2.**

- *(a)* Correct. It needs a KE metric g₀ with c₁ < 0 and complex orientation equal to that of M. Then Ŝ²(g₀) = 32π²c₁² = 32π²T₊. 83.1 gives D ≡ 0 on the component, and D = T_AK forces Kähler.
- *(b)* Correct: D̄ = Ŝ²/16 − 2π²(2χ − 3τ) = 12π²τ on the component. Kim's formula for the reversed orientation gives the same value independently:
  - 8π²(χ + 3τ) = T̄_AK + 3∫|W⁺|²;
  - ∫|W⁺|² = s²V/24 = (4/3)π²(2χ + 3τ) on the component;
  - hence T̄_AK = 12π²τ.

**Product check.** Correct. Σ_g×Σ_h with one factor's complex structure reversed is Kähler for the reversed orientation, and τ = 0.

**Ball-quotient check: the computation is wrong.**

- The session convention (Step 77) is s* = s + q.
- The script docstring for check (4) uses s* − s = q/2, which contradicts Step 77.
- Correct values: on CH²/Γ with reversed orientation, W⁺′ = 0, so r = 0 and s* = s/3. Then q = s* − s = −2s/3, not −4s/3.
- Hence T̄_AK = 3q²V/32 = s²V/24 = (1/24)·32π²·9τ = 12π²τ. This equals the forced value, so the corrected residual r4 is **0**.

The "mismatch" 36π²τ is exactly 3∫|W⁺|², the term dropped by the error. In fact every integral identity of Step 77 is satisfied by a hypothetical reversed AK form here:

- (★) holds with E = 0.
- Weitzenböck for a harmonic constant-length form with W⁺′ = 0 gives |∇ω|² = −2s/3 automatically.

So r4 excludes nothing. The sentence "no reversed AK structure, consistent (r4 = 36π²τ ≠ 0)" must be withdrawn.

**Correct replacement.** W⁺′ = 0 makes ω trivially an eigenvector of W⁺′ everywhere. The LeBrun 2001 file quotes Armstrong: compact Einstein strictly almost-Kähler 4-manifolds with ω everywhere a W⁺-eigenvector do not exist. A Kähler reversed structure is impossible, since it would force |W⁺′|² = s²/24 ≠ 0. LeBrun's Mostow-type rigidity says every Einstein metric on CH²/Γ is the CH metric. Together, ball quotients carry no reversed AKE metric at all.

Lesson for (b): at χ = 3τ the forced value 12π²τ is automatically consistent. Theorem 83.2(b) has content only where the reversed W⁺′ is nonzero.

**Novelty of 83.2(a).** An AKE metric with form ω has a Taubes monopole class: canonical class, chamber of ω, valid for b⁺ = 1 as well. LeBrun gives s²V ≥ 32π²(c₁⁺)² ≥ 32π²c₁². Equality characterizes cscK Kähler metrics (LeBrun 2001, proof of Prop. 4.1, citing [27]). With 83.1, a KE component consists of Kähler metrics. This is a short combination of known results. I recall LeBrun stating that on minimal general-type surfaces KE metrics fill whole components of the Einstein moduli, but the supplied file does not contain that sentence, so the attribution must be checked.

What Step 83 adds:
- the SW-free route through D = T_AK;
- part (b), which has no SW counterpart.

## 3. Lemma 83.3 (deficit transfer)

**Hypotheses.** Fixed s₀ < 0, bounded diameter, and a volume lower bound give uniform noncollapsing by Bishop–Gromov. The bound ∫|Rm|² = 8π²χ holds in the operator norm on Λ², where |s/12·Id_{Λ²}|² = s²/24. These give orbifold compactness with a bounded number of singular points.

**Volume convergence.** Volume on M∖B_δ(S_n) converges smoothly. Bishop–Gromov with Ric ≥ −|λ| bounds the δ-neighbourhoods by NCδ⁴. Hence Vol_n → Vol(V) and Ŝ²(g_n) → Ŝ²(V).

**Concentrated energy.** m = lim_δ lim_n ∫_{B_δ(S_n)}|W⁺|² exists after one subsequence and is monotone in δ.

**Formulas.**
- D(g_n) → D(V) − m.
- T₊(M) = T₊^curv(V) + 2m/(4π²) = T₊^curv(V) + m/(2π²).

Both are correct. They use only the splitting, not an energy identity.

**Necks.** B_δ(S_n) contains every bubble scale and every neck annulus of the tree. m therefore accounts for all of them; question (4) is answered affirmatively.

## 4. Theorem 83.5 (AKE degenerations)

**(a) Convergence and extension of ω.**
- Pulled-back forms Φ_n*ω_n are harmonic with |ω| = √2. Elliptic estimates give C^k convergence on compact sets of V∖S. The limit is closed, self-dual, and of length √2.
- Extension across S: lift to the orbifold chart, where g_V is smooth by the removable-singularity part of BKN/Tian/Anderson. A bounded closed and coclosed form on B⁴∖{0} is weakly harmonic on B⁴: test with a cutoff φ_ε, using ‖dφ_ε‖_{L¹} = O(ε³). It is therefore smooth, with constant length by continuity.
- Side consequence: Γ fixes a vector of Λ⁺, so Γ is conjugate into U(2).

Correct.

**(b) No concentration.** Define m_T = lim_δ lim_n ∫_{B_δ} τ_n ≥ 0, where τ_n = trV² + 3q²/32. The densities converge locally smoothly, because they are built from W⁺, the frame u and ∇ω. Splitting, not merely Fatou, gives lim T_AK(g_n) = T_AK(V) + m_T.

The AAD balance (★) on V comes from integrating divergence identities. Stokes holds on a compact orbifold with smooth orbifold data, so D(V) = T_AK(V). The chain is then

T_AK(V) + m_T = lim D(g_n) = D(V) − m = T_AK(V) − m,

so m + m_T = 0 and both vanish. The argument is valid as written.

**(c) Bubbles.**
- L² norms of W⁺ are scale invariant, and every bubble region eventually lies in each B_δ. Hence W⁺ ≡ 0 on every bubble, including deeper orbifold bubbles.
- The rescaled form λ_n²ω_n has length √2 and is still harmonic, by conformal invariance of self-duality in the middle degree.
- On the Ricci-flat limit, the Weitzenböck formula gives 0 = |∇ω|² − 2W⁺(ω,ω) = |∇ω|². So bubbles are Kähler and Λ⁺-flat, oriented compatibly with M.

Correct. Combined with the signature formula, all concentrated curvature is |W⁻|², which is consistent with T₊ being preserved: 2Δχ + 3Δτ = 2m₋/8π² − 3m₋/12π² = 0.

**(d) Normalized action of the limit.** This follows from D(V) = Ŝ²(V)/16 − 2π²T₊^curv(V) together with m = 0. Correct.

**Torsion-zero migration.** The last paragraph on c₂(E) is heuristic and should be labelled as such.

## 5. Corollaries 83.4, 83.6, Proposition 83.7, Corollary 83.8

**Corollary 83.4.** The proof gives D_𝒞 = D(V) − m.

- When D(V) ≤ 0, every AKE member of 𝒞 is Kähler. Correct.
- When D(V) < 0, 𝒞 contains no AKE metric. Correct.
- "m = 0" does **not** follow in general. Corrected statement: m = D(V) − D_𝒞. If 𝒞 contains an AKE metric and V is KE, then D_𝒞 = 0 and m = 0.
- If M also carries LeBrun's estimate Ŝ² ≥ 32π²T₊, then D ≥ 0 on 𝔈(M), which forces D_𝒞 = 0 and m = 0 for a KE limit. This holds, for example, when M is minimal symplectic with c₁² = T₊ > 0.

**Corollary 83.6.**

- *(a)* Correct: positive values from a finite set are bounded below.
- *(b)* Correct with one fix. The limit is Kähler because T_AK(V) = lim T_AK = 0. It has S ≠ ∅, since otherwise the sequence converges in 𝔈(M), contradicting (a). The relation Ŝ²(g_n) = Ŝ²(V) + 16T_AK(g_n) is correct. But "decreases strictly" is unjustified; replace with "Ŝ²(g_n) > Ŝ²(V) and Ŝ²(g_n) → Ŝ²(V)".
- *Sharpening of (c).* Here Vol = Ŝ²/s₀² ≥ 32π²c₁²/s₀². If c₁²(M) > 0, Bishop–Gromov makes (N) equivalent to a diameter bound. The only alternative to (b) is then diameter divergence with thin regions, a thick–thin/cusp picture. If c₁² = 0, then T_AK → 0 forces Vol → 0, which is genuine collapse.
- The example Σ_g×Σ_h with a pinched geodesic is correct.

**Proposition 83.7.**

- *Topologies.* Two topologies are in play.
  - Within 𝔈(M), GH convergence to a smooth Einstein metric on M implies C^∞ convergence. A bubble at a smooth point would be a Ricci-flat ALE space with trivial group at infinity, hence flat by Bishop–Gromov rigidity.
  - Ŝ is GH-continuous by Colding volume convergence, at fixed s₀.
  - Hence "connected components" is unambiguous. This should be stated.
- *Nested-sets argument.* Correct. The sets F_j are finite, nested and nonempty, so they stabilize. Every stable value is approached by metrics GH-converging to V, so it equals Ŝ(V).
- *Conclusion.* In U_J, D(g) = 2π²(T₊^curv(V) − T₊(M)) = −m(V) ≤ 0. So U_J contains **no** strict AKE metric. "T_AK bounded below on strict AKE metrics GH-near V" is vacuous in that form; state the nonexistence directly.
- *"Reduced exactly".* Overstated. Finiteness of components near every KE orbifold arising as a limit is a **sufficient** condition for a positive lower bound on T_AK over strict AKE metrics with bounded diameter. The converse is not shown. Correct to "reduced to".

**Corollary 83.8.**

- *Arithmetic.* D ≥ 2π²A − 2π²(A − k) = 2π²k, and D(V) ≥ 2π²k + m. Correct, and consistent with script r5.
- *Source of the scalar bound.* The note cites "LeBrun (8)", but (8) in the LeBrun 2001 file is the L³ estimate for (2/3·s + 2w)₋. It does not imply ∫s² ≥ 32π²(c₁⁺)², because |2/3·s + 2w| can exceed |s|. The correct source in the file has two parts:
  - the scalar inequality ∫s² ≥ 32π²(c₁⁺)² for monopole classes (introduction; §4, citing [28]);
  - for every metric on M = X#kCP²bar, a monopole class with (c₁⁺)² ≥ c₁²(X) (proofs of Prop. 3.2 and Thm 4.3). This is valid for b⁺ = 1 because c₁²(X) > 0 keeps c₁⁺ ≠ 0, so no wall is crossed.

  So "every b⁺" is confirmed.
- *Orientation.* The exclusion concerns orbifolds V that are Kähler for the orientation induced from M. A KE orbifold with the opposite complex orientation has D(V) ≠ 0 in general and is not covered. "Of any type and orientation" correctly refers to the ALE trees, which may be arbitrary because the lemma uses no bubble information. It should not be read as referring to the orbifold.
- *Content and novelty.* The result has content only for 1 ≤ k < A/3, since LeBrun's Thm 3.3 gives nonexistence for k ≥ A/3. It is a two-line consequence of LeBrun's scalar estimate plus volume convergence. A KE limit would have Ŝ²(V) = 32π²T₊^curv(V) ≤ 32π²(A − k) < 32π²A ≤ lim Ŝ²(g_n). It is plausibly folklore and should be presented as an immediate corollary.
- *What is new.* The quantitative bulk bound D(V) ≥ 2π²k + m, and its use with T_AK on AKE orbifolds.

## 6. Summary of corrections

| Item | Status | Correction |
|---|---|---|
| 83.1 | correct; classical (Koiso/Besse) | justify "g in every stratum closure" by local conic structure or curve selection |
| (0.1), (0.2), 83.2(a)(b) | correct | 83.2(a) likely known via LeBrun [27] plus 83.1 |
| ball-quotient check r4 | **wrong** (q = −2s/3, residual 0) | replace with Armstrong's theorem plus Mostow-type rigidity |
| 83.3 | correct, necks included | — |
| 83.5 | correct | label the c₂(E) migration as heuristic |
| 83.4 | m = 0 conditional | m = D(V) − D_𝒞; zero if an AKE member exists, or if LeBrun's D ≥ 0 holds |
| 83.6(b), (c) | "strictly decreases" unjustified | (N) ⇔ diameter bound when c₁² > 0 |
| 83.7 | "exactly" overstated | sufficient condition; state GH = C^∞ on 𝔈(M); the conclusion is nonexistence of strict AKE in U_J |
| 83.8 | correct | cite the scalar estimate, not (8); require V Kähler for the orientation induced from M |

The script docstring and check (4) should be corrected to s* = s + q. With that change the residual is 0, which is the expected outcome rather than a contradiction.