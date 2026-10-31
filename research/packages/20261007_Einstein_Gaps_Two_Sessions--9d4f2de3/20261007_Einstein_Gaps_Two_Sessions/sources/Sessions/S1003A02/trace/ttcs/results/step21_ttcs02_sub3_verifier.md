# TTCS Independent Branch Record

```json
{
  "step_id": 21,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/h4_cell_channel_analysis.py",
    "Sessions/S1003A02/workspace/data/h4_cell_channels.json",
    "Sessions/S1003A01/workspace/scripts/h4_perp_cell.py",
    "Sessions/S1003A01/workspace/notes/step18_corrected_riccati_and_H4_comparison.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md"
  ]
}
```

## Task

Check the hyperbolic-cell channel identities and numerical interpretation. The normalization is Ric=-6, scalar -24, sectional curvature -2. Verify algebraically that for an exact-H4-collar one-blow-up cell, P/(8pi^2)-1 = 4 int W+^2/(8pi^2) + [int s^2/12 - 48 Vol(B)]/(8pi^2), and J/(8pi^2)-1 = that Weyl term + int(s+18)^2/3/(8pi^2) + [36 Vol(U)-48 Vol(B)]/(8pi^2). Read the script/data and assess whether the reported X=64 cells support the claim that no volume-saving/scalar-near--18 mechanism appears in the tested diagonal family. Identify any normalization or volume-factor error.

## Output

## Scientific verification memo

### 1. Relative Chern–Weil identity

Let
\[
A_\pm(U)=\int_U |W^\pm|^2\,dV,\qquad
S(U)=\int_U s^2\,dV,\qquad P(U)=\int_U|\Ric^\circ|^2\,dV.
\]
Use the orientation in which the exceptional sphere has self-intersection \(-1\). For a one-blow-up cell \(U\) relative to the four-ball \(B\),
\[
\Delta\chi=1,\qquad \Delta\tau=-1.
\]
Because the outer H4 germs agree, the outer Chern–Simons transgressions cancel after subtracting the formulas for \(U\) and \(B\). Thus
\[
8\pi^2\Delta\chi
 =\Delta\!\left(A_++A_--\frac12P+\frac1{24}S\right),
\]
\[
12\pi^2\Delta\tau=\Delta(A_+-A_-).
\]
Eliminating \(A_-\) gives
\[
\Delta P
 =4\Delta A_+ +\frac1{12}\Delta S
 -8\pi^2(2\Delta\chi+3\Delta\tau).
\]
Here
\[
2\Delta\chi+3\Delta\tau=2-3=-1.
\]
The comparison ball has constant sectional curvature \(-2\), hence
\[
W^\pm_B=0,\qquad \Ric^\circ_B=0,\qquad s_B=-24,
\qquad \frac{s_B^2}{12}=48.
\]
Therefore
\[
P(U)=8\pi^2+4A_+(U)+\int_U\frac{s^2}{12}\,dV-48\Vol(B),
\]
or
\[
\boxed{
\frac{P(U)}{8\pi^2}-1
=
4\frac{\int_U|W^+|^2\,dV}{8\pi^2}
+
\frac{\displaystyle\int_U\frac{s^2}{12}\,dV-48\Vol(B)}
     {8\pi^2}.}
\]
This is algebraically correct under the endomorphism norm convention for \(W^\pm:\Lambda^\pm\to\Lambda^\pm\).

### 2. The \(J\) identity and the appearance of \(-18\)

For the Einstein target \(\Ric=-6g\),
\[
J(U)=\int_U|\Ric+6g|^2\,dV
=P(U)+\frac14\int_U(s+24)^2\,dV.
\]
The scalar polynomial identity is
\[
\frac{s^2}{12}+\frac{(s+24)^2}{4}
=
\frac{(s+18)^2}{3}+36.
\]
Adding the \(J-P\) term to the preceding Chern–Weil formula therefore yields
\[
\boxed{
\frac{J(U)}{8\pi^2}-1
=
4\frac{\int_U|W^+|^2\,dV}{8\pi^2}
+
\frac{\displaystyle\int_U\frac{(s+18)^2}{3}\,dV}{8\pi^2}
+
\frac{36\Vol(U)-48\Vol(B)}{8\pi^2}.}
\]
Thus \(-18\) is produced by completing the square; it is not the Einstein scalar target, which remains \(-24\).

---

### 3. Volume normalization in the scripts

For
\[
g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2,
\qquad \int_{S^3}\sigma_1\sigma_2\sigma_3=2\pi^2,
\]
the radial length factor is \(dx/(2\sqrt G)\), while
\[
abc=\sqrt F\,\sqrt x\,\sqrt{xe^w}
=\sqrt F\,x\,e^{w/2}.
\]
After orbit integration,
\[
dV=\pi^2\frac{\sqrt F\,x\,e^{w/2}}{\sqrt G}\,dx,
\]
so
\[
\boxed{\frac{dV}{8\pi^2}
=\frac{\sqrt F\,x\,e^{w/2}}{8\sqrt G}\,dx.}
\]
This is exactly the active expression in `h4_cell_channel_analysis.py`:
```python
v8 = sqrt(F)*xx*exp(w/2)/(8*sqrt(G))
```
with `dx` already carrying the Gauss quadrature form of the coordinate differential.

For the H4 ball,
\[
F=x,\qquad G=x+2x^2=x(1+2x),\qquad w=0,
\]
hence
\[
\frac{dV_B}{8\pi^2}=\frac{x}{8\sqrt{1+2x}}\,dx.
\]
Writing \(y=\sqrt{1+2X}\),
\[
\frac{\Vol(B_X)}{8\pi^2}
=\int_0^X\frac{x}{8\sqrt{1+2x}}\,dx
=\frac{y^3}{48}-\frac y{16}+\frac1{24},
\]
which agrees with `h4_ball_volume_norm`.

