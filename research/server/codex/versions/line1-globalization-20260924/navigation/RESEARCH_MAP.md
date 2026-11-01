# Yau26: mathematical map across all three scientific lines

This is the current navigation layer for the locally preserved research, through
the first-line realization advance of 24 September 2026. It points to proofs rather
than replacing them. The three lines organize questions; they do not prescribe
three permanent roles, one preferred construction, or a fixed paper count.

The [development account](EVOLUTION.md) explains how the ideas changed. The
[correction register](CLAIMS_AND_CORRECTIONS.md) resolves superseded claims.
The machine-readable [result catalogue](../catalog/results.json) records scope,
proof dependencies and mathematical status. In that catalogue,
`manuscript-theorem` means a statement with its argument in the preserved
manuscripts, not independent certification of correctness or global priority.

## 1. The question every line must return to

Write
\[
\delta_\sigma(g)=\|g^{-1}\operatorname{Ric}_g-\sigma I\|_{\infty,\mathrm{op}},
\qquad \sigma\in\{+1,-1\}.
\]
The adopted working question asks whether, in each dimension, at least one
dimension-only signwise threshold forces the **same closed smooth manifold**
to carry some Einstein metric. Its sign, scale, symmetry, complex structure and
distance from the input are not prescribed. In the project's notation,
\(Q_n=P_n^+\lor P_n^-\). A complete negative answer needs both branches to fail
in one dimension; their witnesses need not be the same manifold, and each
branch may use a sequence of different manifolds.

The [foundational manuscript](../mathematics/current/skill/research/20260910.tex)
and [problem/source map](../mathematics/current/skill/references/research-map.md)
retain the source history and normalization. The adopted formulation must be
compared with the primary historical statement before claiming a solution.

For four-dimensional integral work use
\[
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2\operatorname{Vol}(g)}.
\]
Then \(\mathcal E\le4\delta_\sigma^2\). Non-Ricci-flat Einstein metrics have
\(\mathcal E=0\); Ricci-flat metrics have \(\mathcal E=4\), so their exclusion
needs a separate argument. Integral approximation does not imply pointwise
approximation: the explicit dilution examples below demonstrate the difference.

## 2. Line I — quantitative obstruction and equality geometry

### 2.1 The common analytic mechanism and its actual input

The mechanism is not “a stronger numerical SW inequality” alone. An actual
weighted monopole supplies a bounded field; integral curvature estimates
control its Hessian; a globally smooth polynomial Weyl model can then test
weak Bianchi without differentiating a small Ricci error. The resulting
differential compatibility excludes some algebraically feasible near-equality
profiles and identifies others that survive.

| Result family | Mathematical scope and gain | Proof entry |
| --- | --- | --- |
| I01: exact uniform gap | Earlier monopole/Euler hypotheses give an exact Einstein gap uniformly across topology; collapse-tolerant local development and forbidden local spectrum are a separate proof route. | [Dedicated exact proof](../mathematics/current/skill/research/20260916_uniform_gap.tex) |
| I02: integral gap | Specified actual classes, positive projection budget and square control give a uniform relative integral defect gap without noncollapse, diameter, Sobolev or full-curvature bounds. | [Independent main manuscript](../mathematics/current/line1_integral_rigidity_paper.md); [original integral proof](../mathematics/current/round4_rigidity.md) |
| I03: polarized and all-sign closure | Metricwise class selection, the same class through all positive conformal weights, \(b_+=1\) chambers, handles, uniform constants and separate Ricci-flat exclusion close the classical positive-budget applications. | [Polarized proof](../mathematics/current/round13_chamber.md); [closure](../mathematics/current/lebrun_stability_closure.md); [symplectic chambers](../mathematics/current/round21_chambers.md) |
| I04: twisted gauge supply | Actual \(\mathrm{Pin}^-(2)\) input on a double cover supplies the required invariant weighted equations even when ordinary invariants vanish; a critical connected-sum family is realized. | [Twisted proof](../mathematics/current/round14_twisted_rigidity.md) |
| I05: bounded-form compatibility | A smooth bounded self-dual form with controlled Hodge-Laplacian budget selects \(t=0\) or \(-\sigma/2\) in the rank-one Weyl model. Gauge theory is one supplier, not an assumption of this analytic theorem. | [Two-form theorem](../mathematics/current/round21_analytic.md) |
| I06: actual form supply | Raw conformal monopole solvability plus curvature deficit produces a form aligned with the actual self-dual harmonic Chern representative, with simultaneous amplitude, Weyl, first- and second-order estimates. | [Composed application](../mathematics/current/line1_composed_application.md); [earlier scalar-band supply](../mathematics/current/line1_scalar_band_remainder.md) |
| I07: functional non-saturation | \(\beta=2\) is the cscK-compatible endpoint and \(\beta=8\) is the old topological calibration. Differential compatibility controls the whole finite parameter range; compactification retains the necessary endpoint decay. | [Functional pencil](../mathematics/current/line1_functional_pencil.md); [compactified pencil](../mathematics/current/line1_compactified_pencil.md) |
| I08–I09: energy and two-chirality feasibility | An optimized lower energy envelope and an independent opposite-chirality Chern–Weil upper budget yield all-metric gaps beyond the old near-\(1/3\) band. A further theorem quantitatively tightens the upper energy wall for \(1/4<h<1/3\). | [Lower envelope](../mathematics/current/line1_energy_envelope_gap.md); [two-chirality theorem](../mathematics/current/line1_two_chirality_topology.md); [upper wall](../mathematics/current/line1_compactified_pencil.md) |
| I10: Bauer–Furuta geography | The same analytic engine applies to realized sums of two or three positive-\(b_+\) symplectic blocks. An infinite gap family has vanishing ordinary SW invariants and no almost-complex structure in either orientation. | [Gauge supply and realized family](../mathematics/current/line1_bauer_furuta_geography.md) |

