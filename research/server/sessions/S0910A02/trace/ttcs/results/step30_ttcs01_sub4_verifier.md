# TTCS Independent Branch Record

```json
{
  "step_id": 30,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step30_route_reassessment_noncollapsed_bubble_variational.md",
    "Sessions/S0910A02/workspace/data/step30_noncollapsed_bubble_variational_audit.json",
    "Sessions/S0910A02/workspace/notes/step7_positive_branch_four_constructions.md",
    "Sessions/S0910A02/workspace/notes/step8_preceptor_review_positive_branch.md",
    "Sessions/S0910A02/workspace/notes/step29_positive_allocation_and_twist_spike_execute.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md"
  ]
}
```

## Task

Independently verify the Step-30 route reassessment for Yau Problem 26. The key proposed direction is the four-dimensional positive noncollapsed bubble route: if the Cheeger--Naber bad set is empty, smooth Einstein existence on the same manifold follows; if singularities occur, use a variational Pohozaev/Komar projection for merely C^0 Ricci-pinched metrics to recover the Ozuch/Biquard Eguchi--Hanson first obstruction R_+ v=0, without assuming exact Einstein weighted normal form. Read the supplied notes and source excerpts/files. Assess target fidelity, mathematical correctness of the noncollapsed reduction, source-scope limits, whether the divergence-free Einstein-tensor identity is the right C^0-safe bulk pairing, whether first-obstruction vanishing plausibly leads toward actual Einstein existence, and the most serious gaps or likely false assumptions.

## Output

## Verifier memo — Step 30 noncollapsed positive bubble route for Yau 26

I read the Step 30 note and its JSON, the Step 7/8 positive-branch notes, Step 29, and the two Ozuch sources (Integrability 2021 and Noncollapsed degeneration I). Below I check the specific mathematical objects the reassessment rests on, separate what is correct from what is assumed, and locate the substance that must still be produced.

### 1. Target fidelity

The note keeps the full proposition in view and states repeatedly that nothing is settled. The reduction to a single sign-normalized near-Einstein branch is legitimate **for the proof direction**: to establish existence of some admissible pair it suffices to prove that $\|\operatorname{Ric}_g-g\|_{op}\le\delta$ forces an Einstein metric, which yields the narrow positive interval $(1-\delta,1+\delta)$. One point to record precisely: a *refutation* must defeat every interval, and the most permissive intervals are the mixed-sign ones with $c_n\ll 0\ll C_n$; these are a distinct, weaker hypothesis than either $\sigma=\pm1$ branch. The note's phrasing "defeat both positive and $\sigma=-1$ branches" understates the mixed-sign case. This does not affect Route A (a proof route), so it is a minor bookkeeping item.

### 2. The noncollapsed reduction is mathematically sound, and correctly delimited

The chain — Myers diameter bound, Bishop–Gromov + uniform lower volume bound $\Rightarrow$ noncollapse, Cheeger–Naber $\Rightarrow$ subsequential convergence off an isolated (codimension-4 in dimension 4) singular set with $C^{1,\alpha}\cap W^{2,q}$ on the regular part — is correct. The weak-limit argument is also sound: under $W^{2,q}$ ($q>2$) convergence of the metric with strong $C^{1,\alpha}$ convergence of first derivatives, the highest-order (linear) part of Ricci converges weakly while $g_i\to g_\infty$ strongly, so $\operatorname{Ric}_{g_\infty}=g_\infty$ weakly on the regular set; Einstein metrics are smooth (indeed real-analytic) in harmonic coordinates, so the regular limit is a smooth Einstein 4-orbifold. The empty-singular-set conclusion is likewise correct: uniform harmonic radius $\Rightarrow$ global $C^{1,\alpha}$ ($\to C^\infty$) convergence to a smooth Einstein limit $\Rightarrow$ Cheeger–Gromov eventual diffeomorphism $\Rightarrow$ the $M_i$ carry an Einstein metric. So a noncollapsed non-Einstein counterexample must bubble. This is a genuine and faithful reduction.

The essential thing to keep visible: **noncollapse with a uniform lower volume bound is an added hypothesis, not a consequence of $C^0$ Ricci pinching.** Bishop gives only an upper volume bound. Hence "noncollapsed $P_4^+$" is a fixed-topology sub-question and is disjoint from (a) the collapse regime and (b) uniformity over $\#_k(S^2\times S^2)$ as $k\to\infty$, where Step 8's own lower bound $\int|W|^2\ge 16\pi^2 k-O_\delta(1)$ inside Bishop-bounded volume shows curvature energy must diverge and fixed-scale noncollapse cannot be assumed. The note acknowledges this, but the reader should not read the reduction as touching the uniform problem.

### 3. The divergence-free $\mathcal E_g$ pairing is the correct $C^0$-safe object — but only the outer shell

