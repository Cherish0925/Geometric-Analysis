# Step 44: coefficient-regularized start from global per-datum energies

> **Step 45 update.** The conditional tensor ledger required below has been replaced by the coordinate-time construction in `step45_coordinate_tensor_ledger_and_regularized_closure.md`. That note retains the exact \(B_{r+1}B_{s+1}T_t\) weights, uses a transported fixed-\(\varepsilon\) DeTurck coefficient, obtains a common per-datum time by geometric energies, and records fixed-background smooth compactness and restart. Use the Step 45 version rather than the Step 44 schematic ledger.

## 0. Motivation

Yang gives two constructions of local Ricci flow.  His Approach 1 uses the
transported-coefficient tame inverse.  His Approach 2 solves the strictly
parabolic coefficient-regularized flows and passes to the degenerate limit by
regularization-uniform curvature energies.  The latter is particularly well
matched to the repaired continuation package: Step 44 now supplies the missing
unweighted \(T_0\) energy, and Step 40 supplies the staggered derivative
mechanism.

This route must be global and per datum.  It does **not** argue that the region
\(\{a\ll1\}\) has trivial dynamics, and it does not infer derivative control
from small metric displacement.

> **Status.** Sections 1--2 below identify a viable route and the exact
> regularization-invariant identities.  Sections 2.2--4 are conditional on a
> complete arbitrary-order tensor ledger for the regularized shifted equation.
> The existing Step 40 star-notation and TTCS exponent checks do not by
> themselves prove that ledger, so this note is not yet a stand-alone existence
> theorem.

## 1. Regularized geometric equations

For \(0<\varepsilon\le1\), put

\[
 b_\varepsilon=a+\varepsilon^2=\chi^2+\varepsilon^2
\]

and solve

\[
 \partial_tg_\varepsilon
 =-2b_\varepsilon(\operatorname{Ric}_{g_\varepsilon}+g_\varepsilon),
 \qquad g_\varepsilon(0)=g_0.                                  \tag{1.1}
\]

For each fixed \(\varepsilon>0\), Yang Approach 2 reduces the unnormalized
version to a strictly parabolic DeTurck system.  The added
\(-2b_\varepsilon g_\varepsilon\) is smooth and zeroth order, so standard
strictly parabolic theory supplies a unique smooth solution on an interval
\([0,T_\varepsilon)\).  No uniform lower ellipticity is needed at this point.

Set

\[
 T_\varepsilon=\operatorname{Rm}_{g_\varepsilon}
 +\frac{g_\varepsilon\owedge g_\varepsilon}{2(n-1)},
 \qquad U_\varepsilon=b_\varepsilon T_\varepsilon.              \tag{1.2}
\]

Then

\[
 \operatorname{Ric}(T_\varepsilon)=E_\varepsilon,
 \quad
 \operatorname{Ric}(U_\varepsilon)=b_\varepsilon E_\varepsilon,
 \quad
 \partial_tg_\varepsilon=-2\operatorname{Ric}(U_\varepsilon).  \tag{1.3}
\]

The regularization has three uniform identities:

\[
 0<b_\varepsilon\le2,
 \qquad \nabla^rb_\varepsilon=\nabla^ra\quad(r\ge1),
 \qquad
 \frac{|db_\varepsilon|^2}{b_\varepsilon}
 =\frac{|da|^2}{a+\varepsilon^2}\le4|d\chi|^2.                  \tag{1.4}
\]

They are exactly what the degenerate energy estimates use.

## 2. Uniform bootstrap interval

Let

\[
 K_0=1+\sup_{0<\varepsilon\le1}
       \|U_\varepsilon(0)\|_{C^0(g_0)}<\infty,                  \tag{2.1}
\]

which is finite because \(g_0,\chi\) are fixed and smooth.  Fix
\(K=2K_0\).  On the maximal subinterval on which

\[
 \|U_\varepsilon\|_\infty\le K,
 \qquad \tfrac12g_0\le g_\varepsilon\le2g_0,                   \tag{2.2}
\]

the following estimates have constants depending on the full datum
\((g_0,\chi)\), \(K\), and derivative order, but not on \(\varepsilon\).

### 2.1 Zero-order unweighted seed

Repeat `step44_zero_order_T_seed_repair.md` with \(b_\varepsilon\) in place of
\(a\).  The only quotient is controlled by (1.4), the reaction satisfies

\[
 b_\varepsilon|T_\varepsilon|^{p+1}
 =|U_\varepsilon||T_\varepsilon|^p\le K|T_\varepsilon|^p,
\]

and the signed Hessian term uses
\(\nabla^2b_\varepsilon=\nabla^2a\) followed by integration by parts.  Thus,
for each finite \(p\ge2\),

\[
 \sup_{t}\|T_\varepsilon(t)\|_{L^p}^p
 +\int b_\varepsilon|T_\varepsilon|^{p-2}
        |\nabla T_\varepsilon|^2
 \le C_p(g_0,\chi,K,T),                                        \tag{2.3}
\]

uniformly in \(\varepsilon\).

### 2.2 Staggered derivatives

The Step 40 schedule remains valid with \(b_\varepsilon\) replacing \(a\):

\[
 T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to T_2\to\cdots,           \tag{2.4}
\]

where \(C_j=\nabla^j\chi\).  The reason the constants stay uniform is not a
uniform ellipticity estimate:

* every positive diffusion term \(a|\nabla X|^2\) is replaced by the larger
  \(b_\varepsilon|\nabla X|^2\);
* every derivative of \(b_\varepsilon\) equals the corresponding derivative
  of \(a\);
* every first-derivative quotient is controlled by (1.4);
* every quadratic reaction uses the bounded coefficient
  \(b_\varepsilon T_\varepsilon=U_\varepsilon\);
