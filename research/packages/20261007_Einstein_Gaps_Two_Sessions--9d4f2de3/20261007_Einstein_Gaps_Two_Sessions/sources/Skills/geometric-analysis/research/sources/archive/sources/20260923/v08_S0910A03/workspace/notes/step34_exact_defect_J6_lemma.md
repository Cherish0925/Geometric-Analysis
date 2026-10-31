# Step 34: exact regularized defect moment lemma

## 1. Statement needed by the first-exit argument

Let a smooth solution of
\[
\partial_tg=-2aE,\qquad E=\operatorname{Ric}+g,
\qquad a=\chi^2
\]
exist on a provisional interval on which the current Sobolev coefficient and the same-support curvature energy obey
\[
\|u\|_4^2\le\mathcal S
 (\|\nabla u\|_2^2+r^{-2}\|u\|_2^2),
\qquad
\gamma:=\mathcal S\|F\|_{2,U}\le\gamma_0,
\]
where \(F=(1+|\operatorname{Rm}|^2)^{1/2}\), \(U\) is the buffered support, and \(\gamma_0\) is sufficiently small. Let \(\eta=1\) near \(\operatorname{supp}a\), with \(a=da=0\) on \(\operatorname{supp}d\eta\).

For \(m\ge2\), define
\[
\Phi_\varepsilon=(|E|^2+\varepsilon^2)^{1/2},\qquad
J_{m,\varepsilon}=\int\eta^2a^{m-2}\Phi_\varepsilon^m,
\]
\[
X_{m,\varepsilon}=\int\eta^2a^{m-1}
 \Phi_\varepsilon^{m-2}|\nabla E|^2,
\qquad
z_{m,\varepsilon}=\eta a^{(m-1)/2}\Phi_\varepsilon^{m/2}.
\]
The target lemma is
\[
\boxed{
J_{m,\varepsilon}'+c_mX_{m,\varepsilon}
\le C_m(1+r^{-2})J_{m,\varepsilon}
 +C_m\int\eta^2a^{m-1}F\Phi_\varepsilon^m,}
\tag{1.1}
\]
uniformly for \(0<\varepsilon\le1\), modulo a vanishing regularization remainder described below. The last term equals \(\int Fz_{m,\varepsilon}^2\) and satisfies
\[
\int Fz_{m,\varepsilon}^2
\le C_m\gamma(X_{m,\varepsilon}+r^{-2}J_{m,\varepsilon})
 +\mathcal R_{m,\varepsilon}.
\tag{1.2}
\]
For fixed \(m=6\), small \(\gamma_0\) then yields
\[
J_{6,\varepsilon}'\le C(1+r^{-2})J_{6,\varepsilon}+o_\varepsilon(1),
\]
and after \(\varepsilon\downarrow0\),
\[
J_6(t)\le e^{C(1+r^{-2})t}J_6(0).
\tag{1.3}
\]

## 2. Exact defect equation

The exact tensor equation is
\[
\partial_tE_{ij}=a(\Delta_LE_{ij}-2E_{ij})+\mathcal C_a(E)_{ij},
\tag{2.1}
\]
where, with \(\tau=\operatorname{tr}E\),
\[
\begin{aligned}
\mathcal C_a(E)_{ij}={}&(\Delta a)E_{ij}+2a^k\nabla_kE_{ij}+\tau a_{ij}\\
&+\frac12(a_i\tau_j+a_j\tau_i)
-a_i{}^kE_{kj}-a_j{}^kE_{ki}\\
&-a^k(\nabla_iE_{kj}+\nabla_jE_{ki}).
\end{aligned}
\tag{2.2}
\]
Every term contains \(E\), \(\nabla E\), or a trace. Including inverse-metric variation, the squared norm obeys
\[
(\partial_t-a\Delta)|E|^2
=-2a|\nabla E|^2+4aR_{ikjl}E_{ij}E_{kl}
 +2\langle E,\mathcal C_a(E)\rangle.
\tag{2.3}
\]
For an arbitrary scalar test \(q\), the Hessian-\(a\) terms satisfy the exact integrated identity
\[
\begin{aligned}
\int2q\langle E,\mathcal C_a(E)\rangle
=\int\{&-2|E|^2\langle da,dq\rangle
-2\tau E(dq,da)+4E^2(dq,da)\\
&+q[-\tau\langle da,d\tau\rangle+2E(da,d\tau)]\}.
\end{aligned}
\tag{2.4}
\]
This removes all Hessians of \(a\) before estimation.

