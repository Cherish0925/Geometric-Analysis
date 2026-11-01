# TTCS Independent Branch Record

```json
{
  "step_id": 39,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step39_actual_harmonic_zero_test_and_route_comparison.md",
    "Sessions/S1003A01/workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md",
    "Sessions/S1003A01/workspace/notes/step19_exterior_null_line_LM_stationary_cells.md",
    "Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md",
    "Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md",
    "Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md",
    "Skills/geometric-analysis/references/results-and-questions.md"
  ]
}
```

## Task

Develop a mathematically concrete proof/construction framework for the localized-to-diffuse transition of the actual harmonic-zero configuration described in Step 39. The first target is a pure blow-up tower of compact complex-hyperbolic hosts, outside the inherited linear window. Use one realizable closed metric and its glued harmonic form, not a formal nowhere-zero zero-period field. Give: a precise domain decomposition (host-like bulk, zero/bolt cores, interfaces), candidate quadratic forms or Dirichlet-to-Neumann maps including full metric first jets and harmonic-form flux, the role of cover-uniform CH coercivity and its field-selection caveat, possible collective low modes/compliance scaling with A and k, and a cheapest discriminating calculation or theorem that can tell whether O(k) core cost can become o(k). Keep lower estimates distinct from upper constructions and keep eta/exceptional periods/zero sets separate. Relate any proposed route back to P and the normalized Einstein defect. Do not assume the cap route or density-free O10 is the same problem.

## Output

# Localized-to-Diffuse Transition: Framework and Discriminating Mechanisms

## 1. The precise discrimination target

On $M = X_\Gamma \# k\overline{\mathbb{CP}}^2$ with $X_\Gamma$ a compact ball quotient, $A = c_1^2(X_\Gamma)$, $V = 2\pi^2 A$, pure blow-ups have $Q = k$, $\theta = 1$, $r = 0$, hence $\sigma = 18$: outside the inherited linear window ($\sigma < 4 + c_0$). The certified perpendicular cell gives the localized upper construction $P/(8\pi^2) \leq 4.082\,k/A$, which is $O(k)$. The question bifurcates cleanly:

**Lower side.** Must $\alpha(M) \geq c \cdot k/A$ for some $c > 0$ independent of the cover tower? Equivalently, is the per-blow-up cost $P_{\text{per cell}}/(8\pi^2)$ bounded below?

**Upper side.** Can a coupled metric–form construction achieve $P/(8\pi^2) = o(k)$ as $A \to \infty$ with $k/A$ fixed?

The two questions are not logically symmetric: the lower question requires a proof for every metric; the upper question needs only one realizable family. I develop below the analytical structure that determines which answer holds, together with the cheapest discriminating inputs.

---

## 2. Domain decomposition with precise operator content

Fix a competitor metric $g$ on $M$ and a sign class $\epsilon$ for the monopole equations. Choose disjoint geodesic-ball cores $C_i$ (radius $R_0 \sim 2$ in the $s = -4$ scale, containing the topological neck) around each exceptional sphere $E_i$, interface annuli $\mathcal{A}_i = B_{2R_0}(x_i) \setminus C_i$, and the bulk $\Omega_B = M \setminus \bigcup \overline{B_{2R_0}(x_i)}$.

**On each interface $\Sigma_i = \partial C_i$, the matching data are:**

(a) *Metric first jet:* the induced metric $\gamma_i$ and second fundamental form $K_i$, equivalently the full 1-jet of $g$ restricted to $\Sigma_i$. These determine the Ricci tensor's boundary contributions.

(b) *Harmonic-form flux:* for a self-dual harmonic form $\psi$, the tangential restriction $\psi_T|_{\Sigma_i}$ and normal derivative $\nabla_\nu \psi|_{\Sigma_i}$, forming the Cauchy data of the elliptic Hodge system $\Delta_H \psi = 0$, $d^+\psi = 0$. In the SU(2)-symmetric model these reduce to the scalar traces $(q, q', u, u')$ of Step 29's $B$-interface.

(c) *Monopole data:* the restriction $(A_\epsilon, \Phi_\epsilon)|_{\Sigma_i}$ modulo gauge, equivalently the amplitude $\rho_i = |\Phi|^2/2$ and direction $n_i$ with their normal derivatives. The Weitzenböck bound $\int_M (|\Phi|^2 + s)^2 \leq \int s^2 - 32\pi^2 c_1^2$ is extensive and does not force bulk-closeness of the field to the canonical KE solution.

