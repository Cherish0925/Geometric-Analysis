# Shifted-curvature continuation for the normalized fixed-cutoff flow

> **Supersession notice (current proposal audit).** The shifted-curvature
> identities and base unweighted \(T\) estimate below remain valid, but the
> old dependency claim in Section 7 is too optimistic. Integrating
> \(\chi\nabla^{m+2}\chi*U\) leaves a term involving
> \(\nabla^{m+1}\chi\); \(\nabla^mU\) and
> \(\nabla^{m+1}\chi\) must be closed as a current-order pair. Use
> Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md
> for the corrected induction. That memo also refutes ordinary unweighted
> Moser on \(U,V\).

## 1. Result and setup

Let \(M^n\) be closed, let \(\chi\in C^\infty(M)\) be fixed in time, put
\(a=\chi^2\), and consider, on a finite interval \([0,T)\),

\[
  \partial_t g=-2a(\operatorname{Ric}(g)+g).                    \tag{1.1}
\]

The conclusion is that Wang's smooth-extension induction does transfer to
(1.1). More precisely, if

\[
  \sup_{M\times[0,T)} |a\operatorname{Rm}|_g<\infty,           \tag{1.2}
\]

then every spatial covariant derivative of \(a\operatorname{Rm}\) is uniformly
bounded on \(M\times[0,T)\), \(g(t)\) has a smooth limit at \(T\), and the
solution restarts past \(T\). Constants may depend on the particular
\((g_0,\chi,T)\). No a priori bound on \(\nabla^r\chi\), \(r\ge2\), is inserted.

The essential device is not merely to call the extra term in (1.1) “lower
order.” One must shift curvature so that the complete velocity, including
normalization, is the Ricci contraction of the weighted shifted curvature.
That fact preserves Wang's triangular derivative dependence.

Throughout, \(S*T\) denotes a finite universal linear combination of metric
contractions of \(S\otimes T\). It records derivative order, cutoff weight,
and vanishing, but not inessential numerical coefficients. Equations called
“exact” below are independent of this notation.

## 2. Convention-sensitive algebra

Use the Kulkarni--Nomizu convention

\[
 (h\owedge k)_{ijkl}
 =h_{ik}k_{jl}+h_{jl}k_{ik}-h_{il}k_{jk}-h_{jk}k_{il},         \tag{2.1}
\]

and the curvature convention for which a metric of sectional curvature
\(-1\) has

\[
 \operatorname{Rm}_{ijkl}=-\frac1{n-1}
 (g_{ik}g_{jl}-g_{il}g_{jk}).                                  \tag{2.2}
\]

Define

\[
 G:=\frac1{2(n-1)}g\owedge g,
 \qquad
 G_{ijkl}=\frac1{n-1}(g_{ik}g_{jl}-g_{il}g_{jk}),              \tag{2.3}
\]

and contract by

\[
 \operatorname{Ric}(S)_{jl}=g^{ik}S_{ijkl}.                   \tag{2.4}
\]

Then, exactly,

\[
 \nabla G=0,
 \qquad \operatorname{Ric}(G)=g.                              \tag{2.5}
\]

For an arbitrary metric velocity \(h=\partial_tg\), symmetry of (2.1) gives

\[
 \partial_tG=\frac1{n-1}h\owedge g.                           \tag{2.6}
\]

In particular, with

\[
 E:=\operatorname{Ric}+g,
 \qquad h=-2aE,
\]

one has the exact identity

\[
 \boxed{\ \partial_tG=-\frac{2a}{n-1}E\owedge g\ }.           \tag{2.7}
\]

It is important that contraction itself varies. Differentiating (2.5) yields

\[
 (\partial_tg^{ik})G_{ijkl}+g^{ik}(\partial_tG)_{ijkl}=h_{jl}, \tag{2.8}
\]

which checks both the factor in (2.7) and all-covariant versus mixed-index
calculations.

Set

\[
 \widetilde R:=\operatorname{Rm}+G,
 \qquad U:=a\widetilde R.                                     \tag{2.9}
\]

