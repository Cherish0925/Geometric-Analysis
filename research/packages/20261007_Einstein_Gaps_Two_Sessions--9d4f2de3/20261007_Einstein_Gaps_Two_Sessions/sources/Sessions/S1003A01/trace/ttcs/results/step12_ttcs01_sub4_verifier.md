# TTCS Independent Branch Record

```json
{
  "step_id": 12,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md",
    "Sessions/S1003A01/workspace/notes/step11_independent_review_O11_and_mixed_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260927_covering_geometry_and_sharp_subfamilies.md",
    "Knowledge/objects/papers/Weyl-energy-and-connected-sums-of-four-manifolds--aac98700a100--c47de95b9e22/object.md",
    "Knowledge/objects/papers/1303.0827-Critical-metrics-on-connected-sums-of-Einstein-four-manifolds--711e2a97c44e--5258e72d2de1/object.md"
  ]
}
```

## Task

Check and strengthen the proposed next cost theory after the certified subthreshold single-blow-up cell. Verify the exact subadditivity statements for the cell infima J_{k,l}, including J_{8,7}≤7J_{1,1}+J_{1,0} and J_{8,7}≤4J_{2,0}+224π², and derive precisely what inequalities would improve the currently certified balanced upper coefficient. Then compare three routes—two blow-up interaction, blow-up–handle interaction, and the complete large-collar single-cell limit—using the inherited pure-handle rigidity, actual-field lower results, the certified cell mechanism, and relevant curvature-functional gluing literature. Identify which route gives the best combination of mathematical leverage and faithful connection to the full Einstein-gap goal. Pay special attention to whether a reduced exterior interaction for J must use the fourth-order normal equation A* A rather than the second-order linearized Einstein equation, and to any gauge or boundary-data issue that could invalidate a naive Dirichlet-to-Neumann experiment.

## Output

# Scientific Verification Memo: Cell Cost Theory After the Certified Subthreshold Cell

## 1. Subadditivity of $\mathfrak{J}_{k,\ell}$: Verification

