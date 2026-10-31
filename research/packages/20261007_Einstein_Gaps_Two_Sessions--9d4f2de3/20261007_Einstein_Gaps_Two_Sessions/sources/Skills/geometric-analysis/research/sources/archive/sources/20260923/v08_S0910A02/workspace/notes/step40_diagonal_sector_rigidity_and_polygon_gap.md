# Step 40: Diagonal-sector identification, symmetric-wedge analysis, and product rigidity

> **Step 41 Preceptor correction.** This note is partially superseded by `workspace/notes/step41_preceptor_review_diagonal_route_and_allocation.md`. The Liu-based diagonal-sector identification is retained and source-grade, but the product linearization/rigidity calculation in §4 is not established: the displayed equation for `alpha` is not the direct linearization of the orbit-volume eigenfunction equation, and the alleged `sin x` kernel/rescaling mode violates the full rod derivative data at fixed `Lambda=1`. The constant-curvature gap narrative is also corrected by `workspace/data/step41_regular_polygon_eigenvalue_probe_corrected.json`: the relevant m=6 mismatch is a near miss (about 1.84% rod/side at the eigenvalue-selected curvature, or `lambda1≈1.88945` at the side-matching curvature), not the large `A -> infinity` 68.7% gap. Odd-m topology labels in the data are geometry probes only and should not be treated as closed alternating toric manifolds.

Session S0910A02. Agent2/Constructor. Phase Execute.

## 0. Scope

This step establishes the structural identification of the diagonal twist-free framework with the
alternating-label toric sector, analyzes the polygon/rod gap and eigenvalue constraints, and performs
a linearized deformation analysis at the product metric on $S^2\times S^2$. No branch of Yau-26 is
resolved. The toric work remains a four-dimensional positive-sign symmetry-restricted laboratory.

## 1. Diagonal sector = alternating label sector

