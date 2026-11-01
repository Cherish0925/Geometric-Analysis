# TTCS Independent Branch Record

```json
{
  "step_id": 91,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md",
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md",
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/data/step91_flat_slice_and_stability.json"
  ]
}
```

## Task

Verify the following geometric claim about free-T² metrics with twist on a 4-manifold. Setting: (X⁴,g) complete, free isometric T²-action, g = γ_B + G_ab(dξ^a + A^a)(dξ^b + A^b), G = e^σ M with det M = 1, ρ = e^σ. Connection curvature F^a = dA^a = f^a vol(γ_B). Twist energy Q = (1/2)G_{ab}f^af^b. Orbit-shape map U: B → H² with e = |dU|². Defect E = Ric_g + 3g, ‖E‖_op ≤ δ.

Claim 1 (twist contribution to |II|²): Let Σ = π⁻¹(C) be an invariant hypersurface, C a curve in the base B with tangent T and normal ν. In the orthonormal frame {e_T, e₁, e₂, e_ν}, the second fundamental form satisfies:
  |II|² = |II|²_OT + Q
where |II|²_OT = κ² + (1/2)h_ν² + (1/2)e_ν (with κ = geodesic curvature, h_ν = ∂_ν σ, e_ν = |dU(ν)|²) and the twist contribution is Q through the off-diagonal terms II(e_T, e_a).

Verify: From the Kaluza-Klein/O'Neill formulas, II(e_T, e_a) = (1/2)G_{aa}^{1/2}f^a (in orthonormal orbit frame, for diagonal G). Then 2∑_a II(e_T,e_a)² = (1/2)G_{ab}f^af^b = Q.

Claim 2 (separator stability): If Σ is minimal and area-minimizing in its homology class, then ∫_Σ(|II|² + Ric(ν,ν))dvol ≤ 0 (second variation with φ=1). Since Ric(ν,ν) = -3 + E(ν,ν) ≥ -3 - δ:
  ⟨|II|²⟩_Σ ≤ 3 + δ
and hence Q_C := ⟨Q⟩_Σ ≤ 3 + δ.

Claim 3 (raised floor): The separator identity from Step 88 gives ⟨e_s⟩ = 12 - 2⟨D⟩ + 2⟨|II|²⟩ + ⟨h²⟩ where h = (log ρ)_T. With |II|² = |II|²_OT + Q, this becomes ⟨e_s⟩ ≥ 12 - 8δ + 2Q_C.

Claim 4 (resolvent-floor obstruction): At the exact OT threshold δ* ≈ 0.246 where the Step 87 ceiling B(δ*) = 12 - 8δ*, any Q_C > 0 would make the floor strictly exceed the ceiling, ASSUMING the ceiling still applies. However, the ceiling B(δ) was derived under Q=0 (exact OT). With Q>0, the Bochner identity is modified and the ceiling may increase. The key question is whether the ceiling increases faster or slower than the floor.

Please verify all four claims, check the O'Neill formula for II(e_T, e_a) carefully, and assess whether the resolvent-floor argument genuinely constrains Q_C or whether the modified ceiling with Q>0 invalidates it.

## Output

# Scientific verification memo

## Summary

1. The mixed second-fundamental-form calculation is correct in magnitude. Its sign depends on the orientation of \((T,\nu)\) and the horizontal-lift convention. With the standard norm,
   \[
   2\sum_{\alpha=1}^2 \mathrm{II}(T,e_\alpha)^2=Q.
   \]
   Consequently,
   \[
   |\mathrm{II}|^2
   =\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q.
   \]

2. A two-sided stable minimal separator satisfies
   \[
   \langle|\mathrm{II}|^2\rangle_\Sigma\le 3+\delta,
   \qquad Q_C\le 3+\delta.
   \]
   In fact,
   \[
   \left\langle\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q\right\rangle_\Sigma
   \le 3+\delta.
   \]
   Full area minimization among all hypersurfaces is stronger than needed: the weighted-length minimizer from Step 88 already supplies the constant normal variation used here.

3. The raised separator floor is exact:
   \[
   \langle e_s\rangle_C\ge 12-8\delta+2Q_C.
   \]

