# TTCS Independent Branch Record

```json
{
  "step_id": 64,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step64_diffuse_twist_AAD_and_SW_zeros.md",
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md",
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md"
  ]
}
```

## Task

Verify and strengthen the mathematics of the Step-64 note. Focus on four load-bearing points: (1) the diffuse torsion scale inferred from Theorem 63.T, including constants in equations (64.3)-(64.4); (2) the weak H^{-1}-type estimate (64.7)-(64.9) derived from the Apostolov–Armstrong–Drăghici transition identity—check whether integration by parts really removes every curvature derivative, what norms/boundary hypotheses are needed, and whether the claimed dependence on Ric'', rho_*'', W3 is valid; (3) the scaling argument that topologically required Nijenhuis zeros can shrink without a scale-invariant L2 curvature payment; and (4) Proposition 64.H for a transverse C^2 spinor zero—check the Hopf-map formulas, frame-twist density, logarithmic coefficients, and the conclusion that the normalized SW Bloch field cannot directly be used as the smooth J in Theorem 63.T. Give corrected theorem statements with exact scope where needed, and explain what these results genuinely imply for the open-range Einstein-gap problem. Use the cited AAD source and prior Step-63 theorem as grounding; do not assume an unproved global near-minimizer decomposition.

## Output

# Verification memo on Step 64: diffuse twist, the AAD transport estimate, Nijenhuis zero cores, and SW Bloch zeros

**Grounding.** The checks below use:
- AAD (arXiv math/0109098): equations (19)–(26), Lemma 2, Corollary 1 (37)–(38), and the gauge formulas (21)–(24).
- Theorem 63.T, Proposition 63.AK, and the Step-63 corrections in §6 of the Step-63 note.
- Theorems N and W of Step 40 and the Step-43 material.

**Summary.**
- Most Step-64 algebra is correct.
- Four statements need correction:
  - (64.1) and (64.2) assert equalities where 63.T gives only one-sided bounds, and the sign in (64.2) is reversed.
  - The "diffuse" reading of (64.4) is a hypothesis, not a consequence.
  - (64.9) is quantitatively empty at the template scale.
  - The §4 conditional theorem (a harmonic-radius bound prices the cores) does not hold as stated.
- Three new exact statements come out of the checks:
  - **Lemma H:** the harmonic projection of the twist is pinned by topology.
  - **Lemma B:** the mean torsion equals a symplectic-period/volume slack.
  - **Lemma O:** the torsion field must oscillate at unit scale.

---

## 1. The torsion scale from Theorem 63.T

### 1a. What 63.T actually gives

For any smooth orthogonal J with c₁(J) = a, write
- γ_J⁻ = ρ₀ᴶ + t_J⁻;
- ‖ρ₀ᴶ‖² = ½∫|Ric₀′|² ≤ P/2.

Let 𝖧⁻ denote L²-projection onto g-harmonic ASD forms. Because γ_J is closed with [γ_J] = 2πa, for every harmonic ASD h we have ⟨γ_J⁻, h⟩ = ⟨γ_J, h⟩ = 2π⟨a, h⟩. Hence:

**Lemma H (exact, any g, any J).**
$$\mathsf H^-(t_J^-)=2\pi h_a^- -\mathsf H^-(\rho_0^J),\qquad
\|\mathsf H^-(t_J^-)-2\pi h_a^-\|_2\le\sqrt{P/2}.$$

Consequences:
- **Equation (64.1).** Its first half (‖ρ₀‖ = o(√k)) is correct. Its second half is only the lower bound
  ‖t_J⁻‖ ≥ 2π√(k+Π) − √(P/2).
  The exact ASD part of t_J⁻ is unconstrained by 63.T, so no upper bound follows.
- **Equation (64.2).** It is not implied by 63.T. By Lemma H, it is equivalent to the hypothesis that the exact part of t_J⁻ is o(√k).
  - Sign: in every convention with t := γ⁻ − ρ₀, including the AK one where t = −(a∧Ja)⁻, the harmonic part is **+**2πh_a⁻, not −2πh_a⁻.
