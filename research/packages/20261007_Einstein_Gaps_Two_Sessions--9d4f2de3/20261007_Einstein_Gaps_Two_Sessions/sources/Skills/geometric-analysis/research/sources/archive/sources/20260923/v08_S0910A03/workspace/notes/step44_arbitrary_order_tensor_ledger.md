# Step 44: arbitrary-order tensor ledger for the shifted cutoff flow

> **Superseded by Step 45.** This ledger mixes a metric-compatible time derivative with coordinate-time identities and drops essential \(\chi\)-factors when differentiating \((db*db)T\). Do not use its equations (1.2), (1.8), or family (U3) as proof. The repaired coordinate-time ledger, coefficient weights, independent verification, and regularization closure are in `step45_coordinate_tensor_ledger_and_regularized_closure.md`.

## 0. Aim and notation

This note replaces an appeal to schematic derivative counting by an exhaustive
partition ledger.  It covers both the degenerate coefficient

\[
 b=a=\chi^2
\]

and Yang's coefficient regularization

\[
 b=b_\varepsilon=\chi^2+\varepsilon^2,
 \qquad 0<\varepsilon\le1.                                     \tag{0.1}
\]

Let

\[
 T=\operatorname{Rm}+G,
 \qquad G=\frac{g\owedge g}{2(n-1)},
 \qquad U=bT,
 \qquad S=\operatorname{Ric}(U)=b(\operatorname{Ric}+g),        \tag{0.2}
\]

and evolve by \(\partial_tg=-2S\).  Write

\[
 T_j=\nabla^jT,
 \qquad U_j=\nabla^jU,
 \qquad C_j=\nabla^j\chi.                                      \tag{0.3}
\]

A star denotes a finite universal linear combination of contractions with
\(g,g^{-1}\).  Every displayed sum below specifies all derivative partitions;
the star hides only slot permutations and dimension-dependent numerical
coefficients.  We use a metric-compatible time derivative \(D_t\); replacing it
by coordinate \(\partial_t\) adds only \(S*X=U*X\) algebraic terms already
listed below.

The induction stage is

\[
 T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
 \longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots. \tag{0.4}
\]

At stage \(m\ge1\), all finite \(L^q\) norms of \(T_j\) for \(j<m\), and of
\(U_j,C_{j+1}\) for \(j<m\), are already known.  The current pair is
\((U_m,C_{m+1})\); \(T_m\) is treated afterwards.

## 1. Universal identities generating every term

For \(S=\operatorname{Ric}(U)\), the metric variation identities give

\[
 D_t\operatorname{Rm}=\mathscr D^2S+\operatorname{Rm}*S,
 \qquad
 \partial_t\Gamma=g^{-1}*\nabla S.                              \tag{1.1}
\]

The contracted second Bianchi identity applied to
\(S=b\operatorname{Ric}(T)\), together with \(\nabla G=0\), gives the structural
identity

\[
 D_tT
 =b\Delta T+db*\nabla T+(\nabla^2b)*T
  +b(T*T+T+1).                                                   \tag{1.2}
\]

Here the Hessian term includes the exact traces with
\(E=\operatorname{Ric}(T)\), and every algebraic term is a contraction of the
listed factors.  The shift contributes no spatial derivative because
\(\nabla G=0\), while
\(D_tG=bT*G+bG*G\) is included in the last bracket.

Multiplying (1.2) by \(b\), using \(D_tb=0\), and applying

\[
 \Delta(bT)=b\Delta T+2db*\nabla T+(\Delta b)*T                  \tag{1.3}
\]

yields a division-free equation

\[
 D_tU
 =b\Delta U+db*\nabla U+(\nabla^2b)*U
  +(db*db)*T+U*U+bU+b^2.                                       \tag{1.4}
\]

The coefficients in front of the displayed contractions are immaterial; (1.4)
is an equality in the universal-contraction sense.  It is important that the
only remaining unweighted factor in (1.4) is in \((db*db)*T\).  Since

\[
 db=2\chi\,d\chi,
 \qquad db*db=4a(d\chi*d\chi),                                  \tag{1.5}
\]

its occurrence with a current \(T_m\) can be rewritten using

\[
 bT_m
 =U_m-
   \sum_{r=1}^{m}{m\choose r}(\nabla^rb)*T_{m-r},
 \qquad 0\le a/b\le1.                                          \tag{1.6}
\]

