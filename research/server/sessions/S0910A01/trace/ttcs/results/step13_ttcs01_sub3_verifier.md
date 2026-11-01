# TTCS Independent Branch Record

```json
{
  "step_id": 13,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step13_normalized_accessibility_theorem.md",
    "Sessions/S0910A03/workspace/notes/step12_reduced_equations_accessibility.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step13.md"
  ]
}
```

## Task

Verify the normalization-invariant rank-one reduction and the claimed accessibility bootstrap. Check: (1) The structural formulas: vertical Ric[33] = (-|C|² + 2tr(h) + 2|u|²)/2 with the correct sign, matching A03's tr(H) = 1 + ℓ²|F|²/4 (with the appropriate norm convention). (2) The static limit Spec(W+) = {1/3 - η_i} from the reduction output. (3) The bootstrap argument: is the claim that H ≥ 0 implies Ric_B ≥ -I correct? Is 3D Bishop-Gromov applicable? Does 4D cover noncollapse follow? (4) The gap: does the weighted RCD(-1,4) structure really fail to give ordinary base Ricci? Can any other route (4D arguments on the cover, Moser iteration, Bochner identities) close the gap? Assess what is rigorous and what remains conjectural.

## Output

# Scientific verification memo

## 1. Rank-one reduction: vertical Ricci sign and norm convention

Use
\[
g=q+v^2(dz+B)^2,\qquad e^3=v(dz+B),
\]
with base orthonormal frame \(e^a\), \(a=0,1,2\), and define
\[
u=d\log v,\qquad h_{ab}=\nabla_a\nabla_b\log v,\qquad
H_{ab}=\frac{\nabla_a\nabla_b v}{v}=h_{ab}+u_a u_b,
\]
\[
C_{ab}=vF_{ab},\qquad F=dB,\qquad |C|_{\wedge^2}^2=\sum_{a<b}C_{ab}^2.
\]
Then the geometric Ricci component in the convention where the Einstein metric has
\[
\operatorname{Ric}_g=-g
\]
is
\[
\boxed{
\operatorname{Ric}_g(e_3,e_3)
=
-\operatorname{tr}H+\frac12 |C|_{\wedge^2}^2
=
-\operatorname{tr}h-|u|^2+\frac12 |C|_{\wedge^2}^2 .
}
\]
Thus the Einstein equation \(\operatorname{Ric}_g(e_3,e_3)=-1\) gives
\[
\boxed{
\operatorname{tr}H=\operatorname{tr}h+|u|^2
=
1+\frac12 |C|_{\wedge^2}^2 .
}
\]

The expression appearing in the prompt,
\[
\frac{-|C|^2+2\operatorname{tr}h+2|u|^2}{2}
=
\operatorname{tr}H-\frac12|C|^2,
\]
is the sign-reversed Ricci component relative to the geometric convention above. It matches the same Einstein equation only if the script’s `Ric[33]` uses the sign-reversed curvature convention and the Einstein equation is written there as `Ric[33]=+1`.

Norm conversion matches the supplied Step 12 formula. Since
\[
C=vF,\qquad z=*C,\qquad |z|^2=|C|_{\wedge^2}^2,
\]
and
\[
C_{ab}C^{ab}=2|C|_{\wedge^2}^2,
\]
one has
\[
\frac12 |C|_{\wedge^2}^2
=
\frac14 C_{ab}C^{ab}
=
\frac14 v^2F_{ab}F^{ab}.
\]
So
\[
\operatorname{tr}H
=
1+\frac12|z|^2
=
1+\frac14 v^2F_{ab}F^{ab},
\]
which is exactly the Step 12 relation
\[
\operatorname{tr}H=\kappa+\frac12|z|^2
=
\kappa+\frac14\ell^2F_{ab}F^{ab}
\]
with \(\kappa=1\).

A further structural point: the mixed equation in the supplied Step 13 note should be handled with care. The standard Kaluza–Klein variation gives
\[
d(v^3 *_q F)=0,
\]
or, with \(C=vF\) and \(z=*C\),
\[
d(v^2z)=0.
\]
Equivalently,
\[
\delta_q(v^2C)=0.
\]
Together with \(dF=0\), this gives the Step 12 equations
\[
dz=-2u\wedge z,\qquad \operatorname{div}z=\langle u,z\rangle .
\]
This coefficient matters for the weighted elliptic estimates in the bootstrap.

