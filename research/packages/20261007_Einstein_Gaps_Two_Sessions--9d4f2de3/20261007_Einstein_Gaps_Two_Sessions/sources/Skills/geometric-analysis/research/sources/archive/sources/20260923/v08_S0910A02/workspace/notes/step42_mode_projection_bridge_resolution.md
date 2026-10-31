# Step 42: Mode-projection construction and Bridge resolution for Route A

Session S0910A02. Agent2/Constructor. Phase Execute.

## 0. Scope and target fidelity

This step constructs the mode-projection framework for the four-dimensional positive noncollapsed branch (Route A). It does NOT prove any branch of Yau-26. The active target remains the full proposition for all dimensions, signs, topologies, and closure standard including Lean formalization.

Route A addresses only: four-dimensional, positive-sign, noncollapsed sequences. Even a complete Route A gives a conditional Einstein-existence theorem, not P_4^+ (which requires addressing collapse) and not the full proposition.

## 1. Bridge 1 is resolved by Cheeger–Naber 2015

**Source**: Cheeger–Naber, *Regularity of Einstein Manifolds and the Codimension 4 Conjecture*, Ann. Math. 182 (2015), 1093–1165 (arXiv:1406.6534). Local Knowledge object: `Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md`.

**Key results under bounded Ricci (NOT Einstein)**:

- **Theorem 1.8** (general dim): Under \(|\operatorname{Ric}| \le n-1\) and \(\operatorname{Vol}(B_1(p)) > v > 0\), for each \(q < 2\):
\[
\fint_{B_1(p)} |\operatorname{Rm}|^q \le C(n,v,q).
\]
Under Einstein, the regularity-scale version holds; under just bounded Ricci, the harmonic-radius version (Remark 1.11).

- **Theorem 1.13** (dim 4): Under \(|\operatorname{Ric}| \le 3\) and \(\operatorname{Vol}(B_1(p)) > v > 0\):
\[
\fint_{B_1(p)} |\operatorname{Rm}|^2 \le C(v), \qquad
\operatorname{Vol}\bigl(T_r(\{r_h \le r\})\bigr) \le C(v)\,r^4.
\]
No Einstein hypothesis. The sharp weak-type \(L^2\) estimate on \(r_h\) is a **bounded-Ricci result**.

- **Codimension-4 theorem** (Theorem 1.4 + Corollaries 5.8, Theorem 5.12): The singular set of any noncollapsed GH limit under \(|\operatorname{Ric}| \to 0\) has Hausdorff dimension \(\le n - 4\). In dimension 4: **isolated points**. Tangent cones are \(C(S^3/\Gamma)\) with \(\Gamma \subset SO(4)\) finite (Theorem 5.12 excludes codim-2 and codim-3 singularities using the topological RP² bounding argument).

- **Convergence**: Away from the singular set, the convergence is \(C^{1,\alpha} \cap W^{2,q}\) (Theorem 2.11 + standard ε-regularity in harmonic coordinates). In these coordinates, the limit satisfies \(\operatorname{Ric} = \Lambda g\) weakly, hence is **smooth Einstein** by elliptic regularity.

**Application to our setting**: Our metrics have \(|\operatorname{Ric}(g_i) - \Lambda g_i|_{\operatorname{op}} \le \delta_i \to 0\), hence \(|\operatorname{Ric}(g_i)| \le (\Lambda + \delta_i)\). After normalizing \(\Lambda = 1\), we have \(|\operatorname{Ric}| \le 1 + \delta \le 3\) for \(\delta < 2\). All of the above apply.

**Bridge 1 resolution**: The harmonic-radius ε-regularity, L² curvature bound, and codimension-4 singular-set structure are available from Cheeger–Naber under bounded Ricci. The remaining content of Bridge 1 is that balanced annuli in a bubbling sequence are almost-volume-cones — which follows from Bishop–Gromov volume monotonicity under the lower Ricci bound \(\operatorname{Ric} \ge (\Lambda - \delta)g\), combined with Cheeger–Colding's almost-volume-cone theorem (Lemma 2.4 in Cheeger–Naber, originally [CC96]).

**Step 11 compatibility**: The opposite-warping spike destroys pointwise curvature but preserves volume ratios. Volume monotonicity uses only the lower Ricci bound, which the spike satisfies. Therefore Bridge 1 is not threatened by Step 11.

