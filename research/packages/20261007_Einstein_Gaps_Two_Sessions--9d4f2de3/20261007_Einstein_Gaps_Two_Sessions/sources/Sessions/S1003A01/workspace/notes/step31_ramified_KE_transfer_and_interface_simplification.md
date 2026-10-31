# Step 31 — Transfer to ramified compact Kähler–Einstein surfaces and the simplified interface

## 1. A new closed family carrying the certified saving

Use the normalization \(\operatorname{Ric}=-g\). Let
\[
X^\circ=\Gamma\backslash\mathbb B^2,\qquad (\bar X,D)
\]
be a smooth toroidal compactification of a neat arithmetic nonuniform ball quotient, and put
\[
L=K_{\bar X}+D.
\]
First pass to a sufficiently deep **principal congruence** subgroup of \(\Gamma\): because the intersection of principal congruence subgroups is trivial, one can exclude the finite set of nonidentity elements moving a chosen lift by at most twice the required marked radius. This produces an embedded marked complex-hyperbolic ball and keeps the later high-ramification covers inside the preliminary cover. For the certified \(x_0=.03,X=128\) cell, the outer radius in the \(\operatorname{Ric}=-g\) normalization is
\[
R_{128}=\sqrt6\,\operatorname{arsinh}\sqrt{128}
       =7.64512629467772\ldots,
\]
not \(4.32\) (the latter belongs to the older \(X=8\) witness). Fix a ball of radius \(R_{128}\) plus a fixed annular buffer. A cofinal sequence of further congruence covers with cusp ramification orders \(v_{m,\lambda}\to\infty\) suffices; literal nesting is not used.

Biquard--Guenancia prove local smooth convergence of the conical Kähler--Einstein metrics to the complex-hyperbolic metric on every fixed compact subset of \(X^\circ\), and §4.3 shows that for
\[
\beta_{m,\lambda}=v_{m,\lambda}^{-1}
\]
the pullback to the ramified compactification \(\bar X_m\) is a smooth metric \(g_m\) with \(\operatorname{Ric}_{g_m}=-g_m\) \cite{biquard2022degenerating}. If \(d_m\) is the covering degree, the fixed marked ball has \(d_m\) disjoint lifts, and all lifted metrics have the same \(C^2\) discrepancy
\[
\varepsilon_m=\|g_m-g_{CH}\|_{C^2(K)}\longrightarrow0
\]
on the fixed compact marked region \(K\). Thus no thick-part volume estimate is needed.

### Topology of the compactifications

Hurwitz gives
\[
K_{\bar X_m}=\pi_m^*\left(L-\sum_\lambda\beta_{m,\lambda}D_\lambda\right).
\]
The boundary elliptic curves are disjoint and adjunction gives \(L\cdot D_\lambda=0\). Hence, with
\[
A_m=K_{\bar X_m}^2,
\]
we have
\[
\frac{A_m}{d_m}=L^2+\sum_\lambda\beta_{m,\lambda}^2D_\lambda^2\longrightarrow L^2>0.
\]
Because the boundary elliptic curves have Euler characteristic zero and log proportionality gives \(L^2=3\chi(X^\circ)\),
\[
\chi(\bar X_m)=d_m\chi(X^\circ)=\frac{d_mL^2}{3}.
\]
Therefore
\[
\Delta_m:=3\chi(\bar X_m)-A_m
=-d_m\sum_\lambda\beta_{m,\lambda}^2D_\lambda^2>0,
\qquad \frac{\Delta_m}{A_m}\to0.
\]
In particular \(d_m\asymp A_m\), so the lifted marked balls occur with positive density relative to \(A_m\). The strict inequality \(A_m<3\chi(\bar X_m)\) also shows that these compact surfaces are not compact ball quotients.

The smooth negative Kähler--Einstein metric satisfies \([\omega_m]=2\pi c_1(K_{\bar X_m})\), so the canonical class is Kähler and hence ample by Kodaira. Thus \(\bar X_m\) is a smooth minimal surface of general type. Its canonical Seiberg--Witten structure is nonzero in the canonical chamber. LeBrun's polarized blow-up construction, including the \(b^+=1\) chamber selection when it occurs and the degree-one holonomy insertions for the \(S^1\times S^3\) summands, then gives for every metric a polarization-adapted actual class after choosing the exceptional signs \cite{lebrun2001ricci}. This is the precise field supply used below, not merely the existence of a cohomology class.

### Surgery parameters and the lower order

