# Weighted-variable Moser audit and corrected continuation induction

## 1. Scope and conclusions

Consider on a closed manifold

\[
 \partial_tg=-2aE,\qquad a=\chi^2,\qquad
 E=\operatorname{Ric}+g,
\]

and use

\[
 G=\frac{g\owedge g}{2(n-1)},\qquad
 T=\operatorname{Rm}+G,\qquad U=aT,\qquad V=aE.
\]

The conclusions are:

1. The equations for \(U\) and \(V\) are degenerate parabolic equations with
   principal operator \(a\Delta\). Treating \(U,V\) as unweighted tensors does
   not make that operator uniformly parabolic.
2. The unweighted power energies of \(U,V\) can be derived without dividing
   by \(a\), and all Hessian-cutoff terms can be integrated once using only
   \(d\chi\). Nevertheless ordinary unweighted Moser fails: the energy controls
   only \(\chi\nabla |U|^{p/2}\) or
   \(\chi\nabla |V|^{p/2}\), while unweighted Sobolev requires the full
   gradient. In addition, the shifted quadratic reaction is \(U*U\), not
   \(aU*U\).
3. The strongest currently valid replacement is the mixed
   Hölder--Sobolev recurrence for the weighted moments
   \(H_p(f)=\int\eta^2a^{p-2}f^p\), with \(f=F\) or \(f=|E|\). It repairs the
   half-power mismatch and, conditional on the already established
   positive-time \(H_3\) and propagated \(J_6\) bounds on the same support,
   yields the intended volume-independent endpoints.
4. The continuation induction does close under the terminal hypothesis
   \(\|U\|_\infty<\infty\), but the current weighted derivative
   \(\nabla^mU\) must be estimated together with
   \(\nabla^{m+1}\chi\). Wang's printed claim that cutoff derivatives only
   through order \(m\) suffice misses the term produced when
   \(\chi\nabla^{m+2}\chi*U\) is integrated by parts.

Statements concerning the endpoint Moser bounds below are conditional on the
session's \(H_3,J_6\), metric-comparison, and local Sobolev inputs. The
failure of ordinary \(U,V\) Moser and the corrected continuation dependency
are direct calculations.

## 2. Tensor equations for \(U\) and \(V\)

All stars denote universal metric contractions. The convention is chosen so
that

\[
 \operatorname{Ric}(G)=g,\qquad
 \operatorname{Ric}(T)=E,\qquad
 \operatorname{Ric}(U)=V,
\]

and hence the velocity is exactly

\[
 \partial_tg=-2V.                                             \tag{2.1}
\]

At a fixed time \(\nabla G=0\). The shifted curvature equation derived from
the full metric variation is

\[
 (\partial_t-a\Delta)T
 =da*\nabla T+\nabla^2a*T+a(T*T+G*T).                         \tag{2.2}
\]

There is no bare \(\nabla^2a*G\) source: every cutoff Hessian is contracted
with \(E=\operatorname{Ric}(T)\), and \(T=0\) is stationary.

### 2.1 Equation for \(U=aT\)

Because \(a\) is fixed in time,

\[
\begin{split}
 (\partial_t-a\Delta)(aT)
 ={}&a(\partial_t-a\Delta)T
     -2a\,da*\nabla T-a(\Delta a)T.                            \tag{2.3}
\end{split}
\]

Use

\[
 a\nabla T=\nabla U-da*T,
\qquad
 da*da*T=4\,d\chi*d\chi*U,                                    \tag{2.4}
\]

where the second identity is polynomial and valid on all of \(M\). Also

\[
 a^2T*T=U*U,\qquad a^2G*T=aG*U.                               \tag{2.5}
\]

Thus the reliable nonsingular equation is

\[
 \boxed{
 (\partial_t-a\Delta)U
 =da*\nabla U+\nabla^2a*U+d\chi*d\chi*U+U*U+aG*U.}             \tag{2.6}
\]

Numerical coefficients and contraction patterns depend on the curvature
convention, but every displayed weight and derivative order is fixed. In
particular, the quadratic reaction has no spare factor \(a\).

### 2.2 Equation for \(V=aE\)

The exact defect equation is

\[
 \partial_tE_{ij}=a(\Delta_LE_{ij}-2E_{ij})+\mathcal C_a(E)_{ij}, \tag{2.7}
\]

