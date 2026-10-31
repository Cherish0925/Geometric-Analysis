# Yau Problem 26: established reduction, current instruments, and open frontier

Session `S0910A02`, Agent2/Constructor, Step 85.

This note records, as mathematics with exact scope, every established result of this session toward the Yau–26 proposition. It is not a final paper; it is a reusable research record with theorem-grade statements, complete proofs or proof references, and honest scope limitations.

---

## 0. The proposition

**Yau Problem 26.** For each integer $n \ge 2$, do there exist real constants $c_n < C_n$ (depending only on dimension) such that any closed, connected, smooth $n$-manifold $M$ carrying a smooth Riemannian metric $g$ with
$$
c_n g \le \operatorname{Ric}_g \le C_n g
$$
(as quadratic forms) necessarily admits some smooth Riemannian metric $h$ with
$$
\operatorname{Ric}_h = \lambda h
$$
for some constant $\lambda \in \mathbb{R}$?

The output metric $h$ need not be close to $g$; the Einstein constant $\lambda$ may have any sign; $c_n, C_n$ are not restricted in sign.

---

## 1. All-dimensional interval prerequisite

**Theorem 1 (Lohkamp prerequisite).** *For $n \ge 3$: Yau–26 is false in dimension $n$ only if there exists a closed connected smooth $n$-manifold carrying no Einstein metric of any sign $\lambda$.*

Equivalently: if every closed connected smooth $n$-manifold admits an Einstein metric, then Yau–26 is true in dimension $n$.

