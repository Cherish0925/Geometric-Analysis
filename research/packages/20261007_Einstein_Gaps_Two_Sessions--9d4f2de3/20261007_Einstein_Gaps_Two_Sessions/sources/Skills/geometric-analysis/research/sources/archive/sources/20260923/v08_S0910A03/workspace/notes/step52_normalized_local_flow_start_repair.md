# Step 52: Repair of the normalized local-flow start

Session: S0910A03. Agent3 / Actuator. Phase: Execute.

## 0. Outcome

The assertion in Step 51 that the normalized Yang--Wang theorem had been
established is withdrawn.  The critical-curvature-energy argument in
`step51_normalized_yang_precise_estimate.md` does not prove short-time
existence and its claimed homogeneous closure is false.  The correct per-datum
start is instead obtained by applying the detailed fixed-point construction of
Guoyi Xu for Yang's degenerate local Ricci flow to the **metric equation** with
the extra reaction 
\[
        -2\chi^2 g .
\]
This reaction is algebraic in the unknown metric.  It changes only the
zeroth-order part of Xu's strictly parabolic frozen equation.  The maximum
principle, Sobolev energy, contraction, and compactness estimates in Xu's
Section 2 acquire bounded Gronwall terms but no new derivatives and no inverse
power of the regularization parameter.  Thus they close after decreasing the
per-datum time.  This route is independent of critical curvature smallness and
of the false Step 51 curvature-energy closure.

The positive-time shifted-curvature/cutoff-jet continuation developed in Step
50 remains a separate result.  This note addresses only arbitrary smooth
per-datum start and restart.

## 1. Flat-data falsification of Step 51

Take the flat four-torus with coordinates of period \(2\pi\), and
\[
 \chi(x_1)={1+\cos x_1\over2},\qquad a=\chi^2.
\]
At time zero, \(\operatorname{Ric}=0\), so the normalized flow has
\(\dot g=-2ag\).  The fully lowered curvature variation is
\[
     \dot{\operatorname{Rm}}=g\owedge\operatorname{Hess}a.
\]
For this cutoff,
\[
  a''(x_1)=-{\cos x_1+\cos 2x_1\over2},
 \qquad |g\owedge\operatorname{Hess}a|^2=12(a'')^2.
\]
Consequently
\[
 \int_{T^4}|\operatorname{Rm}(g(t))|^2\,d\mu_{g(t)}
   =48\pi^4t^2+O(t^3).
 \tag{1.1}
\]
The exact symbolic enumeration is in
`workspace/scripts/step52_flat_cutoff_forcing_test.py`; its output is
`workspace/data/step52_flat_cutoff_forcing_test.json`.

