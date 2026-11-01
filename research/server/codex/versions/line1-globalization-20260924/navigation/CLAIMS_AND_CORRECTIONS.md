# Claim scope, corrections, and supersession

This register is a reading aid for the preserved historical files. It does not
rewrite their provenance. A historical “next question” may have been answered
later; a stored program's success message is not evidence for a theorem beyond
what it checks. Result statuses and proof paths are in
[the catalogue](../catalog/results.json).

## 1. Mathematical corrections that must remain adjacent in interpretation

| Claim to avoid | Correct statement and reason | Current source |
| --- | --- | --- |
| One failed sign branch disproves the working Yau26 statement. | With \(Q_n=P_n^+\lor P_n^-\), both signs must fail in the same dimension. Their witness manifolds may differ. | [Foundations](../mathematics/current/skill/research/20260910.tex); [working map](../mathematics/current/skill/references/research-map.md) |
| Every Einstein metric has zero relative defect \(\mathcal E\). | Only a nonzero Einstein constant gives zero. Ricci-flat metrics have \(\mathcal E=4\); positive actual monopole scalar energy excludes them separately in the applications. | [Main paper, Section 8](../mathematics/current/line1_integral_rigidity_paper.md) |
| One fixed exceptional sign choice works for all metric polarizations. | Select signs for the current polarization; keep that selected actual Spin\(^c\) structure fixed while the positive conformal weight varies. | [Polarized proof](../mathematics/current/round13_chamber.md); [closure](../mathematics/current/lebrun_stability_closure.md) |
| A positive cohomology vector is an actual monopole, or ordinary basic classes enumerate every monopole. | Weighted solvability and square control are substantive inputs. Ordinary basic first-Chern sets and refined/all-monopole information are different objects. | [Special input](../mathematics/current/round5_rigidity.md); [ordinary sets](../mathematics/current/round12_global.md); [BF input](../mathematics/current/line1_bauer_furuta_geography.md) |
| LeBrun's cscK deficit unconditionally controls trace-free Ricci energy. | Unequal-curvature negative surface products are cscK equality metrics but not Einstein. On a Kähler surface, scalar variance and the primitive Chern component contribute separately. | [Kähler controls, Sections 1 and 3](../mathematics/current/line1_kahler_energy.md) |
| Ricci-energy minimization forces \(\mathcal E\to0\). | cscK blowups can approach the sharp absolute Ricci-energy infimum with a positive limiting relative defect. | [Actual blowup comparison](../mathematics/current/line1_kahler_energy.md) |
| A universal normalized integral gap substitutes for Yau26. | The fixed-piece hyperbolic-cover surgery sequence has no Einstein metric and \(\mathcal E\to0\), but its maximum Ricci defect stays positive. | [Integral counterexample](../mathematics/current/round18_integral_limits.md) |
| Yamabe normalization preserves pointwise Ricci approximation. | It has useful amplitude/integral estimates, but an actual smooth example shows the Ricci maximum defect can fail to stay small. | [Yamabe endpoint](../mathematics/current/line1_yamabe_endpoint.md) |
| The Fable W theorem produces a fixed closed counterexample. | Local AH flattening does not match physical scales to fixed shrinking cusps. A retained growing AH core conflicts with the fixed-topology CGB volume bound. The claimed global proof is withdrawn; W itself is not disproved. | [Global text](../mathematics/current/skill/research/20260916_global.tex), `sec:AH-matching`, `prop:AH-volume-budget` |
| The observed \(1/3\) log coefficient is universally sharp. | It is the leading coefficient of the specified cutoff profile. High precision does not certify an unsampled supremum or optimize over all constructions. | [Construction text](../mathematics/current/skill/research/20260916_construction.tex), `sec:profile-coefficient`; [experiments](../mathematics/current/skill/references/experiments.md) |
| A charged-OT maximum principle forces the old universal charge ceiling. | The retained forcing derivatives change the equation; the old omission invalidates that inference. The twist-free result is not imported into the charged class. | [Corrected historical appendix](../mathematics/current/skill/references/computations.md), `correction-step95-charged-ceiling` |
| The old calibrated Weyl spectrum is locally realizable because a conformal factor can be chosen freely. | Derdziński's conformal factor is tied to Weyl norm; constant norm forces the incompatible local Kähler relation. | [Corrected historical appendix](../mathematics/current/skill/references/computations.md), `correction-step7-local-rigidity`; [exact proof](../mathematics/current/skill/research/20260916_uniform_gap.tex) |
| Sphere arguments exclude every ASD Ricci-flat ALE bubble, or all rational-ball bubbles are non-spin. | Rational-ball quotients need a separate integer-homology argument. The current proof uses \(\mathbb Z_{n^2}\not\cong\mathbb Z_n\oplus G\), \(|G|=n\), in a contractible universal cover; odd-order spin quotients exist. | [Aspherical no-bubbling, Lemma 1](../mathematics/current/line1_aspherical_no_bubbles.md) |

