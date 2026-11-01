# TTCS Independent Branch Record

```json
{
  "step_id": 51,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step50_minimizer_entry_PS_noncollapsed_alternative.md",
    "Knowledge/objects/papers/Fourth-order-curvature-flows-and-geometric-applications--db88daa8ad64--7e5bf41704a0/object.md"
  ]
}
```

## Task

The active goal is a rigorous noncollapsed structure theorem for minimizing sequences of P(g)=∫|Ric°|² on closed four-manifolds. Read the Step-50 note and the cited Bour fourth-order-flow source. Scrutinize only Theorem 50.A/Lemma W: (i) scaling of the L2 gradient and the weight rho^4; (ii) whether a smoothed curvature scale with all asserted derivative bounds exists without injectivity/noncollapse; (iii) whether multiplying the fourth-order DeTurck flow by a fixed variable weight yields a uniform own-scale existence interval on possibly collapsed metrics; (iv) whether energy descent yields the stated global weighted L2 residual and enough local residual after rescaling; (v) whether the selected metric stays in or can be returned to the scalar -4 Yamabe slice without losing residual. Identify exactly what is proved, what is plausible but unwritten, and what is false. Give a corrected theorem statement with the weakest sufficient entrance hypothesis if the construction is not yet a theorem.

## Output

# Memo: Theorem 50.A and Lemma W (scale-adapted Palais–Smale entry)

## Summary

Three things are proved:

- the scaling identities;
- the energy-descent selection, for any fixed positive weight on any interval where the weighted DeTurck flow exists;
- the strong parabolicity of the weighted DeTurck system.

Three statements in Lemma W and Theorem 50.A are false as written:

- the derivative bounds on the smoothed scale \(\rho\) for orders \(j\ge4\), measured in \(g_0\);
- the uniform \(C^2\)-closeness \(\|\tilde g_t-\tilde g_0\|_{C^2}\le Ct^\theta\);
- the upper comparison \(r_g\le C\rho_{g_0}\) in 50.A(2).

The third error matters most. It is exactly the direction Theorem 50.B uses to turn the weighted residual into a residual at the selected metric's own scale.

The uniform-time existence in Lemma W is not routine. It is a rough-initial-data theorem for a fourth-order quasilinear system, and Bour's paper supplies none of it.

A repaired version holds under an explicit entrance hypothesis: a uniform own-scale Hölder modulus of the curvature of \(g_0\). The ripple example in §4 shows that some such modulus is necessary for the one-step construction.

---

## 1. Scaling of the gradient and of the weight (item i)

The note's identities are correct.

