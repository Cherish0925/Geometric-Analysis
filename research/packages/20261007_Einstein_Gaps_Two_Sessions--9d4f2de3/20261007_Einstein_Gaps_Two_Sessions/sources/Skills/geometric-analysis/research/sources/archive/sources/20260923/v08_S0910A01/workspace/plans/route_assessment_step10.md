# Route assessment after Step 10

## Retained advances

1. **Four-dimensional negative-branch near-critical mechanism.** The LeBrun mixed estimate, Chern--Gauss--Bonnet bookkeeping, explicit gap density, and Derdzinski/projector local contradiction remain valid. They exclude a fixed-scale harmonic-chart limit carrying small mean calibrated defect.

2. **Normal-cover mean theorem.** `notes/step9_general_cover_transport.md` is valid. For any buffered normal cover under a Ricci lower bound, local means of nonnegative densities transfer upstairs with a universal Bishop--Gromov constant. This removes sheet multiplicity as a separate escape mechanism.

3. **Naber--Zhang interface.** Source reading of `Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md` supports the conditional theorem: residual dimension <=3, maximal fibered nilpotency rank, and a uniform model noncollapsing radius imply harmonic radius on the local universal cover (Proposition 6.4, lines 1437--1454), through Theorem 5.1 (lines 914--925 and 1366--1370). This is exactly the fixed-scale accessible-cover package needed for the local contradiction.

4. **Corrected energy bookkeeping.** `scripts/step10_energy_budget_lebrun.py` verifies that the correct signature formula is
   12 pi^2 tau(M)=int(|W+|^2-|W-|^2), tau(M)=tau(X)-k,
   so int|W-|^2=int|W+|^2-12 pi^2(tau(X)-k), not int|W+|^2+32 pi^2 k. A normalized O(A) full-curvature energy bound requires chi(X)/A, k/A, and J/A bounded.

5. **Positive-branch four-dimensional finite-type dichotomy.** S0910A02's use of Cheeger--Naber Theorem 1.12 is valid in dimension four when positive pinching supplies diameter and a lower total-volume bound supplies unit-ball noncollapse by Bishop--Gromov. For #_k(S^2 x S^2), this gives a tail dichotomy: either delta_+ stays away from zero or any near-positive-Einstein sequence collapses in total volume. This is useful but not an Einstein-existence theorem.

## Withdrawn or narrowed statements

- `notes/step9_regular_collapse_exclusion.md` is superseded. Its strongest conclusions are false: all regular collapse is not excluded; the nil^3 sign was wrong; local interval/cusp models exist.
- Abelian orbit-volume equations do not rule out local interval models. Lott's Proposition 2.10 uses a parabolic base and bounded orbit-volume function; circle-base exclusion uses periodic integration; other endpoint or flux conclusions need their own hypotheses.
- The complex-hyperbolic or real-hyperbolic cusp calibrations do not prove a surviving counterexample mechanism. A fixed-scale noncollapsed cover of such a region would fall under the cover-mean/Derdzinski contradiction; only failure of fixed-scale accessibility remains open.
- Small L-infinity Ricci defect is not a pointwise Weyl or curvature-sup estimate. Harmonic coordinates under bounded Ricci give finite W^{2,p} control, not W^{2,∞}. The Weyl divergence identity involves derivatives of Schouten and should be used through integrated identities unless additional regularity is created.
- Cheeger--Naber Theorem 1.12 is four-dimensional, not an all-dimensional finite-diffeomorphism theorem. Theorem 1.4 is all-dimensional codimension-four regularity for noncollapsed bounded-Ricci limits, but it does not itself produce Einstein metrics on the original manifolds.

## Current central problem

For the LeBrun negative near-boundary route, the hard question is now:

**Can a positive volume proportion of a hypothetical near-critical sequence fail all fixed-scale accessible-cover hypotheses?**

A point is accessible if, at a fixed physical scale, it has a normal cover of a buffered domain with noncollapsed harmonic-chart control. Naber--Zhang gives this under residual dimension <=3, maximal fibered nilpotency rank, and a uniform lower model noncollapsing radius. The cover-mean theorem then transports small calibrated mean defect to the cover, and the local contradiction eliminates such points in positive volume proportion.

Thus a surviving sequence must have almost all volume in one or more of:

1. rank-drop collapse;
2. degenerating residual model scale (`r_c -> 0`);
3. residual four-dimensional cores where the Naber--Zhang residual-dimension condition fails;
4. singular-fiber or boundary regions not represented by a buffered normal cover;
5. unwrapping available only at radii `r_i -> 0`, where the Einstein constant rescales away and the calibrated negative-Einstein spectrum no longer persists;
6. curvature/topology concentration regions that may dominate local geometry even if their global measure is controlled.

## Best next mathematical work

### A. Build the accessible-cover theorem cleanly

