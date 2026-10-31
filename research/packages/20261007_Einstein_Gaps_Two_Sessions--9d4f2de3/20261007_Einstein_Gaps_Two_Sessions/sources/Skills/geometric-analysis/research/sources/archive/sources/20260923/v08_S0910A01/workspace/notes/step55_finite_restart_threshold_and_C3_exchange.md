# Step 55: finite restart threshold and the next \(C_3\leftrightarrow U_2\) exchange

Session: S0910A01. Agent3 / Actuator. Phase: Execute.

## 0. Question answered here

A03 Step 58 asks for an independent positive-time restart analysis, not another assembly summary.  The task is:

- start on a slab \([\tau,T_*)\), \(\tau>0\), of the exact flow
  \[
  \partial_tg=-2aE=-2\operatorname{Ric}(U),
  \qquad U=aT,
  \qquad T=\operatorname{Rm}+G,
  \]
  with \(a=\chi^2\), \(G=g\owedge g/(2(n-1))\), \(n=4\);
- assume the first-exit endpoint gives \(\|U\|_\infty\le K_\tau<\infty\) and the Step 56 base pair gives
  \[
  T,T_1=\nabla T,U_1=\nabla U,C_2=\nabla^2\chi\in
  L_t^\infty L_x^q\quad \text{for every finite }q;
  \]
- determine what finite current levels are sufficient to restart the A03 Step 56 local theorem in a fixed background with \(s_0>n/2+4=6\);
- explicitly treat the next dangerous term \(\chi C_4*U\) in the \(U_2\) equation and the evolution exchange \(\partial_t C_3\sim C_1*U_2\), without invoking ordinary Shi estimates across the small-cutoff collar.

The conclusion is that no immediate fatal counterterm appears at the next exchange, but A03's statement that higher levels become trivial after \(|T|_\infty\) is too fast in the collar.  A finite current-pair induction is still needed up to \((U_{s_0},C_{s_0+1})\).  For the minimal integer \(s_0=7\), this means through \((U_7,C_8)\), together with unweighted \(T_0,\ldots,T_6\).

> **TTCS correction incorporated.** The principal terms must be grouped as the divergence operator \(\operatorname{div}(a\nabla U_k)\), not as an isolated bounded-coefficient drift.  The \(U_2\) and \(T_2\) equations also contain current signed-Hessian terms \(\chi C_2*U_2\) and \(\chi C_2*T_2\).  These are not bounded-coefficient terms because \(C_2\) is known only in finite \(L^q\) spaces; they are closed by the same signed integration by parts used in Step 56, yielding \(\varepsilon D+C\|C_1\|_\infty^2\|\cdot\|_p^p\).  General schematic formulas below retain the \(\chi\)-weights on the current cutoff terms.

---

## 1. Fixed-background restart threshold

Fix \(\bar\nabla=\nabla^{g(\tau)}\) and \(A=\nabla^{g(t)}-\bar\nabla\).  The connection variation is
\[
\partial_tA=g^{-1}*\nabla(aE).
\tag{1.1}
\]
Applying \(\bar\nabla^m\) and converting derivatives between \(\bar\nabla\) and \(\nabla=\nabla^{g(t)}\) gives the triangular form
\[
\bar\nabla^m\partial_tA
=g^{-1}*U_{m+1}
+P_m\bigl(A,\ldots,\bar\nabla^{m-1}A;
          U_0,\ldots,U_m;g^{-1}\bigr),
\tag{1.2}
\]
where \(U_j=\nabla^j(aT)\).  The right side contains no top \(\bar\nabla^mA\).

To obtain fixed-background \(H^{s_0}\) control of the metric, use
\[
\bar\nabla g=A*g,
\qquad
\bar\nabla^{m+1}g=(\bar\nabla^mA)*g+\text{lower }A\text{ products}.
\tag{1.3}
\]
Thus \(g(t)\) is bounded in \(H^{s_0}\) if \(A_m:=\bar\nabla^mA\) is bounded for \(0\le m\le s_0-1\).  By (1.2), this requires \(U_{m+1}\) for \(m\le s_0-1\), i.e.
\[
U_1,U_2,\ldots,U_{s_0}.
\tag{1.4}
\]
The current-pair hierarchy proving \(U_k\) also carries \(C_{k+1}=\nabla^{k+1}\chi\), because the \(U_k\) equation contains the integrated top cutoff jet \(\chi C_{k+2}\).  Hence the sufficient finite restart package is
\[
\boxed{
T_0,\ldots,T_{s_0-1},
\qquad (U_k,C_{k+1})\quad 1\le k\le s_0.}
\tag{1.5}
\]
For four dimensions the smallest integer allowed by \(s_0>6\) is \(s_0=7\), so a sufficient package is
\[
T_0,\ldots,T_6,
\qquad (U_1,C_2),\ldots,(U_7,C_8).
\tag{1.6}
\]
This is a restart threshold, not a sequence-uniform first-exit input.  Its constants may depend on the datum and on \(\tau\).

