# TTCS Independent Branch Record

```json
{
  "step_id": 12,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step7_perpendicular_verification_and_endpoint_map.md",
    "Sessions/S1003A01/workspace/notes/step8_kahler_period_law_and_Rplus_response.md",
    "Sessions/S1003A01/workspace/notes/step11_independent_review_O11_and_mixed_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/mathematics/current/round15_boundary_response.md",
    "Knowledge/objects/papers/1303.0827-Critical-metrics-on-connected-sums-of-Einstein-four-manifolds--711e2a97c44e--5258e72d2de1/object.md"
  ]
}
```

## Task

Develop a mathematically precise two-core interaction framework for the established Einstein-defect cell problem. The functional is J(g)=∫|Ric(g)+g|² on a compact region in a complex-hyperbolic four-manifold with an exact CH outer collar. Start from two actual admissible blow-up cores, not formal curvature sources. Derive the correct small-boundary-data reduced action about the CH exterior, including gauge, the order of the Euler equation, the boundary jet variables, the Schur-complement/Dirichlet-to-Neumann form, and the cross term between the two cores. Explain how separation and relative orientation enter, what symmetry could force the orientation-averaged cross term to vanish, and what nonzero calculation would yield a strict improvement over two copies of the certified frozen witness. Distinguish an improvement over a known witness sum from strict nonadditivity relative to unknown infima. Propose one tractable calculation or numerical PDE experiment that could decisively determine the sign while using boundary data extracted from the actual frozen cell. Do not assume ordinary Einstein Dirichlet data suffice for the squared-defect functional.

## Output

## 1. Geometric set-up from two actual cores

Work after the constant rescaling for which the complex-hyperbolic metric \(g_{\mathrm{CH}}\) satisfies
\[
\operatorname{Ric}(g_{\mathrm{CH}})=-g_{\mathrm{CH}}.
\]
The four-dimensional functional
\[
J(g)=\int |\operatorname{Ric}(g)+g|^2\,dV_g
\]
is unchanged by this rescaling.

Let \(g_{\mathrm w}\) be a smooth exact-CH-collar realization of the certified perpendicular cell. Its limiting frozen value is
\[
\frac{J(g_{\mathrm w})}{8\pi^2}
 =0.999116243135324311\ldots .
\]
Choose a hypersurface \(\Sigma=\{x=x_c\}\) inside the unchanged part of the frozen profile, before the final exact-CH smoothing zone. Write
\[
C^-=\{x\le x_c\},\qquad T=\{x_c\le x\le X\}.
\]
The inner piece \((C^-,g_{\mathrm w})\) is an actual smooth blow-up core. Relative to the CH metric in the same marked collar, it supplies the first metric jet
\[
q_{\mathrm w}
 =j^1_{\Sigma}(g_{\mathrm w}-g_{\mathrm{CH}})
 =\bigl(h|_{\Sigma},\nabla_\nu h|_{\Sigma}\bigr).
\]
Because the frozen profile agrees with CH through its second \(x\)-jet at \(X\),
\[
h|_{x=X-\delta}=O(\delta^3),\qquad
\nabla_\nu h|_{x=X-\delta}=O(\delta^2).
\]
Thus \(x_c\) near \(X\) gives genuinely small interface data extracted from the actual metric.

Place two copies \(C^-_1,C^-_2\) into disjoint CH balls. Their common exterior is
\[
\Omega_{d}
 =D_{\mathrm{out}}\setminus
   \bigl(B_{r_c}(p_1)\cup B_{r_c}(p_2)\bigr),
\]
where \(d=d_{\mathrm{CH}}(p_1,p_2)>2r_c\). The metric is fixed to be CH on an open outer collar. The two inner markings transport the frozen jet to
\[
q_1=q_{\mathrm w},\qquad q_2=\rho(R)q_{\mathrm w},
\]
where \(R\) is the relative frame orientation and \(\rho\) is its action on symmetric-tensor first jets.

If both complete exact-CH collars are retained unchanged, then the two costs add exactly and there is no interaction. An interaction appears only after cutting into the two actual transition tails, or after allowing their collar jets to vary.

