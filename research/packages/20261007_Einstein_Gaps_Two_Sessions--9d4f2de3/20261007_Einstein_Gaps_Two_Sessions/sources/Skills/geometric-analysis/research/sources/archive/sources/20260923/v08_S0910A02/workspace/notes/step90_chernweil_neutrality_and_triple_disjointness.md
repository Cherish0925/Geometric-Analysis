# Step 90: Chern–Weil neutrality, entropy inaccessibility, and triple disjointness

This note establishes three structural results that close the entropy/Sambusetti route for every orbifold+ALE resolution and unify the three known disjointness mechanisms into a single theorem. It also corrects the false π₁ claim in Step 88 §4.

---

## 1. Chern–Weil neutrality of Ricci-flat ALE bubbles

### 1.1 The ALE inequality

**Theorem (ALE non-decrease).** *For any complete Ricci-flat ALE 4-space with $\Delta\chi > 0$:*
$$
|\Delta\tau| \le \frac{2}{3}\,\Delta\chi,
$$
*with equality if and only if the ALE space is half-flat ($W^+ = 0$ or $W^- = 0$).*

*Proof.* Since $\operatorname{Ric} = 0$, we have $s = 0$ and $E = 0$, so $|\operatorname{Rm}|^2 = |W|^2$. The ALE Chern–Gauss–Bonnet and Hirzebruch signature integrals give:
$$
8\pi^2\,\Delta\chi = \int |W|^2 = \int |W^+|^2 + \int |W^-|^2,
$$
$$
12\pi^2\,\Delta\tau = \int |W^+|^2 - \int |W^-|^2.
$$
Therefore $|12\pi^2\,\Delta\tau| \le \int |W|^2 = 8\pi^2\,\Delta\chi$, giving $|\Delta\tau| \le \frac{2}{3}\,\Delta\chi$. Equality holds iff $\int |W^-|^2 = 0$ or $\int |W^+|^2 = 0$, i.e., the ALE is half-flat. $\square$

### 1.2 The resolution non-decrease theorem

**Theorem (Hitchin–Thorpe surplus non-decrease).** *Let $\mathcal{O}$ be a closed Einstein 4-orbifold with isolated singularities, and let $M$ be a smooth resolution obtained by replacing each singular neighborhood by a complete Ricci-flat ALE space. Then:*
$$
\chi(M) - \tfrac{3}{2}|\tau(M)| \ge \chi_{\mathrm{orb}}(\mathcal{O}) - \tfrac{3}{2}|\tau_{\mathrm{orb}}(\mathcal{O})|.
$$
*Equality holds iff every ALE bubble is half-flat with all chirality signs aligned.*

*Proof.* By the triangle inequality:
$$
|\tau(M)| = |\tau_{\mathrm{orb}} + \textstyle\sum_i \Delta\tau_i| \le |\tau_{\mathrm{orb}}| + \sum_i |\Delta\tau_i| \le |\tau_{\mathrm{orb}}| + \tfrac{2}{3}\sum_i \Delta\chi_i.
$$
Hence:
$$
\chi(M) - \tfrac{3}{2}|\tau(M)| \ge (\chi_{\mathrm{orb}} + \textstyle\sum \Delta\chi_i) - \tfrac{3}{2}(|\tau_{\mathrm{orb}}| + \tfrac{2}{3}\sum \Delta\chi_i)
= \chi_{\mathrm{orb}} - \tfrac{3}{2}|\tau_{\mathrm{orb}}|. \qquad\square
$$

**Interpretation.** The quantity $S = \chi - \frac{3}{2}|\tau|$ is the Hitchin–Thorpe surplus. For a closed Einstein metric, $S \ge 0$ with $S = 0$ only for flat, locally Calabi–Yau (K3 quotients), or real-hyperbolic metrics. The theorem says that resolving orbifold singularities by Ricci-flat ALE spaces can never decrease $S$. In particular, a manifold with $S < S_{\mathrm{orb}}$ cannot be obtained by such a resolution.

### 1.3 Verification against known examples

