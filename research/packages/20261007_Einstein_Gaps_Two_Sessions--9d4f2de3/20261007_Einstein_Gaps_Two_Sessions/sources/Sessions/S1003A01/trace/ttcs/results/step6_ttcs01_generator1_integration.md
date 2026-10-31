# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 6,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step6_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step6_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop the strongest viable analytic mechanism for the perpendicular fixed-slot diagonal Bianchi-IX O11 cell. The bolt-adapted transgression has T/8π²=Y²+Pi, with Y=-1 and Pi=0 at the O(-1) bolt, while on the complex-hyperbolic collar the charge transfers to Pi and Y=0. Numerical near-minimizers make T dip close to zero before Pi grows to the collar charge, and P and J remain slightly above 8π². Seek an exact boundary/interior decomposition or variational inequality that controls this charge transfer by trace-free Ricci energy P or by J; include the scalar-deviation distinction J=P+(1/4)∫(s+24)^2. Use cohomogeneity-one geometry, Chern–Weil transgression, flux/defect variables, Hamiltonian completion of squares, or calibration ideas as appropriate. Formulate explicit candidate inequalities and say which can plausibly be proved from the existing variables, rather than generic suggestions.

## Integrated Scientific Memo

## Perpendicular fixed-slot O11 cell: exact charge-transfer mechanism

Use bolt-adapted cyclic axes
\[
g=dt^2+a_1^2\sigma_1^2+a_2^2\sigma_2^2+a_3^2\sigma_3^2,
\qquad (a_1,a_2,a_3)=\bigl(\sqrt x,\sqrt{xe^w},\sqrt F\bigr),
\]
so \(a_3\) collapses at the bolt and \(dt=dx/(2\sqrt G)\). Define
\[
u_1=e^\varpi p_+,\qquad
u_2=e^{-\varpi}p_-,\qquad
u_3=Y-\frac12p_+p_-,
\qquad e^{2\varpi}=a_1/a_2 .
\]
Equivalently,
\[
u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k}.
\]
Then the supplied transgression formula becomes the symmetric Chern–Simons cubic
\[
\boxed{\ C(u):=\frac{\mathcal T}{8\pi^2}
=u_1^2+u_2^2+u_3^2+u_1u_2u_3\ }                                      \tag{1}
\]
because \(u_1u_2=p_+p_-\). With the opposite connection sign
\(\alpha=-u\), this is
\(\alpha_1^2+\alpha_2^2+\alpha_3^2-\alpha_1\alpha_2\alpha_3\); the two branch conventions are therefore equivalent.

The perpendicular endpoint data are
\[
u_{\rm bolt}=(0,0,-1),\qquad u_{\rm CH}=(0,3x,0),
\]
hence \(C_{\rm bolt}=1\), while \(C_{\rm CH}=9x^2\). Thus the observed dip and regrowth are a transfer from the collapsing \(u_3\)-channel to the CH \(u_2\)-channel, not a scalar flux crossing. This explains why the aligned-slot zero-\(Y\) argument cannot work here.

### 1. Exact curvature decomposition

Put
\[
H_i=u_i+\frac12u_ju_k,\qquad
\lambda_i=\frac{a_ja_k}{a_i},\qquad
r_i=\frac{\dot u_i}{a_i},\qquad
v_i=\frac{2H_i}{a_ja_k}.
\]
Then
\[
C'=abc\sum_i r_iv_i,                                                \tag{2}
\]
and, in the conventions used by the fixed-slot scripts,
\[
|\Ric^\circ|^2=\sum_i(r_i-v_i)^2,\qquad
\frac{s^2}{12}+4|W^+|^2=\sum_i(r_i+v_i)^2,\qquad
s=-2\sum_i(r_i+v_i).                                                \tag{3}
\]
These identities recover the localized Chern–Weil formula
\[
\boxed{\;
\frac{P([0,\rho])}{8\pi^2}
=1-C(\rho)+\frac1{8\pi^2}
 \int_{[0,\rho]}\left(\frac{s^2}{12}+4|W^+|^2\right)dV .
\;}                                                                  \tag{4}
\]
For the Einstein functional in the \(\Ric_{\rm CH}=-6g\) normalization,
\[
\boxed{\;
J=P+\frac14\int(s+24)^2\,dV .
\;}                                                                  \tag{5}
\]
Consequently,
\[
\frac{J([0,\rho])}{8\pi^2}
=1-C(\rho)+\frac1{8\pi^2}
 \int_{[0,\rho]}
 \left[\frac{(s+18)^2}{3}+36+4|W^+|^2\right]dV.                      \tag{6}
\]
Equation (6), rather than the source note’s \(\Ric=-g\) formula, is the correctly rescaled perpendicular-cell identity.

