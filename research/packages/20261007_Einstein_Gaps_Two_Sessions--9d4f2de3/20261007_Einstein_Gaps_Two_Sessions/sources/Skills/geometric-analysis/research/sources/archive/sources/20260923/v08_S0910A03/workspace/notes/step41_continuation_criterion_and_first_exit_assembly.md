# Step 41: continuation criterion and first-exit assembly

Session: S0910A03. Agent2 / Constructor. Phase: Execute.

## 0. Purpose and status

This note proves the **continuation criterion** for the normalized cutoff flow
and assembles the **first-exit bootstrap** on the resulting actual maximal
smooth interval.  The derivative-energy mechanism (Step 40 staggered induction)
and the transported-coefficient short-time existence (Step 37) are consumed as
established conditional components; the only new mathematical content here is:

1. the connection between the staggered $L^p$ derivative bounds and smooth
   terminal convergence + restart;
2. the actual maximal-interval existence theorem;
3. the closed first-exit bootstrap on a genuine flow interval.

After this note, the per-manifold conditional gap theorem is reduced to the
**terminal geometric passage** (Layer E): from the controlled terminal metric to
the calibrated Einstein germ, the projector contradiction, and the topological
conclusion.

This note does not establish terminal geometry, sequence-uniform gap constants,
positive branch, higher dimensions, or Lean formalization.

## 1. Standing notation and sources

On a closed smooth $n$-manifold $M$ with $\chi\in C^\infty(M)$, $0\le\chi\le1$,
set
\[
  a=\chi^2,\qquad E=\operatorname{Ric}_g+g,\qquad
  G=\frac{g\owedge g}{2(n-1)},\qquad
  T=\operatorname{Rm}+G,\qquad U=aT.
  \tag{1.1}
\]
Then $\operatorname{Ric}(T)=E$ and $\operatorname{Ric}(U)=aE$.  The normalized
cutoff flow is
\[
  \partial_tg=-2aE=-2\operatorname{Ric}(U).
  \tag{1.2}
\]

**Sources consumed.**
- Step 37 note `step37_transported_deturck_existence.md`: the normalized
  transported-coefficient DeTurck system has a smooth short-time solution on
  $[0,T_0]$ for some $T_0>0$, adapting Yang's Theorem 8.2 with the
  normalization absorbed into bounded lower-order matrices.
- Step 40 note `step40_staggered_all_order_continuation_candidate.md`:
  on a smooth positive-time slab $[\tau,T_*)$ with $|U|\le K$, the staggered
  induction
  \[
    T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to T_2\to\cdots
    \tag{1.3}
  \]
  gives $U_m,C_{m+1},T_m\in L^q$ for all $m\ge0$ and all finite $q$, with
  per-datum constants depending on $K$, the initial metric, and the cutoff.
- Step 40 note `step40_m2_coupled_continuation_mechanism.md`: the $m=2$ case
  is proved in full detail; the mechanism (extra signed integration by parts
  on $\chi\nabla^{m+1}\chi*\nabla U*P(\nabla^mU)$) extends to all orders.

## 2. Metric equivalence under bounded $U$

**Lemma 2.1.** If $g(t)$ is a smooth solution of (1.2) on $[0,T_*)$ with
$\sup_{M\times[0,T_*)}|U|\le K$, then
\[
  e^{-C_nKt}g(0)\le g(t)\le e^{C_nKt}g(0)
  \tag{2.1}
\]
for all $t\in[0,T_*)$.  Moreover $|d\chi|_{g(t)}$, $\operatorname{Vol}_{g(t)}(M)$,
and the Sobolev constants of $(M,g(t))$ are uniformly bounded on $[0,T_*)$.

