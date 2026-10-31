# Step 57: Kähler exclusion, van Kampen, and the four-dimensional noncollapsed dichotomy

Session S0910A02. Agent2 / Constructor. Phase Explore.

## 0. Target fidelity

The active target remains Yau's Problem 26: dimension-only constants
\(c_n<C_n\) such that every closed connected smooth \(n\)-manifold with
\(c_ng\le\operatorname{Ric}_g\le C_ng\) admits some (unrelated) Einstein metric.
This note concerns only the four-dimensional noncollapsed bubbling arc in both
signs.  It does not address positive collapse, negative collapse/diameter escape,
non-\(SU(2)\) ALE bubbles, dimensions \(n\ge5\), or Lean formalization.

## 1. Kähler exclusion for mixed rows

### Statement

**For \(1\le r\le35\), the manifold \(M_r\) from the genus-2 family
\((\Sigma_2\times\Sigma_2)/\langle\iota\times\iota\rangle\) admits no
Kähler (or symplectic) structure in either orientation.**

### Proof

Recall the row arithmetic from Steps 55--56: \(M_r\) has \(\chi=56\),
\(\tau=-36+2r\), \(b_+=9+r\), \(b_-=45-r\).

*Original orientation.*  If \(r\ge1\), then \(M_r\) contains \(r\ge1\) non-torsion
embedded spheres of self-intersection \(+2\) (from reversed Eguchi--Hanson
fillings) and \(b_+(M_r)=9+r>1\).  Suppose \(M_r\) carried a Kähler structure.
By Taubes' theorem for symplectic manifolds with \(b_+>1\), there exist
spin\(^c\)-structures \(\mathfrak s\) with \(\mathrm{SW}(M_r,\mathfrak s)\ne0\).
The adjunction inequality for a sphere class (Baraglia/Kronheimer, source lines
30--38: adding a handle gives a genus-1 representative) yields
\[
  |\langle c(\mathfrak s),[S]\rangle|+[S]^2\le0
\]
for any non-torsion class represented by a sphere, whenever
\(\mathrm{SW}(X,\mathfrak s)\ne0\), \(b_+>1\), and simple type.  But
\([S]^2=+2>0\), a contradiction.  Therefore \(M_r\) carries no Kähler/symplectic
structure in its original orientation.

*Reversed orientation.*  For \(r\le35\), the reversed orientation has
\(36-r\ge1\) spheres of self-intersection \(+2\) (the compatible nodes become
reversed under orientation reversal) and \(b_+=45-r>1\).  The same argument
excludes Kähler/symplectic structure in the reversed orientation.

*Endpoint control.*  At \(r=0\), there are no \(+2\)-spheres in the original
orientation, and \(M_0\) is the smooth double cover of \(\mathbb P^1\times\mathbb P^1\)
branched over a smooth \((6,6)\) curve: a minimal surface of general type with
\(K^2=4\) and ample \(K\).  Aubin--Yau gives a negative Kähler--Einstein metric.
At \(r=36\), orientation reversal identifies \(\bar M_{36}\cong M_0\), so it
carries the same unoriented Einstein metric.

### Consequence

This strictly strengthens the Noether parity exclusion from Step 56 (which
reached only odd \(r\)).  More importantly, it removes the even-row question
entirely: no even mixed row can be an ample-canonical surface, so Aubin--Yau
cannot shrink the wall.  All Einstein existence machines in dimension four
require Kähler/algebraic structure for \(b_+>1\), so no mixed row
\(r=1,\ldots,35\) can be settled by any known existence theorem.

## 2. Van Kampen proof: all sign-pattern fillings are simply connected

### Statement

**For every \(0\le r\le36\), the manifold \(M_r\) is simply connected.**

### Proof

*Step 1.* \(M_0\) is simply connected.  It is the smooth double cover
\(\pi:M_0\to\mathbb P^1\times\mathbb P^1\) branched over a smooth connected
curve \(D\in|\mathcal O(6,6)|\).  Since \(\mathbb P^1\times\mathbb P^1\) is
simply connected and \(D\) is connected (ample, hence by Bertini), the Catanese
cyclic-cover proposition (source: `On-Einstein-Metrics-on-4-Manifolds-with-
Finite-Cyclic`, lines 210--219) gives \(\pi_1(M_0)=1\).

