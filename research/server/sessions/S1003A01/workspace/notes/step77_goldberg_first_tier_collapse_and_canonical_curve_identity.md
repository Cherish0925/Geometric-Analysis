# Step 77 — Closed negative Goldberg: collapse of the characteristic identities, the b⁻=0 branch, and an identity on canonical J-curves

Agent2, Explore. Inputs: Step-76 handoff, Spirit #84, LeBrun 2015 (`Einstein-Metrics-Harmonic-Forms-and-Symplectic-Four-Manifolds`, Prop. 1 / Lemma 2) \cite{lebrun2015einstein}, Kim 2023 (`Almost-Kähler-four-manifolds-with-harmonic-self-dual-Weyl-curvature`, Cor. 3–5) \cite{kimalmosta}, the Apostolov–Drăghici survey §7 (ρ̃=ρ*−φ/2) \cite{apostolovcurvature}.
Script: `workspace/scripts/step77_aak_identities_check.py` (exact SymPy; all residuals 0).

## 0. Conventions

(M,g,J,ω) closed, almost-Kähler, Ric=λg, s=4λ<0 constant, |ω|²=2, u=ω/√2. In the orthonormal frame (u,u₂,u₃) of Λ⁺,
W⁺ = [[r, ηᵀ],[η, −(r/2)I+V]], trV=0, Frobenius norms ("step-62 norms"; |η|²₆₂ = ½|W⁺(ω)^⊥|² = ½|η|²₅₉).
∇ω = a⊗φ − Ja⊗ψ, q = |∇ω|² = 4|a|² = 4r − 2s/3, s* = s+q.
T_AK = ∫(trV² + 3q²/32), Q = ∫q, V = Vol.
γ = ρ̃ = curvature form of the first canonical connection on K⁻¹, [γ]=2πc₁ (AD survey (17)): ρ̃ = ρ* − ½φ_T, φ_T(X,Y) = (∇_{JX}ω,∇_Yω) ≥ 0 of type (1,1). For Einstein ρ*=R(ω) is self-dual, giving Kim's formula γ = W⁺(ω)^⊥ + (s+s*)/8·ω + (s−s*)/8·ω̂.

## 1. All first-tier identities are one identity

Pointwise algebra (checked exactly): |W⁺|² = (3/2)r² + 2|η|² + trV², so
|W⁺|² − s²/24 = 2|η|² + trV² + sq/8 + 3q²/32.

**Proposition 77.1.** On a closed Einstein AK four-manifold the following integral statements are identical:
(a) LeBrun's δW⁺=0 identity ∫sW⁺(ω,ω) = 8∫(|W⁺|² − ½|W⁺(ω)^⊥|²);
(b) Chern–Weil for c₁² with the canonical connection (Kim Cor. 3);
(c) the AAD integral balance ∫|W⁺|² = (s²/24)V − T_AK;
(d) Sekigawa's integral formula;
all equal to
(★) |s|Q/16 = ∫|η|² + T_AK.
Exact check: LeBrun integrand = −sq/2 − 8|η|² − 8trV² − 3q²/4; CW density minus topological density = −(2|η|² + 2trV² + 3q²/16 + sq/8). Bianchi-VIII control: 48 = 16+32 (the complete noncompact strict model satisfies (★); its integrands decay).

**Euler class of the torsion bundle.** E = Λ^{0,1}⊗Λ^{0,2} = F⊗det F. Chern roots give c₂(E) = 2c₁(F)² + c₂(F) = (9/4)c₁² − ¼p₁(ad₀F). The difference ∇̃−∇ = −½J∇J takes values in [[Λ^{2,0}]]⊂Λ⁺, so ∇̃ equals Levi-Civita on Λ⁻ = ad₀F. Hence, pointwise as forms,
4π² e(E,∇̃) = (9/4) γ∧γ + ¼(2|W⁻|² + s²/24) dV.
Integration gives 4π²(5χ+6τ) = (7/24)s²V − (9/2)T_AK + ½∫|W⁻|², which is GB + signature + (★). **The c₂(E) transgression contains no information beyond (★)**: the zero degrees enter only through the secondary form Ψ on linking spheres, which is scale-invariant in the torsion amplitude, as Spirit #84 anticipated. The primary transgression bridge is closed.

Exact topological consequences (all equivalent to (★) + GB + signature):
4π²(2χ+3τ) = s²V/8 − 2T_AK,  8π²(χ−3τ) = T_AK + 3∫|W⁻|²,  s²V = 32π²c₁² + 16T_AK.
So T_AK is exactly the excess of the Einstein metric's scalar energy over LeBrun's SW bound 32π²c₁²(J).

## 2. Hodge decomposition (Spirit #84, verified) and the b⁻=0 branch

With β=γ−(s/4)ω and H the harmonic part of γ: H⁺ = (s/4 + Q/(8V))ω + H⁺_⊥, and (step-62 norms)
4π²‖c₁⁻‖² = Q²/(32V) + ‖H⁺_⊥‖² − 2∫|η|².
Combined with (★): ‖H⁺_⊥‖² + 2∫trV² + (3/16)∫q² + Q²/(32V) = |s|Q/8 + 4π²‖c₁⁻‖².
LeBrun's scalar SW estimate is then equivalent to 4π²‖c₁⁻‖² ≤ 2T_AK, and his mixed estimate to the sharper Step-69 form. No reverse inequality exists at this tier.

