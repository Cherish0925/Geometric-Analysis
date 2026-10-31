# Step 11: CZ Hessian spike, the keystone correction, and Proposition A

Session S0910A02, Agent2/Constructor, Execute.

## 1. Main result: pointwise C⁰-Ricci ε-regularity is FALSE

### Statement refuted

**CT_{C⁰} (false):** There exist ε, C, δ₀ > 0 such that any closed Riemannian
4-manifold (M⁴, g) with
$$
\|\operatorname{Ric}_g - g\|_{L^\infty, \mathrm{op}} \le \delta_0
\qquad\text{and}\qquad
\int_{B_r(p)} |\operatorname{Rm}|^2 \le \varepsilon
$$
satisfies $\sup_{B_{r/2}(p)} |\operatorname{Rm}| \le C r^{-2}$.

### Counterexample

**Manifold:** $M = S^2(1) \times S^2(1)$ (closed, Einstein, $\operatorname{Ric} = g$).

**Metric family:** Fix $\rho > 0$ small. Set
$$
g_j = dx^2 + dy^2 + e^{2(F_1 + u_j)} d\theta^2 + e^{2(F_2 - u_j)} d\varphi^2,
$$
where $F_1 = \log\sin x$, $F_2 = \log\sin y$ (so $u_j \equiv 0$ recovers the round
product metric), and
$$
u_j(X,Y) = a_j \cdot \chi(r/\rho) \cdot w_j(X,Y),
\qquad
w_j = X Y \cdot \bigl(-\tfrac12\bigr) \log(X^2 + Y^2 + \sigma_j^2),
$$
with $X = x - \pi/2$, $Y = y - \pi/2$, $r = \sqrt{X^2+Y^2}$,
$a_j = \Lambda_j^{-2/3}$, $\sigma_j = e^{-\Lambda_j}$, $\Lambda_j \to \infty$.

### Mechanism: opposite-warping Hessian cancellation

In the orthonormal frame $\{e_x, e_y, e_\theta = e^{-(F_1+u)}d_\theta,
e_\varphi = e^{-(F_2-u)}d_\varphi\}$:

**(i) Base Ricci block.** The Hessian of $u$ cancels exactly:
$$
\operatorname{Hess}(F_1 + u) + \operatorname{Hess}(F_2 - u) = \operatorname{Hess}(F_1) + \operatorname{Hess}(F_2).
$$
Therefore the base block of $\operatorname{Ric} - g$ depends on $u$ only through
$\nabla u$ (and $|\nabla u|^2$, $\nabla u \cdot \nabla F_i$), but contains
**no second derivatives of $u$**.

**(ii) Fiber Ricci blocks.** $E_{\theta\theta}$ and $E_{\varphi\varphi}$ depend on
second derivatives of $u$ only through $\Delta u$, because $\Delta(F_1+u) + \Delta(F_2-u)
= \Delta F_1 + \Delta F_2$ and the quadratic gradient terms see $\nabla u$ only.

**(iii) Mixed Riemann.** The full Hessian of $u$ survives:
$$
R(e_a, e_\theta, e_b, e_\theta) = -\partial_a\partial_b(F_1 + u) - \partial_a(F_1+u)\partial_b(F_1+u),
$$
$$
R(e_a, e_\varphi, e_b, e_\varphi) = -\partial_a\partial_b(F_2 - u) - \partial_a(F_2-u)\partial_b(F_2-u).
$$
The trace-free Hessian of $u$ contributes to Weyl curvature but not to Ricci.

**Verified symbolically** in `workspace/scripts/step11_cz_spike_analytical.py`.

### Spike function identities

1. $|{\Delta w_j}| \le 9/4$ **uniformly in $\sigma_j$.**
   Proof: $\Delta(XY L_\sigma) = -2XY(2X^2+2Y^2+3\sigma^2)/(X^2+Y^2+\sigma^2)^2$.
   With $R = X^2+Y^2$, $S = R+\sigma^2$: $|\Delta w| \le R(4/S + 2\sigma^2/S^2)/2 \le 2 + 1/4$.

2. $(w_j)_{XY}(0,0) = -\log\sigma_j = \Lambda_j \to \infty.$

3. $\sup_{B_\rho} |\nabla w_j| \le C(\rho)$ **independent of $\sigma_j$.**
   Numerical verification: $\sup|\nabla w| \le 0.362$ for all $\Lambda \in \{1, 10, 100, 1000\}$.
   Analytical explanation: $|\nabla w| = |(Y(L + XL_X), X(L + YL_Y))|$. Since $|X|,|Y| \le \rho$
   and $\sup_{\varepsilon\ge0} \varepsilon|\log(\varepsilon^2 + \sigma^2)| \le C$ (the function
   $t|\log t|$ is bounded on $[0,\rho^2]$), the supremum converges as $\sigma \to 0$.