*Step 2.* Both filling bundles are simply connected.  The \(-2\) disk bundle over
\(S^2\) (total space of the tautological subbundle of the Hopf bundle squared) is
diffeomorphic to \(T^*S^2\) and deformation retracts to \(S^2\).  The \(+2\) disk
bundle is similarly simply connected.  Both have boundary
\(\partial D_\pm\cong\mathrm{RP}^3\) (the unit circle bundle of \(\mathcal O(\pm2)\)
over \(S^2\)).

*Step 3.* The inclusion \(\mathrm{RP}^3\to D_\pm\) induces the zero map on
\(\pi_1\), since \(\pi_1(D_\pm)=\pi_1(S^2)=0\) while
\(\pi_1(\mathrm{RP}^3)=\mathbb Z/2\).

*Step 4.* Let \(W=M_0\setminus\bigsqcup_{k=1}^{36}N_k\), where \(N_k\) are
open tubular neighborhoods of the 36 exceptional \((-2)\)-spheres.  Then
\(\partial W\) consists of 36 copies of \(\mathrm{RP}^3\).  By van Kampen,
\[
  \pi_1(M_0)=\pi_1(W)/\langle\mathrm{images\ of\ }\pi_1(\mathrm{RP}^3_k)
  \rangle_\mathrm{normal}=1.
\]
For any sign-pattern filling \(M_r\), we replace each \(N_k\) by \(D_+\) or \(D_-\)
along the same \(\mathrm{RP}^3\) boundary.  Since both \(D_\pm\) are simply
connected and the inclusion \(\mathrm{RP}^3\to D_\pm\) kills \(\pi_1\),
\[
  \pi_1(M_r)=\pi_1(W)/\langle\mathrm{same\ images}\rangle_\mathrm{normal}
  =\pi_1(M_0)=1.\qquad\square
\]

### Consequence

All mixed rows have trivial fundamental group, hence zero simplicial volume
(Gromov--Thurston: amenable \(\pi_1\Rightarrow\|M\|=0\), source: Simplicial-volume
Manifold-Atlas, lines 338--355).  Therefore:
- Sambusetti/BCG Gromov-norm obstructions are vacuous for this family.
- Kotschick's Gromov--Hitchin--Thorpe/entropy-volume inequalities produce no
  constraint (they require \(\|M\|>0\)).
- These obstructions could only reopen for a different construction with
  rationally essential or nonamenable \(\pi_1\).

## 3. Higher-genus family: strict HT everywhere

For genus \(h\ge2\), the family \((\Sigma_h\times\Sigma_h)/\langle\iota\times\iota\rangle\)
has \(N=4(h+1)^2\) nodes and:
\[
  \chi=8(h^2+h+1),\qquad \tau=-4(h+1)^2+2r,\qquad
  b_+=2h^2+1+r,\qquad b_-=6h^2+8h+5-r.
\]
The Hitchin--Thorpe margin is
\[
  2\chi-3|\tau|=4(h-1)^2+6\min(r,N-r).
\]
For \(h\ge2\), this is at least \(4(h-1)^2\ge4>0\) for every \(r\).  The Kähler
exclusion and van Kampen arguments generalize directly (the hyperelliptic
involution on \(\Sigma_h\) has \(2(h+1)\) fixed points and acts as \(-1\) on
\(H^1\)).  Therefore no enlargement of the genus produces a topological
contradiction to Hitchin--Thorpe, and the entire two-parameter family
\((h,r)\) sits strictly inside HT.

Data: `workspace/data/step57_dichotomy_and_kahler_exclusion.json`, field
`higher_genus_generalization`.

## 4. Bauer--Furuta scope

The question is inverted: not "does a \(+2\)-sphere kill all generic monopole
classes?", but "does any known mechanism produce such a class on a mixed row?"

