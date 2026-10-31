# Step 47: Consolidated restricted negative IL defect gap theorem

> **Step 49 supersession notice.** The hypothesis list in §1 is replaced by
> `step49_corrected_restricted_theorem_statement.md` (explicit monopole sign-family,
> small initial Einstein defect in Module S). The flow construction §4b incorrectly
> transferred exact-flow localized estimates to the $b_\varepsilon$ regularization
> (where the exterior is active); §6 treated $C\gamma/t$ as a uniform bound from
> $t = 0$. Both are repaired by `step49_normalized_flow_existence_and_extension.md`
> (§4: coefficient regularization with $\varepsilon$-independent global energies;
> §6: positive-time slab argument). The terminal repair (§7, core-ball Lipschitz +
> Bishop–Gromov) and the modular architecture (Module S/O) remain valid.

## 0. Overview and modularity

This note assembles the restricted four-dimensional negative Ishida–LeBrun
defect gap theorem from all verified components across Sessions A01 and A03,
Steps 3–46.  The proof separates into two independent modules:

**Module S** (Smoothing).  From *any* closed Riemannian 4-manifold $(M,g)$
with $\operatorname{Ric}\approx-g$, a uniform curvature-to-volume budget,
and positive total volume, produce bounded-curvature terminal charts where
the Einstein defect is pointwise small.  The key mechanism is a
*collapse-independent* Sobolev absorption parameter that arises from the
volume-averaging Hardy–Littlewood maximal function in critical dimension 4.

**Module O** (Obstruction).  On the Ishida–LeBrun no-Einstein geography, a
nonneg pointwise spectral density $\mathfrak D$ satisfies
$\int\mathfrak D\le119Q+912\pi^2(-q)_+$ for any metric, where
$Q=\int|E|^2$.  At a terminal point where $\mathfrak D=0$, the self-dual
Weyl spectrum is forced to $(-1/6,1/12,1/12)$, contradicting the
Derdziński/projector–Bochner obstruction.

Module S is topology-independent.  It can test any no-Einstein mechanism that
supplies (i) a uniform curvature-to-volume budget and (ii) a nonneg
pointwise density whose integral is controlled by $Q$.

---

## 1. Statement

