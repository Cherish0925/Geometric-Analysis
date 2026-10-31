# Step 60: All-order continuation without uniqueness, and terminal pullback selection

Session: S0910A03. Agent3 / Actuator. Phase: Execute.

## 0. Purpose and corrected status

This note repairs two interfaces in the restricted four-dimensional negative
Ishida--LeBrun cutoff-flow route.

1. A restart from a smooth time \(t_j<T_*\) cannot be identified with the old
   branch by the previously proposed ungauged \(L^2\) uniqueness estimate.  The
   Ricci principal symbol contains second-order gauge terms.  Instead, the
   arbitrary-order current-pair hierarchy is used to obtain a positive-definite
   smooth terminal metric \(g_*\), and an arbitrary local solution starting at
   \(g_*\) is spliced at \(T_*\).  All one-sided time jets agree because the
   equation is autonomous.  No overlap uniqueness is used.  The uniform
   induction begins at \(m=2\), after the separately established base layer
   \(T_0,(U_1,C_2),T_1\).

2. The terminal argument does not estimate an arbitrary core ball from the
   global density.  It averages exponential-pullback ball means over the same
   buffered set \(P\) that has volume proportional to the topological scale,
   selects one mean-small pullback chart, and passes to a smooth Einstein germ.
   Strong \(W^{2,q}\) convergence yields curvature and density convergence in
   \(L^q/L^1\), not pointwise convergence of the approximants.  The limiting
   nonnegative density is identically zero because its integral is zero and the
   Einstein limit is smooth.

The conclusions below remain conditional on the per-datum exact flow
construction of Step 56 and the previously derived first-exit inequalities.
They concern a restricted four-dimensional negative geography and do not settle
Yau Problem 26.

---

## 1. Exact coordinate-time identities

Let
\[
 a=\chi^2,\qquad
 T=\operatorname{Rm}+G,\qquad
 G=\frac{g\owedge g}{2(n-1)},\qquad
 U=aT,
 \qquad \partial_tg=-2\operatorname{Ric}(U).
\tag{1.1}
\]
Here \(\chi\) is a fixed scalar on \(M\).  Write
\[
 T_m=\nabla^mT,\qquad U_m=\nabla^mU,\qquad C_j=\nabla^j\chi,
 \qquad B_j=\nabla^ja.
\tag{1.2}
\]
Coordinate-time differentiation gives
\[
 \partial_t(\nabla^mA)
 =\nabla^m(\partial_tA)
  +\sum_{r+s=m-1}\nabla^r(\partial_t\Gamma)*\nabla^sA,
 \qquad
 \nabla^r(\partial_t\Gamma)=U_{r+1}*g^{-1},
\tag{1.3}
\]
up to curvature commutators created by reordering covariant derivatives.  The
spatial commutator is
\[
 [\nabla^m,\Delta]A
 =\sum_{r+s=m}\nabla^r\operatorname{Rm}*\nabla^sA.
\tag{1.4}
\]
Reordering \(r\) derivatives in \(\nabla^r\partial_t\Gamma\) produces
terms \(T_q*U_{r-q}\) with \(q\le r-1\); at stage \(m\) these have
\(q\le m-2\), so the unweighted curvature factor is strictly prior-level.

The two base structural equations are
\[
 \partial_tT
 =a\Delta T+B_1*\nabla T+B_2*T+a(T*T+G*T),
\tag{1.5}
\]
\[
 \partial_tU
 =a\Delta U+B_1*\nabla U+B_2*U
 +(B_1*B_1)*T+U*U+aG*U.
\tag{1.6}
\]
They follow from the all-covariant Riemann variation, the second Bianchi
identity, \(\partial_tG\) being algebraic in \(U\), and
\[
 \Delta(aT)=a\Delta T+2B_1*\nabla T+(\Delta a)T,
 \qquad \nabla U=a\nabla T+B_1*T.
\tag{1.7}
\]
The absence of independent \(a\cdot1\) and \(a^2\) terms is forced by the
stationarity test: \(T=U=0\) means \(\operatorname{Ric}=-g\), so the flow is
stationary for every fixed cutoff.  Such terms may occur only as harmless upper
envelopes after estimating \(G*T\) or \(G*U\), never in the tensor equation.
For the exact coefficient, the sole apparently unweighted term in (1.6)
actually obeys the exact identity
\[
 (B_1*B_1)*T=4(C_1*C_1)*U.
\tag{1.8}
\]
This identity is preferable to carrying a fictitious bare \(T\) coefficient.

