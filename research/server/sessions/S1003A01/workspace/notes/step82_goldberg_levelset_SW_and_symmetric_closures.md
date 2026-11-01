# Step 82 — Closed negative Goldberg: the exact level-set identity, a complete algebraic second tier, the Seiberg–Witten Weyl route on the model, and exclusion of all symmetric closures

Agent2, Execute. Inputs: Steps 77–81, Spirit #89, #95, #97.
Scripts:
- `workspace/scripts/step82_sw_bochner_algebra.py` (exact SymPy algebra)
- `workspace/scripts/step82_sw_model.py`, with output `workspace/data/step82/sw_model.json`

Conventions are those of Steps 62/79–81: s<0 constant, q=|∇ω|², r=s/6+q/4, e=|η|² (vector norm), v=trV², x=ηᵀVη, |W⁺|²=3r²/2+2e+v, X=Re(ηα), Y=∂r−ηα, and the analyst Laplacian.

## 0. Corrections to Step 81 (operative from now on)

1. On the complete model, ∫ε/(q+ε)=∞ for every fixed ε>0, because the integrand tends to 1 on the infinite-volume end. The ε^{-2/3} growth belongs instead to integrable moving-layer quantities such as ∫q/(q+ε).
2. Proposition 81.T applies only to currents whose integrability, decay and end flux on the model are actually verified. It does not classify compact arguments, and it does not make an ε/h-assisted multiplier the only possible route.
3. The claims "Δlog q≈4m/ρ²>0 near every finite-order zero" and the proposed "logarithmic mass balance priced by 5χ+6τ" are withdrawn.
   - Spirit's anisotropic cone jet (c=1, S=diag(3,−1), A=[[0,3],[−3,0]]) has ρ²Δlog q≈−0.181 along the top eigendirection.
   - Neither the signed flux nor the Euler index bounds the positive logarithmic mass or fixes a neighbourhood scale.
   - Only the signed small-sphere flux 4π²mR² survives.

## 1. The amplitude-level flux identity is exactly a Y-density identity

Since s is constant, ∂r=∂q/4. Hence ηα=∂q/4−Y, and as real one-forms

  X = dq/8 − Re Y,  |Re Y|² = |Y|²/2.  (82.1)

Equation (80.3) reads div(∇q−16X)=ρ, with ρ=8(e+v)−|s|q/2+3q²/4. On a level set {q=t} with normal n=∇q/|∇q|,

  ⟨∇q−16X, n⟩ = (|dq|²−16⟨dq,X⟩)/|∇q| = (32|Y|²−16qe)/|∇q|,

using |dq−8X|²=32|Y|² and 64|X|²=16qe. Spirit's identity F(t)−16∫_{q=t}⟨X,n⟩=∫_{q<t}ρ is therefore *exactly*

  (LS)  32∫_{q=t}|Y|²/|∇q| dA = 16t∫_{q=t}|η|²/|∇q| dA + ∫_{q<t}ρ  for every regular t.

Multiplying (80.3) by an arbitrary function f(q) gives the equivalent family

  (82.2)  32∫f′(q)|Y|² = ∫[16f′(q)qe − f(q)ρ].

The cases are:
- f=−1/(q+ε) gives (80.S);
- f=q gives the exact unregularized identity 32∫|Y|²=∫[|s|q²/2+8qe−8qv−3q³/4]. This was checked on the model: both sides equal 224.30476190476… = 32·736/105.
- f=H(t−q), by smooth approximation, gives (LS) with the stated sign.

There is also the exact simplification ρ=−8Z_s, where Z_s is the AAD integrand of §2.

**What this settles.** The "correlation between F(t) and the X-flux" is precisely the relation between the coarea densities of |Y|² and |η|² on the level sets of q. Y is the weight-one component of the twistor part of ∇W⁺, in the decomposition |∇W⁺|²=5|Y|²+10|∂v|²+2|∂̄v+ηᾱ|². The trace equation 16 div(Re Y)−Δq=ρ fixes one real contraction of ∇Y. (82.2) is its complete content when tested against functions of q, i.e. its level-set-averaged content; arbitrary spatial test functions retain more (TTCS verifier, Step 82).

A further restriction would need control of the remaining components of ∇Y. These involve the primitive Hessian of q and ∇(ηα), hence ∂̄η and the jet ∂_Dv through E2, as well as the undetermined symmetric part S of D′α. Neither the trace equation nor the displayed first-order subsystem determines them. This identifies the surviving freedom in the subsystem. It does not prove that the full prolonged Einstein system imposes no further level-set restriction.

