# Step 79 — Closed negative Goldberg, second tier: the complex δW⁺=0 system, Kodaira identities, the complete model as an exact second-tier budget, and a compact log-torsion identity

Agent2, Execute. Inputs: Step-77 note, Step-78 Meta-Trace, Spirit #85/#86, A02 #878.
Script: `workspace/scripts/step79_dW_components_bianchiVIII.py` (independent orthonormal-frame Koszul engine, mpmath 40 digits).
Data: `workspace/data/step79/dW_check.json`, `kodaira_flux.json`, `model_integrals_n{24,40}.json`, `logq_check.json`.

## 0. Conventions (identical to Step 77, made complex)

(M,g,J,ω) almost-Kähler, Ric=(s/4)g, s<0 constant, |ω|²=2. Orthonormal frame of Λ⁺: u₁=ω/√2, u₂,u₃, with ψ=u₂+iu₃ chosen of type (2,0). Then

- ∇u₁ = Re(α⊗ψ), α := ⟨∇u₁,u₂⟩ − i⟨∇u₁,u₃⟩. Closedness of ω forces α∧ψ=0, i.e. α ∈ Λ^{1,0}. |α|² = q/2, q=|∇ω|².
- ∇ψ = −ᾱ⊗u₁ − i b⊗ψ, b=⟨∇u₂,u₃⟩ (the canonical Hermitian connection on K); ⟨db,ω⟩ = −(2s+q)/4, i.e. db and −γ have the same ω-trace (γ = canonical Ricci form, [γ]=2πc₁).
- W⁺u₁ = r u₁ + Re(η̄ψ), W⁺ψ = η u₁ − (r/2)ψ + v ψ̄, with η = W₁₂+iW₁₃ (so |η|² = |η|²₆₂ of Step 77) and v = (W₂₂−W₃₃)/2 + iW₂₃ (so trV² = 2|v|²). r = s/6 + q/4.
- Weights: Dη = dη + i bη, Dv = dv + 2i bv. ∂,∂̄ denote (1,0),(0,1) parts; for complex 1-forms |ξ|² = Σ_a|ξ(e_a)|².
- K: Λ^{1,0}→Λ^{1,0} is the antilinear map K(ξ)=Ĵ(ξ̄), where Ĵ:Λ^{0,1}→Λ^{1,0} is defined by ζ∧ψ = 2i Ĵ(ζ)∧u₁. K is an isometry (|Kα|²=|α|², |K∂r|²=|∂r|² verified) and K² = −1.

## 1. The δW⁺=0 system in almost-Kähler variables

For an Einstein metric δW⁺=0 is d^∇ of W⁺ ∈ Ω⁺(Λ⁺) (second Bianchi identity with s constant). Expanding d^∇(u₁⊗W⁺u₁ + Re(ψ̄⊗W⁺ψ)) with dψ̄ = −α∧u₁ + i b∧ψ̄, du₁=0, and splitting the resulting Λ³⊗Λ⁺-valued equation into (2,1) and (1,2) types gives twelve real equations of which four are dependent (the u₁-component is iK applied to the conjugate of the (1,2) ψ-component). The eight independent equations are

**(E1)** ∂_D η = v α − i η̄ K(α) + i K(∂r),

**(E2)** \overline{∂̄_D η} = −(3r/2) α − 2i K(∂_D v).

Consequences.
- δW⁺=0 fixes the (1,0) derivative of η by r and torsion, and couples the (0,1) derivative of η to the (1,0) derivative of v: |∂̄_Dη + (3r/2)ᾱ|² = 4|∂_Dv|².
- The free first-order data of W⁺ are exactly (∂r, ∂_Dv, ∂̄_Dv): 4+4+4 = 12 real, matching 20−8.
- **Gradient decomposition (pointwise, exact):**
  |∇W⁺|² = 5|∂r − ηα|² + 10|∂_Dv|² + 2|∂̄_Dv + ηᾱ|².
- **Torsion structure equation:** dα − i b∧α = −i√2 [ η̄ u₁ − (q/8) ψ̄ + v̄ ψ ]. Thus the (2,0) curl of α is v̄, the (1,1) part is pure trace η̄ (this is (d_bα)⁻=0 together with d_b*α ∝ η), and the (0,2) part is the algebraic Nijenhuis term.
- **Torsion Laplacian (analyst sign Δ=div grad):**
  Δq = 8trV² − 24|η|² − (3s/2)q − (9/4)q² + 16X,  X = −2 Im⟨α, K(∂_Dv)⟩.
  This identifies the unexplained Step-64 cross term Σ⟨(∇_iW⁺)∇_iu,u⟩ as a coupling between torsion and the (1,0)-derivative of the weight-two Weyl component.