**Geometric splitting construction.** Given two exact-CH-collar cells $C_1$ (topology $D\#k_1\overline{\mathbb{CP}}^2\#\ell_1(S^1\times S^3)$) and $C_2$ (topology $D\#k_2\overline{\mathbb{CP}}^2\#\ell_2(S^1\times S^3)$), embed both inside a single CH ball $D_0$ of sufficient radius using disjoint sub-balls $D_1, D_2 \subset D_0$. The region $D_0 \setminus (D_1^\circ \cup D_2^\circ)$ carries the exact CH metric, contributing zero to $\int |\text{Ric}+g|^2$. The combined cell has topology $D_0\#(k_1+k_2)\overline{\mathbb{CP}}^2\#(\ell_1+\ell_2)(S^1\times S^3)$ and cost $J(C_1) + J(C_2)$. Taking infima:

$$\mathfrak{J}_{k_1+k_2,\,\ell_1+\ell_2} \;\leq\; \mathfrak{J}_{k_1,\ell_1} + \mathfrak{J}_{k_2,\ell_2}.$$

The construction is valid because: (a) the collar matching is exact (the inter-cell region is genuinely CH), (b) the topology combines correctly (connected sums performed inside the contractible $D_0$ commute and produce the standard topology), and (c) the cost integral is exactly additive with no junction contribution.

**Specific inequalities:**

$\mathfrak{J}_{8,7} \leq 7\mathfrak{J}_{1,1} + \mathfrak{J}_{1,0}$: Apply subadditivity as $(8,7) = (1,1) + (1,1) + \cdots + (1,1) + (1,0)$ with seven copies of $(1,1)$ and one copy of $(1,0)$. This is correct.

$\mathfrak{J}_{8,7} \leq 4\mathfrak{J}_{2,0} + 224\pi^2$: Apply subadditivity as $(8,7) = (8,0) + (0,7)$, then $(8,0) = (2,0) + (2,0) + (2,0) + (2,0)$. Combined with $\mathfrak{J}_{0,7} = 32\pi^2 \cdot 7 = 224\pi^2$ (from pure-handle rigidity, Step 11 §3). This is correct.

$\mathfrak{J}_{8,7} \leq 8\mathfrak{J}_{1,0} + 224\pi^2$: The "separated construction" bound, using $(8,0) \leq 8 \cdot (1,0)$ and $(0,7) = 224\pi^2$. This is correct and is the bound used for the current O11 result.

**An inequality that does NOT follow from subadditivity alone:** Whether $4\mathfrak{J}_{2,0} < 8\mathfrak{J}_{1,0}$ (i.e., $\mathfrak{J}_{2,0} < 2\mathfrak{J}_{1,0}$) is the strict subadditivity question for multi-blow-up cells. Subadditivity gives only $\mathfrak{J}_{2,0} \leq 2\mathfrak{J}_{1,0}$, with equality entirely possible if no interaction gain exists.

## 2. Precise Improvement Conditions for the Balanced Coefficient

The balanced family gives $\limsup \alpha(M_j)/h_j \leq \mathfrak{J}_{8,7}/(72\pi^2)$. With the separated bound:

$$c_{\rm sep} = \frac{8\mathfrak{J}_{1,0} + 224\pi^2}{72\pi^2} = \frac{28}{9} + \frac{\mathfrak{J}_{1,0}}{9\pi^2}.$$

Setting $\mathfrak{J}_{1,0} = 8\pi^2(1-\eta)$: $c_{\rm sep} = 4 - 8\eta/9$.

**Improvement channels and their quantitative effects:**

| Mechanism | Condition | Coefficient improvement |
|---|---|---|
| Single-cell optimization | $\eta \to \eta'$ | $8(\eta'-\eta)/9$ |
| Two-blow-up interaction | $\mathfrak{J}_{2,0} < 2\mathfrak{J}_{1,0}$ | $(2\mathfrak{J}_{1,0} - \mathfrak{J}_{2,0})/(18\pi^2)$ |
| Mixed blow-up/handle | $\mathfrak{J}_{1,1} < \mathfrak{J}_{1,0} + 32\pi^2$ | $7(\mathfrak{J}_{1,0} + 32\pi^2 - \mathfrak{J}_{1,1})/(72\pi^2)$ |
| Full mixed block | $\mathfrak{J}_{8,7} < 8\mathfrak{J}_{1,0} + 224\pi^2$ | Direct reduction |

**To reduce the coefficient below $28/9$:** One would need $\mathfrak{J}_{8,7} < 224\pi^2$, which requires the blow-up topology to produce a net *subsidy* for the handles, not merely a cheaper blow-up cost. The relative identity from equation (1.2) of the continuation file,

$$J - 8\pi^2 q = \int_C\!\Bigl(\tfrac{(s+3)^2}{3} + 1 + 4|W^+|^2\Bigr) - 4d,$$

shows this requires $\int_C(\ldots) < 4d + 224\pi^2$ for a $(8,7)$-cell with $q = 36$. Since the integrand equals $4$ on the CH collar, this is $4(v - d) + \int_{\text{core}}(\ldots) < 224\pi^2$ where $v$ is the cell volume. For large collar ($d$ large), the collar contribution $4(v-d)$ can be made as large as desired, so the constraint binds on the core. Whether the core can be made cheap enough is a genuine open question that requires understanding how $|W^+|^2$ and $(s+3)^2$ trade off against the topological terms.

## 3. Comparison of Three Routes

### Route 1: Two-blow-up interaction ($\mathfrak{J}_{2,0} < 2\mathfrak{J}_{1,0}$?)

**Relevant literature.** The Malchiodi–Malizia paper (arxiv:2505.17752) proves that for the *Weyl functional* $\mathcal{W} = \int |W|^2$, the connected sum $Y = M\#Z$ satisfies $\mathcal{W}(g_Y) < \mathcal{W}(g_M) + \mathcal{W}(g_Z)$ when neither factor is LCF and they are not both SD or both ASD. The mechanism is a biharmonic interpolation in a thin neck, producing an interaction energy

$$-\frac{4\pi^2}{9}\lambda^2\, W^{\bar{M}}(p) \circledast W^Z(q)\, a^4 + O(a^{9/2}\gamma^{-5})$$

at leading order (their Proposition 5.13), where $\lambda$ is a relative scaling parameter.