Choose \(Q_m\to\infty\) with \(Q_m=o(A_m)\), and suppose more generally that
\[
\frac{\Delta_m}{Q_m}\longrightarrow r,\qquad 0\le r<1.
\]
(The old coefficient is the case \(r=0\); it requires only \(\Delta_m=o(Q_m)\), not \(1\ll\Delta_m\).) Put
\[
M_m=\bar X_m\#k_m\overline{\mathbb{CP}}^{\,2}
\#\ell_m(S^1\times S^3),
\quad Q_m=k_m+4\ell_m,
\quad h_m=Q_m/A_m.
\]
Writing \(\Delta=3\chi-A\), direct characteristic-number calculation gives
\[
T_+=A-k-4\ell,
\qquad
T_-=\frac A3+\frac{4\Delta}{3}+5k-4\ell.
\]
Choose \((k_m,\ell_m)\) by rounding the real solution
\[
k_m=\frac{2(Q_m-\Delta_m)}9,
\qquad
\ell_m=\frac{7Q_m}{36}+\frac{\Delta_m}{18},
\]
so that \(16\ell_m-14k_m=4\Delta_m+O(1)\). Then
\[
\frac{k_m}{Q_m}\to\frac{2(1-r)}9,
\qquad
\frac{\ell_m}{Q_m}\to\frac{7+2r}{36}.
\]
Moreover
\[
T_{-,m}=\frac{A_m+Q_m}{3}+O(1),
\qquad
U_{\mathrm{top},m}=\frac{3\min(T_{+,m},T_{-,m})}{A_m}
=1+h_m+O(A_m^{-1})=1+h_m+o(h_m).
\]
The last equality uses \(Q_m\to\infty\). The canonical field has \(p\ge A_m\) and selected square \(a^2=A_m-k_m\ge T_{+,m}=A_m-Q_m\). The inherited linear-window theorem therefore yields
\[
\inf_g\mathcal E(g)\ge c h_m
\]
for all large \(m\) (and likewise for \(\mathcal J\)); its actual equations separately exclude Ricci-flat metrics.

For \(r=0\), one may always take
\(Q_m\asymp\sqrt{A_m\max\{\Delta_m,1\}}\), rounded to integers. For prescribed \(0<r<1\), the same conclusion applies to any chosen ramified tower with \(\Delta_m\to\infty\), by taking \(Q_m\sim\Delta_m/r\). Such towers are not hypothetical: for principal congruence Picard modular surfaces, the index has degree-eight level growth while the toroidal boundary self-intersection has the index divided by the square of the cusp-width parameter, so \(\Delta_m\to\infty\) and \(\Delta_m/A_m\to0\) \cite{dambi2014invariants}. If \(\Delta_m\) stays bounded, only \(r=0\) is compatible with \(Q_m\to\infty\). The symbolic algebra is reproduced in `workspace/scripts/step31_topology_window.py` and `workspace/scripts/step32_ramified_transfer_law.py`.

### Upper construction

The exact-CH-collar cell can be inserted into any selected lifted marked ball. Use the fixed buffer to append an exact CH annulus to the cell and choose a fixed cutoff \(\chi\). In the marked tensor coordinates set
\[
g_{m,\mathrm{ann}}=g_{CH}+\chi\,(g_m-g_{CH}).
\]
On the inner subannulus this is the cell's exact CH continuation; on the outer subannulus it is \(g_m\). Uniform ellipticity and the fixed cutoff show that \(g_{m,\mathrm{ann}}\) is positive for large \(m\), differs from CH by \(O(\varepsilon_m)\) in \(C^2\), and has
\[
\operatorname{Ric}(g_{m,\mathrm{ann}})+g_{m,\mathrm{ann}}=O(\varepsilon_m).
\]
Hence its raw annular defect is \(O(\varepsilon_m^2)\), while its volume and total-scalar increments relative to the marked CH annulus are \(O(\varepsilon_m)\) per site. Across \(k_m=O(Q_m)\) sites, these errors are respectively \(o(Q_m)\) and \(o(Q_m)\). The untouched background is exactly Einstein, so there is no error proportional to its full volume.

