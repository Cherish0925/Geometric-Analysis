# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 26,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step26_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step26_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop a mathematically decisive model for the collapsed curved/ Berger connector in the diagonal O(-1) cell problem. The target configuration is an inner ACH Einstein region with Rossi parameter log rho≈0.784, a small orbit-volume W neck across which the CR variable changes to zero, and an exact complex-hyperbolic exterior. Use Lemma P together with four-dimensional Chern–Weil/signature transgression, Bianchi-IX curvature, eta-invariant or Berger-sphere boundary terms, and the existing almost-Euclidean neck quantization as appropriate. Seek either (i) a lower-bound mechanism charging every such curved connector enough to exclude cost below the certified 0.99585, or (ii) a concrete low-dimensional variational ansatz likely to beat it. State equations, scaling regimes, topological conditions, and the cheapest distinguishing computation/proof. Avoid generic brainstorming.

## Integrated Scientific Memo

## Decisive collapsed-connector model

Let
\[
p_\star=0.99584841,\qquad
g=dt^2+\sum_{i=f,g,h}a_i^2\sigma_i^2,\qquad
W=a_fa_ga_h,
\]
with \(d\sigma_i=2\sigma_j\wedge\sigma_k\), and normalize
\[
\widehat P=\frac1{8\pi^2}\int |\Ric^\circ|^2\,dV.
\]
The inner Einstein end has
\[
\widetilde\Phi\simeq\log\rho\simeq0.784,
\]
whereas exact CH has \(\widetilde\Phi=0\).

The most useful conclusion is a dichotomy:

* every connector passing through a genuine product/ALF Berger neck is charged by Chern–Gauss–Bonnet flux, often by an amount much larger than \(p_\star\);
* any possible sub-\(p_\star\) escape must instead be a highly sheared, non-product collapsed transition. That residual class is described exactly by a scale-invariant three-function control problem.

This materially narrows the open collapse branch.

---

### 1. Exact Euler-flux lower bound

