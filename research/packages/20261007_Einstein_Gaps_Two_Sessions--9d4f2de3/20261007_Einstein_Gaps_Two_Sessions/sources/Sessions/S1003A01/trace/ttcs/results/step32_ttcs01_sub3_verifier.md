# TTCS Independent Branch Record

```json
{
  "step_id": 32,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md",
    "Sessions/S1003A01/workspace/scripts/step32_ramified_transfer_law.py",
    "Sessions/S1003A01/workspace/data/step32/ramified_transfer_r05.json",
    "Sessions/S1003A01/workspace/data/perp_area/rigorous_x00.03_X128_d20.json",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/supplements/sources/20261004/step10_rigorous_subthreshold_cell_and_O11.md",
    "Skills/geometric-analysis/research/supplements/sources/20261004/step11_independent_review_O11_and_mixed_cost.md"
  ]
}
```

## Task

Independently verify the upper-construction and normalization part of the revised ramified KE transfer. Check the exact physical radius of the certified x0=.03, X=128 cell after scaling to Ric=-g; the fixed-buffer interpolation g_CH+chi(g_m-g_CH), its positivity and C^2/Ricci/volume/scalar estimates; how those errors enter the complete-cell formula at the Q=o(A) scale; the separated shrinking-handle contribution; integer rounding under Delta/Q→r∈[0,1); and the coefficient limsup alpha/h <= 4-(8 eta/9)(1-r), including the distinction between a diagonal smoothing sequence and a fixed reduced margin. Check also that the statement is only an upper construction law and not an optimality or r=1 transition theorem. Identify any missing quantifier or mismatch between the rigorous certificate and the geometric marked-ball hypothesis.

## Output

# Scientific verification memo

## 1. Normalization and marked radius

For the complex-hyperbolic profile used by the cell,
\[
G_{\mathrm{CH}}(x)=x+x^2,
\qquad
g_{\mathrm{CH,rad}}=\frac{dx^2}{4x(1+x)}.
\]
Writing \(x=\sinh^2\rho\) gives \(g_{\mathrm{CH,rad}}=d\rho^2\). Thus the reference CH ball whose outer sphere is \(x=X\) has radius
\[
\rho_X=\operatorname{arsinh}\sqrt X
\]
in the normalization \(\operatorname{Ric}=-6g\).

Under \(\widetilde g=6g\), distances acquire the factor \(\sqrt6\), while
\[
\operatorname{Ric}_{\widetilde g}
=\operatorname{Ric}_g=-6g=-\widetilde g.
\]
Consequently, for \(X=128\),
\[
\boxed{
R_{128}
=\sqrt6\,\operatorname{arsinh}\sqrt{128}
=\sqrt6\log(8\sqrt2+\sqrt{129})
=7.64512629467772\ldots .
}
\]
This is the radius of the CH reference ball removed from the ambient metric, not the intrinsic distance from the modified bolt to its outer collar. The value \(x_0=.03\) therefore does not enter this marked-ball radius. The earlier value near \(4.32\) is indeed the \(X=8\) radius.

The raw defect is invariant under this rescaling:
\[
\int |\operatorname{Ric}_{6g}+6g|_{6g}^{2}\,dV_{6g}
=
\int |\operatorname{Ric}_{g}+6g|_{g}^{2}\,dV_g,
\]
because the squared norm of a covariant two-tensor contributes \(6^{-2}\), while four-dimensional volume contributes \(6^2\). Hence a certificate for \(J_6/(8\pi^2)\) transfers without another numerical factor to \(J_1/(8\pi^2)\).

Appending an exact CH annulus outside \(x=128\) changes neither the raw defect nor the relative scalar moment \(I+4V\), since \(\operatorname{Ric}=-g\) and \(s=-4\) there. The preliminary congruence cover must contain an embedded ball of radius \(R_{128}+b\), where \(b>0\) is the chosen fixed physical buffer.

## 2. Fixed-buffer interpolation

Let \(K_{\mathrm{ann}}\) be the fixed annulus in marked tensor coordinates and set
\[
h_m=g_m-g_{\mathrm{CH}},
\qquad
\|h_m\|_{C^2(K_{\mathrm{ann}})}\le \varepsilon_m\to0.
\]
Choose a fixed smooth function \(0\le\chi\le1\), equal to zero on the inner subannulus and one on the outer subannulus, and define
\[
g_{m,\mathrm{ann}}=g_{\mathrm{CH}}+\chi h_m.
\]

### Positivity

Because this is pointwise a convex combination
\[
g_{m,\mathrm{ann}}=(1-\chi)g_{\mathrm{CH}}+\chi g_m,
\]
it is positive definite whenever \(0\le\chi\le1\). Even without this normalization of \(\chi\), positivity follows for all large \(m\) from uniform \(C^0\) closeness to \(g_{\mathrm{CH}}\).

