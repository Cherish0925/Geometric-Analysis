# Step 38: Period transport, exact algebra, and corrected collapse assessment

> **Step 39 correction.** Read this note together with `workspace/notes/step39_known_answer_calibration_and_defect_reframe.md` and `workspace/data/step39_known_answer_period_calibration.json`. The finite noncompact Weyl-chain algebra remains useful in its own scope, but its period mismatch does **not** transfer directly to compact toric polygons. Known compact toric positive Einstein metrics (product `S^2 x S^2`, Page on `CP^2#CPbar`, CLW on `CP^2#2CPbar`, and toric KE `dP_3`) require any compact defect functional to vanish on repeated same-circle rods. Step 15/17's `mu=1 iff A=0` is only a separated SdS/cohomogeneity-one result, not a universal two-rod compact obstruction. The proposed perturbation of the alternating `m=6` candidate around `A=0` is not well posed unless an exact background solution is first supplied.

Session S0910A02. Agent2/Constructor. Phase Explore.

## 0. Scope and retractions

This note supersedes Step 36's `step36_edge_cone_accounting_correction.md`
on the collapsed positive branch. It preserves the valid parts of Steps 34–37
while retracting the false inference and formulating the correct compact-polygon
problem.

**RETRACTED (Step 36):** "Alternating adjacent Delzant labels exclude struts."
False. A Weyl conical singularity is a rod-period defect, not a corner defect.
Nonadjacent rods with labels $\pm v$ generate the same $S^1$ subgroup and must
share a single global period. The alternating pattern
$(1,0),(0,1),(-1,0),(0,-1),\ldots$ gives $m/2$ rods per circle, each imposing
a period condition. Source: Emparan–Reall (hep-th/0110258) lines 1358–1426.

**RETRACTED (Step 36):** "NUT smoothing costs $O(1)$, so the α-family survives
all energy arguments." This was based on the false strut-exclusion. The energy
question is correctly tied to the period transport, not to corner-type accounting.

**PRESERVED:** Edge-cone defect terms are separate from bulk $\int|W|^2$ in
Atiyah–LeBrun. Rod count $= \chi = 2 + b_2$. No $\delta\log(1/t)$ rate condition
for noncollapsed Route A. The iterated-limit procedure (fix $R$, $\delta_i \to 0$,
then $R \to \infty$) gives relative error $O(\delta\log R) + O(1/R)$.

## 1. Exact period algebra for noncompact alternating chains

### 1.1 The formula

For $m$ equal-length alternating finite rods on the Weyl axis with two
semi-infinite ends (forming a $\mathbb{Z}^2$-basis pair), the same-label
exponential period range is
$$
\exp(\ell_{\max} - \ell_{\min}) = \prod_{k=1}^{n-1}\frac{2k+1}{2k},
\qquad n = m/2.
$$

**Numerical verification:** matches to relative error $< 10^{-10}$ for
$m = 4, 6, 8, 10$ (Step 37 partition probe + Step 38 exact algebra).
The exact algebraic proof requires the Weyl axis regularity theory (endpoint-
sharing rods give $0/0$ in the naive pairwise $\nu$ formula, cancelled by the
$U_i$ regular contribution in the combined $\ell$ expression). The formula is
confirmed by the numerical quadrature to full machine precision.

| $m$ | $n$ | Predicted | Verified |
|-----|-----|-----------|----------|
| 4   | 2   | 3/2       | ✓        |
| 6   | 3   | 15/8      | ✓        |
| 8   | 4   | 35/16     | ✓        |
| 10  | 5   | 315/128   | ✓        |

### 1.2 Consecutive ratios and central pair

For $m = 10$ (5 same-label rods), the consecutive same-label exp-ratios are:
- Rods 1→3: ≈ 1.346 (not a simple fraction)
- Rods 3→5: ≈ 1.215 (175/144)
- **Rods 5→7: exactly 6/5** (confirmed to $10^{-10}$)
- Rods 7→9: ≈ 1.254

The central pair ratio for even $n$ is exactly $(n+1)/n$:

| $m$ | $n$ | Central exp-ratio | Exact     |
|-----|-----|-------------------|-----------|
| 4   | 2   | 3/2               | $(2+1)/2$ |
| 8   | 4   | 5/4               | $(4+1)/4$ |
| 12  | 6   | 7/6               | $(6+1)/6$ |
| 16  | 8   | 9/8               | $(8+1)/8$ |
| 20  | 10  | 11/10             | $(10+1)/10$ |
| 24  | 12  | 13/12             | $(12+1)/12$ |

