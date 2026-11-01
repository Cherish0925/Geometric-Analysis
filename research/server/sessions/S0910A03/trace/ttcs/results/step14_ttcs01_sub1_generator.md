# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/originals/0911_3104__Smoothing_Riemannian_Metrics_with_Bounded_Ricci_Curvatures_in_Dimens.pdf",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Sessions/S0910A03/workspace/notes/step13_smoothing_bridge_and_L2_propagation.md",
    "Sessions/S0910A03/workspace/scripts/verify_einstein_defect_evolution.py"
  ]
}
```

## Task

Investigate a normalized cutoff Ricci flow on a closed 4-manifold, ∂_t g=-2 χ^2 (Ric+g), as a localization device for a metric with globally small Einstein defect |E|<=delta but curvature-energy control only on a buffered ball. Derive the principal evolution of E=Ric+g, keeping every term from spatially varying χ, and determine whether all added terms are homogeneous in E and its derivatives (so vanish when E=0) or whether gauge/parabolicity issues introduce other terms. Seek an energy bootstrap compatible with Ye Li's Corollary 3.5 and quantify interior boundary influence. Compare this route with local Ricci-DeTurck/Yang flows if needed, but do not cite unstated theorems. Produce explicit formulas and a scientifically useful conditional route or obstruction.

## Output

Let  
\[
E=\operatorname{Ric}+g,\qquad \tau=\operatorname{tr}_gE=R+4,\qquad f=\chi^2,
\]
where \(\chi\) is a fixed smooth scalar function. All derivatives below are taken with respect to \(g(t)\), although the pointwise values of \(\chi\) are time-independent.

## 1. Exact evolution of \(E\)

Use
\[
(\Delta_L h)_{ij}
=\Delta h_{ij}+2R_{ikjl}h^{kl}
-R_i{}^kh_{kj}-R_j{}^kh_{ki}.
\]
For a metric variation \(v=\partial_tg\),
\[
2\,\partial_t\operatorname{Ric}_{ij}
=-(\Delta_Lv)_{ij}-\nabla_i\nabla_j\operatorname{tr}v
+\nabla_i(\operatorname{div}v)_j+\nabla_j(\operatorname{div}v)_i.
\]
Here \(v=-2fE\), while contracted Bianchi gives
\[
\nabla^iE_{ij}=\frac12\nabla_j\tau.
\]
Consequently,
\[
\partial_t\operatorname{Ric}_{ij}
=(\Delta_L(fE))_{ij}
+\nabla_i\nabla_j(f\tau)
-\nabla_i\nabla^k(fE_{kj})
-\nabla_j\nabla^k(fE_{ki}).
\]
After expanding all products,
\[
\boxed{\quad
\partial_tE=f(\Delta_LE-2E)+\mathcal C_f(E),
\quad}
\]
where
\[
\begin{aligned}
\mathcal C_f(E)_{ij}
={}&(\Delta f)E_{ij}+2\nabla^kf\,\nabla_kE_{ij}
+\tau\nabla_i\nabla_jf
+\frac12\bigl(\nabla_if\,\nabla_j\tau+\nabla_jf\,\nabla_i\tau\bigr)\\
&-(\nabla_i\nabla^kf)E_{kj}
-(\nabla_j\nabla^kf)E_{ki}\\
&-\nabla^kf\bigl(\nabla_iE_{kj}+\nabla_jE_{ki}\bigr).
\end{aligned}
\tag{1}
\]

For \(f=\chi^2\), this becomes
\[
\begin{aligned}
\mathcal C_{\chi^2}(E)_{ij}
={}&(2\chi\Delta\chi+2|\nabla\chi|^2)E_{ij}
+4\chi\nabla^k\chi\,\nabla_kE_{ij}\\
&+2\tau(\chi\nabla_i\nabla_j\chi+\nabla_i\chi\nabla_j\chi)
+\chi(\nabla_i\chi\nabla_j\tau+\nabla_j\chi\nabla_i\tau)\\
&-2(\chi\nabla_i\nabla^k\chi+\nabla_i\chi\nabla^k\chi)E_{kj}\\
&-2(\chi\nabla_j\nabla^k\chi+\nabla_j\chi\nabla^k\chi)E_{ki}\\
&-2\chi\nabla^k\chi
 \bigl(\nabla_iE_{kj}+\nabla_jE_{ki}\bigr).
\end{aligned}
\tag{2}
\]

Every cutoff-generated term is linear in \(E,\tau,\nabla E,\nabla\tau\). In particular,
\[
\mathcal C_f(0)=0
\]
for the identically vanishing tensor field. There is no additive term depending only on \(\chi\), its Hessian, or the curvature. This cancellation uses the normalized velocity \(-2f(\operatorname{Ric}+g)\): terms that separately look like \(\nabla^2f\otimes g\) and \(\nabla^2f\otimes\operatorname{Ric}\) combine into \(\nabla^2f\otimes E\).

If \(f=f(t,x)\), formula (1) remains the instantaneous evolution formula; no \(\partial_tf\) occurs because \(\partial_t\operatorname{Ric}\) only uses the current metric velocity. A time derivative of \(f\) does enter weighted energies containing \(f\).

## 2. Exact squared-norm equation

Metric variation contributes
\[
\partial_tg^{ij}=2fE^{ij}.
\]
The same cubic and linear cancellations as in the global normalized flow therefore give
\[
\boxed{
(\partial_t-f\Delta)|E|^2
=-2f|\nabla E|^2
+4fR_{ikjl}E^{ij}E^{kl}
+2\langle E,\mathcal C_f(E)\rangle .
}
\tag{3}
\]
Writing \(u=|E|\), the cutoff contribution is explicitly
\[
\begin{aligned}
2\langle E,\mathcal C_f(E)\rangle
={}&2(\Delta f)u^2+2\langle\nabla f,\nabla u^2\rangle
+2\tau E^{ij}\nabla_i\nabla_jf\\
&+2E^{ij}\nabla_if\,\nabla_j\tau
-4(\nabla_i\nabla_kf)E^{ij}E^k{}_j\\
&-4\nabla^kf\,E^{ij}\nabla_iE_{kj}.
\end{aligned}
\tag{4}
\]
Thus a direct pointwise estimate contains both \(\nabla^2\chi\,u^2\) and
\(\chi\nabla\chi\,u|\nabla E|\). A Ricci lower bound alone does not supply a uniformly controlled Hessian for a distance-based cutoff. The useful fact is that the Hessian terms disappear from the integrated energy after using Bianchi.

## 3. Weighted energy identity using only \(\nabla\chi\)

Let \(q=\eta^2\), where \(\eta\) is another spatial cutoff. At a fixed time, integration by parts on a closed manifold gives the exact identity
\[
\begin{aligned}
\int q\,2\langle E,\mathcal C_f(E)\rangle\,dV
={}&\int\Big[
-2u^2\langle\nabla f,\nabla q\rangle
-2\tau E(\nabla q,\nabla f)
+4E^2(\nabla q,\nabla f)
\Big]\,dV\\
&+\int q\Big[
-\tau\langle\nabla f,\nabla\tau\rangle
+2E(\nabla f,\nabla\tau)
\Big]\,dV .
\end{aligned}
\tag{5}
\]
No second derivative of \(f\) remains. Since
\[
|\tau|\le 2u,\qquad |\nabla\tau|\le 2|\nabla E|,
\]
the last line is bounded by
\[
C\int q|\nabla f|u|\nabla E|.
\]
The special choice \(f=\chi^2\) gives the scale-stable identity
\[
\frac{|\nabla f|^2}{f}=4|\nabla\chi|^2
\tag{6}
\]
on \(\{\chi>0\}\), with continuous value \(0\) where \(f=0\). Hence Young’s inequality absorbs the first-derivative terms into \(f|\nabla E|^2\) without a factor \(1/\chi\).

Accounting also for
\[
\partial_tdV=-f\tau\,dV
\]
and \(u\le C(|\mathrm{Rm}|+1)\), equations (3)–(6) yield
\[
\begin{aligned}
\frac{d}{dt}\int \eta^2u^2\,dV
+c\int\eta^2\chi^2|\nabla E|^2\,dV
\le {}&
C\int\bigl(\chi^2|\nabla\eta|^2+\eta^2|\nabla\chi|^2+\eta^2\chi^2\bigr)u^2\,dV\\
&+C\int\eta^2\chi^2|\mathrm{Rm}|u^2\,dV .
\end{aligned}
\tag{7}
\]

The curvature term has exactly the critical four-dimensional form
\[
\int |\mathrm{Rm}|\,|\eta\chi E|^2
\le \|\mathrm{Rm}\|_{L^2}\|\eta\chi E\|_{L^4}^2.
\]
If
\[
\|w\|_{L^4}^2\le A\|\nabla w\|_{L^2}^2
\]
and
\[
A\|\mathrm{Rm}\|_{L^2}\le\kappa_*
\tag{8}
\]
with \(\kappa_*\) sufficiently small, this term is absorbed into the gradient energy. Expanding \(\nabla(\eta\chi E)\) only adds the two terms already present in (7).

The same regularized calculation with \(u^p\), \(p\ge2\), gives
\[
\begin{aligned}
\frac{d}{dt}\int\eta^2u^p\,dV
+c_p\int\eta^2\chi^2|\nabla u^{p/2}|^2\,dV
\le C_p\int
\bigl(\chi^2|\nabla\eta|^2+\eta^2|\nabla\chi|^2+\eta^2\chi^2\bigr)u^p\,dV,
\end{aligned}
\tag{9}
\]
provided (8) persists on the balls used by the covering argument.

If the transition width is \(D\), so that
\[
|\nabla\chi|+|\nabla\eta|\le C D^{-1},
\]
then (9) gives, in particular,
\[
\int_\Omega u^3(t)\,dV_{g(t)}
\le
\exp\!\left(CtD^{-2}\right)
\int_\Omega u^3(0)\,dV_{g(0)}.
\tag{10}
\]
Here \(\Omega\) can be chosen with \(\operatorname{supp}\chi\Subset\Omega\) and with \(f=df=0\) in a collar of \(\partial\Omega\); there is then no flux from the exterior. From \(|E(0)|\le\delta\),
\[
\int_\Omega u^3(t)\,dV_{g(t)}
\le e^{CtD^{-2}}\delta^3\operatorname{Vol}_{g(0)}(\Omega).
\tag{11}
\]

Equation (10) quantifies the transition-annulus influence: over \(t\le cD^2\), its amplification is a fixed factor. No term independent of \(\delta\) is generated.

## 4. Compatibility with Ye Li’s Moser estimate

Inside the plateau \(\{\chi=1\}\), all of \(\mathcal C_f(E)\) vanishes and
\[
(\partial_t-\Delta)u^2
\le 4|\mathrm{Rm}|u^2.
\]
After regularization,
\[
\partial_tu\le \Delta u+C|\mathrm{Rm}|u.
\tag{12}
\]
Also
\[
\partial_tdV=-\tau\,dV\le C(|\mathrm{Rm}|+1)dV.
\]
Thus the supplied Theorem 2.5 and Corollary 3.5 apply on an interior cylinder with the potential
\[
F=|\mathrm{Rm}|+1,
\]
once the Li curvature bootstrap provides
\[
\left(\int_{B_\rho}F^3\,dV\right)^{1/3}
\le \mu t^{-1/3},
\qquad A^2\mu^3\le C.
\tag{13}
\]

Combining Theorem 2.5 at \(p_0=3\) with (11) gives, schematically,
\[
\begin{aligned}
u(x,t)
\le {}&
C A_\rho^{2/3}
\left(
(1+A_\rho^2\mu^3)t^{-1}+\rho^{-2}
\right)
\left(
t\,e^{CtD^{-2}}
\delta^3\operatorname{Vol}(\Omega)
\right)^{1/3}.
\end{aligned}
\tag{14}
\]
The relative Sobolev estimate
\[
A_\rho\le C
\left(\frac{\rho^4}{\operatorname{Vol}(B_\rho)}\right)^{1/2}
\]
then yields
\[
\boxed{
u(x,t)\le
C\delta\,e^{Ct/(3D^2)}
\left(\frac{\operatorname{Vol}(\Omega)}
{\operatorname{Vol}(B_\rho)}\right)^{1/3}
\left[
\left(\frac{\rho^2}{t}\right)^{2/3}
+\left(\frac{t}{\rho^2}\right)^{1/3}
\right].
}
\tag{15}
\]
If \(\Omega\) and \(B_\rho\) have comparable radii, their volume ratio is controlled by Bishop–Gromov from
\[
\operatorname{Ric}_{g(0)}=-g(0)+E(0)\ge -(1+\delta)g(0),
\]
together with metric equivalence along the flow. For
\[
t=\theta\rho^2,\qquad \rho\le cD,
\]
formula (15) becomes
\[
\sup_{B_{\rho/2}}|E(t)|\le C_\theta\delta,
\tag{16}
\]
independently of collapse.

Corollary 3.5 should therefore be used on the plateau, not directly across the transition annulus. Across that annulus, (5)–(11) replace the pointwise Hessian estimate.

## 5. Gauge and parabolicity

The second-order part of (1) is simply
\[
\chi^2\Delta E.
\]
For the metric equation itself, multiplication by \(\chi^2\) does not remove the usual Ricci diffeomorphism modes. Moreover, where \(\chi=0\), the entire second-order symbol vanishes. Thus the fixed-cutoff metric system is a degenerate Ricci system rather than a uniformly parabolic equation.

A weighted DeTurck vector can be taken as
\[
W=\chi^2 g^{ab}
\bigl(\Gamma(g)_{ab}^{\ \ k}-\Gamma(\bar g)_{ab}^{\ \ k}\bigr)\partial_k.
\]
For
\[
\partial_tg=-2\chi^2E+\mathcal L_Wg,
\]
the defect evolution is
\[
\partial_tE
=\chi^2(\Delta_LE-2E)+\mathcal C_{\chi^2}(E)+\mathcal L_WE.
\tag{17}
\]
Since \(E\) is a natural tensor, the gauge term is exactly \(\mathcal L_WE\); it is again homogeneous in \(E,\nabla E\). In the norm equation it contributes the transport term
\[
W(|E|^2).
\]
Therefore the gauge does not create an additive defect.

There is, however, a coefficient-transport issue. If \(\Phi_t\) is generated by \(-W\), then \(h=\Phi_t^*g\) satisfies
\[
\partial_th=-2(\chi^2\circ\Phi_t)E_h,
\]
rather than the equation with the original fixed scalar. To recover the prescribed cutoff exactly, the DeTurck system must include a transported scalar \(f_D\) satisfying
\[
\partial_tf_D=W(f_D),
\qquad f_D(0)=\chi^2.
\]
Then \(f_D\circ\Phi_t=\chi^2\). This transport does not add a source to (1), but estimates for \(\nabla f_D\) must accompany the metric estimates.

## 6. Curvature bootstrap and the main obstruction

The curvature variation under \(v=-2fE\) has the schematic structure
\[
\partial_t\mathrm{Rm}
=f\bigl(\Delta\mathrm{Rm}
+\mathrm{Rm}*\mathrm{Rm}
+\mathrm{Rm}\bigr)
+\nabla f*\nabla E
+\nabla^2f*E
+\mathrm{Rm}*fE.
\tag{18}
\]
The apparently troublesome \(\nabla^2f*E\) term can again be integrated by parts in the \(L^2\)-curvature energy. Since
\[
\nabla E=\nabla\operatorname{Ric}
\]
is a contraction of \(\nabla\mathrm{Rm}\), one expects an inequality of the form
\[
\begin{aligned}
\frac{d}{dt}\int\zeta^2|\mathrm{Rm}|^2
+c\int\zeta^2f|\nabla\mathrm{Rm}|^2
\le {}&
C\int\zeta^2f\bigl(|\mathrm{Rm}|^3+|\mathrm{Rm}|^2\bigr)\\
&+CD^{-2}\int_{\operatorname{supp}\zeta}
\bigl(|\mathrm{Rm}|^2+1\bigr).
\end{aligned}
\tag{19}
\]
The cubic term is absorbed exactly as in Ye Li using the local Sobolev inequality and critical \(L^2\)-smallness. This suggests a localized analogue of Li’s curvature bootstrap whose constants depend on the transition width but not on volume.

The substantive analytic obstruction is construction of the degenerate cutoff flow for a uniform time from data known only on the active buffer. Formula (19) supplies the interior a priori estimate, but ordinary DeTurck theory is uniformly parabolic only when \(f\ge f_0>0\). Three representations separate this issue:

1. **Regularized coefficient**
   \[
   f_\varepsilon=\chi^2+\varepsilon.
   \]
   The weighted DeTurck system is uniformly parabolic. The key estimates above are uniform in \(\varepsilon\), since
   \[
   \frac{|\nabla f_\varepsilon|^2}{f_\varepsilon}
   \le 4|\nabla\chi|^2.
   \]
   Exterior curvature evolves on the slow \(\varepsilon\)-time scale. For each smooth metric, \(\varepsilon\) may be chosen relative to its exterior \(C^k\)-geometry so the exterior evolution persists past the desired interior time. Passing \(\varepsilon\to0\) requires compactness on the active buffer.

2. **Ricci–DeTurck on a buffered domain.** Solve the coefficient-one normalized DeTurck equation on \(\Omega\), prescribe metric data on \(\partial\Omega\), and estimate a smaller region by nested cutoffs. This avoids both degeneracy and \(\nabla^2\chi\) in the metric PDE. The same Caccioppoli calculation quantifies the influence of the prescribed edge data by \(e^{Ct/D^2}\). Pullback changes the domain by a diffeomorphism but preserves the local Einstein-defect estimate.

3. **Yang-type local flow.** The equation \(\partial_tg=-2\chi^2\operatorname{Ric}\) mentioned in the supplied paper has the same principal degeneracy; adding \(-2\chi^2g\) is lower order and gives the useful stationary tensor \(E\). The supplied text does not contain the local existence estimates needed here. A self-contained use would therefore require deriving the regularized DeTurck construction and the uniform forms of (19), Li’s local Sobolev persistence, and the \(L^3\) curvature estimate (13).

A scientifically useful conditional statement is consequently:

> Suppose the buffered region admits the Li small critical-energy estimate on every ball used by the covering argument, and suppose a cutoff or domain Ricci–DeTurck flow exists for \(0\le t\le\theta\rho^2\), with metric equivalence, Sobolev control, persistence of (8), and the curvature estimate (13). If \(\chi=1\) on a \(3\rho\)-neighborhood of the target and its transition width satisfies \(D\ge c\rho\), then
> \[
> |\mathrm{Rm}(t)|\le C\rho^{-2},
> \qquad
> |E(t)|\le C_\theta\delta
> \]
> on the target at \(t=\theta\rho^2\), with constants independent of local volume.

Thus the normalized cutoff terms themselves are compatible with preservation of a small Einstein defect. The central unresolved substance is the uniform construction of the degenerate flow and the localized curvature bootstrap (19), not an \(E\)-independent source created by the cutoff or by DeTurck gauge.