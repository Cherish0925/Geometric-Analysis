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

## Summary of the decisive computation

I worked out the full cohomogeneity‑one Einstein system for a Heisenberg (nil³) fiber over a 1D base and found that the nil³ case is **not** analogous to the abelian one, yet it is still closed on a circle base by a clean maximum‑principle barrier. The structure constant produces an exact, verifiable orbit‑volume equation with a sign‑indefinite coefficient, and that indefiniteness is controlled by a twist quantity that cannot exceed its complex‑hyperbolic value at any interior maximum. Below is the derivation, the exclusion, the genuine local model that survives (ℂH²), and the mechanism that pushes the remaining case into complex‑hyperbolic cusp geometry connected to LeBrun theory.

## The exact nil³ Einstein system

Use the orthonormal coframe $e^0=ds,\ e^i=a_i(s)\,\theta^i$ with $d\theta^1=d\theta^2=0,\ d\theta^3=\theta^1\wedge\theta^2$. Write $H_i=a_i'/a_i$, $H=H_1+H_2+H_3$, and the twist
$$
\mu=\frac{a_3}{a_1 a_2},\qquad \mu^2=\frac{a_3^2}{a_1^2 a_2^2}.
$$
Milnor's fiber Ricci eigenvalues for this frame are $r_1=r_2=-\tfrac{\mu^2}{2},\ r_3=+\tfrac{\mu^2}{2}$ (signature $(-,-,+)$, the standard Heisenberg profile). The four Einstein equations $\operatorname{Ric}=-g$ read, in the orthonormal frame,
$$
\text{(base)}\quad \sum_i \frac{a_i''}{a_i}=1,\qquad
\text{(fiber $i$)}\quad -\frac{a_i''}{a_i}-H_i(H-H_i)+r_i=-1 .
$$
Solving the fiber equations for the derivatives gives the evolution system
$$
H_1'=1-H_1H-\tfrac{\mu^2}{2},\quad
H_2'=1-H_2H-\tfrac{\mu^2}{2},\quad
H_3'=1-H_3H+\tfrac{\mu^2}{2},\quad
\frac{\mu'}{\mu}=H_3-H_1-H_2,
$$
with the base equation acting as the propagated Hamiltonian constraint
$$
\sum_{i<j}H_iH_j=1-\frac{\mu^2}{4}\quad\Longleftrightarrow\quad H^2-\sum_i H_i^2=2-\frac{\mu^2}{2}.
$$

## The generalized orbit‑volume equation (answer to (c))

Let $v=a_1a_2a_3$, so $v'/v=H$ and $v''/v=\sum_i a_i''/a_i+ (H^2-\sum_i H_i^2)$. Substituting the base equation and the trace of the fiber equations ($\sum_i r_i=-\mu^2/2$) gives, **with no symmetry assumption**,
$$
\boxed{\,v''=\Bigl(3-\tfrac{\mu^2}{2}\Bigr)v\,}.
$$
This is the exact nil³ analogue of Lott's abelian $v''=3v$. The coefficient is **not** sign‑definite: the Heisenberg curvature subtracts $\mu^2/2$ from the mass term $N=3$, and it turns negative once $\mu^2>6$. This is precisely why the abelian subharmonicity argument does not transfer, and it confirms the concern raised in the note. So the honest situation is: there is a clean generalized equation, but its coefficient can in principle change sign, so pointwise subharmonicity is not available.

## The twist barrier (the mechanism that saves the circle case)

The key new fact is that $\mu^2$ cannot climb above the complex‑hyperbolic value at any interior maximum. Set $w=H_3-H_1-H_2$, so $\mu'=\mu w$ and, from the evolution equations,
$$
w'=-1-Hw+\tfrac{3}{2}\mu^2 .
$$
At any interior local maximum of $\mu$ we have $\mu'=0$, hence $w=0$ (since $\mu>0$), and $\mu''=\mu w'=\mu(-1+\tfrac32\mu^2)\le 0$. Therefore
$$
\boxed{\ \text{at any interior local max of }\mu:\quad \mu^2\le \tfrac{2}{3}\ }.
$$
Two independent consequences follow immediately.

**Circle base is impossible.** On a circle $\mu$ is smooth, positive, and attains an interior maximum, so $\mu^2\le 2/3$ everywhere. Then either route closes it:
- $H^2\ge 2-\mu^2/2\ge 5/3>0$ everywhere, so $H$ never vanishes and has fixed sign; $v=\exp\!\int H$ is strictly monotone and cannot be periodic.
- Equivalently, $v''=(3-\mu^2/2)v\ge \tfrac{8}{3}v>0$, so $\int_{S^1}v''=\int_{S^1}(3-\mu^2/2)v>0$ contradicts $\int_{S^1}v''=0$.

This gives a complete, decisive exclusion of nil³ negative Einstein collapse over a circle base, on the same footing as the abelian case, but through a maximum principle rather than pointwise subharmonicity.

**Interval base with two collapse ends is impossible.** Wherever $\mu^2\le 2/3$ the function $v$ is strictly convex; a positive convex function cannot vanish at both endpoints (its graph lies under the zero chord). So a symmetric double cusp is excluded, and any interval solution must be monotone in $v$, with the twist growing monotonically toward at most one end.

## The genuine local model that survives: ℂH²

Nil³ negative Einstein metrics do exist, and the barrier is saturated exactly by one solution. The fixed point of the evolution system is
$$
H_1=H_2=\tfrac{1}{\sqrt6},\quad H_3=\tfrac{2}{\sqrt6},\quad \mu^2=\tfrac23,
$$
i.e. $a_1=a_2=e^{s/\sqrt6},\ a_3=\sqrt{2/3}\,e^{2s/\sqrt6}$, giving $v=\sqrt{2/3}\,e^{4s/\sqrt6}$ and $v''=\tfrac83 v$ (consistent with $3-\mu^2/2=8/3$). All four Einstein equations check exactly. This is the complex hyperbolic plane $\mathbb{C}H^2$ in horospherical form: $\mathbb{C}H^2=\mathbb{R}\ltimes \mathrm{Heis}^3$ is the Iwasawa solvmanifold $AN$ of $SU(2,1)$, Kähler–Einstein with negative Einstein constant. The barrier value $\mu^2=2/3$ is exactly the twist of $\mathbb{C}H^2$; it is the marginal orbit where $w\equiv0$.

Consequence: nil³ cannot be excluded by any purely local pointwise argument, because $\mathbb{C}H^2$ is a complete bounded‑curvature negative Einstein manifold whose nil³ orbits collapse ($v\to0$ as $s\to-\infty$). This is genuine CFG bounded‑curvature collapse, so a nil³ chart modeled on the $\mathbb{C}H^2$ end is an admissible limit germ. The exclusion for the fixed Ishida–LeBrun manifolds must therefore engage the interval/cusp case globally, not locally.

## Where this drives the remaining case, and the lever against it

The interval case is now sharply reduced. Since interior maxima of $\mu$ are bounded by $2/3$, an interval solution has $v$ strictly convex until $\mu^2$ climbs monotonically toward one end, where exactly two things can happen:
1. $\mu^2\to 2/3$ and the solution asymptotes to the $\mathbb{C}H^2$ fixed point — a genuine complex‑hyperbolic cusp with $v\to0$; or
2. $\mu^2\to\infty$ — curvature blows up and the chart leaves the bounded‑curvature region (a curvature‑concentration point, at most $\mathcal N(\chi)$ of them).

Two levers act on case 1. First, a convex positive $v$ attains its maximum at an endpoint; the opposite end where $v\to\infty$ has **large** fibers, i.e. it is not collapsed. But Step 6 established everywhere unit‑scale collapse ($\sup_p\operatorname{Vol}B_1(p)\to0$). So the large‑$v$ end of any nil³ chart cannot persist inside the regular region — it must be truncated at a curvature‑concentration point or at another chart before $v$ grows. This forces nil³ charts to be short, monotone, small‑$v$ segments whose turning is only possible at the finitely many curvature‑blowup strata, giving a covering/combinatorial constraint tied to $\mathcal N(\chi)$.

Second, a $\mathbb{C}H^2$ cusp carries a definite curvature energy budget. As a Kähler–Einstein surface, $\mathbb{C}H^2$ has $W^-=0$ and $|W^+|^2$ pinned to the scalar curvature, so a cusp neighborhood contributes fixed amounts to $\int|\!\operatorname{Rm}|^2$, to $\chi$, and to $\sigma$. These are exactly the quantities LeBrun's estimates and the Ishida–LeBrun critical relation $D=A/3$ control. The natural decisive comparison is: sum the Gauss–Bonnet and signature contributions of the (finitely many) curvature‑blowup strata plus the nil³/abelian regular pieces, and test them against the fixed $\chi,\sigma$ and the volume $32\pi^2 A/9$. A complex‑hyperbolic cusp appearing in the limit signals the manifold is degenerating toward a complex‑hyperbolic orbifold with a compactifying divisor (Hirzebruch–Mumford picture), which carries its own $\chi,\sigma$ that must be reconciled with the fixed topology.

There is also a coarse global cross‑check. A closed nil³‑bundle over $S^1$ has $\chi=0$ (fiber‑bundle multiplicativity over $S^1$), whereas negative Einstein forces $\chi=\frac{1}{8\pi^2}\int(|W|^2+s^2/24)>0$. So the fully global circle scenario is topologically obstructed independently; only the cusp/interval local models can matter, and those must attach to the curvature budget.

## What would make the interval/cusp exclusion decisive

Three concrete pieces of work would settle case 1. (i) Linearize the reduced (constraint‑restricted) system at the $\mathbb{C}H^2$ fixed point to determine whether it is an attracting cusp for generic orbits or a saddle; the eigenvalues of the $2\times2$ reduced Jacobian at $(x,y,\nu)=(1/\sqrt6,2/\sqrt6,2/3)$ decide whether nearby nil³ ends necessarily converge to the complex‑hyperbolic cusp or generically miss it (running into $\mu^2\to\infty$ curvature blowup). (ii) Integrate the volume form $\int v\,ds$ over a monotone convex segment to get the exact volume a single nil³ chart can contribute for given endpoint fiber scales, then bound the number of charts by $\mathcal N(\chi)$ and test against $32\pi^2A/9$. (iii) Compute the Gauss–Bonnet and signature integrands on the $\mathbb{C}H^2$ cusp explicitly (they are elementary since $\mathbb{C}H^2$ is symmetric) and compare with the Ishida–LeBrun budget at $D=A/3$.

## Cross‑field sources to pull in

The exact solution and dynamics are the well‑studied "Einstein solvmanifold" and Bianchi‑II cosmological system: Heber's structure theory of noncompact homogeneous Einstein spaces, Lauret's work on nilsoliton/Einstein solvmanifolds, and Milnor's curvature formulas for left‑invariant metrics give the Ricci and the fixed‑point classification. Anderson's and Bamler's analyses of complex‑hyperbolic cusp ends of finite‑volume Einstein four‑manifolds, and LeBrun's curvature/volume estimates for Einstein metrics on complex surfaces (including the Hirzebruch–Mumford compactification of complex‑hyperbolic cusps), are the right sources for the cusp‑energy comparison. The Bianchi‑II Einstein ODE with a positive constant is also treated in the cohomogeneity‑one Einstein literature (Böhm; Page–Pope), which contains phase‑portrait techniques directly applicable to the linearization in (i).

## Verification and formalization notes

The identity $v''=(3-\mu^2/2)v$, the constraint $H^2-\sum H_i^2=2-\mu^2/2$, and the barrier inequality $\mu^2\le 2/3$ at interior maxima are all algebraic consequences of the four Einstein equations plus one differentiation; they are self‑contained and independently reproducible symbolically (the existing `investigate_nil3_negative_einstein.py` can be extended to verify $w'=-1-Hw+\tfrac32\mu^2$ and the ℂH² fixed‑point data). The circle exclusion is a short lemma (positive‑coefficient ODE with a periodic positive solution is impossible), well suited to Lean formalization once the ODE identities are in place: state $v>0$, $v\in C^2(S^1)$, $\mu^2\le 2/3$ on $S^1$, and $v''=(3-\mu^2/2)v$, then derive the contradiction from $\int_{S^1}v''=0$. The barrier lemma is a standard second‑derivative test at an interior maximum and formalizes cleanly. The one input requiring a cited source rather than internal derivation is Milnor's fiber Ricci eigenvalues $(-\mu^2/2,-\mu^2/2,+\mu^2/2)$ for the Heisenberg left‑invariant metric; that is the single external fact the whole nil³ analysis rests on, and it is verified indirectly here by the exact ℂH² solution satisfying all four equations.