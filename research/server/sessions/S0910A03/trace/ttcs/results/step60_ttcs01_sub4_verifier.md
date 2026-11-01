# TTCS Independent Branch Record

```json
{
  "step_id": 60,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step56_common_time_and_terminal_compactness.md",
    "Sessions/S0910A03/workspace/notes/step43_terminal_density_G_lemma.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A01/workspace/notes/step54_first_exit_continuation_derivation.md",
    "Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md"
  ]
}
```

## Task

Audit the terminal chart argument for the restricted four-dimensional Ishida–LeBrun route. Starting from Vol_T(P)≥cA, ∫𝔇_T≤Cδ²A (q_top≥0), uniform curvature on buffered plateau regions, and exponential-pullback ball averaging, verify the exact selection-and-limit chain: Liouville/Fubini inequality over p∈P, a selected pullback ball with mean density O(δ²), Rauch noncollapse and harmonic coordinates, strong W^{2,q}_loc convergence, and passage of the nonnegative density to zero on the whole limiting ball, sufficient for the calibrated-spectrum projector contradiction. Flag any flaw in claiming curvature convergence or pointwise vanishing from W^{2,q}; propose the minimal rigorous replacement if necessary. Also verify that A cancels and the resulting restricted conclusion is exclusion of sufficiently negative-pinched input metrics on a family already known to admit no Einstein metric—not merely exclusion of λ=-1 output metrics.

## Output

# Verification Memo: Terminal Chart Argument for the Restricted 4D Ishida–LeBrun Route

Prepared in a clean context. I read Step 56 (common observation time + terminal compactness), Step 54/55 (first-exit and continuation), Step 43 (terminal spectral density), and Step 6 (constant-spectrum projector lemma). Below I trace the exact selection-and-limit chain you named, verify what holds, isolate where the density-passage argument is stated imprecisely, give the minimal rigorous replacement, confirm the $A$-cancellation, and characterize the restricted conclusion precisely.

## 1. Summary

The terminal chart chain is essentially correct and the $W^{2,q}$ concern is a phrasing matter with a clean repair already half-present in the notes. The pointwise vanishing of $\Phi_\infty$ must be obtained from **smoothness of the limit metric**, never from pointwise convergence of the sequence's curvature. One reformulation is advisable: harmonic-chart existence should be run from the injectivity radius **at the center** of the exponential pullback ball (Jost–Karcher), not from whole-ball volume noncollapse. The projector contradiction is numerically sound. $A$ cancels cleanly, conditional on two geography inputs (calibrated volume comparison and proportional inner volume) that live upstream of the terminal chart. The restricted conclusion is a family-uniform quantitative gap around the $\mathrm{Ric}=-g$ equation for candidate **input** metrics — genuinely stronger than the known nonexistence of an exact $\lambda=-1$ Einstein metric, and distinct from Yau 26's wide two-sided pinch.

## 2. Selection inequality and the $O(\delta^2)$ pullback ball

The chain is: $\int_{P^{\rm in}} \mathcal A_\rho\Phi(p)\,d\mu(p)\le C\int_M\Phi \le 119C\,Q(T)$, then divide by $\mathrm{Vol}(P^{\rm in})\ge c_0 A$.

- The averaging bound $\int_{P^{\rm in}}\mathcal A_\rho\Phi \le C\int_M\Phi$ (Step 53 §7.2) is a Fubini/integral-geometry statement on the unit tangent bundle, using geodesic-flow invariance of Liouville measure. Structurally this is the correct device to avoid $\exp_p$ injectivity, so folding under collapse does not inject a multiplicity. The one thing that must be true for the family conclusion is that the constant $C$ depends only on $\rho$ and the fixed geometry, **not** on the injectivity radius or the collapse profile of $g(T)$. The Liouville formulation is designed to deliver exactly this; I did not see the constant re-derived in the supplied files, so its independence of collapse should be read directly out of Step 53.

