# TTCS Independent Branch Record

```json
{
  "step_id": 89,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/step58_consolidated_hypothesis_ledger.md",
    "Sessions/S1003A02/workspace/notes/step54_k1_ball_quotient_attainment_theorem.md",
    "Sessions/S1003A02/trace/ttcs/results/step87_ttcs01_verifier1_integration.md",
    "Sessions/S1003A02/trace/ttcs/results/step87_ttcs01_verifier2_integration.md",
    "Knowledge/objects/papers/Geography-of-4-manifolds-with-positive-scalar-curvature--ea1844e3f622--6263e9f8807e/object.md"
  ]
}
```

## Task

Scientist-reader check of Step-88 integration and the oldest package §§2–12. Read the actual theorem package, the Step-87 verifier memos, the current hypothesis ledger, and the Step-54 source note. Identify only mathematically consequential remaining errors or scope mismatches, especially: (i) Theorem 87.O and whether its signature and connected-sum lower construction justify the exact orbifold supremum; (ii) the negative-Yamabe exclusion; (iii) the Γ-vertex replacement for Lemma 54.3, including factorization of the classifying map and multi-ended cap compactification; (iv) stale P_* versus human α language, retired status statements, and historical route headings in §§2–12. Give exact replacement prose/equations for any issue and say when current text is sound. Do not propose new computations or weaken the active open problem.

## Output

## Scientific memo: Step-88 integration and early package sections

The repaired package is mathematically coherent on the main points requested. The remaining consequential edits are mostly precision edits: Theorem 87.O needs an explicit gluing/domain sentence and a clearer Euler-characteristic computation; the Yamabe-sign exclusion should display the two inequalities it uses; the Γ-vertex argument should state the factorization through the capped summand explicitly, especially for multi-ended caps; and §§2–12 plus the Step-58 ledger still contain retired notation and a few stale conflations of \(P_*\) with \(\alpha\).

---

### 1. Theorem 87.O: exact orbifold supremum for ball-quotient hosts

The theorem as repaired is sound.

Let \(X\) be a compact ball quotient, \(A=c_1^2(X)\), and
\[
V_m=X\# m(S^4/\mathbb Z_2)
\]
with connected sums at smooth points. The Satake orbifold numbers are
\[
\chi_{\rm orb}(X)=\frac A3,\qquad \tau_{\rm orb}(X)=\frac A9,
\]
and
\[
\chi_{\rm orb}(S^4/\mathbb Z_2)=1,\qquad \tau_{\rm orb}(S^4/\mathbb Z_2)=0.
\]
Each smooth-point connected sum with \(S^4/\mathbb Z_2\) changes the orbifold Euler characteristic by
\[
+1-2=-1,
\]
and leaves the orbifold signature unchanged. Hence
\[
\chi_{\rm orb}(V_m)=\frac A3-m,\qquad \tau_{\rm orb}(V_m)=\frac A9.
\]

Using the orbifold signature identity in the registered convention, with zero \(A_1\)-link correction,
\[
I_+-I_-=12\pi^2\tau_{\rm orb}(V_m)=\frac{4\pi^2A}{3}.
\]
Therefore every orbifold metric satisfies
\[
I_++I_-\ge \frac{4\pi^2A}{3},
\]
and so
\[
d_{\rm orb}(g)
=8\pi^2\chi_{\rm orb}(V_m)-(I_++I_-)
\le 8\pi^2\left(\frac A3-m\right)-\frac{4\pi^2A}{3}
=4\pi^2\left(\frac A3-2m\right).
\]

The lower side is also adequate, but the text should say explicitly that the Kobayashi gluing argument is being used at smooth points and away from singular points. The connected-sum lower estimate is
\[
d_{*,\rm orb}(V_m)
\ge d_*(X)+m\,d_{*,\rm orb}(S^4/\mathbb Z_2)-16\pi^2 m.
\]
Since
\[
d_*(X)=\frac{4\pi^2A}{3},
\qquad
d_{*,\rm orb}(S^4/\mathbb Z_2)=8\pi^2,
\]
this gives
\[
d_{*,\rm orb}(V_m)
\ge \frac{4\pi^2A}{3}+8\pi^2m-16\pi^2m
=4\pi^2\left(\frac A3-2m\right).
\]
Thus the exact supremum follows.

**Replacement prose for the lower construction in Theorem 87.O:**

