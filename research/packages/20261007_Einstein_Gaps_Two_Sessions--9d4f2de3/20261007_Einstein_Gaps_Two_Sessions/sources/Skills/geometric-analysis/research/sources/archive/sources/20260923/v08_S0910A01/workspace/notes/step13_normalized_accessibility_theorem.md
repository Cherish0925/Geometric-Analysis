# Step 13: Normalization-invariant circle reduction and the accessibility bootstrap

**Step 14 correction.**  Sections 3--7 below are historical route-building and contain withdrawn inferences.  Current use: the normalization-invariant reduction and the chiral formulas remain valuable, but staticity does not imply \(H\ge0\), \(H\ge0\) would not by itself give a sequence-uniform volume anchor, positivity/continuity of \(v\) gives only metric-dependent lower bounds, and the complete bootstrap was not proved.  The current route comparison is `workspace/notes/step14_smoothing_vs_reduction_route.md`: localized Ye Li smoothing at a fixed small radius should be evaluated alongside the reduced-system reconstruction problem.

Session S0910A01, Agent2/Constructor, Execute.

## 1. Purpose

This note develops the Strategist's observation that the collapse parameter
disappears from the local geometry after normalization, and combines it with
A03's fiber survival dichotomy to formulate a period-independent accessibility
argument.  The two main results are:

1. **Normalization-invariant reduction** (Section 2): verified symbolic curvature
   dictionary for the local fields (g_B, v, F_B) that control the lifted geometry.

2. **Accessibility bootstrap** (Section 4): a cascading interior-regularity
   argument whose constants are independent of the fiber period, potentially
   closing both branches of A03's dichotomy.

## 2. Normalization-invariant rank-one reduction

### Setting

Let $g = g_B + \ell^2(d\psi + A)^2$ on a domain in $M^4$ with a free
isometric circle action.  Fix a base point $p$ and set
$$
z = \ell(p)\psi, \qquad v = \frac{\ell}{\ell(p)}, \qquad B = \ell(p) A.
$$
Then on the cover where $z$ is unwrapped to $\mathbb R$,
$$
g = g_B + v^2(dz + B)^2, \qquad v(p) = 1.
$$
The absolute collapse parameter $\ell(p)$ has disappeared from all local
metric coefficients.  It remains only in the fiber period $2\pi\ell(p)$.

The invariant local data at $p$ in an orthonormal base frame
$(e_0, e_1, e_2)$ with $e_3 = v^{-1}\partial_z$ is:
- $u_a = \nabla_a \log v$ (fiber gradient, 3 components);
- $h_{ab} = \nabla_a\nabla_b \log v$ (Hessian of $\log v$, symmetric, 6 components);
- $C_{ab} = v\,(dB)_{ab}$ (scaled twist, antisymmetric, 3 components);
- $\nabla_c C_{ab}$ (derivative of scaled twist, 9 components with 1 closure
  relation);
- $\operatorname{Ric}^B_{ab}$ (base Ricci, symmetric, 6 components).

### Verified formulas (from `step13_rank1_reduction.py`)

**Closure identity:** $d(de^3) = 0$ gives
$$
\nabla_0 C_{12} - \nabla_1 C_{02} + \nabla_2 C_{01}
= C_{01}u_2 - C_{02}u_1 + C_{12}u_0.
$$

**Vertical Einstein equation** ($\operatorname{Ric}(e_3,e_3) = -1$):
$$
\operatorname{tr}(h) + |u|^2 = 1 + \frac{|C|^2}{2},
$$
where $|C|^2 = \sum_{a<b}C_{ab}^2$.  In A03's notation
$h^{A03} = \operatorname{Hess}(\ell)/\ell = h + u\otimes u$:
$$
\operatorname{tr}(h^{A03}) = \frac{\Delta v}{v}
= 1 + \frac{|C|^2}{2}.
$$
The factor $|C|^2/2$ matches A03's $\ell^2 F_{ab}F^{ab}/4$ under the
standard convention $F_{ab}F^{ab} = 2\sum_{a<b}F_{ab}^2$.

**Mixed Einstein equations** ($\operatorname{Ric}(e_a, e_3) = 0$):
$$
\operatorname{div}_B(v^2 F_B) = 0 \quad\Leftrightarrow\quad
\sum_b \nabla_b(v C_{ab}) + 2\sum_b u_b C_{ab} = 0.
$$
Combined with $dF_B = 0$ (Bianchi identity for the connection curvature),
$v^2 F_B$ is a **weighted harmonic** 2-form on the base.