---

## 2. Fourth-order Euler equation and gauge

Put
\[
E(g)=\operatorname{Ric}(g)+g,\qquad
\mathcal L_g h=D_gE[h].
\]
For a metric variation \(h\),
\[
D J_g[h]
 =\int\left[
 2\langle E,\mathcal L_g h\rangle
 -2\langle E\circ E,h\rangle
 +\frac12|E|^2\operatorname{tr}_g h
 \right]dV_g,
\]
where \((E\circ E)_{ij}=E_i{}^kE_{kj}\). Hence the Euler tensor is
\[
\mathscr G(g)
 =2\mathcal L_g^*E-2E\circ E+\frac12|E|^2g.
\]
Since \(E\) contains two derivatives of \(g\), the equation
\[
\mathscr G(g)=0
\]
is fourth order.

At \(g_{\mathrm{CH}}\), \(E=0\), and therefore
\[
D^2J_{g_{\mathrm{CH}}}[h,k]
 =2\int_\Omega
   \langle\mathcal L h,\mathcal L k\rangle\,dV,
 \qquad
 \mathcal L=\mathcal L_{g_{\mathrm{CH}}}.
\]
It is convenient to use the half-action
\[
\mathcal A(g)=\frac12J(g),
\]
whose CH quadratic form is
\[
\mathcal Q_\Omega(h)
 =\frac12\int_\Omega|\mathcal L h|^2\,dV.
\]

Diffeomorphism invariance gives
\[
\mathcal L(\mathcal L_Xg_{\mathrm{CH}})
 =\mathcal L_XE(g_{\mathrm{CH}})=0.
\]
Choose the Bianchi operator
\[
\beta h=\delta h+\frac12d\,\operatorname{tr}h
\]
and work in the slice \(\beta h=0\), with diffeomorphisms fixed on the outer collar. Equivalently, introduce
\[
\mathcal L_B=\mathcal L+\delta^*\beta .
\]
Its principal symbol is a scalar multiple of \(|\xi|^2\operatorname{Id}\). On the Bianchi slice, \(\mathcal L_Bh=\mathcal Lh\).

The constrained linear Euler system can be written
\[
\mathcal L^*\mathcal Lh+\beta^*\lambda=0,
\qquad
\beta h=0,
\]
with a one-form multiplier \(\lambda\). After removing gauge fields and any finite-dimensional Jacobi space, this is an elliptic fourth-order system. A mixed representation is
\[
z=\mathcal Lh,\qquad
\mathcal L^*z+\beta^*\lambda=0,\qquad
\beta h=0.
\]

For a second-order Einstein solve one often prescribes only the induced metric variation. That is insufficient here. The natural first jet is
\[
q_i=(h_i^0,h_i^1)
   =\bigl(h|_{\Sigma_i},\nabla_{\nu_i}h|_{\Sigma_i}\bigr).
\]
In geometric normal gauge this is equivalent to
\[
(\dot\gamma_i,\dot K_i,\xi_i),
\]
where \(\dot\gamma_i\) is the induced metric variation, \(\dot K_i\) is the second-fundamental-form variation, and \(\xi_i\) records relative marking and embedding motion. In Sobolev notation,
\[
q_i\in
H^{3/2}(\Sigma_i;S^2T^*\Omega)
\oplus
H^{1/2}(\Sigma_i;S^2T^*\Omega),
\]
subject to the Bianchi compatibility relations. The paired tractions have orders three and two.

---

## 3. CH exterior D-to-N operator

Let \(H_\Omega q\) denote the CH exterior solution with
\[
j^1_{\Sigma_1\sqcup\Sigma_2}h=q=(q_1,q_2),
\qquad
j^1_{\Gamma_{\mathrm{out}}}h=0,
\qquad
\beta h=0.
\]
The zero outer jet represents an exact CH collar; an \(H^2\) clamped solution extends by zero and can be approximated by smooth exact-collar tensors with convergence of the curvature-square action.

