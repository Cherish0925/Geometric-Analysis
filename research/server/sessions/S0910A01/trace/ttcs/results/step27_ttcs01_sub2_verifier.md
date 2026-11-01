# TTCS Independent Branch Record

```json
{
  "step_id": 27,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step27_normalized_continuation_theorem.md",
    "Sessions/S0910A01/workspace/notes/step27_unified_weak_moser_iteration.md",
    "Sessions/S0910A01/workspace/scripts/step27_three_factor_absorption.py",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A01/workspace/notes/step25_tensor_energy_derivation.md",
    "Sessions/S0910A01/workspace/notes/step26_weighted_velocity_and_local_flow.md"
  ]
}
```

## Task

Verify the normalized cutoff-flow continuation theorem and the full conditional gap chain for the four-dimensional negative Yau-26 laboratory. The claim is that the three theorems in the continuation note (short-time existence, extension under weighted curvature, uniform time via first-exit bootstrap) close the last analytic obstacle, and that the full chain from initial Ricci pinching to the Derdziński forbidden germ is logically complete (conditional on the general-p inequality and Maheux-Saloff-Coste Sobolev).

Specific points to check:
1. In Theorem 1.1 (short-time existence via ε-regularization): Does the lower-order -2χ²g term genuinely not affect the parabolic existence? The ε-independent energy bound (1.3) gains O(Vol) terms from normalization—is this absorbed by Gronwall for short time?
2. In Theorem 2.1 (extension): Wang's induction uses ∇^m(χ²Rm). The normalization adds ∇^m(χ²g) terms. Since g itself evolves, ∇^m g involves m-th derivatives of Christoffel symbols, hence ∇^{m-1}Rm. Does the induction order remain correct (i.e., does controlling ∇^{m-1}(χ²Rm) suffice to control ∇^m(χ²g))?
3. In Theorem 3.1 (uniform time): The first-exit argument uses the weighted curvature bound ||aRm|| ≤ Cβ/t, which diverges at t=0. But Theorem 2.1 requires bounded |χ²Rm| on [0,T). Is the argument correct that short-time existence gives [0,T₁), and then for any t₀ ∈ (0,T₁), |aRm(t₀)| < ∞ by the Moser bound, so extension applies from t₀ onward?
4. Does the three-factor Moser iteration (unified note) correctly supply both ||aF|| ≤ Cβ/t and ||aE|| ≤ Cδ(r²/t)^{1/3} with the stated volume cancellations? The key algebraic identity is the three-factor Hölder decomposition a^{p-1}Ff^p = (aF³)^{1/3}(a^{p-2}f^p)^{1/3}z_p^{4/3}.
5. Is there any logical gap between the positive-time bounded curvature on plateaux and the Derdziński contradiction? Specifically: the calibrated Weyl spectrum from Steps 5-8 was derived for the initial metric; after flowing, do the nonnegative deficit densities transfer to the terminal metric under metric comparability and Q/A → 0?

## Output

# Verification Memo: 4D non-existence-branch continuation theorem and the conditional chain

Session S0910A01. This memo checks the three continuation theorems, the unified three-factor Moser mechanism, and the transfer of the terminal deficit structure, following the five points posed. I read `step27_normalized_continuation_theorem.md`, `step27_unified_weak_moser_iteration.md`, `step27_three_factor_absorption.py`, A03's `step26_general_p_and_sobolev_resolution.md`, and A01's `step25`/`step26` derivations.

Summary judgment up front: the three-factor algebraic core (Point 4) is exact and the metric-drift separation is clean; the extension induction (Point 2) closes for a reason stronger than the note states; the first-exit time logic (Point 3) is sound with a one-line restatement. The short-time existence proof as written (Point 1) contains an unjustified step, though its conclusion is recoverable by a different route. The terminal transfer (Point 5) has a substantive missing input tied to collapse. Several exponent labels across the two Moser notes disagree and should be reconciled; the final boxed outputs survive.

