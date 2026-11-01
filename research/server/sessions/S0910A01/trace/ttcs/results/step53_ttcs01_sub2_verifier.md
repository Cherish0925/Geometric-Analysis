# TTCS Independent Branch Record

```json
{
  "step_id": 53,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step55_direct_nonlinear_flow_construction.md",
    "Sessions/S0910A03/workspace/scripts/verify_step55_direct_construction.py",
    "Sessions/S0910A03/workspace/data/step55_direct_construction_checks.json",
    "Sessions/S0910A01/workspace/notes/step45_consolidated_IL_negative_gap_proof.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step51.md",
    "Sessions/S0910A01/workspace/notes/step52_lefschetz_product_quotient_obstruction_scan.md"
  ]
}
```

## Task

Independently verify the mathematical substance of A03 Step55's direct nonlinear construction of the normalized cutoff flow and its interface with the restricted Ishida--LeBrun negative-gap architecture. Read the supplied A03 note, structural check script/data, and the A01 consolidated IL proof/route notes. Focus on whether the transported-cutoff DeTurck system, epsilon-regularized parabolic-plus-transport construction, epsilon-uniform H^s and all-order hierarchy, epsilon->0 passage, and pullback identity plausibly give a genuine per-datum smooth solution of ∂_t g = -2 χ^2(Ric+g). Then identify precisely what remains before the restricted IL theorem is an end-to-end proof: first-exit quantities, support/terminal chain, sequence-uniform time, or hidden derivative/epsilon losses. Do not decide the session route; give a direct scientific verification memo with load-bearing errors, corrections, and implications for the Yau 26 research state.

## Output

# Verification Memo: A03 Step 55 (direct nonlinear cutoff-flow construction) and its interface with the A01 Ishida–LeBrun no-Einstein architecture

Prepared in a clean context from the supplied A03 Step 55 note + script + JSON, the A01 Step 45 consolidated proof, and the A01 route/Lefschetz notes.

---

## A. What is mathematically sound and load-bearing

**A1. The DeTurck algebra is internally exact.** I reproduced the reduction. Using (1.3), the first line of (1.4) equals
$$-2\beta^2(\mathrm{Ric}(G)+G)+\beta^2\mathcal L_{W}G+2\,\mathrm{sym}(d(\beta^2)\otimes W^\flat).$$
The identity $\mathcal L_{fV}G=f\mathcal L_VG+2\,\mathrm{sym}(df\otimes V^\flat)$ with $f=\beta^2,V=W$ then gives (1.5) exactly. This is correct.

**A2. The pullback identity (7.1)–(7.5) is correct.** The characteristic computation (7.2) holds: with Eulerian velocity $X(t,y)=-\beta_0^2W(G_0)(t,y)$, $\tfrac{d}{dt}\beta_0(t,\varphi(t,x))=[\beta_0^2W\cdot D\beta_0]-D\beta_0\cdot[\beta_0^2W]=0$, so $\beta_0(t,\varphi)=\chi$. The transport-of-tensor identity $\partial_t(\varphi^*G)=\varphi^*(\partial_tG+\mathcal L_XG)$ combined with (1.5) cancels the Lie terms and yields $\partial_tg=-2\chi^2(\mathrm{Ric}_g+g)$ using naturality of Ricci and $\beta_0\circ\varphi=\chi$. On $\{\chi=0\}$, $X=-\beta_0^2W=0$, so $\varphi$ fixes that set and $g\equiv g_0$ there — consistent with the stationary-exterior statement. $\varphi$ is a genuine diffeomorphism because $X$ is smooth on the closed manifold. This is the strongest part of the note.

**A3. The ε-uniform joint $H^s$ estimate (§3) closes without an $\varepsilon^{-1}$ or a derivative loss, and I could confirm the load-bearing power-counting.** The essential mechanism is that the transport velocity $\beta^2W$ vanishes to second order where $\beta\to0$, matching the degenerate dissipation weight $(\beta^2+\varepsilon)$. Concretely:
- Metric commutator with $D(\beta^2)$: the factor is $2\beta D\beta$, so $\beta\,D^{k+1}G=\sqrt{\beta^2}\,D^{k+1}G\le\sqrt{\beta^2+\varepsilon}\,D^{k+1}G$; Cauchy–Schwarz absorbs it into the dissipation with a bounded residual $C_R\|D^kG\|_2^2$.
- Metric commutator with $D(G^{-1})$: carries the full coefficient $(\beta^2+\varepsilon)\le 2$, absorbed with a uniformly-bounded residual.
- The transport cross-term (3.8)–(3.10): the integrand is $\sim|D^k\beta|\,\beta^2\,|D^{k+1}G|\,|D\beta|$; splitting as $(\beta\,D^{k+1}G)\cdot(\beta|D\beta|\,D^k\beta)$ pairs exactly one $\sqrt{\beta^2+\varepsilon}$ factor against the dissipation and leaves $C_R\|D^k\beta\|_2^2$.

