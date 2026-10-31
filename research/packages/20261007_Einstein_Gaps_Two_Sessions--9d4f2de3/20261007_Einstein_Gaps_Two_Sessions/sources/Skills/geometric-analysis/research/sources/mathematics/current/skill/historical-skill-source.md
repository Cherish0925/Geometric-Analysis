---
name: qiushi-yau26
description: >-
  Yau 26 research mathematics and shared computation. Via run_shell:
  qiushi-yau26 COMMAND. doctor --json [--full]; examples list/show;
  curvature [--ricci-only]; linearize; search; ricci|pinching --lower ...
  --upper ... [--non-strict]; certify; verify; lean. Use --help for inputs.
  Box checks: --max-cells, --checkpoint, --resume.
  env numeric|sage|pde|ode PROGRAM ARGS runs custom programs;
  demo runs backend examples. JSON: --output NEW.json. Paths use cwd;
  run_shell/bg_task output parents need write_paths kind=directory.
  research/20260921.md and references/research-map.md lead to three connected
  scientific lines: integral rigidity; pointwise A1/log-Weyl, E_D and closed
  shear constructions; global Einstein existence on the same smooth manifold.
  scripts/reproduce.py
  runs standalone mathematical checks; references/reproduction.md explains
  scope. Computational appendices retain locally corrected historical work.
  Read proofs with their hypotheses. Research routes remain open.
---

# Geometry / Yau 26

Use these shared capabilities through shell, this Skill, another Skill or an
MCP adapter. They have the same underlying implementation. Explore other tools,
representations and purely analytic approaches whenever useful; the inventory
does not rank methods or limit the research problem.

## Commands

```bash
qiushi-yau26 doctor --json
qiushi-yau26 examples list
qiushi-yau26 examples show root-box --output Sessions/<session_id>/workspace/data/yau26/check.json
qiushi-yau26 certify Sessions/<session_id>/workspace/data/yau26/check.json --output Sessions/<session_id>/workspace/data/yau26/certificate.json
qiushi-yau26 verify Sessions/<session_id>/workspace/data/yau26/certificate.json
qiushi-yau26 ricci Sessions/<session_id>/workspace/data/yau26/metric.json --lower 1/2 --upper 3/2
qiushi-yau26 env numeric python Sessions/<session_id>/workspace/scripts/custom.py
qiushi-yau26 env sage sage Sessions/<session_id>/workspace/scripts/geometry.sage
qiushi-yau26 env pde python Sessions/<session_id>/workspace/scripts/pde.py
qiushi-yau26 env ode capd-config --cflags --libs
```

Use `--help` on any subcommand for exact arguments. All outputs are JSON except
the program executed by `env`. Exit 0 means the command's declared result was
produced; it does not upgrade `numeric_candidate` to proof. Exit 1 means a
negative, inconclusive or failed check, and exit 2 means an input/runtime error.
Output files must be new paths. Authorize their parent directory using
`write_paths=[{"path":"Sessions/<session_id>/workspace/data/yau26","kind":"directory"}]`
and place outputs inside that directory. Atomic publication needs this directory
scope, not a single-file mount. File paths are not commands and are not expanded.

Scientific Python/SymPy/Arb, SageManifolds, CAPD validated ODE, FEniCSx with
PETSc/SLEPc/MPI, and the configured Lean/Mathlib project are available through
the release adapters. Existing unrelated tools continue to work directly.
Long computations use the normal `bg_task` facility and task-owned outputs;
the chosen method determines whether it supports checkpoints.

## Results and mathematics

`curvature` returns coordinate expressions and conditions; `--ricci-only` skips
the full Riemann array and wedge operator. `ricci` derives Ricci directly from
the input metric and checks `lower*g < Ricci < upper*g` over its closed box.
`pinching` instead checks sufficient curvature-operator inequalities; it is not
a substitute for Ricci bounds. `--non-strict` includes equality in either
command; metric positive definiteness is still required. Neither assembles a closed manifold, proves
global coverage, or rules out metrics outside a chosen family.

`certify` supports positivity, symmetric generalized matrix bounds and root
boxes. `verify` recomputes from the original specification with the pinned
checker. Keep the certificate and its release identity. `inconclusive` is not
a negative theorem. Numerical searches and discrete PDE spectra remain
numerical results. `lean` checks the specified theorem's transitive axioms;
statement correspondence and the trusted Lean environment remain separate.

For subdivision checks, `--checkpoint new-state.json` saves atomic progress.
Continue with the same input and options plus `--resume old-state.json`, a
larger total `--max-cells`, and a new checkpoint/output path. The saved coverage
and accepted leaves are revalidated; failed parent regions are not searched
again. SIGTERM/interrupt preserves the last complete checkpoint; SIGKILL may
lose work after the last periodic snapshot. These checkpoints do not apply to
arbitrary ODE/PDE programs or single `root_box` checks.

`linearize` accepts both equation Jacobians and `qiushi.metric-variation.v1`
for exact derivatives of a declared metric family. Use `examples show
metric-variation`; this does not impose a PDE gauge or provide an inverse bound.

The original Yau 26 statement must be checked against its primary source before
claiming a solution; the package name does not supply its missing hypotheses.

[Formats, mathematical conventions and complete examples](references/formats.md)
provide further detail and can be read progressively as needed.

## Research papers

[Research synthesis](research/20260921.md) connects three scientific questions,
their proofs, constructions and open problems. The working question is whether,
for every dimension, some dimension-only Ricci interval forces the same closed
smooth manifold to carry an Einstein metric of any sign. It is not yet solved.
The latest manuscripts include an integral Ricci gap for specified actual
monopole families, fixed closed integer-shear constructions, weighted local
repair obstructions, and restrictions on all Einstein outputs on specified
smooth types. These extend the earlier exact gap, A1 and E_D arguments;
they do not establish a general existence theorem or an all-sign counterexample.

