# TTCS Independent Branch Record

```json
{
  "step_id": 70,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step70_selected_support_lemma.md",
    "Sessions/S0910A01/workspace/notes/step68_restricted_IL_canonical_assembly.md"
  ]
}
```

## Task

Verify the mathematical correctness and completeness of the selected-support lemma for the restricted IL negative-gap theorem. The note proves:

1. FULL-CURVATURE BUDGET: ∫|Rm|² ≤ C₀A_i from Chern-Gauss-Bonnet, using I-J=2A/3-q, J≤δ²Vol/(2π²), and Vol≤CA. Check that the identities are correctly applied, the volume upper bound derivation from the mixed SW inequality is valid, and equation (2.4) ∫|Rm|²=8π²χ+3/2∫|Ric°|² holds.

2. WEAK-TYPE MAXIMAL INEQUALITY: Lemma 4.1 under Ric≥-(n-1)g. Check the Vitali covering argument, the Bishop-Gromov volume doubling ratio, and the constant C(n,R₀).

3. COLLAPSE-CANCELLING PRODUCT: γ_α(0)=S_α·H_{2,α}^{1/2}≤C(r²+γ̃). The claim is that S_α~r²/Vol^{1/2} grows under collapse while H_{2,α}^{1/2}~Vol^{1/2}·(1+γ̃/r²) shrinks, so their product eliminates volume. Check each factor's scaling carefully, especially whether H₂ = ∫η²F_T² ≤ C(1+γ̃²/r⁴)Vol is correct.

4. PARAMETER ORDERING: The construction requires fixing γ̃ before r. Verify that the constraints C₁r⁴/γ̃² < c_V/2 and C(r²+γ̃) < γ*/2 are simultaneously satisfiable.

5. INTERFACE: Check that the listed outputs (7 sequence-uniform items and 5 datum-dependent items) are correctly categorized. In particular, is it true that no sequence-uniform bound on initial sectional curvature is needed?

## Output

# Scientific verification memo

## Summary

The maximal-function estimate and the collapse-cancelling product are mathematically sound in their essential form, and the parameter constraints are compatible. The selected-support construction nevertheless contains four substantive errors in its present text:

1. Equations (2.3)–(2.4) use an incorrect coefficient for the trace-free Ricci term under the stated operator normalization.
2. Equation (2.5), \(8\pi^2\chi=I+J\), is false for the definitions of \(I,J\) used in the assembly; the required Euler-characteristic estimate needs a separate topological argument.
3. Proposition 3.1 has the wrong normalized mean \(2/9\); it must be \(3/4\). The displayed volume constant \(32\pi^2/9\) corresponds to \(3/4\).
4. Sections 5.2–5.3 invoke a uniform lower volume for fixed-radius balls from a Ricci lower bound. Such a lower volume does not exist in collapsing geometries. The coloring conclusion remains available through local doubling, but its proof and degree constant need replacement.

There is also a cutoff-smoothing issue: the stated mollification enlarges \(\operatorname{supp}\chi_\alpha\) beyond \(B_{6r}\), which can destroy the exact support identities. Reserve radii repair this.

With these repairs, the support module can provide the intended sequence-uniform data without any sequence-uniform initial sectional-curvature estimate.

---

## 1. Full-curvature budget

### 1.1 Curvature decomposition and Chern–Gauss–Bonnet

Under the note’s normalization
\[
|\operatorname{Rm}|_{\mathrm{op}}^2
=\frac14R_{ijkl}R^{ijkl},
\qquad |G|^2=\frac23,
\]
the four-dimensional orthogonal decomposition is
\[
\operatorname{Rm}
=W+\frac12\operatorname{Ric}^{\circ}\owedge g
+\frac{s}{24}g\owedge g,
\]
and therefore
\[
\boxed{
|\operatorname{Rm}|_{\mathrm{op}}^2
=|W|_{\mathrm{op}}^2
+\frac12|\operatorname{Ric}^{\circ}|^2
+\frac{s^2}{24}.}
\]

Indeed, for a trace-free symmetric tensor \(z\),
\[
|z\owedge g|_{\text{full}}^2=8|z|^2
\quad(n=4),
\]
so the operator-normalized norm of \(\frac12z\owedge g\) is
\[
\frac14\cdot\frac14\cdot8|z|^2=\frac12|z|^2.
\]

The Chern–Gauss–Bonnet formula is
\[
8\pi^2\chi(M)
=\int_M\left(
|W|_{\mathrm{op}}^2-\frac12|\operatorname{Ric}^{\circ}|^2
+\frac{s^2}{24}
\right)d\mu.
\]
Subtracting these identities gives
\[
\boxed{
\int_M|\operatorname{Rm}|_{\mathrm{op}}^2\,d\mu
=8\pi^2\chi(M)+\int_M|\operatorname{Ric}^{\circ}|^2\,d\mu.}
\]