- **Equation (64.17) in §4 is mis-posed.** 𝖧⁻(t_J⁻) is not an unknown to be estimated, because it is fixed by Lemma H. An inequality ‖𝖧⁻(t)‖² ≤ C·𝓔_geom with 𝓔_geom ≲ P would be the gap P ≳ k itself, restated.
  - The genuine unknown is how cheaply the fixed flux 2πh_a⁻ can be written as (α∧β)⁻ plus an exact ASD form, with small ρ₀.

### 1b. Constants in (64.3)–(64.4)

**The AK case.**
- |a∧Ja| = |a|² = u. A decomposable 2-form has |θ⁻| = |θ|/√2, so |t⁻|² = u²/2. ✓
- Squaring the 63.T bound with P = o(k) gives ½∫u² ≥ 4π²(k+Π) − o(k). ✓

**The general-J version.** Here |(α∧β)⁻| ≤ |∇Ω|²/(4√2), so
$$\int|\nabla\Omega|^4\ \ge\ 32\bigl(2\pi\sqrt{k+\Pi}-\sqrt{P/2}\bigr)_+^2 .$$
This should be recorded alongside (64.3), because it does not use the AK hypothesis.

**The RMS bound is volume-dependent.** The correct statement is
u_rms² := ∫u²/V ≥ 8π²(k+Π)/V − o(k/V).

For the s = −4 Yamabe representative the volume lies in a fixed window:
- 2π²(A+Π) ≤ V, from LeBrun's ∫s² ≥ 32π²(a⁺)² with (a⁺)² = A+Π for the best sign;
- V ≤ (3/4)(P + 8π²(A−k)), from the closed identity P = 4∫|W⁺|² + 4V/3 − 8π²(A−k).

So u_rms ≥ 2√((k+Π)/A) only at V ≃ 2π²A. In general the constant 2 becomes 2/√3 at worst.

**The fourth-moment version.** The quantity behind "|∇Ω|_rms ≍ (k/A)^{1/4}" is the fourth moment:
⟨|∇Ω|⁴⟩^{1/4} = 2u_rms^{1/2} ≥ 2√2((k+Π)/A)^{1/4} at V = 2π²A.
The L²-mean of |∇Ω| (equivalently ū) has **no** lower bound, because u may concentrate.

The step from an L²-lower bound on u to "u is diffuse" is therefore item 3 of the construction problem 64.C, an assumption. It is the dividing line between two regimes:
- diffuse: ū ≈ u_rms;
- patch-type (Step 63 §4): u concentrated near |s|/6 on small volume.

### 1c. Two exact AK identities that sharpen the template

**Lemma B (mean torsion is a period slack).**
- From γ_J⁺ = ((s+s*)/8)Ω + ρ_*″, s* = s + 4u and |Ω|² = 2, one gets 2π a·[Ω] = ∫(s/2 + u).
- At s ≡ −4 this gives ∫u = 2V + 2π a·[Ω], where ∫Ω∧Ω = 2V.

With V_* = 2π²(A+Π) and |a⁺| = √(A+Π), this rearranges to
$$\int u=2\sqrt V\bigl(\sqrt V-\sqrt{V_*}\bigr)+2\pi\bigl(a^+\!\cdot[\Omega]+|a^+|\,|[\Omega]|\bigr).$$
Both terms are ≥ 0 by LeBrun's volume bound and Cauchy–Schwarz in H⁺. Check: in the Kähler case ∫u = 0. ✓

Thus the linear "financing" term ∫u(|s| − 5u) in (63.3) is, to leading order, the volume excess plus the misalignment of [Ω] from −a⁺.

**The W₂/W₃ load.** At s ≡ −4, (63.3) gives
2‖ρ_*″‖² + 4‖W₃⁺‖² = ∫u(4 − 5u) + P − 2‖γ⁻‖².

Using ‖γ⁻‖ ≤ ‖ρ₀‖ + ‖t⁻‖ ≤ √(P/2) + ‖u‖₂/√2:
$$2\|\rho_*''\|^2+4\|W_3^+\|^2\ \ge\ 4\!\int u-6\!\int u^2-2\sqrt P\,\|u\|_2 .\tag{B}$$
In the diffuse template, ∫u ≈ 4π²√(kA) while ∫u² ≈ 8π²k. So the Weyl components W₂ and W₃ must carry L² energy of order √(kA) ≫ k.

