# Step 22: Inverse-square counterexample, transcription correction, and two-stage architecture

## 1. The inverse-square stress test

The Step 21 TTCS generator proposed an abstract Nash lemma: if the curvature potential $\mathcal K = aF$ satisfies the form bound
$$
\int_\Omega \mathcal K \phi^2\,d\nu \le \gamma\,\mathfrak e_t[\phi],
\qquad \gamma = C\sqrt{\varepsilon_{\rm Li}} \ll 1,
\tag{1}
$$
then the evolution semigroup satisfies $\|P(t,s)\|_{L^2(\nu)\to L^\infty} \le CA^2(t-s)^{-1}$.

**This claim is false.** The decisive counterexample is the Hardy potential in $\mathbb R^4$.

### The counterexample

On $\mathbb R^4$, consider $V = \kappa/|x|^2$ with $0 < \kappa < 1$. The Hardy inequality gives
$$
\int_{\mathbb R^4} \frac{\kappa}{|x|^2}|\phi|^2\,dx \le \kappa \int_{\mathbb R^4}|\nabla\phi|^2\,dx
\qquad \forall\,\phi\in C_c^\infty(\mathbb R^4).
$$
This is exactly the form bound (1) with $\gamma = \kappa < 1$.

The Schrödinger operator $H = -\Delta - V$ is well-defined and positive in the form sense: $\langle\phi, H\phi\rangle \ge (1-\kappa)\int|\nabla\phi|^2$. The heat semigroup $e^{-tH}$ exists and is bounded on $L^2(\mathbb R^4)$.

However, the radial fundamental solutions of $-\Delta u - Vu = 0$ near $r = 0$ are $u \sim r^{-\alpha}$ with
$$
\alpha^2 - 2\alpha + \kappa = 0,
\qquad
\alpha_\pm = 1 \pm \sqrt{1-\kappa}.
$$
The less singular solution $r^{-\sigma}$ with $\sigma = 1 - \sqrt{1-\kappa} > 0$ is in $L^2_{\rm loc}(\mathbb R^4)$ (since $4 - 2\sigma > 0$) but NOT in $L^\infty$. The heat kernel inherits this singularity:
$$
e^{-tH}(x,y) \sim t^{-2}\,|x|^{-\sigma}|y|^{-\sigma}\,\Phi(|x|/\sqrt{t},\,|y|/\sqrt{t})
$$
near the origin. For any $L^2$ initial data that is nonzero near the origin, $\|e^{-tH}f\|_\infty = \infty$ for all $t > 0$.

**Numerical values:** For $\kappa = 0.5$: $\sigma \approx 0.293$. For $\kappa = 0.9$: $\sigma \approx 0.684$. Even very small $\kappa$ gives $\sigma \approx \kappa/2 > 0$.

### Why it applies to our setting

The conformal domain $(\Omega, \nu_t)$ with $d\nu_t = a^{-2}d\mu_{g(t)}$ has cusps near $\{a = 0\}$. The conformal metric $\hat g = a^{-1}g$ makes $\partial\Omega$ a conformal infinity. The geometry there is effectively non-compact, and the curvature potential $\mathcal K$ is in $L^2(\nu)$ (critical) but not in $L^p(\nu)$ for $p > 2$ at time $t = 0$.

The form bound (1) controls the quadratic energy but does not control the singular spatial behavior of the heat kernel near the cusps. This is exactly the Hardy phenomenon.

Smooth regularization of the Hardy potential preserves the uniform form bound while the $L^2\to L^\infty$ constants degenerate — just as the smooth cutoff $\chi$ regularizes the boundary but the uniform constants of any proposed Nash bound degenerate.

## 2. Transcription correction

The TTCS generator correctly identifies the quadratic form as
$$
\mathfrak e_t[\phi] = \int_\Omega \left|\nabla(a^{-1/2}\phi)\right|^2 d\mu_t + r^{-2}\|\phi\|_{L^2(\nu_t)}^2.
\tag{2}
$$
This arises from the Sobolev substitution $u = a^{-1/2}\phi$ in $\|u\|_{L^4(\mu)}^2 \le A_0^2\,\mathfrak s[u]$, giving $\|\phi\|_{L^4(\nu)}^2 \le A_0^2\,\mathfrak e_t[\phi]$.