### 1.3 Logarithmic drift structure

The total drift is $\frac{1}{2}\log n + O(1)$. The central pair mismatch is
$\log(1 + 1/n) \sim 1/n$ for large $n$. This confirms the drift is a
**logarithmic end effect**, not a fixed local defect. Each rod adds $O(1/n)$
to the accumulated period shift.

**Consequence for equal-length rods:** the α-family has all rods equal.
In the noncompact model, equal rods are the *worst case* for drift
accumulation — the logarithmic drift cannot be absorbed by varying rod lengths.

### 1.4 Positive mass forcing for finite chains

For a finite alternating chain with $\mathbb{Z}^2$-basis semi-infinite ends:
- Asymptotics: $\mathbb{R}^4$ (det of label matrix = 1).
- If all periods matched → complete Ricci-flat ALE metric with $\mathbb{R}^4$
  asymptotics.
- Positive mass theorem: Ricci-flat AE, mass $\ge 0$, equality iff flat $\mathbb{R}^4$.
- Flat $\mathbb{R}^4$ has no bolts → contradiction.
- Therefore: **period mismatch is structurally forced for any finite chain**.

This does NOT apply to the compact polygon (no asymptotics) or the infinite
periodic chain (different boundary structure).

## 2. The recurring closing mechanism

This session has produced three independent instances of the same mechanism:
"local data exists for every parameter; global closure kills it."

### Instance 1: Step 15/17 two-rod rigidity
For a separated Schwarzschild–de Sitter germ with two rods collapsing the same
circle, the surface gravity condition gives $\mu = 1 \iff A = 0$. The deficit
$1 - \mu = (4/3)A + O(A^2)$ is nonzero for any $A > 0$.

### Instance 2: Step 27 H₃ endpoint theorem
For the diagonal cohomogeneity-one $H_3$ model with $\Lambda > 0$ and
$\delta < \Lambda/2$, the bracket function $b$ has no critical point in the
regular regime. Large bracket can exist locally but cannot close at two
compact endpoints.

### Instance 3: α-family period mismatch (this step)
For $m/2$ same-label rods of equal length, the required periods drift
logarithmically from one end to the other. The central pair mismatch is
$(n+1)/n$ for even $n$, and the total mismatch grows as $\sim\frac{1}{2}\log n$.

All three instances share the structure:
- Local Einstein/near-Einstein data admits free parameters.
- Global closure imposes overdetermined compatibility conditions.
- The compatibility gap grows with the curvature/complexity parameter.

## 3. The compact-polygon period transport problem

### 3.1 Setup

The α-family lives on a compact Delzant polygon $P$ with $m = 2k+2$ edges,
normals $(1,0),(0,1),(-1,0),(0,-1),\ldots$. The T² action is by a fixed global
$T^2 = \mathbb{R}^2/(2\pi\mathbb{Z})^2$. At each edge with normal $v$, the
circle $\langle v, \phi\rangle$ collapses. Labels $v$ and $-v$ generate the
same circle, so all $(1,0)$ and $(-1,0)$ edges require the $\phi_1$-circle to
collapse with the same rate, and similarly for the $\phi_2$-circle.

### 3.2 Why the noncompact probe is not the compact problem

The noncompact Weyl-axis computation places all rods on a line with semi-infinite
ends. The compact polygon has no ends — the orbit space is a closed 2D region.
The Weyl formalism on the polygon uses $w = \sqrt{\det h}$ as a harmonic
coordinate ($\Delta_B w = -2w$ for $\Lambda = 1$), positive inside $P$, vanishing
on $\partial P$.

**Key structural difference:** The noncompact chain has two asymptotic regions
(left and right semi-infinite rods) that break the symmetry and create the
logarithmic drift. The compact polygon has no such regions. The infinite periodic
chain (2-periodic translation) has automatic same-label matching by symmetry.

The compact polygon is **intermediate**: finite rod count (like the finite chain)
but no asymptotic regions (like the periodic chain). The correct question is:

> **Does the compact-polygon period monodromy — the product of local transports
> around one full circuit of the boundary — equal the identity?**

