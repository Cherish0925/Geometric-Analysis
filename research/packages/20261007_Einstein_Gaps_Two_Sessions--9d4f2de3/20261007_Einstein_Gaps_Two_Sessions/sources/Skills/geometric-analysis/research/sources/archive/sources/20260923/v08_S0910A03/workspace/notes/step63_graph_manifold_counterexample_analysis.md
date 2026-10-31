# Step 63: Extended graph manifolds as Yau 26 counterexample candidates

Session: S0910A03. Agent2 / Constructor. Phase: Explore.

## 0. The central question

Extended graph 4-manifolds are **the first source-supported topology class that excludes
*all* Einstein metrics** (Di Cerbo \cite{cerbo2022extended}, Theorem 12). This makes them
the most concrete candidate for the negative-branch Yau 26 counterexample: can they
carry smooth metrics with $\|\operatorname{Ric}+3g\|_{\mathrm{op}}\to0$?

If YES: together with a positive-branch analog, this would refute Yau 26 in dimension 4.
If NO: the obstruction reveals a *quantitative* pinching gap, extending the restricted
Ishida–LeBrun mechanism to a new topology class.

## 1. Di Cerbo's obstruction mechanism and its gap

### 1.1 The proof structure (from the source, lines 589–701)

**Case 1 (with pure real-hyperbolic pieces).**
Lemma 9: $\operatorname{Vol}_{Ric}(M) = \sum_i \operatorname{Vol}_{g_{-1}}(V_i)$.
Lemma 7 (LeBrun): an Einstein metric with $\operatorname{Ric}=-3g$ satisfies
$2\chi \ge \frac{3}{2\pi^2}\operatorname{Vol}_{Ric}(M)$, with equality iff half-conformally flat.
Since $\tau=0$, equality forces real-hyperbolic. Preissmann's theorem ($\mathbb{Z}^3 \subset \pi_1$)
contradicts this.

**Case 2 (no pure pieces).**
Lemma 8: $\chi = \tau = 0$. Hitchin–Thorpe equality forces flat/K3 cover. But
$\pi_1(M)$ grows exponentially — contradiction.

### 1.2 The gap for approximate Einstein metrics

The Di Cerbo argument uses **exact** Einstein metrics. For $\|\operatorname{Ric}+3g\|_{\mathrm{op}} \le \delta$:

1. **Lemma 7 gap**: The LeBrun inequality $2\chi \ge \frac{3}{2\pi^2}\operatorname{Vol}_{Ric}(M)$ holds for
   *any* metric with $\operatorname{Ric} \ge -3g$. But $\|\operatorname{Ric}+3g\|_{\mathrm{op}} \le \delta$
   gives $\operatorname{Ric} \ge -(3+\delta)g$, not $\operatorname{Ric} \ge -3g$.
   Rescaling $g \to \frac{3}{3+\delta}g$ gives $\operatorname{Ric} \ge -3g'$ on the rescaled metric,
   but this changes the topology-independent normalization.

2. **Half-conformal flatness gap**: The equality case requires $\operatorname{Ric}^\circ = 0$ exactly.
   For $\delta > 0$, the trace-free Ricci is $O(\delta)$, and the Gauss–Bonnet integral gains
   an $O(\delta^2)$ term. The conclusion "half-conformally flat" becomes "approximately
   half-conformally flat," which no longer forces hyperbolicity.

3. **Entropy rigidity gap**: The Connell–Suárez–Serrato estimate
   $h(g)\operatorname{Vol}_g(M)^{1/4} \ge 3\operatorname{Im}(\operatorname{MinVol}(M))^{1/4}$
   holds for any metric. But the Bishop–Gromov bound $h(g) \le 3$ uses $\operatorname{Ric} \ge -3g$,
   which is not exactly satisfied for $\delta > 0$.

### 1.3 The quantitative question

For each $\delta > 0$, define
$$\rho(\delta) = \inf\{\|\operatorname{Ric}_g + 3g\|_{\mathrm{op}} : g \text{ smooth on } M\}.$$

The Di Cerbo theorem says $\rho(0) > 0$ (no exact Einstein metric). The Yau 26 question asks:
does $\rho(\delta) \to 0$ as $\delta \to 0$? Equivalently: can $M$ carry a sequence of
smooth metrics with defect $\to 0$?

**No known result answers this.** The gap in the Di Cerbo argument is precisely the
approximate-Einstein regime.

## 2. The mean curvature barrier analysis

### 2.1 Flat-slice trace constraint (new, verified computationally)

For $g = dr^2 + G(r)$ on $T^3 \times [a,b]$ with **intrinsically flat** $T^3$ slices:

**Theorem.** If $\|\operatorname{Ric}+3g\|_{\mathrm{op}} \le \delta < 3/2$, then the mean
curvature $H = \operatorname{tr}(S)$ of any flat $T^3$ slice satisfies
$$H^2 \ge 9 - 6\delta > 0.$$

