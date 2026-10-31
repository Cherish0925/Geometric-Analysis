# Verification and reproduction — 23 September 2026

The machine-readable record is [line1_verification.json](line1_verification.json).

## What was run

- The new scalar-band checker: 15 exact symbolic identities/calibrations.
- The separate energy checker: six algebra groups, including four rejected
  false variants.
- The inherited closure checker: six check groups, including finite
  threshold arithmetic.
- Three English documents converted to standalone LaTeX and compiled twice
  with XeLaTeX. Final logs have no missing glyph, overfull box, undefined
  reference, or LaTeX error. Selected first, budget, and literature-table
  pages were visually inspected, not every page.
- All 22 Markdown local links in the three current documents resolve.
  Seven source files agree byte-for-byte with the upload directory.

The analysis and its limits were also reviewed independently: the weighted
defect identities, smoothing without weight-derivative bounds, polynomial
Weyl model, square-root full-gradient estimate, second-order curvature
budget, and normalized allowed-root form were checked in the written proof.
The Kähler formulas were checked separately. The Arezzo--Pacard existence
input was checked at Theorem 1.1 of the author-hosted primary text.

The second-order argument invokes the inherited bounded-section Hessian
lemma from Rounds 4/21. This increment does not independently replace that
lemma's proof or certify the complete earlier integral-calibration
manuscript. Finite symbolic checks verify their stated algebra, not global
PDE existence or worldwide novelty.

## Commands

Python requires SymPy; the remaining verification code uses the standard
library. Typesetting uses Pandoc, XeLaTeX, the Asana Math font and ordinary
TeX Live packages. These dependencies were already present; no shared
environment was changed.

Run from this directory:

    python check_line1_remainders.py
    python line1_scalar_band_check.py
    python check_lebrun_closure.py
    python verify_line1_increment.py

The source-manifest builder additionally checks against the original local
upload directory; it is not needed to verify the archived source hashes
after moving this package.

For the synthesis:

    pandoc line1_unified_v2.md --from=markdown+tex_math_single_backslash --standalone --number-sections --to=latex --output=line1_unified_v2.tex
    xelatex -interaction=batchmode -halt-on-error line1_unified_v2.tex
    xelatex -interaction=batchmode -halt-on-error line1_unified_v2.tex

For either companion proof, use its Markdown basename and add
--metadata-file=line1_paper.yaml. The checked generated LaTeX files are
included and can be compiled directly. Recompilation can change PDF
metadata and therefore its byte hash without changing the mathematics.
The final compilation logs are retained in line1_build_logs; the
verification script uses them when no new local compilation log exists.

## Preservation and scope

The research worktree starts from local commit 046166b. Original proof
files, uploaded files, and the inherited Skill snapshot are unchanged.
The two identically worded uploaded discussion files are both retained
and explicitly identified as duplicates in the manifest.
Their original trailing blank lines are also preserved; the two archival
whitespace warnings are not edits to the research sources.

The current work proves a limited actual-form supply result and correct
functional comparisons. It does not infer small LeBrun defect from Ricci
pinching alone, turn an allowed spectrum into an obstruction, or construct
an exact Einstein metric. Those are distinct mathematical tasks.