Integration by parts gives
\[
\int_\Omega
 \langle\mathcal L_Bh,\mathcal L_Bk\rangle\,dV
 =
\int_\Omega
 \langle\mathcal P_Bh,k\rangle\,dV
 +\sum_{i=1}^2
 \left[
  \langle T_0h,k_i^0\rangle_{\Sigma_i}
 +\langle T_1h,k_i^1\rangle_{\Sigma_i}
 \right],
\]
where
\[
\mathcal P_B=\mathcal L_B^*\mathcal L_B.
\]
Here \(T_0\) has differential order three and \(T_1\) order two; gauge-multiplier contributions are included in these tractions.

Define the D-to-N map
\[
\Lambda^{\mathrm{ext}}q
 =\bigl(T_0H_\Omega q,T_1H_\Omega q\bigr).
\]
It is self-adjoint on the gauge-reduced jet space, and
\[
\mathcal Q_\Omega(H_\Omega q)
 =\frac12\langle q,\Lambda^{\mathrm{ext}}q\rangle.
\]
For two ports,
\[
\Lambda^{\mathrm{ext}}
 =
 \begin{pmatrix}
 \Lambda_{11}&\Lambda_{12}\\
 \Lambda_{21}&\Lambda_{22}
 \end{pmatrix},
 \qquad
 \Lambda_{21}=\Lambda_{12}^*.
\]
Consequently,
\[
\mathcal Q_\Omega
 =
 \frac12\langle q_1,\Lambda_{11}q_1\rangle
 +\langle q_1,\Lambda_{12}q_2\rangle
 +\frac12\langle q_2,\Lambda_{22}q_2\rangle.
\]
The interaction is precisely
\[
\boxed{\mathcal I(d,R)
 =\langle q_{\mathrm w},
   \Lambda_{12}(d)\rho(R)q_{\mathrm w}\rangle.}
\]

A finite-dimensional discretization gives the same operator as a Schur complement. If \(z\) denotes exterior bulk variables and \(q\) the first-jet variables, with quadratic Hessian
\[
\mathbf H_{\mathrm{ext}}
 =
 \begin{pmatrix}
 H_{qq}&H_{qz}\\
 H_{zq}&H_{zz}
 \end{pmatrix},
\]
then
\[
\boxed{
\Lambda^{\mathrm{ext}}
 =H_{qq}-H_{qz}H_{zz}^{-1}H_{zq}.}
\]
Finite Jacobi modes, when present, remain as explicit variables rather than being placed inside \(H_{zz}^{-1}\).

---

## 4. Core response and the coupled Schur equation

There are two useful versions.

### Fixed actual cores

Hold \(C^-_1,C^-_2\) exactly equal to the frozen inner metrics and impose their extracted jets \(q_1,q_2\) on the CH exterior. This produces an explicit geometric competitor and requires no assumption that the frozen cell is stationary.

Let
\[
I_c=\int_{C^-}|\operatorname{Ric}+g|^2\,dV,
\qquad
T_{\mathrm w}=\int_T|\operatorname{Ric}+g|^2\,dV,
\]
so that
\[
J_{\mathrm w}=I_c+T_{\mathrm w}.
\]
The paired construction has
\[
J_{\mathrm{pair}}
 =2I_c+J_{\mathrm{ext}}^{\mathrm{nl}}(q_1,q_2).
\]
Therefore
\[
\boxed{
J_{\mathrm{pair}}<2J_{\mathrm w}
\quad\Longleftrightarrow\quad
J_{\mathrm{ext}}^{\mathrm{nl}}(q_1,q_2)<2T_{\mathrm w}.}
\]

For small jets,
\[
\begin{aligned}
J_{\mathrm{ext}}^{\mathrm{nl}}(q_1,q_2)
={}&
 \langle q_1,\Lambda_{11}q_1\rangle
 +2\langle q_1,\Lambda_{12}q_2\rangle\\
&+\langle q_2,\Lambda_{22}q_2\rangle
 +\mathcal R_3(q_1,q_2),
\end{aligned}
\]
with, on a fixed smooth CH domain,
\[
|\mathcal R_3|
 \le C\|H_\Omega q\|_{C^{2,\alpha}}
       \|H_\Omega q\|_{H^2}^2.
\]

