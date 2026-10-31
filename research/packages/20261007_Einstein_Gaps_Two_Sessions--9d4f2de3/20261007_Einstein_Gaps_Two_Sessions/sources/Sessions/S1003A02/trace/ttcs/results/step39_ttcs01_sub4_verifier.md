# TTCS Independent Branch Record

```json
{
  "step_id": 39,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex",
    "Skills/geometric-analysis/research/paper/sections/field_interfaces_and_curvature_interactions.tex",
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md",
    "Knowledge/objects/papers/Ricci-Curvature-Minimal-Volumes-and-Seiberg-Witten-Theory--995c93498a8f--cab40be18df4/object.md",
    "Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md"
  ]
}
```

## Task

Check the gauge-theoretic quantifiers needed to apply the amplitude identity on arbitrary metrics and near-minimizing sequences. For the full blow-up sign family a_epsilon=c+sum epsilon_i E_i on M=X#k CPbar^2, distinguish: nonzero perturbed Seiberg-Witten invariant, monopole class, existence of an unperturbed solution for a fixed metric, irreducibility/reducibility, b^+>=2 versus b^+=1 chambers, and the role of a_epsilon^2=A-k>0 in the low-blow-up range. Decide whether the amplitude theorem genuinely holds for every scalar-negative metric in the chamber-independent range via LeBrun's limiting argument, whether reducibles can occur when A-k>0, and what exact hypotheses must be stated elsewhere. Also test whether simultaneous choice of all 2^k solutions requires any compatibility beyond individual existence. Give a precise corrected theorem statement and sequence corollary.

## Output

# Gauge-theoretic quantifiers behind the scalar −4 amplitude identity on X # k CP̄² # ℓ(S¹×S³)

## 0. Summary

1. In the range used by the balanced family, the amplitude bound holds on every smooth metric with s ≡ −4. Two conditions suffice. Either b⁺(X) ≥ 2, or b⁺(X) = 1 with k ≤ A. Under either condition, every one of the 2^k classes a_ε has an **irreducible unperturbed** solution on **every** metric. All 2^k can be taken on the same metric. The proof is LeBrun's limiting argument plus the observation that a_ε² ≥ 0 and a_ε ≠ 0 prevent reducibles.

2. The amplitude identity needs the scalar curvature to be **constant**, s ≡ −4. Negativity of s alone does not suffice. Arbitrary metrics enter only through their Yamabe representative ĝ, and the field term is then evaluated on ĝ.

3. Choosing the 2^k solutions independently requires no compatibility condition. One normalization must be respected: the class used for each ε must be a_ε itself, not −a_ε.

4. One hidden topological input must be stated: c² = (2χ+3τ)(X). Without it, Q must be replaced by k + 4ℓ + 4d_X.

5. For b⁺(X) ≥ 2 and k > A, the identity is still exact, but the guaranteed solution may be reducible. For b⁺(X) = 1 and k > A, simultaneous supply of the whole sign family is not guaranteed at a given metric.

## 1. Four notions, and how they relate on this family

Let s_X be a spin^c structure on X with c = c₁(s_X), SW(X, s_X) ≠ 0, A = c² > 0. Set M = X # kCP̄² # ℓ(S¹×S³), Q = k + 4ℓ, a_ε = c + Σ εᵢEᵢ.

| Notion | Quantifier | Source of truth |
|---|---|---|
| Nonzero (perturbed) SW invariant | count over generic (g, η); chamber-dependent if b⁺ = 1 | index/cobordism theory |
| Monopole class (LeBrun 2006, Def. 3.1; 2001, Def. 1 for a polarization H) | **some** solution of the unperturbed equations for **every** (H-adapted) metric | deduced from the invariant by a limiting argument |
| Unperturbed solution at a fixed g | existence only; no regularity or uniqueness | consequence of monopole class |
| Irreducible (Φ ≢ 0) | needs a_g⁺ ≠ 0 | topology of a_ε |

**Topological data.**
- (2χ+3τ)(M) = (2χ+3τ)(X) − k − 4ℓ.
- a_ε² = A − k, since c·Eᵢ = 0 and Eᵢ·Eⱼ = −δᵢⱼ.
- The expected dimension is
 d_ε = (a_ε² − (2χ+3τ)(M))/4 = d_X + ℓ, where d_X = (A − (2χ+3τ)(X))/4.

For a complex minimal surface of general type, d_X = 0. This yields the note's c₂(S⁺_{a_ε}) = ℓ.

If d_X > 0, the Chern–Weil step P = 32π²d_ε + 2‖f_ε⁻‖² + 4W₊ + 4V/3 − ∫ρ_ε² carries 32π²d_ε. After Walsh averaging, 8π²Q becomes 8π²(k + 4ℓ + 4d_X).

