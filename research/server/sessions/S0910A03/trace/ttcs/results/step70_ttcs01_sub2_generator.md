# TTCS Independent Branch Record

```json
{
  "step_id": 70,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step70_mixed_boundary_formulation.md",
    "Sessions/S0910A03/workspace/notes/step69_anisotropic_cusp_compensation.md",
    "Sessions/S0910A03/workspace/notes/step67_corrections_and_analytic_neck_reopening.md"
  ]
}
```

## Task

The research asks whether a T²-invariant Einstein half-core exists: a Riemannian 4-metric on [0,R]×T³ with Ric=-3g, totally geodesic at t=0 (shape operator S=0) with prescribed Koiso center metric q on T³ (scalar curvature -6), and approaching an expanding cusp state at t=R. The T²-invariant Gaussian-gauge system is b_tt - e^{-2a}b_θθ = lower order, which is WAVE-like (hyperbolic), not elliptic. The central obstruction is: every scalar-minus-six T³ metric has S'(0) = Ric_q♯+3I with a negative eigenvalue (from Preissmann/sectional curvature). Numerical Cauchy evolution for all tested conformal seeds shows H reversal before reaching the expanding regime. Li-Liu's exact PE-to-AH-cusp Einstein metrics on (0,∞)×T³ demonstrate global compensation exists without reflection symmetry, using the Toda equation. QUESTION: (1) Characterize when a T²-invariant reflection-symmetric Einstein half-core exists: what conditions on the center metric q guarantee that the exact analytic continuation reaches an expanding cusp state rather than developing a singularity? (2) For the approximate problem, if we allow Einstein defect ||Ric+3g||≤δ, can a smooth core be constructed over a domain of length R~log(1/δ) connecting Koiso center to cusp? (3) Is there a deformation of the Li-Liu ASD Toda solution that breaks W⁺=0 while acquiring a nearly-geodesic T³ slice?

## Output

## Reframing before the three questions

The single most consequential correction to the current picture concerns the character of the equation. In Riemannian signature the tangential Ricci operator in Gaussian gauge has the form $\mathrm{Ric}_{ij}\sim-\tfrac12\partial_{tt}g_{ij}-\tfrac12\Delta_{\text{slice}}g_{ij}$ — both second derivatives enter with the *same* sign, so $\mathrm{Ric}_g+3g=0$ is genuinely of Laplace type, not wave type. The diagonal $T^2$-invariant reduction looks "wave-like" only because Gaussian gauge is not elliptic-complete: the symbol matrix I get from the Step 70 components is
$$
\det\begin{pmatrix}-\tau^2 & -e^{-2a}k^2 & -e^{-2a}k^2\\ 0 & -\tau^2-e^{-2a}k^2 & 0\\ 0&0&-\tau^2-e^{-2a}k^2\end{pmatrix}=-\tau^2\,(\tau^2+e^{-2a}k^2)^2,
$$
whose only real zero is $\tau=k=0$. The two factors $(\tau^2+e^{-2a}k^2)$ are elliptic; the bare $\tau^2$ is the gauge/constraint degeneracy. So the system is a degenerate-elliptic constrained system, and the DeTurck completion (all five components) is strictly elliptic.

The practical consequence: **forward Cauchy evolution from the center is solving an elliptic equation as an initial-value problem, which is ill-posed (Hadamard). The exponential growth of high-$\theta$ Fourier modes at $t\approx0.45$ is the expected amplification of an ill-posed elliptic march, not evidence of a geometric singularity.** The blow-up seen in the Galerkin runs therefore does *not* decide Question 1. The well-posed object is the two-point elliptic problem: the reflection-symmetric core is exactly an *even* Einstein metric on the double $[-R,R]\times T^3$, and $S=0$ at $t=0$ is the natural Neumann-type end condition of that even problem. Existence should be settled by the DeTurck elliptic two-point solve (Step 70, 3b) with Neumann data ($\partial_t g=0$) at $t=0$ and cusp asymptotics at $t=R$ — not by marching. The sign-reversed eigenvalue of $S'(0)$ is a Taylor coefficient of the solution, not an impediment to solvability of that elliptic problem.

## A structural fact that reshapes the disproof direction

