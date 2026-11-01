# TTCS Independent Branch Record

```json
{
  "step_id": 12,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step12_taub_nut_accessibility_and_diffuse_pontryagin.md",
    "Sessions/S0910A01/workspace/scripts/step12_taub_nut_ads_coordinate_curvature.py",
    "Sessions/S0910A01/workspace/scripts/step12_taub_nut_ads_multiscale_calibration.py",
    "Sessions/S0910A01/workspace/data/step12_taub_nut_ads_multiscale_summary.json",
    "Sessions/S0910A03/workspace/notes/step10_multiscale_cover_and_diffuse_pontryagin.tex",
    "Sessions/S0910A02/workspace/notes/step11_cz_spike_and_proposition_A.md"
  ]
}
```

## Task

Check the Step 12 corrected Taub--NUT--AdS and chart-accessibility analysis for mathematical correctness and research consequences. Read the Step 12 note, the coordinate and multiscale scripts/summary, and the A03 source note. Focus on: (1) whether the coordinate computation and exact formulas consistently verify Ric=-g, W+=0 in the stated orientation, the one-quarter norm conversion, and the multiscale mean-energy conclusions; (2) whether the conclusion that Taub--NUT does not refute adjustable-buffer accessibility is sound; (3) whether the diffuse Pontryagin statement fint |P-3/4| -> 0 follows from the near-critical estimates as written; (4) whether the repaired controlled-chart forbidden-germ theorem is correctly stated without overusing Cheeger--Naber or Myers; and (5) what the next mathematical computation/theorem should target. Do not invent outside literature; reason from the supplied files and standard tensor calculus if needed.

## Output

# Scientific verification memo

## 1. Coordinate curvature and multiscale formulas

The tensor calculation is internally consistent with the stated conventions.

For
\[
g_\nu=F_\nu^{-1}dr^2+(r^2-\nu^2)d\Omega_2^2
+4\nu^2F_\nu(d\psi+\cos\theta\,d\phi)^2,
\]
the coordinate script verifies, at several \((\nu,r)\) values,
\[
\Ric_{\mathrm{ON}}=-I,\qquad s=-4,\qquad
\operatorname{tr}\mathcal R=\frac{s}{2},
\]
with errors near machine precision. The last identity is an important sign-convention test for the curvature operator. Cohomogeneity one justifies evaluation at \(\theta=\pi/2\).

The exact identities quoted from the independent symbolic script are mutually consistent:
\[
W^+=0,
\]
\[
\operatorname{Spec}(W^-)= (a,a,-2a),\qquad
a=\frac{2\nu(4\nu^2-3)}{3(r+\nu)^3},
\]
and hence
\[
\|W^-\|_{\mathrm{HS}}^2=6a^2
=\frac{8\nu^2(4\nu^2-3)^2}{3(r+\nu)^6}.
\]
With the curvature-operator convention used here,
\[
W_{abcd}W^{abcd}=4\|W^-\|_{\mathrm{HS}}^2
=\frac{32\nu^2(4\nu^2-3)^2}{3(r+\nu)^6}.
\]

There is one terminology error in the Step 12 prose: the number
\[
0.136356035421
\]
at \((\nu,r)=(0.01,0.5)\) is the **squared** Hilbert–Schmidt norm, not the Hilbert–Schmidt norm. The latter is approximately \(0.3693\). The scripts and summary consistently label this quantity as `u2` or `W_block_hs_sq`, so none of the subsequent formulas are affected. The precise conversion is between squared norms:
\[
|W|_{(0,4)}^2=4|W^\pm|_{\mathrm{HS}}^2.
\]

