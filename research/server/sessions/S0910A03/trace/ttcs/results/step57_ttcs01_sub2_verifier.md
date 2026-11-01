# TTCS Independent Branch Record

```json
{
  "step_id": 57,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md",
    "Sessions/S0910A01/workspace/notes/step25_tensor_energy_derivation.md",
    "Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md"
  ]
}
```

## Task

Verify the H₂ evolution derivation in §§2-7 of this note for the exact normalized cutoff flow ∂_tg = -2χ²(Ric+g) using the shifted curvature T = Rm + g∧g/(2(n-1)). The main claims to check:

1. The identity |∇T|² = |∇Rm|² because ∇G = 0 (G is built from the metric). Does this hold exactly, including under the evolving metric g(t)? The covariant derivative ∇ = ∇_{g(t)} is time-dependent; is ∇_{g(t)}G(g(t)) still zero?

2. The Bochner pair integration §3: the cross term 2ηa(∇η)·∇|T|² vanishes because a = 0 on supp(∇η). The extra shifted-curvature term ∫η²a⟨ΔRm, G⟩ reduces by IBP to εD₂ + C/(εr²)·Vol using ∇G = 0 and the buffer collar. Check the IBP steps explicitly.

3. The Type (C) Hessian-of-a term §5: after one IBP, ∫η²(∇²a)·𝒯 = -∫η²(∇a)·∇𝒯 with the cross term killed by a∇η = 0. Then Young gives ε''D₂ + C/(ε''r²)H₂. Is this correct for 𝒯 involving E·T (a product of two curvature-type tensors)?

4. The normalization cancellation §6: under pure conformal h = -2ag in n = 4, ∫|Rm|²dμ is exactly constant (the 4D conformal invariance). For T = Rm + G, the extra G-dependent terms are bounded by CaF_T. Verify this dimension-specific cancellation.

5. The W^{1,p} → L^∞ bridge (Proposition 9.1): the base pair gives T ∈ L^q and ∇T ∈ L^q for all q on [τ,T*]. For p > 4, Kato + Sobolev gives ‖T‖_∞ < ∞. Is the Sobolev embedding valid on a closed manifold with bilipschitz-controlled geometry? Does the per-datum Sobolev constant depend on collapse? Check whether this really eliminates the need for the infinite staggered hierarchy.

## Output

## Verification memo — H₂ evolution and the W^{1,p}→L^∞ bridge (Step 57, on the exact flow ∂ₜg=−2χ²(Ric+g), n=4)

I worked through §§2–9 line by line against A01 step25 and the Step 56 base pair. The five requested points hold as stated, with one genuine normalization inconsistency in the definition of G that must be pinned down (it does not disturb any estimate but does disturb the flow identity that the whole construction rests on), and with the analytic crux (the Moser endpoint feeding Prop 9.1) being an inherited input rather than something these notes establish.

### 1. ∇_{g(t)}G(g(t))=0 and |∇T|²=|∇Rm|²

Correct, and the time/space distinction is handled properly. At each fixed t, ∇_{g(t)} is the Levi-Civita connection of g(t), so ∇_{g(t)}g(t)=0; since G is a polynomial in g with metric-independent coefficients, the Leibniz rule gives ∇_{g(t)}G(g(t))=0 at every t. Only the spatial covariant derivative at fixed time is ever used in the integrations by parts, so the time-dependence of ∇ is immaterial here. The place where the moving metric actually acts is the *time* derivative ∂ₜG, which is nonzero and is treated separately in (2.8).

Consequences used downstream all check:
- ∇T=∇Rm+∇G=∇Rm as tensors, hence |∇T|²=|∇Rm|² pointwise and D₂ coincides with A01's dissipation exactly.
- |G|² is a pointwise constant, so ∇|G|²=0 and Δ|G|²=0. With the correct normalization (see the factor-2 remark below) |G|²=2n/(n−1) (=8/3 at n=4). Therefore |T|²=|Rm|²+2⟨Rm,G⟩+|G|² gives Δ|T|²=Δ|Rm|²+2⟨ΔRm,G⟩ (3.2), because Δ⟨Rm,G⟩=⟨ΔRm,G⟩ (∇G=0) and Δ|G|²=0. This is the identity the extra Bochner term relies on. Exact.

