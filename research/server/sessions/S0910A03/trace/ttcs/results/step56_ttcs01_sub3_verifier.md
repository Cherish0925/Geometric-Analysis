# TTCS Independent Branch Record

```json
{
  "step_id": 56,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md",
    "Sessions/S0910A03/workspace/notes/step47_consolidated_negative_IL_gap_theorem.md",
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step44_zero_order_T_seed_repair.md",
    "Sessions/S0910A01/workspace/notes/step44_preceptor_reading_first_exit_terminal_chain.md"
  ]
}
```

## Task

Verify Step 56 Section 6 as the interface between per-datum flow construction and the collapse-uniform first-exit program. Check specifically: H_2 must be unweighted in a; shifted T versus Rm comparability; the exact global-Q decomposition with Q_rest and whether Q_rest is stationary given eta=1 near active supports; and the logical continuation argument that starts each datum separately, obtains uniform first-exit estimates only on its actual lifespan, and uses the positive-time U/T/cutoff-jet hierarchy to rule out an endpoint before theta r^2 without importing high cutoff jets into the uniform estimates. Identify any circularity or support-geometry flaw.

## Output

# Scientific verification memo: Step 56 §6

## 1. The \(H_2^\alpha\) seed

From
\[
H_q^\alpha=\int_M\eta_\alpha^2a^{q-2}F_T^q\,d\mu,
\qquad F_T=(1+|T|^2)^{1/2},
\]
one has
\[
H_2^\alpha=\int_M\eta_\alpha^2F_T^2\,d\mu.
\]
At \(q=2\), \(a^{q-2}\) must be defined as \(1\), including on \(\{a=0\}\). This unweighted form is essential because the Sobolev potential estimate is performed over the entire \(\eta_\alpha\)-domain, including the collar where \(a\) is small or zero. An energy containing an extra factor \(a\) supplies no curvature information in that collar.

The sentence asserting that \(|T|^2\) and \(1+|\operatorname{Rm}|^2\) are comparable is not correct as written. Put
\[
G=\frac{g\owedge g}{2(n-1)},\qquad T=\operatorname{Rm}+G.
\]
Since \(|G|_g=b_n\) is a dimensional constant,
\[
1+|T|^2\le 1+2|\operatorname{Rm}|^2+2b_n^2
 \le C_n(1+|\operatorname{Rm}|^2),
\]
and, using \(\operatorname{Rm}=T-G\),
\[
1+|\operatorname{Rm}|^2\le C_n(1+|T|^2).
\]
Thus the correct equivalence is
\[
\boxed{F_T^2=1+|T|^2\asymp_n1+|\operatorname{Rm}|^2.}
\]
The added \(1\) cannot be omitted: when \(\operatorname{Rm}=-G\), one has \(T=0\) while \(1+|\operatorname{Rm}|^2>0\).

Consequently, if
\[
\operatorname{supp}\eta_\alpha\subset B_{7r}(x_\alpha),\qquad
\fint_{B_{7r}(x_\alpha)}|\operatorname{Rm}|^2\le\kappa_0^2,
\]
then
\[
H_2^\alpha(0)
 \le C_n(1+\kappa_0^2)\operatorname{Vol}B_{7r}(x_\alpha).
\]
Together with
\[
\mathcal S_\alpha\le
\frac{Cr^2}{\sqrt{\operatorname{Vol}B_{7r}(x_\alpha)}},
\]
or with a comparable inner-ball volume via Bishop–Gromov, this gives
\[
\mathcal S_\alpha H_2^\alpha(0)^{1/2}
 \le Cr^2\sqrt{1+\kappa_0^2}.
\]
The older notes alternate between \(B_{6r}\) and \(B_{7r}\). Either nesting works, but the ball containing \(\operatorname{supp}\eta_\alpha\), the maximal-function radius, and the Sobolev domain must be synchronized. If different radii are used, the required volume ratio follows from the Ricci lower bound.

## 2. Exact global-\(Q\) decomposition

Assume
\[
0\le\eta_\alpha\le1,
\qquad
\operatorname{supp}\eta_\alpha\cap
\operatorname{supp}\eta_\beta=\varnothing\quad(\alpha\ne\beta),
\]
and set
\[
\rho=\sum_\alpha\eta_\alpha^2.
\]
Then \(0\le\rho\le1\), so
\[
Q_{\rm rest}(t)=\int_M(1-\rho)|E(t)|^2\,d\mu_t\ge0.
\]
At every time,
\[
\begin{aligned}
Q_{\rm rest}(t)+\sum_\alpha Q_\alpha(t)
&=\int_M\left(1-\sum_\alpha\eta_\alpha^2\right)|E|^2\,d\mu_t
  +\sum_\alpha\int_M\eta_\alpha^2|E|^2\,d\mu_t\\
&=\int_M|E|^2\,d\mu_t
=Q_{\rm global}(t).
\end{aligned}
\]
Thus (6.6) is an exact identity.

The stationarity statement requires the open buffer
\[
\boxed{\operatorname{supp}\chi_\alpha
 \Subset\{\eta_\alpha=1\}.}
\]
Under pairwise disjoint outer supports, this implies that \(\rho=1\) on an open neighborhood of \(\operatorname{supp}a\). Hence
\[
\operatorname{supp}(1-\rho)\cap\operatorname{supp}a=\varnothing,
\]
and \(a\) vanishes on an open neighborhood of \(\operatorname{supp}(1-\rho)\). For the exact pulled-back flow
\[
\partial_tg=-2a(\operatorname{Ric}+g),
\]
the metric is therefore identically equal to its initial value on that open set. All its spatial jets, \(E\), and \(d\mu_g\) are constant there, giving
\[
Q_{\rm rest}(t)=Q_{\rm rest}(0).
\]

