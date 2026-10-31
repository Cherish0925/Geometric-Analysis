# Step 29: Terminal density bridge lemma

## Statement

**Lemma (Terminal density bridge).** Let $M$ be a closed oriented
four-manifold carrying an Ishida–LeBrun monopole class $a$ with
$(a^+)^2 \ge A > 0$ and $D_a \ge 0$.  Let $g$ be a smooth Riemannian metric
on $M$ with $E = \operatorname{Ric}_g + g$, $Q = \int|E|^2$, and suppose
$Q/(8\pi^2) \le \varepsilon$ for some $\varepsilon > 0$.  Suppose also that
there exist a set $P \subset M$ and constants $\alpha, K, \rho > 0$ such that:

(i) $\operatorname{Vol}_g(P) \ge \alpha A$;
(ii) for every $p \in P$, $|\operatorname{sec}_g| \le K$ on
     $B_\rho(p)$ and $K\rho^2 < \pi^2/4$.

Then there exists $p \in P$ and a smooth Riemannian metric $\hat g$ on
$B_\rho(0) \subset T_pM$ (the exponential pullback) such that:

(a) $\hat g = (\exp_p^g)^* g$ on $B_\rho(0)$;
(b) $\operatorname{Vol}_{\hat g}(B_{\rho/2}(0)) \ge c(K,\rho) > 0$;
(c) $A_\rho\mathfrak D(p) \le C(K,\rho,\alpha)\varepsilon$,

where $\mathfrak D$ is the combined nonnegative density

$$
\mathfrak D = |E|^2 + (s+4)^2 + (s+8\sqrt6|W^+|)^2 + \mathcal G
+ \left(|2\pi H|-\frac{r}{3\sqrt2}\right)^2 + 2\langle\mathscr AH,H\rangle,
\tag{1}
$$

with $r = q^+ = (\sqrt6|W^+| - s)^+$, $H$ is the harmonic representative
of $iF_A^+/(2\pi)$ for a smooth positive-weight rescaled monopole, and
$\mathscr A = W^+ + \sqrt{2/3}|W^+|I_{\Lambda^+}$ is the lowest-eigenline
projector.

## Construction

### Step 1: Terminal calibration

At the terminal metric $g$, reapply Chern–Gauss–Bonnet and the monopole
inequality (A01 Step 28, eq. (1.1)–(1.7)):

$$
\int|E|^2 = Q, \quad
\int(s+4)^2 \le 4Q, \quad
\int(s+8\sqrt6|W^+|)^2 \le 108Q, \quad
\int\mathcal G \le 6Q.
\tag{2}
$$

These use only the topological identity and the selected sign class; no
flow history is needed.

### Step 2: Positive-part rescaled monopole (Step 16 construction)

Set $q = \sqrt6|W^+| - s$ and $r = q^+ = \max(q, 0)$.  Choose
$\varepsilon_Q = Q$ and smooth positive $a \approx r + \varepsilon_Q$
(uniformly on each metric), set $f = \sqrt a$.  The rescaled monopole
equations for $(A, \Phi)$ with weight $f$ yield:

$$
\int(q^-)^2 \le C_0 Q, \qquad
\left|\int q^2 - \beta\right| \le C_0 Q,
\tag{3}
$$

where $\beta = 72\pi^2(a^+)^2$.  The exact signed decomposition gives

$$
L^+_f - \beta = 18J_A + H_2 + \frac{A_f(X_f + Z^{1/3})}{Z^{2/3}}
(P_f + N_f + H_1^+),
\tag{4}
$$

with all four terms nonnegative.  The key outputs are:

- **Harmonic amplitude**: $\||2\pi H| - r/(3\sqrt2)\|_2^2 \le CQ$.
  Combined with $\|r - 9/2\|_2^2 \le CQ$: $|H| \to 3/(4\sqrt2\pi)$ in $L^2$.
  
- **Eigenline control**: on the bounded-curvature set,
  $\int_P\langle\mathscr AH,H\rangle \le C(K)Q$.

No derivatives of $f$ appear in these estimates.  The spinor is not
transported; it is reconstructed at the terminal metric $g$.

### Step 3: Combined density

From (2) and the Step 16 estimates:

$$
\int_M\mathfrak D \le 119Q + CQ + C(K)Q \le C_{\rm tot}Q.
\tag{5}
$$

The constant $C_{\rm tot}$ depends on $K$ but not on the specific topology.

### Step 4: Exponential-pullback averaging

For nonneg $\mathfrak D$ and the set $P$ satisfying (i)–(ii), the
exponential-pullback lemma (Rauch + Liouville) gives:

$$
\int_P A_\rho\mathfrak D(p)\,d\mu(p) \le C(4,K,\rho)\int_M\mathfrak D\,d\mu.
\tag{6}
$$

