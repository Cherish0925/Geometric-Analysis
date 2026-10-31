# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 20,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step20_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step20_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify Theorem F (first-order Burns blow-up response for a general closed bulk) in Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md, Section 1, together with the exact flux computation in burns_transgression_flux.py and its output JSON. Claim: gluing the Burns metric delta + x0 h (Kaehler potential |z|^2 + x0 log|z|^2) into g-normal coordinates at p with cutoff radius r0 = x0^{1/5} gives P(ghat) = P(g) + 8 pi^2 (1 - x0 R^+_p(zeta,zeta)) + O(x0^{6/5}), with R^+ = W^+ + s/12 on Lambda^+ in endomorphism norm conventions. Check carefully: (1) the exact topological reduction P(ghat)-P(g)-8pi^2 = 4 Delta W^+ + Delta S/12; (2) whether the inner-region estimate |W^+(ghat)-W^+(g)| <= C min(1, x0/r^2) is valid (bilinear structure, pointwise vanishing of the linearized self-dual curvature of the tail, behavior near the exceptional curve), and hence why no first-order term comes from the inner region; (3) the cut-annulus expansion and that the flux Phi = -int P+ R^lin(chi h) P+ is cutoff independent and is computed correctly by the script (sign of curvature convention, the replacement of d_a d_b f by oint n_a d_b f on the inner sphere, the 1/4 normalization of Lambda^2 pairing, orientation of Lambda^+ for omega = dx12+dx34); (4) that -8 x0 <R^+_p, Phi> equals -8 pi^2 x0 R^+(zeta,zeta) given Phi^{++} = pi^2 w1 w1^T; (5) the consistency checks with Kaehler topology (scalar flux 4 pi^2 x0 = 4 pi area(E), area = pi x0) and with the complex-space-form slopes +6/0/-6 at s=-24. Also check the neck-quantization Lemma Q' (Section 2) and the proportionality rigidity Lemma R (Section 3) for correctness of the Chern-Weil bookkeeping (chi(U)<=2 via Mayer-Vietoris, boundary terms, CH densities 6/pi^2 and 2/pi^2). Report any error, missing hypothesis or wrong constant precisely, and whether each statement is proved as stated.

## Integrated Scientific Memo

# Verification memo

## Verdict

- **Theorem F has the correct leading term and \(O(x_0^{6/5})\) remainder, but its proof is not valid literally as written.** The inner-region volume estimate is false and must be replaced by a core/intermediate-region argument. After that repair, the theorem follows.
- The exact flux output
  \[
  \Phi^{++}=\pi^2\,\zeta\otimes\zeta,\qquad
  \Phi^{--}=\frac{\pi^2}{3}I,\qquad
  \Phi^{+-}=0
  \]
  is correct with the stated curvature, pairing, and orientation conventions.
- The script’s numerical/symbolic output is correct, although its two denominator assertions are vacuous.
- The Kähler consistency check has a **factor-\(\pi\) typo in its displayed cohomological formula**, but its final scalar-curvature drop is correct.
- **Lemma Q′ is correct**, subject to the implicit ball-side orientation and quantitative boundary-transgression control. The proof can safely use only \(\chi(U)\le2\).
- **Lemma R is correct under a full, orientation-preserving exact \(\mathbb{CH}^2\) collar hypothesis.** Its immediate “all cells” consequence is not supplied by the displayed proportionality obstruction when \(\Delta\chi=3\Delta\tau\), notably \(\ell=2k\); a separate local-\(\mathbb{CH}^2\) filling rigidity argument is then required.

---

## 1. Exact topological reduction