### Key estimates

With $a_j = \Lambda_j^{-2/3}$:

| Quantity | Bound | Rate |
|----------|-------|------|
| $\|\nabla u_j\|_\infty$ | $C(\rho) \cdot a_j$ | $\to 0$ |
| $\|\Delta u_j\|_\infty$ | $\tfrac94 a_j + O(a_j)$ | $\to 0$ |
| $\|\operatorname{Ric}_{g_j} - g\|_{\mathrm{op}}$ | $C(\rho)(a_j + a_j^2)$ | $\to 0$ |
| $\|u_{j,XY}(0)\|$ | $a_j \Lambda_j = \Lambda_j^{1/3}$ | $\to \infty$ |
| $|\operatorname{Rm}_{g_j}|(p)$ | $\ge c\Lambda_j^{1/3} - C$ | $\to \infty$ |
| $\|\nabla^2 u_j\|_{L^2(B_\rho)}$ | $C(\rho) a_j$ (by CZ $L^2$) | $\to 0$ |
| $\int_{B_\rho} |\operatorname{Rm}|^2$ | $\to 0$ | (from $L^2$ of Hessian) |

**Numerical verification** (rho = 0.30):

| Λ | a | δ_op | |Rm|(center) | ρ²|Rm| | sup|∇u| | L²|Hess u|² |
|---|---|------|-------------|---------|---------|-------------|
| 10 | 0.2154 | 0.437 | 8.09 | 0.73 | 0.072 | 0.902 |
| 50 | 0.0737 | 0.150 | 12.42 | 1.12 | 0.025 | 0.105 |
| 100 | 0.0464 | 0.094 | 15.13 | 1.36 | 0.016 | 0.042 |
| 500 | 0.0159 | 0.032 | 24.45 | 2.20 | 0.005 | 0.005 |

### Scope

