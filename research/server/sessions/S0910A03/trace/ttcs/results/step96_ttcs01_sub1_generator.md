# TTCS Independent Branch Record

```json
{
  "step_id": 96,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step94_charge_sign_correction_and_global_flux.md",
    "Sessions/S0910A03/workspace/notes/step95_KX_and_bochner_cancellation.md",
    "Sessions/S0910A03/workspace/notes/step92_tubular_collar_equations_seed.md",
    "Sessions/S0910A03/workspace/scripts/step94_charged_koiso_separator.py",
    "Sessions/S0910A03/workspace/data/step96_initial_taylor_invariants.json",
    "Sessions/S0910A03/workspace/data/step96_koiso_einstein_cauchy_evolution_N96_short.json",
    "Sessions/S0910A03/workspace/data/step96_relative_KX_diagnostic.json",
    "Sessions/S0910A02/workspace/notes/step83_near_pinched_construction_and_frontier_reduction.md"
  ]
}
```

## Task

Develop a high-value next mathematical construction from the exact charged Koiso center and the verified horizontal Noether/K_X pairing. The goal is a genuinely two-variable, shared-parameter joint matching formulation that can decide whether local Ricci flexibility extends to two expanded ends. Use the provided exact Cauchy data, quotient equations, and short Taylor/numerical evidence. Propose an explicit gauge-fixed unknown space, boundary data, residual/matching map including all Ricci blocks and two ends, and independent adjoint projections (not rearrangements of the area equation). Seek either a low-cost near-kernel analogous to log-Weyl slow interpolation or a finite projection that cannot vanish. Keep flat radial T3 models excluded; do not assume transition length or an interface. Derive as much of the linearized principal operator and dimension/index structure as possible, and specify a decisive computation/proof that could be done next.

## Output

A strong next construction is a **two-ended elliptic trace-matching problem on the \(T^2\)-quotient**, with the charged Koiso separator used as an exact central Cauchy slice and the two expanded ends treated simultaneously. The key point is that the coordinate charge \(q\) is a zero-indicial variable at an expanded OT end: \(Q=\frac12e^{-3\sigma}q^TM^{-1}q\) is order \(e^{-6r}\) when \(\sigma\sim2r\). Thus a nonzero central charge can be redshifted to an almost invisible end variable unless the horizontal Noether/\(K_X\) pairings supply a finite adjoint moment.

## 1. Gauge-fixed quotient unknowns

Work on a two-ended cylinder
\[
\Omega\simeq \mathbb R_\tau\times S^1_s
\]
with fixed \(T^2\)-marking. Put the quotient metric in conformal gauge
\[
\gamma=e^{2\varphi}(d\tau^2+ds^2),
\]
and write the fiber metric as
\[
G=e^\sigma M(U),\qquad U=(\alpha,\zeta)\in\mathbb H^2,\qquad \det M=1,
\]
with
\[
M=
\begin{pmatrix}
 e^\alpha+\zeta^2e^{-\alpha}&\zeta e^{-\alpha}\\
 \zeta e^{-\alpha}&e^{-\alpha}
\end{pmatrix}.
\]
The full metric is
\[
g=\gamma+G_{ab}(dx^a+A^a)(dx^b+A^b),
\]
with the vertical connection placed in a fixed Coulomb representative; its curvature is encoded by the two-component twist charge \(q=(q_1,q_2)\). The physically normalized charge potential is
\[
Q=\frac12e^{-3\sigma}q^TM(U)^{-1}q.
\]

The unknown space consists of
\[
(\varphi,\sigma,U,q)
\]
in weighted \(b\)-Hölder or weighted Sobolev classes at the two expanded ends, together with finite end parameters: horizontal circle scale, fiber flat shape \(U_\pm\), fiber area offset, vertical holonomies, and the shared central charge vector \(\mathfrak q\). The ansatz is genuinely two-variable: all Fourier modes in \(s\) are allowed, and the central trace is required to have the nontrivial Koiso target circle \(U_0(s)\), not a radial \(T^3\) model.