## 2. Reducibles and the role of a_ε² = A − k

A reducible unperturbed solution has Φ = 0, hence F_A⁺ = 0. Then the harmonic representative of a_ε is anti-self-dual, i.e. a_ε ∈ H⁻_g.

The intersection form is definite on H⁻_g: a² ≤ 0 there, with equality only for a = 0. Since a_ε ≠ 0 (all E-coefficients are ±1), we have:

- **k ≤ A ⇒ a_ε ∉ H⁻_g for every g ⇒ every solution of every a_ε on every metric is irreducible.**

The task's strict inequality A − k > 0 is stronger than irreducibility needs. What it adds is uniformity: (a_{ε,g}⁺)² ≥ a_ε² = A − k > 0 for every metric. At A = k each (a_{ε,g}⁺)² is positive, but not uniformly.

Two consequences:

- **Unique continuation.** Irreducibility and unique continuation for the Dirac equation (Bär) give Φ_ε ≠ 0 on an open dense set. This is what makes the a.e. direction field n_ε, and the split |∇Φ|² = |ζ|²/ρ + ρ|∇n|²/4, meaningful.
- **No metrics with s ≥ 0, all Yamabe constants below zero.** If s_g ≥ 0, the Weitzenböck formula forces Φ ≡ 0, which is impossible. Hence every conformal class has Y < 0 and a unique smooth scalar −4 representative. This holds for b⁺ = 1 as well, without LeBrun's Prop. 3.3. LeBrun's Prop. 3.3 covers b⁺ ≥ 2 for all k.

**For k > A.** Metrics with a_ε ∈ H⁻_g are not excluded by topology. At such metrics, the limit of perturbed solutions may be the reducible (Φ = 0, F⁺ = 0).

I checked that the single-solution identities remain exact in this case:
- With ρ = 0, ζ = 0, W₀ = 0, J = 0, p = 0, and C(0) = 2/3, the relation D/18 = J + 2‖ζ‖² + ‖W⁺ − W₀‖² + ½∫C(ρ)(ρ − 2)² reduces to 4V/3 + W₊ = 4V/3 + W₊.
- The slack identity reduces to Σ = 16V.

So the amplitude bound still holds formally. The reducible ε, however, contributes the maximal deficit ∫(2 − ρ) = 2V.

## 3. b⁺(X) ≥ 2: simultaneous supply on every metric

**Every a_ε is a monopole class.**
- The blow-up formula and LeBrun 2001 Prop. 3.2 (handles via the Ozsváth–Szabó holonomy invariant) give a nonzero invariant for c − ΣE'ⱼ, where the E'ⱼ = ±Eⱼ are chosen so that c⁺·E'ⱼ ≤ 0 for the given polarization.
- In LeBrun's proof this sign choice is made per metric. Theorem 4.3 there only needs one class per metric.
- For b⁺ ≥ 2 the invariant does not depend on the metric. At a metric with c⁺·Eⱼ = 0 for all j, every sign pattern is admissible.
- Therefore all 2^k classes a_ε have nonzero invariant. This metric-independence is precisely what upgrades "one class per metric" to "the whole sign cube on every metric."

**Limiting argument at a fixed g.**
1. Take generic perturbations η_n → 0 in C^∞. The nonzero count gives perturbed solutions (Φ_n, A_n).
2. The Weitzenböck formula gives ρ_n ≤ max(−s) + C|η_n|.
3. With Coulomb gauge relative to A₀ and the harmonic part reduced modulo the lattice (compact torus H¹(M;ℝ)/H¹(M;ℤ), needed since b₁ = ℓ), elliptic bootstrapping gives C^∞ bounds modulo gauge.
4. A subsequence converges to a smooth unperturbed solution. By Section 2 it is irreducible when k ≤ A.
5. The limit need be neither regular nor unique. The identity uses neither property.

This confirms the quantifier used in Proposition webvar:all-class-budget: "every class in 𝒞(M) has a solution on g_ε" holds by the definition of a monopole class.

## 4. b⁺(X) = 1: chambers

**Setup.** H⁺_g = span(ω_g), with ω_g in a fixed time-cone component. For small perturbations, the chamber of a class a is the sign of a·ω_g. This is defined whenever a_g⁺ = (a·ω_g/ω_g²)ω_g ≠ 0.

