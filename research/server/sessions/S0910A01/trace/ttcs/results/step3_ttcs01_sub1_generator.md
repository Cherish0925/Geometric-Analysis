# TTCS Independent Branch Record

```json
{
  "step_id": 3,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step3_mixed_bound_analysis.md",
    "Sessions/S0910A01/workspace/notes/step2_mechanisms_analysis.md",
    "Skills/qiushi-yau26/references/research/20260910.tex"
  ]
}
```

## Task

Consider the boundary behavior at k/A = 1/3 for Yau Problem 26 (negative branch). At this ratio, the mixed SW bound δ ≥ 0 becomes degenerate. The question is whether there exists a sequence of no-Einstein manifolds M_j = X_j#k_j CP̄² with k_j/A_j → 1/3⁺ carrying metrics with δ_-(g_j) → 0, or whether additional obstructions create a uniform gap. Key considerations: (1) Below k/A = 1/3, Aubin-Yau gives negative Kähler-Einstein metrics on X, and blow-ups may carry KE metrics for small k; (2) At k/A ≈ 1/3, the energy budget forces near-ASD (|W₊|² → 0); (3) The blow-up points create topological changes that must be accommodated geometrically; (4) Stability and deformation theory of KE metrics under blow-up; (5) Whether the 'broken' KE metric just above k/A = 1/3 might still have small δ; (6) Connections to Tian's alpha-invariant, K-stability, and the Yau-Tian-Donaldson conjecture for negative KE. Generate concrete mathematical mechanisms that could determine whether the transition at k/A = 1/3 is continuous or discontinuous in the Ricci-pinching sense.

## Output

### Notation and the first quantitative picture

Let  
\[
A=c_1^2(X),\qquad p=\frac{k}{A}=\frac13+\alpha,\qquad 
M=X\#k\,\overline{\mathbb{CP}}^{\,2},
\]
and for a metric with \(\Ric\approx -g\) set
\[
S=\frac1{4\pi^2A}\int_M\frac{s^2}{24},\quad
W=\frac1{4\pi^2A}\int_M2|W_+|^2,\quad
T=\frac1{4\pi^2A}\int_M\frac{|E|^2}{2},\quad
v=\frac{\Vol(M,g)}{4\pi^2A}.
\]
Chern–Gauss–Bonnet and the mixed SW estimate give
\[
S+W-T=1-p=\frac23-\alpha,\qquad S+W\ge \frac23,
\]
hence
\[
T\ge \alpha .
\]
If \(\delta=\delta_-(g)\), then
\[
T\le 2\delta^2 v,\qquad
\frac23(1-\delta)^2v\le S\le \frac23(1+\delta)^2v.
\]
Thus any sequence with \(\delta\to0\) must satisfy
\[
\alpha=O(\delta^2),
\]
not merely \(\alpha\to0\). More sharply, the known mixed estimate gives
\[
\frac{\delta}{1-\delta}\ge \sqrt{\frac{\alpha}{2}}.
\]

The near-ASD statement is a second saturation. Indeed
\[
W=\Big(T-\alpha\Big)+\Big(\frac23-S\Big),
\]
and since \(S=\frac23v+O(\delta)v\), one gets
\[
W=\Big(T-\alpha\Big)+\frac23(1-v)+O(\delta)v.
\]
So \(W\to0\) follows if both the traceless-Ricci energy nearly equals the SW minimum \(T\sim\alpha\) and the volume approaches the Chern–Weil ceiling \(v\to1\). If \(W\) remains of order \(A\), then the metric lives in a different regime: either volume is lower, or \(|E|^2\) has extra integrated mass beyond the SW minimum. A useful figure would plot \((\alpha/\delta^2,\ v,\ W)\); the transition is not a single number but a small cone of possible energy distributions.

---

## 1. Ordinary Kähler blow-up cannot be the smooth \(\Ric\approx -g\) path

Aubin–Yau applies directly to the minimal surface \(X\) when \(K_X\) is ample. It does not pass through the ordinary complex blow-up \(\widetilde X\to X\) in a smooth Kähler way.