Agent2 should turn the Step 10 note into a precise proposition with hypotheses and proof, not as a final result but as a reusable lemma. It should explicitly cite Naber--Zhang Proposition 6.4 and Step 9 normal-cover mean theorem, and state exactly what is ruled out: positive volume proportion of fixed-scale NZ-modeled maximal-rank collapsed points in LeBrun near-critical sequences.

### B. Investigate failure modes rather than model-classify exact orbits

Agent3 or Agent2 should study whether the LeBrun near-critical energy/topology forces the NZ hypotheses on a positive volume proportion. Useful subquestions:

- From the normalized O(A) full-curvature energy, can one show that many fixed-radius balls have bounded scale-invariant mean curvature energy after unwrapping?
- Does bounded mean energy plus bounded Ricci imply a weak harmonic-radius or NZ-model condition on a positive volume set, perhaps after passing to a normal cover?
- Can rank-drop occupy positive volume while carrying the large Euler/signature/topology budget of the blow-ups?
- If `r_c -> 0` on most points, what lower-dimensional model degeneration is occurring, and does it force curvature concentration detectable by the normalized energy or calibrated defect density?
- Do singular-fiber regions necessarily have small volume proportion unless topology/energy concentrates there?

### C. Keep positive branch precise but active

S0910A02's four-dimensional finite-type theorem should be used as calibration for P_4^+. The open bridge is not only total noncollapse; even noncollapsed orbifold limits need an approximate-to-exact obstruction projection or desingularization argument before Einstein existence on the original smooth manifold follows. Collapse with large Weyl energy in the Sha--Yang family remains a serious construction/obstruction problem.

### D. Source work still needed

- Read more of Naber--Zhang examples 3.3--3.5 and Section 6.3/6.4 to understand sharpness: especially how maximal rank can hold while GH control/model scale fails.
- Retrieve or read the precise Cheeger--Fukaya--Gromov/Lott hypotheses if exact adapted orbit-volume models are used again.
- For positive branch, inspect the noncollapsed orbifold/desingularization projection bridge sources before treating the bridge as closed.

## Handoff recommendation

Route to Agent2 in Explore or Execute? The next task is mostly mathematical construction from sources, but it still depends on clarifying hypotheses and failure modes. Use **Agent2 / Explore** if the goal is a clean theorem statement plus proof of the accessible-cover exclusion and a map of remaining failure modes. Move to Execute only once a specific calculation or formal proof file is being built. Agent1 should keep broader scope visible: none of this resolves all dimensions or even P_4^- yet.

## TTCS refinement added after independent verification

The independent verification `trace/ttcs/results/step10_ttcs01_verifier1_integration.md` supports the Step 10 route but sharpens several technical points that the next agent should preserve:

- State the normal-cover mean theorem with a **precompact buffer**, e.g. `closure(B_{3r}^{\widehat U}(\hat p))` compactly contained in the covering domain, or by taking a cover over a larger base ball and using only an interior core. Use a Borel section/enumeration of the countable deck group; do not rely on smooth nearest-lift tie sets. The numerical hyperbolic constants in the old note are irrelevant.
- State the accessible-cover theorem for arbitrary **measurable subsets** satisfying the Naber--Zhang package, and choose constants in order: lower model scale `r_*`, Naber--Zhang `delta_*` and harmonic radius `h_*`, then `0<a<min(1/4,h_*/4)`.
- In the harmonic-coordinate passage, choose finite `p>4`. Bounded Ricci gives `C^{1,alpha} cap W^{2,p}` control; the near-Einstein equation gives strong `W^{2,p}` convergence after shrinking. Curvature and the `W+` eigenvalues pass in `L^1` because eigenvalues of symmetric matrices are Lipschitz.
- Lott's formula also assumes the determinant line holonomy condition needed for `sqrt(det G)` to be globally defined. Proposition 2.10 needs parabolicity and bounded orbit volume.
- The nil^3 circle-base exclusion should not be attributed to `v''=(3-mu)v` alone. The corrected equation has indefinite sign. A circle contradiction needs an additional periodic identity such as the one involving `q=H1+H2-H3`: `(vq)'=(1-3mu)v`, which together with `int(3-mu)v=0` contradicts `int(1-3mu)v=0`. If this model theorem is used again, derive and verify the second identity explicitly.
- The four-dimensional energy expression uses the curvature-operator norm `|Rcal|^2=|W+|^2+|W-|^2+|E|^2/2+s^2/24`; for the usual `(0,4)` curvature norm all coefficients change by the convention factor. The normalized `O(A)` energy budget needs `chi(X_i)/A_i` and `k_i/A_i` controlled, plus `J_i/A_i -> 0` from Ricci defect and volume control.
- The accessible-cover route remains a theorem about near-critical LeBrun sequences, not a proof or disproof of the original all-dimensional interval statement. A counterexample to Yau 26 must still defeat every candidate interval/sign branch, while a proof of one normalized sign branch would suffice for the corresponding dimension.
