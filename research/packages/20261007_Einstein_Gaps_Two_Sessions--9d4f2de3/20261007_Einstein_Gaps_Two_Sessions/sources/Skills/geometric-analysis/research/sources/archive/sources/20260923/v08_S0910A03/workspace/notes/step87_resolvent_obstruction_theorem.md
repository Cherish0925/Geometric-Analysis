# Step 87: Massive-resolvent forced connector obstruction

Session `S0910A03`, Agent2 / Execute.

> **Corrects** Step 86 §5–§8 and replaces the proposed local-Moser/superlevel program
> with a global resolvent comparison. The Fisher information bound is corrected per TTCS.
> Supersedes `step85_route_map.md` and `step86_route_map.md` for the forced case.
>
> **Step 88 strengthening.** Reflection is not needed. On a two-ended cylindrical
> weighted base with two exact *outward-expanding* cusp ends, a primitive
> \(e^{2\sigma}\gamma_B\)-length-minimizing essential loop lifts to an invariant
> minimal \(T^3\). Its Gauss identity gives the same floor \(12-8\delta\), with
> additional nonnegative second-fundamental-form terms. See
> `workspace/notes/step88_reflection_free_minimal_separator.md`. The theorem below
> is therefore superseded in scope by the reflection-free theorem there.

## 1. Setup and prior results

On a free orthogonally transitive $T^2$-region, write
\[
g = \gamma_B + G_{ab}d\xi^a d\xi^b,
\qquad G = e^\sigma M,\qquad \det M = 1,
\]
and let $U: B \to \mathbb H^2 = SL(2)/SO(2)$ represent $M$. Put
\[
e = |dU|^2_{\mathbb H^2},
\qquad F = \tau_\sigma(U) \text{ (weighted tension)},
\qquad V(X) = \langle dU(X), F\rangle.
\]
Under $\|E\|_{\mathrm{op}} = \|\operatorname{Ric}+3g\|_{\mathrm{op}} \le \delta$,
the orbit defect gives $|F| \le 2\delta$ and $|V| \le 2\delta\sqrt{e}$ (Step 86 §1).

The forced Bochner inequality (Step 85, verified Step 86) is:
\[
\frac12 Le \ge |DdU|^2 + \operatorname{div}_\sigma V - 4\delta^2
+ \frac12 e^2 - (3+\delta)e.
\tag{1.1}
\]

The reflected center identity (Step 85 §5, TTCS-corrected):
\[
\langle e(0,\cdot)\rangle_\mu = 12 - 2\langle D\rangle_\mu + \langle h^2\rangle_\mu
\ge 12 - 8\delta,
\tag{1.2}
\]
where $D = \mathrm{tr}\,E - 2E(\nu,\nu)$, $|D| \le 4\delta$,
and $h = \sigma_s = (\log\rho)_s$ is the tangential orbit-area derivative.

## 2. Complete extension hypothesis

We consider reflected connectors whose exit data match an exact expanding cusp,
so that gluing exact cusp ends produces a complete, smooth, weighted base
$(B^2, \gamma_B, d\mu = e^\sigma dA)$ with:
- $e \to 0$ at all cusp ends (orbit map constant on exact cusps);
- the finite-dimensional curvature bound holds globally:
\[
\operatorname{Ric}^4_f
:= \operatorname{Ric}_B - \operatorname{Hess}\sigma - \tfrac12 d\sigma \otimes d\sigma
= -3\gamma_B + \tfrac12 U^*h_{\mathbb H^2} + E_B
\ge -(3+\delta)\gamma_B.
\tag{2.1}
\]

**Cusp benchmark correction** (from TTCS): on the round cusp
$\gamma_B = dr^2 + e^{2r}dz^2$, $\sigma = 2r$,
\[
\operatorname{Ric}^4_f = -3\gamma_B
\quad(\text{not } \operatorname{diag}(-1,-3)),
\]
because $\frac12 d\sigma^2 = 2dr^2$ exactly cancels the $-1$ vs $-3$ asymmetry
in $\operatorname{Ric}_B - \operatorname{Hess}\sigma$.

## 3. Massive comparison inequality

Drop $|DdU|^2 \ge 0$ in (1.1) and multiply by 2:
\[
Le \ge e^2 - 2(3+\delta)e - 8\delta^2 + 2\operatorname{div}_\sigma V.
\]
Set $\kappa = 2(3+\delta) = 6 + 2\delta$. Adding $\kappa e$ to both sides:
\[
(-L+\kappa)e \le \kappa e - e^2 + 2(3+\delta)e + 8\delta^2 - 2\operatorname{div}_\sigma V.
\]
Since $\kappa = 2(3+\delta)$, the first three terms give $2\kappa e - e^2 = \kappa^2 - (e-\kappa)^2 \le \kappa^2$. Thus:
\[
\boxed{
(-L+\kappa)e \le \kappa^2 + 8\delta^2 - 2\operatorname{div}_\sigma V.}
\tag{3.1}
\]

