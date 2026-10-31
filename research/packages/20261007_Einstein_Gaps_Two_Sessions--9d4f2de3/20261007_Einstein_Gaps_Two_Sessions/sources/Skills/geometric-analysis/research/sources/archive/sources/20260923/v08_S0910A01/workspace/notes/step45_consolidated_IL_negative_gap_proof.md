# Consolidated proof: family-uniform negative Ishida–LeBrun gap

Session: S0910A01.  Agent2 / Constructor.  Step 45.  Phase: Execute.

This is a research proof note consolidating the corrected modules from
Steps 28, 34–36, 43–44, and A03 Steps 44–45.  It replaces the older
Step 41 assembly as the reference proof, using the corrected module
interfaces identified in Step 44.  This is not a final deliverable.

---

## 0. Statement

**Theorem (family-uniform restricted negative gap).**
*There exists a constant $\varepsilon_{\rm IL}>0$ with the following
property.  Let*
$$
M=\bigl(\#_{j=1}^m X_j\bigr)\# N,
\qquad m\in\{2,3\},
$$
*where each $X_j$ is a minimal complex surface of general type, $N$ is
closed oriented with $b_+(N)=0$, and the connected sum carries the
Ishida–LeBrun monopole sign family.  Set*
$$
A=\sum_j c_1^2(X_j)>0,
\qquad
D=4m-(2\chi+3\tau)(N),
\qquad
q=D-\frac{A}{3}.
\tag{0.1}
$$
*If $q\ge0$, then no smooth Riemannian metric $g$ on $M$ satisfies*
$$
\|g^{-1}(\operatorname{Ric}_g+g)\|_{\infty,\operatorname{op}}
<\varepsilon_{\rm IL}.
\tag{0.2}
$$
*The constant $\varepsilon_{\rm IL}$ is independent of
$A$, $D$, $q$, $N$, and the input metric.*

**Scope.** This is a restricted four-dimensional negative-sign result
for the Ishida–LeBrun no-Einstein geography.  It does not settle the
positive branch, arbitrary four-manifold topology, dimensions $n\ge5$,
or the Lean 4 formalization required by the full Yau Problem 26.

---

## 1. Proof architecture

The proof is by contradiction.  Suppose $(M_i,g_i)$ is a sequence in
the permitted geography with $E_i=\operatorname{Ric}_{g_i}+g_i$ and
$\delta_i=\|E_i\|_\infty\to0$, with $q_i\ge0$ and no Einstein metric
on any $M_i$.  The contradiction will come from three inputs:

- **Topological.** The mixed Seiberg–Witten estimate forces a specific
  calibrated curvature profile as $\delta_i\to0$, with a nonnegative
  density $\Phi$ whose total integral is $O(Q_i)=o(A_i)$ (§2).

- **Local impossibility.** Any Einstein germ with the calibrated profile
  violates Derdziński's local theorem.  By compactness this gives a
  positive local lower bound: on any bounded-curvature noncollapsed
  Riemannian 4-ball, the calibration density $\Phi$ is bounded below in
  the mean by a constant $\eta>0$ (§3).

- **Smoothing bridge.** A degenerate cutoff flow produces
  bounded-curvature noncollapsed terminal charts on a set carrying
  $A_i$-proportional volume, while preserving the global topological
  invariants that control $\Phi$ (§§4–6).

**Contradiction (§7).** The positive local lower bound on
$A$-proportional volume gives $\int\Phi\ge c\eta A_i$,
while the topological estimate gives $\int\Phi=o(A_i)$.

---

## 2. Near-critical calibration from Seiberg–Witten

### 2.1 Mixed estimate and averaged deficit

Each manifold $M_i$ in the Ishida–LeBrun family carries monopole
classes $\kappa_\varepsilon=\sum_j c_1(X_{j,i})+\sum_\ell
\varepsilon_\ell e_\ell$, $\varepsilon_\ell=\pm1$, where $e_\ell$ are
the exceptional cohomology classes.  The mixed Seiberg–Witten inequality
(LeBrun) for each class gives
$$
I_i:=\frac{1}{4\pi^2}\int
\!\left(\frac{s^2}{24}+2|W^+|^2\right)d\mu
\ge\frac{2}{3}(\kappa_\varepsilon^+)^2.
\tag{2.1}
$$
Averaging over all $2^{k_i}$ exceptional sign choices:
$$
I_i\ge\frac{2}{3}\left[A_i+\sum_\ell(e_\ell^+)^2\right].
\tag{2.2}
$$

With $J_i=\frac{1}{4\pi^2}\int\frac{|\mathring{\operatorname{Ric}}|^2}{2}$,
the Chern–Gauss–Bonnet identity in this geography gives
$$
I_i-J_i=(2\chi+3\tau)(M_i)=\frac{2A_i}{3}-q_i.
\tag{2.3}
$$
The averaged deficit is therefore
$$
D_{{\rm av},i}
=I_i-\frac{2}{3}A_i-\frac{2}{3}\sum_\ell(e_\ell^+)^2
=J_i-q_i-\frac{2}{3}\sum_\ell(e_\ell^+)^2
\ge0.
\tag{2.4}
$$
There is no additional $A_i$-term.  Since $q_i\ge0$,
$$
0\le D_{{\rm av},i}\le J_i.
\tag{2.5}
$$

### 2.2 Calibrated profiles

Under $\delta_i\to0$, the defect $E_i=\operatorname{Ric}+g$ satisfies
$|E_i|\le\delta_i$.  The calibrated volume identity
$$
\frac{\operatorname{Vol}(g_i)}{A_i}\to\frac{32\pi^2}{9}
\tag{2.6}
$$
follows from the Euler integral written as a function of $E_i$ and the
topology.  The averaged deficit satisfies $D_{{\rm av},i}/A_i\to0$, so
$q_i/A_i\to0$, $\sum(e_\ell^+)^2/A_i\to0$, and $J_i/A_i\to0$.

The completion-of-squares estimate gives
$$
\int(s+8\sqrt{6}\,|W^+|)^2\le864\pi^2D_{{\rm av},i},
\tag{2.7}
$$
and the self-dual spectral gap density satisfies
$$
\int\mathcal G_i\le48\pi^2D_{{\rm av},i},
\qquad
\mathcal G=f^2-(a_{*,-})^2\ge0,
\tag{2.8}
$$
where $f=\frac{2}{3}s-2\sqrt{2/3}\,|W^+|$ and $a_*=\frac{2}{3}s+2w$
with $w$ the smallest eigenvalue of $W^+$.

The calibrated profiles in normalized ($A$-scaled) mean are:
$$
s\to-4,\quad|W^+|^2\to\frac{1}{24},\quad
\operatorname{spec}(W^+)\to
\left(-\frac{1}{6},\frac{1}{12},\frac{1}{12}\right).
\tag{2.9}
$$

### 2.3 The calibration density

Define the nonnegative density
$$
\Phi=|E|^2+(s+4)^2+(s+8\sqrt{6}\,|W^+|)^2+\mathcal G.
\tag{2.10}
$$
For any metric on $M_i$ with $q_i\ge0$, the terminal estimates
(applicable because SW and Chern–Weil are topological) give
$$
\int(s+4)^2\le4Q,\qquad
\int(s+8\sqrt{6}\,|W^+|)^2\le108Q,\qquad
\int\mathcal G\le6Q,
\tag{2.11}
$$
where $Q=\int|E|^2$.  Hence
$$
\int_{M_i}\Phi\,d\mu\le119\,Q.
\tag{2.12}
$$
The inclusion of $|E|^2$ in $\Phi$ is essential: without it, the
terminal limit need not be Einstein.

---

## 3. Local impossibility and the quantitative lower bound

This section is the mathematical core of the contradiction.

### 3.1 Derdziński's forbidden germ

**Proposition 3.1 (Derdziński, 1983).** *Let $(U,g)$ be a connected
oriented Riemannian 4-manifold with $\delta W^+=0$ and $W^+\ne0$.  If
$W^+$ has at most two distinct eigenvalues, then the conformal metric
$(24|W^+|^2)^{1/3}g$ is locally Kähler.*

**Consequence.** An Einstein metric with $\operatorname{Ric}=-g$ and
$$
\operatorname{spec}(W^+)
=\left(-\frac{1}{6},\frac{1}{12},\frac{1}{12}\right),
\qquad
|W^+|^2=\frac{1}{24},
$$
would satisfy $\delta W^+=0$ (Bianchi) and have at most two eigenvalues
with $W^+\ne0$.  By Proposition 3.1, the conformal factor
$(24\cdot\frac{1}{24})^{1/3}=1$ gives $g$ locally Kähler.  But a
Kähler–Einstein metric with $\operatorname{Ric}=-g$ in dimension $4$
satisfies $|W^+|^2=s^2/24=16/24=2/3\ne1/24$.  Contradiction.

**No smooth Riemannian 4-germ exists with $\operatorname{Ric}=-g$ and
$\Phi=0$.**

### 3.2 Quantitative local lower bound (compactness consequence)

**Proposition 3.2.** *For any $K,\rho,v_0>0$ there exists
$\eta=\eta(K,\rho,v_0)>0$ such that: if $(B_\rho(0),g)$ is a
smooth Riemannian 4-ball with*
$$
|\operatorname{Rm}_g|\le K
\qquad\text{and}\qquad
\operatorname{Vol}(B_{\rho/2}(0))\ge v_0,
\tag{3.1}
$$
*then*
$$
\fint_{B_{\rho/2}(0)}\Phi_g\,d\mu_g\ge\eta.
\tag{3.2}
$$

**Proof.** Suppose not.  Then there exists a sequence of such balls
$(B_\rho(0),g_k)$ with bounded curvature, noncollapse, and
$\fint_{B_{\rho/2}}\Phi_{g_k}\to0$.  Since the volume of $B_{\rho/2}$
is bounded above (by curvature comparison), also
$\int_{B_{\rho/2}}\Phi_{g_k}\to0$.  In particular,
$$
E_k:=\operatorname{Ric}_{g_k}+g_k\to0
\quad\text{strongly in }L^2(B_{\rho/2}).
\tag{3.3}
$$
Since $|E_k|\le C(K)$ (from bounded curvature), interpolation gives
$E_k\to0$ strongly in every finite $L^p$.

The bounded curvature and noncollapse give a uniform harmonic radius on
a slightly smaller ball $B_{\rho'}$ ($\rho'<\rho/2$).  In harmonic
coordinates, the Ricci equation
$$
g_k^{ab}\partial_a\partial_b(g_k)_{ij}
=-2\operatorname{Ric}_{ij}(g_k)+Q_{ij}(g_k^{-1},\partial g_k)
\tag{3.4}
$$
has uniformly bounded $C^{1,\alpha}$ coefficients and the right-hand side
$$
\operatorname{Ric}(g_k)=-g_k+E_k
$$
with $E_k\to0$ strongly in $L^p$.  Interior elliptic estimates therefore
give, after passing to a subsequence,
$$
g_k\to g_\infty
\quad\text{strongly in }W^{2,p}_{\rm loc}(B_{\rho'})\;\;(\forall p<\infty).
\tag{3.5}
$$
Consequently the curvature tensors converge strongly in $L^p_{\rm loc}$.
Since $\Phi$ is a continuous algebraic function of curvature in the
bounded-curvature range, $\Phi_{g_k}\to\Phi_{g_\infty}$ strongly in
$L^1_{\rm loc}$, giving $\int\Phi_{g_\infty}=0$ and therefore
$\Phi_{g_\infty}\equiv0$ pointwise (by nonnegativity).

The vanishing of $\Phi$ forces:
$$
E_\infty=0,\quad s_\infty=-4,\quad
s_\infty+8\sqrt{6}\,|W^+_\infty|=0,\quad \mathcal G_\infty=0.
$$
The first gives $\operatorname{Ric}_{g_\infty}=-g_\infty$.  The second
and third give $|W^+_\infty|^2=1/24$.  For $\mathcal G=0$: the
minimum eigenvalue of $W^+$ satisfies $w=-1/6$, and the remaining
eigenvalues are both $1/12$ (from tracelessness and norm).  Hence
$\operatorname{spec}(W^+)=(-1/6,1/12,1/12)$.  Elliptic bootstrapping of
the limiting Einstein equation in harmonic coordinates makes $g_\infty$
smooth.  This is the forbidden germ of §3.1.  Contradiction.  $\square$

**Remark.** The key mechanism is not abstract Cheeger–Gromov smooth
compactness (which would require curvature-derivative bounds not
available here), but the elliptic upgrade: the $|E|^2$ component of
$\Phi\to0$ drives strong $W^{2,p}$ convergence through the Ricci
equation.  This is why $|E|^2$ must be included in $\Phi$.

### 3.3 Interpretation

Proposition 3.2 converts the local impossibility into a usable analytic
tool.  The constant $\eta$ depends only on the chart parameters
$(K,\rho,v_0)$, not on the global manifold or topology.  It is a
compactness consequence: its value need not be explicitly computed, but
its existence prevents any controlled chart from realizing the calibrated
profile.

The long analytic work of §§4–6 below has one purpose: to produce
terminal charts satisfying the hypotheses $(3.1)$ on a set carrying
positive $A$-proportional volume.  The topological inequality
$\int\Phi\le119Q=o(A)$ then contradicts the locally forced lower bound.

---

## 4. Support selection

### 4.1 Volume-average maximal function and good set

Set $R_0$ with $7r\le R_0$ for a fixed small radius $r\in(0,r_0]$.
Define
$$
\mathcal M_{R_0}f(x)=\sup_{0<s\le R_0}\fint_{B_s(x)}f.
\tag{4.1}
$$
Under $\operatorname{Ric}\ge-2g$ (which holds for $\delta_i$ small),
the weak-type maximal inequality (Bishop–Gromov comparison) gives:
$$
\operatorname{Vol}\{x:\mathcal M_{R_0}(|\operatorname{Rm}|^2)(x)
>\lambda\}
\le\frac{C(R_0)}{\lambda}\int_M|\operatorname{Rm}|^2.
\tag{4.2}
$$
Choose $\lambda=\widetilde\gamma^2/r^4$, where $\widetilde\gamma$ is
fixed below the absorption threshold by a dimensional factor.
Using $\int|\operatorname{Rm}|^2\le C_0A_i$ (Chern–Weil):
$$
\operatorname{Vol}(\text{bad set})
\le\frac{Cr^4}{\widetilde\gamma^2}A_i.
\tag{4.3}
$$
Fix $r$ so $Cr^4/\widetilde\gamma^2<16\pi^2/9$.  For $i$ large:
$$
\operatorname{Vol}(\text{good set})
\ge\left(\frac{32\pi^2}{9}
-\frac{Cr^4}{\widetilde\gamma^2}\right)A_i
\ge\alpha_0A_i.
\tag{4.4}
$$

### 4.2 Cutoff construction

Choose a maximal $r$-separated subset $\{x_\alpha\}$ of the good set.
Apply $14r$-separated coloring to partition the centers into
$N_0\le C(n,r)$ classes; at least one class carries volume
$\ge\alpha_0A_i/N_0$.

For each center $x_\alpha$ in the selected class, choose smooth cutoffs:
$$
\chi_\alpha=1\text{ on }B_{5r}(x_\alpha),\qquad
\operatorname{supp}\chi_\alpha\subset B_{6r}(x_\alpha),\qquad
|d\chi_\alpha|\le C/r.
\tag{4.5}
$$
An auxiliary cutoff:
$$
\eta_\alpha=1\text{ on }B_{6r}(x_\alpha),\qquad
\operatorname{supp}\eta_\alpha\subset B_{7r}(x_\alpha).
\tag{4.6}
$$
The global weight is $a_i=\sum_\alpha\chi_\alpha^2\in[0,1]$,
well-defined by disjointness of the $B_{7r}$ buffers.  On the complement
$M_i\setminus\bigcup_\alpha B_{7r}$, $a_i=0$ and the metric will be
stationary under the cutoff flow.

Each support satisfies $r^4\fint_{B_{7r}}|\operatorname{Rm}|^2
\le\widetilde\gamma^2$ by the maximal-function threshold.  Higher
cutoff jets $\nabla^m\chi_\alpha$ are finite for each smooth datum;
no sequence-uniform bound on jets of order $\ge2$ is asserted.

---

## 5. Cutoff flow construction by coefficient regularization

### 5.1 Regularized flow

For each fixed smooth datum $(M_i,g_i,\chi)$, set
$b_\varepsilon=\chi^2+\varepsilon^2$ and solve the transported-coefficient
geometric flow
$$
\partial_tg_\varepsilon=-2b_\varepsilon(\operatorname{Ric}_{g_\varepsilon}
+g_\varepsilon),
\tag{5.1}
$$
via the DeTurck gauge with transported coefficient
$\widehat b_\varepsilon=b_\varepsilon\circ\varphi_t^{-1}$.  For each
$\varepsilon>0$, the coefficient is uniformly elliptic, and standard
quasilinear parabolic theory gives short-time existence.

The critical observation is that $\varepsilon$-uniform geometric bounds
are available:
$$
0<b_\varepsilon\le2,\qquad
\nabla^r b_\varepsilon=\nabla^r(\chi^2)\;\;(r\ge1),\qquad
\frac{|\nabla b_\varepsilon|^2}{b_\varepsilon}\le4|d\chi|^2,\qquad
\frac{\chi^2}{b_\varepsilon}\le1.
\tag{5.2}
$$
No derivative of $b_\varepsilon^{-1}$ is used.

### 5.2 Common time and smooth limit

The $\varepsilon$-uniform geometric energies — the staggered finite-$L^p$
induction for $U_m^\varepsilon=b_\varepsilon T_\varepsilon$, the first-exit
improvement, and fixed-background connection-difference bounds — yield
a common positive existence time $T_*$ and $\varepsilon$-uniform
fixed-coordinate space-time bounds.

**What is needed for this step.** The algebraic bounds (5.2) are necessary
structural inputs but are not alone sufficient for a common time.  The
complete $\varepsilon$-uniform estimate package must include:
$\Lambda^{-1}g_0\le g_\varepsilon(t)\le\Lambda g_0$ (metric equivalence),
$\sup|U_\varepsilon|\le K$ (zero-order weighted bound), the full unweighted
$T_\varepsilon$ and derivative chain, uniform Sobolev constants, and
fixed-background connection-difference control $\nabla^{g_\varepsilon}
-\nabla^{g_0}$.  These estimates are obtained on the regularized flows
**without** using frozen complement or disjoint-support identities (which
are only valid for the exact degenerate flow).  The staggered continuation
mechanism of §5.3 provides the derivative structure needed for these
bounds, but the complete fixed-coordinate compactness argument is a
separate analytic module.

A subsequence converges smoothly **in fixed background coordinates**
(not merely modulo diffeomorphism) to a smooth metric solving the exact
degenerate equation
$$
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
\tag{5.3}
$$
Fixed-coordinate convergence is essential: it preserves the support
function $\chi$ and the support geometry, so that the stationary
complement and disjoint-support identities can be applied to the limit
without repositioning the cutoffs.
**Only after this limit is taken** do the identities for the exact flow
(stationary complement, frozen outer metric, disjoint-support summation)
become valid.

Uniqueness is not needed: one smooth exact flow suffices.  Restart from
a smooth positive terminal metric uses the same construction with
autonomous time-jet matching at the gluing time.

### 5.3 Weighted extension mechanism

The all-order continuation on the exact flow uses the staggered
schedule
$$
T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to T_2\to\cdots
\tag{5.4}
$$
where $U_m=\nabla^m(aT)$, $C_{m+1}=\nabla^{m+1}\chi$, and
$T_m=\nabla^m T$.

At each weighted stage, $C_{m+1}$ is the **current partner** of $U_m$,
not a previous-layer input.  The coupled energy satisfies
$$
\frac{d}{dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
+c_{m,p}\int a|\nabla U_m|^2|U_m|^{p-2}
\le C_{m,p}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).
\tag{5.5}
$$
The decisive structural fact (Steps 43/A03-45): every highest cutoff jet
$C_{m+2}$ in the weighted evolution carries $\chi$ weight from the
product-rule identity $\nabla^{m+2}(\chi^2)=2\chi C_{m+2}+\text{lower}$.
The two sources (Hessian-$a$ coefficient and extracted Laplacian) both
produce $\chi C_{m+2}*U_0$.  After integrating once off $C_{m+2}$,
the remaining $\chi$ pairs with the weighted dissipation
$\int\chi^2|\nabla U_m|^2|U_m|^{p-2}$.

The zero-order unweighted $T\in L^p$ seed uses $|aT|\le K$ to
bound the quadratic reaction by $K|T|^p$ and signed integration
by parts for the Hessian-$a$ contraction $B^{pq}=|T|^2g^{pq}
+(\operatorname{tr}E)E^{pq}-2(E^2)^{pq}$, giving a Gronwall with
finite per-datum coefficients.

---

## 6. First-exit smoothing and controlled terminal charts

On the exact flow (5.3), the selected supports have stationary
complement.  The first-exit estimates split into three independent
branches from the initial curvature seed $K_2^\eta$:

### 6.1 Curvature branch

The absorption parameter $\gamma=\mathcal S(0)\sqrt{K_2^\eta(0)}
\lesssim Cr^2\sqrt{K_0}$ is collapse-independent after the
Whitney-volume cancellation.  The homogeneous propagation
$$
(K_2^\eta)'\le C(1+r^{-2})K_2^\eta
\tag{6.1}
$$
and the integrated potential $Y=\int\eta^2aF^3$ yield the curvature
Moser endpoint
$$
\|aF(t)\|_\infty\le\frac{C\gamma}{t}.
\tag{6.2}
$$

### 6.2 Defect branch

The unregularized sixth-power defect energy $J_6=\int\eta^2a^4|E|^6$
satisfies
$$
J_6'+cX_6\le C(1+r^{-2})J_6,
\tag{6.3}
$$
using the signed Hessian-$a$ defect contraction (Step 35).  The defect
Moser endpoint is
$$
\|aE(t)\|_\infty\le C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\tag{6.4}
$$

### 6.3 Global $Q$ branch

The global Einstein defect $Q(t)=\int_M|E|^2\,d\mu_t$ is propagated
on the exact flow using disjoint buffered supports and frozen complement:
$$
Q(T)\le e^{C(1+r^{-2})T}Q(0).
\tag{6.5}
$$
Since $Q(0)/A_i\to0$ (from $\delta_i\to0$ and calibrated volume),
$Q(T)/A_i\to0$ for fixed $T=\theta r^2$.

### 6.4 Terminal chart properties

The metric drift is controlled by the integrable defect velocity (6.4):
$$
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C\delta\theta^{2/3}r^2\to0.
\tag{6.6}
$$
On the terminal plateau $\{a=1\}$ (i.e.\ inside $B_{5r}(x_\alpha)$):

- **Bounded curvature:** the endpoint (6.2) at time $T=\theta r^2$ gives
  $|\operatorname{Rm}(T)|\le C\gamma/(\theta r^2)\le K$ for fixed
  parameters.

- **Inner centers:** the set $P_i^{\rm in}=\bigcup_\alpha
  B_r(x_\alpha)$ lies strictly inside the plateau.  Bishop–Gromov gives
  $\operatorname{Vol}(P_i^{\rm in})\ge c\,\alpha_0A_i$.  The drift (6.6)
  preserves this lower bound for $i$ large.

- **Noncollapse:** on the terminal metric, Rauch comparison for bounded
  sectional curvature gives a universal volume lower bound
  $\operatorname{Vol}(B_{\rho/2}(p))\ge v_0(K,\rho)>0$ for any
  $p\in P_i^{\rm in}$ and fixed $\rho\le r/2$.  (This is noncollapse on
  the tangent-space pullback, not on the base manifold.)

- **Geodesic buffer:** for $p\in B_r(x_\alpha)$, all geodesics of
  length $\le\rho$ from $p$ remain in $B_{2r}(x_\alpha)\subset
  B_{5r}(x_\alpha)$, inside the bounded-curvature plateau.

---

## 7. Terminal contradiction

### 7.1 Topological recalibration

The terminal metric $g_i(T)$ lives on the same smooth manifold, so the
mixed SW inequality (2.1) holds for $g_i(T)$.  The corrected deficit is
$$
D_{{\rm av},i}(T)
=J_i(T)-q_i-\frac{2}{3}\sum_\ell(e_\ell^+(T))^2
\le J_i(T)
\le\frac{Q_i(T)}{8\pi^2}.
\tag{7.1}
$$
Thus $\int\Phi_i\,d\mu_T\le119\,Q_i(T)$ and
$Q_i(T)/A_i\to0$ (from (6.5)).

### 7.2 Averaging against the local lower bound

Each terminal pullback chart from $p\in P_i^{\rm in}$ satisfies the
hypotheses of Proposition 3.2 with the fixed parameters $(K,\rho,v_0)$
from §6.4.  Using the Liouville average
$$
A_\rho\Phi(p)
=\frac{\int_{S_pM}\int_0^\rho\Phi(\exp_p(t\xi))J_p(t,\xi)\,dt\,d\xi}
{\int_{S_pM}\int_0^\rho J_p(t,\xi)\,dt\,d\xi},
\tag{7.2}
$$
Rauch comparison gives constants $0<c_0<C_0$ depending only on
$(K,\rho)$ such that $c_0t^3\le J_p(t,\xi)\le C_0t^3$ for
$0<t\le\rho$ on the exponential pullback.  Hence the denominator in
(7.2) is uniformly bounded below and
$$
\int_{P_i^{\rm in}}A_\rho\Phi_i(p)\,d\mu_T(p)
\le C(K,\rho)\rho^{-4}
\int_0^\rho t^3\int_{S M|_{P_i^{\rm in}}}
\Phi_i(\pi\circ\varphi_t(v))\,d\Lambda(v)\,dt,
$$
where $\varphi_t$ is the geodesic flow and $d\Lambda$ is Liouville
measure on the unit tangent bundle.  For each fixed $t$, $\varphi_t$
is a diffeomorphism of $SM$ preserving $d\Lambda$, so
$$
\int_{S M|_{P_i^{\rm in}}}\Phi_i(\pi\circ\varphi_t(v))\,d\Lambda(v)
\le \int_{SM}\Phi_i(\pi(v))\,d\Lambda(v)
=\omega_3\int_{M_i}\Phi_i\,d\mu_T.
$$
Thus
$$
\int_{P_i^{\rm in}}A_\rho\Phi_i(p)\,d\mu_T(p)
\le C(K,\rho)\int_{M_i}\Phi_i\,d\mu_T
\le119C(K,\rho)\,Q_i(T).
\tag{7.3}
$$
This argument uses Liouville invariance and Rauch bounds, not injectivity of
$\exp_p$; short geodesic loops or collapse do not create a multiplicity
factor.  The constant is independent of the number of supports because
$P_i^{\rm in}$ is one global set and the final comparison is on $SM$.

**If $A_\rho\Phi_i(p_i)\to0$ for some sequence $p_i\in P_i^{\rm in}$:**
the exponential-pullback metrics on $B_\rho(0)\subset T_{p_i}M$ have
$|\operatorname{Rm}|\le K$ and $\operatorname{Vol}(B_{\rho/2})\ge v_0$.
By Proposition 3.2 (applied on $B_{\rho/2}$ inside the pullback ball),
$\fint_{B_{\rho/2}}\Phi\ge\eta$.  Since $\Phi\ge0$ and the volume ratio
$\operatorname{Vol}(B_\rho)/\operatorname{Vol}(B_{\rho/2})\le C(K,\rho)$,
this gives
$$
A_\rho\Phi_i(p_i)\ge c(K,\rho,v_0)\,\eta>0,
\tag{7.4a}
$$
contradicting $A_\rho\Phi_i(p_i)\to0$.

**Therefore:** $A_\rho\Phi_i(p)\ge\eta'>0$ for all $p\in P_i^{\rm in}$
and all $i$ large, where $\eta'=c(K,\rho,v_0)\,\eta(K,\rho/2,v_0)$.

### 7.3 Global contradiction

Combining:
$$
\eta'\cdot\operatorname{Vol}(P_i^{\rm in})
\le C(K,\rho)\int_{P_i^{\rm in}}A_\rho\Phi_i
\le119C(K,\rho)\,Q_i(T).
$$
Using $\operatorname{Vol}(P_i^{\rm in})\ge c'\alpha_0A_i$:
$$
\eta'\,c'\alpha_0A_i\le119C(K,\rho)\,Q_i(T).
\tag{7.5}
$$
But $Q_i(T)/A_i\to0$.  For $i$ large, the right side is less than
$\eta' c'\alpha_0A_i$.  Contradiction.  $\square$

---

## 8. Bounded-$A$ subsequences

If $A_i$ is bounded, then $q_i/A_i\to0$ with $q_i\ge0$ and
$q_i\in\frac{1}{3}\mathbb Z_{\ge0}$ forces $q_i=0$ eventually.  Set
$A_0=A_i$ for the eventual constant value.  The calibrated volume gives
$\operatorname{Vol}(g_i)\to32\pi^2A_0/9>0$, and the support construction
with fixed $\alpha_0>0$ applied to $A_0$ yields the same positive
terminal plateau volume.  The smoothing and contradiction arguments
proceed identically with $A_i$ replaced by the fixed $A_0$.  $\square$

---

## 9. Relation to Yau Problem 26

The theorem rules out one well-studied family of no-Einstein four-manifolds
as a source of uniformly tight negative Ricci pinching.  It is meaningful
because:

1. The Ishida–LeBrun geography provides the only known smooth closed
   4-manifolds without Einstein metrics of any sign that also satisfy
   the strict Hitchin–Thorpe inequality.

2. The family-uniform constant $\varepsilon_{\rm IL}$ covers all
   topological parameters $(A,D,q,N)$ and all input metrics, including
   potentially collapsing sequences; it is not a topology-dependent gap.

3. The mechanism — cutoff-flow smoothing into a forbidden-germ
   contradiction — is intrinsically four-dimensional: it uses the
   self-dual Weyl spectrum, Seiberg–Witten invariants, and Derdziński's
   local theorem.

The following remain open:

- **Positive branch:** no analogous obstruction family or smoothing
  mechanism has been established for $\operatorname{Ric}\approx+g$.
  Positive Einstein collapse (lens spaces, torus quotients) is not
  excluded, and the first-order Ozuch chirality obstruction has a
  bi-Kähler loophole (A02 Step 44–45).

- **Arbitrary 4-manifold topology:** the no-Einstein condition uses the
  Ishida–LeBrun connected-sum structure.  Manifolds admitting Einstein
  metrics are not addressed.

- **Dimensions $n\ge5$:** the Seiberg–Witten and self-dual Weyl machinery
  is specific to $n=4$.  No counterpart mechanism exists in higher
  dimensions.

- **Dimension-only constants:** even if both four-dimensional sign branches
  were settled, the original proposition asks for constants depending only
  on $n$, covering all smooth closed $n$-manifolds.

- **Lean formalization:** the formal verification required by the research
  goal has not been attempted for any part of this argument.

---

## 10. Module dependencies

| Component | Source |
|---|---|
| Seiberg–Witten mixed estimate | LeBrun; Ishida–LeBrun Prop 10, Cor 11, Thm D |
| Calibrated profiles and $\Phi$ | Steps 5–8; corrected algebra Step 42 |
| Derdziński Prop 5 | Primary source (1983); Steps 7–8 |
| Support construction | §4; Steps 38, 40, 42 corrections |
| Coefficient regularization and exact flow | A03 Step 45 coordinate ledger; Step 43 H-DT |
| Weighted extension (current pair) | Step 43 H-WU + A03 Step 45 |
| Zero-order $T\in L^p$ seed | A03 Step 44; Step 41 §3 |
| Curvature/defect signed-Hessian contractions | Step 35 |
| $K_2^\eta$, $Y$, $J_6$, Moser endpoints | Step 34 |
| Global $Q$ propagation | Step 36 |
| Terminal recalibration/pullback | Step 28; corrected by Step 44 |
| Preceptor reading of end-to-end chain | Step 44 |
