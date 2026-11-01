# TTCS Independent Branch Record

```json
{
  "step_id": 62,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md",
    "Sessions/S1003A01/workspace/notes/step59_chiral_completion_and_zero_charge.md",
    "Sessions/S1003A01/workspace/notes/step60_kahler_rigidity_weyl_pinching_goldberg.md",
    "Sessions/S1003A02/workspace/notes/step75_Q4_half_twistor_torsion_and_zero_index.md"
  ]
}
```

## Task

Closed negative Goldberg problem (closed 4-manifold, Einstein Ric=lambda g with lambda<0, almost-Kahler Omega; does Omega have to be Kahler?). New local result (attached note): at every torsion zero, |nabla^2 Omega|^2 = 4trV^2 - 12|eta|^2, so the first torsion jet lies on the cone ||A||^2=8|c|^2+||S||^2 and every nondegenerate zero has index +1; W3+ != 0 at every zero with nonzero first jet; the identity is lambda-independent and Ricci-flat Gibbons-Hawking degenerate zeros lie on it. Topology forces total torsion charge 5chi+6tau>0. Propose the strongest concrete next mathematical mechanisms that could turn this into a global obstruction or, conversely, into a construction of a negative-scalar closed or local counterexample germ with an isolated zero. Candidates to evaluate rigorously, not just list: (a) a next-order (cubic/third-jet) identity obtained from Delta^2 of the Weitzenbock identity or from Bianchi relations between nabla^2 W+ and nabla^3 Omega, and whether lambda can enter there; (b) a pointwise elliptic inequality for q or for |nabla Omega| near zeros (e.g. Delta q >= ... using the global AAD Weitzenbock), giving a maximum-principle or Morse/Poincare-Hopf argument tied to the forced positive charge; (c) combining index +1 with the localization of zeros in {lambda_min(W+)<=s/6} and the Hopf/linking-sphere picture; (d) a model local negative AKE germ with an isolated nondegenerate zero (e.g. a cohomogeneity-one or toric ansatz with a fixed point) that would show the local theory cannot close Goldberg. For each, state precisely what would have to be computed and what result would change the global judgment.

## Output

# Torsion zeros of Einstein almost-Kähler 4-manifolds with λ<0: mechanisms beyond the first-jet cone

Notation follows Steps 59–62 and A02 Step 75. T = ∇Ω, q = |T|², and D = ∇^bα is the gauge-covariant torsion derivative. By Theorem 75.H, D has components c (trace part, η), A (antisymmetric part, W₃⁺ plus a quadratic |a|² term) and S (symmetric part, free) at **every** point, not only at zeros. The determinant formula det_ℝD = |c|⁴ − |c|²(‖S‖²−‖A‖²) + |det B|² therefore holds pointwise everywhere. The cone (2.1) is the q = 0 specialization.

## 0. Three structural facts that reorganize the problem

**Weighted grading of the jet system.** Give x weight −1, λ weight 2 and the k-th jet j_k of T weight k+1. W⁺ then has weight 2 (it is linear in j₁ plus the constant s/6 part), ∇W⁺ weight 3, and ∇²W⁺ weight 4.

- **Weight 4.** Theorem 62.A is the weight-4 relation: Q(j₁) is balanced against the free trace-free part of ∇²W⁺ (linear in j₃), and only the trace survives. A term λ·(linear in j₁) is allowed by weight but is absent; it cancels algebraically.
- **Weight 5.** The allowed terms are λ·j₂, j₁·j₂ and j₄. These are odd in jets in a way that can only fix j₂ and j₄ relative to j₁.
- **Weight 6.** This is the first weight at which a **λ-dependent quadratic restriction on j₁** can appear, of the form λ·Q₂(j₁) + C₃(j₁) + (terms in j₂, j₃, j₄). A restriction survives on L only if the higher-jet terms cannot absorb it, as the trace-free ∇²W⁺ absorbed Spirit's source at weight 4.
- **Structure of any such restriction.** Its j₁-part must be a U(2)-invariant polynomial on L = c ⊕ A ⊕ S. The invariant quadratics are |c|², ‖A‖², ‖S‖², so any restriction is λ(β₁|c|²+β₂‖A‖²+β₃‖S‖²) + (invariant cubic) on the cone.
- **Consequence for λ.** The relation is inhomogeneous under j₁ → tj₁. For λ≠0 it would force a quadric condition on small jets that is absent at λ=0. This is the precise sense in which the sign of λ can first act locally.

