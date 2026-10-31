# Step 45: coordinate-time tensor ledger and coefficient-regularized closure

## 0. Purpose and scope

Consider, on a closed smooth manifold,

\[
 \partial_t g=-2S,\qquad S=\operatorname{Ric}(U),\qquad
 T=\operatorname{Rm}+G,\qquad
 G={g\owedge g\over 2(n-1)},\qquad U=bT,
 \tag{0.1}
\]

where

\[
 b=b_\varepsilon=\chi^2+\varepsilon^2,\qquad 0\leq\varepsilon\leq1,
 \qquad 0\leq\chi\leq1.
 \tag{0.2}
\]

Thus \(S=b(\operatorname{Ric}+g)\), and \(\varepsilon=0\) is the desired
normalized cutoff flow.  This note repairs two inconsistencies in
`step44_arbitrary_order_tensor_ledger.md`:

1. all raw tensor evolutions and commutators below use coordinate time
   \(\partial_t\), not a metric-compatible time derivative;
2. derivatives of the term \((db*db)*T\) are retained first as
   \((\nabla^{r+1}b)*(\nabla^{s+1}b)*T_t\).  Only then are derivatives of
   \(b=\chi^2+\varepsilon^2\) expanded.  In particular
   \(db*db*T=4\chi^2(d\chi*d\chi)*T\), with the essential factor
   \(\chi^2\).

The result is a triangular finite-exponent propagation whose constants are
uniform in \(\varepsilon\) on a per-datum bootstrap interval.  This is the
analytic input needed by Yang's coefficient-regularization construction.  It
is not a sequence-uniform estimate for the collapsing family and does not by
itself address the full Yau problem.

## 1. One time-derivative convention

Put

\[
 B_r:=\nabla^r b\quad (r\geq1),\qquad
 T_j:=\nabla^jT,\qquad U_j:=\nabla^jU,\qquad C_j:=\nabla^j\chi.
 \tag{1.1}
\]

Every \(\partial_t\) below differentiates coordinate components.  Consequently

\[
 \partial_t b=0,
 \qquad
 \partial_tG={\partial_t(g\owedge g)\over2(n-1)}
             =-{S\owedge g+g\owedge S\over n-1},
 \tag{1.2}
\]

which is algebraic in \(U\).  In particular, we do not simultaneously impose
\(D_tg=0\) and use (1.2).

For any covariant tensor \(A\),

\[
 \partial_t(\nabla^mA)
 =\nabla^m(\partial_tA)
 +\sum_{r+s=m-1}\nabla^r(\partial_t\Gamma)*\nabla^sA,
 \tag{1.3}
\]

where the star includes the action on every covariant derivative and tensor
slot.  Since

\[
 (\partial_t\Gamma)^k{}_{ij}
 =-g^{k\ell}\bigl(\nabla_iS_{j\ell}+\nabla_jS_{i\ell}
                   -\nabla_\ell S_{ij}\bigr),
 \qquad S=\operatorname{Ric}(U),
 \tag{1.4}
\]

and \(\nabla g^{-1}=0\), an ordered covariant derivative gives

\[
 \nabla^r(\partial_t\Gamma)=U_{r+1}*g^{-1}.
 \tag{1.5}
\]

If derivative slots are reordered, Ricci commutation adds curvature times
strictly lower derivatives.  Formula (1.3), not the Step 44 formula for a
metric-compatible \(D_t\), is used throughout.  Variation of tensor norms and
of \(d\mu_g\) is handled only after testing an equation; it contributes
\(S*|A|^p\), bounded by \(C_n\|U_0\|_\infty|A|^p\).

For the fixed scalar \(\chi\), coordinate time gives

\[
 \partial_tC_1=0,
 \qquad
 \partial_tC_{m+1}
 =\sum_{r+s=m-1}U_{r+1}*C_{s+1}\quad(m\geq1),
 \tag{1.6}
\]

again up to slot permutations.  Thus the unique current allocation at stage
\(m\) is \(U_m*C_1\).  There is no \(U_{m+1}\) or \(C_{m+2}\).

## 2. Base curvature and weighted-curvature equations

The exact variation of an all-covariant Riemann tensor under
\(\partial_tg=-2S\), followed by the second Bianchi identity with
\(S=b\operatorname{Ric}(T)\), has the universal-contraction form

\[
 \partial_tT
 =b\Delta T+B_1*\nabla T+B_2*T+b(T*T+T+1).
 \tag{2.1}
\]

