# TTCS Independent Branch Record

```json
{
  "step_id": 7,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step7_orbit_volume_negative_einstein_collapse.tex",
    "Sessions/S0910A03/workspace/scripts/investigate_nil3_negative_einstein.py"
  ]
}
```

## Task

Investigate whether the full Einstein system Ric(g) = -g can have solutions on a 4-manifold with nil³ (Heisenberg) fiber structure over a 1D base.

The setup: total metric g = ds² + G_IJ(s)(dx^I + A^I(s))(dx^J + A^J(s)) where {e₁,e₂,e₃} generate the Heisenberg algebra [e₁,e₂] = e₃.

For abelian (torus) fibers over 1D base with Ric = -g, Lott's orbit-volume equation gives v'' = 3v (where v = √det G), which has no periodic solutions (contradicts ∫v'' = 0 on a circle). This cleanly excludes abelian collapse.

For nil³: the Heisenberg structure constant contributes negative fiber Ricci curvature R_fiber = -a₃²/(2a₁²a₂²), which partially compensates the positive mass term. The question is whether the full Einstein ODE system has:
(a) ANY periodic solution on a circle base
(b) ANY solution on an interval with controlled behavior at endpoints
(c) A generalized orbit-volume equation with positive coefficient

Key constraint: Ric(∂s,∂s) = -1 gives a₁''/a₁ + a₂''/a₂ + a₃''/a₃ = 1. The cross terms in v''/v = 1 + 2Σ_{i<j}(a_i'/a_i)(a_j'/a_j) can be negative, so the argument doesn't immediately extend from abelian.

Please determine whether a positive-coefficient orbit-volume inequality holds for nil³ with λ = -1, or construct/identify a mechanism that could allow nil³ negative Einstein solutions.

## Output

### Main computation: the nil³ orbit-volume law

For a 1D base, the shift/connection term can be removed locally, so the metric is

\[
g=ds^2+h_s ,
\]

where \(h_s\) is a left-invariant metric on the Heisenberg algebra \(\mathfrak n\). Let