[Research map](references/research-map.md) locates propositions, derivations,
sources, useful failed approaches and unfinished connections across the papers.
Its categories are navigation, not a fixed list of original achievements.
[Mathematical positioning](references/positioning-20260921.md) compares the
relative Einstein-defect gap with LeBrun's absolute Ricci-energy theory and
identifies the specific strengthening, its proof mechanism and open extensions.
The optional [source inventory](references/source-coverage.json) contains the
original coverage tables, current computational locations and later manuscript
integrations; consult it for a particular source rather than loading it with
the papers. The three lines organize current mathematics; they are neither
an exhaustive classification nor a priority order. Choose by the mathematical
question and applicable evidence, not by a fixed Session role:

1. [Integral rigidity and extensions](research/20260921_rigidity.tex): bounded
   weighted spinors, second-order integral estimates, a smooth Weyl model,
   and weak Bianchi self-testing produce a gap without geometric compactness.
   Actual monopole classes and their square cost remain essential hypotheses.
   The stated blow-up near-Einstein gap is no longer open. Metric-dependent
   class selection, realizable calibration models, boundary flux, new gauge
   equations, positive curvature and higher dimensions are distinct extensions.
   The [earlier rigidity paper](research/20260916_rigidity.tex) retains the
   local-development, spinor/Walsh and flow arguments. The
   [uniform-gap paper](research/20260916_uniform_gap.tex) contains the dedicated
   exact-Einstein proof; spinor/Walsh analysis and local-flow methods retain
   their separate assumptions.
2. [Constructions and full-mode repair](research/20260921_construction.tex):
   three distinct mechanisms: fixed A1 resolution by core correction/log-Weyl
   matching; fixed E_D bundles by slow interpolation and balanced collars;
   and closed product-block gluing separating mapping-class variation from
   integer shear. Weighted receiver estimates enlarge the E_D repair analysis.
   Full kernels, Schur complements, nonlinear estimates and marked end matching
   determine exact repair; validated Newton conditions give a separate route.
   The [earlier construction paper](research/20260916_construction.tex) retains
   the detailed foundational constructions.
   ALE extensions, flux, spikes and multi-node analysis support this question.
   The two-pole spherical fillings include a definite smooth type; the
   positive and negative GH-separation results concern nearby normalized
   exact metrics, not all Einstein metrics on the resolution.
3. [Global Einstein determination](research/20260921_global.tex): decide
   existence or nonexistence on the same smooth manifold. Follow the actual
   object: E_D curvature extrema, attainment and general Einstein restrictions;
   harmonic structure; graph-manifold
   connectors and shared end data; algebraic smoothing and new complex
   structures; torus rods/corners, covers and higher dimensions.
   Closed shear examples add fundamental-group, ordinary basic-class,
   non-virtual-Kähler and local-isometric-symmetry restrictions. Absence of
   local Killing fields does not exclude small nonsymmetric Einstein repairs.
   Free-circle boundary connectivity and two-ended approximate metrics concern
   different equations. Tree actions, attainment and matching remain open
   ways to reach a full global decision. The
   [earlier global paper](research/20260916_global.tex) retains the OT
   critical-point/Morse result specifying necessary base and end types.
   AH end flattening retains its local estimate; a fixed closed connector
   still needs physical-scale, lattice and volume compatibility.

The A1 and E_D constructions have separate proof chains. The E_D construction
also supplies upper bounds in its global variational theory; these shared
arguments remain connected, irrespective of how a future paper is divided.
Common resources are:

- [Twelve-round proofs and calculations](references/rounds/README.md): complete
  original arguments, explicit models and 57 executable calculations. The
  [proof index](references/rounds-index.md) connects these to the three papers;
  no earlier Session directory is needed to read or rerun them.

- [Problem and mathematical foundations](research/20260910.tex):
  quantifiers, normalization, literature, hypotheses, a proved perturbation
  radius and the complete kernel/obstruction equation.
- [Extended constructions and analysis](research/20260912.tex):
  full arguments on ALE and algebraic geometry, scalar corrections,
  surface bundles, Weyl identities, harmonic methods and adapted equations.
  These detailed proofs remain part of the research, not background to discard.
- [Computational methods](references/computations.md) and
  [experimental coefficients and parameters](references/experiments.md):
  accumulated symbolic programs, finite calculations, numerical experiments
  and formalized small statements. Read local corrections with historical
  output; a stored success label is not a mathematical premise.
- [Independent computation](references/reproduction.md): runnable checks with
  packaged inputs, commands and exact/numerical scope. Start here for fresh
  calculations rather than executing a historical Session-bound script.

Use standard mathematical English for research exposition and new formal
statements. The synthesis, research map, three main papers and dedicated
uniform-gap proof are in English. The two earlier manuscripts and historical
appendices retain their original language and detailed derivations; they
remain substantive references, not material replaced by translated summaries.

These are mathematical research materials, not only literature background.
Read definitions, proofs and applicable conditions together; distinguish a
proved obstruction from a failed ansatz or an unproved implication. Develop
new constructions and methods wherever the mathematics leads; the papers do
not assign fixed roles or prescribe one research route.

Research papers are directly in `research/`; tool formats and computational
appendices are directly in the sibling `references/`. Search headings or
program names, then read long passages with `start_line` / `max_lines`.
Work in the current Session's workspace when running or extending a program.
The Skill does not alter a Session's goal, progress or handoff. Use its results
alongside the current workspace, and revise or extend any route as warranted.