Here \(1\) denotes contractions of the parallel bounded tensor \(G\), and the
\(B_2*T\) term retains the actual signed Hessian contractions arising from
\(\nabla^2b*\operatorname{Ric}(T)\).  Equation (2.1) agrees with the
coordinate-time local-Ricci formula in the source used by Wang, lines 414--423
of
`Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md`;
the shift and normalization add only the displayed lower algebraic terms.

Because \(\partial_tb=0\), multiply (2.1) by \(b\), use

\[
 \Delta(bT)=b\Delta T+2B_1*\nabla T+(\Delta b)T,
 \qquad
 \nabla U=b\nabla T+B_1*T,
 \tag{2.2}
\]

to obtain the division-free structural equation

\[
 \partial_tU
 =b\Delta U+B_1*\nabla U+B_2*U
   +(B_1*B_1)*T+U*U+bU+b^2.
 \tag{2.3}
\]

The stars in (2.1)--(2.3) hide fixed numerical coefficients and slot
permutations, not coefficient weights.  In particular the unweighted factor
\(T\) in (2.3) occurs only in \((B_1*B_1)*T\).

The spatial commutator is

\[
 [\nabla^m,\Delta]A
 =\sum_{r+s=m}\nabla^r\operatorname{Rm}*\nabla^sA
 \tag{2.4}
\]

for \(m\geq1\), with the usual omission of tensor-slot terms that vanish in a
particular rank.  Multiplication by \(b\) turns a current zero-order curvature
coefficient into

\[
 b\operatorname{Rm}=b(T-G)=U-bG,
 \tag{2.5}
\]

which is bounded whenever \(U\) is bounded.

## 3. Derivatives of the coefficient

For every \(k\geq1\), the ordered Leibniz expansion is

\[
 B_k=\nabla^k(\chi^2)
 =2\chi C_k+\sum_{\mathcal P_k}^{\prime} C_{|I|}*C_{k-|I|},
 \tag{3.1}
\]

where the primed finite sum ranges over nonempty proper allocations of the
ordered derivative slots.  Hence every jet in the primed sum has order at most
\(k-1\).  The three regularization-uniform identities are

\[
 B_1=2\chi C_1,
 \qquad {|B_1|^2\over b}=4{\chi^2\over b}|C_1|^2\leq4|C_1|^2,
 \qquad 0\leq{\chi^2\over b}\leq1.
 \tag{3.2}
\]

No derivative of \(b^{-1}\) will be taken.

## 4. Complete coordinate-time derivative families

### 4.1 The \(T_m\) equation

Applying \(\nabla^m\) to (2.1), then using (1.3)--(1.5) and (2.4), gives only
these families:

\[
\begin{array}{lll}
 \mathrm{(T1)}&b\Delta T_m,\\
 \mathrm{(T2)}&B_r*T_{m+2-r},&1\leq r\leq m+2,\\
 \mathrm{(T3)}&B_r*T_i*T_j,&r+i+j=m,\quad B_0:=b,\\
 \mathrm{(T4)}&b*\nabla^r\operatorname{Rm}*T_s,&r+s=m\quad\text{(spatial commutator)},\\
 \mathrm{(T5)}&U_{r+1}*T_s,&r+s=m-1\quad\text{(time commutator)},\\
 \mathrm{(T6)}&B_r*T_{m-r}\ \text{and}\ B_m,&0\leq r\leq m.
\end{array}
 \tag{4.1}
\]

The current and next objects in (4.1) are exhausted by

\[
\begin{array}{c|l}
 T_{m+1}&B_1*T_{m+1}=2\chi C_1*T_{m+1},\\
 T_m&B_2*T_m,\quad bT_0*T_m,\quad bT_m,\quad bG*T_m,\\
 C_{m+2}&2\chi C_{m+2}*T_0,\\
 C_{m+1}&C_1*C_{m+1}*T_0,\quad\chi C_{m+1}*T_1,\\
 U_m&U_m*T_0.
\end{array}
 \tag{4.2}
\]

Current \(T_m\) terms from (T3) have coefficient \(bT_0=U_0\), not
unweighted \(T_0\).  In (T4), the zero-order curvature factor is treated by
\(b\operatorname{Rm}=U-bG\); its remaining current term has a bounded
coefficient.  The lower linear term \(bT_m\) is harmless because \(b\le2\).
The norm and volume variations likewise have coefficient
\(S=\operatorname{Ric}(U_0)\).

### 4.2 The \(U_m\) equation

Differentiating (2.3) gives