---

## 2. Universal derivative families

Applying \(\nabla^m\) to (1.5), using (1.3)--(1.4), gives the
following universal contraction families.  In the spatial-commutator family,
\(B_\ell\) records derivatives that first land on the coefficient before the
remaining derivatives are commuted through \(\Delta\):
\[
\begin{array}{lll}
\mathrm{(T1)}&a\Delta T_m,\\
\mathrm{(T2)}&B_r*T_{m+2-r},&1\le r\le m+2,\\
\mathrm{(T3)}&B_r*T_i*T_j,&r+i+j=m,\ B_0=a,\\
\mathrm{(T4)}&B_\ell*\nabla^r\operatorname{Rm}*T_s,
 &\ell+r+s=m,\quad 0\le\ell\le m
 \ \text{(spatial commutators)},\\
\mathrm{(T5)}&U_{r+1}*T_s,&r+s=m-1,\\
 \mathrm{(T6)}&B_r*T_{m-r},&0\le r\le m.
\end{array}
\tag{2.1}
\]
The current objects are exhausted by
\[
\begin{array}{c|l}
T_{m+1}&B_1*T_{m+1}=2\chi C_1*T_{m+1},\\
T_m&B_2*T_m,\ aT_0*T_m,\ a\operatorname{Rm}*T_m,\ aT_m,\\
C_{m+2}&2\chi C_{m+2}*T_0,\\
C_{m+1}&C_1*C_{m+1}*T_0,\ \chi C_{m+1}*T_1,\\
U_m&U_m*T_0.
\end{array}
\tag{2.2}
\]
Here \(aT_0=U_0\) and \(a\operatorname{Rm}=U_0-aG\), so the
coefficients of current \(T_m\) are bounded on a slab where \(U_0\) is
bounded.  The unweighted \(T_0\) in \(U_m*T_0\) is forcing after the
weighted pair at level \(m\) has been completed; the independent zero-order
seed supplies \(T_0\in L^q\) for every finite \(q\).

For the exact flow, first rewrite (1.8), then differentiate.  The full
\(U_m\) families are
\[
\begin{array}{lll}
\mathrm{(U1)}&a\Delta U_m,\\
\mathrm{(U2)}&B_r*U_{m+2-r},&1\le r\le m+2,\\
\mathrm{(U3)}&C_{r+1}*C_{s+1}*U_t,&r+s+t=m,\\
\mathrm{(U4)}&U_i*U_j,&i+j=m,\\
\mathrm{(U5)}&B_\ell*\nabla^r\operatorname{Rm}*U_s,
 &\ell+r+s=m,\quad 0\le\ell\le m
 \ \text{(spatial commutators)},\\
\mathrm{(U6)}&U_{r+1}*U_s,&r+s=m-1,\\
 \mathrm{(U7)}&B_r*U_{m-r},&0\le r\le m.
\end{array}
\tag{2.3}
\]
For (T4)/(U5), the \(\ell=0\) terms are the current weighted
commutators treated below, while every \(\ell\ge1\) term has
\(r+s=m-\ell\le m-1\) and is prior-level forcing.

