# Step 25: Structural resolution of Yau-26's landscape

Session S0910A02. Agent2/Constructor. Phase Execute.

## The entanglement principle

For each dimension \(n\ge2\), write
\[
\mathcal P_n^+(\delta) = \{\text{closed smooth }n\text{-manifolds admitting }g\text{ with }
\|\operatorname{Ric}_g-g\|_{\mathrm{op}}\le\delta\}
\]
and \(\mathcal E_n = \{\text{closed smooth }n\text{-manifolds admitting some Einstein metric}\}\).
Then
\[
P_n^+(\delta)\text{ holds} \quad\Longleftrightarrow\quad
\mathcal P_n^+(\delta)\subseteq\mathcal E_n.
\]
Analogously for \(P_n^-\). The Yau-26 proposition holds for dimension \(n\) if and
only if one of the two inclusions holds for some dimension-only \(\delta>0\).

This formulation separates the two sides of the problem:
- **Left set:** which manifolds admit tight Ricci pinching?
- **Right set:** which manifolds admit Einstein metrics?

## Dimension-by-dimension status

### \(n=2\): Settled.
Every closed surface admits a constant-curvature metric (uniformization), hence
an Einstein metric. \(\mathcal E_2\) is the class of all closed surfaces.
\(P_2^+\) and \(P_2^-\) are both trivially true.

### \(n=3\): Settled.
Hamilton's Ricci flow (positive case) and geometrization (general case) give
Einstein or geometric structures on all closed 3-manifolds.
\(\mathcal E_3\) includes all closed 3-manifolds. \(P_3^+\) holds trivially.

### \(n=4\): Open, reduced to the entanglement.

**Left set \(\mathcal P_4^+(\delta)\) characterization.** For \(\delta<1\), the
established constraints from tight positive pinching are:
- Myers: diameter \(\le\pi/\sqrt{1-\delta}\).
- Bishop: volume \(\le V_{S^4}/\sqrt{(1-\delta)^4}\).
- Bochner: \(b_1=0\), finite \(\pi_1\).
- Chern–Gauss–Bonnet: \(\chi>0\), \(\beta(\delta)\operatorname{Vol}\le8\pi^2\chi\).
- Strict Hitchin–Thorpe: \(2\chi>3|\tau|\) for \(\delta<1/(1+\sqrt3)\).
- Cheeger–Naber: finitely many diffeomorphism types under fixed volume lower bound.
- CZ spike: pointwise curvature is NOT bounded (Step 11).
- Collapse IS possible (lens-space examples; toric α-family is BREAK-compatible).