> Conversely, perform the conformal connected sum at smooth points, with gluing balls disjoint from the singular points. The standard Kobayashi gluing argument is unchanged in this orbifold setting and gives orbifold metrics for which \(I_++I_-\) approaches \(4\pi^2A/3\). Equivalently,
> \[
> d_{*,\rm orb}(V_m)
> \ge d_*(X)+m\,d_{*,\rm orb}(S^4/\mathbb Z_2)-16\pi^2m
> =4\pi^2\left(\frac A3-2m\right).
> \]

**Replacement prose for the Euler-characteristic sentence:**

> Each smooth-point connected sum with \(S^4/\mathbb Z_2\) changes \(\chi_{\rm orb}\) by \(+1-2=-1\) and leaves \(\tau_{\rm orb}\) unchanged; hence
> \[
> \chi_{\rm orb}(V_m)=\frac A3-m,\qquad \tau_{\rm orb}(V_m)=\frac A9.
> \]

With these clarifications, Theorem 87.O is correct. The statement also correctly implies that an Einstein orbifold of this type must have
\[
d_{*,\rm orb}(V_m)>0
\iff
2m<\frac A3,
\]
or equivalently \(m<A/6\), because for an Einstein orbifold \(R=6d>0\).

---

### 2. Yamabe-sign exclusion for general-type blow-ups

The exclusion using \(\mathcal Y(M)<0\) is correct, but the proof should display both inequalities.

For
\[
M=X\#k\overline{\mathbb{CP}}^2,
\]
LeBrun’s Yamabe theorem gives
\[
\mathcal Y(M)=-4\pi\sqrt{2A}<0.
\]
For any metric \(g\), let \(s_g^-\) be the part of the scalar curvature below zero. The Yamabe quotient gives
\[
Y([g])\ge -\|s_g^-\|_{L^2}.
\]
Since
\[
\mathcal Y(M)=\sup_{[h]}Y([h])=-4\pi\sqrt{2A},
\]
every conformal class satisfies
\[
Y([g])\le -4\pi\sqrt{2A}.
\]
Combining the two inequalities gives
\[
\|s_g^-\|_{L^2}\ge 4\pi\sqrt{2A},
\]
that is,
\[
\int_M (s_g^-)^2\,d\mu_g\ge 32\pi^2A.
\]

