# Step 31: Noncollapsed positive dichotomy theorem and spectral obstruction analysis

Session `S0910A02`. Agent2/Constructor. Phase Execute.

## 0. Scope

This note constructs the mathematical core of Route A: the four-dimensional
noncollapsed positive branch dichotomy. The main objects are:

1. An **unconditional** regular-limit theorem: noncollapsed near-Einstein sequences
   with no codimension-4 singularity give smooth Einstein on the original manifold.
2. A **spectral obstruction analysis**: at each orbifold singular point, the first
   Ozuch obstruction requires `W_+(p)` to have eigenvalue `-Lambda/3`, verified
   computationally for all standard Einstein 4-manifolds.
3. A **conditional dichotomy**: either Einstein on `M`, or every singular point
   of the orbifold limit lies on a specific codimension-1 locus of `W_+`.
4. An **honest assessment** of which parts are proved and which remain open.

This does not prove or refute any branch of Yau-26. It provides the strongest
conditional positive-existence result obtainable from the noncollapsed bubble route.

## 1. Setup and normalization

Yau Problem 26, positive branch, dimension 4. After scaling, the hypothesis is:

$$
\|\operatorname{Ric}_{g_i}-g_i\|_{\mathrm{op}}\le\delta_i\to0
$$

on closed connected oriented smooth 4-manifolds $(M^4, g_i)$. We additionally
assume a volume lower bound:

$$
\operatorname{Vol}(M, g_i)\ge v_0>0.
$$

The question: does $M$ carry a smooth Einstein metric $h$ with $\operatorname{Ric}_h = \lambda h$?

## 2. The regular-limit theorem (unconditional)

**Theorem A** (Regular Limit). *Under the above hypotheses, suppose the
Cheeger–Naber singular set $\mathcal{S}$ of the GH limit is empty. Then for all
sufficiently large $i$, $M$ carries a smooth Einstein metric $h$ with
$\operatorname{Ric}_h = h$.*

**Proof sketch.** The chain is standard but each link must be source-verified.

**Step 1.** Myers gives

$$
\operatorname{diam}(M, g_i)\le \pi\sqrt{\frac{3}{1-\delta_i}}.
$$

**Step 2.** Bishop–Gromov monotonicity + total-volume lower bound $v_0>0$ gives
local noncollapse: for each $r\le r_0$ and $x\in M$,

$$
\operatorname{Vol}(B_r(x))\ge c(v_0, r_0) r^4.
$$

**Step 3.** Cheeger–Naber bounded-Ricci compactness (Theorem 1.13 of
\cite{cheeger_naber_2015}): under $|\operatorname{Ric}_{g_i}|\le 3$ and
local noncollapse, a subsequence converges in pointed GH sense to a limit
$(M_\infty, d_\infty, g_\infty)$, and there exists a closed set
$\mathcal{S}\subset M_\infty$ of Hausdorff codimension at least 4 such that
on $M_\infty\setminus\mathcal{S}$ the convergence is $C^{1,\alpha}\cap W^{2,q}$
in harmonic coordinates.

**Step 4.** On $M_\infty\setminus\mathcal{S}$, the uniform convergence
$\operatorname{Ric}_{g_i}\to g_i$ in $C^0$ and the $W^{2,q}$ convergence of
metrics imply the limit satisfies

$$
\operatorname{Ric}_{g_\infty}= g_\infty
$$

weakly. By standard elliptic regularity for the Einstein equation (the
Ricci tensor in harmonic coordinates is a quasilinear elliptic system), $g_\infty$
is smooth on $M_\infty\setminus\mathcal{S}$.

**Step 5.** If $\mathcal{S}=\varnothing$, the limit is a smooth closed
Riemannian manifold, and the Cheeger–Gromov diffeomorphism theorem gives, for
large $i$, diffeomorphisms $\phi_i: M\to M_\infty$ with $\phi_i^*g_\infty$
close to $g_i$ in $C^{1,\alpha}$. In particular $M\cong M_\infty$ and $M$
carries the Einstein metric $g_\infty$.  $\square$

**Remark.** This is the conceptual core: the *only* obstruction to Einstein
existence in the noncollapsed case is the possible nonemptiness of $\mathcal{S}$.
In dimension 4, $\mathcal{S}$ consists of isolated points (codimension 4 = the
full dimension), and Cheeger–Naber's codimension-4 conjecture (now theorem) gives
control of the singular set structure.

