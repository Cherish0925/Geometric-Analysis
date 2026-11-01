# TTCS Independent Branch Record

```json
{
  "step_id": 75,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md",
    "Sessions/S0910A03/workspace/scripts/step69_collapsed_koiso_center.py",
    "Sessions/S0910A03/workspace/scripts/step75_core_entry_gauss_newton.py",
    "Sessions/S0910A03/workspace/data/step75_core_entry_gauss_newton_pilot.json",
    "Sessions/S0910A03/workspace/scripts/step75_germ_to_entry_search.py",
    "Sessions/S0910A03/workspace/data/step75_germ_to_entry_pilot.json",
    "Sessions/S0910A03/workspace/scripts/step75_center_shape_search.py",
    "Sessions/S0910A03/workspace/data/step75_center_shape_search_pilot.json",
    "Sessions/S0910A03/workspace/data/step70_ricci_T2inv.json"
  ]
}
```

## Task

Independently read the Step-75 full-residual computation as a mathematical numerical experiment. Check whether the Gaussian Ricci component formulas and orthonormal normalization in the active scripts match g=dr^2+e^{2a}dz^2+e^{2b}dx^2+e^{2c}dy^2; whether the validated Step-69 Yamabe sign and center data are used consistently; whether boundary bases really impose the center and exit jets described; whether all five independent Ricci components enter; and whether the reported locations and sizes support only the stated finite-spectral interpretation. Identify any concrete formula, normalization, basis, or inference error that would change the scientific reading. Also assess whether the center-shape computation supports approach to the exact lower value 3 within its sampled reciprocal-warp family, without treating it as proof of a global infimum.

## Output

# Scientific verification memo

## 1. Gaussian Ricci formulas and frame normalization

For
\[
g=dr^2+e^{2a}dz^2+e^{2b}dx^2+e^{2c}dy^2,
\qquad E=\operatorname{Ric}_g+3g,
\]
in the orthonormal frame
\[
e_{\hat r}=\partial_r,\quad e_{\hat z}=e^{-a}\partial_z,\quad
e_{\hat x}=e^{-b}\partial_x,\quad e_{\hat y}=e^{-c}\partial_y,
\]
the five potentially nonzero independent components are
\[
\begin{aligned}
E_{\hat r\hat r}
 &=3-a_r^2-a_{rr}-b_r^2-b_{rr}-c_r^2-c_{rr},\\
E_{\hat r\hat z}
 &=e^{-a}\!\left[a_r(b_z+c_z)-b_rb_z-c_rc_z-b_{rz}-c_{rz}\right],\\
E_{\hat z\hat z}
 &=3-a_r^2-a_rb_r-a_rc_r-a_{rr}\\
 &\quad+e^{-2a}(a_zb_z+a_zc_z-b_z^2-b_{zz}-c_z^2-c_{zz}),\\
E_{\hat x\hat x}
 &=3-a_rb_r-b_r^2-b_rc_r-b_{rr}\\
 &\quad+e^{-2a}(a_zb_z-b_z^2-b_zc_z-b_{zz}),\\
E_{\hat y\hat y}
 &=3-a_rc_r-b_rc_r-c_r^2-c_{rr}\\
 &\quad+e^{-2a}(a_zc_z-b_zc_z-c_z^2-c_{zz}).
\end{aligned}
\]
These agree term by term with `step70_ricci_T2inv.json`, `step75_core_entry_gauss_newton.py`, and `step75_germ_to_entry_search.py`.

In particular:

- Multiplication of the coordinate \(rz\) component by \(e^{-a}\) is correct.
- The \(zz,xx,yy\) entries are orthonormal components, including the required \(e^{-2a}\) factors.
- No additional components occur for a diagonal metric depending only on \(r,z\).
- The sampled operator norm is computed correctly from the \(2\times2\) \((\hat r,\hat z)\) block and the two orbit eigenvalues.
- The residual vector uses \(\sqrt2\,E_{\hat r\hat z}\), so its squared Euclidean norm contains
  \[
  E_{\hat r\hat r}^2+2E_{\hat r\hat z}^2+E_{\hat z\hat z}^2
  +E_{\hat x\hat x}^2+E_{\hat y\hat y}^2,
  \]
  the orthonormal Frobenius expression.

Thus there is no visible Ricci-sign or orthonormalization error in the two active scripts.

## 2. Step-69 Yamabe sign and the projected center jet