Let \(E_i\subset\widetilde X\) be an exceptional curve. Then
\[
K_{\widetilde X}\cdot E_i=-1,\qquad c_1(T\widetilde X)\cdot E_i=1.
\]
For any Kähler metric \(\omega\) on this blown-up complex surface, the Ricci form \(\rho\) satisfies
\[
[\rho]=2\pi c_1(T\widetilde X),
\]
so
\[
\int_{E_i}\rho=2\pi.
\]
But if the associated Riemannian metric obeys
\[
\|\Ric_g+g\|_{\op}<1,
\]
then on the holomorphic tangent plane of \(E_i\),
\[
\rho(u,Ju)=\Ric_g(u,u)\le -(1-\delta)g(u,u),
\]
and therefore
\[
2\pi=\int_{E_i}\rho\le -(1-\delta)\Area_\omega(E_i)<0,
\]
a contradiction.

So a “broken KE metric” just past \(p=1/3\) cannot remain Kähler for the ordinary blow-up complex structure. If such metrics exist, they must either leave Kähler geometry, use another complex structure on the same smooth 4-manifold, or pass through singular/log geometry before being smoothed in a genuinely Riemannian way.

This also clarifies the role of Tian’s \(\alpha\)-invariant and K-stability. For \(K_X\) ample, the \(\lambda<0\) KE existence theorem is governed by Aubin–Yau, with the YTD picture essentially automatic for canonically polarized manifolds. On the ordinary blow-up, the exceptional curve already gives a direct cohomological sign obstruction, stronger than a subtle K-stability test. The interesting K-stability/log direction is instead: contract exceptional curves, study singular pairs or canonical models, then ask whether smoothing the resulting divisorial Ricci currents can keep \(\|\Ric+g\|_{\op}\) small everywhere.

---

## 2. Quantitative near-equality in the LeBrun estimate could force an almost-Kähler structure

For a monopole class \(a\), define the mixed SW deficit
\[
D_a(g)=
\frac1{4\pi^2}\int_M\left(\frac{s^2}{24}+2|W_+|^2\right)d\mu
-\frac23(a^+)^2.
\]
A sequence with \(p\to1/3^+\), \(\delta\to0\), \(v\to1\), \(T\sim\alpha\), and \(W\to0\) should have
\[
D_{a_j}(g_j)=o(A_j)
\]
for a maximizing basic class \(a_j\).

The proof of LeBrun’s estimate runs through Seiberg–Witten equations and a Weitzenböck identity. Thus a strong quantitative stability theorem for this inequality would plausibly produce a self-dual 2-form \(\omega_j\) coming from the spinor, with schematic controls such as
\[
\frac{\|\nabla\omega_j\|_{L^2}^2}{A_j}\to0,\qquad
\frac{\||\omega_j|-\text{const}\|_{L^2}^2}{A_j}\to0,
\]
plus an alignment relation between \(\omega_j\) and the lowest eigendirection of \(W_+\).

If such a theorem is available, the Riemannian problem is pulled back toward almost-Kähler geometry. Then the exceptional curves may re-enter through adjunction/Taubes-type mechanisms: exceptional classes tend to have \(J\)-holomorphic representatives for compatible almost-complex structures. The Kähler sign computation above could survive in softened form, with the error controlled by \(\|\nabla\omega_j\|\) and the Nijenhuis tensor.

The decisive observable would be:

\[
\int_{E_i}\rho^\omega
\quad\text{versus}\quad
-\int_{E_i}\omega ,
\]
where \(\rho^\omega\) is the Hermitian Ricci form of the almost-Kähler structure. If near equality forces this comparison uniformly over many exceptional classes, then a Ricci-pinching gap emerges. If instead all exceptional \(\omega\)-areas collapse and \(\nabla\omega\) concentrates, the geometry has moved into a cap/collapse regime.

---

## 3. Use all \(2^k\) monopole classes, not just the sign-optimized one

For
\[
a_\varepsilon=c_1(X)+\sum_{i=1}^k \varepsilon_i E_i,\qquad \varepsilon_i=\pm1,
\]
the mixed SW estimate applies to every \(a_\varepsilon\). Averaging over signs gives the exact identity
\[
2^{-k}\sum_{\varepsilon\in\{\pm1\}^k}(a_\varepsilon^+)^2
=
(c_1(X)^+)^2+\sum_{i=1}^k(E_i^+)^2.
\]
Since
\[
I_+(g):=\frac1{4\pi^2}\int\left(\frac{s^2}{24}+2|W_+|^2\right)
\ge \frac23\max_\varepsilon(a_\varepsilon^+)^2,
\]
near saturation at \(I_+\sim 2A/3\) forces
\[
(c_1(X)^+)^2=A+o(A),\qquad
\sum_{i=1}^k(E_i^+)^2=o(A).
\]
Thus the period point of the metric must make almost every exceptional class nearly anti-self-dual.

