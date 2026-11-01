# TTCS Independent Branch Record

```json
{
  "step_id": 58,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/spirit_step57_rational_branch_and_global_tests.md",
    "Sessions/S1003A01/workspace/notes/step57_bianchiVIII_strict_AKE_negative.md"
  ]
}
```

## Task

Analyze the two endpoints of the explicit rational Bianchi-VIII metric/form in spirit_step57_rational_branch_and_global_tests.md. Determine what is needed for a rigorous smooth bolt extension under the stated SL(2,R) structure equations and period convention, including the isotropy weights and smooth extension of Omega, and derive the far-end completeness/ACH asymptotics from the formulas. Flag any topology or period assumptions not established. Explain what the exact torsion profile implies—and does not imply—for the closed negative-scalar Goldberg problem.

## Output

# Verification memo: endpoints of the rational Bianchi-VIII AKE pair, and what the torsion profile says about the closed s<0 Goldberg problem

## 0. Main conclusions

- **Bolt end.** The bolt extension is fully determined by the Lie algebra. With n=(−1,1,1), the collapsing generator has period exactly 2π in SL(2,R). The isotropy weights are:
  - 1 on the normal plane;
  - 2 on the bolt tangent plane;
  - 4 on the trace-free metric part;
  - 1 and 3 on the mixed 2-forms.

  The rational formulas meet every resulting parity and vanishing condition. This includes the slope A₁=t²+O(t⁴) and the correct placement of the mixed part of Ω.
- **What smoothness and completeness still rest on.** They are rigorous modulo exact symbolic verification of Ric=−3g and dΩ=0 for the displayed rational formulas. Both are finite rational-function identities in p.
- **Far end.** The far end is complete with t ≈ −(1/√2)ln(1−p). The flow converges to the exact Bianchi-II equilibrium that represents the complex-hyperbolic horosphere metric with Ric=−3g. Ω converges to its Kähler form, and the Reeb field is the hyperbolic generator E₂.
- **Integral balance.** I recomputed the conditional integral balance exactly. It holds, with per-orbit integrals 32, 32, 32 and 96.
- **Closed problem.** The torsion profile rules out purely local proofs of the closed s<0 Goldberg statement. It gives no closed example and no obstruction, and it says nothing about the local structure at a Nijenhuis zero. Such zeros are topologically forced on closed examples, with algebraic count 5χ+6τ ≥ χ > 0.

## 1. Lie-algebra conventions and the period

dσᵢ=2nᵢσⱼ∧σₖ with n=(−1,1,1) and dσ(X,Y)=−σ([X,Y]) on left-invariant fields gives

[E₂,E₃]=2E₁, [E₃,E₁]=−2E₂, [E₁,E₂]=−2E₃.

A concrete realization is E₁=[[0,1],[−1,0]], E₂=diag(1,−1), E₃=[[0,1],[1,0]]. I checked all three brackets.

- **Period of E₁.** exp(sE₁) is rotation by s. Hence exp(2πE₁)=I and exp(πE₁)=−I.
- **Adjoint action.** ad E₁ maps E₂↦−2E₃ and E₃↦2E₂. In the coordinate w=c₂+ic₃ on p=span(E₂,E₃), Ad(exp sE₁) acts by w↦e^{−2is}w.
- **E₂ is hyperbolic.** ad E₂ has real eigenvalues ±2.

**Model space.** M_Γ = Γ\SL(2,R) ×_K C, where K=exp(RE₁) acts on C by a character of weight ±1. The left-invariant σᵢ descend under left Γ, and the collapsing circle is right K-translation.

The slope condition a₁′(0)=1 with σ₁(E₁)=1 is exactly the 2π period. The alternatives behave as follows:

- **PSL(2,R), or any Γ containing −I.** The fibre has period π, and the bolt becomes a cone angle π (a Z₂ orbifold locus).
- **Universal cover of SL(2,R).** E₁ does not close, so no bolt can be added.

The slope is not forced by the Einstein ODE. Near a collapsing circle, the leading terms of h₁′=−h₁S+… cancel for any slope k in a₁~kt. The exact value k=1 is therefore an output of the 1-parameter curve V(P)/scaling.

## 2. Bolt end (p→1/3)

### Analyticity in t²

Write δ=p−1/3. The quantity √G equals δ^{−1/2} times a function analytic in δ and positive at δ=0. Integrating gives t = δ^{1/2}·(analytic, nonzero). Hence δ is an analytic function of t², with δ=2t²/9+O(t⁴).

