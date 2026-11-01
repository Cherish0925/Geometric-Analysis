# TTCS Independent Branch Record

```json
{
  "step_id": 10,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step10_execute_pivot_volume_gap_and_epsilon_regularization.md",
    "Sessions/S0910A02/workspace/plans/step8_projection_bridge_target.md",
    "Sessions/S0910A02/workspace/notes/step8_preceptor_review_positive_branch.md",
    "Knowledge/objects/papers/1707.05511-ε-regularity-for-shrinking-Ricci-solitons-and-Ricci-flows--77d745e7dfc7--9e2e179bf3bc/object.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step10.md",
    "Sessions/S0910A03/workspace/notes/step8_cover_mean_transport_and_model_scope_corrections.md"
  ]
}
```

## Task

Given the Step 10 pivot, propose concrete Execute-level mathematical attacks on the true pinched regularity bottleneck for Yau Problem 26. The goal is not final writing but actionable research: how to refute or salvage a Cheeger--Tian-style pointwise epsilon-regularity theorem under only ||Ric-g||_{L∞}≤δ; how to use high-frequency transverse-traceless/Weyl packet perturbations as counterexample probes; how to extract a weaker Li/Cheeger--Tian scale-selection or smoothing theorem; and how to connect any surviving regularity to the simply-connected volume gap and the A01/A03 accessible-cover bridge. Give a prioritized set of candidate lemmas/probes with assumptions, expected calculations, failure modes, and what evidence would change the route.

## Output

Below is a prioritized set of concrete mathematical attacks on the real \(C^0\)-Ricci pinched regularity bottleneck. The organizing point is that a Cheeger–Tian pointwise theorem for exact Einstein metrics uses an elliptic curvature equation; under only
\[
\|\operatorname{Ric}_g-g\|_{L^\infty}\le \delta
\]
one has an elliptic metric equation with \(L^\infty\) right-hand side, so second derivatives of the metric can behave like Calderón–Zygmund singular integrals. The right research split is therefore: first test whether pointwise curvature control is actually false; then preserve only the parts that survive—scale selection, smoothing, harmonic-radius-on-covers, and weak projection/flux identities.

---

## 1. Microlocal TT/Weyl packet test: single-frequency packets probably do **not** beat Ricci

Work on a nearly flat chart and perturb
\[
g_\varepsilon=g_0+a\,e^{ik x\cdot \xi}q
\]
with \(q\) constant symmetric. At Euclidean principal-symbol level,
\[
2\,\operatorname{Ric}'_\xi(q)_{ij}
=
|\xi|^2q_{ij}
+\xi_i\xi_j\operatorname{tr}q
-\xi_i\xi^a q_{aj}
-\xi_j\xi^a q_{ai}.
\]

If \(q\) is transverse traceless relative to \(\xi\), then
\[
\operatorname{Ric}'_\xi(q)\sim \frac12|\xi|^2q,
\qquad
W'_\xi(q)\sim |\xi|^2q.
\]
Thus the Ricci defect and Weyl amplitude have the same principal size \(ak^2\). Keeping \(\|\operatorname{Ric}'\|_\infty\le \delta\) forces \(\|W'\|_\infty\lesssim \delta\).

