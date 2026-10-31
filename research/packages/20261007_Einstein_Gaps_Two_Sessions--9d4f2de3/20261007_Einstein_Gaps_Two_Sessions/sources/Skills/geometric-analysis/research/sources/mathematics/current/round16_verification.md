# Round 16 verification

22 September 2026. Work was performed in an isolated local Git worktree
on Round-15 commit dc33557. No inherited proof file, installed Skill,
live Session, service, model configuration, or shared environment was
modified.

## Executed programs

From this directory:

~~~bash
python round16_rigidity_check.py
python round16_global_check.py
python round16_construction_check.py
python round16_minimal_balance_check.py
~~~

All four were independently rerun by the lead investigator and exited
with status zero. The interpreter was
/data/qiushi/qiushi_engine_v09/.venv/bin/python:
Python 3.12.13, SymPy 1.14.0, mpmath 1.3.0.

| Program | What was checked | Outcome |
| --- | --- | --- |
| Rigidity | Six printed groups: product polynomial, normal derivative, full eight-variable tangent-jet divergence, coercivity, mixed signs of the Einstein polynomial, and constants | Pass |
| Global | Thirteen finite identities/tests: cusp primitive, norm, volume form, height, dilation invariance, hyperbolic monodromy algebra, and normalizations; includes wrong-sign rejection | Pass |
| Construction | Eight new groups, with eight inherited groups freshly recomputed on import: coordinate Ricci variation, corrected divergence and all ten gauged blocks, Maxwell/end conditions, source, length force, and gauge decomposition | Pass |
| Minimal balance | Fourteen exact identities and four nonbalanced negative controls: local harmonic forms, stress, conformality, parallel-area formula, Euler characteristic, and action sign | Pass |

The construction program depends on the unchanged
round14_repair_radius_check.py and round14_shear_check.py.
They are present in this worktree. The other three new programs use
SymPy directly.

The finite-interval Maxwell-profile tests use 55-digit mpmath arithmetic,
with error thresholds \(10^{-47}\). They are numerical checks of the
formulas proved by integration in the note, not interval certificates.
Most coordinate and polynomial calculations are exact symbolic
identities. No sampled maximum is reported as a continuous supremum.

These programs do not verify the classical lattice theorems, existence
of the Schwarz P surface, monopole solvability, the entire compactness
theory, or a nonlinear Einstein solution.

## Independent proof reviews

The rigidity and global investigators reviewed each other's full new
arguments. The lead investigator separately checked the algebraic/PDE
connection and the core-embedding proof. The construction investigator
and global investigator separately reviewed the minimal-surface balance
and second-variation argument.

Specific issues checked were:

- The curvature polynomial has a two-dimensional tangent kernel. The
  calculation uses every tangent first-jet variable, not only a
  rank-one principal symbol. The displayed Gram matrix was also
  compared with the computed matrix.
- Entry into the small algebraic neighborhood uses the previously
  obtained Lipschitz bound before applying the refined PDE estimate.
  Mean-value estimates retain the original ball-volume denominator.
- The logarithmic distance lower bound requires a point with a fixed
  nonzero geometric deviation. No existence of such a point is inferred.
- Noncompactness of the limiting quotient retains the specified
  non-Kähler smooth-type hypothesis; closed products satisfy the
  calibration hypotheses but can have compact equality limits.
- The Sol-group proof handles the normal abelian fixed subtree.
  Neither general solvable-tree fixed-point folklore nor an unproved
  injection of the pointed-limit group is used.
- The compactly supported form is supported in the interior of the
  chosen cusp core. Its extension by zero is closed and smooth;
  nullhomotopy makes its restriction exact. This gives the
  self-intersection contradiction directly.
- The core theorem explicitly requires a quotient preserving both
  factor orientations. Passing to a finite cover is not assumed to
  preserve an embedding into the original target.
- The Maxwell correction retains its nonzero divergence and cubic
  mixed component. Their contributions are included in the all-mode
  integration by parts. The physical end bands are not deleted.
- Harmonic energy is minimized at fixed integral cohomology classes
  while the conformal structure varies. The negative second variation
  uses a normal parallel immersion with no volume-preserving constraint.
  It is not a statement about the complete Hessian signature.

Final synthesis review restored the normalized \(O(c)\) size assumption
in the nonlinear end-response summary and made the non-Kähler
limit hypothesis explicit. All four Python files parsed successfully,
all six Markdown files had balanced math delimiters, and all thirteen
local Markdown links resolved. The staged Git diff was checked for
whitespace errors before commit.

These are bounded proof reviews, not independent certification of
every inherited result. The geometric applications explicitly retain
their Round-15 hypotheses.

## Primary inputs checked

- [Biquard–Gauduchon–LeBrun, equation (2)](https://arxiv.org/pdf/2310.14387):
  the divergence-free Weyl operator equation, including the scalar
  and quadratic coefficients.
- [Li–Schoen, Theorem 2.1 and local equation (2.3)](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6362-11511_2006_Article_BF02392380.pdf):
  volume-normalized mean-value estimates with a Ricci lower bound.
  The note handles the zeroth-order term on a product with a real
  interval and retains the necessary local buffer.
- [Hee Oh, Theorem 1.1](https://bpb-us-w2.wpmucdn.com/campuspress.yale.edu/dist/5/5177/files/2025/11/little.pdf):
  the nonuniform irreducible lattice classification up to conjugacy
  and commensurability.
- [McReynolds, Sections 3.3 and 5](https://arxiv.org/pdf/0706.3580):
  Hilbert modular peripheral groups and the Sol torus-bundle description.
- [Bader–Gelander–Levit, Theorem 1.1 and its following discussion](https://arxiv.org/pdf/2411.07033):
  the normal subgroup input in higher real rank, without assuming
  property (T).
- [Ros, Section 4 and page 538](https://wpd.ugr.es/~aros/wp-content/uploads/2025/02/Ros-JDG.pdf):
  the embedded, separating genus-three Schwarz P surface in a cubic
  flat torus. Its existence is classical input, not a numerical result
  of this round.
- [Ejiri–Micallef, Section 2](https://arxiv.org/pdf/0708.2188):
  the classical energy/area framework. The precise second-variation
  inequality used here is derived directly in the note.

The inherited Cheeger–Tian, monopole, closed-gluing and volume inputs
are recorded in Round 15 and earlier proofs. They were not replaced
by a new unproved regularity statement.

## Remaining mathematical work

The reducible limiting case is not excluded. A product-profile
curvature bound does not identify every end with a chosen construction
collar. The exterior linear and nonlinear response conditions are
necessary, not known sufficient and not proved inconsistent.
Fiber balance is an admissible matching configuration, not an Einstein
solution. None of these results decides larger-volume Einstein metrics
on the same manifold or settles a Yau26 sign branch.
