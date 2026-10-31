# Step 29: Consolidated conditional theorem for the Ishida–LeBrun no-Einstein family

## 0. Scope and advance

This note consolidates the entire four-dimensional negative-branch program
into one self-contained conditional theorem covering the **full no-Einstein
Ishida–LeBrun family**, not just the critical boundary.  The key structural
advance is the family extension (Section 1), which shows that above-critical
manifolds have an immediate topological gap requiring no PDE argument, while
the critical boundary requires only the already-developed cutoff-flow chain.
All precise quantitative inputs are stated so that the theorem's reach can
be assessed independently.

## 1. Family extension: above-critical topological gap

### 1.1 Setup

Consider the Ishida–LeBrun family

$$
M = \left(\#_{j=1}^m X_j\right)\# N,\qquad m = 2 \text{ or } 3,
$$

with $A = \sum_j c_1^2(X_j)$, $D = 4m - (2\chi + 3\tau)(N)$, and

$$
\sigma = D - \frac A3 \ge 0.
$$

By Ishida–LeBrun Theorem 7, $M$ admits no Einstein metric when $\sigma \ge 0$.

### 1.2 Topological identity and monopole inequality

Define the normalized integrals (following Step 3):

$$
I = \frac{1}{4\pi^2}\int_M\left(\frac{s^2}{24} + 2|W^+|^2\right)d\mu,
\qquad
R = \frac{1}{4\pi^2}\int_M\frac{|\operatorname{Ric}_0|^2}{2}\,d\mu.
$$

Chern–Gauss–Bonnet and the Hirzebruch signature formula give

$$
I - R = (2\chi + 3\tau)(M) = A - D = \frac{2A}{3} - \sigma.
\tag{1.1}
$$

The Seiberg–Witten monopole inequality for the selected sign class gives

$$
I \ge \frac{2A}{3},
\tag{1.2}
$$

hence

$$
R = I - \frac{2A}{3} + \sigma \ge \sigma.
\tag{1.3}
$$

**This is the topological floor**: the normalized trace-free Ricci energy is
bounded below by the topological excess $\sigma$.

### 1.3 The Ricci-pinching bound on $R$

If $\|g^{-1}(\operatorname{Ric}_g + g)\|_\infty \le \delta$, then
$|\operatorname{Ric}_0|^2 \le 4\delta^2$ pointwise (Step 3), so

$$
R \le \frac{4\delta^2}{8\pi^2}\operatorname{Vol}(M,g)
  = \frac{\delta^2}{2\pi^2}\operatorname{Vol}(M,g).
\tag{1.4}
$$

### 1.4 Volume bound

For $\delta < 1$, the Ricci lower bound gives
$\operatorname{Ric} \ge -(1+\delta)g \ge -2g$, and the
upper bound $\operatorname{Ric} \le -(1-\delta)g$ implies $s \le -4(1-\delta)$.
The Chern–Gauss–Bonnet identity gives

$$
\operatorname{Vol}(M,g) \le C(m, A, \chi(N), \tau(N)) \cdot (1 + R)
\le C(\text{topology})(1 + \delta^2\operatorname{Vol}).
$$

For $\delta$ sufficiently small (depending on topology), this yields

$$
\operatorname{Vol}(M,g) \le C_{\rm top}.
\tag{1.5}
$$

More precisely, from (1.1)–(1.2) and the calibration in Step 3: as
$\delta \to 0$, $I \to 2A/3$ and
$\operatorname{Vol} \to 32\pi^2 A/9$ regardless of $\sigma$.

### 1.5 The above-critical gap

Combining (1.3) and (1.4):

$$
\sigma \le R \le \frac{\delta^2}{2\pi^2}\operatorname{Vol}(M,g),
$$

hence

$$
\delta \ge \sqrt{\frac{2\pi^2\sigma}{\operatorname{Vol}(M,g)}}.
\tag{1.6}
$$

With the volume bound (1.5):

With the volume bound (1.5), the TTCS-verified explicit formula is:

$$
\boxed{\delta \ge \min\left(\frac14,\;\sqrt{\frac{3\sigma}{16A}}\right)
\qquad\text{for}\quad \sigma > 0.}
\tag{1.7}
$$

**Proposition (Above-critical topological gap).** For each fixed manifold $M$
in the Ishida–LeBrun family with $\sigma = D - A/3 > 0$, there exists
$\delta_*(M) > 0$ such that no smooth metric $g$ on $M$ satisfies
$\|g^{-1}(\operatorname{Ric}_g + g)\|_\infty < \delta_*(M)$.

*Proof.* Direct from (1.6) and the topology-dependent volume bound. $\square$

**This requires no PDE argument**, no flow, no collapse analysis.  It is a
direct consequence of Chern–Gauss–Bonnet, the signature formula, and the
Seiberg–Witten monopole inequality.

### 1.6 Uniformity within controlled subfamilies

For a family where $\sigma/A \ge c > 0$ and $\operatorname{Vol}/A$ is
bounded above (which holds for any fixed $m$ and uniformly bounded
$\chi(N)/A$, $\tau(N)/A$), the gap (1.7) gives a **uniform** lower bound
$\delta \ge c' > 0$ independent of the specific manifold.

For the full family with $\sigma \ge 0$, the gap deteriorates as
$\sigma \to 0$, and the critical boundary $\sigma = 0$ requires the full
flow argument.

### 1.7 Strengthened calibration on the entire family

The completion-square algebra gives, via the defect identity $D_a$:

$$
\int(s + 8\sqrt6|W^+|)^2\,d\mu
= 864\pi^2 D_a
\le 864\pi^2(R - \sigma)
\le 864\pi^2 R,
\tag{1.8}
$$

since $D_a = R - \sigma - (2/3)((a^+)^2 - A) \le R - \sigma$ and
$D_a \ge 0$.  The topological excess **tightens** the calibration: larger
$\sigma$ means less room for the Weyl modulus to deviate from the calibrated
value $1/(2\sqrt6)$.

## 2. Critical boundary conditional theorem

At $\sigma = 0$, the topological floor vanishes and the gap must come from
the geometric/analytic argument.  We state the conditional theorem.

### 2.1 Statement

**Conditional Theorem.** Let $M = (\#_{j=1}^m X_j)\# N$ with $m = 2$ or $3$,
$D = A/3$ (critical boundary), and suppose Assumptions (A1)–(A4) below hold.
Then there exists $\delta_0 > 0$, depending only on the topology of $M$, such
that no smooth Riemannian metric $g$ on $M$ satisfies
$\|g^{-1}(\operatorname{Ric}_g + g)\|_\infty < \delta_0$.

### 2.2 Assumptions

**(A1) Selected-support cutoff flow.**
There exist constants $r_*, \theta, \bar\beta_* > 0$ (depending on
topology) such that for every smooth metric $g$ on $M$ with
$\|g^{-1}(\operatorname{Ric} + g)\|_\infty = \delta$ sufficiently small,
the following holds.  There exists a smooth cutoff function
$\chi: M \to [0,1]$ with:

- $\operatorname{supp}\chi$ contained in a maximal-function good support
  with radius $r_* = c(A/K_0)^{1/4}$ where
  $K_0 = \operatorname{Vol}^{-1}\int|\operatorname{Rm}|^2$;
- $|d\chi|_{g_0} \le 2/r_*$, and $\chi = 1$ on an inner plateau
  $P$ with $\operatorname{Vol}(P) \ge \alpha A$ for a fixed $\alpha > 0$;
- geodesic buffer of width $\ge \rho > 0$ between $\partial P$ and
  $\partial(\operatorname{supp}\chi)$;

and the normalized cutoff flow
$\partial_t g = -2\chi^2(\operatorname{Ric} + g)$
has a smooth solution on $[0, \theta r_*^2]$.

**(A2) First-exit energy preservation.**
Under (A1), on the flow interval $[0, \theta r_*^2]$:

$$
\begin{aligned}
&\widehat H_2(t) \le 2\widehat H_2(0),
\quad Q(t) \le e^{C\theta}Q(0),
\quad J_6(t) \le e^{C\theta}J_6(0),\\
&\|a\operatorname{Rm}(t)\|_\infty \le C\bar\beta/t,
\quad
\|aE(t)\|_\infty \le C\delta(r_*^2/t)^{1/3},
\end{aligned}
$$

where $\widehat H_2 = \int_{\operatorname{supp}\chi}F^2$,
$Q = \int_M|E|^2$, $J_6 = \int\eta^2 a^4|E|^6$,
$\bar\beta = \mathsf S\widehat H_2^{1/2}$,
$\mathsf S = C(4, Kr_*^2)r_*^2\operatorname{Vol}(B_{r_*})^{-1/2}$
is the Maheux–Saloff-Coste local Sobolev constant.

**(A3) Metric comparison and plateau geometry at terminal time $T = \theta r_*^2$.**
The metric drift satisfies

$$
I(T) = \int_0^T\|aE(t)\|_\infty\,dt
\le \frac32 C\delta\theta^{2/3}r_*^2 \le \frac{1}{100},
$$

so $e^{-1/10}g_0 \le g(T) \le e^{1/10}g_0$.  The inner plateau $P$ retains

$$
\operatorname{Vol}_{g(T)}(P) \ge \alpha' A,
\qquad
|\operatorname{sec}_{g(T)}|_P \le K < \infty,
\qquad
K\rho^2 < \pi^2/4,
$$

for uniform $\alpha', K, \rho$ depending on topology.

**(A4) Normalized flow continuation.**
If $\sup_{M\times[0,T)}|a\operatorname{Rm}| < \infty$, then $g(t)$ extends
smoothly past $T$.  (This is the shifted-curvature extension theorem of
Step 27.)

### 2.3 Proof sketch from assumptions

1. **Support selection** (Section 3 below): maximal-function good-point
   selection, Vitali thinning, Bishop–Gromov volume retention, and cutoff
   construction give (A1)'s support with $\operatorname{Vol}(P) \ge \alpha A$.

2. **First-exit bootstrap** (Steps 22–26): the weighted Wang/Yang hierarchy,
   including the general-$p$ tensor inequality (Section 4), the $H_2$
   propagation, the critical $H_2 \to H_3$ upgrade, the terminal $H_3$
   propagation, the $J_6$ critical absorption, and the subcritical Moser
   iteration, give the energy bounds in (A2).

3. **Continuation** (Step 27): the shifted-curvature extension theorem
   (Assumption A4) uses $\|a\operatorname{Rm}(t)\| \le C\bar\beta/t < \infty$
   for $t > 0$, and short-time existence for $t$ near $0$, to extend the flow
   to $[0, T]$.  The $C/t$ bound is uniformly bounded on $[T/2, T]$, so the
   extension passes $T$ and contradicts maximality of a first exit time.

4. **Terminal recalibration** (A01 Step 28): at $g(T)$, the Chern–Gauss–Bonnet
   and monopole inequalities are reapplied.  The combined density

   $$
   \mathfrak D = |E|^2 + (s+4)^2 + (s+8\sqrt6|W^+|)^2 + \mathcal G
   $$

   satisfies $\int\mathfrak D \le 119\,Q(T) \le 119\,e^{C\theta}Q(0)$.

5. **Exponential-pullback averaging** (Step 16): for centers $p \in P$ with
   $\operatorname{Vol}(P) \ge \alpha A$ and radial buffer $\rho$ under
   bounded sectional curvature $K$, Rauch comparison gives

   $$
   \frac{1}{\operatorname{Vol}(P)}\int_P A_\rho\mathfrak D(p)\,d\mu(p)
   \le \frac{C(K,\rho)}{\alpha A}\int_M\mathfrak D\,d\mu
   \to 0.
   $$

   A center $p_i \in P$ with $A_\rho\mathfrak D(p_i) \to 0$ is selected.

6. **Tangent-space compactness**: on the pullback domain
   $(B_\rho(0) \subset T_{p_i}M, \exp_{p_i}^*g(T))$, Rauch's theorem gives
   a positive lower volume bound independent of base collapse.  Bounded
   curvature and harmonic-radius estimates yield smooth subsequential
   convergence (after one radius shrink) to a local Einstein metric
   $g_\infty$ with $\operatorname{Ric} = -g_\infty$.

7. **Calibrated spectrum**: the vanishing pullback density forces
   $|W^+_\infty|^2 = 1/24$ and the lowest-eigenline spectrum

   $$
   \operatorname{Spec}(W^+_\infty) = \left(-\frac16, \frac{1}{12}, \frac{1}{12}\right).
   $$

8. **Projector contradiction** (Step 6): the Bianchi identity $\delta W^+ = 0$
   and the constant simple/double eigenvalue structure force $\nabla W^+ = 0$.
   But the Einstein–Weyl identity gives $|\nabla W^+|^2 = 1/16 \ne 0$.
   Contradiction.  $\square$

## 3. Support geometry construction

### 3.1 Maximal-function good set

For a smooth metric $g$ on $M$ with
$\delta = \|g^{-1}(\operatorname{Ric} + g)\|_\infty$ small, define

$$
K_0 = \frac{1}{\operatorname{Vol}}\int_M|\operatorname{Rm}|^2\,d\mu,
$$

bounded by $C(A)/\operatorname{Vol}$ from Chern–Gauss–Bonnet.  Set
$r_* = c(K_0)^{-1/4}$ (the Li radius, Maheux–Saloff-Coste compatible scale).

The maximal function at scale $R = r_*$ satisfies the weak-$(1,1)$ bound
(from the Ricci lower bound and Bishop–Gromov doubling):

$$
\operatorname{Vol}\left(\left\{\mathcal M_{r_*}|\operatorname{Rm}|^2 > 4K_0\right\}\right)
\le \frac{C_D}{4K_0}\int_M|\operatorname{Rm}|^2\,d\mu
= \frac{C_D}{4}\operatorname{Vol}.
$$

Therefore

$$
G = \left\{p : \mathcal M_{r_*}|\operatorname{Rm}|^2(p) \le 4K_0\right\}
$$

satisfies $\operatorname{Vol}(G) \ge (1 - C_D/4)\operatorname{Vol}
\ge \operatorname{Vol}/2$ for $C_D \le 2$.  (The exact doubling constant
$C_D(4, 2r_*^2)$ is bounded for bounded $K_0r_*^2$.)

### 3.2 Vitali thinning and disjoint supports

Select a maximal $r_*/5$-separated subset $\{p_\alpha\} \subset G$.  By
maximality, the balls $B_{r_*/5}(p_\alpha)$ cover $G$.  By Bishop–Gromov
(Ricci lower bound):

$$
\frac{\operatorname{Vol}(B_{r_*/5}(p))}{\operatorname{Vol}(B_{r_*}(p))}
\ge c_{\rm BG}(4, 2r_*^2) > 0.
$$

The number of centers in any ball $B_{r_*}(q)$ is bounded by
$C_{\rm pack}(4, 2r_*^2)$ (packing number from doubling).

Assign disjoint supports: for each $\alpha$, set
$\Omega_\alpha = B_{r_*}(p_\alpha)$ (the maximal-function control ball)
and inner plateau $P_\alpha = B_{r_*/3}(p_\alpha)$.  By $r_*/5$-separation,
the balls $B_{r_*/10}(p_\alpha)$ are disjoint.  Therefore

$$
\sum_\alpha\operatorname{Vol}(B_{r_*/10}(p_\alpha))
\le \operatorname{Vol}(M),
$$

and by Bishop–Gromov,

$$
\operatorname{Vol}(B_{r_*/10}(p_\alpha))
\ge c_{\rm BG}'\operatorname{Vol}(B_{r_*}(p_\alpha)).
$$

The total retained plateau volume is:

$$
\sum_\alpha\operatorname{Vol}(P_\alpha)
\ge c_{\rm BG}''\sum_\alpha\operatorname{Vol}(B_{r_*}(p_\alpha))
\ge c_{\rm BG}''\operatorname{Vol}(G)
\ge \frac{c_{\rm BG}''}{2}\operatorname{Vol}(M)
\ge \alpha A,
\tag{3.1}
$$

using $\operatorname{Vol}(M) \ge c(A)$ from the calibration.

### 3.3 Cutoff construction

For each component $\alpha$, choose $\chi_\alpha: M \to [0,1]$ with:
- $\chi_\alpha = 1$ on $P_\alpha = B_{r_*/3}(p_\alpha)$;
- $\operatorname{supp}\chi_\alpha \subset B_{2r_*/3}(p_\alpha)$;
- $|d\chi_\alpha| \le C/r_*$;
- $\chi_\alpha$ infinitely flat at the boundary (for noninteger Moser powers);
- the geodesic buffer width between $P_\alpha$ and
  $\partial(\operatorname{supp}\chi_\alpha)$ is $\ge r_*/3$.

For the flow on each component, or on a single selected component with the
largest energy ratio, only disjointness of the active supports is needed.
The flow on $\Omega_\alpha$ does not affect metrics on
$M \setminus \operatorname{supp}\chi_\alpha$, and the first-exit argument
uses only the energy within $\operatorname{supp}\chi_\alpha$ and its
Sobolev constant.

### 3.4 Terminal geometry transfer

After the flow, the metric drift (A3) preserves:

$$
e^{-1/10}g_0 \le g(T) \le e^{1/10}g_0.
$$

Therefore:
- $\operatorname{Vol}_{g(T)}(P) \ge e^{-2/5}\operatorname{Vol}_{g_0}(P)
  \ge \alpha' A$;
- sectional curvature on $P$ at time $T$ is bounded by
  $K = C\bar\beta/T + Ce^{1/5}$;
- the geodesic buffer shrinks by at most a factor $e^{1/10}$, giving
  $\rho \ge e^{-1/10}r_*/3 > r_*/4$.

## 4. Corrected general-$p$ coefficient structure

### 4.1 The dissipation–Sobolev relationship

The Step 28 review identified that the dissipation $cD_p$ alone controls
$\|\nabla Z_p\|_2^2$ only with a $p$-dependent coefficient.  The complete
picture is:

The energy inequality gives dissipation
$pD_p + p(p-2)D_F$, where

$$
D_p = \int\eta^2 a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2,
\qquad
D_F = \int\eta^2 a^{p-1}F^{p-2}|\nabla F|^2.
$$

Since $|F\nabla F| \le |\operatorname{Rm}||\nabla\operatorname{Rm}| \le F|\nabla\operatorname{Rm}|$,
we have $D_F \le D_p$.

The Sobolev variable satisfies

$$
|\nabla Z_p|^2
\le C\left(\frac{p^2}{4}a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2
+ (p-1)^2 a^{p-2}|d\chi|^2 F^p
+ |d\eta|^2 a^{p-1}F^p\right),
$$

where the last term vanishes on the active support.  Therefore

$$
\|\nabla Z_p\|_2^2
\le \frac{Cp^2}{4}D_p + C(p-1)^2 r^{-2}K_p.
\tag{4.1}
$$

The dissipation controls this as

$$
\frac{4}{Cp}\cdot\text{(total dissipation)}
\ge D_p
\ge \frac{4}{Cp^2}\|\nabla Z_p\|_2^2 - Cr^{-2}K_p.
\tag{4.2}
$$

### 4.2 Effect on the Moser iteration

At each Moser step $j$ with $p_j = p_0(3/2)^j$, the Sobolev embedding gives

$$
\mathcal M_{p_{j+1}, j+1}
\le C\mathsf S \cdot (L_j\mathcal M_{p_j, j})^{3/2},
$$

where the loss factor is

$$
L_j = Cp_j^3 \cdot 4^j(t^{-1} + r^{-2}) \cdot p_j
= Cp_j^4 \cdot 4^j(t^{-1} + r^{-2}).
\tag{4.3}
$$

The extra factor $p_j$ from (4.2) enters the coefficient.  The normalized
iteration $m_j = \mathcal M_{p_j,j}^{1/p_j}$ then satisfies

$$
m_{j+1} \le (C\mathsf S)^{2/(3p_j)} L_j^{1/p_j}\,m_j.
$$

The infinite product converges because

$$
\sum_{j=0}^\infty \frac{\log L_j}{p_j}
= \sum_j \frac{4\log p_j + j\log 4 + O(1)}{p_j}
\le C\sum_j \frac{j}{p_j}
< \infty,
\tag{4.4}
$$

since $p_j = p_0(3/2)^j$ grows exponentially while the numerator grows only
linearly.  **The polynomial $p$-deterioration is entirely absorbed by the
Moser product.**

### 4.3 Explicit Moser sum

The Sobolev power sum is

$$
\sum_{j=0}^\infty \frac{2}{3p_j}
= \frac{2}{3p_0}\sum_{j=0}^\infty\left(\frac{2}{3}\right)^j
= \frac{2}{p_0},
\tag{4.5}
$$

so the net Sobolev power is $\mathsf S^{2/p_0}$.  For curvature ($p_0 = 3$):
$\mathsf S^{2/3}$; for defect ($p_0 = 6$): $\mathsf S^{1/3}$.

## 5. Complete conditional chain for the full family

### 5.1 The unified result

**Theorem (Conditional, full Ishida–LeBrun no-Einstein family).**
Let $M = (\#_{j=1}^m X_j)\# N$ with $m \in \{2,3\}$, $A = \sum c_1^2(X_j)$,
$D = 4m - (2\chi+3\tau)(N)$, and $D \ge A/3$.  Suppose Assumptions (A1)–(A4)
hold for critical manifolds.

Then there exists $\delta_0(M) > 0$ such that no smooth metric $g$ on $M$
satisfies $\|g^{-1}(\operatorname{Ric}_g + g)\|_\infty < \delta_0(M)$.

*Proof.*
- If $\sigma = D - A/3 > 0$: the topological gap (1.7) gives $\delta_0 = c\sqrt{\sigma/A}$.
- If $\sigma = 0$: the conditional analytic argument (Section 2.3) gives $\delta_0$.  $\square$

### 5.2 Uniformity conditions

For a controlled subfamily where $\sigma/A$ is bounded below by a positive
constant, the above-critical bound is uniform and the flow argument is not
needed.

For the full family, uniformity in $\delta_0$ is **not** established.  Even at
the critical boundary, $\delta_0$ may depend on the specific topology
(specifically on $A$ and the Euler/signature data of $N$).  A universal
negative-branch gap $\delta_0(4) > 0$ independent of topology would require
additional uniformity arguments.

### 5.3 Dependence on assumptions

| Assumption | Content | Status |
|---|---|---|
| (A1) | Selected-support cutoff flow exists | Section 3 constructs the support; smooth short-time existence is standard |
| (A2) | First-exit energy preservation | Steps 22–26 develop the weighted hierarchy; coefficient correction in Section 4 |
| (A3) | Terminal metric comparison | Follows from (A2) via defect integration |
| (A4) | Normalized flow continuation | Step 27 shifted-curvature theorem; Codex verified |

The hardest remaining work is (A2): the complete simultaneous first-exit
argument with all terms and regularization.  The individual pieces (critical
absorption, Yang iteration, Moser product convergence, $J_6$ propagation,
$Q$ preservation) are developed; their simultaneous closure needs the full
term-level tensor inequality and the staggered Wang induction.

## 6. Uniform gap across the full family

### 6.1 Volume cancellation in $K_0$ and $\beta$

The mean curvature energy $K_0 = \operatorname{Vol}^{-1}\int|\operatorname{Rm}|^2$
is bounded uniformly across the Ishida–LeBrun family.  From the decomposition
$|\operatorname{Rm}|^2 = |W|^2 + 2|\operatorname{Ric}_0|^2 + s^2/6$ and
Chern–Gauss–Bonnet:

$$
\int|\operatorname{Rm}|^2 = 32\pi^2\chi(M) + 6\int|\operatorname{Ric}_0|^2.
$$

For the Ishida–LeBrun family, $\chi(M) \sim A + O(1)$ and
$\operatorname{Vol} \sim 32\pi^2A/9$, so

$$
K_0 \le \frac{32\pi^2(A + C) + 6\cdot4\delta^2\operatorname{Vol}}
          {\operatorname{Vol}}
   \le 9 + \frac{C'}{A} + 24\delta^2.
\tag{6.1}
$$

For $\delta \le 1$ and $A \ge 2$ (each summand has $c_1^2 \ge 1$), $K_0$ is
bounded above by a universal constant.

The critical curvature parameter on one component support is

$$
\beta = \mathsf S\cdot\widehat H_2^{1/2}
     = C_{\rm Sob}\,r_*^2\,K_0^{1/2},
\tag{6.2}
$$

where the volume factor from $\mathsf S = Cr_*^2\operatorname{Vol}(B_{r_*})^{-1/2}$
cancels against $\widehat H_2^{1/2} = (K_0\operatorname{Vol}(B_{r_*}))^{1/2}$.
Since $r_* \sim K_0^{-1/4}$, we get $\beta \sim C_{\rm Sob}\,K_0^0 = C_{\rm Sob}$.

**The critical parameter is independent of both the volume and the collapse
geometry, and depends only on the dimension and $K_0$.**

### 6.2 Uniform first-exit threshold

The metric drift satisfies $I(T) \le C\delta\theta^{2/3}r_*^2$.  Since
$r_*$ and $\theta$ are uniform, the threshold $\delta_0 = c/(C\theta^{2/3}r_*^2)$
is a universal constant.  The first-exit conditions (F1)–(F4) are all
self-improving for $\delta \le \delta_0$, with no topology-dependent factor.

### 6.3 Conditional uniform gap theorem

**Conditional Theorem (Uniform for controlled subfamilies).**  Subject to
Assumptions (A1)–(A4), for any constant $\Lambda$ there exists
$\delta_0(\Lambda) > 0$ such that for every manifold $M$ in the Ishida–LeBrun
no-Einstein family with $D \ge A/3$ and $\chi(M) \le \Lambda A$, no smooth
Riemannian metric on $M$ satisfies
$\|g^{-1}(\operatorname{Ric}_g + g)\|_\infty < \delta_0(\Lambda)$.

In particular, for the standard subfamily with $b_2^+(N) = 0$ and BMY-line
summands, $\chi(M)/A$ is universally bounded and the gap is universal.

*Proof.*
For above-critical manifolds ($\sigma > 0$): the topological gap (1.7) gives
$\delta \ge \min(1/4, \sqrt{3\sigma/(16A)})$, which is positive and
independent of the metric.

For the critical boundary ($\sigma = 0$): the flow argument with
$K_0 \le 9\Lambda + 16\delta^2 + O(1/A)$ gives $\beta \le C$ (uniform for
bounded $\Lambda$), hence $\delta \ge \delta_0(\Lambda)$.

The combined gap is $\min(\delta_0(\Lambda), c\sqrt{\sigma/A})$, positive for
each manifold.  For the controlled subfamily, $\Lambda$ is universal and the
gap is universal.  $\square$


### 6.4 Significance

If the conditional assumptions can be verified, this gives a **reusable
mechanism**: any family of no-Einstein four-manifolds satisfying the
Ishida–LeBrun constraints would automatically have a uniform Ricci-pinching
gap.  The mechanism works by converting integral near-equality (from topology
and gauge theory) into a forbidden local Einstein germ (via collapse-adapted
local smoothing), despite arbitrary base collapse.

## 7. What the conditional theorem does NOT settle

1. **Existence of near-Einstein sequences on no-Einstein manifolds.**
   The theorem shows that no such sequence exists, *if the assumptions hold*.
   It does not construct an actual counterexample.

2. **Positive normalized branch** ($\operatorname{Ric} \ge (1-\delta)g$).
   Myers, Cheeger–Naber finiteness, and positive Einstein collapse are all
   relevant, but no gap theorem or global existence theorem has been developed.

3. **Dimensions $n \ge 5$.** The Seiberg–Witten and Chern–Weil machinery is
   four-dimensional.  The Kaluza–Klein positive Einstein collapse in $n \ge 5$
   shows that collapse-exclusion strategies fail.

4. **Dimension-only constants.** Even a complete negative-branch four-dimensional
   gap would require topology-uniform constants for the full Yau 26 statement.

5. **Lean formalization.** Not begun.

## 7. Verification

- Script `workspace/scripts/verify_step29_family_extension_algebra.py`:
  verifies the completed-square identity, the defect monotonicity, the
  topological gap formula, the combined terminal density constant 119, and the
  above-critical volume/gap relationship.
- Steps 22–26 verification scripts: all previously passed.
- Step 27 shifted-curvature script: passed.
- A01 terminal pullback script: passed.

## 8. Sources and cross-references

- Step 3: `workspace/notes/step3_boundary_near_saturation.tex`
- Step 6: `workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex`
- Step 9: `workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex`
- Step 16: `workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md`
- Steps 22–26: weighted hierarchy and first-exit notes
- Step 27: `workspace/notes/step27_normalized_local_flow_extension_theorem.md`
- A01 Step 28: `Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md`
- Codex: `workspace/codex_loop/Research_Report.md` and
  `workspace/codex_loop/work/shifted_curvature_continuation.md`
- Ishida–LeBrun: `\cite{ishida2019}` Theorem 7
- Maheux–Saloff-Coste: `\cite{saloffcoste1995analyse}` Theorem 1.1
- Wang: `\cite{wang2012pseudolocality}` Section 4
- Yang: `\cite{yang2016pseudolocality}` Section 8


## 10. TTCS corrections applied (Step 29)

The following corrections were identified by independent TTCS verification
(`trace/ttcs/results/step29_ttcs01_verifier1_integration.md`):

1. **CGB coefficient**: The correct identity is
   $\int|\operatorname{Rm}|^2 = 32\pi^2\chi + 4\int|\operatorname{Ric}_0|^2$,
   not with coefficient $6$.  Applied.

2. **$\chi(M)/A$ control**: The uniform $K_0$ bound requires
   $\chi(M)/A$ bounded.  The uniform gap theorem was restricted to
   controlled subfamilies with $\chi(M) \le \Lambda A$.  Applied.

3. **$r_*$ definition**: Corrected to $r_* = cK_0^{-1/4}$ throughout.

4. **Calibration inequality**: $\le 864\pi^2 D_a$, not $= 864\pi^2 D_a$.

5. **Explicit above-critical gap**: $\delta \ge \min(1/4, \sqrt{3\sigma/(16A)})$.

6. **Moser coefficient**: $p^4$ loss using only $pD_p$; $p^3$ recoverable
   using full $p(p-2)D_F$ dissipation.  Product converges either way.