### 2. Bochner pair §3

Both mechanisms verify.
- Cross term ∫2ηa(∇η)·∇|T|²=0: ∇η is supported on the collar {6r<d<7r}, and supp χ_α⊆B_{6r} forces a=χ²=0 there, so a∇η≡0. Correct given (1.2).
- Extra shifted term (3.5): ∫η²a⟨ΔRm,G⟩=−∫⟨∇Rm,∇(η²aG)⟩, and ∇(η²aG)=(2ηa∇η+η²∇a)⊗G because ∇G=0. The 2ηa∇η piece dies by a∇η=0, leaving −∫η²(∇a)·⟨∇Rm,G⟩. Young with |∇a|²/a≤4C_χ²/r² and |G|²=const gives (ε/2)η²a|∇Rm|²+C_n/(εr²), integrating to (ε/2)D₂+C_nVol/(εr²). This is genuinely an O(r⁻²Vol) source, correctly absorbed into C₀. Matches (3.6).

One point of terminology worth pinning: Type (A) in (2.7) writes Δ_L (Lichnerowicz), but the Bochner identity 2⟨V,ΔV⟩=Δ|V|²−2|∇V|² in (3.1) is for the rough/connection Laplacian. The difference Δ_L−Δ is a curvature contraction Rm∗Rm, which after pairing with 2T is cubic and lands in Type (D). This is standard and consistent, but the notation should be uniform (either carry Δ throughout and put Q(Rm) in (D), or state explicitly that the Δ_L→Δ correction is folded into the cubic potential).

### 3. Type (C) Hessian-of-a term §5, with 𝒯∼E·T

Correct, including for the product structure. After ∫η²(∇_i∇_j a)𝒯^{ij}, integrating the ∇_i by parts produces −∫η²(∇_i𝒯^{ij})∇_j a −∫2η(∇_iη)𝒯^{ij}∇_j a; the second term dies by ∇a·∇η=0 (1.3). The surviving term carries only ∇a=2χ∇χ, so only |∇χ|≤C/r enters — the Hessian ∇²χ inside ∇²a never appears. This "signed-Hessian" reduction is the real content and it is done correctly.

The product ledger for ∇𝒯 is right: |∇𝒯|≤C(|∇E||T|+|E||∇T|)≤C|∇T|F_T, using |∇E|≤C|∇Rm|=C|∇T|, |T|≤F_T, |E|≤C_nF_T. Only one factor is differentiated at a time, so Young splits into (ε″/2)a|∇T|²+C(|∇a|²/a)F_T²/(2ε″), i.e. ε″D₂+CH₂/(ε″r²). Matches (5.4).

### 4. Normalization cancellation §6 — confirmed, and genuinely n=4-specific

The cancellation is exact in n=4 and I confirm it is dimension-specific. For the pure conformal part h=−2ag with constant a, |Rm|² scales as e^{4t} (the (4,0) tensor scaling gives exponent −2 in λ=e^{−2t}, independent of n), while dμ scales as e^{½·tr(h)t}=e^{−ant}. Then
∂ₜ(|Rm|²dμ)=(4a−an)|Rm|²dμ=(4−n)a|Rm|²dμ.
This vanishes exactly at n=4 and only at n=4. In component terms this is the +8a|Rm|² from the four inverse-metric variations minus 4a|Rm|² from the algebraic tensor reaction (net +4a|Rm|²) against −na|Rm|² from the volume form; the two match only for n=4, leaving the bounded source −4a·dμ acting on the constant "1" in F², i.e. C₀=O(Vol). The A01 consistency computation g(t)=e^{−2t}g₀ ⇒ |Rm|²=e^{4t}|Rm₀|², dμ=e^{−4t}dμ₀ is correct.

