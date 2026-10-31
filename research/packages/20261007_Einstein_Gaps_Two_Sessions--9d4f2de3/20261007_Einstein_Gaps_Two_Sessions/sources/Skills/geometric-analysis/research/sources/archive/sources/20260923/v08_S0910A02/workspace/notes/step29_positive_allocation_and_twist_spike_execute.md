# Step 29: dimension-four allocation and twist-spike audit for the Bochner positive-collapse route

Session `S0910A02`. Agent3/Actuator. Phase Execute.

## 0. Scope

This step tests the Step-28 Bochner-center route against the strategist's corrections.  It does **not** prove or refute Yau 26.  It refines what the Bochner result can actually contribute to the positive branch, especially in the four-dimensional crux case, and checks a local obstruction to pointwise horizontal-twist control.

Main evidence files:

- `workspace/scripts/step29_dim4_allocation_and_twist_spike.py`
- `workspace/data/step29_dim4_allocation_and_twist_spike.json`
- `workspace/proofs/Step29TwistSpikeAlgebra.lean`
- `workspace/proofs/step29_twist_spike_all_components_check.json`
- `workspace/proofs/step29_noncentral_error_check.json`

A follow-up exact finite-ball residual script `workspace/scripts/step29_twist_spike_ball_residual.py` timed out at 300s and is **not** used as evidence; the reliable result here is the exact point-jet/Kaluza--Klein algebra recorded below.

## 1. Dimension-four allocation: quotient induction is not the 4D bracket crux

In a collapsed four-dimensional metric, a nilpotent fiber in an infranil/N-structure model has dimension at most three.  Over `R`, every nilpotent Lie algebra of dimension `<=3` is either abelian or the Heisenberg algebra

\[
[e_1,e_2]=b e_3,
\qquad e_3\in Z(\mathfrak n).
\]

Therefore in dimension four,

\[
[\mathfrak n,\mathfrak n]\subset Z(\mathfrak n),
\]

and the Step-28 central Bochner bound controls every fiber bracket, not merely the first central layer, once an exact or scale-correct almost-Killing central field exists.  In the single H3 bracket convention, the center operator

\[
\langle J_zX,Y\rangle=\langle z,[X,Y]\rangle
\]

has matrix

\[
J_z=\begin{pmatrix}0&b\\-b&0\end{pmatrix},
\qquad \|J_z\|_{HS}^2=2b^2,
\]

and the fiber-center gradient is

\[
|\widehat\nabla Z|^2=\frac{|Z|^2}{4}\|J_z\|_{HS}^2=\frac{b^2}{2}|Z|^2.
\]

Thus the Step-28 almost-Killing Bochner inequality gives, schematically,

\[
\langle b^2\rangle_{|Z|^2}
\le 2(\Lambda+\delta)+\frac{\int|\mathcal L_Zg|^2}{\int|Z|^2}.
\]

For `||L_Z g||=O(|Z|)` at the collapse scale, the right-hand side is bounded at the ambient curvature scale, so the scale-normalized H3 bracket tends to zero in weighted `L^2`.  This is precisely the abelian-forcing conclusion needed for the **fiber bracket part** of four-dimensional positive collapse.

Consequently, the Step-28 quotient-induction gap about pointwise `|phi|^2` is not the immediate four-dimensional obstruction.  It first becomes essential for higher-dimensional multi-step fibers (dimension at least four, total dimension at least five), where brackets not landing in the first central circle must be controlled after quotienting.

This correction matters for research allocation: the 4D positive branch should not spend its next effort proving pointwise horizontal-twist bounds merely to run a quotient induction.  Its load-bearing missing bridge is instead the existence of central exact/almost Killing fields with the correct Lie-derivative scale under **Ricci-only** pinching.

## 2. Pointwise horizontal twist is probably false: exact local Ricci jet

I tested the strategist's warning that pointwise `|phi|^2` control can fail by local dilaton compensation.  The script computes the Ricci tensor at the origin for the circle-bundle local metric

