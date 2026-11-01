# TTCS Independent Branch Record

```json
{
  "step_id": 71,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step70_critical_identity_and_corrections.md",
    "Sessions/S0910A03/workspace/notes/step70_mixed_boundary_formulation.md",
    "Sessions/S0910A03/workspace/scripts/step71_linearized_detruck_hyperbolic.py",
    "Sessions/S0910A03/workspace/data/step71_linearized_detruck_hyperbolic.json",
    "Sessions/S0910A01/workspace/notes/step72_graph_neck_weighted_shear_budget.md",
    "Knowledge/objects/papers/Poincaré-Einstein-4-manifolds-with-cusps--d36d062e94d0--09d8ca1fbe38/object.md"
  ]
}
```

## Task

The active goal is Yau Problem 26, but this task concerns the current negative-branch graph-neck route. Read the Step 70 and Step 71 materials plus the Li–Liu source excerpts. Independently derive and check: (i) the correct weighted normal balance for E=Ric+3g in Gaussian gauge; (ii) whether a complete exact reflection-symmetric half-core with a flat T^3 Poincare-Einstein end is ruled out by doubling and Proposition 6.6 (Witten–Yau/Cai–Galloway), including the warped-product exception; (iii) a complementing, reflection-compatible boundary formulation for the five T^2-invariant metric components in Einstein–DeTurck/Bianchi gauge. Be explicit about parity at t=0, which central metric data may vary, what geometric and gauge data belong at t=R, and why a zero of the gauge-fixed equations is or is not automatically Einstein on a manifold with boundary. Correct any sign, normalization, or boundary-count errors; do not infer nonlinear existence.

## Output

## Verification memo — weighted normal balance, doubling exclusion, and the reflection-compatible DeTurck end-data formulation

I re-derived the three items independently from the Gaussian-gauge geometry and the Li–Liu source. Signs, normalizations, and counts below are checked against the SymPy output quoted in the notes and against Proposition 6.6 as stated in the source.

### (i) The weighted normal balance is correct, with consistent signs

For $g=dt^2+h_t$ with shape endomorphism $S=\tfrac12 h_t^{-1}\partial_t h_t$, $H=\operatorname{tr}S$, the Riccati/Raychaudhuri identity is
$$\operatorname{Ric}(\partial_t,\partial_t)=-H'-|S|^2,\qquad |S|^2=\operatorname{tr}(S^2)\ge 0 .$$
Round expanding cusp check ($a=b=c=t$, $S=I$, $H=3$): $\operatorname{Ric}(\partial_t,\partial_t)=-0-3=-3=-3g(\partial_t,\partial_t)$. ✓ Hence with $E=\operatorname{Ric}+3g$,
$$E_{00}=-H'-|S|^2+3 .$$
Writing $B=S-I$, $b=H-3=\operatorname{tr}B$ and $|S|^2=3+2b+|B|^2$ gives
$$b'+2b+|B|^2=-E_{00},$$
which is exactly the relation used in both Step 70 §2 and Step 72 §2. Multiplying by $e^{2t}$ and integrating,
$$e^{2R}b(R)-b(0)+\int_0^R e^{2t}|B|^2\,dt=-\int_0^R e^{2t}E_{00}\,dt .$$
A reflection center gives $S(0)=0\Rightarrow B(0)=-I\Rightarrow b(0)=-3$; an exact cusp face gives $H(R)=3\Rightarrow b(R)=0$, so
$$3+\int_0^R e^{2t}|B|^2\,dt=-\int_0^R e^{2t}E_{00}\,dt,$$
and $|E_{00}|\le\delta$ forces $3\le\tfrac{\delta}{2}(e^{2R}-1)$, i.e. $R\ge\tfrac12\log(1+6/\delta)$. All of this is arithmetically correct.