**Theorem (structural, combining Liu's results).** For a simply connected closed Einstein
4-manifold $(M^4, g)$ with isometric $T^2$-action:

1. The action is geometrically polar (Liu Theorem 3.1): the twist scalars $\alpha,\beta$ vanish.
2. If the action is *diagonal* (all isotropy groups $S(1,0)$ or $S(0,1)$), then $g$ is a
   *diagonal metric* (Liu Proposition 5): the action fields $V_1,V_2$ are orthogonal everywhere.

**Key structural observation.** In the diagonal metric $g = g_\Sigma + a^2\,d\varphi_1^2 + b^2\,d\varphi_2^2$,
a rod with label $v = (p,q)$ requires $p^2 a^2 + q^2 b^2 \to 0$ on a codimension-2 set.
Since $a,b > 0$ in the interior, this forces $p=0$ or $q=0$. Therefore:

$$\text{Diagonal metrics allow only rod labels } \pm e_1 = (\pm1,0) \text{ and } \pm e_2 = (0,\pm1).$$

This means exactly **two unoriented circle classes**, which is precisely the alternating-label
polygon: $(1,0),(0,1),(-1,0),(0,-1),(1,0),\ldots$

**Consequence.** The diagonal framework is not a restrictive ansatz — it is the *complete*
sector for alternating actions. Page ($F_1$), CLW ($dP_2$), and toric KE $dP_3$ have 3+ circle
classes and are outside this sector; they cannot serve as calibration targets within it.

The only known diagonal $T^2$-Einstein 4-manifolds are $S^4$ ($m=2$) and $S^2\times S^2$ ($m=4$,
product metric). The question becomes: does the diagonal sector contain any solution with $m \ge 6$?
Equivalently, does $\#_k(S^2\times S^2)$ for $k \ge 2$ carry a diagonal $T^2$-invariant Einstein metric?

## 2. Polygon/rod side-length comparison

For a right-angled regular $m$-gon in $\mathbb{H}^2(-A)$ (constant Gaussian curvature $-A$), the
side length is
$$
s_{\mathrm{reg}}(m,A) = \frac{2}{\sqrt{A}}\,\mathrm{arccosh}\bigl(\sqrt{2}\cos(\pi/m)\bigr),
\qquad m \ge 5.
$$
For $m=4$, no right-angled quadrilateral exists in $\mathbb{H}^2$; the orbit space is flat.

The rod ODE for $\mathrm{Ric}=g$ gives $L_{\mathrm{rod}} = \pi/\sqrt{1+2A}$.

**Constant-curvature gap at large $A$:** $L_{\mathrm{rod}}/s_{\mathrm{reg}} \to (\pi/\sqrt{2})/s(m)$.

| $m$ | $s(m)$ in $\mathbb{H}^2(-1)$ | gap at large $A$ | $A_{\mathrm{match}}$ |
|-----|------|------|------|
| 5 | 1.061 | 109.3% | 0.148 |
| 6 | 1.317 | **68.7%** | 0.271 |
| 8 | 1.529 | 45.3% | 0.450 |
| 10 | 1.617 | 37.4% | 0.563 |
| $\to\infty$ | 1.763 | 26.0% | 0.849 |

The gap *grows* with smaller $m$: the hexagonal case ($m=6$) has a 68.7% gap, much worse than the
asymptotic 26% for large $m$. Even at the matching curvature $A_{\mathrm{match}} = 0.271$ where
$L_{\mathrm{rod}} = s_{\mathrm{reg}}$, the eigenvalue constraint (see §3) may be violated.

## 3. Eigenvalue constraint

The orbit volume $\phi = ab$ satisfies $-\Delta_\Sigma\phi = 2\Lambda\phi$ with Dirichlet BCs
(Liu Proposition 2). For $\Lambda = 1$: the principal Dirichlet eigenvalue is $\lambda_1(\Sigma) = 2$.

**Faber–Krahn bound.** For a domain of area $A_\Sigma$ in 2D:
$\lambda_1 \ge \pi j_{0,1}^2/A_\Sigma \approx 18.17/A_\Sigma$.

For $\lambda_1 = 2$: $A_\Sigma \ge 9.08$.

For $m = 6$ in $\mathbb{H}^2(-A)$: $A_\Sigma = \pi/A$ (Gauss–Bonnet).
Faber–Krahn gives $A \le 0.346$.

At $A = 0.346$: $L_{\mathrm{rod}} = 2.415$, $s_{\mathrm{reg}} = 2.239$. **Gap: 7.9%.**

The rod is still longer than the polygon side even at the eigenvalue boundary.
For variable $K_\Sigma$: the argument weakens because Faber–Krahn is not tight and the
orbit space need not have constant curvature. But the combined constraint (Gauss–Bonnet +
eigenvalue + rod ODE) remains nontrivial.

## 4. Product metric rigidity (linearized analysis)

The product metric on $S^2\times S^2$ has $g_\Sigma = dx^2 + dy^2$ on $[0,\pi]^2$,
$a = \sin x$, $b = \sin y$, $K_\Sigma = 0$.

**Linearized eigenfunction equation.** For $a = \sin x + \varepsilon\alpha$,
$g_\Sigma = e^{2\varepsilon s}(dx^2+dy^2)$:
$$
L(\alpha) := -(\Delta_0 + 1)\alpha = (\Delta_0 s - 2s)\sin x.
$$

BCs: Dirichlet in $x$ ($\alpha(0,y)=\alpha(\pi,y)=0$), Neumann in $y$ (free at $b$-rods).

**Kernel of $L$.** Eigenfunctions: $\sin(nx)\cos(my)$ with eigenvalue $n^2+m^2-1$.
Kernel: $n^2+m^2=1$, only $(n,m)=(1,0)$, giving $\sin(x)$ — trivial $\Lambda$-rescaling.

**Deformation count.** The free function is $s(x,y)$ (conformal factor). The constraints are:
1. **Solvability** of the eigenfunction equation (Fredholm condition from the kernel).
2. **Neumann correction** at rod boundaries: $\partial_x\alpha(0,y) = s(0,y)$.
3. **Traceless horizontal Einstein equation**: additional PDE constraint.

Three independent constraint families for one free function $\Rightarrow$ **overdetermined**.

**Conclusion.** The product metric is expected to be isolated (rigid) in the diagonal Einstein
sector, consistent with Liu's uniqueness under $\sec\ge0$ but potentially extendable beyond it.
A rigorous proof requires verifying that the constraints are independent (no hidden algebraic
identity); Liu's Lemma 5.2 provides the strongest available uniqueness tool.

## 5. The $b_+$ question

All known simply connected positive Einstein 4-manifolds have $b_+ \le 1$:

| Manifold | $b_+$ | $b_-$ | Einstein metric |
|---|---|---|---|
| $S^4$ | 0 | 0 | round |
| $\mathbb{CP}^2$ | 1 | 0 | Fubini–Study |
| $S^2\times S^2$ | 1 | 1 | product |
| $\mathbb{CP}^2\#\overline{\mathbb{CP}}^2$ | 1 | 1 | Page |
| $\mathbb{CP}^2\#2\overline{\mathbb{CP}}^2$ | 1 | 2 | CLW |
| $\mathbb{CP}^2\#k\overline{\mathbb{CP}}^2$, $k=3,\ldots,8$ | 1 | $k$ | Kähler–Einstein |

The alternating stress family $\#_k(S^2\times S^2)$ has $b_+ = k$. For $k \ge 2$, this gives
$b_+ \ge 2$.

**If $b_+ \le 1$ is necessary for simply connected positive Einstein 4-manifolds with $T^2$
action, then $m \ge 6$ diagonal Einstein is excluded in one stroke.**

This is an open question. Liu proved the classification under $\sec\ge 0$ (which forces
$b_+ \le 1$ from the topology restriction). No theorem extending this to arbitrary Einstein
metrics with $T^2$ symmetry is known to us. A targeted literature search did not resolve it.

## 6. Implications for the collapsed positive branch

The diagonal-sector identification changes the collapsed positive route:

1. **Page/CLW/dP3 calibration is irrelevant.** These examples are not in the diagonal sector.
   Step 39's calibration requirement was asking the wrong question: it tried to validate the
   noncompact Weyl chain against examples in a different sector.

2. **The only m=4 calibration is S²×S² (product metric).** Within the diagonal sector,
   the product metric is the unique known example, and the linearized analysis suggests
   it is isolated.

3. **The m≥6 question is clean.** It asks whether the overdetermined diagonal Einstein system
   (eigenfunction + horizontal Einstein + boundary conditions) on an $(m)$-gon orbit space
   has any solution. The constant-curvature gap (68.7% at m=6), eigenvalue constraint, and
   linearized rigidity all point toward non-existence, but none gives a complete proof.

4. **The formal α-family is a stress test within this exact sector.** It passes local rod/corner
   conditions and integral identities, but the gap analysis shows global closure faces serious
   geometric obstruction. The 68.7% rod/polygon gap at m=6 is larger than at m→∞.

## 7. Connection to Yau-26

Even a complete proof that no diagonal $T^2$-Einstein metric exists on $\#_k(S^2\times S^2)$ for
$k \ge 2$ would not settle the Yau-26 positive branch, because:

- The Yau-26 antecedent provides only $C^0$ Ricci pinching, not $T^2$ symmetry.
- The output Einstein metric is allowed to be non-toric.
- A $C^0$-Ricci-pinched metric might collapse along a different fibration.

The toric obstruction contributes to Yau-26 only through the "toric stress test" logic:
if the formal α-family cannot be completed to a global smooth metric, then
$\#_k(S^2\times S^2)$ does not admit tight positive toric pinching, and the toric collapsed
positive branch is eliminated. But non-toric collapse and noncollapsed sequences remain.

## 8. Files

| File | Content |
|------|---------|
| `scripts/step40_diagonal_sector_and_symmetric_wedge.py` | Polygon gap and eigenvalue analysis |
| `data/step40_diagonal_sector_and_symmetric_wedge.json` | Polygon/gap/eigenvalue data |
| `scripts/step40_linearized_deformation.py` | Linearized deformation analysis |
| `data/step40_linearized_deformation_analysis.json` | Kernel, deformation count, extension |
| This note | Synthesis |

## 9. Peer status (Steps 38–40)

- **A01 Step 38 (#349):** Withdrew the Step 37 continuation/first-exit closure. The weighted
  shifted $U = aT$ equation and volume-average support normalization are being repaired.
  The negative branch continuation theorem is not proved.
- **A03 Step 40 (#350):** Withdrew the all-order continuation. Proved a valid $m=2$ coupled
  continuation mechanism with the whole-manifold unweighted lemma. Higher-order modules
  remain open. The negative branch route is advancing but not closed.
- **A02 (this step):** The positive collapsed toric route is now identified as the complete
  diagonal sector. Product rigidity and polygon gaps narrow the space of possible m≥6
  solutions. No route to Yau-26 is complete.