This is a strong geometric signature. The exceptional lattice is large, \(k\sim A/3\), so a continuous transition requires a metric whose Hodge decomposition pushes many square \(-1\) classes almost entirely into \(\Lambda^-\). That is not topologically impossible, but it is highly structured.

The next analytic object is the Weitzenböck formula for harmonic anti-self-dual 2-forms:
\[
0=\int_M\left(|\nabla\eta|^2+
\left\langle\left(\frac{s}{3}I-2W_-\right)\eta,\eta\right\rangle\right)d\mu
\]
up to the chosen sign convention. A large family of such harmonic forms needs a large supply of favorable \(W_-\)-directions. Thus the transition can be read as a spectral-density question for the curvature operator on \(\Lambda^-\). If Ricci pinching plus the Chern–Weil budgets allow this density, continuity remains plausible; if not, the monopole polytope produces the missing gap.

---

## 4. The essential local model is a curved \(\overline{\mathbb{CP}}^{\,2}\)-cap, not an ALE bubble

The usual smooth blow-up intuition inserts a small Ricci-flat model such as Burns or Eguchi–Hanson. That cannot give \(C^0\) Ricci pinching to \(-g\): on a Ricci-flat core,
\[
\|\Ric+g\|_{\op}=1
\]
after the target normalization, regardless of how tiny the core volume is. Shrinking the bubble helps integral norms, but not the operator norm in \(\delta_-\).

So a continuous transition needs a different local object: a metric on
\[
P=\overline{\mathbb{CP}}^{\,2}\setminus B^4
\]
whose Ricci tensor is everywhere close to \(-g\), and whose outer hypersurface Cauchy data can be matched to the ambient geometry.

This can be turned into a precise fill-in invariant:
\[
\Delta(P;\mathcal C)
=
\inf_g\ \sup_P\|\Ric_g+g\|_{\op},
\]
where \(\mathcal C\) prescribes the outer hypersurface metric and second fundamental form up to a chosen tolerance. If one can find \(\mathcal C_j\) compatible with the ambient near-KE geometry and \(\Delta(P;\mathcal C_j)\to0\), the local topological surgery has a route to Ricci pinching. If \(\Delta(P;\mathcal C)\ge c>0\) for all compatible outer data, each exceptional summand carries a local Ricci cost.

A concrete computable version uses the \(U(2)\)-invariant Bianchi IX ansatz
\[
g=dt^2+a(t)^2(\sigma_1^2+\sigma_2^2)+b(t)^2\sigma_3^2,
\]
with bolt smoothness conditions at the collapsed circle and prescribed outer data. The Ricci eigenvalues become an explicit ODE system. The finite-dimensional problem is:
\[
\inf_{a,b}\ \sup_t\max_i|r_i(t)+1|.
\]
Even a strong result only inside this ansatz would distinguish whether the needed cap resembles a smooth curved handle, a long cusp-like object, or no symmetric object at all.

The cap also has Chern–Weil transgression constraints:
\[
2\chi(P)\pm3\tau(P)
=
\frac1{4\pi^2}\int_P
\left(2|W^\pm|^2+\frac{s^2}{24}-\frac{|E|^2}{2}\right)
+\operatorname{CS}_\pm(\Sigma),
\]
where \(\Sigma\) is the outer hypersurface. These formulas determine how much \(W_-\)-energy, scalar volume, and hypersurface Chern–Simons contribution a single exceptional cap must carry.

---

## 5. Orbifold/ALE gluing gives a sharp obstruction map

Another natural picture is a singular Einstein or ASD-Einstein object at \(p=1/3\), with smoothings corresponding to exceptional curves. Biquard–Ozuch–Yao-type theory suggests the following local analytic shape.

Let \(g_t\) be an approximate Einstein smoothing and write
\[
F(g_t)=\Ric_{g_t}+g_t=r_t.
\]
After gauge fixing,
\[
F(g_t+h)=r_t+L_t h+Q_t(h).
\]
If \(L_t\) has small eigenvalues or cokernel, the exact equation is controlled by a finite-dimensional obstruction map
\[
\Pi_t r_t+\Pi_t Q_t(h)=0.
\]
The sign and size of \(\Pi_t r_t\) should encode the excess
\[
k-\frac{A}{3}.
\]

