# TTCS Independent Branch Record

```json
{
  "step_id": 42,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step41_symplectic_closure_bolt_layer_and_new_inputs.md",
    "Sessions/S1003A02/workspace/notes/step47_consolidation_two_scale_program.md",
    "Skills/geometric-analysis/research/paper/sections/finite_density_endpoint.tex",
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex",
    "Knowledge/materials/openai-math-20261007/continuation/20261007_openai_math_connections/connections.md"
  ]
}
```

## Task

The active goal is a unified Einstein-gap theory. Compare two central unresolved routes using the supplied exact mathematics, not generic suggestions. Route A is density-free O10 after resetting the actual budget to p: any escape has chi/p→∞, p/V→2/(9pi^2), W-/V→∞; the finite-density proof constructs an actual L^5 section of asymptotically nonzero modulus whose Chern square density stays positive, but W- enters its derivative/second-jet control. Investigate whether the section's zero/phase geometry, a localized Chern transgression, Bianchi identities, or the positive-current mechanism can yield a genuinely new density-independent estimate. State the strongest exact identity or conditional theorem that looks derivable, and identify the precise mathematical quantity still uncontrolled. Route B is O11 after the certified sub-four cell and symplectic closure: generic near-minimizer selection remains valid but the old unit-tariff instability target is false; compare a corrected minimizer-entry/global-comparison route with a diffuse k^2/A transport route. Determine which route presently has the best chance of a major theorem, and formulate a concrete proof object that accommodates the certified construction rather than restoring coefficient four. Do not invent literature or assume compactness/noncollapse.

## Output

# Route A vs Route B: Exact Mathematical Comparison

## Route A — The density-free endpoint

### The chirality separation and the precise obstruction

The finite-density proof's section construction has a sharp chirality structure whose analysis reveals exactly where the density-free extension breaks.

**Positive-chirality data (controlled without $W^-$).** The monopole $\Phi_j \in S^+_j$ satisfies $D^+\Phi_j = 0$, $\nabla^*\nabla\Phi_j = (1-\rho_j/2)\Phi_j$. The Weitzenböck identity on $S^+$ involves $W^+$, the scalar, and the determinant curvature—all converging or bounded on the escape sequence. Consequently:
$$\|\nabla^2\Phi_j\|_2^2 + \|\nabla\Phi_j\|_4^4 \le C(\|\nabla^*\nabla\Phi_j\|_2^2 + \|\mathrm{Ric}\|_2^2 + \|F_{S^+}\|_2^2) \le C$$
independently of $W^-_j/V_j$. The cubic torsion $t_j = t(\Phi_j) \in S^-_j \otimes L_j$ is constructed algebraically from $\Phi_j$ and $\nabla\Phi_j$; hence $\|t_j\|_4 \le C$ and $\|\nabla t_j\|_2 \le C$ without $W^-$.

**Negative-chirality bottleneck.** The resolvent $v_j \in S^-_j \otimes L_j$ satisfies $(4+\nabla^*\nabla)v_j = 6z_j$, giving $|v_j|\le 6$ and $\|\nabla^*\nabla v_j\|_\infty \le 48$. The Hessian interchange for sections of $E_- = S^-\otimes L$ reads
$$\|\nabla^2 v_j\|_2^2 + \|\nabla v_j\|_4^4 \le C\bigl(\|\nabla^*\nabla v_j\|_2^2 + \|\mathrm{Ric}\|_2^2 + \|F_{E_-}\|_2^2\bigr).$$
The curvature of $E_-$ contains the $W^-$ block: $F_{E_-}$ includes the action of $W^-$ on $S^-$ through the representation $\Lambda^-\to\mathrm{End}(S^-)$. Therefore
$$\|\nabla v_j\|_4^2 \le C(1 + b_j), \qquad b_j = \fint|W^-_j|^2.$$
The section $\sigma_j = \Phi_j \wedge t(v_j) \in L^5_j$ inherits this: $\|\nabla^{L^5}\sigma_j\|_2 \le C(1+b_j)^{1/2}$, controlled only with the density bound $b_j \le CB$.

