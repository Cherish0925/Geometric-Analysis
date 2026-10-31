# Independent Computation and Reproduction

These programs use inputs bundled with the Skill. They do not read old Sessions,
Knowledge, network resources or other users' directories. They recompute the
specified algebraic and local curvature quantities from definitions. The
four-node group checks the interpretation of a saved matrix, not the infinite
spectral sum. See the [papers](../research/20260921.md) for the analytic arguments.

## Twelve-round calculations

The [proof library](rounds-index.md) includes all 57 original Python programs
from the twelve rounds. They use the standard library, SymPy and mpmath; the
recorded environment is Python 3.12.13, SymPy 1.14.0 and mpmath 1.3.0.
They need neither the original Sessions nor an external API or GPU.

```bash
qiushi-yau26 env numeric python Skills/qiushi-yau26/scripts/reproduce_rounds.py --proof-dir Skills/qiushi-yau26/references/rounds --output Sessions/<session_id>/workspace/data/yau26-rounds-NEW --jobs 2
```

For an individual calculation:

```bash
qiushi-yau26 env numeric python Skills/qiushi-yau26/references/rounds/round11_closed_gluing_check.py
qiushi-yau26 env numeric python Skills/qiushi-yau26/references/rounds/round12_repair_check.py
```

The runner creates a new output directory, executes at most two programs at
once, limits each to 120 seconds and 4 GiB address space, and records actual
outputs, hashes, exit status and environment. It does not modify the Skill.
The [stored twelve-round execution](rounds-results/summary.json) and individual
logs are retained with matching source hashes. Use the new output directory
for a fresh run, rather than treating stored output as a new execution.

These calculations check polynomial/Clifford contractions, coordinate Ricci
blocks, finite integer presentations and model coefficients. The spinor
Hessian estimates, weighted inverses, gluing analysis, basic-class theorems,
Killing continuation and literature novelty require their mathematical
arguments; process exit zero alone does not establish those results.

## Running the checks

From the current user root, use the existing numerical environment:

```bash
qiushi-yau26 env numeric python Skills/qiushi-yau26/scripts/reproduce.py --output Sessions/<session_id>/workspace/data/yau26-reproduction-NEW
```

Alternatively, run `scripts/reproduce.py` with Python providing SymPy and NumPy.
The output directory must be new. For `run_shell` or `bg_task`, authorize its
parent through `write_paths` with `kind=directory`. The program writes only the
specified result directory, never the Skill.

All eight groups run by default. Add `--group four_node` to select one, or repeat
`--group` for several. Each produces a JSON result; `manifest.json` records
dependency versions, input hashes, results and timing. Exit 0 means all selected
checks passed; 1 means a check failed; 2 means invalid arguments or output path.
Checks remain active under `python -O`. Existing output directories are refused.

## Scope of each group

| Group | Recomputed input | Result and scope |
| --- | --- | --- |
| `uniform_gap` | Completion of squares, calibration density, Noether ratio, Weyl eigenvalues and the earlier SW ratio elimination | Exact checks of 109, 436, 675, 42 and their conditions. Does not replace Cheeger–Tian regularity, local unfolding or limit transfer, or compute the nonexplicit gap constant. |
| `weyl10` | Ten independent Weyl tensors in the self-dual and anti-self-dual blocks; full Ricci linearization | Checks curvature symmetries, Bianchi, trace/divergence/harmonic/radial conditions and the logarithmic identity for arbitrary radial second jets, not merely selected powers. Does not bound global nonlinear gluing errors. |
| `ed_ricci` | Moving-frame structure equations, Koszul connection, curvature and every Ricci component | Checks mixed terms, quadratic terms, scalar curvature and the matrix spectrum. Local formulas do not establish global smooth matching or Einstein nonexistence. |
| `cz_spike` | All first/second derivatives of the spike and full opposite-warping moving-frame curvature | Verifies Hessian cancellation in Ricci, retained mixed derivatives in Riemann and the nonzero background energy. Grid diagnostics are not global bounds or interval certificates. |
| `four_node` | Bundled historical truncated matrix, source/receiver coordinate changes and five node-pattern rows | Distinguishes trace, trace-free diagonal and off-diagonal response and checks necessary inequalities. Does not recompute the spectrum, certify its tail, or solve the complete Lyapunov–Schmidt/global Einstein problem. |
| `ot_critical` | Trace-free Hessian cancellation, critical-point threshold, rational bracket for the OT constant | Finite algebra; completeness, heat-kernel estimates and the Morse argument are in the paper. |
| `ah_matching` | Gaussian diagonal Ricci blocks, CGB volume coefficient and physical scaling | Does not construct a closed connector or solve problem W. |
| `two_pole` | Integral handle-form changes, parity and the two-sign truth table | Smooth topology also requires the actual marked gluing and smooth torus action. |