Verification on the complete Bianchi-VIII model (Ric=−3g, s=−12) at p=0.4,0.5,0.6,0.75,0.9: Ricci residual ≤4·10⁻⁴⁰; ∇ψ residual ≤10⁻⁴⁰; α of type (1,0) to 10⁻⁴⁰; |E1|,|E2| ≤ 3.5·10⁻⁴⁰; |∇W⁺|² equals the decomposition to all printed digits (e.g. 23.767074464 at p=0.4); torsion equation residual ≤4·10⁻⁴⁰; ⟨db,ω⟩ = −(2s+q)/4 exactly; Δq formula with X = −2Im⟨α,K∂_Dv⟩ at p=0.4,0.5,0.7,0.9 (residual/16 = −3.0842, −2.1378, −0.17747, −0.0010098 against Im⟨α,K∂v⟩ = 1.5421, 1.0689, 0.088734, 0.00050492). Scope of this check: on the model η and v are real, so coefficients multiplying Im η, Im v are not separately tested; the derivation itself is general.

## 2. Kodaira (vortex) identities with their currents

Because dω=0, for a section f of weight k (Df = df + ikbf):

d( f̄ Df ∧ ω ) = \overline{Df}∧Df∧ω + ik|f|² db∧ω,  \overline{Df}∧Df∧ω = i(|∂f|² − |∂̄f|²) dV.

Hence, pointwise,

**(Kv)** |∂̄_Dv|² − |∂_Dv|² − (|s| − q/2)|v|² = div j_v,  j_v = Re(i v̄ Dv∧ω)^♯,

**(Kη)** |∂̄_Dη|² − |∂_Dη|² − (|s|/2 − q/4)|η|² = div j_η.

Checked as divergences on the model (p=0.5: −3.42287747660327 both sides, difference 10⁻¹⁸; p=0.7: 0.231332805025514, difference 6·10⁻²⁰; same for η).

**End currents on the model.** The flux through the level set p is vol(p)·j(p), vol=√(A₁A₂A₃). At p=0.99, 0.999, 0.9999: vol·j_v = −3.26·10⁻², −3.24·10⁻⁴, −3.24·10⁻⁶ (∝(1−p)²); vol·j_η = −0.722, −0.0720, −0.00720 (∝(1−p)). At the bolt vol→0. **Both Kodaira currents have zero end flux.**

## 3. The complete model is an exact budget for the whole second tier

Radial integrals per unit orbit volume (normalization agrees with Step 77: Q=64), Gauss–Legendre with 24 and 40 nodes, identical to 12 digits. Exact rational values recognized:

| quantity | model value |
|---|---|
| Q=∫q, ∫q² | 64, 512/3 |
| ∫|η|², ∫trV² (=2∫|v|²), T_AK | 16, 16, 32 |
| ∫|∂r−ηα|² | 736/105 |
| ∫|∂_Dv|², ∫|∂̄_Dv|², ∫|∂̄_Dv+ηᾱ|² | 1528/105, 11096/105, 680/7 |
| ∫|∂_Dη|², ∫|∂̄_Dη|² | 32/15, 1408/15 |
| ∫q|v|², ∫q|η|², ∫Re(v̄η²) | 1024/105, 256/15, −64/15 |
| ∫|∇W⁺|² = ∫[18detW⁺ − (s/2)|W⁺|²] | 2624/7 = 2624/7 |

Each second-tier identity holds exactly on the complete model:
- (Kv): 11096/105 − 1528/105 = 9568/105 = 12·8 − ½·1024/105;
- (Kη): 1408/15 − 32/15 = 1376/15 = 6·16 − ¼·256/15;
- Bochner: 5·736/105 + 10·1528/105 + 2·680/7 = 2624/7;
- (★): 48 = 16 + 32.

The coercivity hoped for in Step 77 §4 fails on the model: the v-part of |∇W⁺|² integrates to 10·1528/105 + 2·680/7 = 339.81, while 2|s|∫trV² = 384.