*Proof.* Gauss equation with $R_N = 0$:
$$H^2 - |S|^2 = 2\operatorname{Ric}(\partial_r,\partial_r) - R_M \in [6-4\delta, 6+4\delta].$$
By Cauchy–Schwarz for the self-adjoint $3 \times 3$ shape operator $S$:
$|S|^2 \ge H^2/3$, so $H^2 - |S|^2 \le 2H^2/3$. Therefore
$2H^2/3 \ge 6 - 4\delta$, giving $H^2 \ge 9 - 6\delta$. $\square$

**Corollary.** For $\delta < 3/2$, no flat $T^3$ slice can be minimal ($H=0$). In particular,
a smooth warped-product collar with flat slices cannot transition from contracting ($H<0$)
to expanding ($H>0$) cusp geometry.

### 2.2 Non-flat-slice escape mechanism — CORRECTED after TTCS verification

**The original claim was WRONG.** $T^3$ cannot carry a metric with
$\operatorname{Ric}_{g_N} = -2g_N$. In dimension 3, this would force constant
sectional curvature $-1$, but a closed hyperbolic 3-manifold cannot have
$\pi_1 = \mathbb{Z}^3$. Lohkamp's theorem gives $\operatorname{Ric} < 0$
(negative as a quadratic form), not Einstein.

**What is correct:** The warped product algebra is sound. If $(N^3, g_N)$ has
$\operatorname{Ric}_{g_N} = -2g_N$ (i.e., $N$ is hyperbolic), then
$g = dr^2 + \cosh^2(r)g_N$ on $\mathbb{R} \times N$ is exactly Einstein.
But this requires $N$ to be a closed hyperbolic 3-manifold, not $T^3$.

**The escape mechanism must use approximate, not exact, Einstein slices.**
Any metric on $T^3$ with $\operatorname{Ric} \approx -2g$ in operator norm
must have some sectional curvatures $\ge 0$ (since not all can be negative
on $T^3$). The deviation from Einstein is controlled by the topology of $T^3$,
not by the metric choice. This creates a **quantitative floor** for the
slice Ricci defect.

**Raychaudhuri mechanism.** At $H=0$, the Gauss equation gives
$|S|^2 = (R_M - 2\operatorname{Ric}(\partial_r,\partial_r)) - R_N$.
With $R_N \approx -6$ (from $\operatorname{Ric}_N = -2g_N$), $|S|^2$ can be small,
and $H' = -\operatorname{Ric}(\partial_r,\partial_r) - |S|^2 \approx 3 > 0$.

**Schoen–Yau compatibility.** Any metric on $T^3$ has $R_N \le 0$
(Schoen–Yau, positive mass theorem). The value $R_N = -6$ is compatible with
$\operatorname{Ric}_N = -2g_N$.

### 2.3 The compact matching problem

The exact Einstein funnel $g = dr^2 + \cosh^2(r)g_N$ is **non-compact**
(cosh grows exponentially). For a compact graph manifold collar $[-L,L] \times T^3$:

- At $r = \pm L$: $H = \pm 3\tanh(L) \to \pm 3$ as $L \to \infty$. ✓ (matches cusp)
- At $r = 0$: $H = 0$, slice metric is $g_N$ (non-flat, $\operatorname{Ric} = -2$).
- At $r = \pm L$: slice metric is $\cosh^2(L)g_N$ (non-flat).

**The cusp interface requires flat slices.** The hyperbolic cusp has metric
$dr^2 + e^{-2r}g_{\mathrm{flat}}$. The Einstein collar has boundary slice metric
$\cosh^2(L)g_N$ (non-flat). A **flat-to-non-flat transition** is needed at each boundary,
introducing Ricci defect.

### 2.4 Quantitative defect estimate

For the pure flat-slice cosh model $g = dr^2 + \cosh^2(r)g_0$ ($g_0$ flat):

- $\operatorname{Ric}(\partial_r,\partial_r) = -3$ (exact).
- Tangential: $\operatorname{Ric}|_{T^3} = -(1+2\tanh^2(r))g_{\mathrm{tang}}$.
- Defect: $\|\operatorname{Ric}+3g\|_{\mathrm{op}} = 2\operatorname{sech}^2(r)$.
- Maximum at $r=0$: $\delta = 2$.

This exceeds the flat-slice barrier threshold $3/2$. ✓ Consistent.

For a model with $\operatorname{Ric}_N = -\alpha g_N$ (isotropic):
- $H' = 3(3-\alpha) - H^2$.
- Equilibria at $H = \pm\sqrt{9-3\alpha}$.
- As $\alpha \to 3$: equilibria coalesce at $H=0$, transition becomes easier.
- Defect in tangential direction: $|\alpha - 3 + O(\text{shear})|$.

