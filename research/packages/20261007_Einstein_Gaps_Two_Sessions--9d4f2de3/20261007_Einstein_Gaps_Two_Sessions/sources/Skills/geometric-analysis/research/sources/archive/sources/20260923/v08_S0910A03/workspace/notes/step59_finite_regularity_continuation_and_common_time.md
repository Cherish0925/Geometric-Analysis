# Step 59: Finite-regularity continuation bridge and common observation time

> **Step 60 superseding correction.**  Sections 3--4 preserve the finite-order
> current-pair estimates, but Section 5's restart from times $t_j<T^*$ cannot
> use "standard uniqueness on the overlap": the ungauged Ricci principal symbol
> has second-order gauge terms, and the proposed direct $L^2$ estimate is false.
> The corrected continuation uses the arbitrary-order tensor-family
> classification, obtains a $C^\infty$ terminal metric, and splices a restart at
> $T^*$ by matching all PDE-generated time jets, without uniqueness.  See
> `step60_all_order_continuation_and_terminal_chart.md`.  Consequently the
> common-time conclusions below are conditional on that corrected all-order
> continuation and on the Step 56 local construction.

Session: S0910A03. Agent2 / Constructor. Phase: Execute.

## 0. Purpose

This note develops the finite-threshold part of the positive-time continuation
bridge for the exact normalized cutoff flow on a closed four-manifold.  It turns the Step 58
curvature endpoint into smooth extension past any putative finite maximal time,
then derives the common observation time that every datum in the Ishida–LeBrun
sequence needs.

The construction uses:

- the curvature endpoint $\|aF_T(t)\|_\infty\le C\Gamma/t$ (Step 58);
- the $W^{1,p}\to L^\infty$ bridge (Step 57, Prop.\ 9.1);
- the collar-safe staggered induction at every finite level (Step 40; A01 Step 55);
- the fixed-background connection conversion (A01 Step 55, §1);
- the per-datum restart from Step 56 Theorem 4.3.

The assembly is self-contained modulo those inputs.  All constants below are
per-datum and may depend on the positive-time slab, the datum's Sobolev
constant, and the finite norms of previous levels; they are **not** entered into
the sequence-uniform first-exit chain.

---

## 1. Standing hypotheses

On a closed Riemannian four-manifold $(M^4,g_0)$, the exact normalized cutoff
flow is
\[
 \partial_tg=-2aE,\qquad E=\operatorname{Ric}_g+g,\qquad a=\chi^2,
\tag{1.1}
\]
where $\chi$ is a fixed smooth cutoff with $|d\chi|\le C_\chi/r$,
$\operatorname{supp}\chi\subset B_{6r}$.  Shifted curvature and weighted
curvature:
\[
 G=\frac{g\owedge g}{6},\qquad T=\operatorname{Rm}+G,\qquad
 U=aT,\qquad F_T=(1+|T|^2)^{1/2}.
\tag{1.2}
\]
Step 56 Theorem 4.3 gives a smooth solution on $[0,T_0)$ with $T_0>0$
depending on the datum $(g_0,\chi)$.  Restart at every smooth endpoint
forms a maximal smooth branch $[0,T^*)$.

**First-exit hypothesis.**  On $(0,\min\{T^*,\theta r^2\})$ the first-exit
curvature estimate
\[
 \|aF_T(t)\|_\infty\le\frac{C_0\Gamma}{t}
\tag{1.3}
\]
holds with $\Gamma=\sup_{(0,t)}\mathcal S(s)H(s)^{1/2}$ bounded by a small
threshold $\Gamma_*$.  This is the Step 58 curvature endpoint; it depends on
$n=4$, $r$, $|d\chi|_\infty$, $H(0)$, and $\mathcal S(0)$ only—no $Y(0)$,
no high Sobolev norm.  The base pair
\[
 T_0,\,\nabla T,\,\nabla U,\,\nabla^2\chi
 \in L^\infty_tL^q_x\quad\forall q<\infty
\tag{1.4}
\]
is supplied by Step 56 supplement on every positive-time slab with $|U|_\infty<\infty$.