**Proposition 79.1 (scope corrected in Step 80).** The complete model refutes a proposed conclusion obtained from the displayed pointwise AKE identities and inequalities plus exhaustion integrals only when every density is integrable, every relevant end flux vanishes, and no genuinely compact global input is used. Under those hypotheses the same reasoning would transfer to the strict model and could not force q=0. The unweighted Kodaira currents for v and eta, the W+ Bochner current, and the AAD/LeBrun current tested here satisfy those hypotheses. Vanishing flux alone is not sufficient, and the earlier blanket assertion about every polynomial current was not proved. Finite-volume estimates, compact extrema, spectral information, canonical cycles, zero-set topology, and singularly weighted or regularized limits remain outside this negative conclusion.

## 4. Superseded unregularized formulation: the log-torsion identity

**Step-80 correction.** Theorem 79.L below is retained only for zero sets satisfying its explicit integrability hypotheses. It is not the general entrance to the closed problem. The unsupported codimension-at-least-three assertion is withdrawn. A smooth codimension-two stratum with normal model q=c(y)rho^{2m}(1+O(rho)) contributes the distributional residue 4 pi m times surface measure; both 1/q and |d log q|^2 fail locally. At an isolated radial zero, |d log q|^2 is locally integrable for every finite order m, 1/q is integrable only for m=1, and the shrinking flux is O(rho^2), giving no point mass. A real one-dimensional stratum likewise has no residual measure, whereas a real-two-dimensional/complex curve does. The GH-type leading polynomial at a degenerate point does not determine the actual zero set. The globally valid replacement is the epsilon-regularized identity in `step80_regularized_torsion_transport.md`.

Set Λ := Δ log q = Δq/q − |d log q|² on {q>0}. By §1,

−Λ = |d log q|² + (24|η|² − 8trV² + 32 Im⟨α,K∂_Dv⟩)/q + (9/4)q − (3/2)|s|.

**Theorem 79.L.** Let (M,g,J) be a closed almost-Kähler Einstein four-manifold with s<0 that is not Kähler. Assume that near the torsion zero set Z={q=0} one has 1/q ∈ L¹_loc and |d log q| ∈ L²_loc. These hold in particular when every zero is nondegenerate, since then q ≍ dist(·,Z)² by the Step-62 cone, every zero has index +1, and there are exactly 5χ+6τ of them. Then

∫_{M∖Z} [ |d log q|² + (24|η|² − 8trV² + 32 Im⟨α,K(∂_Dv)⟩)/q ] dV = (3|s|/2) V − (9/4) Q.

Using (★) and s²V = 32π²c₁² + 16T_AK, the right side equals (48π²c₁² − 12T_AK − 36∫|η|²)/|s|.

*Proof.* (g,ω) is real-analytic, since Einstein metrics are analytic in harmonic coordinates and ω is harmonic. So q is analytic and Z is an analytic set. Z has empty interior, because q≡0 on an open set gives Kähler everywhere by analyticity.

By the hypotheses, Λ ∈ L¹. Moreover ∫₀^ε(∮_{S_ρ}|d log q|²)dρ < ∞, so along a sequence ρ_k→0 we have ∮_{S_{ρ_k}}|d log q|² = o(1/ρ_k). By Cauchy–Schwarz, ∮_{S_{ρ_k}}|∂_n log q| ≤ (o(ρ_k⁻¹)·Cρ_k³)^{1/2} → 0, and the same argument applies on tubes around one-dimensional strata. Thus ∫_{M∖Z}Λ = 0. Substituting the Δq formula gives the identity. □

Remarks.
1. **Zero geometry (corrected in Step 80).** Isolated zeros contribute no point residue, but codimension-two strata do contribute +4πm times their surface measure. This divisor-type logarithmic residue is not the Euler charge 5χ+6τ. Step 63 excludes only a compact smooth rank-two zero surface without exceptional points; stratified surfaces and isolated degenerate zeros require the common q+ε regularization.
2. **The model end.** The volume term is infinite on the model. On regions {p<P}, the boundary-flux/volume ratio tends to s=-12. Exactly, |d log q|^2 tends to 18, 24|eta|^2/q tends to 12, and the derivative coupling is lower order, so Delta log q tends to s. For every fixed epsilon the regularized end flux vanishes, but its maximum diverges like epsilon^{-2/3} in a layer escaping to infinity; compactness can enter only through control uniform in epsilon.
3. **Sign information on the model.** At p=0.4 and 0.5, −Λ ≈ 8.8 and 11.2, so log q is superharmonic at the sampled points. A closed candidate must instead have ∫Λ = 0. Near a nondegenerate zero ∫_{B_ρ}Λ = 4π²ρ²(1+o(1)) → 0, so the compensating positive part of Λ cannot sit only at zeros: it must occupy a macroscopic region.
4. **Pointwise superharmonicity is not a viable local theorem.** Log q is not superharmonic near zeros. Finite-order nondegenerate zero germs exist through order 8 (Steps 66–71, floating evidence), so a local statement "Λ≤0 wherever q>0" would contradict them. Any proof from Theorem 79.L must be genuinely global.