**The decomposed functional:**
$$P = P_B + \sum_{i=1}^k P_{C_i} + \text{cross terms from interface regularity}$$
where $P_B = \int_{\Omega_B} |\operatorname{Ric}^\circ|^2$ and $P_{C_i} = \int_{C_i} |\operatorname{Ric}^\circ|^2$. The cross terms vanish for a partition of unity and reappear as boundary contributions in the Bochner/integration-by-parts formulas. The key example is the Step-29 interface conversion $B$: the local AKΓ tail integral differs from the raw Ricci tail by the flux $B(\text{entry}) - 2$, which is $O(10^{-3})$ at $x = 10$ but represents 96% of the positive AK tail (§2 of Step 29). Any domain-decomposed lower bound must either use the raw $P$ splitting or carefully track these interface conversions.

---

## 3. Perturbative bulk compliance and the additivity principle

**The mechanism.** Each optimized cell has a far-field charge $\lambda \approx 0.183$ (Step 19, §4): the cell metric is not asymptotically Einstein at linear order but carries an antisymmetric mode $v_- \sim f_- \cdot (\text{const} - 2\lambda \log x)$ decaying at rate $x^{-3/2}\log x$. This charge is the Lagrange multiplier conjugate to the exterior trace: $\lambda = -\delta / I(\rho)$ with $\delta$ the boundary mismatch from the mass null line and $I(\rho)$ the exterior integral kernel.

A global bulk deformation $h$ (TT tensor on the host) modifies each cell's boundary conditions. The cost–benefit calculation is:

**Bulk cost.** By the Koiso gap (G1 in Step 44), the Einstein operator on ball quotients satisfies $\langle L_E h, h \rangle \geq \frac{|\lambda|}{3}\|h\|^2$ pointwise on TT tensors, with $|\lambda|/3 = 1/3$ at $s = -4$. Hence
$$P_B \geq \kappa_0 \|h\|_{H^2}^2, \qquad \kappa_0 = \kappa_0(\mathbb{CH}^2, i_0),$$
cover-uniform (from the pointwise Bochner potential, not a spectral gap that might degenerate along towers).

**Per-cell benefit.** A smooth bulk perturbation of amplitude $\varepsilon = \|h\|_{C^0(\Sigma_i)}$ modifies the cell boundary trace by $O(\varepsilon)$. The cell cost's gradient in the $\lambda$-direction gives a first-order saving $\sim \lambda \varepsilon$ per cell. The total benefit from $k$ cells is $\lesssim k\lambda \varepsilon$.

**Sobolev mediation.** In dimension four, $H^2 \hookrightarrow C^0$ with $\|h\|_{C^0} \leq C(i_0)\|h\|_{H^2}$. But the $H^2$ norm is a global integral: $\|h\|_{H^2}^2 = \int_{\Omega_B}(|h|^2 + |\nabla h|^2 + |\nabla^2 h|^2)$. A spatially constant perturbation $h = \varepsilon \cdot h_0$ (with $h_0$ a fixed TT tensor normalized to $\|h_0\|_{C^0} = 1$) has $\|h\|_{H^2}^2 \geq \kappa_0 \varepsilon^2 V$ because the zeroth-order potential dominates.

**Optimization.** Net saving $= k\lambda\varepsilon - \kappa_0 \varepsilon^2 V / 2$. The optimum is
$$\varepsilon^* = \frac{k\lambda}{2\kappa_0 V}, \qquad \text{net improvement} = \frac{k^2\lambda^2}{4\kappa_0 V} = \frac{k^2\lambda^2}{8\pi^2\kappa_0 A}.$$

This is $O(k^2/A)$, a quadratic-in-$k$ correction to the $O(k)$ localized cost. The per-blow-up cost becomes
$$P_{\text{per cell}}/(8\pi^2) = c_0 - O(k/A),$$
which remains $\Theta(1)$ for $k \ll A$. The diffuse perturbative mode reduces the coefficient slightly but does not change the scaling.

