# Step 39: Known-answer calibration and corrected compact-period defect formulation

Session S0910A02. Agent3/Actuator. Phase Execute.

## 0. Scope and target fidelity

This step does **not** prove or refute Yau's Problem 26. It repairs the collapsed positive toric subroute before any new `m=6` compact-period computation is trusted. The full target remains the dimension-only Ricci-pinching implication for all closed connected smooth manifolds, with no symmetry, noncollapse, sign, or closeness assumption on the output Einstein metric.

The toric work here is a four-dimensional, positive-sign, symmetry-restricted laboratory. Even a complete obstruction to exact toric Einstein metrics on the alternating `#_k(S^2\times S^2)` polygons would not by itself settle the pinched, non-symmetric, all-dimensional proposition. Conversely, closing a toric exact-Einstein alternating family would show Einstein existence for that toric topology rather than directly refuting Yau-26.

## 1. Why Step 38 needed calibration

The Step-38 noncompact Weyl-chain algebra remains useful in its own scope: finite alternating rod chains with two semi-infinite ends exhibit exact period drift, and the positive-mass argument explains why period matching is structurally impossible for such asymptotically Euclidean finite chains. But the new strategist note correctly points out that this is **not yet** the compact-polygon defect.

The compact problem has known exact positive toric Einstein answers that any defect functional must reproduce:

- `S^2\times S^2` product: rectangle, two same-circle pairs, zero defect.
- Page metric on `CP^2#\overline{CP}^2` (`F_1`): quadrilateral with one same-circle pair, zero defect, `K_B` not identically zero.
- Chen--LeBrun--Weber metric on `CP^2#2\overline{CP}^2`: pentagon with two independent same-circle pairs, zero defect.
- toric Kähler--Einstein metric on `CP^2#3\overline{CP}^2`: hexagon with three same-circle pairs, zero defect.

Therefore same-circle multiplicity is not an obstruction by itself. The Step-15/17 result `mu=1 iff A=0` is a theorem for the separated Schwarzschild--de Sitter/cohomogeneity-one block with two bolts, not a theorem for arbitrary compact toric quadrilaterals. Page is the decisive cheap validation case: two nonadjacent rods collapse the same circle and close smoothly while the orbit-base curvature is sign-changing and nonzero.

## 2. Source-checked known examples

The source `Knowledge/objects/papers/Toric-Einstein-4-manifolds-with-non-negative-sectional-curvature--24d1f88fe098--1315c2a6cd67/object.md` records:

- lines 37--39: Page and Chen--LeBrun--Weber are in the Hermitian Einstein classification, and the non-Kähler examples are invariant under a biholomorphic `T^2` action;
- lines 41--42: the known positive `T^2`-invariant Einstein examples include round `S^4`, Fubini--Study `CP^2`, product `S^2\times S^2`, Page, CLW, and the toric KE metric on `CP^2#3\overline{CP}^2`;
- lines 84--87 and 130--158: toric actions give polygonal orbit spaces with primitive edge labels and smoothness conditions at edges/vertices;
- lines 181--247: exact simply connected Einstein `T^2` actions are geometrically polar and the orbit-volume function satisfies `-Delta phi = 2 Lambda phi`.

The source `Knowledge/objects/papers/On-the-spectrum-of-the-Page-and-the-Chen-LeBrun-Weber-metrics--c91c79dbc8bc--0506c0122a9c/object.md` adds:

- Page is Einstein on `CP^2#\overline{CP}^2`, has cohomogeneity one `U(2)` action, and is explicitly computable;
- CLW is Einstein on `CP^2#2\overline{CP}^2`, admits a cohomogeneity two `T^2` action, and the conformal Kähler metric is toric-Kähler;
- the Page and CLW conformal Kähler moment polytopes are respectively a trapezoid and pentagon.

These sources make Page/CLW mandatory calibration examples for any proposed compact toric period-defect invariant.

## 3. Exact fan/rod-count calibration

The script

- `workspace/scripts/step39_known_answer_period_calibration.py`

writes

- `workspace/data/step39_known_answer_period_calibration.json`.

It audits cyclic primitive labels modulo unoriented circle class (`v` and `-v` generate the same subgroup):

| example | edge count | same-circle classes | status |
|---|---:|---|---|
| `CP^2` / Fubini--Study | 3 | none repeated | exact KE |
| `S^2\times S^2` rectangle | 4 | `(1,0)` and `(0,1)`, two rods each | exact product Einstein |
| `F_1=CP^2#\overline{CP}^2` / Page | 4 | one repeated class | exact positive Einstein |
| `dP_2=CP^2#2\overline{CP}^2` / CLW | 5 | two repeated classes | exact positive Einstein |
| `dP_3=CP^2#3\overline{CP}^2` | 6 | three repeated classes, two rods each | exact toric KE |
| alternating spin hexagon candidate | 6 | two classes, **three rods each** | unknown |