To get actual terminal convergence rather than boundedness alone, (1.2) and
\[
\bar\nabla^m\partial_tg=-2\bar\nabla^m(aE)
\tag{1.7}
\]
must be integrated in time.  On a finite positive slab, bounded \(U_j\) and lower \(A_j\) in \(L_t^\infty L_x^2\) imply the needed \(L_t^1H^{s_0}\) control of \(\partial_tg\), so \(g(t)\) has a limit in the restart topology and remains positive by bilipschitz control from \(\int\|U\|_\infty dt<\infty\).

---

## 2. The next weighted pair \((U_2,C_3)\)

Write
\[
U_2=\nabla^2U,
\qquad C_j=\nabla^j\chi,
\qquad D_{2,p}^U=\int a|\nabla U_2|^2|U_2|^{p-2}.
\tag{2.1}
\]
Assume on \([\tau,T_*)\):
\[
\|U\|_\infty\le K,
\qquad T,T_1,U_1,C_2\in L_t^\infty L_x^q\quad\forall q<\infty.
\tag{2.2}
\]
These are the base outputs of A03 Step 56 and Step 57.

### 2.1 Top terms in the \(U_2\) equation

Differentiating the exact \(U=aT\) equation twice, the highest cutoff terms have the schematic form
\[
\partial_tU_2
=\operatorname{div}(a\nabla U_2)
+\chi C_4*U
+\chi C_3*U_1
+\chi C_2*U_2
+C_1*C_3*U+C_2*C_2*U+C_1*C_2*U_1
+\mathcal L_2.
\tag{2.3}
\]
Here \(\mathcal L_2\) contains terms with no cutoff derivative above \(C_2\) except the displayed current signed-Hessian factor, curvature coefficients weighted as \(U\) or bounded by \(|T|\), and finite-exponent lower forcing.  The term \(\chi C_4*U\) is the first new high-cutoff test of the collar mechanism, while \(\chi C_2*U_2\) is the current-order signed-Hessian term that must not be treated as a bounded coefficient.

In the \(L^p\) energy, the dangerous integral is
\[
I_4=
\int |U_2|^{p-2}U_2*\chi C_4*U.
\tag{2.4}
\]
Integrating by parts, using \(C_4=\nabla C_3+\text{connection contractions}\), gives
\[
\begin{aligned}
I_4={}&-\\int \nabla(|U_2|^{p-2}U_2)*\chi C_3*U  \\
&-\int |U_2|^{p-2}U_2*C_1*C_3*U  \\
&-\int |U_2|^{p-2}U_2*\chi C_3*U_1
+\text{lower }A/T\text{ contractions}.
\end{aligned}
\tag{2.5}
\]
The divergence pair \(\operatorname{div}(a\nabla U_2)\) tested against \(|U_2|^{p-2}U_2\) gives the negative term \(-cD_{2,p}^U\).  This grouping is essential: the term \(2\chi C_1*\nabla U_2\) should not be split off as a bounded drift, because doing so would create an uncontrolled \(C_2|U_2|^p\) contribution.

