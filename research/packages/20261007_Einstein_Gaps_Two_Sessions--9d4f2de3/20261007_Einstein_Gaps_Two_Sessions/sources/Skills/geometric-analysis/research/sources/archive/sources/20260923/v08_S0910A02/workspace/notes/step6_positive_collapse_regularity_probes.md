# Step 6: positive-branch collapse and regularity probes

Session: S0910A02. Agent3/Actuator. Phase: Explore.

## 0. Purpose and target fidelity

The active target remains the full Yau Problem 26 proposition, equivalently in a fixed dimension the disjunction of positive and negative sign-normalized branches. This note works only on the positive branch, especially the four-dimensional regimes exposed in Steps 4--5:

\[
  \delta_+(g):=\|\operatorname{Ric}_g-g\|_{g\text{-op}}\to0.
\]

The Step-5 positive program correctly identified automatic positive-branch controls (Myers diameter, volume upper bound, \(b_1=0\), finite \(\pi_1\)) but overcorrected the noncollapsed case and still contained two misleading proposed experiments. This Step performs cheap checks that can change route judgment without pretending to prove \(P_n^+\).

Main output: the simplest smooth free circle collapse model -- a constant-fibre-length principal connection metric -- is not the tight positive-pinch enemy in dimension 4; positive-compatible collapse must either use more general warped/inhomogeneous collapse terms or, more plausibly in the four-dimensional CGB accounting, quotient/orbifold/singular/fixed-point strata where Euler characteristic and curvature energy are loaded onto concentration regions. The regularity bridge is sharpened: Cheeger--Naber and Naber--Zhang give harmonic-radius/measure/topology tools under bounded Ricci, but pointwise curvature and Einstein-orbifold gluing still require an Einstein equation, \(\nabla\operatorname{Ric}\) control, or extra structure not supplied by \(C^0\) Ricci pinching.

Artifacts:

- script: `Sessions/S0910A02/workspace/scripts/step6_positive_collapse_probes.py`
- data: `Sessions/S0910A02/workspace/data/step6_positive_collapse_probes.json`

---

## 1. Correction to the Step-5 collapse experiment

The Step-5 plan suggested extending the fixed-connection Berger computation. That would only rediscover an already understood fact: shrinking a fixed connection makes vertical Ricci too small and gives \(\delta_+\to1\). But exact round lens spaces collapse with \(\delta_+=0\), so the relevant collapse scaling is not fixed curvature; it is the Kaluza--Klein scaling in which the rescaled curvature stays order one.

Consider a principal circle connection metric

\[
  g_t = \pi^*g_B + t^2\alpha^2,
  \qquad d\alpha=F,
\]

on a closed 4-manifold with smooth free \(S^1\)-fibres over a closed 3-manifold \((B^3,g_B)\). Let \(U=t^{-1}\xi\) be the unit vertical vector and set

\[
  \phi=tF, \qquad \phi=*b
\]

on the base. With the standard differential-form norm \(|F|^2=\sum_{i<j}F_{ij}^2\), O'Neill/Kaluza--Klein gives, up to sign convention in the mixed term,

\[
\begin{aligned}
  \operatorname{Ric}_{M}(X,Y)
  &=\operatorname{Ric}_{B}(X,Y)-\frac12(\phi\circ\phi)(X,Y),\\
  \operatorname{Ric}_{M}(U,U)&=\frac12|\phi|^2,\\
  \operatorname{Ric}_{M}(X,U)&=\pm\frac12(d^*\phi)(X).
\end{aligned}
\]

Here \((\phi\circ\phi)_{ij}=\sum_k \phi_{ik}\phi_{jk}\). In dimension three,

\[
  \phi=*b,\qquad \phi\circ\phi=|b|^2g_B-b\otimes b.
\]

Thus exact \(\operatorname{Ric}_M=g_M\) would force

\[
  |b|^2=2,
  \qquad d^*\phi=0,
  \qquad d\phi=0,
  \qquad \operatorname{Ric}_B=2g_B-\frac12 b\otimes b.
\]

Since \(d\phi=0\) means \(\delta b=0\), while \(d^*\phi=0\) means \(db=0\), the base would carry a nonzero harmonic one-form. But along \(b\), the horizontal equation gives

\[
  \operatorname{Ric}_B(b,b)=|b|^2>0,
\]

contradicting the Bochner identity for harmonic one-forms on a closed base. Therefore a constant-fibre-length smooth free principal-circle connection metric with bounded base geometry cannot be exactly positive Einstein in dimension four. A general free collapse with nonconstant fibre length or mean-curvature/dilaton terms requires a separate extension of the formula; the present calculation is a discriminator, not a universal collapse theorem.

### Quantitative pinching version

If \(\|\operatorname{Ric}_M-g_M\|_{op}\le\delta\), the same formulas give

