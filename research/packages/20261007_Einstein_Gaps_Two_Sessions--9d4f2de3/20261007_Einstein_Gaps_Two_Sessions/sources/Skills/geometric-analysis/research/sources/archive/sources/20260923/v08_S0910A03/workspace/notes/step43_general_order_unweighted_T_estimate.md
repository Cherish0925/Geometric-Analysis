# Step 43: General-order unweighted $\nabla^m T$ estimate

> **Step 44 correction.** The original base case and one connection-variation
> sentence below were invalid: bounded $aT$, metric equivalence, and finite total
> curvature do not give endpoint-uniform unweighted $T$ bounds or pointwise $T$.
> The actual base is the signed zero-order energy estimate in
> `step44_zero_order_T_seed_repair.md`. Connection terms must be estimated from
> $\nabla^j(\partial_t\Gamma)=\nabla^{j+1}\operatorname{Ric}(U)+\cdots$ using
> established finite-exponent $U$ and lower-$T$ levels. The corrected readings
> are inserted below; no small-$a$ division is used.

## 0. Purpose

Prove that $\nabla^m T \in L^p$ for all $m \ge 0$ and finite $p$, on a
smooth interval where $|U| \le K$.  This resolves hypothesis (H-UT) from
the corrected theorem note and completes the staggered continuation
schedule together with the Step 40 $(U_m, C_{m+1})$ induction.

## 1. Setup and inductive hypothesis

Normalized cutoff flow $\partial_t g = -2aE$, $a = \chi^2$, $E = \operatorname{Ric}+g$,
$T = \operatorname{Rm}+G$, $U = aT$, $G = g \wedge g/(2(n-1))$.

Work on $[\tau, T_*)$ with $\tau > 0$ and $\sup|U| \le K$.

**Staggered schedule (Step 40):**
\[
  T_0 \to (U_1, C_2) \to T_1 \to (U_2, C_3) \to T_2 \to \cdots
\]
where $T_j = \nabla^j T \in L^q$ for all $q$, $U_j = \nabla^j U \in L^q$,
$C_j = \nabla^j\chi \in L^q$.

**Inductive hypothesis for $T_m$.** Assume:
- $T_0, T_1, \ldots, T_{m-1} \in L^q$ for all finite $q$ on $[\tau, T_*)$;
- $U_0, U_1, \ldots, U_m \in L^q$ for all finite $q$;
- $C_0, C_1, \ldots, C_{m+1} \in L^q$ for all finite $q$ ($C_0 = \chi$,
  $C_1 = d\chi$ bounded);
- $|U| \le K$, metric equivalence $e^{-\Lambda}g_0 \le g(t) \le e^{\Lambda}g_0$,
  $|d\chi| \le C_d/r$.

**Target:** $X_m := \nabla^m T \in L^p$ for all finite $p$ on $[\tau, T_*)$.

## 2. The evolution equation for $\nabla^m T$

The $T$ equation is
\[
  (\partial_t - a\Delta)T = a(T*T + G*T) + \nabla a * \nabla T + \nabla^2 a * T.
                                                              \tag{2.1}
\]

Applying $\nabla^m$ and including commutator terms from the time-dependent
connection $\nabla_{g(t)}$:
\[
\begin{split}
  \partial_t X_m ={}&
  a\Delta X_m
  + \nabla a * \nabla X_m
  + \sum_{j=0}^{m+2} \nabla^j a * \mathcal R_m^j
  + \mathcal C_m,
\end{split}                                                    \tag{2.2}
\]
where:
- $\nabla^j a * \mathcal R_m^j$ are products of $j$-th cutoff derivatives with
  curvature and T-derivatives of total $\nabla$-count $= m+2-j$ distributed
  over at most two T-factors;
- $\mathcal C_m$ collects connection-variation terms from
  $[\partial_t\Gamma, \nabla^{m-1}T]$ and similar commutators.

**Key structural facts:**