**Case k ≤ A.** Here a_ε lies in the closed time-cone, and a_ε·c = A > 0 places it in the component of c. Hence a_ε·ω_g ≠ 0 with a fixed sign for **all** metrics, so the small-perturbation invariant of a_ε does not depend on the metric. (The same chamber geometry underlies LeBrun's remark that SW of X is polarization-independent when c² > 0.)

To evaluate it, use Gay–Kirby (cited in LeBrun 2006, proof of Prop. 3.6): the rational class c with c² > 0 is represented by a closed form that is self-dual for some metric g_c. Since b⁺ = 1, this gives H⁺_{g_c} = span(c). Then c⁺·Eⱼ = 0, so every sign pattern satisfies LeBrun's condition at g_c.

Hence every a_ε has nonzero invariant, is a monopole class for every polarization, and is supplied irreducibly on every metric. The same chamber reasoning applies with handles, since only a_ε⁺ enters the chamber. The handle invariant's nonvanishing at span(c) is LeBrun 2001 Prop. 3.2.

**Case k > A.** Now a_ε is spacelike. Polarizations with a_ε⁺ = 0 form a wall, and wall-crossing changes the count. On one side the invariant may vanish.

LeBrun's per-metric sign selection still gives one class with (c₁⁺)² ≥ A at every metric. The full Walsh cube on a common metric is not guaranteed.

Because the balanced family has h_j → 0, we have k_j ≤ Q_j < A_j eventually. The b⁺ = 1 members of the family are therefore covered. The variational section currently states b⁺(M_j) ≥ 2; the extension needs the argument of this section.

## 5. What in the identity needs s ≡ −4

The normalization is F⁺ = 2iσ(Φ), with |σ|² = ρ²/8. LeBrun's form ⟨Φ, D*DΦ⟩ = ½Δ|Φ|² + |∇Φ|² + s|Φ|²/4 + 2⟨−iF⁺, σ⟩ then gives
 0 = 2Δρ + 4|∇Φ|² + sρ + 2ρ².

At s ≡ −4 this yields:

- **Amplitude bound:** ρ ≤ 2, by the maximum principle (−4ρ + 2ρ² ≤ 0 at a maximum).
- **Kinetic term:** K = ∫ρ − ½∫ρ² = ½∫ρ(2 − ρ).
- **Curvature norm:** |f⁺|² = ρ²/2.
- **Scalar term:** S = 16V, so S/12 = 4V/3.

**Checks of the identity's algebra.**
- **Slack identity.** 16K + 4∫(ρ − 2)² + 8J = 16V − 4∫ρ² + 8J, which equals Σ by ∫ρ² = 8π²p + 2J.
- **Amplitude form.** Writing −4K = −4∫(2 − ρ) + 2∫(2 − ρ)² turns P − 8π²Q = 𝒜 − 4E K into the boxed form with weight b + 2.
- **Chern–Weil step.** With P = 4W₊ + 4V/3 − 8π²(A − Q), and Chern–Weil applied to ‖f_ε^±‖², one gets P = 32π²ℓ + 2‖f_ε⁻‖² + 4W₊ + 4V/3 − ∫ρ².
- **Walsh singleton charge.** ‖f_{i}⁻‖² − ‖f_{i}⁺‖² = 4π².
- **Kähler–Einstein test (k = 0, s = −4).** Here ρ ≡ 2, W⁺ = diag(−2/3, 1/3, 1/3) = W₀, and V = 2π²A. This gives D = 24V + 12V − 36V = 0.

The general exact decomposition (ssc-exact-decomposition) is imported from a section not supplied here. Beyond the reducible and Kähler–Einstein tests above, I have not re-derived it.

**Transfer to arbitrary metrics.** For nonconstant s, the K formula, ρ ≤ 2, and S = 16V all change. The statement for arbitrary g therefore goes through ĝ:
 P(g) = P(ĝ) + (S(g) − S(ĝ))/12 ≥ P(ĝ).
This holds because W_±-energies are conformally invariant and the Yamabe metric minimizes S in a class with Y < 0.

## 6. Independent choice of the 2^k solutions

- **No compatibility needed.** Every quantity in the identity is gauge-invariant: f_ε, ρ_ε, |ζ_ε| (since ζ = ⟨Φ, ∇Φ⟩ is invariant), and W₀,ε (built from σ(Φ)). The Walsh/Parseval and Chern–Weil steps use only the real classes [f_ε/2π] = a_ε. Solutions may therefore be chosen independently per ε, with no continuity in ε, in the metric, or along a sequence.
- **Sign normalization.** For each ε the solution must have class +a_ε. Conjugation (LeBrun 2006 Lemma 3.5) also supplies −a_ε, and mixing the two would break [f_∅/2π] = c.
- **Torsion.** If H²(M;ℤ) has 2-torsion, several spin^c structures share the real class a_ε. Any choice is allowed. The paired construction S⁺_{ε'} ≅ S⁺_ε ⊗ N then holds with c₁(N) = (a_{ε'} − a_ε)/2 plus a torsion term, which is invisible to real Chern–Weil.
- **Relative connection on N.** It is forced: from L_{ε'} ≅ L_ε ⊗ N², define B = (A_{ε'} − A_ε)/2. This is unique, because a 1-form b with 2b = 0 vanishes. No extra matching condition arises.
- **Choice dependence.** The combination 4E K − 𝒜 = 8π²Q − P(g) is the same for every choice. The deficit E∫(2 − ρ) may depend on the choice. The optimal statement therefore uses the infimum over choices.

