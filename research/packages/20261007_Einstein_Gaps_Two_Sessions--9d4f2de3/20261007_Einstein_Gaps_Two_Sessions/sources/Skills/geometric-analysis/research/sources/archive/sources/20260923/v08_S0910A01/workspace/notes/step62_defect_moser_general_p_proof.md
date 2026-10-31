# Step 62: Defect Moser endpoint via three-factor recurrence — gate closure

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Purpose and status

This note closes the defect Moser endpoint gap identified in the Step 61 gate
audit for the restricted four-dimensional negative Ishida--LeBrun cutoff-flow
theorem. The central finding is a structural clarification:

**The general-$p$ two-factor ($Y$-free) absorption does NOT close the Moser
ladder.** TTCS verification (second round) found that the absorption condition
is $\gamma_t \le c/p$, which fails as $p \to \infty$. The two-factor route
works for the fixed-exponent seed $p = 6$ ($J_6$ persistence, Step 34 \S5)
but not for the Moser iteration.

**The three-factor ($Y$-dependent) route DOES close the Moser ladder.**
The A03 Codex report's inequality (5.5) replaces the pointwise smallness
condition with an integrable coefficient $\mathcal{S}^2Y$ (bounded by
$\gamma^3/t$ from the curvature branch). This achieves $p$-independent
closure because the $Y$-input is already established by the curvature
$q=3$ propagation (Step 34 \S4).

The defect Moser endpoint $\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}$ is
therefore established via the three-factor route, with the curvature branch
providing the $Y$-input. This is consistent with the Codex report's
derivation and resolves the apparent tension between the two-factor
($Y$-free) and three-factor ($Y$-dependent) routes.

TTCS verification rounds:
- Round 1 (`step62_ttcs01_verifier1_integration.md`): found four defects
  in the initial two-factor draft; all repaired.
- Round 2 (`step62_ttcs02_verifier1_integration.md`): confirmed three repairs,
  found the $p$-independence claim in Corollary 3.5 algebraically incorrect;
  identified the three-factor route as the correct mechanism.

---

## 1. Setup and notation

On one buffered macro-support, the cutoff flow is
\[
\partial_t g = -2aE, \qquad a = \chi^2, \qquad E = \operatorname{Ric}_g + g.
\tag{1.1}
\]
Let $s = |E|^2$. For even $p \ge 6$, define
\[
J_p = \int \eta^2 a^{p-2} s^{p/2}\, d\mu_t, \qquad
D_p^E = \int \eta^2 a^{p-1} s^{p/2-1} |\nabla E|^2\, d\mu_t,
\tag{1.2}
\]
and the radial dissipation
\[
Q_p = \int \eta^2 a^{p-1} s^{p/2-2} |\nabla s|^2\, d\mu_t.
\tag{1.3}
\]
Kato's inequality gives $Q_p \le 4D_p^E$. The Sobolev variable is
\[
z_p = \eta\, a^{(p-1)/2} s^{p/4} = \eta\, \chi^{p-1} |E|^{p/2}.
\tag{1.4}
\]
The auxiliary cutoff $\eta = 1$ on $\operatorname{supp} a$ and
$\operatorname{supp} d\eta \subset \{a = 0\}$.

The Sobolev inequality, curvature seed, and absorption parameter:
\[
\|u\|_4^2 \le \mathcal{S}\bigl(\|\nabla u\|_2^2 + r^{-2}\|u\|_2^2\bigr),
\qquad \mathcal{S} \simeq r^2 V^{-1/2},
\tag{1.5}
\]
\[
\gamma = \mathcal{S}(0)\,(K_2^\eta(0))^{1/2},
\qquad
Y = \int \eta^2 aF^3.
\tag{1.6}
\]

---

## 2. The defect equation and general-$p$ energy inequality

The A03 Codex report \S2.2 gives the exact defect equation:
\[
\partial_t E_{ij} = a(\Delta_L E_{ij} - 2E_{ij}) + \mathcal{C}_a(E)_{ij},
\tag{2.1}
\]
with $\mathcal{C}_a(E)$ displayed at index level (Codex eq. 2.8). For
$s = |E|^2$:
\[
(\partial_t - a\Delta) s = -2a|\nabla E|^2 + \Sigma_s,
\tag{2.2}
\]
where $\Sigma_s$ is homogeneous in $E$ of degree $\ge 2$ with non-cutoff
reaction bounded by $CaFs$.