The choice $\mathcal E_g=\operatorname{Ric}_g-\tfrac12 s_g g+\tfrac{n-2}{2}g$ checks out on all three stated points. In dimension 4, writing $\operatorname{Ric}=g+E$ with $\|E\|_{op}\le\delta$: $\mathcal E_g=E-\tfrac12(\operatorname{tr}E)g$, so $\mathcal E_g$ vanishes for exact $\operatorname{Ric}=g$, is $O(\delta)$ pointwise, and is divergence-free by contracted Bianchi ($\operatorname{div}(\operatorname{Ric}-\tfrac12 s g)=0$ for any metric, $\operatorname{div}\,g=0$). This is a real improvement over pairing with $\operatorname{Ric}-g$, whose divergence is $\tfrac12 ds\neq0$ when scalar curvature varies. Ozuch's Lemma 1.4 then gives, exactly,
$$\int_{\partial\Omega}\mathcal E_g(Z,n)=\tfrac12\int_\Omega\langle\mathcal E_g,\mathcal L_Zg\rangle=O(\delta)\,\|\mathcal L_Zg\|_{L^1(\Omega)},$$
with no derivative of $E$ appearing. That structure is correct and is the strongest technical element of Step 30.

The difficulty is that this identity is only the integration-by-parts skeleton. The Ozuch obstruction is a **quadratic, second-order** quantity $\int_{S^3/\Gamma}\operatorname{Ric}_e^{(2)}(H_2,H^4)(Y,\partial_r)$, bilinear in the orbifold-scale term $H_2$ ($|H_2|\sim r^2$) and the bubble-scale term $H^4$ ($|H^4|\sim r^{-4}$). Producing that number from the flux of the full nonlinear $\mathcal E_g$ requires the two-scale expansion $g=\mathbf e+H_2+t^2H^4+t^2H_2^4+\cdots$ in a controlled gauge, plus the identification (Ozuch Prop 3.13, Cor 3.15, Thm 4.6, and Remark 2.11) of $H^4$ with the ALE asymptotic curvature and the higher-order harmonicity of $r\partial_r$ in volume gauge. The $\mathcal E_g$ pairing does not create that content; it only carries it once it exists.

### 4. What the sources actually establish, and where the true analytic substance sits

The note is careful that Ozuch's Theorem 4.6 and Corollary 4.10 are statements about **exact Einstein** sequences GH-close to an orbifold with **integrable** Ricci-flat ALE bubbles, and that the det R / $R_+v=0$ distinction is faithfully rendered (Corollary 4.10 gives the equivalence of $R_+^{(1)}(H_2)\omega_1^+=0$ with the radial + rotation obstructions; the Step 8 correction that $\det R_+=0$ is one eigenvalue of $W_+$ equal to $-s/12$, weaker than Kähler–Einstein, is right).

