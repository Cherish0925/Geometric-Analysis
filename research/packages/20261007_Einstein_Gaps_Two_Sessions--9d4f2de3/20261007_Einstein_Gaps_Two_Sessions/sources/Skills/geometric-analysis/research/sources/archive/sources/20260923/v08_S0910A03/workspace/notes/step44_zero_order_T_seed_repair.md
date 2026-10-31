# Step 44: zero-order unweighted shifted-curvature seed

## 0. Purpose and corrected status

The Step 43 general-order note incorrectly initialized the staggered continuation
induction by saying that bounded \(U=aT\), metric equivalence, and finite total
curvature imply \(T\in L^q\) uniformly up to a maximal endpoint.  They do not:
where \(a\) is small, \(aT\) can stay bounded while \(T\) grows.  The missing
seed is instead a direct unweighted energy estimate for

\[
 T=\operatorname{Rm}+G,\qquad
 G=\frac{g\owedge g}{2(n-1)},\qquad U=aT,\qquad a=\chi^2,
\]

along

\[
 \partial_tg=-2aE=-2\operatorname{Ric}(U),\qquad
 E=\operatorname{Ric}+g=\operatorname{Ric}(T).
\]

This note records the repaired estimate and the corresponding correction to the
higher-order continuation schedule.  It is a per-datum continuation estimate,
not one of the sequence-uniform smoothing estimates.

## 1. Tensor evolution structure needed at zero order

For the local Ricci part of the flow, the standard curvature variation formula,
together with \(\nabla G=0\), has the form

\[
 \partial_tT
 =a\Delta T+a\,\mathcal Q(T,G)
  +\nabla a*\nabla T+(\nabla^2a)*E+\mathcal N(a,T,G),              \tag{1.1}
\]

where

\[
 |\mathcal Q(T,G)|\le C_n(|T|^2+|T|+1),                          \tag{1.2}
\]

and the normalization and variation of \(G\) obey

\[
 |\mathcal N(a,T,G)|\le C_n(a|T|+a).                             \tag{1.3}
\]

Indeed,

\[
 \partial_tG=-\frac{2a}{n-1}(E\owedge g),
\]

so \(|\partial_tG|\le C_na|T|\).  The important structural points are:

1. every quadratic curvature reaction carries the coefficient \(a\), hence
   \(a|T|^{p+1}=|U|\,|T|^p\);
2. the Hessian-cutoff term is a signed contraction with \(E\), not an absolute
   \(|\nabla^2\chi|\)-coefficient;
3. the variation of the tensor norm and volume form is controlled by
   \(a|E|\le C_n|U|\).

The exact numerical coefficients in (1.1) are irrelevant for this energy
estimate, but the three structural statements above are essential.

## 2. The \(L^p\) estimate

Assume a smooth solution exists on \([\tau,T_*)\), \(0<\tau<T_*<\infty\),
and

\[
 \sup_{M\times[\tau,T_*)}|U|\le K.                               \tag{2.1}
\]

For fixed \(p\ge2\), set

\[
 \mathcal T_p(t)=\int_M|T|^p\,d\mu_g,
 \qquad
 \mathcal D_p(t)=\int_Ma|T|^{p-2}|\nabla T|^2\,d\mu_g.           \tag{2.2}
\]

Because \(T\) is a covariant curvature-type tensor,

\[
 \partial_t|T|^p
 =p|T|^{p-2}\langle\partial_tT,T\rangle
  +O_n\bigl(p\,a|E|\,|T|^p\bigr),                               \tag{2.3}
\]

and

\[
 \partial_t(d\mu_g)=-a\operatorname{tr}(E)d\mu_g.               \tag{2.4}
\]

Both extra terms are bounded by \(C_{n,p}K|T|^p\), because
\(a|E|=|\operatorname{Ric}(U)|\le C_nK\).

### 2.1 Diffusion and first-cutoff derivatives

Testing \(a\Delta T\) against \(p|T|^{p-2}T\) gives the usual negative
quadratic form plus

\[
 C_np\int|\nabla a|\,|T|^{p-1}|\nabla T|.
\]

The explicit \(\nabla a*\nabla T\) terms have the same size.  Young's
inequality and

\[
 \frac{|\nabla a|^2}{a}=4|d\chi|^2                              \tag{2.5}
\]

(with zero extension at \(a=0\)) give

\[
 C_np\int|\nabla a||T|^{p-1}|\nabla T|
 \le \varepsilon\mathcal D_p
   +C_{n,p,\varepsilon}\|d\chi\|_\infty^2\mathcal T_p.          \tag{2.6}
\]

### 2.2 Quadratic reaction through \(U=aT\)

By (1.2),

\[
 \begin{split}
 \left|p\int a|T|^{p-2}\langle\mathcal Q(T,G),T\rangle\right|
 &\le C_{n,p}\int\bigl(a|T|^{p+1}+a|T|^p+a|T|^{p-1}\bigr)\\
 &\le C_{n,p}(K+1)\mathcal T_p+C_{n,p}(K+1)\operatorname{Vol}(g(t)).
 \end{split}                                                     \tag{2.7}
\]