The two extremal allocations that could otherwise break triangularity are:
\[
 C_1*C_1*U_m,
 \qquad
 C_{m+1}*C_1*U_0,
\tag{2.4}
\]
from (U3), and
\[
 aT_m*U_0
 =\left(U_m-\sum_{q=1}^mB_q*T_{m-q}\right)*U_0
\tag{2.5}
\]
from (U5).  Thus neither family introduces an unweighted current \(T_m\).
All other (U3) factors use \(U_t\) and cutoff jets strictly below the current
pair.

For the fixed scalar cutoff,
\[
 \partial_tC_{m+1}
 =U_m*C_1+\sum_{1\le j<m}U_j*C_{m+1-j}
 +\mathcal R_m,
\tag{2.6}
\]
where every curvature commutator in \(\mathcal R_m\) has strictly lower
curvature and cutoff orders.  There is no \(U_{m+1}\) or \(C_{m+2}\).

Equations (2.1)--(2.6) give the universal finite classification at the
star-contraction level: they arise from the base equations by Leibniz, the
spatial commutator (1.4), the time commutator (1.3), and Ricci reordering.
Tensor slot permutations alter only universal coefficients and contractions,
not the derivative allocations or the presence of \(a,\chi\).  A coordinate
index appendix could further expand every slot permutation, but it would not
introduce a new derivative family; the two independent TTCS reconstructions
found none, and the finite enumeration below tests every integer allocation.

---

## 3. Arbitrary-order energy closure

Work on a positive-time slab \([\tau,T_*)\) with \(\|U\|_\infty\le K\),
bilipschitz metrics, and a finite per-datum Sobolev constant.  Assume
inductively that \(T_j,U_j,C_{j+1}\in L^q\) for every finite \(q\) and
all \(j<m\).

Set
\[
 V=U_m,\qquad Z=C_{m+1},\qquad
 D^U_{m,p}=\int a|\nabla V|^2|V|^{p-2}.
\tag{3.1}
\]
The next derivative \(B_1*U_{m+1}=2\chi C_1*\nabla V\) is absorbed by
\(|B_1|^2/a=4|C_1|^2\).  The current Hessian \(B_2*V\) is retained as a
signed contraction and integrated by parts:
\[
 \left|\int (\nabla_i\nabla_ja)\,\mathcal B^{ij}(V)\right|
 \le\varepsilon D^U_{m,p}
 +C_{p,\varepsilon}\|C_1\|_\infty^2\|V\|_p^p.
\tag{3.2}
\]
The top cutoff term \(2\chi C_{m+2}*U_0\), integrated once, leaves the
residual
\[
 I_m=\int\chi|Z|\,|U_1|\,|V|^{p-1}.
\tag{3.3}
\]
In four dimensions, with \(f=\chi|V|^{p/2}\),
\[
 I_m\le\|f\|_4\|Z\|_p\|U_1\|_4\|V\|_p^{p/2-1},
\tag{3.4}
\]
\[
 \|f\|_4^2
 \le C_S\left(p^2D^U_{m,p}+C_{p,r}\|V\|_p^p\right).
\tag{3.5}
\]
Young therefore gives
\[
 I_m\le\varepsilon D^U_{m,p}
 +C_{m,p,\tau}(1+\|Z\|_p^p+\|V\|_p^p).
\tag{3.6}
\]
The current jet remains at exponent \(p\).  Every remaining monomial is a
bounded coefficient times the current variable, or finitely many prior-level
factors against its \((p-1)\)-st power; assigning those prior factors finite
larger exponents closes it.  Testing (2.6) gives the same-exponent current
coupling \(U_m*C_1\).  Hence
\[
 \boxed{
 \frac d{dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
 +cD^U_{m,p}
 \le C_{m,p,\tau}
  \bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).}
\tag{3.7}
\]