Thus it never demands \(T_m\) before the \(T_m\)-stage, uniformly in
\(\varepsilon\).

Two commutator identities complete the ledger.  For every covariant tensor
\(A\),

\[
 [\nabla^m,\Delta]A
 =\sum_{r+s=m}\nabla^r\operatorname{Rm}*\nabla^sA,               \tag{1.7}
\]

where terms with impossible negative derivative orders are omitted, and

\[
 [D_t,\nabla^m]A
 =\sum_{r+s=m-1}\nabla^r(\partial_t\Gamma)*\nabla^sA
 =\sum_{r+s=m-1}U_{r+1}*\nabla^sA.                              \tag{1.8}
\]

The last equality uses \(\nabla^r\partial_t\Gamma
=g^{-1}*\nabla^{r+1}\operatorname{Ric}(U)\); metric contraction commutes with
\(\nabla\).  If derivative slots are reordered, the resulting commutators are
again instances of (1.7), with strictly lower total derivative order in the
factor being reordered.

## 2. Complete differentiated \(T_m\) families

Apply \(\nabla^m\) to (1.2), use (1.7)--(1.8), and collect terms by derivative
partition.  Apart from bounded contractions with \(G\), every term belongs to
one of the following families:

\[
\begin{array}{lll}
\mathrm{(T1)}&b\Delta T_m,&\\
\mathrm{(T2)}&(\nabla^rb)*T_{m+2-r},&1\le r\le m+2,\\
\mathrm{(T3)}&(\nabla^rb)*T_i*T_j,&r+i+j=m,\\
\mathrm{(T4)}&b*T_i*T_j,&i+j=m\quad\text{(from (1.7))},\\
\mathrm{(T5)}&U_{r+1}*T_s,&r+s=m-1\quad\text{(from (1.8))},\\
\mathrm{(T6)}&(\nabla^rb)*T_{m-r}\ \text{or}\ \nabla^mb,&0\le r\le m.
\end{array}                                                       \tag{2.1}
\]

Families (T3)--(T4) may be combined; they are separated to record their
origins.  This list is exhaustive because (1.2) has only the five base
monomials \(b\Delta T\), \(db*\nabla T\), \(\nabla^2b*T\), \(bT*T\), and
lower algebraic \(b(T+1)\), while (1.7)--(1.8) list every commutator.

### 2.1 Every current or next object in (2.1)

The only terms involving \(T_{m+1}\), \(T_m\), \(C_{m+2}\), or the current
pair \(U_m,C_{m+1}\) are:

\[
\begin{array}{c|l}
\text{object}&\text{all possible structures}\\ \hline
T_{m+1}&db*T_{m+1}=2\chi C_1*T_{m+1},\\
T_m&(\nabla^2b)*T_m,\quad bT_0*T_m,\\
C_{m+2}&2\chi C_{m+2}*T_0,\\
C_{m+1}&C_1*C_{m+1}*T_0,\quad \chi C_{m+1}*T_1,\\
U_m&U_m*T_0.
\end{array}                                                       \tag{2.2}
\]

To see completeness, in (T2) solve \(m+2-r=m+1,m\), or \(0\); in the
Leibniz expansion

\[
 \nabla^rb=2\chi C_r+
  \sum_{\substack{\alpha+\beta=r\\\alpha,\beta\ge1}}
  {r\choose\alpha}C_\alpha*C_\beta,                              \tag{2.3}
\]

only the first summand contains \(C_r\).  In (T3)--(T4), a current \(T_m\)
forces all other derivative orders to be zero, and its coefficient is
\(bT_0=U_0\).  In (T5), the top allocation is exactly \(U_m*T_0\).

Testing against \(P(T_m)=|T_m|^{p-2}T_m\):

* (T1) gives weighted dissipation;
* \(db*T_{m+1}\) is absorbed using \(|db|^2/b\le4|d\chi|^2\);
* the \(2\chi C_2*T_m\) part of \((\nabla^2b)*T_m\) is retained as
  \(\int\chi\nabla_i\nabla_j\chi\,B^{ij}(T_m)\) and integrated once;
* \(bT_0*T_m=U_0*T_m\) has bounded coefficient;
* \(U_m*T_0\) is controlled by finite-exponent Holder, since the current pair
  is completed before \(T_m\) and \(T_0\) is supplied by the zero-order seed;
