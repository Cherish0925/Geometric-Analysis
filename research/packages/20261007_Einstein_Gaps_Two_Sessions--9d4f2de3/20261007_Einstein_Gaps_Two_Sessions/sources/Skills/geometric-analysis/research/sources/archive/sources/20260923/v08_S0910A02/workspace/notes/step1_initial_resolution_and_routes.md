# Step 1 initial resolution state and route map for Yau Problem 26

Session: S0910A02. Agent: Agent1/Explore. Date anchor: 2026-09-10.

Human update: the human scientist explicitly said not to modify the original goal; the aligned goal and original goal in `workspace/briefing/` are identical. The target below is therefore the original working target, not a narrowed substitute.

## Exact target and normalization

Working category: closed (= compact without boundary), connected, smooth real manifolds, dimension `n >= 2`, with smooth Riemannian input metric `g`. The claim to prove or refute is:

`Q_n`: there exist real constants `c_n < C_n`, depending only on `n`, such that every such `M^n` and every smooth `g` satisfying `c_n g <= Ric_g <= C_n g` (quadratic-form sense) has some smooth Einstein metric `h` on the same smooth manifold: `Ric_h = lambda h` for some real constant `lambda`.

For sign-normalized work define, for `sigma in {+1,-1}`,

`delta_sigma(g) = sup_x || g^{-1} Ric_g - sigma Id ||_op`.

Then

`P_n^sigma`: there exists `epsilon_n^sigma in (0,1)` such that `delta_sigma(g) <= epsilon_n^sigma` implies `M` carries an Einstein metric.

The dossier proves the important quantifier equivalence in the stated category:

`Q_n <=> P_n^+ OR P_n^-`.

Reason: any nondegenerate interval contains a nondegenerate same-sign subinterval; after constant rescaling of `g`, the same-sign subinterval becomes a small interval around `+1` or `-1`. Conversely a sign-normalized interval is itself an instance of `Q_n`. Therefore a full proof for dimension `n` only needs one branch, but a refutation of `Q_n` for a fixed `n` must refute both branches in that same dimension. Cross-zero intervals are not an independent third branch.

Completion standard remains extremely high: complete mathematical proof or strict refutation of all dimensions, and ultimately a Lean 4 formalization/audit of the final proof. At Step 1 we only have orientation, not resolution.

## Source status after Step 1 reading/retrieval

1. `Sessions/S0910A02/workspace/briefing/original_research_goal.md` and `aligned_research_goal.md` are identical and state the above target and completion standard.
2. `Skills/qiushi-yau26/references/research/20260910.tex` is the main dossier. It gives the working problem text from a user-provided reorganized open-problem PDF and records page locations, but it also says the 1982 historical original has not yet been fully compared page-by-page.
3. `Knowledge/objects/books/Preview-9781400881918-A27764136--0cd226eb76cf--1153cba28721/object.md` and duplicate `Knowledge/objects/books/seminar-on-differential-geometry--0cd226eb76cf--bcd0bdd20261/object.md` confirm the 1982 Annals Studies volume identity and table-of-contents entry `PROBLEM SECTION by S.-T. Yau 669`, but the available preview does not include the actual Problem Section pages containing Problem 26. Thus historical exact wording remains a source obligation. It does not invalidate the human-provided target.
4. Min-Oo 1990 was retrieved from ProjectEuclid as `Knowledge/objects/papers/ALMOST-EINSTEIN-MANIFOLDS-OF-NEGATIVE-RICCI--c331e7060106--bcf9bda031d7/object.md` (DOI 10.4310/jdg/1214445315), with a noisier duplicate at `Knowledge/objects/papers/Almost-Einstein-manifolds-of-negative-Ricci-curvature--1777cabbd0f4--2f3b8d36356a/object.md`.
5. Anderson 1989 JAMS Corollary B(4) and Ye 1993 were not retrieved in exact theorem form by the two knowledge requests. They remain high-priority source gaps, because their hidden hypotheses may sharply define what classical stability already proves.
6. Morteza--Viaclovsky, `Knowledge/objects/papers/The-Calabi-metric-and-desingularization-of-Einstein-orbifolds--3b9fd6e4b2cd--c8fe6b2cf08c/object.md`, and Ozuch I, `Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md`, were inspected for the orbifold-resolution counterexample mechanism.

