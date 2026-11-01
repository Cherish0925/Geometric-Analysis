# TTCS Independent Branch Record

```json
{
  "step_id": 71,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/Poincaré-Einstein-4-manifolds-with-cusps--d36d062e94d0--09d8ca1fbe38/object.md",
    "Sessions/S0910A03/workspace/notes/step69_anisotropic_cusp_compensation.md",
    "Sessions/S0910A03/workspace/notes/step70_critical_identity_and_corrections.md",
    "Sessions/S0910A01/workspace/notes/step72_graph_neck_weighted_shear_budget.md"
  ]
}
```

## Task

Analyze the Li–Liu Type-I equation relevant to T^2-compatible anisotropic quotients. The source equation is (e^v)_{xi xi}+Delta_{T^2}v=0, with W=1-(xi/2)v_xi. For a one-angular-variable reduction v(xi,theta), derive the correct nonlinear PDE, its linearization around a constant bounded AH-cusp solution, Fourier radial branches, the slice-average conservation law, and the reflection/totally-geodesic condition translated into the Li–Liu metric variables if possible. Decide whether their BVP1 family can contain a totally geodesic T^3 level or whether Proposition 6.6/global geometry rules it out. Identify a mathematically meaningful finite-cylinder approximate matching experiment that preserves the nonlinear equation and quotient symmetry, without claiming it solves the full graph gluing.

## Output

## Scientific memo

### 1. One-angular-variable Toda equation

Take flat coordinates
\[
g_{T^2}=d\theta^2+dy^2,\qquad \theta\in \mathbb R/P\mathbb Z,
\]
and assume \(v=v(\xi,\theta)\), independent of \(y\). Li–Liu’s Type-I equation becomes
\[
\boxed{(e^v)_{\xi\xi}+v_{\theta\theta}=0.}
\]
Equivalently,
\[
\boxed{e^v\bigl(v_{\xi\xi}+v_\xi^2\bigr)+v_{\theta\theta}=0,}
\qquad
v_{\xi\xi}+v_\xi^2+e^{-v}v_{\theta\theta}=0.
\]
The \(v_\xi^2\) term is essential. For bounded \(v\), the principal coefficients \(e^v\) and \(1\) are uniformly positive, so this is elliptic in \((\xi,\theta)\).

If the \(\theta\)-part of the flat metric is \(a^2d\theta^2\), replace \(v_{\theta\theta}\) by \(a^{-2}v_{\theta\theta}\).

### 2. Linearization and Fourier radial branches

A constant solution
\[
v\equiv v_0,\qquad W=1
\]
gives the real-hyperbolic cusp metric
\[
h_0=\xi^{-2}\left(d\xi^2+d\tau^2+e^{v_0}(d\theta^2+dy^2)\right).
\]

Writing \(v=v_0+\varepsilon u+O(\varepsilon^2)\), the linearized equation is
\[
e^{v_0}u_{\xi\xi}+u_{\theta\theta}=0.
\]
For
\[
u(\xi,\theta)=a_m(\xi)e^{i\kappa_m\theta},
\qquad
\kappa_m=\frac{2\pi m}{P},
\]
one obtains
\[
a_m''-\mu_m^2a_m=0,
\qquad
\mu_m=e^{-v_0/2}|\kappa_m|.
\]
Thus
\[
a_m(\xi)=A_me^{\mu_m\xi}+B_me^{-\mu_m\xi},\qquad m\ne0,
\]
while
\[
a_0(\xi)=A_0+B_0\xi.
\]
On the BVP1 half-cylinder, boundedness removes \(e^{+\mu_m\xi}\) and the affine zero-mode slope. Hence every nonzero Fourier mode decays exponentially in \(\xi\). Nonlinear products generate the zero mode and harmonics \(2m,3m,\dots\), so a single-mode truncation is not preserved by the exact equation.

