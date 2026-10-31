# TTCS Independent Branch Record

```json
{
  "step_id": 6,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step5_slice_charge_and_zero_flux.md",
    "Sessions/S1003A01/workspace/scripts/transgression_triaxial.py",
    "Sessions/S1003A01/workspace/scripts/perp_dual_cost.py",
    "Sessions/S1003A02/workspace/scripts/o11_perp_cell.py",
    "Sessions/S1003A02/workspace/notes/step8_first_order_cell_law_ASD_Qprinciple.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md"
  ]
}
```

## Task

Develop the strongest viable analytic mechanism for the perpendicular fixed-slot diagonal Bianchi-IX O11 cell. The bolt-adapted transgression has T/8π²=Y²+Pi, with Y=-1 and Pi=0 at the O(-1) bolt, while on the complex-hyperbolic collar the charge transfers to Pi and Y=0. Numerical near-minimizers make T dip close to zero before Pi grows to the collar charge, and P and J remain slightly above 8π². Seek an exact boundary/interior decomposition or variational inequality that controls this charge transfer by trace-free Ricci energy P or by J; include the scalar-deviation distinction J=P+(1/4)∫(s+24)^2. Use cohomogeneity-one geometry, Chern–Weil transgression, flux/defect variables, Hamiltonian completion of squares, or calibration ideas as appropriate. Formulate explicit candidate inequalities and say which can plausibly be proved from the existing variables, rather than generic suggestions.

## Output

## 1. Put the transgression into spin-connection coordinates

Write the bolt-adapted metric as
\[
g=dt^{2}+a^{2}\sigma _1^{2}+b^{2}\sigma _2^{2}+c^{2}\sigma _3^{2},
\qquad d\sigma_i=2\sigma_j\wedge\sigma_k .
\]
For the perpendicular fixed-slot ansatz,
\[
a=\sqrt x,\qquad b=\sqrt{x\,e^{w(x)}},\qquad c=\sqrt{F(x)},
\qquad dt=\frac{dx}{2\sqrt G}.
\]
Let \(\varpi=\frac12\log(a/b)=-w/4\). Define
\[
u_1=e^{\varpi}p_+,\qquad
u_2=e^{-\varpi}p_-,\qquad
u_3=Y-\frac12p_+p_- .
\]
Then the slice charge becomes the cubic Chern–Simons polynomial
\[
\boxed{
C(u):=\frac{\mathcal T}{8\pi ^2}
=u_1^2+u_2^2+u_3^2+u_1u_2u_3 .
}
\tag{1.1}
\]
Indeed,
\[
u_3^2+u_1u_2u_3
=Y^2-\frac14(p_+p_-)^2,
\]
so (1.1) is exactly \(Y^2+\Pi\).

These \(u_i\) are, up to the fixed orientation convention, the coefficients of the self-dual Levi–Civita connection. They also have the direct metric expression
\[
\boxed{
u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k}.
}
\tag{1.2}
\]
In the fixed-slot variables this gives
\[
\begin{aligned}
u_1={}&\sqrt{\frac Gx}
-\frac{xe^w+F-x}{\sqrt{x e^wF}},\\
u_2={}&e^{w/2}\sqrt{\frac Gx}(1+xw_x)
-\frac{x+F-xe^w}{\sqrt{xF}},\\
u_3={}&\sqrt{\frac GF}\,F_x
-\frac{x+xe^w-F}{xe^{w/2}}.
\end{aligned}
\tag{1.3}
\]
The two endpoint states are especially simple:
\[
u_{\rm bolt}=(0,0,-1),\qquad
u_{\rm CH}(x)=(0,3x,0).
\tag{1.4}
\]
Thus \(C=1\) at the \(\mathcal O(-1)\) bolt, while \(C=9x^2\) on the complex-hyperbolic collar. The observed charge transfer is literally a path in \(u\)-space from the \(u_3\)-axis to the \(u_2\)-axis, passing close to the origin.

