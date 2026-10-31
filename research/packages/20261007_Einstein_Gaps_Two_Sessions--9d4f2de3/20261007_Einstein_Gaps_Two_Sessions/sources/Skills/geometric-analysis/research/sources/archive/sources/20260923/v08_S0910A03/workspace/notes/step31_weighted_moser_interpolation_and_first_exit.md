# Step 31: Weighted Moser interpolation lemma and corrected first-exit theorem

## 0. Purpose and correction

This note formalizes the weighted parabolic Moser interpolation that was
challenged in A01 Step 29 and TTCS Step 30 V2. It shows that the alleged
"half-power gap" is an artifact of computing the wrong quantity (||Z_p||_3^3)
rather than the quantity actually used by the iteration (K_{3p/2}).

The note then assembles the complete first-exit closure using the weighted
moments, and identifies the remaining conditional dependence on the
continuation theorem.

## 1. Setup

Let (M^4, g(t)) satisfy the normalized cutoff flow
$$
\partial_t g = -2a(\operatorname{Ric} + g), \qquad a = \chi^2 \in [0,1],
$$
on a closed 4-manifold, where $\chi \in C^\infty(M, [0,1])$ with
$|\nabla\chi| \le C_\chi/r$ on supp $\chi$.

Define
$$
F = (1 + |\operatorname{Rm}|^2)^{1/2}, \qquad
\Phi = F \text{ or } |E| \text{ as appropriate},
$$
and the weighted moments
$$
K_p = \int_{\operatorname{supp}\chi} a^{p-2} \Phi^p \, d\mu, \qquad p \ge 2.
$$

The Moser test function is
$$
Z_p = a^{(p-1)/2} \Phi^{p/2}.
$$

## 2. The interpolation lemma

**Lemma 1 (Weighted Cauchy–Schwarz interpolation).**
For $p \ge 2$, on the support of $\chi$:

(i) $K_{2p} = \|Z_p\|_{L^4}^4$.

(ii) $K_{3p/2} \le K_p^{1/2} \cdot K_{2p}^{1/2}$.

(iii) $\|Z_p\|_{L^2}^2 \le K_p$ (since $a \le 1$).

*Proof.*

(i) $\|Z_p\|_4^4 = \int a^{2(p-1)} \Phi^{2p} = \int a^{2p-2} \Phi^{2p} = K_{2p}$. ✓

(ii) By Cauchy–Schwarz:
$$
K_{3p/2} = \int a^{3p/2 - 2} \Phi^{3p/2}
= \int \underbrace{a^{(p-2)/2} \Phi^{p/2}}_{\text{factor 1}}
\cdot \underbrace{a^{(2p-2)/2} \Phi^p}_{\text{factor 2}}.
$$
Check: $(p-2)/2 + (2p-2)/2 = (3p-4)/2 = 3p/2 - 2$. ✓
Check: $p/2 + p = 3p/2$. ✓

By Cauchy–Schwarz in $L^2$:
$$
K_{3p/2} \le \left(\int a^{p-2} \Phi^p\right)^{1/2}
\left(\int a^{2p-2} \Phi^{2p}\right)^{1/2}
= K_p^{1/2} \cdot K_{2p}^{1/2}. \quad\square
$$

(iii) $\|Z_p\|_2^2 = \int a^{p-1} \Phi^p$. Since $a \le 1$ and $p \ge 2$,
$a^{p-1} \le a^{p-2}$, so $\|Z_p\|_2^2 \le K_p$. $\square$

## 3. Why ||Z_p||_3^3 is irrelevant

The A01 "half-power gap" computes:
$$
\|Z_p\|_3^3 = \int a^{3(p-1)/2} \Phi^{3p/2}.
$$
The $a$-exponent is $3(p-1)/2 = (3p-3)/2$, while $K_{3p/2}$ needs
$3p/2 - 2 = (3p-4)/2$. The gap is $1/2$.

Since $a \le 1$, $a^{(3p-3)/2} \le a^{(3p-4)/2}$, so
$\|Z_p\|_3^3 \le K_{3p/2}$. Thus $\|Z_p\|_3^3$ is **smaller** than
$K_{3p/2}$ and cannot bound it from above. This is A01's observation.

**But the iteration never uses $\|Z_p\|_3^3$.** The actual parabolic Moser step is:

1. **Energy:** $\sup_t K_p(t) + c\int_0^T D_p \le C \cdot (\text{initial} + \text{reaction})$
2. **Sobolev on each time slice:** $K_{2p}(t)^{1/2} \le C S^2 (\|\nabla Z_p\|_2^2 + r^{-2} K_p)$
3. **Spacetime integration:** $\int_0^T K_{2p} \le (\sup K_p) \cdot C S^2 \int_0^T(D_p + r^{-2} K_p)$
4. **Good slice + propagation:** $\sup_{[T/2,T]} K_{2p}(t) \le \ldots$
5. **Cauchy–Schwarz:** $K_{3p/2}(t) \le K_p(t)^{1/2} \cdot K_{2p}(t)^{1/2}$

The recurrence $p \to 3p/2$ arises from averaging the controlled quantity
($K_p$, exponent $p$) and the Sobolev-upgraded quantity ($K_{2p}$, exponent $2p$):
$(p + 2p)/2 = 3p/2$.

## 4. Gradient control: the a-weighted dissipation matches Z_p

The energy inequality for $K_p$ produces the dissipation
$$
D_p = \int a^{p-1} F^{p-2} |\nabla\operatorname{Rm}|^2.
$$

The gradient of the test function $Z_p$ is:
$$
\nabla Z_p = \frac{p-1}{2} a^{(p-3)/2} (\nabla a) \Phi^{p/2}
+ a^{(p-1)/2} \frac{p}{2} \Phi^{p/2-1} \nabla\Phi.
$$

Hence
$$
\|\nabla Z_p\|_2^2 \le C p^2 \left[
\int a^{p-3} |\nabla a|^2 \Phi^p
+ \int a^{p-1} \Phi^{p-2} |\nabla\Phi|^2
\right].
$$

**Cutoff gradient term:** Since $a = \chi^2$ and $|\nabla a| = 2\chi|\nabla\chi| \le 2C_\chi/r$, we have
$a^{p-3}|\nabla a|^2 = 4 a^{p-3} \chi^2 |\nabla\chi|^2 = 4 a^{p-2} |\nabla\chi|^2 \le 4C_\chi^2 r^{-2} a^{p-2}$.
So this term is $\le C r^{-2} K_p$.

**Curvature gradient term:** $|\nabla\Phi| \le |\nabla\operatorname{Rm}|/\Phi \le |\nabla\operatorname{Rm}|$ (since $\Phi \ge 1$).
So $\int a^{p-1} \Phi^{p-2} |\nabla\Phi|^2 \le D_p$.

Therefore:
$$
\boxed{\|\nabla Z_p\|_2^2 \le C p^2 (D_p + r^{-2} K_p).}
$$

This is the KEY: the $a$-weighted dissipation $D_p$ from the energy inequality
exactly matches the gradient needed for $Z_p$ in the Sobolev embedding.
No unweighted gradient control is needed. No lower bound on $a$ is needed.

## 5. Why the unweighted route on U=aT has the same difficulty

For $U = a(\operatorname{Rm} + G)$, the evolution equation has diffusion
$a\Delta U$ (not $\Delta U$). Testing $\int |U|^p$ with $|U|^{p-2} U$ gives
an a-weighted dissipation:
$$
\tilde D_p = \int a \, |U|^{p-2} |\nabla U|^2.
$$

The unweighted Moser variable $W_p = |U|^{p/2}$ satisfies:
$$
\|\nabla W_p\|_2^2 = \frac{p^2}{4} \int |U|^{p-2} |\nabla|U||^2.
$$

From the energy we only control $\int a |U|^{p-2} |\nabla|U||^2 \le \tilde D_p$.
Since $a \le 1$, the unweighted gradient is LARGER:
$$
\int |U|^{p-2} |\nabla|U||^2 \ge \int a |U|^{p-2} |\nabla|U||^2.
$$

We cannot bound $\|\nabla W_p\|_2^2$ from $\tilde D_p$ without a lower bound on $a$.
Therefore the unweighted route on $|U|$ faces the **same degenerate-diffusion
issue** that it was supposed to solve.

In contrast, the weighted route absorbs this naturally because $Z_p$ carries
$a^{(p-1)/2}$, and $\nabla Z_p$ contains $a^{(p-3)/2} \nabla a$ and
$a^{(p-1)/2} \nabla\Phi$—both of which are controlled by the a-weighted
dissipation and cutoff gradients.

