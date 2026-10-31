# Step 66: Route reorientation after completing the restricted IL analytic bridge

Session: S0910A01. Agent1 / Orchestrator. Phase: Explore.

## 0. Starting point

Step 65 supplied the per-datum existence theorem for the exact degenerate cutoff flow
\[
\partial_t g=-2\chi^2(\operatorname{Ric}_g-\sigma g)
\]
on any closed smooth manifold, for any smooth positive initial metric and smooth cutoff, with datum-dependent time and arbitrary normalization sign \(\sigma\in\mathbb R\). This removes the last named analytic hypothesis in the restricted four-dimensional Ishida--LeBrun (IL) negative-gap route.

The governing Yau26 problem is still much larger: find dimension-only constants \(c_n<C_n\) forcing the underlying closed smooth \(n\)-manifold to admit *some* Einstein metric, or disprove that proposition. The input metric and output Einstein metric are unrelated; the constants may have any sign. The IL result is a restricted negative-normalization theorem over a special Seiberg--Witten geography, not a solution of the original problem.

## 1. Correction to Step 65's application-level wording

Step 65 §8 originally said that the restricted IL first-exit endpoints give family-uniform \(C^k\) bounds on positive-time slabs. That is too strong and is not needed.

Correct statement:

* The per-datum theorem gives a smooth solution up to a datum-dependent time.
* In the IL application, the first-exit bootstrap controls the weighted curvature quantity and the velocity integral \(V(t)=\int_0^t\|aE\|_\infty\) up to the desired observation time.
* If a per-datum solution hypothetically stopped before \(\theta r^2\), then on a positive-time slab ending at that time the weighted estimates and the separate continuation hierarchy give a smooth positive endpoint with higher bounds depending on that datum/slab.
* Since the equation is autonomous in geometric variables, the solution can be restarted from the endpoint, with matching time jets. No family-uniform higher derivative bounds and no single concatenated DeTurck gauge are required.

I patched `workspace/notes/step65_per_datum_existence_theorem.md` accordingly.

## 2. Two route regressions removed

### 2.1 `#_5 CP^2` is excluded, not live