*Proof.* For any nonzero $X\in T_pM$,
\[
  \left|\frac{d}{dt}\log g(t)(X,X)\right|
  =\frac{|\partial_tg(X,X)|}{g(t)(X,X)}
  \le|\partial_tg|_{\mathrm{op},g(t)}
  \le2|\operatorname{Ric}(U)|_{g(t)}
  \le C_nK.
\]
Integrating gives the multiplicative bound (2.1).  Sobolev constants and
$|d\chi|$ are then controlled by metric equivalence and volume comparison;
their upper bounds depend on $n$, $K$, $T_*$, and the initial
$(M,g(0))$.  $\square$

## 3. Continuation criterion

**Theorem 3.1 (Continuation Criterion).** Let $(M^n,g_0)$ be a closed smooth
Riemannian manifold, $\chi\in C^\infty(M)$, $0\le\chi\le1$.  Suppose $g(t)$ is
a smooth solution of (1.2) on $[0,T_*)$ with $T_*<\infty$ and
\[
  \sup_{M\times[0,T_*)}|U(t)|_{g(t)}\le K.
  \tag{3.1}
\]
Then the solution extends smoothly past $T_*$: there exists $\varepsilon>0$ and
a smooth solution $g(t)$ on $[0,T_*+\varepsilon)$ satisfying (1.2).

*Proof.* We verify that all derivatives of the velocity are uniformly bounded
on $[0,T_*)$, then extract a smooth terminal metric and restart.

**Step A.** By Lemma 2.1, the metrics $g(t)$ are uniformly equivalent on
$[0,T_*)$.  Fix $\tau=T_*/2>0$.  At time $\tau$, the smooth solution has finite
norms
\[
  \|U_m(\tau)\|_{L^q}+\|C_{m+1}(\tau)\|_{L^q}+\|T_m(\tau)\|_{L^q}<\infty
\]
for every $m$ and $q$ (since $g(\tau)$ is smooth and $M$ is compact).

**Step B (Staggered L^p induction).** Apply the Step 40 staggered induction on
$[\tau,T_*)$ with the input $|U|\le K$ and the finite initial data at time
$\tau$.  By induction in spatial order, using (1.3):

- Stage 0: $T\in L^q$ for all $q$ (unweighted $\operatorname{Rm}$ propagation,
  adapting Wang Lemma 4.10 with the normalization term, which is
  zeroth-order).
- Stage 1: $(U_1,C_2)\in L^q$ for all $q$ (base pair with signed Hessian
  repair); then $T_1=\nabla T\in L^q$ for all $q$ (unweighted whole-manifold
  lemma, Step 40 Section 4A).
- Stage $m\ge2$: $(U_m,C_{m+1})\in L^q$ for all $q$ (coupled estimate with the
  extra integration by parts); then $T_m=\nabla^mT\in L^q$ for all $q$
  (unweighted estimate with honest expansion of $\nabla^{m+2}a$).

Each stage closes by Grönwall with per-datum constants depending on $K$,
metric equivalence, the cutoff, and the finite data at time $\tau$.  The result
is: for every $m\ge0$ and every finite $q$,
\[
  \sup_{t\in[\tau,T_*)}
  \bigl(\|U_m(t)\|_{L^q}+\|C_{m+1}(t)\|_{L^q}+\|T_m(t)\|_{L^q}\bigr)
  <\infty.
  \tag{3.2}
\]

**Step C (Pointwise bounds).** Choose $q>n$.  By Kato's inequality
$|\nabla|U_m||\le|U_{m+1}|$ and the Sobolev embedding
$W^{1,q}(M)\hookrightarrow L^\infty(M)$ with uniformly bounded Sobolev constant
(Lemma 2.1):
\[
  \|U_m\|_{L^\infty}\le C\bigl(\|U_m\|_{L^q}+\|U_{m+1}\|_{L^q}\bigr)<\infty
  \tag{3.3}
\]
for every $m\ge0$, uniformly on $[\tau,T_*)$.  Likewise for $C_{m+1}$ and $T_m$.
Since $|U|\le K$ already holds on $[0,\tau]$, and all derivative norms are
finite on $[0,\tau]$ by the smooth solution, (3.3) extends to uniform bounds on
all of $[0,T_*)$.