The raw slice bound is therefore exact but insufficient:
\[
J-8\pi^2\ge \int_{\rm in}\mathfrak F-\mathcal T(\rho).
\]
Near-minimizers make \(C(\rho)\) nearly zero and then rebuild it along the Einstein CH channel. A proof must control the differential transfer, not merely the minimum of \(C\).

---

## 2. Relative calibration that removes the outgoing CH charge

The basic \(P\)-energy has the Bogomolny form
\[
\boxed{\;
\frac{P}{8\pi^2}
=\int\sum_{i=1}^3\frac{\lambda_i}{4}
 \left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt .
\;}                                                                  \tag{7}
\]
The ordinary calibration \(C\) charges both endpoint channels. The correct relative calibration is
\[
\boxed{\;
\Phi(u)=C(u)-u_2^2=u_1^2+u_3^2+u_1u_2u_3 ,
\;}                                                                  \tag{8}
\]
for which
\[
\Phi_{\rm bolt}=1,\qquad \Phi_{\rm CH}=0.
\]
Thus it subtracts precisely the Chern–Simons charge transported freely by the outgoing CH Einstein branch.

Completing squares gives the exact identity
\[
\boxed{
\begin{aligned}
\frac{P}{8\pi^2}-1=\int\Bigg[
&\frac{\lambda_1}{4}
 \left(\dot u_1+\frac{2H_1}{\lambda_1}\right)^2
+\frac{\lambda_3}{4}
 \left(\dot u_3+\frac{2H_3}{\lambda_3}\right)^2\\
&+\frac{\lambda_2}{4}
 \left(\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2}\right)^2
+\frac{2u_1u_2u_3}{\lambda_2}
\Bigg]dt .
\end{aligned}}                                                       \tag{9}
\]
Every CH-collar square vanishes. The whole threshold problem is therefore reduced to one non-abelian cubic interaction.

An immediate rigorous result is:

\[
\boxed{\quad
u_1u_2u_3\ge0\ \text{on the cell}
\ \Longrightarrow\ 
P\ge8\pi^2,\qquad J\ge8\pi^2 .
\quad}                                                               \tag{10}
\]
In the original transgression variables this chamber is
\[
\boxed{\quad
(p_+p_-)\left(Y-\frac12p_+p_-\right)\ge0 .
\quad}                                                               \tag{11}
\]

For unrestricted profiles, the exact missing inequality is
\[
\boxed{
\begin{aligned}
\int\Bigg[
&\frac{\lambda_1}{4}
 \left(\dot u_1+\frac{2H_1}{\lambda_1}\right)^2
+\frac{\lambda_3}{4}
 \left(\dot u_3+\frac{2H_3}{\lambda_3}\right)^2\\
&+\frac{\lambda_2}{4}
 \left(\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2}\right)^2
\Bigg]dt
\ge
2\int\frac{(-u_1u_2u_3)_+}{\lambda_2}\,dt .
\end{aligned}}                                                       \tag{12}
\]
This is the strongest explicit \(P\)-candidate supported by the present variables. It is substantially sharper than any inequality controlling \(\Pi\) at a single slice.

---

## 3. Matrix Hardy/Sturm formulation