where, with \(\tau=\operatorname{tr}E\),

\[
\begin{split}
 \mathcal C_a(E)_{ij}={}&(\Delta a)E_{ij}
 +2a^k\nabla_kE_{ij}+\tau a_{ij}\\
 &+\frac12(a_i\tau_j+a_j\tau_i)
 -a_i{}^kE_{kj}-a_j{}^kE_{ki}\\
 &-a^k(\nabla_iE_{kj}+\nabla_jE_{ki}).                         \tag{2.8}
\end{split}
\]

In

\[
 (\partial_t-a\Delta)V
 =a(\partial_t-a\Delta)E-a(\Delta a)E-2a\,da*\nabla E,         \tag{2.9}
\]

the first two terms of (2.8) cancel exactly with the last two product-rule
terms in (2.9). The remaining expressions are rewritten without division:

\[
\begin{aligned}
 a\,da*\nabla E
   &=da*\nabla V-da*da*E
     =da*\nabla V-4d\chi*d\chi*V,\\
 a\,\tau\,\nabla^2a&=(\operatorname{tr}V)\nabla^2a,\\
 a\,(\nabla^2a)*E&=(\nabla^2a)*V.
\end{aligned}                                                   \tag{2.10}
\]

The Lichnerowicz algebraic terms can be expressed using
\(a\operatorname{Rm}=U-aG\) and
\(a\operatorname{Ric}=V-ag\). Consequently

\[
 \boxed{
 (\partial_t-a\Delta)V
 =da*\nabla V+\nabla^2a*V+d\chi*d\chi*V
   +U*V+V*V+aG*V.}                                            \tag{2.11}
\]

Since \(V=\operatorname{Ric}(U)\), pointwise
\(|V|\le C_n|U|\). Hence all algebraic terms in (2.11) obey

\[
 |\mathcal R_V|\le C_n(|U|+a)|V|.                             \tag{2.12}
\]

The \(V\)-equation is homogeneous in \(V\): there is no curvature-only
source.

## 3. Unweighted weak power energies

Let \(p\ge2\). Smooth regularization of the tensor norm is understood at its
zero set. For a covariant tensor \(Z\), (2.1) gives

\[
 \partial_t|Z|^2=2\langle\partial_tZ,Z\rangle+V*Z*Z,\qquad
 \partial_td\mu=-(\operatorname{tr}V)d\mu.                    \tag{3.1}
\]

Thus moving norms and moving measure contribute a potential bounded by
\(C|U||Z|^p\).

The principal term in either (2.6) or (2.11) satisfies

\[
\begin{split}
 p\int a|Z|^{p-2}\langle Z,\Delta Z\rangle
 \le{}&-c_pp\int a|Z|^{p-2}|\nabla Z|^2\\
 &+Cp^2\int |d\chi|^2|Z|^p.                                  \tag{3.2}
\end{split}
\]

The derivative of \(a\) created by integration by parts is estimated without
forming \(1/a\):

\[
 |da|\,|Z|^{p-1}|\nabla Z|
 =2|d\chi|\,|Z|^{p/2}
   \bigl(\chi|Z|^{(p-2)/2}|\nabla Z|\bigr).                   \tag{3.3}
\]

Young's inequality absorbs the parenthesized factor into the weighted
dissipation.

A representative Hessian term is likewise integrated once:

\[
 \int |Z|^{p-2}Z*(\nabla^2a)*Z
 =-\int da*\nabla(|Z|^{p-2}Z*Z),                              \tag{3.4}
\]

and (3.3) applies. Therefore, assuming
\(\|d\chi\|_\infty\le C/r\) and \(0\le a\le1\), the \(U\) equation gives

\[
\boxed{
\begin{split}
 \frac d{dt}X_p^U+c_ppD_p^U
 \le Cp^2(1+r^{-2})X_p^U
      +Cp\int |U|^{p+1},\\
 X_p^U=\int|U|^p,\qquad
 D_p^U=\int a|U|^{p-2}|\nabla U|^2.
\end{split}}                                                   \tag{3.5}
\]

Here the last integral includes both the \(U*U\) reaction and the
moving-norm/measure potential. Similarly, (2.11)--(2.12) give

