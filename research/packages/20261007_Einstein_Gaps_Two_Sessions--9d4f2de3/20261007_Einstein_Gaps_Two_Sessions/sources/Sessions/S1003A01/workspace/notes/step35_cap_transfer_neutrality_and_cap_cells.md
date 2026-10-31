# Step 35 — Ramification caps: exact chiral curvature, quadratic environment neutrality of the cell infimum, the analytic and arithmetic cap transfer, and the admissible cap-cell problem

Conventions: \(\operatorname{Ric}=-g\) (so \(s=-4\)) unless stated; \(D(g)=\int|\operatorname{Ric}+g|^2\) is the
closed-family defect entering \(\mathcal E=(4D-T^2/V)/(4V+D-2T)\) (Step 32); \(B=\int|W^-|^2\),
\(B_\Delta=8\pi^2\Delta/3\), \(t=h(1-6\theta)\). Cap model (Steps 33–34):
\[
g_C=u(dX^2+dY^2)+\frac{du^2}{q(u)}+q(u)\,(d\Psi+X\,dY)^2,\qquad q(u)=\tfrac23(u^2-u^{-1}),\ u\ge1 .
\]

## 0. The separated theorem, with its correct reach

Step 34 proved, for surgery in \(U\), a topology-preserving modification in a disjoint \(N\), exact KE matching
annuli, metricwise actual-field scalar supply, \(0\le t\le 1/3\), \(B_U^0=o(Q)\), \(\Delta/A\to0\):
\[
\mathcal N(g)\ \ge\ -16B_U^0-48tB_N^0+\tfrac{1-3t}{3}\bigl(S(g_1)-S_0\bigr)+4(1-3t)P_N+(1+t)L_s(g),
\qquad \mathcal E(g)\ge 4h(1-6\theta)-o(h).
\]
What this proves is the floor \(4(1-6\theta)\) for \(\mathcal E/h\) in the separated class. At \(\theta=0\) it meets the
upper coefficient \(4\); for \(0<\theta<1/6\) it lies far below the construction \(4(1-\eta\theta)\). It does **not**
prove \(\mathcal E(g)\ge\mathcal E(g_1)-o(h)\), and therefore does not exclude a first-order \(r\)-dependent
improvement by separated modifications. The exact obstruction is visible in the decomposition
\[
\mathcal N(g)=\mathcal N_0(g_1)+\bigl[4(1-3t)P_N+48t\,\delta B_N\bigr]+(1+t)L_s(g),
\qquad \mathcal N_0(g_1)=\tfrac{1-3t}{3}(S(g_1)-S_0)+16(B(g_1)-B_\Delta),
\]
which uses only \(P_N=\delta S_N/12+4\delta B_N\). A separated modification can lower the numerator only if
\(48t|\delta B_N|>4(1-3t)P_N\), i.e. it must strip anti-self-dual energy at Ricci cost \(P_N<12t|\delta B_N|/(1-3t)\),
which tends to zero with \(h\). A local retention inequality \(B_N\ge B_N^0-C_NP_N\) with \(C_N\) uniform over sites
would close this (no gain whenever \(t\le 1/(3+12C_N)\)); it is not proved. By the relative identity it is
equivalent to a relative volume bound \(\delta V_N\le(3/4+3C_N)P_N\) at \(s=-4\). This is recorded as the precise open
local statement of the separated class, not as an established exclusion.

## 1. Exact chiral curvature of the cap (computed)