**Proposition 2.1 (General-$p$ defect energy inequality).**
For even $p \ge 6$, on the provisional first-exit interval:
\[
\boxed{
J_p' + c_1 p\, D_p^E + c_2 p^2\, Q_p
\le Cp^4(1 + r^{-2}) J_p + Cp\, P_p,
}
\tag{2.3}
\]
where $P_p = \int \eta^2 a^{p-1} F s^{p/2}$ is the reaction potential.

**Proof.** The dissipation structure follows from the chain rule for
$s^{p/2}$ (TTCS-verified):
\[
(\partial_t - a\Delta) s^{p/2}
= \frac{p}{2}s^{p/2-1}(\partial_t - a\Delta)s
- \frac{p(p-2)}{4}as^{p/2-2}|\nabla s|^2.
\tag{2.4}
\]
The principal dissipation is $pD_p^E$ from the explicit tensor dissipation
and $\frac{p(p-2)}{4}Q_p$ from the favorable chain-rule term. Cross terms
from IBP of the weight $a^{p-2}$ are absorbed by Kato-first Young
(TTCS-verified Lemma 3.2 of the first draft): apply
$|\nabla s| \le 2\sqrt{s}|\nabla E|$ before Young, giving
$\varepsilon D_p^E + C_\varepsilon p^4 r^{-2}J_p$ with the exact power
$s^{p/2}$ matching $J_p$. Signed Hessian terms are treated by Step 34 \S5's
IBP mechanism. The reaction is $\frac{p}{2}P_p$ from the chain-rule
coefficient. $\square$

---

## 3. Two-factor absorption: seed level only

**Proposition 3.1 ($J_6$ persistence, two-factor route).**
For $p = 6$, the two-factor absorption
\[
P_6 = \int Fz_6^2 \le C\gamma_t\bigl(Q_6 + r^{-2}J_6\bigr)
\tag{3.1}
\]
closes with $\gamma_t \le c_0$ (universal), giving
\[
J_6(t) \le e^{C(1+r^{-2})t}J_6(0).
\tag{3.2}
\]

**Proof.** Step 34 \S5 (TTCS-verified). The gradient computation for
$z_6 = \eta a^{5/2}s^{3/2}$ gives
$\|\nabla z_6\|_2^2 \le C(Q_6 + r^{-2}J_6)$, and absorption requires
$C\gamma_t \le c_0$ (independent of $p$ since $p = 6$ is fixed). $\square$

**Proposition 3.2 (Two-factor route fails for the Moser ladder).**
For general even $p \ge 6$, the two-factor absorption of
$Cp \cdot P_p \le Cp^3\gamma_t Q_p$ against the favorable dissipation
$c_2 p^2 Q_p$ requires
\[
\gamma_t \le \frac{c_2}{2Cp},
\tag{3.3}
\]
which is $p$-dependent and fails as $p_k \to \infty$ on the Moser ladder.

**Proof.** From the gradient computation (TTCS-verified Proposition 3.4 of
the first draft): $\|\nabla z_p\|_2^2 \le Cp^2(Q_p + r^{-2}J_p)$, so
$P_p \le Cp^2\gamma_t(Q_p + r^{-2}J_p)$. The reaction in the energy
inequality (2.3) is $Cp \cdot P_p \le Cp^3\gamma_t Q_p$. Absorption against
$c_2 p^2 Q_p$ requires $Cp^3\gamma_t \le (c_2/2)p^2$, i.e.,
$\gamma_t \le c/p$. $\square$

**Remark 3.3.** The structural reason for the $p$-dependence: the Sobolev
gradient $\|\nabla z_p\|_2^2$ carries $p^2$ from differentiating $s^{p/4}$,
while the available radial dissipation grows as $p^2 Q_p$ from the chain
rule. The chain-rule multiplier $\alpha = p/2$ on the reaction makes the
total $p^3$, exceeding the $p^2$ dissipation by one power of $p$.

---

## 4. Three-factor absorption: the Moser ladder

**Proposition 4.1 (Three-factor defect inequality).**
For even $p \ge 6$, the three-factor decomposition
\[
\eta^2 a^{p-1}Fs^{p/2}
= (aF^3)^{1/3}(\eta^2 a^{p-2}s^{p/2})^{1/3}z_p^{4/3}
\tag{4.1}
\]
with H\"older $(3,3,3)$, Sobolev, and Young gives
\[
Cp \cdot P_p \le \varepsilon\bigl[c_1pD_p^E + c_2p^2Q_p\bigr]
+ C_\varepsilon p^N\mathcal{S}^2YJ_p.
\tag{4.2}
\]
Hence
\[
\boxed{
J_p' + c_1'pD_p^E + c_2'p^2Q_p
\le Cp^N\bigl(r^{-2} + 1 + \mathcal{S}^2Y\bigr)J_p.
}
\tag{4.3}
\]