## 3. Chain rule and full-gradient coercivity

The exact scalar chain rule is
\[
(\partial_t-a\Delta)\Phi_\varepsilon^m
=\frac m2\Phi_\varepsilon^{m-2}
 (\partial_t-a\Delta)|E|^2
-m(m-2)a\Phi_\varepsilon^{m-2}|\nabla\Phi_\varepsilon|^2.
\tag{3.1}
\]
Because
\[
|\nabla\Phi_\varepsilon|\le|\nabla E|,
\]
the second term is favorable. More importantly, the first term in (2.3) gives the full tensor dissipation
\[
-m\int\eta^2a^{m-1}\Phi_\varepsilon^{m-2}|\nabla E|^2
=-mX_{m,\varepsilon}.
\tag{3.2}
\]
This is the coercive term needed for the cutoff-gradient cross terms; scalar Kato dissipation alone would not control rotations of \(E\).

The evolving weight \(a^{m-2}\) is fixed as a scalar function, while the evolving measure obeys
\[
\partial_td\mu=-a\tau\,d\mu.
\tag{3.3}
\]
The measure term is bounded by
\[
\left|\int\eta^2a^{m-1}\tau\Phi_\varepsilon^m\right|
\le C\int\eta^2a^{m-1}F\Phi_\varepsilon^m,
\tag{3.4}
\]
since \(|\tau|\le C|E|\le CF\).

## 4. Diffusion and cutoff terms

Integrating the \(a\Delta\Phi_\varepsilon^m\) term against \(\eta^2a^{m-2}\) produces
\[
-\int\langle d(\eta^2a^{m-1}),d\Phi_\varepsilon^m\rangle.
\tag{4.1}
\]
The \(d\eta\) term vanishes because \(a=0\) on \(\operatorname{supp}d\eta\). The remaining term is bounded by
\[
C_m\int\eta^2a^{m-2}|da|\Phi_\varepsilon^{m-1}|\nabla E|
\le \epsilon X_{m,\varepsilon}
+C_{m,\epsilon}\int\eta^2a^{m-3}|da|^2\Phi_\varepsilon^m.
\tag{4.2}
\]
For \(a=\chi^2\),
\[
a^{m-3}|da|^2
=4|d\chi|^2a^{m-2}
\le Cr^{-2}a^{m-2},
\tag{4.3}
\]
so (4.2) is at most
\[
\epsilon X_{m,\varepsilon}+C_{m,\epsilon}r^{-2}J_{m,\varepsilon}.
\tag{4.4}
\]

To use (2.4), take the nonlinear scalar test
\[
q_\varepsilon=\frac m2\eta^2a^{m-2}\Phi_\varepsilon^{m-2}.
\tag{4.5}
\]
Identity (2.4), initially proved for a fixed smooth scalar, applies at each time to this smooth spatial test. Its derivative has three pieces. The \(d\eta\) piece again vanishes when paired with \(da\). The derivative of \(a^{m-2}\) gives exactly (4.3). The derivative of \(\Phi_\varepsilon^{m-2}\) is bounded by
\[
C_m\eta^2a^{m-2}\Phi_\varepsilon^{m-3}|da|\,|E|\,|\nabla E|,
\]
which is estimated by the same Young inequality and (4.3). The last line of (2.4), which contains \(q_\varepsilon da*d\tau\), has the same structure because \(|d\tau|\le C|\nabla E|\). Hence
\[
\left|\frac m2\int\eta^2a^{m-2}\Phi_\varepsilon^{m-2}
 2\langle E,\mathcal C_a(E)\rangle\right|
\le\epsilon X_{m,\varepsilon}+C_{m,\epsilon}r^{-2}J_{m,\varepsilon}
+\mathcal R^{(a)}_{m,\varepsilon}.
\tag{4.6}
\]
The regularization remainder arises only where factors \(|E|/\Phi_\varepsilon\) fail to equal one; it remains homogeneous in \(E\) and is dominated by the displayed integrable terms. A fully formal proof should write this remainder explicitly before taking \(\varepsilon\to0\).

