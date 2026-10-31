# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 11,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step11_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step11_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Derive a concrete rigorous certification route for the frozen diagonal Bianchi-IX cell J_6/(8π²)<1 using its explicit F,G,w profile. The raw spin formulas suffer bolt cancellation. Starting from y=x-x0, F=y Fhat, G=y Ghat, w=y² what and/or a regular proper-radius variable, derive regularized formulas or Taylor-model structure for the relative-plus-scalar density that can be enclosed by Arb/MPFI on finitely many intervals. Specify which analytic bounds and endpoint expansions suffice, how to handle exp/log/Chebyshev terms with decimal coefficients, and how to turn the 8.84e-4 numerical margin into a theorem-level upper bound without relying on optimizer convergence or empirical Richardson error. Use the supplied formulas and scripts, and pursue an implementable proof rather than general advice.

## Integrated Scientific Memo

## Rigorous certificate for the frozen \(X=8,\ x_0=10^{-2}\) cell

Let
\[
c=x_0=\frac1{100},\qquad \ell=\log(X/c)=\log 800,\qquad
z=\frac{\log(x/c)}{\ell}\in[0,1].
\]
The theorem should concern the metric defined by the 24 displayed JSON decimals interpreted as **exact rationals**. The optimization metadata and previously computed values of \(P,J\) play no role.

The cleanest proof is:

1. factor the bolt zeros exactly;
2. evaluate an everywhere regular relative-plus-scalar density;
3. enclose its integral by interval Taylor/Simpson bounds with proved derivative remainders;
4. verify that its upper endpoint is below an exact negative rational.

This eliminates the omitted bolt segment and empirical Richardson estimate in the current Arb script.

---

### 1. Exact profile and regular bolt factors

Write
\[
y=x-c=c(e^{\ell z}-1)=c\ell z\,E(\ell z),
\qquad
E(t)=\frac{e^t-1}{t},\quad E(0)=1.
\]
Put
\[
S(z)=10z^3-15z^4+6z^5=z^3s(z),
\qquad s(z)=10-15z+6z^2.
\]
Let
\[
p_F(z)=\sum_{k=0}^7c_k^FT_k(2z-1),\quad
p_G(z)=\sum_{k=0}^7c_k^GT_k(2z-1),\quad
p_w(z)=\sum_{k=0}^7c_k^wT_k(2z-1),
\]
and
\[
q_F=(1-z)^3p_F,\qquad q_G=(1-z)^3p_G.
\]

The code’s shift of \(c_0^G\) must be performed in exact rational arithmetic:
\[
c_0^G\leftarrow c_0^G-\sum_{k=0}^7(-1)^k(c_k^F+c_k^G).
\]
Hence \(p_G(0)=-p_F(0)\) exactly.

Factor
\[
F=yf,\qquad G=yg,\qquad w=y^2h.
\]
The regular factors are
\[
\boxed{
f=e^{q_F}+\frac{z^2s(z)}{\ell E(\ell z)}
}
\]
and
\[
\boxed{
g=
\left(1+
\frac{(x^2+c)z^2s(z)}{c\ell E(\ell z)}
\right)e^{q_G}.
}
\]
For \(w\), either retain its explicit unfactored formula
\[
w=\log(1+x)\,z^3s(z)+z^2(1-z)^3p_w(z),
\]
or use
\[
\boxed{
h=
\frac{z\,s(z)\log(1+x)+(1-z)^3p_w(z)}
{c^2\ell^2E(\ell z)^2}.
}
\]

These identities are exact and have no division by a quantity vanishing at \(z=0\). Moreover,
\[
f>0,\qquad g>0,\qquad x\ge c>0
\]
structurally, since \(E(\ell z)>0\), \(S(z)\ge0\), and the exponential factors are positive.

At the bolt,
\[
f_0=e^{p_F(0)},\qquad g_0=e^{p_G(0)}=f_0^{-1},
\]
so \(f_0g_0=1\) exactly, while \(w=O(y^2)\). With \(r=\sqrt y\),
\[
g_{\rm metric}
=\frac{dr^2}{g(r^2)}
+r^2f(r^2)\sigma_1^2
+x(r^2)\sigma_2^2
+x(r^2)e^{r^4h(r^2)}\sigma_3^2,
\]
making bolt smoothness and parity explicit.

---

### 2. Regularized spin variables

