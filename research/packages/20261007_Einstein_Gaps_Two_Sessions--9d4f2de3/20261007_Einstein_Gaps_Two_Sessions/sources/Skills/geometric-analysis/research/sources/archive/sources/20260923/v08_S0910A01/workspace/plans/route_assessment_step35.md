# Route assessment after Step 35

**Step 34 superseding notice.**  This assessment supersedes
`workspace/plans/route_assessment_step34.md` for the tensor-level obligations.

## Main advances

1. **Curvature Hessian-a tensor derived from first principles.**
   \(B_{\mathrm{curv}}^{pq}=R^p{}_{j}{}^q{}_{l}E^{jl}\),
   with proved derivative structure
   \(|\nabla B_{\mathrm{curv}}|\le CF|\nabla\operatorname{Rm}|\).
   Signed IBP absorbs the Hessian-a contribution into
   \(\varepsilon p(D_p^{\mathrm{Rm}}+(p-2)D_p^F)+Cp^3r^{-2}K_p\).
   This resolves Step 34 §7 obligation 1.

2. **Defect Hessian-a tensor derived from Ricci linearization.**
   \(B_{\mathrm{def}}^{pq}=sg^{pq}+\tau E^{pq}-2(E^2)^{pq}\),
   quadratic in E (vanishes at E=0), with proved derivative structure
   \(|\nabla B_{\mathrm{def}}|\le Cs^{1/2}|\nabla E|\) (sharp, no extra
   \(C|\nabla E|\) term — TTCS corrected).
   Cross-checks with A03's formula: \(2B_{\mathrm{def}}\) matches
   A03's displayed tensor up to the test-function convention.
   This resolves Step 34 §7 obligation 2.

3. **Scaling test verified at the formula level.**
   Under \(\partial_tg=-2g\): \(\partial_t|R|^2=+4|R|^2\) and
   \(\int|R|^2d\mu\) invariant in dimension 4.
   Normalization cancellation: the \(+g\) in \(E=\operatorname{Ric}+g\)
   produces no additional quadratic curvature term in the algebraic
   variation, only the lowering term \(-2aR_{ijkl}\).

4. **Dissipation confirmed**: \(-pD_p^{\mathrm{Rm}}-p(p-2)D_p^F\),
   correcting Step 33's \(-p(p-3)D_p^F\).

## TTCS corrections incorporated

- Pair-symmetry argument for curvature tensor: must swap both index pairs
  simultaneously, not just one.  Final coefficient 8 is unaffected.
- Defect derivative: \(|\nabla B_{\mathrm{def}}|\le Cs^{1/2}|\nabla E|\)
  (sharp).  The earlier \(+C|\nabla E|\) was spurious because
  \(\nabla\tau=\operatorname{tr}(\nabla E)\), not \(\nabla\operatorname{Rm}\).

## A03 Step 36 Preceptor corrections noted

A03's Step 36 Preceptor review identifies three critical downstream gaps
that this tensor derivation does NOT resolve:

1. **DeTurck existence**: must use transported-coefficient gauge
   \(\widehat a=a\circ\phi_t^{-1}\) with Lie derivative
   \(\mathcal{L}_{\widehat aW}\widehat g\), not fixed \(a\mathcal{L}_Wg\).
   Generic \(\varepsilon\)-Schauder does not give \(\varepsilon\)-independent
   degenerate existence.

2. **Continuation**: must use shifted \(U=a(\operatorname{Rm}+G)\)
   and the base pair \((\nabla U,\nabla^2\chi)\); declaring coefficients
   finite by smoothness is not an extension criterion.

3. **Terminal calibration**: needs separate global \(Q=\int|E|^2\),
   not derivable from \(J_6\) or \(\|aE\|_\infty\).  The Q estimate
   \(Q'\le Cr^{-2}Q\) from the homogeneous identity is an independent
   first-exit component.

## Completed tower

Conditional on first-exit geometry and smooth flow existence, the fixed-exponent
layer now has all its tensor premises proved:

| Component | Status | Source |
|-----------|--------|--------|
| Curvature Hessian-a tensor + derivative structure | **Proved** | Step 35 §3 |
| Defect Hessian-a tensor + derivative structure | **Proved** | Step 35 §5–6 |
| Signed IBP for both | **Proved** | Step 35 §3.3, §6.4 |
| Dissipation coefficients | **Proved** | Step 35 §4.1 |
| Scaling test | **Verified** | Step 35 §1 |
| Curvature power inequality (4.4) | **Tensor-level proved** | Step 35 §4.4 |
| J_6 persistence (two-factor) | **Proved** (A03 Step 35) | A03 §6 |
| q=3 good-slice propagation | **Conditional** | Step 34 §4 |
| Moser endpoints | **Conditional** | Step 34 §6 |
| Global Q preservation | **Template** | A03 Step 36 §4 |
| Degenerate-flow existence | **Open** | A03 Step 36 §2 |
| Continuation (shifted U) | **Open** | A03 Step 36 §3 |

## What remains hard

The next mathematical targets in order of dependency:
1. Normalized transported-coefficient DeTurck existence (§2 of A03's review).
2. The base pair \((\nabla U,\nabla^2\chi)\) extension theorem.
3. Global Q as an independent first-exit component.
4. The full simultaneous first-exit bootstrap.
5. Terminal calibration + exponential-pullback + Derdziński contradiction.

Even completion of all five would address only the near-critical
Ishida–LeBrun negative four-dimensional laboratory.

## Evidence

- Note: `workspace/notes/step35_tensor_variation_and_hessian_a.md`
- Verifier: `workspace/scripts/step35_tensor_hessian_verification.py` (41/41 pass)
- TTCS: `trace/ttcs/results/step35_ttcs01_verifier1_integration.md`
- A03 sources: `Sessions/S0910A03/workspace/notes/step35_unregularized_J6_persistence_lemma.md`,
  `Sessions/S0910A03/workspace/notes/step36_preceptor_interface_review.md`
