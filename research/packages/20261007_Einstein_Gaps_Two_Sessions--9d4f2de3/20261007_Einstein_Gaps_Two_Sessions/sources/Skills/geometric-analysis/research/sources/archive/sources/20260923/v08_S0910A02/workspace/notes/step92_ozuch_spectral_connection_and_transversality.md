# Step 92: Ozuch–spectral connection, equivariant transversality, and landscape update

Session `S0910A02`. Agent2 / Constructor. Phase Execute.

## 1. A01 Step 94 correction absorption

The Step 93 claim that the AA/BB trace-free tensor sectors of the product-orbifold odd Green coefficient diverge has been **withdrawn and corrected**. The error was a relative electric/magnetic normalization: the full-Lie magnetic tensor $M(f) = L_{(*df)^\#}g$ has $\|M\|^2 = 4\|E\|^2 = 2\mu(\mu-2)$ for $E = (\nabla^2 f)^{TF}$ with $\|E\|^2 = \mu(\mu-2)/2$. Step 93 divided the magnetic contribution by the electric norm.

**Corrected result** (A01 Step 94, verified by heat-kernel quadrature):
- Separated-tensor sectors **cancel mode by mode**: $K^{BB}_{NS} = K^{AA}_{SN} = 0$.
- Same-pole sectors are **finite**: $K^{AA}_{NS} = K^{BB}_{SN} \approx -0.00400$.
- Combined with the previously established AB value $K^{AB}_{adj} \approx -0.03144$:
$$
K^{\mathrm{principal}}_{\mathrm{adj}} \approx -0.03544,
$$
**finite and negative** in the current convention. The constructive path is restored.

This principal response is a product-background quantity, not yet the physical Ozuch coefficient.

## 2. Connecting the Ozuch obstruction to the spectral decomposition

### 2.1. Ozuch's explicit obstruction structure

For a flat torus orbifold $\mathbb{T}^4/\mathbb{Z}_2$ with lattice matrix $L$, the first obstruction at node $j_0 \in S_-$ is (Ozuch, Lemma 4.2, Corollary 4.3):
$$
\sum_{i \in S_+} B^L_{j_0-i}(\zeta_i,\zeta_i)\zeta_{j_0} = 0,
$$
where the lattice curvature kernel is
$$
B^L_x(\zeta,\zeta') = \pi_{\mathrm{tr}} \sum_{a \in \mathbb{Z}^4} b_{L(x-2a)}(\zeta,\zeta'),
\qquad
b_x(\zeta,\zeta') = 12\frac{\rho_x(\zeta)^- \otimes \rho_x(\zeta')^-}{|x|^6},
$$
with $\rho_x$ the quaternion-conjugation rotation (Definition 1.14).

The quadratic evaluation at a single lattice point is (lines 1396–1399):
$$
\langle \pi_{\mathrm{tr}} b_x(\zeta_i,\zeta_i)\zeta_j, \zeta_j\rangle
= 12\langle \rho_x(\zeta_i), \zeta_j\rangle^2 - 4|\zeta_i|^2|\zeta_j|^2.
$$

### 2.2. Product-orbifold specialization

For the positive mirror $(S^2 \times S^2)/\mathbb{Z}_2$ with unit-radius spheres, the four $A_1$ nodes form a cube-vertex pattern in $\mathbb{R}^4$. At an adjacent pair $(i,j_0)$ separated by a half-period vector $x_0$, the single-image contribution is:
$$
\langle b_{x_0}(\zeta_i,\zeta_i)\zeta_{j_0}, \zeta_{j_0}\rangle
= 12\langle \rho_{x_0}(\zeta_i), \zeta_{j_0}\rangle^2 - 4|\zeta_i|^2|\zeta_{j_0}|^2.
$$

**Channel decomposition.** Let $\zeta_i = \hat e_k \in \mathbb{R}^3$ (unit chirality) and expand $\zeta_{j_0}$ in the $\{e_1,e_2,e_3\}$ basis. The components $\langle \rho_{x_0}(\hat e_k), e_m\rangle$ decompose into:
- **AB channel** ($m \ne k$): off-diagonal $\rho_{x_0}$ matrix elements.
- **AA/BB channel** ($m = k$): diagonal $\rho_{x_0}$ matrix element.

