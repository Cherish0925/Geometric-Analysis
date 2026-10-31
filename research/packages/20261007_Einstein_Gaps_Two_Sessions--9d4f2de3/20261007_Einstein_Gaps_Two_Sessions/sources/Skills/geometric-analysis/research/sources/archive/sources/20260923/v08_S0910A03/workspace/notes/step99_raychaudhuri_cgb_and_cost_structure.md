# Step 99: Raychaudhuri floor, cost structure, and Chern–Gauss–Bonnet obstruction

> **Step 100 correction.** The Raychaudhuri identity/floor and the full-matrix cost decomposition below remain valid. The change of construction target from defect tending to zero to a finite value near `1.098`, the assertion that the graph-manifold completion has Euler characteristic zero or a global free torus action, the proposed connector absorption inequality in §4, and the asserted attainment/sharpness of the eigenvalue bounds at `1.098` are withdrawn. The `1.098` estimate is the older Step 2/64 lower bound for closed four-manifolds with nonpositive Euler characteristic; it does not apply to a connector with boundary or to pure real-hyperbolic-piece graph completions, whose Euler characteristic is positive. See `workspace/notes/step100_relative_cgb_graph_budget.md`.

Session `S0910A03`, Agent2 / Execute.

## 1. Raychaudhuri floor for the normal block

For a Gaussian 4-metric $g = dr^2 + q(r,s)$ with $H = \operatorname{tr}(q^{-1}q_r/2)$
and $W^\circ = W - (H/3)I$, the Raychaudhuri identity gives
$$
H' + \frac{H^2}{3} + |W^\circ|^2 = 3 - E_{rr}.
$$
Setting $u = H - 3\tanh r$ and multiplying by $\cosh^2 r$:
$$
\frac{d}{dr}[\cosh^2 r\, u] + \cosh^2 r\left(\frac{u^2}{3} + |W^\circ|^2\right)
= -\cosh^2 r\, E_{rr}.
$$
Integrating $0 \to R$ with $H(0)=0$ (minimal center) and $H(R)=3$ (expanding):
$$
\int_0^R \cosh^2 r(-E_{rr})\,dr
= 3\cosh^2 R(1-\tanh R)
+ \int_0^R \cosh^2 r\left[|W^\circ|^2 + \frac{u^2}{3}\right]dr.
$$
The RHS is strictly positive. The endpoint cost $3\cosh^2 R(1-\tanh R) \to 3/2$.

The comparison ODE $h' = (3+\delta) - h^2/3$, $h(0) = 0$, $h(R) = 3$ forces
$$
1 \le k\tanh(kR), \qquad k = \sqrt{1 + \delta/3}.
$$

| R   | δ\_min    | 12e^{−2R} | ratio |
|----:|----------:|----------:|------:|
| 1.0 | 1.317687  | 1.624023  | 0.811 |
| 1.5 | 0.507061  | 0.597445  | 0.849 |
| 2.0 | 0.199216  | 0.219788  | 0.906 |
| 3.0 | 0.029035  | 0.029745  | 0.976 |
| 4.0 | 0.004007  | 0.004026  | 0.995 |
| 5.0 | 0.000544  | 0.000545  | 0.999 |

**Radius continuation is mathematically necessary**, not a numerical convenience.
Verified: identity residual 3.4×10⁻³ on the quintic trial at rt=1.0.

## 2. Cost structure of the quintic transition

At $r_t = 1.0$ with the Step 94 charged Koiso center (S=1, Q\_max=0.5, wind=2):

**Block decomposition (peak operator norms)**:
- $E_{rr}$: 10.75 (peak at r\_frac = 0.32)
- $E_{ri}$ (Codazzi): 0.07
- $E_T$ (tangential): 28.66 (peak at r\_frac = 0.38) — **DOMINATES**
- Total: 28.66
- Raychaudhuri floor: 1.32