**Horizontal Einstein equations** ($\operatorname{Ric}(e_a,e_b) = -\delta_{ab}$):
$$
\operatorname{Ric}^B_{ab} = -\delta_{ab} + h_{ab} + u_a u_b
+ \frac{1}{2}\sum_c C_{ac}C_{bc}.
$$
In 3 dimensions, $\operatorname{Ric}^B$ determines the full curvature of the
base:
$$
\operatorname{Rm}^B = \operatorname{Ric}^B \wedge g_B
- \frac{s_B}{2}\, g_B \wedge g_B.
$$

### Verified static formula

In the static limit ($C = 0$, $u = 0$), with diagonal Hessian
$h = \operatorname{diag}(h_0,h_1,h_2)$, $\operatorname{tr} h = 1$, and
$\operatorname{Ric}^B = h - I$, the script confirms
$$
\boxed{
W^+ = \operatorname{diag}\!\left(\frac13 - h_2,\;\frac13 - h_1,\;
\frac13 - h_0\right),
\qquad
\operatorname{Spec}(W^+) = \left\{\frac13 - \eta_i\right\}.
}
$$
This verifies A03's corrected Proposition.  The only constant-eigenvalue
static Einstein metric compatible with any given $W^+$ spectrum is
$h = \frac13 I$, giving $W^+ = 0$ (real hyperbolic space with $K = -1/3$).

### Twist correction

The twist modifies $W^+$ through terms involving $C_{ab}$, $u_a$, $\nabla_c C_{ab}$,
and their products.  The correction is **nonzero**: diffuse non-basic mixed
curvature can change $W^+$ eigenvalues away from the static values.  The full
symbolic formulas are in the script.  In particular, the twist correction to
the diagonal entries involves the cross terms $C_{ab}u_c$ and $\nabla_c C_{ab}$,
confirming that both the scaled twist amplitude AND its gradients participate.

## 3. A03's fiber survival dichotomy (stated precisely)

On the calibrated good set of a hypothetical near-critical sequence, at each
point one of two alternatives holds:

**(S) Fiber survival:** The circle fiber has $\ell(p) \ge c_0 > 0$ (or more
precisely, a buffered normal cover unwraps the fiber at a fixed scale).
Then the cover is noncollapsed and the forbidden calibrated Einstein germ
(Derdziński) applies.  Contradiction.

**(D) Fiber death with high twist:** The fiber contracts within every fixed
buffer scale, but the static incompatibility forces $\ell^2|F|^2 = |C|^2 \ge c > 0$
on a definite fraction of the region; otherwise $W^+ \to 0$ (isotropic),
contradicting the calibrated deficit bound $|W^+|^2 \to 1/24$.

## 4. The normalization-invariant accessibility bootstrap

**Key observation (Strategist):** In case (D), the local geometry of the
cover metric $g = g_B + v^2(dz + B)^2$ is determined by $(g_B, v, F_B)$
with $v(p) = 1$.  The fiber period $2\pi\ell(p) \to 0$ appears nowhere in
these coefficients.  The reduced Einstein equations are
period-independent.

**Theorem (conditional on the energy-to-$L^2$ passage).**
*Fix $r > 0$, $\Lambda > 0$, $c_0 > 0$.  There exist $h_0 > 0$
and $Q_0 > 0$, depending only on $r$, $\Lambda$, $c_0$, and dimension, such
that the following holds.  If*
- *$(B^3, g_B, v, F_B)$ satisfies the reduced Einstein system with error
  $\delta$ on $B_r(p) \subset B$, with $v(p) = 1$;*
- *the 3D curvature energy satisfies
  $\int_{B_r(p)} |\operatorname{Rm}^B|^2 + |\nabla v/v|^2 + v^2|F_B|^2 \le \Lambda$;*
- *the scaled twist satisfies $|C(p)|^2 = v(p)^2|F_B(p)|^2 \ge c_0$;*

*then the lifted metric $\hat g = g_B + v^2(dz+B)^2$ admits a harmonic chart
of radius $\ge h_0$ with $C^{1,\alpha}$ control $\le Q_0$ on the 4D cover,
centered at a lift of $p$, for $\delta$ sufficiently small.*

### Bootstrap proof sketch

