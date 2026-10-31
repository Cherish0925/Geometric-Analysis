# Step 61: Toric-cone opposite warping, Weyl eigenvalue reachability, and the Bianchi/Cotton necessity theorem

Session `S0910A02`. Agent2 / Constructor. Phase Execute.

Depends on: Steps 11, 34, 48–50, 57–60, and the Strategist's correction that the Step-60 local model uses the wrong geometry (flat T² over R² instead of the cone over S³/Z₂).

## 0. Summary

Three results established in this step:

**A. Toric-cone opposite warping.** The toric form of the flat cone R⁴/Z₂,
$$
g_0 = dr_1^2 + r_1^2\,d\phi^2 + dr_2^2 + r_2^2\,d\psi^2,
$$
with Z₂ acting by (φ,ψ) → (φ+π, ψ+π), admits the opposite-warping deformation
$$
g = dr_1^2 + r_1^2 e^{2v}\,d\phi^2 + dr_2^2 + r_2^2 e^{-2v}\,d\psi^2
$$
where $v = v(r_1, r_2)$ is a function on the orbit space (quarter-plane). **The opposite-warping cancellation holds exactly**: the base $(r_1, r_2)$ Ricci block depends only on **first** derivatives of $v$ (no Hessian), and the fiber Ricci blocks carry
$$
\operatorname{Ric}_{\phi\phi}/g_{\phi\phi} = -\mathcal{D}v, \qquad \operatorname{Ric}_{\psi\psi}/g_{\psi\psi} = +\mathcal{D}v,
$$
where $\mathcal{D}v = v_{r_1r_1} + v_{r_2r_2} + v_{r_1}/r_1 + v_{r_2}/r_2$ is the flat 4D Laplacian restricted to T²-invariant functions. This is the Step-11 mechanism on the correct A₁/EH geometry, replacing the flat-base-T² model of Step 60.

**B. Weyl eigenvalue structure and reachability.** The T²-invariant degree-2 harmonic $r_1^2 - r_2^2 = r^2\cos 2\alpha$ satisfies $\mathcal{D}(r_1^2 - r_2^2) = 0$. The static perturbation $v = \varepsilon A(r_1^2 - r_2^2)$ creates Weyl curvature with (at $\alpha = \pi/4$, linear in $\varepsilon$):
$$
W^+ = W^- = \varepsilon A \cdot \operatorname{diag}\!\left(\frac{8}{3}, -\frac{16}{3}, \frac{8}{3}\right),
$$
traceless (verified: $8 - 16 + 8 = 0$). The characteristic polynomial at $r_1 = r_2$ is
$$
p(\lambda) = -\frac{(8A - 3\lambda)^2(16A + 3\lambda)}{27},
$$
with eigenvalues $8\varepsilon A/3$ (double) and $-16\varepsilon A/3$ (single). The degeneracy condition $R_\pm = W_\pm + (\Lambda/3)\operatorname{Id}$ having a zero eigenvalue is reached at $\varepsilon A = \Lambda/16$ (giving $R_\pm = \operatorname{diag}(\Lambda/2, 0, \Lambda/2)$, one-dimensional kernel). At general angle $\alpha \ne \pi/4$, off-diagonal entries $\pm A(r_1/r_2 - r_2/r_1)$ split the double degeneracy, but the existence of a zero eigenvalue persists.

The eigenvalue ratio $1:(-2):1$ of the drift mode does NOT match the orbifold ratio $2:(-1):(-1)$ (from $R_\pm = \operatorname{diag}(\Lambda, 0, 0)$ on the product-quotient orbifold). This constrains the single-mode drift but does not prevent the first obstruction from being satisfied: on the product-quotient orbifold the kernel of $R_\pm$ is already 2-dimensional, so the first obstruction is automatically killed for any EH $\zeta$ in that plane. The drift becomes decisive only for generic orbifolds with 1D kernel.