\[
g=e^{2\psi}(dx^2+dy^2+dz^2)+e^{2u}(d\theta+A)^2,
\]

with

\[
A=-\frac{B y}{2}\,dx+\frac{B x}{2}\,dy,
\qquad |F|^2=B^2=S,
\]

\[
u=\frac H2(x^2+y^2+z^2),
\qquad
\psi=\frac{p_a}{2}(x^2+y^2)+\frac{p_c}{2}z^2.
\]

The direct symbolic 4D Ricci computation gives at the origin

\[
\operatorname{Ric}_{xx}=\operatorname{Ric}_{yy}
=-\frac{2H+S+6p_a+2p_c}{2},
\]

\[
\operatorname{Ric}_{zz}=-H-2p_a-2p_c,
\qquad
\operatorname{Ric}_{\theta\theta}= -\frac{6H-S}{2}=\frac S2-3H.
\]

Solving `Ric = Lambda g` leaves `S=B^2` arbitrary:

\[
H=\frac{S-2\Lambda}{6},
\quad
p_a=-\frac{4\Lambda+7S}{24},
\quad
p_c=\frac{5S-4\Lambda}{24}.
\]

Thus arbitrarily large pointwise connection curvature `S=|F|^2` can be canceled at a point by the dilaton Hessian and the base Ricci 2-jet.  The finite-dimensional algebraic core was machine-checked in Lean:

- `Yau26Step29.all_Ricci_components_solved` passes strict dependency check with only permitted Mathlib axioms in `workspace/proofs/step29_twist_spike_all_components_check.json`.
- `Yau26Step29.noncentral_error_pos_of_bracket_ne_zero` also passes, recording the noncentral-field warning below.

The scaling samples in `workspace/data/step29_dim4_allocation_and_twist_spike.json` use `Lambda=1`, `S=2(N+1)`.  Then `H=N/3`; on a ball of radius `r=N^{-2}`, the dilaton has size `||u||_{C^0}=O(Nr^2)` and `||du||_{C^0}=O(Nr)`, both tending to zero while `|F|^2~2N` tends to infinity.  This is local/jet evidence, not a global construction.  A full finite-ball or compactly-supported version still needs transition and mixed-equation control.  The attempted exact finite-ball residual script was too expensive and timed out, so no stronger global/local-neighborhood claim is made here.

What this does reliably show is that the algebraic Kaluza--Klein Ricci equations themselves do not contain a pointwise `|phi|^2` bound.  Any proof of such a bound would need genuinely additional PDE/regularity input, and the known obstructions are severe: the 2-form Weitzenböck equation sees the full curvature operator of the base, and Step 11 already showed that `C^0` Ricci control does not control pointwise Riemann curvature.

## 3. Noncentral fields cannot replace the central bridge

For a unit left-invariant H3 field `X=e1`, the Lie derivative on the fiber metric satisfies

\[
(\mathcal L_X g)(e_2,e_3)=(\mathcal L_X g)(e_3,e_2)=-b,
\]

so its Frobenius norm square is

\[
|\mathcal L_Xg|^2=2b^2.
\]

Lean verifies the algebraic positivity statement in `Yau26Step29.noncentral_error_pos_of_bracket_ne_zero`.  This means noncentral directions are almost-Killing only at the same scale as the bracket being controlled; the Weitzenböck correction is then the same order as the Bochner gain and the inequality becomes vacuous.  The central direction is not a convenience but the mathematically special direction where the fiber metric can be exactly/almost invariant while still detecting the bracket.

## 4. What this changes for the positive branch

The positive-collapse structural route should now be organized as follows.

1. **Four-dimensional fiber brackets.**  If the collapse supplies a central circle field `Z` with `||L_Z g||=O(|Z|)`, then all possible nilpotent fiber brackets in dimension four are controlled by the center Bochner identity.  No quotient induction is needed for this bracket statement.

2. **Pointwise horizontal twist.**  Do not pursue pointwise `|phi|^2` as the next decisive 4D goal.  The local jet test makes that target suspect, and it is not needed for 4D bracket abelianization.