Equations (2.4)--(2.5) imply the decisive exact identities

\[
 E=\operatorname{Ric}(\widetilde R),
 \qquad
 aE=\operatorname{Ric}(U),                                    \tag{2.10}
\]

and hence

\[
 \boxed{\ \partial_tg=-2\operatorname{Ric}(U)\ }.             \tag{2.11}
\]

Thus no separate term \(ag\) occurs in the connection evolution.

## 3. Exact variation starting point and shifted-curvature evolution

For reference, under an arbitrary velocity \(h\),

\[
 \partial_t\Gamma^\ell{}_{ik}=C^\ell{}_{ik}
 =\frac12g^{\ell p}
 (\nabla_i h_{kp}+\nabla_kh_{ip}-\nabla_ph_{ik}),               \tag{3.1}
\]

and

\[
 \partial_tR^\ell{}_{kij}=\nabla_iC^\ell{}_{jk}
                          -\nabla_jC^\ell{}_{ik}.              \tag{3.2}
\]

For \(h=-2aE\), (3.1) is the exact formula

\[
 C^\ell{}_{ik}=-g^{\ell p}\big[
 (\nabla_i a)E_{kp}+(\nabla_k a)E_{ip}-(\nabla_pa)E_{ik}
 +a(\nabla_iE_{kp}+\nabla_kE_{ip}-\nabla_pE_{ik})\big].        \tag{3.3}
\]

Consequently (3.2) contains, with no possible omission, the terms

\[
 (\nabla^2a)*E+(\nabla a)*(\nabla E)+a\nabla^2E.               \tag{3.4}
\]

In particular, if \(a_i=\nabla_i a\), \(a_{ij}=\nabla_i\nabla_j a\), and
\(A_{jkp}=\nabla_jE_{kp}+\nabla_kE_{jp}-\nabla_pE_{jk}\), the Hessian and
first-cutoff-derivative pieces of the mixed curvature variation are exactly

\[
\begin{split}
 \mathcal H^\ell{}_{kij}
 ={}&-g^{\ell p}
 (a_{ik}E_{jp}-a_{ip}E_{jk}-a_{jk}E_{ip}+a_{jp}E_{ik}),\\
 \mathcal D^\ell{}_{kij}
 ={}&-g^{\ell p}\big[
 a_j\nabla_iE_{kp}+a_k\nabla_iE_{jp}-a_p\nabla_iE_{jk}
 +a_iA_{jkp}\\
 &\hspace{37mm}
 -a_i\nabla_jE_{kp}-a_k\nabla_jE_{ip}+a_p\nabla_jE_{ik}
 -a_jA_{ikp}\big].
                                                                    \tag{3.5}
\end{split}
\]

The remaining second-\(E\)-derivative piece is exactly
\(-ag^{\ell p}(\nabla_iA_{jkp}-\nabla_jA_{ikp})\). Thus the answer to the
proposal's component-level question is yes: the Hessian term is a contraction
of \(\nabla^2a\) with
\(E=\operatorname{Ric}(\widetilde R)\), and the first-derivative term is a
contraction of \(da\) with
\(\nabla E=\nabla\operatorname{Ric}(\widetilde R)\).

After the Bianchi commutations convert \(a\nabla^2E\) to
\(a\Delta\operatorname{Rm}+a\operatorname{Rm}*\operatorname{Rm}\), lowering
the first index contributes \(h*\operatorname{Rm}\), and (2.7) contributes
the variation of \(G\). Substituting
\(\operatorname{Rm}=\widetilde R-G\) and \(E=\operatorname{Ric}(\widetilde R)\)
gives the reliable all-covariant schematic equation

\[
 \boxed{
 (\partial_t-a\Delta)\widetilde R
 =a(\widetilde R*\widetilde R+G*\widetilde R)
  +(\nabla a)*(\nabla\widetilde R)
  +(\nabla^2a)*\widetilde R .}                                 \tag{3.6}
\]

