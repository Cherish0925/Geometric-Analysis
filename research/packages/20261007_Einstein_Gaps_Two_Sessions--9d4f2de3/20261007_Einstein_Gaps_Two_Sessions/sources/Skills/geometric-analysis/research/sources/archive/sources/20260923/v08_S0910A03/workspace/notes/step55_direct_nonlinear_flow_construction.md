# Step 55: Direct nonlinear construction of the normalized cutoff flow

> **Step 56 correction.** The direct nonlinear architecture is retained, but Proposition 5.1 and Theorem 9.1 are not established by this version: lines 385–398 use a false high/low derivative split. The repaired tame hierarchy, doubly parabolic approximation, unweighted $H_2$ interface, stationary global-$Q$ remainder, and per-datum-versus-uniform continuation distinction are in `step56_tame_direct_flow_repair.md`. Cite that file rather than this theorem statement.

Session: S0910A03. Agent2 / Constructor. Phase: Execute.

## 0. Summary

The Strategist identified that setting U = V = G in Step 54's synchronized-output
ledger collapses the two-layer iteration (inner coupled solve + outer Xu contraction)
into a single direct nonlinear construction.  For ε > 0, the coupled
metric–transport system is strictly parabolic plus first-order transport, handled
by standard quasilinear theory.  The joint H^s energy estimate provides ε-uniform
bounds on a common time interval.  An all-order ε-uniform hierarchy plus diagonal
compactness gives a smooth limit solving the degenerate ε = 0 system.  Pullback
by the transported diffeomorphism recovers the fixed-cutoff geometric flow.

This replaces all previous start constructions (Steps 44, 49, 50, 51, 52, 53, 54).

## 1. The systems

### 1.1 Exact geometric equation

On a closed Riemannian manifold $(M^n,g_0)$ with a smooth function $\chi:M\to[0,1]$,
the target geometric equation is
$$
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g),\qquad g(0)=g_0.
\tag{1.1}
$$

### 1.2 DeTurck-gauged transported-cutoff system

Fix a smooth background metric $\bar g$ on $M$.  Define the DeTurck vector
$$
W^k(G)=G^{ab}\bigl(\Gamma(G)^k_{ab}-\Gamma(\bar g)^k_{ab}\bigr).
\tag{1.2}
$$
There are smooth universal tensors $R_{ij}(G,V)$ (linear in $V$) and $Q_{ij}(G,DG)$
(quadratic in $DG$, $D=\bar\nabla$) such that
$$
-2\operatorname{Ric}(G)+\mathcal L_{W(G)}G
=G^{ab}D_aD_bG_{ij}+R_{ij}(G,G)+Q_{ij}(G,DG).
\tag{1.3}
$$
The exact transported-cutoff normalized DeTurck system is
$$
\boxed{
\begin{cases}
\partial_tG
=\beta^2\bigl[G^{-1}D^2G+R(G,G)+Q(G,DG)-2G\bigr]
+2\operatorname{sym}\bigl(d(\beta^2)\otimes W(G)^\flat_G\bigr),\\[4pt]
\partial_t\beta=\beta^2W(G)\cdot D\beta,\\[4pt]
(G,\beta)|_{t=0}=(g_0,\chi).
\end{cases}
}
\tag{1.4}
$$
Using (1.3), the metric equation can be rewritten as
$$
\partial_tG=-2\beta^2(\operatorname{Ric}(G)+G)+\mathcal L_{\beta^2W(G)}G,
\tag{1.5}
$$
where $\mathcal L_{\beta^2W}G=\beta^2\mathcal L_WG+2\operatorname{sym}(d(\beta^2)\otimes W^\flat)$.

### 1.3 ε-regularized system

For $\varepsilon>0$, replace $\beta^2$ by $\beta^2+\varepsilon$ in the principal metric coefficient:
$$
\begin{cases}
\partial_tG_\varepsilon
=(\beta_\varepsilon^2+\varepsilon)\bigl[G_\varepsilon^{-1}D^2G_\varepsilon
+R(G_\varepsilon,G_\varepsilon)+Q(G_\varepsilon,DG_\varepsilon)\bigr]
-2\beta_\varepsilon^2G_\varepsilon
+2\operatorname{sym}\bigl(d(\beta_\varepsilon^2)\otimes W(G_\varepsilon)^\flat\bigr),\\[4pt]
\partial_t\beta_\varepsilon=\beta_\varepsilon^2W(G_\varepsilon)\cdot D\beta_\varepsilon,\\[4pt]
(G_\varepsilon,\beta_\varepsilon)|_{t=0}=(g_0,\chi).
\end{cases}
\tag{1.6}
$$
The critical structural facts:

