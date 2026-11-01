# TTCS Independent Branch Record

```json
{
  "step_id": 94,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/scripts/step94_corrected_aabb_principal_response.py",
    "Sessions/S0910A01/workspace/data/step94_corrected_aabb_principal_response.json",
    "Sessions/S0910A01/workspace/scripts/step93_aabb_tensor_sector_analysis.py",
    "Sessions/S0910A01/workspace/notes/step93_aabb_sector_divergence.md",
    "Sessions/S0910A01/trace/ttcs/results/step93_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Verify the Step 94 correction to the Step 93 AA/BB tensor-sector calculation for the product-orbifold chirality-odd Green response. Check specifically: (1) if electric TF tensor E=(Hess f)^TF has pole amplitude 2b and norm mu(mu-2)/2, then magnetic tensor M=L_{(*df)^#}g has pole amplitude 4b and norm four times the electric norm; equivalently using (1/2)M restores amplitude 2b and the electric norm. (2) With this corrected normalization, separated-pole tensor electric and magnetic contributions cancel exactly under the Step-93 transported pole signs, so the claimed BB_NS/AA_SN coincident divergence is not intrinsic. (3) Same-pole tensor electric and magnetic contributions reinforce equally, leaving a finite AA_NS/BB_SN principal response. (4) The heat-kernel representation K_AA_NS = -1/1024 int_0^infty e^s A0(s) B2(s) ds with B2=32*pi d_x^2 p_{s/2}^{S2}(-1) is consistent with the script and gives a negative finite value in the stated Step89/91 principal normalization. Identify any remaining source/gauge/Ozuch normalizations not settled by this correction.

## Output

# Step 94 scientific verification memo

## Main result

For the spectral object implemented in `step94_corrected_aabb_principal_response.py`, the normalization repair is mathematically correct:

1. \(M=L_{(*df)^\#}g\) has twice the electric pole amplitude and four times its squared \(L^2\) norm.
2. After division by the correct norm, electric and magnetic tensors cancel exactly when the tensor factor is evaluated at opposite poles.
3. They contribute equally when the tensor factor is evaluated at the same pole.
4. The resulting \(AA_{NS}\) and \(BB_{SN}\) response has the stated heat-kernel representation, is finite, and is strictly below zero in the Step 89/91 convention.

Thus the \(t^{-3}\) term reported in Step 93 came from combining the full-Lie magnetic pole amplitude with the electric tensor norm.

## 1. Electric and magnetic normalization

Let \(f\) be an \(L^2\)-normalized scalar harmonic on the unit sphere with
\[
-\Delta f=\mu f,\qquad \mu=\ell(\ell+1).
\]
For
\[
E=(\nabla^2f)^{\mathrm{TF}},
\]
the Bochner identity gives
\[
\int_{S^2}|\nabla^2f|^2
 =\mu^2-\mu.
\]
Removing the trace in dimension two gives
\[
\|E\|_{L^2}^2
 =\mu^2-\mu-\frac{\mu^2}{2}
 =\frac12\mu(\mu-2).
\]

Write \(J\) for rotation by \(\pi/2\) and set \(X=J\nabla f\). Since the trace part of \(\nabla^2f\) commutes with \(J\),
\[
M=L_Xg=JE-EJ
\]
up to the harmless sign determined by the convention for \(J\). If
\[
E=\begin{pmatrix}a&b\\ b&-a\end{pmatrix},
\]
then
\[
JE-EJ=
\begin{pmatrix}
-2b&2a\\
2a&2b
\end{pmatrix},
\qquad
|JE-EJ|^2=4|E|^2.
\]
Consequently,
\[
\|M\|_{L^2}^2
 =4\|E\|_{L^2}^2
 =2\mu(\mu-2).
\]

For the real \(m=2\) pole jets used in the scripts,
\[
\nabla^2Y_{\ell,2}^{c}
 =2b_\ell\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
\nabla^2Y_{\ell,2}^{s}
 =2b_\ell\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Hence
\[
E(Y_{\ell,2}^{s})_{01}=2b_\ell,\qquad
M(Y_{\ell,2}^{c})_{01}=4b_\ell.
\]
It follows immediately that \(\frac12M\) has pole amplitude \(2b_\ell\) and squared norm \(\frac12\mu(\mu-2)\), exactly matching \(E\).

## 2. Opposite-pole cancellation and same-pole reinforcement

Let \(\varepsilon_\ell=(-1)^\ell\). With the oriented south-pole frame used in Steps 93–94, the implemented tensor values are
\[
\begin{array}{c|cc}
 &N&S\\ \hline
E_{01}&2b_\ell&-\varepsilon_\ell\,2b_\ell\\
M_{01}&4b_\ell&\varepsilon_\ell\,4b_\ell.
\end{array}
\]
These signs agree with the local north/south expansions: the sine \(m=2\) quadratic acquires an additional sign under the oriented south frame, whereas the cosine quadratic does not.

Put
\[
N_E=\frac12\mu(\mu-2),\qquad N_M=4N_E.
\]
For opposite poles,
\[
\frac{E_{01}(N)E_{01}(S)}{N_E}
 =-\varepsilon_\ell\frac{4b_\ell^2}{N_E},
\]
while
\[
\frac{M_{01}(N)M_{01}(S)}{N_M}
 =\varepsilon_\ell\frac{16b_\ell^2}{4N_E}
 =\varepsilon_\ell\frac{4b_\ell^2}{N_E}.
\]
Their sum is zero for every \(\ell\), before any spectral or heat summation.

This removes:

- the \(BB_{NS}\) contribution, where the \(B\)-tensor factor is evaluated at \(N_B,S_B\);
- the \(AA_{SN}\) contribution, where the \(A\)-tensor factor is evaluated at \(N_A,S_A\);
- likewise the displayed \(SS\) contributions, since their tensor factor is also evaluated at opposite poles.

Step 93 instead divided the magnetic numerator \(16b_\ell^2\) by \(N_E\), making its normalized magnitude four times the electric magnitude. The uncancelled remainder was therefore three electric units, precisely the structure visible in the Step 93 reorganized heat sum.

At the same pole,
\[
\frac{E_{01}(N)^2}{N_E}
 =\frac{4b_\ell^2}{N_E},
\qquad
\frac{M_{01}(N)^2}{N_M}
 =\frac{16b_\ell^2}{4N_E}
 =\frac{4b_\ell^2}{N_E}.
\]
Thus the two polarizations contribute equally and add. This leaves \(AA_{NS}\), and by factor exchange \(BB_{SN}\). Finiteness then comes from the scalar factor being evaluated at antipodal points.

## 3. Heat-kernel formula and coefficient

Let \(r\ge2\) be the tensor degree and \(q\ge2\) the scalar degree, with
\[
P_{rq}=\frac{\mu_r+\mu_q}{2}-1.
\]
Using
\[
b_\ell^2
 =\frac{(2\ell+1)\mu_\ell(\mu_\ell-2)}{128\pi},
\]
the corrected electric-plus-magnetic contribution in the script reduces exactly to
\[
K^{AA}_{NS}(\tau)
 =-\frac1{1024}
 \sum_{r,q\ge2}
 \frac{(2r+1)(-1)^q(2q+1)\mu_q(\mu_q-2)}
 {P_{rq}}\,
 e^{-\tau P_{rq}}.
\]
Since
\[
\frac{e^{-\tau P}}P=\int_\tau^\infty e^{-sP}\,ds,
\]
this becomes
\[
K^{AA}_{NS}(\tau)
 =-\frac1{1024}\int_\tau^\infty
 e^sA_0(s)B_2(s)\,ds,
\]
where
\[
A_0(s)=\sum_{r\ge2}(2r+1)e^{-s\mu_r/2},
\]
and
\[
B_2(s)=\sum_{q\ge2}
 (-1)^q(2q+1)\mu_q(\mu_q-2)e^{-s\mu_q/2}.
\]
Therefore the unregularized expression is
\[
K^{AA}_{NS}
 =-\frac1{1024}\int_0^\infty e^sA_0(s)B_2(s)\,ds.
\]

For the mass-one zonal heat kernel
\[
p_t^{S^2}(x)
 =\frac1{4\pi}\sum_{\ell\ge0}
 (2\ell+1)e^{-t\mu_\ell}P_\ell(x),
\]
one has
\[
P_\ell''(-1)
 =(-1)^\ell\frac{\mu_\ell(\mu_\ell-2)}8.
\]
The \(\ell=0,1\) terms vanish, so
\[
B_2(s)
 =32\pi\,\partial_x^2p_{s/2}^{S^2}(-1).
\]
The dimension-raising identity gives
\[
\partial_x^2p_t^{S^2}(x)
 =4\pi^2e^{-6t}p_t^{S^6}(x),
\]
hence
\[
B_2(s)
 =128\pi^3e^{-3s}p_{s/2}^{S^6}(-1)>0.
\]
Because \(A_0(s)>0\), the integral is positive before multiplication by \(-1/1024\), proving
\[
K^{AA}_{NS}<0.
\]

At large \(s\),
\[
e^sA_0(s)B_2(s)=O(e^{-5s}).
\]
At small \(s\), \(A_0(s)=O(s^{-1})\), while the antipodal \(S^6\) heat kernel is exponentially suppressed as \(e^{-c/s}\) times a power of \(s^{-1}\). Thus both ends are integrable.

The stable numerical value supported by the data is
\[
K^{AA}_{NS}\approx-0.00400249866,
\qquad
K^{BB}_{SN}=K^{AA}_{NS}.
\]
The function `heat_series_B2_alt` evaluates a strongly cancelling alternating series in double precision near \(s=0\); this explains the spread among the quadratures beginning at \(10^{-4}\). The analytic sign and finiteness do not depend on that numerical evaluation. A numerically stronger evaluator would use the dimension-raised \(S^6\) heat kernel or multiprecision summation.

## 4. Quotient-action wording

There is one artifact-level ambiguity. Step 93 uses the descent rule \(m_A+m_B\) even, appropriate for the simultaneous axial half-turn
\[
(\phi_A,\phi_B)\longmapsto(\phi_A+\pi,\phi_B+\pi),
\]
which fixes the four pole products and acts by \(-I\) on each tangent plane there. Under that action, all displayed \(m=2\) modes descend and the quotient norm is half the cover norm.

The comments in Step 94 instead say “simultaneous antipodal.” If interpreted literally as
\[
(x_A,x_B)\longmapsto(-x_A,-x_B),
\]
the action is free, descent is governed by \(\ell\)-parity rather than \(m\)-parity, and the magnetic Hodge construction acquires an additional orientation sign. The four-node orbifold geometry and Step 93 mode rule indicate that the intended map is the axial half-turn, but the generator must be stated explicitly for the quotient normalization to be independently reproducible.

## 5. Ozuch data still absent

The script computes the symmetric principal pairing
\[
\frac{\pi^2}{2}
\sum_e
\frac{R_i(e)R_j(e)}{P_e\|e\|^2}.
\]
The Ozuch interaction instead involves
\[
\sum_e
\frac{R_i(e)\,\langle S^{\mathrm{ALE}}_j,e\rangle}
 {P_e\|e\|^2},
\]
after the relevant gauge projection. Identifying these expressions still requires:

- the exact Eguchi–Hanson \(H^4\) singular tensor and its scale and chirality normalization;
- the Bianchi projection and accompanying gauge correction;
- the Green-operator sign and the origin of the prefactor \(\pi^2/2\);
- quotient isotropy and mode-descent normalization;
- ordered north/south frame transport into each local \(\mathbb R^4/\{\pm1\}\) chart;
- large-radius ALE-to-orbifold radial matching;
- the nonlinear gluing expansion that converts this principal response into the Ozuch interaction coefficient.

In particular, the physical source may weight electric and magnetic modes differently from \(R_j(e)\). Step 94 therefore rigorously repairs the principal AA/BB spectral response and removes the Step 93 divergence from that object, while the full Ozuch-normalized coefficient remains unidentified.