\[
\begin{array}{lll}
 \mathrm{(U1)}&b\Delta U_m,\\
 \mathrm{(U2)}&B_r*U_{m+2-r},&1\leq r\leq m+2,\\
 \mathrm{(U3)}&B_{r+1}*B_{s+1}*T_t,&r+s+t=m,\\
 \mathrm{(U4)}&U_i*U_j,&i+j=m,\\
 \mathrm{(U5)}&b*\nabla^r\operatorname{Rm}*U_s,&r+s=m\quad\text{(spatial commutator)},\\
 \mathrm{(U6)}&U_{r+1}*U_s,&r+s=m-1\quad\text{(time commutator)},\\
 \mathrm{(U7)}&B_r*U_{m-r}\ \text{and}\ \nabla^m(b^2),&0\leq r\leq m.
\end{array}
 \tag{4.3}
\]

Family (U3) is intentionally left in \(B\)-notation until its derivative
allocations are fixed.  It must not be replaced by
\(C_{r+1}*C_{s+1}*T_t\).

There are two important extremal allocations in (U3).

* A current \(T_m\) occurs only for \(r=s=0\):
  \[
   B_1*B_1*T_m
   =4\chi^2(C_1*C_1)*T_m
   =4{\chi^2\over b}(C_1*C_1)
      *\left[U_m-\sum_{q=1}^m(\nabla^qb)*T_{m-q}\right].
   \tag{4.4}
  \]
  Its current coefficient is uniformly bounded.

* A current cutoff jet \(C_{m+1}\) occurs only for
  \((r,s,t)=(m,0,0)\) or \((0,m,0)\).  Its leading part is
  \[
   (2\chi C_{m+1})*(2\chi C_1)*T_0
   =4{\chi^2\over b}C_{m+1}*C_1*U_0.
   \tag{4.5}
  \]
  The two factors of \(\chi\) are essential: even at \(m=1\), (4.5) has a
  bounded \(U_0\) coefficient and does not ask for \(T_0\in L^\infty\).

After (4.4)--(4.5), the complete current/next table for (4.3) is

\[
\begin{array}{c|l}
 U_{m+1}&2\chi C_1*U_{m+1},\\
 U_m&B_2*U_m,\quad U_0*U_m,\quad bT_0*U_m,\quad bU_m,\quad
       bT_m*U_0\ \text{before (4.4)-type conversion},\quad
       {\chi^2\over b}C_1*C_1*U_m,\\
 C_{m+2}&2\chi C_{m+2}*U_0,\\
 C_{m+1}&C_1*C_{m+1}*U_0,\quad
              \chi C_{m+1}*U_1,\quad
              {\chi^2\over b}C_1*C_{m+1}*U_0.
\end{array}
 \tag{4.6}
\]

There is no \(C_{m+1}*U_j\) with \(j\geq2\).  The corrected (U3) family adds
only the last term in the \(C_{m+1}\) row, and its coefficient is bounded.
The spatial-commutator allocation \(bT_m*U_0\) is converted by the same
Leibniz identity as (4.4), yielding \(U_m*U_0\) plus prior \(T\)-levels; it
does not require the not-yet-completed \(T_m\).

## 5. Signed integrations and finite-exponent closure

Assume on a finite interval that \(|U_0|\leq K\) and the metrics are
bilipschitz equivalent.  At the start of spatial stage \(m\geq1\), suppose all
finite \(L^q\) norms of

\[
 T_j\ (j<m),\qquad U_j,C_{j+1}\ (j<m)
 \tag{5.1}
\]

are finite.  First treat \((U_m,C_{m+1})\), then \(T_m\).

### 5.1 Current weighted pair

Set \(V=U_m\), \(Z=C_{m+1}\), and test the \(U_m\) equation with
\(P(V)=|V|^{p-2}V\).  The derivative term \(B_1*U_{m+1}\) is absorbed by

\[
 {|B_1|^2\over b}\leq4|C_1|^2.
 \tag{5.2}
\]

Every \(B_2*V\) contraction is retained as

\[
 \int (\nabla_i\nabla_jb)\,\mathcal B^{ij}(V),
 \qquad |\mathcal B(V)|\leq C_p|V|^p,
 \qquad |\nabla\mathcal B(V)|\leq C_p|V|^{p-1}|\nabla V|,
 \tag{5.3}
\]

and integrated by parts.  Since \(db=2\chi d\chi\), it is bounded by a small
multiple of \(\int b|\nabla V|^2|V|^{p-2}\) plus
\(C_p\|d\chi\|_\infty^2\|V\|_p^p\).