Set
\[
H_i=u_i+\frac12u_ju_k,\qquad
\lambda_i=\frac{a_ja_k}{a_i}.
\tag{1.5}
\]
Then
\[
C'(t)=2\sum_iH_i\dot u_i.
\tag{1.6}
\]
Introduce the radial and tangential spin-curvature components
\[
r_i=\frac{\dot u_i}{a_i},\qquad
v_i=\frac{2H_i}{a_ja_k}.
\tag{1.7}
\]
A direct curvature-operator calculation gives the exact identities
\[
\boxed{
|\operatorname{Ric}^{\circ}|^2=\sum_i(r_i-v_i)^2,
\qquad
\frac{s^2}{12}+4|W^+|^2=\sum_i(r_i+v_i)^2,
\qquad
s=-2\sum_i(r_i+v_i).
}
\tag{1.8}
\]
Moreover,
\[
C'=abc\sum_i r_iv_i.
\tag{1.9}
\]
Consequently, for a slice at \(t=\rho\),
\[
\boxed{
\frac{P([0,\rho])}{8\pi^2}
=1-C(\rho)
+\frac1{8\pi^2}\int_{[0,\rho]}
\left(\frac{s^2}{12}+4|W^+|^2\right)dV .
}
\tag{1.10}
\]
Likewise,
\[
\boxed{
\frac{J([0,\rho])}{8\pi^2}
=1-C(\rho)
+\frac1{8\pi^2}\int_{[0,\rho]}
\left[
\frac{(s+18)^2}{3}+36+4|W^+|^2
\right]dV .
}
\tag{1.11}
\]
Equation (1.10) is the exact slice/interior Chern–Weil decomposition for \(P\); (1.11) records the extra scalar cost in \(J\).

---

## 2. A relative Chern–Simons calibration that removes the outgoing CH charge

From (1.7),
\[
\boxed{
\frac{P}{8\pi^2}
=\int
\sum_{i=1}^3
\frac{\lambda_i}{4}
\left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt .
}
\tag{2.1}
\]
The ordinary topological completion using \(C\) only measures the drop \(1-C_{\min}\). It misses the residual \(C_{\min}\). The perpendicular geometry supplies a better calibration: subtract the charge carried freely along the outgoing CH axis,
\[
\Phi(u)=C(u)-u_2^2
=u_1^2+u_3^2+u_1u_2u_3.
\tag{2.2}
\]
Equivalently, in the original variables,
\[
\boxed{
\Phi
=Y^2+e^{2\varpi}p_+^2-\frac14(p_+p_-)^2.
}
\tag{2.3}
\]
It has the desired endpoint values
\[
\Phi_{\rm bolt}=1,\qquad \Phi_{\rm CH}=0,
\tag{2.4}
\]
even though \(C_{\rm CH}=9x^2\).

Since
\[
\Phi_{u_1}=2H_1,\qquad
\Phi_{u_3}=2H_3,\qquad
\Phi_{u_2}=u_1u_3,
\]
Hamiltonian completion gives the exact identity
\[
\boxed{
\begin{aligned}
\frac{P}{8\pi^2}-1
=\int\Bigg[
&\frac{\lambda_1}{4}
 \left(\dot u_1+\frac{2H_1}{\lambda_1}\right)^2
+\frac{\lambda_3}{4}
 \left(\dot u_3+\frac{2H_3}{\lambda_3}\right)^2\\
&+\frac{\lambda_2}{4}
 \left(\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2}\right)^2
+\frac{2u_1u_2u_3}{\lambda_2}
\Bigg]dt .
\end{aligned}
}
\tag{2.5}
\]
This is the most useful exact decomposition for the perpendicular cell.

Its geometry is transparent:

* \(u_1,u_3\) follow the reversed spin-Einstein flow and die toward the nearly flat slice.
* \(u_2\) follows the forward spin-Einstein flow and becomes \(3x\) on the CH collar.
* The exact CH branch makes every square in (2.5) vanish.
* The sole signed interaction is
  \[
  \frac{2u_1u_2u_3}{\lambda_2}
  =\frac{2(p_+p_-)\left(Y-\frac12p_+p_-\right)}{\lambda_2}.
  \tag{2.6}
  \]