The only top-order object requiring dissipation is the term carrying the full $\beta^2$ weight, and its $\beta$-power matches. Every $\varepsilon$-dependent quantity enters as $\beta^2+\varepsilon\ge\beta^2$ in the good direction. This is exactly the structural fact that the earlier iteration route (Step 53) could not exploit, because a contraction there lost a derivative in the transport velocity. The direct joint solve genuinely circumvents that obstruction — a real advance, not a relabeling.

**A4. The difference estimate (§4) is coherent and its central observation is correct.** At $r=s-2$ the worst coefficient-difference term is $\omega\cdot D^{s}G_1$; $\|\omega\|_\infty\le C\|\omega\|_{H^r}$ (from $r>n/2$) and $\|D^sG_1\|_2$ from the individual $H^s$ bound give (4.5) with no interpolation of the difference. This yields ε-independent Grönwall stability and uniqueness of the DeTurck solution, hence full-sequence convergence in §6. This is the correct repair of the Step 53 problem.

**A5. ε→0 (§6) and higher regularity (§5) are sound given A3–A4.** $(\beta_\varepsilon^2+\varepsilon)G_\varepsilon^{-1}D^2G_\varepsilon\to\beta_0^2G_0^{-1}D^2G_0$ in $C^0$ from $C^2$ convergence and $\varepsilon\to0$; the all-order induction $E_s\Rightarrow E_{s+1}\Rightarrow\cdots$ is standard parabolic bootstrapping and the transport cross-coupling reproduces the A3 power-counting at each order.

**Net:** the per-datum short-time existence of a smooth solution of $\partial_tg=-2\chi^2(\mathrm{Ric}_g+g)$, smooth across the transition set $\partial\{\chi>0\}$ and stationary on $\{\chi=0\}$, is plausible and structurally coherent as stated, subject to the standard technical items §B4.

---

## B. The two load-bearing items that stand between this and an end-to-end Ric≈−g Ishida–LeBrun theorem

**B1. Family-uniform start time is unproven, and the controlling norm is the wrong one.** Theorem 9.1 controls the existence time by the fixed-background $\|g_0\|_{H^s(\bar g)}$ and $\|\chi\|_{C^s}$. The Ishida–LeBrun contradiction runs a sequence $(M_i,g_i)$ that the A01 route note explicitly permits to collapse. Under collapse, injectivity radius $\to0$, and $\|g_i\|_{H^s(\bar g)}$ in fixed coordinates can degenerate even when curvature stays bounded. So Thm 9.1's assertion "$T$ depends on $\|g_0\|_{H^s}$, not on the zero set" does **not** deliver the $T_i\ge T_0>0$ that §7–8 of A01 need. The Appendix line "$T_i\ge T_0$ from the uniform curvature-to-volume budgets" is precisely the missing bridge: it needs the existence time recontrolled by *geometric* (curvature/volume/harmonic-radius) data rather than a fixed-background Sobolev norm. A01 §5.2 candidly lists the geometric package required ($\Lambda^{-1}g_0\le g_\varepsilon(t)\le\Lambda g_0$, $\sup|U|\le K$, uniform Sobolev constants, connection-difference control) and calls it "a separate analytic module." Neither note closes it, and the two framings — an $H^s$-based time in A03, a curvature-based time in A01 — are not reconciled. This is the single most consequential open analytic object for the sign-restricted theorem, and it sits on the *start* side, not the first-exit side.

A concrete way the material could resolve it: localize the §3 energy estimate to the active plateaux $B_{5r}(x_\alpha)$, where good-set selection gives $r^4\fint|\mathrm{Rm}|^2\le\tilde\gamma^2$ (bounded curvature) and use harmonic-coordinate $H^s$ control on those balls, with the stationary exterior handling $\{a=0\}$. That is a genuine reworking of the global energy estimate, not a corollary of it.

