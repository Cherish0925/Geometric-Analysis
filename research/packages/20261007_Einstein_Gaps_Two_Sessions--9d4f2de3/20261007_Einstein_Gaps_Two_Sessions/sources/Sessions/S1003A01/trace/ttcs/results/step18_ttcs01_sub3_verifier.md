# TTCS Independent Branch Record

```json
{
  "step_id": 18,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step18_corrected_riccati_and_H4_comparison.md",
    "Sessions/S1003A01/workspace/scripts/h4_perp_cell.py",
    "Sessions/S1003A01/workspace/scripts/u2_general_cell.py",
    "Sessions/S1003A01/workspace/data/h4_cells/corrected_perp_x0.003_X64_P_d16.json",
    "Sessions/S1003A01/workspace/data/h4_cells/corrected_perp_x0.01_X64_P_d16.json",
    "Sessions/S1003A01/workspace/data/h4_cells/corrected_perp_x0.03_X64_P_d16.json",
    "Sessions/S1003A01/workspace/data/h4_cells/corrected_perp_x0.01_X8_P_d12.json"
  ]
}
```

## Task

Independently read and check the real-hyperbolic cell comparison. Verify the normalization Ric=-6, the coordinate collar F=x, G=x+2x^2, w=0, bolt smoothness conditions and energy normalizations in h4_perp_cell.py, and assess what the floating results at X up to 64 establish scientifically about the absence or presence of a finite-scale subthreshold mechanism compared with complex hyperbolic cells. Look for implementation inconsistencies, especially the repaired G base, exact-collar contact, and whether the small anisotropy is meaningful. Do not turn numerical evidence into a theorem.

## Output

## Scientific verification memo

### 1. Real-hyperbolic normalization and collar

The normalization in `h4_perp_cell.py` is correct.

