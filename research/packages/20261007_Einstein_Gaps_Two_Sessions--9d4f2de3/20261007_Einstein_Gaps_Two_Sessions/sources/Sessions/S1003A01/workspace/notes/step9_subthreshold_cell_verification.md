# Step 9 — Verification state of the finite-scale perpendicular subthreshold cell

Session S1003A01, Step 9, Agent3, Execute.

## 1. Fixed witness and the quantity that matters

Keep the Step-8 degree-eight coefficient vector fixed; no stationarity or numerical infimum is used.  It is stored in

`workspace/data/perp_collar/x0.01_X8_J_d8.json`.

The cell is in the `Ric_CH=-6g` normalization and has

\[
g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2,
\qquad x_0=10^{-2},\quad X=8.
\]

The target is

\[
 J_6=\int|\operatorname{Ric}+6g|^2
 =P+\frac14\int(s+24)^2,
 \qquad P=\int|\operatorname{Ric}^\circ|^2.
\]

Under the simultaneous rescaling \(\widetilde g=6g\), the background satisfies
\(\operatorname{Ric}_{\widetilde g}=-\widetilde g\), and scale invariance of the dimension-four integral gives

\[
 \int|\operatorname{Ric}_{\widetilde g}+\widetilde g|_{\widetilde g}^2dV_{\widetilde g}
 =J_6(g).
\]

Thus `J` in the record is exactly the single-blowup cell cost \(J_1/(8\pi^2)\) in I54 §2.

## 2. Independent numerical reconstruction

The local verifier `workspace/scripts/perp_collar_verify.py` uses two formula sets:

1. the coordinate-curvature implementation inherited from `o11_perp_cell.py`;
2. the independently Cartan-verified spin formula, integrated in logarithmic radius with split Gauss quadrature.

For the frozen \(X=8\) record it gives

\[
 \frac{P}{8\pi^2}=0.99910870273352,\qquad
 \frac{J_6}{8\pi^2}=0.99911624313525.
\]

The coordinate implementation at 600, 1200 and 2400 nodes gives \(J=0.9991162433,0.9991163627,0.9991163780\), while the split spin computation at 1200 and 3000 gives identical values to about \(6\times10^{-14}\).  The slight coordinate drift at high unsplit order is numerical conditioning near the bolt, not a sign change.

The peer independently reconstructed the metric in a new local script importing neither `DualCell` nor this Session's spin code.  Their 200/400/800 split orders gave

\[
 P/(8\pi^2)=0.99910870273359,
 \quad (J-P)/(8\pi^2)=7.54040173166\times10^{-6},
 \quad J/(8\pi^2)=0.99911624313532,
\]

and their positive-square and relative-calibration formulas agreed to \(4\times10^{-15}\).  This is peer message 756.

A second fixed witness with a larger margin is
`workspace/data/perp_collar/x00.01_X16_J_d8.json`.  Its independent local output is

\[
 P/(8\pi^2)=0.99887845250601,
 \qquad J/(8\pi^2)=0.99890294371985,
\]

in `workspace/data/perp_collar/verify_x0.01_X16_J_d8.json`.  This has a deficit about \(1.10\times10^{-3}\), but requires a larger embedded ball.  The \(X=8\) witness is retained as the smaller geometric construction.

## 3. Smoothness and exact-collar structure

The profile is built from entire functions of

\[
 u=\frac{\log(x/x_0)}{\log(X/x_0)}
\]

on the closed interval.  At the bolt, putting \(y=x-x_0\),

\[
 F=f_1y+O(y^2),\qquad G=g_1y+O(y^2),\qquad f_1g_1=1,
 \qquad w=O(y^2).
\]