### Two-jet and Ricci estimates

The cutoff and annulus are fixed, so
\[
\|\chi h_m\|_{C^2(K_{\mathrm{ann}})}
\le C_\chi\varepsilon_m.
\]
On a uniformly elliptic \(C^2\) neighborhood of \(g_{\mathrm{CH}}\), the map
\[
j^2g\longmapsto \operatorname{Ric}(g)+g
\]
is locally Lipschitz. Since \(\operatorname{Ric}(g_{\mathrm{CH}})+g_{\mathrm{CH}}=0\),
\[
\|\operatorname{Ric}(g_{m,\mathrm{ann}})
       +g_{m,\mathrm{ann}}\|_{C^0}
\le C\varepsilon_m.
\]
The annulus has fixed uniformly controlled volume, hence
\[
\int_{K_{\mathrm{ann}}}
 |\operatorname{Ric}(g_{m,\mathrm{ann}})
       +g_{m,\mathrm{ann}}|^2\,dV
=O(\varepsilon_m^2).
\]

Similarly, smooth dependence of the volume density on the metric zero-jet and of scalar curvature on its two-jet gives
\[
\left|\operatorname{Vol}(g_{m,\mathrm{ann}})
-\operatorname{Vol}(g_{\mathrm{CH}})\right|
=O(\varepsilon_m),
\]
\[
\left|\int s_{g_{m,\mathrm{ann}}}\,dV_{g_{m,\mathrm{ann}}}
-\int s_{g_{\mathrm{CH}}}\,dV_{g_{\mathrm{CH}}}\right|
=O(\varepsilon_m).
\]
The removed \(g_m\)-ball is itself \(C^2\)-close to the corresponding CH ball, so its volume and scalar-integral differences from the CH reference are also \(O(\varepsilon_m)\). This comparison of the whole removed region, not only the transition annulus, is what connects the CH complete-cell formula to the varying KE background.

Across \(k_m=O(Q_m)\) sites,
\[
O(k_m\varepsilon_m)=o(Q_m),\qquad
O(k_m\varepsilon_m^2)=o(Q_m).
\]
No relation such as \(Q_m\varepsilon_m\to0\) is needed: after division by \(Q_m\), these terms are \(O(\varepsilon_m)\) and \(O(\varepsilon_m^2)\).

The exterior of the surgery regions contributes exactly zero raw defect because \(g_m\) is Einstein. Thus there is no \(A_m\varepsilon_m^2\) contribution.

## 3. Entry into the complete-cell expansion

For any constructed metric write
\[
V=\operatorname{Vol}(g),\qquad
I=\int s_g\,dV_g,\qquad
D=\int|\operatorname{Ric}_g+g|^2\,dV_g,
\]
and set
\[
T=I+4V.
\]
If \(R=\int|\operatorname{Ric}|^2\), then
\[
R=D+4V-2T,\qquad I=T-4V.
\]
Therefore the functional used in the complete-cell calculation satisfies the exact identity
\[
\mathcal E(g)
=4-\frac{I^2}{VR}
=\frac{4D-T^2/V}{4V+D-2T}.
\]

For the compact KE background,
\[
[\omega_m]=2\pi c_1(K_{\bar X_m}),\qquad
V_m^0=\frac12[\omega_m]^2=2\pi^2A_m.
\]
The replicated construction has
\[
V_m=2\pi^2A_m+O(Q_m),\qquad T_m=O(Q_m),
\]
and
\[
D_m=k_mJ_{1,m}+32\pi^2\ell_m+o(Q_m).
\]
Here:

* \(J_{1,m}\) is the raw defect of the smoothed single-blowup cell;
* the fixed-buffer splices contribute \(O(k_m\varepsilon_m^2)=o(Q_m)\);
* the volume and scalar-moment splice terms are \(o(Q_m)\);
* the separated handle construction contributes \(32\pi^2\ell_m+o(Q_m)\).

Since \(Q_m=o(A_m)\),
\[
\frac{T_m^2}{V_m}=O(Q_m^2/A_m)=o(Q_m),
\]
and
\[
4V_m+D_m-2T_m=8\pi^2A_m+O(Q_m).
\]
It follows that
\[
\mathcal E(g_m^{\mathrm{constr}})
=
\frac{D_m}{2\pi^2A_m}+o(Q_m/A_m).
\]
With \(h_m=Q_m/A_m\),
\[
\frac{\alpha(M_m)}{h_m}
\le
\frac{\mathcal E(g_m^{\mathrm{constr}})}{h_m}
=
\frac{k_mJ_{1,m}+32\pi^2\ell_m}{2\pi^2Q_m}+o(1).
\]

