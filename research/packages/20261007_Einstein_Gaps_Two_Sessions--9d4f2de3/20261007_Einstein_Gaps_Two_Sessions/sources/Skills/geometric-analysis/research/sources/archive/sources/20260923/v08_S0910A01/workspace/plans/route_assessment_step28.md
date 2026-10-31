# Route assessment after Step 28

## Main correction: downstream geometry uses exponential pullback

The Step 27 route assessment's plateau-noncollapse/F-structure direction is
superseded for the restricted four-dimensional negative LeBrun/Ishida--LeBrun
route.  Once the selected-support flow produces a sequence-uniform family of
inner plateau centers

\[
\operatorname{Vol}_{g_i(T)}(P_i)\ge \alpha A_i,
\qquad |\sec_{g_i(T)}|\le K
\]

on radius-`rho` buffers from every center in `P_i`, Step 16 exponential-pullback
averaging selects a tangent-space exponential ball with vanishing terminal
deficit mean.  The pullback tangent domain is noncollapsed by Rauch comparison
even if the base plateau is collapsed.  No Euler-density localization or base
injectivity-radius lower bound is needed.

The precise terminal density is

\[
\mathfrak D_i=|\operatorname{Ric}+g|^2+(s+4)^2+
(s+8\sqrt6|W^+|)^2+\mathcal G_i,
\]

where `mathcal G` is the Step 8 Weyl-eigenvalue gap density.  Reapplying the
mixed Seiberg--Witten/Chern--Gauss--Bonnet calibration to the terminal metric,
not transporting curvature from the initial metric, gives

\[
\int \mathfrak D_i\le119 Q_i(T),
\qquad Q_i(T)=\int|\operatorname{Ric}_{g_i(T)}+g_i(T)|^2.
\]

Thus `Q_i(T)/A_i -> 0` implies `A_i^{-1}\int mathfrak D_i -> 0`; if
`Vol(P_i)>=alpha A_i`, the pullback mean tends to zero at some `p_i in P_i`.
The Step 8 finite-`W^{2,p}`/Derdzinski argument then produces the forbidden
Einstein germ with calibrated spectrum `(-1/6,1/12,1/12)`.

## Analytic consolidation after TTCS

The patched A01 weak-Moser note now follows A03 Sections 5.2--5.3 rather than a
separate per-exponent Gronwall estimate.  The corrected bookkeeping is:

\[
\sum_k 1/p_k=(n+2)/(2p_0),
\qquad
\text{net Sobolev power}=n/(2p_0),
\]

because each step contributes `S^{1/(kappa p_k)}`.  Polynomial `p^N` losses are
kept inside the time-cutoff recurrence.  This preserves the two outputs:

\[
\|aF(t)\|_\infty\le C\beta/t,
\qquad
\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}.
\]

Fixed `J_6` persistence must start at time zero from fixed-exponent critical
absorption, not from integrating a positive-time `Y~1/t` coefficient.

The shifted-curvature continuation theorem should now be based on A03/Codex:

\[
G={g\owedge g\over2(n-1)},\quad T=Rm+G,
\quad U=aT,
\quad \operatorname{Ric}(U)=a(\operatorname{Ric}+g).
\]

This formulation prevents splitting `-2ag` as a vague lower-order term and
restores Wang's derivative induction.  TTCS supports the mechanism, while a
fully self-contained proof still needs the Wang Proposition 4.14 grouped
integration by parts, staggered Hölder exponents, and Yang degenerate restart
written out.

## Remaining mathematical obligations for the restricted negative route

The downstream pullback selection is now clean.  The real remaining issue is
upstream: prove a simultaneous selected-support theorem in the same multi-support
cutoff flow, with sequence-uniform constants, giving

1. active `H_2`/critical product persistence;
2. `S^2Y(t)<=C beta^3/t` without circular dependence;
3. fixed `J_6` persistence from time zero;
4. triangular global `Q(T)<=e^{Ctheta}Q(0)`;
5. support-wide weighted velocity for metric/Sobolev/cutoff comparison;
6. bounded-curvature inner plateaux with `Vol(P_i)>=alpha A_i` and uniform
   radius-`rho` buffers.

General-`p` tensor inequalities and shifted continuation are strongly supported
by A03 and Codex but still deserve an independently written proof if this route
is to become a theorem.

## Positive-branch update from A02

A02 Step 28 established a useful Bochner center bound for positive collapse:
for a genuine Killing central circle field `Z`, Ricci upper control gives

\[
\int|\nabla Z|^2=\int Ric(Z,Z)\le (\Lambda+\delta)\int|Z|^2,
\]

and in Heisenberg-type fibers this bounds the weighted center bracket
`<b^2> <= 2(Lambda+delta)`.  Negative Ricci kills Killing fields entirely.
A02 corrected the scope: compact nilpotent isometry algebras are abelian, so
one assumes a central circle Killing field, not a full nonabelian nilpotent
isometric action; quotient induction also needs an independent horizontal twist
`|phi|^2` bound not supplied by the Bochner center estimate; almost-Killing
errors of order `O(fiber scale)` suffice for normalized bracket vanishing.  This
is promising for positive-collapse structure but does not solve Yau-26 or affect
the current negative-flow chain.

## Scope

Even completing the restricted negative route would exclude only the critical
four-dimensional LeBrun/Ishida--LeBrun laboratory from carrying arbitrarily
tight negative normalized Ricci pinching.  It would not settle arbitrary
four-dimensional no-Einstein topologies, the positive branch, dimensions `n>=5`,
the full interval proposition, or the required Lean formalization.

## Files

- Step 28 terminal/pullback note: `workspace/notes/step28_terminal_recalibration_pullback.md`
- Patched weak Moser note: `workspace/notes/step27_unified_weak_moser_iteration.md`
- Patched continuation note: `workspace/notes/step27_normalized_continuation_theorem.md`
- Step 28 scripts: `workspace/scripts/step28_terminal_pullback_constants.py`,
  `workspace/scripts/step28_moser_recurrence_verify.py`
- A03 shifted continuation artifact:
  `Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md`
- TTCS verification:
  `trace/ttcs/results/step28_ttcs01_verifier1_integration.md`
