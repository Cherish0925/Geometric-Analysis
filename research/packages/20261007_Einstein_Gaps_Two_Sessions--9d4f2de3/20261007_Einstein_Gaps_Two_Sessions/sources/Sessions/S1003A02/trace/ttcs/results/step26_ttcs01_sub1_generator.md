# TTCS Independent Branch Record

```json
{
  "step_id": 26,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md",
    "Sessions/S1003A02/workspace/scripts/cr_pinning_check.py",
    "Sessions/S1003A02/workspace/scripts/squash_escape_cost.py",
    "Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md"
  ]
}
```

## Task

Develop a mathematically decisive model for the collapsed curved/ Berger connector in the diagonal O(-1) cell problem. The target configuration is an inner ACH Einstein region with Rossi parameter log rho≈0.784, a small orbit-volume W neck across which the CR variable changes to zero, and an exact complex-hyperbolic exterior. Use Lemma P together with four-dimensional Chern–Weil/signature transgression, Bianchi-IX curvature, eta-invariant or Berger-sphere boundary terms, and the existing almost-Euclidean neck quantization as appropriate. Seek either (i) a lower-bound mechanism charging every such curved connector enough to exclude cost below the certified 0.99585, or (ii) a concrete low-dimensional variational ansatz likely to beat it. State equations, scaling regimes, topological conditions, and the cheapest distinguishing computation/proof. Avoid generic brainstorming.

## Output

## A transgression–optimal-control model for the collapsed connector