## 2. Bridge 2: Mode-projection construction

### 2.1 Setup

Near a singular point \(p\) in the GH limit with tangent cone \(C(S^3/\Gamma)\), consider the annular region \(\rho_1 < d(x, p) < \rho_2\) where \(\rho_1\) is the bubble scale and \(\rho_2\) is macroscopic.

By Bridge 1, the harmonic radius satisfies \(r_h(x) \ge c \cdot d(x, p)\) in this annular region. In harmonic coordinates, the metric is \(C^{1,\alpha} \cap W^{2,q}\) and approximates the cone metric:
\[
g_i = g_{\text{cone}} + h_i, \qquad |h_i|_{C^{1,\alpha}} \to 0 \text{ away from }p.
\]

### 2.2 Angular mode decomposition

Decompose symmetric 2-tensors on the cone \(C(S^3/\Gamma)\) into angular modes on \(S^3/\Gamma\). For \(\Gamma = \mathbb{Z}_2\) (the simplest ALE singularity, producing Eguchi–Hanson bubbles), the \(\mathbb{Z}_2\)-invariant TT (transverse-traceless) tensor harmonics have even angular momentum \(l = 0, 2, 4, \ldots\).

The **l = 2** mode is the critical one:
- **Growing mode** \(\rho^2\): carries the orbifold curvature 2-jet at \(p\).
- **Decaying mode** \(\rho^{-4}\): carries the ALE/Eguchi–Hanson asymptotic coefficient.
- **l = 0**: removable singularity (trace/gauge).
- **l \ge 4**: subdominant at the balanced radius.

### 2.3 Mode function and radial ODE

For a TT l = 2 harmonic \(Y\) on \(S^3/\mathbb{Z}_2\), define the **mode function**:
\[
a_i(\rho) = \rho^{-2} \int_{S_\rho/\mathbb{Z}_2} \langle g_i - g_{\text{cone}}, Y \rangle \, dS.
\]

This involves only metric **values** (no derivatives), hence is well-defined and continuous under \(C^{1,\alpha}\) convergence.

From the Bianchi-gauged Ricci equation, \(a_i\) satisfies the l = 2 radial ODE:
\[
a'' + \frac{3}{\rho}\,a' - \frac{8}{\rho^2}\,a = S_i(\rho), \qquad |S_i| \le C\delta_i.
\]

**Verified** (symbolic computation):
- Characteristic equation: \(\alpha^2 + 2\alpha - 8 = 0\), roots \(\alpha = 2, -4\).
- Homogeneous solutions: \(f_1 = \rho^2\), \(f_2 = \rho^{-4}\).
- **Wronskian**: \(W = f_1 f_2' - f_2 f_1' = -6\rho^{-3}\), hence \(\rho^3 W = -6\) (constant).

The constant Wronskian makes the bilinear pairing **scale-independent**: this is the structural reason the obstruction can be read at any radius.

### 2.4 Wronskian extraction on a fixed dyadic annulus

On a dyadic annulus \([R, 2R]\) **in the bubble frame** (R large but fixed, independent of \(t_i\) and \(\delta_i\)), the growing coefficient is extracted from two metric-value measurements:
\[
\alpha_+ = \frac{16\,a(2R) - a(R)}{63\,R^2}.
\]

**Error analysis** (verified numerically): For a constant source \(S = \delta\), the particular solution from variation of parameters is:
\[
f_p(\rho) = \frac{\delta}{6}\,\rho^2 \ln\rho + \text{lower terms}.
\]

The extraction error on the fixed annulus \([R, 2R]\) is:
\[
|\alpha_+^{\text{extracted}} - \alpha_+^{\text{true}}| \le C \cdot \delta \cdot \ln R.
\]

**Critical improvement over the old neck-integration approach**:
- **Old**: error \(\sim \delta \cdot \ln(1/t)\), requiring the artificial rate condition \(\delta \ln(1/t) \to 0\).
- **New**: error \(\sim \delta \cdot \ln R\) for fixed \(R\), requiring only \(\delta \to 0\) (which is given).

The iterated limit procedure:
1. Fix \(R\) large in the bubble frame.
2. Send \(\delta_i \to 0\) along the sequence.
3. The extracted \(\alpha_+\) converges to the orbifold value plus \(O(1/R)\) tail.
4. Send \(R \to \infty\) to recover the exact orbifold coefficient.