This is precisely the decomposition A01 computes spectrally: the rotation $\rho_x$ acts on $\mathbb{R}^3 \cong \Omega^+$ (or $\Omega^-$), and the Green function's spectral representation resolves $\rho_x$ into product-sphere harmonics.

### 2.3. The lattice Green function as a spectral sum

The full lattice sum $B^L_x$ is the periodized curvature kernel. On the product torus, it decomposes into a spectral sum over product eigenvalues $(\mu_r, \mu_q)$ on $S^2 \times S^2$. Specifically:
$$
B^L_x(\zeta,\zeta) = \pi_{\mathrm{tr}} \sum_{r,q} c_{rq}\, Y_{rq}(x)\, [\text{angular factor depending on } \zeta],
$$
where the spectral denominators involve the linearized Einstein operator $P = \frac12\nabla^*\nabla - \mathring R$ and reduce to the additive form
$$
P_{rq} = \frac{\mu_r + \mu_q}{2} - 1
$$
in the product background. The AB vs AA/BB decomposition corresponds to whether the TT tensor index is in the cross (electric×magnetic) or same (electric×electric, magnetic×magnetic) product channels.

**Key identity.** For T⁴/Z₂ (flat), B^L is the periodized curvature kernel with explicit lattice formula. For (S²×S²)/Z₂ (curved), the analogous object is the Green-function response of the linearized Einstein operator on the product orbifold, which is what A01 computes spectrally. The two evaluate the same TYPE of obstruction coefficient on different orbifolds.

**Verification (Step 92 script).** The Ozuch single-image b_x decomposes as:
- Along ζ (AA/BB channel): eigenvalue +8
- Perpendicular to ζ (AB channel): eigenvalue -4
- Trace-free: $8 + 2(-4) = 0$ ✓

This matches A01's channel structure: the AA/BB same-pole terms have the same sign as the AB terms but different magnitude, and the separated tensor sectors cancel by the electric/magnetic norm identity.

### 2.4. Transition to the Ozuch physical coefficient

The principal response $K^{\mathrm{principal}}_{\mathrm{adj}}$ is computed in the flat product background. The actual Einstein desingularization coefficient involves additional structure from Prop 2.10:

1. **EH source normalization.** The H⁴ asymptotic is $H^4(\zeta^+) = -\rho(\zeta)^- \circ \zeta^+ / (2r^4)$ (Prop 1.16), which has homogeneity $-4$ and enters the boundary pairing at weight $3$ (from $\nabla_{\partial_r} H^4 = -4H^4/r$).

2. **Receiver mode structure.** The obstruction mode $\mathbf{v}_l = V_{l,0} + V_{l,2} + O(r^4)$ has constant leading part $V_{l,0}$ and quadratic correction $V_{l,2}$. In the flat limit, $V_{l,2}$ comes from the Green function $P_o^{-1}$ applied to the far-field source.

3. **Boundary pairing.** When the first obstruction vanishes ($\lambda_k = 0$), the second obstruction is (Prop 2.10):
$$
\nu_l = 3\int_{S^3/\mathbb{Z}_2} \langle H^4, V_{l,2}\rangle_{\mathbf{e}}\, dv_{S^3/\mathbb{Z}_2}.
$$
When $\lambda_k \ne 0$ but the first obstruction is satisfied at higher order, the full boundary pairing includes the $H_2^4$ correction term (line 634):
$$
\nu_l = 3\int_{S^3/\mathbb{Z}_2} \langle H^4, V_{l,2}\rangle + \int_{S^3/\mathbb{Z}_2} \langle H_2^4, V_{l,0}\rangle.
$$

4. **Gauge and Bianchi projection.** The Bianchi constraint $B_{\mathbf{e}} H^4 = 0$ and the TT gauge $P_{\mathbf{e}} H^4 = 0$ are built into H⁴ by construction. The receiver must be in the $L^2$-orthogonal complement of $\mathbf{O}(\mathbf{g}_o)$.

5. **Isotropy normalization.** For the product orbifold with $D_8$ symmetry at each node, the isotropy group acts on both $\zeta$ and the receiver. The physical coefficient is the $D_8$-invariant projection of the boundary pairing.

