# Round 14: checks and proof dependencies

## Executed calculations

The root agent ran all five commands below from the Round-14 directory
using the existing v09 Python interpreter with SymPy 1.14. All returned
exit code zero. They also run with a compatible Python/SymPy installation;
no old Session path, network service, GPU, or private input is required.

```bash
python3 round14_rigidity_check.py
python3 round14_shear_check.py
python3 round14_collar_check.py
python3 round14_global_check.py
python3 round14_repair_radius_check.py
```

| Program | Checked identities |
| --- | --- |
| Rigidity | Cover factors, 16 quotient cohomology cases, scalar saturation, blow-up ratio, all-cover shear budget, twisted connected-sum loss, critical infinite family, sign-invariant Weyl model; two incorrect normalizations rejected |
| Shear | Ten Ricci blocks independently derived from coordinate Christoffel symbols; harmonic TT stress, Hodge-energy variation, connection capacity, finite-interval response, complete-throat constants; wrong-weight optimizer rejected |
| Collar | Coordinate covariant tensor Hessian on both radial polarizations; divergence, exact kernel, conjugation, factorization and partner gap, scalar potential, cutoff density; wrong profile and potential rejected |
| Global | Nineteen exact identities for Maxwell profile, trace-free norms, scalar and Ricci-energy coefficients, conformal scalar equation, integrated volume cancellation, Yamabe deficit, optimal Einstein constant, relative integral defect and receiver energy lower bound; wrong Maxwell profile rejected |
| Repair radius | Recomputes the shear checker, then independently differentiates coordinate Christoffel/Ricci tensors; exact TT identity on the sheared metric, all ten first-variation blocks, trace-free elimination of the Einstein-scale term |

The repair-radius script imports `round14_shear_check.py` for its coordinate
metric and freshly calculated connection. These are two programs, not two
independent derivations of the original metric. The subsequent coordinate
Ricci first variation is additional computation. None of the five programs
tests a global gauge-theory existence theorem or certifies a nonlinear PDE
existence argument.

## Mathematical cross-checks

The root agent read the finite-cover, twisted-input, shear, scalar-calibration,
and all-mode repair proofs. A separate agent checked the full collar
complement proof, including all tensor summands, the second radial
polarization, the nonzero angular modes, and the min--max step.
That agent also independently reviewed the complete all-mode repair
argument and the scalar-calibration estimates. The review recomputed the
core first variation for a general harmonic shear form, rather than relying
only on the single local coordinate model in the finite program.

The important checks beyond finite algebra were:

- The round-3/4 integral proof uses only metric-curvature weights and the
  constant weight; smoothing them equivariantly preserves the majorant
  inequalities. No ordinary nonvanishing on all cover metrics is assumed.
- The lifted twisted characteristic class has twice the downstairs square
  and self-dual norm, matching twice the volume and topological numbers.
  The actual glued class has square at least the required topological
  quantity; this is not inferred from the ordinary SW dimension formula.
- The quotient SW-vanishing proof uses scalar-energy equality to force a
  parallel two-form, then uses the actual deck action to rule it out.
- The collar has two radial polarizations. Its nonzero angular bound uses
  a **finite collar with maximal radius tending to zero**; it is not a
  false claim that a complete hyperbolic funnel has only two TT modes.
- The full-collar pure-shear construction is distinct from that smaller
  collapsing subcollar. Its outer radius is of fixed order; the receiver
  proof there uses exact product bands, not the small-radius angular bound.
- Scalar repair uses explicit uniform unwrapped local charts and the global
  maximum principle. Its volume identity retains every background term and
  distinguishes the original and conformally repaired Ricci-energy coefficients.
- The repair-radius proof includes the ungauged Bianchi term. Its test tensor
  is extended smoothly by zero before closed-manifold integration by parts.
  The quadratic Ricci remainder is a covariant pointwise estimate, valid for
  arbitrary perturbations with small geometric \(C^2\) norm.
- Excluding other Einstein constants uses a separate trace-free pairing and
  a bound on the possible constant. It is not inferred merely from a lower
  bound for the fixed normalization's residual.

## Primary inputs checked against their text

- [Ishida--Matsuo--Nakamura, *Yamabe invariants and the Pin-minus monopole equations*](https://arxiv.org/pdf/1505.05948): Section 2, Proposition 8 (lifting and curvature estimates), Proposition 9 and its proof (actual classes, arbitrary exceptional signs, and projection budget), and Theorem 16 (the already-known exact obstruction). The hypotheses of Proposition 9 do not include the Yamabe assumptions used separately in the paper's Yamabe-equality theorem.
- [Delay, *Spectrum of the Lichnerowicz Laplacian on asymptotically hyperbolic surfaces*](https://arxiv.org/pdf/0802.3174): Section 2 supplies the surface Weitzenbock identity with the conventions used in the complement proof. The radial factorization, finite-collar estimate and product decomposition are written out in this round.
- [LeBrun, *Monopole classes and the Einstein equation*](https://arxiv.org/pdf/math/0611450): the conformal weighted-monopole input used in the inherited proof. The present extension also checks the specific weights in `round3_monopole_input.md`, `round4_rigidity.md`, and `round13_chamber.md`.

The integral theorem, the original closed smooth gluing, its symplectic
classes and variational invariant remain explicitly cited earlier proof
inputs. This round does not substitute five successful checks for a fresh
audit of the entire preceding archive, and does not claim a completed
literature-priority review.

All work is local to the isolated research worktree. No installed Skill,
live service, Session configuration, user selection, model route, or GPU
allocation was changed.