In the cutoff families of Lemma 86.S and Lemma 86.S′ whose bulk is Ricci-flat or has Einstein constant \(>0\), the scalar curvature below zero is supported only in shrinking transition regions, and the balanced cutoff gives
\[
\|s_{g_\varepsilon}^-\|_{L^2}\to0.
\]
Such families therefore cannot produce metrics on \(M=X\#k\overline{\mathbb{CP}}^2\). Consequently, within these Ricci-flat ALE or Wahl-smoothing architectures, any Einstein orbifold bulk absorbed into a general-type blow-up must have Einstein constant \(<0\).

**Replacement prose for the exclusion paragraph in Lemma 86.S:**

> For \(M=X\#k\overline{\mathbb{CP}}^2\), LeBrun’s theorem gives
> \[
> \mathcal Y(M)=-4\pi\sqrt{2A}<0.
> \]
> For every metric,
> \[
> Y([g])\ge -\|s_g^-\|_{L^2}.
> \]
> Since every conformal class has \(Y([g])\le \mathcal Y(M)\), one obtains
> \[
> \|s_g^-\|_{L^2}\ge 4\pi\sqrt{2A},
> \qquad
> \int (s_g^-)^2\ge 32\pi^2A.
> \]
> In the cutoff families of Lemma 86.S and Lemma 86.S′ with Ricci-flat bulk or Einstein constant \(>0\), \(\|s_{g_\varepsilon}^-\|_{L^2}\to0\). Hence such families cannot have limit topology \(M\). Any Einstein orbifold absorbed into a general-type blow-up through these Ricci-flat ALE or Wahl constructions therefore has Einstein constant \(<0\).

This is a statement about those glued families. It does not by itself exclude arbitrary degenerations, and the current package already says so.

---

### 3. Γ-vertex replacement for Lemma 54.3

The Step-87 Γ-vertex proof order is sound and is stronger than the older route through Lemma 54.3 for ball-quotient hosts. Two formulations should be made explicit.

#### 3.1 Factorization of the classifying map

Let
\[
M_k=X\#k\overline{\mathbb{CP}}^2,
\qquad
\Gamma=\pi_1(X).
\]
In a trivial-group case-(I) configuration, the connected-sum graph has one vertex \(Y\) carrying \(\Gamma\); all other vertices are simply connected, and there are no graph loops because \(\Gamma\) is torsion-free, one-ended, and freely indecomposable.

The inclusion \(Y\hookrightarrow M_k\) induces an isomorphism on \(\pi_1\). Let \(\widehat Y\) denote the compactification of \(Y\) obtained by adding one point for each end, if \(Y\) is a bubble cap. There is a collapse/pinch map
\[
q:M_k\to \widehat Y
\]
of degree one. The classifying map
\[
f:M_k\to X=B\Gamma
\]
is homotopic to
\[
f_Y\circ q,
\]
where \(f_Y:\widehat Y\to X\) classifies \(\widehat Y\). Since
\[
f_*[M_k]=[X],
\qquad
q_*[M_k]=[\widehat Y],
\]
one obtains
\[
(f_Y)_*[\widehat Y]=[X].
\]
Thus \(f_Y\) has degree one. Consequently,
\[
H^2(X;\mathbb Q)\hookrightarrow H^2(\widehat Y;\mathbb Q)
\]
by degree-one intersection-form injection, and therefore
\[
b^+(\widehat Y)\ge b^+(X)\ge3.
\]

**Replacement prose for the factorization sentence:**

> Since all other summands are simply connected, the inclusion \(Y\hookrightarrow M_k\) induces an isomorphism on \(\pi_1\). Let \(q:M_k\to\widehat Y\) be the collapse map to the compactified summand. The classifying map \(f:M_k\to X=B\Gamma\) is homotopic to \(f_Y\circ q\), where \(f_Y:\widehat Y\to X\) classifies \(\widehat Y\). Because \(q_*[M_k]=[\widehat Y]\) and \(f_*[M_k]=[X]\), the map \(f_Y\) has degree one. Hence \(Q_X\hookrightarrow Q_Y\) rationally and \(b^+(\widehat Y)\ge b^+(X)\ge3\).

#### 3.2 Multi-ended cap compactification

If the \(\Gamma\)-carrying summand \(Y\) were a bubble cap with several ends, the relevant closed object is its multi-end compactification \(\widehat Y\). Lemma 53.Y, under \(H_{\rm dec}\), gives a PSC metric on \(\widehat Y\). But the degree-one map \(\widehat Y\to X\) makes \(\widehat Y\) essential, and Mantione–Torres Proposition 2 forbids PSC on an essential manifold whose fundamental group is that of a closed four-manifold with sectional curvature \(<0\), such as a ball quotient. Therefore the \(\Gamma\)-carrying summand cannot be a bubble cap; it is a bulk component.

**Replacement prose for the bubble-cap exclusion:**

> If the \(\Gamma\)-carrying summand were a bubble cap \(N\) with \(e\) ends, compactify it by adding one point at each end to obtain \(\widehat N\). The collapse map \(M_k\to\widehat N\) has degree one, so the induced classifying map \(\widehat N\to X\) has degree one. Lemma 53.Y and \(H_{\rm dec}\) give a PSC metric on \(\widehat N\), while Mantione–Torres Proposition 2 forbids PSC on an essential manifold with this fundamental group. Hence the \(\Gamma\)-carrying summand is a bulk component.

With these edits, the Γ-vertex argument replaces Lemma 54.3 for ball-quotient hosts. Lemma 54.3 may remain recorded as a standalone \([P^*]\) statement for other hosts, but it is not part of the proof of Theorem 54.A in the ball-quotient case.

#### 3.3 Superseded paragraph in the Step-54 source note

The Step-54 source note still contains, in the original proof of Theorem 54.A(iii), a passage using SW transfer through a PSC homotopy sphere. The binding erratum at the top supersedes it, but the body text should be replaced to avoid contradiction.

**Replacement for the old SW-transfer paragraph in Step-54, proof of Theorem 54.A(iii):**

> Since \(V\) is essential and \(\pi_1(V)=\Gamma\), Mantione–Torres Proposition 2 excludes PSC on \(V\). Thus the constant scalar curvature of the \(P\)-critical metric \(g_0\) is not \(>0\). If \(s_{g_0}=0\), Bourguignon’s theorem makes \(g_0\) Ricci-flat; Cheeger–Gromoll then makes \(\pi_1(V)\) virtually abelian, which is impossible for a cocompact lattice in \(PU(2,1)\). Hence \(s_{g_0}<0\). The Einstein/non-Bach-flat dichotomy follows from the one-line Bach-flat argument in §0.8.

This replacement is consistent with the Step-87 proof order and with the package §15.

---

### 4. Stale notation and retired statements in §§2–12 and in the Step-58 ledger

The Step-86 pass corrected §§13–24, but several older sections still use retired notation or mix \(P_*\) with \(\alpha\). The following replacements are consequential.

#### 4.1 Theorem package §§2–12

##### 4.1.1 Theorem D and the diagonal cell infimum

In §4.1, Theorem D uses \(p^{\rm diag}_{1,0}\) for an infimum. Since the package now reserves lowercase \(p\) for the value at one metric, replace this by a normalized infimum symbol.

**Replacement in Theorem D:**

> Let
> \[
> \mathfrak p^{\rm diag}_{1,0}=\inf \widehat P
> \]
> over diagonal Bianchi–IX metrics on \(O(-1)\) with an exact CH collar. Equivalently,
> \[
> P^{\rm diag}_{1,0}=8\pi^2\mathfrak p^{\rm diag}_{1,0}
> \]
> is the dimensional infimum.

In Theorem D(iii), replace
\[
p^{\rm diag}_{1,0}>0
\]
by
\[
\mathfrak p^{\rm diag}_{1,0}>0
\]
or equivalently \(P^{\rm diag}_{1,0}>0\).

##### 4.1.2 §6.3

Current text says that Theorem E is not a proof that \(p_{1,0}=0\). Replace by:

> The theorem supplies a possible compactness endpoint and an existence result, not a proof that
> \[
> \mathfrak p^{\rm diag}_{1,0}=0
> \]
> or equivalently \(P^{\rm diag}_{1,0}=0\).

##### 4.1.3 §7 common mechanism

Two edits are needed.

First, the phrase “positivity of \(p_{1,0}\)” should be replaced by positivity of the dimensional cell infimum:

> Still open: the global compactness/localization theorem that would turn the certified local first- and second-order cell laws into unrestricted infimum information; positivity of \(\mathfrak P_{1,0}\); equality of global and cell asymptotics; standard-CR diagonal nonexistence; and a universal degeneration theorem.

This also replaces the older “full \(-9\) remainder” item. The local second-order coefficient is now covered by Theorem 57.Φ/Theorem 59.R on \(P\)-critical backgrounds; the remaining issue is the global passage from those local laws to arbitrary near-minimizers.

Second, later in §7, replace

> Positivity of \(p_{1,0}\) must come from intrinsic Weyl–volume geometry

by

> Positivity of \(\mathfrak P_{1,0}\) must come from intrinsic Weyl–volume geometry

or, if using the normalized version,

> Positivity of \(\mathfrak p_{1,0}=\mathfrak P_{1,0}/(8\pi^2)\) must come from intrinsic Weyl–volume geometry.

##### 4.1.4 §9, item 5

Replace

> determine whether \(p_{1,0}>0\)

by

> determine whether \(\mathfrak P_{1,0}>0\), equivalently whether \(\mathfrak p_{1,0}>0\).

##### 4.1.5 Historical theorem labels

There are two different objects called “Theorem E”: the affine pointwise exhaustion in §3.6 and the complete nonstandard-CR filling in §6. This is not a mathematical error by itself, but it can obscure cross-references. A clean editorial repair is:

- In §3.6, rename “Theorem E” as “Theorem \(E_{\rm aff}\)” or “affine exhaustion theorem.”
- In §4.1, where the older diagonal-cell statement is discussed, refer to “the earlier diagonal-cell zero-cost statement” rather than “Theorem E.”

This preserves all mathematical content.

#### 4.2 Step-58 consolidated hypothesis ledger

The Step-58 ledger predates the final \(P_*\)/\(\alpha\) split and needs explicit replacement text.

##### 4.2.1 Conventions

Replace

> \(p_*(M)=\inf P\)

by

> \(P_*(M)=\inf_g P(g)\), and \(\alpha(M)=\inf_g\mathscr D(g)\). The retired symbol \(p_*\) is not used in current statements.

Every occurrence of \(p_*\) in the ledger should be read as \(P_*\), unless the statement is explicitly about \(\alpha\).

##### 4.2.2 Upper bound (U)

Replace

> \(p_*(M)<8\pi^2k\)

by

> \(P_*(M)<8\pi^2k\).

##### 4.2.3 Theorem 57.Φ formal consequence

Replace

> Hence \(p_*(X\#k\overline{\mathbb{CP}}^2)<8\pi^2k\)

by

> Hence \(P_*(X\#k\overline{\mathbb{CP}}^2)<8\pi^2k\).

##### 4.2.4 Proposition 56.U

Replace

> \(p_*(M')\le P(V,g)\)

by

> \(P_*(M')\le P(V,g)\).

The \(\alpha\)-version should be stated separately:

> By Lemma 86.S, if \((V,g)\) is Einstein with nonzero Einstein constant, then \(\alpha(M')=0\). If the bulk is Ricci-flat, this construction gives \(P_*(M')=0\) and the simple cutoff family has \(\mathscr D\to4\); no \(\alpha\) conclusion follows from that family alone.

##### 4.2.5 Theorem 56.A(i)

The ledger currently says

> \(p_*(M)=P(V,g_0)=\alpha_{\rm orb}(V)\).

This conflates \(P_*\) and \(\alpha\). Replace by:

> \[
> P_*(M)=P_{*,\rm orb}(V)=P(V,g_0).
> \]
> If the attained orbifold metric has nonzero Einstein constant, Lemma 86.S gives
> \[
> \alpha(M)=\alpha_{\rm orb}(V)=0
> \]
> after Ricci-flat ALE or Wahl smoothing. If the attained orbifold metric is Ricci-flat, the cutoff family gives \(P_*(M)=0\), while the same family has \(\mathscr D\to4\); no conclusion about \(\alpha(M)\) follows from that family alone.

##### 4.2.6 Corollary 56.B

Replace

> An Einstein orbifold metric on such \(V\) forces \(\alpha(M')=0\)

by

> An Einstein orbifold metric with nonzero Einstein constant on such \(V\) gives \(\alpha(M')=0\) after Ricci-flat ALE or Wahl smoothing. A Ricci-flat orbifold bulk gives \(P_*(M')=0\), and the simple cutoff family has \(\mathscr D\to4\); no \(\alpha\) conclusion follows from that family alone.

##### 4.2.7 Proposition 58.O attainment sentence

Replace

> \(\alpha(M')=0\) is attained iff \(M'\) carries an Einstein metric

by

> \(\alpha(M')=0\) is attained iff \(M'\) carries an Einstein metric with nonzero Einstein constant.

This matches the general identity recorded in §1 and §22.4.

#### 4.3 Step-54 source note

The source note begins with a binding erratum stating that \(p_*\) below is the trace-free infimum \(P_*\). That is enough for notation, but for current citation one may replace the conventions line by:

> Conventions. \(P(g)=\int|\operatorname{Ric}^\circ|^2\), \(P_*(M)=\inf P\), \(T_+=2\chi+3\tau\). The older symbol \(p_*\) appearing below is the retired notation for \(P_*\); no statement in this note concerns \(\alpha\).

The mathematical content of Theorem 54.A, with the Step-87 proof order and the replacement paragraph in §3.3 above, is sound.

---

### 5. Items already sound

The following requested points are already correct in the repaired package:

1. The exact value
   \[
   d_{*,\rm orb}(V_m)=4\pi^2\left(\frac A3-2m\right)
   \]
   for ball-quotient hosts follows from the orbifold signature upper estimate and the Kobayashi connected-sum lower estimate.

2. The conservation of Weyl deficit under shrinking Ricci-flat ALE resolution is correct:
   \[
   d(M,g_\varepsilon)\to d_{\rm orb}(V,g).
   \]
   For Eguchi–Hanson resolution,
   \[
   \Delta\chi=3m,\qquad \Delta\mathcal W=24\pi^2m=8\pi^2\Delta\chi,
   \]
   so the deficit is preserved in the shrinking limit.

3. The Yamabe-sign exclusion correctly forces any absorbed Einstein orbifold for a general-type blow-up, within the stated Ricci-flat ALE/Wahl architectures, to have Einstein constant \(<0\).

4. The Γ-vertex proof order for Theorem 54.A is valid for ball-quotient hosts and removes the dependence on Lemma 54.3 in that case.

5. The repaired Corollary 52.8 distinction is correct:
   \[
   P_{*,\rm orb}(X\#S^4/\mathbb Z_2)=\frac12P_*^\iota(X\#X),
   \]
   but
   \[
   \alpha_{\rm orb}(X\#S^4/\mathbb Z_2)=\alpha^\iota(X\#X),
   \]
   with no factor \(1/2\) for \(\alpha\).

6. The active open problem in the hard range
   \[
   0<k<\frac A3
   \]
   remains intact. The edits above do not weaken it. The unresolved substance remains a global inequality or construction that controls the joint data \((\kappa,\upsilon)\), sees individual exceptional classes, and remains compatible with certified sub-\(8\pi^2\) cells, lattice absorption, and the known orbifold-channel restrictions.