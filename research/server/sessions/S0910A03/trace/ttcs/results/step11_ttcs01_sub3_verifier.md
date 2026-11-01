# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/circle_reduction_weyl.py",
    "Sessions/S0910A03/workspace/scripts/verify_static_incompatibility.py",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Verify the following static circle reduction formulas for a 4D Einstein metric with Ric = -g.

For a static Kaluza-Klein metric g = g_B + ℓ(x)² dψ² with Ric = -g:
1. The Einstein equations give: Ric_B = h - g_B and Δ_B ℓ = ℓ, where h = Hess_B(ℓ)/ℓ and tr(h) = 1.
2. The curvature operator on Λ²₊ (Besse convention) in the adapted SD basis has matrix R̂₊ with:
   - Diagonal: (R̂₊)₁₁ = 2h₃₃ - 1, (R̂₊)₂₂ = 2h₂₂ - 1, (R̂₊)₃₃ = 2h₁₁ - 1
   - Off-diagonal: (R̂₊)₁₂ = -2h₂₃, (R̂₊)₁₃ = 2h₁₃, (R̂₊)₂₃ = -2h₁₂
3. Hence W⁺ = R̂₊ + (1/3)I has: (W⁺)₁₁ = 2h₃₃ - 2/3, (W⁺)₂₂ = 2h₂₂ - 2/3, (W⁺)₃₃ = 2h₁₁ - 2/3, etc.
4. tr(R̂₊) = -1 = s/4, tr(W⁺) = 0.
5. The calibrated spectrum (-1/6, 1/12, 1/12) requires h = diag(3/8, 3/8, 1/4) in the eigenbasis.