- **The metric equation is strictly parabolic** for $\varepsilon>0$: the principal
  coefficient $(\beta^2+\varepsilon)G^{-1}\ge\varepsilon\lambda_{\min}(G^{-1})>0$.

- **The transport equation is unchanged**: $\varepsilon$ appears only in the metric
  equation.  The transport $\partial_t\beta=\beta^2W(G)\cdot D\beta$ is first-order
  with smooth coefficients (since $G$ is smooth for $\varepsilon>0$).

- **At $\varepsilon=0$, the system reduces to (1.4).**

## 2. Local well-posedness for ε > 0 (standard)

For $\varepsilon>0$, system (1.6) is a quasilinear strictly parabolic equation for
$G$ coupled to a first-order symmetric hyperbolic (transport) equation for $\beta$.
Standard theory applies:

**Proposition 2.1** (Standard quasilinear existence).  *For fixed $\varepsilon>0$ and
smooth initial data $(g_0,\chi)$ on a closed manifold $M^n$, there exists
$T_\varepsilon>0$ and a unique smooth solution $(G_\varepsilon,\beta_\varepsilon)$
of (1.6) on $[0,T_\varepsilon]$.*

*Proof sketch.*  The metric equation has the form
$\partial_tG=a(G,\beta)^{ab}D_aD_bG+F(G,DG,\beta,D\beta)$ with $a\ge\varepsilon C^{-1}>0$.
The transport equation $\partial_t\beta=\beta^2W(G)\cdot D\beta$ is a first-order
transport PDE with smooth velocity field $\beta^2W(G)$.  For the coupled system:

1. **Galerkin or Friedrichs truncation.**  Approximate $G$ and $\beta$ jointly on a
   finite-dimensional subspace $V_N\subset H^s(M)$.  The projected system is a
   finite-dimensional ODE with smooth right-hand side; Cauchy–Lipschitz gives
   existence on $[0,T_N]$.

2. **A priori H^s bounds** (identical to §3 below with the same data) give
   $T_N\ge T_0>0$ independently of $N$.

3. **Passage $N\to\infty$** by compactness in $H^s$ (standard: weak-$*$
   convergence in $L^\infty_t(H^s)$, strong convergence in $L^2_t(H^{s-1})$
   by Aubin–Lions, and passage of the nonlinear terms).

Uniqueness follows from the H^r difference estimate in §4 below.  $\square$

## 3. Joint H^s energy estimate (ε-uniform)

This is the central calculation.  Let $s>n/2+4$ and define
$$
\mathcal E_s(t)=\|G(t)\|_{H^s(\bar g)}^2+A\|\beta(t)\|_{H^s(\bar g)}^2,
\tag{3.1}
$$
where $A\gg1$ is a fixed coupling constant (to be chosen below), and all Sobolev norms
use the fixed background $\bar g$.

**Proposition 3.1** (ε-uniform a priori bound).  *There exist constants
$C_0=C_0(g_0,\chi,\bar g,s)$ and $T_0=T_0(g_0,\chi,\bar g,s)>0$,
**independent of $\varepsilon\in(0,1]$**, such that every smooth solution of (1.6)
on $[0,T]\subseteq[0,T_0]$ satisfies*
$$
\sup_{t\le T}\mathcal E_s(t)
+c\int_0^T\mathcal D_s(t)\,dt
\le 1+2\mathcal E_s(0),
\tag{3.2}
$$
$$
*where $\mathcal D_s=\sum_{k\le s}\int(\beta^2+\varepsilon)|D^{k+1}G|^2\,d\mu_{\bar g}$.*

*Proof.*  Differentiate $\|D^kG\|_2^2$ and $\|D^k\beta\|_2^2$ for $k\le s$ and sum.

**Metric dissipation.**  Testing $D^k\partial_tG$ against $D^kG$ at the principal level:
$$
\int D^kG\cdot D^k\bigl[(\beta^2+\varepsilon)G^{-1}D^2G\bigr]\,d\mu.
$$
The top-order term (all $k$ derivatives on $D^2G$) gives, after integration by parts,
$$
-\int(\beta^2+\varepsilon)|D^{k+1}G|^2\,d\mu.
\tag{3.3}
$$
**Metric commutators.**  When derivatives hit the coefficient $(\beta^2+\varepsilon)G^{-1}$,
the leading commutator involves $D\beta\cdot G^{-1}\cdot D^{k+1}G$ or
$DG\cdot G^{-2}\cdot D^{k+1}G$.  For $s>n/2+4$, $\|DG\|_\infty+\|D\beta\|_\infty\le C_R$.
Hence each commutator is estimated by
$$
\eta\int(\beta^2+\varepsilon)|D^{k+1}G|^2+C_\eta\mathcal E_s.
\tag{3.4}
$$
Absorb $\eta$-portions into the dissipation.