**Goal.**  Prove: if $T^*<\theta r^2$, the flow extends smoothly past $T^*$.

---

## 2. Pointwise curvature from the $W^{1,p}$ bridge

Fix any $\tau\in(0,T^*)$.  On $[\tau,T^*)$, (1.3) gives
\[
 \|U(t)\|_\infty\le\frac{C_0\Gamma}{\tau}=:K_\tau<\infty.
\tag{2.1}
\]
Bilipschitz equivalence:
$e^{-2K_\tau(T^*-\tau)}g(\tau)\le g(t)\le e^{2K_\tau(T^*-\tau)}g(\tau)$.
On this slab, the base pair (1.4) holds with constants depending on $K_\tau$.

**Step 1: $T\in L^q$ for all $q$ (Step 56 eq.\ 1.1).**
The unweighted $T$-energy satisfies
\[
 \frac d{dt}\|T\|_q^q+c\int a|\nabla T|^2|T|^{q-2}
 \le C_{K_\tau}\|T\|_q^q+C\operatorname{Vol},
\tag{2.2}
\]
giving $T\in L^\infty([\tau,T^*];L^q)$ for every finite $q$.

**Step 2: $(U_1,C_2)\in L^q$, then $\nabla T\in L^q$ (Step 56 supplement).**
The base pair Grönwall with coefficient $C_{K_\tau}$ closes by signed Hessian
integration.  Subsequently,
\[
 \frac d{dt}\|\nabla T\|_p^p+cD_p^T
 \le C_{K_\tau}(1+\|\nabla T\|_p^p+\|T\|_{2p}^{2p}+\|U_1\|_{2p}^{2p}
       +\|C_2\|_{2p}^{2p}),
\tag{2.3}
\]
giving $\nabla T\in L^\infty([\tau,T^*];L^p)$ for all $p$.

**Step 3: Kato + Sobolev.**  For $p>4$,
\[
 \|T(t)\|_\infty
 \le C_S\bigl(\|T(t)\|_p+\|\nabla T(t)\|_p\bigr)<\infty,
\tag{2.4}
\]
where $C_S=C_S(M,g(\tau),K_\tau,p)$ is per-datum.  Hence
\[
 |\operatorname{Rm}(t)|\le|T(t)|+|G|\le C_\tau
 \qquad\text{on }[\tau,T^*].
\tag{2.5}
\]

---

## 3. Finite staggered induction through the restart threshold

### 3.0 Target

For $n=4$, the Step 56 restart needs $H^{s_0}$ data with $s_0>n/2+4=6$.
Choose $s_0=7$.  The sufficient restart package (A01 Step 55, eq.\ 1.6) is
\[
 T_k\in L^p\ (0\le k\le6),\qquad
 (U_k,C_{k+1})\in L^p\ (1\le k\le7),
\tag{3.0}
\]
for some fixed $p>4$ on the slab $[\tau,T^*]$.

The base pair gives $k=0,1$:
$T_0,T_1,(U_1,C_2)\in L^q$ for all $q$.  The induction starts at $k=2$.

### 3.1 The weighted pair at level $m\ge2$

Write $U_m=\nabla^mU$, $C_j=\nabla^j\chi$, $P(V)=|V|^{p-2}V$,
$D_{m,p}^U=\int a|\nabla U_m|^2|U_m|^{p-2}$.

**Inductive input:** $U_j,C_{j+1},T_j\in L^q$ for all $j<m$ and all $q<\infty$;
also $U_0\in L^\infty$ and $|T|_\infty\le C_\tau$ from §2.