After this pair is known, test (2.1).  The \(B_1*T_{m+1}\) and
\(B_2*T_m\) terms use the same weighted Young and signed-Hessian estimates.
The sole unavailable cutoff jet \(2\chi C_{m+2}*T_0\) is integrated once.
Its descendants contain only \(C_{m+1},T_0,T_1\) and the current gradient;
all are controlled by the completed pair, the independent \(T_0\) seed, and
prior \(T_1\).  Thus
\[
 \boxed{
 \frac d{dt}\|T_m\|_p^p+cD^T_{m,p}
 \le C_{m,p,\tau}(1+\|T_m\|_p^p).}
\tag{3.8}
\]
The base block
\[
 T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
\]
is supplied by the separate positive-time argument in
`step56_positive_time_base_pair.md`.  The estimate (3.3)--(3.6) must not be
used to establish that base block: for \(m=1\), its factor \(U_1\) is the
current variable and the Hölder step would be circular.  Starting at \(m=2\),
the uniform induction proves, for every fixed finite order and every finite
\(p\),
\[
 T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
 \longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots.
\tag{3.9}
\]
After removing the nonexistent constant-forcing families, the finite program
`workspace/scripts/step60_family_enumeration_verify.py` checks all integer
allocations in (2.1)--(2.6), including coefficient-before-commutator and
time-reordering subfamilies, through order 64; its output is
`workspace/data/step60_family_enumeration_verify.json`.  This computation
checks the classification consequences, while the derivation above supplies
the mathematical reason that the universal families are exhaustive.

---

## 4. Why the proposed ungauged uniqueness estimate fails

For \(F(g)=-2a(\operatorname{Ric}_g+g)\), the second-order part of the
linearization is
\[
 DF_g(h)_{ij}
 =a\left(\Delta h_{ij}+\nabla_i\nabla_j\operatorname{tr}h
 -\nabla_i(\operatorname{div}h)_j
 -\nabla_j(\operatorname{div}h)_i\right)+\text{lower terms}.
\tag{4.1}
\]
Thus the \(\nabla^2\operatorname{tr}h\) and
\(\nabla\operatorname{div}h\) terms are principal gauge terms, not lower
order.  At a covector \(\xi\),
\[
 \sigma_\xi(DF)(h)_{ij}
 =a\left(-|\xi|^2h_{ij}-\xi_i\xi_j\operatorname{tr}h
 +\xi_i\xi^kh_{kj}+\xi_j\xi^kh_{ki}\right).
\tag{4.2}
\]
It has the usual gauge kernel \(h=\xi\odot v\), and its quadratic form is
not bounded above by \(-ca|\xi|^2|h|^2+C|h|^2\).  On a flat plateau, take
\(\xi=e_1\) and
\[
 h=\operatorname{diag}(1,-\varepsilon,0,0)e^{ikx^1},
 \qquad 0<\varepsilon<1.
\tag{4.3}
\]
Then \(\sigma_\xi(DF)(h)=\operatorname{diag}(\varepsilon,\varepsilon,0,0)\)
and
\[
 \langle\sigma_\xi(DF)(h),h\rangle
 =\varepsilon-\varepsilon^2>0.
\tag{4.4}
\]
After restoring frequency, the positive contribution grows like \(k^2\).
Consequently the proposed estimate
\[
 \frac d{dt}\int|g_1-g_2|^2\le C\int|g_1-g_2|^2
\tag{4.5}
\]
cannot follow from an ungauged Ricci coercivity calculation.  Restarting from
an earlier \(t_j\) and invoking (4.5) is therefore invalid.

---

## 5. Smooth terminal limit and uniqueness-free splice

