# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 12,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step12_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step12_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop a mathematically precise two-core interaction framework for the established Einstein-defect cell problem. The functional is J(g)=∫|Ric(g)+g|² on a compact region in a complex-hyperbolic four-manifold with an exact CH outer collar. Start from two actual admissible blow-up cores, not formal curvature sources. Derive the correct small-boundary-data reduced action about the CH exterior, including gauge, the order of the Euler equation, the boundary jet variables, the Schur-complement/Dirichlet-to-Neumann form, and the cross term between the two cores. Explain how separation and relative orientation enter, what symmetry could force the orientation-averaged cross term to vanish, and what nonzero calculation would yield a strict improvement over two copies of the certified frozen witness. Distinguish an improvement over a known witness sum from strict nonadditivity relative to unknown infima. Propose one tractable calculation or numerical PDE experiment that could decisively determine the sign while using boundary data extracted from the actual frozen cell. Do not assume ordinary Einstein Dirichlet data suffice for the squared-defect functional.

## Integrated Scientific Memo

# Two-core interaction framework for the Einstein-defect cell problem

Work in the normalization
\[
\operatorname{Ric}(g_0)=-g_0,\qquad
J(g)=\int |\operatorname{Ric}(g)+g|^2\,dV_g ,
\]
where \(g_0=g_{\mathrm{CH}}\). The certified frozen perpendicular cell rescales from the \(\operatorname{Ric}=-6g\) normalization without changing \(J\), and has
\[
J_*=
8\pi^2(0.999116243135324311\ldots).
\]

The rigorous framework below starts from two copies of this actual cell, not from formal curvature charges.

---

## 1. Two actual cores and their interface jets

Choose a cut \(\Sigma=\{x=x_c\}\), \(x_c<X=8\), inside the stored frozen profile and set
\[
K_*=\{x\le x_c\},\qquad T_*=\{x_c\le x\le X\}.
\]
The inner piece \(K_*\) is a smooth ordinary blow-up core. In the common marked collar coordinates define
\[
h_*=g_*-g_0,\qquad
q_*:=j^1_\Sigma h_*
   =\left(h_*|_\Sigma,\nabla_\nu h_*|_\Sigma\right).
\]
Near the outer matching point, the frozen profile agrees with CH through its second \(x\)-jet, so for \(x_c=X-\delta\),
\[
h_*|_\Sigma=O(\delta^3),\qquad
\nabla_\nu h_*|_\Sigma=O(\delta^2).
\]
Thus these are genuinely small data extracted from an actual admissible cell.

Place two copies at \(p_1,p_2\) in a CH region, at separation
\[
d=d_{g_0}(p_1,p_2)>2r_c.
\]
After parallel transport of the markings along the joining geodesic, their boundary data are
\[
q_1=q_*,\qquad q_2=\rho(R)q_*,
\]
where \(R\) is the relative frame orientation and \(\rho(R)\) acts on tensor first jets. Let
\[
\Omega_d=D_{\rm out}\setminus(K_1\cup K_2),
\]
with the metric fixed equal to \(g_0\) on an open outer collar.

If the two complete exact-CH collars are retained independently, the costs add exactly; interaction arises only after cutting into the transition tails or allowing their boundary jets to relax.

---

## 2. Linearization, gauge, and the fourth-order Euler equation

Write
\[
E(g)=\operatorname{Ric}(g)+g,\qquad L:=D_{g_0}E.
\]
Since \(E(g_0)=0\),
\[
J_\Omega(g_0+h)
=\int_\Omega |Lh|^2\,dV_0+O(\|h\|^3),
\]
and
\[
D^2J_{g_0}[h,k]=2\int_\Omega\langle Lh,Lk\rangle\,dV_0.
\]

The exact first variation is
\[
DJ_g[h]
=\int\left(
2\langle E,D_gE[h]\rangle
-2\langle E\circ E,h\rangle
+\frac12|E|^2\operatorname{tr}_g h
\right)dV_g,
\]
so the Euler tensor is
\[
\mathscr G(g)
=2(D_gE)^*E-2E\circ E+\frac12|E|^2g.
\]
Because \(E\) is second order in \(g\), \(\mathscr G(g)=0\) is fourth order. At CH its linearization is
\[
L^*Lh=0.
\]