The evolution of $U_m$ has the schematic form (Step 40, eq.\ 1.4)
\[
 \partial_tU_m=\operatorname{div}(a\nabla U_m)
 +\chi C_{m+2}*U
 +\chi C_{m+1}*U_1
 +\chi C_2*U_m
 +C_1*C_1*U_m
 +\mathcal P_m,
\tag{3.1}
\]
where $\mathcal P_m$ contains only previous-level quantities at finite exponents,
products with bounded coefficient $|U|\le K_\tau$, and normalization/commutator
terms.  The notation groups $\operatorname{div}(a\nabla U_m)$ without isolating
the drift $2\chi C_1*\nabla U_m$ (TTCS correction from A01).

**Term 1: Top cutoff $\chi C_{m+2}*U$.**
One integration by parts lowers the jet:
\[
\begin{aligned}
 \int P(U_m)*\chi C_{m+2}*U
 ={}&-\int\nabla P(U_m)*\chi C_{m+1}*U\\
 &-\int P(U_m)*C_1*C_{m+1}*U\\
 &-\int P(U_m)*\chi C_{m+1}*U_1.
\end{aligned}
\tag{3.2}
\]
First line: $\le\varepsilon D_{m,p}^U+C_{K_\tau}(\|C_{m+1}\|_p^p+\|U_m\|_p^p)$.
Second line: $|C_1|,|U|\le C$, so same-exponent Young.

Third line (the residual): set $f=\chi|U_m|^{p/2}$.  Then (A01 Step 55, eqs.\
2.8--2.13)
\[
\begin{aligned}
 I_{\rm res}&=\int\chi|C_{m+1}|\,|U_1|\,|U_m|^{p-1}\\
 &\le\|f\|_4\,\|C_{m+1}\|_p\,\|U_1\|_4\,\|U_m\|_p^{p/2-1},
\end{aligned}
\tag{3.3}
\]
with Sobolev on $f$:
\[
 \|f\|_4^2\le C_S\bigl(p^2D_{m,p}^U+C_{p,r}\|U_m\|_p^p\bigr).
\tag{3.4}
\]
Since $U_1\in L^4$ on $[\tau,T^*]$ with per-datum constant, Young gives
\[
 I_{\rm res}\le\varepsilon D_{m,p}^U
 +C_{m,p,\tau}(1+\|C_{m+1}\|_p^p+\|U_m\|_p^p).
\tag{3.5}
\]

**Term 2: Current signed-Hessian $\chi C_2*U_m$.**
This is not a bounded-coefficient term because $C_2$ is only in $L^q$.
The signed-Hessian lemma (Step 38, A01 eq.\ 2.13b) gives
\[
 \left|\int\chi(C_2)_{ij}B^{ij}(U_m)\right|
 \le\varepsilon D_{m,p}^U+C_{p,\varepsilon}\|C_1\|_\infty^2\|U_m\|_p^p
 \le\varepsilon D_{m,p}^U+\frac C{r^2}\|U_m\|_p^p.
\tag{3.6}
\]

**Term 3: $C_1*C_1*U_m$.**  Bounded coefficient, $\le C/r^2\,\|U_m\|_p^p$.

**Term 4: $\chi C_{m+1}*U_1$ (direct, not from the top cutoff).**
Same Hölder–Sobolev mechanism as the residual (3.3).

**Term 5: Lower products $\mathcal P_m$.**
Each monomial has the form $A_1*\cdots*A_N*|U_m|^{p-1}$ with every $A_j$
either bounded ($|U|,|C_1|$), or a previous-level quantity in $L^{Np}$.
Hölder with exponents $(Np,\ldots,Np,p/(p-1))$ closes each.  The curvature
coefficient $|T|_\infty\le C_\tau$ also simplifies products containing
$aT^k$ terms.

**Weighted pair closure.**  Combining all terms,
\[
 \frac d{dt}\|U_m\|_p^p+cD_{m,p}^U
 \le C_{m,p,\tau}(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p).
\tag{3.7}
\]

