# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 7,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step7_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step7_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify and strengthen the exact-CH endpoint theorem for the perpendicular O11 relative-calibration problem. Read the Step-6 derivation, the new exact Cartan checker, Sturm factorization/Lean file, and transition data. Starting from Q_± with p=x(1+x)/4, prove the ground-state representations, derive the sharp Dirichlet-to-Neumann form on a CH interval [rho,1] with terminal value v(1)=0, and determine exactly what quadratic boundary payment the bolt-transition region must supply. Check all factors and signs against equation (4.8). Then assess whether the full nonlinear torsion-free evolution dot a_i=u_i+gamma_i(a_i) naturally supplies that payment, or identify the narrowest still-missing inequality. Do not treat the numerical profiles as proof, and do not replace the signed cubic by its negative part.

## Integrated Scientific Memo

## Verification memo: exact-CH endpoint theorem for the perpendicular \(O11\) calibration

### 1. Cartan normalization and the sign in (4.8)

The exact Cartan checker supports the identities
\[
|\Ric^\circ|^2=\sum_{i=1}^3(r_i-v_i)^2,\qquad
s=-2\sum_{i=1}^3(r_i+v_i),
\]
where
\[
r_i=\frac{\dot u_i}{a_i},\qquad
v_i=\frac{2H_i}{a_ja_k},\qquad
H_i=u_i+\frac12u_ju_k.
\]
Since \(\int \sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2\),
\[
\frac{P}{8\pi^2}
=\int\sum_i\frac{\lambda_i}{4}
\left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt,
\qquad
\lambda_i=\frac{a_ja_k}{a_i}.
\]
Also
\[
\dot C=abc\sum_i r_iv_i=2\sum_iH_i\dot u_i,
\qquad
C=\sum_i u_i^2+u_1u_2u_3.
\]

For
\[
\Phi=C-u_2^2=u_1^2+u_3^2+u_1u_2u_3,
\]
one has
\[
\dot\Phi=2H_1\dot u_1+2H_3\dot u_3+u_1u_3\dot u_2.
\]
Completing the \(i=1,3\) squares with the reversed sign and the \(i=2\) square around \(2u_2-u_1u_3\) gives exactly
\[
\frac{P}{8\pi^2}-1
=\int\left[
\frac{\lambda_1}{4}\left(\dot u_1+\frac{2H_1}{\lambda_1}\right)^2
+\frac{\lambda_3}{4}\left(\dot u_3+\frac{2H_3}{\lambda_3}\right)^2
+\frac{\lambda_2}{4}\left(\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2}\right)^2
+\frac{2u_1u_2u_3}{\lambda_2}
\right]dt.
\]
Thus all factors in (4.8) are correct, and the cubic has the **plus** sign displayed there. It must remain signed; replacing it by its negative part changes the exact action.

---

### 2. Quadratic action on exact CH

Along CH,
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

