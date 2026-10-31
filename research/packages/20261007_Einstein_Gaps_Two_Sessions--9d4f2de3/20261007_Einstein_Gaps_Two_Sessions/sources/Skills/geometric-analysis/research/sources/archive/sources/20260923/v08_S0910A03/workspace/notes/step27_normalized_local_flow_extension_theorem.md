# Step 27: normalized local Ricci flow extension via shifted curvature

## 1. Statement

Let \(M^n\) be closed, let \(\chi\in C^\infty(M)\), set
\(a=\chi^2\), and let

\[
\partial_tg=-2a(\operatorname{Ric}_g+g),\qquad 0\le t<T<\infty,
\tag{1.1}
\]

be a smooth solution.  If

\[
\sup_{M\times[0,T)}|a\operatorname{Rm}_g|_g<\infty,
\tag{1.2}
\]

then \(g(t)\) has a smooth positive-definite limit at \(T\) and extends as a
smooth solution of (1.1) to \([0,T+\varepsilon)\).

The constants in this extension result may depend on the individual smooth
triple \((M,g_0,\chi)\), on \(T\), and on (1.2).  This is exactly what the
four-dimensional first-exit argument needs: sequence-uniform higher cutoff
jets are not part of the extension statement.

The proof below transfers Wang's Section 4 derivative induction without
suppressing its highest cutoff derivatives.

## 2. Curvature convention and the parallel shift

Use the curvature convention

\[
g^{ik}R_{ijkl}=\operatorname{Ric}_{jl}
\]

and the Kulkarni--Nomizu convention

\[
(g\owedge g)_{ijkl}=2(g_{ik}g_{jl}-g_{il}g_{jk}).
\]

Define

\[
G=\frac{g\owedge g}{2(n-1)},\qquad
T=\operatorname{Rm}+G,\qquad U=aT.
\tag{2.1}
\]

Then

\[
\operatorname{Ric}(G)=g,
\quad \operatorname{Ric}(T)=\operatorname{Ric}+g=:E,
\quad \operatorname{Ric}(U)=aE.
\tag{2.2}
\]

At every fixed time,

\[
\nabla G=0,
\qquad \nabla^rT=\nabla^r\operatorname{Rm}\quad(r\ge1).
\tag{2.3}
\]

If \(h=\partial_tg=-2aE\), then

\[
(\partial_tG)_{ijkl}
=\frac1{n-1}
(h_{ik}g_{jl}+g_{ik}h_{jl}-h_{il}g_{jk}-g_{il}h_{jk}),
\tag{2.4}
\]

so \(\partial_tG\) is algebraic in \(aE\) and \(g\).  It contains no spatial
derivative of either factor.  Moreover,

\[
|U|\le |a\operatorname{Rm}|+C_n\|a\|_\infty,
\tag{2.5}
\]

so (1.2) is equivalent to a uniform bound \(|U|\le K\).

The all-covariant shifted evolution has the universal-contraction form

\[
(\partial_t-a\Delta)T
=da*\nabla T+\nabla^2a*T+a(T*T+G*T).
\tag{2.6}
\]

Every term on the right contains \(T\) or a derivative of \(T\).  In
particular there is no independent \(\nabla^2a*G\) source.  This follows either
by inserting \(E=\operatorname{Ric}(T)\) into the full curvature variation and
adding (2.4), or by observing that \(T=0\) is the stationary curvature
condition \(\operatorname{Ric}=-g\).  Hence the algebraic reaction vanishes at
\(T=0\); schematically it is bounded by

\[
C_n(|T|+|T|^2),
\tag{2.7}
\]

not by a genuinely forced constant.

Multiplying by the fixed scalar \(a\) and using
\(\Delta(aT)=a\Delta T+2da*\nabla T+(\Delta a)T\) gives a nonsingular equation
for \(U\):

\[
(\partial_t-a\Delta)U
=da*\nabla U+\nabla^2a*U+d\chi*d\chi*U+U*U+aG*U.
\tag{2.8}
\]

No division by \(a\) is used.  Identities such as
\(|da|^2T=4|d\chi|^2U\) extend across \(\{a=0\}\).

## 3. The differentiated systems

Commuting \(m\) covariant derivatives in (2.6) gives

\[
\begin{aligned}
\partial_t\nabla^mT={}&a\Delta\nabla^mT\\
&+\sum_{i+j+k=m+2,\ k\le m+1}
 \nabla^i\chi*\nabla^j\chi*\nabla^kT\\
&+\sum_{i+j+k=m}
 \nabla^ia*\nabla^jT*\nabla^kT
 +\sum_{i+k=m}\nabla^ia*G*\nabla^kT.
\end{aligned}
\tag{3.1}
\]

Likewise (2.8) yields