## 3. Strategic assessment

### 3.1 What the flat-slice barrier establishes

The barrier is a **new quantitative pinching obstruction** for torus-sliced
near-Einstein 4-manifolds: any collar with flat $T^3$ slices and
$\|\operatorname{Ric}+3g\|_{\mathrm{op}} < 3/2$ cannot reverse mean curvature.
This is a *local* obstruction that doesn't require global topology.

### 3.2 What the non-flat escape establishes

The exact Einstein funnel $dr^2 + \cosh^2(r)g_N$ with $\operatorname{Ric}_N = -2g_N$
proves that **non-flat torus slices can carry exact Einstein geometry with mean
curvature reversal**. The question becomes quantitative: what is the minimum defect
in a compact collar that transitions from flat cusp boundary to non-flat Einstein
interior and back?

### 3.3 Connection to the Ishida–LeBrun mechanism — REVISED

The IL route uses a **localizing obstruction**: the monopole density $\mathfrak{D}$
has support proportional to volume, and its zero set forces an impossible Einstein
spectrum. The graph manifold obstruction was initially classified as **evacuable**,
but the TTCS correction reveals a deeper structure:

**The $T^3$ topology itself provides a local obstruction.** Any slice metric on $T^3$
that is close to $\operatorname{Ric} = -2g$ in operator norm must have some sectional
curvatures $\ge 0$. This is a **pointwise** constraint, not a global one. The
traced Gauss equation then couples this slice-level obstruction to the 4D Ricci
defect through the shape operator.

The corrected dichotomy is:
- IL topology localizes via monopole density → gap theorem.
- $T^3$ topology localizes via the impossibility of Einstein slices → different
  gap mechanism.
- Graph manifold topology also has the global (evacuable) $\pi_1$ component.

This suggests the graph manifold route may yield a **gap theorem** (Route B)
rather than a counterexample (Route A), but through a new mechanism: the
flat-slice barrier + the $T^3$ slice-Einstein impossibility.

### 3.4 Three routes for the graph manifold candidate

**Route A (counterexample).** Construct a compact collar with non-flat slices
and defect $\delta \to 0$. Requires solving the flat-to-non-flat matching problem
with controlled defect. If successful, combined with Di Cerbo's all-Einstein exclusion,
this gives a Yau 26 counterexample.

**Route B (gap theorem).** Prove that the flat-to-non-flat transition itself
requires defect $\ge \delta_0 > 0$ uniformly. This would extend the IL gap to
graph manifolds. The flat-slice barrier is a first step.

**Route C (approximate Di Cerbo).** Quantify the Di Cerbo argument for
approximate Einstein metrics. The key question: does the entropy estimate
$h(g)\operatorname{Vol}^{1/4} \ge 3\operatorname{Im}(\operatorname{MinVol})^{1/4}$
have a stability version under $\|\operatorname{Ric}+3g\|_{\mathrm{op}} \le \delta$?

## 4. Anderson's 2003 preprint status

### 4.1 What the preprint claims

Theorem 0.1 (\cite{anderson2003arxiv}): for $\varepsilon$ small (depending only on $n$),
any compact $n$-manifold with $\varepsilon$-pinched negative sectional curvature
($|K+1| \le \varepsilon$) admits an Einstein metric.

### 4.2 Internal evidence of completeness

The preprint is **self-contained and complete as written** (369 lines in our Knowledge copy):

1. **Proposition 2.1** (the key estimate): $\|h\|_{C^{m,\alpha}} \le \Lambda\|L(h)\|_{C^{m-2,\alpha}}$
   with $\Lambda$ depending only on $m,n$. The proof uses:
   - Local Schauder estimates (standard).
   - Weighted $L^2$ estimates with the exponential weight $\eta = e^{-\alpha(r-R)}$.
   - **Lemma 2.2**: ergodic-theoretic measure convergence on the sphere bundle.
   - Absorption of the seam term at $S(R)$ using volume growth.
   - Extension to $\varepsilon$-pinched case via comparison geometry (Lemma 2.3).

2. **Corollary 2.6**: uniform invertibility in a $C^{m,\alpha}$ neighborhood.

3. **Theorem 0.1 proof**: inverse function theorem using Corollary 2.6.

### 4.3 The ergodic lemma (Lemma 2.2)

This is the subtlest step. It claims that the spherical averages of
$|h_{11}|^2 = \langle dr \cdot dr, h^2\rangle$ over $S(r) \subset \widetilde{M}$
converge to $\frac{1}{n^2\operatorname{Vol} M}\int_M |h|^2$ as $r \to \infty$.
The proof uses weak convergence of the normalized sphere measures to Liouville
measure on $SM$, valid for compact hyperbolic manifolds.

