# Step 94 route map: after the charge-sign correction

## Established this step

1. The diagonal algebra
   \[
   LQ=|dQ|^2/Q-18Q-4Q^2,
   \qquad L\log Q=-18-4Q
   \]
   is correct, but it gives no maximum bound. Negative drift Laplacian at a
   maximum is compatible with that maximum. The former Step 93 corollary and
   forced \(Q=O(\delta^2)\) expectation are withdrawn.

2. For fixed nonzero full two-component charge, if
   \(F=\frac12q^TM^{-1}q\), \(\beta=\log F\), then
   \[
   \operatorname{Hess}\beta=h-d\beta^2,
   \quad |d\beta|=1,
   \quad
   L\log Q=-18-4Q+e-|d(\beta\circ U)|^2.
   \]
   The extra transverse orbit energy is nonnegative and vanishes only in the
   charge-aligned diagonal reduction.

3. Liu's mixed Ricci law gives the exact physical source norm
   \[
   e^{-3\sigma}M^{ab}\langle dq_a,dq_b\rangle
   =4|E_{\rm mix}|_{\rm HS}^2.
   \]
   Exact OT on an open end plus exact Einstein still forces \(q=0\) on the
   connected exact region. Physical \(Q\to0\) alone does not.

4. The smooth two-ended redshift-taper benchmark imposes both OT end values,
   Maxwell transport, exact area equation, zero total charge flux, and fixed
   finite separator \(Q=1/2\), yet has
   \[
   \|b\|_\infty\asymp e^{-3\sqrt6R/2},
   \qquad
   \frac{\int w^2\rho}{\int b^2\rho}\asymp e^{2\sqrt6R}.
   \]
   Thus those ingredients cannot yield source-small charge or a length-uniform
   weighted Poincare inequality. The model is not a connector because it omits
   orbit-shape and horizontal equations.

5. Charged Koiso data now show that even nonzero twist is compatible with a
   fully stable minimal separator and all exact local Einstein constraints. For
   \(0<S<3\), choose \(|U_s|^2=12+2S\), fixed charge \(q\),
   \(P=S-Q>0\), vertical block \(B=\sqrt{P/2}M^{-1}dM(N)\), and mixed
   Weingarten covector \(m=-q/2\). Then \(|II|^2=P+Q=S\), all Cauchy constraints
   hold, and the full Jacobi lower bound is \(3-S>0\). Koiso gives a local
   charged Einstein germ. Hence no separator-local charge-vanishing theorem is
   possible.

6. The invariant horizontal Bianchi identity has been derived:
   \[
   2\operatorname{div}_\sigma H-d\operatorname{tr}H
   =-dT-Td\sigma-\langle Z,dU\rangle-m_q,
   \quad m_q=e^{-3\sigma}\langle M^{-1}q,dq\rangle.
   \]
   Its radial form is exactly \(C'=-2(u+h)C-wb\). The second matching moment is
   therefore the invariant charge-work pairing, not a radial artifact.

## Decisive remaining free-\(T^2\) question

The cost, if one exists, must come from the **joint** horizontal/orbit system and
stable separator across the two-dimensional quotient. Terminal OT matching
requires not only zero total charge change but also the adjoint charge-work
identity above. A monotone radial taper cannot satisfy both; a crude two-mode
sign-changing pilot did so only with a source about \(26\delta\), which is not a
lower bound.

The next constructor should exploit the derivative-free global pairing (also
symbolically recorded in `step94_horizontal_flux_pairing.py/.json`) obtained by
testing the Bianchi identity against an end-separating vector field \(X\):
\[
\int m_q(X)d\mu_\sigma=\int[2H:\operatorname{sym}\nabla X
-(\operatorname{tr}H)\operatorname{div}_\sigma X+T\operatorname{div}X
-\langle Z,dU(X)\rangle]d\mu_\sigma.
\]
Determine whether the full quotient geometry and separator stability provide a
uniformly controlled adjoint field and a sign/lower bound, or whether a
distributed sign-changing mixed source can make this pairing and the total
charge flux vanish while every Ricci block tends to zero. The redshift taper and
charged Koiso germ are adverse benchmarks: any proposed estimate must explain
both escapes.

This remains a restricted symmetry-class problem and does not settle graph
metrics without free \(T^2\), the positive branch, higher dimensions, or Yau 26.
A01's positive desingularization result is currently structural only for AA/BB
distinct-node same-chirality sectors; AB and the full self/deformation/complement
system remain unfinished.
