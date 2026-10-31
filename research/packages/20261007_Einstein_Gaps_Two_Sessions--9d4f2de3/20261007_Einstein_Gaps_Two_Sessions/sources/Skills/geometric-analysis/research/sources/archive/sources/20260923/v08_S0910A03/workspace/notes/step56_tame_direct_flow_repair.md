# Step 56: tame completion of the direct transported-cutoff construction

Session: S0910A03. Agent3 / Actuator. Phase: Execute.

## 0. Purpose and corrected status

The direct nonlinear architecture of Step 55 is retained: one solves for one metric–cutoff pair rather than introducing frozen inputs and an outer contraction.  Step 55, however, did not prove its arbitrary-order estimate.  In particular, its split at derivative order `j <= m-s` incorrectly asserted that arbitrarily high coefficient derivatives are controlled by the fixed low energy `E_s`.

This note replaces that split by a genuine tame product estimate.  It also makes the approximation fully parabolic by adding an auxiliary scalar viscosity.  The scalar viscosity is used only to construct the joint approximants and is removed together with the metric regularization.  No estimate below divides by either regularization parameter.

The resulting local theorem is **per datum**.  Its lifespan depends on high Sobolev norms of the initial metric and cutoff.  Curvature-to-volume bounds do not control those norms.  Sequence-uniform time in the Ishida–LeBrun application must instead come from the unweighted critical curvature first-exit estimates and positive-time continuation.

## 1. Coupled systems

Fix a closed manifold, a smooth background metric $\bar g$, and write $D=\bar\nabla$.  For a positive metric $G$, let
\[
 W^k(G)=G^{ab}\bigl(\Gamma(G)^k_{ab}-\Gamma(\bar g)^k_{ab}\bigr).
\]
The transported-cutoff DeTurck system is
\[
\begin{split}
 \partial_tG={}&\beta^2\bigl[G^{-1}D^2G+R(G,G)+Q(G,DG)-2G\bigr]
 +2\operatorname{sym}\bigl(d(\beta^2)\otimes W(G)^\flat_G\bigr),\\
 \partial_t\beta={}&\beta^2W(G)\cdot D\beta,
\end{split}
\tag{1.1}
\]
where $R$ is algebraic in $G$ and the background curvature and $Q$ is quadratic in $DG$, with coefficients smooth in $G^{\pm1}$.

For $0<\varepsilon,\nu\le1$, use the doubly regularized system
\[
\begin{split}
 \partial_tG={}&(\beta^2+\varepsilon)G^{-1}D^2G
 +(\beta^2+\varepsilon)\{R(G,G)+Q(G,DG)\}-2\beta^2G\\
 &\quad+2\operatorname{sym}\bigl(d(\beta^2)\otimes W(G)^\flat_G\bigr),\\
 \partial_t\beta={}&\beta^2W(G)\cdot D\beta+\nu\bar\Delta\beta.
\end{split}
\tag{1.2}
\]
The harmless choice of multiplying $R,Q$ by $\beta^2+\varepsilon$ makes the metric principal block the standard Ricci–DeTurck block.  The extra $\varepsilon(R+Q)$ and $\nu\bar\Delta\beta$ vanish in the limit.  For fixed positive $(\varepsilon,\nu)$, (1.2) is a quasilinear strongly parabolic system with diagonal principal blocks.

The scalar maximum principle gives
\[
 0\le\beta(t)\le1
\tag{1.3}
\]
when $0\le\beta(0)=\chi\le1$: at a spatial extremum the transport term vanishes, while the sign of $\nu\bar\Delta\beta$ is favorable.

## 2. Tame product lemma

Choose an integer
\[
 s_0>\frac n2+4.
\tag{2.1}
\]
All constants below are taken on a metric neighborhood
\[
 \lambda\bar g\le G\le\lambda^{-1}\bar g,
 \qquad \|G\|_{H^{s_0}}+\|\beta\|_{H^{s_0}}\le R.
\tag{2.2}
\]

