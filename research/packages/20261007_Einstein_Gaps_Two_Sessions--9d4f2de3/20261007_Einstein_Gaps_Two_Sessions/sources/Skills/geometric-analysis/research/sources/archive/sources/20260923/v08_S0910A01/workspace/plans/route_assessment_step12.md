# Route assessment after Step 12

## What Step 12 established

1. **Step 11 Taub--NUT curvature error repaired.**  The coordinate script
   `workspace/scripts/step12_taub_nut_ads_coordinate_curvature.py` computes the
   Christoffel symbols, Riemann tensor, Ricci tensor, curvature-operator blocks,
   and calibrated defect directly from the coordinate metric
   \[
   g_\nu=F_\nu^{-1}dr^2+(r^2-\nu^2)d\Omega_2^2+4\nu^2F_\nu(d\psi+\cos\theta d\phi)^2.
   \]
   At \(\nu=0.01,r=0.5\) it gives \(\operatorname{Ric}_{ON}=-I\) to numerical
   precision, scalar \(-4\), curvature-operator trace \(s/2\), \(W^+=0\) in the
   coordinate orientation, and nonzero opposite-half eigenvalues
   \((-0.150751470651,-0.150751470651,0.301502941302)\).  Running A03's exact
   symbolic script independently confirms
   \[
   |W|^2_{(0,4)}={32\nu^2(4\nu^2-3)^2\over3(r+\nu)^6},\quad W^+=0.
   \]

2. **Taub--NUT does not refute adjustable-buffer accessibility.**  A large ball
   containing the NUT can make the Hopf fiber contractible and hence invisible to
   the cover, but that same core-containing fixed-radius region has mean full
   Weyl energy \(\sim3/(\nu R^3)\).  At fixed annular distance from the NUT, one
   can choose a smaller buffered domain first; the Hopf fiber survives and unwraps,
   and with \(z=2\nu\psi\) the lifted limit is real hyperbolic four-space
   (sectional curvature \(-1/3\)).  Such annular regions are accessible but have
   macroscopic calibrated defect \(16\) in the coordinate orientation.  Therefore
   the general fixed-scale accessibility question remains alive.

3. **Standard NUT is not a calibrated-bulk model.**  In the coordinate orientation
   the LeBrun scalar--Weyl term is exactly \((s+8\sqrt6|W^+|)^2=16\).  Reversing
   orientation, the nonzero half has the wrong sign pattern; the shell where
   \(|W^+|^2=1/24\) lies at
   \[
   r_\nu\sim576^{1/6}\nu^{1/3}=2\,3^{1/3}\nu^{1/3},
   \]
   tends to zero physical scale, and has tensor defect \(F=35/36\), while the
   cumulative mean energy from the NUT to that shell diverges like \(\nu^{-2}\).

4. **Pontryagin density is diffuse in a near-critical LeBrun sequence.**  From
   \(s\to-4\) in \(L^\infty\), \(E\to0\) in \(L^\infty\), and the completed-square
   remainder, one obtains
   \[
   \fint |W^+|^2\to {1\over24},\qquad
   \fint\left|2|W^+|^2+{s^2\over24}-{1\over2}|E|^2-{3\over4}\right|\to0.
   \]
   Thus \(p_1(\Lambda^2_+)\) mass follows volume up to a global \(o(A)\) error.
   It is not concentrated in tiny NUT cores.  The remaining collapse mechanism,
   if any, is diffuse non-basic mixed \(\Lambda^2_+\) connection curvature.

5. **Controlled-chart theorem repaired.**  The Step 11 chart-accessible exclusion
   remains valid only in controlled-chart form.  The harmonic chart/control
   package is part of the local hypothesis.  The proof uses the harmonic-coordinate
   Ricci equation and strong finite-\(p\) \(W^{2,p}\) convergence on smaller balls;
   it does not derive harmonic radius from bounded Ricci plus cover noncollapse
   alone.  Basepoint selection in the negative branch uses local maximal-function
   estimates under Ricci lower bounds, not a Myers diameter.

