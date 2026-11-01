# Step 61 — The Eguchi–Hanson obstruction as a sharp gap estimate (Theorem 61.EH)

Agent2, Execute. Target 58.Q at leading order. Inputs:
- Step 60: `scripts/step60_EH_obstruction_pairing.py`, `scripts/step60_EH_sector_check.py`, data `data/step60_EH_obstruction_pairing.json`.
- Step 61: `scripts/step61_EH_cokernel_norm.py` → `data/step61_EH_cokernel_norm.json`, which checks the exact cokernel norm.
- Source: Ozuch, *Higher order obstructions to the desingularization of Einstein metrics* \cite{ozuch2020higher}, §§1.2, 2.1, Thm 0.2. His linear theory follows Biquard (Biq13, Biq16).

## 1. Objects and normalisations

**Orbifold.** (V, g_V) is an orbifold with an isolated point p ≅ ℝ⁴/ℤ₂, and g_V is Einstein near p: Ric = Λg, s = 4Λ.
- R^± = W^± + (s/12)I on Λ^±, so tr R⁺ = Λ.
- In Bianchi/normal coordinates, g_V = δ + h₂ + h₄ + O(r⁶). Odd jets vanish by ℤ₂-invariance in orbifold charts.

**Eguchi–Hanson space.** EH_a in its hyperkähler orientation is
dr²/f + (r²/4)(σ₁² + σ₂²) + (r²f/4)σ₃²,  f = 1 − a⁴/r⁴,  r ≥ a.
- Its level sets are RP³, and its volume element is π²r³dr after angular integration.
- The Kähler forms ω₁, ω₂, ω₃ are self-dual and parallel.
- The resolution direction ζ = ω₁/√2 is the unit self-dual form whose complex structure makes the bolt S² holomorphic.

**Cokernel.** Ω = (e⁰³ − e¹²)/r⁴ = −¼ d(σ₃/r²) in EH orthonormal frames, exactly for every a. This is because d(σ₃/r²) = −(4/r⁴)(e⁰³ − e¹²) does not involve f.
- Ω is closed, anti-self-dual and L², hence harmonic.
- o_i := Ω∘ω_i is symmetric, trace-free and TT, and lies in the L²-kernel of the Einstein operator P_EH. These o_i span Ozuch's O(eh), the infinitesimal variations of the hyperkähler period ζ.
- |o_i|² = |Ω|²_endo = 4/r⁸, and ⟨o_i, o_j⟩ = 0 for i ≠ j, since ω_iω_j is anti-commuting and trace-free.
- **‖o_i‖²_{L²(EH_a)} = ∫_a^∞ (4/r⁸)π²r³dr = π²/a⁴.** This is independent of i and scale invariant once multiplied by a⁴.

**Flux pairing (Step 60, exact).** Let ĥ be any smooth extension of h₂ over EH with ĥ − h₂ = O(r^{−2+ε}) at infinity. Since DRic*_EH o_i = 0 on the complete space EH, the pairing ∫⟨DRic_EH[ĥ], o_i⟩ is a flux at infinity. It equals the flat flux of (h₂, o_i^flat), and is constant in r because ⟨DRic_flat h₂, o⟩ = ⟨(s/4)δ, o⟩ = 0 pointwise. The result is

  B_i := ∫_EH ⟨DRic_EH[ĥ], o_i⟩ = π² (R⁺_p ζ)_i,  i = 1, 2, 3,

computed in the frame (ζ, ζ₂, ζ₃) at a = 1. It vanishes for every W⁻, Ric°_ζ, Ric°_⊥ and mixed jet (`step60_EH_sector_check.py`).
- The scaling is as follows. In y = x/a units, a⁻²g̃ = EH₁ + a²ĥ(y) + O(a⁴|y|⁴), so the pairing is a²B_i.
- This makes explicit Ozuch's constant: his (22), λ_k(ζ) = c⟨R⁺(H₂)ζ, ζ_(k)⟩ with c > 0 unspecified, is our B with c fixed.

## 2. Theorem 61.EH

