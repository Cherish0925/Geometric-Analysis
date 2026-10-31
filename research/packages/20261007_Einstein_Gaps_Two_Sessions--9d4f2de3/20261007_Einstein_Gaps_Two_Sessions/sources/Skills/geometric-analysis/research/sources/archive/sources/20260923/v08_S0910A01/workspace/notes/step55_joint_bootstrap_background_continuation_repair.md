# Step 55: Coupled first-exit bootstrap and fixed-background continuation bridge

Session: S0910A01. Agent3 / Actuator. Phase: Execute.

## 0. Purpose

This note repairs two mathematical interfaces in `step54_first_exit_continuation_derivation.md` without restarting the exact-flow construction or the signed tensor estimates.

The restricted Ishida--LeBrun route uses the exact degenerate flow
\[
\partial_t g=-2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}_g+g,
\tag{0.1}
\]
obtained from A03 Step 56.  The useful Step 54 distinction remains: augmented curvature energies may contain a volume term, while defect energies must stay homogeneous in \(E\).  The repairs here are:

1. The first-exit argument must not assume an evolving unweighted bound \(|E(t)|\le \delta\).  The flow velocity is controlled by \(aE\), so the correct bootstrap variable is
\[
V(t)=\int_0^t\|aE(s)\|_{L^\infty(g(s))}\,ds.
\tag{0.2}
\]
The small critical parameter \(\gamma(t)=\mathcal S(t)H_2(t)^{1/2}\) and the metric distortion variable \(V(t)\) must be closed together.  Sobolev constants are transported by bilipschitz comparison with the initial metric; no preservation of a Ricci lower bound is used.

2. The continuation step must be written with a fixed background connection.  Since \(\nabla^{g(t)}g(t)=0\), one cannot integrate \(\nabla^m(\partial_t g)\) as \(\partial_t(\nabla^m g)\).  Put \(\bar\nabla=\nabla^{g(\tau)}\) on a positive-time slab and set
\[
A(t)=\nabla^{g(t)}-\bar\nabla.
\tag{0.3}
\]
The evolution of \(A\), together with conversion between \(\nabla^{g(t)}\) and \(\bar\nabla\), gives a triangular bridge from current-pair estimates to fixed-background Sobolev restart data.

The terminal local geometry is also localized precisely: curvature control and Rauch comparison provide a controlled metric on the exponential pullback ball in \(T_pM\).  They do not imply a uniform lower volume bound for the image ball in a collapsed base manifold.

---

## 1. Coupled first-exit bootstrap

Fix one selected support and suppress the index \(\alpha\).  Let
\[
T=\operatorname{Rm}+{g\owedge g\over 2(n-1)},\qquad
F_T=(1+|T|^2)^{1/2},\qquad
H(t)=\int\eta^2F_T^2\,d\mu_t.
\tag{1.1}
\]
Let \(\mathcal S(t)\) be a local Sobolev constant on the fixed support set, for the metric \(g(t)\), in the four-dimensional form
\[
\|u\|_{L^4(g(t))}^2\le
\mathcal S(t)\bigl(\|\nabla u\|_{L^2(g(t))}^2+r^{-2}\|u\|_{L^2(g(t))}^2\bigr).
\tag{1.2}
\]
Define
\[
\gamma(t)=\mathcal S(t)H(t)^{1/2},\qquad
\Gamma(t)=\sup_{0\le s\le t}\gamma(s),\qquad
V(t)=\int_0^t\|aE(s)\|_\infty\,ds.
\tag{1.3}
\]
The provisional assumptions on \([0,T]\), with \(T\le \theta r^2\), are
\[
\Gamma(T)\le \gamma_*,\qquad V(T)\le V_*.
\tag{1.4}
\]
Only these two quantities are used to control the energy constants.

### 1.1 Bilipschitz and Sobolev transport from \(V\)