The load-bearing point that the note states but does not sharpen enough: **the weighted two-scale gauge itself rests on the neck curvature-decay estimate (Bando; Ozuch I, Prop 3 / Thm 0.2), $\rho^{2+l}|\nabla^l\operatorname{Rm}|\le C\epsilon[(\rho_1/\rho)^{\beta_1}+(\rho/\rho_2)^{\beta_2}]$, whose proof uses the exact Einstein equation through harmonicity of the curvature tensor.** For a metric that is only $C^0$-Ricci-pinched, curvature is not harmonic — the 2-form Weitzenböck picks up $\nabla\operatorname{Ric}$ terms that are uncontrolled from $C^0$ data (consistent with the note's Step 11). Cheeger–Naber supplies $C^{1,\alpha}\cap W^{2,q}$ on the regular set and $\epsilon$-regularity, which is far weaker than this weighted decay. So the "approximate-to-exact bridge" is not a matter of restating the obstruction more geometrically; it requires replacing an estimate that presently comes only from the exact equation. This is the single most serious unresolved item, and it is the same one flagged (less pointedly) in Step 8 §4 and Step 7 gap (a).

### 5. The constructive direction is heavier than the route framing suggests

Two structural facts deserve emphasis.

First, forcing the first obstruction to vanish is **necessary, not sufficient**. Higher-order obstructions (Ozu20), the Biquard gluing existence theorem with its nondegeneracy hypotheses, and topology recovery all remain. The note says this (gaps 3–4; Step 29 §4.5), and it should not be read past.

Second, and more structurally: Ozuch's apparatus is primarily a **non-existence** engine. Its headline consequence (Theorem 0.9, via Corollary 4.11) is that spherical/hyperbolic orbifolds cannot be resolved, because the obstruction $\Lambda\,\mathcal V(g_b)+\sum\mathring h^{\pm}_{ij}W^{\pm}_{ji}$ can never vanish when $W^\pm=0$ and $\Lambda\neq0$. For the positive branch, the limit orbifold is positive Einstein with generically $W^\pm\neq0$, so the obstruction *can* vanish. This means the clean contradiction route — "pinched bubbling forces an obstruction that cannot be met, so no bubbling occurs, so the empty-set case applies" — is generally unavailable in the positive branch. Route A as written ("pinching forces $R_+v=0$") therefore lands in the constructive desingularization program (build the Einstein metric on the resolution), which is the hard direction, rather than in a contradiction that excludes bubbles. Calling this "the clearest direct path from Ricci pinching to actual Einstein existence" is optimistic given that the constructive endpoint carries the full Biquard/Ozuch existence machinery plus higher obstructions plus diffeotype recovery.

### 6. A concrete mismatch in the variational-field proposal

The variational functional $J(Z)=\int|\mathcal L_Zg|^2=4\int|\delta_g^*Z|^2$ has Euler–Lagrange operator $\delta_g\delta_g^*Z=0$, whose closed kernel is the Killing fields — correct. But Ozuch's asymptotic fields (Prop 4.1/4.2) are **harmonic** vector fields, $\nabla^*\nabla X=0$, on the *Ricci-flat* ALE bubble. On the pinched metric these operators differ by a Bochner curvature term $\sim\operatorname{Ric}(Z)\approx Z$, which is order one (because $\operatorname{Ric}\approx g$), not $O(\delta)$. So the minimizer of $J$ on the pinched geometry is not the same object as Ozuch's ALE-harmonic field, and reconciling them again requires weighted $C^2$ closeness of the pinched neck to the exact cone/EH geometry — i.e. the same missing two-scale normal form. This should be stated explicitly before the variational field is treated as a drop-in for the exact construction.

The annular scaling in §4.3 / the JSON ($\eta\ll t^2/r^2$) is a plausible heuristic motivating minimizers over transplanted cone fields, but the exact powers are not derived from a genuine neck computation and are labeled exploratory; the bilinear $H_2\!\cdot\!H^4$ structure of the true obstruction (scale-invariant, second order) is not yet matched to the flux error, so the detection threshold remains conjectural.

### 7. Smaller checks that hold

- **EH volume-gauge trace-free leading term (§4.1).** Recomputed: relative coefficients against the flat cone are $(1+x)^{-1/2}$ for $dr^2,\alpha_1$ and $(1+x)^{1/2}$ for $\alpha_2,\alpha_3$ (with $\sqrt{r^4/(1+r^4)}=(1+x)^{-1/2}$, $\sqrt{1+r^4}/r^2=(1+x)^{1/2}$, $x=r^{-4}$). Order-$x$ trace $-\tfrac12-\tfrac12+\tfrac12+\tfrac12=0$. Correct, and it correctly matches Ozuch's volume gauge (Def 3.12, Example 3.11): EH is volume-normalized, so ADM/mass flux is blind at leading order and the useful object is the anisotropic $H^4$ paired with $H_2$. Good observation.
- **det $R_+$ algebra (§4.2, JSON).** For $\operatorname{Ric}=g$, $R_+=W_++\tfrac13 I$, $\det R_+=\prod(w_i+\tfrac13)$: $S^4$ gives $1/27$, KE spectrum $(2/3,-1/3,-1/3)$ gives $0$, generic $(1/3,0,-1/3)$ gives $0$ but is not KE. Consistent with Ozuch Cor 4.10 and with the Step 8 correction.
- **Bubble type.** The obstruction as used assumes Kähler Ricci-flat ALE bubbles in the positive orientation (Ozuch Thm 0.3). Non-Kähler Ricci-flat ALE metrics are not excluded — the source itself notes (Remark 0.11) that the motivating Kähler conjecture's Yang–Mills analog was disproved [SSU89]. General ALE models remain untreated (gap 5, correctly flagged).

### 8. Net reading and what would move the judgment

The reassessment is internally consistent and target-faithful, and it correctly identifies the noncollapsed empty-set case as effectively closed. The $\mathcal E_g$ pairing is a correct and worthwhile $C^0$-safe device. The decisive unresolved substance is not the flux identity but the **weighted two-scale neck normal form and its underlying curvature-decay estimate, which in every existing source is a theorem of the exact Einstein equation (harmonic curvature), and which $C^0$ Ricci pinching does not supply.** Until that is produced (or replaced by a direct projection that bypasses it), the flux identity cannot deliver the Ozuch obstruction from $C^0$ data. Independently, even a $C^0$ obstruction projection would leave the constructive desingularization (higher obstructions, gluing existence, topology recovery) untouched, and the positive-branch limit orbifolds are precisely the ones where obstruction vanishing is *permitted*, so a contradiction-style exclusion of bubbling is not generically on offer.

The cheapest work that would actually change the route's standing: attempt the neck curvature-decay / weighted expansion for a merely $C^0$-Ricci-pinched (non-Einstein) annulus and see whether any decay survives without harmonic curvature — a concrete model calculation on a $t\,g_{EH}$-plus-error neck would either expose that the two-scale gauge collapses without the exact equation, or reveal a weaker decay that still supports a leading-order projection. Everything downstream (the $\mathcal E_g$ flux, the variational field, the $R_+v=0$ identification) is contingent on that estimate existing.