### Why the $L^5$ line bundle curvature is actually controlled

The curvature of $L^5_j$ is $5F_{\mathcal{A}_j}$. The self-dual part is $5F^+_{\mathcal{A}_j} = 10i\sigma(\Phi_j)$ with $|F^+|^2 = \rho_j^2/2 \to 8/9$. The anti-self-dual part has the bounded model decomposition from the strong-current lemma: $\|F^-_{\mathcal{A}} - K\|_2 \to 0$ with $|K|\le C$. Hence $\|F_{L^5}\|_2^2/V$ is bounded independently of $W^-$.

This means the Hessian interchange *for sections of $L^5$ itself* does not involve $W^-$:
$$\fint(|\nabla^2_{L^5} u|^2 + |\nabla_{L^5} u|^4) \le C_{L^5}(\|\nabla^*_{L^5}\nabla_{L^5} u\|_2^2 + \|\mathrm{Ric}\|_2^2 + \|F_{L^5}\|_2^2) \le C_{L^5}(\|\nabla^*\nabla u\|_2^2 + C).$$

The obstacle is that $\sigma_j$ is constructed through the intermediate $v_j \in S^-\otimes L$, and we cannot derive an elliptic equation for $\sigma_j$ on $L^5$ whose coefficients avoid $W^-$. The algebraic formula $\sigma = \Phi \wedge t(v)$ couples the $S^+$ and $S^-\otimes L$ factors multiplicatively, so $\nabla^2\sigma$ involves $\nabla^2 v$, and the latter requires the $S^-$ Bochner identity.

### Three candidate bypass routes and why each stops

**1. Direct $S^+$-only line-bundle section.** The natural object $\tau_X = \Phi \wedge \nabla_X\Phi \in L$ (for each tangent direction $X$) has controlled derivative: $\|\nabla^L \tau_X\|_2 \le C(\|\nabla\Phi\|_4^2 + \|\Phi\|_\infty\|\nabla^2\Phi\|_2) \le C$ from the $S^+$ bounds. The total norm $\sum_i|\tau_{e_i}|^2 = \rho\sum_i|(\nabla_i\Phi)_2|^2 \to \rho_*q_*/2 > 0$ in measure. But no *single global* direction gives a section with nonvanishing modulus: the surviving derivative concentrates in the anti-holomorphic transverse direction $\bar{Z}_2$, which depends on $J_\Phi$ and the metric and cannot be defined as a global smooth vector field. The sum $\sum|\tau_{e_i}|^2$ is a scalar function on $M$, not a section of a line bundle; it does not carry Chern data.

**2. Resolvent directly on $L^5$.** Cap $t_j$ to get $z_j = T(t_j)$ bounded, form $\sigma'_j = \Phi_j \wedge t(z_j)$, and apply the $L^5$ resolvent. Since $t(z_j)$ involves $\nabla z_j$, we get $|\sigma'_j| \le C|\nabla t_j|$, which is in $L^2$ but not $L^\infty$. A second cap of $\sigma'_j$ would lose the modulus-convergence property unless $\sigma'_j$ is already uniformly bounded. Its $\nabla^{L^5}$ energy involves $\|\nabla^2 z_j\|_2$ and $\|\nabla z_j\|_4$—the same quantities that require $W^-$ through the $S^-$ Bochner. The chain cannot be short-circuited.

**3. Positive-current/Bianchi mechanism.** The curvature $F_{\mathcal{A}}$ is closed ($dF = 0$), and $dF^+ = 2id(\sigma(\Phi))$ is controlled from $S^+$ data, hence $dF^-$ is also controlled. But controlled $dF^-$ does not bound $F^-$ or $W^-$ in $L^p$ for $p > 2$; a high-frequency divergence-free perturbation of $W^-$ has small $dF^-$ norm relative to its $L^2$ amplitude. The almost-Kähler form $\omega_\Phi = -i\sigma(\Phi)/|\Phi|$ has $\|d\omega_\Phi\|_2 \le C$ (from $\|\nabla\Phi\|_4$), so it is approximately closed. But its Nijenhuis error $\|d\omega_\Phi\|_2$ is order $\sqrt{R_\rho/V}$, which tends to a positive constant (not zero) on the escape sequence by the $R_\rho \ge 16\pi^2(1-c)k$ bound. The form is not approximately symplectic, and the taming/compatibility machinery of family 342 requires a fixed background almost-complex structure, not a varying one.