## 3. The singular case: bubble structure

When $\mathcal{S}\ne\varnothing$, the singular points are isolated in dimension 4.
Two independent mechanisms constrain the number:

1. **CGB energy budget.** Under $\delta < 1/2$:

$$
\beta(\delta)\operatorname{Vol}+\int|W|^2\le8\pi^2\chi(M).
$$

Each nonflat Ricci-flat ALE bubble carries energy at least $12\pi^2$ (the
Eguchi–Hanson quantum). Hence $|\mathcal{S}|\le C(\chi, v_0, \delta)$.

2. **Volume control.** Bishop gives $\operatorname{Vol}\le V_0(\delta)$ uniformly.
Combined with the lower bound, the total volume is bounded.

The orbifold limit $(M_\infty, g_\infty)$ is an Einstein orbifold with
$\operatorname{Ric}_{g_\infty}=g_\infty$ (exact Einstein on the regular part,
extended to the orbifold by removable-singularity results). At each singular point
$p$, the tangent cone is $\mathbb{R}^4/\Gamma$ for a finite group
$\Gamma\subset\mathrm{SO}(4)$, and the blow-up at scale $t_i\to0$ gives a
Ricci-flat ALE space $(N, g_b)$ asymptotic to $\mathbb{R}^4/\Gamma$ (exact
Ricci-flat).

**Both ends of the degeneration are exact**: the orbifold is exact Einstein, and
each ALE blow-up is exact Ricci-flat. This is because:
- Regular-part Ricci convergence gives the orbifold limit solving $\operatorname{Ric}=g$.
- At the blow-up scale $t_i$, the rescaled Ricci is $t_i^2(g+A_i)\to 0$, so the
  blow-up limit is Ricci-flat.

## 4. The Ozuch first obstruction: source-verified

From Ozuch 2021 (\cite{ozuch2021integrability}), Theorem 4.6 and Corollary 4.10–4.11.

### 4.1. General obstruction (equation 65 in Ozuch)

For the orbifold expansion $g_o = e + H_2 + O(r^3)$ and ALE expansion
$g_b = e + H^4 + O(r^{-5})$ (both in volume gauge), the first obstruction to
desingularization is:

$$
\sum_{ij} h_{ij}^+ R_{ji}^+ + \sum_{kl} h_{kl}^- R_{lk}^- = 0
$$

where $R_{ij}^{\pm}$ are the self-dual/anti-self-dual curvature operator
components of the orbifold at $p$, and $h_{ij}^{\pm}$ encode the asymptotic
curvature of the ALE space. Separating trace and traceless parts:

$$
0 = \Lambda\, c(\Gamma)\,\mathcal{V}(N, g_b)
  + \sum_{ij}\mathring{h}_{ij}^+ W_{ji}^+
  + \sum_{kl}\mathring{h}_{kl}^- W_{lk}^-
$$

where $\Lambda=\lambda$ is the Einstein constant, $\mathcal{V}<0$ is the reduced
volume of the ALE space, $c(\Gamma)>0$ is a group-theoretic constant, and
$W^{\pm}$ are the orbifold Weyl tensors at $p$.

### 4.2. Spherical/hyperbolic exclusion (Ozuch Remark 0.6)

For conformally flat orbifolds ($W^{\pm}=0$), the obstruction becomes
$\Lambda\,c(\Gamma)\,\mathcal{V}=0$. Since $\Lambda\ne0$ and $\mathcal{V}<0$,
this is impossible. **No Ricci-flat ALE desingularization of any type is
compatible with the first obstruction at conformally flat Einstein points.**

This is the mechanism behind Ozuch's Theorem 0.9: spherical and hyperbolic
4-orbifolds with $\mathbb{R}^4/\mathbb{Z}_2$ singularities cannot be GH limits
of smooth Einstein 4-metrics.

### 4.3. EH-specific obstruction (Ozuch Corollary 4.10)

For the Eguchi–Hanson bubble ($\Gamma=\mathbb{Z}_2$, $N=T^*S^2$):
$$
H^4 = -\frac{\theta_1^-\circ\omega_1^+}{2r^4},
$$
the first obstruction is equivalent to:

$$
R_e^{+,(1)}(H_2)\omega_1^+ = 0,
$$