4. At \(\delta=\delta_*\), retaining the OT ceiling would force \(Q_C=0\). But that ceiling is not available once \(Q>0\). The supplied non-OT Bochner calculation introduces \(Q_+\), not merely \(Q_C\), and its current upper expression grows faster than the floor near \((\delta_*,Q)= (\delta_*,0)\). Thus the resolvent-floor combination presently gives no new estimate on \(Q_C\) beyond stability.

---

## 1. Mixed O’Neill component and the exact \(Q\) coefficient

Let \(K_a\) be the fundamental vertical fields and let \(\bar T,\bar\nu\) be invariant horizontal lifts. Write
\[
F^a(T,\nu)=\varepsilon f^a,\qquad
\varepsilon=\operatorname{vol}_{\gamma_B}(T,\nu)\in\{\pm1\}.
\]
For the connection convention \(d\xi^a+A^a\),
\[
[\bar T,\bar\nu]^{\mathcal V}
=-F^a(T,\nu)K_a=-\varepsilon f^aK_a.
\]
Koszul’s formula gives
\[
2g(\nabla_{\bar T}\bar\nu,K_a)
=g(K_a,[\bar T,\bar\nu])
=-\varepsilon G_{ab}f^b.
\]
Therefore
\[
\boxed{\mathrm{II}(\bar T,K_a)
=-\frac{\varepsilon}{2}G_{ab}f^b.}
\]
For diagonal \(G\) and \(e_a=K_a/\sqrt{G_{aa}}\),
\[
\mathrm{II}(\bar T,e_a)
=-\frac{\varepsilon}{2}\sqrt{G_{aa}}\,f^a.
\]
Thus the displayed positive sign in the question corresponds to \(\varepsilon=-1\), or to the opposite horizontal-bracket convention. Only this sign changes.

For a general orbit orthonormal frame \(e_\alpha=L_\alpha^{\,a}K_a\),
\[
\sum_{\alpha}\mathrm{II}(\bar T,e_\alpha)^2
=\frac14\,G_{ab}f^af^b.
\]
Since the tensor norm counts both symmetric positions \((T,e_\alpha)\) and \((e_\alpha,T)\),
\[
2\sum_\alpha\mathrm{II}(\bar T,e_\alpha)^2
=\frac12G_{ab}f^af^b=Q.
\]

The other components are independent of \(F\). With
\[
S_\nu=\frac12G^{-1}\partial_\nu G
=\frac12(h_\nu I+M^{-1}\partial_\nu M),
\]
and \(e_\nu=\frac12\operatorname{tr}(M^{-1}\partial_\nu M)^2\),
\[
|S_\nu|^2
=\frac12h_\nu^2+\frac12e_\nu.
\]
Also \(\mathrm{II}(T,T)=-\kappa\). Hence
\[
\boxed{
|\mathrm{II}|^2
=\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q.}
\]
The twist does not enter the mean curvature because the mixed components have zero trace.

---

## 2. Stability estimate

For a compact, two-sided stable minimal hypersurface,
\[
\int_\Sigma
\left(
|\nabla_\Sigma\phi|^2-
\bigl(|\mathrm{II}|^2+\operatorname{Ric}(\nu,\nu)\bigr)\phi^2
\right)d\mu_\Sigma\ge0.
\]
Taking \(\phi=1\),
\[
\int_\Sigma
\bigl(|\mathrm{II}|^2+\operatorname{Ric}(\nu,\nu)\bigr)d\mu_\Sigma
\le0.
\]
Since
\[
\operatorname{Ric}(\nu,\nu)=-3+E(\nu,\nu),
\qquad E(\nu,\nu)\ge-\delta,
\]
one gets
\[
\langle|\mathrm{II}|^2\rangle_\Sigma
\le3-\langle E(\nu,\nu)\rangle_\Sigma
\le3+\delta.
\]
Using the exact decomposition above,
\[
\boxed{
\left\langle
\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q
\right\rangle_\Sigma\le3+\delta.}
\]
In particular,
\[
\boxed{Q_C\le3+\delta,}
\qquad
\boxed{\langle e_\nu\rangle_C\le6+2\delta-2Q_C.}
\]

For the Step 88 separator, \(\Sigma\) was obtained by minimizing
\(\int_C\rho\,ds\) among essential base curves. This already makes the second variation nonnegative for invariant normal variations. The choice \(\phi=1\) is such a variation, so the displayed integral estimate does not require minimization against every non-invariant hypersurface.

---

## 3. Raised separator floor