For a round warped metric
\[
g=dt^2+a(t)^2(\sigma_1^2+\sigma_2^2+\sigma_3^2),
\qquad d\sigma_i=2\sigma_j\wedge\sigma_k,
\]
the profile
\[
a(t)=\frac{1}{\sqrt2}\sinh(\sqrt2 t)
\]
has sectional curvature \(-2\), hence
\[
\operatorname{Ric}=-6g,\qquad s=-24.
\]
With \(x=a^2\),
\[
x=\frac12\sinh^2(\sqrt2t),\qquad
\frac{dx}{dt}=2aa',
\]
so the radial expression \(dt^2=dx^2/(4G)\) gives
\[
G=a^2(a')^2=x(1+2x)=x+2x^2.
\]
Isotropy gives
\[
F=x,\qquad w=0.
\]
Thus the code’s exact exterior
\[
F=x,\qquad G=x+2x^2,\qquad w=0
\]
has precisely the stated normalization.

This can also be verified directly in the Ricci formula used by the script. For the isotropic profile,
\[
\frac{a''}{a}=2,\qquad
\left(\frac{a'}a\right)^2=\frac1x+2.
\]
The radial eigenvalue is \(-3a''/a=-6\), while each orbit eigenvalue is
\[
-2-2\left(\frac1x+2\right)+\frac2x=-6.
\]
Therefore `ric0=0` and `s=-24` exactly. This independently agrees with the `RSF` symbolic substitution in `u2_general_cell.py`.

The curvature-operator statement used for interpretation is also algebraically correct:
\[
W^+=0,\qquad R^+=W^++\frac{s}{12}I=-2I.
\]
Hence the real-hyperbolic self-dual curvature block has no kernel.

---

### 2. Ordinary \(O(-1)\) bolt

Let \(\delta=x-x_0\). If
\[
F=f_1\delta+O(\delta^2),\qquad
G=g_1\delta+O(\delta^2),
\]
then
\[
dt=\frac{d\delta}{2\sqrt{g_1\delta}}+O(\sqrt\delta\,d\delta),
\qquad
\delta=g_1t^2+O(t^4),
\]
and hence
\[
F=f_1g_1t^2+O(t^4).
\]
For a full Hopf circle of period \(2\pi\), ordinary disk smoothness is therefore
\[
f_1g_1=F'(x_0)G'(x_0)=1.
\]

The repaired profiles satisfy this exactly. Writing
\[
S(u)=u^3(10-15u+6u^2),\qquad
u=\frac{\log(x/x_0)}{\log(X/x_0)},
\]
one has \(S(0)=S'(0)=0\). The unexponentiated parts are
\[
F_{\rm base}=x-x_0+x_0S,
\]
\[
G_{\rm base}=x-x_0+(2x^2+x_0)S,
\]
so
\[
F_{\rm base}'(x_0)=G_{\rm base}'(x_0)=1.
\]
Consequently
\[
F'(x_0)=e^{q_F(0)},\qquad
G'(x_0)=e^{q_G(0)}.
\]
The coefficient replacement
```python
cG = cG.at[0].add(-sum(cF*T0)-sum(cG*T0))
```
indeed enforces
\[
q_F(0)+q_G(0)=0,
\]
because the zeroth Chebyshev polynomial equals one. Thus
\[
F'(x_0)G'(x_0)=1.
\]

The two noncollapsing directions also meet smoothly:
\[
a_2^2(x_0)=x_0,\qquad a_3^2(x_0)=x_0e^{w(x_0)}=x_0,
\]
since
\[
w=u^2(1-u)^3\sum c_kT_k(2u-1)=O(u^2)=O(\delta^2)=O(t^4).
\]
All radial expansions have the required even/odd form. The formulas also guarantee \(F,G>0\) for every \(x_0<x\le X\): \(S\in[0,1]\), the displayed base factors are positive, and exponentials are positive. The reported `minF` and `minG` are merely values at the nearest Gauss nodes; the actual endpoint values are zero by construction.

One implementation detail is that the raw parameter `cG[0]` is an exact redundant coordinate: it cancels from the corrected coefficient. The represented metrics are unaffected, but the declared `3*deg` parameter count contains one null direction.

---

### 3. Contact with the exact exterior

At \(u=1\),
\[
S=1,\qquad S'=S''=0.
\]
Furthermore,
\[
q_F,q_G=(1-u)^3(\cdots),\qquad
w=u^2(1-u)^3(\cdots),
\]
so each of these functions and its first two \(x\)-derivatives vanishes at \(x=X\). It follows that
\[
F(X)=X,\quad F'(X)=1,\quad F''(X)=0,
\]
and, for
\[
B=x-x_0+(2x^2+x_0)S,
\]
\[
B(X)=X+2X^2,\quad B'(X)=1+4X,\quad B''(X)=4.
\]
Therefore \(G,G',G''\) match \(x+2x^2\), and \(w,w',w''\) match zero.

Thus an exterior \(x\ge X\) can be attached with \(C^2\) contact, which is sufficient for the displayed curvature integrals without a singular junction term. The third derivatives generally do not match because \(S'''(1)\) and the third derivatives of the cutoff factors need not vanish. These profiles are therefore exact real hyperbolic outside \(X\) after a \(C^2\) attachment, rather than smooth to every order at the joining orbit. Standard smoothing in a thin annulus can approximate them in \(C^2\), with \(P\) and \(J\) converging to the reported values.

The repaired \(G\) base passes both essential algebraic tests:
\[
G'(x_0)=e^{q_G(0)}
\quad\text{and}\quad
G(X)=X+2X^2.
\]
No inconsistency remains in that part of the implementation.

---

### 4. Energy normalization

With
\[
a_1=\sqrt F,\qquad a_2=\sqrt x,\qquad
a_3=\sqrt{xe^w},
\]
and \(\int\sigma_1\sigma_2\sigma_3=2\pi^2\),
\[
d\mu
=2\pi^2a_1a_2a_3\,dt
=2\pi^2\frac{a_1a_2a_3}{2\sqrt G}\,dx.
\]
The script defines
\[
\mathrm{vol}=\frac{a_1a_2a_3}{2\sqrt G}.
\]
Therefore
\[
\frac1{8\pi^2}\int |\operatorname{Ric}_0|^2d\mu
=\int\frac{\mathrm{vol}}4|\operatorname{Ric}_0|^2\,dx,
\]
exactly matching `PD`.

Likewise,
\[
|\operatorname{Ric}+6g|^2
=|\operatorname{Ric}_0|^2+\frac14(s+24)^2,
\]
so
\[
\frac1{8\pi^2}\int \frac14(s+24)^2d\mu
=\int\frac{\mathrm{vol}}{16}(s+24)^2\,dx,
\]
exactly matching `SF`. Thus
\[
J=P+\frac1{8\pi^2}\int\frac14(s+24)^2d\mu
\]
is the normalized \(\operatorname{Ric}+6g\) energy.

The JSON files are internally consistent: in every case `J-P` equals the stored scalar contribution. All listed runs used `target="P"`, so the displayed \(J\) values belong to \(P\)-optimized metrics and are not numerical minima of \(J\).

---

### 5. Meaning of the floating-point results

For the \(X=64\) runs,
\[
\begin{array}{c|c|c|c|c}
x_0&P-1&(P-1)/x_0&J-P&\max|w|\\ \hline
0.003&0.00605638&2.01879&1.2884\times10^{-4}&4.42\times10^{-5}\\
0.01&0.02046688&2.04669&1.1854\times10^{-3}&6.51\times10^{-5}\\
0.03&0.06306957&2.10232&9.0798\times10^{-3}&3.58\times10^{-5}
\end{array}
\]
No computed representative crosses the normalized level \(P=1\). The near-linear behavior
\[
P-1\approx 2x_0
\]
is numerically compatible with a positive first-order real-hyperbolic interaction. Together with \(R^+=-2I\), this fits the proposed curvature-response explanation, but the code does not itself derive that first variation.

At \(x_0=0.01\), the reported change
\[
1.0205588060\longrightarrow1.0204668804
\]
from the \(X=8\) file to the \(X=64\) file is only
\[
9.19\times10^{-5},
\]
about \(0.45\%\) of the excess above one. This supports saturation along that optimized branch: allowing perturbations to extend much farther into the exterior did not reveal a sizable saving. The comparison simultaneously changes degree from 12 to 16 and reoptimizes, so the difference cannot be attributed purely to \(X\).

The optimization records also matter. Although SciPy reports success, the final infinity norms of the gradients are approximately \(4\times10^{-5}\) to \(6\times10^{-5}\), rather than the requested \(10^{-12}\). No Hessian enclosure, multiple-start comparison, degree convergence study, or independent quadrature reevaluation is supplied. The 1000-point Gauss rule is generous for these smooth degree-16 profiles, but direct Ricci evaluation near the bolt contains large cancelling terms, and no high-precision bolt-series comparison is recorded. These facts do not identify a numerical defect; they mean the values are floating approximations to local optima.

Accordingly, the scientific content is:

* The supplied diagonal triaxial runs show no finite-scale subthreshold representative for \(x_0=0.003,0.01,0.03\) with \(X\le64\).
* The very small change between the \(X=8\) and \(X=64\) branches gives evidence against a large far-collar saving in this parameterization.
* These computations do not establish that every diagonal metric, every \(x_0\), larger \(X\), higher polynomial degree, another optimization basin, or a non-diagonal metric has \(P\ge1\).
* Taking the Step-18 description of the complex-hyperbolic runs as the comparison datum, the real-hyperbolic calculations do not reproduce the CH finite-scale subthreshold behavior. This is a meaningful numerical contrast, not an analytic separation theorem.

---

### 6. Interpretation of the small anisotropy

Here
\[
\frac{a_3^2}{a_2^2}=e^w,\qquad
\frac{a_3}{a_2}=e^{w/2}.
\]
Thus the largest reported value, \(6.51\times10^{-5}\), means that the squared orbit radii differ pointwise by about \(6.51\times10^{-5}\), and the radii themselves by about \(3.26\times10^{-5}\), at the sampled nodes. This is genuine \(C^0\) closeness to the biaxial locus \(w=0\).

It does not by itself show that the anisotropic channel contributes negligibly to \(P\), because the curvature density contains \(w'\) and \(w''\). The JSON files contain neither derivative norms nor the value obtained by optimizing the identical \(F,G\) family with \(w\equiv0\). The older biaxial value \(1.0647909208\) at \((x_0,X)=(0.03,4)\) is supportive, but its comparison with the triaxial \(X=64\) value also changes the collar length and parameterization.

The precise supported statement is therefore that the optimized metrics are nearly biaxial in their orbit radii. Energetic irrelevance of anisotropy, and the proposed distinction between the CH kernel direction and the \(H^4\) response, would require the same-parameter \(w=0\) value or a decomposition of the energy change into the \(w\)-dependent terms.