### Relaxed ports

If selected core deformations are also varied, let \(u_i\) be internal variables and \(q_i\) the interface jet. For the exact half-action \(\mathcal A_i=J_i/2\), write the Taylor Hessian as
\[
H_i=
\begin{pmatrix}
H_{uu}^{(i)}&H_{uq}^{(i)}\\
H_{qu}^{(i)}&H_{qq}^{(i)}
\end{pmatrix},
\qquad
g_i=(g_u^{(i)},g_q^{(i)}).
\]
Eliminating \(u_i\) gives
\[
C_i
 =H_{qq}^{(i)}
  -H_{qu}^{(i)}(H_{uu}^{(i)})^{-1}H_{uq}^{(i)},
\]
and the reduced linear force
\[
f_i
 =g_q^{(i)}
  -H_{qu}^{(i)}(H_{uu}^{(i)})^{-1}g_u^{(i)}.
\]
These are computed from the actual core metric. They are not postulated curvature distributions.

The total reduced half-action is
\[
\mathcal A_{\mathrm{red}}
 =\mathcal A_0
  +\langle f_1,q_1\rangle+\langle f_2,q_2\rangle
  +\frac12
   \left\langle
   \binom{q_1}{q_2},
   M
   \binom{q_1}{q_2}
   \right\rangle
  +O(\|q\|^3),
\]
where
\[
M=
\begin{pmatrix}
C_1+\Lambda_{11}&\Lambda_{12}\\
\Lambda_{21}&C_2+\Lambda_{22}
\end{pmatrix}.
\]
The reduced equation is
\[
M\binom{q_1}{q_2}
 =-\binom{f_1}{f_2}+O(\|q\|^2).
\]
Eliminating \(q_2\) yields
\[
\begin{aligned}
\bigl[
M_{11}-M_{12}M_{22}^{-1}M_{21}
\bigr]q_1
={}&-f_1+M_{12}M_{22}^{-1}f_2
 +O(\|q\|^2).
\end{aligned}
\]
This is the exact two-port Schur equation.

For weak coupling \(B=\Lambda_{12}\), let \(M_i\) denote the isolated one-port blocks. The paired minimum differs from the sum of isolated reduced minima by
\[
\mathcal A_{\min}^{(2)}
 -\mathcal A_{\min}^{(1)}-\mathcal A_{\min}^{(1)}
 =
 f_1^*M_1^{-1}B\,M_2^{-1}f_2
 +O(\|B\|^2).
\]
Equivalently, in a traction-driven representation
\[
\frac12\langle q,\Lambda q\rangle-\langle s,q\rangle,
\]
eliminating \(q\) gives
\[
-\frac12\langle s,\Lambda^{-1}s\rangle,
\]
whose two-core term is
\[
-\langle s_1,(\Lambda^{-1})_{12}s_2\rangle.
\]
The traction \(s_i\) is derived from the actual core first variation.

A nontrivial fixed-collar blow-up cell has no smooth unrestricted stationary metric for \(J\). Thus the relaxed core Hessian must refer to a stated finite-dimensional deformation family, a regularized discretization, or a fixed-cut formulation. Treating the frozen profile as an unrestricted critical point would be mathematically inconsistent.

---

## 5. Separation and relative orientation

Choose marked orthonormal frames \(F_i\) at \(p_i\), and use parallel transport along the joining geodesic. The relative orientation is
\[
R=F_1^{-1}P_{21}F_2.
\]
Homogeneity of CH reduces the position dependence to the separation \(d\), the geodesic direction, and this relative frame.

The cross term can be written as a kernel pairing
\[
\mathcal I(d,R)
 =
 \iint_{\Sigma_1\times\Sigma_2}
 q_{\mathrm w}(x)\,
 \mathcal K_d(x,y)\,
 \rho(R)q_{\mathrm w}(y)\,dS_xdS_y,
\]
where \(\mathcal K_d\) is obtained from the CH Poisson kernel for
\(\mathcal L^*\mathcal L\), together with the appropriate jet-to-traction operators. Its decay as \(d\to\infty\) is governed by the tensor resolvent spectrum of the gauge-fixed CH operator; no specific exponent is needed for the framework.