The extra G-dependent terms for T are bounded as advertised: the conformal variation of 2⟨Rm,G⟩ is O(a|Rm|)≤O(aF_T), of |G|² is O(a), and the G-evolution contraction 2⟨T,∂ₜG⟩=−2a⟨T,E⊛g⟩/(n−1) is O(aF_T²); all sit inside C₁∫aF_T³+C₀ since F_T≥1. Correct.

The consequence for the wider program: the H₂ mechanism as written is tied to the exact n=4 cancellation. For n≥5 there is a residual (4−n)a|Rm|² term (a quadratic reaction, absorbable but altering constants and sign structure). This is consistent with §12 listing n≥5 as not yet handled, but it means the current H₂ derivation does not transfer to n≥5 without re-deriving this term.

### 5. W^{1,p}→L^∞ bridge, Prop 9.1

The Sobolev step is valid and the reduction of the infinite staggered hierarchy to (first level + Shi-type bootstrap) is logically sound, conditional on the input estimate (9.1).

- **Sobolev validity.** On [τ,T*] with τ>0 fixed and ‖U‖_∞≤Cγ/τ<∞, the metrics are bilipschitz with ratio e^{C(T*−τ)/τ}, so Morrey W^{1,p}↪L^∞ (p>n=4) on the closed manifold (M,g(t)) holds with a constant comparable to that of g(τ). Kato |d|T||≤|∇T| makes |T| a scalar in W^{1,p}, giving ‖T‖_∞<∞. The steps in §9.2 (bilipschitz → L^q seed (9.3) via the identity a|T|^{q+1}=|U||T|^q with |U|≤K → coupled (V,Z) → X=∇T) are internally consistent with the Step 56 base pair, which establishes exactly the first level T₀∈∩_qL^q ⇒ (U₁,C₂)∈∩L^q ⇒ T₁∈∩L^q. So Prop 9.1 uses only the established first level plus Sobolev, not the full infinite tower.

- **The per-datum Sobolev constant does depend on collapse.** This is stated correctly: C_S depends on (M,g(τ),K,p), and for a collapsing sequence the injectivity radius / volume of g(τ) can degenerate, driving C_S up. The architecture isolates this correctly — C_S enters only the finite-time continuation for a single datum near T*, never the sequence-uniform first-exit constants, which use γ=𝒮K₂^{1/2} claimed collapse-independent via Maheux–Saloff-Coste under Ric≥−(n−1)r⁻². The two Sobolev constants are genuinely different objects and are not conflated.

- **Does it eliminate the hierarchy?** Yes in the sense that once |T|<∞ pointwise (hence |Rm|<∞), Step 6(a) is a standard Bando–Shi bootstrap: bounded curvature on a time interval controls all ∇^m Rm with coefficients depending only on K and the fixed cutoff jets. The infinite hierarchy is then needed "in principle" only and closes by Grönwall with bounded data. This is correct as a bootstrap, provided the pointwise curvature bound is actually in hand.

- **The load-bearing input is (9.1), which is not established in these notes.** §12 states this: ‖aF_T(t)‖_∞≤Cγ/t is inherited from the H₂–Y–Moser chain; the Moser iteration itself is not re-derived here. Prop 9.1 is therefore a conditional continuation lemma: it converts (9.1) into smooth extension, but the production of (9.1) (the weighted Moser endpoint) is the actual analytic engine and remains outside what §§2–9 verify. Everything in the terminal-slab contradiction of §10 rests on (9.1).

### Cross-cutting item to fix: the normalization of G (factor 2)

There is an internal inconsistency in the component formula for G that should be corrected before this is treated as settled, and certainly before any Lean encoding.

- The operative definition (Step 57 (1.1), Step 56 §6.1) is G=g⊛g/(2(n−1)) with the property Ric(G)=g, which is what makes Ric(T)=Ric+g=E and hence ∂ₜg=−2Ric(U)=−2aE (the flow itself). This forces G_{ijkl}=(g_{ik}g_{jl}−g_{il}g_{jk})/(n−1) (Kulkarni–Nomizu of g with itself carries a factor 2: (g⊛g)_{ijkl}=2(g_{ik}g_{jl}−g_{il}g_{jk})). Check: g^{ik}G_{ijkl}=(n−1)g_{jl}/(n−1)=g_{jl}. ✓ Ric(G)=g.
- The explicit component line written in Step 57 §2.8, "G_{ijkl}=(g_{ik}g_{jl}−g_{il}g_{jk})/(2(n−1))", gives instead Ric(G)=½g, which contradicts Ric(G)=g and would break Ric(T)=E. The ∂ₜG in (2.8), written −a(E⊛g)/(n−1), is also a factor of 2 off; the correct value with the /(n−1) normalization is ∂ₜG=−2a(E⊛g)/(n−1).