We use the standard Moser–Hamilton estimates on the fixed compact background:
\[
 \|uv\|_{H^m}
 \le C_m\bigl(\|u\|_{L^\infty}\|v\|_{H^m}
                 +\|u\|_{H^m}\|v\|_{L^\infty}\bigr),
\tag{2.3}
\]
\[
 \|[D^m,u]v\|_2
 \le C_m\bigl(\|Du\|_{L^\infty}\|v\|_{H^{m-1}}
                 +\|u\|_{H^m}\|v\|_{L^\infty}\bigr),
\tag{2.4}
\]
and their smooth-composition versions for $G^{-1}$ and tensors depending smoothly on $G$.

The form needed below is the following two-derivative tame remainder estimate.  If $m\ge s_0$ and $u_i$ obey (2.2), then every finite sum of products
\[
 D^{q_1}u_1*\cdots*D^{q_N}u_N,
 \qquad q_i\le m,
 \qquad \sum_iq_i\le m+2,
\tag{2.5}
\]
which remains after all occurrences of a single $D^{m+1}G$ or $D^{m+1}\beta$ have been removed, obeys
\[
 \left\|D^{q_1}u_1*\cdots*D^{q_N}u_N\right\|_2
 \le C_{m,R}\left(1+\|G\|_{H^m}+\|\beta\|_{H^m}\right).
\tag{2.6}
\]
Here undifferentiated smooth functions of $G^{\pm1}$ are allowed as coefficients.

Here is the precise interpolation count.  For every factor with $q_i>4$, put
\[
 \theta_i=\frac{q_i-4}{m-4}.
\]
Gagliardo–Nirenberg interpolation between $H^m$ and the $W^{4,\infty}$ norm supplied by (2.1)–(2.2) gives
\[
 \|D^{q_i}u_i\|_{L^{2/\theta_i}}
 \le C_{m,R}\|u_i\|_{H^m}^{\theta_i}.
\tag{2.5a}
\]
Factors with $q_i\le4$ go in $L^\infty$.  If there are $k\ge2$ high factors, then
\[
 \sum_{q_i>4}(q_i-4)\le m+2-4k\le m-6<m-4,
\]
so $\sum\theta_i<1$; if there is one high factor, $\theta_1\le1$.  Hölder, with the unused reciprocal exponent assigned to the finite-volume factor $1$, gives (2.6), and $x^\theta\le1+x$ makes the estimate linear in the current high norm.  Faà di Bruno expansion gives the same conclusion for smooth functions of $G^{\pm1}$.  This is the usual tame, rather than algebra, estimate: only one high $H^m$ norm occurs on the right.  Equations (2.3)–(2.4) are equivalent convenient formulations for the binary products below.  The finite derivative-budget check in `workspace/scripts/step56_tame_allocation_check.py` exhausts the principal, $Q$, Lie, and transport partitions for $7\le m\le40$; its 14,002,305 checks have zero failures (`workspace/data/step56_tame_allocation_checks.json`).  That computation checks only the integer allocation and interpolation exponents, not the tensor identities or PDE argument.

Two explicit consequences used repeatedly are
\[
 \sum_{j=2}^m\|D^jA*D^{m-j+2}G\|_2
 \le C_{m,R}(1+\|G\|_{H^m}+\|\beta\|_{H^m}),
\tag{2.7}
\]
for $A=(\beta^2+\varepsilon)G^{-1}$, and
\[
 \|D^{m+1}(\beta^2)-2\beta D^{m+1}\beta\|_2
 \le C_{m,R}\|\beta\|_{H^m}.
\tag{2.8}
\]
Neither estimate asserts that a high coefficient derivative is bounded by $E_{s_0}$; the high derivative is retained linearly in the current $H^m$ energy.

## 3. Arbitrary-order energy

Set
\[
 \mathcal E_m=\|G\|_{H^m}^2+A_m\|\beta\|_{H^m}^2,
\quad
 \mathcal D_m^G=\sum_{k\le m}\int_M(\beta^2+\varepsilon)|D^{k+1}G|^2d\mu_{\bar g},
\quad
 \mathcal D_m^\beta=\nu\|D^{m+1}\beta\|_2^2.
\tag{3.1}
\]
The constants $A_m>0$ are fixed and finite.

