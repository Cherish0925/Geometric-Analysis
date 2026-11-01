# TTCS Independent Branch Record

```json
{
  "step_id": 98,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step98_full_matrix_joint_transition.py",
    "Sessions/S0910A03/workspace/scripts/step98_direct_spd_transition.py",
    "Sessions/S0910A03/workspace/data/step98_direct_spd_N16_interior.json",
    "Sessions/S0910A03/workspace/data/step98_center_residual_resolution.json",
    "Sessions/S0910A03/workspace/data/step98_full_matrix_joint_transition_resolution64.json",
    "Sessions/S0910A03/workspace/scripts/step96_koiso_einstein_cauchy_evolution.py",
    "Sessions/S0910A03/workspace/scripts/step94_charged_koiso_separator.py",
    "Sessions/S0910A03/workspace/notes/step96_charged_koiso_local_evolution_and_joint_matching.md"
  ]
}
```

## Task

Independently verify the mathematical and computational substance of Step 98's full-matrix charged-Koiso matching experiment. Focus on: (i) the Gaussian formulas for all blocks of E=Ric+3g, especially E_nn, E_ni=div K-dH, and E_ij; (ii) whether q=q0^{1/2} exp(X) q0^{1/2} with X_n(0)=±2A and X_nn(0)=2(Rhat+3I) really reproduces q_n=±2K0 and the sign-independent exact Einstein q_nn jet, including noncommutative exponential terms; (iii) invariant norm computation by Cholesky conjugation; (iv) what the low-resolution direct nodal residual decrease actually establishes and what aliasing, endpoint, regularization, underresolution, or overfitting artifacts remain; and (v) propose the most decisive convergence/cross-resolution experiment and residual-projection calculation. Read the actual scripts and JSON evidence. Return corrections with explicit equations, not generic process advice.

## Output

# Scientific verification memo

## 1. Gaussian-coordinate Einstein tensor

For
\[
g=dr^2+q_{ij}(r,s)\,dy^i dy^j,\qquad
K=\frac12 q_r,\qquad W=q^{-1}K,\qquad H=\operatorname{tr}W,
\]
the relevant Christoffel symbols are
\[
\Gamma^r_{ij}=-K_{ij},\qquad
\Gamma^i_{rj}=W^i{}_j,\qquad
\Gamma^i_{jk}=\Gamma(q)^i{}_{jk}.
\]
Differentiating \(H=\operatorname{tr}(q^{-1}K)\) gives
\[
H_r=\operatorname{tr}(q^{-1}K_r)-2\operatorname{tr}(W^2).
\]
Consequently,
\[
\boxed{\operatorname{Ric}_{rr}
=-\operatorname{tr}(q^{-1}K_r)+\operatorname{tr}(W^2),}
\]
\[
\boxed{\operatorname{Ric}_{ri}
=q^{jk}\nabla_jK_{ki}-\partial_iH,}
\]
and
\[
\boxed{\operatorname{Ric}_{ij}
=\operatorname{Ric}(q)_{ij}
-(K_r)_{ij}-HK_{ij}
+2(Kq^{-1}K)_{ij}.}
\]
Thus for \(E=\operatorname{Ric}_g+3g\),
\[
\boxed{E_{rr}
=3-\operatorname{tr}(q^{-1}K_r)+\operatorname{tr}(W^2),}
\]
\[
\boxed{E_{ri}
=q^{jk}\nabla_jK_{ki}-\partial_iH,}
\]
\[
\boxed{E_{ij}
=\operatorname{Ric}(q)_{ij}+3q_{ij}
-(K_r)_{ij}-HK_{ij}
+2(Kq^{-1}K)_{ij}.}
\]

These are exactly the formulas implemented in `full_residual`:

- `Enn = 3 - einsum(qi,Kn) + W2`;
- `mom` computes \(q^{jk}\nabla_jK_{ki}-\partial_iH\), with the derivative direction correctly indexed by \(j\);
- `ET = ric3 + 3q - Kn - HK + 2KqiK`.

Because only the coordinate \(s=y^0\) varies, setting the derivative term to `ks[:,kk,i]` only when `j == 0` is correct. No derivative of \(q^{jk}\) is missing: the expression is the covariant divergence \(q^{jk}\nabla_jK_{ki}\).