The first variation of \(W\) is
\[
\delta W=-\frac{\xi}{2}u_\xi.
\]
For the decaying branch \(u=Ce^{-\mu\xi}\cos(\kappa\theta)\),
\[
\delta W=\frac{\mu\xi}{2}Ce^{-\mu\xi}\cos(\kappa\theta).
\]

### 3. Slice-average conservation and bundle degree

Let
\[
F(\xi)=\int_{S^1}e^{v(\xi,\theta)}\,d\theta .
\]
Integration of the Toda equation gives
\[
\boxed{F''(\xi)=0,\qquad F(\xi)=c_1\xi+c_0.}
\]
For a bounded BVP1 solution, \(F\) is bounded, hence
\[
\boxed{c_1=0,\qquad F(\xi)\equiv F(0).}
\]
The conserved quantity is the average of \(e^v\), not the average of \(v\).

Furthermore,
\[
\int_{S^1}We^v\,d\theta
 =F-\frac{\xi}{2}F'
 =c_0+\frac{c_1}{2}\xi.
\]
Therefore
\[
\frac{d}{d\xi}\int_{S^1}We^v\,d\theta=\frac{c_1}{2}.
\]
Together with Li–Liu equation (14), this shows that BVP1 has circle-bundle degree zero. Its links are \(T^3\), even though the connection curvature need not vanish pointwise.

### 4. Connection and shape operator of a \(\xi\)-level

With \(x=\theta\), Li–Liu equation (13) reduces to
\[
d\eta=(We^v)_\xi\,d\theta\wedge dy
      +W_\theta\,dy\wedge d\xi.
\]
In radial gauge one may write
\[
\eta=d\tau+A(\xi,\theta)\,dy,
\]
where
\[
A_\theta=(We^v)_\xi,\qquad A_\xi=-W_\theta.
\]
The integrability relation is precisely a consequence of the Toda equation.

The metric induced on \(\{\xi=\mathrm{const}\}\) is
\[
q_\xi=\xi^{-2}\left(W^{-1}\eta^2+We^v(d\theta^2+dy^2)\right),
\]
and a unit normal is
\[
N=\frac{\xi}{\sqrt W}\,\partial_\xi.
\]
Set
\[
\alpha=\frac{\xi W_\xi}{W},\qquad
p=\xi v_\xi=2(1-W),\qquad
\beta=-\frac{\xi W_\theta}{2W^{3/2}e^{v/2}}.
\]
In the orthonormal frame adapted to the fiber, \(\theta\), and \(y\), the shape operator is
\[
S=
\begin{pmatrix}
\dfrac{-2-\alpha}{2\sqrt W}&0&\beta\\[2mm]
0&\dfrac{-2+\alpha+p}{2\sqrt W}&0\\[2mm]
\beta&0&\dfrac{-2+\alpha+p}{2\sqrt W}
\end{pmatrix},
\]
up to reversing the overall normal orientation.

A totally geodesic level would require
\[
-2-\alpha=0,\qquad -2+\alpha+p=0,\qquad \beta=0.
\]
The first two equations give \(p=4\), but then
\[
W=1-\frac p2=-1,
\]
which is incompatible with a Riemannian Type-I metric. Thus:

\[
\boxed{\text{No Riemannian Li–Liu Type-I metric has a totally geodesic }\xi\text{-level}.}
\]

There is also a quantitative identity:
\[
|S|^2
=\frac{(\alpha+2)^2+2(\alpha-2W)^2}{4W}+2\beta^2
\ge \frac{2}{3}\frac{(1+W)^2}{W}
\ge \boxed{\frac83}.
\]
Consequently anisotropic lattice quotients do not make these coordinate levels nearly geodesic; they alter volume but leave this local norm unchanged.

### 5. No tilted totally geodesic \(T^3\) either