**β level-set refinement (no new restriction).** Because β is closed and β(P)≥0 on every J-plane, for every smooth u and regular t one has

  ∫_{u<t}dd^cu∧β = ∫_{u=t}d^cu∧β = ±∫_{u=t}|∇u|β(n,Jn) dA,

with the sign fixed by the boundary orientation.

*Correction (TTCS verifier).* The boundary weight is β on the complex line *tangent* to the level set. On {u=t} choose a tangent frame (Jn,e,Je) with e ⊥_ℂ n. Then d^cu∧β=±|du|β(e,Je)dA=±|du|(q/4)|n_α|²dA, where n_α is the component of n in ℓ_α. The interior density simplifies to dd^cu∧β=((q/4)L_u(ℓ_α)+2⟨du,X⟩)dμ.

For u=q this expresses (t/4)F_α(t), the torsion-line part of the amplitude flux F=F_α+F_⊥, through a sublevel integral. It is the level-set form of 81.I.

At a nondegenerate maximum of q it reduces to L_q(ℓ_α)≤0, which is just the sign of the Hessian. No closed-manifold restriction has been extracted from it.

## 2. The second tier is completely algebraic: identity (82.B)

The following three statements are exact on a closed candidate:
- the W⁺ Bochner identity ∫|∇W⁺|²=∫Bo, where Bo=−(s/2)|W⁺|²+18 det W⁺ and det W⁺=r³/4−rv/2+re/2+x;
- the f=q case of (82.2);
- the AAD balance ∫Z_s=0, where Z_s=|s|q/16−e−v−3q²/32.

Subtract 5|Y|² and Z_s/2. SymPy (`step82_sw_bochner_algebra.py`, with scale s=−1 and dimensions restored) gives

  (82.B)  10∫|∂_Dv|² + 2∫|∂̄_Dv+ηᾱ|² = ∫[ (5|s|/2)trV² + 18ηᵀVη + q|η|² − q trV² − |s|q²/8 + 3q³/16 ].

So the entire non-Y part of the Weyl-gradient energy equals an explicit algebraic integral. On the model the left side is 339.81 (Step 79). The identity explains the Step-79 no-go exactly: its right side is (5|s|/2)∫v plus corrections, and it falls below 2|s|∫v only because of the q-weighted and ηᵀVη terms.

Like every identity built from integrable, decaying local densities, (82.B) holds on the complete model as well. It is a consolidation, not an obstruction.

## 3. A genuinely different global input: LeBrun's Seiberg–Witten Weyl estimate

For b⁺>1 symplectic M and *every* metric, the Seiberg–Witten Weyl estimate reads ∫(s−√6|W⁺|)²≥72π²(c₁⁺)². This input is not a local density identity; it should be read in LeBrun's chamber and normalization before final use.

For a closed AKE candidate:
- s²V=32π²c₁²+16T_AK gives 72π²c₁²=(9/4)(s²V−16T_AK);
- (c₁⁺)²=c₁²+(c₁⁻)_abs²;
- 4π²(c₁⁻)_abs²=‖Hγ⁻‖²≤‖γ⁻‖²=∫q²/32, where H is harmonic projection onto ASD forms.

The estimate therefore becomes

  ∫ψ₀ ≥ 18‖Hγ⁻‖² ≥ 0,  ψ₀=(|s|+√6|W⁺|)² − 9s²/4 + 36(v+3q²/32).

**Exact algebra.** The linear parts at the Kähler point are:

| integrand | coefficient of q | coefficient of e | coefficient of v |
|---|---:|---:|---:|
| Z_s | 1/16 | −1 | −1 |
| ψ₀ | −9/4 | 36 | 54 |
| Bo | 1/32 | −1/2 | 2 |

(Bo also has the term 18x.) The direction v=x=0, e=|s|q/16 is null for all three integrands at first order. The only multiplier making ψ₀ pointwise nonnegative to first order is λ=36 in ψ₀+λZ_s, and ψ₀+36Z_s=(|s|+√6|W⁺|)²−9s²/4+(9/4)|s|q−36e.

Second order along the null direction gives two consequences:
- the SW condition becomes 27Q₂/16+18B₂≥0, which always holds;
- the Bochner condition becomes (5/2)B₂+18C₂≥Q₂/16.

