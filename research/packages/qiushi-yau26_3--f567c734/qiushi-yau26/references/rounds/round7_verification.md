# Round 7: checks and dependencies

20 September 2026. All commands below were executed in this isolated
worktree through the existing `qiushi-yau26 env numeric` environment.
No package installation, live Session change, or installed Skill update
was performed.

| Program | Actual result | What it checks |
| --- | --- | --- |
| `round7_endpoint_check.py` | 17 checks passed | Concentration coefficients, completed square, symmetric-source ratios, reversed-Kähler slope, critical Weyl estimates; a wrong denominator is rejected. |
| `round7_topology_check.py` | Four groups passed | All 123 chirality counts, characteristic parity, possible special-class indices, stable-cohomotopy parity and the positive-bolt cases. |
| `round7_spectral_check.py` | Four groups passed | Harmonic Hessian decomposition, exponent and residual signs, Ricci recomputed from a coordinate metric, twist coefficient, and an exact complete twisted AH example. |
| `round7_rigidity_check.py` | Four algebraic groups passed | Wedge-dual matrix identity, frame covariance, determinant charge and rescaling in the explicitly defined projection model. |

The analytical arguments are in the four accompanying notes. The programs
do not prove the inherited log-Weyl construction, monopole estimates,
Bauer--Furuta adjunction and target identification, harmonic boundary
regularity, or published uniformization theorems. Those dependencies are
stated and linked where used.

Two independent readers checked the concentration argument and the
harmonic-separator calculation; this led to explicit treatment of the
critical set, end cutoffs, nonzero monopole denominators, and the distinction
between the classical critical ratio and the prior stronger special-class
gap. These are checks of specified arguments, not a certification of all
prior research or of publication novelty.

The nonabelian comparison required a substantive restriction: the published
author's canonical-line and spinor-determinant conventions do not let the
relative quadratic sign be inferred from a matrix identity alone. The
explicit-model calculation is retained, but it is not reported as a proved
obstruction to the published nonabelian system. That correspondence remains
unresolved.

This round proves no unrestricted Yau26 branch and constructs no closed
manifold with both a vanishing Ricci defect and all-sign Einstein
nonexistence. Its results are the stated compatibility theorem, deductions
about the actual Davis fillings under the inherited construction, and a
global spectral necessary condition for complete connectors.
