# Step 56: Common observation time and terminal compactness for the restricted IL cutoff flow

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Purpose and scope

This note assembles the **common observation time theorem** and its interface
with the **terminal compactness** mechanism for the restricted four-dimensional
negative Ishida–LeBrun gap.  It takes as input:

- Per-datum smooth existence from A03 Step 56 (Theorem 4.3/5.4);
- The coupled $(\Gamma,V)$ first-exit bootstrap from A01 Step 55 §1;
- The no-$Y(0)$ curvature branch from A03 Step 58 §2–§4;
- The defect endpoint and $Q$ propagation from Steps 34–36;
- The finite current-pair induction from A01 Step 55 §2–§4;
- The fixed-background continuation bridge from A01 Step 55 §2;
- The terminal calibration and forbidden-germ mechanism from Step 45.

The Strategist's distinction governs the architecture:

1. **Smooth continuation** (per-datum) requires H^{s₀} control to prevent
   finite-time blow-up.  Its constants depend on the individual datum.
   This is needed to reach θr².

2. **Terminal compactness** (sequence-uniform) requires only bounded
   curvature and pullback noncollapse on the plateau, together with
   vanishing local defect.  This uses harmonic-coordinate elliptic
   convergence and does not require sequence-uniform derivative bounds.

These are separate mathematical problems.  Do not mix per-datum
continuation constants into the sequence-uniform compactness argument.

---

## 1. Statement

**Proposition 1.1** (Common observation time).
*Fix $n=4$, $r \in (0,1]$, and $\theta, \gamma_*, V_*$ satisfying the
coupled bootstrap conditions (Step 55, eq.\ (1.12)).  There exist
$\delta_0 = \delta_0(\gamma_*, V_*, \theta, r) > 0$ and
$\kappa_0 = \kappa_0(\gamma_*, r) > 0$ such that the following holds.*

*If $(M^4, g_0)$ is a smooth closed Riemannian manifold with a
maximal-function-selected support system satisfying*
$$
\gamma_\alpha(0) = \mathcal{S}_\alpha(0) H_{2,\alpha}(0)^{1/2} \le \gamma_*/2,
\qquad
\delta = \|E_0\|_\infty \le \delta_0,
\tag{1.1}
$$
*then the exact cutoff flow $\partial_t g = -2\chi^2(\operatorname{Ric}_g + g)$
exists smoothly on $[0, \theta r^2]$, and on this interval:*

*(i) The coupled bootstrap holds: $\Gamma(\theta r^2) \le \frac34\gamma_*$
and $V(\theta r^2) \le \frac12 V_*$.*

*(ii) The curvature endpoint: $\|a F_T(t)\|_\infty \le C\Gamma/t$ for
$t \in (0, \theta r^2]$.*

*(iii) The defect endpoint: $\|a E(t)\|_\infty \le C_E\delta(r^2/t)^{1/3}$
for $t \in (0, \theta r^2]$.*

*(iv) The global defect: $Q(\theta r^2) \le e^{C\theta} Q(0)$.*

*(v) On the terminal plateau $\{a = 1\}$ at time $T = \theta r^2$:
$|\operatorname{Rm}(T)| \le K(\gamma_*, \theta, r)$.*

**Proposition 1.2** (Terminal compactness and forbidden-germ lower bound).
*Under the same hypotheses, at time $T = \theta r^2$, for any inner center
$p \in P^{\rm in}$ and any $\rho \in (0, \min\{r/2, \rho_0(K)\}]$,
where $\rho_0(K)$ is the curvature scale, the exponential pullback ball
$(\mathcal{B}_\rho(p), \tilde g_p)$ satisfies:*

*(i) Curvature: $|\operatorname{Rm}_{\tilde g}| \le K$.*

*(ii) Noncollapse: $\operatorname{Vol}(\mathcal{B}_\rho) \ge v_0(K, \rho) > 0$.*