Here Q₂=∫q², B₂=∫b q², C₂=∫c q², with v=bq², x=cq² and |c|≤√(b/2)/16.

So in the small-torsion regime the integrated algebraic constraints are mutually consistent. The only requirement is that W₃⁺ carries energy comparable to ∫q². No contradiction arises from integrated algebra alone.

**Model test** (`sw_model.json`; s=−12; adaptive quadrature):
- ∫q=64, ∫e=∫v=16, ∫q²=170.667, ∫Z_s≈3×10⁻³¹;
- ∫(|W⁺|²−s²/24)=−32=−T_AK.

The SW integrand gives ∫ψ₀=520.134. This exceeds the largest possible harmonic slack 18∫q²/32=96 by a wide margin. ψ₀ is negative only far out on the end (p=0.99: −3.7×10⁻⁵).

**Conclusion.** The Seiberg–Witten Weyl estimate, combined with the AAD balance, the Bochner identity and (82.2), is satisfied by the complete strict model with room to spare. As a closed-manifold mechanism it cannot exclude geometry modelled on the strict Bianchi-VIII metric. Together with §2, every presently available integral input is compatible with that geometry: the local identities, the topological identities, and SW. A proof must use information that the model evades only through its infinite volume or its absence of torsion zeros. Examples are pointwise or unique-continuation structure at torsion zeros, combined with genuinely global objects (canonical currents, harmonic ASD classes, the Euler class of E).

## 4. Exclusion of every symmetric closure (constructive route)

**Proposition 82.H (corrected scope, Step 83, after the Step-82 verifier).** Let M be closed and oriented, and suppose its regular region is a finite union of products I×N with N=Γ\G for a fixed unimodular three-dimensional Lie group G, and g=dt²+g_t with each g_t descended from a left-invariant inner product on G. Assume every omitted stratum has a smooth tubular disk neighbourhood whose unit normal sphere bundle is the adjacent level N. Then all non-SU(2) class-A cases have χ(M)≤0 and admit no Einstein metric with s<0. The SU(2) case is also excluded whenever each nut or bolt supplies a connected subgroup of N_{SU(2)}(Γ) acting isometrically on the regular region.

The original statement (arbitrary locally homogeneous levels, any degenerating strata) is withdrawn: nonorientable bolt normal bundles, lens-space bolts, spherical quotients with complicated finite holonomy, infra-homogeneous flat/Nil/Sol levels not of the form Γ\G, and developing holonomy twisting the homogeneous frames between levels are not covered. The corrected statement covers the Bianchi-VIII model and the standard fixed-lattice class-A closures.

*Proof sketch (under the corrected hypotheses).*
1. The principal part is a finite union of I×N with χ(N)=0, so χ(M)=Σχ(singular strata).
2. Smoothness at a stratum with the stated tubular structure requires the degenerating directions to integrate to a free circle action, or to S³ collapsing at a nut.
3. G=\widetilde{SL}₂: only the Seifert circle acts as a circle; a free action has a hyperbolic base, so χ(stratum)<0.
4. Nil, Sol, Ẽ(2), R³: strata are tori or Klein bottles (χ=0), or no circle collapses.
5. In cases 3–4, χ(M)≤0; a closed Einstein 4-manifold with χ≤0 is flat by Gauss–Bonnet, contradicting λ<0.
6. G=SU(2): under the stated isometry-extension hypothesis the regular-region isometries extend to M and give nonzero Killing fields, forbidden by Bochner when Ric<0. ∎

This closes the standard fixed-lattice symmetric constructive route, not every locally homogeneous closure.

## 5. State of Problem 4 after this Step

The F(t)–X correlation reduces exactly to (LS). The coupled first-order system adds no restriction there, because the trace-free ∇Y is free through ∂_Dv.

The second tier is fully algebraic, (82.B). The SW Weyl estimate is the first genuinely global, non-local input tested, and the model satisfies it with a large margin. Symmetric closures are excluded.

The remaining live mathematical possibilities are:
- pointwise/PDE information at torsion-zero strata (unique continuation, the index-+1 cone, the analytic zero-set structure), joined to the Euler class c₂(E)=5χ+6τ and finite volume;
- curve and current information in the effective cone (the β-budget) beyond LeBrun's classes;
- a nonsymmetric construction.

None of these is reduced to a computation yet. Further identity generation on local densities is not expected to change the closed-manifold conclusion.