This isolates the first genuinely new compact-period test: not `m=4`, and not every `m=6`, but the alternating spin hexagon with three rods in each of two circle classes. The known toric KE `dP_3` hexagon is a validation control with zero defect and must not be confused with the alternating `#_2(S^2\times S^2)` fan.

The right-angle Gauss--Bonnet values are also recorded:

\[
\int_\Sigma K_B\,dA=2\pi-\frac{m\pi}{2}.
\]

Thus `m=6` gives `-pi`, not an `A=0`/flat background. A perturbation of the alternating spin hexagon around `A=0` is not well-posed unless an exact background solution is first supplied; having such a solution would already be a positive Einstein metric on the target unknown topology.

## 4. Page explicit calibration

Using the explicit Page formula from `Knowledge/objects/papers/Toric-U-2-and-LeBrun-metrics--fb99f416c130--13e07193d27a/object.md`, lines 319--340,

\[
 g=S\bigl(A(r)dr^2+B(r)(d\psi+\cos\theta\,d\phi)^2+C(r)(d\theta^2+\sin^2\theta\,d\phi^2)\bigr),
\]

the orbit-base metric for the `T^2` generated by `\psi,\phi` is

\[
 g_B=S(A(r)dr^2+C(r)d\theta^2),\qquad r\in[0,\pi],\ \theta\in[0,\pi].
\]

The Step-39 script computes the Gaussian curvature exactly enough to verify:

- `nu = 0.2817015579087726`;
- `\int K_B dA = 7.6e-17`, matching the right-angled quadrilateral prediction `0`;
- `K_B` is **not** zero: sampled/stable range approximately `[-0.1051, 0.0716]` in this normalization;
- the two nonadjacent `r=0` and `r=pi` rods collapsing the same `(1,0)` circle have equal surface-gravity coefficient in the Euler-angle basis:
  \[
  \kappa_{r=0}=1.281701557864\ldots,
  \quad
  \kappa_{r=\pi}=1.281701557888\ldots,
  \]
  relative difference `1.9e-11`. The common value is not `1` because the Euler-angle period is not yet converted to primitive toric period; equality is the meaningful period-matching test.

This directly invalidates any compact defect rule that treats two same-circle rods or nonzero/sign-changing `K_B` as automatically obstructed. Page is a nontrivial exact toric positive Einstein quadrilateral with repeated circle class and `K_B\not\equiv0`.

## 5. What survives from the Weyl-chain computation

The finite noncompact Weyl-chain period ratios should be retained only as a model for **force/period drift with asymptotic ends**, not as compact polygon values. In particular:

- The noncompact four-finite-rod chain has exp-range `3/2`, but the compact rectangle product metric has zero defect.
- The positive-mass argument explains finite-chain mismatch because complete Ricci-flat AE with matched periods and `R^4` asymptotics would have to be flat and hence have no bolts.
- Compact polygons have no AE end; infinite periodic chains have no two semi-infinite ends and can equalize same-label rods by translation. The defect, if any, must be a compact substitute for the same force/sign phenomenon, not the finite-chain exp-range itself.

The useful conceptual remnant is: local exact or near-exact rod data do not determine global closure. Global period/surface-gravity compatibility is a real invariant. But it must be calibrated against Page, CLW, and `dP_3`.

## 6. Correct defect-vector formulation

A safe formulation is not “count same-circle rods” or “compare with finite Weyl exp-range”. It is:

1. Work on a relaxed toric boundary-value space where the reduced equations are enforced but primitive unit slopes are **not** all imposed at once.
2. For each edge `e`, compute the surface-gravity coefficient `\kappa_e` of the collapsing primitive circle in a fixed global torus lattice.
3. For each unoriented circle class `c`, define log-ratio defects
   \[
   D_{e,e'}=\log\kappa_e-\log\kappa_{e'},\qquad e,e'\in c.
   \]
   A single global rescaling of that circle can make one `\kappa` equal to `1`; all ratios in the same class are invariant.
4. Quotient the finite-dimensional or functional parameter space by the two circle rescalings and overall metric scaling before doing any count.
5. Validate that `D=0` at the exact known examples: product rectangle, Page, CLW, and toric KE `dP_3`.
6. Only then test the alternating spin hexagon and higher alternating spin polygons.

For the alternating spin pattern with `m=2k+2`, there are `k+1` rods per each of two circle classes. The first case with three rods per class is `m=6`, corresponding to the spin stress topology `#_2(S^2\times S^2)` in the session's label convention. This is analogous to Israel--Khan in the sense of three same-axis rods, but the obstruction should be a sign/force inequality, not a naive equation count.

## 7. Exact versus pinched relaxation