*(iii) Geodesic buffer: all geodesics of length $\le \rho$ from $p$
remain inside the plateau.*

*Consequently, there exists $\eta = \eta(K, \rho, v_0) > 0$ such that*
$$
\mathcal{A}_\rho \Phi(p) :=
\fint_{\mathcal{B}_\rho(p)} (\exp_p)^* \Phi\, d\mu_{\tilde g_p}
\ge \eta > 0.
\tag{1.2}
$$

*Otherwise, harmonic-coordinate strong $W^{2,q}_{\rm loc}$ convergence would
produce the forbidden calibrated Einstein germ.*

---

## 2. Per-datum smooth continuation

This section proves that no smooth solution of the cutoff flow can
terminate in finite time while the $(\Gamma, V)$ bootstrap holds.

### 2.1 Setup

Let $T_* \in (0, \theta r^2]$ be the supremum of smooth existence times
for a fixed smooth datum $g_0$.  A03 Step 56 (Theorem 4.3/5.4) gives
$T_* > 0$.  If $T_* = \theta r^2$, there is nothing to prove.

Assume for contradiction that $T_* < \theta r^2$.  By continuity, the
coupled $(\Gamma, V)$ bootstrap (Step 55 §1) holds on $[0, T_*)$ with
the strict inequalities $\Gamma(T_*^-) \le \frac34 \gamma_*$ and
$V(T_*^-) \le \frac12 V_*$.

### 2.2 Pointwise curvature from the base pair

Fix any $\tau \in (0, T_*/2)$.  On $[\tau, T_*)$:

1. **Bilipschitz equivalence** (Step 55, eq.\ (1.5)–(1.6)):
   $e^{-2V_*} g(0) \le g(t) \le e^{2V_*} g(0)$.

2. **Weighted curvature endpoint** (A03 Step 58, eq.\ (4.11)):
   $\|aF_T(t)\|_\infty \le C\Gamma/t \le C\gamma_*/\tau < \infty$.

3. **W^{1,p} → L^\infty bridge** (A03 Step 57, Prop 9.1):
   the base pair $T_0, (U_1, C_2), T_1$ gives
   $T, \nabla T \in L^\infty_t L^q_x$ for every finite $q$.
   Kato + Sobolev on the bilipschitz-equivalent $(M, g(\tau))$ gives
   $$
   \|T(t)\|_\infty \le K_\tau, \qquad t \in [\tau, T_*),
   \tag{2.1}
   $$
   where $K_\tau$ depends on $\gamma_*, V_*, \tau$, and the datum
   $(M, g(\tau))$.  In particular $|\operatorname{Rm}(t)| \le K_\tau + C_n$.

### 2.3 Finite current-pair induction

Once $\|T\|_\infty \le K_\tau$ and $\|U\|_\infty \le K_\tau$ on $[\tau, T_*)$,
the current-pair evolution equations (Step 55 §4, eqs.\ (4.1)–(4.6))
have coefficients bounded by functions of $K_\tau$ and the per-datum
cutoff data.  Each stage of the induction

$$
(U_k, C_{k+1}) \longrightarrow T_k \longrightarrow (U_{k+1}, C_{k+2})
\tag{2.2}
$$

closes by Grönwall on $[\tau, T_*)$ with per-datum finite constants.
The top cutoff term $\chi C_{k+2} * U$ is integrated once using the
$\chi$-weight; the signed-Hessian term $\chi C_2 * U_k$ uses
one integration by parts giving
$\varepsilon D_{k,p}^U + C\|C_1\|_\infty^2 \|U_k\|_p^p$
(Step 55, eq.\ (2.13b)).

After $s_0 = 7$ stages:
$$
(U_k, C_{k+1}) \in L^\infty_t L^q_x, \quad
T_k \in L^\infty_t L^q_x,
\qquad 1 \le k \le 7, \quad 0 \le k \le 6, \quad \forall q < \infty.
\tag{2.3}
$$