BVP1 metrics are Type I, hence \(W_h^+=0\). Suppose a compact \(T^3\subset M\) were totally geodesic, with unit normal \(\nu\). Codazzi gives
\[
R_h(\nu,X,Y,Z)=0.
\]
Since \(\operatorname{Ric}_h=-3h\), the constant-curvature part has no component of this form, so
\[
W_h(\nu,X,Y,Z)=0.
\]
Let
\[
E_{ij}=W_{\nu i\nu j},\qquad
B_{ij}=\frac12\varepsilon_i{}^{kl}W_{\nu jkl}.
\]
Codazzi gives \(B=0\). In four dimensions, \(W^+=0\) identifies \(E\) with \(\pm B\), depending on orientation convention. Hence \(E=0\), and therefore \(W=0\) along the hypersurface.

The Gauss equation then gives sectional curvature \(-1\) for the induced three-metric. A compact \(T^3\) cannot carry such a metric. Therefore the Type-I family contains no totally geodesic \(T^3\), whether or not it is a \(\xi\)-level.

Proposition 6.6 is not the general reason. For the nonflat BVP1 conformal infinities, source Lemma 6.8 gives \(Y<0\), whereas Proposition 6.6 assumes \(Y\ge0\). In the flat case Proposition 6.6 yields the rigid metric
\[
h=ds^2+e^{-2s}q_{\mathrm{flat}},
\qquad s=\log\xi,
\]
which is exactly the constant-\(v\) solution. Its levels have \(S=\pm I\), never \(S=0\).

### 6. A finite-cylinder nonlinear matching experiment

A useful exact Toda experiment is the following. Normalize the lower trace by
\[
\phi_\varepsilon(\theta)
 =v_0+\varepsilon\cos(m\theta)-\log I_0(\varepsilon),
\]
so that
\[
\frac1{2\pi}\int_0^{2\pi}e^{\phi_\varepsilon}\,d\theta=e^{v_0}.
\]
For \(L>0\), solve
\[
\begin{cases}
(e^v)_{\xi\xi}+v_{\theta\theta}=0,
       &0<\xi<L,\\
v(0,\theta)=\phi_\varepsilon(\theta),\\
v(L,\theta)=v_0.
\end{cases}
\]
This is the finite-cylinder problem used in Li–Liu Proposition 5.3 after normalization. Equal exponential averages at the two endpoints force
\[
\int e^v\,d\theta\equiv 2\pi e^{v_0}.
\]
For fixed \(L\) and sufficiently small \(\varepsilon\), elliptic perturbation theory gives \(W>0\), so \(W\) and \(\eta\) reconstruct an exact Einstein collar.

At first order,
\[
v-v_0
=\varepsilon
\frac{\sinh(\mu(L-\xi))}{\sinh(\mu L)}
\cos(m\theta)+O(\varepsilon^2),
\qquad
\mu=|m|e^{-v_0/2},
\]
and hence
\[
v_\xi(L,\theta)
=-\varepsilon\frac{\mu}{\sinh(\mu L)}\cos(m\theta)
\]
to first order, while
\[
W(L,\theta)-1
=\varepsilon\frac{L\mu}{2\sinh(\mu L)}
\cos(m\theta).
\]
Thus the upper level approaches standard cusp data at an exponentially small rate, with polynomial factors in \(L\) arising from \(W=1-\xi v_\xi/2\).

The geometrically relevant output is
\[
\mathcal M_L=
\|q_L-q_L^{\mathrm{cusp}}\|_{C^2}
+\|S_L+I\|_{C^1}
+\|d\eta_L\|_{C^1},
\]
after matching the constant holonomy of \(\eta\). A cutoff attachment to the standard cusp should then be evaluated directly through
\[
\|\operatorname{Ric}+3h\|_{\mathrm{op},\infty},
\]
including the first two normal jets, rather than only through the Toda residual.

Because all coefficients are independent of \((\tau,y)\), integer quotients in those two translation directions preserve the nonlinear equation and all local curvature quantities while reducing interface volume. This directly tests anisotropy damping and cusp matching. Its output is an exact Type-I Einstein collar plus a quantified terminal attachment; it provides neither a reflection center nor the closed graph-manifold assembly.