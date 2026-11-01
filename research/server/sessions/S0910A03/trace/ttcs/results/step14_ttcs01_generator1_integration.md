# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 14,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step14_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step14_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Investigate a normalized cutoff Ricci flow on a closed 4-manifold, ∂_t g=-2 χ^2 (Ric+g), as a localization device for a metric with globally small Einstein defect |E|<=delta but curvature-energy control only on a buffered ball. Derive the principal evolution of E=Ric+g, keeping every term from spatially varying χ, and determine whether all added terms are homogeneous in E and its derivatives (so vanish when E=0) or whether gauge/parabolicity issues introduce other terms. Seek an energy bootstrap compatible with Ye Li's Corollary 3.5 and quantify interior boundary influence. Compare this route with local Ricci-DeTurck/Yang flows if needed, but do not cite unstated theorems. Produce explicit formulas and a scientifically useful conditional route or obstruction.

## Integrated Scientific Memo

## Scientific integration memo

Let
\[
a=\chi^2,\qquad E=\Ric(g)+g,\qquad \tau=\tr_gE=R+4,
\]
and consider on a closed four-manifold
\[
\partial_tg=-2aE,
\]
with \(\chi\) fixed as a scalar function. Covariant derivatives below use \(g(t)\).

### 1. Exact defect evolution

For a variation \(v=\partial_tg\),
\[
2\,\partial_t\Ric_{ij}
=-(\Delta_Lv)_{ij}-\nabla_i\nabla_j\tr v
+\nabla_i(\div v)_j+\nabla_j(\div v)_i,
\]
where
\[
(\Delta_Lh)_{ij}
=\Delta h_{ij}+2R_{ikjl}h^{kl}
-R_i{}^kh_{kj}-R_j{}^kh_{ki}.
\]
Since \(v=-2aE\) and
\[
\nabla^iE_{ij}=\frac12\nabla_j\tau,
\]
one obtains
\[
\boxed{\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E)}
\]
with
\[
\begin{aligned}
\mathcal C_a(E)_{ij}={}&
(\Delta a)E_{ij}+2\nabla^ka\,\nabla_kE_{ij}
+\tau\nabla_i\nabla_ja\\
&+\frac12\bigl(\nabla_i a\,\nabla_j\tau
+\nabla_j a\,\nabla_i\tau\bigr)\\
&-(\nabla_i\nabla^ka)E_{kj}
-(\nabla_j\nabla^ka)E_{ki}\\
&-\nabla^ka\bigl(\nabla_iE_{kj}+\nabla_jE_{ki}\bigr).
\end{aligned}
\tag{1}
\]

For \(a=\chi^2\),
\[
\nabla a=2\chi\nabla\chi,\qquad
\nabla^2a=2\chi\nabla^2\chi+2\,d\chi\otimes d\chi,\qquad
\Delta a=2\chi\Delta\chi+2|\nabla\chi|^2.
\]

Every cutoff term in (1) is linear in \(E,\tau,\nabla E,\nabla\tau\). Thus
\[
\mathcal C_a(0)=0.
\]
There is no source involving only \(\chi\) and curvature. In particular, an Einstein metric with \(\Ric=-g\) remains exactly stationary even through the transition annulus. Apparent \(\nabla^2a\otimes g\) terms cancel against the corresponding Ricci terms after writing \(\Ric=E-g\).

### 2. Squared norm and the absence of linear damping

Because \(\partial_tg^{ij}=2aE^{ij}\), the cubic terms from inverse-metric variation cancel the corresponding Lichnerowicz terms, as in the uncut normalized flow. The exact equation is
\[
\boxed{
(\partial_t-a\Delta)|E|^2
=-2a|\nabla E|^2
+4aR_{ikjl}E^{ij}E^{kl}
+2\langle E,\mathcal C_a(E)\rangle .
}
\tag{2}
\]

An explicit contraction is
\[
\begin{aligned}
2\langle E,\mathcal C_a(E)\rangle
={}&2(\Delta a)|E|^2
+2\langle\nabla a,\nabla |E|^2\rangle
+2\tau E^{ij}\nabla_i\nabla_ja\\
&+2E^{ij}\nabla_i a\,\nabla_j\tau
-4(\nabla_i\nabla_ka)E^{ij}E^k{}_j\\
&-4\nabla^ka\,E^{ij}\nabla_iE_{kj}.
\end{aligned}
\tag{3}
\]

Although the tensor equation contains \(-2aE\), no net \(-c\,a|E|^2\) survives in (2). Consequently the global pointwise argument
\[
(\partial_t-\Delta)|E|^2\lesssim |\Rm||E|^2,\qquad |\Rm|\lesssim t^{-1},
\]
leads to the divergent coefficient \(\int_0^{t_0}dt/t\). This is a genuine obstruction to direct pointwise Grönwall propagation from \(t=0\), not a bookkeeping artifact.

The identity sometimes used to rewrite part of the scalar operator,
\[
a\Delta u+2\nabla a\cdot\nabla u
=\chi^{-2}\div(\chi^4\nabla u),
\]
is valid only where \(\chi>0\) and is singular at \(\chi=0\); it should not be treated as a globally regular uniformly parabolic formulation.

