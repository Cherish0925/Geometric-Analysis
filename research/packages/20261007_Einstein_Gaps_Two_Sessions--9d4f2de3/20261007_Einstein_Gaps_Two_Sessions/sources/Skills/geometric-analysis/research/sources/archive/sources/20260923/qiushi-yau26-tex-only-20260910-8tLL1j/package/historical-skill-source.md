---
name: qiushi-yau26
description: >-
  Geometry tools via run_shell: qiushi-yau26 <command>. doctor --json checks
  backends (--full runs demos/proof); examples list; examples show <name> emits
  JSON. curvature <metric.json> [--ricci-only]; linearize <equations-or-variation.json>;
  search <equations.json> finds numeric roots. ricci|pinching <metric.json>
  --lower <rational> --upper <rational> checks Ricci|curvature-operator bounds;
  --non-strict includes equality. certify <check.json>; verify <certificate.json>.
  Box checks support --max-cells N --checkpoint <new.json> --resume <old.json>.
  lean <Proof.lean> --declaration <theorem> checks axioms.
  env <numeric|sage|pde|ode> <program> <args> runs custom programs;
  demo <sage|ode|pde> runs examples. Save JSON with --output <new.json>.
  Paths use cwd; run_shell/bg_task needs output parents in write_paths kind=directory.
  Local certificates are not global proofs; methods remain unrestricted.
  Research dossier, definitions and literature: references/research/20260910.tex.
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

## Research references

[Yau 26 research dossier — 2026-09-10](references/research/20260910.tex) is the
editable investigation: problem definitions, mathematical arguments, literature
relationships, open directions and a framework for sustained research. Read it
in full when establishing the research; return to relevant sections as needed.
Its claims and routes can be challenged, extended or replaced. It does not
restrict methods, tools or Session goals.

Each Session develops its work in its own workspace. Incorporate reviewed
findings into this shared reference deliberately, preserving other Sessions'
contributions. Source details and unresolved literature checks are in the TeX;
no PDF, separate source manifest or research index is needed.