**Lemma O (oscillation).** This uses AAD (23): da − Ja∧b = −R(Jφ) and d(Ja) + a∧b = −R(φ).
- In a gauge with b = 0 at the point, the left sides are antisymmetrized covariant derivatives of a.
- ⟨R(φ), Ω⟩ = ⟨φ, ρ_*⟩ gives |ρ_*″| ≤ C|∇ᵇa|.
- On ⟦Λ^{0,2}⟧, R restricts to W⁺ + s/12 = −(u/2)Id + W₃⁺, so |W₃⁺| ≤ C(|∇ᵇa| + u).
- Since |∇²Ω| ≥ c|∇ᵇa| − Cu, (B) gives, for every closed AK four-manifold with s ≡ −4,
$$\|\nabla^2\Omega\|_2^2\ \ge\ c\!\int u-C\!\int u^2-C\sqrt P\,\|u\|_2 .$$

In the template, the right side is ≍ √(kA). With |∇Ω| ~ (k/A)^{1/4} pointwise, this forces |∇²Ω| ~ |∇Ω|. The torsion field a must therefore rotate or oscillate on the unit length scale of the s = −4 normalization; it cannot be a slowly varying mode.

Combined with Step 40's perturbative torsion quotient: if C_AK is bounded along the family, then near a KE host P ≳ ∫|∇J|²/C_AK ≍ √(kA)/C_AK ≫ k. Hence the template can exist only far from every KE host, or along families where C_AK grows like √(A/k).

---

## 2. The weak transport estimate (64.6)–(64.9)

### 2a. The identity

AAD (20) gives s* − s = |∇Ω|² with s* = (2κ+s)/3, so κ − s = 6u. Then −(1/3)d^J(κ−s) = −2d^Ju, and AAD (37) becomes exactly (64.6). ✓
- AAD (26), dρ = *(Jδ Ric″), follows from the contracted Bianchi identity and δΩ = 0, so it holds for every AK structure. ✓

### 2b. Term-by-term integration against a test 1-form η

Assume M is closed, or η ∈ H¹₀(U) for a local version; the metric is smooth. No constraint on s is needed.

1. **⟨δW₃⁺, Ω⟩ is algebraic.** It needs no integration.
   - Since ⟨W₃⁺(X∧Y), Ω⟩ ≡ 0, differentiation gives ⟨(δW₃⁺)_Z, Ω⟩ = ±Σᵢ⟨W₃⁺(eᵢ∧Z), ∇_{eᵢ}Ω⟩. AAD record this as 2W₃⁺(φ)(a) in (52).
   - Contribution: ≤ C‖W₃⁺‖·‖√u η‖, with no ‖∇η‖.
2. **2δρ_*″.** ∫(δρ_*″)(η) = ∫⟨ρ_*″, dη⟩, so the contribution is ≤ C‖ρ_*″‖‖∇η‖.
3. **⟨ρ_*″, ∇_{JZ}Ω⟩.** Algebraic; contribution ≤ 2‖ρ_*″‖‖√u η‖.
4. **⟨(d^∇Ric″)_Z, Ω⟩η^Z.** One integration by parts places the derivative on Ω⊗η. Contribution ≤ C‖Ric″‖(‖∇η‖ + ‖√u η‖).
5. **⟨ι_{JZ}dρ, Ω⟩η^Z.** Insert (26), then integrate δRic″ by parts against a vector field w = w(η, J, Ω) with |∇w| ≤ C(|∇η| + √u|η|). Same bound as item 4.
   - If dρ is integrated directly instead, the ρ₀ part (≤ √(P/2)) and an ∫ds term appear. The latter vanishes for constant s because dΩ = 0.

Every curvature derivative is removed, and (64.7) holds. The refined form is
$$2|\langle d^Ju,\eta\rangle|\le C\Bigl[(\|W_3^+\|+\|\rho_*''\|+\|\mathrm{Ric}''\|)\,\|\sqrt u\,\eta\|+(\|\rho_*''\|+\|\mathrm{Ric}''\|)\,\|\nabla\eta\|\Bigr].$$

