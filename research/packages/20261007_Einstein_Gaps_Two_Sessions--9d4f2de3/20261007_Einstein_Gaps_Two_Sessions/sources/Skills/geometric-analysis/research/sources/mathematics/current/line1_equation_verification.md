# Verification of the two-chirality and equation-supplied advances

23 September 2026. Baseline `6065e33`; work kept on a separate local
branch and worktree. No live service or installed Skill was changed.

## Mathematical dependency and review

The main new application is `line1_two_chirality_topology.md`.
The root and an independent parallel reviewer re-derived:

- the all-sign minimization \(\mathcal E=4-I^2/(RV)\), including the
  unattained infimum when \(I=0\), and \(\mathcal E\ge4P/R\);
- both Chern--Weil identities and \(e(1-\mathcal E)\le U\);
- the \(\varepsilon/7\) transfer and the separate Ricci-flat exclusion;
- the actual ball-quotient covers, their Chern ratios and eventual
  \(b_+>1\), the integer floor construction and \(62/A_j\) bound;
- the positive pointwise gaps and the precisely stated classical
  comparison tests.

No blocker was identified in this composition. It uses the inherited
functional-pencil and energy-envelope proofs; this turn did not repeat
an independent review of every estimate in their analytic core.

For `line1_signed_harmonic_weyl.md`, the root compared the weighted
Weitzenböck formula and the integral coefficient with Catino--Dameno
equation (3.9), checked the negative signed normalization, conformal
weights, eigenvalue-collision handling and the scalar restoring test.
The scalar Young estimate uses
\(u/(u^2+uu_0+u_0^2)\le1/(3u_0)\), so its no-upper-amplitude
claim does not conceal a bounded-amplitude constant.

An independent reviewer checked the root's
`line1_einstein_spectral_application.md`: the simple-eigenvalue Hessian
formula has the correct nonnegative-Laplacian sign; the maximum principle
supplies only an upper amplitude; the scalar monopole bound supplies the
volume lower bound in the correct direction; and the spectral gap follows
from the written assumptions. No additional exact Kähler conclusion was
inferred from small positive splitting.

For `line1_half_weyl_regularity.md`, the root and another reviewer checked
the Hessian interchange identity: commuting on the bundle-valued
one-form \(\nabla z\) produces the Ricci contraction and one bundle
curvature term, but no derivative of bundle curvature. The induced
\(\operatorname{Sym}_0(\Lambda^+)\) connection sees \(W^+,s,\operatorname{Ric}^\circ\)
and not \(W^-\). The spectral projector estimates retain their required
isolated-eigenvalue gap. The nonzero PDE source is explicit and is not
asserted to follow from pointwise Ricci bounds.

## Finite reproduction

`verify_line1_equation.py` was run with the shared scientific Python,
writing `evidence/line1_equation_checks/`. All four scripts exited zero.
The evidence contains stdout, return codes, checker hashes and hashes of
the four new Markdown, TeX and PDF artifacts.

| Checker | What it checks |
| --- | --- |
| `check_line1_two_chirality_topology.py` | Chern--Weil and defect algebra; rational ratios, floor-error margins and classical comparison arithmetic; wrong orientation/trace-free coefficients rejected |
| `check_line1_signed_harmonic_weyl.py` | Signed normalization, spectral coefficients, conformal powers, scalar potential and reaction linearization; wrong signs/factors rejected |
| `check_line1_half_weyl_regularity.py` | Curvature polynomial, projector derivatives, equation residual and target-orbit distance; wrong signs/factors rejected |
| `check_line1_einstein_spectral_application.py` | Ordered-eigenvalue algebra, maximum-principle reaction, Kähler endpoint and Chern--Weil rearrangement; wrong splitting sign rejected |

These finite computations do not prove Seiberg--Witten solvability, the
global differential estimates or literature priority. Those depend on
the written proofs and identified primary inputs.

The four new PDF manuscripts compile successfully from the packaged TeX.
The root's spectral note emits only a mathrsfs font-size substitution
warning; no undefined references or overfull boxes were reported there.

## Retained provenance

The analytic and topological chains are indexed in
`START_LINE1_TWO_CHIRALITY_20260923.md`. Earlier sources, proofs,
checkers and the Skill snapshot are retained unchanged. The new main
application is a deduction from the existing stability mechanism, not
an independent replacement for that mechanism. Its actual topology
coverage is broader than the recorded one-third band; exhaustive
world-priority and journal evaluation have not been performed.
