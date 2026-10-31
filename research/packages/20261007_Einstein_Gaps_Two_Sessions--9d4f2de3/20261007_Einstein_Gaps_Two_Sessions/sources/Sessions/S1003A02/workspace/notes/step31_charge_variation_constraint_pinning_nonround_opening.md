# Step 31 — Charge variation, scalar-normalized constraint pinning, non-round opening, and the large-bolt face limit

Conventions are those of Steps 25–30: diagonal Bianchi–IX metrics \(g=dt^2+\sum a_i^2\sigma_i^2\), \(y_i=a_i'/a_i\), \(W=a_fa_ga_h\), \(\widehat P=\int W|\operatorname{Ric}^\circ|^2/4\,dt\), \(|\operatorname{Ric}^\circ|^2=\tfrac34H^2+\tfrac23E^2+\tfrac12D^2\). The best certified cell value is \(p_*=0.995848\).

## 1. The charge-variation functional

The chiral identities of Theorem X hold on every annulus, hence pointwise in \(t\):
\[
\frac{d\widehat P}{dt}=\frac{d\mathfrak b_\pm}{dt}+\omega_\pm,\qquad
\omega_\pm=\frac{W}{2\pi^2}\Big(|W^\pm|^2\text{-density}\Big)+\frac{W}{96\pi^2}\Big(s^2\text{-density}\Big)\ge0 .
\]
**Lemma V.** For every diagonal annulus \(C=[a,b]\times S^3\),
\[
\widehat P(C)\ \ge\ \int_a^b\max\{0,\mathfrak b_+',\mathfrak b_-'\}\,dt\ \ge\ \max\{V^+_C(\mathfrak b_+),V^+_C(\mathfrak b_-)\},
\]
where \(V^+\) is positive variation. In particular, for an \(O(-1)\) cell with bolt charges \((\mathfrak b_+,\mathfrak b_-)=(1,7)\),
\[
\widehat P\ \ge\ \sup_t\max\{\mathfrak b_+(t)-1,\ \mathfrak b_-(t)-7\},
\qquad
\widehat P\ \ge\ \sup_{s<t}\big(\mathfrak b_\pm(t)-\mathfrak b_\pm(s)\big).
\]
*Proof.* Integrate the pointwise identity and drop \(\omega_\pm\); on any finite disjoint family of intervals the increments add. \(\square\)

The opposite charge is \(\mathfrak b_-=\sum w_i^2-w_fw_gw_h-2\), \(w_i=a_i'+\gamma_i\) (scale-free normalization \(r=1\)), with \(\mathfrak b_+=2-\sum u_i^2-u_fu_gu_h\), \(u_i=a_i'-\gamma_i\). Checks: smooth centre \(u=0,w=(2,2,2)\Rightarrow(2,2)\); bolt with \(a_h'(0)=1\), \(\gamma_h=2\): \(u=(0,0,-1)\), \(w=(0,0,3)\Rightarrow(1,7)\); CH orbit \(\mathfrak b_-=2-3\sinh^4t\) (numerically \(1.00657\) at \(t=.7\), \(-59.667\) at \(t=1.5\), exact agreement; `data/saturation_control/two_sided_bounds.json`).

**Consequences.**

1. *Round passages.* Any cell that passes an orbit with \(\mathfrak b_+\ge 1+p_*\) costs more than \(p_*\). A cheap cell stays in \(\{\mathfrak b_+<1+p_*,\ \mathfrak b_-<7+p_*\}\), and after any section \(s\) it satisfies \(\mathfrak b_\pm(t)<\mathfrak b_\pm(s)+p_*\).
2. *The raw high-shear escape is excluded by the bolt prefix alone.* The Step-30 entry state with \(\Delta\eta=-8\) has \(\mathfrak b_+=1.45194\) and \(\mathfrak b_-=8.54957\). Any trajectory from an \(O(-1)\) bolt to that state therefore costs at least \(8.54957-7=1.5496\) before the connector begins. This replaces the Step-30 reconstructed total \(\ge1.0264\) by a connector-independent bound, using only the opposite chirality.
3. *Reduction of mechanisms 1 and 3.* A cheap cell that ever reaches a collapsed section (\(\mathfrak b_+\approx-2\)) satisfies \(\mathfrak b_+<-2+p_*\approx-1.004\) afterwards. Since a CH orbit has \(\mathfrak b_+=2-9\sinh^4\tau\), it must first reach CH shape at \(\tau>0.70\). The small-bolt saturation branch and every shear bounce that collapses therefore reduce to one problem: **non-round late opening** — a path from a collapsed or sheared state to a CH orbit at \(\tau\ge0.70\) along which \(\mathfrak b_+\) stays below \(-1\).

## 2. Non-round late opening: numerical value

`scripts/saturation_optimal_control.py` now accepts `SAT_BPMAX=c`, imposing \(\mathfrak b_+\le c\) at every collocation node, with the CH opening radius free in \([0.701,4.6]\). Outputs: `data/saturation_control/eps*_ch_bpmax_*.json`.

| \(\varepsilon\) | \(N\) | cap \(c\) | cost | \(t_{\rm CH}\) |
|---|---|---|---|---|
| 1/16 | 60 | none (Step 29) | 3.888 | 2.0 |
| 1/16 | 60 | 1 | 4.035 | 2.14 |
| 1/16 | 60 | 0 | 4.810 | 2.24 |
| 1/16 | 60 | −0.5 | 5.501 | 2.26 |
| 1/16 | 60 | −1 | 6.478 (two warm starts agree to \(10^{-9}\)) | 2.28 |
| 1/16 | 80 | −1 | 6.437 | 2.39 |
| 1/16 | 60 | −1.5 | 7.890 | 2.29 |
| 1/16 | 60 | −2.5 | 11.874 | 2.53 |
| 1/4 | 60 | −1 | 5.374 | 2.62 |
| 1/32 | 80 | −1 | 6.551 | 2.30 |
| 1/64 | 80 | −1 | 6.619 | 2.22 |

All runs converged with collocation residual \(\le10^{-10}\). The non-round value increases as \(\varepsilon\to0\) and is mesh-stable. These are feasible constrained paths returned by a local optimizer (explicit upper constructions for the constrained problem), not lower bounds; they show that the cheapest paths the optimizer finds in the reduced problem of §1 have cost about six times \(p_*\).

The cost is not paid by charges. `scripts/charge_variation_bound.py` (output `data/saturation_control/charge_variation.json`) evaluates the discrete Lemma-V functional: it recovers \(3.85/3.89\) and \(3.994/3.994\) of the round-reopening paths, but only \(1.49\) of the \(c=-1\) cost \(6.48\) and \(1.54\) of the \(c=-2.5\) cost \(11.87\). The channel split of the \(c=-1\) optimum is \((H,E,D)=(0.53,1.70,4.30)\); for \(c=-2.5\) it is \((2.58,2.73,6.61)\). Non-round opening is paid mainly through \(D\), the slot channel that opens the collapsed circle into a contact direction, at large orbit volume. This is the Weyl/scalar part \(\omega_\pm\) of the cost, i.e. a pinning effect rather than a transgression effect.

## 3. Lemma N: the H channel is the Hamiltonian constraint

In compact variables \(y_i'=6-y_iS+P_i-e_i\), \(e_i=\operatorname{Ric}_{ii}+6\), \(R^{(3)}=\sum P_i\), and \(e_0=\operatorname{Ric}_{00}+6\). Put
\[
\mathcal C=\sigma_2(y)-6-\tfrac12R^{(3)}
=\kappa^2+y_fy_g+y_gy_h+y_hy_f-4\zeta\cosh q-6+4\zeta^2\sinh^2q/\kappa^2 .
\]
**Lemma N.** For every diagonal metric:
1. \(\mathcal C=G_{00}-6=\tfrac12(e_0-\sum_ie_i)\);
2. (Bianchi propagation) \(\mathcal C'=-2S\mathcal C-\sum_i(S-y_i)e_i\);
3. if \(s\equiv-24\), then \(\mathcal C=\operatorname{Ric}^\circ_{00}=-\tfrac34H\), so
\[
\widehat P=\int W\Big(\frac{\mathcal C^2}{3}+\frac{E^2}{6}+\frac{D^2}{8}\Big)dt ;
\]
4. if \(s\equiv-24\), then \(S'=18-S^2+R^{(3)}+\mathcal C\).

All four identities, the norm decomposition, and \(\mathcal C=0\) on CH are verified exactly by `scripts/scalar_normalized_constraint.py` (`data/scalar_normalized_constraint.json`, all residuals \(0\)).

By Theorem C and the weak-barrier theorem, \(P(g)-P(\hat g)=24\int|\nabla u|^2+3\int(\Delta u/u)^2\ge0\) for the scalar-\(-24\) conformal metric \(\hat g=u^2g\); the radial \(u\) preserves the diagonal class. It does **not** literally preserve an exact CH collar (\(u\to1\) only at rate \(m\in(4,2+2\sqrt3)\)), and it rescales the bolt radius to \(u(0)b\). The correct statement (Step-32 independent reading): the exact-ended diagonal infimum equals the infimum of \(P\) over diagonal scalar-\(-24\) metrics asymptotic to the marked standard CH end at rate \(>4\); conversely such a metric is truncated to an exact CH collar with vanishing added cost by Theorem T. In the scalar-normalized class (3) holds. A large-bolt statement must use the normalized bolt scale \(u(0)b\) or control \(u(0)\) separately. In that class the trace channel is not a third first-order pinning observable but a **zeroth-order pointwise penalty**: the state must lie on the Einstein constraint surface \(\mathcal C=0\) wherever \(W\) is large. The chiral density also strengthens there to \(d\widehat P/dt=\mathfrak b_\pm'+3\widehat V'+(\text{Weyl}^\pm\text{ density})\), \(\widehat V=2\operatorname{Vol}/\pi^2\); see the volume-renormalized charges in `notes/step33_link_charges_global_decomposition_static_channel.md`.

This answers the proposed scale-channel mechanism precisely. The Einstein constant \(\hat\lambda=-G_{00}\) has zero free drift and is pinned, but the collapsed \(\Lambda\)-Taub–NUT neck already has \(\hat\lambda=-6\). The trace channel therefore cannot be where late opening is paid, consistent with the \(D\)-dominated split in §2.

**Lemma W (volume comparison).** Let \(s\equiv-24\) on \([T,T_1]\), suppose \(R^{(3)}\ge-\rho_0\) there with \(A^2=18-\rho_0>0\), and let \(0<\sigma_0<m:=\min\{S(T),A\}\). If
\[
m-\Big(\frac{3\widehat P_{[T,T_1]}}{\sigma_0W(T)}\Big)^{1/2}\ >\ \sigma_0,
\]
then \(S>\sigma_0\) on \([T,T_1]\), \(W(t)\ge W(T)e^{\sigma_0(t-T)}\), and \(\int_T^{T_1}dt/W\le1/(\sigma_0W(T))\) (hypothesis with strict inequality \(>\sigma_0\)).

*Proof (last-crossing form, repaired after the Step-32 independent reading).* Let \(T^*=\sup\{t\le T_1:S\ge\sigma_0\text{ on }[T,t]\}\). On \([T,T^*]\), \(W'=SW\ge\sigma_0W\), so \(\int_T^tdt/W\le1/(\sigma_0W(T))\) and, by (3) and Cauchy–Schwarz, \(\int_T^t|\mathcal C|\le(3\widehat P)^{1/2}(\sigma_0W(T))^{-1/2}\). Fix \(t\in[T,T^*]\). If \(S(t)\ge m\) there is nothing to prove. Otherwise let \(t_0=\sup\{s\in[T,t]:S(s)\ge m\}\); it exists because \(S(T)\ge m\), and \(S(t_0)\ge m\) by continuity. On \((t_0,t]\), \(0<\sigma_0\le S<m\le A\), hence \(S'\ge A^2-S^2+\mathcal C>-|\mathcal C|\) by (4), and \(S(t)\ge m-\int_{t_0}^t|\mathcal C|\ge m-(3\widehat P/(\sigma_0W(T)))^{1/2}>\sigma_0\). (When \(S(T)>A\) the curve may first decrease freely while \(S>A\); the last crossing of the level \(m\) is what makes the argument valid.) Thus \(S>\sigma_0\) at \(T^*\), so \(T^*=T_1\). \(\square\)

Lemma W supplies the volume comparison needed to apply Lemma P and fibre/base pinning to a general connector: on an interval with \(R^{(3)}\ge-\rho_0\), the actual \(\int W^{-1}\) is bounded by \(1/(\sigma_0W(T))\). It also prices the high-shear volume bounce: \(S\) can fall below \(\min\{S(T),A\}\) only by \(\int|\mathcal C|\), which costs \(\ge(\Delta S)^2\sigma_0W/3\). Two residual inputs remain. The orbit curvature hypothesis \(R^{(3)}\ge-\rho_0\) is a bound on \(\kappa\) and on \(\zeta^2\sinh^2q/\kappa^2\), and the drifts \(F,F_\beta\) of the first-order pinning observables are small only in an ACH block.

## 4. Large bolt: the Rossi datum is fixed at volume \(b^2\)

`scripts/large_bolt_volume_profile.py` integrates the validated ACH1 separatrices (`data/ach_fate/large_bolt_volume_profile.json`). Along the Einstein orbit from the bolt, \(W\) is monotone; there is no base-shrinking excursion. The minimum of \(W\) on \(t\ge.05\) is at \(t=.05\), with value \(\approx b^2t\). The Rossi observable is set early, in a region of volume \(\sim b^2\):

| \(b\) | \(\widetilde\Phi(0.77)\) | \(\widetilde\Phi(1.15)\) | \(\widetilde\Phi_\infty=\log\rho\) | \(W(0.77)\) |
|---|---|---|---|---|
| 0.8 | 0.096 | 0.630 | 0.7847 | 2.96 |
| 2 | 0.680 | 1.061 | 1.1543 | 13.2 |
| 20 | 2.861 | 3.213 | 3.2941 | 1212 |

Profiles are close to \(b\)-independent in \(\kappa(t)\) (2.63, 1.43, 1.14 at \(t=.38,.77,1.15\) for \(b=20\); 2.66, 1.46, 1.16 for \(b=2\)), while \(\zeta b\) and \(\widetilde\Phi-\log b\) converge. This suggests the **face limit**: as \(b\to\infty\), the separatrix converges in \((y,\kappa,\zeta b,\widetilde\Phi-\log b)\) to an Einstein trajectory of the \(\zeta=0\) face from the bolt corner \(\kappa=\infty\) to \(E(q)\). The face system is \(q\)-independent, so \(q\) is cyclic there and its offset is \(\log b\).

The face limit is confirmed numerically by `scripts/large_bolt_face_limit.py` (`data/ach_fate/large_bolt_face_limit.json`), which bisects the AH/SING separatrix near \(d\approx0.9b\):

| \(b\) | \(d/b\) | \(\kappa(1)\) | \(\zeta b\,(1)\) | \(W/b^2\,(1)\) | \(\widetilde\Phi-\log b\) at \(t=0.5,1,2,3\) |
|---|---|---|---|---|---|
| 20 | 0.903977 | 1.21352 | 0.38711 | 8.0979 | −1.2418, 0.14396, 0.29593, 0.29828 |
| 50 | 0.905139 | 1.21330 | 0.38724 | 8.0910 | −1.2425, 0.14262, 0.29439, 0.29674 |
| 100 | 0.905305 | 1.21327 | 0.38726 | 8.0900 | −1.2426, 0.14243, 0.29417, 0.29652 |
| 200 | 0.905346 | 1.21326 | 0.38727 | 8.0898 | −1.2426, 0.14238, 0.29412, 0.29646 |

Hence \(d\sim0.90535\,b\) and \(\rho_\infty\sim e^{0.2965}b\approx1.345\,b\), in agreement with the earlier fit \(1.343b\). Every rescaled face quantity converges with differences of order \(b^{-2}\). The Rossi offset is produced between \(t=0.5\) and \(t\approx1.5\), where \(W/b^2\in[0.97,64]\). The large-bolt Einstein orbit is therefore an \(O(b^{-2})\) perturbation of one face Einstein trajectory, and its CR datum differs from the standard one by \(\log(1.345b)\), carried at volume \(\asymp b^2\). (The \(b=2\) bracket \([0.8b,b]\) contained no transition; the \(b=2\) separatrix at \(d=1.555\) lies outside it and is consistent with the trend \(d/b\uparrow0.905\).)

**Theorem L (programme).** For standard-CR diagonal cells with bolt \(b\to\infty\), \(\widehat P\to\infty\), heuristically as \(b^2(\log b)^2\).

The proposed proof has three steps.
1. Bounded \(\widehat P\) together with \(W\gtrsim b^2t\) forces \(\int(\mathcal C^2+E^2+D^2)\,W/b^2\to0\) at face scale. This uses Lemma N, with the bolt series controlling \(t\lesssim b^{-2}\).
2. Lemma W and face compactness give convergence on \([t_0,T_0]\) to face Einstein trajectories. Their ACH separatrices have \(\widetilde\Phi-\log b\to\phi_1\), with \(|\phi_1|\) bounded; this includes the mirror ACH2.
3. At \(T_0\) the state lies in a standard ACH block at volume \(W\gtrsim b^2e^{4T_0}\). Lemma P with Lemma W then charges the shift \(\log b\) by at least \(c\,b^2(\log b)^2\).

A linear-response estimate near the bolt shows that earlier correction is not cheaper. Forcing \(\Delta e=A\) on \([0,t_1]\), where \(W\sim b^2t\), shifts \(\int(y_g-y_h)\) by \(-At_1^2/4\) at cost \(\sim b^2A^2t_1^2\). A shift of \(\log b\) therefore costs \(\sim b^2(\log b)^2/t_1^2\), which is minimized at \(t_1\sim1\).

## 5. Revised compactness statement

The converse of Theorem D now needs three inputs instead of four:

* **(N) non-round late opening** — covers small-bolt saturation, collapsed shear and every collapsing bounce. It is numerically \(\ge5.37\) for every tested \(\varepsilon\), and round reopening is excluded by Lemma V;
* **(L) large bolt** — follows from the face-limit programme of §4, with growth \(b^2(\log b)^2\);
* **(F) conformal-face escape** — the large-bolt face analysis takes place on the same \(\zeta=0\) face. The face spectrum at \(E(q)\) (\(2,0,-4,-6,-8\)), the AH attractor \(y_i=\sqrt2,\kappa=0\), and Lemma W are the common tools.

Raw high shear that does not collapse is excluded by Lemma V Consequence 2 whenever it raises \(\mathfrak b_-\) above \(7+p_*\) or \(\mathfrak b_+\) above \(1+p_*\). A shear bounce that does neither falls under Lemma W, which prices the volume bounce through \(\mathcal C\).