For the perpendicular core, the visible orientation parameter is especially simple. The CH isotropy \(U(2)\) fixes the ambient Kähler form and rotates its orthogonal two-plane in \(\Lambda^+\). A perpendicular Burns orientation therefore carries a phase
\[
\theta\in S^1.
\]
Decompose the port into \(S^1\)-weights,
\[
q_{\mathrm w}=\sum_m q_m,\qquad
\rho(\theta)q_m=e^{im\theta}q_m.
\]
The traceless pair
\[
\sigma_1^2-\sigma_3^2,\qquad 2\sigma_1\sigma_3
\]
is a typical weight-two channel. Scalar and biaxial pieces have weight zero.

For a compact orientation group \(H\),
\[
P_H=\int_H\rho(R)\,dR
\]
is projection onto the invariant subspace, and
\[
\int_H\mathcal I(d,R)\,dR
 =
 \langle q_{\mathrm w},
   \Lambda_{12}(d)P_Hq_{\mathrm w}\rangle.
\]
Hence the orientation average vanishes whenever
\[
P_Hq_{\mathrm w}=0.
\]
The same statement applies to an actual reduced traction \(s_{\mathrm w}\). A pure weight-two port has zero phase average. The full frozen port must first be decomposed, since its weight-zero part can survive averaging.

If the average is zero and \(\mathcal I(d,R)\) is not identically zero, continuity forces values on both sides of zero. In a large-separation multiple-scattering expansion, the first-pass cross term is linear in the inter-core transmission operator, while the diagonal return terms begin quadratically in that operator. A nonzero orientation Fourier coefficient can then select a phase for which the cross term lowers the sum of the isolated reduced costs.

For example,
\[
\widehat{\mathcal I}_2(d)
 =\frac1{2\pi}\int_0^{2\pi}
   \mathcal I(d,\theta)e^{-2i\theta}\,d\theta
\]
is the decisive weight-two number. If
\[
\widehat{\mathcal I}_2(d)\ne0
\]
and the weight-zero contribution vanishes by symmetry, then the favorable phase contributes
\[
-\bigl|\widehat{\mathcal I}_2(d)\bigr|
\]
at leading order.

---

## 6. What must be computed to beat the certified witness sum

For the fixed-cut construction, define
\[
\Delta(d,R;x_c)
 =
J_{\mathrm{ext}}^{\mathrm{nl}}
   (q_{\mathrm w},\rho(R)q_{\mathrm w})
 -2T_{\mathrm w}.
\]
Then
\[
\boxed{\Delta(d,R;x_c)<0}
\]
produces an actual two-core metric with
\[
J_{\mathrm{pair}}<2J_{\mathrm w}.
\]

At quadratic order,
\[
\begin{aligned}
\Delta_2
={}&
 \langle q_{\mathrm w},\Lambda_{11}q_{\mathrm w}\rangle
 +\langle\rho(R)q_{\mathrm w},
        \Lambda_{22}\rho(R)q_{\mathrm w}\rangle\\
&+2\mathcal I(d,R)-2T_{\mathrm w}.
\end{aligned}
\]
A rigorous sufficient inequality is
\[
\Delta_2+
\bigl|\mathcal R_3(q_{\mathrm w},\rho(R)q_{\mathrm w})\bigr|<0.
\]

Using the frozen center as the benchmark, the desired pair value is
\[
\frac{J_{\mathrm{pair}}}{8\pi^2}
 <1.998232486270648622\ldots,
\]
with the selected exact-collar smoothing increment included on both sides.

