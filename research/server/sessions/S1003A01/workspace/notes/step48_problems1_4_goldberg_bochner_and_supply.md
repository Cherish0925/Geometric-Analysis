# Step 48 — Problems 1 and 4: supply analysis, the AK Weyl–Bochner identity, and the near-KE reduction

Session S1003A01, Agent2. Status labels: [P] proved here (hand derivation, not yet independently verified or symbolically checked), [K] known/cited, [O] open.
Sources read: `Skills/geometric-analysis/references/einstein-problems-20261007.md`; `five_research_problems.tex` §§1–4 (lines 120–700); `web_research_collected.tex` Ch.1 §N1 (lines 130–330) and Ch.6 (2296–2893); Knowledge: Kim arXiv:2311.16729 (full), AAD arXiv:math/0109098 §2.3–2.5, Kirchberg math/0605611 abstract, AAD math/9911197 abstract; A02 notes step42, step44.
Literature request s48_t11_tool1 (Armstrong ansatz, local λ<0 strictly AK Einstein existence, 2015–2026 progress, LeBrun 2005) was still running at step close — read its result before relying on any novelty statement below.

## 1. Known integrability results that fix the open configuration [K]
For closed AK Einstein (M,g,J,ω), |ω|²=2, s<0 const, q=|∇ω|², s*=s+q:
- Sekigawa: s≥0 ⇒ Kähler.  AAD (Math. Ann. 2002): Ric J-invariant + ω eigenform of W⁺ (η:=W⁺(ω)^⊥=0) ⇒ Kähler (compact).  Kirchberg: Einstein + |W⁺| const ⇒ Kähler.  Drăghici/Kim: c₁·[ω]≥0 ⇒ Kähler.  Kim Cor.7: π₁=1 + degenerate W⁺ spectrum ⇒ KE.
- LeBrun's δW⁺=0 identity ∫ sW⁺(ω,ω)=8∫(|W⁺|²−½|η|²) is, on Einstein metrics, IDENTICAL to the Chern–Weil c₁² identity (Kim Cor.3): substituting W⁺(ω,ω)=s*/2−s/6 gives ∫(ss*/8−s²/24)=∫(2|W⁺|²−|η|²) both ways. So it carries no information beyond the five-problems AK balance (eq. AKbalance).
- In the negative case c₁·[ω]<0 always: 4πc₁·ω=V(s+q̄/2) and AK balance + Cauchy–Schwarz give q̄≤(2/3)|s|. Hence the Drăghici/Kim criterion is vacuous for s<0.
- N nowhere zero ⇒ 5χ+6τ=0 (Armstrong/LeBrun, AAD Lemma 2); with Hitchin–Thorpe this forces flatness, so for s<0 the Kähler-nullity set {∇ω=0} is nonempty (weighted count 5χ+6τ≥χ>0).

## 2. AK Weyl–Bochner identity [P]
Frame e₀=ω/√2, e₁=φ/√2, e₂=Jφ/√2 (AAD gauge: ∇Ω=a⊗φ−Ja⊗Jφ, ∇φ=−a⊗Ω+b⊗Jφ). Then ∇e₀=A₁e₁+A₂e₂, A₁=a, A₂=−Ja, |A_i|²=|a|²=q/4, A₁⊥A₂. Write W⁺ entries W₀₀=ν=s/6+q/4, W₀ᵢ=ηᵢ, block −ν/2·I+V, V=[[v₁₁,v₁₂],[v₁₂,−v₁₁]], |η|²=η₁²+η₂², |v|²=v₁₁²+v₁₂² (entry norms; five-problems norms are 2|η|², 2|v|²).
(i) Divergence identity: from ∇*∇Ω=2ρ*''+(q/2)Ω, η=−½ div¹(A) (canonical-connection divergence of the torsion), i.e. −div a−⟨Ja,b⟩=2η₁, div(Ja)−⟨a,b⟩=2η₂.
(ii) Derdziński Weitzenböck (δW⁺=0): ∫(2|∇W⁺|²+s|W⁺|²−36detW⁺)=0, with 36detW⁺−s|W⁺|²=(9/4)qν²+(8|s|−9q)|v|²+(9q/2−|s|)|η|²+36C₃, C₃=v₁₁(η₁²−η₂²)+2v₁₂η₁η₂.
(iii) Splitting ∇W⁺=∇¹W⁺+T(A)·W⁺ and integrating cross terms by parts with (i):
∫[ (3/2)|dν|²+2|∇¹η|²+2|∇¹v|²+(9/8)qν²+(11/2)q|v|²+((13/4)q−(3/2)|s|)|η|²−4|s||v|²−26C₃−12⟨dν,η·A⟩+8Y ]=0,
Y=⟨∇¹v₁₁,η₁A₁−η₂A₂⟩+⟨∇¹v₁₂,η₂A₁+η₁A₂⟩.
(iv) Eliminating 4|s|∫|v|² with AK balance ∫(2|η|²+4|v|²+3q²/16)=(|s|/8)∫q leaves
∫[ (3/2)|dν|²+2|∇¹η|²+2|∇¹v|²−(3/32)s²q+(3/32)|s|q²+(9/128)q³+(11/2)q|v|²+((13/4)q+½|s|)|η|²−26C₃−12⟨dν,η·A⟩+8Y ]=0.
Reading: in the case η=V=0 the identity immediately forces q=0 (short Bochner proof of the Einstein eigenform case). In general the zeroth-order term −(3/32)s²q is the obstruction: integral formulas alone cannot beat it (no Poincaré inequality in the right direction). The only plausible source of a compensating term is the AAD Bianchi component (38), which fixes the canonical divergence of V as ≈−(κ/8)∇_{J·}Ω plus η, dq terms, so |∇¹v|²≥|δ¹V|²~(s²/64)q·const; whether this, combined with the line-bundle Weitzenböck on K⁻² (∂ vs ∂̄ parts of ∇¹V) and the η-equation (37), beats 3s²q/32 is the decisive computation [O]. Coefficients above must be symbolically verified before use.