\[
\begin{aligned}
\partial_t\nabla^mU={}&a\Delta\nabla^mU\\
&+\sum_{i+j+k=m+2,\ k\le m+1}
 \nabla^i\chi*\nabla^j\chi*\nabla^kU\\
&+\sum_{i+j+k=m,\ k\le m-1}
 \nabla^ia*\nabla^jU*\nabla^kT
 +U*\nabla^mU+\mathcal G_m.
\end{aligned}
\tag{3.2}
\]

Each monomial in \(\mathcal G_m\) has one parallel \(G\)-factor, one
\(\nabla^sU\) with \(s\le m\), and cutoff derivatives of order at most \(m\).
When \(s=m\), its coefficient is the bounded tensor \(aG\).

The highest cutoff contribution in (3.2) is not lower order pointwise.  It is

\[
\chi\nabla^{m+2}\chi*U,
\tag{3.3}
\]

accompanied by

\[
\nabla\chi*\nabla^{m+1}\chi*U,
\qquad
\chi\nabla^{m+1}\chi*\nabla U.
\tag{3.4}
\]

Let \(W=\nabla^mU\).  In the \(L^p\) energy of \(W\), integrate (3.3) by
parts once:

\[
\begin{aligned}
\int |W|^{p-2}\langle W,\chi\nabla^{m+2}\chi*U\rangle
={}&-\int\nabla(|W|^{p-2}W)*\chi\nabla^{m+1}\chi*U\\
&-\int|W|^{p-2}W*\nabla\chi*\nabla^{m+1}\chi*U\\
&-\int|W|^{p-2}W*\chi\nabla^{m+1}\chi*\nabla U.
\end{aligned}
\tag{3.5}
\]

The first term satisfies

\[
|\text{first term}|
\le \varepsilon\int a|\nabla W|^2|W|^{p-2}
 +C_{p,\varepsilon}K^2
  \int|\nabla^{m+1}\chi|^2|W|^{p-2}.
\tag{3.6}
\]

The factor \(\chi\) in (3.3) is exactly what matches the diffusion weight
\(a=\chi^2\).  Equations (3.5)--(3.6) lower the highest cutoff order from
\(m+2\) to \(m+1\); no such derivative remains after this integration by
parts.  The remaining products are estimated with the same staggered large
\(L^p\) exponents used in Wang's Lemma 4.11 and Proposition 4.14.  The
\(G\)-terms never have the derivative count of (3.3) and add only bounded
linear coefficients or previously controlled lower derivatives.

## 4. Cutoff derivative evolution

The shifted contraction identity is exact:

\[
aE=\operatorname{Ric}(U),
\qquad
\nabla^q(aE)=\operatorname{Ric}(\nabla^qU).
\tag{4.1}
\]

There are no spatial lower-order corrections in (4.1), because \(\nabla g=0\).
The connection variation is

\[
\partial_t\Gamma=g^{-1}*\nabla(aE)
                 =g^{-1}*\nabla\operatorname{Ric}(U).
\tag{4.2}
\]

Since \(\chi\) is a fixed scalar, for \(r\ge2\),

\[
\partial_t\nabla^r\chi
 =\sum_{q=0}^{r-2}\nabla^q(\partial_t\Gamma)
                       *\nabla^{r-1-q}\chi.
\tag{4.3}
\]

Including the evolving norm gives

\[
\partial_t|\nabla^r\chi|
\le C_rK|\nabla^r\chi|
 +C_r\sum_{s=1}^{r-1}|\nabla^sU|\,|\nabla^{r-s}\chi|.
\tag{4.4}
\]

At \(r=m+1\), the only current-order input is
\(|\nabla^mU||\nabla\chi|\).  Thus, after Hölder,

\[
\|\nabla^{m+1}\chi(t)\|_{L^p}
\le C+C\int_0^t\bigl(1+\|\nabla^mU(s)\|_{L^{p_1}}\bigr)\,ds,
\tag{4.5}
\]

with lower derivatives already controlled.  Formula (4.5) is the normalized
version of Wang Lemma 4.6.

## 5. Base bounds

From \(|U|\le K\) and \(\partial_tg=-2\operatorname{Ric}(U)\),

\[
|\partial_tg|_g\le C_nK.
\tag{5.1}
\]

Therefore the metrics are uniformly equivalent on \([0,T)\).  The volume
forms, the nonhomogeneous Sobolev constants on the fixed closed manifold, and
\(|d\chi|\) are uniformly controlled.

Testing (2.6) by \(|T|^{p-2}T\), integrating the Hessian-cutoff term once, and
using only the tensor quotient

\[
\frac{da\otimes da}{a}=4d\chi\otimes d\chi
\tag{5.2}
\]

(which extends across \(a=0\)) gives, for every finite sufficiently large
\(p\),

