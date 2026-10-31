# TTCS Independent Branch Record

```json
{
  "step_id": 32,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md",
    "Sessions/S1003A01/workspace/scripts/step32_ramified_transfer_law.py",
    "Sessions/S1003A01/workspace/data/step32/ramified_transfer_r05.json",
    "Sessions/S1003A01/workspace/data/perp_area/rigorous_x00.03_X128_d20.json",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/supplements/sources/20261004/step10_rigorous_subthreshold_cell_and_O11.md",
    "Skills/geometric-analysis/research/supplements/sources/20261004/step11_independent_review_O11_and_mixed_cost.md"
  ]
}
```

## Task

Independently verify the upper-construction and normalization part of the revised ramified KE transfer. Check the exact physical radius of the certified x0=.03, X=128 cell after scaling to Ric=-g; the fixed-buffer interpolation g_CH+chi(g_m-g_CH), its positivity and C^2/Ricci/volume/scalar estimates; how those errors enter the complete-cell formula at the Q=o(A) scale; the separated shrinking-handle contribution; integer rounding under Delta/Q→r∈[0,1); and the coefficient limsup alpha/h <= 4-(8 eta/9)(1-r), including the distinction between a diagonal smoothing sequence and a fixed reduced margin. Check also that the statement is only an upper construction law and not an optimality or r=1 transition theorem. Identify any missing quantifier or mismatch between the rigorous certificate and the geometric marked-ball hypothesis.

## Output

# Memo: upper construction and normalization in the ramified KE transfer (Step 31 / step32 script)

## 0. Summary

The upper construction holds as stated in its essentials:

- the radius,
- the interpolation estimates,
- the complete-cell accounting,
- the handle contribution,
- the rounding,
- the coefficient \(4-\tfrac{8\eta}{9}(1-r)\) for a single diagonal sequence.

Four points need correction or sharpening:

1. Positivity of the interpolated metric is automatic for every \(m\), not only for large \(m\).
2. Only the raw defect needs \(o(Q)\) total error. Volume and scalar errors need only \(O(Q)\), and no rate for \(\varepsilon_m\) is needed. The quadratic splice structure matters for a different, non-convergent statement.
3. The 9-digit bound \(3.996152073\) depends on the binary64 `upper` field, not on the printed Arb ball string.
4. The X=128 certificate has a provenance gap relative to the Step-11 strict-Arb standard. The profile admissibility of the degree-20 cell is not recorded in the supplied material.

## 1. Physical radius of the \(x_0=.03,\ X=128\) cell

The cell's exact-CH continuation is
\[
g_{CH}=\frac{dx^2}{4x(1+x)}+x\sigma_1^2+x\sigma_2^2+x(1+x)\sigma_3^2,\qquad \operatorname{Ric}=-6g .
\]

Substitute \(x=\sinh^2\rho\). Then \(dx=2\sinh\rho\cosh\rho\,d\rho\) and \(\sqrt{x(1+x)}=\sinh\rho\cosh\rho\), so \(dx/(2\sqrt{x(1+x)})=d\rho\). The metric becomes
\[
d\rho^2+\sinh^2\rho(\sigma_1^2+\sigma_2^2)+\sinh^2\rho\cosh^2\rho\,\sigma_3^2,
\]
which is CH of holomorphic sectional curvature \(-4\). The level \(x=0\) is the centre, so \(x=X\) is the geodesic sphere of radius \(\operatorname{arsinh}\sqrt X\).

Passing to \(\tilde g=6g\), which has \(\operatorname{Ric}=-\tilde g\), multiplies distances by \(\sqrt6\). This gives
\[
R_{128}=\sqrt6\,\operatorname{arsinh}\sqrt{128}=\sqrt6\,\log(\sqrt{128}+\sqrt{129})=2.449490\times3.121119=7.645126\ldots
\]
This matches the script value 7.64512629467772. The X=8 value is \(\sqrt6\log(\sqrt8+3)=4.3178\), as in Step 10.

The \(\operatorname{Ric}=-g\) normalization agrees with Biquard–Guenancia's \(\operatorname{Ric}=-\omega\). It also gives \(\operatorname{Vol}(g_m)=\tfrac12\int\omega^2=2\pi^2A_m\), which is the \(v_j^0\) of I54 (2.1). The scale invariance \(J_6(g)=\int|\operatorname{Ric}_{\tilde g}+\tilde g|^2dV_{\tilde g}\) is the Step-11 §2.4 computation.

**Quantifiers to make explicit.**