**$E_T$ term decomposition**:
| Term        | Peak op norm |
|:------------|------------:|
| Ric(q)      | 21.42       |
| 3q          | 3.00        |
| −K\_r       | 11.94       |
| −HK         | 9.79        |
| 2Kq⁻¹K     | 9.64        |
| **Total ET**| **28.66**   |

The spatial curvature Ric(q) of the intermediate trial metrics dominates ET.
The quintic creates metrics whose 3D Ricci is much larger than either endpoint.

**Conformal expansion benchmark**: $q = \cosh^2(r)q_0$ has $E_{rr}=E_{ri}=0$ and
$$
\|E_T\|_{\rm op} = 9.94\,\mathrm{sech}^2(r).
$$
This gives ET\_center = 9.94 (irreducible orbit-shape cost), decaying at rate
$e^{-2r}$. But this trial has $K(0) = 0$, not matching the charged Koiso center.

**Optimization**: X(r\_t) optimization with Nelder-Mead gives only modest
improvement (factor 1.2-1.7×). Additional radial perturbation modes give
negligible further improvement. The quintic parametrization is structurally
inadequate for large-R transitions.

## 3. Segmented construction: inner transition + exact expanding exterior

Replacing the monolithic quintic by:
- Inner segment [0, r\_t]: quintic from center jets to isotropic expansion
- Outer segment [r\_t, R]: exact $q = e^{2(r-r_t)}q_t$

Results:
- Inner residual is **fixed** (independent of R): 28.6 at r\_t=1.0
- Outer residual decays as $e^{-2(R-r_t)}$
- Total = max(inner, outer) = inner for all R ≥ r\_t + 1

The inner quintic residual gets **worse** with larger r\_t (60 at 1.5, 202 at
2.0) because the quintic oscillations grow with interval length.

## 4. Chern–Gauss–Bonnet Ricci pinching obstruction

**Theorem.** On any closed oriented 4-manifold $M$ with $\chi(M) = 0$, and
any smooth Riemannian metric with $\|\operatorname{Ric}+\Lambda g\|_{\rm op}
\le \delta$ for some $\Lambda \in \mathbb{R}$:
$$
\delta \ge \frac{|\Lambda|}{1+\sqrt{3}}
= \frac{|\Lambda|(\sqrt{3}-1)}{2}.
$$
For $\Lambda = -3$: $\delta \ge 3(\sqrt{3}-1)/2 \approx 1.098$.

**Proof.** By Chern–Gauss–Bonnet with $\chi = 0$:
$$
\int_M |\operatorname{Ric}^\circ|^2 = 2\int_M |W|^2 + \frac{1}{12}\int_M s^2.
$$
The pointwise bound $\|\operatorname{Ric}+\Lambda g\|_{\rm op} \le \delta$
gives all Ricci eigenvalues in $[\Lambda-\delta, \Lambda+\delta]$, so:
- $|\operatorname{Ric}^\circ|^2 \le 4\delta^2$ (optimal for the 2-2 split)
- $|s| \ge 4(|\Lambda|-\delta)$ when $\delta < |\Lambda|$

Since $|W|^2 \ge 0$:
$$
4\delta^2\operatorname{Vol} \ge \frac{4}{3}(|\Lambda|-\delta)^2\operatorname{Vol},
$$
giving $\sqrt{3}\,\delta \ge |\Lambda|-\delta$, hence
$\delta \ge |\Lambda|/(1+\sqrt{3})$. □

**Correct scope.** This is the Step 2/64 closed-manifold estimate. It applies only when the entire closed four-manifold has $\chi=0$ (or, with the corresponding sign conclusion, $\chi\le0$). A local free-$T^2$ connector has boundary, and local torus symmetry neither extends globally nor forces the completed graph manifold to have $\chi=0$. In the pure real-hyperbolic-piece setting, torus gluing preserves the sum of the positive piece Euler characteristics. Thus this estimate gives no finite target for that construction. Moreover, equating the pointwise upper bound for $|\operatorname{Ric}^\circ|^2$ and the lower bound for $s^2$ does not exhibit a metric attaining both bounds with $W=0$; no sharpness statement follows.