- The upper bound $\int_M\Phi \le 119\,Q(T)$ requires $q_{\rm top}\ge 0$ (Step 43, eq. 5.5 with the $912\pi^2(-q_{\rm top})_+$ term dropped). I checked the internal algebra of Step 43 and it holds (details in §5 below).

- Division gives some $p$ with $\mathcal A_\rho\Phi(p)\le C\delta^2 A/(c_0 A)=C\delta^2/c_0$. This is the promised $O(\delta^2)$ selected ball.

## 3. Rauch noncollapse and harmonic charts — one reformulation

The note derives chart existence from the whole-ball pullback volume bound (4.3): $\mathrm{Vol}_{\tilde g}(\mathcal B_\rho)\ge v_0$. This whole-ball bound is true and is the right object for the noncollapse **statement**, but it is not the operative hypothesis for Anderson-type harmonic-coordinate existence, which in general wants volume noncollapse of sub-balls $B_\sigma(x)$ at interior $x$ — and that is exactly what collapse can spoil.

The correct and cleaner input is the **injectivity radius at the center**. On the exponential pullback ball $(\mathcal B_\rho(p),\tilde g_p)$ with $\tilde g_p=(\exp_p)^*g(T)$:

- Radial $\tilde g_p$-geodesics from $0$ are the straight rays $t\mapsto tv$; distinct rays meet only at $0$, so there is no $\tilde g_p$-geodesic loop through $0$ inside $\mathcal B_\rho$.
- Conjugate radius $\ge \pi/\sqrt{K}$ by Rauch under $|\mathrm{Rm}_{\tilde g}|\le K$.

Hence $\mathrm{inj}_{\tilde g_p}(0)\ge \min(\rho,\pi/\sqrt K)$. Jost–Karcher / Anderson then give harmonic coordinates on a definite ball about $0$ with $C^{1,\alpha}$ bounds depending only on $K$, that injectivity radius, and $n$ — using only the **center** injectivity radius plus the curvature bound on the ball. This is precisely the geometry that survives collapse (the flat-cylinder model unwraps to a genuinely noncollapsed flat pullback ball), so the mechanism is real; only the stated hypothesis should be shifted from "whole-ball volume" to "center injectivity radius." The extracted limit lives on a definite ball, which is all the germ contradiction needs.

## 4. Passage of the density to zero on the limit ball — the flagged step and its repair

The sentence in Step 56 §4.4 — "$W^{2,q}$ convergence is sufficient … because the calibrated density $\Phi$ involves only curvature algebraic quantities, which converge under $W^{2,q}$" — is where the reasoning is stated too loosely. Two things it should not be read to assert:

1. **Pointwise curvature convergence of the sequence.** $g_i\to g_\infty$ in $W^{2,q}_{\rm loc}$ means $\partial^2 g_i\to\partial^2 g_\infty$ in $L^q$, so curvature converges only in $L^q$, not pointwise. Curvature of $g_i$ is not even continuous in general.
2. **Pointwise vanishing of $\Phi$ from sequence convergence.** One cannot pass $\Phi_i\to 0$ pointwise.

The rigorous chain, which the notes partly contain, is:

- **(a) $L^1$ convergence of the density.** Strong $W^{2,q}_{\rm loc}$ ($q\ge 2$) gives curvature $\to$ in $L^q_{\rm loc}$, and $\Phi$ is quadratic in curvature, so $\Phi_i\to\Phi_\infty$ in $L^{q/2}_{\rm loc}\subset L^1_{\rm loc}$.
- **(b) Zero integral.** The selected mean gives $\int_{\mathcal B_\rho}\Phi_i\to 0$, hence $\int_{\mathcal B_\rho}\Phi_\infty=0$.
- **(c) Smoothness of the limit.** $g_\infty$ solves $\mathrm{Ric}_\infty=-g_\infty$ weakly; in harmonic coordinates the Einstein system $g^{ab}\partial_a\partial_b g_{ij}=2g_{ij}+Q(g,\partial g)$ has smooth nonlinearity, so $W^{2,q}\Rightarrow C^{1,\alpha}\Rightarrow C^\infty$ (DeTurck–Kazdan even gives analyticity). Thus $\Phi_\infty$ is continuous.
- **(d) Everywhere vanishing.** A continuous nonnegative $\Phi_\infty$ with zero integral is $\equiv 0$ on the whole ball.

