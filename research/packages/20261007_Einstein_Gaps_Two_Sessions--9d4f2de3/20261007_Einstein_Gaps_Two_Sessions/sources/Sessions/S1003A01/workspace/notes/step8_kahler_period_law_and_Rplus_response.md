# Step 8 — Kähler period law, signed blow-up cells, and the first-order response \(1-\tfrac{t}{\pi}R^+(\hat\zeta,\hat\zeta)\)

Session S1003A01, Step 8, Agent2, Execute. Conventions: \(d\sigma_i=2\sigma_j\wedge\sigma_k\), \(\int_{S^3}\sigma_{123}=2\pi^2\); \(P=\int|\operatorname{Ric}^\circ|^2\) (tensor norm), \(J_\lambda=\int|\operatorname{Ric}-\lambda g|^2=P+\tfrac14\int(s-4\lambda)^2\); a *cell* is a metric on the blow-up of a ball that coincides with an Einstein background \(\operatorname{Ric}=\lambda g\) on a collar; its cost is the integral over the cell (the background contributes zero). In peer/cell coordinates the complex-space-form collar is \(K=x+\kappa x^2\) with \(\lambda=-6\kappa\) (\(\kappa=1\): complex hyperbolic, \(\kappa=-1\): Fubini–Study), the bolt sits at \(x=x_0\), and the exceptional area is \(t=\pi x_0\).

## 1. The Kähler period law (no symmetry assumed)

**Theorem 1.** Let \((C,J,\omega)\) be a Kähler cell: the one-point complex blow-up of a ball in a Kähler–Einstein surface with \(\operatorname{Ric}=\lambda g\), with \(\omega\) equal to the background on a collar. Let \(t=\int_E\omega\) and \(L=\int_C(s-4\lambda)^2\). Then
\[
\boxed{P=2(2\pi-\lambda t)^2+\tfrac14L,\qquad J_\lambda=2(2\pi-\lambda t)^2+\tfrac12L.}
\]
*Proof.* \(\psi=\rho-\lambda\omega\) is closed, of type (1,1), and vanishes on the collar, so it defines a compactly supported class. Relative to the background, \([\rho]\) changes by \(-2\pi\,\mathrm{PD}(E)\) and \([\omega]\) by \(-t\,\mathrm{PD}(E)\); with \(E^2=-1\), \(\int\psi\wedge\psi=-(2\pi-\lambda t)^2\). Since \(\psi^+=\tfrac14(s-4\lambda)\omega\) and \(\psi^-=\rho_0\), \(\int|\rho_0|^2=(2\pi-\lambda t)^2+L/8\) in form norms, and \(|\operatorname{Ric}^\circ|^2=2|\rho_0|^2\). \(\square\)
This is the signed version of I54 (3.2) (\(\lambda=-1\)).