### Proposition 3.1 (tame hierarchy)

On a time interval satisfying (2.2), every smooth solution of (1.2) obeys, for $m\ge s_0$,
\[
 \frac d{dt}\mathcal E_m+c_{m,\lambda}\mathcal D_m^G
       +c_m\mathcal D_m^\beta
 \le C_{m,R}(1+\mathcal E_m),
\tag{3.2}
\]
with constants independent of $0<\varepsilon,\nu\le1$.

### 3.1 Principal metric term

Write $A^{ab}=(\beta^2+\varepsilon)G^{ab}$.  After applying $D^m$ and integrating the leading term once,
\[
 \langle D^mG,D^m(AD^2G)\rangle
 \le-c\int(\beta^2+\varepsilon)|D^{m+1}G|^2+I_1+I_{\ge2}.
\tag{3.3}
\]
The first coefficient derivative splits exactly as
\[
 DA=2\beta D\beta\,G^{-1}+(\beta^2+\varepsilon)D(G^{-1}).
\tag{3.4}
\]
Thus weighted Young gives
\[
 |I_1|\le \zeta\mathcal D_m^G+C_{\zeta,R}\|G\|_{H^m}^2,
\tag{3.5}
\]
using $\beta^2/(\beta^2+\varepsilon)\le1$.  For $j\ge2$, the other metric factor has derivative order $m-j+2\le m$; (2.7), followed by pairing with $D^mG$, gives
\[
 |I_{\ge2}|\le C_{m,R}(1+\mathcal E_m).
\tag{3.6}
\]
This is the point where the false Step 55 derivative split is replaced.

### 3.2 Quadratic and algebraic metric terms

For $(\beta^2+\varepsilon)Q(G,DG)$, the only factor above order $m$ is
\[
 (\beta^2+\varepsilon)A(G,DG)D^{m+1}G.
\tag{3.7}
\]
It is absorbed by weighted Young.  If a derivative hits $\beta^2$ or a second differentiated $G$ factor, all remaining factors have order at most $m$ and total derivative order at most $m+2$; (2.6) gives $C_{m,R}(1+\mathcal E_m)$.  The $R$ and $-2\beta^2G$ terms have still lower differential order and satisfy the same bound.

### 3.3 Lie cross term

Suppress fixed contractions and write it as $D(\beta^2)*W(G)$.  There are two top allocations.

First,
\[
 D(\beta^2)*D^mW(G)
 =2\beta D\beta*A(G)D^{m+1}G+\text{tame remainder},
\tag{3.8}
\]
and the displayed term is absorbed by $\mathcal D_m^G$.

Second, all $m$ derivatives can hit $D(\beta^2)$.  By (2.8), its only derivative above the energy is $2\beta D^{m+1}\beta$.  In the metric energy it occurs as
\[
 \int D^mG*\beta D^{m+1}\beta*W(G).
\tag{3.9}
\]
Integrating the ordered top derivative once gives
\[
 -\int \beta D^{m+1}G*D^m\beta*W
 -\int D^mG*D\beta*D^m\beta*W
 -\int D^mG*\beta D^m\beta*DW.
\tag{3.10}
\]
The first term is absorbed by weighted Young; the other two are bounded by $C_{m,R}\mathcal E_m$.  Every intermediate allocation has all factors of order at most $m$ and total order at most $m+2$, so (2.6) applies.  No $D^{m+1}\beta$ remains and no inverse power of $\varepsilon$ is introduced.

### 3.4 Transport term

