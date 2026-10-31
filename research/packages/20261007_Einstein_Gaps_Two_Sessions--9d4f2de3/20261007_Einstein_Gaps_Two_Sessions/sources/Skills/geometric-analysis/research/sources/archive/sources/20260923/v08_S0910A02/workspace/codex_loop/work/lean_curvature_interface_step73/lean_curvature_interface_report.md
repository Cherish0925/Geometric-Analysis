# Lean curvature-interface audit for Step 73

## Outcome

The locked Lean 4.33.1 / Mathlib v4.33.1 environment does **not** contain a geometric Levi--Civita, Riemann-curvature, Ricci-curvature, scalar-curvature, or sectional-curvature API. It does, however, contain more infrastructure than the Step 71 name probe exposed: a recently added bundled covariant-derivative API, smoothness predicates for connections, torsion, metric compatibility, smooth Riemannian bundle metrics, and ordinary finite-dimensional trace. Those pieces give a credible starting point, but they stop strictly below the layer needed for a faithful Yau Problem 26 statement.

Accordingly, `Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/CurvatureInterfacePrototype.lean` is an explicitly conditional interface design, not a claimed formalization of Yau 26. It uses the real Mathlib manifold, tangent-bundle, metric, smooth-section, connection, torsion, metric-compatibility, compactness, connectedness, and trace objects. Its only new geometric data are the missing layers: a Levi--Civita candidate and a pointwise curvature tensor, tied by a realization law to the standard connection-commutator formula. Ricci is then genuinely defined by trace rather than supplied as an arbitrary predicate.

## Locked environment and audit method

