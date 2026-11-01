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

## Verification memo

### Conclusion

The horizontal Ricci contraction does contain \(+Qe\). However, the full twisted Bochner identity also contains the derivative of the twist-induced orbit-map tension. Its \(U\)-derivative contributes exactly \(-Qe\), canceling the apparent \(+Qe\) improvement. Therefore the Step 87 ceiling \(\mathcal B(\delta)\), which uses a tension bounded solely by \(O(\delta)\), does not extend to arbitrary twist by simply discarding \(+Qe\).

Thus the proposed all-twist theorem is not established by this proof chain. The supplied material also contains no global twisted connector exhibiting the opposite result, so the all-twist statement itself remains unresolved here.

### 1. What is correct in the Ricci calculation

Let
\[
A_{ij}=h_{\mathbb H^2}(U_i,U_j),\qquad e=\operatorname{tr}_{\gamma_B}A.
\]
The horizontal equation from Step 89 is
\[
\operatorname{Ric}_B-\operatorname{Hess}\sigma
=(-3+Q)\gamma_B+\frac12d\sigma^2+\frac12U^*h_{\mathbb H^2}+E_B .
\]
Consequently,
\[
(\operatorname{Ric}_B-\operatorname{Hess}\sigma):A
=(-3+Q)e
+\frac12|dU(\nabla\sigma)|^2
+\frac12\operatorname{tr}(A^2)
+E_B:A.
\]
Hence the direct curvature contribution is indeed
\[
(-3+Q)e,
\]
so the \(+Qe\) term is algebraically real.

Likewise, the finite-dimensional tensor used in the heat-kernel estimate is
\[
\operatorname{Ric}^4_\sigma
=\operatorname{Ric}_B-\operatorname{Hess}\sigma-\frac12d\sigma^2
=(-3+Q)\gamma_B+\frac12U^*h+E_B
\ge -(3+\delta)\gamma_B.
\]
Thus the same \(CD(-(3+\delta),4)\) heat-kernel estimate remains available.

### 2. The omitted Bochner term

The complete weighted Bochner formula is
\[
\begin{aligned}
\frac12Le={}&|DdU|^2
+\frac12|dU(\nabla\sigma)|^2
+\frac12\operatorname{tr}(A^2)+2\det A\\
&-3e+Qe+E_B:A
+\langle dU,D\tau_\sigma(U)\rangle .
\end{aligned}
\tag{1}
\]

For a twisted reduction, \(U\) is not merely forced by the Ricci defect. Step 94 gives
\[
\tau_\sigma(U)=-\nabla_UQ+Z=-Q\nabla\beta+Z,
\qquad |Z|\le 2\delta,
\tag{2}
\]
where \(Z\) is the vertical traceless defect and, for fixed charge \(q\),
\[
Q=e^{-3\sigma}F(U),\qquad
\operatorname{Hess}F=Fh_{\mathbb H^2}.
\]

Therefore the \(U\)-derivative of the twist source satisfies
\[
\operatorname{Hess}_UQ=Qh_{\mathbb H^2},
\]
and hence
\[
\sum_i
\left\langle U_i,
D_{U_i}(-\nabla_UQ)\right\rangle
=-Qe.
\tag{3}
\]
This cancels the \(+Qe\) in (1).

Including the explicit \(e^{-3\sigma}\) dependence, the exact fixed-charge calculation is
\[
\boxed{
\langle dU,D(-Q\nabla\beta)\rangle
=-Qe+3Q\langle d\sigma,d(\beta\circ U)\rangle .}
\tag{4}
\]
Thus the combination furnished by curvature and twist tension is
\[
Qe+\langle dU,D(-Q\nabla\beta)\rangle
=3Q\langle d\sigma,d(\beta\circ U)\rangle,
\]
whose sign is not fixed.

This is precisely the cancellation recorded in the supersession notice at the start of Step 89.

### 3. Why the OT resolvent ceiling does not follow