Let $V=\beta^2W(G)$.  The top advective term satisfies
\[
 \int D^m\beta\,V\cdot D^{m+1}\beta
 =-\frac12\int \operatorname{div}_{\bar g}V\,|D^m\beta|^2+	ext{background commutators}.
\tag{3.11}
\]
The top metric coupling is
\[
 \int D^m\beta\,\beta^2A(G)D^{m+1}G*D\beta,
\tag{3.12}
\]
and
\[
 |(3.12)|\le\zeta\mathcal D_m^G+C_{m,R,\zeta}\|\beta\|_{H^m}^2,
\tag{3.13}
\]
because $\beta^4/(\beta^2+\varepsilon)\le1$.  After these two allocations are removed, the differentiated transport nonlinearity is a tame remainder of the form (2.5), hence contributes $C_{m,R}(1+\mathcal E_m)$.

Finally, $\nu\bar\Delta\beta$ contributes
\[
 -\nu\|D^{m+1}\beta\|_2^2+C_m\nu\|\beta\|_{H^m}^2,
\tag{3.14}
\]
where the second term contains only fixed-background curvature commutators.  Equations (3.3)–(3.14), with the finitely many $\zeta$ chosen small, prove (3.2).

## 4. One common low-order interval and all higher orders

At $m=s_0$, do not assume (2.2) in advance.  The same calculation gives a locally bounded polynomial inequality
\[
 \mathcal E_{s_0}'+c\mathcal D_{s_0}^G+c\mathcal D_{s_0}^\beta
 \le P_{s_0}(1+\mathcal E_{s_0}),
\tag{4.1}
\]
uniformly in $(\varepsilon,\nu)$.  Also the equations give
\[
 \|\partial_tG\|_{H^{s_0-2}}+\|\partial_t\beta\|_{H^{s_0-2}}
 \le P_{s_0}(1+\mathcal E_{s_0}),
\tag{4.2}
\]
again without negative regularization powers.  Sobolev embedding and (4.2) keep $G$ in a fixed positive metric neighborhood for sufficiently small
\[
 T_0=T_0(g_0,\chi,\bar g,s_0)>0.
\tag{4.3}
\]
An ODE comparison in (4.1) keeps $\mathcal E_{s_0}\le R^2$ on $[0,T_0]$.

For fixed positive $(\varepsilon,\nu)$, standard strongly parabolic theory supplies a solution initially.  If its maximal time were below $T_0$, the $H^{s_0}$ bound and metric positivity above would satisfy the fixed-parameter continuation theorem, contradicting maximality.  Thus every regularized solution reaches the same **per-datum** interval $[0,T_0]$.

Now fix any $m>s_0$.  On this already constructed interval, (3.2) has coefficient $C_{m,R}$ depending only on the low norm bound and the fixed smooth initial datum.  Grönwall gives
\[
 \sup_{t\le T_0}\mathcal E_m(t)
 +\int_0^{T_0}(\mathcal D_m^G+\mathcal D_m^\beta)dt
 \le C_m(g_0,\chi,T_0),
\tag{4.4}
\]
uniformly in $(\varepsilon,\nu)$.  The interval does not shrink with $m$.  This is the required tame feature: high energies enter linearly, while the coefficient is determined by the fixed low energy.

For fixed positive $(\varepsilon,\nu)$, the principal symbol of (1.2) is diagonal with blocks
\[
 (\beta^2+\varepsilon)G^{ab}\xi_a\xi_b I_{\mathrm{Sym}^2}
 \quad\text{and}\quad
 \nu\bar g^{ab}\xi_a\xi_b,
\]
so standard quasilinear strongly parabolic theory on a closed manifold gives the smooth solution and its fixed-parameter continuation theorem.  This is the construction used here.  A background spectral Galerkin shortcut is **not** asserted: such a projection need not commute with $D$, preserve pointwise positivity, or preserve the maximum principle without additional commutator work.  The scalar-viscosity version has the advantage that (1.3) follows directly from the maximum principle before either regularization is removed.

## 5. Smooth limit and geometric pullback