So the pointwise, everywhere vanishing on the limit ball comes from **step (c) smoothness**, not from convergence of the sequence. This is the minimal rigorous replacement and it makes the "whole limiting ball" conclusion correct. I recommend the summary sentence be rewritten to state exactly (a)–(d).

Two supporting points I checked:

- **Strong $W^{2,q}$ is genuinely available** (not merely weak). Writing the harmonic-coordinate Ricci equation for the difference $g_i-g_j$, the right side converges in $L^q$ (using $E_i\to 0$ in $L^q$, which follows from $\int|E_i|^2\to 0$ interpolated against the uniform $L^\infty$ curvature bound), and the coefficient differences $g_i^{ab}-g_j^{ab}\to 0$ in $C^0$ multiply an $L^q$-bounded $\partial^2 g$; interior $L^q$ estimates then make $\{g_i\}$ Cauchy in $W^{2,q}_{\rm loc}$. This is the standard elliptic difference argument and it is valid here.
- **$E_\infty=0$ is secure.** From strong $W^{2,q}$, $E_i=\mathrm{Ric}_i+g_i\to E_\infty$ in $L^2$, and $\int_{\mathcal B_\rho}|E_i|^2\to 0$ forces $E_\infty=0$, i.e. $\mathrm{Ric}_\infty=-g_\infty$ exactly. (A weak-lower-semicontinuity shortcut delivers $E_\infty=0$ and $(s_\infty+4)=0$ from weak $W^{2,2}$ alone, but the $(s+8\sqrt6|W^+|)^2$ and $G$ terms are not convex in $\partial^2 g$ where their arguments change sign, so weak lsc does not close those; the strong-convergence route the notes take is the appropriate one and should be retained.)

## 5. The calibrated-spectrum projector contradiction — verified

I checked the arithmetic of the forbidden germ end to end.

- $\Phi_\infty=0$ forces $E_\infty=0$, $s_\infty=-4$, $s_\infty+8\sqrt6|W^+_\infty|=0\Rightarrow |W^+_\infty|=1/(2\sqrt6)$, $|W^+_\infty|^2=1/24$, and $G_\infty=0$.
- With $s=-4$, $|W^+|^2=1/24$: Step 43 Lemma 1.2 gives $f=-3$, $G=4\xi(3-\xi)$, so $G=0\Leftrightarrow\xi=0$, forcing $\mathrm{Spec}(W^+)=(-\tfrac16,\tfrac1{12},\tfrac1{12})$. Trace $=0$ ✓, $\sum\lambda^2=1/24$ ✓, $\det=-1/864$ ✓.
- Weitzenböck: with $|W^+|^2$ constant, $0=2|\nabla W^+|^2+s|W^+|^2-36\det W^+ = 2|\nabla W^+|^2 -4\cdot\tfrac1{24}+36\cdot\tfrac1{864}=2|\nabla W^+|^2-\tfrac18$, so $|\nabla W^+|^2=1/16$ (matches Step 6 eq. 4).
- Constant-spectrum lemma (Step 6 §2): Einstein $\Rightarrow \delta W^+=0$; two distinct constant eigenvalues $\Rightarrow \nabla W^+=0$. The internal computation ($\nabla^a\omega_{ab}=0$ then $\nabla\omega=0$ via nondegeneracy of a self-dual 2-form) is correct and matches Derdziński Prop. 5.
- $|\nabla W^+|^2=1/16$ versus $\nabla W^+=0$ is the contradiction. Equivalently, Derdziński forces the germ locally Kähler; a Kähler–Einstein metric with $s=-4$ has $\mathrm{Spec}(W^+)=(-\tfrac23,\tfrac13,\tfrac13)$, $|W^+|^2=2/3\ne1/24$. Both phrasings are consistent.

