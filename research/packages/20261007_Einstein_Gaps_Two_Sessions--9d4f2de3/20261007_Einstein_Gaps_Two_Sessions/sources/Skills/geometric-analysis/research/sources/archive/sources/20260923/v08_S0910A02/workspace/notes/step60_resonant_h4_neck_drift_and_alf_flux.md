# Step 60: Resonant H4 flux correction, neck-drift channel, and ALF collapse target

Session `S0910A02`. Agent3 / Actuator. Phase Execute.

This note corrects the Step-59 H4-dual analysis using the Wronskian propagator already present in Steps 34/42/49, and converts it into a rate-limited necessity theorem plus a named constructive failure channel.  It also reframes positive collapse: not as regular bounded-curvature collapse or a principal-circle problem, but as curvature-blowup bubbling with ALF models.

Main executable ledgers:

- `workspace/scripts/step60_resonant_flux_neck_alf.py`
- `workspace/data/step60_resonant_flux_neck_alf.json`
- `workspace/scripts/step60_neck_drift_schedules.py`
- `workspace/data/step60_neck_drift_schedules.json`
- `workspace/scripts/step60_warp_neck_drift_model.py`
- `workspace/data/step60_warp_neck_drift_model.json`

This remains a structural theorem/counterexample-channel result, not a proof or refutation of Yau--26.

## 1. Correction of Step 59: the matching obstruction is resonant flux, not a failed weighted estimate

Step 59 correctly isolated the two-scale matching as the H4-dual crux, but its proposed weighted open lemma was miscalibrated.  In the ALE frame for an Eguchi--Hanson bubble of metric scale `t`, the pointwise Ricci defect has size
\[
  |E_i|_{\tilde g_i}\le t_i\delta_i.
\]
The ambient quadratic signal in the metric perturbation is of size `t_i H_2`; the Wronskian signal is likewise linear in `t_i` under this convention.  For a weighted estimate with exponent \(\beta\), the source size at the outer ALE radius \(R_i\sim t_i^{-1/2}\) is
\[
  \|E_i\|_{C^0_{\beta-2}}
  \sim t_i\delta_i R_i^{2-\beta}
  = \delta_i t_i^{\beta/2}.
\]
The target needed to identify the ambient \(H_2\) coefficient on compact bubble sets is \(O(t_i)\).  Therefore, for every fixed \(\beta<2\), the factor over target is
\[
  \delta_i t_i^{\beta/2-1},
\]
which diverges along many natural schedules, even if \(\delta_i\log(1/t_i)\to0\).  The endpoint \(\beta=2\) is precisely the indicial root of the l=2 mode.  Thus the correct object is not a nonresonant Fredholm estimate with \(\beta\in(0,2)\); it is the resonant Wronskian/flux identity at \(\beta=2\), where one logarithm is unavoidable and computable.

The script `step60_resonant_flux_neck_alf.py` records this correction.  A second script, `step60_neck_drift_schedules.py`, checks explicitly that for every fixed \(\beta<2\), the nonresonant source factor eventually exceeds the target (e.g. for \(\beta=1.9\), the threshold for the schedule \(\delta=1/\log^2(1/t)\) is around \(\log_{10}(1/t)\approx95.5\)).

## 2. The rate-limited H4 necessity theorem

The l=2 radial model is
\[
  Lf=f''+\frac3r f'-\frac8{r^2}f=S(r),
\]
with homogeneous solutions \(r^2\) and \(r^{-4}\).  The Wronskian satisfies
\[
  r^3(f_1f_2'-f_2f_1')=-6,
\]
so the l=2 obstruction coefficient can be propagated by a scale-independent boundary flux.

