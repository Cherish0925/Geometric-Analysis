# Step 33 — The two-parameter surgery law over ramified Kähler–Einstein towers, the sharpened certified cell, and anti-self-dual retention

Conventions as in the corpus (`paper/sections/linear_coercivity.tex`, `variational_geometry.tex`):
\(\mathcal E(g)=\inf_{\lambda\ne0}\int|\mathrm{Ric}-\lambda g|^2/(\lambda^2V)\), \(\alpha(M)=\inf_{\mathscr G(M)}\mathcal E\),
\(R=\int|\mathrm{Ric}|^2\), \(P=\int|\mathrm{Ric}^\circ|^2\), \(S=\int s^2\), \(B=\int|W^-|^2\), \(L_s=\int(s-\bar s)^2\).
Scripts/data: `scripts/step33_fraction_window.py` → `data/step33/fraction_window.json`;
`scripts/perp_rigorous_enclosure.py` (Step-33 exact-endpoint output) → `data/step33/rigorous_x00.03_X128_d20_{J,P,S}_exact.json`.

## 0. Families

Fix the post-preliminary arithmetic base and Galois ramified tower of Steps 31–32
(`notes/step31_ramified_KE_transfer_and_interface_simplification.md`): smooth compact
Kähler–Einstein surfaces \(\bar X_m\), \(\mathrm{Ric}=-g\), \(A_m=c_1^2\), Chern defect
\(\Delta_m=3\chi(\bar X_m)-A_m>0\), \(d_m\asymp A_m\) disjoint lifts of one fixed marked ball of
radius \(\sqrt6\,\mathrm{arsinh}\sqrt{128}=7.6451262946\ldots\) plus buffer, uniformly \(C^2\)
\(\varepsilon_m\)-close to CH. Put
\[
M_m=\bar X_m\#k_m\overline{\mathbf{CP}}^2\#\ell_m(S^1\times S^3),\quad
Q_m=k_m+4\ell_m,\quad h_m=\frac{Q_m}{A_m},\quad
\theta_m=\frac{k_m}{Q_m},\quad r_m=\frac{\Delta_m}{Q_m},
\]
and the **topological chiral slope**
\[
\boxed{\sigma_m=4r_m+18\theta_m=\frac{4\Delta_m+18k_m}{Q_m}.}
\]
No balancing is imposed. Any integers are allowed; all statements below are written in
the exact values \(\theta_m,r_m,\sigma_m\), so rounding never enters. (To realize prescribed limits
\(\theta,r\) choose \(\widehat Q_m\), \(k_m=\lceil\theta\widehat Q_m\rceil\),
\(\ell_m=\lfloor(1-\theta)\widehat Q_m/4\rfloor\).)

Exact characteristic numbers (SymPy, `fraction_window.json`):
\(T_+=2\chi+3\tau=A-Q=A(1-h)\) exactly, and
\[
\frac{3T_-}{A}=\frac{3(2\chi-3\tau)}{A}=1+(\sigma-3)h .
\]
Hence \(U_{\rm top}=\min\{3-3h,\,1+(\sigma-3)h\}=1+(\sigma-3)h\) exactly when \(\sigma h\le2\), in
particular for all large \(m\) when \(Q_m=o(A_m)\) and \(\sigma_m\) stays bounded.

## 1. All-metric lower theory depends only on the slope \(\sigma\)

Actual-field input (LeBrun polarized connected sums, verified in Step 32): for every metric,
\(p\ge A\), selected determinant class \(a=c-\sum\pm E_i\) with \(a^2=A-k\ge A-Q=T_+\); the
handle summands are absorbed by holonomy insertions; \(0<h\le1/3\). Two independent inequalities
then hold **for every smooth metric** on \(M_m\):

**(L1) Linear window** (thm:linear-window, with \(\mathcal E\ge\mathcal J\)). With \(L_h=1+(1+c_0)h\),
\[
\mathcal E(g)\ \ge\ \frac{(L_h-U_{\rm top})_+}{L_h+U_{\rm top}/18}
=\frac{(4+c_0-\sigma)_+\,h}{L_h+U_{\rm top}/18}.
\]

