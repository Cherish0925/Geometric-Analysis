# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md",
    "Sessions/S1003A02/workspace/scripts/burns_transgression_flux.py",
    "Sessions/S1003A02/workspace/data/burns_transgression_flux.json"
  ]
}
```

## Task

Verify Theorem F (first-order Burns blow-up response for a general closed bulk) in Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md, Section 1, together with the exact flux computation in burns_transgression_flux.py and its output JSON. Claim: gluing the Burns metric delta + x0 h (Kaehler potential |z|^2 + x0 log|z|^2) into g-normal coordinates at p with cutoff radius r0 = x0^{1/5} gives P(ghat) = P(g) + 8 pi^2 (1 - x0 R^+_p(zeta,zeta)) + O(x0^{6/5}), with R^+ = W^+ + s/12 on Lambda^+ in endomorphism norm conventions. Check carefully: (1) the exact topological reduction P(ghat)-P(g)-8pi^2 = 4 Delta W^+ + Delta S/12; (2) whether the inner-region estimate |W^+(ghat)-W^+(g)| <= C min(1, x0/r^2) is valid (bilinear structure, pointwise vanishing of the linearized self-dual curvature of the tail, behavior near the exceptional curve), and hence why no first-order term comes from the inner region; (3) the cut-annulus expansion and that the flux Phi = -int P+ R^lin(chi h) P+ is cutoff independent and is computed correctly by the script (sign of curvature convention, the replacement of d_a d_b f by oint n_a d_b f on the inner sphere, the 1/4 normalization of Lambda^2 pairing, orientation of Lambda^+ for omega = dx12+dx34); (4) that -8 x0 <R^+_p, Phi> equals -8 pi^2 x0 R^+(zeta,zeta) given Phi^{++} = pi^2 w1 w1^T; (5) the consistency checks with Kaehler topology (scalar flux 4 pi^2 x0 = 4 pi area(E), area = pi x0) and with the complex-space-form slopes +6/0/-6 at s=-24. Also check the neck-quantization Lemma Q' (Section 2) and the proportionality rigidity Lemma R (Section 3) for correctness of the Chern-Weil bookkeeping (chi(U)<=2 via Mayer-Vietoris, boundary terms, CH densities 6/pi^2 and 2/pi^2). Report any error, missing hypothesis or wrong constant precisely, and whether each statement is proved as stated.

## Output

# Scientific verification memo

## Overall assessment

- The topological identity and the coefficient
  \[
  -8\pi^2x_0\,\mathbf R_p^+(\zeta,\zeta)
  \]
  are correct with the stated curvature-operator normalization.
- The SymPy flux output
  \[
  \Phi^{++}=\pi^2\,w_1w_1^T,\qquad
  \Phi^{--}=\frac{\pi^2}{3}I,\qquad
  \Phi^{+-}=0
  \]
  has the correct sign, orientation, and \(1/4\) two-form normalization.
- Theorem F has the stated asymptotic after a repair to the inner-region argument. One displayed volume-form estimate there is incorrect, and the “bilinear” sentence abbreviates a mixed finite-difference estimate that needs a two-region derivation. The corrected argument still gives the stronger inner contribution
  \[
  O\!\left(x_0r_0^2+x_0^2|\log x_0|\right)=o(x_0),
  \]
  so the final \(O(x_0^{6/5})\) remainder remains unchanged.
- Lemma Q′ has the correct constant \(8\pi^2\), assuming the usual ball-side orientation and an orientation-preserving \(C^2\) annular parametrization.
- Lemma R has the correct Chern–Weil constants. It requires “exact \(\mathbb{CH}^2\)-collar” to mean an orientation-preserving isometry to a normalized complex-hyperbolic collar, not merely \(\operatorname{Ric}=-6g\) there.

---

## 1. Exact topological reduction

Write
\[
A_+(g)=\int_M |W^+_g|^2\,dV_g,\qquad
S(g)=\int_M s_g^2\,dV_g,\qquad
P(g)=\int_M|\operatorname{Ric}_g^\circ|^2\,dV_g.
\]
From
\[
8\pi^2\chi=A_++A_- -\frac12P+\frac1{24}S,
\qquad
12\pi^2\tau=A_+-A_-,
\]
eliminating \(A_-\) gives
\[
P=4A_++\frac1{12}S-16\pi^2\chi-24\pi^2\tau.
\]
For
\[
\widehat M=M\#\overline{\mathbb{CP}}^{\,2},
\qquad
\Delta\chi=1,\quad \Delta\tau=-1,
\]
one therefore obtains exactly
\[
\begin{aligned}
P(\hat g)-P(g)
&=4\Delta A_++\frac1{12}\Delta S
 -16\pi^2(1)-24\pi^2(-1)\\
&=8\pi^2+4\Delta A_++\frac1{12}\Delta S.
\end{aligned}
\]
Thus
\[
\boxed{P(\hat g)-P(g)-8\pi^2
=4\Delta W^++\frac1{12}\Delta S}
\]
is correct.

The orientation is also consistent: the complex orientation has
\(\omega=dx_1\wedge dx_2+dx_3\wedge dx_4\in\Lambda^+\), while the inserted exceptional class has square \(-1\), hence the connected summand is \(\overline{\mathbb{CP}}^{\,2}\).

---

## 2. Burns normalization and exact self-dual cancellation

For
\[
h_{ij}=\frac1{r^2}\left(
\delta_{ij}-\frac{x_ix_j}{r^2}
-\frac{(Jx)_i(Jx)_j}{r^2}
\right),
\]
the tensor \(h\) has eigenvalue \(r^{-2}\) on the two-dimensional subspace orthogonal to \(x,Jx\), and eigenvalue \(0\) on \(\operatorname{span}\{x,Jx\}\). Hence
\[
B_a=\delta+ah
\]
is exactly
\[
dr^2+(r^2+a)(\sigma_1^2+\sigma_2^2)+r^2\sigma_3^2.
\]
With the stated normalization of the Hopf forms, the metric induced on the exceptional \(\mathbb{CP}^1\) is
\[
a(\sigma_1^2+\sigma_2^2)
\]
and has area \(\pi a\). Thus \(a=x_0=\operatorname{area}(E)/\pi\) is correct.

Since \(B_a\) is scalar-flat Kähler with the complex orientation,
\[
W^+(B_a)=0,\qquad s(B_a)=0.
\]
Differentiating at \(a=0\) is legitimate on \(r>0\). Terms from differentiating the Hodge projector vanish because the Euclidean curvature is zero. Therefore
\[
P_+\mathcal R_\delta^{\mathrm{lin}}(h)P_+=0,
\qquad
s_\delta^{\mathrm{lin}}(h)=0
\]
pointwise away from the origin. The JSON records exactly these identities.

---

## 3. Inner-region estimate

### 3.1 The volume-form sentence is incorrect

For the pure Burns metric,
\[
\sqrt{\det(\delta+ah)}=1+\frac{a}{r^2},
\]
because the two horizontal eigenvalues are \(1+a/r^2\). Consequently
\[
dV_{B_a}=\left(1+\frac{a}{r^2}\right)dx.
\]
Thus, when \(r\ll\sqrt a\),
\[
|dV_{B_a}-dx|=\frac{a}{r^2}\,dx,
\]
which cannot be bounded by
\[
C\min\left(1,\frac{a}{r^2}\right)dx=C\,dx.
\]
So the displayed estimate
\[
|dV_{\hat g}-dV_g|
\le C\min(1,a/r^2)\,dV
\]
is not correct for a uniformly Euclidean reference measure.

This does not create an \(O(a)\) term. The correct proof splits at \(r=\sqrt a\).

### 3.2 Core \(r\le\sqrt a\)

Under \(x=\sqrt a\,y\),
\[
a^{-1}D_{\sqrt a}^{*}\hat g=B_1+K_a,
\qquad K_a(y)=k(\sqrt a\,y).
\]
Normal coordinates give
\[
k(x)=O(r^2),\qquad \partial k=O(r),\qquad \partial^2k=O(1),
\]
hence on bounded \(y\)-sets
\[
\|K_a\|_{C^2(B_1)}\le Ca.
\]
Since \(W^+(B_1)=s(B_1)=0\), smooth dependence of curvature on the metric gives
\[
|W^+(B_1+K_a)|+|s(B_1+K_a)|\le Ca.
\]
Scaling back by \(a^{-1}\) yields
\[
|W^+(\hat g)|+|s(\hat g)|\le C
\]
near the exceptional curve. The smooth bulk curvature is also bounded.

Moreover,
\[
dV_{\hat g}\le C(r^3+ar)\,dr\,d\Omega.
\]
Therefore the total \(W^+\)- and scalar-square contributions from
\(r\le\sqrt a\) are
\[
O\!\left(\int_0^{\sqrt a}(r^3+ar)\,dr\right)=O(a^2).
\]

### 3.3 Intermediate region \(\sqrt a\le r\le r_0/2\)

Here \(b=a/r^2\le1\), so \(B_a\) and \(\delta\) are uniformly equivalent. The precise replacement for “bilinear” is a mixed finite-difference estimate for the nonlinear curvature functional \(F=(W^+,s)\):
\[
F(B_a+k)-F(\delta+k)-F(B_a)+F(\delta).
\]
Because
\[
F(B_a)=F(\delta)=0,
\]
only terms containing both the Burns tail and the bulk perturbation remain. In scaled variables,
\[
B_1-\delta=O(|y|^{-2})
\]
with corresponding weighted derivative decay, while
\[
K_a=O(a|y|^2),\quad
\partial K_a=O(a|y|),\quad
\partial^2K_a=O(a).
\]
Every mixed curvature term is therefore \(O(a|y|^{-2})\) in the scaled metric. Scaling back gives
\[
|F(\hat g)-F(g)|\le C|y|^{-2}
=C\frac{a}{r^2}.
\]
Thus, on the punctured inner region, after choosing a metric isometry to compare the two curvature bundles,
\[
|W^+(\hat g)-W^+(g)|+|s(\hat g)-s(g)|
\le C\min\left(1,\frac{a}{r^2}\right).
\]

For \(r\ge\sqrt a\), the relative volume change is \(O(a/r^2)\). Hence the energy-density difference is bounded by
\[
C\left(\frac{a}{r^2}+\frac{a^2}{r^4}\right)dx.
\]
Integration gives
\[
\begin{aligned}
\int_{\sqrt a}^{r_0}
\left(\frac{a}{r^2}+\frac{a^2}{r^4}\right)r^3\,dr
&=O\!\left(ar_0^2+a^2|\log a|\right).
\end{aligned}
\]
Together with the \(O(a^2)\) core estimate,
\[
\boxed{
\Delta W^+_{\mathrm{inner}},\ \Delta S_{\mathrm{inner}}
=O\!\left(ar_0^2+a^2|\log a|\right).
}
\]
This is \(o(a)\). Thus no first-order term comes from the region containing the exceptional curve.

The theorem’s conclusion survives, but this corrected split is needed in place of the stated pointwise volume estimate.

---

## 4. Cut-annulus expansion

Set
\[
q=a\chi(r/r_0)h.
\]
On \(r_0/2\le r\le r_0\),
\[
|\partial^jq|\le Ca\,r_0^{-2-j},\qquad j=0,1,2.
\]
Since normal coordinates satisfy
\[
g-\delta=O(r_0^2),\quad \partial g=O(r_0),\quad
\partial^2g=O(1),
\]
the difference between the \(g\)-linearization and the flat linearization is
\[
O(ar_0^{-2}).
\]
The flat linear curvature has size \(O(ar_0^{-4})\), so its squared contribution is
\[
O(a^2r_0^{-8}).
\]
Projector and volume variations are also absorbed by these terms. Therefore
\[
|W^+(g+q)|^2dV_{g+q}-|W^+(g)|^2dV_g
=
2a\left\langle W^+(g),
P_+\mathcal R_\delta^{\rm lin}(\chi h)P_+
\right\rangle dx+E\,dx,
\]
with
\[
|E|\le C\left(ar_0^{-2}+a^2r_0^{-8}\right).
\]
After integration over a four-dimensional annulus,
\[
\int |E|\,dx
=O\!\left(ar_0^2+a^2r_0^{-4}\right).
\]

Replacing \(W^+(g)\) by \(W_p^+\) costs
\[
O(ar_0),
\]
because \(W^+(g)=W_p^++O(r_0)\) and the \(L^1\)-norm of the scaled linear curvature is \(O(1)\). The identical reasoning applies to \(s(g)=s_p+O(r_0)\).

These estimates are consistent with the displayed annulus remainder.

---

## 5. Flux computation and script verification

### 5.1 Sign from integration by parts

Let \(A=\{\rho<r<R\}\), with \(\chi=1\) near \(r=\rho\) and \(\chi=0\) near \(r=R\). For any component,
\[
\int_A\partial_a\partial_b(\chi f)\,dx
=
-\int_{S_\rho}n_a\partial_bf\,dS,
\]
because the outward normal of the annulus at its inner sphere is \(-n\). Hence
\[
-\int_A\mathcal R^{\rm lin}(\chi h)\,dx
\]
is the positive radial flux used in the script. This verifies the sign in `flux()`.

Since \(\mathcal R^{\rm lin}\) is a sum of second derivatives, the integral depends only on the endpoint jets of \(\chi h\). It is therefore independent of the detailed cutoff profile. Homogeneity \(h(r\theta)=r^{-2}h(\theta)\) makes the inner-sphere flux independent of \(\rho\).

### 5.2 Curvature convention and \(1/4\) factor

The normal-coordinate constant-curvature jet
\[
h_{ij}=-\frac K3(r^2\delta_{ij}-x_ix_j)
\]
returns
\[
R_{1212}=K
\]
and both diagonal \(\Lambda^\pm\) blocks equal \(KI\), exactly as recorded in the JSON.

If two-forms are represented by antisymmetric matrices,
\[
|\alpha|^2=\frac12\sum_{ij}\alpha_{ij}^2.
\]
Accordingly,
\[
\langle\mathcal R(\alpha),\beta\rangle
=\frac14R_{ijkl}\alpha_{ij}\beta_{kl}.
\]
The `block()` implementation uses precisely this normalization.

### 5.3 Orientation

For \(dx_1\wedge dx_2\wedge dx_3\wedge dx_4>0\),
\[
*(dx_1\wedge dx_2)=dx_3\wedge dx_4,
\]
so
\[
w_1=\frac{dx_1\wedge dx_2+dx_3\wedge dx_4}{\sqrt2}
=\frac{\omega}{\sqrt2}
\]
is unit and self-dual. The other two basis elements in `Wp` also have the correct self-dual signs.

### 5.4 Exact values

The sphere monomial formula in the script,
\[
\int_{S^3}x^\alpha\,dS
=
\frac{2\prod_i\Gamma((\alpha_i+1)/2)}
{\Gamma((|\alpha|+4)/2)}
\]
for even exponents, is correct.

The computed matrices are
\[
\boxed{
\Phi^{++}=
\begin{pmatrix}
\pi^2&0&0\\0&0&0\\0&0&0
\end{pmatrix},\quad
\Phi^{--}=\frac{\pi^2}{3}I,\quad
\Phi^{+-}=0.
}
\]
An independent scalar verification follows from
\[
\operatorname{tr}h=\frac2{r^2},
\qquad
\partial_jh_{ij}=-\frac{2x_i}{r^4}.
\]
Thus
\[
n_i\left(\partial_jh_{ij}-\partial_i\operatorname{tr}h\right)
=\frac2{r^3},
\]
and on \(S_r^3\),
\[
-\int s^{\rm lin}(\chi h)\,dx
=\int_{S_r^3}\frac2{r^3}\,dS
=4\pi^2.
\]
Hence
\[
F_s=4\operatorname{tr}\Phi^{++}=4\pi^2,
\]
in agreement with the JSON.

There is one artifact defect: both denominator assertions contain `if False`, so they reduce to an assertion that \(0=0\). They do not verify that the denominator is a power of \(t^2\). For this particular tensor, direct inspection shows that differentiation produces only denominators \(c(t^2)^m\), so evaluating the denominator at \((1,0,0,0)\) is valid on \(S^3\). The emitted matrices are therefore unaffected, but the script does not internally certify that algebraic property.

---

## 6. Assembly of the first-order coefficient

The annulus terms are
\[
\Delta W^+_{\rm cut}
=-2a\langle W_p^+,\Phi^{++}\rangle
+O(ar_0+ar_0^2+a^2r_0^{-4}),
\]
and
\[
\Delta S_{\rm cut}
=-2a\,s_pF_s
+O(ar_0+ar_0^2+a^2r_0^{-4}).
\]
Therefore
\[
\begin{aligned}
4\Delta W^++\frac1{12}\Delta S
&=-8a\langle W_p^+,\Phi^{++}\rangle
-\frac a6s_pF_s+O(\cdots)\\
&=-8a\langle W_p^+,\Phi^{++}\rangle
-\frac23as_p\operatorname{tr}\Phi^{++}+O(\cdots)\\
&=-8a\left\langle
W_p^++\frac{s_p}{12}I,\Phi^{++}
\right\rangle+O(\cdots)\\
&=-8a\langle\mathbf R_p^+,\Phi^{++}\rangle+O(\cdots).
\end{aligned}
\]
Since the frame identifies \(\zeta\) with \(w_1\),
\[
\langle\mathbf R_p^+,\Phi^{++}\rangle
=\pi^2\mathbf R_p^+(\zeta,\zeta).
\]
Thus
\[
4\Delta W^++\frac1{12}\Delta S
=-8\pi^2a\,\mathbf R_p^+(\zeta,\zeta)+O(\cdots).
\]

With \(r_0=a^{1/5}\),
\[
ar_0=a^{6/5},\qquad
a^2r_0^{-4}=a^{6/5},\qquad
ar_0^2=a^{7/5},
\]
and
\[
a^2|\log a|=O(a^{6/5}).
\]
Combining with the exact topological term gives
\[
\boxed{
P(\hat g_a)
=P(g)+8\pi^2\left(1-a\mathbf R_p^+(\zeta,\zeta)\right)
+O(a^{6/5}).
}
\]

For an Einstein bulk, \(s=4\lambda\) and
\[
J(\hat g)-P(\hat g)
=\frac14\int(s_{\hat g}-4\lambda)^2\,dV_{\hat g}.
\]
The core estimate gives \(O(a^2|\log a|)\), while on the cut annulus
\[
|s_{\hat g}-4\lambda|=O(ar_0^{-4}),
\]
so its square integrates to \(O(a^2r_0^{-4})=O(a^{6/5})\). Thus the same expansion holds for \(J\). Vanishing of the first variation alone does not provide this remainder, but the preceding scalar estimates do.

---

## 7. Consistency tests

### Kähler scalar-curvature normalization

The flux gives
\[
\Delta\int s\,dV=-4\pi^2a+o(a).
\]
Since \(\operatorname{area}(E)=\pi a\),
\[
4\pi\,\operatorname{area}(E)=4\pi^2a.
\]
For a Kähler surface,
\[
\int s\,dV=4\pi\,c_1\cdot[\omega],
\]
and blowing up changes
\[
c_1(\hat M)\cdot[\hat\omega]
=c_1(M)\cdot[\omega]-\operatorname{area}(E).
\]
The sign and factor therefore agree exactly.

### Complex space forms

For a Kähler–Einstein surface,
\[
\mathbf R^+
=\operatorname{diag}\left(\frac s4,0,0\right)
\]
in the Kähler self-dual frame.

- For \(\mathbb{CH}^2\), \(s=-24\):
  \[
  \mathbf R^+=\operatorname{diag}(-6,0,0).
  \]
  Hence the normalized slopes of \(P/(8\pi^2)\) are \(+6\) in the Kähler direction and \(0\) on \(\omega^\perp\).

- For Fubini–Study normalized by \(s=+24\):
  \[
  \mathbf R^+=\operatorname{diag}(6,0,0),
  \]
  so the aligned slope is \(-6\).

Thus \(+6/0\) belong to the \(s=-24\) complex-hyperbolic case; the \(-6\) value belongs to the \(s=+24\) Fubini–Study case.

---

## 8. Lemma Q′

Let \(U_0=U\cup V\), with intersection homotopy equivalent to \(S^3\). Over \(\mathbb R\), Mayer–Vietoris gives
\[
H_2(U)\oplus H_2(V)\cong H_2(U_0)\cong\mathbb R
\]
and
\[
H_1(U)\oplus H_1(V)=0.
\]
Since \(\tau(U)=-1\), the intersection form of \(U\) has rank at least one. Hence
\[
b_2(U)=1,\qquad b_1(U)=0.
\]
As \(U\) has an outer hypersurface, \(b_4(U)=0\), and therefore
\[
\chi(U)=1+b_2(U)-b_3(U)=2-b_3(U)\le2.
\]

For a ball-side hypersurface whose rescaled collar is \(C^2\)-close to a Euclidean annulus, the Gauss–Bonnet and signature transgressions satisfy
\[
\mathcal E_\chi=8\pi^2+O(\varepsilon),
\qquad
\mathcal E_\tau=O(\varepsilon).
\]
Thus
\[
P(U)
=
2\int_U|W|^2+\frac1{12}\int_Us^2
-16\pi^2\chi(U)+16\pi^2+O(\varepsilon).
\]
The signature formula gives
\[
\int_U(|W^+|^2-|W^-|^2)
=-12\pi^2+O(\varepsilon),
\]
so
\[
\int_U|W|^2\ge12\pi^2-C\varepsilon.
\]
Using \(s^2\ge0\) and \(\chi(U)\le2\),
\[
\begin{aligned}
P(U)
&\ge24\pi^2-16\pi^2(2)+16\pi^2-C\varepsilon\\
&=\boxed{8\pi^2-C\varepsilon}.
\end{aligned}
\]

The constant and signs are correct. The hypotheses need the ball-side choice, connectedness of the two pieces, and an orientation-preserving annular parametrization; these are normally implicit in “a sphere enclosing the exceptional class with \(U\) on the ball side.”

---

## 9. Lemma R

For normalized \(\mathbb{CH}^2\),
\[
s=-24,\qquad
W^+=\operatorname{diag}(-4,2,2),\qquad
W^-=0.
\]
Hence
\[
|W^+|^2=24,\qquad \frac{s^2}{24}=24.
\]
The Euler and signature densities are therefore
\[
\frac{24+24}{8\pi^2}=\frac6{\pi^2},
\qquad
\frac{24}{12\pi^2}=\frac2{\pi^2}.
\]

If an Einstein metric agrees with the normalized complex-hyperbolic metric on an open collar, its Einstein constant is \(-6\). Einstein metrics are real analytic in harmonic coordinates. Since \(\nabla\mathrm{Rm}=0\) and the full complex-hyperbolic curvature tensor occur on that open set, analytic continuation gives the same locally symmetric curvature throughout connected \(U\). In particular, the two characteristic densities above are constant on all of \(U\).

Comparing \(U\) with the standard complex-hyperbolic ball having the identical collar makes their transgression terms cancel. If \(\Delta V\) is the volume difference, then
\[
8\pi^2\Delta\chi=48\,\Delta V,
\qquad
12\pi^2\Delta\tau=24\,\Delta V.
\]
Equivalently,
\[
\Delta\chi=\frac6{\pi^2}\Delta V,\qquad
\Delta\tau=\frac2{\pi^2}\Delta V,
\]
and therefore
\[
\boxed{\Delta\chi=3\Delta\tau}.
\]
So \(\Delta\chi\ne3\Delta\tau\) excludes an Einstein extension. Since \(P(U)=0\) would imply \(\operatorname{Ric}^\circ\equiv0\), every individual smooth metric extending such a collar has \(P(U)>0\).

The wording must retain two points:

1. “Exact \(\mathbb{CH}^2\)-collar” must prescribe the full metric, not only \(\operatorname{Ric}=-6g\).
2. The collar isometry must preserve the complex orientation. Reversing orientation changes the sign of the signature density and changes the proportionality relation accordingly.

This establishes strict positivity for each metric; it remains compatible with a degenerating sequence for which \(P\to0\).

---

## Final status by object

| Object | Verification |
|---|---|
| Topological reduction | Exact as written |
| Burns normalization and exceptional area | Correct |
| Pointwise linearized \(++\) block | Correct |
| Flux matrices and scalar flux | Correct |
| Script sign, orientation, \(1/4\) factor | Correct |
| Script denominator self-test | Inactive, though the present denominators are radial powers and the output is correct |
| Inner curvature mechanism | Correct after spelling out the mixed finite-difference estimate |
| Inner volume-form estimate | Incorrect as written; corrected two-region integration preserves the stated remainder |
| Theorem F coefficient and exponent | Correct after that repair |
| Einstein \(J\)-version | Correct using the scalar-square estimates |
| Kähler normalization test | Correct |
| Complex-space-form slopes | \(+6,0\) for \(s=-24\); \(-6\) for Fubini–Study with \(s=+24\) |
| Lemma Q′ | Correct with the standard ball-side and orientation hypotheses |
| Lemma R | Correct when “exact collar” means full orientation-preserving complex-hyperbolic agreement |