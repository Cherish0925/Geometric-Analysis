# Source library

This portable library contains **1,178 distinct source
payloads**, representing **4,610 source paths**, with
22.47 MiB of source text and navigation data.
These are file counts, not theorem counts. The current reading order is in
[the research map](research-map.md), and the current conclusions are in
[results and questions](results-and-questions.md).

## Reading and retrieval

The [continuous English manuscript](../research/Curvature_Realizability.tex)
is self-contained LaTeX, with its mathematical appendices and bibliography.
It can be compiled with XeLaTeX; the editable current sections are in
`research/paper/sections/`. The original Chinese and English texts remain
in their original languages. The single-file manuscript needs no source
archive or external image to compile.

Search [source-index.tsv](source-index.tsv) for an old filename, then open
the `skill_file` it names, relative to the Skill root. `project_source`
retains the old project-relative alias, not a required server path. Equal
texts have one physical copy. Distinct historical versions are retained.
Paths below are relative to this index and remain valid after moving the
entire Skill folder.

For example, from the Skill root:

```sh
rg -n 'line1_period_inertia|20260924_bilateral|web_n1_complete' references/source-index.tsv
rg -n 'thm:finite-density-endpoint|thm:vg-first-order-reduction' research/Curvature_Realizability.tex
rg -n 'torsion|monodromy' research/sources/continuation
```

Historical relative links can use an older layout. Resolve their filenames
through the alias index; use the current manuscript for continuous proof
references. Historical `SKILL.md` texts are named
`historical-skill-source.md` here and are sources, not active instructions.
Current guides take precedence over dated task lists and superseded claims.

## Scope of the text package

Included: current manuscript and editable sections; all selected inherited
and continuation mathematical texts; distinct historical proof versions;
the web research and source-version texts; the latest scientific overview;
research guidance, mathematical corrections and source-to-proof maps. The
small READ_FIRST text existing only inside a nested web ZIP is extracted
as its own source. No original text is rewritten by this packaging step.

Raw session transcripts, large code-and-output record books, executable
programs, numerical binary data, build logs, repeated PDFs and ZIPs are
not part of this reading Skill. They remain in the original project; this
is a mathematical text library, not the complete computational-runtime
archive. The preserved independent derivations and mathematical reports
are included below.

The source texts include earlier unsuccessful or conditional arguments.
Their preservation keeps the research history usable; it does not change
their mathematical status. The current map identifies the successor
proofs and the questions that remain open.

## Text groups

| Group | Distinct payloads | Source bytes |
| --- | ---: | ---: |
| current-manuscript | 26 | 3,091,346 |
| continuations | 84 | 1,962,144 |
| inherited-research | 263 | 4,701,491 |
| research-navigation | 60 | 1,094,537 |
| web-research | 77 | 968,297 |
| scientific-overview | 1 | 26,123 |
| historical-sources | 667 | 11,716,944 |

The [distinct-text catalogue](source-catalogue.md) gives a clickable entry for every bundled source. Search it by filename or subject; the alias index resolves repeated historical paths. Neither index needs to be read in full to continue a mathematical argument.
