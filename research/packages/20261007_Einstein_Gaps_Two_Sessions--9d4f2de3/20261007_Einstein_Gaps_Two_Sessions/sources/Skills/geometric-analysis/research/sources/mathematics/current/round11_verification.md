# Round 11: calculation and proof checks

21 September 2026. The parent reran the following commands in the
existing `qiushi-yau26` numeric environment, with Python 3.12.13 and
SymPy 1.14.0:

```sh
qiushi-yau26 env numeric python round11_closed_gluing_check.py
qiushi-yau26 env numeric python round11_graph_topology_check.py
qiushi-yau26 env numeric python round11_rankone_check.py
qiushi-yau26 env numeric python round8_multitwist_check.py
qiushi-yau26 env numeric python round10_nonabelian_check.py
```

All five commands completed with exit code zero.

| Check | What was actually checked |
| --- | --- |
| Closed gluing | Independent coordinate Christoffel/Ricci calculation; every entry of the shear defect and of a nonzero-trace hyperbolic path defect; orthonormal-frame normalization; three incorrect mixed/trace formulas rejected |
| Topology | Integral presentation matrices, exact Smith normal forms, no torsion, symplectic monodromy matrices and the two Betti-number tables |
| Rank one | Eight exact Clifford, exterior-algebra, curvature-block, pairing and Chern-normalization checks |
| Earlier multitwist family | The earlier full Ricci tensor, operator norm, collar, group-relator and representation-volume calculations |
| Earlier gauge family | Quadratic map, determinant/Chern form, actual product residual, source connection and rank-one partial-seed checks |

The metric theorem is proved in `round11_closed_gluing.md`: hyperbolic
collar existence, fixed global gluing, disjoint interpolation supports,
the uniform estimates, exact volume, Moser endpoints and symplectic
forms are analytic/geometric arguments. They are not inferred from
point samples. The coordinate program tests nonzero fibre divergence
and nonzero path trace; it does not merely test a diagonal or
divergence-free special case.

The parent read the new proofs. The topology and rigidity agents also
independently checked the metric assembly and tree argument. For the
Kähler obstruction, the parent and both reviewers read Nicolás's
Theorem 25 and Lemma 24 directly: nonfaithful action is allowed,
finite generation comes from the compact generic fibre, and the
finite-index minimality/no-fixed-end conditions are checked in the
proof. The no-surface-bundle conclusion comes from the written group
argument, not the homology program.

The variational note was read in full by the parent. Its scalar
negative-part bound is derived from the monopole Weitzenböck formula;
the full-curvature convention is fixed explicitly. Its key distinction
is that scalar/Ricci equality forces Kähler geometry, while full-Riemann
energy equality only forces the Einstein equation. The latter is still
an open attainment problem for these objects.

Primary sources used for these deductions are linked at their relevant
statements. The Taubes paper is also available through the publisher's
[current PDF endpoint](https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1806607694305849346-1806607694305849346-d452d5e2544ec5237395f95c572f3f35.pdf);
the older publisher PDF URL returned HTTP 403 in the parent check.

These checks support the specified deductions, not publication novelty,
a formal verification of all proofs, or an all-Einstein obstruction.
No shared environment, running Session, installed Skill, service or
external repository was changed. The research is retained in this
local branch.
