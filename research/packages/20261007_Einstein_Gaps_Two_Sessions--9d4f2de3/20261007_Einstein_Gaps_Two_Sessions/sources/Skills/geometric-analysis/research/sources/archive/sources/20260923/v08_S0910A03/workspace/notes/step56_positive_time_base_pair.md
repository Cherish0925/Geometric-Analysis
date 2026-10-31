# Step 56 supplement: the first positive-time continuation block

This note records the earliest nontrivial block needed to turn the weighted endpoint
\(\sup|U|<\infty\) into unweighted smooth restart data near the small-cutoff collar.
It is the exact-flow calculation; the two start regularizations do not occur.

Let
\[
a=\chi^2,\qquad T=\operatorname{Rm}+{g\owedge g\over2(n-1)},\qquad
U=aT,
\qquad \partial_tg=-2\operatorname{Ric}(U).
\]
Work on a fixed slab \([\tau,T_*)\), \(\tau>0\), with
\(\|U\|_\infty\le K\) and bilipschitz-equivalent metrics.  Put
\[
V=\nabla U,\qquad Z=\nabla^2\chi,\qquad X=\nabla T,
\qquad C_j=\nabla^j\chi,
\]
and fix a finite exponent \(p\ge2\).

## 1. The necessary unweighted seed

The bound on \(U=aT\) does not control \(T\) near \(a=0\).  The independent
signed-Hessian estimate of Step 44 gives, for every finite \(q\),
\[
 {d\over dt}\|T\|_q^q
 +c_{n,q}\int a|\nabla T|^2|T|^{q-2}
 \le C_{n,q,K,\|d\chi\|_\infty}
       (\|T\|_q^q+\operatorname{Vol}_{g(t)}M).
\tag{1.1}
\]
Hence \(T\in L^\infty_tL^q_x\) for every finite \(q\).  The proof uses
\(|da|^2\le4a|d\chi|^2\), the identity
\(a|T|^{q+1}=|U||T|^q\), and signed integration of every \(\nabla^2a\)
contraction.  It never divides by \(a\).

## 2. Universal signed-Hessian estimate

For \(Y=V\) or \(Y=X\), every current Hessian contraction has the form
\[
 H_p(Y)=\int\chi(C_2)_{ij}\mathcal B^{ij}(Y),
\quad
 |\mathcal B(Y)|\le C|Y|^p,
\quad
 |\nabla\mathcal B(Y)|\le C|Y|^{p-1}|\nabla Y|.
\]
One integration by parts gives
\[
 |H_p(Y)|\le
 \epsilon\int a|\nabla Y|^2|Y|^{p-2}
 +C_{p,\epsilon}\|d\chi\|_\infty^2\|Y\|_p^p.
\tag{2.1}
\]
Thus no \(L^\infty\) norm of \(C_2\) is used.

## 3. The coupled pair \((V,Z)=(\nabla U,\nabla^2\chi)\)

The complete highest-order types in the once-differentiated \(U\) equation are
\[
a\Delta V,
\quad 2\chi C_1*\nabla V,
\quad \chi C_3*U,
\quad \chi C_2*V,
\quad C_1*C_2*U,
\tag{3.1}
\]
together with current terms having bounded coefficients \(U\) or
\(a\operatorname{Rm}=U-aG\), and finite-exponent forcing involving \(T\).
The apparent \(T_1\) terms in \(\nabla[(da*da)*T]\) must not be separated:
\[
 (da*da)*T=4(C_1*C_1)*U,
\qquad
 \nabla[(da*da)*T]=C_1*C_2*U+C_1*C_1*V.
\tag{3.2}
\]
Similarly,
\[
 a\nabla T=V-da*T,
\tag{3.3}
\]
so no circular input \(X\) is needed.

The top cutoff term is integrated as
\[
\begin{split}
 \int |V|^{p-2}V*\chi C_3*U
 ={}&-\int\nabla(|V|^{p-2}V)*\chi Z*U\\
 &-\int |V|^{p-2}V*C_1*Z*U
 -\int |V|^{p-2}V*\chi Z*V.
\end{split}
\tag{3.4}
\]
The first term is bounded by
\[
 \epsilon D^U_{1,p}+C_{p,K,\epsilon}
 \bigl(\|Z\|_p^p+\|V\|_p^p\bigr),
\quad
 D^U_{1,p}=\int a|\nabla V|^2|V|^{p-2},
\tag{3.5}
\]
the second by same-exponent Young, and the third by (2.1).  The direct
\(\chi C_2V\) term is also (2.1); no current \(Z\in L^{2p}\) is requested.