The left set contains all standard \(S^4\), \(\mathbb{CP}^2\),
\(S^2\times S^2\) and, if the α-family is realizable, also
\(\#_k(S^2\times S^2)\) for all \(k\).

**Right set \(\mathcal E_4\).** Known no-Einstein manifolds:
- \(\#_5\mathbb{CP}^2\) and beyond: strict Hitchin–Thorpe violators.
  But these are already excluded from \(\mathcal P_4^+\) by our
  strict-HT bound for tight positive pinching.
- Ishida–LeBrun family \(X\#k\overline{\mathbb{CP}}^{\,2}\) with
  \(k\ge A/3\): no negative Einstein by SW.

**The gap.** The membership of \(\#_k(S^2\times S^2)\) for large \(k\) in
\(\mathcal E_4\) is unknown. PSC kills SW, so there is no known obstruction
to Einstein existence on this family. The toric verdict says the left-set
membership is BREAK-compatible (tight pinching may allow collapse), but
the right-set membership is an independent open problem.

### \(n\ge5\): Open, entangled with the general Einstein-existence problem.

**Left set \(\mathcal P_n^+(\delta)\).** Poorly characterized. Myers/Bishop/finite
\(\pi_1\) apply. No Chern–Gauss–Bonnet or Hitchin–Thorpe analogue. No
\(L^2\)-curvature-based exclusion. Collapse is explicitly Einstein-compatible:
the KK product family \(L(q,1)\times N^{n-3}\) gives exact positive Einstein
collapse in every \(n\ge5\) (Step 24). The left set could be very large.

**Right set \(\mathcal E_n\).** Wang's survey states: it is unknown whether every
closed smooth manifold of dimension \(\ge5\) admits an Einstein metric. No general
obstruction to Einstein existence is known. Homogeneous nonexistence only
concerns invariant metrics, not the smooth manifold.

**Consequence.** If \(\mathcal E_n\) is the class of all closed \(n\)-manifolds
for \(n\ge5\), then \(P_n^+\) holds vacuously regardless of pinching. A refutation
of \(P_n^+\) requires both (i) a closed \(n\)-manifold admitting no Einstein metric
of any sign, and (ii) a tight positive-pinching construction on that manifold.
Task (i) is itself a recognized open problem at least as hard as parts of
Yau-26. Task (ii) additionally requires controlling two-sided Ricci on the
specific topology, which Lohkamp/Gao–Yau one-sided flexibility does not provide.

## Reusable lemma suite

1. **Eigenvalue equation** (all \(n\), torus-invariant): \(-\Delta_B w = kw\)
   for \(T^k\) collapse with \(\operatorname{Ric}=g\).
2. **Determinant trace** (verified for \(k=1,\ldots,5\)):
   \(\operatorname{tr}_h\operatorname{Ric}^V=-\Delta_Bw/w+\frac12|F|_h^2\).
3. **Corrected individual warping** (\(k=2\), diagonal, twist-free):
   \(-\Delta_Bp=(1-K_B)p\), \(\langle\nabla p,\nabla q\rangle=-K_Bw\).
4. **Flux equi-partition** (\(k=2\), diagonal): \(\Phi_p=\Phi_q=\int w\).
5. **Rod identity**: \(\Phi_i=2+2\int K_{\mathrm{edge}}Q_i\,ds\).
6. **CZ spike**: \(C^0\) Ricci pinching does not bound pointwise curvature.
7. **Circle-collapse obstruction** (\(n=4\) only): Bochner/Step-6 threshold
   \(\delta<1/(1+\sqrt2)\) for constant-fiber free \(S^1\) over 3D base.
8. **KK product collapse** (\(n\ge5\)): \(L(q,1)\times N^d\) gives exact positive
   Einstein collapse in every \(n=d+3\ge5\).
9. **Strict Hitchin–Thorpe** (\(n=4\)): \(\delta<1/(1+\sqrt3)\Rightarrow 2\chi>3|\tau|\).
10. **\(\beta(\delta)\) energy budget** (\(n=4\)):
    \(\beta(\delta)\operatorname{Vol}\le8\pi^2\chi-\int|W|^2\).

## Abelian-forcing observation (all \(n\ge5\), not yet a theorem)

For nonabelian nilpotent collapse with fiber \(N\) of diameter \(\varepsilon\) and
bracket norm \(b\) (in the fiber metric at unit scale), the fiber Ricci in the
bracket direction carries a term \(-cb^2/\varepsilon^2\). Total-space positive
Ricci \(\ge(1-\delta)\) forces \(b^2/\varepsilon^2\le C(1+\delta)\), i.e.
\(b\le C\varepsilon\). In the collapsing limit (\(\varepsilon\to0\)), the bracket
vanishes and the fiber is effectively abelian.

This is a candidate all-dimensional theorem: tight positive Ricci pinching
forces collapse fibers to be abelian (torus), reducing the problem to the
determinant trace/KK equations. It uses only Milnor's nilpotent Ricci formula
and the O'Neill/submersion structure; the missing ingredient is the collapse-
to-fibration regularity bridge under \(C^0\) Ricci only (without bounded
sectional curvature, which the CZ spike forbids).

**The abelian-forcing computation with full second-fundamental-form and twist
terms is the primary mathematical continuation for the session.**
