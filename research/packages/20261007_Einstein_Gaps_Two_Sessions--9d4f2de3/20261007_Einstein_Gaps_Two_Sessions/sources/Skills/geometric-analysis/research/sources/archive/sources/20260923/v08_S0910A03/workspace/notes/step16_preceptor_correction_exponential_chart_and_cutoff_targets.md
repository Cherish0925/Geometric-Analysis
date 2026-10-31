# Step 16: correction of the fixed-topology gap, exponential-chart averaging, and the exact remaining analytic bridge

## 1. Correction to Step 15

The assertion in Sections 10--13 of `step15_L2_chain_and_separated_demands.md` that Ye Li's proof directly localizes to the plateau is withdrawn.

There are two definite failures.

1. Li's bootstrap quantity is a supremum over every center in the domain on which the energy propagation is asserted. If the centers range over `Omega_work`, centers near its boundary require adjacent covering balls outside `Omega_work`. If one instead takes the supremum only over `Omega_inner`, evolution of an inner ball still invokes neighboring outer balls; this is the same unresolved inner/outer inequality identified in Step 14.
2. Ricci flow has no finite propagation speed. The scale `sqrt(t)` is a diffusion scale, not a region outside which boundary or transition data have no effect. Freezing the exterior of the cutoff flow does not remove the transition annulus from an interior estimate.

There is also a static scale mismatch in the old presentation: a maximal-function bound at one good point controls all radius-`r_*` centers in a fixed multiple of `r_*`, not all centers in a much larger `rho/4` ball when `r_* << rho`. A coherent construction must choose support, buffer, and covering radii as fixed multiples of the same Li scale.

Consequently the fixed critical Ishida--LeBrun negative-branch gap is not proved. The valid result retained from Step 15 is the metric-by-metric calibration inequality

\[
 \int_M\left(|W^+|-\frac1{2\sqrt6}\right)^2d\mu
 \le \frac7{24}\int_M|\operatorname{Ric}+g|^2d\mu.
\]

This applies to every smooth metric on the fixed critical manifold and therefore to every smooth time of a cutoff flow, but it does not propagate the right-hand side.

## 2. Transition-inclusive cutoff-flow target

Set

\[
 E=\operatorname{Ric}+g,\qquad a=\chi^2,\qquad \partial_tg=-2aE.
\]

The exact defect variation has the form

\[
 \partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E),
\]

where every term in `C_a(E)` contains `E`, `tr E`, or a first derivative thereof. After testing by an independent cutoff `eta`, integration by parts, and the contracted Bianchi identity, the useful energy inequality is

\[
\begin{aligned}
 \frac d{dt}\int\eta^2|E|^2+c\int\eta^2a|\nabla E|^2
 \le{}&C\int(a|d\eta|^2+\eta^2|d\chi|^2+\eta^2a)|E|^2\\
 &+C\int\eta^2a|\operatorname{Rm}|\,|E|^2.
\end{aligned}
\tag{E}
\]

The identity `|da|^2/a=4|d chi|^2` removes an intrinsic `1/chi` loss. Homogeneity therefore rules out an additive collar source, but not multiplicative amplification.

The full curvature evolution contains transition terms schematically

\[
 \nabla^2a*E+\nabla a*\nabla E.
\]

At the local energy level this gives

\[
\begin{aligned}
 \frac d{dt}\int\eta^2|\operatorname{Rm}|^2+c\int\eta^2a|\nabla\operatorname{Rm}|^2
 \le{}&Cr^{-2}\int_{\mathrm{nbhd}(\eta)}(|\operatorname{Rm}|^2+|E|^2)\\
 &+C\int\eta^2a|\operatorname{Rm}|^3
 +\epsilon\int\eta^2a|\nabla E|^2.
\end{aligned}
\tag{R}
\]

Here the last term comes from

\[
 |\nabla a|\,|\nabla E|\,|\operatorname{Rm}|
 =2\chi|\nabla\chi|\,|\nabla E|\,|\operatorname{Rm}|
\]

and must be absorbed by the defect dissipation in (E). Thus the right object is a coupled energy, not a curvature-only estimate.

For a finite-overlap cover of the **entire active support and buffer**, define normalized local energies and dissipations

\[
\begin{aligned}
 R_\alpha&=\frac{r^4}{V_\alpha(0)}\int\eta_\alpha^2|\operatorname{Rm}|^2,
 &X_\alpha&=\frac{r^4}{V_\alpha(0)}\int\eta_\alpha^2a|\nabla\operatorname{Rm}|^2,\\
 P_\alpha&=\frac{r^4}{V_\alpha(0)}\int\eta_\alpha^2|E|^2,
 &Y_\alpha&=\frac{r^4}{V_\alpha(0)}\int\eta_\alpha^2a|\nabla E|^2.
\end{aligned}
\]