The volume calculation also checks directly. With the smooth NUT period \(\psi\sim\psi+4\pi\),
\[
\sqrt{\det g}=2\nu(r^2-\nu^2)\sin\theta,
\qquad
\frac{dV}{dr}=32\pi^2\nu(r^2-\nu^2).
\]
Multiplication by the full four-index Weyl density and radial integration gives
\[
E_\nu^W(R)=
\frac{32\pi^2(4\nu^2-3)^2}{9}
\frac{(R-\nu)^2(R^2+6R\nu+17\nu^2)}{(R+\nu)^4}.
\]
Therefore, for fixed \(R>0\),
\[
E_\nu^W(R)\longrightarrow32\pi^2,
\qquad
\Vol\{\nu\le r\le R\}
\sim\frac{32\pi^2}{3}\nu R^3,
\]
and consequently
\[
\fint_{\nu\le r\le R}|W|_{(0,4)}^2
\sim\frac{3}{\nu R^3}.
\]
This establishes the stated \(\nu^{-1}\) divergence. When this energy is compared with Chern–Weil formulas, the operator norm must be used: the corresponding nonzero-half operator energy tends to \(8\pi^2\), not \(32\pi^2\).

The calibrated-magnitude shell is also correct. Solving
\[
|W^-|_{\mathrm{HS}}^2=\frac1{24}
\]
gives
\[
(r_\nu+\nu)^6=64\nu^2(4\nu^2-3)^2,
\]
so
\[
r_\nu\sim576^{1/6}\nu^{1/3}
=2\,3^{1/3}\nu^{1/3}.
\]
Its enclosed volume is \(\Theta(\nu^2)\), while its enclosed full Weyl energy tends to \(32\pi^2\), producing mean energy of order \(\nu^{-2}\).

