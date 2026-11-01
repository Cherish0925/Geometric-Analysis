# TTCS Independent Branch Record

```json
{
  "step_id": 16,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step15_L2_chain_and_separated_demands.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Independently analyze the proposed exponential-pullback chart averaging lemma in dimension four. Let (M,g) be closed with |sec_g|<=K on a buffered region U, fix 0<r<min(buffer, pi/(2 sqrt K)) so exp_p^*g is nonsingular on B_r(0) subset T_pM for every p in a positive-volume set P whose r-geodesics remain in U. For nonnegative measurable F supported in U, determine whether one can prove

∫_P [Vol_{exp_p^*g}(B_r(0))^{-1} ∫_{B_r(0)} F(exp_p v) dμ_{exp_p^*g}(v)] dμ_g(p) <= C(n,K,r) ∫_U F dμ_g,

with no injectivity-radius or sheet-number assumption. Give a rigorous derivation or counterexample. Track polar-coordinate Jacobians, the v=0 singularity, conjugate-radius assumptions, Liouville/geodesic-flow invariance, and normalization of pullback-ball volume. Also explain what curvature-derivative bounds are needed for smooth compactness of these exponential charts. This is for a collapsed near-Einstein four-manifold route; do not assume CFG or local covers.

## Output

# Scientific memo: exponential-pullback averaging

## 1. Result

The proposed estimate is valid without any injectivity-radius or sheet-count hypothesis.

Extend \(F\) by zero from \(U\) to \(M\). For \(K>0\), define
\[
\mathfrak s_K(t)=\frac{\sin(\sqrt K\,t)}{\sqrt K},
\qquad
\mathfrak s_{-K}(t)=\frac{\sinh(\sqrt K\,t)}{\sqrt K},
\]
and use \(\mathfrak s_0(t)=t\). Then
\[
\boxed{
\int_P
\frac{\displaystyle\int_{B_r(0)}F(\exp_pv)\,d\mu_{\exp_p^*g}(v)}
{\displaystyle\operatorname{Vol}_{\exp_p^*g}(B_r(0))}
\,d\mu_g(p)
\le
C_n(K,r)\int_UF\,d\mu_g
}
\]
with
\[
C_n(K,r)=
\frac{\displaystyle\int_0^r \mathfrak s_{-K}(t)^{n-1}\,dt}
{\displaystyle\int_0^r \mathfrak s_K(t)^{n-1}\,dt}.
\]
In particular,
\[
C_n(K,r)\le
\left(\frac{\sinh(\sqrt K r)}{\sin(\sqrt K r)}\right)^{n-1},
\]
with value \(1\) when \(K=0\).

For \(n=4\), putting \(x=\sqrt K r\),
\[
C_4(K,r)=
\frac{\cosh^3x-3\cosh x+2}
{2-3\cos x+\cos^3x}
\le
\left(\frac{\sinh x}{\sin x}\right)^3.
\]

The positivity of \(\operatorname{Vol}(P)\) is not needed for the inequality itself; it matters when the estimate is used to select a basepoint.

---

## 2. Polar Jacobian of the pullback metric

Fix \(p\in P\), \(\theta\in S_pM\), and write
\[
\gamma_{p,\theta}(t)=\exp_p(t\theta).
\]
Let
\[
A_{p,\theta}(t):\theta^\perp\longrightarrow \dot\gamma(t)^\perp
\]
be the radial Jacobi tensor:
\[
A(0)=0,\qquad D_tA(0)=I,\qquad
D_t^2A+R(\,\cdot\,,\dot\gamma)\dot\gamma\circ A=0.
\]
Because \(d\exp_p\) is nonsingular for \(0<t<r\), its determinant has fixed sign, and the polar-coordinate density of
\[
h_p=\exp_p^*g
\]
is
\[
J_p(t,\theta)=\det A_{p,\theta}(t)>0.
\]
Thus
\[
d\mu_{h_p}=J_p(t,\theta)\,dt\,d\sigma_p(\theta).
\]

The Rauch comparison theorem, using
\[
-K\le \sec_g\le K
\]
along the selected radial segments, gives
\[
\mathfrak s_K(t)|\xi|
\le |A_{p,\theta}(t)\xi|
\le \mathfrak s_{-K}(t)|\xi|
\]
for \(\xi\in\theta^\perp\). Hence every singular value of \(A\) lies between these two model values, so
\[
\boxed{
\mathfrak s_K(t)^{n-1}
\le J_p(t,\theta)
\le \mathfrak s_{-K}(t)^{n-1}.
}
\]

The polar parametrization is singular at \(t=0\), but the pullback metric is smooth there because \(d\exp_p|_0=I\). More precisely,
\[
A_{p,\theta}(t)=tI+O(t^3),\qquad
J_p(t,\theta)=t^{n-1}(1+O(t^2)).
\]
Thus the Cartesian density \(J_p(t,\theta)/t^{n-1}\) tends to \(1\). The point \(v=0\) has zero measure, so arbitrary measurable values of \(F(p)\) cause no extra term.

The upper sectional estimate also places the first conjugate time at or after \(\pi/\sqrt K\). Thus, when every relevant geodesic remains in \(U\), the nonsingularity assumption already follows from \(r<\pi/\sqrt K\). The stricter radius \(r<\pi/(2\sqrt K)\) gives a uniform margin and
\[
\frac{\mathfrak s_K(t)}t\ge \frac2\pi.
\]
Cut points created by short loops can occur much earlier on a collapsed manifold, but they affect injectivity of \(\exp_p\), not nonsingularity of its differential.

---

## 3. Pullback-ball volume normalization

Set
\[
V_p=\operatorname{Vol}_{h_p}(B_r(0)).
\]
The lower Jacobian comparison gives
\[
V_p
=\int_{S_pM}\int_0^rJ_p(t,\theta)\,dt\,d\sigma_p(\theta)
\ge
\omega_{n-1}\int_0^r\mathfrak s_K(t)^{n-1}\,dt,
\]
where \(\omega_{n-1}=\operatorname{Vol}(S^{n-1})\).

Consequently,
\[
\frac1{V_p}
\le
\frac1{\omega_{n-1}\int_0^r\mathfrak s_K(t)^{n-1}\,dt}.
\]
This is the essential normalization fact: even when the physical ball in \(M\) has very small volume, the exponential pullback ball has volume uniformly comparable to \(r^n\). It counts all tangent-domain sheets separately.

Here \(B_r(0)\) is the radial vector ball \(\{|v|_{g_p}<r\}\). For \(h_p\), radial lines are geodesics and \(\exp^{h_p}_0\) is the identity on this vector domain.

---

## 4. Liouville invariance and the averaged numerator

Define
\[
N_p=\int_{B_r(0)}F(\exp_pv)\,d\mu_{h_p}(v).
\]
Using the upper Jacobian estimate,
\[
N_p
\le
\int_0^r\mathfrak s_{-K}(t)^{n-1}
\int_{S_pM}F(\gamma_{p,\theta}(t))\,d\sigma_p(\theta)\,dt.
\]

Let \(SM\) be the unit tangent bundle, \(\pi:SM\to M\) its projection, and \(\phi_t\) the geodesic flow. Its Liouville measure is
\[
dL(z)=d\mu_g(p)\,d\sigma_p(\theta),
\qquad z=(p,\theta),
\]
and \(\phi_t\) preserves \(dL\). Therefore
\[
\begin{aligned}
\int_{SM}F(\pi\phi_tz)\,dL(z)
&=\int_{SM}F(\pi z)\,dL(z)\\
&=\omega_{n-1}\int_MF\,d\mu_g\\
&=\omega_{n-1}\int_UF\,d\mu_g.
\end{aligned}
\]

Since \(F\ge0\), the integral over \(SM|_P=\pi^{-1}(P)\) is bounded by the integral over all \(SM\). Tonelli’s theorem then gives
\[
\begin{aligned}
\int_PN_p\,d\mu_g(p)
&\le
\int_0^r \mathfrak s_{-K}(t)^{n-1}
\int_{SM|_P}F(\pi\phi_tz)\,dL(z)\,dt\\
&\le
\omega_{n-1}
\left(\int_0^r\mathfrak s_{-K}(t)^{n-1}\,dt\right)
\int_UF\,d\mu_g.
\end{aligned}
\]
Combining this with the uniform lower estimate for \(V_p\) yields the stated constant.

No curvature information outside the selected radial segments is inserted into this step. After replacing \(J_p\) by its model upper estimate, the restricted unit-tangent integral is simply enlarged to all of \(SM\), where global geodesic-flow invariance applies.

---

## 5. Why arbitrary sheet multiplicity causes no extra factor

For fixed \(p\), the map
\[
\exp_p:B_r(0)\to M
\]
may revisit the same point many times. The pullback integral counts every preimage. A direct area-formula rewrite would therefore contain a multiplicity function.

The geodesic-flow argument avoids estimating that multiplicity. Although
\[
(p,\theta)\longmapsto \gamma_{p,\theta}(t)
\]
may be many-to-one after forgetting the terminal direction, the full map
\[
(p,\theta)\longmapsto
\bigl(\gamma_{p,\theta}(t),\dot\gamma_{p,\theta}(t)\bigr)
=\phi_t(p,\theta)
\]
is a bijection of \(SM\) and preserves Liouville measure. The terminal direction retains the sheet information exactly.

As a model case, on an arbitrarily collapsed flat torus one has
\[
\exp_p^*g=g_p^{\mathrm{Eucl}},\qquad J_p(t,\theta)=t^{n-1},
\]
even when \(B_r(0)\) wraps around the torus many times. The estimate then holds with \(C_n(0,r)=1\).

---

## 6. Smooth compactness of the exponential charts

The sectional estimate alone gives uniform metric ellipticity. After identifying \(T_pM\) with \(\mathbb R^n\) by an orthonormal frame,
\[
a(K,r)^2\,g_{\mathrm{Eucl}}
\le h_p\le
b(K,r)^2\,g_{\mathrm{Eucl}},
\]
where
\[
a(K,r)=\frac{\sin(\sqrt Kr)}{\sqrt Kr},
\qquad
b(K,r)=\frac{\sinh(\sqrt Kr)}{\sqrt Kr}.
\]
It also gives the Jacobian estimates used above. It does not by itself yield smooth precompactness of \(h_p\).

A standard sufficient package for \(C^\infty_{\mathrm{loc}}\) compactness is
\[
\sup_U|\nabla^m\operatorname{Rm}(g_i)|\le C_m
\qquad\text{for every }m\ge0,
\]
uniformly on all radial images under consideration, preferably with a small additional radial cushion. Since
\[
\exp_{p_i}:(B_r(0),h_i)\to(M,g_i)
\]
is a local isometry,
\[
|\nabla^m\operatorname{Rm}(h_i)|(v)
=
|\nabla^m\operatorname{Rm}(g_i)|(\exp_{p_i}v).
\]
Differentiating the geodesic and Jacobi equations then gives uniform coordinate derivative estimates for \(h_i\). After choosing orthonormal frames, a subsequence converges smoothly on every \(B_{r'}(0)\), \(r'<r\). Smooth convergence on the closed radius-\(r\) domain follows when the estimates hold slightly beyond \(r\).

That all-order input cannot be replaced by \(|\sec|\le K\) alone. For example, on \(T^4\) consider
\[
g_j=e^{2u_j(x_1)}(dx_1^2+dx_2^2)+dx_3^2+dx_4^2,
\qquad
u_j(x_1)=j^{-2}\sin(jx_1).
\]
The Gaussian curvature of the first factor is
\[
\kappa_j=e^{-2u_j}\sin(jx_1),
\]
so \(|\sec_{g_j}|\le2\), uniformly. At a point with \(x_1=0\),
\[
|\nabla\operatorname{Rm}(g_j)|\asymp j.
\]
For the exponential pullbacks \(h_j\) based there,
\[
|\nabla\operatorname{Rm}(h_j)|(0)\asymp j,
\]
so these charts have no smoothly convergent subsequence. This explicitly separates the averaging estimate, which needs only sectional control, from smooth chart convergence, which needs curvature-derivative control or an analytic smoothing mechanism that supplies it.

For a set \(P\) with \(\operatorname{Vol}(P)\ge v>0\), the lemma also gives a basepoint \(p\in P\) satisfying
\[
\frac1{\operatorname{Vol}_{h_p}(B_r)}
\int_{B_r}F(\exp_pv)\,d\mu_{h_p}
\le
\frac{C_n(K,r)}{v}\int_UF\,d\mu_g.
\]
Thus global smallness of a defect produces a pullback chart with small averaged defect, independently of collapse and exponential-map multiplicity. Smooth geometric passage on that chart still uses the derivative estimates described above.