---

## 2. Static limit and \(W^+\)-spectrum

In the static case \(C=0\), the vertical sectional curvature term is
\[
R_{a3b3}=-H_{ab}.
\]
For \(\operatorname{Ric}_g=-g\), the electric Weyl tensor is
\[
E_{ab}=W_{a3b3}
=
\frac13 q_{ab}-H_{ab}.
\]
The magnetic block vanishes in the static case, so, up to exchanging chirality by orientation,
\[
W^+=E.
\]
Therefore, if \(\eta_1,\eta_2,\eta_3\) are the eigenvalues of
\[
H=\frac{\operatorname{Hess}v}{v},
\qquad \operatorname{tr}H=1,
\]
then
\[
\boxed{
\operatorname{Spec}(W^+)=\left\{\frac13-\eta_i\right\}_{i=1}^3 .
}
\]

The script verification with \(u=0\), \(C=0\), and diagonal \(h\) checks the special case \(H=h\). The tensor formula above is the invariant static formula; it also covers static points with \(u\ne0\) once \(H=h+u\otimes u\) is used.

The product model \(H^2\times H^2\), written with a polar circle on one \(H^2\) factor, has
\[
\operatorname{Spec}(H)=(1,0,0),
\]
so
\[
\operatorname{Spec}(W^+)=\left(-\frac23,\frac13,\frac13\right),
\]
matching the supplied Step 12 correction. Thus the static spectrum formula is correct, but it does not imply that constant static spectrum forces \(W^+=0\).

---

## 3. Algebraic part of the bootstrap: \(H\ge0\Rightarrow \operatorname{Ric}_B\ge -q\)

The horizontal Einstein equation is
\[
\boxed{
\operatorname{Ric}_B
=
-q+H+\frac12\, C_{ac}C_b{}^c .
}
\]
For every horizontal vector \(X\),
\[
C_{ac}C_b{}^c X^aX^b
=
\sum_c\left(\sum_a X^aC_{ac}\right)^2
\ge0.
\]
Therefore, if
\[
H=\frac{\operatorname{Hess}v}{v}\ge0
\]
as a quadratic form, then
\[
\boxed{
\operatorname{Ric}_B\ge -q .
}
\]
This algebraic implication is correct.

However, the subsequent use of Bishop–Gromov needs an additional input. A Ricci lower bound alone does not give an absolute lower volume bound for a fixed-radius ball. Smooth 3-manifolds can collapse with \(\operatorname{Ric}\ge -q\); flat manifolds with a very short circle already show that lower Ricci does not create a fixed harmonic radius or fixed volume ratio.

What Bishop–Gromov gives is relative volume comparison. It propagates a volume lower bound from one scale to smaller scales, but it does not supply the first such bound. Thus the statement

\[
H\ge0\quad\Longrightarrow\quad \operatorname{Ric}_B\ge -q
\quad\Longrightarrow\quad
\text{fixed base noncollapse}
\]
is not mathematically valid without an extra base volume, injectivity, local-cover, or no-further-collapse assumption.

The same issue appears in the Step 13 harmonic-radius step. In dimension three, a two-sided Ricci bound controls full curvature, but a harmonic radius lower bound still needs noncollapse, or one must pass to a suitable local cover that unwraps all short directions. The rank-one fiber cover unwraps only the chosen circle direction; it does not automatically unwrap short loops already present in the base.

---

## 4. Does 4D cover noncollapse follow from \(H\ge0\)?

Only with extra quantitative data.

If one has:

1. a smooth buffered free-circle domain;
2. an unwrapped fiber coordinate \(z\);
3. a base ball \(B_q(p,s)\) with
   \[
   \operatorname{Vol}_q(B_q(p,s))\ge v_0s^3;
   \]
4. enough control of \(v\) or at least of \(\int_{B_q(p,s)}v\,dV_q\);

