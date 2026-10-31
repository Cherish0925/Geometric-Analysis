# Integral rigidity: functional compatibility and actual form supply

23 September 2026. Research continuation from commit `fa5efed`.

## Results

1. [Parameterized functional theorem](line1_functional_pencil.md).
   For an actual conformally solvable Spin\(^c\) class, the truncated
   monopole construction now supplies the entire calibration
   \(t=1/\beta\), not only \(t=1/8\). On each finite interval
   \(2\le\beta\le L\),
   \[
   (1+b_a)\left(r+\mathfrak D_\beta/V\right)
   \ge c_L(\beta-2)^2.
   \]
   Here \(r=\fint|\operatorname{Ric}+g|^2\),
   \(b_a=(-a^2)_+/V\), and
   \(\mathfrak D_\beta=(\beta+1)\int(s^2+6\beta|W^+|^2)/\beta
   -72\pi^2(a^+)^2\). If \(a^2\ge2\chi+3\tau\), the square-cost
   factor can be removed after changing the constant. The theorem has
   no scalar band or geometric compactness assumption.

2. [Allowed-branch application](line1_composed_application.md).
   At \(\beta=2\), write \(\kappa=r+144\pi^2D_{\rm LB}/V\).
   The actual bounded smooth form satisfies, with arbitrarily small
   allowance,
   \[
   \fint|\omega+2\pi H(a^+)|^2\le49\kappa+\eta,
   \qquad
   \fint|\nabla\omega|^2\le13\kappa+4\sqrt{2\kappa}+\eta.
   \]
   Both estimates hold without a scalar band or negative-square budget.
   The separate second-order bound retains the square cost. This is
   actual harmonic-class alignment and low rough-Laplacian spectral
   concentration, not a new Einstein obstruction or global Kähler
   realization. It strictly removes a hypothesis of the earlier
   scalar-band supply theorem.

3. [Standalone integral-rigidity paper](line1_integral_rigidity_paper.md).
   The inherited calibration proof, polarization/chamber application,
   all-sign passage and Ricci-flat exclusion are assembled in one
   manuscript. This stabilizes the existing main result; it is not
   counted as a new theorem merely because it is now independently
   readable.

The two new manuscripts also have generated LaTeX and PDF versions, as
does the standalone paper. The original arguments and sources remain in
this snapshot. Installed v08/v09 Skills, Sessions and services were not
modified.

## Mathematical relation to the earlier work

The key distinction is between a forbidden calibration and an allowed
one. At \(\beta=8\), Chern–Weil identifies the deficit with the old
topological boundary \(T/p=2/3\). At \(\beta=2\), the target is the
realizable negative Kähler–Einstein spectrum. The new proof supplies the
parameter from a raw curvature functional and controls its joint budget;
it does not assume a suitable Weyl eigenform exists.

Classical Einstein equality forcing KE is already LeBrun's Corollary
2.5. The present functional theorem concerns quantitative non-saturation
under integral Ricci error. Its proof and the exact endpoint example
are in the manuscript. This is not a comprehensive literature-priority
claim, and no new smooth topological family is asserted.

For the original pointwise negative input, \(r\le4\delta_-^2\).
Consequently the functional inequality directly constrains such input.
Converting another parameter into a new topological obstruction still
requires independent control of its functional deficit. The present
results do not determine all Einstein metrics on the earlier shear
manifolds and do not solve a complete Yau26 sign branch.

## Reproduction

Run `python verify_line1_composition.py --output NEW_DIRECTORY` with
SymPy installed. It reruns the new finite identities and the relevant
inherited algebra, checks local manuscript links, and writes exact
commands, return codes and output. The script refuses an existing output
directory. Mathematical reviews are in
`line1_functional_pencil_review.md`; finite checks do not certify the
gauge existence or global PDE arguments.

Sources are preserved in `line1_sources_20260923/`, the earlier research
notes, and `skill/`. The user's research guidance motivated completing
the raw-input application; it is not used as a mathematical premise.