The checks used Lean 4.33.1 (commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`) and the locked Mathlib input `v4.33.1`, Git revision `0df444a360eaa60ab8c11dca51a86af692955474`. The project lock hashes were:

- `lake-manifest.json`: `14a93e63a5df91ca2739c1c6c6e2a55a37b4677e040e25e4a0c9163eca92371c`
- `lean-toolchain`: `3aac669c7a910ec2389f4e4f921b605adf6ebf2d1e0c9b9cd0be4d33f3f5db71`

The conclusion is based on three complementary checks.

1. `Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/scan_mathlib_curvature_api.py` scanned all 8,311 `.lean` files in the locked Mathlib source tree. The patterns for Levi--Civita, Christoffel, Riemann curvature/tensor, Ricci, scalar curvature, and sectional curvature each had zero matches. The only generic `curvature` match was a prose comment about the hyperbolic disc in `Mathlib/MeasureTheory/Measure/Doubling.lean`, not a declaration. The complete machine-readable result is `Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/mathlib_curvature_source_scan.json`.
2. `Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/MathlibCurvatureEnvironmentScan.lean` inspected all constants loaded by `import Mathlib`. All tested Levi--Civita/Christoffel/Riemann/Ricci/scalar/sectional spellings had count zero. By contrast, `CovariantDerivative` had 163 substring hits and `RiemannianMetric` had 100, confirming that the scan was seeing the new lower-level API. The compiled output is preserved in `Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/MathlibCurvatureEnvironmentScan-audit.json`.
3. `Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/MathlibCurvatureApiProbe.lean` directly checked the exact declarations used by the prototype. Its accepted certificate, including the printed inferred types, is `Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/MathlibCurvatureApiProbe-audit.json`.

Substring scans cannot logically exclude a semantically equivalent API with wholly unrelated terminology. Here that residual risk is small because the environment scan was paired with a complete source scan, inspection of all manifold vector-bundle connection modules, and direct checks of the available neighboring API.

## Exact Mathlib boundary

| Needed layer | Status in locked Mathlib | Actual import/declaration or gap |
|---|---|---|
| Smooth finite-dimensional real manifold | Available | `Mathlib.Geometry.Manifold.Instances.Real`; `IsManifold (𝓡 n) ∞ M`, where `𝓡 n` uses `EuclideanSpace ℝ (Fin n)` and is boundaryless |
| Hausdorff/second-countable/compact/connected hypotheses | Available | `T2Space`, `SecondCountableTopology`, `CompactSpace`, `ConnectedSpace`; these are explicit because `IsManifold` does not bundle all of them |
| Smooth tangent-bundle metric as data | Available | `Mathlib.Geometry.Manifold.VectorBundle.Riemannian`; `Bundle.ContMDiffRiemannianMetric`, `.toRiemannianMetric`, `Bundle.RiemannianBundle`, `IsContMDiffRiemannianBundle` |
| Metric-induced manifold distance | Available but not needed for curvature statement | `Mathlib.Geometry.Manifold.Riemannian.Basic`; `IsRiemannianManifold`, `EMetricSpace.ofRiemannianMetric`. The former concerns the path-length distance after a metric is installed; it is not a curvature class. |
| Bundled connection | Available | `Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Basic`; `CovariantDerivative`, `CovariantDerivative.ContMDiffCovariantDerivative` |
| Torsion | Available | `Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Torsion`; `CovariantDerivative.torsion`, `.torsion_eq_zero_iff` |
| Metric compatibility | Available | `Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Metric`; `CovariantDerivative.derivMetricTensor`, `.IsMetricCompatible`, `.isMetricCompatible_iff` |
| Levi--Civita connection | Missing | No constructor and no existence/uniqueness theorem producing the torsion-free metric-compatible connection of a supplied smooth metric |
| Riemann tensor | Missing | No curvature commutator definition, pointwise tensor construction, tensoriality theorem, or symmetry/Bianchi library |
| Ricci tensor | Missing | No contraction or symmetry theorem. Import `Mathlib.LinearAlgebra.Trace`; its `LinearMap.trace` is sufficient for the algebraic contraction once a pointwise Riemann endomorphism exists. |
| Scalar and sectional curvature | Missing | No declarations or supporting curvature tensor layer |
| Quadratic-form nonnegativity | Available algebraically | `Mathlib.LinearAlgebra.BilinearForm.Properties`; `LinearMap.BilinForm.IsNonneg` means nonnegative on the diagonal, and `.IsPosSemidef` additionally includes symmetry. There is no ready-made pointwise order for a dependent field of bilinear forms. |

The connection API is recent and intentionally partial. Its own implementation notes state that dependence of `cov σ x` on only the 1-jet of `σ` is still to be proved, with an Ehresmann-connection file planned. The metric-connection file also lists induced connections on Hom bundles and parallel transport as future work. These omissions matter: curvature tensoriality is exactly a second connection operation whose dependence on point values must be established cleanly.

## Prototype design

`Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/CurvatureInterfacePrototype.lean` imports only the needed Mathlib modules and defines the following.

- `ModelSpace n` is `EuclideanSpace ℝ (Fin n)`, and `SmoothMetric n M` is the genuine `Bundle.ContMDiffRiemannianMetric` on `TangentSpace (𝓡 n)`.
- `TangentConnection n M` is the genuine bundled `CovariantDerivative` on that tangent bundle; `SmoothVectorField n M` is the genuine `ContMDiffSection` type.
- `curvatureOnFields` implements
  \[
  R(X,Y)Z=\nabla_X\nabla_Y Z-\nabla_Y\nabla_X Z-\nabla_{[X,Y]}Z,
  \]
  taking account of Mathlib's documented nonstandard argument order `cov σ x (X x) = ∇_X σ(x)`.
- `GeometryFor g` is the explicit missing layer. It carries a smooth connection, the real Mathlib conditions `torsion = 0` and `IsMetricCompatible`, a pointwise continuous trilinear curvature tensor, and a law requiring that tensor to realize the commutator formula on smooth vector fields. Thus the curvature is assumed as tensor data because Mathlib cannot yet construct it, but it is not an arbitrary Ricci predicate.
- `ricciAt G x v w` is defined as `LinearMap.trace ℝ (T_xM)` of `z ↦ R_x(z,v)w`, fixing the convention `Ric(v,w) = tr(z ↦ R(z,v)w)`.
- `QuadraticLE A B := ∀ v, A v v ≤ B v v`; `RicciPinched` therefore states the literal pointwise diagonal inequalities `c g_x(v,v) ≤ Ric_x(v,v) ≤ C g_x(v,v)`. This avoids asserting symmetry before the curvature-symmetry theorems exist.
- `IsEinstein` requires one global `λ : ℝ` and equality `Ric_h = λ h` at every point and on every pair of tangent vectors.
- `DimensionStatementDesign` explicitly quantifies `T2Space`, `SecondCountableTopology`, `CompactSpace`, `ConnectedSpace`, and a smooth charted structure using the boundaryless model `𝓡 n`. It also exposes `Nonempty (CurvatureAPI n M)` as missing infrastructure and quantifies over all lawful implementations.

This is materially stronger than the Step 71 synthetic shell because the metric, connection, torsion, compatibility, curvature formula, trace contraction, and inequalities have geometric content. It is still not a faithful Yau 26 formalization: `CurvatureAPI` is not constructed by Mathlib, and `DimensionStatementDesign` consequently includes an infrastructure condition that is not part of the mathematical conjecture. No theorem asserting Yau 26 was proved or claimed.

## Verification

The following commands were run in the configured Qiushi Lean environment (the runtime-specific `ELAN_HOME` was set to the installed Lean toolchain):

```text
Skills/qiushi-lean-proof/scripts/lean_check Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/MathlibCurvatureApiProbe.lean
Skills/qiushi-lean-proof/scripts/lean_check Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/MathlibCurvatureEnvironmentScan.lean
Skills/qiushi-lean-proof/scripts/lean_check Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/CurvatureInterfacePrototype.lean
qiushi-yau26 lean Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/CurvatureInterfacePrototype.lean --declaration Yau26CurvaturePrototype.ricciPinched_iff --output Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/CurvatureInterfacePrototype-dependency-audit.json
$QIUSHI_PYTHON Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/scan_mathlib_curvature_api.py --output Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/mathlib_curvature_source_scan.json
```

All three Lean files compiled. The checkers found no `sorry`, `admit`, or source-declared axioms. The strict dependency audit of `Yau26CurvaturePrototype.ricciPinched_iff` recompiled in a fresh process and observed only the allowed dependencies `propext`, `Classical.choice`, and `Quot.sound`; its source hash `ca22155ae9bd907e8d27592f962542593de9527cea9abf520a81fc9a7a12a4b7` matches the final prototype.

That audited theorem only checks the logical unpacking of the two diagonal inequalities. It does not certify curvature construction or Yau 26, because neither appears as a proved theorem in the file. This separation between kernel checking and scientific statement correspondence follows the `Skills/qiushi-lean-proof/SKILL.md` verification discipline.

`Skills/qiushi-lean-proof/scripts/lean_probe` could not create its hard-coded temporary directory under the read-only user-root `.cache/qiushi-lean-proof` location. The normalized diagnostic is preserved in `Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/lean_probe_failure.json`. This is a helper-script filesystem issue rather than a Lean failure: `lean_check` and the strict audit both executed successfully against the locked project. No shared skill or project file was modified.

## Recommended construction path

The shortest honest path is a small Mathlib development, not another synthetic theorem shell.

1. Define the curvature of a smooth tangent connection first as the field commutator already prototyped, then prove pointwise tensoriality and package it as a `(1,3)` continuous multilinear tensor. This likely depends on finishing or bypassing the connection 1-jet lemma noted in Mathlib's TODO.
2. Prove the Levi--Civita existence and uniqueness theorem for `Bundle.ContMDiffRiemannianMetric`. A useful public result should construct `CovariantDerivative`, its smoothness instance, `torsion = 0`, and `IsMetricCompatible`; uniqueness prevents the downstream statement from depending on a chosen implementation.
3. Define Ricci from the Riemann endomorphism using `LinearMap.trace`; prove bilinearity, smooth dependence, and symmetry for a Levi--Civita connection. Then package the pointwise `(0,2)` tensor so `B - A` can use `LinearMap.BilinForm.IsNonneg` directly.
4. Add the fieldwise quadratic-form order and prove its equivalence to diagonal inequalities. Scalar and sectional curvature can be built afterward; neither is needed merely to state the Ricci-pinching version of Yau 26.
5. Replace `CurvatureAPI` in the prototype by the canonical construction. Only at that point should `DimensionStatementDesign` be rewritten as, and advertised as, a faithful Yau 26 statement.

For immediate Qiushi work, use the prototype as a type-correct specification and regression test for the missing library layer. Do not use it as a proved result, and do not promote the Step 71 uninterpreted Ricci shell as geometry.
