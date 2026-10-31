# Computational tools

## Choose by the mathematical question

| Question | Environment / interface | Editable example |
| --- | --- | --- |
| Exact algebra, identities, parameter derivatives, numerical exploration | `qiushi-geometry env core python` (SymPy, NumPy, SciPy, mpmath, python-flint) | `examples/variation.py`, `examples/boundary_value.py`, `examples/ball_arithmetic.py` |
| Coordinates, frames, connections, curvature, differential forms and Hodge star | `qiushi-geometry env sage python` or `... sage file.sage` (SageManifolds) | `examples/hyperbolic4.py` |
| Abstract indices, symmetries, covariant commutators and Clifford algebra | `qiushi-geometry env tensor cadabra2 file.cdb` or `... python file.py` (Cadabra) | `examples/tensor_symmetry.cdb` |
| Triangulations, homology, marked 3D boundaries and Dehn filling | `qiushi-geometry env topology python` (Regina, SnapPy and Sage) | `examples/topology.py` |
| Meshes, weak forms, nonlinear solves and discrete spectra | `qiushi-geometry env pde python` (DOLFINx, PETSc, SLEPc, MPI) | `examples/pde_spectrum.py` |
| Validated finite-dimensional ODE integration | `qiushi-geometry env ode capd-config --cflags --libs`; `qiushi-capd-ivp` | existing `qiushi-geometry demo ode` |
| Named theorem checking with cached mathlib | `qiushi-geometry lean file.lean --declaration geometric_square` | `examples/Polynomial.lean` |
| Literature and mathematical writing | Existing search/HTTP tools, `pdftotext`, `latexmk`, `biber`, `git`, `rg` | manuscript and bibliography in `research/` |

Run `qiushi-geometry info` for this host's selected environments. Run
`qiushi-geometry examples` for installed example paths; copy a useful example
to the research workspace and adapt it. The entry script
`scripts/geometry.py` forwards the same interface where a Skill-relative call
is convenient. Neither command installs dependencies during research.

## Existing geometric algorithms

The shared engine already implements chart-level symbolic Riemann/Ricci/scalar
curvature, coordinate-family linearization, finite-dimensional search, and
Arb-backed finite-box checks. Reuse those implementations:

```bash
qiushi-geometry examples engine
qiushi-geometry curvature metric.json --output curvature.json
qiushi-geometry linearize family.json --output derivative.json
qiushi-geometry search equations.json --output candidate.json
qiushi-geometry certify finite_box.json --output certificate.json
qiushi-geometry verify certificate.json
qiushi-geometry ricci metric.json --lower 1/2 --upper 2 --output bounds.json
```

The compatibility command `qiushi-yau26 examples show <name>` emits the complete
JSON inputs consumed by this existing engine. Its historical name does not
restrict the supported coordinate problems. Use `--help` for each subcommand.
New output files are created atomically: through `run_shell` or `bg_task`,
declare their **parent directory** in `write_paths`, not only the new filename.
Use different output names for independent runs. General Sage, Cadabra and
Python programs remain available when a built-in JSON model is unsuitable.

## Conventions that affect the result

Declare dimension, signature, orientation, Riemann sign, metric scale, Hodge
star, tensor versus curvature-operator norms, and Clifford normalization before
comparing calculations. Use `conventions-and-literature.md` for the included
four-dimensional corpus. The example hyperbolic metric has sectional curvature
`-1`, so in dimension four `Ric = -3 g` and scalar curvature is `-12`.

Cadabra uses the tensor properties supplied by the calculation. Canonicalizing
monomial symmetries does not by itself impose every multi-term Bianchi identity;
declare the appropriate Young symmetry or use the corresponding algorithms.
Sage computes concrete coordinates and frames; it complements this abstract
calculus. Neither engine supplies missing global geometric hypotheses.

Regina supports four-dimensional combinatorial triangulations. SnapPy concerns
three-dimensional hyperbolic manifolds and boundaries. Gmsh and the installed
DOLFINx conventional meshes are at most three-dimensional, not a general 4D
Einstein discretization. PETSc's algebraic solvers can also serve a separately
implemented higher-dimensional discretization. Gmsh is available in the
topology environment for mesh generation; write a mesh file for the PDE
environment instead of mixing binary MPI environments.

SciPy and finite-element spectra support construction and variational work.
Ball arithmetic supplies rigorous finite arithmetic bounds; truncation and
discretization estimates must come from the problem. Lean checks the stated
formal theorem against the selected project and cached dependencies. The
bundled examples demonstrate these distinct interfaces, not a solution of an
open geometric problem.

## Shared execution

The Skill is public research material. Environments are host-owned, versioned
and mounted read-only; outputs and caches stay in the caller's writable space.
Select MPI rank and thread counts for the problem and available resources.
`UCX_TLS=self` is suitable only for a restricted **single-process** check;
do not use it as a distributed-MPI configuration. The PDE environment keeps
its own matching PETSc/SLEPc/MPI libraries.

The default research Python may offer additional optimization or GPU libraries;
reuse those through the platform's Python interface when useful. Wolfram/xAct
are optional alternatives, not dependencies of this Skill. A licensed kernel
must actually run before using that route; the 1F kernel's license was expired
at the 2026-10-04 preparation. No OCR or literature server is required for
ordinary text PDFs or the included TeX sources.

## Primary documentation

- [SageManifolds](https://doc.sagemath.org/html/en/reference/manifolds/)
- [Cadabra algorithms](https://cadabra.science/man.html)
- [SymPy tensor algebra](https://docs.sympy.org/latest/modules/tensor/tensor.html)
- [SciPy integration](https://docs.scipy.org/doc/scipy/reference/integrate.html)
- [python-flint / Arb](https://python-flint.readthedocs.io/)
- [DOLFINx 0.10](https://docs.fenicsproject.org/dolfinx/v0.10.0.post5/python/)
- [PETSc](https://petsc.org/release/manual/), [SLEPc](https://slepc.upv.es/release/documentation/)
- [Regina](https://regina-normal.github.io/), [SnapPy verification](https://snappy.computop.org/verify.html)
- [Gmsh](https://gmsh.info/doc/texinfo/)
- [Lean/mathlib](https://leanprover-community.github.io/)

Use documentation matching the installed versions shown by the environment,
not an assumption that a website's latest release is already installed.
