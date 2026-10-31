# Route assessment: Step 64

Session S0910A01, Agent1 / Orchestrator. Phase: Explore.

## 1. What Step 64 changed

The Step 63 KN sign repair introduced a global convention risk: Step 63 uses
standard KN
\[
G=(g\owedge g)/(2(n-1)),\qquad T=\operatorname{Rm}-G,
\]
while Steps 34--62 were written with `T=Rm+G`. Step 64 performed the needed
cross-note consistency sweep and wrote
`workspace/notes/step64_convention_consistency_sweep.md`.

TTCS (`trace/ttcs/results/step64_ttcs01_verifier1_integration.md`) found that
the first sweep draft was overstrong and identified two real repairs:

1. The two properties `Ric(T)=E` and `nabla T=nabla Rm` alone do not determine
   the auxiliary shift; one also needs that the old `G` was the universal
   `g owedge g` multiple. Under that intended old definition,
   `G_old=-G` and `Rm+G_old=Rm-G`, so the tensor `T` is the same.
2. Step 63's pure-scaling line for `G` missed a factor two. Correctly,
   under pure scaling `partial_t G=-4G`, hence
   `partial_t T=-2T+2G`, not `-2T`. The exact shifted tensor is not
   homogeneous under pure scaling.

Repairs applied:

- `workspace/notes/step63_curvature_variation_index_proof.md` now states the
  operator-normalized curvature norm, keeping `|G|^2=n/(2(n-1))=2/3` in
  dimension four; if the raw four-index contraction were used, the value would
  be `2n/(n-1)`, so the theorem writeup must not mix conventions.
- The stale `T=Rm+G` sentence in Step 63 §4.2 is corrected.
- The false pure-scaling table in Step 63 §9 is replaced by the correct
  non-homogeneous `T` computation; the estimates only use algebraic
  zero-order absorption by `C a F_T^3`, so the curvature endpoint survives as
  an inequality.
- Step 58's stationarity line and schematic zero-order term were annotated so
  the final writeup will not quote the old sign literally.
- `workspace/scripts/step63_curvature_variation_verify.py` was updated and now
  passes 21/21, writing `workspace/data/step63_curvature_variation_verify.json`.
- New structural script `workspace/scripts/step64_convention_consistency_verify.py`
  passes 17/17, writing `workspace/data/step64_convention_consistency_verify.json`.

## 2. Impact on the restricted IL theorem

No curvature or defect Moser estimate changes. The synchronous reflection
`G_old=-G` makes the shifted tensor `T` identical across notes. The bridge uses
only:

- `Ric(T)=E`;
- `nabla T=nabla Rm`;
- `F_T=(1+|T|^2)^{1/2}` and `F_T asymp F`;
- algebraic zero-order control by `C a F_T^3`;
- weighted defect quantities independent of `G`.

Thus the IL analytic bridge remains at proof level as an a priori estimate
stack, but the theorem writeup must use the canonical convention everywhere and
must not copy exact legacy signs involving `G_old`.

## 3. Updated existence-module understanding

I read A03 `workspace/notes/step56_tame_direct_flow_repair.md` and the older
A01 TTCS review `trace/ttcs/results/step61_ttcs01_verifier3_integration.md`.
The status after Steps 62--64 is sharper than the older review:

- For fixed positive `(epsilon,nu)`, A03's doubly regularized transported-DeTurck
  system has diagonal strongly parabolic principal blocks. A named standard
  quasilinear parabolic theorem is now plausible here, because the
  regularization removes the degeneracy.
- The exact degenerate system still cannot be obtained by direct citation of a
  uniformly elliptic theorem. It must be obtained as `(epsilon,nu)->0` from the
  uniform estimates.
- A03 #469 correctly reframes the remaining work: the issue is not the
  existence theorem for the fixed regularized system, but connecting that
  theorem to the already developed regularization-uniform energy estimates and
  smooth-limit passage.
- The older TTCS review also listed missing first-exit estimates and curvature/
  defect endpoints; those have since been supplied by Steps 62 and 63, modulo
  the Step 64 convention repair.

The next IL proof task is therefore concrete: write a self-contained per-datum
existence theorem for the exact degenerate cutoff flow by combining (i) a named
fixed-parameter quasilinear parabolic theorem for the regularized system, (ii)
A03 Step 56's uniform tame hierarchy, maximum principle, and smooth-limit
argument, and (iii) the Step 55--63 a priori estimates. It must be written under
the canonical `T=Rm-G` convention and explicitly avoid using the false pure
scaling of `T`.

## 4. Broader Yau-26 route implications

A03 Step 66 (`Sessions/S0910A03/workspace/notes/step66_curved_slice_collar_assessment.md`)
adds useful independent evidence on the graph-manifold counterexample front:
full 4D Ricci optimization on `T^3 x [-1,1]` with curved `(x,y)`-dependent slices
could not reduce `sup ||Ric+3g||_op` below order-one defects. The model class is
blocked by a two-pronged mechanism: flat-slice self-adjointness forces
`H^2 >= 9-O(delta)`, while activated curved slices push tangential Einstein
forcing toward `Ric_gamma ~ -3 gamma`, impossible on `T^3` by Preissmann-type
negative-curvature topology. This does not settle non-warped graph manifolds,
but it reduces the plausibility of the negative-branch graph counterexample in
four dimensions and keeps the IL gap route as the most developed negative-line
mathematics.

The broader Yau-26 problem remains open: the restricted IL theorem is a strong
family-uniform negative-pinching gap, not a dimension-only theorem over all
closed manifolds; positive branch, arbitrary four-dimensional topology,
dimensions `n>=5`, and Lean formalization remain unsolved.

## 5. Recommended next work

The next step should be Agent2 / Execute on the per-datum existence theorem,
not final expression. It should:

1. Fix the canonical convention page at the start of the theorem writeup:
   standard KN, `G=(g owedge g)/(2(n-1))`, `T=Rm-G`, operator-normalized
   curvature norm.
2. Pin a fixed-parameter parabolic theorem suitable for A03 Step 56's
   regularized system on a closed manifold, and verify strong parabolicity,
   smooth coefficients on the metric-positive open set, compatibility with the
   scalar parabolic block, and short-time smoothness/continuation.
3. Recast A03 Step 56's uniform hierarchy and smooth-limit passage with enough
   detail that no inverse powers of `epsilon` or `nu` enter.
4. Use the autonomous splice/restart logic already developed, but write the
   endpoint smoothness and time-jet matching explicitly; do not invoke raw
   ungauged uniqueness.
5. State exactly how Steps 55--64 feed the observation-time theorem once the
   per-datum existence is obtained.

If this succeeds, the restricted IL theorem becomes an unconditional theorem
within its family. The session should then return to the higher-level Yau-26
question rather than move to final expression for the restricted theorem alone.
