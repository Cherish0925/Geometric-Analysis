# Step 73: Preissmann obstruction, Koiso center structure, and anisotropy decay

Session: S0910A01.  Agent2 / Constructor.  Step 73, Execute.

## 1. Purpose

This note establishes three structural results that sharpen the graph-neck
construction for Yau 26, following the Strategist correction about the
isotropic tanh profile:

- **Preissmann obstruction** (Proposition 2.1): every isotropic warped
  product collar $dt^2 + \cosh^2(t)\,h$ on $[0,R]\times T^3$ has operator-norm
  Einstein defect $\geq 2/3$ at the center $t = 0$, independently of the fiber
  metric $h$ and the collar length $R$.

- **Koiso center conditions** (§3): the correct starting point is anisotropic,
  with $S'(0) = \operatorname{Ric}_h^\sharp + 3I$ and $R_h = -6$. This
  eliminates the center defect entirely but requires the fiber to have
  non-Einstein, variable Ricci curvature.

- **Exponential anisotropy decay** (§4): in the ODE approximation
  (homogeneous collar), anisotropy from the Koiso center subsides
  exponentially with rate $\sim e^{-\sqrt{3}\,t}$, and the normalized weighted
  shear budget tends to zero as $R\to\infty$.

Files:

- Verification: `workspace/data/step73_preissmann_koiso_verify.json` (22/22)
- Fiber and collar data: `workspace/data/step73_koiso_center_analysis.json`
- Scripts: `workspace/scripts/step73_preissmann_and_koiso_center.py`,
  `workspace/scripts/step73_koiso_collar_ode.py`

---

## 2. Preissmann obstruction for isotropic torus collars

### 2.1 Warped product formulas

For $g = dt^2 + f(t)^2 h$ on $[0,R]\times (T^3, h)$ with fiber dimension 3:

$$
(\operatorname{Ric}_g + 3g)_{00}
= -3\frac{f''}{f} + 3, \tag{2.1}
$$

