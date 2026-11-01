# TTCS Independent Branch Record

```json
{
  "step_id": 95,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/notes/step87_resolvent_obstruction_theorem.md",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md",
    "Sessions/S0910A03/workspace/notes/step89_twist_bochner_and_resolvent.md",
    "Sessions/S0910A03/workspace/notes/step91_separator_stability_and_barriers.md",
    "Sessions/S0910A03/workspace/notes/step94_charge_sign_correction_and_global_flux.md",
    "Sessions/S0910A03/workspace/data/step95_charged_obstruction_theorem.json"
  ]
}
```

## Task

Verify the following theorem about free-T² connectors with twist. The claim is that twist (Q > 0) CANNOT help evade the existing OT connector obstruction.

**Theorem**: For a free T² metric on a closed 4-manifold with ||Ric+3g||_op ≤ δ, two complete cusp-type expanding ends, and cylindrical base B ≅ S¹ × ℝ, if δ < δ* ≈ 0.246, then no such metric exists regardless of the twist charge Q ≥ 0.

**Proof chain**:
1. Forced Bochner with twist: the corrected drift curvature (Step 89) is Ric_f = Ric_B - Hess σ = (-3+Q)γ + ½dσ² + ½U*h + E_B. Since Q ≥ 0, Ric_f ≥ -(3+δ)γ (same lower bound as OT). The Bochner becomes ½Le ≥ ½e(e-6) + Qe - Cδ² - (3+δ)e. Since Qe ≥ 0, dropping it gives the OT Bochner: ½Le ≥ ½e(e-6) - Cδ² - (3+δ)e.

2. Resolvent ceiling: applying the massive resolvent (Step 87) to the weakened OT Bochner gives ceiling B(δ) ≈ [4δ/√(3+δ)+√(2(3+δ)+20δ²/(3+δ))]². This is valid because the actual Bochner with +Qe is stronger, making e decay at least as fast.

3. Separator floor: the minimal separator (Step 88) gives ⟨e_s⟩ ≥ 12 - 8δ + 2⟨|II|²⟩ + ⟨h²⟩. Since |II|² ≥ 0 and h² ≥ 0, the floor is ≥ 12-8δ regardless of Q_C.

4. For δ < δ*: 12-8δ > B(δ), so ⟨e_s⟩ > sup e, contradiction.

Key question: Is step 1 correct — does the +Qe Bochner term arise from the corrected drift curvature with twist? Specifically, does Ric_f(dU,dU) = (-3+Q)e + nonneg terms? And is it valid to drop +Qe and use the OT ceiling?

## Output

## Verifier memo: twist-invariant free-T² connector theorem (Step 95)

### Bottom line

Step 1 of the proof chain is essentially correct as a statement about the drift curvature. Step 2 is where the argument breaks down: it is **not** valid to drop the favorable $+Qe$ term and then reuse the pure-OT ceiling $\mathcal B(\delta)$. Twist enlarges the forcing terms that feed the resolvent source, so the true twist ceiling exceeds $\mathcal B(\delta)$ and rises with $Q$ faster than the separator floor rises. This is exactly the correction the same session recorded in Step 91 §5 and in the Step 89 header, and the Step 95 note reverts to the reasoning those two notes explicitly withdrew. The theorem as written is not established, and its own numerical machinery refutes it once the correct ceiling is used.

### Step 1 verification (correct)

The drift-curvature identity is algebraically sound. From Step 89:

- direct base twist Ricci is $\operatorname{Ric}^{\rm twist}_{ij}=-Q\gamma_{ij}$ (symbolically verified, $\operatorname{Ric}^{\rm twist}_{rr}/(e^{2\lambda}Q)=-1$);
- the horizontal Einstein equation $\operatorname{Ric}_B-\operatorname{Hess}\sigma-\tfrac12 d\sigma^2-\tfrac12U^*h-Q\gamma_B=-3\gamma_B$ solves to
$$
\operatorname{Ric}_B-\operatorname{Hess}\sigma=(-3+Q)\gamma_B+\tfrac12 d\sigma^2+\tfrac12U^*h+E_B .
$$

The $-Q\gamma$ on the left does become $+Q\gamma$ on the right; contracting with $A=dU\otimes dU$ gives $\operatorname{Ric}_f(dU,dU)=(-3+Q)e+\text{nonneg}$, so the reaction term is $\tfrac12e^2-(3-Q)e=\tfrac12e(e-6)+Qe$. The $+Qe$ is real. Your first question answers affirmatively.

One bookkeeping slip in the memo's written Bochner "$\tfrac12Le\ge\tfrac12e(e-6)+Qe-C\delta^2-(3+\delta)e$" double-counts the linear term: $\tfrac12e(e-6)$ already contains $-3e$, so adding $-(3+\delta)e$ produces $-(6+\delta)e$. The correct reaction (Step 89 §3.2) is $\tfrac12e^2-(3+\delta)e+Qe$, i.e. a single factor of $3$. This is a transcription issue, not the core problem, but it should be fixed before the identity is used.

### Step 2 breaks down: the ceiling is not $\mathcal B(\delta)$

The pure-OT ceiling $\mathcal B(\delta)$ was derived from a resolvent source built with a forcing field bounded by $|V|\le 2\delta\sqrt e$ and no $-Q^2$ tension. With twist, two things change that are **not** removed by dropping $+Qe$:

1. **Tension.** The orbit-shape equation is forced by the charge even at $E=0$ (Step 88 §5.3, Step 89 eq 1.5): $|S_F|^2=Q^2$. This enters the forced Bochner as $-Q^2$, which becomes $+2Q^2$ in the resolvent source.
2. **Enlarged forcing field.** Step 89 §4 gives $|V|\le f\sqrt e$ with $f=Q+2\delta$, strictly larger than the OT value $2\delta$. In the self-consistent Duhamel closure $B\le \alpha+\beta\sqrt B$, the coefficient $\beta$ is proportional to $\|V\|_\infty$, so it grows linearly in $Q$.

