# Input Formats and Methods

Expressions use declared variables, exact decimal/rational literals, `+ - * /
**`, parentheses and `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`. Powers must be
integers; use `sqrt` for square roots. `pi` is available. No Python evaluation,
attributes, indexing or imports are accepted in an expression. JSON exact
endpoints are integers or strings, not floating-point JSON numbers.

## Coordinate metric

```json
{
  "schema": "qiushi.metric-chart.v1",
  "coordinates": ["theta", "phi"],
  "parameters": [],
  "metric": [[1, 0], [0, "sin(theta)**2"]],
  "box": {"theta": ["1/2", "1"], "phi": ["0", "1"]}
}
```

`curvature metric.json` computes Christoffel symbols, Riemann tensor, Ricci,
scalar curvature, trace-free Ricci and the induced wedge metric. Convention:
`R^i_jkl = d_k Gamma^i_lj - d_l Gamma^i_kj + Gamma^i_km Gamma^m_lj - Gamma^i_lm Gamma^m_kj`;
`Ric_jl = sum_i R^i_jil`. The unit sphere has positive scalar curvature 2.
The metric must be symmetric and nonsingular. Positivity, original expression
domains and global assumptions are conditions, not silently discharged claims.
Parameters may be declared after coordinates; they are not differentiated as
coordinates. A proportional Ricci tensor alone does not certify a constant
Einstein factor in dimension two.

`pinching metric.json --lower 1/2 --upper 2` creates a finite certificate using
all variables' box ranges. It proves strict inequalities via positive
definiteness of `g`, the wedge metric `B`, `A-lower*B`, and `upper*B-A`, where
`A` is the curvature operator in the wedge basis. This sufficient condition
can be stronger than sectional pinching. Unresolved inequalities return
`inconclusive`, never a global obstruction. The coordinate box, not a whole
closed manifold, is the coverage domain. Coordinate singularities require
other charts and separately established transitions and coverage.

## Finite rigorous checks

```json
{
  "schema": "qiushi.finite-check.v1",
  "kind": "root_box",
  "variables": ["x", "y"],
  "expressions": ["x**2-2", "y-x"],
  "box": {"x": ["7/5", "3/2"], "y": ["7/5", "3/2"]},
  "precision_bits": 128
}
```

`root_box` needs as many equations as variables and a box with interior. It
verifies a Krawczyk self-map strictly inside the box and an infinity-norm
contraction, using a rational midpoint preconditioner and Arb enclosures.
Together these give existence and uniqueness in the specified box. A singular
preconditioner or wide enclosure returns `inconclusive`; other root boxes may
still work. Original expression domains are evaluated before simplification.

`positive_box` uses the same schema, variables, expressions and box, and proves
all expressions strictly positive throughout the box. `matrix_bounds_box`
instead takes symmetric square `matrix` and `metric` arrays plus `lower` and
`upper` rational bounds. The metric must be positive definite. Full examples
are available via `examples show positive-box` and `examples show matrix-bounds`.

Set `strict` to the JSON boolean `false` for non-strict scalar/matrix bounds.
For example, `examples show semidefinite-bounds` gives a variable Gram matrix
with a genuine zero direction. The checker uses certified positive Schur pivots,
nonnegative diagonal blocks and exact zero blocks without adding epsilon.
If this sufficient criterion cannot certify a matrix, the result stays
inconclusive. Equal lower/upper constants are allowed only in non-strict mode.
The reference metric must be strictly positive definite in either mode.

`metric_ricci_box` embeds a `metric_chart`, `box`, `lower` and `upper`. It derives
Ricci from that chart; `qiushi-yau26 ricci metric.json --lower 1/2 --upper 3/2`
constructs this specification automatically. Add `--non-strict` to include
equality. `examples show product-spheres` has Ricci=g but zero mixed sectional
curvatures, so it distinguishes this command from the original `pinching`
curvature-operator test. Scaling g changes the constants relative to g; constants
are never silently normalized. The certificate embeds the original chart and
derived tensor, not a separate matrix whose relationship to the metric is assumed.