From (1.2) and (4.4),
\[
 \|\partial_tG\|_{H^{m-2}}+\|\partial_t\beta\|_{H^{m-2}}\le C_m
\tag{5.1}
\]
for every $m$.  Repeated time differentiation uses only higher spatial bounds and the factors $0<\varepsilon,\nu\le1$; it never divides by them.  Hence a diagonal sequence $(\varepsilon_j,\nu_j)\to(0,0)$ converges in every space-time $C^k$ norm to a smooth pair $(G,\beta)$ solving (1.1) on $[0,T_0]$.  In particular,
\[
 \varepsilon_j\bigl[G_j^{-1}D^2G_j+R(G_j,G_j)+Q(G_j,DG_j)\bigr]\to0,
 \qquad \nu_j\bar\Delta\beta_j\to0
\tag{5.2}
\]
in every fixed $C^k$ norm after invoking sufficiently high spatial estimates.

Let $\varphi$ solve
\[
 \partial_t\varphi(t,x)=-\beta(t,\varphi(t,x))^2W(G)(t,\varphi(t,x)),
 \qquad\varphi(0,x)=x.
\tag{5.3}
\]
Then $\beta(t,\varphi(t,x))=\chi(x)$, and $g=\varphi^*G$ satisfies
\[
 \partial_tg=-2\chi^2(\operatorname{Ric}_g+g),\qquad g(0)=g_0.
\tag{5.4}
\]
This proves existence of at least one smooth per-datum exact flow.  The restricted Ishida–LeBrun argument needs existence and restart, not canonical uniqueness.  A full uniqueness statement can be added only after the branch-oriented difference ledger is independently completed for arbitrary smooth solutions.

## 6. Correct interface with collapse-uniform first exit

### 6.1 Critical curvature energy is unweighted

For
\[
 F_T=(1+|T|^2)^{1/2},\qquad T=\operatorname{Rm}+\frac{g\owedge g}{2(n-1)},
\]
the hierarchy is
\[
 H_q^\alpha(t)=\int\eta_\alpha^2a^{q-2}F_T^q\,d\mu_t.
\tag{6.1}
\]
Therefore
\[
 \boxed{H_2^\alpha(t)=\int\eta_\alpha^2F_T^2\,d\mu_t}
\tag{6.2}
\]
is unweighted in $a$.  This is essential: it controls curvature throughout the matched $\eta_\alpha$ support, including small-$a$ collars.  Since
\[
 1+|T|^2\asymp_n1+|\operatorname{Rm}|^2
\tag{6.2a}
\]
(the added `1` is essential, e.g. when $\operatorname{Rm}=-G$), the initial maximal-function bound gives
\[
 H_2^\alpha(0)\le C(1+\kappa_0^2)\operatorname{Vol}B_{7r}(x_\alpha),
\quad
 \mathcal S_\alpha H_2^\alpha(0)^{1/2}\le Cr^2\sqrt{1+\kappa_0^2}.
\tag{6.3}
\]
An energy with an inserted factor $a$ is weaker and cannot be substituted into the Sobolev absorption.

### 6.2 Global defect includes the stationary remainder

Use one consistent buffered geometry, for example
\[
 \chi_\alpha=1\ \text{on }B_{5r}(x_\alpha),\quad
 \operatorname{supp}\chi_\alpha\subset B_{6r}(x_\alpha),\quad
 \eta_\alpha=1\ \text{on }B_{6r}(x_\alpha),\quad
 \operatorname{supp}\eta_\alpha\subset B_{7r}(x_\alpha),
\]
with the $B_{7r}(x_\alpha)$ pairwise disjoint and the maximal-function bound available through radius $7r$.  Define $\chi=\sum_\alpha\chi_\alpha$ and put
\[
 a=\chi^2=\sum_\alpha\chi_\alpha^2,
\]
where the last equality uses disjointness of the inner supports.  Put
\[
 \rho=\sum_\alpha\eta_\alpha^2,\qquad
 Q_\alpha(t)=\int\eta_\alpha^2|E(t)|^2d\mu_t,
\qquad
 Q_{\rm rest}(t)=\int(1-\rho)|E(t)|^2d\mu_t.
\tag{6.4}
\]
Because $\eta_\alpha=1$ on a neighborhood of every active support, $1-\rho$ is supported in an open region where $a=0$.  The exact flow and all its spatial jets are stationary there, so
\[
 Q_{\rm rest}(t)=Q_{\rm rest}(0).
\tag{6.5}
\]
The correct identity is
\[
 \boxed{Q_{\rm global}(t)=Q_{\rm rest}(0)+\sum_\alpha Q_\alpha(t).}
\tag{6.6}
\]
If $Q_\alpha(t)\le e^{Ct/r^2}Q_\alpha(0)$, then
\[
 Q_{\rm global}(t)
 \le Q_{\rm rest}(0)+e^{Ct/r^2}\sum_\alpha Q_\alpha(0)
 \le e^{Ct/r^2}Q_{\rm global}(0).
\tag{6.7}
\]
The selected supports need not cover $M$.