The flat-slice test \(q=e^{2r}I\) gives \(K=q\), \(K_r=2q\), \(H=3\), and \(\operatorname{tr}(W^2)=3\), so every block vanishes. The reported \(2.46\times10^{-11}\) residual therefore supports the radial differentiation and the signs in \(E_{rr},E_{ij}\). It does not separately test a spatially varying Codazzi block, but the displayed tensor derivation does.

For the actual exterior \(q=e^{2r}q_0\), where \(q_0\) is not flat,
\[
E_{rr}=0,\qquad E_{ri}=0,\qquad E_{ij}=\operatorname{Ric}(q_0)_{ij}.
\]
Hence
\[
\|E\|_{\mathrm{op},g}
=e^{-2r}\left\|q_0^{-1/2}\operatorname{Ric}(q_0)q_0^{-1/2}\right\|_{\mathrm{op}}.
\]
This explains the endpoint values \(1.0741905\) at \(R=1\) and \(0.0534808\) at \(R=2.5\); their ratio is \(e^{-3}\), exactly as the formula predicts. These are expanding asymptotic ends, not exact Einstein ends at finite \(R\).

---

## 2. Matrix-exponential center jets

Let
\[
S=q_0^{1/2},\qquad
A=S^{-1}K_0S^{-1},\qquad
\widehat R=S^{-1}\operatorname{Ric}(q_0)S^{-1}.
\]
At \(X(0)=0\),
\[
e^{X(r)}
=I+rX_r(0)+\frac{r^2}{2}\bigl(X_{rr}(0)+X_r(0)^2\bigr)+O(r^3).
\]
This formula already contains the second Fréchet derivative of the exponential. There is no commutativity assumption: for the repeated direction \(X_r\), the second-order term is \(X_r^2\).

For
\[
q=S e^X S,\qquad
X_r(0)=2\varepsilon A,\quad \varepsilon\in\{+1,-1\},
\]
one obtains
\[
q_r(0)=S(2\varepsilon A)S=2\varepsilon K_0.
\]
With
\[
X_{rr}(0)=2(\widehat R+3I),
\]
the second derivative is
\[
\begin{aligned}
q_{rr}(0)
&=S\left(2(\widehat R+3I)+4A^2\right)S\\
&=2\operatorname{Ric}(q_0)+6q_0+4K_0q_0^{-1}K_0\\
&=2\left(\operatorname{Ric}(q_0)+3q_0
+2K_0q_0^{-1}K_0\right).
\end{aligned}
\]
This is precisely \(2K_r\) from the tangential Einstein equation at a minimal slice \(H=0\). It is independent of \(\varepsilon\), since the only first-jet contribution is \(X_r^2\).

At \(r=R\), \(X=2RI\) commutes with every matrix. Therefore
\[
q_r=e^{2R}S X_rS,\qquad
q_{rr}=e^{2R}S(X_{rr}+X_r^2)S.
\]
The data \(X_r=2I,\ X_{rr}=0\) give \(q_r=2q\) and \(q_{rr}=4q\), as required for attachment to \(e^{2r}q_0\).

The correction shapes \(t^3(1-t)^3p(t)\) vanish with their first two derivatives at both endpoints. The finite-basis script therefore preserves all these jets analytically. The two halves also match through second order after converting the outward coordinate on the \(-\) half to a signed global normal coordinate.

This conclusion does **not** transfer to `step98_direct_spd_transition.py`. There the interior values of \(X\) are independent nodal variables. Endpoint values remain fixed, but endpoint derivatives of the interpolated field are unconstrained. The evaluator simply replaces the computed endpoint \(q_r,q_{rr}\) by desired values.

For an SPD continuum interpretation \(q=S e^{X^I}S\), the unreported endpoint discrepancies are
\[
\Delta q_r(0)
=S\bigl(X_r^I(0)-2\varepsilon A\bigr)S,
\]
\[
\Delta q_{rr}(0)
=S\left(X_{rr}^I(0)+X_r^I(0)^2
-2(\widehat R+3I)-4A^2\right)S,
\]
and
\[
\Delta q_r(R)
=e^{2R}S\bigl(X_r^I(R)-2I\bigr)S,
\]
\[
\Delta q_{rr}(R)
=e^{2R}S\bigl(X_{rr}^I(R)+X_r^I(R)^2-4I\bigr)S.
\]
None of these quantities appears in the JSON.