Every contraction in (3.6) is universal. Most importantly, every summand on
the right contains \(\widetilde R\) or a derivative of it. There is no
\((\nabla^2a)*G\) source. This is also forced by a stringent consistency
check: when \(\widetilde R=0\), the metric is hyperbolic, \(E=0\), and (1.1)
is stationary for an arbitrary fixed cutoff.

Taking covariant derivatives requires commuting both \(\partial_t\) and
\(\Delta\) through \(\nabla^m\). Equation (2.11) gives

\[
 \partial_t\Gamma=\nabla\operatorname{Ric}(U)=\nabla U         \tag{3.7}
\]

schematically. Combining (3.6), (3.7), and curvature commutators gives

\[
\begin{split}
 \partial_t\nabla^m\widetilde R
={}&a\Delta\nabla^m\widetilde R\\
 &+\sum_{\substack{r+k=m+2\\1\le r\le m+2,\ 0\le k\le m+1}}
       \nabla^r a*\nabla^k\widetilde R\\
 &+\sum_{i+j+k=m}\nabla^ia*\nabla^j\widetilde R*
                         \nabla^k\widetilde R
  +\sum_{i+k=m}\nabla^ia*G*\nabla^k\widetilde R .              \tag{3.8}
\end{split}
\]

Repeated terms in (3.8) are harmless; the displayed ranges are safe rather
than irredundant. The first sum explicitly includes
\(\nabla^{m+2}a*\widetilde R\). Since

\[
 \nabla^ra=\nabla^r(\chi^2)
 =\sum_{s=0}^r {r\choose s}\nabla^s\chi*\nabla^{r-s}\chi,      \tag{3.9}
\]

there is no legitimate way to omit the apparent
\(\chi\nabla^{m+2}\chi*\widetilde R\) term.

## 4. Evolution of the weighted shifted curvature

Multiplying (3.6) by \(a\), rewriting the principal part as \(a\Delta U\),
and applying the same commutators gives the normalized analogue of Wang's
Lemmas 4.4--4.5:

\[
\begin{split}
 \partial_t\nabla^mU
={}&a\Delta\nabla^mU\\
 &+\sum_{\substack{\alpha+\beta+\gamma=m+2\\
                    0\le\gamma\le m+1\\
                    \alpha+\beta\ge1}}
   \nabla^\alpha\chi*\nabla^\beta\chi*\nabla^\gamma U\\
 &+\sum_{\substack{i+j+k=m\\0\le k\le m-1}}
   \nabla^ia*\nabla^jU*\nabla^k\widetilde R
   +U*\nabla^mU\\
 &+\underbrace{\sum_{i+j=m}\nabla^ia*G*\nabla^jU}_{\mathcal N_m}.
                                                                    \tag{4.1}
\end{split}
\]

An empty sum is absent (notably when \(m=0\)). The first three lines have
exactly Wang's derivative structure after replacing
\(\operatorname{Rm}\) by \(\widetilde R\). The final line is the entire new
normalization contribution relevant to the induction.

The four apparently dangerous allocations in the first sum are

\[
\begin{array}{ll}
 \Gamma_1=\chi\nabla^{m+2}\chi*U,&
 \Gamma_2=\nabla\chi*\nabla^{m+1}\chi*U,\\
 \Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,&
 \Gamma_4=\chi\nabla\chi*\nabla^{m+1}U.                         \tag{4.2}
\end{array}
\]

Thus \(\nabla^{m+2}\chi\) and \(\nabla^{m+1}U\) really occur in the raw
equation. They are removed or absorbed by the energy argument, not assumed
bounded.

The cutoff equation also remains exactly triangular. A fixed scalar has

\[
 \partial_t\nabla^m\chi
 =\sum_{r=0}^{m-1}\nabla^r(\partial_t\Gamma)*
                         \nabla^{m-r}\chi,
\]

so (3.7) implies

\[
 \boxed{
 \partial_t|\nabla^m\chi|
 \le C_m\sum_{r=0}^{m-1}|\nabla^rU|\,|\nabla^{m-r}\chi| .}     \tag{4.3}
\]