### 3.3 Gauge freedoms and invariant quantities

Gauge freedoms in the period transport:
1. **Global circle rescaling:** $\phi_1 \mapsto \lambda\phi_1$, $\phi_2 \mapsto \mu\phi_2$.
   This adds constants to all same-label $\ell$ values. Cancels in the range.
2. **Weyl-coordinate shifts:** $z \mapsto z + c$. Does not affect $\ell$ differences.
3. **Rod-length normalization:** Total boundary length can be rescaled.

The invariant quantity is the **same-label period ratio**: for all pairs of
rods with the same label, the ratio $e^{\ell_i - \ell_j}$ must equal 1.

### 3.4 What the transport actually computes

On the orbit-space boundary $\partial P$, moving along each edge:
- **On a rod (edge) with label $v$:** The metric degenerates along the
  $v$-direction. The regularity condition determines the local period coefficient
  $\ell(z)$ as a function along the rod, involving $\nu$ and the regular part of
  the other potentials.
- **At a corner (vertex) where labels change:** Both circles degenerate.
  The NUT/corner smoothness condition sets $\nu = 0$ (in the standard
  normalization). This is the "reset condition" at each corner.

The transport is:
$$
\ell_{\text{rod}_{k+2}} - \ell_{\text{rod}_k} = \int_{\text{rod}_{k} \to \text{corner} \to \text{rod}_{k+1} \to \text{corner} \to \text{rod}_{k+2}} d\ell,
$$
accumulated over two consecutive edges and two corners, comparing two rods
with the same label.

### 3.5 The two-scale matching architecture

For the α-family with $A \to \infty$:
- **Inner scale:** Each rod rescaled by $\sqrt{2A}$ approaches Euclidean
  Schwarzschild with mass $\hat{M} \to 1/2$. Rod length $\hat{L} = \sqrt{2A}L \to \pi$.
  Adjacent rods are at finite rescaled distance.
- **Outer scale:** The macroscopic orbit space is the polygon $P$ with
  $\operatorname{Ric} = g$ and shrinking fibers.

The period transport has both inner and outer contributions:
- **Inner:** local Schwarzschild period at each bolt, sensitive to the bolt
  geometry. For equal rods, these are all the same.
- **Outer:** accumulated phase from the macroscopic orbit-space geometry.
  This is where the mismatch lives in the noncompact case.

For the compact polygon, the macroscopic geometry has finite total Gauss–Bonnet
angle $2\pi\chi_B = 2\pi(m+2)/m \cdot m = 2\pi(m+2)$... actually,
$\chi(\text{polygon with m edges}) = 1$ (contractible), so
$\int K_B\,dA_B + \int \kappa\,ds = 2\pi$.

The total angle turning is $2\pi$, distributed among $m$ corners and $m$ edges.
The inner-scale Schwarzschild contributions are $O(1)$ per cell, and the
outer-scale contributions involve the integrated base curvature $K_B$.

### 3.6 Connection to the two-rod rigidity

For $m = 4$ (rectangle, $S^2 \times S^2$), there are exactly 2 same-label rods
per circle. The period matching condition is exactly the two-rod rigidity from
Step 15/17: $\mu = 1 \iff A = 0$. This is the $n = 2$ case of the exact formula,
where the exp-range is $3/2$ (definitely $\neq 1$ for any nonzero rod source).

For $m = 6, 8, \ldots$, the number of same-label rods grows, and the question
becomes more complex. But the mechanism is the same: each bolt's Schwarzschild
geometry determines a preferred period, and all bolts with the same circle must
agree.

## 4. Corrected energy accounting

### 4.1 Bolt-cell energy

Each rod in the rescaled Schwarzschild limit contributes $8\pi^2$ to the total
curvature energy $\int|\mathrm{Rm}|^2$. The Euclidean Schwarzschild metric is
a complete manifold with $\chi = 2$, giving total energy $8\pi^2\chi_{\mathrm{ES}} = 16\pi^2$.
But each Schwarzschild covers ONE bolt with TWO polar caps. In the alternating
chain, each bolt cell includes one bolt and shares caps with neighbors.
The half-cell energy is $8\pi^2$, which INCLUDES the polar/cap contributions.

### 4.2 Budget