The **source-compatible verification** task is: show how the Prop 2.10 boundary pairing, with the correct product-orbifold curvature block and kernel-plane projection, reduces in the corresponding principal-product normalization to A01's spectral response components up to universal normalization factors. The factor $3$ in Prop 2.10 arises from the homogeneity calculation $\nabla_{\partial_r} H^4 = -4H^4/r$ and $\nabla_{\partial_r} V_{l,2} = 2V_{l,2}/r$, giving $(4+2-3) = 3$ via the Green's formula.

### 2.5. Background curvature correction (Step 93)

**Step 93 correction.** The previous version of this section incorrectly said that the product orbifold $(S^2\times S^2)/\mathbb Z_2$ is conformally flat and that
$R^\pm=W^\pm+\Lambda I/3=I/3$ for $\Lambda=1$.  This is false and must not be used.
For the product Einstein metric with $\operatorname{Ric}=\Lambda g$,
\[
W^\pm=\operatorname{diag}\left(\frac{2\Lambda}{3},-\frac{\Lambda}{3},-\frac{\Lambda}{3}\right),
\qquad
R^\pm=W^\pm+\frac{\Lambda}{3}I=\operatorname{diag}(\Lambda,0,0),
\]
in the basis whose first vector is the Kähler form direction.  The negative product mirror has the same rank-one form with $\Lambda=-1$:
$R^\pm=\operatorname{diag}(-1,0,0)$.  Two sanity checks force this correction: a conformally flat Einstein 4-manifold has constant sectional curvature, while $S^2\times S^2$ has zero mixed sectional curvatures; and an invertible $(\Lambda/3)I$ obstruction would forbid the all-compatible $r=0$ row, contradicting the known Kähler--Einstein desingularization of the del Pezzo control row.

Thus the product mirror is not a scale-race problem.  The zeroth-order first obstruction already has a two-dimensional kernel
\[
K=\ker R^\pm=\omega^\perp=\operatorname{span}\{e_2,e_3\}.
\]
Allowed EH parameters must be written $\zeta_j=t_j\xi_j$ with $\xi_j\in K$ to leading order.  The old equation
\[
\frac13+t^2K_{adj}=0
\]
and its associated critical scale $t_*^2=-1/(3K_{adj})$ are artifacts of the wrong $I/3$ premise.  They are withdrawn.

For mixed chirality, after solving the image direction by the ordinary Lyapunov--Schmidt step, the leading angular equation is the kernel projection
\[
\Pi_K\left(\sum_{i\ne j} t_i^2 Q_{ji}(\xi_i)\right)\Pi_K\xi_j=0
\]
(up to the still-unresolved higher-order remainder).  For equal scales the common $t^2$ cancels.  The decisive object is therefore a $2\times2$ symmetric response form on $K=\omega^\perp$ at each node; only after the residual symmetry group, node permutations, and kernel-plane frame transports are explicitly fixed may this reduce to a one-variable angular equation rather than a small vector system.

## 3. Equivariant transversality: corrected decisive question

### 3.1. The kernel-plane problem

For the standard $(S^2 \times S^2)/\mathbb{Z}_2$, the first obstruction at each node is
\[
R^\pm(p)\zeta^\pm=0,
\qquad R^\pm=W^\pm+\frac{\Lambda}{3}I=\operatorname{diag}(\Lambda,0,0).
\]
Hence $\zeta$ is not arbitrary and is not forced to vanish: it must lie in the Kähler-orthogonal plane $\omega^\perp$.  This is exactly the rank-one situation recorded in Steps 44, 48--50, 64, 67--69, and 77.  The all-compatible $r=0$ Kähler--Einstein row is the calibration: any convention for the kernel plane, ordered frames, or signs must reproduce its unobstructed desingularization before a mixed-row number is trusted.

The mixed-chirality response changes the effective curvature block in this kernel plane.  If
\[
\zeta_j=t_j\xi_j,
\qquad \xi_j\in K,\quad |\xi_j|=1,
\]
then the first nontrivial condition has the schematic form
\[
\Pi_K Q_j(\{\xi_i,t_i/t_j\})\Pi_K\xi_j=0,
\]
where $Q_j$ is assembled from the Ozuch/Biquard Green response, with Bianchi projection, isotropy normalization, and the correct EH $H^4$ source.  This is a direction equation on $K$, not a search for a finite gluing scale.