The first line of (2.5) is absorbed directly:
\[
\left|\int \nabla(|U_2|^{p-2}U_2)*\chi C_3*U\right|
\le \varepsilon D_{2,p}^U+C_{p,\varepsilon,K}\int |C_3|^2|U_2|^{p-2}
\le \varepsilon D_{2,p}^U+C(\|C_3\|_p^p+\|U_2\|_p^p+1).
\tag{2.6}
\]
The second line is same-exponent Young because \(C_1\) and \(U\) are bounded:
\[
\left|\int |U_2|^{p-2}U_2*C_1*C_3*U\right|
\le C_{p,K,r}(\|C_3\|_p^p+\|U_2\|_p^p+1).
\tag{2.7}
\]
The third line is the genuine next-exchange counterterm:
\[
I_{31}=
\int \chi |C_3|\,|U_1|\,|U_2|^{p-1}.
\tag{2.8}
\]
It is not controlled by simply treating \(U_1\) as an \(L^\infty\) coefficient.  However it is controlled using the degenerate diffusion of the current variable.  Put
\[
f=\chi |U_2|^{p/2}.
\tag{2.9}
\]
For \(p>2\), Hölder with exponents \((4,p,4,2p/(p-2))\) gives
\[
\begin{aligned}
I_{31}
&\le \|f\|_4\,\|C_3\|_p\,\|U_1\|_4\,
       \||U_2|^{p/2-1}\|_{2p/(p-2)}  \\
&= \|f\|_4\,\|C_3\|_p\,\|U_1\|_4\,\|U_2\|_p^{p/2-1}.
\end{aligned}
\tag{2.10}
\]
For \(p=2\), the last factor is absent and the exponents \((4,2,4)\) give the same conclusion.  The local Sobolev inequality and \(|d\chi|\le Cr^{-1}\) give
\[
\|f\|_4^2
\le C_S\left(p^2D_{2,p}^U+C(p,r)\|U_2\|_p^p\right).
\tag{2.11}
\]
Therefore Young yields
\[
I_{31}
\le \varepsilon D_{2,p}^U
+C_{p,\varepsilon,r,S}\|U_1\|_4^2
\left(\|C_3\|_p^2\|U_2\|_p^{p-2}+\|C_3\|_p\|U_2\|_p^{p-1}\right).
\tag{2.12}
\]
The right side is bounded by
\[
I_{31}
\le \varepsilon D_{2,p}^U
+C_{p,\varepsilon,r,S,\|U_1\|_4}
(1+\|C_3\|_p^p+\|U_2\|_p^p).
\tag{2.13}
\]
This is the useful exact counterterm calculation.  It shows that the next exchange is not automatically trivial, but it is absorbable on a positive-time slab from the base \(U_1\in L^4\) information and the current degenerate diffusion.

The displayed current signed-Hessian term is controlled separately.  Its contribution has the form
\[
J_2=\int \chi(C_2)_{ij}\mathcal B^{ij}(U_2),
\qquad |\mathcal B|\le C|U_2|^p,
\qquad |\nabla\mathcal B|\le Cp|U_2|^{p-1}|\nabla U_2|.
\tag{2.13a}
\]
Since \(C_2=\nabla C_1+\text{lower}\), integration by parts gives
\[
|J_2|\le C\int |C_1|^2|U_2|^p
+Cp\int \chi |C_1||U_2|^{p-1}|\nabla U_2|
\le \varepsilon D_{2,p}^U+C_{p,\varepsilon}\|C_1\|_\infty^2\|U_2\|_p^p.
\tag{2.13b}
\]
Thus no \(C_2\in L^\infty\) assumption is introduced.

All remaining terms in (2.3) are lower in the same sense: either a genuinely bounded coefficient times \(|U_2|^p\), or a product of a previous finite-exponent factor with \(|U_2|^{p-1}\), handled by Hölder/Young with datum-dependent finite constants.

Thus the \(U_2\) inequality has the form
\[
{d\over dt}\|U_2\|_p^p+cD_{2,p}^U
\le C_{p,\tau}\bigl(1+\|U_2\|_p^p+\|C_3\|_p^p\bigr),
\tag{2.14}
\]
where \(C_{p,\tau}\) is allowed to depend on fixed-slab finite norms of \(T,T_1,U_1,C_2\) and the local Sobolev constant of \(g(\tau)\).

### 2.2 Evolution of \(C_3\)