**The b⁻=0 branch is already closed for Einstein metrics** (Kim 2023, Cor. 4–5): 8π²(χ−3τ) = T_AK + 3∫|W⁻|² ≥ 0, while b⁻=0 gives χ−3τ = 2−2b₁−2b⁺ ≤ 0, hence T_AK=0. Thus Spirit's fake-plane control (non-Einstein) has no Einstein analogue; every closed strict AKE candidate has b⁻ ≥ 1 and χ > 3τ. (Ball quotients are also excluded by LeBrun's Mostow-type rigidity.)

## 3. New global input: integrating over canonical J-holomorphic cycles

**Lemma 77.2 (pointwise).** For a unit J-complex 2-plane P,
γ(P) = s/4 + |a_{P⊥}|²,
where a_{P⊥} is the component of the torsion 1-form normal to P.
Proof: η∈[[Λ^{2,0}]] vanishes on J-planes and the ω-component of ρ* is (s*/4)ω, so ρ*(P)=s*/4. φ_T(P)=|∇_eω|² = 2|a_P|². Hence γ(P)=s*/4 − |a_P|² = s/4 + |a|² − |a_P|². □
Consequently s/4 ≤ γ(P) ≤ s*/4 on all J-planes, and γ−(s/4)ω is a semipositive form on J-holomorphic currents.

**Theorem 77.3 (canonical-cycle identity).** Suppose K = −c₁(J) is represented by a J-holomorphic cycle T = Σ mᵢCᵢ (true for every compatible J when b⁺>1 by Taubes SW⇒Gr plus Gromov compactness; for b⁺=1 when the relevant Gromov invariant of K is nonzero — hypothesis to be checked against \cite{zhang2021moduli,li2025symplectic,likodaira}). Then
T_AK − ∫_M |η|² = 2π ∫_T |a^⊥|² dA ≥ 0.
Proof: ∫_Tγ = 2πc₁·K = −2πc₁², ∫_Tω = −c₁·[ω] = −(sV/2+Q/4)/(2π). Then 2π∫_T(γ−(s/4)ω) = −4π²c₁² + s²V/8 + sQ/16 = 2T_AK − |s|Q/16 = T_AK − ∫|η|² by §1 and (★); the integrand is |a^⊥|² by Lemma 77.2. □
Meaning: the off-diagonal Weyl component η is bounded by the transverse-Weyl/torsion budget, with deficit equal to the torsion normal to the canonical curve. Equality ∫|η|²=T_AK holds iff the torsion is tangent to every component of T. This uses SW/Gr input on the compact manifold and is not implied by (★) or the LeBrun inequalities; the noncompact Bianchi-VIII model, having no canonical cycle, is not a counterexample to any consequence (there ∫|η|²=16 < T_AK=32 anyway).

**Corollary 77.4 (exceptional curves carry torsion).** If C is a J-holomorphic cycle with c₁·C = d > 0 (e.g. every exceptional class on a non-minimal symplectic manifold, which has a J-subvariety for every tame J outside CP²#kCPbar², Chen–Zhang Thm A.4 \cite{chen2024kodaira}), then
∫_C q dA ≥ 8πd + |s|·Area_ω(C).
In particular no torsion-free neighbourhood of such a curve exists. Together with s²V ≥ 32π²c₁²(X_min) (LeBrun, \cite{lebrun1999kodairaa}) and §1, an AKE metric with s<0 on X#kCPbar² must have T_AK ≥ 2π²k. The upper bound γ(P) ≤ s*/4 is presumably the mechanism of LeBrun 2005 ("Einstein metrics, symplectic minimality and pseudo-holomorphic curves", \cite{lebrun2005einstein}, only metadata retrieved); novelty of Theorem 77.3 relative to that paper is not yet checked.

## 4. What the second tier must supply

Bochner for harmonic W⁺ (exact algebra verified): ∫|∇W⁺|² = ∫[(9/8)r²q + (s/2+9q/4)|η|² + (−2s−9q/4)trV² + 18ηᵀVη]. Writing W⁺ = r(3/2 uuᵀ − ½I) + Z, the AK conformality (∇u)(∇u)ᵀ = |a|²I kills the ⟨V∇u,∇u⟩ cross term, leaving
∫[(3/2)|dr|² + (9/8)r²q + |∇Z|² − 6⟨dr,⟨∇u,η⟩⟩ + 6r⟨∇u,∇η⟩] = ∫[(s/2+9q/4)|η|² + (2|s|−9q/4)trV² + 18ηᵀVη].
For s<0 the RHS contains +2|s|∫trV²; a contradiction needs a lower bound of order 2|s|∫trV² on ∫|∇V|². V is a section of [[K^{±2}]]; the almost-Kähler Kähler/vortex identity gives ∫|∂̄v|²−∫|∂v|² proportional to −∫⟨γ,ω⟩|v|² = ∫((2|s|−q)/4)|v|² (constant to be fixed), which heuristically supplies only a fraction of 2|s| unless δW⁺=0 also controls the ∂-component. Any argument built from local identities plus integration by parts alone holds on the complete Bianchi-VIII model (finite integrals) and so cannot prove Goldberg; a proof must use compact global input — finite volume in the topological identities, Hodge projections (b⁻≥1), and J-curves (Theorem 77.3). The concrete next problem: couple Theorem 77.3 (torsion normal to the canonical curve) with the zero set of torsion (charge 5χ+6τ) and with b⁻≥1 harmonic ASD forms, or show that these inputs remain jointly consistent with T_AK>0.

## 5. Status

Established: Prop. 77.1 (collapse; exact), Euler-form identity, Hodge identity, b⁻=0 closure (Kim), Lemma 77.2, Theorem 77.3 under the stated curve-existence hypothesis, Corollary 77.4. Open: exact vortex constant and the full δW⁺=0 component system in (r,η,V,a); interaction of the canonical cycle with torsion zeros; novelty versus LeBrun 2005.
