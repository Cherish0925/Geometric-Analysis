# Step 71: localized collapse quantum audit and Lean statement-scope probe

Session `S0910A02`. Agent3 / Actuator. Phase Execute.

This step follows the Step-70 handoff plus the Strategist correction. It does not prove or refute Yau--26. It performs two executable audits that change the research state:

1. the collapse front for the spin balanced row `#_3(S^2\times S^2)` must use localized Chern--Gauss--Bonnet/Weyl quantum accounting, not total rod energy; and
2. the current Lean/Mathlib environment cannot natively state the Ricci-pinching hypothesis with actual Ricci curvature, although it has Riemannian metric infrastructure.

A third conceptual correction is recorded: the noncollapsed A1 arc should be seen as a conditional proof route for the noncollapsed half of `P_4^+`, not merely as a spent local-construction plateau.

---

## 1. Noncollapsed positive branch: proof-route skeleton now visible

Suppose the positive branch `P_4^+` fails in the noncollapsed regime. Then there is a sequence `(M_i,g_i)` with
\[
\|\operatorname{Ric}_{g_i}-g_i\|_{op}\le \delta_i\to0,
\qquad \operatorname{Vol}(M_i,g_i)\ge v>0,
\]
where the smooth `M_i` carry no Einstein metric of any sign.

The session already has the needed compactness outline (Step 9/58): after passing to a subsequence, Cheeger--Naber gives an Einstein orbifold limit with isolated singularities in dimension four. If no bubbling occurs, smooth Cheeger--Gromov recovery gives an Einstein metric on the stabilized diffeotype, contradicting the no-Einstein assumption. Thus a genuine counterexample sequence must bubble.

The bubbling configuration is a Biquard--Ozuch datum: an Einstein orbifold plus ALE bubbles whose smooth resolution is the original diffeotype. The proof-side reading is:

- if tight `C^0` Ricci pinching forces the full obstruction tower to vanish at that datum, and
- if the relevant Ozuch existence/transversality theorem applies after slicing the four scalar full-gauged kernel modes, then
- the desingularization carries an exact Einstein metric, contradicting the assumed failure.

So the noncollapsed positive proof route has three named gaps:

1. **Higher-obstruction necessity.** Step 70 states the first-obstruction flux dichotomy. A full proof needs mode-by-mode necessity for the higher obstruction tower, with the correct indicial roots and endpoint/gauge error control.
2. **Ozuch existence hypotheses.** Need transversality/nondegeneracy and explicit treatment of the four non-TT scalar/gauge modes found in Steps 68--69.
3. **Exponential branch.** Step 63 shows the branch `t \lesssim e^{-c/\delta}` is a real two-jet channel. Under the proof reading, the valuable target is to prove that this two-jet drift cannot be globally realized on a closed smooth manifold under the required matching/axis/smoothness/topological closure conditions, not to use it as a refutation construction.

This revalues the mixed-row Ozuch computation: it is a test case for gap (2), not a route that can by itself decide `P_4^+`.

---

## 2. Corrected collapse ledger for the spin balanced row