The one substantive correction is the one Step 72 already made and Step 70 §7 partly retained: from the exact identity one gets
$$3-H(t)=e^{-2t}\Big(3+\int_0^t e^{2s}|B|^2\,ds\Big),$$
so $3-H(t)\ge 3e^{-2t}$ is a lower estimate only. Step 70's phrase "$3-H\sim 3e^{-2t}$" is not an asymptotic equality: the accumulated shear $\int_0^t e^{2s}|B|^2\,ds$ can dominate and can even prevent $H\to 3$. Read the identity as a one-sided weighted balance, not as a decay rate.

### (ii) A reflection half-core reaching a flat-$T^3$ Poincaré–Einstein end is excluded — two independent routes

**Global doubling argument.** A complete exact reflection-symmetric half on $[0,\infty)\times T^3$ with totally geodesic central slice, reaching an expanding end with flat $T^3$ conformal infinity, doubles across $t=0$ to a complete $\operatorname{Ric}=-3h$ manifold on $\mathbb R\times T^3$ with **two** Poincaré–Einstein ends, each with flat conformal infinity. The flat torus has $Y(T^3,[\gamma])=0$. Proposition 6.6 (Witten–Yau/Cai–Galloway, as stated in the source) applied at either end permits, for $Y\ge0$, only: (1) $Y>0$ with one end; (2) $Y=0$ with one end; or (3) the warped product $\mathbb R\times N,\ h=ds^2+e^{-2s}g_N,\ \operatorname{Ric}_{g_N}=0$. A manifold with two Poincaré–Einstein ends is none of these, so the configuration cannot exist.

The warped-product case (3) does **not** furnish a loophole. Its shape endomorphism is $S=-I$ everywhere (from $h_t=e^{-2s}g_N$, $\partial_s h_t=-2h_t$), so it has no totally geodesic slice and is not reflection-symmetric; moreover it carries only one Poincaré–Einstein end (at $s\to-\infty$) together with a collapsing cusp end (at $s\to+\infty$). It therefore fails the two hypotheses of the half-core setup (a totally geodesic slice and a flat expanding end obtained by doubling).

**Pointwise identity, cross-checked.** Step 70 §3 reaches the same conclusion locally. Using the geodesic defining function $\rho=e^{-t}$, the mean-curvature expansion in the source's own normalization, $H_\rho=3+\tfrac14 R_\gamma\rho^2+o(\rho^2)$ (their $H_r=n+\tfrac1{2(n-1)}R_\gamma r^2$ at $n=3$), gives $b=\tfrac14 R_{h_0}e^{-2t}+o(e^{-2t})$, so $e^{2t}b(t)\to\tfrac14 R_{h_0}$. The boxed identity then yields
$$\tfrac14 R_{h_0}=-3-\int_0^\infty e^{2s}|B|^2\,ds,\qquad R_{h_0}=-12-4\!\int_0^\infty e^{2s}|B|^2\,ds\le-12 .$$
(The label "$h_t=e^{-2t}\gamma_t$" in Step 70 §3 is a slip — the expanding end is $h_t\sim e^{2t}\gamma$ — but the limit $e^{2t}b\to\tfrac14 R_{h_0}$ and the conclusion are correct.) This representative-level statement is fully consistent with the global one: for the flat conformal class there is **no** representative with $R\le-12$ everywhere. Writing a representative as $e^{2\phi}\delta$ on $T^3$, the 3-dimensional conformal law gives $R=e^{-2\phi}(-4\Delta\phi-2|\nabla\phi|^2)$; at an interior maximum of $\phi$ one has $\Delta\phi\le0$ and $\nabla\phi=0$, so $R\ge0>-12$ there. Thus $R_{h_0}\le-12$ excludes the whole flat conformal class, matching the $Y=0$ exclusion from Proposition 6.6. The two arguments corroborate each other.

Consequently the flat-$T^3$ Poincaré–Einstein end is genuinely unavailable to a reflection core; any surviving nonexistence route must target a conformal infinity with $Y<0$ (aspherical circle-bundle cross-sections, per source Lemma 6.8), where Proposition 6.6 does not apply.

### (iii) A reflection-compatible five-component DeTurck/Bianchi end-data formulation

