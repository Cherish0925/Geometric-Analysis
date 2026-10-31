# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 6,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step6_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step6_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently examine the corrected perpendicular O11 branch and our new dual-cost/transgression computation. Check: (i) the normalization relation J=P+(1/4)∫(s+24)^2 in the peer's Ric=-6g normalization; (ii) the axis relabeling (new a,b,c)=(old s2,old s3,old s1) and the reported bolt/collar values Y=-1 at the bolt, Y=0 and Pi=X^4? here X=1 gives Pi=9 because CH h=(x,x,x+x^2) and radial normalization; identify the exact general formula in these coordinates; (iii) what the profile x0=.01, P≈1.001996, J≈1.002453, Tmin≈0.0516 says mathematically; and (iv) whether there is a sharper localized boundary/interior identity or inequality that could prove P≥8π² or J≥8π² in the perpendicular diagonal class. Distinguish established algebra from numerical indication and surface any normalization or smoothness errors. Give a direct technical memo with explicit equations and a proposed theorem target.

## Integrated Scientific Memo

# Technical verification memo: perpendicular fixed-slot \(O11\) cell

Write the peer-normalized metric as
\[
g=\frac{dx^{2}}{4G(x)}
   +F(x)\sigma _1^{2}+x\sigma _2^{2}+xe^{\omega(x)}\sigma _3^{2},
\qquad x_0\le x\le X,
\]
where the bolt collapses in the old \(\sigma _1\)-slot and the complex-hyperbolic (CH) fibre is the old \(\sigma _3\)-slot. Numerical \(P,J\) values below are divided by \(8\pi^2\) unless stated otherwise.

## 1. Normalization: exact, with one correction to the script documentation

In dimension four,
\[
\operatorname{Ric}
=\operatorname{Ric}^{\circ}+\frac{s}{4}g,\qquad |g|^2=4.
\]
Therefore
\[
\left|\operatorname{Ric}+6g\right|^2
=\left|\operatorname{Ric}^{\circ}
+\frac{s+24}{4}g\right|^2
=|\operatorname{Ric}^{\circ}|^2+\frac14(s+24)^2.
\]
Thus
\[
\boxed{
J_6(g):=\int |\operatorname{Ric}+6g|^2\,dV
=P(g)+\frac14\int(s+24)^2\,dV .
}
\]
The implementation
\[
p=\frac{P}{8\pi^2},\qquad
q=\frac{1}{32\pi^2}\int(s+24)^2,\qquad j=p+q
\]
is correct.

The scale statement in `perp_dual_cost.py` needs qualification. \(P\) is scale invariant, but \(J_6\) with the coefficient \(6\) held fixed is not. The correct covariance is
\[
J_a(g)=J_{a/\lambda}(\lambda g).
\]
In particular, for \(\widetilde g=6g\),
\[
J_6(g)=J_1(\widetilde g),
\]
and \(\operatorname{Ric}_g=-6g\) becomes \(\operatorname{Ric}_{\widetilde g}=-\widetilde g\). Hence the peer and I54/I55 costs agree after the stated rescaling.

## 2. Axis relabeling and exact slice formulas

The cyclic relabeling
\[
(\text{new }a,\text{new }b,\text{new }c)
=(\text{old }\sigma_2,\text{old }\sigma_3,\text{old }\sigma_1)
\]
is orientation preserving and retains the cyclic structure equations. Its scale factors are
\[
\boxed{
a=\sqrt{x},\qquad b=\sqrt{x\,e^\omega},\qquad c=\sqrt F.
}
\]
If \(t\) is radial arclength,
\[
dt=\frac{dx}{2\sqrt G},\qquad
\dot f=2\sqrt G\,f_x,
\]
so `dots = 2*sqrt(G)*dabc_dx` is correct.

Let
\[
\varepsilon=\frac ab=e^{-\omega/2}.
\]
Then the transgression variables become
\[
p_+=
\frac{e^{\omega/2}\sqrt G-\sqrt F+x(1-e^\omega)/\sqrt F}
     {\sqrt{x}\,e^{\omega/4}},
\]
\[
p_-=
\frac{e^{\omega/2}(1+x\omega_x)\sqrt G-\sqrt F
      -x(1-e^\omega)/\sqrt F}
     {\sqrt{x}\,e^{\omega/4}},
\]
\[
Y=\sqrt G\,\frac{F_x}{\sqrt F}
   -2\cosh\frac{\omega}{2}
   +\frac{F e^{-\omega/2}}{x}
   +\frac12p_+p_-,
\]
\[
\Pi=e^{-\omega/2}p_+^2+e^{\omega/2}p_-^2
      -\frac14(p_+p_-)^2,
\qquad
\frac{\mathcal T}{8\pi^2}=Y^2+\Pi.
\]