Thus equations (2.3) and (2.4) are inconsistent with the declared normalization: the coefficient in (2.3) should be \(1/2\), and the coefficient in (2.4) should be \(1\), not \(3/2\). This numerical correction does not obstruct the desired upper estimate.

### 1.2 Operator norm versus Hilbert–Schmidt norm

Since
\[
\delta_i=\|g^{-1}E_i\|_{\infty,\mathrm{op}},
\]
one has
\[
|\operatorname{tr}E_i|\le4\delta_i,
\qquad
|E_i|_{\mathrm{HS}}\le2\delta_i.
\]
Orthogonal projection onto the trace-free tensors gives
\[
|\operatorname{Ric}^{\circ}|=|E_i^\circ|
\le |E_i|_{\mathrm{HS}}\le2\delta_i.
\]
Consequently
\[
J_i=\frac1{8\pi^2}\int|\operatorname{Ric}^{\circ}|^2
\le \frac{\delta_i^2}{2\pi^2}\operatorname{Vol}(M_i).
\]
The estimate used later is therefore correct, although the intermediate statement \(|E|\le\delta_i\) is not correct when \(\delta_i\) is the operator norm.

### 1.3 Volume upper estimate

Write
\[
I_i=\frac1{4\pi^2}\int\left(\frac{s^2}{24}+2|W^+|^2\right),
\qquad
I_i-J_i=\frac{2A_i}{3}-q_i.
\]
Since \(s=-4+\operatorname{tr}E_i\) and \(|\operatorname{tr}E_i|\le4\delta_i\),
\[
|s|\ge4(1-\delta_i)
\quad(\delta_i<1).
\]
Hence
\[
I_i\ge
\frac{(1-\delta_i)^2}{6\pi^2}\operatorname{Vol}(M_i).
\]
Because \(q_i\ge0\),
\[
I_i=J_i+\frac{2A_i}{3}-q_i
\le \frac{\delta_i^2}{2\pi^2}\operatorname{Vol}(M_i)
+\frac{2A_i}{3}.
\]
Therefore
\[
\left[(1-\delta_i)^2-3\delta_i^2\right]\operatorname{Vol}(M_i)
\le4\pi^2A_i,
\]
and for \(\delta_i<1/4\),
\[
\operatorname{Vol}(M_i)\le C_VA_i.
\]
This part is valid after replacing the one-sided sentence about \(s\) by the two-sided estimate \(|s+4|\le4\delta_i\).

### 1.4 The Euler-characteristic step

For the normalized \(I_i,J_i\) above,
\[
I_i+J_i\ne8\pi^2\chi(M_i).
\]
The quantity \(I_i-J_i\) equals \(2\chi+3\tau\), while \(I_i+J_i\) is another curvature integral and does not determine \(\chi\). Equation (2.5) therefore cannot justify \(\chi(M_i)=O(A_i)\).

A valid replacement follows from the supplied mixed Seiberg–Witten estimate:
\[
I_i\ge\frac{2A_i}{3}.
\]
Together with \(I_i=J_i+2A_i/3-q_i\), this gives
\[
0\le q_i\le J_i\le C\delta_i^2A_i.
\]
Thus
\[
D_i=\frac{A_i}{3}+q_i\le CA_i.
\]

For connected oriented \(N_i\) with \(b_+(N_i)=0\),
\[
(2\chi+3\tau)(N_i)=4-4b_1(N_i)-b_-(N_i),
\]
so
\[
D_i=4(m_i-1)+4b_1(N_i)+b_-(N_i).
\]
It follows that
\[
|\chi(N_i)|\le 2+2b_1(N_i)+b_-(N_i)\le C(1+D_i)\le CA_i,
\]
using \(A_i\ge m_i\ge2\).

For each minimal surface of general type \(X\), the topological Euler number is \(c_2(X)\), and the connected-sum formula is
\[
\chi(M_i)=\sum_j c_2(X_{j,i})+\chi(N_i)-2m_i.
\]
The displayed connected-sum formula in §2 is not this formula. The classical Noether inequality
\[
K_X^2\ge2p_g(X)-4
\]
and \(c_2=12\chi(\mathcal O_X)-K_X^2\) give
\[
c_2(X)\le 5K_X^2+36\le41K_X^2,
\]
since \(K_X^2=c_1^2(X)\) is a positive integer. Hence
\[
|\chi(M_i)|\le CA_i.
\]