### 2.4 Fixed-background H^{s₀} convergence

Fix $\bar\nabla = \nabla^{g(\tau)}$ and $A(t) = \nabla^{g(t)} - \bar\nabla$.
The triangular estimate (Step 55, eq.\ (2.8)–(2.10)):
$$
{d \over dt} \|\bar\nabla^m A\|_{L^p(\bar g)}
\le C_m \bigl(\|U_{m+1}\|_{L^p(g(t))} + \text{lower}\bigr)
\tag{2.4}
$$
is integrated on $[\tau, T_*)$ using (2.3).  Induction in $m$ for
$0 \le m \le s_0 - 1 = 6$ gives
$$
\sup_{t \in [\tau, T_*)} \|\bar\nabla^m A(t)\|_{L^p(\bar g)} < \infty
\qquad \text{for every finite } p.
\tag{2.5}
$$
The metric identity $\bar\nabla^{m+1} g = (\bar\nabla^m A) * g + \text{lower}$
(Step 55, eq.\ (2.12)) then gives
$$
\sup_{t \in [\tau, T_*)} \|g(t)\|_{H^{s_0}(\bar\nabla)} < \infty.
\tag{2.6}
$$

### 2.5 Uniform H^{s₀} bounds and time-Lipschitz regularity

The H^{s₀} bound (2.6) with $s_0 = 7 > n/2 + 4 + \alpha$ for small
$\alpha > 0$ gives, by Sobolev embedding on the closed manifold
$(M, \bar g)$,
$$
\|g(t)\|_{C^{4,\alpha}(\bar g)} \le C, \qquad t \in [\tau, T_*),
\tag{2.7}
$$
for any $\alpha \in (0, 1)$.  The time derivative satisfies
$$
\|\partial_t g(t)\|_{H^{s_0-2}(\bar g)}
= \|2aE(t)\|_{H^{s_0-2}}
\le C_{s_0,\tau}(1 + \|U(t)\|_{H^{s_0-2}}),
\tag{2.7a}
$$
which is bounded by the staggered induction.  Therefore $g(t)$ is
Lipschitz in $H^{s_0 - 2}$ and bounded in $H^{s_0}$ uniformly on
$[\tau, T_*)$.

> **TTCS correction incorporated.** We do NOT claim Schauder bootstrap
> on the degenerate equation to get $C^\infty$ convergence at $T_*$.
> The coefficient $\chi^2$ vanishes on the collar, so
> $\varepsilon$-regularized Schauder constants diverge as
> $\varepsilon \to 0$.  Instead, we use smooth approximating restart
> (§2.6 below), avoiding the need for the H^{s₀} limit to be smooth.

### 2.6 Smooth-approximation restart and contradiction

Take a sequence $t_j \uparrow T_*$.  Each $g(t_j)$ is **smooth** (because
$T_*$ is the maximal smooth existence time; each $t_j < T_*$) and
satisfies the uniform bounds:
$$
\|g(t_j)\|_{H^{s_0}(\bar g)} \le R,
\qquad
\lambda g(\tau) \le g(t_j) \le \lambda^{-1} g(\tau),
\tag{2.8}
$$
where $R$ and $\lambda$ are independent of $j$.

A03 Step 56, Theorem 4.3 constructs a smooth solution starting from
each $g(t_j)$.  Its lifespan $\varepsilon_j > 0$ depends on the
$H^{s_0}$ radius, the ellipticity constant, and the fixed smooth $\chi$.
Since these inputs are uniformly bounded (2.8), there exists
$\varepsilon_0 > 0$ such that $\varepsilon_j \ge \varepsilon_0$
for all $j$.

For $j$ large enough that $T_* - t_j < \varepsilon_0$, the solution
starting from $g(t_j)$ extends past $T_*$.