Before optimizing cores it is worth seeing how strong the input pinch already is. In four dimensions, with $\mathrm{Ric}\in[c,C]g$ pointwise and eigenvalues $\lambda_i$, write $s=\sum\lambda_i$ and $\mathrm{Ric}_0$ for the trace-free part. Chern–Gauss–Bonnet and signature give
$$
\chi=\frac1{8\pi^2}\!\int\!\Big(|W|^2+\tfrac{s^2}{24}-\tfrac12|\mathrm{Ric}_0|^2\Big),\qquad
2\chi+3\tau=\frac1{4\pi^2}\!\int\!\Big(2|W^+|^2+\tfrac{s^2}{24}-\tfrac12|\mathrm{Ric}_0|^2\Big).
$$
If the admissible window $[c,C]$ is *narrow* around a value $\mu$, then $|\mathrm{Ric}_0|^2\to0$ and $s\to4\mu$, forcing
$$
\chi\ \ge\ \frac{\mu^2}{12\pi^2}\,\mathrm{Vol}(M)\ >\ 0 .
$$
So a narrow two-sided Ricci pinch by itself *manufactures* the Hitchin–Thorpe/positive-$\chi$ conclusion together with a volume lower bound; it also feeds Bishop–Gromov and minimal-volume-entropy inequalities. This means the manifolds that fail to be Einstein for the "cheap" reasons (Sambusetti-type simplicial-volume-versus-$\chi$ violations, Hitchin–Thorpe violations) are *the same manifolds that cannot carry a narrow-window pinched metric*. The disproof direction therefore cannot use those manifolds in its hard case.

The strategic content: to disprove the statement one must exhibit, **for every** universal window $[c_n,C_n]$, a pinched metric on a non-Einstein manifold — including narrow windows, where the pinch already implies Einstein's classical necessary inequalities. A *wide* window frees $|\mathrm{Ric}_0|^2$ and can push $\chi\le0$, so wide-window counterexamples are cheaper — but they do not suffice, because the statement only asks for the existence of *some* $c_n<C_n$. Conversely a proof may *choose* a narrow window, where the task becomes "approximately-Einstein $\Rightarrow$ exactly-Einstein" — a deformation existence question, not a curvature inequality. This dichotomy is, I think, the real axis of the problem, and it says the graph-manifold effort is implicitly living in the narrow-window regime where its own pinch input fights the topological non-existence it wants.

## Q1: when the exact reflection-symmetric core continues to an expanding cusp

**Exact structural input.** A totally geodesic slice in a $\mathrm{Ric}=-3g$ four-manifold has $\mathrm{Scal}_{\text{slice}}=\mathrm{Scal}_{\text{amb}}-2\mathrm{Ric}(\nu,\nu)=-12+6=-6$; this is why the center must be a $\mathrm{Scal}=-6$ metric, and such metrics on $T^3$ exist (Kazdan–Warner: $T^3$ is of the scalar-flat type, and a function that is below zero everywhere is realized as a scalar curvature). The diagonal spatially-averaged dynamics reduce cleanly. In log-scale-factor variables $g_t=\mathrm{diag}(e^{2\beta_i})$ the exact tangential evolution gives
$$
\ddot\beta_i \;=\; 3 \;-\; H\dot\beta_i \;+\; R_i,\qquad H=\textstyle\sum_j\dot\beta_j,
$$
with $R_i$ the intrinsic-Ricci contribution in the frame. At the center $\dot\beta_i=0$, $H=0$, so
$$
\ddot\beta_i(0)=3+\mathrm{Ric}_{q,i}=-K_{jk},
$$
using the three-dimensional identity $\mathrm{Ric}_{q,i}+3=-K_{jk}$ for the complementary plane. Preissmann forbids all sectional curvatures below zero on $T^3$, so at least one $K_{jk}\ge0$ somewhere and the corresponding direction has $\ddot\beta_i(0)\le0$: the center *must* begin with a contracting or stationary direction. This is exact, not seed-dependent.

**The continuation competition (the actual condition).** The linear behaviour of the contracting mode is benign: near $t=0$, $H\approx3t$, $\dot\beta_i\approx-Kt$, and the friction term $-H\dot\beta_i\approx+3Kt^2$ is *restoring* — it re-enters at order $t^2$ and turns the acceleration positive around $t\sim1/\sqrt3$, with $\beta_i$ having dropped only by $O(K)$. So the cosmological push and friction alone would re-expand the contracting direction after finite decrease. What decides Question 1 is whether the *intrinsic* term $R_i$ — which grows as the slice becomes more anisotropic (Kasner-type amplification) — overtakes the friction before $t\sim1/\sqrt3$. In the tested seeds the ill-posed march reports trouble near $t\approx0.45<1/\sqrt3$, consistent with intrinsic amplification winning, but as noted this march is not a reliable arbiter.

This gives a concrete, testable characterization rather than a verdict: **the reflection core continues to the expanding regime iff the anisotropic intrinsic curvature stays subdominant to the friction $-H\dot\beta$ over the transient, equivalently iff the center metric avoids the Kasner attractor and lands in the basin of the isotropic future fixed point of the expansion-normalized (Wainwright–Hsu) flow.** Because we may *choose* $q$ among all $\mathrm{Scal}=-6$ metrics, the productive subproblem is variational:
$$
\inf\big\{\ \max_{\text{planes}}K_+(q)\ :\ q\in\mathrm{Met}(T^3),\ \mathrm{Scal}_q\equiv-6\ \big\},
$$
i.e. minimize the forced positive sectional curvature (equivalently minimize the largest $-\ddot\beta_i(0)$). A center realizing a small value of this infimum starts nearly all-expanding and is the strongest candidate to continue. This is worth computing directly (constrained optimization over conformal-plus-anisotropic families), and it converts Q1 from "does the germ blow up" into "how small can the forced contraction be made."