Let
\[
\xi=\delta u_1,\qquad \zeta=\delta u_3,\qquad
v_\pm=\xi\pm\zeta.
\]
Holding \(u_2=3x\) at transverse quadratic order, the quadratic part of (4.8) is
\[
\int_\rho^1\left\{
\frac12\left[L\xi'+\frac{\xi+\frac32x\zeta}{L}\right]^2
+\frac12\left[L\zeta'+\frac{\zeta+\frac32x\xi}{L}\right]^2
+3\xi\zeta
\right\}dx. \tag{2.1}
\]
The final term is precisely the quadratic contribution of the full cubic:
\[
\frac{2u_1u_2u_3}{\lambda_2}\,dt
=3\xi\zeta\,dx
=\frac34(v_+^2-v_-^2)\,dx.
\]

After diagonalization and integration by parts,
\[
\mathcal A_{\rm CH}^{(2)}
=Q_+[v_+]+Q_-[v_-]
+\left[\beta_+(x)v_+^2+\beta_-(x)v_-^2\right]_\rho^1, \tag{2.2}
\]
where
\[
Q_\pm[v]=\int_\rho^1\bigl(pv'^2+V_\pm v^2\bigr)\,dx,
\qquad
p=\frac{x(1+x)}4,
\]
\[
V_+=\frac{4+18x+15x^2}{16x(1+x)},\qquad
V_-=\frac{4-18x+3x^2}{16x(1+x)},
\]
and
\[
\beta_\pm(x)=\frac{2\pm3x}{8}.
\]
Hence, under terminal matching \(v_\pm(1)=0\),
\[
\mathcal A_{\rm CH}^{(2)}
=Q_+[v_+]+Q_-[v_-]
-\beta_+(\rho)v_+(\rho)^2
-\beta_-(\rho)v_-(\rho)^2. \tag{2.3}
\]

The boundary terms in (2.3) are essential. There is a second boundary contribution inside each ground-state representation below; omitting either copy gives the wrong transition payment.

---

### 3. Ground-state representations

The positive zero modes are
\[
f_+(x)=x\sqrt{1+x},\qquad
f_-(x)=\frac{x}{(1+x)^{5/2}},
\]
and direct substitution gives
\[
-(pf_\pm')'+V_\pm f_\pm=0,
\qquad
p\frac{f_\pm'}{f_\pm}=\beta_\pm=\frac{2\pm3x}{8}. \tag{3.1}
\]
These are the Riccati identities checked algebraically in `PerpGroundState.lean`. The Lean file establishes the rational identity after denominator clearing; positivity, integration by parts, and sharpness are analytic steps.

For \(v=f_\pm w\),
\[
pv'^2+V_\pm v^2
=p f_\pm^2(w')^2+\frac d{dx}\bigl(\beta_\pm v^2\bigr).
\]
Therefore
\[
\boxed{
Q_\pm[v]
=\int_\rho^1p f_\pm^2
\left(\left(\frac v{f_\pm}\right)'\right)^2dx
+\left[\beta_\pm v^2\right]_\rho^1.
} \tag{3.2}
\]
If \(v(1)=0\) and \(V=v(\rho)\), this becomes
\[
Q_\pm[v]
=\int_\rho^1p f_\pm^2
\left(\left(\frac v{f_\pm}\right)'\right)^2dx
-\beta_\pm(\rho)V^2. \tag{3.3}
\]

---

### 4. Sharp Dirichlet-to-Neumann form

Define
\[
R_\pm(\rho)=\int_\rho^1\frac{dx}{p(x)f_\pm(x)^2}.
\]
Since \(w(1)=0\) and \(w(\rho)=V/f_\pm(\rho)\), weighted Cauchy–Schwarz gives
\[
\int_\rho^1pf_\pm^2(w')^2dx
\ge \frac{V^2}{f_\pm(\rho)^2R_\pm(\rho)}.
\]
Equality holds uniquely for
\[
v_{\pm,*}(x)
=
V\,\frac{f_\pm(x)}{f_\pm(\rho)}
\frac{R_\pm(x)}{R_\pm(\rho)},
\qquad
R_\pm(x)=\int_x^1\frac{ds}{p(s)f_\pm(s)^2}.
\]
Thus
\[
\boxed{
Q_\pm[v]\ge \kappa_\pm(\rho)V^2,\qquad
\kappa_\pm(\rho)
=\frac{1}{f_\pm(\rho)^2R_\pm(\rho)}-\beta_\pm(\rho).
} \tag{4.1}
\]
Equivalently,
\[
\kappa_\pm(\rho)
=-p(\rho)\frac{v_{\pm,*}'(\rho)}{v_{\pm,*}(\rho)}.
\]

#### Minus channel

Because
\[
\frac1{pf_-^2}=\frac{4(1+x)^4}{x^3},
\]
\[
R_-(\rho)
=\frac2{\rho^2}+\frac{16}{\rho}
-24\log\rho-16\rho-2\rho^2.
\]
Set
\[
\Delta_-(\rho)
=1+8\rho-12\rho^2\log\rho-8\rho^3-\rho^4.
\]
Then
\[
f_-(\rho)^2R_-(\rho)
=\frac{2\Delta_-(\rho)}{(1+\rho)^5},
\]
and therefore
\[
\boxed{
\kappa_-(\rho)
=\frac{(1+\rho)^5}{2\Delta_-(\rho)}
-\frac{2-3\rho}{8}.
} \tag{4.2}
\]

#### Plus channel

Here
\[
\frac1{pf_+^2}=\frac4{x^3(1+x)^2},
\]
so
\[
R_+(\rho)
=\frac2{\rho^2}-\frac8\rho+8-\frac4{1+\rho}
+12\log\frac{1+\rho}{2\rho}.
\]
Define
\[
\Delta_+(\rho)
=1-3\rho-2\rho^2+4\rho^3
+6\rho^2(1+\rho)\log\frac{1+\rho}{2\rho}.
\]
Then
\[
f_+(\rho)^2R_+(\rho)=2\Delta_+(\rho),
\]
hence
\[
\boxed{
\kappa_+(\rho)
=\frac1{2\Delta_+(\rho)}
-\frac{2+3\rho}{8}.
} \tag{4.3}
\]

These formulas hold for \(0<\rho<1\).

---

### 5. Exact boundary payment required from the transition

Combining the sharp bound (4.1) with the already-present traces in (2.3) yields
\[
\boxed{
\mathcal A_{\rm CH}^{(2)}
\ge d_+(\rho)V_+^2+d_-(\rho)V_-^2,
\qquad V_\pm=v_\pm(\rho),
} \tag{5.1}
\]
where
\[
d_\pm=\kappa_\pm-\beta_\pm.
\]
Explicitly,
\[
\boxed{
d_+(\rho)
=\frac1{2\Delta_+(\rho)}-\frac{2+3\rho}{4},
} \tag{5.2}
\]
\[
\boxed{
d_-(\rho)
=\frac{(1+\rho)^5}{2\Delta_-(\rho)}
-\frac{2-3\rho}{4}.
} \tag{5.3}
\]

Therefore the bolt-to-\(\rho\) transition action must satisfy the sharp signed trace inequality
\[
\boxed{
\begin{aligned}
\mathcal A_{\rm tr}^{(2)}\ge{}&
\left(\frac{2+3\rho}{4}
-\frac1{2\Delta_+(\rho)}\right)V_+^2\\
&+
\left(\frac{2-3\rho}{4}
-\frac{(1+\rho)^5}{2\Delta_-(\rho)}\right)V_-^2.
\end{aligned}
} \tag{5.4}
\]
Equivalently,
\[
\mathcal A_{\rm tr}^{(2)}
+d_+(\rho)V_+^2+d_-(\rho)V_-^2\ge0. \tag{5.5}
\]

This is the exact quadratic payment. It is signed, not a positive multiple of \(V_+^2+V_-^2\). As \(\rho\downarrow0\),
\[
d_+(\rho)=\frac34\rho+O(\rho^2|\log\rho|),
\qquad
d_-(\rho)=-\frac34\rho+O(\rho^2|\log\rho|),
\]
so, to leading order,
\[
\mathcal A_{\rm tr}^{(2)}
\ge \frac34\rho\,V_-^2-\frac34\rho\,V_+^2
+O(\rho^2|\log\rho|)(V_+^2+V_-^2).
\]
At \(\rho=0.1\),
\[
d_+(0.1)\approx0.05274,\qquad d_-(0.1)\approx-0.03565,
\]
and the required payment is approximately
\[
\mathcal A_{\rm tr}^{(2)}
\ge -0.05274\,V_+^2+0.03565\,V_-^2.
\]

The two appearances of \(\beta_\pm\) have different origins:

1. diagonalizing the quadratic form (2.1) produces the trace in (2.2);
2. factorizing \(Q_\pm\) produces the trace in (3.2).

Hence the coefficient relevant to the full quadratic expansion of (4.8) is
\[
\frac1{f_\pm(\rho)^2R_\pm(\rho)}-2\beta_\pm(\rho),
\]
not merely the Dirichlet-to-Neumann coefficient \(\kappa_\pm\) of \(Q_\pm\).

---

### 6. What the reconstruction evolution supplies

The exact reconstruction equation
\[
\dot a_i=u_i+\gamma_i(a)
\]
implies
\[
\frac d{dt}\log\frac ac
=\frac{u_1}{a}-\frac{u_3}{c}
+\frac{2(c^2-a^2)}{abc}. \tag{6.1}
\]
Linearize at CH and write
\[
\theta=\delta\log(a/c),\qquad
v_-=\delta u_1-\delta u_3.
\]
Using \(dx/dt=2\sqrt{x(1+x)}\), one obtains
\[
\theta'+\frac{2}{x(1+x)}\theta
=\frac{v_-}{2x\sqrt{1+x}}.
\]
The integrating factor is \((x/(1+x))^2\), giving
\[
\boxed{
\frac d{dx}\left[\left(\frac{x}{1+x}\right)^2\theta\right]
=\frac12 f_-(x)v_-(x).
} \tag{6.2}
\]
Thus the same \(f_-\) that factors the minus Sturm operator is naturally selected by the geometric evolution.

If \(\theta(1)=0\),
\[
\boxed{
\int_\rho^1 f_-(x)v_-(x)\,dx
=-2\left(\frac{\rho}{1+\rho}\right)^2\theta(\rho).
} \tag{6.3}
\]
If the metric itself is already matched to CH at \(x=\rho\), so that \(\theta(\rho)=0\), this reduces to the moment constraint
\[
\int_\rho^1 f_-v_-\,dx=0.
\]

This compatibility gives additional coercivity but does **not**, by itself, imply the payment (5.4). Indeed, put
\[
k=pf_-^2,\qquad h=f_-^2,\qquad
R(x)=\int_x^1k(s)^{-1}ds,\qquad R_\rho=R(\rho),
\]
\[
H_\rho=\int_\rho^1h(x)R(x)\,dx.
\]
Let \(\phi\) solve
\[
-(k\phi')'=h,\qquad \phi(\rho)=\phi(1)=0,
\]
and set
\[
N_\rho=\int_\rho^1h\phi\,dx
=\int_\rho^1k(\phi')^2dx>0.
\]
For fixed
\[
V=v_-(\rho),\qquad \Theta=\theta(\rho),
\]
the exact constrained minus-channel minimum is
\[
\boxed{
d_-(\rho)V^2+
\frac{\left[
-2\left(\frac{\rho}{1+\rho}\right)^2\Theta
-\dfrac{VH_\rho}{f_-(\rho)R_\rho}
\right]^2}{N_\rho}.
} \tag{6.4}
\]
The extra term is nonnegative, but \(\Theta\) can make it vanish. Consequently, the first-order evolution is a reconstruction/compatibility equation, not an automatic positive boundary payment.

---

### 7. Narrowest unresolved inequality

At quadratic order, the remaining object is the joint bolt-transition trace inequality
\[
\boxed{
\begin{aligned}
0\le{}&
\mathcal A_{\rm tr}^{(2)}
+d_+(\rho)V_+^2+d_-(\rho)V_-^2\\
&+
\frac{\left[
-2\left(\frac{\rho}{1+\rho}\right)^2\Theta
-\dfrac{V_-H_\rho}{f_-(\rho)R_\rho}
\right]^2}{N_\rho},
\end{aligned}
} \tag{7.1}
\]
subject to regular bolt data and the corresponding longitudinal endpoint constraints. The substantive missing control is specifically the joint minus-channel trace \((V_-,\Theta)\); the plus channel contributes a credit when \(d_+>0\).

For the full nonlinear theorem, the unresolved statement is the variable-coefficient analogue of (7.1) for trajectories satisfying
\[
\dot a_i=u_i+\gamma_i(a),
\]
with the transition action taken directly from (4.8), including
\[
\frac{2u_1u_2u_3}{\lambda_2}
\]
with its full sign. The evolution does not impose a pointwise sign on this cubic and does not independently force the required endpoint payment.

The supplied transition profiles are consistent with the boundary signs and factors—for example, their stored identity
\[
Q_-=\text{ground-state bulk}-\beta_-(\rho)v_-(\rho)^2
\]
matches to quadrature accuracy—but they are neither exact-CH collars at typical cuts nor proofs of (7.1). The exact CH endpoint theorem is therefore closed by formulas (3.2), (4.1)–(4.3), and (5.1)–(5.4); the bolt-transition inequality (7.1), or its nonlinear counterpart, remains the precise missing step.