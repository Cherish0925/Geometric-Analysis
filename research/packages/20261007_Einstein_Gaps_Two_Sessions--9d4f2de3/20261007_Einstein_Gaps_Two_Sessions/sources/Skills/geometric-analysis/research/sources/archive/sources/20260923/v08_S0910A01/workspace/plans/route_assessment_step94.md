# Route assessment: Step 94

## Corrections made

1. **Step 93 AA/BB divergence withdrawn.** The full-Lie magnetic tensor \(M=L_{(*df)^\#}g\) has pole amplitude \(4b\) and norm four times the electric trace-free Hessian norm. Step 93 used the electric norm for both. After correction, separated-pole tensor electric and magnetic contributions cancel mode by mode; the apparent \(BB_{NS}/AA_{SN}\) coincident divergence is not intrinsic.

2. **Corrected principal AA/BB response.** In the Step89/91 product-background principal normalization,
   \[
   K^{BB}_{NS}=K^{AA}_{SN}=0,
   \qquad
   K^{AA}_{NS}=K^{BB}_{SN}\approx -0.00400249866.
   \]
   Together with \(K^{AB}_{adj}\approx -0.03144249732\), the currently computed principal adjacent sum is about \(-0.03544499598\) for either ordered adjacent pair. This is a principal receiver/source-adjoint calculation, not the Ozuch radial coefficient.

3. **Heat representation.** The finite AA term has
   \[
   K_{AA,NS}=-\frac1{1024}\int_0^\infty e^s A_0(s)B_2(s)\,ds,
   \quad
   B_2(s)=32\pi\,\partial_x^2p_{s/2}^{S^2}(-1)>0,
   \]
   via \(\partial_x^2p_t^{S^2}=4\pi^2e^{-6t}p_t^{S^6}\). This proves the sign in the stated convention.

4. **A02/A03 scope narrowed.** A02's Chern--Weil/BCG theorem is valuable for orbifold+ALE near-pinched constructions with volume convergence, but it is not a classification of all near-pinched manifolds or no-Einstein mechanisms. The Ricci rescaling in the peer note should be \(\hat g=(1+\varepsilon/3)g\), not the reciprocal; the volume limit survives when \(\varepsilon\to0\). A03's \(\delta_*\approx0.24625\) resolvent theorem is a strong result for reflected free-OT cusp-extension connectors, not for general non-OT graph metrics or hyperbolic \(N\#N\) with \(S^3\) necks.

## Best next research work

1. **Product branch, constructive continuation.** Derive the actual Eguchi--Hanson \(H^4(\zeta^{\pm})\) source contraction into AB and corrected AA/BB receiver channels using Ozuch's boundary formula. Needed anchors are in `Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md` lines 283--321, 628--647, and 770--807. Include Bianchi/gauge projection, quotient/isotropy factors, symmetric-product convention, and ordered north/south frame transport. Do not treat the principal sum as physical until this source matching is done.

2. **Negative branch, complementary continuation.** Keep A03's resolvent theorem as a serious restricted obstruction and compare it with graph/non-OT mechanisms, but do not reallocate all sessions to it as if triple disjointness closed every route. Hyperbolic \(N\#N\) still asks for a non-warped connector mechanism or a general pointwise neck obstruction.

3. **Restricted IL theorem.** Still worth independent verification because it remains the most mature direct negative-pinching obstruction family, even though it does not solve the full dimension/sign problem.

4. **Full goal.** The all-dimensional Yau-26 statement remains open and far from Lean formalization. All current routes are restricted laboratories; preserve quantifier discipline.