Use the Einstein–DeTurck operator $\Phi(g)=\operatorname{Ric}(g)+3g-\delta_g^{*}W$, $W=W(g,\bar g)$ the vector field built from Christoffel differences, on the diagonal $T^2$-invariant ansatz with five unknowns $(g_{tt},g_{t\theta},g_{\theta\theta},g_{xx},g_{yy})(t,\theta)$. This is the clean formulation: DeTurck removes the diffeomorphism freedom, so the five equations are a determined elliptic system with **no** separate propagated constraints (contrast the Gaussian gauge of Step 70 §3a, where $E_{00},E_{01}$ sit outside the three evolution equations and forced the over-determination noted in Step 70 §7). One caveat on the ansatz: the diagonal-in-$(x,y)$ five-component form is preserved only if the extra involutions $x\to-x$, $y\to-y$ are isometries of $\bar g$ and of the end data; otherwise the DeTurck system can generate $g_{\theta x},g_{\theta y},g_{xy},g_{tx},g_{ty}$. Impose those parities on $\bar g$ and the data.

**Parity at $t=0$.** Under $t\to-t$ the components split by their differential type: $g_{tt},g_{\theta\theta},g_{xx},g_{yy}$ are even, $g_{t\theta}$ is odd. A smooth reflection-symmetric metric therefore satisfies at $t=0$
$$\partial_t g_{tt}=\partial_t g_{\theta\theta}=\partial_t g_{xx}=\partial_t g_{yy}=0\quad(\text{even}),\qquad g_{t\theta}=0\quad(\text{odd}).$$
These five conditions (four Neumann, one Dirichlet) are exactly one per component. They automatically encode the totally geodesic condition: $t=0$ is the fixed-point set of the isometric reflection, hence totally geodesic, so $S(0)=0$ holds without imposing it separately. This removes the over-determination that appeared when Step 70 tried to add $\dot a(0)=\dot b(0)=\dot c(0)=0$ on top of Dirichlet data.

**Which central data vary.** With Neumann at $t=0$ the *values* $g_{\theta\theta}(0,\theta),g_{xx}(0,\theta),g_{yy}(0,\theta)$ are outputs, not prescribed — the induced flat-type metric on the central $T^3$ (the analogue of the Koiso/$q_N$ center) is determined by the solve. $g_{tt}(0)$ is normalizable to the reference; $g_{t\theta}(0)=0$ is fixed. Coercivity of the linearized operator (the $+3g$ term supplies a favorable zeroth-order sign on the $\operatorname{Ric}<0$ background) is what makes the Neumann problem non-degenerate.

**Data at $t=R$ and the counting tension.** Dirichlet data for all five components at $t=R$ gives a well-posed elliptic two-ended value problem: five conditions at each end, ten total for five second-order equations. But cusp-matching wants two *different* kinds of information at $t=R$: the induced cross-section metric (Dirichlet) **and** the mean curvature $H(R)=3$ / shape operator (Neumann). Prescribing both is Cauchy data for an elliptic system — over-determined and Hadamard ill-posed, the same mechanism behind the finite-$t$ Fourier blow-up correctly re-read in Step 70 §1. A well-posed elliptic solve fixes only one type at $t=R$; the Dirichlet solution then has a *determined* $S(R)$ that generically does not meet $H(R)=3$, and the residual normal defect is precisely what the weighted-shear identity of part (i) measures. This is the honest statement of why "the solver converged" in Step 72 §4 is not evidence of an Einstein neck.