**Index-blindness is lifted for nondegenerate zeros.** A02 §3(ii) showed that singular-weight Bochner arguments only see |det Df|. Corollary 62.C makes every nondegenerate zero index +1, so |det|-weighted counts now coincide with the topological count. The remaining sign ambiguity lives entirely in the degenerate stratum: c = 0, |det S| = ‖S‖²/2, det S = −a², i.e. det B = det S + a² = 0. The Ricci-flat Gibbons–Hawking zero lies there.

**The complete Bianchi-VIII/Fino pair is a universal test object for pointwise inequalities.** q attains its maximum 32/3 at the bolt, an interior point. So any universal F = F(q, |W⁺|², η, W₃⁺, …) with an interior maximum on the pair cannot satisfy ΔF ≥ 0 there. This extends the decay principle (Step 75 §3(iii)) from integral identities to maximum principles: candidate subharmonic quantities can be screened exactly on the pair before any closed-manifold argument.

## (a) Next-order identities: what Δ² and the Bianchi relations can and cannot give

**The pointwise identity behind Theorem 62.A.** Away from zeros, with u = Ω/√2 and Δ the analyst's Laplacian,

Δq = 4Δr,
Δr = ⟨ΔW⁺u,u⟩ + 4⟨∇_iW⁺∇_iu,u⟩ + 2⟨W⁺Δu,u⟩ + 2⟨W⁺∇_iu,∇_iu⟩,

with ΔW⁺ = (s/2)W⁺ − 6W⁺² + 2tr(W⁺²)Id and Δu = −(2W⁺u − (s/3)u). Every term is algebraic in (s, q, η, V) except two:

- the cross term 4⟨∇W⁺·T, u⟩, which is bilinear in a curvature jet and T;
- the quadratic term ⟨W⁺T,T⟩, whose s/6 part carries λ.

**Global cone identity.** Rewriting |∇T|² through (c, A, S), the same identity reads

‖A‖² − 8|c|² − ‖S‖² = 𝓡,

where 𝓡 is an explicit expression vanishing at T = 0. 𝓡 is linear in T times (∇W⁺, η, V, s) plus quadratic in T times W⁺. The exact form of 𝓡 should be written down, including its sq-type term. Off the zero set it controls the sign of det D through the determinant formula:

- Near a nondegenerate zero, det D ≥ 25|c|⁴ − O(|α|·|j|³), so D stays invertible on a neighbourhood whose size is set by 𝓡.
- Wherever 𝓡 is dominated by the cone terms, the global analogue of Corollary 62.C holds.
- This identity, not Δ² at a single point, is the object connecting the zero analysis to the critical-point topology in (b).

**Δ² of the Weitzenböck identity at a zero.**

- *At a zero with nonzero first jet.* Δ²q(p) contains a bilinear pairing of j₁ with ∇²W⁺. Through the Ricci identity this is j₁ paired with j₃. The trace-free part of ∇²W⁺ is free, so the scalar Δ² identity alone cannot restrict j₁. It can only fix one contraction of j₃.
- *At a zero of order ≥ 2* (T(p) = ∇T(p) = 0, so W⁺(p) is of Kähler type). Since T(p) = ∇T(p) = 0, Δ²q(p) is a positive quadratic form in ∇²T(p) alone. On the right, the Derdziński quadratic map vanishes identically at the Kähler-type spectrum (s/6, −s/12, −s/12): the u-entry is −s²/12 + s²/6 − s²/12 = 0, and the other entries are s²/24 + s²/24 − s²/12 = 0. Also Δu(p) = 0 and ∇u(p) = 0. So Δ²r(p) reduces to −12∇W⁺∇W⁺ + 4|∇W⁺|²Id paired with u⊗u, plus ∇W⁺ paired with ∇²T.
- Every surviving term has weight 6 with no factor of s. The order-2 zero identity is therefore again **λ-independent**: a homogeneous quadratic relation between ∇²T(p) and ∇W⁺(p). The latter is tied linearly to ∇²T(p) by the Ricci identity, so the identity is a quadratic form Q on the second jet. Whether Q is definite on the admissible second jets is an algebra problem of the same size as Step 62.
- Where this leads: if Q is definite, zeros of order exactly 2 cannot exist, and the next order must be computed. Continuing, every finite-order zero has a leading identity of this type. Note that infinite-order vanishing already forces local Kählerness.

**Where λ can enter.** By the grading, λ can only enter at weight 6 through λ·Q₂(j₁). This happens at nondegenerate zeros, not at higher-order ones. The scalar identities do not isolate it because of the free j₃ coupling. The decisive object is the full projection of the D = 5 and D = 6 compatibility varieties onto L, for λ = −1 and λ = 0. The jet engine of Step 62 is the right tool.