## 4. Li–Yau Fisher information (CORRECTED)

On a complete smooth weighted manifold satisfying $CD(-K,N)$ (i.e., $\operatorname{Ric}^N_f \ge -Kg$),
the weighted heat kernel $p_t$ of $L$ satisfies the **Riccati** Fisher information bound:
\[
\boxed{
I(t) := \int p_t(x,y) |\nabla_y \log p_t(x,y)|^2\,d\mu(y)
\le \frac{NK}{1 - e^{-2Kt}}.}
\tag{4.1}
\]

**Proof.** The de Bruijn–$\Gamma_2$ identity gives
$I'(t) = -2\int p_t \Gamma_2(\log p_t)\,d\mu$.
The $CD(-K,N)$ condition $\Gamma_2(\phi) \ge -K\Gamma(\phi) + (L\phi)^2/N$
combined with $\int p_t L(\log p_t)\,d\mu = -I(t)$ and Jensen gives
\[
I'(t) \le 2KI(t) - \frac{2}{N}I(t)^2.
\]
Comparing with the Riccati solution (initial data $I(0^+) = +\infty$) yields (4.1). $\square$

**Correction.** The naive bound $I(t) \le N/(2t) + NK/2$ is only the small-$t$
expansion of (4.1) and fails for large $t$. On the round cusp ($N=4$, $K=3$),
the radial Fisher information is $9 + 1/(2t)$, which exceeds $2/t + 6$
for $t > 1/2$. The Riccati bound $12/(1-e^{-6t}) \to 12$ correctly
dominates the radial lower bound for all $t$.

## 5. Resolvent gradient estimate

By Cauchy–Schwarz and heat conservation ($\int p_t\,d\mu = 1$, guaranteed by
$CD(-K,N)$ stochastic completeness with finite $N$):
\[
\int |\nabla_y p_t(x,y)|\,d\mu(y) \le \sqrt{I(t)}.
\]

The massive resolvent $G_\kappa(x,y) = \int_0^\infty e^{-\kappa t} p_t(x,y)\,dt$ therefore satisfies:
\[
C_\kappa := \sup_x \int |\nabla_y G_\kappa(x,y)|\,d\mu(y)
\le \int_0^\infty e^{-\kappa t} \sqrt{\frac{NK}{1-e^{-2Kt}}}\,dt.
\]

Substituting $u = 1 - e^{-2Kt}$, $du = 2K e^{-2Kt}\,dt = 2K(1-u)\,dt$:
\[
= \frac{\sqrt{NK}}{2K} \int_0^1 (1-u)^{\kappa/(2K)-1} u^{-1/2}\,du
= \frac{\sqrt{NK}}{2K} B\!\left(\frac{\kappa}{2K}, \frac12\right).
\]

With $\kappa = 2K$: $B(1, \frac12) = \Gamma(1)\Gamma(\frac12)/\Gamma(\frac32) = 2$, giving the upper estimate
\[
\boxed{
C_\kappa \le \frac{\sqrt{NK}}{2K} \cdot 2 = \sqrt{\frac{N}{K}} = \frac{2}{\sqrt{3+\delta}}.}
\tag{5.1}
\]
Equality in the intervening heat-kernel inequalities is not asserted; only this
upper estimate is used below.

**Numerically verified**: at $\delta=0$, $C_6 = 2/\sqrt{3} \approx 1.15470$.
Direct numerical integration of the Riccati integrand agrees to 10 digits.

## 6. Duhamel comparison principle

For bounded $e$ on a complete manifold with $\kappa > 0$ and $(-L+\kappa)e \le S$,
the Duhamel formula gives:
\[
e = e^{-\kappa T} P_T e + \int_0^T e^{-\kappa t} P_t[(-L+\kappa)e]\,dt
\le e^{-\kappa T} P_T e + \int_0^T e^{-\kappa t} P_t S\,dt.
\]
As $T \to \infty$: $e^{-\kappa T} P_T e \le e^{-\kappa T} \|e\|_\infty \to 0$. Hence:
\[
\boxed{e \le R_\kappa S = R_\kappa[\kappa^2 + 8\delta^2 - 2\operatorname{div}_\sigma V].}
\tag{6.1}
\]

**Resolvent of the constant part:** $(-L+\kappa)(c/\kappa) = c$ since $L(1) = 0$, so
$R_\kappa[\kappa^2 + 8\delta^2] = \kappa + 8\delta^2/\kappa$.

**Resolvent of the divergence part:** by integration by parts
(justified since $V \to 0$ on cusp ends and $|\nabla_y G_\kappa|$ is $L^1$-integrable):
\[
|R_\kappa[\operatorname{div}_\sigma V](x)|
= \left|\int \langle \nabla_y G_\kappa(x,y), V(y)\rangle\,d\mu(y)\right|
\le C_\kappa \|V\|_\infty.
\]