The Step-70 handoff contained a numerical slip inherited from prior memory: it said the pinned Weyl energy for `#_3(S^2\times S^2)` was `24\pi^2`. The correct topology is
\[
\chi(#_3(S^2\times S^2))=2+2\cdot3=8,
\qquad \tau=0.
\]
For a collapsing positive-pinched sequence with `Ric \approx g` and `Vol \to0`, Chern--Gauss--Bonnet gives
\[
8\pi^2\chi
=\int_M \left(|W|^2+\frac{s^2}{24}-\frac{|E|^2}{2}\right)d\mu.
\]
Since `s\approx4`, `E\to0`, and `Vol\to0`, the scalar and trace-free Ricci integrals vanish. Thus
\[
\int |W|^2 \to 8\pi^2\chi = 64\pi^2.
\]
The signature formula gives
\[
\int |W^+|^2-\int |W^-|^2 = 12\pi^2\tau=0,
\]
so each chiral half must carry
\[
\int |W^+|^2\to 32\pi^2,
\qquad
\int |W^-|^2\to 32\pi^2,
\]
i.e. **4 units of `8\pi^2` in each half**.

The sharper point is locality: on any region whose full curvature stays bounded, the CGB integrand is `O(1)` while the volume goes to zero, hence that region contributes `o(1)`. Therefore all of `\chi=8` must be carried by curvature-concentration regions. This is different from the noncollapsed orbifold case, where the base orbifold carries most of the topological mass.

---

## 3. ALE/ALF quantum calculation

I wrote and ran

- `workspace/scripts/step71_collapse_quantum_diophantine.py`
  -> `workspace/data/step71_collapse_quantum_diophantine.json`.

Source anchor for the curvature quantum formulas:

- `Knowledge/objects/papers/Curvature-cones-and-characteristic-numbers--8d08033cf0c7--47e3a363f7a4/object.md`, lines 400--417.

For a Ricci-flat ALE concentration region asymptotic to `S^3/\Gamma`, CGB with boundary gives
\[
Q_{ALE}:=\frac{1}{8\pi^2}\int |Rm|^2 = \chi(X)-\frac1{|\Gamma|}.
\]
For an ALF gravitational instanton with the usual finite-topology/decay assumptions, the boundary term tends to zero and
\[
Q_{ALF}=\chi(X).
\]

For Kronheimer ADE ALE spaces, `\chi=rank+1`. The script enumerates all ADE quanta with `Q\le8` and exact multiset sums.

### Total quantum `Q=8`

There is exactly one all-ADE total solution:
\[
3\times A_2:
\quad 3\left(3-\frac13\right)=8.
\]
This corrects the naive first thought that the integrality condition by itself rules out all-ADE concentration. The total CGB mass alone still has one ADE solution.

### Chiral half quantum `Q=4`

Because `\tau=0`, a half-conformally-flat concentration model must split the mass into `Q=4` in each Weyl half. The script finds:

\[
\textbf{no ADE multiset sums to }4.
\]

Thus the only all-ADE total solution `3A_2` cannot be split into two chiral groups each carrying `4` units. If all concentration regions are hyperkähler/Kronheimer ALE spaces whose curvature sits in one Weyl half after orientation choice, then the spin balanced row cannot collapse by pure ADE ALE concentration.

### Allowing ALF integer quanta

ALF quanta are integers. For one chiral half to have total quantum `4`, the ADE ALE part must have integer total quantum. The script finds only:

1. no ALE contribution plus `4` ALF units; or
2. two `A_1` ALE bubbles with quantum `3`, plus `1` ALF unit.

So localized CGB gives a real compatibility gate:

- pure all-ADE half-flat concentration is chiral-impossible;
- viable half-flat models must involve ALF/integer-quantum regions, or some non-half-flat/non-ADE Ricci-flat concentration where the chiral split is not atomic in this way.

This is **not** yet a collapse contradiction. It identifies the next proof obligation: determine which concentration geometries a `C^0` positive-Ricci-pinched collapse on the `#_3(S^2\times S^2)` row can actually have, including ALF/ALG/Ooguri--Vafa transition regions and their chirality/topological attachment.

---

## 4. Relation to prior collapse records

This calculation sharpens Step 58. Step 58 was right that total Weyl energy is not enough: the rod budget can saturate the total CGB mass. The new object is the **localized quantum plus chiral split**.

It also fits Lott's almost-Ricci-flat collapse examples (Knowledge lines 240--289 of `The-collapsing-geometry-of-almost-Ricci-flat-4-manifolds`): collapsed Ricci-flat K3 limits can bubble ALF dihedral or Taub--NUT/Ooguri--Vafa regions. Hence ALF is not optional decoration; it is the expected way a genuinely collapsed four-dimensional sequence evades pure ALE quantization.

For the Yau--26 positive collapse front, the high-value theorem is therefore not a rod total-energy inequality. It is a classification/forcing statement of the form:

> Under `Ric \approx g`, `Vol\to0`, and the spin balanced-row topology, every curvature concentration is of allowed type X with chiral/integer quanta satisfying Y; then either the allowed patterns are topologically incompatible with `#_3(S^2\times S^2)`, or they imply an Einstein-compatible collapse/existence mechanism.

The current computation only supplies the arithmetic gate Y for the half-flat ALE/ALF cases.

---

## 5. Lean statement-scope probe

The user goal ultimately requires a Lean 4 proof of the full proposition, after proposition-consistency and axiom/dependency audit. Step 70 produced useful arithmetic and logical kernels, but its `Step70LowDimAndStructure.lean` declares uniformization/Hamilton/Ye as axioms; that is a documented reduction, not a completed formalization of the low-dimensional cases.

I cheaply probed whether current Mathlib can state the actual Ricci-pinching hypothesis.

Files:

- `workspace/proofs/Step71RicciPinchingStatementProbe.lean`
- `workspace/proofs/Step71RicciOnlySearch.lean`

Commands:

```bash
Skills/qiushi-lean-proof/scripts/lean_check \
  Sessions/S0910A02/workspace/proofs/Step71RicciPinchingStatementProbe.lean

Skills/qiushi-lean-proof/scripts/lean_check \
  Sessions/S0910A02/workspace/proofs/Step71RicciOnlySearch.lean
```

Results:

- The naive statement probe failed on unknown identifiers including `RiemannianMetric`, `ricci`, `Ricci`, `riemannCurvature`, `sectionalCurvature`, and `scalarCurvature`.
- A second environment-search file compiled and printed that imported Mathlib has Riemannian infrastructure such as `IsRiemannianManifold`, `Bundle.ContMDiffRiemannianMetric`, and `ModelWithCorners`, but **zero constants containing**:
  `Ricci`, `ricci`, `RiemannCurvature`, `riemannCurvature`, `sectionalCurvature`, `scalarCurvature`, `LeviCivita`, `Christoffel`, or `PseudoRiemannian`.

Conclusion: in the current locked Lean environment, the exact proposition cannot yet be faithfully stated using native Mathlib Ricci curvature objects. Any full formalization will require either:

1. a new/extended Riemannian curvature development defining Levi-Civita connection, Riemann curvature, Ricci tensor, quadratic-form inequalities, Einstein metric, compact/closed smooth manifold assumptions, and smooth metric quantification; or
2. a deliberately synthetic axiomatized interface that records the proposition's quantifiers and predicates but is clearly marked as an interface, not a proof of the geometric content.

This is a scoping fact, not a failure of the existing Lean arithmetic harvest. It prevents us from mistaking clean audits of `1/8`, `1/6`, or sign-branch logic for a formalization of Yau--26 itself.

---

## 6. Peer context

Peer message #493 reports that A01 completed two standalone proof modules for the restricted Ishida--LeBrun negative branch: selected support and real-exponent defect Moser, with TTCS-repaired issues. I did not audit those modules in this step. They may be the strongest restricted negative theorem record and should receive a connected Agent4/Agent1 review if the project shifts to the negative branch, but they do not by themselves resolve the sign-unrestricted Yau--26 target.

---

## 7. Current status after this step

- Full Yau--26 remains unresolved in all dimensions `n\ge4`.
- The noncollapsed positive branch has a newly explicit proof-route skeleton with three named gaps: higher-obstruction necessity, Ozuch transversality/kernel slicing, and global exclusion or absorption of the exponential neck branch.
- The collapse branch on the spin balanced row now has the corrected localized energy ledger: total `64\pi^2`, chiral `32\pi^2` each, with pure ADE half-flat concentration chiral-impossible but ALF/integer-quantum channels still open.
- Native Mathlib cannot currently state the Ricci-pinching proposition faithfully; future formalization must first build or axiomatize the missing curvature layer.


---

## 8. TTCS verification assimilation

A grounded TTCS verifier read this note, the script/data, Step 58/64 records, the Atiyah--LeBrun curvature-quantum source, Lott's collapse source, and the Lean probe files. The integration is saved at

- `Sessions/S0910A02/trace/ttcs/results/step71_ttcs01_verifier1_integration.md`

with complete branches at `step71_ttcs01_sub1_verifier.md` and `step71_ttcs01_sub2_verifier.md`.

What I accept from the verification:

1. **CGB/chiral ledger confirmed, with a stronger wording.** For `\tau=0`,
   \[
   \int |W^+|^2=\int |W^-|^2
   \]
   holds for each metric, not only in the limit. Since the scalar/trace-free Ricci term is `O(Vol)` under `Ric\approx g`, both halves tend to `32\pi^2`.
2. **Bounded-curvature collapse is already excluded on this row.** If `|Rm|` were uniformly bounded globally while `Vol\to0`, Cheeger--Fukaya--Gromov would force `\chi=0`; locally, any uniformly bounded-curvature region contributes `o(1)` to CGB. The open issue is not whether curvature concentrates, but whether concentration has a finite complete-instanton decomposition with no neck/diffuse loss.
3. **ADE enumeration is verified.** The total quantum `8` has exactly `3A_2`; one chiral half `4` has no ADE solution. With standard half-flat ALF integer quanta, each chiral half can only be `(ADE,ALF)=(0,4)` or `(2A_1,1)` in normalized units. The phrase “4 ALF units” means total ALF quantum 4, not necessarily four separate bubbles.
4. **The arithmetic gate is narrower than a collapse obstruction.** It assumes finite energy identity, complete smooth Ricci-flat half-conformally-flat models, Kronheimer SU(2) ADE ALE for the ALE pieces, standard ALF decay/topology for ALF pieces, no neck/transition/diffuse energy, and a definite assignment of each model to the mother orientation's `W^+` or `W^-`. Non-half-flat Ricci-flat bubbles, non-SU(2) or quotient ALE ends, APS/signature boundary corrections, ALG/ALH regions, and Ooguri--Vafa-type transition curvature are not covered by the enumeration.
5. **Lean scoping is confirmed.** `Step71Yau26SyntheticStatement.lean` is only a synthetic quantifier shell. Its audited theorem proves the unfolding of an abstract predicate statement, not Ricci geometry. The environment search justifies the practical conclusion that native Mathlib Ricci curvature is not currently available in the locked proof environment.

The strongest valid collapse conclusion after independent checking is therefore:

> For any hypothetical `Ric\approx g`, `Vol\to0` sequence on the `\chi=8,\tau=0` row, each Weyl chirality must carry exactly four normalized units of concentration. If all concentration energy is losslessly carried by definite-chirality Kronheimer ADE ALE bubbles, the split is impossible; if standard half-flat ALF integer quanta are also allowed, each chirality's ADE part is either empty or exactly `2A_1`. Turning this into a Yau--26 collapse theorem requires a new compactness/classification/energy-identity result under only `C^0` Ricci pinching.