I also confirmed the supporting algebra of Step 43: the identity $27(s^2/24+2|W^+|^2)-(s-\sqrt6|W^+|)^2=\tfrac18(s+8\sqrt6|W^+|)^2$ holds exactly; $\mathrm{Ric}^\circ=E^\circ$ so $R\le Q/8\pi^2$; and $(s+4)^2=(\mathrm{tr}\,E)^2\le 4|E|^2$ since $\mathrm{tr}\,E=\langle E,g\rangle$ and $|g|=2$ in $n=4$. The nonnegativity Lemma 1.1 ($G\ge0$) is correct. So the SW-to-density link is internally sound; its one external dependency is LeBrun's spectral lower bound $\int(b_-)^2\ge 32\pi^2 p$ (the nonnegativity of $D_{\rm Yam}$ and $D_{\rm mono}$ in eq. 4.5'), which is a cited published inequality and should be matched against LeBrun's stated constant.

There is **no circularity** between the germ lower bound $\eta>0$ and the selection: the germ argument establishes that no near-critical sequence can have $\mathcal A_\rho\Phi(p_i)\to0$; the selection produces exactly such a sequence when $\delta_i\to0$; the two are the same object viewed from opposite ends, and their collision is the contradiction.

## 6. $A$-cancellation — verified, with its two upstream dependencies named

Tracing all $A$-dependence:

- Upper: $\int\Phi\le119\,Q(T)\le119\,e^{C\theta}Q(0)\le C\delta^2\,\mathrm{Vol}(M)\le C\delta^2 A$, using $Q(0)\le\delta^2\mathrm{Vol}(M)$ (pointwise $|E(0)|\lesssim\delta$) and $\mathrm{Vol}(M)/A\le C$.
- Lower: $\mathrm{Vol}(P^{\rm in})\ge c_0 A$.
- Selection: $\mathcal A_\rho\Phi(p)\le C\delta^2 A/(c_0 A)=C\delta^2/c_0$ — $A$ cancels.
- Germ: $\mathcal A_\rho\Phi(p)\ge\eta(K,\rho,v_0)>0$, independent of $A$.

The cancellation is valid provided two inputs are sequence-uniform and hold in the geography, neither of which is proved inside the terminal chart:
1. **Calibrated volume comparison** $\mathrm{Vol}(g_i)/A_i\le C$ (Step 6 §5 states $\mathrm{Vol}(g_i)\to 32\pi^2 A/9$; this uses the near-Einstein normalization and should be pinned to the actual sequence).
2. **Proportional inner volume** $\mathrm{Vol}(P^{\rm in})\ge c_0 A_i$ with $c_0$ geography-only (Step 45 §4).
Both are the mechanism by which "$A$ fixed / $A$-proportional" makes the deficits vanish absolutely; the notes themselves warn (Step 6 §4 close) that if topology varies with $A_i\to\infty$ the available errors are only $o(A_i)$ and a small noncollapsed island can absorb nonvanishing defect. So the family-uniform cancellation is tied to the fixed-geography setting, and the varying-topology case is measure-relative rather than absolute.

## 7. Input-versus-output character of the restricted conclusion

This is the point most worth stating precisely.

The conclusion (Step 56 §5.4) is: there is $\varepsilon>0$ (depending on the geography parameters $m,\{c_1^2(X_j)\},(2\chi+3\tau)(N)$) such that **no** smooth metric $g$ on $M$ satisfies $\|g^{-1}(\mathrm{Ric}_g+g)\|_{\infty,\rm op}<\varepsilon$.

