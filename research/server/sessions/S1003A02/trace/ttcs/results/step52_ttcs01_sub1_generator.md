# TTCS Independent Branch Record

```json
{
  "step_id": 52,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step52_residual_norm_selection_absorption.md",
    "Sessions/S1003A02/workspace/notes/step51_residual_entry_link_charges_and_kahler_recovery.md",
    "Knowledge/objects/papers/The-long-time-behavior-of-fourth-order-curvature-flows--5b1863f1c7b9--f1cab1a2d745/object.md"
  ]
}
```

## Task

The entry programme for minimizing sequences of P(g)=∫|Ric°|² on closed four-manifolds now hinges on Lemma 52.KS in the attached note: an own-scale concentration lemma for the energy-radius-weighted (frozen-weight) gradient flow of P — lifespan ≥ c1 in own-scale time, two-sided comparability of the energy radius, Sobolev persistence — the analogue of Kuwert–Schätzle's lemma for Willmore flow. P is in Bour's strongly parabolic class (a=b=0) but its gradient dissipates only the Ricci part; the Weyl energy must be controlled through the Pfaffian transgression and the Bianchi system δW ~ ∇Ric. Produce the strongest concrete proof architecture you can: the localized energy identity with cutoffs (exact form of d/dt ∫φ|Rm|² or of a better localized quantity), interpolation inequalities replacing Kuwert–Schätzle's, where the Sobolev constant enters, and how the weight's own-scale derivatives enter. If you believe the lemma is false, give a precise counter-mechanism (e.g. Weyl-energy transfer through necks at zero Ricci dissipation) and the weakest replacement that still yields a Palais–Smale minimizing sequence in the sense (PS_ε). Also propose an alternative selection mechanism (not a sixth-order regularization) if you see one that avoids flow lifetime altogether.

## Output

The most useful simplification is that the Pfaffian flux can be written **without derivatives of the Weyl tensor or of the flow velocity**. The divergence-free double dual of curvature converts the entire Euler-density contribution into curvature times the Hessian of the cutoff. This gives a genuinely coercive localized estimate.

There is also a structural issue with Lemma 52.KS: its two-sided comparison for the hard-threshold energy radius is not valid for arbitrary smooth initial data. A concentration packet whose total energy crosses just below \(\varepsilon\) can make that radius jump from a microscopic scale to the cap. The selection argument can instead be formulated using output-compatible dissipation time, or an adaptive weight built from a threshold-averaged radius.

## 1. An exact localized identity with no differentiated Weyl flux

Use the full tensor norm
\[
|\mathrm{Rm}|_{\mathrm{ten}}^2=R_{ijkl}R^{ijkl}.
\]
Write \(E=\mathrm{Ric}^{\circ}\), \(H=\operatorname{tr}h\), and
\[
\mathcal E=|\mathrm{Rm}|_{\mathrm{ten}}^2-4|E|^2.
\]
In dimension four,
\[
\mathcal E\,d\mu=32\pi^2\,e(TM,g),\qquad
\int_M|\mathrm{Rm}|_{\mathrm{ten}}^2=4P+32\pi^2\chi(M).
\]
If the curvature-operator norm is used, all full-curvature energies below are divided by four.

For a fixed smooth cutoff \(\phi\), set
\[
P_\phi(g)=\int_M\phi |E|^2\,d\mu .
\]
The exact first variation is
\[
DP_{\phi,g}(h)=\int_M\langle \phi Q+C_\phi,h\rangle\,d\mu ,
\tag{1}
\]
where
\[
C_\phi=2(D\mathrm{Ric})_g^*(\phi E)
       -2\phi(D\mathrm{Ric})_g^*E .
\tag{2}
\]
This expression specifies the cutoff terms exactly, including their derivative ordering. In particular,
\[
|C_\phi|
\le C\bigl(|\nabla\phi|\,|\nabla E|
             +|\nabla^2\phi|\,|E|\bigr).
\tag{3}
\]