### 3. Integrated cutoff terms: Hessians of \(\chi\) are avoidable

For an independent test cutoff \(q=\eta^2\), integration by parts and Bianchi give
\[
\begin{aligned}
\int q\,2\langle E,\mathcal C_a(E)\rangle\,dV
={}&\int\Big[
-2|E|^2\langle\nabla a,\nabla q\rangle
-2\tau E(\nabla q,\nabla a)
+4E^2(\nabla q,\nabla a)
\Big]\,dV\\
&+\int q\Big[
-\tau\langle\nabla a,\nabla\tau\rangle
+2E(\nabla a,\nabla\tau)
\Big]\,dV .
\end{aligned}
\tag{4}
\]
Hence no \(\nabla^2a\) estimate is required in the energy argument. Since in dimension four
\[
|\tau|\le2|E|,\qquad |\nabla\tau|\le2|\nabla E|,
\]
and
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2
\quad\text{on }\{\chi>0\},
\tag{5}
\]
Young’s inequality absorbs all \(a^{1/2}|\nabla E|\) terms without a \(1/\chi\) loss.

Including
\[
\partial_tdV=-a\tau\,dV
\]
gives, schematically but with the correct dependencies,
\[
\begin{aligned}
\frac d{dt}\int\eta^2|E|^2\,dV
+c\int\eta^2a|\nabla E|^2\,dV
\le{}&
C\int\bigl(a|\nabla\eta|^2+\eta^2|\nabla\chi|^2+\eta^2a\bigr)|E|^2\,dV\\
&+C\int\eta^2a|\Rm|\,|E|^2\,dV .
\end{aligned}
\tag{6}
\]
Thus the transition annulus contributes multiplicatively through \(|\nabla\chi|^2|E|^2\), not as an \(E\)-independent feed. This corrects the weaker estimate obtained by bounding annulus terms merely by \(\delta^2\Vol\): such a bound is available only while pointwise smallness has already been propagated there and is unnecessary for the closed homogeneous energy estimate.

If the transition and testing widths are \(D\), so
\[
|\nabla\chi|+|\nabla\eta|\lesssim D^{-1},
\]
the boundary influence over time \(t\) has the scale
\[
\exp(CtD^{-2}).
\tag{7}
\]
For \(t\le cD^2\), it is a fixed amplification factor. If \(a=da=0\) in a collar outside the active region, the metric is frozen there and there is no physical exterior flux; nevertheless, existence of the resulting degenerate metric equation remains a separate issue.

### 4. Four-dimensional absorption and defect propagation

The critical reaction term satisfies
\[
\int |\Rm|\,|\eta\chi E|^2
\le \|\Rm\|_{L^2}\,\|\eta\chi E\|_{L^4}^2.
\]
With a local Sobolev inequality
\[
\|w\|_{L^4}^2\le A\|\nabla w\|_{L^2}^2,
\tag{8}
\]
it is absorbable provided
\[
A\,\|\Rm\|_{L^2(B)}\le\kappa_*
\tag{9}
\]
for a sufficiently small dimensional \(\kappa_*\).

Using Li’s relative estimate
\[
A\lesssim\left(\frac{r^4}{\Vol(B_r)}\right)^{1/2},
\]
condition (9) is precisely smallness of
\[
\varepsilon_r
=\frac{r^4}{\Vol(B_r)}\int_{B_r}|\Rm|^2.
\]
Collapse causes no extra loss because the volume factors cancel. Expanding \(\nabla(\eta\chi E)\) introduces only the cutoff terms already appearing in (6).

Assuming persistence of (8)–(9) on every ball used in the covering argument, the regularized \(p\)-energy calculation yields
\[
\frac d{dt}\int\eta^2|E|^p
+c_p\int\eta^2a|\nabla |E|^{p/2}|^2
\le
C_p(D^{-2}+1)\int_{\operatorname{supp}\eta}|E|^p .
\tag{10}
\]
For \(p=3\),
\[
\int_{\Omega_{\rm in}}|E(t)|^3
\le e^{C t(D^{-2}+1)}
\int_{\Omega_{\rm buffer}}|E(0)|^3.
\tag{11}
\]
Thus \(|E(0)|\le\delta\) gives an \(O(\delta^3)\) interior \(L^3\) bound with no generated additive defect.

### 5. What Li’s Corollary 3.5 supplies—and what it does not

Li proves Corollary 3.5 under a pre-existing smooth family satisfying:

1. metric equivalence;
2. a uniform local Sobolev inequality;
3. curvature-energy persistence sufficient to derive
   \[
   \int_{B_r}|\Rm|^3\lesssim t^{-1};
   \]
4. a scalar inequality
   \[
   \partial_tu\le\phi^2(\Delta u+c_0fu).
   \]

The paper treats global Ricci flow and does not prove existence or smoothing for the cutoff normalized flow. Therefore it is unjustified to say that Li’s theorem applies “verbatim” merely because \(\chi=1\) on an interior plateau: parabolic equations have infinite propagation, and local equality of the differential operator does not by itself import the global curvature bootstrap.