Total error: \(O(\delta \ln R) + O(1/R)\), both independently controllable.

### 2.5 Lambda-source growing coefficient

In the bubble frame \(\hat{g} = t^{-2}g\), the Ricci equation becomes:
\[
\operatorname{Ric}(\hat{g}) = \Lambda t^2 \hat{g} + \hat{E}, \qquad |\hat{E}|_{\hat{g}} \le t^2 \delta.
\]

The linearized equation for \(h = \hat{g} - g_{\text{EH}}\) around the Ricci-flat EH metric:
\[
D\operatorname{Ric}_{g_{\text{EH}}}(h) = \Lambda t^2 g_{\text{EH}} + \text{lower order}.
\]

The l = 2 projection of \(g_{\text{EH}}\) at large \(\hat{\rho}\) is \(c_{-4} \hat{\rho}^{-4}\) (the EH asymptotic). The variation-of-parameters particular solution for this source is (**verified symbolically**):
\[
f_p(\hat{\rho}) = \frac{\Lambda t^2 c_{-4}}{24}\,\hat{\rho}^2 + \text{decaying terms}.
\]

This means the **\(\Lambda\) source generates a nonzero growing coefficient**:
\[
\alpha_+^{\text{source}} = \frac{\Lambda t^2 c_{-4}}{24}.
\]

This is \(O(t^2)\) — subleading as \(t \to 0\), but nonzero for any finite \(t > 0\). For smooth matching, the total growing coefficient must be compatible with the orbifold curvature:
\[
\alpha_+^{\text{total}} = \alpha_+^{\text{orbifold}} + \frac{\Lambda t^2 c_{-4}}{24} + O(t^2 \delta \ln R).
\]

As \(t \to 0\): the leading obstruction is the Ozuch condition \(\alpha_+^{\text{orbifold}} = 0\), equivalent to the first obstruction \(\det \mathbf{R} = 0\).

## 3. Connection to the Ozuch obstruction

**Source**: Ozuch, *Noncollapsed degeneration of Einstein 4-manifolds I–II*, local Knowledge object.

The Ozuch first obstruction states: if a sequence of smooth Einstein 4-manifolds converges to an Einstein orbifold with isolated singularities, and the singularities can be desingularized by gravitational instantons, then at each singular point \(p\):
\[
\det \mathbf{R}_{g_o}(p) = 0,
\]
where \(\mathbf{R}\) is the curvature endomorphism on \(\Lambda^2\). For positive Einstein (\(\operatorname{Ric} = \Lambda g\)), this decomposes as \(\mathbf{R}_{\pm} = W_{\pm} + \frac{\Lambda}{3}\operatorname{Id}\) on \(\Lambda^2_\pm\), and the obstruction becomes:
\[
\det\!\left(W_+ + \frac{\Lambda}{3}\operatorname{Id}\right) = 0 \quad \text{or} \quad
\det\!\left(W_- + \frac{\Lambda}{3}\operatorname{Id}\right) = 0.
\]

**Example**: For the round \(S^4\): \(W = 0\), so \(\mathbf{R}_{\pm} = \frac{\Lambda}{3}\operatorname{Id}\), and \(\det \mathbf{R}_{\pm} = (\Lambda/3)^3 \ne 0\). Hence no EH desingularization of orbifolds near the round geometry.

**Mode-projection connection**: The growing coefficient \(\alpha_+\) measured by the mode projection is precisely the bilinear pairing \(\langle \mathbf{R}_+(p) \cdot v, v \rangle\) between the orbifold curvature endomorphism and the ALE direction \(v\). The condition \(\det \mathbf{R}_+(p) = 0\) means there exists a direction \(v\) with \(\mathbf{R}_+ \cdot v = 0\), which is \(\alpha_+ = 0\) for that mode.

The mode-projection approach reads this coefficient from the \(C^{1,\alpha}\)-convergent sequence using \(L^2\) inner products (no metric derivatives), via the constant-Wronskian extraction formula on a fixed dyadic annulus. This **bypasses** the need for a \(C^2\) blow-up limit or second-order jet that does not exist under merely \(C^0\) Ricci pinching.

## 4. Theorem sketch (Route A mode-projection obstruction)

**Conditional Theorem** (noncollapsed positive-sign, dim 4, sketch):