The arbitrary-order tower (3.9), justified by the universal-family lemma,
followed by the fixed-background connection conversion, gives for every integer
\(s\)
\[
 \sup_{\tau\le t<T_*}\|g(t)\|_{H^s(\bar g)}<\infty,
 \qquad \bar g=g(\tau).
\tag{5.1}
\]
Indeed, with \(A=\nabla^{g(t)}-\bar\nabla\),
\[
 \bar\nabla^m\partial_tA
 =g^{-1}*U_{m+1}+B_0*A_m
 +P_m(A_{<m},U_{\le m},g^{-1}),
\tag{5.2}
\]
so the completed \(U\)-tower gives all fixed-background derivatives of
\(A\), then all derivatives of \(g\).  Moreover
\[
 \partial_tg=-2\operatorname{Ric}(U).
\tag{5.3}
\]
For every fixed \(s\), the all-order tower supplies sufficiently many
\(U\)- and connection derivatives to obtain
\[
 \sup_{\tau\le t<T_*}\|\partial_tg(t)\|_{H^s(\bar g)}<\infty.
\tag{5.4}
\]
(The required current order grows with \(s\); no single finite level is being
used for every \(s\).)  Therefore \(g(t)\) is Cauchy in every \(H^s\) and
\[
 g(t)\longrightarrow g_*\quad\text{in }C^\infty(M)
 \quad(t\uparrow T_*).
\tag{5.5}
\]
The integrated bound on \(\|aE\|_\infty\) makes \(g_*\) positive definite.

Let
\[
 \mathcal F(g)=-2\chi^2(\operatorname{Ric}_g+g).
\tag{5.6}
\]
Define recursively
\[
 \mathcal F_1=\mathcal F,
 \qquad
 \mathcal F_{\ell+1}(g)=D\mathcal F_\ell(g)[\mathcal F(g)].
\tag{5.7}
\]
Each \(\mathcal F_\ell\) depends on a finite spatial jet of \(g\) and the
fixed \(\chi\).  By (5.5) and the equation,
\[
 \lim_{t\uparrow T_*}\partial_t^\ell g(t)
 =\mathcal F_\ell(g_*)
 \quad\text{in }C^\infty(M),\qquad \ell\ge1.
\tag{5.8}
\]
Apply the per-datum local construction to the smooth positive metric \(g_*\)
and choose any smooth restart \(\widehat g(s)\), \(s\in[0,\epsilon)\), with
\(\widehat g(0)=g_*\).  Since it satisfies the same autonomous equation,
\[
 \partial_s^\ell\widehat g(0)=\mathcal F_\ell(g_*)
 \quad\forall\ell.
\tag{5.9}
\]
Hence
\[
 \widetilde g(t)=
 \begin{cases}
 g(t),&t<T_*,\\
 g_*,&t=T_*,\\
 \widehat g(t-T_*),&t>T_*
 \end{cases}
\tag{5.10}
\]
has matching space-time jets of every order and is a smooth solution across
\(T_*\).  This extends the chosen branch without comparing it with a restart
on an earlier overlap.  No uniqueness statement is required.

Thus, conditional on the Step 56 per-datum local construction and the exact
first-exit inputs, the all-order continuation mechanism excludes a finite
endpoint before the common observation time.  Unlike the former finite-
threshold argument, this conclusion does not import an unproved geometric
uniqueness theorem.

---

## 6. Terminal selection on exponential pullback balls

At terminal time \(T=\theta r^2\), assume the same buffered eligible-center
set \(P_i\) satisfies
\[
 \operatorname{Vol}_{g_i(T)}(P_i)\ge c_0A_i,
 \qquad
 \int_{M_i}\mathfrak D_i\,d\mu_i\le C_0\delta_i^2A_i,
\tag{6.1}
\]
where \(q_{\rm top}\ge0\) and
\[
 \mathfrak D_i=|E_i|^2+(s_i+4)^2
 +(s_i+8\sqrt6|W_i^+|)^2+\mathcal G_i\ge0.
\tag{6.2}
\]
Every radial geodesic of length at most \(\rho\) from \(P_i\) is required to
remain in the plateau on which \(|\operatorname{Rm}|\le K\), with
\[
 \rho\le c\min\{r,K^{-1/2}\}.
\tag{6.3}
\]
For \(p\in P_i\), define
\[
 \mathcal B_\rho(p)=\{v\in T_pM_i:|v|<\rho\},
 \qquad \widetilde g_{i,p}=(\exp_p)^*g_i(T),
\tag{6.4}
\]
and let \(\mathcal A_\rho\mathfrak D_i(p)\) be the mean of the pulled-back
density over this tangent ball.