The top cutoff term \(\chi C_{m+2}*U_0*P(V)\) is integrated once.  It produces

\[
 d\chi*C_{m+1}*U_0*P(V),\quad
 \chi C_{m+1}*U_1*P(V),\quad
 \chi C_{m+1}*U_0*\nabla P(V).
 \tag{5.4}
\]

The last term uses weighted dissipation and leaves
\(|Z|^2|V|^{p-2}\).  For \(m\geq2\), the middle term is integrated once more
by writing the chosen ordered copy of \(C_{m+1}\) as \(\nabla C_m\).  The
result contains

\[
 d\chi*C_m*U_1*P(V),\quad
 \chi C_m*U_2*P(V),\quad
 \chi C_m*U_1*\nabla P(V),
 \tag{5.5}
\]

plus Ricci-commutation remainders \(T_q*C_s*U_1*P(V)\) with
\(q\leq m-1\).  At \(m=2\), the second term in (5.5) is explicitly
\(\int\chi(\nabla_i\nabla_j\chi)\mathcal B^{ij}(U_2)\), with
\(|\mathcal B|\lesssim|U_2|^p\) and
\(|\nabla\mathcal B|\lesssim|U_2|^{p-1}|\nabla U_2|\); it is treated again
by (5.3).  At \(m\geq3\) its factors are previous levels.  At \(m=1\), the original \(\chi C_2*U_1*P(U_1)\) is directly of the
form (5.3).

The corrected (U3) contribution (4.5) is merely a bounded multiple of
\(Z*P(V)\), because \(U_0,C_1,\chi^2/b\) are bounded.  This is the place where
omitting \(\chi^2\) would falsely introduce the unavailable coefficient
\(T_0\) at the base stage.

All remaining terms are either bounded coefficients times \(|V|^p\), or a
forcing \(F\,|V|^{p-1}\) with \(F\in L^p\) obtained from previous factors in
sufficiently large finite exponents.  Current cross-products are only

\[
 |Z||V|^{p-1},\qquad |Z|^2|V|^{p-2}.
 \tag{5.6}
\]

Equation (1.6), tested against \(|Z|^{p-2}Z\), has current term
\(U_m*C_1\), while norm and measure variation has bounded coefficient
\(U_0\).  Therefore

\[
 {d\over dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
 +c_{m,p}\int b|\nabla U_m|^2|U_m|^{p-2}
 \leq C_{m,p}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).
 \tag{5.7}
\]

### 5.2 The subsequent unweighted \(T_m\) estimate

After (5.7), test the \(T_m\) equation.  The \(B_1*T_{m+1}\) term uses
(5.2), and \(B_2*T_m\) uses (5.3).  A current quadratic or spatial-commutator
term has coefficient \(bT_0=U_0\).  A top time-commutator term is
\(U_m*T_0\), which is a forcing in \(L^p\) because both factors are already
known in every finite exponent; it is not treated as a pointwise coefficient.

The only unavailable cutoff jet is \(2\chi C_{m+2}*T_0\).  One integration by
parts produces

\[
 d\chi*C_{m+1}*T_0*P(T_m),\quad
 \chi C_{m+1}*T_1*P(T_m),\quad
 \chi C_{m+1}*T_0*\nabla P(T_m).
 \tag{5.8}
\]

For \(m=1\), the middle term is a signed Hessian contraction in \(T_1\); for
\(m\geq2\), \(T_1\) is a previous level.  The last term leaves
\(|C_{m+1}|^2|T_0|^2|T_m|^{p-2}\), controlled by finite higher exponents of
the already completed factors.  Thus

\[
 {d\over dt}\|T_m\|_p^p
 +c_{m,p}\int b|\nabla T_m|^2|T_m|^{p-2}
 \leq C_{m,p}(1+\|T_m\|_p^p).
 \tag{5.9}
\]

The zero-order estimate in `step44_zero_order_T_seed_repair.md`, with \(b\) in
place of \(a\), starts the ordering

\[
 T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
 \longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots.
 \tag{5.10}
\]

Wang's coordinate-time Lemmas 4.4--4.6 and Propositions 4.13--4.14 exhibit the
same three-way dependence for the unshifted \(b=\chi^2\) flow: weighted
curvature derivatives, unweighted curvature derivatives, and cutoff jets.  The
argument above preserves the factors needed for \(b=\chi^2+\varepsilon^2\)
and adds only lower algebraic normalization terms.