For completeness, if
\[
A(T)_{ab}
 =\nabla^i\nabla_aT_{bi}
  +\nabla^i\nabla_bT_{ai}
  -\Delta T_{ab}
  -(\nabla^i\nabla^jT_{ij})g_{ab},
\]
then
\[
Q=A(E)-2E_i{}^kE_{jk}-\frac{s}{2}E_{ij}
              +\frac12|E|^2g_{ij},
\qquad
C_\phi=A(\phi E)-\phi A(E).
\tag{4}
\]

Now introduce the double dual curvature tensor
\[
\begin{aligned}
\mathcal R_{ikjl}
={}&R_{ikjl}
-g_{ij}\mathrm{Ric}_{kl}
-g_{kl}\mathrm{Ric}_{ij}
+g_{il}\mathrm{Ric}_{kj}
+g_{kj}\mathrm{Ric}_{il}\\
&+\frac{s}{2}(g_{ij}g_{kl}-g_{il}g_{kj}).
\end{aligned}
\]
It satisfies
\[
\nabla^k\mathcal R_{ikjl}=0.
\]
The four-dimensional Lovelock variation identity is
\[
D_g\!\left(\int_M\phi\mathcal E\,d\mu\right)(h)
=
-4\int_M
\mathcal R_{ikjl}\nabla^k\nabla^l\phi\,h^{ij}\,d\mu .
\tag{5}
\]
Thus the Chern–Weil transgression, initially involving
\(\nabla h*\mathrm{Rm}*\nabla\phi\), collapses after integration by parts to
\[
h*\mathrm{Rm}*\nabla^2\phi.
\]
The cancellation uses the differential Bianchi identity. It is stronger than an estimate of \(\delta W\) in terms of \(\nabla\mathrm{Ric}\).

For the geometric flow
\[
\partial_tg=-wQ
\]
with any positive scalar weight \(w\), define
\[
\mathcal H_\phi(t)=\int_M\phi|\mathrm{Rm}|_{\mathrm{ten}}^2\,d\mu.
\]
Equations (1)–(5) give
\[
\boxed{
\frac{d}{dt}\mathcal H_\phi
=
-4\int_M\phi w|Q|^2
-4\int_Mw
\left\langle
C_\phi-\mathcal R_{ikjl}\nabla^k\nabla^l\phi,\ Q
\right\rangle .
}
\tag{6}
\]
There are **no spatial derivatives of \(w\)** in this identity. There is also no \(\nabla W\) term.

For a time-dependent cutoff, add
\[
\int_M\partial_t\phi\,|\mathrm{Rm}|_{\mathrm{ten}}^2\,d\mu .
\]
In DeTurck coordinates, the Lie-derivative contribution disappears when the cutoff is transported by
\[
\partial_t\phi=Y\phi ,
\]
where \(Y\) is the DeTurck vector field. A weight frozen in those coordinates becomes time-dependent after pullback; (6) remains valid.

### The basic cutoff inequality

Take \(\phi=\eta^4\), \(0\le\eta\le1\). Young’s inequality gives
\[
\begin{aligned}
\frac{d}{dt}\mathcal H_{\eta^4}
+2\int\eta^4w|Q|^2
\le C\int w\Big[
&\eta^2|\nabla\eta|^2|\nabla E|^2\\
&+\bigl(|\nabla^2\eta|^2+|\nabla\eta|^4\bigr)
|\mathrm{Rm}|^2
\Big].
\end{aligned}
\tag{7}
\]
If the support has scale \(r\), and
\[
c r^4\le w\le C r^4,\qquad
|\nabla\eta|\le C r^{-1},\qquad
|\nabla^2\eta|\le C r^{-2},
\]
then
\[
\frac{d}{dt}\mathcal H_{\eta^4}+2D_\eta
\le C r^2\int\eta^2|\nabla E|^2
   +C\int_{\operatorname{supp}\eta}|\mathrm{Rm}|^2,
\qquad
D_\eta=\int\eta^4w|Q|^2 .
\tag{8}
\]

