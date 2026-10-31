# Step 31: Corrected macro-support construction and terminal density

## 1. Macro-support selection

### 1.1 Good-center definition

Let $(M^4, g_i)$ be a sequence with $\operatorname{Ric}_{g_i} \ge -\kappa g_i$
($\kappa$ uniformly bounded). Fix a scale $r > 0$ small enough that all balls
up to radius $30r$ have controlled doubling ($C_D = C_D(4, \kappa r^2)$).

Define the truncated centered maximal function:
$$
\mathcal{M}_r(F^2)(x) = \sup_{0 < s \le 6r} \fint_{B_s(x)} F^2 \, d\mu,
\qquad F = (1 + |\operatorname{Rm}|^2)^{1/2}.
$$

The good set at threshold $\Lambda$:
$$
G = \{x \in M : \mathcal{M}_r(F^2)(x) \le \Lambda \bar K\},
\qquad \bar K = \fint_M F^2.
$$

**Choice of $\Lambda$:** Take $\Lambda = 2 C_M(4, \kappa r^2)$ where $C_M$ is
the weak-$(1,1)$ constant of the centered maximal function on $(M, g)$.
The Vitali covering theorem gives $C_M \le C(n) \cdot C_D^{O(1)}$.

By the weak-$(1,1)$ maximal inequality:
$$
\operatorname{Vol}(M \setminus G)
\le \frac{C_M}{\Lambda \bar K} \int_M F^2
= \frac{C_M}{\Lambda} \cdot \operatorname{Vol}(M)
= \frac{1}{2} \operatorname{Vol}(M).
$$

Therefore $\operatorname{Vol}(G) \ge \frac{1}{2} \operatorname{Vol}(M)$.

### 1.2 Maximal r-separated net in G

Select a maximal $r$-separated subset $\{p_\alpha\}_{\alpha \in \mathcal{A}}
\subset G$: for all $\alpha \ne \beta$, $d(p_\alpha, p_\beta) \ge r$,
and every point of $G$ is within $r$ of some $p_\alpha$.

Then $\{B_r(p_\alpha)\}$ covers $G$.

### 1.3 Bounded-degree graph and coloring

Form the graph $\Gamma$: vertices $\mathcal{A}$, edges $\alpha \sim \beta$
iff $d(p_\alpha, p_\beta) \le 12r$. The maximum degree is bounded by the
packing number:
$$
\deg(\alpha) \le N_{\text{pack}}(B_{13r}(p_\alpha), r/2)
\le C(4, \kappa r^2) =: N.
$$

By greedy coloring, $\Gamma$ is $(N+1)$-colorable. For each color class
$\mathcal{C}_c$, define the weight:
$$
w_c = \sum_{\alpha \in \mathcal{C}_c} \operatorname{Vol}(B_r(p_\alpha)).
$$

Select the color $c^*$ maximizing $w_c$. Then:
$$
\sum_{\alpha \in \mathcal{C}_{c^*}} \operatorname{Vol}(B_r(p_\alpha))
\ge \frac{1}{N+1} \sum_\alpha \operatorname{Vol}(B_r(p_\alpha))
\ge \frac{\operatorname{Vol}(G)}{N+1}
\ge \frac{\operatorname{Vol}(M)}{2(N+1)}.
$$

Relabel the selected centers as $\{p_j\}_{j=1}^J$. By construction,
$d(p_j, p_k) > 12r$ for $j \ne k$, so $B_{6r}(p_j)$ are pairwise
disjoint.

### 1.4 Nested support structure

For each $j$, define:

| Region | Definition | Role |
|--------|-----------|------|
| $P_j = B_r(p_j)$ | Strict plateau center | Chart selection domain |
| $L_j = B_{4r}(p_j)$ | Larger plateau | Contains all chart geodesics from $P_j$ |
| $\operatorname{supp} \chi_j \subset B_{5r}(p_j)$ | Cutoff support | Flow-active region |
| $U_j = B_{6r}(p_j)$ | Auxiliary domain | Sobolev inequality domain |

The cutoff $\chi_j \in C^\infty(M, [0,1])$ satisfies:
- $\chi_j = 1$ on $B_{4r}(p_j)$
- $\operatorname{supp} \chi_j \subset B_{5r}(p_j)$
- $|\nabla \chi_j| \le C/r$

The common cutoff:
$$
a = \sum_j \chi_j^2.
$$
Since $U_j$ are disjoint, on each $U_j$ we have $a = \chi_j^2$.

### 1.5 Retained volume

$$
\operatorname{Vol}_{\text{retained}} = \sum_j \operatorname{Vol}(P_j)
\ge \frac{\operatorname{Vol}(M)}{2(N+1)}
=: \alpha \cdot \operatorname{Vol}(M),
$$
where $\alpha = 1/(2(N+1)) > 0$ depends only on $(4, \kappa r^2)$.

### 1.6 Good-center energy control on $U_j$

Since $p_j \in G$ and $6r$ is the maximal function scale:
$$
\fint_{B_{6r}(p_j)} F^2 \le \Lambda \bar K.
$$