**Uniqueness on the overlap.**  On $[t_j, T_*)$, both the original
and restarted solutions are smooth and solve the same fixed-cutoff
geometric equation.  The raw metric-difference estimate formerly written
here is invalid: the ungauged Ricci linearization contains second-order
diffeomorphism terms and is not a coercive tensor heat operator on
$h=g_1-g_2$.  The needed overlap statement must instead be proved in the
same transported-cutoff DeTurck variables used for existence.  Comparing
two smooth pairs $(G_i,\beta_i)$ for the coupled system gives, for
$H=G_1-G_2$ and $b=\beta_1-\beta_2$ on a per-datum smooth slab,
$$
\frac{d}{dt}\bigl(\|H\|_2^2+A\|b\|_2^2\bigr)
+c\int (\beta_1^2+\beta_2^2)|DH|^2
\le C\bigl(\|H\|_2^2+A\|b\|_2^2\bigr).
\tag{2.9}
$$
The scalar transport and the $d(\beta^2)\otimes W$ cross term are part of
this coupled estimate.  If a reverse geometric-to-pair DeTurck gauge lemma
is supplied, pair uniqueness yields branch-preserving overlap uniqueness
for the fixed-cutoff geometric flow.  Without that extra gauge lemma, one
can instead formulate the continuation argument in existence-time language:
restart from a smooth preterminal slice $g(t_j)$ and paste the newly
constructed geometric solution after $t_j$ to the old solution on
$[0,t_j]$.  Since the equation is autonomous and both one-sided time jets
are determined recursively by the same smooth spatial metric and cutoff,
the pasted branch is smooth.  This avoids using raw geometric uniqueness.
A proof-level ledger for this repair is recorded in
`workspace/notes/step57_preceptor_deTurck_uniqueness_and_scope_review.md` §2.

Thus the preterminal restart can still extend existence past $T_*$ once the
per-datum existence theorem and finite-current restart bounds are proved,
contradicting the supremum definition of $T_*$.  This proves
$T_* \ge \theta r^2$ for an extendible smooth branch.

### 2.7 Remark: per-datum vs.\ sequence-uniform

The constants in §2.3–§2.6 depend on $\tau$, $K_\tau$, the datum
$(M, g(\tau))$, and the per-datum Sobolev constant.  They are not
sequence-uniform.  This is permissible because the common observation
time $\theta r^2$ comes from the **a priori** $(\Gamma, V)$ bootstrap
(which is sequence-uniform and uses only the critical absorption
parameter $\gamma_\alpha(0)$ and the initial defect $\delta$), not
from the per-datum continuation estimates.

The per-datum H^{s₀} argument is needed only to show that no
individual smooth datum terminates before θr².  The sequence-uniform
estimates (curvature, defect, $Q$ propagation) are already available
from the first-exit bootstrap.

---

## 3. Sequence-uniform terminal estimates

These estimates hold at time $T = \theta r^2$ and are uniform across the
near-critical IL sequence.  Their proofs use only the $(\Gamma, V)$
bootstrap, not the per-datum continuation.

### 3.1 Terminal curvature on the plateau

At $T = \theta r^2$ and on the plateau $\{a = 1\}$:
$$
|\operatorname{Rm}(T)|
\le |T(T)| + |G|
\le F_T(T) + C_n
\le \frac{C\Gamma}{\theta r^2} + C_n
\le K(\gamma_*, \theta, r).
\tag{3.1}
$$

### 3.2 Terminal metric distortion

The bilipschitz constant is
$$
e^{-2V(\theta r^2)} g(0) \le g(\theta r^2) \le e^{2V(\theta r^2)} g(0),
\tag{3.2}
$$
where $V(\theta r^2) \le V_*/2$.

### 3.3 Terminal global defect

