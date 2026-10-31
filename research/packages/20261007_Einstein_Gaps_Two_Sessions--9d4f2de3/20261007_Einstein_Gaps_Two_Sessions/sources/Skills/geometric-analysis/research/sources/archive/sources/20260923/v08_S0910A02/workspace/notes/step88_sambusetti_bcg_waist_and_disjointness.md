# Step 88: Sambusetti–BCG entropy obstruction, warped-product waist barrier, and resolution/simplicial-volume disjointness

Session `S0910A02`, Agent2/Constructor, Step 88.

This note records three structural results that reshape the negative-branch landscape of Yau–26 in dimension four: (1) the Sambusetti–BCG all-sign no-Einstein family and its quantitative pinching threshold, (2) a pointwise waist obstruction preventing warped-product near-pinching on connected sums, and (3) the decisive topological question about whether any A₁-resolution can access the entropy-obstructed reservoir.

---

## 1. Sambusetti–BCG all-sign no-Einstein family

**Sources.** LeBrun's footnote in `Knowledge/objects/papers/Four-Manifolds-without-Einstein-Metrics--5b090e14de27--d63c56d541e8/object.md`, lines 269–270; Kotschick `Knowledge/objects/papers/Entropies-Volumes-and-Einstein-Metrics--a5cc2bf9d68e--94203f883336/object.md`, Theorem 1 and Corollary 3 (lines 156–226); Bessières–Besson–Courtois–Gallot `Knowledge/objects/papers/Differentiable-rigidity-under-Ricci-curvature-lower-bound--cfb4c9cdd3c7--65a5a48bd00c/object.md`, Theorems 1.1, 1.5, Corollary 1.7. The primary Sambusetti source (Math. Ann. 311, 1998, 533–547, DOI 10.1007/s002080050199) was not fully retrieved.

**Setup.** Let $N^4$ be a closed oriented real-hyperbolic 4-manifold with sectional curvature $-1$:
$$
\operatorname{Ric}_{g_0} = -3g_0, \qquad
\operatorname{Vol}(N,g_0) = \frac{4\pi^2}{3}\chi(N), \qquad
\tau(N) = 0.
$$
The connected sum $M_N = N \# N$ has:
$$
\chi(M_N) = 2\chi(N) - 2, \qquad
\tau(M_N) = 0, \qquad
\|M_N\| = 2\|N\| > 0.
$$
There is a degree-two continuous map $f: M_N \to N$ obtained by collapsing one punctured summand to a point and mapping the other by the identity.

**Theorem (Sambusetti, via Kotschick/BCG).** *$M_N$ admits no Einstein metric of any sign.*

*Proof.* By Kotschick Corollary 3, any closed oriented Einstein 4-manifold $X$ admitting a nonzero-degree map $f: X \to Y$ to a closed real-hyperbolic manifold $Y$ satisfies:
$$
\chi(X) \ge \frac{3}{2}|\sigma(X)| + |\deg f| \, \chi(Y),
$$
with equality only if $X$ is real-hyperbolic. For $M_N$ with $\deg f = 2$:
$$
2\chi(N) - 2 \ge 0 + 2\chi(N)
$$
is impossible. $\square$

**Observations.** (a) This is NOT a gauge-theoretic obstruction: it uses the Besson–Courtois–Gallot entropy inequality and homotopy degree, not monopole classes, SW invariants, or BF invariants. (b) The family has $\chi > 0$, $\tau = 0$, and strict Hitchin–Thorpe $(2\chi - 2 > 3|\tau| = 0)$ for $\chi(N) \ge 2$. (c) The manifolds are not simply connected: $\pi_1(M_N)$ is a free product with one relation from the hyperbolic lattice. (d) The positive simplicial volume $\|M_N\| > 0$ obstructs $\lambda \ge 0$ independently: any metric with $\operatorname{Ric} \ge 0$ forces simplicial volume zero by the Cheeger–Gromoll/Bishop–Gromov mechanism, contradicting $\|M_N\| > 0$.

---

## 2. BCG extension to Ricci-lower-bound metrics and quantitative pinching threshold