---

## Point 1 — Short-time existence (Theorem 1.1)

**The lower-order term is genuinely harmless.** The added velocity piece $-2\chi^2 g$ is algebraic in $g$ (no derivatives of the metric), so it does not touch the principal symbol $-2(\varepsilon^2+\chi^2)\Delta$. As a zeroth-order coefficient in the DeTurck-linearized system it cannot alter strict parabolicity for fixed $\varepsilon>0$. This part is correct, and it agrees with the independent reasoning in `step26_weighted_velocity` §5 (the DeTurck hatted equation carries $(\chi\circ\varphi^{-1})^2$ in front of both $\operatorname{Ric}(\hat g)$ and $\hat g$, and pullback restores the fixed spatial $\chi^2$).

**The $O(\mathrm{Vol})$ source is absorbed for short time — but this is not where the difficulty lives.** Inequality (1.3) is a linear differential inequality $y'\le Cy+C_0\mathrm{Vol}$, whose Gronwall solution $y(t)\le (y_0+C_0\mathrm{Vol}\,t)e^{Ct}$ is bounded on $[0,T_0]$ with a constant uniform in $\varepsilon$ (the coefficient $C(\varepsilon^2+\chi^2)\le C(1+\|\chi\|_\infty^2)$ does not degenerate as $\varepsilon\to0$). So the normalization source is indeed benign.

**The unjustified step is the $\varepsilon\to0$ passage.** The proof concludes from a uniform bound on $\int|\operatorname{Rm}_\varepsilon|^{n/2}$ that "the metrics $g_\varepsilon(t)$ remain uniformly bounded in $C^k$ on $[0,T_0]$," then applies Arzelà–Ascoli in $C^{k-1}$. In dimension four $\int|\operatorname{Rm}|^{n/2}=\int|\operatorname{Rm}|^2$ is the scaling-invariant integral, and control of this integral does **not** imply uniform $C^k$ bounds. Extracting pointwise/$C^k$ control from an $L^{n/2}$ curvature integral is exactly the content of the Moser/$\varepsilon$-regularity machinery elsewhere in the program; it cannot be assumed here as a free consequence of Gronwall. Furthermore, the parabolic existence time $T_\varepsilon$ produced by DeTurck for the regularized equation ordinarily depends on the ellipticity constant, whose lower bound $\varepsilon^2$ collapses as $\varepsilon\to0$; the note asserts $T_\varepsilon\ge T_0$ uniform but supports this only through the same integral bound. So the regularization argument, as written, does not deliver a smooth limit.

**A sound route to the same conclusion exists and is already in the file.** `step26_weighted_velocity` §5 records that Yang's DeTurck construction (source lines 787–823) gives short-time existence for the degenerate coefficient flow $\partial_t g=-2\chi^2\operatorname{Ric}$ directly, without regularization, by transporting the coefficient in DeTurck gauge and pulling back. Because $-2\chi^2 g$ is a compactly supported term with no second derivatives, it enters only through lower-order constants. The clean statement of Theorem 1.1 is therefore: *short-time existence is inherited from Yang's degenerate-coefficient DeTurck construction, modified by a lower-order algebraic term.* This is what `step26` §5 already says is required ("this adaptation must be written explicitly before T5 is regarded as inherited from Yang"). The $\varepsilon$-regularization presentation in the continuation note should either be replaced by this route or repaired at the $L^{n/2}\to C^k$ step, which it currently does not justify.

---

## Point 2 — Extension under weighted curvature control (Theorem 2.1)

