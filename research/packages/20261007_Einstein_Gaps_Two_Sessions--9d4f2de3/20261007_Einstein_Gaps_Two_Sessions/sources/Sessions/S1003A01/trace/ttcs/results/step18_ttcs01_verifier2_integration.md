# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 18,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step18_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step18_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently read and check the real-hyperbolic cell comparison. Verify the normalization Ric=-6, the coordinate collar F=x, G=x+2x^2, w=0, bolt smoothness conditions and energy normalizations in h4_perp_cell.py, and assess what the floating results at X up to 64 establish scientifically about the absence or presence of a finite-scale subthreshold mechanism compared with complex hyperbolic cells. Look for implementation inconsistencies, especially the repaired G base, exact-collar contact, and whether the small anisotropy is meaningful. Do not turn numerical evidence into a theorem.

## Integrated Scientific Memo

# Verification memo: real-hyperbolic cell comparison

## 1. Hyperbolic normalization and collar are correct

With
\[
g=dt^2+a(t)^2(\sigma_1^2+\sigma_2^2+\sigma_3^2),
\qquad d\sigma_i=2\sigma_j\wedge\sigma_k,
\]
the profile
\[
a(t)=\frac1{\sqrt2}\sinh(\sqrt2t)
\]
has sectional curvature \(-2\), hence
\[
\operatorname{Ric}=-6g,\qquad s=-24.
\]
Setting \(x=a^2\),
\[
a'^2=\cosh^2(\sqrt2t)=1+2a^2=1+2x.
\]
Since \(dt^2=dx^2/(4G)\) and \(dx/dt=2aa'\),
\[
G=a^2a'^2=x(1+2x)=x+2x^2.
\]
Roundness gives
\[
F=x,\qquad w=0.
\]

This also checks directly against the Ricci formulas in `h4_perp_cell.py`: \(a''/a=2\) and \((a'/a)^2=x^{-1}+2\), so every Ricci eigenvalue is \(-6\). Thus `ric0=0` and \(s=-24\), agreeing with the independent `RSF` symbolic check in `u2_general_cell.py`.

The associated self-dual curvature block is
\[
R^+=W^++\frac{s}{12}I=-2I,
\]
so unlike the stated complex-hyperbolic perpendicular situation, there is no kernel direction in \(R^+\).

## 2. The repaired bolt profile satisfies the required smoothness conditions

Let \(\delta=x-x_0\). If
\[
F=f_1\delta+O(\delta^2),\qquad G=g_1\delta+O(\delta^2),
\]
then geodesic distance satisfies \(\delta=g_1t^2+O(t^4)\), and
\[
a_1^2=F=f_1g_1t^2+O(t^4).
\]
For the ordinary \(O(-1)\) bolt, whose collapsing Hopf circle has period \(2\pi\), smoothness therefore requires
\[
F'(x_0)G'(x_0)=1.
\]

In the code,
\[
S(u)=u^3(10-15u+6u^2),\qquad
u=\frac{\log(x/x_0)}{\log(X/x_0)},
\]
has \(S(0)=S'(0)=0\). The unexponentiated bases are
\[
F_{\rm base}=x-x_0+x_0S,
\]
\[
G_{\rm base}=x-x_0+(2x^2+x_0)S.
\]
Both vanish at \(x_0\) and both have derivative \(1\) there. This confirms that the repaired \(G\)-base is correct; the earlier defective base is not present in the supplied corrected outputs.

Consequently,
\[
F'(x_0)=e^{q_F(0)},\qquad G'(x_0)=e^{q_G(0)}.
\]
Because \(T_0=\operatorname{cheb}(d,-1)\) and its constant component is one, the update
```python
cG = cG.at[0].add(-sum(cF*T0)-sum(cG*T0))
```
enforces
\[
q_F(0)+q_G(0)=0,
\]
hence \(F'(x_0)G'(x_0)=1\) exactly.

The noncollapsing directions also agree at the bolt:
\[
a_2^2(x_0)=x_0,\qquad a_3^2(x_0)=x_0e^{w(x_0)}=x_0,
\]
because \(w=O(u^2)=O((x-x_0)^2)=O(t^4)\). This is the correct order for smooth anisotropy at this bolt. The displayed bases are positive for \(x>x_0\), and the exponential factors preserve positivity. The JSON fields `minF` and `minG` are merely values at the first interior Gauss node; \(F=G=0\) at the actual bolt by construction.

One harmless implementation defect is that the original `cG[0]` is a null parameter: the update cancels its contribution. Thus `3*deg` overcounts the effective dimension by one. This does not change the represented metrics, but it introduces an exactly flat optimization direction.

## 3. Exterior contact is exact through the order used by the energy

At \(u=1\),
\[
S=1,\qquad S'=S''=0.
\]
Moreover, \(q_F,q_G,w\) contain \((1-u)^3\), so each and its first two \(x\)-derivatives vanish at \(X\). Therefore
\[
F(X)=X,\quad F'(X)=1,\quad F''(X)=0,
\]
and
\[
G(X)=X+2X^2,\quad G'(X)=1+4X,\quad G''(X)=4,
\]
while
\[
w(X)=w'(X)=w''(X)=0.
\]

Thus the cell has \(C^2\) contact with the exact hyperbolic exterior. This is sufficient for the curvature-energy formulas and creates no distributional junction contribution. It is not generally \(C^\infty\) contact: third derivatives need not match. Consequently, the literal piecewise metric is \(C^2\), while smooth metrics with arbitrarily nearby energies require smoothing in a thin annulus.

This is stronger contact than the older `u2_general_cell.py` profile, which was designed only for \(C^1\) matching.

## 4. Energy normalizations are correct

For
\[
a_1=\sqrt F,\quad a_2=\sqrt x,\quad a_3=\sqrt{xe^w},
\qquad \int\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2,
\]
one has
\[
d\mu
=2\pi^2a_1a_2a_3\,dt
=2\pi^2\frac{a_1a_2a_3}{2\sqrt G}\,dx.
\]
The code’s
\[
\mathrm{vol}=\frac{a_1a_2a_3}{2\sqrt G}
\]
therefore gives
\[
\frac1{8\pi^2}\int |\operatorname{Ric}_0|^2\,d\mu
=\int\frac{\mathrm{vol}}4|\operatorname{Ric}_0|^2\,dx,
\]
which is exactly `PD`.

Since in dimension four
\[
|\operatorname{Ric}+6g|^2
=|\operatorname{Ric}_0|^2+\frac14(s+24)^2,
\]
the expression
\[
\int\frac{\mathrm{vol}}{16}(s+24)^2\,dx
\]
is exactly the scalar contribution to the normalized \(\operatorname{Ric}+6g\) energy. Hence
\[
J=P+\frac1{8\pi^2}\int\frac14(s+24)^2\,d\mu.
\]
All JSON files satisfy `J-P = scalar` to the displayed precision.

Every supplied run has `target="P"`. The listed \(J\)-values are therefore evaluations on \(P\)-optimized metrics, not computed minima of \(J\).

## 5. What the floating calculations actually show

For \(X=64\),
\[
\begin{array}{c|c|c|c|c}
x_0&P-1&(P-1)/x_0&J-P&\max|w|\\ \hline
0.003&0.00605638&2.01879&1.2884\times10^{-4}&4.42\times10^{-5}\\
0.01&0.02046688&2.04669&1.1854\times10^{-3}&6.51\times10^{-5}\\
0.03&0.06306957&2.10232&9.0798\times10^{-3}&3.58\times10^{-5}.
\end{array}
\]
Thus the best representatives found in this finite-dimensional diagonal family all satisfy \(P>1\), with behavior numerically compatible with
\[
P=1+2x_0+o(x_0).
\]
This is consistent with, but does not derive, a positive first-order response associated with \(R^+=-2I\).

At \(x_0=0.01\), the optimized values are
\[
P(X=8)=1.0205588060,\qquad
P(X=64)=1.0204668804.
\]
Their difference is only \(9.19\times10^{-5}\), about \(0.45\%\) of the excess \(P-1\). This indicates that in these two discretizations, extending the deformation much farther into the exterior did not uncover a substantial energy saving.

That comparison is not a clean one-variable continuation test: degree changes from \(12\) to \(16\), quadrature from \(800\) to \(1000\), and the Chebyshev variable depends on \(\log(X/x_0)\). The files also do not record whether a seed was used. Hence the change cannot be attributed solely to \(X\), and the note’s word “continuation” should be read only informally.

More importantly, optimizer output supplies upper bounds on the restricted infimum, not lower bounds. These calculations establish only that:

* no supplied optimized representative is subthreshold;
* no sizable far-collar saving appeared in the tested parameterizations;
* the tested \(H^4\) cells do not reproduce the explicitly constructed finite-scale CH subthreshold behavior.

They do **not** establish \(P\ge1\) for all diagonal metrics, all \(x_0\), all \(X\), higher degrees, other optimization basins, or non-diagonal metrics. In particular, the sampled values \(x_0\le0.03\) do not directly explore a genuinely moderate-\(x_0\) finite-scale regime.

The numerical convergence evidence is also limited. Although SciPy reports success, the recorded gradient infinity norms are \(4\!-\!6\times10^{-5}\), not near the requested \(10^{-12}\); termination likely came from function tolerance. There is no degree-refinement, quadrature-refinement, multiple-start, high-precision bolt evaluation, or Hessian enclosure. These are reasons to treat the values as approximate local optima, not evidence of a detected error.

## 6. The small anisotropy is geometrically real but not yet energetically diagnostic

Since
\[
\frac{a_3^2}{a_2^2}=e^w,
\]
the reported \(\max|w|\lesssim6.6\times10^{-5}\) means that the squared orbit radii differ by only about \(10^{-5}\), and the radii themselves by roughly half that relative amount. Thus the computed metrics are genuinely very close in \(C^0\) to the biaxial locus.

There are, however, two reasons not to overinterpret this:

1. Curvature depends on \(w'\) and \(w''\), whose norms are not recorded. Small \(\|w\|_\infty\) alone does not prove that anisotropy contributes negligibly to \(P\).
2. The real-hyperbolic collar and bolt data are invariant under interchange of the two noncollapsing directions, so \(w=0\) is a symmetry-fixed family. Starting every run with \(c_W=0\) can naturally converge near that family and does not strongly test symmetry-breaking minima.

Moreover, CH perpendicular cells have anisotropy forced by the mismatch between their collar directions and the round bolt, whereas the \(H^4\) collar is isotropic. Consequently, “small \(w\) for \(H^4\) versus substantial \(w\) for CH” is partly built into the boundary geometry; it is not by itself evidence that the anisotropic variational channel is dynamically absent in \(H^4\).

The older biaxial result \(P=1.0647909\) at \((x_0,X)=(0.03,4)\) is compatible with the triaxial \(X=64\) value \(1.0630696\), but it changes both collar length and parameterization and is not an independent same-parameter test of anisotropy. A decisive numerical check would compare, at identical \((x_0,X,\deg,n_q)\), unrestricted \(w\), constrained \(w=0\), random anisotropic starts, and the odd-sector Hessian at the biaxial optimum.

## 7. Scientific comparison with complex hyperbolic cells

The supported contrast is asymmetric:

* A rigorously evaluated CH construction with \(P<1\) would positively exhibit a subthreshold mechanism.
* The present \(H^4\) optimizations merely failed to find one in a restricted finite-dimensional class.

Nevertheless, the contrast is scientifically meaningful. The \(H^4\) data show a stable positive excess approximately proportional to \(x_0\), little apparent gain from extending \(X\) from \(8\) to \(64\), and near-biaxial optimizers. This is consistent with the curvature-response picture
\[
R^+_{H^4}=-2I,
\]
which charges every self-dual gluing direction at first order, whereas a kernel direction in the CH curvature block can suppress the first-order cost and permit a second-order signed interaction.

That mechanism remains a hypothesis, not a conclusion of the code. Its sharp verification would require an analytic first-variation expansion around the Burns cell and a matched numerical comparison between \(H^4\) and CH using the same discretization and bolt-area normalization. The present evidence supports the absence of a **detected** finite-scale subthreshold mechanism in the tested real-hyperbolic family; it does not prove its mathematical absence.