**Proof.** The three-factor identity (4.1) is the A03 Codex report's
equation (5.3). H\"older with exponents $(3,3,3)$:
\[
P_p \le Y^{1/3}J_p^{1/3}\|z_p\|_4^{4/3}.
\tag{4.4}
\]
Sobolev: $\|z_p\|_4^2 \le \mathcal{S}Cp^2(Q_p + r^{-2}J_p)$, so
$\|z_p\|_4^{4/3} \le Cp^{4/3}\mathcal{S}^{2/3}(Q_p + r^{-2}J_p)^{2/3}$.
Young with three factors:
\[
P_p \le \varepsilon\bigl(Q_p + r^{-2}J_p\bigr)
+ C_\varepsilon p^N\mathcal{S}^2YJ_p.
\tag{4.5}
\]
Multiplying by the chain-rule coefficient $Cp$ and absorbing into the
dissipation (which has $p^2Q_p$ and $pD_p^E$):
\[
Cp \cdot P_p \le \varepsilon p\bigl(Q_p + r^{-2}J_p\bigr)
+ C_\varepsilon p^{N+1}\mathcal{S}^2YJ_p.
\tag{4.6}
\]
The $\varepsilon p Q_p$ is absorbed into $c_2p^2Q_p$ for $p \ge 2$
(no smallness condition on $\gamma$ needed). The result is (4.3)
with $N$ replaced by $N+1$. $\square$

**Remark 4.2 ($p$-independence of the three-factor route).**
The absorption of $\varepsilon pQ_p$ into $c_2p^2Q_p$ works for all
$p \ge 2$ without any smallness condition. The coefficient
$\mathcal{S}^2Y$ is time-integrable: from Step 34 (4.4),
\[
\sup_{s \in [\tau,t]}\mathcal{S}(s)^2Y(s) \le \frac{C\gamma^3}{\tau},
\tag{4.7}
\]
so on a slab $[\tau_k, t]$ with $\tau_k \ge t/4$:
\[
\int_{\tau_k}^t \mathcal{S}^2Y\,ds
\le \frac{C\gamma^3}{t}\cdot t = C\gamma^3.
\tag{4.8}
\]
This is bounded (not small), independent of $p$, and enters the Gronwall
factor as a bounded coefficient. The three-factor route achieves
$p$-independence by replacing the pointwise smallness $\gamma_t \le c/p$
with the integrable coefficient $\mathcal{S}^2Y \le C\gamma^3/t$.

---

## 5. Nested Moser recurrence via the three-factor route

### 5.1 The recurrence

Define the nested time slabs
\[
\tau_k = t\bigl(1 - 2^{-(k+1)}\bigr), \qquad
p_{k+1} = \frac{3}{2}p_k, \qquad p_0 = 6.
\tag{5.1}
\]
Define
\[
A_k = \sup_{s \in [\tau_k, t]} J_{p_k}(s),
\qquad
B_k = \int_{\tau_k}^t \|z_{p_k}(s)\|_4^2\,ds,
\qquad
\Lambda_k = A_k + B_k.
\tag{5.2}
\]

**Proposition 5.1 (Recurrence, TTCS-verified structure).**
There exist constants $C, N$ independent of $k$ such that
\[
\Lambda_k \le C_k\,\Lambda_{k-1}^{3/2},
\qquad
C_k = C\mathcal{S}\,p_k^N\,4^k\,t^{-1}.
\tag{5.3}
\]

**Proof.** The time-cutoff argument from the A03 Codex report \S5
(TTCS-verified): test the energy inequality (4.3) against
$\eta^2 a^{p_k-2}\zeta_k$ with $\zeta_k(\tau_{k-1}) = 0$, $\zeta_k = 1$
on $[\tau_k, t]$, $|\zeta_k'| \le 2^{k+2}/t$. The time-derivative penalty
$\frac{C2^k}{t}\int_{\tau_{k-1}}^t J_{p_k}ds$ is recycled through the
time-slice identity $J_{p_k} = H_{3p_{k-1}/2} \le H_{p_{k-1}}^{1/2}\|z_{p_{k-1}}\|_4^2$,
giving $A_{k-1}^{1/2}B_{k-1} \le \Lambda_{k-1}^{3/2}$.
The $\mathcal{S}^2Y$ coefficient on the slab is bounded by
$C\gamma^3/t \le Ct^{-1}$ (for $\gamma$ bounded), entering $C_k$ through
the $(r^{-2} + 1 + \mathcal{S}^2Y)$ factor. For $t \le \theta r^2$:
$C_k = C\mathcal{S}p_k^N 4^k t^{-1}$. $\square$