**The induction order is correct, and for a cleaner reason than the note gives.** The concern is that $\nabla^m g$ might involve $\nabla^{m-1}\operatorname{Rm}$ through Christoffel derivatives. In the covariant tensor formulation used by Wang/Hamilton, all derivatives are with respect to the evolving Levi-Civita connection, for which $\nabla g\equiv0$. Hence
$$
\nabla^m(\chi^2 g)=\sum_{k}\binom{m}{k}(\nabla^k\chi^2)\,\nabla^{m-k}g=(\nabla^m\chi^2)\,g,
$$
i.e. every derivative lands on the time-independent, bounded factor $\chi^2$, and $g$ is carried unchanged. No curvature appears in $\nabla^m(\chi^2 g)$ at all. This is stronger than the note's phrasing ("$\nabla^i g$ controlled by metric equivalence, Wang Prop 4.9"), which invokes a bilipschitz comparison that is only needed for the $C^0$ equivalence, not for the higher derivatives.

**Where curvature does enter, it enters below the induction level.** The normalization contributes to $\partial_t\Gamma$ the term $-2\nabla(\chi^2 g)=-2(\nabla\chi^2)\otimes g$. In the commutator $[\partial_t,\nabla^m]\operatorname{Rm}$ this produces contributions of the form $(\nabla^{k+1}\chi^2)\,g*\nabla^{m-k}\operatorname{Rm}$ with $k\ge0$, so the highest curvature order is $\nabla^{m-1}\operatorname{Rm}$ — strictly one order below the induction target $\nabla^m\operatorname{Rm}$. The induction therefore closes. This confirms the note's "handled by the same induction" for the right reason.

**The metric-equivalence hypothesis for Wang Prop 4.9 is correctly established:** $|\partial_t g|=2\chi^2|\operatorname{Ric}+g|\le C(\chi^2|\operatorname{Rm}|+\chi^2)\le C(K+1)$ under (2.1), giving $e^{-C(K+1)T}g_0\le g(t)\le e^{C(K+1)T}g_0$. The Christoffel-variation ledger (i)–(iii) is consistent with this. Theorem 2.1 stands.

---

## Point 3 — Uniform time via first-exit (Theorem 3.1)

**The near-$t=0$ divergence of $\|a\operatorname{Rm}\|\le C\beta/t$ does not obstruct the extension, and the resolution you describe is correct.** Short-time existence supplies smooth flow on $[0,T_1)$, $T_1>0$. For any $t_0\in(0,T_1)$ the metric is smooth on compact $M$, so $|a\operatorname{Rm}(t_0)|<\infty$; thereafter the Moser bound gives $\sup_{[t_0,\,\cdot)}|\chi^2\operatorname{Rm}|\le C\beta/t_0<\infty$. Extension then applies on $[t_0,\cdot)$. Combined with smooth existence on $[0,t_0]$, the flow persists smoothly past any $\tau<T_*$. The $T_*$-maximality contradiction closes as written.

**One statement should be tightened.** Theorem 2.1 is phrased with $\sup_{[0,T)}|\chi^2\operatorname{Rm}|\le K$, i.e. a bound over the whole interval including near $0$, where the Moser output diverges. The application in Theorem 3.1 item 6 uses it "beyond any $t<T_*$," which really invokes the bound on $[t_0,\tau]$ with $t_0>0$. Theorem 2.1 should be stated (or re-read) with time origin at $t_0>0$: *bounded $|\chi^2\operatorname{Rm}|$ on $[t_0,T)$ extends the flow past $T$.* This is a translation of the time variable, not a new argument, but as literally written the hypothesis and the application do not match.

**The deeper point: Theorem 3.1 does not close the last obstacle; it reduces to the power-energy inequality.** Items 1–6 of the first-exit step (the strict improvement of F1–F4, the drift bound $I(t)<1/20$, the $\beta$-persistence) all rest on the Moser outputs (5.4)/(6.5). Those outputs are conditional on the power-energy inequality (2.3), which the notes themselves list as unfinished: `step27_unified` §9(1) states the remaining work is "full index-level formulas including moving-norm, moving-volume, Lichnerowicz reaction, Hessian IBP, Kato regularization for $|E|$, and exact constant tracking," and `step26_weighted_velocity` §7 lists the same items as still open. So the note's framing that these three theorems "close the last open analytic obstacle" is not consistent with the note's own list of open analytic obligations. What Theorem 3.1 correctly establishes is: *given* the weighted estimates with the stated $t$-behavior, the first-exit bootstrap is self-consistent and yields a uniform continuation time. That conditional statement is sound; the unconditional "obstacle closed" is not, because the power-energy inequality with polynomial $p$-dependence and tracked constants is not yet in hand.