The target inequalities are

\[
\begin{aligned}
 \dot R_\alpha+cX_\alpha&\le Cr^{-2}\sum_{\beta\sim\alpha}(R_\beta+P_\beta)+\epsilon_1Y_\alpha,\\
 \dot P_\alpha+cY_\alpha&\le Cr^{-2}\sum_{\beta\sim\alpha}P_\beta.
\end{aligned}
\tag{C}
\]

The cubic and curvature--defect reactions are absorbable when the local normalized curvature energy stays below the critical four-dimensional threshold; relative Sobolev volume factors cancel against local `L^2` curvature volume. For sufficiently large fixed `kappa`, `H_alpha=R_alpha+kappa P_alpha` would then obey a closed finite-neighbor inequality and yield persistence for time `theta r^2`.

This formal architecture is plausible but still lacks a noncircular continuation package. The missing outputs from the initial data are:

- metric equivalence on the entire active support;
- preservation of relative Sobolev inequalities, balls, and overlap constants;
- control of `|nabla chi|` and especially the covariant `|nabla^2 chi|` along the evolving metric;
- an integrable weighted pointwise estimate for `aE`, needed because `partial_t g=-2aE` and `L^2` energy alone does not control metric drift.

The required theorem should prove these jointly with

\[
 \sup_\alpha R_\alpha(t)\le 2\varepsilon,
 \quad |\chi^2\operatorname{Rm}(t)|\le C/t,
 \quad |\chi^2E(t)|\le C\delta(r^2/t)^\gamma\quad(\gamma<1),
\]

rather than assuming any one of them to prove the others. Existing Yang--Wang and Fei He local-flow theorems support the tensor structure but impose stronger global Sobolev/full-support energy or initial derivative hypotheses.

## 3. Exponential-pullback averaging lemma

The later collapse reconstruction can be simplified once a positive-volume buffered set with bounded sectional curvature exists.

### Lemma

Let `(M^n,g)` be closed, let `P subset M` be measurable, and suppose every radius-`r` geodesic emitted from every `p in P` stays in a region with

\[
 |\sec_g|\le K,
 \qquad 0<r<\frac{\pi}{2\sqrt K}
\]

(with the evident convention for `K=0`). Put `h_p=exp_p^*g` on `B_r(0) subset T_pM`. For every nonnegative measurable `F`, extended by zero outside the controlled region,

\[
 \int_P \fint_{B_r(0),h_p}F(\exp_pv)\,d\mu_{h_p}(v)\,d\mu_g(p)
 \le C(n,K,r)\int_MF\,d\mu_g,
\tag{A}
\]

where

\[
 C(n,K,r)=
 \frac{\displaystyle\int_0^r\left(\frac{\sinh(\sqrt Kt)}{\sqrt K}\right)^{n-1}dt}
 {\displaystyle\int_0^r\left(\frac{\sin(\sqrt Kt)}{\sqrt K}\right)^{n-1}dt}.
\]

No injectivity-radius or sheet-number bound is required.

### Proof

Let `gamma_{p,theta}(t)=exp_p(t theta)` and let `J_p(t,theta)` be the radial Jacobi determinant. Rauch comparison gives

\[
 s_K(t)^{n-1}\le J_p(t,\theta)\le s_{-K}(t)^{n-1},
\]

where `s_K(t)=sin(sqrt(K)t)/sqrt(K)` and `s_{-K}(t)=sinh(sqrt(K)t)/sqrt(K)`. Hence

\[
 \operatorname{Vol}_{h_p}B_r(0)
 \ge \omega_{n-1}\int_0^rs_K(t)^{n-1}dt.
\tag{B}
\]

For the numerator,

\[
 \int_{B_r(0)}F(\exp_pv)d\mu_{h_p}
 \le\int_0^rs_{-K}(t)^{n-1}\int_{S_pM}F(\gamma_{p,\theta}(t))d\theta\,dt.
\]

The geodesic flow `phi_t` preserves Liouville measure on `SM`; therefore

\[
 \int_{SM}F(\pi\phi_tz)dL(z)=\omega_{n-1}\int_MF\,d\mu_g.
\]

Because `F>=0`, enlarging `SM|_P` to all of `SM`, applying Tonelli, and dividing by (B) proves (A). Arbitrarily many exponential sheets cause no loss: terminal direction is retained in the measure-preserving map `phi_t`. The origin is harmless because `J_p(t,theta)=t^{n-1}(1+O(t^2))`.