i.e., $R_+$ acting on the EH self-dual direction $\omega_1^+$ vanishes. Since

$$
R_+ = W_+ + \frac{\Lambda}{3}\operatorname{Id}_{\Lambda^2_+},
$$

this means $W_+(p)$ has eigenvalue $-\Lambda/3$. Allowing all EH orientations,
the condition weakens to $\det R_+(p)=0$.

## 5. Spectral computation: when does `det R_+ = 0`?

For positive Einstein with $\operatorname{Ric}=g$ ($\Lambda=1$, $s=4$):

$$
R_+ = W_+ + \tfrac{1}{3}\operatorname{Id}.
$$

$W_+$ is trace-free on $\Lambda^2_+$ (a 3-dimensional space), with eigenvalues
$\mu_1+\mu_2+\mu_3=0$.

$$
\det R_+ = \prod_{i=1}^3\left(\mu_i+\tfrac{1}{3}\right) = 0
\quad\Longleftrightarrow\quad
\text{some }\mu_i = -\tfrac{1}{3}.
$$

### 5.1. Verified examples

| Manifold | $W_+$ eigenvalues | $R_+$ eigenvalues | $\det R_+$ | EH compatible? |
|---|---|---|---|---|
| $S^4$ (round) | $(0,0,0)$ | $(1/3, 1/3, 1/3)$ | $1/27$ | **No** |
| $\mathbb{CP}^2$ (Fubini-Study) | $(2/3, -1/3, -1/3)$ | $(1, 0, 0)$ | $0$ | **Yes** |
| $S^2\times S^2$ (product) | $(2/3, -1/3, -1/3)$ | $(1, 0, 0)$ | $0$ | **Yes** |
| $H^4$ (rescaled to $-g$) | $(0,0,0)$ | $(-1/3,-1/3,-1/3)$ | $-1/27$ | **No** |
| General Kähler-Einstein | $(2\Lambda/3, -\Lambda/3, -\Lambda/3)$ | $(\Lambda, 0, 0)$ | $0$ | **Yes** |

All numerical values confirmed in `workspace/data/step31_noncollapsed_dichotomy_spectral_audit.json`.

### 5.2. Codimension analysis

In the 5-dimensional space of trace-free symmetric $3\times3$ matrices
(the fiber of the $W_+$ bundle), $\{\det R_+=0\}$ is a codimension-1 algebraic
subvariety. In eigenvalue coordinates $(\mu_1,\mu_2)$ with $\mu_3=-\mu_1-\mu_2$
(a 2-dimensional plane), the zero locus is the union of three lines:

$$
\mu_1=-\tfrac{1}{3},\quad
\mu_2=-\tfrac{1}{3},\quad
\mu_1+\mu_2=\tfrac{1}{3}.
$$

**Kähler-Einstein exception**: All Kähler-Einstein 4-manifolds have $W_+$
eigenvalue $-\Lambda/3$ at every point (the anti-Kähler directions in
$\Lambda^2_+$). Hence $\det R_+=0$ identically, and EH bubbling is always
compatible with the first obstruction.

**Generic non-Kähler case**: $\det R_+\ne0$ is an open and dense condition.
For a generic non-Kähler positive Einstein orbifold, no singular point satisfies
$\det R_+=0$.

### 5.3. Key structural observation

The spectral condition $\det R_+(p)=0$ partitions the positive-Einstein world:

- **Non-Kähler with generic $W_+$**: $\det R_+\ne0$ at all points. No EH bubbling
  can occur at any orbifold singularity at first-obstruction level.
- **Kähler-Einstein**: $\det R_+=0$ everywhere. EH bubbling is first-order
  compatible. These include $\mathbb{CP}^2$, $S^2\times S^2$, del Pezzo surfaces
  (if Einstein), K3 (Ricci-flat, $\Lambda=0$).

## 6. The conditional dichotomy theorem

### 6.1. Statement

**Theorem B** (Conditional Noncollapsed Dichotomy). *Let $(M^4, g_i)$ satisfy
$\|\operatorname{Ric}_{g_i}-g_i\|_{\mathrm{op}}\le\delta_i\to0$ and
$\operatorname{Vol}(M, g_i)\ge v_0>0$. Assume:*

