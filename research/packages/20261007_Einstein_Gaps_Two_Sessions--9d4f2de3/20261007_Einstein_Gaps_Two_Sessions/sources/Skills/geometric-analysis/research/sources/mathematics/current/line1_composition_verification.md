# Verification record

23 September 2026. Scope: the three manuscripts listed in
`START_LINE1_COMPOSITION_20260923.md`.

## Reproduction

`verify_line1_composition.py` ran nine check programs successfully.
The three new programs contain 22, 23 and 19 exact checks, respectively;
the other six exercise the inherited algebra used by the proofs.
Commands, return codes, output and manuscript hashes are preserved in
`line1_composition_evidence/`. Five local manuscript links were checked.
These are finite algebra and artifact checks, not automated verification
of the global PDE or gauge-theoretic existence arguments.

The functional, actual-form and integral-rigidity manuscripts compiled
with XeLaTeX to 8, 5 and 21 pages. Their final logs contain no undefined
references, missing-character reports, overfull boxes or LaTeX errors.
The long manuscript retains harmless font-size substitution and underfull
box warnings. Compiler logs are retained alongside the check outputs.

## Independent mathematical reading

The separate `line1_direction_review` agent read the functional proof
and then its added harmonic-alignment section; its findings and separate
symbolic checks are recorded in `line1_functional_pencil_review.md`.

For the standalone integral-rigidity paper, `r21_analytic` independently
read the weak Bianchi self-testing argument in Section 6, including its
signs, normalization and testing regularity. It found no substantive
issue. `line1_direction_review` read the abstract, Section 1 and Sections
7–11 against the polarization closure and chamber sources. It found no
mathematical discrepancy in those sections, conditional on the analytic
core and cited classical gauge inputs. The reported notation and layout
errors were corrected before the final compilation. The main agent also
read the analytic proof and the remaining manuscript sections.

These are internal, bounded reviews, not external peer review or a proof
of publication priority. The new functional statement continues to use
the inherited bounded-form compatibility and bundle Hessian arguments;
their sources remain in the package. The standalone main paper includes
the analytic derivation instead of citing a round number as its proof.

## Scope of the results

The new functional theorem gives quantitative integral non-saturation
under its stated actual-class assumptions. The endpoint application
strictly removes the earlier pointwise scalar-band assumption, with an
actual conformal family witnessing the larger domain. Neither result
establishes a new smooth topological family with no Einstein metric.
The endpoint conformal example concerns integral, not pointwise, Ricci
error. No complete Yau26 sign branch is claimed.

The existing Skill conventions and proof lineage were retained; this
research package does not overwrite the installed v08/v09 Skills or any
running Session.
