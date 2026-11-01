# TTCS Independent Branch Record

```json
{
  "step_id": 62,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step62_ttcs_assimilation_and_negative_branch_triage.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md",
    "Sessions/S0910A03/workspace/notes/step60_all_order_continuation_and_terminal_chart.md",
    "Sessions/S0910A01/workspace/notes/step56_common_time_and_terminal_compactness.md",
    "Sessions/S0910A01/workspace/notes/step58_all_order_continuation_proof.md"
  ]
}
```

## Task

Independently verify the current peer restricted negative Ishida--LeBrun/cutoff-flow chain for Yau Problem 26, using the supplied A01/A03 notes plus A02's Step-62 triage. Do not decide the full Yau-26 problem. Assess whether the chain, as written, plausibly proves a restricted four-dimensional negative-sign gap, and identify exact load-bearing gaps or scope limitations. Focus on: per-datum transported-cutoff DeTurck existence; low-order first-exit/Moser modules imported into common time; all-order continuation without ungauged uniqueness; terminal Liouville-pullback compactness and Derdzinski forbidden-germ contradiction; whether any conclusion gives dimension-only constants or a counterexample. Return a mathematical verification memo with concrete items A02 should audit next.

## Output

# Verification Memo: Restricted Four-Dimensional $\operatorname{Ric}\to -g$ Ishida–LeBrun / Cutoff-Flow Chain

To the core research agent. I read the four peer notes (A03 Step 56, A03 Step 60, A01 Step 56, A01 Step 58) and the A02 Step-62 triage, and independently reconstructed the parts I could check from first principles. Below I separate what I confirmed by direct computation, what is architecturally sound but rests on modules proved elsewhere, and the exact items whose correctness the whole restricted theorem depends on.

## 1. Overall status of the chain as written

The four notes assemble an internally coherent architecture for a single restricted statement: for a specified Ishida–LeBrun geography of four-manifolds already carrying no $\operatorname{Ric}=-g$ Einstein metric (monopole sign family, $q_{\rm top}\ge 0$, calibrated proportional volume), no input metric has Ricci spectrum inside $[-(1+\varepsilon_{\mathcal F}),-(1+\varepsilon_{\mathcal F})^{-1}]$ for a family-uniform $\varepsilon_{\mathcal F}>0$. The A02 triage description of this target is accurate: it is a proof-side pinching gap on a special family, not a construction, not dimension-only, and neither proves nor disproves Yau-26.

The machinery *present in these notes* — the all-order continuation, the autonomous jet-splice replacing ungauged uniqueness, the terminal Liouville selection, and the Derdzinski contradiction — is internally correct where I could check it. The *sequence-uniform heart* (base layer, the low-order first-exit/Moser inequalities, the Seiberg–Witten calibration, and the Derdzinski source) is imported from steps not contained in the supplied files. So the chain is, as written, a conditional theorem: correct connective tissue over a set of imported analytic and gauge-theoretic inputs that are not reproved here.

## 2. Per-datum transported-cutoff DeTurck existence (A03 Step 56)

I verified the two structural pieces that make this construction usable:

- **Pullback identity (5.3)–(5.4) is exact.** With $V_t=-\beta^2W$ and the Ricci–DeTurck algebra $-2\operatorname{Ric}(G)=G^{-1}D^2G+R+Q-\mathcal L_WG$, one gets $\partial_tG=-2\beta^2(\operatorname{Ric}(G)+G)+\mathcal L_{\beta^2W}G$, and $\partial_t(\varphi^*G)=\varphi^*(\partial_tG-\mathcal L_{\beta^2W}G)=-2(\beta\circ\varphi)^2(\operatorname{Ric}_g+g)$. Since transport gives $\beta\circ\varphi=\chi$, the geometric flow $\partial_tg=-2\chi^2(\operatorname{Ric}_g+g)$ follows. The DeTurck cross term $2\operatorname{sym}(d(\beta^2)\otimes W^\flat)$ is exactly the piece of $\mathcal L_{\beta^2W}G$ that survives, so the algebra closes.
- **Tame interpolation exponent (2.5a) is correct.** Gagliardo–Nirenberg between $H^m$ and $W^{4,\infty}$ with $\theta=(q-4)/(m-4)$ gives precisely $D^qu\in L^{2/\theta}$; the $\sum(q_i-4)\le m+2-4k$ bookkeeping yields $\sum\theta_i<1$ for $k\ge2$ high factors and $\theta_1\le1$ for one high factor. The requirement $s_0>n/2+4=6$, hence $s_0=7$, matches $H^7(M^4)\hookrightarrow C^{4,\alpha}$. The 14M-partition script indeed checks only this integer arithmetic, not the tensor identities.

The genuinely load-bearing items still needing direct examination:

1. **Regularized existence and continuation for (1.2), and the $(\varepsilon,\nu)\to0$ passage.** The uniform-in-$(\varepsilon,\nu)$ energy (3.2) controls $\|G\|_{H^m}$, but its dissipation $\int(\beta^2+\varepsilon)|D^{m+1}G|^2$ degenerates on the collar $\{\beta=0\}$. The argument that the diagonal limit solves (1.1) rather than a weak relaxation relies on the space-time $C^k$ convergence from (4.4)+(5.1). This is standard degenerate-parabolic practice, but the local existence theorem for the quasilinear system, the fixed-parameter continuation used at (4.3), and the preservation of $0\le\beta\le1$ under (1.2) (the maximum-principle sign of $\nu\bar\Delta\beta$ at extrema and the vanishing of transport at $D\beta=0$) should be checked line by line. The zero set of $\beta$ is preserved (the ODE $\beta\circ\varphi=\chi$), so the collar remains stationary in the limit; confirm that this stationarity is what the limiting equation actually enforces on the open set $\{a=0\}$.
2. **Per-datum, not sequence-uniform, lifespan.** The note is explicit and correct that $T_0=T_0(g_0,\chi,\bar g,s_0)$ depends on high Sobolev norms and cannot furnish the common time $\theta r^2$. The whole reach to $\theta r^2$ therefore rests entirely on the imported first-exit estimates (6.8), which this note does *not* reprove.

## 3. Base layer and low-order first-exit/Moser modules — the true imported heart

Everything downstream depends on the base layer
$$\|U\|_\infty=\|aT\|_\infty\le K_\tau,\qquad T_0,T_1,U_1,C_2\in L^q_x\ \ \forall q<\infty,$$
and on the sequence-uniform first-exit outputs $\|aF_T\|_\infty\le C\Gamma/t$, $\|aE\|_\infty\le C\delta(r^2/t)^{1/3}$, the $(\Gamma,V)$ bootstrap, and $Q$-propagation. None of these are proved in the supplied files (A01 Step 58 §3 attributes them to A03 Step 57, Steps 34–35, Step 55). Concrete items to examine directly:

1. **Unweighted $L^q$ control on the transition annulus.** $\|U\|_\infty=\|aT\|_\infty$ is genuinely controlled by the weighted endpoint, since $U=aT$. But the induction integrates *unweighted* $\|T_m\|_p^p$ over all of $M$, and the residuals (5.5), (6.2) require $T_0,T_1\in L^q$ globally. On the exact collar $\{a=0\}$ the metric is stationary $=g_0$, so $T_m=\nabla^mT(g_0)$ is fixed and smooth — fine. On the transition region $\{0<a<1\}$ the weighted endpoint gives only $|T|\le C\Gamma/(a\tau)$, which degenerates as $a\to0$. Whether $\int|T|^q$ and $\int|\nabla T|^q$ over the transition annulus are finite depends on the vanishing profile of $\chi$ and on the $W^{1,p}\to L^\infty$ bridge that produces the base layer. This is the precise point where the imported low-order module must be examined: confirm that the base-layer $L^q$ control genuinely holds across the transition annulus, not merely on $\{a\ge a_0>0\}$. If it holds only on the plateau/buffer, the unweighted energy inequalities (6.5) would need the transition contribution separately closed.
2. **Signed-Hessian absorption at low order.** The all-order notes absorb the current Hessian $\chi C_2*U_m$ using only $\|C_1\|_\infty\lesssim r^{-1}$ via one integration by parts (3.2), (5.10). The corresponding *low-order* $H_2$, $Y$, $J_6$, $Q_\alpha$ inequalities carrying the sequence-uniform constants must be checked to use the same single-cutoff-derivative mechanism and no $\|\nabla^2\chi\|_\infty$ constant, since sequence-uniformity of $\theta r^2$ hinges on this.
3. **The unweighted-$H_2$ point (A03 Step 56 §6.1).** The equivalence $1+|T|^2\asymp_n 1+|\operatorname{Rm}|^2$ and the unweighted $H_2^\alpha=\int\eta_\alpha^2F_T^2\,d\mu$ are the objects controlling curvature in small-$a$ collars. Verify that the initial bound (6.3) and its use in the Sobolev absorption survive without an inserted factor $a$.

## 4. All-order continuation without ungauged uniqueness (A03 Step 60 §4–§5, A01 Step 58 §7–§8)

I confirm the correction here is genuine and the replacement is sound:

- **The ungauged $L^2$ metric-difference estimate cannot be derived.** I reproduced the principal-symbol computation (4.2)–(4.4): with $\xi=e_1$, $h=\operatorname{diag}(1,-\varepsilon,0,0)$, the symbol is $a\,\operatorname{diag}(\varepsilon,\varepsilon,0,0)$ and $\langle\sigma_\xi(DF)h,h\rangle=\varepsilon-\varepsilon^2>0$. So the linearization is not coercive on $h=g_1-g_2$, and the earlier estimate (4.5) is correctly abandoned.
- **The autonomous jet-splice is valid.** If $g(t)\to g_*$ in $C^\infty$ as $t\uparrow T_*$, then because the equation is autonomous, both one-sided space-time derivatives of every order equal $\mathcal F_\ell(g_*)$, and the spliced $\widetilde g$ has continuous matching derivatives of all orders across $T_*$, hence is $C^\infty$. This uses no comparison of two solutions on an overlap. The reasoning is correct **conditional on genuine $C^\infty$ terminal convergence**, which is exactly the output of the all-order tower (§7) and therefore inherits the base-layer dependence of §3.
- **The induction starting at $m=2$ is correctly forced.** The circularity at $m=1$ (where $\|U_1\|_4$ in (5.7) is the current unknown) is real; the base layer must supply $U_1,T_1\in L^q$ independently. The stationarity test $T=U=0\Rightarrow$ stationary, removing fictitious $a\cdot1$ and $a^2$ forcing terms, and the exact identity $(B_1*B_1)*T=4(C_1*C_1)*U$ (2.4), are algebraically correct and eliminate the apparent unweighted current-$T$ factor.

The one structural point to examine: the family enumerations (2.1)–(2.6) / (4.4)–(4.5) are asserted exhaustive from the derivation, with the script checking only integer allocations through order 64. The mathematical argument that Leibniz + spatial commutator + time commutator + Ricci reordering produce no further derivative family (in particular that no bare $T_{m}$ or $C_{m+2}$/$U_{m+1}$ survives outside the displayed current terms) is the content; verify the reordering claim $\nabla^r(\partial_t\Gamma)=g^{-1}*U_{r+1}$ with reorder terms $T_q*U_{r-q}$, $q\le r-1$, since the whole triangular structure rests on the current-level factor being $U$ (weighted), never unweighted $T_m$.

## 5. Terminal Liouville-pullback compactness and Derdzinski contradiction

I checked the internal arithmetic of the endgame and it is consistent and, in fact, precisely tuned:

- **$A$-cancellation.** $\int\Phi\le C\delta^2A$ and $\operatorname{Vol}(P)\ge c_0A$, fed through the Liouville average (6.6) with Jacobian bounds $c_Rt^3\le j\le C_Rt^3$ and $\varphi_t^*dL=dL$, select $p_i$ with $\mathcal A_\rho\Phi(p_i)\le C\delta^2/c_0$, independent of $A$. The old $A^{-1/2}$ loss is genuinely removed.
- **Pullback (not image) ball noncollapse.** Using Rauch on the pullback ball in $T_{p}M$ handles a possibly collapsing manifold sequence without a global noncollapse hypothesis. This is the correct device.
- **The calibrated forbidden germ is arithmetically exact.** $\Phi=|E|^2+(s+4)^2+(s+8\sqrt6|W^+|)^2+\mathcal G$. $\Phi=0$ forces $\operatorname{Ric}=-g$, $s=-4$, and $|W^+|=1/(2\sqrt6)$, i.e. $|W^+|^2=1/24$; with $\mathcal G=0$ giving two equal eigenvalues, the spectrum is $(-1/6,1/12,1/12)$ (sum zero, norm $1/24$, simple eigenvalue extremal — the same sign pattern as a genuine $\operatorname{Ric}=-g$ Kähler germ). The conformal factor $(24|W^+|^2)^{1/3}=(24\cdot\tfrac1{24})^{1/3}=1$, so Derdzinski's normalized metric is $g_\infty$ itself, i.e. $g_\infty$ would be Kähler. But a Kähler germ with $\operatorname{Ric}=-g$, $s=-4$ has $|W^+|^2=s^2/24=2/3\ne1/24$. Contradiction. The calibration is evidently engineered so that $\Phi=0$ sits exactly at the Derdzinski Kähler threshold, which is strong internal evidence the constants ($8\sqrt6$, the $1/24$ threshold) are the intended ones.

Note that a genuine $\operatorname{Ric}=-g$ Kähler germ is *far* from the calibrated zero: $s+8\sqrt6|W^+|=-4+8\sqrt6\sqrt{2/3}=12$, so $\Phi\ge144$ there. This confirms the calibration targets the LeBrun optimal profile, not Kähler-Einstein, and the contradiction is that the optimal-profile Einstein germ cannot exist.

Items to check against sources (none in the supplied files):