Use the cyclic axes of the supplied scripts:
\[
a_1=\sqrt x,\qquad
a_2=\sqrt x\,e^{w/2},\qquad
a_3=\sqrt y\,\sqrt f.
\]
Let
\[
\Phi(t)=\frac{e^t-1}{t},\qquad \Phi(0)=1.
\]
Then the raw Cartan variables factor as
\[
u_1=\sqrt y\,U_1,\qquad
u_2=\sqrt y\,U_2,\qquad
u_3=U_3,
\]
where, with \(\partial_y=(\ell x)^{-1}\partial_z\),
\[
\boxed{
U_1=
\sqrt{\frac gx}
-
\frac{e^{-w/2}}{\sqrt{xf}}
\left(f+xyh\,\Phi(w)\right),
}
\]
\[
\boxed{
U_2=
e^{w/2}\sqrt{\frac gx}(1+xw_y)
-
\frac{f-xyh\,\Phi(w)}{\sqrt{xf}},
}
\]
\[
\boxed{
U_3=
\sqrt{gf}\left(1+y\frac{f_y}{f}\right)
-2\cosh\frac w2
+\frac{yf}{x}e^{-w/2}.
}
\]
Equivalently, to avoid forming \(h=w/y^2\), define the regular function
\[
\omega=\frac wy
=
\frac{z\{\log(1+x)z\,s(z)+(1-z)^3p_w(z)\}}
{c\ell E(\ell z)}
\]
and replace \(yh\) by \(\omega\). Either representation is regular.

Set
\[
L_1=e^{w/2}\sqrt f,\qquad
L_2=e^{-w/2}\sqrt f,\qquad
L_3=\frac{x e^{w/2}}{\sqrt f}.
\]
Then
\[
\lambda_1=\sqrt y\,L_1,\qquad
\lambda_2=\sqrt y\,L_2,\qquad
\lambda_3=y^{-1/2}L_3.
\]

Define
\[
K_1=U_1+\frac12U_2U_3,\qquad
K_2=U_2+\frac12U_3U_1,\qquad
K_3=U_3+\frac y2U_1U_2
\]
and
\[
V_1=\sqrt g\,(U_1+2yU_{1,y}),\qquad
V_2=\sqrt g\,(U_2+2yU_{2,y}),\qquad
V_3=2\sqrt g\,U_{3,y}.
\]
Thus
\[
\dot u_1=V_1,\qquad
\dot u_2=V_2,\qquad
\dot u_3=\sqrt y\,V_3.
\]

The completed-square brackets regularize to
\[
B_1=V_1+\frac{2K_1}{L_1},
\]
\[
B_2=V_2-\frac{2U_2-U_1U_3}{L_2},
\]
\[
B_3=V_3+\frac{2K_3}{L_3}.
\]

Since
\[
dt=\frac{dy}{2\sqrt{yg}},
\]
all half-powers of \(y\) cancel. The relative \(P\)-density with respect to \(dy\) is
\[
\boxed{
R_P=
\frac{L_1B_1^2+L_2B_2^2+L_3B_3^2}{8\sqrt g}
+\frac{U_1U_2U_3}{L_2\sqrt g}.
}
\]

For the scalar square, put
\[
\boxed{
\begin{aligned}
\Sigma={}&
\frac{V_1}{\sqrt x}
+\frac{V_2}{\sqrt x\,e^{w/2}}
+\frac{V_3}{\sqrt f}\\
&+\frac{2K_1}{\sqrt x\,e^{w/2}\sqrt f}
+\frac{2K_2}{\sqrt x\,\sqrt f}
+\frac{2K_3}{x e^{w/2}} .
\end{aligned}
}
\]
Then
\[
\boxed{
R_s=
\frac{x e^{w/2}\sqrt f}{8\sqrt g}(\Sigma-12)^2.
}
\]

Therefore the regular integrand on \([0,1]\) is
\[
\boxed{
\mathcal R(z)=\ell x(z)\,[R_P(z)+R_s(z)]
}
\]
and
\[
\boxed{
\frac{J_6}{8\pi^2}-1=\int_0^1\mathcal R(z)\,dz.
}
\]

This is the expression to certify—not the raw square-root spin formula.

At \(z=0\), if
\[
A=\frac{\sqrt{g_0}-\sqrt{f_0}}{\sqrt c},
\]
then
\[
U_1(0)=U_2(0)=A,\qquad U_3(0)=-1,
\]
so every displayed term is finite. In particular,
\[
\frac{U_1U_2U_3}{L_2\sqrt g}\longrightarrow -A^2.
\]

---

### 3. Correct endpoint identity