I rechecked the stated limits: G≈9/(8δ), A₁≈(9/2)δ=t², A₂, A₃→6.

Every rational function of p that is regular at 1/3 is therefore an even analytic function of t.

### Metric (Eschenburg–Wang)

Isotropy at a bolt point is K. It acts with weight 1 on the normal plane and weight 2 on p. Equivariant smooth maps into a weight-m representation restrict to the ray as t^{|m|}·(even). The conditions are:

- **Collapsing direction.** A₁ must equal t²·(even) with leading coefficient 1. This holds exactly.
- **Weight-0 part.** A₂+A₃ must be even. This holds.
- **Weight-4 part, A₂−A₃.** It must be t⁴·(even). The factor (3p−1)²=9δ² supplies this. I rechecked that the leading coefficient is (135/2)δ²=(10/3)t⁴.
- **Cross terms.** The metric is diagonal, so there are none.

**Extra facts at the bolt.**
- Since A₂ and A₃ are even, the bolt is totally geodesic.
- The metric σ₂²+σ₃² on G/K has curvature −4. Indeed, the Levi-Civita connection form is 2σ₁ and d(2σ₁)=−4σ₂∧σ₃.
- The bolt metric 6(σ₂²+σ₃²) therefore has K=−2/3. For a closed genus-g bolt its area is 6π(g−1).

### The form Ω

Ω = x₁(dt∧a₁σ₁ + a₂a₃σ₂∧σ₃) + x₂(dt∧a₂σ₂ + a₃a₁σ₃∧σ₁),

with X₁=1−X₂ and X₂=(8/3)t²+O(t⁴), which I rechecked.

**Smooth frame on the ray.** Take the ray at g=e and weight +1, so that σ₁=dθ there. Then dt=dx and tσ₁=dy. Write z=x+iy (weight +1) and dw=σ₂+iσ₃ (weight −2).

- **x₁-term.** It equals x₁[(a₁/t)dx∧dy + a₂a₃σ₂∧σ₃]. This is weight 0 with even coefficients, so it is smooth when x₁ is the positive even root.
- **x₂-term.** It equals c₊Re(dz∧dw) + c₋Re(dz∧dw̄), where
  - c₊ = x₂(a₂ + a₃a₁/t)/2;
  - c₋ = x₂(a₂ − a₃a₁/t)/2.
- **Weights of the mixed forms.** dz∧dw has weight 1−2=−1. dz∧dw̄ has weight 1+2=3. Smoothness therefore requires c₊ = t·(even) and c₋ = t³·(even).
- **Both conditions hold.** Take x₂ = t·√(X₂/t²), an odd function. Then c₊ ~ 2√6·√(8/3)·t/2 ≠ 0. Also a₂ − a₃a₁/t = O(t²) is even, so c₋ = O(t³) is odd.

With weight −1 one finds σ₁=−dθ, and the same assignment results. The conclusion does not depend on the sign of the character.

**This is a genuine structural check.** The O(t) piece lands in the weight-1 slot only because of two things together: n₁=−1, and the specific combination e₀∧e₂+e₃∧e₁. With the opposite sign of n₁, or of that combination, the O(t) part would sit in weight 3, and Ω would not extend. The note's remark that x₂=O(t) and Ω→w₁ is not a proof is correct. The decomposition above is the proof.

**Leading-order closure checks.** I checked the closure equation (x₂a₃a₁)′ = 2n₂x₂a₂ at leading order:
- at the bolt, both sides are 64t³;
- at the far end, both sides are 128√2/(3ε²).

The x₁ equation is consistent at the far end, where both sides are O(ε).

### Topology of the bolt (derived, sign to be cross-checked)

- **Normal bundle.** TΣ = P ×_K C_{−2} has degree 2−2g. The normal bundle N = P ×_K C_{+1}, oriented by dt∧σ₁ (the Ω-orientation), therefore has degree g−1. Equivalently N² ≅ K_Σ: the normal bundle is the square root of the canonical bundle selected by the lift Γ ⊂ SL(2,R), i.e. a spin structure.
- **Circle bundle check.** |deg| = g−1 also follows from Γ\SL(2,R) being the double cover of T¹Σ.
- **Self-intersection.** In the Ω-orientation, Σ·Σ = g−1. The Ω-orientation agrees with dt∧σ₁∧σ₂∧σ₃.
- **Adjunction.** Σ is J-holomorphic because x₂=0 there. Adjunction then gives c₁·Σ = 1−g.

The sign of the degree rests on weight bookkeeping. It deserves an independent check, for example via the curvature of the connection σ₁ restricted to the normal circle.