**Theorem (BCG lower bound, metric-level).** For any metric $g$ on $M_N$ with $\operatorname{Ric}_g \ge -(n-1)g$ (with $n = 4$: $\operatorname{Ric}_g \ge -3g$):
$$
\operatorname{Vol}(M_N, g) \ge 2 \, \operatorname{Vol}(N, g_0).
$$
Equality implies $g$ is isometric to $g_0$ on each summand. Corollary 1.7 of BBCG: for fixed $N$, there exists $\varepsilon_N > 0$ such that
$$
\operatorname{Vol}_g(M_N) \ge 2(1 + \varepsilon_N) \operatorname{Vol}(N)
$$
for all metrics with $\operatorname{Ric}_g \ge -3g$.

**Source:** BBCG Theorem 1.5 (lines 67–81) and Corollary 1.7 (lines 91–99). This uses only $\operatorname{Ric} \ge -3g$, not the Einstein equation.

**CGB upper bound under two-sided negative Ricci pinching.** Suppose
$$
-3(1+\varepsilon)g \le \operatorname{Ric}_g \le -3(1-\varepsilon)g, \qquad 0 < \varepsilon < 1.
$$
Let $r_i = -3x_i$ be the Ricci eigenvalues with $x_i \in [1-\varepsilon, 1+\varepsilon]$. The CGB integrand satisfies:
$$
\frac{s^2}{6} - \frac{|\operatorname{Ric}|^2}{2}
= \frac{3}{2}\bigl[(\textstyle\sum x_i)^2 - 3\sum x_i^2\bigr].
$$
This quadratic is concave in each variable; its minimum on the box $[1-\varepsilon, 1+\varepsilon]^4$ occurs at the vertex $x_1 = \cdots = x_4 = 1-\varepsilon$ for $\varepsilon \le 1/2$, giving:
$$
\frac{s^2}{6} - \frac{|\operatorname{Ric}|^2}{2} \ge 6(1-\varepsilon)^2.
$$
(Note: A01's message #610–611 uses an intermediate formula $(3/2)[(\sum x)^2/3 - \sum x^2]$, which has a factor-of-3 error in the first term. The final bound $6(1-\varepsilon)^2$ is nevertheless correct. See `workspace/data/step88_warped_waist_and_bcg_threshold.json`.)

**CGB gives:**
$$
8\pi^2(2\chi(N)-2) \ge 6(1-\varepsilon)^2 \operatorname{Vol}(M_N, g),
$$
hence
$$
\operatorname{Vol}(M_N, g) \le \frac{2\operatorname{Vol}(N)(1 - 1/\chi(N))}{(1-\varepsilon)^2}.
$$

**Rescaling for BCG.** If $\|\operatorname{Ric}_g + 3g\|_{\mathrm{op}} \le \delta$, set $\varepsilon = \delta/3$. Then $\operatorname{Ric}_g \ge -(3+\delta)g$. Scale $\hat g = (1 + \delta/3)g$: then $\operatorname{Ric}_{\hat g} = \operatorname{Ric}_g \ge -3\hat g$ and $\operatorname{Vol}_{\hat g} = (1+\delta/3)^2 \operatorname{Vol}_g$.

BCG lower bound applied to $\hat g$:
$$
\operatorname{Vol}_g \ge \frac{2\operatorname{Vol}(N)}{(1+\varepsilon)^2}.
$$

**Volume incompatibility.** The lower and upper bounds are incompatible when:
$$
\left(\frac{1-\varepsilon}{1+\varepsilon}\right)^2 > 1 - \frac{1}{\chi(N)}.
$$

**Threshold:**
$$
\varepsilon < \varepsilon_\chi := \frac{1 - \sqrt{1 - 1/\chi(N)}}{1 + \sqrt{1 - 1/\chi(N)}} = \frac{1}{4\chi(N)} + O(\chi(N)^{-2}).
$$
In operator norm: $\delta < 3\varepsilon_\chi \approx \frac{3}{4\chi(N)}$.

**Meaning.** This is an additive certificate: the volume deficit arises from the constant $\chi(M_N) = 2\chi(N) - 2$ versus $2\chi(N)$, an additive gap of 2. No additive certificate can produce a uniform $\delta_0 > 0$ independent of $N$, because the critical rate goes to zero as $\chi(N) \to \infty$. This means the entropy obstruction *prices* a refutation of $P_4^-$ at rate $O(1/\chi)$ but cannot *close* the branch.

**Weyl budget at critical rate:** when $\delta \sim 1/\chi(N)$, the Weyl curvature integral satisfies $\int |W|^2 = O(1)$, an extremely tight scale-invariant budget.

---

## 3. Warped-product waist obstruction

**Theorem (waist barrier, $k \ge 0$).** *For a warped product $g = dr^2 + f(r)^2 g_F$ on $\mathbb{R} \times F^3$ with $\operatorname{Ric}_F = 2k\, g_F$ and $k \ge 0$ (flat or positively curved fiber): at any waist $r_0$ where $f'(r_0) = 0$, $f''(r_0) \ge 0$, the Ricci endomorphism defect from $-3$ satisfies*
$$
\delta := \max\bigl(|\lambda_r + 3|, |\lambda_F + 3|\bigr) \ge \frac{3}{2},
$$
*with equality if and only if $k = 0$ and $f''(r_0)/f(r_0) = 3/2$.*

*Proof.* At the waist, the Ricci endomorphism eigenvalues are:
$$
\lambda_r = -3\alpha, \qquad \lambda_F = \beta - \alpha,
$$
where $\alpha = f''/f \ge 0$ and $\beta = 2k/f^2 \ge 0$. The defects from $-3$ are:
$$
\delta_r = 3|1 - \alpha|, \qquad \delta_F = |3 - \alpha + \beta|.
$$
For $\alpha \le 1$: $\delta_F = 3 - \alpha + \beta \ge 2$ (since $\beta \ge 0$, $\alpha \le 1$).
For $1 \le \alpha \le 3$: equalize $3(\alpha - 1) = 3 - \alpha + \beta \Rightarrow \alpha = (6 + \beta)/4$, $\delta = 3(\beta + 2)/4$. For $\beta = 0$: $\alpha = 3/2$, $\delta = 3/2$. For $\beta > 0$: $\delta > 3/2$.
For $\alpha > 3$: $\delta_r > 6$ and $\delta_F = \alpha - 3 + \beta - \alpha = \beta - 3$ or $3 - \alpha + \beta < 0$... In fact, for $\alpha > 3$ and $\beta \ge 0$: $\delta_r = 3(\alpha - 1) > 6$, always worse.

Hence $\inf_{\alpha \ge 0, \beta \ge 0} \delta = 3/2$, achieved at $\alpha = 3/2$, $\beta = 0$.

For the round $S^3$ fiber ($k = 1$): $\beta = 2/f_0^2 > 0$, so $\delta = 3/2 + 3/(2f_0^2) > 3/2$, approaching $3/2$ only as $f_0 \to \infty$.

*Check.* Hyperbolic $\mathbb{H}^4$ in equidistant coordinates from $\mathbb{H}^3$: $f(r) = \cosh r$, $k = -1$, $\beta = -2$, $\alpha = 1$ at $r = 0$. Then $\lambda_r = -3$, $\lambda_F = -2 - 1 = -3$. Zero defect. $\checkmark$

*Check.* The cusp metric $f(r) = e^{-r}$, $k = 0$: $\alpha = 1$, $\beta = 0$, $(f'/f)^2 = 1$. $\lambda_r = -3$, $\lambda_F = 0 - 1 - 2 = -3$. Zero defect, but no waist (monotone $f$). $\checkmark$ $\square$

**Implication for connected-sum necks.** A connected sum $N \# N$ where $N$ is a closed hyperbolic 4-manifold has a separating $S^3$ waist (round fiber, $k = 1$). The waist barrier gives $\delta > 3/2$ at any warped-product turnaround, regardless of scale. This is a **pointwise** obstruction: it cannot be amortized over large volume, unlike the CGB energy accounting. It explains why A03's monotone-functional search found no construction: in the warped-product class, a cusp-to-cusp turnaround through $S^3$ or $T^3$ is locally forbidden below $\delta = 3/2$.

**General (non-warped) waists.** For a minimal separating hypersurface $\Sigma^3$ in $(M^4, g)$ with $\operatorname{Ric} \approx -3g$, the traced Gauss equation gives:
$$
\operatorname{Scal}_\Sigma = -6 - |A|^2 + O(\delta).
$$
This does not yield a contradiction since any closed 3-manifold admits metrics of arbitrarily negative scalar curvature. A general "no near-pinched $S^3$ or $T^3$ waist" theorem would be a stronger statement and would kill both known negative reservoirs (LeBrun blow-ups and Sambusetti sums are both connected sums).

---

## 4. Chern–Weil neutrality and entropy inaccessibility

*Corrected in Step 90. The original Step 88 §4.1 incorrectly claimed the negative mirror has infinite $\pi_1$ with abelianization $(\mathbb{Z}/2)^8$. Step 57 van Kampen proves all fillings are simply connected. The entropy-access criteria of §4.2–4.3 are superseded by the BCG inaccessibility theorem below.*

### 4.1 Correction: both mirrors are simply connected

Step 57 proved by van Kampen that every sign-pattern filling of both mirrors is simply connected. Each EH cap has $\pi_1(\mathrm{EH}) = 1$ and kills the $\mathbb{Z}/2$ peripheral group of the $\mathrm{RP}^3$ boundary. With many stabilizer normal closures, the filling relations annihilate all remaining torsion — the same mechanism that makes Kummer K3 simply connected from $T^4/\mathbb{Z}_2$ with 16 nodes.

The coinvariant-only shortcut omitted 35 (resp. 3) extra filling relations. The self-contradiction was visible: if $\iota_*$ inverts every element, then every element in the coinvariant quotient satisfies $\gamma = \gamma^{-1}$, making it abelian and finite — and the filling relations collapse it to the trivial group.

**Standing caution (seam compression).** $\mathrm{RP}^3$ boundaries are amenable seams. Filling them with simply-connected EH caps compresses the fundamental group. The relative simplicial volume $\|(X_0, \partial X_0)\|$ of the complement may be positive, but amenable-boundary additivity requires $\pi_1$-injective seams. EH caps violate this, so $\|M\| = 0$ despite $\|(X_0, \partial)\| > 0$. Sources: Bargagnati–Frigerio Proposition 2.3; Bucher–Burger–Frigerio–Iozzi–Pagliantini–Pozzetti Theorem 2.1.

### 4.2 Chern–Weil neutrality of Ricci-flat ALE bubbles

**Theorem (ALE non-decrease).** *For any Ricci-flat ALE 4-space, $|\Delta\tau| \le \frac{2}{3}\,\Delta\chi$ with equality iff half-flat. Hence for any orbifold+Ricci-flat-ALE resolution:*
$$
\chi(M) - \tfrac{3}{2}|\tau(M)| \ge \chi_{\mathrm{orb}}(\mathcal{O}) - \tfrac{3}{2}|\tau_{\mathrm{orb}}(\mathcal{O})|.
$$

*Proof.* Since $\operatorname{Ric} = 0$: $|12\pi^2\,\Delta\tau| = |\int(|W^+|^2 - |W^-|^2)| \le \int |W|^2 = 8\pi^2\,\Delta\chi$, giving $|\Delta\tau| \le \frac{2}{3}\,\Delta\chi$. Triangle inequality on $\tau(M) = \tau_{\mathrm{orb}} + \sum \Delta\tau_i$ gives $|\tau(M)| \le |\tau_{\mathrm{orb}}| + \frac{2}{3}\sum \Delta\chi_i$. Subtracting: $\chi(M) - \frac{3}{2}|\tau(M)| \ge \chi_{\mathrm{orb}} - \frac{3}{2}|\tau_{\mathrm{orb}}|$. $\square$

For the Eguchi–Hanson: $\Delta\chi = 3/2$, $|\Delta\tau| = 1$, ratio $= 2/3$ exactly. Verified on 15 examples including K3 (equality at surplus 0), positive mirror (equality at aligned $r=0,4$; strict at mixed $r=1,2,3$), negative mirror (equality at aligned; strict at balanced), and both Davis involutions. Data: `workspace/data/step90_chernweil_neutrality_verification.json`.

### 4.3 Entropy inaccessibility (answers §4.3 of original Step 88 decisively)

**Theorem (Entropy inaccessibility).** *For any smooth $A_1$ resolution $M$ of any closed real-hyperbolic 4-orbifold $\mathcal{O}$ with isolated $A_1$ points, and any degree-$d \ne 0$ map $f: M \to Y$ ($Y$ closed hyperbolic):*
$$
d \cdot \chi(Y) \le \chi_{\mathrm{orb}}(\mathcal{O}).
$$
*Hence the Sambusetti inequality is automatically satisfied and no entropy certificate can obstruct Einstein metrics on $M$.*

*Proof.* The near-pinched construction (Theorem 5) gives metrics $g_a$ on $M$ with $\operatorname{Ric}_{g_a} \ge -(3+\varepsilon_a)g_a$, $\varepsilon_a \to 0$, and $\operatorname{Vol}(g_a) \to \operatorname{Vol}(\mathcal{O})$. Rescaling: $\operatorname{Ric} \ge -3\hat g$ with $\operatorname{Vol}(\hat g) \to \operatorname{Vol}(\mathcal{O})$. BCG (BBCG Thm 1.1): $d \cdot \operatorname{Vol}(Y) \le \operatorname{Vol}(\mathcal{O})$. Converting via $\chi = \frac{3}{4\pi^2}\operatorname{Vol}$: $d\cdot\chi(Y) \le \chi_{\mathrm{orb}}$. By non-decrease: $\chi(M) - \frac{3}{2}|\tau(M)| \ge \chi_{\mathrm{orb}} \ge d\cdot\chi(Y)$. $\square$

This answers the original decisive question **NEGATIVELY for ALL orbifold+ALE resolutions.** No $\pi_1$ computation, simplicial-volume estimate, or degree-map topology is needed. The BCG volume bound from the near-pinched metrics closes the entire entropy route at once.

### 4.4 Triple disjointness

All three known families of no-Einstein certificates are independently blind to the audited near-pinched orbifold+ALE construction:

1. **PSC/Weitzenböck $\perp$ monopole/BF** (positive, class-level): positive Ric pinching $\Rightarrow$ PSC $\Rightarrow$ Weitzenböck kills SW/BF.
2. **IMT adjunction $\perp$ reversed $A_1$ nodes** (negative, construction-class): reversed nodes insert $+2$-spheres $\Rightarrow$ IMT kills BF.
3. **Chern–Weil neutrality $\perp$ entropy** (all signs, all orbifold+ALE): half-flat ALE: $\Delta(\chi - \frac{3}{2}|\tau|) = 0$; BCG: $d\cdot\chi(Y) \le \chi_{\mathrm{orb}}$. Sambusetti always satisfied.

A refutation must either construct near-pinched metrics outside orbifold+ALE (non-warped connector), or discover a no-Einstein mechanism outside all three shields. Full analysis: `workspace/notes/step90_chernweil_neutrality_and_triple_disjointness.md`.

---

## 5. Implications for the negative branch $P_4^-$

The negative-branch landscape is now:

| Family | No-Einstein mechanism | Near-pinching status | Notes |
|---|---|---|---|
| $N \# N$, $N$ hyperbolic | Sambusetti/BCG entropy | $\delta \ge 3/(4\chi(N))$; warped $S^3$ waist: $\delta \ge 3/2$ | Non-warped waists remain open |
| $X \# k\overline{\mathbb{CP}}^2$, LeBrun | BF/monopole | Burns core $O(1)$ defect | A₁ machine disjoint from this reservoir |
| Negative mirror mixed rows | Unknown | $\delta \le C/|\log a|$ by A₁ construction | Entropy invisible ($\|M\| = 0$) |
| Hyp. orbifold $A_1$ resolution | Sambusetti (inaccessible) | $\delta \le C/|\log a|$ (exists, e.g. Davis) | §4.3 answered NO: Chern–Weil neutrality + BCG |

**Current state of $P_4^-$:**
- Warped-product methods cannot produce near-negative-pinched connected sums ($\delta \ge 3/2$ at waists).
- The CGB/BCG threshold $\delta \sim 1/\chi(N)$ is additive and cannot produce a uniform $\delta_0$.
- The A₁ construction machine produces $\delta \to 0$ metrics, but on manifolds that are currently entropy-invisible.
- Question 4.3 is answered negatively (§4.3): Chern–Weil neutrality + BCG volume comparison prove entropy inaccessibility for ALL orbifold+ALE resolutions. Refuting $P_4^-$ requires a non-warped connector at rate $O(1/\chi)$ or a new no-Einstein mechanism outside all three disjointness shields.

---

## 6. Evidence files

- `workspace/data/step88_warped_waist_and_bcg_threshold.json`: verified computation.
- `workspace/scripts/step88_warped_waist_and_bcg_threshold.py`: source.
- A01 `workspace/notes/step91_sambusetti_bcg_quantitative_route.md`: parallel BCG derivation.
- Source references in §1 header.