**Normalization term** $-2\beta^2G$: this is algebraic (no new derivatives), contributing
$\le C\mathcal E_s$.

**Quadratic term** $\beta^2Q(G,DG)$: $Q$ is quadratic in $DG$ with $G$-dependent
coefficients.  At order $k$, the top term is schematically
$\beta^2\cdot G^{-1}\cdot DG\cdot D^{k+1}G$.  When tested against $D^kG$:
$$
\left|\int D^kG\cdot\beta^2 A(G)D^{k+1}G\right|
\le\eta\int(\beta^2+\varepsilon)|D^{k+1}G|^2
+C_{\eta,R}\|D^kG\|_2^2,
\tag{3.5}
$$
using $\beta^2\le\beta^2+\varepsilon$ and Young's inequality with the bounded
factor $\|A(G)\|_{\infty}\le C_R$.  The $\eta$-portion is absorbed into dissipation.

**Lie cross-term** $2\operatorname{sym}(d(\beta^2)\otimes W(G)^\flat)$:  Since
$d(\beta^2)=2\beta D\beta$, the top-order contribution at order $k$ is either:
- $\beta\cdot D^{k+1}\beta\cdot W(G)$: integrate the top $\beta$-derivative onto
  $D^kG$, producing $\beta\cdot D^k\beta\cdot DW$ plus $\beta D^{k+1}G\cdot D^k\beta$;
  the latter is absorbed by the $(\beta^2+\varepsilon)|D^{k+1}G|^2$ dissipation
  (after Cauchy–Schwarz with the $\beta$ factor).
- $\beta\cdot D\beta\cdot D^kW(G)$: involves $D^{k+1}G$ with bounded
  $\beta D\beta$ coefficient; absorbed by dissipation.

**Transport equation.**  At order $k$:
$$
\int D^k\beta\cdot D^k[\beta^2W(G)\cdot D\beta]\,d\mu.
\tag{3.6}
$$
The top advective term $\beta^2W\cdot D^{k+1}\beta$ is handled by the standard
transport IBP identity:
$$
\int D^k\beta\cdot\beta^2W\cdot D^{k+1}\beta
=-\tfrac12\int|D^k\beta|^2\operatorname{div}(\beta^2W)\,d\mu
\le C_R\|D^k\beta\|_2^2.
\tag{3.7}
$$
The **critical cross-coupling** is the term from Moser commutators where $D^k$ hits $W(G)$:
$$
\int D^k\beta\cdot\beta^2\cdot D^kW(G)\cdot D\beta\,d\mu.
\tag{3.8}
$$
Since $D^kW(G)$ involves $D^{k+1}G$, this becomes schematically
$$
\int\beta\cdot|D^k\beta|\cdot\beta\cdot|D^{k+1}G|\cdot|D\beta|\,d\mu.
\tag{3.9}
$$
By Cauchy–Schwarz:
$$
\le\eta\int\beta^2|D^{k+1}G|^2+C_\eta\|D\beta\|_\infty^2\int\beta^2|D^k\beta|^2.
\tag{3.10}
$$
The $\eta$-term is absorbed into the metric dissipation (note $\beta^2\le\beta^2+\varepsilon$);
the second term contributes $C_R\mathcal E_s$.

**Assembly.**  Combining all contributions with $A$ chosen large enough to dominate
the transport coupling:
$$
\mathcal E_s'+c\mathcal D_s\le C_R(1+\mathcal E_s).
\tag{3.11}
$$
Grönwall on the ODE $y'=C_R(1+y)$ gives $\mathcal E_s(t)\le(1+\mathcal E_s(0))e^{C_Rt}-1$.
Choose $T_0$ so that $(1+\mathcal E_s(0))e^{C_RT_0}\le 1+2\mathcal E_s(0)$.  The
continuation also requires $G(t)$ to stay uniformly positive definite; this follows
from $\|\partial_tG\|_{C^0}\le C$ (by Sobolev embedding from $H^{s-2}$) giving
$G(t)\ge g_0/2>0$ for $t\le T_0$ sufficiently small.  Crucially,
**$C_R$ depends on the initial data and $s$, not on $\varepsilon$**, because every $\varepsilon$-dependent term appeared as
$\beta^2+\varepsilon\ge\beta^2$ in the dissipation, not as $\varepsilon^{-1}$
in a source.  $\square$

## 4. Difference estimate and uniqueness at H^r (r = s − 2)

Let $(G_1,\beta_1)$ and $(G_2,\beta_2)$ be two smooth solutions of (1.6) on $[0,T]$ with
the **same** initial data and the **same** $\varepsilon\ge0$.  Set
$$
Z=G_1-G_2,\qquad\omega=\beta_1-\beta_2,\qquad r=s-2>n/2+2.
\tag{4.1}
$$