This is Wang's Lemma 4.6 with \(\chi^2\operatorname{Rm}\) replaced by \(U\).
Writing the velocity as \(-2a\operatorname{Ric}-2ag\) and estimating the two
pieces separately would obscure this fact and falsely suggest an additional
cutoff derivative branch.

## 5. Consequences of the sole curvature hypothesis

Let \(K\) denote the bound in (1.2). Since \(M\) is closed and \(\chi\) is a
fixed smooth function,

\[
 |U|\le |a\operatorname{Rm}|+a|G|\le K+C(n)\|a\|_\infty.       \tag{5.1}
\]

Moreover

\[
 |aE|\le C(n)(|a\operatorname{Rm}|+a),                         \tag{5.2}
\]

and hence \(|\partial_tg|_g\le C\). Integrating the scalar inequality for
\(g(t)(v,v)\) gives

\[
 e^{-Ct}g_0\le g(t)\le e^{Ct}g_0.                              \tag{5.3}
\]

Thus volume, the \(L^p\) norms defined by \(g(t)\), and Sobolev constants are
uniformly equivalent to those of \(g_0\). In particular,
\(|\nabla\chi|_{g(t)}\) is bounded. This argument supplies no higher cutoff
derivatives and does not need to.

## 6. Base unweighted \(L^p\) estimate without a Hessian-cutoff assumption

Fix \(p>\max\{n,2\}\); in a Wang-style all-orders argument it is convenient to
run the estimates for every sufficiently large \(p\). Test (3.6) against
\(|\widetilde R|^{p-2}\widetilde R\), using
\((|\widetilde R|^2+\varepsilon^2)^{1/2}\) and then
\(\varepsilon\downarrow0\) if desired. The time variation of the norm and
measure is controlled by (5.2). The diffusion term supplies

\[
 -c_p\int_M a|\nabla\widetilde R|^2
                     |\widetilde R|^{p-2}\,d\mu.               \tag{6.1}
\]

The only term which seems to require \(\nabla^2\chi\) is

\[
 I=\int_M (\nabla^2a)*\widetilde R*
                   \widetilde R|\widetilde R|^{p-2}\,d\mu.     \tag{6.2}
\]

Integrating one derivative from \(a\) gives terms bounded by

\[
 C_p\int_M |\nabla a|\,|\nabla\widetilde R|
                         |\widetilde R|^{p-1}\,d\mu.
\]

Young's inequality and \(a=\chi^2\) give, pointwise across the zero set by
continuous extension,

\[
 \frac{|\nabla a|^2}{a}=4|\nabla\chi|^2,                       \tag{6.3}
\]

and therefore

\[
 |I|\le \varepsilon\int_Ma|\nabla\widetilde R|^2
                              |\widetilde R|^{p-2}
       +C_{p,\varepsilon}\|\nabla\chi\|_\infty^2
                              \int_M|\widetilde R|^p.           \tag{6.4}
\]

The quadratic reaction is bounded using \(a|\widetilde R|=|U|\), and the
\(aG*\widetilde R\) term is linear with bounded coefficient. Combining all
terms gives

\[
 \frac d{dt}\int_M|\widetilde R|^p\,d\mu
 +c_p\int_Ma|\nabla\widetilde R|^2
                    |\widetilde R|^{p-2}\,d\mu
 \le C_p\int_M|\widetilde R|^p\,d\mu.                          \tag{6.5}
\]

The initial integral is finite, so Gronwall proves

\[
 \sup_{t<T}\|\widetilde R(t)\|_{L^p}<\infty.                   \tag{6.6}
\]

This is the required analogue of Wang's Lemma 4.10. It uses (1.2), metric
equivalence, and the first derivative of the fixed cutoff only.

## 7. Closing the derivative triangle

For bookkeeping define, for large \(q\),

\[
 A_m(q)=\sup_{t<T}\|\nabla^mU\|_{L^q},\qquad
 B_m(q)=\sup_{t<T}\|\nabla^m\widetilde R\|_{L^q},\qquad
 C_m(q)=\sup_{t<T}\|\nabla^m\chi\|_{L^q}.                     \tag{7.1}
\]

The actual dependency graph is