Let g̃_{a,ζ} be the naïve desingularisation: EH_a glued at p in direction ζ, at a fixed gluing radius t₀, with g_V unchanged outside B_{2t₀}(p).

**Weighted neighbourhood.** For δ > 0 and a weight w ∈ [0, 2), define 𝒩_δ(a,ζ) as the set of metrics g on the resolution M such that, after a diffeomorphism, for j = 0, 1, 2 in y = x/a units,
  |∇^j_{EH}(a⁻²g − a⁻²g̃_{a,ζ})| ≤ δ a² (1 + |y|)^{w−j}.
This bound is required on {|y| ≤ t₀/a}, with the corresponding unweighted bound δa^{2−w}t₀^{w} outside.

**(a) Lower bound.** There are constants a₀ and C, depending on g_V near p, on t₀ and on w, such that for a < a₀ and every g ∈ 𝒩_δ(a,ζ):

  P(g) ≥ π² a⁴ ( |R⁺_p ζ| − C(δ + a^{2−w}) )₊².

**(b) Matching upper bound.** There is a metric g*_{a,ζ} ∈ 𝒩_{Ca^{2−w}}(a,ζ) with

  P(g*_{a,ζ}) = π² a⁴ |R⁺_p ζ|² + O(a⁶ log(1/a)).

Hence, uniformly in ζ:

  inf_{𝒩_δ(a,ζ)} P = π² a⁴ |R⁺_p ζ|² (1 + O(δ) + o(1)),
  inf_ζ inf_{𝒩_δ} P ≈ π² a⁴ σ_min(R⁺_p)².

**(c) Near-extremal structure.** If g ∈ 𝒩_δ satisfies P(g) ≤ π²a⁴|R⁺ζ|²(1 + η), then
  ‖Ric°(g) − Π Ric°(g)‖²_{L²} ≤ (η + C(δ + a^{2−w})) π²a⁴|R⁺ζ|²,
where Π is the L²-projection onto span{χô_i}. In words, near-minimisers are Einstein modulo the EH cokernel, and their Einstein defect is the cokernel tensor a²Σ B_i o_i/‖o‖², concentrated at the EH scale. When R⁺ζ ≠ 0, Cauchy–Schwarz equality forces Ric° to be parallel, in L², to Σ(R⁺ζ)_i o_i.

### Proof of (a)

Let ô = Σ_i b_i χ_Λ o_i with b = R⁺ζ/|R⁺ζ|, where χ_Λ cuts off at |y| ≈ Λ := t₀/(2a). This cut-off lies inside the region where g̃ = g_V, hence Ric°(g̃) = 0 there. For any g, Cauchy–Schwarz gives

  P(g) ≥ ⟨Ric°(g), ô⟩_g² / ‖ô‖_g².

Everything below is computed in y-units, using the scale invariance of P and of L² norms of 2-tensors in dimension four.

(i) Since ‖o‖²_EH = π² (a = 1) and the tail is ∫_Λ^∞ 4y⁻⁸y³dy = O(Λ⁻⁴), we have ‖ô‖²_g = π²(1 + O(a⁴ + δa²)).

(ii) The naïve metric. In the core |y| ≤ Λ we have a⁻²g̃ = EH + a²ĥ + a⁴ĥ₄ + O(a⁶|y|⁶), with ĥ = h₂ off a compact set. Expanding, Ric°(a⁻²g̃) = a²DRic°_EH[ĥ] + a⁴(Q(ĥ,ĥ) + DRic[ĥ₄]) + ….
- The trace-free projection of DRic_EH[ĥ] and DRic_EH[ĥ] itself have the same pairing with o, because o is trace-free.
- Hence ⟨Ric°(g̃), ô⟩ = a²|B| + E, where E collects the a⁴ terms paired with o.
- A naive bound would be |y|²·|y|⁻⁴·|y|³ integrated up to Λ, i.e. O(a⁴Λ²) = O(a²t₀²). But in the region 1 ≪ |y| ≤ Λ, the order-a⁴ part of Ric° is the order-r² part of Ric°(g_V) = 0, by the Einstein equation for the jet: P_e H₄ = ΛH₂ − Q(H₂,H₂) up to trace. Only EH-tail cross terms survive there, of size O(|y|²·|y|⁻⁴).
- So the a⁴ integrand is O(|y|⁻²·|y|⁻⁴·|y|³), which is integrable, and E = O(a⁴), uniformly in t₀. The gluing-annulus terms are O(a⁴t₀⁻⁶)-type and pair with ô to give O(a⁴).