`scripts/step34_cap_weyl_operator.py` (bug fixed: integer zero had no `.subs`) →
`data/step34/cap_weyl_operator.json`. Orthonormal coframe \(e^0=d\tau/\sqrt\Theta,\ e^1=\sqrt\tau dx,\ e^2=\sqrt\tau dy,\
e^3=\sqrt\Theta(d\psi+x\,dy)\), orientation \(e^{0123}\), \(\omega=e^{03}+e^{12}\in\Lambda^+\). Exact output, with
\(\Theta=\tfrac23\tau^2-c/\tau\):
\[
\operatorname{Ric}=-g,\quad
W^+=\operatorname{diag}\!\left(-\tfrac23,\tfrac13,\tfrac13\right),\quad
W^-=\frac{c}{\tau^3}\operatorname{diag}(2,-1,-1),
\]
in the bases \(\{(e^{03}\pm e^{12}),(e^{01}\pm e^{23}),(e^{02}\mp e^{13})\}/\sqrt2\). Hence \(|W^-|^2=6c^2/\tau^6=8/(3u^6)\)
(agreeing with Step 33) and, at the divisor \(u=1\),
\[
W^-=\tfrac23\operatorname{diag}(2,-1,-1),\qquad R^-=W^-+\tfrac{s}{12}=\operatorname{diag}(1,-1,-1),\qquad R^+=\operatorname{diag}(-1,0,0).
\]
Consequences. (i) \(W^+\) and \(s\) are pointwise identical to CH, and \(\nabla W^+=0\) since \(\nabla\omega=0\); the cap
differs from CH **only** through \(W^-\). (ii) \(W^-\) is type D with simple positive eigenvector
\(\bar\omega=e^{03}-e^{12}\) (normal area minus divisor area); by Derdziński the cap is conformally Kähler for the
reversed complex structure with factor \(|W^-|^{2/3}\propto u^{-2}\), i.e. it is ambi-Kähler. (iii) The anti-self-dual
curvature operator has a **positive** eigenvalue \(+1\) at \(D'\), where CH has \(R^-=-\tfrac13\mathrm{Id}\). (iv) Both the
normal plane \(e^{03}\) and the divisor plane \(e^{12}\) have sectional curvature \((R^+_{11}+R^-_{11})/2=0\) at \(D'\); mixed
planes have \(-\tfrac12\).

Scale. Distance from \(D'\) is \(d(u)=\int_1^u dv/\sqrt{q(v)}\):
\(d=0.447,0.994,1.388,1.904,2.536\) at \(u=1.1,1.5,2,3,5\); the reservoir fraction inside is
\(0.317,0.802,0.9375,0.988,0.9984\). On the certified \(x_0=.03,X=128\) cell
(`data/step29/local_AK_flux_certified_x003_X128.json`), the raw action beyond physical radius
\(r=\sqrt6\operatorname{arsinh}\sqrt x\) is \(0.119,\,0.0040,\,0.00033\) at \(r=0.76,2.16,3.78\). The cell's action core and the
cap reservoir therefore live on the **same** \(O(1)\) scale (not a small-cell or small-background regime); a cap cell
is a genuinely nonlinear object.

## 2. The blow-up chiral ledger in any Einstein environment

**Step-36 correction.** The formulas in this section are exact, but the exclusion inferred from them below is not. For one blow-up,
\[
\delta S=12P+480\pi^2-48b.
\]
Thus net \(W^-\)-depletion is accompanied by a large scalar-square contribution, but a bound such as \(P\le8\pi^2\) does not by itself force the previously stated inequality \(\delta S>576\pi^2\): \(\delta S\) is the change in \(\int s^2\), not the nonnegative residual \(\int(s+4)^2\), and volume/scalar-moment compensation is still possible. Treat the ledger as a payment identity, not as an exclusion of cap interaction.

For a modification of a region with fixed outer germ which adds \(k\) blow-ups and \(\ell\) handles, relative Euler
and signature give, with \(a=\delta\!\int|W^+|^2,\ b=\delta\!\int|W^-|^2\),
\[
b=a+12\pi^2k,\qquad P=8\pi^2(k+4\ell)+4a+\frac{\delta S}{12}.
\]
(Check: Burns in flat space, \(a=\delta S=0\), gives \(b=12\pi^2\), \(P=8\pi^2\).) When a particular cell has \(|a|\ll12\pi^2\), as the certified CH cell does, the identity says that this cell adds about \(12\pi^2\) of anti-self-dual energy relative to its own background. This fact about that cell is not a general consequence of being near the \(P\)-tariff, because \(\delta S\) can compensate a large negative \(a\). Net \(W^-\) depletion by a blow-up cell (\(b<0\)) forces \(a<-12\pi^2\), while the exact rearrangement is \(\delta S=12P+480\pi^2-48b\). This records a large scalar-square payment but, because \(\delta S\) is relative and includes scalar-moment and volume exchange, it does not exclude compensation or determine the cap-cell cost. The cap can enter through finite-amplitude geometry, changing the attainable coupled \(W^+\), scalar, volume, and \(W^-\) channels. The ledger preserves that payment rather than deciding its sign.

## 3. Buffered Einstein-environment transfer (correction to the former Theorem N)

**Step-36 correction.** The construction below does not belong to the stated target class: it equals \(g_2\) only on a smaller outer collar, whereas \(j_{g_2}(R)\) prescribes \(g_2\) on the entire annulus \(A\). Therefore the same-class conclusion \(|j_{g_1}(R)-j_{g_2}(R)|\le C\varepsilon^2\) and the claimed exclusion of first-order adapted core responses are withdrawn. What the cutoff proves is a useful buffered comparison: after adding transition space, or after shrinking the prescribed target collar, a given competitor transfers with \(O(\varepsilon^2)\) defect. Moving the transition inward while preserving the whole same annulus needs further collar space or control depending on the competitor.

**Setting of the former statement.** Let \(B_R\) be a ball with annulus \(A=B_R\setminus B_{R-1}\). For an Einstein metric \(g_b\) (\(\operatorname{Ric}=-g_b\))
on a neighbourhood of \(\bar B_R\), let \(j_{g_b}(R)=\inf D(g)\) over smooth metrics \(g\) on
\(B_R\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\) (fixed marking) with \(g=g_b\) on \(A\). Let \(g_1,g_2\) be two such
Einstein metrics with \(\|g_1-g_2\|_{C^2(A,g_2)}\le\varepsilon\le\varepsilon_0\).

**Statement.** \(|j_{g_1}(R)-j_{g_2}(R)|\le C\varepsilon^2\), with \(C\) depending only on \(R\), a cutoff, and \(C^2\) bounds of
\(g_2\) on \(A\); it is uniform over all competitors.

**Proof.** Given a competitor \(g\) for \(g_1\), define \(G=g\) on \(B_{R-1}\), \(G=g_2+\chi(g_1-g_2)\) on \(A\) with
\(\chi=1\) near the inner and \(0\) near the outer boundary, and \(G=g_2\) outside. \(G\) is smooth and positive. Since
\(g=g_1\) is Einstein on \(A\), \(D(g)=\int_{B_{R-1}}|\operatorname{Ric}(g)+g|^2\). On \(A\), with \(k=g_1-g_2\),
\(\operatorname{Ric}(G)+G=\mathcal L_{g_2}[\chi k]+O(|k|^2_{C^2})\), \(\mathcal L=D(\operatorname{Ric}+g)\); and
\(\mathcal L_{g_2}[k]=O(|k|_{C^2}^2)\) because both metrics are Einstein, so
\(\mathcal L_{g_2}[\chi k]=\chi\mathcal L_{g_2}[k]+O(|\nabla\chi||k|_{C^1}+|\nabla^2\chi||k|)=O(\varepsilon)\). Hence
\(D(G)\le D(g)+C\varepsilon^2\). Exchange the roles. \(\square\)

**Valid consequence after correction.** If a construction supplies a fixed buffer in which the prescribed collar may be shrunk, the displayed interpolation gives an \(O(\varepsilon^2)\) added defect for that competitor. This remains useful for transferring a known exact-model cell into a nearby closed Einstein background, because the marked ball construction already includes a buffer. It does not establish flatness of the same exact-collar infimum, and does not constrain a core adapted to the nearby environment when no such buffer is part of the comparison class.

## 4. Theorem T (analytic cap transfer on fixed normalized slabs)

**Inputs (Biquard–Guenancia \cite{biquard2022degenerating}, §4).** On the fixed holomorphic disc-bundle neighbourhood
\(U\) of a cusp divisor, the model \(\omega_\beta\) is the exact Calabi-ansatz KE cone metric (its potential solves
\((i\partial\bar\partial\psi_\beta)^2=e^{\psi_\beta}\Omega\wedge\bar\Omega\)), the actual conic KE metric \(\hat\omega_\beta\)
satisfies \(\operatorname{Ric}=-\hat\omega_\beta\), and Lemma 4.4 gives \((1-\varepsilon_\beta)\omega_\beta\le\hat\omega_\beta
\le(1+\varepsilon_\beta)\omega_\beta\) on \(U^*\) with \(\varepsilon_\beta\to0\); they note \(dd^cF_\beta=\hat\omega_\beta-\omega_\beta\) for
\(F_\beta=\log(\hat\omega_\beta^2/\omega_\beta^2)\). The §4.3 ramified congruence covers \(\bar\pi_m\) have ramification
\(v_{m,\lambda}=1/\beta_{m,\lambda}\) along \(D\), so \(\omega_m=\bar\pi_m^*\hat\omega_{\beta_m}\) is smooth KE on \(\bar X_m\) and
\(\bar\pi_m^*\omega_{\beta_m}\) is the smooth Calabi cap \(g_C\) (Step 34 normalization) on \(\bar\pi_m^{-1}(U)\).

**Lemma C (local KE comparison).** Let \(\omega_0,\omega_1\) be Kähler on a holomorphic ball \(B_{2\rho}\) with
\(\operatorname{Ric}=-\omega_i\), \(\omega_0\) with \(C^{k+3}\) bounds \(\Lambda\) in the chart, and
\((1-\varepsilon)\omega_0\le\omega_1\le(1+\varepsilon)\omega_0\), \(\varepsilon\le1/2\). Then
\(\|\omega_1-\omega_0\|_{C^{k,\alpha}(B_\rho)}\le C(k,\rho,\Lambda)\,\varepsilon\).

*Proof.* \(F=\log(\omega_1^2/\omega_0^2)\) satisfies \(|F|\le3\varepsilon\), \(dd^cF=\omega_1-\omega_0\), \(|dd^cF|_{\omega_0}\le2\varepsilon\),
and \((\omega_0+dd^cF)^2=e^F\omega_0^2\). The complex Hessian of \(F\) is bounded and the equation is concave and uniformly
elliptic; the interior complex Evans–Krylov estimate (bounded complex Hessian suffices; e.g. Tosatti–Wang–Weinkove–Yang,
citation to be registered) gives \(\|F\|_{C^{2,\alpha}(B_{3\rho/2})}\le C\). In dimension two
\((\omega_0+\beta)^2/\omega_0^2=1+\operatorname{tr}\beta+\det\beta\), so
\(\Delta_{\omega_0}F-F=(e^F-1-F)-\det_{\omega_0}(dd^cF)=:N\) with \(\|N\|_{C^\alpha}\le C\varepsilon\). Schauder gives
\(\|F\|_{C^{2,\alpha}(B_{5\rho/4})}\le C\varepsilon\); differentiating the equation and bootstrapping gives
\(\|F\|_{C^{k+2,\alpha}(B_\rho)}\le C_k\varepsilon\). \(\square\)

**Theorem T.** For every \(L\ge1\), \(k\ge0\) there is \(C(k,L)\) such that on every lifted slab
\(\Sigma_{L}=\{1\le u\le L\}\subset\bar\pi_m^{-1}(U)\),
\[
\sup_{\Sigma_L}\bigl|\nabla^j_{g_C}(g_m-g_C)\bigr|_{g_C}\le C(k,L)\,\varepsilon_{\beta_m}\qquad(j\le k).
\]
*Proof.* Pull back the Lemma 4.4 inequality (pullback by the local branched cover preserves it on the complement of the
divisor; both lifted metrics are smooth, so it extends across \(D_m\)). For \(\beta\) small, \(\{u\le L+1\}\) corresponds to
\(\beta t\le-c(L)<0\) and lies in \(U\). Apply Lemma C on holomorphic balls of fixed \(g_C\)-size in the horizontal
universal cover of \(\{u\le L+1\}\): the universal pointed model is homogeneous along \(D'\), smooth up to \(u=1\), and has
uniform holomorphic charts, independent of \(m\) and of the horizontal lattice. Estimates are local, so they descend. \(\square\)

**Corollary (concentration).** Uniform \(C^2\) convergence on slabs and the exact model fraction give
\(\sum_c\int_{\Sigma_{L,c}}|W^-(g_m)|^2=(1-L^{-4})B_\Delta(1+O(\varepsilon_{\beta_m}))\); since the total is exactly
\(B_\Delta\) for any KE metric, the complement carries at most \((L^{-4}+O(\varepsilon_{\beta_m}))B_\Delta\). If \(\Delta/Q\) grows,
choose \(L\) with \(\Delta L^{-4}=o(Q)\).

The derivative upgrade needs only that both metrics are KE with the same constant and that BG's comparison is ratio-one
in \(C^0\); it does not need their remark on global derivative control of the degenerating family.

## 5. Proposition P (packing via the Heisenberg lattice) — arithmetic part, with its checks

For a cusp component \(D_c\) of \(\bar X_m\), the normalized horizontal metric on \(D_c\) is flat of area \(2\pi e_c\),
\(e_c=-D_c^2\). A normalized cap ball of radius \(\rho\) about \(p\in D_c\) embeds when the normalized horizontal systole
exceeds \(2\rho\) (central elements are the \(\Psi\)-rotations, which fix \(D_c\)). If the horizontal lattice is similar to a
fixed lattice up to bounded index (shape-bounded), then \(\mathrm{sys}^2_{\rm norm}\ge c_0\,e_c\).

For principal congruence of level \(\mathfrak a=p^nO_K\), \(p\) inert, in a Picard group: the horizontal projection of the
cusp lattice lies between \(\mathfrak a\mathfrak b_1\Lambda_0\) and \(\mathfrak a\mathfrak b_2^{-1}\Lambda_0\) for fixed
\(\mathfrak b_i\), so it is shape-bounded; horizontal covolume grows by \(N(\mathfrak a)=p^{2n}\) and the central period by
\(\asymp\vartheta_{\mathfrak a}=p^n\), so \(e_c\asymp p^{n}\). Cross-check with Džambić \cite{dambi2014invariants},
\((T\cdot T)=-h_K\eta_K\vartheta_{\mathfrak a}^{-2}[\Gamma_K:\Gamma_K(\mathfrak a)]\asymp p^{6n}\): it gives
\(\#\text{cusps}\asymp p^{5n}\), matching \([\Gamma_K:\Gamma_K(\mathfrak a)]/[\Gamma_P:\Gamma_P(\mathfrak a)]\asymp p^{8n}/p^{3n}\)
(the parabolic image is the 3-dimensional unipotent radical; the Levi part of \(\Gamma_P\) is finite). Hence
\(\mathrm{sys}_{\rm norm}\asymp p^{n/2}\to\infty\), each component holds \(\asymp e_c/\rho^2\) disjoint embedded normalized cap
balls, and the tower holds \(\asymp\Delta\) of them. Status: consistent derivation from the Heisenberg structure and an
independent count; the lattice inclusions and the central index should still be written out explicitly from Hill's or
Holzapfel's description before the proposition is quoted as a theorem.

With Theorem T, the buffered transfer estimate above, and the still-to-be-completed Proposition P, any fixed cap cell with an exact Calabi collar and an additional marked buffer can be transferred to the positive-\(r\) towers with total error \(o(Q)\), as in the CH-cell insertion. This statement uses the buffer and is not the withdrawn same-class comparison.

## 6. The admissible cap-cell problem

**Local symmetry at the divisor.** In the symmetric gauge \(\Psi'=\Psi+XY/2\),
\(g_C=u(dX^2+dY^2)+du^2/q+q(d\Psi'+\tfrac12(X\,dY-Y\,dX))^2\), so the isotropy of \(p=(0,0,u{=}1)\) in the universal model
contains \(T^2=U(1)_{\rm rot}\times U(1)_{\Psi'}\), with weights \((1,0)\) on the divisor plane and \((0,1)\) on the normal
plane: locally the cap is a toric KE corner. \(T^2\) contains \(U(1)_+\) (weights \((1,1)\), rotating \(\omega^\perp\subset\Lambda^+\)) and
\(U(1)_-\) (weights \((1,-1)\), trivial on \(\Lambda^+\), fixing \(\bar\omega\in\Lambda^-\)).

**Two genuinely different trial classes.**
1. *Toric (cohomogeneity two).* The \(T^2\)-equivariant blow-up of the corner. Its exceptional sphere is \(T^2\)-invariant,
   so at its poles the tangent plane is a weight plane and its \(\Lambda^+\) part is parallel to \(\omega\): this is the
   **aligned** branch. Kähler competitors are expected to obey the inherited period law \(P=2(2\pi+t)^2+L/4>8\pi^2\) (derived for
   Kähler cells with Einstein collar and \(\lambda=-1\); its use with the Calabi collar should be rechecked), and
   A02's closed Kähler tariff \(P>8\pi^2k\) points the same way, so a successful toric cell must be non-Kähler; it tests whether the positive \(R^-\) at \(D'\) changes the aligned first-order
   cost through finite-amplitude or higher-order coupling. The positive cap eigenvalue lies in \(R^-\), whereas the inherited glued-Burns first variation uses \(R^+(\hat\zeta,\hat\zeta)\). At the aligned cap direction \(R^+=-1\), so the linear term is unfavorable; the Fubini–Study analogy does not apply at first order.
2. *Perpendicular (cohomogeneity three, \(U(1)_-\)-invariant).* The certified mechanism needs the exceptional
   \(\Lambda^+\) direction \(\perp\omega\); the only part of the cap isotropy compatible with it is \(U(1)_-\). A cap
   perpendicular cell is therefore a \(U(1)_-\)-invariant metric on \(B_\rho(p)\#\overline{\mathbb{CP}}^2\) equal to \(g_C\) on the
   collar. A direct transplant of the certified perpendicular core, including its complete interpolation to the Calabi collar, is the first realizable probe; no same-class neutrality theorem rules it out.

**Decision quantity.** For either class, compute the full \(D=\int|\operatorname{Ric}+g|^2\), with \(\delta V\), \(\delta\!\int s\), and the
ledger \(a,b\) of §2 as checks (\(b-a=12\pi^2k\) exactly). Compare with the certified CH value
\(8\pi^2\times0.995670030355131\). A first, inexpensive, decisive object is a finite block in the toric class: a
\(T^2\)-invariant blow-up family with regular corner/edge expansions, exact cap outside \(B_\rho\), a few response
amplitudes, and direct evaluation of \(D\); no stationary base or continuum Jacobi inverse is assumed.

## 7. State

Established in Step 35 and retained after Step-36 corrections: exact cap \(W^\pm\) (§1); the chiral ledger formulas (§2); a buffered cutoff transfer, not same-class infimum flatness; Lemma C and Theorem T with proof modulo the cited complex Evans–Krylov estimate; concentration corollary. Derived with explicit
checks still to write: Proposition P. Open: local retention for the separated class (§0); the toric and \(U(1)_-\) cap cells
(§6); the unrestricted blow-up tariff, mixed cells, non-diagonal collapse, density-free O10, Dehn-twist attainment.