then the 4D cover has volume lower bounds. Indeed, horizontal lifting gives a set comparable to
\[
B_q(p,s)\times (-a,a)
\]
inside a 4D ball, and
\[
dV_4=v\,dV_q\,dz,
\]
so
\[
\operatorname{Vol}_4\gtrsim 2a\int_{B_q(p,s)}v\,dV_q.
\]
With \(v(p)=1\), a mean-value estimate for positive subharmonic \(v\) could help once the base geometry is already controlled. But \(H\ge0\) and \(\operatorname{Ric}_B\ge -q\) do not by themselves give the required base volume or a uniform lower integral for \(v\) at fixed scale.

Therefore the static rank-one case is closed only under an added base noncollapse/local-cover hypothesis. The algebra \(H\ge0\Rightarrow \operatorname{Ric}_B\ge -q\) is sound; the volume conclusion is not automatic.

---

## 5. The weighted \(RCD(-1,4)\) structure and ordinary base Ricci

The supplied Step 12 note is correct on this point. For the quotient measure
\[
dm=v\,dV_q,
\]
the smooth \(N=4\) Bakry–Émery tensor is
\[
\operatorname{Ric}^{4}_{q,v}
=
\operatorname{Ric}_q-\frac{\operatorname{Hess}v}{v}
=
\operatorname{Ric}_q-H.
\]
From the 4D Ricci lower bound one obtains
\[
\operatorname{Ric}^{4}_{q,v}\ge -q,
\]
hence weighted \(RCD(-1,4)\)-type structure for the quotient metric-measure space.

This does not give ordinary \(\operatorname{Ric}_q\) bounds. The missing term is exactly
\[
H=\frac{\operatorname{Hess}v}{v},
\]
and the horizontal equation reads
\[
\operatorname{Ric}_q
=
-q+H+\frac12C^2.
\]
Thus \(H\) and the twist-square term can make ordinary base Ricci large while the weighted tensor remains controlled. Weighted doubling and Poincaré estimates are for \(v\,dV_q\), not for the unweighted Riemannian measure \(dV_q\), and they do not produce a three-dimensional harmonic coordinate radius for \(q\).

So the Step 13 correction identifying weighted \(RCD(-1,4)\) as insufficient for ordinary base regularity is scientifically right.

---

## 6. The bootstrap gap

The bootstrap as written has several circular dependencies.

### Weighted harmonic-form estimate

The desired estimate is roughly:
\[
dF=0,\qquad d(v^3*_qF)=0
\quad\Longrightarrow\quad
\|F\|_{L^\infty(B_{r/2})}\le C\|F\|_{L^2(B_r)}.
\]
But the operator has coefficients involving powers of \(v\). Uniform ellipticity requires quantitative upper and lower control for \(v\), or an equivalent weighted regularity theory with controlled weight constants.

The center condition
\[
|C(p)|^2=v(p)^2|F(p)|^2\ge c_0,\qquad v(p)=1,
\]
does not give a lower bound for \(v\) on a ball. Smooth positivity of \(v\) gives a lower bound depending on the individual solution, not a uniform one. Hence the elliptic estimate cannot be initiated from the stated data.

### Harnack for \(v\)

The equation
\[
\Delta_q v
=
v\left(1+\frac12|C|^2\right)
\]
has coefficient
\[
1+\frac12|C|^2.
\]
A Harnack constant depends on a bound for this coefficient in a suitable norm and on Sobolev/doubling data for \(q\). Those are precisely the quantities the bootstrap is trying to obtain.

The fact that \(v>0\) and \(\Delta v\ge0\) is not enough. Positive subharmonic functions with \(v(p)=1\) can have arbitrarily large growth at fixed radius, and uniform two-sided Harnack estimates require more than positivity.

### Base harmonic radius

Even if one obtained pointwise \(|F|\) and \(v\)-Harnack estimates, the passage
\[
|\operatorname{Ric}_B|\le R
\quad\Longrightarrow\quad
\text{base harmonic radius}\ge h_0
\]
still needs a base noncollapse input. In dimension three, bounded Ricci gives bounded full curvature, but collapsed flat examples show that curvature bounds alone do not give a fixed harmonic coordinate radius.

---

## 7. Other possible routes

### 4D arguments on the cover