**Gradient scaling.** From \(P(\lambda^2g)=P(g)\) and \(P'_g(h)=\int\langle\nabla P,h\rangle_g\,d\mu_g\), one gets \(\nabla P(\lambda^2 g)=\lambda^{-2}\nabla P(g)\) as a \((0,2)\)-tensor. Then
\[
|\nabla P|^2_{\lambda^2g}\,d\mu_{\lambda^2g}=\lambda^{-4}|\nabla P|^2_g\,d\mu_g,
\]
so \(\rho^4|\nabla P|^2d\mu\) is dilation-invariant when \(\rho\) scales like length.

**Time scaling.** For \(\partial_tg=-\nabla P(g)\), setting \(\hat g=\lambda^2g\) requires \(\hat t=\lambda^{4}t\). Hence the weight \(w=\rho^4\) gives unit flow time at every own scale. This is the correct parabolic normalization.

**Energy identity.** It holds for the DeTurck-modified system itself:
\[
\frac{d}{dt}P(g_t)=\int\langle\nabla P,-w\nabla P+\mathcal L_{X}g\rangle\,d\mu=-\int w|\nabla P|^2\,d\mu,\qquad X=wV.
\]
The term \(\int\langle\nabla P,\mathcal L_Xg\rangle\) vanishes because \(P\) is diffeomorphism-invariant and \(X\) is a vector field. No pull-back to an undeformed flow is needed. The selected metric can simply be the DeTurck solution \(\tilde g_{t_*}\), so "isotopic through the flow" is harmless but unnecessary.

**Two small corrections.**

- In 50.B the local conversion constant is \(16C^4\), not \(16\), where \(C\) is the comparability constant of 50.A(2).
- The weighted flow does not preserve volume. By Bour, \(P=2\mathcal F^{1}\) and \(\operatorname{tr}\nabla\mathcal F^\alpha=\frac\alpha4\Delta R\), so \(\operatorname{tr}\nabla P=\tfrac12\Delta R\) and
\[
\partial_t\mathrm{Vol}=-\tfrac14\int w\,\Delta R\,d\mu\neq0 .
\]
  This is harmless, since \(P\) is scale-invariant and (NC) survives through metric equivalence. The "Vol = 1" in the output is a renormalization.

**Bour-class membership.** This is confirmed. \(P=\mathcal F_{\rm Ric}-\frac14\mathcal F_R\) is Bour's class \(E_P\) with \(a=b=0\).

A reading note on the source: in the Mathpix text the symbol "\(\mathcal F_{\rm Ric}\)" inside \(\mathcal F^\alpha\) and the Gauss–Bonnet display must be read as \(\mathcal F_{\mathring{\rm Ric}}\). Only that reading reproduces Bour's equivalence \(\mathcal F^\alpha\le(1-\alpha)8\pi^2\chi\iff\int|\mathring{\rm Ric}|^2\le\frac{1-\alpha}{12}\int R^2\).

---

## 2. The smoothed curvature scale (item ii)

**Proved.** \(r_g\) is 1-Lipschitz. If \(d(x,y)=\delta\), then \(B(y,r_g(x)-\delta)\subset B(x,r_g(x))\), which gives \(r_g(y)\ge r_g(x)-\delta\).

**The construction as written does not produce a function on \(M\).** A function mollified in a chart pulled back to a tangent ball is not invariant under the local pseudogroup of the collapsed geometry, so it does not descend to \(M\). Any smoothing must be intrinsic: defined on \(M\) by a geometric operation, with estimates proved on lifts.

**The bounds \(|\nabla^j\log\rho|_{\rho^{-2}g_0}\le C_j\) are false for \(j\ge4\) with constants independent of \(g_0\).** The obstruction is the fourth-order Ricci identity applied to \(f=\log\rho\):
\[
\nabla_a\nabla_b\nabla_c\nabla_df-\nabla_a\nabla_c\nabla_b\nabla_df=-(\nabla_aR_{bcd}{}^{e})\nabla_ef-R_{bcd}{}^e\nabla_a\nabla_ef .
\]
Hence, in units of \(\rho\),
\[
|(\nabla_a R_{bcde})\nabla^ef|\le 2|\nabla^4f|+|\mathrm{Rm}||\nabla^2f| .
\]
Now take \(g_0\) whose own scale varies by a factor of 8 over a unit \(\tilde g_0\)-distance (any curvature concentration point does this). Then \(|\nabla\log\rho|_{\tilde g_0}\ge c\) on an open set. Superpose there a high-frequency ripple \(\delta g=\lambda^{2+\theta}\psi(x/\lambda)\) with \(0<\theta<1\), with ripples in all four coordinate directions. The ripple has \(|\mathrm{Rm}_{\rm ripple}|\sim\lambda^\theta\to0\), so \(r_{g_0}\) is unchanged. It has \(|\nabla\mathrm{Rm}(\cdot,\cdot,\cdot,e)|\sim\lambda^{\theta-1}\to\infty\) for every unit \(e\). Then \(C_4\to\infty\).

Lemma W's proof needs \(\nabla^4\log\rho\): the error term \(\mathcal E\) in \(\rho^2\nabla P(\rho^2\tilde g)=\nabla P(\tilde g)+\mathcal E\) contains \(\nabla^2\) of \(\mathrm{Rm}(\rho^2\tilde g)\ni\nabla^2\log\rho\). So the conformal-variable proof is invalid as written.

**What can actually be obtained.**

1. *Orders \(j\le2\), plus a Hölder bound on \(\nabla^2\), with no injectivity bound.* Define \(\rho\) by an intrinsic elliptic equation with own-scale coefficients, for example
\[
u-\operatorname{div}(r^2\nabla u)=\log r ,
\]
   bootstrapped once with coefficient \(e^{2u}\). Estimates are proved on lifted balls. Lifted balls are noncollapsed under bounded curvature, and their harmonic coordinates have \(g\in C^{1,\alpha}\cap W^{2,p}\) with no first-order term in \(\Delta\). Schauder theory then gives \(\nabla^2u\in C^\alpha\).
   - The ceiling is \(j=2\): \(\nabla^3u\) contains \(\partial\Gamma\in L^p\) only.
   - The bound \(|u-\log r|\le C\) needs a Green-function decay estimate at own scale. This is plausible, since only a Ricci lower bound is needed locally, but it is unwritten.
2. *All orders, with respect to a smoothed background metric.* Rescale to \(\rho^{-2}g_0\), which has bounded curvature once \(\rho\in C^2\) at own scale. Run Ricci flow for unit time. Shi's existence and estimates use the maximum principle and need no injectivity radius, so collapse is allowed. This yields \(\hat g\) with \(|\nabla^k\mathrm{Rm}|\le C_k\). Since \(|\partial_t\Gamma|\lesssim t^{-1/2}\), \(\hat g\) is \(C^1\)-close to \(\rho^{-2}g_0\).
   - Re-smooth \(\rho\) with respect to \(\hat g\) and set \(\bar g=\rho^2\hat g\).
   - Then \(\bar g\) is comparable to \(g_0\) and has own-scale bounded geometry of every order. The Ricci-identity obstruction does not apply, because derivatives are now taken in \(\bar g\).

This is plausible but unwritten. It is the correct form of (ii): derivative bounds of all orders exist for \((\rho,\bar g)\), not for \((\rho,g_0)\).

---

## 3. The weighted DeTurck flow (item iii)

**Proved.**

- Linearizing \(-w\nabla P(g)+\mathcal L_{wV}g\) gives principal symbol \(w\cdot(-\tfrac12|\xi|^4\mathrm{Id})\). This is Bour Prop. 2.4 with \(a=0\).
- The \(dw\otimes V\) terms have order 3.
- So the system is strongly parabolic, and on a closed \(M\) with smooth \(w>0\) it has a unique smooth solution on some \([0,T(g_0,w))\), by Bour Prop. 2.1 and MM10.

Diffeomorphism-naturality is lost, since \(\phi^*(w\nabla P(g))=(w\circ\phi)\nabla P(\phi^*g)\). By §1 this does no harm.

**Not supplied by Bour, and not routine.** Bour gives four things, none of which is a uniform existence time:

- Thm 1.4: the existence time depends on \(g_0\) in high norms, through MM10.
- Thm 1.5: Bando–Bernstein–Shi-type (BBS) estimates that presuppose \(\|\mathrm{Rm}\|_\infty\le D\) on the whole interval.
- Prop 9.21: the conversion to \(C^0\) needs the Sobolev constant \(\mathcal B_A\), which Prop 5.3 ties to noncollapse.
- Prop 5.6: Bour's only source of noncollapse is \(\inf Y>0\), which is unavailable at \(\alpha=1\) (Bour notes Thm 1.11 is empty there) and for every \(Y<0\) manifold in this project.

There is also no fourth-order maximum principle, so Shi's doubling-time argument does not transfer. In \(L^\infty\), \(|\partial_t\mathrm{Rm}|\sim|\nabla^4\mathrm{Rm}|\sim t^{-1}\) is not integrable.

**Three concrete defects in Lemma W.**

1. *The conformal variable.* Use constant rescalings by \(\rho(x)^2\) on lifted unit balls instead. The equation becomes \(\partial_t\hat g=-a\nabla P(\hat g)+\mathcal L_{aV}\hat g\) with \(a=(\rho/\rho(x))^4\in[C^{-1},C]\). This needs only \(w\in C^{1,\alpha}\) at own scale, which §2.1 provides.
2. *The DeTurck background.* With background \(g_0\), the field \(V=-\Delta\gamma_{g,g_0}-\frac14\nabla R\) carries \(\partial^3g_0\), and \(\mathcal L_Vg\) carries \(\partial^4g_0\). These are unbounded at own scale for general \(g_0\). The background must be the smoothed \(\bar g\) of §2.2.
3. *The asserted closeness.* \(\|\tilde g_t-\tilde g_0\|_{C^2}\le Ct^\theta\) is false. Take a ripple of rescaled wavelength \(\sqrt a\ll1\) with curvature amplitude \(O(1)\). Its Fourier mode decays like \(e^{-t/2a^2}\), so \(|\mathrm{Rm}(t)-\mathrm{Rm}(0)|\sim1\) for \(t\gg a^2\), with no uniform \(C\). What can hold is \(C^{1,\beta}\)- or \(C^0\)-closeness \(\le Ct^\theta\), together with \(|\mathrm{Rm}_{g_t}|\le C\rho^{-2}\).

**What remains unwritten.** Lemma W then reduces to the following statement:

> Uniform-time existence for the weighted DeTurck system with smooth background and weight, from initial data that are only \(C^{1,\alpha}\cap W^{2,p}\) at own scale (\(p>2\), which is subcritical in 4D), with \(t^{-k/4}\) smoothing.

Collapse is plausibly harmless here: the solution on \(M\) lifts to a solution on tangent balls, and lifted balls are noncollapsed, so localized energy and Sobolev estimates hold there. The far-field cutoff terms need a uniformly-local norm (a supremum over lifted balls), closed by continuation. This is a genuine theorem to prove, not a routine adaptation.

The phrase "all derivatives, by the choice of \(\rho\) and \(t\ge c_0/2\) smoothing" in the proof is circular: it uses the smoothing to obtain the existence time.

---

## 4. Energy descent and the local residual (item iv)

**Proved.** Given existence on \([0,T]\), there is \(t_*\in[T/2,T]\) with
\[
\int w|\nabla P(g_{t_*})|^2\,d\mu\le \frac2T\bigl(P(g_{T/2})-P(g_T)\bigr)\le\frac2T\bigl(P(g_0)-\alpha(M)\bigr).
\]
This holds for any positive weight.

**False: the upper comparison \(r_{g}\le C\rho_{g_0}\).** The ripple of §3, or a crease sheet of thickness \(\tau\ll r\), gives \(r_{g_0}\sim r\) at negligible cost in \(P\). For the sheet, \(\int_{B(r)}|\mathrm{Rm}|^2\sim\tau/r\), so it can be added to any minimizing sequence. After unit local time the flow spreads it and \(r_g\gg\rho_{g_0}\) there.

**Why this breaks 50.B.** In 50.B, point-picking runs on \(r_{g'}\), and one needs \(\rho_{g_0}\ge c\,r_{g'}(y)\) on \(B(y,A\,r_{g'}(y))\). That is precisely the false direction.

Picking on \(\rho_{g_0}\) instead does not help. The rescaled limit is then smooth, critical, small-energy and noncollapsed, so by Anderson's estimate it is flat. That only says \(r_{g'}(y)\gg\rho_{g_0}(y)\), which is consistent with the mismatch and gives no contradiction.

The lower comparison \(r_g\ge C^{-1}\rho_{g_0}\) is plausible, given Lemma W in its corrected form. Iterating the construction does not fix the mismatch: there is no monotone scale quantity, since each step can also shrink the scale by a factor \(2/c\).

**What 50.B actually needs.** Given (NC), it needs only the own-scale Palais–Smale (PS) residual
\[
\varepsilon_i:=\int_M r_{g_i}^4|\nabla P(g_i)|^2\,d\mu_{g_i}\to0\qquad(r\text{ capped at }1),
\]
with weight equal to the scale of the same metric. Own-scale derivative bounds can be dropped. The reason is as follows.

- Under (NC) and \(|\mathrm{Rm}|\le r^{-2}\), harmonic coordinates of radius \(cr\) exist (via Bour Lemma 5.4, rescaled).
- In harmonic gauge, \(\Delta\gamma\equiv0\), so
\[
-\nabla P=[P-\mathcal L_{-\Delta\gamma-\frac14\nabla R}](g)+\tfrac12\nabla^2R .
\]
- The resulting symbol is \(-\tfrac12|\xi|^4h+c\,\xi\otimes\xi\,\langle R_\xi,h\rangle\) with \(R_\xi=\xi\otimes\xi-|\xi|^2g\). It is injective: a kernel element must be \(h=\mu\,\xi\otimes\xi\), and \(\langle R_\xi,\xi\otimes\xi\rangle=0\) then forces \(\mu=0\).
- Bootstrapping from \(W^{2,p}\) (subcritical) with \(\nabla P=f\in L^2\) gives \(W^{4,2}\) bounds.
- These give strong \(W^{3,2}_{\rm loc}\) convergence, and \(\nabla P(g_\infty)=0\) as a weak limit, because \(\partial^4g\) enters linearly.

This step is needed. With only \(C^{1,\alpha}\) convergence, \(\mathrm{Rm}*\mathrm{Rm}\) does not pass to the limit, and local almost-minimality does not pass either, since \(|\mathring{\rm Ric}(g)|^2_{g+h}\) is quadratic in \(\mathring{\rm Ric}\). The elliptic bootstrap is plausible and short but unwritten.

---

## 5. The scalar-curvature −4 Yamabe slice (item v)

**The flow does not preserve the slice.** \(\partial_tR=R'(-w\nabla P)\neq0\) generically.

**Proved: returning to the slice keeps the sequence minimizing.** For \(Y_{[g]}\le0\), with Bour's normalization of \(Y\), Hölder's inequality gives
\[
Y\ge\inf_u\frac{\int\frac16Ru^2}{\|u\|_4^2}\ge-\tfrac16\|R\|_{L^2},
\]
so \(\int R^2\ge36Y^2\), with equality at the Yamabe metric (Bour Lemma 4.5). Combined with \(P=2\int|W|^2+\frac1{12}\int R^2-16\pi^2\chi\), this gives \(P(\hat g)\le P(g')\). Hence \(\inf_{\{s\equiv-4\}}P=\alpha\) on manifolds where every conformal class has \(Y<0\).

**The residual does not transfer.** Write \(\hat g=u^2g'\) with \(f=\log u\). Using \(\nabla P=2B+\frac16[\delta D(Rg)-R\mathring{\rm Ric}]\), \(B_{\hat g}=u^{-2}B_{g'}\), and \(u^{-2}R_{g'}=-4+6u^{-3}\nabla^\alpha\nabla_\alpha u\), the leading \(\mathring{\rm Ric}\) terms cancel and
\[
\nabla P(\hat g)-u^{-2}\nabla P(g')=u^{-3}(\nabla^\alpha\nabla_\alpha u)\mathring{\rm Ric}_{g'}-\tfrac43(\nabla^2f-df\otimes df)^\circ-\tfrac16u^{-2}\bigl(\Delta R_{g'}\,g'+\nabla^2R_{g'}\bigr).
\]
- These terms vanish only when \(u\) and \(R_{g'}\) are constant.
- Theorem 50.A controls only \(\operatorname{tr}\nabla P=\tfrac12\Delta R_{g'}\), and only locally at own scale. That does not control \(\nabla\log|R_{g'}|\) across necks or regions where \(R_{g'}>0\).
- The linearized Yamabe operator \(6\Delta+8\) at \(s=-4\) is coercive with unit-scale exponential decay, so the return is a local problem. The residual is therefore preserved when \(R_{g'}<0\), \(|R_{g'}|\gtrsim r^{-2}\), and \(r|\nabla\log|R||\) and \(r^2|\nabla^2\log|R||\) are small in own-scale \(L^2\). It is not preserved in general.

The slice is not used in 50.B or 50.C. It enters only the §6–7 bookkeeping, where the \(P\)-decrease is the relevant fact.

---

## 6. Status of each statement

| Statement | Status |
|---|---|
| Gradient scaling and the weight \(\rho^4\); fourth-order time scaling | proved |
| Energy identity for the weighted DeTurck system; mean-value selection | proved, given existence |
| Strong parabolicity; short-time existence for fixed \(g_0,w\) | proved (Bour 2.1/2.4 + MM10) |
| \(r_g\) is 1-Lipschitz | proved |
| Smoothed \(\rho\) with \(j\le2\) plus Hölder, intrinsic, collapse allowed | plausible, unwritten |
| \(\rho,\bar g\) with all orders relative to \(\bar g\) (Shi on \(\rho^{-2}g_0\)) | plausible, unwritten |
| \(|\nabla^j\log\rho|_{g_0}\le C_j\) for \(j\ge4\) | false (Ricci-identity ripple) |
| Lemma W proof via the conformal variable \(\tilde g=\rho^{-2}g\) | invalid (needs \(\nabla^4\log\rho\); background \(g_0\) injects \(\partial^4g_0\)) |
| Uniform own-scale existence time from rough data | open analytic theorem; Bour supplies none of it |
| \(\|\tilde g_t-\tilde g_0\|_{C^2}\le Ct^\theta\) | false; \(C^{1,\beta}\) or \(C^0\) version plausible |
| \(r_g\ge C^{-1}\rho_{g_0}\) | plausible, given corrected Lemma W |
| \(r_g\le C\rho_{g_0}\) | false for general \(g_0\), at negligible \(P\)-cost |
| Local own-scale residual in 50.B | not justified (rests on the false comparison) |
| Derivative bounds needed in the 50.B limit | not needed: elliptic bootstrap in harmonic gauge (plausible) |
| Return to slice keeps the minimizing property | proved (\(Y\le0\), Hölder) |
| Return to slice keeps the residual | false in general; holds under the stated conditions on \(R_{g'}\) |

---

## 7. Corrected statements

**Theorem 50.A₀ (proved).** Let \(g_0\) and \(w>0\) be smooth on a closed \(M^4\), and let \(\bar g\) be any smooth background. The system
\[
\partial_tg=-w\nabla P(g)+\mathcal L_{wV_{\bar g}(g)}g
\]
has a smooth solution on some \([0,T)\). For every \(T'<T\) there is \(t_*\in[T'/2,T']\) with \(P(g_{t_*})\le P(g_0)\) and
\[
\int w|\nabla P(g_{t_*})|^2\le \frac{2}{T'}\bigl(P(g_0)-\alpha(M)\bigr).
\]

**Entrance hypothesis \((H_{\beta,\Lambda})\).** For every \(x\), on the lifted \(g_0\)-ball of radius \(r_{g_0}(x)\), rescaled to unit size,
\[
[\mathrm{Rm}_{g_0}]_{C^\beta}\le\Lambda .
\]
That is, the curvature has a uniform own-scale Hölder modulus. The ripple and sheet examples show that a uniform own-scale modulus of continuity of \(\mathrm{Rm}\) is necessary for any one-step construction that preserves the scale in both directions. \(C^{\beta}\) is the weakest form that parabolic Schauder theory handles directly.

**Theorem 50.A_H (conditional on Lemma W′).** Assume \(\mathrm{Vol}(g_0)=1\) and \((H_{\beta,\Lambda})\). Then there is \(g\) with:

1. \(P(g)\le P(g_0)\);
2. \(C^{-1}g_0\le g\le Cg_0\) and \(C^{-1}r_{g_0}\le r_g\le Cr_{g_0}\);
3. \(|\nabla^k\mathrm{Rm}_g|\le C_kr_g^{-2-k}\);
4. \(\int r_g^4|\nabla P(g)|^2\le C\,(P(g_0)-\alpha)\).

The constants depend only on \(\beta\) and \(\Lambda\), not on injectivity radius or volume ratios.

**Lemma W′ (the item to write).** Under \((H_{\beta,\Lambda})\), the weighted system with background \(\bar g\) and weight \(\rho^4\) exists on \([0,t_0(\beta,\Lambda)]\). In local units it satisfies
\[
|\mathrm{Rm}(t)-\mathrm{Rm}(0)|\le Ct^{\beta/4},\qquad |\nabla^k\mathrm{Rm}|\le C_kt^{-k/4}.
\]
The estimates are proved on lifted balls.

Upper comparability then follows from a point-chasing argument:

- With \(\Phi(y)=|\mathrm{Rm}(y)|r(y)^2\), iterate from a near-maximizer of \(|\mathrm{Rm}|\) on \(B(x,r(x))\). Because \(|\mathrm{Rm}|\) is bounded on a compact \(M\), the iteration stops at a point \(w\) with \(d(x,w)\le Cr(x)\), \(r(w)\le Cr(x)\) and \(\Phi(w)\ge c\).
- For \(t\le t_0\), Hölder continuity in time keeps \(|\mathrm{Rm}_{g_t}(w)|\ge\frac c2r(w)^{-2}\).
- Hence \(r_{g_t}(x)\le r_{g_t}(w)+d(x,w)\le Cr(x)\).

**Theorem 50.B′ (entrance for the structure theorem).** The conclusions of 50.B hold for any minimizing sequence satisfying (NC) and \(\varepsilon_i=\int r_{g_i}^4|\nabla P(g_i)|^2\to0\). No derivative bounds are needed, given the harmonic-gauge elliptic bootstrap of §4.

**Target 50.A\* (open).** For arbitrary smooth \(g_0\), find \(g\) with \(P(g)\le P(g_0)\) and \(\int r_g^4|\nabla P(g)|^2\le C(P(g_0)-\alpha)\), where the weight is the own scale of the output. Two-sided comparability with \(g_0\) is then not needed. Two mechanisms are candidates:

- **Evolving geometric weight.** Use \(w_t=\rho_{g_t}^4\), with \(\rho_g\) defined by the intrinsic elliptic equation of §2, so that it depends continuously on \(g\). This restores diffeomorphism-naturality, so Bour Prop. 2.1 applies verbatim, and the mean-value selection weights by the selected metric's own scale.
- **Pointwise weight.** \(w=(|\mathrm{Rm}_g|^2+1)^{-1}\) is geometric and gives \(\int_{B(x,r_g(x))}|\nabla P|^2\le(1+r_g^{-4})\int w|\nabla P|^2\) directly. However, its rescaled coefficient \((r^4+|\widehat{\mathrm{Rm}}|^2)^{-1}\) is unbounded where \(\mathrm{Rm}\) vanishes pointwise, so it needs a cap by \(\rho_g^4\).

Reducing an arbitrary minimizing sequence to \((H_{\beta,\Lambda})\) at \(P\)-cost tending to zero is equivalent to 50.A\*. This is the precise remaining content of "every minimizing sequence admits a scale-adapted Palais–Smale replacement."