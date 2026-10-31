# Step 49: Corrected restricted negative IL theorem statement

Session: S0910A03. Agent2 / Constructor. Phase: Execute.

> **Supersedes** the hypothesis list in Step 47 `step47_consolidated_negative_IL_gap_theorem.md` §1.
> **Step 50 correction:** the proof modules are not yet an established theorem. The
> flow construction in `step49_normalized_flow_existence_and_extension.md` is superseded
> by `step50_normalized_yang_wang_verification.md`. The normalized start is reduced
> directly to Yang's transported smooth-tame inverse, while continuation depends on the
> coupled shifted-curvature/cutoff-jet Wang hierarchy. The restricted IL gap remains to
> be reassembled and rechecked after this replacement.

---

## 1. Corrected statement

**Theorem A (Restricted negative IL defect gap).**
*Let $m \in \{2,3\}$. Let $M = (\#_{j=1}^m X_j)\#N$ be a closed oriented smooth
4-manifold where:*

- *each $X_j$ is a closed simply-connected smooth 4-manifold carrying
  a monopole class $\mathfrak{a}_j$ with $\mathfrak{a}_j^2 = c_1^2(X_j) > 0$,*
- *the connected sum $M$ carries the full monopole sign family: all $2^m$ classes
  $\sum_{j=1}^m \varepsilon_j\mathfrak{a}_j$, $\varepsilon_j = \pm1$, are
  monopole classes of $M$ (in the sense of the Bauer–Furuta stable cohomotopy
  Seiberg–Witten invariant),*
- *$N$ is a closed oriented smooth 4-manifold with $b_+(N) = 0$,*
- *$q := D - A/3 \ge 0$, where $A = \sum c_1^2(X_j)$ and
  $D = 4m - (2\chi + 3\tau)(N)$.*

*Then $M$ does not admit an Einstein metric, and there exists $\delta_0 = \delta_0(M) > 0$
such that every smooth Riemannian metric $g$ on $M$ satisfies*

$$
\|g^{-1}(\operatorname{Ric}_g + g)\|_{L^\infty,\mathrm{op}} \ge \delta_0.
$$

**Corollary A.1 (Above-critical gap).**
*If $q/A \ge c > 0$, then $\delta_0 \ge \min(1/4, \sqrt{3c/16})$. No smoothing
argument is needed — this follows from the calibrated Chern–Weil identity alone.*

**Corollary A.2 (Family uniformity).**
*For fixed $m$ and any $A_{\max} > 0$, there exists $\delta_1 = \delta_1(m, A_{\max}) > 0$
such that $\delta_0(M) \ge \delta_1$ for every $M$ in the above family with
$A \le A_{\max}$.*

---

## 2. Source-supported sufficient conditions for the monopole sign family

The explicit monopole hypotheses in Theorem A are satisfied in the following
source-supported settings:

### 2.1 Ishida–LeBrun (Theorem 7, \cite{ishida_lebrun_2002})

Each $X_j$ is a simply-connected minimal complex surface of general type.
Then $\pm c_1(X_j)$ are basic classes of $X_j$, and for $m = 2$ or $3$, the
Bauer–Furuta refinement gives the full sign family on $M$.

*Sufficient condition:* $X_j$ simply connected, minimal, general type,
$c_1^2(X_j) > 0$; $N$ with $b_1(N) = 0$, $b_+(N) = 0$.

### 2.2 Ishida–LeBrun (Theorem D, \cite{ishida_lebrun_2003})

More generally, each $X_j$ is a closed simply-connected almost-complex 4-manifold
with $b_+(X_j) \equiv 3 \pmod{4}$ and nonzero mod-2 Seiberg–Witten invariant.
Under Bauer's congruence assumption, the stable cohomotopy refinement gives the
monopole sign family.

*Sufficient condition:* $X_j$ simply connected, almost-complex, $b_1(X_j) = 0$,
$b_+(X_j) \equiv 3 \pmod{4}$, nonzero mod-2 Seiberg–Witten or BF-admissible;
$N$ negative-definite (i.e., $b_+(N) = 0$) with $b_1(N) = 0$.

### 2.3 Why general type alone is insufficient

Step 48 correction: the assumptions "simply connected, general type" do not by
themselves establish the monopole sign family. The proof requires that the summands
$X_j$ contribute Seiberg–Witten basic classes that survive in the connected sum.
This is guaranteed by the Bauer–Furuta refinement under the conditions above, but
not by algebraic-geometric properties alone without the SW hypothesis.

---

## 3. Module S hypotheses (corrected)

Module S (the topology-independent smoothing module) takes as input:

**(S1)** A smooth closed Riemannian 4-manifold $(M, g)$ with initial Einstein defect
$$
\delta := \|g^{-1}(\operatorname{Ric}_g + g)\|_{L^\infty,\mathrm{op}} \le \delta_0.
$$

**(S2)** A curvature-to-volume budget: $\int_M|\operatorname{Rm}|^2\,d\mu \le \kappa_0^2
\operatorname{Vol}(M, g)$, where $\kappa_0$ depends on the geography.

**(S3)** A positive total volume lower bound: $\operatorname{Vol}(M, g) \ge v_0 > 0$.

**(S4)** Buffered supports with uniform gradient bounds: the good-support construction
from maximal-function selection yields cutoff functions $\chi_\alpha$ with
$\|\nabla\chi_\alpha\|_\infty \le C/r$ and uniform geometry.

**Why (S1) is needed separately from a Ricci lower bound:**
- The $J_6$ defect seed requires $J_6(0) \le C\delta^6\operatorname{Vol}$.
- The global $Q(0) = \int|E|^2 = O(\delta^2\operatorname{Vol})$ estimate
  requires the $L^\infty$ initial defect.
- The defect Moser iteration and small metric drift both use
  $\delta = \|E\|_\infty$ multiplicatively.
- A Ricci lower bound $\operatorname{Ric} \ge -Kg$ does not provide these:
  it controls volume comparison and Sobolev constants but not the defect
  power hierarchy.

**Why (S2) is needed:**
- The maximal-function threshold selects good balls with local
  $\int_{B_r}|\operatorname{Rm}|^2 \le \kappa_0^2\operatorname{Vol}(B_r)$.
- The collapse-independent Sobolev absorption parameter is
  $\gamma = \mathcal S \cdot K_2^{1/2} \le Cr^2\sqrt{1+\kappa_0^2}$
  (the $\operatorname{Vol}^{-1/2}$ in $\mathcal S$ cancels against the
  $\operatorname{Vol}$ in $K_2$, critical dimension 4).
- The IL geography provides $\kappa_0^2 \le C(A)$ via Chern–Weil.

---

## 4. Module O interface (summary)

Module O supplies:

**(O1)** The Ishida–LeBrun theorem: under the monopole hypotheses above, $M$ does
not admit an Einstein metric.

**(O2)** The calibrated Chern–Weil identity: for the scalar $s$, self-dual Weyl
$W^+$, and scalar-Weyl density $G = f^2 - (b_-)^2$ where
$f = (2s/3 + 2w)_-$ and $w = \min\operatorname{Spec}(W^+)$:
$$
\int G \le 6Q + 48\pi^2(-q_{\rm top})_+,
\tag{O.1}
$$
valid for every smooth metric on every manifold in the family (using LeBrun's
spectral inequality for every $H$-adapted metric, not only Yamabe minimizers).

**(O3)** The terminal density $\mathfrak D = |E|^2 + (s+4)^2 + (s+8\sqrt6|W^+|)^2 + G$
satisfies
$$
\int\mathfrak D \le 119Q + 912\pi^2(-q_{\rm top})_+.
\tag{O.2}
$$
For $q_{\rm top} \ge 0$, the last term vanishes.

**(O4)** The spectral zero set of $\mathfrak D$ forces Spec$(W^+) = (-1/6, 1/12, 1/12)$,
contradicting the Derdziński projector/Bochner obstruction on any Einstein metric.

---

## 5. Proof architecture (corrected logical order)

Assume for contradiction a sequence $(M_i, g_i)$ in the family with $\delta_i \to 0$.

### Phase 1: Calibration (pure topology/algebra, no flow)
- Near-equality Chern–Weil analysis gives calibrated profiles: $s_i \to -4$,
  $\operatorname{Ric}^\circ_i \to 0$ in $L^2$, volume convergence, calibrated Weyl.
- For $q > 0$: the above-critical gap (Corollary A.1) gives a contradiction directly.
- For $q = 0$ (or $q/A \to 0$ along the sequence): the flow argument is needed.

### Phase 2: Per-datum flow construction (Theorem 4.1 of companion note)
- For each $(M_i, g_i)$, select good supports via the Hardy–Littlewood maximal function
  with threshold $\kappa_0^2/r^4$.
- Construct the normalized cutoff flow via coefficient regularization ($\varepsilon$-independent
  energy bounds, $\varepsilon \to 0$ passage).
- This gives an exact smooth flow $g_i(t)$ on $[0, T_{0,i}]$ for each datum.

### Phase 3: Sequence-uniform first-exit bootstrap
- Applied to the EXACT $\varepsilon = 0$ flows.
- Uses stationary collars, disjoint-support summation, localized $K_2/J_m/Q$.
- Self-improving estimates give a common observation time $T = \theta r^2$.
- Continuation (§6 of companion note) ensures the flow reaches $T$.

### Phase 4: Terminal contradiction
- At time $T$, terminal curvature charts have bounded curvature and small defect.
- Core-ball Lipschitz control (from Shi + Bishop–Gromov) gives $\sup\mathfrak D \to 0$.
- The spectral zero set forces $\operatorname{Spec}(W^+) = (-1/6, 1/12, 1/12)$.
- The Derdziński/projector–Bochner obstruction gives $0 = -1/8$. Contradiction.

---

## 6. What remains conditional

1. **The staggered derivative induction at arbitrary order:** Steps 40, 44, 45
   develop the tensor combinatorics and weight structure. The exact provenance of
   every nonlinear tensor contraction at order $m \ge 3$ is structurally classified
   but not yet carried through as a complete formal induction with all constants.

2. **The per-datum start vs. sequence-uniform interface:** Theorem 4.1 gives a
   per-datum $T_0(g_i, \chi_i)$. The localized first-exit estimates then produce
   a common $T = \theta r^2$ depending only on support parameters. The formal
   connection between these two regimes — ensuring that the per-datum $T_0 \ge T$
   or that the continuation mechanism bridges any gap — is structurally clear
   from §6 but requires the complete staggered estimates to be formally closed.

3. **The broader Yau Problem 26:** The restricted theorem covers only the
   four-dimensional negative IL geography with $q \ge 0$. Positive pinching,
   arbitrary four-manifold topology, dimensions $n \ge 5$, dimension-only
   constants, and Lean 4 formalization are all untouched.