\[
\boxed{
\begin{split}
 \frac d{dt}X_p^V+c_ppD_p^V
 \le Cp^2(1+r^{-2})X_p^V
      +Cp\int |U||V|^p,\\
 X_p^V=\int|V|^p,\qquad
 D_p^V=\int a|V|^{p-2}|\nabla V|^2.
\end{split}}                                                   \tag{3.6}
\]

No unweighted \(T\), no Hessian bound for \(\chi\), and no division by \(a\)
is needed for (3.5)--(3.6). The fatal issue comes at the Sobolev step, not
in deriving these weak energies.

## 4. Why ordinary unweighted Moser does not close

The proposed seeds do dominate the initial unweighted moments:

\[
 \int|U|^3\le C\int a^3F^3\le C\int aF^3=CH_3,                \tag{4.1}
\]

and

\[
 \int|V|^6=\int a^6|E|^6\le\int a^4|E|^6=J_6.                \tag{4.2}
\]

These inequalities do not repair the principal degeneracy. If
\(w=|U|^{p/2}\), (3.5) controls only

\[
 \int a|\nabla w|^2=\int|\chi\nabla w|^2.                    \tag{4.3}
\]

The available Sobolev inequality can be applied to \(\chi w\):

\[
 \|\chi w\|_4^2
 \le S\left(\int a|\nabla w|^2
             +C\int|d\chi|^2w^2+r^{-2}\int aw^2\right).       \tag{4.4}
\]

Its left side is

\[
 \|\chi w\|_4^2
 =\left(\int a^2|U|^{2p}\right)^{1/2},                        \tag{4.5}
\]

not \((\int|U|^{2p})^{1/2}\). The same mismatch holds for \(V\).
Therefore the usual unweighted parabolic recurrence cannot even be formed.

This is a genuine functional obstruction. Near a regular zero of \(\chi\),
use a normal coordinate with \(a=x^2+O(x^3)\), and place a triangular bump
\(w_\varepsilon\) in \(x\in[\varepsilon,2\varepsilon]\), constant in fixed
tangential directions. In the one-dimensional normal factor,

\[
 \int w_\varepsilon^2=\frac{\varepsilon}{3},\qquad
 \int w_\varepsilon^4=\frac{\varepsilon}{5},\qquad
 \int x^2|w_\varepsilon'|^2=\frac{28\varepsilon}{3}.           \tag{4.6}
\]

Consequently

\[
 \frac{\|w_\varepsilon\|_4^2}
 {\int a|\nabla w_\varepsilon|^2+\|w_\varepsilon\|_2^2}
 =\frac{3}{29\sqrt{5\varepsilon}}\longrightarrow\infty.       \tag{4.7}
\]

Smooth approximations have the same scaling. Since the bump is supported
where \(a>0\), it can be written as a smooth \(aT\) there; the factorization
\(U=aT\) imposes no uniform coercivity as the bump approaches \(\{a=0\}\).

There is a second, compatible failure. The last term of (3.5) is
\(\int|U|^{p+1}\), not \(\int a|U|^{p+1}\). Weighted diffusion and (4.4)
cannot absorb this unweighted reaction. For \(V\), the unmatched potential
is \(\int|U||V|^p\); bounding it requires the very \(L^\infty\) estimate for
\(U\) that the proposed iteration was meant to produce.

Thus standard unweighted Moser on \(U,V\) does not prove either proposed
endpoint from (4.1)--(4.2).

## 5. Strongest valid Moser replacement

Return to the smooth unweighted geometric scalars
\(f=F=(1+|\operatorname{Rm}|^2)^{1/2}\) and a regularization of
\(f=|E|\), but keep the cutoff weights in their moments:

\[
\begin{split}
 H_p(f)&=\int\eta^2a^{p-2}f^p,\\
 D_p(f)&=\int\eta^2a^{p-1}f^{p-2}|\nabla f|^2,\\
 z_p&=\eta a^{(p-1)/2}f^{p/2}.                                \tag{5.1}
\end{split}
\]

Here \(\eta=1\) on the active support and
\(\operatorname{supp}d\eta\) lies in the stationary collar \(a=da=0\).
The full tensor power calculation, including Hessian \(a\), moving norms,
moving measure, and the defect Kato regularization, gives

\[
 H_p'+c\|\nabla z_p\|_2^2
 \le Cp^N r^{-2}H_p+Cp\,R_p,\qquad
 R_p=\int\eta^2a^{p-1}Ff^p,                                  \tag{5.2}
\]