Box checks bisect at exact rational midpoints and prove every accepted leaf.
`max_cells` defaults to 4096 and is configurable. `precision_bits` defaults to
128 and is configurable from 64 to 16384. Resource exhaustion is inconclusive.
A certified nonpositive midpoint disproves a strict scalar positivity claim;
a failed sufficient matrix criterion is not interpreted as a geometric
counterexample. Receipts include the full input, its hash, checker identity and
the bounded conclusion. They do not execute user-supplied verifier code.

For scalar/matrix/metric box checks, `--checkpoint new.json` writes a complete
snapshot initially, every 32 inspected cells, and at a safe finish/interrupt
boundary. `--checkpoint-every N` adjusts the snapshot interval. Each snapshot
is atomic; use a new path, not an old input/result/checkpoint. Resume using the
same input/precision with `--resume old.json --max-cells N`. The budget N is
the total, including previously inspected cells. Increase it to do more work.
Changing the mathematical input or checker requires a fresh run. Unlike normal
input JSON, a generated checkpoint is not restricted to the 16 MiB input size;
loading it uses memory proportional to the retained cover.

Resume reconstructs all rational cells from the original box and split tree,
rejects missing/overlapping/unreachable cells, and rechecks certified leaves
and terminal findings. It does not repeat subdivision of already explored
parents. SIGTERM and keyboard interrupt attempt to save the last complete
state; SIGKILL only leaves the last already-published snapshot. Root-box checks
are single checks and do not use this subdivision recovery mechanism.

Old certificates keep their original immutable release; `verify` rejects a
different checker instead of silently changing the meaning of an old proof.

## Search and differentiation

```json
{
  "variables": ["x", "y"],
  "expressions": ["x**2-2", "y-x"],
  "initial_guess": ["1", "1"]
}
```

`linearize` returns the finite-dimensional Jacobian. `search` runs a SciPy
root search and saves a numerical candidate. It neither supplies PDE gauge
fixing nor proves a root. Use surrounding rational root boxes for subsequent
validation, or write another search algorithm using `env numeric python`.

`linearize` also accepts `qiushi.metric-variation.v1`: `metric_chart`, a declared
`parameter`, and exact rational `at`. See `examples show metric-variation`.
It returns the exact parameter derivatives of the metric, inverse metric,
Christoffel symbols, Ricci tensor, scalar curvature and trace-free Ricci.
The family must be smooth with a positive metric near the evaluation parameter;
the reported chart conditions remain obligations, not a global existence claim.
No diffeomorphism gauge, boundary conditions or function-space inverse is chosen.

## ODE, PDE and Lean

`qiushi-yau26 env ode qiushi-capd-ivp 'var:x,y;fun:y,-x;' 1 20 1 1 0 0`
integrates the oscillator to time 1, Taylor order 20, from `[1,1] x [0,0]`.
Arguments are finite binary64 values; the returned hexadecimal endpoints
represent those binary numbers exactly. For decimal/scientific input the
problem solved uses the parsed binary64 numbers, not an unrecorded exact
decimal. Use outward-rounded endpoint arguments to enclose exact input data.
This is a validated initial-value endpoint, not a global boundary-value or
Einstein existence certificate. The full CAPD C++ library and `capd-config`
support custom programs, including augmented systems and other library methods.

`qiushi-yau26 env pde python script.py` selects the isolated FEniCSx/PETSc/SLEPc
environment. `env pde mpiexec -n 2 python script.py` is available for actual MPI
programs under the existing task resource contract. `demo pde` runs Poisson
and Dirichlet eigenvalue grid-refinement checks. These are numerical checks;
continuous inverse bounds, truncation error and infinite-dimensional tails
remain separate mathematical obligations.

`qiushi-yau26 lean Proof.lean --declaration MyNamespace.myTheorem` requires a
named theorem, fresh compilation and a transitive axiom list. Only `propext`,
`Classical.choice` and `Quot.sound` are admitted by this checker. Imported
`sorryAx` and extra axioms are rejected. `--timeout` configures the compilation
wait; the default is 300 seconds. The existing Lean project and compiled
dependencies are trusted inputs. This does not assert natural-language
correspondence or replace an independent kernel/artifact audit.