For \(M=\#_m\mathbb{CP}^2\),
\[
\chi=m+2,\qquad \tau=m,
\qquad 2\chi-3\tau=4-m.
\]
Thus \(\#_5\mathbb{CP}^2\) has \(2\chi-3\tau=-1\). The elementary four-dimensional Chern--Weil estimate already recorded in the dossier and earlier steps implies that sufficiently tight normalized Ricci pinching of either sign forces strict Hitchin--Thorpe:
\[
2\chi>3|\tau|.
\]
Consequently \(\#_5\mathbb{CP}^2\) and all stronger Hitchin--Thorpe violators cannot support arbitrarily tight positive or negative \(\pm1\)-Ricci pinching. Positive-Ricci connected-sum metrics on these smooth types therefore provide useful coarse examples and negative controls, but not a live near-Einstein counterexample family.

The live positive-Ricci topology problem is instead concentrated in strict-Hitchin--Thorpe smooth types whose Einstein existence is absent, unknown, or dependent on smooth structure, and for which no curvature-integral gap already prevents tight pinching. Even there, positive Ricci existence is only a sign condition; it carries no known quantitative near-Einstein information.

### 2.2 A02's Green-operator calculation has asymmetric meaning

A02's mixed Eguchi--Hanson pattern computation on \((S^2\times S^2)/\mathbb Z_2\) can decide whether a *particular orbifold degeneration* can be desingularized to Einstein metrics. Its implications are asymmetric:

* Success would construct exact Einstein metrics on the resulting smooth type, removing that smooth type as a no-Einstein counterexample candidate and adding positive-branch existence evidence.
* Failure would obstruct that degeneration or that local gluing channel. It would not by itself prove that the smooth type admits no Einstein metric, because an unrelated Einstein metric need not approach the studied orbifold.

Thus the computation is valuable for positive-branch geometry and obstruction theory, but it cannot be substituted for global Einstein nonexistence without an additional compactness/rigidity theorem forcing all relevant Einstein metrics into that degeneration.

## 3. What the new cutoff-flow capability actually transfers

The sign-general cutoff flow gives a reusable analytic implication of the following form.

Suppose a branch \(\sigma\in\{-1,0,+1\}\) and a manifold family supply:

1. a global curvature/defect budget from topology or another invariant;
2. a selected-support construction with proportional volume and small local mean terminal density;
3. a branch-specific nonnegative density \(\Phi_\sigma\) whose zero set, after passing through the cutoff flow and harmonic-chart compactness, forces an impossible smooth Einstein germ or a rigid output class incompatible with the topology.

Then the Step 65 flow plus Steps 55--63 smoothing machinery can convert near-\(\sigma\)-Einstein input metrics into a local contradiction. This is exactly what happens for the IL negative branch: Seiberg--Witten supplies the mixed scalar--\(W^+\) budget, and Derdziński supplies the forbidden calibrated germ.

The flow does **not** supply the missing ingredient for the positive branch: no known positive analogue of the mixed Seiberg--Witten calibration produces a dimension-uniform density whose zero set contradicts a positive Einstein germ. Positive Einstein four-manifolds can have nonzero Weyl curvature and can degenerate to orbifolds, so a naive curvature-concentration or gluing-failure argument is not enough.

## 4. Assessment of currently live fronts

### Front A: finish a self-contained restricted IL theorem

Now that the per-datum existence bridge is in place, a self-contained theorem can likely be assembled:

> In the specified IL geography with \(m\in\{2,3\}\), \(b_+(N)=0\), full monopole sign family, and \(q\ge0\), there exists \(\varepsilon_{IL}>0\) independent of the geography parameter \(A\) such that no metric satisfies \(\|g^{-1}\operatorname{Ric}_g+I\|_{\infty,op}<\varepsilon_{IL}\).

This is scientifically valuable because it proves a family-uniform negative gap where elementary characteristic estimates only gave topology-dependent information. But it is not dimension-only Yau26: it excludes a special no-Einstein geography from one sign branch rather than proving that all sufficiently pinched manifolds admit Einstein metrics.

The theorem assembly must be done under the canonical convention \(G=(g\owedge g)/(2(n-1))\), \(T=\operatorname{Rm}-G\), \(\operatorname{Ric}(G)=-g\). Legacy plus-sign displays must be rewritten, not copied.

### Front B: positive branch in dimension four

After eliminating Hitchin--Thorpe violators like \(\#_5\mathbb{CP}^2\), a counterexample would need a strict-Hitchin--Thorpe no-Einstein smooth type carrying metrics with \(\delta_+(g)\to0\). Known positive-Ricci constructions (Perelman/Burdick/Reiser) give \(\operatorname{Ric}>0\) on connected sums such as \(\#_k\mathbb{CP}^2\), but source reading confirms they are coarse sign constructions using core metrics, docking stations, and Ricci-positive gluing; they do not provide near-Einstein pinching estimates.

Promising questions:

* Is \(\#_3\mathbb{CP}^2\) known to admit no Einstein metric, or is its status open? It satisfies strict Hitchin--Thorpe: \(2\chi-3\tau=1\), so elementary Chern--Weil pinching does not exclude tight positive Ricci.
* Can one prove a quantitative neck anisotropy lower bound for Perelman/Burdick positive-Ricci connected-sum metrics that prevents \(\delta_+\to0\), analogous to a positive-side gluing obstruction?
* Can positive Einstein orbifold degeneration theory give a global theorem: any putative tight positive branch on a no-Einstein smooth type must approach a finite list of orbifolds, where desingularization obstructions can be checked? At present this global compactness bridge is missing.

### Front C: negative branch outside IL

The IL mechanism depends on the mixed Seiberg--Witten inequality and a monopole sign family. Extending it beyond IL requires either a new topological/invariant budget replacing \((a^+)^2\ge A\), or a classification showing all negative near-Einstein no-Einstein candidates enter a comparable calibration regime. Neither is known.

A03's graph-manifold work remains live only in the general \(g=dr^2+\gamma(r,x)\) class after correction #478. The flat-slice result is valid for coordinate-independent collars, but finite JAX runs and the withdrawn Preissmann/Ricci implication do not prove global nonexistence. This route may still expose a collapse-compensation mechanism, but it should be treated as a genuine PDE/topology problem rather than a closed model class.

### Front D: higher dimensions

The cutoff-flow existence theorem works in all dimensions, but the four-dimensional IL calibration uses Chern--Weil and self-dual Weyl geometry. For \(n\ge5\), there is no known topological curvature budget of the same strength. Candidate sources include Pontryagin/Chern--Weil integrals, entropy/simplicial-volume rigidity, locally symmetric degree theorems, and Einstein orbifold/desingularization obstructions, but each currently carries non-dimension-only parameters or hypotheses.

## 5. Best next mathematical action

The strongest immediate research action is not final expression. It is to build a branch-and-front decision theorem/note that makes the full Yau26 search sharper after the restricted IL bridge:

1. Extract a precise reusable proposition: "flow-transfer principle" = per-datum sign-general cutoff flow + first-exit smoothing + local compactness converts any suitable branch calibration into a uniform gap.
2. Apply it to the IL negative branch as the first complete instance.
3. State exactly why the same proposition does not yet apply to the positive branch: missing calibration density and missing global compactness/rigidity forcing Einstein metrics into studied degenerations.
4. For positive topology, replace `#_5 CP^2` by strict-Hitchin--Thorpe targets and verify their Einstein status from sources before investing computation.
5. Ask A02 for outputs of the Green-operator computation with the asymmetric interpretation: construction proves existence; obstruction is only local unless paired with a global compactness theorem.
6. Ask A03 to formulate a concrete general-\(\gamma(r,x)\) graph-neck estimate or counterestimate, not a model-class closure.

This route preserves the IL achievement while using it as a reusable analytic capability for the actual sign-unrestricted problem.

## 6. Source grounding read in this step

* Original goal: `workspace/briefing/original_research_goal.md`.
* Step 65 existence theorem: `workspace/notes/step65_per_datum_existence_theorem.md` (patched §8).
* First-exit structure: `workspace/notes/step55_joint_bootstrap_background_continuation_repair.md`.
* Local forbidden-germ and averaging route: `workspace/notes/step8_derdzinski_measure_local_theorem.md`.
* Dossier lines around the original problem, Hitchin--Thorpe pinching barrier, Anderson caution, positive Ricci constructions, and desingularization warnings: `Skills/qiushi-yau26/references/research/20260910.tex`.
* Positive-Ricci construction source: Burdick `Knowledge/objects/papers/Ricci-positive-metrics-on-connected-sums-of-projective-spaces--17bdbf22f9bb--cb9ce73e65bd/object.md`, lines 50--83; Reiser `Knowledge/objects/papers/Positive-Ricci-curvature-on-connected-sums-of-fibre-bundles--def298bd9dda--58891086f50d/object.md`, lines 29--76.
* Min-Oo source: `Knowledge/objects/papers/Almost-Einstein-manifolds-of-negative-Ricci-curvature--1777cabbd0f4--2f3b8d36356a/object.md`, lines 95--169, confirming the negative almost-Einstein theorem assumes a class with diameter/curvature parameter and explicitly says the method fails for nonnegative Einstein constant.
* Peer messages #478 and #479, incorporated with corrections.

---

## Step 67 correction: terminal IL density is recovered, not newly missing

Step 67 supersedes the part of this note that left the IL terminal density interface as an unresolved possibility.  Direct reading of Step 28 §1 and Step 45 §§2,7 shows that the terminal closed metric satisfies the same monopole and Chern--Weil identities, so the density is regenerated algebraically at time `T`:
\[
D_{\rm av}(T)=J(T)-q-\frac23\sum_\ell |e_\ell^+(T)|^2
\le J(T)\le \frac{Q(T)}{8\pi^2}\quad(q\ge0),
\]
and hence
\[
\int \Phi(g(T))\le119Q(T).
\]
No transport of initial Weyl density is used, and no `q_+` term appears in the restricted `q>=0` theorem.  The detailed recovered lemma is `workspace/notes/step67_terminal_recalibration_recovery.md`, with constants verified by `workspace/scripts/step67_terminal_recalibration_verify.py` (11/11).  The remaining IL work is canonical-convention assembly of the selected-support flow modules, not invention of a new terminal transport theorem.