- This is a statement about candidate **input** metrics $g$: it empties a definite pointwise operator-norm neighborhood of the equation $\mathrm{Ric}=-g$. It is strictly more than the already-known nonexistence of an exact $\lambda=-1$ Einstein metric, which is the single point $\varepsilon\to0$. So it is correctly described as "excluding sufficiently pinched input metrics," not "excluding $\lambda=-1$ output metrics." The nontrivial content is that $\varepsilon>0$ is family-uniform.

- The pinch it excludes is **narrow**: $\|g^{-1}(\mathrm{Ric}+g)\|_{\rm op}<\varepsilon$ means every Ricci eigenvalue lies in $(-1-\varepsilon,-1+\varepsilon)$ relative to $g$ — a two-sided pinch centered at $-1$ after scale normalization. This is far narrower than Yau 26's hypothesis $c_n g\le\mathrm{Ric}\le C_n g$ with dimension-only $c_n<C_n$, which permits a wide band and does not force $\mathrm{Ric}$ near any single $\lambda g$. Emptying the narrow band does not empty the wide band, so the restricted result neither establishes nor refutes Yau 26 on these manifolds; it is an obstruction result orthogonal to the theorem's implication.

- The essential work the germ mechanism does (beyond LeBrun's existing $L^2$ obstruction) is worth noting: a small **pointwise Ricci** defect $\|E\|_\infty<\varepsilon$ does not by itself violate LeBrun's $\int(s-\sqrt6|W^+|)^2\ge72\pi^2 A>0$, because a metric with $\mathrm{Ric}\approx-g$ may still carry large Weyl. It is the SW/Chern–Weil chain of Step 43 (using $q_{\rm top}\ge0$) that converts the small Ricci defect $Q$ into control of the Weyl-bearing terms $\int(s+8\sqrt6|W^+|)^2$ and $\int G$, and then the local germ upgrades the resulting $L^2$ smallness at a selected center into a pointwise contradiction. So the terminal chart is doing genuine work, and its dependence on $q_{\rm top}\ge0$ (to avoid the additive $912\pi^2(-q_{\rm top})_+$) is load-bearing.

## 8. What feeds the terminal chart but is not established inside it

The terminal chart itself is sound (with the §3–§4 reformulations). Its correctness is conditional on the imports it names, none of which is a curvature-convergence issue:

- Per-datum smooth existence and the common observation time $\theta r^2$ (Step 56 §2, from A03 Step 56 + the coupled $(\Gamma,V)$ bootstrap of Step 55). The uniqueness energy estimate (2.9) drops the degenerate dissipation $-\int\chi^2|\nabla h|^2$, which is legitimate, and controls $\int|\nabla\chi|^2|h|^2$ by $Q$-terms; this is fine as written.
- Curvature and defect Moser endpoints $\|aF_T\|_\infty\le C\Gamma/t$, $\|aE\|_\infty\le C_E\delta(r^2/t)^{1/3}$ (Modules B, C).
- The SW spectral density bound (Step 43), resting on LeBrun's published spectral lower bound.
- Calibrated volume and proportional inner volume (Step 45), the two inputs behind §6.
- Liouville averaging with a collapse-independent constant (Step 53).

## 9. Bottom line for the terminal chart

The selection $\to$ pullback ball $\to$ Rauch $\to$ harmonic coordinates $\to$ strong $W^{2,q}_{\rm loc}$ $\to$ smooth Einstein limit $\to$ everywhere-zero density $\to$ projector contradiction chain is correct once two edits are made: (i) chart existence phrased via center injectivity radius (Jost–Karcher) rather than whole-ball noncollapse; (ii) whole-ball vanishing of $\Phi_\infty$ obtained from $L^1$ convergence plus smoothness/continuity of the limit, never from sequence pointwise curvature convergence. $A$ cancels, conditional on the two Step 45 volume inputs. The resulting statement is a family-uniform quantitative gap around $\mathrm{Ric}=-g$ for input metrics — stronger than the known nonexistence, narrower than and orthogonal to Yau 26's two-sided pinch.