Therefore:
$$
\hat H_{2,j} := \int_{U_j} F^2 \le \Lambda \bar K \cdot \operatorname{Vol}(U_j),
$$
and the critical coupling:
$$
\gamma_j = S_j \hat H_{2,j}^{1/2}
= C r^2 \operatorname{Vol}(U_j)^{-1/2} \cdot (\Lambda \bar K \operatorname{Vol}(U_j))^{1/2}
= C r^2 (\Lambda \bar K)^{1/2}
$$
is independent of $\operatorname{Vol}(U_j)$ and hence of collapse.

## 2. Terminal density bridge (corrected for varying families)

### 2.1 Setup

Consider a sequence $(M_i, g_i)$ in the controlled Ishida–LeBrun family
with $\sigma_i/A_i \to 0$ and
$\delta_i = \|g_i^{-1}(\operatorname{Ric}_{g_i} + g_i)\|_\infty \to 0$.

After running the cutoff flow to terminal time $T$, we obtain $g_i(T)$ with:
- Global defect: $Q_i(T) = \int |E_i(T)|^2 \le e^{C\theta} Q_i(0) \le C \delta_i^2 \operatorname{Vol}_i$
- Bounded curvature on plateaux: $|a \operatorname{Rm}| \le C\beta_j/T$ on $\operatorname{supp} \chi_j$
- Defect rate: $|aE_i| \le C \delta_i (r^2/T)^{1/3}$
- Metric comparison: $g_i(T)$ is $C\delta_i$-bilipschitz to $g_i(0)$ on $\operatorname{supp} a$

### 2.2 Combined terminal density

Define the combined density on $g_i(T)$:
$$
\mathfrak{D}_i = |E_i|^2 + (s_i + 4)^2 + (s_i + 8\sqrt{6}|W_i^+|)^2 + \mathfrak{G}_i
$$
where $\mathfrak{G}_i$ is the gap density from the monopole argument
(eigenline error + harmonic amplitude error).

**Global terms** (controlled everywhere):
$$
\int_M |E_i|^2 \le C Q_i, \qquad
\int_M (s_i + 4)^2 \le 4 Q_i, \qquad
\int_M (s_i + 8\sqrt{6}|W_i^+|)^2 \le 864\pi^2 R_i \le C Q_i.
$$

**Eigenline term** (controlled only on bounded-curvature plateau $L$):
The eigenline density from the Step 16 positive-part monopole construction
is defined only where curvature is bounded. Set:
$$
\mathfrak{G}_i^{\text{loc}} = \mathfrak{G}_i \cdot \mathbf{1}_{L_i},
$$
extended by zero outside the plateaux $L_i = \bigcup_j L_j$.

The positive-part construction with $q^+ = (\sqrt{6}|W^+| - s)^+$ and
regularization parameter $\varepsilon_i = Q_i / \operatorname{Vol}_i$
gives:
$$
\int_{L_i} \mathfrak{G}_i \le C(Q_i + \varepsilon_i^2 \operatorname{Vol}_i)
= C(Q_i + Q_i^2/\operatorname{Vol}_i) \le C' Q_i
$$
since $Q_i \le \delta_i^2 \operatorname{Vol}_i$ and $\delta_i \le 1$.

### 2.3 Combined bound

$$
\int_M \mathfrak{D}_i^{\text{loc}} \le C Q_i,
$$
where $\mathfrak{D}_i^{\text{loc}} = |E_i|^2 + (s_i + 4)^2
+ (s_i + 8\sqrt{6}|W_i^+|)^2 + \mathfrak{G}_i^{\text{loc}}$.

### 2.4 Normalization per topology

In the controlled family with $\chi(M_i)/A_i \le \Lambda$:

(**TTCS correction:** use CGB volume UPPER bound, not lower bound.)
At small defect $\delta$, CGB gives $8\pi^2\chi(M) = \int(|W|^2 - |z|^2/2 + s^2/24)$.
Since $\int(s+4)^2 \le 4Q$, $\int|z|^2 \le Q$, and $Q = o(\operatorname{Vol})$:
$$
\int s^2 \ge c \operatorname{Vol} \quad\text{(from } s \approx -4\text{)}.
$$
Combined with $8\pi^2\chi \ge \int s^2/24 - C Q$:
$$
\operatorname{Vol}_i \le C \chi(M_i) \le C \Lambda A_i.
$$

Therefore:
$$
Q_i \le C \delta_i^2 \operatorname{Vol}_i \le C \Lambda \delta_i^2 A_i,
$$
$$
\frac{Q_i}{A_i} \le C \Lambda \delta_i^2 \to 0.
$$

### 2.5 Exponential-pullback chart selection

On each strict plateau center $p \in P_j$ with $|a\operatorname{Rm}| \le K$
on $L_j = B_{4r}(p_j) \supset P_j$, the exponential map $\exp_p$
restricted to $B_{2r}(0) \subset T_pM$ (**TTCS correction:** use $2r$ not
$3r$ to ensure $\exp_p(B_{2r}) \subset B_{3r}(p) \subset L_j$ even after
bilipschitz drift) satisfies Rauch comparison:
(1 - C\sqrt{K} r) g_{\text{flat}} \le \exp_p^* g \le (1 + C\sqrt{K} r) g_{\text{flat}}.
$$