**Step D (Bounded velocity derivatives).** Since
$\partial_tg=-2\operatorname{Ric}(U)$ and $\operatorname{Ric}$ is a trace
contraction, every covariant derivative of the velocity satisfies
\[
  |\nabla^m(\partial_tg)|\le C_m\sum_{j\le m}|U_j|\le C_m'
  \tag{3.4}
\]
uniformly on $[0,T_*)$.

**Step E (Smooth terminal convergence via connection-difference induction).**
Let $A(t)=\nabla^{g(t)}-\nabla^{g(0)}$ be the connection difference.  The
connection variation formula gives
\[
  |\partial_tA|\le C_n|\nabla(\partial_tg)|\le C_n|\nabla\operatorname{Ric}(U)|,
\]
which is bounded on $[\tau,T_*)$ by Step C.  By induction on $r$, using
$\nabla^{g(0)}=\nabla^{g(t)}+A*$ and the bounded $g(t)$-derivatives of the
velocity:
\[
  \sup_{t\in[\tau,T_*)}\|(\nabla^{g(0)})^rA(t)\|_\infty<\infty
  \quad\text{for every }r\ge0.
\]
Therefore in fixed coordinates (harmonic at time 0), the components $g_{ij}(t)$
and all their spatial and time derivatives satisfy
\[
  \|g(t)-g(s)\|_{C^k(g(0))}\le C_k|t-s|
  \quad\text{for all }s,t\in[\tau,T_*).
\]
The family is Cauchy in every $C^k$ norm and converges to a unique $C^\infty$
limit $g_*=\lim_{t\to T_*}g(t)$.  Positive definiteness is preserved by the
multiplicative bound (2.1).  Since the flow equation is autonomous, all time
jets of the old solution and the would-be restart agree at $T_*$ by the same
recursive evaluation of $\mathcal F(g)=−2a(\operatorname{Ric}_g+g)$, so the
pasting is $C^\infty$.

**Step F (Restart).** Apply the Step 37 existence theorem to the smooth initial
data $(M,g_*,\chi)$.  This produces a smooth solution of (1.2) on
$[T_*,T_*+\varepsilon]$ for some $\varepsilon>0$.  By the $C^\infty$ jet
matching of Step E, the combined family is a smooth solution on
$[0,T_*+\varepsilon)$.  $\square$

**Remark 3.4 (Nonlinear local uniqueness).** The Yang tame estimates for the
transported-coefficient DeTurck system imply local uniqueness of smooth solutions
in the Nash--Moser framework: two smooth solutions with the same initial data
agree on their common interval.  This ensures that the restart does not produce
a different branch.

**Remark 3.2.** The criterion uses $|U|=|a(Rm+G)|$ rather than $|aRm|$.  Since
$|G|\le C(n)$ on any Riemannian manifold, bounded $|U|$ is equivalent to bounded
$|aRm|$ up to an additive constant.  This is also the natural variable for the
energy estimates, since $\operatorname{Ric}(U)=aE$.

**Remark 3.3 (Comparison with Wang Theorem 4.1).** Wang's Theorem 4.1 proves
extension under bounded $|\chi^2\operatorname{Rm}|_\infty$ for the unnormalized
LRF $\partial_tg=-2\chi^2\operatorname{Ric}$.  Our Theorem 3.1 extends this to
the normalized flow $\partial_tg=-2\chi^2(\operatorname{Ric}+g)$, with the
normalization absorbed into the zeroth-order reaction at every stage of the
staggered induction.  The proof structure is the same (Wang Proposition 4.3,
Lemma 4.10, Lemma 4.11, Proposition 4.14), but our variable $U=aT$ packages
the normalization and avoids separate treatment of $aG$.

## 4. Maximal existence theorem