\[
  |b|^2\ge 2(1-\delta),\qquad |db|=|d^*\phi|\le 2\delta,
  \qquad \delta b=0,
\]

and, using the horizontal component in the \(b\)-direction,

\[
  \operatorname{Ric}_B(b,b)\ge(1-\delta)|b|^2.
\]

The Weitzenbock identity for one-forms on \(B\) gives

\[
  \int_B\operatorname{Ric}_B(b,b)
  \le \int_B(|db|^2+|\delta b|^2)
  \le 4\delta^2\operatorname{Vol}(B).
\]

Combining with the lower bound on \(|b|^2\) yields a contradiction whenever

\[
  2(1-\delta)^2>4\delta^2,
  \qquad\text{i.e.}\qquad
  \delta < \frac{1}{1+\sqrt2}\approx0.414213562.
\]

This constant is not claimed to be optimal; it is a convention-dependent model calculation. Its value is that it directly tests the pinching-compatible scaling \(\phi=tF=O(1)\), rather than the irrelevant fixed-connection scaling.

The script `step6_positive_collapse_probes.py` records sample values:

```text
Free S^1 Kaluza-Klein Bochner threshold δ >= 0.414213562
  δ=0.010000: lower=1.960200, upper=0.000400, contradiction=True
  δ=0.050000: lower=1.805000, upper=0.010000, contradiction=True
  δ=0.100000: lower=1.620000, upper=0.040000, contradiction=True
  δ=0.200000: lower=1.280000, upper=0.160000, contradiction=True
```

### Relation to topology and CGB accounting

A free circle action on a compact manifold forces \(\chi(M)=0\). But for a closed oriented four-manifold with \(\delta_+(g)<1/2\), the Step-4/TTCS CGB estimate gives

\[
  \int_M |W|^2+\beta(\delta)\operatorname{Vol}(M,g)
  \le 8\pi^2\chi(M),\qquad \beta(\delta)>0,
\]

so \(\chi(M)>0\). Also positive Ricci gives \(b_1=0\), hence \(\chi=2+b_2\ge2\) in the oriented case. Thus a global smooth free \(S^1\)-bundle cannot even be the topology of a tight positive-pinched four-manifold.

Consequently the four-dimensional collapse gap does not stand independent of curvature concentration. Regular free-collapse pieces may exist only away from regions where the Euler characteristic and CGB curvature energy are carried; any positive-compatible collapsed counterexample must either exploit warped/inhomogeneous free-collapse terms not captured by the constant-length model, or involve singular orbit strata, fixed-point strata, orbifold quotient collapse, or curvature-concentration caps. This is consistent with exact odd-dimensional lens-space/Sasaki--Einstein quotient collapse: those collapsed manifolds are already Einstein-compatible, and in dimension four the free circle model is blocked by Euler/Bochner accounting.

---

## 2. S^4 normalization and cheap rotational ansatz probe

The Step-5 proposed test used the wrong comparison volume. For metrics normalized by \(\operatorname{Ric}=g\) on \(S^4\), the round radius is \(\sqrt3\) and

\[
  \operatorname{Vol}(S^4_{\operatorname{Ric}=g})
  =\frac{8\pi^2}{3}(\sqrt3)^4
  =24\pi^2\approx236.8705.
\]

The unit-radius value \(8\pi^2/3\approx26.3189\) has \(\operatorname{Ric}=3g\), not \(\operatorname{Ric}=g\). With \(\chi(S^4)=2\) and \(\beta(0)=2/3\), the round \(\operatorname{Ric}=g\) metric exactly saturates

\[
  \beta(0)\operatorname{Vol}=8\pi^2\chi(S^4)=16\pi^2.
\]

The script also records the ALE Ricci-flat energy normalization:

\[
  \frac{1}{8\pi^2}\int |Rm|^2 = \chi(X)-\frac1{|\Gamma|},
\]

so Eguchi--Hanson has \(\chi=2\), \(|\Gamma|=2\), and

\[
  \int |Rm|^2=12\pi^2,
\]

not \(8\pi^2\). This matters for bubble-counting: the quantum is the orbifold Gauss--Bonnet defect, not a universal \(8\pi^2\) per bubble.

### Rotational S^4 probe

I ran a cheap optimization over smooth rotational metrics

\[
  g=dr^2+f(r)^2g_{S^3},
  \qquad
  f(r)=\frac{L}{\pi}\sin\frac{\pi r}{L}\exp\left(\sum_{k=1}^3 a_k\sin^2\frac{k\pi r}{L}\right).
\]

For this ansatz,