This is the appropriate intrinsic counterpart of the localized Willmore energy inequality.

## 2. The interpolation mechanism: a special Ricci multiplier

The principal part of \(Q\) is
\[
Q=-\Delta E+\frac12\nabla^2s-\frac14(\Delta s)g
       +\mathrm{Rm}*E+E*E,
\qquad
\operatorname{tr}Q=-\frac12\Delta s.
\tag{9}
\]
Pairing only with \(E\) produces
\[
\int\langle Q,E\rangle
=
\int|\nabla E|^2-\frac18\int|\nabla s|^2
+\int\mathrm{Rm}*E*E.
\]
The scalar term has the wrong sign for direct coercivity. The useful multiplier is instead
\[
T=E+\frac{s}{2}g.
\]
Its trace component reverses that sign:
\[
\boxed{
\int\langle Q,T\rangle
=
\int\left(|\nabla E|^2+\frac18|\nabla s|^2\right)
+\int\mathrm{Rm}*E*E .
}
\tag{10}
\]
The final term denotes the exact algebraic contractions coming from (4); its magnitude is bounded by \(C|\mathrm{Rm}|\,|E|^2\).

With a cutoff \(\eta^2\), integration by parts and absorption of cutoff cross terms yield
\[
\begin{aligned}
I_\eta
&:=\int\eta^2\left(|\nabla E|^2+|\nabla s|^2\right)\\
&\le
C\|\eta^2Q\|_2\,
  \|\mathrm{Rm}\|_{L^2(\operatorname{supp}\eta)}
+C\int|\nabla\eta|^2|\mathrm{Rm}|^2
+C\int\eta^2|\mathrm{Rm}|\,|E|^2 .
\end{aligned}
\tag{11}
\]

Suppose the ball supports
\[
\|u\|_4^2
\le C_S\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right).
\tag{12}
\]
Kato’s inequality permits its application to tensor norms. Then
\[
\begin{aligned}
\int\eta^2|\mathrm{Rm}|\,|E|^2
&\le \|\mathrm{Rm}\|_2\,\|\eta E\|_4^2\\
&\le C C_S\|\mathrm{Rm}\|_2
\left[
\int\eta^2|\nabla E|^2
+\int|\nabla\eta|^2|E|^2
+r^{-2}\int\eta^2|E|^2
\right].
\end{aligned}
\]
Consequently, for
\[
C C_S\left(\int_{\operatorname{supp}\eta}|\mathrm{Rm}|^2\right)^{1/2}
\le \frac12,
\tag{13}
\]
the cubic term is absorbed. Writing
\[
\mathcal H=\int_{\operatorname{supp}\eta}|\mathrm{Rm}|^2,
\]
one obtains
\[
r^2 I_\eta
\le C D_\eta^{1/2}\mathcal H^{1/2}+C\mathcal H
\le \theta D_\eta+C_\theta\mathcal H .
\tag{14}
\]
Combining this with (8) gives
\[
\boxed{
\frac{d}{dt}\mathcal H_{\eta^4}+cD_\eta
\le C\mathcal H .
}
\tag{15}
\]

The Sobolev constant enters exactly through the cubic absorption in (13). The first localized concentration estimate needs only first derivatives of Ricci; it does not require a separate estimate of differentiated Weyl curvature.

### Recovering full-curvature derivatives

For smoothing, the Bianchi system supplies the missing Weyl derivatives. Regarding curvature as a bundle-valued two-form,
\[
d^\nabla\mathrm{Rm}=0,\qquad
\delta^\nabla\mathrm{Rm}=\nabla\mathrm{Ric}-\nabla\mathrm{Ric}^{\mathrm{swap}}.
\]
The localized Weitzenböck identity gives, after the same small-energy absorption,
\[
\int\eta^2|\nabla\mathrm{Rm}|^2
\le C\int\eta^2|\nabla\mathrm{Ric}|^2
   +Cr^{-2}\mathcal H.
\tag{16}
\]