All known four-dimensional monopole nonvanishing inputs for Einstein obstruction
run through Kähler/symplectic summands:
- Taubes' theorem gives \(\mathrm{SW}\ne0\) for symplectic manifolds with \(b_+>1\).
- Kotschick's Theorem 10 (connected-sum nonvanishing, source lines 105--118)
  produces monopole classes on \(X\#Y\) from basic classes on symplectic summands.
- Ishida--LeBrun Corollary 13 (source lines 152--158) needs simply connected
  symplectic summands with \(b_+\equiv3\pmod4\).
- Bauer--Furuta stable-cohomotopy nonvanishing also typically uses Kähler building
  blocks.

For mixed rows:
- \(M_r\) is not Kähler/symplectic in either orientation (§1 above).
- \(M_r\) does not decompose along the \(+2\)-sphere: the neighborhood \(D_+\) has
  boundary \(\mathrm{RP}^3\), not \(S^3\) or a homology sphere, so the sphere does
  not represent a connected-sum splitting.
- No other mechanism is known to produce nonzero generic monopole classes on
  these manifolds.

**Conclusion.** Currently no known mechanism provides a nonzero monopole or
Bauer--Furuta class on any mixed row.  This is a status statement, not a
vanishing theorem.  A genuinely new source of stable-cohomotopy classes on
non-Kähler simply connected manifolds with \(+2\)-spheres would change the
assessment and could convert the wall into an actual \(P_4^\pm\) refutation.

## 5. Multi-bubble estimate: conditional status

The construction half of the reduction theorem uses:
\[
  \|\operatorname{Ric}_{g_t}-\Lambda g_t\|_{\mathrm{op},g_t}\le Ct^{1/2}\to0
\]
on each realized sign-pattern filling \(M_r\), after killing all vector first
obstructions.  This estimate is sourced from:
- Ozuch, `Higher-order-obstructions`, lines 715--789: defines the approximate
  metric \(g^A_{\zeta,v}\), gives local weighted controls, and bounds the
  projected defect by \(C|\zeta|^{3/2-\beta/4}\) (Proposition 2.19).
- Ozuch cites **[Biq13] O. Biquard, Désingularisation de métriques d'Einstein. I,
  Invent. Math. 192 (2013), no. 1, 197–252**, Section 14, for the EH-region
  estimate (line 783).

**This session has not retrieved the Biquard paper despite two attempts.**  The
estimate is imported through Ozuch's reference.  For 36 simultaneous bubbles at comparable
scale on a compact orbifold:
1. Transition annuli are mutually disjoint when all scales \(t_j\) are comparable
   and small relative to inter-node distance (fixed on the orbifold).
2. Reversed EH is isometric to standard EH (orientation-reversed) and the local
   estimate transfers.
3. Non-interaction of first obstructions at different nodes holds because each
   \(\lambda_k^j\) is a local boundary flux (Ozuch lines 650--654).

The reduction should be stated as conditional on (a) Biquard's estimate as cited
and (b) disjoint non-interaction of finitely many simultaneous EH insertions.
Alternatively, the Biquard source should be retrieved for independent verification.

## 6. The unified dichotomy

### Statement

In dimension four, tight noncollapsed operator-norm Ricci pinching through
codimension-four ALE bubble insertion drives the construction into the unique
region where all four-dimensional Einstein existence and nonexistence tools for
simply connected \(b_+>1\) manifolds are simultaneously void.  The mechanism is:

1. **Compatible bubbling is holomorphic.**  It preserves \(K^2\) and lands on
   manifolds where algebraic geometry (Aubin--Yau, del Pezzo, Tian) already
   supplies an Einstein metric.
2. **Reversed bubbling inserts a \(+2\)-sphere.**  This annihilates all ordinary
   SW basic classes (adjunction with handle, \(b_+>1\)) and therefore kills every
   Kähler/symplectic structure in both orientations.  It simultaneously removes
   all known Einstein nonexistence inputs (LeBrun/Ishida--LeBrun/Kotschick
   require nonzero monopole classes) and all known Einstein existence inputs
   (Aubin--Yau/Kähler--Einstein/Tian require Kähler structure).
3. **The endpoint correlation is structural.**  The two rows retaining SW classes
   in one orientation (\(r=0\) and \(r=N\)) are exactly the two rows known to be
   Einstein: the all-compatible row carries a Kähler--Einstein metric, and the
   all-reversed row is its orientation reverse.

### Mirror walls

The Kähler exclusion applies verbatim to both mirrors:

**Positive mirror** \((S^2\times S^2)/\mathbb Z_2\), 4 nodes.  For \(r=1,2,3\):
\(b_+=1+r\ge2>1\) in the original orientation, and
\(b_+=5-r\ge2>1\) in the reverse orientation with \(4-r\ge1\) reversed nodes.
So all positive mixed rows are non-Kähler in both orientations by the same
adjunction argument.

**Negative mirror** \((\Sigma_2\times\Sigma_2)/\langle\iota\times\iota\rangle\),
36 nodes.  For \(1\le r\le35\): proved in §1.

| Sign | Orbifold | Nodes | Curvature blocks | Live rows |
|------|----------|-------|------------------|-----------|
| \(+\) | \((S^2\times S^2)/\mathbb Z_2\) | 4 | \(R_+=R_-=\operatorname{diag}(\Lambda,0,0)\) | \(r=1,2,3\) |
| \(-\) | \((\Sigma_2\times\Sigma_2)/\langle\iota\times\iota\rangle\) | 36 | \(R_+=R_-=\operatorname{diag}(-1,0,0)\) | \(r=1,\ldots,18\) (up to orientation) |

Both families have:
- All live rows simply connected
- Strict Hitchin--Thorpe
- No Kähler/symplectic structure in either orientation
- No known monopole/SW/Gromov-norm obstruction
- Explicit near-Einstein metrics with \(\|\operatorname{Ric}-\Lambda g\|_{\mathrm{op}}\to0\)
  (conditional on Ozuch/Biquard cited estimate)

### Content

**Yau Problem 26 in dimension four (noncollapsed) is at least as hard as
producing Einstein metrics on simply connected closed four-manifolds with
\(b_+\ge2\) and no monopole classes.**

This is a real result about the difficulty of the problem, not progress toward
its resolution.  Two mirror walls show that the proposition's truth or falsehood
in dimension four passes through an open question in Einstein geometry that
current gauge-theoretic and Kähler--geometric tools cannot reach.

### What this does not touch

- Positive collapse (\(n=4\))
- Negative collapse and diameter escape (\(n=4\))
- Non-\(SU(2)\) ALE bubbles (non-Kähler Ricci-flat ALE beyond EH)
- All dimensions \(n\ge5\) (codimension-four stratification, ALE bundles)
- The H4-dual normalized-flux necessity bridge (from arbitrary pinched
  degeneration to \(R_\pm\zeta=0\))
- The Lean formalization obligation

## 7. Files and sources

- Script: `workspace/scripts/step57_dichotomy_and_kahler_exclusion.py`
- Data: `workspace/data/step57_dichotomy_and_kahler_exclusion.json`
- Adjunction source: `Knowledge/objects/papers/Constraints-on-embedded-spheres-and-real-projective-planes-in-4-manifold--8ed554585965--84b24ecda19e/object.md`, lines 30--38
- Kotschick monopole: `Knowledge/objects/papers/Monopole-classes-and-Einstein-metrics--7e930960f4ba--238b99595d67/object.md`, lines 80--168
- LeBrun Seiberg--Witten: `Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md`, lines 279--353, 480--511
- Cyclic-cover π₁: `Knowledge/objects/papers/On-Einstein-Metrics-on-4-Manifolds-with-Finite-Cyclic--70cb8f6b826f--572747b3a569/object.md`, lines 210--219
- Ozuch obstruction: `Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md`, lines 650--789
- Simplicial volume: `Knowledge/objects/web/Simplicial-volume-Manifold-Atlas--f6b45b4cd81c--1a88f1506496/object.md`, lines 338--355
- Step 49 operator-norm note: `workspace/notes/step49_positive_branch_wall_and_operator_norm.md`
- Step 50 reversed estimate: `workspace/notes/step50_reversed_bubble_estimate_and_hardness_reduction.md`
- Step 55 negative wall: `workspace/data/step55_negative_bikahler_mixed_wall.json`
- Step 56 audit: `workspace/data/step56_negative_bikahler_audit.json`

No branch of the full Yau--26 proposition is proved or refuted.
