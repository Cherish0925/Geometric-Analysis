# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step11_subthreshold_perpendicular_cell.md",
    "Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md",
    "Sessions/S1003A02/workspace/scripts/o11_collar_independent_verify.py",
    "Sessions/S1003A02/workspace/scripts/o11_collar_arb_certificate.py",
    "Sessions/S1003A01/workspace/scripts/perp_spin_diagnostics.py",
    "Sessions/S1003A01/workspace/data/perp_collar/x0.01_X8_J_d8.json"
  ]
}
```

## Task

Derive a concrete rigorous certification route for the frozen diagonal Bianchi-IX cell J_6/(8π²)<1 using its explicit F,G,w profile. The raw spin formulas suffer bolt cancellation. Starting from y=x-x0, F=y Fhat, G=y Ghat, w=y² what and/or a regular proper-radius variable, derive regularized formulas or Taylor-model structure for the relative-plus-scalar density that can be enclosed by Arb/MPFI on finitely many intervals. Specify which analytic bounds and endpoint expansions suffice, how to handle exp/log/Chebyshev terms with decimal coefficients, and how to turn the 8.84e-4 numerical margin into a theorem-level upper bound without relying on optimizer convergence or empirical Richardson error. Use the supplied formulas and scripts, and pursue an implementable proof rather than general advice.

## Output

## 1. Remove the bolt singularities algebraically

Write
\[
c=x_0=\frac1{100},\qquad y=x-c,\qquad
F=yf,\qquad G=yg,\qquad w=y^2h.
\]
Here \(f=\widehat F\), \(g=\widehat G\), and \(h=\widehat w\). Use the logarithmic collar coordinate
\[
z=\frac{\log(x/c)}{\ell}\in[0,1],\qquad
\ell=\log(X/c)=\log 800.
\]
Introduce the entire function
\[
E(t)=\frac{e^t-1}{t},\qquad E(0)=1.
\]
Then
\[
y=c\ell zE(\ell z),\qquad x=c+y.
\]

Let
\[
s(z)=10-15z+6z^2=1+3(1-z)(3-2z),
\qquad S(z)=z^3s(z),
\]
and let
\[
p_F(z)=\sum_{k=0}^7c^F_kT_k(2z-1),\quad
p_G(z)=\sum_{k=0}^7c^G_kT_k(2z-1),\quad
p_w(z)=\sum_{k=0}^7c^w_kT_k(2z-1).
\]
The \(c^G_0\) adjustment in the supplied script is made exactly:
\[
c^G_0\longmapsto c^G_0-p_F(0)-p_G(0).
\]
Thus \(p_G(0)=-p_F(0)\) as an exact rational identity. Set
\[
q_F=(1-z)^3p_F,\qquad q_G=(1-z)^3p_G.
\]

Dividing the supplied profiles by their bolt factors gives the regular functions
\[
\boxed{
f=e^{q_F}+\frac{z^2s(z)}{\ell E(\ell z)}
}
\]
and
\[
\boxed{
g=
\left[
1+\frac{(x^2+c)z^2s(z)}{c\ell E(\ell z)}
\right]e^{q_G}.
}
\]
Similarly,
\[
\boxed{
h=
\frac{z\,s(z)\log(1+x)+(1-z)^3p_w(z)}
     {c^2\ell^2E(\ell z)^2}.
}
\]
These formulas contain no quotient vanishing at \(z=0\). They are exactly equivalent to the JSON profile:
\[
F=yf,\qquad G=yg,\qquad w=y^2h.
\]

The elementary positivity needed later is structural:
\[
E(\ell z)\ge1,\qquad s(z)\ge1,\qquad f>0,\qquad g>0,\qquad x\ge c>0.
\]
Consequently every square root and reciprocal below is well-defined throughout the closed interval.

---

## 2. Proper-radius interpretation and bolt expansion

Put \(r=\sqrt y\). Then
\[
g_{\mathrm{metric}}
=
\frac{dr^2}{g(r^2)}
+r^2f(r^2)\sigma_1^2
+x(r^2)\sigma_2^2
+x(r^2)e^{r^4h(r^2)}\sigma_3^2.
\]
At the bolt,
\[
f_0=e^{p_F(0)},\qquad
g_0=e^{p_G(0)}=e^{-p_F(0)},\qquad f_0g_0=1,
\]
and \(w=O(r^4)\). Thus the radial and collapsing-circle coefficients have the standard smooth parity.

In the cyclic axes used by the scripts,
\[
a_1=\sqrt x,\qquad
a_2=\sqrt x\,e^{w/2},\qquad
a_3=\sqrt y\,\sqrt f.
\]
Define
\[
\Phi(t)=\frac{e^t-1}{t},\qquad \Phi(0)=1.
\]
Direct substitution into the spin variables gives
\[
u_1=\sqrt y\,U_1,\qquad
u_2=\sqrt y\,U_2,\qquad
u_3=U_3,
\]
where
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
e^{w/2}\sqrt{\frac gx}\,(1+xw_y)
-
\frac{f-xyh\,\Phi(w)}{\sqrt{xf}},
}
\]
and
\[
\boxed{
U_3=
\sqrt{gf}\left(1+y\frac{f_y}{f}\right)
-2\cosh\frac w2
+\frac{yf}{x}e^{-w/2}.
}
\]
Here
\[
\partial_y=\frac1{\ell x}\partial_z,
\]
so all \(y\)-derivatives can be generated without dividing by \(y\).

If
\[
A=\frac{\sqrt{g_0}-\sqrt{f_0}}{\sqrt c},
\]
then the endpoint behavior is
\[
u_1=rA+O(r^3),\qquad
u_2=rA+O(r^3),\qquad
u_3=-1+O(r^2).
\]
This is the cancellation that is obscured in the raw spin expressions.

---

## 3. A completely regular normalized density

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
Indeed,
\[
\dot u_1=V_1,\qquad
\dot u_2=V_2,\qquad
\dot u_3=\sqrt y\,V_3.
\]

The three completed-square brackets become
\[
B_1=V_1+\frac{2K_1}{L_1},
\]
\[
B_2=V_2-\frac{2U_2-U_1U_3}{L_2},
\]
\[
B_3=V_3+\frac{2K_3}{L_3}.
\]

After also inserting
\[
dt=\frac{dy}{2\sqrt{yg}},
\]
all powers of \(\sqrt y\) cancel. The relative \(P\)-density with respect to \(dy\) is
\[
\boxed{
R_P(y)=
\frac{L_1B_1^2+L_2B_2^2+L_3B_3^2}{8\sqrt g}
+\frac{U_1U_2U_3}{L_2\sqrt g}.
}
\]

For the scalar term, the regularized trace expression is
\[
\boxed{
\begin{aligned}
\Sigma={}&
\frac{V_1}{\sqrt x}
+\frac{V_2}{\sqrt x\,e^{w/2}}
+\frac{V_3}{\sqrt f}\\
&+\frac{2K_1}{\sqrt x\,e^{w/2}\sqrt f}
+\frac{2K_2}{\sqrt x\,\sqrt f}
+\frac{2K_3}{x e^{w/2}}.
\end{aligned}
}
\]
Hence
\[
\boxed{
R_s(y)=
\frac{x e^{w/2}\sqrt f}{8\sqrt g}\,(\Sigma-12)^2.
}
\]

The full normalized signed density is therefore
\[
R_y=R_P+R_s,
\]
and, since \(dy/dz=\ell x\),
\[
\boxed{
R(z)=\ell x(z)\,R_y(z).
}
\]
The exact relative identity from the supplied spin completion now reads
\[
\boxed{
\frac{J_6}{8\pi^2}-1=\int_0^1R(z)\,dz.
}
\]
No \(\pi\)-evaluation is needed in the numerical certificate.

At \(z=0\),
\[
L_1=L_2=\sqrt{f_0},\qquad L_3=\frac c{\sqrt{f_0}},
\]
\[
K_1=K_2=\frac A2,\qquad K_3=-1,
\]
\[
V_1=V_2=\sqrt{g_0}A.
\]
Thus every displayed expression has a finite endpoint value. In particular, the cubic contribution tends to
\[
\frac{U_1U_2U_3}{L_2\sqrt g}\longrightarrow -A^2.
\]

---

## 4. Exact treatment of the decimal witness

The twenty-four JSON coefficients should define exact rational numbers, not binary floats. For a decimal token
\[
d=\pm m\,10^{-k},
\]
construct the corresponding `fmpq(±m,10^k)`. The same applies to \(c=1/100\). The value \(X=8\) is integral.

The metadata fields `P`, `J`, `success`, `nit`, and `grad_inf` do not enter the proof. The profile is defined solely by the exact coefficient vector and the exact \(c^G_0\) adjustment.

Suitable arithmetic rules are:

1. Construct each Chebyshev polynomial by
   \[
   T_0=1,\quad T_1=2z-1,\quad
   T_{k+1}=2(2z-1)T_k-T_{k-1}.
   \]
   All coefficients remain rational.

2. Construct one Arb ball
   \[
   \ell=\log(800)
   \]
   at 256 or 320 bits and reuse it everywhere.

3. Evaluate \(\exp\), \(\log\), reciprocals, and square roots by Arb series arithmetic. Positivity of \(f,g,x,L_i\) is already established by the displayed representations.

4. Implement \(E\) and \(\Phi\) as entire functions rather than as a subtraction followed by division near zero.

For either function,
\[
\Phi^{(j)}(t)
=
\sum_{m=0}^{\infty}\frac{t^m}{m!(m+j+1)}
=
\int_0^1s^je^{st}\,ds.
\]
For \(|t|\le B\), truncation after \(m=K\) has magnitude at most
\[
\boxed{
\frac{e^B B^{K+1}}
     {(K+j+2)(K+1)!}.
}
\]
This supplies all derivatives through the required jet order.

For \(E(\ell z)\), one may use \(B=6.685\). For \(\Phi(w)\), the explicit coefficients give a simple uniform estimate. Since
\[
|p_w(z)|\le\sum_{k=0}^7|c_k^w|<23
\]
and
\[
\max_{0\le z\le1}z^2(1-z)^3=\frac{108}{3125},
\]
while \(0\le S\le1\),
\[
|w|
\le \log9+\frac{108}{3125}\,23<3.
\]
Thus \(B=3\) suffices for \(\Phi(w)\). Taking \(K=160\) makes these analytic tails far smaller than the desired integral enclosure at 256-bit precision.

---

## 5. Jet construction for values and fourth derivatives

Use normalized Taylor jets
\[
A(\varepsilon)=\sum_{j=0}^m A_j\varepsilon^j,
\qquad A_j=\frac{A^{(j)}}{j!}.
\]
Multiplication is convolution. The derivative operator is
\[
(D_zA)_j=(j+1)A_{j+1}.
\]
Define
\[
D_yA=\delta D_zA,\qquad
\delta=\frac1{\ell x}.
\]

To obtain \(R\) through order \(N\):

1. Build \(z\), \(E(\ell z)\), \(x\), \(y\), \(f\), \(g\), \(h\), and \(w=y^2h\) through order \(N+2\).

2. Form
   \[
   f_y=D_yf,\qquad w_y=D_yw
   \]
   through order \(N+1\).

3. Form \(U_1,U_2,U_3\) through order \(N+1\).

4. Form
   \[
   U_{i,y}=D_yU_i
   \]
   through order \(N\).

5. Form \(V_i,K_i,L_i,B_i,\Sigma,R_y,R\) through order \(N\).

Consequently:

- point evaluation of \(R\) uses profile jets of order \(2\);
- enclosure of \(R^{(4)}\) uses profile jets of order \(6\);
- an eighth-degree bolt Taylor polynomial uses profile jets of order \(10\);
- enclosure of \(R^{(9)}\) uses profile jets of order \(11\).

For interval derivative bounds, initialize
\[
Z=(I,1,0,\ldots,0)
\]
where \(I\) is an Arb interval. Then the fourth jet coefficient of \(R(Z)\) encloses \(R^{(4)}(z)/4!\) for every \(z\in I\). Thus
\[
M_4(I)=24\,\operatorname{mag}(R_4(I))
\]
is a proved upper bound for \(|R^{(4)}|\) on \(I\).

A minimal implementation skeleton is:

```python
def Dy(A, delta):
    return truncate(delta * Dz(A))