## 2. Scope distinctions that prevent false global conclusions

- **Local, neighborhood and all-output statements are different.** A
  conformal-class exclusion, a shrinking \(C^2\) repair ball, or a selected
  degeneration obstruction does not exclude distant Einstein metrics. The
  [all-mode repair theorem](../mathematics/current/round14_repair_radius.md)
  retains its shrinking radius; the [volume-component result](../mathematics/current/round13_global.md)
  leaves infinitely many components with accumulating volumes as a possibility.
- **No local Killing fields does not give a positive perturbation distance.**
  Arbitrarily small nonsymmetric perturbations may destroy every continuous
  local symmetry. [Round 12 symmetry](../mathematics/current/round12_symmetry.md)
  is an all-output structural restriction, not a no-repair theorem.
- **A realizable curvature orbit is not a forbidden model.** Hyperbolic
  products attain the product orbit and the KE root. More accurate supply of
  their auxiliary forms need not create a contradiction. The rank-one Weyl
  model is not a classification of every Einstein Weyl tensor.
- **Average structure is not exact structure.** Small \(\fint|\nabla\omega|^2\),
  harmonic alignment, or curvature-model distance alone does not create a
  global parallel form, complex structure or exact Einstein metric.
  The new [gauge realization theorem](../continuation/20260923_gauge_saturation_ke.md)
  does prove this implication with its actual gauge supply, topology and
  diameter hypotheses, via topology-preserving compactness. Its Section 7.2
  gives a real counterexample if diameter is deleted.
- **Scalar and Ricci nonattainment do not settle full-curvature attainment.**
  On the specified \(E_D\) and shear objects, the last is equivalent to
  Einstein existence; the first two are already established separately.
- **The product-boundary results have a volume-endpoint hypothesis.**
  [Rounds 15–16](../mathematics/current/round16.md) do not describe arbitrary
  exact metrics at other volumes. The later diameter-only theorem replaces
  those hypotheses only in its different, explicitly spectrally pinched class.
- **Complete noncompact models are not closed counterexamples.**
  Double cylinders, free-circle conformal ends, flat-torus ends, one-ended
  capped spaces, and fixed closed product-block assemblies are different
  topological and asymptotic problems.
- **Actual marking and smooth type matter.** \(A_1\) chirality freedom does
  not automatically extend to higher ADE cones. A homeomorphic KE surface
  does not supply a metric on the chosen standard smooth resolution. See
  [Round 19](../mathematics/current/round19_positive_bridge.md) and
  [Round 20](../mathematics/current/round20_global.md).
- **Finite spectra do not settle full matching.** The old multi-node
  coefficients retain truncation/tail errors; same-order self, deformation,
  inter-node and complement terms belong in the same obstruction equation.
- **No general flow shortcut has been proved.** Failure of the chosen Ricci
  flow to converge is not an all-metrics obstruction. The old common-time
  flow interface is not established merely by fixed-order estimates.

## 3. Superseded tasks and results that must not be rediscovered