For the cutoff jet, $C_{m+1}=\nabla^{m+1}\chi$ evolves by connection variation
(Step 40, eq.\ 2.10):
\[
 \partial_tC_{m+1}
 =C_1*U_m+\sum_{1\le j<m}C_{m+1-j}*U_j
  +\text{previous-level curvature commutators}.
\tag{3.8}
\]
The leading term is $C_1*U_m$, which is same-exponent; all other products
involve two previous-level factors.  Hence
\[
 \frac d{dt}\|C_{m+1}\|_p^p
 \le C_{m,p,\tau}(1+\|C_{m+1}\|_p^p+\|U_m\|_p^p).
\tag{3.9}
\]

Adding (3.7) and (3.9):
\[
 \boxed{
 \frac d{dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)+cD_{m,p}^U
 \le C_{m,p,\tau}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).}
\tag{3.10}
\]
Grönwall gives $(U_m,C_{m+1})\in L^\infty([\tau,T^*];L^p)$ for every finite $p$.

### 3.2 The unweighted $T_m$ at level $m\ge2$

After $(U_m,C_{m+1})$ is known, the $m$-th curvature derivative $T_m=\nabla^mT$
has the top cutoff term (Step 40, eq.\ 3.2)
\[
 \nabla^{m+2}a*T=2\chi C_{m+2}*T
 +\sum_{s=1}^{m+1}C_s*C_{m+2-s}*T.
\tag{3.11}
\]
The sum uses jets $\le C_{m+1}$ (known).  For $\chi C_{m+2}*T$, integrate once:
\[
\begin{aligned}
 \int |T_m|^{p-2}T_m*\chi C_{m+2}*T
 ={}&-\int\nabla(|T_m|^{p-2}T_m)*\chi C_{m+1}*T\\
 &-\int |T_m|^{p-2}T_m*\chi C_{m+1}*T_1+\text{lower}.
\end{aligned}
\tag{3.12}
\]
First line: $\le\varepsilon D_{T_m,p}+C(\|C_{m+1}\|_p^p+\|T_m\|_p^p)$, using
$|T|\le C_\tau$.  Second line:  same Hölder–Sobolev structure as (3.3)
with $T_1\in L^4$ in place of $U_1$.  The current signed-Hessian $\chi C_2*T_m$
is handled by the same lemma (3.6).

All remaining terms involve previous levels plus the bounded $|T|$ and $|U|$:
\[
 \frac d{dt}\|T_m\|_p^p+cD_{T_m,p}
 \le C_{m,p,\tau}(1+\|T_m\|_p^p).
\tag{3.13}
\]
Grönwall gives $T_m\in L^\infty([\tau,T^*];L^p)$ for every $p$.

### 3.3 Induction closure

The staggered ordering is
\[
 T_0\to(U_1,C_2)\to T_1
 \to(U_2,C_3)\to T_2
 \to\cdots
 \to(U_7,C_8)\to T_6.
\tag{3.14}
\]
At each transition, the inputs from the previous stage are in $L^q$ for all $q$,
and the current stage satisfies a Grönwall inequality (3.10) or (3.13) with
per-datum constants.  After $7$ weighted pairs and $7$ unweighted curvature
levels (including the base), the restart package (3.0) is complete.

**Structural properties verified at every level $m$:**

(i) The only cutoff jet above the current pair is $\chi C_{m+2}$, and it
    is integrated once. (Step 40, §2.2)

(ii) The residual after integration involves $U_1$ at exponent $4$ (or $T_1$
     for the $T_m$ equation); not any higher $U_j$ at the current level.

(iii) The current signed-Hessian $\chi C_2*U_m$ and $\chi C_2*T_m$ are
      absorbed by the Step 38 lemma with coefficient $C/r^2$.

(iv) All honest expansion of $\nabla^ra=\sum C_s*C_{r-s}$ is performed;
     no false $\chi$ factor is inserted.  (Step 40, eq.\ 1.8)