Gursky–Viaclovsky (arxiv:1303.0827) prove a more refined version for the combined functional $\mathcal{B}_t = \int |W|^2 + t\int R^2$: the leading term of the Kuranishi map is (their Theorem 1.1)

$$\lambda_1(a) = \Bigl(\tfrac{2}{3}W(z_0) \circledast W(y_0) + 4t\,R(z_0)\,\text{mass}(g_N)\Bigr)\omega_3\, a^4 + O(a^{6-\epsilon}).$$

**Obstruction to direct transfer.** Neither result applies directly to the Ricci defect functional $J = \int|\text{Ric}+g|^2$ on cells:

(a) *Conformal invariance breaks.* The Weyl energy is conformally invariant; $J$ is not. The biharmonic interpolation technique relies on the linearized Bach operator being the bilaplacian on TT tensors at the flat metric (Malchiodi–Malizia eq. (2.20)). For $J$, the linearized operator around CH involves the Lichnerowicz Laplacian and scalar terms that do not factorize as a bilaplacian.

(b) *Cell vs. closed manifold.* Both references work on closed manifolds. Adapting to cells with boundary requires solving the gauged fourth-order problem with Dirichlet + Neumann boundary conditions, introducing boundary terms absent from the closed-manifold expansion.

(c) *Background curvature.* The Malchiodi–Malizia expansion uses conformal normal coordinates at the Euclidean metric. On a CH background with $\text{Ric} = -g$, the curvature terms in the expansion are $O(1)$, not perturbative.

