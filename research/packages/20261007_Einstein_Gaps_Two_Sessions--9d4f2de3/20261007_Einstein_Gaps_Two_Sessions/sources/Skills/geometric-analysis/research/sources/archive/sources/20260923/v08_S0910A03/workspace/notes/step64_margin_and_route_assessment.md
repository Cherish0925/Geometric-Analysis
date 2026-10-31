# Step 64: Margin analysis of Di Cerbo's exclusion and route restructure

Session: S0910A03. Agent1 / Orchestrator. Phase: Explore.

## 1. The Di Cerbo exclusion argument, decomposed by stability

Di Cerbo's Theorem 12 (closed extended graph 4-manifolds carry no Einstein metric)
rests on a chain whose steps have sharply different stability under approximate
negative Ricci pinching. We separate them.

Let \(M\) be a closed extended graph 4-manifold with pure pieces
\(\{(V_i,g_{-1})\}_{i=1}^k\), \(k\ge1\), and set
\(P=\sum_i\operatorname{Vol}_{g_{-1}}(V_i)\). The argument is:

1. **Minimal Ricci volume (CSS Proposition 12 + Theorem 4).**
   \(\operatorname{Vol}_{\mathrm{Ric}}(M)=P\).
   Uses: Bishop–Gromov entropy bound \(h(g)\le3\) for \(\operatorname{Ric}\ge-3g\),
   and the CSS inequality \(h(g)\operatorname{Vol}_g(M)^{1/4}\ge3P^{1/4}\).

2. **Gauss–Bonnet (Harder, Cheeger–Gromov).**
   \(2\chi(M)=\frac{3}{2\pi^2}P\).

3. **LeBrun's Lemma 7.** For a closed Einstein 4-manifold rescaled to
   \(\operatorname{Ric}=-3g\),
   \[
   2\chi(M)-3|\tau(M)|\ge\frac{3}{2\pi^2}\operatorname{Vol}_{\mathrm{Ric}}(M),
   \]
   with equality iff \(g\) is half-conformally flat and realizes
   \(\operatorname{Vol}_{\mathrm{Ric}}\). If moreover \(\tau(M)=0\) and equality
   holds, \(g\) is real-hyperbolic.

4. **Preissmann contradiction.** An extended graph manifold with a pure piece
   has \(\mathbb Z^3\subset\pi_1(M)\), so it cannot be real-hyperbolic.

## 2. Stability verdict

| Step | Stable? | Reason |
|------|---------|--------|
| 1. CSS \(\operatorname{Vol}_{\mathrm{Ric}}(M)=P\) | **No** | Bishop–Gromov entropy bound uses \(\operatorname{Ric}\ge-3g\) **pointwise**. Under \(\|\operatorname{Ric}+3g\|_\infty\le\delta\), \(\operatorname{Ric}\ge-(3+\delta)g\), so the available bound is \(h(g)\le3+\delta\), not \(h(g)\le3\). The CSS inequality gives only \(\operatorname{Vol}_g(M)\ge\frac{81}{(3+\delta)^4}P\), which **decreases** as \(\delta\to0\). |
| 2. Gauss–Bonnet \(2\chi(M)=\frac{3}{2\pi^2}P\) | **Yes** | Topological identity, independent of metric. |
| 3. LeBrun inequality | **Yes (inequality), No (rigidity)** | The inequality holds for every metric. But the rigidity conclusion (half-conformally flat, real-hyperbolic) is an equality characterization; it does not persist under approximate pinching. |
| 4. Preissmann | N/A | Only used at the exact-Einstein endpoint; irrelevant to the approximate problem. |

The exclusion is **exactly saturated** at every step: the hypothetical Einstein
metric would realize both the minimal Ricci volume and the LeBrun equality. There
is therefore **no slack anywhere** to absorb an \(O(\delta)\) perturbation.

## 3. The entropy margin is O(1), but in the wrong direction

One might hope that the CSS inequality retains an \(O(1)\) margin under pinching.
It does not. Writing the available entropy bound as \(h\le3+\delta\),
\[
\operatorname{Vol}_g(M)\ge\frac{81}{h^4}P
\ge\frac{81}{(3+\delta)^4}P
=P\Bigl(1-\frac{4\delta}{3}+O(\delta^2)\Bigr).
\]
The lower bound **relaxes** as the pinching tightens. Meanwhile
\(\operatorname{Vol}_{\mathrm{Ric}}(M)=P\) is a fixed topological target. So the
volume side has no positive margin; the available bound is always below the
minimal-Ricci-volume value by \(O(\delta)\).

The Gauss–Bonnet side is exact and \(O(1)\). Combining,
\[
2\chi(M)-3|\tau(M)|
=\frac{3}{2\pi^2}P
=\frac{3}{2\pi^2}\operatorname{Vol}_{\mathrm{Ric}}(M).
\]
A metric with \(\|\operatorname{Ric}+3g\|_\infty\le\delta\) satisfies
\(\operatorname{Ric}\ge-(3+\delta)g\), hence
\(\operatorname{Vol}_{\mathrm{Ric}}(M)\le\operatorname{Vol}_g(M)\)
only after rescaling; the inequality chain does not produce a contradiction for
any fixed \(\delta>0\).