The $Q$ propagation (Step 36, §3; Step 55, §1.2) gives
$$
Q(\theta r^2) \le e^{C_H(1+r^{-2})\theta r^2 + C_V V_*} Q(0)
\le e^{C\theta} Q(0),
\tag{3.3}
$$
where the last step uses $r \le 1$.  Since $Q(0) \le \delta^2 \operatorname{Vol}(M)$
and $\operatorname{Vol}(M)/A \le C$ in the calibrated IL geography,
$$
Q(T)/A \le C\delta^2 e^{C\theta} \to 0
\tag{3.4}
$$
as $\delta \to 0$ along the near-critical sequence.

### 3.4 Terminal inner volume

The inner centers $P^{\rm in} = \bigcup_\alpha B_r(x_\alpha)$ satisfy
$P^{\rm in} \subset \{a = 1\}$ and the retained proportional-volume
estimate (Step 45, §4) gives $\operatorname{Vol}_{g(0)}(P^{\rm in}) \ge c_0 A$.
Under (3.2), $\operatorname{Vol}_{g(T)}(P^{\rm in}) \ge e^{-4V_*} c_0 A$,
which is proportional to $A$ for fixed $V_*$.

---

## 4. Terminal compactness mechanism

This section uses only the sequence-uniform terminal estimates (§3) and
standard comparison geometry.  It does not require per-datum derivative
bounds.

### 4.1 Pullback balls and Rauch comparison

For any inner center $p \in P^{\rm in}$ at time $T$, define
$$
\mathcal{B}_\rho(p) = \{v \in T_p M : |v|_{g(T)} < \rho\},
\qquad \tilde g_p = (\exp_p)^* g(T).
\tag{4.1}
$$
By (3.1), $|\operatorname{Rm}_{g(T)}| \le K$ on the plateau.
For $\rho \le \rho_0(K)$ (the curvature scale), the Jacobian of
$\exp_p$ satisfies Rauch comparison:
$$
(1 - C K \rho^2)^{n-1} \le
\frac{J(v)}{|v|^{n-1}} \le (1 + C K \rho^2)^{n-1}.
\tag{4.2}
$$
In particular, $(\mathcal{B}_\rho, \tilde g_p)$ is noncollapsed:
$$
\operatorname{Vol}_{\tilde g_p}(\mathcal{B}_\rho)
\ge (1 - C K \rho^2)^{n-1} \omega_n \rho^n
=: v_0(K, \rho) > 0.
\tag{4.3}
$$
This is a volume bound on the **pullback ball in $T_p M$**, not on
the image ball $B_{g(T)}(p, \rho) \subset M$.  Under collapse,
$\exp_p$ may fold, but the pullback ball always has Euclidean volume
up to curvature corrections.

### 4.2 Harmonic coordinates on pullback balls

On $(\mathcal{B}_\rho, \tilde g_p)$ with curvature bound $K$ and
noncollapse $v_0$, harmonic coordinates exist on
$\mathcal{B}_{\rho/2}$ with $C^{1,\alpha}$ bounds depending only on
$K$, $\rho$, $v_0$, and $n$.  The harmonic-coordinate Ricci equation
$$
g^{ab} \partial_a \partial_b g_{ij}
= -2 \operatorname{Ric}_{ij}(g) + Q_{ij}(g^{-1}, \partial g)
\tag{4.4}
$$
is a quasilinear elliptic system with bounded RHS (since $|Ric| \le K$
and $|\partial g| \le C(K, \rho, v_0)$).  Standard elliptic regularity
gives $g \in W^{2,q}_{\rm loc}(\mathcal{B}_{\rho/2})$ for every $q < \infty$.

### 4.3 Strong $W^{2,q}_{\rm loc}$ compactness

Consider a sequence of such pullback balls along the IL near-critical
family.  By the $C^{1,\alpha}$ harmonic-coordinate bounds, there is a
subsequence converging in $C^{1,\alpha'}$ (for $\alpha' < \alpha$) to a
limit metric $g_\infty$ on a limit ball.  The limit satisfies
$$
\operatorname{Ric}_{g_\infty} = -g_\infty + E_\infty,
\tag{4.5}
$$
where $E_\infty$ is the $W^{2,q}_{\rm loc}$ weak limit of $E_i$.