**Proposition 4.1** (Stability and uniqueness).  *There exists $C=C(g_0,\chi,s)$,
independent of $\varepsilon$, such that*
$$
\|Z(t)\|_{H^r}^2+A\|\omega(t)\|_{H^r}^2
\le e^{Ct}\bigl(\|Z(0)\|_{H^r}^2+A\|\omega(0)\|_{H^r}^2\bigr).
\tag{4.2}
$$
*In particular, same initial data implies $Z\equiv0$, $\omega\equiv0$.*

*Proof.*  The difference of the principal metric terms is
$$
(\beta_1^2+\varepsilon)G_1^{-1}D^2G_1
-(\beta_2^2+\varepsilon)G_2^{-1}D^2G_2
=(\beta_2^2+\varepsilon)G_2^{-1}D^2Z+\Sigma,
\tag{4.3}
$$
where the coefficient-difference remainder is
$$
\Sigma=(\beta_1^2-\beta_2^2)G_1^{-1}D^2G_1
+(\beta_2^2+\varepsilon)(G_1^{-1}-G_2^{-1})D^2G_1.
\tag{4.4}
$$
The first term in (4.3) gives branch-2 dissipation $-(\beta_2^2+\varepsilon)\|D^{r+1}Z\|_2^2$.

**Coefficient-difference control** (the key structural simplification).
At Sobolev order $r$, the worst term in $D^r\Sigma$ involves
$\omega\cdot D^{r+2}G_1=\omega\cdot D^sG_1$.  Since $r>n/2$, Sobolev embedding gives
$\|\omega\|_\infty\le C\|\omega\|_{H^r}$, and $D^sG_1\in L^2$ from the $H^s$ ball.
Therefore
$$
\|D^r\Sigma\|_2\le C_R(\|\omega\|_{H^r}+\|Z\|_{H^r}).
\tag{4.5}
$$
**No interpolation of a difference is used.** The individual $H^s$ bounds control
every factor in (4.4) except the difference itself, which appears only at order $r$.

**Quadratic Q-type difference** (corrected per TTCS: direct Young, not
antisymmetric identity).  The top contribution is
$\beta_2^2 G_2^{-1}DG_2\cdot D^{r+1}Z$.  When tested against $D^rZ$:
$$
\left|\int D^rZ\cdot\beta_2^2 A(G_2)\cdot D^{r+1}Z\right|
\le\eta\int(\beta_2^2+\varepsilon)|D^{r+1}Z|^2
+C_{\eta,R}\|Z\|_{H^r}^2,
\tag{4.6}
$$
using $\beta_2^2\le\beta_2^2+\varepsilon$ and Young's inequality with the bounded
factor $\|A(G_2)\|_\infty\le C_R$.  The $\eta$-portion is absorbed by the
branch-2 metric dissipation.

**Lie cross-term difference.**  Use the identities
$$
d(\beta_1^2)-d(\beta_2^2)=2\beta_2d\omega+2\omega d\beta_1,
\tag{4.7}
$$
$$
W(G_1)-W(G_2)\sim G^{-1}D(G_1-G_2)+\text{lower}=G^{-1}DZ+\text{lower}.
\tag{4.8}
$$
The top cutoff-difference term is $\beta_2W(G_2)D^{r+1}\omega$ (tested against $D^rZ$).
Integrate by parts:
$$
\int D^rZ\cdot\beta_2W(G_2)\cdot D^{r+1}\omega
=-\int\beta_2 D^{r+1}Z\cdot W(G_2)\cdot D^r\omega+\text{lower}.
\tag{4.9}
$$
The result carries $\beta_2\cdot D^{r+1}Z$, absorbed by $(\beta_2^2+\varepsilon)|D^{r+1}Z|^2$.
**Branch-oriented Lie decomposition** (corrected per TTCS).  The full Lie
difference is
$$
d(\beta_1^2)\odot\mathcal W(G_1)-d(\beta_2^2)\odot\mathcal W(G_2)
=[d(\beta_1^2)-d(\beta_2^2)]\odot\mathcal W(G_1)
+d(\beta_2^2)\odot[\mathcal W(G_1)-\mathcal W(G_2)].
\tag{4.7b}
$$
The first bracket splits as $2\beta_2d\omega\odot\mathcal W(G_1)
+2\omega d\beta_1\odot\mathcal W(G_1)$.  The term
$\omega d\beta_1\odot\mathcal W(G_1)$ at order $r$ contains
$\omega\cdot d\beta_1\cdot D^r\mathcal W(G_1)\sim\omega\cdot d\beta_1\cdot D^{r+1}G_1$.
This is a **complete branch-1 quantity**: $\|\omega\|_\infty\cdot\|d\beta_1\|_\infty
\cdot\|D^{r+1}G_1\|_2\le C_R\|\omega\|_{H^r}$,
controlled by the individual $H^s$ ball.  It must **not** be split further to
manufacture an unweighted $D^{r+1}Z$.  The second bracket
$d(\beta_2^2)\cdot[\mathcal W(G_1)-\mathcal W(G_2)]$ has top term
$\beta_2 d\beta_2\cdot D^{r+1}Z$, which carries the correct $\beta_2$ weight
for absorption.