A particularly useful second-order interpolation follows from (12) and integration by parts:
\[
\|\xi F\|_4^2
\le C C_S\|\xi F\|_2
\left(
\|\xi\nabla^2F\|_2
+r^{-1}\|\nabla F\|_{L^2(\operatorname{supp}\xi)}
+r^{-2}\|F\|_{L^2(\operatorname{supp}\xi)}
\right).
\tag{17}
\]
In particular, with nested cutoffs,
\[
\int |\xi\mathrm{Rm}|^4
\le C C_S^2\mathcal H
\left(
\int_{\operatorname{supp}\xi}|\nabla^2\mathrm{Rm}|^2
+r^{-4}\mathcal H
\right).
\tag{18}
\]
This handles the quartic terms that appear when the Bianchi system is differentiated.

Combining:

* the trace equation in (9);
* the Ricci equation in (9);
* the differentiated Bianchi–Weitzenböck identity;
* the absorption in (18);

gives the useful local elliptic estimate
\[
r^4\int_{\mathrm{inner}}
\left(|\nabla^2\mathrm{Rm}|^2+|\nabla^2s|^2\right)
\le
C r^4\int_{\mathrm{outer}}|Q|^2+C\mathcal H,
\tag{19}
\]
provided the enlarged ball has sufficiently small curvature energy and controlled cutoffs. Nested cutoffs prevent the highest derivatives of curvature from being multiplied by singular cutoff quotients.

Equation (19) explains why Ricci dissipation can provide fourth-order smoothing of the whole curvature tensor. It also respects the endpoint phenomenon in Step 52: two curvature derivatives in \(L^2\) give every finite \(L^q\), not pointwise curvature control at a single time.

## 3. What the weighted parabolic proof would actually need

At the initial energy scale \(r=r_\varepsilon(x)\), the Lipschitz property gives
\[
r_\varepsilon(y)\asymp r
\quad\text{on }B(x,\vartheta r),\qquad \vartheta<1.
\]
Thus a frozen weight comparable to \(r_\varepsilon^4\) is uniformly elliptic after spatial rescaling on such a ball.

For curvature evolution, the relevant weight contributions come from
\[
\nabla^2(wQ)
=
w\nabla^2Q+2\nabla w*\nabla Q+\nabla^2w*Q.
\tag{20}
\]
The natural assumptions are
\[
|\nabla^jw|\le K_j r^{4-j}.
\tag{21}
\]
The first two spatial derivatives suffice for the basic curvature evolution estimate. Higher derivative smoothing uses further \(K_j\). After rescaling, these are ordinary coefficient bounds independent of the physical size \(r\).

A weighted version of Streets’ local estimates should have the shape
\[
\begin{aligned}
\frac{d}{dt}\int\eta^{2m+4}|\nabla^m\mathrm{Rm}|^2
+c\int\eta^{2m+4}w|\nabla^{m+2}\mathrm{Rm}|^2
\le {}&
C\int_{\mathrm{outer}}|\nabla^m\mathrm{Rm}|^2\\
&+C_m\int_{\mathrm{outer}}|\mathrm{Rm}|^2 ,
\end{aligned}
\tag{22}
\]
in normalized coordinates. The constants depend on \(C_S\), the cutoff geometry, and finitely many \(K_j\). The identities above supply the \(m=0\) coercivity; differentiated equations and (17) supply the higher orders.

There are two genuine geometric ingredients beyond these calculations.

**Intrinsic cutoff construction.** Small \(L^2\) curvature and a Sobolev inequality do not themselves provide pointwise Hessian bounds for a distance cutoff. Nor do they provide the initial harmonic-coordinate regularity used in Step 52.1. The proof needs either an intrinsic cutoff construction adapted to critical curvature energy, or a parabolic startup argument that produces suitable charts before (22) is applied. This is where an intrinsic analogue of the ambient cutoffs in Kuwert–Schätzle enters.