**A cross-field framing that may already contain the answer.** A reflection-symmetric Riemannian Einstein metric with a totally geodesic slice is precisely a *real tunneling geometry* / time-symmetric instanton: the slice is a moment of time symmetry that continues to Lorentzian $\mathrm{Ric}=-3g$ (an AdS cosmology). The existence of $\mathrm{Ric}=-3$ fillings with a prescribed time-symmetric slice and AH/cusp asymptotics is exactly the "no-boundary/tunneling" filling question in AdS quantum cosmology. The relevant source family to retrieve: Hartle–Hawking and Hawking–Turok tunneling instantons in AdS, real-tunneling geometries (work of Gibbons–Hartle, Garriga), and Poincaré–Einstein filling existence/non-existence for flat $T^3$ conformal infinity (Anderson; Graham–Lee). These may supply either an existence route (constructive fillings with a $T^3$ time-symmetric slice) or the exact quantity that obstructs one.

## Q2: the approximate core and why $R\sim\log(1/\delta)$ is the right length — and why exactness is not needed

The correct dilution is visible in the operator norm, which is the norm the problem actually uses. Take the expanding cone over the *fixed* center: $g=dt^2+e^{2t}q$, $\mathrm{Scal}_q=-6$. The warped-product formulas give exactly
$$
\mathrm{Ric}(\nu,\nu)=-3,\qquad \mathrm{Ric}_{ij}+3g_{ij}=\mathrm{Ric}^q_{ij}.
$$
As a $(0,2)$-tensor the defect is the *fixed* tensor $\mathrm{Ric}^q$, but as an endomorphism measured against $g=e^{2t}q$,
$$
\big\|\mathrm{Ric}_g+3g\big\|_{\mathrm{op}}=e^{-2t}\,\big\|\mathrm{Ric}^q\big\|_{q}.
$$
So the operator-norm defect decays like $e^{-2t}$, and
$$
\big\|\mathrm{Ric}_g+3g\big\|_{\mathrm{op}}\le\delta\quad\Longleftrightarrow\quad t\ \ge\ \tfrac12\log\!\frac{\|\mathrm{Ric}^q\|_q}{\delta}.
$$
This is the mechanism behind $R\sim\tfrac12\log(1/\delta)$: begin with the exact analytic Koiso germ near $t=0$ (defect zero), transition over an $O(1)$ layer to the expanding cone over the fixed $q$, and let the cone dilute the anisotropic intrinsic Ricci by $e^{-2t}$. The transition-layer defect is $O(1/R)$ from the interpolation of $S$ from $0$ to $\approx I$, so it too is $\lesssim\delta$ once $R\gtrsim1/\delta$; the dominant cost is the $e^{-2t}$ dilution, giving the logarithmic length. The volume cost is $\mathrm{Vol}\sim e^{3R}\sim\delta^{-3/2}$, and the $T^2$ lattice quotient of Step 69 ($\mathrm{Vol}(q_N)=N^{-2}\mathrm{Vol}(q_1)$) is the natural device to keep the interface volume finite.

The deeper point Q2 exposes: **the expanding cone over any $\mathrm{Scal}=-6$ slice already keeps the Ricci endomorphism inside a *fixed* window,** since $\mathrm{Ric}\,g^{-1}=-3+e^{-2t}\mathrm{Ric}^q q^{-1}\in(-3-\varepsilon,-3+\varepsilon)$ for $t\gtrsim1$ and equals $-3$ exactly on the germ. So the two-sided pinch — the *input* of Yau 26 — never requires an exact Einstein core; it requires a smooth metric with $\mathrm{Ric}$ confined to a dimension-only window, which the cone supplies without $\delta\to0$. The exact-continuation, reflection, and totally-geodesic-matching difficulties are therefore self-imposed by insisting on exact Einstein cores. The genuine remaining substance is (i) whether two such pieces (or a piece and a hyperbolic cusp) can be joined smoothly with $\mathrm{Ric}$ staying in the window, and (ii) whether the assembled closed manifold fails Einstein for a reason that survives the pinch — which by the CGB argument above cannot be a narrow-window Hitchin–Thorpe/simplicial-volume reason.