(a) The maximum derivative of $T$ appearing in any term (other than the
    principal $X_m = \nabla^m T$ and the Laplacian $\Delta X_m$) is $\nabla^m T$
    itself, appearing linearly as a coefficient from connection variation.

(b) The highest cutoff derivative is $\nabla^{m+2}a$.  Expanding
    $\nabla^{m+2}(a) = \nabla^{m+2}(\chi^2)$:
    \[
      \nabla^{m+2}(\chi^2) = 2\chi\nabla^{m+2}\chi
      + \sum_{\substack{s+t = m+2 \\ 1 \le s,t}}
      \binom{m+2}{s}\nabla^s\chi \otimes \nabla^t\chi.       \tag{2.3}
    \]
    Every term in the sum has both indices $\le m+1$, hence all factors
    are in $L^q$ by the inductive hypothesis.  Only $2\chi\nabla^{m+2}\chi$
    may exceed the available level.

(c) In (2.2), $2\chi\nabla^{m+2}\chi$ always appears multiplied by $T$
    (the lowest curvature factor in $\nabla^{m+2}a * T$ from (2.1)),
    giving the critical integral
    \[
      I_m = \int \chi \, C_{m+2} * T * P(X_m),                \tag{2.4}
    \]
    where $C_{m+2} = \nabla^{m+2}\chi$ is NOT yet controlled and
    $P(X_m) = |X_m|^{p-2}X_m$.

## 3. Signed integration by parts for the critical term

The mechanism is the same as Step 40 §4A.  Write $C_{m+2} = \nabla(C_{m+1})$
and integrate the outermost derivative:
\[
\begin{split}
  I_m ={}&
  -\int d\chi * C_{m+1} * T * P(X_m)   \quad\text{(I)}\\
  &-\int \chi * C_{m+1} * \nabla T * P(X_m)  \quad\text{(II)}\\
  &-\int \chi * C_{m+1} * T * \nabla P(X_m). \quad\text{(III)}
\end{split}                                                    \tag{3.1}
\]

**Term (I):** $|d\chi| \le C_d/r$ is bounded; $C_{m+1}$ and $T$ are in $L^q$
for all $q$.  By Hölder:
\[
  |\text{(I)}| \le C_d r^{-1} \|C_{m+1}\|_{2p}\|T\|_{2p}\|X_m\|_p^{p-1}
  \le C_p(1 + \|X_m\|_p^p).                                   \tag{3.2}
\]

**Term (II):** $\chi$ is bounded, $C_{m+1} \in L^q$, $\nabla T = T_1 \in L^q$.
\[
  |\text{(II)}| \le \|C_{m+1}\|_{2p}\|T_1\|_{2p}\|X_m\|_p^{p-1}
  \le C_p(1 + \|X_m\|_p^p).                                   \tag{3.3}
\]

For $m=1$, $T_1=X_m$ is the current unknown and the term has the signed
structure $\int\chi(\nabla_i\nabla_j\chi)B^{ij}(T_1)$.  It is **not**
estimated using an $L^\infty$ bound for $C_2=\nabla^2\chi$.  The Step 38
signed Hessian lemma integrates it by parts and gives
\[
 \varepsilon\int\chi^2|\nabla T_1|^2|T_1|^{p-2}
 +C_{p,\varepsilon}\|d\chi\|_\infty^2\|T_1\|_p^p.
\]