Dropping the favorable $+Qe$ from the reaction while retaining these adverse forcing terms does not reduce the problem to the $Q=0$ problem. The genuine $Q=0$ problem has $Q=0$ in **every** term, including the forcing. What the proof actually produces after dropping $+Qe$ is
$$
(-L+\kappa)e\le \kappa^2+2Q^2-2\operatorname{div}_\sigma V,\qquad \|V\|_\infty\le (Q+2\delta)\sqrt B,
$$
whose self-consistent solution is the Step 89 formula (4.3), not $\mathcal B(\delta)$.

The monotonicity heuristic offered ("the actual Bochner with $+Qe$ is stronger, so $e$ decays at least as fast, so the OT ceiling still bounds $e$") compares the wrong pair of problems. The correct comparison is: true twist Bochner (favorable reaction + adverse forcing) versus pure-OT Bochner (OT reaction + OT forcing). These differ in the source, not only the reaction, and the source difference is adverse. A subsolution of a barrier with a larger source has a larger ceiling.

### Numerical refutation using the note's own formulas

Take $\delta=0.1$, $Q=1$ (the JSON's own test point). The Step 89 twist ceiling (keeping $+Qe$, mass $\kappa=6-2Q+2\delta$, $3-Q+\delta=2.1$, $f=1.2$):
$$
B\le\Big[\tfrac{2f}{\sqrt{2.1}}+\sqrt{2(2.1)+\tfrac{5f^2}{2.1}}\Big]^2
=[1.656+2.762]^2\approx 19.5 .
$$
If instead one drops $+Qe$ (mass $\kappa=6+2\delta$, $3+\delta=3.1$) as the theorem proposes but keeps $f=Q+2\delta=1.2$:
$$
B\le[1.363+2.919]^2\approx 18.3 .
$$
Either value dwarfs the charged floor $12-8\delta+2Q_C=13.2$. The gap is **negative** (ceiling $\approx 18$–$19$ exceeds floor $13.2$): no contradiction, so no obstruction at $Q=1$, $\delta=0.1$.

The JSON's `at_delta_0.1` block reports `ceiling: 7.453` for the charged $Q=1$ row while using `floor_charged_Q1: 13.2`. The $7.453$ is $\mathcal B(0.1)$, the $Q=0$ ceiling. Pairing a charged floor with an uncharged ceiling is precisely the disallowed substitution; replacing it with the $\approx 18$–$19$ twist ceiling reverses the sign of every "gap_charged" entry in the file. This reproduces Step 91 §5's derivative comparison $\partial\mathcal B_{\rm tw}/\partial Q_+\approx 8.86$ versus $\partial\text{floor}/\partial Q_C=2$: the ceiling outpaces the floor.

### The $Q_C$ versus $Q_+$ gap the theorem does not bridge

Even granting the resolvent machinery, the floor is controlled by the separator-averaged charge $Q_C=\langle Q\rangle_C$, bounded by stability at $Q_C\le 3+\delta$ (Step 91 §3). The ceiling is driven by the interior supremum $Q_+=\sup Q$, which Step 91 §5 states is not bounded by stability, and which Step 90's charged radial disk caps show can be order-one with small local defect. The theorem tacitly identifies $Q_C$ with $Q_+$ (the "$2Q_C$ gain" reasoning). For spatially varying $Q$, a small separator value ($\to$ small floor gain) can coexist with large interior charge ($\to$ large ceiling), which is the worst configuration for the argument, not the safe one.

### Additional item on variable $Q$

The Step 89 header and Step 90 record that for spatially varying $Q$ the target source $S_F=-\nabla_{\mathbb H^2}Q$ contributes a $-Qe$ that cancels the $+Qe$ drift improvement exactly. If that cancellation holds, then even the favorable term the proof leans on in Step 1 is absent in the variable-charge setting, while the enlarged forcing $|V|\le(Q+2\delta)\sqrt e$ persists. This removes the only element the proof treats as a margin. The theorem does not address whether $Q$ is constant; for a genuine connector it varies (Step 94 §6 exhibits an exact area-equation redshift-taper family with order-one interior $Q$ and $Q\to0$ at both ends).

### What would be needed to rescue the assertion

The obstruction for $Q>0$ would require one of:

- an upper estimate for $\sup e$ expressed through the separator value $Q_C$ rather than the interior $Q_+$, so floor and ceiling share the same charge variable (flagged as missing in Step 91 §5 and Step 94 §4);
- a transport theorem tying $Q_+$ to $Q_C$ with a $Q$-independent constant, or a weighted geometry-coupled source-to-charge estimate of the type (4.9)/(8.6) in Step 94 with a length- and area-independent constant — Step 94 §6's redshift-taper benchmark shows no such constant follows from Maxwell conservation, both end values, the area equation, and finite separator charge alone;
- a demonstration that the twist forcing terms $2Q^2$ and the $Q$-dependent enlargement of $\|V\|_\infty$ are themselves absorbable, which the Step 89 (4.3) closure indicates they are not.

None of these is present. Consequently the Step 95 theorem stands only for $Q=0$, where it coincides with the already-established Step 87/88 result at $\delta_*\approx0.246$; for $Q>0$ its proof and its tabulated gaps do not support the stated conclusion, and its own upstream notes (89 §4, 91 §5, 94 §§4–6) contain the corrected picture in which the twist ceiling rises faster than the floor.