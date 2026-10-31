# TTCS Independent Branch Record

```json
{
  "step_id": 3,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step3_coupled_compensation_and_route_reassessment.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md"
  ]
}
```

## Task

Check the proposed fixed-exterior orbifold rigidity lemma in Section 7 of the note. Exact setting: X=CH^2/Γ is a closed smooth complex-hyperbolic surface; D is an embedded metric ball with Vol(D)<Vol(X)/2; U=X\D° isometrically embeds as the unchanged open exterior of a compact connected locally CH orbifold base O arising from a stationary fixed-collar degeneration. The argument says O=CH^2/Γ', equality of the exterior germ yields Γ<Γ', volumes give Vol(O)=Vol(X)/[Γ':Γ], while Vol(O)>=Vol(U)>Vol(X)/2, so the index is one and O=X smoothly. Verify each topological, holonomy, developability, completeness, volume, and unique-continuation step; identify and repair any hidden issue, especially whether an isometric embedding of U really gives the lattice inclusion and whether orbifold points or nontrivial developing maps can evade it. Then state the strongest rigorously supportable lemma and what it actually removes from the bubble-tree problem.

## Output

# Verification memo: fixed-exterior orbifold rigidity (Step 3, §7)

## 1. Summary

The argument in §7 is correct under its stated hypotheses. Every topological and volume step holds. The lattice inclusion is genuine, and orbifold points cannot evade it.

Three points need to be made explicit:

- the embedded exterior must lie in the regular part of the orbifold;
- the stationarity of the base has a different source from the one implied by "stationary fixed-collar degeneration";
- connectedness is needed only for the component of the regular set that contains the collar.

Two improvements follow:

- **The hypothesis \(\operatorname{Vol}(D)<\operatorname{Vol}(X)/2\) is unnecessary.** A short sheet argument in \(\mathbb{CH}^2\) gives \(\Gamma'=\Gamma\) for any embedded ball, or any finite family of disjoint embedded balls. It also shows that the identification \(\mathcal O\cong X\) extends the given embedding of \(U\), so the base region is isometric to \(D\) itself.
- **The global identity I54 (1.2) then gives the cell inequality directly for every such degeneration, by Fatou.** No whole-tree charge theorem is needed for the inequality. The tree analysis is needed only for the equality and near-equality structure.

So the rigidity lemma removes more of the bubble-tree problem than §7 states.

## 2. Step-by-step check of the argument as written

**(a) \(\pi_1(U)=\Gamma\).**
\(U=X\setminus D^\circ\) with \(D\) a closed embedded 4-ball. Van Kampen applied to \(X=U\cup D\) along a collar of \(S^3\), with \(\pi_1(S^3)=\pi_1(D)=1\), gives \(\pi_1(U)\to\pi_1(X)\) an isomorphism. Correct. The same holds for any finite disjoint union of embedded balls.

**(b) Locally CH on the regular base.**
- The conformal Euler–Lagrange equation is \(\Delta_+s+s+4=0\). With \(f=s+4\) it becomes the linear equation \(\Delta_+f+f=0\).
- \(f=0\) on the open collar, so Aronszajn unique continuation gives \(f\equiv0\) on the connected component \(Y\) of the regular set containing the collar.
- Then I54 (8.2) reads \(\Delta_-E=-2\operatorname{Rm}(E)+\tfrac12|E|^2g\). For the fixed smooth limit metric this is a linear system \(\Delta E=A(x)E\) with bounded coefficients and scalar principal part. Its coefficient \(\tfrac12\langle E,\cdot\rangle g\) uses \(E\) itself as a bounded function. Unique continuation gives \(E\equiv0\) on \(Y\).
- Einstein metrics are analytic in harmonic coordinates (DeTurck–Kazdan). Hence \(\nabla\operatorname{Rm}\), which vanishes on the collar, vanishes on \(Y\), and the CH curvature type persists.
- On an orbifold chart \(\tilde V\to\tilde V/\Gamma_x\), the lifted metric is smooth and the preimage of the regular set is dense. So \(E=0\) and \(\nabla\operatorname{Rm}=0\) extend to the chart.

All correct. The only thing needed is that "regular base" means the component \(Y\) containing the collar (see §4b).

**(c) Local groups lie in \(\operatorname{Isom}(\mathbb{CH}^2)\).**
\(\mathbb{CH}^2\) is a complete, simply connected, real-analytic symmetric space. A local isometry between connected open subsets extends uniquely to a global isometry. So the locally CH Riemannian orbifold is an \((\operatorname{Isom}\mathbb{CH}^2,\mathbb{CH}^2)\)-orbifold.

The local groups and \(\Gamma'\) may contain orientation-preserving antiholomorphic isometries. Complex conjugation on \(\mathbb C^2\) has real determinant \(+1\). Nothing in the argument uses holomorphy of \(\Gamma'\).

**(d) Completeness and developability.**
A compact Riemannian orbifold is complete. The developing-map theorem for complete \((G,X)\)-orbifolds with \(X\) simply connected (Thurston's notes, Ch. 13) makes \(\mathcal O\) good, with \(\mathcal O=\mathbb{CH}^2/\Gamma'\) and \(\Gamma'\) discrete, cocompact and acting effectively. Correct.

**(e) Lattice inclusion.**
This is correct, but it needs \(\iota(U)\subset\mathcal O_{\rm reg}\). An isometric embedding of the smooth manifold \(U\) as the unchanged exterior has trivial local groups at its image points, so the condition holds. It is satisfied by construction, since the collar is fixed. A concrete version of the inclusion, avoiding abstract holonomy:

- Let \(\pi:\mathbb{CH}^2\to X\) and \(q:\mathbb{CH}^2\to\mathcal O\) be the quotient maps, and \(\tilde U=\pi^{-1}(U)\).
- \(\tilde U\) is \(\mathbb{CH}^2\) minus a \(\Gamma\)-orbit of disjoint closed balls. It is connected and simply connected.
- Since \(\iota(U)\subset\mathcal O_{\rm reg}\), \(q\) restricts to an honest covering over \(\iota(U)\). Hence \(\iota\circ\pi|_{\tilde U}\) lifts to a local isometry \(f:\tilde U\to\mathbb{CH}^2\), and \(f=h|_{\tilde U}\) for a unique \(h\in\operatorname{Isom}(\mathbb{CH}^2)\).
- For \(\gamma\in\Gamma\), \(f\circ\gamma\) is another lift. So \(f\circ\gamma=\gamma'\circ f\) for some \(\gamma'\in\Gamma'\), hence \(h\gamma h^{-1}=\gamma'\).

Thus \(h\Gamma h^{-1}\subset\Gamma'\). After replacing \(\Gamma'\) by \(h^{-1}\Gamma'h\):
\[
\Gamma\subset\Gamma',\qquad q|_{\tilde U}=\iota\circ\pi|_{\tilde U}.
\tag{2.1}
\]
The developing map of \(U\) is injective on \(\tilde U\) and is unique up to a global isometry. So a "nontrivial developing map" cannot produce a different inclusion.

**(f) Volume step.**
- \([\Gamma':\Gamma]<\infty\): \(X\to\mathcal O\) is an orbifold covering of a compact orbifold by a compact manifold.
- \(\operatorname{Vol}(\mathcal O)=V/[\Gamma':\Gamma]\).
- \(\operatorname{Vol}(\mathcal O)\ge\operatorname{Vol}(U)=V-d\), using injectivity of \(\iota\).
- With \(d<V/2\) the index is \(1\).

All correct.

**(g) Smoothness of \(\mathcal O\).**
\(\Gamma'=\Gamma\) is torsion-free. Correct.

## 3. Repaired argument without the volume hypothesis

**Proposition.** Let \(D\subset X\) be a finite disjoint union of closed embedded 4-balls (or, more generally, a compact set each of whose components lies in an embedded ball, with \(X\setminus D^\circ\) connected). In the setting of (2.1), \(\Gamma'=\Gamma\).

**Proof.**

1. *Translates of \(\tilde U\) by \(\Gamma'\setminus\Gamma\) miss \(\tilde U\).* Take \(g\in\Gamma'\setminus\Gamma\) and suppose \(x,gx\in\tilde U\). Then \(\iota(\pi x)=q(x)=q(gx)=\iota(\pi gx)\). Injectivity of \(\iota\) gives \(gx=\gamma x\) with \(\gamma\in\Gamma\). Now \(x\in q^{-1}(\mathcal O_{\rm reg})\) has trivial stabilizer in \(\Gamma'\), so \(g=\gamma\), a contradiction. Hence \(g\tilde U\cap\tilde U=\emptyset\).

2. *Such a translate lies in one lifted ball.* We get \(g\tilde U\subset\mathbb{CH}^2\setminus\tilde U=\pi^{-1}(D^\circ)\). Each ball is simply connected, so \(\pi^{-1}(D^\circ)\) is a disjoint union of bounded open sets, each mapped isometrically onto a ball component of \(D^\circ\). The connected set \(g\tilde U\) therefore lies in one bounded component.

3. *Contradiction.* \(\tilde U\) is \(\Gamma\)-invariant and \(\Gamma\) is infinite and discrete, so \(\tilde U\) is unbounded. Its isometric image \(g\tilde U\) is unbounded too, contradicting step 2.

So \(\Gamma'=\Gamma\), \(\mathcal O=X\), and by (2.1) the isometry \(X\to\mathcal O\) restricts to \(\iota\) on \(U\). ∎

Consequences:

- The base region is \(\mathcal O\setminus\iota(U)\cong D^\circ\) isometrically, not merely "some region of the right volume".
- Finite index, covolume comparison and \(d<V/2\) are all superfluous.
- The multi-ball version covers degenerations in which bubble points form inside several inserted cells simultaneously. This is exactly the situation of the \(n_j\)-cell family in I54 §2, where \(\sum d_i\) is not small relative to \(V\) on each cover.

An equivalent route uses orbifold van Kampen. Write \(\mathcal O=U\cup B\) along a regular \(S^3\). Then \(\pi_1^{\rm orb}(\mathcal O)=\Gamma*\pi_1^{\rm orb}(B)\). In a free product with \(\pi_1^{\rm orb}(B)\ne1\) the factor \(\Gamma\) has infinite index, contradicting finiteness of \([\Gamma':\Gamma]\). The sheet argument above is more elementary.

## 4. Hidden issues in the hypotheses

**(a) Where stationarity comes from.**
By I54 Proposition 2, no smooth fixed-collar cell with \(q>0\) is critical. So the degenerating sequence cannot be a sequence of critical cells, and Tian–Viaclovsky-type compactness for critical metrics does not apply to it directly.

The natural source is a minimizing sequence \(G_i\) for \(\inf J\) on \(C\) that converges in \(C^2_{\rm loc}\) away from a finite set \(S\), via diffeomorphisms fixing the collar. The base is then stationary by a transplant argument:

- Suppose a compactly supported variation \(h\) in the regular part lowers the limit energy by \(\delta>0\).
- Push \(h\) forward to \(G_i\). On its compact support, \(C^2\) convergence makes the change in \(J(G_i)\) converge to the change for the limit, since \(J\) involves only second derivatives.
- So \(J(G_i+h_i)<J(G_i)-\delta/2\) for large \(i\), contradicting minimality.

The analytic input is therefore \(C^2_{\rm loc}\) (or \(C^{2,\alpha}_{\rm loc}\)) convergence off a finite set, together with an orbifold structure at the completion points. For this fourth-order-type functional on arbitrary minimizing sequences, no ε-regularity theorem is supplied in the material. That is the genuinely open analytic input.

**(b) Connectedness.**
Limits of quadratic-curvature problems can have multi-fold points: several orbifold sheets meeting at one point, as in the Tian–Viaclovsky theory for critical metrics. If such points occur, \(\mathcal O\) need not have connected regular set. The argument only needs \(\mathcal O_0\), the completion of the component \(Y\) containing the collar, with multi-fold points separated into individual orbifold points.

Other components are closed stationary pieces. Testing \(\Delta_+s+s+4=0\) against \(s+4\) gives \(s\equiv-4\) there, but not \(E=0\). They play no role in the rigidity statement, and in §5 they only add to the left side of the inequality.

**(c) Orbifold structure at \(S\).**
Unique continuation alone gives a locally CH manifold \(Y\) whose metric completion adds finitely many points. That these points are orbifold points with finite groups \(\Gamma_p\) has to come from the compactness theory. It is a hypothesis, not a consequence of the local CH structure.

## 5. Strongest supportable statements

**Lemma A (fixed-exterior rigidity).**

*Hypotheses:*
- \(X=\mathbb{CH}^2/\Gamma\) is closed and smooth.
- \(D\subset X\) is a finite disjoint union of closed embedded balls, and \(U=X\setminus D^\circ\).
- \(\mathcal O_0\) is a compact connected Riemannian orbifold whose regular part contains an isometric copy \(\iota(U)\).
- The regular part of \(\mathcal O_0\) is connected and satisfies the conformal and tensor Euler–Lagrange equations of \(J\).

*Conclusion:* \(\mathcal O_0\) is isometric to \(X\) by an isometry extending \(\iota\). In particular \(\mathcal O_0\) has no orbifold points, and \(\mathcal O_0\setminus\iota(U)\cong D^\circ\).

No volume hypothesis is needed.

**Corollary B (degenerations of this type pay the full charge).**

*Hypotheses:*
- \(G_i\) are smooth metrics on \(C=D\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\), equal to the CH germ on the collar.
- There are diffeomorphisms \(\Phi_i\), equal to the identity on the collar, and a finite set \(S\subset\mathcal O_0\setminus\iota(U)\).
- \(\Phi_i^*G_i\to g_\infty\) in \(C^2_{\rm loc}(Y)\), where \(Y\) is the regular component containing the collar, and \(\mathcal O_0\) is as in Lemma A.

*Conclusion:*
\[
\liminf_i J(G_i)\ge 8\pi^2q,\qquad q=k+4\ell .
\]

*Proof.* By Lemma A, \(Y=D^\circ\setminus S\) with the CH metric. Apply the exact identity I54 (1.2):
\[
J-8\pi^2q=\int_C\Big(\tfrac{(s+3)^2}{3}+1+4|W^+|^2\Big)-4d .
\]
- The density is pointwise at least \(1\).
- On the CH ball it equals \(\tfrac13+1+4\cdot\tfrac23=4\).
- For a compact \(K\subset D\setminus S\) containing the collar, \(C^2\) convergence gives \(\int_{\Phi_i(K)}\text{density}\to4\operatorname{Vol}(K)\).
- Dropping the rest of \(C\), where the density is at least \(1\), gives \(\liminf(J_i-8\pi^2q)\ge4\operatorname{Vol}(K)-4d\).
- Letting \(\operatorname{Vol}(K)\uparrow d\) proves the bound. ∎

**Equality structure.** Equality \(J_i\to8\pi^2q\) forces three things:
- \(\operatorname{Vol}\big(C\setminus\Phi_i(K)\big)\to0\);
- \(\int_{C\setminus\Phi_i(K)}(s+3)^2\to0\);
- \(\int_{C\setminus\Phi_i(K)}|W^+|^2\to0\).

Since \(s^2\le2(s+3)^2+18\), the scale-invariant energy \(\int(s^2/3+4|W^+|^2)\) concentrating at \(S\) must vanish at every scale. So every bubble level, and every neck, is asymptotically scalar-flat with \(W^+=0\) in the CH orientation. This matches the Burns/LeBrun shrinking mechanism that realizes \(8\pi^2\) per blowup (I54 §2).

The topology \(q\) enters only through the relative Chern–Weil/signature identity on the whole cell, which is exact for each \(G_i\). The distribution of marked classes across trees, the quotient-ended levels and the η-terms all disappear from the inequality.

## 6. What this removes from the bubble-tree problem, and what remains

**Removed:**
- **Orbifold bases.** Residual locally CH orbifold geometries are excluded entirely; the base is exactly the CH ball.
- **The volume hypothesis.** Lemma A holds for the multi-cell configurations of I54 §2.
- **The whole-tree charge theorem, for the lower bound.** §5 and §7 of the note list four requirements: the Euler–Lagrange equation with base classification, APS bookkeeping, preservation of marked classes, and a whole-tree \(8\pi^2q\) theorem. Under the hypotheses of Corollary B, the last three are not needed for \(\liminf J\ge8\pi^2q\). The zero-Ricci-cost quotient-ended ALE pieces, the \(1/|\Gamma|\) charges and the η-invariants of §5 cannot lower the energy below the threshold in this regime. They matter only for classifying near-extremal sequences.

**Remains.** Any subthreshold sequence (\(\limsup J_i<8\pi^2q\)) must violate the hypotheses of Corollary B. The possible ways are:

1. **Concentration on a larger set or collapse.** Loss of \(C^2_{\rm loc}\) convergence on more than a finite set, for example codimension-1 or codimension-2 concentration, or collapse of part of the cell. No compactness theorem supplied here prevents this. The required analytic input is an ε-regularity and finite-concentration statement for minimizing (or Palais–Smale) sequences of \(J\) with a fixed collar.
2. **Non-orbifold completion points** of the regular component containing the collar.
3. **A non-stationary limit**, which by §4a is impossible for minimizing sequences with \(C^2_{\rm loc}\) convergence. Equivalently, a non-CH smooth base: this is exactly the nondegenerate filling problem, i.e. C1 / (2) / (3) of the note.

So the content of Lemma A plus Corollary B is that energy concentration at finitely many points with a stationary base never helps. The remaining cell question is the nondegenerate coercivity problem (equations (2)–(3) of the note) together with the compactness theory for minimizing sequences. The "whole-tree theorem" sentence ending §7 of the note can be replaced by Corollary B.