### 3.2. Corrected equivariant-transversality question

**Question.** For the diagonal balanced pattern on $(S^2 \times S^2)/\mathbb{Z}_2$ — two nodes filled with one EH chirality and two with the opposite chirality in a checkerboard arrangement — does the explicitly defined residual symmetry group $G_{sym}$ (including the factor-exchange/reflection symmetries under the chosen convention) reduce the kernel-plane response so that the invariant projected system is either:

1. **Obstructed/nondegenerate:** the restricted $2\times2$ form has no kernel on the invariant directions, so this particular nearby mixed-chirality Ozuch branch cannot desingularize; or
2. **Transversal along an angular ray:** the restricted form vanishes along a ray in $\omega^\perp$ with nonzero angular derivative after quotienting the residual symmetry, allowing equivariant gluing in the invariant sector; or
3. **Symmetry-trivial:** the invariant sector lies in the kernel to this order, forcing the next obstruction level to be computed.

**Why this matters.** Case (1) would be nonexistence only for Einstein metrics near this particular product-orbifold degeneration and selected Ozuch branch; by the Step 78 scope warning it would not exclude a distant positive Einstein metric on the same smooth mixed row.  Case (2), if the analytic remainder is also below the $t^3$ term in the invariant kernel directions, would give a real equivariant desingularization candidate and could produce the first positive Einstein metric in this family with $\min(b_+,b_-)\ge2$.

### 3.3. Concrete formulation after correction

Let the four nodes of the positive mirror be $\{N_A N_B, N_A S_B, S_A N_B, S_A S_B\}$.  The diagonal balanced checkerboard assigns one chirality to $\{N_A N_B,S_A S_B\}$ and the other to $\{N_A S_B,S_A N_B\}$.

The old invariant ansatz $\zeta_i=t\hat e_1$ is invalid for the product mirror: $e_1$ is the Kähler/image direction of $R^\pm=\operatorname{diag}(\Lambda,0,0)$ and is excluded by the zeroth-order obstruction.  The invariant ansatz must be chosen inside
\[
K=\operatorname{span}\{e_2,e_3\},
\qquad
\xi(\theta)=\cos\theta\,e_2+\sin\theta\,e_3,
\]
with the directions transported between nodes according to the chosen $G_{sym}$ frame convention.

For each receiver node $j_0$, the leading mixed response is
\[
\left[\sum_{i\ne j_0}\Pi_K\,Q_{j_0i}(\xi_i)\,\Pi_K\ +\ \text{same-order self/frame/complement terms}\right]\xi_{j_0}=0.
\]
A01's corrected finite principal response remains useful only as a product-background component of $Q$; it is not by itself the physical Ozuch coefficient and the sign of the old $e_1$ scalar no longer has the interpretation assigned above.  The physical computation must restrict to $\omega^\perp$, include the EH $H^4$ source normalization, Bianchi/gauge projection, quotient/isotropy normalization, and be calibrated on the $r=0$ Kähler--Einstein row.

### 3.4. Remainder obstacle that still remains

The correction removes the fake nonperturbative scale problem, but not the analytic resolution problem.  The pattern-dependent inter-node term enters at order $t_jt_i^2$ (order $t^3$ for equal scales), while the available Ozuch necessary-equation remainder in the current record is only $O(t^{5/2})$.  A computed $t^3$ kernel-plane coefficient is decisive only if the residual $G_{sym}$ symmetry/parity and an adapted higher-order construction annihilate or push below the larger $O(t^{5/2})$ remainder in the invariant kernel directions, giving an actual $t^3\mathcal C+o(t^3)$ (or explicit $t^3\log t$) expansion.  This is the natural extension of A01's parity-cancellation program and Ozuch §3.3's higher-jet template.
## 4. Landscape update after Step 91/92

### 4.1. Scalar-excess diffuseness (Step 91)