For $m$ rods with $\chi = m + 2$ (toric 4-manifold):
- Total bolt energy: $m \times 8\pi^2$.
- CGB budget: $8\pi^2\chi = 8\pi^2(m+2)$.
- Slack: $16\pi^2$ (for boundary/polar contributions).

This is NOT zero slack. The $16\pi^2$ accommodates the orbit-space boundary
conditions. Whether this slack is consistent with smooth closure is part of
the global PDE problem, not something that can be settled by pure accounting.

## 5. Current status of the collapsed positive branch

### What is known:
1. The α-family passes all tested local constraints (Steps 19, 25).
2. Period mismatch in the noncompact model is exact and structurally forced
   for finite chains (positive mass theorem).
3. Central mismatch is $(n+1)/n \to 1$ as $n \to \infty$ (end effect).
4. The infinite periodic chain has automatic same-label matching by symmetry.
5. The compact polygon is intermediate: no ends, but finite total angle.

### What is NOT known:
1. Whether the compact-polygon period monodromy is trivial or not.
2. Whether variable rod lengths can absorb the logarithmic drift.
3. Whether the Einstein (Ric = g) boundary conditions change the period
   structure compared to Ricci-flat.
4. Whether the two-rod rigidity $\mu = 1 \iff A = 0$ generalizes to all $m$.

### The decisive computation:
Define the compact-polygon period transport for $m = 6$ and $m = 8$ in
the Abreu–Guillemin or Weyl formalism. Compute the same-label period
monodromy explicitly. If it is bounded away from the identity as $A \to \infty$,
this gives a topology-uniform collapse obstruction for the alternating stress
family. If it can be trivialized (by varying rod parameters), this is a
genuine BREAK candidate.

## 6. Extension beyond four dimensions

The closing mechanism is not intrinsically four-dimensional. Step 27's H₃
endpoint argument uses the same structure in arbitrary dimensions: local data
admits free parameters, global closure on a compact base kills them. The
correct general formulation is:

> For a compact toric manifold $M^{2n}$ with $T^k$ action ($k \ge 1$) and
> Delzant polytope $P$ with primitive facet normals, the Einstein equation
> $\operatorname{Ric} = \Lambda g$ on $M$ reduces to a PDE system on $P$ with
> boundary conditions at each facet determined by the collapsing circle.
> The **period monodromy** around a cycle of same-label facets is the invariant
> quantity measuring global closing compatibility.

This generalizes the two-rod $\mu = 1$ condition, the H₃ endpoint theorem,
and the alternating-chain period transport to a single framework applicable
in all dimensions with toric symmetry.

## 7. Evidence files

- Exact algebra: `workspace/data/step38_exact_period_algebra.json`
- Step 37 Weyl probes: `workspace/data/step37_weyl_partition_period_probe.json`,
  `workspace/data/step37_weyl_period_probe.json`
- Step 36 data (partially retracted): `workspace/data/step36_*.json`
- Step 25 corrected toric equations: `workspace/notes/step25_build_break_analytic_verdict.md`
- Step 17 two-rod rigidity: `workspace/notes/step17_rigidity_Tk_identity_and_route_assessment.md`
- Script: `workspace/scripts/step38_exact_period_algebra.py`

## 8. The compact-polygon period problem: precise formulation

### 8.1 From separated to connected models

For a single constant-$K_B$ rod of the warping equation $-\Delta_B P = (1-K_B)P$
reduced to 1D: $P'' + \omega^2 P = 0$ with $\omega = \sqrt{1+2A}$, the transfer
matrix from one end to the other is
$$
T_{\text{rod}} = \begin{pmatrix} \cos(\omega L) & \sin(\omega L)/\omega \\
-\omega\sin(\omega L) & \cos(\omega L) \end{pmatrix}
= \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I.
$$
This means: **in isolation**, each rod preserves the surface gravity magnitude
exactly. The mismatch between same-label rods arises from the **inter-rod
geometry** — the metric on the orbit-space interior connecting different rods.

### 8.2 The Weyl-coordinate connection

In the Weyl formalism, the inter-rod geometry is encoded in $\nu(r,z)$, which
satisfies:
$$
\nu_r = -r(U_{1,r}U_{2,r} - U_{1,z}U_{2,z}), \qquad
\nu_z = -r(U_{1,r}U_{2,z} + U_{1,z}U_{2,r}).
$$
At a corner (NUT point) where both circles degenerate, the smoothness condition
requires $\nu \to 0$. At each rod, $\nu$ determines the period coefficient
$\ell = \nu - (U_{\text{label}} - \log r)$ as $r \to 0$.

