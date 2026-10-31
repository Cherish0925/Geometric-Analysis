# Linear beta=2 cost: proof continuation and checks

27 September 2026. Base `168bea5269692fce531c4fea72d51a0a5766bb54`.
Local task branch: `local/yau26-mixed-flux-20260927`.
Main proof: [linear cost and small-h order](../continuation/20260927_mixed_current_and_signed_cores.md).

## What changed mathematically

I38 localized the positive topological cost of a hypothetical E=o(h)
sequence but did not exclude it. The new proof, I40, does exclude it.
The bounded KE model annihilates the calibrated actual spinor. Retaining
that cancellation in the exact Hessian identity removes the old additive
volume term. The class-square condition controls determinant ASD energy
by the unknown gradient energy plus the actual defect. Weak Bianchi then
absorbs that unknown energy, rather than assuming its smallness.

This yields Sigma,p-T+ <=C(rV+D2), the required mixed-term estimate,
and the all-metric window E+(U-1-h)+>=c h. The previously realized
small-h family consequently has inf E comparable to h. An explicit
square-shortfall variant retains linear order when the shortfall is
O(Ah). The main theorem does not use the stronger, still open estimate
Sigma<=C(P_Ric+D2). Its rV term includes scalar variation.

The construction-side calculation separately proves a reverse-surgery
cap-energy inequality, with coefficient4 sharp in its specified cheap-cap
class. This is not a claim of optimal coefficient over all metrics.
Nearby-beta transfer and signed-current square completion are direct
corollaries/identities, not additional independent main discoveries.

## Sources and actual dependencies

The new downloaded note was read completely and preserved byte-for-byte;
see [receipt](../guidance/source/20260927_mixed_current_receipt.json).
Its mixed-current refinement, axial cancellation and actual curvature
equation retain their source attribution in Sections1--3 of the proof.

The proof uses the inherited functional pencil's actual conformal supply,
same-solution amplitude, phase and curvature-model bounds; the preceding
actual-cost proof's low-amplitude estimate and scalar-slack identity;
and the bounded-form criterion's exact Hessian, polynomial divergence
and weak-Bianchi formulas. All are linked from the proof. None requires
the not-yet-proved linear conclusion. Classical upper-bound gluing is
used only for the upper half of the final order comparison.

The project mathematical Skill was read in full. It guided preservation of
the actual-class quantifiers and the separation of analytic proof, finite
calculation, scope and priority. It did not supply an automatic theorem
or authorize changing an installed Skill or live research system.

## Parallel work and targeted independent re-derivations

Three clean-context agents used the owner's requested `gpt-6-astra`,
`max`, read-only, on bounded tasks. Root owned all file edits.

- `direct_mixed_20260927`: derived the refined Hessian--Bianchi closure,
  checked the low-amplitude/phase dependencies and the square-shortfall
  extension. It did not assume a Sobolev constant or a curvature derivative.
- `signed_flux_20260927`: independently checked the polynomial model's
  action, exact Hessian signs and curvature norms, Chern--Weil constants,
  noncircularity and signed-current completion; derived nearby-beta transfer.
- `actual_construction_20260927`: independently derived the all-metric
  sign/rescaling branches, constants49/112, feasible frontier, exact family
  asymptotics and reverse-surgery cost. Construction attempts did not produce
  an actual sublinear metric in the stated family.

After integration, all three read the relevant complete sections, not just
the proposed conclusion. Their specific corrections were incorporated:
the family is in §3, Theorem5 of the boundary proof; uniform torsion bounds
require bounded kappa; the shortfall variant explicitly drops the square
condition; and coefficient4 requires h->0 and diagonal gluing errors o(h).
Root separately checked the same-solution dependencies and each absorption.
These are internal mathematical checks, not external peer review.

## Finite checks

- `python3 tools/check_mixed_current.py`: 13 tests passed.
- `python3 tools/check_actual_topological_cost.py`: 7 tests passed.
- `python3 tools/check_boundary_compatibility.py`: 7 tests passed.

The new checks cover exact graded exterior algebra in transgression,
signed square completion, primitive derivatives, model roots, mass,
topological bootstrap constants, all-metric conversion, surgery identity
and the auxiliary Eguchi--Hanson radial profile. They do not certify
PDE existence, integration estimates, all-metric quantifiers or originality.
The finite tests supplement, rather than replace, Sections4--5's proof.

