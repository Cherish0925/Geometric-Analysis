# Step 81: closed negative Goldberg. Normalized sections, the fixed-ε transfer principle, and the dd^c pairing with the canonical forms

Agent2, Execute. Inputs: the Step-80 note, Spirit #88, and the Step-79 frame engine.
Scripts:
- `workspace/scripts/step81_ddc_canonical_pairing.py` (modes `points`, `integrals`)
- `step81_torsion_jet.py`
- `step81_levi_leading_sign.py`

Data:
- `workspace/data/step81/ddc_points.json`
- `workspace/data/step81/torsion_jet.json`
- `workspace/tasks/s81_t11_tool1/stdout.log`, which holds the integral run; the JSON copy is `data/step81/ddc_integrals.json`
- `workspace/data/step81c/levi_leading_sign.json`

**Step-82 corrections (operative; see `step82_goldberg_levelset_SW_and_symmetric_closures.md` §0):**
1. On the complete model ∫ε/(q+ε)=∞ for every fixed ε>0; the ε^{-2/3} growth belongs to ∫q/(q+ε).
2. Proposition 81.T holds only for currents whose integrability, decay and end flux are verified.
3. The radial-positivity claim "Δlog q≈4m/ρ²>0 near zeros" and the "logarithmic mass balance priced by 5χ+6τ" in §2 are withdrawn. An anisotropic Step-62 cone jet gives ρ²Δlog q≈−0.181 along one direction, and Euler index does not bound positive log-mass or a neighbourhood scale.

Conventions are those of Steps 79–80: h=q+ε, Y=∂r−ηα, X=Re(ηα), and K antilinear with K²=−1.

## 1. Normalized sections (Spirit #88), made exact

**E1 simplifies in general.** Since K is antilinear, K(∂r)=K(Y)+η̄K(α). The two η̄K(α) terms of E1 therefore cancel:

  (E1′)  ∂_Dη = vα + iK(Y).

So the (1,0)-derivative of η is controlled exactly by v and by the same square Y that appears in (80.S).

**Normalized variables.** Set σ_η=η/√h, σ_v=v/√h, α̂=α/√h, Ỹ=Y/h, and ℓ=log h. These satisfy:
- |α̂|²=q/(2h)<1/2;
- ∂ℓ=4(Ỹ+σ_ηα̂), because ∂q=4∂r=4(Y+ηα);
- j_σ=j_f/h, because the extra term Re(i|f|²dℓ∧ω)/2 is imaginary. Hence (80.K) is literally the Kodaira identity for σ.

The Bianchi system in normalized form is:

  (E1σ) ∂σ_η = σ_vα + i√h K(Ỹ) − 2σ_η(Ỹ+σ_ηα̂),

  (E2σ) conj(∂̄σ_η) + 2iK(∂σ_v) = −(3r/2)α̂ − 2σ̄_η(Ỹ+σ_ηα̂) − 4iσ̄_v(K(Ỹ)+σ̄_ηK(α̂)).

Every drift term is either Ỹ, which is controlled in L² by the left side of (80.S) since 32‖Ỹ‖² appears there, or a σ·σ·α̂ product with α̂ bounded. In these variables (80.S) reads

  32‖Ỹ‖² + (|s|/2)∫q/h = 8∫(|σ_η|²+2|σ_v|²) + 16∫(q/h)|σ_η|² + (3/4)∫q²/h.

**Weighted Bochner identity.** The weighted W⁺ Bochner identity in exact form is

  ∫(|∇W⁺|² − bochR)/h = ∫(s/16+3q/32)|dq|²/h² + ∫⟨d(|η|²+2|v|²),dq⟩/h².

The coefficient s/16+3q/32 equals 3r/8. It is negative wherever q<2|s|/3, which is a favourable sign near zeros.

In σ-variables the genuinely quartic terms are |σ_v|²|dℓ|² and |σ_η|²|dℓ|², where |dℓ|²=32|Ỹ+σ_ηα̂|². The gradient side of the identity contributes (3/2)|σ_v|²|dℓ|², and the weight side contributes 2|σ_v|²|dℓ|² + |σ_η|²|dℓ|². The net coefficient of |σ_v|²|dℓ|² is therefore −1/2 on the gradient side, and |σ_η|²|dℓ|² carries no matching square.

This is the exact residue of the denominator mismatch. It is a product of two L²-type quantities, |σ|² and |Ỹ|². It is not a loss caused by splitting the current prematurely, because σ-normalization has already absorbed all such splitting.

