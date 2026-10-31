# Step 51: Preceptor audit of the positive wall and the negative Yang--IL interface

Session S0910A02. Agent4 / Preceptor. Phase Explore.

## 0. Target fidelity

The active target remains the full Yau--26 proposition for all closed connected smooth manifolds in every dimension.  Nothing in Steps 49--50 proves or refutes it.  The reliable outcome is a restricted four-dimensional positive-sign construction/reduction and a sharper map of where the negative cutoff-flow chain must be independently checked.

This note has two purposes:

1. bank the Step-50 product-quotient conclusion at exactly the strength it supports;
2. audit the newest A03 normalized Yang reports enough to isolate the single next load-bearing negative-chain estimate for A02 to check.

## 1. Positive product-quotient wall: accepted at one-way strength

Step 50's load-bearing conclusion survives this review.  The construction is local and operator-norm calibrated:

- Eguchi--Hanson with the opposite orientation is isometric/homothetic as an unoriented Riemannian metric; the analytic pointwise/weighted estimates transfer, while the first obstruction uses the opposite chiral block.
- At the product quotient \((S^2\times S^2)/\mathbb Z_2\), Steps 44--45 verified
  \[
    R_+=R_- = \operatorname{diag}(\Lambda,0,0),
  \]
  so both chiral blocks have a two-dimensional kernel.  Kernel choices kill the vector first obstruction \(R_\varepsilon(p)\zeta=0\) at every \(A_1\) point and for every chirality assignment.
- Once the first obstruction vanishes, the refined residual is higher order in the Yau--26 norm: in the clean model it gives \(O(t)\) on the EH core and \(O(t^{1/2})\) on the standard transition annulus; using only Ozuch/Biquard weighted estimates still gives a positive power tending to zero.  Higher exact-Einstein obstructions may block an actual Einstein gluing, but they do not block \(\|\operatorname{Ric}-\Lambda g\|_{op}\to0\).

Thus every actual mixed orientation filling \(M_r\), \(r=1,2,3\), produced by the four-node construction carries positive near-Einstein input metrics in the sense of the positive branch.  After rescaling, it enters any dimension-four positive pinching interval.

The direction of implication is only:

\[
  P_4^+ \quad\Longrightarrow\quad M_r\text{ admits some Einstein metric.}
\]

It is not an existence theorem for \(M_r\), and it is not a refutation of Yau--26.  It is a hardness reduction: the positive noncollapsed product-quotient arc has reached the wall where the remaining question is independent Einstein existence on these mixed smooth four-manifolds.

## 2. Minimal topology/status of the mixed rows

The minimal facts recorded in Step 50 are enough for the reduction and should not be inflated:

- Armstrong plus the standard \(\mathbb RP^3\)-filling van Kampen picture make simple-connectedness plausible and adequate for the current reduction; a final theorem would still write the boundary-normal-generation argument explicitly.
- Rational bookkeeping gives
  \[
  \chi(M_r)=8,
  \qquad (b_+(M_r),b_-(M_r))=(1+r,5-r),
  \qquad \tau(M_r)=2r-4 .
  \]
