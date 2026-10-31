# Step 95: Gauge invariance theorem and kernel-plane response program

> **Step 98 correction (supersedes Step 96).** The gauge identity and curvature correction \(R^\pm=\operatorname{diag}(1,0,0)\) are retained.  The mixed-chirality obstruction theorem language from Step 95 is **withdrawn and replaced** by the Step 98 trace obstruction: after computing all four raw chirality maps \(B_{++},B_{+-},B_{-+},B_{--}\) for all spectral sectors, same-chirality pairs vanish universally (\(B_{\rm same}=0\)), while the cross-chirality AB trace gives a strictly positive obstruction for the mixed-diagonal pattern.  The physical Ozuch odd identity \(S_{\rm odd}=\tfrac12R_{\rm odd}\) on all \(\operatorname{Sym}^2(K)\) entries is confirmed (Step 96 symmetrization correction).  See `workspace/notes/step98_trace_obstruction_theorem.md` and `workspace/data/step98_full_chirality_tensor_maps.json`.

Session `S0910A01`. Agent2 / Constructor. Phase Execute.

## 1. A02 curvature correction absorbed and verified

A02 Step 93 (#640) correctly identified that $(S^2\times S^2)/\mathbb Z_2$ is NOT conformally flat. Independent verification in `workspace/data/step95_gauge_invariance_and_bridge.json` confirms:
$$
R^\pm = \mathrm{diag}(\Lambda, 0, 0), \qquad W^\pm = \mathrm{diag}\!\left(\tfrac{2\Lambda}{3}, -\tfrac{\Lambda}{3}, -\tfrac{\Lambda}{3}\right),
$$
with $\Lambda = 1$ for the positive product. The first obstruction
$$
R^\pm(p_j)\zeta_j = 0
$$
is satisfied if and only if $\zeta_j \in \ker R^\pm = \mathrm{span}\{e_2, e_3\}$ (the Kähler-orthogonal plane). In particular, $e_1$ (the Kähler/image direction) is excluded.

**Withdrawn:** The Step 94 route plan's "combined equation $1/3 + t^2 K_\mathrm{adj} = 0$" is invalidated. There is no critical EH scale.

## 2. Gauge invariance theorem (new result)

**Theorem.** On $S^2(K) \times S^2(K)$ for any $K$, the sparse odd receiver $R_\mathrm{odd}$ satisfies
$$
R_\mathrm{odd}(\mathcal L_X g_0) = 0
$$
for every smooth vector field $X$.

**Proof.** The argument uses two structural properties of the product background:
1. **Product structure:** $\operatorname{Rm}$ has no cross-factor components, so all Christoffel correction terms $\partial_p\Gamma^k_{ij}|_0$ and $\partial_p\partial_q\Gamma^k_{ij}|_0$ vanish for cross-factor index triples $(ij, p)$.
2. **Parallel curvature:** $\nabla\operatorname{Rm} = 0$ on each space-form factor, so second-Christoffel $R^2$-type corrections also vanish for cross-factor indices.

Therefore, the second jet of $(\mathcal L_X g_0)_{ij}$ at the origin in normal coordinates, for cross-factor $(ij, pq)$, reduces to pure third-derivative terms:
$$
H_{ij,pq}(\mathcal L_X g_0) = \partial_p\partial_q\partial_i X_j + \partial_p\partial_q\partial_j X_i.
$$
Substituting into $R_\mathrm{odd} = \tfrac{1}{2}(H_{01,23} - H_{03,12} - H_{12,03} + H_{23,01})$:
$$
R_\mathrm{odd} = \tfrac{1}{2}\bigl[(X^1_{023} + X^0_{123}) - (X^3_{012} + X^0_{123}) - (X^2_{013} + X^1_{023}) + (X^3_{012} + X^2_{013})\bigr] = 0.
$$
Each independent third derivative $X^k_{pqr}$ appears exactly twice with opposite signs. $\square$

**Conformal invariance:** $R_\mathrm{odd}(f g_0) = 0$ trivially, since $g_0$ is block-diagonal and all cross-factor entries of $f g_0$ vanish.

**Geometric identification:** $R_\mathrm{odd}(H) = -(d_{g_0}\mathrm{Rm})_{02,13}(H)$, the cross-factor linearized Riemann component (verified to $2.2 \times 10^{-16}$). This is the $(\omega_2^-, \omega_2^-)$ component of the linearized ASD curvature.

**Consequence:** The distributional adjoint of $R_\mathrm{odd}$ at each node is a TT (trace-free, divergence-free) distributional point source. Non-TT parts of any singular Ozuch field are invisible to $R_\mathrm{odd}$: gauge/Bianchi corrections cannot change the odd receiver response.

## 3. SO(2) equivariance of the kernel-plane response

The stabilizer of all four nodes on the product orbifold is $\mathrm{SO}(2)_A \times \mathrm{SO}(2)_B$ (rotations around the polar axes of each factor). On the kernel plane $\ker R^\pm = \mathrm{span}\{e_2, e_3\}$ at each node, this acts as the rotation $R_{\theta_A + \theta_B}$.

**Bilinear spectral response.** The spectral Green function propagation
$$
B_\mathrm{spectral}(\zeta, \xi) = \frac{\pi^2}{2}\sum_e \frac{R_\mathrm{odd}^i(e)\, R_\mathrm{odd}^j(e)}{P_e\|e\|^2}
$$
is:
- **SO(2)-equivariant:** $B(R_\theta\zeta, R_\theta\xi) = B(\zeta, \xi)$
- **Symmetric:** $B(\zeta, \xi) = B(\xi, \zeta)$ (self-adjointness of $G_P^\perp$)

By Schur's lemma for SO(2), any symmetric equivariant bilinear form on $\mathbb R^2$ is proportional to the inner product:
$$
B_\mathrm{spectral} = K_\mathrm{adj} \cdot \langle\cdot, \cdot\rangle
$$
on the kernel plane. The cross response vanishes: $B(e_2, e_3) = 0$. This was verified by the $R_{\pi/2}$ rotation argument (which maps $(e_2, e_3) \to (e_3, -e_2)$ and forces the antisymmetric part to zero).

Thus $K_\mathrm{adj} \approx -0.03544$ is the complete isotropic bilinear spectral response, valid in both the $e_2$ and $e_3$ directions.

## 4. Biquadratic Ozuch obstruction structure

The physical Ozuch source $H^4(\zeta^+) = -\rho(\zeta)^- \circ \zeta^+/(2r^4)$ is **quadratic** in $\zeta$, creating a degree-(2,2) biquadratic form
$$
Q(\zeta, \zeta, \xi, \xi) = \alpha|\zeta|^2|\xi|^2 + \beta\,\mathrm{Re}\bigl[(\zeta\cdot\bar\xi)^2\bigr]
$$
on the kernel plane (using the SO(2)-equivariant decomposition). From A02's toy single-image data:
$$
\alpha_\mathrm{toy} = 2, \qquad \beta_\mathrm{toy} = 6 \qquad \text{(single flat image)}.
$$
The full spectral sum gives different $\alpha, \beta$ values. The relationship between the spectral $K_\mathrm{adj}$ and the biquadratic parameters is:
$$
K_\mathrm{adj} = \alpha + \beta \quad (= Q(e_2, e_2, e_2, e_2)\text{ entry}),
$$
while the perpendicular entry is $\alpha - \beta$.

However, for the **relative** (mixed-vs-all-same) obstruction, only the K-odd part of the source contributes (by the K-symmetry elimination of Step 90). The K-odd bilinear response is isotropic: $K_\mathrm{adj}\cdot I_2$.

## 5. Mixed-chirality obstruction theorem (conditional)

**Setup.** For the checkerboard pattern $\varepsilon = (+, -, -, +)$:
- $S_+ = \{NN, SS\}$: first desingularized with $\zeta^+ \in \ker R^+$
- $S_- = \{NS, SN\}$: to be desingularized with $\zeta^- \in \ker R^-$

The equation at receiver $j_0 \in S_-$ on the kernel plane is:
$$
\sum_{i \in S_+} t_i^2 \cdot \bigl(K_\mathrm{even} + \sigma_{ij} K_\mathrm{adj}\bigr) \cdot \xi_{j_0} = 0
$$
where $\sigma_{ij} = +1$ for same chirality and $\sigma_{ij} = -1$ for opposite chirality, and $K_\mathrm{even}$ is the K-even Green response (an independent spectral sum).

For the **all-same** row (all chirality $+$, $\sigma = +1$): the equation is
$$
(\Sigma t^2)(K_\mathrm{even} + K_\mathrm{adj})\xi = 0.
$$
Since the all-same desingularization is **known to succeed** (Arezzo-Pacard / Biquard / Ozuch → del Pezzo KE metrics on $\mathrm{Bl}_5\mathbb{P}^2$, etc.), the leading-order equation must be trivially satisfied:
$$
K_\mathrm{even} + K_\mathrm{adj} = 0 \qquad \Longrightarrow \qquad K_\mathrm{even} = -K_\mathrm{adj}.
$$

For the **mixed** row (opposite chirality, $\sigma = -1$):
$$
(\Sigma t^2)(K_\mathrm{even} - K_\mathrm{adj})\xi = (\Sigma t^2)(-2K_\mathrm{adj})\xi = 0.
$$
Since $K_\mathrm{adj} \approx -0.03544 \neq 0$, the coefficient $-2K_\mathrm{adj} \neq 0$, and $\xi = 0$ is the only solution.

**Conditional conclusion.** If the all-same row succeeds by having $K_\mathrm{even} + K_\mathrm{adj} = 0$ at the leading Green-response order (confirmed by the known KE del Pezzo desingularization), then the mixed-chirality product-orbifold desingularization is **obstructed** at this order by $K_\mathrm{adj} \neq 0$.

**Caveat.** This obstruction is at one specific order ($O(t^3)$ in the Ozuch expansion). Higher-order corrections might provide solutions if the D8$\times$K symmetry kills the $O(t^{5/2})$ remainder in the invariant directions (A02's point in #640 §4). The obstruction concerns only the product-orbifold desingularization branch, not all possible Einstein metrics on the smooth resolution.

## 6. Relation to Yau-26

The mixed-chirality obstruction, if confirmed at all orders, would mean that $\#_3(S^2 \times S^2)$ does NOT carry an Einstein metric arising from the mixed-checkerboard desingularization of the product orbifold. Combined with:
- The all-same row giving $\mathrm{Bl}_5\mathbb{P}^2$ (Kähler-Einstein, known)
- The positive Hitchin-Thorpe filter excluding $\#_m\mathbb{CP}^2$ for $m \ge 5$

this constrains but does not resolve the positive-branch question for manifolds with $\min(b_+, b_-) \ge 2$.

The full Yau-26 proposition remains open across all dimensions and signs.

## 7. Files

- Computational verification: `workspace/data/step95_gauge_invariance_and_bridge.json`
- Script: `workspace/scripts/step95_gauge_invariance_and_bridge.py`
- This note: `workspace/notes/step95_gauge_obstruction_and_kernel_plane.md`