## Corrected Min-Oo scope

Important correction to avoid propagating OCR error: Min-Oo denotes the diameter by `d`. The class in the introduction is OCR-corrupted, but Section 3 normalizes `max |K(0)| = 1` and assumes `d(0) < Lambda`, so the scale-invariant geometric bound is best read as roughly

`d(g)^2 max |K_g| < Lambda^2`,

not as `r^{-2} max |K|`. Min-Oo's theorem is therefore: for `n > 3` and `Lambda > 0`, compact metrics with `r < 0`, the above diameter/full-sectional-curvature scale bound, and sufficiently small normalized Ricci deviation `max_SM | n p/r - 1 | < epsilon(n,Lambda)` admit a negative Einstein metric (indeed via normalized Ricci flow, near the input). The theorem does not solve `P_n^-` because `epsilon` depends on `Lambda`, and `Lambda` is not controlled by pure Ricci pinching. A negative-branch counterexample sequence with `delta_-(g_j) -> 0` must therefore evade Min-Oo by `d(g_j)^2 max |K_{g_j}| -> infinity` (or by falling outside the precise normalization), not merely by lacking injectivity-radius control. Exact OCR/formula should be rechecked from a clean PDF when available.

## Low-dimensional baseline

- `n=2`: every closed connected surface carries a constant-curvature metric by uniformization, hence an Einstein metric. Thus `Q_2` is true regardless of the input pinching interval.
- `n=3`: the dossier records strong evidence that both branches are true. Positive branch: Hamilton's positive Ricci theorem gives a spherical space-form metric from `Ric>0`. Negative branch: if Ricci eigenvalues lie in `[-1-epsilon,-1+epsilon]` with `epsilon<1/3`, the 3D curvature-operator algebra gives all sectional curvatures negative; geometrization plus negative-curvature topology yields a hyperbolic metric. This needs formal source-grade reconstruction later, but it is a strong baseline.

The real unresolved frontier begins at `n >= 4`.

## Orbifold-resolution mechanism: current adversarial scaling check

Peer S0910A03 proposed: resolutions of Einstein orbifolds might support metrics with unweighted sup operator-norm `|Ric - lambda g| -> 0`, while a 4-manifold obstruction excludes all Einstein metrics. This is a serious possible refutation route, but Step 1 found a crucial obstruction to using currently inspected Morteza--Viaclovsky estimates naively.

Morteza--Viaclovsky define on the Calabi piece a refined metric `h_t = g_cal + t h`. Lemma 4.1 gives, on `X^t`,

`| nabla^k ( Ric_{h_t} - t Lambda h_t - t lambda o ) |_{g_cal} <= c_k t^2 rho^{2-k}`.

On the compact desingularization metric `g_t`, Lemma 4.2 gives

`| nabla^k ( Ric_{g_t} - Lambda g_t - t lambda chi_t(rho) o ) |_{g_cal} <= c_k t^2 rho^{2-k}`

on the Calabi/damage region, with `g_t ~ t g_cal` in the core and transition scale `rho <= O(t^{-1/4})`.

For the Yau26 defect one needs operator norm with respect to `g_t`, not `g_cal`. A `(0,2)` tensor norm scales by `t^{-1}` under `t g_cal`. Therefore:

- the remainder `O(t^2 rho^2)` becomes `O(t rho^2)` in `g_t`-operator norm, hence at worst `O(t^{1/2})` in the transition and `O(t)` in the core: this part is compatible with unweighted pointwise defect going to zero;
- but the obstruction term `t lambda chi_t o` becomes order `|lambda o|_{g_cal}` in `g_t`-operator norm on the Calabi core. Since `o` is bounded and nonzero near the exceptional set, if `lambda != 0` the unweighted `delta`-type defect does not tend to zero.