### The strongest conditional theorem on Route A

**Conditional Theorem.** Suppose the escape sequence satisfies
$$\|\nabla t(\Phi_j)\|_{L^4(M_j,g_j)} \le C$$
independently of $W^-_j/V_j$. Then $c_1(L_j^5)^2/V_j \to 0$, contradicting $c_1(L_j^5)^2/V_j \to 25/(6\pi^2)$, and the finite-density endpoint becomes density-free.

*Mechanism:* $L^4$ gradient control of $t$ and Sobolev embedding give $t_j \in L^q$ for all $q < \infty$. The cap $z_j = T(t_j)$ then has $\|\nabla z_j\|_4 \le C$, the section $t(z_j)$ is in $L^2$ with derivatives in $L^{4/3}$, and after one more algebraic composition with $\Phi$, the section $\sigma_j \in L^5$ has $\|\nabla\sigma_j\|_2 \le C\|\nabla\Phi\|_4\|\nabla z\|_4 + C\|\Phi\|_\infty(\|\nabla z\|_4^2 + \|\nabla^2 z\|_2) \le C$. The $L^5$ Hessian interchange (which avoids $W^-$) then controls the higher regularity, and the logarithmic resolvent applies.

**The precise uncontrolled quantity:** $\|\nabla t(\Phi)\|_{L^4}$, or equivalently $\|\nabla^2\Phi\|_{L^4}$ (since $t$ is algebraic in $\Phi,\nabla\Phi$). The $S^+$ Bochner gives $\|\nabla^2\Phi\|_{L^2} \le C$ (without $W^-$); the step from $L^2$ to $L^4$ requires a Gagliardo–Nirenberg interpolation involving $\|\nabla^3\Phi\|_{L^2}$, which in turn introduces $\nabla\mathrm{Ric}$ and $\nabla W^+$ through the iterated Bochner identity. On the $s = -4$ representative, $\mathrm{div}(\mathrm{Ric}^\circ) = 0$ (Bianchi with constant scalar), so $\nabla\mathrm{Ric}^\circ$ satisfies an elliptic system. However, its $L^2$ norm is not controlled by $P$ alone: $\|\nabla\mathrm{Ric}^\circ\|_2^2 = \langle\nabla^*\nabla\mathrm{Ric}^\circ, \mathrm{Ric}^\circ\rangle$, and the Lichnerowicz identity produces curvature-quadratic terms that include $W^-$. A different mechanism—not the Bochner identity at any order—would be needed.

### Verdict on Route A

A density-free O10 theorem requires an analytical tool that detects line-bundle Chern-class topology from $L^2$-controlled field data without the $L^4$ Sobolev interpolation on $S^-\otimes L$. No such tool is currently available. The chirality wall is structural: the surviving nonzero modulus lives in $L^5 = \det(S^+)\otimes\det(S^-\otimes L)^2\otimes L$, and any section construction must ultimately pass through the $S^-$ factor.

---

## Route B — O11 after the certified sub-four cell

### The actual state of the problem

The certified isolated cell gives $P/(8\pi^2) \in [0.99566273, 0.99566274]$ for a single exceptional class. The rotation argument constructs genuinely symplectic subthreshold metrics. The formal common mode saturates Theorem K at $h \to 0$, with $P/k$ scaling like $k(1+h)/(2-h)^2$. Lemma T excludes the exact common mode. No all-metric positive lower bound for $P$ is known in the open range $0 < k < A/3$.

On the manifold $M = X\#k\overline{\mathbb{CP}}^2$ with $X$ a CH surface ($c_1^2 = 3c_2 = A$): $T_+ = A - k > 0$ and $T_- = A/3 + 5k > 0$ for $0 < k < A/3$. Hitchin–Thorpe is satisfied. LeBrun's $C_+ \ge 2A/3$ gives $P \ge 8\pi^2(k - A/3)$, which is negative for $k < A/3$. A hypothetical Einstein metric would have $W^+ = 4\pi^2(A-k)$, $W^- = 4\pi^2(A/3+5k)$, both positive: it would not be excluded by any known Chern–Weil argument.