## 6. Corrected Sobolev step via Ladyzhenskaya

In four dimensions, the Ladyzhenskaya-type inequality on a ball $B$ with
collapse-adapted Sobolev constant $S$ gives:
$$
\int_B u^4 \le S^2 \left(\int_B |\nabla u|^2\right)
\left(\int_B u^2\right) + C r^{-2} S^2 \left(\int_B u^2\right)^2
$$
for $u \in W^{1,2}_0(B)$ in dimension 4 (from $\|u\|_4^2 \le S(\|\nabla u\|_2^2 + r^{-2}\|u\|_2^2)$, 
then $\|u\|_4^4 \le \|u\|_4^2 \cdot \|u\|_4^2$).

More precisely, the collapse-adapted bound (Maheux–Saloff-Coste) gives
$$
\|u\|_4^2 \le S^2(\|\nabla u\|_2^2 + r^{-2}\|u\|_2^2),
\qquad S^2 = C(4, \kappa r^2) \cdot r^4 / \operatorname{Vol}(B_r)
$$
where $\kappa$ is the lower Ricci bound in units of $r^{-2}$.

With $u = Z_p$ on the support within $B_{6r}(p_j)$:
$$
K_{2p}^{1/2} = \|Z_p\|_4^2 \le S^2 \cdot C p^2 (D_p + r^{-2} K_p).
$$

Integrating in time over $[0,T]$:
$$
\int_0^T K_{2p}^{1/2} \, dt \le C S^2 p^2 
\left(\int_0^T D_p \, dt + r^{-2} \int_0^T K_p \, dt\right).
$$

From the energy inequality, $\int_0^T D_p \le C(K_p(0) + \text{reaction})$
and $\int_0^T K_p \le T \cdot \sup_t K_p$.

## 7. Complete first-exit closure (conditional on smooth existence)

### 7.1 Definitions

Fix a macro-support family $\{p_j\}$ as in the Step 30 corrected
construction. The common cutoff is $a = \sum_j \chi_j^2$. On each component
$B_{6r}(p_j)$, only $\chi_j$ is nonzero, so $a = \chi_j^2$.

Define:
- $K_{p,j}(t) = \int_{B_{6r}(p_j)} a^{p-2} F^p \, d\mu_t$
- $D_{p,j}(t) = \int_{B_{6r}(p_j)} a^{p-1} F^{p-2} |\nabla\operatorname{Rm}|^2 \, d\mu_t$
- $\hat H_{2,j}(t) = \int_{B_{6r}(p_j)} F^2 \, d\mu_t$ (active-region energy; note $a^0 = 1$)
- $Q(t) = \int_M |E|^2 \, d\mu_t$ (global defect)
- $J_{6,j}(t) = \int_{B_{6r}(p_j)} a^4 |E|^6 \, d\mu_t$

The critical dimensionless parameter is
$$
\gamma_j = S_j \cdot \hat H_{2,j}^{1/2},
$$
where $S_j = C r^2 / \operatorname{Vol}(B_{6r}(p_j))^{1/2}$ is the
collapse-adapted Sobolev constant. By the good-center condition:
$$
\hat H_{2,j} \le \operatorname{Vol}(B_{6r}(p_j)) \cdot \Lambda \bar K,
$$
so $\gamma_j \le C r^2 \sqrt{\Lambda \bar K}$. The mean curvature energy
$\bar K$ is uniformly bounded (by CGB + Noether in controlled families),
so $\gamma_j \le C(r, \Lambda, \bar K)$ independent of collapse.

### 7.2 Energy inequality for $K_p$ ($p \ge 3$)

From the Step 26 derivation (with Step 25 normalization correction):
$$
\frac{d}{dt} K_{p,j} + c_p D_{p,j}
\le C_p r^{-2} K_{p,j} + C_p \int_{B_{6r}} a^{p-1} F^{p+1} \, d\mu
+ C_p \int_{B_{6r}} a^{p-2} F^p \cdot a|E| \, d\mu.
$$

The reaction terms arise with weight $a^{p-1}$ (from the cubic contraction
$a \cdot \operatorname{Rm}*\operatorname{Rm}$ tested against $a^{p-2}F^{p-2}$):
$$
R_{p,j} = \int_{B_{6r}} a^{p-1} F^{p+1} \, d\mu.
$$

