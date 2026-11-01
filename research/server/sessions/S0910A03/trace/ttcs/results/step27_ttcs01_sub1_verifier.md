# TTCS Independent Branch Record

```json
{
  "step_id": 27,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step27_shifted_curvature_continuation_analysis.md",
    "Sessions/S0910A03/workspace/notes/step26_wang_continuation_specification.md",
    "Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Independently verify the shifted-curvature continuation mechanism for the normalized fixed-cutoff flow ∂_t g=-2a(Ric+g), a=χ². Read the Step 27 note, Wang's actual Section 4 proof, Yang's DeTurck construction, and the full-velocity tensor derivation. Check the convention G=(g∧g)/(2(n−1)), Ric(G)=g, ∇G=0, ∂_tG algebraic; derive the schematic evolutions of T=Rm+G and U=aT with all highest cutoff derivatives visible. Then assess whether Wang Lemmas 4.10, 4.11, 4.13, 4.14 transfer without an uncancelled highest-order term. Focus especially on χ∇^{m+2}χ*U, the integration by parts, the cutoff derivative equation driven by Ric(U), and any error in the proposed dependency triangle. Give explicit repairs or a precise obstruction; do not merely call terms lower order.

## Output

# Scientific verification memo

## 1. Algebraic shift

Use the convention

\[
(g\owedge g)_{ijkl}=2(g_{ik}g_{jl}-g_{il}g_{jk}),\qquad
G=\frac{g\owedge g}{2(n-1)}.
\]

Then

\[
G_{ijkl}=\frac{1}{n-1}(g_{ik}g_{jl}-g_{il}g_{jk}),
\]

and contraction in the first and third indices gives

\[
g^{ik}G_{ijkl}
=\frac{ng_{jl}-g_{jl}}{n-1}=g_{jl}.
\]

Thus, for

\[
T=\operatorname{Rm}+G,
\]

one has the exact identity

\[
\operatorname{Ric}(T)=\operatorname{Ric}+g=E.
\]

Metric compatibility gives, at every time,

\[
\nabla G=0,\qquad \nabla^rG=0\quad(r\ge1),
\]

hence

\[
\nabla^rT=\nabla^r\operatorname{Rm}\quad(r\ge1).
\]

For \(h=\partial_tg=-2aE\),

\[
\partial_tG_{ijkl}
=\frac{1}{n-1}
(h_{ik}g_{jl}+g_{ik}h_{jl}-h_{il}g_{jk}-g_{il}h_{jk}),
\]

so explicitly

\[
\partial_tG
=-\frac{2a}{n-1}
(E_{ik}g_{jl}+g_{ik}E_{jl}-E_{il}g_{jk}-g_{il}E_{jk}).
\]

It is therefore algebraic in \(a,E,g\), with no derivative of \(a\) or \(E\).

The equivalence between bounds for \(aT\) and \(a\operatorname{Rm}\) is

\[
aT=a\operatorname{Rm}+aG.
\]

If \(\|\chi\|_\infty\le1\), then \(|aG|\le C_n\). For an arbitrary fixed smooth \(\chi\), the constant is instead \(C_n\|\chi\|_\infty^2\).

A useful correction to Step 27 is that the shifted algebraic polynomial has no constant term. Indeed, \(T=0\) implies \(E=0\), hence \(\partial_tg=0\) and \(\partial_tT=0\). Consequently,

\[
|\mathcal Q_G(T)|\le C_n(|T|+|T|^2),
\]

rather than needing \(C_n(1+|T|+|T|^2)\). The extra \(1\) is harmless in an integral estimate, but it hides an exact cancellation.

## 2. Evolution of \(T\)

The full-velocity formula supplied in the tensor-energy derivation is

\[
\partial_t\operatorname{Rm}
=a\Delta\operatorname{Rm}
+a\mathcal A(\operatorname{Rm})
+da*\nabla E+\nabla^2a*E.
\]

Because \(E=\operatorname{Ric}(T)\), \(\nabla T=\nabla\operatorname{Rm}\), and \(T\) obeys the differential Bianchi identity, the second derivatives of \(\operatorname{Ric}(T)\) produce

\[
\Delta T+\operatorname{Rm}*T
=\Delta T+(T-G)*T.
\]

Adding the algebraic variation of \(G\) yields

\[
\boxed{
(\partial_t-a\Delta)T
=da*\nabla T+\nabla^2a*T
+a(T*T+G*T).
}
\tag{2.1}
\]

All contractions are universal. Every term on the right contains \(T\) or a derivative of \(T\). In particular, there is no term of the form

\[
\nabla^2a*G
\]

and no pure-cutoff term. Any derivation that produces \(\chi\nabla^{m+2}\chi*G\) must also contain cancelling pieces from the normalization and from \(\partial_tG\).

Commuting \(m\) covariant derivatives gives the Wang-type structure

\[
\begin{aligned}
\partial_t\nabla^mT
={}&a\Delta\nabla^mT\\
&+\sum_{\substack{i+j+k=m+2\\ k\le m+1}}
\nabla^i\chi*\nabla^j\chi*\nabla^kT\\
&+\sum_{i+j+k=m}
\nabla^ia*\nabla^jT*\nabla^kT\\
&+\sum_{i+k=m}\nabla^ia*G*\nabla^kT.
\end{aligned}
\tag{2.2}
\]

The highest cutoff contribution is

\[
\chi\nabla^{m+2}\chi*T.
\]

The last line contains cutoff derivatives only through order \(m\), and it always contains a derivative of \(T\). This is the precise replacement for the loosely specified \(G\)-terms in Step 27.

## 3. Evolution of \(U=aT\)

Since \(a\) is fixed as a scalar function, \(\partial_ta=0\). From

\[
\Delta(aT)=a\Delta T+2\,da*\nabla T+(\Delta a)T
\]

and \(a=\chi^2\), equation (2.1) can be rewritten without division by \(a\):

\[
\boxed{
(\partial_t-a\Delta)U
=da*\nabla U+\nabla^2a*U
+d\chi*d\chi*U
+U*U+aG*U.
}
\tag{3.1}
\]

For example,

\[
|da|^2T=4\chi^2|d\chi|^2T=4|d\chi|^2U,
\]

including at points where \(\chi=0\).

After commuting \(m\) derivatives,

\[
\begin{aligned}
\partial_t\nabla^mU
={}&a\Delta\nabla^mU\\
&+\sum_{\substack{i+j+k=m+2\\k\le m+1}}
\nabla^i\chi*\nabla^j\chi*\nabla^kU\\
&+\sum_{\substack{i+j+k=m\\k\le m-1}}
\nabla^ia*\nabla^jU*\nabla^kT\\
&+U*\nabla^mU+\mathcal G_m,
\end{aligned}
\tag{3.2}
\]

where every monomial in \(\mathcal G_m\):

- contains one \(G\) and one derivative \(\nabla^sU\);
- has \(s\le m\);
- contains cutoff derivatives only through order \(m\);
- has coefficient \(aG\) when \(s=m\).

Thus a term with \(\nabla^mU\) contributes at most \(C\|\nabla^mU\|_p^p\) in the energy estimate, while terms with \(s<m\) use already available \(U\)-derivative norms.

The truly highest cutoff piece comes from

\[
\nabla^{m+2}a*U.
\]

Leibniz expansion gives schematically

\[
\nabla^{m+2}a
=
\chi\nabla^{m+2}\chi
+\nabla\chi*\nabla^{m+1}\chi
+\sum_{2\le r\le m}
\nabla^r\chi*\nabla^{m+2-r}\chi.
\]

Hence the relevant terms are exactly

\[
\chi\nabla^{m+2}\chi*U,\qquad
\nabla\chi*\nabla^{m+1}\chi*U,\qquad
\chi\nabla^{m+1}\chi*\nabla U.
\]

No \(G\)-term has this derivative count.

## 4. Integration by parts of the top cutoff term

Let

\[
W=\nabla^mU,\qquad
D_m=\int a|\nabla W|^2|W|^{p-2}.
\]

The top integral has the form

\[
I_m=\int |W|^{p-2}
\left\langle W,\chi\nabla^{m+2}\chi*U\right\rangle.
\]

Transfer one derivative from \(\nabla^{m+2}\chi\). Up to universal contractions,

\[
\begin{aligned}
I_m={}&
-\int \nabla(|W|^{p-2}W)
   *\chi\nabla^{m+1}\chi*U\\
&-\int |W|^{p-2}W
   *\nabla\chi*\nabla^{m+1}\chi*U\\
&-\int |W|^{p-2}W
   *\chi\nabla^{m+1}\chi*\nabla U.
\end{aligned}
\tag{4.1}
\]

The first line satisfies

\[
\left|\text{first line}\right|
\le
\varepsilon D_m+
C_{\varepsilon,p}\int
|\nabla^{m+1}\chi|^2|U|^2|W|^{p-2}.
\tag{4.2}
\]

The factor \(\chi\) is what permits absorption into \(D_m\). The other two lines contain only \(\nabla^{m+1}\chi\), not \(\nabla^{m+2}\chi\).

As in Wang’s Lemma 4.11 and Proposition 4.14, these products are not generally closed at one fixed exponent. One chooses larger exponents \(p_1,p_2\) and uses Hölder, for example

\[
\int |\nabla^{m+1}\chi|^2|W|^{p-2}
\le
\|\nabla^{m+1}\chi\|_{L^p}^2
\|W\|_{L^p}^{p-2},
\]

or a staggered version when the additional \(\nabla U\) factor is not yet in \(L^\infty\). Wang’s use of estimates for every sufficiently large exponent supplies this flexibility.

## 5. Cutoff derivative evolution

The exact contraction identity is

\[
aE=a\operatorname{Ric}(T)=\operatorname{Ric}(U).
\]

There are no spatial-derivative correction terms here because \(\nabla g=0\):

\[
\nabla^q\operatorname{Ric}(U)
=\operatorname{Ric}(\nabla^qU).
\]

Also,

\[
\partial_t\Gamma=g^{-1}*\nabla h
=g^{-1}*\nabla\operatorname{Ric}(U).
\]

For \(r\ge2\),

\[
\partial_t\nabla^r\chi
=
\sum_{q=0}^{r-2}
\nabla^q(\partial_t\Gamma)
*\nabla^{r-1-q}\chi.
\]

Including the variation of the tensor norm gives

\[
\boxed{
\partial_t|\nabla^r\chi|
\le
C_r|U|\,|\nabla^r\chi|
+
C_r\sum_{s=1}^{r-1}
|\nabla^sU|\,|\nabla^{r-s}\chi|.
}
\tag{5.1}
\]

At \(r=m+1\), the only occurrence of the current \(m\)-th derivative is

\[
|\nabla^mU|\,|\nabla\chi|.
\]

After Hölder and integration in time,

\[
\|\nabla^{m+1}\chi(t)\|_{L^p}
\le
C+
C\int_0^t
\bigl(1+\|\nabla^mU(s)\|_{L^{p_1}}\bigr)\,ds,
\tag{5.2}
\]

where all other products use derivatives from earlier induction levels.

## 6. Transfer of Wang’s Section 4 estimates

### Lemma 4.10: unweighted \(L^p\) estimate for \(T\)

Testing (2.1) against \(|T|^{p-2}T\), integrating the Hessian term once, and using

\[
\frac{|da|^2}{a}=4|d\chi|^2
\]

on \(\{a>0\}\), gives

\[
\frac{d}{dt}\int |T|^p
+c_p\int a|\nabla T|^2|T|^{p-2}
\le
C_p(1+\|U\|_\infty)\int |T|^p.
\tag{6.1}
\]

The terms \(aT*T\) are bounded by \(|U||T|^p\), while \(aG*T\), norm variation, and volume variation have bounded coefficients. Thus Wang’s Lemma 4.10 transfers directly.

### Lemma 4.11: simultaneous bounds for \(\nabla U\) and \(\nabla^2\chi\)

For \(m=1\), the top term is

\[
\chi\nabla^3\chi*U.
\]

Equation (4.1) reduces it to expressions containing \(\nabla^2\chi\), \(\nabla U\), and the diffusion of \(\nabla U\). Meanwhile (5.1) with \(r=2\) gives

\[
\partial_t|\nabla^2\chi|
\le
C|U||\nabla^2\chi|
+C|\nabla U||\nabla\chi|.
\]

Hence

\[
\|\nabla^2\chi(t)\|_p
\le C+C\int_0^t\|\nabla U(s)\|_p\,ds.
\]

Substitution into the \(\nabla U\) energy inequality produces Wang’s Volterra form

\[
y'(t)\le C\left(1+y(t)+\int_0^t y(s)\,ds\right).
\]

The new \(G\)-terms contribute only \(Cy\), \(C\), or products with the already bounded \(T\)-norms from (6.1). There is no additional top cutoff derivative.

### Proposition 4.13: unweighted derivatives of \(T\)

For \(\nabla^rT\), the term

\[
\chi\nabla^{r+2}\chi*T
\]

is integrated once. It then requires \(\nabla^{r+1}\chi\), together with previously controlled derivatives of \(T\). The \(G\)-terms in (2.2) contain cutoff derivatives through order \(r\) and \(T\)-derivatives through order \(r\); the term containing \(\nabla^rT\) has bounded coefficient \(aG\).

Consequently,

\[
\nabla^rT \quad\text{uses cutoff derivatives through order }r+1.
\tag{6.2}
\]

### Proposition 4.14: derivatives of \(U\)

At level \(m\), the energy estimate for \(\nabla^mU\) uses

\[
\nabla^{m+1}\chi,\qquad \nabla^{m-1}T,
\]

besides earlier \(U\)-derivatives. Equation (5.2) expresses \(\nabla^{m+1}\chi\) through a time integral of \(\nabla^mU\). After choosing the staggered exponents required by Hölder, one again obtains a finite system of inequalities of the form

\[
y'(t)\le C\left(1+y(t)+\int_0^t y(s)\,ds\right).
\]

Thus the same induction mechanism used by Wang remains available.

## 7. Correction to the dependency triangle

Step 27 overindexes the unweighted-curvature branch by one derivative.

The accurate dependencies at level \(m\) are

\[
\begin{aligned}
A_m:=\|\nabla^mU\|
&\quad\text{uses}\quad
B_{m-1}:=\|\nabla^{m-1}T\|,
\quad C_{m+1}:=\|\nabla^{m+1}\chi\|,\\
B_{m-1}
&\quad\text{uses}\quad C_m,\\
C_{m+1}
&\quad\text{uses a time integral of}\quad A_m.
\end{aligned}
\]

Indeed, Proposition 4.13 says that \(\nabla^rT\) requires cutoff derivatives through \(r+1\); setting \(r=m-1\) gives \(C_m\), not \(C_{m+1}\).

Therefore the current-level cycle is

\[
A_m\longleftrightarrow C_{m+1},
\]

while \(B_{m-1}\) is already obtained from \(C_m\) and earlier levels. This is a useful simplification of Step 27’s triangle.

## 8. Metric comparison, terminal reconstruction, and DeTurck construction

Since

\[
\partial_tg=-2\operatorname{Ric}(U),
\qquad
|\operatorname{Ric}(U)|\le C_n|U|,
\]

a uniform bound for \(U\) gives uniform metric equivalence on every finite time interval. It also controls \(|d\chi|_{g(t)}\) and the compact-manifold Sobolev constants.

Bounds for all \(\nabla^mU\) imply bounds for all spatial derivatives of

\[
aE=\operatorname{Ric}(U),
\]

hence for the velocity, connection variation, and the required coordinate derivatives of \(g(t)\). This is the normalized analogue of Wang’s Proposition 4.3.

Yang’s Section 8 construction uses the transported coefficient

\[
\widehat a=(\chi\circ\varphi_t^{-1})^2.
\]

Adding

\[
-2\widehat a\,\widehat g
\]

to Yang’s hatted metric equation changes only algebraic terms in the linearization. Variation with respect to \(\varphi\) adds \(d\chi*\psi\)-type expressions but no second derivatives of the metric or diffeomorphism variables. The regularized principal system is therefore unchanged. With Yang’s weighted DeTurck vector field,

\[
\frac{d}{dt}\varphi_t^*\widehat g
=
\varphi_t^*
\left(\partial_t\widehat g+\mathcal L_X\widehat g\right),
\]

and the gauge terms cancel, while

\[
\varphi_t^*\widehat a=a.
\]

This yields exactly

\[
\partial_tg=-2a(\operatorname{Ric}(g)+g).
\]

## 9. Overall assessment

There is no uncancelled term carrying \(\nabla^{m+2}\chi\). The sole such contribution is

\[
\chi\nabla^{m+2}\chi*U,
\]

and one integration by parts converts it into diffusion-controlled terms and expressions containing only \(\nabla^{m+1}\chi\). The cutoff evolution is driven exactly by \(\operatorname{Ric}(U)\), which closes the current-level Volterra system.

The two substantive repairs to Step 27 are:

1. pure \(G\)-cutoff terms do not occur; they cancel exactly, and every shifted evolution term contains \(T\) or \(U\);
2. \(\nabla^{m-1}T\) depends on \(\nabla^m\chi\), not on \(\nabla^{m+1}\chi\).

The supplied Step 27 note still omits the staggered-exponent inequalities used in Wang’s Lemma 4.11 and Proposition 4.14, but the shifted normalization introduces no new highest-derivative obstruction.