### Bolt

For a smooth ordinary bolt,
\[
F(x_0)=G(x_0)=0,\qquad F_x(x_0)G_x(x_0)=1,
\]
and smooth transverse anisotropy requires
\[
\omega=O((x-x_0)^2)=O(t^4).
\]
Consequently
\[
a=b=\sqrt{x_0},\quad c=0,\quad
\dot a=\dot b=0,\quad \dot c=1,\quad p_\pm\to0,
\]
and hence
\[
\boxed{
Y_{\rm bolt}=-1,\qquad
\Pi_{\rm bolt}=0,\qquad
\frac{\mathcal T_{\rm bolt}}{8\pi^2}=1.
}
\]

Thus the earlier claim that \(Y\) is singular in the perpendicular branch is incorrect after the bolt-adapted cyclic relabeling. What fails is not regularity but the aligned scalar-flux endpoint argument.

### CH collar

The code’s actual CH collar is
\[
F=x,\qquad G=x(1+x),\qquad e^\omega=1+x,
\]
so
\[
a=c=\sqrt x,\qquad b=\sqrt{x(1+x)},
\]
and
\[
\dot a=\dot c=\sqrt{1+x},\qquad \dot b=1+2x.
\]
Substitution gives
\[
\boxed{
p_+=0,\qquad
p_-=3x(1+x)^{-1/4},\qquad
Y=0,\qquad
\Pi=9x^2.
}
\]
Therefore
\[
\boxed{
\frac{\mathcal T_{\rm CH}(x)}{8\pi^2}=9x^2,\qquad
\frac{\mathcal T(X)}{8\pi^2}=9X^2.
}
\]
It is not \(X^4\) in the script coordinate \(x\). If \(\rho=\sqrt x\), then it is \(9\rho^4\). After rescaling to the I54 normalization and writing \(R^2=6x\),
\[
9x^2=\frac{R^4}{4},
\]
which is the previously reported formula.

Thus `expected_T_collar=9.0` is correct only because the script fixes \(X=1\); the general value is \(9X^2\).

The CH volume density is
\[
\frac{dV}{dx}=\pi^2x,\qquad
d(x):=\operatorname{Vol}\{0<y<x\}=\frac{\pi^2x^2}{2}
\]
in the peer normalization. Consequently
\[
\mathcal T_{\rm CH}(x)=72\pi^2x^2=144\,d(x).
\]
After scaling to \(\operatorname{Ric}=-g\), the volume is multiplied by \(36\), so this becomes the familiar \(\mathcal T=4d\).

The nonzero \(\Pi\) on the CH collar is not a failure of CH to be Kähler. It records the mismatch between the bolt-adapted \(c\)-slot and the CH Kähler fibre, which lies in the new \(b\)-slot.

## 3. Exact localized identities

Chern–Weil transgression gives
\[
d\mathcal T=
\left(4|W^+|^2+\frac{s^2}{12}
-|\operatorname{Ric}^{\circ}|^2\right)dV .
\]
Define
\[
A(\rho)=\frac1{8\pi^2}\int_{x_0}^{\rho}
\left(\frac{s^2}{12}+4|W^+|^2\right)dV,
\]
\[
B(\rho)=\frac1{8\pi^2}\int_{x_0}^{\rho}
\left[
\frac{s^2}{12}+4|W^+|^2+\frac{(s+24)^2}{4}
\right]dV,
\]
and
\[
\tau(\rho)=Y(\rho)^2+\Pi(\rho)
=\frac{\mathcal T(\rho)}{8\pi^2}.
\]
Then the bolt-to-\(\rho\) region satisfies
\[
\boxed{
\frac{P_{\rm in}(\rho)}{8\pi^2}
=1+A(\rho)-\tau(\rho),
}
\]
\[
\boxed{
\frac{J_{\rm in}(\rho)}{8\pi^2}
=1+B(\rho)-\tau(\rho).
}
\]
For the entire cell,
\[
\boxed{
\frac{P}{8\pi^2}=1+A(X)-9X^2,
\qquad
\frac{J}{8\pi^2}=1+B(X)-9X^2.
}
\]

For \(J\), the interior density has the useful exact completion
\[
\frac{s^2}{12}+\frac{(s+24)^2}{4}+4|W^+|^2
=\frac{(s+18)^2}{3}+36+4|W^+|^2,
\]
hence
\[
\boxed{
J\ge 8\pi^2+36\,\operatorname{Vol}(C_\rho)-\mathcal T(\rho)
}
\]
for every slice \(\rho\). This is a rigorous localized inequality, but it closes the threshold only if the chosen slice also satisfies
\[
36\,\operatorname{Vol}(C_\rho)\ge \mathcal T(\rho).
\]