Further remarks:
- ‖Ric″‖ ≤ √P gives (64.8). ✓
- ‖d^Ju‖ and ‖du‖ in the dual norm 𝓗_u⁻¹ are equivalent up to constants, because |∇J| = |∇Ω| = 2√u.
- The left side equals ∫u·δ(Jη)-type terms, so constants are annihilated, as stated in the note.

### 2c. Equation (64.9)

At s ≡ −4, (63.3) gives 2‖ρ_*″‖² + 4‖W₃‖² ≤ P + ∫u(4 − 5u)₊. For variable s < 0 the same holds with |s|. ✓

**Quantitative content in the template.**
- The right side of (64.9) is ≍ 4∫u ≍ √(kA).
- An O(1)-relative fluctuation of u on unit scale has ‖du‖²_{H⁻¹} ≲ ‖u − ū‖₂² ≍ k.

Since √(kA) ≫ k, (64.9) excludes nothing at the relevant scale. (64.8) would bind only if W₃ and ρ_*″ were separately small, and Lemma B / estimate (B) show they cannot be small in the diffuse regime.

Hence the AAD Ω-component identity is not a usable transport constraint for the template. Its content is fully absorbed by the large Weyl load that (63.3) already requires.

### 2d. The second identity (64.11)

The transcription matches AAD (38), with (1/6)(d(κ−s)∧Z)″ = (du∧Z)″. ✓

A natural test is the pairing with ξ_Z = ∇_{JZ}Ω, which makes the zeroth-order term (κ/4)·4u ≈ −4u with κ ≈ −4. The other terms integrate against ‖∇ξ‖ + ‖u‖₂, and ‖∇ξ‖ ≈ ‖∇²Ω‖. By Lemma O, ‖∇²Ω‖ is itself ≍ (∫u)^{1/2}. Both sides are then ≍ √(kA), so the inequality balances at leading order.

This is the concrete form of the Step-43 derivative loss in the diffuse regime. A gap from (64.11) needs an upper bound on ‖∇²Ω‖ that is strictly better than its Bochner value, by a factor → 0 as k/A → 0.

---

## 3. Shrinking Nijenhuis zeros

**Topology.** ∇Ω is a section of ⟦Λ^{0,1}⊗Λ^{0,2}⟧ ≅ T^{1,0}⊗K⁻¹, with
c₂ = c₂ + 2c₁² = 5χ + 6τ = c₂(X) + 2A − k.
The computation uses τ(X) = (A − 2c₂(X))/3. ✓

So constant u > 0 is excluded throughout the open range (Armstrong–LeBrun, AAD Lemma 2).

**Count versus k.** The signed number of Nijenhuis zeros is c₂(X) + 2A − k, which is of host order, ≥ 7A/3 − k for ball quotients. It is not attached to the exceptional classes. Pricing these cores therefore cannot by itself produce a per-class tariff.

**Scaling (64.10 discussion).** The computation ‖u − u₀‖₂² = O(u₀²ε⁴) per core, and ‖du‖_{H⁻¹} ≤ 2‖u − u₀‖₂ = O(u₀ε²), is correct.

The dimensional count can be made concrete inside AK geometry, which strengthens the note:
- Fix ω. Compatible J are arbitrary sections of the Siegel-disc bundle.
- Altering J on B_{2ε} so that |a| drops from √u₀ to a nondegenerate zero costs δJ = O(√u₀ ε), ∇δJ = O(√u₀) and ∇²δJ = O(√u₀/ε).
- The change in curvature of g_J = ω(·, J·) is then O(√u₀/ε + u₀), so ∫|δRm|² = O(u₀ε²) + O(|Rm|²ε⁴).
- The cross term with the background Ric° is O(|Ric°| ε² · √u₀ ε).

Hence a degree-one core costs vanishing L² curvature as ε → 0. The c₂-count is paid globally by Chern–Weil curvature through Mathai–Quillen transgression, not locally.

Two points are not covered by this argument:
- the effect of the Yamabe renormalization to s ≡ −4 is not controlled;
- this is a local implant estimate, not a construction of the template.