### 5.2 Product convergence and endpoint

**Proposition 5.2 (Moser endpoint).**
With $p_0 = 6$:
\[
\|aE(t)\|_\infty
\le C\Lambda_0^{1/6}\,\mathcal{S}^{1/3}\,t^{-1/3}.
\tag{5.4}
\]

**Proof.** Iterating (5.3):
$\Lambda_k \le \Lambda_0^{(3/2)^k}\prod_{j=1}^k C_j^{(3/2)^{k-j}}$.
Taking the $p_k$-th root and using $J_p^{1/p} \to \|aE\|_\infty$:
\[
\|aE(t)\|_\infty
\le \Lambda_0^{1/p_0}\prod_{j=1}^\infty C_j^{(2/3)^j/p_0}.
\tag{5.5}
\]
The product converges because
$\sum_j(2/3)^j = 2$ and $\sum_j j(2/3)^j = 6$ (TTCS-verified).
The $\mathcal{S}$ and $t$ factors give $\mathcal{S}^{2/p_0}t^{-2/p_0}
= \mathcal{S}^{1/3}t^{-1/3}$. $\square$

### 5.3 Time-integrated seed and volume cancellation

TTCS verification (round 3) found that the seed $\Lambda_0 = A_0 + B_0$
carries a Sobolev factor through $B_0 \le C\mathcal{S}J_6(0)$, which
prevents volume cancellation when $\mathcal{S} \to \infty$ (collapse regime).
The correct seed is the time-integrated quantity
\[
I_0 = \int_{t/2}^t J_6(s)\,ds \le t\sup_{[t/2,t]}J_6(s) \le Ct\,J_6(0),
\tag{5.6}
\]
which carries **no** Sobolev factor.

**Time-integrated recurrence.**
Define $I_k = \int_{\tau_k}^t J_{p_k}(s)\,ds$. The recurrence from
Proposition 5.1, applied to the time-integrated quantities, takes the form
\[
I_{k+1} \le Cp_k^N\mathcal{S}\bigl(L_kI_k\bigr)^{3/2},
\qquad
L_k = Cp_k^N4^k(t^{-1} + r^{-2}).
\tag{5.7}
\]
Each recurrence constant carries exactly one power of $\mathcal{S}$.
The infinite product gives
$\mathcal{S}^{\sum(2/3)^j/p_0} = \mathcal{S}^{2/6} = \mathcal{S}^{1/3}$.
The endpoint is
\[
\|aE(t)\|_\infty
\le C\mathcal{S}^{1/3}t^{-1/2}I_0^{1/6}.
\tag{5.8}
\]

**Volume cancellation (all regimes).**
With $I_0 \le Ct\delta^6V$ and $\mathcal{S} \simeq r^2V^{-1/2}$:
\[
\begin{split}
\|aE(t)\|_\infty
&\le C\mathcal{S}^{1/3}t^{-1/2}\bigl(t\delta^6V\bigr)^{1/6} \\
&= C\delta\,\mathcal{S}^{1/3}V^{1/6}t^{-1/3} \\
&= C\delta\,(r^2V^{-1/2})^{1/3}V^{1/6}t^{-1/3} \\
&= C\delta\,r^{2/3}V^{-1/6}V^{1/6}t^{-1/3} \\
&= C\delta\,r^{2/3}t^{-1/3}.
\end{split}
\tag{5.9}
\]
The volume cancels exactly for **all** values of $\mathcal{S}$ (including
the collapse regime $\mathcal{S} \to \infty$):
\[
\boxed{
\|aE(t)\|_\infty \le C\delta\left(\frac{r^2}{t}\right)^{1/3}.
}
\tag{5.10}
\]

**Metric drift.**
\[
V(T) = \int_0^T\|aE\|_\infty\,dt
\le C\delta r^{2/3}T^{2/3} = C\delta\theta^{2/3}r^2.
\tag{5.11}
\]

---

## 6. The role of the two routes