(v) No current quantity appears at an enlarged exponent; the system
    is finite-triangular, not an infinite exponent ascent.  (Step 40, §4)

---

## 4. Fixed-background $H^{s_0}$ conversion

Fix $\bar\nabla=\nabla^{g(\tau)}$ and
\[
 A(t)=\nabla^{g(t)}-\bar\nabla.
\tag{4.1}
\]
The connection evolution is (A01 eq.\ 1.1)
\[
 \partial_tA=g^{-1}*\bar\nabla(aE)+P_0(A,U,g^{-1})
 =g^{-1}*U_1+P_0(A,U,g^{-1}),
\tag{4.2}
\]
where $P_0$ is polynomial in $A,U,g^{-1}$ with no highest derivative.
Since $|U|\le K_\tau$ and $U_1\in L^p$ for all $p$, this is a semilinear ODE
for $A$ in $L^p$:
\[
 \|A(t)\|_p\le\int_\tau^t C(K_\tau,\|A(s)\|_p)\,\|U_1(s)\|_p\,ds.
\tag{4.3}
\]
Grönwall gives $A\in L^\infty([\tau,T^*];L^p)$.

At higher orders, applying $\bar\nabla^m$ to (4.2) gives (A01 eq.\ 1.2,
corrected per TTCS)
\[
 \bar\nabla^m\partial_tA
 =g^{-1}*U_{m+1}
 +B_0*A_m
 +P_m(A_{<m};U_{\le m};g^{-1}),
\tag{4.4}
\]
where $A_j=\bar\nabla^jA$, $B_0$ is a bounded zero-order coefficient from
$g^{-1},U$, and $P_m$ is polynomial in previous levels.  The $B_0*A_m$ term
arises from $\bar\nabla^m(g^{-1}*A*U)$ by Leibniz; it is linear at current
order with bounded coefficient and does not cause derivative loss.
Since $U_{m+1}\in L^p$ for $m+1\le s_0=7$ and all previous $A_j\in L^p$,
the triangular Grönwall gives
\[
 A_m\in L^\infty([\tau,T^*];L^p)\quad\text{for }0\le m\le s_0-1=6.
\tag{4.5}
\]
Using $\bar\nabla^{m+1}g=(\bar\nabla^mA)*g+\text{lower }A$-products
(A01 eq.\ 1.3), we get
\[
 g(t)\in H^{s_0}(M,g(\tau))\quad\text{uniformly on }[\tau,T^*].
\tag{4.6}
\]

---

## 5. Smooth extension past $T^*$

**Existence of limit.**  On $[\tau,T^*]$,
\[
 \|\partial_tg(t)\|_{H^{s_0-2}}
 =\|2aE(t)\|_{H^{s_0-2}}
 \le C_{s_0,\tau}(1+\|U(t)\|_{H^{s_0-2}}),
\tag{5.1}
\]
which is bounded by the staggered induction.  Hence $g(t)$ is Lipschitz in
$H^{s_0-2}$ and converges to a limit $g(T^*)\in H^{s_0-2}$.  Since
$g(t)\in H^{s_0}$ uniformly, weak-$*$ compactness gives
$g(T^*)\in H^{s_0}$.

**Positive definiteness.**  Bilipschitz equivalence (§2)
ensures $e^{-C}g(\tau)\le g(T^*)\le e^Cg(\tau)$, so the limit metric is
positive definite.

**Cutoff regularity.** $\chi$ is a fixed smooth function, so
$\|\chi\|_{H^{s_0}}\le C_\chi$ is a constant of the datum.  The
transported-cutoff energy $\|\beta\|_{H^{s_0}}$ is controlled by
$\|\chi\|_{H^{s_0}}$ plus the diffeomorphism regularity, which is bounded
by $A\in H^{s_0-1}$.