for a fixed polynomial power \(N\). The curvature equation uses \(f=F\);
the defect equation is homogeneous in \(E\), so it has no curvature-only
source.

Let

\[
 Y=\int_{\operatorname{supp}\chi}aF^3.
\]

The exact three-factor decomposition, including the auxiliary cutoff, is

\[
 \eta^2a^{p-1}Ff^p
 =(aF^3)^{1/3}(\eta^2a^{p-2}f^p)^{1/3}z_p^{4/3},             \tag{5.3}
\]

where \(\eta=1\) on the support of \(a\); nested collars give the same identity
when successive auxiliary cutoffs are distinguished. Hölder, Sobolev, and
Young imply

\[
 R_p\le\varepsilon(D_p+r^{-2}H_p)+C_\varepsilon p^N S^2YH_p, \tag{5.4}
\]

and hence

\[
 H_p'+cD_p\le Cp^N(r^{-2}+S^2Y)H_p.                           \tag{5.5}
\]

The old direct comparison of \(\|z_p\|_3^3\) with \(H_{3p/2}\) fails by one
half-power of \(a\). The corrected time-slice identity is instead

\[
 \boxed{
 H_{3p/2}
 =\int(a^{p-2}f^p)^{1/2}z_p^2
 \le H_p^{1/2}\|z_p\|_4^2.}                                  \tag{5.6}
\]

The weight equality is

\[
 \frac{p-2}{2}+(p-1)=\frac{3p}{2}-2.                          \tag{5.7}
\]

Combining (5.6) with time cutoffs and (5.5) yields, for
\(p_{k+1}=\frac32p_k\),

\[
 \int_{\tau_{k+1}}^tH_{p_{k+1}}
 \le Cp_k^NS
 \left(L_k\int_{\tau_k}^tH_{p_k}\right)^{3/2},\qquad
 L_k=Cp_k^N4^k(t^{-1}+r^{-2}).                                \tag{5.8}
\]

Since

\[
 \sum_{k\ge0}\frac1{p_k}=\frac3{p_0},\qquad
 \sum_{k\ge0}\frac1{(3/2)p_k}=\frac2{p_0},                    \tag{5.9}
\]

the dimension-four endpoint is

\[
 \boxed{
 \|af(t)\|_\infty
 \le CS^{2/p_0}t^{-3/p_0}
 \left(\int_{t/2}^tH_{p_0}(s)\,ds\right)^{1/p_0}.}             \tag{5.10}
\]

For curvature, \(p_0=3\) and the positive-time seed

\[
 S^2H_3(s)\le C\beta^3/s
\]

give

\[
 \|aF(t)\|_\infty\le C\beta/t.                                \tag{5.11}
\]

For defect, \(p_0=6\) and
\(J_6(s)\le C\delta^6\operatorname{Vol}\) give

\[
\begin{split}
 \|aE(t)\|_\infty
 &\le CS^{1/3}t^{-1/2}
       (\delta^6\operatorname{Vol}\,t)^{1/6}\\
 &\le C\delta(r^2/t)^{1/3},                                   \tag{5.12}
\end{split}
\]

because \(S\asymp r^2\operatorname{Vol}^{-1/2}\). Thus the intended
volume cancellation survives, but through the weighted mixed recurrence,
not ordinary Moser on \(U,V\).

Equations (5.11)--(5.12) remain conditional on the session's derivations of
the same-support \(H_3\) estimate, \(J_6\) persistence, Sobolev persistence,
and the metric first-exit bootstrap. The present calculation validates the
weight bridge and refutes the proposed shortcut.

## 6. Corrected current-order continuation pair

Now assume the terminal continuation hypothesis

\[
 \sup_{M\times[0,T)}|U|\le K.                                 \tag{6.1}
\]

It implies \(|V|\le C_nK\), uniform metric equivalence, uniform Sobolev
constants, and a bound for \(|d\chi|\). The unweighted base estimate obtained
by testing (2.2) gives

\[
 \sup_{t<T}\|T(t)\|_{L^q}<\infty
\quad\text{for every finite }q.                               \tag{6.2}
\]

No higher cutoff derivative is used in (6.2).

Let