**(L2) \(\Delta\)-corrected scalar–Weyl identity.** The signature formula with the background
\(\tau(\bar X)=(A-2\Delta)/9\) gives \(\int|W^+|^2=B+12\pi^2\tau(M)\) and
\(P=4\int|W^+|^2+S/12-8\pi^2T_+\). Writing \(\theta_0=(4\ell-5k)/A=h(1-6\theta)\),
\(S_0=32\pi^2A\) and
\[
B_\Delta:=\tfrac{8\pi^2}{3}\Delta ,
\]
one has the exact identity (verified symbolically)
\[
P=\frac{S-S_0}{12}+4(B-B_\Delta)+8\pi^2A\,\theta_0 .
\tag{1.1}
\]
Equivalently, with \(\theta_\Delta=\theta_0-\tfrac{4\Delta}{3A}=h\,\frac{3-\sigma}{3}\),
\(P=(S-S_0)/12+4B+8\pi^2A\theta_\Delta\), and the corpus proof of
prop:vg-handle-identity applies verbatim:
\[
\mathcal E-\frac{4\theta_\Delta}{1+\theta_\Delta}
=\frac{(1-3\theta_\Delta)(S-S_0)/3+16B+(1+\theta_\Delta)L_s}{(1+\theta_\Delta)R}\ \ge 0
\qquad(0\le\theta_\Delta\le\tfrac13),
\]
using only the monopole scalar budget \(S\ge32\pi^2p\ge S_0\).

**Theorem A (slope law for the lower order).** On \(M_m\), for all large \(m\),
\[
\frac{\alpha(M_m)}{h_m}\ \ge\ \max\Bigl\{\tfrac43(3-\sigma_m)_+\,\frac{1}{1+\theta_\Delta},\;
\frac{(4+c_0-\sigma_m)_+}{L_h+U_{\rm top}/18}\Bigr\},
\qquad
\liminf\frac{\alpha}{h}\ge \max\Bigl\{\tfrac43(3-\sigma)_+,\ \tfrac{18}{19}(4+c_0-\sigma)_+\Bigr\}.
\]
The first branch is completely explicit; the second has the nonexplicit universal \(c_0>0\).
Consistency with the exact pure-handle theorem (\(\sigma=0\), value \(4\)) forces \(c_0\le 2/9\).
Both lower mechanisms see the surgery and the background **only through \(\sigma\)**.

## 2. Upper law depends only on the blow-up fraction \(\theta\)

**Theorem B.** Insert \(k_m\) copies of the certified exact-collar cell into distinct lifted marked
balls and \(\ell_m\) shrinking standard handles in separated regions. With
\(D=\int|\mathrm{Ric}+g|^2\), \(T=\int s+4V\),
\(\mathcal E=(4D-T^2/V)/(4V+D-2T)\), \(V=2\pi^2A+O(Q)\), \(T=O(Q)\),
\(D=kJ_1+32\pi^2\ell+O(Q\varepsilon_m^2)+o(Q)\), hence
\[
\limsup\frac{\alpha(M_m)}{h_m}\le 4(1-\eta\theta),\qquad
\eta\ \ge\ \eta_{\rm cert}=0.004329969644869361\ldots\ (\text{§4}).
\]
The background Chern defect does not enter: the KE background contributes \(D=0\) exactly and its
\(W^-\) energy \(B_\Delta\) costs nothing in \(D\).

## 3. Consequences

* **Coexistence region.** Every realizable limit pair with \(0<\theta\le1\) and \(\sigma<4+c_0\) has
  a positive all-metric linear gap and a strictly sub-four construction. The explicit
  (\(c_0\)-free) subregion is \(\sigma<3\), where
  \[
  \tfrac43(3-\sigma)\ \le\ \liminf\alpha/h\ \le\ \limsup\alpha/h\ \le\ 4-4\eta\theta .
  \]
  Examples: \(r=0,\theta=1/9\): \([4/3,\;4-0.0019244]\); \(r=1/2,\theta=1/36\): \([2/3,\;4-0.00048]\).
* **Beyond \(r=1\).** For \(1\le r<1+c_0/4\), every \(0<\theta<(4+c_0-4r)/18\) is admissible;
  the vanishing of the *balanced* saving \(8\eta(1-r)/9\) at \(r=1\) is an artifact of the
  balanced slice \(\sigma=4\), not an existence barrier.
