# Integral Einstein Rigidity and the Geometry of Monopole Defects

The deliverable is `Integral_Einstein_Rigidity.tex`, a standalone English
LaTeX source. It requires no project-local input files, images, or bibliography
database. Compile with XeLaTeX until cross-references stabilize (three
passes on a fresh build); the fonts are TeX Gyre Pagella,
TeX Gyre Heros, DejaVu Sans Mono, Asana Math, and Latin Modern Math.

The standalone delivery copy is
[`../handoff/20261003_Einstein_Compatibility_Integrated_Manuscript.tex`](../handoff/20261003_Einstein_Compatibility_Integrated_Manuscript.tex).
It records the October 3 integration and needs no other project files.
The current reading copy is also inside
[Geometric Analysis](../skills/geometric-analysis/research/Curvature_Realizability.tex).
The October 4 packaging corrected two external-subsection links in the
Chern-boundary section; it did not change the mathematical arguments.
The earlier synthesis and assemblies remain under their original names.

The main text develops the integral calibration, finite-parameter theorem,
trace-free Ricci gap, linear coercivity, actual applications, and variational
problem. The September 29–30 increment adds the arbitrary finite-density
endpoint, its two alternative proofs and polynomial density loss, critical
variational selection, the complete ordinary-monopole budget, and the
simultaneous-field sharp-cost identity. The mathematical appendices retain
both the earlier local arguments and the new proofs of current convergence,
fifth-line prolongation, radial identities and admissible variations,
scalar-band estimates, actual forms, period geometry, realization theorems,
slow-mode analysis, closed constructions, and signed-core identities.
The density-independent endpoint and the optimal balanced coefficient are
stated separately; neither is reported as solved.

The October 3 scientific overview is preserved verbatim under
`../archive/sources/20261003-scientific-overview/`. The updated reading
synopsis is `../handoff/20261003_Einstein_Compatibility_Overview.tex`.
The English section `sections/field_interfaces_and_curvature_interactions.tex`
connects the bounded-form interface with spectral defects and recent
Weyl-energy gluing, derives the joint scalar cost with explicit norm and
topology conventions, and retains the replication fraction in the
conditional first-order gain. All fourteen overview references and their
roles are indexed in `../catalog/web_increment_20261003.json`.

[`RESEARCH_TO_MANUSCRIPT.md`](RESEARCH_TO_MANUSCRIPT.md) maps the month-long
research and web supplements to the continuous argument, distinguishes
the original three-line program from this first-line manuscript, and
states the remaining mathematical conclusions. The manuscript itself
contains the mathematical dependency diagram and reading table.

Editable new sections are under `sections/`. The assembly plan in
`../tools/build_english_manuscript.py` selects full mathematical arguments
from the preserved manuscripts, resolves notation and internal references,
and omits program logs and superseded exposition. `source_selection.json`
locates the original arguments; it is not needed to read or compile the paper.

From the project root:

```sh
python3 tools/build_english_manuscript.py
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error paper/Integral_Einstein_Rigidity.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error paper/Integral_Einstein_Rigidity.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error paper/Integral_Einstein_Rigidity.tex
```

The source archive and earlier versions are not overwritten by this build.
The complete incoming package, including both web sessions' originals and
mathematical checks, is retained in
`../archive/sources/20261001-web-increment/`. The source-to-section index
`../catalog/web_increment_20261001.json` distinguishes complete proof
imports, translated supplements, overlapping arguments, and historical
or computational material. The latter remain available without becoming
repeated sections of the mathematical manuscript.
