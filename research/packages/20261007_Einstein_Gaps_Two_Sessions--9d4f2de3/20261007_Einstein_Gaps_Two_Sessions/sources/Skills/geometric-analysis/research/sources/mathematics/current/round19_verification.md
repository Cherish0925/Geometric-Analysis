# Round 19 verification

Executed in the isolated Round 19 worktree on 22 September 2026.

## Actual executions

Interpreter: /data/qiushi/qiushi_engine_v09/.venv/bin/python.
Dependencies: standard Python and SymPy; no installation or shared-runtime change.
All three commands returned exit code 0. Twelve finite check groups passed.

### round19_surgery_check.py

Command: python round19_surgery_check.py

~~~text
PASS: Codazzi mixed coefficients and intrinsic SU(2) Ricci
PASS: rotating-frame term, trace sign, and indefinite-matrix warning
PASS: short-axis intrinsic barrier and initial Hamiltonian constraint
PASS: mixed norm, matrix cone, and finite-time constants
PASS: arbitrary-radius rotation bound, cone margin, uniform lifetime
5 exact check groups passed; no closed surgery construction asserted
~~~

### round19_positive_bridge_check.py

Command: python round19_positive_bridge_check.py

~~~text
PASS quaternionic factor exchange and scalar intersection
PASS A2 discriminant linking form has no orientation-reversing isometry
PASS modified curvature budget for 40 ADE examples
PASS all Ricci-box vertices and the four simple-eigenline equality patterns
All finite checks passed; no analytic gluing or Einstein existence claim.
~~~

### round19_global_gap_check.py

Command: python round19_global_gap_check.py

~~~text
PASS: five Ricci-box vertices and separate concavity
PASS: exact box minimum branches and inverse thresholds
PASS: all-monopole 3/4 limit and explicit 17/24 threshold
~~~

## Mathematical review

- The root agent rederived the moving-frame angular velocity and the signs of
  both rotation terms. A separate topology agent also checked the first-exit
  argument and short-axis crossings.
- The arbitrary-radius extension was derived by the root agent and independently
  reconstructed by the surgery agent: the uniform mixed bound is delta/2,
  the short-block margin at delta=1/2 is -4/A^2-7/24, and the lifetime is
  less than 69/8. The original small-radius statement remains separate.
- The root agent checked the actual-metric projection infimum separately from
  the infimum over all positive period planes. The test metric bounds both;
  no surjectivity assumption is used.
- The root agent checked the Ricci-box equality proof and the quaternionic
  normalizer argument in the positive-filling note.

## External inputs actually inspected

- BBCG, Differentiable rigidity under Ricci curvature lower bound:
  author-hosted journal PDF, Theorems 1.3 and 1.6 and the preceding
  exotic-cover discussion. The literal degree-independent statement of 1.6
  is not used to prove a new uniform gap.
  https://www.math.u-bordeaux.fr/~labessie/bbcg_duke.pdf
- Farrell--Ontaneda, Theorem 1, quoting the Farrell--Jones construction:
  fixed hyperbolic base, exotic sphere, finite cover and arbitrarily tight
  sectional pinching. The original Farrell--Jones publisher PDF was
  unavailable in the agent's fetch; the primary-author account was read.
  https://arxiv.org/pdf/math/0402173
- Lock--Viaclovsky: Theorem 1.5, Corollary 1.10, quaternionic representation
  and ALE signature convention (3.5).
  https://arxiv.org/pdf/1501.03234

The notes contain further primary references at the relevant deductions.

## Limits of these checks

The programs check finite tensor and polynomial identities, linking arithmetic,
and inequality coefficients. They do not certify analytic gluing, all cited
theorems, global Einstein existence/nonexistence on unresolved candidates,
or novelty relative to the entire literature. No closed pointwise
near-Einstein counterexample was constructed in this round.