There is a minor diagnostic issue in the source scripts: the recorded
\[
C=\sum_i u_i^2+u_1u_2u_3
\]
is not the boundary primitive for the relative completion. Direct expansion gives
\[
P_{\rm pos}
-\left(S_1+S_2+S_3+\frac{2u_1u_2u_3}{\lambda_2}\right)
=-\frac d{dt}B
\]
with
\[
\boxed{
B=u_1^2+u_3^2+u_1u_2u_3.
}
\]
There is no \(u_2^2\) term. This follows by the product rule:
\[
-2\dot u_1H_1-2\dot u_3H_3-\dot u_2u_1u_3
=-\frac d{dt}(u_1^2+u_3^2+u_1u_2u_3).
\]

In regular variables,
\[
B=yU_1^2+U_3^2+yU_1U_2U_3.
\]
Thus \(B(x_0)=1\). At \(X\), the profile agrees with the complex-hyperbolic profile through the required jets, yielding \(u_1(X)=u_3(X)=0\), hence \(B(X)=0\). Consequently
\[
\frac P{8\pi^2}=1+\int(S_1+S_2+S_3+\text{cubic})\,dt
\]
exactly. The density formulas used numerically remain valid; only the auxiliary diagnostic \(C\) should not be presented as this primitive.

This algebraic identity is suitable for a one-line symbolic polynomial expansion or a Lean `ring` proof.

---

### 4. Exact treatment of decimals and transcendental functions

Parse every decimal token \(d=\pm m10^{-k}\) as
\[
d=\frac{\pm m}{10^k}\in\mathbb Q,
\]
using `fmpq`; do not first pass through Python `float`. Construct Chebyshev polynomials by
\[
T_0=1,\quad T_1=2z-1,\quad
T_{n+1}=2(2z-1)T_n-T_{n-1}.
\]
Thus the polynomial data and the \(c_0^G\) correction are exact.

Construct one outward-rounded Arb ball for
\[
\ell=\log 800
\]
at, say, 256 bits and reuse it.

The removable functions \(E\) and \(\Phi\) should be evaluated as entire functions, not as `(exp(t)-1)/t`. For
\[
\Phi^{(j)}(t)=\sum_{m=0}^\infty\frac{t^m}{m!(m+j+1)}
=\int_0^1s^je^{st}\,ds,
\]
truncation after degree \(K\) obeys
\[
\left|
\Phi^{(j)}(t)-\sum_{m=0}^K\frac{t^m}{m!(m+j+1)}
\right|
\le
\frac{e^B B^{K+1}}{(K+j+2)(K+1)!},
\qquad |t|\le B.
\]
Here \(B=6.685\) suffices for \(E(\ell z)\). Also
\[
|p_w(z)|\le\sum|c_k^w|<23,\qquad
\max z^2(1-z)^3=\frac{108}{3125},
\]
so
\[
|w|<\log9+\frac{108}{3125}\,23<3.
\]
Thus \(B=3\) suffices for \(\Phi(w)\). Degree \(K=100\) is already ample at 256-bit precision; \(K=160\) is a simple conservative choice.

Ordinary Arb series operations handle `exp`, `log(1+x)`, reciprocal, square root, and \(\cosh\). Their domains are certified by
\[
x\ge c,\qquad 1+x>0,\qquad f>0,\qquad g>0.
\]

---

### 5. Taylor-jet implementation

Use normalized jets
\[
A(\varepsilon)=\sum_{j=0}^N A_j\varepsilon^j,
\qquad A_j=\frac{A^{(j)}}{j!}.
\]
Multiplication is convolution, and
\[
(D_zA)_j=(j+1)A_{j+1},\qquad
D_yA=\frac1{\ell x}D_zA.
\]

To enclose \(\mathcal R^{(N)}\), build the base profile through order \(N+2\), because \(\mathcal R\) uses \(U_{i,y}\), while \(U_i\) already contains first derivatives of \(f,w\). In particular:

- values of \(\mathcal R\): profile order \(2\);
- \(\mathcal R^{(4)}\): profile order \(6\);
- degree-eight endpoint polynomial: profile order \(10\);
- \(\mathcal R^{(9)}\): profile order \(11\).

For an interval \(I\), initialize
\[
Z=(I,1,0,\ldots,0).
\]
If the resulting fourth normalized coefficient is \(\mathcal R_4(I)\), then
\[
M_4(I)=24\,\operatorname{mag}(\mathcal R_4(I))
\]
rigorously bounds \(\sup_I|\mathcal R^{(4)}|\).

The existing `J2` code should not simply be extended by repeatedly promoting derivatives: its construction
```python
J2(a[i].d, a[i].dd, 0)
```
silently sets a needed higher derivative to zero when differentiated again. A genuine arbitrary-order normalized-series class is required.

---

### 6. Finite theorem-level quadrature certificate

A robust implementation splits off a short bolt interval.

#### Bolt panel