The correct graph-gluing identity is relative. If $N$ denotes the union of replacement regions, $V_{\rm removed}$ the total volume of the exact hyperbolic cusp pieces removed, and the complement is exactly sectional-curvature $-1$, then
$$
2\int_N|W|^2+12\bigl(\operatorname{Vol}(N)-V_{\rm removed}\bigr)
=\int_N\left(|E^\circ|^2+2\operatorname{tr}E-rac{(\operatorname{tr}E)^2}{12}\right),
\qquad E=\operatorname{Ric}+3g.
$$
This retains the hyperbolic topology term that the former absorption argument deleted. Details and scaling consequences are in `step100_relative_cgb_graph_budget.md`.

## 5. Tangential block: no Raychaudhuri analog, but universal nonvanishing

**No tangential floor** in the Raychaudhuri sense: the traceless Weingarten
evolution does not produce a positive-definite integrand.

**But** $E_T \equiv 0 \Rightarrow E \equiv 0$ (contracted Bianchi identity
with constraint propagation). So the exact Einstein germ is the only way to
achieve $E_T = 0$, and any finite-R connector must have $E_T \ne 0$ somewhere.

An exact Einstein metric with $H(0)=0$ satisfies $H(r) \le 3\tanh r < 3$ for
all finite $r$, so it cannot reach $H(R) = 3$ at any finite $R$.

**Whether** $\sup\|E_T\|_{\rm op} \to 0$ is achievable as $R \to \infty$
remains open. The conformal expansion benchmark gives $9.94\,\mathrm{sech}^2(r)$
but doesn't match the center data. The Koiso germ continuation domain is
estimated (not proved) at $r_{\rm focus} \sim 0.7$–$0.8$ from base-circle
focusing and $r_{\rm hf} \sim 0.035$ from high-frequency elliptic Cauchy
amplification ($\kappa=800$).

## 6. Synthesis

The retained local cost structure is:
1. **Normal cost**: the finite-length floor $\delta_{\min}(R)\sim12e^{-2R}$ tends to zero, so radius continuation is necessary.
2. **Tangential cost**: no proven positive floor; the displayed quintic has much larger tangential than normal error.
3. **Global completion**: the relevant Chern–Gauss–Bonnet statement is the relative identity above, not the closed-$\chi=0$ bound.

For a negative-branch counterexample, the full defect must still tend to zero. The finite value `1.098` is not a construction target. The large tangential residual shows only that this quintic parametrization is poor; it neither proves nor refutes a vanishing-defect connector.

## 7. Superseded material

Step 97's orbit-shape mechanism and cosh² trial are superseded by the full-matrix
analysis: the diagonal extraction, orbit roots 0 and −2, and coordinate-norm
ranking were incorrect (see Step 98 corrections). The conformal trial
$q=\cosh^2(r)q_0$ is retained only as an exterior benchmark with known ET = 9.94
at center.

## Files

- `workspace/scripts/step99_raychaudhuri_floor_and_projection.py`: floor computation
- `workspace/scripts/step99_radius_continuation.py`: radius sweep with block decomposition
- `workspace/scripts/step99_cost_structure_analysis.py`: ET term decomposition
- `workspace/scripts/step99_optimized_transition.py`: optimization experiments
- `workspace/scripts/step99_segmented_trial.py`: inner + outer construction
- `workspace/scripts/step99_cgb_ricci_floor.py`: CGB verification
- `workspace/data/step99_raychaudhuri_floor.json`
- `workspace/data/step99_radius_continuation.json`
- `workspace/data/step99_cost_structure_analysis.json`
- `workspace/data/step99_optimized_transition.json`
- `workspace/data/step99_segmented_radius_sweep.json`
- `workspace/data/step99_cgb_obstruction.json`
- `trace/ttcs/results/step99_ttcs01_generator1_integration.md`
- `trace/ttcs/results/step99_ttcs01_verifier1_integration.md`