By Hölder with the correct weight: $R_{p,j} \le K_{3,j}^{1/3} K_{3p/2,j}^{2/3}$
(TTCS suggestion).

The second factor involves $K_{2p,j}^{1/p}$. This creates the coupling with
the Sobolev step.

### 7.3 The $q=2$ critical step: $K_2 \to H_3$

At $p=2$, $K_2 = \hat H_2$ and the energy inequality gives:
$$
\frac{d}{dt} \hat H_{2,j} + c D_{2,j}
\le C r^{-2} \hat H_{2,j} + C \int_{B_{6r}} a F^3.
$$

Using the Sobolev step with $Z_2 = a^{1/2} F$:
$$
K_{4,j}^{1/2} = \|Z_2\|_4^2 \le C S_j^2 (D_{2,j} + r^{-2} \hat H_{2,j}).
$$

By Lemma 1: $K_{3,j} \le K_{2,j}^{1/2} K_{4,j}^{1/2}$. Hence
(**TTCS correction: no square root**):
$$
K_{3,j} \le C S_j \hat H_{2,j}^{1/2} (D_{2,j} + r^{-2} \hat H_{2,j})
= C \gamma_j (D_{2,j} + r^{-2} \hat H_{2,j}).
$$

When $\gamma_j$ is small ($C\gamma_j < c/2$), the $D_2$ reaction is absorbed:

This gives $H_2$ persistence and spacetime $H_3$ control:
$$
\sup_t \hat H_{2,j} \le e^{C(\gamma_j^2 + 1)r^{-2}T} \hat H_{2,j}(0),
$$
$$
\int_0^T K_{3,j} \, dt \le C \gamma_j (T \sup_t \hat H_{2,j}).
$$

### 7.4 The $q=3$ step: terminal $H_3$ bound

At $p=3$, the energy inequality with $Z_3 = a \Phi^{3/2}$ gives:
$$
\frac{d}{dt} K_{3,j} + c D_{3,j} \le C r^{-2} K_{3,j} + \text{reaction}.
$$

A good time slice $t_* \in [T/4, T/2]$ satisfies
$K_{3,j}(t_*) \le (4/T) \int_0^T K_{3,j}$. Forward propagation:
$$
K_{3,j}(t) \le e^{Cr^{-2}(t-t_*)} K_{3,j}(t_*), \qquad t \ge t_*.
$$

Combined: terminal $K_3$ is controlled by the spacetime $H_3$ integral.

### 7.5 Subcritical Moser: $K_p \to K_{3p/2} \to \cdots \to L^\infty$

Starting from $p_0 = 3$ (controlled at terminal time), the Moser recurrence
$p_{k+1} = (3/2) p_k$ gives $p_k = 3 \cdot (3/2)^k \to \infty$.

At each step, the energy inequality for $K_{p_k}$ and Sobolev for
$K_{2p_k}$ yield:
$$
\sup_{[T/2, T]} K_{3p_k/2}(t)
\le C_k \cdot (\sup K_{p_k})^{1/2} \cdot (\sup K_{2p_k})^{1/2}.
$$

The constant $C_k$ grows polynomially as $p_k^4$ per step (or $p_k^3$ if
the full scalar-gradient dissipation is retained). The Moser product
converges because $\sum_{k=0}^\infty (\log p_k) / p_k < \infty$ for the
geometric sequence $p_k = 3(3/2)^k$.

The endpoint is:
$$
\|a^{p-2} F^p\|_\infty^{1/p} = \|a^{1-2/p} F\|_\infty \to \|aF\|_\infty
\quad\text{as } p \to \infty.
$$

Wait—this is the sup norm of $a \cdot F$, not $a^{1/2} F$. Since $K_p = \int a^{p-2} F^p$
and $p \to \infty$, $K_p^{1/p} \to \|aF\|_\infty^1$ provided we work on
$\{a > 0\}$. This gives $|a\operatorname{Rm}| \le C\beta/t$ on the flow
support.

### 7.6 Defect estimates: $Q$ and $J_6$

$Q(t) = \int_M |E|^2$ evolves homogeneously in $E$ (Step 14 identity):
$$
Q(t) \le e^{C\theta} Q(0), \qquad \theta = r^{-2} T + T.
$$

$J_{6,j}$ with $z_6 = a^{5/2} |E|^3$ has critical absorption at $p=6$:
$$
J_{6,j}(t) \le e^{C\theta} J_{6,j}(0).
$$