**Step 1 (Weighted harmonic form ⟹ $L^\infty$ twist).**
$F_B$ is closed ($dF_B = 0$) and $v^2 F_B$ is approximately co-closed
($\delta_B(v^2 F_B) \approx 0$).  On the base ball $B_r(p)$, with the $L^2$
energy bound $\int |F_B|^2 \le \Lambda/c_0$ (from the energy hypothesis and
$v \ge c_0^{1/2}$), weighted elliptic theory for the approximate
$v^2$-Hodge Laplacian gives
$$
\sup_{B_{r/2}} |F_B| \le C_1(\Lambda, c_0, r).
$$

**Step 2 (Eigenfunction equation ⟹ Harnack for $v$).**
The vertical equation is $\Delta_B v = v(1 + |C|^2/2) + O(\delta)$.
Write $q(x) = 1 + v(x)^2|F_B(x)|^2/2$.  From Step 1, $q$ is bounded on
$B_{r/2}$, so the equation $\Delta v = qv + O(\delta)$ has a Harnack
inequality:
$$
\sup_{B_{r/4}} v \le C_H \inf_{B_{r/4}} v, \qquad
|\nabla \log v| \le C_H / r \quad \text{on } B_{r/4}.
$$
Since $v(p) = 1$, this gives $c_2 \le v \le C_2$ on $B_{r/4}$ with
$c_2, C_2$ depending only on $C_1$ and $r$.

**Step 3 (Base Ricci control ⟹ 3D harmonic radius).**
From the horizontal equation and Steps 1–2:
$$
|\operatorname{Ric}^B| \le 1 + |h| + |u|^2 + |C|^2/2
\le 1 + C_1^2 + C_H^2/r^2 + C_1^2/2 \eqqcolon R_3
$$
on $B_{r/4}$.  In dimension 3, bounded Ricci implies bounded full curvature.
By the local Cheeger–Gromov theorem in 3D, the harmonic radius of $g_B$ on
$B_{r/8}$ is bounded below by $h_B(R_3, r) > 0$.

**Step 4 (4D harmonic chart from base chart + fiber).**
In the base harmonic chart $(x^1, x^2, x^3)$ on $B_{h_B}(p)$,
the base metric $g_B$ is $C^{1,\alpha}$ with controlled constants.  The
fiber coordinate $z$ satisfies $\Delta_4 z = 0$ exactly (since $\partial_z$
is Killing on the cover).  Therefore $(x^1, x^2, x^3, z)$ is a coordinate
chart for the 4D metric, and
$$
\hat g_{ij} = g_{B,ij} + v^2 B_i B_j, \quad
\hat g_{i4} = v^2 B_i, \quad
\hat g_{44} = v^2.
$$
The entries are $C^{1,\alpha}$ by the $C^{1,\alpha}$ control of $(g_B, v, B)$
from Steps 1–3 and gauge choice.  The chart has radius $\ge h_0 = h_B/2$ and
control $Q_0 = Q_0(R_3, h_B)$.

**Step 5 (Forbidden germ).**
The controlled chart from Step 4 is a *supplied harmonic chart* in the sense
of the Step 8–11 chart-accessible exclusion mechanism.  The forbidden
calibrated Einstein germ (Derdziński + finite-$p$ $W^{2,p}$ convergence)
then produces a smooth Einstein limit on the chart with the calibrated $W^+$
spectrum, which is locally Kähler and contradicts
$|W^+|^2 = 1/24 \ne 2/3$.

### Consequence

If the energy-to-$L^2$ passage holds (i.e., the 4D curvature energy on
a cover ball maps to controlled 3D energy on the base ball), **both**
branches of A03's dichotomy lead to a contradiction:
- **(S)** directly produces the forbidden germ.
- **(D)** the normalization removes $\ell(p)$, the bootstrap gives a chart,
  and the same forbidden germ applies.

## 5. Corrections from A03 Step 12

A03's Step 12 note (`step12_reduced_equations_accessibility.md`) corrects
three assumptions in the original bootstrap:

### (a) H²×H² counterexample to general static rigidity

The product $H^2 \times H^2$ with the circle in polar coordinates has
$\operatorname{Spec}(H) = (1, 0, 0)$ and constant $W^+ = (-2/3, 1/3, 1/3)$.
This is NOT $W^+ = 0$.  Therefore "only $W^+ = 0$ is compatible with constant
static spectrum" was proved only in the cohomogeneity-one ansatz (A03's Step 11
ODE argument), not in general.  The Derdziński forbidden-germ obstruction
(open-set Einstein rigidity) remains the correct general tool.