One may rewrite the tension term as
\[
\langle dU,D\tau_\sigma\rangle
=\operatorname{div}_\sigma V-|\tau_\sigma|^2,
\qquad
V(X)=\langle dU(X),\tau_\sigma\rangle.
\tag{5}
\]
In the OT calculation,
\[
\tau_\sigma=Z,\qquad |Z|\le2\delta,
\]
which gives
\[
|V|\le2\delta\sqrt e,\qquad |Z|^2\le4\delta^2.
\]
These two estimates are essential for the Step 87 formula \(\mathcal B(\delta)\).

With twist,
\[
\tau_\sigma=-Q\nabla\beta+Z,\qquad |\nabla\beta|=1,
\]
so only the \(Q\)-dependent estimates
\[
|\tau_\sigma|\le Q+2\delta,\qquad
|V|\le(Q+2\delta)\sqrt e
\tag{6}
\]
are immediately available. The resolvent divergence term then depends on \(Q_+=\sup Q\), and \(-|\tau_\sigma|^2\) also contributes a \(Q\)-dependent term. This is the source of the three-parameter ceiling displayed in Step 91 equation (5.1), rather than the OT ceiling \(\mathcal B(\delta)\).

Accordingly:

- Dropping \(+Qe\) by itself is algebraically permissible.
- After doing so, the twist tension terms in (5) remain.
- Replacing those terms by the OT estimates \(2\delta\sqrt e\) and \(4\delta^2\) is not permissible.

The statement that twist makes \(e\) decay at least as fast as in the OT system therefore does not follow.

There is also a literal linear-term mismatch in the proposed Step 1 formula. The OT reaction term is
\[
\frac12e^2-(3+\delta)e,
\]
equivalently
\[
\frac12e(e-6)-\delta e,
\]
not \(\frac12e(e-6)-(3+\delta)e\).

### 4. Separator floor

The minimal-separator identity remains valid:
\[
\langle e_s\rangle_C
=12-2\langle D\rangle_C
+2\langle|\mathrm{II}|^2\rangle_C
+\langle h_T^2\rangle_C,
\qquad |D|\le4\delta.
\]
Hence
\[
\langle e_s\rangle_C\ge12-8\delta.
\]
With twist, Step 91 gives
\[
|\mathrm{II}|^2
=\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q,
\]
so in fact
\[
\langle e_s\rangle_C\ge12-8\delta+2\langle Q\rangle_C.
\]
This part of the argument is sound. It yields a contradiction only after a suitable global upper estimate for \(e\), and the OT expression \(\mathcal B(\delta)\) is not such an estimate in the twisted system.

### 5. Conflict with the Step 95 JSON summary

The JSON statement that \(Q_C\le5\delta\) follows from a simple maximum principle conflicts with Step 94:

- \(LQ<0\) at a positive interior maximum is compatible with such a maximum.
- Step 94 explicitly withdraws the corresponding maximum-principle inference.
- Its charged Koiso germs have \(E=0\), strict separator stability, and \(Q>0\) locally.
- Its redshift-taper computation keeps order-one separator charge while making the physical mixed source exponentially small, although that model does not solve every reduced Einstein equation.

Thus no supplied derivation gives a \(\delta\)-only pointwise estimate for \(Q\).

### 6. Formulation issue

A closed four-manifold with a globally free action of the compact group \(T^2\) has compact quotient. Its quotient cannot be \(S^1\times\mathbb R\) with two complete ends. Step 88 instead concerns a complete noncompact extension whose quotient is cylindrical. If the intended object is a compact connector inside a closed manifold together with an auxiliary complete extension, those must be distinguished in the theorem statement.

In summary: the direct identity
\[
(\operatorname{Ric}_B-\operatorname{Hess}\sigma):U^*h
=(-3+Q)e+\text{positive-semidefinite terms}+E_B:A
\]
is correct, but the ensuing OT ceiling is not. The omitted twist-tension derivative cancels \(+Qe\) and leaves further \(Q\)-dependent transport terms.