**Term (III):** This has $\nabla P(X_m) = (p-1)|X_m|^{p-2}\nabla X_m$, giving
\[
  |\text{(III)}| \le (p-1)\int \chi|C_{m+1}||T||X_m|^{p-2}|\nabla X_m|.
                                                                \tag{3.4}
\]
Use $\chi \le \sqrt{a}$ and Cauchy–Schwarz:
\[
\begin{split}
  |\text{(III)}|
  &\le (p-1)\int\sqrt{a}\,|C_{m+1}||T||X_m|^{p-2}|\nabla X_m|\\
  &\le \varepsilon \int a|\nabla X_m|^2|X_m|^{p-2}
  + C_{p,\varepsilon}\int|C_{m+1}|^2|T|^2|X_m|^{p-2}\\
  &\le \varepsilon D_p^{T,m}
  + C_{p,\varepsilon}\|C_{m+1}\|_{2p}^2\|T\|_{2p}^2\|X_m\|_p^{p-2},
\end{split}                                                    \tag{3.5}
\]
where $D_p^{T,m} = \int a|\nabla X_m|^2|X_m|^{p-2}$ is the weighted
dissipation.  The Hölder product uses $C_{m+1}, T \in L^{2p}$ (given by
induction) and $|X_m|^{p-2} \in L^{p/(p-2)}$.

The last term is bounded by $C_p(1 + \|X_m\|_p^p)$ via Young.

## 4. Connection variation terms

The connection variation generates terms of the schematic form
\[
  \partial_t\Gamma^{(j)} * \nabla^{m-j-1}T,
  \qquad j = 0, \ldots, m-1,                                  \tag{4.1}
\]
where $\partial_t\Gamma^{(j)} = \nabla^j(\partial_t\Gamma)$ involves
derivatives of $\nabla(aE) = \nabla\operatorname{Ric}(U)$.

Since $\operatorname{Ric}(U) = aE$ and $\nabla(aE) = da*E + a\nabla E$,
with $\nabla E = \nabla(\operatorname{Ric}(T)) = \nabla T + T*\Gamma$:
\[
  \nabla^j(\partial_t\Gamma) \sim
  \sum_{r+s \le j+1} \nabla^r a * \nabla^s T
  + \sum_{r+s+t \le j} \nabla^r a * \nabla^s T * \nabla^t T.
                                                                \tag{4.2}
\]

Multiplied by $\nabla^{m-j-1}T$ and tested against $P(X_m)$, the maximum
derivative order of $T$ appearing (other than $X_m$) is:
\[
  \max(s, m-j-1) \le \max(j+1, m-j-1).
\]
For $j \le m-2$: both $s \le j+1 \le m-1$ and $m-j-1 \le m-1$ are below $m$,
hence controlled by the inductive hypothesis.

For $j=m-1$, do **not** rewrite the connection variation as an uncontrolled
$\nabla^mT*T$ coefficient.  The geometric identity is
\[
 \nabla^{m-1}(\partial_t\Gamma)
 =g^{-1}*\nabla^m\operatorname{Ric}(U)+\text{lower products}.
\]
Thus its top factor is the already established current-pair variable $U_m$,
while the accompanying curvature factor is $T_0$.  At fixed target exponent
$p$, Hölder assigns finite larger exponents to $U_m$ and to the zero-order
$T_0$ seed supplied by Step 44; all remaining factors lie at previous spatial
levels.  No assertion that finite total curvature bounds $T$ pointwise is used.

## 5. All lower-order cutoff products

The remaining cutoff products from (2.3) at positions $s + t = m+2$ with
$1 \le s,t \le m+1$ give:
\[
  \nabla^s\chi \otimes \nabla^t\chi * T * P(X_m),
  \qquad s,t \le m+1.
\]
Both factors are in $L^q$ for all $q$ (inductive hypothesis for $C_j$ with
$j \le m+1$).  By Hölder against $\|X_m\|_p^{p-1}$, these contribute
$C_p(1 + \|X_m\|_p^p)$.

Products of the form $\nabla^j a * T * \nabla^k T$ with $k < m$ are likewise
controlled by the inductive hypothesis.

## 6. The closed energy estimate

Combining all terms:
\[
  \boxed{
  \frac{d}{dt}\|X_m\|_p^p + cD_p^{T,m}
  \le C_p(1 + \|X_m\|_p^p),
  }                                                            \tag{6.1}
\]
where $C_p$ depends on: $K$, $r$, the metric equivalence constant $\Lambda$,
$|d\chi|_\infty$, and finite $L^{2p}$ norms of $T_0, \ldots, T_{m-1}$
and $U_0, \ldots, U_m$ and $C_0, \ldots, C_{m+1}$.
All of these are finite by the inductive hypothesis.