For the latest feasible-region result set \(T_\pm=2\chi\pm3\tau\), choose the
actual projection budget \(A\), and put
\[
h=1-T_+/A,\qquad U=3\min(T_+,T_-)/A,\qquad
F(h)=\frac{(4-\sqrt{1-3h})^2}{9}.
\]
Under the theorem's metricwise actual-class and square hypotheses,
\[
\mathcal E(g)+(U-F(h))_+\ge ch^2,\qquad 0<h<1/3.
\]
The two chiral budgets do **not** require monopole nonvanishing in both
orientations: one may use only curvature nonnegativity on the other side.
The realized examples with \(h\to19/300\) establish an actual increase of
coverage relative to the older recorded inequality. They are uniformly
separated from pointwise near-Einstein input and are not Yau26 counterexamples.

### 2.2 The allowed branch is a different mathematical problem

| Result family | What is controlled | What it does not imply |
| --- | --- | --- |
| I11: product calibration | [Constant-scalar](../mathematics/current/round15_rigidity.md) and [arbitrary-scalar](../mathematics/current/round17_integral.md) estimates control distance to a realizable hyperbolic-product curvature orbit. | A forbidden spectrum or a global product decomposition. |
| I12: multiple classes and periods | [Actual class intersections](../mathematics/current/round18_periods.md) force scalar low modes under near saturation; [period-domain properness](../mathematics/current/round20_rigidity.md) and [period inertia](../mathematics/current/line1_period_inertia.md) isolate which harmonic directions are constrained. | Compactness of metrics or all period planes from a small monopole span. |
| I13: variable and harmonic Weyl models | [Variable calibration](../mathematics/current/line1_variable_calibration.md), [negative-amplitude selection](../mathematics/current/line1_variable_negative_selection.md), [equation-supplied budget](../mathematics/current/line1_half_weyl_regularity.md), and [signed harmonic-Weyl balance](../mathematics/current/line1_signed_harmonic_weyl.md) retain amplitude, source and spectral-line data. | That arbitrary near-Einstein inputs have harmonic Weyl curvature, or that small splitting vanishes. |
| I14: exact spectral application | The exact equation bounds amplitude under relative pinching; actual class information gives additional splitting restrictions. | Classification of generic Weyl tensors or arbitrary Einstein outputs. See [the application](../mathematics/current/line1_einstein_spectral_application.md). |
| I15: aspherical no-bubbling | Nonflat ASD Ricci-flat ALE cores, including rational-ball quotients, cannot embed in a closed aspherical four-manifold. One bounded Weyl half plus the stated global Einstein data therefore controls full curvature. | A curvature estimate without those Einstein and global geometric hypotheses. |
| I16: actual diameter-only splitting gap | On the specified nonzero-shear self-gluings, exact negative Einstein metrics with \(b\le4\theta t\), \(\theta<1/\sqrt3\), and bounded diameter have a uniform positive averaged spectral splitting. | Nonexistence outside this relative pinching class, or along diameter-divergent sequences. See [I15–I16](../mathematics/current/line1_aspherical_no_bubbles.md). |