1. **Exact Derdzinski statement and orientation.** The step "$\delta W^+=0$ + $W^+$ with a repeated eigenvalue (simple eigenvalue extremal) $\Rightarrow$ $g$ Kähler after conformal normalization" and its applicability to a *local* germ must be verified against Derdzinski's proposition, including the orientation convention that places the simple eigenvalue as extremal.
2. **The Seiberg–Witten calibration $\int\Phi\le 119\,Q$.** This is an *upper* bound on $\int\Phi$ by the Einstein defect, so the topological/monopole terms must cancel (this is where $q_{\rm top}\ge0$ and the monopole sign family enter). The constant $119$, the combination inside $\Phi$, and the direction of the inequality are load-bearing and cited to Step 45. Verify the sign and the cancellation, since the entire "near-Einstein $\Rightarrow$ small $\int\Phi$" logic depends on it.
3. **The spectral-gap density $\mathcal G$ and its convergence.** Confirm $\mathcal G=0\Leftrightarrow$ two equal $W^+$ eigenvalues, that $\mathcal G$ is Lipschitz/algebraic in $W^+$ so that $W^{2,q}$ curvature convergence gives $\mathcal G_i\to\mathcal G_\infty$ in $L^1_{\rm loc}$ (the note's distinction between $L^1$/$W^{2,q}$ convergence and pointwise convergence is handled correctly). Also cross-check the A03 §7 alternative endgame ("$\nabla W^+_\infty=0$ from constant spectrum" vs. "$|\nabla W^+_\infty|^2=1/16$ from the Einstein–Weyl identity"): "constant eigenvalues $\Rightarrow$ parallel $W^+$" is not automatic (eigenspaces can rotate), so verify the exact projector lemma. The A01 §4.5/§9 magnitude endgame ($1/24$ vs $2/3$) is cleaner and I recommend relying on it.

## 6. Relation to Yau-26, dimension-only constants, counterexample

I confirm the A02 reading. The output (8.1)/(8.2) is a family-uniform pinching gap around $\operatorname{Ric}=-g$; the constant $\varepsilon_{\mathcal F}$ depends on geography inputs $(c_0,K,\rho,$ calibration, first-exit constants$)$, not on $n$ alone (both notes state this). It constructs no metric, so it is not a counterexample to Yau-26. It also does not force Yau-26: Yau-26 permits a fixed possibly-wide dimension-only band $[c_n,C_n]$, whereas this result concerns arbitrarily tight pinning to $-1$ on a special no-Einstein family. The two statements are essentially orthogonal. Positive pinching, arbitrary four-manifold topology, $n\ge5$, dimension-only constants, and Lean formalization are untouched.

One relevant conceptual point: the no-Einstein topology enters *only* through the SW calibration $\int\Phi\le119Q$ and the proportional-volume estimate; the forbidden germ itself is a local Derdzinski statement. So the theorem's dependence on the geography is concentrated in item 5.2 above.

## 7. Concrete items to verify next, in dependency order

1. **Base-layer global $L^q$ control across the transition annulus $\{0<a<1\}$** (§3.1). This is the single foundation of the all-order induction and is imported. Determine whether $T_0,T_1\in L^q(M)$ (not just on $\{a\ge a_0\}$) with sequence-uniform-compatible constants.
2. **Low-order first-exit/Moser inequalities** ($H_2$, $Y$, $J_6$, $Q_\alpha$, $(\Gamma,V)$ bootstrap, $Q$-propagation), specifically the single-cutoff-derivative signed-Hessian absorptions and the unweighted-$H_2$ Sobolev step (§3.2–3.3). These carry the sequence-uniform $\theta r^2$.
3. **Regularized parabolic existence/continuation and the $(\varepsilon,\nu)\to0$ limit** for (1.2), including preservation of $0\le\beta\le1$ and that the limit solves (1.1) exactly on $\{a=0\}$ (§2).
4. **SW calibration $\int\Phi\le119\,Q$**: the sign, the topological cancellation under $q_{\rm top}\ge0$/monopole family, and the constant (§5.2).
5. **Derdzinski proposition** — exact hypotheses, orientation, applicability to a local germ, and the conformal normalization; plus the $\mathcal G$ definition and its convergence (§5.1, §5.3).
6. **Family exhaustiveness** of (2.1)–(2.6) at the derivation level (the reordering identity $\nabla^r\partial_t\Gamma=g^{-1}*U_{r+1}+\{T_q*U_{r-q}\}_{q\le r-1}$), independent of the integer-allocation script (§4).

Items confirmed correct by direct computation in this reading: the DeTurck pullback identity, the GN interpolation exponent, the non-coercivity symbol computation, the $A$-cancellation, and the calibrated-germ arithmetic including the Derdzinski threshold tuning. What remains unresolved from the supplied material is everything imported in items 1, 2, 4, 5 — these are precisely the sequence-uniform and gauge-theoretic inputs whose correctness would turn the present coherent architecture into a complete restricted theorem.