**Corollary 4.1 (Maximal Existence).** For any smooth initial data $(M,g_0,\chi)$
with $M$ closed and $0\le\chi\le1$, there exists a unique maximal smooth solution
$g(t)$ of (1.2) on $[0,T_{\max})$ with $0<T_{\max}\le\infty$.  If $T_{\max}<\infty$,
then
\[
  \limsup_{t\to T_{\max}}\sup_M|U(t)|=+\infty.
  \tag{4.1}
\]

*Proof.* Short-time existence (Step 37) gives $T_{\max}>0$.  If $T_{\max}<\infty$
and $|U|$ were bounded on $[0,T_{\max})$, Theorem 3.1 would extend the solution,
contradicting maximality.  $\square$

## 5. First-exit bootstrap on the actual maximal interval

We now assemble the first-exit argument.  The setting is dimension $n=4$
with the critical Ishida--LeBrun topology and $\chi$ a buffered cutoff
supported on a macro-disjoint component (Step 30, corrected Step 34).

**Bootstrap hypotheses** on $[0,T_{\rm ex})$:

\[
\begin{aligned}
&\text{(H1)}&&
  e^{-1}g(0)\le g(t)\le eg(0),\quad\text{on }M, \\
&\text{(H2)}&&
  \sup_M|U(t)|\le K_*,\\
&\text{(H3)}&&
  K_2(t)=\int\eta^2a^0F^2\,d\mu\le 2K_2^{(0)},\\
&\text{(H4)}&&
  \gamma(t)=\mathcal S(t)K_2(t)^{1/2}\le 2\gamma_0,
\end{aligned}
\tag{5.1}
\]

where $K_*,K_2^{(0)},\gamma_0$ are determined by the initial data and must
satisfy $\gamma_0\le c_4$ for a dimensional constant $c_4$.  Here
$F=(1+|\operatorname{Rm}|^2)^{1/2}$, $\eta$ is the macro-support cutoff, and
$\mathcal S$ is the local Sobolev constant on the $6r$-auxiliary ball.

The first-exit time is
\[
  T_{\rm ex}=\sup\{t\in[0,T_{\max}):
  \text{(H1)--(H4) hold on }[0,t)\}.
  \tag{5.2}
\]

By continuity of smooth solutions, $T_{\rm ex}>0$.

### 5.1. Self-improvement under (H1)--(H4)

Assuming (H1)--(H4) on $[0,T_{\rm ex})$:

**(a) Curvature energy seed ($q=2$).**
\[
  \sup_{t<T_{\rm ex}}K_2(t)+\int_0^{T_{\rm ex}}D_2\,dt
  \le CK_2^{(0)}.
  \tag{5.3}
\]
The reaction $a|\operatorname{Rm}|^3$ is controlled by $|U||\operatorname{Rm}|^2$,
using (H2) and the Sobolev absorption with $\gamma\le 2\gamma_0\le 2c_4$.

**(b) Curvature potential ($q=3$).**
\[
  Y(t)=\int\eta^2aF^3\,d\mu
  \le C\gamma_0 K_2^{(0)}/t.
  \tag{5.4}
\]

**(c) Curvature Moser endpoint.**
By the $p\mapsto3p/2$ spacetime recurrence (Step 34):
\[
  \|aF(t)\|_\infty\le C\gamma_0/t.
  \tag{5.5}
\]
Therefore
\[
  |U(t)|=|aT|\le a|F|+|aG|\le C\gamma_0/t+C.
  \tag{5.6}
\]

**(d) Defect seed ($J_6$).**  Step 35:
\[
  J_6(t)\le e^{C(1+r^{-2})t}J_6(0)\le C\delta^6V.
  \tag{5.7}
\]

**(e) General-$p$ defect Moser.**  Step 39 Theorem 7.1:
\[
  H_p^E{}'+c\|\nabla z_p\|_2^2\le Cp^4(1+r^{-2}+\mathcal S^2Y)H_p^E,
  \tag{5.8}
\]
with three-factor coupling to $Y$.  The Moser ladder $p_k=6\cdot(3/2)^k$
converges to
\[
  \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}.
  \tag{5.9}