Let
\[
A_\pm(g)=\int |W_g^\pm|^2\,dV_g,\qquad
S(g)=\int s_g^2\,dV_g,\qquad
P(g)=\int|\operatorname{Ric}_g^\circ|^2\,dV_g .
\]
From
\[
8\pi^2\chi=A_++A_--\frac12P+\frac1{24}S,
\qquad
12\pi^2\tau=A_+-A_-,
\]
eliminating \(A_-\) yields
\[
P=4A_++\frac1{12}S-16\pi^2\chi-24\pi^2\tau.
\]
For \(\widehat M=M\#\overline{\mathbb{CP}}^{\,2}\),
\[
\Delta\chi=1,\qquad \Delta\tau=-1,
\]
so exactly
\[
\boxed{
P(\hat g)-P(g)-8\pi^2
=4\Delta A_++\frac1{12}\Delta S .
}
\]
Thus item (1), including the constant \(8\pi^2\), is correct.

The orientation is consistent: with \(dx^{1234}>0\),
\[
\omega=dx^1\wedge dx^2+dx^3\wedge dx^4
\]
is self-dual, while the exceptional class has square \(-1\), hence the summand is \(\overline{\mathbb{CP}}^2\).

---

## 2. Burns normalization and inner-region repair

### Exact Burns facts

For
\[
h_{ij}=\frac1{r^2}\left(
\delta_{ij}-\frac{x_ix_j}{r^2}
-\frac{(Jx)_i(Jx)_j}{r^2}
\right),
\]
the tensor \(h\) vanishes on \(\operatorname{span}\{x,Jx\}\) and has eigenvalue \(r^{-2}\) on its orthogonal complement. Hence
\[
B_a=\delta+ah
=dr^2+(r^2+a)(\sigma_1^2+\sigma_2^2)+r^2\sigma_3^2.
\]
The exceptional curve has
\[
\operatorname{area}(E)=\pi a.
\]

Since \(B_a\) is scalar-flat Kähler in the complex orientation,
\[
W^+(B_a)=0,\qquad s(B_a)=0.
\]
Differentiating at \(a=0\), away from \(r=0\), gives
\[
P_+\mathcal R_\delta^{\rm lin}(h)P_+=0,
\qquad
s_\delta^{\rm lin}(h)=0.
\]
The JSON verifies these pointwise identities.

### The false statement in the note

The proof asserts
\[
|dV_{\hat g}-dV_g|
\le C\min(1,a/r^2)\,dx.
\]
This is false near the exceptional curve. For the pure Burns metric,
\[
\sqrt{\det(\delta+ah)}=1+\frac a{r^2},
\]
so
\[
dV_{B_a}=\left(1+\frac a{r^2}\right)dx.
\]
When \(r\ll\sqrt a\), the difference is \(a r^{-2}dx\), not \(O(dx)\).

### Correct core estimate: \(r\le\sqrt a\)

Put \(x=\sqrt a\,y\). Then
\[
a^{-1}D_{\sqrt a}^{*}\hat g=B_1+K_a,
\qquad K_a(y)=k(\sqrt a\,y),
\]
where \(k=g-\delta\). Normal-coordinate estimates give
\[
K_a=O(a|y|^2),\qquad
\partial_yK_a=O(a|y|),\qquad
\partial_y^2K_a=O(a).
\]
On a bounded neighborhood of the exceptional curve, \(B_1\) has bounded geometry and the pullback perturbation is \(O(a)\) in \(C^2\). Therefore
\[
|W^+(B_1+K_a)|+|s(B_1+K_a)|\le Ca.
\]
After scaling back,
\[
|W^+(\hat g)|+|s(\hat g)|\le C.
\]
Moreover,
\[
dV_{\hat g}\le C(r^3+ar)\,dr\,d\Omega.
\]
Thus the curvature-square contributions of the core are
\[
O\!\left(\int_0^{\sqrt a}(r^3+ar)\,dr\right)=O(a^2).
\]

### Intermediate region: \(\sqrt a\le r\le r_0/2\)

Here \(a/r^2\le1\), so all relevant metrics are uniformly equivalent. For \(F=(W^+,s)\), use the mixed finite difference
\[
F(B_a+k)-F(\delta+k)-F(B_a)+F(\delta).
\]
The pure terms vanish:
\[
F(B_a)=F(\delta)=0.
\]
Every remaining term contains both a Burns-tail factor and a bulk-jet factor. In rescaled variables,
\[
B_1-\delta=O(|y|^{-2}),\qquad
K_a=O(a|y|^2),\quad
\partial K_a=O(a|y|),\quad
\partial^2K_a=O(a),
\]
so the mixed curvature is \(O(a|y|^{-2})\) in the scaled metric. Scaling back gives
\[
|W^+(\hat g)-W^+(g)|+|s(\hat g)-s(g)|
\le C\frac a{r^2}.
\]
The relative volume correction is also \(O(a/r^2)\) in this region. Consequently the energy-density difference is bounded by
\[
C\left(\frac a{r^2}+\frac{a^2}{r^4}\right)dx,
\]
and
\[
\int_{\sqrt a}^{r_0}
\left(\frac a{r^2}+\frac{a^2}{r^4}\right)r^3\,dr
=
O\!\left(ar_0^2+a^2|\log a|\right).
\]

Combining both regions,
\[
\boxed{
\Delta A_{+,\mathrm{inner}},\ \Delta S_{\mathrm{inner}}
=
O\!\left(ar_0^2+a^2|\log a|\right)=o(a).
}
\]
Thus the claimed absence of an inner first-order term is correct, but the proof requires this two-region argument. Calling the curvature difference merely “bilinear” is too terse: the needed object is the mixed finite difference of the nonlinear curvature functional.

---

## 3. Cut annulus and exact flux

Let
\[
q=a\,\chi(r/r_0)h.
\]
On \(r_0/2\le r\le r_0\),
\[
|\partial^jq|\le Ca\,r_0^{-2-j},\qquad j=0,1,2.
\]
Normal coordinates give
\[
g-\delta=O(r_0^2),\qquad \partial g=O(r_0),\qquad \partial^2g=O(1).
\]
Hence
\[
|W^+(g+q)|^2dV_{g+q}-|W^+(g)|^2dV_g
=
2a\left\langle W^+(g),
P_+\mathcal R_\delta^{\rm lin}(\chi h)P_+
\right\rangle dx+E\,dx,
\]
where
\[
|E|\le C\left(ar_0^{-2}+a^2r_0^{-8}\right).
\]
After integration over the annulus,
\[
\int |E|=O\!\left(ar_0^2+a^2r_0^{-4}\right).
\]
Replacing \(W^+(g)\) and \(s(g)\) by their values at \(p\) costs \(O(ar_0)\). Therefore
\[
\Delta A_{+,\mathrm{cut}}
=
-2a\langle W_p^+,\Phi^{++}\rangle
+O(ar_0+ar_0^2+a^2r_0^{-4}),
\]
and
\[
\Delta S_{\mathrm{cut}}
=
-2a\,s_pF_s
+O(ar_0+ar_0^2+a^2r_0^{-4}).
\]

### Sign and cutoff independence

For an annulus \(A=\{\rho<r<R\}\), with \(\chi=1\) near \(r=\rho\) and \(\chi=0\) near \(r=R\),
\[
\int_A\partial_a\partial_b(\chi f)\,dx
=
-\int_{S_\rho}n_a\partial_bf\,dS,
\]
because the outward annular normal at the inner boundary is \(-n\). Thus
\[
-\int_A\mathcal R^{\rm lin}(\chi h)
\]
is the positive radial flux implemented by the script. Since \(h\) is homogeneous of degree \(-2\), the integrand \(n\,\partial h\,dS\) has degree zero; the result is independent of the inner radius and of the cutoff profile.

### Curvature convention and two-form normalization

The script’s constant-curvature jet gives
\[
R_{1212}=K,\qquad
\mathcal R|_{\Lambda^\pm}=KI,
\]
so its curvature sign agrees with the note.

For antisymmetric-matrix representatives of two-forms,
\[
|\alpha|^2=\frac12\sum_{ij}\alpha_{ij}^2,
\]
and therefore
\[
\langle\mathcal R(\alpha),\beta\rangle
=\frac14R_{ijkl}\alpha_{ij}\beta_{kl}.
\]
The script’s factor \(1/4\) is correct.

With orientation \(dx^{1234}>0\),
\[
w_1=\frac{dx^{12}+dx^{34}}{\sqrt2}
=\frac{\omega}{\sqrt2}
\]
is a unit self-dual form, and the remaining `Wp` basis signs are also correct.

### Exact output

The exact sphere integration gives
\[
\boxed{
\Phi^{++}=
\begin{pmatrix}
\pi^2&0&0\\
0&0&0\\
0&0&0
\end{pmatrix},
\qquad
\Phi^{--}=\frac{\pi^2}{3}I,
\qquad
\Phi^{+-}=0 .
}
\]
The scalar flux is
\[
F_s=4\operatorname{tr}\Phi^{++}=4\pi^2.
\]

An independent scalar check is
\[
\operatorname{tr}h=\frac2{r^2},\qquad
\partial_jh_{ij}=-\frac{2x_i}{r^4},
\]
so
\[
n_i\bigl(\partial_jh_{ij}-\partial_i\operatorname{tr}h\bigr)
=\frac2{r^3},
\]
and hence
\[
-\int s^{\rm lin}(\chi h)\,dx
=\int_{S_r^3}\frac2{r^3}\,dS
=4\pi^2.
\]

### Script defect

Both denominator assertions contain
```python
... if False else 0
```
and therefore only assert \(0=0\). They do not check that each denominator is a constant times a power of \(t^2\). That property is true for this calculation, so the output is unaffected, but the script does not itself certify it. `sphere_integral` is unused.

---

## 4. Assembly

Using \(F_s=4\operatorname{tr}\Phi^{++}\),
\[
\begin{aligned}
4\Delta A_++\frac1{12}\Delta S
&=
-8a\langle W_p^+,\Phi^{++}\rangle
-\frac a6s_pF_s+O(\text{errors})\\
&=
-8a\left\langle W_p^++\frac{s_p}{12}I,\Phi^{++}\right\rangle
+O(\text{errors})\\
&=
-8a\langle\mathbf R_p^+,\Phi^{++}\rangle+O(\text{errors}).
\end{aligned}
\]
Since the frame sends \(\zeta\) to \(w_1\),
\[
\langle\mathbf R_p^+,\Phi^{++}\rangle
=\pi^2\mathbf R_p^+(\zeta,\zeta).
\]
Therefore
\[
4\Delta A_++\frac1{12}\Delta S
=
-8\pi^2a\,\mathbf R_p^+(\zeta,\zeta)
+O\!\left(ar_0+a^2r_0^{-4}+ar_0^2+a^2|\log a|\right).
\]
For \(r_0=a^{1/5}\),
\[
ar_0=a^{6/5},\qquad
a^2r_0^{-4}=a^{6/5},
\]
while the remaining terms are smaller. Hence
\[
\boxed{
P(\hat g_a)
=
P(g)+8\pi^2\bigl(1-a\,\mathbf R_p^+(\zeta,\zeta)\bigr)
+O(a^{6/5}).
}
\]

Thus **Theorem F is mathematically correct after repairing the inner proof**, but it is not proved literally by the displayed volume estimate in the source.

For Einstein \(g\), \(s_g=4\lambda\) and
\[
J(\hat g)-P(\hat g)
=\frac14\int(s_{\hat g}-4\lambda)^2\,dV_{\hat g}.
\]
The repaired core and annular estimates give
\[
J(\hat g)-P(\hat g)
=O(a^2|\log a|+a^2r_0^{-4})
=O(a^{6/5}),
\]
so the same expansion holds for \(J\). Merely saying that the first variation vanishes is not by itself enough to establish the stated remainder; the scalar-square estimate completes the argument.

---

## 5. Consistency checks

### Kähler topology

The flux gives
\[
\Delta\int s\,dV=-4\pi^2a.
\]
Since \(\operatorname{area}(E)=\pi a\),
\[
4\pi\,\operatorname{area}(E)=4\pi^2a,
\]
so the scalar drop is correct.

However, the note writes
\[
c_1(\hat M)\cdot[\hat\omega]
=c_1(M)\cdot[\omega]-\operatorname{area}(E)/\pi.
\]
Under the simultaneously stated convention
\[
\int s\,dV=4\pi\,c_1\cdot[\omega],
\]
the correct formula is
\[
\boxed{
c_1(\hat M)\cdot[\hat\omega]
=c_1(M)\cdot[\omega]-\operatorname{area}(E).
}
\]
The displayed `/\pi` is a normalization typo. The numerical conclusion \(4\pi^2a\) uses the correct formula.

### Complex-space-form slopes

For a Kähler–Einstein surface,
\[
\mathbf R^+
=\operatorname{diag}\left(\frac s4,0,0\right)
\]
in the Kähler self-dual frame. Therefore:

- \(\mathbb{CH}^2\), \(s=-24\):
  \[
  \mathbf R^+=\operatorname{diag}(-6,0,0),
  \]
  so the slopes of \(P/(8\pi^2)\) are \(+6\) in the aligned direction and \(0\) on \(\omega^\perp\).

- Fubini–Study with \(s=+24\):
  the aligned slope is \(-6\).

Thus the stated \(+6/0/-6\) check is correct, provided the \(-6\) is understood as the positively curved Fubini–Study case, not another \(s=-24\) direction.

---

## 6. Lemma Q′

Mayer–Vietoris for \(U_0=U\cup V\), with \(U\cap V\simeq S^3\), gives
\[
H_2(U)\oplus H_2(V)\cong H_2(U_0)\cong\mathbb R,
\qquad
H_1(U)\oplus H_1(V)=0.
\]
Since \(\tau(U)=-1\), \(b_2(U)\ge1\); hence
\[
b_2(U)=1,\qquad b_1(U)=0.
\]
For a connected compact \(U\) with boundary,
\[
\chi(U)=1+b_2(U)-b_3(U)=2-b_3(U)\le2.
\]
That is all the proof needs. Under additional standard separation hypotheses one can obtain \(b_3(U)=0\), but claiming exact equality \(\chi(U)=2\) is unnecessary.

For a ball-side collar that is orientation-preservingly \(C^2\)-close after rescaling to a Euclidean annulus, the boundary transgressions satisfy
\[
\mathcal B_{\rm GB}=8\pi^2+O(\varepsilon),
\qquad
\mathcal B_{\rm sign}=O(\varepsilon).
\]
One rigorous way to justify this quantitatively is to interpolate within the collar to an exactly flat annulus; the scale-invariant curvature-integral error is \(O(\varepsilon)\), after which one attaches a flat exterior.

The signature identity and \(\tau(U)=-1\) imply
\[
\int_U(|W^+|^2-|W^-|^2)
=-12\pi^2+O(\varepsilon),
\]
hence
\[
\int_U|W|^2\ge12\pi^2-C\varepsilon.
\]
Gauss–Bonnet gives
\[
P(U)
=
2\int_U|W|^2+\frac1{12}\int_Us^2
-16\pi^2\chi(U)+16\pi^2+O(\varepsilon).
\]
Using \(s^2\ge0\), \(\chi(U)\le2\), and the Weyl bound,
\[
\boxed{
P(U)\ge8\pi^2-C\varepsilon.
}
\]

Thus **Lemma Q′ is correct**, with the implicit requirements:

1. \(\Sigma\) separates and \(U\) is the ball-side component;
2. the annular identification is orientation-preserving;
3. the \(C^2\)-closeness is interpreted so that the characteristic boundary terms are \(O(\varepsilon)\)-close.

The stated consequence also uses \(P(U_0)\ge P(U)\), which is valid since the density is nonnegative. The external certified numerical value \(0.99584841\cdot8\pi^2\) is not independently established by the three supplied files.

---

## 7. Lemma R

For normalized \(\mathbb{CH}^2\),
\[
s=-24,\qquad
W^+=\operatorname{diag}(-4,2,2),\qquad
W^-=0.
\]
Therefore
\[
|W^+|^2=24,\qquad \frac{s^2}{24}=24,
\]
and the Euler and signature densities are
\[
\boxed{
\frac{24+24}{8\pi^2}=\frac6{\pi^2},
\qquad
\frac{24}{12\pi^2}=\frac2{\pi^2}.
}
\]

If an Einstein metric agrees with the full normalized complex-hyperbolic metric on an open collar, analyticity in harmonic coordinates propagates the full locally symmetric curvature tensor across connected \(U\). Thus the characteristic densities are constant throughout \(U\). Comparing with the complex-hyperbolic ball sharing the exact collar cancels the boundary terms, giving
\[
\Delta\chi=\frac6{\pi^2}\Delta V,
\qquad
\Delta\tau=\frac2{\pi^2}\Delta V,
\]
and hence
\[
\boxed{\Delta\chi=3\Delta\tau.}
\]
Therefore \(\Delta\chi\ne3\Delta\tau\) excludes an Einstein extension. If \(P(U)=0\), then \(\operatorname{Ric}^\circ=0\), so the metric is Einstein; consequently every such metric has \(P(U)>0\).

The necessary interpretation is:

- “exact \(\mathbb{CH}^2\)-collar” must mean equality with the **full** normalized complex-hyperbolic metric, not merely \(\operatorname{Ric}=-6g\);
- the collar identification must preserve the chosen complex orientation. Reversing orientation changes the signature sign.

Thus **Lemma R itself is correct as stated under that interpretation**.

### Limitation of its stated consequence

For a cell with \(k\) blow-ups and \(\ell\) handles,
\[
(\Delta\chi,\Delta\tau)=(k-2\ell,-k).
\]
The proportionality condition becomes
\[
k-2\ell=-3k
\quad\Longleftrightarrow\quad
\ell=2k.
\]
Hence the Chern–Weil contradiction does **not** exclude exact Einstein cells in the exceptional family \(\ell=2k\). In particular, the sentence suggesting the argument covers all blow-up/handle cells is not justified by Lemma R alone.

A stronger geometric filling-rigidity theorem—showing that a compact locally complex-hyperbolic manifold with an exact geodesic-sphere collar must be the corresponding ball—would cover these proportional cases, but that theorem and its needed global hypotheses are not proved in the supplied note. Therefore the broad consequence concerning every \(\mathfrak P_{k,\ell}\) has a gap for \(\ell=2k\).

---

## Final status

| Statement | Status |
|---|---|
| Exact topological reduction | Correct as written |
| Burns normalization and exceptional area | Correct |
| Pointwise linearized \(++\) and scalar cancellation | Correct |
| Inner curvature conclusion | Correct after a two-region repair |
| Inner volume-form estimate | False as written |
| Cut-annulus expansion | Correct |
| Flux sign, cutoff independence, \(1/4\) pairing, orientation | Correct |
| JSON flux matrices | Correct |
| Script denominator checks | Vacuous, but output unaffected |
| Assembly into \(-8\pi^2x_0\mathbf R^+(\zeta,\zeta)\) | Correct |
| Theorem F | Correct, but proof requires the stated repair |
| Einstein \(J\)-version | Correct with scalar-square estimate |
| Kähler numerical check | Correct |
| Kähler cohomology formula in note | Wrong by a factor of \(\pi\) |
| Complex-space-form slopes | Correct |
| Lemma Q′ | Correct with implicit separation/orientation/boundary hypotheses |
| Lemma R | Correct for a full orientation-preserving exact \(\mathbb{CH}^2\) collar |
| Lemma R’s all-cell consequence | Not proved for \(\ell=2k\) by the supplied proportionality argument |