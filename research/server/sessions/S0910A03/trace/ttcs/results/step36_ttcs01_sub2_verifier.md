# TTCS Independent Branch Record

```json
{
  "step_id": 36,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step35_unregularized_J6_persistence_lemma.md",
    "Sessions/S0910A03/workspace/notes/step35_degenerate_flow_existence.md",
    "Sessions/S0910A03/workspace/notes/step35_cutoff_jet_continuation.md",
    "Sessions/S0910A03/workspace/notes/step35_first_exit_bootstrap_assembly.md",
    "Sessions/S0910A03/workspace/notes/step27_shifted_curvature_continuation_analysis.md",
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md",
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Review the Step 35 analytic handoff for the normalized fixed-cutoff Ricci flow in the four-dimensional negative Ishida--LeBrun route. Focus on four interfaces: (i) whether the unregularized fixed J6 persistence lemma is a genuine valid advance and exactly what assumptions it still needs; (ii) whether the Step 35 DeTurck/existence note uses the correct gauge and transported coefficient, and whether its epsilon/Schauder argument actually gives epsilon-independent smooth existence; (iii) whether the cutoff-jet continuation note proves an extension criterion on [0,Tmax) or instead assumes smoothness/uses uncontrolled quantities such as unweighted T or a∇Rm; and (iv) whether terminal calibration still needs a separate global Q=∫|E|^2 estimate rather than J6 or |aE|. Give a direct scientific memo with corrected mathematical status and the next proof targets, not publication advice.

## Output

# Verification Memo — Step 35 Analytic Handoff (normalized fixed-cutoff flow, 4D negative Ishida–LeBrun route)

Scientific reading of the four requested interfaces, with corrected status and the concrete proof objects each still needs. I read the two Step 35 lemma notes, the assembly note, the two Step 27 continuation notes, and Yang 1992 (the source theorem 8.2 / §9 / Appendix A that all of this is transferring).

---

## Interface (i): unregularized fixed $J_6$ persistence lemma — genuine advance, still conditional on three inputs

**What is actually correct and new.** The lemma's central structural move is sound and is a real simplification over the A01 route:

- Working with $s=|E|^2$ and integer powers $s^3=|E|^6$ keeps the integrand and the test function $q=3\eta^2a^4s^2$ smooth through $E=0$. No Kato approximant $\Phi_\varepsilon=(|E|^2+\varepsilon^2)^{1/2}$ and no $\varepsilon$-remainder is generated. This is legitimate: $t\mapsto t^{3/2}$ is $C^1$ on $[0,\infty)$, and the Sobolev variable $w_6=\eta\chi^5 s^{3/2}$ has $|\nabla w_6|\lesssim s|\nabla E|$ continuous and bounded. The Sobolev inequality applies to $w_6\in W^{1,2}_c$.
- The decisive two-factor absorption is correct **because the defect reaction is genuinely linear in curvature**. The Lichnerowicz reaction $4aR_{ikjl}E^{ij}E^{kl}$ carries one power of $\mathrm{Rm}$ and two of $E$, so the potential $P_6=\int\eta^2a^5Fs^3$ has a single factor $F$. Hölder $(2;4,4)$ then peels $F$ off in $L^2$: $P_6\le\|F\|_{2,U}\|w_6\|_4^2$, and Sobolev gives $P_6\le C\gamma(X_6+r^{-2}J_6)$ with $\gamma=\mathcal S K_2^{1/2}$. The three-factor $\int aF^3=Y$ that the curvature energy needs (quadratic curvature reaction) does not appear here. The distinction between the curvature energy (reaction quadratic in $\mathrm{Rm}$) and the defect energy (reaction linear in $\mathrm{Rm}$) is real; the advance is correctly confined to $J_6$ and does **not** eliminate $Y$ from the curvature Moser chain (the note states this in §7.2).
- The Hessian-of-$a$ handling in §3.5 uses the correct device: integrate by parts the actual tensor $\nabla_i\nabla_j a$ (not $|\nabla^2 a|$), transferring one derivative so only $\nabla_j a=2\chi\nabla_j\chi$, i.e. $|da|\le C/r$, survives. This is exactly the mechanism that removes any pointwise $\nabla^2\chi$ dependence, matching the Step 23 §2 "no cutoff Hessian" weak inequality and the Yang/Wang philosophy. Because $B^{ij}(q)=O(s)$ vanishes at $E=0$, the Hessian branch is not a bare curvature source; all three sub-branches reduce to the structure of $I_1$ and are absorbed by Young into $\varepsilon X_6+C_\varepsilon r^{-2}J_6$. The vanishing of the $d\eta$ terms is consistent: $\eta\equiv1$ on a neighborhood of $\operatorname{supp}\chi\supset\operatorname{supp}a$, so on $\operatorname{supp}d\eta$ one has $a=da=0$.
- The Gronwall exponent is scale-stable: $(1+r^{-2})t\le\theta(r^2+1)$ on $[0,\theta r^2]$, so for small $r$ the amplification is $\approx e^{C_0\theta}$, and the volume-cancelled $\gamma=Cr^2\sqrt{K_0}$ is collapse-independent on a good center. Coefficient bookkeeping closes: the Sobolev third term contributes $\le9X_6$, absorbed into the $-6X_6$ dissipation once $C\gamma_0<c/2$.

**Corrected status.** The $J_6$ persistence estimate is a valid, self-contained Gronwall **conditional on three inputs that must be stated as hypotheses**, not only on "flow existence and first-exit geometry":

1. **$K_2$ persistence with the small-$\gamma$ absorption threshold.** $\gamma=\mathcal S K_2^{1/2}$ must stay below the absorption threshold for the whole interval. This is supplied by the $q=2$ curvature energy inequality (Step 23 §3 / Step 34 eq 3.1), itself conditional. So $J_6$ does not depend on $Y$, but it does depend on $K_2$ control. The dependency graph in the assembly note ($K_2\to J_6$ via $\gamma$; $K_2\to Y\to$ curvature Moser; $J_6+Y\to$ defect Moser) has no cycle, which is correct, but $J_6$ is not unconditional.
2. **The good-center volume relation $K_2\le K_0V$**, i.e. $\|F\|_{2,U}^2\lesssim K_0V$, which is what makes $\gamma$ collapse-independent. This is an initial-data selection property (maximal-function good center), sequence-uniform, and should be listed as a standing hypothesis of the lemma.
3. **Moving Sobolev / metric / support comparability on $[0,T]$** (Step 34 §5). The Sobolev constant $\mathcal S(t)$ and the weight comparabilities enter $\gamma$; these are part of the first-exit bundle and are used, not proved, here.

**Point to check in the algebra.** In §2.2 the "metric variation" source is written $4aE^{ip}R_{ijkl}E^{jkl}{}^p$; the index pattern is malformed ($E$ is a $2$-tensor and cannot carry four indices). This is presumably a transcription of a term like $aE^{ip}R_{ijkl}E^{kl}{}_p$ or $a\,\mathrm{Rm}*E*E$. Since the constant $B^{ij}(q)=q(2g^{ij}|E|^2+2\tau E^{ij}-4E^{ik}E_k{}^j)$ depends on getting this reaction right, the exact reaction algebra (asserted verified by the 28-check script, which I did not see) is the one place where an independent hand derivation of $(\partial_t-a\Delta)s$ and of $B^{ij}$ would confirm the lemma at the level of the printed identities.

---

## Interface (ii): DeTurck / existence note — gauge recovery of (0.1) is not established, and $\varepsilon$-independence is asserted from the wrong estimate

**Gauge issue.** §1 writes the DeTurck-modified equation
$$\partial_t g=-2a(\mathrm{Ric}+g)+a(\nabla_iW_j+\nabla_jW_i)=a\,\mathcal F(g),$$
including the DeTurck term, and §2 regularizes this modified equation as $\partial_tg^\varepsilon=a_\varepsilon\mathcal F(g^\varepsilon)$. But §3.3 then states the limit "satisfies (0.1)," where (0.1) is the **original** equation $\partial_tg=-2a(\mathrm{Ric}+g)$ **without** the DeTurck term. The two are different equations; the DeTurck term does not vanish. The solution of the modified system is $\hat g$, and the original flow is recovered only through the pullback $g=\varphi_t^*\hat g$, where $\varphi_t$ solves the accompanying diffeomorphism ODE. For a **fixed-cutoff local** flow this requires transporting the coefficient — $\widehat a=(\chi\circ\varphi_t^{-1})^2$ — so that pullback returns the original fixed $\chi$; otherwise the recovered equation carries coefficient $\chi\circ\varphi_t$, not $\chi$. This transport, with the Lie-derivative cancellation, is exactly what Yang 1992 Approach 1 does and what Step 27 §6 (eq. 6.1–6.2) writes correctly. The Step 35 existence note omits it entirely, so as a standalone it does not deliver a solution of (0.1).

**$\varepsilon$-independence issue.** §3.2 asserts $\varepsilon$-independent $C^{k,\alpha}$ bounds from a decomposition $M=U_+\cup U_0$ and generic parabolic Schauder. Two problems:
- The energy inequality written in §3.2 for $U_0$, $\frac{d}{dt}\|h\|_{H^k}^2\le C(2a_0+\varepsilon)\|h\|_{H^{k+1}}^2+C$, has the diffusion term on the **wrong side** with a positive sign. As written it does not close a Gronwall (the top norm $\|h\|_{H^{k+1}}$ appears as an upper bound, not as $-c\,a_\varepsilon\|h\|_{H^{k+1}}^2$ dissipation). The intended statement is dissipative, but then the interface flux terms on $\partial U_+$, produced by integrating by parts on the subdomains $U_+,U_0$ across the transition $a\sim a_0$, are not addressed — and that interface is precisely the difficult region.
- More fundamentally, Yang's Approach 2 obtains $\varepsilon$-independence from the **weighted (χ-powered) curvature energy** structure of the evolution (the Moser iteration of Appendix A, the same machinery as the $J_6$/curvature energy notes), not from generic Schauder on the metric. The Step 35 note's own §6 disclaims $\varepsilon$-independent energy estimates while §3.2 asserts $\varepsilon$-independent $C^{k,\alpha}$ bounds; for a nonlinear degenerate system these cannot be separated — the regularity bound needs the very energy control that §6 declines.

**Corrected status and the cleaner path.** Per-datum short-time existence for a **fixed** smooth $(g_0,\chi)$ needs no $\varepsilon$-independence at all: Yang Approach 1 / Step 27 §6 (transported-coefficient DeTurck) gives it directly with a datum-dependent time, and the assembly note confirms per-datum existence is sufficient (F4), since the bootstrap supplies the uniform time. The $\varepsilon$-route in this note is both incomplete (no pullback / no coefficient transport) and aimed at a stronger property ($\varepsilon$-uniformity) that is not required. The correct existence statement is the one in Step 27 §6, not the one derived here.

Note that the uniqueness argument (§3.4) is fine as written: $\frac{d}{dt}\|h\|_2^2\le C\|h\|_2^2$ with $\int a|\nabla h|^2\ge0$ discarded — the degenerate diffusion helps, so Gronwall gives $h\equiv0$.

---

## Interface (iii): cutoff-jet continuation note — this is interior regularity given smoothness, not an extension statement

The note presupposes what an extension result must produce. §4.5 ("Finiteness of the Gronwall coefficient") explicitly uses "$\|T(t)\|_\infty$ is finite … (the solution is smooth by the degenerate existence proposition)" and "$\|a\nabla\mathrm{Rm}(t)\|_\infty$ is finite … (smooth solution)." So the coefficients $\Lambda(t),R(t)$ are declared locally integrable on $(0,T]$ **because the solution is already assumed smooth**. That is an interior-regularity / higher-jet-finiteness statement on $[\tau,T]$, not a continuation statement of the form "$\sup_{[0,T_{\max})}|a\mathrm{Rm}|<\infty\Rightarrow$ smooth extension through $T_{\max}$."

Two specific quantities used as inputs are **not** controlled by the zero-order bootstrap:
- **Unweighted $\|T\|_\infty=\|\mathrm{Rm}+G\|_\infty$.** The bootstrap controls the weighted $\|aF\|_\infty\le C\gamma/t$ and $\|aE\|_\infty$. Unweighted curvature is bounded only through the fixed initial datum on $\{a=0\}$ plus interior smoothness on $\{a>0\}$; it is datum-dependent, not a bootstrap output.
- **$\|a\nabla\mathrm{Rm}\|_\infty$.** This is a first-derivative bound. On the plateau it comes from Shi (§2.3); on the transition it is exactly what the coupled cutoff-jet estimate is meant to produce. Using it as an input in §4.5 (via "smoothness") is using the conclusion to bound the coefficient.

**What is nonetheless usable.** For extension through a **positive** terminal time $T_{\max}<\theta r^2$, the coefficient $\Lambda$ near $T_{\max}$ is bounded by the zero-order Moser endpoint $\|aF\|_\infty\le C\gamma/t$ (finite near $t=T_{\max}>0$), not by "smoothness." The note conflates these two sources of boundedness. If the near-$T_{\max}$ boundedness of $\Lambda$ is derived from the Moser endpoint alone, the $\mathcal E_p$ Gronwall (4.7) does give bounded higher jets up to $T_{\max}$ — but this must be written from the weighted zero-order bounds, not from an assumption of smoothness on the open interval.

**Corrected status.** The rigorous extension statement (from $\sup|a\mathrm{Rm}|<\infty$ alone, without assuming higher smoothness) is the one attempted in **Step 27's normalized extension theorem** via the shifted tensor $U=aT$ and Wang's triangular induction — that note carries $\nabla^m U$ and the cutoff-jet evolution $\partial_t\nabla^r\chi$ coupled, integrating by parts $\chi\nabla^{m+2}\chi*U$ once to lower the highest cutoff order from $m+2$ to $m+1$. The Step 35 continuation note is a per-datum interior-regularity companion to that theorem, valid for datum-dependent higher jets **given** existence, plus sequence-uniform plateau bounds via Shi. It is not itself an extension statement. This is acceptable for the downstream terminal passage **only because** that passage (per §6 and the assembly §5) uses the sequence-uniform plateau regularity (a) and the global $L^2$ defect control, not the datum-dependent transition-region jets (b). That reliance should be made explicit so the uncontrolled $\|T\|_\infty$, $\|a\nabla\mathrm{Rm}\|_\infty$ are seen to be non-load-bearing for the sequence-uniform contradiction.

One internal tension to resolve: the two Step 27 notes disagree on maturity. `step27_shifted_curvature_continuation_analysis.md` §5 states the transfer "establishes a credible transfer mechanism but … not yet a complete extension theorem," and insists the $\chi\nabla^{m+2}\chi*U$ term must not be suppressed before the integration by parts; `step27_normalized_local_flow_extension_theorem.md` presents the same induction as a completed theorem. The rigorous extension rests on carrying $\mathcal L_{G,m}$ (the parallel-$G$ monomials) and the staggered-exponent Hölder bookkeeping of Wang Lemma 4.11 / Prop. 4.13–4.14 through term by term. The verify scripts cited cover algebraic bookkeeping (exit 0) only, and the independent Codex derivation is still to be inspected. So the extension is at "detailed induction structure with asserted constant bookkeeping," not "checked line by line."

---

## Interface (iv): terminal calibration needs a separate global $Q=\int_M|E|^2$; $J_6$ and $\|aE\|_\infty$ do not substitute

Yes — a separate global unweighted $Q(t)=\int_M|E|^2\,d\mu_t$ is genuinely required. The calibration inequality
$$\int\Big(|W^+|-\tfrac{1}{2\sqrt6}\Big)^2\le\tfrac{7}{24}\int|E|^2$$
has a **global unweighted $L^2$** right-hand side over all of $M$, including the frozen exterior $\{a=0\}$. Neither of the other two controlled quantities delivers this:
- $J_6=\int\eta^2a^4|E|^6$ is weighted by $a^4=\chi^8$, localized by $\eta$ to good supports, and is $L^6$. Hölder on the support gives at best a **weighted** $L^2$ on the support, $\int a^4|E|^2\le(\int a^4|E|^6)^{1/3}(\int a^4)^{2/3}$, and loses the exterior entirely. It cannot reconstruct $\int_M|E|^2$.
- $\|aE\|_\infty$ is weighted and pointwise; squaring and integrating gives $\int|aE|^2$, again weight-suppressed on the transition and zero in structure on the exterior.

Step 23 §5.1 supplies the correct object: with **no** localizing cutoff, $Q'+c\int_M a|\nabla E|^2\le Cr^{-2}Q+C\int_M a|\mathrm{Rm}||E|^2$, the curvature potential absorbed component-by-component on disjoint good supports via $\int_{U_j}\chi_j^2|\mathrm{Rm}||E|^2\le\|\mathrm{Rm}\|_{2,U_j}\|\chi_jE\|_4^2\le C\gamma_j(\int a|\nabla E|^2+r^{-2}\int|E|^2)$, giving $Q(t)\le e^{C\theta}Q(0)$. On $\{a=0\}$ the metric is stationary, so $\partial_t|E|^2=\partial_td\mu=0$ there and the exterior contributes the frozen initial defect $\int_{\{a=0\}}|E(0)|^2\le\delta^2\mathrm{Vol}$. Combined with the interior amplification, $Q(0)\le\delta^2V$ from the pinching gives $Q(T)\lesssim\delta^2V$.

**Corrected status.** The three defect quantities are independent objects with distinct roles: $Q$ (global unweighted $L^2$) feeds the calibration right-hand side; $J_6$ (localized weighted $L^6$) is the Moser seed producing $\|aE\|_\infty\le C\delta(r^2/t)^{1/3}$; $\|aE\|_\infty$ produces the integrable drift $\int_0^T\|aE\|_\infty\lesssim\delta\theta^{2/3}r^2$ that runs the metric/Sobolev self-improvement. The assembly note keeps $Q$ separate, which is correct. Two consistency points worth confirming: (a) the $Q$-absorption (Step 23 (5.2)) uses the same small-$\gamma_j$ threshold as the $J_6$ and curvature energies, so the same good-center selection controls all three simultaneously; (b) the calibration left-hand side needs $|W^+|$ of the **terminal** metric on the plateau, controlled by the sequence-uniform plateau curvature bound $|\mathrm{Rm}_{g(T)}|\le C\gamma/(Tr^2)$ from continuation part (a) — that dependency is analytic-into-geometric and sits just outside the four interfaces, but it is what makes the $Q$ and plateau estimates jointly the inputs to the projector obstruction.

---

## Cross-cutting: corrected dependency picture and the next proof objects

**Corrected status of the handoff.**
- $J_6$ persistence: valid Gronwall, genuine simplification (no $\varepsilon$-regularization, two-factor absorption linear in $F$), conditional on $K_2$ persistence + small-$\gamma$, the good-center volume relation, and moving-geometry comparability. Not unconditional.
- Existence: the Step 35 note does not recover (0.1) (missing pullback / coefficient transport) and its $\varepsilon$-independence is asserted from generic Schauder rather than the weighted-energy structure. The correct per-datum existence is Step 27 §6 / Yang Approach 1.
- Continuation: the Step 35 note is interior regularity given smoothness, using bootstrap-uncontrolled $\|T\|_\infty$ and $\|a\nabla\mathrm{Rm}\|_\infty$; it is not an extension statement. The extension statement is Step 27's shifted-tensor induction, whose detailed constant bookkeeping is asserted, not yet checked term by term.
- Global $Q$: correctly retained as a separate estimate; not replaceable by $J_6$ or $\|aE\|_\infty$.

**Next proof objects, in order of leverage on the overall argument.**
1. **Existence recovered cleanly.** Rewrite the existence step as transported-coefficient DeTurck (Yang Approach 1 / Step 27 §6): solve the gauge-fixed $\hat g$ system with $\widehat a=(\chi\circ\varphi_t^{-1})^2$, integrate the (degenerate, hence stationary on $\{\chi=0\}$) diffeomorphism ODE, and pull back to get a genuine solution of $\partial_tg=-2\chi^2(\mathrm{Ric}+g)$ with the fixed $\chi$. This removes the $\varepsilon$-route and its interface-flux problem; per-datum time suffices.
2. **Extension made independent of assumed smoothness.** Complete the Step 27 Wang-type induction so that finiteness of every $\nabla^m U$ follows from $\sup|a\mathrm{Rm}|<\infty$ alone, carrying $\mathcal L_{G,m}$ and the staggered-exponent Hölder chain explicitly through Wang Lemma 4.11 / Prop. 4.13–4.14, and never suppressing $\chi\nabla^{m+2}\chi*U$ before its single integration by parts. Then rewrite the Step 35 continuation coefficients so that near-$T_{\max}$ boundedness of $\Lambda$ comes from the Moser endpoint $\|aF\|_\infty\le C\gamma/t$, not from "the solution is smooth."
3. **$K_2$ persistence pinned down** as the standing input to $J_6$: the $q=2$ curvature energy inequality with the small-$\gamma$ absorption, including the same Hessian-$a$ integration-by-parts device, so that the $J_6$ lemma's hypothesis list is closed by an established estimate rather than a conditional one.
4. **Independent recomputation of $(\partial_t-a\Delta)s$ and $B^{ij}$** to confirm the printed reaction identities (repairing the malformed $E^{jkl}{}^p$ index in §2.2) — this is the single algebraic point the $J_6$ Gronwall rests on.
5. **Joint use of plateau $|\mathrm{Rm}_{g(T)}|$ and global $Q$** in the calibration/projector step, verifying that the terminal $|W^+|$ enters only through the sequence-uniform plateau bound and $Q$ only through the global $L^2$, so the datum-dependent transition-region jets remain non-load-bearing.

The largest structural point: the analytic handoff currently rests existence and continuation on two Step 35 notes that are weaker than they read (one does not recover the target equation, one assumes its own conclusion), while the mathematically correct versions already exist in Step 27 but at "asserted-bookkeeping" maturity. Consolidating existence+extension onto the Step 27 shifted-tensor treatment, and checking its induction line by line, is what would turn the conditional first-exit chain into an unconditional one for this 4D family — after which the remaining distance to Yau 26 (positive branch, arbitrary topology, $n\ge5$, dimension-only interval quantifiers, and the Lean formalization) is untouched by any of these four interfaces.