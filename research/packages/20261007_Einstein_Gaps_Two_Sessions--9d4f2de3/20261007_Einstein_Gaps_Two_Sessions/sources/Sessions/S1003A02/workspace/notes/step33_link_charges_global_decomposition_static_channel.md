# Step 33 — Chiral link charges without symmetry, the link-separated global decomposition, and the static charge channel for non-round opening

Conventions. \(P(g;\Omega)=\int_\Omega|\operatorname{Ric}^\circ|^2d\mu\), \(\widehat P=P/8\pi^2\). Orientation is the blow-up orientation (the exceptional sphere has square \(-1\); the CH Kähler block is \(W^+\)). For a compact oriented \(\Omega\) with boundary, the Gauss–Bonnet–Chern and Atiyah–Patodi–Singer formulas are written
\[
\chi(\Omega)=\int_\Omega e+\mathcal E(\partial\Omega),\qquad
\int_\Omega L=\tau(\Omega)+\mathcal H(\partial\Omega),
\]
\(e=\frac1{8\pi^2}(|W|^2-\frac12|\operatorname{Ric}^\circ|^2+\frac{s^2}{24})\), \(L=\frac1{12\pi^2}(|W^+|^2-|W^-|^2)\). \(\mathcal E\) is Chern's boundary transgression (intrinsic curvature and second fundamental form of \(\partial\Omega\)); \(\mathcal H=\eta(\partial\Omega)+\int_{\partial\Omega}T_{p_1}\) is the APS eta invariant of the odd signature operator plus the local transgression to a product collar. Both depend only on the metric near \(\partial\Omega\); \(\mathcal E\) and \(\mathcal H\) of a boundary component change sign when its orientation is reversed. With several boundary components, each is oriented as the boundary of \(\Omega\).

## 1. Theorem G (chiral characteristic identity)

For every compact \(\Omega\subset(M^4,g)\) with smooth boundary,
\[
\widehat P(\Omega)=\frac1{2\pi^2}\int_\Omega|W^\pm|^2+\frac1{96\pi^2}\int_\Omega s^2-\bigl(2\chi(\Omega)\pm3\tau(\Omega)\bigr)+\mathcal Q_\pm(\partial\Omega),
\qquad \mathcal Q_\pm=2\mathcal E\mp3\mathcal H .
\]
*Proof.* \(2e\pm3L=\frac1{4\pi^2}(2|W^\pm|^2-\frac12|\operatorname{Ric}^\circ|^2+\frac{s^2}{24})\); integrate and insert the two boundary formulas. \(\square\)

Consequently, for every \(\Omega\),
\[
\widehat P(\Omega)\ \ge\ \max_\pm\bigl[\mathcal Q_\pm(\partial\Omega)-(2\chi\pm3\tau)(\Omega)\bigr],\tag{G}
\]
and on an annulus \(C\) with inner and outer links, \(\widehat P(C)\ge\max_\pm[\mathcal Q_\pm(\text{out})-\mathcal Q_\pm(\text{in})]\) (the inner link enters with reversed orientation). In diagonal Bianchi-IX symmetry \(\mathfrak b=2\mathcal E\), \(\mathfrak s=3\mathcal H\), \(\mathfrak b_\pm=\mathcal Q_\pm\): Theorem X, Lemma Q″ and Lemma V are the symmetric reductions of (G).

### Model link charges \((\mathcal Q_+,\mathcal Q_-)\)

Each value is the charge of the link as outer boundary of the region it encloses.