Diffeomorphism invariance gives
\[
L(\mathcal L_Xg_0)=0.
\]
Choose the Bianchi operator
\[
\beta h=\delta h+\frac12d\,\operatorname{tr}h
\]
and either impose \(\beta h=0\) with boundary marking fixed, or use a gauge-fixed second-order operator
\[
L_B=L+\delta^*\beta.
\]
On the Bianchi slice \(L_Bh=Lh\), and the principal symbol of \(L_B\) is scalar elliptic. The fourth-order problem can be solved as the mixed system
\[
z=L_Bh,\qquad
L_B^*z+\beta^*\lambda=0,\qquad
\beta h=0,
\]
which avoids globally \(C^1\) finite elements.

The boundary data are not ordinary Einstein Dirichlet data. Since the quadratic functional contains two derivatives of \(h\), its natural Dirichlet variables are the full first jet
\[
q=(h^0,h^1)
 =\left(h|_\Sigma,\nabla_\nu h|_\Sigma\right),
\]
or, in geometric normal gauge,
\[
q\simeq(\dot\gamma,\dot K,\xi),
\]
where \(\dot\gamma\) is the induced-metric variation, \(\dot K\) the second-fundamental-form variation, and \(\xi\) records interface marking/embedding data. Analytically,
\[
q\in H^{3/2}(\Sigma;S^2T^*\Omega)
 \oplus H^{1/2}(\Sigma;S^2T^*\Omega),
\]
subject to Bianchi compatibility. The dual tractions have orders three and two.

---

## 3. Exterior Dirichlet-to-Neumann form

For a gauge-reduced jet
\[
q=(q_1,q_2)
\]
on \(\Sigma_1\sqcup\Sigma_2\), let \(H_{\Omega_d}q\) solve
\[
L_B^*L_Bh+\beta^*\lambda=0,\qquad
\beta h=0,
\]
with
\[
j^1_{\Sigma_i}h=q_i,\qquad
j^1_{\Gamma_{\rm out}}h=0.
\]
The zero outer first jet implements an exact CH outer collar.

Green’s formula has the form
\[
\int_{\Omega_d}\langle L_Bh,L_Bk\rangle
=
\int_{\Omega_d}\langle L_B^*L_Bh,k\rangle
+\sum_i\Big[
 \langle T_0h,k|_{\Sigma_i}\rangle
+\langle T_1h,\nabla_\nu k|_{\Sigma_i}\rangle
\Big],
\]
where \(T_0\) and \(T_1\) have orders three and two, including gauge-multiplier terms. Define
\[
\Lambda^{\rm ext}_d q
=\bigl(T_0H_{\Omega_d}q,T_1H_{\Omega_d}q\bigr).
\]
After quotienting gauge and retaining any genuine Jacobi modes explicitly,
\[
\Lambda^{\rm ext}_d=(\Lambda^{\rm ext}_d)^*
\]
and
\[
\int_{\Omega_d}|L_BH_{\Omega_d}q|^2\,dV_0
=\langle q,\Lambda^{\rm ext}_dq\rangle.
\]

In two-port form,
\[
\Lambda^{\rm ext}_d=
\begin{pmatrix}
\Lambda_{11}(d)&\Lambda_{12}(d)\\
\Lambda_{21}(d)&\Lambda_{22}(d)
\end{pmatrix},
\qquad
\Lambda_{21}=\Lambda_{12}^*,
\]
hence
\[
\begin{aligned}
J_{\Omega_d}^{(2)}
={}&\langle q_1,\Lambda_{11}q_1\rangle
+2\langle q_1,\Lambda_{12}q_2\rangle\\
&+\langle q_2,\Lambda_{22}q_2\rangle.
\end{aligned}
\]
The leading two-core interaction is therefore
\[
\boxed{
I(d,R)=
2\left\langle q_*,
\Lambda_{12}(d)\rho(R)q_*
\right\rangle .}
\]
If one uses the half-action \(J/2\), the corresponding cross term is the same formula without the prefactor \(2\).

For a discretized exterior Hessian with boundary variables \(q\) and bulk variables \(z\),
\[
H_{\rm ext}=
\begin{pmatrix}
H_{qq}&H_{qz}\\
H_{zq}&H_{zz}
\end{pmatrix},
\]
the exterior response is the Schur complement
\[
\boxed{
\Lambda^{\rm ext}
=H_{qq}-H_{qz}H_{zz}^{-1}H_{zq}.}
\]
Kernel or Jacobi variables must not be hidden inside \(H_{zz}^{-1}\).