This exact moment calculation explains why the \(O(Q_m)\) cell volume and scalar changes do not appear in the leading coefficient: their linear contributions cancel, while \(T_m^2/V_m=o(Q_m)\).

## 4. Separated shrinking handles

The supplied Step-11 analysis gives the exact-CH pure-handle infimum
\[
\inf J_{\mathrm{handle}}=32\pi^2\ell.
\]
The value is approached by shrinking cores. For the \(m\)-th manifold, the scales may be chosen so that
\[
D_{\mathrm{handles}}
=32\pi^2\ell_m+o(Q_m),
\]
while their aggregate volume and \(I+4V\) contributions are \(o(Q_m)\).

Because \(\ell_m=O(Q_m)\), it is enough that the per-handle excess tend to zero. For example, a per-handle excess \(e_m\to0\) gives total excess \(O(\ell_me_m)=o(Q_m)\). Each metric in the sequence remains smooth at its chosen positive scale. The endpoint \(32\pi^2\ell_m\) uses scales varying with \(m\); a single fixed handle model would generally add a fixed per-handle excess to the coefficient.

The number of required blowup and handle sites is \(k_m+\ell_m=O(Q_m)=o(A_m)\), while the marked lifts occur in number comparable to \(A_m\). Thus site availability is sufficient.

## 5. Integer realization and the balance residual

Start with an integer target \(\widehat Q_m\) satisfying
\[
\widehat Q_m\to\infty,\qquad
\widehat Q_m=o(A_m),\qquad
\frac{\Delta_m}{\widehat Q_m}\to r<1.
\]
The real balanced solution is
\[
k_m^*=\frac{2(\widehat Q_m-\Delta_m)}9,\qquad
\ell_m^*=\frac{7\widehat Q_m+2\Delta_m}{36}.
\]

There are two equivalent integer conventions.

1. Round \(k_m^*,\ell_m^*\) independently and define
   \[
   Q_m=k_m+4\ell_m.
   \]
   Then \(Q_m=\widehat Q_m+O(1)\).

2. Preserve \(Q_m=\widehat Q_m\) exactly by choosing \(k_m\equiv Q_m\pmod4\) nearest to \(k_m^*\), and set
   \[
   \ell_m=\frac{Q_m-k_m}{4}.
   \]
   Since the allowed \(k_m\)'s have spacing four, \(k_m-k_m^*=O(1)\).

Under either convention,
\[
b_m:=16\ell_m-14k_m-4\Delta_m=O(1),
\]
and
\[
\frac{k_m}{Q_m}\to\frac{2(1-r)}9,\qquad
\frac{\ell_m}{Q_m}\to\frac{7+2r}{36}.
\]
Because \(r<1\), \(k_m\) and \(\ell_m\) are eventually positive.

The topological quantities then satisfy
\[
T_{+,m}=A_m-Q_m,
\]
and, directly from the definition of \(b_m\),
\[
T_{-,m}
=\frac{A_m+Q_m}{3}-\frac{b_m}{3}
=\frac{A_m+Q_m}{3}+O(1).
\]
Since \(Q_m=o(A_m)\), \(T_{-,m}\) is the smaller term for large \(m\), and
\[
\frac{3\min(T_{+,m},T_{-,m})}{A_m}
=1+\frac{Q_m}{A_m}+O(A_m^{-1})
=1+h_m+o(h_m).
\]
The last step uses \(Q_m\to\infty\), since \(A_m^{-1}/h_m=Q_m^{-1}\to0\).

The Step-31 wording defines \(Q_m=k_m+4\ell_m\) and then speaks of rounding a real solution written in terms of \(Q_m\). The asymptotics are valid, but one of the two conventions above makes the quantifiers and the \(O(1)\) residual explicit.

## 6. Coefficient and smoothing choices

Suppose
\[
\frac{J_{1,m}}{8\pi^2}
\le 1-\eta+o(1).
\]
Then
\[
\begin{aligned}
\limsup_m\frac{\alpha(M_m)}{h_m}
&\le
4(1-\eta)\frac{2(1-r)}9
+16\frac{7+2r}{36}\\
&=
\boxed{4-\frac{8\eta}{9}(1-r)}.
\end{aligned}
\]
Thus the coefficient algebra in `step32_ramified_transfer_law.py` and its JSON output is correct.

Using the recorded endpoint
\[
U=0.9956710815089548,\qquad
\eta=1-U=0.004328918491045219,
\]
the \(r=0\) value is
\[
4-\frac{8\eta}{9}
=3.996152072452404\ldots
<3.996152073.
\]

### Diagonal smoothing