\[
 W_m=\nabla^mU,\qquad C_{m+1}=\nabla^{m+1}\chi,\qquad
 P_p(W)=|W|^{p-2}W.                                           \tag{6.3}
\]

The differentiated \(U\)-equation contains

\[
\begin{array}{ll}
 \Gamma_1=\chi\nabla^{m+2}\chi*U,&
 \Gamma_2=\nabla\chi*\nabla^{m+1}\chi*U,\\
 \Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,&
 \Gamma_4=\chi\nabla\chi*\nabla W_m.                          \tag{6.4}
\end{array}
\]

All other terms contain only \(\nabla^{m-1}T\), derivatives of \(U\) below
\(m\), cutoff derivatives through \(m\), or a bounded \(G\)-coefficient.

### 6.1 Expanded high-term estimates

The fourth term is immediate:

\[
 \left|\int P_p(W_m)*\Gamma_4\right|
 \le\varepsilon\mathcal D_{m,p}+Cp^2\|W_m\|_p^p,              \tag{6.5}
\]

where

\[
 \mathcal D_{m,p}
 =\int\chi^2|\nabla W_m|^2|W_m|^{p-2}.                        \tag{6.6}
\]

Integrating \(\Gamma_1\) once gives, up to lower curvature commutators,

\[
\begin{split}
 \int P_p(W_m)*\Gamma_1
 ={}&-\int\nabla P_p(W_m)*\chi C_{m+1}*U\\
 &-\int P_p(W_m)*\nabla\chi*C_{m+1}*U\\
 &-\int P_p(W_m)*\chi C_{m+1}*\nabla U.                       \tag{6.7}
\end{split}
\]

The first descendant is the term omitted if cutoff order \(m\) alone is
claimed:

\[
\begin{split}
 \left|\int\nabla P_p(W_m)*\chi C_{m+1}*U\right|
 \le{}&\varepsilon\mathcal D_{m,p}\\
 &+C_{p,\varepsilon}K^2
   \int|C_{m+1}|^2|W_m|^{p-2}.                                \tag{6.8}
\end{split}
\]

Hölder gives exactly

\[
 \int|C_{m+1}|^2|W_m|^{p-2}
 \le\|C_{m+1}\|_p^2\|W_m\|_p^{p-2}.                           \tag{6.9}
\]

The second descendant in (6.7), together with \(\Gamma_2\), satisfies

\[
 \left|\int P_p(W_m)*\nabla\chi*C_{m+1}*U\right|
 \le CK\|\nabla\chi\|_\infty
       \|C_{m+1}\|_p\|W_m\|_p^{p-1}.                          \tag{6.10}
\]

For the third descendant and \(\Gamma_3\), integrate one derivative from
\(C_{m+1}=\nabla(\nabla^m\chi)\):

\[
\begin{split}
 \int P_p(W_m)*\chi C_{m+1}*\nabla U
 ={}&-\int\nabla P_p(W_m)*\chi\nabla^m\chi*\nabla U\\
 &-\int P_p(W_m)*\nabla\chi*\nabla^m\chi*\nabla U\\
 &-\int P_p(W_m)*\chi\nabla^m\chi*\nabla^2U
   +\mathcal L_m.                                             \tag{6.11}
\end{split}
\]

Here \(\mathcal L_m\) contains only curvature commutators with cutoff order at
most \(m\) and unweighted \(T\)-order at most \(m-1\). The first line of
(6.11) is bounded by

\[
 \varepsilon\mathcal D_{m,p}
 +C\int|\nabla^m\chi|^2|\nabla U|^2|W_m|^{p-2}.               \tag{6.12}
\]

The second line has no current cutoff derivative and is handled by ordinary
Hölder. The last line has a factor \(\chi\). For \(m=1\),
\(\nabla^2U=\nabla W_1\) and it is absorbed into (6.6). For \(m=2\), it is a
coefficient times \(\chi|W_2|^p\); for \(m\ge3\), \(\nabla^2U\) is a
previous-level derivative. In the latter cases use

\[
 \|\chi|W_m|^{p/2}\|_4^2
 \le C_pS\bigl(\mathcal D_{m,p}
 +(1+r^{-2})\|W_m\|_p^p\bigr)                                \tag{6.13}
\]

and Hölder--Young. Thus (6.11) costs only a small multiple of
\(\mathcal D_{m,p}\) plus \(C(1+\|W_m\|_p^p)\), using previous-level finite
norms.