There is a second interpretation issue: the code forms \(q\) at nodes and applies the Chebyshev matrices directly to those nodal \(q\)-values. That differentiates the polynomial interpolant of \(q\), not \(S e^{X^I}S\). The former need not remain positive definite between nodes; the latter is positive definite but generally has different derivatives at this resolution. Endpoint replacement hides the distinction at the two endpoint rows.

---

## 3. Invariant tensor norms

NumPy returns \(g=LL^T\) from `cholesky(g)`. The code computes
\[
E_{\mathrm{orth}}=L^{-1}EL^{-T}.
\]
Indeed, its two solves produce exactly this matrix. If the orthonormal frame matrix is \(B=L^{-T}\), then
\[
E_{\mathrm{orth}}=B^TEB.
\]
Its eigenvalues are the generalized eigenvalues of
\[
Ev=\lambda gv.
\]
Therefore
\[
\max|\lambda(E_{\mathrm{orth}})|
\]
is the invariant operator norm relevant to the two-sided Ricci inequality.

The packed representation is also correct:
\[
\sum_i E_{ii}^2+2\sum_{i<j}E_{ij}^2
=\|E_{\mathrm{orth}}\|_{\mathrm{HS}}^2.
\]
The reported `minimum_q_eigenvalue` is only a coordinate-matrix positivity indicator at sampled nodes; it is not an invariant geometric eigenvalue and says nothing about unsampled points.

---

## 4. Meaning of the direct nodal decrease

The \(N_r=11,N_s=16,R=1\) direct calculation gives
\[
260.21\longrightarrow8.90
\]
on the \(+\) half and
\[
137.10\longrightarrow8.22
\]
on the \(-\) half for the endpoint-excluded sampled geometric vector. The joint Euclidean value decreases by a factor of about \(24.3\). Along the stored line segment, the same sampled quantity decreases monotonically. This is genuine evidence that full symmetric-matrix nodal directions compensate much of the coarse sampled residual.

More precisely, each half has \(9\cdot16\cdot10=1440\) packed interior residual entries, so the final RMS per packed entry is approximately
\[
8.8978/\sqrt{1440}=0.2345,\qquad
8.2226/\sqrt{1440}=0.2167.
\]
It is still an order-\(10^{-1}\) sampled residual, not a near-zero discrete solution.

Several supplied numbers identify strong discretization effects:

1. **The final supremum is the unresolved center momentum term.**  
   At \(N_s=16\),
   \[
   \|E_{ri}(0)\|=1.3634185384,
   \]
   exactly matching the final reported operator supremum. The resolution file shows
   \[
   1.3634,\ 0.7084,\ 0.3289,\ 0.07121,\ 0.01212,\
   3.04\times10^{-4},\ 6.76\times10^{-6}
   \]
   for \(N_s=16,24,32,48,64,96,128\). Analytically the center momentum tensor is zero. Thus the dominant final supremum is a Fourier discretization residue.

2. **The exterior value is intentionally omitted from optimization.**  
   The \(R=1\) endpoint tangential norm \(1.0741905\) is the exact non-Einstein exterior value described above. Because endpoint rows are excluded, it does not enter the geometric least-squares vector.

3. **The regularizer contributes materially.**  
   From `cost_including_regularizer`, the regularizer-vector norms are approximately \(5.82\) and \(4.36\). Since the weight is \(10^{-3}\), the unweighted radial-curvature norms are about \(184\) and \(138\). Moreover, the regularizer contains only radial second derivatives; grid-scale oscillations in \(s\) are not penalized.

4. **The nonlinear solve stopped after four evaluations.**  
   The stored `optimality` values are \(745.9\) and \(79.7\), so the returned vectors are far from stationary points of the regularized objective. They are substantial descent iterates.

5. **Nonlinear spectral aliasing is untreated.**  
   Matrix exponentials, inverses, products in \(Kq^{-1}K\), and Christoffel products create Fourier and Chebyshev content above the represented modes. At \(N_s=16\), even the fixed center data are visibly unresolved. No zero-padding or independent fine-grid evaluation is present.

6. **The discrete target changes with \(N_s\).**  
   `initial_data` computes \(\alpha_s,\beta_s\) spectrally and then constructs \(K_0\). A resolution study therefore resamples slightly different discrete Cauchy tensors unless the analytic Step-94 derivatives are frozen.