The normalization
\[
z=\ell(p)\psi,\qquad v=\ell/\ell(p),\qquad B=\ell(p)A
\]
is valid: the local coefficients of
\[
\hat g=q+v^2(dz+B)^2
\]
are independent of the original fiber period. The period only decides whether \(z\) is periodic or unwrapped.

But 4D Ricci bounds plus bounded \(L^2\)-curvature mean do not yield a harmonic radius in dimension four without noncollapse or small normalized energy. Ye Li’s smoothing theorem cited in the supplied Step 12 note uses small
\[
\frac{r^4}{\operatorname{Vol}(B_r)}\int_{B_r}|Rm|^2,
\]
not merely a bounded mean. The calibrated region has a nonzero background curvature density, so the required smallness is absent unless a new renormalized smoothing theorem is proved.

A gauge-covariant smoothing theory for the calibrated residual could be powerful, but no such theorem is supplied.

### Moser iteration on the 4D cover

For a base function \(v\),
\[
\Delta_{\hat g} v
=
\Delta_q v+\langle\nabla\log v,\nabla v\rangle
=
v\left(1+\frac12|C|^2+|u|^2\right).
\]
Equivalently,
\[
\Delta_{\hat g}\log v
=
1+\frac12|C|^2.
\]
These equations still contain \(|C|^2\) and \(|u|^2\). Moser iteration would require integral control of these terms and Sobolev constants on the cover. Those are not available before noncollapse or a substitute weighted estimate is established.

### Chiral Bochner identities

The Step 12 chiral factorization
\[
a_\pm=u\mp\frac12z,
\]
\[
W^\pm
=
-\big[\operatorname{sym}\nabla a_\pm+a_\pm\otimes a_\pm\big]_0,
\]
\[
da_+=a_+\wedge a_-,
\qquad
da_-=-a_+\wedge a_-
\]
is a strong structural reformulation.

A Bochner identity could in principle control
\[
|\nabla a_\pm|^2,\qquad |a_+\wedge a_-|^2,
\]
from the two chiral Weyl energies plus cutoff terms. The main analytic obstruction is the trace mode:
\[
\operatorname{div}a_\pm+|a_\pm|^2,
\]
which is not controlled by the trace-free Weyl block alone. Large \(u\) and \(z\) may cancel in one chiral combination while remaining large in the other. Thus the chiral system is promising but not yet a regularity theorem.

---

## 8. What is rigorous at this stage

The following pieces are mathematically solid from the supplied material and the standard Kaluza–Klein formulas:

1. The normalized local cover form
   \[
   g=q+v^2(dz+B)^2,\qquad v(p)=1,
   \]
   removes the absolute fiber length from local coefficients.

2. The geometric vertical Ricci formula is
   \[
   \operatorname{Ric}_{33}
   =
   -\operatorname{tr}H+\frac12|C|_{\wedge^2}^2.
   \]

3. The Einstein equation \(\operatorname{Ric}=-g\) gives
   \[
   \operatorname{tr}H
   =
   1+\frac12|C|_{\wedge^2}^2
   =
   1+\frac14 v^2F_{ab}F^{ab}.
   \]

4. In the static case,
   \[
   \operatorname{Spec}(W^+)=\left\{\frac13-\eta_i\right\},
   \]
   where \(\eta_i\) are the eigenvalues of \(H=\operatorname{Hess}v/v\).

5. The algebraic implication
   \[
   H\ge0\quad\Longrightarrow\quad \operatorname{Ric}_B\ge -q
   \]
   is correct.

6. Weighted quotient geometry gives
   \[
   \operatorname{Ric}_q-H\ge -q,
   \]
   not ordinary \(\operatorname{Ric}_q\) control.

The accessibility bootstrap remains conjectural in the twisted or further-collapsed setting. To make it rigorous, one needs an additional mechanism supplying at least one of the following:

- fixed-scale base noncollapse or an appropriate local cover unwrapping all short base directions;
- uniform control of \(v\) sufficient for weighted elliptic estimates;
- a 4D regularity theorem driven by calibrated residual rather than full small curvature energy;
- a coercive chiral Bochner identity controlling the trace modes as well as the trace-free Weyl blocks.