## 6. Uniformity in the coefficient regularization

The constants in (5.7)--(5.9) use only

\[
 0<b\leq2,\qquad B_r=\nabla^r(\chi^2)\ (r\geq1),\qquad
 {|B_1|^2\over b}\leq4|C_1|^2,\qquad {\chi^2\over b}\leq1,
 \tag{6.1}
\]

and finitely many smooth norms of the fixed datum.  They contain no negative
power of \(\varepsilon\).  Initial norms of \(T\), \(U=bT\), and all their
covariant derivatives are uniform for \(0<\varepsilon\leq1\).

For each fixed \(\varepsilon>0\), Yang's Approach 2 supplies a strictly
parabolic DeTurck construction.  In hatted variables the coefficient must be
transported, \(\widehat b_\varepsilon=b_\varepsilon\circ\varphi_t^{-1}\),
so that pullback gives the exact geometric equation

\[
 \partial_tg_\varepsilon
 =-2b_\varepsilon(\operatorname{Ric}_{g_\varepsilon}+g_\varepsilon).
 \tag{6.2}
\]

The fixed-\(\varepsilon\) existence constants may depend on
\(\varepsilon^{-1}\); the common time comes only from the following geometric
energy first-exit argument.

On the first interval where \(|U_\varepsilon|\leq K\) and
\(g_\varepsilon\) is bilipschitz to \(g_0\), (5.7)--(5.10) give every finite
spatial \(L^p\) bound uniformly in \(\varepsilon\).  Taking one more derivative
and using scalar Sobolev embedding gives uniform pointwise bounds for all
\(U_j,T_j\).  Equation (2.3) then bounds \(\partial_tU\), and (0.1) bounds
\(\partial_tg\), uniformly.  Since all initial norms are uniform, a sufficiently
small per-datum time improves both bootstrap bounds.  Fixed-\(\varepsilon\)
parabolic continuation prevents an earlier maximal time.

To turn covariant bounds into fixed-coordinate compactness, fix
\(\bar\nabla=\nabla^{g_0}\) and set
\(A_\varepsilon=\nabla^{g_\varepsilon}-\bar\nabla\).  The identity
\(\partial_tA_\varepsilon=g_\varepsilon^{-1}*\nabla\operatorname{Ric}(U_\varepsilon)\),
followed by induction using \(\bar\nabla=\nabla+A_\varepsilon\), gives uniform
bounds for every \(\bar\nabla^kA_\varepsilon\) and hence every
\(\bar\nabla^kg_\varepsilon\).  Repeated time differentiation of (6.2) uses
only finitely more spatial derivatives and never divides by \(b_\varepsilon\).
Consequently the regularized flows share a positive per-datum interval and
have uniform fixed-coordinate space-time derivatives there.  A diagonal smooth limit solves

\[
 \partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
 \tag{6.3}
\]

The same construction starts from any positive-definite smooth terminal metric,
so smooth time-jet matching supplies at least one restart.  Uniqueness of the
degenerate geometric flow is not supplied by coefficient regularization; it is
unneeded for existence of the continuation used here, but would be needed for
a canonical maximal flow or subsequence-independent regularization limit.  This
route makes reconstruction of Yang's compressed nonlinear smooth-tame inverse
unnecessary for existence and restart, although Yang's transported construction
remains an independent route.

## 7. What this establishes and what remains elsewhere

The corrected coordinate-time identities remove the two structural errors in
the Step 44 ledger.  The retained \(\chi^2\) in (U3) is not cosmetic: it turns
the base-stage factor \(C_2*T_0\) into a bounded \(C_2*U_0\) coupling.  With
that repair, the coefficient-regularized finite-exponent induction has no
current-exponent escalation and no inverse power of \(\varepsilon\).  Two
independent Step 45 TTCS branches reconstructed these families against Wang's
coordinate-time formulas; their corrections to \(\partial_tG\), spatial
commutators, current tables, and the \(m=2\) signed-Hessian endpoint have been
inserted above.  The accompanying scalar/partition script passes 110/110 checks
but, by design, is not evidence for tensor contractions or PDE existence.

This supplies the per-datum start/restart and derivative-propagation interface
for the restricted four-dimensional negative Ishida--LeBrun smoothing route,
subject to independent examination of the tensor-family derivation and the
subsequent simultaneous first-exit application on one common flow.  It does not
prove a dimension-only Ricci-pinching theorem, settle the positive branch,
cover arbitrary four-manifold topology or dimensions \(n\geq5\), or provide
the required Lean formalization.