Radial Jacobi comparison gives
\[
 c_Rt^3\le j_i(p,u,t)\le C_Rt^3,
 \qquad
 c_v\rho^4\le\operatorname{Vol}_{\widetilde g_{i,p}}\mathcal B_\rho(p)
 \le C_v\rho^4.
\tag{6.5}
\]
Let \(\varphi_t\) be geodesic flow on \(SM_i\), with Liouville measure
\(dL\).  Fubini and \(\varphi_t^*dL=dL\) give
\[
\begin{aligned}
 \int_{P_i}\mathcal A_\rho\mathfrak D_i(p)\,d\mu_i(p)
 &\le {C\over\rho^4}\int_0^\rho t^3
  \int_{SP_i}\mathfrak D_i(\pi\varphi_tz)\,dL(z)\,dt\\
 &\le C_L(K,\rho)\int_{M_i}\mathfrak D_i\,d\mu_i.
\end{aligned}
\tag{6.6}
\]
Folding of \(\exp_p\) causes no loss because the integral is over initial
unit tangent vectors and geodesic flow is a diffeomorphism of \(SM_i\).
Equations (6.1) and (6.6) select \(p_i\in P_i\) with
\[
 \mathcal A_\rho\mathfrak D_i(p_i)
 \le {C_LC_0\over c_0}\delta_i^2.
\tag{6.7}
\]
The factor \(A_i\) cancels exactly; no \(A_i^{-1/2}\) loss occurs in this
selection.

---

## 7. Pullback compactness and zero-density Einstein germ

