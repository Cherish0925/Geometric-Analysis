# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/scripts/step9_nil3_orbit_volume.py",
    "Sessions/S0910A01/workspace/notes/step9_regular_collapse_exclusion.md",
    "Sessions/S0910A03/workspace/notes/step7_orbit_volume_negative_einstein_collapse.tex"
  ]
}
```

## Task

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

## Output

## Scientific memo

### Main finding

The \(tt\)-equation \(E0\) is correct, but the Nil\(^3\) curvature terms in \(E1,E2,E3\) have the opposite signs. With the standard Riemannian curvature convention and \([X_1,X_2]=X_3\), the correct orbit-volume identity is

\[
\boxed{\frac{v''}{v}=3-\mu},
\qquad
\mu=\frac{a_3^2}{2a_1^2a_2^2},
\]

not \(3+\mu\). Thus the asserted estimate \(v''\ge 3v\) does not follow.

### 1. Intrinsic Ricci tensor of the Nil\(^3\) orbit

Let \(X_i\) be the left-invariant frame dual to the coframe \(\sigma_i\), with

\[
[X_1,X_2]=X_3.
\]

For the orthonormal frame

\[
e_i=\frac{X_i}{a_i},
\]

one has

\[
[e_1,e_2]=c\,e_3,
\qquad
c=\frac{a_3}{a_1a_2}.
\]

The sectional curvatures of this left-invariant Nil\(^3\) metric are

\[
K_{12}=-\frac{3c^2}{4},
\qquad
K_{13}=K_{23}=\frac{c^2}{4}.
\]

Consequently,

\[
\operatorname{Ric}^{(3)}(e_1,e_1)
=\operatorname{Ric}^{(3)}(e_2,e_2)
=-\frac{c^2}{2}=-\mu,
\]

\[
\operatorname{Ric}^{(3)}(e_3,e_3)
=\frac{c^2}{2}=+\mu,
\]

and the orbit scalar curvature is

\[
R^{(3)}=-\mu.
\]

Thus the two horizontal directions carry \(-\mu\), while the central direction carries \(+\mu\).

### 2. Four-dimensional Ricci equations

Put

\[
f_i=\frac{a_i'}{a_i},
\qquad
F=f_1+f_2+f_3.
\]

For \(g=dt^2+g_t\),

\[
\operatorname{Ric}_{00}
=-\sum_i(f_i'+f_i^2),
\]

and

\[
\operatorname{Ric}_{ii}
=\operatorname{Ric}^{(3)}_{ii}-f_i'-f_iF.
\]

Therefore \(\operatorname{Ric}_g=-g\) gives

\[
\boxed{
(f_1'+f_1^2)+f_1f_2+f_1f_3+\mu=1,
}
\]

\[
\boxed{
(f_2'+f_2^2)+f_1f_2+f_2f_3+\mu=1,
}
\]

\[
\boxed{
(f_3'+f_3^2)+f_1f_3+f_2f_3-\mu=1.
}
\]

The supplied equations have all three \(\mu\)-signs reversed.

The radial equation is indeed

\[
\boxed{
(f_1'+f_1^2)+(f_2'+f_2^2)+(f_3'+f_3^2)=1.
}
\]

Hence \(E0\) is being used correctly when writing

\[
\frac{v''}{v}
=1+2(f_1f_2+f_1f_3+f_2f_3).
\]

### 3. Correct cross-term extraction

Let

\[
S=f_1f_2+f_1f_3+f_2f_3.
\]

Summing the corrected tangential equations gives

\[
\left[\sum_i(f_i'+f_i^2)\right]+2S+\mu=3.
\]

Using \(E0\),

\[
1+2S+\mu=3,
\]

so

\[
2S=2-\mu.
\]

It follows that

\[
\boxed{
\frac{v''}{v}=1+2S=3-\mu.
}
\]

An even shorter derivation comes from tracing the tangential Ricci tensor:

\[
\sum_{i=1}^3\operatorname{Ric}_{ii}
=R^{(3)}-\frac{v''}{v}.
\]

Since the left side is \(-3\) and \(R^{(3)}=-\mu\),

\[
-3=-\mu-\frac{v''}{v},
\]

which again gives \(v''/v=3-\mu\). Intrinsic Nil curvature therefore subtracts from the abelian mass term.

The arithmetic in step 4 is internally correct for the displayed equations; the mathematical issue occurs earlier, in the intrinsic Ricci signs.

### 4. Explicit exact test metric

Take

\[
a_1=a_2=e^{t/\sqrt6},
\qquad
a_3=\sqrt{\frac23}\,e^{2t/\sqrt6}.
\]

Then

\[
(f_1,f_2,f_3)=\frac1{\sqrt6}(1,1,2),
\qquad
\mu=\frac13.
\]

The Ricci formulas give

\[
\operatorname{Ric}_{00}
=-\frac{1+1+4}{6}=-1,
\]

\[
\operatorname{Ric}_{11}
=-\frac13-\frac23=-1,
\qquad
\operatorname{Ric}_{22}=-1,
\]

\[
\operatorname{Ric}_{33}
=\frac13-\frac43=-1.
\]

Thus this is an exact \(\operatorname{Ric}=-g\) Bianchi-II metric. Its orbit volume satisfies

\[
v\propto e^{4t/\sqrt6},
\qquad
\frac{v''}{v}=\frac{16}{6}=\frac83
=3-\frac13.
\]

The proposed formula would instead give \(10/3\), so this metric directly distinguishes the two signs.

### 5. Periodic and zero-endpoint data

If one had \(v''\ge3v\) with \(v>0\), then both arguments in the note would be valid:

- For an \(L\)-periodic \(v\),

  \[
  0=\int_0^L v''\,dt
  \ge3\int_0^L v\,dt>0,
  \]

  which is impossible.

- If \(v(0)=v(L)=0\), \(v>0\) inside, and \(v\) is continuous on \([0,L]\), its positive maximum occurs inside, where \(v''\le0\), contradicting \(v''>0\).

The corrected identity \(v''=(3-\mu)v\) does not provide that convexity because \(\mu\) has no universal upper estimate in this derivation.

For periodic diagonal Bianchi-II metrics there is nevertheless a separate contradiction. The corrected central equation gives

\[
(vf_3)'=v(f_3'+Ff_3)=(1+\mu)v>0.
\]

A periodic \(vf_3\) cannot have a strictly positive derivative everywhere. Thus the periodic case remains excluded, but by the central-direction equation rather than \(v''\ge3v\).

For \(v(0)=v(L)=0\), the volume equation alone is insufficient. The endpoint behavior of

\[
vf_3=a_1a_2a_3'
\]

or an independent geometric description of the collapsing orbit is needed.

### 6. Near-\(-g\) equation

Write

\[
\operatorname{Ric}=-g+E
\]

in the orthonormal frame. Then

\[
\sum_i(f_i'+f_i^2)=1-E_{00},
\]

while the tangential equations become

\[
f_1'+f_1F+\mu=1-E_{11},
\]

\[
f_2'+f_2F+\mu=1-E_{22},
\]

\[
f_3'+f_3F-\mu=1-E_{33}.
\]

Tracing gives the exact identity

\[
\boxed{
\frac{v''}{v}
=3-\mu-(E_{11}+E_{22}+E_{33}).
}
\]

If every orthonormal component obeys \(|E_{ii}|\le\delta\), then only

\[
\boxed{
v''\ge (3-\mu-3\delta)v
}
\]

follows. In particular, \(v''\ge3(1-\delta)v\) is unavailable without an independent upper estimate for \(\mu\). The exact example above already violates that proposed estimate at \(\delta=0\).

The periodic central-direction argument does have a stable near-\(-g\) form:

\[
(vf_3)'=(1+\mu-E_{33})v
\ge(1-\delta+\mu)v>0
\]

when \(\delta<1\).

### 7. Structure-sign convention and supplied script

Replacing \([X_1,X_2]=X_3\) by \([X_1,X_2]=-X_3\) changes \(c\) to \(-c\), but every intrinsic Ricci term depends on \(c^2\). It therefore does not alter the result. More generally, \([X_1,X_2]=\kappa X_3\) replaces \(\mu\) by

\[
\mu=\frac{\kappa^2a_3^2}{2a_1^2a_2^2}.
\]

Reversing the entire Riemann-tensor convention would also reverse the \(tt\)-Ricci formula, so it cannot preserve the stated \(E0\) while reversing only the Nil terms.

In `step9_nil3_orbit_volume.py`, the correct acceleration equations are

\[
a_1''=a_1\!\left(1-f_1(f_2+f_3)-\mu\right),
\]

\[
a_2''=a_2\!\left(1-f_2(f_1+f_3)-\mu\right),
\]

\[
a_3''=a_3\!\left(1-f_3(f_1+f_2)+\mu\right).
\]

The script uses the opposite \(\mu\)-signs. Its zero-velocity initial data also do not generally satisfy \(E0\): with \(f_i(0)=0\), the corrected tangential equations give \(\sum a_i''/a_i=3-\mu\), while \(E0\) requires this sum to equal \(1\), hence \(\mu=2\). Therefore those numerical trajectories do not test the full Einstein equations.

The Nil\(^3\) part of the stated regular-collapse exclusion is consequently not established by the orbit-volume convexity argument. The periodic diagonal case has the separate monotonicity identity above; interval-type degenerations and general Nil \(N\)-structures require additional geometric equations.