Conditionally, if the cutoff or domain flow has Li’s metric, Sobolev, and curvature estimates on a buffered cylinder, then on the plateau \(a=1\),
\[
\partial_t|E|\le\Delta|E|+C(|\Rm|+1)|E|.
\tag{12}
\]
Combining Corollary 3.5 with (11) at \(t=\theta\rho^2\) gives
\[
\sup_{B_{\rho/2}}|E(t)|
\le
C_\theta\,\delta\,
e^{Ct/(3D^2)}
\left(\frac{\Vol(\Omega_{\rm buffer})}{\Vol(B_\rho)}\right)^{1/3}.
\tag{13}
\]
For comparable concentric radii, the volume ratio is controlled from the initial Ricci lower bound
\[
\Ric(g_0)=-g_0+E(g_0)\ge-(1+\delta)g_0
\]
and metric equivalence. Hence, independently of collapse,
\[
\sup_{B_{\rho/2}}|E(\theta\rho^2)|\le C_\theta\delta.
\tag{14}
\]

The same conclusion can be reached from \(L^2\) propagation plus an interior parabolic mean-value inequality, provided curvature is bounded on a preceding cylinder. Either method avoids the divergent pointwise \(t^{-1}\) Grönwall estimate.

### 6. Gauge and parabolicity

The geometric cutoff equation remains diffeomorphism-degenerate, and its elliptic symbol vanishes where \(\chi=0\). It is therefore not covered by ordinary uniformly parabolic Ricci–DeTurck theory.

For a weighted DeTurck field
\[
W=a\,g^{pq}\bigl(\Gamma(g)_{pq}^{\,k}-\Gamma(\bar g)_{pq}^{\,k}\bigr)\partial_k
\]
and
\[
\partial_tg=-2aE+\mathcal L_Wg,
\]
naturality gives
\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E)+\mathcal L_WE.
\tag{15}
\]
The gauge term is homogeneous and contributes transport \(W(|E|^2)\) to the norm equation; it creates no defect source.

Two qualifications are essential:

* Adding \(a\mathcal L_Wg\) versus using \(W\) already containing \(a\) must not double the weight.
* Pullback by the DeTurck diffeomorphism changes a fixed spatial coefficient to \(a\circ\Phi_t\). To recover the prescribed geometric cutoff exactly, one must evolve a DeTurck-side coefficient by
  \[
  \partial_ta_D=W(a_D),\qquad a_D(0)=\chi^2.
  \]
  Bounds for its derivatives then become part of the existence theory.

No supplied estimate controls \(\int|W|dt\), so claims that the DeTurck displacement is automatically smaller than the buffer are presently unsupported.

### 7. Curvature bootstrap and precise unresolved object

For the cutoff flow, curvature evolves schematically as
\[
\partial_t\Rm
=a(\Delta\Rm+\Rm*\Rm+\Rm)
+\nabla a*\nabla E+\nabla^2a*E+a\,\Rm*E.
\tag{16}
\]
Since \(\nabla E=\nabla\Ric\) is a contraction of \(\nabla\Rm\), integration by parts should yield
\[
\begin{aligned}
\frac d{dt}\int\zeta^2|\Rm|^2
+c\int\zeta^2a|\nabla\Rm|^2
\le{}&
C\int\zeta^2a\bigl(|\Rm|^3+|\Rm|^2\bigr)\\
&+CD^{-2}\int_{\operatorname{supp}\zeta}
\bigl(|\Rm|^2+|E|^2\bigr),
\end{aligned}
\tag{17}
\]
after suitable nested cutoffs. The cubic term has Li’s critical form and is absorbable under (9). However, (17), its exact cutoff coefficients, and the associated covering/bootstrap argument have not been established in the supplied source.

Accordingly, the strongest justified result is conditional:

> Suppose a cutoff or buffered-domain Ricci–DeTurck flow exists for \(0\le t\le\theta\rho^2\), remains uniformly equivalent to \(g_0\), preserves the required local Sobolev inequalities and critical \(L^2\)-curvature smallness, and supplies Li’s local \(L^3\) potential estimate on a plateau whose distance to the transition annulus is \(D\gtrsim\rho\). Then at \(t=\theta\rho^2\),
> \[
> |\Rm|\le C\rho^{-2},\qquad |E|\le C_\theta\delta
> \]
> on the target ball, with constants independent of collapse. Transition-annulus influence is bounded by \(e^{Ct/D^2}\), and no additive defect is generated.

The unresolved analytic object is not defect homogeneity: that is settled affirmatively by (1). It is the uniform short-time construction and localized curvature-energy bootstrap for the degenerate coefficient \(a=\chi^2\).

The cleanest alternatives are:

1. regularize \(a_\varepsilon=\chi^2+\varepsilon\), prove estimates uniform in \(\varepsilon\), and pass to a limit on the active buffer;
2. solve a uniformly parabolic normalized Ricci–DeTurck problem on a buffered domain and use nested interior cutoffs;
3. derive a Yang-type local-flow existence argument from the same energy estimates.

The supplied Li paper motivates these routes and provides the Moser/critical-energy machinery, but does not itself close any of these localization constructions.