The numerical cell profile appears to be a finite-regularity exact-matching profile before flat cutoff smoothing. If its smoothings satisfy
\[
J_{1,\delta}\longrightarrow J_{1,0},
\]
choose \(\delta_m\to0\). Then
\[
\frac{J_{1,\delta_m}}{8\pi^2}\le U+o(1),
\]
so the displayed endpoint with \(\eta=1-U\) survives in the limsup. The handle scales are likewise chosen along the sequence.

### One fixed smooth cell

For any fixed
\[
0<\eta'<\eta,
\]
continuity under collar smoothing supplies a sufficiently small fixed width with
\[
J_{1,\delta}\le8\pi^2(1-\eta').
\]
Replication of this one cell gives
\[
\limsup_m\frac{\alpha(M_m)}{h_m}
\le4-\frac{8\eta'}9(1-r)<4.
\]
Without a separate enclosure for the smoothed profile, the full numerical value \(\eta\) belongs to the diagonal construction, while a fixed cell carries a chosen reduced margin \(\eta'<\eta\).

## 7. Certificate-to-geometry items requiring explicit data

### The \(x_0=.03,\ X=128\) JSON is not a complete geometric artifact by itself

`rigorous_x00.03_X128_d20.json` records \(x_0,X\) and an integral enclosure, but it points to
`../data/perp_area/x00.03_X128_d20.json`, which was not supplied here. The displayed file alone does not encode:

* the 20-degree profile itself;
* the identification \(x=\sinh^2\rho\);
* smooth ordinary-blowup behavior at \(x=x_0\);
* the order of matching to CH at \(x=128\);
* the smoothing estimate producing a smooth exact-CH collar;
* the normalization of the integrand as \(J_6/(8\pi^2)\).

The older \(x_0=.01\) documentation proves all analogous points for that profile, but it is not a proof for the \(x_0=.03\) profile. Thus the transfer calculation is verified provided the corresponding \(x_0=.03\) profile and smoothness record establish these geometric properties.

### Precision of the serialized Arb interval

The rigorous field is displayed as
\[
[0.99567\mathbin{+/-}1.09\times10^{-6}],
\]
which directly supports the coarser endpoint \(0.99567109\), hence
\[
\eta\ge0.00432891,\qquad
4-\frac{8\eta}{9}\le3.99615208.
\]
The sharper decimal \(0.9956710815089548\) is stored in the binary64 `upper` field. As emphasized for the earlier profile in the supplied Step-11 review, such convenience fields should be tied to a sufficiently precise serialized Arb endpoint if all displayed digits are to form part of the computer-assisted theorem. This precision issue does not affect the strict sub-four conclusion.

### Uniformity over all marked lifts

The needed statement is stronger than convergence at one marked lift:
\[
g_m|_{K_{m,j}}
=\pi_m^*g_{\beta_m}|_{K_0}
\quad\text{for every lift }j,
\qquad
\|g_{\beta_m}-g_{\mathrm{CH}}\|_{C^2(K_0)}
=\varepsilon_m\to0.
\]
If \(g_m\) is literally the pullback of one conical KE metric on the fixed pair, this gives the same \(\varepsilon_m\) on all \(d_m\) lifts. Local convergence on varying compactifications, without this pullback identity, would not alone control the maximum over a growing number of lifts.

The fixed set \(K_0\) must contain the radius-\(R_{128}\) ball together with the entire interpolation buffer and have compact closure in \(X^\circ\). The preliminary principal congruence cover should be selected for this enlarged radius.

Finally, the degree \(d_m\), the pair \((\bar X,D)\), and \(L^2\) in the topology formulas must all be measured relative to the post-preliminary cover. If \(d_m\) is instead measured from the original quotient, the marked ball has \(d_m/d_0\) lifts, where \(d_0\) is the preliminary degree. This changes only a fixed density factor and still supplies \(O(A_m)\) sites, but the literal statement “\(d_m\) disjoint lifts” requires the relabeling.

## 8. Scientific interpretation

The verified result is an upper construction law for the selected surgery proportions and separated handle geometry:
\[
\limsup\frac{\alpha(M_m)}{h_m}
\le4-\frac{8\eta}{9}(1-r),\qquad 0\le r<1.
\]
It does not identify the best first coefficient, exclude cheaper mixed cells or unrestricted global metrics, or provide matching asymptotics.

At \(r=1\), the cell fraction \(k_m/Q_m\) tends to zero and this particular saving vanishes algebraically. Moreover, \(\Delta_m/Q_m\to1\) does not by itself ensure \(Q_m\ge\Delta_m\) at every large index, which is needed for \(k_m\ge0\). The calculation therefore gives neither a transition result nor a value of \(\alpha/h\) at \(r=1\).

Subject to the explicit \(x_0=.03\) geometric profile record and the full-precision Arb serialization, the radius, normalization, interpolation estimates, complete-cell expansion, handle accounting, rounding law, and coefficient formula are mutually consistent.