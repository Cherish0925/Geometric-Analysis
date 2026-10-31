# Round 17: proof checks and reproduction

The research was performed in an isolated local worktree based on
Round-16 commit 7f1ee60. The inherited proofs, installed Skills,
live research Sessions and services were not changed.

## Reproduction

The three new programs use Python and SymPy only:

~~~bash
python round17_integral_check.py
python round17_product_operator_check.py
python round17_positive_check.py
~~~

They do not import earlier project checking functions. The execution
interpreter on this host is
/data/qiushi/qiushi_engine_v09/.venv/bin/python.
No dependency was installed or upgraded.

All three programs were rerun by the lead investigator on the final
files and exited with status zero:

| Program | Printed check groups | Result |
| --- | --- | --- |
| Integral calibration | 10 | Pass |
| Product operator | 10 | Pass |
| Positive branch | 9 | Pass |

The first two use exact symbolic differentiation and algebra. The
positive program uses exact rational arithmetic for characteristic
numbers and energy budgets; its square-root threshold substitution is
a floating-point check, while the threshold itself is proved
algebraically in the note. Three Python files passed syntax parsing.
All five Markdown files had balanced displayed and inline math
delimiters, and all fifteen local links resolved.

The checks concern finite symbolic identities. The monopole existence
input, global Hodge decompositions, min–max argument, perturbative
operator estimates and classical geometric theorems are justified in
the proof notes, not by program exit status.

## Analytic checks performed by the lead investigator

For the integral estimate, the cap is the identity near a zero of the
spinor, so the resulting two-form is smooth. Its derivative is bounded
by the spinor energy with constant proportional to \(\kappa\), without
a pointwise bound on the untruncated spinor. The quartic term of the
capped form is controlled by its bounded amplitude and the two
quadratic errors; no fourth moment of the original \(\rho\) is
assumed. The Hodge cross term, topological remainder and conversion
from the two half-Weyl operators to the full curvature operator were
recomputed separately. The quantity \(D\) in mean-scalar normalization
was not assumed nonnegative.
The determinant convention is \([iF/(2\pi)]=a\); the associated
quadratic form was given the matching sign. This was corrected before
the final run and does not change any norm estimate.

A second investigator independently reviewed the integral proof,
including the two cap derivative coefficients, the signed
topological remainder and both orientations. This review found no
concrete gap in that chain; it is separate from the symbolic checks.

For product stability, the review covered all tensor blocks, including
harmonic one-forms, trace and relative scaling. The retained channel
consists of genuine four-dimensional TT fields. The half-collar
potential gives accumulation above \(3/8\), not arbitrarily close to
zero at fixed genus. The global \(H^2\) estimate uses covariant
integration by parts on a locally symmetric closed metric. It does
not use a uniform coordinate radius. The metric transport is exactly
\(L^2\)-unitary, and the perturbative inverse is for the compressed
reference complement, not the full moving operator.

For the positive branch, the two Chern–Weil equations were solved
independently, giving
\(\int|W^-|^2=4\pi^2-3\operatorname{Vol}\) for
\(\operatorname{Ric}=3g\) on the stated smooth type.
Gursky–LeBrun's nonzero-half-Weyl hypothesis and the equality case
were checked, not omitted. The relative \(C^0\) conclusion uses the
power two in four-dimensional volume comparison and retains the
normalization of the output metric.
The positive-branch investigator also checked that its summary
retains exactly that scope.

## Primary literature checked

- [Gursky–LeBrun, Theorem 1 and Corollary 1](https://arxiv.org/pdf/math/9807055):
  positive Einstein half-Weyl energy gap and equality case.
- [Kröncke, Proposition 4.1 and Section 4](https://arxiv.org/pdf/1508.00721):
  classical product spectra, commuting identities and negative
  Einstein product deformation spaces.
- [Jäckel, Theorem 1.1](https://arxiv.org/html/2502.16692v2):
  the strict sectional-curvature and hyperbolic-thin-part hypotheses
  which prevent direct application to the present products.

The actual-monopole input and the marked \(A_1\) construction are
inherited mathematical inputs. This round does not claim a fresh
verification of every earlier proof, a complete novelty search or
a solution of the global nonlinear Einstein problem.