A useful two-flux rewriting is obtained by setting
\[
Y_\perp=\frac{p_-}{\sqrt{\varepsilon}}.
\]
Then
\[
\boxed{
\tau=Y^2+Y_\perp^2+
p_+^2\left(\varepsilon-\frac{p_-^2}{4}\right).
}
\]
On the collar, \((Y,Y_\perp)=(0,3x)\), while at the bolt it is
\((-1,0)\). This explains why the aligned one-dimensional intermediate-value argument disappears: the relevant flux has rotated into a second component rather than being forced through the origin.

## 4. Meaning of the \(x_0=0.01\) computation

The reported values mean
\[
\frac{P}{8\pi^2}\approx1.001996,\qquad
\frac{J}{8\pi^2}\approx1.002453.
\]
Thus this numerical competitor lies above both thresholds:
\[
P-8\pi^2\approx0.001996(8\pi^2)\approx0.1576,
\]
\[
J-8\pi^2\approx0.002453(8\pi^2)\approx0.1937.
\]
Moreover
\[
\frac{J-P}{8\pi^2}\approx0.000457,
\]
so
\[
\frac14\int(s+24)^2\approx0.000457(8\pi^2)\approx0.0361,
\qquad
\int(s+24)^2\approx0.1443.
\]

At \(X=1\), the exact global identities require
\[
A(1)=9.001996,\qquad B(1)=9.002453.
\]
These are useful independent consistency checks for the curvature and transgression implementations.

The excesses scale numerically as
\[
\frac{P}{8\pi^2}-1\approx19.96\,x_0^2,\qquad
\frac{J}{8\pi^2}-1\approx24.53\,x_0^2
\]
at this one value of \(x_0\). Together with the separate small-\(x_0\) runs, this supports cancellation of the \(O(x_0)\) term in the perpendicular direction. A single value does not prove either an \(x_0^2\) asymptotic or positivity of its coefficient.

If the sampled minimum
\[
\tau_{\min}\approx0.0516
\]
is close to the continuous minimum, then
\[
\mathcal T_{\min}\approx0.0516(8\pi^2)\approx4.07.
\]
At such a slice,
\[
\frac{P_{\rm in}}{8\pi^2}=0.9484+A_*,
\qquad
\frac{J_{\rm in}}{8\pi^2}=0.9484+B_*.
\]
Therefore that slice proves the threshold precisely when
\[
A_*\ge0.0516
\quad\text{or}\quad
B_*\ge0.0516,
\]
respectively. The number \(\tau_{\min}\) alone does not establish either inequality.

The elementary \(J\)-density estimate would suffice if
\[
\operatorname{Vol}(C_*)\ge
\frac{\mathcal T_{\min}}{36}
\approx0.1132.
\]
For \(P\), using
\[
\int_{C_\rho}\frac{s^2}{12}
\ge \frac1{12}
\left(24\sqrt{V_\rho}
-\sqrt{\int_C(s+24)^2}\right)_+^2
\]
and discarding the nonnegative Weyl term gives a sufficient volume of approximately \(0.0944\) at the minimizing slice. The supplied summary does not include that cumulative volume, so neither criterion is presently verified.

The heuristic model
\[
\tau(x)\approx\frac{x_0^2}{x^2}+9x^2
\]
has minimum \(6x_0=0.06\) at \(x=\sqrt{x_0/3}\), reasonably close to \(0.0516\). This is a useful interpretation—orthogonal Burns and CH fluxes—but not an established asymptotic formula.

Finally, the script quantity
\[
\texttt{intF}=H_J-1+\tau
\]
is exactly \(B(\rho)\); hence
\[
\texttt{intF}-\tau=H_J-1.
\]
Its minimum is therefore largely a reformulation of the cumulative \(J\)-cost and is not an independent certificate.

## 5. Smoothness and implementation cautions

1. **Bolt anisotropy.**  
   `wpow=2` gives
   \[
   \omega=O((x-x_0)^2)=O(t^4),
   \]
   as required for the smooth charge-four transverse mode. `wpow=1` gives only \(O(t^2)\) and is not a smooth ordinary-bolt metric in this representation. The reported smooth \(x_0=0.01\) value uses `wpow=2`.

