# Step 18 plan: execute the toric `#_k(S^2 x S^2)` crux

Session S0910A02.  This plan is the operational handoff from Agent1 after the
Step-18 correction note.

## 1. Corrected global premise

Do not use Hitchin--Thorpe violators as positive-branch enemies.  By the
sign-blind Chern--Weil lemma, if
\[
\|\operatorname{Ric}-\sigma g\|_{op}\le \varepsilon<1/(1+\sqrt3),
\qquad \sigma=\pm1,
\]
then `2 chi > 3 |tau|`.  Thus `#_5 CP^2` and `#_4 CP^2` never enter the
arbitrarily tight pinched class.  The positive four-dimensional branch is now a
pinching-rigidity/BUILD problem unless a genuinely new Einstein-nonexistence
mechanism is invented.

The active crux family is `#_k(S^2 x S^2)`, `k>=2`: strict HT, positive Ricci
known in the sourced survey/Sha--Yang line, large Euler characteristic, and not
known in this session record to admit Einstein metrics for large `k`.

## 2. Candidate toric topology family

Use the periodic characteristic labels
\[
(1,0),(0,1),(-1,0),(0,-1),(1,0),(0,1),\ldots
\]
on an even `m=2k+2`-gon.  The source `Toric-Einstein-4-manifolds...` lines
84--86 gives the Orlik--Raymond polygon/slopes description and determinant
condition; lines 41 and 512 give the connected-sum/topological/Sha--Yang context.
The local determinant condition holds: adjacent determinants are all `±1`.

A sanity checker was written and fixed:

* script: `Sessions/S0910A02/workspace/scripts/step18_toric_topology_checker_integral.py`
* data: `Sessions/S0910A02/workspace/data/step18_toric_topology_checker_integral.json`

For `m=4,6,8,10,12`, the checker obtains an integral intersection form of rank
`m-2`, determinant `±1`, even parity, and signature `0`.  Hence it is consistent
with `#_{(m-2)/2}(S^2 x S^2)` over the standard simply connected even unimodular
form classification.  This is a topology sanity check, not a substitute for a
full Orlik--Raymond proof.  If the next step relies critically on exact
diffeomorphism type, it should either source the classification statement more
fully or give an elementary handle argument for the periodic labels.

## 3. Metric formulation: start with diagonal only as a probe, then upgrade

A globally diagonal fiber metric
\[
g=g_B+p^2d\theta^2+q^2d\phi^2
\]
is natural only when the same two circle generators degenerate on all rods in an
alternating way.  The periodic label family alternates these generators, so a
diagonal ansatz is a plausible first probe.  But because rod labels repeat and
orientation signs change around the polygon, a general smooth `T^2`-invariant
metric should be represented by
\[
  g=g_B+h_{IJ}(d\phi^I+A^I)(d\phi^J+A^J)
\]
with a positive definite `2x2` fiber matrix on the principal region, linearly
rank-one degeneration `h(v_i,v_i)=O(r^2)` at rod `i`, and smoothness conditions
as in source lines 100--128 and 132--138.

Therefore:

1. **First computation may be diagonal/twist-free** to test the candidate collapse
   mechanism cheaply.
2. If the diagonal residual has a persistent obstruction that could be an ansatz
   artifact, immediately move to a non-diagonal matrix-fiber residual evaluator.
3. Do not interpret a diagonal failure as a theorem for toric metrics.

## 4. Pinched Ricci residual for the diagonal probe

On the principal orbit region with base metric `g_B` and
\[
 w=pq,
 \qquad v=\log(p/q),
\]
the vertical eigenvalues are
\[
  r_p=-\Delta\log p-|\nabla\log p|^2
      -\langle\nabla\log p,\nabla\log q\rangle,
\]
\[
  r_q=-\Delta\log q-|\nabla\log q|^2
      -\langle\nabla\log p,\nabla\log q\rangle.
\]
Equivalently,
\[
  r_p+r_q=-\Delta w/w,
  \qquad
  r_p-r_q=-w^{-1}\operatorname{div}(w\nabla v).
\]
The horizontal block is
\[
  \operatorname{Ric}^H=K_Bg_B-\left[\nabla^2\log w+
  \frac12(d\log w\otimes d\log w+dv\otimes dv)\right].
\]
The positive normalized pinching error is
\[
  \delta(g)=\sup_{\Omega}\max\{ |r_p-1|, |r_q-1|,
  \| (\operatorname{Ric}^H)^a{}_b-\delta^a_b\|_{op}\}.
\]
The next script should evaluate this residual on a discretized curved polygon or
on a conformal rectangle surrogate with imposed rod boundary conditions.

## 5. Formal collapse seed

Use the Step-15 high-negative-edge model as initialization, not as proof:
\[
K_B|_{rod}=-A_m,
\qquad A_m\sim m^2,
\]
so
\[
 Q''+(1+2A_m)Q=0,
 \qquad \Phi_i=\int Q_i ds\approx \frac{2}{1+2A_m},
 \qquad \sum_i\Phi_i\sim m/A_m\to0.
\]
The optimizer should attempt to realize this boundary profile while satisfying
all four Ricci eigenvalue inequalities to small `delta` and keeping smooth rod
slopes.  The previous flat Faber--Krahn area barrier is not available without a
base-curvature lower bound, so do not enforce it as a hard obstruction.

## 6. Minimal Execute tasks

### Task A: topology certificate

For `m=6,8,10`, output labels, adjacent determinants, intersection matrix,
parity, determinant, and signature.  Save a short JSON certificate.  If possible,
reduce the matrix by integer congruence to `kH`; if not, record the current form
classification as a sanity check only.

### Task B: diagonal residual evaluator

Implement functions for a conformal base `g_B=e^{2\phi}(dx^2+dy^2)` and scalar
fields `p,q` on a polygon/rectangle surrogate:

* compute `w=pq`, `v=log(p/q)`, `K_B=-e^{-2phi} Delta_E phi`;
* compute gradients/Hessians/Laplacians in `g_B`;
* compute vertical residuals `r_p,r_q` and horizontal residual eigenvalues;
* enforce rod behavior by boundary profiles: on alternating sides, `p~dist` or
  `q~dist`, with the other factor equal to the rod profile `Q_i(s)`.

Calibrate the evaluator on:

1. `S^2 x S^2`: product square/rectangle, residual zero after normalization;
2. `S^4`: quarter-sphere anchor if implemented;
3. Step-15 separated SdS/Nariai family in a rectangular/separated limit to see
   the cone-angle mismatch appear as residual or boundary slope failure.

### Task C: cheap optimization/probe

For `m=6` first, optimize a finite-dimensional family seeded by negative edge
curvature collars.  Report the best `delta`, total flux/volume proxy, and which
residual component dominates.  The outcome should distinguish:

* **constructive trend:** as `m` increases and flux decreases, best `delta` also
  decreases or remains controllably small;
* **obstruction trend:** best `delta` has a stable lower bound, and the dominant
  residual localizes at corners/rod transitions/horizontal traceless block;
* **ansatz artifact:** diagonal formulas fail due to label changes or non-diagonal
  effects; upgrade to matrix-fiber ansatz before making mathematical claims.

## 7. Interaction with peer work

A01/A03's negative-branch cutoff-flow architecture is not complete.  Messages
#281--#283 clarify that the remaining gap is degenerate epsilon-regularity:
from coupled small `L^2` energy under the `chi^2`-weighted operator to
pointwise `||chi^2 Rm|| <= C/t` on the transition.  This is important but
independent of the first A02 toric crux probe.  Continue monitoring it, and do
not cite the negative branch as solved unless that theorem is proved and checked.
