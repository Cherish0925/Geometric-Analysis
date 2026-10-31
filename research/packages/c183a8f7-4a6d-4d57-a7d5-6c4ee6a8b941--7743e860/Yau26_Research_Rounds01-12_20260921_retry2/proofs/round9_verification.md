# Round 9: checks and proof dependencies

21 September 2026. Work was performed on the local branch
`local/yau26-research-round9-20260921`, based on `ad1bdd6`, in an isolated
research worktree. No running Session, installed Skill, service, shared
environment or external repository was changed.

## Executed calculations

Run from this directory with the existing scientific environment:

```bash
qiushi-yau26 env numeric python round9_signature_check.py
qiushi-yau26 env numeric python round9_global_check.py
qiushi-yau26 env numeric python round9_nonabelian_check.py
qiushi-yau26 env numeric python round9_bundle_check.py
qiushi-yau26 env numeric python round8_multitwist_check.py
qiushi-yau26 env numeric python round8_global_check.py
```

| Program | Observed result | What it checks |
| --- | --- | --- |
| `round9_signature_check.py` | 16 signed coordinate-jet checks, six static-auxiliary block comparisons and the exact/error Jacobi identity passed; wrong-sign and factor-of-two variants rejected | Ricci reconstructed from coordinate metric derivatives with nonflat base, varying lapse and multicomponent connection curvature; auxiliary static metric compared to the original twisted metric; mixed-block scaling; quotient separator contraction. |
| `round9_global_check.py` | Six groups passed | Complete cosh-warped countermodel Ricci tensor, positive spectral eigenfunction, weighted Jacobi conjugation and charged throat potential. |
| `round9_nonabelian_check.py` | Seven groups passed | Full and determinant-preserving Dirac-map minors, scalar-locus rank drop, quadratic trace and rank, Clifford injection and index arithmetic. |
| `round9_bundle_check.py` | Fifteen checks passed | Two-orientation Hodge interval, Bochner/error normalization, actual shear-error cancellation and pullback fibre metric. |
| `round8_multitwist_check.py` | All checks passed again | All sixteen Ricci entries of the inherited actual input, volume density, actual twist relations and homology/cohomology arithmetic. |
| `round8_global_check.py` | Seven groups passed again | Orbit scalar curvature, shape Bochner/separator constants and the inherited OT exclusion's algebra. |

The signature test uses a separate coordinate-jet implementation rather
than substituting the proposed reduced formulas into themselves. It does
not prove boundary connectedness by sampling. The global arguments are
the mathematical proofs in the notes.

## Global connector proof

The primary Galloway--Schleich--Witt--Woolgar text, Section II and
Theorem 2, was read at its actual assumptions. It requires the averaged
null energy condition and global hyperbolicity of the spacetime **with
timelike boundary**; a compact spacelike cut is an alternative to the
generic condition. It does not require vacuum Einstein equations or
nonnegative boundary Yamabe class.

The proof supplies each condition: an invariant defining function,
positive smooth compactified lapse, global quotient data, compact optical
quotient, an auxiliary static metric, compact causal diamonds and compact
spacelike boundary cuts. The null Ricci expression is pointwise
nonnegative. The cross-boundary timelike path is explicit from a finite
optical path. An earlier scaled stationary argument was simplified:
the final static construction needs neither a global connection potential
nor principal-bundle triviality. It does not change the original
Riemannian metric or require the auxiliary metric to be vacuum Einstein.

Independent readers checked these hypotheses and the signed curvature
blocks. The second, Riemannian argument was checked separately: area
minimization in a nonzero homology class inside a mean-convex compact
truncation gives an interior stable surface; testing with the circle
lapse forces connection curvature to vanish; the conserved nonzero
torus-charge component prevents that vanishing. The quotient surface
is not the full three-dimensional local separator from round 6.

Primary sources:

- [Galloway--Schleich--Witt--Woolgar, Theorems 1--2](https://arxiv.org/pdf/hep-th/9912119).
- [Hwang, Lemma 1, Riemannian circle-reduction identities](https://doi.org/10.1017/S0004972700019134).

## Closed-bundle and gauge arguments

The positive harmonic-energy gap uses existence, uniqueness and fixed-
source properness of the target optimization, then the exact Bochner/
Hodge identity and the actual infinite outer monodromy. Its constants
are not uniform as the source metric degenerates. For the constructed
inputs, a global closed fibre area form proves the energy minimum
exactly and identifies its harmonic cohomology representative.

The full-rank seed theorem is constructive: distinct positive singular
values give a surjective determinant-preserving connection map, whose
smooth right inverse solves Dirac without changing trace curvature.
On the actual almost-Kähler inputs the canonical Hermitian determinant
has nonvanishing self-dual curvature. The fixed harmonic source
connection and the variable target determinant are kept distinct.
The remaining traceless curvature equation is not solved or assumed
to have small residual.

The full `U(2)` index was checked against Zentner's formula; the
fixed-determinant `PU(2)` problem is explicitly different. A potential
transfer involving Leung's parallel equality field remains unresolved
and is isolated in an appendix, not used to assert empty moduli or
Einstein nonexistence. The original paper's product-hyperbolic converse
has not been silently discarded.

Primary references and their relevant locations are linked in the two
specialized notes. The limited literature checks here do not establish
worldwide priority. Agreement among readers and passing algebra tests
are not substitutes for the proofs, nor for a complete Yau26 argument.