* the top \(C_{m+2}\) term is integrated once, producing only
  \(C_{m+1}\), \(T_1\), and \(\nabla P(T_m)\);
* at \(m=1\), the resulting \(\chi C_2*T_1*P(T_1)\) is another signed
  Hessian contraction, not an \(L^\infty\)-Hessian coefficient.

All other factors in (2.1) lie at prior spatial levels.  Hence

\[
 \frac d{dt}\|T_m\|_p^p
 +c_{m,p}\int b|\nabla T_m|^2|T_m|^{p-2}
 \le C_{m,p}(1+\|T_m\|_p^p).                                   \tag{2.4}
\]

At each fixed \((m,p)\), constants depend on finitely larger exponents of
already completed levels only.

## 3. Complete differentiated \(U_m\) families

Apply \(\nabla^m\) to (1.4).  Use (1.7)--(1.8), and retain
\((db*db)*T\) without differentiating a quotient.  Every term belongs to:

\[
\begin{array}{lll}
\mathrm{(U1)}&b\Delta U_m,&\\
\mathrm{(U2)}&(\nabla^rb)*U_{m+2-r},&1\le r\le m+2,\\
\mathrm{(U3)}&C_{\alpha+1}*C_{\beta+1}*T_\gamma,
 &\alpha+\beta+\gamma=m,\\
\mathrm{(U4)}&U_i*U_j,&i+j=m,\\
\mathrm{(U5)}&b*T_r*U_s,&r+s=m\quad\text{(from (1.7))},\\
\mathrm{(U6)}&U_{r+1}*U_s,&r+s=m-1\quad\text{(from (1.8))},\\
\mathrm{(U7)}&(\nabla^rb)*U_{m-r}\ \text{or}\ \nabla^m(b^2),&0\le r\le m.
\end{array}                                                       \tag{3.1}
\]

Again, the list is exhaustive by the base monomials in (1.4) and the two
commutator identities.

### 3.1 Removing apparent current \(T_m\)

A \(T_m\) factor can occur only in:

1. (U3) with \(\alpha=\beta=0\), namely \(db*db*T_m\);
2. (U5) with \((r,s)=(m,0)\), namely \(bT_m*U_0\).

For the first, (1.5)--(1.6) give

\[
 db*db*T_m
 =4\frac{a}{b}(d\chi*d\chi)*
   \left[U_m-
      \sum_{r=1}^m{m\choose r}(\nabla^rb)*T_{m-r}\right],        \tag{3.2}
\]

and \(0\le a/b\le1\).  The second uses (1.6) directly.  Thus both become a
bounded coefficient times the current \(U_m\), plus prior \(T\)-levels.  No
unproved \(T_m\) norm enters the current-pair estimate.

### 3.2 Exhaustive current-jet table

After (3.2), the only terms containing a current/next variable are

\[
\begin{array}{c|l}
\text{object}&\text{all possible structures}\\ \hline
U_{m+1}&db*U_{m+1}=2\chi C_1*U_{m+1},\\
U_m&(\nabla^2b)*U_m,\ U_0*U_m,\ bT_0*U_m,\ (d\chi*d\chi)*U_m,\\
C_{m+2}&2\chi C_{m+2}*U_0,\\
C_{m+1}&C_1*C_{m+1}*U_0,\quad \chi C_{m+1}*U_1.
\end{array}                                                       \tag{3.3}
\]

There is no \(C_{m+1}*U_j\) with \(j\ge2\): such a term would have cutoff
order at least \(m+1\) and U order at least \(2\), exceeding the total
\(m+2\) derivatives in (U2); the other families have even smaller available
total order.

Let \(V=U_m\), \(Z=C_{m+1}\).  The first two rows of (3.3) are handled by
weighted dissipation, signed Hessian integration, and bounded \(U_0\).  The
top-cutoff term is integrated once:

\[
 \int\chi C_{m+2}*U_0*P(V)
 =-\int d\chi*C_{m+1}*U_0*P(V)
  -\int\chi C_{m+1}*U_1*P(V)
  -\int\chi C_{m+1}*U_0*\nabla P(V).                            \tag{3.4}
\]

Every occurrence of the middle type is integrated a second time for \(m\ge2\):