What to extract from that computation:

- **The image V_D ⊂ L.** If it stays the full cone, there is no local restriction at weight 6. If it is cut, the cut must be fitted to the invariant form λ(β₁|c|² + β₂‖A‖² + β₃‖S‖²) + C₃.
- **The fibre dimensions over cone points.** These give the Hilbert function of the prolonged system. Its stabilization identifies the involutivity order needed for (d).

A λ-dependent cut that removes all nondegenerate jets at λ<0 but not at λ=0 would be the first genuinely sign-sensitive local mechanism. It would shift all weight onto the degenerate stratum. That stratum lies in the cone even at λ=0 (GH), so the order-2 identity and the index of degenerate zeros would then decide the problem.

## (b) Elliptic inequalities and Morse/Poincaré–Hopf for q

**Maximum principles for q.** No pointwise inequality Δq ≥ P(s,q,η,V) without gradient terms follows from the Weitzenböck identity, because of the cross term 4⟨∇W⁺·T,u⟩. Absorbing it by F = q + β|W⁺|² gives ΔF ≥ (algebraic polynomial) using Δ|W⁺|² = 2|∇W⁺|² + ⟨ΔW⁺,W⁺⟩. At a maximum of F this yields a pinching bound, not a sign. By §0, any such F is ruled out as a subharmonic quantity if it peaks at the bolt of the pair. So maximum principles can give a priori bounds but cannot give Goldberg.

**The useful mechanism: Poincaré–Hopf for ∇q.** Write ∇q = 2D*α.

- Every isolated torsion zero is an isolated strict minimum of q, so it has gradient index +1 regardless of its T-index.
- A critical point with q > 0 requires D* to have α in its kernel, hence det_ℝD = 0.
- With N the number of zeros, Poincaré–Hopf for ∇q gives a sum over critical components with q > 0 equal to χ − N. Rewriting with Σ ind_T = 5χ+6τ:

  Σ_{crit, q>0} ind = −2(2χ+3τ) + Σ_{Z}(ind_T − 1) = −(1/2π²)∫(2|W⁺|² + s²/24) + Σ_{Z}(ind_T − 1).

- If all zeros are nondegenerate, the strict critical set of q must carry Euler charge exactly −2(2χ+3τ) < 0. This is the Hitchin–Thorpe quantity.

**How the pair absorbs this charge.** Charge can be carried by isolated critical points of odd Morse index, or by Morse–Bott critical surfaces C with even normal index contributing χ(C) < 0. The complete pair realizes the second option exactly: its bolt Σ_g is a Morse–Bott maximum of q with contribution 2 − 2g < 0. So no local theorem can forbid this charge carrier.

**Consistency picture for a "pair-like" closed counterexample.** Assume:

- all zeros are nondegenerate;
- the only strict critical set of q is one J-holomorphic maximum curve C;
- C satisfies the pair's normal relation N² = K_C.

Then:

- Adjunction gives C² = K·C = g − 1.
- Poincaré–Hopf requires 2g − 2 = 2K².
- Hence K² = g − 1 = C² = K·C. The Hodge index inequality K²·C² ≥ (K·C)² is an equality, so C ≡ K numerically.

This is not an obstruction but an architecture: q minima at 5χ+6τ points, and q maximal on a canonical-class curve. It is the shape a construction would have to take. The test is whether the holomorphicity of maximal critical surfaces of q, or the relation N² = K_C, follows from the AKE equations at a Morse–Bott maximum. The bolt computation of Step 59 supplies the model.

**Pointwise theorem that would close the problem.** It would suffice to show that at every critical point of q with q > 0, Hess q is J- or I-Hermitian (so isolated Morse indices are even) **and** that critical surfaces have χ ≥ 0. The pair shows the second half must use compactness.

**Cheap computations for (b):**

- Evaluate det D, the components (c, A, S) and Hess q along the pair. Check whether det D vanishes only at the bolt, and whether ‖S‖ ever dominates.
- Compute the J-anti-invariant part (Hess q)'' at the bolt.

## (c) Index +1, localization in {λ_min ≤ s/6}, Hopf linking, and the nonlocal partner

**The purely topological combination is inert.** 5χ+6τ index-+1 zeros can sit in small balls inside Σ₋. Each linking 3-sphere carries Hopf degree +1 for the opposite structure I, which therefore fails to extend at each zero. Nothing contradicts this. Any content must be quantitative and sensitive to λ.

**Where λ enters near a zero.** Near a zero, identity (1.3) gives

|W⁺|² − s²/24 = |η|² + |W₃⁺|² + (s/8)q + (3/32)q².