- Mixed rows have \(b_+\ge2\), positive scalar curvature from the near-positive-Einstein metrics, and strict Hitchin--Thorpe \(2\chi=16>3|\tau|\).
- Ordinary Seiberg--Witten/LeBrun obstructions do not apply directly: for \(b_+>1\), positive scalar curvature kills the usual SW invariants/moduli, while Hitchin--Thorpe is silent.
- The balanced \(r=2\) row may be homeomorphic to \(\#_3(S^2\times S^2)\) in an even boundary-gluing realization, but Step 50 correctly does **not** assert spin or smooth diffeomorphism type.  The discriminant-glue probe is only an algebraic model and shows parity is not forced by the existing data.

A useful public formulation is therefore:

> The positive branch is at least as hard as deciding Einstein existence on explicit simply connected positive-scalar-curvature four-manifolds with \(b_+\ge2\).  All known simply connected compact positive Einstein four-manifold examples in the session record have \(b_+\le1\), and no available theorem excludes or constructs a positive Einstein metric on the mixed rows.

The phrase "all known examples" is a status statement, not a theorem.  It should be paired with the source-backed open-status observation from Step 41/Broder/Liu, not used as a proof of nonexistence.

## 3. Relation to A01 Q-Gorenstein smoothing

A01 #378 is valuable but does not overturn the Step-50 positive wall.  Its Aubin--Yau chain applies to general-type product-quotient canonical models with ample canonical class and global Q-Gorenstein smoothing.  The A01 note itself says the positive \(S^2\times S^2\) quotient rows are not covered by that negative-KE mechanism, and mixed chirality may be non-holomorphic.  Thus the two conclusions are compatible:

- general-type product-quotient surfaces may become Einstein-existence evidence if globally Q-Gorenstein smoothable;
- positive mixed \((S^2\times S^2)/\mathbb Z_2\) rows remain a one-way hardness reduction for \(P_4^+\).

There is no reason for A02 to spend the next step computing spin, V4 topology, or attempting a Seiberg--Witten obstruction on these PSC mixed rows unless a new error appears.

## 4. Audit of A03 normalized Yang reports

I read A03 `step50_normalized_yang_wang_verification.md`, A03 `step51_normalized_yang_precise_estimate.md`, Yang's local Ricci-flow source lines 785--878 and A.7/B.1 lines 1069--1136, Wang's continuation source lines 392--571, and the older A03 conditional theorem notes.

### 4.1 The normalization reaction: final coefficient correct, intermediate sign wrong

For the normalization-only variation
\[
  \partial_t g=-2a g,
\]
constant scaling already fixes the sign.  The fully lowered curvature contribution and norm variation give
\[
  \partial_t |\operatorname{Rm}|^2 = 4a|\operatorname{Rm}|^2
  +2\langle \operatorname{Rm},g\owedge\nabla^2a\rangle.
\]
The volume variation is
\[
  \partial_t d\mu=-n a\,d\mu,
\]
not \(+na\,d\mu\).  Therefore the normalization-only reaction in
\(\frac{d}{dt}\int F^p\) is
\[
  (2p-n)\int aF^p .
\]
At \(p=n/2\) this vanishes exactly.  This is the important identity and it is correct in A03 Step 51's final formulas (lines 297--315 and summary lines 523--559), but the intermediate §2.2 lines 144--191 contain a contradictory \((2p+n)\) computation and should be superseded or patched before the note is treated as a stable proof.

### 4.2 Hessian source: A03's stated IBP is not yet safe, but a safer repair exists

A03 Step 51 tries to eliminate
\[
  p\int F^{p-2}\langle\operatorname{Rm},g\owedge\nabla^2a\rangle
\]
using the KN trace identity and contracted Bianchi.  The conclusion is plausible, but the displayed argument line 233 uses a bound like \(|\Delta_g a|\le C\).  That is not available from mere metric equivalence: this is exactly the cutoff-jet issue A03 Step 50 correctly emphasized.  A final proof should not rely on a prescribed evolving Hessian/Laplacian bound for the fixed scalar cutoff.

A safer estimate is to avoid contracting to Ricci/Bianchi and integrate one derivative directly from \(\nabla^2a\) onto \(F^{p-2}\operatorname{Rm}\).  Since \(a=\chi^2\),
\[
  |\nabla a|^2/a = 4|\nabla\chi|^2,
\]
so, schematically,
\[
\begin{aligned}
\left|\int F^{p-2}\operatorname{Rm}*\nabla^2a\right|
&\le C_p\int F^{p-2}|\nabla\operatorname{Rm}|\,|\nabla a| \\
&\le \varepsilon\int a|\nabla\operatorname{Rm}|^2F^{p-2}
   +C_{p,\varepsilon}\|\nabla\chi\|_\infty^2\int F^{p-2} \\
&\le \varepsilon\int a|\nabla\operatorname{Rm}|^2F^{p-2}
   +C_{p,\varepsilon}\|\nabla\chi\|_\infty^2(\operatorname{Vol}+\int F^p).
\end{aligned}
\]
This uses the weighted dissipation already present in Yang's curvature-energy calculation and no evolving Hessian bound for \(\chi\).  It supports the qualitative A03 claim that no new non-homogeneous Moser theory is needed, but it changes the proof route and leaves the additive volume term and sequence-uniform constants to be checked in the first-exit setting.

### 4.3 Start/restart: use the Step-50 transported-coefficient reduction, not the resurrected nonlinear regularization

A03 Step 50 made a clean distinction: the nonlinear \(a+\varepsilon^2\) start was withdrawn because metric equivalence does not control cutoff jets, and the reliable start is a direct perturbation of Yang's transported-coefficient DeTurck/Nash--Moser construction.  A03 Step 51 §4.5 then reintroduces coefficient regularization language.  That should not be the cited module.

For A02's purposes, the defensible statement is:

- per-datum normalized short-time start/restart reduces to Yang's displayed hatted system, with the added term
  \[
    \delta(-2\widehat a\widehat g)
    =-2\widehat a h+4\widehat\chi d\widehat\chi(\zeta)\widehat g
  \]
  occupying Yang's lower-order \(D h+E\psi\) slots;
- this imports Yang's tame inverse rather than reconstructing it;
- sequence-uniform smoothing and the restricted IL gap still depend on the first-exit preservation estimates.

## 5. What is now the single negative-chain interface to check?

The newest A03 reports improve the start/restart and terminal-slab continuation modules, but they do not by themselves prove the restricted Ishida--LeBrun gap.  The older A03 conditional theorem itself identifies the hard module as (A2): simultaneous first-exit energy preservation.  The theorem needs, on the selected support and up to time \(T=\theta r_*^2\),
\[
\widehat H_2(t)\le2\widehat H_2(0),\quad
Q(t)\le e^{C\theta}Q(0),\quad
J_6(t)\le e^{C\theta}J_6(0),
\]
plus the pointwise consequences
\[
\|a\operatorname{Rm}(t)\|_\infty\le C\bar\beta/t,
\qquad
\|aE(t)\|_\infty\le C\delta(r_*^2/t)^{1/3}.
\]
This is the narrow next A02 verification target.  It is smaller than "review the whole negative flow theorem" and more relevant than rechecking the per-datum Yang existence again.

The first sub-estimate to attack should be the normalized critical \(H_2\) / \(L^2\) inequality on the actual selected support, with the corrected reaction sign and the safe Hessian-source integration above.  The question is not merely whether the formal coefficient \(2p-n\) vanishes, but whether the resulting additive \(\operatorname{Vol}\) term, Sobolev constants, support volume, and smallness/self-improvement thresholds remain uniform in the Ishida--LeBrun sequence.  If this fails, the restricted negative theorem breaks at the earliest analytic stage.  If it passes, the next checks are the coupled \(Q(t)\) and \(J_6(t)\) preservation estimates under the same normalized source terms.

## 6. Allocation after this audit

- **Banked:** positive product-quotient arc = citable one-way hardness reduction for \(P_4^+\), not a counterexample route.
- **Highest-value next work:** independent A02 check of A03's first-exit energy preservation interface, beginning with the corrected normalized critical \(H_2\) inequality on the selected support.
- **Keep alive but not next unless a new idea appears:** positive collapse via almost-Killing/Bochner field production.
- **Bounded future probe:** the \(n\ge5\) codimension-four stratum-integral idea deserves a small structural test later because it is the only active all-dimensional front, but it should not preempt the negative-chain cross-check at this moment.

No branch of the full Yau--26 proposition is proved, refuted, or formalized by this audit.