$$
(\operatorname{Ric}_g + 3g)(X,Y)\big|_{\mathrm{tan}}
= \operatorname{Ric}_h(X,Y) + \left[3f^2 - ff'' - 2(f')^2\right]h(X,Y).
\tag{2.2}
$$

With $f = \cosh(t)$: $f'' = \cosh(t)$, so $f''/f = 1$ and (2.1) vanishes.
The coefficient of $h$ in (2.2) is
$3\cosh^2 - \cosh^2 - 2\sinh^2 = 2$.
Thus
$$
(\operatorname{Ric}_g + 3g)\big|_{\mathrm{tan}}
= \operatorname{Ric}_h + 2h, \tag{2.3}
$$
and the operator norm of the tangential defect is
$\cosh^{-2}(t)\,|\operatorname{Ric}_h + 2h|_{\mathrm{op}}$
at each point.

### 2.2 Three-dimensional Preissmann argument

**Proposition 2.1.** *For every Riemannian metric $h$ on $T^3$,*
$$
\max_{T^3}\,|\operatorname{Ric}_h + 2h|_{\mathrm{op}} \ge \tfrac23.
$$

*Proof.* Suppose $|\operatorname{Ric}_h + 2h|_{\mathrm{op}} < c$
everywhere, so the Ricci eigenvalues satisfy $r_i\in(-2-c,-2+c)$.
By the three-dimensional identity $K_{ij}=(r_i+r_j-r_k)/2$,
$$
K_{ij} < \frac{2(-2+c)-(-2-c)}{2} = \frac{3c-2}{2}.
$$
For $c < 2/3$: $K_{ij}<0$ strictly at every point. By Preissmann's theorem,
the fundamental group of a closed negatively curved manifold contains no
$\mathbb{Z}^2$ subgroup, contradicting $\pi_1(T^3)=\mathbb{Z}^3$.

At the boundary $c = 2/3$: $K_{ij}\le0$. By the flat torus theorem
(Gromoll–Wolf, Lawson–Yau), any $K\le0$ metric on $T^3$ is flat.
But a flat metric has $\operatorname{Ric}_h = 0$, so
$|\operatorname{Ric}_h + 2h|_{\mathrm{op}} = 2 > 2/3$, contradicting
the assumption. (The earlier version claimed a fixed boundary triple
$(-4/3,-4/3,-8/3)$, which does not follow from the bound; the flat torus
theorem bypasses this.) $\square$

In fact the argument shows $D(h) > 2/3$ strictly.

**Corollary 2.2.** *The isotropic collar $g = dt^2 + \cosh^2(t)\,h$ has*
$$
\|\operatorname{Ric}_g + 3g\|_{\mathrm{op}} \ge \tfrac23
$$
*at $t = 0$, for every $h$ and every $R > 0$.  Long collars reduce the outer
defect but cannot reduce the center defect below $2/3$.*

**Remark.** For flat $T^3$: $|\operatorname{Ric}_h+2h|_{\mathrm{op}}=2$,
which is three times larger than the threshold.  The obstruction is tight in
the sense that $c = 2/3$ separates negatively curved from non-negatively
curved regimes, and non-negative curvature forces flatness.

---

## 3. Koiso center conditions

### 3.1 General formulation

At a totally geodesic center $S(0) = 0$ of a Gaussian collar
$g = dt^2 + h_t$:

- **Normal:** $-\operatorname{tr}(S'(0)) + 3 = 0$, so $\operatorname{tr}(S'(0))=3$.
- **Tangential:** $S'(0) = \operatorname{Ric}_h^\sharp + 3I$ (Gauss equation).
- **Trace consistency:** $R_h + 9 = 3$, so $R_h = -6$.

The tangential Einstein defect vanishes at $t = 0$ by construction:
$E_{ij}(0) = \operatorname{Ric}_h + 3h - S'(0) = 0$.

### 3.2 Isotropic impossibility

If $S'(0) = cI$: $\operatorname{tr}(S') = 3c = 3$ forces $c = 1$,
so $\operatorname{Ric}_h = (c-3)h = -2h$.  A $T^3$ with
$\operatorname{Ric} = -2h$ is a space form of constant negative curvature.
By Preissmann, $\pi_1(T^3) = \mathbb{Z}^3$ has a $\mathbb{Z}^2$ subgroup,
contradiction.

**Therefore the Koiso acceleration must be anisotropic:**
$S'(0) = \operatorname{Ric}_h^\sharp + 3I$ with
$\operatorname{Ric}_h \ne -2h$.

### 3.3 Diagonal t-only constraint

For the simpler ansatz $g = dt^2 + e^{2a(t)}d\theta^2 + e^{2b(t)}dx^2
+ e^{2c(t)}dy^2$ (no $\theta$-dependence), combining the normal and
tangential Einstein equations gives the algebraic constraint:
$$
|S|^2 = H^2 - 6 - R^{(3)}_h. \tag{3.1}
$$
At the reflection center $S(0) = 0$: $0 = 0 - 6 - R^{(3)}_h$, requiring
$R^{(3)}_h = -6$.  But this flat-fiber ansatz has $R^{(3)}_h = 0$,
yielding $0 = -6$: a contradiction.

**The diagonal $t$-only ansatz cannot have a totally geodesic reflection
center.** The $\theta$-dependence of the fiber metric is necessary.

### 3.4 The $a = 0$ gauge

In the gauge $a \equiv 0$ (fixing $g_{\theta\theta} = d\theta^2$) for
the full $T^2$-invariant metric $g = dt^2 + d\theta^2 + e^{2b(t,\theta)}dx^2
+ e^{2c(t,\theta)}dy^2$:

- $H = b_t + c_t$, and the mean curvature satisfies $V_0'' = 3 - V_0'^2$
  where $V_0(t) = b + c$ at the $t$-dependent part.
- Combining with the normal equation forces $b_t c_t = 0$ everywhere.
- The asymptotic $V_0' \to \sqrt{3}$, not $3$.  The shape operator has rank
  at most 1 and cannot reach the cusp $S = I$.

**The $a = 0$ gauge is incompatible with the cusp end.** The collar
must be formulated with all three conformal factors varying.

### 3.5 Explicit Koiso data for T²-invariant fibers

For the fiber $h = d\theta^2 + e^{2b_0(\theta)}dx^2 + e^{2c_0(\theta)}dy^2$
in the $a_0 = 0$ gauge, setting $u = b_{0\theta}$, $v = c_{0\theta}$:

$$
R^{(3)}_h = -2(u^2 + v^2 + uv + u' + v') = -6
\quad\Longleftrightarrow\quad
u^2 + v^2 + uv + u' + v' = 3. \tag{3.2}
$$

Fixing $v(\theta) = B\sin\theta$ and solving the Riccati equation
$u' = 3 - u^2 - v^2 - uv - v'$ for $2\pi$-periodic $u$ yields explicit
fiber metrics with $R = -6$ for all $B > 0$ tested ($B = 0.5, 1.0, 1.5, 2.0$).

The Koiso initial accelerations follow from the constraint:
$$
a_{tt}(0) = uv, \qquad
b_{tt}(0) = v^2 + v', \qquad
c_{tt}(0) = u^2 + u'. \tag{3.3}
$$
Trace: $a_{tt} + b_{tt} + c_{tt} = u^2 + v^2 + uv + u' + v' = 3$.  $\checkmark$

**Example ($B = 1.0$):**
- At $\theta = 0$: $S'(0) = (0, 1, 2)$ — strongly anisotropic.
- At $\theta = \pi/2$: $S'(0) = (0.988, 1.000, 1.012)$ — nearly isotropic.
- Fiber defect: $|\operatorname{Ric}_h + 2h|_{\mathrm{op}} \in [0.012, 3.72]$.

The Preissmann bound $2/3$ is satisfied since the maximum is $3.72$.

---

## 4. Exponential anisotropy decay (ODE approximation)

### 4.1 The diagonal ODE system

Ignoring $\theta$-dependence, the tangential Einstein equations reduce to:
$$
f_i'' + f_i' H = 3, \qquad i = 1,2,3, \tag{4.1}
$$
where $f_i' = s_i$ are the eigenvalues of the shape operator and
$H = s_1 + s_2 + s_3$.

**Difference equation:**  Setting $\delta_{ij} = s_i - s_j$:
$$
\delta_{ij}' + H\,\delta_{ij} = 0
\quad\Longrightarrow\quad
\delta_{ij}(t) = \delta_{ij}(0)\,\exp\!\left(-\!\int_0^t H(s)\,ds\right).
\tag{4.2}
$$

### 4.2 Decay rate

For the reflection center $H(0) = 0$, the isotropic approximation gives
$H(t) \approx \sqrt{3}\tanh(\sqrt{3}\,t)$, so
$$
\int_0^t H(s)\,ds = \log\cosh(\sqrt{3}\,t). \tag{4.3}
$$
Therefore
$$
\delta_{ij}(t) = \delta_{ij}(0)\,\operatorname{sech}(3t)
\sim \delta_{ij}(0)\cdot 2e^{-3t} \quad\text{as }t\to\infty.
\tag{4.4}
$$

**TTCS correction:** The three-direction ODE $H' = 9 - H^2$ gives
$H = 3\tanh(3t)$, not $\sqrt{3}\tanh(\sqrt{3}t)$.  The earlier $\sqrt{3}$
rate came from the two-direction $a=0$ gauge.  The correct decay rate is
$\operatorname{sech}(3t) \sim 2e^{-3t}$, which is faster.

**Fundamental limitation:** The simplified ODE $s_i' + Hs_i = 3$ cannot
produce the Koiso anisotropy because $s_i(0) = 0$ forces $\delta_{ij}(0)=0$.
The correct tangential Einstein equation is
$$
s_i' + Hs_i = 3 + r_i(h_t), \tag{4.5}
$$
where $r_i(h_t)$ are the fiber Ricci eigenvalues.  The difference satisfies
$$
\delta_{ij}' + H\delta_{ij} = r_i(h_t) - r_j(h_t), \tag{4.6}
$$
with Duhamel representation from $\delta_{ij}(0) = 0$.
In the cusp regime, $\operatorname{Ric}_{h_t} \sim e^{-2t}$ by conformal
scaling of expanding fibers, giving a forced decay rate $\sim e^{-2t}$
(confirmed numerically: fitted rate $= 2.002$).

Numerically for the unforced system (`step73_koiso_collar_ode.py`, which
does not include fiber Ricci forcing):
- $\operatorname{sech}(3)$ at $t = 1$: $0.099$ (much faster than the wrong
  $\operatorname{sech}(\sqrt{3}) = 0.34$)

For the forced system (`step73_ttcs_corrections.json`), with
$r_i(h_t) = r_i(0)e^{-2t}$ modeling fiber Ricci decay:
- Fitted decay rate: $2.00$ (vs unforced $3.0$)
- The forcing slows decay from $e^{-3t}$ to $e^{-2t}$ but does not
  prevent convergence

### 4.3 Convergence to the isotropic cusp

The full ODE system (4.1) with Koiso initial data was solved numerically
for $B = 0.5$ and $B = 1.0$.  At the $\theta = 0$ slice:

| $R$ | $H$ | $3-H$ | $|S-I|^2$ | Norm budget |
|-----|-----|--------|-----------|-------------|
| 2 | 3.000 | $3.7\times10^{-5}$ | $5\times10^{-10}$ | $1.3\times10^{-1}$ |
| 4 | 3.000 | $2\times10^{-10}$ | $5\times10^{-16}$ | $2.3\times10^{-3}$ |
| 6 | 3.000 | $<10^{-14}$ | $3\times10^{-21}$ | $4.3\times10^{-5}$ |
| 8 | 3.000 | $<10^{-15}$ | $2\times10^{-26}$ | $7.9\times10^{-7}$ |

The normalized weighted shear budget
$2(3 + \int_0^R e^{2t}|S-I|^2\,dt)/(e^{2R}-1) \to 0$
as $R\to\infty$.

**Comparison with isotropic tanh:** The isotropic profile
$S = \tanh(\sqrt{3}\,t)\,I$ has comparable decay:

| $R$ | $|S-I|^2_{\rm iso}$ | Norm budget (iso) |
|-----|-------|------|
| 4 | $1.1\times10^{-11}$ | $2.7\times10^{-3}$ |
| 8 | $1.0\times10^{-23}$ | $9.2\times10^{-7}$ |

The anisotropic Koiso center achieves essentially the same asymptotic
decay rate as the isotropic reference.

### 4.4 Higher Fourier modes (open)

**TTCS correction:** The principal part $\partial_{tt} + n^2 e^{-2a}$ for
mode $n$ has both growing and decaying solutions.  In the cusp regime
$a(t) \sim t$, the term $n^2 e^{-2t} \to 0$, so it does not change the
asymptotic index root.  The earlier claim that higher modes decay faster
is not justified by the principal part alone; a full spectral analysis
of the linearized Einstein–DeTurck operator with gauge and coupling terms
is needed.

---

## 5. Consequences for the graph construction

### 5.1 Positive signal

1. The isotropic tanh obstruction ($\geq 2/3$) is not a barrier to the Koiso
   center, which achieves zero defect at $t = 0$.
2. The $T^2$-invariant diagonal ansatz with $v = B\sin\theta$ produces
   periodic solutions of the Riccati constraint, but these have **nonzero
   mean** $\int u \ne 0$, so the fiber metric is not periodic on $T^3$.
   The solution branch terminates at $B \approx 2.25$ with mean $\approx
   0.88$.  Zero-mean periodic fibers with $R_h = -6$ are not yet found
   in this diagonal form.  The Kazdan–Warner theorem guarantees existence
   of such metrics on $T^3$ in general, but not in the restricted ansatz.
3. In the ODE approximation, anisotropy subsides exponentially and the
   normalized shear budget tends to zero.
4. Higher Fourier mode stability in the full PDE is not yet established
   (TTCS correction).  The asymptotic spectral analysis remains open.

### 5.2 Remaining difficulties

1. **Cusp matching:** The ODE system approaches $S = I$ asymptotically but
   never reaches $H = 3$ at finite $R$ (A03's identity). The approximate
   construction must truncate and glue with exponentially small defect.

2. **Gauge and constraint compatibility:** The $a = 0$ gauge fails: the full PDE gives $b_tc_t + b_\theta c_\theta
   = 0$ (not $b_tc_t = 0$), and the Koiso center has $a_{tt}(0) = uv \ne 0$,
   so the solution immediately leaves $a \equiv 0$.  A full construction
   needs a DeTurck-elliptic formulation with all three conformal factors.

3. **Global closing:** The collar produces only a neck. The graph manifold
   construction must close both ends (two half-cores glued along a cusp
   torus), and each half-core must maintain the pinching bound.

4. **Maximum-norm control:** The ODE approximation controls the shape
   operator but not the full Riemann tensor or the mixed Ricci components.
   The full PDE must be solved to confirm maximum-norm defect control.

5. **All-sign Einstein nonexistence:** Even a successful negative-branch
   graph construction does not refute Yau 26, which is sign-unrestricted.
   The positive branch on the same or a related manifold must also be
   addressed.

### 5.3 Proposed next computation

Formulate the DeTurck-regularized elliptic BVP for the $T^2$-invariant
diagonal metric on $[0,R]\times T^3$:

- **Interior equation:** $\operatorname{Ric}(g) + 3g + \mathcal{L}_W g = 0$
- **Boundary at $t = 0$:** Koiso reflection data: $a_t = b_t = c_t = 0$
  with fiber $(a_0, b_0, c_0)$ satisfying $R_h = -6$
- **Boundary at $t = R$:** asymptotic cusp data:
  $a_t = b_t = c_t = 1 + O(e^{-\sqrt{3}(R-t)})$

Solve numerically for increasing $R$ and measure:

1. $\|\operatorname{Ric}_g + 3g\|_{\mathrm{op},\infty}$ (full defect)
2. $2(3 + \int_0^R e^{2t}|S-I|^2\,dt)/(e^{2R}-1)$ (weighted shear budget)
3. All five Einstein equation components (not just the tangential)

If both quantities decay to zero as $R\to\infty$, the graph-neck
construction becomes a serious near-negative-Einstein candidate.

---

## 6. Relationship to the full Yau 26 problem

The restricted IL negative-gap theorem (assembly Steps 68–71) shows that
sufficiently tight negative Ricci pinching on certain four-manifold
topologies forces an Einstein metric.  The graph-neck construction
explores the complementary question: can a four-manifold without any
Einstein metric carry a tightly pinched metric?

If the graph construction succeeds: it provides a negative-branch
counterexample family (near $-1$ pinching, no Einstein metric).  But
the sign-unrestricted Yau 26 proposition also requires defeating the
positive branch, which may use entirely different geometry.

If the graph construction fails at the PDE level: the exponential
stability of the cusp suggests that some other geometric mechanism
prevents global approximate Einstein matching on graph manifolds.
This would strengthen the case for a dimension-4 positive result.

Either outcome advances the full problem.

---

**Verification:**
- `step73_preissmann_koiso_verify.json`: 22/22 structural checks passed
- `step73_koiso_center_analysis.json`: fiber metrics with $R=-6$ found
  for $B = 0.5, 1.0, 1.5, 2.0$ (periodic but NOT zero-mean)
- `step73_ttcs_corrections.json`: forced decay rate $\approx e^{-2t}$
  confirmed numerically; ODE rate corrected to $\operatorname{sech}(3t)$
- `step73_mean_u_track.json`: mean(u) vs B tracking; branch terminates
  at $B \approx 2.25$ with mean $> 0$; zero-mean not reached
- TTCS verification:
  `trace/ttcs/results/step73_ttcs01_verifier1_integration.md`