**The defect vanishes in the limit.**  By (3.4), $Q_i(T)/A_i \to 0$
and $\operatorname{Vol}(P^{\rm in}_i) \ge c_0 A_i$.  The unit-tangent-bundle
Liouville argument (Step 53, §7.2) gives some inner center $p_i$
with
$$
\mathcal{A}_\rho \Phi(p_i) \le C \frac{Q_i(T)}{A_i} \to 0.
\tag{4.6}
$$
Since $\Phi \ge |E|^2$, the defect vanishes:
$\|E_i\|_{L^2(\mathcal{B}_\rho)} \to 0$.  Combined with the uniform
$L^\infty$ bound $|E_i| \le C(K + 1)$ from bounded curvature,
interpolation gives $E_i \to 0$ strongly in $L^q_{\rm loc}$ for
every finite $q$.

### 4.4 Strong $W^{2,q}$ convergence and smooth limit

In harmonic coordinates, the Ricci equation (4.4) with
$g_i \to g_\infty$ in $C^{1,\alpha'}_{\rm loc}$ (from the subsequence)
and $\operatorname{Ric}_{g_i} = -g_i + E_i$ with $E_i \to 0$ in
$L^q_{\rm loc}$ gives, by interior elliptic estimates,
$$
g_i \to g_\infty \quad \text{strongly in } W^{2,q}_{\rm loc}
\tag{4.4a}
$$
for every $q < \infty$.  The limit metric satisfies
$\operatorname{Ric}_{g_\infty} = -g_\infty$ weakly.  Schauder
bootstrap on the Einstein equation in harmonic coordinates gives
$g_\infty \in C^\infty$.  The sequence convergence is
$W^{2,q}_{\rm loc}$, not $C^\infty_{\rm loc}$; the latter would
require sequence-uniform derivative bounds that are not available.
$W^{2,q}$ convergence is sufficient for the forbidden-germ
contradiction because the calibrated density $\Phi$ involves only
curvature algebraic quantities, which converge under $W^{2,q}$.

### 4.5 Forbidden-germ lower bound

On the limit ball, $g_\infty$ is a smooth Einstein germ with
$\operatorname{Ric} = -g_\infty$.  The full density is
$$
\Phi = |E|^2 + (s+4)^2 + (s + 8\sqrt{6}|W^+|)^2 + \mathcal{G}.
\tag{4.7}
$$
Under the hypothetical vanishing $\mathcal{A}_\rho \Phi \to 0$, the
limit would satisfy $s_\infty = -4$, $|W^+_\infty| = 1/(2\sqrt{6})$,
and $\mathcal{G}_\infty = 0$.  But $\mathcal{G} = 0$ forces the
calibrated Weyl spectrum
$$
\operatorname{spec}(W^+_\infty) =
\left(-\frac{1}{6}, \frac{1}{12}, \frac{1}{12}\right),
\tag{4.8}
$$
and Derdziński's proposition shows this Einstein germ is locally Kähler.
A negative Kähler–Einstein germ with $\operatorname{Ric} = -g$ has
$$
\operatorname{spec}(W^+) =
\left(\frac{1}{3}, \frac{1}{3}, -\frac{2}{3}\right),
\qquad |W^+|^2 = \frac{2}{3},
\tag{4.9}
$$
contradicting $|W^+|^2 = 1/24$.

Therefore $\mathcal{A}_\rho \Phi(p) \ge \eta > 0$ for a universal
$\eta(K, \rho, v_0)$.

---

## 5. Global contradiction for the restricted IL family

### 5.1 Upper bound on integrated $\Phi$

At terminal time $T = \theta r^2$, the monopole-calibrated terminal
bound (Step 45, §7.1) gives
$$
\int_M \Phi\, d\mu_{g(T)} \le 119\, Q(T) \le 119\, e^{C\theta} Q(0).
\tag{5.1}
$$
For $Q(0) \le \delta^2 \operatorname{Vol}(M)$ and $\operatorname{Vol}/A \le C$:
$$
\int \Phi \le C \delta^2 A.
\tag{5.2}
$$

### 5.2 Lower bound from proportional volume

The inner centers have
$\operatorname{Vol}(P^{\rm in}) \ge c_0 A$ (§3.4).
By Step 53 §7.2 (unit-tangent-bundle Liouville averaging):
$$
\int_{P^{\rm in}} \mathcal{A}_\rho \Phi(p)\, d\mu(p)
\le C \int_M \Phi\, d\mu
\le C \delta^2 A.
\tag{5.3}
$$
Therefore there exists $p \in P^{\rm in}$ with
$$
\mathcal{A}_\rho \Phi(p) \le \frac{C \delta^2 A}{\operatorname{Vol}(P^{\rm in})}
\le \frac{C \delta^2}{c_0}.
\tag{5.4}
$$

### 5.3 Contradiction

Equations (4.7)–(4.9) give $\mathcal{A}_\rho \Phi(p) \ge \eta > 0$.
Equation (5.4) gives $\mathcal{A}_\rho \Phi(p) \le C\delta^2/c_0$.
For $\delta < \sqrt{c_0 \eta/C}$, the two are incompatible.

### 5.4 Conclusion for the restricted family

Every near-negative-Einstein sequence with $\delta_i \to 0$ in the
restricted IL geography (with $q_i \ge 0$ and the full monopole sign
family) reaches the terminal contradiction for $i$ large.  In the
assembled terminal estimate,
$$
\int\Phi_i\le C\delta_i^2A_i,
\qquad
\operatorname{Vol}(P_i^{\rm in})\ge c_0A_i,
$$
so the factor $A_i$ cancels in the selected-chart average.  Consequently,
if the support, flow, chart, and terminal constants are made uniform over
the stated IL class, the resulting negative pinching gap is uniform over
that class; it should not be described as depending on the varying
characteristic numbers or as having the earlier shrinking-with-topology loss.

This remains a restricted four-dimensional negative-branch gap, not a
dimension-only Yau-26 result.

---

## 6. Separation of roles and remaining status

### 6.1 What is now established (conditional)

The following chain is logically complete only after the analytic modules
and the two Step 57 repairs below are fully proved:

$$
\text{SW/Chern–Weil calibration (§2–3 of Step 45)}
$$
$$
\downarrow
$$
$$
\text{near-critical profile } q/A \to 0,\ J/A \to 0
$$
$$
\downarrow
$$
$$
\text{proportional-volume support selection (§4 of Step 45)}
$$
$$
\downarrow
$$
$$
\text{per-datum exact flow existence (A03 Step 56)}
$$
$$
\downarrow
$$
$$
\text{coupled } (\Gamma, V) \text{ first-exit bootstrap (Step 55 §1)}
$$
$$
\downarrow
$$
$$
\text{curvature/defect Moser endpoints (A03 Step 58 + Steps 34–35)}
$$
$$
\downarrow
$$
$$
\text{per-datum continuation (this note §2)}
$$
$$
\downarrow
$$
$$
\text{common observation time } \theta r^2 \text{ (this note §2.6)}
$$
$$
\downarrow
$$
$$
\text{terminal calibration + proportional volume (§3)}
$$
$$
\downarrow
$$
$$
\text{terminal compactness + forbidden germ (§4)}
$$
$$
\downarrow
$$
$$
\text{global contradiction (§5)}
$$

### 6.2 Conditional analytic inputs

The imported modules and repairs whose full proof-level details are not
independently re-derived in this note:

**Module A: Per-datum smooth existence and overlap uniqueness.**
A03 Step 56, Theorem 4.3/5.4 constructs a smooth solution of the
transported-coefficient DeTurck system via scalar viscosity
regularization, tame high–low allocation, and transported cutoff, then
pulls back to the geometric cutoff flow.  Step 57 adds the necessary
coupled DeTurck pair uniqueness ledger for overlap pasting; raw metric
uniqueness for the ungauged equation must not be used.

**Module B: Curvature Moser iteration.**
A03 Step 58, §2–§4.  Starting from $H(0)$, proves $Y(t) \le C\Gamma H(0)/t$
and $\|aF_T(t)\|_\infty \le C\Gamma/t$ without $Y(0)$.  Uses the
shifted-curvature tensor identity from A03 Step 57 and the signed
Hessian-$a$ integration by parts from A01 Steps 34–35.  The polynomial
$p$-growth constant in the Moser iteration converges (Step 58, eq.\ (4.8)).

**Module C: Defect Moser iteration.**
Steps 34–35, adapted to the $(\Gamma, V)$ framework.  The
$E$-homogeneous sixth-power energy $J_6$ satisfies
$J_6' + cX_6 \le C(1+r^{-2})J_6$ under small $\gamma$.  The defect
endpoint $\|aE(t)\|_\infty \le C_E\delta(r^2/t)^{1/3}$ uses the
same positive-time Moser mechanism.  This module imports the tensor
calculations from Steps 34–35 and uses small-$\gamma$ absorption.

**Module D: Finite current-pair expansion.**
Step 55 proves the first nontrivial $(U_2,C_3)$ exchange and A03 Step 59
states the general staggered pattern through $(U_7,C_8)$ and
$T_0,\ldots,T_6$.  A full commutator expansion must still show that no
undisplayed current-order term requires unavailable bounds; scripts check
order arithmetic but not the tensor identities.

### 6.3 What is NOT used from these modules

- No sequence-uniform Sobolev constant at positive time
- No sequence-uniform higher derivative bound
- No noncollapse assumption on the base manifold
- No curvature-to-volume budget outside the specific IL geography
- No global compactness theorem for the manifold sequence

### 6.4 Remaining open fronts

Even if all three modules are completed:

- **Positive branch:** uncovered.  Myers gives diameter control but no
  dimension-only volume lower bound.  Positive Einstein collapse is
  possible (lens spaces).  No obstruction mechanism analogous to the
  negative IL route is known.

- **Arbitrary four-manifold topology:** the IL geography is a specific
  connected-sum family.  Other strict-Hitchin–Thorpe manifolds (graph
  manifolds, Farrell–Jones exotics, mixed fillings) are not covered.

- **Dimensions $n \ge 5$:** no SW/Weyl calibration, no forbidden local
  profile, no dimension-only obstruction mechanism.

- **Lean formalization:** not started.

- **Dimension-only constants:** the gap depends on the geography
  parameters, not only on $n = 4$.

---

## 7. Verification

A structural verification script checks the following:

1. Sobolev embedding: $H^7(M^4) \hookrightarrow C^{4,\alpha}$ for $\alpha < 1$
2. Smooth-approximation restart uses $H^7$ preterminal bounds; no Schauder bootstrap across the degenerate interface is used
3. Bootstrap self-improvement: if $\gamma(0) \le \gamma_*/2$ and
   $\delta$ satisfies (1.17), then $\Gamma(T) \le (3/4)\gamma_*$,
   $V(T) \le V_*/2$
4. $A$-cancellation: $Q/A \to 0$ and $\operatorname{Vol}(P^{\rm in}) \ge c_0 A$
   give $\mathcal{A}_\rho \Phi \le C\delta^2/c_0$
5. Continuation hierarchy levels: $s_0 = 7$ suffices for $n = 4$
6. Separation check: per-datum constants appear only in §2; §3–§5 are
   sequence-uniform
