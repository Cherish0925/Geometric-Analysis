# Step 2 — the blow-up cell problem behind O11: exact reduction and the first U(2) computation

## 1. Exact reduction of the coefficient question to a W⁺/scalar functional

Conventions: Hilbert–Schmidt norms on two-forms (manuscript convention), \(S=\int s^2\), \(W_\pm=\int|W^\pm|^2\), \(P=\int|\mathrm{Ric}^\circ|^2\), \(T_+=2\chi+3\tau\). The identity \(4\pi^2T_+=S/24+2W_+-P/2\) gives, for every metric on a closed manifold,
\[
P=\frac{S}{12}+4W_+-8\pi^2T_+ .
\]
On \(M=X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\) with \(A=c_1^2(X)\), \(Q=k+4\ell\), \(T_+(M)=A-Q\). For the Kähler–Einstein metric on \(X\), \(S_{KE}=32\pi^2A\) and \(W_+^{KE}=S_{KE}/24=\tfrac43\pi^2A\). Hence the **exact** all-metric identity
\[
\boxed{P(g)-8\pi^2Q=\frac{S(g)-32\pi^2A}{12}+4\Bigl(W_+(g)-\tfrac43\pi^2A\Bigr).}
\]
LeBrun's polarized scalar estimate gives \(S(g)\ge32\pi^2A\) for every metric on the blow-ups (its supply for the handle summands must be taken from the corpus' supply statements). Thus:

* the O11 coefficient-4 lower bound \(\inf P\ge8\pi^2Q-o(Q)\) holds as soon as \(W_+(g)\ge\tfrac43\pi^2A-o(Q)\) for metrics with \(P=O(Q)\);
* conversely, any competitor with a better coefficient must lower the self-dual Weyl energy below its Kähler–Einstein value by an amount \(\gtrsim Q\) while its scalar excess stays below \(48\times\) that deficit.

Equivalently, with \(\Phi(g)=\frac1{4\pi^2}\int(s^2/24+2|W^+|^2)\), coefficient 4 is \(\inf\Phi=A-o(Q)\). LeBrun's Weyl–scalar estimate gives only \(\Phi\ge\frac23A\) (this is exactly the Einstein obstruction \(k<A/3\)); the recovery metrics give \(\Phi\to A\). So **O11 is the asymptotic, small-\(h\) form of the sharpening of LeBrun's 2/3 estimate** — the same quantity whose sharp value would decide Einstein metrics on blow-ups with \(k<A/3\). (Literature status of a sharp \(\Phi\)-bound should be confirmed by a knowledge request before any novelty statement.) This explains why separate infima cannot settle O11: the relaxation using only \(S\ge32\pi^2A\) and \(\int(s-\sqrt6|W^+|)^2\ge72\pi^2A\) has optimum \(F=S/12+4W_+=\tfrac{16}3\pi^2A<8\pi^2A\), attained at \(|W^+|/|s|=\sqrt6/48\), far from the Kähler ratio \(1/(2\sqrt6)\).

For a cell \(U\) (blown-up ball) that replaces a complex-hyperbolic ball \(B\) and agrees with it near \(\partial B\), Gauss–Bonnet and signature with identical boundary data give
\[
P(U)=8\pi^2+4\,\Delta W_++\frac{\Delta S}{12},\qquad \Delta=\int_U-\int_B .
\]
Because the bulk is Einstein, \(P(M)=\sum_{\rm cells}P(U_i)\) for sparse disjoint cells. With covers of a fixed ball quotient (injectivity radius \(\to\infty\)), any fixed cell can be planted at \(k_j\ll A_j\) sites; a single cell with \(P(U)<8\pi^2\) would give \(\limsup\alpha_j/h_j<4\) on blow-up subfamilies. So the decisive non-perturbative constructive test is \(\inf_U P(U)\) over complete cells.

## 2. Exact Kähler U(2) cells