- The smoothed cell agrees with the C² certified profile for \(x\le X-\delta\) and is exact CH on \([X-\delta/2,X]\). All smoothing therefore lies inside the radius-\(R_{128}\) ball.
- The interpolation annulus is the buffer \([R_{128},R_{128}+b]\) with fixed \(b>0\).
- The residual-finiteness step must exclude lattice elements with \(d(p,\gamma p)\le 2(R_{128}+b)\), with the buffer included. The text's "twice the required marked radius" is correct only if "required" includes \(b\).
- The compact set on which \(\varepsilon_m=\|g_m-g_{CH}\|_{C^2(K)}\) is measured must contain the closed ball of radius \(R_{128}+b\). It must also lie in \(X^\circ\), away from the cusp divisors.

## 2. The background lifts

Step 31 asserts that all lifted marked balls carry the same discrepancy \(\varepsilon_m\). This is correct for the following reasons:

- \(X^\circ_m\to X^\circ\) is an unramified covering of the fixed preliminary quotient.
- The marked ball is simply connected, so it is evenly covered by \(d_m\) disjoint isometric copies.
- \(g_m\) on each copy is the pullback of the single downstairs conical metric \(\omega_{\beta_m}\) restricted to the ball.

So no thick-part counting is needed. The count \(d_m\asymp A_m\) follows from \(A_m/d_m=L^2+\sum_\lambda\beta_{m,\lambda}^2D_\lambda^2\to L^2\). This uses \(L\cdot D_\lambda=0\), and I verified the expansion.

Three hypotheses carry this step. They are attributed to Biquard–Guenancia and cannot be checked from the supplied files:

- **(i) Uniform ramification along each \(D_\lambda\).** Every component over \(D_\lambda\) must have the same index \(v_{m,\lambda}\); otherwise the pullback of a single cone angle is not smooth. This holds for Galois covers. Principal congruence \(\Gamma_m\subset\Gamma_*\), with \(\Gamma_*\) also principal congruence, is normal in \(\Gamma_*\).
- **(ii) Convergence in the vector parameter.** Convergence on compacta of \(X^\circ\) is needed as \(\max_\lambda\beta_{m,\lambda}\to0\), not only for a single common \(\beta\).
- **(iii) Smoothness of the pullback.** Smoothness for \(\beta=1/v\) exactly (BG §4.3).

The construction uses only qualitative convergence \(\varepsilon_m\to0\); see §4.

## 3. The interpolation \(g_{m,\rm ann}=g_{CH}+\chi(g_m-g_{CH})\)

**Positivity.** With \(0\le\chi\le1\), \(g_{m,\rm ann}=(1-\chi)g_{CH}+\chi g_m\) is a convex combination of two positive-definite tensors. It is positive for every \(m\), with no smallness required.

**Estimates on the fixed annulus.**

- C² closeness: \(\|g_{m,\rm ann}-g_{CH}\|_{C^2}\le C(\|\chi\|_{C^2})\,\varepsilon_m\).
- Ricci defect: \(\operatorname{Ric}+g\) is a smooth function of the 2-jet and vanishes at the CH jet, so it is \(O(\varepsilon_m)\) uniformly. Hence the raw annular defect is \(\int_{\rm ann}|\operatorname{Ric}+g|^2=O(\varepsilon_m^2)\).
- Volume and scalar: \(dV-dV_{CH}=O(\varepsilon_m)\) and \(s+4=O(\varepsilon_m)\).
- Uniformity: all constants depend only on \(b\), \(\chi\) and \(R_{128}\).

The inner subannulus continues the cell's exact CH collar, so the cell metric itself is used unchanged. Its defect is the certified \(J\), up to the smoothing change. There is no cross term between the cell defect and the background discrepancy. Outside, \(g_m\) is exactly Einstein.

## 4. How the errors enter the complete-cell formula

With exact Einstein background (\(s=-4\)), the I54 identities hold for arbitrary sites \(i\). Write \(t_i=\int_{C_i}(s+4)\) and let \(J_i\) be the raw defect of region \(i\) (cell plus annulus, or handle site). Then
\[
I=-4v+\textstyle\sum t_i,\qquad R=4v+\sum(J_i-2t_i),
\]
\[
\mathcal E=\frac{4\sum J_i-(\sum t_i)^2/v}{4v+\sum(J_i-2t_i)},\qquad v=2\pi^2A_m+V_{\rm err}.
\]