Thus the known first-obstruction nonexistence case (`lambda != 0`) appears *not* to provide a Yau26 pinched input; it gives only weighted/Lp/small-volume residual phenomena. This aligns with Ozuch I's example of metrics with `Ric(g_i) >= 3 g_i` and `||Ric(g_i)-3g_i||_{L^p}->0` but no Einstein sequence with the same GH limit: `L^p` smallness is not `C^0` operator pinching, and no-nearby-Einstein is not global no-Einstein.

A refined live route remains: find a compact orbifold desingularization where the leading unweighted obstruction term can be killed (`lambda=0` or by adding correct local/global parameters), so the approximate metrics are genuinely `C^0` Ricci-pinched, while a higher/global obstruction still rules out all Einstein metrics on the smooth topology. That route has two hard missing pieces: (i) actual unweighted full-manifold estimates after all matching terms, and (ii) a global all-sign all-metric Einstein obstruction for the chosen smooth manifolds.

## Current candidate route space (to be expanded and attacked over opening Explore steps)

1. **Negative uniform stability beyond Min-Oo.** Try to prove `P_n^-` by removing Min-Oo's `d^2 max|K|` dependence through multiscale analysis of bounded Ricci + near-Einstein trace-free Ricci. Failure mode: collapse/large-diameter/full-curvature blow-up may create no uniform inverse bound.
2. **Negative counterexample by obstructed orbifold resolution with killed first obstruction.** Construct `delta_-(g_t)->0` on no-Einstein smooth resolutions. Failure mode: nonzero first obstruction gives order-one C0 defect; vanishing obstruction may actually allow an Einstein metric or fail global exclusion.
3. **Positive counterexample by positive Einstein orbifold resolution plus smooth-topology obstruction.** Seek C0 `Ric~+g` metrics where LeBrun/SW/HT-type obstructions exclude all Einstein metrics. Failure mode: Chern-Weil near-pinching may force the topological inequalities needed by Einstein, and known obstructed gluing may only be Lp-small.
4. **Positive existence via Ricci flow/sphere-theorem upgrade.** Try to show sufficiently `Ric~+g` in any dimension gives an Einstein metric, maybe via finite-time smoothing plus topology. Failure mode: pure Ricci does not control Weyl or curvature operator; known sphere theorems need stronger curvature positivity.
5. **Four-dimensional integral gap program.** Extend the dossier's `delta_sigma < 1/(1+sqrt 3)` implication `2 chi > 3 |tau|` into stronger SW/LeBrun-compatible quantitative inequalities for all no-Einstein topologies. Failure mode: known no-Einstein manifolds satisfying HT may not be blocked by Ricci pinching alone.
6. **Noncollapsed compactness and bubble obstruction.** Under added volume lower bound, bounded Ricci tools (Cheeger--Naber/Jiang--Naber/Ozuch) may reduce failure of `P_4^sigma` to orbifold/bubble obstructions. Failure mode: Yau26 includes collapse, and converting limit information to existence on each input topology is hard.
7. **Collapse/F-structure classification under `Ric~sigma g`.** Analyze whether collapse with near nonzero Einstein Ricci forces local bundle/quotient structures that already carry Einstein metrics. Failure mode: negative branch has no diameter bound; positive branch finite fundamental group still allows quotient collapse.
8. **Lohkamp/Kazdan negative-Ricci flexibility test.** Determine whether arbitrary closed manifolds can carry metrics with `delta_-` arbitrarily small. Known sources only support `Ric<0`/negative Ricci flexibility or prescribed-Ricci local/special results, not tight `Ric≈-g`. If tight flexibility existed it would likely refute `P_n^-` using no-Einstein manifolds.
9. **Prescribed Ricci equation as a deformation around `T=-g`.** Study why solving `Ric(g)=-g+small` is flexible but solving `Ric(g)=-g` is obstructed; maybe approximate solvability is universal. Failure mode: because the target tensor is the metric itself, not a fixed tensor, prescribed-Ricci results do not directly apply.
10. **Surgery/connected-sum quantitative Ricci pinching.** Use positive/negative Ricci surgery to build near-Einstein metrics on connected sums with no Einstein metric. Failure mode: neck regions usually have order-one anisotropic Ricci unless a precise Einstein gluing model controls C0 error.
11. **Exotic smooth structures.** Use smooth structures admitting curvature/sign input but obstructing Einstein metrics. Failure mode: input metrics often obstructed by positive scalar/Dirac/SW conditions, or exact Einstein may exist with a different sign.
12. **Besson--Courtois--Gallot / entropy rigidity negative route.** Near `Ric=-g` may imply entropy/volume constraints; perhaps obstruct exact Einstein on certain aspherical manifolds or prove existence. Failure mode: Ricci lower bounds give weak upper entropy only under additional curvature/topological hypotheses.
13. **Hyperbolization and non-locally-symmetric manifolds.** Strictly negative sectional pinching is no longer an obstruction because Hamenstädt--Jäckel construct negative Einstein metrics on Gromov--Thurston-type manifolds. Still, other hyperbolized no-Einstein candidates could be tested. Failure mode: no local-symmetry is not no-Einstein.
14. **Homogeneous and cohomogeneity-one laboratories.** Use exact algebra/ODE systems to find new mechanisms, hidden branches, and rigorous certificates. Failure mode: ansatz results do not decide all metrics on the underlying manifold.
15. **Degree/continuation for the Einstein operator.** Treat near-Einstein metrics as approximate zeros and use an index/degree argument robust to degenerations. Failure mode: moduli noncompactness, diffeomorphism gauge, sign changes, and near-kernel escape.
16. **Variational Palais--Smale analysis of normalized total scalar/Yamabe-type functionals.** `delta_sigma` small gives approximate criticality of Einstein-Hilbert in a strong pointwise sense; classify failure of convergence. Failure mode: lack of compactness may be exactly the hard problem.
17. **Finite cover/quotient descent.** If input pinching implies a finite/controlled cover carrying an Einstein metric, determine when it descends. Failure mode: an Einstein metric on a cover does not automatically descend unless deck transformations are isometries for that metric.
18. **Kähler/complex subprogram.** In Kähler classes, KE existence theory gives exact answers; use it as a controlled testbed and source of examples, not as global proof. Failure mode: no KE for one complex structure is not no Riemannian Einstein on the smooth manifold.
19. **Lean/formalization backbone.** Formalize branch equivalence, scaling identities, low-dimensional algebraic curvature identity, and Chern-Weil inequality fragments as reusable audited pieces. Failure mode: formalizing only reductions does not solve the analytic/geometric theorem.
20. **Historical/source-resolution route.** Obtain and compare the original 1982 Problem Section and exact Anderson/Ye theorem statements. Failure mode: source work cannot solve the mathematics, but it can prevent target drift and duplicate work.

## Near-term priorities for subsequent opening Explore steps

A. Correctly recover Anderson 1989 Corollary B(4) and Ye 1993 theorem statements. If not retrievable by automated knowledge, search library metadata, citations inside later papers, or ask peers.

B. Have Agent2/Agent3 perform a more careful unweighted scaling calculation for the orbifold-resolution metrics: convert all Morteza--Viaclovsky/Ozuch weighted estimates into `g_t`-operator norms region by region, identify whether any obstruction-free approximate family gives `delta_sigma -> 0`, and decide which topology would be involved.

C. Have Agent4 independently challenge target fidelity and the logical equivalence/refutation quantifiers, especially the requirement that a fixed dimension refutation must kill both positive and negative branches.

D. Prepare grounded TTCS generator/verifier calls while still in early Explore: ask for genuinely different high-value route ideas and for adversarial checking of the current route map and orbifold scaling logic.