Hence the following is immediate.

### Sign-chamber theorem

If
\[
u_1u_2u_3\ge0
\tag{2.7}
\]
throughout the cell, then
\[
\boxed{P\ge8\pi^2,\qquad J\ge8\pi^2.}
\tag{2.8}
\]
This requires no estimate of \(C_{\min}\), no zero of \(Y\), and no smallness assumption. In the original variables, (2.7) is
\[
(p_+p_-)\left(Y-\frac12p_+p_-\right)\ge0.
\tag{2.9}
\]

For arbitrary sign, the entire fixed-slot problem is reduced exactly to
\[
\boxed{
\int\!\left[
\frac{\lambda_1}{4}\left(\dot u_1+\frac{2H_1}{\lambda_1}\right)^2
+\frac{\lambda_3}{4}\left(\dot u_3+\frac{2H_3}{\lambda_3}\right)^2
+\frac{\lambda_2}{4}\left(\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2}\right)^2
\right]dt
\ge
2\int\frac{(-u_1u_2u_3)_+}{\lambda_2}\,dt .
}
\tag{2.10}
\]
Unlike an estimate involving only \(\min C\), (2.10) retains exactly the orientation-transfer mode.

The near-minimizers have the expected broken-flow structure:
\[
(0,0,-1)\longrightarrow(0,0,0)\longrightarrow(0,3x,0).
\]
The first leg pays one unit of \(P/(8\pi^2)\); the second is Einstein and pays zero. A smooth finite-scale interpolation produces the observed second-order excess.

---

## 3. The remaining signed interaction is a \(2\times2\) Sturm problem

On the outgoing branch, regard \(u_2\) and the radii as a background and set
\[
\eta=\binom{u_1}{u_3},\qquad
\Lambda=\begin{pmatrix}\lambda_1&0\\0&\lambda_3\end{pmatrix},
\qquad
A=\begin{pmatrix}1&u_2/2\\u_2/2&1\end{pmatrix}.
\]
The first, third, and cubic terms of (2.5) form
\[
\mathcal Q_\perp(\eta)
=
\int\left[
\frac14\bigl(\dot\eta+2\Lambda^{-1}A\eta\bigr)^T
\Lambda
\bigl(\dot\eta+2\Lambda^{-1}A\eta\bigr)
+\eta^TB\eta
\right]dt,
\tag{3.1}
\]
where
\[
B=\begin{pmatrix}
0&u_2/\lambda_2\\
u_2/\lambda_2&0
\end{pmatrix}.
\]
After integration by parts,
\[
\mathcal Q_\perp
=
\left[\frac12\eta^TA\eta\right]
+\int\left[
\frac14\dot\eta^T\Lambda\dot\eta
+\eta^T
\left(A\Lambda^{-1}A+B-\frac12\dot A\right)\eta
\right]dt .
\tag{3.2}
\]
Thus the all-profile estimate is a matrix Hardy inequality, not a scalar Chern–Weil estimate.

A particularly concrete proof form is obtained from a symmetric matrix \(K(t)\):
\[
V-K\Lambda^{-1}K+\frac12\dot K\succeq0,
\qquad
V=A\Lambda^{-1}A+B-\frac12\dot A.
\tag{3.3}
\]
Then
\[
\mathcal Q_\perp
=
\left[\frac12\eta^T(A-K)\eta\right]
+\int\left[
\frac14
(\dot\eta+2\Lambda^{-1}K\eta)^T
\Lambda
(\dot\eta+2\Lambda^{-1}K\eta)
+\eta^T
\left(V-K\Lambda^{-1}K+\frac12\dot K\right)\eta
\right]dt .
\tag{3.4}
\]
A positive matrix supersolution \(K\), together with the explicit endpoint quadratic form, proves (2.10). All coefficients are functions of \(F,G,w\) and their first derivatives.