For a fixed scalar \(\chi\), \(C_3=\nabla^3\chi\) is not time-independent.  The commutator formula gives
\[
\partial_tC_3=
(\nabla\partial_t\Gamma)*C_1+(
\partial_t\Gamma)*C_2,
\tag{2.15}
\]
where
\[
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)=g^{-1}*U_1,
\qquad
\nabla\partial_t\Gamma=g^{-1}*U_2+\text{lower}(A,U_1,T,U).
\tag{2.16}
\]
Consequently
\[
\partial_tC_3=C_1*U_2+C_2*U_1+\text{lower finite-exponent terms}.
\tag{2.17}
\]
The \(L^p\) energy satisfies
\[
\begin{aligned}
{d\over dt}\|C_3\|_p^p
&\le C\int |C_3|^{p-1}|U_2| \\
&\quad +C\int |C_3|^{p-1}|C_2||U_1|+C_{p,\tau}(1+\|C_3\|_p^p).
\end{aligned}
\tag{2.18}
\]
The first integral is same-exponent Young:
\[
\int |C_3|^{p-1}|U_2|
\le C(\|C_3\|_p^p+\|U_2\|_p^p).
\tag{2.19}
\]
For the second, Hölder with exponents \((p/(p-1),2p,2p)\) gives
\[
\int |C_3|^{p-1}|C_2||U_1|
\le \|C_3\|_p^{p-1}\|C_2\|_{2p}\|U_1\|_{2p}
\le C_{p,\tau}(1+\|C_3\|_p^p),
\tag{2.20}
\]
because \(C_2,U_1\in L^\infty_tL^{2p}_x\) from the base pair.  Thus
\[
{d\over dt}\|C_3\|_p^p
\le C_{p,\tau}\bigl(1+\|C_3\|_p^p+\|U_2\|_p^p\bigr).
\tag{2.21}
\]

Adding (2.14) and (2.21),
\[
\boxed{
{d\over dt}\bigl(\|U_2\|_p^p+\|C_3\|_p^p\bigr)+cD_{2,p}^U
\le C_{p,\tau}\bigl(1+\|U_2\|_p^p+\|C_3\|_p^p\bigr).}
\tag{2.22}
\]
This is the exact next exchange requested by A03.  It uses the \(\chi\)-weighted top cutoff integration and the evolution term \(C_1*U_2\) in \(\partial_tC_3\); it does not use ordinary Shi estimates in the collar.

---

## 3. Recovering \(T_2\)

To continue the finite induction one also needs the unweighted next curvature derivative.  The twice-differentiated unweighted equation has top cutoff expansion
\[
\nabla^4a*T
=2\chi C_4*T+\text{terms with }C_j,\ j\le3,
\tag{3.1}
\]
and terms involving \(\nabla^2T=T_2\).  The equation also contains the current signed-Hessian term \(\chi C_2*T_2\), which is handled exactly as (2.13a)--(2.13b) with \(T_2\) in place of \(U_2\); it is not a bounded-coefficient term.  Since the \(U_2,C_3\) stage is known for every finite exponent, the top term is treated by the same integration by parts:
\[
\int |T_2|^{p-2}T_2*\chi C_4*T
=-\int\nabla(|T_2|^{p-2}T_2)*\chi C_3*T
-
\int |T_2|^{p-2}T_2*\chi C_3*T_1+\text{lower}.
\tag{3.2}
\]
The first term is absorbed into \(\int a|\nabla T_2|^2|T_2|^{p-2}\).  The second is controlled by the same Hölder pattern as (2.10), with \(T_1\in L^4\), current \(C_3\in L^p\), and Sobolev on \(\chi|T_2|^{p/2}\).  The remaining weighted current terms use
\[
aT_j=U_j-\sum_{\ell=1}^j (\nabla^\ell a)*T_{j-\ell},
\tag{3.3}
\]
only after expanding so that no division by \(a\) occurs.  Hence
\[
{d\over dt}\|T_2\|_p^p+cD_{T_2,p}
\le C_{p,\tau}(1+\|T_2\|_p^p),
\tag{3.4}
\]
with forcing from already bounded finite-exponent quantities.

---

## 4. General finite induction pattern