**Restart.**  Take a sequence $t_j\uparrow T^*$.  Each $g(t_j)$ is smooth and
has $\|g(t_j)\|_{H^{s_0}}\le R$ and $\lambda g(\tau)\le g(t_j)\le\lambda^{-1}
g(\tau)$ uniformly.  If the Step 56 local theorem's lifespan depends only
on the $H^{s_0}$ radius, ellipticity, and the fixed smooth $\chi$, then
all $g(t_j)$ share a common positive lifespan lower bound $T_1>0$.  For
$j$ large enough, $t_j+T_1>T^*$, so the restarted branch exists beyond
$T^*$.  This finite-threshold argument by itself does **not** identify it with
the old branch on an overlap: ungauged uniqueness was not established.  Step 60
replaces this paragraph by an arbitrary-order $C^\infty$ terminal limit and a
direct splice at $T^*$ with matching autonomous-PDE time jets.

The displayed implication is recovered only after importing Step 60's
all-order terminal-splice argument:
\[
 \boxed{T^*<\theta r^2\implies\text{flow extends past }T^*
 \implies\text{contradiction with maximality.}}
\tag{5.2}
\]
Thus, conditional on that all-order module, $T^*\ge\theta r^2$ and the flow
exists smoothly on $[0,\theta r^2]$.

---

## 6. Common observation time

For the Ishida–LeBrun sequence $(M,g_i)$ with
$\delta_i=\|\operatorname{Ric}_{g_i}+g_i\|_\infty\to0$, the complete
argument is:

**(a) Support selection and cutoff.**  Choose $r$ so that $\gamma_i(0)=
\mathcal S_i(0)H_i(0)^{1/2}\le\gamma_*$ on each selected support
(Step 30 coloring).

**(b) Per-datum flow start.**  Step 56 Theorem 4.3 starts each flow for
$T_i>0$.  Form maximal smooth branch $[0,T_i^*)$.

**(c) First-exit estimates on $(0,\min\{T_i^*,\theta r^2\})$.**
The Step 58 curvature branch gives:
\[
 H_i(t)\le e^{C\theta}H_i(0),
 \quad\int_0^tD_i\le CH_i(0),
 \quad\int_0^tY_i\le C\Gamma_iH_i(0),
\tag{6.1}
\]
\[
 Y_i(t)\le C\Gamma_iH_i(0)/t,
 \qquad
 \|aF_T(t)\|_\infty\le C\Gamma_i/t.
\tag{6.2}
\]
No $Y_i(0)$, high Sobolev norm, or higher cutoff jet enters these bounds.
The coupled defect ladder gives, under small $\gamma$,
\[
 Q_{i,\alpha}(t)\le e^{C(1+r^{-2})t}Q_{i,\alpha}(0),
 \qquad J_{6,i,\alpha}(t)\le e^{C(1+r^{-2})t}J_{6,i,\alpha}(0).
\tag{6.3}
\]
The defect Moser endpoint gives (Step 39, eq.\ 8.3)
\[
 \|aE_i(t)\|_\infty\le C\delta_i\!\left(\frac{r^2}t\right)^{\!1/3},
\tag{6.4}
\]
which is integrable near $t=0$.  The time power $1/3$ comes from the
four-dimensional Moser iteration starting at $p_0=6$ ($=J_6$ exponent);
the mechanism is Step 39 Theorem 7.1 with three-factor Hölder and the
curvature input $\mathcal S^2Y\le C\Gamma^3/t$ from Step 58.

**(d) Metric drift and Sobolev transport (A01 Step 55).**
\[
 V_i(t)=\int_0^t\|aE_i\|_\infty
 \le C\delta_i r^{2/3}\cdot\tfrac32 t^{2/3}.
\tag{6.5}
\]
At $t=\theta r^2$:
\[
 V_i(\theta r^2)\le C\delta_i\,\theta^{2/3}r^2.
\tag{6.5a}
\]
\[
 \mathcal S_i(t)\le e^{8V_i}\mathcal S_i(0),\qquad
 \gamma_i(t)\le\gamma_i(0)\exp\{4V_i+C\theta\}.
\tag{6.6}
\]
For $\delta_i$ small and $\theta$ small, $\gamma_i(t)\le\gamma_*$ and
$V_i\le V_*$.  The bootstrap closes.

