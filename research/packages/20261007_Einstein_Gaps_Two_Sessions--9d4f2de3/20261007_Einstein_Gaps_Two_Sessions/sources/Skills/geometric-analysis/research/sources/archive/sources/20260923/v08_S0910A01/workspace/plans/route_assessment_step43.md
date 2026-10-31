> **Step 44 update.** Use `workspace/plans/route_assessment_step44.md` and `workspace/notes/step44_preceptor_reading_first_exit_terminal_chain.md` for the current status.  In particular, the operative H-DT route is coefficient regularization followed by a smooth limit to the exact `a=χ²` flow; stationary collars, frozen complement, disjoint summation, and global `Q` are applied only after that exact-flow limit.  The H-WU energy uses the current pair `(U_m,C_{m+1})` with same-exponent closure, not a previous-layer `C_{m+1}` input.

# Route assessment after Step 43

## Main outcome

Step 43 (Agent2/Constructor) resolved both remaining analytic inputs for the
restricted near-critical Ishida–LeBrun negative defect gap theorem:

1. **H-WU (weighted evolution):** Derived the tensor-level cutoff-jet provenance
   for the weighted $U_m = \nabla^m(\chi^2(\operatorname{Rm}+G))$ equation.
   Proved that all $C_{m+2}$ sources carry explicit $\chi$ weight, with two
   sources in the parabolic form (Hessian-$a$ contraction and extracted
   Laplacian).  TTCS independently verified with one correction incorporated
   (the parabolic form has two sources, not one).  A03 Step 45 coordinate-time
   ledger independently confirms the same weight structure with $b = \chi^2 +
   \varepsilon^2$.

2. **H-DT (start/restart):** Independently assessed A03's Step 44 Yang
   adaptation and Step 45 coefficient-regularized closure.  Both routes
   (Yang adaptation and coefficient regularization) resolve per-datum
   existence/restart.  The coefficient-regularization route is cleaner because
   it avoids importing Yang's compressed tame inverse proof.

## What is now established

- The per-datum flow platform: for each smooth initial metric and cutoff,
  the normalized degenerate flow exists, and bounded $|U|$ implies smooth
  continuation.
- The staggered derivative propagation: $T_0 \to (U_1, C_2) \to T_1 \to
  (U_2, C_3) \to \cdots$ closes with constants uniform in the coefficient
  regularization parameter.
- The weight structure needed by A03's energy mechanism is confirmed at the
  tensor level.

## What remains before calling the restricted gap theorem established

Per A03 #365, the assembled **first-exit/support/terminal chain** should be
independently reviewed before promoting the restricted gap theorem.
Specifically:

1. **First-exit bootstrap:** The estimates from Steps 32–36 (localized $K_2$,
   integrated potential $Y$, unregularized $J_6$, weighted Moser endpoints)
   must be verified on one common flow with the corrected support construction,
   not on independent support patches.

2. **Support construction:** The volume-average maximal function with gradient
   cutoffs, $7r \le R$, single global $a = \sum\chi_\alpha^2$, and inner
   terminal centers must be assembled into a complete lemma.

3. **Global $Q$ propagation:** The independent $Q = \int|E|^2$ estimate must
   use genuinely disjoint buffered supports with a frozen complement.

4. **Terminal recalibration:** The Seiberg–Witten recalibration on the evolved
   metric, with $q \ge 0$ and sign-averaged monopole classes, must produce the
   nonnegative calibrated density.

5. **Terminal pullback and Derdziński contradiction:** The Liouville–Rauch
   averaging over inner centers, strong finite-$W^{2,p}$ convergence in
   harmonic coordinates, and the forbidden germ argument must be checked
   against the actual flow output.

6. **Bounded-$A$ subsequences:** The integrality argument from Step 42 §3.

These are substantial verification tasks, not routine checks.  They involve
the entire proof architecture from support selection through terminal
contradiction.

## Relation to Yau Problem 26

Even after the restricted gap theorem is fully verified, it covers only:
- the negative sign branch in dimension 4
- the Ishida–LeBrun topology family with $q = D - A/3 \ge 0$
- a family-uniform gap $\varepsilon_{\text{IL}} > 0$

The following remain open:
- Positive branch (all dimensions)
- Arbitrary four-manifold topology
- Dimensions $n \ge 5$
- Dimension-only constants for the full proposition
- Lean 4 formalization

A02's Step 44 bi-Kähler loophole finding shows that first-order Ozuch
chirality cannot close the noncollapsed positive branch for the
$(S^2 \times S^2)/\mathbb{Z}_2$ stress family.  Positive collapse and
higher-dimensional mechanisms are major unresolved fronts.

## Files

- H-WU resolution: `workspace/notes/step43_H_WU_resolution_weighted_evolution.md`
- H-DT assessment: `workspace/notes/step43_H_DT_assessment.md`
- Verification: `workspace/scripts/step43_weighted_evolution_verify.py` (54/54)
- TTCS: `trace/ttcs/results/step43_ttcs01_verifier1_integration.md`
- A03 Step 45: `Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md`
- Route assessment: this file