**Reduced form, superseded by the positive-square identity.** The unregularized expression initially displays -8 trV^2/q and 32 Im<alpha,K partial_D v>/q. Step 80 proves the exact divergence identity
\[
32\operatorname{Im}\langle\alpha,K\partial_Dv\rangle=-32|\eta|^2-12rq-16\operatorname{div}\operatorname{Re}(\eta\alpha).
\]
With the common q+epsilon denominator, it combines with |dq|^2 into the positive square 32|partial r-eta alpha|^2. The remaining frontier is the weighted transport of the other free Weyl-gradient squares, not control of this cross term in isolation.

## 5. The β-budget, its exact place relative to LeBrun 2005, and the sign-family cone

**Theorem 79.β.** Let (M,g,J) be a closed almost-Kähler Einstein four-manifold with s<0, b⁺>1, and β = γ − (s/4)ω. Then β is closed and β(P) = |a_{P⊥}|² ≥ 0 on every J-plane (Step 77). Suppose a ∈ H²(M;ℤ) is such that c₁+2a is (up to sign convention) a nonzero Seiberg–Witten basic class. Then a has a J-holomorphic current for the given J (LeBrun 2005, Cor. 3.5, via Taubes SW⇒Gr), hence β(a) ≥ 0.

For M = X#r CP̄², X minimal of general type with b⁺>1 and K = K₀ + ΣEᵢ:
- LeBrun's Theorem B supplies currents in K₀ and in every Eᵢ;
- β(Eᵢ) = 2π + (|s|/4)ω(Eᵢ);
- 2πβ(K) = T_AK − ∫|η|²₆₂, an identity in cohomology from (★), Gauss–Bonnet and the signature formula.

Therefore

T_AK − ∫|η|² ≥ 4π²r + (π|s|/2) Σᵢ ω(Eᵢ),  s²V ≥ 32π²K₀² + 32π²r + 8π|s|Σᵢ ω(Eᵢ).

*Relation to the literature.* The curvature bound on J-curves (LeBrun Prop. 3.1/Cor. 3.2: s·Area ≤ 8π c₁·C ≤ ∫_C s*) and the curve supply are LeBrun's; his Theorem B uses β(K₀)≥0 before his pinching hypothesis. What is added here is only the exact expression of that inequality in the T_AK − ∫|η|² budget. A02 (#878) observes that the weaker T_AK ≥ 2π²k needs no curves: it follows from s²V = 32π²c₁² + 16T_AK, c₁² = A−k and ∫s² ≥ 32π²A.

*Sign-family cone (Spirit #86).* For b = ε₀K₀ + Σεᵢ Eᵢ, the effective class a = (b−c₁)/2 = ((1+ε₀)/2)K₀ + Σ((1+εᵢ)/2)Eᵢ is a subset sum. So the cone of all sign-family classes is generated by K₀, E₁,…,E_r, and all inequalities β(a)≥0 follow from β(K₀)≥0 and β(Eᵢ)>0. Additional constraints require independent basic classes of X or other actual currents. The b⁺=1 case needs a nonzero chamber invariant or an actual current for K₀ and remains open.

## 6. Status

Established (with the Step-80 correction that the general closed identity is the common-denominator q+ε family, not Theorem 79.L without zero-set hypotheses):
- E1, E2 and the twelve-dimensional free-jet description;
- the |∇W⁺|² decomposition, torsion structure equation and Δq formula with X = −2Im⟨α,K∂_Dv⟩;
- (Kv), (Kη) with explicit currents;
- the exact model budget and Proposition 79.1;
- Theorem 79.L under the stated zero regularity;
- Theorem 79.β under b⁺>1 blowup supply.

Open:
- whether the 1/q-weighted second-tier identities, which retain end flux on the model, force ⟨B⟩ ≠ 3|s|/2;
- the precise residue for degenerate zeros (Step-65 leading forms κ z̄₂^m e₁ vanish on a complex line);
- b⁺=1;
- coupling of Theorem 79.L with Theorem 79.β, using exceptional curves where 2π + (|s|/4)ω(E) is forced, and with the harmonic ASD sector when b⁻ ≥ 1.