**When a zero of the gauge-fixed system is Einstein on $[0,R]\times T^3$.** Applying the Bianchi operator to $\Phi(g)=0$ gives, for the DeTurck vector $V$,
$$\nabla^{*}\nabla V-\operatorname{Ric}(g)V=0 .$$
Pairing with $V$ and integrating over $[0,R]\times T^3$,
$$\int\big(|\nabla V|^2-\operatorname{Ric}(V,V)\big)=\oint_{\partial}\langle\nabla_\nu V,V\rangle .$$
On the $\operatorname{Ric}=-3g+\delta^*\xi$ solution, $-\operatorname{Ric}(V,V)=3|V|^2-(\delta^*\xi)(V,V)$; the first term has the favorable sign and the second is cubic in $V$, controlled near the reference. In the closed or complete-with-decay setting (Li–Liu §6.2: "$\tau>0$, the Bianchi one-form decays at the PE end") the edge term is absent and $V\equiv0$, so the zero is genuinely Einstein. On a manifold carrying the two faces $t=0,R$ the edge term must be handled:

- At $t=0$ the reflection parity does the work for free: $V^{t}$ is odd (so $V^{t}(0)=0$) and $V^{\theta}$ is even (so $\partial_t V^{\theta}(0)=0$), whence $\langle\nabla_\nu V,V\rangle=0$ at $t=0$. The reflection end is clean.
- At $t=R$ plain Dirichlet data on $g$ do **not** force $\xi|_{t=R}=0$, because $\xi$ is built from Christoffel differences and hence from *normal derivatives* of $g$ that Dirichlet data leave free. So a zero of the DeTurck end-data problem is **not** automatically Einstein at the finite face; one must additionally arrange $V|_{t=R}=0$ (a gauge-adapted face condition, matching $\bar g$ to first order) or ensure the $t=R$ edge term is sign-definite. This is the true content of "checking the DeTurck vector vanishes" for a finite face.

**Sign/normalization note on the linearization script.** The step71 output, computed with the $+\tfrac12\mathcal L_V$ convention, has an *indefinite* principal part (e.g. $\Phi_{tt}$ carries $+\tfrac12 p_{tt}-\tfrac12 e^{-2t}p_{\theta\theta}$; $\Phi_{\theta\theta}$ carries $-\tfrac12 e^{2t}r_{tt}+\tfrac12 r_{\theta\theta}$). That mixed signature is the wave-type structure, not the elliptic one Einstein–DeTurck must have. It signals that the DeTurck term entered with the non-cancelling sign. With $-\tfrac12\mathcal L_V$ (equivalently $V\to-V$) the gauge terms cancel the $\operatorname{Ric}$ gauge part and the symbol becomes $-\tfrac12(\xi_t^2+e^{-2t}\xi_\theta^2)\,\mathrm{Id}$, definite. The script's own comment anticipates this; the elliptic assertion of Step 70 §1 is correct in principle but the script as written does not yet display it. Separately, for the reflection formulation the reference $\bar g$ must be even in $t$; the script's $\bar g=dt^2+e^{2t}(\cdots)$ is not reflection-symmetric about $t=0$, so a symmetric interpolating reference is needed before the $t=0$ parity of $V$ can be invoked.

One more consistency point across the two Step 70 notes: the diagonal evolution equations quoted in step70\_mixed already have the elliptic structure ($\hat E_{22}=3-\ddot b-\dot b\dot H+e^{-2a}(\cdots-b'')$ gives coefficients $-1$ on $\partial_t^2 b$ and $-e^{-2a}$ on $\partial_\theta^2 b$, same sign). The "hyperbolic / $\ddot a-\alpha a''$" prose in step70\_mixed §1 misreads its own SymPy output; step70\_critical §1's elliptic conclusion is the correct one, and the elliptic-Cauchy reading of the earlier blow-up follows.

### What remains open (not settled by the above)

The exclusion in (ii) and the well-posedness structure in (iii) are structural; they do not produce an Einstein neck. The unresolved analytic content is: existence of a solution to the reflection-compatible elliptic DeTurck problem whose $t=R$ face simultaneously (a) matches the target cusp cross-section, (b) drives the measured normal defect and the weighted shear cost of part (i) to zero at the required rate $R\gtrsim\tfrac12\log(1/\delta)$, and (c) carries $V|_{t=R}=0$ so the zero is Einstein. None of these follow from the linear/elliptic set-up alone, and I have not inferred them.