\[
\begin{split}
 \int\chi C_{m+1}*U_1*P(V)
 ={}&-\int d\chi*C_m*U_1*P(V)
     -\int\chi C_m*U_2*P(V)\\
    &-\int\chi C_m*U_1*\nabla P(V)+\mathcal R_{m}.          \tag{3.5}
\end{split}
\]

Here \(\mathcal R_m\) arises only if derivative slots are permuted.  The Ricci
commutation formula writes every such term as

\[
 \nabla^q\operatorname{Rm}*C_s*U_1*P(V),
 \qquad q+s\le m-1,                                               \tag{3.6}
\]

so it uses a prior \(T_q\) level.  For \(m=2\), the second term of (3.5) is a
signed \(\chi C_2*V*P(V)\) Hessian contraction; for \(m\ge3\), both
\(C_m\) and \(U_2\) are prior levels.  The derivative of \(P(V)\) is absorbed
by weighted dissipation.  At \(m=1\), the middle row is directly the signed
Hessian term.

It follows that

\[
 \frac d{dt}\|U_m\|_p^p+c_{m,p}
   \int b|\nabla U_m|^2|U_m|^{p-2}
 \le C_{m,p}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).          \tag{3.7}
\]

## 4. Cutoff-jet ledger

Since \(\chi\) is a fixed scalar, \(C_1=d\chi\) is time independent as a
covector, and for \(m\ge1\),

\[
 D_tC_{m+1}
 =\sum_{r+s=m-1}\nabla^r(\partial_t\Gamma)*C_{s+1}
 =\sum_{r+s=m-1}U_{r+1}*C_{s+1}.                                \tag{4.1}
\]

The unique current allocation is \(U_m*C_1\); neither \(U_{m+1}\) nor
\(C_{m+2}\) occurs.  Variation of inverse metrics in \(|C_{m+1}|^p\) and of
volume contributes only \(U_0*|C_{m+1}|^p\).  All other products contain
prior levels.  Hence

\[
 \frac d{dt}\|C_{m+1}\|_p^p
 \le C_{m,p}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).          \tag{4.2}
\]

Adding (3.7) and (4.2) closes the current pair before (2.4) is invoked.

## 5. Finite-exponent closure

Every remainder is a finite product of prior-level factors against either
\(|V|^{p-1}\) or \(|V|^{p-2}\).  If there are \(N\) prior factors, choose a
common finite exponent \(Np\) (or \(2Np\) after Young) for those factors.
Since the induction hypothesis at each completed spatial level provides every
finite \(L^q\) norm, no current quantity changes exponent.  The only current
pair products left after (3.4)--(3.5) are

\[
 |Z||V|^{p-1},
 \qquad |Z|^2|V|^{p-2},                                        \tag{5.1}
\]

which use exactly \(Z,V\in L^p\).

The zero-order estimate in `step44_zero_order_T_seed_repair.md` initializes
\(T_0\) for all finite exponents.  Equations (3.7), (4.2), and (2.4) therefore
prove the staggered finite-exponent propagation at every order, provided the
base curvature identity (1.2) is read with its exact universal contractions.

## 6. Regularization uniformity and endpoint

All constants above are uniform for \(b=\chi^2+\varepsilon^2\),
\(0<\varepsilon\le1\), on a common bootstrap interval:

\[
 \nabla^rb=\nabla^ra\ (r\ge1),
 \quad |db|^2/b\le4|d\chi|^2,
 \quad 0\le a/b\le1.                                           \tag{6.1}
\]

No inverse derivative of \(b\) occurs.  Choosing \(p>n\) and proceeding one
additional spatial level gives pointwise bounds for all derivatives of
\(U\).  Since

\[
 \partial_tg=-2\operatorname{Ric}(U),
 \qquad
 \partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U),           \tag{6.2}
\]

the metric, connection, and all fixed-coordinate spatial derivatives converge
at a finite endpoint.  This gives a positive-definite smooth endpoint under
metric equivalence.

The ledger proves the derivative-propagation portion of continuation and the
regularization-uniform derivative estimates needed by Yang's coefficient route.
It does not replace the initial fixed-\(\varepsilon\) strictly parabolic
existence theorem, nor the compactness/pasting argument, which are recorded in
`step44_coefficient_regularization_start.md`.