The stored witness has \(f_1=0.9688603622\), \(g_1=1.0321404807\).  These are the standard no-cone bolt relation and the weight-four anisotropy condition for the \(s_1\)-collapsing slot.  The peer independently checked
\(F=G=w=0\), \(F'G'=1\), \(w'=0\) at the bolt.

The implemented factors `(1-u)^3` imply exact agreement of values and first two \(x\)-derivatives with the complex-hyperbolic profile at \(x=X\).  It is therefore a \(C^2\) metric after direct attachment to an exact collar, with zero curvature jump but not yet literally \(C^\infty\).  The Step-7 cutoff lemma applies: because the deviations vanish to third order at the attachment, replacing them by a flat cutoff in a collar of width \(\delta\) changes \(P\) and \(J_6\) by \(O(\delta^3)\) for this fixed witness.  Since the computed deficit is fixed, a sufficiently small \(\delta\) preserves \(J_6<8\pi^2\).  A quantitative derivative bound for a specified cutoff remains to be written if a fully explicit margin is desired.

Positivity is actually analytic, not merely sampled.  The smoothstep satisfies \(0\le S(u)\le1\), and the profile formula gives
\[
 F=(x-x_0)e^{q_F}+x_0S(u)>0,
 \qquad
 G=[(x-x_0)+(x^2+x_0)S(u)]e^{q_G}>0
\]
for \(x_0<x\le X\), while \(h_2=x>0\) and \(h_3=xe^w>0\).  The 20,001-point values
\[
 \min\frac{F}{x-x_0}=0.9661766585,
 \qquad
 \min\frac{G}{x-x_0}=1.0321421993
\]
are useful conditioning measurements, not the proof.  An Arb subdivision attempt also enclosed positive normalized \(F,G\), but the direct raw spin interval integrand suffered severe dependency inflation and did not enclose the energy sharply.  The files `workspace/scripts/perp_interval_certificate.py`, `perp_ball_integrate_fast.py`, and `workspace/data/perp_collar/interval_*` record this unsuccessful route; none is a valid energy certificate.

## 4. Mechanism, not just the total

The exact relative calibration gives

\[
 \frac{P}{8\pi^2}-1=S_1+S_2+S_3+C_3.
\]

For the \(X=8\) witness,

\[
 (S_1,S_2,S_3)=(0.0015972917,0.0005224470,0.0010902866),
 \qquad C_3=-0.0041013225.
\]

Only about \(1.14\times10^{-6}\) of the cubic integral is positive.  Hence the cubic compensation exceeds the three flow squares by \(8.91\times10^{-4}\); the scalar square adds only \(7.54\times10^{-6}\).  A 20,001-point mechanism run shows that the relative-plus-scalar density is negative over much of \(0.016\lesssim u\lesssim0.835\).  Contributions over the five logarithmic ranges are approximately

\[
(-8.65,-77.78,-77.39,+48.45,+27.00)\times10^{-5}
\]

for \(u\in(0,.1),(.1,.3),(.3,.6),(.6,.9),(.9,1)\).  The cumulative deficit reaches \(-1.91\times10^{-3}\) near \(u=.513\), and part is paid back before the collar, leaving \(-8.84\times10^{-4}\).  This is a finite-scale core-to-background interaction, not an AE shrinking-core effect.

The Step-8 continuation task adds corroboration.  At \(X=8\), subthreshold values occur for \(x_0=.003,.01,.03\), though the \(x_0=.001\) J-target restart remained slightly above one.  At \(x_0=.01\), the degree-12 restart stays below one, and \(X=16,32\) remain below one.  These runs support a basin, but the theorem needs only one fixed witness.

## 5. Global transfer on a suitably chosen balanced sequence

I54 §2 proves for one blow-up cell of cost \(J_1\), with the handle surgeries made by the standard shrinking construction,

\[
 \limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}
 \le \frac{28}{9}+\frac{J_1}{9\pi^2}.
\]

Writing \(J_1=8\pi^2(1-\varepsilon_0)\), this is

\[
 \limsup\frac{\alpha(M_j)}{h_j}
 \le4-\frac{8\varepsilon_0}{9}.
\]

For the numerical \(X=8\) witness, \(\varepsilon_0\approx8.83757\times10^{-4}\), so the indicated coefficient is approximately

\[
 3.9992144389.
\]

The large fixed ball does not require a uniform injectivity-radius theorem for arbitrary covers.  Let \(p\in\mathbb{CH}^2\) and choose a buffered radius \(r\) containing the fixed cell and smoothing collar.  Only finitely many nonidentity lattice elements satisfy \(d(p,\gamma p)\le2r\).  Residual finiteness supplies a finite-index subgroup avoiding this finite set, hence a compact finite cover \(X_*\) with the required embedded ball.  Taking further covers inside this subgroup produces disjoint lifts with number proportional to the degree, hence proportional to \(A_j\).  Since the balanced family uses only \(Q_j=o(A_j)\) surgeries and only \(k_j\sim(2/9)Q_j\) copies of this one-blowup cell, the selected large-ball lifts suffice.  A subsequence can still be chosen with \(A_j\ge j^4\), exactly as in the inherited residual-finiteness construction.  This proves availability for an existential balanced sequence; it does not retrofit every previously fixed cover sequence.

The radial relation in the peer coordinates is \(r_{-6}=\operatorname{arsinh}\sqrt X\); after scaling to `Ric=-g`, \(r_{-1}=\sqrt6\,r_{-6}\).  At \(X=8\), \(r_{-1}\approx4.32\), plus a fixed smoothing buffer.

## 6. What is and is not established

The following parts are now independently supported:

* exact algebraic identities for \(P\), \(J_6\), and the relative calibration;
* two independent numerical reconstructions of the frozen profile;
* positive metric analytically from the profile formula, with a wide sampled conditioning margin;
* exact bolt jets and second-jet CH matching;
* a qualitative smooth-collar perturbation preserving a strict gap;
* the residual-finiteness large-ball supply and I54 transfer formula.

The missing part for a fully rigorous explicit upper witness is a sharp validated enclosure of the frozen integral together with positivity on the whole interval and a numerical bound for the chosen smoothing cutoff.  The first Arb implementation exposed the difficulty: raw spin variables near the bolt contain cancelling terms and interval dependency grows catastrophically.  The next verified route should use analytic bolt Taylor series on a short initial interval and a compiled Arb/MPFI evaluator of the already simplified relative density on the remainder, or exact rational-polynomial bounds after replacing exponentials by Taylor models.  The available floating margin is \(8.84\times10^{-4}\) at \(X=8\), or \(1.10\times10^{-3}\) at \(X=16\).

Accordingly, O11 has not yet been declared solved in this note.  The evidence has, however, changed its likely answer: the universal coefficient four is now threatened by an explicit finite-scale perpendicular cell, while all earlier AE and shrinking-core lower mechanisms can remain valid in their stated regimes.
