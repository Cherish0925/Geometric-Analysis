---
name: qiushi-yau26
description: >-
  Yau 26 tools and research mathematics. Via run_shell:
  qiushi-yau26 COMMAND. doctor --json [--full]; examples list/show;
  curvature [--ricci-only]; linearize; search; ricci|pinching --lower ...
  --upper ... [--non-strict]; certify; verify; lean. Use --help for inputs.
  Box checks: --max-cells, --checkpoint, --resume.
  env numeric|sage|pde|ode PROGRAM ARGS runs custom programs;
  demo runs backend examples. JSON: --output NEW.json. Paths use cwd;
  run_shell/bg_task output parents need write_paths kind=directory.
  Local certificates are not global proofs; methods remain unrestricted.
  references/research/20260916.tex maps the research: full proofs,
  constructions, mechanisms, failures and open possibilities from Qiushi
  and web research. It routes to the preserved 20260910.tex
  and 20260912.tex, the uniform-gap proof, and rigidity/construction/global
  continuations. Read relevant arguments; reuse, extend or challenge them under
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

## Research mathematics and references

[Integrated research map — 2026-09-16](references/research/20260916.tex) connects
the historical manuscripts, new web research and the three Sessions' concrete
results. It records which arguments live where, corrects conflicting versions,
and keeps broader routes available. This is the entry point, not a replacement
for the detailed proofs. Choose references by mathematical question, not by
Session identity:

- [Rigidity and degeneration](references/research/20260916_rigidity.tex):
  exact Einstein topology gap, near-equality calibration, necessary degeneration,
  and the separate, still conditional near-Einstein smoothing route.
- [Complete uniform-gap proof](references/research/20260916_uniform_gap.tex):
  the supplied September 14 proof manuscript, preserved in full. Its conditional
  extension is separate from its exact Einstein theorem.
- [Constructions and Weyl matching](references/research/20260916_construction.tex):
  core correction, logarithmic interpolation, pointwise Ricci estimates,
  ADE/type-T extensions, multi-node calculations and their remaining interfaces.
- [Global geometry and topology](references/research/20260916_global.tex):
  same-manifold existence/nonexistence, surface bundles, graph connectors,
  smoothing, global compatibility, and possibilities beyond these models.

[Research overview — 2026-09-10](references/research/20260910.tex) covers problem
definitions and quantifiers, literature relationships and hypotheses,
mathematical deductions, key obstacles and open directions.

[Cumulative research — 2026-09-12](references/research/20260912.tex) contains the
complete user-supplied mathematical synthesis, including explicit constructions,
derived identities and estimates, proof arguments, conditional results,
obstruction mechanisms and failures of proposed arguments. These are working
research materials, not merely literature summaries. Useful entry points are:

- Chapters 1 and 5: quantitative topological and gauge-theoretic constraints,
  curvature defects, degeneration and the hypotheses needed to close arguments.
- Chapters 2--4: Einstein/Eguchi--Hanson local models, logarithmic gluing,
  boundary mean-curvature barriers and algebraic deformation problems.
- Chapter 6: fixed surface-bundle approximations, full Ricci formulas,
  correction equations and the distinction between spectral and inverse bounds.
- Chapters 7--10: Weyl identities with source terms, harmonic maps,
  adapted Einstein equations and global candidate constraints.

The two historical manuscripts remain complete and unchanged. New continuations
supplement them; they do not replace their longer proofs or discard older
constructions. Source locations, revisions and unfinished dependencies are
recorded in the TeX files. A source's historical “not available” refers to that
writer's environment, not necessarily to this shared workspace.

Start from your current mathematical question and research state. Locate the
relevant sections, reuse or recompute concrete formulas, compare constructions
and estimates with your own, and develop alternative arguments or new routes.
Distinguish a demonstrated obstruction from a missing argument; a failed
ansatz does not exclude other constructions. Preserve each result's hypotheses,
scope and proof status, and distinguish classical inputs from proposed new
results. Any document can be challenged, extended or superseded; none changes
Session goals, their quantifiers, or the available methods and tools. These
references do not assign a mandatory next Step or fixed roles to Sessions.
Search the TeX section headings and read long passages with `read_file`
`start_line` / `max_lines`; a truncated read is not the entire document.

The September 12 file is a byte-preserved copy of the user2 upload
`Sessions/S0908A03/workspace/briefing/Yau26_source_package/Yau26_synthesis.tex`;
it supplements, rather than replaces, the September 10 dossier.

Each Session develops its work in its own workspace. Incorporate reviewed
findings into this shared reference deliberately, preserving other Sessions'
contributions. Research references are kept directly as dated TeX files;
no PDF, OCR copy or separate source-manifest file is needed.