A Coulomb-frame representation is promising:
\[
\|A\|_4+\|\nabla A\|_2
\lesssim \|\mathrm{Rm}\|_2,
\qquad
de+A\wedge e=0.
\]
The substantive issue is converting the connection estimate and torsion equation into cutoff and coordinate estimates for the metric, rather than merely for its \(SO(4)\) connection.

**Sobolev persistence.** The energy law alone does not control the Sobolev quotient. For a fixed test function \(u\),
\[
\frac{d}{dt}\int|\nabla u|^2\,d\mu
=
\int\left[-h(\nabla u,\nabla u)
+\frac12(\operatorname{tr}h)|\nabla u|^2\right]d\mu,
\tag{23}
\]
while
\[
\frac{d}{dt}\log\left(\int u^4\,d\mu\right)^{1/2}
=
\frac14\frac{\int(\operatorname{tr}h)u^4\,d\mu}{\int u^4\,d\mu}.
\tag{24}
\]
An \(L^2\) estimate for \(h=-wQ\) does not control (23) uniformly over \(H^1\) test functions.

An integrable estimate for \(\|h\|_\infty\) would suffice, but the critical parabolic estimate near the initial time naturally has a \(t^{-1}\) singularity. Its integral diverges. Thus uniform pointwise metric comparison with the initial metric is substantially stronger than what the concentration calculation supplies. Sobolev persistence needs a quadratic-form argument, a critical parabolic coordinate theory, or additional geometric input.

The supplied Streets paper makes this distinction concrete: its localized smoothing estimates assume controlled cutoff Hessians, and its pointwise smoothing theorem assumes a spacetime curvature bound. Neither directly supplies these two ingredients.

## 4. A precise obstruction to two-sided hard-radius comparison

Consider a flat four-torus and a smooth metric perturbation supported in a ball of radius \(\ell\):
\[
g_{\ell,a}=g_{\mathrm{flat}}+
a\,k(x/\ell),
\]
with \(k\) a fixed smooth compactly supported symmetric tensor and \(a\) small. The metrics have uniformly controlled Sobolev constants because they are uniformly equivalent to the flat metric. Four-dimensional scaling gives
\[
\int|\mathrm{Rm}(g_{\ell,a})|_{\mathrm{ten}}^2
=C_k a^2+O(a^3),
\qquad
P(g_{\ell,a})=\frac14
\int|\mathrm{Rm}(g_{\ell,a})|_{\mathrm{ten}}^2.
\]
Choose \(a\) so that the total curvature energy is
\[
\varepsilon+\zeta,\qquad \zeta>0.
\]
At a point in the packet,
\[
r_\varepsilon(g_{\ell,a})\asymp \ell.
\]
A frozen weight has size \(\ell^4\) there. After rescaling the packet, its flow has an order-one parabolic speed. For a nonstationary choice of \(k\),
\[
\frac{d}{dt}\int|\mathrm{Rm}|_{\mathrm{ten}}^2
=-4\int w|Q|^2<0.
\]
Taking \(\zeta\) sufficiently small makes the total energy cross below \(\varepsilon\) during an arbitrarily short fixed own-scale interval. At that instant,
\[
r_\varepsilon(x,t)=r_0
\quad\text{for every }x,
\]
because even the total energy is below the threshold. Hence
\[
\frac{r_\varepsilon(x,t)}{r_\varepsilon(x,0)}
\asymp \frac{r_0}{\ell}\longrightarrow\infty.
\tag{25}
\]

This invalidates the asserted universal upper comparison. It uses ordinary Ricci dissipation, not a speculative Weyl transport mechanism.

It also shows why smoothing at the **output’s** hard energy radius cannot follow from smoothing at the frozen input radius: the output radius can become \(r_0\) while the surviving packet still has microscopic curvature scale.

This example has \(P\asymp\varepsilon\). It leaves room for a theorem specifically using
\[
P(g)-\alpha(M)\ll\varepsilon.
\]
Such a theorem would need local replacement competitors or an elliptic argument explaining why removable Ricci-active packets cannot persist in an almost minimizing metric. That information is not contained in the input-independent version of 52.KS.

