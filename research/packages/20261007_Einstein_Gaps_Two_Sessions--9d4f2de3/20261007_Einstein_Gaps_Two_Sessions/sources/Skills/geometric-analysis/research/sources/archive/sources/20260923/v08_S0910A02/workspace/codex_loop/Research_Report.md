# Research Report: Constant metric scaling and Ricci-pinching normalization

## Outcome

This run produced a contentful Lean 4 formalization of constant positive rescaling of a smooth Riemannian metric, preservation of metric compatibility by the same connection, invariance of the Ricci `(0,2)` tensor obtained from that common connection and curvature, and the strict positive and negative Ricci-pinching interval normalizations. The final source compiles without placeholders or source-declared axioms, and six named declarations pass the strict transitive dependency audit.

The work also found and repaired, in a separate patch, a consequential reciprocal typo in the current mathematical reduction note. If `h=αg`, the correct scale that centers a positive interval `[c,C]` at `+1` is

`α=(c+C)/2`,

not `2/(c+C)`. For a negative interval it is `α=-(c+C)/2`. The existing delta formulas are correct. The original note was not edited; a checked patch is provided under the permitted work directory.

This is an infrastructure advance for the formalization path. It is not a proof or refutation of Yau Problem 26.

## Formal artifact and geometry boundary

The central file is `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/MetricScalingNormalization.lean`. It uses real Mathlib v4.33.1 objects wherever the locked library supports them:

- `Bundle.ContMDiffRiemannianMetric` for the smooth metric;
- `CovariantDerivative`, `ContMDiffCovariantDerivative`, the Mathlib torsion map, and `CovariantDerivative.IsMetricCompatible` for connection data;
- continuous linear maps for the pointwise Riemann tensor; and
- `LinearMap.trace` and `LinearMap.BilinForm` for the Ricci contraction as a genuine bundled `(0,2)` tensor.

`scaleMetric g α hα` is an actual Mathlib smooth Riemannian metric for `0<α`. The construction proves positive-definiteness, von Neumann boundedness of the rescaled unit ball, and smoothness rather than treating scaling as an abstract symbol. The theorem `scaleMetric_inner` identifies its inner product with `α * g.inner`.

The theorem `isMetricCompatibleWith_scaleMetric` proves that any connection compatible with `g` remains compatible with `αg`. The proof opens Mathlib's pointwise metric-compatibility characterization and uses the manifold derivative product rule for a constant multiple. This is the substantive connection-scaling step needed to reuse a Levi-Civita connection under constant rescaling.

The exact remaining library gap is explicit in `GeometryFor`. Mathlib v4.33.1 has the connection substrate but no supplied canonical construction joining a smooth metric to its Levi-Civita connection, Riemann curvature, and Ricci tensor. Accordingly, `GeometryFor g` contains:

- a genuine Mathlib tangent covariant derivative;
- proofs that it is smooth, torsion-free, and metric-compatible with `g`;
- a pointwise continuous trilinear curvature tensor; and
- `riemann_realizes`, tying that tensor to the covariant-derivative commutator on smooth vector fields.

These fields are assumptions/data of the local interface. In particular, this artifact does not prove that every Mathlib smooth metric has a `GeometryFor` instance, nor does it add a source axiom claiming so. Conversely, Ricci invariance is not an assumed interface law. `ricciAt` defines Ricci by tracing `z ↦ R(z,v)w`, `ricciTensor` proves that this contraction is bilinear, and `scaleGeometry` constructs geometry for `αg` using the same connection and curvature. Its metric compatibility is discharged by the theorem above; smoothness and torsion-freeness are unchanged. Thus:

- `ricciTensor_scale_const` proves equality of the bundled bilinear forms at each point;
- `ricciTensorField_scale_const` proves equality of the full pointwise tensor fields; and
- `ricci_scale_const` gives the evaluated equality on tangent vectors.

The equality is definitionally short after `scaleGeometry`, but its construction is meaningful: Lean has first checked that the reused connection is valid for the scaled metric and that the curvature realization remains the same.

## Pinching normalization and correction to Step 85

`QuadraticLE` formalizes diagonal order of two bilinear forms, and `RicciPinched G c C` is the literal pointwise condition

`c g(v,v) ≤ Ric(v,v) ≤ C g(v,v)`.

The general theorem `ricciPinched_scale_iff_of_endpoint_identities` proves that if `aα=c` and `bα=C`, then `[c,C]` pinching relative to `g` is equivalent to `[a,b]` pinching relative to `αg`. The proof uses the checked identities `Ric(αg)=Ric(g)` and `(αg)(v,v)=αg(v,v)` in both directions.

For `0<c<C`, the file defines

`positiveScale c C = (c+C)/2`,  
`positiveDelta c C = (C-c)/(C+c)`.

It proves positivity of the scale, `0<δ<1`, both endpoint identities

`(1-δ)α=c` and `(1+δ)α=C`,

and the packaged equivalence `positive_interval_normalization_package`. The analogous negative package, under `c<C<0`, uses

`negativeScale c C = -(c+C)/2`,  
`negativeDelta c C = (C-c)/(-(C+c))`,