## 5. Curvature and lower-order reactions

The Lichnerowicz reaction in (2.3) obeys
\[
\left|2m\int\eta^2a^{m-1}\Phi_\varepsilon^{m-2}
 R_{ikjl}E_{ij}E_{kl}\right|
\le C_m\int\eta^2a^{m-1}F\Phi_\varepsilon^m.
\tag{5.1}
\]
All normalization and moving-norm lower-order terms are bounded either by the same potential or by \(C_mJ_{m,\varepsilon}\), since \(F\ge1\). Combining (3.2), (3.4), (4.4), (4.6), and (5.1), and taking \(\epsilon\) small, gives (1.1) up to the explicit regularization remainder.

## 6. Sobolev absorption of the potential

The potential is
\[
P_{m,\varepsilon}
:=\int\eta^2a^{m-1}F\Phi_\varepsilon^m
=\int Fz_{m,\varepsilon}^2.
\tag{6.1}
\]
By Hölder and the same-support Sobolev inequality,
\[
P_{m,\varepsilon}
\le\|F\|_{2,U}\|z_{m,\varepsilon}\|_4^2
\le\gamma\left(\|\nabla z_{m,\varepsilon}\|_2^2
+r^{-2}\|z_{m,\varepsilon}\|_2^2\right).
\tag{6.2}
\]
The gradient decomposes as
\[
\begin{aligned}
|\nabla z_{m,\varepsilon}|^2
\le C_m\{&\eta^2a^{m-1}\Phi_\varepsilon^{m-2}|\nabla E|^2\\
&+\eta^2a^{m-2}|d\chi|^2\Phi_\varepsilon^m
+|d\eta|^2a^{m-1}\Phi_\varepsilon^m\}.
\end{aligned}
\tag{6.3}
\]
The last term vanishes; the middle term is \(Cr^{-2}J_{m,\varepsilon}\). Also \(\|z_{m,\varepsilon}\|_2^2\le J_{m,\varepsilon}\), because \(a\le1\). Thus
\[
P_{m,\varepsilon}
\le C_m\gamma(X_{m,\varepsilon}+r^{-2}J_{m,\varepsilon}).
\tag{6.4}
\]
For \(m=6\), choose the same-support radius so that \(C_6\gamma<c_6/2\). Equations (1.1) and (6.4) yield (1.3), after the regularization limit is justified.

## 7. What is now derived and what remains

The tensor equation, Hessian-\(a\) integrated identity, weight identity \(|da|^2/a=4|d\chi|^2\), full-gradient coercivity, and Sobolev absorption together give a term-level derivation of the desired \(J_6\) mechanism. It avoids any use of the nonintegrable pointwise curvature coefficient \(\|aF(t)\|_\infty\sim t^{-1}\).

Two points still require a final constructor-level treatment before this can be cited as a proved lemma:

1. write the \(\varepsilon\)-dependent remainder in (4.6) explicitly and prove uniform domination/convergence, rather than only describing its homogeneity;
2. align \(\|F\|_{2,U}\), the Sobolev domain, \(\eta\), and the stationary collar exactly with the macro-support construction, including the provisional moving-metric comparison factors.

No coefficient regularization \(a\mapsto a+\varepsilon\) is used here; \(\varepsilon\) regularizes only the norm \(|E|\).