Treat the outgoing \(u_2\)-channel and radii as background and let
\[
\eta=(u_1,u_3)^T,\qquad
\Lambda=\diag(\lambda_1,\lambda_3),\qquad
A=\begin{pmatrix}1&u_2/2\\u_2/2&1\end{pmatrix}.
\]
The transverse part of (9), including its signed cubic, is
\[
\mathcal Q_\perp(\eta)
=\int\left[
\frac14(\dot\eta+2\Lambda^{-1}A\eta)^T
       \Lambda(\dot\eta+2\Lambda^{-1}A\eta)
+\eta^TB\eta
\right]dt,                                                           \tag{13}
\]
where
\[
B=\begin{pmatrix}0&u_2/\lambda_2\\u_2/\lambda_2&0\end{pmatrix}.
\]
After integration by parts,
\[
\mathcal Q_\perp
=\left[\frac12\eta^TA\eta\right]
+\int\left[
\frac14\dot\eta^T\Lambda\dot\eta+
\eta^T\left(A\Lambda^{-1}A+B-\frac12\dot A\right)\eta
\right]dt.                                                           \tag{14}
\]
Hence a symmetric matrix \(K(t)\) satisfying
\[
\boxed{\;
V-K\Lambda^{-1}K+\frac12\dot K\succeq0,
\qquad
V=A\Lambda^{-1}A+B-\frac12\dot A,
\;}                                                                  \tag{15}
\]
together with nonnegative endpoint form
\(\frac12\eta^T(A-K)\eta\), proves \(\mathcal Q_\perp\ge0\) and thus (12).