---

## Point 4 — Three-factor Moser and volume cancellations

**The central identity is exact.** With $z_p=a^{(p-1)/2}f^{p/2}$,
$$
(aF^3)^{1/3}(a^{p-2}f^p)^{1/3}z_p^{4/3}=a^{\frac13+\frac{p-2}{3}+\frac{2(p-1)}{3}}F\,f^{\frac p3+\frac{2p}{3}}=a^{p-1}Ff^p,
$$
matching the LHS. The $a$-exponent sums to $p-1$, $F$ to $1$, $f$ to $p$. The sympy check (`ratio==1`) is a genuine confirmation of this algebra. Hölder$(3,3,3)$ then gives $R_p\le Y^{1/3}H_p^{1/3}\|z_p\|_4^{4/3}$ exactly, and the subsequent Sobolev + Young step correctly yields $R_p\le\varepsilon(D_p+r^{-2}H_p)+C_\varepsilon C_p^2 S^2 Y H_p$, so $Y$ enters the Gronwall coefficient **linearly**. This is the real structural advance over a critical-threshold absorption, and it is correct.

**Both volume cancellations check out at the level of the final exponents.**
- Curvature, $p_0=3$: $S^{2/3}\cdot(\beta^3/S^2)^{1/3}=S^{2/3}\cdot\beta S^{-2/3}=\beta$, giving $\|aF\|\le C\beta/t$.
- Defect, $p_0=6$: $S^{1/3}V^{1/6}=(r^2 V^{-1/2})^{1/3}V^{1/6}=r^{2/3}$, and $t^{-1/2}\cdot t^{1/6}=t^{-1/3}$, giving $\|aE\|\le C\delta(r^2/t)^{1/3}$.

The drift integral $\int_0^{\theta r^2}\delta(r^2/t)^{1/3}\,dt=\tfrac32\delta\theta^{2/3}r^2\to0$ is correct and integrable at $t=0$; the observation that $\|aF\|\sim\beta/t$ is **not** integrable and is deliberately not used for metric comparison is a clean and correct separation of roles.

**A concrete exponent inconsistency to reconcile between the two Moser notes.** `step27_unified` §4 writes the per-step factor as $[S(\Lambda+\Delta t^{-1})]^{1/p_k}$ and then states
$$
\sum_{k}\frac{1}{p_k}=\frac{1}{p_0}\frac{\kappa}{\kappa-1}=\frac{n}{2p_0}.
$$
This equality is arithmetically wrong. With $\kappa=1+2/n$, one has $\kappa/(\kappa-1)=(n+2)/2$, so $\sum 1/p_k=(n+2)/(2p_0)$, which for $n=4,p_0=3$ is $3/p_0=1$ — and this matches the script's `moser_sum_3 = 1.0`. The quantity $n/(2p_0)$ is a *different* object: it is the accumulated Sobolev power in the $L^\infty$ prefactor, equal to $(1/\kappa)\sum 1/p_k=\frac{n}{n+2}\cdot\frac{n+2}{2p_0}=\frac{n}{2p_0}$. A03's `step26` §5.2 carries this correctly: its per-step factor is $(CS)^{2/(3p_j)}$ (i.e. $S^{1/(\kappa p_j)}$), and $\sum 2/(3p_j)=\tfrac23\cdot 3/p_0=2/p_0=n/(2p_0)$. So the final Sobolev power $S^{n/(2p_0)}$ used in output (4.2) is correct, but the §4 prose conflates the per-step exponent ($1/(\kappa p_k)$, not $1/p_k$) with the raw sum $\sum 1/p_k$, and mislabels the sum's value. The two notes should be made to state the same per-step factor. This is a labeling defect, not a break in the final result.