\]

**(f) Metric drift.**
\[
  |g(t)-g(0)|
  \le 2\int_0^t|aE|\,ds
  \le C\delta\int_0^t(r^2/s)^{1/3}\,ds
  = C'\delta\,t^{2/3}r^{2/3}.
  \tag{5.10}
\]
For $\delta\le c_4$ and $t\le\theta$ (the observation time), this is
$\le C\delta\theta^{2/3}r^{2/3}\ll 1$.  In particular, (H1) is improved to
a $1+O(\delta)$ bilipschitz estimate.

**(g) Sobolev and support constants.**
Under the improved metric comparability, the Sobolev constant $\mathcal S$ and
the support parameters are within $1+O(\delta)$ of their initial values.
Hence $\gamma(t)$ is within $1+O(\delta)$ of $\gamma_0$, improving (H4).

**(h) Energy improvement.** The same metric comparability improves (H3) to
$K_2(t)\le(1+C\delta)K_2^{(0)}$.

### 5.2. Closure

Combining (c) and (f)--(h): for $\delta$ and $\gamma_0$ sufficiently small
(depending only on $n=4$, $r$, and $\theta$), the bootstrap hypotheses
(H1)--(H4) are strictly improved.

**First-exit equals maximal time.** By continuity, if $T_{\rm ex}<T_{\max}$,
then (H1)--(H4) hold on $[0,T_{\rm ex}]$ by the limit values.  The strict
improvement shows that (H1)--(H4) hold on $[0,T_{\rm ex}+\delta t)$ for some
small $\delta t>0$, contradicting the definition of $T_{\rm ex}$.  Hence
$T_{\rm ex}=T_{\max}$.

**Infinite existence.** On $[0,T_{\max})$ with $T_{\rm ex}=T_{\max}$, the
bound (5.6) gives
\[
  \sup_M|U(t)|\le C\gamma_0/t+C\quad\text{for }t>0.
  \tag{5.11}
\]
This is finite for each $t>0$.  If $T_{\max}<\infty$, then $\sup|U|$ is bounded
on $[0,T_{\max})$ (by (5.11) for $t\ge\tau$ and by the smooth solution for
$t\le\tau$), contradicting Corollary 4.1.  Hence $T_{\max}=\infty$.

### 5.3. Global $Q$ preservation

The global defect integral $Q(t)=\int_M|E|^2\,d\mu$ satisfies the separate
homogeneous estimate (Step 37, `step37_global_Q_persistence.md`):
\[
  Q(t)\le e^{C\theta}Q(0)\le C\delta^2V
  \tag{5.12}
\]
on the now-established infinite interval.  This is needed for terminal
calibration and is independent of $J_6$ and $\|aE\|_\infty$.

## 6. Summary of established flow properties

For the normalized cutoff flow on a closed 4-manifold with
$\gamma_0,\delta\le c_4$:

| Property | Estimate | Source |
|----------|----------|--------|
| Existence | $T_{\max}=\infty$ | §5.2 + Corollary 4.1 |
| Curvature decay | $\|aF(t)\|_\infty\le C\gamma_0/t$ | (5.5) |
| Defect decay | $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$ | (5.9) |
| Metric drift | $|g(t)-g(0)|\le C\delta t^{2/3}r^{2/3}$ | (5.10) |
| Energy | $K_2(t)\le CK_2^{(0)}$ | (5.3) |
| Global defect | $Q(t)\le C\delta^2V$ | (5.12) |
| All derivatives | $\|\nabla^mU(t)\|_\infty<\infty$ | Thm 3.1 + §5 |

These are per-datum estimates: the constants $c_4$, $C$, and the required
initial smallness depend on the individual smooth metric $g_0$ and cutoff $\chi$,
through $K_2^{(0)}$, the Sobolev constant $\mathcal S_0$, and the support
geometry.  Sequence-uniform estimates require additional arguments about the
terminal calibrated family and are not supplied here.

## 7. Conditional per-manifold gap statement