Using the corrected curvature identity,
\[
\int|\operatorname{Rm}|^2
=8\pi^2\chi(M_i)+\int|\operatorname{Ric}^{\circ}|^2
\le C A_i.
\]
The shifted estimate then follows:
\[
F_T^2=1+|\operatorname{Rm}-G|^2
\le \frac73+2|\operatorname{Rm}|^2,
\]
so
\[
\int F_T^2\le C A_i.
\]

---

## 2. Volume lower estimate

The constant in Proposition 3.1 is compatible with the calibration inequality, but the stated mean \(2/9\) is not.

Let
\[
u=s+8\sqrt6\,|W^+|,
\qquad
d=\frac{s^2}{24}+2|W^+|^2.
\]
Since \(|W^+|=(u-s)/(8\sqrt6)\),
\[
d=\frac{3s^2}{64}-\frac{su}{96}+\frac{u^2}{192}.
\]
The supplied calibration gives
\[
\int u^2\le108Q,
\qquad
Q\le4\delta_i^2\operatorname{Vol}(M_i),
\]
while \(|s+4|\le4\delta_i\). Therefore
\[
\fint d\le\frac34+C\delta_i.
\]
The reference value is visibly \(3/4\): at \(s=-4\) and \(u=0\),
\[
|W^+|^2=\frac1{24},
\qquad
d=\frac{16}{24}+\frac{2}{24}=\frac34.
\]

Since
\[
4\pi^2I_i=\int d
\quad\text{and}\quad
I_i\ge\frac{2A_i}{3},
\]
one obtains
\[
\operatorname{Vol}(M_i)
\ge
\frac{8\pi^2A_i/3}{3/4+C\delta_i}
=
\frac{32\pi^2}{9}A_i(1-O(\delta_i)).
\]
Thus the displayed lower-volume constant is correct after replacing \(2/9\) by \(3/4\).

---

## 3. Weak-type maximal inequality

Lemma 4.1 is valid. A \(5r\)-Vitali subfamily gives
\[
\operatorname{Vol}\{\mathcal M_{R_0}f>\lambda\}
\le\sum_j\operatorname{Vol}(B_{5s_j}(x_j)).
\]
Bishop–Gromov comparison under
\(\operatorname{Ric}\ge-(n-1)g\) yields
\[
\frac{\operatorname{Vol}(B_{5s}(x))}
{\operatorname{Vol}(B_s(x))}
\le
\frac{V_{-1}(5s)}{V_{-1}(s)}.
\]
Hence
\[
C(n,R_0)
=
\sup_{0<s\le R_0}\frac{V_{-1}(5s)}{V_{-1}(s)}
<\infty,
\]
and disjointness of the selected \(B_{s_j}\) gives (4.1).

For \(R_0=10r\), this constant remains uniformly bounded as \(r\downarrow0\); it approaches the Euclidean ratio \(5^n\). Thus \(C_1\) in (4.3) can be taken uniformly for \(0<r\le r_0\).

---

## 4. Packing and coloring

The sentence asserting
\[
\operatorname{Vol}(B_{r/2}(x))\ge v_-(r/2)
\]
from \(\operatorname{Ric}\ge-3g\) is false. Ricci lower control permits collapse and gives no universal positive lower volume. Compactness alone implies that an \(r\)-separated family is finite.

The graph-degree estimate can instead be obtained from local doubling. Fix a center \(x\), and let \(y_j\) be its graph neighbors. Then the balls \(B_{r/2}(y_j)\) are pairwise disjoint and lie in \(B_{15r}(x)\). Also,
\[
B_{15r}(x)\subset B_{29r}(y_j).
\]
Bishop–Gromov at \(y_j\) gives
\[
\operatorname{Vol}(B_{r/2}(y_j))
\ge
\frac{V_{-1}(r/2)}{V_{-1}(29r)}
\operatorname{Vol}(B_{29r}(y_j))
\ge
c(n,r)\operatorname{Vol}(B_{15r}(x)).
\]
Summing the disjoint small balls inside \(B_{15r}(x)\) gives
\[
\#\{y_j\}
\le
\frac{V_{-1}(29r)}{V_{-1}(r/2)}.
\]
This produces a sequence-uniform finite degree and hence a finite coloring. Partitioning the sum of the \(B_r\)-volumes among the colors then gives the stated \(A_i\)-proportional retained volume.

---

## 5. Collapse-cancelling product

This is the strongest part of the note and is correct.

For \(U_\alpha=B_{7r}(x_\alpha)\), goodness of the center gives
\[
\int_{U_\alpha}|\operatorname{Rm}|^2
\le\frac{\widetilde\gamma^2}{r^4}\operatorname{Vol}(U_\alpha).
\]
Since
\[
F_T^2
=1+|\operatorname{Rm}-G|^2
\le\frac73+2|\operatorname{Rm}|^2,
\]
one has
\[
H_{2,\alpha}(0)
\le
C\left(1+\frac{\widetilde\gamma^2}{r^4}\right)
\operatorname{Vol}(U_\alpha).
\]

