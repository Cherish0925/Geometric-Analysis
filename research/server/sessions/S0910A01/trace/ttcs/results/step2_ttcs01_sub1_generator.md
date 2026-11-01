# TTCS Independent Branch Record

```json
{
  "step_id": 2,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step2_mechanisms_analysis.md",
    "Skills/qiushi-yau26/references/research/20260910.tex"
  ]
}
```

## Task

Yau Problem 26 asks whether for each dimension n, there exist dimension-only constants c_n < C_n such that any closed connected smooth Riemannian n-manifold (M,g) with c_n g ≤ Ric_g ≤ C_n g admits an Einstein metric h on M. The problem decomposes into positive and negative branches P_n^+ and P_n^-. Through quantitative Chern-Weil analysis combined with Seiberg-Witten theory, the positive branch in dimension 4 is strongly protected: all known no-Einstein 4-manifolds have δ_+ bounded away from 0 (HT-violating: δ_+ ≥ 0.366; LeBrun SW-obstructed: δ_+ ≥ 1 since no positive scalar curvature). The NEGATIVE branch is the live territory. For LeBrun manifolds M = X#k CPbar² with A = c₁²(X), combining LeBrun's ∫s²dV ≥ 32π²A with CGB volume bounds gives δ_- ≥ C/√A for varying manifolds with A→∞, which tends to 0. So varying-manifold counterexamples are not ruled out by current integral bounds. The central unsolved problems are: (A) Can tight two-sided negative Ricci pinching (Ric ≈ -g in operator norm) be constructed on manifolds with no Einstein metric? Lohkamp gives one-sided Ric < 0 flexibility and h-principle for open relations, but not two-sided bounds. DeTurck prescribed-Ricci is local. Min-Oo/Jäckel need additional conditions (d²max|K| bounded or sec < 0). (B) Alternatively, can a new existence theorem work with ONLY Ricci pinching, without full curvature/derivative/diameter control? All known existence theorems require more than Ricci. Propose genuinely new mathematical mechanisms, constructions, or proof strategies that could resolve either direction. For a counterexample mechanism: how could one construct a metric with all Ricci eigenvalues in (-1-ε, -1+ε) on a LeBrun manifold with the Weyl curvature free? For an existence mechanism: what new analytic, variational, or topological principle could extract Einstein existence from pure Ricci pinching, possibly through a new flow, functional, or topological constraint?

## Output

The live variable is Weyl curvature.  In dimension four, \(\Ric\approx -g\) fixes
\[
s\approx -4,\qquad E=\Ric-\frac{s}{4}g\approx 0,
\]
but leaves \(W^\pm\) and the volume ledger free enough to carry \(\chi,\tau\).  For
\[
M=X\#k\,\overline{\mathbb{CP}}^{\,2},\qquad A=c_1^2(X),
\]
the Chern–Weil/Seiberg–Witten estimate says roughly
\[
\delta^2 \gtrsim \frac{k-2A/3}{3(A-k)}.
\]
Thus a LeBrun counterexample family should take
\[
k=\Big(\frac23+\theta\Big)A,\qquad \theta\sim \varepsilon^2,
\]
not \(k/A\) separated from \(2/3\).  The Ricci defect then has to be distributed over volume \(O(A)\), while \(W\) carries the topology.  This is an extensive, many-cell construction problem, not a tiny local surgery problem.

## 1. A concrete counterexample architecture: finite-volume \(\overline{\mathbb{CP}}^2\) Ric\(<0\) bolt plugs