\[
L=\frac12 h_s^{-1}\dot h_s,\qquad H=\operatorname{tr}L=\frac{v'}v,\qquad v=\sqrt{\det h_s}.
\]

The hypersurface Ricci formulas give

\[
\operatorname{Ric}_{ss}=-\dot H-\operatorname{tr}L^2,
\]

\[
\operatorname{Ric}^{\#}_{T}
=\operatorname{Ric}^{\#}_{h_s}-\dot L-HL .
\]

Thus \(\operatorname{Ric}_g=-g\) is equivalent to

\[
\dot H+\operatorname{tr}L^2=1,
\]

\[
\dot L+HL=\operatorname{Ric}^{\#}_{h_s}+I.
\]

Taking the tangential trace,

\[
\dot H+H^2=3+\operatorname{Scal}(h_s).
\]

For Heisenberg, in an orthonormal Milnor frame with

\[
[E_1,E_2]=mE_3,
\]

the fiber Ricci eigenvalues are

\[
-\frac{m^2}{2},\quad -\frac{m^2}{2},\quad +\frac{m^2}{2},
\]

so

\[
\operatorname{Scal}(h_s)=-\frac{m^2}{2}.
\]

Put

\[
\rho=m^2.
\]

For a diagonal metric

\[
h_s=a_1(s)^2\theta_1^2+a_2(s)^2\theta_2^2+a_3(s)^2\theta_3^2,
\qquad d\theta_3=\theta_1\wedge\theta_2,
\]

this is

\[
\rho=\frac{a_3^2}{a_1^2a_2^2}.
\]

Therefore the exact nil³ orbit-volume equation is

\[
\boxed{\quad v''=\left(3-\frac{\rho}{2}\right)v.\quad}
\]

So the abelian equation \(v''=3v\) is replaced by

\[
v''=(3+\operatorname{Scal}(h_s))v.
\]

The Heisenberg scalar curvature subtracts from the abelian mass term. Hence there is no universal pointwise inequality \(v''\ge c v\) with \(c>0\) unless one also controls

\[
\rho<6.
\]

When \(\rho>6\), the coefficient \(3-\rho/2\) becomes \(<0\), and the nil curvature can bend \(v\) downward.

---

### Full diagonal Einstein ODE

With

\[
k_i=\frac{a_i'}{a_i},\qquad H=k_1+k_2+k_3,\qquad 
\rho=\frac{a_3^2}{a_1^2a_2^2},
\]

the full system is

\[
k_1'+Hk_1=1-\frac{\rho}{2},
\]

\[
k_2'+Hk_2=1-\frac{\rho}{2},
\]

\[
k_3'+Hk_3=1+\frac{\rho}{2},
\]

\[
H'+k_1^2+k_2^2+k_3^2=1,
\]

and

\[
\rho'=2\rho(k_3-k_1-k_2).
\]

The Hamiltonian relation is

\[
H^2-(k_1^2+k_2^2+k_3^2)=2-\frac{\rho}{2}.
\]

This also explains the cross-term issue directly:

\[
\frac{v''}{v}
=
1+2(k_1k_2+k_1k_3+k_2k_3),
\]

while the Hamiltonian relation gives

\[
2(k_1k_2+k_1k_3+k_2k_3)
=
2-\frac{\rho}{2}.
\]

Hence again

\[
\frac{v''}{v}=3-\frac{\rho}{2}.
\]

So the cross terms are not arbitrary once the full Einstein equations are imposed; they are exactly tied to the Heisenberg bracket norm \(\rho\).

---

### Invariant reduced system and circle case

The no-circle result is stronger than the raw volume equation suggests.

Let \(Z\) be the center direction and \(Q=\mathfrak n/Z\). Write

\[
z=\operatorname{tr}(L|_Z),\qquad a=\operatorname{tr}(L|_Q),\qquad H=a+z,
\]

and define

\[
D=z-a.
\]

The Heisenberg bracket norm satisfies

\[
(\log \rho)'=2D,
\]

so

\[
\rho'=2\rho D.
\]

Taking the center trace and horizontal trace of the tangential Einstein equation gives

\[
z'+Hz=1+\frac{\rho}{2},
\]

\[
a'+Ha=2-\rho.
\]

Subtracting,

\[
D'=-1+\frac{3\rho}{2}-HD.
\]

Also,

\[
H'=3-\frac{\rho}{2}-H^2.
\]

Thus the scalar subsystem is

\[
\boxed{
\begin{aligned}
H'&=3-\frac{\rho}{2}-H^2,\\
D'&=-1+\frac{3\rho}{2}-HD,\\
\rho'&=2\rho D.
\end{aligned}}
\]

Now suppose the base is a circle. The scalar \(\rho\) is periodic. At any extremum of \(\rho\),

\[
\rho'=0.
\]

Since \(\rho>0\), this gives \(D=0\). Then

\[
\rho''=2\rho D'
=2\rho\left(-1+\frac{3\rho}{2}\right)
=\rho(3\rho-2).
\]

At a maximum,

\[
\rho''\le 0
\quad\Longrightarrow\quad
\rho\le \frac23.
\]

At a minimum,

\[
\rho''\ge 0
\quad\Longrightarrow\quad
\rho\ge \frac23.
\]

Therefore a periodic \(\rho\) must satisfy

\[
\rho\equiv \frac23.
\]

Then the orbit-volume equation becomes

\[
v''=\left(3-\frac13\right)v=\frac83\,v.
\]

But \(v\) is periodic on a compact nilmanifold mapping torus: nilmanifold monodromy preserves Haar covolume. Hence

\[
0=\int_{S^1}v''\,ds
=
\frac83\int_{S^1}v\,ds,
\]

which is impossible because \(v>0\).

So:

\[
\boxed{\text{No nil}^{3}\text{ Einstein solution with }\operatorname{Ric}=-g\text{ exists over a circle base.}}
\]

This remains valid with horizontal shear. The mixed Einstein equation forces \(L\) to preserve the center line; the horizontal traceless part obeys a decoupled equation \(\Sigma'+H\Sigma=0\), while \(H,D,\rho\) still satisfy the subsystem above.

---

### Why a universal positive coefficient is absent

The exact equation

\[
v''=\left(3-\frac{\rho}{2}\right)v
\]

shows that a pointwise positive coefficient requires

\[
\rho<6.
\]

The full ODE permits local Einstein data with \(\rho>6\). For example, at one point take

\[
H=0,\qquad D=0,\qquad k_3=0,\qquad k_2=-k_1,
\]

and impose the Hamiltonian relation

\[
-2k_1^2=2-\frac{\rho}{2}.
\]

This is solvable whenever

\[
\rho>4.
\]

For \(\rho>6\), the volume coefficient is \(3-\rho/2<0\), so \(v\) has downward acceleration at that point. Thus the Heisenberg bracket can genuinely compensate the abelian \(+3v\) term.

The clean abelian inequality survives only in regimes where the nil curvature ratio is controlled, for example

\[
\rho\le 6-\varepsilon
\quad\Longrightarrow\quad
v''\ge \frac{\varepsilon}{2}v.
\]

A stronger natural regime is

\[
\rho\le \frac23,
\]

which gives

\[
v''\ge \frac83 v.
\]

---

### Interval behavior

For an interval \(I=(0,L)\), the scalar subsystem gives a useful maximum principle for \(\rho\):

- an interior local maximum of \(\rho\) must occur at \(\rho\le 2/3\);
- an interior local minimum of \(\rho\) must occur at \(\rho\ge 2/3\).

So any value \(\rho>2/3\) cannot arise as an interior peak; it must be imported from an endpoint region.

Consequences:

1. If both endpoints have controlled Heisenberg ratio with

\[
\limsup \rho<6,
\]

then \(\rho\) stays \(<6\) throughout the interval, and

\[
v''\ge c v
\]

for some \(c>0\).

2. If additionally

\[
v\to0
\]

at both finite endpoints, then such a solution cannot exist: a positive function with \(v''\ge c v>0\) cannot vanish at both ends of a finite interval.

3. Smooth central-circle collapse has

\[
\rho\to0.
\]

Indeed, near a finite endpoint where the central \(S^1\) collapses and the horizontal \(T^2\) remains of positive size, one obtains formal expansions

\[
a_1(s)=a_1(0)\left(1+\frac{s^2}{4}+O(s^4)\right),
\]

\[
a_2(s)=a_2(0)\left(1+\frac{s^2}{4}+O(s^4)\right),
\]

\[
a_3(s)=s+O(s^5),
\]

so

\[
\rho(s)=\frac{s^2}{a_1(0)^2a_2(0)^2}+O(s^4),
\qquad
v(s)=a_1(0)a_2(0)s+O(s^3).
\]

This is compatible with

\[
v''\sim 3v.
\]

Thus one finite central-collapse endpoint is locally compatible with the Einstein ODE; two such finite endpoints are ruled out by the positive volume convexity.

---

### A real mechanism allowing nil³ \(\operatorname{Ric}=-g\) metrics

There is an explicit complete ray solution: the horospherical complex-hyperbolic cusp model. With

\[
\alpha=\frac1{\sqrt6},
\]

set

\[
g
=
ds^2
+
e^{2\alpha s}(\theta_1^2+\theta_2^2)
+
\frac23 e^{4\alpha s}\theta_3^2,
\qquad
d\theta_3=\theta_1\wedge\theta_2.
\]

Then

\[
k_1=k_2=\alpha,\qquad k_3=2\alpha,\qquad H=4\alpha,
\]

\[
\rho=\frac23.
\]

The equations give

\[
k_1'+Hk_1=\frac23=1-\frac13,
\]

\[
k_3'+Hk_3=\frac43=1+\frac13,
\]

\[
k_1^2+k_2^2+k_3^2=6\alpha^2=1.
\]

Hence

\[
\operatorname{Ric}_g=-g.
\]

The volume satisfies

\[
v''=\frac83 v.
\]

Quotienting the Heisenberg fibers by a lattice gives a complete finite-volume nil cusp as \(s\to-\infty\). This model cannot be made periodic over a circle by a nilmanifold diffeomorphism, because the required return map is a genuine dilation of the Heisenberg metric rather than a volume-preserving lattice automorphism.

So the nil³ case has a clear split:

\[
\boxed{
\begin{array}{ll}
\text{circle base} & \text{impossible},\\[2mm]
\text{finite interval with two low-}\rho\text{ collapses} & \text{impossible},\\[2mm]
\text{ray/cusp geometry} & \text{exists},\\[2mm]
\text{finite endpoints with }\rho\to\infty & \text{the Heisenberg curvature can compensate }+3v.
\end{array}}
\]

The exact scientific replacement for the abelian orbit-volume equation is therefore

\[
\boxed{\quad v''=(3-\rho/2)v,\qquad \rho=|\,[\cdot,\cdot]\,|_{h_s}^2.\quad}
\]

The coefficient is positive precisely when the Heisenberg bracket norm satisfies \(\rho<6\); the full Einstein system then supplies strong one-dimensional control of \(\rho\), enough to rule out the circle case completely.