**B2. The terminal averaging step §7.3 has an unaddressed multiplicity that can grow under collapse — a new concern.** The contradiction combines a lower bound $A_\rho\Phi(p)\ge\eta'$ (from Prop 3.2 on the tangent-space pullback) with an upper bound $\int_{P^{\rm in}}A_\rho\Phi\le C(K,\rho)\int_M\Phi\le119C\,Q$. The lower-bound direction is fine: the exponential pullback $(B_\rho(0),\tilde g)$ is genuinely noncollapsed and Prop 3.2 applies. The upper-bound direction is the exposed one. Bounded curvature gives a lower bound on the *conjugate* radius $\sim\pi/\sqrt K$ but not on the injectivity radius; collapse destroys the latter. Hence $\exp_p$ on $B_\rho$ is an immersion but generally many-to-one, and the Liouville average $A_\rho\Phi(p)=\fint_{B_\rho(0),\tilde g}\Phi$ over-represents base $\Phi$ with a multiplicity (number of short geodesic loops) that grows as the plateau collapses. Summing over $p\in P^{\rm in}$, the constant $C(K,\rho)$ claimed collapse-independent can pick up this multiplicity. The §6.4 "geodesic buffer" states only that geodesics stay inside the plateau, not that $\exp_p$ is injective, so it does not remove the effect. This must be treated explicitly — by bounding geodesic-loop multiplicity uniformly, by restricting $\rho$ below a collapse-uniform local-diffeomorphism scale, or by an argument that the relevant inner cores are noncollapsed. As written, the collapse-uniform terminal contradiction is not established.

**B3. First-exit branches (A01 §6, upstream Steps 34–36) are not supplied and cannot be checked here.** What I can confirm is that they now compute on a genuine exact $\varepsilon=0$ flow: Step 55's real service to A01 is that the disjoint-support identity $Q(T)=\sum_\alpha Q_\alpha(T)$ (Appendix A.2), the stationary complement, and frozen-outer-metric identities — valid only on the exact flow — now rest on an existing object rather than on the withdrawn Step 53 construction. Their collapse-independence ($\gamma$ collapse-free after Whitney-volume cancellation, §6.1) is meaningful only once B1 is closed.

**B4. Standard technical items acknowledged as open in §10.2/§11.** Explicit form and all-order Moser control of the DeTurck tensors $R,Q$; the explicit Galerkin/Friedrichs scheme for the coupled parabolic-plus-transport system (transport does not sit comfortably in a spectral truncation, and the energy identity (3.7) uses the exact transport form — this needs care, not merely citation); and the Sobolev multiplication lemmas. These are standard-type but not yet executed, and are prerequisites for any Lean-level formalization.

---

## C. The verification script carries no evidential weight for the analytic content

`verify_step55_direct_construction.py` records "22/22 pass," but every substantive entry is `check(name, True, detail)` with a hard-coded `True`. The only genuine computations are trivial arithmetic ($r=8>n/2=2$, $r+2=10=s$, $2p-n=0$, $s>n/2+4$). None of the load-bearing statements — dissipation sign, cross-coupling absorption, absence of $\varepsilon^{-1}$, ε-uniformity — is computed; they are transcribed as `True`. The note's §11 "22/22 structural checks pass" should therefore not be read as verifying §3–§5. The script is a consistency ledger, not a proof check (its own trailing "NOT CHECKED" list is accurate).

One internal inconsistency: script/JSON check #12 still asserts the antisymmetric identity $\int h\cdot a\cdot Dh=-\tfrac12\int|h|^2\,Da$ as PASS, whereas note correction #2 explicitly abandons that identity (it does not hold for a tensor $h$ with matrix coefficient $a=G_2^{-1}DG_2$) and replaces it with direct weighted Young. The script was not updated to match the corrected note.

---

## D. Version reconciliation between the two sessions

A01 §5 regularizes the **coefficient** ($b_\varepsilon=\chi^2+\varepsilon^2$, transported), while A03 Step 55 introduces $\beta$ as a **transported variable** and adds $\varepsilon$ to the **principal metric coefficient** $(\beta^2+\varepsilon)G^{-1}$. These are different regularizations of the same target flow; on $\{\beta=0\}$ the A03 flow moves by $\varepsilon[G^{-1}D^2G+R+Q]\to0$ while the A01 flow moves by $-2\varepsilon^2(\mathrm{Ric}+g)$. Step 55 supersedes A03 Steps 44–54 (including the "Step 45 coordinate ledger" that A01 §10 cites as its flow module). The A01 first-exit quantities $U_m=\nabla^m(aT)$ (§5.3 weighted hierarchy, §6) are computed on the exact flow and remain valid as computations on that object, but A01's §5 construction is now redundant relative to Step 55 and the module table is stale. The support conventions also differ ($\mathrm{supp}\chi_\alpha\subset B_{6r}$, 14r-separated in A01 §4.2 vs $\subset B_{5r}$, $d>12r$ in the A03 Appendix). The disjoint-support identity $\chi^2=\sum\chi_\alpha^2$ holds under either convention, but the interface is not tightly synchronized.