*Let \((M^4, g_i)\) be a sequence of closed Riemannian 4-manifolds with*
\[
|\operatorname{Ric}(g_i) - g_i|_{\operatorname{op}} \le \delta_i \to 0, \qquad
\operatorname{Vol}(M, g_i) \ge v_0 > 0.
\]

*Then either:*
1. *\(M\) admits a smooth Einstein metric (the GH limit is smooth and diffeomorphic to \(M\)), or*
2. *The GH limit is an Einstein orbifold with isolated singularities, each satisfying \(\det \mathbf{R} = 0\).*

**Proof architecture**:
- **Step 1** (Cheeger–Naber): The GH limit \(X\) has singular set of dimension \(\le 0\) (isolated points). Away from singularities, \(C^{1,\alpha} \cap W^{2,q}\) convergence → smooth Einstein limit by elliptic regularity.
- **Step 2** (Diffeomorphism recovery): If no singularities, \(M \cong X\) diffeomorphically, and \(X\) carries the limit Einstein metric. Done.
- **Step 3** (Mode projection at singular points): At each singular point \(p\) with tangent cone \(C(S^3/\Gamma)\), define the l = 2 mode function \(a_i(\rho)\). Under \(C^{1,\alpha}\) convergence, \(a_i\) is well-defined and satisfies the radial ODE with source \(O(\delta_i)\).
- **Step 4** (Wronskian extraction): On a fixed dyadic annulus, extract the growing coefficient with error \(O(\delta_i \ln R)\). In the limit, this equals the Ozuch \(\mathbf{R}_+ \cdot v\) pairing.
- **Step 5** (Obstruction): If \(\det \mathbf{R}_+(p) \ne 0\) for all possible orbifold limits and all singular-point types, no bubbling can occur → only case 1 remains.

**Status**: This is a **theorem sketch**, not a complete proof. The rigorous verification of the Bianchi-gauge → radial-ODE step, the precise definition of mode projection on GH-converging sequences, and the commutator/nonlinear error control remain to be established.

## 5. Negative-branch peer progress