\[
 A_{\le m-1}\Longrightarrow C_m,
 \qquad
 (C_{\le m+1},B_{<m})\Longrightarrow B_m,
 \qquad
 (C_{\le m},B_{\le m-1},A_{<m})\Longrightarrow A_m.           \tag{7.2}
\]

The third arrow is an energy arrow: the raw equation contains \(C_{m+2}\),
\(C_{m+1}\), and a weighted \(A_{m+1}\) term as in (4.2), but integration by
parts lowers the cutoff order and diffusion absorbs the weighted derivative.
Therefore the ordering at level \(m\) is

\[
 A_{m-1}\ \longrightarrow\ C_m\ \longrightarrow\ B_{m-1}
 \ \longrightarrow\ A_m.                                     \tag{7.3}
\]

Here are the estimates that justify the nonformal arrows.

### 7.1 The first coupled step

For \(m=2\), (4.3) gives, after Hölder,

\[
 \frac d{dt}\|\nabla^2\chi\|_{L^p}^p
 \le C(1+\|\nabla^2\chi\|_{L^p}^p+\|\nabla U\|_{L^p}^p).       \tag{7.4}
\]

The \(m=1\) instance of (4.1), tested against
\(|\nabla U|^{p-2}\nabla U\), and the integrations used below give

\[
 \frac d{dt}\|\nabla U\|_{L^p}^p+cD_1
 \le C(1+\|\nabla U\|_{L^p}^p+\|\nabla^2\chi\|_{L^p}^p),       \tag{7.5}
\]

where

\[
 D_m=\int_M\chi^2|\nabla^{m+1}U|^2|\nabla^mU|^{p-2}\,d\mu.    \tag{7.6}
\]

Equations (7.4)--(7.5) close by Gronwall. This is Wang's
\((\nabla U,\nabla^2\chi)\) base pair. The normalization contribution in
(4.1) obeys the estimate in Section 7.3 below and adds only
\(C(1+\|\nabla U\|_p^p)\).

### 7.2 Unweighted derivatives

Testing (3.8) at order \(m\), the top cutoff term is

\[
 \chi\nabla^{m+2}\chi*\widetilde R*\nabla^m\widetilde R
 |\nabla^m\widetilde R|^{p-2}.                                \tag{7.7}
\]

One integration by parts moves one derivative off
\(\nabla^{m+2}\chi\). If it lands on the top curvature factor, its term has
a factor \(\chi\) and is absorbed by diffusion; if it lands elsewhere, only
\(\nabla^{m+1}\chi\), lower curvature derivatives, and controlled products
occur. Hölder and Young then give

\[
 \frac d{dt}B_m(p)^p+c\int_Ma|\nabla^{m+1}\widetilde R|^2
                              |\nabla^m\widetilde R|^{p-2}
 \le C(1+B_m(p)^p),                                           \tag{7.8}
\]

provided \(C_r(q)\) is known through \(r=m+1\) and \(B_r(q)\) is known for
\(r<m\), with sufficiently large Hölder exponents \(q\). The added normalized
terms are

\[
 \sum_{i+k=m}\nabla^ia*G*\nabla^k\widetilde R.                 \tag{7.9}
\]

For \(k=m,i=0\), their tested integral is at most \(CB_m(p)^p\). For \(k<m\),
Hölder followed by Young bounds it by \(C(1+B_m(p)^p)\). Thus (7.9) asks for
no \(C_{m+2}\) and does not alter the second arrow of (7.2).

### 7.3 Weighted derivatives and removal of apparent top cutoff orders

Let \(V=\nabla^mU\). The \(\Gamma_4\) integral satisfies directly

\[
 \left|\int |V|^{p-2}V*(\chi\nabla\chi*\nabla V)\right|
 \le\varepsilon D_m+C_{\varepsilon,p}
                         \|\nabla\chi\|_\infty^2\|V\|_p^p.    \tag{7.10}
\]