Coordinate-time connection variation is
\[
 \partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U),
 \qquad |\partial_t\Gamma|\le C|V|.
\tag{3.6}
\]
Because \(\chi\) is a fixed scalar,
\[
 \partial_tZ=-(\partial_t\Gamma)*C_1,
\tag{3.7}
\]
while norm and measure variation have coefficient bounded by \(|U|\).
Consequently
\[
\boxed{
 {d\over dt}\bigl(\|V\|_p^p+\|Z\|_p^p\bigr)
 +cD^U_{1,p}
 \le C_{p,K,\|d\chi\|_\infty}
 \bigl(1+\|T\|_p^p+\|V\|_p^p+\|Z\|_p^p\bigr).}
\tag{3.8}
\]
Together with (1.1), this gives \(V,Z\in L^\infty_tL^p_x\) for every finite
\(p\).

## 4. The subsequent unweighted \(X=\nabla T\) estimate

The only new cutoff jet in the once-differentiated unweighted equation is
\[
 \nabla^3a*T=2\chi C_3*T+C_1*C_2*T.
\tag{4.1}
\]
It is essential to expand first.  Only \(\chi C_3T\) is integrated by parts:
\[
\begin{split}
 \int |X|^{p-2}X*\chi C_3*T
 ={}&-\int C_1*Z*T*|X|^{p-2}X\\
 &-\int\chi Z*X*|X|^{p-2}X
 -\int\chi Z*T*\nabla(|X|^{p-2}X).
\end{split}
\tag{4.2}
\]
The middle term is (2.1).  The last term obeys
\[
 \le\epsilon D^T_{1,p}
 +C_{p,\epsilon}\|Z\|_{2p}^2\|T\|_{2p}^2\|X\|_p^{p-2},
\quad
 D^T_{1,p}=\int a|\nabla X|^2|X|^{p-2}.
\tag{4.3}
\]
Here \(Z,T\) at exponent \(2p\) are legitimate because both preceding stages
have already been completed for every finite exponent.  Other current curvature
coefficients are weighted:
\[
 aT*X=U*X,
 \quad a\operatorname{Rm}*X=(U-aG)*X,
 \quad a\nabla\operatorname{Rm}*T=X*U,
\tag{4.4}
\]
while \([\partial_t,\nabla]T=V*T\) is finite-exponent forcing.  Therefore
\[
\boxed{
 {d\over dt}\|X\|_p^p+cD^T_{1,p}
 \le C_{p,K,\|d\chi\|_\infty}
 \left(1+\|X\|_p^p+
 \|T\|_{2p}^{2p}+\|V\|_{2p}^{2p}+\|Z\|_{2p}^{2p}\right).}
\tag{4.5}
\]
Thus \(X\in L^\infty_tL^p_x\) for every finite \(p\).

## 5. What this establishes

The first collar-sensitive continuation block closes:
\[
 T_0\in\bigcap_{q<\infty}L^q
 \Longrightarrow
 (U_1,C_2)\in\bigcap_{q<\infty}L^q
 \Longrightarrow
 T_1\in\bigcap_{q<\infty}L^q.
\tag{5.1}
\]
No step divides by \(\chi\), assumes unweighted pointwise curvature, or imports
high cutoff jets into the sequence-uniform first-exit constants.  Every derivative
absorbed by degenerate diffusion carries an explicit \(\chi\).  Blindly integrating
all of \(\nabla^3a\) would instead create a bare
\(C_1*C_1*T*\nabla(|X|^{p-2}X)\) term and fail; expansion (4.1) is indispensable.

There is no ratio loss between the start regularizations: this exact positive-time
block contains neither \(\varepsilon\) nor \(\nu\).  If compared to the older
coefficient regularization, only \(\chi^2/b\le1\) and \(|db|^2/b\le4|d\chi|^2\)
are used.

The independent reconstruction is saved at
`trace/ttcs/results/step56_ttcs02_verifier1_integration.md`.  This block does not
by itself prove every higher stage or the first-exit moment inequalities; it
establishes the earliest requested bridge and validates the small-\(a\) collar
mechanism at the first derivative level.