For a tangent vector \(\xi\),
\[
\left|{d\over dt}\log g(t)(\xi,\xi)\right|
\le 2\|aE(t)\|_\infty.
\tag{1.5}
\]
Therefore
\[
e^{-2V(t)}g(0)\le g(t)\le e^{2V(t)}g(0).
\tag{1.6}
\]
If \(L=e^{V(t)}\) is the length bilipschitz factor, then in dimension \(n\)
\[
\mathcal S(t)\le L^{2n}\mathcal S(0)=e^{2nV(t)}\mathcal S(0).
\tag{1.7}
\]
Indeed, for \(p=2n/(n-2)\), the left side \(\|u\|_{L^p}^2\) contributes \(L^{n-2}\), the gradient integral contributes at most \(L^{n+2}\), and the lower-order \(L^2\) term contributes at most \(L^n\).  The gradient term is dominant.  In dimension four this gives
\[
\mathcal S(t)\le e^{8V(t)}\mathcal S(0).
\tag{1.8}
\]
This replaces the unsupported Ricci-lower-bound discussion in Step 54 §5.2.

### 1.2 Augmented curvature energy under the joint bootstrap

The signed tensor estimates from Steps 34--35 and A03 Step 57 give, under \(\gamma(t)\le\gamma_*\),
\[
H'(t)+cD_2(t)
\le C_H(1+r^{-2})H(t)+C_V\|aE(t)\|_\infty H(t).
\tag{1.9}
\]
A03 Step 57's apparent volume source is local:
\[
C_{0,\alpha}(t)\le C\int\eta^2a\,d\mu_t\le CH(t),
\]
using \(F_T\ge1\) and \(0\le a\le1\).  It is therefore already included in the multiplicative \(C_HH\) term; no copy of the total manifold volume is added on each support.  The cubic potential is absorbed directly by
\[
Y=\int\eta^2aF_T^3
\le C\mathcal S(t)H(t)^{1/2}(D_2+r^{-2}H),
\]
not by any bound involving \(Y(0)\).

The extra \(\|aE\|_\infty H\) term accounts for norm and volume-form variation; it is harmless because it integrates to \(V(t)\).  Hence
\[
H(t)
\le H(0)\exp\{C_H(1+r^{-2})t+C_VV(t)\}.
\tag{1.10}
\]
Combining (1.7) and (1.10), for \(t\le T\le\theta r^2\) and \(r\le1\),
\[
\gamma(t)
\le
\gamma(0)
\exp\{2nV(t)+\tfrac12C_VV(t)+C_H\theta\}
\tag{1.11}
\]
after enlarging \(C_H\), since \((1+r^{-2})\theta r^2\le2\theta\).

Choose \(V_*,\theta>0\) so that
\[
\exp\{(2n+\tfrac12C_V)V_*+C_H\theta\}\le {3\over2}.
\tag{1.12}
\]
If initially \(\gamma(0)\le\gamma_*/2\), then (1.11) improves the first bootstrap bound to
\[
\Gamma(T)\le {3\over4}\gamma_*.
\tag{1.13}
\]
No evolving unweighted estimate for \(E\) appears.

### 1.3 Defect endpoint and improvement of \(V\)

Under the same \(\Gamma\le\gamma_*\) assumption, the \(E\)-homogeneous defect hierarchy gives
\[
\|aE(t)\|_\infty
\le C_E\delta\left({r^2\over t}\right)^{1/3},
\qquad 0<t\le T,
\tag{1.14}
\]
where \(\delta=\|E(0)\|_\infty\).  This estimate is weighted in \(a\) and integrable at zero.  Therefore
\[
V(T)
\le C_E\delta r^{2/3}\int_0^Tt^{-1/3}\,dt
={3\over2}C_E\delta r^{2/3}T^{2/3}.
\tag{1.15}
\]
For \(T\le\theta r^2\),
\[
V(T)
\le {3\over2}C_E\delta\theta^{2/3}r^2.
\tag{1.16}
\]
For the selected fixed scale \(0<r\le1\), the exact sufficient condition is
\[
\delta\le {V_*\over 3C_E\theta^{2/3}r^2}.
\tag{1.17}
\]
One may impose the stronger \(r\)-independent condition \(\delta\le V_*/(3C_E\theta^{2/3})\) when \(r\le1\), but the displayed scaling with \(r^2\) is the sharp output of (1.16).  Under (1.17), the second bootstrap bound improves to \(V(T)\le V_*/2\).  The coupled bootstrap closes by the standard first-time argument applied to the pair \((\Gamma,V)\).

### 1.4 Resulting first-exit outputs

