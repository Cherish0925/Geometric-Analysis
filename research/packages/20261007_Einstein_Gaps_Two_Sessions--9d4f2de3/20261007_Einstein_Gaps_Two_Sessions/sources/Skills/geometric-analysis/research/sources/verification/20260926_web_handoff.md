# 26 September: current scientific handoff to an external reader

This update packages the existing research; it does not add a mathematical
theorem or independently certify the inherited proofs. No upload, publication,
live Session change, service change or installed Skill mutation was performed.

## Preserved sources and navigation

Five exact selected message bodies were recovered from this conversation,
including the user's two latest quoted web analyses and the preceding
assistant explanations. Selection is by message type, role and exact prefix,
with exactly one match required per requested message. Raw execution contexts
are not exported. The source receipt records hashes, timestamps and message
locations: [selected messages](../guidance/source/20260926_selected_messages.json).

The new [web entry](../WEB_REVIEW_START_HERE.md),
[proof map](../handoff/PROOF_AND_EVIDENCE_MAP.md),
[discussion status](../handoff/LATEST_DISCUSSION_STATUS.md) and
[coverage limits](../handoff/COVERAGE_AND_LIMITS.md) connect the current
proofs, computation records, original guidance and historical sources.
The original guidance directory's seven files and the historical export
comparisons are recorded in the coverage page. The old `bc8ced8` package
already contains I27, but lacks I28–I37; it is not the current handoff.

## Bounded checks performed before freezing

- `python3 tools/library.py verify`: 884 baseline files, 10,191 archived
  source records, 554 editorial links; no failures.
- `git diff --check`: passed.
- No changes in `mathematics/current/`, `archive/sources/` or `continuation/`.
  The mathematical result catalogue is unchanged.
- `python3 tools/test_web_handoff.py`: seven test methods passed, with eight
  corruption subcases in the main rejection test. Coverage includes positive
  replay, wrong bytes/hash, missing/extra/duplicate/unsafe members, omitted
  required proof, empty complete package, coordinated proof/manifest deletion,
  disagreement with the independent inventory, verbatim code preservation,
  refusal to replace an existing delivery, and a changing source tree.
- A separate read-only review checked the source map and export code. It found
  and prompted correction of the I27 historical boundary, code corruption by
  Markdown link rewriting, self-declared coverage and premature final output.
  The follow-up review confirmed those changes and the passing tests.
- The reviewer checked all 82 selected Markdown/TeX bodies: each is present
  verbatim in the generated reading view. Selection covers 55 result families
  with recursive cross-line dependencies, not 55 independently new theorems.

## Export and independent scope

`tools/web_handoff.py build --output-directory NEW_DIRECTORY` requires a clean
committed tree. It freezes one revision into two profiles: all tracked files,
or all tracked files except `archive/sources/`. Every omitted historical path
is listed. Both include the same original current mathematics and continuation.

The builder checks ZIP content against an independently computed source
inventory and re-derives required proof coverage from the embedded catalogue.
Offline `verify` without that independent inventory checks internal consistency
only; it does not authenticate provenance or a Git revision. Neither check
certifies mathematical correctness or priority.

Scientific reading-view bodies are not rewritten. Their local links still
belong to the marked original files. A standalone large text is a fallback,
not a promise that any particular web interface can ingest its entire content.

Both ZIPs, receipts and delivery metadata are built under a hidden staging
directory. The intended output directory is published only after source-state
checks pass. A failed build remains visibly incomplete; it must not be sent
as a final package. The final, same-revision archive hashes, counts and actual
build outcome are recorded outside the source snapshot in `DELIVERY.json`,
`SOURCE_INVENTORY.json` and the two archive receipts.

Five named external originals remain unlocated in the inspected roots. They
are listed explicitly in the coverage page; quotations and differently titled
earlier manuscripts are not relabelled as those originals. The package is a
complete export of its declared local source set, not a claim that every
historical conversation or outside paper has been recovered.
