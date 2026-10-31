---
name: qiushi-yau26
description: >-
  Yau 26 mathematics and shared computation. Via run_shell:
  qiushi-yau26 COMMAND. doctor --json [--full]; examples list/show;
  curvature [--ricci-only]; linearize; search; ricci|pinching --lower ...
  --upper ... [--non-strict]; certify; verify; lean. Use --help for inputs.
  Box checks: --max-cells, --checkpoint, --resume.
  env numeric|sage|pde|ode PROGRAM ARGS runs custom programs;
  demo runs backend examples. JSON: --output NEW.json. Paths use cwd;
  run_shell/bg_task output parents need write_paths kind=directory.
  research/20260916.md introduces the mathematical papers:
  Ricci pinching, uniform Einstein topology gaps, near-equality rigidity,
  ALE/log-Weyl constructions, global topology and connectors.
  Full 20260910.tex/20260912.tex derivations and thematic proofs are in research/;
  references/computations.md and experiments.md contain mathematical
  programs and results. Use, extend or challenge the arguments under
  their stated hypotheses. Research routes remain open.
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

[Research synthesis](research/20260916.md) connects the question, mathematical
methods, deductions and unresolved problems. Choose material by the problem you
are working on:

- [Problem and mathematical foundations](research/20260910.tex):
  quantifiers, normalization, literature, hypotheses and possible approaches.
- [Extended constructions and analysis](research/20260912.tex):
  detailed arguments on ALE and algebraic geometry, scalar corrections,
  surface bundles, Weyl identities, harmonic methods and adapted equations.
- [Uniform topology gap](research/20260916_uniform_gap.tex):
  the complete proof manuscript for the exact Einstein theorem and its
  separate conditional extension.
- [Rigidity and degeneration](research/20260916_rigidity.tex):
  curvature budgets, near-equality densities, local estimates, weighted
  energy, necessary degeneration and the remaining near-Einstein analysis.
- [Near-Einstein constructions](research/20260916_construction.tex):
  core corrections, logarithmic interpolation, full pointwise estimates,
  flux identities, angular modes and multi-node geometry.
- [Global geometry and topology](research/20260916_global.tex):
  surface bundles, graph manifolds, smoothing, charged local models,
  global compatibility and two-ended matching.
- [Computational methods](references/computations.md) and
  [experimental coefficients and parameters](references/experiments.md):
  symbolic programs, finite calculations, numerical experiments and
  formalized small statements.

These are mathematical research materials, not only literature background.
Read definitions, proofs and applicable conditions together; distinguish a
proved obstruction from a failed ansatz or an unproved implication. Develop
new constructions and methods wherever the mathematics leads; the papers do
not assign fixed roles or prescribe one research route.

Research papers are directly in `research/`; tool formats and computational
appendices are directly in the sibling `references/`. Search headings or
program names, then read long passages with `start_line` / `max_lines`.
Work in the current Session's workspace when running or extending a program.