The Ricci residual is the full block vector
\[
\mathscr R(\varphi,\sigma,U,q)=(H,T,Z,\mathcal B),
\]
where
\[
\begin{aligned}
H={}&\operatorname{Ric}_\gamma-\operatorname{Hess}\sigma
-\frac12\,d\sigma^2-\frac12\,U^*h_{\mathbb H^2}
-Q\gamma+3\gamma,\\
T={}&L\sigma-6-Q,\\
Z={}&\tau_\sigma(U)+\nabla_UQ,\\
\mathcal B={}&e^{-3\sigma/2}M^{-1/2}dq.
\end{aligned}
\]
The mixed block normalization is exactly the one from
\[
e^{-3\sigma}M^{ab}\langle dq_a,dq_b\rangle_\gamma=4|E_{\rm mix}|^2.
\]
Thus small \(\mathscr R\) is directly comparable to small operator Ricci defect.

In conformal coordinates \(y^i=(\tau,s)\),
\[
T=e^{-2\varphi}\bigl(\Delta_0\sigma+|\nabla_0\sigma|^2\bigr)-6-Q,
\]
and
\[
Z^A=e^{-2\varphi}\bigl(\Delta_0U^A+\Gamma^A_{BC}(U)\partial_iU^B\partial_iU^C
+\partial_i\sigma\,\partial_iU^A\bigr)+h^{AB}\partial_BQ.
\]
Also
\[
\begin{aligned}
H_{ij}={}&-\Delta_0\varphi\,\delta_{ij}
-\bigl(\partial_{ij}\sigma-\partial_i\varphi\,\partial_j\sigma
-\partial_j\varphi\,\partial_i\sigma+\delta_{ij}\partial_k\varphi\,\partial_k\sigma\bigr)\\
&-\frac12\partial_i\sigma\partial_j\sigma
-\frac12h_{AB}(U)\partial_iU^A\partial_jU^B
+(3-Q)e^{2\varphi}\delta_{ij}.
\end{aligned}
\]

## 2. Exact charged Koiso central trace