**Green's function picture.** The Einstein operator's Green's function on $\mathbb{CH}^2$ decays as $G_E(x,y) \sim e^{-r\sqrt{\mu}}/r$ where $\mu = 1/3$ (the Koiso mass) and $r = d(x,y)$. Cell–cell interactions through the bulk are
$$\sum_{i\neq j} \lambda_i \lambda_j G_E(x_i, x_j),$$
which are exponentially suppressed when inter-site distances exceed $1/\sqrt{\mu} = \sqrt{3}$. For $k$ cells on a host of volume $2\pi^2 A$, the typical inter-site distance is $(A/k)^{1/4}$, which exceeds $\sqrt{3}$ when $k < A/9$ (well within the open range). The perturbative cost is therefore additive up to exponentially small corrections:
$$P \geq k\cdot c_0 - O(k^2/A) - O(k \cdot e^{-c(A/k)^{1/4}}).$$

This is the **additivity principle**: the cover-uniform Koiso gap prevents collective low modes from coupling sparse cells, and each cell pays its individual tariff.

---

## 4. Field selection: the genuine obstruction to closing the lower bound

The perturbative compliance argument (§3) assumes the metric is globally $\varepsilon_0$-close to $g_\Gamma$ on $\Omega_B$ and the monopole is close to the canonical branch there. Both assumptions can be violated:

**Metric escape.** An arbitrary competitor metric on $M$ need not be anywhere close to $g_\Gamma$. A metric that is far from KE everywhere has $P \geq \varepsilon^2 V$ for some effective $\varepsilon$, which is large — but only if $\varepsilon$ is bounded below. The Cheeger–Tian theory gives metric regularity from bounded $\int |Rm|^2$, but this integral is not directly controlled by $P$ (the full Riemann curvature includes Weyl and scalar parts that can be large while Ricci is small).

However, the Chern–Weil identity $\frac{1}{8\pi^2}\int |Rm|^2 = 2\chi - \frac{1}{4\pi^2}\int |\operatorname{Ric}^\circ|^2 + \frac{1}{8\pi^2}\int |W|^2 + \frac{1}{96\pi^2}\int s^2$ gives $\int |Rm|^2 = 16\pi^2\chi + \text{topological} + O(P)$ on the Yamabe representative — so $\int |Rm|^2$ is topologically controlled. For the blow-up family, $\chi = A/3 + k$, so $\int |Rm|^2 = O(A)$. Combined with volume $V = O(A)$, the Chern–Gromov compactness gives subsequential convergence of near-minimizers; but the limit could be an orbifold or collapsed space, and the geometry near exceptional spheres can degenerate.