Two asymptotic laws would lead to very different transition behavior:

\[
|\Pi_t r_t|\sim C\left(\frac{k}{A}-\frac13\right)
\]
would match the SW lower bound and allow \(\delta\) to scale like \(\sqrt{\alpha}\). But
\[
|\Pi_t r_t|\ge c
\]
for an excess exceptional component would force a uniform Ricci-pinching gap.

This is where higher-order obstruction formulas, Pohozaev identities, ALE mass terms, and curvature values at orbifold points become decisive. The calculation to seek is not just “can the singularity be smoothed to an exact Einstein metric?” but rather: how small can the unprojected Ricci residual be when the projected obstruction is topologically nonzero?

The integer rounding regime is especially revealing. Taking
\[
k=\left\lceil\frac{A}{3}\right\rceil
\]
gives
\[
\alpha=O(A^{-1}),
\]
so the mixed SW lower bound permits
\[
\delta\gtrsim A^{-1/2}.
\]
If the obstruction is averaged over the whole manifold, this scale is natural. If one extra exceptional cap has a local Ricci cost independent of \(A\), then no averaging can hide it in a \(C^0\) norm.

---

## 6. Volume accounting separates small blow-ups from genuine Ricci-pinched topology change

For the minimal \(X\) with its \(\lambda<0\) KE metric normalized by \(\Ric=-g\), the scalar-only SW equality gives
\[
\Vol(X)=2\pi^2 A.
\]
In contrast, an ASD-like Ricci-pinched metric near \(p=1/3\) with \(W\to0\) has
\[
S\sim \frac23,\qquad v\sim1,
\]
hence
\[
\Vol(M)\sim 4\pi^2A.
\]
The volume has doubled. Since
\[
k\sim\frac{A}{3},
\]
the added volume per exceptional summand is roughly
\[
\frac{2\pi^2A}{A/3}=6\pi^2.
\]
Thus a near-ASD transition cannot be produced by tiny bubbles attached to a fixed KE background. Each exceptional contribution must occupy order-one volume at the \(\Ric=-g\) scale, unless the metric lies in the alternative regime with extensive \(W_+\)-energy.

This gives a clean comparison:

* **Small Kähler blow-up picture:** local volume tends to zero; Ricci-flat bubble gives \(C^0\) Ricci error near \(1\).
* **Curved cap picture:** each exceptional summand carries order-one volume and stores topology mostly in \(W_-\).
* **Extensive \(W_+\) picture:** volume can be lower, but near-ASD no longer describes the transition.

A numerical or analytic construction should therefore report not only \(\delta\), but also \(v\), \(W/A\), \(W_-/A\), and the volume distribution per exceptional class.

---

## 7. Log/K-stability can model the singular route, but smooth pinching asks a sharper question

For canonically polarized smooth varieties, the \(\lambda<0\) KE existence theorem is not controlled by the delicate Fano-type instability phenomena. The ordinary blow-up leaves the ample-canonical world because \(K\cdot E_i=-1\).

However, log geometry may still encode the transition. Contracting exceptional curves produces singular canonical models; log KE equations include current terms along divisors or exceptional loci. The formal equation has the shape
\[
\rho=-\omega+\sum_j c_j[D_j]
\]
in currents. The exceptional topology is then balanced by singular Ricci mass.

The smooth Ricci-pinching question becomes: can those current terms be smoothed so that the pointwise operator norm of \(\Ric+g\) tends to zero? If the topological \(2\pi\) integral over each exceptional class must remain concentrated in a small tube, then the operator norm should stay large. If the smoothing spreads that mass through a long cusp-like region while preserving \(\Ric\approx -g\), continuity becomes plausible.

Relevant source families to search here are:

* Tian \(\alpha\)-invariant estimates for continuity methods;
* log canonical thresholds of blow-ups of canonically polarized surfaces;
* slope/K-stability tests involving exceptional divisors;
* Donaldson-type lower bounds for curvature functionals from test configurations.

The transfer to the present problem is partial: these tools live in Kähler or log-Kähler geometry, while the final Riemannian metric need not be Kähler. Their strongest role may be to show that any continuous transition must abandon the ordinary complex blow-up picture.

