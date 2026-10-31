# TTCS Independent Branch Record

```json
{
  "step_id": 7,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step6_perpendicular_dual_cost_and_relative_calibration.md",
    "Sessions/S1003A01/workspace/scripts/perp_cartan_verify.py",
    "Sessions/S1003A01/workspace/scripts/perp_ground_state_check.py",
    "Sessions/S1003A01/workspace/proofs/PerpGroundState.lean",
    "Sessions/S1003A01/workspace/data/perp_dual/transition_x001_Jd8.json",
    "Sessions/S1003A01/workspace/data/perp_dual/transition_x001_Pd8.json"
  ]
}
```

## Task

Independently verify and strengthen the exact-CH endpoint theorem for the perpendicular O11 relative-calibration problem. Read the Step-6 derivation, the new exact Cartan checker, Sturm factorization/Lean file, and transition data. Starting from Q_± with p=x(1+x)/4, prove the ground-state representations, derive the sharp Dirichlet-to-Neumann form on a CH interval [rho,1] with terminal value v(1)=0, and determine exactly what quadratic boundary payment the bolt-transition region must supply. Check all factors and signs against equation (4.8). Then assess whether the full nonlinear torsion-free evolution dot a_i=u_i+gamma_i(a_i) naturally supplies that payment, or identify the narrowest still-missing inequality. Do not treat the numerical profiles as proof, and do not replace the signed cubic by its negative part.

## Output

## Scientific verification memo

### 1. Normalization and the sign inherited from (4.8)

The Cartan script is consistent with the orbit normalization  
\(\int \sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2\). Indeed,
\[
\frac{P}{8\pi^2}
=\frac14\int abc\,|\operatorname{Ric}^{\circ}|^2dt
=\int\sum_{i=1}^3\frac{\lambda_i}{4}
\left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt,
\qquad
\lambda_i=\frac{a_ja_k}{a_i}.
\]
The symbolic identities in `perp_cartan_verify.py`,
\[
|\operatorname{Ric}^{\circ}|^2=\sum_i(r_i-v_i)^2,\qquad
\dot C=abc\sum_i r_iv_i,
\]
give precisely this factor \(1/4\). Completing the \(i=1,3\) squares with the opposite sign and using
\[
\Phi=C-u_2^2,\qquad
\dot\Phi=2H_1\dot u_1+2H_3\dot u_3+u_1u_3\dot u_2,
\]
gives
\[
\frac{P}{8\pi^2}-1
=\int\left[
\frac{\lambda_1}{4}\left(\dot u_1+\frac{2H_1}{\lambda_1}\right)^2
+\frac{\lambda_3}{4}\left(\dot u_3+\frac{2H_3}{\lambda_3}\right)^2
+\frac{\lambda_2}{4}\left(\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2}\right)^2
+\frac{2u_1u_2u_3}{\lambda_2}\right]dt .
\]
Thus the cubic in (4.8) has the displayed plus sign.

On the exact CH trajectory,
\[
a=c=\sqrt x,\qquad b=\sqrt{x(1+x)},\qquad
u=(0,3x,0),
\]
and
\[
\lambda_1=\lambda_3=L:=\sqrt{x(1+x)},\qquad
\lambda_2=\sqrt{\frac{x}{1+x}},\qquad
dt=\frac{dx}{2L}.
\]