U(2)-invariant metrics in the coordinate \(x=b^2\): \(g=\frac{dx^2}{4G}+F\sigma_3^2+x(\sigma_1^2+\sigma_2^2)\) (round unit \(S^3=\sum\sigma_i^2\)). Bolt (exceptional sphere of self-intersection −1, area \(\pi x_0\)): \(F(x_0)=G(x_0)=0\), \(F'(x_0)G'(x_0)=1\). Complex hyperbolic (Ric = −6g): \(F=G=x+x^2\); Burns: \(F=G=x-x_0\), \(P=8\pi^2\) exactly (checked). Kähler iff \(F=G=K\); then \(s=(8-4(xK)'')/x\), \(|\mathrm{Ric}^\circ|^2=4(x^2K''+2x-2K)^2/x^4\), and with \(K=x+H\), \(P=4\pi^2\int L^2x^{-3}dx\), \(L=x^2H''-2H\). The Euler–Lagrange solution is \(L=c_1x^3+c_2\), giving the exact optimum (script `kahler_cell_exact.py`)
\[
\frac{P_{\rm K\ddot ahler}}{8\pi^2}=1+6x_0+9x_0^2(1+X^{-2})+O(x_0^3)\quad(\text{gluing radius }X=\sinh^2R).
\]
The linear term coincides with the global Hodge-index bound for Kähler metrics on \(X\#k\overline{\mathbb{CP}}^2\): \(\int s^2\ge32\pi^2(c_1\cdot[\omega])^2/[\omega]^2\) gives \(P\ge8\pi^2k(1+2\varepsilon)\) with \(\varepsilon=3x_0\) in these units. Kähler cells therefore never beat \(8\pi^2\).

## 3. Non-Kähler U(2) cells (numerical; scripts `u2_curvature.py`, `u2_xcoord.py`, `u2_cell_jax_log.py`)

Parametrization: \(F=K_{\rm opt}e^{\phi p_1}\), \(G=K_{\rm opt}e^{\phi p_2}\), Chebyshev polynomials of degree 12 in \(u=\log(x/x_0)/\log(X/x_0)\), \(\phi=(1-u)^3\), bolt constraint \(p_1+p_2=0\) at \(x_0\); exact JAX gradients, L-BFGS. The identity \(P-8\pi^2=4\Delta W_++\Delta S/12\) is reproduced to \(10^{-8}\)–\(10^{-12}\) in every run, an independent check of the curvature formulas and orientation. Data: `workspace/data/u2grid/u2_cell_grid2.jsonl`; figure `workspace/figures/u2_cell_cost.png`.

| \(x_0\) | \(X\) | Kähler opt. \(P/8\pi^2\) | non-Kähler min | slope \((P/8\pi^2-1)/x_0\) | \(4\Delta W_+/8\pi^2\) | \(\Delta S/12/8\pi^2\) |
|---|---|---|---|---|---|---|
| 0.0003 | 10 | 1.0018008 | 1.0017942 | 5.981 | 0.00119 | 0.00060 |
| 0.003 | 10 | 1.01808 | 1.01763 | 5.876 | 0.0116 | 0.0060 |
| 0.03 | 10 | 1.1882 | 1.1636 | 5.45 | 0.100 | 0.063 |
| 0.1 | 10 | 1.6915 | 1.5073 | 5.07 | 0.279 | 0.229 |
| 0.3 | 50 | 3.611 | 2.453 | 4.84 | 0.650 | 0.802 |
| 1.0 | 50 | 16.06 | 6.42 | 5.42 | 1.67 | 3.74 |
| 3.0 | 50 | 103.0 | 25.6 | 8.2 | 4.5 | 20.1 |
| 10 | 50 | 1277 | 198 | 19.7 | 23.6 | 173.8 |

Results are insensitive to \(X\in\{2,10,50\}\) at fixed \(x_0\) (cells are local). Observed facts:

1. Every computed U(2) cell has \(P>8\pi^2\); the cost increases with the bolt size, and the infimum \(8\pi^2\) is approached only as \(x_0\to0\) (shrinking Burns bubble). It is not attained.
2. The first-order penalty is \(6x_0\) for non-Kähler cells as well: the non-Kähler improvement over the Kähler optimum is of second order (\(\approx0.06x_0\) at \(x_0=3\cdot10^{-4}\), \(\approx0.5x_0\) at \(x_0=0.03\)).
3. Both pieces pay separately at every tested size: \(\Delta W_+>0\) and \(\Delta S>0\); near the Burns limit they split exactly as in the Kähler case, \(4\Delta W_+\approx4x_0\), \(\Delta S/12\approx2x_0\) (units \(8\pi^2\)). The opposite energy satisfies \(W_-(U)>12\pi^2\) (the Burns value).

## 4. Interpretation and its range

Within U(2) symmetry, a blow-up cell planted in complex-hyperbolic space cannot lower the first-order Einstein-gap coefficient: the per-site cost is \(8\pi^2(1+6x_0+\dots)\) with \(\pi x_0\) the exceptional area in Ric = −6g units; scale-invariantly, \(8\pi^2\bigl(1+|\lambda|\,\mathrm{Area}(E)/\pi+\dots\bigr)\) with \(\mathrm{Ric}=\lambda g\) outside the cell. The correction is positive and linear in the exceptional area times background curvature, so near-minimizers must concentrate their blow-up bubbles at vanishing scale. This is a concrete near-extremal/degeneration statement: within this class the infimum is a bubbling limit, consistent with nonattainment of \(\alpha\).

A mechanism for the universality of the coefficient 6 beyond U(2): Burns minimizes \(4W_++S/12\) among asymptotically flat fillings of the blow-up (where it vanishes), so it is a critical point of \(P\) for decaying variations. In a scaled gluing \(g_\varepsilon\), any change of the bubble's shape enters at second order, while the order-\(\varepsilon^2\) term is a boundary pairing between the Burns \(r^{-2}\) asymptotic mode (Kähler mass \(x_0\)) and the background curvature at the site. For a complex-hyperbolic background this pairing is U(2)-invariant, so its value should be the same for non-symmetric competitors: \(P=8\pi^2(1+6x_0)+O(x_0^2\log)\). Proving this would give a rigorous first-order statement: no small-scale perturbation of a Burns bubble, symmetric or not, lowers the per-site cost.

What the computation does not cover: cells without U(2) symmetry; clusters of several blow-ups in one cell (multi-centre/toric cells, same \(Q\)); handle cells \(S^1\times S^3\) (cost \(32\pi^2\)); non-monotone \(b\) (necks inside the cell); the full balanced family, whose lower bound also uses the opposite chirality through \(U=3\min(T_+,T_-)/A\). Numerical minima are upper bounds for the U(2) infimum only within the parametrization.

## 5. Work that would decide O11 from here

* **Perturbative theorem (both sides at once).** Prove \(P(g)\ge8\pi^2(1+6x_0)-Cx_0^2\log(1/x_0)\) for all metrics \(C^{2}\)-close (in weighted norms) to a scaled Burns bubble glued into a complex-hyperbolic background, without symmetry. This upgrades "coefficient 4 in recovery neighbourhoods" to a quantitative strict per-site penalty and identifies the boundary pairing.
* **Non-perturbative cells without symmetry.** The cell problem \(\inf_U P(U)\) is a well-posed local variational problem. The natural next class is \(T^2\)-invariant (toric) cells, which contain multi-centre blow-up clusters and Gibbons–Hawking/LeBrun hyperbolic-ansatz metrics; cohomogeneity two, still computable.
* **Local W⁺ inequality.** The data suggest the stronger local statement \(\Delta W_+\ge0\) for every cell. A proof (even in U(2)) would follow from a local SW/Kähler-calibration argument and would be the cell form of the needed global inequality \(W_+\ge\frac43\pi^2A-o(Q)\).
* **Positioning.** Request literature on sharp lower bounds for \(\int(s^2/24+2|W^+|^2)\) and \(\int|W^+|^2\) on blow-ups of minimal general-type surfaces (LeBrun 1998–2004, Gursky, Sung, Kim) and on Einstein metrics on \(X\#k\overline{\mathbb{CP}}^2\) for \(k<c_1^2/3\).