**What the script does and does not establish.** `step27_three_factor_absorption.py` verifies (a) the exact three-factor decomposition, (b) the $(3,3,3)$ Hölder bookkeeping, (c) the two volume cancellations, (d) the drift integral, (e) the geometric convergence of $\sum 1/p_k$. It does **not** verify the power-energy inequality (2.3), the actual iteration with the polynomial constants $C_p\le Cp^2$ (A03 uses $Cp^3$ — a further inter-note constant discrepancy worth resolving, since "exact constant tracking" is a listed open item), or that the time-slab coefficient integral (4.1) stays bounded with the correct dependence. The script confirms the algebra that makes the outputs *dimensionally forced*; it does not confirm the outputs.

---

## Point 5 — Transfer of the calibrated Weyl structure to the terminal metric

**The Seiberg–Witten/LeBrun integral inequalities transfer for free.** These are consequences of the smooth structure and the SW basic classes, which are diffeomorphism invariants independent of the metric. Any metric on the fixed $M$, including $g(\theta r^2)$, satisfies the same LeBrun-type curvature integral bounds. So the "mixed SW and tensor-gap inequalities from Steps 3–8" apply to the terminal metric without needing metric comparability. This part of the transfer is legitimate.

**The defect preservation is internally consistent as stated.** The global identity $Q_{\rm global}(t)\le e^{C\theta}Q_{\rm global}(0)$ follows from the support-local (3.6)/(2.9) plus the disjoint-support decomposition, using that off-support the metric is stationary. With $Q_{\rm global}(0)\le C\delta^2\mathrm{Vol}(M)$ and $\mathrm{Vol}/A=O(1)$, $Q_{\rm global}/A\to0$. Granting the support estimates, this is fine.

**The substantive missing input is the passage from bounded-curvature plateaux to a smooth Einstein germ under collapse.** Two things are asserted but not established in these files:

1. *A sequence-independent positive plateau volume fraction.* `step25` §4 and `step27` §10 both say "a sequence-independent positive plateau fraction (however small) suffices." The Moser bound gives $|\operatorname{Rm}|\le C\beta/t$ on $\{a=1\}$ at positive time, but the total volume fraction of $\bigcup\{a_j=1\}$ across the selected supports, bounded below uniformly along the pinching sequence, is not demonstrated. If the plateau fraction tends to zero along the sequence, the averaged nonnegative deficit contributes vanishing mass and no contradiction is forced. This lower bound must come from the maximal-function selection and is not present in the supplied notes.

2. *Compactness under collapse.* The entire Sobolev input (Maheux–Saloff-Coste, A03 §1) is designed to work **without** a noncollapse hypothesis, and the notes emphasize this repeatedly (e.g. "available without any noncollapse hypothesis"). But the downstream step "harmonic-chart compactness + smooth Einstein limit" (step27 §10.4) presupposes a uniform harmonic-radius lower bound, which requires bounded curvature **and** a volume/injectivity-radius lower bound. Bounded $|\operatorname{Rm}|$ alone on collapsed balls does not yield a smooth four-dimensional Einstein limit (the standard obstruction: bounded-curvature collapsing sequences converge, in the Cheeger–Gromov–Fukaya sense, to lower-dimensional or nilpotent structures, not to a non-degenerate four-metric). So the extraction of a genuine smooth Einstein germ carrying the calibrated $W^+$ spectrum is in direct tension with the collapsed setting the machinery was built for. Either a noncollapse statement on the plateau balls must be proved (which would restrict which sequences are admissible), or the terminal contradiction must be run through an equivariant/collapsed limit and a Derdziński-type statement valid on that structure. Neither is supplied.