**(e) Continuation.**  If $T_i^*<\theta r^2$, then on $[T_i^*/2,T_i^*)$
the curvature endpoint and the $W^{1,p}$ bridge give $|T_i|_\infty<\infty$.
The finite staggered induction (§3) and fixed-background conversion (§4)
give $g_i(T_i^*)\in H^{s_0}$, positive definite.  Step 56 restarts.
Contradiction.

**(f) Conclusion.**
\[
 \boxed{
 \text{Every datum }g_i\text{ reaches the common observation time }\theta r^2.}
\tag{6.7}
\]

**(g) Global defect decomposition.**
\[
 Q_{\rm global,i}(t)=Q_{\rm rest,i}(0)+\sum_\alpha Q_{i,\alpha}(t)
 \le e^{C\theta}Q_{\rm global,i}(0),
\tag{6.8}
\]
where $Q_{\rm rest,i}(0)=\int(1-\sum\eta_\alpha^2)|E_i|^2\,d\mu_0$
is stationary because $a=0$ on its support.

---

## 7. Conditional restricted IL chain

Assembling the curvature branch, continuation bridge, and terminal density:

**Theorem (Conditional).**  *Let $M=(\#_j X_j)\#N$ be a closed oriented
four-manifold in the Ishida–LeBrun geography with monopole sign-family
hypothesis, supercritical parameter $\sigma=D-A/3\ge0$, and $D\ge A/3$.
If the following analytic inputs are complete:*

*(i) Per-datum smooth flow existence (Step 56);*

*(ii) Curvature first-exit chain: $H_2\to Y\to$ curvature Moser
$\|aF_T\|_\infty\le C\Gamma/t$ (Step 58);*

*(iii) Defect first-exit chain: $Q\to J_6\to$ defect Moser $\|aE\|_\infty\le
C\delta\phi(t)$ (Step 39 adapted);*

*(iv) Terminal spectral density: $\int\mathfrak D\le119Q+912\pi^2(-q_{\rm top})_+$
(Step 43);*

*(v) Buffered-center Liouville averaging, exponential-pullback compactness,
   and the spectral projector contradiction (Step 60 and Step 6);*

*then there exists $\delta_0>0$, depending on the specified geography data,
such that no smooth input metric on these already no-Einstein manifolds can
satisfy $\|g^{-1}(\operatorname{Ric}_g+g)\|_{L^\infty,\mathrm{op}}<\delta_0$.
Equivalently, the normalized negative Ricci cone has a positive input-metric
gap on this family.*

**Correction on the scale $A$.**  The terminal density upper bound is
$O(\delta^2A)$ while the eligible-center volume is $\ge c_0A$; their ratio is
$O(\delta^2)$, so this mechanism does not force a $c/\sqrt A$ deterioration.
Uniformity remains conditional on the geography-dependent constants
$c_0,K,\rho$ and the calibrated volume/support inputs.  It therefore still
does not provide dimension-only constants $c_4,C_4$.

---

## 8. Interface verification

The following quantities enter the **sequence-uniform** first-exit chain:

| Input | Where it enters | Status |
|:------|:----------------|:-------|
| $n=4$ | everywhere | fixed |
| $r$, $\|d\chi\|\le C/r$ | support scale | from coloring |
| $H_i(0)\lesssim K_0\operatorname{Vol}(B_{7r})$ | critical energy | initial data |
| $\mathcal S_i(0)\lesssim r^2\operatorname{Vol}(B_{7r})^{-1/2}$ | Sobolev const | initial data |
| $\gamma_i(0)\lesssim r^2\sqrt{K_0}$ | critical parameter | collapse-independent |
| $\delta_i=\|E_i\|_\infty$ | defect | initial pinching |
| $Q_i(0)=\int|E_i|^2\le C\delta_i^2\operatorname{Vol}$ | defect energy | initial |
| $J_{6,i}(0)\le C\delta_i^4 Q_i(0)$ | defect sixth moment | initial |

**Not entered** into the sequence-uniform chain:
- $Y_i(0)$: removed by Step 58 relative bridge
- High Sobolev norms of $g_i$: only $H_i(0)$ appears
- Higher cutoff jets $\|\nabla^k\chi\|$ for $k\ge2$: only $|d\chi|$ appears
- Per-datum Sobolev constant of $g(\tau)$: enters only continuation (§5)
- Per-datum curvature bound $C_\tau$: enters only continuation
- Support-count factor: none (disjoint supports, no overcounting)
- $Q_{\rm rest,i}(0)$: appears in global identity, not local chain

---

## 9. Scope and status

**Preserved conclusions and Step 60 corrections (conditional on input correctness):**

1. The $W^{1,p}\to L^\infty$ bridge (Step 57) turns the curvature endpoint
   into bounded curvature on every positive-time slab.

2. The bounded-curvature staggered induction (Step 40, A01 Step 55) propagates
   7 weighted pairs and 7 unweighted curvature levels through $s_0=7$.

3. The fixed-background connection conversion gives $g(t)\in H^{s_0}$ uniformly.

4. The finite $H^7$ package alone does not prove extension because overlap
   uniqueness is unavailable.  Step 60 supplies the corrected all-order smooth
   endpoint and uniqueness-free splice; common observation time is conditional
   on that all-order module.

5. The defect Moser endpoint $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$ and
   integrable drift $V(\theta r^2)\le C\delta\theta^{2/3}r^2$ (Step 39, eq.\ 8.3).

6. The coupled $(\Gamma,V)$ bootstrap closure (A01 Step 55, with Step 58
   curvature input and Step 39 defect input).

7. The global $Q$ decomposition with stationary remainder is preserved.


**Not established by this note:**

- Step 60 derives the universal coordinate-time derivative families for all
  $m$, classifies the commutator remainders as strictly prior-level, and checks
  252,256 finite allocations through order 64.  A fully expanded coordinate-index
  appendix would add slot-level detail but no new derivative family was found.

- Step 60 replaces the proposed core-ball Lipschitz detour by Liouville averaging
  on buffered exponential pullback balls, center harmonic charts, strong
  $W^{2,q}$ convergence, and zero limiting density by continuity.

- Positive branch, arbitrary four-manifold topology, dimensions $n\ge5$,
  dimension-only constants, and Lean formalization.  The restricted IL theorem,
  even if complete, covers only a specified four-dimensional negative geography.

## 10. Sources

- Step 56 tame construction: `workspace/notes/step56_tame_direct_flow_repair.md`
- Step 56 base pair: `workspace/notes/step56_positive_time_base_pair.md`
- Step 57 H₂ + W^{1,p}: `workspace/notes/step57_H2_evolution_and_continuation_bridge.md`
- Step 58 curvature bridge: `workspace/notes/step58_critical_to_subcritical_bridge.md`
- Step 40 staggered pattern: `workspace/notes/step40_staggered_all_order_continuation_candidate.md`
- Step 40 m=2 mechanism: `workspace/notes/step40_m2_coupled_continuation_mechanism.md`
- A01 Step 55 restart threshold: `Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md`
- A01 Step 55 bootstrap: `Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md`
- Step 39 defect ladder: `workspace/notes/step39_allp_proof_level_defect_power_inequality.md`
- Step 43 terminal density: `workspace/notes/step43_terminal_density_G_lemma.md`