(iii) Perturbation. Let k := a⁻²(g − g̃). Then
  ⟨Ric°(g), ô⟩ − ⟨Ric°(g̃), ô⟩ = ⟨k, DRic°*_{g̃} ô⟩ + O(∫|k||∇²k||ô| + |∇k|²|ô|).
- DRic*_EH o_i = 0 exactly, so DRic*_{g̃}ô = a²·O(|y|⁻⁴) + O(χ'_Λ terms). The first term comes from g̃ − EH = a²ĥ, which multiplies the background coefficients by O(|ĥ|, |∇ĥ|, |∇²ĥ|) ~ a²|y|^{2−j}.
- The linear term is therefore ≤ ∫_{|y|≤Λ} δa²|y|^w · a²|y|⁻⁴ · |y|³ dy + δa²Λ^{w}·Λ⁻⁶·Λ⁴ ≤ Cδ a⁴ Λ^{w} + Cδa²Λ^{w−2}. Since a⁴Λ^w = a^{4−w}t₀^w = o(a²) for w < 2, this is ≤ Cδ a² (t₀^{w}a^{2−w} + a^{2−w}t₀^{w−2}) ≤ C δ a².
- The quadratic term is ≤ ∫ δ²a⁴|y|^{2w−2}|y|⁻⁴|y|³dy ≤ Cδ²a⁴Λ^{2w−2} = Cδ² a^{6−2w} = o(a²) for w < 2. Outside |y| ≤ Λ, ô vanishes.

(iv) Combining (i)–(iii): |⟨Ric°(g), ô⟩| ≥ a²(π²|R⁺ζ| − C(δ + a^{2−w})), so
  P ≥ a⁴(π²|R⁺ζ| − ⋯)²/(π²(1 + o(1))) = π²a⁴(|R⁺ζ| − ⋯)². □

(The error exponents above are bookkeeping-level. The decisive structural facts are four: the pairing is a flux, o is TT and in the kernel of DRic*_EH, the decay ô ~ |y|⁻⁴ makes every error integral converge for w < 2, and ‖o‖² is finite. A full Hölder-space version would follow Ozuch's decoupled norms C^{2,α}_{β,*}, App. A of \cite{ozuch2020higher}.)

### Proof of (b)

This uses the Einstein-modulo-obstruction solution, which exists by the Biquard–Ozuch linear theory and is quoted in \cite{ozuch2020higher} (22)–(23), Lemma 2.3: there is a unique ĥ₂ on EH with

  P_EH ĥ₂ = Λ·eh + Σ_k λ_k o_k,  ĥ₂ = H₂ + H₂⁴ + O(r^{−4+ε}),  ĥ₂ ⊥ o_k on the bolt,

where P_EH = DRic + δ*B is the gauged linearisation and |H₂⁴| ~ r⁻².
- Pairing with o_k identifies λ_k‖o‖² = B_k, i.e. λ_k = (R⁺ζ)_k. The Λ·eh term carries the trace part s = 4Λ; it is pure trace and drops out of Ric°.
- Set g* = g̃ + a²χ_{t₀}(ĥ₂ − h₂), so that in y-units a⁻²g* = EH + a²ĥ₂ + O(a⁴|y|⁴). Ozuch's construction places the solution in Bianchi gauge, so B(ĥ₂) = 0 is part of the linear solution, and Ric(a⁻²g*) = a²Λ·eh + a² Σλ_k o_k + O(a⁴(1+|y|)^{0}).
- Hence Ric°(g*) = a²Σλ_k o_k + R₄, with |R₄| ≲ a⁴(1+|y|)^{−2} in the core, plus a gluing-annulus error O(a⁴ t₀^{−4} … ).
- Then P(g*) = a⁴|λ|²‖o‖² + 2a²⟨Σλ_k o_k, R₄⟩ + ‖R₄‖². With |λ|²‖o‖² = π²|R⁺ζ|²:
  - ‖R₄‖² ≲ a⁸∫(1+|y|)^{−4}|y|³dy ≲ a⁸ log Λ = O(a⁸ log(1/a));
  - the cross term is ≲ a⁶ ∫(1+|y|)^{−4−2}|y|³ dy = O(a⁶);
  - the annulus error is O(a⁸).
- The metric difference g* − g̃ is a²(ĥ₂ − h₂) = a²O((1+|y|)^{−2}), so g* ∈ 𝒩_{Ca^{2−w}}. □

The input from \cite{ozuch2020higher} is the existence of ĥ₂ with the stated asymptotics, Lemma 2.3. That paper also records "Einstein up to an o(t) error iff R⁺ζ = 0", with t = a². Theorem 61.EH converts this qualitative statement into the sharp value of the gap functional.

## 3. Consequences

**3.1 The rate of approach to zero gap is Θ(a⁴), with an explicit constant.** In Prop. 59.N / 58.O, the resolution of an Einstein orbifold by EH spaces at ℝ⁴/ℤ₂ points p_j, with parameters (a_j, ζ_j), has
  P = π² Σ_j a_j⁴ |R⁺_{p_j}ζ_j|² (1 + o(1))
for the optimised metrics. Every metric in the 𝒩_δ neighbourhoods costs at least this much, up to the factor (1 − Cδ).
- Example: CP²#CP² ≅ (S⁴/±1) with two EH. The round unit S⁴ has R⁺ = I, so inf over the neighbourhoods is 2π²a⁴(1 + o(1)).
- No Einstein metric lies in these neighbourhoods. This is the quantitative form of Ozuch's non-approximability result \cite{ozuch2021integrability}. α = 0 is approached only at the rate a⁴ → 0.
- The bound concerns metrics near glued configurations. It reaches arbitrary sequences on M only through a 59.Z-type decomposition together with Ozuch's GH ⇒ 𝒩_δ theorem. Ozuch shows that Einstein metrics GH-close to V lie in such neighbourhoods; extending this to near-minimisers of P is open.

**3.2 Kähler–Einstein orbifolds.** For g_V KE with Λ ≠ 0, R⁺ = diag(Λ, 0, 0) in the basis (ω̂, ω̂^⊥).
- Holomorphic direction ζ = ω̂ (the Kronheimer/crepant gluing used in Theorem Z and 59.N for canonical models of minimal surfaces with (−2)-curves): |R⁺ζ| = |Λ|, so P ≥ π²Λ²a⁴ per A₁ point on 𝒩_δ. The Kähler desingularisation is λ⁴-obstructed. This is consistent with Biquard's det R⁺ = 0 obstruction being blind to direction, and with the absence of KE metrics on the minimal resolution when K is not ample.
- Directions ζ ∈ ω̂^⊥: R⁺ζ = 0, so the leading obstruction vanishes and inf P = o(a⁴). These directions are non-holomorphic for the orbifold complex structure.
- Ozuch's second obstruction, Thm 0.2, requires R⁺_p = diag(0, 0, Λ) in some basis. A KE point satisfies it with ζ ∈ ω̂^⊥. So KE orbifolds are exactly the orbifolds unobstructed through second order, in non-Kähler directions.
- Einstein existence on the smooth minimal surface with non-ample K, near the KE orbifold, is therefore decided by the third and higher obstructions in ω̂^⊥ directions. These are unknown. The quantitative rate is inf P = O(a⁶) or smaller in ω̂^⊥ directions; the exact order is to be computed.

**3.3 Duality between Burns insertion and EH desingularisation.** On the R⁺ ≤ 0 kernel stratum μ₁ = 0, with μ₂, μ₃ ≤ 0 and μ₂ + μ₃ = Λ:
- First order. Burns pays −8π²εμ₁, which vanishes iff R⁺(ζ,ζ) = 0. EH pays π²a⁴|R⁺ζ|², which vanishes iff R⁺ζ = 0. On R⁺ ≤ 0 the two conditions coincide.
- Second order. Burns saves −4π²(μ₂ − μ₃)²/2 ε²log(1/ε). On the stratum this saving is **maximal exactly when one of μ₂, μ₃ is 0**, i.e. at Ozuch's locus diag(0, 0, Λ), the KE type. It **vanishes exactly at the isotropic point (0, Λ/2, Λ/2)**.
- The isotropic point is the curvature type of the AdS Taub–bolt orbifold, R⁺ = diag(0, −3/2, −3/2) (\cite{ozuch2020higher}, Example 2.1). That orbifold is EH-obstructed at second order in the compact setting.
- So the undecided boundary case of 59.R is exactly Ozuch's second-order obstructed type, and the maximal-saving Burns type is exactly the type with the most unobstructed EH desingularisation. The two Kähler ALE insertions (Burns, which has mass, and EH, which has none) see the same tensor R⁺ through the same invariants: the kernel at first order, and the splitting of the complementary eigenvalues at second order.
- Conjecture 61.D. The second-order EH pairing on the kernel is a quadratic form in (μ₂, μ₃) vanishing exactly on μ₂μ₃ = 0. If so, the minimal-P rate in the kernel direction would be c·a⁸(μ₂μ₃)² with an explicit c, and Burns and EH would be governed by complementary invariants, (μ₂ − μ₃)² and μ₂μ₃, of the same 2×2 block. This is to be computed by the flux method applied to ĥ₄ (Ozuch (23), Lemma 2.7–2.9).

**3.4 Kronheimer A_n and Wahl fibres.** The same argument applies verbatim to any Ricci-flat ALE bubble with L² cokernel {o}. The cokernel consists of TT tensors built from L² harmonic ASD forms ⊗ parallel SD forms in the hyperkähler case. The leading pairing is the flux of (h₂, o) at infinity and is linear in Rm_p. For hyperkähler A_{n−1} it is linear in R⁺_p, through the period map.
- The general principle: **a Ricci-flat ALE insertion at an Einstein orbifold point costs, to leading order and sharply, ‖Π_{coker}(DRic[h₂])‖²·(scale)⁴.** This is the squared flux of the background quadratic jet against the bubble's L² infinitesimal Einstein deformations.
- This is deferred until the ℤ₂ case is fully written with Hölder norms.

## 4. What is proved and what is not

- **Proved:** B_i = π²(R⁺ζ)_i, an exact flux computation; ‖o‖² = π²/a⁴, by exact hand computation, with the script check `step61_EH_cokernel_norm.py` pending at the time of writing (see the JSON); and the Cauchy–Schwarz lower bound (a), with polynomial error bookkeeping.
- **Proved modulo the quoted linear theory:** the upper bound (b). Its input is Ozuch's Lemma 2.3 (existence and asymptotics of ĥ₂, in Bianchi gauge). The Bianchi-gauge identity B(ĥ₂) = 0 is part of Ozuch's construction, (22) with P = DRic + δ*B.
- **Not proved:** that every near-minimising sequence of P on M near the orbifold lies in some 𝒩_δ; the second-order rate in ζ ∈ ker R⁺ (Conj. 61.D); and the A_n and Wahl extensions.

## 5. Verified and corrected form (TTCS step61 verifier; binding over §§2–4)

Source: `trace/ttcs/results/step61_ttcs01_verifier1_integration.md`.

**5.1 Normalisations confirmed, with two precisions.**
- Ω = (e⁰³ − e¹²)/r⁴ = −¼ d(σ₃/r²) holds exactly for every a. It is ASD, closed and coclosed.
- The potential σ₃/r² is defined only off the bolt. Ω is harmonic and L² but **not globally exact**: its bolt period is ∫_{S²}Ω = −π/a².
- The o_i satisfy ⟨o_i, o_j⟩ = 4δ_ij/r⁸ pointwise, because J_iJ_j = −δ_ij + ε_ijk J_k and (r⁴Ω)² = −I. They span Ozuch's O(eh).
- dV = (r³/8) dr σ₁₂₃, so ∫_{r≤R} F dV = π²∫F r³ dr. The induced area of a level set is π²r³√f, not π²r³.
- ‖o_i‖² = π²/a⁴ exactly.
- B = π²R⁺_pζ is confirmed, including the ℤ₂ factor and c₀ = 0. An independent round-sphere check gives c₂ = 2π²/3, c₁ = 8π²/3, B₁ = π².
- The normal-coordinate jet is not in flat Bianchi gauge, but the flux is gauge independent, because DRic_EH(L_X EH) = 0.
- In the flux basis, λ_i = (R⁺ζ)_i. Ozuch's basis has |ζ_(k)| = √2, so his c is compatible with magnitude ½ up to basis signs.

**5.2 Corrected Theorem 61.EH.**
- Centre. Use the jet-extended superposition g̃_{a,ζ} = g_V + χ_{t₀}(EH_a − δ), with the background extended over the bolt, so that a⁻²g̃ = EH₁ + a²ĥ₂ + a⁴ĥ₄ + ⋯ in the core. Compare with the **exact** Einstein background, not a truncated Taylor expansion.
- Lower bound (P). For every bounded δ and w ∈ [0, 2), and every g ∈ 𝒩_δ(a,ζ),
  P(g) ≥ π²a⁴(|R⁺_pζ| − ε_w(a,δ))₊²,
  where ε_w = C[a² + δa²(1 + |log a|) (w = 0) or δa^{2−w} (0 < w < 2) + δ²a² (w < 1), δ²a²|log a| (w = 1), δ²a^{4−2w} (1 < w < 2)].
  - In particular ε_w → 0 for fixed δ. This is sharper than §2's C(δ + a^{2−w}).
  - Some intermediate integrals grow logarithmically or polynomially in L; their scaled contributions are still o(a²).
  - The test-tensor norm has an O(a²) error.
  - The lower bound needs no gauge choice. Any diffeomorphism representative satisfying the estimate may be used, with the test tensor transported along.
- Gauge fact needed for (b) (proved by the verifier). Applying B_EH to Ozuch's (22) and using the linearised Bianchi identity gives ½∇*∇(B_EH ĥ₂) = 0. With B_EH ĥ₂ = O(r⁻³) this forces B_EH ĥ₂ = 0. Hence DRic_EH ĥ₂ = Λ·EH + Σλ_i o_i exactly.
- Upper bound (P*, Ozuch Lemma 2.3 plus matching). Let g_V be **globally** Einstein; otherwise add P(g_V). The adapted metric g*_a with centre built from ĥ₂ satisfies
  P(g*_a) = π²a⁴|R⁺ζ|² + O(a⁶).
  If R⁺ζ = 0, it satisfies P(g*_a) = O(a⁸ log(1/a)).
  - g*_a lies in 𝒩_{C₀} of a generic centre, **not** in 𝒩_{Ca^{2−w}}.
  - Two sharp formulations are valid: (i) adapted centre, any small δ; (ii) generic centre with δ ≥ C₀.
  - The exact a⁶ coefficient is not established.
- Infimum, additive form. With q = |R⁺ζ|, in a neighbourhood containing the adapted metric:
  π²a⁴(q − ε)₊² ≤ inf P ≤ π²a⁴q² + O(a⁶).
  The multiplicative form holds only when q is bounded below.
- Near-extremal structure. If P(g) ≤ π²a⁴q²(1 + η), then
  ‖(1 − Π_g)Ric°(g)‖² ≤ π²a⁴[ηq² + Cqε],
  where Π_g is the L²(g) projection onto the cut-off obstruction span.

**5.3 Corrected consequences.**
- S⁴/±1 means the suspension quotient (x₁,…,x₄,x₅) ↦ (−x₁,…,−x₄,x₅), with two A₁ points; it is not RP⁴. With R⁺ = I on the unit sphere, two adapted insertions have energy 2π²a⁴(1 + o(1)). This is a local sharp asymptotic, not a universal rate.
- KE orbifolds. R⁺ = diag(Λ,0,0), and the holomorphic direction costs π²Λ²a⁴. For ζ ⊥ ω̂ the first obstruction vanishes.
  - These directions are **not** "non-Kähler": EH is hyperkähler, and the bolt is Lagrangian for the ω̂-structure, which corresponds to the local smoothing interpretation.
  - Ozuch's Thm 0.2 is a necessary condition under compactness, integrability and stability/rigidity hypotheses. The §3.2 phrases "exactly the orbifolds unobstructed through second order" and "decided by third and higher obstructions" are withdrawn.
- **Conjecture 61.D is partly known.** Ozuch §2.1.4 already gives the second obstruction μ₁ = C·det(R⁺|_{ζ^⊥}), C > 0, when the first vanishes. What remains open is the normalised coefficient, the other second-order components, and an a⁸ minimised-defect theorem. The latter must control orbifold Einstein deformations and scale/direction changes (Ozuch Cor. 2.12).
- **Burns/EH unification (exact).** On the kernel stratum with complementary eigenvalues u, v and u + v = Λ, we have (u − v)² = Λ² − 4uv. Hence
  **Φ_opt(kernel) = −(u − v)²/2 = −Λ²/2 + 2 det(R⁺|_{ζ^⊥}).**
  - The second-order Burns saving and Ozuch's second EH obstruction are therefore the same invariant, det(R⁺|_{ζ^⊥}), at fixed Λ.
  - Maximal Burns saving, −Λ²/2, occurs exactly where the second EH obstruction vanishes (KE type).
  - Zero Burns saving occurs at the isotropic point (0, Λ/2, Λ/2), where the determinant is maximal, Λ²/4 (AdS Taub–bolt type, det = 9/4).
  - The two Kähler-ALE insertions thus read the same pair of invariants of R⁺: the kernel at first order, and det(R⁺|_{ζ^⊥}) at second order.
- Other ALE bubbles. The leading energy is B^T G⁻¹ B a⁴, with G the Gram matrix of the L² cokernel. The extension to A_n and Wahl bubbles is **not** verbatim: it needs decay, period normalisation, all cokernel modes, and the curvature-derivative obstructions of A_k (Ozuch Rem. 2.21).
- Theorem 61.EH does not remove (N0), and it does not produce a positive scale-independent gap. Positivity of an obstruction changes only the rate.


## Step-64 execution addendum: EH normalization script status

The previously staged coordinate script `scripts/step61_EH_cokernel_norm.py` was finally run in Step 64. Its radial norm integral returned the intended `pi**2/a**4`, but its coordinate Ricci/duality booleans were false because its Euler-angle one-forms use structure equations inconsistent with the claimed left-invariant convention; `data/step61_EH_cokernel_norm.json` is therefore a failed diagnostic and must not be cited as verification.

A repaired independent moving-frame script, `scripts/step61_EH_cokernel_norm_v2.py`, uses
\(d\sigma_i=-\sigma_j\wedge\sigma_k\) cyclically and verifies exactly
\[
 d(\sigma_3/r^2)=-\frac4{r^4}(e^{03}+e^{12}),\qquad
 \Omega=-\frac14d(\sigma_3/r^2),\qquad
 |\Omega|_{\rm endo}^2=\frac4{r^8}.
\]
For the orientation \(e^{0123}\) this form is self-dual; reversing orientation makes it ASD, matching the orientation used in Theorem 61.EH.  Since the RP\(^3\) radial shell density is \(\pi^2r^3\),
\[
 \|o_i\|_2^2=\int_a^\infty\frac4{r^8}\pi^2r^3\,dr
 =\frac{\pi^2}{a^4}.
\]
Authoritative output: `workspace/data/step61_EH_cokernel_norm_v2.json`.