A01 (#354) reports a complete conditional defect gap theorem for the negative branch (near-critical Ishida–LeBrun manifolds), conditional on (H1) DeTurck existence/restart. A03 (#355) claims to discharge (H1) via their Step 37 transported-coefficient DeTurck existence. If both hold, the negative-branch gap theorem would be:

> There exists \(\varepsilon_4 > 0\) such that no near-critical Ishida–LeBrun 4-manifold admits \(\|\operatorname{Ric} + g\|_{\operatorname{op}} < \varepsilon_4\).

**Assessment**: This is conditional on (a) the all-order staggered induction being rigorously formalized (currently TTCS-verified, combinatorially checked 70/70, but schematic at high orders), and (b) the transported-coefficient DeTurck existence being independently verified. Neither has been independently checked by this session. The result addresses only specific four-dimensional negative-sign topologies, not the full Yau-26 proposition.

## 6. What remains for Yau-26

| Front | Status | Next critical work |
|-------|--------|--------------------|
| Positive noncollapsed (Route A) | Mode-projection framework constructed, Bridge 1 resolved | Rigorous Bianchi-ODE verification; determine which orbifold types satisfy det R ≠ 0 |
| Positive collapsed (toric) | Diagonal sector identified, constant-K model has ~1.8% gap | Full variable-curvature det(g^Ω) = φ² existence/nonexistence |
| Negative (flow) | A01/A03 conditional gap for specific topologies | Independent verification; dimension-only gap; bridge from Ric-pinching to U-control |
| Dimensions n ≥ 5 | KK collapse shows positive Einstein collapse exists | No work since Step 24 |
| Lean formalization | Only local algebraic kernels | Entire geometric framework unformalized |

## Files

- Computation: `workspace/scripts/step42_mode_projection_and_bridge_resolution.py`
- Data: `workspace/data/step42_mode_projection_and_bridge_resolution.json`
- Prior Route A notes: `workspace/notes/step33_routeA_consolidation_indicial_topology.md`
- Diagonal toric correction: `workspace/notes/step41_preceptor_review_diagonal_route_and_allocation.md`


## 7. det R₊ computation and Route A's actual reach

**Computation** (verified in `workspace/scripts/step42_det_R_plus_computation.py`):

For a positive Einstein 4-manifold (Ric = Λg), the curvature operator on \(\Lambda^2_+\) is:
\[
\mathbf{R}_+ = W_+ + \frac{\Lambda}{3}\,\mathrm{Id}.
\]

| Orbifold type | \(W_+\) eigenvalues | \(\mathbf{R}_+\) eigenvalues | \(\det \mathbf{R}_+\) | First obstruction |
|---------------|---------------------|-------------------------------|------------------------|-------------------|
| \(S^4\) (round) | (0, 0, 0) | (Λ/3, Λ/3, Λ/3) | (Λ/3)³ > 0 | **EFFECTIVE** |
| \(S^4/\Gamma\) | (0, 0, 0) | (Λ/3, Λ/3, Λ/3) | (Λ/3)³ > 0 | **EFFECTIVE** |
| \(\mathbb{CP}^2\) (FS) | (2Λ/3, −Λ/3, −Λ/3) | (Λ, 0, 0) | 0 | trivial |
| \(S^2 \times S^2\) | (2Λ/3, −Λ/3, −Λ/3) | (Λ, 0, 0) | 0 | trivial |
| Any KE surface | (2Λ/3, −Λ/3, −Λ/3) | (Λ, 0, 0) | 0 | trivial |
| Hyperbolic | (0, 0, 0) | (Λ/3, Λ/3, Λ/3) | (Λ/3)³ ≠ 0 | **EFFECTIVE** |

**Universal KE statement**: For ALL positive Kähler–Einstein 4-manifolds, the Kähler form \(\omega\) satisfies \(W_+\omega = (2\Lambda/3)\omega\) and \(W_+|_{\Lambda^2_{+,0}} = -(\Lambda/3)\,\mathrm{Id}\). Therefore \(\mathbf{R}_+ = \mathrm{diag}(\Lambda, 0, 0)\) in the \((\omega, \Lambda^2_{+,0})\) basis, and \(\det \mathbf{R}_+ = 0\) **always**.

**Consequence for Route A**:

- **Near-round regime**: If the GH limit is a quotient of the round \(S^4\), \(\det \mathbf{R}_+ \ne 0\) everywhere, so no EH bubbling is possible. The limit must be smooth, and the limiting Einstein metric lives on the original smooth manifold \(M\).

- **KE regime**: If the GH limit has Kähler–Einstein geometry at its singular points, \(\det \mathbf{R}_+ = 0\) automatically, and the first obstruction does not prevent bubbling. Higher-order analysis is needed.

**For the stress family \(\#_k(S^2 \times S^2)\)**: The most natural orbifold limits (KE type, close to the product geometry) automatically satisfy the first obstruction. Route A's first-order mode-projection analysis is therefore NOT sufficient to decide the noncollapsed positive case for \(k \ge 2\). The next targets would be:
1. Second-order obstruction (Ozuch's higher Taub/Pohozaev identities)
2. LeBrun–Ozuch classification (if Hermitian/admissible input can be obtained)
3. Topological constraints from the bubble-tree structure (\(b_+ = k \ge 2\) vs Del Pezzo \(b_+ = 1\))

The mode-projection framework itself remains valuable: it provides the machinery to read ANY order obstruction from the C^{1,α}-convergent sequence, not just the first. The l=2 radial ODE, Wronskian constancy, and fixed-annulus extraction work equally for second-order and higher-order coefficients.

## 8. Summary assessment

**Built in this step**:
- Bridge 1 resolution via Cheeger–Naber Theorem 1.13 (source-verified)
- Bridge 2 mode-projection construction (l=2 ODE, Wronskian, VoP, extraction formula)
- Error estimate: O(δ ln R) on fixed annulus, rate-free (no log(1/t))
- Λ-source growing coefficient: Λt²c₋₄/24 (subleading but computable)
- det R₊ computation: first obstruction trivial for all KE orbifolds

**What this changes**: Route A is now a clean conditional theorem sketch with identified bridges. The first-order obstruction is effective against near-round limits but not against KE limits. The stress family requires second-order or classification analysis beyond the first obstruction.

**What this does NOT change**: No branch of Yau-26 is proved or disproved. The construction is for dim 4, positive sign, noncollapsed only. Lean formalization, n ≥ 5, negative branch, and collapsed positive branch remain independent fronts.
