# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 14,
  "task_field": "verifier",
  "task_index": 3,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step14_ttcs01_sub5_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step14_ttcs01_sub6_verifier.md"
    }
  ]
}
```

## Exact Task

Critically read the empirical comparison between the certified X=8 subthreshold cell and the Einstein bolt flow. The profile reconstructs geodesic state, estimates a bolt anisotropy d_fit≈-0.462, and shows the same-bolt Einstein trajectory becomes singular at t≈0.297 while 99% of the positive P action of the cell is accumulated by t≈0.319 (90% by t≈0.150). State what scientific conclusion about the 'shadow Einstein separatrix then pay a late CR layer' picture is warranted. Check slot/sign conventions and whether d_fit instability invalidates the comparison. Relate this to the exact control-action identity shared by the peer: P/(8π²)=∫Σ λ_i/4 (u_i'−2H_i/λ_i)^2 dt. Suggest the strongest next mathematical object this evidence supports: local bolt action/calibration, compactness contradiction, or another formulation.

## Integrated Scientific Memo

## Scientific verdict

The \(X=8,\ b=0.1\) cell does **not** support the literal picture

> “shadow the relevant Einstein separatrix for a long time, then pay most of the cost in a late CR-correction layer.”

What is supported is more limited and essentially opposite in localization:

1. The positive action
   \[
   \frac{P}{8\pi^2}
   =\int \sum_i\frac{\lambda_i}{4}
   \left(u_i'-\frac{2H_i}{\lambda_i}\right)^2dt
   \]
   is overwhelmingly a **bolt-core cost**:
   \[
   t_{50}=0.0649,\quad t_{75}=0.1009,\quad
   t_{90}=0.1496,\quad t_{99}=0.3191,
   \]
   whereas \(t_{\rm outer}=1.7547\). Thus only about \(1\%\) of the positive action lies beyond \(t=0.319\). There is no substantial late outer-collar payment.

2. The particular Einstein trajectory used for comparison cannot be shadowed for long: its numerical integration stops at \(t=0.29714\), while the cell continues smoothly to the CH collar.

3. More importantly, this trajectory is not an identified ACH separatrix. Step 13 reports that at \(b=0.1<0.29\) the AH/singular transition no longer approaches the perpendicular ACH fixed point. Hence this experiment does not directly test shadowing of the genuine Einstein ACH separatrix relevant to the Rossi-to-standard-CR mismatch.

The defensible interpretation is therefore:

> The cell pays nearly all of its trace-free Ricci control action in the small bolt-scale core, thereby following a non-Einstein, approximately Burns-type bubble rather than the displayed Ric\(=-6\) orbit; after entering a CH-directed state, it reaches the exact CH collar with very little additional positive action.

This rules out the **late-payment** version of the proposed mechanism for this cell. It does not rule out separatrix shadowing for larger bolts \(b\gtrsim0.29\), where an actual perpendicular ACH Einstein separatrix exists.

## Why the displayed orbit is not a matched Einstein continuation

The comparison matches only:

- bolt radius \(b=0.1\),
- normal charge \(n=1\),
- fourth-order anisotropy \(d\).

It does **not** match the full bolt jet. Let
\[
A=G'(x_0)=e^{-\sum_k c_{F,k}(-1)^k}\simeq1.03214.
\]
The cell has
\[
a_1=a_2=b+\frac{A}{2b}t^2+O(t^4),
\qquad
p_{2,\mathrm{cell}}\simeq5.1607.
\]
The Ric\(=-6\) Einstein bolt equations instead force
\[
p_{2,E}=\frac{3b^2+2}{2b}=10.15.
\]
Thus the flows already differ at order \(t^2\), before the anisotropy \(d\,t^4\) enters. This explains why the axes are initially close while the recorded \(y\)-distance is already \(3.59\) at \(t\simeq0.0204\), and why by \(t\simeq0.1\) the log-axis distance is \(0.484\).

Consequently, “same bolt jet” is too strong: this is a comparison with the Einstein solution having the same \((b,n,d)\), not with an Einstein evolution initialized from the cell’s complete state.

The finite integration endpoint also needs care. Since `solve_ivp` returns `status=-1` at \(t=0.297137\), all plotted Einstein values after that time are dense-output extrapolations, not values of a computed solution. The \(10^{105}\), infinities, and NaNs at \(t\ge0.4\) have no geometric content. The data establish solver termination near \(0.297\); certifying a curvature singularity from this run alone would additionally require terminal axis/curvature blow-up and constraint control.

## Slot and sign conventions

The conventions in the scripts are consistent:

\[
(a_1,a_2,a_3)=\bigl(\sqrt{x},\sqrt{x e^w},\sqrt F\bigr).
\]

- \(a_3\) collapses at the bolt, so the bolt fibre is slot \(3\).
- At the exact CH collar,
  \[
  (a_1,a_2,a_3)=\bigl(\sqrt{x},\sqrt{x(1+x)},\sqrt{x}\bigr),
  \]
  so the fast/Kähler direction is slot \(2\).
- Accordingly,
  \[
  \kappa_2=\frac{a_2}{a_3a_1},\qquad
  \rho_2=\frac{a_3}{a_1}
  \]
  are the correct ACH\(_2\) variables.
- Near the bolt \(w>0\), hence \(a_2>a_1\), so
  \[
  a_1-a_2=d\,t^4+\cdots
  \]
  has \(d<0\), as found. Interchanging slots \(1\) and \(2\) reverses the sign of \(d\) and exchanges the corresponding perpendicular ACH branches.

The nonzero “ACH deviation” \(0.0859\) at \(X=8\) is not a CR mismatch: even exact finite-radius CH has exponentially decaying finite-\(t\) corrections. In particular, \(\rho_2=1\) there is the relevant standard-CR datum.

## Does instability of \(d_{\rm fit}\) invalidate the comparison?

No, but it limits what can be inferred about the precise Einstein exit time.

The fitted coefficient can be obtained directly from the endpoint jet. Put
\[
C_w=\sum_k c_{w,k}(-1)^k,\qquad
\ell=\log(X/x_0),\qquad A=G'(x_0).
\]
Since the smooth collar interpolation starts at higher order and
\[
x-x_0=A t^2+O(t^4),\qquad
w=\frac{C_wA^2}{x_0^2\ell^2}t^4+O(t^6),
\]
one obtains
\[
d_{\rm jet}
=-\frac{b\,C_wA^2}{2x_0^2\ell^2}
=-\frac{C_wA^2}{2b^3\ell^2}
\simeq-0.4621.
\]
This agrees with \(d_{\rm fit}=-0.462267\) at roughly \(4\times10^{-4}\) relative error. The large coefficients in the polynomial fit reflect higher-order terms over the finite fitting window, not a sign or slot error.

There is nevertheless genuine sensitivity: \(C_w\) is a cancellation among larger stored coefficients, and an unstable Einstein orbit can have an exit time highly sensitive to \(d\). Therefore \(t\simeq0.297\) should be rechecked using the exact endpoint jet and nearby \(d\)-intervals if its numerical value matters. But this does not repair shadowing: the dominant second-order mismatch \(p_{2,\mathrm{cell}}\ne p_{2,E}\), the early action concentration, and the absence of an ACH separatrix at \(b=0.1\) are insensitive to such a small change in \(d\).

## Control-action interpretation

Writing
\[
r_i=u_i'-\frac{2H_i}{\lambda_i},
\]
the exact identity turns the profile equations into a weighted control problem:
\[
a_i'=u_i+K_i(a),\qquad
u_i'=\frac{2H_i}{\lambda_i}+r_i,
\qquad
\frac{P}{8\pi^2}
=\int\frac14\sum_i\lambda_i r_i^2\,dt.
\]
The measured quantiles say that the control \(r\) is expended mainly on the bolt scale, not near the remote CR collar.

For orientation, the Burns profile
\[
a_1=a_2=\sqrt{t^2+x_0},\qquad a_3=t
\]
has
\[
u_1=u_2=0,\qquad u_3=-\frac{x_0}{t^2+x_0},
\]
and the identity gives
\[
\frac{1}{8\pi^2}\frac{dP_{\rm Burns}}{dt}
=\frac{4x_0^2t}{(t^2+x_0)^3},\qquad
\frac{P_{\rm Burns}([0,T])}{8\pi^2}
=1-\frac{x_0^2}{(T^2+x_0)^2}.
\]
Its predicted cumulative fractions agree closely with the recorded cell quantiles. Thus the plot predominantly resolves the approximately \(8\pi^2\) Burns bubble cost. It does **not** resolve the much smaller subthreshold gain
\[
1-\frac{P}{8\pi^2}\simeq 8.9\times10^{-4},
\]
so one should not infer from the cumulative positive-density plot where that saving is produced. Locating the saving requires plotting the difference from the Burns density and, preferably, the completed-square and cubic terms separately.

Also, zero \(P\)-control means trace-free Ricci vanishes, hence “Einstein” with an a priori variable Einstein constant. Ric\(=-6\) is selected by the CH normalization or by including the scalar-error term in \(J\). This distinction must be retained in a pure-\(P\) control theorem.

## Strongest next mathematical object

The evidence most directly supports a **local bolt-scale weighted action/calibration**, not yet a global compactness contradiction. A natural value function is
\[
\mathcal I_{\rm core}
=
\inf\left\{
\int_0^\tau\frac14\sum_i\lambda_i r_i^2\,dt:
\text{regular }O(-1)\text{ bolt data evolve to a CH-directed transverse section}
\right\}.
\]
A calibration \(\Phi(a,u)\) satisfying the Hamilton–Jacobi subsolution inequality
\[
F\!\cdot\nabla\Phi+
\sum_i\frac{(\partial_{u_i}\Phi)^2}{\lambda_i}\le0
\]
would imply, by completing the square,
\[
\Phi(z(\tau))-\Phi(z(0))
\le
\int_0^\tau\frac14\sum_i\lambda_i r_i^2\,dt.
\]
This formulation directly measures the weighted action needed to escape the bolt-side zero-control dynamics and enter the low-cost CH basin.

For this small-\(b\) cell, an even sharper version is a **Burns-centered local calibration/small-b expansion**. The independent completion encoded in `density_x` gives
\[
\frac{P}{8\pi^2}
=
1+S_1+S_2+S_3
+\int\frac{2u_1u_2u_3}{\lambda_2}\,dt,
\]
with \(S_i\ge0\). The unit term is the bolt/Burns cost; only the cubic perpendicular interaction can lower the action below \(1\). Linearizing around the Burns core and minimizing the quadratic squares against this cubic term is the natural route to
\[
\inf\frac{P_{\rm cell}(b)}{8\pi^2}
=1-c\,b^4+o(b^4),
\]
with the observed record suggesting \(c\approx9\), but not yet proving it.

A compactness contradiction remains important for a global positive gap, but the present single \(b=0.1\) comparison does not supply the uniform ingredients needed for it: control over varying \(b,d\), the bolt-degenerate weights \(\lambda_i\), the Einstein constant, and the location of defect as the outer radius diverges. The local Burns/bolt calibration is therefore the strongest object genuinely supported by these data. For testing the original Einstein-separatrix/CR-bending scenario itself, analogous optimized cells should instead be compared at \(b\gtrsim0.29\) with the actual tuned separatrix \(d_*(b)\), not with a same-\(d\) singular orbit.