Programs: [reproduce.py](../scripts/reproduce.py) and
[math_checks.py](../scripts/math_checks.py).
Input: [four_node_fixture.json](../scripts/data/four_node_fixture.json).
The [computational](computations.md) and [experimental](experiments.md) appendices
retain original programs, parameters and outputs, with corrections beside
the affected material. Locate them by program name.

### Four-node coordinates and normalization

The saved matrix maps `(S22,S33,2*S23)` to `(R22,R33,R23)`. The factor 2
accounts for contraction over both off-diagonal indices of a symmetric tensor.
The trace, trace-free diagonal and off-diagonal tensors each have
Hilbert–Schmidt norm √2. Their coordinate inputs are `(1,1,0)`, `(1,-1,0)`
and `(0,0,2)`. The saved adjacent matrix should respectively return `0`,
`(2q,-2q,0)` and `(0,0,-2q)`. Zero trace response cannot test the nonzero
trace-free coefficient.

Decimal matrix entries are read exactly as regression inputs; this does not
make the original truncated spectral approximation an exact spectral value.
The five rows comprise one compatible and four mixed patterns on the fixed
positive background, under square-adjacency-preserving node permutations.
This neither identifies global chirality reversal as a full geometric
equivalence nor enumerates every marked filling.

### Spike energy and numerical domain

Historical parameters are `rho=0.30`, `Lambda=5,10,20,50,100,200,500`,
`sigma=exp(-Lambda)` and amplitude `Lambda^(-2/3)`.
The numerical diagnostic uses a 384×64 inner-disk grid with lower radius
`max(sigma/10,1e-14)`. It omits the smaller core and cutoff annulus.
The central value is computed separately by an exact formula.

Small perturbation-Hessian energy does not remove background curvature on
a fixed region. With the full four-index norm, the closed manifold S²×S²
satisfies ∫|Rm|² = 128π² + 4∫|Ric°|², so total energy cannot tend to zero.
A smaller ball chosen first controls its background contribution; that is
different from a perturbation limit on the same fixed ball.

## Failure tests

Every group requires rejection of a deliberately incorrect variant, such as
a changed calibration coefficient, omitted mixed Ricci component, reversed
mixed-derivative sign or missing off-diagonal contraction factor.
The four-node CLI also supplies an explicit failure case:

```bash
qiushi-yau26 env numeric python -O Skills/qiushi-yau26/scripts/reproduce.py --group four_node --mutation four-node-zero --output Sessions/<session_id>/workspace/data/yau26-reproduction-bad-NEW
```

This must return 1 with JSON status `failed`; a zero matrix is not a passing
test. Reusing an output directory must return 2. The retained isolated normal
and failure runs are in [reproduction-results.json](reproduction-results.json).

These checks provide a Session-independent entry to selected computations.
They do not require a computational research route or restrict the development
of new proofs, constructions, literature analysis or verification methods.

## Supplemental independent programs

The uploaded report, 39 original programs, original sampled numerical logs and
saved JSON results are retained byte-for-byte inside the two existing appendices.
Corrections beside the affected report blocks govern their interpretation.
The archive can be checked or extracted without any old Session or upload:

```bash
qiushi-yau26 env numeric python Skills/qiushi-yau26/scripts/source_archive.py Skills/qiushi-yau26
qiushi-yau26 env numeric python Skills/qiushi-yau26/scripts/source_archive.py Skills/qiushi-yau26 --extract Sessions/<session_id>/workspace/data/yau26-independent-sources-NEW
```

Extraction preserves the original relative imports but does not execute code.
The new destination is mandatory; altered payloads and unsafe paths are rejected.
For a selected original computation, the checked wrapper reconstructs its
quantities and rejects nonzero residuals, rather than relying on process exit:

```bash
qiushi-yau26 env numeric python Skills/qiushi-yau26/scripts/independent_checks.py --original-check ot --source-root Sessions/<session_id>/workspace/data/yau26-independent-sources-NEW
```

Available selections are `ot`, `core`, `weyl`, `log`, `bundle`, `ah`, and
`bochner`. They cover coordinate OT Ricci blocks; EH core linearization and bolt
matching; Weyl jets; the logarithmic identity in dimensions four and five; the
full ED matrix; sampled nondiagonal Gaussian blocks; and exact rational-jet
Bochner checks. The last two are specific tests, not universal proofs. Symbolic
checks may take minutes; use the existing task timeout and resource controls.

`independent_checks.py` supplies the three new default algebra groups as well.
The reproduction record distinguishes current runs from the source author's
saved output. The other original programs are preserved but not all rerun.
In the recorded Session-independent run, `ot`, `core`, `weyl`, `log`, `bundle`
and `ah` completed; `bochner` exceeded 180 seconds without returning a result.
It is not counted as passed. All eight default finite-check groups completed.
In particular, finite samples of the football metric do not certify a continuous
supremum, and the retained extreme-scale table is not a new certified run.