### (b) Chiral factorization

A03 identifies the correct reduced structure.  With $a_\pm = u \mp z/2$:
$$
W^\pm = -[\operatorname{sym}\nabla a_\pm + a_\pm \otimes a_\pm]_0,
$$
$$
da_+ = a_+ \wedge a_-, \qquad da_- = -a_+ \wedge a_-.
$$
This is a coupled chiral Riccati--Maurer--Cartan system.  The calibrated $W^+$
constrains $a_+$ through a nonlinear first-order equation; bounded curvature
constrains both $a_+$ and $a_-$.  Large $u$ and $z$ can cancel in $a_+$ while
surviving in $a_-$, creating a derivative-twist mechanism invisible to the
calibrated defect.

### (c) Weighted vs ordinary base Ricci

The four-dimensional Ricci bound $\operatorname{Ric}_g \ge -3g$ descends to
the weighted bound
$$
\operatorname{Ric}^4_{q,\ell} = \operatorname{Ric}_B - H \ge -g_B
$$
on the three-dimensional base quotient (Galaz-García et al.).  This gives
$\operatorname{RCD}(-1, 4)$ structure: doubling, Poincaré, and heat-flow
regularity in the weighted sense.

The **ordinary** base Ricci is $\operatorname{Ric}_B = -I + H + \frac12
C^2_{\operatorname{sym}}$.  This is NOT bounded above by a fixed constant
because $H$ and $C^2$ can be large.  My Step 3 in the bootstrap (base harmonic
radius from bounded ordinary Ricci) was therefore too strong.

### (d) Calibrated H-spectrum and twist

The static formula gives $\operatorname{Spec}(W^+) = \{1/3 - \eta_i\}$
only when $B = 0$ (no twist).  With twist, $W^+ = E + B$ and the relationship
between $H$-eigenvalues and $W^+$-eigenvalues changes.  The observation that
the calibrated $H = (1/2, 1/4, 1/4)$ has $\operatorname{tr} = 1$, hence
$|C|^2 = 0$, is valid ONLY in the static case.  Near-calibrated metrics with
small twist defect need not have small twist.

## 6. Revised accessibility argument: what survives

### The normalization is valid

The Strategist's observation is **not** affected by A03's corrections: the
local metric $g = g_B + v^2(dz + B)^2$ with $v(p) = 1$ has all coefficients
independent of $\ell(p)$.  This is a coordinate-free fact.  The reduced
Einstein equations in the variables $(g_B, v, F_B)$ are period-independent.

### The bootstrap gap

The specific gap is at Step 3: obtaining a 3D harmonic radius on the base.
This requires $|\operatorname{Ric}_B| \le R_3$ on a fixed ball.  The
available bound is $\operatorname{Ric}_B - H \ge -I$ (weighted), but
$\operatorname{Ric}_B$ itself can be large.

On the **calibrated bulk**, the $W^+$ eigenvalue constraint limits the
combination $E + B$.  If $|B|$ is controlled (twist gradient bounded), then
$E$ is constrained, which bounds $H$ (since $E = \kappa/3\,I - H + \text{twist
quadratic}$).  This would give $\operatorname{Ric}_B$ bounded.

But the control on $|B|$ requires $|\nabla z|$ bounded, which depends on the
quotient geometry.  This is circular unless we can find an external estimate.

### Cover noncollapse: partial result

If the calibrated conditions force $H \ge 0$ on most of the calibrated volume
(i.e., $\operatorname{Hess}(\ell)/\ell \ge 0$), then
$\operatorname{Ric}_B \ge -I$, giving a 3D Bishop--Gromov volume lower bound.
Combined with the fiber extent on the cover, this gives 4D noncollapse.

In the static case ($C = 0$), $H$ has eigenvalues $(1/2, 1/4, 1/4) \ge 0$ at
the calibrated profile, so this holds.

With twist, the eigenvalues of $H$ can shift, but the trace is
$\operatorname{tr} H = 1 + |C|^2/2 \ge 1 > 0$.  Whether all eigenvalues
remain nonneg on the calibrated bulk requires analysis of the constrained system.

## 7. The energy-to-$L^2$ passage (original Section 5, revised)