**Transport difference.**
$$
\partial_t\omega
=\beta_1^2W(G_1)\cdot D\omega
+[\beta_1^2W(G_1)-\beta_2^2W(G_2)]\cdot D\beta_2.
\tag{4.10}
$$
The advective top $\beta_1^2W(G_1)\cdot D^{r+1}\omega$ is removed by transport IBP.
The critical cross-coupling term, after the velocity splitting
$$
\beta_1^2W(G_1)-\beta_2^2W(G_2)
=\beta_2^2[W(G_1)-W(G_2)]
+(\beta_1^2-\beta_2^2)W(G_1),
\tag{4.11}
$$
produces $\beta_2^2\cdot D^{r+1}Z\cdot D\beta_2$ at the top level.  When tested against
$D^r\omega$:
$$
\int D^r\omega\cdot\beta_2^2\cdot D^{r+1}Z\cdot D\beta_2
\le\eta\int(\beta_2^2+\varepsilon)|D^{r+1}Z|^2
+C_\eta\|\omega\|_{H^r}^2.
\tag{4.12}
$$
The $\eta$-term is absorbed by the metric dissipation.

**Assembly.**  Summing metric and transport contributions:
$$
\frac d{dt}\bigl(\|Z\|_{H^r}^2+A\|\omega\|_{H^r}^2\bigr)
+c\int(\beta_2^2+\varepsilon)|D^{r+1}Z|^2
\le C_R\bigl(\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2\bigr).
\tag{4.13}
$$
The dissipation is a bonus.  Grönwall gives (4.2), with $C$ depending only on
initial data and $s$.  For $\varepsilon=0$, the estimate still holds: $\beta_2^2$ helps
dissipation but is not required for the Grönwall bound.  $\square$

**Remark 4.2.**  This estimate works at the **same regularity** for both $\varepsilon>0$
and $\varepsilon=0$ because **every** coefficient difference is controlled by the
individual $H^s$ balls without interpolation.  The grading $r=s-2$ is needed only
so that $D^{r+2}G_i=D^sG_i\in L^2$, not for a Banach contraction.

## 5. All-order ε-uniform hierarchy

For each integer $m\ge s$, define
$$
E_m=\|G\|_{H^m}^2+A_m\|\beta\|_{H^m}^2,\qquad
D_m=\sum_{k\le m}\int(\beta^2+\varepsilon)|D^{k+1}G|^2.
\tag{5.1}
$$

**Proposition 5.1** (Higher regularity propagation).  *On $[0,T_0]$, for each $m\ge s$,
there exist constants depending on lower-order norms but not on $\varepsilon$ such that*
$$
E_m'+c_mD_m\le C_m(E_{m-1})(1+E_m).
\tag{5.2}
$$

*Proof.*  The argument parallels §3 at each order $m$, with one important
inductive feature.  At order $m$, the Moser commutator estimates on the principal
coefficient $(\beta^2+\varepsilon)G^{-1}$ produce terms involving $D^j$ of this
coefficient for $j=1,\ldots,m$ and $D^{m+1-j}$ of $D^2G$.  For $j\le m-s$, the
coefficient factor $D^j[(\beta^2+\varepsilon)G^{-1}]$ is bounded by
$C(E_s)$ (using the already-established $H^s$ bound).  For $j>m-s$, the $G$-factor
has fewer than $s+2$ derivatives and is bounded, while the coefficient factor
involves $D^j\beta$ or $D^jG$ with $j\le m$ (controlled by $E_m$).

The cross-coupling structure is preserved: the transport equation's Moser
commutator at order $m$ produces $\beta^2D^{m+1}G\cdot D\beta$, absorbed by
$(\beta^2+\varepsilon)|D^{m+1}G|^2$ exactly as in §3.  Iterating: $E_s$ is
bounded first, then $E_{s+1}$ using $E_s$, then $E_{s+2}$ using $E_{s+1}$, etc.
Each step is an ODE $y'\le C(1+y)$ with $\varepsilon$-independent constants.