For a cohomogeneity-one model g = dt² + a(t)² g_{S²} + ℓ(t)² dψ²:
6. The calibrated spectrum + Einstein give a'' = 3a/8 AND (a')² = 1 + a²/4, but differentiating the second gives a'' = a/4 ≠ 3a/8. Contradiction.
7. The ONLY constant-eigenvalue static Einstein has u = v = 1/3 (i.e., h = I/3, W⁺ = 0).

For the twisted case g = g_B + ℓ²(dψ + A)²:
8. The modified Laplacian is Δ_B ℓ + (ℓ³/4)|F|² = ℓ, giving tr(h) = 1 - ℓ²|F|²/4 < 1.
9. Near a smooth NUT (ℓ → 0), twist corrections to W⁺ are O(ℓ²), so the static formula W⁺ ≈ 2J(h - I/3) holds to leading order.

Check all signs, factors, and index assignments. Verify against the known results: constant curvature K = -1/3 gives h = I/3 and W⁺ = 0; the Taub-NUT-AdS has W⁺ = 0 but nontrivial warping (so twist must compensate).

## Output

# Scientific verification memo

Fix an oriented orthonormal frame \(e_1,e_2,e_3\) on \(B\), put
\[
e_4=\ell^{-1}\partial_\psi,
\]
and use the orthonormal self-dual basis
\[
\omega_1=\frac{e^{12}+e^{34}}{\sqrt2},\qquad
\omega_2=\frac{e^{13}-e^{24}}{\sqrt2},\qquad
\omega_3=\frac{e^{14}+e^{23}}{\sqrt2}.
\]
The curvature operator convention is the Besse block convention
\[
\widehat R|_{\Lambda^+}=W^++\frac{s}{12}I,
\]
so a constant-curvature metric of sectional curvature \(K\) has
\(\widehat R|_{\Lambda^+}=K I\). Take \(\Delta=\operatorname{tr}\operatorname{Hess}\).

## 1. Static Einstein equations

For
\[
g=g_B+\ell^2d\psi^2
\]
the standard warped-product formulas are
\[
\operatorname{Ric}_g(X,Y)
=\operatorname{Ric}_B(X,Y)-\frac{\operatorname{Hess}_B\ell(X,Y)}{\ell},
\]
and
\[
\operatorname{Ric}_g(e_4,e_4)=-\frac{\Delta_B\ell}{\ell}.
\]
Thus \(\operatorname{Ric}_g=-g\) gives
\[
\boxed{\operatorname{Ric}_B=h-g_B,\qquad \Delta_B\ell=\ell,}
\qquad
h=\frac{\operatorname{Hess}_B\ell}{\ell},
\]
and consequently
\[
\boxed{\operatorname{tr}h=1.}
\]
Item 1 is correct. It also gives \(s_B=-2\) and \(s_g=-4\).

If \(B\) were closed and \(\ell>0\) globally, integrating \(\Delta_B\ell=\ell\) would be impossible. Thus this static model is naturally local, noncompact, or accompanied by fiber degeneration.

## 2. Static curvature operator: the stated matrix has the wrong dependence on \(h\)

The warped-product curvature components are
\[
R_{abcd}=R^B_{abcd},\qquad
R_{a4b4}=-h_{ab},\qquad
R_{abc4}=0.
\]
In three dimensions,
\[
R^B_{abcd}
=(\operatorname{Ric}_B\owedge g_B)_{abcd}
-\frac{s_B}{2}(g_B\owedge g_B)_{abcd}
\]
in component form. Using \(\operatorname{Ric}_B=h-I\), \(s_B=-2\), and
\(\operatorname{tr}h=1\), representative components are
\[
R^B_{1212}=-h_{33},\qquad
R^B_{1213}=h_{23},\qquad
R^B_{1223}=-h_{13},\qquad
R^B_{1323}=h_{12}.
\]

Directly evaluating \(\langle\widehat R\omega_i,\omega_j\rangle\) gives
\[
\boxed{
\widehat R_+=
\begin{pmatrix}
-h_{33}&h_{23}&-h_{13}\\
h_{23}&-h_{22}&h_{12}\\
-h_{13}&h_{12}&-h_{11}
\end{pmatrix}.}
\]
For example,
\[
\langle\widehat R\omega_1,\omega_2\rangle
=\frac12(R_{1213}-R_{3424})
=\frac12(h_{23}+h_{23})
=h_{23}.
\]

Changing signs of the adapted SD basis conjugates this matrix by a diagonal orthogonal matrix, so some off-diagonal signs can change. The factor and diagonal dependence cannot change: \(\widehat R_+\) is orthogonally conjugate to \(-h\), and therefore
\[
\boxed{\operatorname{Spec}(\widehat R_+)=-\operatorname{Spec}(h).}
\]

Hence the matrix
\[
(2h_{33}-1,\,2h_{22}-1,\,2h_{11}-1)
\]
with off-diagonal magnitudes \(2|h_{ij}|\) is not the static curvature operator in the stated convention. No change of SD basis can reconcile the two formulas for general \(h\), since their eigenvalue multisets are respectively
\[
\{-\eta_1,-\eta_2,-\eta_3\}
\quad\text{and}\quad
\{2\eta_1-1,2\eta_2-1,2\eta_3-1\}.
\]

## 3. The corrected \(W^+\) formula

Since \(s=-4\),
\[
\widehat R_+=W^+-\frac13I,
\qquad
W^+=\widehat R_++\frac13I.
\]
Therefore
\[
\boxed{
W^+=
\begin{pmatrix}
\frac13-h_{33}&h_{23}&-h_{13}\\
h_{23}&\frac13-h_{22}&h_{12}\\
-h_{13}&h_{12}&\frac13-h_{11}
\end{pmatrix}.}
\]
Thus Item 3 has the correct scalar shift \(+\frac13I\), but its entries inherit the incorrect matrix from Item 2.

The trace identities are
\[
\operatorname{tr}\widehat R_+=-\operatorname{tr}h=-1=\frac{s}{4},
\qquad
\operatorname{tr}W^+=0.
\]
Item 4 is correct.

For \(h=I/3\),
\[
\widehat R_+=-\frac13I,\qquad W^+=0.
\]
Moreover \(\operatorname{Ric}_B=-\frac23g_B\); in dimension three this gives sectional curvature \(-1/3\), while \(R_{a4b4}=-1/3\). This reproduces the four-dimensional constant-curvature metric with \(K=-1/3\).

## 4. Correct \(h\)-spectrum for the calibrated \(W^+\)-spectrum

Because
\[
\operatorname{Spec}(W^+)
=\left\{\frac13-\eta_i:\eta_i\in\operatorname{Spec}(h)\right\},
\]
the spectrum
\[
\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
requires
\[
\boxed{\operatorname{Spec}(h)=\left(\frac12,\frac14,\frac14\right).}
\]

More explicitly, if \(W^+\) is diagonal in the displayed \(\omega_i\) basis with
\[
(W^+_{11},W^+_{22},W^+_{33})
=\left(-\frac16,\frac1{12},\frac1{12}\right),
\]
then
\[
(h_{11},h_{22},h_{33})
=\left(\frac14,\frac14,\frac12\right).
\]
Thus Item 5’s \((3/8,3/8,1/4)\) is not compatible with the Besse curvature operator.

## 5. Cohomogeneity-one calculation

For
\[
g=dt^2+a(t)^2g_{S^2}+\ell(t)^2d\psi^2,
\]
put
\[
u=\frac{\ell''}{\ell},\qquad
v=\frac{a'\ell'}{a\ell}.
\]
Then
\[
h=\operatorname{diag}(u,v,v)
\]
in the base frame \(e_1=\partial_t,e_2,e_3\), and
\[
\operatorname{Spec}(W^+)
=\left(\frac13-v,\frac13-v,\frac13-u\right).
\]
The calibrated spectrum therefore requires
\[
\boxed{u=\frac12,\qquad v=\frac14.}
\]

The Einstein equations are
\[
-2\frac{a''}{a}=u-1,
\]
\[
-\frac{a''}{a}+\frac{1-(a')^2}{a^2}=v-1,
\]
\[
u+2v=1.
\]
Substitution gives
\[
a''=\frac14a
\]
and
\[
-\frac14+\frac{1-(a')^2}{a^2}=-\frac34,
\]
hence
\[
(a')^2=1+\frac12a^2.
\]
Since this identity makes \(a'\neq0\), differentiation yields
\[
a''=\frac12a,
\]
contradicting \(a''=a/4\).

Thus the incompatibility survives, but Item 6’s displayed equations
\[
a''=\frac38a,\qquad (a')^2=1+\frac14a^2
\]
come from the incorrect calibrated values for \(h\).

For constant \(u,v\), write
\[
k=\frac{1-(a')^2}{a^2}
=v-\frac12-\frac u2.
\]
Then
\[
(a')^2=1-ka^2.
\]
Differentiation, together with the first Einstein equation, gives
\[
-k=\frac{1-u}{2}.
\]
Comparing the two expressions for \(k\) gives \(u=v\); the trace equation then gives
\[
\boxed{u=v=\frac13.}
\]
Consequently \(h=I/3\) and \(W^+=0\). Item 7 is correct within this cohomogeneity-one ansatz. The displayed ODE does not by itself establish the same statement for every possible three-dimensional static base.

## 6. Twisted vertical equation: sign and norm factor

For
\[
g=g_B+\ell^2(d\psi+A)^2,\qquad F=dA,
\]
let
\[
|F|_{\Lambda^2}^2=\frac12F_{ab}F_{ab}.
\]
The vertical Ricci component is
\[
\operatorname{Ric}_g(e_4,e_4)
=-\frac{\Delta_B\ell}{\ell}
+\frac{\ell^2}{4}F_{ab}F_{ab}
=-\frac{\Delta_B\ell}{\ell}
+\frac{\ell^2}{2}|F|_{\Lambda^2}^2.
\]
Therefore \(\operatorname{Ric}(e_4,e_4)=-1\) gives
\[
\boxed{
\Delta_B\ell-\frac{\ell^3}{4}F_{ab}F_{ab}=\ell,
}
\]
or equivalently
\[
\boxed{
\Delta_B\ell-\frac{\ell^3}{2}|F|_{\Lambda^2}^2=\ell.
}
\]
Thus
\[
\boxed{
\operatorname{tr}h
=1+\frac{\ell^2}{4}F_{ab}F_{ab}
=1+\frac{\ell^2}{2}|F|_{\Lambda^2}^2.
}
\]
It is larger than \(1\) wherever \(F\neq0\) and \(\ell>0\). Item 8 has the opposite sign. If the notation \(|F|^2\) means the raw contraction \(F_{ab}F_{ab}\), the coefficient \(1/4\) is correct after changing the displayed plus to a minus.

## 7. Twist terms near a NUT

The relevant curvature components include
\[
R_{a4b4}
=-h_{ab}+\frac{\ell^2}{4}F_{ac}F_{bc},
\]
and
\[
R_{abcd}
=R^B_{abcd}
-\frac{\ell^2}{4}
\left(2F_{ab}F_{cd}+F_{ac}F_{bd}-F_{ad}F_{bc}\right).
\]
Mixed components also contain first-order terms of the form
\[
R_{abc4}
=-\frac{\ell}{2}\nabla_cF_{ab}
-\ell_cF_{ab}
+\frac12\ell_aF_{bc}
-\frac12\ell_bF_{ac},
\]
for the horizontal-lift convention
\([e_a,e_b]^{\mathrm{vert}}=-\ell F_{ab}e_4\).

Thus even when \(F\) remains bounded, the general correction is not automatically \(O(\ell^2)\): mixed curvature contains \(\ell\nabla F\) and \((\nabla\ell)F\). At an isolated smooth NUT, the quotient-base norm of \(F\) generally grows as the fiber closes, so the quadratic terms need not tend to zero either.

The supplied Taub–NUT–AdS metric gives an explicit computation. Write its radial function as
\[
V(r)=\frac{r-\nu}{r+\nu}
\left(1+\frac{(r-\nu)(r+3\nu)}3\right),
\]
so that
\[
\ell=2\nu\sqrt V,\qquad b^2=r^2-\nu^2.
\]
Then
\[
h_{rr}=\frac{V''}{2},\qquad
h_{\mathrm{ang}}=\frac{rV'}{2(r^2-\nu^2)},
\]
while
\[
F_{\hat\theta\hat\phi}=-\frac1{r^2-\nu^2},
\qquad
F_{ab}F_{ab}=\frac{2}{(r^2-\nu^2)^2}.
\]
Direct substitution verifies
\[
h_{rr}+2h_{\mathrm{ang}}
=1+\frac{\ell^2}{2(r^2-\nu^2)^2},
\]
in agreement with the corrected vertical equation.

Set \(x=r-\nu\). Near the NUT,
\[
V=\frac{x}{2\nu}+O(x^2),\qquad
\ell^2=2\nu x+O(x^2),
\]
and
\[
h_{\mathrm{ang}}
=\frac{1}{8\nu x}+O(1)
=\frac{1}{4\ell^2}+O(1).
\]
Also
\[
\ell^2F_{\hat\theta\hat\phi}^2
\asymp \ell^{-2}.
\]
Therefore the static contribution itself diverges in the quotient-adapted frame, and the twist terms cancel it so that the total four-dimensional curvature remains smooth. Item 9 is false for a smooth NUT. In particular, \(h\) does not approach \(I/3\) in this model.

This also explains Taub–NUT–AdS: in one orientation one Weyl block vanishes, despite nontrivial warping, because connection, base, and Hessian terms compensate. Reversing orientation exchanges \(W^+\) and \(W^-\).

## 8. Supplied scripts

Two concrete script features affect their conclusions:

- `circle_reduction_weyl.py` Part 1 hard-codes \(2J(h-I/3)\); the isotropic test \(h=I/3\) cannot distinguish it from the corrected formula because both give zero there. The “calibrated” test merely solves the hard-coded equation.
- The Taub–NUT portion computes only \(h\), then infers the twist contribution from the known half-flat result. It does not compute the full twisted curvature operator.
- In Part 4,
  ```python
  F_mag_sq = 1/rho_sq
  ```
  has the wrong power. Since \(F_{\hat\theta\hat\phi}=-1/\rho^2=-1/\texttt{rho\_sq}\), its square is
  ```python
  1/rho_sq**2
  ```
- `verify_static_incompatibility.py` performs valid ODE algebra after inserting \(u=1/4,v=3/8\), but those inserted values arise from the incorrect static curvature matrix. The corrected values \(u=1/2,v=1/4\) produce the alternative contradiction above.

### Final formula assessment

\[
\begin{array}{c|c}
\text{Item}&\text{Result}\\ \hline
1&\text{Correct}\\
2&\text{Incorrect; }\widehat R_+\text{ is orthogonally conjugate to }-h\\
3&\text{The }+\frac13I\text{ shift is correct; the entries are not}\\
4&\text{Correct}\\
5&\text{Replace by }\operatorname{Spec}(h)=(1/2,1/4,1/4)\\
6&\text{The contradiction remains, with }a''=a/4\text{ versus }a''=a/2\\
7&\text{Correct for the stated cohomogeneity-one model}\\
8&\text{Sign reversed; }\operatorname{tr}h>1\text{ where twist is present}\\
9&\text{False in general and explicitly false near Taub--NUT}
\end{array}
\]