## 7. Self-consistent ceiling bound

Let $B = \sup e$ (finite by boundedness). Then $\|V\|_\infty \le 2\delta\sqrt{B}$, and (6.1) gives:
\[
\boxed{
B \le \kappa + \frac{8\delta^2}{\kappa} + \frac{4\delta}{\sqrt{3+\delta}} \cdot 2\sqrt{B}
= \alpha + \beta\sqrt{B},}
\tag{7.1}
\]
where
\[
\alpha = 2(3+\delta) + \frac{4\delta^2}{3+\delta},
\qquad
\beta = \frac{8\delta}{\sqrt{3+\delta}}.
\]

Solving the quadratic $\sqrt{B} \le \beta/2 + \sqrt{\beta^2/4 + \alpha}$:
\[
\boxed{
B \le \mathcal B(\delta) :=
\left[\frac{4\delta}{\sqrt{3+\delta}}
+ \sqrt{2(3+\delta) + \frac{20\delta^2}{3+\delta}}\right]^2.}
\tag{7.2}
\]

At $\delta = 0$: $\mathcal B(0) = (\sqrt{6})^2 = 6$.

## 8. The obstruction theorem

**Theorem.** *For $\delta < \delta_*$, no reflected free-OT approximate Einstein
connector with complete cusp-type extensions exists.*

**Proof.** The center floor (1.2) gives $\sup e \ge \langle e(0,\cdot)\rangle_\mu \ge 12 - 8\delta$.
The resolvent ceiling (7.2) gives $\sup e \le \mathcal B(\delta)$. Therefore:
\[
12 - 8\delta \le \mathcal B(\delta).
\]
At $\delta = 0$: $12 > 6$, contradiction. By continuity, the obstruction persists for all
$\delta < \delta_*$ where $\mathcal B(\delta_*) = 12 - 8\delta_*$. Numerically:
\[
\boxed{\delta_* \approx 0.24625.}
\]

The leading-order expansion gives:
\[
\mathcal B(\delta) \approx 6 + (2 + 8\sqrt{2})\delta, \qquad 12 - 8\delta,
\]
hence the leading threshold is $6/(10 + 8\sqrt{2}) \approx 0.282$, corrected downward
by quadratic terms.

## 9. Combined negative-branch landscape

| Class | Obstruction | Threshold |
|-------|-------------|-----------|
| Exact reflected OT | Step 85 Bochner comparison | $\sup e \ge 12$ at center vs $\le 6$ ceiling |
| Warped product $k \ge 0$ | A02 waist barrier (#614) | $\delta \ge 3/2$ |
| Forced reflected OT (this Step) | Resolvent comparison | $\delta \ge \delta_* \approx 0.246$ |
| Volume-convergent orbifold + ALE route | A02 Chern–Weil neutrality/BCG (#625, scope corrected #633) | Sambusetti route inaccessible in that construction class |

**Remaining mechanisms for negative-branch refutation after Step 88:**
1. Free-$T^2$ metrics with connection twist (failure of OT), or fully non-$T^2$ graph metrics
2. $N\#N$ $S^3$ necks with nonlocal, non-warped deformation (different topology, no free $T^2$ action)
3. New no-Einstein mechanisms not tied to the present graph/orbifold construction classes

Nonreflection alone is no longer an escape for complete OT cylinders with two
outward-expanding exact ends; Step 88 supplies a minimal separator.

## 10. Scope and non-extensions

This theorem concerns reflected, free-$T^2$, orthogonally transitive connectors
with complete cusp-type extensions. It does NOT address:
- Approximate twist ($c_X, c_Y \ne 0$): twist vanishing was proved only for
  exact reflected Einstein, not approximate
- Singular $T^2$ orbits: the free-action hypothesis is used throughout
- Non-OT graph metrics: general graph manifolds need not have this symmetry
- $N\#N$ connected sums: the interface is $S^3$, not $T^3$; there is no free $T^2$ action
- The positive normalized branch: independent and unresolved
- Higher dimensions: four-dimensional Chern–Weil/Seiberg–Witten tools do not transfer

## 11. Reproducible evidence

- `workspace/scripts/step87_resolvent_corrected.py` — main computation
- `workspace/data/step87_resolvent_corrected.json` — all numerical results
- `workspace/scripts/step87_resolvent_comparison.py` — initial (uncorrected) computation
- `workspace/data/step87_resolvent_comparison.json` — initial results (Fisher bound wrong)
- `trace/ttcs/results/step87_ttcs01_verifier1_integration.md` — independent TTCS verification
- Step 85 files: exact Bochner comparison
- Step 86 files: forced Caccioppoli, combined W energy, cusp spectral benchmark