**Time derivatives.**  From the equation,
$\|\partial_tG\|_{H^{m-2}}\le C_m(E_m)$ and
$\|\partial_t\beta\|_{H^{m-1}}\le C_m(E_m)$, both $\varepsilon$-uniform.
Higher time derivatives: $\partial_t^2G$ involves $\partial_t$ of all
coefficients and $D^2(\partial_tG)$; from the equation and $E_m$ bounds,
$\|\partial_t^2G\|_{H^{m-4}}\le C_m$.  Inductively, all space-time jets
are $\varepsilon$-uniformly bounded.  $\square$

## 6. Passage ε → 0

**Proposition 6.1** (Smooth degenerate limit).  *There exists a unique smooth solution
$(G_0,\beta_0)$ of the $\varepsilon=0$ system (1.4) on $[0,T_0]$, obtained as the
$C^\infty$ limit of the $\varepsilon$-regularized solutions.*

*Proof.*

**Compactness.**  The ε-uniform bounds $E_m(t)\le C_m$ for all $m$ on $[0,T_0]$ give
$(G_\varepsilon,\beta_\varepsilon)$ bounded in $C^k([0,T_0]\times M)$ for every $k$.
By Arzelà–Ascoli (using the compact embedding $H^{m+1}\hookrightarrow\hookrightarrow H^m$
on the closed manifold $M$, combined with the equicontinuity from time-derivative bounds),
a diagonal subsequence $\varepsilon_j\to0$ satisfies
$$
(G_{\varepsilon_j},\beta_{\varepsilon_j})\to(G_0,\beta_0)\quad\text{in }C^\infty([0,T_0]\times M).
\tag{6.1}
$$

**Limit equation.**  Since $G_{\varepsilon_j}\to G_0$ in $C^2$ and
$\varepsilon_j\to0$:
$$
\varepsilon_j\cdot G_{\varepsilon_j}^{-1}D^2G_{\varepsilon_j}
\to 0\cdot G_0^{-1}D^2G_0=0
\quad\text{in }C^0.
\tag{6.2}
$$
All other terms converge in $C^k$ to their $\varepsilon=0$ values.  Therefore
$(G_0,\beta_0)$ solves (1.4).

**Uniqueness.**  Proposition 4.1 applies with $\varepsilon=0$: any two smooth solutions
with the same initial data satisfy $Z\equiv0$, $\omega\equiv0$.  Hence the full
sequence converges (not just a subsequence).

**Zero-set behavior.**  On $\{\chi=0\}$:  $\beta_0(0,\cdot)=\chi=0$ and
$\partial_t\beta_0=\beta_0^2W\cdot D\beta_0=0$ wherever $\beta_0=0$.  By uniqueness
of the (trivial) ODE, $\beta_0(t,\cdot)\equiv0$ on $\{\chi=0\}$ for all $t\in[0,T_0]$.
Then $\partial_tG_0=0$ on $\{\beta_0=0\}$, so $G_0(t,\cdot)=g_0$ on $\{\chi=0\}$.  $\square$

## 7. Pullback to the geometric equation

**Proposition 7.1** (Geometric flow existence).  *The smooth family
$g(t)=\varphi(t)^*G_0(t)$, where $\varphi$ solves*
$$
\partial_t\varphi(t,x)=-\beta_0(t,\varphi(t,x))^2\,W(G_0)(t,\varphi(t,x)),
\qquad\varphi(0)=\operatorname{id},
\tag{7.1}
$$
*satisfies $\partial_tg=-2\chi^2(\operatorname{Ric}_g+g)$, $g(0)=g_0$.*

*Proof.*

**Step 1: Transport preserves the initial cutoff.**
The Eulerian velocity is $X(t,y)=-\beta_0(t,y)^2W(G_0)(t,y)$, and the characteristic
ODE is $\partial_t\varphi(t,x)=X(t,\varphi(t,x))$.  Let $f(t)=\beta_0(t,\varphi(t,x))$.  Then
$$
f'(t)
=\partial_t\beta_0\big|_{\varphi}+D\beta_0\big|_{\varphi}\cdot\partial_t\varphi
=\bigl[\beta_0^2 W\cdot D\beta_0\bigr]_{\varphi}
+D\beta_0\big|_{\varphi}\cdot\bigl[-\beta_0^2W\bigr]_{\varphi}
=0.
\tag{7.2}
$$
Hence $\beta_0(t,\varphi(t,x))=\beta_0(0,x)=\chi(x)$ for all $t$.

**Step 2: Pullback formula.**
Since $\varphi_t$ has Eulerian velocity $X=-\beta_0^2W(G_0)$,
the standard identity $\partial_t(\varphi^*G)=\varphi^*(\partial_tG+\mathcal L_XG)$ gives
$$
\partial_tg=\varphi^*(\partial_tG_0+\mathcal L_XG_0).
\tag{7.3}
$$