**Any positive lower bound $\inf_g P(g) > 0$ for fixed $M$ with $0 < k < A/3$ would be a genuinely new obstruction to Einstein metrics.**

### Route B1 — Minimizer-entry/global-comparison

The Coulomb-style architecture requires: (i) approximate the infimum by controlled objects, (ii) identify the geometric decomposition (bulk + cores + collars), (iii) apply a global comparison identity, (iv) sum local lower bounds.

Step (i) is done: the variational selection provides near-minimizers with $s = -4$ and controlled first/second variations. The fundamental obstruction to (ii)–(iv) is twofold.

First, the conditional whole-AE-core proposition gives $P \ge 8\pi^2 k$ under ideal decomposition—but the certified cell proves this is *too strong* by a factor of $0.4\%$. The contradiction shows that actual near-minimizers do NOT decompose into a smooth $X$ bulk plus isolated AE cores with exact curvature accounting. The sub-four saving is a *diffuse* interaction between the core and the background.

Second, on complete AE manifolds with $b_2 \ge 1$ and $\mathrm{Ric} = \Lambda g$, $\Lambda < 0$: the formula $P = 8\pi^2 b_2 + 4W^+ + S/12 + 32\pi^2(b_1 + e - 1)$ and $S = 16\Lambda^2 V = 16V$ (with our normalization), combined with $V = \infty$ for noncompact negative-Einstein manifolds, gives $P = \infty$. So negative-Einstein AE bubbles cannot form; any bubble is Ricci-flat or has finite $P$. Ricci-flat AE bubbles with trivial end group and $b_2 = 1$ have $P = 8\pi^2 + 4W^+ \ge 8\pi^2$. Ricci-flat ALE with nontrivial group (Eguchi–Hanson) has $P = 0$ but can't serve as a whole AE core for the standard blow-up topology. This constrains the bubble zoo but doesn't close the accounting.

**Route B1 is blocked by the collar/entry theorem and by the fundamental mismatch between coefficient four (from ideal decomposition) and the actual sub-four infimum.**

### Route B2 — Localized coercivity and the positive gap

The correct target is not coefficient four but a *positive* gap accommodating the certified cell:
$$\inf_{g\in\mathcal{M}(M)} P(g) \ge c(M) > 0, \qquad M = X\#k\overline{\mathbb{CP}}^2, \quad 0 < k < A/3.$$

The mechanism is the interaction between three exact ingredients.

**Ingredient 1: Localized CH coercivity.** On a domain $\Omega \Subset \Omega_1$ in a metric $g$ with $s_g = -4$ and $\|g - g_{CH}\|_{C^{2,\alpha}(\Omega_1)} \le \delta$, the contracted Bianchi identity reads $\mathrm{div}(\mathrm{Ric}^\circ) = 0$ (constant scalar). The Lichnerowicz Laplacian $\Delta_L$ at a negative Einstein metric has a spectral gap $\lambda_L > 0$ on TT (trace-free transverse) tensors. In the DeTurck gauge $h = g - g_{CH}$ satisfying $\beta_{g_{CH}}(h) = 0$, standard interior elliptic estimates give
$$\|h\|_{H^2(\Omega)}^2 \le C\|\mathrm{Ric}^\circ_g\|_{L^2(\Omega_1)}^2 + C\|h\|_{H^{3/2}(\partial\Omega_1)}^2.$$
Since the curvature deviation is controlled by $\|h\|_{H^2}$:
$$\int_\Omega |\mathrm{Rm}_g - \mathrm{Rm}_{CH}|^2 \le C\int_{\Omega_1}|\mathrm{Ric}^\circ_g|^2 + C\,\mathcal{B}(\partial\Omega_1)$$
where $\mathcal{B}$ is gauge-invariant boundary data. This is a provable PDE theorem, requiring only the spectral gap of $\Delta_L$ and standard elliptic theory.

