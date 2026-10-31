# Step 5: All-Dimensional Positive-Branch Existence Program

> **ERRATUM (Step 5, same session).** Theorem 2 as stated is not proven for
> n ≥ 4. The harmonic-radius Step 2.1 does not follow from Ricci bounds +
> noncollapse: Weyl curvature can concentrate. The corrected version (Thm 2')
> needs |Rm| ≤ K. The gap identification is also wrong: P_n^+ has TWO open
> gaps (curvature concentration + collapse), not one. See
> `step5_erratum_theorem2_correction.md` for the full correction. Sections
> 1, 6, 7, 8 (4D CGB, topological filter, Lean) remain valid.


Session: S0910A02. Agent2/Constructor. Phase: Explore.

## Purpose

This note is the first dimension-independent mathematical construction for Yau
Problem 26 in this session. It states the positive-branch program as a sequence
of theorems with explicit hypotheses and constant dependence, identifies the
exact gap between known results and the dimension-only constants required by
the original problem, and specializes to dimension four where the CGB/Weyl
budget gives additional purchase.

**Target fidelity.** The active target is the full proposition: for every
\(n \ge 2\), does \(P_n^+ \lor P_n^-\) hold? This note addresses \(P_n^+\):
does there exist \(\varepsilon_n > 0\) (depending only on \(n\)) such that
\(\delta_+(g) \le \varepsilon_n\) implies \(\mathcal{E}(M) \ne \varnothing\)?
Resolution of \(P_n^+\) for all \(n\) would prove the full proposition.

---

## 1. Automatic geometric control on the positive branch

**Theorem 1 (Positive precompactness, all dimensions).** Let \((M^n, g)\) be
a closed connected smooth Riemannian \(n\)-manifold with
\(\delta_+(g) \le \delta < 1\). Then:

(a) **Two-sided Ricci bounds:**
\[
(1-\delta)g \le \operatorname{Ric}_g \le (1+\delta)g.
\]

(b) **Myers diameter bound:**
\[
\operatorname{diam}(M,g) \le \frac{\pi\sqrt{n-1}}{\sqrt{1-\delta}}
=: D(n,\delta).
\]
*Proof.* \(\operatorname{Ric}_g \ge (1-\delta)g\) and Myers's theorem with
\(\operatorname{Ric} \ge (n-1)\kappa g\) giving \(\operatorname{diam} \le
\pi/\sqrt{\kappa}\). Here \(\kappa = (1-\delta)/(n-1)\). \(\square\)

(c) **Bishop–Gromov volume bound:**
\[
\operatorname{Vol}(M,g) \le V_n(\delta)
:= \operatorname{Vol}(S^n(\sqrt{(n-1)/(1-\delta)})),
\]
where \(S^n(R)\) is the round sphere of radius \(R\). As \(\delta \to 0\),
\(V_n(\delta) \to \omega_n (\pi\sqrt{n-1})^n / (n-1)^{n/2}\), which is
\(\operatorname{Vol}(S^n(1))\) in the normalization \(\operatorname{Ric} = g\).

*Proof.* Bishop–Gromov comparison with the simply connected space form of
constant Ricci \((1-\delta)g\), i.e., the round sphere. \(\square\)

(d) **Fundamental group:** \(\pi_1(M)\) is finite by applying Myers to the universal cover. There is **no dimension-only upper bound** on \(|\pi_1(M)|\): round lens spaces have \(\delta_+=0\) and \(|\pi_1|\to\infty\). If an additional volume lower bound \(\operatorname{Vol}(M,g)\ge v>0\) is imposed, then Bishop's volume upper bound on the universal cover gives the conditional estimate \(|\pi_1(M)|\le V_n(\delta)/v\).

(e) **Bochner vanishing:** \(b_1(M) = 0\). *Proof.* \(\operatorname{Ric} > 0\)
kills harmonic one-forms by the Bochner formula. \(\square\)

(f) **Gromov–Hausdorff precompactness.** The class of all
\((M^n, g)\) with \(\delta_+(g) \le \delta\) is GH-precompact: every
sequence has a subsequence converging in the pointed GH sense to a compact
length space \((X, d_X)\).

*Proof.* Bounded diameter + bounded Ricci below gives GH-precompactness by
Gromov's compactness theorem. \(\square\)

**All of (a)–(f) hold uniformly in every dimension with constants depending
only on \(n\) and \(\delta\).** This is the automatic control provided by
\(\operatorname{Ric} \approx +g\). In contrast, the negative branch has no
diameter bound from Ricci alone, so (b)–(f) fail.

---

## 2. The noncollapsed/collapsed dichotomy

For a sequence \((M_i^n, g_i)\) with \(\delta_+(g_i) \le \delta_i \to 0\),
Theorem 1 gives uniform diameter and volume upper bounds. Two regimes arise:

**Case I (Noncollapsed).** There exists \(v > 0\) with
\(\operatorname{Vol}(M_i, g_i) \ge v\) for all \(i\)
(after passing to a subsequence).

**Case II (Collapsed).** \(\operatorname{Vol}(M_i, g_i) \to 0\).

The positive-branch program reduces \(P_n^+\) to:

\[
\boxed{P_n^+ \iff \text{(Noncollapsed convergence)} \land
\text{(Collapsed compatibility)}.}
\]

---

## 3. Noncollapsed case: convergence to Einstein

**Theorem 2 (Noncollapsed positive convergence).** *For each \(n \ge 2\) and
\(v > 0\), there exists \(\varepsilon(n,v) > 0\) such that if \((M^n,g)\) is a
closed connected smooth Riemannian \(n\)-manifold with*

\[
\delta_+(g) \le \varepsilon(n,v), \qquad \operatorname{Vol}(M,g) \ge v,
\]

*then \(M\) admits a smooth Einstein metric \(h\) with
\(\operatorname{Ric}_h = \lambda h\) for some \(\lambda > 0\).*

**Proof structure** (with explicit dependencies; this is a reconstruction
from standard tools, not a citation of a single source):

**Step 2.1. Harmonic radius lower bound.** From Theorem 1(a,b),
\(|\operatorname{Ric}_{g_i}| \le \Lambda := 2\) (for \(\delta_i \le 1\))
and \(\operatorname{diam}(M_i) \le D := 2\pi\sqrt{n-1}\). Combined with the
volume lower bound \(\operatorname{Vol} \ge v\), the harmonic radius satisfies
\[
r_h(M_i, g_i) \ge r_0(n, \Lambda, D, v) > 0.
\]
This is a consequence of the fact that two-sided Ricci bounds + noncollapse +
bounded diameter give a definite harmonic radius. The key argument: by volume
comparison, every ball of radius \(r\) has volume at least
\(c(n,\Lambda) \cdot v \cdot r^n / D^n\), so sufficiently small balls are
noncollapsed. In harmonic coordinates on such a ball, the metric coefficients
\(g_{ij}\) satisfy the elliptic PDE
\[
-\frac{1}{2}\Delta g_{ij} + Q_{ij}(g, \partial g) = R_{ij},
\]
where \(Q\) is quadratic in \(\partial g\) and \(R_{ij}\) is the Ricci tensor.
The two-sided bound \(|R_{ij}| \le \Lambda\) together with the C^0 metric
control gives uniform \(C^{1,\alpha}\) estimates for \(g_{ij}\) on a ball of
definite radius. [This step uses Anderson's harmonic coordinate approach;
the exact constant \(r_0\) depends on \((n, \Lambda, D, v)\) through Sobolev
constants and elliptic regularity.]

**Step 2.2. \(C^{1,\alpha}\) convergence.** The uniform harmonic radius
lower bound and \(C^{1,\alpha}\) metric bounds give, by Arzelà–Ascoli on the
harmonic-coordinate atlases, a subsequence converging in \(C^{1,\alpha}\) to
a \(C^{1,\alpha}\) Riemannian manifold \((M_\infty, g_\infty)\). The
convergence is global on the compact manifolds (finitely many charts suffice).

**Step 2.3. Limit is Einstein.** In harmonic coordinates, \(\delta_+(g_i)
\to 0\) means \(\operatorname{Ric}_{g_i} \to g_i\) uniformly. In the
\(C^{1,\alpha}\) limit,
\[
\operatorname{Ric}_{g_\infty} = g_\infty
\]
in the distributional/weak sense. Since \(g_\infty\) is \(C^{1,\alpha}\),
the Einstein equation in harmonic coordinates is an elliptic system for
\(g_{ij}\); distributional Einstein solutions in \(C^{1,\alpha}\) are
smooth by elliptic bootstrapping:
- \(g \in C^{1,\alpha}\) and \(\operatorname{Ric} = g\) weakly
  \(\Rightarrow\) \(g \in C^{2,\alpha}\) (Schauder estimates)
  \(\Rightarrow\) \(g \in C^{3,\alpha}\) \(\Rightarrow \cdots \Rightarrow
  g \in C^\infty\).

**Step 2.4. Diffeomorphism for large \(i\).** The \(C^{1,\alpha}\)
convergence of compact manifolds means: for large \(i\), there exist
diffeomorphisms \(\varphi_i : M_\infty \to M_i\) with
\(\|\varphi_i^* g_i - g_\infty\|_{C^{1,\alpha}} \to 0\). In particular,
\(M_i\) is diffeomorphic to \(M_\infty\).

**Step 2.5. Conclusion.** \(M_\infty\) carries the smooth Einstein metric
\(g_\infty\) with \(\operatorname{Ric}_{g_\infty} = g_\infty\). Since
\(M_i \cong M_\infty\) for large \(i\), the pullback
\(h_i := (\varphi_i^{-1})^* g_\infty\) is a smooth Einstein metric on
\(M_i\). Therefore \(\mathcal{E}(M_i) \ne \varnothing\). \(\square\)

**Remark on constant dependence.** The threshold \(\varepsilon(n,v)\) arises
from the harmonic radius bound in Step 2.1. It depends on \(v\) through the
noncollapse ratio. The dependence on \(v\) is the entire distance from
Theorem 2 to \(P_n^+\): Yau's problem asks for \(\varepsilon_n\) independent
of \(v\), while Theorem 2 needs \(v > 0\).

---

## 4. The gap: collapse is the only remaining enemy

**Corollary (Gap identification).** \(P_n^+\) holds if and only if there exists
\(\varepsilon_n > 0\) such that \(\delta_+(g) \le \varepsilon_n\) prevents
collapse: \(\operatorname{Vol}(M,g) \ge v(\varepsilon_n, n) > 0\).

*Proof.* If noncollapse holds uniformly, Theorem 2 gives the conclusion. If
collapse cannot be prevented, there exist \((M_i, g_i)\) with \(\delta_i \to 0\)
and \(\operatorname{Vol}(M_i) \to 0\); but these might still have underlying
topologies carrying Einstein metrics. The correct equivalence is:

\(P_n^+\) fails \(\iff\) there exists a sequence \((M_i^n, g_i)\) with
\(\delta_+(g_i) \to 0\) and \(\mathcal{E}(M_i) = \varnothing\). By Theorem 2,
such \(M_i\) must have \(\operatorname{Vol}(M_i, g_i) \to 0\) (else a
noncollapsed subsequence gives the Einstein metric). \(\square\)

**Therefore, the positive branch in every dimension reduces to a single
question: can collapse under tight positive Ricci pinching produce a topology
that admits no Einstein metric?**

---

## 5. What collapse looks like under tight positive pinching

Under \(\delta_+(g_i) \to 0\), the collapsing sequence has:
- \(\operatorname{Ric}_{g_i} \ge (1-\delta_i)g_i \to g_i\)
  (positive Ricci)
- \(\operatorname{diam}(M_i) \le D(n)\) (bounded)
- \(\operatorname{Vol}(M_i) \to 0\) (collapsing)
- \(\pi_1(M_i)\) finite, \(b_1(M_i) = 0\)

The Gromov–Hausdorff limit \(X\) is a compact metric space of
\(\dim_{\mathrm{Haus}} X < n\). The theory of collapse under bounded
Ricci (as opposed to bounded sectional curvature) is less developed:

- **Cheeger–Fukaya–Gromov (CFG):** requires \(|K| \le \Lambda\)
  (bounded sectional curvature) to produce nilpotent Killing structures
  and F-structures. We do not have sectional bounds.

- **Cheeger–Colding:** under Ricci lower bounds, the GH limits have
  well-defined \(k\)-dimensional regular sets where convergence is
  smooth away from a singular set of measure zero.

- **Kapovitch–Wilking generalized Margulis lemma:** under \(\operatorname{Ric}
  \ge -(n-1)g\), the fundamental group of a small ball is virtually nilpotent.
  This applies.

- **Naber–Zhang \(\varepsilon\)-regularity:** on collapsed manifolds with
  bounded Ricci, local regularity theory.

**Key observation.** Exact Einstein metrics can collapse under positive
pinching: round lens spaces \(L(m,1) = S^3/\mathbb{Z}_m\) with the metric
\(h_m\) satisfying \(\operatorname{Ric}_{h_m} = h_m\) have
\(\operatorname{Vol}(h_m) = \operatorname{Vol}(S^3)/m \to 0\). Their
GH limit is \(S^2(\frac{1}{2})\) (the base of the Hopf fibration). So
collapse under tight positive pinching is real and can be Einstein-compatible.

This means that **any proof of \(P_n^+\) must allow Einstein-compatible
collapse rather than exclude all collapse**. The question is:

> *Is every topology that can appear as a collapsing sequence with
> \(\delta_+ \to 0\) also a topology that admits an Einstein metric?*

---

## 6. Low-dimensional resolution

**\(n = 2\):** \(P_2^+\) holds. Every closed surface admits a constant-curvature
metric by the uniformization theorem. The positive branch requires
\(\operatorname{Ric}_g \ge (1-\varepsilon)g > 0\), which forces \(M = S^2\)
or \(M = \mathbb{RP}^2\). Both are Einstein (round metric).

**\(n = 3\):** \(P_3^+\) holds. By Hamilton's theorem (1982),
\(\operatorname{Ric}_g > 0\) on a closed 3-manifold implies the Ricci flow
deforms \(g\) to a metric of constant positive sectional curvature. Therefore
\(M\) is a spherical space form \(S^3/\Gamma\), which carries the round
(Einstein) metric. No \(\varepsilon\)-threshold is needed; any positive Ricci
suffices.

---

## 7. Four-dimensional specialization: CGB forces curvature concentration

In dimension four, the full-Weyl Chern–Gauss–Bonnet identity provides
additional control on collapse. With the TTCS-verified optimal pointwise bound:

**Theorem 3 (Four-dimensional Weyl/volume accounting).** Let \((M^4, g)\) be
closed and oriented with \(\delta_\sigma(g) \le \delta < 1/2\). Then:

\[
\int_M |W|^2 \, d\mu + \beta(\delta) \operatorname{Vol}(M,g)
\le 8\pi^2 \chi(M), \tag{GB}
\]

where
\[
\beta(\delta) = \begin{cases}
\frac{2}{3}(1-\delta)^2 & \text{if } \delta \le 1/3, \\[4pt]
\frac{2}{3}(1+\delta)(1-2\delta) & \text{if } 1/3 \le \delta < 1/2.
\end{cases}
\]

*This is sign-blind: the same estimate holds for both \(\sigma = +1\) and
\(\sigma = -1\).*

**Corollary (Bounded-curvature collapse impossible in dim 4).** If
additionally \(|Rm_g| \le K\), then since \(|W|^2 \le K^2\) and
\(\chi(M) \ge 1\) (from \(\beta > 0\)):

\[
\operatorname{Vol}(M,g) \ge \frac{8\pi^2}{K^2 + a(\delta)},
\qquad a(\delta) = \frac{2}{3}(1+\delta)^2.
\]

**Therefore, four-dimensional collapse under tight pinching must involve
\(|Rm|_\infty \to \infty\), i.e., curvature concentration.** This is not
bounded-curvature collapse in the CFG sense; it is Weyl-energy
concentrating onto a set of small measure to fill the topological
budget \(8\pi^2\chi\).

**Positive-branch corollary for dim 4.** Combining with Theorem 1(b):
if \(\delta_+(g_i) \to 0\), Myers gives \(\operatorname{diam} \le D(4)\),
and CGB gives \(\chi > 0\), \(2\chi > 3|\tau|\), \(b_1 = 0\). If also
\(|Rm_{g_i}| \le K\), noncollapse follows and Theorem 2 gives Einstein
existence. So:

> *The only four-dimensional positive-branch enemy is collapse with
> \(|Rm| \to \infty\) (curvature concentration), not bounded-curvature
> collapse.*

---

## 8. Four-dimensional topological filter

In the positive branch (\(\delta_+(g) \le \delta \ll 1\)) on a closed oriented
four-manifold, the automatic constraints are:

1. \(\chi(M) > 0\)
2. \(2\chi(M) > 3|\tau(M)|\) (strict Hitchin–Thorpe)
3. \(b_1(M) = 0\) (Bochner; \(\operatorname{Ric} > 0\))
4. \(\pi_1(M)\) finite
5. Positive scalar curvature (\(s > 0\))
6. \(\operatorname{Vol}(M,g) \le 8\pi^2\chi/\beta(\delta)\)

For the positive branch, constraint (5) is particularly powerful: by
Seiberg–Witten theory, a closed oriented smooth four-manifold with
\(b_2^+ \ge 2\) and a metric-independent nonzero Seiberg–Witten invariant
cannot carry positive scalar curvature. Therefore:

> *Manifolds that are no-Einstein due to Seiberg–Witten obstructions
> (LeBrun-type general-type blow-ups) cannot even enter the positive
> branch with \(\delta_+ < 1\).*

This means the positive-branch topological filter automatically excludes
the main known families of no-Einstein four-manifolds from appearing as
tight-pinching inputs. The remaining question is: among the four-manifolds
that do pass this filter, do all carry Einstein metrics?

**Simply connected case.** With \(b_1 = 0\) and \(\pi_1\) finite, the
universal cover \(\tilde{M}\) is compact and simply connected with
\(\chi(\tilde{M}) > 0\), \(b_1(\tilde{M}) = 0\), and positive scalar
curvature. By the 11/8 theorem and related results, the intersection form
is restricted. Known simply connected closed four-manifolds with positive
scalar curvature include:

- \(S^4\): Einstein (round).
- \(\mathbb{CP}^2\): Einstein (Fubini–Study).
- \(S^2 \times S^2\): Einstein (product of round spheres).
- \(\mathbb{CP}^2 \# \overline{\mathbb{CP}}^2\): Einstein (Page metric).
- \(\mathbb{CP}^2 \# 2\overline{\mathbb{CP}}^2\): Einstein
  (Chen–LeBrun–Weber metric).
- \(\#_k \mathbb{CP}^2 \# l\overline{\mathbb{CP}}^2\) for small \(k,l\):
  many carry Einstein metrics; the landscape is not fully mapped.

Whether *every* simply connected four-manifold passing the filter carries
an Einstein metric is a deep open question in four-dimensional geometry.

---

## 9. Summary: the dimension-independent program for \(P_n^+\)

\[
\begin{array}{ll}
\textbf{Known} & \textbf{Status} \\
\hline
\text{Precompactness: diam, Vol, } b_1, \pi_1 & \text{Theorem 1, all } n \\
\text{Noncollapsed } \Rightarrow \text{ Einstein on same topology}
& \text{Theorem 2, all } n, \varepsilon = \varepsilon(n,v) \\
P_2^+ & \text{Proved (uniformization)} \\
P_3^+ & \text{Proved (Hamilton 1982)} \\
\text{4D collapse } \Rightarrow |Rm| \to \infty & \text{Theorem 3} \\
\text{4D positive branch excludes SW no-Einstein} & \text{PSC filter} \\
\hline
\textbf{Open (for all } n \ge 4\textbf{)} \\
\hline
\text{Collapse with } \delta_+ \to 0 \text{ always Einstein-compatible?}
& \text{Central open question} \\
\text{Noncollapse threshold } \varepsilon_n \text{ independent of } v
& \text{Equivalent formulation} \\
\text{4D: curvature concentration compatible with no-Einstein?}
& \text{Testbed for the general question}
\end{array}
\]

The positive-branch program has a clean architecture:
1. In every dimension, tight positive pinching gives GH-precompactness with
   uniform geometric bounds.
2. Noncollapsed subsequences converge to smooth positive Einstein metrics
   on the same smooth manifold.
3. The entire gap is collapse: whether collapsing topologies under tight
   positive pinching always carry Einstein metrics.
4. In dimension four, CGB shows collapse requires curvature concentration
   (not bounded-curvature collapse), and the PSC filter excludes the main
   known no-Einstein families.

---

## 10. Lean 4 scoping assessment

Mathlib (as of lean4 v4.29.1 / current mathlib) provides:
- `IsRiemannianManifold` typeclass and Riemannian distance
- `ContMDiffRiemannianMetric` for smooth Riemannian vector bundles
- Smooth manifold infrastructure (charts, tangent spaces, derivations,
  diffeomorphisms, integral curves, Lie groups)
- Instances: spheres, real spaces

**Missing from Mathlib (essential for Yau26):**
- Levi-Civita connection
- Curvature tensor (Riemann, Ricci, scalar, Weyl)
- Einstein condition \(\operatorname{Ric}_h = \lambda h\)
- Comparison geometry (Myers, Bishop-Gromov)
- Harmonic coordinates and harmonic radius
- GH convergence and compactness
- Chern–Gauss–Bonnet formula
- Seiberg–Witten invariants

Building from `IsRiemannianManifold` to the Einstein condition requires
at minimum: connection on tangent bundle → parallel transport → curvature
endomorphism → Ricci contraction → operator-norm pinching → Einstein
definition. Each step needs substantial Lean infrastructure not currently
in mathlib.

**Assessment:** Full Lean formalization of Yau26 is a multi-year project
at current mathlib maturity. The most realistic formalization targets for
the current session are:
- Branch equivalence \(Q_n \iff P_n^+ \lor P_n^-\) (logic, needs only
  the definitions and scaling identity)
- The scaling identity \(\operatorname{Ric}_{cg} = \operatorname{Ric}_g\)
  (requires connection/curvature, the hardest prerequisite)
- CGB corollaries (requires the full CGB formula, which is far from
  current mathlib)

For the current session, the mathematical proof/counterexample should be
the primary target; Lean formalization can be scoped as a parallel
infrastructure development whose feasibility is now assessed.

---

## 11. Comparison with the negative branch

| Feature | Positive branch | Negative branch |
|---------|----------------|-----------------|
| Diameter | \(\le D(n,\delta)\) (Myers) | **No bound** |
| Volume upper bound | \(\le V_n(\delta)\) (Bishop) | Need separate argument |
| \(\pi_1\) | Finite | No constraint |
| \(b_1\) | \(= 0\) (Bochner) | No constraint |
| GH precompact | Yes | No (without diameter) |
| Noncollapsed \(\Rightarrow\) Einstein | Yes (Thm 2) | Need \(d^2\max|K| < \Lambda^2\) (Min-Oo) |
| Known no-Einstein families | Excluded by PSC filter | Available (LeBrun, dim 4) |
| Collapse | Real, possibly Einstein-compatible | Real, no diameter control |

The positive branch is structurally much stronger: one gap (collapse)
versus the negative branch's two gaps (diameter + collapse). This
asymmetry suggests that a proof of the full proposition is more likely to
succeed through \(P_n^+\) than through \(P_n^-\).

---

## Files

- This note: `workspace/notes/step5_positive_branch_all_dimensions.md`
- Step 4 accounting: `workspace/notes/step4_preceptor_energy_accounting_and_route_review.md`
- Dossier: `Skills/qiushi-yau26/references/research/20260910.tex` (§3.3 positive/negative, §5.1)