For a constant source \(S\), the exact particular solution with zero initial data at \(r_0\) is
\[
  f_p(r)=\frac{S}{6}r^2\log\frac r{r_0}
        -\frac{S}{36}\left(r^2-r_0^6r^{-4}\right).
\]
This was verified symbolically by `step60_resonant_flux_neck_alf.py`: applying \(L\) to the displayed expression simplifies to \(S\), and both initial data vanish at \(r_0\).  The growing coefficient changes by
\[
  \Delta A_2 \sim \frac S6\log(R/r_0).
\]
In the geometric setting \(S\) is proportional to \(t_i\delta_i\), the outer ALE radius is \(R_i\sim t_i^{-1/2}\), and the signal coefficient is proportional to \(t_i\kappa\), where
\[
  \kappa=\langle R_\pm(p)\zeta,\zeta_{(k)}\rangle.
\]
Thus the relative error is
\[
  O\bigl(\delta_i\log(1/t_i)\bigr).
\]

Consequently the corrected theorem-level statement is:

> **Rate-limited H4-dual necessity theorem (A1/EH model, conditional on the standard annular gauge/projection setup).**
> Let a noncollapsed four-dimensional sequence satisfy \(\|\operatorname{Ric}_{g_i}-\Lambda g_i\|_{op}\le\delta_i\to0\) and develop an Eguchi--Hanson bubble of metric scale \(t_i\) at an \(A_1\) orbifold point.  After subtracting the known ambient \(H_2/H_4\) tower and using the l=2 Wronskian pairing against the smooth EH obstruction tensor \(o_k\), the flux identity gives
> \[
>   \lambda_k
>   = c\,\langle R_\pm(p)\zeta,\zeta_{(k)}\rangle
>     + O\bigl(\delta_i\log(1/t_i)\bigr)
> \]
> in relative units.  If \(\delta_i\log(1/t_i)\to0\), then exact bubbling forces the first vector obstruction \(R_\pm(p)\zeta=0\).

The theorem is conditional only in the same remaining geometric sense as earlier H4-dual work: one still needs rigorous compatible gauges, l=2 projection on annular regions of a Cheeger--Naber limit, nonlinear/gauge commutator control, and subtraction of the ambient \(H_2/H_4\) tower.  The Step-60 point is that, once those standard flux objects are in place, the rate statement follows from a one-dimensional Wronskian computation rather than from an unavailable weighted Fredholm estimate.

This also corrects the session record.  Step 34's radial-ODE computation of a \(\delta\log(1/t)\) resonance was structurally right.  Steps 35--36 and part of Step 42 removed it by using fixed annuli and an iterated \(i\to\infty\), \(R\to\infty\) limit, but that procedure presupposes the very compact-set \(h_i=O(t_i)\) matching rate under dispute.  Fixed annuli are valid only after the rate has already been propagated through the whole neck.

## 3. Named failure/counterexample channel: exponential bubble scale

The failure of the rate-limited theorem is no longer a vague "wild bubbling" channel.  It is the explicit regime
\[
  t_i \lesssim \exp(-c/\delta_i),
\]
where \(\delta_i\log(1/t_i)=O(1)\).  In this regime the pointwise Ricci defect can carry an order-one l=2 Wronskian drift over the long neck, so a nondegenerate curvature block at the outer/orbifold scale can appear degenerate at the bubble scale.

`step60_neck_drift_schedules.py` records concrete numbers.  For example, with \(t=\exp(-3/\delta)\), the scalar l=2 model gives relative flux drift \(3/12=0.25\) for every small \(\delta\); with \(t=\exp(-12/\delta)\), it gives drift of order one.  The number of dyadic scales is \(\sim(2\log2)^{-1}\log(1/t)\sim c/\delta\).

This is mathematically natural because \(C^0\) Ricci pinching controls only the value of Ricci, not \(\nabla\operatorname{Ric}\) or the Cotton tensor.  Since
\[
  \operatorname{div} W = \text{Cotton}(\operatorname{Ric}),
\]
the Weyl block can drift across many scales even when Ricci itself stays within \(O(\delta)\) of \(\Lambda g\).  This is the same free trace-free Hessian/Cotton channel exposed by Step 11.