For s < 0, the −|s|q/8 term is the only place where the sign of λ enters near a zero. Both |η(p)|² + |W₃⁺(p)|² and q ≈ |Df·x|² are quadratic in j₁. So, to leading order, the Weyl-excess region {t > 1} around a zero (t = √24|W⁺|/|s|) has radius of order 1/√|s|, independent of jet size. The higher-order corrections are small only when |j₂| ≪ √|s||j₁|. For λ = 0 there is no such region: the excess is ≥ 0 everywhere.

**An exact integral identity.** Combining (1.3) with the AAD balance, written in s-covariant form as ∫(|η|² + 2|W₃⁺|² + 3q²/16 + sq/8) = 0, gives on every closed AKE manifold

∫(|W⁺|² − s²/24) = −∫(|W₃⁺|² + 3q²/32).

Check on the pair, per unit orbit volume: 32 + 16 − 96 + 16 = −32 = −(16 + 16). Hence

32π²c₁² = ∫s² − 16∫|W₃⁺|² − (3/2)∫q².

This is in the same direction as LeBrun's scalar estimate ∫s² ≥ 32π²c₁², and adds nothing to it.

**Genuinely new nonlocal input from LeBrun's Weyl-weighted estimate.** Assume b₊ ≥ 2, so Taubes gives a monopole class. LeBrun's Seiberg–Witten estimate ∫(s − √6|W⁺|)² ≥ 72π²c₁² reduces, for Einstein metrics, to

⟨(1−t)(1+5t)⟩ ≥ 0.

Set δ = 1 − t and ε := (24/s²)⟨|W₃⁺|² + 3q²/32⟩.

- The identity above gives ⟨1 − t²⟩ = 2⟨δ⟩ − ⟨δ²⟩ = ε.
- The estimate gives 6⟨δ⟩ ≥ 5⟨δ²⟩.
- Eliminating ⟨δ⟩ yields ⟨δ²⟩ ≤ (3/2)ε, that is,

  ∫(|s|/√24 − |W⁺|)² ≤ (3/2)∫(|W₃⁺|² + 3q²/32).

This is a Seiberg–Witten-certified upper bound on the L² deviation of |W⁺| from its Kähler value in terms of torsion energy. It is independent of the local theory.

**Decisive cheap test.** Evaluate both sides on the pair's exact profile. It is noncompact, so the Seiberg–Witten estimate does not apply there, but the comparison is meaningful:

- If the pair violates the inequality, Seiberg–Witten carries information that no local differential compatibility can supply. The closed problem then becomes a competition: the zeros force Weyl-excess bubbles of size roughly 1/√|s|, contributing to the left side, while the right side is torsion energy, which is small near zeros. A lower bound on the left-hand contribution of each nondegenerate zero, as an explicit function of its jet on the cone, multiplied by N = 5χ+6τ and compared with the right side via Gauss–Bonnet (Vol·s² ≤ 192π²χ), is then a concrete quantitative route.
- If the pair satisfies it with room to spare, this route is weak.

**Source to read.** LeBrun's Seiberg–Witten curvature estimates for ∫(s − √6|W⁺|)² on symplectic 4-manifolds with b₊ > 1, including the equality case (Kähler with constant s), and the corresponding b₊ = 1 chamber versions.

## (d) Local germs with an isolated nondegenerate zero λ<0

**SU(2) nut: the strongest symmetric candidate.**

- *The zero is forced.* At a nut of an SU(2)-cohomogeneity-one AK structure with Ω invariant, the isotropy SU(2) ⊂ U(2) acts trivially on Λ⁺, fixes Ω(p), acts on Λ^{0,1} as the fundamental representation and trivially on Λ^{0,2}. E_p has no invariants, so **T(p) = 0 automatically**.
- *The first jet.* The invariant first jets in Hom(T_p, E_p) are exactly span(c, A); S is not invariant. The cone becomes ‖A‖² = 8|c|².
- *Nondegeneracy is automatic.* Any nonzero invariant jet has c ≠ 0, and then det = 9|c|⁴ + |a|⁴ > 0. Index +1 and isolatedness are both automatic.
- *Curvature at the nut.* Isotropy forces W⁻(p) = 0, which matches the half-conformally-flat structure of A01's pair (W⁻ ≡ 0). W⁺(p) is free subject to r = s/6.
- *Explicit nut condition.* For the diagonal ansatz Ω = √X₁ω₁ + √X₂ω₂ with W⁺ = diag(w₁, w₂, w₃) in the A01 normalization (Kähler spectrum (s/6, −s/12, −s/12)):
  - V = diag(d, −d) with d = (X₂w₁ + X₁w₂ − w₃)/2;
  - |η|²₆₂ = X₁X₂(w₁−w₂)².
  - The cone condition trV² = 8|η|² becomes

    X₂w₁ + X₁w₂ − w₃ = ±4√(X₁X₂)(w₁ − w₂),

    together with X₁w₁ + X₂w₂ = s/6 and Σwᵢ = 0. This leaves a one-parameter family of admissible nut curvatures for each λ.