**Monopole depletion.** Even when the metric is bulk-close to $g_\Gamma$, the monopole amplitude $\rho$ can deplete ($\rho \ll 2$) on unit-scale regions. The Weitzenböck $L^2$ bound is
$$\int (\rho - 2)^2 \leq \int (|\Phi|^2 + s)^2 / 4 \leq \frac{1}{4}\left(\int s^2 - 32\pi^2 c_1^2\right) = O(A),$$
so the average depletion is $O(1)$ — it does not force $\rho \approx 2$ everywhere. A near-minimizer with $P \ll k$ has (from Step 39's depletion law) $\int (2 - \rho)_+ \gtrsim (1-c)k$, confirming that depletion is required. But depletion on the KE-close bulk means the monopole direction $n$ is not determined by the canonical branch, and the Nijenhuis energy bound $R \leq C'P$ (Theorem A) does not apply there.

**What must be proved.** A complete lower bound for the per-blow-up tariff requires one of:

(i) A *metric-free* linear relation $R \leq CP$ (quantitative Goldberg for $s < 0$), which is open and should not be assumed.

(ii) A *localized* version of Theorem A: on any domain where $g$ is KE-close, either the monopole is canonically close there (and $R \leq C'P$), or the monopole depletion itself contributes to $P$ through a separate mechanism.

(iii) A *cell-intrinsic* lower bound: for any metric on a topological core $C_i$ (with general boundary data), $P_{C_i} \geq c_1 > 0$, regardless of the bulk geometry. This would immediately give $P \geq c_1 k$.

Approach (iii) is the most direct. It requires a relative Chern–Gauss–Bonnet or relative Bochner argument on a manifold with boundary. The obstruction is that a core with the topology of a punctured ball carrying one exceptional $\mathbb{CP}^1$ can in principle have an exact Einstein metric extending to its boundary (the Burns metric is a local Einstein metric on $\overline{\mathbb{CP}}^2 \setminus \{pt\}$). So the boundary conditions must enter — the core pays $c_1 > 0$ only when the boundary data is compatible with being part of a closed manifold with the given topology. This makes (iii) equivalent to a Dirichlet-to-Neumann statement.

---

## 5. The three form channels: period angle η, exceptional areas α, zero sets

These are genuinely distinct mechanisms and must be tracked separately.

**Channel 1: Period angle $\eta$.** On the blow-up with $b^+(X_\Gamma) \geq 2$, the almost-Kähler form $\omega$ determines $\eta = |K_X \cdot [\omega]|/\sqrt{2AV}$. Under the Lorentzian hypothesis (H$_L$), $\eta \geq 1$. But (H$_L$) depends on $[\omega]$ lying in a Kähler-type Hodge plane, which is not automatic. If $p_g(X_\Gamma) \geq 1$, there exist symplectic forms $\omega_t = \omega_0 + t\operatorname{Re}\Omega$ with $\eta(t) \to 0$ (Step 42 correction). This reduces the AKΓ prefactor $A(\eta + \alpha)^2 \to A\alpha^2$, potentially eliminating the topological contribution if $\alpha$ is also small.

For ball quotients with $p_g = 0$ (e.g., fake projective planes): $b^+ = 1$, so $H^+$ is spanned by a single class and $\eta = 1$ exactly. But $b^+(M) = 1 < 2$, and the Seiberg–Witten theory used in Theorems N/W requires $b^+ \geq 2$. These low-$b^+$ quotients require a separate argument (typically passing to a tower of covers where $b^+$ grows).

For ball quotients with $p_g \geq 1$: $b^+ \geq 3$, the $\eta$-drift channel is open, and any lower bound must either control $\eta$ or be independent of it.

**Consequence.** On hosts with $p_g \geq 1$, the AKΓ almost-Kähler route alone cannot give the per-blow-up tariff because $\eta$ can approach 0. The tariff must come from the Ricci defect through the monopole identity (Theorem N), not from the Weyl/scalar Chern–Weil identity alone.

**Channel 2: Exceptional areas $\alpha_i = |E_i \cdot [\omega]|$.** By Lemma T (Step 42), a symplectic form on $M$ has $\alpha_i > 0$ for every $i$. This contributes $\alpha = \sum \alpha_i / \sqrt{2AV}$ to the AKΓ prefactor. By Gromov monotonicity, $\alpha_i \geq c r_0^2$ when the almost-Kähler geometry has scale $r_0$ near $E_i$. But there is no uniform lower bound on $r_0$: the metric can collapse near $E_i$, making $\alpha_i$ arbitrarily small.

For the aligned branch: each $E_i$ is a $J$-holomorphic sphere of area $\alpha_i$. The associated Proposition Π (Step 44) prices $s^* > 0$ pockets but shows only that uniform $s^* > 0$ is expensive, not that sparse small pockets are.

For the perpendicular/zero-period branch: $\alpha_i = 0$, the form vanishes somewhere (Lemma T), and the almost-Kähler machinery does not apply at the zero set. The conformal metric $\hat{g} = u^2 g$ is singular there, and the AKΓ integral identity acquires boundary/residue terms from the zero set.

**Channel 3: Zero set geometry.** For a closed harmonic self-dual form $\psi$ with $\psi^{-1}(0) = Z$, the Taubes near-symplectic theory describes $Z$ as a smooth surface (generically) with a neighborhood foliated by local almost-complex structures. The gradient energy near $Z$ is:
$$\int_{B_r(Z)} |\nabla\psi|^2 \sim |\text{length}(Z)| \cdot \log(R/r_0),$$
a logarithmic divergence characteristic of codimension-2 vortices in 4 dimensions. The total zero-set "length" (2-dimensional area of $Z$) determines the leading gradient energy.

In the localized construction: $Z$ consists of $k$ exceptional 2-spheres (bolts), each of unit area, contributing $O(1)$ gradient energy per sphere and $O(k)$ total. For a diffuse construction with the same zero-period class, $Z$ must still exist (Lemma T) but could potentially be shorter (fewer or smaller components), reducing the gradient cost.

The question: can $Z$ be eliminated entirely while keeping $[\psi] \cdot [E_i] = 0$? No — Lemma T forces zeros when exceptional periods vanish. Can $Z$ consist of a single connected surface passing through all $k$ exceptional spheres? Potentially, but its topology is constrained: each $E_i$ contributes a homological constraint, and the total area of $Z$ is bounded below by the number of topological constraints it must satisfy.

---

## 6. The Nijenhuis energy budget and the Goldberg equivalence

From Theorem N at $s = -4$:
$$P \geq 8\pi^2 k - \tfrac{1}{2}R, \qquad R = \mathbb{E}_\epsilon \int \rho_\epsilon^2 |\nabla n_\epsilon|^2_{W_2}.$$

A sequence with $P/(8\pi^2 k) \to c < 1$ must have $R \geq 16\pi^2(1 - c)k$.

**Perturbative regime (§3).** On $\varepsilon_0$-close-to-KE bulk, Theorem A gives $R_{\text{bulk}} \leq C'P$. Combined with $P \geq 8\pi^2 k - R/2$:
$$P \geq 8\pi^2 k - C'P/2, \qquad P \geq \frac{8\pi^2 k}{1 + C'/2}.$$
This is the perturbative per-blow-up tariff.

**Non-perturbative regime.** The quadratic Cotton law (Step 43, conditional) gives $P \geq R^2/(\Lambda A)$ for some $\Lambda$. Combined with $P \geq 8\pi^2 k - R/2$, optimization over $R$ yields
$$P \geq \left(\sqrt{\Lambda A + 8\pi^2 k} - \sqrt{\Lambda A}\right)^2 = \frac{16\pi^4 k^2}{\Lambda A} + O(k^3/A^2).$$
This is $O(k^2/A)$ — positive but sublinear. It would not establish a per-blow-up tariff.

**The equivalence.** The per-blow-up tariff $P \geq ck$ is precisely equivalent to a *global linear Goldberg-type bound* $R \leq (2/c - 2) \cdot 8\pi^2 k + 2P$, which combined with $P \geq 8\pi^2 k - R/2$ gives $P \geq ck$. For this to hold on every metric, one needs
$$R \leq C_G \cdot P + (\text{topological terms})$$
with $C_G$ cover-uniform. This is the quantitative negative-scalar Goldberg property. The perturbative version (Theorem A, near KE) is proved. The global version is open. Any proof strategy for the tariff must either establish global Goldberg or find a completely different route (such as a cell-intrinsic lower bound).

---

## 7. Non-perturbative mechanisms and their scaling

**Mechanism A: Effective mass reduction.** In a nonlinear deformation far from KE, the effective spectral gap of the Einstein operator could decrease. The perturbative Koiso mass $\mu = 1/3$ controls the Green's function decay and hence the additivity range. If a large deformation creates a region where the effective mass is $\mu_{\text{eff}} \ll 1$, the "Compton wavelength" $1/\sqrt{\mu_{\text{eff}}}$ increases, the cell–cell interactions become long-range, and collective modes arise.

The diagnostic observable is the smallest eigenvalue of the linearized Einstein operator on the deformed metric. In the AAD proper 3-symmetric model (Step 43, §7), $|\operatorname{Ric}^\circ|^2 / |\nabla\omega|^4 = 9/64$, a finite ratio, suggesting the Goldberg gap stays open in that family. But this is a local, non-compact model; behavior on closed manifolds could differ.

**Mechanism B: Topological flux obstruction.** On the closed manifold $M$, the Chern–Gauss–Bonnet theorem gives
$$\frac{1}{8\pi^2}\int_M \left(|W^+|^2 + |W^-|^2 + \frac{s^2}{24} - \frac{|\operatorname{Ric}^\circ|^2}{2}\right) = \chi(M) = \frac{A}{3} + k.$$
Since $|W^-|^2 \geq 0$ and $s^2/24 \geq 0$, this gives $|W^+|^2 + s^2/24 + P/2 \geq 8\pi^2(A/3 + k)$. The $C_+$ identity further gives $C_+ = A - k + P/(8\pi^2)$, so $P/(8\pi^2) = C_+ - A + k \geq 0$ is automatic (since $C_+ \geq 2A/3$ from LeBrun).

The per-blow-up tariff is not a consequence of Chern–Gauss–Bonnet alone; it requires the signed curvature identities of the monopole field. The topological charge $k$ enters only through these identities.

**Mechanism C: Zero-set flux and its obstruction to diffusion.** For the perpendicular branch (zero exceptional periods), the harmonic form $\psi$ vanishes on a surface $Z$. The Weitzenböck formula for $\psi$ gives $\frac{1}{2}\Delta |\psi|^2 = |\nabla\psi|^2 - \langle R^+\psi, \psi\rangle$ where $R^+ = W^+ + s/12$. Near $Z$, the form $\psi$ grows linearly in the normal direction: $|\psi| \sim d(x, Z)$. The gradient energy density $|\nabla\psi|^2 \sim 1$ near $Z$, concentrated in a tube of radius $\sim 1$ around $Z$.

The total gradient energy is $\int |\nabla\psi|^2 \geq c \cdot \operatorname{Area}(Z)$. The Euler characteristic of $Z$ is topologically constrained: for each $E_i$ with $[\psi] \cdot [E_i] = 0$, the zero surface must "absorb" the topological linking. The minimum-area representative of $Z$ compatible with $k$ such constraints is a precise geometric-measure problem.

If $\operatorname{Area}(Z) \geq c'k$ for topological reasons, then $\int |\nabla\psi|^2 \geq c c' k$, contributing a term that feeds back into the Ricci defect through the Weitzenböck identity $\int |\nabla\psi|^2 = \int \langle R^+\psi, \psi\rangle$. This would be a topological lower bound on the harmonic-form gradient energy, independent of the metric.

The computation: what is $\min \operatorname{Area}(Z)$ subject to $Z$ being the zero set of a harmonic self-dual form with $[\psi] \cdot [E_i] = 0$ for $i = 1, \ldots, k$? This is a well-posed question in calibrated geometry / Taubes near-symplectic theory and would directly discriminate the localized-to-diffuse transition.

---

## 8. Cheapest discriminating calculations

In decreasing order of cost-effectiveness:

**(D1) Cell cost as a function of boundary flux (computational, on existing infrastructure).** Using the Step-19 LM optimizer and the Step-29 interface identity, compute $P_{\text{cell}}(\lambda_{\text{ext}})$ for the symmetric perpendicular cell with a modified exterior boundary condition. Specifically, replace the zero-charge infinite collar with a finite collar ($X = 128$ or $256$) and an imposed nonzero boundary value $w(X) = w_{\text{ext}}$ in the antisymmetric channel. Optimize the interior profile for each $w_{\text{ext}}$. The function $P_{\text{cell}}(w_{\text{ext}})$ has a minimum at $w_{\text{ext}} = 0$ (the current cell) or at $w_{\text{ext}} \neq 0$ (the cell prefers a particular incoming flux). Its curvature $\partial^2 P / \partial w_{\text{ext}}^2|_0$ directly gives the cell's "stiffness" in the compliance calculation.

This computation uses the existing Cartan curvature package, the Hessian from Step 19, and requires only varying one boundary parameter. Expected cost: one session of optimization runs.

The Step-19 data already provides this information indirectly: the far-field charge $\lambda \approx 0.183$ and the exterior response $E_{\text{ext}} = \delta^2/I(\rho)$ with $I(10) = 0.00423$. The cell's boundary gradient is $\partial P / \partial w_0 = 2\delta \cdot (\partial\delta/\partial w_0)/I - 2\delta^2 (\partial I / \partial w_0) / I^2$ evaluated at the optimizer. The second derivative of the total cell cost (core + exterior) with respect to $w_0$ is the relevant compliance number.

**(D2) Green's function of the Einstein operator on $\mathbb{CH}^2$ (analytical/numerical, one-time).** Compute $G_E(r)$, the radial Green's function of the TT Einstein operator $L_E = \nabla^*\nabla - 2\mathring{R}$ on $\mathbb{CH}^2$, restricted to the antisymmetric ($J$-anti-invariant) sector where the Koiso mass is $\mu = 1/3$. By homogeneity this reduces to an ODE in the radial variable $r$ with a regular singular point at $r = 0$ and exponential decay at $r = \infty$. The decay exponent is $\sqrt{\mu} = 1/\sqrt{3}$, and the Green's function determines the exact interaction kernel $G_E(x_i, x_j)$ between cells.

The $L^1$ norm $\|G_E\|_{L^1} = \int_0^\infty G_E(r) \sinh^3(r)\,dr$ (in the $\mathbb{CH}^2$ volume form) determines whether the $L^\infty \to L^\infty$ resolvent is bounded (Lemma M of Step 44). For $\mu > \rho_0^2$ where $\rho_0^2 = 4$ is the $L^2$ bottom of the full Laplacian on $\mathbb{CH}^2$, the Green's function is in $L^1$ by standard spherical-function estimates (the mass exceeds the volume growth threshold). Since the $J$-anti-invariant sector has $\mu = 1/3 < 4$, the relevant operator is $\nabla^*\nabla + (\lambda + a) = \nabla^*\nabla + 2$ (effective mass $2$), which exceeds $\rho_0^2 = 4$ only if the correct comparison is with the Bochner Laplacian's bottom rather than the scalar Laplacian's. This comparison is exactly Lemma M and is the open input for the Hölder-form Theorem A.

**(D3) Minimum zero-set area for $k$ null periods (topological/geometric-measure, theory).** Formulate and solve: given a closed Riemannian 4-manifold $(M, g)$ and a harmonic self-dual form $\psi$ with $k$ prescribed null periods $[\psi] \cdot [E_i] = 0$, what is the minimum $\mathcal{H}^2(Z)$ of the zero set $Z = \psi^{-1}(0)$?

Taubes' near-symplectic theory gives $Z$ a smooth surface (for generic $g$) with $[Z]$ Poincaré dual to $e(\mathcal{V}^+)$, the Euler class of a complementary rank-2 bundle. Each null period forces a linking condition between $Z$ and the corresponding exceptional sphere. The minimum area of a surface satisfying $k$ such linking conditions, in a metric of bounded geometry, should be $\geq c(g) \cdot k$ by a calibration or linking-number argument.

If this bound holds and is metric-uniform (with $c(g)$ depending only on a curvature bound and non-collapsing), it would give $\int |\nabla\psi|^2 \geq c' k$, a *metric-free* linear lower bound on the harmonic-form gradient energy for the zero-period branch. Combined with the Weitzenböck identity and the Ricci defect, this would establish the per-blow-up tariff for the perpendicular channel without needing the Goldberg property.

This is the most theoretically promising route because it bypasses the non-perturbative Goldberg question entirely, using instead the topological rigidity of the zero set.

**(D4) Cohomogeneity-one interpolation family (computational, medium cost).** On a symmetric model (e.g., $\mathbb{CH}^2/\Gamma$ blown up at a fixed point, with the $\mathrm{SU}(2)$ symmetry of the cell extended to a larger domain), construct a 1-parameter family of metrics $g_t$ with $t \in [0, 1]$ where $g_0$ is the localized perpendicular cell and $g_1$ has the torsion distributed over a large ball of radius $R_1$. For each $t$, solve the coupled metric + harmonic-form system numerically (in the equivariant ODE reduction) and compute $P(g_t)$, $R(g_t)$, $\int |\nabla\psi_t|^2$, and the zero-set geometry.

This would directly reveal whether the cost decreases, increases, or stays constant as the torsion spreads. The comparison of $P$ vs $R$ along the family would empirically determine the $P$–$R$ scaling in the transition regime.

---

## 9. Construction program for testing $o(k)$

A construction achieving $P = o(k)$ on a pure blow-up tower must solve several simultaneous problems:

**(C1) Scalar normalization.** The Yamabe condition $s = -4$ must hold globally. On the bulk, this is automatic if the metric is close to KE. On the transition region, the scalar curvature must be controlled by a conformal adjustment, whose cost enters through (G2).

**(C2) Harmonic form.** A closed self-dual harmonic form $\psi$ must exist on $(M, g)$. For generic $g$, $\mathcal{H}^+$ has dimension $b^+$. The form's cohomology class is constrained by the Taubes period lemma. For the perpendicular branch: $[\psi] \cdot [E_i] = 0$, forcing zeros. For the aligned branch: $[\psi] \cdot [E_i] = a_i > 0$, requiring $s^*$-pockets near each $E_i$.

**(C3) Distributed torsion.** If the torsion (almost-Kähler rotation) is distributed over volume $V' \sim A$, the torsion density is $\delta \sim k/A$ per unit volume. The Ricci cost of this distributed torsion, in the perturbative regime, is $P_{\text{torsion}} \sim \kappa (k/A)^2 \cdot A = \kappa k^2/A$ — exactly the quadratic scale. This is consistent with the Cotton law and would give $P \sim k^2/A = o(k)$ for $k \ll A$.

The question is whether such a construction exists as a genuine smooth metric on $M$, not just as a formal perturbative estimate. The construction must:

(a) Solve the coupled elliptic system (Yamabe + Hodge-harmonic + smooth matching at cells) with the distributed torsion profile.

(b) Control the cell cost: each cell must accommodate the incoming torsional flux without incurring a large local defect. The cell's response to boundary torsion is governed by computation (D1).

(c) Maintain the topological constraints: the harmonic form's zero set or exceptional areas must be consistent with Lemma T.

**(C4) The interpolation ansatz.** Take the existing localized construction and introduce a "spreading parameter" $\sigma$: at $\sigma = 0$, the torsion is localized in unit cells; at $\sigma = 1$, it is spread over the host. Concretely, in the collar region of each cell, instead of matching to the exact Kähler form at radius $R$, match to an almost-Kähler form with torsion $\delta_{\text{ext}}(\sigma)$ that decays as $\delta_{\text{ext}} \sim \sigma / r^2$ (the Green's function profile). The interior of the cell adjusts to minimize $P$ for the given exterior boundary condition.

For the SU(2)-symmetric cell: the "spreading" corresponds to a nonzero antisymmetric mode $w(X) \neq 0$ at the collar end, with $w \sim \sigma \cdot (\text{Green profile})$. Computation (D1) gives $P_{\text{cell}}(\sigma)$, and the bulk cost is $P_{\text{bulk}}(\sigma) \sim \kappa_0 \sigma^2 / A$ per cell (from the Green's function interaction). The total cost at the optimal $\sigma$ would reveal the achievable improvement.

If the interpolation shows $P_{\text{total}}(\sigma^*) < P_{\text{total}}(0)$ with a relative improvement $> O(k/A)$, the diffuse mode genuinely beats the localized one beyond the perturbative estimate. If not, the perturbative compliance calculation is tight and the per-blow-up tariff holds.

---

## 10. Summary of the mathematical status and the decisive fork

The localized-to-diffuse transition on pure blow-up towers outside the inherited window is governed by three interlocking quantities:

| Quantity | Perturbative (near KE) | Non-perturbative (global) |
|---|---|---|
| $P$ vs $R$ | $R \leq C'P$ (Theorem A, proved) | $R \leq ?$ (Goldberg, open) |
| Cell coupling | Exponentially decayed (Koiso gap) | Unknown if gap persists |
| Harmonic zero-set area | $\geq ck$ on model cells | $\geq c'k$ for topological reasons? |

The perturbative analysis establishes the per-blow-up tariff for metrics close to KE: the improvement from diffuse bulk deformation is $O(k^2/A)$, preserving the $\Theta(k)$ scaling. The non-perturbative transition hinges on one of two independent mechanisms:

**Fork A (Goldberg).** If $R \leq C_G P$ globally (quantitative negative-scalar Goldberg), then $P \geq 8\pi^2 k/(1 + C_G/2)$ — the tariff holds. The perturbative version is Theorem A. Extending it requires either Lemma M (for the Hölder form, a computable spherical-function question on $\mathbb{CH}^2$) or a genuinely new argument for metrics far from KE.

**Fork B (Zero-set topology).** If $\operatorname{Area}(Z) \geq c k$ for every harmonic self-dual form with $k$ null exceptional periods (a topological lower bound on the vortex sheet area), then $\int |\nabla\psi|^2 \geq c' k$ — the gradient energy is linear, and combined with the Weitzenböck identity and Theorem N, this gives the tariff for the perpendicular branch independently of Goldberg. This route uses the Taubes near-symplectic structure and the linking topology of $Z$ with the exceptional spheres, and is insensitive to the $\eta$-drift channel.

The construction side: a family achieving $P = o(k)$ must circumvent both forks — either by exploiting the aligned branch ($\alpha > 0$, small $\eta$, no zero set) where neither fork applies, or by finding metrics sufficiently far from KE that the perturbative Goldberg gap closes while the zero-set area grows sublinearly in $k$.

The cheapest discriminating input is calculation (D1): the cell cost's second derivative with respect to boundary flux, combined with the known Koiso gap, immediately determines the perturbative compliance and verifies or refines the $O(k^2/A)$ estimate. If the cell cost is convex in boundary flux with curvature $\sim 1/I(\rho)$ (as predicted by the Step-19 exterior response), the perturbative tariff is quantitatively established. The non-perturbative extension then reduces to Fork A or Fork B, each of which has a concrete mathematical target: the spherical-function integrability (Lemma M) for Fork A, or the linking-area bound for Fork B.