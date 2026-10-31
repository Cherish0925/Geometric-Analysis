# Localized coefficient, full radial cost and global torsion cancellation

28 September 2026. Base commit: `105df84343dfb8f304255b71ca431b5a0293d813`.
Local branch: `local/yau26-cell-cost-20260928`.
This is continued mathematical work in the existing research tree.
No web package, publication, upload, live-system change or installed-Skill
change was made. The original research and archive trees were preserved.

## What changed mathematically

[I55](../continuation/20260928_localization_and_coupled_filling.md)
proves a first-coefficient result with arbitrary interior metrics.
The precise exterior budget replaces small perturbations, individual
core identification, and smooth interfaces. The equality statement
identifies the volume and curvature energies of the whole complement.
The more general non-Einstein exterior version retains its additive
defect. Section 4.1 identifies an intrinsic integral selection sufficient
for this conclusion without a reference metric. It does not supply
that selection from every near-minimizer.

The actual one-bolt construction problem was continued beyond a
neighborhood calculation. Section 8 integrates one exact combination
of the full Ricci residual and retains every orthogonal square.
It excludes all diagonal almost-Kahler profiles before conformal
change, without smallness of F or w. Arbitrary conformal profiles
must enter a specific signed gradient window. An actual conformal
bump makes the leading moment exactly zero while retaining positive
full cost, so that moment cannot be used alone.

Section 9 combines this identity with the actual scalar-transfer
remainder. Any fixed improvement in the shrinking-bolt regime must
carry a nonzero rescaled conformal-gradient payment at shrinking
canonical radii, while its complete background modification remains
nonshrinking. This is a necessary two-scale structure, not a proof
that the two mechanisms cannot coexist. It sharpens the actual
construction problem rather than adding an arbitrary regularity premise.

[The zero-end continuation](../continuation/20260928_signed_quartic_flux.md)
first keeps the complete Chern transgression and completes the Weyl
square. Global Stokes then moves the transition flux to the bulk.
Continuing further, closed central curvature and the weighted
Lichnerowicz identity cancel the determinant and scalar derivative
payments exactly. The positive characteristic budget cancels as well.
The final equation (6.6) contains a single intrinsic trace-free-Ricci
pairing against the full mixed-handed matrix, coupled to a signed
Weyl square difference. It is not an endpoint gap. Testing the actual
unnormalized torsion recovers the same cancellation, including all
radial and cutoff terms.

O10 and the unrestricted O11 remain open. I40/I41's linear order and
scalar-variance-free coercivity were used as the existing baseline,
not counted again or reopened.

## Parallel derivations and independent checks

Three existing Astra research contexts were resumed for bounded tasks;
they were not three newly isolated contexts in this continuation.
The main agent was the sole file writer.

- `cell_variational_push` pursued the complete profile cost, first
  through nonlinear and Hessian comparisons and then through the
  global radial moment. It derived the all-AK exclusion, the exact
  conformal window and the two-scale consequence, and tested an actual
  negative-mode route with every transition included.
- `subfour_construction` independently audited the localized proof,
  proposed the arbitrary-exterior and intrinsic-budget extensions,
  checked the nonlinear profile theorem and radial boundary constants,
  constructed the actual zero-moment bump, and checked the two-scale
  normalization. It also independently checked every sign in the final
  zero-end central/scalar and mixed-curvature cancellation.
- `zero_signed_prolongation` derived the complete quartic flux,
  Euler multiplier, Stokes continuation, calibrated quadratic form,
  central/scalar cancellation and final mixed Ricci identity. It read
  the integrated manuscript and confirmed that no positive budget was
  silently retained after cancellation.
- The main agent derived and proved the localized coefficient,
  equality-energy and intrinsic-bulk results, checked the extensions
  and radial moment independently, implemented the actual profile search,
  retained failed construction outcomes and assembled the continuous
  proofs and their exact continuation points.

These are scoped derivations and cross-checks, not external certification
of the entire project or a claim of literature priority.

## Classical inputs

The localized argument uses closed Chern--Weil and signature identities
and weighted Cauchy with its full remainder. The near-Einstein reference
estimate uses the classical Ricci-energy lower bound in LeBrun's
Theorem 4.3, with its actual applicability conditions.

