# Step 26 — Action-budget matching for small bolts

## 1. Two different small-bolt limits

The small-bolt question has two mathematically distinct inputs.

### Exact-Einstein degeneration

For a sequence of diagonal Einstein metrics with `Ric = -6 g` and bolt scale `b_j -> 0`, the rescaling `g_j^# = b_j^{-2} g_j` preserves the Einstein equation with rescaled Einstein constant `-6 b_j^2`. A smooth pointed limit can therefore be Ricci-flat. The Taub-bolt / collapsed Lambda–Taub–NUT matching and its unstable triaxial mode are relevant to this sequence, provided the rescaling, convergence, and end extraction are proved.

### Near-minimizing scalar-normalized cells

For a general exact-CH-ended competitor, scalar normalization gives `s(g_j)=-24`, but the cell functional is
\[
\widehat P(g)=\frac{1}{8\pi^2}\int|\operatorname{Ric}^{\circ}|^2.
\]
If `b_j` is the bolt scale and `g_j^#=b_j^{-2}g_j`, then in dimension four
\[
\widehat P(g_j^\#)=\widehat P(g_j),\qquad s(g_j^\#)=-24b_j^2\longrightarrow0.
\]
Consequently a smooth rescaled limit is scalar-flat, but it need not be Ricci-flat when only `\widehat P(g_j)\le c<1` is known. The Einstein bolt series imposes Ricci equations and fixes jets that a general scalar-normalized competitor does not satisfy. Refining its free anisotropy parameter can settle the exact-Einstein branch, but cannot by itself exclude a scalar-flat finite-action core from the cell infimum.

The correct matching problem must therefore retain both possibilities: a Ricci-flat Taub-bolt limit when the defect tends to zero, and a potentially non-Einstein scalar-flat core for a merely subthreshold sequence.

## 2. Exact chiral action budget on a bolt-to-section prefix

For a diagonal annulus the independently verified chiral identities are
\[
\widehat P(C)=\Delta \mathfrak b_+ + \frac{1}{2\pi^2}\int_C|W^+|^2
 +\frac{1}{96\pi^2}\int_Cs^2,
\]
and the same formula with `+` replaced by `-`. All terms after the charge difference are nonnegative.

A smooth `O(-1)` bolt has
\[
\mathfrak b_+=1,\qquad \mathfrak b_-=7.
\]
Therefore, for every diagonal prefix from the bolt to a section `\Sigma`,
\[
\boxed{
\widehat P([\mathrm{bolt},\Sigma])\ge
\max\{0,\mathfrak b_+(\Sigma)-1,\mathfrak b_-(\Sigma)-7\}.
}
\tag{2.1}
\]
The two chiral lower bounds refer to the same prefix energy and must not be added. This statement is exact for the diagonal annulus and does not require the prefix to be Einstein or scalar-flat.

At a controlled collapsed section, with
\[
x=Xz^3+o(z^3),\quad p=Pz+o(z),\quad
\chi=Cz+o(z),\quad \eta=Nz+o(z),
\]
the exact charge limit is
\[
\mathfrak b_+=-2-(C+4X)^2,\qquad
\mathfrak b_-=2+(C-4X)^2.
\]
Thus (2.1) gives
\[
\boxed{
\liminf\widehat P([\mathrm{bolt},\Sigma_j])
\ge \max\{0,(C-4X)^2-5\}.
}
\tag{2.2}
\]
The plus channel is nonpositive at this endpoint and supplies no positive bound; the opposite channel is the useful one.

If the whole competitor has `\widehat P\le c+o(1)`, then every controlled section reached by that competitor satisfies
\[
(C-4X)^2\le c+5.
\tag{2.3}
\]
On the plus-charge kernel `C+4X=0`, this becomes
\[
64X^2\le c+5,
\qquad |X|\le\frac{\sqrt{c+5}}8.
\tag{2.4}
\]
For illustration, if `c=0.99585` (the peer's Step-31 numerical scale; the current Session's authoritative certified transfer remains `0.995671...`), this gives `|X|<0.3061` on the kernel. In particular an order-one kernel entry such as `(X,C)=(1,-4)` cannot be reached within a total action below one. This is a finite-action obstruction to the most favorable normalized kernel search; it does not prove that every bolt sequence enters the controlled class.

## 3. The action-budget matching alternative

Let `\Sigma_j` be the first section at which a collapsing bolt sequence enters a controlled finite-charge class. Then the chiral budget supplies the explicit prefix cost (2.2). There are only two ways for a low-action sequence to avoid this bound:

1. it reaches a controlled section, in which case (2.2)--(2.4) constrain the normalized shear parameters; or
2. no such section occurs before the geometry leaves the collapsed regime, so the sequence remains outside controlled first-jet compactness. The missing estimate is then a direct action bound for the departure from the controlled class, not an Einstein matching statement.

A useful theorem target is therefore an action-budget alternative of the form
\[
\widehat P([\mathrm{bolt},\Sigma])
\ge \Psi(\mathcal D_\Sigma,W_\Sigma),
\]
where `\mathcal D_\Sigma` measures failure of the controlled scale-free expansion and `W_\Sigma=a_fa_ga_h` records the volume weight. The charge identities give the part of `\Psi` depending on `C-4X`; they are blind to the radial variable `P`, the volume/shear variable `N`, and the uncontrolled raw contact rate. The Ricci equations, scalar constraint, and an actual `W^{-1}` estimate must supply these missing terms.

The fibre/base pinning identity has the complementary form
\[
\widetilde B'=F_\beta-\frac14E,
\qquad
\widehat P\ge\frac16\int W E^2\,dt,
\]
so
\[
\left|\Delta\widetilde B-\int F_\beta dt\right|
\le\sqrt{\frac{3\widehat P}{8}}
\left(\int\frac{dt}{W}\right)^{1/2}.
\]
On an exact CH tail the denominator is explicit, but on a general connector it must remain the actual `\int W^{-1}dt`. This identity can price the part invisible to the chiral charges only after the drift `F_\beta` and volume degeneration have been controlled.

## 4. Consequences for the research route

The diagonal degeneration route should now be separated into:

* the exact-Einstein branch, where rigorous Taub-bolt / Lambda–Taub–NUT matching can describe a Ricci-flat rescaled limit;
* the scalar-flat finite-action branch, where nonzero trace-free Ricci energy remains possible and must be included in the compactness statement;
* the raw high-shear branch, where neither controlled charge limits nor the Einstein bolt series apply automatically.

The chiral budget has already removed the order-one plus-kernel entry from the low-action controlled class. The decisive remaining work is a quantitative estimate for the third branch, ideally combining the normalized Ricci equations, the scalar constraint, and fibre/base pinning with the exact chiral budget. This would connect collapse analysis to the unrestricted cell infimum rather than classifying only the zero-defect Einstein family.

## 5. Independent verification and a D-channel pinning identity

The peer's Lemma N was independently re-derived in `workspace/scripts/step26_independent_constraint_and_D_pin.py`; output is `data/step26_independent_constraint_and_D_pin.json`. All five symbolic residuals vanish: the Hamiltonian residual satisfies
\[
\mathcal C=\frac{e_0-e_f-e_g-e_h}{2},
\]
its Bianchi propagation is
\[
\mathcal C'=-2S\mathcal C-\sum_i(S-y_i)e_i,
\]
constant scalar `-24` gives `C=Ric^\circ_{00}` and
\[
S'=18-S^2+R^{(3)}+\mathcal C.
\]
The independent calculation also verifies the exact anisotropy equation
\[
(Wq')'=W(P_g-P_h-D),\qquad q=\log(a_g/a_h),\quad D=e_g-e_h,
\]
with
\[
P_g-P_h=-8z\sinh q+\frac{8z^2}{\kappa^2}\sinh(2q).
\]

For an interval `[T_0,T_1]`, define
\[
K(t)=\int_t^{T_1}\frac{du}{W(u)},\qquad K(T_1)=0,
\]
and
\[
M=q(T_1)-q(T_0)-W(T_0)q'(T_0)K(T_0)
-\int_{T_0}^{T_1}W(P_g-P_h)K\,dt.
\]
Then the exact Green identity is
\[
M=-\int_{T_0}^{T_1}WDK\,dt,
\]
and hence
\[
\boxed{\widehat P_{[T_0,T_1]}\ge
\frac{M^2}{8\int_{T_0}^{T_1}WK^2dt}.}
\]
This is a rigorous D-channel pinning bound for prescribed endpoint data, but it does not become a universal positive lower bound until the Einstein drift `P_g-P_h`, the volume `W`, and the endpoint momentum are controlled.

If on the interval `W(t)\ge W_0e^{\sigma(t-T_0)}` and an upper comparison is also available for the Green denominator, the model exponential weight gives
\[
\int WK^2dt=\frac{1-e^{-2\sigma L}-2\sigma L e^{-\sigma L}}{W_0\sigma^3},\qquad L=T_1-T_0,
\]
so a drift-corrected anisotropy mismatch of order one at volume `W_0` costs order `W_0\sigma^3` unless the Einstein drift itself supplies the change. In a bounded AH/ACH block, the exact drift formula gives the conditional estimate
\[
|P_g-P_h|\le 8z|\sinh q|+8z^2\kappa^{-2}|\sinh(2q)|,
\]
which can be integrated against `WK` and subtracted from the endpoint mismatch. This is the natural D analogue of the volume comparison: it isolates the only zero-cost route (the controlled Einstein drift) and prices all residual q-opening by the full Ricci-defect action.

## 6. Verification correction to Lemma W

The scalar-normalized constraint identities are exact. The proof of Lemma W is valid after stating its bootstrap carefully. Set `E(t)=\int_T^t|\mathcal C|du`. For any first point where `S+E` would fall below `m=min(S(T),A)`, the boundary value satisfies `S=m-E\le A`, so `A^2-S^2\ge0` and `S'+E'\ge0`; thus `S+E\ge m`. While `S\ge\sigma_0`, `W\ge W(T)e^{\sigma_0(t-T)}` and
\[
E(t)\le\left(\int_T^tW\mathcal C^2du\right)^{1/2}
\left(\int_T^tW^{-1}du\right)^{1/2}
\le\left(\frac{3\widehat P_{[T,T_1]}}{\sigma_0W(T)}\right)^{1/2}.
\]
The stated hypothesis closes the bootstrap and yields
\[
S\ge\sigma_0,\quad W(t)\ge W(T)e^{\sigma_0(t-T)},\quad
\int_T^{T_1}W^{-1}dt\le(\sigma_0W(T))^{-1}.
\]
The argument needs `R^(3)\ge-\rho_0` and `A^2=18-\rho_0>0`; no Einstein condition is used. The phrase `while |S|\le A` should be replaced by the first-barrier argument above, since `S(T)` may exceed `A`.

## 7. Charge variation strengthens raw-shear exclusion

The peer's Step-31 Lemma V adds a pathwise form of the chiral budget. Since each chiral identity is pointwise in the orbit parameter,
\[
\frac{W}{4}|\Ric^\circ|^2\ge \max\{0,\mathfrak b_+',\mathfrak b_- '\}
\]
(pointwise derivatives), and therefore
\[
\widehat P([T_0,T_1])\ge\int_{T_0}^{T_1}\max\{0,\mathfrak b_+',\mathfrak b_- '\}\,dt.
\]
In particular, for an `O(-1)` bolt,
\[
\widehat P\ge\sup_t\max\{\mathfrak b_+(t)-1,\mathfrak b_-(t)-7\},
\]
and the positive variation of either charge gives a stronger path-sensitive bound. The raw `\Delta\eta=-8` entry has `\mathfrak b_-=8.54957`, so its bolt prefix alone costs at least `1.54957`, independently of the connector reconstruction. This removes that numerical escape below the certified cell even more decisively than the earlier prefix-plus-connector estimate.

The charge-variation bound still does not price late opening when the charges decrease or remain low. The constrained optimal-control runs with `\mathfrak b_+\le-1` have costs around `6.44--6.62`, while the charge-variation contribution is only about `1.5`; the remaining cost is mainly the `D` channel. Thus the Green identity above is the appropriate next analytic object: it prices residual contact-slot anisotropy after subtracting its geometric drift, whereas the chiral charge prices only characteristic upward motion.

## 8. Status of the main theorem target

The strongest current statement is an action-budget alternative for the diagonal scalar-normalized class, not a completed unrestricted lower bound. A sequence with bounded total `\widehat P` and a controlled collapsed section obeys the exact charge limit and the kernel restriction. A raw high-shear section that raises either chiral charge above the bolt budget is excluded directly by Lemma V. The remaining branch—non-round late opening with low/decreasing charges—must be controlled by the scalar constraint, volume bootstrap, and D-channel Green pinning. The exact equations now separate:

* `C`, the Hamiltonian constraint residual, with pointwise penalty `\int W C^2/3`;
* `D`, the contact-slot anisotropy residual, with the exact Green pinning estimate;
* `E`, the fibre/base residual, controlled by the established `\widetilde B` identity;
* chiral positive variation, which prices upward topology/shape charge changes.

This decomposition identifies the missing lower estimate without assuming that an Einstein separatrix describes every near-minimizer. The exact-Einstein Taub-bolt matching remains relevant only to the defect-to-zero branch; finite-action scalar-flat rescaled cores remain admissible in the subthreshold cell problem.

## 9. A conditional D-analogue of the volume comparison

The exact D Green estimate becomes explicit in an expanding AH/ACH block. Let `[T_0,T_1]` satisfy the separate expanding-block hypotheses
\[
B(t):=y_g+y_h\ge\sigma>0,
\qquad S(t):=y_f+y_g+y_h\ge\sigma>0,
\qquad |q(t)|\le Q,
\qquad \kappa(t)\ge\kappa_0>0.
\]
(The first condition controls the collapsed ratio; the second controls volume.) Since `z'=-Bz`,
\[
z(t)\le z_0e^{-\sigma(t-T_0)},
\quad |P_g-P_h|\le A_Q z_0e^{-\sigma(t-T_0)}+B_Qz_0^2e^{-2\sigma(t-T_0)},
\]
where
\[
A_Q=8\sinh Q,\qquad B_Q=8\kappa_0^{-2}\sinh(2Q).
\]
The volume hypothesis gives `W(t)\ge W_0e^{\sigma(t-T_0)}`. Therefore
\[
K(t)\le\frac{1}{\sigma W(t)},\qquad
\int_{T_0}^{T_1}WK^2dt\le\frac1{\sigma^3W_0},
\]
and the drift term obeys
\[
\left|\int_{T_0}^{T_1}W(P_g-P_h)Kdt\right|
\le \frac{A_Qz_0}{\sigma^2}+\frac{B_Qz_0^2}{2\sigma^2}.
\]
Consequently the following conditional lower estimate is rigorous:
\[
\widehat P_{[T_0,T_1]}
\ge \frac{\sigma^3W_0}{8}
\left(
\left|q_1-q_0-W_0q'_0K_0\right|
-\frac{A_Qz_0}{\sigma^2}-\frac{B_Qz_0^2}{2\sigma^2}
\right)_+^2.
\tag{9.1}
\]
Here `K_0` is the actual Green tail `int_{T0}^{T1}W^{-1}` and `q_1=q(T_1)`. A simpler endpoint version replaces `|W_0q'_0K_0|` by `|q'_0|/sigma`. This is a genuine D-channel counterpart to Lemma W: it prices a residual contact-slot mismatch at initial volume `W_0`, after subtracting the explicit Einstein drift. It applies only after a controlled expanding block has been established; it does not price the initial collapsed or raw high-shear region, where `q` may be unbounded or `kappa` may degenerate.

The bound exposes the research bottleneck sharply. To close non-round late opening, one needs either (i) an expanding block with `sigma`, `Q`, and `kappa_0` uniform and a mismatch exceeding the drift/error budget, or (ii) a separate action estimate for the interval before those hypotheses hold. The first is now a concrete interval-enclosure task rather than a vague D-channel assertion.

## 10. Momentum-renormalized late-opening alternative

A clean two-stage form removes the free incoming `D`-momentum from the one-interval estimate. Let `T_-<T_0<T_1`, `J=Wq'`, and on `[T_0,T_1]` let
\[
K(t)=\int_t^{T_1}W(u)^{-1}du,
\quad K_0=K(T_0),
\quad \Pi=P_g-P_h.
\]
Set
\[
J_-=J(T_-),\quad R_- =\int_{T_-}^{T_0}W\Pi\,dt,
\quad R_+=\int_{T_0}^{T_1}W\Pi K\,dt.
\]
The exact equation `J'=W(Pi-D)` gives
\[
M:=q(T_1)-q(T_0)-(J_-+R_-)K_0-R_+
=-K_0\int_{T_-}^{T_0}WD\,dt-
\int_{T_0}^{T_1}WDK\,dt.
\]
Therefore
\[
\boxed{
\widehat P_{[T_-,T_1]}\ge
\frac{M^2}{8\left(K_0^2\int_{T_-}^{T_0}Wdt+\int_{T_0}^{T_1}WK^2dt\right)}.}
\tag{10.1}
\]
This is stronger than treating `J(T_0)` as an arbitrary endpoint datum: only the flux entering at `T_-` is free, while momentum created inside the preceding interval is charged by the same `D` action.

On `[T_0,T_1]`, assume
\[
R^{(3)}\ge-\rho,
\quad A^2=18-\rho>0,
\quad B=y_g+y_h\ge\mu>0,
\quad S\ge\sigma>0,
\quad |q|\le Q,
\quad \kappa\ge\kappa_0>0.
\]
Let `m=min(S(T0),A)` and choose `0<sigma<m`. The corrected Hamiltonian barrier gives the alternative
\[
S\ge\sigma\quad\text{or}\quad
\widehat P_{[T_0,T_1]}\ge L_C:=\frac{\sigma W(T_0)}3(m-\sigma)^2.
\]
On the expanding branch,
\[
K_0\le(\sigma W_0)^{-1},\qquad
\int_{T_0}^{T_1}WK^2dt\le(\sigma^3W_0)^{-1},
\]
and with `zeta=1/(a_ga_h)`, `zeta'=-B zeta`,
\[
|R_+|\le
\frac{8\zeta_0\sinh Q}{\sigma\mu}
+\frac{4\zeta_0^2\sinh(2Q)}{\sigma\mu\kappa_0^2}.
\]
If `Xi_- = ∫_{T_-}^{T0}W|Pi|dt` and `W_- = ∫_{T_-}^{T0}Wdt`, then
\[
|M|\ge\left(|q(T_1)-q(T_0)|-
\frac{|J_-|+\Xi_-}{\sigma W_0}-\Lambda_+\right)_+,
\]
with `Lambda_+` the displayed drift bound, while the Green denominator is at most
\[
H=\frac{W_-}{\sigma^2W_0^2}+\frac1{\sigma^3W_0}.
\]
Hence
\[
\boxed{
\widehat P_{[T_-,T_1]}
\ge\min\left\{L_C,\frac{\Delta_q^2}{8H}\right\}.}
\tag{10.2}
\]
The estimate is conditional and reusable: it prices a residual contact-slot change after explicitly subtracting inherited momentum and Einstein drift. It does not assert a universal positive late-opening constant, because exact Einstein arcs can carry arbitrary incoming anisotropy momentum with zero defect action. The correct global statement is an alternative: upward chiral variation, Hamiltonian loss of expansion, or a momentum-renormalized `D` mismatch must occur, unless the trajectory follows a globally compatible Einstein mode.

This also explains the peer's numerical `D`-dominated non-round opening. Charge variation sees only the upward part of characteristic flux; the residual opening is supplied by `D` after subtracting `J_-` and `Pi`. A theorem for all near-minimizers must bound the incoming flux from the bolt or prove that producing it already consumes the action. Exact-Einstein matching alone cannot supply that bound for scalar-normalized competitors.
