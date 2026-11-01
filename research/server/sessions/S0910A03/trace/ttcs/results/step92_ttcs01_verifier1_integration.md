# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 92,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step92_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step92_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify and sharpen the Step 92 separator analysis. Check the corrected contracted-Gauss sign; derive the full invariant second-variation inequality from the rho^2 gamma minimizing loop; conjugate the weighted Jacobi operator and verify the stated potential after substituting R_q=-2h_s-(3/2)h^2-e_s/2 and R_q=-6+D-|II|^2. Then assess the square-spike calculation: does stable J=-d^2+a-A 1_I on a periodic circle permit A→∞ with width ell→0 and A ell approaching 2 sqrt(a)tanh(sqrt(a)L/2)? State precisely what this proves and does not prove for geometric Q, including the role of variable rho and Maxwell/orbit equations. Seek any immediate rigorous concentration consequence stronger than the constant test, but reject unsupported regularity or scale assumptions.

## Integrated Scientific Memo

## Step 92 verification and sharpening

### 1. Contracted Gauss sign

For \(\Sigma^3\subset(X^4,g)\),
\[
R_q=R_g-2\operatorname{Ric}_g(\nu,\nu)+\mathcal H^2-|\mathrm{II}|^2.
\]
Writing \(E=\operatorname{Ric}_g+3g\) and
\[
D=\operatorname{tr}_gE-2E(\nu,\nu),
\]
gives
\[
\boxed{R_q=-6+D+\mathcal H^2-|\mathrm{II}|^2.}
\]
Hence on the minimal separator,
\[
\boxed{R_q=-6+D-|\mathrm{II}|^2\le -6+4\delta.}
\]
The corrected sign is therefore right. In
\[
R_q=-2h_s-\frac32h^2-\frac12e_s,
\]
the term \(-e_s/2\) helps produce the required negative intrinsic curvature. Minimality is \(\mathcal H=0\), not \(\partial_r\mathcal H=0\).

The flat-slice consequence also checks: if \(R_q=0\), then
\[
\mathcal H^2-|\mathrm{II}|^2=6-D.
\]
Since \(|\mathrm{II}|^2\ge \mathcal H^2/3\),
\[
\boxed{\mathcal H^2\ge 9-6\delta.}
\]
Thus a flat torus slice cannot be minimal for \(\delta<3/2\).

### 2. Full invariant second variation

