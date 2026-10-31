# Round 20 verification

22 September 2026. Four checks were executed again after the final target
construction was added. Each exited with status zero.

## Reproduction

Python 3 and SymPy are required. From this directory:

```sh
python round20_rigidity_check.py
python round20_construction_check.py
python round20_submersion_check.py
python round20_global_check.py
```

The actual interpreter used was
`/data/qiushi/qiushi_engine_v09/.venv/bin/python`. No runtime dependencies or
shared environments were changed.

| Check | Actual result | Scope |
| --- | --- | --- |
| Rigidity | Six exact identity groups passed | Projection radius, graph projections, Hodge norm, null escape, Einstein calibration, product invariants |
| Construction | Seven reported groups passed | Both surface curvatures, all sixteen coordinate Ricci entries, traces and omitted-term rejection, characteristic-form normalization, inequality constants, five-curve incidence and bundle Betti arithmetic |
| Nonflat submersion | Three reported groups passed | Orthonormal frame, horizontal Ricci defect, vertical and scalar traces with nonzero connection curvature |
| Global comparison | Two reported groups passed | Teicher branch and Chern-number substitutions, signature, intersection-form rank and Noether integrality |

The construction checker uses a flat connection and a varying fibre metric.
The independently written submersion checker instead uses a nonflat connection
and parallel fibre metric. These are complementary coordinate checks; neither
claims to sample all metrics or to prove the global signature formula.

## Proof and source checks

The primary notes contain the analytic and topological proofs separately from
their executable algebra. The main review checked the positive/negative-span
properness argument, its degenerate-span case, the product collar and integral
lattice argument, the characteristic normalization, all Ricci trace signs,
and the smooth-versus-topological distinction in the complex-surface comparison.

The newly specified bundle uses the explicit genus-two subgroup in
Crisp–Wiest, Section 4, Figure 2, and the separating-twist application of
Koberda's Theorem 1.1. The genus-six surface, exact diffeomorphism lift, section,
signature and first homology are proved in the construction note. The finite
incidence check does not independently establish the subgroup embeddings.
An independent focused review of this section checked the original genus-two
embedding, the six-torus curve realization, literal area-preserving lift,
signature and Betti calculations, and the scope of the free-factor argument;
it found no material gap in that stated construction.

The old Skill was checked before assigning novelty: its WP-signature formula,
full submersion blocks and exact basic-mean-curvature rigidity were retained
as inherited results; arbitrary free-quotient monodromy was already covered
by Round 11. The positive comparison uses classical results. No global
literature-priority certification was performed.

There was no new numerical Einstein solution, PDE existence verification, or
proof that the faithful bundle's smooth total space lies outside every older
construction. Installed Skills, system configuration and research Sessions
were not modified.
