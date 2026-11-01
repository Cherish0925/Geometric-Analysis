# Step 69 start — close the balanced-tower matching law using Theorem 59.R

The next mathematical object is not another local cell optimization. It is the global error ledger turning one fixed strict cell into the existential balanced-cover coefficient below 4.

## Inputs to read together

1. A01 construction/arithmetic:
   - `Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md`
   - `Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md`
   - `Sessions/S1003A01/workspace/notes/step35_cap_transfer_neutrality_and_cap_cells.md`
2. A02 local expansion:
   - `workspace/notes/step59_rigorous_burns_expansion_and_zero_gap_structure.md`, especially binding Part D
   - `workspace/notes/step57_kernel_burns_coefficient_general_background.md`
   - theorem package §§19–20
3. Certified endpoint:
   - `Sessions/S1003A01/workspace/data/perp_area/rigorous_x00.03_X128_d20.json`
   - current coefficient `3.996151138093450...` in A01 Step 33.

## Statement to establish

For a suitably chosen ramified negative-KE cover family with `Q_m` disjoint buffered lifts of one fixed cell, and the balanced topology `(k_m,l_m,Q_m)=(8Q_m,7Q_m,36Q_m)` after the prescribed separated surgeries,
\[
P(g_m)=P(g_{\rm KE,m})+8\pi^2Q_m p_{\rm cell}+o(Q_m),
\]
with every error source written explicitly and uniformly. This yields the existing existential `limsup alpha/h < 3.9961512`; it is not a theorem for every prescribed cover tower.

## Exact global error ledger

Prove that the sum of the following is `o(Q_m)`:

- host mismatch on each buffered ball: `Q_m * omega(epsilon_m)`, where `epsilon_m=||g_m-g_CH||_{C^2(K)} -> 0` (raise the derivative order if the smoothing construction/59.R requires it);
- collar smoothing: choose smoothing width `delta_m -> 0` only after fixing the strict cell, with per-site loss `omega_s(delta_m)`;
- metric positivity/interpolation errors on annular buffers;
- interactions: zero for disjoint supports at the raw metric level; any global conformal/Yamabe correction must have a separate additive estimate rather than being called independent;
- topology-balancing handle surgeries and cap transfer errors, with their exact normalized weights (blow-ups and handles are not interchangeable);
- background ALE/ADE resolution error if canonical-model KE orbifolds are used;
- rounding errors in `Q_m`, `k_m`, `l_m`, and the denominator `h_m`.

Theorem 59.R supplies a moving-background second-order local law when the host is genuinely P-critical on the full insertion support. For the exact certified CH-collared cell, the stronger direct transfer may suffice; state which route is used and do not double-count the AK-tail and Ricci cost. The all-sector correctors show that `W^-` and `Ric^0` do not create an additional logarithmic corner penalty, but they do not remove ordinary finite matching errors.

## Arithmetic/geometric supply to check

- Residual finiteness gives one buffered embedded ball in a preliminary finite cover; further covers give disjoint lifts.
- Verify the required number of selected lifts relative to `Q_m` and to the cover degree.
- In ramified towers, write the actual asymptotics `Delta_m/A_m -> 0`, `Q_m/A_m -> 0`, and the balanced ratio; do not silently pass from one cover sequence to all sequences.
- If positive-r cap sites are invoked, A01 Step 35 says the Heisenberg lattice inclusion/central-index write-up is unfinished. The balanced `r=0` endpoint should avoid depending on that unfinished proposition if possible.

## Output

A dependence-ordered theorem with a one-line diagonal choice of scales/cover levels, plus an exact normalized coefficient calculation. Ask Agent4 to review §§19–21 by Step 72–73 after this law is integrated, not after all later work.