| Orbifold | $k$ | Chirality | $\chi(M)$ | $\tau(M)$ | $S(M)$ | $S_{\mathrm{orb}}$ | Status |
|---|---|---|---|---|---|---|---|
| $T^4/\mathbb{Z}_2$ (Kummer) | 16 | aligned | 24 | $-16$ | 0 | 0 | = |
| $(S^2{\times}S^2)/\mathbb{Z}_2$ | 4 | aligned ($r{=}0$) | 8 | $-4$ | 2 | 2 | = |
| $(S^2{\times}S^2)/\mathbb{Z}_2$ | 4 | balanced ($r{=}2$) | 8 | 0 | 8 | 2 | > |
| $(\Sigma_2{\times}\Sigma_2)/\langle\iota{\times}\iota\rangle$ | 36 | aligned | 56 | $-36$ | 2 | 2 | = |
| $(\Sigma_2{\times}\Sigma_2)/\langle\iota{\times}\iota\rangle$ | 36 | balanced | 56 | 0 | 56 | 2 | > |
| $M_{\mathrm{Davis}}/\alpha$ | 122 | aligned | 196 | $-122$ | 13 | 13 | = |
| $M_{\mathrm{Davis}}/\alpha\sigma$ | 10 | aligned | 28 | $-10$ | 13 | 13 | = |

All 15 tested examples (including intermediate mixed rows) satisfy non-decrease. Aligned cases give exact equality; mixed cases give strict increase. Data: `workspace/data/step90_chernweil_neutrality_verification.json`.

---

## 2. Entropy inaccessibility of orbifold+ALE resolutions

### 2.1 The BCG volume comparison for near-pinched metrics

**Theorem (Entropy inaccessibility).** *Let $\mathcal{O}$ be a closed real-hyperbolic Einstein 4-orbifold (sectional curvature $-1$, so $\operatorname{Ric} = -3g$, $\tau_{\mathrm{orb}} = 0$) with $k \ge 1$ isolated $A_1$ singularities. Let $M$ be any smooth $A_1$ resolution of $\mathcal{O}$, with any chirality pattern. Then for any closed hyperbolic 4-manifold $Y$ and any continuous map $f: M \to Y$ of degree $d \ne 0$:*
$$
d \cdot \chi(Y) \le \chi_{\mathrm{orb}}(\mathcal{O}).
$$
*In particular, the Sambusetti inequality $\chi(M) \ge \frac{3}{2}|\tau(M)| + d\cdot\chi(Y)$ is automatically satisfied for every resolution $M$, so no Sambusetti-type entropy certificate can obstruct Einstein metrics on $M$.*

*Proof.* The near-pinched construction (Theorem 5 of the reduction) produces a one-parameter family of smooth metrics $g_a$ on $M$ with:
$$
\operatorname{Ric}_{g_a} \ge -(3 + \varepsilon_a)g_a, \qquad \varepsilon_a = \frac{C}{|\log a|} \to 0,
$$
and $\operatorname{Vol}(g_a) \to \operatorname{Vol}(\mathcal{O})$ as $a \to 0$. Rescaling $\hat g_a = (1+\varepsilon_a/3)g_a$ gives $\operatorname{Ric}_{\hat g_a} = \operatorname{Ric}_{g_a} \ge -(3+\varepsilon_a)g_a = -3\hat g_a$, hence:
$$
\operatorname{Ric}_{\hat g_a} \ge -3\hat g_a, \qquad \operatorname{Vol}(\hat g_a) = (1+\varepsilon_a/3)^2\operatorname{Vol}(g_a) \to \operatorname{Vol}(\mathcal{O}).
$$

By the Bessières–Besson–Courtois–Gallot theorem (BBCG, Theorem 1.1): for a closed orientable $n$-manifold with $\operatorname{Ric} \ge -(n{-}1)g$ and a degree-$d$ map to a closed hyperbolic manifold $Y$:
$$
d \cdot \operatorname{Vol}(Y) \le \operatorname{Vol}(M, \hat g_a).
$$
Taking $a \to 0$:
$$
d \cdot \operatorname{Vol}(Y) \le \operatorname{Vol}(\mathcal{O}).
$$

Since both $\mathcal{O}$ and $Y$ have constant sectional curvature $-1$, the hyperbolic Gauss–Bonnet identity gives $\chi = \frac{3}{4\pi^2}\operatorname{Vol}$ for both, so:
$$
d \cdot \chi(Y) \le \chi_{\mathrm{orb}}(\mathcal{O}).
$$

By the non-decrease theorem (§1.2) with $\tau_{\mathrm{orb}} = 0$:
$$
\chi(M) - \tfrac{3}{2}|\tau(M)| \ge \chi_{\mathrm{orb}}(\mathcal{O}) \ge d \cdot \chi(Y).
$$
This is exactly the Sambusetti inequality. $\square$

### 2.2 Why this closes the entropy route completely

The theorem applies to *every* orbifold+ALE resolution with *any* chirality pattern, not only our two mirrors. It does not require computing $\pi_1(M)$, simplicial volume, or the existence of degree maps — it proves a priori that no such map can produce a Sambusetti violation. The three ingredients are:

1. The ALE inequality (pure algebra of Chern–Weil integrals);
2. The near-pinched construction (the audited Theorem 5);
3. The BCG volume comparison (metric-level, applied to a specific family of metrics on $M$).

The argument is not circular: BCG says that *if* $M$ carries a metric with $\operatorname{Ric} \ge -3g$, *then* any degree map to a hyperbolic target is volume-bounded. The near-pinched construction exhibits such metrics. The topology of the degree map is independent of the metric.

### 2.3 The decisive question of Step 88 §4.3 is answered negatively

Step 88 asked: *does there exist a hyperbolic $A_1$ orbifold whose resolution violates Sambusetti?* The answer is **no, for every hyperbolic $A_1$ orbifold**, because $d \cdot \chi(Y) \le \chi_{\mathrm{orb}}(\mathcal{O})$ is forced by the near-pinched metrics that the resolution carries. This is stronger than computing $\pi_1$ case by case — it closes the entire route at once.

---

## 3. Correction of Step 88 §4.1: negative mirror π₁

Step 88 §4.1 claimed the negative mirror resolution has infinite $\pi_1$ with abelianization $(\mathbb{Z}/2)^8$. This was **wrong**. Step 57 proved by van Kampen that *every* sign-pattern filling of $(\Sigma_2 \times \Sigma_2)/\langle \iota \times \iota \rangle$ is simply connected: each of the 36 EH caps has $\pi_1(\mathrm{EH}) = 1$ and kills the $\mathbb{Z}/2$ peripheral group of the $\mathrm{RP}^3$ boundary. With 36 stabilizer normal closures, the extra relations annihilate all remaining torsion.

The coinvariant-only shortcut omitted these 35 extra relations beyond the first coinvariance. The self-contradiction was already visible: if $\iota_*$ inverts every element, then every element in the coinvariant quotient satisfies $\gamma = \gamma^{-1}$, making the quotient abelian and finite, not infinite — and the 36 filling relations are even stronger, collapsing the quotient to the trivial group.

**Mechanism: seam compression.** The $\mathrm{RP}^3$ boundaries are amenable seams. Filling them with simply-connected EH caps compresses the fundamental group. This is the same mechanism that makes Kummer K3 simply connected from $T^4/\mathbb{Z}_2$ with 16 nodes. Source support for the compression of simplicial volume through non-$\pi_1$-injective amenable seams: Capovilla–Frigerio–Pagliantini, Bucher–Burger–Frigerio–Iozzi–Pagliantini–Pozzetti, Bargagnati–Frigerio (lines 118–150 of Knowledge source).

**Standing caution.** The relative simplicial volume $\|(X_0, \partial X_0)\|$ of the complement of the resolved balls may be positive (e.g., for the negative mirror, the outside piece inherits the locally-symmetric $\mathbb{H}^2 \times \mathbb{H}^2$ mass). But filling with a ball satisfying $\|(D^4, S^3)\| = 0$ does not guarantee $\|M\| = \|X_0\| + \|(D^4, S^3)\|$: the amenable-additivity theorem requires $\pi_1$-injective seams, and EH caps violate this. So $\|M\| = 0$ despite $\|(X_0, \partial)\| > 0$.

---

## 4. Triple disjointness theorem

**Theorem (Triple disjointness).** *All three known families of no-Einstein certificates in dimension four are independently blind to the audited near-pinched orbifold+ALE construction:*

1. **PSC/Weitzenböck ⊥ monopole/BF** (positive branch, class-level):
   Positive Ricci pinching gives PSC. Weitzenböck then kills all SW/BF classes. This excludes every monopole-based no-Einstein certificate (Ishida–LeBrun, Kotschick, Bauer–Furuta) from the hypothesis class of any positive interval. *Scope: every positively pinched closed 4-manifold.*

2. **IMT adjunction ⊥ reversed $A_1$ nodes** (negative branch, construction-class):
   On the negative side, compatible $A_1$ nodes place the resolution in the Kähler smoothing / ample-canonical regime where Aubin–Yau already supplies negative KE (not a no-Einstein example). Reversed nodes insert non-torsion embedded $+2$-spheres. The Iida–Mukherjee–Taniguchi BF adjunction inequality, applied through the closed-to-punctured interface $BF(X^\circ) = BF(X)$, kills the standard BF invariants used by Ishida–LeBrun. *Scope: the $A_1$-resolution construction class with BF/monopole-type certificates.*

