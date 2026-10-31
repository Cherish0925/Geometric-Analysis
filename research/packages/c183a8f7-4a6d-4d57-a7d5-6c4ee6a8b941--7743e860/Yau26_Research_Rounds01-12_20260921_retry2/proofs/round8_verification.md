# Round 8: reproduction and proof dependencies

21 September 2026. The following programs were run in this isolated
worktree using the existing scientific environment:

```bash
qiushi-yau26 env numeric python round8_nonabelian_check.py
qiushi-yau26 env numeric python round8_construction_check.py
qiushi-yau26 env numeric python round8_global_check.py
qiushi-yau26 env numeric python round8_boundary_check.py
qiushi-yau26 env numeric python round8_multitwist_check.py
```

| Program | Observed result | Scope |
| --- | --- | --- |
| `round8_nonabelian_check.py` | Eight groups passed | Projection norms, spinor Chern identity, graded trace projection, critical-distance commutator estimate, sharp complex-ball curvature arithmetic and constants. |
| `round8_construction_check.py` | 41 checks passed | Based twist relators, Euler-product maxima and volume constants, the power-twist torsion distinction, real versus complex projective centralizers. |
| `round8_global_check.py` | Seven groups passed | Full coordinate scalar curvature for an arbitrary orbit matrix, shape-target curvature, Bochner and separator constants, charged off-diagonal Ricci component and charge-adapted shear current. |
| `round8_boundary_check.py` | Three groups passed | Full boundary Ricci contraction for arbitrary two-jets, the finite positive end pairing, integer winding and a complete mixed-block solution with nonzero remaining Ricci defect. |
| `round8_multitwist_check.py` | All checks passed | Independent Koszul reconstruction of all sixteen Ricci entries, the exact operator-norm polynomial, volume density, twist relators, fibre-homology coinvariants, noncommuting monodromies and the rank-dependent Euler-product bound. |

The scripts include tests that reject a missing scalar Hessian term, a
wrong boundary scalar coefficient, and two overextensions of the group
factorization. They do not replace the global variational, topological,
maximum-principle or connection arguments given in the notes.

For the multiple-twist metrics, the parent read the fixed gluing, collar
construction, smooth endpoint matching and orthonormal derivative argument.
The previously installed manuscript already contains the broader
free-quotient construction; this round does not claim its specialization
as a new metric mechanism. The new family-level representation formulas
retain the residual genus-zero and genus-one cases and do not import the
single-twist example's odd-Betti or finite-cover conclusions.
An independent group/cohomology review checked that mixed degree-two
classes in the quotient do not create an omitted representation Euler
class: commuting nontrivial factor images have abelian total image and
zero real Euler class. It also checked the noncommuting full-generator
variant, signature bordism, homology coinvariants and the separate
positive-scalar and Ricci-flat exclusions.

## Independent mathematical checks

Separate readers checked the full OT proof: confinement of the minimizing
essential loop, invariant minimality, the Gauss-equation signs and the
shape-energy ceiling. The nonabelian argument was checked at connection
level, including induced line curvature and the trace-free projection
constant, without assuming the unresolved ordinary/nonabelian quadratic
sign. The parent independently read the group factorization and checked
the low-genus and power-twist restrictions.

For the static-circle exclusion, the primary Galloway--Schleich--Witt--Woolgar
Theorem 2 explicitly permits a compact spacelike cut **instead of** null
genericity. Its modified averaged null energy condition holds for vacuum
Einstein, with zero integrand. The optical compactification is an actual
ultrastatic product with compact spatial completion, providing strong
causality and compact causal diamonds with timelike boundary. Flat
holonomy removal and changing a constant irrational torus lattice were
checked separately; neither is claimed to be a global isometry of the
original marked metric.

The shear boundary theorem uses the interior maximum principle, not a
uniform ellipticity claim at conformal infinity. The relative-end Jacobi
modes are pure marking/gauge directions: their pairing with a compactly
supported conserved source vanishes, and they disappear under the larger
boundary-translation quotient.

## Published inputs checked at their actual hypotheses

* Leung's 2000 Proposition 2.4: the graded block connection and required
  projective ASD implication. Its ambiguous quadratic-map identification
  is not used.
* Leung's 1996 rank-three uniformization construction: bundle, determinant,
  central curvature and complex-ball equality case for the sharp example.
* Calderbank--Pedersen Proposition 3.2: nonzero-scalar selfdual Einstein
  metrics with two commuting Killing fields have orthogonally transitive
  action.
* Galloway--Schleich--Witt--Woolgar, Theorem 2: disconnected conformal
  boundaries cannot communicate under the stated Lorentzian hypotheses.
* Cai--Galloway, Theorem 1: the nonnegative-Yamabe boundary obstruction.
* Anderson, Theorem 5.4: its relative fundamental-group condition does not
  hold for this two-boundary cylinder. No independent extension of all
  boundary symmetries is assumed.
* Classical Milnor--Wood bounds, extremal Fuchsian representations and
  cyclic centralizers of strictly negatively curved manifold groups.

Primary links are attached to the corresponding arguments. This is not a
comprehensive originality search. The result status is the mathematical
scope of the stated proofs, not a count of checks or agreement among
readers.

All files are local research artifacts. No installed Skill, research
Session, GUI service, shared environment or external repository was changed.
