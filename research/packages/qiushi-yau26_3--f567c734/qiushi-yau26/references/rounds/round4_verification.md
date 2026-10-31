# Round-four verification and reproduction

20 September 2026. The research and checks were carried out in the isolated
local branch local/yau26-research-round4-20260920, based on round-three
commit d0e64b1. No installed Skill, live Session, service, shared environment
or external repository was modified.

## Reproduction

From this directory, use the existing mathematical environment:

The actual interpreter was Python 3.12.13 with SymPy 1.14.0.

    qiushi-yau26 env numeric python round4_rigidity_check.py
    qiushi-yau26 env numeric python round4_all_sign_check.py
    qiushi-yau26 env numeric python round4_construction_check.py
    qiushi-yau26 env numeric python round4_global_check.py

All four commands were run in this round and exited successfully.

The integral-rigidity checker verifies the truncation costs, Hessian
absorption, ideal-moment factorization, bounded-spinor approximation
coefficients, signed density algebra, topology/volume constants and
scale optimization. In particular it returned the weight cost 117/4,
the unrounded approximation coefficients 44/27, 1724/9 and 24586/3,
and the family comparison coefficient 1215.

The all-sign checker verifies the positive-normalization contradiction
and the exact optimization over a nonzero signed Einstein constant.

The construction checker derives a mixed Ricci component with varying
base metric, orbit lengths and connection; checks the charge convention,
reference integral matrix, integrated nonlinear coefficients, oriented
boundary sum and lattice covariance. Its numerical matrix symbols and
integrals are handled by exact SymPy arithmetic.

The connector checker reconstructs all nine Heisenberg slice Ricci
components from the Koszul formula, checks the moving-central-vector
identity for full symmetric matrices, the residual signs and thresholds,
and a known exact Nil cusp which must remain allowed. It also verifies
the bracket normalization with nonzero central cross terms.

## Imported identities rechecked in this round

The following three dependency checks were also run and passed:

    qiushi-yau26 env numeric python round3_independent_checks.py
    qiushi-yau26 env numeric python round3_monopole_input_check.py
    qiushi-yau26 env numeric python round3_construction_check.py

The nonabelian-connection Hessian check returned the exact energies

    Hessian = 417/32, Laplacian = 263/32,
    curvature-gradient = 5/4, half curvature-section = 57/16.

Both curvature contributions are nonzero. The check rejects either
omitted term. Other imported checks cover the positive-spin curvature
projection, monopole normalization, exact cylinder curvature and face
Ricci cancellation, the moving-gauge issue, weighted conjugation and
second-variation flux normalization.

These computations support the displayed identities. They do not compute
a numerical exact Einstein metric, prove the Banach-space theorem by a
finite sample, or establish publication priority.

## Mathematical cross-checks

- The main agent read the new proofs, recalculated the ideal/actual
  moment comparison, the Weyl-orbit approximation coefficients and the
  family transfer, and derived the all-sign corollary and exact-core
  obstruction independently of the three assigned subproblems.
- [Construction-side review](round4_review_construction.md) checks the
  modified-weight argument and the exact-core obstruction.
- [Integral-closure review](round4_rigidity_review_global.md) checks
  the Hessian/Bianchi/Hodge step, unrestricted scalar-sign transfer and
  scale optimization. The alternative class-square condition retains
  the smaller 1/4 branch of the constant.
- [Companion review](round4_global_all_sign_review.md) independently
  checks the full-matrix Nil calculation and the positive/all-sign
  corollary.

The new integral argument uses
G=(2s/3-2alpha)^2-(2s/3+2w)_-^2, not the untruncated expression valid
under negative scalar curvature in the older pointwise proof. This
distinction was explicitly checked. Similarly the nonlinear charge
boundary limit is not substituted for the still-uncomputed nonlinear
length receiver.

For the exact-core proof, the primary texts of DeTurck--Kazdan's
Theorem 5.2 and Anderson's paragraph introducing the proof of Lemma 2.6
were read. They provide Einstein analyticity and the complete,
simply connected analytic local-isometry extension theorem, respectively.
Links and the application are in [the proof](round4_exact_core.md).

No common-geometry hypothesis has been silently added to the integral
gap; no no-Einstein theorem for the closed surface bundles has been
inferred from the noncompact exact-core result. The unrestricted
two-variable connector and the full Yau26 question remain open in this
research package.