> **(A1)** Bubble-tree existence and finiteness for the near-Einstein
> sequence: a subsequence converges in GH sense to an Einstein orbifold
> $(M_\infty, g_\infty)$ with isolated singularities and Ricci-flat ALE
> blow-ups.

> **(A2)** The degeneration of the near-Einstein sequence inherits the
> exact-Einstein Ozuch first obstruction: at each singularity $p\in\mathcal{S}$
> with ALE blow-up $(N, g_b)$, equation (65) of \cite{ozuch2021integrability}
> holds.

*Then either:*

*(a) $M$ carries a smooth Einstein metric with $\operatorname{Ric}=g$, or*

*(b) every singular point $p\in\mathcal{S}$ of the orbifold limit satisfies the
first Ozuch obstruction. For $\Gamma=\mathbb{Z}_2$ (EH) singularities, this
means $\det R_+(p) = \det(W_+(p)+\tfrac{1}{3}\operatorname{Id})=0$.*

*In particular, if $\det R_+(p)\ne0$ at all potential singular points (e.g.,
when $M_\infty$ is conformally flat), then case (a) holds.*

### 6.2. Status of assumptions

**A1**: In dimension 4, follows from the CGB $L^2$-curvature budget (each bubble
carries $\ge 12\pi^2$) and Cheeger–Naber codimension-4 structure. The main gap:
Cheeger–Naber gives the singular-set structure for bounded Ricci, but the precise
Anderson–BKN orbifold/ALE identification is proved only for exact Einstein
sequences. For near-Einstein sequences, the blow-up is exact Ricci-flat (by Ricci
scaling), but the detailed bubble-tree description has not been established at
the full generality of $C^0$ Ricci pinching.

**A2**: This is the core mathematical content. Ozuch's Theorem 4.6 proves the
obstruction for exact Einstein sequences. The extension to near-Einstein requires
showing that the near-Einstein degeneration pattern must satisfy the same
compatibility conditions as the exact-Einstein pattern, at least in the limit
$\delta_i\to 0$.

**Possible approach**: Both the orbifold and ALE limits are exact. The
compatibility condition is a boundary integral on the matching sphere. A
divergence-free quantity (such as $\mathcal{E}_g$ or a Pohozaev-type identity
involving the second variation of Ricci) could approximately preserve this
integral across the annular region. The approximate conservation error goes to
zero as $\delta\to 0$ for fixed annular ratio. This is the content of the
annular flux argument (Step 30).

**What is NOT needed for A2**: A full weighted orbifold/ALE normal form for
near-Einstein metrics. The key insight is that both ends are exact, and only
the connecting annular region carries the approximation error.

### 6.3. What this does NOT establish

- Does not handle the collapsed positive branch ($\operatorname{Vol}\to 0$).
- Does not handle the negative branch or dimensions $n\ge 5$.
- In case (b), does not produce an Einstein metric on $M$. The obstruction
  constrains the orbifold limit, not the existence of Einstein metrics on
  the resolution topology.
- Does not address higher-order obstructions (Ozuch Remark 0.7, Question 0.8).
  Even when $\det R_+=0$, higher obstructions may prevent exact Einstein
  desingularization while allowing near-Einstein approximation.
- Does not address multiple bubbles, bubble trees, or ALE type selection beyond
  $\mathbb{Z}_2$.

## 7. Implications for the positive branch of Yau-26

### 7.1. The exclusion direction (most valuable)

For manifolds whose noncollapsed orbifold limit has $\det R_+\ne0$ at all
potential singular points, case (a) of the dichotomy gives Einstein existence.
This includes:

- Any manifold whose orbifold limit is conformally flat (spherical, flat, or
  hyperbolic). In particular, if a noncollapsed near-Einstein sequence converges
  to $S^4/\Gamma$, then the obstruction forces $\mathcal{S}=\varnothing$, giving
  Einstein on $M$.
- Any manifold whose orbifold limit has generic non-Kähler $W_+$.

### 7.2. The Kähler-Einstein boundary

Kähler-Einstein orbifold limits ($\det R_+=0$ everywhere) are the hard case.
These include orbifold quotients of $\mathbb{CP}^2$ and $S^2\times S^2$, which
are exactly the topological families in the toric stress-test program.