The normalizations in `h4_perp_cell.py` are also consistent:

- `PD = vol*ric0/4` integrates to \(P/(8\pi^2)\);
- `SD = vol*(s+24)^2/16` integrates to
  \[
  \frac1{8\pi^2}\frac14\int(s+24)^2\,dV.
  \]

I find no factor-of-two, \(8\pi^2\), or radial-volume discrepancy in the active computation. The unused `vol_density=...*0` line has no numerical effect.

---

### 4. What the \(X=64\) data show

Define the combined non-Weyl \(J\)-channel
\[
C_J=
\frac{\displaystyle\int_U\frac{(s+18)^2}{3}\,dV
      +36\Vol(U)-48\Vol(B)}
     {8\pi^2}.
\]
For the three degree-16, \(P\)-targeted \(X=64\) profiles:

| \(x_0\) | \(\Vol(U)/\Vol(B)-1\) | mean \(s\) | RMS \(s+18\) | \(C_J\) | \(4\int|W^+|^2/(8\pi^2)\) | \(J/(8\pi^2)-1\) |
|---:|---:|---:|---:|---:|---:|---:|
| .003 | \(1.6774\times10^{-5}\) | \(-23.999849\) | \(5.999850\) | \(0.00614040\) | \(0.0000448212\) | \(0.00618522\) |
| .01 | \(4.7988\times10^{-5}\) | \(-23.999589\) | \(5.999602\) | \(0.02122358\) | \(0.000428750\) | \(0.02165233\) |
| .03 | \(1.1856\times10^{-4}\) | \(-23.999053\) | \(5.999155\) | \(0.06894252\) | \(0.00320689\) | \(0.07214942\) |

Several points are clear.

1. **There is no raw volume reduction in these profiles.**  
   Every recorded \(\Vol(U)/\Vol(B)\) is slightly above one.

2. **The scalar curvature remains overwhelmingly H4-like.**  
   Exact H4 has \(s+18=-6\), so its RMS value is \(6\). The recorded RMS values differ from \(6\) only in the fourth decimal place.

3. **Very little volume has scalar curvature close to \(-18\).**  
   The recorded fractions satisfying \(|s+18|\le3\) are
   \[
   1.28\times10^{-7},\quad
   1.44\times10^{-6},\quad
   1.20\times10^{-5}.
   \]

4. **The large square and volume terms must be interpreted together.**  
   For \(x_0=.003\), for example,
   \[
   \frac1{8\pi^2}\int\frac{(s+18)^2}{3}=358.259337,
   \qquad
   \frac{36\Vol(U)-48\Vol(B)}{8\pi^2}=-358.253197.
   \]
   Their near cancellation is the ordinary H4 background cancellation. If \(s=-24\) exactly, their sum would be
   \[
   48\,\frac{\Vol(U)-\Vol(B)}{8\pi^2}.
   \]
   Hence the large term below zero is not by itself evidence for a volume-saving core. The scientifically relevant quantity is the combined \(C_J\), and it is above zero in all three records.

5. The first identity gives similarly
   \[
   \frac{P}{8\pi^2}-1
   =
   \begin{cases}
   0.00601156+0.00004482,&x_0=.003,\\
   0.02003813+0.00042875,&x_0=.01,\\
   0.05986267+0.00320689,&x_0=.03.
   \end{cases}
   \]
   Both displayed channels are above zero.

Thus the supplied \(X=64\) metrics show no integrated volume/scalar mechanism capable of taking either \(P/(8\pi^2)\) or \(J/(8\pi^2)\) below one. They also show that the scalar profile is much closer to \(-24\) than to \(-18\).

---

### 5. Interpretation of the computational fields

Two aspects are not independent numerical tests:

- `fourWp` is defined by
  ```python
  fourWp = P - 1 - scalar_rel
  ```
  rather than obtained from a coordinate evaluation of \(W^+\). It is therefore the Weyl channel inferred from the relative Chern–Weil formula. Its value tests neither the orientation assignment nor the local Weyl formula independently.

- `J_identity_residual` is essentially the polynomial identity
  \[
  \frac{s^2}{12}+\frac{(s+24)^2}{4}
  =
  \frac{(s+18)^2}{3}+36
  \]
  evaluated with the same quadrature arrays. Residuals near \(10^{-13}\) demonstrate floating-point consistency, not a separate geometric calculation.

There is also an orientation wording issue in the analysis-script docstring. Requiring \(W^+=0\) on an H4 collar does not choose chirality, because real hyperbolic space has both
\[
W^+=0,\qquad W^-=0.
\]
The label \(W^+\) is justified instead by choosing the orientation in which the exceptional class has square \(-1\), so that \(\Delta\tau=-1\). With the opposite orientation, the analogous residual would correspond to the other Weyl block.

Finally, the parametrization has H4 two-jet contact at \(u=1\): the perturbations vanish cubically there. It does not contain an open H4 interval inside the numerical integration domain. This is enough for matching the outer transgression data used by the relative identities. A globally smooth attachment to an exact exterior would use a taper flat to every order or a short smoothing segment.

### Overall assessment

Both channel identities are correct in the stated curvature convention, and the script uses the correct normalized volume density and H4-ball volume. The three \(X=64\) outputs provide strong numerical evidence that their optimized profiles remain H4-like in scalar curvature, have slightly increased volume, and possess positive combined scalar-volume channels. The supplied records concern \(P\)-targeted degree-16 profiles at three \(x_0\) values; they do not determine the behavior of every diagonal profile or of a separate optimization targeted directly at \(J\).