**An alternative engine that may survive the pinch.** LeBrun's Seiberg–Witten Einstein constraints are not implied by Hitchin–Thorpe and may be evadable by pinched but non-Einstein metrics. For a $4$-manifold with a nonzero SW basic class, Einstein existence requires curvature integral inequalities beyond CGB; but $\int s^2\,dV=16\mu^2\mathrm{Vol}$ is scale-invariant and, for a pinched metric, is controlled by the pinch, so it is not freely large. The decisive computation is: over metrics with $\mathrm{Ric}\in[c,C]g$, what region of the invariant triple $\big(\int s^2\,dV,\ \int|W^+|^2\,dV,\ 2\chi+3\tau\big)$ is achievable? If a pinched metric can be built with $\int(2|W^+|^2+\tfrac{s^2}{24})$ exceeding $4\pi^2(2\chi+3\tau)$ on an SW-obstructed manifold, that disproves the statement without any cusp gluing. If the pinch forces that combination back below the SW threshold, that is strong evidence toward the positive direction in dimension four. This is a cleaner and more decisive test than the graph-manifold assembly and should be prioritized because it can change the top-level judgment.

## Q3: deforming Li–Liu off $W^+=0$

There is a clean reason the deformation is *forced*, with a computable rate. Reflection across a totally geodesic hypersurface is an orientation-reversing isometry that exchanges $W^+\leftrightarrow W^-$. If the metric is ASD ($W^+\equiv0$) and reflection-symmetric, then $W^-$ is carried to $W^+=0$, forcing $W^-\equiv0$ as well: the metric is conformally flat, i.e. real hyperbolic $H^4$, whose totally geodesic slices are $H^3$, never a curved $T^3$. **Hence no ASD Einstein metric contains a curved-$T^3$ totally geodesic slice; breaking $W^+=0$ is unavoidable, and the amount of $W^+$ turned on is tied to the reflection asymmetry, i.e. to $|S|$ on the near-geodesic slice.** The quantity to compute is the forced relation $|W^+|\gtrsim f(|S|)$: linearize $\mathrm{Ric}=-3g$ around the explicit Li–Liu solution $h=\xi^{-2}(W\,d\xi^2+W^{-1}\eta^2+We^vg_{T^2})$, $W=1-\tfrac12\xi v_\xi$, with $(e^v)_{\xi\xi}+\Delta_{T^2}v=0$. The self-dual/anti-self-dual split of the linearized operator around an ASD Einstein background is well studied (the deformation complex of ASD Einstein metrics), and the $W^+$-turning-on modes are the cokernel/image of a definite piece of that complex; the Toda/Laplace structure makes the background explicit enough to compute the linear map from a prescribed near-geodesic $S$ on a $\xi$-slice to the induced $W^+$. Two outcomes are decisive: if the linear map from "$S=0$ data" to "$W^+$" has a solvable inhomogeneous problem with $|W^+|=O(|S|)$, a genuine reflection-near-symmetric non-ASD core exists as a deformation and Q1/Q2 gain an exact anchor; if instead $|W^+|$ is bounded below independent of $|S|$ (a rigidity of the ASD family), then the Li–Liu route cannot approach a totally geodesic $T^3$ and the core must be sought entirely outside it.

A complementary reading of Li–Liu that avoids the reflection issue: their solutions already realize the compensation you want (fixed-scale inhomogeneous $T^2$ geometry carried into a rank-three collapsing flat cusp) *without* a totally geodesic slice. If the assembly does not actually require reflection symmetry — and per Q2 the pinch input does not require exact Einstein or exact matching — then the more productive use of Li–Liu is as one exact end of a *non-symmetric* two-piece join: Li–Liu PE-to-cusp on one side, expanding-cone-over-Koiso on the other, matched in the window rather than exactly. That sidesteps the $W^+$ rigidity entirely.

## Distinguishing computations and sources worth the cost

The DeTurck elliptic two-point solve on $[0,R]\times T^3$ with Neumann ($S=0$) data at $t=0$ and cusp asymptotics at $t=R$ is the one computation that would actually decide Q1, because it replaces the ill-posed march with the well-posed elliptic problem; run it against the variational center that minimizes forced positive sectional curvature. The achievable-region computation for $(\int s^2,\ \int|W^+|^2,\ 2\chi+3\tau)$ over pinched metrics is the computation that could change the top-level judgment either way, and connects directly to LeBrun's inequalities. The linearized ASD deformation complex around the explicit Li–Liu background is the computation that resolves Q3. Source families to retrieve in ordinary terms: Wainwright–Ellis / Ringström expansion-normalized dynamical systems for Einstein-$\Lambda$ isotropization; Anderson and Graham–Lee on Poincaré–Einstein fillings of flat-$T^3$ conformal infinity and their non-existence results; real-tunneling / Hartle–Hawking AdS instanton geometries with a time-symmetric slice; LeBrun's Seiberg–Witten Einstein estimates and Sambusetti's simplicial-volume non-Einstein $4$-manifolds; and the deformation theory of ASD Einstein metrics for the $W^+$-turning-on linearization.