Choose
\[
\eta=2^{-10}.
\]
At \(z=0\), compute
\[
\mathcal R(z)=\sum_{j=0}^8a_jz^j+\mathcal E_9(z),
\qquad
a_j=\frac{\mathcal R^{(j)}(0)}{j!}.
\]
Use an order-eleven interval jet on \([0,\eta]\) to obtain
\[
M_9\ge\sup_{[0,\eta]}|\mathcal R^{(9)}|.
\]
Then
\[
\boxed{
\int_0^\eta\mathcal R(z)\,dz
\in
\sum_{j=0}^8\frac{a_j\eta^{j+1}}{j+1}
+
\left[-\frac{M_9\eta^{10}}{10!},
       \frac{M_9\eta^{10}}{10!}\right].
}
\]
Unlike the current script, this includes the bolt and leaves no unproved \([0,10^{-12}]\) tail.

#### Remaining interval

On \([\eta,1]\), use composite Simpson with even \(n\), mesh
\[
h=\frac{1-\eta}{n}.
\]
Evaluate the Simpson sum entirely in Arb. For each two-subinterval panel
\[
I_k=[\eta+2kh,\eta+(2k+2)h],
\]
obtain a proved \(M_{4,k}\) from the interval jet. The exact remainder is
\[
\boxed{
E_S\le \frac{h^5}{90}
\sum_{k=0}^{n/2-1}M_{4,k}.
}
\]
Derivative enclosures may be shared over blocks: begin, for example, with 512 blocks and \(n=2^{15}\), then bisect only blocks whose contribution to \(E_S\) is excessive.

Alternatively, the midpoint second-order Taylor rule on a panel of width \(h\),
\[
\int_I\mathcal R
=h\mathcal R(m)+\frac{h^3}{24}\mathcal R''(m)+E_I,
\qquad
|E_I|\le\frac{h^5}{1920}\sup_I|\mathcal R^{(4)}|,
\]
is equally rigorous and often simpler with Taylor-series arithmetic.

A complex-ball Petras/Arb integrator applied to the same regular expression is a useful independent certificate, but the real Taylor/Simpson route already supplies a self-contained proof and avoids having to certify complex branch domains.

---

### 7. Exact final inequality

The numerical center is approximately
\[
\int_0^1\mathcal R(z)\,dz
=-8.8375686\times10^{-4}.
\]
Do not attempt merely to prove negativity at machine precision. Use the rational target
\[
\frac{J_6}{8\pi^2}<\frac{1249}{1250}=0.9992,
\]
equivalent to
\[
\int_0^1\mathcal R(z)\,dz<-\frac1{1250}.
\]
This leaves approximately \(8.38\times10^{-5}\) of certification slack.

If \(Q\) is the combined Arb quadrature ball and
\[
E=E_{\rm bolt}+E_S
\]
is the proved remainder bound, the final exact check is simply
\[
\boxed{
\operatorname{upper}(Q)+E<-\frac1{1250}.
}
\]
For example, the stronger pair
\[
\operatorname{upper}(Q)<-\frac{87}{100000},
\qquad
E<\frac1{20000}
\]
already implies
\[
\operatorname{upper}(Q)+E<-\frac{82}{100000}
<-\frac1{1250}.
\]

The certificate should print:

```text
profile_coefficients_parsed_as_exact_rationals = true
exact_cG_shift_identity                         = true
bolt_integral_ball                              = [...]
bolt_remainder_upper                            = ...
bulk_quadrature_ball                            = [...]
bulk_remainder_upper                            = ...
total_integral_upper                            = ...
target                                          = -1/1250
total_integral_upper < target                   = true
J6_over_8pi2 < 1249/1250 < 1
```

No optimizer convergence, sampled positivity, Richardson extrapolation, or empirical error model appears in this deduction.

---

### 8. Recommended algebraic cross-checks

Before trusting the final enclosure, verify symbolically:

1. substitution of \(F=yf,\ G=yg,\ w=y^2h\) into the raw spin density equals the regular expression above;
2. the endpoint primitive
   \[
   B=u_1^2+u_3^2+u_1u_2u_3
   \]
   satisfies the completed-square identity;
3. the positive-square expression for \(P/(8\pi^2)\) overlaps the enclosure of
   \[
   1+\int R_P.
   \]

The last comparison is especially useful because the endpoint constant \(1\) enters only the relative representation. It tests the formula transcription independently of the final sign inequality.

This gives an implementable theorem-level route for the frozen rational witness and converts the observed \(8.84\times10^{-4}\) deficit into the rigorous bound
\[
\boxed{\frac{J_6}{8\pi^2}<\frac{1249}{1250}<1.}
\]