On the interval \([0,\theta r^2]\) produced by the coupled bootstrap, the previously derived Moser estimates may be used in their weighted form:
\[
\|aF_T(t)\|_\infty\le {C\gamma_0\over t},
\qquad
\|aE(t)\|_\infty\le C_E\delta(r^2/t)^{1/3}.
\tag{1.18}
\]
The curvature endpoint on the plateau \(a=1\) at \(t=\theta r^2\) remains
\[
|\operatorname{Rm}|\le K(r,\theta,\gamma_0,n),
\tag{1.19}
\]
and the metric distortion is controlled by \(V(\theta r^2)=O(\delta\theta^{2/3}r^2)\).

---

## 2. Fixed-background continuation bridge

Let \([\tau,T_*)\), \(\tau>0\), be a positive-time slab on a maximal smooth branch of the exact flow.  Fix
\[
\bar g=g(\tau),\qquad \bar\nabla=\nabla^{\bar g},
\qquad A=\nabla^{g(t)}-\bar\nabla.
\tag{2.1}
\]
All estimates in this section are per datum; their constants may depend on \(\tau\), \(T_*\), finitely many already obtained bounds, and fixed background smooth data.  They are not used in the sequence-uniform first-exit constants.

### 2.1 Evolution of the connection difference

For \(h=\partial_tg=-2aE\), the standard variation formula gives
\[
\partial_tA^k{}_{ij}
={1\over2}g^{k\ell}\bigl(\nabla_i h_{j\ell}+\nabla_jh_{i\ell}-\nabla_\ell h_{ij}\bigr).
\tag{2.2}
\]
Thus, schematically,
\[
\partial_tA=g^{-1}*\nabla(aE).
\tag{2.3}
\]
Since \(E\) is a Ricci contraction of \(T=\operatorname{Rm}+G\), and \(\nabla G=0\) for the evolving Levi--Civita connection,
\[
\nabla^{m+1}(aE)
\quad\text{is a contraction of}\quad
U_{m+1}:=\nabla^{m+1}(aT)
\tag{2.4}
\]
plus lower contractions coming from traces and the metric.  In particular, no division by \(a\) is introduced.

### 2.2 Conversion between \(\bar\nabla\) and \(\nabla\)

For any tensor \(Y\),
\[
\bar\nabla Y=\nabla Y+A*Y.
\tag{2.5}
\]
Inductively,
\[
\bar\nabla^m(\nabla W)
=
\nabla^{m+1}W+
\sum (\nabla^{q_1}A)*\cdots*(\nabla^{q_s}A)*\nabla^\ell W,
\tag{2.6}
\]
where \(\ell\le m\) in every product term and every \(A\)-derivative has order at most \(m-1\) (for \(m=0\), no \(A\)-term appears).  Derivatives of \(g^{-1}\) with respect to \(\bar\nabla\) satisfy the same triangular property because
\[
\bar\nabla g=A*g,
\qquad
\bar\nabla^j g=P_j(A,\bar\nabla A,\ldots,\bar\nabla^{j-1}A;g).
\tag{2.7}
\]
Consequently
\[
\bar\nabla^m\bigl(g^{-1}*\nabla(aE)\bigr)
=
 g^{-1}*U_{m+1}
 +P_m\bigl(A,\ldots,\bar\nabla^{m-1}A;
          U_0,\ldots,U_m;g^{-1}\bigr).
\tag{2.8}
\]
The top background derivative \(\bar\nabla^mA\) does not occur on the right side of (2.8).  This is the triangular feature needed for restart.

### 2.3 Per-datum estimate for \(A\)

Taking fixed-background \(L^p(\bar g)\) norms in (2.2)--(2.8), and using bilipschitz equivalence on the positive-time slab,
\[
{d\over dt}\|\bar\nabla^mA\|_{L^p(\bar g)}
\le
C_m\Bigl(
\|U_{m+1}\|_{L^p(g(t))}
+1+P_m(\|\bar\nabla^jA\|_{L^{p_j}(\bar g)},\|U_j\|_{L^{q_j}(g(t))})_{j<m+1}
\Bigr).
\tag{2.9}
\]
Here the exponents are finite and chosen by ordinary Sobolev/Hölder on the smooth fixed background.  If the current-pair hierarchy supplies finite \(L^\infty_tL^q_x\) bounds for \(U_j\) and the corresponding cutoff jets up to order \(m+1\) for every finite \(q\), then induction in \(m\) gives
\[
\sup_{t\in[\tau,T_*)}\|\bar\nabla^mA(t)\|_{L^p(\bar g)}<\infty
\tag{2.10}
\]
for every finite \(p\).