A very sharp route would start from minimal general type surfaces already carrying exact \(\Ric=-g\).  The clean laboratory is
\[
X_{p,q}=\Sigma_p\times \Sigma_q
\]
with both factors hyperbolic of curvature \(-1\).  Then \(X_{p,q}\) is Einstein with \(\Ric=-g\), and
\[
A=c_1^2(X_{p,q})=8(p-1)(q-1),\qquad
\Vol(X_{p,q})=2\pi^2 A.
\]
Choose \(k\approx 2A/3+\theta A\), \(\theta>0\) tiny, and replace \(k\) disjoint balls by copies of a smooth plug
\[
P\cong \overline{\mathbb{CP}}^{\,2}\setminus B^4.
\]
Topologically this produces \(X\#k\overline{\mathbb{CP}}^{\,2}\), which LeBrun excludes from carrying any Einstein metric once \(k>2A/3\).

The missing geometric object is a family of plug metrics \(p_\eta\) on \(P\) satisfying:

\[
\|\Ric_{p_\eta}+p_\eta\|_{\op}<\eta,
\]
and whose outer \(S^3\)-edge data are \(C^2\)-close to the edge data of a geodesic sphere in the ambient \(\Ric=-g\) background.  More explicitly, if the outer hypersurface has induced metric \(\gamma_\eta\) and second fundamental form \(K_\eta\), one wants
\[
\|\gamma_\eta-\gamma_{\mathrm{hyp}}\|_{C^2}
+
\|K_\eta-K_{\mathrm{hyp}}\|_{C^1}
\le \eta .
\]
Then a short interpolation annulus should give
\[
\|\Ric+g\|_{\op}\le C\eta
\]
on the glued metric.

The most promising source family is not an ALE Ricci-flat bubble, because a Ricci-flat core has operator defect \(1\) relative to the target \(\Ric=-g\).  The right source family is instead exact Einstein metrics with Ric\(<0\) on disk bundles over \(S^2\): AdS Taub–Bolt metrics, Pedersen self-dual Einstein metrics, and related conformally compact Einstein fillings of Berger \(S^3\) conformal infinities.  In Bianchi IX form one studies metrics
\[
p=dt^2+a(t)^2(\sigma_1^2+\sigma_2^2)+b(t)^2\sigma_3^2
\]
on the disk bundle of Euler number \(-1\), with bolt smoothness
\[
a(0)=a_0>0,\qquad a'(0)=0,\qquad b(t)=t+O(t^3).
\]
At \(t=T\), the outer \(S^3\) has Berger data
\[
\gamma_T=a(T)^2(\sigma_1^2+\sigma_2^2)+b(T)^2\sigma_3^2,
\]
with shape eigenvalues \(a'(T)/a(T)\) and \(b'(T)/b(T)\).  A hyperbolic geodesic sphere has round data
\[
a=b=R,\qquad a'/a=b'/b=H.
\]
So the finite-dimensional matching problem is: can the bolt parameters and \(T\) make
\[
\frac{b(T)}{a(T)}\approx 1,\qquad
\frac{a'(T)}{a(T)}-\frac{b'(T)}{b(T)}\approx 0,
\]
while also matching the mean curvature and volume contribution?

The volume condition is important.  The LeBrun/Chern–Weil inequalities force any \(\delta\)-pinched metric on the near-threshold family to have
\[
\Vol(M)=2\pi^2 A+O(\delta A).
\]
Since \(k\sim 2A/3\), the average inserted-minus-removed volume per plug must be \(O(1)\), in fact tuned to \(O(\delta)\) on average.  A plug whose small mismatch is achieved only by an enormously long hyperbolic collar would have too much volume per blow-up.  Thus the decisive plug is a finite-size resonance: a Ric\(<0\) Einstein bolt whose outer \(S^3\) data nearly coincide with those of a finite-radius hyperbolic sphere, not merely an asymptotic end far away.

A figure worth having here would show:

- a large product surface \(X_{p,q}\) with \(O(A)\) disjoint balls;
- each ball replaced by an \(O(-1)\) bolt cell;
- \(|\Ric+g|\) concentrated only in interpolation annuli;
- \(W^-\) carrying the \(\overline{\mathbb{CP}}^{\,2}\) topology;
- the Chern–Weil quantities \(2\chi\pm3\tau\) tracked before and after insertion.

If the finite-radius bolt matching exists with error \(\eta\), choosing \(A\gg \eta^{-2}\) and
\[
k=\left\lceil \frac23 A+c\eta^2 A\right\rceil
\]
would fit the known LeBrun lower estimate and would create a direct minus-sign counterexample sequence.

## 2. A relative two-sided Lohkamp principle with Chern–Weil charge accounting

Lohkamp’s one-sided flexibility suggests a stronger but much more rigid local principle:

For a prescribed handle or disk-bundle cell \(H\), construct a metric with
\[
-1-\varepsilon<\lambda_i(\Ric^\#)<-1+\varepsilon
\]
and with chosen outer edge data, while the Weyl curvature supplies a prescribed Chern–Weil charge.

In four dimensions the charge bookkeeping is unavoidable.  For any cell-like region,
\[
2\chi\pm 3\tau
\sim
\frac1{4\pi^2}\int
\left(
2|W^\pm|^2+\frac{s^2}{24}-\frac{|E|^2}{2}
\right).
\]
A hypothetical two-sided Lohkamp theorem cannot simply work for every handle decomposition in dimension four, because tight Ricci pinching forces \(2\chi>3|\tau|\).  The cell library would need charge types whose total satisfies this inequality.  LeBrun near-threshold manifolds do satisfy it, so they are exactly the natural test class.

The local equations in Gaussian form make the difficulty explicit.  Write
\[
g=dt^2+\gamma(t),\qquad K=\frac12\gamma'(t).
\]
Then schematically
\[
\Ric_{tt}=-\operatorname{tr}_\gamma K'-\operatorname{tr}_\gamma(K^2),
\]
\[
\Ric_{ti}=\nabla^jK_{ij}-\partial_i\operatorname{tr}K,
\]
\[
\Ric_{ij}=\Ric_{\gamma,ij}-K'_{ij}-(\operatorname{tr}K)K_{ij}
+2K_i{}^aK_{aj}.
\]
The Ricci target \(-g+O(\varepsilon)\) becomes a constrained evolution system for \((\gamma,K)\).  The Weyl degrees of freedom are the tracefree parts of the hypersurface curvature and shape operator.  A genuine two-sided construction would use those tracefree variables as a reservoir while keeping the Ricci equations almost isotropic.

The distinguishing calculation is finite and concrete in cohomogeneity-one cells.  For the Bianchi IX ansatz above, the Ricci eigenvalues are explicit ODE expressions in \(a,b,a',b',a'',b''\).  One can search for cell trajectories whose endpoints match round or nearly round \(S^3\) data, while
\[
\max_t\max_i|\lambda_i(t)+1|<\varepsilon.
\]
If such cells exist for the \(-1\) disk bundle, the LeBrun route becomes geometrically plausible.  If the ODE phase portrait keeps a definite distance from round hyperbolic edge data, the bolt-plug mechanism loses its simplest form.

## 3. Ricci corrugation: cancel \(E\) while dumping curvature into \(W\)

Another counterexample mechanism would be a high-frequency correction scheme.  The Ricci operator contains second derivatives of the metric.  A perturbation of size \(\rho^2\),
\[
h_\rho=\rho^2 a(x)\cos(\phi(x)/\rho),
\]
has small \(C^0\) size but contributes \(O(1)\) to curvature.  At principal-symbol level, the linearized Ricci tensor has the form
\[
2\sigma_\xi(D\Ric)(h)_{ij}
=
|\xi|^2 h_{ij}
+\xi_i\xi_j\operatorname{tr}h
-\xi_i\xi^a h_{aj}
-\xi_j\xi^a h_{ai}.
\]
By superposing several wave directions \(\xi\), one can ask whether arbitrary small tracefree Ricci errors \(E\) can be canceled while the leading oscillatory curvature mostly lands in \(W\).  The scalar part could then be corrected by a conformal or warped adjustment.

This would be a Ricci analogue of Nash-style stress absorption, but with an elliptic second-order operator rather than a first-order metric relation.  The Bianchi identity imposes divergence relations, so the wave packets must be arranged in balanced families.  The core algebraic test is the span of the symbol images above: for a finite set of covectors \(\{\xi_\alpha\}\), does
\[
\sum_\alpha \sigma_{\xi_\alpha}(D\Ric)(h_\alpha)
\]
cover all tracefree symmetric tensors after quotienting diffeomorphism directions?  In dimension four, the remaining curvature can be placed in \(W^\pm\), precisely the part allowed by the problem.

A successful corrugation theorem would have the following shape:

Given a metric with \(\Ric<0\) and with Chern–Weil-compatible topology, for every \(\varepsilon>0\) there is a \(C^0\)-nearby metric \(g_\varepsilon\) such that
\[
\|\Ric_{g_\varepsilon}+g_\varepsilon\|_{\op}<\varepsilon,
\]
while \(|W_{g_\varepsilon}|\) may become large or oscillatory.

This would turn Lohkamp’s one-sided flexibility into a two-sided pinching machine.  The observable signature would be sequences with small Ricci spectral width and rapidly growing Weyl oscillation, with Chern–Weil integrals converging to the required \(\chi,\tau\).

## 4. A rival four-dimensional protection mechanism: the full monopole cube

The current LeBrun estimate uses Seiberg–Witten theory but may leave unused information from the many basic classes on a blow-up.  On
\[
M=X\#k\,\overline{\mathbb{CP}}^{\,2},
\]
one has monopole classes of the form
\[
a_\sigma=K_X+\sum_{i=1}^k\sigma_i E_i,\qquad \sigma_i\in\{\pm1\}.
\]
For each such class, LeBrun-type estimates give inequalities of the schematic form
\[
\int_M (s-\sqrt6|W^+|)^2\,dV
\ge
72\pi^2 (a_\sigma^+)^2.
\]
Instead of choosing one class, optimize over the whole sign cube.  Averaging over signs gives
\[
\frac1{2^k}\sum_\sigma (a_\sigma^+)^2
=
(K_X^+)^2+\sum_{i=1}^k(E_i^+)^2,
\]
so
\[
\max_\sigma (a_\sigma^+)^2
\ge
(K_X^+)^2+\sum_i(E_i^+)^2.
\]
The unknown is how small the projections \(E_i^+\) can be under a metric satisfying \(\Ric\approx -g\).  Without Ricci pinching, the Hodge \(+\)-plane can rotate so that many exceptional classes are nearly anti-self-dual.  A new theorem could show that pointwise Ricci pinching restricts this rotation enough to force a stronger curvature inequality.

The resulting algebraic-analytic program is:

\[
\begin{aligned}
\text{minimize } &\delta\\
\text{subject to }&
\Ric\text{-pinching Chern--Weil equations},\\
&\text{LeBrun inequalities for all }a_\sigma,\\
&\text{intersection form relations for }K_X,E_i .
\end{aligned}
\]
If the optimized lower estimate stays comparable to a positive constant when \(k>2A/3\), LeBrun manifolds cannot realize the minus-sign counterexample mechanism.  If the optimum remains \(A^{-1/2}\), the known integral inequalities are essentially sharp for this purpose, and the plug/corrugation mechanisms remain compatible with all present four-dimensional topology.

This route is attractive because it attacks exactly the place where the current estimate weakens: \(k-2A/3=O(1)\) while \(A\to\infty\).  It also produces concrete figures: the lower envelope of allowed \(\delta\) versus \(k/A\), first from the classical single-class estimate and then from the full monopole cube.

## 5. Bubble arithmetic from pure Ricci pinching

Suppose a sequence with
\[
\|\Ric+g\|_{\op}\to 0
\]
has Weyl curvature concentrating.  At a point where \(|\Rm|=Q\to\infty\), rescale by \(Q\).  The rescaled metrics satisfy
\[
|\Ric_{\mathrm{rescaled}}|\to 0.
\]
Thus any noncollapsed high-curvature limit is Ricci-flat.  In four dimensions such bubbles have quantized Chern–Weil and APS contributions determined by the link at infinity:
\[
\chi_{\mathrm{loc}},\qquad \tau_{\mathrm{loc}},
\]
with model families including Kronheimer ALE spaces and other Ricci-flat gravitational instantons.

This gives a possible existence-side obstruction to certain counterexample constructions: if the topology of \(X\#k\overline{\mathbb{CP}}^{\,2}\) had to be assembled from allowed Ricci-flat bubble atoms, then \(-1\)-sphere blow-ups might be arithmetically incompatible with the ALE atom list, which naturally contains ADE \(-2\)-configurations in the hyperkähler case.

This does not touch finite-volume Ric\(<0\) bolt plugs, because those carry topology at curvature scale \(O(1)\), not by Ricci-flat blow-up bubbles.  That distinction is valuable: any proposed LeBrun construction must choose between

\[
\text{large-volume Ric<0 bolt cells}
\quad\text{or}\quad
\text{high-curvature Ricci-flat bubble atoms}.
\]

The first route is governed by the finite-radius edge matching and volume ledger above.  The second route is governed by ALE/ALF topology, Chern–Weil quantization, and bubble-tree analysis.  These are genuinely different mechanisms and should lead to different observable geometry.

## 6. A pure Ricci-pinch flow principle

A possible existence mechanism is a flow that sees only the small traceless Ricci tensor and treats Weyl as a passive coefficient.  Under normalized Ricci flow near an Einstein metric with \(\Ric=-g\), the traceless Ricci tensor \(E\) evolves schematically as
\[
(\partial_t-\Delta)E
=
2\,W*E+\text{quadratic terms in }E+\text{scalar terms}.
\]
The important cancellation is
\[
W*g=0.
\]
So Weyl does not directly source \(E\); it only couples through the already small tensor \(E\).  Standard estimates lose control through \(|W||E|\), but a stronger spectral-width estimate might avoid any separate \(|W|\) input.

The ideal inequality would be something like
\[
(\partial_t-\Delta)\operatorname{osc}(\Ric^\#)
\le
-c\,\operatorname{osc}(\Ric^\#)
+
C\,\operatorname{osc}(\Ric^\#)^2,
\]
where
\[
\operatorname{osc}(\Ric^\#)
=
\lambda_{\max}(\Ric^\#)-\lambda_{\min}(\Ric^\#).
\]
If such an inequality were true after a DeTurck normalization, then initial pinching
\[
-1-\varepsilon<\lambda_i(\Ric^\#)<-1+\varepsilon
\]
would improve, and the flow could converge to an Einstein metric without sectional curvature, diameter, or derivative hypotheses.

The decisive local calculation is purely algebraic: diagonalize \(E\) at a point and write \(W^\pm\) as symmetric tracefree endomorphisms of \(\Lambda^\pm\).  Compute the Weyl contribution to the evolution of
\[
\lambda_{\max}(E)-\lambda_{\min}(E).
\]
If the worst Weyl terms cancel in this spectral diameter, the flow route gains a real chance.  If a four-frame algebra example produces growth proportional to \(|W|\operatorname{osc}(E)\), then a modified flow is needed.

A natural modification is the gradient flow of
\[
\mathcal R(g)
=
\int_M |\Ric+g|^2\,dV
\]
with volume normalization and DeTurck gauge.  Its leading part is fourth order and parabolic modulo diffeomorphisms.  The hope is that large Weyl becomes smoothing data rather than an uncontrolled zero-order coefficient.  A theorem of this form would say:

If \(\|\Ric+g\|_{\op}<\varepsilon_n\), then the \(\mathcal R\)-flow exists long enough to reach a zero of \(\mathcal R\), hence an Einstein metric, with constants depending only on dimension.

The hard part is excluding loss of compactness through Weyl concentration or collapse.  In dimension four, that hard part could be tied to the bubble arithmetic above; in higher dimensions it would need a substitute for Chern–Weil quantization.

## 7. Yamabe–LeBrun near-equality rigidity

For LeBrun manifolds near \(k=2A/3\), any hypothetical Ricci-pinched metric nearly saturates several inequalities simultaneously:

\[
\int s^2\,dV\ge 32\pi^2 A,
\]
\[
2\chi+3\tau
=
\frac1{4\pi^2}\int
\left(
2|W^+|^2+\frac{s^2}{24}-\frac{|E|^2}{2}
\right)dV,
\]
and \(|E|\le O(\delta)\), \(s=-4+O(\delta)\).

Equality in the Yamabe–LeBrun inequalities is highly rigid and is tied to Kähler–Einstein geometry on the minimal model.  A quantitative rigidity theorem could have the shape:

If
\[
M=X\#k\overline{\mathbb{CP}}^{\,2},\qquad k>2A/3,
\]
and \(g\) satisfies \(\|\Ric+g\|_{\op}<\varepsilon\), then \(\varepsilon\ge \varepsilon_0\), where \(\varepsilon_0\) is independent of \(A\).

Such a theorem would need to use more than the scalar \(L^2\) inequality, because the existing estimate permits \(\varepsilon\sim A^{-1/2}\).  The extra input could be the full monopole cube, rigidity of equality in the Yamabe invariant, or a Weitzenböck analysis showing that exceptional classes cannot all hide in the anti-self-dual sector while Ricci remains almost isotropic.

The observable signature of this mechanism would be forced concentration of monopole curvature or harmonic representatives near exceptional classes, producing a definite amount of \(E\) somewhere.  That would be a pointwise Ricci obstruction, not merely an integral scalar obstruction.

## 8. The sharp comparison

The two most decisive scientific possibilities are mirror images.

One side is constructive:

\[
\text{finite-volume Ric<0 }\overline{\mathbb{CP}}^2\text{ plug}
+
\text{large KE general type base}
+
k=\frac23A+O(\varepsilon^2A)
\]
would produce LeBrun manifolds with \(\delta_-\to0\) and no Einstein metric.

The other side is structural:

\[
\text{full SW monopole cube}
+
\text{Yamabe equality rigidity}
+
\text{Ricci-pinched bubble arithmetic}
\]
could turn the present \(A^{-1/2}\) lower estimate into a uniform positive gap for LeBrun-type candidates.

The plug route asks for explicit Ric\(<0\) cells with nearly hyperbolic finite-radius edge data and correct volume.  The structural route asks for a new inequality using all basic classes or all possible curvature bubbles, not only the classical scalar estimate.  Either one would materially change the understanding of Yau’s problem: the first would make the minus-sign branch collapse in dimension four; the second would show that pure Ricci pinching secretly contains much more four-dimensional topology than current estimates reveal.