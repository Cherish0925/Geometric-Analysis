# Step 4 — Direct positive-q cells, inner-scale coercivity, and quantitative fixed-exterior loss

Session S1003A01, Step 4. Notation follows I54/I55 and `step3_coupled_compensation_and_route_reassessment.md`. The cell metric is

\[
G=e^{2\phi}\left\{\frac{dr^2}{F}+r^2(e^{2w}\sigma_1^2+e^{-2w}\sigma_2^2)+r^2F\sigma_3^2\right\},
\]

with \(r_0^2=\mu\), exact CH outer collar, and \(j=J/(2\pi^2)\). Define

\[
I_R=\frac14(\mu^{-2}-R^{-4}),\quad M_0=1+\frac2\mu,
\quad q=T_\phi-P_w,
\]

so I55 gives

\[
j=\frac{(M_0-q)^2}{4I_R}+R_X+R_Y+R_Z+R_V. \tag{1}
\]

This Step tested the previously unvisited signed sector \(q>0\), corrected the fixed-exterior stationarity argument at the free/fixed interface, and extracted the natural inner-scale inequality that now organizes the diagonal route.

## 1. Direct positive-q instrument

`workspace/scripts/cell_qsearch.py` minimizes \(j\) while constraining \(q=fM_0\). It uses the exact bolt/collar basis of `cell_opt.py` and reports all terms in (1). Three conformal initializations were compared:

- `inner`: a smooth bump in \(r/\sqrt\mu\) initially supported on \(2<r/\sqrt\mu<3\);
- `fixed`: a bump on a fixed physical annulus \(0.55<r<1.05\);
- `broad`: the lowest exact-collar Chebyshev mode.

Both signs of \(\phi\) and zero/nonzero low-mode triaxial seeds were used. After initialization, all variables are free, so these labels describe continuation basins, not a preserved support condition. Raw data are

- `workspace/data/cell_qsearch/main_mu01.jsonl` for \(\mu=.1\), degree 22, 650 Gauss nodes;
- `workspace/data/cell_qsearch_small/musmall.jsonl` for \(\mu=.03,.01\), degree 22, 750 nodes;
- the selected robust profiles are in `workspace/data/cell_qsearch/qsearch_best.csv`.

The direct Ricci integral and I55 square decomposition agree to at worst \(7.3\times10^{-11}\) over all runs, and usually \(10^{-13}\). The I54 `B0` value is inferred from its exact identity, so its machine-zero closure is bookkeeping, not an independent Weyl implementation.

### 1.1 The search actually enters the necessary signed sector

A subthreshold cell must satisfy I55 (8.4). Its positive lower endpoint is

\[
\delta_{\mu,R}=1+\frac2\mu\left(1-\sqrt{1-\mu^2/R^4}\right),
\]

which is approximately \(1.0063,1.0019,1.0006\) at \(R=2\), \(\mu=.1,.03,.01\). The smallest searched targets were \(q=1.05,6.77,20.1\), respectively, and hence all cross this necessary lower endpoint. The previous fixed-\(N\) runs never entered this regime; this one does.

No profile had \(j<4\), or even \(j<K\). The best robust records were:

