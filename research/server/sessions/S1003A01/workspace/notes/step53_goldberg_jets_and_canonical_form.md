# Step 53 — Problem 4 (negative-scalar Goldberg): formal-jet structure and the closed canonical form β

Session S1003A01, Agent2. Labels: [P] proved here (by hand), [N] numerical evidence, [K] cited, [O] open.

## 0. Setting and conventions
(M⁴,g,J,ω) closed, ω(X,Y)=g(JX,Y), dω=0, Ric=λg, λ<0, s=4λ. Orientation of J; ω self-dual harmonic, |ω|²=2 (form norm).
q=|∇ω|², s*=s+q. W⁺ in the splitting ℝω/√2 ⊕ ω^⊥ (five_research_problems.tex §4, eq. (eta),(canonicalcurv)):
W⁺ = [[ν, η*/√2],[η/√2, −ν/2 I + V]], ν = s/6 + q/4.
Canonical (Blair/Chern) connection 𝒜 on K⁻¹: iF_𝒜 = η + ((s+s*)/8) ω + ((s−s*)/8) ω̂, ω̂ ASD with |ω̂|²=2 on {q>0}.
Integrability bridge [K, AAD]: η ≡ 0 ⇒ Kähler on closed M.

## 1. Local status [K]
AAD, "Local rigidity of certain classes of almost Kähler 4-manifolds" (Knowledge object Local-rigidity-…c0d51aa8ffb7, intro lines 33–38):
- Nurowski–Przanowski and Tod give *local* strictly AK Einstein metrics, all Ricci-flat; in all of them W⁻=0 and η=0.
- [AAD/Armstrong, ref. [6] there] every strictly AK Einstein 4-manifold with ω an eigenform of W⁺ (η=0) is of NPT type, hence Ricci-flat and never compact.
- "The case of negative scalar curvature is still wide open."
Consequence: for λ<0 the existence of *local* strictly AK Einstein metrics is itself not supplied by these sources (literature request s53_t7_tool1 pending). If no local λ<0 examples exist, a finite-order prolongation obstruction would prove local, hence global, Goldberg; if they exist formally, the problem is genuinely global. Deciding which is the case is therefore a decisive question, not a side computation.

## 2. Formal system and corrected symbol interpretation [P]
Unknown jets in coordinates with g=δ+O(|x|²), ω(0)=e⁰¹+e²³: g (10 comps, degree 2..D), ω (6 comps, degree 1..D). Equations: E1 ωᵀg⁻¹ω=g, E2 dω=0, E3 Ric=λg. The Step-53 count omitted an independent scalar Ricci-symbol relation. In Darboux gauge, a compatible variation h satisfies hJ+Jh=0 and
 σ_Ric(ξ)h(Jξ,Jξ)−(1/2)|ξ|² tr σ_Ric(ξ)h=0.
Its prolongations add n_{N−4}; the corrected top-degree free count is N²+8N−5 for N≥4, so the earlier negative count at N=15 and estimate near 18 do not predict a Goldberg obstruction. Nor can the full nonlinear Jacobian rank detect a genuine lower-jet condition reliably: one must hold a lower jet fixed and project the next-order source onto the symbol cokernel after removing known identities. Exact details and the intrinsic AAD interpretation are in `step55_darboux_ricci_compatibility.md`.

## 3. Numerical jet engine [N]
`workspace/scripts/step53_ak_einstein_jets.py` uses JAX truncated multivariate polynomials and all-at-once Gauss–Newton. The exact H²(−1)×H²(−1) Kähler–Einstein jet has residual 0 at D=4.
D=4 and independently optimized D=5 truncations exist numerically for q₀=0, RF (λ=0,q₀=0.3), and NEG (λ=−1,q₀=0.3), with residual squares about 10⁻²⁷. At D=5, ranks are 1035 for q₀=0 and 1036 for RF/NEG. These independently optimized jets are not compatible formal germs. The q₀=0 random jets are also not Kähler germs: their pointwise q is zero but the reported η and W⁺ are generic, so only the explicit H²×H² jet is an exact KE control. D6/D7 files from the cancelled high-memory task are incomplete and have no mathematical meaning.
A first fixed D4→D5 extension of the numerical random jets gave nonzero cokernel projections for every branch, including the controls; it therefore establishes only that these random D4 truncations do not lie on the sampled degree-five branches. Before further prolongation the code must use exact KE and exact Tod sources and quotient the cokernel by algebraic compatibility, closure, Bianchi, and the Darboux Ricci relation. Re-running the unconstrained degree ladder is not warranted.

## 4. The closed canonical form β [P]
Einstein gives ρ=(s/4)ω for the Riemannian Ricci form, closed. Put β := iF_𝒜 − (s/4)ω. Then dβ=0, [β]=2πc₁ − (s/4)[ω], and
 β⁺ = η + (q/8)ω,  β⁻ = −(q/8)ω̂,  β − η = (q/8)(ω − ω̂) = ± a∧Ja (decomposable, |·|² = q²/16).
Since η ∈ [[Λ^{2,0}]] and a∧Ja is of type (1,1), β∧β = |η|² vol pointwise. Hence ∫|η|² = [β]² — this is exactly the AK balance (AKbalance) again, now as a cup-square identity.
Hodge comparison with the harmonic representative H of [β] (H⁺ = 2πc₁^{+,h} − (s/4)ω, H⁻ = 2πc₁^{−,h}): ‖β‖² ≥ ‖H‖² and ‖β⁺‖²−‖β⁻‖² = ‖H⁺‖²−‖H⁻‖² give
 ∫ q²/16 ≥ 2‖H⁻‖² = 8π² ‖c₁^{−,h}‖²_{L²}.
So the anti-self-dual harmonic part of c₁ is a lower bound for nonintegrability (vanishes for KE, consistent). It does not force q=0; it shows that a strictly AK Einstein metric whose harmonic c₁ is not self-dual must pay q in L². The upper side still needs a new compatibility relation.

## 5. Open [O]
- Local λ<0,q>0 existence remains unresolved. The next meaningful local calculation is an intrinsic prolongation of the AAD Ricci/Bianchi system, or a fixed-lower-jet calculation based on exact KE and exact Tod controls with all universal identities removed.
- Globally, the checked Einstein AAD equations couple q, η, W₃⁺ and the Nijenhuis derivative; the exact identities are recorded in `step55_darboux_ricci_compatibility.md`. The missing input is canonical-connection/actual-field coercivity for the transverse terms, not another scalar counting argument.
