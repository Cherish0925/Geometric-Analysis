# Round-three verification

19 September 2026. All commands below were executed in this independent
local worktree. No live Session, Skill, service or shared environment
was modified.

## Mathematical derivations

The intrinsic monopole proof and its blow-up specialization were read
independently by the root, construction and global researchers. Their
checks are preserved in
[the first review](round3_rigidity_review.md) and
[the second review](round3_rigidity_second_review.md).
The complete model theorem was independently examined by the root and
rigidity researcher; see [the construction review](round3_construction_review.md).

The checks addressed the points on which the conclusions depend:
the absence of a missing connection-curvature derivative in the Hessian
identity; extensive, rather than volume-dependent, norm estimates;
the positive-spin representation and determinant anti-self-dual
curvature; testing Bianchi against the actual divergence tensor;
smooth-weight approximation; the complete nonlinear residual at all
model faces; weighted invertibility; nondecaying parameter backgrounds;
and removal of the gauge term without assuming the Einstein equation.

The research notes contain the arguments. Agreement among reviewers is
not used as a premise of any theorem.

## Executable checks

Each command has the form

    qiushi-yau26 env numeric python <file>

| File | Checked content | Outcome |
| --- | --- | --- |
| round3_rigidity_check.py | Nonconstant unitary-connection Hessian identity; Clifford chirality; weighted energy coefficients | Passed |
| round3_monopole_input_check.py | Rescaled spinor normalization; exact Holder deficits; Hopf differential; good-set spectral gap and Weyl-model constants | Passed |
| round3_independent_checks.py | Nonabelian periodic connection; omitted-term negative checks; positive-spin curvature projection; normalization; topological completed squares and connected-sum class squares | Passed |
| round3_construction_check.py | Exact cylinder curvature; every Ricci block at the radial faces; gauge error; conjugation; projected correction ODE, tails and fluxes | Passed |
| round3_matching_check.py | End-parameter shifts; four interface equations; invariant channel sums; marked twist and physical scaling | Passed |
| round3_global_check.py | All warped-product Ricci components; free-boundary index flux; signed moments; sharp width inversion | Passed |
| round2_rigidity_check.py | Imported calibration constants, first-jet identity, weighted energies and endpoint example | Passed again |
| round2_construction_check.py | Imported full ten-sector model operator, quadratic source, Bianchi and spectral factorizations | Passed again |
| round2_construction_cross_check.py | Independent full mixed quadratic Ricci matrix and its projections | Passed again |
| round2_global_checks.py | Imported twisted soliton, coordinate shear, charge threshold and transport scaling | Passed again |

The nonabelian check obtains the exact torus-averaged energies
\[
\|\nabla^2u\|^2=\frac{417}{32},\quad
\|Lu\|^2=\frac{263}{32},\quad
\text{curvature-gradient term}=\frac54,\quad
\tfrac12\sum_{ij}\|F_{ij}u\|^2=\frac{57}{16}.
\]
Their sum satisfies the Hessian identity; deleting either curvature
term fails it.

The independent abelian example gives
\[
\frac{371}{16}=\frac{329}{16}+\frac14+\frac{19}{8}.
\]
The construction check recovers the total quadratic receiver flux
\(\pi^2(b_1^2+B_1^2)/2\).
The width checker gives \(L_{\min}(10^{-6})=16.300414658143\)
in dimension four.

These are exact algebraic checks except the displayed decimal evaluations
of the proved width formula. They do not numerically approximate a
closed-manifold Einstein solution.

## Execution environment

The existing qiushi-yau26 launcher resolved the numeric environment to

    /data/qiushi/runtime/releases/gpu-python-3-12-13-c5028c26082aae76bb0d68b42399085e0112394cf9a7fd14adcfb89cea5a1af1/bin/python
    Python 3.12.13
    SymPy 1.14.0
    mpmath 1.3.0

No package installation or upgrade was required. These scripts use CPU
symbolic arithmetic and do not require a GPU allocation.

## Scope

The analytic existence and gap statements are proved in the accompanying
notes; finite symbolic tests alone do not certify them. The near-Einstein
gap retains actual monopole hypotheses. The exact construction is a
complete invariant noncompact model. Its closed-manifold matching law
retains the stated interface hypotheses, and the complete global
\(E_D\) Einstein problem is not settled.

This round does not establish priority over the entire literature.
Classical inputs and relevant primary sources are linked in the proofs.
All new work is retained on a local Git branch with the preceding rounds;
nothing has been published or sent to an external repository.