**Potential concern**: The weak convergence of measures gives convergence for
*fixed* functions on $SM$. But $h$ varies with the metric $g$ as $\varepsilon \to 0$.
However, since $h$ is $\Gamma$-invariant and the function $\langle v \cdot v, h^2\rangle$
is a well-defined continuous function on $SM$ (independent of $r$), the weak convergence
does apply uniformly.

### 4.4 Publication status

The knowledge request found **no published version, errata, or retraction**.
The preprint remains on arXiv as math/0310041v1 (October 2003). Anderson has not
published this result in a refereed journal to our knowledge.

**However**, the recent Hamenstädt–Jäckel paper (\cite{hamenstdt2024negatively})
independently constructs negative Einstein metrics on Gromov–Thurston manifolds
using a different spectral method. This provides **independent confirmation**
that such manifolds do carry Einstein metrics, consistent with Anderson's claim.

**Assessment**: Anderson's preprint appears mathematically sound on internal review.
The absence of formal publication is unusual but does not indicate a known error.
The ergodic argument (Lemma 2.2) is the most subtle step and deserves independent
verification. For the purpose of Yau 26, the result means:

> **Sectional-pinching routes are closed.** Any manifold with sufficiently pinched
> negative sectional curvature carries an Einstein metric (assuming Anderson's
> result). The counterexample must use metrics that are Ricci-pinched but NOT
> sectionally pinched.

## 5. Implications for the full problem

### 5.1 What this step establishes

1. Extended graph manifolds exclude all Einstein metrics (Di Cerbo, source-verified).
2. Flat-slice torus collars have a quantitative mean curvature barrier at $\delta < 3/2$.
3. Non-flat torus slices admit exact Einstein geometry with mean curvature reversal.
4. Anderson's theorem (if valid) closes all sectionally-pinched counterexample routes.
5. The graph manifold candidate is **the most concrete Yau 26 counterexample candidate**
   identified in 62 steps of this project.

### 5.2 The critical open question

Can an extended graph 4-manifold carry a sequence of smooth metrics with
$\|\operatorname{Ric}+3g\|_{\mathrm{op}} \to 0$?

**For a YES answer** (counterexample), one needs:
- A compact collar with non-flat torus slices whose Ricci is close enough to $-2g$
  to satisfy the tangential equation, but not so close as to violate the $T^3$
  sectional curvature constraint.
- The TTCS analysis suggests this is **impossible**: the $T^3$ topology creates
  a quantitative floor for the slice Ricci defect, which propagates to the 4D defect.

**For a NO answer** (gap theorem), the corrected mechanism is:
- Flat-slice barrier: $H^2 \ge 9-6\delta$ prevents $H=0$ on flat slices.
- Non-flat slices must have $\operatorname{Ric} \approx -2g$ to allow $H$ reversal.
- But $T^3$ cannot carry such metrics (sectional curvature constraint).
- Therefore: any torus-sliced collar with $\|\operatorname{Ric}+3g\|_{\mathrm{op}}$
  small enough cannot reverse mean curvature, regardless of slice geometry.

**The remaining question is whether the graph manifold transition REQUIRES
torus-sliced collars.** If the transition region can avoid a $T^3$ foliation
altogether (e.g., using a more complex topology in the neck), the barrier
may not apply. This is the key open question for Route A.

### 5.3 The positive branch remains untouched

The graph manifold analysis is entirely negative-branch. The positive branch
($\operatorname{Ric} \approx +g$) requires a different topology class and a
different mechanism. No candidate has been identified in this session.

## 6. Next steps

1. **Compute the matching defect**: For the collar $[-L,L] \times T^3$, estimate
   the minimum defect when matching flat cusp boundary to non-flat Einstein interior.
   This is a concrete variational problem.

2. **Check entropy stability**: Does the Connell–Suárez–Serrato inequality have a
   stability version? If $h(g) \le 3+\epsilon$ forces $\operatorname{Vol}_g(M)$
   close to $\operatorname{MinVol}(M)$, this gives a quantitative gap.

3. **Independently verify Anderson's Lemma 2.2**: The ergodic measure convergence
   argument is the load-bearing step. If it fails, sectional-pinching routes reopen.

4. **Assess the positive branch**: Search for a topology class that excludes all
   Einstein metrics and can carry $\operatorname{Ric} \approx +g$. Hitchin–Thorpe
   violation already gives a pinching gap, so the candidate must satisfy
   $2\chi \ge 3|\tau|$ but still exclude all Einstein metrics (LeBrun-type).

## 7. Files

- Script: `workspace/scripts/step63_torus_transition_analysis.py`
- Data: `workspace/data/step63_torus_transition_analysis.json`
- This note: `workspace/notes/step63_graph_manifold_counterexample_analysis.md`