## 3. Far end (p→1)

Write ε=1−p. The leading asymptotics are:

| Quantity | Leading term |
|---|---|
| G | 1/(2ε²) |
| A₁ | 8/(3ε) |
| A₂ | 32/(3ε²) |
| A₃ | 8/ε |
| X₁ | ε³/4 |
| q | (9/2)ε³ |
| dV/dp | (32/3)ε^{−3} |

All corrections are analytic in ε.

**Completeness.**
- dt/dε = −(1/(√2ε))(1+O(ε)), so t = −(1/√2)ln ε + c + O(ε). Every curve to infinity has length at least Δt.
- For cocompact torsion-free Γ, the sets {t≤T} are compact. M_Γ is therefore complete, and every other quotient is complete by covering.
- **Match with Step 57 numerics.** The predicted t-increment per factor 10³ in the cutoff is ln(10³)/√2 = 4.885. Step 57 reports 4.93 and 4.89. This agrees, because dp/dφ ≠ 0 at φ=−2π/3.

**Rates and the equilibrium.**
- a₁ ~ e^{t/√2}, a₂ ~ e^{√2t}, a₃ ~ e^{t/√2}. Hence h → (1/√2, √2, 1/√2) and a₃/a₁ → √3, matching Step 57.
- In W-variables: W₂² = A₂/(A₁A₃) → 1/2. W₁ and W₃ are O(ε).
- **Comparison with the exact equilibrium.** The Bianchi-II flow with Ric=−6g has the exact equilibrium a₁=e^{2t}, a₂=a₃=e^{t}, i.e. h=(2,1,1) and W=(1,0,0). Inserting this into the stated ODE system:
  - h₁′=0 forces W₁²=1;
  - the constraint gives Q=6.

  This is the CH² horosphere with holomorphic sectional curvature −4. Rescaled to Ric=−3g, it becomes h=(1/√2, √2, 1/√2) and |W_Reeb|=1/√2.
- **Conclusion.** The orbit converges to exactly this equilibrium, with W₂ playing the Reeb role. The normalization of the θ² coefficient against the Levi form is then automatic.
- **Error rates.** Relative errors are O(e^{−√2t}), which is O(e^{−2r}) in the holomorphic-curvature −4 normalization (r = t/√2).

**Volume growth.** dV/dt ~ ε^{−2} ~ e^{4r}, which is the CH² rate.

**Ω at infinity.** Ω tends to e₀∧e₂ + e₃∧e₁, the model Kähler form (radial paired with Reeb, plus the contact-plane area). Along the way:
- x₁ ~ e^{−3t/√2};
- q ~ e^{−3√2t}.

**Conformal infinity.**
- The underlying manifold is Γ\SL(2,R), compact for cocompact Γ.
- The contact form is σ₂ (dσ₂ = 2σ₃∧σ₁), with contact plane span(E₁,E₃).
- The CR structure satisfies JE₃ = ±√3E₁, which is compatible with the conformal class σ₁²+3σ₃².
- The Reeb field E₂ is hyperbolic. So the Reeb flow is the lift of a geodesic-type flow on T¹Σ, not the fibre rotation.

Calling the end "ACH" in Biquard's sense uses only these leading terms and the O(ε) corrections. Both follow from analyticity in ε.

## 4. Exact consistency checks on the Spirit note

- **The exact point is p=1/2.** At p=1/2 one gets u = −1/15 and v = 192/245, and X = (5/32, 27/32), matching §1 of the note.
- **Scale of q.** q(1/2) = 972/343 in the Ric=−3 normalization. Rescaling by λ ratio (256/105)/3 gives 27648/12005, the note's value. The two sections are consistent.
- **Positivity of X.** X₁+X₂ = 16p³/16p³ = 1 is confirmed by expansion.
- **Bolt torsion.** q(1/3) = 32/3, consistent with the numerical maximum 10.7. q′<0 on (1/3,1), so q is strictly monotone along the orbit space and has no interior zero.
- **ODE existence is unnecessary.** Given the explicit p-formulas, the local ODE existence argument in §1 of the note is no longer needed. Exact certification of Ric+3g=0, dΩ=0 and W⁻=0 (in the stated chirality) on these formulas would replace all the 1e−12 numerics.

## 5. Topology and period inputs the files do not yet establish