This refutes CT_{C⁰}, **not**:
- Cheeger–Tian (hypothesis is exactly Einstein: $\operatorname{Ric} = \lambda g$)
- Harmonic-radius lower bounds from bounded Ricci (Cheeger–Naber, Naber–Zhang)
- $L^p$ or BMO curvature control (CZ gives $\|\nabla^2 u\|_{L^p} \le C_p\|\Delta u\|_{L^p} \to 0$)
- Li smoothing (bounded curvature for smoothed metric where $L^2$ energy doesn't concentrate)
- Yau Problem 26 itself ($S^2 \times S^2$ is Einstein)

---

## 2. Consequence: the regularity keystone must be L^p / BMO, not L^∞

The failure is **exactly the Calderón–Zygmund endpoint**: $\Delta u \in L^\infty$ does not
imply $\nabla^2 u \in L^\infty$; but $\|\nabla^2 u\|_{L^p} \le C_p\|\Delta u\|_{L^p}$
for all $p < \infty$, and $\|\nabla^2 u\|_{\mathrm{BMO}} \le C\|\Delta u\|_{L^\infty}$.

**The surviving regularity for C⁰-pinched metrics:**

In harmonic coordinates (where Naber–Zhang gives $r_h \ge h_0 > 0$ on covers):
$$
g^{ab}\partial_a\partial_b g_{ij} = -2\operatorname{Ric}_{ij} + Q_{ij}(g^{-1}, \partial g).
$$
With $\operatorname{Ric} = g + E$, $\|E\|_\infty \le \delta$:
- $g \in W^{2,p}_{\mathrm{loc}}$ for all $p < \infty$ (elliptic regularity with $L^\infty$ RHS)
- $g \in C^{1,\alpha}_{\mathrm{loc}}$ for all $\alpha < 1$
- $\nabla^2 g \in \mathrm{BMO}_{\mathrm{loc}}$
- But NOT $g \in W^{2,\infty}$, so NOT $|\operatorname{Rm}| \le C$ pointwise.

**For the Yau-26 program this means:**
Any argument requiring a pointwise curvature bound must get it from
Li smoothing (which changes the metric), Cheeger–Tian (which needs Einstein),
or a distributional/test-field formulation (which avoids differentiating $E$).
The CGB integrand is quadratic in curvature, so $L^p$ estimates for $p > 2$ are
sufficient for localization, and this should be the new keystone target.

---

## 3. Proposition A: Conditional finite-cover amplifier (dimension 4)

**Proposition A.** Fix $0 < \delta_0 < 1/2$. Suppose there exists $v_0 > 0$ such
that every closed simply connected smooth four-manifold $(X^4, g)$ with
$$
\|\operatorname{Ric}_g - g\|_{\mathrm{op}} \le \delta_0
$$
satisfies $\operatorname{Vol}(X, g) \ge v_0$. Then there exists
$v_1 = v_1(\delta_0, v_0) > 0$ such that every closed connected smooth four-manifold
$(M^4, g)$ (orientable or not) with the same pinching has
$$
\operatorname{Vol}(M, g) \ge v_1.
$$
Consequently the class of all such $M$ realizes only finitely many diffeomorphism types.

**Proof.**

Step 1. Positive Ricci gives $\operatorname{Ric}_g \ge (1-\delta_0)g > 0$. Myers'
theorem makes $\pi_1(M)$ finite. Let $\pi: (\widetilde{M}, \widetilde{g}) \to (M, g)$
be the universal cover, $d = |\pi_1(M)|$. Then $\widetilde{M}$ is closed, simply
connected, and $\|\operatorname{Ric}_{\widetilde{g}} - \widetilde{g}\|_{\mathrm{op}} \le
\delta_0$ (pulled-back pinching).

Step 2. By the assumed simply connected gap: $\operatorname{Vol}(\widetilde{M}) \ge v_0$.

Step 3. Apply the Step 9 noncollapsed finiteness theorem to the universal covers.
Myers gives $\operatorname{diam}(\widetilde{M}) \le D(\delta_0)$. Bishop–Gromov with
$B_D(p) = \widetilde{M}$ gives $\operatorname{Vol}(B_1(p)) \ge v'(\delta_0, v_0) > 0$
for every $p$. Then Cheeger–Naber Theorem 1.12 (requiring $|\operatorname{Ric}| \le 3$
and unit-ball noncollapse) gives at most $N(\delta_0, v_0)$ diffeomorphism types of
$\widetilde{M}$. Hence $\chi(\widetilde{M}) \le X(\delta_0, v_0) < \infty$.

Step 4. Since $\widetilde{M}$ is simply connected (hence orientable and $b_1 = 0$):
$\chi(\widetilde{M}) = 2 + b_2(\widetilde{M}) \ge 2$.

Step 5. Euler characteristic multiplicativity: $\chi(\widetilde{M}) = d \cdot \chi(M)$.
Since $\chi(M) \ge 1$ (it is a positive integer—the quotient of $\chi(\widetilde{M}) \ge 2$
by $d$), we get $d \le \chi(\widetilde{M}) \le X(\delta_0, v_0)$.

Step 6. $\operatorname{Vol}(M) = \operatorname{Vol}(\widetilde{M})/d \ge v_0/X(\delta_0,v_0)
=: v_1 > 0$.

Step 7. With $\operatorname{Vol}(M) \ge v_1$ and $\operatorname{diam}(M) \le D(\delta_0)$
(Myers again), Cheeger–Naber Theorem 1.12 applies directly to $M$, giving finitely many
diffeomorphism types. $\square$

**Remark.** This does not produce Einstein metrics. Even if every simply connected
manifold in the class carries an Einstein metric, one still needs an invariant metric
or a separate argument on quotients.

---

## 4. Restatement of the volume-gap target

The correct target is now:

> **Volume-gap conjecture (4D positive).** There exists $\delta_0 \in (0, 1/2)$ and
> $v_0 > 0$ such that every closed simply connected four-manifold with
> $\|\operatorname{Ric}_g - g\|_{\mathrm{op}} \le \delta_0$ has
> $\operatorname{Vol}(M, g) \ge v_0$.

A proof would combine with Proposition A to give unconditional noncollapse and
finite diffeomorphism types for arbitrary topology. For a simply connected sequence
with $\delta_j \to 0$ and $\operatorname{Vol} \to 0$:

- CGB: $\int|W|^2 + \beta(\delta)\operatorname{Vol} \le 8\pi^2\chi$ with
  $\beta(\delta) > 0$ for $\delta < 1/2$.
- Bishop: $\operatorname{Vol} \le 24\pi^2/(1-\delta)^2$.
- So $\int|W|^2 \to 8\pi^2\chi$ and all Euler mass concentrates as Weyl energy.
- The CGB density $|W|^2 + s^2/24 - |E|^2/2 \ge |W|^2 + \beta(\delta)$ is **pointwise
  positive**, so there is nothing to cancel.

The obstacle is localizing the contradiction: $\chi$ can be large and support
many concentration regions, so a counting argument alone is insufficient.
The new regularity insight (L^p/BMO instead of pointwise) suggests:

- **Li smoothing** to pass to bounded curvature on the complement of concentration balls
- **CFG F-structure** on the smoothed collapsed complement (topological statement: $\chi = 0$)
- Energy quantization on concentration balls (need ALF/ALG table, not just ALE)

---

## 5. Files and evidence

| File | Content |
|------|---------|
| `scripts/step11_cz_spike_analytical.py` | Construction and numerical verification |
| `data/step11_cz_hessian_spike.json` | Full numerical results |
| This note | Mathematical proof and program consequence |

**Source dependencies:** doubly-warped curvature formulas (standard Riemannian geometry);
Calderón–Zygmund $L^p$ and BMO estimates; Cheeger–Naber Theorem 1.12 [1406.6534];
Myers, Bishop–Gromov, Bochner (standard); Li [0911.3104].

---

## 6. Symbol lemma: why the mechanism must be nonlinear/CZ

**Lemma (linear symbol).** On an Einstein background $(M^n, g_0)$ with
$\operatorname{Ric}_{g_0} = g_0$, consider a linearized perturbation
$h = a \cdot e^{ik\langle\xi,\cdot\rangle} q$ with $q$ transverse-traceless and
$q \perp \xi \odot T_pM$. Then the principal symbols satisfy
$D\operatorname{Ric}(h) \sim ak^2 q$ and $D\operatorname{Rm}(h) \sim ak^2 q$ with
the same scaling. Directions in $\ker \sigma_\xi(\operatorname{Ric})$ are pure gauge
($\xi \odot v$), and $\sigma_\xi(\operatorname{Rm})$ also vanishes on those.
Therefore no single-frequency linear perturbation can make $|W|$ large while keeping
$|\operatorname{Ric} - g_0|$ small: **the Ricci and Weyl principal symbols have the same
scaling on physical modes.** This confirms that the CZ/Hessian-spike mechanism is
genuinely nonlinear (it uses the cancellation between two finite warpings, not
high-frequency oscillation) and cannot be captured at the WKB level.

---

## 7. L^p ε-regularity: the surviving conjecture

**Conjecture (L^p ε-regularity under C⁰ Ricci pinching).**
For every $n \ge 4$ and $p > n/2$ there exist $\varepsilon(n,p), \delta_0(n,p) > 0$
such that if $(M^n, g)$ satisfies
$$
\|\operatorname{Ric}_g - g\|_{L^\infty, \mathrm{op}} \le \delta_0,
\qquad
r^{4-n}\int_{B_r(p)} |\operatorname{Rm}|^2 \le \varepsilon,
$$
then
$$
r^2 \|\operatorname{Rm}\|_{L^p(B_{r/2}(p))} \le C(n,p).
$$

This is strictly weaker than $CT_{C^0}$ (which asks for $L^\infty$) but is:
- **consistent with the CZ spike** (the family has $\|\operatorname{Rm}\|_{L^p} \to 0$ for all $p < \infty$);
- **sufficient for CGB localization** (the integrand is quadratic, so $L^p$ with $p > 2$ controls the Euler density);
- **provable in harmonic coordinates** from CZ theory, if harmonic radius is controlled.

The main gap between this conjecture and a proof is the harmonic-radius input:
Naber–Zhang Proposition 6.4 gives harmonic radius on covers under additional
hypotheses (maximal fibered nilpotency rank, fixed-scale GH model). The conjecture
would close automatically if the Naber–Zhang hypotheses were shown to hold at positive
volume fraction under tight pinching, which is exactly the accessible-cover question
that A01 and A03 are pursuing.

---

## 8. Connection to peer session work

- **A03 (msg #248):** Taub-NUT-AdS shows maximal rank is an independent geometric
  hypothesis, not derivable from curvature bounds alone. This is complementary to
  our CZ spike: pointwise regularity fails even when maximal rank holds.
  Together: the next route cannot assume either pointwise curvature or automatic
  maximal rank; it must use global closed-manifold topology.

- **A01 (msg #246–247):** The accessible-cover theorem uses normal-cover mean transport
  and Naber–Zhang harmonic-radius to exclude positive-volume sets of well-modeled
  collapse. The energy-cost theorem for the remaining bad volume is the shared
  infrastructure target.

- **Shared consequence:** The CZ spike makes the projection/test-field bridge
  (Step 8 target) even more important: pairing $\operatorname{Ric} - g$ against
  smooth test tensors is the ONLY derivative-free mechanism compatible with the
  available regularity. It works because derivatives fall on the test data, not on
  the Ricci defect.