1. **Small geodesic sphere / round link in an almost flat region:** \((2,2)\). (Ball: \(\chi=1,\tau=0\), interior integrals \(\to0\).)
2. **Flat-conical or ALE spherical-space-form end \(S^3/\Gamma\):** for an exact flat-conical collar, or in the limit along an ALE end, \(\mathcal E\to1/|\Gamma|\), \(\mathcal H\to\eta_\Gamma\), where the eta sign is fixed by the outgoing-link orientation and \(\int L=\tau+\mathcal H\). Thus \(\mathcal Q_\pm\to2/|\Gamma|\mp3\eta_\Gamma\). The intrinsic round metric alone does not determine this charge if the radial first jet is arbitrary. Applied to a smooth complete scalar-flat ALE bubble \(N\), (G) gives \(\widehat P(N)\ge 2/|\Gamma|-2\chi+3|\tau+\eta_\Gamma|\), exactly Lemma Q of Step 20; its near-Euclidean \(\Gamma=1\) neck form is Lemma Q′. Regions containing an actual orbifold singularity require the orbifold characteristic corrections.
3. **Thin tube around an embedded surface \(\Sigma\) with self-intersection \(n\neq0\):** for a fixed smooth ambient metric, as the tube radius tends to zero, \(\int e,\int L\to0\) on the disk bundle \(D(n)\), \(\chi(D)=\chi(\Sigma)\), \(\tau(D)=\operatorname{sgn}n\). Hence \(\mathcal E\to\chi(\Sigma)\), \(\mathcal H\to-\operatorname{sgn}n\), and
\[
\mathcal Q_\pm(\text{tube})=2\chi(\Sigma)\pm3\operatorname{sgn}n .
\]
For the \((-1)\)-sphere this is \((4-3,\,4+3)=(1,7)\), the diagonal bolt charge, now derived without symmetry and without any regularity of the bolt beyond smoothness.
4. **Taub–NUT-chirality Hopf-adiabatic Berger link with controlled collar:** \((-2,2)\). Reversing the four-dimensional orientation exchanges the two charges, giving \((2,-2)\). Self-contained derivation: for the Taub–NUT metric (a ball, \(\chi=1,\tau=0\), Ricci-flat, \(W^-=0\) in this orientation), the outer link at radius \(R\to\infty\) is an adiabatically collapsing Berger sphere with bounded base geometry and bounded second fundamental form, so \(\mathcal E\to0\): every term of Chern's boundary integrand contains a principal curvature times link curvature or a cubic in principal curvatures; here the fibre principal curvature is \(O(R^{-2})\), the base ones \(O(R^{-1})\), the link sectional curvatures \(O(R^{-2})\) (base–base) and \(O(R^{-4})\) (fibre–base), and the link area is \(O(R^2)\), so \(\mathcal E=O(R^{-2})\). The index structure of Chern's integrand is essential here: its terms pair a principal curvature with the sectional curvature of the complementary plane, or multiply all three principal curvatures. Then Gauss–Bonnet gives \(\frac1{8\pi^2}\int|W^+|^2=1\), hence \(\int L=2/3\) and \(\mathcal H\to2/3\). So \(\mathcal Q_+=0-2=-2\), \(\mathcal Q_-=0+2=2\). This derivation uses the Ricci-flat half-conformally-flat Taub–NUT filling. It is not a formula for an arbitrary half-conformally-flat filling: in general the scalar and trace-free Ricci terms alter the relation between \(\mathcal H\) and \(\mathcal E\).
   The diagonal formula (`scripts/berger_eta_charge.py`, `data/berger_eta_charge.json`) gives for \(h_\lambda=\lambda^2\sigma_f^2+\sigma_g^2+\sigma_h^2\) with radial jets \(a_f'=\lambda V\), \(a_g'=a_h'=U\):
   \[
   \mathfrak s=2(1-\lambda^2)^2+\lambda^2(U-V)^2 ,
   \]
   exact (residual 0). The first term is intrinsic and equals \(3\eta_{\rm APS}(\lambda)\) with \(\eta_{\rm APS}=\frac23(1-\lambda^2)^2\) (blow-up orientation, lift anchored by \(\eta(1)=0\)); its \(\lambda\to0\) value \(2/3\) agrees with the Taub–NUT derivation above, which uses no eta formula at all. (The script encodes the eta formula as an input; the Taub–NUT argument is the independent check.) The second term is the collar transgression \(\int T_{p_1}\): it vanishes for a product or conical collar and is the precise reason an intrinsic eta cannot price uncontrolled radial shear.
5. **CH geodesic sphere of radius \(\tau\):** \((2-9\sinh^4\tau,\ 2-3\sinh^4\tau)\); from (G) on the CH ball, since \(\frac1{96\pi^2}\int_{B_\tau}s^2=3\sinh^4\tau\) (\(\operatorname{Vol}B_\tau=\frac{\pi^2}2\sinh^4\tau\)) and \(\frac1{2\pi^2}\int_{B_\tau}|W^+|^2=6\sinh^4\tau\).

The lower pricing rule "bubble cost is at least outgoing charge minus incoming charge" is therefore a theorem about links, not about symmetry (and applies in this pure form to a product-topology annulus): an exceptional class enclosed by a round link costs \(2-1=1\); after Hopf-adiabatic collapse, reopening to a round link costs \(2-(-2)=4\); a CH sphere is a link whose \(\mathcal Q_+\) deficit \(9\sinh^4\tau\) equals the Weyl-plus-scalar energy deleted from the CH ball.

### Volume-renormalized charges (scalar-normalized class)

If \(s\equiv-24\) on \(\Omega\), \(\frac1{96\pi^2}\int_\Omega s^2=3\widehat V(\Omega)\) with \(\widehat V=2\operatorname{Vol}/\pi^2\) (CH ball: \(\widehat V=\sinh^4\tau\)). Put \(\mathfrak B_\pm=\mathcal Q_\pm+3\widehat V\). Then \(\widehat P(\Omega)\ge\mathfrak B_\pm(\partial\Omega)-(2\chi\pm3\tau)\), and pathwise on a radial family \(\widehat P\ge\int\max\{0,\mathfrak B_+',\mathfrak B_-'\}\). On CH, \(\mathfrak B_-\) is constant and \(\mathfrak B_+\) strictly decreasing. For an \(O(-1)\) cell ending in an exact CH collar at \(\tau\), the \(\mathfrak B_-\) bound is the relative-signature form \(-5+3(\widehat V_{\rm cell}-\widehat V_{\rm CH})+\dots\) of Theorem C. For a non-round opening from a collapsed section (charges \((-2,2)\), volume \(\widehat V_c\)) to a CH sphere at \(\tau\):
\[
\widehat P\ \ge\ 4-9\sinh^4\tau+3\Delta\widehat V,\qquad \widehat P\ \ge\ 3(\Delta\widehat V-\sinh^4\tau),
\]
so a cell below \(p_*\) must satisfy \(\Delta\widehat V<\sinh^4\tau+p_*/3\) and \(9\sinh^4\tau>4-p_*+3\Delta\widehat V\). These are volume budgets for the opening; with Riccati control of the mean curvature they do not by themselves exclude opening at \(\tau\gtrsim0.8\).

## 2. The link-separated global decomposition

Let \(M=X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\) and let \(D\subset M\) be a compact region with connected boundary link such that \(D\cong(\#k_D\overline{\mathbb{CP}}^2\#\ell_D(S^1\times S^3))\setminus B^4\). Then \((2\chi+3\tau)(D)=2-k_D-4\ell_D\), and (G) gives
\[
P(g)\ \ge\ P(g;D)\ \ge\ 8\pi^2\Bigl[k_D+4\ell_D-\bigl(2-\mathcal Q_+(\partial D)\bigr)\Bigr].\tag{G1}
\]
The constant \(k+4\ell\) of Theorem C is the round-link value. Disjoint regions add.

**Corollary G2 (disjoint round separation forces the bubble price).** If \(D_1,\dots,D_m\) are pairwise disjoint, carry \(k_i\) exceptional classes and \(\ell_i\) handles, and \(\mathcal Q_+(\partial D_i)\ge2-\varepsilon_i\), then \(P(g)\ge8\pi^2\sum_i(k_i+4\ell_i-\varepsilon_i)\). Since the charge of an outer \(S^3\) collar converging after rescaling in \(C^2\) to the flat-conical germ on the bounded side is \(2-o(1)\), a sequence with pairwise disjoint regions satisfying \(\sum_i k_i=k\) and \(\sum_i\varepsilon_i=o(1)\) has \(\liminf P\ge8\pi^2k\). A single region enclosing all \(k\) classes gives the same conclusion. Merely giving each class some possibly nested or intersecting link does not allow the local energies to be added.

**Corollary G3 (subunit sequences admit no Euclidean-round \(S^3\) separation of the exceptional subtree).** Let \(X\) be a compact ball quotient whose injectivity radius exceeds the outer radius of the certified cell (available on suitable finite covers). Inserting the certified perpendicular cell gives a metric on \(X\#\overline{\mathbb{CP}}^2\) with \(\widehat P\le p_*=0.995848\). By (G1), every metric with \(\widehat P<1-\varepsilon\) and every standard negative-definite blow-up region \(D\) with \(b_2^-(D)=1,b_2^+(D)=b_1(D)=0\) satisfy
\[
\mathcal Q_+(\partial D)\le1+\widehat P(D)\le1+\widehat P(g)<2-\varepsilon.
\]
Thus such a region cannot have an outer \(S^3\) collar converging to the Euclidean flat-conical germ, even if the exceptional subtree contains further inner bubbles. More generally, any separating link with \(\mathcal Q_+>1+\widehat P(g)\) is excluded. This does **not** exclude orbifold \(S^3/\Gamma\) necks, Taub–NUT-chirality Hopf collapse with \(\mathcal Q_+\approx-2\), curved or sheared links below the charge threshold, pure bulk bubbling, or regions also carrying positive intersection form.

For several classes, if pairwise disjoint standard negative-definite regions carrying a total of \(K\) classes all satisfy \(\mathcal Q_+\ge2-\varepsilon\), then \(K\le\lfloor\widehat P/(1-\varepsilon)\rfloor\). With a separated-cell upper bound of order \(kp_*\), this guarantees only that at least \(k-\lfloor kp_* /(1-\varepsilon)\rfloor\) classes fail such disjoint round separation; it does not keep every class unseparated. In real-hyperbolic bulk, by contrast, the conditional Theorem H gives \(\inf P=8\pi^2k\) with Burns sequences realizing round-link concentration.

**What the decomposition leaves.** (G1) prices cells by their links but the bulk \(B=M\setminus\cup D_i\) satisfies the complementary identity
\[
\widehat P(B)=\frac1{2\pi^2}\int_B|W^+|^2+\frac1{96\pi^2}\int_Bs^2-(2\chi+3\tau)(B)-\sum_i\mathcal Q_+(\partial D_i),
\]
whose lower bound requires field information on \(B\). The global LeBrun/Seiberg–Witten estimates are integrated over all of \(M\). Their localization to \(B\) produces two link terms of the same type: the flux \(\oint_{\partial B}\partial_\nu|\psi|^2\) from \(\int\Delta|\psi|^2\) in the Weitzenböck identity, and the Chern–Simons term \(\mathrm{CS}(A|_{\partial B})\) in \(\frac1{4\pi^2}\int_B(|F_A^+|^2-|F_A^-|^2)=c_1^2[B]+\mathrm{CS}\). A matching bulk-plus-cells theorem therefore needs **link regularity**: a selection of links \(\partial D_i\) on which (a) the Euler and signature transgressions converge (in particular the second fundamental form, including the \(\lambda^2(U-V)^2\)-type collar shear, is controlled), (b) the SW flux and Chern–Simons terms converge, and (c) along collapsing links, the small nonzero eigenvalues of the odd signature operator contribute the Dai adiabatic correction in a controlled way. (For noncollapsing links, \(C^2\) collar convergence—or an equivalent Sobolev hypothesis controlling the boundary connection, curvature, and second fundamental form—gives convergence of these terms; \(C^1\) collar convergence alone is insufficient for the Chern–Simons/transgression integrals.) Under link regularity the problem splits exactly into cell infima priced by \(\mathcal Q_\pm\) jumps and a bulk-with-links SW problem. Supplying (a)–(c) from near-minimality and critical \(L^2\) control, without pointwise Ricci bounds, is the precise remaining selection problem of the global passage.

## 3. Static test of Lemma V for non-round opening (Lemma Z)

In scale-free first-jet coordinates \(X=(u_f,u_g,u_h,\beta,q)\), \(u_i=a_i'-\gamma_i\),
\[
\mathfrak b_+=2-|u|^2-u_fu_gu_h\quad(\text{independent of shape}),\qquad
\mathfrak b_-=|w|^2-w_fw_gw_h-2,\ w=u+2\gamma(\beta,q).
\]
Collapsed (Taub–NUT/ALF) state: \(u\to(1,1,-2)\), \(h\)-slot collapsed. CH orbit at \(\tau\): \(u=(3\sinh^2\tau,0,0)\), \(\beta=\log\cosh\tau\), \(q=0\).

**Lemma Z.** (i) \(\mathfrak b_+\) alone gives no static obstruction: for \(A>5/2\) the path \((1,1,-2)\to(A,1,-2)\to(A,s,-2s)_{s:1\to0}\) has \(|u|^2+u_fu_gu_h=(A-1)^2+4\), then \(A^2+s^2(5-2A)\), both nondecreasing, so \(\mathfrak b_+\) is nonincreasing; the shape is free because \(\mathfrak b_+\) does not depend on it. The endpoint is the CH orbit with \(3\sinh^2\tau=A\) (\(\tau>0.816\)). (ii) On the jet family \(u=(A,A,-2)\) (base expansion rate \(A\)), \(\mathfrak b_+\equiv-2\) exactly, and at collapsed shape with ratio \(\lambda\), \(\mathfrak b_-=2(1+\lambda^2(A^2-4)+4A\lambda^3+6\lambda^4)\to2\): the base expansion rate is charge-neutral in the collapsed limit. (Exact checks of (i),(ii): `scripts/lemmaZ_exact.py`, `data/lemmaZ_exact.json`.) (iii) Jointly, numerical minimization of the polygonal \(\Lambda=\int\max(0,d\mathfrak b_+,d\mathfrak b_-)\) (`scripts/static_charge_path.py`, `data/static_charge/path_*.json`, step bound 0.25, 120 nodes, refined 40× on the linear interpolation) finds paths from the collapsed state (\(\lambda=0.02\)) to CH orbits at \(\tau\approx0.82\)–\(0.84\) with refined \(\Lambda=0.050\) and \(0.021\), \(|u|\le2.7\), maximal rises above running minima \(\le0.008\). With the endpoint forced to \(\tau\in[0.70,0.71]\) and \(|u|\le3\) (200 nodes) the minimizer has \(\Lambda=0.824\), essentially the unavoidable endpoint increment \(\mathfrak b_+(\tau)-\mathfrak b_+(\text{start})=0.816\): the static value is the endpoint bound \(\max\{0,4-9\sinh^4\tau\}\) up to discretization, nothing more. (Two further random/detour starts at 200/320 nodes did not converge and are not evidence.)

So Lemma V cannot prove the non-round input by any static argument: the sublevel geometry contains a monotone channel. The channel is explicit (data file): the state stays triaxial with \(a_f\) the largest slot throughout (\(a_f/a_g\) from 1 to 1.38, never round), \(u_f\) rises to \(\approx2.6\) while \(\mathfrak b_-\) stays at \(\approx2\), then \(q\) descends from \(3.9\) to \(0\) (slot \(h\) opens to match \(g\)) while both charges decrease. This is the same triaxial swap the dynamic optimizer performs (Step 32 profile). What the static test ignores is kinematics: shape velocity is not free but determined by the jets (\(q'=y_g-y_h\), \(\beta'\) similarly) and jets change only through the controlled second-order flow. The cost of the swap therefore lives in the Weyl/scalar densities \(\omega_\pm\) along kinematically admissible paths, consistent with the \(D\)-dominated split (4.30 of 6.48). A lower theorem for (N) must be a Hamilton–Jacobi subsolution \(V=\mathfrak b_++\phi(X)\) with \(\phi\) shape/jet dependent and \(\nabla\phi\cdot f\le\omega_+\) on the kinematic band, or the peer Green identity \(M=-\int WDK\) with kinematics; charges alone are exhausted.

## 4. Status

Proved: Theorem G; model charges 1–5 with the collar, chirality, and smooth-tube scopes stated above; (G1); the corrected finite disjoint-region G2; and the one-blow-up charge bound (G3), which excludes Euclidean-round \(S^3\) separation of the standard exceptional subtree but not general bubble trees. Proved exact: Lemma Z(i),(ii). Numerical: Lemma Z(iii). Open: link-regularity selection; the matching bulk estimate using global field information and same-metric cell accounting; the kinematic lower bound for (N); large-bolt Theorem L and face no-return. Step 34 gives the independent verification, the symmetry-free constraint calculus, and the exact obstruction to a \(\mathfrak b_++\phi(q,\eta)\) certificate.