2. **Outer collar.**  
   The factors `(1-u)^3` and the quintic smoothstep make the profile agree with CH through two derivatives at \(X\), but not on an open collar and generally not to all orders. The finite-dimensional profile is therefore a \(C^2\)-matched cell, not literally a smooth exact-collar metric. A flat cutoff on a thin terminal interval should produce smooth exact-collar approximants with convergent curvature-square costs, but that approximation must be stated rather than identifying the printed profile itself with a smooth exact-collar cell.

3. **Fixed diagonal branch only.**  
   `adapted_slice` extracts `sqrt(diag(h))`. This is valid for the fixed-slot perpendicular diagonal profile. It is not valid for the rotated non-diagonal `beta` family without diagonalizing the orbit metric and tracking the moving frame.

4. **Grid minimum.**  
   \(0.0516\) is a minimum over 401 sampled logarithmic points, not a certified continuous minimum. Endpoint values \(1\) and \(9X^2\), by contrast, are exact.

5. **Docstring inconsistency.**  
   `o11_perp_cell.py` describes an \(xe^{-\omega}\) second slot, but the implemented metric is
   \[
   \operatorname{diag}(F,x,xe^\omega).
   \]
   The implementation is consistent with the claimed CH collar; the docstring should be corrected.

6. **Optimization status.**  
   Line-search termination and finite polynomial degree make the quoted values upper bounds for the class infima, not certified minimizers.

The claim that the fixed-slot aligned control is literally “the Kähler cell” should also be avoided. The reported slopes below \(6\) are incompatible with the exact Kähler/conformally Kähler lower bounds; the optimized controls contain genuine triaxial/nonintegrable freedom.

## 6. What is proved, what is only indicated, and the sharp target

### Established

- \(J=P+\frac14\int(s+24)^2\).
- The cyclic relabeling and radial derivative convention.
- \(Y_{\rm bolt}=-1,\ \Pi_{\rm bolt}=0,\ \tau_{\rm bolt}=1\).
- On the perpendicular CH collar,
  \[
  Y=0,\quad p_+=0,\quad \Pi=\tau=9x^2.
  \]
- The exact localized identities above.
- The displayed numerical competitor has \(P,J>8\pi^2\).

### Numerical indication only

- The perpendicular first-order term vanishes.
- The residual cost appears \(O(x_0^2)\) over the currently tested range.
- A possible \(x_0^2\log(1/x_0)\) correction is plausible from overlap-tail interactions, but the sign and coefficient are unresolved. The rough fit suggesting a future sign change is too weak to support the assertion that subthreshold cells exist.

The decisive unresolved object is the second-order asymptotic coefficient—potentially including a logarithm—for the optimized perpendicular cell:
\[
\inf\frac{P}{8\pi^2}
=1+\lambda_P x_0^2\log(1/x_0)+\gamma_Px_0^2+o(x_0^2),
\]
and similarly for \(J\). Its sign cannot be inferred from the current values.

### Proposed theorem target

The strongest natural fixed-slot diagonal theorem is:

> **Perpendicular diagonal cell inequality.**  
> Every smooth ordinary \(\mathcal O(-1)\) one-bolt diagonal cell
> \[
> g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^\omega\sigma_3^2
> \]
> that equals the CH metric on an outer collar satisfies
> \[
> \boxed{P\ge8\pi^2.}
> \]
> Equivalently,
> \[
> \boxed{
> \int_C\left(\frac{s^2}{12}+4|W^+|^2\right)dV
> \ge72\pi^2X^2.
> }
> \]
> Consequently \(J\ge8\pi^2\).

A sharper localized statement, closer to the observed geometry, would be:

> There exists a slice \(\rho\), preferably a minimizer of \(\tau\), such that
> \[
> \boxed{
> \int_{C_\rho}
> \left(\frac{s^2}{12}+4|W^+|^2\right)dV
> \ge 8\pi^2\bigl(Y(\rho)^2+\Pi(\rho)\bigr).
> }
> \]

This immediately implies \(P\ge8\pi^2\) through the exact interior identity. For \(J\), the corresponding target is
\[
\int_{C_\rho}
\left(\frac{(s+18)^2}{3}+36+4|W^+|^2\right)dV
\ge8\pi^2\tau(\rho).
\]

The missing analytic ingredient is therefore a one-dimensional trace/interior estimate controlling the two-component boundary charge \((Y,Y_\perp)\), or directly \(\tau\), by the accumulated scalar and self-dual Weyl energy. The aligned zero-flux argument cannot supply it because the perpendicular collar ends at \(Y=0\) but \(\Pi=9X^2\). Any successful estimate must retain terms through the \(O(x_0^2)\), and possibly \(O(x_0^2\log(1/x_0))\), scale; an \(O(x_0)\)-loss is too coarse.