**What would be needed.** A two-blow-up interaction theorem for $J$ on CH cells would require: setting up the biharmonic interpolation for the full fourth-order operator $A^*A$ (where $A = \text{Ric}' + \text{id}$ is the linearized Einstein defect, see §5 below); computing the boundary terms from the cell collar; and evaluating the interaction $W_{\rm CH} \circledast W_{\rm cell}$. The CH Weyl tensor has both $W^+ \neq 0$ and $W^- \neq 0$ (it is Kähler-Einstein in one orientation but not conformally flat), so the non-degeneracy condition of Malchiodi–Malizia (Theorem 1.1) is satisfied.

**Assessment:** Genuine mathematical content exists here—the Weyl interaction is nonzero—but the technical adaptation is substantial. The expected gain per blow-up is modest (the interaction is $O(a^4)$ where $a$ is the neck parameter, contributing a multiplicative correction to the per-blow-up cost).

### Route 2: Blow-up–handle interaction ($\mathfrak{J}_{1,1} < \mathfrak{J}_{1,0} + 32\pi^2$?)

**Inherited structural obstruction.** The continuation file (§4 of `20260928_relative_cell_cost.md`) establishes:

$$\tfrac{2d}{3} - W_C = 12\pi^2 k - B_C \leq 12\pi^2 k.$$

Handles contribute $4\ell$ to $q = k + 4\ell$ but provide zero additional self-dual-Weyl-depletion budget. Only blow-ups contribute $12\pi^2 k$ of potential Weyl depletion. A mixed saving requires that handle topology changes how the blow-up-funded depletion is used—a collective effect with no identified mechanism.

**Pure-handle rigidity.** The Step 11 proof that $\mathfrak{J}_{0,\ell} = 32\pi^2\ell$ (strict for smooth cells, attained in the shrinking limit) is exact. This means the handle cost $32\pi^2$ per unit is a hard floor for isolated handles. Reducing it requires coupling to blow-up topology.

**Assessment:** No construction or spectral argument suggests such coupling exists. The route is speculative.

### Route 3: Large-collar single-cell limit ($\eta_\infty = \lim_{X\to\infty}(1 - \mathfrak{J}_{1,0}^X/(8\pi^2))$?)

**Existing data.** The frozen witnesses give $\eta_8 \approx 8.84 \times 10^{-4}$ and $\eta_{16} \approx 1.10 \times 10^{-3}$. The increment $\Delta\eta \approx 2.1 \times 10^{-4}$ from doubling the collar parameter $X$ suggests diminishing but nonzero returns.

**Mathematical structure.** The single-blow-up perpendicular cell is governed by a coupled ODE system for three profile functions $(F, G, w)$ on $[x_0, X]$, subject to bolt conditions at $x_0$ and $C^3$-matching to CH at $X$. The desingularized Ricci formulas (Step 10 §2) show that the integrand $\sum_a (R_{aa}+6)^2$ is a smooth function of the profile and its first two derivatives, analytic on a complex neighborhood of $[0,1]$ in the $u = \log(x/x_0)/\ell$ coordinate. The Arb integration exploits this analyticity via Gauss-Legendre quadrature with rigorous complex-ellipse error bounds.

Increasing the number of Chebyshev parameters from 8 to, say, 12 or 16 per profile function would enlarge the optimization space. Increasing $X$ beyond 16 would extend the collar, allowing more "room" for the profile to distribute the Ricci defect. The optimization infrastructure (JAX gradient descent + Arb certification) scales favorably.

**Theoretical limit.** The question of $\lim_{X\to\infty}\inf_{\rm profiles} J_X/(8\pi^2)$ is related to the spectral theory of the linearized Ricci defect operator on the half-complete CH metric $\{x \geq x_0\}$. If the essential spectrum of this operator starts at $0$, the infimum over profiles could approach $0$ as $X \to \infty$, meaning $\eta_\infty$ could be arbitrarily close to $1$. If there is a spectral gap, $\eta_\infty$ would be bounded away from $1$. The former scenario would make the single-blow-up route sufficient to bring the balanced coefficient arbitrarily close to $28/9$; the latter would cap its contribution and force consideration of Routes 1–2 for further improvement.

**Assessment:** Highest immediate leverage. Every increment in $\eta$ directly improves the certified coefficient by $8\Delta\eta/9$. The infrastructure exists and the computation is rigorously certifiable.

## 4. The Reduced Exterior Interaction: $A^*A$ vs. $A$

This is the most substantive technical point for Route 1.

**The linearized Einstein operator.** Around a metric $g_0$ with $\text{Ric}(g_0) = -g_0$, the linearization of $E(g) = \text{Ric}(g) + g$ is (in a suitable gauge):

$$Ah = -\tfrac{1}{2}\Delta_L h + h + \text{(gauge corrections)},$$

a second-order elliptic operator. Here $\Delta_L h_{ij} = \Delta h_{ij} + 2R_{ikjl}h^{kl} - \text{Ric}_{ik}h^k{}_j - \text{Ric}_{jk}h^k{}_i$ is the Lichnerowicz Laplacian.

**The cell variational problem.** Minimizing $J = \int_C |E(g)|^2$ over smooth metrics on $C$ with prescribed CH boundary data gives the Euler-Lagrange equation:

$$A^*_g\, E(g) = 0 \quad\text{in } C^\circ,$$

where $A^*_g$ is the formal $L^2$-adjoint of $A_g$. At a near-CH metric $g = g_{\rm CH} + h$, expanding $E(g) = Ah + Q(h)$ gives:

$$A^*(Ah + Q(h)) = 0.$$

At leading order this is $A^*Ah = 0$, a *fourth-order* equation with symbol $|\xi|^4$.

**Why $A$ alone gives the wrong problem.** The second-order equation $Ah = 0$ asks for an infinitesimal Einstein deformation. By the nonattainment result (continuation file, Proposition 2 = §8): no smooth cell with $q > 0$ and exact CH collar has a metric satisfying $A^*A = 0$ in the strong form $Ah = 0$ globally. The proof uses unique continuation for the elliptic system $\Delta_- E + 2\text{Rm}(E) - \frac{1}{2}|E|^2 g = 0$ from the open CH collar, combined with Chern-Weil topology. An Einstein metric on the cell would force the full closed extension to be locally CH, contradicting $k > 0$ or $\ell > 0$.

So the minimum of $J$ is achieved by a metric where $E \neq 0$ but $A^*E = 0$—the fourth-order condition. This is the crucial distinction.

**Boundary conditions for $A^*A$.** For a second-order Dirichlet problem, one prescribes the metric on $\partial C$ (one boundary condition per component). For the fourth-order problem $A^*A h = 0$, one needs Dirichlet + Neumann data (metric and normal derivative on $\partial C$)—four boundary conditions per component in total. The exact-CH-collar condition prescribes both: the metric equals CH and all its derivatives match CH to infinite order on the collar.

A naive "Dirichlet-to-Neumann experiment" that prescribes only the induced metric on $\partial C$ and varies the interior metric freely would be *under-determined* for the fourth-order problem—the Neumann data (second fundamental form, or equivalently the normal derivative of the 4-metric) remains free. If one attempted to match two cells across a common boundary using only Dirichlet data, the normal derivatives would generically disagree, creating a distributional (delta-function) contribution to $J$ at the junction. This would invalidate any energy estimate that treats the cells as independent.

**Gauge matching across boundaries.** The Gursky–Viaclovsky gauge adds the term $\mathcal{K}_{g+h}\delta_g\mathcal{K}_g\delta_g\stackrel{\circ}{h}$ to make the total equation elliptic (their equation 3.6, Proposition 3.3). This gauge must be consistent across any boundary where two cells meet. On the exact-CH collar, the gauge-fixing term involves the conformal Killing operator $\mathcal{K}$ of the CH metric, which has a well-understood kernel (the conformal Killing fields of $\mathbb{CH}^2$ restricted to the collar region). Any gluing construction must respect this kernel structure—the "approximate cokernel" elements $o_1, o_2, o_3$ of Gursky–Viaclovsky §10 have analogues in the CH cell setting, and the Lyapunov-Schmidt reduction must account for them.

**Concrete implication.** For Route 1 (two-blow-up interaction): the correct computation of the interaction energy between two blow-up cells must:

1. Use the fourth-order gauged operator $P_g^t(\theta) = B^t(g+\theta) + \mathcal{K}_{g+\theta}\delta_g\mathcal{K}_g\delta_g\stackrel{\circ}{\theta}$ (adapted to the CH background and cell boundary conditions).
2. Solve the biharmonic interpolation problem in the neck region for this operator, not for the simpler second-order Einstein linearization.
3. Match all four boundary conditions (Dirichlet + Neumann) at the cell-to-collar junctions.
4. Account for the cokernel elements arising from the CH background symmetries (dilations, rotations).

A computation using only the linearized Einstein operator $A$ would give the wrong variational equation, wrong boundary condition count, and wrong spectral structure for the Kuranishi map.

## 5. Recommendation and Precise Open Questions

**Recommended priority order:**

1. **Route 3 (large-collar optimization):** Increase the Chebyshev degree from 8 to 12–16 per profile, and explore $X = 32, 64, 128$. Certify each with Arb. Determine whether $\eta_X$ has a finite limit or grows without bound. This resolves the question of whether the single-blow-up route can bring $\mathfrak{J}_{1,0}$ significantly below $8\pi^2$ or only marginally so.

2. **Spectral analysis of the half-CH linearization:** Determine the spectrum of the linearized Ricci defect operator $A^*A$ (gauged, on the half-complete CH space with bolt boundary conditions). This answers the theoretical question of whether $\eta_\infty < 1$ or $\eta_\infty = 1$.

3. **Route 1 (two-blow-up interaction):** Adapt the Gursky–Viaclovsky framework to CH cells. The key computation is the leading term of the Kuranishi map for two blow-up cells embedded in a single CH ball. The interaction involves $W_{\rm CH}(z_0) \circledast W_{\rm cell}(y_0)$ evaluated using the fourth-order gauged operator on the CH background. If this interaction is negative (energy-reducing), it gives strict subadditivity $\mathfrak{J}_{2,0} < 2\mathfrak{J}_{1,0}$.

**Precise open questions whose resolution would materially advance the programme:**

(a) $\lim_{X\to\infty}(1 - \inf_{\rm profiles} J_X/(8\pi^2)) = ?$ (finite or infinite; determines the reach of Route 3)

(b) Is the spectrum of $A^*A$ on the half-CH bolt space discrete near zero? (determines whether the large-collar limit approaches a computable eigenvalue problem)

(c) Does $W_{\rm CH} \circledast W_{\rm Burns} > 0$ for the perpendicular bolt orientation? (determines sign of Route 1 interaction)

(d) Is $\mathfrak{J}_{8,7} < 8\mathfrak{J}_{1,0} + 224\pi^2$? (strict subadditivity for the actual balanced block; would improve the coefficient beyond what separated cells achieve)