The Step 21 handoff erroneously wrote $\nabla(a^{-1}\phi)$ instead of $\nabla(a^{-1/2}\phi)$. The distinction matters near $a = 0$:
$$
|\nabla(a^{-1/2}\phi)|^2 = a^{-1}|\nabla\phi|^2 + O(a^{-2}|da|^2|\phi|^2 + a^{-1}|\phi||\nabla\phi|),
$$
$$
|\nabla(a^{-1}\phi)|^2 = a^{-2}|\nabla\phi|^2 + O(a^{-4}|da|^2|\phi|^2 + a^{-3}|\phi||\nabla\phi|).
$$
The latter has two powers of $a^{-1}$ in the leading term, giving falsely strong gradient control near $\{a=0\}$. Since $|da|^2/a = 4|d\chi|^2 \le C/r^2$ is bounded for $a = \chi^2$, the correct form (2) does not have a hidden singularity in the cross terms.

**All subsequent formulas must use $a^{-1/2}$, not $a^{-1}$.**

## 3. The essential mechanism: critical-to-subcritical upgrade

### Critical vs subcritical potentials in 4D

For the De Giorgi–Nash–Moser iteration on a 4-manifold, the potential $V$ enters through Hölder absorption. At the $k$-th Moser step from $L^{q_k}$ to $L^{q_{k+1}}$ with $q_{k+1} = 2q_k$, the potential must be in $L^{r_k}$ where
$$
\frac{1}{r_k} = \frac{1}{2} - \frac{1}{q_k}.
$$

As $k \to \infty$: $r_k \to 2$ from above. Therefore:
- If $V \in L^p$ with $p > 2 = n/2$ (**subcritical**): $V \in L^{r_k}$ for all $k$, and the Moser constants converge.
- If $V \in L^2$ only (**critical**): the estimates degenerate as $k \to \infty$, and the iteration may fail to produce an $L^\infty$ bound.

The Hardy potential $V = \kappa/|x|^2$ is exactly $L^2$-critical in 4D ($\int_{B_1}|x|^{-4}r^3\,dr$ diverges logarithmically), demonstrating that critical potentials can prevent ultracontractivity.

### The role of $H_3$

At time $t = 0$, the curvature potential $\mathcal K = aF$ is in $L^2(\nu)$ only (from $H_2 = \int \mathcal K^2\,d\nu < \infty$, bounded by Chern–Weil). This is the critical level.

The Wang hierarchy Step 20 establishes, conditionally on the energy inequality:
$$
H_3(t) = \int_\Omega \mathcal K^3\,d\nu_t \le \frac{C\gamma^3}{t},
\qquad t \in (0, \theta r^2].
\tag{3}
$$
This means $\mathcal K(t) \in L^3(\nu_t)$ at any positive time. Since $3 > 2 = n/2$, **the potential becomes subcritical at positive time**.

This is the essential upgrade. Once $\mathcal K \in L^3(\nu)$, the De Giorgi–Nash–Moser iteration from $L^3$ to $L^\infty$ has convergent constants, and a standard argument gives
$$
\|\mathcal K(t_0)\|_\infty \le C\|\mathcal K(t_0)\|_{L^2(\nu)}^{2/(2+\epsilon)}\|\mathcal K(t_0)\|_{L^3(\nu)}^{\epsilon/(2+\epsilon)} \cdot \text{(convergent product)}.
$$

## 4. Two-stage architecture

The corrected architecture has two stages with sharply different characters.

### Stage 1: Critical bootstrap $H_2 \to H_3$ (Essential, hard)

**Input:** Chern–Weil: $H_2(0) = \int F^2\,d\mu \le C(M)$, volume-independent $\beta = A_0^2\|F\|_2 = C\sqrt{\varepsilon_{\rm Li}}$.