## 7. Corrected statement

**Theorem (metric-wise amplitude bound).** Let X be closed and oriented, and let s_X be a spin^c structure with c = c₁(s_X), A = c² = (2χ+3τ)(X) > 0, and SW(X, s_X) ≠ 0. If b⁺(X) = 1, the invariant is taken in the small-perturbation chamber, which is metric-independent since c² > 0. For ℓ > 0, assume the nonzero holonomy invariant of LeBrun 2001 Prop. 3.2. Put M = X # kCP̄² # ℓ(S¹×S³), Q = k + 4ℓ, a_ε = c + ΣεᵢEᵢ. Assume either

- (i) b⁺(X) ≥ 2, or
- (ii) b⁺(X) = 1 and k ≤ A.

Then:

(a) For every smooth metric g and every ε ∈ {±1}^k, the unperturbed equations D_AΦ = 0, F_A⁺ = 2iσ(Φ) have a smooth solution for a spin^c structure with c₁^ℝ = a_ε. If k ≤ A, every such solution is irreducible and Φ_ε ≠ 0 on an open dense set. In case (i) with k > A, a solution exists but may be reducible.

(b) Every conformal class has Y < 0.

(c) Suppose s_g ≡ −4, and pick any one solution per ε, independently. Then the exact identity
 P − 8π²Q + 4E_ε∫(2 − ρ_ε) = 2‖f_∅⁻‖² + 2Σ_{I≠∅}‖f_I⁺‖² + E_ε[8‖ζ_ε‖² + 4‖W⁺ − W₀,ε‖² + ∫(b(ρ_ε) + 2)(2 − ρ_ε)²]
holds. Hence P(g) ≥ 8π²Q − 4 inf_{choices} E_ε∫_M(2 − ρ_ε) dμ_g.

(d) For an arbitrary metric g, let ĝ be its scalar −4 Yamabe representative. Then P(g) ≥ P(ĝ) ≥ 8π²Q − 4 inf_{choices} E_ε∫(2 − ρ_ε) dμ_ĝ.

If (2χ+3τ)(X) < c², replace Q by k + 4ℓ + 4d_X throughout.

**Corollary (near-minimizing sequences).** Let M_j be the balanced family, with each X_j satisfying the hypotheses, so that eventually k_j ≤ Q_j < A_j. Let g_j be arbitrary smooth metrics with s ≡ −4. Write δ_j := inf_{choices} E_ε∫(2 − ρ_ε) dμ_{g_j}.

1. P(g_j) ≥ 8π²Q_j − 4δ_j. Combined with ∫ρ ≥ ½∫ρ² = 4π²p_ε + J_ε and p_ε ≥ A_j − k_j, this gives the a priori bound
 4δ_j ≤ 16π²k_j + Δ_S(g_j)/2 − 4 E_ε J_ε,
 so on selected near-minimizers δ_j = O(Q_j).
2. If some sequence with P(g_j) − p_j → 0 has δ_j = o(Q_j), then p_j/(8π²Q_j) → 1 and α_j/h_j → 4, using recovery and (webvar:reduction).
3. If p_j ≤ 8π²(1 − δ)Q_j along a subsequence, then every scalar −4 near-minimizer and every field choice satisfy
 - E∫(2 − ρ_ε) ≥ 2π²δQ_j − o(1), and
 - the bracketed remainder ≤ 4E∫(2 − ρ_ε) − 8π²δQ_j + o(1).

## 8. What this does not settle

The quantifiers are closed: for k ≤ A, the full sign cube is supplied irreducibly on every metric. The coefficient-four question is now equivalent, on near-minimizers, to proving δ_j = o(Q_j) for some field choice.

Nothing in the gauge theory above produces such a bound. Both the existence argument and the choice freedom act only through individual solutions. The a priori estimate 4δ ≤ 16π²k + Δ_S/2 shows that the open coefficient sits entirely in the amplitude deficit tied to the exceptional classes and the scalar excess.

Resolving it needs an estimate on amplitude depletion that is not supplied by the existence or choice arguments. It must also be compatible with the null-period perpendicular cell, where (E_g⁺)² → 0 and the 4π² relative charge is carried by h⁻.