Here the leading term uses exactly

\[
 a|T|^{p+1}=|aT|\,|T|^p\le K|T|^p.                              \tag{2.8}
\]

The lower powers are handled by Young.  The normalization and \(G\)-variation
terms satisfy the same bound.

### 2.3 Signed Hessian-\(a\) contraction

The Hessian contribution can be written

\[
 I_H=p\int_M(\nabla_i\nabla_ja)\,
       \mathcal B^{ij}(T,E)|T|^{p-2}\,d\mu,                     \tag{2.9}
\]

where, for the contractions produced by curvature variation,

\[
 |\mathcal B(T,E)|\le C_n|T||E|\le C_n|T|^2,
 \qquad
 |\nabla\mathcal B(T,E)|\le C_n|T||\nabla T|.                    \tag{2.10}
\]

The second estimate uses that \(E\) is a trace of \(T\), so \(\nabla E\) is a
trace of \(\nabla T\), and \(\nabla G=0\).  Since \(M\) is closed, integrate
(2.9) once by parts without taking an absolute value first:

\[
 I_H=-p\int_M(\nabla_ja)\nabla_i
      \left(\mathcal B^{ij}(T,E)|T|^{p-2}\right)d\mu.            \tag{2.11}
\]

Using (2.10), (2.5), and Young,

\[
 |I_H|\le\varepsilon\mathcal D_p
   +C_{n,p,\varepsilon}\|d\chi\|_\infty^2\mathcal T_p.          \tag{2.12}
\]

Thus no pointwise Hessian bound for \(\chi\) is used.

### 2.4 Conclusion

After choosing \(\varepsilon\) small, the preceding terms give

\[
 \boxed{
 \frac d{dt}\mathcal T_p+c_{n,p}\mathcal D_p
 \le C_{n,p}\bigl(K+1+\|d\chi\|_\infty^2\bigr)\mathcal T_p
   +C'_{n,p}(K+1)\operatorname{Vol}(g(t)).}                      \tag{2.13}
\]

The volume is uniformly finite on the finite slab because
\(|\partial_tg|\le C_nK\) gives bilipschitz metric comparison.  Since the
solution is smooth at time \(\tau\), \(\mathcal T_p(\tau)<\infty\).
Gronwall therefore yields

\[
 \sup_{t\in[\tau,T_*)}\|T(t)\|_{L^p(g(t))}<\infty               \tag{2.14}
\]

for every finite \(p\ge2\).  This is the actual \(T_0\) seed.

The additive finite-volume term is harmless here because continuation needs
finiteness, not the relative, collapse-uniform, homogeneous estimate used in
the first-exit smoothing argument.

## 3. Repair of the higher-order schedule

With (2.14) available for every finite exponent, the Step 40 staggered order
can start:

\[
 T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
 \longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots. \tag{3.1}
\]

At the unweighted \(T_m\) stage, the Step 43 connection-variation paragraph
must also be corrected.  One must not say that \(T\) is pointwise bounded
because total curvature is finite.  Instead,

\[
 \nabla^j(\partial_t\Gamma)=g^{-1}*\nabla^{j+1}\operatorname{Ric}(U)
 +\text{products of lower connection/metric derivatives},       \tag{3.2}
\]

so every connection-variation product is allocated using the already obtained
finite-exponent \(U\)-levels and previous \(T\)-levels.  At fixed \((m,p)\),
Hölder only asks for finitely larger exponents of previously completed spatial
levels.  The current \(T_m\) never needs a pointwise \(T_0\) coefficient.

For \(m=1\), the term

\[
 \int\chi\,\nabla^2\chi*|\nabla T|^p                           \tag{3.3}
\]

is retained with its signed contraction and treated by the Step 38 Hessian
integration-by-parts lemma; it is not bounded by an assumed
\(\|\nabla^2\chi\|_\infty\).  For general \(m\), the only new cutoff jet in
\(\nabla^{m+2}a\) is \(2\chi C_{m+2}\), which is integrated once down to
\(C_{m+1}\), as in Step 40.  The weighted \(U_m\) stage retains the second
integration by parts for every \(\chi C_{m+1}U_1P(U_m)\) term.

Therefore (2.13), together with the already verified Step 40 signed-IBP
mechanisms, repairs the initialization and the two unsupported assertions in
the Step 43 note.  It does not by itself establish short-time existence or
restart.

## 4. Consequence for current theorem status

The corrected continuation package has two logically distinct inputs:

1. **positive-time derivative propagation:** (2.13) supplies \(T_0\), then the
   Step 40 staggered finite-exponent induction supplies all \(U_m,C_{m+1},T_m\);
2. **start/restart:** a per-datum short-time theorem for the transported
   degenerate DeTurck system.

The first input is now supported at its missing base.  The second still needs a
faithful adaptation of Yang's actual tame inverse, including the metric and
transport variables together.  No small-cutoff-region Schauder shortcut is
used or justified.