This is an integration statement for the fixed connection difference, not for \(\nabla^m g\) with the moving connection.

### 2.4 Metric and cutoff restart data

The identity \(\nabla g=0\) becomes, after subtracting the fixed background connection,
\[
\bar\nabla g=A*g.
\tag{2.11}
\]
Hence
\[
\bar\nabla^{m+1}g=(\bar\nabla^mA)*g
+P_m(A,\bar\nabla A,\ldots,\bar\nabla^{m-1}A;g).
\tag{2.12}
\]
The bounds (2.10) therefore give fixed-background \(W^{m+1,p}\) bounds for the metric components.  The scalar cutoff is fixed as a function, so its background derivatives \(\bar\nabla^j\chi\) are smooth and time-independent.  The evolving covariant cutoff jets satisfy
\[
\nabla^j\chi=ar\nabla^j\chi
+P_{j-2}(A,\bar\nabla A,\ldots,\bar\nabla^{j-2}A;ar\nabla\chi,\ldots,\bar\nabla^{j-1}\chi)
\quad (j\ge2),
\tag{2.13}
\]
so the same \(A\)-bounds control them when the exact-flow local theorem is restarted at a positive time.

Thus the continuation bridge is:
\[
\text{current-pair finite-order bounds}
\Longrightarrow
A\text{-bounds in a fixed background}
\Longrightarrow
(g(t),\chi)\text{ smooth restart data}.
\tag{2.14}
\]
It proves the missing logical bridge in Step 54 §6.3, provided the current-pair estimates are completed to the required finite order.  It does not assert that \(T_m\) is recovered from \(U_m\) by dividing by \(a\), and it does not identify \(\nabla^m(\partial_tg)\) with \(\partial_t(\nabla^mg)\).

---

## 3. Terminal local geometry on exponential pullbacks

Step 54 §8.1 should be read with the following localization.

At terminal time \(T=\theta r^2\), the weighted endpoint gives bounded curvature on the plateau \(a=1\).  For a center \(p\) whose geodesic buffer remains inside the plateau, define the pulled-back ball
\[
\mathcal B_\rho(p)=\{v\in T_pM: |v|_{g(T)}<\rho\},
\qquad
\tilde g_p=(\exp_p)^*g(T).
\tag{3.1}
\]
For \(\rho\) below the curvature scale, Rauch comparison controls the Jacobian and curvature of \((\mathcal B_\rho(p),\tilde g_p)\).  Therefore the pullback ball is noncollapsed with a uniform lower volume.  If the local forbidden-germ argument is invoked through smooth compactness rather than weak elliptic convergence, one must also use positive-time plateau derivative bounds on a smaller pullback ball; these follow only after the finite restart/continuation estimates are available.

No uniform lower bound for the image ball \(B_{g(T)}(p,\rho)\subset M\) is needed or justified under collapse; the exponential map may fold or identify directions.  The averaged quantity must be interpreted as
\[
A_\rho\Phi(p)=\fint_{\mathcal B_\rho(p)}(\exp_p)^*\Phi\,d\mu_{\tilde g_p}.
\tag{3.2}
\]
The Step 53 Liouville-invariance argument controls
\[
\int_{P^{\rm in}}A_\rho\Phi(p)\,d\mu(p)
\tag{3.3}
\]
through integration over the unit tangent bundle and geodesic flow.  It does not require injectivity of \(\exp_p\) on the base manifold.

---

## 4. What remains after this repair

The restricted IL theorem is closer but still not complete.  The remaining analytic work is now sharply located.

1. The first-exit estimates must be written in the coupled \((\Gamma,V)\) form above.  The curvature and defect Moser iterations must be embedded inside that joint bootstrap, not inside an unsupported evolving \(|E|\le\delta\) assumption.

2. The current-pair hierarchy must be completed to every finite order needed for restart, using evolving covariant derivatives and the signed Hessian-cutoff integration.  The fixed-background bridge in §2 shows how those estimates imply restart data; it does not replace them.

3. Terminal compactness and the local forbidden-germ lower bound should be stated on exponential pullback balls, with proportional-volume averaging supplied by the unit tangent bundle mechanism.

The positive branch, arbitrary four-dimensional topology, all dimensions \(n\ge5\), and Lean formalization remain outside what this restricted analytic module currently proves.