For the compact polygon, $\nu$ satisfies these equations on the interior of $P$
with boundary conditions at each edge and vertex. The period monodromy is the
accumulated $\ell$ change around a circuit of same-label edges.

### 8.3 Rescaling identification (precise statement)

**Claim (derived in Step 38):** For the compact toric $T^2$-invariant Einstein
metric $\operatorname{Ric} = g$ on $\#_k(S^2\times S^2)$ with $m = 2k+2$ edges
and constant edge curvature $A_m$ on all edges, rescaling the orbit-space metric
by $\sqrt{2A_m}$ gives:
- Rod length $\hat{L} = \sqrt{2A_m}\,L = \pi/\sqrt{1+1/(2A_m)} \to \pi$.
- Eigenvalue equation: $-\hat\Delta \hat{w} = \frac{2}{2A_m}\hat{w} \to 0$.
- Boundary conditions unchanged (unit slope at rods, smoothness at corners).

In the limit $A_m \to \infty$, the rescaled problem converges to the Weyl
Ricci-flat rod problem with $m$ equal-length rods of length $\pi$.

**Consequence:** The noncompact Weyl period mismatch is the **leading-order
approximation** to the compact-polygon mismatch. Correction terms are
$O(1/A_m)$ from the eigenvalue equation.

### 8.4 Compact versus noncompact: the closure effect

The noncompact chain has two semi-infinite ends that break the translational
symmetry and create the logarithmic drift. The compact polygon has no ends
but wraps around. Three cases:

1. **Noncompact finite chain** ($m$ finite rods + 2 semi-infinite):
   Mismatch is $\prod_{k=1}^{n-1}(2k+1)/(2k)$, forced by positive mass theorem.

2. **Infinite periodic chain** (2-periodic translation):
   Same-label rods identified by symmetry → automatic $\ell$ matching.

3. **Compact polygon** ($m$ edges, total angle $2\pi$):
   The boundary wraps around. The monodromy question is whether the
   wrapping creates or absorbs the mismatch.

For $m = 4$ (rectangle), the compact two-rod rigidity $\mu = 1 - (4/3)A$
(Step 15/17) shows the compact mismatch is **nonzero and grows with $A$**.
This is a genuine compact computation, not a noncompact approximation.

### 8.5 Decisive computation for $m = 6, 8$

For $m = 6$ (hexagonal orbit space, $\#_2(S^2\times S^2)$):
- 3 same-label rods per circle.
- Noncompact mismatch: exp-range $= 15/8 = 1.875$.
- Central pair ratio: $45/32 \approx 1.406$.
- Question: Does the compact hexagonal boundary condition reduce this?

**Two approaches:**
1. **Numerical PDE:** Solve the coupled toric Einstein system on the hexagonal
   domain with prescribed edge labels and constant edge curvature $A$. Read off
   the surface gravity at each rod.
2. **Perturbative:** Expand around the flat model ($A = 0$, round product metric)
   and compute the period variation to leading order in $A$.

For approach (2): at $A = 0$, all rods are equally spaced with period-matching
$\ell = \text{const}$. The perturbation at first order in $A$ gives the
linear response of $\ell$ to edge curvature. If this linear response is nonzero
for the same-label difference, the mismatch is $O(A)$ for small $A$, which
becomes large as $A \to \infty$.

### 8.6 Extension to $T^k$-polytope statement

The period transport is not intrinsically four-dimensional. For a compact
$T^k$-manifold with Delzant polytope $P \subset \mathbb{R}^k$ and Einstein
metric, each facet with primitive normal $v \in \mathbb{Z}^k$ requires the
circle $\langle v, \phi\rangle$ to collapse with a specific rate. Facets with
normals $\pm v$ or more generally with $v$ and $v'$ generating the same circle
must share a single global period.

The **period monodromy** is the product of local transports around a cycle
of same-circle facets, through the connecting corners and interior geometry.
This generalizes the Yau-26 closing mechanism to all dimensions with toric
symmetry, producing a family of topologically constrained period-matching
obstructions.