Let \(C\) minimize
\[
\int_C\rho\,ds=\operatorname{Length}_{\rho^2\gamma_B}(C)
\]
in its essential class, and let \(\Sigma=\pi^{-1}(C)\). Every sufficiently small normal variation of \(C\) stays in that class, so the minimizing property gives nonnegative second variation for every smooth periodic invariant speed \(\phi(s)\). Since
\[
d\mu_\Sigma=\rho\,ds\,d\xi^1d\xi^2,\qquad
|\nabla_\Sigma\phi|^2=(\phi_s)^2,
\]
one obtains
\[
0\le \int_C\rho\left[(\phi_s)^2-
\bigl(\operatorname{Ric}(\nu,\nu)+|\mathrm{II}|^2\bigr)\phi^2\right]ds.
\]
Therefore, with
\[
V:=|\mathrm{II}|^2
=\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q,
\qquad
a:=3-E(\nu,\nu),
\]
\[
\boxed{\int_C\rho V\phi^2\,ds
\le\int_C\rho\bigl[(\phi_s)^2+a\phi^2\bigr]ds.}
\]
Equivalently,
\[
\boxed{J=-\rho^{-1}(\rho\,\partial_s)'+a-V\ge0}
\]
as a periodic quadratic form.

This proves stability only for invariant speeds; full stability against torus-dependent variations is neither needed nor established by the minimizing-loop argument. The connection along a one-dimensional curve affects only translational holonomy and does not alter the local volume reduction.

The constant test gives
\[
\langle V\rangle_\rho\le 3+\delta,\qquad
\langle Q\rangle_\rho\le3+\delta.
\]

### 3. Conjugation and exact potential

Put \(\rho=e^\sigma\), \(h=\sigma_s\), and \(y=e^{\sigma/2}\phi\). Then
\[
e^{\sigma/2}J(e^{-\sigma/2}y)
=-y_{ss}+
\left(a-V+\frac12h_s+\frac14h^2\right)y.
\]
Using
\[
R_q=-2h_s-\frac32h^2-\frac12e_s
\]
gives
\[
\frac12h_s+\frac14h^2
=-\frac14R_q-\frac18h^2-\frac18e_s.
\]
At the minimal separator, \(R_q=-6+D-V\), hence the Schrödinger potential is
\[
\boxed{
W=
\frac92-E(\nu,\nu)-\frac14D
-\frac34V-\frac18e_s-\frac18h^2.}
\]
Thus the coefficient of \(V\) is \(-3/4\), not \(-1\). There is no favorable pointwise cancellation.

It is useful to define
\[
c_E:=\frac92-E(\nu,\nu)-\frac14D
=\frac92-\frac14\sum_{i=1}^3E(e_i,e_i)-\frac34E(\nu,\nu).
\]
The operator-norm bound yields the sharper estimate
\[
\boxed{\frac92-\frac32\delta\le c_E\le\frac92+\frac32\delta.}
\]
The transformed form is therefore
\[
\boxed{
\int_C\left[\frac34V+\frac18(e_s+h^2)\right]y^2ds
\le\int_C\left[(y_s)^2+c_Ey^2\right]ds.}
\]

### 4. Immediate concentration bounds

The natural sharp statement is a capacity bound. For an arc \(I\subset C\),
\[
\boxed{
\int_I\rho V\,ds
\le
\inf_{\substack{\phi\in H^1_{\rm per}(C)\\ \phi\ge1\ {\rm on}\ I}}
\int_C\rho\bigl[(\phi_s)^2+a\phi^2\bigr]ds.}
\]
The same holds with \(Q\) because \(0\le Q\le V\). This is strictly stronger than the constant test, but remains a mass—not height—estimate.

For constant \(\rho=1\), constant \(a>0\), circle length \(L\), and an interval of length \(\ell\), the exact capacity is
\[
\boxed{
\operatorname{Cap}_a(I_\ell)
=a\ell+2\sqrt a\,
\tanh\!\left(\frac{\sqrt a(L-\ell)}2\right).}
\]
Hence
\[
\int_{I_\ell}V\,ds
\le a\ell+2\sqrt a\,
\tanh\!\left(\frac{\sqrt a(L-\ell)}2\right).
\]
Unlike the tent estimate, this stays finite as \(\ell\downarrow0\).

The conjugated form also gives a \(\rho\)-independent estimate. With
\[
b_\delta=\frac92+\frac32\delta,
\]
\[
\boxed{
\int_{I_\ell}Q\,ds\le\int_{I_\ell}V\,ds
\le\frac43\left[
b_\delta\ell+
2\sqrt{b_\delta}\tanh\!\left(
\frac{\sqrt{b_\delta}(L-\ell)}2\right)\right].}
\]
In particular,
\[
\int_CV\,ds\le (6+2\delta)L.
\]
These estimates impose a height–width tradeoff on plateaus but no pointwise ceiling or universal minimum width.

### 5. Square-spike model

For
\[
J_A=-\frac{d^2}{ds^2}+a-A\mathbf1_I
\]
on a periodic circle of length \(L\), \(|I|=\ell\), let
\[
\mu=\sqrt a,\qquad k=\sqrt{A-a},\qquad d=L-\ell.
\]
At zero energy the monodromy trace is
\[
T(A)=2\cosh(\mu d)\cos(k\ell)
+\sinh(\mu d)\left(\frac{\mu}{k}-\frac{k}{\mu}\right)\sin(k\ell).
\]
The first solution of \(T(A)=2\) is the threshold \(A_{\rm crit}(\ell)\) at which the lowest periodic eigenvalue reaches zero; monotonicity in \(A\) gives stability for \(A\le A_{\rm crit}(\ell)\).

If \(A\ell\to\alpha\), expansion of the trace equation gives
\[
2\cosh(\sqrt aL)-\frac{\alpha}{\sqrt a}\sinh(\sqrt aL)=2,
\]
so
\[
\boxed{
A_{\rm crit}(\ell)\ell\longrightarrow
2\sqrt a\,\tanh\!\left(\frac{\sqrt aL}{2}\right).}
\]
Consequently,
\[
A_{\rm crit}(\ell)\sim
\frac{2\sqrt a\,\tanh(\sqrt aL/2)}{\ell}\to\infty.
\]
Thus stable operators with \(A\to\infty\), \(\ell\to0\), and bounded nonzero mass \(A\ell\) do exist. Taking a fixed fraction below threshold gives strict stability and allows smoothing of the square well without changing the conclusion.

For \(a=3,L=2\pi\), the limiting mass is
\[
2\sqrt3\,\tanh(\sqrt3\pi)\approx3.46397,
\]
not exactly \(2\sqrt3\), though the difference is tiny.

### 6. Exact geometric meaning

The spike calculation proves only that the isolated one-dimensional Jacobi inequality is compatible with arbitrarily tall, narrow spikes of its potential. It proves:

* no finite \(\sup V\) or \(\sup Q\) bound follows from stability alone;
* no dimension-only concentration length follows;
* stability does impose finite weighted and unweighted capacity bounds on local mass.

It does **not** construct a geometric \(Q\)-spike. Geometrically,
\[
V=\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q
\]
and the Gauss identity couples \(V\) to the weight:
\[
\boxed{
h_s=3-\frac12D+\frac12V-\frac34h^2-\frac14e_s.}
\]
Thus a tall \(V\)-spike forces corresponding rapid variation of \(h=(\log\rho)_s\), unless balanced by \(e_s\). The free square-well model omits this back-reaction.

Moreover, under the charge normalization recorded in the source,
\[
q_a=\rho G_{ab}*F^b,\qquad
Q=\frac1{2\rho^2}G^{ab}q_aq_b.
\]
In the exact Einstein case the Maxwell equation makes \(q_a\) constant; a \(Q\)-spike must then arise through concentration of \(\rho^{-2}G^{-1}\). With Ricci defect, the mixed equation has a source involving mixed components of \(E\). Neither a quantitative transport estimate for \(q_a\) nor uniform ellipticity/modulus bounds for \(\rho,G\) are supplied here. The orbit-shape equation simultaneously couples \(G\), \(e_s\), and twist stress.

Therefore smoothness of each individual metric cannot be promoted to a uniform regularity scale across a family. The strongest justified Step 92 conclusion is capacity/local-mass control. Any pointwise control of geometric \(Q\), or any relation between separator \(Q_C\) and an interior maximum \(Q_+\), requires new Maxwell/orbit-equation transport or regularity estimates.