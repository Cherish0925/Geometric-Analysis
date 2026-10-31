# Round 10 calculation and proof checks

21 September 2026. Run from this directory using the existing numeric
environment; no environment installation or shared-runtime change was made.
The resolved environment used Python 3.12.13 and SymPy 1.14.0.

```sh
qiushi-yau26 env numeric python round10_kottler_check.py
qiushi-yau26 env numeric python round10_kottler_coordinate_check.py
qiushi-yau26 env numeric python round10_cusp_doubling_check.py
qiushi-yau26 env numeric python round10_optical_check.py
qiushi-yau26 env numeric python round10_connector_check.py
qiushi-yau26 env numeric python round10_bundle_check.py
qiushi-yau26 env numeric python round10_nonabelian_check.py
```

All seven commands completed successfully in the parent session.
The added torus comparison initially failed a literal-zero assertion
because SymPy's `trigsimp` retained an equivalent hyperbolic expression.
Rewriting in exponentials and performing exact rational cancellation
returned zero in both components; the final checker uses that reduction.

| Calculation | Actual scope |
| --- | --- |
| Kottler warped calculation: nine checks | Exact Einstein input, every error eigenvalue, smooth doubling, sharp continuous supremum, optical monotonicity, arbitrary fixed cutoff, parameter variation, fixed-defect torus comparison |
| Kottler coordinate calculation | Independent Christoffel/Ricci reconstruction of all sixteen entries; no warped Ricci formula reused |
| Twisted cusp coordinate calculation | All sixteen Ricci entries, zero mixed blocks, four error eigenvalues, Chern/lapse identities |
| Optical calculation: six groups | Coordinate Ricci, conformal null-Ricci identity, endpoint Green signs, nonconstant ground-state example, scalar/full-Ricci distinction and sign mutations |
| Charge transport: six checks | Mixed equation with variable charge and non-diagonal torus metric, separator constants and weighted transport example |
| Kodaira family: nineteen checks | Euler/signature/base-change identities, exact volume and harmonic/Hodge formulas, normalized limits and algebraic feasibility example |
| Nonabelian analysis: eight groups | Full-target quadratic map, determinant identity, complete residual, Dirac rank conditions and slow-profile source correction |

The following earlier checks also completed successfully in this parent
session:

```sh
qiushi-yau26 env numeric python round9_signature_check.py
qiushi-yau26 env numeric python round9_bundle_check.py
qiushi-yau26 env numeric python round9_nonabelian_check.py
```

The parent read the new proofs. A separate agent reviewed the cusp gluing
and approximate-Jacobi arguments; the other principal notes received
cross-reading during the work. The complete Ricci tensor in each new
explicit metric was checked along independent calculation paths.

These computations do not certify the cited external existence theorems,
prove all possible gluing constructions, establish publication priority,
or resolve Einstein existence on a closed candidate manifold. Uniform
collar estimates, completeness, topology and the continuous norm maximum
are argued in the mathematical notes rather than inferred from numerical
samples. There are no sampled claims of a sharp global supremum in the
new Kottler theorem.