**Grönwall** gives $\|X_m(t)\|_p \le C(m,p,K,\text{data})$ on $[\tau, T_*)$.

## 7. Induction closure

**Theorem (general-order unweighted $T$ estimate).**
*On a smooth interval $[\tau, T_*)$ with $\tau > 0$ and $\sup|U| \le K$:
if the staggered $(U_j, C_{j+1})$ pairs through level $m$ are established
by Step 40's induction, then $\nabla^m T \in L^p$ for all finite $p$
and all $m \ge 0$.*

*Proof.* By induction on $m$.

Base case $m=0$: for every finite $q\ge2$, test the exact shifted-curvature
equation against $|T|^{q-2}T$.  The quadratic reaction is linearized by
$a|T|^{q+1}=|U||T|^q$, the gradient-cutoff terms use
$|da|^2/a=4|d\chi|^2$, and the signed Hessian-$a$ contraction is integrated by
parts once.  This gives the Step 44 estimate
\[
 \frac d{dt}\int|T|^q+c_q\int a|T|^{q-2}|\nabla T|^2
 \le C_q(K+1+\|d\chi\|_\infty^2)\int|T|^q+C'_q,
\]
so $T_0\in L^q$ uniformly on the finite positive-time slab.  Bounded $U$ and
finite total curvature alone would not imply this.

Inductive step: Assume $T_j \in L^q$ for $j < m$ and the $(U_m, C_{m+1})$
pair is established.  The energy estimate (6.1) gives $T_m \in L^p$.  $\square$

**Corollary.** Combined with the Step 40 staggered $(U_m, C_{m+1})$ induction,
bounded $|U|$ on $[\tau, T_*)$ implies all derivatives of $T$, $U$, and $\chi$
are in $L^p$ for every finite $p$.  Sobolev embedding then gives pointwise
bounds, hence smooth extension past $T_*$ (the continuation criterion).

## 8. Comparison with $m = 1$ (Step 40 §4A)

The present argument is the direct generalization of §4A.  At $m = 1$:

- Critical term: $\chi\nabla^3\chi * T * P(\nabla T)$
- IBP yields: $d\chi*\nabla^2\chi*T*P(\nabla T)$,
  $\chi*\nabla^2\chi*\nabla T*P(\nabla T)$, and
  $\chi*\nabla^2\chi*T*\nabla P(\nabla T)$
- All controlled by $C_2 = \nabla^2\chi \in L^q$ (from the $(U_1,C_2)$ pair)

At general $m$, the pattern is identical with $C_{m+2}$ replacing $\nabla^3\chi$
and $C_{m+1}$ replacing $\nabla^2\chi$.  The connection variation at high
order introduces more terms but no new mechanism.

## 9. Status and remaining work

After insertion of the Step 44 zero-order energy seed and the corrected
connection allocation, this note supplies the unweighted $T_m$ half of the
staggered continuation mechanism.  The $m=1$ signed
$\chi\operatorname{Hess}\chi*|\nabla T|^p$ term must be treated by integration
by parts, not by an $L^\infty$ Hessian bound.

The remaining independent start/restart problem is the transported-coefficient
DeTurck theorem.  Its proof must use Yang's global per-datum tame estimates for
the coupled metric/transport variables; small metric drift on $\{a\ll1\}$ is
not a substitute for derivative control.

## 10. Cross-references

- Step 40 §4A ($m = 1$ proof): `workspace/notes/step40_m2_coupled_continuation_mechanism.md`
- Staggered schedule: `workspace/notes/step40_staggered_all_order_continuation_candidate.md`
- Signed Hessian IBP: `workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md`
- Corrected theorem: `workspace/notes/step43_corrected_negative_IL_theorem.md`