For a principal orbit \(\Sigma_t\cong S^3\), let \(K^{(3)}_{jk}\) be its intrinsic sectional curvatures:
\[
K_{jk}^{(3)}
=
\frac{(a_j^2-a_k^2)^2+2a_i^2(a_j^2+a_k^2)-3a_i^4}
{a_i^2a_j^2a_k^2},
\qquad \{i,j,k\}=\{f,g,h\}.
\]
Define
\[
\mathfrak b(t)=
W\left(
y_fK^{(3)}_{gh}+y_gK^{(3)}_{hf}+y_hK^{(3)}_{fg}
-y_fy_gy_h
\right),\qquad y_i=\frac{a_i'}{a_i}.
\tag{1}
\]
With outward-normal conventions fixed so that a round Euclidean sphere has
\(\mathfrak b=2\), the Gauss–Bonnet boundary term is \(4\pi^2\mathfrak b\).

For an annulus \(C=[t_0,t_1]\times S^3\), \(\chi(C)=0\), and Chern–Gauss–Bonnet gives
\[
\widehat P(C)
=
\mathfrak b(t_1)-\mathfrak b(t_0)
+\frac1{4\pi^2}\int_C |W_g|^2
+\frac1{96\pi^2}\int_C s_g^2.
\tag{2}
\]
Hence
\[
\boxed{\widehat P(C)\ge \mathfrak b(t_1)-\mathfrak b(t_0).}
\tag{3}
\]
This estimate is scale invariant: under \(g\mapsto\lambda^2g\), the factors \(W,y,K^{(3)}\) scale as \(\lambda^3,\lambda^{-1},\lambda^{-2}\).

For exact CH,
\[
a_f=\sinh t\cosh t,\qquad a_g=a_h=\sinh t,
\]
direct substitution yields
\[
\mathfrak b_{\rm CH}(t)=2-6\sinh^4t.
\tag{4}
\]
More generally, near an ACH Einstein state, with
\[
\kappa=\frac{a_f}{a_ga_h},\qquad
\zeta=\frac1{a_ga_h},\qquad
(y_f,y_g,y_h)=(2,1,1)+o(1),
\]
one obtains
\[
\mathfrak b
=
-\kappa(4\kappa^2+2)\zeta^{-2}+O(\zeta^{-1}).
\tag{5}
\]
Thus near \(\kappa=1\),
\[
\mathfrak b=-6\zeta^{-2}+O(\zeta^{-1}).
\tag{6}
\]

At the validated block \(\zeta=10^{-2}\), \(q\in[0.7,0.9]\), this predicts an Euler flux of order \(-6\times10^4\). Meanwhile the source bounds give
\[
\left|\int_T^\infty\zeta^2G\,dt\right|
\le \frac{19.58}{2(1.998)}10^{-4}
<4.91\times10^{-4},
\]
so this orbit already represents the Rossi parameter \(\log\rho\simeq0.784\) to \(5\times10^{-4}\).

Therefore, if the later collapsed neck has \(\mathfrak b\) near \(0\), then (3) charges the intervening connector by approximately \(-\mathfrak b(T)\), overwhelmingly exceeding \(p_\star\). This does not depend on the physical size of the orbit.

---

### 2. Berger and ALF necks have small Euler flux

For a biaxial orbit
\[
a_g=a_h=A,\qquad a_f=B,\qquad
\lambda=\frac BA,
\]
set
\[
U=A'=A\,\frac{A'}A,\qquad
V=A\,\frac{B'}B.
\]
Equation (1) reduces to
\[
\boxed{
\mathfrak b
=
\lambda\left[
V(4-3\lambda^2-U^2)+2U\lambda^2
\right].
}
\tag{7}
\]

Consequently:

* a quasi-product Berger neck, \(U,V\simeq0\), has \(\mathfrak b\simeq0\);
* an ALF end, \(A\sim R\), \(B\to m\), has \(\lambda\to0\), \(U\to1\), \(V\to0\), hence \(\mathfrak b\to0\);
* an almost-Euclidean sphere has \(\lambda,U,V\to1\), hence \(\mathfrak b\to2\), consistently with Lemma Q′.

A coordinate-free quantitative version is obtained with
\[
r=W^{1/3},\qquad
\widehat y_i=ry_i,\qquad
\widehat K_{jk}=r^2K^{(3)}_{jk}.
\]
If
\[
|\widehat y_i|\le\varepsilon,\qquad
|\widehat K_{jk}|\le K_0,
\]
then
\[
\mathfrak b\ge-3K_0\varepsilon-\varepsilon^3.
\tag{8}
\]
Thus an inner orbit \(\Sigma_-\) is separated from every such curved product neck whenever
\[
-\mathfrak b(\Sigma_-)
>
p_\star+3K_0\varepsilon+\varepsilon^3.
\tag{9}
\]
For the developed Rossi block the margin should be enormous.

This proves the desired lower bound for ordinary Berger/ALF connectors once (1), evaluated on the validated state box, is enclosed rigorously by interval arithmetic.

---

### 3. Signature refinement and its correct use

Let \(\vartheta(t)\) denote the Pontryagin Chern–Simons flux in the Hopf framing determined by the \(O(-1)\) bolt:
\[
\frac1{12\pi^2}\int_{U_t}
\bigl(|W^+|^2-|W^-|^2\bigr)
=
\tau(U_t)+\vartheta(t).
\tag{10}
\]
For an annulus,
\[
\int_C(|W^+|^2-|W^-|^2)
=
12\pi^2\bigl(\vartheta(t_1)-\vartheta(t_0)\bigr).
\tag{11}
\]
Since
\[
\int_C|W|^2
\ge
\left|\int_C(|W^+|^2-|W^-|^2)\right|,
\]
combining (2) and (11) gives
\[
\boxed{
\widehat P(C)\ge
\mathfrak b(t_1)-\mathfrak b(t_0)
+
3|\vartheta(t_1)-\vartheta(t_0)|.
}
\tag{12}
\]

For the inner region \(U_t\), whose topology is \((\chi,\tau)=(2,-1)\),
\[
\widehat P(U_t)
\ge
3|-1+\vartheta(t)|+\mathfrak b(t)-4.
\tag{13}
\]
At an almost-Euclidean enclosing sphere,
\[
(\mathfrak b,\vartheta)=(2,0)+O(\varepsilon),
\]
and (13) recovers
\[
\widehat P(U_t)\ge1-O(\varepsilon),
\]
the existing neck quantization.

For a general moving Bianchi-IX hypersurface, \(\vartheta\) is not merely the intrinsic Berger \(\eta\)-invariant; extrinsic terms enter. It should therefore be computed directly from the Levi-Civita connection,
\[
\operatorname{CS}(\omega)
=\operatorname{tr}\left(\omega\wedge d\omega+\frac23\omega^3\right),
\]
using
\[
\omega_{i0}=y_i e^i,\qquad
\omega_{ij}
=
\frac{a_i^2+a_j^2-a_k^2}{a_ia_ja_k}\,e^k
\]
with the appropriate cyclic signs. The intrinsic APS \(\eta\)-formula is safe only on a totally geodesic boundary, or after accounting explicitly for the extrinsic transgression.

The pair
\[
t\longmapsto (\mathfrak b(t),\vartheta(t))
\]
therefore provides a two-dimensional obstruction diagram. A connector of cost below \(p_\star\) must satisfy
\[
\mathfrak b(t)-\mathfrak b(t_-)
+3|\vartheta(t)-\vartheta(t_-)|
<p_\star
\tag{14}
\]
at every intermediate orbit. The product/ALF locus lies near \(\mathfrak b=0\), while the developed ACH orbit lies far to the left.

---

### 4. Exact residual variational problem for high-shear collapse

The flux argument does not by itself rule out a transition that keeps \(\mathfrak b\) very negative by introducing large normalized second fundamental form. Such a transition is not a product or ALF Berger neck. It is the only residual collapse mechanism.

Introduce volume and shape variables
\[
a_f=r\,e^{2\beta/3},\qquad
a_g=r\,e^{-\beta/3+q/2},\qquad
a_h=r\,e^{-\beta/3-q/2},\qquad
h=\log r.
\tag{15}
\]
Then
\[
W=r^3,\qquad
q=\log(a_g/a_h),\qquad
\beta=\log\frac{a_f}{\sqrt{a_ga_h}}.
\]

Define the three trace-free Ricci combinations
\[
D=R_{gg}-R_{hh},
\]
\[
E=R_{ff}-\frac{R_{gg}+R_{hh}}2,
\]
\[
H=R_{00}-\frac{R_{ff}+R_{gg}+R_{hh}}3.
\]
The diagonal Bianchi-IX equations give
\[
\begin{aligned}
D={}&-q''-3h'q'
+8e^{-2h}\left(
e^{-4\beta/3}\sinh 2q-e^{2\beta/3}\sinh q
\right),\\
E={}&-\beta''-3h'\beta'
+e^{-2h}\left(
4e^{8\beta/3}-4e^{2\beta/3}\cosh q
-8e^{-4\beta/3}\sinh^2q
\right),\\
H={}&-2h''-\frac23(\beta')^2-\frac12(q')^2\\
&\quad
+e^{-2h}\left(
\frac23e^{8\beta/3}
-\frac83e^{2\beta/3}\cosh q
+\frac83e^{-4\beta/3}\sinh^2q
\right).
\end{aligned}
\tag{16}
\]
The full diagonal defect is exactly
\[
\boxed{
\widehat P
=
\int r^3\left(
\frac{3}{16}H^2+\frac16E^2+\frac18D^2
\right)\,dt.
}
\tag{17}
\]
This is the desired finite-dimensional variational model, not merely a lower bound.

Under a simultaneous neck rescaling
\[
t=\varepsilon x,\qquad r(t)=\varepsilon R(x),
\]
the three controls \(H,E,D\) scale as \(\varepsilon^{-2}\), whereas \(r^3dt\) scales as \(\varepsilon^4\). Hence (17) is exactly scale invariant. Small orbit volume alone cannot make the connector cheap.

Moreover, in the strong Hopf-collapse regime \(\beta\to-\infty\),
\[
D\supset8e^{-2h-4\beta/3}\sinh2q,\qquad
H\supset\frac83e^{-2h-4\beta/3}\sinh^2q.
\tag{18}
\]
Thus finite subunit action generically forces \(q\to0\) before severe collapse. Avoiding this requires a singular cancellation through \(q'',h'',\beta''\), which is precisely the high-shear residual class measured by (17).

---

### 5. Incorporating CR pinning

The exact pinning identity is
\[
\widetilde\Phi'=\zeta^2G-\frac14D,
\tag{19}
\]
because \(D=\Ric^\circ_{gg}-\Ric^\circ_{hh}\). From the \(D^2/8\) term in (17),
\[
\boxed{
\widehat P(C)\ge
\frac{2\left(
\Delta\widetilde\Phi-\int_C\zeta^2G\,dt
\right)^2}
{\displaystyle\int_C\frac{dt}{r^3}}.
}
\tag{20}
\]
At large volume this is sharp and gives
\[
\widehat P\sim \frac12e^{4T}(\Delta\log\rho)^2,
\]
so changing \(0.784\) to zero cannot occur in the developed ACH region.

At small volume, \(\int dt/r^3\) may become large and (20) alone degenerates. Equations (16)–(18) supply the missing coercivity: producing a large Einstein drift \(\zeta^2G\), or maintaining nonzero \(q\) through Hopf collapse, forces large \(E,H,D\) unless the state follows a special singular trajectory.

Thus the two estimates divide the problem cleanly:

* Lemma P excludes resetting \(q\) at large \(W\);
* Euler/signature flux excludes resetting it through an ordinary product or ALF neck;
* only a high-shear scale-invariant transition remains.

---

### 6. Cheapest distinguishing computation

The least expensive decisive test is not a full connector optimization.

1. **Certified endpoint flux.** Evaluate \(\mathfrak b\) by interval arithmetic on the existing validated Einstein state box at \(\zeta=10^{-2}\), \(q\in[0.7,0.9]\). The target certificate is simply
   \[
   \mathfrak b_{\rm inner}< -p_\star-\delta
   \]
   for a comfortably large \(\delta\); asymptotics predict a vastly stronger result.

2. **Neck-class flux bound.** Prove from the proposed Berger/ALF neck hypotheses either
   \[
   \mathfrak b_{\rm neck}\ge-\delta
   \]
   via (7), or via the normalized bounds (8). Then (3) yields
   \[
   \widehat P_{\rm connector}
   \ge \mathfrak b_{\rm neck}-\mathfrak b_{\rm inner}
   >p_\star.
   \]

3. **Only if large shear is allowed**, minimize the exact action (17). Treat
   \[
   X=(h,\beta,q,h',\beta',q')
   \]
   as state and \((H,E,D)\) as controls:
   \[
   \begin{aligned}
   q''&=-3h'q'+V_D-D,\\
   \beta''&=-3h'\beta'+V_E-E,\\
   h''&=-\frac12H-\frac13(\beta')^2-\frac14(q')^2+\frac12V_H.
   \end{aligned}
   \tag{21}
   \]
   A minimal witness search uses one or two cubic-Hermite segments joining:
   * a homothetically rescaled point of the Rossi Einstein trajectory;
   * an exact CH state;
   * optionally an internal collapsed orbit with \(h'=0\).

   The free dimension can be kept to roughly seven parameters:
   \[
   T_-,\,T_+,\,L,\,
   h_0,\,\beta_0,\,q_0,\,
   \text{one scale/matching parameter}.
   \]
   Curvature must be evaluated from (16), not by finite differences.

For a lower-bound proof on the residual domain, use a Hamilton–Jacobi subsolution \(V(X)\):
\[
\nabla V\cdot F(X;H,E,D)
\le
e^{3h}\left(
\frac{3}{16}H^2+\frac16E^2+\frac18D^2
\right).
\tag{22}
\]
The controls are quadratic and can be minimized analytically, leaving an interval-verifiable inequality in the six state variables.

---

## Resulting conclusion

A genuine Taub-bolt/ALF core can have negligible \(\widehat P\), but its ALF end has \(\mathfrak b\to0\). Therefore it cannot be connected cheaply to a sufficiently developed Rossi ACH orbit carrying large negative Euler flux. Collapse does not erase this charge because the flux and action are scale invariant.

Accordingly, the unresolved object is now precise: a sub-\(0.99584841\) connector, if it exists at all, must avoid every quasi-product and ALF Berger regime and realize a highly sheared singular trajectory of the six-dimensional controlled system (21). The endpoint Euler-flux interval computation is the cheapest test and is likely to exclude the intended Berger/ALF connector immediately; only then is the low-dimensional Hermite optimization of (17) warranted.