To make Point 5 defensible, the missing scientific substance is precisely: (i) a uniform lower bound on plateau volume fraction along the near-critical sequence, and (ii) a harmonic-radius (equivalently, local noncollapse) statement on those plateaux, so that $Q/A\to0$ plus bounded curvature plus nonnegative saturating deficit forces a smooth Einstein germ. Until these are in place, the terminal step is a conditional consequence, as the notes themselves label it.

**A separate structural question about the terminal contradiction's role.** The chain terminates in "smooth Einstein limit carrying the calibrated Weyl spectrum $\longrightarrow$ Derdziński forbidden germ," i.e. a contradiction. It would be worth stating explicitly what this contradiction refutes. If it shows that a Ricci-pinched metric on the Ishida–LeBrun $M$ forces an Einstein germ that $M$ forbids, the conclusion is that such $M$ carries no pinched metric — which is a statement about $M$, not by itself a refutation of the universal-constant proposition (a refutation needs an $M$ that *does* carry a pinched metric yet admits no Einstein metric). The analytic notes do not spell out how the terminal contradiction is converted into a statement about the original all-dimensional proposition. This is outside the analytic checks requested but bears on whether the completed chain, even if fully proved, addresses the stated research problem for this laboratory.

---

## Consolidated findings

- **Sound as written:** the algebraic core of the three-factor absorption (Point 4 identity + Hölder + Young + both volume cancellations), the metric-drift separation, the extension induction order (Point 2, closing because $\nabla g\equiv0$), and the first-exit time logic (Point 3, up to a one-line time-translation restatement).
- **Recoverable but presently unjustified:** the short-time existence proof (Point 1) — the $L^{n/2}\to C^k$ step in the $\varepsilon\to0$ passage is not valid; the conclusion is available instead from Yang's degenerate-coefficient DeTurck construction plus a lower-order algebraic term, which `step26` §5 already flags as needing to be written explicitly.
- **Inter-note inconsistencies to reconcile:** the per-step Sobolev exponent and the value of $\sum 1/p_k$ in `step27_unified` §4 (should be $S^{1/(\kappa p_k)}$ and $\sum 1/p_k=(n+2)/(2p_0)$, as A03 has consistently); and the polynomial constant $C_p$ ($p^2$ in A01 vs $p^3$ in A03). Final boxed outputs are unaffected, but "exact constant tracking" is listed as unfinished, so these should be unified.
- **Not closed:** the assertion that the three theorems "close the last analytic obstacle." Both notes' own §9/§7 list the power-energy inequality (2.3) with index-level constants, the weighted $L^p\!\to\!L^\infty$ step, and the explicit normalized DeTurck adaptation as open. Theorem 3.1 is a correct *conditional* self-consistency of the first-exit bootstrap given those estimates.
- **Missing substance for Point 5:** a uniform lower bound on plateau volume fraction along the sequence, and a noncollapse/harmonic-radius input on plateaux, are needed before bounded-curvature plateaux yield a smooth Einstein germ; the current compactness step is in tension with the deliberately noncollapse-free Sobolev machinery. The SW/LeBrun inequalities themselves transfer to the terminal metric without difficulty.

The strongest present result is the conditional statement: *given* the power-energy inequality with polynomial $p$-dependence and the initial Maheux–Saloff-Coste Sobolev, the weighted estimates $\|aF\|\le C\beta/t$ and $\|aE\|\le C\delta(r^2/t)^{1/3}$ follow with exact volume cancellation, and they close the first-exit bootstrap to a uniform continuation time. The remaining analytic substance is the full index-level derivation of (2.3), the noncollapse input at the terminal step, and the explicit normalized short-time construction; the second of these is the one most likely to change the overall judgment, since it decides whether the terminal Einstein germ exists at all.