# Marked charge, actual local concentration and signed first-order cost

27 September 2026. Base commit `fbe5404`; local branch
`local/yau26-weak-boundary-20260927`.

[Continuous proof](../continuation/20260927_marked_charge_and_first_order_flux.md),
[editable TeX](../continuation/20260927_marked_charge_and_first_order_flux.tex),
[rendered PDF](../continuation/20260927_marked_charge_and_first_order_flux.pdf).

## Mathematical changes

I50 connects the actual determinant line to a whole smooth core with its
specified cyclic boundary marking. It controls the full relative charge,
including its integer part and the boundary correction. The endpoint
application gives charge tightness on small-volume marked cores without
assuming a nonzero rescaled spinor in their interiors. Harmonic replacement
preserves the same integral line and relative charge. Finite tree cancellation
is independent of depth, with sums taken over frontiers rather than all
ancestors.

This is not torsion-index tightness. The relative characteristic identities
give explicit canonical-resolution models with unbounded opposite-spinor
index and bounded determinant charge. The new X07 construction strengthens
this distinction within the actual local gauge equation: hyperbolic balls
have torsion index d-squared, zero determinant charge and vanishing specified
subcritical costs, while quartic unit-torsion direction energy grows like
d-to-the-fourth. Every radial cut in a fixed-ratio round collar retains the
index. The construction has no prescribed exterior matching or closed global
class supply.

The torsion trace estimate retains the phase of the actual unit section.
Under the explicit whole-core decomposition and exterior amplitude routing,
an endpoint escape must have divergent normalized quartic direction energy,
at least a constant times `(H/V)^(-1/3)`. Neither this decomposition nor an
upper bound on that critical energy follows from the original weak input.
In particular, trivial-boundary torsion cores must not be discarded because
their determinant charge vanishes.

For balanced small-h families, a separate exact localization uses one
ordinary actual SW solution throughout. A coefficient below four requires
exterior ASD determinant energy or positive transition flux. Below 28/9,
positive first-order flux and a critical mixed-current contribution are
necessary. The value 28/9 is conditional on the absence of positive leading
flux, not an unconditional improvement of the all-metric coefficient.

## Parallel derivation and cross-checks

The root integrated the manuscript. Three GPT-6 Astra/max agents worked
read-only in several successive assignments; two were newly created with
clean contexts, and one existing agent was reused. This was three concurrent
subagent slots, not six simultaneous agents or three newly created agents.

- `marked_loss_20260927f` derived the marked atom, tree bounds and directional
  trace; independently checked the high-index actual local construction.
- `weak_zero_actual_20260927f` derived the harmonic bridge, budget-density
  comparison and actual local construction; independently checked the signed
  first-order balance and the trace/routing implication.
- `review_dependencies` derived the ordinary-solution spatial balances and
  independently checked marked charge, characteristic signs and sharpness.

Corrections incorporated before integration: the endpoint error is at most
one; the spinor relative-index formula requires an actual global Spin-c
extension; incoming tree boundaries have the child's outward orientation;
index additivity uses disjoint cores, not merely bounded overlap; routing
must hold throughout the selectable collars; the curvature-density argument
retains `p >= A`; and constants in the trace statement retain the collar
comparison parameter. The high-index construction chooses its radius after
the integer degree and asserts total index, not a unique transverse zero.

These are recorded mathematical cross-checks, not independent publication
certification. The inherited I40/I41 proofs were used as manuscript inputs;
the entire earlier proof library was not re-proved in this continuation.

## Classical input

[Calderbank--Singer, Einstein metrics and complex singularities](https://arxiv.org/html/math/0206229),
Theorem A and Section 2.1, provides the scalar-flat Kahler ALE comparison
metrics and the oriented resolution model. Abelian Chern--Simons
transgression, spherical-quotient Hodge theory, the relative Chern index and
Dirichlet Schauder right inverses are classical inputs. Their use does not
constitute a new ALE existence theorem or a global bubble extraction result.

## Source preservation and editable research methods

The downloaded external review and both selected user messages are preserved
in full under `guidance/source/`. The
[source receipt](../guidance/source/20260927_review_guidance_receipt.json)
records source identity, exact hashes and byte counts. The downloaded review
is byte-identical; each captured message has only a documented terminal
newline added. No unrelated raw conversation records were copied.
The original Markdown hard-break spaces at line 404 of the long user message
are retained. The staged whitespace check passes outside that source file;
it reports those two preserved spaces when run without the source exclusion.

Following the owner's explicit request, the project now has an editable
[research Skill](../skills/line1-research/SKILL.md). It routes current proofs,
permits alternate mathematical methods and scoped environment improvements,
and records the new distinctions between determinant charge, torsion index
and actual phase. The historical Skill and proof baseline remain unchanged.
The skill-creator instructions informed its concise routing structure and
validation. No installed Skill, running service, live Session or shared
runtime was modified. No package was uploaded or published.

## Executed checks and their limits

`python3 tools/check_marked_charge_and_flux.py` passed all 15 tests. They
check plumbing coefficients, relative characteristic formulas, integer and
fractional charge bounds, finite-tree cancellation, trace exponents, signed
spatial coefficients, the balanced ratios, cutoff constants, polynomial
seeds, rational samples of direction bounds, scaling and source hashes.
Finite computation does not certify PDE existence or universal compactness.

The project Skill passed `quick_validate.py` from skill-creator. The result
catalogue parses as JSON. The new proof rendered to 15 pages with no reported
TeX warnings, overfull boxes or missing characters; the exact source hash is
in the [render receipt](20260927_marked_charge_render.json).

Archive-byte and local-link verification is recorded separately in
[the library receipt](../catalog/verification.json). These checks concern
preservation and navigation, not mathematical correctness or originality.
The verifier now also checks editable Skill routes and verification-record
links, so these new entry points cannot silently outlive their proof targets.

## Remaining target

The general actual weak integral zero endpoint remains open. The next
sufficient implication must use additional actual compatibility or closed
global matching: X07 rules out recovering the needed flux bound solely from
the displayed subcritical local budgets. The marked-decomposition route is
one option, not an imposed prerequisite for a direct PDE proof.

The balanced optimal coefficient also remains open. The exact signed spatial
identity isolates the exterior ASD energy and transition flux that a better
sequence would have to exploit. The unrestricted core decomposition,
diameter-free realization and fixed E_D existence have not been settled.