| Historical wording or weaker stage | Present state |
| --- | --- |
| The specified blowup near-Einstein gap still needs a collapsed local-chart theorem. | The intrinsic Round-4 integral proof supplies this application by another mechanism. The broader chart/flow question remains separate. |
| \(b_+=1\), metricwise weights and Ricci-flat are open closure tasks. | The polarized proof, closure note and independent main manuscript contain these arguments under their precise gauge/chamber assumptions. |
| Exact two-ended free-torus completion is wholly open. | Round 9 excludes the exact smoothly conformally compact boundary-free-circle class. Nonsymmetric, nonfree and approximate variants are different questions. |
| Round 17 first removed constant scalar curvature from the integral gap. | Round 4 already allowed it. Round 17 generalized the different, realizable product-structure estimate. |
| Every old \(E_D\) correction restriction is still necessary. | The Round-6 theorem allows all tensor perturbations in its stated linear-size neighborhood; it is still a neighborhood theorem. |
| Removing exact Teichmüller kernels solves product degeneration. | Full Teichmüller-valued scalar channels remain, and many small positive modes may occur. Finite-monodromy local realization is proved only with constants for each fixed geometry. |
| \(\#_4\mathbb{CP}^2\) is a new positive candidate. | The old strict Hitchin–Thorpe Ricci-box obstruction already excludes arbitrarily tight pinching of either sign; Round 19 is a strengthened endpoint check/recall, not a new candidate. |
| More unknown ordinary monopoles may push the stated hyperbolic surgery sequence to ratio \(2/3\). | Round 19 tests all eligible projection budgets and gives the asymptotic ceiling corresponding to ratio at least \(3/4\). |
| Noncommuting free-quotient monodromy is a new construction target. | Round 11 already permits arbitrary free-quotient monodromy. Round 20 instead isolates a faithful surface relation not factoring through a free group. |
| An opposite-Weyl bound is still required for the latest actual shear spectral gap. | The aspherical no-bubbling proof removes it for the specified self-gluings. The older broader bounded-geometry theorem remains valid in its own setting. |
| Relative pointwise pinching is still required for that exact shear spectral gap. | [Spectral compactness](../continuation/20260923_allowed_mode_rigidity.md), Theorem 4.1 and Corollary 8.1, now remove it. Diameter remains. |
| Only aspherical smooth topology can use the compact-core argument. | The intermediate topology extension used torsion-free \(\pi_1\) and \(\pi_2=0\); the [latest all-ALE proof](../continuation/20260924_ale_boundary_compatibility.md) needs only \(\pi_2=0\), by a finite-cover lift. |
| The latest realization always needs a Weyl bound, monopole square cost, or gauge saturation. | The latest all-ALE proof needs none for general Einstein existence with \(\pi_2=0\), diameter and positive volume. Separate actual-form hypotheses still identify stronger KE geometry. |
| A finite-range \(c_L\) can be made uniform over unbounded \(\beta\) without decay. | KE models forbid that. The compactified theorem includes the explicit factor \((\beta-2)^2/\beta^4\). |

## 4. Attribution, novelty and what verification means

### 24 September: stronger realization inputs and corrected output logic

- **A KE output completes Einstein existence on the covered input class.**
  It is not an additional output limitation. Uncovered input classes remain
  the issue; this must not be confused with nonexistence, for which excluding
  KE alone would be insufficient.
- **The mixed-chirality ALE rational-ball alternative is no longer open under
  vanishing second homotopy.** The earlier notes correctly stopped at what
  their half-flat classification supplied. The stronger existing
  Zhang/Bamler–Chen nonembedding lemma and a finite-cover lift now exclude
  every nonflat Ricci-flat ALE core; see
  [the new proof](../continuation/20260924_ale_boundary_compatibility.md).
  Neither a torsion-free fundamental group nor a vanishing Weyl half is
  needed. The older proof is preserved, not declared false.
- **Saturation is no longer needed for general Einstein existence** in that
  compact, noncollapsed, \(\pi_2=0\) regime. It still provides stronger
  KE geometry in the separate actual-form argument. The
  [bilateral theorem](../continuation/20260924_bilateral_realization.md)
  and [Chern-boundary theorem](../continuation/20260924_chern_boundary_realization.md)
  instead remove homotopy assumptions by controlling both curvature halves.
- **Diameter-free repair has different hypotheses, not none.** The
  [local-to-global theorem](../continuation/20260924_local_to_global_scope.md)
  retains unit-ball noncollapse, a full tensor linearized gap, Ricci regularity
  and small unnormalized residual. These do not follow from pointwise Ricci
  smallness by definition.

The project distinguishes a new local deduction from a new theorem in the
literature. Bauer–Furuta nonvanishing, symplectic geography, cscK blowups,
Derdziński classification, Gursky–LeBrun gaps, Einstein compactness, ALE
classification and causal boundary noncommunication remain credited external
inputs. Applying them to an actual object with verified hypotheses can be a
substantive project result; it does not rediscover the source theorem.

The parameter-family nonnegativity and classical envelope endpoints are
algebraic consequences of established curvature inequalities. The claimed
increment is their quantitative non-saturation under approximate Einstein
input and its realized applications. The catalogue records this distinction.

Reproduction programs certify their named finite algebra, coordinate Ricci
identities, arithmetic, or numerical samples. Compilation establishes readable
artifacts. Neither is a replacement for PDE, smooth-topology, gauge-theory or
global existence proofs. Historical evaluation phrases such as “major
breakthrough,” “four-journal candidate,” or “complete Skill” are not mathematical
dependencies and are not promoted to result status.
