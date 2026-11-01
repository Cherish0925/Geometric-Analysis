# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 11,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step11_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step11_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

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

## Integrated Scientific Memo

## Verification memo

Fix an oriented orthonormal base frame \(e_1,e_2,e_3\), let \(e_4=\ell^{-1}\partial_\psi\), and use
\[
\omega_1=\frac{e^{12}+e^{34}}{\sqrt2},\qquad
\omega_2=\frac{e^{13}-e^{24}}{\sqrt2},\qquad
\omega_3=\frac{e^{14}+e^{23}}{\sqrt2}.
\]
Take \(\Delta=\operatorname{tr}\operatorname{Hess}\) and Besse’s convention
\[
\widehat R|_{\Lambda^+}=W^++\frac{s}{12}I.
\]

The proposed formulas are not all correct. In particular, Items 2, 5, 6, 8, and 9 require correction.

### 1. Static Einstein reduction

For
\[
g=g_B+\ell^2d\psi^2,
\]
the warped-product identities are
\[
\operatorname{Ric}_g(X,Y)
 =\operatorname{Ric}_B(X,Y)-\ell^{-1}\operatorname{Hess}_B\ell(X,Y),
\]
\[
\operatorname{Ric}_g(e_4,e_4)=-\ell^{-1}\Delta_B\ell.
\]
Thus \(\operatorname{Ric}_g=-g\) gives
\[
\boxed{\operatorname{Ric}_B=h-g_B,\qquad \Delta_B\ell=\ell,\qquad
h=\ell^{-1}\operatorname{Hess}_B\ell,}
\]
and therefore
\[
\boxed{\operatorname{tr}h=1.}
\]
Hence Item 1 is correct. Also \(s_B=-2\) and \(s_g=-4\).

### 2–4. Correct static curvature and Weyl matrices

The relevant curvature components are
\[
R_{abcd}=R^B_{abcd},\qquad R_{a4b4}=-h_{ab},\qquad R_{abc4}=0.
\]
Since \(B\) is three-dimensional, \(\operatorname{Ric}_B=h-I\), \(s_B=-2\), and \(\operatorname{tr}h=1\), one obtains
\[
\boxed{
\widehat R_+=
\begin{pmatrix}
-h_{33}&h_{23}&-h_{13}\\
h_{23}&-h_{22}&h_{12}\\
-h_{13}&h_{12}&-h_{11}
\end{pmatrix}.}
\]
Other sign choices for the adapted SD basis can change some off-diagonal signs by diagonal orthogonal conjugation, but neither the factor nor the diagonal dependence. Intrinsically,
\[
\boxed{\operatorname{Spec}(\widehat R_+)=-\operatorname{Spec}(h).}
\]

Therefore Item 2’s entries \(2h_{ii}-1\) and off-diagonal factor \(2\) are incorrect.

Because \(s=-4\),
\[
\widehat R_+=W^+-\frac13I,
\]
so
\[
\boxed{
W^+=
\begin{pmatrix}
\frac13-h_{33}&h_{23}&-h_{13}\\
h_{23}&\frac13-h_{22}&h_{12}\\
-h_{13}&h_{12}&\frac13-h_{11}
\end{pmatrix}.}
\]
Thus Item 3 has the correct scalar shift \(+\frac13I\), but inherits the incorrect entries from Item 2.

The trace statements are correct:
\[
\boxed{\operatorname{tr}\widehat R_+=-\operatorname{tr}h=-1=\frac{s}{4}},
\qquad
\boxed{\operatorname{tr}W^+=0}.
\]

The constant-curvature calibration also works correctly:
\[
h=\frac13I
\quad\Longrightarrow\quad
\widehat R_+=-\frac13I,\qquad W^+=0.
\]
Indeed, the resulting four-metric has sectional curvature \(-1/3\).

### 5. Correct Hessian spectrum for the calibrated Weyl spectrum

