# Two-chirality application: verification and provenance

23 September 2026. Worktree:
`/data/qiushi/runtime/build/yau26-energy-realization-n5cifh`.
Parent research baseline: `6065e33`. This work did not change any installed
Skill, research Session, runtime, service, or historical proof.

## Mathematical dependency

The new theorem uses the existing `line1_energy_envelope_gap.md`, which
in turn uses `line1_functional_pencil.md`. Those analytical dependencies
are not independently recertified by this algebraic transfer.

The new proof supplies the previously missing upper bound on *every*
Einstein candidate, from the opposite-chirality Chern--Weil formula.
No opposite-orientation monopole class is assumed. Combined with the
parameter-dependent lower envelope this gives an all-metric relative
Einstein-defect gap controlled by both Euler/signature combinations.

The floor construction produces actual smooth manifolds using compact
complex-hyperbolic covers, exceptional connected sums, and handle
additions. Gauge nonvanishing, loop insertions, class signs, and positive
weights use the already written polarized closure, not arithmetic alone.
Ricci-flatness is separately excluded by the positive scalar monopole
budget. The pointwise corollary covers both normalized target signs.

## Executed checks

`/data/qiushi/.venv/bin/python check_line1_two_chirality_topology.py`
passed 30 grouped exact algebra checks. Three deliberately incorrect
formulas were rejected: the opposite-orientation handle sign, the
trace-free-Ricci coefficient, and the floor-offset sign.

`pandoc` generated the standalone TeX source; `xelatex` ran twice without
errors or undefined references. `pdfinfo` reports five pages. The log
contains only the inherited `mathrsfs` small-font substitution warning;
there are no overfull boxes. `git diff --check` passed.

## Primary-source checks

The original mathematical statements consulted were:

- LeBrun, arXiv:math/0003068, Proposition 3.2 and Theorem 3.3:
  polarized classes on the actual mixed connected sums, with loop
  insertions; Corollary 2.5: classical exact equality forces KE.
- Kotschick, arXiv:math/0410215, Corollary 3, equation (15):
  the displayed degree-to-complex-hyperbolic entropy condition.
- Nica, arXiv:1306.2385: an account of Mal'cev's theorem for the
  residual-finiteness input; the unbounded-index deduction is given in
  the new proof itself.

The examples pass the explicitly compared classical inequalities and
the prior package's stated one-third stability constant. This is a
precise coverage comparison, not an assertion that no earlier paper
could imply nonexistence by another method. No Yau26 sign-branch is
settled: these examples obstruct the required input as well as exact
Einstein output.
