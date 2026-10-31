# Verification of the first-line energy and conformal increment

Baseline: local research commit 0263799. All work was performed in isolated
research worktrees. No live Skill installation, Session, model configuration,
service, original upload, or prior paper was changed.

## Mathematical review

- The energy-selection proof was independently rederived, and the complete
  main manuscript was reviewed for its scalar-loss constants, variational
  quantifiers, conformal signs, and Einstein energy bound.
- Review distinguished convergence to the limiting lower value from equality
  of a liminf. The manuscript now explicitly uses convergence when asserting
  equivalence to vanishing scalar variance.
- The conformal-neck construction was read from its actual collar through
  the period calculation, both energy limits, the scalar variance, and the
  growing-window variant. Its Ricci tensor was additionally recomputed from
  coordinate Christoffels, not merely checked against a trace formula.
- The converse paper keeps the original-metric and conformally changed
  conclusions separate. The original-metric form budget inherits the
  bounded-section Hessian estimate; that PDE lemma was not independently
  reproved in this increment.
- Round17 already contained the ordinary monopole scalar-loss identity.
  Round14 already used Yamabe normalization for one shear family. Neither
  classical input is advertised here as a new method.

## Primary-source checks

LeBrun's [curvature-functional preprint](https://arxiv.org/pdf/math/0003068)
was checked for the scalar–Weyl inequality, polarized selection, exact
Ricci-energy identity and all-metrics infimum. Its
[later account](https://arxiv.org/pdf/math/0611450), Proposition 3.2, supplies
the scalar inequality and its negative cscK equality case.
The collar model is the classical collar lemma, recalled in
[Rupflin–Topping, Appendix A](https://arxiv.org/pdf/1605.06691).
The product's actual canonical monopole input uses classical Kähler
nonvanishing, as recorded in
[LeBrun's earlier paper](https://arxiv.org/pdf/dg-ga/9412006).
These checks establish the stated inputs, not an exhaustive novelty search.

## Reproduction

Run the companion verifier with a Python environment containing SymPy:

    python verify_line1_bridge.py

It runs four current programs and three inherited regression programs.
The current algebra programs deliberately overlap on central identities;
their check totals must not be interpreted as numbers of independent
theorems. The coordinate program checks all ten symmetric Ricci components
and the scalar trace of the local conformal neck.

The same verifier checks local references, the three compiled papers, and
the hashes of all seven preserved uploaded source files. Execution output,
document hashes and final compilation logs are in
[the evidence directory](line1_bridge_evidence/results.json).
The three PDFs were compiled with XeLaTeX; the recorded logs are checked
for overfull boxes, missing glyphs, undefined references and TeX errors.
Minor font-size substitution warnings are not mathematical errors.

The proof review and finite computations have distinct scopes. None of
these checks proves global Einstein existence or converts an integrated
residual into pointwise Ricci pinching.
