# Tool-source and historical-hash coverage addendum

Date: 23 September 2026. This supplements, rather than replaces,
[`source-discovery.md`](source-discovery.md) and its 65-root allowlist.
The additional allowlist and full hash-disposition evidence are in
[`catalog/discovery-addendum.json`](../catalog/discovery-addendum.json).

## Additional sources

The addendum names seventeen bounded roots:

- Ten mathematical tool releases, `qiushi-yau26-1f-20260909.1` through `.7`
  and `qiushi-yau26-1f-20260910.1` through `.3`. Only `libexec/yau26`,
  `share/examples`, `share/scripts` and `user-assets/skills/qiushi-yau26`
  are included. These retain symbolic curvature/linearization/checker source,
  JSON examples, and the Sage/PDE smoke scripts. Native binaries, launchers,
  virtual environments and release configuration are not copied.
- Three immutable research-release Skill origins corresponding to the already
  identified platform Skill copies. They are provenance aliases, not new
  mathematical versions.
- Additional historical standalone/paper-package variants and exact
  computation programs from `qiushi-yau26-flat-20260916-6fHNZy`.
- The Fable isolated-check runner, the all-user finite-math-check runner, and
  the package-only mathematical reconstruction assessment.

The flat-package additions matter: its `paper-package/references/computations.md`
and `experiments.md` are older distinct versions, and
`interface_algebra.py`, `step59_induction_ledger_verify.py`, and
`step67_terminal_recalibration_verify.py` preserve executable extraction variants.
They belong in the historical/reproduction layer, not in place of corrected
current text.

All sources remain unmodified. Importing these scripts must not execute them.
Their old hard-coded paths are historical facts; new execution needs a scoped
working copy and the recorded dependencies.

## Actual coverage comparison

The comparison scanned the historical Yau26-named build roots for Markdown,
TeX, Python, Sage, Lean, Wolfram, notebooks and C/C++ sources, excluding caches,
private `.qiushi_runtime` material and the current-turn library/inventory,
three-line-synthesis and compact-realization worktrees.

| Quantity | Observed count |
| --- | ---: |
| Historical text/program file instances | 22,360 |
| Distinct content hashes among those instances | 631 |
| Distinct historical hashes covered by combined source allowlists | 569 |
| Remaining hashes, all explicitly dispositioned | 62 |
| Source paths selected by the combined allowlists | 10,191 |
| Distinct selected content hashes across all source categories | 2,884 |

The seventeen additions contribute 693 selected paths and 46 previously
unselected content hashes. The source-path count includes copies and aliases;
it is not a count of scientific results.

The remaining 62 hashes are listed individually in the JSON, including every
discovered path alias and the reason for exclusion. They are platform/browser
test fixtures; generic or unrelated Skill integration; Session/model/privacy
probes; publication/installation/maintenance scripts and draft messages; or old
archive-assembly implementations whose scientific inputs and outputs are
retained separately. They are not silently labelled duplicates.

This is a bounded source-coverage result: no additional unmatched proof body or
mathematical checking program was identified in this scan after the additions.
It is not a theorem audit, a claim that every past chat was recovered, or a
claim that all published sources needed by the proofs are locally archived.
The missing-original ledger from the first discovery remains applicable.

## Importer detail

A pattern ending in `/**` means all descendant regular files. In Python's
`pathlib`, `Path.glob('package/**')` alone enumerates directories, so normalize
such a terminal pattern to `package/**/*` or use an equivalent recursive-file
matcher. This distinction was included in the coverage calculation; without
it, a directory may appear selected while its mathematical contents are missed.

Apply both the original global exclusions and the addendum's exclusions for
`.qiushi_runtime` and duplicate `.qiushi_document_assets`. Hash/stat checks at
copy time, rather than these discovery counts, determine the final snapshot.