## 2. Fixed-ε transfer principle

**Proposition 81.T.** Fix ε>0. Consider any finite family of integral identities ∫Φ_k=0 obtained from divergences of currents Σ w(q,r,ε)·P, where P is polynomial in (α, η, v, r−s/6, Dα, Dη, Dv, dq) and w is smooth and bounded with bounded derivatives on h≥ε. Every such identity holds on the complete Bianchi-VIII model.

*Reason.* All densities are at least quadratic in fields decaying like t^{3/2} or faster at the ACH end, while the measure is ~t^{-3}dt. All fluxes are at least quadratic in decaying fields against area ~t^{-2}.

**Consequence.** No pointwise certificate Σc_kΦ_k ≥ κ q/h (κ>0) exists at fixed ε; if one did, the model would be Kähler.

**Where compactness can enter.** The only compactness-sensitive density is the field-free weight ε/h=1−q/h. On a closed manifold ∫ε/h → Vol(Z)=0 as ε→0. On the model it diverges like ε^{-2/3}.

**The sharp algebraic target.** Find a combination with

  Φ_ε ≥ κ(q/h) − C(ε/h) − (zero-localized terms whose integrals → 0).

Such a certificate is *not* ruled out by the model, and it would prove closed Goldberg. At ε=0 it becomes a uniform normalized superharmonicity statement. The model in fact satisfies −Δlog q ≥ 6=|s|/2 at every sampled point (`torsion_jet.json`: Δlog q ranges over −6.32…−12.38). That is the model's ε=0 version of 79.L, with the end flux absorbing it.

On a closed manifold, Δlog q≈4m/ρ²>0 near isolated zeros. The decisive global question therefore becomes a **logarithmic mass balance**:
- the positive mass carried within curvature distance of the zeros, whose number is forced by c₂(E)=5χ+6τ;
- against the negative mass of a model-like bulk, which is proportional to V, with s²V=32π²c₁²+16T_AK.

Both are topological at the scale |s|^{-1}, so the competition is quantitative, of order O(1). This formulation is new, and the next attempt should be pursued in it.

## 3. The exact two-form Θ_u=dd^c u and the canonical forms (general results)

**(P1)** Θ_u∧ω=(Δu)dV on every almost-Kähler 4-manifold, because d^cu∧ω=*du and dω=0.

**(P2) Nijenhuis part.** Write ∇_XJ via ∇ω=√2Re(α⊗ψ), and use the algebraic identity α∧ι_Xψ=α(X)ψ for ψ∈Λ^{2,0}. Then

  Θ_u = (Hess u∘J)^{J-inv} + √2 Re(α(∇u)ψ).

The (1,1) part is the Levi-Civita Levi form, with Θ(e,Je)=Hess u(e,e)+Hess u(Je,Je)=:L_u(ℓ). The (2,0)+(0,2) part is first order in du.

**(P3) Kim.** γ⁺=(s/4+q/8)ω+√2Re(η̄ψ) and |γ⁻|²=q²/32.

**(P4)** β^{1,1}=(q/8)ω+γ⁻ has rank one. It vanishes on the torsion line ℓ_α=span(Reα^♯,Imα^♯) and equals q/4 on the complementary line ℓ_α^⊥. This is consistent with Lemma 77.2, and Im α^♯=J Re α^♯ holds exactly.

**(P5)** Θ_u∧β=(q/8)Δu+2⟨du,X⟩−⟨Θ⁻,γ⁻⟩, with ⟨Θ⁻,γ⁻⟩=(q/8)(L_u(ℓ_α^⊥)−L_u(ℓ_α)).

**Identity 81.I.** Since β is closed, for every u

  ∫⟨Θ_u⁻,γ⁻⟩ = ∫⟨du, 2X − dq/8⟩.

For u=log h this becomes, via |dq−8X|²=32|Y|² and 64|X|²=16q|η|²,

  ∫(q/8)[L_{log h}(ℓ_α^⊥) − L_{log h}(ℓ_α)] = ∫(2q|η|² − 4|Y|²)/h.

This is a regularized identity for the *primitive anisotropy* of the Levi form of log h between the torsion line and its complement. It is not contained in (80.R), which sees only the trace.

**Surface residues.** On a torsion-zero J-surface C one has β|_C=0, so the 4πm[C] residue is invisible to β. Pairing with γ reproduces exactly (s/4)× the ω-residue, which is the Step-63 degree formula γ(C)=(s/4)Area(C). The scalar γ-pairing therefore carries no independent canonical-degree information. New information lives only in the primitive or anisotropic part of 81.I.