If \(q\) lies in the principal kernel of \(\operatorname{Ric}'_\xi\), then \(q=\xi\odot v\), a pure-gauge symbol, and the principal Weyl symbol also vanishes. So a naive high-frequency TT packet is not the right counterexample.

**Value of this calculation.** It separates two mechanisms:

- single WKB TT waves do not refute pointwise regularity;
- any real counterexample must use elliptic \(L^\infty\to\mathrm{BMO}\) behavior, collapse, nonlinear cancellation, or gauge concentration rather than one clean transverse wave.

This is the first sanity computation because it prevents chasing a visually plausible but symbolically wrong Weyl packet.

---

## 2. Strong counterexample probe: DeTurck–Calderón–Zygmund tensor spikes

This is the most decisive local test against a Cheeger–Tian-style pointwise theorem for \(C^0\)-Ricci pinching.

Let \((M^4,g_0)\) be a smooth Einstein metric with
\[
\operatorname{Ric}_{g_0}=g_0.
\]
Use Bianchi-gauged Einstein operator
\[
\Phi_{g_0}(g)=\operatorname{Ric}_g-g+\delta_g^*\beta_{g_0}(g),
\]
whose linearization at \(g_0\) is elliptic:
\[
Lh=D\Phi_{g_0}(h)
=
\frac12\nabla^*\nabla h-\mathring R(h)-h
\]
up to convention.

Construct smooth symmetric tensors \(h_j\) satisfying, in a chosen chart,

\[
\beta_{g_0}h_j=0,
\qquad
\|Lh_j\|_{L^\infty}\le 1,
\qquad
\|h_j\|_{C^1}\le C,
\qquad
\|\nabla^2h_j\|_{L^2}\le C,
\]
but
\[
| \Pi_W(\nabla^2h_j)(p_j)|\ge j,
\]
where \(\Pi_W\) denotes the algebraic part of second derivatives feeding the Weyl tensor.

The source family is standard elliptic singular-integral behavior: bounded right-hand sides for Poisson-type equations whose Hessians have arbitrarily large point values while \(L^2\) stays controlled. The exact source topic to consult is:

> Calderón–Zygmund examples for the Poisson equation with bounded right-hand side and unbounded Hessian, plus tensor-valued Bianchi/de Donder projection.

Now set
\[
g_j=g_0+a_jh_j,
\qquad
a_j=j^{-3/4}.
\]
Then \(g_j\) is positive definite for large \(j\), and the expansion gives
\[
\operatorname{Ric}_{g_j}-g_j
=
a_jLh_j
+
O\!\left(a_j^2|\nabla^2h_j|+a_j^2|\nabla h_j|^2\right)
\]
in Bianchi gauge. Hence
\[
\|\operatorname{Ric}_{g_j}-g_j\|_{L^\infty}
\le
C(a_j+a_j^2j)
=
O(j^{-3/4}+j^{-1/2})
\to0.
\]

Meanwhile,
\[
|W(g_j)|(p_j)
\ge
c\,a_jj-C
=
c\,j^{1/4}-C
\to\infty.
\]

The \(L^2\) curvature added by the perturbation satisfies
\[
\int | \operatorname{Rm}(g_j)-\operatorname{Rm}(g_0)|^2
\lesssim
a_j^2\|\nabla^2h_j\|_{L^2}^2+o(1)
\to0.
\]

To violate a scale-\(r\) Cheeger–Tian estimate, choose \(r_j\to0\) with
\[
r_j^2 |W(g_j)(p_j)|\to\infty,
\qquad
r_j^4\to0.
\]
For instance, with \(|W(p_j)|\sim j^{1/4}\), take \(r_j=j^{-1/16}\). Then
\[
\int_{B_{r_j}(p_j)}|\operatorname{Rm}(g_j)|^2\to0
\]
because the background contribution is \(O(r_j^4)\), while
\[
\sup_{B_{r_j/2}(p_j)}|\operatorname{Rm}(g_j)|
\gg r_j^{-2}.
\]

**Stress points.**

- The Bianchi projection must preserve a Weyl-active Hessian component at \(p_j\), not convert the spike into pure gauge.
- The nonlinear term \(a_j^2|\nabla^2h_j|\) must remain \(o(1)\) in \(L^\infty\); the choice \(a_j=j^{-3/4}\) does this.
- One should verify that the full gauge vector \(\beta_{g_0}(g_j)\) contributes only \(O(a_j^2j)\) after differentiating.
- If one wants a closed-manifold version, the elliptic inverse should be taken after removing the finite-dimensional kernel and arranging the usual orthogonality conditions.

**Route-moving observation.** If this construction is completed, the strong pointwise theorem is false even with
\[
\|\operatorname{Ric}-g\|_{L^\infty}\to0
\]
and arbitrarily small local \(L^2\) curvature at the tested scale. Then the regularity infrastructure must be weak: scale selection, smoothing, harmonic radius, and pairings against smooth test tensors.

---

## 3. Explicit nonlinear collapsed model: diagonal \(T^2\)-bundle metric

A more geometric counterexample probe is the metric
\[
g_u
=
dx^2+dy^2+e^{2u(x,y)}d\theta^2+e^{-2u(x,y)}d\phi^2
\]
on \(D^2\times T^2_\ell\), where \(T^2_\ell\) has small fiber area.

In the orthonormal frame
\[
e_1=\partial_x,\quad e_2=\partial_y,\quad
e_3=e^{-u}\partial_\theta,\quad e_4=e^{u}\partial_\phi,
\]
one obtains the exact Ricci structure
\[
\operatorname{Ric}_{ab}=-2u_a u_b,\qquad a,b\in\{1,2\},
\]
\[
\operatorname{Ric}_{33}=-\Delta u,\qquad
\operatorname{Ric}_{44}=+\Delta u,
\]
and no second trace-free Hessian term appears in Ricci. By contrast, the Riemann tensor contains
\[
R_{a3b3}\sim -u_{ab}-u_a u_b,\qquad
R_{a4b4}\sim +u_{ab}-u_a u_b.
\]
Thus
\[
|W|
\ge
c\,|(\nabla^2u)^\circ|
-
C(|\Delta u|+|\nabla u|^2).
\]

Now choose \(u_j\) solving a scalar Calderón–Zygmund spike problem:
\[
\|\nabla u_j\|_{L^\infty}\le \eta_j,\qquad
\|\Delta u_j\|_{L^\infty}\le \eta_j,
\]
\[
|(\nabla^2u_j)^\circ(p_j)|\ge \eta_j j,
\qquad
\|\nabla^2u_j\|_{L^2}\le C\eta_j.
\]
Taking \(\eta_j=j^{-1/2}\) gives
\[
\|\operatorname{Ric}_{g_{u_j}}\|_{L^\infty}\le Cj^{-1/2},
\qquad
|W(g_{u_j})(p_j)|\ge c j^{1/2}.
\]
The total curvature energy on \(D^2\times T^2_\ell\) satisfies
\[
\int |\operatorname{Rm}|^2
\lesssim
\ell^2\,\|\nabla^2u_j\|_{L^2(D^2)}^2
+
O(\ell^2\eta_j^4),
\]
so choosing \(\ell\) small makes the absolute energy arbitrarily small without changing the pointwise Weyl spike.

**Why this model matters.**

It shows, in a completely geometric form, why Naber–Zhang Proposition 6.4 gives only harmonic radius on the local cover, not pointwise curvature. After unwrapping \(T^2_\ell\), the local universal cover has a fixed \(C^1\)-harmonic chart when \(u_j\) is \(C^1\)-small, yet \(|W|\) blows up.

**Positive-normalized adaptation.**

To fit \(\operatorname{Ric}\approx g\), implant the same principal construction into a tiny chart of an Einstein \(4\)-manifold. The leading cancellation is local and principal-symbolic; ambient curvature contributes lower-order terms involving \(u\), \(\nabla u\), and the background curvature. If the spike scale \(s_j\) is much smaller than the chart scale and
\[
\|u_j\|_{C^1}\to0,
\]
those lower-order terms are dominated by the chosen \(C^0\)-Ricci tolerance.

This model is also a useful collapsed laboratory for checking Li smoothing, local covers, and flux identities.

---

## 4. Weaker theorem to extract: Li/Cheeger–Tian scale selection

The source-supported substitute for pointwise regularity is the scale-selection theorem quoted in Ge–Jiang and attributed to Cheeger–Tian/Li:

For every \(\varepsilon>0\), there exist \(\delta(\varepsilon)>0\) and \(a(\varepsilon)>0\) such that if a \(4\)-manifold satisfies
\[
|\operatorname{Ric}|\le 3
\]
on \(B_r(x)\), \(r\le1\), and
\[
\int_{B_r(x)}|\operatorname{Rm}|^2\le \delta(\varepsilon),
\]
then for some
\[
s\ge a(\varepsilon)r
\]
one has
\[
s^4\fint_{B_s(x)}|\operatorname{Rm}|^2\le \varepsilon.
\]

Li’s paper further phrases the collapsed quantity as a volume-normalized energy:
\[
\frac{r^4}{\operatorname{Vol}(B_r(x))}
\int_{B_r(x)}|\operatorname{Rm}|^2.
\]
Under bounded Ricci, this is the quantity that can be made small on a comparable smaller concentric ball. It does not give pointwise curvature for the original metric.

**Mathematical extraction target.**

A useful proposition should have the following exact form:

Let \((M^4,g)\) satisfy \(|\operatorname{Ric}|\le K\) on \(B_{2r}(p)\). If
\[
\int_{B_{2r}(p)}|\operatorname{Rm}|^2\le \delta_L(\varepsilon),
\]
then there is \(s\in[a_Lr,r]\) such that
\[
\frac{s^4}{\operatorname{Vol}(B_s(p))}
\int_{B_s(p)}|\operatorname{Rm}|^2
\le \varepsilon.
\]

The constants depend only on the Ricci bound after scaling and on \(\varepsilon\). This is the precise weak replacement for collapsed \(L^2\) smallness.

**Smoothing corollary to extract.**

Li’s smoothing theorem gives:

If \(|\operatorname{Ric}(g_0)|\le K\) and every \(r\)-ball satisfies the suitable small volume-normalized \(L^2\) curvature condition, then the Ricci flow exists for
\[
t\in[0,T),
\qquad
T\ge C\min(r^2,K^{-1}),
\]
and
\[
|\operatorname{Rm}(g(t))|\le C t^{-1}.
\]

The smoothed metric is useful for topology, chopping, and \(F\)-structure arguments, but the initial pinching
\[
\operatorname{Ric}_{g_0}\approx g_0
\]
is not automatically preserved in the quantitative form needed for Einstein obstruction theory.

**Stress points.**

- Scale selection is not pointwise curvature control.
- Smoothing can alter the Ricci defect in ways not visible from \(C^0\) pinching alone.
- The original metric remains the one to use in obstruction pairings; the smoothed metric is mainly a topological/geometric comparison device.

**Route-moving observation.** If the DeTurck–CZ or \(T^2\)-bundle probes work, Li’s theorem becomes the correct analytic backbone: use it to isolate good averaged scales and to smooth where topology rather than exact curvature is needed.

---

## 5. Weak Pohozaev/projection bridge: pair Ricci defect only against smooth tensors

The strongest surviving analytic bridge for the positive four-dimensional branch is not pointwise curvature; it is an integral identity.

Assume a pinched sequence has a controlled two-scale region with an \(\mathbb R^4/\mathbb Z_2\) neck and an Eguchi–Hanson bubble. Let \(t_i\) be the gluing scale. Let \(\phi_i\) be a cutoff approximate cokernel tensor transported from the Eguchi–Hanson model.

One wants
\[
\int_{\Omega_i}
\langle \operatorname{Ric}(g_i)-g_i,\phi_i\rangle\,d\mu_{g_i}
=
t_i\,\mathcal O(R_+(p),\mathrm{orientation},\mathrm{rotation})
+
o(t_i).
\tag{P}
\]
Since
\[
\|\operatorname{Ric}(g_i)-g_i\|_{L^\infty}\le\delta_i,
\]
the left side is controlled by
\[
\delta_i\|\phi_i\|_{L^1}.
\]
On the Eguchi–Hanson core,
\[
|\phi_i|_{g_i}\sim t_i^{-1}|\phi|_{h_{EH}},
\qquad
d\mu_{g_i}\sim t_i^2\,d\mu_{h_{EH}},
\]
so the core contribution gives
\[
\|\phi_i\|_{L^1}=O(t_i).
\]
Then (P) implies
\[
\mathcal O(R_+(p),\mathrm{orientation},\mathrm{rotation})
=
O(\delta_i)+o(1).
\]

**Essential calculation.**

The neck \(L^1\)-norm must be computed with the exact decay of the obstruction mode. If the model tensor decays like \(\rho^{-4}\), a naive annular integral may produce
\[
t_i\int^{\rho_{\max}}\rho^{-1}d\rho
=
t_i\log\rho_{\max}.
\]
A logarithm would require an additional relation between \(\delta_i\) and \(t_i\), which Yau-26 does not provide. Two ways to avoid this:

1. choose a compactly supported dual tensor with controlled adjoint error;
2. use a Komar/rotation flux identity across annular hypersurfaces, where the obstruction appears as a flux coefficient rather than an \(L^1\)-large bulk pairing.

**Komar version.**

For a rotation field \(X\) on the cone,
\[
d(*dX^\flat)=2*\operatorname{Ric}(X,\cdot)
\]
when \(X\) is Killing, up to the known Einstein-constant contribution. For
\[
\operatorname{Ric}=g+E,
\]
the uncontrolled part is only
\[
2*E(X,\cdot),
\]
which is bounded by \(\delta_i\) times explicit annular geometry. Derivatives of \(E\) never appear.

**Stress points.**

- The annular geometry must be strong enough: \(C^{1,\alpha}\cap W^{2,p}\) control in a Bianchi/ALE-compatible gauge.
- Bubble trees require summing fluxes over several necks.
- Rank-drop collapsed regions may not contain a clean ALE annulus.
- The algebraic obstruction from \(R_+(p)\) is first-order only; higher-order gluing obstructions remain separate.

**Route-moving observation.** If (P) can be proved under \(C^1/W^{2,p}\) annular control, then \(C^0\) Ricci pinching suffices for first-obstruction projection even though pointwise curvature regularity is false.

---

## 6. Accessible-cover bridge: what survives from Naber–Zhang

Naber–Zhang Proposition 6.4 gives the correct collapsed regularity package:

If a bounded-Ricci ball is GH-close at fixed scale to
\[
\mathbb R^{k-\ell}\times Z^\ell,\qquad \ell\le3,
\]
and the fibered nilpotency rank is maximal, with model noncollapsing radius bounded below, then the local universal cover has a definite \(C^1\)-harmonic radius.

Proposition 6.5 explains exactly why this does not yield pointwise curvature unless one adds either

\[
|\nabla\operatorname{Ric}|\le\Lambda
\]
or the metric is Einstein.

For Yau-26 pinched metrics, the usable conclusion is:

\[
g_i\to g_\infty
\quad\text{in}\quad
C^{1,\alpha}\cap W^{2,p}_{\mathrm{loc}}
\]
on fixed cover charts, and
\[
\operatorname{Ric}_{g_\infty}=\pm g_\infty
\]
after passing to the limit. The limit is smooth by elliptic bootstrapping, but the approximating curvatures may still spike.

Together with the normal-cover mean transport lemma, any \(F_i\ge0\) density whose downstairs local mean is small also has small mean upstairs:
\[
\fint_{B_a(\tilde p_i)}\pi_i^*F_i
\le
C
\fint_{B_a(p_i)}F_i.
\]
This is enough for the LeBrun/Ishida calibrated branch: small lifted mean plus harmonic-coordinate compactness produces the forbidden local Einstein germ with calibrated \(W^+\) spectrum.

For the positive branch, the same cover mechanism does not by itself contradict anything. Its role is to supply fixed charts and smooth Einstein limits so that the Pohozaev/Komar projection can be applied near orbifold/ALE necks.

---

## 7. Simply-connected volume gap: how the corrected regularity feeds the global problem

The finite-cover amplifier is clear in dimension four:

If every simply connected positively pinched \(4\)-manifold has a uniform volume lower bound, then all positively pinched \(4\)-manifolds have a uniform volume lower bound, hence finitely many diffeomorphism types by Cheeger–Naber plus Myers/Bishop–Gromov.

The real missing theorem is therefore:

\[
\|\operatorname{Ric}-g\|_{L^\infty}\le\delta
\quad\text{and}\quad
\pi_1(M)=0
\quad\Longrightarrow\quad
\operatorname{Vol}(M,g)\ge v(\delta)>0?
\]

The corrected regularity picture suggests a decomposition of any hypothetical collapsed simply connected sequence:

1. **Maximal-rank regular collapsed part.**  
   Naber–Zhang gives cover harmonic radius. Li smoothing can produce bounded-curvature comparison metrics. Such regions look like nil/torus fibered pieces after unwrapping.

2. **Rank-drop or singular-fiber part.**  
   This is where fiber fundamental groups die and where K3-type examples concentrate curvature in Ricci-flat collapse. In the positive pinched case, Chern–Gauss–Bonnet gives
   \[
   8\pi^2\chi
   =
   \int\left(|W|^2+\frac{s^2}{24}-\frac{|E|^2}{2}\right),
   \]
   and if total volume collapses, the scalar-volume term becomes small, so \(\chi\) must be carried by Weyl energy.

3. **High-\(\chi\) stress.**  
   For \(M_k=\#_k(S^2\times S^2)\),
   \[
   \int|W|^2\ge 16\pi^2k-O_\delta(1).
   \]
   Thus any near-positive-Einstein metric on this family must contain many curvature packets or a strongly singular collapsed docking geometry.

A useful candidate lemma would be:

> On a positively pinched collapsed \(4\)-ball, if the fibered nilpotency rank drops from the maximal value, then either a definite amount of Weyl energy appears at a comparable scale, or the ball belongs to a controlled singular-fiber model.

This would turn collapse topology into countable curvature packets. It still would not alone bound \(\chi\), but it would locate the entire obstruction in rank-drop geometry rather than in smooth regular collapse.

**Route-moving observations.**

- If explicit Sha–Yang/Burdick/Perelman-style metrics can be tuned so that
  \[
  \inf \|\operatorname{Ric}-ag\|/a\to0
  \]
  on \(\#_k(S^2\times S^2)\), then the positive branch becomes a direct Einstein-existence stress test.
- If one proves a uniform lower bound for that pinching defect on high connected sums, then the positive branch gains a new rigidity mechanism.
- If DeTurck–CZ spikes can be implanted globally while preserving \(\operatorname{Ric}\approx g\), then any proof of the volume gap must be topological/collapsed, not pointwise-curvature based.

---

## 8. Source work needed for exact constants and normalization

The immediate source targets are precise and limited:

1. Cheeger–Tian, *Curvature and injectivity radius estimates for Einstein 4-manifolds*, JAMS 2006: exact collapsed Einstein \(L^2\) estimate and chopping mechanism.
2. Ye Li, *Smoothing Riemannian metrics with bounded Ricci curvatures in dimension four*, Adv. Math. 2010: the first paper behind the scale-selection theorem quoted in Li II and Ge–Jiang.
3. Calderón–Zygmund constructions for Poisson equations with bounded right-hand side and unbounded Hessian.
4. DeTurck-gauge local prescribed-Ricci elliptic theory for turning tensor Poisson examples into genuine metric perturbations.
5. Biquard–Ozuch/Eguchi–Hanson obstruction normalization: exact tensor decay, flux coefficient, and \(R_+\) algebra.

The decisive near-term mathematical fork is sharp: either the DeTurck–CZ or \(T^2\)-bundle probes produce a rigorous pinched counterexample to pointwise \(\varepsilon\)-regularity, or an unexpected elliptic complex estimate blocks them. In the first case, the research should lean fully into weak projection, Li smoothing, and Naber–Zhang cover charts. In the second, the hidden estimate would be a major new regularity theorem worth isolating.