Equations (6.8)--(6.10) show why \(\nabla^{m+1}\chi\) cannot be erased. They
also show that it enters in exactly the form needed for a same-exponent
coupling.

### 6.2 Finite exponent schedule

Fix a desired \(p\ge\max\{4,n+2\}\). The schedule is:

1. Current factors \(W_m,C_{m+1}\) occur only in (6.9)--(6.10), at the same
   exponent \(p\).
2. A product of two squared previous-level factors, such as (6.12), uses
   each factor in \(L^{4p}\); together with
   \(|W_m|^{p-2}\) this consumes at most \((p-1)/p\) of the Hölder exponent.
3. All remaining differentiated monomials have at most four
   previous-level factors. Assign each \(L^{8p}\); finite-volume embedding
   covers unused exponent.
4. Terms with a factor \(\chi\) and one current power use (6.13), with their
   previous-level coefficients in \(L^{8p}\).

This is finite at every \(m,p\). There is no upward current-order chain:
the induction hypothesis supplies every previous level in every finite
exponent, so \(4p\) and \(8p\) are already available.

### 6.3 Coupling to the cutoff equation

Since
\(\partial_t\Gamma=g^{-1}*\nabla V
=g^{-1}*\operatorname{Ric}(\nabla U)\), the exact
derivative count for the fixed scalar is

\[
 \partial_t\nabla^{m+1}\chi
 =\sum_{q=0}^{m-1}\nabla^q(\partial_t\Gamma)*
                         \nabla^{m-q}\chi.                    \tag{6.14}
\]

The unique current-order product is

\[
 \nabla^mU*\nabla\chi=W_m*\nabla\chi.                         \tag{6.15}
\]

Include the evolving norm and measure and regularize the \(L^p\) norms by

\[
\begin{split}
 \mathcal X_{m,p}
   &=(\varepsilon+\|W_m\|_p^p)^{2/p},\\
 \mathcal Z_{m+1,p}
   &=(\varepsilon+\|C_{m+1}\|_p^p)^{2/p}.                     \tag{6.16}
\end{split}
\]

After (6.5)--(6.13), division by the standard norm factor converts
(6.9) and (6.10) into quadratic and bilinear terms in
\(\mathcal X^{1/2},\mathcal Z^{1/2}\). The result is

\[
 \mathcal X_{m,p}'
 +c\,(\varepsilon+\|W_m\|_p^p)^{2/p-1}\mathcal D_{m,p}
 \le C_{m,p}(1+\mathcal X_{m,p}+\mathcal Z_{m+1,p}).           \tag{6.17}
\]

Testing (6.14) in \(L^p\) with the same finite schedule gives

\[
 \mathcal Z_{m+1,p}'
 \le C_{m,p}(1+\mathcal X_{m,p}+\mathcal Z_{m+1,p}).           \tag{6.18}
\]

Therefore

\[
 \frac d{dt}(\mathcal X_{m,p}+\mathcal Z_{m+1,p})
 \le C_{m,p}(1+\mathcal X_{m,p}+\mathcal Z_{m+1,p}),           \tag{6.19}
\]

and Gronwall closes the current pair. This replaces the incorrect arrow
\(A_{m-1}\to C_m\to T_{m-1}\to A_m\) by

\[
 \boxed{
 (\nabla^mU,\nabla^{m+1}\chi)\ \text{coupled first},
 \qquad \nabla^mT\ \text{second}.}                            \tag{6.20}
\]

## 7. Estimate for \(\nabla^mT\) and completion

Assume \(T_j\), \(j<m\), and the previous \(U,\chi\) levels have been
controlled in every finite exponent. After (6.19), \(U_m\) and
\(\chi_{m+1}\) are also controlled in every finite exponent.

The raw \(T_m=\nabla^mT\) equation contains

\[
 \chi\nabla^{m+2}\chi*T.                                     \tag{7.1}
\]

One integration by parts lowers it to \(\nabla^{m+1}\chi\). A derivative on
\(T_m\) carries the factor \(\chi\) and is absorbed by

\[
 \int\chi^2|\nabla T_m|^2|T_m|^{p-2}.                         \tag{7.2}
\]

The resulting worst coefficient term has the form

\[
 \int|\nabla^{m+1}\chi|^2|T|^2|T_m|^{p-2},                   \tag{7.3}
\]