The normalized local Sobolev inequality under a Ricci lower estimate has
\[
\mathcal S_\alpha(0)
\le
C r^2\operatorname{Vol}(U_\alpha)^{-1/2},
\]
with the factor \(7^2\) absorbed into \(C\). Therefore
\[
\begin{aligned}
\gamma_\alpha(0)
&=\mathcal S_\alpha(0)H_{2,\alpha}(0)^{1/2}\\
&\le
Cr^2\operatorname{Vol}(U_\alpha)^{-1/2}
\left[
\left(1+\frac{\widetilde\gamma^2}{r^4}\right)
\operatorname{Vol}(U_\alpha)
\right]^{1/2}\\
&\le C\sqrt{r^4+\widetilde\gamma^2}
\le C(r^2+\widetilde\gamma).
\end{aligned}
\]
The local volume cancels exactly. Neither factor is separately sequence-uniform under collapse, but their product is.

---

## 6. Parameter compatibility

Let \(C_\gamma\) be the constant in
\[
\gamma_\alpha(0)\le C_\gamma(r^2+\widetilde\gamma),
\]
and let \(\overline C_1\) bound the maximal-function constant for
\(0<r\le r_0\). Once the downstream universal number \(\gamma_*\) is fixed, one may take
\[
0<\widetilde\gamma<
\frac{\gamma_*}{4C_\gamma}
\]
together with the absorption requirement. Then any positive \(r\) satisfying
\[
r<
\min\left\{
r_0,\,
\left(\frac{\gamma_*}{4C_\gamma}\right)^{1/2},\,
\left(\frac{c_V\widetilde\gamma^2}{2\overline C_1}\right)^{1/4}
\right\}
\]
gives simultaneously
\[
C_\gamma(r^2+\widetilde\gamma)<\frac{\gamma_*}{2},
\qquad
\frac{C_1r^4}{\widetilde\gamma^2}<\frac{c_V}{2}.
\]
Thus fixing \(\widetilde\gamma\) before \(r\) is consistent.

---

## 7. Cutoff support identities

The exact identities
\[
a_i|\nabla\eta_\alpha|^2=0,
\qquad
\nabla a_i\cdot\nabla\eta_\alpha=0
\]
require the final smooth functions to satisfy the exact displayed nesting.

The mollification described in §6.1 produces a plateau only on
\(B_{5r-\varepsilon}\) and support extending to \(B_{6r+\varepsilon}\). That description does not by itself preserve (6.1)–(6.2). A rigorous construction uses reserve radii before smoothing, for example:

- raw \(\chi_\alpha=1\) through \(5r+\varepsilon\), zero from \(6r-\varepsilon\);
- raw \(\eta_\alpha=1\) through \(6r+\varepsilon\), zero from \(7r-\varepsilon\);

followed by smoothing at a smaller scale. The resulting smooth cutoffs satisfy the original \(5r,6r,7r\) inclusions and \(|\nabla\chi_\alpha|+|\nabla\eta_\alpha|\le C/r\). Higher derivatives remain datum-dependent.

---

## 8. Interface classification

After the preceding repairs, the following are genuinely sequence-uniform:

- \(\int|\operatorname{Rm}|^2\le C A_i\);
- \(\int F_T^2\le C A_i\);
- \(c_VA_i\le\operatorname{Vol}(M_i)\le C_VA_i\);
- good-set and retained-color volumes proportional to \(A_i\);
- finite graph degree and disjoint outer supports;
- smooth global weight with a uniform first-derivative estimate and exact support identities;
- \(\gamma_\alpha(0)\le C(r^2+\widetilde\gamma)\);
- \(Q_i(0)\le C\delta_i^2A_i\).

The following are only datum-dependent as absolute quantities:

- higher cutoff derivatives;
- the initial Sobolev constants;
- the local energies \(H_{2,\alpha}(0)\), although they obey the uniform volume-weighted formula above;
- the short existence time supplied by the per-datum flow theorem;
- initial pointwise sectional curvature.

No sequence-uniform initial sectional-curvature estimate enters the maximal-function selection, normalized Sobolev estimate, energy-product cancellation, packing via doubling, or support construction. Every smooth compact datum individually has finite pointwise curvature, which may enter its own short-time existence theorem. The sequence-uniform pointwise curvature used at terminal time is instead intended to arise from the later positive-time smoothing estimates. Thus this interface is coherent, provided the cited \(q=2\) curvature-energy and continuation modules indeed consume only the product \(\mathcal S_\alpha H_{2,\alpha}^{1/2}\), as stated in the assembly.