\[
\frac d{dt}\int|T|^p
+c_p\int a|\nabla T|^2|T|^{p-2}
\le C_p(1+K)\left(1+\int|T|^p\right).
\tag{5.3}
\]

Here \(aT*T=U*T\); norm and measure variations have coefficients bounded by
\(U\); and \(aG*T\) is linear with a bounded coefficient.  Grönwall gives

\[
\sup_{t<T}\|T(t)\|_{L^p}<\infty
\quad\text{for every finite }p.
\tag{5.4}
\]

Thus the zeros of \(a\) do not hide an unbounded unweighted curvature norm.
Outside \(\operatorname{supp}\chi\), the metric is stationary; its fixed
curvature contributes a finite, though not sequence-uniform, amount.

At the first derivative level, (3.5)--(3.6) with \(m=1\) and (4.4) with
\(r=2\) give the same coupled estimates as Wang Lemma 4.11.  With the finite
staggered exponents used there, one obtains a quantity \(Y_1\), composed of
\(\|\nabla U\|_{L^p}^2\) and \(\|\nabla^2\chi\|_{L^q}^2\), satisfying

\[
Y_1'(t)\le C\left(1+Y_1(t)+\int_0^tY_1(s)\,ds\right).
\tag{5.5}
\]

The extra \(G\)-terms contribute only \(CY_1+C\).  Wang's Volterra comparison
lemma yields a uniform bound for \(Y_1\) on \([0,T)\).

## 6. High-order induction

Assume for all finite large exponents that

\[
\nabla^\ell U\ (\ell<m),\qquad
\nabla^\ell T\ (\ell<m),\qquad
\nabla^r\chi\ (r\le m)
\tag{6.1}
\]

are uniformly bounded in their required \(L^p\) spaces, and that the lower
\(U\)-derivatives have the corresponding \(L^\infty\) bounds obtained by
Sobolev embedding.

The induction is most clearly ordered in three moves at each level.

**Move A: current weighted curvature and current cutoff jet.**  Estimate
\(\nabla^mU\) together with \(\nabla^{m+1}\chi\).  Equations (3.2)--(3.6)
show that the \(\nabla^mU\) energy uses only

\[
\nabla^{m-1}T,
\qquad \nabla^{m+1}\chi,
\qquad\text{the quantities in (6.1)}.
\tag{6.2}
\]

Equation (4.5) expresses \(\nabla^{m+1}\chi\) through a time integral of
\(\nabla^mU\).  To make the exponent bookkeeping explicit, choose a finite
descending family of exponents, all larger than \(n+2\), so that every
product in (3.5) is controlled by Hölder from one current \(L^p\) norm and
previous-level norms; for example the quadratic top remainder uses

\[
\int |\nabla^{m+1}\chi|^2|U|^2|W|^{p-2}
\le K^2\|\nabla^{m+1}\chi\|_{L^p}^2\|W\|_{L^p}^{p-2},
\tag{6.3}
\]

and terms with an extra \(\nabla U\) use a larger auxiliary exponent already
available from the \(m=1\) base step and its Sobolev upgrades.  This is exactly
the finite staggered-exponent device in Wang's proof; only the coefficients
have changed.  Summing the finitely many current norms gives \(Y_m\) with

\[
Y_m'(t)
\le C_m\left(1+Y_m(t)+\int_0^tY_m(s)\,ds\right).
\tag{6.4}
\]

All \(G\)-monomials have either a bounded coefficient multiplying the current
\(U\)-derivative or lower derivatives already in (6.1), so they only enlarge
\(C_m\).  Wang's Volterra comparison bounds \(\nabla^mU\) and
\(\nabla^{m+1}\chi\) in every finite required \(L^p\) space.

**Move B: current unweighted curvature.**  Use (3.1) at order \(m\).  Its
highest cutoff term \(\chi\nabla^{m+2}\chi*T\) is integrated by parts once,
so the resulting estimate uses cutoff derivatives only through order
\(m+1\), now available from Move A, and lower \(T\)-derivatives from (6.1).
Terms produced by the connection commutator, such as
\(\operatorname{Ric}(\nabla^mU)*T\), are estimated by Hölder using the current
\(L^{p_1}\) bound for \(\nabla^mU\), the arbitrarily high finite \(L^{p_2}\)
bounds for \(T\) from (5.4), and \(1/p_1+1/p_2=1/p\); they do not require an
unweighted \(L^\infty\) curvature bound.  This is Wang Proposition 4.13 with
an additional bounded linear \(G*T\) reaction.  It gives

\[
\sup_{t<T}\|\nabla^mT(t)\|_{L^p}<\infty
\quad\text{for every finite required }p.
\tag{6.5}
\]