which is finite using \(\nabla^{m+1}\chi,T\in L^{4p}\). The connection
commutator contains

\[
 \int|\nabla^mU|\,|T|\,|T_m|^{p-1};                           \tag{7.4}
\]

it closes with \(\nabla^mU,T\in L^{2p}\), since

\[
 \frac1{2p}+\frac1{2p}+\frac{p-1}{p}=1.                       \tag{7.5}
\]

All other terms use the finite \(8p\) schedule. Hence

\[
 \sup_{t<T}\|\nabla^mT(t)\|_{L^p}<\infty.                     \tag{7.6}
\]

The induction starts with \(U\in L^\infty\), \(T\in L^q\) for all finite
\(q\), and \(\nabla\chi\in L^\infty\). At \(m=1\), (6.19) couples
\((\nabla U,\nabla^2\chi)\), then (7.6) gives \(\nabla T\). Repeating first
(6.19), then (7.6), controls all orders. Applying Sobolev after the next
derivative level gives

\[
 \sup_{M\times[0,T)}|\nabla^mU|<\infty
\quad\text{for every }m.                                     \tag{7.7}
\]

Since

\[
 \nabla^m(a\operatorname{Rm})
 =\nabla^mU-(\nabla^ma)*G,                                   \tag{7.8}
\]

all weighted curvature derivatives are bounded. The standard
connection-difference argument then produces a smooth terminal metric and
the normalized transported-coefficient DeTurck system restarts the flow.

The corrected proof therefore preserves the extension theorem, but not the
earlier claim that the \(U_m\) estimate needs cutoff derivatives only through
order \(m\).

## 8. Common flow on disjoint macro-supports

Let

\[
 a=\sum_{j=1}^N\chi_j^2
\]

with pairwise disjoint active supports and pairwise disjoint buffered
macro-supports. Then at every point at most one summand is active. The
consequences are:

1. Equations (2.2), (2.6), and (2.11) hold componentwise with
   \(a=\chi_j^2\); no mixed \(d\chi_i*d\chi_j\) terms occur.
2. Weighted \(H_p,D_p,J_6\) energies sum exactly over components. Global
   pointwise endpoints are maxima of the component endpoints, so they are
   independent of the number of components if the support geometry, seed
   bounds, and Sobolev constants are uniform.
3. The failure of ordinary \(U,V\) Moser persists separately in every
   transition collar. Taking a union does not restore coercivity.
4. The continuation theorem applies to the single global smooth coefficient
   \(a\). For a fixed flow, its constants may depend on that coefficient.
   If all component cutoffs have uniform jets and their supports are
   disjoint, the pointwise cutoff constants do not grow with \(N\).
5. A stationary collar between macro-supports is essential. Disjoint active
   sets with overlapping auxiliary buffers do not make localized integration
   by parts additive.
6. In DeTurck gauge the global coefficient is transported as
   \(\widehat a=a\circ\phi^{-1}\), multiplying both
   \(\operatorname{Ric}(\widehat g)\) and \(\widehat g\). Pullback restores
   the original disjoint fixed supports.

Thus a common flow is analytically compatible with a macro-disjoint family,
but it must use the weighted mixed Moser bridge before invoking the corrected
shifted-curvature continuation theorem.

## 9. Verification and source dependence

The script
Sessions/S0910A03/workspace/codex_loop/work/verify_weighted_moser_coupling.py
checks:

- \(a^2T*T=U*U\), not \(aU*U\);
- cancellation of product-rule Laplacian terms in the \(V=aE\) equation;
- domination of the unweighted \(U,V\) seeds by \(H_3,J_6\);
- the mixed weight identity (5.7) and three-factor absorption weights;
- the curvature/defect endpoint exponents and defect volume cancellation;
- the divergent scaling ratio (4.7);
- the same-exponent coupled terms and the finite \(4p,8p\) Hölder schedule.

The exact full-velocity and defect equations are taken from
Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md.
The weighted general-\(p\) calculation is aligned with
Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md.
The mixed recurrence was independently checked against
Sessions/S0910A01/workspace/notes/step30_weighted_moser_and_family_repair.md.
Wang's Section 4 remains the source for the original derivative templates,
but its Proposition 4.14 cutoff-order conclusion is corrected by
(6.7)--(6.20).