If \(\eta_i\) are the eigenvalues of \(h\), then
\[
\operatorname{Spec}(W^+)=\left\{\frac13-\eta_i\right\}.
\]
Consequently,
\[
\operatorname{Spec}(W^+)
 =\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
requires
\[
\boxed{\operatorname{Spec}(h)=\left(\frac12,\frac14,\frac14\right),}
\]
not \((3/8,3/8,1/4)\).

With the displayed basis and the simple Weyl eigenvalue placed in the first slot,
\[
(W^+_{11},W^+_{22},W^+_{33})
=\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
corresponds to
\[
(h_{11},h_{22},h_{33})
=\left(\frac14,\frac14,\frac12\right),
\]
because of the \(1\leftrightarrow3\) index pairing.

### 6. Cohomogeneity-one contradiction

For
\[
g=dt^2+a(t)^2g_{S^2}+\ell(t)^2d\psi^2,
\]
set
\[
u=\frac{\ell''}{\ell},\qquad
v=\frac{a'\ell'}{a\ell}.
\]
Then
\[
h=\operatorname{diag}(u,v,v),\qquad
\operatorname{Spec}(W^+)
=\left(\frac13-v,\frac13-v,\frac13-u\right).
\]
The calibrated spectrum therefore gives
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
Substitution yields
\[
\boxed{a''=\frac14a},
\]
and
\[
-\frac14+\frac{1-(a')^2}{a^2}=-\frac34,
\]
hence
\[
\boxed{(a')^2=1+\frac12a^2}.
\]
This implies \(a'\ne0\); differentiating gives
\[
\boxed{a''=\frac12a},
\]
contradicting \(a''=a/4\).

Thus the intended incompatibility is valid, but Item 6’s numerical equations
\[
a''=\frac38a,\qquad (a')^2=1+\frac14a^2
\]
are consequences of the incorrect static curvature formula.

### 7. Constant-eigenvalue conclusion

Suppose \(u,v\) are constant. From the angular Einstein equation,
\[
k:=\frac{1-(a')^2}{a^2}
=v-\frac12-\frac u2.
\]
Thus \((a')^2=1-ka^2\), and differentiation gives
\[
-k=\frac{a''}{a}=\frac{1-u}{2}.
\]
Comparing the two expressions for \(k\) gives \(u=v\). The trace equation
\(u+2v=1\) then yields
\[
\boxed{u=v=\frac13,\qquad h=\frac13I,\qquad W^+=0.}
\]

Item 7 is therefore correct **within the stated cohomogeneity-one ansatz**. This ODE argument does not establish uniqueness among all static Einstein circle metrics with arbitrary three-dimensional base geometry.

### 8. Twisted vertical Einstein equation

For
\[
g=g_B+\ell^2(d\psi+A)^2,\qquad F=dA,
\]
one has
\[
\operatorname{Ric}_g(e_4,e_4)
=-\frac{\Delta_B\ell}{\ell}
+\frac{\ell^2}{4}F_{ab}F_{ab}.
\]
Hence \(\operatorname{Ric}(e_4,e_4)=-1\) gives
\[
\boxed{\Delta_B\ell-\frac{\ell^3}{4}F_{ab}F_{ab}=\ell.}
\]
If
\[
|F|_{\Lambda^2}^2=\frac12F_{ab}F_{ab},
\]
this is equivalently
\[
\boxed{\Delta_B\ell-\frac{\ell^3}{2}|F|_{\Lambda^2}^2=\ell.}
\]
Therefore
\[
\boxed{\operatorname{tr}h
=1+\frac{\ell^2}{4}F_{ab}F_{ab}
=1+\frac{\ell^2}{2}|F|_{\Lambda^2}^2.}
\]
Thus Item 8 has the wrong sign: twist makes \(\operatorname{tr}h>1\), not \(<1\), wherever \(F\ne0\).

The coefficient depends on whether \(|F|^2\) denotes the two-form norm \(\frac12F_{ab}F_{ab}\) or the raw contraction \(F_{ab}F_{ab}\).

### 9. Behavior near a smooth NUT

Twisted curvature contains both quadratic and mixed terms. Schematically,
\[
R_{a4b4}
=-h_{ab}+\frac{\ell^2}{4}F_{ac}F_{bc},
\]
\[
R_{abcd}
=R^B_{abcd}
-\frac{\ell^2}{4}
\left(2F_{ab}F_{cd}+F_{ac}F_{bd}-F_{ad}F_{bc}\right),
\]
while \(R_{abc4}\) contains terms of orders
\[
\ell\nabla F,\qquad (\nabla\ell)F.
\]
Consequently, twist corrections are not generally \(O(\ell^2)\), even if \(F\) is bounded; mixed terms can be larger. Near a NUT, the quotient-base norm of \(F\) typically diverges as the fiber closes.

Taub–NUT–AdS gives an explicit counterexample to Item 9. Write
\[
V(r)=\frac{r-\nu}{r+\nu}
\left(1+\frac{(r-\nu)(r+3\nu)}3\right),
\quad
\ell=2\nu\sqrt V,
\quad
b^2=r^2-\nu^2.
\]
Then
\[
h_{rr}=\frac{V''}{2},\qquad
h_{\mathrm{ang}}=\frac{rV'}{2(r^2-\nu^2)},
\]
and
\[
F_{\hat\theta\hat\phi}=-\frac1{r^2-\nu^2}.
\]
The corrected vertical equation is verified by
\[
h_{rr}+2h_{\mathrm{ang}}
=1+\frac{\ell^2}{2(r^2-\nu^2)^2}.
\]

Putting \(x=r-\nu\), near the NUT,
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
Moreover,
\[
\ell^2F_{\hat\theta\hat\phi}^{\,2}\asymp \ell^{-2}.
\]
Thus neither the static Hessian contribution nor the twist correction is small in the quotient-adapted frame: both can diverge and cancel, leaving a smooth four-dimensional curvature tensor. In particular,
\[
h\not\to \frac13I
\]
in this model.

This is precisely compatible with Taub–NUT–AdS being half-conformally flat in one orientation despite nontrivial warping: base curvature, Hessian, connection curvature, and mixed terms compensate. Reversing orientation exchanges \(W^+\) and \(W^-\).

## Final assessment

\[
\begin{array}{c|l}
1 & \text{Correct}\\
2 & \text{Incorrect; }\widehat R_+\text{ is orthogonally conjugate to }-h\\
3 & \text{The }+\frac13I\text{ shift is correct, but the entries are incorrect}\\
4 & \text{Correct}\\
5 & \operatorname{Spec}(h)=(1/2,1/4,1/4)\\
6 & \text{Contradiction valid, but corrected equations are }
a''=a/4,\ (a')^2=1+a^2/2,\ a''=a/2\\
7 & \text{Correct only for the stated cohomogeneity-one constant-}u,v\text{ ansatz}\\
8 & \text{Wrong sign; }\operatorname{tr}h>1\text{ under nonzero twist}\\
9 & \text{False in general and false for Taub--NUT--AdS near its NUT}
\end{array}
\]

The supplied scripts hard-code the incorrect \(2J(h-I/3)\) formula; their isotropic test cannot detect the error because both the correct and incorrect formulas vanish at \(h=I/3\). They also do not compute the full twisted curvature. Additionally, in `circle_reduction_weyl.py`, since
\[
F_{\hat\theta\hat\phi}=-1/\texttt{rho\_sq},
\]
its square is `1/rho_sq**2`, not `1/rho_sq`.