The induced connection over the one-dimensional curve \(C\) can be removed locally by a torus translation. Its holonomy does not affect local scalar curvature. Thus the intrinsic identity remains
\[
\langle R_\Sigma\rangle_C
=\frac12\bigl(\langle h_T^2\rangle_C-\langle e_s\rangle_C\bigr),
\]
where \(h_T=(\log\rho)_T\), distinct from \(h_\nu=\partial_\nu\sigma\).

For a minimal hypersurface,
\[
R_\Sigma=-6+D-|\mathrm{II}|^2,
\qquad
D=\operatorname{tr}E-2E(\nu,\nu),
\qquad |D|\le4\delta.
\]
Therefore
\[
\langle e_s\rangle_C
=12-2\langle D\rangle_C
+2\langle|\mathrm{II}|^2\rangle_C
+\langle h_T^2\rangle_C.
\]
Substitution gives the more explicit identity
\[
\begin{aligned}
\langle e_s\rangle_C
={}&12-2\langle D\rangle_C
+2\langle\kappa^2\rangle_C
+\langle h_\nu^2\rangle_C\\
&+\langle e_\nu\rangle_C
+2Q_C+\langle h_T^2\rangle_C.
\end{aligned}
\]
All terms after \(D\) are nonnegative, hence
\[
\boxed{\langle e_s\rangle_C\ge12-8\delta+2Q_C.}
\]

This verifies that twist raises the separator energy floor by exactly \(2Q_C\).

---

## 4. What the resolvent comparison currently implies

If one additionally assumed the OT estimate
\[
\sup_Be\le\mathcal B(\delta),
\]
then
\[
12-8\delta+2Q_C
\le\langle e_s\rangle_C\le\sup_Be\le\mathcal B(\delta),
\]
so
\[
Q_C\le\frac{\mathcal B(\delta)-12+8\delta}{2}.
\]
At
\[
\delta_*=0.246249763690668\ldots,\qquad
\mathcal B(\delta_*)=12-8\delta_*
=10.0300018905\ldots,
\]
this would force \(Q_C=0\).

That implication is only conditional. The OT resolvent estimate used both \(F=0\) and the associated orbit equation. With twist,
\[
\tau_\sigma(U)=-\nabla_{\mathbb H^2}Q+Z,
\]
and the \(+Qe\) contribution from drift curvature cancels the \(-Qe\) contribution obtained by differentiating the target potential. The remaining Bochner terms include \(Q^2\), charge-gradient terms, and corresponding divergence fluxes. They are not controlled by \(\delta\) alone.

Under the same Green-kernel hypotheses and exact OT ends, the supplied Step 90 comparison has \(Q_-=0\) and reads
\[
12+2Q_C-8\delta
\le
\left[
\frac{2(Q_++2\delta)}{\sqrt{3+\delta}}
+
\sqrt{2(3+\delta)+
\frac{5(Q_++2\delta)^2}{3+\delta}}
\right]^2.
\]
At \(Q_+=0\) its right-hand side is \(\mathcal B(\delta)\). Writing that side as \(\mathcal B_{\rm tw}(\delta,Q_+)\),
\[
\left.\frac{\partial\mathcal B_{\rm tw}}{\partial Q_+}
\right|_{(\delta_*,0)}
\approx8.86.
\]
Even under the most favorable identification \(Q_+=Q_C\), the floor has derivative only \(2\). Thus the current modified upper expression grows faster than the floor near the OT crossing. Since generally
\[
Q_+\ge Q_C
\]
and stability controls only the separator average, the comparison becomes still weaker when twist is concentrated away from \(C\).

Accordingly, the established twist information is
\[
Q_C\le3+\delta,
\qquad
\sup_Be\ge12-8\delta+2Q_C.
\]
No further \(Q_C\) estimate follows from the OT resolvent formula. A stronger relation would require either an upper estimate for \(e\) expressed directly through \(Q_C\), or a geometric transport estimate connecting \(Q_+\) or the Green-kernel-weighted twist energy to \(Q_C\).

Finally, `step91_flat_slice_and_stability.json` contains one numerical inconsistency: the field `combined_constraints.at_delta_0246.step87_ceiling` is listed as `12.0`, whereas the same file’s resolvent table and formula give \(10.025139\) at \(\delta=0.246\). At \(\delta_*\), the common OT value is approximately \(10.030002\), not \(12\).