Because all G-terms are used only through the bounds |G|≤C_n, |∂ₜG|≤C_naF_T, this factor-2 slip does not alter the validity of any estimate — it only shifts dimensional constants. But it does touch the identity Ric(G)=g that defines the flow, so the component formula and the ∂ₜG coefficient should be rewritten consistently as /(n−1) and −2a(E⊛g)/(n−1). This is exactly the kind of constant that a kernel re-check will not forgive.

### What the note establishes versus what it rests on

Read against the top research target (all n≥2, dimension-only c_n<C_n, all closed topologies, an actual Einstein metric h, plus Lean), §§2–9 provide a correct conditional analytic component:

- The H₂ inequality (7.1) is derived correctly and reproduces A01's structure with only first-cutoff-derivative constants (no ∇²χ), plus an r⁻²Vol source from the G-shift. Verified term by term.
- The continuation bridge Prop 9.1 is a valid finite-order replacement for the infinite hierarchy, conditional on (9.1).

The result these notes report sits on a substantial tower of inputs proved elsewhere or not yet proved: smooth per-datum existence (Step 56, itself a large tame construction, per-datum lifespan depending on high Sobolev norms of the datum); the Moser endpoint (9.1) (the true crux, inherited); the base-pair first level (Step 56, invoking a Step 44 signed-Hessian seed not shown here); J₆ persistence (Step 35); and the terminal density mechanism (Steps 43, 47) that alone connects "every datum reaches θr²" to the Ishida–LeBrun contradiction and thence to existence of an Einstein metric with λ<0. None of that payoff link is visible in §§2–9, so what is verified here is a clean piece of the analytic machinery, restricted to n=4 and the λ<0 branch, not a statement about M carrying h with Ric_h=λh.

### Items that would strengthen this specific note

1. Rewrite G's component formula and ∂ₜG coefficient consistently with Ric(G)=g (the /(n−1) convention), and record |G|²=2n/(n−1).
2. Remove or replace the admittedly-wrong scratch line in §8 ("Y=∫η²u²≤‖ηu‖₄²·Vol^{1/2}… not the correct absorption"); the correct absorption via I₄=∫F_T u² with u=aF_T^{3/2}, u²=a²F_T³ (Cauchy–Schwarz ‖F_T‖₂‖u‖₄² then Sobolev) should stand alone. As written the section mixes a discarded step with the real one.
3. State whether (2.7)'s Type (A) uses Δ or Δ_L uniformly, and where the Δ_L−Δ curvature correction is placed (it is cubic and belongs in Type (D)); currently the notation switches.
4. Make explicit, in Prop 9.1, that C_S(g(τ)) can degenerate along the collapsing sequence and quantify what fails if T*↓0 (the bound Cγ/T* also degenerates); the terminal-slab argument in §10 step 4 needs T* bounded below by a per-datum positive number, which it gets from finiteness at fixed τ but the argument should say this explicitly.
5. The link from (9.1) to a full statement about the Einstein metric is the deciding piece; since these notes inherit (9.1) and defer the Ishida–LeBrun contradiction to Steps 43/47, the value of §§2–9 is only realizable once those are checked with the same term-by-term care applied here.

Net: the four PDE derivations (points 1–4) are correct as written, the n=4 cancellation is genuinely dimension-specific and correctly used, and the W^{1,p}→L^∞ bridge (point 5) is a valid conditional lemma whose sole nontrivial input (9.1) is not proved in these files. The one concrete correction needed is the factor-2 normalization of G, which touches the defining identity Ric(G)=g even though it leaves every estimate's validity intact.