*Proof.* Fix any $c < 0$ and set $C = 0$. For any closed connected smooth $n$-manifold $M$ with $n \ge 3$, Lohkamp's theorem gives a Riemannian metric $g_1$ with $\operatorname{Ric}_{g_1} < 0$ (all Ricci endomorphism eigenvalues negative). Let $\lambda_{\min} < 0$ be the smallest eigenvalue. Set $\alpha = |\lambda_{\min}|/|c| > 0$ and $g' = \alpha g_1$. The $(0,2)$ Ricci tensor is scaling-invariant: $\operatorname{Ric}_{g'} = \operatorname{Ric}_{g_1}$. The hypothesis $c\, g' \le \operatorname{Ric}_{g'} \le 0$ as quadratic forms is equivalent to $c\alpha\, g_1(v,v) \le \operatorname{Ric}_{g_1}(v,v) \le 0$ for all tangent vectors $v$. The upper bound holds because all eigenvalues are negative. For the lower bound: $c\alpha = c \cdot |\lambda_{\min}|/|c| = -|\lambda_{\min}| = \lambda_{\min}$ (since $\lambda_{\min} < 0$), so $c\alpha = \lambda_{\min} \le \lambda_i$ for all eigenvalues $\lambda_i$.

Hence every closed connected smooth $n$-manifold is in the hypothesis class of the interval $[c, 0]$. If Yau–26 holds for this interval, every such manifold admits an Einstein metric. By contrapositive, if Yau–26 is false (i.e., no interval works), the interval $[c, 0]$ must also fail, so some manifold in the hypothesis class — that is, some closed connected smooth $n$-manifold — has no Einstein metric. $\square$

**Corollary 1.1 (high-dimensional prerequisite, current status).** *For $n \ge 5$: Theorem 1 requires any refutation to exhibit a closed $n$-manifold with no Einstein metric. As of the current literature search, no such manifold is known for $n \ge 5$. This is a search status, not a theorem forbidding $n \ge 5$ inquiry: the necessary prerequisite could exist undiscovered. In dimension $4$, the Sambusetti–BCG connected-sum family provides such manifolds (see §8a).*

**Corollary 1.2 (dual formulation).** *For any $n \ge 3$: if every closed connected smooth $n$-manifold admits at least one Einstein metric, then Yau–26 is true with the interval $[c_n, 0]$ for any $c_n < 0$.*

This is the clean framing: **Yau–26 asks how much pinching is required to enter the region where Einstein existence is universal; Theorem 1 shows the boundary is between "no Einstein reservoir exists" (trivially true) and "the reservoir requires tight pinching to detect."**

---

## 2. Dimensions 2 and 3

**Theorem 2 (dimension 2).** *Yau–26 is true in dimension $2$ unconditionally: every closed connected smooth surface admits a constant-curvature metric, hence an Einstein metric, with no pinching hypothesis needed.*

*Proof.* Uniformization theorem. $\square$

**Theorem 3 (dimension 3).** *Yau–26 is true in dimension $3$. The positive branch $P_3^+(\delta)$ holds for any $\delta < 1$: if $(M^3, g)$ is closed connected with $\|\operatorname{Ric}_g - g\|_{\mathrm{op}} \le \delta < 1$, then $M$ admits a positive Einstein metric (a spherical space-form metric).*

*Proof.* The hypothesis gives $\operatorname{Ric}_g > 0$. By Hamilton's theorem (1982), the Ricci flow deforms $g$ to a metric of constant positive sectional curvature. This is Einstein with $\lambda > 0$. $\square$

The negative branch in dimension 3 is also available: sufficiently tight Ricci pinching $\|\operatorname{Ric}_g + g\|_{\mathrm{op}} \le \delta$ forces all sectional curvatures negative (since in dimension 3, sectional curvatures are determined by Ricci curvatures), after which geometrization yields a hyperbolic metric.

---

## 3. Dimension-four interval classification

**Theorem 4 (four-dimensional interval reduction).** *In dimension $4$, the original Yau–26 proposition is equivalent to: at least one strict normalized branch $P_4^+(\delta)$ or $P_4^-(\delta)$ holds for some $\delta \in (0, 1)$, where*
$$
P_4^\sigma(\delta): \quad \|\operatorname{Ric}_g - \sigma g\|_{\mathrm{op}} \le \delta \implies M \text{ admits an Einstein metric}, \qquad \sigma = \pm 1.
$$
*A refutation in dimension $4$ must defeat both strict branches; a proof needs only one.*

*Proof.* We classify all interval types and show only strict one-signed intervals survive.

**Case 1: $c < 0 < C$ (zero in interior).** For any closed $4$-manifold $M$, take any smooth metric $g_0$ and set $g = tg_0$ for large $t > 0$. Then $\operatorname{Ric}_g = \operatorname{Ric}_{g_0}$ has bounded eigenvalues, while $cg(v,v) = ct g_0(v,v)$ and $Cg(v,v) = Ct g_0(v,v)$ scale linearly. For $t$ large enough, $ct \le \lambda_{\min}(\operatorname{Ric}_{g_0})$ and $Ct \ge \lambda_{\max}(\operatorname{Ric}_{g_0})$, so $cg \le \operatorname{Ric} \le Cg$. Every manifold is in the hypothesis class; $S^1 \times S^3$ has no Einstein metric (below), so this interval fails.

**Case 2: $c = 0 < C$ (nonnegative boundary).** $S^1 \times S^3$ with the flat circle times round $S^3$ has $\operatorname{Ric} = \operatorname{diag}(0, 2, 2, 2) \ge 0$. After rescaling, $0 \le \operatorname{Ric} \le Cg$ for any $C > 0$. Same manifold, no Einstein.

**Case 3: $c < 0 = C$ (nonpositive boundary).** Lohkamp gives a metric on $S^1 \times S^3$ with $\operatorname{Ric} < 0$. After rescaling: $cg \le \operatorname{Ric} \le 0$. Same manifold, no Einstein.

**Case 4: $0 < c < C$.** Rescale: $h = \frac{c+C}{2}\, g$. Since $\operatorname{Ric}_h = \operatorname{Ric}_g$ as a $(0,2)$ tensor, $cg \le \operatorname{Ric}_g \le Cg$ becomes $(1-\delta)h \le \operatorname{Ric}_h \le (1+\delta)h$, equivalently $\|\operatorname{Ric}_h - h\|_{\mathrm{op},h} \le \delta$, with $\delta = (C-c)/(C+c) \in (0,1)$. This is $P_4^+(\delta)$. (The scale $\alpha = (c+C)/2$ is the unique positive constant centering the interval at $+1$; the Codex-verified Lean theorem `positive_centering_scale_unique` confirms this.)

**Case 5: $c < C < 0$.** Rescale: $h = -\frac{c+C}{2}\, g$. Then $cg \le \operatorname{Ric}_g \le Cg$ becomes $(-1-\delta)h \le \operatorname{Ric}_h \le (-1+\delta)h$, equivalently $\|\operatorname{Ric}_h + h\|_{\mathrm{op},h} \le \delta$, with $\delta = (C-c)/(-(C+c)) \in (0,1)$. This is $P_4^-(\delta)$.

**No-Einstein certificate for $S^1 \times S^3$.** If $(S^1 \times S^3, h)$ is Einstein with $\operatorname{Ric}_h = \lambda h$, then $\chi(S^1 \times S^3) = 0$ and the four-dimensional Chern–Gauss–Bonnet formula gives
$$
0 = 8\pi^2 \chi = \int \left(|W|^2 + \frac{s^2}{24}\right) d\mu \ge 0,
$$
forcing $W = 0$ and $s = 0$. Combined with $E = \operatorname{Ric} - (s/4)g = 0$ (Einstein), the metric is flat. A closed flat 4-manifold has a Bieberbach fundamental group, which is virtually $\mathbb{Z}^4$ (first Bieberbach theorem). But $\pi_1(S^1 \times S^3) = \mathbb{Z}$, whose finite-index subgroups have rank 1, not 4. Contradiction. $\square$

---

## 4. Near-pinched construction theorem

**Theorem 5 (fixed-$A_1$ log-Weyl construction).** *Let $(\mathcal{O}^4, g_0)$ be a closed oriented Einstein 4-orbifold with $\operatorname{Ric}(g_0) = \sigma g_0$, $\sigma = \pm 1$, having finitely many $A_1$ singularities $\{p_1, \ldots, p_N\}$. Fix equivariant normal coordinate charts, Eguchi–Hanson end markings and chiralities, and common radial normal gauge between the EH far-field and ambient quadratic jets, with $O_2$ control of the EH tail and ambient Taylor remainder. Then for each fixed chirality/marking assignment, the smooth marked resolution $M$ carries a one-parameter family of metrics $g_a$ ($a \to 0^+$) with*
$$
\|\operatorname{Ric}_{g_a} - \sigma g_a\|_{\mathrm{op}} \le \frac{C}{|\log a|},
$$
*where $C$ depends on the fixed orbifold, node, marking, cutoff, and gauge data but not on $a$.*

**Proof architecture.** Three zones:

1. **Core ($r \le b = a^{1/2}$).** The biaxial Einstein family $q_\Lambda$ on $\mathcal{O}(-2)$ is differentiated at $\Lambda = 0$ and the radial gauge vector $V = \frac{5}{72}(r^3 - r^{-1})\partial_r$ subtracted to obtain $\widetilde{h}$ solving $D\operatorname{Ric}_{\mathrm{EH}} \widetilde{h} = g_{\mathrm{EH}}$ with $O_2$ ALE tail. Residual: $(0,2)$-tensor $O(a^4(1+\rho)^2)$; raised-index $O(a^2 + r^2)$; inner cutoff at $r = b$: $O(a)$.

2. **Log annulus ($b \le r \le R = a^{1/4}$).** Quadratic Weyl mismatch $K_{ij} = -\frac{1}{3}C_{ikjl}x^k x^l$ satisfies $\operatorname{tr} K = 0$, $\operatorname{div} K = 0$, $\Delta K = 0$, $K(x, \cdot) = 0$, and $D\operatorname{Ric}_e K = 0$. For arbitrary smooth radial cutoff $\eta(t)$, $t = \log r$:
$$
D\operatorname{Ric}_e(\eta K) = -\frac{1}{2}\Delta(\eta K) = -\frac{\eta_{tt} + 6\eta_t}{2r^2} K.
$$
Optimal linear interpolation gives defect $O(1/L)$ with $L = \log(R/(8b)) = \frac{1}{4}|\log a| + O(1)$.

   The full ten-dimensional Weyl quadratic space (five in each chirality $\operatorname{Sym}^2_0(\Lambda^\pm)$) has been verified computationally in Step 83 (`workspace/data/step83_full_weyl_log_annulus_audit.json`): all basis tensors satisfy the required identities. This addresses product-node non-$U(2)$ sectors.

3. **Ambient ($r \ge R$).** $A_1$ evenness gives $g_0 = e + H_0 + O_2(r^4)$. At $r = R = a^{1/4}$: $O(R^2) = O(a^{1/2})$.

**Global.** The four (or $N$) modification balls are disjoint for small $a$; Ricci is local; the global constant is $C = \max_j C_j$ over finitely many nodes. $\square$

**Scope.** Theorem 5 is a near-pinched input construction, not an existence or nonexistence theorem. It is sign-neutral: it applies to positive and negative Einstein orbifolds alike.

---

## 5. Variational closure: the L² size of the near-pinched family

**Proposition 6 (L² closure).** *The near-pinched family $g_a$ of Theorem 5 satisfies*
$$
\int_M |E_{g_a}|^2 \, dV_{g_a} = O\!\left(\frac{a}{|\log a|^2}\right) \to 0,
$$
*where $E = \operatorname{Ric} - (s/4)g$ is the traceless Ricci tensor. This is polynomially small in $a$, much faster than the $C^0$-defect $O(1/|\log a|)$.*

*Proof.* The modification lives in $N$ balls of radius $R = a^{1/4}$. In each ball, $|E|_{\mathrm{op}} \le C/L$ with $L \asymp |\log a|$. The volume of each ball is $\omega_4 R^4 = \omega_4 a$. Outside, $E = 0$. Hence
$$
\int |E|^2 \le N \cdot \frac{C^2}{L^2} \cdot \omega_4 a = O(a / |\log a|^2). \quad \square
$$

**Consequence.** The scale-invariant functional $F(g) = 8\pi^2\chi + \frac{1}{2}\int|E|^2$ satisfies $\inf F = 8\pi^2\chi$ on each fixed row, with the infimum attained only in the degenerate orbifold-plus-EH limit. The energy ledgers are exact:
- Positive mirror (4 nodes): $16\pi^2 + 4 \cdot 12\pi^2 = 64\pi^2 = 8\pi^2 \cdot 8$.
- Negative mirror (36 nodes): $16\pi^2 + 36 \cdot 12\pi^2 = 448\pi^2 = 8\pi^2 \cdot 56$.

**No $L^p$ instrument with $p \ge 2$ can obstruct these rows.** For general $p \ge 2$:
$$
\left(\int |E|^p\right)^{1/p} \le \|E\|_\infty^{(p-2)/p} \left(\int |E|^2\right)^{1/p} = O\!\left(\frac{1}{|\log a|^{(p-2)/p}} \cdot \frac{a^{1/p}}{|\log a|^{2/p}}\right) = O\!\left(\frac{a^{1/p}}{|\log a|}\right),
$$
which vanishes polynomially. The unweighted $C^0$ operator norm is the only sharp norm, consistent with the $\ell = 2$ quadratic-mode classification: only the degree-2 cone mode is unweighted logarithmically critical.

**The variational route is closed.** The near-pinched family $g_a$ is a genuine degenerating minimizer of $Z = \int |E|^2$ with $\inf Z = 0$. Any concentration-compactness or almost-critical epsilon-regularity theorem would need to handle the polynomial-vs-logarithmic mismatch between $Z(g_a) = O(a/|\log a|^2)$ and $\|E\|_\infty = O(1/|\log a|)$. The infimum is not attained by any smooth metric; the family degenerates to the orbifold boundary. This is not a gap one can close with standard PDE machinery.

---

## 6. Test families: positive and negative mirrors

### 6.1 Positive mirror

The orbifold $(S^2 \times S^2)/\langle r_\pi \times r_\pi \rangle$ with product Einstein metric $\operatorname{Ric} = g$ has 4 $A_1$ points. By Theorem 5, every chirality/marking pattern gives a smooth resolution with $\|\operatorname{Ric} - g\| = O(1/|\log a|)$. The resolutions include:

| Pattern $r$ | Topology | $(b_+, b_-)$ | $\tau$ | Spin? |
|---|---|---|---|---|
| 0 | $\mathbb{CP}^2 \# 5\overline{\mathbb{CP}}{}^2$ | (1,5) | −4 | No |
| 1 | $2\mathbb{CP}^2 \# 4\overline{\mathbb{CP}}{}^2$ | (2,4) | −2 | No |
| 2 adj | $3\mathbb{CP}^2 \# 3\overline{\mathbb{CP}}{}^2$ | (3,3) | 0 | No |
| 2 diag | $\#_3(S^2 \times S^2)$ | (3,3) | 0 | Yes |
| 3 | $4\mathbb{CP}^2 \# 2\overline{\mathbb{CP}}{}^2$ | (4,2) | 2 | No |

All have $\chi = 8$, are simply connected, PSC, strict Hitchin–Thorpe, SW-void, and non-Kähler/non-symplectic in both orientations. The mixed rows ($r = 1, 2, 3$) are outside all known positive Einstein existence classifications and all known no-Einstein certificates.

### 6.2 Negative mirror

The orbifold $(\Sigma_2 \times \Sigma_2)/\langle \iota \times \iota \rangle$ with product Einstein metric $\operatorname{Ric} = -g$ has 36 $A_1$ points, $\chi_{\mathrm{smooth}} = 56$. By Theorem 5, every 36-node pattern carries metrics with $\|\operatorname{Ric} + g\| = O(1/|\log a|)$. Mixed rows have similar SW-void, non-Kähler/non-symplectic properties.

### 6.3 Refutation requirements

A full dimension-four refutation of Yau–26 requires:
1. One positive-mirror mixed row with no Einstein metric of any sign $\lambda$.
2. One negative-mirror mixed row with no Einstein metric of any sign $\lambda$.
3. The $S^1 \times S^3$ argument for boundary/crossing intervals (Theorem 4).

Item (1) alone refutes $P_4^+$; item (2) alone refutes $P_4^-$.

---

## 7. Capped instruments and sign-leg map

### 7.1 Positive Einstein leg ($\lambda > 0$)

**Alignment mechanism collapses to Gursky–LeBrun.** The summed Weitzenböck chain for $b_+$ harmonic self-dual forms gives $\int |W^+|^2 \ge 6V$ (Step 81), which is exactly the Gursky–LeBrun estimate independent of $b_+$. The balanced $(\chi, \tau) = (8, 0)$ row has Bishop-normalized gap factor $\sqrt{3/2} \approx 22.5\%$, far from contradiction. The CLR approach requires $C_{\mathrm{CLR}} < 12$, but $\mathbb{CP}^2$ forces $C_{\mathrm{CLR}} \ge 36$. No known integral mechanism can obstruct positive Einstein on the mixed rows.

**Open targets.** The tensor PDE $\nabla^*\nabla T = BT + TB - 2S$ with $B = 2W^+ - 4I$ and $S \ge 0$; the Gram degeneracy from $p_1(\Lambda^+) = 16 \ne 0$; and the Einstein threshold-CLR using $\delta W^+ = 0$ remain open theorem-shaped objects.

### 7.2 Ricci-flat leg ($\lambda = 0$)

Compact simply connected Ricci-flat 4-manifolds with flat, reducible, or $SU(2)$ holonomy are excluded on the $\chi = 8$ rows: flat has $\chi = 0$, reducible requires flat factors of lower dimension, and the $SU(2)/\text{hyperkähler}$ case is K3 with $\chi = 24$. The open loophole is generic irreducible $SO(4)$-holonomy compact Ricci-flat, which is unknown in any dimension and doubly unprecedented on manifolds also carrying PSC metrics.

### 7.3 Negative Einstein leg ($\lambda < 0$)

CGB depends on $\lambda^2$, giving no sign-specific advantage. Known negative-Einstein nonexistence tools (LeBrun monopole, symplectic methods) require input destroyed by the embedded $+2$-spheres and PSC/SW-void structure. No compatible obstruction is known.

### 7.4 Summary

The fixed-row no-Einstein problem is a conjunction of three frontier problems. No single instrument currently covers any of the three legs.

---

## 8. The LeBrun negative-branch sequence question

The stable integral obstruction (Step 3) gives: for LeBrun manifolds $M = X \# k\overline{\mathbb{CP}}{}^2$ with $p = k/A > 1/3$,
$$
\frac{\delta}{1-\delta} \ge \sqrt{\frac{p - 1/3}{2}}.
$$
At $p = 1/3$ the bound gives $\delta \ge 0$ (vacuous), while LeBrun's theorem still excludes Einstein metrics at $k = A/3$.

**Question (LeBrun sequence).** *Does there exist a sequence of minimal complex surfaces $X_i$ of general type with $A_i = c_1^2(X_i) \to \infty$, integers $k_i$ with $k_i/A_i \to 1/3^+$, and metrics $g_i$ on $M_i = X_i \# k_i \overline{\mathbb{CP}}{}^2$ with $\|\operatorname{Ric}_{g_i} + g_i\|_{\mathrm{op}} \to 0$?*

**Significance.** If yes: every strict negative interval is defeated by LeBrun-obstructed manifolds, reducing the dimension-four refutation to the positive branch $P_4^+$ alone. If no: the negative branch $P_4^-$ remains a potential proof direction.

**Burns core tension.** The ordinary $(-1)$-blowup core (Burns metric on $\mathcal{O}(-1) \to \mathbb{CP}^1$) is NOT Ricci-flat. Its Ricci endomorphism has eigenvalues of order 1 (not $o(1)$ in the gluing parameter), giving a raised-index $C^0$ defect of $O(1)$. This is fundamentally different from the $A_1$/Eguchi–Hanson core, which is Ricci-flat and produces only the $O(1/|\log a|)$ Weyl-transition defect. Naive local gluing therefore cannot produce tight negative pinching on $(-1)$-blowups.

**Pinching–monopole disjointness (corrected scope).** On the *positive* side there is a genuine class-level disjointness: tight positive Ricci pinching forces positive scalar curvature, and the Weitzenböck argument kills all monopole classes, so no BF/monopole no-Einstein certificate can coexist with a positively pinched metric.

On the *negative* side there is no class-level exclusion. The integral accounting is permissive: $\int s^2 \ge 32\pi^2 (a^+)^2$ holds for every metric, tight negative pinching gives $s \approx -4$ and $\operatorname{Vol} \le 12\pi^2\chi$, hence $(a^+)^2 \le 6\chi$ — while LeBrun-type exclusion needs $(a^+)^2 > 3(2\chi+3\tau) = 6\chi + 9\tau$, satisfied with room whenever $\tau < 0$, and the entire blow-up reservoir has $\tau \ll 0$. **Nothing forbids a LeBrun-obstructed manifold from being tightly negatively pinched by some mechanism other than $A_1$ resolutions.**

What *is* established is narrower: the specific $A_1$-resolution construction machine of Theorem 5 is disjoint from the known BF/monopole certificates, for two separate reasons. Compatible nodes place the resolution in the Kähler smoothing / ample-canonical regime where Aubin–Yau supplies a negative Kähler–Einstein metric (so it is not a no-Einstein example). Reversed nodes insert non-torsion embedded $+2$-spheres, which kill ordinary SW basic classes by adjunction and, via Iida–Mukherjee–Taniguchi's relative BF adjunction inequality applied through the punctured/closed interface $BF(X^\circ) = BF(X)$, also kill the standard closed BF invariants used by Ishida–LeBrun. This is disjointness for the certificates the literature actually uses within our construction class — not a claim that every conceivable gauge invariant vanishes, and not a class-level obstruction to arbitrary negative pinching.

**Possible escapes.** (a) A non-local construction (Ricci flow, conformal deformation, Kähler-edge/cuspidal methods) might avoid the Burns core. (b) A different no-Einstein reservoir not requiring $(-1)$-blowups could provide the sequence — the Sambusetti–BCG family of §8a is exactly such a reservoir. (c) Conversely, the Burns obstruction might extend to ALL construction methods on these manifolds, making $P_4^-$ genuinely true.

---

## 8a. The Sambusetti–BCG entropy reservoir (non-gauge, all-sign)

The negative-branch landscape is not exhausted by monopole methods. Entropy supplies an all-sign no-Einstein family inside the pinching-compatible topological window.

**Theorem 8a.1 (Sambusetti, via Kotschick/BCG).** *Let $N^4$ be a closed oriented real-hyperbolic 4-manifold with sectional curvature $-1$, and $M_N = N \# N$. Then*
$$
\chi(M_N) = 2\chi(N) - 2, \qquad \tau(M_N) = 0, \qquad \|M_N\| = 2\|N\| > 0,
$$
*and $M_N$ admits no Einstein metric of any sign $\lambda$, despite satisfying strict Hitchin–Thorpe and having $\chi > 0$.*

*Proof.* Collapsing one punctured summand gives a degree-two map $f: M_N \to N$. Kotschick's Corollary 3 (attributed to Sambusetti) states that a closed oriented Einstein 4-manifold $X$ with a degree-$d$ map to a closed real-hyperbolic $Y$ satisfies $\chi(X) \ge \frac{3}{2}|\sigma(X)| + |d|\chi(Y)$, with equality only if $X$ is real hyperbolic. Here this demands $2\chi(N) - 2 \ge 2\chi(N)$, impossible. $\square$

Unlike monopole/BF certificates, this is a homotopy/entropy obstruction: it needs no Kähler, symplectic, spin, or gauge input, and it is not destroyed by positive scalar curvature considerations (the manifolds have $\|M_N\| > 0$, which itself excludes $\operatorname{Ric} \ge 0$).

**Theorem 8a.2 (quantitative pinching threshold).** *If $g$ is a metric on $M_N$ with $\|\operatorname{Ric}_g + 3g\|_{\mathrm{op}} \le \delta = 3\varepsilon$, then BCG (which needs only $\operatorname{Ric} \ge -3\hat g$ after rescaling by $1+\varepsilon$) gives $\operatorname{Vol}_g \ge 2\operatorname{Vol}(N)/(1+\varepsilon)^2$, while Chern–Gauss–Bonnet with $\frac{s^2}{6} - \frac{|\operatorname{Ric}|^2}{2} \ge 6(1-\varepsilon)^2$ gives $\operatorname{Vol}_g \le 2\operatorname{Vol}(N)(1 - 1/\chi(N))/(1-\varepsilon)^2$. These are incompatible for*
$$
\varepsilon < \varepsilon_\chi = \frac{1 - \sqrt{1-1/\chi(N)}}{1 + \sqrt{1-1/\chi(N)}} = \frac{1}{4\chi(N)} + O(\chi(N)^{-2}),
$$
*i.e. $\delta \lesssim 3/(4\chi(N))$.*

**Critical limitation: the certificate is additive.** The volume deficit arises entirely from the fixed additive constant in $\chi(M_N) = 2\chi(N) - 2$ — a deficit of $8\pi^2/3$ in volume terms, independent of $N$. Consequently the threshold $\delta_\chi \to 0$ as $\chi(N) \to \infty$: **no additive certificate can produce a uniform $\delta_0 > 0$.** This obstruction *prices* a refutation of $P_4^-$ at rate $O(1/\chi)$; it cannot close the branch. Closing it would require a multiplicative uniform gap $\operatorname{Vol} \ge 2(1+\varepsilon_0)\operatorname{Vol}(N)$ valid for all hyperbolic $N$, which is implausible because a connect-sum cost is localized. Note also that at the critical rate the same accounting forces $\int|W|^2 = O(1)$.

**Theorem 8a.3 (warped-product waist barrier).** *For $g = dr^2 + f(r)^2 g_F$ on $\mathbb{R}\times F^3$ with $\operatorname{Ric}_F = 2k\,g_F$, the Ricci endomorphism eigenvalues are $\lambda_r = -3f''/f$ and $\lambda_F = 2k/f^2 - f''/f - 2(f'/f)^2$. At a waist ($f' = 0$, $f'' \ge 0$) with $k \ge 0$, the defect from $-3$ satisfies*
$$
\delta = \max\bigl(3|1-\alpha|,\ |3 - \alpha + \beta|\bigr) \ge \tfrac{3}{2}, \qquad \alpha = f''/f,\ \beta = 2k/f^2,
$$
*with equality exactly at $k = 0$, $\alpha = 3/2$ (large flat fiber). For the round $S^3$ fiber, $\delta = \frac{3}{2} + \frac{3}{2f_0^2} > \frac{3}{2}$ at every scale.*

So a round $S^3$ waist and a flat $T^3$ waist both cost $\delta \ge 3/2$, **independent of scale and of collar length.** This is a *pointwise* obstruction, which cannot be amortized over volume the way CGB energy accounting can — explaining why no monotone functional argument closes the connector problem and why no construction achieves it. The exception is illuminating: a defect-free waist exists when the cross-section is negatively curved, e.g. $f = \cosh r$ over hyperbolic $F$ — but that metric is simply $\mathbb{H}^4$ in coordinates equidistant from a totally geodesic $\mathbb{H}^3$. The fibers permitting a turnaround are exactly those whose gluings produce hyperbolic, hence Einstein, manifolds.

For a general (non-warped) minimal separating $\Sigma^3$, the traced Gauss equation gives $\operatorname{Scal}_\Sigma \approx -6 - |A|^2$, which is not yet a contradiction. A general "no near-pinched $S^3$ or $T^3$ waist" lemma would be a real theorem, and it would kill both known negative reservoirs at once, since LeBrun blow-ups and Sambusetti sums are both connected sums (the Burns $t^{-1}$ defect is the blow-up instance of the same phenomenon).

**Theorem 8a.4 (Chern–Weil neutrality, Step 90).** *For any Ricci-flat ALE 4-space, $|\Delta\tau| \le \frac{2}{3}\Delta\chi$ with equality iff half-flat. Hence for any orbifold+Ricci-flat-ALE resolution: $\chi(M) - \frac{3}{2}|\tau(M)| \ge \chi_{\mathrm{orb}} - \frac{3}{2}|\tau_{\mathrm{orb}}|$.*

*Proof.* $|12\pi^2\Delta\tau| = |\int(|W^+|^2 - |W^-|^2)| \le \int|W|^2 = 8\pi^2\Delta\chi$, so $|\Delta\tau| \le \frac{2}{3}\Delta\chi$. Triangle inequality on $\tau(M)$ gives $|\tau(M)| \le |\tau_{\mathrm{orb}}| + \frac{2}{3}\sum\Delta\chi_i$, and the cancellation $\sum\Delta\chi_i - \frac{3}{2}\cdot\frac{2}{3}\sum\Delta\chi_i = 0$ yields the result. $\square$

**Theorem 8a.5 (Entropy inaccessibility, Step 90).** *For any smooth $A_1$ resolution $M$ of any closed real-hyperbolic 4-orbifold $\mathcal{O}$, and any degree-$d \ne 0$ map $f: M \to Y$ ($Y$ closed hyperbolic): $d \cdot \chi(Y) \le \chi_{\mathrm{orb}}(\mathcal{O})$. Hence the Sambusetti inequality is automatically satisfied and no entropy certificate can obstruct Einstein metrics on $M$.*

*Proof.* Near-pinched construction $\Rightarrow$ $\operatorname{Ric} \ge -(3+\varepsilon)g$, $\operatorname{Vol} \to \operatorname{Vol}(\mathcal{O})$. BCG $\Rightarrow$ $d \cdot \operatorname{Vol}(Y) \le \operatorname{Vol}(\mathcal{O})$. Convert via $\chi = \frac{3}{4\pi^2}\operatorname{Vol}$. Non-decrease $\Rightarrow$ $\chi(M) - \frac{3}{2}|\tau(M)| \ge \chi_{\mathrm{orb}} \ge d\cdot\chi(Y)$. $\square$

**The Step 88 §4.3 decisive question is answered NEGATIVELY** for ALL orbifold+ALE resolutions. No $\pi_1$ computation or simplicial-volume estimate is needed: the BCG volume bound from the near-pinched metrics closes the route at once.

**Triple disjointness (Step 90).** All three known families of no-Einstein certificates are independently blind to the near-pinched construction: (1) PSC/Weitzenböck kills monopoles on the positive side; (2) IMT adjunction kills BF on the negative side; (3) Chern–Weil neutrality + BCG kills entropy on all sides. A refutation must construct near-pinched metrics outside orbifold+ALE (non-warped connector) or discover a new no-Einstein mechanism. Full analysis: `workspace/notes/step90_chernweil_neutrality_and_triple_disjointness.md`. Data: `workspace/data/step90_chernweil_neutrality_verification.json`.
---

## 9. Higher obstructions and mode classification

**Theorem 7 ($\ell = 2$ uniqueness).** *Among the radial cone modes on a flat $A_1$ cone, only the quadratic ($\ell = 2$) mode is unweighted logarithmically critical for $C^0$-Ricci pinching. The annular mass of the degree-$\ell$ TT mode is*
$$
H_2(b, R) = \log(R/b), \qquad H_\ell(b, R) = \frac{b^{2-\ell} - R^{2-\ell}}{\ell - 2} \quad (\ell > 2).
$$
*Higher exact-gluing obstructions contribute $O(t^{k-1})$ as Ricci endomorphisms ($k \ge 2$), subcritical relative to $O(1/|\log a|)$. Tight pinching alone cannot force the entire Biquard–Ozuch obstruction tower to vanish.*

This retires the compactness-to-exact-desingularization proof route: the first obstruction is the unique critical mode, and it vanishes nontransversally on a 2-plane rather than being forced to zero by pinching.

### 9.1 Local second obstruction and Step99 trace-channel Gate 3

From Ozuch's formula ([Biq16, Lemme 9]; Ozuch arxiv:2012.13316, lines 673–706), when the first obstruction \(\lambda_k=0\),
$$
\mu_1=C\det\begin{pmatrix}R_{22}&R_{23}\\R_{32}&R_{33}\end{pmatrix},\quad C>0.
$$
For the product orbifold with \(R^\pm=\mathrm{diag}(\Lambda,0,0)\), any \(\zeta\in K=\ker R^\pm\) leaves a rank-one adapted block and hence \(\mu_1=0\).  The full projected quadratic map \(K\to K\) vanishes by the corrected \(T^2\)-weight-parity proof (not by the invalid SO(2)-transitivity argument): the \(\beta=0\) subcircle has weight one on \(K\), and no degree-two monomial has weight one.  **Consequence:** the \(O(t^2)\) local self-correction is absent from the kernel equation; pattern dependence begins at the \(O(t^3)\) inter-node response.

Step 99 audited A01 Step 98's full raw chirality computation.  Physical same-chirality inter-node maps \(B_{++}=B_{--}\) vanish in AB and AA/BB sectors at every checked rung, agreeing with the compatible Kähler-smoothing calibration from Biquard--Rollin and OSS/Tian--Yau.  Physical cross-chirality AB response is a pure isotropic (trace) channel: adjacent pairs have isotropic eigenvalue \(c_{\rm adj}=+0.06288499464\); the diagonal pair has \(c_{\rm diag}=-0.035453521442\).  AA/BB tensor cross-chirality channels are purely traceless with adjacent coefficient magnitude \(q_{\rm adj}=0.0080049973185\).

**Step 100: structural diagonal tensor vanishing.**  The diagonal tensor cross-chirality coefficient \(q_{\rm diag}=0\) identically at all spectral rungs.  *Mechanism:* the cos\((2\phi)\) and sin\((2\phi)\) tensor modes at antipodal \(S^2\) poles have sign ratios \((-1)^\ell\) and \(-(-1)^\ell\); the SO(2) rotational symmetry of the kernel plane ensures equal contribution magnitudes, giving exact pairwise cancellation at every spectral level.  This is a structural identity, not a numerical coincidence.

**Step 100: four-node exchange-closure theorem.**  In the adjacent balanced pattern \(\varepsilon=(+,+,-,-)\), the two receivers in each chirality class have swapped adjacent/diagonal roles to the opposite class.  Writing \(r=u_4/u_3\), the single-node feasibility window for node 1 is the reciprocal of node 2's.  They can overlap only if \(r=1\) is feasible:
\[
|c_{\rm adj}+c_{\rm diag}|\le q_{\rm adj}+q_{\rm diag}.
\]
With the audited values \(|c_{\rm adj}+c_{\rm diag}|=0.027431\), \(q_{\rm adj}=0.008005\), \(q_{\rm diag}=0\): the condition fails with margin \(0.019426\).

**Positive mirror leading obstruction (Step 100).**  Combined with the single-node diagonal-balanced and one/three-reversed obstructions (margin \(0.054880\)), **ALL five mixed chirality patterns on the positive mirror are obstructed at leading inter-node order**.  The compatible pattern \(\varepsilon=(+,+,+,+)\) has \(f_4\equiv0\) by the same-chirality vanishing, consistent with KE existence via Tian--Yau/OSS.  The coefficient table reproduces the known KE/non-KE dichotomy: same-chirality vanishing \(\Rightarrow\) \(f_4=0\) on the compatible locus (KE by Tian--Yau); nonvanishing cross-chirality couplings on mixed rows (non-Kähler/non-symplectic).

This remains a leading inter-node computation, not a complete gluing theorem: a calibrated LS reduction, self/complement/frame/global term accounting, and a relative \(o(t^3)\) remainder are still required.  Even a completed local obstruction would not prove that the same smooth row carries no distant Einstein metric.
---

## 10. Transition-scale and collapse infrastructure

**Proposition 8 (transition scale).** *For a collapsing near-Einstein sequence on a closed 4-manifold with $\chi > 0$, the Bishop–Gromov transition scale $\rho_\varepsilon(x) = \sup\{r : \Theta(x,r) \ge \varepsilon\}$ provides a rescaling at which the Ricci bound vanishes, volume ratio is bounded, and any pointed limit is $\mathrm{RCD}(0,4)$ with AVR $\le \varepsilon$. This requires two-sided Ricci control; one-sided collapse (shrinking round spheres) is a counterexample.*

**ALE exclusion (qualified).** On balanced $(\chi, \tau) = (8, 0)$ rows, one-chirality Chern–Weil budget gives Kronheimer ADE rank $\le 3$, $|\Gamma| \le 4$ ($A_3$). For outermost transition $\varepsilon < 1/4$, no hyperkähler ALE model fits. However, class-$T$ Ricci-flat Kähler ALE smoothings have unbounded end-group order at fixed energy, and non-$SU(2)$-holonomy ALE families are not excluded.

**Scope.** The transition-scale theorem applies only to $\mathrm{Vol} \to 0$ sequences. The decisive near-pinched families on the mixed rows are noncollapsed (converging to a fixed-volume orbifold), so the transition theorem does not directly address them.

---

## 11. Current status by dimension

| Dimension | Status | Key mechanism |
|---|---|---|
| $n = 2$ | **True.** | Uniformization. |
| $n = 3$ | **True.** | Hamilton/geometrization. |
| $n = 4$ | **Open.** | Reduces to strict branches $P_4^\pm(\delta)$. Boundary/crossing-zero intervals fail by $S^1\times S^3$. Negative side: Sambusetti--BCG gives all-sign no-Einstein $N\#N$ but only an additive $O(1/\chi)$ near-negative obstruction; scalar-excess diffuseness and A03 OT/waist barriers leave the diffuse non-OT connector frontier open. Positive side: the fixed-$A_1$ near-pinch construction gives metrics on all product-mirror rows. **Step 100:** ALL mixed rows of the positive mirror are obstructed at leading inter-node order, by the four-node exchange-closure theorem (adjacent balanced, margin $0.01943$) and single-node adjacent dominance (other patterns, margin $0.05488$), with the structural diagonal tensor vanishing $q_{\rm diag}=0$. The coefficient table reproduces the known KE/non-KE dichotomy. Full LS/remainder control and global no-Einstein arguments still missing. |
| $n \ge 5$ | **Open.** | No certified closed manifold without an Einstein metric found in current search. **Structural theorem (Step 94):** all known negative-Einstein obstructions use the 4D Einstein CGB identity $8\pi^2\chi = \int|W|^2 + \frac23\lambda^2V$ or the self-dual splitting $\Lambda^2 = \Lambda^+\oplus\Lambda^-$; neither survives above dimension 4. For $n$ odd, $\chi=0$ and no CGB exists; for $n=2m\ge6$, the Pfaffian involves indefinite cross-terms. On the positive side, Gromov's bound ($\operatorname{Ric}\ge0\Rightarrow\|M\|=0$) works in all dimensions. Thus refutation for $n\ge5$ requires a fundamentally new mechanism. |

---

## 12. Evidence files

- `workspace/data/step85_L2_variational_closure.json`: L² size, interval theorem, LeBrun table.
- `workspace/data/step84_interval_variational_audit.json`: interval classification, mirror energy budgets.
- `workspace/data/step83_full_weyl_log_annulus_audit.json`: ten-sector Weyl identity verification.
- `workspace/data/step82_sign_leg_and_ricciflat_scope.json`: sign-leg corrected Chern–Weil formulas.
- `workspace/data/step88_warped_waist_and_bcg_threshold.json`: waist barrier and BCG threshold.
- `workspace/notes/step88_sambusetti_bcg_waist_and_disjointness.md`: full §8a analysis.
- `workspace/notes/step81_alignment_mechanism_definitive.md`: alignment-to-Gursky–LeBrun collapse.
- `workspace/notes/step83_near_pinched_construction_and_frontier_reduction.md`: audited construction with TTCS corrections.
- `workspace/notes/step3_stable_integral_obstruction_principle.md`: stable-gap bound derivation.
- `workspace/codex_loop/work/lean_metric_scaling_step86/`: machine-checked Lean artifact for scaling/normalization.
- `workspace/data/step90_chernweil_neutrality_verification.json`: ALE non-decrease, BCG inaccessibility, triple disjointness.
- `workspace/notes/step90_chernweil_neutrality_and_triple_disjointness.md`: comprehensive Step 90 analysis.
- `workspace/data/step89_involution_resolution_audit.json`: hyperbolic A₁ orbifold local-type and Euler bookkeeping.
- `workspace/data/step91_scalar_excess_bbcg_gap.json`: scalar-excess diffuseness, BBCG non-uniform-gap.
- `workspace/data/step92_ozuch_spectral_crossverification.json`: superseded Step 92 toy Ozuch channel decomposition and A01 absorption; see Step 93 correction before using its interpretation.
- `workspace/notes/step92_ozuch_spectral_connection_and_transversality.md`: Ozuch–spectral connection patched by Step 93; the corrected target is the $\omega^\perp$ kernel-plane response, not an $e_1$ critical-scale scalar.
- `workspace/notes/step99_a01_trace_obstruction_audit.md`: A02 audit of A01 Step98 same-chirality vanishing, cross-chirality trace coefficients, balanced-row split, and Lean algebra certificate.
- `workspace/data/step99_a01_trace_obstruction_audit.json`: parsed A01 data audit and pattern formulas.
- `workspace/data/step99_selected_spectral_recompute.json`: independent selected rerun from A01 scripts matching stored AB/tensor data.
- `workspace/proofs/Step99RealLinearPQ.lean` and `workspace/proofs/Step99RealLinearPQ.check.json`: Lean-checked finite-dimensional determinant/kernel algebra for \(z\mapsto Pz+Q\bar z\); not a curvature/gluing formalization.
- Cumulative source: `Skills/qiushi-yau26/references/research/20260912.tex`.
- `Sessions/S0910A03/workspace/notes/step88_source_note_twist.md`: peer A03 Liu-source twist formula note; exact twist killed by exact OT ends, approximate/asymptotic twist open.
- `workspace/data/step94_gate1_and_highdim.json`: Gate 1 local second-obstruction vanishing and high-dimensional structural theorem.
- `workspace/data/step96_corrected_selection_determinantal.json`: corrected node-dependent sigma and the now-superseded determinantal response framework; use with Step99 corrections.
- `workspace/notes/step94_three_gates_and_highdim_theorem.md`: Step 94–99 corrected Gate structure and high-dimensional theorem.
- `workspace/notes/step96_corrected_selection_and_determinantal.md`: Step96 note overwritten with Step99 trace-channel corrections.
- `workspace/notes/step99_a01_trace_obstruction_audit.md`: A02 audit of A01 Step98 same-chirality vanishing, cross-chirality trace coefficients, and balanced-row split.
- `workspace/data/step99_a01_trace_obstruction_audit.json`: parsed A01 data audit and pattern formulas.
- `workspace/data/step99_selected_spectral_recompute.json`: independent selected rerun from A01 scripts matching stored AB/tensor data.
- Cumulative source: `Skills/qiushi-yau26/references/research/20260912.tex`.

---

## 13. What has NOT been established

1. No Einstein existence or nonexistence theorem on any mixed row (positive or negative mirror).
2. No positive-Einstein rigidity theorem beyond Gursky–LeBrun on $\chi = 8$ manifolds.
3. No compact generic-$SO(4)$-holonomy Ricci-flat metric (existence or nonexistence, in any dimension).
4. No negative-Einstein obstruction compatible with the *simply connected* PSC/SW-void mixed rows.
5. No tight negative pinching on any all-sign-no-Einstein manifold. The entropy route for orbifold+ALE resolutions is closed by Chern–Weil neutrality and BCG (§8a, Theorems 8a.4–8a.5). Scalar-excess diffuseness (Step 91): $\operatorname{Vol}\{s > -12\} \ge 4\pi^2/\delta$, so the topology change cannot be localized. BBCG gives no dimension-only uniform gap (diameter-dependent, see BBCG Thm 1.3/1.6). A03's OT resolvent barrier now applies to complete free-$T^2$ OT cylinders with two exact outward-expanding ends even without reflection, giving $\delta^* \approx 0.246249763690668$ under those hypotheses; it still does not apply to $S^3$-neck $N \# N$ or diffuse non-OT connectors. Liu's mixed Ricci formulas kill exact twist when exact OT ends force conserved $\alpha=0$, but approximate/asymptotic twist requires new weighted control. The remaining negative-refutation mechanism is a *diffuse*, non-OT, non-warped connector through $N \# N$ spreading $16\pi^2$ scalar excess over volume $\gtrsim 1/\delta$.
6. No certified no-Einstein closed $n$-manifold for $n \ge 5$ found in the current search. **This is not just search status**: all known negative-Einstein obstruction mechanisms (Hitchin–Thorpe, SW/BF, Sambusetti–BCG entropy) require 4D-specific tools (Einstein CGB identity or self-dual splitting). No analogous mechanism exists for $n \ge 5$. A refutation there requires inventing one.
7. No faithful Lean formalization of curvature beyond the packaged `GeometryFor` interface (Step 86 Codex artifact).
8. The triple disjointness theorem (PSC/Weitzenböck, IMT adjunction, Chern–Weil/BCG) is established as the structural explanation for the current impasse, but it is a characterization of the known landscape, not a resolution of Yau–26.