**Mechanism:** The Wang-type energy inequality for $H_2$ under the cutoff flow $\partial_t g = -2a(\operatorname{Ric}+g)$:
$$
\frac{d}{dt}H_2 \le -cD_2 + C\,R_3 + \text{(lower order)},
\tag{4}
$$
where $D_2 = \int\eta^2 a|\nabla F|^2\,d\mu$ is the dissipation and $R_3 = \int\eta^2 a F^3\,d\mu = H_3$ is the cubic reaction.

The critical absorption step: define the Sobolev variable $v_2 = \eta a^{1/2}F$. Then
$$
\|\nabla v_2\|_2^2 \le C\left(D_2 + \frac{H_2}{r^2}\right),
\qquad
\|v_2\|_4^2 \le A_0^2 \left(\|\nabla v_2\|_2^2 + r^{-2}\|v_2\|_2^2\right).
$$
The gradient of $v_2$ satisfies $|\nabla v_2|^2 \le C(\eta^2 a|\nabla F|^2 + |d\chi|^2 F^2 + |\nabla\eta|^2 a F^2)$, using $|\nabla(a^{1/2})|^2 = |d\chi|^2 \le C/r^2$.

The reaction is then absorbed:
$$
R_3 \le H_2^{1/2}\cdot (H_4^{\rm out})^{1/2},
$$
where $H_4^{\rm out}$ uses outer cutoffs (A01 correction). Via Sobolev on the outer support:
$$
R_3 \le C\beta \left(D_2 + \frac{H_2}{r^2}\right) + \text{(finite-neighbor terms)},
$$
and for $\beta \ll 1$ the $D_2$ term is absorbed by the dissipation, giving:
$$
\frac{d}{dt}H_2 \le -\frac{c}{2}D_2 + C\frac{H_2}{r^2} + \text{(lower order + neighbor)}.
\tag{5}
$$
Time integration yields $H_2$ persistence and, combined with (4), the bound $H_3(t) \le C\gamma^3/t$.

**This is a SINGLE Moser step,** not an infinite iteration. It is the only step that requires the critical Sobolev absorption mechanism and is the genuine hard part of the PDE problem.