---

## 8. Pure Riemannian flexibility: Weyl packets with Ricci fixed

Ricci pinching leaves the Weyl tensor largely free. In four dimensions the exceptional summands can be stored mainly in \(W_-\)-energy while \(W_+\) remains small. This suggests a possible “Weyl packet” mechanism:

Construct local regions with
\[
\Ric=-g+O(\varepsilon),
\]
large prescribed \(W_-\)-energy, small \(W_+\)-energy, and Chern–Weil densities matching the topological contribution of \(\overline{\mathbb{CP}}^{\,2}\). If such packets can be glued with \(\varepsilon\to0\), then the transition could be continuous even though no exact Einstein metric exists beyond \(p=1/3\).

This is the two-sided analogue of Lohkamp-type flexibility, but much sharper because the target is a narrow Ricci interval rather than a one-sided inequality. The local Einstein equation itself has many degrees of freedom in dimension four; the hard part is matching packets globally while controlling hypersurface Cauchy data and Chern–Simons terms.

A decisive computation would build analytic local models with Ricci tensor exactly or nearly \(-g\), then calculate their \((\chi,\tau)\)-density contributions:
\[
\frac1{4\pi^2}\left(2|W^\pm|^2+\frac{s^2}{24}\right)d\mu.
\]
If such packets exist with the correct sign distribution, they provide a concrete route to \(\delta\to0\). If every packet carrying a \(-1\) intersection form contribution forces \(W_+\) or \(|\Ric+g|\) of order one, a gap mechanism appears.

---

## 9. Thin-part and diameter escape are not secondary details

Min-Oo-type theorems require additional geometric control such as a diameter–curvature product. A sequence with \(\delta\to0\) and no exact Einstein metric can escape through:

\[
\diam^2\max|\Rm|\to\infty,
\]
by Weyl concentration, long regions, or both.

Near \(p=1/3\), a plausible continuous construction would place exceptional topology into long cusp-like or tube-like regions where Ricci remains close to \(-g\). This aligns with Dehn filling and orbifold smoothing analogies: approximate metrics can have very small residual, while the exact correction is prevented by a finite-dimensional obstruction detected by SW theory.

The observable signature is:

\[
\diam(M_j,g_j)\to\infty
\quad\text{or}\quad
\max|W_j|\to\infty,
\]
together with concentration of \(W_-\)-energy near exceptional regions and small \(W_+\)-energy in the LeBrun orientation. If instead one proves that \(\Ric\approx -g\), \(p\to1/3\), and the Chern–Weil budgets force controlled diameter and controlled Weyl concentration, then existing stability machinery becomes much closer to applicable.

---

## Two competing mathematical pictures

### Gap picture

Near saturation of the mixed SW inequality forces an almost-Kähler structure. Exceptional classes then behave like holomorphic or almost-holomorphic \((-1)\)-curves. The Ricci form sign calculation survives quantitatively, giving a uniform lower bound for \(\delta_-\). The full monopole-class polytope strengthens this by forcing many exceptional classes to be almost anti-self-dual at once.

Core theorem shape:
\[
D_a(g)\ll A,\quad \|\Ric+g\|_{\op}\ll1
\quad\Longrightarrow\quad
\text{almost-Kähler control strong enough to see exceptional curves}.
\]

### Continuous picture

The metrics leave Kähler geometry entirely. Each exceptional summand is represented by a curved cap, thin tube, orbifold smoothing, or Weyl packet with Ricci close to \(-g\). The obstruction to exact Einstein metrics is finite-dimensional and scales like \(k/A-1/3\), so for \(k=\lceil A/3\rceil\) the allowed defect is of order \(A^{-1/2}\), matching the mixed SW lower bound.

Core construction shape:
\[
\overline{\mathbb{CP}}^{\,2}\setminus B^4
\ \text{admits caps with}\ 
\sup|\Ric+g|\to0,
\]
with Chern–Weil transgression carrying the exceptional topology mostly through \(W_-\).

The transition at \(p=1/3\) is therefore governed by one central scientific question:

\[
\text{Is the exceptional }(-1)\text{ topology forced to appear through almost-Kähler curves,}
\]
or can it be hidden inside purely Riemannian Weyl/cap/thin-part geometry while Ricci remains uniformly close to \(-g\)?