The remaining three terms must be integrated as a group; estimating
\(\Gamma_1\) alone after only one integration would incorrectly demand
\(\nabla^{m+1}\chi\). Apply the contraction-preserving integrations by parts
in Wang's Proposition 4.14 to \(\Gamma_1,\Gamma_2,\Gamma_3\), with his
\(\chi^2\operatorname{Rm}\) replaced everywhere by \(U\). This substitution
is valid because the high-cutoff line of (4.1) has the identical contraction
and derivative structure. Terms with \(\nabla^{m+1}U\) retain a factor
\(\chi\) and are absorbed exactly as in (7.10); derivatives placed on a
lower \(U\)-factor or on \(V\) produce the induction terms in (4.1). The one
distribution that is not of those types is, explicitly,

\[
 \nabla^2\chi*\nabla^m\chi*U*V|V|^{p-2}.                       \tag{7.11}
\]

All other distributions have cutoff order at most \(m\) and weighted-curvature
order at most \(m\). Thus this is not an appeal to an unspecified
“lower-order term”: the only residual top-cutoff product is (7.11), while
the derivative-of-\(V\) terms are paid for by \(D_m\). Running the induction
simultaneously for all sufficiently large Hölder exponents, Hölder and Young
bound (7.11) and the induction terms by \(C(1+\|V\|_p^p)\). Consequently the
verbatim Wang energy identity gives

\[
 \left|\int |V|^{p-2}V*(\Gamma_1+\Gamma_2+\Gamma_3+\Gamma_4)\right|
 \le\varepsilon D_m+C(1+\|V\|_p^p).                            \tag{7.12}
\]

This is the precise mechanism behind Wang's Proposition 4.14: neither
\(\nabla^{m+2}\chi\) nor \(\nabla^{m+1}\chi\) is an input to the \(A_m\)
estimate, and the occurrence of \(\nabla^{m+1}U\) is paid for by \(D_m\).

It remains to estimate the genuinely new term \(\mathcal N_m\) in (4.1).
When \(j=m,i=0\),

\[
 \left|\int |V|^{p-2}V*(aG*V)\right|\le C\|V\|_p^p.            \tag{7.13}
\]

When \(j<m\), Hölder and Young give

\[
 \left|\int |V|^{p-2}V*(\nabla^ia*G*\nabla^jU)\right|
 \le C(1+\|V\|_p^p),                                          \tag{7.14}
\]

using \(C_i(q)\) and \(A_j(q)\) already available in (7.3). Equations
(7.13)--(7.14) have no derivative to absorb and require no new node in the
graph. Together with the standard estimates for the remaining lines of
(4.1), they yield

\[
 \frac d{dt}A_m(p)^p+cD_m\le C(1+A_m(p)^p).                   \tag{7.15}
\]

### 7.4 Completion of the induction

Starting from (5.1), (6.6), and the coupled step (7.4)--(7.5), iterate (7.3):

1. Equation (4.3) bounds \(C_m\) from \(A_{\le m-1}\).
2. Equation (7.8) at order \(m-1\) bounds \(B_{m-1}\), requiring cutoff
   derivatives only through \(m\).
3. Equation (7.15) bounds \(A_m\), requiring unweighted derivatives only
   through \(m-1\) and cutoff derivatives only through \(m\).

This proves \(A_m(p)<\infty\) for every \(m\) and every sufficiently large
\(p\). Uniform Sobolev and the \(A_m,A_{m+1}\) estimates imply

\[
 \sup_{M\times[0,T)}|\nabla^mU|<\infty\quad\text{for every }m. \tag{7.16}
\]

The dependence on the individual higher derivatives of \(g_0\) and \(\chi\)
enters through the finite initial norms in each stage; this is permitted and
is not an a priori terminal-time assumption.

## 8. Smooth extension and the normalized DeTurck restart

Since \(\nabla G=0\) at each time,

\[
 \nabla^m(a\operatorname{Rm})
 =\nabla^mU-\nabla^m(aG)
 =\nabla^mU-(\nabla^ma)*G.                                    \tag{8.1}
\]

Equations (4.3) and (7.16) therefore bound every derivative of
\(a\operatorname{Rm}\). Also (2.11) gives