## 4. Local opposite-warping realization of the drift channel

To test whether the exponential channel is merely formal, I built a local warping model.  In a two-dimensional base, take
\[
  u(r,\theta)=t\,r^2 A(\log r)\cos(2\theta).
\]
The script `step60_warp_neck_drift_model.py` verifies symbolically that
\[
  \Delta\bigl(t r^2 A(\log r)\cos(2\theta)\bigr)
  =t\bigl(A''(\log r)+4A'(\log r)\bigr)\cos(2\theta).
\]
For constant \(A\), this is a pure harmonic l=2 mode and the linear Ricci source vanishes.  If \(A\) changes by \(O(1)\) over a logarithmic neck of length \(L\), then
\[
  |\Delta u|/t = O(1/L).
\]
Choosing \(L\sim1/\delta\) gives an order-one l=2 curvature/Weyl block drift with Ricci source \(O(t\delta)\), and the matching relation \(R=e^L=t^{-1/2}\) gives \(t=\exp(-2/\delta)\).

This shows that the exponential failure channel is compatible with the same opposite-warping mechanism that produced the Step-11 spike: trace-free Hessian/Weyl data can be modified while Ricci sees only a small Laplacian source.  It is **not** a closed construction.  The unresolved constructive tasks are:

1. replace the linearized two-dimensional base calculation by a full doubly-warped or Kaluza--Klein metric with positive definite global tensor;
2. add long-neck caps without creating endpoint cutoff Ricci defects larger than \(O(\delta)\);
3. control quadratic gradient terms (they are small in this model when the actual metric amplitude on orbifold balls is \(O(tR^2)=O(1)\) only after correct subtraction/gauge normalization; this needs a real nonlinear estimate);
4. match to an actual EH/ALF bubble and a closed smooth topology.

But as an actuator test, this is important: the channel is not contradicted by the local equations, and the next construction attempt should attack these four obstructions directly.

## 5. Positive collapse corrected: curvature blow-up and ALF bubbles, not principal S^1 regular collapse

The previous handoff suggestion to use `S^2 x S^2` as a principal-circle background was wrong.  A closed principal \(S^1\)-bundle over a closed 3-manifold has Euler characteristic zero, whereas \(\chi(S^2\times S^2)=4\).  A localized spike in a fixed background also does not test collapse.

More generally, Step 58's Chern--Weil pinning gives a stronger conclusion.  In four dimensions, if
\[
  \|\operatorname{Ric}_g-g\|_{op}\to0,
  \qquad \operatorname{Vol}(M,g)\to0,
\]
then the scalar and traceless-Ricci Chern--Weil terms vanish and
\[
  \int |W|^2\to8\pi^2\chi,
  \qquad
  \int |W^\pm|^2\to2\pi^2(2\chi\pm3\tau).
\]
If \(\chi>0\), bounded-curvature collapse would force \(\int |W|^2\le \sup|W|^2\operatorname{Vol}\to0\), contradiction.  Equivalently, bounded-curvature collapse would carry an F-structure and hence impose the familiar vanishing-Euler-characteristic behavior.  Thus positive pinched collapse on \(\chi>0\) manifolds must include curvature blow-up/bubbling.

The correct local bubbles in collapsed four-dimensional positive pinching are therefore plausibly **ALF** rather than ALE: Taub--NUT, multi-Taub--NUT, Euclidean Schwarzschild/bolt models, and related toric rod bubbles already seen in Steps 34--35.  This reframes the "forced energy defect" question: not whether total energy is missing (it is saturated), but whether ALF bubble/neck fluxes are forced to lose energy to lower-dimensional limits, transition regions, or nonmaximal nilpotent topology.

## 6. First ALF flux model: different indicial structure from ALE

As a first cheap computation, I modeled the scalar ALF mass mode by the Gibbons--Hawking/Taub--NUT asymptotic equation on \(\mathbb R^3\):
\[
  V=1+\frac m r+\cdots,\qquad \Delta_{\mathbb R^3}V=0.
\]
The scalar roots for angular degree \(\ell\) are
\[
  \alpha_+=\ell,
  \qquad
  \alpha_-=-\ell-1,
\]
with radial Wronskian
\[
  r^2(f_+f_-'-f_-f_+')=-(2\ell+1).
\]
For the mass mode \(\ell=0\), the pair is \((0,-1)\), not the ALE l=2 pair \((2,-4)\).  The leading deviation is \(O(1/r)\), and it pairs against the constant mode with nonzero flux.  Therefore the ALE degeneracy condition \(R_\pm\zeta=0\) is not the right collapse obstruction.  ALF flux must be derived in fibration variables.

The scalar source accumulation also differs.  For a model source
\[
  S=t\delta r^{-q}
\]
in \(\Delta V=S\), the mass-flux drift is
\[
  \Delta m(R)=\int_1^R S r^2\,dr.
\]
It grows like \(R^{3-q}\) for \(q<3\), logarithmically at \(q=3\), and has a bounded tail for \(q>3\).  Thus ALF collapse can be more sensitive to slowly decaying errors than ALE H4 flux, and the correct tensor source weight is decisive.

This scalar computation is only a model.  The next real ALF task is to compute the tensor indicial roots and the boundary flux for Taub--NUT or Euclidean Schwarzschild in the actual Ricci/Lichnerowicz system, including circle-fibration gauge and the cosmological/positive-Einstein normalization.

## 7. Updated resolution state for Yau--26

What Step 60 establishes:

1. The H4-dual obstruction bridge is no longer an all-sequence theorem.  It gives a rate-limited theorem under \(\delta_i\log(1/t_i)\to0\), conditional on standard annular gauge/projection work.
2. The complementary failure channel is precise and constructive: exponentially small bubble scale relative to Ricci pinching defect, enabled by the trace-free Hessian/Cotton channel.
3. A local opposite-warping neck can realize the correct l=2 drift scale while keeping the Ricci/Laplacian source \(O(\delta)\).  This makes the counterexample channel credible enough to deserve construction pressure.
4. Positive collapse with \(\chi>0\) cannot be bounded-curvature regular collapse; it must bubble, and the natural collapsed bubbles are ALF with different indicial/flux structure.
5. Pure Chern--Weil energy counting remains saturated and cannot by itself obstruct the toric/rod adversary.

What is not established:

- no closed smooth near-pinched metric has been built from the neck-drift model;
- no ALF tensor flux obstruction has been computed;
- no mixed-row Einstein nonexistence has been proved;
- no sign branch or dimension of Yau--26 has been proved or refuted;
- no Lean formalization of a final theorem exists.

## 8. Highest-value next work

The next actuator/construction work should not return to symmetric principal-bundle almost-Killing tests or another product quotient.  It should attack one of two directly decisive local-to-global mechanisms:

1. **Neck-drift construction:** turn the local warping model into a genuine smooth annular metric segment with full Ricci-operator defect \(O(\delta)\), then cap/match it to an EH or orbifold model.  The first check is a full doubly-warped curvature computation for the ansatz \(u=t r^2A(\log r)\cos2\theta\) with long-neck cutoffs, including all gradient and transition terms.
2. **ALF flux computation:** compute the tensor Lichnerowicz indicial roots and boundary Wronskian for Taub--NUT / Euclidean Schwarzschild ALF bubbles and identify whether the leading mass/bolt mode creates a forced nonzero flux or an energy defect under positive Ricci pinching.

Either outcome advances the original Yau--26 problem: a successful neck-drift model opens a general counterexample channel; a proof that nonlinear/capping terms necessarily exceed \(O(\delta)\), or that ALF flux forces a defect, supplies the missing mechanism for the positive-collapse proof side.