## 3. Near-KE and rigidity reduction [P, modulo cited inputs]
Lemma KE. On a compact KE surface with s<0, every self-dual (complex orientation) harmonic 2-form of constant length √2 is ±ω₀. Proof: ω=cω₀+Reθ, θ∈H⁰(K); constant length forces |θ| const; i∂∂̄log|θ|²=ρ=λω₀≠0 where θ≠0, so θ=0.
Consequences: (a) if every Einstein metric on M is KE for some complex structure (with the AK orientation equal to the complex one), Goldberg holds on M. (b) On manifolds underlying compact ball quotients: LeBrun's Einstein rigidity (every Einstein metric is CH up to diffeo/scale) + Lemma KE handles the complex orientation; for the reverse orientation W⁺(M̄)=W⁻(CH)=0 gives q=−2s/3 const>0, contradicting nonempty Nijenhuis zeros since 5χ+6τ(M̄)=3χ≠0. So Goldberg holds on every ball-quotient manifold [likely folklore — check survey]. (c) Near a negative KE metric, AK Einstein pairs converge smoothly to (g₀,±ω₀); Goldberg near KE reduces to Koiso's statement that Einstein metrics near negative KE are KE (needs the obstructed-Kuranishi case checked). The linearization is degenerate along ω₀+tReθ (length violated only at order t²), so any near-KE quantitative Goldberg estimate is Łojasiewicz/square-root type, not linear.

## 4. Problem 1: actual-field supply [P]
- Reverse orientation: M̄=X̄#kCP². If b⁻(X)≥1 both summands have b⁺≥1, so ordinary SW of M̄ vanish; Bauer–Furuta of kCP² is trivial. Fake projective planes (b⁻=0) give only a b⁺=1 chamber input at k=1,2. Hence the Chapter-6 two-orientation cross-pairing has no supply on blowups of general type.
- Same orientation: the 2^k classes a_ε=K+Σε_iE_i give only max/average information (LeBrun; N1); near k/A=1/3 the average forces ‖E_i⁺‖→0 and ‖K⁻‖→0. FD with each class (budget A−k, bounded density B≲6+36/A+k/A since c₂≤5c₁²+36 for general type) reproduces exactly the N1 window: on an Einstein metric κ_β=D_β/V, and D_β≥0 ∀β is equivalent to LeBrun's k≤A/3 (extremal β≈8, x=V/(2π²A)≈1.78 at k/A=1/3); FD's c(B)(β−2)²/β² gives the ε-extension and nothing far below 1/3.
- The exact-Einstein entrance: LeBrun's loss is the Cauchy–Schwarz ratio t=√6|W⁺|/|s| (extremal t=1/8; Kähler t=1/2). If an Einstein metric with the blowup SW classes had t≥1/2 in the weighted sense, ∫(s²/24+2|W⁺|²)≥4π²(c₁⁺)²≥4π²A would exclude every k≥1. δW⁺=0 alone does not force large t (constant-|W⁺| Einstein at t=1/8 only needs |∇W⁺|²≥|s|³/1024). Missing information: an Einstein/SW mechanism controlling the |W⁺|:|s| ratio [O].

## 5. Collaboration
Reply #825 to A02 #824: the S⁴/Z₂ absorption cell is the ι-quotient of a two-ended connected-sum neck with σ=diag(1,−1,−1,−1); shrinking cost 16π² = 8π² per absorbed class (standard), so savings can come only from the CH germ; ι maps left- to right-invariant Berger sections, so the cell lies outside the SU(2)-diagonal class (T² reduction needed).
A02 #826 (Step 53, unanswered at close): Anderson case-(I) energy equality, bubble-movement theorem 53.B forcing R⁺≤0 on bulk components, Theorem 53.D/E, and a question whether the Chapter-5 x²log(1/x) kernel coefficient stays negative on non-CH KE backgrounds for all W⁻.
