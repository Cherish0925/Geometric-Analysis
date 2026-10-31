# O11: a genuinely global construction test, and its topological obstruction

2026-09-30. Status: no improvement of the O11 coefficient is obtained in this note. The result below rejects a class of global competitors; it is not another claim of progress toward the sharp lower bound.

## 1. The global mechanism that was actually checked

The original family is

\[
M=X\#k\overline{\mathbb {CP}}^2\#\ell(S^1\times S^3),
\qquad X=\mathbb {CH}^2/\Gamma,
\qquad Q=k+4\ell.
\]

Instead of another local cap, we checked a known global way to defeat natural curvature-minimizing candidates: combine large general-type pieces with their orientation reverses, and use connected-sum/stabilization identities to change the decomposition of the entire smooth manifold. LeBrun's *Curvature in the Balance: The Weyl Functional and Scalar Curvature of 4-Manifolds*, arXiv:2203.02528v2, Theorem A and Section 1, carries out such a construction for large connected sums of projective planes or of \(S^2\times S^2\). This is genuine evidence that local optimality and Kähler optimality need not decide unrestricted curvature minimization.

However, that theorem controls the Weyl functional, not \(P=\int|\operatorname{Ric}^{\circ}|^2\). Its construction also uses positive-intersection summands that the original O11 manifolds cannot have. Thus it supplies neither a metric on the original \(M_j\) nor a scalar-energy budget at precision \(o(Q_j)\).

## 2. All compact simply connected positive-intersection pieces are excluded

**Proposition.** Let \(X\) be a closed oriented aspherical four-manifold and set
\[
M=X\#k\overline{\mathbb {CP}}^2\#\ell(S^1\times S^3).
\]
The intersection pairing on \(H_2(\widetilde M;\mathbb R)\), evaluated on compact cycles in the universal cover, is negative definite. Consequently, an oriented compact smooth four-dimensional domain \(B\subset M\) with simply connected interior cannot have a positive vector in its intersection pairing. In particular, \(M\) has no closed simply connected connected-sum factor \(Y\) with \(b^+(Y)>0\).

**Proof.** Use the connected-sum three-spheres to describe the universal cover as a tree of lifted punctured pieces. A lift of the punctured aspherical piece has vanishing second homology: it is obtained from the contractible universal cover of \(X\) by removing a locally finite family of open four-balls. A lift of a punctured \(S^1\times S^3\) piece also contributes no second homology. Every lifted punctured \(\overline{\mathbb {CP}}^2\) contributes one generator with square \(-1\).

Apply Mayer--Vietoris first to any finite connected subtree. The gluing cross-sections have \(H_1=H_2=0\), so its second homology is the direct sum of the contributions from its vertices. Generators from different vertices are represented by disjoint cycles; their intersections vanish. Every compact cycle and every finite chain witnessing a homology relation lie in such a finite subtree. Taking the direct limit therefore gives
\[
H_2(\widetilde M;\mathbb R)\cong
\bigoplus_{\nu}\mathbb R E_\nu,
\qquad E_\nu\cdot E_\mu=-\delta_{\nu\mu}.
\]
Only finite sums occur in ordinary homology.

A simply connected domain \(B\) lifts diffeomorphically to a domain of \(\widetilde M\). Intersection numbers of compact cycles computed in \(B\) are unchanged in the ambient universal cover. If a vector \(x\in H_2(B;\mathbb R)\) had \(x\cdot x>0\), its image would therefore have positive square in the displayed negative definite form, a contradiction. No injectivity assumption on all of \(H_2(B)\) is needed: positive square itself guarantees that this particular image is nonzero. Apply this to \(Y\setminus B^4\) for the connected-sum assertion. \(\square\)

For the O11 family, \(\pi_1(M)=\Gamma*F_\ell\) is torsion-free. The same lifting argument applies to domains with finite fundamental group, since their fundamental-group image in \(\pi_1(M)\) is trivial.

This proposition is an elementary topological check, not a new curvature theorem. It excludes directly transplanting the separated general-type/orientation-reversed blocks and positive stabilizations from the cited global Weyl construction. It does **not** exclude all nonlocal changes of metric, arbitrary cobordism constructions, or negative-definite merged cores.

## 3. Why an apparent merged ALE saving is not a complete competitor

A tempting alternative is to trade several \(-1\) classes for \(-2\) root configurations plus a residual class, use Ricci-flat ALE metrics on the root configurations, and count only the residual core's Ricci energy. That is incomplete: the pieces have lens-space boundaries and different end markings, so neither their boundary transgressions nor their transition regions can be omitted.

In fact, any completed scalar-flat asymptotically Euclidean filling with the original ordinary outer end and surgery topology already satisfies the relative Chern--Weil identity
\[
P=8\pi^2Q+4\int|W^+|^2\ge8\pi^2Q.
\]
With nonzero scalar curvature the additional term is \(\int s^2/12\). These are the Euclidean-background versions of the integrated manuscript's Section `Relative cell costs and non-Kähler variations`, not new results of this note. They apply to the **completed filling**, including all merged cores and transitions. Thus merely rearranging charges among ALE pieces cannot evade the standard threshold while retaining an ordinary Euclidean outer end.

A subthreshold construction must change the geometry on a nonvanishing background-volume scale, or avoid this entire completed-filling regime. The manuscript already quantifies this necessity in its coupled-filling section; it should not be reported as a new discovery here.

## 4. Exact consequence for the research decision

No complete competitor with
\[
P<8\pi^2Q-\delta Q
\]
was produced. No global lower bound was proved. The cited global Weyl theorem is not an unused theorem that solves O11 after substitution.

These checks explain why two superficially promising global constructions fail to become admissible competitors. They should remain a short record, and should not consume another round of cap optimization or be elevated to a main result. The unresolved unrestricted metric tradeoff remains
\[
\frac{\int s^2-32\pi^2A}{12}+4\int|W^-|^2
\ge48\pi^2k-o(Q),
\]
or a genuine counterexample to it with the same smooth topology and all costs included.

## Sources actually consulted

- C. LeBrun, *Curvature in the Balance: The Weyl Functional and Scalar Curvature of 4-Manifolds*, arXiv:2203.02528v2, Theorem A and Section 1. https://arxiv.org/pdf/2203.02528 . Only the stated scope and construction mechanism are used; the topological proposition above is proved here.
- Unchanged integrated manuscript, lines 7790--8525: complete relative cells, replication, conformally Kähler exclusion, and coupled-filling volume requirements.
- `Line1_Continuation_20260929D/O11_Competitors.md`: exact invariance of \(A,Q\) under alternative minimal-general-type bulk decompositions.
- `Line1_Continuation_20260929C/O11_Geometry_Competitor.md`: exceptional scalar--Weyl compensation and the limitations of projection-only budgets.