Equation (1.1) immediately rules out any homogeneous estimate
\(E'(t)\le C E(t)\) for the unshifted critical curvature energy near zero:
\(E'/E=2/t+O(1)\).  The cancellation of the coefficient \(2p-n\) at
\(p=n/2\) concerns only constant homothety.  Spatial variation of \(a\) creates
the genuine \(g\owedge\nabla^2a\) forcing.

The error in Step 51's integration by parts can also be seen directly.  From
\[
 \int F^{p-2}\operatorname{Ric}_{ij}\nabla_i\nabla_j a
\]
one integration gives terms of size
\[
 |da|F^{p-2}|\nabla\operatorname{Ric}|
 \quad\hbox{and}\quad
 |da|F^{p-2}|\operatorname{Ric}|\,|\nabla F|.
\]
Absorption by \(aF^{p-2}|\nabla\operatorname{Rm}|^2\) leaves
\[
       {|da|^2\over a}F^{p-2},
\]
not \(F^p\).  Integrating the contracted-Bianchi term again instead restores
\(\Delta_g a\), whose sequence-uniform bound is not available before the
cutoff-jet hierarchy.  Thus a lower-power/volume forcing is real.  It may be
handled in a shifted norm such as \(1+|\operatorname{Rm}|\) for a quantitative
estimate with correspondingly altered hypotheses, but it neither proves
arbitrary-data existence nor yields the homogeneous Moser statement claimed in
Step 51.

## 2. The detailed existence source that separates start from smoothing

Yang's Theorem 8.2 states arbitrary smooth short-time existence for
\(\partial_tg=-2\chi^2\operatorname{Ric}\), while Yang's Theorem 9.2 imposes
small critical curvature energy to obtain a **uniform smoothing time and
curvature estimate**.  These are different theorems.

Guoyi Xu, *Short-time existence of the Ricci flow on noncompact Riemannian
manifolds* \cite{xu2018short}, gives the first detailed proof of Yang's start.
The source used here is the downloaded v3 PDF
`staging/downloads/0907.5604.pdf`, converted for inspection to
`staging/processing/xu_local_ricci_flow.txt`.

Xu's Section 2 writes the local Ricci--DeTurck metric equation relative to the
initial metric \(\widetilde g\) as
\[
 \partial_tg=\chi^2 g^{\alpha\beta}
 \widetilde\nabla_\alpha\widetilde\nabla_\beta g
       +D(g,g)+B(g,\widetilde\nabla g),                       \tag{2.1}
\]
where \(D\) is algebraic and linear in its second metric argument and \(B\) is
quadratic/first-order.  Unlike Yang's compressed transported-pair proof, Xu
regularizes and freezes the metric coefficients directly.  For
\(0<\varepsilon\le1\), given a positive-definite tensor \(U\), define
\(V=\Phi_\varepsilon(U)\) by the strictly parabolic problem
\[
 \partial_tV=(\chi^2+\varepsilon)U^{-1}*
     \widetilde\nabla^2V+D(U,V)+B(U,\widetilde\nabla U),       \tag{2.2}
\]
with the fixed initial and boundary metric.  Xu proves, on a time independent
of \(\varepsilon\):

1. \(\Phi_\varepsilon\) preserves a bilipschitz, high-Sobolev ball
   (Propositions 2.5 and 2.7; converted lines 399--764);
2. it is a contraction in a lower Sobolev norm (Proposition 2.8, lines
   766--1026);
3. its fixed point has estimates independent of \(\varepsilon\), and a
   subsequence converges to a smooth solution of the degenerate equation
   (Theorem 2.9, lines 1027--1106).

The time depends on the full smooth datum, cutoff, domain, and initial Sobolev
constant.  No critical-energy smallness is used in this start.  Xu explicitly
separates this from the later domain-uniform time estimates in Sections 5--6.

## 3. Normalized extension of Xu's fixed-point construction

### 3.1 Modified Ricci--DeTurck equation

Add the geometric normalization to Xu's first equation:
\[
 \partial_tg=-2\chi^2(\operatorname{Ric}_g+g)
       +\mathcal L_{\chi^2W(g,\widetilde g)}g .               \tag{3.1}
\]
The same diffeomorphism equation
\[
       \partial_t\varphi=-\chi^2W\circ\varphi                 \tag{3.2}
\]
removes the Lie derivative.  Naturality of the Ricci tensor and
\(\varphi^*(\chi^2g)=\chi^2\varphi^*g\) then gives the exact geometric flow
\[
       \partial_t(\varphi^*g)
       =-2\chi^2\bigl(\operatorname{Ric}_{\varphi^*g}
                       +\varphi^*g\bigr).                     \tag{3.3}
\]
Here \(\chi\) is fixed in Xu's Eulerian formulation, so no transported-cutoff
composition is needed.

Relative to \(\widetilde\nabla\), (3.1) is simply
\[
 \partial_tg=\chi^2g^{-1}*\widetilde\nabla^2g
       +D(g,g)+B(g,\widetilde\nabla g)-2\chi^2g.               \tag{3.4}
\]
For frozen \(U\), define the normalized solution map
\(\Phi^N_\varepsilon(U)=V\) by
\[
 \partial_tV=(\chi^2+\varepsilon)U^{-1}*
   \widetilde\nabla^2V+D(U,V)+B(U,\widetilde\nabla U)
   -2\chi^2V.                                                  \tag{3.5}
\]
This is the exact regularization needed for the normalized degenerate metric
equation.  The extra term is linear in \(V\), contains no spatial derivative,
and is independent of \(\varepsilon\).

### 3.2 Invariance of Xu's ball

Xu controls positive definiteness by scalar functions made from powers of the
eigenvalues of \(V\) relative to \(\widetilde g\).  Under the new term alone,
\(\dot V=-2\chi^2V\), hence
\[
       \dot V^{-1}=2\chi^2V^{-1}.
\]
For Xu's power traces \(\phi_m=\operatorname{tr}(V^{-m})\) and
\(\psi_m=\operatorname{tr}(V^m)\), the additions are respectively
\[
       (\partial_t\phi_m)_N=2m\chi^2\phi_m,
       \qquad
       (\partial_t\psi_m)_N=-2m\chi^2\psi_m.                 \tag{3.6}
\]
Thus Xu's maximum-principle inequalities acquire at worst
\(2m\phi_m\) and \(2m\psi_m\).  The same ODE comparison closes after reducing
his \(t_1\); no derivative or \(\varepsilon^{-1}\) appears.

For a fixed-background Sobolev energy
\[
       \|V\|_m^2=\sum_{|\alpha|\le m}
          \|\widetilde\nabla^\alpha V\|_2^2,
\]
fixedness of \(\chi\) and the product estimate give
\[
 \begin{aligned}
 \left|\sum_{|\alpha|\le m}
  \langle\widetilde\nabla^\alpha V,
   \widetilde\nabla^\alpha(-2\chi^2V)\rangle\right|
 &\le C_m\|\chi\|_{C^m}^2\|V\|_m^2 .                       \tag{3.7}
 \end{aligned}
\]
Xu's inequality (2.22) therefore changes only by a bounded multiple of
\(\|V\|_m^2\).  Propositions 2.5 and 2.7 still hold, with a smaller time
depending on \(\|\chi\|_{C^m}\).

### 3.3 Contraction

Let \(V=\Phi^N_\varepsilon(U)\),
\(\widetilde V=\Phi^N_\varepsilon(\widetilde U)\), and
\(W=V-\widetilde V\).  Because the reaction coefficient is the same fixed
\(\chi^2\), the difference equation gains exactly
\[
                  -2\chi^2W.                                 \tag{3.8}
\]
At every fixed-background Sobolev order \(m\),
\[
 \left|\sum_{|\alpha|\le m}
  \langle\widetilde\nabla^\alpha W,
   \widetilde\nabla^\alpha(-2\chi^2W)\rangle\right|
 \le C_m\|\chi\|_{C^m}^2\|W\|_m^2.                           \tag{3.9}
\]
Accordingly Xu's difference inequality (2.49) becomes
\[
 {d\over dt}\|W\|_{\widetilde p}^2
 \le (C_1+C_N)\|W\|_{\widetilde p}^2
       +C_2\|U-\widetilde U\|_{\widetilde p}^2.               \tag{3.10}
\]
Since \(W(0)=0\),
\[
 \|W\|_{T,\widetilde p}^2
 \le C_2T e^{(C_1+C_N)T}
       \|U-\widetilde U\|_{T,\widetilde p}^2.                 \tag{3.11}
\]
Choosing \(T\) so this coefficient is below \(1/4\) gives the same contraction
constant \(1/2\).  The new term therefore strengthens neither the derivative
nor regularization requirements of the fixed-point map.

### 3.4 The \(\varepsilon\to0\) limit

The high-Sobolev estimates used by Xu are changed only by (3.7), uniformly in
\(\varepsilon\).  Time derivatives obtained from (3.5) acquire
\(-2\chi^2V\), already controlled in the same spaces.  Hence Xu's compactness
argument passes to a limit satisfying (3.4).  Smoothness follows in
\(\{\chi>0\}\) by ordinary parabolic regularity.  On the interior of
\(\{\chi=0\}\), every term in the exact equation vanishes and the metric is
stationary.  Xu's Theorem 2.9 uses this same two-region conclusion.  If one
needs smoothness precisely at a non-flat interface, the global fixed-background
Sobolev bounds, rather than an interior Schauder assertion, provide it; this is
why the estimates are carried at arbitrary finite order before the diagonal
limit.

We therefore obtain the following per-datum result.

**Proposition 3.1 (normalized Xu--Yang start).**  Let \(M\) be closed,
\(g_0\) a smooth Riemannian metric, and \(\chi\) a smooth function.  There is a
\(T=T(g_0,\chi)>0\) and a smooth solution
\[
      \partial_tg=-2\chi^2(\operatorname{Ric}_g+g),
      \qquad g(0)=g_0,
\]
on \([0,T]\).  The same construction applies to any smooth positive-definite
restart datum.  The time is not asserted to be uniform across a collapsing
sequence.

The proof is Xu's Section 2 fixed-point argument with the explicit changes
(3.6)--(3.11), followed by the unchanged DeTurck pullback (3.2)--(3.3).  It
requires arbitrary smooth per-datum Sobolev bounds, but no small critical
curvature energy.

## 4. What survives downstream

The valid analytic architecture is now:

1. **Per-datum start/restart:** Proposition 3.1, based on Xu's detailed
   fixed-point construction, with the normalization treated as the algebraic
   reaction \(-2\chi^2V\).
2. **Quantitative exact-flow estimates:** begin only after the exact degenerate
   flow exists.  The Step 51 unshifted homogeneous critical-energy estimate is
   not among them; true spatial forcing must be retained.
3. **Positive-time continuation:** the Step 50 shifted variables
   \(T=\operatorname{Rm}+g\owedge g/[2(n-1)]\), \(U=\chi^2T\), together with
   the coupled cutoff jets, remain the appropriate mechanism.  This theorem
   should be cited separately from the start.

This repairs only the analytic start required by the restricted
four-dimensional negative program.  The sequence-uniform first-exit estimates
still require a new connected reading that does not import Step 51's false
homogeneous curvature-energy statement.  The full Yau Problem 26 remains open:
the restricted IL geography, the positive product-quotient wall, arbitrary
four-manifold topology, dimensions \(n\ge5\), dimension-only constants, and Lean
formalization are not resolved here.

## 5. TTCS correction: the metric-only Xu extension does not yet give the fixed-cutoff geometric flow

The TTCS verification `trace/ttcs/results/step52_ttcs01_verifier1_integration.md`
confirmed the flat-torus falsification of Step 51 and confirmed that the
algebraic reaction \(-2\chi^2V\) is harmless inside Xu's **fixed Eulerian
coefficient** frozen parabolic map.  It also found a decisive error in §3 above:
the DeTurck pullback does not preserve the fixed cutoff factor.

If a gauge-fixed equation with fixed \(a=\chi^2\) is solved and
\(\partial_t\varphi=-(aW)\circ\varphi\), then
\[
 \partial_t(\varphi^*\widehat g)
 =-2\varphi^*\!igl(a(\operatorname{Ric}_{\widehat g}+\widehat g)\bigr)
 =-2(a\circ\varphi)(\operatorname{Ric}_{\varphi^*\widehat g}
      +\varphi^*\widehat g),
\]
not \(-2a(\operatorname{Ric}+g)\).  The identity
\(\varphi^*(a\widehat g)=a\varphi^*\widehat g\) used in §3.1 is false unless
\(a\circ\varphi=a\).  Xu's metric-only fixed-point construction therefore
supplies at most a flow with a transported cutoff in geometric coordinates; it
does not establish Proposition 3.1 as stated.

The harmless-zero-order conclusion should be retained only as an estimate inside
a fixed-coordinate model equation.  The actual fixed-cutoff geometric start
requires a transported coefficient.  In hatted coordinates set
\[
   \widehat a=a\circ\varphi^{-1},
   \qquad X=-\widehat a W(\widehat g,S).
\]
Then
\[
   \partial_t\widehat a+X(\widehat a)=0,
   \quad\hbox{equivalently}\quad
   \partial_t\widehat a=\widehat a W(\widehat a),             \tag{5.1}
\]
and \((\widehat a\circ\varphi)(t)=a\).  The correct gauge-fixed normalized
system is
\[
\begin{cases}
 \partial_t\widehat g
 =-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
       +\mathcal L_{\widehat a W(\widehat g,S)}\widehat g,\\[1mm]
 \partial_t\widehat a=\widehat a W(\widehat a),\qquad
 \widehat g(0)=g_0,\\ 
 \widehat a(0)=a .
\end{cases}                                                   \tag{5.2}
\]
Solving (5.2) and pulling back by
\(\partial_t\varphi=-(\widehat a W)\circ\varphi\) gives the exact fixed-cutoff
flow
\[
        \partial_tg=-2a(\operatorname{Ric}_g+g).              \tag{5.3}
\]

Thus the remaining analytic task is not another curvature-energy closure but a
coupled existence proof for (5.2).  The expected estimates are plausible:

* the metric equation has the same degenerate principal part as Xu/Yang with
  coefficient \(\widehat a\); the normalization is still the algebraic reaction
  \(-2\widehat a\widehat g\);
* the scalar coefficient equation is first-order transport by a vector field
  containing one derivative of \(\widehat g\), so high Sobolev norms of
  \(\widehat a\) must be propagated together with metric norms;
* in differences, terms like
  \((\widehat a_1-\widehat a_2)(\operatorname{Ric}_{\widehat g_2}+\widehat g_2)
  and \((W_1-W_2)(\widehat a_2)\) appear, requiring the same staggered
  metric/transport grading already visible in Yang's displayed \((h,\psi)
  linearization;
* no small critical curvature energy should be assumed for start/restart; the
  time may depend on all smooth norms of \((g_0,a)\).

This restores the status to the Step 50 conclusion, sharpened by the Xu source:
the fixed-cutoff start remains a specific coupled Yang-transport existence
problem.  The metric-only Xu perturbation is a useful local model, not a proof of
the geometric equation.  The positive-time shifted Wang continuation remains
separate and can only be used after such an exact start is obtained.