**Model verification** (`ddc_points.json`; p=0.4–0.9, ε=10⁻² and 0):
- P1, P2 and P5 hold to residuals ≤10⁻²⁹;
- the γ-trace, |η|², and |γ⁻|²=q²/32 match exact formulas to all digits;
- β(ℓ_α)~10⁻³¹ and β(ℓ_α^⊥)=q/4.

**Integrated 81.I** on the model at fixed ε (`s81_t11_tool1`; 12 Gauss nodes per unit u, u≤18):
- the pairing ∫⟨Θ⁻,γ⁻⟩ equals ∫(2q|η|²−4|Y|²)/h: 2.37845981569 at ε=10⁻¹, 4.21877413201 at 10⁻², 6.89101186092 at 10⁻⁴ and 7.74212111898 at 10⁻⁶, with residuals ≈5.8×10⁻¹²;
- ∫Θ∧β is of order 10⁻¹³, consistent with Proposition 81.T.

## 4. Torsion first-jet structure

**General fact.** (d_bα)^{1,1} is pure trace (Step 79), and antisymmetrization Λ^{0,1}⊗Λ^{1,0}→Λ^{1,1} is an isomorphism. Hence the antiholomorphic derivative D''α is pure trace, algebraically ∝η̄·𝟙. For every unit Z:
- |D_Z̄α|²=|η|²/2;
- D_Z̄α ∥ α along ℓ_α.

The holomorphic derivative D'α=S+Skew, with |Skew|²=2|v|² and S free. On the model (`torsion_jet.json`) the trace-free part of D''α is ≤10⁻⁵⁹ and |D'_Zα|²=16|D_Z̄α|². At a zero, Δq=4|∇α|²=16|v|²−24|η|² reproduces the Step-62 cone ‖A‖²=‖S‖²+8|c|².

**Exact model law.** L_{log q}(ℓ_α)=s/2=2γ(ℓ_α) at every one of 11 sampled p∈[0.34,0.99], to 14 digits. Correspondingly Δlog q=s/2+L_{log q}(ℓ_α^⊥).

In general, a Poincaré–Lelong expansion with Z∈ℓ_α (canonical connection; Chern torsion has no (1,1) part) gives

  L = 8Re⟨∇̃²_{ZZ̄}α,α⟩/|α|² − 4Re⟨R̃(Z,Z̄)α,α⟩/|α|² + 4Gdef/|α|⁴ − 8Re(ab)/|α|⁴,

where:
- a=⟨D_Zα,α⟩ and b=⟨D_Z̄α,α⟩;
- Gdef=|D_Zα|²|α|²−|a|²≥0;
- ∇̃²_{ZZ̄}α is fixed by E2, so −(3r/2)α and K(∂_Dv), i.e. I, enter.

The model has Gdef=0 and a=−4b exactly. The R̃ term has not yet been reduced to (W⁺,W⁻,s,q); this reduction is open.

**The law is not general (falsification).** At a nondegenerate zero the leading part is L≈4Λ/|f|², with

  Λ=|Bw|²−|⟨Bw,f̂⟩|²−2Re(c⟨Bw,f̂⟩),  f=Bx+cx̄,  w=conj f̂.

On 20000 Step-62 cone jets and directions, Λ<0 in 6.3% of samples (minimum −4.30; median 3.27). Off the cone the fraction is 44%. The c=0 sector is psh, as expected. The closed formula agrees with finite differences.

So log q is not J-psh along torsion lines even at leading order, and no general inequality L_{log q}(ℓ_α)≥s/2 holds. The model's exact law is special to it, plausibly a first integral of the cohomogeneity-one ansatz, and should not be used as a general mechanism.

## 5. What this changes

- Spirit #88's normalization is exact and removes all "Young-splitting" losses. The irreducible obstruction is the quartic product |σ|²|Ỹ+σ_ηα̂|², together with the free jets ∂̄σ_v and S.
- Proposition 81.T converts the question of a multiplier search into a precise algebraic target. Any proof must use ε/h, i.e. finite volume, together with zero-localized mass.
- The dd^c–β pairing gives one genuinely new regularized identity (81.I, primitive anisotropy). It adds no independent surface canonical-degree information.
- The natural next global object is the logarithmic mass balance between the forced torsion zeros (5χ+6τ) and the bulk superharmonicity of log q.
