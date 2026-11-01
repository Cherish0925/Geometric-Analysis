# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step14_smoothing_vs_reduction_route.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Sessions/S0910A01/workspace/notes/step11_chart_accessibility_and_energy.md"
  ]
}
```

## Task

Evaluate the source-grounded smoothing route for the four-dimensional negative branch of Yau Problem 26. Read the Step 14 route note and the Ye Li 0911.3104 smoothing source carefully. Check the scale calculation: bounded local mean |Rm|^2 on a maximal-function good ball implies Ye Li's r^4-average smallness after choosing a fixed small physical radius. Determine exactly what is and is not supplied by Li's theorem as stated (complete/all-centers vs buffered local), and whether the route note faithfully identifies the missing bridges. Then assess how this could interact with the existing Derdziński chart-accessibility theorem: what additional statement would be sufficient to turn smoothing into a fixed-scale normal-cover/harmonic-chart contradiction, and what assumptions would be unsupported? Do not decide the session; give a rigorous mathematical memo with source-specific hypotheses and possible proof repairs.

## Output

# Verification memo: Ye Li smoothing in the four-dimensional \(\operatorname{Ric}\simeq-g\) branch

## 1. Fixed-small-radius calculation

Let
\[
f=|\operatorname{Rm}|^2,\qquad
\mathcal M_Rf(p)=\sup_{0<s\le R}\fint_{B_s(p)}f.
\]
Assume
\[
\operatorname{Ric}\ge-3g,\qquad \mathcal M_Rf(p)\le K_0.
\]
Fix an integer buffer factor \(m\ge1\), and choose \(\rho>0\) with
\[
(m+1)\rho\le R.
\]
For every \(q\in B_{m\rho}(p)\),
\[
B_\rho(q)\subset B_{(m+1)\rho}(p),
\]
so
\[
\int_{B_\rho(q)}f
 \le K_0\operatorname{Vol}B_{(m+1)\rho}(p).
\]
Moreover,
\[
B_{(m+1)\rho}(p)\subset B_{(2m+1)\rho}(q).
\]
Bishop–Gromov comparison at the center \(q\) therefore gives
\[
\fint_{B_\rho(q)}f
 \le K_0
 \frac{\operatorname{Vol}B_{(2m+1)\rho}(q)}
      {\operatorname{Vol}B_\rho(q)}
 \le K_0
 \frac{V_{-1}((2m+1)\rho)}{V_{-1}(\rho)}
 \le C_mK_0
\]
for \(0<\rho\le1\). Consequently,
\[
\frac{\rho^4}{\operatorname{Vol}B_\rho(q)}
 \int_{B_\rho(q)}|\operatorname{Rm}|^2
 \le C_mK_0\rho^4.
\]
Thus the Ye Li smallness condition holds throughout \(B_{m\rho}(p)\) once
\[
\rho\le
\min\left\{
1,\frac{R}{m+1},
\left(\frac{\varepsilon_{\mathrm{Li}}}{C_mK_0}\right)^{1/4}
\right\}.
\]
For the normalized near-Einstein metrics, \(|\operatorname{Ric}|\le K\) with fixed \(K\), and \(\rho\) may also be chosen so that \(\rho^2\le K^{-1}\). The resulting Li lifetime is then \(T\ge c\rho^2\).

This verifies the central scale observation in Step 14: an \(O(1)\) curvature mean is compatible with Li’s hypothesis at a sufficiently small physical radius. Since \(K_0,R\), and the buffer factor are fixed before the sequence index tends to infinity, \(\rho>0\) is sequence-independent. No rescaling sends the Einstein constant to zero.

There is one essential qualification. A bound only on the single macroscopic average
\[
\fint_{B_R(p)}|\operatorname{Rm}|^2\le K_0
\]
does not yield the displayed \(\rho^4\)-decay. Estimating a much smaller ball from \(B_R(p)\) introduces a volume ratio of order \((R/\rho)^4\), which cancels \(\rho^4\). The argument requires the truncated maximal estimate at \(p\), or at least bounds on the concentric averages at radii comparable to \((m+1)\rho\). Step 14 eventually invokes precisely this maximal-function input, but its scale calculation is clearest when written in the form above.

The global Noether energy estimate from Step 11 can supply such points. Local doubling under the Ricci lower bound gives a truncated Hardy–Littlewood estimate
\[
\operatorname{Vol}\{\mathcal M_Rf>\Lambda\}
 \le \frac{C(R)}{\Lambda}\int_M f.
\]
With globally bounded mean curvature energy, a sufficiently large fixed \(\Lambda=K_0\) leaves a fixed positive volume proportion. The analogous maximal estimate for the calibrated defect, whose global mean tends to zero, permits simultaneous selection of energy-good and defect-good centers.

## 2. Exact content of Li’s source

The source has two related formulations.

1. **Theorem 1.1:** on a smooth complete noncompact four-manifold, for one common radius \(r\le1\),
   \[
   \int_{B_r(x)}|\operatorname{Rm}(g_0)|^2\le\varepsilon
   \quad\text{for every }x\in M,
   \qquad |\operatorname{Ric}(g_0)|\le K.
   \]

2. **Theorem 3.6:** the absolute energy condition is replaced by
   \[
   \frac{r^4}{\operatorname{Vol}B_r(x)}
   \int_{B_r(x)}|\operatorname{Rm}(g_0)|^2\le\varepsilon.
   \]
   Although the extracted display omits “for every \(x\),” the theorem inherits the setup of Theorem 3.1, and its covering proof compares balls centered at arbitrary points. The mathematically coherent reading is uniform smallness for every center of the complete manifold.

The conclusion is a global Ricci flow
\[
\partial_tg=-2\operatorname{Ric}(g),\qquad g(0)=g_0,
\]
on
\[
0\le t<T,\qquad
T\ge C_1\min(r^2,K^{-1}),
\]
with
\[
\|\operatorname{Rm}(g(t))\|_\infty\le C_2t^{-1}.
\]

The proof also maintains
\[
\frac12g_0\le g(t)\le2g_0
\]
on the controlled interval; this is equation (3.8) in the continuation argument. Thus coarse bilipschitz comparison is present in the proof, although it is not part of the displayed conclusion of Theorem 3.6. The source does not state sharper distance distortion, derivative control at \(t=0\), or regularity transfer from \(g(t)\) back to \(g_0\).

The theorem as printed is for complete noncompact manifolds. A compact all-center version is very plausible and technically easier in several respects, but it still requires the smallness hypothesis throughout the whole compact manifold. The selected maximal-function ball supplies that hypothesis only in a buffer.

Most importantly, Li does not state a result of the form:

> Small dimensionless energy at every center of a buffered domain produces a flow on an interior subdomain for a sequence-independent time.

The introduction explicitly contrasts Li’s global direct-flow method with Yang’s genuinely local construction, for which local Sobolev or noncollapse data enter. A conformal completion of the selected domain is not automatic: curvature produced in the completion collar can be of order \(\rho^{-2}\), making
\[
\rho^4\fint|\operatorname{Rm}|^2
\]
order one rather than smaller than \(\varepsilon_{\mathrm{Li}}\). Uniform Ricci control in that collar is another nontrivial issue.

Accordingly, one selected good ball cannot be inserted directly into Theorem 3.6.

## 3. What smoothing itself supplies

If a complete or suitably localized Li flow were available, then at
\[
t_0=\theta\rho^2,\qquad 0<\theta<c,
\]
one would have
\[
|\operatorname{Rm}(g(t_0))|
 \le \frac{C}{\theta\rho^2},
\]
and the proof gives coarse comparison with the initial metric. Standard positive-time Ricci-flow estimates could then provide curvature-derivative bounds on a slightly smaller spacetime region.

These facts place \(g(t_0)\) in bounded-sectional-curvature collapsed geometry at the fixed physical scale \(\rho\). They do not, by themselves, produce the normal cover required in the Step 11 accessibility theorem. In particular:

- a bounded-curvature collapsed region may have short fibers that become contractible inside the buffer;
- a local CFG or frame-bundle description need not descend to a genuine normal cover of the selected base domain;
- noncollapse of the relevant lifted ball requires additional information about the local fibered fundamental group or an equivalent geometric input.

The Huang–Wang theorem cited in Step 14 supplies such an output only under its explicit hypotheses: closeness to a lower-dimensional Euclidean model and maximal nilpotency rank. Neither the Noether mean-energy estimate nor Li smoothing proves those hypotheses on the calibrated bulk.

Coarse bilipschitz comparison does transfer ball inclusions and volume estimates, up to fixed constants, once the same smooth covering domain has been identified. It does not transfer a \(C^{1,\alpha}\) harmonic radius from \(g(t_0)\) to \(g_0\). High-frequency second-derivative structure can be removed by parabolic smoothing while the two metrics remain uniformly bilipschitz.

## 4. Interaction with the Derdziński accessibility theorem

There are two mathematically sufficient forms of a smoothing bridge.

### 4.1 Geometry transferred to the original metric

For a maximal-function good center \(p_i\), it would suffice to obtain fixed \(h,v>0\) and a normal cover
\[
\pi_i:(\widehat U_i,\hat g_i(0))
 \longrightarrow (U_i,g_i(0)),
\]
with:

1. a precompact buffer containing the lifted \(3h\)-ball;
2. \(\operatorname{Vol}_{\hat g_i(0)}B_h(\hat p_i)\ge vh^4\);
3. a supplied \(C^{1,\alpha}\cap W^{2,p}\) harmonic chart of radius comparable to \(h\) at some lifted interior point;
4. the normal-cover mean estimate
   \[
   \fint_{B_h(\hat p_i)}\pi_i^*F_i
   \le C\,\mathcal M_RF_i(p_i)\longrightarrow0.
   \]

This is exactly the local object used by the repaired Step 11 theorem. The original near-Einstein and calibrated defects are then used without evolving them.

A Li flow plus bounded curvature at \(t_0\) would contribute to items 1–2, provided a genuine noncollapsed normal cover is obtained. Item 3 still requires a backward chart-transfer theorem. Bilipschitz comparison alone is insufficient. A suitable analytic statement would be a spacetime gauge estimate showing that, on the lifted interior,
\[
\Psi_i^*g_i(0)
\]
has sequence-uniform \(C^{1,\alpha}\cap W^{2,p}\) control in coordinates supplied by \(g_i(t_0)\). No such result appears in Li’s paper.

### 4.2 Applying Derdziński to the smoothed metric

Alternatively, one could use the chart for the normalized smoothed metric
\[
\bar g_i(\tau)
 =e^{-2\tau}g_i\!\left(\frac{e^{2\tau}-1}{2}\right),
\]
which satisfies
\[
\partial_\tau\bar g=-2(\operatorname{Ric}_{\bar g}+\bar g).
\]
A sufficient quantitative estimate would be
\[
\fint_{\widehat B_h}
F_{\bar g_i(\tau_0)}
\le
C\fint_{\widehat B_{Ch}}\pi_i^*F_{g_i(0)}
+\omega(\theta),
\qquad
\tau_0\asymp\theta\rho^2,
\]
where \(\omega(\theta)\to0\) independently of \(i\). Choosing \(\theta\) so that the right-hand side is below the fixed forbidden-germ gap \(\varepsilon_0(h,v)\) would produce the Derdziński contradiction.

The near-Einstein part has a plausible source-based repair. If
\[
S=\operatorname{Ric}_{\bar g}+\bar g,
\]
then under normalized flow
\[
\partial_\tau S=\Delta_LS-2S,
\]
so schematically
\[
\partial_\tau|S|
 \le\Delta|S|+C(|\operatorname{Rm}|+1)|S|.
\]
Li’s Corollary 3.5 is designed for this type of homogeneous linear equation. If \(|S(0)|\le\delta_i\), its estimate and the collapsed Sobolev bound give
\[
|S(t)|
 \lesssim
 A^{2/3}t^{-2/3}
 \left(\int_{B_{3\rho}}|S(0)|^3\right)^{1/3}
 \lesssim
 \delta_i\left(\frac{\rho^2}{t}\right)^{2/3}.
\]
At \(t=\theta\rho^2\),
\[
|S(t)|\lesssim C(\theta)\delta_i\longrightarrow0.
\]
A buffered local version would require the same cutoff and covering estimates, but the source contains the relevant Moser mechanism.

The Weyl calibration is substantially less automatic. The quantities
\[
s+8\sqrt6\,|W^+|,
\qquad
\mathcal G
\]
are nonlinear curvature functions, and their evolution contains quadratic curvature terms. Bounded initial \(L^2\) curvature does not provide a sequence-uniform small-time continuity modulus. Even for the linear heat equation, normalized eigenfunctions satisfy
\[
e^{t\Delta}\phi_\lambda=e^{-\lambda t}\phi_\lambda;
\]
on a bounded \(L^2\) family with \(\lambda\to\infty\), the difference from the initial data remains order one whenever \(\lambda t\gg1\). Thus choosing one small fixed \(\theta\) does not by itself ensure that calibrated Weyl data change only slightly across the whole sequence. A favorable evolution inequality, additional derivative compactness, or a weak curvature-measure transport theorem is needed.

## 5. Assessment of Step 14

Step 14 is mathematically accurate on the central scale point and correctly separates fixed physical radius from radii tending to zero with the sequence. Its description of Li’s theorem as complete and all-center is also correct.

The two principal analytic bridges identified there are real:

1. a buffered local Li theorem without a noncollapse hypothesis;
2. either backward transfer of controlled geometry to \(g_i(0)\), or quantitative retention of the near-Einstein and calibrated data by normalized flow.

A third component is already acknowledged later in the note but should be stated at equal prominence: bounded curvature after smoothing still does not imply the required noncollapsed normal cover. Maximal local rank, fiber survival in the chosen buffer, or a direct normal-cover volume theorem remains necessary.

Two phrases in Step 14 merit sharper interpretation:

- “The proof structure suggests a local version” is a plausible research direction, not a consequence of the cited theorem. A rigorous local construction must handle lateral parabolic data, collapsed Sobolev constants, cutoff errors, and deck equivariance.
- “Metric/distance distortion” is supported only at the coarse factor-two level by Li’s continuation proof. It does not provide harmonic-radius transfer or a \(C^{1,\alpha}\) comparison with the initial metric.

A precise source-grounded smoothing program therefore consists of three separate mathematical statements: buffered Li flow, noncollapsed genuine normal-cover production at positive time, and either backward harmonic-chart transfer or quantitative evolution of the full calibrated defect. The fixed-radius calculation supplies the hypothesis for the first statement on maximal-function good buffers, but Li 0911.3104 alone supplies none of the latter two.