**Ingredient 2: Canonical-branch $A_C$ on the bulk.** On the near-CH bulk, the canonical monopole branch satisfies $R_{\mathrm{can}} \le CP$ (from the perturbative theorem $A_C$). Meanwhile, the global identity forces $R_\rho \ge 16\pi^2(1-c)k$ whenever $P \le 8\pi^2 ck$. On near-minimizers with $P \to 0$: $R_\rho \to 16\pi^2 k$. Since $R_{\mathrm{can}} \le CP \to 0$ on the bulk, ALL Nijenhuis energy resides in cores/collars.

**Ingredient 3: Core Nijenhuis energy requires curvature.** In each core of volume $O(1)$ and metric bounded away from CH, the monopole field wraps around the exceptional sphere. The Nijenhuis energy per core, $R_{\rho,i} \ge c_0 > 0$, interacts with $W^+$ through the alignment identity $\|W^+ - W_0\|^2$. On the $s = -4$ representative, the Chern–Gauss–Bonnet identity relates $W^+$ contributions to $P$. Specifically, the signed identity gives $\mathscr{A} \ge 4\mathbb{E}\|W^+ - W_0\|^2$, and $P = 8\pi^2 k + \mathscr{A} - 4\mathbb{E}K$. If each core contributes $W^+$-alignment energy $\ge c_1 > 0$ (from the nontrivial topology), then $\mathscr{A} \ge c_1 k$, and the identity gives $P \ge c_1 k - 4(\mathbb{E}K - 2\pi^2 k)$. An independent control of $\mathbb{E}K - 2\pi^2 k$ from the amplitude equation would close this.

### The concrete proof object

**Target Theorem.** *Let $X$ be a closed complex-hyperbolic surface, $A = c_1^2(X)$. There exists $c = c(X) > 0$ such that for every integer $k$ with $1 \le k \le A/3 - 1$ and every Riemannian metric $g$ on $M = X\#k\overline{\mathbb{CP}}^2$,*
$$P(g) = \int_M|\mathrm{Ric}^\circ_g|^2\,dV_g \ge c.$$

**Proof architecture (three theorems to prove):**

**Theorem L (localized coercivity).** For every $\delta_0 > 0$ and compact domain-pair $\Omega \Subset \Omega_1$ in a closed four-manifold with $s = -4$, if $\|g - g_0\|_{C^{2,\alpha}(\Omega_1)} \le \delta_0$ for an Einstein metric $g_0$ with $\mathrm{Ric}_{g_0} = -g_0$, then
$$\int_\Omega|\mathrm{Rm}_g - \mathrm{Rm}_{g_0}|^2 \le C_L\int_{\Omega_1}|\mathrm{Ric}^\circ_g|^2 + C_L\,\mathcal{B}(\Omega_1\setminus\Omega).$$
The constant $C_L$ depends on $\delta_0$ and the spectral gap of $\Delta_L$ on $g_0$, not on the global topology.

**Theorem R (restricted Nijenhuis localization).** For $g$ on $M$ with $s = -4$ and actual sign-family solutions, let $\Omega$ be a domain where $g$ is $\delta$-close to $g_{CH}$ in $C^{2,\alpha}$ and the canonical monopole branch is identified. Then
$$\int_\Omega \rho^2|\nabla n|_{W_2}^2 \le C_R\int_{\Omega_1}|\mathrm{Ric}^\circ_g|^2 + C_R\,\mathcal{B}'(\Omega_1\setminus\Omega),$$
with $C_R$ depending on the CH background.

**Theorem C (core Weyl contribution).** For each connected core component $U_i$ containing an exceptional class $E_i$ and supporting the non-canonical field branch:
$$\int_{U_i}|W^+_g - W_{0,\epsilon}|^2\,dV_g \ge c_C > 0,$$
where $c_C$ depends on the minimal self-intersection capacity and the topological constraint $E_i^2 = -1$.

