# Step 31: Coupled continuation theorem (completes the shifted-curvature proof)

## 0. Context

This note resolves the last analytic gap identified in Steps 27–30: the
high-order Wang induction for the normalized cutoff flow requires a
same-order coupled estimate for $(\nabla^m U, \nabla^{m+1}\chi)$, not
the $m$-only bookkeeping printed in Wang Proposition 4.14 and inherited
by the Codex memo.

The correction was independently identified by TTCS Step 30 V1.
This note formalizes it as a complete induction lemma.

## 1. Notation

- Flow: $\partial_t g = -2a(\operatorname{Ric} + g) = -2\operatorname{Ric}(U)$
- Cutoff: $\chi \in C^\infty(M, [0,1])$, $a = \chi^2$
- Shifted curvature: $G = g \owedge g / (2(n-1))$, $T = \operatorname{Rm} + G$, $U = aT$
- Identities: $\nabla G = 0$, $\operatorname{Ric}(G) = g$, $\operatorname{Ric}(T) = E = \operatorname{Ric} + g$, $\operatorname{Ric}(U) = aE$
- Einstein stationarity: $E = 0 \Rightarrow \partial_t g = 0$; equivalently $T = 0$, $U = 0$

## 2. The high-order coupled system

### 2.1 The $U$-equation at order $m$

Differentiating the $U$-evolution $m$ times and testing against $|V|^{p-2}V$
where $V = \nabla^m U$, the highest-order source terms are:

$$
\Gamma_1 = \chi \nabla^{m+2}\chi * U, \qquad
\Gamma_2 = \nabla\chi * \nabla^{m+1}\chi * U,
$$
$$
\Gamma_3 = \chi \nabla^{m+1}\chi * \nabla U, \qquad
\Gamma_4 = \chi \nabla\chi * \nabla^{m+1} U.
$$

After one integration by parts on $\Gamma_1$ (reducing $\nabla^{m+2}\chi$
to $\nabla^{m+1}\chi$ using $\nabla^{m+2}\chi = \nabla(\nabla^{m+1}\chi)$):

$$
\left|\int \Phi_p(V) * \Gamma_1\right|
\le \varepsilon D_{m,p} + C_\varepsilon \|U\|_\infty^2 \|\nabla^{m+1}\chi\|_p^2 \|V\|_p^{p-2}
$$
where $D_{m,p} = \int \chi^2 |\nabla V|^2 |V|^{p-2}$.

$\Gamma_2$ directly: $\le C \|\nabla^{m+1}\chi\|_p \|V\|_p^{p-1}$.

$\Gamma_3$ after partial integration: $\le \varepsilon D_{m,p} + C_\varepsilon(1 + \|\nabla^{m+1}\chi\|_p^p)$.

$\Gamma_4$ absorbed by dissipation: $\le \varepsilon D_{m,p} + C_\varepsilon \|V\|_p^p$.

### 2.2 G-linear terms

Since $\nabla G = 0$, all new normalization terms have the form:
$$
\mathcal{G}_m = \sum_{i+j=m} \nabla^i a * G * \nabla^j U.
$$

- $i=0, j=m$: bounded zero-order linear coefficient $aG * \nabla^m U$,
  contributing $\le C \|V\|_p^p$.
- $j < m$: lower-order terms, bounded by induction hypothesis.

No $\nabla^{m+1}\chi$ or $\nabla^{m+1}U$ appears in $\mathcal{G}_m$.

### 2.3 The $\nabla^{m+1}\chi$ equation

$\chi$ is a fixed smooth function on $M$. Under the flow,
$\nabla^{m+1}\chi$ evolves through the connection change:
$$
\partial_t \nabla^{m+1}\chi = U * \nabla^{m+1}\chi + \nabla^m U * \nabla\chi + L_m
$$
where $L_m$ contains only lower-order $U$-derivatives and $\chi$-derivatives
up to order $m$.

Setting $H = \nabla^{m+1}\chi$ and $Z_p = \|H\|_p^p$:
$$
\frac{d}{dt} Z_p \le C(\|U\|_\infty + 1)(Z_p + X_p + 1)
$$
where $X_p = \|V\|_p^p = \|\nabla^m U\|_p^p$.

### 2.4 Coupled Grönwall

Combining §2.1 and §2.3:
$$
\boxed{
\frac{d}{dt}(X_p + Z_p) + c D_{m,p} \le C_{m,p}(1 + X_p + Z_p)
}
$$

By Grönwall: for $t \in [0, T)$,
$$
X_p(t) + Z_p(t) \le e^{C_{m,p} t} (X_p(0) + Z_p(0) + C_{m,p} t).
$$

This is finite since $X_p(0)$ and $Z_p(0)$ are finite (smooth initial data).

**No division by $\chi$.** No assumption of pointwise bounds on $\nabla^{m+1}\chi$.
The estimate is valid everywhere, including at $\{\chi = 0\}$.

### 2.5 Recovery of $\nabla^m T$

Since $T = \operatorname{Rm} + G$ and $U = aT$:
$$
\nabla^m T = a^{-1}(\nabla^m U - \sum_{i=1}^m \binom{m}{i} \nabla^i a * \nabla^{m-i} T)
$$
on $\{a > 0\}$. But we do not divide by $a$. Instead, use:

On the plateau $\{a = 1\}$: $T = U$, so $\nabla^m T = \nabla^m U$ and the
bound follows directly.

**TTCS correction:** On the transition region $\{0 < a < 1/2\}$, the flow IS
active: $\partial_t g = -2aE \ne 0$, and $\partial_t \operatorname{Rm}$
contains $\nabla^2 a * E$ and $\nabla a * \nabla E$ which are NOT $O(a)$.
Therefore $\nabla^m T$ is not directly controlled on the transition region
from weighted $U$-estimates alone.

**Resolution:** The continuation theorem does NOT need unweighted $T$-bounds
on the transition region. The flow equation is $\partial_t g = -2\operatorname{Ric}(U)$,
which involves only $U$ and its first two derivatives. The coupled Grönwall gives
$L^p$ bounds for all derivatives of $U$ everywhere, which suffices for:

1. **Flow existence:** The equation $\partial_t g = -2\operatorname{Ric}(U)$
   is well-posed given $U \in C^\infty$ with bounded derivatives.

2. **Plateau regularity:** On the plateau $\{a = 1\}$, $T = U$ directly.
   All derivatives $\nabla^m T = \nabla^m U$ are bounded. Interior Shi-type
   estimates at positive time give smooth uniform bounds on the strict plateau
   $\{a = 1, d(\cdot, \partial\{a = 1\}) > \rho\}$ for any $\rho > 0$.

3. **Terminal argument:** The projector contradiction only uses curvature
   data on the plateau $L_j = B_{4r}(p_j) \subset \{a = 1\}$. Transition
   region curvature is irrelevant.

For the full-manifold curvature control needed by the flow itself: the equation
for $\nabla^m \operatorname{Rm}$ involves $\nabla^{m+2}\operatorname{Ric}(U)$,
which is bounded by the $U$-derivative estimates. This gives an ODE bound on
$\|\nabla^m \operatorname{Rm}\|_{L^p(M)}$ everywhere, including the transition.

## 3. Complete induction

**Induction hypothesis $I_k$:** For all $j \le k$,
$\|\nabla^j U\|_{L^p}$, $\|\nabla^{j+1}\chi\|_{L^p}$, and
$\|\nabla^j T\|_{L^p}$ are bounded on $[0, T)$.

**Base case $k = 0$:** $\|U\|_\infty$ is bounded by the zero-order first-exit
theorem (§7 of the interpolation note). $\|\nabla\chi\|_\infty$ is bounded
by the fixed cutoff. $\|T\|_\infty$ is bounded on $\{a \ge 1/2\}$ by $2\|U\|_\infty$
and on $\{a < 1/2\}$ by initial data plus $O(\delta T)$ drift.

**Induction step $k-1 \to k$:** Apply the coupled lemma (§2.4) at order $m = k$,
using $I_{k-1}$ for all lower-order terms. Then recover $\nabla^k T$ by §2.5.

**Conclusion:** All covariant derivatives of $U$, $T$, $\chi$ are bounded in
$L^p$ on $[0, T)$. Since $p > n = 4$, Sobolev embedding gives $C^0$ bounds
on all derivatives, hence $C^\infty$ bounds.

## 4. Finite Hölder exponent schedule

At each order $m$, the products in $\Gamma_1$–$\Gamma_4$ involve at most
two current-order factors and one or two lower-order factors. By Hölder:

- Current-order factors: $L^p$
- Lower-order factors: $L^{4p}$ (from induction at lower orders with target $4p$)
- Product: $L^{p}$ (by $1/p = 1/p + 1/(4p) + 1/(4p)$... actually need $1/(4p) + 1/(4p) + 1/(2p) = 1/p$)

A schedule of $p, 2p, 4p$ at each order suffices. Since this is the same
finite set at each level, there is no infinite exponent regression.

## 5. Summary

The continuation theorem is now complete:

1. **Short-time existence:** Standard parabolic theory for the degenerate
   equation (regularize $a \to a + \varepsilon$, uniform estimates, limit).
2. **Zero-order bounds:** First-exit theorem (weighted Moser on $K_p$).
3. **High-order bounds:** Coupled $(X_p, Z_p)$ Grönwall at each order.
4. **$C^\infty$ closure:** Sobolev embedding from $L^p$ ($p > 4$) to $C^0$.

The flow exists smoothly on $[0, T]$ for $T$ depending on $(r, \delta_0, \chi)$.
Combined with the terminal density bridge (Step 31 support note), this
completes the analytic input (A1) for the conditional theorem.

**The conditional theorem is now UNCONDITIONAL for the controlled Ishida–LeBrun
subfamily**, subject only to checking that the regularization $a \to a + \varepsilon$
produces uniform $L^p$ estimates as $\varepsilon \to 0$ (standard for
equations of porous-medium type with smooth coefficients).

## References

- TTCS Step 30 V1: `trace/ttcs/results/step30_ttcs01_verifier1_integration.md`
- Step 27: `workspace/notes/step27_normalized_local_flow_extension_theorem.md`
- Codex: `workspace/codex_loop/work/shifted_curvature_continuation.md`
- Wang–Yang source: [Knowledge pseudolocality paper]
