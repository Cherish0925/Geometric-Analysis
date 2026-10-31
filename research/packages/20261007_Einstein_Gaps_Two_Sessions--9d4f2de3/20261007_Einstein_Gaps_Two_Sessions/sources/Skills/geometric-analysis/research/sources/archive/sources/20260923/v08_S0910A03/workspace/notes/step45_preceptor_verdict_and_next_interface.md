# Step 45 Preceptor verdict: repaired smoothing interface

## 1. Verdict on the Step 44 handoff

The Step 44 ledger could not support continuation or coefficient regularization
as written.  It mixed a metric-compatible time derivative with coordinate-time
variation formulas and erased coefficient factors in the differentiated
\((db*db)T\) term.  Those are structural errors rather than stylistic
ambiguities.

The replacement note
`step45_coordinate_tensor_ledger_and_regularized_closure.md` uses coordinate
\(\partial_t\) consistently and retains

\[
 \nabla^{r+1}b*\nabla^{s+1}b*T_t,
 \qquad r+s+t=m,
 \qquad b=\chi^2+\varepsilon^2.
\]

After TTCS review, the following further corrections were inserted:

* \(\partial_tG=-(S\owedge g+g\owedge S)/(n-1)\), with
  \(S=\operatorname{Ric}(U)\);
* spatial commutators retain \(\operatorname{Rm}\), with
  \(b\operatorname{Rm}=U-bG\) at derivative order zero;
* the current tables explicitly include the harmless linear terms \(bT_m\),
  \(bU_m\), and the pre-conversion term \(bT_m*U_0\);
* the \(m=2\) endpoint of the second cutoff-jet integration is written as an
  actual signed Hessian contraction.

Both independent verifier branches reconstructed the base equations from the
coordinate variation of curvature and Wang's formulas and found no remaining
current derivative, unweighted pointwise-curvature coefficient, exponent
escalation, or negative power of \(\varepsilon\) in the staggered estimates.

## 2. Decisive coefficient mechanism

The old family

\[
 C_{r+1}*C_{s+1}*T_t
\]

was false as an exhaustive representation.  The correct family is

\[
 B_{r+1}*B_{s+1}*T_t,
 \qquad B_k=\nabla^kb.
\]

At the two dangerous allocations this gives

\[
 B_1*B_1*T_m
 =4{\chi^2\over b}C_1*C_1*
   \left(U_m-\sum_{q=1}^m B_q*T_{m-q}\right),
\]

and

\[
 B_{m+1}*B_1*T_0
 =4{\chi^2\over b}C_{m+1}*C_1*U_0+	ext{previous cutoff levels}.
\]

Thus the first term has a bounded coefficient on the current \(U_m\), while
the second uses bounded \(U_0\), not unavailable \(T_0\in L^\infty\).  This
is exactly why coefficient regularization is compatible with the staggered
order

\[
 T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to T_2\to\cdots.
\]

The scalar/partition script
`workspace/scripts/verify_step45_weight_partitions.py` passes 110/110 checks;
it does not verify tensor provenance or PDE existence.  The tensor provenance
was examined independently in the two Step 45 TTCS branches against Wang's
coordinate-time formulas.

## 3. Per-datum start and restart

For each fixed \(\varepsilon>0\), use a DeTurck system with transported
coefficient

\[
 \widehat b_\varepsilon=b_\varepsilon\circ\varphi_t^{-1};
\]

a fixed spatial coefficient in hatted coordinates would pull back to the wrong
geometric equation.  Strict parabolicity may have constants depending on
\(\varepsilon^{-1}\).  The common time is obtained afterward on the pulled-back
geometric flows by the \(\varepsilon\)-uniform finite-exponent estimates and a
bootstrap on \(|U|\) and metric equivalence.

Fixed-background compactness should be expressed through

\[
 A_\varepsilon=\nabla^{g_\varepsilon}-\nabla^{g_0},
 \qquad
 \partial_tA_\varepsilon
 =g_\varepsilon^{-1}*\nabla\operatorname{Ric}(U_\varepsilon).
\]

The all-order \(U\)-bounds imply all fixed-coordinate spatial derivatives of
\(A_\varepsilon\) and \(g_\varepsilon\); the equation gives mixed time
bounds.  Hence a subsequence converges smoothly to a positive-definite solution
of the exact degenerate normalized cutoff flow.  Repeating the same construction
from a smooth endpoint and matching autonomous time jets gives at least one
smooth extension.  This does not prove uniqueness of the degenerate flow or
subsequence independence, but those are not needed to exhibit a continuation
for the contradiction argument.

## 4. Current mathematical status

The per-datum flow start/restart and derivative propagation now have a coherent
constructive route that no longer depends on reconstructing Yang's compressed
smooth-tame inverse.  The restriction is important: these estimates are
per-datum and use finite additive terms; the collapse-uniform observation time
must still come from the separate homogeneous weighted first-exit estimates.

The entire restricted near-critical Ishida--LeBrun gap should not yet be called
proved solely from this interface review.  The next load-bearing work is to
re-examine the assembled first-exit theorem on one actual regularization-limit
flow, especially:

1. simultaneous preservation of moving Sobolev constants, support geometry,
   homogeneous \(K_2\), \(Y\), \(J_6\), the all-\(p\) defect ladder, and global
   \(Q\);
2. whether every support-selection volume estimate is valid under collapse and
   gives enough inner plateau volume after coloring;
3. conversion on the \(a=1\) plateau to ordinary Ricci flow, local Shi bounds,
   and strong terminal chart convergence;
4. terminal density normalization and the Derdziński contradiction.

Even completion of that review would prove only a dimension-four negative
pinching gap on a particular Ishida--LeBrun geography.  It would not prove or
refute Yau Problem 26, which still requires a dimension-only forcing interval
or failure of both normalized sign branches in some dimension, as well as the
requested Lean formalization.