On an exact CH segment,
\[
\lambda_1=\lambda_3=\sqrt{x(1+x)},\qquad
\lambda_2=\sqrt{\frac{x}{1+x}},\qquad
u_2=3x.
\]
With \(v_\pm=u_1\pm u_3\), compactly supported transverse modes diagonalize:
\[
\begin{aligned}
\mathcal Q_+
&=\int\left[
\frac{x(1+x)}4(v_+')^2
+\frac{4+18x+15x^2}{16x(1+x)}\,v_+^2
\right]dx,\\
\mathcal Q_-
&=\int\left[
\frac{x(1+x)}4(v_-')^2
+\frac{4-18x+3x^2}{16x(1+x)}\,v_-^2
\right]dx.
\end{aligned}
\tag{3.5}
\]
Only the \(v_-\) channel has a coefficient that changes sign. This is the exact analytic representative of the perpendicular, first-order-free mode. A weighted Hardy estimate for \(\mathcal Q_-\), or equivalently a positive solution of its scalar Riccati equation, is therefore the sharp local ingredient. Pointwise positivity is too strong and misses the actual mechanism.

The same matrix form applies in the transition region with unequal \(\lambda_1,\lambda_3\). It is substantially more plausible than attempting to control \(\Pi\) directly, because it uses the differential cost of rotating charge between spin-connection axes.

---

## 4. The scalar contribution in \(J\) and an explicit strengthened completion

From (1.8),
\[
\boxed{
\frac{J-P}{8\pi^2}
=
\frac14\int abc
\left[
\sum_i\left(
\frac{\dot u_i}{a_i}+\frac{2H_i}{a_ja_k}
\right)-12
\right]^2dt .
}
\tag{4.1}
\]
Combining this with (2.5) gives
\[
\boxed{
\begin{aligned}
\frac{J}{8\pi^2}-1
=\int\Bigg[
&\frac{\lambda_1}{4}
 \left(\dot u_1+\frac{2H_1}{\lambda_1}\right)^2
+\frac{\lambda_3}{4}
 \left(\dot u_3+\frac{2H_3}{\lambda_3}\right)^2\\
&+\frac{\lambda_2}{4}
 \left(\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2}\right)^2
+\frac{2u_1u_2u_3}{\lambda_2}\\
&+\frac{abc}{4}
\left[
\sum_i\left(
\frac{\dot u_i}{a_i}+\frac{2H_i}{a_ja_k}
\right)-12
\right]^2
\Bigg]dt .
\end{aligned}
}
\tag{4.2}
\]
Thus \(J\) has a rank-one coercive term absent from \(P\).

The velocities \(\dot u_i\) can be minimized pointwise in the sum of the three mixed-flow squares and the scalar square. Because
\[
\lambda_i a_i^2=abc,
\]
the Schur complement is especially simple:
\[
\boxed{
\frac{J}{8\pi^2}-1
\ge
\int abc\left[
(y-3)^2+2zy
\right]dt,
}
\tag{4.3}
\]
where
\[
y=\frac{u_2}{a_1a_3},\qquad
z=\frac{u_1u_3}{a_1a_3}.
\tag{4.4}
\]
On the exact CH branch, \(y=3\) and \(z=0\), so equality occurs in the local elimination. Formula (4.3) gives a direct scalar-assisted theorem whenever
\[
\int abc\bigl[(y-3)^2+2zy\bigr]\,dt\ge0.
\tag{4.5}
\]
The sharper exact target, retaining all derivative information, is
\[
\begin{aligned}
\int\Bigg[
&\sum_i\frac{\lambda_i}{4}(\dot u_i-\beta_i)^2
+\frac{abc}{4}
\left(
\sum_i\left[\frac{\dot u_i}{a_i}+\frac{2H_i}{a_ja_k}\right]-12
\right)^2
\Bigg]dt\\
&\hspace{35mm}\ge
2\int\frac{(-u_1u_2u_3)_+}{\lambda_2}\,dt,
\end{aligned}
\tag{4.6}
\]
with
\[
\beta_1=-\frac{2H_1}{\lambda_1},\qquad
\beta_3=-\frac{2H_3}{\lambda_3},\qquad
\beta_2=\frac{2u_2-u_1u_3}{\lambda_2}.
\]
Equation (4.6) is the natural \(J\)-version of (2.10). It also makes clear why a proof for \(J\) need not imply the corresponding statement for \(P\).

---

## 5. Enlarged Hamilton–Jacobi formulation using torsion-freeness

The \(u_i\) are not arbitrary invariant connection coefficients. Equation (1.2) imposes
\[
\dot a_i=u_i+\gamma_i(a),\qquad
\gamma_i(a)=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k}.
\tag{5.1}
\]
This extra relation is precisely what can control the signed cubic in the full class.