**Step 3: Cancellation.**
From (1.5), $\partial_tG_0=-2\beta_0^2(\operatorname{Ric}(G_0)+G_0)+\mathcal L_{\beta_0^2W}G_0$.
Since $X=-\beta_0^2W$:
$$
\partial_tG_0+\mathcal L_XG_0
=-2\beta_0^2(\operatorname{Ric}(G_0)+G_0)
+\mathcal L_{\beta_0^2W}G_0+\mathcal L_{-\beta_0^2W}G_0
=-2\beta_0^2(\operatorname{Ric}(G_0)+G_0).
\tag{7.4}
$$
Pulling back and using $\beta_0(t,\varphi(t,x))=\chi(x)$:
$$
\partial_tg
=\varphi^*\bigl(-2\beta_0^2(\operatorname{Ric}(G_0)+G_0)\bigr)
=-2\chi^2\bigl(\operatorname{Ric}(g)+g\bigr),
\tag{7.5}
$$
where we used $\varphi^*(\beta_0^2T)=(\beta_0\circ\varphi)^2\varphi^*T=\chi^2\,\varphi^*T$,
$\varphi^*\operatorname{Ric}(G_0)=\operatorname{Ric}(g)$, and $\varphi^*G_0=g$.  $\square$

## 8. Restart and persistence

At $t=T_0$, a smooth endpoint can be restarted by a valid per-datum local construction.  The new lifespan may depend on high Sobolev norms of the endpoint and on higher cutoff jets.  Curvature-to-volume budgets alone do **not** bound these quantities or give a sequence-uniform restart time.  The uniform observation-time mechanism must instead run the legitimate first-exit estimates on each actual lifespan and use positive-time shifted-curvature continuation to exclude an earlier endpoint; see Step 56 §6.3.

## 9. Main theorem

**Theorem 9.1** (Per-datum normalized cutoff flow).
*Let $(M^n,g_0)$ be a closed smooth Riemannian manifold and $\chi:M\to[0,1]$ a smooth
function.  There exist $T=T(g_0,\chi)>0$ and a unique smooth family of Riemannian
metrics $g(t)$, $t\in[0,T]$, solving*
$$
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g),\qquad g(0)=g_0.
\tag{9.1}
$$
*The solution satisfies:*

1. *$g(t)=g_0$ on $\{\chi=0\}$ for all $t$* (stationary exterior);
2. *$g(t)$ is smooth across the interface $\partial\{\chi>0\}$;*
3. *the existence time $T$ depends on $\|g_0\|_{H^s}$ and $\|\chi\|_{C^s}$, not on
   the zero set of $\chi$.*

*Proof.*  The ε-regularized solutions exist by Proposition 2.1.  The ε-uniform
H^s bound (Proposition 3.1) gives a common time $T_0$.  The all-order hierarchy
(Proposition 5.1) gives ε-uniform bounds at every Sobolev level.  Diagonal
compactness (Proposition 6.1) produces a unique smooth ε=0 solution.  The pullback
(Proposition 7.1) recovers the geometric equation.  $\square$

## 10. What this replaces and what remains

### 10.1 Superseded constructions

All previous start constructions are superseded:
- Step 44 (Yang tame-inverse adaptation)
- Step 49 (nonlinear coefficient-regularization)
- Step 50 (lower-order perturbation analysis)
- Step 51 (critical L^p estimate)
- Step 52 (metric-only Xu repair)
- Step 53 (coupled frozen-product iteration)
- Step 54 (synchronized-output inner/outer iteration)

The direct nonlinear route is simpler because it avoids all iteration
architectures.  For ε > 0, the system is standard; the degenerate limit is
obtained by compactness.

### 10.2 What the theorem does NOT provide

1. **Sequence-uniform existence time.**  $T$ depends on the initial datum.
   For the restricted IL argument, we need $T$ to be uniform across a collapsing
   sequence.  This requires the geography-uniform curvature/volume budgets
   established in the terminal chain (Steps 29, 46, 47).

2. **First-exit estimates.**  The ε-uniform H^s bound secures existence, but the
   weighted curvature quantities $K_2$, $Y$, $J_6$, the all-$p$ defect ladder,
   global $Q$, and metric drift must still be verified on the exact flow with
   the correct support geometry.

3. **Terminal spectral obstruction.**  The forbidden Einstein germ,
   terminal density $\int\mathfrak D\le119Q$, core-ball spectral determination,
   and the projector/Derdziński contradiction are all downstream of the
   first-exit chain.

4. **Full Yau Problem 26.**  The smoothing theorem is topology-independent and
   reusable, but it does not by itself prove or disprove the original problem.
   Positive branch, arbitrary topology, $n\ge5$, and Lean formalization remain.