## 4. Conclusion: no direct gap; two repair routes

**Di Cerbo's argument does not yield a quantitative pinching gap on extended
graph manifolds by inspection.** The obstruction is an equality-saturated
rigidity statement, and every step of the proof is at its boundary. This is the
same structural feature that makes the Seiberg–Witten/Ishida–LeBrun route require
the full cutoff-flow extraction machinery.

Two repair routes remain.

1. **Quantitative LeBrun rigidity (compactness).** Show that a sequence
   \(\|\operatorname{Ric}_{g_j}+3g_j\|_\infty\to0\) on a fixed extended graph
   \(M\) converges (in a suitable sense) to a half-conformally-flat Einstein
   metric, contradicting Preissmann. This requires a compactness theorem in the
   collapsing, Ricci-only-controlled regime—precisely the regime the session's
   cutoff-flow / Cheeger–Naber machinery addresses. It is not a cheap corollary.

2. **Direct geometric gap.** Prove that the necks/cusps of an extended graph
   manifold force an \(O(1)\) Ricci defect independent of Di Cerbo's argument.
   The Step 63 flat-slice barrier \(H^2\ge9-6\delta\) and the Preissmann
   dimension-three slice lemma (\(\|\operatorname{Ric}+2g\|_{\mathrm{op}}<2/3\)
   forces \(K<0\), impossible on \(T^3\)) are local obstructions of this kind.
   They show the simplest neck models cannot be made tight, but a general
   \(O(1)\) lower bound for arbitrary tight metrics on extended graph manifolds
   remains open.

The second route is the more promising negative-branch mechanism because it is
intrinsic and does not require resolving the compactness problem.

## 5. Dimension-three slice lemma (Strategist)

In dimension three,
\(\operatorname{Ric}=2Kg\) on any 2-plane. If
\(\|\operatorname{Ric}+2g\|_{\mathrm{op}}<\frac23\), then
\(\operatorname{Ric}<-\frac43g\), hence \(K<-\frac23<0\) everywhere. A closed
3-manifold with strictly negative sectional curvature has no \(\mathbb Z^2\)
subgroup (Preissmann), so the slice cannot be a \(T^3\). Consequently the
transition slices of an extended-graph neck cannot be intrinsically Ricci-close
to \(-2g\); they must remain anisotropic. The scalar constraint at the \(H=0\)
slice is \(R(\gamma)\approx-6-|S|^2\), satisfiable by
\((\mathbb H^2/\Gamma)\times S^1\) with \(\operatorname{Ric}=\operatorname{diag}(-3,-3,0)\),
but only off-isotropy. This converts the neck from a free construction into a
constrained ODE/design problem.

## 6. Route restructure after Step 64

- **Sectional-pinching counterexample routes are closed** (Anderson 2003,
  internally reviewed; flagged as preprint pending independent confirmation).
- **Graph-manifold route**: not a counterexample (Step 63); not a direct gap
  theorem (this Step). It is a candidate gap theorem only via a new intrinsic
  neck obstruction or a compactness/rigidity repair.
- **IL restricted route**: remains the most developed negative-branch gap
  candidate. A01's gate audit identifies the defect-Moser general-\(p\)
  inequality and nested recurrence as the blocking gap; A03's Codex report
  contains the relevant derivation (weighted mixed recurrence, not the rejected
  unweighted Moser).
- **Positive branch**: no counterexample known; treat primarily as existence
  (variational thresholds, weak limits, collapsed Kaluza–Klein). K-stability
  obstructs only Kähler–Einstein, not general Einstein.
- **\(n\ge5\)**: extended graph manifolds give the first concrete candidate
  topology class; the entropy estimate holds in all dimensions, but the
  LeBrun/Hitchin–Thorpe rigidity is four-dimensional. A higher-dimensional
  replacement is the missing ingredient.

## 7. Quantifier normalization (Step 1 restatement)

For \(n\ge4\), any metric can be rescaled into a cross-zero interval, so a valid
pinching interval \([c_n,C_n]\) cannot cross zero. Yau 26 reduces to two
independent single-sign questions. This is a restatement of the Step 1 branch
reduction, not a new foundation; the existential choice of interval and the
homothetic normalization remain explicit.

## 8. Remaining open actions

1. Prove or refute an \(O(1)\) intrinsic Ricci gap for extended graph necks
   (negative branch).
2. Close the defect-Moser general-\(p\) inequality and nested recurrence
   (IL restricted module; A01 owns, A03 Codex has the derivation).
3. Verify Anderson's preprint status independently before any load-bearing use.
4. Determine whether any closed manifold carries positive Ricci and no Einstein
   metric; if none, pursue positive-branch existence mechanisms.
5. Find a higher-dimensional replacement for the LeBrun rigidity step to extend
   the graph-manifold exclusion to \(n\ge5\).