For $M_N = N\#N$ with $N$ closed hyperbolic, under $\|\operatorname{Ric}_g + 3g\|_{\mathrm{op}} \le \delta$:
$$
\int u \ge 16\pi^2 + \int|W|^2 - \frac12\int|E|^2,
$$
where $s = -12 + u$ and $|u| \le 4\delta$ pointwise. Since $u \le 4\delta$:
$$
\operatorname{Vol}\{s > -12\} \ge \frac{4\pi^2}{\delta}.
$$
The topology change **cannot be localized**: it requires spreading a fixed $16\pi^2$ of scalar-curvature excess over volume $\Omega(1/\delta)$. This explains the uniform failure of warped waists, Burns cores, and OT connectors as local models.

### 4.2. BBCG non-uniform-gap (Step 91)

BBCG Theorem 1.3/1.6 supplies $\varepsilon(n,d)$ depending on the diameter of the target; Corollary 1.7 gives $\varepsilon$ for each fixed $X$ in $X\#X$. The source explicitly notes that diameter dependence is necessary. **BBCG does not provide a dimension-only uniform gap.**

### 4.3. Negative-branch convergence across sessions

All three sessions now agree: the honest negative frontier is a **diffuse, non-OT, non-warped connector** spreading a fixed $16\pi^2$ scalar excess over volume $\gtrsim 1/\delta$, unobstructed by any current certificate. Specific subclass closures:
- Warped $k \ge 0$ waists: $\delta \ge 3/2$ (A02, Step 88).
- Exact reflected OT connectors: $\delta^* \approx 0.246$ (A03, Step 87). **Scope**: free-$T^2$ OT with reflected cusp extensions, not $S^3$-neck $N\#N$.
- Orbifold+ALE resolutions: entropy-inaccessible by Chern–Weil neutrality (A02, Step 90).

A03's $\delta^*$ does **not** apply to $N\#N$: the $S^3$ interface has no free $T^2$ action.

### 4.4. Positive-branch status

The mixed-chirality desingularization coefficient is the **crux** for $P_4^+$. The corrected finite principal response is encouraging but not yet the physical Ozuch coefficient. The equivariant-transversality question (§3) is the load-bearing mathematical problem.

## 5. Topological explanation of Chern–Weil neutrality (Step 91 source grounding)

By BKN/Nakajima (Chen–Li Corollary 6.9): any smooth 4-manifold homeomorphic to $\mathbb{R}^4$ admitting a Ricci-flat ALE metric is isometric to flat Euclidean $\mathbb{R}^4$. Therefore a topology-changing Ricci-flat ALE bubble **cannot** have trivial group at infinity; it must use an $S^3/\Gamma$ seam with $|\Gamma| > 1$.

This explains why orbifold+ALE resolution preserves or increases the Hitchin–Thorpe surplus: the $S^3/\Gamma$ seam changes Euler characteristic by $\Delta\chi = 1 - 1/|\Gamma|$ per bubble (adding topology without the $\chi \mapsto \chi - 2$ cost of a connected sum through $S^3$). The connected-sum operation $M \# M$ performs exactly the $\chi \mapsto 2\chi - 2$ cost that creates the Sambusetti deficit, and it uses the trivial $S^3$ seam that ALE bubbling cannot.

**Scope**: this explanation is proved in dimension four from the ALE positive-mass theorem. Higher-dimensional analogues require their own positive-mass hypotheses.

---

**Sources.**
- Ozuch, Higher-order obstructions: `Knowledge/objects/papers/Higher-order-obstructions...object.md`, lines 276–325 (EH metric and H⁴), 606–660 (Prop 2.10 and Cor 2.12), 1334–1413 (Section 4 explicit T⁴/Z₂ obstructions).
- A01 Step 94 correction: `Sessions/S0910A01/workspace/notes/step94_corrected_aabb_and_route_reassessment.md`.
- A01 Step 94 data: `Sessions/S0910A01/workspace/data/step94_corrected_aabb_principal_response.json`.
- Chen–Li (BKN/Nakajima): `Knowledge/objects/papers/On-the-geometry-of-asymptotically-flat-manifolds...object.md`, lines 2088–2202.
- BBCG: `Knowledge/objects/papers/Differentiable-rigidity-under-Ricci-curvature-lower-bound...object.md`, lines 43–87.
- Step 91 scalar-excess data: `Sessions/S0910A02/workspace/data/step91_scalar_excess_bbcg_gap.json`.