**The §4 conditional theorem does not price the cores.** The core radius is not a curvature scale: |Rm| in the core is ~ √u₀/ε, far below ε⁻².
- Suppose bounded curvature and a harmonic-radius lower bound are given. Elliptic regularity for the harmonic form Ω then bounds ∇²Ω, which forces ε ≳ √u₀/Λ.
- The core contribution to second-jet energy is then ≍ N·u₀ε² ≳ N u₀²/Λ². With u₀ ≈ 2√(k/A) and N ≈ c₂(X) + 2A, this is of order k/Λ².
- That is subleading to the bulk load ∫u ≍ √(kA) from (B), and it is Weyl/second-jet energy, not P.

So noncollapse at the cores does not yield an L² price of order k on P. The statement "AAD identities and local trace estimates can price the finitely many cores" is unsupported.

---

## 4. Proposition 64.H

**Hopf formulas.**
- With z₁ = x₁ + ix₂ and z₂ = x₃ + ix₄, (64.12) is (2z₁z̄₂, |z₁|² − |z₂|²)/r². ✓
- The Hopf map S³(1) → S²(1) has horizontal singular values 2, 2, and n is homogeneous of degree 0. Hence |∇n|² = 8/r² and |n*ω_{S²}|² = 16/r⁴. ✓

**Twist density.** With Ω = Σnᵢωᵢ (|ωᵢ|² = 2) and φ, Jφ built from an oriented tangent frame f₁, f₂ of S²:
- α = ⟨dn, f₁⟩, β = ⟨dn, f₂⟩, and α∧β = n*ω_{S²};
- the decomposable split gives |(α∧β)⁻|² = 8/r⁴. ✓

This **saturates** the 63.T algebraic bound |(α∧β)⁻| ≤ |∇Ω|²/(4√2), since |∇Ω|² = 16/r², |α| = |β| and α ⊥ β.

**Logarithmic coefficients.** Using |S³| = 2π²:
- ∫|∇n|⁴ = 64·2π² log(R/ε) = 128π² log(R/ε); ✓
- ∫|(α∧β)⁻|² = 16π² log(R/ε). ✓
- The weighted bounds (64.16) are ✓.

**Corrected statement for the model zero.** Let Φ ∈ C² (true for SW solutions) with Φ(p) = 0 and invertible linear part L.
- Write n_L = Hopf∘(Lx/|Lx|). Then n = n_L + O(r) and ∇n = ∇n_L + O(1).
- The corrections are integrable, so the log coefficient is c(L) = ∫_{S³}|(n_L*ω)⁻|² > 0. Positivity holds because n_L|_{S³} is a submersion, so n_L*ω ≠ 0 and its ASD part has half its norm.
- c(L) = 16π² exactly when L is conformal. In general it depends on the conformal distortion of L.
- The Hopf invariant of the linking map is sign(det L) = ±1. Since H(f∘g) = deg(g)H(f), the map is never trivial.

### 4a. What this does and does not obstruct

- **The zero count is zero.** For the best-sign class, a² = c₁²(M) = 2χ + 3τ, so the signed zero count of Φ is c₂(W⁺) = (a² − 2χ − 3τ)/4 = 0.
  - Zeros pair into ± Hopf charges.
  - Replacing n on a ball of radius ~2d around a pair at separation d by any extension of the (homotopically trivial) dipole data gives a smooth J with c₁(J) = a.
  - The repair costs a scale-invariant amount per pair. Its constant depends on the leading linear parts and on d relative to the C² scale; it is not proved uniform.
  - So the obstruction is "unbounded twist plus a repair cost per zero pair", not "no smooth J can be extracted".
- **The zero-free case.** If ρ ≥ ρ₀ > 0 everywhere, as in a shallow-band near-minimizer with no zeros, the Bloch field is a smooth global J with c₁ = a, and 63.T applies directly.
- **The obstruction that persists without zeros is an integrability gap.**
  - t⁻ is quadratic in ∇n, so 𝒯_J ≤ C‖∇n‖²_{L⁴}.
  - Theorem N controls only ∫ρ²|∇n|²_{W₂}, a weighted L² quantity.
  - In the template, ∫|∇n|² ≍ √(kA) while ∫|∇n|⁴ ≍ k, and Theorem N needs only ∫ρ²|∇n|²_{W₂} ≥ 16π²(1−c)k. Diffuse rotation therefore satisfies both Theorem N and 63.T simultaneously.

