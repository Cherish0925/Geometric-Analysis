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

Box checks bisect at exact rational midpoints and prove every accepted leaf.
`max_cells` defaults to 4096 and is configurable. `precision_bits` defaults to
128 and is configurable from 64 to 16384. Resource exhaustion is inconclusive.
A certified nonpositive midpoint disproves a strict scalar positivity claim;
a failed sufficient matrix criterion is not interpreted as a geometric
counterexample. Receipts include the full input, its hash, checker identity and
the bounded conclusion. They do not execute user-supplied verifier code.

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