For $\#_k(S^2\times S^2)$: a noncollapsed near-Einstein sequence converging to
an orbifold with $k$ singular points would require $\det R_+=0$ at each. With
Weyl energy $\int|W|^2\ge 16\pi^2 k - O_\delta(1)$ (Step 18 estimate),
the Weyl must be distributed so that $\det R_+=0$ at every singular point.
This is a nontrivial constraint that strengthens with $k$.

### 7.3. Tight pinching vs. integral nonexistence

(From the research record, Steps 3–4.) For negative Seiberg–Witten/LeBrun
no-Einstein manifolds, the ratio bound

$$
\frac{\delta}{1-\delta}\ge\sqrt{\frac{p-1/3}{2}},\qquad p = k/A,
$$

shows that tight pinching and positive-margin integral nonexistence are
mutually exclusive. Combined with the spectral condition, this means: a
four-dimensional refutation needs either the zero-margin boundary $p\to 1/3$
or an entirely new nonexistence mechanism.

### 7.4. Higher-order obstructions and counterexample locus

The counterexample locus for Yau-26 positive branch (noncollapsed) is:

- First obstruction vanishes ($\det R_+=0$), but
- Some higher obstruction is nonzero (preventing exact Einstein desingularization), while
- The resolution topology carries a metric with tight positive Ricci pinching.

Ozuch Question 0.8 asks whether the Taub/Pohozaev framework can compute these
higher obstructions. Reading whether any known case has first obstruction zero
and second nonzero is a cheap source check that could be decisive.

## 8. Divergence-free cosmological Einstein tensor

For completeness, the $C^0$-Ricci-safe identity from Step 30:

$$
\mathcal{E}_g = \operatorname{Ric}_g - \tfrac{1}{2}s_g\,g + g.
$$

Under $\|\operatorname{Ric}-g\|_{\mathrm{op}}\le\delta$: $\mathcal{E}_g = A - \tfrac{1}{2}(\operatorname{tr}A)g = O(\delta)$ pointwise, and $\operatorname{div}\mathcal{E}_g=0$ (contracted Bianchi). For any vector field $Z$:

$$
\int_{\partial\Omega}\mathcal{E}_g(Z,\nu)
= \frac{1}{2}\int_\Omega\langle\mathcal{E}_g, \mathcal{L}_Zg\rangle.
$$

This identity avoids differentiating the Ricci defect and is the natural tool for
the annular flux argument. However, it is a **first-order** identity (detects
$O(\delta)$ defect), while the Ozuch obstruction is a **second-order** phenomenon
(matching of curvature 2-jets). The connection between the two requires either:
- A refined identity involving second variations of Ricci on the annulus, or
- A compactness/limiting argument that transfers the exact-Einstein obstruction
  to the near-Einstein setting through the exactness of both ends.

The latter approach (exploiting the fact that both orbifold and ALE limits are
exact) appears more natural and avoids the scaling difficulties of the direct
annular projection.

## 9. Open mathematical obligations

1. **A2 bridge**: Establish that near-Einstein degeneration inherits the
   exact-Einstein Ozuch obstruction. The most promising approach is a
   compactness argument using the exactness of both limits.

2. **Higher-order obstruction computation**: Check Ozuch [Ozu20] and
   subsequent work for cases where the first obstruction vanishes but higher
   obstructions do not.

3. **Collapsed positive branch**: The Bochner center bound (Step 28) controls
   fiber brackets once a central almost-Killing field exists. The bridge from
   $C^0$ Ricci pinching to such fields remains the main collapsed obligation.

4. **Volume lower bound**: The noncollapsed hypothesis $\operatorname{Vol}\ge v_0$
   is itself a theorem to be proved (or refuted). The toric $\alpha$-family
   (Steps 19–26) is the main test case for whether a uniform volume gap exists.

5. **Lean formalization**: Only the algebraic kernels (Steps 27–29) have been
   Lean-checked. The regular-limit theorem, spectral condition, and dichotomy
   all require standard Riemannian geometry infrastructure.

## Files

- Script: `workspace/scripts/step31_noncollapsed_dichotomy_spectral_audit.py`
- Data: `workspace/data/step31_noncollapsed_dichotomy_spectral_audit.json`
- Sources: \cite{ozuch2021integrability} (Theorem 4.6, Corollaries 4.10–4.11,
  Remark 0.5–0.6, Theorem 0.9), \cite{cheeger_naber_2015} (Theorem 1.13)