I16 supersedes the opposite-Weyl curvature assumption of the retained
[bounded-geometry precursor](../mathematics/current/line1_allowed_branch_escape.md)
for this actual aspherical family. It is stronger than an analysis of the
chosen approximating family: it concerns every exact output meeting its
conditions. Those conditions are still not automatic for every Einstein metric.

### 2.3 The new compact-regime bridge reaches exact realization

The library's [compact-regime realization manuscript](../continuation/20260923_compact_realization.md)
(I19) takes the no-ALE-core information beyond exact input. For closed
aspherical four-manifolds with bounded diameter, positive total-volume lower
bound and an \(L^q\) bound on one Weyl half, \(q>2\), a sufficiently small
**pointwise** negative Ricci defect implies a negative Einstein metric on
the same smooth manifold. The threshold depends on those geometric data.

Its proof uses Jiang–Naber to supply full curvature energy, then normalizes
harmonic radius rather than an uncontrolled curvature maximum. At a collapsing
radius the supercritical Weyl half disappears; the exact Ricci-flat limit is
an excluded ASD ALE space. Harmonic-coordinate compactness and the limiting
Einstein equation preserve the smooth type. This is a conditional
pointwise-input-to-exact-output theorem, not just another obstruction; it is
not the dimension-only Yau26 threshold. It is a new continuation manuscript,
with classical compactness inputs listed in its proof.

The [subsequent realization and rigidity synthesis](../continuation/20260923_realization_and_rigidity.md)
now adds I20–I23:

- [I20: topology](../continuation/20260923_topological_core_scope.md) weakens
  asphericity to torsion-free fundamental group and vanishing \(\pi_2\).
  Connected sums and handle additions give genuinely nonaspherical examples.
- [I21: critical chiral compactness](../continuation/20260923_critical_chiral_threshold.md)
  replaces supercritical control by small critical energy at a fixed local
  radius. The controlled half can vary from ball to ball. Any surviving
  degeneration must concentrate both halves at the same location.
- [I22: gauge-to-KE realization](../continuation/20260923_gauge_saturation_ke.md)
  derives noncollapse and half-Weyl concentration control from actual positive
  projection, bounded diameter, pointwise Ricci error and parameter-two
  saturation. Global actual forms produce a parallel form on the compact
  limit and a compatible negative KE metric on the same smooth manifold.
  No external Weyl or class-square cost is needed.
- [I23: spectral no-bubbling and exact modes](../continuation/20260923_allowed_mode_rigidity.md)
  works for exact Einstein input with small averaged upper-eigenvalue
  splitting, without relative pointwise pinching. It yields exact local
  product rigidity on products of curves and removes the relative-pinching
  condition from I16. General KE mode selection retains its local-moduli
  integrability hypothesis.

There is a genuine obstruction to removing diameter from I22: the actual
C03 shear metrics have both \(\delta_-\to0\) and \(\mathfrak D_2/V\to0\),
but G03 excludes every Kähler structure. Section 7.2 of I22 derives the
explicit saturation bound and proves the necessary diameter escape.
This connects all three original lines without deciding arbitrary
non-Kähler Einstein existence on those manifolds.

### 2.4 General existence no longer requires prescribed saturation in the compact regime

The [24 September entry](../continuation/20260924_global_realization.md)
separates the task of producing an Einstein metric from identifying stronger
geometry on it. A KE output already completes existence on its covered inputs.

- [I24](../continuation/20260924_ale_boundary_compatibility.md) uses the
  stronger existing Zhang/Bamler–Chen ALE nonembedding theorem and a finite-cover
  lift. Under \(\pi_2=0\), bounded diameter and positive volume lower bound,
  pointwise approximation alone gives same-smooth-type Einstein existence for
  **either sign**. No Weyl, saturation or torsion-free \(\pi_1\) assumption
  remains. Positive Ricci supplies diameter by Myers; a negative-side actual
  positive projection supplies volume. The earlier mixed-chirality bubble
  alternative is resolved in this topology.
- [I25](../continuation/20260924_bilateral_realization.md) gives exact bidisk
  realization from two actual saturation inputs with diameter control, without
  any homotopy restriction. Its two global parallel forms identify the metric;
  local product geometry is not a globally marked direct product.