**C. Bianchi/Cotton rate-limited necessity.** Second Bianchi gives $\operatorname{div} W = C$ (Cotton tensor), and $C$ is controlled by $\nabla(\operatorname{Ric} - \Lambda g)$. In the Wronskian flux form: the obstruction pairing
$$
B(\rho) = \int_{S^3/\mathbb{Z}_2(\rho)} \langle h, o_k \rangle\,dS
$$
satisfies
$$
|B(R) - B(r_0)| \le C t_i \delta_i \log(R/r_0),
$$
since the source $|\operatorname{Ric}_{\tilde g} - \Lambda t \tilde g| \le t\delta$ pairs against the obstruction mode $o_k \sim \rho^{-4}$ over each dyadic shell. The signal is $B \sim t\kappa$ (ambient H₂ coefficient). Therefore:
$$
\text{relative error} = O(\delta \log(1/t)).
$$
**Under $\delta_i \log(1/t_i) \to 0$**, the flux identifies the asymptotic H₂ coefficient, forcing $R_\pm(p)\zeta = 0$ at every noncollapsed A₁ bubble point.

The failure channel: at $t \sim e^{-a/\delta}$, the Cotton source saturates the Bianchi constraint over $\sim 1/\delta$ dyadic scales. Each shell contributes $\delta$ to the Weyl rotation, totaling $O(1)$. The Chern–Weil integral cannot see this: $|\operatorname{Rm}| = O(1)$ locally, and each annular shell contributes $\sim r^4 \, dr \sim r^3$ to $\int |W|^2$, giving total $O(R^4) = O(t^{-2})$ — negligible against the topological Chern–Weil total $8\pi^2\chi$.

## 1. Toric-cone computation (exact sympy verification)

### 1.1 Flat background check

Script `step61_toric_cone_warp_ricci.py` computes the full Ricci tensor of the warped metric via Christoffel symbols and curvature, all symbolically. At $v = 0$: all Ricci components vanish, confirming the toric coordinates describe flat $\mathbb{R}^4/\mathbb{Z}_2$.

### 1.2 Opposite-warping structure

The computation confirms:
- **Base block** (00, 01, 11 components): depends on $v_{r_1}, v_{r_2}$ (first derivatives only). The leading terms are:
$$
\operatorname{Ric}_{00} = -2v_{r_1}^2 - 2v_{r_1}/r_1, \qquad \operatorname{Ric}_{01} = -2v_{r_1}v_{r_2} + v_{r_1}/r_2 - v_{r_2}/r_1.
$$
The **linear** terms ($v_{r_1}/r_1$, $v_{r_1}/r_2 - v_{r_2}/r_1$) come from the nonconstant fiber radii; they are absent in the flat-base-T² model of Step 60. These are O(v_{r_i}) rather than O(v_{r_i}²).

**Crucial interpretation**: for the drift mode $v = tA(\rho)(r_1^2 - r_2^2)$ with $A = O(1)$, the linear terms are $O(t)$, the SAME order as the H₂ ambient signal. They are NOT a new Ricci defect — they are part of the linearized Einstein equation for the H₂ expansion on the cone, balanced by the cosmological term $\Lambda g$. The drift rate $A' = O(\delta)$ introduces an ADDITIONAL $O(t\delta)$ correction to both the base and fiber Ricci, compatible with the pinching window.

- **Fiber blocks**: carry $\pm\mathcal{D}v$ (second-order operator), exactly as in Step 60.

### 1.3 Drift mode harmonic

The unique T²-invariant degree-2 harmonic polynomial on $\mathbb{R}^4$ (restricted to the orbit space) is $r_1^2 - r_2^2 = r^2\cos 2\alpha$, where $r = \sqrt{r_1^2 + r_2^2}$ and $\alpha = \arctan(r_2/r_1)$.

Verified: $\mathcal{D}(r_1^2 - r_2^2) = 0$.