## 10. Higher-order obstructions: the counterexample locus (Ozuch 2020)

Source: \cite{ozuch2020higher} (arxiv:2012.13316), Theorem 0.2, Theorem 0.13,
Theorem 0.15.

### 10.1. The Kähler-type curvature condition

Ozuch 2020 proves that for compact Einstein orbifolds with $\mathbb{R}^4/\mathbb{Z}_2$
singularities which are GH limits of (stable Ricci-flat or single-singularity rigid)
Einstein metrics, the orbifold curvature at each singular point must be of
**Kähler type**: $R_+(p)$ has a specific one-dimensional kernel. This strengthens
the first-obstruction condition $\det R_+ = 0$ of Corollary 4.10 in
\cite{ozuch2021integrability}.

### 10.2. The T^4/Z_2 polynomial system

For the flat torus $T^4/\mathbb{Z}_2$ with 16 singular points (standard lattice),
desingularized by Eguchi-Hanson metrics in various orientations, sizes, and
directions, Ozuch computes:

| Setting | Parameters | Polynomial constraints |
|---|---|---|
| General Einstein desingularization | 57 | **57** (48 analogous to first obstruction) |
| Stable Ricci-flat desingularization | 57 | **84** (80 analogous to curvature condition) |
| Nondegenerate Einstein desingularization | 57 | **84** |

### 10.3. Decisive finding: a 14-dimensional solution family EXISTS

> "Perhaps surprisingly, we find a set of solutions to our 84 equations. More
> precisely, there exists an explicit 14-dimensional set of configurations of
> gluing of Eguchi-Hanson metrics which satisfy the 84 above equations. The
> orientations of the Eguchi-Hanson metrics follow the chessboard pattern of
> [BK17], but their directions and sizes are not constrained."
> (Ozuch 2020, after Theorem 0.13)

This means: **the known obstructions do NOT exclude all EH bubble configurations
on $T^4/\mathbb{Z}_2$.** The chessboard (8 positive + 8 negative) pattern with
unconstrained sizes and directions survives all 84 identified polynomial
constraints.

### 10.4. Excluded configurations

Theorem 0.15 proves that 1 positive + 15 negative EH bubbles on the regular
torus CANNOT be an Einstein desingularization. Remark 0.17 extends this to
fewer than 3 positive + rest negative for stable Ricci-flat.

### 10.5. Implications for the counterexample locus

The counterexample locus for Yau-26 noncollapsed positive branch is:

1. **First obstruction zero** ($\det R_+ = 0$, Kähler-type $W_+$) — necessary,
   and satisfied at all Kähler-Einstein orbifold points.
2. **All known higher obstructions zero** — the 14-dimensional chessboard family
   satisfies this on $T^4/\mathbb{Z}_2$.
3. **Yet some unknown higher obstruction nonzero** — preventing actual smooth
   Einstein on the resolution. This is UNKNOWN.
4. **The resolution topology carries tight positive Ricci pinching** — independent
   requirement.

Ozuch raises the fundamental question (from the abstract): **"These new
obstructions... raise the question of whether a compact Einstein 4-orbifold
which is limit of Einstein metrics bubbling out Eguchi-Hanson metrics has to
be Kähler."** If the answer is YES, then every EH bubble configuration from
an exact-Einstein sequence must sit inside the Kähler moduli, severely
constraining counterexamples. If NO, then non-Kähler Ricci-flat metrics might
exist on K3-like topologies, which would be a major discovery independent of
Yau-26.

### 10.6. Connection to the noncollapsed dichotomy

The noncollapsed dichotomy (Section 6) is strongest in the non-Kähler regime
($\det R_+ \ne 0$): there, the first obstruction automatically excludes EH
bubbling, forcing the regular limit and Einstein on $M$.

In the Kähler regime ($\det R_+ = 0$), higher obstructions provide additional
constraints but do not close. The 14-dimensional surviving family on $T^4/\mathbb{Z}_2$
shows that a complete resolution of the Kähler case requires either:
- Computing and verifying ALL obstructions (not just the first 84), or
- An entirely different argument not based on order-by-order obstruction analysis.

This is consistent with the research trajectory: the noncollapsed positive branch
has a clean structure (regular vs. bubble) and a clean spectral condition
(Kähler vs. non-Kähler), but the Kähler boundary remains the hard open frontier.
