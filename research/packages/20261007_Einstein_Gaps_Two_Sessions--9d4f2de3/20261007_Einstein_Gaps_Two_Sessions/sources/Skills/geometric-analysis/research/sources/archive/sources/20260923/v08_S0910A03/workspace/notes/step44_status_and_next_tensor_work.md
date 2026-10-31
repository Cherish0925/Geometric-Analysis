# Step 44 consolidated analytic status

## 1. What changed

The continuation package had an invalid base: bounded \(U=aT\) and finite total
curvature do not control unweighted \(T\) near \(a=0\).  The direct energy
calculation now supplies the actual seed:

\[
 \frac d{dt}\int|T|^p+c_p\int a|T|^{p-2}|\nabla T|^2
 \le C_p(K+1+\|d\chi\|_\infty^2)\int|T|^p+C'_p\operatorname{Vol}.
\]

The quadratic reaction closes through \(a|T|^{p+1}=|U||T|^p\), and the
Hessian-cutoff contraction is integrated by parts before taking absolute
values.  TTCS independently confirmed this per-datum endpoint-uniform seed.
The earlier Step 43 assertion that finite total curvature bounded \(T\), and
its use of an \(L^\infty\) Hessian bound at \(m=1\), were corrected.

## 2. Start/restart

Yang Theorem 8.2 gives the exact transported-coefficient system for the
unnormalized local Ricci flow.  Adding \(-2\widehat a\widehat g\) changes the
linearized metric equation only by

\[
 -2\widehat a h+4\widehat\chi\,d\widehat\chi(\zeta)\widehat g,
\]

which is zeroth order in the coupled metric/transport variables.  A direct
same-order \(H^k\) calculation shows that Yang's linear regularization
\(\varepsilon^2\Delta h\) has estimates independent of \(\varepsilon\); the
single-cutoff metric--transport term loses no derivative after one integration
by parts.  This rigorously establishes that the normalization preserves the
principal and weight structure.

What remains if one demands a proof independent of Yang's compressed
“standard tame estimates” sentence is the neighborhood-uniform smooth-tame
inverse: explicit high--low inequalities with fixed derivative loss, the
transport symmetrizer, time norms, and smooth parameter dependence.  The
normalized term itself obeys the needed tame product/composition bounds and
creates no new difficulty.

A complementary coefficient-regularization route was formulated.  Its uniform
identities

\[
 b_\varepsilon=a+\varepsilon^2,\quad
 \nabla^rb_\varepsilon=\nabla^ra\ (r\ge1),\quad
 |db_\varepsilon|^2/b_\varepsilon\le4|d\chi|^2
\]

show that the zero-order seed and signed cutoff integrations are uniform in
\(\varepsilon\).  This route avoids a false small-cutoff Schauder argument, but
it still depends on the full arbitrary-order tensor ledger.

## 3. Remaining proof objects for the restricted negative-family theorem

The analytic obligations are therefore two connected, explicit objects rather
than a vague existence issue:

1. **Arbitrary-order tensor ledger.** Expand
   \([\nabla^m,a\Delta]T\), \([\partial_t,\nabla^m]T\), the analogous
   \(U_m\) equation, every curvature commutator, and each signed Hessian
   contraction.  Prove that current terms are exactly those handled in Step 40:
   weighted gradient, signed \(\chi C_2\), one integration for
   \(\chi C_{m+2}\), and the extra integration for
   \(\chi C_{m+1}U_1\).  Show all reordered terms lie at prior spatial levels.

2. **Start/restart realization.** Either import Yang's Theorem 8.2 as a proved
   nonlinear tame theorem and state the lower-order perturbation lemma cleanly,
   or reconstruct the high--low tame inverse in full.  Alternatively, combine
   the arbitrary-order ledger with coefficient regularization to obtain a
   common per-datum time and smooth limit.  Uniqueness must compare the metric
   and transported coefficient together; smooth extension itself can be pasted
   by matching all autonomous time jets at a smooth endpoint.

The terminal spectral-density reduction remains intact and is preferable to
the abandoned harmonic-form/eigenline extraction.  The full Yau 26 problem is
far beyond this restricted four-dimensional negative-family program: positive
collapse, arbitrary topology, higher dimensions, dimension-only constants,
and Lean formalization remain unresolved.