### 6.3 Per-datum start, uniform first exit, positive-time continuation

The local time $T_i$ produced by (4.3) depends on high Sobolev norms and higher cutoff jets of datum $i$.  A curvature-to-volume budget supplies neither, so no sequence-uniform lower bound for $T_i$ follows from the local theorem.

Instead, for each datum start its exact flow for some $T_i>0$ and use every available smooth endpoint restart to form a maximal extendible smooth branch; let $T_i^*$ denote its right endpoint.  On
\[
 (0,\min\{T_i^*,\theta r^2\})
\]
run only the first-exit estimates whose constants use legitimate uniform inputs: the unweighted $H_2$, local Sobolev coefficient, $|d\chi|\lesssim r^{-1}$, initial Ricci defect, and fixed support buffers.  They yield
\[
 \|aF_T(t)\|_\infty\le C\gamma/t,
 \qquad
 \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3},
\tag{6.8}
\]
and strict improvement of the $H_2$, drift, Sobolev, and support conditions.

If $T_i^*<\theta r^2$, then on the terminal slab $[T_i^*/2,T_i^*)$ the first estimate in (6.8) is finite (although not uniform as $T_i^*\downarrow0$).  The per-datum staggered continuation hierarchy
\[
 T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
 \longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots
\tag{6.9}
\]
then gives a smooth endpoint and the local theorem restarts the flow, contradicting maximality of $T_i^*$.  Consequently every datum reaches the common observation time $\theta r^2$, while no high initial Sobolev norm or higher cutoff jet enters the sequence-uniform Grönwall estimates.

## 7. Scope

The direct construction now has the right analytical division of labor:

- low-order tame energy gives a common interval for all regularizations of one datum;
- arbitrary-order tame propagation gives a smooth degenerate limit on that interval;
- unweighted critical first-exit estimates, not initial high Sobolev bounds, provide collapse-uniform time;
- positive-time shifted-curvature continuation bridges any short per-datum local lifespan;
- the stationary remainder preserves the global topological defect quantity.

The TTCS verification at `trace/ttcs/results/step56_ttcs01_verifier1_integration.md` independently reconstructed the tame exponent count and all four top-order families.  It required the corrections now incorporated here: deleting the unsupported spectral-Galerkin shortcut, adding the vanished $\varepsilon R$ and $\varepsilon Q$ terms in the limit, and restricting the conclusion to existence.  The interface verification at `trace/ttcs/results/step56_ttcs01_verifier2_integration.md` required the corrected shifted-curvature comparison, strict buffers, and maximal-branch wording, also incorporated.  The allocation script checks 14,002,305 finite partitions with zero failures.

The first-exit outputs (6.8) are not reproved in this note.  Their use remains conditional on the exact unweighted $H_2$, $Y$, $J_6$, and local $Q_\alpha$ inequalities having only first-cutoff-derivative constants after signed Hessian integration by parts.  In particular, no direct $\|\nabla^2\chi\|_\infty$ or higher-jet constant may enter the collapse-uniform estimates.

This is an analytic component of the restricted four-dimensional negative Ishida–LeBrun route.  It does not settle the positive branch, arbitrary four-manifold topology, dimensions $n\ge5$, dimension-only pinching constants, or the complete Yau Problem 26 statement.