This comparison is distinct from strict nonadditivity of the unknown optimal costs. If
\[
\mathfrak J_1=\inf J
\quad\text{for one blow-up core},\qquad
\mathfrak J_2=\inf J
\quad\text{for two blow-up cores},
\]
then a metric satisfying
\[
J_{\mathrm{pair}}<2J_{\mathrm w}
\]
establishes
\[
\mathfrak J_2<2J_{\mathrm w}.
\]
Since \(\mathfrak J_1\le J_{\mathrm w}\), this alone does not imply
\[
\mathfrak J_2<2\mathfrak J_1.
\]
The latter would follow from an interaction analysis applied to a sequence approaching \(\mathfrak J_1\), with a uniform nonzero port response and uniform control of the cubic remainder, or from an independent lower estimate for \(\mathfrak J_1\).

---

## 7. A tractable decisive computation

A direct experiment can use the exact frozen coefficients rather than an idealized Burns source.

1. **Extract the port.**  
   Choose several cuts \(x_c=X-\delta\) in the unchanged frozen profile. Convert \(g_{\mathrm w}-g_{\mathrm{CH}}\) to CH Gaussian normal coordinates. Solve the radial Bianchi-gauge ODE with the gauge vector zero on the outer CH collar, and record
   \[
   q_{\mathrm w}
   =\bigl(h|_{\Sigma},\nabla_\nu h|_{\Sigma}\bigr)
   \]
   together with its \(S^1\)-weight decomposition. Compute the exact tail cost \(T_{\mathrm w}(x_c)\).

2. **Solve the two-port quadratic problem.**  
   On a CH ball containing two radius-\(r_c\) holes, minimize
   \[
   \mathcal Q_\Omega(h)
   =\frac12\int_\Omega|\mathcal L h|^2\,dV
   \]
   under
   \[
   \beta h=0,\qquad
   j^1_{\Sigma_1}h=q_{\mathrm w},\qquad
   j^1_{\Sigma_2}h=\rho(\theta)q_{\mathrm w},\qquad
   j^1_{\Gamma_{\mathrm{out}}}h=0.
   \]
   The mixed system
   \[
   z=\mathcal Lh,\qquad
   \mathcal L^*z+\beta^*\lambda=0,\qquad
   \beta h=0
   \]
   permits standard \(C^0\) finite elements or high-order spectral elements without globally \(C^1\) shape functions.

3. **Isolate the cross term by polarization.**  
   Let \(\mathcal Q(q_1,q_2)\) be the minimized half-action. Then
   \[
   \boxed{
   \mathcal I(d,\theta)
   =
   \mathcal Q(q_{\mathrm w},\rho(\theta)q_{\mathrm w})
   -\mathcal Q(q_{\mathrm w},0)
   -\mathcal Q(0,\rho(\theta)q_{\mathrm w}).}
   \]
   Equivalently,
   \[
   \mathcal I
   =\frac12\left[
   \mathcal Q(q_{\mathrm w},\rho(\theta)q_{\mathrm w})
   -
   \mathcal Q(q_{\mathrm w},-\rho(\theta)q_{\mathrm w})
   \right].
   \]
   A phase scan extracts \(\widehat{\mathcal I}_2(d)\) and any invariant component.

4. **Evaluate the actual nonlinear metric.**  
   Use the linear solution as the initial field for minimizing the full exterior functional
   \[
   \frac12\int_\Omega
   |\operatorname{Ric}(g_{\mathrm{CH}}+h)+g_{\mathrm{CH}}+h|^2\,dV.
   \]
   Glue it to the two unchanged frozen interiors. Since the metric and its first normal derivative match, the resulting \(H^2\) metric has smooth approximants with convergent \(J\). Freezing the exterior coefficients into a finite smooth basis then permits interval evaluation of the full curvature integral, just as in the certified one-core computation.

The decisive output is the signed quantity
\[
\Delta(d,\theta;x_c)
 =
J_{\mathrm{ext}}^{\mathrm{nl}}
   (q_{\mathrm w},\rho(\theta)q_{\mathrm w})
 -2T_{\mathrm w}(x_c).
\]
It simultaneously includes the fourth-order exterior response, the correct first metric jet, the gauge and marking data, separation, relative orientation, and the actual frozen-core geometry.