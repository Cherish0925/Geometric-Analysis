# Step 36 — A realizable perpendicular-core transplant into the Calabi cap

Conventions: closed-family scale `Ric=-g`,
\[
D(g)=\int|\operatorname{Ric}+g|^2,
\qquad P(g)=\int|\operatorname{Ric}^{\circ}|^2,
\qquad D=P+\frac14\int(s+4)^2.
\]
The authoritative CH cell has
\[
D/(8\pi^2)\le 0.995670030355131.
\]
This note records a finite-amplitude construction experiment, not an infimum or lower theorem.

## 1. Corrections to Step 35

Three statements from `step35_cap_transfer_neutrality_and_cap_cells.md` were corrected in that file.

1. The cutoff used in the former Theorem N equals the target Einstein metric only on a smaller outer collar, not on the entire prescribed annulus. It proves an \(O(\varepsilon^2)\) **buffered transfer** for a given competitor; it does not compare the two same-annulus cell infima and does not exclude a first-order environment-adapted response.
2. The positive cap eigenvalue lies in \(R^-\). The glued-Burns first variation uses \(R^+(\hat\zeta,\hat\zeta)\). At the aligned cap direction \(R^+=-1\), so the first-order term is unfavorable. Any toric benefit must be nonlinear or higher order; chirality reversal would be a different signed-surgery problem.
3. The exact ledger
   \[
   b=a+12\pi^2,
   \qquad P=8\pi^2+4a+\frac{\delta S}{12},
   \qquad \delta S=12P+480\pi^2-48b
   \]
   is a payment identity. Because \(\delta S\) is the change in \(\int s^2\), not the nonnegative residual \(\int(s+4)^2\), it does not exclude scalar-moment and volume compensation. The incorrect \(576\pi^2\) inference was removed.

The cap construction remains valuable because it tests a new actual geometry, not because these corrected statements eliminate alternatives.

## 2. Construction

`scripts/step36_cap_perp_transplant.py` transports the certified perpendicular core into the exact universal Calabi cap.

### 2.1 Perpendicular core in a common marking

The stored cell has `Ric=-6g` and radial coordinate \(x\). Scale by six. In the CH exponential marking \(\xi=rv\in\mathbb R^4\),
\[
x=\sinh^2(r/\sqrt6).
\]
If the old diagonal orbit matrix is \(h=\operatorname{diag}(h_1,h_2,h_3)\), its scaled exponential-coordinate eigenvalues are
\[
\frac{x(1+x)}G,
\quad \frac{6h_1}{r^2},
\quad \frac{6h_2}{r^2},
\quad \frac{6h_3}{r^2}
\]
in the radial, perpendicular-bolt, companion, and Hopf directions. This reproduces scaled CH exactly when
\(G=x(1+x)\), \(h=(x,x,x(1+x))\). The bolt and the old core metric are unchanged.

### 2.2 Exact cap in proper normal coordinates

Use divisor coordinates \((X,Y)\) and proper normal polar coordinates \((n,\Psi)\), written Cartesian as \((Z,W)\), \(n^2=Z^2+W^2\). Then
\[
u(n)=\cosh(\sqrt{3/2}\,n)^{2/3},
\qquad q(u)=\frac23(u^2-u^{-1}),
\qquad du/dn=\sqrt q,
\]
and
\[
g_C=u(dX^2+dY^2)+dn^2+q\left(d\Psi+\frac12(XdY-YdX)\right)^2.
\]
The script evaluates the exact Cartesian matrix; its generic coordinate-Ricci routine gives `Ric+g` residuals between \(9\times10^{-16}\) and \(3\times10^{-15}\) at test points.

### 2.3 Full transition and response modes