### 10.3 Relation to A02's product-quotient work

A02 #394 tests reversed negative product-quotient surfaces.  The combined
status is: the smoothing mechanism (this note) supplies Module S; the
IL spectral obstruction (Steps 29, 43, 46, 47) supplies Module O with
family-uniform normalization confirmed in Step 54.  But a complete
restricted IL theorem still requires the connected first-exit verification
on this exact flow.

## 11. Verification and corrections

- 22/22 structural checks pass (`verify_step55_direct_construction.py`).
- Pullback identity (7.2)–(7.5) verified by explicit computation.
- Zero-set preservation follows from the ODE $f'=0$.
- ε-cancellation (6.2) is elementary.

**TTCS corrections incorporated** (from `trace/ttcs/results/step55_ttcs01_verifier1_integration.md`):

1. **Diffeomorphism ODE** (7.1): corrected to evaluate $\beta$ at $\varphi(t,x)$, not
   at $x$.  Eulerian velocity is $X(t,y)=-\beta(t,y)^2W(G)(t,y)$.
2. **Q-type energy terms** (3.5) and (4.6): replaced the unverified tensor antisymmetric
   identity with direct weighted Young/Cauchy–Schwarz, which is strictly valid.
3. **Lie difference decomposition** (4.7b): rewritten with Step 54's branch-oriented
   split.  The $\omega\cdot d\beta_1$ term is kept as a complete branch-1 quantity,
   not split further.
4. **Grönwall bound** (3.2): replaced $2\mathcal E_s(0)$ with the correct
   $(1+\mathcal E_s(0))e^{C_RT_0}-1$; added metric positivity bootstrap.
5. **All-order hierarchy** (Prop 5.1): made the inductive structure explicit, with
   each order $m$ using bounds from orders $\le m-1$.
6. **Fixed-ε construction** (Prop 2.1): replaced mollification with joint
   Galerkin/Friedrichs truncation for the coupled parabolic–transport system.

**Remaining items not addressed in this note:**
- Term-by-term verification of the exact DeTurck tensors $R,Q$ at every order.
- Explicit Galerkin basis and convergence for the coupled system.
- Complete first-exit chain, terminal obstruction, or Yau 26.


## Appendix: Interface with the first-exit chain

The start theorem (Theorem 9.1) applies directly to the global cutoff
$\chi=\sum_{\alpha\in\mathcal C}\chi_\alpha$, where the support construction gives
disjoint $\operatorname{supp}(\chi_\alpha)\subset B_{5r}(x_\alpha)$ with
$d(x_\alpha,x_\beta)>12r$.  Then
$$
\chi^2=\left(\sum\chi_\alpha\right)^2=\sum\chi_\alpha^2=a
\tag{A.1}
$$
since $\chi_\alpha\chi_\beta=0$ for $\alpha\ne\beta$ (disjoint supports).

The exact flow $\partial_tg=-2a(\operatorname{Ric}+g)$ on $[0,T_0]$ has:
- **Stationary exterior:** $g(t)=g_0$ on $\{a=0\}$ (exact, not approximate).
- **Standard normalized Ricci flow on plateaux:** $\partial_tg=-2(\operatorname{Ric}+g)$
  on each $B_{4r}(x_\alpha)$ where $a=1$.
- **Smooth transition:** bounded cutoff derivatives $|\nabla^ka|\le C_k/r^k$, per-datum.

The shifted curvature $T=\operatorname{Rm}+G$, $U=aT$ gives
$\partial_tg=-2\operatorname{Ric}(U)$ and $\operatorname{Ric}(T)=\operatorname{Ric}+g=E$.

**Disjoint-support global Q.**  Since $\operatorname{supp}(\eta_\alpha)$ are
pairwise disjoint:
$$
Q_{\rm global}(T)=Q_{\rm rest}(0)+\sum_\alpha Q_\alpha(T),\qquad
Q_{\rm rest}(t)=\int_M\left(1-\sum_\alpha\eta_\alpha^2\right)|E(t)|^2d\mu_t,
\tag{A.2}
$$
where each $Q_\alpha$ is a local defect integral and the strict buffer $\operatorname{supp}\chi_\alpha\Subset\{\eta_\alpha=1\}$ makes $Q_{\rm rest}$ stationary on the exact flow.  The selected supports need not cover $M$.

**Sequence uniformity.**  Geography-uniform curvature-to-volume budgets control the unweighted critical curvature energies and first cutoff derivatives used in first exit; they do not control initial high Sobolev norms or higher cutoff jets.  Local start is therefore per datum.  A common observation time, if obtained, comes from uniform first-exit estimates on each actual lifespan followed by datum-dependent positive-time continuation, as described in Step 56 §6.3.