---

## 4. Coupling to actual core response

### 4.1 Fixed frozen interiors

Let
\[
J_{\rm in}=\int_{K_*}|E(g_*)|^2,\qquad
J_{\rm tail}=\int_{T_*}|E(g_*)|^2,
\]
so that
\[
J_*=J_{\rm in}+J_{\rm tail}.
\]
Holding the two inner cores exactly fixed gives
\[
J_{\rm pair}
=2J_{\rm in}
+J_{\rm ext}^{\rm nl}(q_*,\rho(R)q_*).
\]
Thus the exact benchmark comparison is
\[
\boxed{
J_{\rm pair}<2J_*
\iff
J_{\rm ext}^{\rm nl}(q_*,\rho(R)q_*)
<2J_{\rm tail}.}
\]

For small data,
\[
\begin{aligned}
J_{\rm ext}^{\rm nl}
={}&
\langle q_*,\Lambda_{11}q_*\rangle
+2\langle q_*,\Lambda_{12}\rho(R)q_*\rangle\\
&+\langle \rho(R)q_*,
 \Lambda_{22}\rho(R)q_*\rangle
+\mathcal R_3,
\end{aligned}
\]
where, on a fixed smooth domain,
\[
|\mathcal R_3|
\le C\|h\|_{C^{2,\alpha}}\|h\|_{H^2}^2.
\]

A strict certified gain over two frozen witnesses follows from
\[
\boxed{
\Delta_2(d,R;x_c)+|\mathcal R_3|<0,}
\]
where
\[
\begin{aligned}
\Delta_2
={}&
\langle q_*,\Lambda_{11}q_*\rangle
+\langle \rho(R)q_*,
 \Lambda_{22}\rho(R)q_*\rangle\\
&+2\langle q_*,\Lambda_{12}\rho(R)q_*\rangle
-2J_{\rm tail}.
\end{aligned}
\]
Numerically the target is
\[
\frac{J_{\rm pair}}{8\pi^2}
<1.998232486270648622\ldots,
\]
with any exact-collar smoothing increment included consistently.

### 4.2 Relaxed core ports

If a stated finite-dimensional family of actual core deformations is allowed, let \(u_i\) be interior variables and \(q_i\) interface jets. Expanding the half-action \(A=J/2\) about each actual core gives
\[
A_i=A_i^0+
\langle g_u^{(i)},u_i\rangle+
\langle g_q^{(i)},q_i\rangle
+\frac12
\left\langle
\binom{u_i}{q_i},
\begin{pmatrix}
H_{uu}^{(i)}&H_{uq}^{(i)}\\
H_{qu}^{(i)}&H_{qq}^{(i)}
\end{pmatrix}
\binom{u_i}{q_i}
\right\rangle+\cdots .
\]
Eliminating \(u_i\) gives the actual core stiffness and force
\[
C_i=
H_{qq}^{(i)}
-H_{qu}^{(i)}(H_{uu}^{(i)})^{-1}H_{uq}^{(i)},
\]
\[
f_i=
g_q^{(i)}
-H_{qu}^{(i)}(H_{uu}^{(i)})^{-1}g_u^{(i)}.
\]
The total reduced action is
\[
A_{\rm red}
=A_0+\langle f,q\rangle+\frac12\langle q,Mq\rangle
+O(\|q\|^3),
\]
with
\[
M=
\begin{pmatrix}
C_1+\Lambda_{11}&\Lambda_{12}\\
\Lambda_{21}&C_2+\Lambda_{22}
\end{pmatrix}.
\]
Its reduced Euler equation is
\[
Mq=-f+O(\|q\|^2).
\]
Eliminating the second port yields
\[
\bigl(M_{11}-M_{12}M_{22}^{-1}M_{21}\bigr)q_1
=
-f_1+M_{12}M_{22}^{-1}f_2+O(\|q\|^2).
\]

The certified frozen cell must not be treated as an unrestricted stationary point: the fixed-collar cell problem has no smooth unrestricted interior critical point. Any “core Hessian” must therefore refer to a specified deformation family, discretization, or fixed-cut problem.