For \(a<r<b\), put
\[
H(t)=t^4(35-84t+70t^2-20t^3),
\qquad t=\frac{r-a}{b-a},
\]
\[
g_0=(1-H)g_{\rm cell}+Hg_C.
\]
Since \(H' =140t^3(1-t)^3\), \(0\le H\le1\), so the baseline is positive. Three compactly supported modes with
\(F(t)=256t^4(1-t)^4\) vary the interpolation path, conformal scale, and horizontal-normal trace-free splitting:
\[
F(g_C-g_{\rm cell}),\qquad Fg_0,
\qquad \frac F2(g_0S+Sg_0),\quad S=\operatorname{diag}(-1,-1,1,1).
\]
The metric is literally \(C^3\) at the two joins, which is enough for ordinary continuous Ricci curvature; it can be smoothed in thin collars with arbitrarily small change in all reported integrals. It should therefore be called a smoothable trial, not already \(C^\infty\).

The core is integrated in the old exact radial coordinates. The whole transition is integrated by Sobol quadrature in \(\mathbb R^4\), using JAX automatic differentiation of the full coordinate metric and no symmetry formula for Ricci. The exact cap outside contributes zero defect.

## 3. Numerical results

The first pilot used incompatible algebraic radial charts and cost \(12.78\); it was superseded after both geometries were placed in the markings above (`data/step36_cap_perp_pilot.json` is retained only as a failed attempt).

### 3.1 Baseline scans

`data/step36/cap_perp_baseline_scan.json` and `cap_perp_width_scan.json` scan several \((a,b)\). The best tested pair was \((0.5,1.5)\):
\[
D/(8\pi^2)=2.44057,
\qquad P/(8\pi^2)=1.68279.
\]
The core to \(a=0.5\), where \(x_a=0.0422486\), contributes only
\[
D_{\rm core}/(8\pi^2)=0.459454,
\]
while the transition contributes \(1.98112\). Wider or later transitions were more expensive. For example \((a,b)=(0.6,1.8)\) gives \(D/(8\pi^2)\simeq3.09\), while \((1.2,2.1)\) gives about \(23.9\). The large growth means that this radial identification accumulates substantial profile/marking mismatch when it is extended farther out.

### 3.2 Three-mode response

The three response coefficients were fitted on 128 fixed Sobol points at \((a,b)=(0.5,1.5)\):
\[
(c_0,c_1,c_2)=(0.1122072,-0.0048520,-0.0118740).
\]
The in-sample value \(2.20827\) is optimistic. On three independent 512-point samples (`cap_perp_response_validation.json`),
\[
D/(8\pi^2)=2.25792,\ 2.26806,\ 2.26950,
\]
with mean \(2.26516\). The minimum sampled coordinate eigenvalue is \(0.272\)--\(0.279\), so positivity is numerically strong but not certified over the full annulus. The response recovers roughly \(0.18\) from the baseline but leaves the transition dominant.

At validation seed 1,
\[
P/(8\pi^2)=1.57336,
\quad \delta V=-1.06969,
\quad a/(8\pi^2)=0.07113,
\quad b/(8\pi^2)=1.57113.
\]
The ledger values are reconstructed from relative Chern--Weil; `b-a=12pi^2` is therefore automatic rather than an independent numerical check.

### 3.3 Same-pipeline CH control

The identical core truncation, interpolation, quadrature, and response family were rerun with exact CH as the outer metric (`ch_perp_same_pipeline.json`, `ch_perp_response_validation.json`). At \((0.5,1.5)\), the baseline gives
\[
D_{\rm CH-control}/(8\pi^2)=1.581\text{--}1.589,
\]
and independently validated response coefficients give
\[
D_{\rm CH-control}/(8\pi^2)=1.534,\ 1.541.
\]
Thus about \(0.73\) of the optimized cap trial's normalized cost is cap-specific within this same radial three-mode pipeline, but about \(0.54\) above the certified threshold is already caused by truncating the successful cell at \(a=0.5\) and rebuilding its long optimal CH transition with only three modes. The experiment therefore separates two effects:

- the chosen radial cap identification is genuinely costly relative to the CH control;
- the trial space is too thin even to recover the known CH construction.

It would be wrong to interpret \(2.265\) as the cap-cell infimum, or the cap--CH difference as an intrinsic invariant of the cap.

## 4. Verification and interpretation

TTCS independently checked the scaling, exponential CH reconstruction, exact cap Cartesian matrix, Ricci and norm contractions, shell Jacobian, core/annulus matching, scalar moments, and ledger in `trace/ttcs/results/step36_ttcs01_verifier1_integration.md`. No normalization error capable of moving the values near one was found. It identified the \(C^3\) versus \(C^\infty\) point, sampled rather than uniform positivity, the automatic ledger check, and the need for the same-pipeline CH control; the first three are recorded above and the CH control was then computed.

The result changes the constructive judgment without excluding cap benefit. A direct radial transplant of an early perpendicular core into the cap is a poor construction. The cost is generated mainly in the transition and, after subtraction of the CH control, remains substantially cap-dependent. The positive \(R^-\) eigenvalue does not automatically rescue this metric. But the control also shows that most of the successful CH transition has been thrown away: the certified cell is exact CH only at physical radius about \(7.65\), while the trial cuts it at \(0.5\) and reaches the cap by \(1.5\). Richer \(U(1)_-\) modes, an optimized diffeomorphism/marking, a cap-adapted core, or a matched short-collar solution remain open and could change the sign.

The next constructive step should therefore optimize the **transition itself** in the common cap chart and demand simultaneous success on the CH control. A useful response family must first reduce the CH control from \(1.54\) toward the known \(0.99567\); only then does its cap--CH comparison isolate the nonlinear \(W^-\) response rather than lack of representation. A toric non-Kähler trial remains complementary, but the cap's \(R^-\) sign supplies no favorable aligned first-order prediction.

## 5. Analytic cap transfer

The external regularity source is now registered: Tosatti--Wang--Weinkove--Yang prove a local \(C^{2,\alpha}\) estimate for equations \(F(S+T(D^2u,x),x)=f\) under uniform ellipticity, concavity, Hölder coefficients and source, a matrix-range condition, and an \(L^\infty\) bound on \(u\) \cite{tosatti2015alpha}. Their complex Monge--Ampère application uses the \(J\)-invariant projection of the real Hessian; it does not assume a bound on the full real Hessian. This supports Step 35's local derivative upgrade only after verifying uniformly, on the reciprocal-angle lifted charts, the chart size, smooth reference coefficients, potential normalization/oscillation, ellipticity, and source Hölder bounds. Biquard--Guenancia's ratio-one metric comparison supplies the complex-Hessian range and ellipticity. The remaining uniform-potential normalization and chart-constant bookkeeping should be written explicitly before Theorem T is quoted in a final theorem.

Wolfram was checked again and is unavailable because the local Engine license has expired; the exact and automatic-differentiation work used SymPy/JAX.