Let \(\xi=u_1\), \(\zeta=u_3\), keep \(u_2=3x\) at quadratic order, and put
\[
v_+=\xi+\zeta,\qquad v_-=\xi-\zeta.
\]
The quadratic transverse part of (4.8), before integration by parts, is
\[
\int_\rho^1\left\{
\frac12\left[L\xi'+\frac{\xi+\frac32x\zeta}{L}\right]^2
+\frac12\left[L\zeta'+\frac{\zeta+\frac32x\xi}{L}\right]^2
+3\xi\zeta
\right\}dx. \tag{1}
\]
The last term comes from the full signed cubic:
\[
\frac{2u_1u_2u_3}{\lambda_2}\,dt
=3\xi\zeta\,dx
=\frac34(v_+^2-v_-^2)\,dx. \tag{2}
\]
No one-sided truncation of \(u_1u_2u_3\) is involved.

Integrating the mixed derivative terms in (1) gives
\[
\mathcal A_{\mathrm{CH}}^{(2)}
=Q_+[v_+]+Q_-[v_-]
+\left[\beta_+(x)v_+^2+\beta_-(x)v_-^2\right]_\rho^1, \tag{3}
\]
where
\[
p=\frac{x(1+x)}4,\qquad
\beta_\pm(x)=\frac{2\pm3x}{8},
\]
and
\[
Q_\pm[v]=\int_\rho^1\bigl(pv'^2+V_\pm v^2\bigr)\,dx,
\]
with
\[
V_+=\frac{4+18x+15x^2}{16x(1+x)},\qquad
V_-=\frac{4-18x+3x^2}{16x(1+x)}.
\]
This reproduces (5.2)–(5.3), including every factor. If \(v_\pm(1)=0\), then
\[
\mathcal A_{\mathrm{CH}}^{(2)}
=Q_+[v_+]+Q_-[v_-]
-\beta_+(\rho)v_+(\rho)^2-\beta_-(\rho)v_-(\rho)^2. \tag{4}
\]

The last trace terms in (4) are essential. Applying a Dirichlet-to-Neumann estimate to \(Q_\pm\) without also retaining these terms misses one copy of \(\beta_\pm(\rho)v_\pm(\rho)^2\).

---

### 2. Exact ground-state representations

The positive zero modes are
\[
f_+(x)=x\sqrt{1+x},\qquad
f_-(x)=\frac{x}{(1+x)^{5/2}},
\]
and they satisfy
\[
-(pf_\pm')'+V_\pm f_\pm=0.
\]
Moreover,
\[
p\frac{f_\pm'}{f_\pm}=\beta_\pm
=\frac{2\pm3x}{8}. \tag{5}
\]
These are exactly the rational Riccati identities formalized in `PerpGroundState.lean`. The Lean file proves the cleared-denominator algebra for \(x\ne0\) and \(1+x\ne0\); positivity of \(f_\pm\), integration, and the sharp trace minimization remain analytic arguments.

For \(v=f_\pm w\), direct expansion using the Sturm equation gives the pointwise identity
\[
pv'^2+V_\pm v^2
=p f_\pm^2(w')^2
+\frac{d}{dx}\left(\beta_\pm v^2\right).
\]
Hence
\[
\boxed{
Q_\pm[v]
=\int_\rho^1p f_\pm^2
\left(\left(\frac{v}{f_\pm}\right)'\right)^2dx
+\left[\beta_\pm v^2\right]_\rho^1.
} \tag{6}
\]
For \(v(1)=0\) and \(V=v(\rho)\),
\[
Q_\pm[v]
=\int_\rho^1p f_\pm^2
\left(\left(\frac{v}{f_\pm}\right)'\right)^2dx
-\beta_\pm(\rho)V^2. \tag{7}
\]

Define
\[
R_\pm(\rho)=\int_\rho^1\frac{dx}{p(x)f_\pm(x)^2}.
\]
Cauchy–Schwarz gives
\[
\int_\rho^1p f_\pm^2(w')^2dx
\ge
\frac{w(\rho)^2}{R_\pm(\rho)}
=\frac{V^2}{f_\pm(\rho)^2R_\pm(\rho)}.
\]
Equality is attained uniquely by
\[
v_{\pm,*}(x)
=
V\,\frac{f_\pm(x)}{f_\pm(\rho)}
\frac{R_\pm(x)}{R_\pm(\rho)},\qquad
R_\pm(x)=\int_x^1\frac{ds}{p(s)f_\pm(s)^2}. \tag{8}
\]
Therefore the sharp Dirichlet-to-Neumann form is
\[
\boxed{
Q_\pm[v]\ge\kappa_\pm(\rho)V^2,\qquad
\kappa_\pm(\rho)
=\frac{1}{f_\pm(\rho)^2R_\pm(\rho)}-\beta_\pm(\rho).
} \tag{9}
\]
Equivalently, for the extremizer,
\[
\kappa_\pm(\rho)
=-p(\rho)\frac{v_{\pm,*}'(\rho)}{v_{\pm,*}(\rho)}.
\]

---

### 3. Closed formulas for the sharp coefficients

For the minus mode,
\[
\frac1{pf_-^2}=\frac{4(1+x)^4}{x^3},
\]
so
\[
R_-(\rho)
=\frac2{\rho^2}+\frac{16}{\rho}-24\log\rho-16\rho-2\rho^2.
\]
Writing
\[
\Delta_-(\rho)
=1+8\rho-12\rho^2\log\rho-8\rho^3-\rho^4,
\]
one has
\[
f_-(\rho)^2R_-(\rho)
=\frac{2\Delta_-(\rho)}{(1+\rho)^5}.
\]
Thus
\[
\boxed{
\kappa_-(\rho)
=\frac{(1+\rho)^5}{2\Delta_-(\rho)}
-\frac{2-3\rho}{8}.
} \tag{10}
\]

For the plus mode,
\[
\frac1{pf_+^2}=\frac4{x^3(1+x)^2},
\]
and partial fractions give
\[
R_+(\rho)
=
\frac2{\rho^2}-\frac8\rho+8-\frac4{1+\rho}
+12\log\frac{1+\rho}{2\rho}.
\]
Set
\[
\Delta_+(\rho)
=
1-3\rho-2\rho^2+4\rho^3
+6\rho^2(1+\rho)\log\frac{1+\rho}{2\rho}.
\]
Then
\[
f_+(\rho)^2R_+(\rho)=2\Delta_+(\rho),
\]
and
\[
\boxed{
\kappa_+(\rho)
=\frac1{2\Delta_+(\rho)}
-\frac{2+3\rho}{8}.
} \tag{11}
\]

These formulas are valid for \(0<\rho<1\).

---

### 4. Exact quadratic endpoint payment for the transition region

Because (4) already contains the additional trace contribution arising in the diagonalization of (1), the sharp lower form for the actual CH part of (4.8) is
\[
\boxed{
\mathcal A_{\mathrm{CH}}^{(2)}
\ge
d_+(\rho)V_+^2+d_-(\rho)V_-^2,
} \tag{12}
\]
where \(V_\pm=v_\pm(\rho)\) and
\[
d_\pm=\kappa_\pm-\beta_\pm.
\]
Explicitly,
\[
\boxed{
d_+(\rho)
=
\frac1{2\Delta_+(\rho)}
-\frac{2+3\rho}{4},
} \tag{13}
\]
\[
\boxed{
d_-(\rho)
=
\frac{(1+\rho)^5}{2\Delta_-(\rho)}
-\frac{2-3\rho}{4}.
} \tag{14}
\]

Consequently the sharp signed trace payment required from the bolt-to-\(\rho\) piece is
\[
\boxed{
\begin{aligned}
\mathcal A_{\mathrm{tr}}^{(2)}
\ge {}&
\left(\frac{2+3\rho}{4}
-\frac1{2\Delta_+(\rho)}\right)V_+^2\\
&+
\left(\frac{2-3\rho}{4}
-\frac{(1+\rho)^5}{2\Delta_-(\rho)}\right)V_-^2 .
\end{aligned}
} \tag{15}
\]
This is a signed quadratic form; discarding either sign loses the sharp matching with (4.8).

As \(\rho\downarrow0\),
\[
d_+(\rho)=\frac34\rho+O\!\left(\rho^2|\log\rho|\right),
\qquad
d_-(\rho)=-\frac34\rho+O\!\left(\rho^2|\log\rho|\right). \tag{16}
\]
Thus the transition receives a plus-channel credit and must furnish, to leading order,
\[
\frac34\rho\,V_-^2-\frac34\rho\,V_+^2.
\]
At \(\rho=0.1\),
\[
d_+(0.1)\approx0.05274,\qquad
d_-(0.1)\approx-0.03565,
\]
so (15) reads approximately
\[
\mathcal A_{\mathrm{tr}}^{(2)}
\ge-0.05274\,V_+^2+0.03565\,V_-^2.
\]
The equation \(d_-(\rho)=0\) is exactly
\[
2(1+\rho)^5=(2-3\rho)\Delta_-(\rho),
\]
with an interior zero numerically near \(\rho=0.1686\).

A useful interpretation is that two copies of \(\beta_\pm\) occur:

1. one trace term appears when (1) is rewritten as \(Q_++Q_-\);
2. another appears in the ground-state representation of each \(Q_\pm\).

This is why the coefficient relevant to (4.8) is
\[
\frac1{f_\pm(\rho)^2R_\pm(\rho)}-2\beta_\pm(\rho),
\]
not merely \(\kappa_\pm\).

---

### 5. What the torsion-free evolution contributes

The evolution
\[
\dot a_i=u_i+\gamma_i(a)
\]
does produce a natural compatibility relation in the minus channel. Exactly,
\[
\frac d{dt}\log\frac ac
=
\frac{u_1}{a}-\frac{u_3}{c}
+\frac{2(c^2-a^2)}{abc}. \tag{17}
\]
Linearize around CH and put
\[
\theta=\delta\log(a/c),\qquad v_-=\delta u_1-\delta u_3.
\]
Using \(dx/dt=2\sqrt{x(1+x)}\), equation (17) becomes
\[
\theta'
+\frac{2}{x(1+x)}\theta
=
\frac{v_-}{2x\sqrt{1+x}}.
\]
Its integrating factor is \((x/(1+x))^2\), and therefore
\[
\boxed{
\frac d{dx}\left[\left(\frac{x}{1+x}\right)^2\theta\right]
=\frac12 f_-(x)v_-(x).
} \tag{18}
\]
The same \(f_-\) that factors the Sturm operator is thus the adjoint weight selected by the torsion-free evolution.

If the terminal metric variation vanishes, \(\theta(1)=0\), then
\[
\int_\rho^1f_-(x)v_-(x)\,dx
=-2\left(\frac{\rho}{1+\rho}\right)^2\theta(\rho). \tag{19}
\]
In particular, exact CH metric matching at \(x=\rho\) gives the moment relation
\[
\int_\rho^1f_-v_-\,dx=0. \tag{20}
\]

This compatibility adds coercivity, but it does not by itself furnish the trace payment in (15). The sharp form can be written explicitly. Let
\[
k=pf_-^2,\qquad h=f_-^2,\qquad
R(x)=\int_x^1k(s)^{-1}ds,\qquad R_\rho=R(\rho),
\]
\[
H_\rho=\int_\rho^1h(x)R(x)\,dx,
\]
and let \(\phi\) solve
\[
-(k\phi')'=h,\qquad \phi(\rho)=\phi(1)=0,
\]
with
\[
N_\rho=\int_\rho^1h\phi\,dx
=\int_\rho^1k(\phi')^2dx>0.
\]
For prescribed
\[
V=v_-(\rho),\qquad \Theta=\theta(\rho),
\]
the sharp constrained minus-channel value of the CH quadratic action is
\[
\boxed{
d_-(\rho)V^2
+
\frac{\left[
-2\left(\frac{\rho}{1+\rho}\right)^2\Theta
-\dfrac{V H_\rho}{f_-(\rho)R_\rho}
\right]^2}{N_\rho}.
} \tag{21}
\]
The second term is the exact extra square supplied by the evolution compatibility. Since \(\Theta\) can align so that this square vanishes, the evolution equation alone does not imply the required estimate. Scientifically, the remaining object is the joint transition trace inequality
\[
\boxed{
\mathcal A_{\mathrm{tr}}^{(2)}
+d_+(\rho)V_+^2+d_-(\rho)V_-^2
+\frac{\left[
-2\left(\frac{\rho}{1+\rho}\right)^2\Theta
-\dfrac{V_-H_\rho}{f_-(\rho)R_\rho}
\right]^2}{N_\rho}
\ge0,
} \tag{22}
\]
with the regular bolt data and the corresponding longitudinal matching data. Equation (22) isolates the smallest remaining quadratic problem: control of the minus trace jointly with the metric-anisotropy trace \(\Theta\), while retaining the full cubic in the transition action.

At finite amplitude, the analogous statement is a variable-coefficient action inequality for solutions of \(\dot a_i=u_i+\gamma_i(a)\). The evolution is a first-order reconstruction equation: away from the bolt, a smooth choice of \(u_i\) locally determines \(a_i\). It therefore does not impose a pointwise sign on \(u_1u_2u_3\). Any all-amplitude proof must extract the payment from the integrated action and endpoint matching, not from the evolution equation alone.

---

### 6. Agreement with the supplied computations

The transition records support the factor and sign bookkeeping:

- In `transition_x001_Jd8.json`, at \(x_{\rm cut}\approx0.1\),
  \[
  v_-(\rho)=0.1033955126,\qquad
  \beta_-(\rho)=0.2125.
  \]
  Hence
  \[
  -\beta_-(\rho)v_-(\rho)^2
  =-0.00227176,
  \]
  agreeing with the stored value \(-0.0022717593\).

- The same row gives
  \[
  Q_-=0.0041720999,\qquad
  \int p f_-^2\bigl((v_-/f_-)'\bigr)^2dx=0.0064438842,
  \]
  whose difference is again \(-0.00227176\).

- The P-target record gives the analogous agreement at about \(2.5\times10^{-8}\) for the sampled quadrature.

These rows verify the ground-state trace sign and exclude a factor-of-two error in (6). They do not establish (15) or (22): the stored outer profiles use coefficients that differ from exact CH by roughly \(5\%\)–\(10\%\) around cuts such as \(\rho=0.1\), and the files do not record all endpoint variables needed for the joint trace form.

The resulting endpoint theorem is therefore exact and sharp: formulas (6), (9)–(15) completely determine the CH Dirichlet-to-Neumann contribution. The remaining mathematical substance is the bolt-transition inequality (22), or its finite-amplitude variable-coefficient analogue, with the signed cubic retained in full.