1. **Group of the principal orbits.** It must be SL(2,R), or Γ\SL(2,R) with −I ∉ Γ. Torsion-free Γ suffices.
   - Elliptic elements in Γ give orbifold points on Σ.
   - The "Γ ⊂ SL(2,R) with σ₁-circle 2π" of Step 57 is correct only under this choice.
   - A cocompact Γ must be a lift of a surface group, i.e. a spin structure. There are 2^{2g} such lifts.
2. **Γ is optional.** Γ = {1} gives a complete metric on SL(2,R) ×_{SO(2)} C ≅ R⁴. Finite-area Γ gives a noncompact bolt. The phrase "disk bundles over closed hyperbolic surfaces" is one choice, not a consequence.
3. **Normal degree.** The normal degree g−1 is derived in §2. Its sign relative to the Ω-orientation is unverified.
4. **Exact identities.** The Einstein, closure and W⁻=0 identities for the rational formulas are not yet exact.
5. **Literature identification.** Armstrong 2002, an ansatz for AK Einstein metrics, is a direct candidate. Only its metadata is available, so identification with that ansatz is unresolved.

## 6. Torsion profile and the closed s<0 Goldberg problem

### Exact integrals

All integrals are per unit invariant orbit measure, on p ∈ [1/3,1]. With w = 1+3p²:

| Integrand (times dV/dp) | Simplified form | Integral |
|---|---|---|
| q | 768p/(1+3p²)² | 64 |
| q² | 27648p(1−p²)³/(1+3p²)⁵ | 512/3 |
| \|η\|² | 384p(9p²−1)/(3p²+1)³ | 32 |
| 2\|W₃⁺\|² | 1728p(1−p²)(9p²−1)²/(3p²+1)⁵ | 32 |

The balance therefore reads 32 + 32 + (3/16)(512/3) − (3/2)·64 = 32 + 32 + 32 − 96 = 0. I independently confirm Spirit's exact zero. It remains conditional on W⁻=0 and the chirality.

The coefficient −3/2 equals s/8 at s=−12. This is consistent with the integrand being |η|² + 2|W₃⁺|² + 3q²/16 + sq/8. That form is an inference from the numbers, not a derivation.

### What this implies

- **Local arguments cannot work.** A smooth complete strict AKE metric with s<0 exists, with q>0 everywhere. No pointwise or jet-level identity can force q=0. Any proof for closed manifolds must use compactness or finite volume. The example has infinite volume and an ACH end.
- **The integrand has no sign.** At the bolt it equals 16/3 > 0, since q > 8 there. Near infinity it tends to −24 per dp. The Sekigawa-type mechanism that settles s ≥ 0 therefore has no positivity to exploit. The example realizes the zero balance with zero flux at infinity.
- **A conditional bound on closed examples.** If the displayed identity holds on closed AKE manifolds with s<0, then:
  - ∫q² ≤ −(2s/3)∫q, which is 8∫q at s=−12;
  - by Cauchy–Schwarz, the mean of q is at most 8.

  This is an upper bound on torsion, not an obstruction. The example has ∫q²/∫q = 8/3.
- **Zeros of N are forced, with a definite count.** N is a section of Λ^{0,2}⊗T^{1,0} ≅ K⁻¹⊗T^{1,0}, whose c₂ equals c₂ + 2c₁² = 5χ + 6τ. On a closed Einstein manifold with s ≠ 0:
  - Hitchin–Thorpe (|τ| ≤ 2χ/3) and χ > 0 for non-flat Einstein give 5χ + 6τ ≥ χ > 0;
  - so N must vanish, with algebraic zero count 5χ+6τ.

  This reproduces the inherited argument. Ω is harmonic and the metric is analytic, so q is real-analytic and its zero set is an analytic subvariety.

### What this does not imply

- **No obstruction from quotients.** The example has no compact quotient. q is invariant under symmetries of the pair, has infimum 0, and that infimum is not attained. This says nothing about other closed AKE metrics.
- **No model of a Nijenhuis zero.** The profile has no zero, so it carries no information about a germ at a point where N vanishes. Its torsion decays only at infinity, like e^{−3√2t}. Heuristically, the required zero count escapes to the ACH end. A relative Euler number of N against its asymptotic frame would make this precise, but it has not been computed.
- **No energy bound for zeros.** Topology fixes the count of zeros, not a lower bound on their curvature cost.
- **Nothing for the Einstein gap.** The example is exactly Einstein, so D=0 on a noncompact manifold. It gives no information about α(M) for closed M.

### What would decide the closed problem

- The local structure of AKE metrics with s<0 near a zero of N: vanishing order and form of the zero set.
- Or a global identity in which the zero count 5χ+6τ enters with a sign that the integral balance above cannot absorb.