**Theorem A.**  *Let $m\in\{2,3\}$.  Let
$M=(\#_{j=1}^mX_j)\#N$ be a closed oriented smooth 4-manifold where:*
- *each $X_j$ is a simply-connected smooth complex surface of general type
  with $c_1^2(X_j)>0$,*
- *$N$ is a closed oriented smooth 4-manifold with $b_+(N)=0$,*
- *$q:=D-A/3\ge0$, where $A=\sum c_1^2(X_j)$ and $D=4m-(2\chi+3\tau)(N)$.*

*Then there exists $\delta_0=\delta_0(M)>0$ such that every smooth Riemannian
metric $g$ on $M$ satisfies*
\[
  \|g^{-1}(\operatorname{Ric}_g+g)\|_\infty\ge\delta_0.
\]

**Corollary (above-critical gap).**  *If $q/A\ge c>0$, then
$\delta_0\ge\min(1/4,\sqrt{3c/16})$.  No smoothing argument is needed.*

**Corollary (family uniformity).**  *Within any subfamily with $A\le A_{\max}$,
the constant $\delta_0$ is bounded below by a positive constant depending only
on $m$ and $A_{\max}$.*

**Proof structure.**  Assume for contradiction a sequence $(M_i,g_i)$ with
$\delta_i:=\|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_\infty\to0$.
The proof proceeds through: calibrated profile (§2), support selection (§3),
flow existence (§4), first-exit bootstrap (§5), continuation (§6),
terminal contradiction (§7).

---

## 2. Calibrated profile (Module O, Part 1)

Write $E_i=\operatorname{Ric}_{g_i}+g_i$, $Q_i=\int|E_i|^2$,
$s_i=\operatorname{scal}(g_i)$.  Since $|E_i|\le\delta_i$,
$|s_i+4|\le2\delta_i$ and $|\operatorname{Ric}_i^\circ|\le\delta_i$.

**Chern–Gauss–Bonnet + Hirzebruch.**
$(2\chi+3\tau)(M_i)=A_i-D_i=2A_i/3-q_i$.

**Chern–Weil identity (CW).**
\[
  \frac{1}{4\pi^2}\int\!\left(\frac{s^2}{24}+2|W^+|^2-\frac{|\operatorname{Ric}^\circ|^2}{2}\right)=\frac{2A_i}{3}-q_i.
\]
With $s=-4+O(\delta)$ and $|\operatorname{Ric}^\circ|=O(\delta)$ this gives:
\[
  \frac{\operatorname{Vol}_i}{6\pi^2}+\frac{1}{2\pi^2}\int|W_i^+|^2
  =\frac{2A_i}{3}+O(\delta_i^2A_i).
\]

**Published SW monopole inequality** (LeBrun Prop 3.8, sign-averaged by
Ishida–LeBrun):
\[
  \int(s-\sqrt6|W^+|)^2\ge72\pi^2 A_i.
\]

**Calibrated profile.**  Combining these as $\delta_i\to0$:
\[
  \operatorname{Vol}_i\to\tfrac{32\pi^2}{9}A_i,\qquad
  \int|W_i^+|^2\to\tfrac{4\pi^2}{27}A_i,\qquad
  \int|\operatorname{Ric}_i^\circ|^2\to0.
\]

**Calibration inequality** (completed square, Step 15 constant-verified):
\[
  \int\!\left(|W_i^+|-\tfrac{1}{2\sqrt6}\right)^2\le\tfrac{7}{24}Q_i.
  \tag{2.1}
\]
**Scalar–Weyl calibration:**
\[
  \int(s_i+8\sqrt6|W_i^+|)^2\le864\pi^2(R_i-q_i),\quad
  R_i=\tfrac{1}{8\pi^2}\!\int|\operatorname{Ric}_i^\circ|^2\le\tfrac{Q_i}{8\pi^2}.
  \tag{2.2}
\]

**Above-critical exclusion.**  The mixed identity $R_i\ge q_i+\ldots$ in
the Ishida–LeBrun algebra yields $\delta_i\ge\min(1/4,\sqrt{3q_i/(16A_i)})$.
Hence any escaping sequence must have $q_i/A_i\to0$.  For the bounded-$A$
subfamily: $q\in(1/3)\mathbb Z_{\ge0}$ and $q/A\to0$ forces $q_i=0$
eventually.  Both sub-cases enter the smoothing module below.

**Curvature-to-volume budget.**
\[
  \Lambda:=\frac{\int(1+|\operatorname{Rm}|^2)}{\operatorname{Vol}}
  =O(1)\qquad\text{(geography-uniform)}.
  \tag{2.3}
\]
This is the only input Module S requires from the topology.

---

## 3. Support construction (Module S, Part 1)

Fix a single datum $(M,g)$ with $\operatorname{Ric}\ge-3g$ (which follows
from $|E|\le1$) and the budget (2.3).

**Step 3a. Volume-averaging maximal function.**
Define
\[
  \mathcal M_{\rm vol}(|{\rm Rm}|^2)(x)
  =\sup_{0<\rho\le1}\frac{1}{\operatorname{Vol}B_\rho(x)}\int_{B_\rho(x)}|{\rm Rm}|^2.
\]
Under $\operatorname{Ric}\ge-3g$, Bishop–Gromov gives local volume doubling
(ratio $\le C(4)$ for $\rho\le1$).  The Hardy–Littlewood weak-type
inequality on the resulting doubling space gives
\[
  \operatorname{Vol}\{M_{\rm vol}(|{\rm Rm}|^2)>\kappa^2\}
  \le\frac{C_{\rm HL}}{\kappa^2}\int|{\rm Rm}|^2
  \le\frac{C_{\rm HL}\Lambda}{\kappa^2}\operatorname{Vol}.
  \tag{3.1}
\]
Choose $\kappa_0^2=4C_{\rm HL}\Lambda$ (geography-uniform, independent of
collapse).  Then the *good set*
\[
  G:=\{x:\mathcal M_{\rm vol}(|{\rm Rm}|^2)(x)\le\kappa_0^2\}
\]
satisfies $\operatorname{Vol}(G)\ge3\operatorname{Vol}(M)/4$.

**Step 3b. Disjoint Sobolev domains.**
Choose a small radius $r>0$ (to be fixed in §5).  Take a maximal
$r$-separated net $\{x_\alpha\}\subset G$.  Form the graph with edge
$x_\alpha\sim x_\beta$ when $d(x_\alpha,x_\beta)\le12r$.  By volume doubling,
the graph degree is $\le C_{\rm deg}(4)$, hence chromatic number
$\le C_{\rm chr}(4)$.  Choose the color class $\mathcal C$ with
\[
  \sum_{\alpha\in\mathcal C}\operatorname{Vol}B_r(x_\alpha)
  \ge\frac{\operatorname{Vol}(G)}{C_{\rm chr}}
  \ge\frac{3}{4C_{\rm chr}}\operatorname{Vol}.
  \tag{3.2}
\]
All centers in $\mathcal C$ satisfy $d(x_\alpha,x_\beta)>12r$, so the
$B_{6r}(x_\alpha)$ are pairwise disjoint.

**Step 3c. Cutoffs.**  On each $\alpha\in\mathcal C$, take smooth radial
cutoffs using an exhaustion of distance:
- $\chi_\alpha=1$ on $B_{4r}(x_\alpha)$, $\operatorname{supp}\chi_\alpha\subset B_{5r}(x_\alpha)$,
  $\|d\chi_\alpha\|_\infty\le C/r$;
- $\eta_\alpha=1$ on $B_{5r}(x_\alpha)$, $\operatorname{supp}\eta_\alpha\subset B_{6r}(x_\alpha)$,
  $\|d\eta_\alpha\|_\infty\le C/r$.

Set $a=\sum_{\alpha\in\mathcal C}\chi_\alpha^2$.
Then $a=1$ on the union of *plateaux* $\bigcup B_{4r}(x_\alpha)$, and
$a=da=0$ on $\operatorname{supp}d\eta_\alpha$ for every $\alpha$.
Higher cutoff derivatives $\|\nabla^k\chi_\alpha\|_\infty\le C_k/r^k$ are
per-datum controlled.

**Step 3d. Collapse cancellation** (the key 4D mechanism).
On each $B_{6r}(x_\alpha)$, the local Sobolev inequality
(Maheux–Saloff-Coste under $\operatorname{Ric}\ge-3$) gives
\[
  \|u\|_{L^4}^2\le\mathcal S_\alpha\bigl(\|\nabla u\|_{L^2}^2
  +r^{-2}\|u\|_{L^2}^2\bigr),
  \qquad
  \mathcal S_\alpha\le\frac{Cr^2}{\sqrt{\operatorname{Vol}B_{6r}(x_\alpha)}}.
  \tag{3.3}
\]
Since $x_\alpha\in G$:
$\int_{B_{6r}}|{\rm Rm}|^2\le\kappa_0^2\operatorname{Vol}B_{6r}(x_\alpha)$.
The initial curvature energy on the support is
\[
  K_{2,\alpha}(0):=\int\eta_\alpha^2(1+|{\rm Rm}|^2)
  \le(1+\kappa_0^2)\operatorname{Vol}B_{6r}(x_\alpha).
\]
The absorption parameter is
\[
  \gamma_\alpha=\mathcal S_\alpha K_{2,\alpha}(0)^{1/2}
  \le\frac{Cr^2}{\sqrt{\operatorname{Vol}}}
  \cdot\sqrt{(1+\kappa_0^2)\operatorname{Vol}}
  =Cr^2\sqrt{1+\kappa_0^2}.
  \tag{3.4}
\]
**The volume cancels exactly.**  Hence $\gamma_\alpha\le C'r^2$ with a
geography-uniform constant $C'$.  This is the 4D critical-dimension
collapse cancellation: the Sobolev constant's $\operatorname{Vol}^{-1/2}$
is exactly compensated by the volume-averaging integral bound.

---

## 4. Coefficient-regularized flow (Module S, Part 2)

**4a. Regularized equation.**  Set $b_\varepsilon=a+\varepsilon^2$ for
$\varepsilon\in(0,1]$ and consider
\[
  \partial_tg=-2b_\varepsilon(\operatorname{Ric}_g+g).
  \tag{4.1}
\]
Since $b_\varepsilon\ge\varepsilon^2>0$, equation (4.1) is strictly
parabolic.  A DeTurck gauge with transported hatted coefficient
$\hat b_\varepsilon=b_\varepsilon\circ\varphi_t^{-1}$ produces a
quasilinear parabolic system admitting short-time smooth solutions by
standard theory.

**4b. Regularization-uniform energy bounds.**
The key identities are
\[
  |db_\varepsilon|^2/b_\varepsilon\le4|d\chi|^2,
  \qquad
  a/b_\varepsilon\le1.
  \tag{4.2}
\]
These ensure that the weighted curvature moments $K_q$, defect moments
$J_m$, and global $Q$ satisfy the *same* differential inequalities as in
the $\varepsilon=0$ case, with constants independent of $\varepsilon$.  In
particular, the first-exit bootstrap (§5) produces a common per-datum time
$T_0>0$ that is $\varepsilon$-uniform.

**4c. Passage $\varepsilon\to0$.**
On $[0,T_0]$: uniform $C^0$ metric bounds and all-order covariant
derivative bounds (§6).  The connection differences
$A_\varepsilon=\nabla^{g_\varepsilon}-\nabla^{g_0}$ satisfy
$\partial_tA_\varepsilon=g_\varepsilon^{-1}*\nabla\operatorname{Ric}(U_\varepsilon)$,
with uniformly bounded RHS.  By Arzelà–Ascoli on fixed-coordinate
atlases, a subsequence $\varepsilon_j\to0$ converges in $C^\infty_{\rm loc}$
to a smooth solution of the exact degenerate flow
$\partial_tg=-2a(\operatorname{Ric}+g)$ on $[0,T_0]$.

**4d. Restart.**  At any smooth endpoint $t^*\le T_0$, the evolved metric
$g(t^*)$ is smooth.  Reapply the same construction (with a new
initial datum).  Time jets match because both the old and new solutions
solve (4.1) with $\varepsilon=0$.  This gives smooth extension, and by the
continuation criterion (§6), the flow extends as long as
$|U|<\infty$.

**References:** `step45_coordinate_tensor_ledger_and_regularized_closure.md` §7;
A01 `step43_H_DT_assessment.md`.

---

## 5. First-exit bootstrap (Module S, Part 3)

All estimates below are on the exact $\varepsilon=0$ flow obtained in §4.
Set $T=\theta r^2$ with $\theta$ to be chosen.  Define the first-exit time
$\tau=\min(T,\inf\{t:K_2(t)=2K_{2}(0)\text{ or }d(t)=d_0\})$, where
$d(t)=\int_0^t\|aE\|_\infty\,ds$ is the metric drift and $d_0>0$ is a
small constant ensuring bilipschitz comparison.

**5a. Parameter ordering.**  Choose:
1. $\kappa_0^2=4C_{\rm HL}\Lambda$ (geography-uniform);
2. $r\le r_0:=(\gamma_0/C')^{1/2}$ where $\gamma_0$ is the Moser threshold;
3. $\theta\le\ln(3/2)/(C_K(r^2+1))$ ensuring $K_2(T)<2K_2(0)$;
4. $\delta_0$ from the drift condition $C\delta_0\theta^{2/3}r^2<d_0$.

**5b. $K_2$ evolution.**
$H_2=\int\eta^2(1+|{\rm Rm}|^2)$.  The normalized-flow curvature equation
and two-factor absorption with $\gamma\le C'r^2\le\gamma_0$ give
\[
  K_{2}(t)+c\int_0^t D_2\le K_2(0)+C_K\int_0^t(1+r^{-2})K_2\,ds,
  \tag{5.1}
\]
hence by Grönwall $K_2(t)\le e^{C_K(1+r^{-2})t}K_2(0)$.
At $t=\theta r^2$: $K_2\le e^{C_K\theta(r^2+1)}K_2(0)$.  Choosing
$\theta\le\ln(3/2)/(C_K(r^2+1))$ ensures $K_2(T)\le(3/2)K_2(0)<2K_2(0)$.

**5c. $Y$ propagation.**
$Y=\int\eta^2aF^3$.  Good-slice propagation using
$\mathcal S^2K_2\le C\gamma^2$:
\[
  Y(t)\le C\gamma K_2(0)/t,
  \qquad
  \mathcal S^2 Y(t)\le C\gamma^3/t.
  \tag{5.2}
\]

**5d. $J_6$ persistence** (Step 35, unregularized, no $Y$-dependence).
$J_6=\int\eta^2a^4|E|^6$.  Using $s=|E|^2$ directly and two-factor
absorption with $\gamma$:
\[
  J_6(t)\le e^{C(1+r^{-2})t}J_6(0)\le e^{C(1+r^{-2})\theta r^2}\delta^6\cdot C_{\rm vol}.
  \tag{5.3}
\]
This preserves the initial $\delta^6$ factor.

**5e. All-$p$ defect Moser ladder** (Step 39).
For every real $p\ge6$, with $z_p=\eta a^{(p-1)/2}|E|^{p/2}$
and $H_p^E=\int\eta^2a^{p-2}|E|^p$:
\[
  (H_p^E)'+c\|\nabla z_p\|_2^2
  \le Cp^4(1+r^{-2}+\mathcal S^2Y)H_p^E.
  \tag{5.4}
\]
Three-factor Hölder + Young$(3,\tfrac32)$ gives a Grönwall coefficient
with polynomial $p$-growth; the two-factor method would require
$\gamma\lesssim1/p$, which fails.  The spacetime recurrence
$K_{3p/2}^E\le(K_p^E)^{1/2}(K_{2p}^E)^{1/2}$ with Sobolev
$K_{2p}^E=\|z_p\|_4^4$ then yields:
\[
  \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}.
  \tag{5.5}
\]

**5f. Metric drift.**
\[
  d(T)=\int_0^T\|aE\|_\infty\,ds
  \le C\delta\int_0^T(r^2/s)^{1/3}\,ds
  =C'\delta\theta^{2/3}r^2.
  \tag{5.6}
\]
Choosing $\delta\le\delta_0$ with $C'\delta_0\theta^{2/3}r^2<d_0$ ensures
$d(T)<d_0$ and hence bilipschitz comparison $|g(t)/g(0)-\mathrm{Id}|\le
\psi(d_0)$.  This keeps the Sobolev constants comparable to initial values.

**5g. Global $Q$.**
The homogeneous defect equation and disjoint-support absorption (on the
exact $\varepsilon=0$ flow where the exterior is stationary) give
\[
  Q(T)\le e^{C\theta}Q(0)\le C_1\delta^2\operatorname{Vol}(M).
  \tag{5.7}
\]
The disjoint supports ensure that the curvature potential in the $Q$
estimate is summed over disjoint domains, avoiding a factor equal to the
number of supports.

**5h. Self-improving closure.**
With $d_0$ small, the moving Sobolev constants satisfy
$\mathcal S_\alpha(t)\le e^{Cd_0}\mathcal S_\alpha(0)$, comparable to
initial values.  The Grönwall estimate (5.1) with $\theta$ chosen in 5a
gives $K_2(T)\le(3/2)K_2(0)<2K_2(0)$.  The drift estimate (5.6) with
$\delta\le\delta_0$ gives $d(T)<d_0$.  Hence $\tau\ge T=\theta r^2$ and
both first-exit conditions hold strictly throughout $[0,T]$.
Hence $\tau\ge T=\theta r^2$.

---

## 6. Higher-derivative continuation (Module S, Part 4)

On the bootstrap interval $[0,T]$, $|U|\le K:=C\gamma/(\theta r^2)^{1/2}$
(from the curvature Moser endpoint).  The shifted curvature is
\[
  T=\operatorname{Rm}+G,\quad G=\frac{g\wedge g}{6},\quad U=aT.
\]

**Staggered ordering** (Step 40 mechanism, Step 45 ledger).
\[
  T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to T_2\to\cdots
\]
At each level $m$: test the $T_m=\nabla^mT$ equation with $|T_m|^{p-2}T_m$
to get finite $L^p$.  Then test the $U_m=\nabla^mU$ equation with $|U_m|^{p-2}U_m$;
the hardest term $\chi C_{m+2}$ is reduced by one integration by parts
(signed Hessian lemma, Step 38) to current-level quantities.  Key identities:
- $|db|^2/b\le4|d\chi|^2$ (exact, all $\varepsilon$);
- $db*db*T_m=4(\chi^2/b)d\chi*d\chi*[U_m-\text{lower}]$ (bounded coefficient);
- Spatial commutators use $b\operatorname{Rm}=U-bG$ (no pointwise $T$);
- Time commutators use $\partial_t\Gamma=-g^{-1}*\nabla\operatorname{Ric}(U)$.

Constants at each level are per-datum (may depend on $K$ and cutoff jets)
but finite on any smooth finite slab.  The $\varepsilon$-uniform geometric
bounds supply a common time for all $\varepsilon>0$, and the smooth
$\varepsilon\to0$ limit inherits all finite-order $L^p$ bounds.

**Continuation criterion.**  If $|U|$ remains bounded on $[0,T^*)$, then
all derivatives are bounded and the flow extends past $T^*$.  Combined
with the first-exit bootstrap, the flow reaches $T=\theta r^2$ with
controlled $|U|$ and all derivatives.

**References:** `step45_coordinate_tensor_ledger_and_regularized_closure.md`;
`step40_m2_coupled_continuation_mechanism.md`;
A01 `step43_H_WU_resolution_weighted_evolution.md` (54/54 checks);
`step44_zero_order_T_seed_repair.md`.

---

## 7. Terminal spectral contradiction (Module O, Part 2)

**7a. Terminal density** (Step 43).
The nonneg pointwise density is
\[
  \mathfrak D=|E|^2+(s+4)^2+(s+8\sqrt6|W^+|)^2+G,
  \qquad
  G=f^2-(b_-)^2\ge0.
  \tag{7.1}
\]
For any smooth metric on any manifold in the IL geography with $q\ge0$:
\[
  \int\mathfrak D\le119Q.
  \tag{7.2}
\]
The coefficient decomposes as $1+4+108+6$: the four summands are bounded
by $Q$, $4Q$, $108Q$, and $6Q$ respectively.  Every step uses only
Chern–Weil, SW monopole, and LeBrun spectral lower bound (applicable to
any smooth metric, including the evolved $g(T)$).

**7b. Core-ball selection and uniform $\mathfrak D\to0$.**
At time $T=\theta r^2$, the *core balls*
$\Omega_\alpha=B_r^{g(0)}(x_\alpha)\subset\{a=1\}$ satisfy:
- Disjoint with total $g(0)$-volume $\ge\alpha_0\operatorname{Vol}$
  (Step 3b);
- Bilipschitz to $g(T)$-balls: $e^{-4d_0}\operatorname{Vol}_{g(0)}\le
  \operatorname{Vol}_{g(T)}\le e^{4d_0}\operatorname{Vol}_{g(0)}$
  (from $d(T)<d_0$);
- Each core lies strictly inside the $a=1$ plateau, with a buffer of
  radius $\ge3r$ to the support boundary;
- $|\nabla^k\operatorname{Rm}(x,T)|\le C_k$ on the plateau
  (Shi estimates on $[T/2,T]$ after converting the normalized flow to
  ordinary Ricci flow on $\{a=1\}$).

By (7.2) and (5.7):
\[
  \sum_\alpha\int_{\Omega_\alpha}\mathfrak D(T)
  \le\int_M\mathfrak D\le119Q(T)\le C_2\delta^2\operatorname{Vol}.
  \tag{7.3}
\]
Since $\sum_\alpha\operatorname{Vol}_{g(T)}\Omega_\alpha\ge
e^{-4d_0}\alpha_0\operatorname{Vol}$, at least one core $\Omega_*$ has
\[
  \fint_{\Omega_*}\mathfrak D(T)\le\frac{C_2}{e^{-4d_0}\alpha_0}\delta^2
  =:C_3\delta^2.
  \tag{7.4}
\]

The Shi estimates give $|\nabla\mathfrak D|\le L$ uniformly on the plateau
(the ordered Weyl eigenvalues are Lipschitz in the curvature endomorphism,
and $b\mapsto(\min\{b,0\})^2$ is $C^1$, so $\mathfrak D$ is Lipschitz
with a uniform constant $L$ depending on $C_k$).

If $m=\sup_{\Omega_*^{\rm inner}}\mathfrak D$ with $\Omega_*^{\rm inner}
=B_{r/2}^{g(T)}(x_*)$, then $\mathfrak D\ge m/2$ on a ball of $g(T)$-radius
$\rho=\min\{r/4,m/(2L)\}$ around the supremum point.  Bishop–Gromov
(under $\operatorname{Ric}_{g(T)}\ge-3-\varepsilon$) gives
\[
  \operatorname{Vol}B_\rho\ge c_4\left(\frac\rho r\right)^4\operatorname{Vol}\Omega_*,
\]
without noncollapse.  Combining with (7.4):
\[
  C_3\delta^2\ge\frac{m}{2}\cdot
  c_4\left(\frac{\min\{r/4,m/(2L)\}}{r}\right)^4.
  \tag{7.5}
\]
In the small-$m$ regime ($m/(2L)<r/4$):
$C_3\delta^2\ge c_5\,m^5/(L^4r^4)$, so $m\le C_6\delta^{2/5}$.
In both regimes, $m\to0$ as $\delta\to0$.  Hence
\[
  \sup_{\Omega_*^{\rm inner}}\mathfrak D(T)\to0
  \qquad\text{uniformly.}
  \tag{7.6}
\]

**7c. Limit extraction.**
Pick $x_i=x_{*,i}\in\Omega_{*,i}^{\rm inner}$ (the centers of the selected
core balls along the sequence).  Pull back $g_i(T_i)$ to
$B_R(0)\subset T_{x_i}M_i$ via $\exp_{x_i}$, with $R<\min\{r/4,\pi/(2\sqrt K)\}$.
The pullback metrics $\tilde g_i$ satisfy uniform $C^k$ bounds (from Shi)
and noncollapsed volume $\operatorname{Vol}_{\tilde g_i}(B_R)\ge c_1R^4$
(from Rauch comparison under bounded sectional curvature).  By
Arzelà–Ascoli, a subsequence converges $C^\infty$-locally to a smooth
limit metric $h$ on $B_R(0)\subset\mathbb R^4$.

The limit satisfies:
- $\operatorname{Ric}_h=-h$ (from $|E_i|\to0$ in $C^k$, as $a=1$ on
  the core);
- $\mathfrak D_h\equiv0$ on $B_R$ (from (7.6): uniform
  $\sup\mathfrak D\to0$ on $\Omega_*^{\rm inner}$, and the pullback image
  lies inside $\Omega_*^{\rm inner}$ by choice of $R$).

**7d. Spectral determination on the entire ball** (Step 43 Lemma 1.2).
At *every* point $y\in(B_R,h)$: $E_h=0$ gives $s_h=-4$.
$\mathfrak D_h(y)=0$ gives $(s_h+8\sqrt6|W_h^+|)^2=0$, hence
$|W_h^+|(y)=1/(2\sqrt6)$ and $|W_h^+|^2(y)=1/24$.
Also $G_h(y)=0$.  Since $f=-3$ and $\xi=w+|W^+|\sqrt{2/3}\in[0,1/6]$,
$G=4\xi(3-\xi)=0$ forces $\xi=0$, hence $w(y)=-1/6$ and
\[
  \operatorname{Spec}(W_h^+)\equiv
  \left(-\frac{1}{6},\frac{1}{12},\frac{1}{12}\right)
  \qquad\text{on }B_R.
  \tag{7.7}
\]

**7e. Derdziński/projector–Bochner contradiction** (Step 6).
On the Einstein manifold $(B_R,h)$ with $\operatorname{Ric}_h=-h$ and
the *constant* calibrated Weyl spectrum (7.7):

1. The eigenvalue $-1/6$ is simple with a double eigenvalue $1/12$,
   and both are *constant* on $B_R$ (from (7.7), not from continuity
   at one point).

2. On any Einstein 4-manifold, $\delta W^+=0$.  When the simple eigenvalue
   is constant, the projector lemma forces the simple eigenform $\omega$
   to satisfy $\nabla\omega=0$ (Step 6: contract the divergence-free
   condition with the nondegenerate $\omega$ to get
   $\omega_{ab}\nabla^a\omega_{cd}=0$, then use
   $\omega_a{}^c\omega_c{}^b=-\delta_a{}^b$ to conclude $\nabla\omega=0$).

3. Hence $\nabla W^+=0$ on $B_R$.  Then $|W^+|^2=1/24$ is constant, so
   $\Delta|W^+|^2=0$.  The Einstein–Weyl identity
   \[
     \Delta|W^+|^2=2|\nabla W^+|^2+s|W^+|^2-36\det W^+
   \]
   at $s=-4$, $|W^+|^2=1/24$, $\det W^+=(-1/6)(1/12)^2=-1/864$ gives:
   \[
     0=0+(-4)\!\cdot\!\tfrac{1}{24}-36\!\cdot\!(-\tfrac{1}{864})
     =-\tfrac{1}{6}+\tfrac{1}{24}=-\tfrac{1}{8}\ne0.
   \]
   **Pointwise contradiction.**

---

## 8. Proof assembly

Assume for contradiction a sequence $(M_i,g_i)$ in the IL geography with
$q_i\ge0$ and $\delta_i\to0$.

- §2 produces the calibrated profile and budget $\Lambda=O(1)$.
- §3 constructs supports with collapse-independent $\gamma\le C'r^2$.
- §4 produces a smooth exact degenerate flow on each $(M_i,g_i)$.
- §5 runs the first-exit bootstrap to $T=\theta r^2$ for all large $i$.
- §6 ensures smooth continuation throughout $[0,T]$.
- §7a–7c: core-ball selection gives $\sup_{\Omega_*^{\rm inner}}\mathfrak D
  \le C_6\delta_i^{2/5}\to0$, and the limit has $\mathfrak D_h\equiv0$ on
  $B_R$.
- §7d: spectral determination forces the *constant* calibrated Weyl spectrum
  on the entire ball.
- §7e: the projector–Bochner contradiction eliminates the limit.

No escaping sequence exists.  Hence $\delta_0(M)>0$ for every $M$ in the
geography.  Family uniformity for bounded $A$ follows because all constants
depend on $A_{\max}$ and geography-uniform ratios.  $\square$

---

## 9. Scope, dependencies, and next research

**What this proves.**  A lower bound $\delta_0>0$ on $\|g^{-1}(\operatorname{Ric}+g)\|_\infty$
for every Riemannian metric on every manifold in the $q\ge0$ Ishida–LeBrun
no-Einstein geography in dimension 4 (negative normalization).

**What this does not prove.**
- The positive ($\Lambda>0$) normalized branch of Yau Problem 26.
- Any result in dimensions $n\ge5$.
- Dimension-only constants $c_n<C_n$ covering both signs.
- A Lean 4 formalization.
- The full original statement of Yau Problem 26.

**Reusable Module S.**  The smoothing module (§§3–6) depends only on
$\operatorname{Ric}\ge-3g$ and the curvature-to-volume budget $\Lambda$.
It produces bounded-curvature terminal charts with pointwise $|E|\to0$ on
any closed 4-manifold satisfying these inputs.  A new no-Einstein
obstruction is consequential if it supplies a genuinely different spectral
density controlled by $Q$, or if it exposes a limitation of the
chart-extraction mechanism.

**Source files.**

| Component | Source |
|-----------|--------|
| Calibration | `step3_boundary_near_saturation.tex`, `step15_whole_support_moser_and_normalization_repair.md` |
| Support | `step29_terminal_density_bridge_lemma.md` (A01 `step29_simultaneous_support_theorem.md`) |
| $J_6$ seed | `step35_unregularized_J6_persistence_lemma.md` |
| All-$p$ defect | `step39_general_p_defect_power_inequality.md` |
| Hessian IBP | `step38_hessian_ibp_and_conditional_moser_repair.md` |
| Global $Q$ | `step37_global_Q_persistence.md` |
| Continuation | `step40_m2_coupled_continuation_mechanism.md`, `step45_coordinate_tensor_ledger_and_regularized_closure.md` |
| Zero-order $T$ | `step44_zero_order_T_seed_repair.md` |
| Weighted $U_m$ | A01 `step43_H_WU_resolution_weighted_evolution.md` |
| Existence | `step45_coordinate_tensor_ledger_and_regularized_closure.md` §7, A01 `step43_H_DT_assessment.md` |
| Terminal density | `step43_terminal_density_G_lemma.md` |
| Projector | `step6_local_projector_obstruction_and_collapse_reduction.tex` |
| Terminal geometry | A01 `step28_terminal_recalibration_pullback.md`, A01 `step42_uniform_gap_weight_terminal_repairs.md` |
| Curvature Moser | A01 `step34_integrated_potential_q3_and_defect.md` |
| Shi | standard, via `step43_corrected_negative_IL_theorem.md` §4 |
| LeBrun spectral | `Knowledge/.../Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory...object.md` lines 195–225 |
| Verification | `verify_step43_terminal_density.py` (26/26), `verify_step45_weight_partitions.py` (110/110) |