\[
 \nabla^m\partial_tg=-2\operatorname{Ric}(\nabla^mU),          \tag{8.2}
\]

with only harmless index contractions by \(g\). Wang's connection-difference
argument (equivalently, the Hamilton extension criterion adapted to the fixed
coefficient) then shows that \(g(t)\) converges in \(C^\infty\) to a smooth
metric \(g(T)\).

For completeness, the restart can be formulated without pretending the
cutoff stays fixed in gauge coordinates. With a fixed smooth background
metric \(s\), define

\[
 W(\widehat g,s)^k=\widehat g^{pq}
 (\Gamma(\widehat g)^k{}_{pq}-\Gamma(s)^k{}_{pq}).              \tag{8.3}
\]

The normalized local Ricci--DeTurck system is

\[
 \partial_t\widehat g
 =-2\widehat a(\operatorname{Ric}(\widehat g)+\widehat g)
   +\mathcal L_{\widehat aW}\widehat g,                        \tag{8.4}
\]

coupled to the transported coefficient

\[
 \widehat a=a\circ\phi_t^{-1},\qquad
 \partial_t\phi_t\circ\phi_t^{-1}=-\widehat aW.                \tag{8.5}
\]

Equivalently, differentiating \(\phi_t^*\widehat a=a\) gives

\[
 \partial_t\widehat a=(\widehat aW)\cdot\widehat\nabla\widehat a. \tag{8.6}
\]

If \(g=\phi_t^*\widehat g\), (8.4)--(8.5) cancel the Lie derivative and pull
back both terms in the parentheses to give precisely

\[
 \partial_tg=-2a(\operatorname{Ric}(g)+g).                    \tag{8.7}
\]

Transporting the coefficient only in front of Ricci, but not in front of
\(\widehat g\), would not reproduce the desired equation.

When \(a\) vanishes, (8.4) is degenerate rather than uniformly parabolic. The
local-existence construction used by Yang/Wang regularizes the coefficient,
solves strictly parabolic approximants, and takes a limit using estimates
adapted to \(a=\chi^2\). Adding \(-2\widehat a\widehat g\) changes only the
zeroth-order part of that system; it changes neither its principal symbol nor
the transported-coefficient equation. The same construction therefore starts
(1.1) from the smooth terminal metric. Pullback, uniqueness, and pasting with
the original solution produce an extension to \([0,T+\delta)\).

## 9. Audit of the possible obstruction

The transfer succeeds. The terms that could have broken it have been tracked
as follows:

- \(\partial_tG\) is included exactly in (2.7), including the factor
  \(1/(n-1)\).
- The raw \((\nabla^2a)*E\) term is present in (3.4)--(3.5); it is not
  discarded.
- \(\nabla^{m+2}a\), hence \(\chi\nabla^{m+2}\chi\), is present in (3.8) and
  (4.2), then removed by the integrations leading to (7.12).
- \(\nabla^{m+1}U\) is present in \(\Gamma_4\) and absorbed by weighted
  diffusion, not used as inductive input.
- Unweighted \(\nabla^m\widetilde R\) requires
  \(\nabla^{m+1}\chi\), but the triangle uses that estimate one level lower,
  exactly as in (7.3).
- The new \(G\)-terms are explicitly (7.9) and \(\mathcal N_m\); estimates
  (7.13)--(7.14) show rather than assert that they introduce no top derivative.
- The base \(L^p\) estimate integrates the Hessian of the cutoff and uses
  \(|\nabla a|^2/a=4|\nabla\chi|^2\), so it assumes no higher cutoff bound.

The executable check in
Sessions/S0910A03/workspace/codex_loop/work/verify_shifted_curvature.py
verifies the convention-sensitive contraction and variation identities and
the highest cutoff allocations.

## 10. Source alignment

The derivative templates, base estimate, and induction order used above were
checked against Section 4 (Theorem 4.1, Lemmas 4.4--4.6 and 4.10--4.11, and
Propositions 4.13--4.14) of
Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md.
The transported-coefficient restart was checked against Section 8 of
Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md.
The exact full-velocity variation (3.1)--(3.5) agrees with
Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md.