- [I26](../continuation/20260924_chern_boundary_realization.md) assumes
  \(A=T_+=3T_->0\) and one actual projection \(p\ge A\). The numerical
  equality itself forces \(\mathfrak D_2/V\le72\delta_-^2\) and small
  opposite Weyl energy. Bounded diameter and pointwise approximation yield
  complex-hyperbolic geometry on the same smooth type, with no separate
  saturation or homotopy hypothesis.
- [I27](../continuation/20260924_local_to_global_scope.md) obtains local
  harmonic radius from \(\pi_2=0\), bounded Ricci and unit-ball noncollapse
  without diameter. A separately assumed full tensor spectral gap, Ricci
  regularity and small unnormalized mixed residual then permit classical
  nonlinear Einstein repair. Local regularity does not supply that inverse.

These are explicit compositions with credited classical results, not an ALE
classification or an unrestricted Yau26 dichotomy. On \(\pi_2=0\), possible
positive counterexample inputs must collapse in total volume; possible negative
inputs with a uniform actual positive budget must escape in diameter.

### 2.5 Equality and sharpness controls belong inside the theory

The [Kähler comparison](../mathematics/current/line1_kahler_energy.md) keeps
cscK non-Einstein products in the full equality set and identifies the primitive
Chern component missed by the scalar–Weyl defect. The
[energy-selection theorem](../mathematics/current/line1_energy_selection.md) and
[non-Kähler bridges](../mathematics/current/line1_non_kahler_bridge.md) distinguish
absolute Ricci-energy minimization from relative Einstein approximation.
The [Yamabe test](../mathematics/current/line1_yamabe_endpoint.md) proves what
conformal normalization preserves and gives an actual failure of pointwise
Ricci preservation. The [volume-dilution example](../mathematics/current/round18_integral_limits.md)
rules out a topology-free integral replacement for Yau26.

Not every additional invariant supplies independent information. The
[all-class budget ceiling](../mathematics/current/round19_global_gap.md) limits
the hyperbolic-cover surgery strategy, while the
[rank-one entropy comparison](../mathematics/current/line1_rank_one_entropy_scope.md)
shows that ordinary degree-to-rank-one bounds are dominated by the scalar
monopole budget throughout the specified classical complex-base family.
Neither excludes all entropy, representation-volume or gauge-theoretic routes.

## 3. Line II — actual pointwise input and exact realization

The following mechanisms must remain distinct. Their topologies, degeneration
scales, residuals and correction spaces are not interchangeable.

| Construction or realization | Mechanism and current endpoint | Proof entry |
| --- | --- | --- |
| C01: marked \(A_1\) resolution | Correct the EH core, put core and exterior in a common gauge, interpolate the quadratic Weyl mismatch logarithmically, and control all three regions to obtain \(\delta_\sigma\le C/|\log a|\). | [Foundational construction](../mathematics/current/skill/research/20260916_construction.tex), `thm:A1`, `sec:scalechoice`; [long derivations](../mathematics/current/skill/research/20260912.tex), `FND:A1construction` |
| C02: fixed \(E_D\) bundle | Long base collars slowly interpolate a fixed Dehn twist; double collars and three scalar corrections reduce the full Ricci residual. | [Construction paper](../mathematics/current/skill/research/20260916_construction.tex), `sec:ED-object` through `sec:ED-inverse` |
| C03: closed integer-shear assemblies | Long collars absorb mapping-class change, and separate collapsing throats absorb integral shear. Fixed gluing yields \(O(|\log\ell|^{-1}+\ell)\) pointwise defect on a fixed closed manifold. | [Closed construction](../mathematics/current/round11_closed_gluing.md); [actual topology](../mathematics/current/round11_graph_topology.md) |
| C04: complete exact charged model | A nonlinear Einstein family integrates the specified double-cylinder Jacobi directions with retained charge and end response. | [Complete model](../mathematics/current/round3_construction.md); [nonlinear charge](../mathematics/current/round4_construction.md) |
| C05: \(E_D\) repair exclusion | Whole-fibre receivers and weighted kernel/complement control exclude every tensor correction in a linear-size \(C^2\) ball, with cubic residual lower order. | [Weighted inverse](../mathematics/current/round6_weighted_inverse.md); [neighbourhood theorem](../mathematics/current/round6_construction.md) |
| C06: optimized pure shear | The Maxwell profile gives \(O(\ell^2)\) pointwise defect; scalar correction, exact volume excess and full-tensor receiver give a shrinking but symmetry-free repair barrier. | [Maxwell profile](../mathematics/current/round14_shear.md); [scalar correction](../mathematics/current/round14_global.md); [all-mode barrier](../mathematics/current/round14_repair_radius.md) |
| C07: full matching, not just one receiver | Actual neck and exterior responses, integral rank-two and Schwarz-P rank-three balance, and Maxwell-compatible tests identify compatible data and the remaining waist/end forcing. | [Boundary response](../mathematics/current/round15_boundary_response.md); [exterior](../mathematics/current/round15_global.md); [integral balance](../mathematics/current/round15_shear_balance.md); [minimal-surface data](../mathematics/current/round16_minimal_balance.md); [end response](../mathematics/current/round16_construction.md) |
| C08: complete product and twisted operators | The dangerous channels are entire Teichmüller-valued function spaces. The complement has uniform Hilbert-space control; finite-monodromy quotients admit a full local classification of nearby exact Einstein metrics at each fixed geometry. | [Product decomposition](../mathematics/current/round17_product_operator.md); [finite-monodromy realization](../mathematics/current/round18_twisted_operator.md) |
| C09: a genuinely different bundle target | A faithful Torelli bundle has signature zero but does not factor through a free group after finite base cover. An adapted-submersion defect bound measures nonzero signature; no general metric theorem for the new target is claimed. | [Scope and actual target](../mathematics/current/round20_construction.md) |