6. **Rank-one mixed-curvature toy calculations begun.**  The flat-base
   constant-fiber Cartan calculation shows constant scaled twist gives zero
   \(\sum F_i\wedge F_i\).  A variable-fiber toy shows closed one-jets can carry
   nonzero local Pontryagin coefficient through coupling between \(u=d\log\ell\)
   and scaled twist, but the precise Chern--Weil normalization and base-curvature
   terms remain to be matched.  A concrete metric
   \[
   dx^2+dy^2+dz^2+e^{2ux}(dt+C y dz)^2
   \]
   has
   \[
   \operatorname{Ric}=\operatorname{diag}(-u^2,-C^2/2,-C^2/2,C^2/2-u^2),
   \]
   so it cannot be \(\operatorname{Ric}=-\kappa g\) with \(\kappa>0\).  The
   simplest flat-base closed one-jet therefore does not give a near-negative-
   Einstein diffuse model.

## Files produced or repaired

- `notes/step12_taub_nut_accessibility_and_diffuse_pontryagin.md` — main Step 12 synthesis.
- `scripts/step12_taub_nut_ads_coordinate_curvature.py` — coordinate curvature computation.
- `scripts/step12_taub_nut_ads_multiscale_calibration.py` — exact multiscale NUT calibration.
- `data/step12_taub_nut_ads_multiscale.csv` and `data/step12_taub_nut_ads_multiscale_summary.json` — numerical/multiscale outputs.
- `figures/step12_taub_nut_ads_multiscale.png` — visual calibration.
- `scripts/step12_rank1_sd_connection_cartan.py` — constant-fiber rank-one Cartan toy.
- `scripts/step12_rank1_variable_length_cartan.py` — variable-fiber rank-one Cartan toy.
- `scripts/step12_rank1_exp_twist_metric.py` — concrete exponential twist metric test.
- `notes/step11_chart_accessibility_and_energy.md` and `plans/route_assessment_step11.md` — repaired with Step 12 warnings and replacements.
- TTCS verification: `trace/ttcs/results/step12_ttcs01_verifier1_integration.md`.

## Consequences for the research route

The negative LeBrun route should no longer focus on a single F-per-NUT ratio.  A
standard NUT core is too curved on core-containing fixed balls and too defective
on annular accessible balls.  The charge in the actual near-critical sequence is
already spread over the bulk.  The central mathematical question is now:

\[
\text{Can diffuse non-basic mixed }\Lambda^2_+\text{ connection curvature prevent}
\]
\[
\text{fixed-scale chart accessibility on most volume while }F\to0\text{ and }P\to3/4?
\]

The most valuable next work is constructive/theoretical rather than another NUT
sample.  It should derive a full rank-one Kaluza--Klein reduction of the Ricci
equations, Weyl spectrum, and \(p_1(\Lambda^2_+)\) density with variable fiber
length, base curvature, O'Neill tensor, and scaled twist.  The calculation should
answer whether the calibrated conditions
\[
\operatorname{Ric}\approx-g,\quad |W^+|^2\approx1/24,
\quad \operatorname{spec}(W^+)\approx(-1/6,1/12,1/12),
\quad P\approx3/4
\]
allow persistent mixed curvature one-jets without producing a fixed-scale
unwrapping/harmonic chart.  If the reduced system has no such local solutions,
there may be a quantitative rank-recovery theorem.  If it has solutions, they
become genuine countergeometry candidates needing global/topological closure.

A02's toric determinant/twist equations are the parallel positive-branch and
rank-two analogue: determinant equations and boundary degeneration may force
scale in simply connected/fixed-point settings, while free quotients escape.  Any
next step should keep the two branches connected through the common reduced
collapse equations but not conflate their signs or characteristic classes.