On an exact CH segment,
\[
\lambda_1=\lambda_3=\sqrt{x(1+x)},\qquad
\lambda_2=\sqrt{\frac{x}{1+x}},\qquad u_2=3x.
\]
Writing \(v_\pm=u_1\pm u_3\), the form diagonalizes:
\[
\mathcal Q_+
=\int\left[
\frac{x(1+x)}4(v_+')^2+
\frac{4+18x+15x^2}{16x(1+x)}v_+^2
\right]dx,                                                          \tag{16}
\]
\[
\mathcal Q_-
=\int\left[
\frac{x(1+x)}4(v_-')^2+
\frac{4-18x+3x^2}{16x(1+x)}v_-^2
\right]dx.                                                          \tag{17}
\]
Only the \(v_-\) potential changes sign. Thus the perpendicular first-order-free direction is exactly one scalar Sturm channel. Pointwise positivity is false and unnecessary; what is needed is a weighted Hardy inequality or a positive solution of the associated Riccati equation, patched to the transition-region matrix inequality (15).

This is the most plausible direct proof route under quantitative bounds on \(F,G,w\). A universal argument must additionally use the torsion-free equations, because the coefficients in (15) are themselves metric-dependent.

---

## 4. The stronger \(J\)-completion

The distinction between \(J\) and \(P\) is essential at second order. From (3),
\[
\boxed{\;
\frac{J-P}{8\pi^2}
=\frac14\int abc\left[
\sum_i\left(
\frac{\dot u_i}{a_i}+\frac{2H_i}{a_ja_k}
\right)-12
\right]^2dt .
\;}                                                                  \tag{18}
\]
Combining (18) with (9),
\[
\boxed{
\begin{aligned}
\frac{J}{8\pi^2}-1=\int\Bigg[
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
\end{aligned}}                                                       \tag{19}
\]
Therefore the exact \(J\)-target is (12) with the scalar square added on the left. This is genuinely easier than the corresponding \(P\)-problem and a proof for \(J\) need not prove \(P\ge8\pi^2\).

Pointwise minimization over the three velocities yields the weaker but explicit consequence
\[
\boxed{\;
\frac{J}{8\pi^2}-1
\ge\int abc\bigl[(y-3)^2+2zy\bigr]\,dt,
\qquad
y=\frac{u_2}{a_1a_3},\quad
z=\frac{u_1u_3}{a_1a_3}.
\;}                                                                  \tag{20}
\]
It is exact on the CH branch \((y,z)=(3,0)\). Hence
\[
\int abc\bigl[(y-3)^2+2zy\bigr]dt\ge0
\]
is an immediately checkable sufficient condition for \(J\ge8\pi^2\), though it discards the derivative coercivity needed in the difficult sign chamber.

---

## 5. Full Hamilton–Jacobi calibration

The connection variables are constrained by torsion-freeness:
\[
\dot a_i=u_i+\gamma_i(a),\qquad
\gamma_i(a)=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k}.                       \tag{21}
\]
For any \(B(a,u)\), (7) admits the exact completion
\[
\frac{P}{8\pi^2}
=B_{\rm bolt}-B_{\rm CH}
+\int\left[
\sum_i\frac{\lambda_i}{4}
\left(
\dot u_i-\frac{2(H_i-B_{u_i})}{\lambda_i}
\right)^2+\mathcal R_B
\right]dt,                                                          \tag{22}
\]
with
\[
\boxed{\;
\mathcal R_B
=\nabla_aB\cdot(u+\gamma)
+\sum_i\frac{B_{u_i}(2H_i-B_{u_i})}{\lambda_i}.
\;}                                                                  \tag{23}
\]
Thus any scale-invariant \(B\) satisfying
\[
B_{\rm bolt}=1,\qquad B_{\rm CH}=0,\qquad \mathcal R_B\ge0            \tag{24}
\]
proves the complete fixed-slot \(P\)-threshold.

The zeroth approximation is precisely
\[
B_0=C-u_2^2,\qquad
\mathcal R_{B_0}=\frac{2u_1u_2u_3}{\lambda_2}.                        \tag{25}
\]
A concrete correction is suggested by
\[
\psi(a,u)=-\frac{a_2^2}{a_1a_3}u_1u_3,
\]
because
\[
\psi_{a_2}u_2=-\frac{2u_1u_2u_3}{\lambda_2},                         \tag{26}
\]
which cancels the bad cubic transport term exactly. The remaining terms in
\(\mathcal R_{B_0+\psi}\) are explicit quadratic and quartic expressions. The raw \(\psi\) must be modified or localized so that it is smooth at the bolt and has zero endpoint contribution, but (26) identifies the correct first correction rather than merely postulating another flux.

---

## 6. What is established and what remains unresolved

The exact, source-compatible conclusion is:

1. The relevant charge is the cubic Chern–Simons function (1), not \(Y\) alone.
2. The correct relative calibration is
   \[
   \Phi=C-u_2^2,
   \]
   which removes all outgoing CH charge.
3. The perpendicular threshold reduces exactly to one signed cubic term, equivalently to the matrix Hardy inequality (12)–(15).
4. The sign chamber (11) already gives a rigorous finite-amplitude theorem:
   \[
   P\ge8\pi^2,\qquad J\ge8\pi^2.
   \]
5. For \(J\), the scalar-deviation square (18) supplies additional rank-one coercivity and must not be suppressed by replacing \(J\) with \(P\).

The second branch’s proposed \(x_0^2\log(1/x_0)\) negative drain and eventual subthreshold prediction is not established by the supplied sources. It is based on an uncontrolled round-weight middle-region reduction and coarse cancellation of small numerical excesses; the existing data quoted in the source remain positive and are explicitly described as optimizer-dependent upper bounds. Moreover, the matrix/Sturm formulation shows that a locally negative potential does not determine the sign of the integrated form because derivative and endpoint costs are decisive. The logarithmic scenario is therefore a testable hypothesis, not a consequence.

The precise unresolved object is either:

- a positive matrix/Riccati supersolution for (15), including the bolt-to-collar transition and admissible metric-dependent coefficients; or
- a smooth scale-invariant calibration \(B(a,u)\) satisfying (24), likely obtained by repairing \(B_0+\psi\); or
- an actual admissible profile for which the exact right side of (9) or (19) is negative.

Existing numerical profiles can distinguish these without new curvature code by recording
\[
u_1u_2u_3,\qquad
\text{the three square densities in (9)},\qquad
(y-3)^2+2zy,
\]
and the lowest eigenvalue of the transverse Sturm form (13). This evaluates the exact mechanism directly and avoids subtracting two quantities both close to \(8\pi^2\).