\[
  \operatorname{Ric}_{rr}=-3\frac{f''}{f},
  \qquad
  \operatorname{Ric}_{S^3}=\frac{2(1-(f')^2)-ff''}{f^2}.
\]

The search minimized volume subject to Ricci eigenvalues near \([0.9,1.1]\). It found only the nearly constant-curvature endpoint:

```text
round δ=6.1e-10, Vol=236.870505627
best δ=0.100129, Vol=195.933329354, Vol/round=0.827175
best Ric_rad=[1.098123,1.100129], Ric_tan=[1.099205,1.100049]
```

This is essentially the allowed rescaling toward \(\operatorname{Ric}=1.1g\), whose volume is approximately \(24\pi^2/1.1^2\). It is very far from the proposed low-volume target \(\operatorname{Vol}\le10\). This does not prove a volume lower bound on \(S^4\); it only says the simplest smooth cohomogeneity-one ansatz does not cheaply produce a collapsed positive-pinched metric.

---

## 3. Regularity source check: what bounded Ricci actually gives

### Cheeger--Naber: noncollapsed measure-theoretic control, not uniform smooth compactness

The Step-5 erratum retracted the false claim that two-sided Ricci bounds plus noncollapse give a uniform harmonic-radius lower bound. Peer messages #222--#223 correctly noted that this retraction should be narrower in dimension four. The source `Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md` gives:

- Theorem 1.13, lines 107--110: if \(|\operatorname{Ric}_{M^4}|\le3\) and \(\operatorname{Vol}(B_1(p))>v>0\), then the averaged \(L^2\) curvature is bounded and
  \[
    \operatorname{Vol}\bigl(T_r(\{x\in B_1(p): r_h\le r\})\bigr)\le C(v)r^4.
  \]
- Lines 111--113: replacing harmonic radius by the stronger regularity scale requires the Einstein assumption, or at least a bound on \(|\nabla\operatorname{Ric}|\).
- Lines 284--291: harmonic coordinates under bounded Ricci give \(C^{1,\alpha}\cap W^{2,q}\) control; if \(|\nabla\operatorname{Ric}|\) is bounded one gets stronger \(C^{2,\alpha}\) bounds.

Thus a noncollapsed four-dimensional ball under \(|\operatorname{Ric}|\le3\) contains many definite harmonic patches. On such patches, if additionally \(\operatorname{Ric}_{g_i}-g_i\to0\) uniformly, a subsequential \(C^{1,\alpha}\cap W^{2,q}\) limit satisfies \(\operatorname{Ric}=g\) weakly and is smooth by elliptic bootstrapping. This extracts local Einstein regular-set limits. It does **not** recover the global topology, remove bubbles, or prove that the original smooth \(M_i\) carries an Einstein metric.

### Naber--Zhang: collapsed bounded-Ricci regularity is conditional on local topology

The source `Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md` gives the relevant collapse bridge:

- Theorem 1.1, lines 98--103: under \(|\operatorname{Ric}|\le n-1\), GH closeness to a lower-dimensional Ricci-limit model, and maximal nilpotency rank of the fibered fundamental group, one obtains a conjugate-radius lower bound; if the manifold is Einstein, then \(\sup|Rm|\) is bounded.
- Remark 1.1 / lines 107--109: the curvature bound can also follow from \(|\nabla\operatorname{Ric}|\) control; otherwise the output is harmonic/conjugate-radius control, not full curvature.
- Proposition 6.4, lines 1439--1455: under the maximal-rank hypothesis, lifts to local universal covers have \(C^1\)-harmonic radius bounded below.
- Proposition 6.5, lines 1456--1469: pointwise curvature follows only after adding \(|\nabla\operatorname{Ric}|\le\Lambda\), or in the Einstein case.

This is exactly the missing bridge for Yau26. The positive pinching hypothesis is a pointwise algebraic condition

\[
  \operatorname{Ric}=g+E,
  \qquad \|E\|_{op}\le\delta,
\]

but it is not an elliptic equation with controlled derivatives of the right-hand side. It does not give \(|\nabla\operatorname{Ric}|\), nor an equation for the Weyl tensor strong enough to upgrade harmonic-radius control to pointwise curvature control. This is the same error mode that caused the last repairs: importing Einstein regularity into a merely \(C^0\)-pinched setting.

### Cheeger--Tian primary-source status

A focused `knowledge_request` did not recover the Cheeger--Tian primary paper. A secondary source in Knowledge states that Cheeger--Tian proved an \(\varepsilon\)-regularity theorem for four-dimensional Einstein manifolds without a volume assumption, but this Step did not read the primary theorem. It must remain a source obligation. In any case, every retrieved account presents the theorem as using the Einstein/critical-metric equation, not merely \(C^0\) Ricci pinching.

---

## 4. Positive-branch obstruction-amplitude route: what was checked and what remains

Step 1's Calabi/Morteza--Viaclovsky computation showed that, in real dimension at least six for the Calabi model and negative-Einstein desingularization setting, the approximate Einstein error has the form

\[
  \operatorname{Ric}_{g_t}-\Lambda g_t-t\lambda\chi_t o
  =O_{g_{cal}}(t^2\rho^2),
\]

and since \(g_t\sim tg_{cal}\), the remainder is small in \(g_t\)-operator norm whereas the obstruction term \(t\lambda o\) is order one and non-scalar after raising an index. Lines 456--491 of the MV source record the relevant estimates. The sign of \(\Lambda\) does not change the scaling statement: a nonzero non-scalar obstruction tensor remains an order-one unweighted Ricci-endomorphism defect.

For the positive branch in dimension four, the exact available source statements are different. Ozuch's `Noncollapsed degeneration of Einstein 4-manifolds, I` records:

- Theorem 0.1 (lines 69--82): noncollapsed exact Einstein 4-manifolds with bounded diameter and \(L^2\) curvature converge to Einstein orbifolds; singularities bubble off Ricci-flat ALE spaces.
- Lines 91--94: Biquard's Eguchi--Hanson desingularization has a local obstruction \(\det R=0\) at the singular point; hyperbolic orbifolds fail it.
- Theorem 0.2 (lines 114--124): exact Einstein metrics sufficiently close to an Einstein orbifold come from a gluing-perturbation procedure.

These source statements support an obstruction-amplitude philosophy for exact Einstein degenerations, but they do **not** yet prove the Yau26 claim for approximate \(C^0\)-pinched metrics. The needed checks remain:

1. redo the unweighted-operator-norm scaling for the four-dimensional Eguchi--Hanson/ALE positive-Einstein gluing model, where constants and rotation parameters differ from the Calabi model;
2. determine whether gluing theorems require exact obstruction vanishing or whether sufficiently small obstruction amplitudes already solve after moving parameters;
3. bridge from \(\operatorname{Ric}-g\to0\) in \(L^\infty\) to the weighted gluing norms used by Ozuch/Biquard, which is not automatic without an Einstein-like PDE.

The self-certifying version of Strategy A is still promising but conditional: if a sequence of \(\delta_i\)-pinched metrics actually enters a noncollapsed Einstein-orbifold/ALE gluing regime with a first obstruction term in the Ricci expansion, then \(
\delta_i\to0\) would force that non-scalar obstruction amplitude to vanish. The current gap is proving that merely pinched metrics enter such a gluing regime at all.

---

## 5. Revised positive-branch regimes after Step 6

For \(P_n^+\), exact odd-dimensional lens spaces and Sasaki--Einstein quotients show that collapse is not false; the desired theorem must say compatible collapse topologies already carry Einstein metrics. In dimension four, the Step-6 probes sharpen this into:

1. **Regular noncollapsed patches:** Cheeger--Naber gives harmonic-radius patches under bounded Ricci and noncollapse; pinching gives smooth local Einstein limits on those patches. This is regular-set extraction, not global Einstein existence.
2. **Smooth free circle collapsed regions:** the Kaluza--Klein/Bochner calculation blocks \(\delta_+\to0\) on the constant-fibre-length closed principal-circle model, and the Euler/CGB accounting also blocks a global free action. More general warped free-collapse models remain to be formulated, but regular pieces, if present locally, must be attached to singular/concentration regions carrying topology.
3. **Curvature-concentration/orbifold regions:** in 4D the CGB energy budget and ALE energy quantization control their number/topological cost, but an approximate-pinching analogue of Einstein \(\varepsilon\)-regularity/gluing is missing.
4. **Singular/fixed-stratum collapse:** the real positive-branch collapse enemy. It is compatible with known exact Einstein quotient collapse in odd dimensions and may be the only way four-dimensional collapse carries \(\chi>0\).

A02 should not spend further effort on fixed-connection Berger catalogues or on proving all collapse impossible. The high-value questions are:

- Can one obtain an approximate Einstein \(\varepsilon\)-regularity theorem from \(\|\operatorname{Ric}-g\|_{L^\infty}\le\delta\), perhaps after adding a gauge or Ricci-flow smoothing argument? The essential obstacle is lack of \(\nabla\operatorname{Ric}\) or Weyl PDE control.
- In dimension four, can Chern--Gauss--Bonnet transgression plus Naber--Zhang maximal-rank regularity decompose a tight positive-pinched metric into bounded-curvature collapsed pieces with zero Euler contribution and finitely many singular/concentration caps?
- For noncollapsed orbifold concentration, does the unweighted obstruction-amplitude principle extend to Eguchi--Hanson/ALE positive gluing strongly enough to return an Einstein metric on the same smooth topology?

None of these resolves Yau26 yet, but this Step removes two misleading computations and turns the positive-collapse gap into a more precise singular-stratum/regularity problem.