On \((\mathcal B_\rho(p_i),\widetilde g_i)\), curvature is bounded by \(K\).
The clean chart input is center injectivity, not merely total pullback volume:
radial rays in \(T_{p_i}M_i\) do not intersect, while Rauch gives a uniform
conjugate-radius bound.  Hence the center of the pullback ball has a uniform
injectivity radius.  On a fixed smaller ball \(U\Subset\mathcal B_\rho\),
harmonic coordinates give
\[
 \lambda^{-1}\delta\le\widetilde g_i\le\lambda\delta,
 \qquad
 \|\widetilde g_i\|_{C^{1,\alpha}(U)}
 +\|\widetilde g_i\|_{W^{2,q}(U)}\le C_q.
\tag{7.1}
\]
After a subsequence,
\[
 \widetilde g_i\to g_\infty\text{ strongly in }C^{1,\beta}_{\rm loc},
 \qquad
 \widetilde g_i\rightharpoonup g_\infty\text{ weakly in }W^{2,q}_{\rm loc}.
\tag{7.2}
\]
Since \(\mathfrak D_i\ge|E_i|^2\), (6.7) yields
\(E_i\to0\) in \(L^2_{\rm loc}\).  Uniform curvature bounds give uniform
\(L^\infty\) bounds, hence \(E_i\to0\) in every finite \(L^q_{\rm loc}\).
The harmonic-coordinate Ricci equation
\[
 g_i^{ab}\partial_a\partial_b(g_i)_{jk}
 =2(g_i)_{jk}-2(E_i)_{jk}+Q_{jk}(g_i^{-1},\partial g_i)
\tag{7.3}
\]
then implies \(\operatorname{Ric}_{g_\infty}=-g_\infty\) weakly, and the
Einstein elliptic system makes \(g_\infty\) smooth.  Applying interior
elliptic estimates to the difference equation upgrades (7.2) to
\[
 \widetilde g_i\to g_\infty
 \quad\text{strongly in }W^{2,q}_{\rm loc}\quad\forall q<\infty.
\tag{7.4}
\]
This gives strong \(L^q\) curvature convergence, not pointwise curvature
convergence.  Since the minimum eigenvalue of a symmetric endomorphism is
Lipschitz and the curvature is uniformly bounded, every algebraic term in
\(\mathfrak D_i\), including the spectral gap density \(\mathcal G_i\),
converges in \(L^1_{\rm loc}\).  Thus
for every \(U'\Subset U\),
\[
 \int_{U'}\mathfrak D_\infty\,d\mu_{g_\infty}=0.
\tag{7.5}
\]
The limiting density is nonnegative and continuous because \(g_\infty\) is
smooth.  Therefore
\[
 \mathfrak D_\infty\equiv0\quad\text{on }U.
\tag{7.6}
\]
Consequently
\[
 \operatorname{Ric}_{g_\infty}=-g_\infty,
 \quad s_\infty=-4,
 \quad |W_\infty^+|^2=\frac1{24},
 \quad \mathcal G_\infty=0,
 \quad
 \operatorname{Spec}(W_\infty^+)
 =\left(-\frac16,\frac1{12},\frac1{12}\right).
\tag{7.7}
\]
The constant-spectrum projector lemma gives \(\nabla W_\infty^+=0\), whereas
the Einstein--Weyl identity gives \(|\nabla W_\infty^+|^2=1/16\).  This is
the forbidden-germ contradiction.  Hence the controlled pullback-ball means
have a positive lower bound \(\eta(K,\rho)>0\), contradicting (6.7) for
sufficiently small \(\delta_i\).

---

## 8. Correct restricted conclusion and scale of constants

For any specified IL geography of manifolds for which the actual
Ishida--LeBrun hypotheses already exclude every Einstein metric, and satisfying
the full monopole sign-family hypotheses, \(q_{\rm top}\ge0\), the calibrated
volume comparison, and the proportional buffered-center estimate, the
completed conditional chain yields
\[
 \inf_g\left\|g^{-1}(\operatorname{Ric}_g+g)\right\|_{L^\infty,\mathrm{op}}
 \ge\varepsilon_{\mathcal F}>0.
\tag{8.1}
\]
Equivalently, no input metric on a member of this no-Einstein family has Ricci
spectrum contained in
\[
 [-(1+\varepsilon_{\mathcal F}),-(1-\varepsilon_{\mathcal F})].
\tag{8.2}
\]
This is a quantitative gap for candidate input metrics, not the already known
statement that the manifold carries no \(\lambda=-1\) Einstein output metric.
The restriction to IL members satisfying the actual no-Einstein theorem is
essential: their independent gauge-theoretic/topological obstruction supplies
the absence of every Einstein output on the underlying smooth manifold.

The terminal normalization does not force
\(\varepsilon_{\mathcal F}\sim A^{-1/2}\): both
\(\int\mathfrak D\) and \(\operatorname{Vol}(P)\) scale with \(A\), and
(6.7) cancels this scale.  If the geography inputs \(c_0,K,\rho\), calibrated
volume comparison, and first-exit constants are uniform over a chosen family,
then the resulting gap is uniform over that family.  Nothing here establishes
that those inputs depend only on dimension.

Most importantly, (8.1) says that these known no-Einstein manifolds do **not**
admit metrics arbitrarily close to the normalized negative Einstein equation.
It does not construct a metric satisfying a fixed dimension-only two-sided
Ricci interval on a no-Einstein manifold, so it does not disprove Yau Problem
26.  Positive pinching, arbitrary four-dimensional topology, dimensions
\(n\ge5\), and Lean formalization remain open.

## 9. Verification records

- General family and symbol check:
  `workspace/scripts/step60_family_enumeration_verify.py`.
- Machine-readable output:
  `workspace/data/step60_family_enumeration_verify.json`.
- Independent continuation and terminal-chart review:
  `trace/ttcs/results/step60_ttcs01_verifier1_integration.md` and
  `trace/ttcs/results/step60_ttcs01_verifier2_integration.md`.