and proves `(-1-δ)α=c`, `(-1+δ)α=C`, `0<δ<1`, and the corresponding pinching equivalence. Theorems `positive_centering_scale_unique` and `negative_centering_scale_unique` prove algebraically that the two midpoint scales are forced by those centered endpoint equations.

This exposes an error in Section 3, Case 4 of `Sessions/S0910A02/workspace/notes/step85_yau26_established_reduction.md`, which currently says `h=2/(c+C) g`. Indeed, coefficients relative to `h=αg` are divided by `α`; adding the desired positive endpoint equations gives `2α=c+C`. The negative centered equations likewise give `-2α=c+C`. `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/step85_normalization_correction.patch` corrects both cases and makes the operator norm's metric dependence explicit with a subscript `h`. `git apply --check` confirms that this patch applies to the present note, but the patch was intentionally not applied outside `codex_loop`.

The Lean conclusion itself is the pair of quadratic-form inequalities, which is the option explicitly allowed by the proposal. The artifact does not prove equivalence with the operator norm formulation: the minimal `GeometryFor` interface does not yet derive the usual symmetry of Levi-Civita Ricci or build the metric-raised self-adjoint Ricci endomorphism. For genuine Levi-Civita curvature, symmetry gives the standard equivalence between the order interval and the operator-norm bound. That correspondence should not be described as formalized here.

## Verification performed

The final source SHA-256 is `f3d92ec4db6a2dfb8cc06b688a83e5de15c8b9cba0791f56f6e7e08551b35541`. The locked environment reports Lean 4.33.1, `lake-manifest.json` hash `14a93e63a5df91ca2739c1c6c6e2a55a37b4677e040e25e4a0c9163eca92371c`, and toolchain-file hash `3aac669c7a910ec2389f4e4f921b605adf6ebf2d1e0c9b9cd0be4d33f3f5db71`.

The source-level check was run as:

```text
Skills/qiushi-lean-proof/scripts/lean_check Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/MetricScalingNormalization.lean
```

with the runner's installed Lean home selected. It returned `status: accepted`, successful compilation, no stderr/stdout warnings, no placeholders, and `declares_axiom: false`. The captured result is `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/lean_check-final.json`.

Fresh-process strict checks were run with the pattern:

```text
qiushi-yau26 lean Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/MetricScalingNormalization.lean --declaration <name> --output <audit.json>
```

for these declarations:

| Declaration | Result |
|---|---|
| `Yau26MetricScaling.isMetricCompatibleWith_scaleMetric` | `dependency_checked` |
| `Yau26MetricScaling.ricciTensorField_scale_const` | `dependency_checked` |
| `Yau26MetricScaling.positive_interval_normalization_package` | `dependency_checked` |
| `Yau26MetricScaling.negative_interval_normalization_package` | `dependency_checked` |
| `Yau26MetricScaling.positive_centering_scale_unique` | `dependency_checked` |
| `Yau26MetricScaling.negative_centering_scale_unique` | `dependency_checked` |

Each strict audit observes only the policy-allowed logical axioms `propext`, `Classical.choice`, and `Quot.sound`; every `rejected_axioms` list is empty, and every audit records the final source hash. All generated JSON files were validated with `jq -e`. The correction was independently checked with:

```text
git apply --check Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/step85_normalization_correction.patch
```

## Artifacts

All new research artifacts are confined to the authorized directory:

- `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/MetricScalingNormalization.lean`: checked source and theorem statements.
- `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/lean_check-final.json`: final whole-file compile and source-policy result.
- `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/metricCompatibility_scale-final-audit.json`: strict compatibility-scaling audit.
- `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/ricciTensorField_scale_const-final-audit.json`: strict tensor-field invariance audit.
- `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/positive_interval_normalization-final-audit.json` and `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/negative_interval_normalization-final-audit.json`: strict normalization-package audits.
- `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/positive_centering_scale_unique-final-audit.json` and `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/negative_centering_scale_unique-final-audit.json`: strict scale-uniqueness audits.
- `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/step85_normalization_correction.patch`: valid patch for the Step 85 prose formulas.
- `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/metric_scaling_report.md`: concise local summary.

## Remaining work and recommended use

Qiushi should absorb the corrected midpoint scales into the mathematical reduction by reviewing and applying `step85_normalization_correction.patch`. The Lean theorem packages can then be cited as machine-checked support for the strict one-signed interval algebra.

The next formal infrastructure step is not more scalar algebra. It is to supply or develop a Mathlib-compatible theorem constructing the Levi-Civita connection and its tensorial Riemann curvature for `ContMDiffRiemannianMetric`, then instantiate `GeometryFor` rather than accept it as input. A subsequent layer should derive Riemann symmetries and Ricci symmetry and define the raised self-adjoint Ricci operator, allowing a checked equivalence between `NormalizedPinched` and the operator-norm notation used in the prose.

Until those steps exist, this result should be stated precisely as: conditional on the explicitly packaged smooth torsion-free metric-compatible connection and its realized curvature tensor, constant positive scaling preserves the constructed Ricci `(0,2)` tensor and transports strict positive or negative quadratic-form pinching to the normalized centered interval. It should not be represented as a formal proof of the existence of Levi-Civita/Ricci for every Mathlib metric, or as progress resolving the substantive existence question in Yau Problem 26.