3. **Chern–Weil neutrality ⊥ Sambusetti/entropy** (all signs, all orbifold+ALE):
   Half-flat Ricci-flat ALE bubbles satisfy $\Delta(\chi - \frac{3}{2}|\tau|) = 0$ exactly. For any resolution of a real-hyperbolic orbifold, the BCG volume comparison applied to the near-pinched metrics forces $d \cdot \chi(Y) \le \chi_{\mathrm{orb}}$, so the Sambusetti inequality is automatically satisfied. *Scope: every smooth $A_1$ resolution of every real-hyperbolic 4-orbifold.*

Each mechanism is independent and structural. Together they explain why Yau–26 resists both proof and refutation in dimension four: **every known no-Einstein certificate is disjoint from every known near-pinched construction, each for its own reason.**

### 4.1 What a refutation must invent

A refutation of $P_4^-$ must either:
- construct near-pinched metrics *outside* the orbifold+ALE class (a non-warped neck/connector through $N \# N$ at rate $O(1/\chi)$), or
- discover a no-Einstein mechanism outside monopole, BF, and entropy certificates.

A refutation of $P_4^+$ must:
- prove that some positively near-pinched manifold in the mixed-row class carries no positive Einstein metric, using a tool not killed by PSC.

A proof of either branch must:
- show that the near-pinched sequence converges (in some sense) to an actual Einstein metric, overcoming the orbifold degeneration.

### 4.2 Proof-side consequence of neutrality

The Chern–Weil neutrality also has a proof-side implication. If every near-pinched sequence is asymptotically an Einstein orbifold with Ricci-flat ALE bubbles (as the noncollapsed compactness theory predicts), then no curvature-integral or entropy obstruction *can ever* refute either strict branch — because neutrality guarantees that all such integral certificates are automatically satisfied by the construction. The transition-scale theorem and the class-T ALE loophole become the load-bearing infrastructure: they determine whether the orbifold+ALE decomposition is *all* that can happen, or whether more exotic degenerations are possible.

---

## 5. Relocation of live work

**Negative branch.** The only known near-pinched construction outside orbifold+ALE is a connected-sum neck. The warped-product waist barrier (Theorem 8a.3) gives $\delta \ge 3/2$ for warped $k \ge 0$ waists. A03's exact reflected OT Bochner comparison gives $\sup e \ge 12$ at exit, blocking exact OT connectors. The non-warped forced connector gap is now the *single remaining* negative-branch refutation mechanism. A03's coupled $W = e + c|\nabla\sigma|^2$ bootstrap (message #624) is the most promising current approach. If it closes at $\sup W \le 9 + C\delta$, then forced connectors cost $\delta \ge \delta_{\min} > 0$ — a uniform threshold that, combined with the waist barrier, would close the entire negative-refutation hemisphere against every known certificate and construction.

**Positive branch.** The positive branch is untouched by all entropy mechanisms and remains tied to the mixed-row Ozuch-desingularization program. A01's $K$-symmetry/AB-sector sign theorem (#617) is progress for local positive-Einstein existence but does not yet determine the sign of the full Green interaction. The Gram-determinant/transgression approach (Step 81–82) is a possible complementary obstruction but has no quantitative zero-set estimate.

---

## 6. Sources and evidence

- Verification data: `workspace/data/step90_chernweil_neutrality_verification.json`
- Waist barrier and BCG threshold: `workspace/data/step88_warped_waist_and_bcg_threshold.json`
- Ten-sector Weyl audit: `workspace/data/step83_full_weyl_log_annulus_audit.json`
- Audited construction: `workspace/notes/step83_near_pinched_construction_and_frontier_reduction.md`
- Sambusetti/BCG sources: Kotschick, *Entropies, Volumes, and Einstein Metrics* (Corollary 3); Bessières–Besson–Courtois–Gallot, *Differentiable rigidity under Ricci curvature lower bound* (Theorems 1.1, 1.5, Corollary 1.7); LeBrun, *Four-Manifolds without Einstein Metrics* (footnote on Sambusetti).
- BF adjunction: Iida–Mukherjee–Taniguchi, *An adjunction inequality for the Bauer–Furuta type invariants* (Theorems 1.1, 3.1, 4.6).
- Simplicial volume caution: Bargagnati–Frigerio (Proposition 2.3, Remark 2.5); Bucher–Burger–Frigerio–Iozzi–Pagliantini–Pozzetti (Theorem 2.1); Capovilla (amenable excision).
- Hyperbolic A₁ orbifolds: Ratcliffe–Tschantz, *The Ĝ-Index of a Spin, Closed, Hyperbolic Manifold* (§7, lines 552–667).
- Cumulative source: `Skills/qiushi-yau26/references/research/20260912.tex`.