With \(\sum t_i=O(Q)\) and \(V_{\rm err}=O(Q)\), this gives
\[
\frac{\mathcal E}{h}=\frac{\sum J_i}{2\pi^2Q}+O(h).
\]
The \((\sum t)^2/v\) term contributes \(O(h^2)\), and the volume error contributes \(O(h)\) relative corrections.

**Consequences.**

- **Defect is the only binding error.** Only \(\sum J_i-(k J_1+32\pi^2\ell)=o(Q)\) is needed. Volume and scalar errors need only \(O(Q)\). The text's "\(o(Q)\)" for these is true but more than required.
- **No rate for \(\varepsilon_m\).** Even a linear per-site defect error \(O(\varepsilon_m)\), with no exact collar, would sum to \(k_mO(\varepsilon_m)=o(Q)\). The convergent family therefore needs no rate and no quadratic splice.
- **Where the quadratic structure does matter.** The exact CH collar is still needed to define a smooth glued metric with a known cell defect. Its quadratic error is what supports a stronger, transferable statement:
  - Take any closed Einstein surface with \(\operatorname{Ric}=-g\) containing at least \(k\) disjoint balls of radius \(R_{128}+b\) that are fixed-\(\varepsilon\) C²-close to CH, with \(k\) of the order required.
  - Such a surface carries the saving with margin \(\eta-C\varepsilon^2/(8\pi^2)\).
  - This holds without \(\varepsilon\to0\).

## 5. Separated shrinking handles

The coefficient \(16\ell/Q\) uses a per-handle cost \(32\pi^2+o_\rho(1)\) as the neck scale \(\rho\to0\). This is the Step-10 §5 accounting \(\tfrac79\cdot\tfrac{8\pi^2}{2\pi^2}\). The inherited construction was stated in CH lifts.

In \(g_m\) the cleanest justification reuses the device of §3:

1. Place each handle (two small balls joined by a neck) in its own lifted marked ball.
2. Interpolate that ball to exact CH on an interior region.
3. Perform the inherited CH shrinking construction there.

The handle site is then identical to the I54 case, with additional defect \(O(\varepsilon_m^2)\) and \(O(\varepsilon_m)\) volume and scalar errors. Because all sites have identical geometry, the per-handle error depends on \(\rho\) alone, so choosing \(\rho_m\to0\) gives \(\ell_m\,o_{\rho_m}(1)=o(Q)\).

Site count: cells plus handles use \(O(Q)=o(A)\le d_m\) lifts for large \(m\). The text's "aggregate errors \(o(Q_m)\)" is correct in this form.

## 6. Rounding under \(\Delta/Q\to r\in[0,1)\)

The real solution \(k=2(Q-\Delta)/9\), \(\ell=(7Q+2\Delta)/36\) gives \(T_+=A-Q\) and \(T_-=(A+Q)/3\). I verified this from \(\chi=\chi_X+k-2\ell\), \(\tau=\tau_X-k\) and \(4\chi_X-A=A/3+4\Delta/3\).

Rounding properties:

- Rounding changes \(k/Q\) and \(\ell/Q\) by \(O(1/Q)\to0\) and \(T_\pm\) by \(O(1)\). Hence \(U_{\rm top}=1+h+O(1/A)=1+h+o(h)\), using \(Q\to\infty\).
- Nonnegativity of \(k_m\) needs \(\Delta_m\le Q_m\) eventually. This follows from \(r<1\).
- The conditions \(\Delta=o(A)\) and \(Q=o(A)\) are compatible:
  - for \(r=0\), \(Q\asymp\sqrt{A\max(\Delta,1)}\) gives \(\Delta/Q\asymp\sqrt{\Delta/A}\to0\);
  - for \(r\in(0,1)\), \(Q\sim\Delta/r\) with \(\Delta\to\infty\) gives \(Q=o(A)\).

The script example is exact: \(16\cdot22222223-14\cdot11111112=2\times10^8=4\Delta\). Its coefficient 3.998076036 equals \(4-\tfrac{8\eta}{9}\cdot\tfrac12\).

The symbolic asserts are pure algebra. They do not test any geometric estimate.

## 7. The coefficient and the smoothing sequences

The algebra is correct:
\[
4(1-\eta)\frac{2(1-r)}9+16\frac{7+2r}{36}=4-\frac{8\eta}9(1-r).
\]