Since $|a \operatorname{Rm}| \le K$ on $L_j$ and $\exp_p(B_{3r}(0)) \subset L_j$
(all chart geodesics stay in the plateau), the pullback chart is noncollapsed
even if the base manifold is collapsed.

Define the averaged density (over reduced chart radius $2r$):
$$
\bar{\mathfrak{D}}_i(p) = \fint_{B_{r}(0)} (\mathfrak{D}_i^{\text{loc}} \circ \exp_p)
\, d\text{vol}_{\exp_p^*g}.
$$

By Rauch comparison and Liouville invariance:
$$
\int_{P_j} \bar{\mathfrak{D}}_i \, d\mu
\le C(K, r) \int_{L_j} \mathfrak{D}_i^{\text{loc}} \, d\mu.
$$

Summing over $j$ and using retained volume:
$$
\alpha \operatorname{Vol}_i \cdot \min_p \bar{\mathfrak{D}}_i(p)
\le \sum_j \int_{P_j} \bar{\mathfrak{D}}_i \, d\mu
\le C \int_M \mathfrak{D}_i^{\text{loc}}
\le C Q_i.
$$

Therefore there exists $p_i \in \bigcup_j P_j$ with:
$$
\bar{\mathfrak{D}}_i(p_i) \le \frac{C Q_i}{\alpha \operatorname{Vol}_i}
\le C \delta_i^2 \to 0.
$$

### 2.6 Smooth convergence to forbidden Einstein germ

The pullback $\exp_{p_i}^* g_i(T)$ on $B_r(0) \subset \mathbb{R}^4$
has bounded curvature and noncollapsed volume. By Cheeger–Gromov compactness,
a subsequence converges smoothly to a limit metric $g_\infty$ on $B_{r/2}(0)$.

Since $\bar{\mathfrak{D}}_i(p_i) \to 0$:
- $E_\infty = 0$: $\operatorname{Ric}_{g_\infty} = -g_\infty$ (Einstein)
- $s_\infty = -4$ and $|W_\infty^+| = 1/(2\sqrt{6})$ (calibrated spectrum)
- $\mathfrak{G}_\infty = 0$: eigenline saturation

The limit satisfies $\operatorname{Spec}(W_\infty^+) = (-1/6, 1/12, 1/12)$.
By the projector argument (Step 6), this forces $\nabla W_\infty^+ = 0$.
But the Einstein–Weyl identity gives $|\nabla W_\infty^+|^2 = 1/16 \ne 0$.
**Contradiction.**

## 3. Complete conditional theorem statement

**Theorem (Conditional).** Let $\mathcal{F}_\kappa$ be the subfamily of
Ishida–LeBrun manifolds $M = (\#_{j=1}^m X_j) \# N$ with $m \in \{2,3\}$,
$b_+(N) = 0$, and $\sigma/A \le \kappa$, where
$\sigma = D - A/3 \ge 0$ and $A = \sum c_1^2(X_j)$.

Assume the following analytic input:

**(A1)** The degenerate cutoff flow $\partial_t g = -2a(\operatorname{Ric}+g)$
with $a = \sum \chi_j^2$ on the disjoint macro-supports exists smoothly on
$[0, T]$ for some $T > 0$ depending on $(r, \delta_0)$.

Then there exists $\delta_0 = \delta_0(\kappa) > 0$ such that no
$M \in \mathcal{F}_\kappa$ carries a smooth metric $g$ with
$$
\|g^{-1}(\operatorname{Ric}_g + g)\|_\infty < \delta_0.
$$

**Proof structure:**
1. If $\sigma/A > \eta(\kappa)$, the unconditional above-critical bound gives
   $\delta \ge c\sqrt{\sigma/A}$.
2. If $\sigma/A \le \eta(\kappa)$, construct macro-supports, run the flow,
   apply the first-exit theorem (§7 of the interpolation note),
   and the terminal density bridge above to reach a contradiction.

The threshold $\delta_0$ is universal within $\mathcal{F}_\kappa$:
$\gamma_j = Cr^2\sqrt{\Lambda\bar K}$ is controlled by $\bar K \le C\chi(M)/\operatorname{Vol}$,
and in $\mathcal{F}_\kappa$, $\chi(M)/A \le C(\kappa)$ by Noether
($c_2(X_j) \le 5c_1^2(X_j) + 36$ and
$\chi(N) = A/3 + \sigma + 6 - 4m - 6b_1(N)$). $\square$

## 4. What remains

The only unproved analytic assumption is (A1): short-time smooth existence
of the degenerate flow. This requires the shifted-curvature continuation
theorem with the coupled $(\nabla^m U, \nabla^{m+1}\chi)$ estimate.
All other ingredients—support construction, first-exit, terminal density,
projector contradiction—are complete modulo (A1).