So the SW route requires an L²→L⁴ upgrade for ∇n, plus zero-pair accounting. The zero singularity is the secondary of these two issues.

---

## 5. Corrected statements

1. **63.T consequences (any g, J).**
   - ‖𝖧⁻(t_J⁻) − 2πh_a⁻‖ ≤ √(P/2).
   - ‖t_J⁻‖ ≥ 2π√(k+Π) − √(P/2).
   - ∫|∇Ω|⁴ ≥ 32(2π√(k+Π) − √(P/2))₊².
   - AK case: ½∫u² ≥ (2π√(k+Π) − √(P/2))₊², hence u_rms² ≥ 8π²(k+Π)/V(1 − o(1)) when P = o(k), with V ∈ [2π²(A+Π), 6π²A].
2. **Lemma B (AK, s ≡ −4).** ∫u = 2V + 2πa·[Ω] = volume excess + H⁺-misalignment; both are ≥ 0.
3. **Lemma O (AK, s ≡ −4, closed).** Estimate (B) holds, and ‖∇²Ω‖₂² ≥ c∫u − C∫u² − C√P‖u‖₂.
4. **Weak transport (AK, closed or η ∈ H¹₀, any s).** The refined form of (64.7) in §2b. The W₃ term is algebraic, and every curvature derivative is removed. It is vacuous at the template scale.
5. **Core implant (fixed ω).** A nondegenerate Nijenhuis zero of radius ε with outer amplitude √u₀ is implantable with ∫|δRm|² = O(u₀ε² + ε⁴). The Yamabe step is not covered.
6. **Proposition 64.H (C² spinor, invertible L).**
   - Twist and L⁴ rotation diverge like c(L)log(R/ε), with c(L) = 16π² and 128π² respectively in the conformal case.
   - The linking class is the Hopf class ±1.
   - Zeros cancel in pairs for the best-sign class, so a smooth J with c₁ = a exists after repairing each pair.

---

## 6. What this means for the open range

1. **The diffuse template is sharper and more constrained than stated.** A cheap state (P = o(k)) of AK type with diffuse u requires all of the following:
   - ū ≈ 2√(k/A);
   - ∫u ≍ √(kA) supplied by volume excess or period misalignment (Lemma B);
   - Weyl energy ‖W₂‖² + ‖W₃‖² ≍ √(kA) (estimate B);
   - torsion oscillating at unit scale (Lemma O);
   - distance from any KE host, if Step 40's C_AK is uniform.

   This is the object a construction must realize. It is not near-Kähler in its W⁺ components, and it is not slowly varying.
2. **Neither AAD identity closes the problem by Cauchy–Schwarz.**
   - The Ω-component (64.6) is dominated by the Weyl load.
   - The ⟦Λ^{0,2}⟧-component (64.11) balances at leading order.
   - A lower bound must show that ‖∇²Ω‖ (equivalently ‖W₂‖ + ‖W₃‖) is strictly smaller than (∫u)^{1/2} when P = o(k), or that the volume-excess/misalignment in Lemma B itself costs P at rate ≳ ∫u. The latter is a concrete, untested route: the closed identity P = 4∫|W⁺|² + 4V/3 − 8π²(A−k) charges volume at 4/3 per unit.
3. **Cores are a host-scale phenomenon.**
   - Their number is c₂(X) + 2A − k.
   - Their L² cost can be made arbitrarily small.
   - Under bounded geometry their second-jet cost is O(k), and it is Weyl energy rather than P.
   - No per-class tariff can come from Nijenhuis zeros alone.
4. **For the SW-selected J, the missing input is an L⁴ estimate on ∇n.** Zero-pair repair is secondary. Without that estimate, Theorem N and 63.T are jointly consistent with the diffuse template.

**Unresolved and needed.**
- Either a construction of the template, a Lemma B/O-compatible AK texture with Yamabe-normalized P = o(k);
- or an inequality bounding ‖∇²Ω‖₂² or the Lemma-B slack by o(∫u) + O(P).

Only one of these two would decide between the zero-tariff scenario and a positive per-class law.