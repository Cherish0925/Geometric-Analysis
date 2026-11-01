# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 9,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step9_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step9_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following derivation for the nil³ orbit-volume equation. For a 4D Bianchi-II warped product g = dt² + a₁²σ₁² + a₂²σ₂² + a₃²σ₃² with [σ₁,σ₂] = σ₃ (Nil³ frame) and Ric = -g:

1. Define fᵢ = aᵢ'/aᵢ and μ = a₃²/(2a₁²a₂²).
2. The Einstein equations are:
   E0: (f₁'+f₁²)+(f₂'+f₂²)+(f₃'+f₃²) = 1
   E1: (f₁'+f₁²)+f₁f₂+f₁f₃-μ = 1
   E2: (f₂'+f₂²)+f₁f₂+f₂f₃-μ = 1
   E3: (f₃'+f₃²)+f₁f₃+f₂f₃+μ = 1
3. The orbit volume v = a₁a₂a₃ satisfies v''/v = 1 + 2(f₁f₂+f₁f₃+f₂f₃).
4. Summing E1+E2+E3: 1 + 2(f₁f₂+f₁f₃+f₂f₃) - μ = 3.
5. Therefore v'' = (3+μ)v ≥ 3v.

Check each step: (a) Are the Ricci tensor components correct for Bianchi II? (b) Is the cross-term sum correctly extracted from E1+E2+E3? (c) Does E0 play the right role? (d) Does the result v'' ≥ 3v exclude periodic and vanishing-boundary solutions? (e) For the near-Einstein case Ric = -g+E with |E| ≤ δ, does v'' ≥ 3(1-δ)v hold? (f) Is there any sign convention issue with the Nil³ structure constants that could affect the result?

## Integrated Scientific Memo

# Verification result

The proposed derivation is **incorrect at step 2**: the Nil\(^3\) curvature terms in \(E1,E2,E3\) have the opposite signs. With the standard convention and center direction \(3\),

\[
\boxed{\frac{v''}{v}=3-\mu},\qquad
\mu=\frac{a_3^2}{2a_1^2a_2^2},
\]

not \(3+\mu\). Consequently, neither \(v''\ge 3v\) nor its claimed near-Einstein analogue follows.

## (a) Correct Ricci components

Let \(X_i\) be dual to \(\sigma_i\), with

\[
[X_1,X_2]=X_3,
\qquad e_i=\frac{X_i}{a_i},
\qquad [e_1,e_2]=c\,e_3,
\quad c=\frac{a_3}{a_1a_2}.
\]

For the left-invariant Nil\(^3\) orbit metric,

\[
\operatorname{Ric}^{(3)}_{11}
=\operatorname{Ric}^{(3)}_{22}
=-\frac{c^2}{2}=-\mu,
\qquad
\operatorname{Ric}^{(3)}_{33}
=+\frac{c^2}{2}=+\mu.
\]

For \(g=dt^2+g_t\), writing \(F=f_1+f_2+f_3\),

\[
\operatorname{Ric}_{00}=-\sum_i(f_i'+f_i^2),
\qquad
\operatorname{Ric}_{ii}
=\operatorname{Ric}^{(3)}_{ii}-f_i'-f_iF.
\]

Thus \(\operatorname{Ric}=-g\) gives

\[
E0:\quad \sum_i(f_i'+f_i^2)=1,
\]

and the corrected tangential equations

\[
E1:\quad (f_1'+f_1^2)+f_1f_2+f_1f_3+\mu=1,
\]

\[
E2:\quad (f_2'+f_2^2)+f_1f_2+f_2f_3+\mu=1,
\]

\[
E3:\quad (f_3'+f_3^2)+f_1f_3+f_2f_3-\mu=1.
\]

The source note and script reverse all three \(\mu\)-signs.

## (b) Correct cross-term extraction

Set

\[
S=f_1f_2+f_1f_3+f_2f_3.
\]

Summing the corrected equations \(E1+E2+E3\) gives

\[
\sum_i(f_i'+f_i^2)+2S+\mu=3.
\]

Using \(E0\),

\[
1+2S+\mu=3,
\qquad
2S=2-\mu.
\]

Therefore

\[
\frac{v''}{v}=1+2S=3-\mu.
\]

Step 4 was algebraically consistent with the *stated* equations, but those equations had the wrong intrinsic-curvature signs.

A useful invariant check is

\[
\sum_{i=1}^3\operatorname{Ric}_{ii}
=R^{(3)}-\frac{v''}{v},
\qquad R^{(3)}=-\mu.
\]

Since the tangential trace equals \(-3\),

\[
-3=-\mu-\frac{v''}{v},
\]

again yielding \(v''/v=3-\mu\).

## (c) Role of \(E0\)

\(E0\) is correct and used correctly:

\[
\frac{v''}{v}
=\sum_i f_i'+\left(\sum_i f_i\right)^2
=1+2S.
\]

There is no intrinsic Nil curvature term in \(\operatorname{Ric}_{00}\). The failure lies solely in the tangential equations.

## Independent exact check

Take

\[
a_1=a_2=e^{t/\sqrt6},
\qquad
a_3=\sqrt{\frac23}\,e^{2t/\sqrt6}.
\]

Then

\[
(f_1,f_2,f_3)=\frac1{\sqrt6}(1,1,2),
\qquad \mu=\frac13,
\]

and the corrected equations give \(\operatorname{Ric}=-g\). Moreover,

\[
v=a_1a_2a_3=C e^{4t/\sqrt6},
\qquad
\frac{v''}{v}=\frac{16}{6}=\frac83
=3-\frac13.
\]

The proposed formula \(3+\mu\) would incorrectly give \(10/3\).

## (d) Periodic and vanishing-boundary consequences

If \(v''\ge3v\) were true, both proposed contradictions would be valid. But the corrected equation

\[
v''=(3-\mu)v
\]

does not imply convexity because \(\mu\) has no established universal upper bound.

### Periodic case

The volume equation alone gives only

\[
\int_0^L(3-\mu)v\,dt=0,
\]

which is not contradictory. Nevertheless, periodic diagonal Bianchi-II solutions are excluded by the corrected central equation:

\[
f_3'+Ff_3-\mu=1.
\]

Since \(v'=Fv\),

\[
(vf_3)'=v(f_3'+Ff_3)=(1+\mu)v>0.
\]

For periodic \(a_i\), the quantity \(vf_3=a_1a_2a_3'\) is periodic, so it cannot have strictly positive derivative everywhere.

### Vanishing endpoints

If \(v(0)=v(L)=0\) and \(v>0\) inside, an interior maximum now implies only

\[
0\ge v''=(3-\mu)v
\quad\Longrightarrow\quad \mu\ge3
\]

at that point. There is no contradiction. Endpoint regularity and the behavior of \(vf_3=a_1a_2a_3'\), or a geometric classification of the singular orbit, are required.

## (e) Near-Einstein equation

Let

\[
\operatorname{Ric}=-g+E
\]

and express \(E_{\alpha\alpha}\) in the adapted orthonormal frame. Then

\[
\sum_i(f_i'+f_i^2)=1-E_{00},
\]

while

\[
f_1'+Ff_1+\mu=1-E_{11},
\]

\[
f_2'+Ff_2+\mu=1-E_{22},
\]

\[
f_3'+Ff_3-\mu=1-E_{33}.
\]

Tracing the tangential equations gives the exact identity

\[
\boxed{
\frac{v''}{v}
=3-\mu-(E_{11}+E_{22}+E_{33}).
}
\]

Hence, if \(|E|\le\delta\) means operator or pointwise tensor norm so that
\(|E_{ii}|\le\delta\),

\[
v''\ge (3-\mu-3\delta)v.
\]

The claimed estimate

\[
v''\ge3(1-\delta)v
\]

is false without an independent bound eliminating or controlling \(\mu\).

The periodic monotonicity argument remains stable:

\[
(vf_3)'=(1+\mu-E_{33})v
\ge(1-\delta+\mu)v>0
\]

for \(\delta<1\).

## (f) Structure-constant convention

Changing

\[
[X_1,X_2]=X_3
\quad\text{to}\quad
[X_1,X_2]=-X_3
\]

does not change the result, because the curvature terms depend on the square of the structure constant. More generally, for

\[
[X_1,X_2]=\kappa X_3,
\]

one has

\[
\mu=\frac{\kappa^2a_3^2}{2a_1^2a_2^2}.
\]

Thus this is not a bracket-sign ambiguity. Reversing the full Riemann-tensor convention would also reverse the \(tt\)-Ricci convention, so it cannot justify retaining the stated \(E0\) while reversing only the Nil terms.

## Script corrections

In `step9_nil3_orbit_volume.py`, the corrected acceleration equations are

\[
a_1''=a_1\left(1-f_1(f_2+f_3)-\mu\right),
\]

\[
a_2''=a_2\left(1-f_2(f_1+f_3)-\mu\right),
\]

\[
a_3''=a_3\left(1-f_3(f_1+f_2)+\mu\right).
\]

The current script uses the opposite signs. It also integrates only the tangential evolution equations; arbitrary initial data need not satisfy the \(E0\) constraint. In particular, zero initial velocities satisfy that constraint only for special initial scale data, so the numerical trajectories are not generally Einstein solutions.

## Conclusion

\[
\boxed{v''=(3-\mu)v}
\]

is the correct exact Nil\(^3\) orbit-volume equation. The claimed Nil\(^3\) convexity exclusion and the downstream assertion that all regular four-dimensional collapse is excluded are therefore unsupported. The periodic diagonal case is still ruled out by \((vf_3)'>0\), but interval degenerations and more general Nil \(N\)-structures remain unresolved by this computation.