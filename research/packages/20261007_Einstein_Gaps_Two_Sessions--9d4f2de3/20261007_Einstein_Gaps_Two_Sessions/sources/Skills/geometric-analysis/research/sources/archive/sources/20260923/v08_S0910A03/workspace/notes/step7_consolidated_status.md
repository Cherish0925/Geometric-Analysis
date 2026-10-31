# Step 7 results after Step 8 review

The Step 7 computations supplied useful exact-model identities, but they do not classify an arbitrary collapsed near-Einstein sequence. The current bridge and all scope corrections are in:

`step8_cover_mean_transport_and_model_scope_corrections.md`.

## Exact model results retained

### Abelian adapted metrics

For an exact free isometric abelian adapted metric,

\[
\Delta_B\sqrt{\det G}=\left(|F|^2/4-\lambda N\right)\sqrt{\det G}.
\]

For \(\lambda<0\), this excludes the model when the base is parabolic and the orbit-volume function is bounded above. A circle base is excluded by periodic integration. Finite total volume does not imply bounded orbit volume, polar ends, or parabolicity. The near-Einstein coefficient \(N(1-\delta)\) is available only when the action is exactly isometric and adapted to the actual metric.

### Exact \(\mathrm{nil}^3\) cohomogeneity-one metrics

With \([E_1,E_2]=\sqrt\rho E_3\),

\[
v''=(3-\rho/2)v.
\]

This sign is verified by the \(\mathbb{CH}^2\) cusp. On a circle, the full Einstein trace system gives \(\rho\le2/3\), hence \(v''\ge(8/3)v\), contradicting periodicity.

On a finite interval, convexity follows only if endpoint behavior controls \(\rho\), e.g. \(\limsup_{\partial I}\rho<6\). With that condition and \(v\to0\) at both finite endpoints, a positive solution is impossible. Without endpoint control, \(\rho\) may diverge and no global convexity follows.

The \(\mathbb{CH}^2\) nil cusp has finite volume and infinite base length:

\[
v(s)=Ce^{4s/\sqrt6},\qquad s\in(-\infty,0].
\]

Thus finite volume gives no cusp-length bound.

## Errors withdrawn

- The cover degree cannot be dropped from a lifted total integral.
- Absolute smallness of the global deficit does not itself give a small lifted integral.
- The proposed capacity inequality is false and gives no regular-region volume estimate.
- Exact abelian and \(\mathrm{nil}^3\) models do not exhaust collapse of the actual pinched metrics.
- Interval \(\mathrm{nil}^3\) collapse is not excluded without endpoint control of \(\rho\).
- A fixed-topology negative pinching gap has not been proved.

## New bridge established in Step 8

For a normal local cover of a buffered base domain whose radius-\(3r\) cover ball remains interior, and with \(\operatorname{Ric}\ge-(n-1)Kg\), a cover-ball mean is controlled by the corresponding base-ball mean:

\[
\fint_{B_r(\hat p)}\pi^*F
\le \frac{V_{-K}^{(n)}(3r)}{V_{-K}^{(n)}(r)}
\fint_{B_r(p)}F.
\]

Combined with Fubini/Bishop–Gromov point selection and Naber–Zhang Proposition 6.4, this excludes any positive-volume set of collapsed points that has, at a fixed scale, a uniformly controlled low-dimensional model, maximal fibered nilpotency rank, and nondegenerating model scale. The unresolved object is the volume distribution of such Naber–Zhang-good points versus rank-drop, model-degenerate, residual-four-dimensional, and shrinking-scale regions.