* **Realizability of every \(r\).** In the inert-prime-power Picard tower (Džambić,
  \cite{dambi2014invariants}), \(A_n\asymp p^{8n}\), \(\Delta_n=-T_n^2\asymp p^{6n}\). For \(r\in(0,\infty)\) take
  \(Q_n\sim\Delta_n/r\): then \(Q_n/A_n\asymp p^{-2n}\to0\). For \(r=0\) take
  \(Q_n=\lceil p^{n}\Delta_n\rceil\), still \(o(A_n)\). So the whole half-line of \(r\) is
  geometrically supplied with linearly many CH-close sites.
* **Where the lower theory stops.** For \(\sigma\ge4+c_0\) (in particular every \(\theta\) once
  \(r\ge1+c_0/4\)), neither L1 nor L2 gives anything, and Einstein metrics on \(M_m\) are not
  excluded by these actual-field Chern–Weil arguments (an Einstein metric needs \(L_h\le U_{\rm top}\),
  i.e. \(\sigma\ge4+c_0\)). The extreme \(Q=o(\Delta)\) contains the unsurgered background, where
  \(\alpha=0\) is attained by the KE metric; the topological window must therefore close somewhere,
  but the present upper constructions remain at \(4h(1-\eta\theta)\) uniformly in \(r\).

## 4. Anti-self-dual retention: the exact meaning of the \(r\)-loss

Identity (1.1) shows exactly what the \(r\)-dependence of the lower theory measures. For the KE
background, \(|W^+|^2=s^2/24\) and the signature formula give
\(\int_{\bar X}|W^-|^2=B_\Delta=8\pi^2\Delta/3\) exactly (checked in the script). Rewriting with the
\(\Delta\)-free parameter \(\theta_0=h(1-6\theta)\):
\[
\mathcal E-\frac{4\theta_0}{1+\theta_0}
=\frac{(1-3\theta_0)(S-S_0)/3+16(B-B_\Delta)+(1+\theta_0)L_s}{(1+\theta_0)R}.
\tag{4.1}
\]
Consequently:

* **Retention ⇒ \(r\)-free lower bound.** On any class of metrics with
  \(B\ge B_\Delta-o(Q)\), one has \(\mathcal E\ge 4h(1-6\theta)+o(h)\), independent of \(r\).
  All present constructions (KE exterior untouched, cells and handles adding their own \(W^-\))
  lie in this class.
