# Round 12: proof review and executable checks

21 September 2026. Work is confined to the local Round 12 research
worktree; no running Session, installed Skill, shared environment,
service or external repository was changed.

## Executed checks

The parent reran these commands in the existing numeric environment:

```sh
qiushi-yau26 env numeric python round12_global_check.py
qiushi-yau26 env numeric python round12_repair_check.py
qiushi-yau26 env numeric python round12_uniformization_check.py
qiushi-yau26 env numeric python round11_closed_gluing_check.py
qiushi-yau26 env numeric python round11_graph_topology_check.py
```

All five final runs succeeded. Their scopes are distinct:

* `round12_global_check.py`: the canonical Gram matrix, the exact
  square identity forcing the proportionality coefficient to be
  plus or minus one, and the neck-map rank in the explicit example.
* `round12_repair_check.py`: coordinate Christoffel/Ricci calculation
  with evolving fibre area, electric and magnetic connection
  curvature, and a spatially varying circle radius; the weighted
  constraint, radius cancellation, and Maxwell shear energy.
  Three deliberately incorrect formulas were rejected.
* `round12_uniformization_check.py`: oriented Clifford algebra,
  both quadratic wedge terms, the graded projection/Dirac relation,
  the central coefficient, positive graded Chern pairing, characteristic
  classes, dual-spinor normalization, and the hyperbolic exact model.
* `round11_closed_gluing_check.py`: all 16 entries of each inherited
  coordinate Ricci-defect formula and the corresponding wrong-formula
  checks.
* `round11_graph_topology_check.py`: the two explicit integer
  presentations, Smith forms and Betti-number calculations.

The first parent run of the new Clifford checker stopped at a
structural equality comparison between algebraically identical SymPy
expressions. The assertion was changed to simplify their difference;
the entire checker then passed. No failed assertion was removed or
converted into a successful output.

The parent also checked 37 local Markdown links in the new notes and
the top-level navigation; none was missing.

## Mathematical review

The parent read all new proof notes. An independent agent checked the
ordinary basic-class proof, including the order of the simple-type
and adjunction arguments, the real Mayer--Vietoris neck space, and
the integral equality statement in Taubes's original Theorem 2.
The hypothesis \(b^\pm\ge2\) is now stated explicitly.

Two agents independently checked the parent's global symmetry proof
against Farb--Weinberger's Theorem 1.3, Einstein analyticity and
Nomizu extension. The proof was strengthened to cover arbitrary
metrics on finite covers: it repeats the finite-index subgroup
argument rather than only considering lifted metrics. The sources
and the complete proof are in `round12_symmetry.md`.

The collar argument was checked at both the geometric and algebraic
levels. The spatial Laplacian is retained in the unrestricted formula;
the Teichmüller estimate is stated only in the orbit-radius-only
sector. No coordinate-dependent deformation is substituted for a
marked mapping-class displacement.

The parent checked the Clifford-block proof after requiring that the
indefinite connection's Chern energy be derived with the graded Hodge
operator. Its solution classification concerns exactly the written
system, not every equation called a nonabelian monopole equation.
The Schoen control is an application of an established algebraic
surface construction, not a new example attributed to this project.

The executable checks do not prove gauge theory, analytic continuation,
or the global gluing theorems. Those deductions are written out with
their mathematical inputs. This round does not prove arbitrary
Einstein nonexistence or establish publication novelty.