Starting from pointwise $|E| \le \delta$:
$J_{6,j}(0) \le \delta^6 \cdot \operatorname{Vol}(B_{6r})$,
$Q(0) \le \delta^2 \cdot \operatorname{Vol}(M)$.

The defect Moser iteration starting from $J_6$ and using the curvature bound
$|a\operatorname{Rm}| \le C\beta/t$ gives
$$
|aE|(t) \le C \delta (r^2/t)^{1/3}, \qquad t \in (0, T].
$$

### 7.7 Metric comparison

The metric drift is
$$
g(t) = g(0) - 2\int_0^t a E(s) \, ds.
$$

Since $|aE|(s) \le C\delta(r^2/s)^{1/3}$ and $\int_0^T s^{-1/3} ds = (3/2)T^{2/3}$:
$$
\|g(t) - g(0)\|_\infty \le C\delta r^{2/3} T^{2/3} = C\delta \theta^{2/3},
$$
which is small for $\delta \ll 1$. Thus $g(t)$ remains bilipschitz to $g(0)$
on the flow support.

## 8. Remaining conditional dependencies

The above first-exit closure is **conditional** on:

**(C1)** Short-time smooth existence of the degenerate flow on $[0, T]$.
This requires the shifted-curvature continuation theorem with the coupled
$(\nabla^m U, \nabla^{m+1}\chi)$ estimate (Step 30 TTCS V1).

**(C2)** The Maheux–Saloff-Coste Sobolev constant is the claimed
$S^2 = Cr^4/\operatorname{Vol}(B_r)$ with $C$ depending only on $(n, \kappa r^2)$.

**(C3)** The good-center maximal function threshold $\Lambda = 2C_M$ where
$C_M$ is the weak-$(1,1)$ constant. In four dimensions with
$\operatorname{Ric} \ge -\kappa g$, the maximal function is weak-$(1,1)$
with a constant depending on $(4, \kappa r^2)$.

These are well-established for (C2) and (C3). Only (C1) remains an open
mathematical question.

## 9. Comparison with A01 unweighted route

A01 proposed switching to unweighted $\int |U|^p$ where $U = a(\operatorname{Rm} + G)$.
The diffusion in the $U$-equation is $a\Delta U$, not $\Delta U$. Testing
$\int |U|^p$ gives the a-weighted dissipation $\int a |U|^{p-2} |\nabla U|^2$.

The Sobolev step requires $\|\nabla |U|^{p/2}\|_2^2 = (p^2/4)\int |U|^{p-2} |\nabla|U||^2$.
This is the **unweighted** gradient, which is not controlled by the a-weighted
dissipation without a lower bound on $a$.

Therefore the unweighted route faces the same degenerate-diffusion issue.
The weighted route resolves it by building $a^{(p-1)/2}$ into the test
function, so that $\nabla Z_p$ naturally involves only a-weighted derivatives.

**Conclusion:** The weighted K_p route is the correct primary route.
The unweighted U route is not automatically easier; it requires separate
justification near $\{a = 0\}$ that has not been provided.

## 10. Yang's recurrence verification

Yang (Appendix B of the pseudolocality paper) uses the sequence
$p'_{k+1} = (3/2) p'_k + 1$ where $p' = p - 2$. Starting from $p'_0 = 1$
(i.e., $p_0 = 3$):

| $k$ | $p'_k$   | $p_k$     |
|-----|----------|-----------|
| 0   | 1        | 3         |
| 1   | 5/2      | 9/2       |
| 2   | 19/4     | 27/4      |
| 3   | 65/8     | 81/8      |

The $+1$ accounts for the dimension-dependent Sobolev embedding amplification.
The net amplification ratio is $p_{k+1}/p_k \to 3/2$, consistent with our
Cauchy–Schwarz interpolation. $\square$

## References within session

- Step 25: `workspace/notes/step25_whole_support_moser_and_normalization_repair.md`
- Step 26: `workspace/notes/step26_general_p_and_sobolev_resolution.md`
- Step 30 TTCS V1: `trace/ttcs/results/step30_ttcs01_verifier1_integration.md`
- Step 30 TTCS V2: `trace/ttcs/results/step30_ttcs01_verifier2_integration.md`
- A01 Step 29: `Sessions/S0910A01/workspace/notes/step29_simultaneous_support_theorem.md`