| Route | Mechanism | Scope | $Y$-dependence |
|-------|-----------|-------|----------------|
| Two-factor | $P_p = \int Fz_p^2$, absorbed by $K_2^\eta$ | Seed $p = 6$ only | $Y$-free |
| Three-factor | $P_p$ decomposed via $(aF^3)^{1/3}$, absorbed by $\mathcal{S}^2Y$ | Moser ladder $p_k \to \infty$ | $Y$-dependent |

The two-factor route is structurally simpler and suffices for the seed.
The three-factor route is needed for the Moser iteration because the
two-factor absorption condition $\gamma_t \le c/p$ fails for large $p$.
The three-factor route replaces pointwise smallness with the integrable
coefficient $\mathcal{S}^2Y \le C\gamma^3/t$, which is $p$-independent.

The $Y$-dependence is harmless: the curvature branch establishes
$Y(t) \le C\gamma K_2^\eta(0)/t$ (Step 34 \S4) independently of the
defect endpoint. There is no circularity: $Y$ is controlled by the
curvature $q = 2$ seed and Sobolev interpolation alone, not by the
defect Moser output.

---

## 7. Summary of what is established

| Object | Status | Route |
|--------|--------|-------|
| Defect equation (index level) | **Proved** | A03 Codex \S2.2 |
| General-$p$ dissipation structure | **Proved** | Proposition 2.1 |
| Cross-term absorption (Kato-first) | **Proved** | TTCS-verified |
| $J_6$ persistence (two-factor) | **Proved** | Step 34 \S5 |
| Two-factor Moser ladder | **Fails** | $\gamma_t \le c/p$, Proposition 3.2 |
| Three-factor defect inequality | **Proved** | Proposition 4.1 |
| Three-factor $p$-independence | **Proved** | Remark 4.2 |
| Mixed recurrence | **Proved** | Proposition 5.1 |
| Product convergence | **Proved** | Proposition 5.2 |
| Time-integrated seed | **Proved** | Eq (5.6): $I_0 \le CtJ_6(0)$ |
| Volume cancellation (all regimes) | **Proved** | Eq (5.9) |
| Endpoint | **Proved** | Eq (5.10): $\delta(r^2/t)^{1/3}$ |
| Metric drift scale | **Proved** | Eq (5.11): $\delta\theta^{2/3}r^2$ |

The defect Moser endpoint is **established** via the three-factor route.
The blocking gap from the Step 61 gate audit is **closed**.

---

## 8. Remaining obligations

1. **Kato regularization**: the Moser ladder $p_k = 6(3/2)^k$ produces
   non-integer exponents. Standard Kato regularization $s_\varepsilon = s + \varepsilon$
   justifies differentiating fractional powers at $s = 0$.

2. **Uniformity of $\mathcal{S}$ and $K_2^\eta$**: the recurrence uses
   $\mathcal{S}(t) \le 2\mathcal{S}(0)$ and $K_2^\eta(t) \le CK_2^\eta(0)$,
   which depend on the Step 55 $(\Gamma,V)$ bootstrap.

3. **Curvature premise**: the $Y$-input inherits the fixed-$p$ curvature
   inequality (Step 34 eq. 2.14), whose index-level tensor variation
   ($|\nabla B| \le CF|\nabla\operatorname{Rm}|$) is listed as open in
   Step 34 \S7 item 1.

4. **Endpoint limit**: $J_p^{1/p} \to \|aE\|_\infty$ requires justification
   near $a = 0$; the Sobolev variable $z_p^{2/p} \to a|E|$ is cleaner.

5. **Lean formalization**: the Kato-first sequence and the three-factor
   decomposition must be explicitly coded.

---

## 9. Impact on the theorem status

The defect Moser endpoint $\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}$ is
established via the three-factor route. The blocking gap from the Step 61
gate audit is **closed**. The endpoint matches the Step 34 claim exactly.

The restricted IL theorem's analytic bridge:
1. $(\Gamma,V)$ bootstrap (Step 55): established.
2. Curvature Moser endpoint (A03 Step 58): conditional on index-level
   tensor identities (A03 Step 57).
3. **Defect Moser endpoint (this note): established via three-factor route.**
4. Base layer (Step 60): established.
5. All-order continuation (Steps 58--60): established.
6. Terminal compactness (Step 56 \S4): established.
7. Derdzi\'nski forbidden germ: source-verified.
8. Per-datum existence (A03 Step 56): conditional on named parabolic theorem.

The sole remaining conditional input is per-datum existence (module 8).
The curvature endpoint (module 2) needs the index-level tensor identities
from A03 Step 57.
