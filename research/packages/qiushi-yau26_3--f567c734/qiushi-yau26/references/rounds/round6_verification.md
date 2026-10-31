# Round-six verification

20 September 2026. The commands below were actually run in the independent
round-six worktree through the existing numeric environment. They all passed.
No running Qiushi service, Session, installed Skill, model configuration or
shared environment was changed.

```bash
qiushi-yau26 env numeric python check_round6_weighted_inverse.py
qiushi-yau26 env numeric python round6_construction_check.py
qiushi-yau26 env numeric python round6_global_check.py
qiushi-yau26 env numeric python round6_entropy_check.py
```

## What the executable checks establish

| Program | Checked content |
| --- | --- |
| `check_round6_weighted_inverse.py` | Nine exact operator identities, including the weighted adjoints, horizontal factorization and coercive partner, collar Dirichlet conjugation, and transfer mode; receiver coefficient minus pi/8; an intentionally wrong partner potential is rejected. |
| `round6_construction_check.py` | Receiver tails, finite-period averaging scale, an actual two-dimensional Ricci variation retaining the nonzero gauge-forcing term, fixed and little-o radius error orders, and the closed lower-defect coefficient. |
| `round6_global_check.py` | Direct coordinate computation of the analytic neck's scalar curvature and every momentum constraint, its twist and positive orbit curvature, the full variable-mass Ricci eigenvalues, mixed charge equation, Weyl entries and twist-energy primitive. |
| `round6_entropy_check.py` | Exact Davis Euler/signature/Betti arithmetic, all 123 chirality counts, branched-cover identities, almost-complex parity and curvature normalizations. |

These are exact algebra checks, not numerical sampling certificates for
the PDE theorems. The analytic weighted inverse, geometric cutoff transfer,
Koiso local-existence application, and topological/entropy arguments are
given in their proof notes. The new conditional AH-flattening proposition
is proved using the full Gaussian Ricci equations; no complete AH
extension was generated or verified.

## Independent mathematical checks and corrections

An independent reading of the weighted inverse and the actual closed
transfer found no blocking error. Its detailed domain, tensor, gauge,
angular and error-scale calculations are retained in
[round6_receiver_review.md](round6_receiver_review.md). It also reran the
finite-collar checker. A citation weakness was removed by giving a direct
proof of the scalar gap for the specified single nonseparating pinch;
Ji--Wentworth's hyperbolic comparison on page 493 was read separately.

A separate cross-check of the connector data confirmed the cancellation
of both terms in the momentum constraint, the charge sign, the primitive
integral torus-coordinate change and freeness at the bolt. It identified
one clarification now made in the note: a twist peak has r-coordinate
width O(c^-2), but proper radial width O(c^-1). The mixed-block norm is
also explicitly defined as one rectangular block.

Primary text checked for the local Einstein existence step was Koiso,
Proposition 6 and its constraint-propagation proof. The Davis quotient's
122 fixed points and coarse simple connectivity were checked in
Fine--Panov, Lemma 26. The discussion of AH continuation retains the
boundary-conformal-class condition in Cai--Galloway, Theorem 1.

## Scope of the outcome

The fixed-small-multiple linear-radius repair exclusion is a theorem for
the specified balanced closed bundle family. The charged Einstein neck is
local; the complete charge-removal example is one-ended. The Davis
resolution has a near-Einstein input but no all-sign Einstein
nonexistence proof here. None is a complete Yau26 proof or counterexample,
and publication priority has not been established.

All new mathematical notes and programs are kept on the local research
branch. There was no external publication or synchronization.