Pointwise vanishing of \(a\) without the open buffer would not suffice, because \(E\) depends on spatial second derivatives of \(g\). The “neighborhood” wording in §6.2 supplies exactly what is needed.

If
\[
Q_\alpha(t)\le e^{Lt}Q_\alpha(0),
\]
then, since \(Q_{\rm rest}(0)\ge0\),
\[
\begin{aligned}
Q_{\rm global}(t)
&\le Q_{\rm rest}(0)+e^{Lt}\sum_\alpha Q_\alpha(0)\\
&=e^{Lt}Q_{\rm global}(0)
 -(e^{Lt}-1)Q_{\rm rest}(0)\\
&\le e^{Lt}Q_{\rm global}(0).
\end{aligned}
\]
Thus selected supports need not cover \(M\).

This identity belongs to the exact geometric flow after the regularizations have been removed and the DeTurck pullback performed. It is not available for the \((\varepsilon,\nu)\)-approximants, whose metric and scalar coefficient can evolve outside the original active region.

## 3. Compatibility of the one-cutoff construction with many supports

Section 5 constructs a flow with coefficient \(\chi^2\), whereas §6 writes
\[
a=\sum_\alpha\chi_\alpha^2.
\]
The two are the same when the inner supports are disjoint: define
\[
\chi=\sum_\alpha\chi_\alpha.
\]
Then
\[
0\le\chi\le1,\qquad
\chi^2=\sum_\alpha\chi_\alpha^2=a,
\]
because all cross-products vanish. Pairwise disjoint \(\eta_\alpha\)-supports imply the required disjointness of the enclosed \(\chi_\alpha\)-supports. This identification should be explicit when joining §§5 and 6.

The first-exit estimates also use
\[
|d\eta_\alpha|\lesssim r^{-1}
\]
in addition to \(|d\chi|\lesssim r^{-1}\). Only first derivatives of these cutoffs enter the critical energy and Moser estimates after the signed Hessian integrations by parts. Higher cutoff jets enter later only in the datum-dependent continuation hierarchy.

## 4. Per-datum start and positive-time continuation

The continuation logic is sound after replacing “endpoint of the chosen smooth branch” by the endpoint \(T_i^*\) of a maximally extendible smooth branch, where local solutions are concatenated whenever a smooth endpoint exists. Without maximality, restarting an arbitrarily stopped branch gives no contradiction.

For each datum \(i\):

1. The tame local theorem supplies some \(T_i>0\), possibly depending on every initial Sobolev norm and cutoff jet.

2. On the existing portion of the maximal branch, define the first threshold time using only the \(H_2\), drift, Sobolev, and support conditions. The first-exit estimates are applied on
   \[
   0<t<\min\{T_i^*,\theta r^2\}.
   \]
   Their strict improvements exclude a threshold exit before either \(T_i^*\) or \(\theta r^2\).

3. Suppose \(T_i^*<\theta r^2\). On
   \[
   \tau_i:=T_i^*/2\le t<T_i^*,
   \]
   (6.8) gives
   \[
   |U|=|aT|\le aF_T\le \frac{C\gamma}{t}
   \le\frac{2C\gamma}{T_i^*}<\infty.
   \]
   This constant can become large as \(T_i^*\) becomes small, but it is finite for this datum.

4. Step 44 equation (2.13) then propagates every finite \(L^p\) norm of the unweighted \(T\) on the terminal slab. The staggered estimates from Step 40,
   \[
   T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
   \longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots,
   \]
   propagate all finite \(L^p\) norms of \(U_m\), \(C_{m+1}\), and \(T_m\). Taking \(p>n\) supplies pointwise bounds for all derivatives of \(U\).

5. Since
   \[
   \partial_tg=-2\operatorname{Ric}(U),
   \]
   all spatial derivatives of the metric velocity remain bounded on the terminal slab. The metric converges in fixed coordinates to a smooth positive metric \(g(T_i^*)\). The local theorem starts a new exact flow from that metric. Because the equation is autonomous with fixed \(a\), all time jets agree at the joining slice, so the concatenation is smooth even without uniqueness.

This contradicts maximal extendibility. Therefore \(T_i^*\ge\theta r^2\).

There is no cyclic dependence between the two sets of estimates. The uniform quantities \(r,\theta,\gamma,\delta\) are fixed entirely through \(H_2\), local Sobolev constants, \(|d\chi|\), \(|d\eta|\), initial defect energy, and support buffers. Higher jets \(C_j\) appear only after moving to the positive-time slab and are used merely to establish finite per-datum continuation constants. Those constants never enter the uniform first-exit parameter choices.

## Overall assessment

Section 6 provides a coherent interface once three points are stated precisely:

- replace the incorrect \(|T|^2\)-comparison by
  \[
  1+|T|^2\asymp_n1+|\operatorname{Rm}|^2;
  \]
- identify the global cutoff \(\chi=\sum_\alpha\chi_\alpha\), so \(a=\chi^2\);
- define \(T_i^*\) using a maximally extendible concatenated branch.

The \(Q_{\rm rest}\) argument is exact under the stated open support buffer and pairwise disjoint outer supports. The continuation mechanism does not import high cutoff jets into the collapse-uniform estimates.