I also note a minor over-statement: Thm 9.1 asserts a **unique** geometric family $g(t)$, but §7's proof establishes uniqueness only for the DeTurck solution (Prop 4.1/6.1). Geometric uniqueness needs a gauge-equivalence argument (any geometric solution is the pullback of a transported-cutoff DeTurck solution). A01 §5.2 correctly states uniqueness is not needed for the contradiction, so this is not load-bearing.

---

## E. Independent checks I could complete on the topological side (A01 §2)

These are the inputs that feed the $o(A)$ upper bound on $\int\Phi$, and they hold:
- Chern–Gauss–Bonnet identity $I-J=(2\chi+3\tau)$ and the connected-sum bookkeeping: $(2\chi+3\tau)(M)=A+(2\chi+3\tau)(N)-4m=A-D$, matching $\tfrac{2A}{3}-q$ with $q=D-\tfrac{A}{3}$. Uses $(2\chi+3\tau)(X_j)=c_1^2(X_j)$ for minimal general type. Correct.
- $\int(s+4)^2\le 4Q$: since $s+4=\mathrm{tr}(E)$ in $n=4$ and $(\mathrm{tr}E)^2\le4|E|^2$ pointwise, this integrates cleanly. Correct.
- The Derdziński forbidden-germ contradiction (Prop 3.1→3.2) and its elliptic upgrade are sound: $|E|^2\to0$ in $L^2$ drives $W^{2,p}$ convergence through the harmonic-coordinate Ricci equation, not Cheeger–Gromov, so no curvature-derivative bounds are needed. The compactness constant $\eta$ is non-explicit but that is acceptable for a contradiction.

The $108Q$ and $6Q$ bounds in (2.11) rely on the Step-42 completion-of-squares/self-dual spectral algebra, which is not supplied; the $4Q$ bound checking cleanly is mild positive evidence for that family.

---

## F. Implications for the Yau 26 research state

1. Step 55 upgrades the flow-start module from "withdrawn/open" (Step 53) to "structurally coherent per-datum smoothing," and this is the correct object on which A01 §6's exact-flow identities live. The prior derivative-loss obstruction is genuinely resolved by the direct joint solve. This is the concrete forward motion.

2. The sign-restricted Ishida–LeBrun no-Einstein argument is **not yet end-to-end**. Two analytic objects remain load-bearing: (B1) a family-uniform, geometry-controlled start time replacing the fixed-background $H^s$ time; and (B2) collapse-uniform control of the terminal Liouville-average multiplicity. B1 is flagged by both sessions; B2 is not flagged and should be examined explicitly, because the same collapse that the tangent-pullback device exploits for the lower bound threatens the upper bound.

3. Even fully completed, this addresses only the Ric$\approx-g$ (attractive-sign) four-dimensional Ishida–LeBrun family. The Ric$\approx+g$ branch, arbitrary four-manifold topology, $n\ge5$, dimension-only constants $c_n<C_n$, and the Lean 4 formalization all remain untouched by this chain. The parallel product-quotient work (Steps 50–52) proves Einstein *existence* on specific $b_+=1$ manifolds outside the Ishida–LeBrun geography (reinforcing a positive-answer expectation for those types) and the Lefschetz scan correctly finds that the $H^2(X,T_X^0)=0$ sufficient mechanism does not extend beyond the $K^2=2,\ \mathbb Z_4^2$ row — but neither settles the dimension-only proposition.

**What would most change the research judgment:** an explicit statement and proof that the §3 energy estimate can be localized to bounded-curvature, harmonic-radius-controlled plateaux with a start time depending only on $(K,r,v_0)$-type geometric data (closing B1), together with a collapse-uniform bound on the geodesic-loop multiplicity in the §7.3 averaging (closing B2). These two are the concrete objects on which the sign-restricted theorem's status now turns; the algebraic and single-datum-existence content behind them is, as far as I can verify, correct.