The drift mode $v = A(\rho)(r_1^2 - r_2^2)$ with $\rho = \log r$ has:
$$
\mathcal{D}v = \cos 2\alpha \cdot (A'' + 6A')
$$
(computed symbolically). For a slow profile $A'(\rho) = O(1/L)$, $A'' = O(1/L^2)$:
$$
|\mathcal{D}v| \le C/L = C\delta/a,
$$
confirming the drift produces $O(\delta)$ fiber Ricci per dyadic scale.

## 2. Weyl eigenvalue computation

Script `step61_weyl_eigenvalues.py` computes the full 4D Riemann and Weyl tensors in the orthonormal frame to first order in $\varepsilon$, using the Kulkarni–Nomizu decomposition:
$$
W = \operatorname{Rm} - \frac{1}{2}(\operatorname{Ric} \wedge g) + \frac{\operatorname{Scal}}{12}(g \wedge g).
$$
(Factor 1/12 corrected from initial 1/6 bug.)

### 2.1 Sectional curvatures (linear in $\varepsilon$)

All six independent sectional curvatures are constant (no $r_1, r_2$ dependence):
$$
K_{12} = 0, \quad K_{13} = -6A, \quad K_{14} = 2A, \quad K_{23} = 2A, \quad K_{24} = -6A, \quad K_{34} = 4A.
$$
Ricci check: $\operatorname{Ric}_{11} = K_{12} + K_{13} + K_{14} = 0 - 6A + 2A = -4A$ ✓.

### 2.2 Self-dual and anti-self-dual Weyl matrices

In the SD basis $\{\omega_1^+ = e_{12}+e_{34},\; \omega_2^+ = e_{13}-e_{24},\; \omega_3^+ = e_{14}+e_{23}\}$:
$$
W^+ = \varepsilon A \begin{pmatrix} 8/3 & 0 & 0 \\ 0 & -16/3 & -(r_1/r_2 - r_2/r_1) \\ 0 & -(r_1/r_2 - r_2/r_1) & 8/3 \end{pmatrix}.
$$
$W^-$ has the same diagonal but opposite sign on the off-diagonal entry. Both are traceless.

The characteristic polynomials of $W^+$ and $W^-$ are **identical**:
$$
p(\lambda) = \frac{1}{27r_1^2 r_2^2}\!\left[9A^2(r_1^4+r_2^4)(-8A+3\lambda) + r_1^2 r_2^2(-880A^3+522A^2\lambda-27\lambda^3)\right].
$$

### 2.3 Eigenvalue table

| Point | $W_\pm$ eigenvalues (× $\varepsilon$) |
|-------|---------------------------------------|
| $r_1 = r_2$ ($\alpha = \pi/4$) | $8A/3,\; 8A/3,\; -16A/3$ |
| $r_1 = \sqrt{2},\; r_2 = 1$ | $8A/3,\; -A(8+3\sqrt{66})/6,\; A(-8+3\sqrt{66})/6$ |
| General $\alpha \ne \pi/4$ | Split from double degeneracy; single $-16A/3$ mixes with $8A/3$ through off-diagonal |

### 2.4 Degeneracy/reachability

$R_\pm = W_\pm + (\Lambda/3)\operatorname{Id}$ degenerates when one eigenvalue is zero. At $\alpha = \pi/4$:
- **Single-mode target**: $-16\varepsilon A/3 + \Lambda/3 = 0$ at $\varepsilon A = \Lambda/16$, giving $R_\pm = \operatorname{diag}(\Lambda/2, 0, \Lambda/2)$.
- **Double-mode target**: $8\varepsilon A/3 + \Lambda/3 = 0$ at $\varepsilon A = -\Lambda/8$, giving $R_\pm = \operatorname{diag}(-2\Lambda/3, 2\Lambda, 0)$ (two zero eigenvalues impossible from a single mode).

The Weyl eigenvalue ratio $1:(-2):1$ is **structurally different** from the product-quotient orbifold ratio $2:(-1):(-1)$ (from $R_\pm = \operatorname{diag}(\Lambda, 0, 0)$). This means: the single T²-invariant mode cannot reproduce the full orbifold Weyl pattern. However, on the product-quotient orbifold, $R_\pm$ has a 2D kernel, so the first obstruction is automatically satisfied for any EH $\zeta$ in that plane, and **no drift is needed**.

For a generic orbifold with only a 1D kernel of $R_\pm$, the drift by $O(t)$ is the first-order obstruction coefficient $\lambda_k = c\langle R_\pm(p)\zeta, \zeta_k\rangle$ itself. The rate condition $\delta \log(1/t) \to 0$ freezes this O(t) coefficient, giving the classification theorem.

## 3. The Bianchi/Cotton one-inequality theorem

**Theorem (rate-limited H4 necessity).** Let $(M^4, g_i)$ be closed Riemannian with $\|\operatorname{Ric}_{g_i} - \Lambda g_i\|_{\mathrm{op}} \le \delta_i \to 0$, $\Lambda > 0$, noncollapsed, converging to an Einstein orbifold with an $A_1$ point $p$ at bubble scale $t_i \to 0$. If
$$
\delta_i \log(1/t_i) \to 0,
$$
then the Eguchi–Hanson orientation $\zeta$ must satisfy $R_\pm(p)\zeta = 0$.

**Mechanism.** Second Bianchi: $\nabla^i W_{ijkl} = C_{jkl}$ (Cotton), and for $\operatorname{Ric} = \Lambda g + E$:
$$
|C| \le C_n |\nabla E|.
$$
In flux form, the obstruction Wronskian satisfies
$$
|B(R) - B(r_0)| \le C \int_{r_0}^R \!\! t\delta \cdot \rho^{-4} \cdot \rho^3\,d\rho = Ct\delta \log(R/r_0).
$$
With $R \sim t^{-1/2}$ and signal $B \sim t\kappa$:
$$
\frac{|B(R) - B(r_0)|}{B_{\text{signal}}} \le C\delta \log(1/t).
$$

**Energy invisibility.** The drift produces $|W| = O(1)$ per annular shell, but each shell contributes $\sim r^4\,dr$ to $\int |W|^2$, totaling $O(R^4) = O(t^{-2}) \ll 8\pi^2\chi$ (the topological Chern–Weil total). No energy counting argument can detect the drift.

**Named failure channel.** At $t \sim e^{-a/\delta}$ ($a > 0$ fixed), the Cotton source saturates the Bianchi constraint:
$$
\delta \cdot L = \delta \cdot \frac{a}{\delta} = a = O(1),
$$
producing $O(1)$ total Weyl rotation. The resulting eigenvalue drift changes $R_\pm$ from the ambient value by $O(t)$, at signal level.

## 4. What this establishes and what remains

### Established

1. The opposite-warping mechanism transfers exactly to the toric-cone/EH geometry (from the flat-base-T² model of Step 60).
2. The Weyl eigenvalue structure under T²-invariant drift is completely determined: ratio $1:(-2):1$, reachability at $\varepsilon A = \Lambda/16$.
3. The Bianchi/Cotton one-inequality gives the sharpest form of the rate-limited necessity theorem, with the energy-invisibility observation showing why Chern–Weil arguments cannot replace it.
4. For the product-quotient orbifold family (Steps 55–57), the 2D kernel of $R_\pm$ means the first obstruction is automatically satisfied; the drift is irrelevant and the wall construction does not need the exponential neck.

### Not established

1. The full tensor flux identity (gauges, tower subtraction, nonlinear errors) needed to promote the one-inequality from a scaling argument to a geometric theorem.
2. Global caps for the toric-cone drift model (smooth end caps, EH matching, closed topology).
3. Whether non-T²-invariant modes can extend the single-mode reachability to the full obstruction.
4. Positive collapse, negative branch, and $n \ge 5$ (all untouched by this step).
5. Lean formalization (no global geometric theorem is proved).

### Files

- `workspace/scripts/step61_toric_cone_warp_ricci.py` → `workspace/data/step61_toric_cone_warp_ricci.json`
- `workspace/scripts/step61_drift_mode_and_weyl.py` → `workspace/data/step61_drift_mode_and_weyl.json`
- `workspace/scripts/step61_weyl_eigenvalues.py` → `workspace/data/step61_weyl_eigenvalues.json`
- `workspace/scripts/step61_bianchi_cotton_theorem.py` → `workspace/data/step61_bianchi_cotton_theorem.json`