| \(\mu\) | \(f=q/M_0\) | \(j\) | \(K\) | projection | \(R_X\) | \(R_Y\) | \(R_Z\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| .10 | .05 | 7.1723 | 4.4128 | 3.9825 | 1.0549 | .5347 | 1.6002 |
| .10 | .15 | 11.8396 | 4.4128 | 3.1882 | 3.8527 | 1.0230 | 3.7758 |
| .03 | .10 | 8.6603 | 4.1211 | 3.3381 | 2.0308 | .7062 | 2.5852 |
| .01 | .10 | 8.4084 | 4.0401 | 3.2725 | 1.9414 | .6719 | 2.5226 |
| .01 | .35 | 16.0987 | 4.0401 | 1.7070 | 9.5245 | .7138 | 4.1534 |

These minima are numerical competitors, not certified constrained minima. The augmented-Lagrangian stopping check enforces the q constraint but does not certify the full KKT system or rule out negative Hessian modes.

### 1.2 What mechanism the data do and do not test

The cheapest profiles return to \(w=0\), so they are in the already-proved conformally Kähler class. In seeded runs the final amplitudes are commonly \(10^{-4}\)–\(10^{-3}\), with tiny \(P_w,N,R_V\). Thus the computation resolves the conformal payment in the signed dangerous sector but does **not** exclude an unknown finite-amplitude \(w\ne0\) escape. The unsearched half \(M_0<q<2M_0\) must also remain open: the projection is symmetric around \(q=M_0\), but the residual system is not.

For the low-cost branch, forcing \(q\) positive lowers the projection term exactly as intended, but the payment moves into \(R_X\) and \(R_Z\), with \(R_Y\) becoming significant nearer \(M=0\). At \(\mu=.01,f=.1\), the formal projection saves \(K-3.2725=.7676\), while the residuals total \(5.1359\), giving \(j=8.4084\). At \(f=1\), the projection nearly vanishes but the total cost is about \(35.45\) in the lowest recorded basin. This is the numerical realization of I55's zero-moment warning: killing \(M\) does not kill the metric residual.

A second, high-cost continuation basin was found from the fixed physical bump. At fixed \(f\), its cost scales approximately as \(j\sim C_f/\mu\), and \(\phi_{\max}\sim C_f'/\sqrt\mu\); for example at \(f=.1\), \(\mu j\) is about 10.84 at \(\mu=.03\) and 10.42 at \(\mu=.01\). The low-cost broad branch remains \(O(1)\). Because support is not preserved by the optimization, this is evidence for two basins rather than a theorem separating scales. At high \(q\), many runs approach the soft positivity floor for \(F\), so only records with `F_min_scaled>0.05` were used in the robust summary.

The independent SU(2)_L relative-orientation computation in peer Session S1003A02 provides complementary evidence outside this diagonal fixed-eigenframe parameterization. Its rotated Bianchi-IX cells show a positive first-order orientation penalty: at \(x_0=.003\), the slope \((P/(8\pi^2)-1)/x_0\) rises from 5.90 at aligned angle to 15.20 at \(\pi/2\), with both \(4\Delta W^+\) and \(\Delta S/12\) positive. Files are `Sessions/S1003A02/workspace/scripts/o11_rotated_cell.py` and `.../data/o11rot/summary.csv`. Some nonzero-angle optimizations ended at iteration/line-search limits, so these remain competitor values, but they show that rotating the Burns and CH Weyl axes does not expose the desired same-metric negative cost; the misalignment is paid at the same first order as the exceptional scale.

## 2. Inner-scale limit and the next proof object

Put \(r=\sqrt\mu x\), and suppose a low-cost branch has

\[
F_\mu(\sqrt\mu x)\to\mathcal F(x),\quad
w_\mu(\sqrt\mu x)\to W(x),\quad
\phi_\mu(\sqrt\mu x)\to\Phi(x),
\]

with bolt conditions

\[
\mathcal F(1)=0,\quad \dot{\mathcal F}(1)=2,\quad
W(1)=\dot W(1)=0,
\]

and terminal behavior \((\mathcal F,W,\Phi)\to(1,0,0)\) as \(x\to\infty\). If

\[
\vartheta=\lim_{\mu\downarrow0}\mu q,
\]

then \(q=fM_0\) corresponds to \(\vartheta=2f\). The signed moment becomes

\[
\vartheta=\widehat T-\widehat P,
\]

\[
\widehat T=2\int_1^\infty\frac{\mathcal F\dot\Phi^2}{x}\,dx,
\]

\[
\widehat P=\int_1^\infty\left[
\frac{2\mathcal F\dot W^2}{x}
+\frac{8(\cosh2W-1)}{x^3}
+\frac{8\sinh^2(2W)}{x^3\mathcal F}\right]dx.
\]

The rescaled radial identity is

\[
\int_1^\infty\frac{\widehat X}{x}\,dx=2-\vartheta,
\]

and the limiting energy has the exact formal structure

\[
\mathcal J_\infty=(2-\vartheta)^2+\widehat{\mathscr R}, \tag{2}
\]

where

\[
\begin{aligned}
\widehat{\mathscr R}={}&\frac14\int_1^\infty x^3
\left(\widehat X-\frac{4(2-\vartheta)}{x^4}\right)^2dx
+\frac14\int_1^\infty x^3\widehat Y^2dx\\
&+\frac12\int_1^\infty x^3\widehat Z^2dx
+2\int_1^\infty x^3\widehat V^2dx.
\end{aligned}
\]

The scale-correct diagonal theorem to prove is therefore

\[
\boxed{\widehat{\mathscr R}\ge \vartheta(4-\vartheta),
\qquad 0<\vartheta<4,} \tag{3}
\]

which is equivalent to \(\mathcal J_\infty\ge4\). It is sharp at \(\vartheta=0\): \(\mathcal F=1-x^{-2},W=\Phi=0\) gives \(\widehat X=8x^{-4}\), all other residuals zero, and energy 4. The present data cover only \(0<\vartheta\le2\), predominantly with \(W=0\); the genuinely new theorem is (3) for finite-amplitude \(W\ne0\) over the full interval.

A useful logarithmic formulation takes \(s=\log x\), \(A=x\dot\Phi\), \(B=x\dot W\). The exact \(Z,V\) identities become a coupled Riccati/transport system schematically

\[
\partial_sA-2A-A^2=-B^2+\frac{4\sinh^2(2W)}{\mathcal F^2}
-\frac{x^2\widehat Z}{2\mathcal F},
\]

\[
x^2\widehat V=-\mathcal F\partial_sB-(\partial_s\mathcal F)B
-2\mathcal F B-2\mathcal F AB
+\frac{4\sinh4W}{\mathcal F}-4\sinh2W.
\]

This identifies the analytic content missing from a moment-only argument: the \(e^{-2s}\)-weighted gain in \(\widehat T-\widehat P\) must be paid through the weighted squares of the radial Riccati and anisotropy transport residuals, together with \(\widehat X,\widehat Y\). Proving (3), rather than bounding \(T_\phi\) or \(P_w\) separately, is the strongest next diagonal route.

## 3. Fixed exterior: what minimality gives, and the interface defect

Let \(\mathcal A\) be smooth cell metrics equal to CH on a fixed open outer collar and let \(g_i\in\mathcal A\) be a true minimizing sequence, \(J(g_i)\to J_*\). Suppose marked, single-sheeted \(C^2\) convergence holds on compact subsets of a regular free-interior region. If \(h\) is compactly supported there, transport it to \(h_i\). Then, for fixed small \(t\),

\[
J(g_i+t h_i)-J(g_i)\ge J_*-J(g_i)=o(1).
\]

The local difference converges under \(C^2\), so

\[
J_K(g_\infty+t h)\ge J_K(g_\infty).
\]

Using both signs yields local stationarity and stability. This avoids passing a higher-order regularizer's equation. It is valid only away from singular, multi-sheeted, and fixed-collar regions and does not itself supply regularity beyond the local variational equation.

The previous Step overextended this to the collar interface. Compactly supported free-interior variations give

\[
(\Delta_++1)(s+4)=0
\]

and, after establishing \(s=-4\), an elliptic system for \(E=\operatorname{Ric}+g\). But \(C^2\) matching to CH gives only \(E|_\Sigma=0\). Extending \(E\) by zero across the fixed/free interface produces distributionally a possible term

\[
(\Delta E-AE)_{\rm dist}
=\pm(\nabla_\nu E)_{\rm free}\,\delta_\Sigma. \tag{4}
\]

Allowed variations vanish on the fixed open collar and do not detect this interface stress. Thus local stationarity does not prove the tensor equation across \(\Sigma\), and Dirichlet data alone do not imply \(E=0\).

Sufficient repairs include: fixed-coordinate \(C^3\) convergence across the interface; a global weak equation with no interface measure; an actual CH open set lying inside the free PDE region; or a separate coercive Dirichlet theorem for the trace-free Einstein operator. Once (4) vanishes, unique continuation gives \(E=0\); Einstein analyticity and the retained CH germ then imply that the regular base is locally CH. This is the exact missing input before the developing-map rigidity of Step 3 can be used.

## 4. Quantitative recovered-volume theorem

Let \(D\) be the original CH ball of background volume \(d\), and define

\[
\mathcal F(g)=\frac{(s+3)^2}{3}+1+4|W^+|^2\ge0.
\]

On CH, \(\mathcal F=4\). The relative identity is

\[
J(g_i)-8\pi^2Q_{\rm cell}=\int_C\mathcal F(g_i)-4d. \tag{5}
\]

Suppose a single-sheeted marked region \(\mathcal R\subset D\) is recovered in \(C^2_{\rm loc}\) as the original CH background. On compact exhaustions of \(\mathcal R\), the integral tends to four times CH volume; nonnegativity controls everything omitted. Therefore

\[
\liminf_iJ(g_i)\ge8\pi^2Q_{\rm cell}-4v_{\rm miss},\qquad
v_{\rm miss}=d-\operatorname{Vol}_{\rm CH}(\mathcal R). \tag{6}
\]

In particular,

\[
\boxed{\limsup_iJ(g_i)\le8\pi^2Q_{\rm cell}-\delta
\quad\Longrightarrow\quad v_{\rm miss}\ge\delta/4.} \tag{7}
\]

For \(j\le4-\epsilon\) in a one-blowup cell, \(\delta=2\pi^2\epsilon\), so \(v_{\rm miss}\ge\pi^2\epsilon/2\). A finite set of concentration points has zero CH volume and cannot itself create a strict deficit. A subthreshold degeneration must lose positive background volume, fail single-valued regular recovery, or leave the orbifold framework; bubbles and collapse matter only insofar as they cause such loss.

Equation (6) is conditional on constructing the recovery regions. It does not identify missing CH background volume with actual replacement volume under \(g_i\), and no stronger coefficient follows merely from the pointwise bound \(\mathcal F\ge1\).

## 5. Locally symmetric extension and its scope

The developing-map argument extends from CH to any complete locally real-hyperbolic base under the same hypotheses. If \(X=\mathbb H^4_{-1/3}/\Gamma\) is closed smooth, \(U=X\setminus\cup D_a^\circ\) is connected, and a connected effective boundaryless complete locally real-hyperbolic orbifold \(\mathcal O=\mathbb H^4_{-1/3}/\Gamma'\) contains \(U\) by a smooth injective local isometry, then \(\Gamma<\Gamma'\). Any extra deck transformation would send the connected unbounded lift of \(U\) disjointly into a bounded lifted ball, impossible. Hence \(\Gamma'=\Gamma\), so \(\mathcal O=X\) smoothly.

This does not apply to a merely negative Einstein, \(W^+\)-flat base: in four dimensions \(W^+=0\) fixes only one curvature-operator block; real hyperbolicity also requires \(W^-=0\). If an Einstein regular base contains a genuine real-hyperbolic open set and the interface stress has been removed, analyticity propagates the full constant-curvature tensor and the argument can then start. Otherwise half-conformal flatness is not a substitute for a real-hyperbolic developing structure.

Likewise, the O11 developing-map argument does not directly exclude a general non-Kähler Einstein orbifold with Ricci-flat ALE fillers. It first requires the local CH conclusion, which is precisely what (4) obstructs at present. Once single-sheeted CH recovery covers all but zero background volume, however, the threshold follows already from (6), regardless of how the ALE tree distributes topology. This distinction is important for both O11 and the peer O10 degeneration programme.

## 6. Route assessment

The Step-3 handoff was scientifically useful: direct q targeting revealed a low-cost positive-q basin and identified its payments. But it also showed that continuing the same optimizer will not settle C1: the best profiles collapse back to the proved \(w=0\) class, while high-q runs approach the positivity floor. The finite-amplitude diagonal unknown should now be attacked through the inner-limit inequality (3), preferably by deriving a weighted Hardy/Riccati estimate and using numerical searches only to test its sharp sublemmas or find a finite-amplitude counterprofile. The peer rotated-cell result independently shows that the most natural non-diagonal relative-orientation modulus is penalized at first order, strengthening the case for a lower mechanism without proving all-cell optimality.

The compactness route is now quantitatively clearer. It need not charge each bubble. It must either construct CH recovery regions whose missed volume tends to zero, yielding the threshold from (6), or explain a positive-volume loss/multi-sheet/collapse mechanism. Local comparison minimality supplies the free-interior equation, but removing the interface stress (4) is a separate analytic theorem and should not be hidden inside the word stationarity.