## 5. The exact replacement needed for Palais–Smale selection

For a fixed-weight segment, put
\[
D(t)=\int_Mw|Q(g(t))|^2,
\qquad
R(t)=\int_Mr_\varepsilon(g(t))^4|Q(g(t))|^2,
\]
and
\[
A(t)=\max\left\{
1,\ \sup_M\frac{r_\varepsilon(g(t))^4}{w}
\right\}.
\]
Then
\[
R(t)\le A(t)D(t),\qquad
\int_0^T D(t)\,dt\le P(g(0))-\alpha(M).
\]
Define the **output-compatible dissipation time**
\[
\Theta(T)=\int_0^T A(t)^{-1}\,dt.
\]
It follows directly that
\[
\boxed{
\inf_{0<t<T}R(t)
\le
\frac{P(g(0))-\alpha(M)}{\Theta(T)}.
}
\tag{26}
\]

Thus a sufficient replacement for 52.KS is:

\[
\sum_n\Theta_n=\infty
\]
along energy-decreasing frozen-weight segments, together with a uniform Sobolev bound at the selected times. No uniform segment lifespan and no two-sided hard-radius comparison are needed.

For a sequence with excess \(\delta_i\), the finite-segment version is simply
\[
\frac{\delta_i}{\Theta_i}\longrightarrow0.
\tag{27}
\]
This is the precise resource the selection argument consumes. A one-sided estimate preventing shrinkage of the input radius is not enough: it does not control the factor \(A(t)\) when the output radius grows.

### A better radius for adaptive weights

A threshold-averaged radius removes the discontinuity in (25):
\[
\mathfrak r_\varepsilon(x)
=
\left[
\frac1\varepsilon
\int_\varepsilon^{2\varepsilon}r_a(x)^4\,da
\right]^{1/4}.
\tag{28}
\]
It has three useful properties:
\[
r_\varepsilon\le\mathfrak r_\varepsilon\le r_{2\varepsilon},
\qquad
|\mathfrak r_\varepsilon(x)-\mathfrak r_\varepsilon(y)|
\le d(x,y),
\tag{29}
\]
and
\[
\int_{B(x,\mathfrak r_\varepsilon(x))}|\mathrm{Rm}|^2
\le2\varepsilon.
\tag{30}
\]
The Lipschitz estimate follows from Minkowski’s inequality. Under smooth metric convergence, continuity follows by integrating the generalized inverse of the ball-energy function over the threshold parameter; its exceptional threshold values form a measure-zero set.

Crucially,
\[
\int r_\varepsilon^4|Q|^2
\le\int\mathfrak r_\varepsilon^4|Q|^2.
\tag{31}
\]
An adaptive weight comparable to the current \(\mathfrak r_\varepsilon^4\) therefore selects the required residual and retains small curvature energy on its spatial scales.

For such an adaptive flow, \(\partial_tw\) is absent from both the global dissipation law and (6). This permits measurable-in-time coefficient constructions more readily than a formulation requiring differentiability of the radius with respect to the metric. The substantive analytic theorem becomes existence for sufficient total adaptive time, intrinsic cutoffs, and Sobolev persistence—not two-sided comparison with the initial hard radius.

## 6. A flow-free possibility: weighted metric slope and elliptic selection

There is a natural alternative that adds no higher-order term to \(P\). On the space of smooth metrics define
\[
\|h\|_{\mathfrak r,g}^2
=
\int_M\mathfrak r_\varepsilon(g)^{-4}|h|_g^2\,d\mu_g,
\]
and let \(d_{\mathfrak r}\) be its path distance. At a smooth metric, its dual differential norm is exactly
\[
\|DP_g\|_{\mathfrak r,*}^2
=
\int_M\mathfrak r_\varepsilon(g)^4|Q(g)|^2\,d\mu_g.
\tag{32}
\]