For any function \(B(a,u)\), completion of (2.1) gives
\[
\frac{P}{8\pi^2}
=
B_{\rm bolt}-B_{\rm CH}
+\int\left[
\sum_i\frac{\lambda_i}{4}
\left(
\dot u_i-\frac{2(H_i-B_{u_i})}{\lambda_i}
\right)^2
+\mathcal R_B
\right]dt,
\tag{5.2}
\]
where
\[
\boxed{
\mathcal R_B
=
\nabla_aB\cdot(u+\gamma)
+\sum_i
\frac{B_{u_i}(2H_i-B_{u_i})}{\lambda_i}.
}
\tag{5.3}
\]
Thus a relative calibration with
\[
B_{\rm bolt}=1,\qquad B_{\rm CH}=0,\qquad \mathcal R_B\ge0
\tag{5.4}
\]
proves \(P\ge8\pi^2\).

The basic choice \(B_0=C-u_2^2\) gives
\[
\mathcal R_{B_0}=\frac{2u_1u_2u_3}{\lambda_2}.
\tag{5.5}
\]
A concrete first correction is
\[
\psi(a,u)=-\frac{a_2^2}{a_1a_3}\,u_1u_3.
\tag{5.6}
\]
Its \(a_2\)-transport term satisfies
\[
\psi_{a_2}u_2
=-\frac{2u_1u_2u_3}{\lambda_2},
\tag{5.7}
\]
so it cancels the cubic in (5.5) exactly. The remaining terms in \(\mathcal R_{B_0+\psi}\) are explicit quadratic and quartic expressions involving \(u_1,u_3\), the anisotropy of \(a_i\), and the mixed-flow squares. The raw factor in (5.6) must be matched to the smooth bolt expansion; a version localized to the transfer annulus preserves both endpoint values. This gives a concrete algebraic route to a full sum-of-squares identity, rather than an unspecified search for another flux.

---

## 6. Strongest theorem shapes supported by the present variables

The exact representation above supports three increasingly broad statements.

1. **Direct chamber result.**
   \[
   (p_+p_-)\left(Y-\frac12p_+p_-\right)\ge0
   \quad\Longrightarrow\quad
   P\ge8\pi^2,\ J\ge8\pi^2.
   \]
   This follows immediately from (2.5).

2. **Matrix Hardy result.**  
   The all-profile trace-free estimate is exactly the \(2\times2\) Sturm inequality (3.1), together with the third mixed-flow square. Its CH model reduces to the explicit scalar forms (3.5). A positive matrix Riccati supersolution proves the estimate on any coefficient class described by inequalities on \(F,G,w\).

3. **Torsion-free calibration result.**  
   A function \(B(a,u)\) satisfying (5.4) proves the full fixed-slot theorem. The basic relative Chern–Simons function \(C-u_2^2\) already removes the entire CH collar charge; only the cubic interaction remains. Formula (5.7) identifies an \(a\)-dependent correction that cancels that interaction at leading algebraic order.

The stored profiles already contain all quantities needed to distinguish these mechanisms: \(u_1u_2u_3\), the three mixed-flow square densities in (2.5), the scalar variables \(y,z\), and the lowest mode of the matrix form (3.1). No new curvature evaluation is required. The central conceptual point is that the relevant calibrated quantity is not \(C=Y^2+\Pi\) itself, but
\[
\boxed{\Phi=C-u_2^2,}
\]
the transgression relative to the outgoing complex-hyperbolic Einstein branch. This converts the observed “dip and regrowth” of \(\mathcal T\) into a one-dimensional heteroclinic energy problem and isolates a single signed cubic as the entire unresolved analytic interaction.