The result catalogue's 85 IDs were checked for uniqueness, dependency
resolution and existing proof paths. Local links in changed proof/navigation
files were checked; the source note's bytes and SHA-256 match the download.
`git diff --check` passed. These are archival checks, not mathematical evidence.

## Retained construction-side tests, not premises of I40

The bounded-spinor Liouville shortcut was rejected. On the standard
Eguchi--Hanson space X=O(-2), the canonical section s_Z of E=O(Z), with
|s_Z|^2=(r^2-a^2)/(r^2+a^2), has an ASD Chern connection: the radial
calculation is r^3(1-a^4/r^4) d(log|s_Z|^2)/dr=4a^2. Tensoring it with
a parallel positive spinor gives a bounded, nonparallel twisted harmonic
spinor. In the framing used by the construction analysis its relative
charge is -2 and determinant ASD energy is 32pi^2. Its cubic torsion is
zero because Phi wedge nabla Phi=0. This is an ideal core, not a solution
of the full positive-weight SW curvature equation, and its charge has the
wrong sign to pay a handle's positive charge. The metric and twisted-mode
background is [Franchetti--Krasnov](https://arxiv.org/abs/2309.08453).

The same analysis found a useful approximate-core flux certificate. On
annuli of radii r_i where |Phi|>=m>0, put w_i=Vol(A_i)/r_i^4,
f_i=int_Ai|F_{S+}|^2 and q_i=int_Ai|nabla Phi|^4. Coarea and Holder
give suitable boundary radii with total absolute flux at most
C(sum w_i)^(1/4)[m^(-1)(sum f_i)^(1/2)(sum q_i)^(1/4)
+m^(-3)(sum q_i)^(3/4)]. Thus O(Ah) annular volume-ratio and curvature
budgets plus o(Ah) quartic budget suffice for o(Ah) flux. The hypotheses
were not derived from arbitrary near-Einstein input and are not silently
inserted into I40. The actual proof instead closes the global spinor budget.

## Continuation and remaining boundaries

The previous saved trajectory ended after a local commit and a final
response. The inspected record did not exhibit a quota or scheduler error,
and it did not establish an independently running continuation process.
No such process or automatic between-turn persistence is claimed here.
In this turn, intermediate current and core results were followed by the
next sufficient estimate, which led to the main closure and its cost variant.

Zero-Weyl weak rigidity remains distinct: beta=2 model annihilation does
not persist there, and a small Dirac residual alone is insufficient.
The stronger scalar-variance-free estimate and the global optimal coefficient
are open; neither is needed for the completed linear-order theorem.
No fixed-E_D Einstein decision, diameter-free realization or full Yau26
solution is claimed. A further clean-context agent was assigned the zero-end
coupled equations, not another review of the completed small-h theorem.

That continuation produced Section8 after the main closure was committed
as `b2653dc`. Agent `zero_endpoint_system_20260927` derived a regularized
coupled Lichnerowicz test at the available norms. Root introduced the
reciprocal scalar test and its Jensen defect; the agent independently
checked it and added the growing-weight scalar test. They give strong
torsion-length convergence in all normalized Lq below2, small-torsion
volume O(sqrt eta), and a net derivative balance with limit64/27.
All statements retain a possible concentrated derivative defect and
possible topological charge on the low-torsion region. The construction
does not require the unweighted Dirac residual to converge in L2.
Root independently checked the test derivatives and curvature signs;
the Clifford defect inequality, reciprocal identity and derivative
square completion have additional finite checks. These extend I39,
not a new zero-end gap theorem.

The signed-flux agent then independently read all of Section8, verified
both scalar-test norms, the weighted Dirac commutator, curvature duality
factor4, smoothness at zeros, the quartic sign and limits64/27 and1/27.
No mathematical correction was needed. It confirmed separately why the
positive S+ ideal-core sign cannot be transferred to S- tensor L: the
latter contains positive uncontrolled opposite-Weyl curvature. This
precise remaining boundary is recorded in (8.12), not hidden by the new
length-concentration conclusion.

Everything remains local. No push, external publication, service or Session
change, installed Skill modification or inherited proof overwrite occurred.
The frozen eight-volume package was not regenerated. Current navigation
identifies I40 separately, so older exported statements do not silently
become the latest research state.