* **Beating the \(r\)-free bound requires depletion.** A metric family with
  \(\mathcal E/h<4(1-6\theta)\) must have \(B<B_\Delta-cQ\): it must remove a positive fraction of
  the background anti-self-dual energy at the scale of the surgery budget. Since \(|W^-|^2\ge0\)
  pointwise, the reduction must occur where \(W^-_{KE}\) lives, i.e. where the KE metric is not
  locally symmetric. In the exact cusp-closing model below, all of \(B_\Delta\) lies in unit
  neighbourhoods of the ramification curves \(D'_\lambda\).
* **Why \(r=0\) is sharp and \(r>0\) is not, in the same identity.** By the signature formula,
  \(B-B_\Delta=12\pi^2k-\delta_+\), where \(\delta_+=\tfrac{4\pi^2}{3}A-\int|W^+_g|^2\) is the
  self-dual Weyl deficit relative to the KE level. On a ball quotient \(B_\Delta=0\) and
  \(B\ge0\) caps \(\delta_+\le12\pi^2k\): self-dual depletion beyond what the exceptional cells
  supply is impossible, which is exactly why the pure-handle value \(4\) is sharp. For \(r>0\) the
  background reservoir \(B_\Delta\) permits \(\delta_+\) up to \(B_\Delta+12\pi^2k\). LeBrun's
  monopole estimate prices \(\delta_+\le (S-S_0)/12\), i.e. at rate \(4\) in the numerator of (4.1)
  against a gain of \(16\); so no presently available inequality excludes the trade.
* **Localization by relative signature.** If \(g\) agrees with \(g_{KE}\) near \(\partial N\) of a
  region \(N\), the APS boundary terms coincide and
  \(\int_N(|W^+_g|^2-|W^-_g|^2)=\int_N(|W^+_{KE}|^2-|W^-_{KE}|^2)\). Depleting \(W^-\) in a
  ramification neighbourhood therefore depletes \(W^+\) there by the same amount: it is the
  **same non-Kähler self-dual depletion mechanism that produces the certified blow-up saving**,
  now acting on the background's ramification geometry instead of on an exceptional sphere.

**Exact location of the reservoir \(B_\Delta\) (computed).** `scripts/step33_cusp_closing_Wminus.py`
(→ `data/step33/cusp_closing_Wminus.json`, full SymPy Riemann/Weyl computation) treats the exact
cusp-closing Kähler–Einstein model: the Calabi ansatz over a flat torus,
\[
g=\tau(dx^2+dy^2)+\frac{d\tau^2}{\Theta}+\Theta\,\eta^2,\quad d\eta=dx\wedge dy,\qquad
\mathrm{Ric}=-g\iff\Theta=\tfrac23\tau^2-\frac{c}{\tau}.
\]
\(c=0\) is the complex-hyperbolic cusp. For \(c>0\) the circle closes at \(\tau_0=(3c/2)^{1/3}\) with
\(\Theta'(\tau_0)=2\tau_0\); with \(\psi\)-period \(2\pi/\tau_0\) the closing is smooth, the zero
section is an elliptic curve of self-intersection \(-e\), \(e=a\tau_0/2\pi\) (\(a\) = coordinate torus area).
The output is exact:
\[
s=-4,\qquad |W^+|^2=\tfrac23,\qquad |W^-|^2=\frac{6c^2}{\tau^6},\qquad
\int_{\tau\ge\tau_0}|W^-|^2\,d\mu=\frac{8\pi^2}{3}\,e .
\]
Since \(\Delta_m=\sum_{\rm components}e_c\) (Hurwitz/adjunction, Step 31), the model reproduces
\(B_\Delta=8\pi^2\Delta/3\) **exactly and entirely inside the cusp-closing neighbourhoods**. The
reservoir sits at unit curvature scale: \(|W^-|^2=8/3\) on \(D'\) (independent of \(c\)) and
\(|W^-|^2\sim C\,e^{-2\sqrt6\,d}\) at large distance \(d\) from \(D'\). Each \(D'_c\) is a flat-ish torus
of area \(2\pi e_c\) (in these units), so a positive-\(r\) tower offers \(\asymp\Delta=rQ\)
disjoint unit-size sites where the Kähler–Einstein background has \(O(1)\) anti-self-dual curvature
and is genuinely not CH. (Whether Biquard–Guenancia's metrics are \(C^2\)-close to this model on the
whole unit neighbourhood of \(D'\), as their construction strongly suggests, should be read off
their §4 model metric; the topological identity \(B_\Delta=8\pi^2\Delta/3\) itself is exact for any KE metric.)

This turns the \(r\)-question into a concrete local problem: **the cost of a blow-up (or handle)
cell placed in the cusp-closing model near \(D'\), with \(O(1)\) background \(W^-\)**. If it is below
the CH-site cost \(8\pi^2(1-\eta)\), the upper law improves with \(r\); if retention holds there, the
\(r\)-loss of the lower theory is an artefact.

The topology dependence of the optimal coefficient is therefore equivalent to a concrete geometric
question: **can surgery-scale energy deplete the anti-self-dual Weyl energy of the ramification
neighbourhoods at a favourable exchange rate?**

**Separated depletion is unfavourable (structure, partial proof).** On the unsurgered background,
\(\mathcal E\ge0\) and (4.1) with \(\theta_0=0\) give, for every metric on \(\bar X\),
\[
S-S_0\ \ge\ 48\,(B_\Delta-B)-3L_s ,
\]
so on \(\bar X\) itself depletion costs scalar excess at rate \(48\), not the rate \(12\) of the bare
monopole estimate (KE is the global minimizer, and Einstein metrics are critical for each
\(\int|W^\pm|^2\)). Now let \(g\) on \(M_m\) coincide with \(g_{KE}\) outside (i) the surgery regions,
placed where \(g_{KE}\) is \(\varepsilon\)-close to CH, and (ii) a disjoint modification region \(N\),
with exact-KE annuli in between. Restoring \(N\) to KE gives \(g_1\); modifying only \(N\) on
\(\bar X\) gives \(g'\). Then \(S,B\) are additive, \(\int|\mathrm{Ric}+g|^2\) is additive, and
\[
\mathcal N(g)=\mathcal N(g_1)+\bigl[\mathcal N_{\bar X}(g')-L_s(g')\bigr]
-\theta_0\Delta S_N+(1+\theta_0)\bigl(L_s(g)-L_s(g_1)\bigr),
\]
where \(\mathcal N\) is the numerator of (4.1) and \(\mathcal N_{\bar X}(g')\ge0\). For \(g_1\),
\(B(g_1)\ge B_\Delta-O(\varepsilon^2Q)\) because the cells replace regions with
\(|W^-_{KE}|=O(\varepsilon)\) by regions with \(|W^-|^2\ge0\); hence
\(\mathcal E(g_1)\ge4h(1-6\theta)-o(h)\) independently of \(r\). The remaining terms are the
scalar-variance comparison \(L_s(g)\) versus \(L_s(g_1)+L_s(g')\) and the \(O(h)\cdot\Delta S_N\)
correction; controlling them (both are lower order when \(s\) stays near \(-4\)) would prove that
**depletion separated from the surgery never improves the coefficient**. The \(r\)-dependence of the
true coefficient can therefore arise only from surgery cells that *interact* with the
non-locally-symmetric part of the KE background (cells placed in, or overlapping, ramification
neighbourhoods), not from the global count \(\Delta\). In the additive regime the true coefficient is
governed by local cell costs in CH-close regions and is \(r\)-independent.

By (1.1), lowering \(B\) by \(\delta\) lowers
\(P\) by \(4\delta\) at fixed \(S\); the monopole budget only forces \(S\ge S_0\), so no current
global estimate prices this exchange. A positive answer would give constructions beating \(4(1-6\theta)h\)
for large \(r\) by cells interacting with ramification geometry; a negative answer (an ASD-retention inequality \(B\ge B_\Delta-C(P+L_s+S-S_0)-o(Q)\))
would extend the positive linear gap to every \(r\) and every \(\theta<1/6\).

**Correction (Steps 34–35).** The variance obstacle above is removed by retaining the global
\(L_s(g)\ge0\) (Step 34), which proves the floor \(\mathcal E/h\ge4(1-6\theta)-o(1)\) in the separated class. That
floor does not give \(\mathcal E(g)\ge\mathcal E(g_1)-o(h)\); hence the sentence that separated depletion
"never improves the coefficient" and the claim that the coefficient is \(r\)-independent in the additive
regime are not established. The precise remaining local statement is a retention inequality
\(B_N\ge B_N^0-C_NP_N\) (see `step35_cap_transfer_neutrality_and_cap_cells.md`, §0). The statement that a
positive-\(r\) tower offers \(\asymp\Delta\) unit cap sites is not implied by divisor area; it now rests on
Theorem T (analytic slab transfer) and Proposition P (Heisenberg systole) of the Step-35 note, the latter
still requiring an explicit lattice write-up.

## 5. Background response of the cell

* **Exact first-order neutrality.** For the fixed certified cell glued into a background
  \(g_{CH}+\kappa\) on the exact-CH collar annulus, the first variation of
  \(\int|\mathrm{Ric}+g|^2\) in \(\kappa\) is \(2\int\langle\mathrm{Ric}+g,\,D(\mathrm{Ric}+g)[\chi\kappa]\rangle=0\),
  because \(\mathrm{Ric}+g=0\) wherever \(\chi\kappa\ne0\) at zeroth order. Hence background
  effects on a fixed cell are \(O(\|\kappa\|_{C^2}^2)\), the Step-31 estimate.
* **KE rigidity of \(R^+\).** For any KE background with \(\mathrm{Ric}=-g\), \(R^+=W^++s/12\) has
  spectrum \(\{-1,0,0\}\) pointwise, identical to CH. KE environments differ from CH only through
  \(W^-\) and covariant derivatives. Heuristic supplement (not yet a proof): the cell symmetry
  \(SU(2)_L\) is the \(\mathbf C\)-linear \(SU(2)\subset U(2)\) of the CH ball, so it acts trivially on
  \(\Lambda^+\) and irreducibly on \(\Lambda^-\); even after re-optimizing an \(SU(2)_L\)-symmetric core, a
  linear coupling can only see the \(SU(2)_L\)-invariant part of the background deviation, and a
  pointwise \(W^-\in S^2_0\Lambda^-\) has none (Schur). The expected leading coupling is quadratic in
  \(W^-\); symmetry-broken cells could couple linearly, but then pay their own second-order cost.
* Consequence: within KE towers, a larger first-order saving cannot come from the local background;
  it must come from the unrestricted cell problem itself (re-optimized nonlinear cores and tails),
  from non-Kähler Einstein environments where \(R^+\) acquires a positive eigenvalue
  (the first-order response principle of Step 8), or from the global \(W^-\)-depletion of §4.

## 6. Sharpened certificate for the authoritative cell

Profile `data/perp_area/x00.03_X128_d20.json` (degree 20, \(x_0=3/100\), \(X=128\), coefficients
the exact binary doubles; bolt shift \(q_F(0)+q_G(0)=0\) imposed exactly). Arb, 128 bits,
`acb_calc_integrate`, tol \(10^{-14}\), one piece, exact dyadic endpoints printed outwardly:
\[
\frac{J_6}{8\pi^2}\in[0.995670030344086466\ldots,\ 0.995670030355130639\ldots],
\]
\[
\frac{P}{8\pi^2}\in[0.995662732753254,\ 0.995662732771115],\qquad
\frac{\int(s+24)^2/4}{8\pi^2}\in[7.29759\times10^{-6}\pm6.4\times10^{-12}],
\]
and the independent reconstruction \(P+S\) overlaps \(J\) (interval \([0.995670030336849,0.995670030362368]\)).
Pointwise checks: \(\mathrm{Ric}=-6\) at the collar to \(3\times10^{-14}\), finite bolt values.
The new ball lies inside the Step-15 ball \([0.9956689792,0.9956710815]\) (that run reported a
much coarser radius). Hence
\[
\eta_{\rm cert}\ge0.004329969644869361,\qquad 4-\tfrac{8}{9}\eta_{\rm cert}\le 3.996151138093450 .
\]
The balanced (\(r=0\)) coefficient is now \(\limsup\alpha/h<3.9961512\) (after arbitrarily small
smoothing loss), superseding \(3.9961521\). The admissibility chain (positivity \(0\le S\le1\),
\(\hat F,\hat G>0\), ordinary \((-1)\) Hopf bolt with \(q_F(0)+q_G(0)=0\), weight-four anisotropy,
perpendicular topology \(D\#\overline{\mathbf{CP}}^2\), third-order CH contact, \(O(\delta^3)\) smoothing,
\(g\mapsto6g\)) is proved for every \(x_0>0\) and degree in
`Skills/.../20261004/step10_rigorous_subthreshold_cell_and_O11.md` §3–4 and therefore applies to this
exact profile; only the collar radius changes to \(7.6451\ldots\) in \(\mathrm{Ric}=-g\) units.

## 7. What this changes

The construction law and the lower law are governed by different variables: the upper bound by the
geometric blow-up fraction \(\theta\), the lower bound by the topological slope \(\sigma=4r+18\theta\).
At \(\sigma=0\) they meet (pure handles, exact value \(4\)). Along \(\theta\) the lower slope is
\(-24\) (explicit) or \(-18\cdot18/19\) while the upper slope is \(-4\eta\): the all-metric blow-up
tariff is the dominant unknown. Along \(r\) the lower bound decays with slope \(-16/3\) while the
upper is flat; by (4.1) this gap is precisely the question of anti-self-dual retention near the
ramification curves. Open: the true blow-up tariff (unrestricted cell infimum and its all-metric
counterpart), ASD retention/depletion, mixed blow-up–handle cells, density-free O10, collapse, and
fixed-manifold attainment.