Since $\operatorname{Vol}(P) \ge \alpha A$ and $\int\mathfrak D \le C_{\rm tot}Q$:

$$
\frac{1}{\operatorname{Vol}(P)}\int_P A_\rho\mathfrak D(p)\,d\mu(p)
\le \frac{C(K,\rho)C_{\rm tot}}{\alpha A} \cdot Q.
\tag{7}
$$

Select $p \in P$ with $A_\rho\mathfrak D(p) \le C(K,\rho,\alpha)Q/A$.

If $Q/A \to 0$ along the pinching sequence, then
$A_\rho\mathfrak D(p_i) \to 0$.

### Step 5: Tangent-space compactness

The pullback $\hat g_i = (\exp_{p_i}^g)^*g$ on $B_\rho(0)$ satisfies:

- Rauch lower Jacobian: $J_i(t,\xi) \ge s_K(t)^3$, so
  $\operatorname{Vol}_{\hat g_i}(B_{\rho/2}(0)) \ge c(K,\rho) > 0$.
- Bounded curvature: $|\operatorname{Rm}_{\hat g_i}| \le K$ on $B_\rho(0)$.
- No collapse on the tangent ball, even if $M$ is arbitrarily collapsed.

Standard harmonic-coordinate theory (Cheeger–Gromov–Taylor, with one radius
shrink): extract a subsequence converging in $C^{1,\alpha}$ (and strongly in
$W^{2,p}$ for finite $p$) on $B_{\rho/2}(0)$ to a smooth metric $g_\infty$.

At positive flow time, interior Shi estimates supply all curvature derivative
bounds on a smaller ball, upgrading to smooth convergence.

### Step 6: Vanishing density on the limit

The pullback mean $A_\rho\mathfrak D(p_i) \to 0$ and the nonneg components
force, on the limit:

$$
\operatorname{Ric}_{g_\infty} = -g_\infty, \quad
s_\infty = -4, \quad
|W^+_\infty|^2 = \frac{1}{24}, \quad
\mathscr A_\infty H_\infty = 0, \quad
|H_\infty| = \frac{3}{4\sqrt2\pi} > 0.
\tag{8}
$$

### Step 7: Calibrated spectrum and projector contradiction

From $\mathscr A_\infty H_\infty = 0$ and $H_\infty \ne 0$:
$H_\infty$ is a nonzero self-dual eigenform lying in the lowest eigenspace
of $W^+_\infty$.  Combined with $|W^+_\infty|^2 = 1/24$:

$$
\operatorname{Spec}(W^+_\infty) = \left(-\frac16, \frac{1}{12}, \frac{1}{12}\right).
\tag{9}
$$

The Bianchi identity gives $\delta W^+_\infty = 0$ (Einstein).  The
constant simple/double eigenvalue structure and the projector identity
force $\nabla W^+_\infty = 0$ (Step 6 argument).

But the Einstein–Weyl identity:

$$
\Delta|W^+|^2 = 2|\nabla W^+|^2 + s|W^+|^2 - 36\det W^+,
$$

with $s = -4$, $|W^+|^2 = 1/24$,
$\det W^+ = (-1/6)(1/12)^2 = -1/864$:

$$
0 = 2|\nabla W^+|^2 - \frac{1}{6} + \frac{36}{864}
= 2|\nabla W^+|^2 - \frac{1}{6} + \frac{1}{24}
= 2|\nabla W^+|^2 - \frac{1}{8}.
$$

So $|\nabla W^+|^2 = 1/16 \ne 0$.  **Contradiction.**

## What is proved and what is assumed

**Proved unconditionally** (in this lemma):
- Terminal recalibration from topology + gauge theory
- Positive-part weight construction and harmonic-amplitude/eigenline estimates
- Exponential-pullback averaging without base noncollapse
- Tangent-space compactness and smooth limit extraction
- Calibrated spectrum determination
- Projector contradiction

**Assumed** (from the cutoff-flow chain):
- $Q/A \to 0$ along the sequence (from global $Q$ preservation under the flow)
- Existence of $P$ with $\operatorname{Vol}(P) \ge \alpha A$ and bounded
  sectional curvature with geodesic buffer (from the selected-support flow
  at terminal time)
- Smooth convergence on the tangent ball (from interior Shi estimates at
  positive flow time, requiring the continuation theorem)

## Cross-references

- Step 16 positive-part construction:
  `trace/ttcs/results/step16_ttcs02_sub1_generator.md`
- A01 terminal recalibration:
  `Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md`
- Step 6 projector contradiction:
  `workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex`
- Step 16 exponential-pullback:
  `workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md`
- Calibrated density verification:
  `workspace/scripts/verify_positive_part_monopole_algebra.py`