3. **Actual missing bridge.**  The unsolved part is to manufacture the central almost-Killing fields from `C^0` Ricci pinching alone.  Cheeger--Fukaya--Gromov would give N-structures under bounded `|Rm|`, but Step 11 denies such curvature control.  Kapovitch--Wilking/Naber--Zhang gives nilpotent short-loop groups under lower Ricci control, but not invariant metrics or Lie-derivative estimates.  The Step-28 almost-Killing formula identifies the exact estimate needed:

\[
R_Z:=\frac{\int|\mathcal L_Zg|^2}{\int|Z|^2}=O(1)
\]

at the relevant collapse scale, or stronger if one wants the exact-Killing constant.

4. **Connection to peer smoothing work.**  The A01/A03 selected-support smoothing architecture was designed for a four-dimensional negative branch, but the part that manufactures curvature-controlled geometry on buffered covers could be relevant to this positive bridge.  If it yields bounded-curvature local covers or controlled approximate symmetry at a scale dictated only by Ricci pinching and the selected support, it may provide the missing source of almost-Killing fields.  This is a concrete cross-session question, not a claim.

5. **Terminal target caution.**  Even a complete theorem saying tight positive pinching forces abelian collapse would not prove Yau 26.  It must land in topologies with known Einstein metrics or feed a separate existence theorem.  The Step-24 examples `L(q,1) x N` show one Einstein-compatible abelian outcome, but a general abelian-collapse classification ending only in “some torus/circle collapse” is not enough.

## 5. Negative-route peer audit performed in this step

Peer messages #319 and #320 report progress on the restricted four-dimensional negative Ishida--LeBrun route.  I inspected A01's `step28_terminal_recalibration_pullback.md`, A03's `step29_consolidated_conditional_theorem.md`, and reran the relevant scripts:

- `python Sessions/S0910A01/workspace/scripts/step28_terminal_pullback_constants.py` passed, confirming the terminal density bound `int mathfrakD <= 119 Q` and exponential-pullback selection ledger.
- `python Sessions/S0910A01/workspace/scripts/step28_moser_recurrence_verify.py` passed, confirming the corrected Moser exponent sums and polynomial `p`-loss compatibility.
- `python Sessions/S0910A03/workspace/scripts/verify_step29_family_extension_algebra.py` passed, confirming the `sigma=D-A/3` extension algebra, `R>=sigma`, and strengthened calibration `int(s+8sqrt6|W+|)^2 <= 864 pi^2(R-sigma)`.
- `python Sessions/S0910A03/workspace/scripts/verify_step29_uniform_gap.py` passed, confirming the **formal** volume cancellation `beta = S_sob H_2^{1/2}=C r_*^2 K_0^{1/2}` and the claimed conditional uniformity, assuming the selected-support flow hypotheses.

My judgment: the above-critical topological floor `R>=sigma` is reliable within the Ishida--LeBrun hypotheses, but it gives a metric-independent gap only at the strength allowed by the actual ratio `sigma/A` and volume control; the claimed universal gap across the full family still depends on the unresolved selected-support assumptions A1--A4 for the critical and near-critical cases.  In particular, the scripts verify algebra and bookkeeping, not the hard simultaneous PDE theorem.  This negative-route work remains a valuable conditional four-dimensional side result; it does not settle the positive branch, dimensions `n>=5`, or the all-dimensional Yau 26 proposition.

## 6. Current resolution state

The exact Yau-26 proposition remains unresolved.  Step 29 strengthens the research state by reallocating the positive-collapse effort away from pointwise quotient Ricci/twist control and toward the true bridge: central almost-Killing fields under Ricci-only pinching.  It also records a Lean-checked local algebraic obstruction to naive pointwise twist bounds.  For the crux dimension four, once a central almost-Killing N-structure direction is available, all nilpotent fiber brackets are controlled in weighted `L^2`; but the source of that field and the topological/existence endpoint remain open.
