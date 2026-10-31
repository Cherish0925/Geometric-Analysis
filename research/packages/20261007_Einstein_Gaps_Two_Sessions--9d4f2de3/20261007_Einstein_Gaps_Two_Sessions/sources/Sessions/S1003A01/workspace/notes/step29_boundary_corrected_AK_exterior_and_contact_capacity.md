# Step 29 — Boundary-corrected AK exterior response and nonlinear contact constraints

## 1. Scope and purpose

The object remains the unrestricted Einstein-gap problem, with the certified perpendicular cell providing an actual closed-family upper construction rather than a substitute for the all-metric problem. This note resolves a mathematical dependency between two representations of the same diagonal exterior response:

* the raw antisymmetric complex-hyperbolic (CH) Ricci action from Step 19;
* the local almost-Kähler (AK) action from Step 28.

It also tests the nonlinear contact-closure constraint on actual low-cost profiles. The capacity numbers below are frozen-profile computations and are not asserted uniformly over all diagonal cells, still less over all metrics.

Normalization: \(\operatorname{Ric}_{CH}=-6g\), \(\widehat P=P/(8\pi^2)\), and \(Wdt\) is the normalized volume density.

## 2. Full local identity with interface flux

Let
\[
\mathcal F=4\mathcal P\cosh q-\mathcal P\mathcal P_{TT}-\frac12\mathcal P_T^2
\]
be the Chern–Stokes bracket of Step 28, and let \(L_{AK}\) denote the complete all-scalar Theorem-A density
\[
L_{AK}=12W\left(u^2+\frac{s}{24}\right)^2+6Wu'^2
 +\frac32\delta^2\,d\widehat V/dt+2\lambda^2\,d\widehat V/dt
 -6\nu^2\,d\widehat V/dt.
\]
The local relation is
\[
\boxed{\widehat P[t_0,t_1]=\int_{t_0}^{t_1}L_{AK}\,dt+B(t_1)-B(t_0)},
\]
\[
\boxed{B=b_+-3\mathcal F-9\mathcal P^2-6Wuu'},
\]
where the prime on \(u\) is the original arclength derivative. The smooth perpendicular bolt has \(B\to1\); exact CH has \(B=2\). Hence the whole-cell formula gives \(\widehat P=1+\int L_{AK}\), but on a terminal interval ending in CH,
\[
\boxed{\int_{\rm tail}L_{AK}=\widehat P_{\rm tail}+B(\text{entry})-2.}
\]
The AK tail integral is therefore not the raw tail Ricci action.

`scripts/step29_local_AK_flux.py` evaluates every term directly on the \(x_0=.038,X=128\) optimized cell. At the exact collar it finds \(B=2-5.8\times10^{-11}\). For entries \(x=.1,.2,.5,1,2,5,10,20,50\), the local identity residual is \(5.4\times10^{-11}\)–\(6.3\times10^{-11}\). Representative tail data are:

| entry \(x\) | raw \(\widehat P_{tail}\) | \(\int L_{AK}\) | \(B(entry)-2\) |
|---:|---:|---:|---:|
| 0.5 | 0.01636263 | 0.01195842 | -0.00440421 |
| 2 | 0.00230694 | 0.00365499 | +0.00134805 |
| 5 | 0.00050020 | 0.00599201 | +0.00549181 |
| 10 | 0.00015309 | 0.00450865 | +0.00435556 |
| 20 | 0.00007147 | 0.00222222 | +0.00215075 |

At \(x=10\), more than 96% of the positive AK tail number is the interface conversion: the raw action is \(1.53\times10^{-4}\), whereas \(B(entry)-2=4.36\times10^{-3}\). Adding the AK tail number to the Step-19 exterior response would therefore duplicate the same quantity at incompatible splittings.

Artifact: `data/step29/local_AK_flux_x0038_X128.json`.

## 3. Exact linear CH bridge

Use the exact Step-19 antisymmetric variables
\[
q=\theta,\qquad v_-=f_-w,\qquad
f_-=\frac{x}{(1+x)^{5/2}},\qquad
(k\theta)'=\frac12f_-^2w,
\quad k=\left(\frac{x}{1+x}\right)^2.
\]
On CH the AK variables are
\[
\boxed{\nu=-\frac{v_-}{2\sqrt x}=-\frac{\sqrt x}{2(1+x)^{5/2}}w},
\]
\[
\boxed{\lambda=-\frac{x(1+x)w'+(2-3x)w}{2(1+x)^3}}.
\]
Direct symbolic expansion (`scripts/step29_ak_exterior_bridge.py`) gives the exact identity
\[
\boxed{
\frac{x}{2}(2\lambda^2-6\nu^2)
=\mu(w')^2+\frac{d}{dx}\bigl(A(x)w^2\bigr),
}
\]
where
\[
\mu=\frac{x^3}{4(1+x)^4},\qquad
\boxed{A(x)=-\frac{x^2(3x-2)}{4(1+x)^5}}.
\]
The symbolic residual is zero. This is the linearized form of the full \(B\)-conversion.

The Step-19 exterior functional is exactly
\[
E_{ext}=\int_\rho^\infty\mu(w')^2dx=\frac{\delta^2}{I(\rho)},
\qquad
\delta=-2k(\rho)\Theta-w_0G(\rho),
\]
with its existing mass null line \(\delta=0\). Thus the AK expression induces no second positive tail response:
\[
\int_\rho^\infty L_{AK}^{(2)}dx=E_{ext}-A(\rho)w_0^2.
\]
For the exact outgoing Einstein mass mode \(w\equiv1\), raw action is zero but at \(\rho=10\)
\[
\int_{10}^\infty L_{AK}^{(2)}dx=-A(10)=0.004346449261414086,
\]
which is canceled exactly by the entrance flux \(A(10)=-0.004346449261414086\). This supplies the required Einstein benchmark and preserves the same mass null direction.

On the nonlinear \(x_0=.038,X=128\) profile beyond \(\rho=10\), reconstructing \(w\) and evaluating the **CH quadratic bridge** gives:

* reconstructed CH-quadratic raw tail: \(1.47497210\times10^{-4}\);
* reconstructed CH-quadratic AK tail: \(4.56894793\times10^{-3}\);
* interface change: \(4.42145057\times10^{-3}\);
* bridge residual: \(1.49\times10^{-10}\).

These are not the exact nonlinear values in §2; the differences are finite nonlinear/off-CH corrections (the exact nonlinear raw tail at \(x=10\) is \(1.53090270\times10^{-4}\), and the exact nonlinear AK tail is \(4.50865207\times10^{-3}\)). For the same entrance trace, the exact finite-\(X\) Step-19 quadratic minimizer has raw cost \(1.435700999\times10^{-4}\), giving boundary-converted quadratic AK value \(4.565020671\times10^{-3}\), within \(3.93\times10^{-6}\) of the reconstructed profile's quadratic AK value. The mismatch measures that the optimized finite tail is close to, but not exactly, the frozen-trace linear minimizer; it is not a missing positive action.

Artifact: `data/step29/ak_exterior_bridge_x0038_X128_rho10.json`.

## 4. Contact closure is the old torsion/reconstruction relation

Set \(y=\tanh(q/2)\). The definition of \(\nu\) gives
\[
\boxed{y_T+\frac4{A_f}y=-\nu(1-y^2)}.
\]
With \(\eta_T=4\eta/A_f\),
\[
(\eta y)_T=-\eta\nu(1-y^2).
\]
On the linear CH tail, \(y=q/2+O(q^3)\), \(\eta\) is proportional to the existing contact integrating factor \(k=(x/(1+x))^2\), and \(\nu=-v_-/(2\sqrt x)\). Therefore this relation is the Step-19 torsion equation \((k\theta)'=f_-v_-/2\) in AK variables, not a new independent terminal condition.

`scripts/step29_capacity_contact.py` verifies the nonlinear contact equation on the actual \(x_0=.015,.038,.07\) profiles, with maximum bulk residual \(0.6\times10^{-6}\)–\(1.3\times10^{-6}\), and confirms a sign change of \(\nu\) in all three. The weights, integrating factors, and moments all come from the same metric.

## 5. Frozen-profile transport capacity does not close the lower problem

Put \(h=\mu\nu\), \(\rho=\widehat W/\mu^2\). Then
\[
\frac12Q_A=\frac12\int\rho h_T^2dT.
\]
For each actual profile, I computed:

1. the minimum with the actual endpoint values of \(h\);
2. the minimum after additionally imposing the actual linear contact moment \(\int c(T)h(T)dT\), with \(c=\eta(1-y^2)/\mu\), while freezing \(\rho,c\) from that metric.

| \(x_0\) | observed \(Q_A/2\) | endpoint capacity | endpoint + contact capacity | fractions |
|---:|---:|---:|---:|---:|
| .015 | .0070468 | .0010298 | .0018579 | .146, .264 |
| .038 | .0328566 | .0058549 | .0106619 | .178, .324 |
| .07 | .0801134 | .0167547 | .0311244 | .209, .389 |

The nonlinear contact identity is real and it materially raises the frozen capacity, but even the two-constraint number explains only 26–39% of the observed \(W_3\) transport energy. It is therefore not near saturation and cannot by itself reduce the lower problem to two scalar moments. More importantly, these coefficients are generated by the same metric and have no presently derived uniform comparison over the full diagonal class. The next lower-bound step must retain nonlinear evolution of \((A_f,\mathcal P,q,u)\), or an equivalent full Ricci-control/Hamilton–Jacobi system, with the existing boundary-converted exterior value attached.

Artifacts: `data/step29/capacity_x0015_X256.json`, `capacity_x0038_X128.json`, `capacity_x007_X256.json`.

## 6. Consequences for the construction and global programme

1. **No second tail theory is needed in the antisymmetric sector.** The Step-19 exterior response \(\delta^2/I\), including its Einstein mass null direction, is the correct raw terminal value. The AK tail expression is the same response plus the explicit interface conversion. A matrix Riccati construction that assigns a new positive price to the mass mode would be wrong.
2. **The saving mechanism is genuinely intermediate and nonlinear.** In the far linear CH sector, the AK and raw formulations differ only by flux. The negative net contribution must be produced before this linear response, where bolt-forced nonintegrability, conformal response, contact closure, and terminal trace evolve on one metric.
3. **The interface \(B\) is a useful matching observable.** Unlike the enormous individual CH values of \(b_+\), \(\mathcal F\), and \(9\mathcal P^2\), their combination is exactly 2. It converts local AK decompositions into raw action without cancellation ambiguity at the mathematical level. Numerically the local identity is stable to \(10^{-10}\) on the tested profile.
4. **Applicability beyond one profile.** The full nonlinear \(B\)-identity holds for every smooth diagonal perpendicular exact-CH cell, whereas the explicit \(A(x)w^2\) bridge is its linear CH specialization. The latter can be used at any section where a competitor is quantitatively close to CH. Uniform entry into such a section remains part of the global lower problem.
5. **Construction transfer.** The strict cell saving is already reproducible on suitable CH cover towers through exact collar insertion; the certified theorem-level source remains `data/perp_area/rigorous_x00.03_X128_d20.json`, not the floating \(x_0=.038\) record. The interface analysis explains its exterior compatibility but does not change the certified coefficient \(<3.9961521+\varepsilon\).
6. **Beyond fixed symmetric profiles.** The immediate transferable object is not a numerical capacity weight but the geometric package: a closed self-dual form, its Nijenhuis transport, the conformal selector, and the Chern/interface flux. Extending that package to nonsymmetric cells requires actual existence of the relative self-dual form and treatment of its zero set. The global all-metric O11 lower value, mixed blow-up–handle cells, O10, and fixed-manifold Einstein attainment remain open.

## 7. Independent verification corrections

A two-branch TTCS verification (`trace/ttcs/results/step29_ttcs01_verifier1_integration.md`) re-derived the nonlinear local identity, the linear CH bridge, the mass-null cancellation, and the capacity Euler problem. It found and repaired two presentation issues:

* the correct displayed formula is \(\lambda=-[x(1+x)w'+(2-3x)w]/[2(1+x)^3]\); the original draft had an extra factor of \(x\) in front of \(w'\), while the SymPy script and computed identity already used the correct coefficient;
* the bridge script's profile block evaluates the CH quadratic reconstruction from a nonlinear tail, whereas the exact nonlinear raw and AK tail values are those of `step29_local_AK_flux.py`.

With those corrections, the verifier confirmed that the interface accounts for 96.6% of the exact positive AK tail integral at \(x=10\), that the finite-\(X\) and infinite mass-null responses retain the Step-19 sign conventions, and that the two-constraint capacity formula has the correct Green representer and factor \(1/2\). The corrected note and script labels now distinguish exact nonlinear values from CH-quadratic reconstructions.

## 8. The theorem-level cell obeys the same interface mechanism

The nonlinear local calculation was also run on the actual frozen profile underlying the authoritative Arb enclosure, `data/perp_area/x00.03_X128_d20.json` (whose separate rigorous record gives \(J_6/(8\pi^2)\le0.9956710815089548\)). The interface identity again holds at all nine sections with residuals \(5.0\times10^{-11}\)–\(5.8\times10^{-11}\). At \(x=10\), the exact nonlinear tail values are
\[
\widehat P_{tail}=1.14618031\times10^{-4},\qquad
\int L_{AK}=2.87473373\times10^{-3},\qquad
B(entry)-2=2.76011570\times10^{-3}.
\]
Thus the same geometric conversion is present in the theorem-level realizable construction, not only in the improved floating branch. The new local calculations are ordinary floating checks; the certified global energy remains supplied by `data/perp_area/rigorous_x00.03_X128_d20.json`. Artifacts: `data/step29/local_AK_flux_certified_x003_X128.json` and `ak_exterior_bridge_certified_x003_X128_rho10.json`.

A cutoff-sensitivity check on the \(x_0=.038\) capacity used inner computational parameters \(u_{min}=10^{-4},10^{-5},3\times10^{-6}\). The endpoint-only fractions were \(0.178240,0.178196,0.178193\), and the endpoint-plus-contact fractions were \(0.324581,0.324498,0.324491\). Thus the conclusion that the two frozen constraints account for about 32.45% is stable against the singular-bolt cutoff at the displayed accuracy. Artifacts: `capacity_x0038_X128_eps1e4.json`, `capacity_x0038_X128.json`, `capacity_x0038_X128_eps3e6.json`.