Suppose Ekeland’s variational principle produces a point \(h\) satisfying
\[
P(v)\ge P(h)-\eta\,d_{\mathfrak r}(v,h)
\]
for nearby metrics \(v\). Differentiation along smooth metric variations gives
\[
\int_M\mathfrak r_\varepsilon(h)^4|Q(h)|^2
\le\eta^2.
\tag{33}
\]
For an input with \(P(g)\le\alpha+\delta\), the usual choice \(\eta=\sqrt\delta\) would yield the desired residual directly.

A proximal version minimizes
\[
P(h)+\frac1{2\tau}d_{\mathfrak r}(h,g)^2.
\tag{34}
\]
Its energy inequality gives
\[
d_{\mathfrak r}(h,g)^2\le2\tau\delta,
\]
and its metric slope estimate gives
\[
\int\mathfrak r_\varepsilon(h)^4|Q(h)|^2
\le\frac{2\delta}{\tau}.
\tag{35}
\]
This is an implicit fourth-order variational mechanism. The added term is a distance penalty, not a curvature regularization.

The actual mathematical issue is **completion and elliptic regularity**, not the formal variational inequality. Smooth metrics with this weak path norm need not form a complete space. A workable formulation is the lower-semicontinuous relaxation of \(P\) on the metric completion, followed by a theorem identifying finite-slope points as sufficiently regular metrics.

The theorem shape needed is concrete:

> A relaxed finite-slope point with a uniform Sobolev inequality and small curvature energy on its \(\mathfrak r_\varepsilon\)-balls has a uniformly elliptic metric representative, admits harmonic coordinates, and lies locally in \(W^{4,2}\). Its distributional gradient is an \(L^2(\mathfrak r_\varepsilon^4d\mu)\) tensor satisfying the slope estimate.

Once this is established, smooth approximation in \(W^{4,2}\) preserves \(P\) and \(Q\) in \(L^2\), so the selected relaxed metrics give genuine smooth Palais–Smale metrics. The coupled elliptic system (9), the Bianchi estimates (16)–(19), and the Step-52 residual compactness argument are precisely the relevant tools.

The weighted distance has a useful geometric feature. Along a homothetically shrinking curvature bubble of scale \(\ell\), carrying more than \(2\varepsilon\) curvature energy,
\[
\mathfrak r_\varepsilon\asymp\ell,\qquad
\|\partial_\ell g_\ell\|_{\mathfrak r,g_\ell}
\asymp\ell^{-1}.
\]
Consequently its model path length is
\[
\int\frac{d\ell}{\ell}=\infty.
\tag{36}
\]
The weighting puts standard curvature concentration at infinite path length, while allowing small-amplitude high-frequency ripples to have finite length. A completion theorem must therefore address subthreshold roughness; the elliptic finite-slope equation is the mechanism capable of resolving that roughness.

A Sobolev constraint cannot simply be inserted into (34) and then ignored: an active constrained extremum adds a variational multiplier. The plain \(Q\) estimate requires unrestricted local variations, or a proof that the selected point lies strictly inside the chosen Sobolev class.

## Scientific synthesis

The Weyl part is not the principal obstruction to a localized concentration argument. Equations (5)–(15) control it through an exact Lovelock cancellation and a Ricci–scalar coercive multiplier. The remaining substantive connections are intrinsic critical-energy cutoffs, Sobolev persistence, and a selection representation that follows the output scale.

Three distinct theorem forms now emerge:

1. **A near-minimum parabolic theorem**, using the small total dissipation budget together with local replacement geometry.
2. **An adaptive-weight theorem**, using the continuous radius (28) and sufficient output-compatible time.
3. **An elliptic metric-slope theorem**, giving Palais–Smale selection through completion and fourth-order regularity, without a flow lifespan theorem.

The relevant source families are localized fourth-order estimates in the supplied Streets paper; Kuwert–Schätzle concentration estimates and their ambient-cutoff mechanism; Lovelock/Chern–Weil first variations with scalar multipliers; Uhlenbeck small-curvature gauges coupled to the torsion equation; and Ekeland or minimizing-movement theory for weak Riemannian path distances.