For
\[
h_f=dz^2+e^{2f}dx^2+e^{-2f}dy^2,\qquad q=u^4h_f,
\]
one has \(R_{h_f}=-2(f')^2\) and \(\Delta_{h_f}u=u''\). Therefore \(R_q=-6\) is equivalent to
\[
-8u''-2(f')^2u=-6u^5,
\qquad
u''=\frac34u^5-\frac14(f')^2u.
\]
Both `step69_collapsed_koiso_center.py` and `step75_center_shape_search.py` use this correct sign.

In the core-entry script,
\[
L_i=l_{0,i}+\log\cosh r+\rho(r)g_i+\sum_j B_j(r)c_{ij}(z),
\]
where
\[
\rho(0)=\rho'(0)=0,\qquad \rho''(0)=1,
\]
and every free radial mode is \(O(r^4)\). Hence
\[
L(0)=l_0,\qquad L_r(0)=0,\qquad L_{rr}(0)=1+g.
\]
Since the code sets \(g\) to the Fourier projection of \(\operatorname{Ric}_{q_0}^{\sharp}+2I\), the extra \(1\) from \((\log\cosh r)''|_{0}\) gives
\[
L_{rr}(0)=\mathcal P_{K_z}\bigl(\operatorname{Ric}_{q_0}^{\sharp}+3I\bigr).
\]
The apparently unusual `center_ric + 2` is therefore correct.

There is, however, an important exactness distinction. `C0` and `Gcoef` are \(K_z=5\) least-squares Fourier projections. Thus the script fixes the projected center and projected Koiso acceleration, not the continuum Step-69 functions exactly. The JSON records
\[
\|R_{\mathcal Pq_0}+6\|_{\infty,\mathrm{grid}}
 =1.1863\times10^{-3},
\]
and center component errors as large as \(2.9583\times10^{-3}\). The reported `second_jet_error_sup` near \(10^{-15}\) compares the constructed second derivative to the same projected array used to construct it; it verifies basis algebra rather than agreement with the continuum center.

The supplied artifacts omit `step75_full_residual_core_search.py`, which defines `base.yamabe_center`, `base.intrinsic_ric_np`, and the Fourier basis. The visible standalone Step-69 implementation has the correct sign, and the resulting center numbers are consistent with it, but a direct line-level verification of that imported implementation is unavailable here.

## 3. Endpoint and interface bases

### Core-entry script

The local modes \(x^4e^{-x^2}\) and global modes
\[
s^4T_j(2s^2-1)
\]
are even and vanish through second order at \(r=0\). They therefore preserve reflection, center value, and center second jet exactly within the projected ansatz.

No exact condition is imposed at \(r=R\). The second continuation merely adds penalties for \(L_r(R)\approx(1,1,1)\) and small intrinsic Ricci curvature. In particular, \(d_r(R)=b_r(R)-c_r(R)\) remains free.

The global endpoint pairs span value and first derivative: at \(s=1\),
\[
p_j(1)=1,\qquad \partial_rp_j(1)=\frac{4+4j^2}{R},
\]
up to each mode’s normalization. Distinct \(j\) therefore give rank two. The core-entry ansatz can vary endpoint metric and shape independently for every retained Fourier mode.

### Germ-to-entry script

Here the correction modes are \(O(x^2)\), where \(x=r-T_\ast\). Consequently,
\[
L(T_\ast)=L_{\mathrm{inner}},\qquad
L_r(T_\ast)=S_{\mathrm{inner}},
\]
but \(L_{rr}(T_\ast)\) is free. The outer metric is therefore only \(C^1\)-matched to the numerical germ as parameterized. It cannot be glued smoothly to the stored inner germ without additionally matching its second and higher derivatives.

This explains a major feature of the JSON. Although the germ constraints are reported as \(0.00324\) and \(0.00564\), the outer linear extension already has inner-face components as large as \(8.48\), and the optimized runs have inner-face components around \(16\)–\(23\). Those values arise because the outer second derivative is unrelated to the germ acceleration.

There is also an outer-endpoint rank issue in this script. For
\[
v_j(s)=s^2\cos(j\pi s),
\]
one has
\[
v_j'(1)=\frac{2}{X}v_j(1),\qquad X=R-T_\ast,
\]
for every \(j\). The local Gaussian modes become exponentially tiny at the outer face when \(X\) is large and coefficients are bounded. Thus, especially at \(R=6\), the global basis ties endpoint correction value and derivative by essentially one relation. Endpoint metric and shape are not independently variable there. This can materially influence the reported exit data.

## 4. What the full-residual numbers establish

All five components enter both optimization objectives. The numerical interpretation nevertheless remains tied to the chosen finite ansatz and sampling:

- Core-entry: \(K_z=5\), \(N_z=32\), about \(31\) radial points.
- Germ-to-entry: \(K_z=5\), \(N_z=32\), about \(29\) radial points.
- No dense off-grid reevaluation is included in the JSON.
- The solvers stop at their evaluation caps. In the core run, final optimalities remain between roughly \(0.87\) and \(12.46\).
- The objective is an averaged Frobenius \(L^2\) quantity, not the operator supremum. Indeed, at \(R=2\) the unoptimized carrier has operator supremum \(12.78\), while the optimized residual-only result has \(16.03\) despite a smaller averaged objective.
- Radial weights are divided by \(R\) or \(X\), so a fixed inner interval receives progressively less objective weight as the total length grows.

The core-entry sampled suprema
\[
16.0268,\quad16.0348,\quad15.9641
\]
occur at \(r=0.1957,0.1875,0.1875\), respectively. The soft-entry values are similarly near \(16\). This supports the textual statement that these runs did not produce a small full defect and that the largest sampled contribution stayed near the center transition. It does not distinguish among insufficient radial modes, coarse inner sampling, averaged weighting, or incomplete nonlinear optimization.

For the germ runs, the residual-only sampled suprema are
\[
23.5201,\quad22.1245,\quad21.5961,
\]
with maxima at \(r=0.15,0.15,0.225\). Because the ansatz frees \(L_{rr}(T_\ast)\) and gives the endpoint half quadrature weight, these maxima do not specifically measure continuation of the stored smooth germ.

Two reported consistency quantities require careful reading:

1. `normal_identity_pointwise_sup` is algebraic. Substituting the code definition of \(E_{\hat r\hat r}\) makes it identically zero.
2. The integrated normal balance is mathematically correct, but its recorded errors become \(10^4\) at \(R=6\). The factor \(e^{2r}\) amplifies radial quadrature error and cancellation. Thus the coarse grid does not numerically resolve this weighted identity, even though the identity itself follows exactly from the component formula.

## 5. Center-shape computation

The Ricci formulas used for \(q=u^4h_f\) are correct. With
\[
\varphi=2\log u,
\]
the three Ricci eigenvalues are exactly the expressions implemented in the script. Since \(R_q=-6\), in dimension three
\[
K_{\text{plane complementary to }e_i}
=-\bigl(\operatorname{Ric}^{\sharp}_q+3I\bigr)_i.
\]
Therefore the script’s
```python
posK = maximum(-P, 0)
```
correctly measures sampled positive sectional curvature.

The analytic center theorem supplies the lower value \(3\) for every scalar-minus-six \(T^2\)-cohomogeneity-one center. The sampled reciprocal-warp sequence is strongly consistent with approach toward it:
\[
\begin{array}{c|cccccc}
A&0.5&1&2&3&5&8\\ \hline
\max K_+&10.8271&5.32335&4.33353&3.74435&3.28337&3.12623 .
\end{array}
\]
The three-mode result gives \(3.03297037\), still above the analytic value \(3\). This is meaningful numerical evidence inside the sampled family.

Three numerical details prevent interpreting it as an asymptotic theorem:

- The optimized \(p=16\) averaged surrogate is \(2.66586\), below \(3\); it is not the supremum. The scientifically relevant reported number is the direct dense-grid maximum \(3.03297\).
- `upp` is evaluated from the ODE right-hand side and then reused in both the Yamabe and scalar-curvature residuals. Hence the \(10^{-15}\) residuals are algebraic consequences of that substitution, not independent measures of the `solve_bvp` interpolation error.
- No mesh-refinement sequence or independent second-derivative evaluation is recorded. The high-amplitude result does use 15,143 adaptive nodes and 8,001 evaluation points, which gives useful numerical support, but not a proof of convergence to \(3\).

The \(A=10\) and \(A=15\) numbers quoted in the note are absent from the supplied pilot JSON and from its listed baseline loop, so those two values are not independently reproducible from the provided outputs.

## Overall scientific reading

The Gaussian Ricci tensor, orthonormal factors, five-component residual, Step-69 Yamabe sign, and core center-jet algebra are correct. The central numerical qualifications are more specific:

1. The core uses a Fourier-projected Step-69 center, with visible \(10^{-3}\)-scale center error.
2. The germ experiment fixes only metric and shape at its inner face; its second jet is unrelated to the stored germ.
3. The germ outer basis substantially couples endpoint values and derivatives for long intervals.
4. Reported suprema are coarse-grid observations from an averaged optimization that had not converged to stationarity.
5. The center-shape data convincingly show sampled values nearing the analytic lower value \(3\), while the tiny scalar residual fields are self-referential rather than independent numerical residuals.

These points preserve the Step-75 finite-spectral interpretation but materially sharpen what each computation does and does not establish.