* the signed Hessian and top-cutoff integrations by parts are unchanged,
  because the constant \(\varepsilon^2\) disappears upon differentiation;
* connection variation remains
  \(\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U_\varepsilon)\).

If the full tensor ledger confirms that every commutator and signed contraction
falls into these families, it yields, for every finite set of orders and
exponents,

\[
 \sup_t\bigl(
 \|\nabla^mU_\varepsilon\|_{L^p}
 +\|\nabla^{m+1}\chi\|_{L^p}
 +\|\nabla^mT_\varepsilon\|_{L^p}
 \bigr)\le C_{m,p},                                             \tag{2.5}
\]

with \(C_{m,p}\) independent of \(\varepsilon\) on the bootstrap interval.
The missing verification is not an exponent issue: it is the exhaustive
index-level expansion of $[\nabla^m,b_\varepsilon\Delta]$, time-connection
commutators, and all Hessian-cutoff contractions.
At \(m=1\), the term
\(\chi\operatorname{Hess}\chi*|\nabla T|^p\) is treated by signed
integration by parts, never by a uniform Hessian bound.

## 3. Uniform first-exit improvement

Take \(m_0>n/2+4\) in (2.5).  Fixed-background Sobolev comparison from (2.2)
gives a uniform bound

\[
 \|U_\varepsilon\|_{C^2}
 +\|T_\varepsilon\|_{C^1}
 \le C(g_0,\chi,K)                                               \tag{3.1}
\]

on the bootstrap interval.  More safely, choose two additional derivative
levels in (2.5).  The evolution equation for \(U_\varepsilon\) then yields

\[
 \|\partial_tU_\varepsilon\|_{C^0}
 \le C(g_0,\chi,K),                                             \tag{3.2}
\]

uniformly in \(\varepsilon\).  Likewise,

\[
 \|\partial_tg_\varepsilon\|_{C^0}
 =2\|\operatorname{Ric}(U_\varepsilon)\|_{C^0}
 \le C_nK.                                                       \tag{3.3}
\]

Since \(\|U_\varepsilon(0)\|_\infty\le K_0-1\), choose a time
\(T_0=T_0(g_0,\chi)>0\) so small that

\[
 C T_0<\tfrac12,
 \qquad C_nKT_0<\log 2/2.                                      \tag{3.4}
\]

Then throughout \([0,T_0]\), (3.2) improves the first inequality in (2.2) to
\(\|U_\varepsilon\|_\infty<K_0\), and (3.3) improves the metric comparison.
If a fixed-\(\varepsilon\) strictly parabolic solution had maximal time below
\(T_0\) without a first exit, (2.5) and standard fixed-\(\varepsilon\)
parabolic continuation would extend it.  Hence all regularized flows exist on
the same \([0,T_0]\), and all bounds above hold there uniformly in
\(\varepsilon\).

This is the point at which per-datum high derivatives of the exterior geometry
are allowed: they enter \(C_{m,p}(g_0,\chi,K)\) but never through
\(\varepsilon^{-1}\).

## 4. Smooth degenerate limit

Equations (2.5), (3.2), and repeated time differentiation of (1.1) give
uniform space--time derivative bounds of every fixed order.  On the compact
manifold, a diagonal Arzela--Ascoli argument gives

\[
 g_{\varepsilon_j}\longrightarrow g
 \quad\text{in }C^\infty(M\times[0,T_0])                         \tag{4.1}
\]

along a subsequence.  Since \(b_{\varepsilon_j}\to a\) smoothly, passage to
the equation gives

\[
 \partial_tg=-2a(\operatorname{Ric}_g+g),\qquad g(0)=g_0.        \tag{4.2}
\]

At \(a=0\), this follows from the equation and smooth convergence; it is not
inferred from an informal claim that the regularized dynamics there are
trivial.

Thus the coefficient-regularization route would supply **existence** of a smooth
degenerate flow for a positive per-datum time once the full Step 40 staggered
tensor-energy ledger is established uniformly for $b_\varepsilon$.  Existence
alone would then suffice to initiate the sequence-uniform first-exit estimates.

## 5. Restart without using uniqueness

Suppose the derivative continuation argument gives a positive-definite
\(C^\infty\) endpoint metric \(g_*\) at time \(T_*\).  Conditional on completing the regularized construction above, apply it to
\((g_*,\chi)\), obtaining a right-hand solution.  Because (4.2) is
autonomous and both one-sided metrics converge smoothly to \(g_*\), their time
jets agree recursively:

\[
 \partial_tg(T_*^\pm)=F(g_*),
 \quad
 \partial_t^2g(T_*^\pm)=DF(g_*)[F(g_*)],
 \quad\ldots,                                                    \tag{5.1}
\]

where \(F(g)=-2a(\operatorname{Ric}_g+g)\).  Hence the concatenated metric is
smooth and solves the equation across \(T_*\).  A uniqueness theorem is useful
for a canonical maximal flow, but it is not needed for the existence of this
extension or for the contradiction argument.

## 6. Remaining precision

This route replaces the unsupported small-cutoff Schauder claim by global,
regularization-uniform per-datum energies.  Its load-bearing ingredients are
now explicit: the zero-order seed, the staggered derivative induction, and the
uniform first-exit interpolation.

For a fully self-contained theorem, the arbitrary-order tensor ledger in the
Step 40 induction must still be written rather than represented only by
schematic stars: one must enumerate the commutators of \(\nabla^m\) with
\(b_\varepsilon\Delta\), the connection-variation terms, and every signed
Hessian contraction.  The coefficient-regularization argument itself adds no
new exponent or cutoff-weight obstruction; its remaining dependence is exactly
that ledger.