Treat the handles by the inherited shrinking construction, choosing their scale on the \(m\)-th manifold so their aggregate volume, scalar-moment, and defect errors are \(o(Q_m)\). Let the certified cell's exact-collar smoothing width tend to zero along the sequence. If
\[
\frac{J_1}{8\pi^2}\le1-\eta,
\]
then the complete-cell expansion gives
\[
\frac{\alpha(M_m)}{h_m}
\le 4(1-\eta)\frac{k_m}{Q_m}
   +16\frac{\ell_m}{Q_m}+o(1),
\]
and therefore
\[
\boxed{\limsup_m\frac{\alpha(M_m)}{h_m}
\le4-\frac{8\eta}{9}(1-r).}
\]
Using the rigorous \(x_0=.03,X=128\) enclosure
\[
\frac{J_1}{8\pi^2}\le0.9956710815089548,
\qquad \eta=0.004328918491045219,
\]
from `workspace/data/perp_area/rigorous_x00.03_X128_d20.json`, the \(r=0\) specialization is
\[
\boxed{\limsup_m\frac{\alpha(M_m)}{h_m}
\le4-\frac{8\eta}{9}<3.996152073.}
\]
For every fixed \(0<r<1\) the saving remains strict, but is reduced by the exceptional-site fraction \(1-r\). This is a construction law for the chosen topology and separated handle geometry, not an optimality result and not a transition theorem at \(r=1\). A fixed smoothing width or fixed nonsymmetric perturbation gives the same formulas with a smaller uniform margin \(\eta'<\eta\); the displayed certified endpoint uses a diagonal sequence of smoothing widths tending to zero.

## 2. Why the saving transfers

The ingredients used by the upper construction are local and geometric:

1. a fixed marked region close in \(C^2\) to CH at the cell's physical scale;
2. a negative Einstein background, so the exterior contributes zero raw defect;
3. the perpendicular compatible field inside the cell, where self-dual Weyl depletion, scalar response, contact closure and Nijenhuis transport coexist on one metric;
4. an exact CH collar on the cell, which makes the splice error quadratic in the background discrepancy for the raw Ricci defect;
5. enough disjoint marked regions relative to the surgery count.

Global local symmetry of the closed background is not used. The ramified family supplies these ingredients while changing its Chern slope away from equality.

## 3. Nonsymmetric openness

Fix a smooth exact-collar subthreshold cell \(g_c\), with a compact set \(K\) disjoint from the bolt and the exact collar. For every smooth symmetric tensor \(h\) supported in \(K\), positivity and continuity of the Ricci map as a function of the metric two-jet imply
\[
\|h\|_{C^2}<\epsilon
\quad\Longrightarrow\quad
J_6(g_c+h)<8\pi^2
\]
for sufficiently small \(\epsilon\). The bolt, marking, topology and exact collar are unchanged. Choosing non-\(SU(2)\)-invariant \(h\) gives an open family of genuinely nonsymmetric subthreshold cells. Replication of any fixed compact family with a uniform reduced margin produces a strict sub-four coefficient; preserving the sharper certified coefficient instead uses perturbations and smoothing losses tending to zero.

## 4. Simplified \(B-b_+\) relation

The Step-30 formula simplifies exactly because its bracket is
\[
u_f=a_f'-\gamma_f.
\]
Hence
\[
\boxed{B-b_+=6\phi u_f-9\phi^2,}
\]
and, if \(b_+=2-\mathcal C(u)\),
\[
\boxed{B=2-[\mathcal C(u)-u_f^2]-(u_f-3\phi)^2.}
\]
The separately large ratios in the first expansion cancel. The revised `workspace/scripts/step29_local_AK_flux.py` evaluates this formula on the improved and certified-profile cells. In `workspace/data/step31/Bsimple_x0038_X128.json` and `Bsimple_certifiedprofile_x003_X128.json`, the residual between the direct and simplified formulas ranges from about \(10^{-16}\) in the core to \(4\times10^{-12}\) near the far collar.

This also corrects the Step-30 collapse interpretation. The moment \(\phi\) has a multiplicative normalization fixed by the outer marking:
\[
\phi(s)=\phi(T_c)\exp\left(-\int_s^{T_c}\frac{2a_f}{a_ga_h}\,dt\right).
\]
It cannot be normalized from a collapsed entry alone. If a complete marked collapsed trajectory has bounded \(u_f\) and collar-normalized \(\phi(s)\to0\), then \(B(s)-b_+(s)\to0\); no estimate of \(\phi\cosh q\) is needed. The A02 scale-free calibrated leaves omit the absolute radial scale and this outer normalization, so their existing records do not yet decide whether \(B(s)\) remains controlled. The next collapse calculation must reconstruct a complete marked trajectory or evolve \(\phi\) from the actual outer collar.