**Unresolved components:**
- Exact tensor weak inequality for the degenerate cutoff flow (the evolution of $|aF|^2$)
- Finite-neighbor outer cutoff bookkeeping (A01's correction: inner/outer cutoffs distinct)
- Evolving measure contribution (Step 21 correction: $|a\operatorname{tr}(E)| \le CaF$)
- Graph absorption for the energy ledger $S_\alpha' \le Cr^{-2}\sum_{\beta\sim\alpha}(A_\alpha/A_\beta)^4 S_\beta$
- Initial-time behavior and regularization at $a = 0$

### Stage 2: Subcritical closure $H_3 \to L^\infty$ (Standard, convergent)

**Input:** $H_3(t_0) \le C\gamma^3/t_0$ at some positive $t_0$.

**Mechanism:** The curvature potential is now in $L^3(\nu_{t_0})$, which is subcritical. The standard Moser iteration from $L^3$ to $L^{q_k}$ with $q_{k+1} = 2q_k$ (or $q_{k+1} = 3q_k/2$) has constants:
$$
\prod_{k=0}^\infty C_k^{1/q_k} = \exp\left(\sum_{k=0}^\infty \frac{\log C_k}{q_k}\right) < \infty,
$$
because $C_k$ grows at most polynomially in $k$ while $q_k$ grows geometrically.

**Output:** $|\chi^2\operatorname{Rm}(t_0)| \le C\gamma/t_0$ on the support of $\chi$. This is the weighted curvature bound (F4) from Step 21.

This stage is standard once Stage 1 is established. It can be expressed via explicit Moser iteration (the Step 20 $q \to 3q/2$ products, which now have convergent constants) or via Nash (which now works because the potential is subcritical). The choice is a matter of exposition, not substance.

### Defect hierarchy

The defect moments $J_m = \int\eta^2 a^{m-2}|E|^m$ follow the same pattern:
- **Starting data:** $J_6(0) \le C\delta^6 V$ (from initial pointwise pinching and the $a^4$ weight)
- **Curvature potential:** $H_3(t)$ from Stage 1
- **Integrability:** $m = 6 > 4 = 2n/2$ is already subcritical for the defect
- **Iteration:** Standard from $J_6$ to $J_\infty$ with convergent constants

The defect hierarchy is therefore entirely subcritical once the curvature Stage 1 is complete.

## 5. What Nash can and cannot do

### Cannot do: replace the critical $H_2 \to H_3$ step

The inverse-square counterexample shows that the critical form bound (1) does not imply ultracontractivity. The $H_2 \to H_3$ bootstrap requires the explicit Wang-type energy inequality, not an abstract semigroup estimate.

### Can do: simplify the subcritical $H_3 \to L^\infty$ stage

At positive time with $\mathcal K \in L^3(\nu)$, the perturbed form $\mathfrak e_t - \int\mathcal K\phi^2 d\nu$ is sectorial with form-relative bound zero (since $L^3 > L^2 = n/2$). Varopoulos-type ultracontractivity on the sub-Riemannian cusped domain $(\Omega, \hat g)$ would then give the $L^2 \to L^\infty$ bound in one step.

However, this is not strictly needed: the standard Moser iteration from $L^3$ to $L^\infty$ works with convergent constants and is more concrete. The Nash formulation may be cleaner for exposition but does not provide a shorter proof.

### Net assessment

The Nash route compresses the easy part (Stage 2) but cannot touch the hard part (Stage 1). The Wang-type weighted energy inequality for the single critical Moser step remains the essential PDE target.

## 6. Revised task list

After removing the incorrect Nash shortcut, the remaining tasks are:

**T1 (Critical, hard):** Derive the exact localized energy inequality for $H_2$ under the degenerate cutoff flow, with:
- Correct tensor evolution (Lichnerowicz + normalization + cutoff)
- Weighted dissipation $D_2 = \int\eta^2 a|\nabla F|^2 d\mu$
- Cubic reaction $R_3 = H_3$, absorbed by $\beta D_2$ with outer cutoffs
- Finite-neighbor graph system $S_\alpha' \le Cr^{-2}\sum_\beta S_\beta$
- Evolving measure correction $|a\operatorname{tr}(E)| \le CaF$

**T2 (Critical, hard):** Time integration of T1 to get $H_3(t) \le C\gamma^3/t$.

**T3 (Subcritical, standard):** Given $H_3$, subcritical Moser iteration to $|\chi^2\operatorname{Rm}| \le C\gamma/t$.

**T4 (Subcritical, standard):** Given $H_3$ and $J_6$, subcritical defect iteration to $|\chi^2 E| \le C\delta(r^2/t)^{1/3}$.

**T5 (Global, hard):** Triangular $Q$ system: $Q_\alpha' \le Cr^{-2}\sum Q_\beta$, using curvature absorption at small $\beta$.

**T6 (Qualitative):** Smooth continuation for each initial metric (Wang/DeTurck framework).

Tasks T3, T4 are standard given T1–T2. Tasks T1, T2, T5 are the genuine remaining work.

## 7. Files and verification

- Script: `workspace/scripts/verify_step22_inverse_square_and_subcritical.py` — verifies Hardy exponents, L² integrability, L∞ failure, critical/subcritical distinction, Moser constant convergence, and transcription correction.
- Step 20 weighted hierarchy: `workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md`
- Step 21 architecture: `workspace/notes/step21_derivative_free_first_exit_and_plateau_regularity.md`
- Step 21 corrections: `workspace/notes/step21_corrections_from_ttcs_and_peers.md`


## 8. TTCS corrections (Step 22)

The TTCS verification confirmed all five items with the following important corrections:

### 8.1. Hardy counterexample: L²_loc, not global L²
The singular solution $r^{-\sigma}$ is in $L^2_{\rm loc}(\mathbb R^4)$, not in $L^2(\mathbb R^4)$. The global behavior at infinity is irrelevant; the counterexample works locally. The critical reference is the on-diagonal heat kernel estimate (Milman–Semenov):
$$
p_t(x,x) \asymp t^{-2}\left(1 \wedge \frac{\sqrt{t}}{|x|}\right)^{2\sigma},
$$
which diverges as $x \to 0$ for any $\sigma > 0$, confirming $\|e^{-tH}\|_{L^2\to L^\infty} = \infty$.

Also: $r^{-\sigma}$ is not an eigenfunction (the spectrum is purely continuous on $\mathbb R^4$); it is the less-singular homogeneous harmonic function governing the near-origin heat kernel asymptotics.

### 8.2. Subcritical upgrade: the correct bound carries $A_0^4$
The Wang hierarchy gives $A_0^4 H_3(t) \le C\gamma^3/t$, not the simplified $H_3 \le C\gamma^3/t$. The Sobolev constant normalization is essential:
$$
\|\mathcal K\|_{L^3(\nu)}^3 = H_3 = \frac{A_0^4 H_3}{A_0^4} \le \frac{C\gamma^3}{A_0^4\,t}.
$$
For the subcritical form bound, we need:
$$
\int \mathcal K\phi^2\,d\nu_s \le \varepsilon\,\mathfrak e_s[\phi] + C\varepsilon^{-2}\frac{\gamma^3}{t}\|\phi\|_{L^2(\nu_s)}^2,
$$
using the $L^3$ interpolation (Sobolev + Hölder, with $\varepsilon$ chosen to decrease with Moser exponent).

### 8.3. Sobolev variable: missing $\eta^2$ and conformal-Hardy term
The gradient expansion should carry $\eta^2$:
$$
|\nabla v|^2 = \eta^2 a|\nabla F|^2 + \eta^2|\nabla\chi|^2 F^2 + aF^2|\nabla\eta|^2 + \text{cross terms}.
$$
The conformal-Hardy zero-order term in the quadratic form is:
$$
\frac{1}{4}a^{-3}|\nabla a|^2\phi^2 = a^{-2}|\nabla\chi|^2\phi^2,
$$
which has a genuine $a^{-2}$ singularity. However, when $\phi = \eta\mathcal K = \eta\cdot aF$, we have $a^{-1/2}\phi = v = \eta\chi F$, and the term reduces to $|\nabla\chi|^2 F^2$, which is bounded. So the singularity is "screened" by the natural test function.

### 8.4. Outer cutoff: graph mechanism algebraically correct but not yet proved
The Cauchy–Schwarz factoring and bounded-degree graph absorption are algebraically valid. The TTCS confirmed that for graph degree $N$ and small $\beta_*$, the condition $CN\beta_* < c/2$ suffices. But the complete normalized-flow tensor inequality, nested cutoff family, and finite-neighbor bookkeeping have not been assembled into a closed proof.

### 8.5. Mass term: valid enlargement
The lower-order term $r^{-2}\int a^{-1}\phi^2\,d\mu \le r^{-2}\|\phi\|_{L^2(\nu)}^2$ is a legitimate enlargement (since $a \le 1$), not an exact identity. This is consistent with using the $L^2(\nu)$ norm for the quadratic form.

## 9. Positive-branch observation (A02 Step 24)

A02 identified that codimension-1 positive Einstein collapse is NOT generally obstructed in dimensions $n \ge 5$. The KK construction: for $B = S^2_{\mathrm{Ric}=2} \times N^d_{\mathrm{Ric}=1}$ with $d \ge 2$ and a unit harmonic 2-form $\phi = \sqrt{2}\,\omega_{S^2}$, the circle bundle $L(q,1) \times N^d$ admits exact Ric $= g$ metrics with fiber length $t = \sqrt{2}/q \to 0$. This gives collapsing positive Einstein metrics in every dimension $n = d+3 \ge 5$.

In dimension 4, this requires $\mathrm{Ric}_{S^1} = g$, which is impossible, matching the Bochner obstruction. So the collapse character of the positive branch is:
- $n = 4$: positive collapse blocked (codim-1 Bochner)
- $n \ge 5$: positive collapse compatible (KK models exist)

**Consequence for Yau 26:** The positive branch in dimensions $\ge 5$ cannot rely on a collapse obstruction to force Einstein existence. Either a fundamentally different mechanism is needed, or the positive branch of Yau 26 may actually fail in high dimensions.