The remaining analytical gap is Step 1's hypothesis: controlled 3D $L^2$
energy on the base ball.

On the 4D cover, a ball of radius $r$ centered at a lift $\hat p$ of $p$
has volume form $dV_4 = v\, dV_3 \wedge dz$.  With $v(p) = 1$ and $v$
bounded on $B_{r/4}^{3D}$ (by Step 2, once established), the fiber extent in
the 4D ball is $\Theta(r)$.  Therefore
$$
\int_{B_r^{4D}(\hat p)} |\operatorname{Rm}|^2\, dV_4
\ge c\, r \int_{B_{r/4}^{3D}(p)} |\operatorname{Rm}^{3D}|^2\, dV_3,
$$
where $|\operatorname{Rm}^{3D}|^2$ includes $|\operatorname{Rm}^B|^2$,
$|\nabla v/v|^2$, $v^2|F_B|^2$, and mixed terms.

The 4D energy on a random good ball is controlled by the Noether energy
bound and volume averaging (Step 11): $\fint |\mathcal{R}|^2 \le 12$ in
the adopted convention.

**However**, this passage is only valid AFTER $v$ is known to be bounded,
creating a circular dependence with Step 2.  Breaking the circle requires
either:

(a) A **direct $L^2$ bound** on $F_B$ on the base ball from the 4D energy,
without first controlling $v$.  This may follow from the representation of
the 4D curvature in terms of the reduced fields: the component
$\operatorname{Rm}(e_a, e_3, e_b, e_3) = -h_{ab}^{A03}$ is directly the
Hessian of the fiber function, whose trace is $1 + |C|^2/2$.  Integration
of $|\operatorname{Rm}|^2$ over the fiber gives a fiber-averaged bound on
$|h^{A03}|^2 + |C|^2 + \ldots$ without needing $v$ bounded.

(b) A **Moser iteration** argument directly on the 4D eigenfunction equation
$\Delta_4 \ell = (1 + \ell^2|F_A|^2/4)\ell$ (with error $O(\delta)$),
using only the 4D volume doubling and Sobolev constants from the Ricci
lower bound.

(c) An **a priori maximum principle** for $v$ from the sign of the
eigenfunction equation: $\Delta v = v(1 + |C|^2/2) > 0$ implies $v$ is
strictly subharmonic at $v = 1$ when $|C| > 0$.  By the maximum principle,
$v$ cannot have a local max at the center.  Combined with the normalization
$v(p) = 1$, this gives an *upper* bound on $v$ in terms of boundary data.
The lower bound then follows from the Harnack inequality for the equation.

Route (c) appears most promising for a self-contained argument.  The
subharmonicity of $v$ forces $\inf_{\partial B_r} v \ge v(p) = 1$ or
$v$ increases toward the boundary.  But $v > 0$ everywhere (since $\ell > 0$
on the free-circle domain), and the Harnack inequality for $\Delta v = qv$
with $q > 0$ and $v > 0$ gives two-sided control.

## 6. The vertical equation and regularity

Write the vertical equation as
$$
\Delta_B v - v = \frac{v^3|F_B|^2}{2} + O(\delta\, v)
= \frac{|C|^2 v}{2} + O(\delta\, v).
$$
Since $v > 0$ and $|C|^2 \ge 0$, the operator $L v = \Delta v - v$ is
bounded below by $0$ (the RHS is nonneg).

For $\Lambda = 1 + |C(p)|^2/2 \ge 1$ at the center, the equation
$\Delta v = \Lambda v$ at the center has the local behavior
$v(x) \approx 1 + \Lambda|x|^2/(2n) + \ldots$, showing $v$ increases
away from the center.

The key estimate: the Harnack inequality for $-\Delta v + c(x)v = 0$
with $c(x) = -(1 + v^2|F_B|^2/2) < 0$ and $v > 0$ gives, on $B_r(p)$
with controlled $c$:
$$
\frac{\sup v}{\inf v} \le C_H(r, \sup|c|).
$$
Combined with $v(p) = 1$, this pins $v$ between $C_H^{-1}$ and $C_H$.

The bottleneck: $\sup |c|$ depends on $v^2|F_B|^2$.  If we can bound
$|F_B|$ on a slightly smaller ball FIRST, then the Harnack follows.  The
harmonic-form argument of Step 1 requires $v$ bounded... but only from
below ($v \ge c > 0$), which follows from $v > 0$ plus subharmonicity of
$v$ (no zeros in the interior).