Let  
\[
p_\star=0.99584841,\qquad P=8\pi^2\widehat P,
\]
and write the diagonal metric as
\[
g=dt^2+a_f^2\sigma_f^2+a_g^2\sigma_g^2+a_h^2\sigma_h^2,\qquad
W=a_fa_ga_h,\qquad y_i=\frac{a_i'}{a_i}.
\]
The intended cell has an \(O(-1)\) bolt, hence every principal orbit separating the bolt from the CH exterior is an \(S^3\) with the weight-one Hopf marking. The inner piece has \((\chi,\tau)=(2,-1)\); every connector between two principal orbits has \((\chi,\tau)=(0,0)\).

The useful model has two complementary parts:

1. a scale-invariant Chern–Weil flux pair attached to every principal orbit;
2. an exact three-function optimal-control representation of \(\widehat P\).

Together they distinguish an ordinary Berger/ALF collapse from a high-shear singular transition.

---

### 1. Euler transgression gives a scale-invariant charge

For the induced left-invariant metric on \(\Sigma_t\cong S^3\), let \(K_{jk}^{(3)}\) denote the sectional curvature of the \(jk\)-plane. With \(\{i,j,k\}=\{f,g,h\}\),
\[
K_{jk}^{(3)}
=
\frac{(a_j^2-a_k^2)^2+2a_i^2(a_j^2+a_k^2)-3a_i^4}
     {a_i^2a_j^2a_k^2}.
\]
Define the normalized Euler flux
\[
\boxed{\;
\mathfrak b(t)
=
W\left(
y_fK_{gh}^{(3)}+y_gK_{hf}^{(3)}+y_hK_{fg}^{(3)}
-y_fy_gy_h
\right).
\;} \tag{1}
\]
The Chern–Gauss–Bonnet hypersurface term is \(4\pi^2\mathfrak b\). In particular, a round Euclidean sphere has \(\mathfrak b=2\), while a small tube around a smooth weight-one bolt has \(\mathfrak b\to4\).

For an annulus \(C=[t_0,t_1]\times S^3\), Chern–Gauss–Bonnet gives the exact identity
\[
\boxed{\;
\widehat P(C)
=
\mathfrak b(t_1)-\mathfrak b(t_0)
+\frac1{4\pi^2}\int_C|W_g|^2
+\frac1{96\pi^2}\int_Cs_g^2.
\;} \tag{2}
\]
Consequently,
\[
\widehat P(C)\ge \mathfrak b(t_1)-\mathfrak b(t_0). \tag{3}
\]
No scalar normalization is used here. A common homothety leaves \(\mathfrak b\) unchanged because \(W\), \(y_i\), and \(K_{jk}^{(3)}\) scale as length\(^{3}\), length\(^{-1}\), and length\(^{-2}\).

For exact CH,
\[
a_f=\sinh t\cosh t,\qquad a_g=a_h=\sinh t,
\]
and direct substitution gives
\[
\boxed{\;
\mathfrak b_{\rm CH}(t)=2-6\sinh^4t.
\;} \tag{4}
\]
Thus the large-radius CH flux is very far below zero even though the physical orbit can be made small by an overall rescaling.

For an ACH state with
\[
\kappa=\frac{a_f}{a_ga_h},\qquad
\zeta=\frac1{a_ga_h},\qquad
(y_f,y_g,y_h)=(2,1,1)+o(1),
\]
one obtains, uniformly for \(q\) in a compact interval,
\[
\boxed{\;
\mathfrak b
=
-\kappa(4\kappa^2+2)\zeta^{-2}+O(\zeta^{-1}).
\;} \tag{5}
\]
Near the Einstein curve \(\kappa=1\), this is
\[
\mathfrak b=-6\zeta^{-2}+O(\zeta^{-1}).
\]
Hence a developed Rossi ACH region carries a huge Euler-flux debt. Rescaling that region does not change the debt.

This immediately charges the standard collapsed models. If \(\Sigma_-\) lies in the inner ACH region and \(\Sigma_0\) is a later quasi-product Berger or ALF neck with \(\mathfrak b(\Sigma_0)=o(1)\), then
\[
\widehat P([\Sigma_-,\Sigma_0])
\ge -\mathfrak b(\Sigma_-)-o(1). \tag{6}
\]
Already \(\mathfrak b(\Sigma_-)\le-1\) is enough to exceed the certified value.

The existing block at \(\zeta=10^{-2}\), \(q\in[0.7,0.9]\), has
\[
|\widetilde\Phi(\infty)-\widetilde\Phi(T)|
\le
\frac{19.58}{2(1.998)}10^{-4}
<4.91\times10^{-4}.
\]
Thus it represents \(\log\rho\simeq0.784\) to better than \(5\times10^{-4}\). Formula (5) places its Euler flux at order \(-6\times10^4\). The exact interval evaluation of (1) on the already validated state box is the least expensive decisive calculation; no integration of a connector is required.

---

### 2. Signature transgression strengthens the flux estimate

Fix the Hopf framing induced from the \(O(-1)\) bolt and let \(\vartheta(t)\) be the normalized Pontryagin/Chern–Simons flux satisfying
\[
\frac1{12\pi^2}\int_{U_t}
\bigl(|W^+|^2-|W^-|^2\bigr)
=
\tau(U_t)+\vartheta(t). \tag{7}
\]
For an annulus,
\[
\int_C(|W^+|^2-|W^-|^2)
=
12\pi^2\bigl(\vartheta(t_1)-\vartheta(t_0)\bigr).
\]
Combining this with (2) yields
\[
\boxed{\;
\widehat P(C)
\ge
\mathfrak b(t_1)-\mathfrak b(t_0)
+
3\bigl|\vartheta(t_1)-\vartheta(t_0)\bigr|.
\;} \tag{8}
\]
For the inner region \(U_t\), where \((\chi,\tau)=(2,-1)\),
\[
\boxed{\;
\widehat P(U_t)
\ge
3|-1+\vartheta(t)|+\mathfrak b(t)-4.
\;} \tag{9}
\]
At the bolt, \((\mathfrak b,\vartheta)\to(4,1)\), making the right side zero. At an almost-Euclidean enclosing sphere,
\[
(\mathfrak b,\vartheta)=(2,0)+O(\varepsilon),
\]
and (9) becomes
\[
\widehat P(U_t)\ge1-O(\varepsilon),
\]
which is precisely the almost-Euclidean neck quantization.

For exact CH, the chosen normalization gives
\[
\vartheta_{\rm CH}(t)=\sinh^4t,\qquad
\mathfrak b_{\rm CH}(t)=2-6\sinh^4t. \tag{10}
\]
Indeed the Weyl and scalar terms in (2) each contribute \(3\sinh^4t\), cancelling the change in \(\mathfrak b\).

When the second fundamental form vanishes, \(\vartheta\) is the APS odd-signature eta term of the induced Berger metric, with the integer fixed by the Hopf framing. For a general neck it is better to compute \(\vartheta(a_i,y_i)\) directly from
\[
\operatorname{CS}(\omega)
=
\operatorname{tr}\left(\omega\wedge d\omega+\frac23\omega^3\right),
\]
using
\[
\omega_{i0}=y_i e^i,\qquad
\omega_{ij}
=
\frac{a_i^2+a_j^2-a_k^2}{a_ia_ja_k}\,e^k
\]
with cyclic signs. This avoids the several eta normalizations used in the literature. If an intrinsic formula is desired, the exact source topic is “APS/Hitchin odd-signature eta invariant of the Berger three-sphere with \(d\sigma_i=2\sigma_j\wedge\sigma_k\).”

A useful figure is the path
\[
t\longmapsto\bigl(\mathfrak b(t),\vartheta(t)\bigr).
\]
From an inner orbit \((\mathfrak b_-,\vartheta_-)\), every connector with cost below \(p_\star\) must remain inside
\[
\mathfrak b-\mathfrak b_-+3|\vartheta-\vartheta_-|<p_\star. \tag{11}
\]
The quasi-product Berger curve has \(\mathfrak b\simeq0\); the almost-Euclidean point is \((2,0)\); the CH curve is given by (10). Separation in this flux plane proves the desired charge without solving the fourth-order variational equations.

---

### 3. Ordinary Berger and ALF necks are charged

For a biaxial orbit
\[
a_g=a_h=A,\qquad a_f=B,\qquad \lambda=\frac BA,
\]
put
\[
U=A\frac{A'}A=A',\qquad V=A\frac{B'}B.
\]
Formula (1) reduces to
\[
\boxed{\;
\mathfrak b
=
\lambda\Bigl[
V(4-3\lambda^2-U^2)+2U\lambda^2
\Bigr].
\;} \tag{12}
\]

Three cases follow.

* **Product Berger neck:** \(U,V\simeq0\), hence \(\mathfrak b\simeq0\).
* **ALF Taub-bolt-type end:** \(A\sim R\), \(B\to m\), so \(\lambda\to0\), \(U\to1\), \(V\to0\), and again \(\mathfrak b\to0\).
* **Almost-Euclidean neck:** \(\lambda,U,V\to1\), giving \(\mathfrak b\to2\), and (9) gives the unit charge.

More generally, let \(r=W^{1/3}\), \(\widehat y_i=ry_i\), and \(\widehat K_{jk}=r^2K_{jk}^{(3)}\). If a curved product neck satisfies
\[
|\widehat y_i|\le\varepsilon,\qquad
|\widehat K_{jk}|\le K_0,
\]
then
\[
\mathfrak b\ge-3K_0\varepsilon-\varepsilon^3. \tag{13}
\]
Thus every such connector is excluded whenever
\[
-\mathfrak b(\Sigma_-)
>
p_\star+3K_0\varepsilon+\varepsilon^3. \tag{14}
\]
For the developed ACH block, the left side is of order \(\zeta^{-2}\), so (14) has an enormous margin.

The only remaining geometry is a neck with large scale-normalized second fundamental form, arranged so that \(\mathfrak b\) stays as low as the inner ACH value. That is not an ALF or quasi-product Berger neck; it is a high-shear singular transition. Its cost is captured exactly by the next model.

---

### 4. Exact three-function action for all diagonal connectors

Introduce volume and shape variables
\[
a_f=r\,e^{2\beta/3},\qquad
a_g=r\,e^{-\beta/3+q/2},\qquad
a_h=r\,e^{-\beta/3-q/2},
\qquad h=\log r.
\]
Then \(W=r^3\), \(\beta=\log(a_f/\sqrt{a_ga_h})\), and \(q=\log(a_g/a_h)\).

Let
\[
D=R_{gg}-R_{hh},
\qquad
E=R_{ff}-\frac{R_{gg}+R_{hh}}2,
\qquad
H=R_{00}-\frac{R_{ff}+R_{gg}+R_{hh}}3.
\]
Using the Bianchi-IX curvature potentials from the session, one obtains
\[
\begin{aligned}
D={}&-q''-3h'q'
+8e^{-2h}\left(
e^{-4\beta/3}\sinh 2q-e^{2\beta/3}\sinh q
\right),\\[1mm]
E={}&-\beta''-3h'\beta'
+e^{-2h}\left(
4e^{8\beta/3}-4e^{2\beta/3}\cosh q
-8e^{-4\beta/3}\sinh^2q
\right),\\[1mm]
H={}&-2h''-\frac23(\beta')^2-\frac12(q')^2\\
&\quad
+e^{-2h}\left(
\frac23e^{8\beta/3}
-\frac83e^{2\beta/3}\cosh q
+\frac83e^{-4\beta/3}\sinh^2q
\right).
\end{aligned} \tag{15}
\]
The orthogonal Ricci decomposition gives the exact action
\[
\boxed{\;
\widehat P
=
\int r^3\left(
\frac{3}{16}H^2+\frac16E^2+\frac18D^2
\right)dt.
\;} \tag{16}
\]
This is not merely a reduced lower estimate: it is the full diagonal \(\widehat P\).

Under
\[
t=\varepsilon x,\qquad r(t)=\varepsilon R(x),
\]
the quantities \(D,E,H\) scale as \(\varepsilon^{-2}\), while \(r^3dt\) scales as \(\varepsilon^4\). Therefore (16) is exactly scale invariant. Sending the neck volume to zero does not send its action to zero; it produces a fixed dimensionless variational problem.

Equation (15) also shows why extreme Berger collapse does not freely transport Rossi anisotropy. If \(B/A=e^\beta\to0\), then
\[
D\supset 8e^{-2h-4\beta/3}\sinh 2q,
\]
and
\[
H\supset \frac83e^{-2h-4\beta/3}\sinh^2q.
\]
Finite subunit action forces \(q\to0\) before strong Hopf collapse, unless \(q'\) and \(q''\) follow a singular Einstein cancellation. Such cancellation drives the geometry into the high-shear branch, where \(E\) and \(H\) control the smoothing needed to return to a regular CH orbit.

Lemma P appears here as the \(D\)-channel:
\[
\widetilde\Phi'=\zeta^2G-\frac14D,
\]
hence on a connector \(C\),
\[
\boxed{\;
\widehat P(C)\ge
\frac{2\left(
\Delta\widetilde\Phi-\int_C\zeta^2G\,dt
\right)^2}
{\displaystyle\int_C\frac{dt}{r^3}}.
\;} \tag{17}
\]
Collapse makes the denominator large, but then the reset must be supplied by the Einstein drift \(\zeta^2G\). Equations (15)–(16) charge the volume and shape excursion needed to create that drift. Thus (17) and (16) separate the two apparent escape mechanisms rather than duplicating each other.

---

### 5. The least expensive decisive computation

For the intended Rossi filling, the shortest route is:

1. Evaluate \(\mathfrak b\) and \(\vartheta\) by interval arithmetic on the existing validated Einstein state box at the first orbit where
   \[
   |\widetilde\Phi-\log\rho|\le5\times10^{-4}.
   \]
   Formula (5) predicts \(\mathfrak b\) of order \(-6\times10^4\) at \(\zeta=10^{-2}\).

2. Evaluate \((\mathfrak b,\vartheta)\) on the proposed Berger neck box. For a product or ALF neck, \(\mathfrak b=o(1)\). Then (8) already gives a connector cost far above \(p_\star\).

3. If the neck is allowed to retain very large normalized shear, solve the six-dimensional controlled system obtained from (15):
   \[
   \begin{aligned}
   q''&=-3h'q'+V_D-D,\\
   \beta''&=-3h'\beta'+V_E-E,\\
   h''&=-\frac12H-\frac13(\beta')^2-\frac14(q')^2+\frac12V_H,
   \end{aligned}
   \]
   with running action (16). The state is
   \[
   X=(h,\beta,q,h',\beta',q'),
   \]
   and the controls are \((H,E,D)\).

A very small witness search is obtained by taking \(h,\beta,q\) as cubic Hermite interpolants between:

* a homothetically scaled inner Einstein state at truncation \(T_-\);
* an exact CH state at \(T_+\).

After removing the fixed CH scale, the free parameters are
\[
T_-,\quad T_+,\quad \log\varepsilon_{\rm inner},\quad L.
\]
A second Hermite segment with an internal condition \(h'=0\) adds an explicit volume neck and only three shape parameters \((h_0,\beta_0,q_0)\). The action is then evaluated from (16), not from finite-difference curvature.

For a proof covering the high-shear branch, the same controlled system admits a Hamilton–Jacobi subsolution \(V(X)\):
\[
\nabla V(X)\cdot F(X;H,E,D)
\le
e^{3h}\left(\frac{3}{16}H^2+\frac16E^2+\frac18D^2\right)
\]
for all controls. Minimizing the right side analytically in \((H,E,D)\) leaves an interval-verifiable inequality in the six state variables. Endpoint evaluation of \(V\) then supplies a certified lower value.

The transgression calculation is expected to settle every genuine Berger/ALF connector immediately. Only a singular high-shear path can evade the simple flux rise, and that residual path is represented exactly by the scale-invariant action (16). A Ricci-flat Taub-bolt core itself costs no \(P\), but its ALF end has \(\mathfrak b\to0\); connecting it to a developed Rossi ACH state must repay the large Euler and signature flux carried by that state.