For small \(\nu\), \(a<0\). At this shell the reversed-orientation eigenvalues are
\[
\left(-\frac1{12},-\frac1{12},\frac16\right),
\]
rather than
\[
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
Substitution into the supplied algebraic remainder indeed gives
\[
G=\frac{35}{36},
\]
while the scalar–Weyl square vanishes. The summary value \(0.972222\ldots\) is exactly \(35/36\).

One evidentiary distinction should remain explicit: the A01 coordinate script is a numerical tensor computation, whereas the exact rational formulas come from the independent symbolic script quoted in the A03 note. Together they provide strong independent support, but the A01 script alone does not symbolically derive the displayed exact expressions.

## 2. Adjustable-buffer accessibility

The corrected accessibility conclusion is mathematically sound.

At a point \(p_\nu\) a fixed physical distance from the NUT, choose a fixed scale \(\rho\) such that
\[
\nu\ll \rho,\qquad A\rho<d(p_\nu,\mathrm{NUT}),
\]
and such that the projected base region is a contractible three-dimensional patch. The buffered domain then avoids the NUT, retains the short Hopf circle in its fundamental group, and its normal or universal cover unrolls that circle. Enlarging the domain until it contains the NUT changes the fundamental-group image because the circle then contracts through the core.

The unwrapped limit follows directly from \(z=2\nu\psi\):
\[
g_\nu\longrightarrow
\frac{dr^2}{1+r^2/3}+r^2d\Omega_2^2+(1+r^2/3)dz^2.
\]
Writing \(r=\sqrt3\sinh(t/\sqrt3)\) identifies this as
\[
dt^2+3\sinh^2(t/\sqrt3)d\Omega_2^2
+\cosh^2(t/\sqrt3)dz^2,
\]
the cylindrical form of real hyperbolic four-space with sectional curvature \(-1/3\).

Thus the annular covers are accessible and smoothly modeled at fixed scale. They are excluded from the calibrated bulk for a different reason:
\[
W^+=0,\qquad s=-4,\qquad
(s+8\sqrt6|W^+|)^2=16.
\]
Near the NUT the centered curvature mean becomes large; away from it the calibrated defect remains macroscopically positive. Taub–NUT–AdS therefore does not refute accessibility in which the buffered domain is selected before taking its cover.

## 3. Diffuse Chern–Weil density

The normalized mean statement follows from the written near-critical estimates.

Set \(u_i=|W_i^+|\) and \(u_0=1/(2\sqrt6)\). Since
\[
s_i\to-4\quad\text{uniformly}
\]
and
\[
\fint\bigl(s_i+8\sqrt6\,u_i\bigr)^2\to0,
\]
one has
\[
\|u_i-u_0\|_{L^2_{\mathrm{av}}}
\le \frac1{8\sqrt6}
\left(
\|s_i+8\sqrt6u_i\|_{L^2_{\mathrm{av}}}
+\|s_i+4\|_{L^2_{\mathrm{av}}}
\right)\to0.
\]
Cauchy–Schwarz then gives
\[
\fint|u_i^2-u_0^2|\to0.
\]
Together with \(E_i\to0\) uniformly and \(s_i^2\to16\) uniformly,
\[
\fint\left|
2|W_i^+|^2+\frac{s_i^2}{24}
-\frac12|E_i|^2-\frac34
\right|\to0.
\]
Hence
\[
\fint\left|\rho_{+,i}-\frac{3}{16\pi^2}\right|\to0,
\qquad
\rho_{+,i}=\frac{P_i}{4\pi^2}.
\]

For every measurable \(U_i\),
\[
\left|
\int_{U_i}\rho_{+,i}
-\frac{3}{16\pi^2}\Vol(U_i)
\right|
\le
\int_{M_i}\left|
\rho_{+,i}-\frac{3}{16\pi^2}
\right|
=o(\Vol M_i).
\]
Using the supplied identity
\[
\int_{M_i}\rho_{+,i}=\frac{2A_i}{3},
\]
the same mean convergence yields
\[
\Vol(M_i)=\frac{32\pi^2}{9}A_i+o(A_i).
\]
Thus the uniform subset error is \(o(A_i)\), exactly as stated in Step 12.

Equations (14)–(15) of the A03 note need this normalized interpretation: unnormalized \(L^1\to0\) and a global \(o(1)\) subset remainder are stronger than what the displayed near-equality estimates provide when \(A_i\) and volume grow. Step 12’s \(L^1\)-mean and \(o(A_i)\) formulation is the supported one.

The resulting formula gives distribution at the \(A_i\)-scale. It excludes concentration on a union whose total volume is \(o(A_i)\). It does not give an \(o(\Vol U_i)\) remainder for arbitrarily small \(U_i\).

For the rank-one decomposition
\[
F_A=F_H+\eta\wedge\Xi,\qquad \Xi=\iota_VF_A,
\]
horizontal dimension three implies
\[
P(F_A)=2\eta\wedge P(\Xi,F_H).
\]
If
\[
\fint_U|F_H|^2\le K
\]
and \(U\) carries the bulk density above, Cauchy–Schwarz gives
\[
\fint_U|\Xi|^2\ge c(K)>0
\]
up to vanishing errors. Thus the conclusion about persistent mixed connection curvature is valid under the stated regular collapsed-region hypotheses. Converting this algebraic identity into a theorem for approximately invariant collapsed metrics still requires quantified approximation terms.

## 4. Controlled-chart forbidden germ

The repaired local theorem is correct provided the harmonic-coordinate package \(Q\) is made explicit. A sufficient package consists of:

\[
Q^{-1}\delta\le(g_{ij})\le Q\delta,
\qquad
\|g_{ij}\|_{C^{1,\alpha}(B_h)}\le Q,
\]
together with a fixed interior ball \(B_{\sigma h}\), \(0<\sigma<1\).

In harmonic coordinates,
\[
g^{ab}\partial_a\partial_b g_{ij}
=-2\Ric_{ij}+Q_{ij}(g^{-1},\partial g).
\]
Uniform \(C^{1,\alpha}\) control gives subsequential \(C^{1,\alpha'}\) convergence. Since
\[
\Ric_i=-g_i+e_i,\qquad \|e_i\|_{L^\infty}\to0,
\]
interior elliptic estimates give strong \(W^{2,p}\) convergence on \(B_{\sigma h}\) for every finite \(p\). Taking \(p>2\) in dimension four is enough to pass quadratic curvature expressions in \(L^1\). The limiting metric is weakly Einstein, then elliptic bootstrapping makes it smooth.

Vanishing limiting defect gives
\[
s=-4,\qquad |W^+|^2=\frac1{24},
\qquad
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
Derdziński’s local Einstein–Weyl argument then makes the metric locally Kähler in the selected orientation. A Kähler–Einstein surface with \(s=-4\) instead satisfies
\[
|W^+|^2=\frac{s^2}{24}=\frac23,
\]
which is incompatible with \(1/24\).

The chart is therefore a genuine hypothesis, not a consequence of bounded Ricci. This avoids the pointwise-curvature issue exhibited by the Calderón–Zygmund spike. The A03 phrase that constant spectrum alone forces \(\nabla W^+=0\) should be read together with the Einstein harmonic-Weyl equation; constant eigenvalues by themselves do not prevent rotating eigenspaces.

The diameter-free maximal-function selection is also valid under the local Ricci lower bound. To obtain defect means tending to zero, rather than merely below a fixed number, use
\[
\bar F_i=\fint_{M_i}F_i,\qquad
\lambda_i=\sqrt{\bar F_i}.
\]
Then
\[
\frac{\Vol\{M_hF_i>\lambda_i\}}{\Vol(M_i)}
\le C(h)\sqrt{\bar F_i}\to0.
\]
Consequently any accessible set occupying a fixed positive fraction of total volume intersects the set where all relevant centered means tend to zero. This is the precise version of “positive-volume family.”

The normal-cover transport estimate is consistent with a \(3h\) buffer:
\[
\fint_{B_h(\hat p)}\pi^*F
\le
\frac{V_{-1}(3h)}{V_{-1}(h)}
\fint_{B_h(p)}F.
\]
Its proof compares lift multiplicities over \(B_h(p)\) with volume in \(B_{3h}(\hat p)\), followed by local Bishop–Gromov comparison. No diameter estimate or Myers theorem enters.

## 5. Mathematically decisive next object

The remaining issue is fixed-scale rank recovery on a positive volume fraction. A useful theorem would quantify the following alternative under
\[
\Ric\approx-g,\qquad
\sup_{r\le1}\fint_{B_r(p)}|\Rm|^2\le K,
\qquad
\sup_{r\le1}\fint_{B_r(p)}F\ll1:
\]

* either some \(\rho\ge r_*(K)>0\) admits a buffered normal cover with uniform four-dimensional volume ratio and controlled harmonic radius;
* or deficient buffered fundamental-group rank produces a definite filling, O’Neill, nilpotent-twisting, or mixed-connection energy at that scale.

The most concrete supporting computation is the \(\Lambda^2_+\) Levi-Civita connection for a collapsing Kaluza–Klein metric
\[
g_\ell=g_B+\ell^2(d\theta+\alpha)^2.
\]
An explicit decomposition of
\[
F_{A_+}=F_H+\eta\wedge\Xi
\]
in terms of \(g_B\), \(\ell\), \(d\alpha\), Hessians of \(\log\ell\), and O’Neill tensors would determine whether
\[
\Ric(g_\ell)+g_\ell\to0,\qquad
\operatorname{Spec}(W^+)\to
\left(-\frac16,\frac1{12},\frac1{12}\right),
\qquad
P(F_{A_+})\to\frac34
\]
can coexist with \(\ell\to0\) throughout a regular region. Taub–NUT supplies an exact calibration for this computation: core inclusion gives large centered curvature means, while annular unwrapping gives hyperbolic geometry with defect \(16\).

Thus Step 12 correctly replaces a finite-core picture by a diffuse mixed-curvature problem. It provides a sound conditional obstruction in controlled charts, but the all-dimensional Einstein-existence problem still requires the fixed-scale rank/mixed-energy theorem or an explicit collapsed reduced model realizing the calibrated equations.