*Combination:* Theorems L and R localize curvature departure and Nijenhuis energy to cores. Theorem C forces each core to contribute positive $W^+$-alignment energy. Summing over $k$ cores: $\mathscr{A} \ge 4c_Ck$. The signed identity gives $P \ge 4c_Ck - 4(\mathbb{E}K - 2\pi^2 k)$. The amplitude identity $\Sigma = 16K + 4\int(\rho-2)^2 + 8J$ and the near-maximality of $\rho$ on the bulk force $\mathbb{E}K$ close to $2\pi^2 k$ from below, with the excess controlled by the same core contributions. A bootstrap closes.

The constant $c = c(X)$ depends on $X$ through the spectral gap of $\Delta_L$ on $g_{CH}$, the injectivity radius, and the minimal collar geometry. For tower families ($X = X_j$ with $A_j \to \infty$, uniform geometry), $c$ is uniform.

### Compatibility with the certified construction

The certified cell has $P/(8\pi^2) = 0.9957$ per blow-up and uses a metric that is modified only in a neighborhood of the exceptional sphere. On the bulk, the metric is exactly CH, so $\mathrm{Ric}^\circ = 0$ there and Theorem L contributes nothing. The core is where all the curvature energy lives: $P_{\mathrm{core}} = 0.9957 \times 8\pi^2$. Theorem C requires $c_C \le P_{\mathrm{core}}/4 \approx 0.9957\times 2\pi^2$. The gap between $c_C$ and $2\pi^2$ is the sub-four saving from the diagonal optimization.

The target theorem does NOT assert coefficient four. It asserts $P > 0$, which is compatible with any positive coefficient. The signed identity and core analysis determine the mechanism; the certified cell determines the optimal coefficient from above.

For the quantitative $k^2/A$ conjecture: on tower families with $k/A \to 0$, the formal common mode spreads Weyl departure of size $k/A$ over volume $A$, paying $L^2$ cost $(k/A)^2 \times A = k^2/A$. Theorem K's near-saturation on the formal mode (ratio $4/(4-5h) \to 1$) suggests this is tight. A matching lower bound would require Theorem L to be globalized with collar terms summing to $O(k)$ (not $O(k^2/A)$), and a separate quadratic transport estimate for the diffuse channel. This is a second-stage refinement, not the first theorem.

---

## Comparative assessment

| | Route A (density-free O10) | Route B2 (positive gap for O11) |
|---|---|---|
| **Target** | Remove Euler-density dependence from the endpoint constant | Prove $\inf_g P > 0$ for $0 < k < A/3$ |
| **Obstruction** | $L^4$ gradient of $S^-\otimes L$ sections requires $W^-$ | Localized coercivity + core Weyl contribution |
| **Nature** | Structural chirality wall | Three-theorem PDE program |
| **Available tools** | $S^+$ Bochner (reaches $L^2$ gradient only) | Lichnerowicz gap, $A_C$, signed identities, Theorem K |
| **New idea needed** | Fundamentally new: detect $c_1(L^5)^2$ from $L^2$ data | Extension of existing methods: localize $A_C$, prove per-core $W^+$ contribution |
| **Relation to known results** | Would improve polynomial $c(B)$ to absolute $c$ | Would establish Einstein non-existence in a new topological range |
| **Testability** | The conditional theorem is precise but uncontrolled | Each sub-theorem is separately testable on the certified cell |

**Route B2 presently has a substantially better chance of a major theorem.** Its three sub-theorems (L, R, C) are natural extensions of established techniques: Theorem L is standard elliptic theory for the linearized Einstein operator; Theorem R extends the perturbative $A_C$ to localized domains; Theorem C uses the topological constraint $E_i^2 = -1$ and the monopole wrapping energy. Route A requires a qualitative analytical innovation (detecting Chern topology from $L^2$ section data) for which no current method exists.

The first research action for Route B2 should be Theorem L: prove the localized coercivity on a single ball in $\mathbb{CH}^2$, with an explicit spectral gap constant and boundary term. This is a self-contained computation involving the representation theory of $\Delta_L$ on the CH background and can be verified against the certified cell data (where the bulk contribution to $P$ is exactly zero). If the boundary terms are of the right order ($O(1)$ per collar), the combination with the signed identities becomes immediately accessible.