# 26 September: eight direct-reading volumes

The user clarified that the web recipient needs mathematical text, not a
303 MB research archive or calculation scripts. This update changes the
default handoff accordingly. It does not remove any original files or change
mathematical conclusions.

## Selection

The reproducible selection is `handoff/reading_volumes.json`. Eight Markdown
volumes retain selected original Markdown and TeX bodies, together with
source paths and hashes. Matching PDF/TeX/Markdown format copies are not all
included. Historical computation compilations, executable scripts, data,
LaTeX auxiliary outputs and source-archive copies are not included.

I01–I37 each have at least one catalogue-registered full manuscript in the
selection. Superseded/provenance manuscripts omitted from first reading have
explicit reasons. The selection also includes actual proof dependencies not
listed among those catalogue paths: the monopole input, full product/twisted
operators, nonlinear construction and closed-shear topology papers.

Three clearly labelled TeX excerpts retain the E_D example interface without
including two large omnibus manuscripts. The source ranges are 3283–3476
and 4038–4332 of `20260912.tex`, and 747–980 of `20260916_global.tex`.
The last is the current section labelled `sec:bundle-global` (section eight),
not the old numerical section-seven reference.

The first-reading packet is a curated text edition, not a statement that all
historical proofs, external articles or executable reproduction assets are
contained in eight files. All original materials remain on the server.

## Checks

- `python3 tools/test_reading_volumes.py`: six tests passed. Tests cover
  verbatim scientific bodies and exact line excerpts, text-only selection,
  all first-line catalogue entries, and rejection of a missing main proof,
  repeated source and invalid excerpt range.
- Independent read-only selection review confirmed preservation of the
  distinct scalar-band / near-Einstein ranges, finite-cover / twisted inputs,
  and full-matrix / positive-inertia conclusions. It checked the three E_D
  ranges and the non-catalogue dependencies above.
- Preflight produced 79 source segments in eight files, approximately
  1.23 MB total. This counts source segments, not original theorems.
  They comprise 76 complete documents and three labelled excerpts from two
  other source files. There are 78 distinct original paths. The separate
  all-three-lines working trees contain 424 Markdown/TeX paths (353/71),
  including repeated formats and historical compilations; that is not a
  first-line theorem or manuscript count.
- Each scientific body is checked by byte offset against its source bytes;
  no link-rewriting regex is applied to mathematical text or code snippets.
- `git diff --check`: passed. No inherited mathematics, historical source
  tree, theorem catalogue, live Session or installed Skill was modified.

The actual frozen output sizes, source hashes, excerpt locations and commit
are in `READING_MANIFEST.json` beside the eight Markdown files. The small ZIP
there is for convenient download and extraction, not a requirement that the
web recipient process archives. The builder requires a clean committed tree,
rejects an existing destination and publishes only after source-state and
byte-identity checks. No files are uploaded automatically.