def Rjet(I, N):
    M = N + 2
    Z = Jet([I, 1] + [0]*(M-1))

    E = exprel(ell*Z, M)
    y = c*ell*Z*E
    x = c + y

    pF, pG, pw = cheb_polynomials(Z)
    s = 1 + 3*(1-Z)*(3-2*Z)
    qF = (1-Z)**3*pF
    qG = (1-Z)**3*pG

    f = exp(qF) + Z**2*s/(ell*E)
    g = (1 + (x*x+c)*Z**2*s/(c*ell*E))*exp(qG)
    h = (Z*s*log(1+x) + (1-Z)**3*pw)/(c*c*ell*ell*E*E)
    w = y*y*h

    delta = 1/(ell*x)
    fy = Dy(f, delta)
    wy = Dy(w, delta)

    phi = exprel(w, M-1)

    U1 = ...
    U2 = ...
    U3 = ...
    U1, U2, U3 = truncate_each((U1,U2,U3), N+1)

    U1y, U2y, U3y = [Dy(U,delta) for U in (U1,U2,U3)]

    # Construct L_i, K_i, V_i, B_i, Sigma, Ry.
    return truncate(ell*x*Ry, N)
```

All constants and jet coefficients in this computation are Arb balls; no ordinary floating-point number is needed.

---

## 6. A finite integration certificate

A particularly robust version separates a very short bolt interval from the rest.

### 6.1 Bolt interval

Take
\[
\eta=2^{-10}.
\]
Compute the degree-eight endpoint Taylor polynomial
\[
R(z)=\sum_{j=0}^8a_jz^j+\mathcal R_9(z),
\qquad
a_j=\frac{R^{(j)}(0)}{j!},
\]
using order-ten jets at \(z=0\). Enclose \(R^{(9)}\) on \([0,\eta]\) using an order-eleven interval jet, and write
\[
M_9=\sup_{[0,\eta]}|R^{(9)}|.
\]
Then
\[
\boxed{
\int_0^\eta R(z)\,dz
\in
\sum_{j=0}^8\frac{a_j\eta^{j+1}}{j+1}
+
\left[-\frac{M_9\eta^{10}}{10!},
       \frac{M_9\eta^{10}}{10!}\right].
}
\]
This interval includes the bolt itself; no omitted \(\varepsilon\)-segment remains.

### 6.2 Remaining interval

On \([\eta,1]\), use composite Simpson quadrature with an even number \(n\) of subintervals,
\[
h=\frac{1-\eta}{n}.
\]
The Arb-valued Simpson sum is
\[
Q_S=\frac h3
\left(
R(\eta)+R(1)
+4\sum_{\substack{1\le j<n\\j\ {\rm odd}}}R(\eta+jh)
+2\sum_{\substack{2\le j<n\\j\ {\rm even}}}R(\eta+jh)
\right).
\]

For the \(k\)-th Simpson pair
\[
I_k=[\eta+2kh,\eta+(2k+2)h],
\]
obtain \(M_{4,k}\) from the order-six interval-jet evaluator. The exact Simpson remainder bound is
\[
\boxed{
E_S\le\frac{h^5}{90}\sum_{k=0}^{n/2-1}M_{4,k}.
}
\]
Thus
\[
\int_\eta^1R(z)\,dz
\in Q_S+[-E_S,E_S].
\]

The derivative bounds may be computed on blocks containing several Simpson pairs: if a block enclosure supplies one \(M_4\), use that value for each pair in the block. Starting with 512 blocks and \(n=2^{15}\) gives narrow interval input while requiring only 512 order-six interval-jet evaluations. Individual blocks can be bisected whenever their contribution to \(E_S\) is disproportionately large.

For a single global fourth-derivative bound \(M_4\), the simpler estimate is
\[
E_S\le
\frac{(1-\eta)h^4}{180}M_4.
\]
With \(n=2^{15}\), an enclosure
\[
M_4<8\times10^{15}
\]
already gives a Simpson remainder below approximately \(4\times10^{-5}\). Local \(M_{4,k}\) values should give a considerably smaller sum.

---

## 7. Converting the observed margin into an exact rational inequality

Let \(Q_0\) be the Arb interval for the integrated bolt Taylor polynomial, and let \(E_0\) be its ninth-derivative remainder. Define
\[
Q=Q_0+Q_S,\qquad E=E_0+E_S.
\]
Then
\[
\int_0^1R(z)\,dz
\in Q+[-E,E].
\]

A useful exact target is
\[
\frac{J_6}{8\pi^2}<\frac{1249}{1250}=0.9992.
\]
It is enough for the certificate to print and verify
\[
\boxed{
\operatorname{upper}(Q)+E<-\frac1{1250}.
}
\]
The supplied evaluations place the center near
\[
-8.8375686\times10^{-4},
\]
so the distance to \(-1/1250=-8\times10^{-4}\) is about
\[
8.38\times10^{-5}.
\]
One convenient allocation is
\[
\operatorname{upper}(Q)<-\frac{87}{100000},
\qquad
E<\frac1{20000}.
\]
These imply
\[
\operatorname{upper}(Q)+E
<
-\frac{82}{100000}
<
-\frac1{1250}.
\]
All comparisons can be made between Arb endpoints and exact `fmpq` numbers.

The final machine-readable lines can therefore be as short as

```text
exact_decimal_profile = true
bolt_integral_ball     = [...]
simpson_sum_ball       = [...]
bolt_remainder_upper   = ...
simpson_remainder_upper= ...
integral_upper         = ...
target                 = -1/1250
integral_upper < target
J6_over_8pi2 < 1249/1250 < 1
```

This route uses neither optimizer stationarity nor Richardson extrapolation. The only numerical theorem ingredients are outward-rounded evaluations of an everywhere regular expression and explicit Taylor/Simpson derivative remainders.