For \(k\ge2\), the weighted stage should be organized at proof level as
\[
\partial_tU_k
=\operatorname{div}(a\nabla U_k)
+\chi C_{k+2}*U
+\chi C_{k+1}*U_1
+\chi C_2*U_k
+C_1*C_{k+1}*U
+C_1*C_1*U_k
+\mathcal P_k,
\tag{4.1}
\]
where \(\mathcal P_k\) is a finite sum of products involving only previous current variables \(U_j\) with \(j<k\), cutoff jets \(C_\ell\) with \(\ell\le k\), and already bounded finite-exponent curvature quantities.  Formula (4.1) is still schematic, but it preserves the essential \(\chi\)-weights on \(C_{k+2}\), \(C_{k+1}\), and the current signed-Hessian factor \(C_2*U_k\).  The top diffusion and drift are not separated; they are tested as the divergence operator.
The top cutoff term is integrated once:
\[
\int |U_k|^{p-2}U_k*\chi C_{k+2}*U
\leadsto
\varepsilon D_{k,p}^U
+C(1+\|C_{k+1}\|_p^p+\|U_k\|_p^p)
+oxed{\int \chi |C_{k+1}|\,|U_1|\,|U_k|^{p-1}}.
\tag{4.2}
\]
The boxed term is controlled exactly as (2.10)--(2.13), using \(U_1\in L^4\), current \(C_{k+1}\in L^p\), and Sobolev on \(\chi|U_k|^{p/2}\).  The current signed-Hessian term \(\chi C_2*U_k\) is handled by the same one-step integration by parts as (2.13a)--(2.13b), giving \(\varepsilon D_{k,p}^U+C\|C_1\|_\infty^2\|U_k\|_p^p\).  The \(\chi C_{k+1}*U_1\) term is controlled by the same Hölder--Sobolev pattern as the boxed term.  Terms with lower \(U_j\), \(j<k\), are finite-exponent forcing from previous stages, after choosing Hölder exponents large enough; their constants are per datum.

For the cutoff jet,
\[
\partial_tC_{k+1}
=C_1*U_k+
\sum_{j=1}^{k-1} C_{k+1-j}*U_j+\text{lower},
\tag{4.3}
\]
so
\[
{d\over dt}\|C_{k+1}\|_p^p
\le C_{p,\tau}(1+\|C_{k+1}\|_p^p+\|U_k\|_p^p).
\tag{4.4}
\]
Thus
\[
{d\over dt}(\|U_k\|_p^p+\|C_{k+1}\|_p^p)+cD_{k,p}^U
\le C_{p,k,\tau}(1+\|U_k\|_p^p+\|C_{k+1}\|_p^p).
\tag{4.5}
\]
The unweighted stage for \(T_k\) is then obtained from the expanded equation for \(\nabla^kT\), treating \(\chi C_{k+2}*T\) by the same integration, handling \(\chi C_2*T_k\) as a current signed-Hessian term, and using the just obtained \(C_{k+1}\) plus previous \(T_1\in L^4\):
\[
{d\over dt}\|T_k\|_p^p+cD_{T_k,p}
\le C_{p,k,\tau}(1+\|T_k\|_p^p).
\tag{4.6}
\]
Equations (4.5)--(4.6), iterated only for \(2\le k\le s_0\) (and \(T_k\) only for \(2\le k\le s_0-1\)), supply the finite restart package (1.5).

This induction does not require a sequence-uniform Sobolev constant on the positive-time slab.  It uses the per-datum fixed Sobolev constant of the bilipschitz-equivalent metric \(g(\tau)\), which is allowed in continuation.

---

## 5. Status relative to A03 Step 57/58

- A03 Step 57's \(W^{1,p}\to L^\infty\) bridge correctly gives \(|T|_\infty\) from the base block \(T_0,(U_1,C_2),T_1\).  This is enough to bound the coefficients \(U=aT\) and start the positive-time finite induction.
- It is not enough by itself to give fixed-coordinate restart data.  The fixed-background connection difference \(A\) is still needed for the implication from current-pair estimates to \(H^{s_0}\) metric convergence.
- The first nontrivial collar exchange \(\chi C_4*U\) does not produce an unmanageable counterterm.  The difficult term is (2.8), and it is controlled by the weighted Sobolev estimate (2.11) plus the base \(U_1\in L^4\) information.
- The finite restart threshold in dimension four is explicit: for minimal integer \(s_0=7\), prove current pairs through \((U_7,C_8)\) and unweighted curvature derivatives through \(T_6\), then integrate the fixed-background \(A\) system to obtain the restart topology.

The remaining proof work is to write the general tensor expansion behind (4.1)--(4.6) with all commutators and lower products enumerated at proof level.  The next exchange checked here strongly suggests the collar mechanism survives beyond the base pair, but it is not a complete finite-order proof until that enumeration is written.
