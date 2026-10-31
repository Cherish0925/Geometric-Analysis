# Recent line-I review packet: preservation and scope record

27 September 2026. Research snapshot `844e62f`; seven commits after `168bea5`.
Packaging branch: `local/yau26-review-packet-20260927`.
This work assembles existing research for discussion. It proves no new theorem
and does not certify all PDE arguments or priority claims.

## Selection and editorial review

The six new continuation manuscripts are included in full, with ten complete
technical prerequisites and six complete original verification records. Two
clean-context GPT-6 Astra/max agents independently checked the recent-result
scope and selected proof dependencies. The root reconciled the guide with their
findings, including the parameter range, local integral exponent, outward core
collar, and scalar normalization for the flow time.

The project research Skill was read to retain actual-class, auxiliary-weight,
chirality, and norm conventions. No installed Skill, immutable baseline,
historical proof, runtime, service, or external platform was changed.

The guide explicitly records supersession: I40 closes linear order; I41 closes
the previously open scalar-variance-free transfer; I45 closes a conditional
bounded-Ricci endpoint case. The balanced-family leading coefficient, general
weak integral endpoint, and complete marked-core/actual-field bridge remain open.
The handle-only sharp infimum, balanced-family coefficient, and h=0 Weyl-payment
example are not merged.

## Catalogue correction

The frozen snapshot's `catalog/results.json` had a missing comma after the I48
statement. Inspection of the previous edit history showed this was introduced
after the prior catalogue test. This branch adds that comma only; no mathematical
text, status, or dependency was changed. The current library verification is
rerun after all packaging edits rather than inheriting the earlier receipt.

## Full-text and rendering checks

- 22 complete sources agree byte-for-byte with `git show 844e62f:path`.
- Every changed `continuation/20260927_*.md` since `168bea5` is included.
- Every source has its original path, SHA-256, full-selection flag, byte offset
  and length in the build receipt. Original formulas and local references remain.
- Seven MD files contain 554,030 bytes; matching TeX files contain 638,406 bytes.
- All seven TeX files compiled twice with XeLaTeX and shell escape disabled.
  The temporary PDFs total 171 pages; they are not included in the ZIP.
- 2,464 parsed math nodes were checked against generated TeX, allowing only
  whitespace and recorded display-layout transformations.
- Original `split` environments become `aligned`, and equation tags move outside
  the alignment environment. This repairs multi-column/tag placement for TeX;
  mathematical tokens and all original Markdown bytes remain unchanged.
- Two raw TeX fragments outside math delimiters are treated as literal prose.
  Superscript/subscript shorthand in plain ASCII prose is not silently parsed
  as mathematical markup. Defined math delimiters retain their contents.
- Compilation has no missing glyphs or errors. Overfull lines and one legacy
  `\over` warning remain explicitly recorded; this is not publication-layout QA.

## Executed checks

`python3 tools/test_recent_review.py`: eight tests passed. They check layout
conversion, unaffected formulas, math-node selection, rejection of a changed
source, refusal to overwrite an existing directory, every frozen source, and
the byte-identified historical catalogue comma repair. Catalogue metadata is
read from the frozen research commit so future research updates cannot alter it.

The archive was reopened independently after creation. CRC, fourteen member
names, extensions, bytes and hashes all matched. Each embedded proof slice was
again compared to the frozen Git object, not merely to a generated summary.
No executable, PDF, runtime record, database, or archive-within-archive is present.
A second full build in a fresh temporary directory produced the identical ZIP
SHA-256 after the frozen-catalogue reader was installed.

The ZIP is 432,761 bytes, SHA-256
`b3756d2be6a31f2d7ec2023da73fe5f4229617adb10ce3d666a341b2352be03b`.
Exact data: [build receipt](20260927_recent_review_build.json).
User entry: [recent review](../handoff/RECENT_REVIEW.md).

The post-edit library verification passed: 884 inherited files, 10,191 source
records, 659 navigation links, no failures. These are integrity counts, not
counts of mathematical contributions.

The tests establish preservation and deliverability, not mathematical
correctness. Previous finite-check records are included as historical evidence;
their programs were not re-run merely to create this reading package. External
review, theorem-level novelty comparison and further research remain separate.

All artifacts were kept on this server. No upload, publication, push, account
access, or transmission to a web GPT service was performed.
