# Step 88 source note: twist scalars for a free/invariant \(T^2\) reduction

The focused external search for full variable-fibre Kaluza--Klein equations was
uneven, but it retrieved one directly useful primary source:

* Tianyue Liu, *Toric Einstein 4-manifolds with non-negative sectional curvature*,
  `Knowledge/objects/papers/Toric-Einstein-4-manifolds-with-non-negative-sectional-curvature--24d1f88fe098--1315c2a6cd67/object.md`,
  citation key `liutoric`.

On the principal stratum, Liu chooses quotient coordinates with
\(g_\Sigma=dx^2+\mu^2dy^2\), horizontal lifts \(X,Y\), and Killing fields
\(V_1,V_2\). The vertical bracket \([X,Y]\) measures failure of orthogonal
transitivity. The mixed Ricci components are written explicitly as
\[
 \operatorname{Ric}(Y,V_a)
 =\frac{\mu}{2\rho}\,\partial_x
   \left(\frac{\rho}{\mu}\langle[X,Y],V_a\rangle\right),
\]
\[
 \operatorname{Ric}(X,V_a)
 =-\frac{1}{2\mu\rho}\,\partial_y
   \left(\frac{\rho}{\mu}\langle[X,Y],V_a\rangle\right),
\]
where \(\rho=\sqrt{\det(g^\Omega_{ij})}\). Equivalently the twist scalars
\[
 \alpha_a:=\rho\left\langle[X,Y/\mu],V_a\right\rangle
\]
satisfy
\[
 \operatorname{Ric}(Z,V_a)=-\frac1{2\rho}\langle d\alpha_a,JZ\rangle.
\]
Thus exact Einstein equations make each \(\alpha_a\) constant. In Liu's closed
simply connected setting, singular orbit strata force those constants to vanish;
that latter step does not apply to our free cylindrical action. For exact open end
neighborhoods where \([X,Y]=0\), however, constancy likewise forces
\(\alpha_a=0\) globally on the connected principal region. This supports an
important distinction:

1. **Exact OT end on an open set + exact Einstein:** twist vanishes globally, so no
   separate exact-twist escape exists.
2. **Only asymptotically OT end:** \([X,Y]\to0\) need not imply
   \(\alpha_a\to0\), because the prefactor \(\rho\) grows; nonzero conserved twist
   may have decaying physical connection curvature.
3. **Approximate Einstein:** \(d\alpha_a\) is controlled by mixed Ricci defect only
   after retaining the \(\rho\) and frame factors. A long expanding region can
   accumulate substantial change despite small pointwise defect.

This source establishes the mixed conservation law. It does not, in the passages
read, provide all base and vertical Ricci blocks with variable \(G=e^\sigma M\) in
the Step 79 normalization. Those coefficients remain the next derivation before
using the TTCS-proposed modified Bochner inequality or any numerical twist
threshold.

Use as \cite{liutoric} when a formal citation is needed.
