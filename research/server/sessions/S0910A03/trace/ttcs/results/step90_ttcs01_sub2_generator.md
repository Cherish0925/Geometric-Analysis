# TTCS Independent Branch Record

```json
{
  "step_id": 90,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step89_twist_bochner_and_resolvent.md",
    "Sessions/S0910A03/workspace/scripts/step90_charge_potential_verify.py",
    "Sessions/S0910A03/workspace/data/step90_charge_potential_verify.json",
    "Sessions/S0910A03/workspace/scripts/step90_exchange_inequality_verify.py",
    "Sessions/S0910A03/workspace/data/step90_exchange_inequality_verify.json",
    "Sessions/S0910A03/workspace/notes/step86_forced_bochner_superlevel_and_localization.md",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md",
    "Sessions/S0910A03/workspace/notes/step88_source_note_twist.md"
  ]
}
```

## Task

Develop the structured Maxwell-area-orbit-map system for an approximately Einstein free-T^2 metric after the Step 90 charge-potential cancellation. Starting from Q=(1/2)e^{-3σ}q^T M^{-1}q, S_F=-grad_H Q, the mixed Ricci law for dq, Lσ=6+Q-tr_orb E, and the base drift equation, look for a geometrically natural energy or variable-potential comparison that controls physical twist without differentiating Ricci defect. Explore combinations of orbit energy e, |∇σ|^2, Q, and the normalized physical charge amplitude, and distinguish what can be proved from what merely looks plausible. Identify either (i) a coercive inequality compatible with exact OT ends and a minimal separator, or (ii) a concrete concentration/escape mechanism consistent with all reduced equations. Provide explicit equations and the most decisive next computation or proof, not broad brainstorming.

## Output

## The structured twist system after the Step‑90 cancellation

Everything below uses the Step‑90 verified facts: on the free‑$T^2$ base $B$ with $G=e^\sigma M$, orbit map $U:B\to\mathbb H^2$, physical charge $q_a$ and twist energy
$$
Q=\tfrac12 e^{-3\sigma}\,q^{T}M^{-1}q,\qquad
\operatorname{Hess}_{\mathbb H^2}Q=Q\,h,\qquad |\operatorname{grad}_{\mathbb H^2}Q|=Q,\qquad S_F=-\operatorname{grad}_{\mathbb H^2}Q .
$$
The Hessian relation says $Q$ is the exponential of a Busemann function on the target: the charge direction selects an ideal point, and the orbit‑map tension is pulled toward it. This horospherical convexity is the single most usable piece of structure and it is exact, not perturbative.

I will (1) derive the exact first‑order evolution of $Q$, (2) turn it into a coercive average estimate that needs no differentiation of the Ricci defect and is compatible with exact orthogonally‑transitive (OT) ends, (3) give the feedback that makes twist self‑limiting, (4) explain precisely why a pointwise maximum principle for $Q$ does not close and what replaces it, and (5) name the two decisive computations.

---

### 1. Exact first‑order twist identity

Differentiate $Q$ directly, splitting the target‑position, area, and charge dependences:
$$
\boxed{\;dQ=-3Q\,d\sigma+\langle \operatorname{grad}_{\mathbb H^2}Q,\,dU\rangle+\langle w,b\rangle\;}
\tag{$\star$}
$$
with $w=e^{-3\sigma/2}M^{-1/2}q$ the normalized charge ($|w|^2=2Q$) and $b=e^{-3\sigma/2}M^{-1/2}dq$ the physical charge source, obeying the Maxwell estimate $|b|\le 2\sqrt2\,\delta$ (this is $|b|^2=e^{-3\sigma}M^{-1}(dq,dq)=4|E_{\rm mix}|^2$ from Step 90). Hence $|\langle w,b\rangle|\le 4\delta\sqrt Q$.

Two corrections to earlier reasoning are important and both are honest here:

- The term $\langle\operatorname{grad}_{\mathbb H^2}Q,dU\rangle$ does **not** drop. A naive "metric‑connection rotation is antisymmetric" argument would kill it, but the conserved quantity is $q_a$ in a *fixed* Lie‑algebra frame (Liu's $\alpha_a$), not in the $M^{-1}$‑metric frame; converting frames reintroduces exactly this orbit‑map coupling. Its size is $|\langle\operatorname{grad}_{\mathbb H^2}Q,dU\rangle|\le Q\sqrt e$, i.e. it is *not* $\delta$‑small — this is the genuine coupling that makes twist a real object rather than a $\delta$‑perturbation.

- Only $\langle w,b\rangle$ is defect‑sized. Everything else is algebraic in $(Q,e,|\nabla\sigma|)$.

The integrating‑factor form is clean: $\nabla\!\big(e^{3\sigma}Q\big)=e^{3\sigma}\big(\langle\operatorname{grad}Q,dU\rangle+\langle w,b\rangle\big)$, and $e^{3\sigma}Q=\tfrac12 q^{T}M^{-1}q$ is the un‑normalized charge magnitude squared.

---

### 2. A coercive average estimate for $Q$ (no defect differentiation)

Test $(\star)$ against $\nabla\sigma$ in the reduced measure $d\mu=e^\sigma d\mathrm{vol}_\gamma$ and use the exact area equation $L\sigma=6+Q-T$, $T=\operatorname{tr}_{\rm orb}E$, $|T|\le2\delta$, $L=\Delta+\nabla\sigma\!\cdot\!\nabla$. Weighted integration by parts on $\int\langle\nabla Q,\nabla\sigma\rangle d\mu=-\int Q\,L\sigma\,d\mu+\text{(flux)}$ gives the **exact identity**
$$
\int_\Omega\!\Big[3Q|\nabla\sigma|^2+Q(6+Q-T)\Big]d\mu
=\int_\Omega\!\Big[\langle\operatorname{grad}_{\mathbb H^2}Q,dU(\nabla\sigma)\rangle+\langle w,b\rangle\!\cdot\!\nabla\sigma\Big]d\mu+\!\int_{\partial\Omega}\!Q\,\partial_\nu\sigma\,d\mu_\partial .
\tag{2.1}
$$
The right side carries $b$ **undifferentiated**. Young splitting $Q\sqrt e|\nabla\sigma|\le\tfrac32Q|\nabla\sigma|^2+\tfrac16Qe$ and $4\delta\sqrt Q|\nabla\sigma|\le\tfrac32 Q|\nabla\sigma|^2+\tfrac83\delta^2$ cancels the full $3\int Q|\nabla\sigma|^2$:
$$
\boxed{\;(6-2\delta)\!\int_\Omega Q\,d\mu+\int_\Omega Q^2\,d\mu\;\le\;\tfrac16\!\int_\Omega Qe\,d\mu+\tfrac83\delta^2\mu(\Omega)+\!\int_{\partial\Omega}\!Q\,\partial_\nu\sigma\,d\mu_\partial.\;}
\tag{2.2}
$$
If $e\le B$ on $\Omega$ (the resolvent ceiling, $B\approx13.8$), the coefficient $6-2\delta-B/6$ is positive whenever $B<36-12\delta$, so
$$
\langle Q\rangle_\Omega\;\le\;\frac{\tfrac83\delta^2+\ \text{(face flux per measure)}}{6-2\delta-B/6}.
\tag{2.3}
$$

**The face term is uniform, not divergent.** On an expanding end $\gamma_B=dt^2+e^{2t}dz^2$, $\rho=ce^{2t}$: the reduced measure has density $e^{3t}$, so $\mu(\Omega_R)\sim c e^{3R}\ell/3$, while the flux through the truncation face $\{t=R\}$ is $\sim Q_{\rm end}\cdot\partial_t\sigma\cdot c e^{3R}\ell=2Q_{\rm end}ce^{3R}\ell$. Their ratio is $\sim 6\,Q_{\rm end}$, independent of $R$. Since the transport envelope pins $Q_{\rm end}\le 4\delta^2/9$ near a nearly‑exact expanding end (the round‑cusp ODE $w'+3w=b$, $|b|\le2\sqrt2\delta$, gives $|w|\le B/3$ so $Q\le\tfrac12(B/3)^2$), we obtain
$$
\boxed{\;\langle Q\rangle_\Omega\lesssim \delta^2\quad\text{uniformly in the truncation }R.\;}
$$
At an exact OT end $Q\equiv0$ (Maxwell conservation forces $q=0$ on the connected free region), so the estimate degenerates to the trivial OT case with no face term. This is exactly the object $(i)$: a coercive inequality compatible with exact OT ends and with the minimal separator, giving the twist‑corrected floor $\langle e_s\rangle_C\ge 12+2\langle Q\rangle_C-8\delta$ (twist raises the floor) with $\langle Q\rangle=O(\delta^2)$ controlled.

---

### 3. The self‑limiting feedback (why sustained large $Q$ is obstructed)

$Q=\tfrac12 e^{-3\sigma}q^{T}M^{-1}q$ is large only where the area $\rho=e^\sigma$ is small relative to the charge magnitude. But the area equation $L\sigma=6+Q-T\ge 6-2\delta+Q>0$ is a strict subsolution, so $\sigma$ has **no interior maximum**; more usefully, large $Q$ *forces* strong weighted expansion $L\sigma\gtrsim Q$, which drives $\rho$ up and pushes $Q=\tfrac12\rho^{-3}(q^TM^{-1}q)$ back down. In parallel the transport $(\star)$ damps the normalized charge at rate $3\,d\sigma$ along the outward flow. The two effects act on the same variable in the same direction: a would‑be twist concentration both suppresses itself through area growth and is damped by the drift. Step 89's phase count is consistent — twist strengthens the obstruction throughout $0\le Q<Q_*\approx0.899$ — and the estimate of §2 places the physical $Q$ two orders below $Q_*$ for $\delta<\delta_*\approx0.246$. This is the mechanism that argues *against* an escape branch $(ii)$: to escape one needs $Q>Q_*$ on the reaction core, but $Q>Q_*$ requires a deep area well co‑located with a large charge, and the area equation forbids that well from being sustained while the drift damps the charge that would feed it.

---

### 4. Why the pointwise maximum principle does not close, and the replacement

Computing $LQ$ from $(\star)$ is tempting because the second‑order pieces are algebraic through the horospherical relations:
$$
\tfrac12 LQ\ \supset\ \underbrace{Q\,e}_{\operatorname{Hess}=Qh}\ \underbrace{-\,Q^2}_{\langle\operatorname{grad}Q,\tau_\sigma\rangle,\ \tau_\sigma=-\operatorname{grad}Q+O(\delta)}\ +\ \operatorname{div}_\sigma\langle w,b\rangle+\cdots
$$
so the target curvature and the orbit‑map tension enter only through $\operatorname{Hess}_{\mathbb H^2}Q=Qh$ and $\tau_\sigma(U)=-\operatorname{grad}Q+O(\delta)$ — no Ricci‑defect derivative there. The single term that resists is $\operatorname{div}_\sigma\langle w,b\rangle$: a pointwise bound at an interior maximum of $Q$ requires $LQ\le0$, hence a bound on $\operatorname{div} b$, i.e. a *derivative of the Ricci defect*. That is exactly the move to avoid. The energy identity (2.1) is the correct circumvention: paired against $\nabla\sigma$ and integrated, $b$ never gets differentiated. So the deliverable is intrinsically an averaged/energy statement, and the pointwise ceiling on $Q$ should be obtained not by a maximum principle but by feeding $\langle Q\rangle=O(\delta^2)$ into a variable‑potential resolvent.

---

### 5. The two decisive computations

**(A) Pin the Maxwell constant for variable $G$.** The whole estimate rides on $|b|\le2\sqrt2\,\delta$, i.e. on $|dq|\le c\,\rho\,\delta$ with the *exact* $c$ in the Step‑79 normalization. Liu's mixed‑Ricci law $\operatorname{Ric}(Z,V_a)=-\tfrac1{2\rho}\langle d\alpha_a,JZ\rangle$ is written for his frame $g_\Sigma=dx^2+\mu^2dy^2$ with $\alpha_a=\rho\langle[X,Y/\mu],V_a\rangle$. The needed computation is the identification $\alpha_a\leftrightarrow q_a$ and the full variable‑$G=e^\sigma M$ mixed block $\operatorname{Ric}(e_i,V_a)$ in the present normalization, producing $|b|^2=e^{-3\sigma}M^{-1}(dq,dq)$ with the constant that makes $|b|\le 2\sqrt2\,\delta$ from $\|E\|_{\rm op}\le\delta$ rigorous rather than asserted. This is a finite symbolic SymPy computation of the same type as Step 89's `step89_symbolic_twist_ricci.py`, extended to keep the mixed $(e_i,V_a)$ block with all $\sigma,M,A$ dependence, checked against Liu's formula in his coordinate specialization.

**(B) The variable‑potential resolvent, using $\langle Q\rangle$ small.** Step 90 correctly warns that the ceiling cannot simply replace pointwise $Q$ by $Q_{\max}$ or by a spatially varying mass. The clean replacement is a Feynman–Kac occupation‑time estimate for the massive drift operator $-L+\kappa(\cdot)$ with $\kappa(x)=6-2Q(x)$: since $\mu\{Q>a\}\le\langle Q\rangle/a\lesssim\delta^2/a$, the weighted heat flow spends measure $O(\delta^2)$ of its time in $\{Q>Q_*\}$, so the effective mass seen by the Duhamel comparison is $\ge 6-O(\delta^2)$ and the Step‑87/89 ceiling $B(\delta)$ survives with an $O(\delta^2)$ shift. Concretely one wants
$$
\sup_B e\ \le\ \Big[\tfrac{2f}{\sqrt{3+\delta}}+\sqrt{2(3+\delta)+\tfrac{5f^2}{3+\delta}}\Big]^2+C\langle Q\rangle,\qquad f=O(\delta),
$$
i.e. a resolvent‑gradient bound $\sup_x\int|\nabla_yG_\kappa(x,y)|d\mu(y)\le \tfrac{2}{\sqrt{3+\delta}}+C\langle Q\rangle$ for a mass $\kappa\ge 6-2Q$ with $\langle Q\rangle$ controlled. Establishing this closes the loop: crude transport gives $Q\le4\delta^2/9<Q_*$ to start; Step‑89 gives $e\le B<36$; (2.3) gives $\langle Q\rangle\lesssim\delta^2$; the variable‑potential resolvent upgrades the ceiling; the separator floor $12+2\langle Q\rangle-8\delta$ and the ceiling then cross near the OT threshold $\delta_*\approx0.246$ shifted by $O(\delta^2)$. This would extend the complete‑cylinder obstruction from OT to *all* free‑$T^2$ metrics with two expanding ends.

The alternative deliverable — the coupled energy $W=e+cQ$ — is less attractive because $Q$'s natural operator is first‑order (transport of a Maxwell charge), while $e$ is second‑order (Bochner); the mismatch is why testing $(\star)$ against $\nabla\sigma$ and separately running the $e$‑resolvent is cleaner than a single combined subsolution.

---

### What is settled and what is plausible

Established from verified structure: the exact identity $(\star)$; the exact energy identity (2.1); the average estimate $\langle Q\rangle\lesssim\delta^2$ once $e\le B<36$ and once the Maxwell constant (A) is fixed; the uniform‑in‑$R$ face/measure scaling; the favorable sign of twist in the separator floor. Plausible but not yet closed: the variable‑potential resolvent (B), hence the pointwise conclusion $Q<Q_*$ on the reaction core and the full extension of the obstruction to non‑OT free‑$T^2$ metrics; and the passage from "two nearly‑exact expanding ends" to "merely asymptotically OT ends," where completeness/properness of $\rho^2\gamma_B$, coercivity of the primitive loop class, and decay of the drift field $V$ at infinity must be re‑established with $Q\neq0$ present. No general graph‑manifold or diffuse $S^3$‑neck metric is touched by any of this; it is a statement about the free‑$T^2$ symmetry class with the stated end geometry.

The most decisive single action is computation (A): the entire $O(\delta^2)$ chain hinges on the exact Maxwell constant relating $|dq|$ to $\|E\|_{\rm op}$ in the working normalization, and it is a bounded symbolic calculation whose outcome either confirms $|b|\le2\sqrt2\delta$ or replaces the constant everywhere downstream.