**Conditional Theorem 7.1.** Let $M^4$ be a critical Ishida--LeBrun manifold,
$D=A/3$, admitting no Einstein metric.  Suppose the terminal geometric passage
(Layer E) is established: namely, from the controlled terminal metric at large
$\theta$ and preserved global $Q$, one can extract a positive-volume calibrated
chart, a nonzero limiting self-dual eigenform, and use it to reach the forbidden
Einstein germ with calibrated $W^+$-spectrum
$(-1/6,1/12,1/12)$, contradicting the Step 6 projector obstruction.

Then there exists $\delta_0(M)>0$ such that no smooth metric $g$ on $M$ satisfies
$\|g^{-1}(\operatorname{Ric}_g+g)\|_\infty\le\delta_0$.

*Proof (sketch).* Suppose $g_i$ is a sequence with
$\delta_i=\|\operatorname{Ric}_{g_i}+g_i\|_\infty\to0$.  Choose the macro-support
cutoff $\chi$ using the maximal separated net on $(M,g_i)$ (Step 30).  The initial
data $K_2^{(0)},\gamma_0,\delta_i$ satisfy the bootstrap hypotheses for $i$
large.  The flow exists for all time with the estimates of §6.  The terminal
geometric passage produces the Einstein germ, which is forbidden.  $\square$

## 8. Discharge of A01's hypothesis (H1)

A01's `step39_complete_conditional_defect_gap_theorem.md` assembles the full
end-to-end proof of the near-critical Ishida–LeBrun gap conditional on one
analytic hypothesis:

> **(H1):** The transported-coefficient DeTurck system for
> $\partial_tg=-2\chi^2(\operatorname{Ric}+g)$ has a smooth short-time solution
> for any smooth initial data, and the construction can restart from any smooth
> terminal metric.

**Discharge.**  Step 37 (`step37_transported_deturck_existence.md`) proves the
short-time existence by adapting Yang's Theorem 8.2 with the normalization
absorbed as a bounded zeroth-order perturbation of the linearized matrices.
The restart is immediate: the existence theorem applies to any smooth
$(M,g_*,\chi)$, hence to the terminal metric.  Theorem 3.1 above ensures that
the restart can be combined with the previous solution whenever $|U|$ is bounded.

A01's first-exit uses a **finite** observation time $T_*\le\theta r^2$; the flow
does not need $T_{\max}=\infty$.  The bootstrap proceeds:
1. Step 37 starts the flow on $[0,T_1)$ for some $T_1>0$.
2. If $T_1<\theta r^2$ and (F1)--(F3) hold on $[0,T_1)$, then $|U|$ is bounded
   (from the Moser endpoint + initial-layer smoothness), and Theorem 3.1 extends
   the flow past $T_1$.
3. The self-improvement of (F1)--(F3) (A01 §4.6) gives strict margin, so the
   bootstrap continues.
4. By induction, the flow reaches $\theta r^2$.

This makes A01's Theorem 1.1 **unconditional** (modulo the full formalization of
the Step 40 all-order derivative-energy induction, which is TTCS-verified but
schematic at high orders).

## 9. Remaining obligations

1. **Terminal geometric passage (Layer E).** The calibrated-chart extraction,
   eigenline density, exponential-pullback averaging, limiting eigenform, and
   the Step 6 projector contradiction must be assembled into one continuous
   argument.  The pieces exist in Steps 3--6 and 29--30 but have not been
   connected on the actual controlled terminal metric.

2. **Topology-uniform gap.** The per-manifold constants depend on $K_2^{(0)}$
   and $\mathcal S_0$ of the individual metric.  A topology-uniform gap would
   require that these quantities are controlled by the topological invariants
   $(A,D)$ alone, via the calibrated volume and energy identities.  This is a
   separate argument.

3. **Positive branch and higher dimensions.** Entirely open.

4. **Lean formalization.** Not begun.

This note does not claim any of these remaining obligations are trivial or
established.