- *Existence step.* Regularity at a nut is a singular initial-value problem, where Eschenburg–Wang-type existence applies and formal solutions converge. One needs:
  - the dimension of the regular-nut diagonal Bianchi IX Einstein germs with λ<0;
  - the closure ODE for (X₁, X₂), which is overdetermined;
  - whether the two meet along the curve above.
- *Cheapest version.* Continue A01's algebraic Bianchi-VIII solution (in p and y with y² = (3p−1)(3p+1)(3p²+1)) to SU(2) structure constants. Check whether some branch has an endpoint where all A_i ~ r²/4 with Ω regular, i.e. a nut instead of the p = 1/3 bolt.
- *What it would change.* A positive outcome gives an analytic strict AKE germ with λ<0 and an isolated nondegenerate index-+1 zero. Route 2 of Step 75 §3 (a local no-zero theorem) would then be closed off, and the problem would rest on nonlocal input such as (c). An outcome where the overdetermined system is incompatible at λ<0 but compatible at λ=0 would be a sign-of-λ mechanism visible at symmetric zeros; it is worth contrasting with Ricci-flat SU(2) nuts.
- *Related literature to check.* Hitchin/Tod SU(2)-invariant self-dual Einstein metrics with λ<0 (Painlevé VI), viewed in the orientation where Ω lives. Pair this with a full-text search for Armstrong's almost-Kähler Einstein ansatz.

**U(2) (biaxial) nuts.** The full isotropy U(2) forbids A and S. The only possible invariant first jet is pure c, which the cone excludes. So biaxial AKE nuts have zeros of order ≥ 2, with Kähler-type W⁺(p), or are Kähler. Testing this on Taub-NUT-AdS/Pedersen-type metrics carrying invariant closed forms is an independent check of Theorem 62.A.

**Toric germs.** At a point with circle isotropy, the tangent space splits into a fixed plane of weight 0 and a normal plane of weight ±1. E then has weights {±1, ±2}, with no weight 0, so T = 0. This holds for either relative orientation of J on the normal plane. Hence T² symmetry forces torsion to vanish along entire circle-stabilizer surfaces: zero sets of dimension 2, never isolated. Toric ansätze cannot produce the desired germ, but they do produce explicit nonisolated zero sets whose supported Euler class can be studied.

**Without symmetry: Cartan–Kähler.** The AKE system is analytic and overdetermined: Ω has 2 unknowns and dΩ = 0 imposes 4 equations. The required objects are:

- its Cartan characters and Spencer cohomology, computable from the fibre dimensions in (a);
- its involutivity order k.

If cone points with c ≠ 0 lift to integral elements at order k, then Cartan–Kähler produces analytic germs with an isolated nondegenerate zero for generic jets on the cone. This is the general form of the SU(2) test and does not depend on finding an ansatz.

## What would change the global picture

| Outcome | Consequence |
|---|---|
| SU(2) nut or Cartan–Kähler lift on the cone exists at λ<0 | Local zero theory cannot obstruct. Goldberg (closed, λ<0) rests on nonlocal quantities: the Seiberg–Witten bound of (c), the Poincaré–Hopf charge −2(2χ+3τ) on the strict critical set of q, and its canonical-curve architecture. The constructive direction becomes that architecture. |
| D = 6 at λ<0 cuts all nondegenerate jets from the cone, but not at λ=0 | Weight moves to degenerate zeros. Two inputs then decide: the index of the degenerate (GH-type) stratum, computable from the exact GH jets as the degree of T/\|T\| on small 3-spheres, and definiteness of the order-2 quadratic form Q. If all surviving zeros had index ≤ 0, the forced charge 5χ+6τ > 0 would close the problem. |
| Pair violates the Seiberg–Witten deviation inequality | The quantitative bubble-versus-torsion-energy competition is the live global route. |
| (Hess q)'' vanishes at strict critical points, or maximal critical surfaces are J-holomorphic | Poincaré–Hopf plus adjunction either closes the problem (if χ(C) ≥ 0 can be forced) or pins any counterexample to q-maxima along canonical-class curves. |