**Diagonal sequence.** The smoothing change is \(|J(g_\delta)-J(g)|\le C\delta^3\) (Step 10 §4). Choosing \(\delta_m\to0\), together with \(\varepsilon_m\to0\) and \(\rho_m\to0\), defines one sequence of manifolds \(M_m\); the topology is independent of \(\delta\). Along it,
\[
\limsup\frac{\alpha}{h}\le4-\frac89(1-r)\Bigl(1-\frac{J(g)}{8\pi^2}\Bigr)\le4-\frac{8\eta}{9}(1-r),
\]
with no "\(+\epsilon\)". This is the Step-11 sharpening of Step 10's per-\(\epsilon\) family.

**Fixed width.** A fixed width gives margin \(\eta_\delta\ge\eta-C\delta^3/(8\pi^2)\). This is not necessarily smaller than \(\eta\), since the \(O(\delta^3)\) change has no fixed sign. The same holds for a fixed nonsymmetric perturbation in §3 of the note: its margin is some \(\eta'>0\), possibly larger or smaller. The text's "\(\eta'<\eta\)" should read "a possibly different uniform margin \(\eta'>0\)." The openness argument itself, continuity of \(J\) in the C² topology for perturbations supported in a fixed compact set, is correct.

**Digits.** The boxed \(<3.996152073\) uses \(J_{\rm upper}=0.9956710815089548\). This gives \(4-8\eta/9=3.99615207245\), a margin of \(5.5\times10^{-10}\). The printed ball string \([0.99567\pm1.09\times10^{-6}]\) alone yields only \(J\le0.99567109\), hence \(4-8\eta/9\le3.9961520800\), which does not support the ninth digit.

Step 11 stated that the binary64 `lower`, `upper` and `eta_certified` fields are convenience values and that the ball is the proof object. The 9-digit statement therefore needs either:

- the Arb upper endpoint recorded exactly, as a full-precision string, outward-rounded; or
- the bound stated as \(<3.9961521\).

The float subtraction \(1-J_{\rm upper}\) is exact (Sterbenz). The open point is only whether `upper` was rounded outward from the Arb endpoint.

## 8. Certificate versus marked-ball hypothesis

- **(a) Provenance.** The cited file is `perp_area/rigorous_x00.03_X128_d20.json`, at 128 bits, degree 20, with radius about \(10^{-6}\). The Step-11 canonical certificate is `strict_rigorous_…` for X=8, after the float-mediated \(\phi\)-tail radius was replaced by a pure-Arb bound. The JSON records no script version or hash. It therefore does not establish that the X=128 run used the strict \(\phi\)-tail code. The margin \(\eta\approx4.3\times10^{-3}\) dwarfs the radius, so the open point is the trust base, not precision.
- **(b) Profile admissibility of the degree-20 cell.** The supplied material does not record admissibility for this cell. Step 10 §3 gives a structural argument for the degree-8 parametrization:
  - positivity through \(0\le S\le1\);
  - the exact constant-term shift enforcing \(q_F(0)+q_G(0)=0\), which gives a full-period bolt;
  - \(a_2^2-a_3^2=O(t^4)\);
  - third-order vanishing of the deviations at \(X\).

  This argument transfers verbatim only if the degree-20 cell uses the same form, with the shift applied to the corresponding coefficient. The certificate encloses the energy only; it does not encode these facts.
- **(c) The energy certified is that of the C² unsmoothed profile.** The upper construction uses smoothed cells, which is covered by §7.
- **(d) Background hypotheses.** The marked-ball hypothesis must refer to \(K\supseteq\overline{B}(R_{128}+b)\). The quantifiers on the covers (Galois, \(\max_\lambda\beta_{m,\lambda}\to0\), \(\Delta_m\to\infty\) when \(r>0\)) belong in the statement.

## 9. What the result is

This is an existential upper construction law over a chosen cover tower and chosen separated geometry. It contains no lower matching statement and no optimality in \(r\).

At \(r=1\), the balance forces \(k=0\) and \(\ell=\Delta/4\). The construction then gives coefficient exactly 4 with no saving. Pure-handle rigidity, \(\alpha=4h/(1+h)\), was proved on CH covers with \(\Delta=0\). It is not available here, so nothing is asserted at \(r=1\). For \(r>1\), the equal-chirality balance cannot be met with \(k\ge0\).

The saving \(\tfrac{8\eta}{9}(1-r)\) is linear in the blow-up fraction \(2(1-r)/9\), exactly as the cell-plus-separated-handle mechanism predicts. Handles carry no Weyl-depletion budget (Step 11 §4). The note's own wording, "construction law, not an optimality result and not a transition theorem at \(r=1\)," matches the mathematics.