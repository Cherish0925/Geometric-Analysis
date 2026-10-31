---
name: qiushi-yau26
description: >-
  Geometry, Einstein-metric and Yau 26 research software, available directly in run_shell.
  qiushi-yau26 doctor --json checks this environment; qiushi-yau26 examples list lists
  complete inputs; qiushi-yau26 examples show <name> --output <input.json> creates one.
  Use qiushi-yau26 curvature <metric.json>, linearize <equations.json>, search
  <equations.json>, certify <check.json>, or verify <certificate.json>; each accepts
  --output <new.json>. Pinching: qiushi-yau26 pinching <metric.json> --lower <rational>
  --upper <rational>. Lean: qiushi-yau26 lean <Proof.lean> --declaration <theorem>.
  Run custom programs with qiushi-yau26 env <numeric|sage|pde|ode> <program> <args>.
  qiushi-yau26 demo <sage|ode|pde> runs known-answer examples. Paths are cwd-relative;
  authorize output parent directories with write_paths kind=directory in run_shell/bg_task.
  Symbolic/local, numerical and rigorous results are distinct. Local certificates
  do not prove global theorems. No research route is prescribed.
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

`curvature` returns coordinate expressions and conditions. `pinching` can
certify bounds over a declared closed coordinate box using sufficient
curvature-operator inequalities. Neither assembles a closed manifold, proves
global coverage, or rules out metrics outside a chosen family.

`certify` supports positivity, symmetric generalized matrix bounds and root
boxes. `verify` recomputes from the original specification with the pinned
checker. Keep the certificate and its release identity. `inconclusive` is not
a negative theorem. Numerical searches and discrete PDE spectra remain
numerical results. `lean` checks the specified theorem's transitive axioms;
statement correspondence and the trusted Lean environment remain separate.

The original Yau 26 statement must be checked against its primary source before
claiming a solution; the package name does not supply its missing hypotheses.

[Formats, mathematical conventions and complete examples](references/formats.md)
provide further detail and can be read progressively as needed.