---

## 5. Separation and relative orientation

Choose marked orthonormal frames at \(p_i\) and compare them by parallel transport along the joining geodesic:
\[
R=F_1^{-1}P_{21}F_2.
\]
CH homogeneity makes the response depend on the placement through \(d\), the joining direction, and \(R\). Equivalently,
\[
I(d,R)=
2\iint_{\Sigma_1\times\Sigma_2}
q_*(x)\,\mathcal K_d(x,y)\,
\rho(R)q_*(y)\,dS_xdS_y,
\]
where \(\mathcal K_d\) is the jet-to-traction kernel for the gauge-fixed operator \(L_B^*L_B\). Its large-\(d\) decay is determined by the tensor indicial spectrum; no decay exponent is established by the supplied sources.

For the perpendicular core, the relevant residual orientation is naturally a phase
\[
\theta\in U(1)
\]
rotating the plane \(\omega^\perp\subset\Lambda^+\). Decompose
\[
q_*=\sum_mq_m,\qquad
\rho(\theta)q_m=e^{im\theta}q_m.
\]
The triaxial pair
\[
\sigma_1^2-\sigma_3^2,\qquad
2\sigma_1\sigma_3
\]
is a typical weight-two channel; scalar and biaxial components are weight zero. Thus the interaction generally has the form
\[
I(d,\theta)
=I_0(d)+2\operatorname{Re}\!\left(
\widehat I_2(d)e^{2i\theta}\right)+\cdots .
\]

For any compact orientation group \(H\),
\[
P_H=\int_H\rho(R)\,dR
\]
is projection onto the invariant boundary-data sector, and
\[
\int_H I(d,R)\,dR
=
2\langle q_*,\Lambda_{12}(d)P_Hq_*\rangle.
\]
Therefore symmetry forces the orientation average to vanish if
\[
\boxed{P_Hq_*=0}
\]
—or, in a traction formulation, if the corresponding actual core traction has no invariant component.

This condition cannot be assumed for the full frozen cell: its weight-zero biaxial/scalar part may survive. In particular, CH symmetry alone does not force the average to vanish. What symmetry does guarantee is that a pure nontrivial representation, such as a pure weight-two port, has zero phase average.

If the average is zero and \(I(d,\theta)\not\equiv0\), continuity implies both signs. In the pure weight-two case,
\[
\widehat I_2(d)
=\frac1{2\pi}\int_0^{2\pi}
I(d,\theta)e^{-2i\theta}\,d\theta,
\]
and the favorable orientation contributes
\[
-2|\widehat I_2(d)|
\]
to the full-\(J\) cross term.

---

## 6. What a nonzero calculation proves

A negative interaction is not by itself enough to compare with the frozen witnesses; the diagonal replacement cost must also be included. The decisive fixed-core quantity is
\[
\boxed{
\Delta(d,R;x_c)=
J_{\rm ext}^{\rm nl}(q_*,\rho(R)q_*)
-2J_{\rm tail}(x_c).}
\]
If \(\Delta<0\), gluing the computed exterior to the two unchanged actual interiors gives an admissible metric with
\[
J_{\rm pair}<2J_*.
\]

At quadratic order, a nonzero orientation Fourier coefficient is useful as follows:

* if the invariant cross component vanishes and
  \(\widehat I_2(d)\neq0\), one can choose an orientation making the leading cross term negative;
* a strict improvement follows once this negative term dominates the two one-port replacement errors and the nonlinear remainder;
* equivalently, compare the full two-port minimum with the sum of the two isolated one-port minima. This subtraction removes ordinary single-tail relaxation and isolates genuine fixed-core interaction.

These statements must be separated from strict nonadditivity of the unknown infima. Let
\[
\mathfrak J_1=\inf\{J:\text{one blow-up exact-CH cell}\},
\qquad
\mathfrak J_2=\inf\{J:\text{two blow-up exact-CH cell}\}.
\]
A constructed metric with
\[
J_{\rm pair}<2J_*
\]
proves only
\[
\mathfrak J_2<2J_*.
\]
Since \(\mathfrak J_1\le J_*\), it does **not** imply
\[
\mathfrak J_2<2\mathfrak J_1.
\]
The latter would require either:

1. applying the interaction construction uniformly to a minimizing sequence for \(\mathfrak J_1\), with nonvanishing limiting port response and controlled remainders; or
2. an independent lower bound on \(\mathfrak J_1\) strong enough to compare with the constructed pair.

Similarly, merely beating \(2J_*\) after independently improving each frozen tail is not evidence of interaction. Genuine fixed-core nonadditivity is measured by
\[
J_{\rm two}^{\rm opt}(d,R)
-J_{\rm one,1}^{\rm opt}
-J_{\rm one,2}^{\rm opt},
\]
whose leading term is the off-diagonal response.

---

## 7. Decisive numerical PDE experiment

The most robust experiment is a direct two-port solve using boundary data from the frozen dyadic cell.

### Step 1: Extract actual data

For several cuts \(x_c=X-\delta\), convert
\[
g_*-g_0
\]
to CH Gaussian normal coordinates. Apply a gauge transformation whose vector field vanishes on the outer collar and solve the radial Bianchi-gauge equation. Record
\[
q_*=
\left(h_*|_\Sigma,\nabla_\nu h_*|_\Sigma\right),
\]
its weight-zero and weight-two components, and the exact frozen tail cost
\[
J_{\rm tail}(x_c).
\]

Cuts close to \(X\) provide the cleanest controlled linear regime; cuts farther inward produce larger signals and test robustness.

### Step 2: Solve the gauge-fixed two-port problem

On a CH domain with two spherical holes, solve
\[
z=L_Bh,\qquad
L_B^*z+\beta^*\lambda=0,\qquad
\beta h=0,
\]
with
\[
j^1_{\Sigma_1}h=q_*,
\qquad
j^1_{\Sigma_2}h=\rho(\theta)q_*,
\qquad
j^1_{\Gamma_{\rm out}}h=0.
\]
A mixed finite-element or spectral-element discretization is preferable because it avoids globally \(C^1\) basis functions.

### Step 3: Isolate the interaction by polarization

Let
\[
Q(q_1,q_2)
=\frac12\min\int_{\Omega_d}|L_Bh|^2\,dV_0.
\]
Then the half-action cross term is
\[
\boxed{
\mathcal I(d,\theta)
=
Q(q_*,\rho(\theta)q_*)
-Q(q_*,0)-Q(0,\rho(\theta)q_*).}
\]
Equivalently,
\[
\mathcal I(d,\theta)
=\frac12\Big[
Q(q_*,\rho(\theta)q_*)
-Q(q_*,-\rho(\theta)q_*)
\Big].
\]
A phase scan extracts the invariant component and
\[
\widehat{\mathcal I}_2(d)
=\frac1{2\pi}\int_0^{2\pi}
\mathcal I(d,\theta)e^{-2i\theta}\,d\theta.
\]
This calculation directly determines whether some orientation makes the leading interaction attractive.

### Step 4: Compare against isolated optimized tails

Compute
\[
Q(q_*,0),\qquad Q(0,q_*),
\]
and compare each with \(J_{\rm tail}/2\). This separates ordinary one-cell tail relaxation from genuine off-diagonal interaction.

The quadratic prediction for the full cost difference is
\[
\Delta_2(d,\theta;x_c)
=
2Q(q_*,\rho(\theta)q_*)-2J_{\rm tail}(x_c).
\]

### Step 5: Nonlinear continuation and certification

Use the linear solution as the initial field for minimizing
\[
\int_{\Omega_d}
\bigl|\operatorname{Ric}(g_0+h)+g_0+h\bigr|^2\,dV.
\]
Glue this exterior to the unchanged frozen interiors. Matching the metric and first normal derivative gives an \(H^2\) metric; smooth exact-collar approximants have convergent \(J\). Freeze the exterior solution in a finite smooth basis and evaluate the full curvature integral with interval arithmetic, paralleling the certified one-core calculation.

The decisive signed output is
\[
\boxed{
\Delta(d,\theta;x_c)
=
J_{\rm ext}^{\rm nl}(q_*,\rho(\theta)q_*)
-2J_{\rm tail}(x_c).}
\]
A validated negative value proves a strict two-core improvement over two copies of the certified witness. A separate polarization comparison against the two isolated optimized exteriors determines whether that improvement is genuinely due to interaction rather than independent tail relaxation.