7. **The JSON does not preserve the resulting field.**  
   It stores neither `ls.x`, \(X_1\), \(q_1\), nor spectral coefficients. The reported field therefore cannot be independently prolonged and recomputed from the JSON alone.

The \(N_r=35,N_s=64,R=2.5\) finite-basis file has `gn_steps=0`; its \(970.66\) and \(99.57\) values belong only to the unadjusted quintic interpolation. It contains no Jacobian or nonlinear correction and is not directly comparable with the \(R=1,N_r=11,N_s=16\) nodal calculation.

---

## 5. Decisive cross-resolution experiment

A continuum-compatible full-matrix parameterization is
\[
X_\varepsilon(t,s)
=X_{\varepsilon,\mathrm{Hermite}}(t,s)
+t^3(1-t)^3Y_\varepsilon(t,s),
\]
with
\[
Y_\varepsilon
=\sum_{\ell=0}^{m}\sum_{|k|\le K}
C_{\ell k}^{(\varepsilon)}
T_\ell(2t-1)e^{iks},
\]
subject to the usual reality and symmetry relations. This retains direct full-matrix freedom while preserving the center and exterior jets analytically.

The decisive numerical comparison consists of:

- frozen analytic Step-94 data \(q_0,K_0\), rather than resolution-dependent spectral derivatives;
- nested modal spaces \((m,K)\);
- nonlinear residual evaluation on separate, phase-shifted grids with at least \(3\)–\(4\) times the modal density, including \(N_s=96,128\), since the center data show that this scale is needed;
- no endpoint derivative replacement;
- direct reporting of all four endpoint jet discrepancies above;
- invariant operator supremum on a densely sampled grid, all three blockwise norms, a Clenshaw–Curtis/trapezoidal \(L^2(d\mu_g)\) norm, and Fourier/Chebyshev coefficient tails;
- minimum eigenvalue on the fine grid and a record of whether the \([-40,40]\) exponential clipping was ever active;
- separate regularizer weights, including the unregularized geometric residual.

A coarse-grid reduction that survives this prolongation with stable norms and decaying spectral tails represents continuum information. A large rebound on the independent grid identifies aliasing or nodal interpolation as the source of the coarse reduction.

---

## 6. Residual projection

For a fine-grid weighted residual \(F\) and geometric Jacobian \(J\), define
\[
\widehat F=W^{1/2}F,\qquad
\widehat J=W^{1/2}J,
\]
where \(W\) contains quadrature and volume-density weights. If
\[
\widehat J=U\Sigma V^T,\qquad p_j=u_j^T\widehat F,
\]
then the resolvable projection at threshold \(\tau\) is
\[
P_\tau\widehat F
=\sum_{\sigma_j>\tau}p_j u_j,
\]
and the residual orthogonal to the retained Jacobian image is
\[
\widehat F_\perp=\widehat F-P_\tau\widehat F.
\]
The quantities
\[
\sigma_j,\qquad p_j,\qquad \frac{|p_j|}{\sigma_j}
\]
measure sensitivity, residual coupling, and the undamped correction amplitude. Each important \(u_j\) can be decomposed by \(rr\), \(ri\), and \(ij\) blocks and by radial/Fourier localization.

The ridge step currently used is algebraically correct:
\[
\Delta x
=-\sum_j\frac{\sigma_jp_j}{\sigma_j^2+\rho^2}v_j.
\]
Its predicted removable residual is
\[
-J\Delta x
=\sum_j\frac{\sigma_j^2}{\sigma_j^2+\rho^2}p_j u_j.
\]
By contrast, the script’s
```python
accessible = U @ (U.T @ F)
```
includes every returned singular vector, even one associated with a numerically zero singular value, and it does not represent the ridge-effective reduction. A singular-value threshold or the last displayed ridge factor is required.

For cross-resolution use, the most informative object is the fine-grid Jacobian with respect to prolonged coarse coefficients,
\[
J_{m\to M}=D\mathcal F_M(Px_m)\,P.
\]
Projecting the fine-grid residual onto \(\operatorname{ran}J_{m\to M}\), followed by projection onto newly added modal shells, distinguishes residual components already adjustable at coarse resolution from components visible only after refinement. No such projection is present in the supplied Step-98 JSON; the finite-basis file has an empty `spectral_analysis`, and the direct nodal file stores no Jacobian.