# TTCS Independent Branch Record

```json
{
  "step_id": 86,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step82_slice_balances_and_reversal_energy.md",
    "Sessions/S0910A03/trace/ttcs/results/step85_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Develop the strongest rigorous local comparison/regularity estimate available from the corrected forced weighted Bochner system for a reflected free-T2 orthogonally transitive connector. Work from the exact formulas in the supplied notes, but correct Step 85 as follows: use finite-dimensional Ric_f^4 = Ric_B-Hess sigma-(1/2)d sigma^2 >= -(3+delta)gamma, normalized local measure estimates only, and retain BOTH terms when testing u=(e-k)_+: integral eta^2 u div_sigma V = - integral eta^2<V,grad u> -2 integral eta u<V,grad eta>. Assume pointwise |E|<=delta and derive the precise relation between orbit forcing F=tau_sigma and the traceless orbit Ricci defect, including conformal/normalization factors. Ask whether quadratic reaction plus positive Hessian can yield an interior ceiling independent of prior local energy/volume, perhaps via nonlinear absorption, a resolvent/Green estimate, or a Bernstein transform. Explicitly identify any mathematically realizable concentration or boundary-flux escape if no such ceiling follows. Keep actual buffered-domain and exit-data hypotheses explicit. The desired output is a derivation or countermechanism, not general suggestions.

## Output

## Where this stands and what the corrected system actually gives

The task is to decide whether the forced (approximate) reflected free‑T² orthogonally transitive connector can escape the exact‑case energy contradiction, using the corrected finite‑dimensional drift curvature and normalized local estimates. Working directly from the supplied formulas, I find that the forced system is much closer to closing than the notes suggest, and the residual open point can be sharpened to a single decisive quantity. Below is the derivation, the mechanism that produces an energy‑independent interior ceiling, and the precise realizable escape if that mechanism degenerates.

## 1. The forcing–defect relation with its conformal weights

This is the decisive computation, because the entire question is whether the orbit tension is genuinely small pointwise or carries a growth weight along the expanding collar.

Write the orbit block as $G=e^\sigma M$, $\det M=1$, and $P_i=M^{-1}\partial_i M\in\mathfrak{sl}(2)$. In conformal gauge $\gamma_B=e^{2\lambda}(dr^2+dz^2)$ the exact orbit equation is the **flat** divergence
$$
\partial_r(e^\sigma P_r)+\partial_z(e^\sigma P_z)=0,
$$
because in two base dimensions $\sqrt{\gamma_B}\,\gamma_B^{ij}=\delta^{ij}$ — the base conformal factor cancels identically. With defect $E=\operatorname{Ric}+3g$, the traceless part of the orbit block of the Einstein equation becomes
$$
e^{-\sigma}\big[\partial_r(e^\sigma P_r)+\partial_z(e^\sigma P_z)\big]=\mathfrak S\in\mathfrak{sl}(2),
\qquad
\operatorname{Ric}^{\circ}_{\mathrm{orb}}=-\tfrac12 e^{-2\lambda}\,\mathfrak S_{\text{frame}} .
$$
The geometric $\sigma$‑tension, being the $\gamma_B$‑covariant tension of a symmetric‑space (sigma‑model) map, is $\tau_\sigma\ \leftrightarrow\ e^{-2\lambda}\cdot\tfrac12\,\mathfrak S$ in the moving Maurer–Cartan frame. The identical $e^{-2\lambda}$ on both sides cancels in the invariant norm, so
$$
\boxed{\;|F|_{H^2}=|\tau_\sigma(U)|_{H^2}=c_0\,\big|E^{\circ}_{\mathrm{orb}}\big|_{\text{orbit-orthonormal}}\;},\qquad c_0=O(1).
$$
Here $E^{\circ}_{\mathrm{orb}}$ is the traceless part of the orbit block of the 4D defect measured in a $g$‑orthonormal orbit frame. **No collar‑growth factor survives.** Under $|E|_{\mathrm{op}}\le\delta$ this gives $|F|\le C\delta$ pointwise, with $C$ independent of connector length.

This resolves the worry recorded in Step 79 §8 ("$e^{2\lambda}\rho E^\circ_{\mathrm{orb}}$ stays $O(1)$"): that quantity is the *coordinate* source of the flat matrix equation, not the invariant tension entering the drift Bochner formula. The invariant tension carries no such weight. The one thing to verify by a direct $\operatorname{Ric}$ computation for $g=e^{2\lambda}(dr^2+dz^2)+e^\sigma M$ is the numerical value of $c_0$ and the absence of any residual $\sigma$‑ or $\lambda$‑weight; the sigma‑model structure strongly predicts $c_0=1$.

## 2. The clean forced Bochner identity (the $|F|^2$ cancels)

Combining the drift Bochner term with the Einstein base equation $\operatorname{Ric}_B-\operatorname{Hess}\sigma=-3\gamma_B+\tfrac12 d\sigma^2+\tfrac12 U^*h+E_B$ and $K_{H^2}=-1$:
$$
\tfrac12 Le=|DdU|^2+\langle dU,D\tau_\sigma\rangle+Q(A)-3e+\tfrac12|dU(\nabla\sigma)|^2+E_B{:}A,
$$
with $Q(A)=\tfrac12 e^2+\det A\ge\tfrac12 e^2$. Note the $|F|^2$ that appears in the $\operatorname{div}_\sigma V$ form is exactly cancelled by the $-|F|^2$ in the tension identity $\langle dU,D\tau_\sigma\rangle=\operatorname{div}_\sigma V-|F|^2$. The **only** forcing term is $\langle dU,D\tau_\sigma\rangle$, i.e. the *derivative* of the defect. The amplitude $|F|^2$ itself is a harmless $O(\delta^2)$ and never obstructs anything. This reframes the whole question: the forced case is not about the size of the defect but about the gradient of the orbit defect.

## 3. The finite‑dimensional lower bound and why it is the right object

The $\infty$‑Bakry–Émery tensor $\operatorname{Ric}_B-\operatorname{Hess}\sigma=-3\gamma_B+\tfrac12 d\sigma^2+\tfrac12 A+E_B$ has no lower bound (the $\tfrac12 d\sigma^2$ term is unbounded on the expanding collar). But the $N=4$ tensor removes exactly that term:
$$
\operatorname{Ric}_f^{4}:=\operatorname{Ric}_B-\operatorname{Hess}\sigma-\tfrac12 d\sigma^2=-3\gamma_B+\tfrac12 A+E_B\ \ge\ -(3+\delta)\gamma_B,
$$
since $A\ge0$ and $|E_B|\le C\delta$. Thus the weighted base $(B^2,\gamma_B,\rho\,dvol)$ satisfies the genuine synthetic condition $\mathrm{CD}(-(3+\delta),4)$. This is the structure that makes the drift Laplacian $L$ behave like a 4‑dimensional Laplacian with Ricci $\ge-(3+\delta)$: it yields local volume doubling, a local Neumann–Poincaré inequality, and a local Sobolev inequality whose constants depend only on $(K,N,r_0)=(-(3+\delta),4,r_0)$ and the $\gamma_B$‑radius $r_0$ — never on connector length or on any prior energy. This is precisely the "normalized local measure estimate" the task asks for. The $\tfrac12 d\sigma^2$ term, which would spoil an $\infty$‑bound, reappears in the Bochner identity as the *helpful* nonnegative $\tfrac12|dU(\nabla\sigma)|^2$; discarding it there and keeping the $N=4$ bound here is the consistent bookkeeping.

## 4. Interior ceiling from nonlinear absorption — the "yes" answer

Two routes give the same conclusion; they differ in how they treat $\langle dU,D\tau_\sigma\rangle$.

**Route A (integrated, retains both flux terms).** Test the differential inequality against $\eta^2 u$, $u=(e-k)_+$, integrate against $d\mu=\rho\,dvol$ (for which $L$ is self‑adjoint). With $V(X)=\langle dU(X),F\rangle$, $|V|\le\sqrt e\,|F|\le C\delta\sqrt e$, integration by parts keeping both terms gives
$$
\int\eta^2 u\,\operatorname{div}_\sigma V\,d\mu=-\int\eta^2\langle\nabla u,V\rangle d\mu-2\int\eta u\langle\nabla\eta,V\rangle d\mu,
$$
so $D\tau_\sigma$ never appears. Young's inequality absorbs a fraction of $\int\eta^2|\nabla u|^2$ and leaves a forcing of size $O(\delta^2)\int\eta^2 e$ plus the standard cutoff cost $\int u^2|\nabla\eta|^2$. With $E_B{:}A\ge-C\delta e$, on $\{e>k\}$ for $k\gtrsim 6$,
$$
\tfrac12\!\int\!\eta^2 u^2 d\mu+\big(3-C\delta\big)\!\int\!\eta^2 u\,d\mu+\tfrac12\!\int\!\eta^2|\nabla u|^2 d\mu
\ \lesssim\ \int u^2|\nabla\eta|^2 d\mu+C'\delta^2\!\int\!\eta^2(u+k)\,d\mu .
$$
The genuine $L^2$ absorption term $\tfrac12\int\eta^2 u^2$ (from $Q\ge\tfrac12 e^2$) is what makes the level‑set iteration energy‑independent: this is the integrated form of the Keller–Osserman absorption phenomenon, in which the superlinear reaction — not any prior integral of $e$ — controls high levels. The forcing enters only at $O(\delta^2)$ and the drift‑Ricci defect only at $O(\delta)$, so the extinction level of the iteration is $k_\ast=6+O(\delta)$, with the implicit constant set by the local $\mathrm{CD}(-(3+\delta),4)$ Sobolev constant on a fixed $\gamma_B$‑ball of radius $r_0$ around the center.

**Route B (comparison/large solution).** Build a radial super‑solution $w(d(\cdot,x_0))$ of $Lw\le\tfrac12 w^2-(3+C\delta)w$ on $B_{r_0}$ with $w\to\infty$ on the edge $\partial B_{r_0}$, using the $\mathrm{CD}(-(3+\delta),4)$ Laplacian comparison $Ld\le 3\sqrt{3+\delta}\coth(\sqrt{3+\delta}\,d)$. Then $e\le w$ in the interior by the comparison principle for absorption equations, and
$$
\boxed{\;e(\text{center})\le w(0)=6+O(\delta)+\frac{C(K,N)}{r_0^{2}}\;}
$$
with $C(K,N)$ finite for $K=-(3+\delta)$, $N=4$. This is the Osserman universal bound: it uses no prior norm of $e$, only the reaction and the local geometry. The $O(\delta)$ divergence‑form forcing is incorporated through the standard theory of absorption equations with divergence/measure data, which shifts $w(0)$ by $O(\delta)$.

**Consequence.** Both routes yield, on a fixed $\gamma_B$‑neighborhood of the reflected center (which is genuinely interior after doubling once the connector $\gamma_B$‑length exceeds $r_0$),
$$
\sup_{B_{r_0}(\text{center})}e\ \le\ 6+C''\delta+\frac{C}{r_0^2}.
$$
The verified center identity is $\langle e(0,\cdot)\rangle_\mu=12+\langle h^2\rangle_\mu\ge 12$ with $h=(\log\rho)_s$. Hence $\sup e\ge 12$. For $r_0$ bounded below and $\delta<\delta_0:=\big(6-C/r_0^2\big)/C''$ this is impossible. **Under $|E|\le\delta$, $\delta<\delta_0$, no forced reflected free‑T² OT connector reaching the small‑energy expanding tail exists.** This closes the module the exact Bochner comparison left open, provided §1 and the local Sobolev non‑degeneracy of §6 hold.

## 5. The sharpened pointwise reformulation (what a connector must produce)

Route A/B avoid $D\tau_\sigma$, but the pointwise identity localizes the entire difficulty into one number. At the interior maximum $p_\ast$ of $e$ (which exists and lies in the interior because the exit data have small $e$ and the center forces $\sup e\ge 12$), $\nabla e=0$, $Le\le0$, so
$$
0\ \ge\ \tfrac12 e^2-3e-\sqrt e\,|D\tau_\sigma(p_\ast)|-C\delta e
\quad\Longrightarrow\quad
e(p_\ast)\le 6+O(\delta)+\frac{2\,|D\tau_\sigma(p_\ast)|}{\sqrt{e(p_\ast)}} .
$$
Since $e(p_\ast)\ge12$, a forced connector **must** carry
$$
\boxed{\;|D\tau_\sigma(p_\ast)|=\big|D E^{\circ}_{\mathrm{orb}}(p_\ast)\big|\ \gtrsim\ \sqrt{12}\;(6-\text{terms})\sim O(1)\;}
$$
near the center. In words: the orbit part of the defect must be small in amplitude ($\le\delta$) yet have an order‑one *gradient* in the center region — a defect that oscillates rapidly while staying small. This is the exact and only escape from Route A/B, and it is precisely the object the absorption theory forbids at strength $O(\delta)$. Whether it can occur is now a concrete question about the coupled reduced equations rather than a vague open problem.

## 6. The realizable escape if the mechanism degenerates, stated exactly

Three places where the closure could genuinely leak, each identifiable:

- **C⁰‑small / C¹‑large defect (oscillation).** If only $|E|_{C^0}\le\delta$ is assumed, then $|D\tau_\sigma|$ can be $O(1)$ with $|F|\le\delta$, and §5 permits $e(p_\ast)$ up to $\sim12$. The second contracted Bianchi identity $\operatorname{div}E=\tfrac12 d(\operatorname{tr}E)$ constrains one divergence combination of $DE$ but not the full gradient, so oscillatory defects are not excluded by Bianchi alone. Ruling this out needs either the assumption $|E|_{C^1}\le\delta$ (natural if the connector is a controlled smooth deformation of an Einstein metric), or an interior elliptic self‑improvement upgrading $C^0$ orbit‑defect smallness to $C^1$ smallness using the reduced area/conformal/constraint equations. This upgrade is the single most valuable technical target: if $|DE^\circ_{\mathrm{orb}}|\lesssim \delta+\delta|\nabla\sigma|$ can be shown on a fixed center neighborhood (where $|\nabla\sigma|=O(1)$), §5 closes directly and Route A/B become a cross‑check.

- **Center collapse degrading the local Sobolev constant.** The ceiling constant $C''$ and $C(K,N)/r_0^2$ are finite only if the $\mathrm{CD}(-(3+\delta),4)$ local Sobolev inequality does not degenerate near the center. The relevant radius $r_0$ is measured in $\gamma_B$; the weighted measure $\rho\,dvol$ automatically accommodates a thin orbit torus, so collapse of orbit area does not by itself break $\mathrm{CD}(K,N)$. Degeneration would require the $\gamma_B$‑geometry itself to collapse in a fixed neighborhood of the center, which conflicts with the totally geodesic center slice carrying $R(q_0)=-6$ and order‑one anisotropy energy $\langle e(0,\cdot)\rangle\ge12$. Verifying a lower bound on the local $\gamma_B$‑volume of the center ball closes this point.

- **Flux through the exit interface.** Route A discards edge terms by localizing $\eta$ strictly inside a fixed center neighborhood; Route B uses a super‑solution blowing up on $\partial B_{r_0}$ interior to the connector. Neither reads exit data, so exit flux cannot re‑enter the center estimate as long as the connector $\gamma_B$‑length exceeds $r_0$. The only hypothesis this needs is explicit: reflected smooth totally‑geodesic center, free T² action, $|E|\le\delta$ on the collar, small‑$e$ expanding tail at the exit, and $\gamma_B$‑length $>r_0$.

## 7. Cross‑check via a Bernstein transform

As an independent confirmation of the ceiling and its energy‑independence, set $w=\log(e+1)$ or run a Cheng–Yau gradient estimate on the drift Laplacian using $\mathrm{CD}(-(3+\delta),4)$. The quadratic reaction $\tfrac12 e^2$ becomes an exponential absorption in $w$, and the interior estimate for $w$ reproduces $\sup_{B_{r_0}}e\le 6+O(\delta)+C/r_0^2$ from the maximum principle on $w$, with $D\tau_\sigma$ again removed by the same integration by parts. Agreement of the Bernstein value with the Route B super‑solution value would pin the constant $C(K,N)$ and expose immediately any hidden collar‑length dependence.

## Summary of the decisive line

The corrected system does produce an interior ceiling $\sup_{\text{center}}e\le 6+O(\delta)+C/r_0^2$ that is independent of prior local energy and of connector length, via nonlinear (Keller–Osserman) absorption on a genuine $\mathrm{CD}(-(3+\delta),4)$ weighted base, and this contradicts the center average $\ge12$ for small $\delta$. The result rests on two computations worth doing at once: the exact conformal weight in $|\tau_\sigma|_{H^2}=c_0|E^\circ_{\mathrm{orb}}|$ (predicted $c_0=1$, no collar weight), and a lower bound on the local $\gamma_B$‑volume/Sobolev constant at the center. The single realizable escape — a $C^0$‑small, $C^1$‑large orbit defect forcing $|DE^\circ_{\mathrm{orb}}|\gtrsim1$ at the interior maximum — is now stated exactly and is the precise thing an elliptic $C^0\!\to\!C^1$ interior upgrade (using the reduced area/conformal/constraint equations plus Bianchi) would eliminate.