Smooth toric exact Einstein metrics require exact unit slopes. The Yau-26 antecedent only supplies `C^0` Ricci pinching; after reducing to a symmetric model, the reduced equations would hold only up to a defect `\delta`, and the output Einstein metric is allowed to be completely different from the input metric.

Thus a compact toric obstruction can affect Yau-26 only if it is stable with a quantitative margin:

\[
\|D\|\ge m(A)>0
\]

for all relevant relaxed exact/near-exact configurations, with residual estimates of the form

\[
\|D_\delta-D_0\|\le C\delta
\]

(or a scale-sensitive analogue). If the obstruction margin tends to zero along the collapse scale or can be absorbed by variable rod lengths/edge curvature profiles, it cannot close the pinched branch. This is the collapsed analogue of the Step 3--4 stable-integral principle and the Route-A balanced-annulus requirement.

## 8. Updated next computation

The previous handoff’s “perturb around `A=0` for the alternating `m=6` hexagon” should be dropped: the right-angle Gauss--Bonnet integral is `-pi`, and no exact `A=0` background is known. The well-posed next computation is:

1. Build a relaxed compact toric defect model whose unknowns include rod lengths, edge curvature data, and possibly a low-dimensional ansatz for the orbit-base metric or conformal factor.
2. First run it on known answers:
   - product rectangle: all same-circle ratios vanish;
   - Page: the two same-circle slopes match (already checked directly from the explicit `U(2)` formula);
   - CLW and toric KE `dP_3`: use toric Kähler/numerical extremal data if available, or use them as source-mandated zero tests until explicit orbit metrics are built.
3. Only after those tests, evaluate the alternating spin hexagon with three same-circle rods per class.
4. Track variable rod lengths. Equal-length rods are not a neutral compact model; they are a special constraint and may artificially create or hide drift. If variable lengths absorb the defect, the route shifts toward constructing a BREAK candidate rather than proving an obstruction.

The defect mechanism remains promising because the first unknown topology appears exactly when the count reaches three rods per circle class, but it is weaker and subtler than Step 38’s framing.

## 9. Files

- Script: `Sessions/S0910A02/workspace/scripts/step39_known_answer_period_calibration.py`
- Data: `Sessions/S0910A02/workspace/data/step39_known_answer_period_calibration.json`
- This note: `Sessions/S0910A02/workspace/notes/step39_known_answer_calibration_and_defect_reframe.md`
- Partially superseded note: `Sessions/S0910A02/workspace/notes/step38_period_transport_corrected_collapse.md`

No branch of Yau-26 is solved, and no Lean formalization was advanced in this step.

## 10. Addendum: topology audit separates the two hexagons

I also wrote and ran

- `workspace/scripts/step39_fan_topology_samecircle_audit.py`, producing
- `workspace/data/step39_fan_topology_samecircle_audit.json`.

This verifies using the same integral cohomology presentation as Step 18 that the known toric Kähler--Einstein `dP_3` hexagon and the alternating spin hexagon are topologically different despite both having six edges:

- `dP_3` labels `[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]` have three repeated unoriented classes, each of size two, and odd unimodular form with `(b_+,b_-)=(1,3)`, signature `-2`, i.e. `CP^2#3\overline{CP}^2` in the orientation convention.
- alternating spin labels `[(1,0),(0,1),(-1,0),(0,-1),(1,0),(0,1)]` have two repeated classes, each of size three, and an even unimodular indefinite rank-four form, consistent with `#_2(S^2\times S^2)`.

Thus the first unknown compact-period target is not “hexagon” in general; it is the spin alternating hexagon with three rods in the same circle class. The `dP_3` hexagon is a known-zero calibration control.

## 11. Addendum: energy budget correction to Step 38

The Step-38 JSON `energy_per_cell` entry claimed a Chern--Gauss--Bonnet budget `8π²(m+2)` and a universal `16π²` slack. This was a topology error for closed toric four-polygons. In the toric polygon setting, the number of vertices/edges is `χ(M)=m`. Therefore if the high-`A` model really contributes `8π²` per rod, the leading energy is `m·8π²`, exactly the `8π²χ` budget (up to trace-free-Ricci error in a pinched non-Einstein metric). Any independent positive corner/collar contribution not already included in the rod cell would overflow by order `m`. What remains open is the geometric decomposition: whether the quoted per-rod `8π²` quantum already includes the corner/collar/polar pieces. The corrected data entry is in `workspace/data/step39_known_answer_period_calibration.json` under `toric_energy_budget_correction_to_step38`.

## 12. Peer-negative-flow update

Peer message #346 from A03 reports a TTCS-verified general-`p` homogeneous defect power inequality for the negative-flow route and a corrected Moser ladder using three-factor Hölder rather than fixed-`p` two-factor absorption. I did not verify their files in this step. The report matters as possible progress for the negative branch, but it does not change the present toric calibration conclusion and still concerns a different route with downstream endpoint/global-flow obligations.