If `Vol(P)>=v_0>0` and `int F_i ->0`, (A) selects `p_i in P_i` with a fixed-radius, noncollapsed exponential pullback chart on which the normalized integral of `F_i o exp_{p_i}` tends to zero.

For smooth convergence of these charts, bounded sectional curvature alone is insufficient. A standard sufficient positive-time input is uniform `|nabla^m Rm|` bounds on a slightly larger buffered region for every `m`; Shi-type estimates would supply these after a successful smoothing theorem. Weaker harmonic-coordinate compactness followed by Einstein elliptic regularity may also suffice, but must be stated at its actual regularity.

## 4. Quantitative monopole/eigenline density for chart selection

Unique continuation does not ensure that a selected sequence of charts carries nonzero limiting harmonic-form mass. For each metric, a nonzero harmonic form may be nonzero almost everywhere yet tend to zero on the chosen charts. Local nonvanishing must be selected through a nonnegative amplitude density.

At an evolved smooth metric, all monopole objects must be reconstructed for that current metric. A maximizing sign class may depend on the metric; on a fixed manifold its finite sign family permits a constant-class subsequence. The harmonic representative `H_i`, spinor quadratic form, Hodge projection, and rescaled monopole equation are not transported by the cutoff flow.

A potential sign issue arises because

\[
 q_i=\sqrt6|W_i^+|-s_i
\]

need only converge to `9/2` in `L^2` when `Q_i=int|E_i|^2 ->0`; it need not be positive pointwise. This can be repaired by setting `r_i=q_i^+`. For a smooth positive weight `f`, define

\[
 L_i^+(f)=\left(\int f^4\right)^{1/3}
 \left(\int r_i^3f^{-2}\right)^{2/3}.
\]

Taking `f^2` to be a smooth positive approximation of `r_i+epsilon_i` gives

\[
 \int r_i^2\le L_i^+(f_i)\le\int r_i^2+\epsilon_i^2\operatorname{Vol}(g_i)+o(1).
\]

The exact deficit algebra acquires one extra favorable term

\[
 N_f=\int q_i^-u_i^2\ge0,
\]

and otherwise has the same nonnegative decomposition. No derivatives of `f` occur. Hence, on a fixed critical manifold with `Q_i->0` and bounded recovered volume, choose `epsilon_i^2 Vol_i->0` and obtain a current-metric monopole with primitive deficit `O(Q_i)`. In particular,

\[
 \left\||H_i|-\frac{3}{4\sqrt2\pi}\right\|_{L^2}^2\le C Q_i.
\tag{H}
\]

On a bounded-curvature plateau define the nonnegative operator

\[
 \mathscr A_i=W_i^++\sqrt{\frac23}|W_i^+|I_{\Lambda^+}\ge0.
\]

The corrected deficit decomposition plus bounded plateau curvature gives

\[
 \int_{P_i}\langle\mathscr A_iH_i,H_i\rangle\le C(K)Q_i.
\tag{L}
\]

Thus one convenient joint chart-selection density is

\[
\begin{aligned}
 \mathcal D_i={}&|E_i|^2+
 \left(q_i^+-\frac92\right)^2+
 \left(|2\pi H_i|-\frac{q_i^+}{3\sqrt2}\right)^2\\
 &+2\langle\mathscr A_iH_i,H_i\rangle.
\end{aligned}
\tag{D}
\]

Its integral tends to zero whenever the terminal global defect energy does. Apply (A) with `F=D_i`. On the selected noncollapsed pullback chart, smooth metric compactness and interior Hodge estimates produce a limiting self-dual harmonic form `H_infty`. The amplitude terms give

\[
 |H_\infty|=\frac{3}{4\sqrt2\pi}>0,
\]

while (L) gives `A_infty H_infty=0`. Together with the calibrated Weyl modulus, this forces

\[
 \operatorname{Spec}(W_\infty^+)=(-1/6,1/12,1/12).
\]

This supplies the Step 6 forbidden Einstein germ without a rank-drop or CFG accessibility theorem. It remains conditional on the unresolved smoothing/terminal-defect bridge and on sufficient positive-time regularity.

## 5. Current mathematical status

Established in this line:

- the metric-by-metric `7/24` calibration inequality;
- exact homogeneity and integrated defect-energy structure for the cutoff flow;
- the corrected support-scale requirement;
- the exponential-pullback averaging lemma, independent of collapse and sheet multiplicity;
- a positive-part rescaled-monopole repair and a finite nonnegative density that jointly selects amplitude and lowest-eigenline saturation once terminal `L^2` defect and bounded geometry are available;
- the local projector/Derdzinski forbidden germ from Step 6.

Unresolved:

- a transition-inclusive cutoff-flow existence and continuation theorem from the actual collapsed initial data, jointly preserving Sobolev geometry, cutoff derivatives, local normalized curvature energy, metric equivalence, and global `L^2` defect;
- production of a positive-volume uniformly buffered bounded-curvature plateau with positive-time derivative estimates;
- all dimension-only quantifiers of Yau Problem 26, the positive normalized branch, dimensions at least five, and Lean formalization.

The exponential-chart lemma removes an unnecessary collapse-classification prerequisite. It does not repair the missing parabolic theorem and therefore does not establish a fixed-topology gap by itself.

## Evidence paths

- Step 14 cutoff identity: `workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md`
- Step 15 calibration: `workspace/notes/step15_L2_chain_and_separated_demands.md`
- Quantitative monopole deficits: `workspace/codex_loop/work/quantitative_deficit_analysis.md`
- A01 independent correction: `Sessions/S0910A01/workspace/notes/step16_preceptor_review_smoothing_architecture.md`
- TTCS exponential averaging: `trace/ttcs/results/step16_ttcs01_verifier1_integration.md`
- TTCS chart density: `trace/ttcs/results/step16_ttcs01_verifier2_integration.md`
- TTCS positive-weight repair: `trace/ttcs/results/step16_ttcs02_generator1_integration.md`
- TTCS coupled cutoff review: `trace/ttcs/results/step16_ttcs02_verifier1_integration.md`

## 6. Additional source check on the continuation circle

Direct reading of Wang's local-flow paper confirms that the missing continuation package is not already hidden in its extension discussion. Proposition 4.9 obtains evolving Sobolev and cutoff-gradient bounds only after assuming a uniform weighted pointwise curvature bound `|chi^2 Rm|_infty`. Lemma 4.11 explicitly notes that `nabla^2 chi` and `nabla(chi^2 Rm)` evolve in a coupled way. The critical-energy computation near lines 681--703 propagates energy and obtains weighted pointwise curvature under a **global** Sobolev inequality and a global full-support `L^{n/2}` curvature threshold (Theorem 6.3), together with an `L^p` Ricci input. These are stronger than the collapsed relative-ball hypotheses here. Thus a new bounded-overlap relative-Sobolev version must genuinely resolve the simultaneous metric/Sobolev/cutoff-Hessian/weighted-curvature continuation circle; it cannot be cited from this source without a new proof.

The finite-dimensional algebra for the `q^+` repair was independently encoded in `workspace/scripts/verify_positive_part_monopole_algebra.py`. It checks the regularized functional bound, polynomial-division identity, corrected exact deficit decomposition with `N_f`, negative-part control, and limiting amplitude; the script exits successfully. As with the earlier scripts, this verifies algebra only, not the Seiberg--Witten existence input or analytic passage to a chart limit.

**Notation warning.** In Section 4, `q_i=sqrt(6)|W_i^+|-s_i` is the positive scalar--Weyl weight from the monopole argument. This is not the Step 15 trace variable `s_i+4`; the latter is denoted `tr E_i` here.

## 7. Promising way to break the metric-equivalence circle

Wang's quoted Deane Yang estimate suggests a specific construction rather than merely assuming the integrable weighted defect bound. For the usual local Ricci flow it has the form

\[
 \|\chi^2\operatorname{Ric}(t)\|_\infty
 \lesssim A_0^{n/p}t^{-n/(2p)}\|\operatorname{Ric}(0)\|_{L^p},
 \qquad p>n/2.
\]

A transition-inclusive adaptation to the homogeneous defect equation should aim for, in four dimensions,

\[
 \|aE(t)\|_\infty
 \le C_p\,\delta\left(\frac{r^2}{t}\right)^{2/p},
 \qquad p>2.
\tag{M_p}
\]

The collapse factor cancels on a relative-Sobolev ball: in norm form the local Sobolev coefficient scales as `A_0 ~ r Vol(B_r)^(-1/4)`, while `||E(0)||_p <= delta Vol(B_r)^(1/p)`, so

\[
 A_0^{4/p}\|E(0)\|_p
 \lesssim \delta r^{4/p}.
\]

Thus `(M_p)` has the correct scale and its time singularity is integrable precisely because `p>2`; over `t<=theta r^2` it would give metric drift `O(delta r^2)`, uniformly under collapse. This could establish metric equivalence early enough to preserve the relative Sobolev cover and then close the coupled energies. It is not supplied by the source: one must derive the weighted `aE` Moser inequality for the normalized cutoff equation on the entire active support, including cutoff terms and finite-neighbor summation. But it is a sharper construction target than assuming metric equivalence as an independent bootstrap input.