**Move C: Sobolev upgrade.**  Taking exponents above \(n\), and applying the
uniform Sobolev inequality to the next derivative level, upgrades the finite
\(L^p\) estimates to

\[
\sup_{M\times[0,T)}|\nabla^mU|<\infty
\qquad(m=0,1,2,\ldots).
\tag{6.6}
\]

The accurate current-order dependency is

\[
\nabla^mU\longleftrightarrow\nabla^{m+1}\chi,
\qquad
\nabla^{m-1}T\text{ uses only }\nabla^m\chi.
\tag{6.7}
\]

For the second relation, apply the unweighted estimate at order \(m-1\): its
raw top source \(\chi\nabla^{m+1}\chi*T\) loses one derivative under the
energy integration by parts and therefore uses \(\nabla^m\chi\), already
available from the previous weighted level.  Thus \(\nabla^{m-1}T\) is known
before Move A.  This is the normalized counterpart of Wang Propositions
4.13--4.14.

## 7. Smooth terminal metric and restart

By (4.1) and (6.6), every covariant derivative of the compactly supported
velocity

\[
\partial_tg=-2\operatorname{Ric}(U)
\tag{7.1}
\]

is bounded.  Let \(A(t)=\nabla^{g(t)}-\nabla^{g_0}\).  From

\[
\partial_tA=g^{-1}*\nabla\operatorname{Ric}(U),
\tag{7.2}
\]

and its fixed-background derivatives, induction gives uniform bounds for all
\(\nabla_{g_0}^rA\).  Equations (7.1)--(7.2) then show that all fixed-coordinate
spatial derivatives of \(\partial_tg\) are bounded and integrable on the
finite interval.  Therefore \(g(t)\) is Cauchy in every \(C^r\) norm and
converges smoothly to a metric \(g(T)\).  Uniform metric equivalence from
(5.1) makes \(g(T)\) positive definite.

For short-time existence at \(g(T)\), use Yang's transported-coefficient
DeTurck system with

\[
\widehat a=(\chi\circ\varphi_t^{-1})^2,
\qquad
\partial_t\widehat g
=-2\widehat a(\operatorname{Ric}(\widehat g)+\widehat g)
 +\mathcal L_V\widehat g.
\tag{7.3}
\]

The added \(-2\widehat a\widehat g\) is zeroth order in the metric and leaves
the regularized principal operator unchanged.  Since
\(\varphi_t^*\widehat a=a\), pullback cancels the gauge Lie derivative and
returns (1.1) with the original fixed cutoff.  Restarting at \(g(T)\) extends
the solution beyond \(T\), proving the theorem.

## 8. Interface with the four-dimensional first-exit argument

The whole-support Moser estimate from Step 26 has the form

\[
\|a\operatorname{Rm}(t)\|_\infty\le C\bar\beta/t,
\qquad 0<t<T_{\max}.
\tag{8.1}
\]

If \(0<T_{\max}<\theta r^2\), then (8.1) is uniformly bounded on
\([T_{\max}/2,T_{\max})\); smooth short-time existence supplies a bound on the
earlier compact interval.  The extension theorem therefore contradicts the
maximality of \(T_{\max}\).  This closes the continuation part of the
simultaneous first-exit argument.  The apparent singularity of (8.1) at
\(t=0\) is irrelevant to extension across a positive terminal time.

After continuation to the common positive time, uniform higher derivatives
across the pinching sequence are obtained only on a smaller \(a=1\) plateau
through ordinary normalized Ricci-flow interior estimates.  The theorem above
needs no sequence-uniform higher cutoff jets.

## 9. Scope

This theorem closes the smooth-continuation subproblem inside the current
four-dimensional negative Ishida--LeBrun route.  It does not by itself prove a
Ricci-pinching gap: the selected-support construction, terminal calibration
selection, and smooth-limit passage must still be read as one connected
argument.  Even a completed gap for that family would not settle the positive
branch, arbitrary topology, dimensions \(n\ge5\), the dimension-only interval
quantifiers, or the requested Lean formalization of the full Yau 26 result.

## 10. Verification record

- Source mechanism: Wang, Section 4, Theorem 4.1 and Lemmas/Propositions
  4.4--4.14.
- Short-time construction: Yang, Section 8.
- Full-velocity variation: A01
  `workspace/codex_loop/work/tensor_energy_derivation.md`.
- Shift bookkeeping script:
  `workspace/scripts/verify_step27_shifted_curvature_algebra.py` (exit 0).
- Independent TTCS reading:
  `trace/ttcs/results/step27_ttcs01_verifier1_integration.md` and
  `trace/ttcs/results/step27_ttcs01_verifier2_integration.md`.
- The session Codex worker is independently deriving the same transfer; its
  report must be inspected in a later step before the entire downstream chain
  is sent for scientific review.