Use the exact charged Koiso separator as the central slice \(\Sigma=\{\tau=0\}\). Fix \(0<S<3\), a closed hyperbolic target curve \(U_0(s)\) with
\[
|U_0'(s)|^2=12+2S,
\]
and a constant charge vector \(\mathfrak q\) satisfying
\[
Q_0(s)=\frac12\mathfrak q^TM(U_0(s))^{-1}\mathfrak q<S.
\]
Let
\[
P(s)=S-Q_0(s)>0,
\]
and let \(N(s)\) be the target unit normal to \(U_0'(s)\). The central metric trace is
\[
\varphi(0,s)=0,\qquad \sigma(0,s)=0,\qquad U(0,s)=U_0(s),\qquad q(0,s)=\mathfrak q.
\]
The Koiso normal jet is
\[
\varphi_\nu(0,s)=0,\qquad \sigma_\nu(0,s)=0,\qquad
U_\nu(0,s)=\sqrt{2P(s)}\,N(s),
\]
with the sign reversed when the same geometric slice is read from the other side. The vertical Weingarten block is
\[
B=\sqrt{P/2}\,M^{-1}dM(N),
\]
and the mixed block is \(m=-\mathfrak q/2\) up to orientation.

The short Taylor data from Step 96 are valuable because they give the first nontrivial expansion forced by the full equations:
\[
\sigma_{\nu\nu}=6+Q_0(s),
\]
and, in the Fermi form \(\gamma=d\nu^2+a(\nu,s)^2ds^2\),
\[
a_{\nu\nu}=-(3+S+Q_0(s)).
\]
The mean curvature of the \(T^3\) slice satisfies
\[
\mathcal H_\Sigma(0)=0,\qquad \partial_\nu\mathcal H_\Sigma(0)=2.
\]
For the seed \(S=1,\ Q_{\max}=1/2,\ \mathrm{wind}=1\), the numerical Cauchy continuation shows both sides initially expand, coordinate charge remains constant to numerical precision, and \(Q_{\max}\) moves only from \(0.5\) to about \(0.5096\) by \(|\nu|=0.02\). This strongly supports treating the Koiso slice as a genuine two-sided central germ rather than a radial toy model.

## 3. Two expanded end traces

At each end choose a geometric coordinate \(r_\pm\to+\infty\) away from the center. The expanded OT model has
\[
\gamma=dr_\pm^2+\ell_\pm^2e^{2r_\pm}ds^2,\qquad
\sigma=2r_\pm+\sigma_\pm,\qquad
U=U_\pm,\qquad q=0.
\]
Equivalently,
\[
g=dr_\pm^2+e^{2r_\pm}h_{\pm,T^3}
\]
with \(h_{\pm,T^3}\) a flat split \(T^3\)-metric.

There are two closely related trace problems.

### Redshifted exact-charge bridge

Set
\[
q\equiv\mathfrak q
\]
through the whole cylinder and require
\[
\gamma=dr_\pm^2+\ell_\pm^2e^{2r_\pm}ds^2+o(1),\qquad
\sigma=2r_\pm+\sigma_\pm+o(1),\qquad
U=U_\pm+o(1).
\]
Then
\[
Q=\frac12e^{-3\sigma}\mathfrak q^TM(U_\pm)^{-1}\mathfrak q
=O(e^{-6r_\pm}).
\]
Thus a nonzero coordinate charge is asymptotically invisible in the physical Ricci blocks. If this exact fixed-charge bridge exists, an OT end can be produced afterward by tapering \(q\) where \(Q\) is exponentially small.

### OT-taper near-Ricci bridge

Require
\[
q\to0
\]
at both expanded ends, while \(q=\mathfrak q\) at the Koiso center. The function \(q(\tau,s)\) is not prescribed by a chosen transition length; it is part of the unknown. The residual block \(\mathcal B\) records the mixed Ricci cost of its variation, and \(H,T,Z\) record the charge-work cost through \(Q\).

In a hyperbolic end with \(\sigma=2r\),
\[
|\mathcal B|\sim e^{-3r}|\partial_rq|+e^{-4r}|\partial_sq|.
\]
Hence a taper
\[
q_R(r)=\mathfrak q\,\chi\!\left(\frac{r-R}{\ell}\right)
\]
has
\[
\|\mathcal B\|_\infty\le C|\mathfrak q|\,e^{-3R}\ell^{-1},
\qquad
\|Q\|_\infty\le C|\mathfrak q|^2e^{-6R}.
\]
This is the redshift near-kernel. A true obstruction must therefore arise from a finite adjoint projection, not from a pointwise charge estimate.

## 4. Joint matching map

A useful formulation is a two-half Dirichlet-to-Neumann matching, with both halves sharing the same Koiso parameters.

For each side \(\Omega_\pm=[0,\infty)_{r_\pm}\times S^1_s\), solve the reduced elliptic core
\[
T=0,\qquad Z=0,\qquad \operatorname{tr}_\gamma H=0
\]
with the central Dirichlet trace
\[
\varphi=0,\qquad \sigma=0,\qquad U=U_0(s)
\quad\text{at }r_\pm=0,
\]
and with expanded end asymptotics. The output is the normal trace
\[
\mathcal N_\pm=(\partial_{r_\pm}\varphi,\partial_{r_\pm}\sigma,\partial_{r_\pm}U)\big|_{r_\pm=0}.
\]
The Koiso central normal trace is
\[
\mathcal K_\pm=(0,0,\sqrt{2P}N),
\]
with the orientation sign handled by the choice of \(r_\pm\). The central matching component is
\[
\mathcal M_{\rm cen}
=
\bigl(\mathcal N_+-\mathcal K_+,\ \mathcal N_--\mathcal K_-\bigr).
\]

The full residual/matching map is then
\[
\mathfrak M=
\Bigl(
H,T,Z,\mathcal B,\ 
\mathcal M_{\rm cen},\
\mathcal M_{\rm end,+},\
\mathcal M_{\rm end,-},\
\Pi_{\rm TT},\
\Pi_{K_X},\
\Pi_{\rm targ}
\Bigr).
\]
Here \(\mathcal M_{\rm end,\pm}\) records the desired end expansion coefficients: OT exact trace for the taper problem, or redshifted fixed-charge asymptotics for the exact-charge bridge. The map is deliberately not radial and not scalar: \(U(\tau,s)\), \(q(\tau,s)\), and the base conformal factor are coupled everywhere.

## 5. Linearized principal operator and index structure

Freeze a background \((\varphi,\sigma,U,q)\). For variations
\[
(\dot\varphi,\dot\sigma,\dot U,\dot q),
\]
the second-order principal part of the conformal-gauge equations is
\[
D T_2=e^{-2\varphi}\Delta_0\dot\sigma,
\]
\[
D Z_2=e^{-2\varphi}\Delta_0\dot U,
\]
\[
D(\operatorname{tr}_\gamma H)_2
=e^{-2\varphi}\bigl(-2\Delta_0\dot\varphi-\Delta_0\dot\sigma\bigr),
\]
and
\[
D(\mathring H)_2=-(\nabla^2_0\dot\sigma)^\circ.
\]
Thus \((T,Z,\operatorname{tr}H)\) give a square elliptic core for
\[
(\dot\sigma,\dot U,\dot\varphi),
\]
while \(\mathring H\) supplies the holomorphic-quadratic-differential matching. On a two-ended cylinder the bounded weighted trace-free divergence-free quadratic differentials are finite-dimensional; their real length/twist modes pair with conformal modulus and relative \(s\)-phase. These are independent of the area equation.

The charge variation satisfies
\[
\dot Q
=
e^{-3\sigma}q^TM^{-1}\dot q
-3Q\dot\sigma
+\langle\nabla_UQ,\dot U\rangle.
\]
At an OT expanded end \(q=0\), the linear contribution of \(\dot q\) to \(H,T,Z\) vanishes:
\[
D_q(H,T,Z)=0,
\]
and only the first-order mixed block remains:
\[
D_q\mathcal B=e^{-3\sigma/2}M^{-1/2}d\dot q.
\]
This is the precise linear reason the charge taper is a low-cost mode. The adjoint variable dual to \(d q\) must grow like \(e^{3r}\) to see the coordinate charge square; a bounded adjoint sees only the exponentially redshifted physical source.

In a Fourier truncation with modes \(|k|\le K\), the elliptic core has \(4(2K+1)\) scalar radial unknowns and the same number of core scalar equations after the two Bianchi relations are accounted for. The \(\mathring H\) modes add finite conformal matching equations. The charge field contributes \(2(2K+1)\) first-order variables, with two end traces and the shared central value \(\mathfrak q\); the redshift weight destroys any length-independent inverse unless a finite adjoint moment enters through \(H\), \(Z\), or \(K_X\).

## 6. Independent adjoint projections

The useful projections must not be multiples or rearrangements of \(T=L\sigma-6-Q\). Three families are natural.

### A. Weighted TT/Hopf projections

Let \(\Theta\) be trace-free and \(\operatorname{div}_\sigma\Theta=0\) on the quotient cylinder. Define
\[
\Pi_\Theta=\int_\Omega \mathring H:\Theta\,d\mu_\sigma.
\]
The two lowest cylinder modes correspond to conformal length and twist. If one of these pairings tends to a nonzero number along redshift tapers while the adjoint norm stays controlled, the two-ended matching has a finite obstruction. If the adjoint form concentrates at the far taper and its norm grows like \(e^{3R}\), it is part of the redshift near-kernel rather than a finite obstruction.

### B. Horizontal Noether/\(K_X\) projections

For any vector field \(X\) cut off inside the exact end trace, the verified identity gives
\[
\int_\Omega
\Bigl[
2H:\operatorname{sym}\nabla X
-(\operatorname{tr}H)\operatorname{div}_\sigma X
+T\operatorname{div}X
-\langle Z,dU(X)\rangle
\Bigr]d\mu_\sigma
=
\int_\Omega m_q(X)\,d\mu_\sigma,
\]
with
\[
m_q(X)=q^TA\,dq(X),\qquad A=e^{-3\sigma}M^{-1}.
\]
The integration-by-parts form is
\[
\int_\Omega m_q(X)\,d\mu_\sigma
=
-\frac12\int_\Omega q^TK_Xq\,d\mu_\sigma,
\]
where
\[
K_X=X(A)+(\operatorname{div}_\sigma X)A.
\]
Thus
\[
\Pi_X=
\int_\Omega
\Bigl[
2H:\operatorname{sym}\nabla X
-(\operatorname{tr}H)\operatorname{div}_\sigma X
+T\operatorname{div}X
-\langle Z,dU(X)\rangle
\Bigr]d\mu_\sigma
+\frac12\int_\Omega q^TK_Xq\,d\mu_\sigma
\]
vanishes identically for any actual quotient metric residual.

The vector fields worth using are not \(X=\nabla\sigma\), since that collapses back to the area-charge identity in the fixed-charge case. Better choices are:

\[
X_{\rm len}:\ \text{two-ended length modulus field},
\]
\[
X_{\rm tw}:\ \text{relative }s\text{-phase field},
\]
and Fourier-tied fields
\[
X_k \sim \eta_k(s)\partial_\tau,\qquad
\eta_k\in\{1,\cos s,\sin s,\ldots\},
\]
solving a vector adjoint equation with controlled weighted norm. The \(k=\pm1\) modes are essential for the Step 96 wind-one Koiso seed, because \(Q_0(s)\) and \(M(U_0(s))\) are not constant.

The compactly supported \(X\) computation inside the exact Koiso germ already gives zero in the continuum limit. Therefore a meaningful \(K_X\) projection must connect the center to the end redshift region.

### C. Target \(SL(2,\mathbb R)\) current projections

For a Killing field \(Y\) of \(\mathbb H^2\), define the target current flux
\[
\mathcal J_Y(r)=
\int_{S^1} e^\sigma a\,\langle U_r,Y(U)\rangle_h\,ds
\]
in a geometric end coordinate \(\gamma=dr^2+a(r,s)^2ds^2\). The orbit equation gives
\[
\mathcal J_Y(r_2)-\mathcal J_Y(r_1)
=
\int_{r_1<r<r_2}
\bigl(
\langle Z,Y(U)\rangle-\langle\nabla_UQ,Y(U)\rangle
\bigr)d\mu_\sigma.
\]
Using the simultaneous \(SL(2)\)-action on \(M\) and \(q\), the potential term can be rewritten as a charge-rotation term
\[
-\langle\nabla_UQ,Y\rangle=D_qQ(R_Yq),
\]
where \(R_Y\) is the infinitesimal charge representation. These three projections test whether the central target winding and charge orientation can settle to two constant end shapes \(U_\pm\).

## 7. Two mathematical alternatives exposed by this formulation

### Redshift near-kernel route

If the fixed-charge exact bridge
\[
q\equiv\mathfrak q,\qquad H=T=Z=0
\]
exists from the charged Koiso center to two expanded asymptotic ends, then OT collars can be reached with arbitrarily small Ricci defect by tapering \(q\) far out. The quantitative statement is:

If for \(r_\pm\ge R\),
\[
\sigma\ge2r_\pm-C,\qquad
\gamma=dr_\pm^2+e^{2r_\pm}h_\pm+O(e^{-\eta r_\pm}),\qquad
U=U_\pm+O(e^{-\eta r_\pm}),
\]
and if \(q\) is changed from \(\mathfrak q\) to \(0\) over width \(\ell\), then
\[
\|E_{\rm mix}\|_\infty\le C|\mathfrak q|e^{-3R}\ell^{-1},
\]
while the induced \(H,T,Z\) cost is
\[
O(|\mathfrak q|^2e^{-6R}).
\]
This is stronger than a log-Weyl \(1/L\) interpolation: the charge mode is exponentially cheap in the expanded coordinate. Any proof of the fixed-charge redshifted bridge would immediately yield near-Ricci OT metrics by this taper mechanism.

### Finite adjoint obstruction route

If no such bridge exists, the most plausible finite obstruction is a convergent adjoint object in one of the three families above. The horizontal moment most closely related to the radial Step 90 terminal relation is obtained from an \(X\) whose end behavior resembles \(e^{3r}\partial_r\). It pairs with
\[
q^TA\,dq
\]
in exactly the way needed to see a coordinate charge-square change. The decisive question is whether the full two-variable system converts this singular radial adjoint into a bounded weighted adjoint by mixing \(H\), \(Z\), and the TT modes. If yes, the projection cannot vanish for a nonzero Koiso charge. If no, the redshift near-kernel remains available.

The two-component nature of \(q\) and the \(s\)-dependence of \(M(U)\) matter here. Since
\[
m_q(X)=\frac12X(q^TAq)-\frac12q^TX(A)q,
\]
a two-variable taper can rotate \(q\) and vary the orbit shape \(U\) so that the charge-work moment changes sign in ways impossible in scalar radial models. This is exactly why the matching map must retain \(U(\tau,s)\), \(q(\tau,s)\), \(\mathring H\), and the target currents.

## 8. Decisive computation/proof

The sharp low-cost computation is a Chebyshev–Fourier all-at-once solve on the compactified two-ended cylinder, seeded by the Step 96 data
\[
S=1,\qquad Q_{\max}=1/2,\qquad \mathrm{wind}=1.
\]
Use \(y_\pm=e^{-r_\pm}\) at the two ends, factor
\[
\varphi=-\log y_\pm+\log\ell_\pm+\hat\varphi_\pm,\qquad
\sigma=-2\log y_\pm+\sigma_\pm+\hat\sigma_\pm,\qquad
U=U_\pm+\hat U_\pm,
\]
and include all Fourier modes up to \(|k|\le K\).

Two numerical objects would be decisive:

1. **Fixed-charge bridge solve.** Set \(q\equiv\mathfrak q\), solve \(H=T=Z=0\) with the Koiso central Dirichlet trace and expanded end asymptotics, and measure the Koiso Neumann mismatch
   \[
   \mathcal N_\pm-\mathcal K_\pm
   \]
   together with \(\Pi_\Theta\) and \(\Pi_{\rm targ}\). Spectral convergence of the residual and collapse of the mismatch would exhibit the redshifted exact bridge.

2. **Variable-charge singular-pair computation.** Allow \(q\) to vanish at the two ends and equal \(\mathfrak q\) at the center. Compute the smallest singular value
   \[
   \lambda_R=
   \inf_{\dot V}
   \frac{\|D\mathfrak M_R(\dot V)\|}
        {\|\dot q|_{\Sigma}\|}
   \]
   using the full block norm \((H,T,Z,\mathcal B)\) and the projection equations \(\Pi_\Theta,\Pi_X,\Pi_{\rm targ}\). A redshift near-kernel has
   \[
   \lambda_R\sim e^{-3R}
   \]
   and a left singular vector growing like \(e^{3r}\) in the expanded region. A finite obstruction has \(\lambda_R\to\lambda_*>0\) with a bounded adjoint limit and a nonzero \(K_X\), TT, or target-current projection.

This construction directly uses the exact charged Koiso center, the corrected charge-work identity, the Bochner cancellation, and the Step 96 local expansion. It also cleanly separates the two possible outcomes: either the charged local flexibility extends to two expanded ends through the redshift charge mode, or a finite two-variable adjoint projection survives and blocks the simultaneous matching.