Therefore the bootstrap can be initiated:
1. $v > 0$ (fiber free circle action) ⟹ $v \ge c_3$ on any compact subset
   by continuity and $v(p) = 1$;
2. $|F_B|$ bounded in $L^\infty$ on a smaller ball by weighted-harmonic
   elliptic theory;
3. Harnack for $v$ on a still smaller ball;
4. Ric^B control, base harmonic radius, 4D chart.

The first step requires only that $v$ is CONTINUOUS and POSITIVE on the
base domain, not that it is bounded.  Since $v = \ell/\ell(p)$ and $\ell$
is a smooth positive function on the free-circle domain, this is automatic.

## 7. Consequence for the negative branch

If the bootstrap in Section 4 succeeds, both branches of the fiber survival
dichotomy produce a forbidden calibrated Einstein germ on the cover, giving:

**Volume vanishing:** On a hypothetical near-critical sequence
$(M_i, g_i)$ in the LeBrun laboratory with $\delta_i \to 0$, the set of
rank-one collapsing good points has vanishing volume proportion:
$$
\frac{\operatorname{Vol}\{p : p \text{ is rank-one circle-collapsing and good}\}}
     {\operatorname{Vol}(M_i)} \to 0.
$$

Combined with the Step 8 measure-local theorem (noncollapsed good points
also have vanishing proportion) and the diffuse Pontryagin density (basic
collapse excluded), the remaining question is: can the near-critical
sequence evade all these mechanisms through
- rank-two or higher collapse;
- non-circle fiber degeneration (NUT-type);
- singular fibers or degenerate base geometry;
- curvature concentration preventing the energy averaging.

## 8. Remaining gaps and next work

1. **Completing the bootstrap (Step 1):** The weighted harmonic form argument
   needs the precise Hodge Laplacian for $v^2$-weighted 2-forms on a 3D ball
   with Ricci bounds.  Standard references cover $v = 1$; the variable weight
   requires adaptation.

2. **Non-circle degeneration:** Near a NUT, $\ell(x) \to 0$ and the circle
   action is NOT free.  The reduction breaks down.  The accessibility
   bootstrap applies only to the free-circle domain, not at the NUT itself.
   Taub-NUT-AdS shows that NUT-containing large balls can have collapsed
   covers.  The remaining question is whether the NUT point density is
   $o(\operatorname{Vol})$.

3. **Rank-two collapse:** For $T^2$-invariant collapse, A02's toric determinant
   equations provide the analogue of the normalized vertical equation
   ($\Delta_B w = (|F|^2/2 + 2)w$).  The bootstrap should extend to this
   case with the orbit-volume function $w = \sqrt{\det h}$ replacing $v$.

4. **Energy averaging:** The Noether bound gives global mean $|\mathcal R|^2
   \le 12$, but the passage to base-ball $L^2$ energy requires care about the
   fiber-averaging step.

5. **Higher dimensions:** The 3D base regularity (Ricci ⟹ full curvature)
   is special to dimension 4.  Higher-dimensional reductions need different
   arguments.

## 9. Curvature operator sign correction

The Step 12 exponential-twist script (`step12_rank1_exp_twist_metric.py`)
has a curvature-operator indexing error: `R6[I,J] = R[a,b,d,c]` instead of
`R[a,b,c,d]`, negating the curvature operator.  The Step 12 W+ eigenvalues
$(-7/6, -7/6, 13/3)$ at $u=1, C=2$ correspond to $-W^+_{\rm correct}
+ (2/3)I_3$, not to $W^+$.  The correct eigenvalues (from the current
reduction script) are $(-11/3, 11/6, 11/6)$.  This affects only the
non-Einstein numerical test; all Einstein conclusions (Taub-NUT-AdS,
Derdziński) remain valid because W+ vanishes or the sign error is
orientation-dependent.

## Files

- `workspace/scripts/step13_rank1_reduction.py` — the verified reduction
  script.
- `workspace/notes/step13_normalized_accessibility_theorem.md` — this note.
- A03 `workspace/notes/step11_circle_reduction_anisotropy_and_fiber_survival.tex`
  — the fiber survival dichotomy.
- A02 `workspace/notes/step13_preceptor_toric_spectral_review.md` —
  toric spectral anchors.