The product-complement bound is not a uniform maximum-norm nonlinear inverse
on arbitrary glued manifolds. Retained slow channels may be infinite-dimensional;
removing a few exact kernels is insufficient. A Schur complement retains
feedback rather than eliminating the missing equation. The
[September construction paper](../mathematics/current/skill/research/20260921_construction.tex)
also retains the a posteriori Newton framework: actual residual, inverse error,
nonlinear constant, gauge removal and metric-positivity radius must close together.

### Positive resolutions and algebraic alternatives are not secondary copies

The marked two-pole \(A_1\) constructions distinguish
\(S^2\times S^2\) from \(\mathbb{CP}^2\#\mathbb{CP}^2\) by actual equivariant
gluing, not just by the intersection form. Both-sign normalized GH separation
concerns approximation to a specified orbifold, not all Einstein existence.
See the [construction text](../mathematics/current/skill/research/20260916_construction.tex),
`sec:two-pole-fillings`, `lem:hyperbolic-A1`, `cor:both-sign-GH`.

Higher ADE, type-T and Wahl extensions retain their own cokernel, marking,
orientation and analytic-extension requirements. The
[marked ADE comparison](../mathematics/current/round19_positive_bridge.md)
and [smooth-structure comparison](../mathematics/current/round20_global.md)
prevent an \(A_1\) statement from being promoted to an unrestricted all-rank
construction. Multi-node spectral coefficients, source cones, self-interaction,
complement feedback and infinite tails are retained in the earlier construction
paper, not certified by finite matrix output.

## 4. Line III — all possible outputs on the same smooth object

| Actual object | Established content in the manuscripts | Exact question still open here |
| --- | --- | --- |
| Fixed \(E_D\) | Sharp scalar/Ricci/full-curvature variational values, specified nonattainment, general Einstein volume and spectral restrictions, local and conformal repair exclusions. | An unrestricted negative Einstein metric in another region of metric space; full-curvature minimum attainment. |
| Nonzero-shear self-gluings | Asphericity, no Kähler finite cover, complete ordinary basic first-Chern sets in both orientations, sharp variational values, and no local Killing germ for any Einstein output. | A completely nonsymmetric negative Einstein metric. |
| Exact outputs near the shear volume lower endpoint | Componentwise normalized volume rigidity; near-endpoint curvature control, product propagation, and irreducible Hilbert modular core exclusion. | Reducible degeneration, very thin/distant regions and exact metrics away from the volume endpoint. |
| Relative-spectrally-pinched shear outputs | The latest aspherical no-bubbling theorem rules out the curvature-concentration escape; spectral collapse now forces diameter divergence. | Diameter escape and outputs outside the spectral class. |
| Marked \(\mathbb{CP}^2\#\mathbb{CP}^2\) | Every normalized positive Einstein output has volume below \(4\pi^2/9\), separated from the constructed volume \(4\pi^2/3\); all-sign local conformally-Kähler/product restrictions and Weyl discriminant constraints. | Smaller-volume positive outputs, generic-spectrum outputs and the retained negative self-dual possibility. |
| Standard positive product resolutions | Some standard sums are not complex or symplectic, even though homeomorphic smooth structures carry negative KE metrics. | Einstein existence on the exact standard smooth type; a homeomorphism does not transfer the metric. |
| BCGP and seven-line Campedelli objects | Separate actual smoothing arguments produce negative KE metrics on the specified underlying smooth manifolds. | Their existence cannot be transferred to different fillings with the same numerical invariants. |
| Pure-hyperbolic-block graph manifolds and hyperbolic surgeries | Existing all-sign obstructions, necessary small-defect volume/Weyl budgets, and limits of proposed connectors. | Actual pointwise-small closed input on these already obstructed smooth types. |
| Faithful Torelli target | Actual group-theoretic bundle, topology and adapted-metric signature budget. | Pointwise near-Einstein input, alternative decomposition, and unrestricted exact output. |

Proof routes for the first four rows:
[global variational text](../mathematics/current/skill/research/20260916_global.tex),
`sec:bundle-values`; [virtual Kähler obstruction](../mathematics/current/round11_kahler.md);
[shear variational theory](../mathematics/current/round11_variational.md);
[ordinary basic sets](../mathematics/current/round12_global.md);
[all-output symmetry](../mathematics/current/round12_symmetry.md);
[componentwise repair restriction](../mathematics/current/round13_global.md);
[product propagation](../mathematics/current/round16_rigidity.md);
[actual cusp-core exclusion](../mathematics/current/round16_global.md);
[latest aspherical theorem](../mathematics/current/line1_aspherical_no_bubbles.md).

Positive-side proofs: [volume separation](../mathematics/current/round17_positive.md),
[all-output local structure](../mathematics/current/round18_positive.md),
[smooth comparison](../mathematics/current/round20_global.md).
Algebraic existence and Wahl non-smoothing are separate sections of the
[global paper](../mathematics/current/skill/research/20260916_global.tex),
`sec:bcgp-global-object`, `sec:campedelli-global-object`, `sec:wahl-global-scope`.

### Complete noncompact connectors have their own equations and topology

The restricted OT critical-point/Morse theorem is retained in the
[earlier global manuscript](../mathematics/current/skill/research/20260916_global.tex),
`sec:OT-critical`: free, isometric, orthogonally transitive action, completeness,
finite topology and the specified exact ends are essential.
The [free-circle boundary-connectedness theorem](../mathematics/current/round9_connector.md)
is broader in symmetry and twist but requires an exact negative Einstein
equation and smooth conformal compactification with a boundary-free action.

In contrast, [actual two-ended approximations](../mathematics/current/round10_kottler.md)
and [circle-bundle doubling](../mathematics/current/round10_cusp_doubling.md)
have vanishing Ricci error on noncompact manifolds with surface cross-sections.
They do not solve the fixed closed flat-\(T^3\) connector problem. Charged
Koiso germs, one-ended caps, nonabelian models, Nil/flat-slice barriers,
relative Chern–Gauss–Bonnet, holonomy and Chern constraints remain individually
locatable in the [inherited full map](../mathematics/current/skill/references/research-map.md),
Sections 11 and “Further substantive proof modules.”

## 5. Proof depth and continuation

The main texts above are not a replacement for the full historical mathematics.
The [September 10 foundation](../mathematics/current/skill/research/20260910.tex),
[September 12 long manuscript](../mathematics/current/skill/research/20260912.tex),
[computational appendix](../mathematics/current/skill/references/computations.md),
[experiment ledger](../mathematics/current/skill/references/experiments.md), and
[source-coverage table](../mathematics/current/skill/references/source-coverage.json)
retain local-flow estimates, ALE kernels/flux, algebraic deformation theory,
rods/corners, harmonic and submersion calculations, sources and nearby corrections.
They prevent “three lines” from becoming three short abstracts.

The [twelve-round synthesis](../mathematics/current/SYNTHESIS.md) is a historical
milestone, not the latest authority for claims extended after Round 12. Later
proofs are direct children of `mathematics/current/`; the installed Skill snapshot
is under `mathematics/current/skill/`. Its older open-status sentences must be
read with this map and the correction register.

Three substantial questions remain independent: broaden the actual inputs and
independent budgets that force a gap; understand surviving equality geometry
and its possible degeneration; realize or exclude an exact metric on the same
smooth topology. A new master formulation is useful if it supplies new
deductions across those questions. Merely renaming their currently unproved
connections does not close them. Neither Yau26 sign branch is settled by this
library's current manuscripts.