**Corollaries.** (a) Every Kähler cell has \(P>2(2\pi-\lambda t)^2\) unless \(\lambda t=2\pi\): equality forces \(s\equiv4\lambda\), so \(\psi\) is a compactly supported closed anti-self-dual, hence harmonic, form; unique continuation from the collar gives \(\psi=0\), contradicting the nonzero period. The bound is not attained. (b) For \(\lambda<0\) all Kähler cells cost more than \(8\pi^2\) (inherited). (c) For \(\lambda>0\) the topological term is \(8\pi^2(1-\lambda t/2\pi)^2<8\pi^2\): Kähler blow-up cells in positive Kähler–Einstein backgrounds are cheaper than the flat charge \(8\pi^2\) whenever \(L=o(t)\). In cell coordinates the topological term is \(8\pi^2(1+3\kappa x_0)^2\).
(d) Global form: for a Kähler metric on a compact surface, \(P=\tfrac14\int s^2-8\pi^2c_1^2\ge8\pi^2[(c_1\cdot\omega)^2/\omega^2-c_1^2]\) (Hodge index/Cauchy–Schwarz). On \(\mathbb{CP}^2\#\overline{\mathbb{CP}}^2\) with \([\omega]=H-\varepsilon E\) this is \(8\pi^2(1-3\varepsilon)^2/(1-\varepsilon^2)\); its localization at small \(\varepsilon=x_0\) is exactly the cell term \((1+3\kappa x_0)^2\), \(\kappa=-1\). The cell constant \(8\pi^2\) is the local Hodge-index defect of one exceptional class.

## 2. U(2) Kähler cells: exact identity and exact infimum

For \(g=dx^2/(4K)+x(\sigma_1^2+\sigma_2^2)+K\sigma_3^2\) (Kähler for every \(K\); ordinary bolt \(K(x_0)=0,\ K'(x_0)=1\)), `scripts/kahler_period_cell.py` derives from the Cartan-verified spin formulas:
\[
s=\frac{4(2-(xK)'')}{x},\qquad
\frac{P}{8\pi^2}=(1+3\kappa x_0)^2+\frac12\int_{x_0}^{X}\frac{u''^2}{x}\,dx,\qquad
\frac{J}{8\pi^2}=(1+3\kappa x_0)^2+\int_{x_0}^{X}\frac{u''^2}{x}\,dx,
\]
with \(u=xK-x^2-\kappa x^3\). The density identity is exact: \(P\)-density \(-\tfrac12u''^2/x=B'(x)\), \(B=-(K+xK'-3\kappa x^2)(K+xK'-3\kappa x^2-4x)/x^2\), \(B(\text{collar})-B(\text{bolt})=(1+3\kappa x_0)^2\); only \(C^1\) matching enters. Burns (\(K=x-x_0\), flat collar at infinity) has \(P\)-density \(2x_0^2/x^3\), total \(8\pi^2\).

The constraints are \(\int u''=x_0+3\kappa x_0^2\), \(\int xu''=2\kappa x_0^3\). Weighted Cauchy–Schwarz gives the **exact infimum over U(2) Kähler cells with collar radius \(X\)**:
\[
\inf\frac{P}{8\pi^2}=(1+3\kappa x_0)^2+\tfrac12m^TG^{-1}m,\qquad G_{ij}=\int_{x_0}^Xx^{1+i+j}dx,
\]
approached by Calabi-extremal profiles \(u''=x(A+Bx)\) (scalar curvature affine in the moment coordinate). The extremal profile has a scalar-curvature jump at \(X\); smooth cells approach but do not attain the infimum. Series: \(m^TG^{-1}m=18x_0^2(1+6\kappa x_0)/X^2+O(x_0^4)\).

Independent check (`scripts/kahler_crosscheck_peer.py`, `data/kahler_cells/peer_crosscheck.json`): the peer coordinate-curvature code evaluated on the extremal profile agrees with the identity to \(3\times10^{-14}\) for \(P\) and \(J\) in four cases, e.g. \(x_0=.001,X=.25,\kappa=-1\): \(P=0.99415216083\). Exact infima are in `data/kahler_cells/extremal_inf.json`.

## 3. Explicit smooth countercells in a Fubini–Study collar

**Theorem 2.** There are smooth U(2)-invariant Kähler metrics on the blow-up of a ball, equal to the Fubini–Study metric (\(\operatorname{Ric}=6g\)) on a collar, with \(P<8\pi^2\) and \(J_6<8\pi^2\). Explicitly take \(\kappa=-1\) and
\[
K=x-x^2+(1-\chi)\Big(-x_0+3x_0^2-\frac{2x_0^3}{x}\Big),
\]
with \(\chi\) the standard \(C^\infty\) step from 0 at \(a\) to 1 at \(X\). For \(x<a\) this is the exact constant-scalar-curvature profile \(K=x_0(y-1)[1-x_0(y-1)(y+2)/y]\), \(y=x/x_0\), with \(K(x_0)=0,K'(x_0)=1\); for \(x\ge X\) it is Fubini–Study. With \((x_0,a,X)=(0.01,0.1,0.5)\): \(P/8\pi^2=0.949823\), \(J/8\pi^2=0.958747\), \(\min K/(x-x_0)=0.5102\) (`scripts/kahler_smooth_countercell.py`, 30-digit quadrature, `data/kahler_cells/smooth_fs_countercells.json`). For fixed \(a,X\), \(P/8\pi^2=1-6x_0+O(x_0^2)\). Since the Fubini–Study collar extends to the line at infinity (\(K'(1)=-1\)), this also gives explicit Kähler metrics on \(\mathbb{CP}^2\#\overline{\mathbb{CP}}^2\) with \(\int|\operatorname{Ric}-6g|^2<8\pi^2\).

The peer's numerical sign reversal is therefore a theorem. Its source is the relative Chern-class/Einstein-constant pairing \(2\pi-\lambda t\), not an \(O(x_0)\) analytical correction.

## 4. All U(2) (conformally Kähler) cells: relative identity and second-order relaxation

Every biaxial U(2) metric \(g=dx^2/(4G)+x(\sigma_1^2+\sigma_2^2)+F\sigma_3^2\) is conformally Kähler (I54 §5). With Gauss–Bonnet and signature relative to the ball (\(\Delta\chi=1,\ \Delta\tau=-1\), identical collars):
\[
P=8\pi^2+4\Delta W^++\tfrac1{12}\Delta S,\qquad \Delta W^+=\tfrac1{24}\big(S_K-S_K^{\rm bulk}\big)\ \text{for } G=w^2K,
\]
with \(K\) the Kähler representative. For \(K\) of constant scalar curvature, the conformal Yamabe-type quotient \((\int6|dw|^2+s_Kw^2)^2/\int w^4\) is stationary at \(w=1\). Hence conformal relaxation away from Kähler gains only at second order. Numerically (`scripts/u2_general_cell.py`, Fubini–Study, \(X=.25\)), the general U(2) infimum lies below the Kähler infimum by \(6\times10^{-5}\approx60x_0^2\) at \(x_0=.001\) and by \(4.1\times10^{-4}\approx46x_0^2\) at \(x_0=.003\). The first-order term is unchanged.

## 5. Real space-form backgrounds: universal scalar response

\(H^4\) and \(S^4\) with \(\operatorname{Ric}=-6kg\) are \(F=x,\ G=x+2kx^2\) (verified Einstein symbolically in `u2_general_cell.py verify`). Write such a background as \(w^2g_{\rm flat}\), \(w=2/(1+cy)\), \(c=\lambda/3\). Insert a flat-collar Kähler cell \(K=y-y_0(1-\chi)\) with \(G=w^2K\). Since \(dV_K=\pi^2y\,dy\) does not depend on \(K\), \(s_GdV_G=(-6w\Delta_Kw+s_Kw^2)dV_K\). Integrating by parts, the cutoff-dependent term is \(\int y(1-\chi)(2ww''-4w'^2)\), and it vanishes identically for the space-form factor. Hence
\[
\Delta\!\int s_G\,dV_G=-4\pi t_G+O(t_G^2),\qquad t_G=\pi y_0w(y_0)^2,
\]
which is exactly the Kähler topological value (`scripts/spaceform_scalar_response.py`, symbolic). Also \(S_K=O(t^2)\) (Burns is anti-self-dual), \(\Delta V=O(t^2)\), and \(\int(s_G-4\lambda)^2=O(t^2\log t^{-1})\). Thus \(\Delta S=-32\pi\lambda t_G+o(t)\) and
\[
\frac{P}{8\pi^2}\le1-\frac{\lambda}{3}x_0+o(x_0)\qquad\text{in every orientation (isotropy).}
\]
Numerical infima of the general U(2) class (`data/u2_general/`, degree 10, \(X=.25\)) at \(x_0=3\times10^{-5}\) have slopes \((P/8\pi^2-1)/x_0=+2.0048\) (\(H^4\), prediction \(+2\)) and \(-1.9977\) (\(S^4\), prediction \(-2\)), against \(+6.0003\) and \(-5.9981\) for the complex space forms (prediction \(\pm6\)). The slopes converge as \(x_0\downarrow0\): \(H^4\) gives 2.0158, 2.0475, 2.4340, 3.2484 at \(x_0=10^{-4},3\cdot10^{-4},3\cdot10^{-3},10^{-2}\).

## 6. The first-order response law

For a background metric with curvature \(\mathrm{Rm}_p\) at the blow-up point, a Burns cell of area \(t=\pi a^2\) is oriented by its asymptotic Kähler form \(\hat\zeta\in\Lambda^+_p\), \(|\hat\zeta|=1\). The rescaled background is flat plus \(a^2\mathrm{Rm}_p\). The first-order response is therefore a linear functional \(\mathcal L(\mathrm{Rm}_p)\), invariant under the stabilizer \(U(2)_{\hat\zeta}=(U(1)_+\times SU(2)_-)/\pm1\). Since \(SU(2)_-\) acts irreducibly on \(\Lambda^-\), \(\Lambda^+\otimes\Lambda^-\) (traceless Ricci) and \(\mathrm{Sym}^2_0\Lambda^-\) (\(W^-\)) contain no invariants. The invariants are spanned by \(s\) and \(W^+(\hat\zeta,\hat\zeta)\). The two exact computations fix both coefficients:

* Kähler–Einstein, aligned: \(s=4\lambda\), \(W^+(\hat\omega,\hat\omega)=2\lambda/3\), slope \(-\lambda\) (Theorem 1);
* real space form: \(W^+=0\), slope \(-\lambda/3=-s/12\) (§5).

Therefore
\[
\boxed{\frac{P_{\rm cell}}{8\pi^2}=1-\frac t\pi\Big(W^+(\hat\zeta,\hat\zeta)+\frac s{12}\Big)+o(t)=1-\frac t\pi R^+(\hat\zeta,\hat\zeta)+o(t).}
\]
A third, independent datum confirms it. For the perpendicular orientation in a Kähler–Einstein background, \(R^+(\hat\zeta_\perp,\hat\zeta_\perp)=-s/12+s/12=0\), and the CH perpendicular cells indeed have no linear term (Steps 6–7, peer Step 8). Scope: Theorem 1 gives the exact topological term for all aligned Kähler cells. §5 gives an upper construction in all orientations of space forms. The law for the cell *infimum* in a general background still assumes that the infimum's first-order term is the linear response of the glued Burns tail. Numerically, relaxations enter only at \(O(t^2)\) in all four backgrounds; this has not been proved.

## 7. Consequences for the Einstein-gap programme

1. **The \(8\pi^2\) blow-up charge is a flat-background value.** In a background it is shifted by \(-8\pi tR^+(\hat\zeta,\hat\zeta)\). A cell is cheaper than \(8\pi^2\) to first order exactly when the oriented self-dual curvature operator has a positive eigenvalue at the insertion point.
2. **The balanced complex-hyperbolic family is critical.** For negative Kähler–Einstein metrics, \(\operatorname{spec}R^+=\{s/4,0,0\}\le0\), with a two-dimensional kernel \(\omega^\perp\). No orientation gains at first order, and the kernel is precisely the perpendicular slot. The coefficient-four question therefore sits at a degenerate point of the first-order law, and only the second-order term can decide it. This explains structurally why the perpendicular branch has no linear term and why its observed margin is \(O(x_0^2)\).
3. **Real hyperbolic backgrounds are strictly first-order rigid.** There \(R^+=(s/12)\mathrm{Id}<0\), so every orientation pays \(+2x_0\) (in \(\operatorname{Ric}=-6g\) units). Surgery families over real-hyperbolic pieces have a first-order cell cost strictly above \(8\pi^2\).
4. **For general negative backgrounds**, first-order saving requires \(w^+_{\max}>|s|/12\). The background is a free variable in the global problem, but an Einstein metric agreeing with complex hyperbolic space on a collar is complex hyperbolic (unique continuation). Creating \(R^+>0\) near a cell therefore costs \(\int|\operatorname{Ric}^\circ|^2\sim\delta^2\) against a gain \(\sim x_0\delta\), a net effect of order \(x_0^2\). This is the same order as the perpendicular margin. The second-order problem consists of the perpendicular cell together with its optimal background response (the Green operator of the linearized Einstein operator on CH with the collar condition). It is monotone in the collar radius \(X\), because a collar-\(X\) cell is admissible for every \(X'>X\). The X-scan of the perpendicular cell (`scripts/perp_collar_scan.py`, `data/perp_collar/`) tests exactly this channel.

## 8. Files

`scripts/kahler_period_cell.py`, `kahler_cell_infimum.py`, `kahler_crosscheck_peer.py`, `kahler_smooth_countercell.py`, `spaceform_scalar_response.py`, `u2_general_cell.py`, `u2_general_sweep.sh`, `perp_collar_scan.py`; data `data/kahler_cells/`, `data/u2_general/`, `data/perp_collar/`.
