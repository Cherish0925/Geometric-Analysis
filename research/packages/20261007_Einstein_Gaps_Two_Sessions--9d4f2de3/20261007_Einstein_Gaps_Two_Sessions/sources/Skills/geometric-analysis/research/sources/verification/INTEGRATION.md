# Consolidation and research handoff — 23 September 2026

Later delivery update: [26 September web handoff](20260926_web_handoff.md).
The figures below describe the original consolidation, not the latest export.

## What was preserved

- The complete inherited tree at `29f7d2cef30f2ccdba192acdcd02bf516d850fe8`:
  **884 tracked files**, relocated byte-for-byte to `mathematics/current/`.
- **82 explicitly scoped source roots**: original scientific Session subtrees,
  briefing uploads, exported research history, Skill versions, historical
  mathematical packages, supplied reviews/guidance, research exports and
  scientific tool implementations/examples.
- **10,191 original-path file records**, representing **2,884 distinct SHA-256
  contents**. Copies and aliases are not counted as new mathematical results.
- **14 distinct ZIP archives**, all CRC-tested; **6,214 member entries** are
  searchable without relabelling or modifying the original ZIPs.
- The full supplied thirteen-section first-line charter, separately from the
  derived English research guidance and current theorem statuses.

The source manifests record before/after size, time, inode and device as well
as source/destination hashes. Each copied source was stable across its copy
and hash check. This is a dated scientific snapshot, not a promise that live
Session files will never change afterwards.

## What was organized

The current map preserves the original three lines and their cross-connections.
The development account explains transitions in method rather than assigning
equal importance to every round. The result catalogue contains **60 result
families**, including open and retracted entries; this is not a claim of sixty
independent new theorems. Each family retains proof paths, scope and dependencies.

The root README, project instructions and first-line charter provide short
entry routes. Historical source text is not silently edited to match later
knowledge. Corrections and supersession are explicit navigation objects.

## What was checked this turn

1. SHA-256 and sizes of all 884 inherited files and all 10,191 archived records:
   passed, with no byte changes in the preserved baseline.
2. **264 local links** in the new navigation/guidance/proof layer: passed.
3. All catalogue proof paths, result IDs and declared dependency targets:
   passed.
4. **13 selected finite-check programs** after relocation: passed. The exact
   list, program hashes and outputs are in
   [the reproduction record](relocation-checks/results.json).
5. The new exact-realization note has matching Markdown, LaTeX and a six-page
   PDF. Its scaling program checks four elementary scale/budget relations;
   it does not verify the compactness or topology proof.
6. The source-discovery follow-up compared 22,360 historical text/program
   instances by hash. The excluded unmatched items are individually classified
   operational/fixture/assembly material, not silently discarded proof bodies;
   see [the follow-up](../navigation/source-discovery-addendum.md).

These checks establish artifact integrity and limited reproducibility, not
independent certification of all inherited proofs or worldwide originality.
Historical checking outputs retain their original dates; they were not all
rerun this turn.

## New mathematics, separate from archival work

The [compact-regime realization theorem](../continuation/20260923_compact_realization.md)
gives the following implication on closed oriented aspherical four-manifolds:

\[
\delta_-(g)<\varepsilon(D,v,\Lambda,q),\quad
\operatorname{diam}g\le D,\quad \operatorname{Vol}g\ge v,\quad
\|W^+\|_{L^q}\le\Lambda,\quad q>2
\quad\Longrightarrow\quad
\exists h\text{ on the same smooth }M:\ \operatorname{Ric}_h=-h.
\]

The proof uses harmonic-radius rather than curvature-maximum normalization,
the bounded-Ricci curvature-energy theorem, and the inherited obstruction to
embedding half-flat ALE cores. It avoids assuming derivatives of the Ricci
error are small. Actual positive monopole projection can supply the volume
lower bound. The notes state the classical inputs and precise limiting
regularity; this is not an unrestricted Yau26 solution or an effective
Newton-repair estimate. Its proposed novelty has not undergone exhaustive
literature comparison.

## Explicit limits of source coverage

The later three manuscripts with the titles “从统一间隙到更广Einstein判定”,
“跨尺度匹配与新闭拓扑”, and “同一光滑流形与原题闭合” were named in a supplied
review but their original files were not found in the inspected roots. The
external twelve-round audit Markdown and evidence ZIP named in quoted web
links were also not found locally. Earlier actual three-manuscript sources
and the local review are preserved. Missing originals are recorded in the
source manifest, not invented from summaries.

Private execution contexts, credentials, Session configurations/databases,
unrelated research and live control state are outside this scientific archive.
No original source, live Session, installed Skill or service was altered. All
commits and the portable history export remain local.