The nonsymmetric almost-Kahler calculation uses the canonical Chern
form and equation (21)/(25) of
[Apostolov--Armstrong--Draghici](https://faculty.fiu.edu/~draghici/research/paperfiles/Math-Ann.pdf).
The cited formulas were checked in the primary paper. This identity
and its consequences are distinguished from the current project's new
range statements. The zero-end weighted Lichnerowicz and Chern identities
are likewise classical; the complete actual-field cancellations and
their unresolved remainder are written out rather than attributed to
an unnamed general principle.

## Reproducible algebra and implementation checks

The following commands pass:

```bash
python3 tools/check_relative_cell_cost.py
OPENBLAS_NUM_THREADS=1 python3 tools/check_coupled_cell.py
python3 tools/check_signed_quartic_flux.py
```

They contain 23, 5 and 5 tests respectively. The 33 checks cover
inherited relative formulas and the new exterior remainder, radial
boundary moment, full-square and two-scale algebra; an independent
Bianchi-IX Ricci/conformal implementation; analytic complex-step
derivatives and refined quadrature; complete Weyl/cubic wedge signs;
the calibrated quadratic identity; and weighted Clifford/cutoff and
central/scalar cancellation. They do not prove analytic existence,
the automatic bulk selection, or the missing strict endpoint estimate.
The 15 inherited checks in `tools/check_marked_centers_and_harmonic_slices.py`
also pass, including catalogue identifiers and dependencies. The current
catalogue keeps I40/I41 and I55 as manuscript theorems and O10/O11 open.

## Actual construction searches

Every parameter vector in `tools/search_coupled_cell.py` defines a
positive smooth ordinary-bolt metric with a full unchanged CH collar.
F, anisotropy w, and conformal factor phi are optimized together.
All transition regions enter the cost. The listed minima are numerical,
not certified infima.

| Bolt radius | Outer radius | Modes per profile | Starts | Lowest refined J/(2 pi squared) |
| --- | --- | --- | --- | --- |
| 0.1 | 1 | 5 | 3 | 4.052345152642925 |
| 0.2 | 4 | 9 | 8 | 4.162710092036585 |
| 0.03 | 3 | 12 | 12 | 4.003604484077047 |
| 0.5 | 8 | 10 | 5 | 5.065274136748879 |

The 28 starts produced no cost below four. Coarse/refined cost
differences were below 7.2e-13; refined scalar-identity errors were
below 3.4e-13. Parameters and receipts are retained in
[small](computations/20260928_coupled_cell_small.jsonl),
[wide](computations/20260928_coupled_cell_wide.jsonl),
[small-bolt](computations/20260928_coupled_cell_smallbolt.jsonl), and
[large](computations/20260928_coupled_cell_large.jsonl).

The targeted negative-mode search did not merely restart this random
search. It minimized biaxial cost subject to a negative generalized
triaxial Hessian direction, then optimized finite amplitude. The
specified eigenvalue constraint was not met to its requested tolerance;
that optimizer return is recorded as unsuccessful, not rounded into
success. The resulting actual negative direction nonetheless decreases
the complete cost from 12.354924696876633 to 12.335535274566897.
It enters the permitted radial-moment window, but its other squares
keep the cost well above four.

The complete 24-parameter profile and search conditions are in
[the fixture](computations/20260928_coupled_negative_mode.json).
Three quadratures reproduce its cost within 7.1e-15. The last numerical
test above replays the profile and its biaxial base. A separate root
replay of the full joint descent converged in 10 evaluations back to
w approximately zero, with cost 4.162715591768544; its complete output
is [preserved here](computations/20260928_coupled_negative_mode_joint.json).
No floating-point failure to discover a competitor is used as a lower
bound in the manuscript.

## Rendering, preservation and exact continuation

Both continuous MD proofs have editable TeX siblings generated using
the existing renderer. The renderer checks every parsed formula against
the TeX before compiling twice with XeLaTeX. Its exact counts and
warnings are in [the build receipt](20260928_localization_render.json).
The coefficient proof preserves 130 formula nodes and compiles to
12 pages; the flux proof preserves 95 and compiles to eight pages.
Neither reports LaTeX warnings, missing glyphs or overfull boxes.
This is not a new web-review archive.

The repository integrity check compares the preserved baseline and
archived source records byte-for-byte and checks navigation links.
Its machine-readable result remains `catalog/verification.json`.
This preservation check is distinct from mathematical verification.
The completed check confirms all 884 baseline files and 10,191 source
records unchanged, with 828 navigation links checked and no failure.
`git diff --check` also passes.

The next missing mathematical connections are now narrower:

1. Supply the intrinsic bulk selection of I55 from actual unrestricted
   competitive sequences, or realize a lower coefficient outside that
   range. For the complete one-bolt profile route, any fixed improvement
   must satisfy the proved microscopic/macroscopic two-scale conditions
   and simultaneously pay all residual squares.
2. Use the actual cubic provenance and bracket to obtain a strict
   signed estimate in zero-end equation (6.6), together with its Ricci
   pairing. Determinant covariance and scalar radial terms have already
   canceled; do not reintroduce them as unproved absolute-value targets.

Neither a full bubble-tree decomposition nor a new abstract supplier
is imposed as a mandatory route. The existing principal theorem remains
available while these stronger connections remain under investigation.
