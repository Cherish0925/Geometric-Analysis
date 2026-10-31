# Route assessment after Step 26

## Main correction

The Step 25 first-exit reduction was too weak.  Plateau bounded curvature and
plateau defect estimates are enough for the eventual Derdzinski contradiction,
but they do not preserve the analytic environment on the transition where the
support energy estimates live.  Current Sobolev constants, cutoff-gradient
bounds, and the critical product beta_a(t) all require whole-active-support
metric comparison.

The correct metric comparison target is

\[
V(t)=\int_0^t\|aE(s)\|_{L^\infty(\operatorname{supp}\chi)}ds,
\qquad e^{-2V(t)}g_0\le g(t)\le e^{2V(t)}g_0 .
\]

The factor a=chi^2 in the velocity is not enough by itself; E could grow where
chi is small.  Therefore transition stability must be supplied by a weighted
velocity estimate, not discarded in favor of plateau regularity.

The Step 25 first-exit note has been patched with this supersession.

## New analytic asset

Step 26 formulates the fixed-p weighted defect energy

\[
J_p=\int\eta^2 a^{p-2}|E|^p,
\quad
Z_p=\int\eta^2a^{p-1}|E|^{p-2}|\nabla E|^2,
\quad
z_p=\eta a^{(p-1)/2}|E|^{p/2}.
\]

Testing the homogeneous defect equation should give

\[
J_p'+c_pZ_p\le C_pr^{-2}J_p+C_p\int\eta^2a^{p-1}F|E|^p.
\]

The curvature potential is exactly `F z_p^2`, and the same critical curvature
product absorbs it:

\[
\int Fz_p^2\le C_p\beta_a(t)(Z_p+r^{-2}J_p).
\]

Initial pinching gives `J_p(0)<=C delta^p Vol(Omega)` without initial
supercritical Riemann curvature integrability.  The ledger scripts verify the
powers and volume cancellation.

The most useful concrete exponent is p=6:

\[
J_6=\int\eta^2\chi^8|E|^6,
\qquad z_6=\eta\chi^5|E|^3.
\]

Use standard `(|E|^2+eps)^{3/2}` regularization or weak Kato estimates; do not
claim |E|^3 is smooth at E=0.

## Yang-template match

Yang Appendix B, lines 1127--1136 of the retrieved source, gives a local heat
estimate with output `|chi^2 f|` from spacetime input
`int chi^{2p0-n} f^{p0}` and a potential condition
`(int chi^{q-n}u^{q/2})^{2/q}<=mu`.  Setting n=4, p0=q=6, f=|E|, u=F gives:

\[
\chi^{2p0-n}=\chi^8,
\qquad
\left(\int\chi^{q-n}F^{q/2}\right)^{2/q}
=\left(\int\chi^2F^3\right)^{1/3}.
\]

Thus the q=3 curvature layer should feed directly into a support-wide weighted
velocity bound

\[
\|aE(t)\|_\infty\le C\delta (r^2/t)^{1/3},
\]

with integrable drift

\[
\int_0^{\theta r^2}\|aE\|_\infty dt\le C\delta r^2\theta^{2/3}.
\]

The script `workspace/scripts/step26_yang_b1_instantiation.py` verifies the
scaling `S^{1/3}t^{-1/2}(t delta^6 V)^{1/6}=delta r^{2/3}t^{-1/3}` for
`S~r^2 V^{-1/2}`.  TTCS confirmed that this is a real Yang-type template, not
just dimensional bookkeeping, and found no immediate Hardy obstruction because
the cutoff weights prevent inverse-square loss.

## Source/existence status

Yang Section 8 (source lines 787--823) proves short-time existence for the fixed
cutoff local Ricci flow.  In the DeTurck construction, the hatted coefficient is
`(chi o phi^{-1})^2`; after pullback, this returns the fixed spatial coefficient
`chi^2`.  The normalized term `-2chi^2 g` should be included in the hatted flow
as `-2(chi o phi^{-1})^2 hat g`; it is lower order and should not change the
principal parabolic argument, but this adaptation still needs to be written.

Short-time existence for each smooth input does not give the required common
time `theta r^2`, because the initial pointwise curvature can be uncontrolled.
Uniform continuation must follow Yang/Wang's first-exit/extension pattern.
Wang's extension theorem for local Ricci flow uses a support-wide weighted
curvature bound `|chi^2 Rm|_infty`, not just plateau bounded curvature.  Hence
the continuing target includes both weighted curvature and weighted velocity on
all of `supp chi`.

## Immediate next work

1. Prove the fixed p=6 defect energy inequality at the same rigor level as the
   Codex/Step25 q=2,Q ledgers, including Kato regularization and moving norm/
   volume terms.
2. Instantiate Yang Appendix B for `f=|E|`, potential `u=F`, n=4, p0=q=6 on the
   buffered selected support.  The key input to verify is a whole time-slab
   bound for `Y=int chi^2F^3`, not only a single terminal slice.
3. Complete the q=2/q=3 curvature chain to supply that potential and a
   support-wide `|aRm|<=C/t` bound sufficient for Yang/Wang extension.
4. Write the normalized local Ricci-DeTurck construction with transported
   coefficient and show that pulling back gives the fixed-cutoff normalized
   equation.
5. Only after these analytic pieces close should the route return to the
   global defect identity, selected plateau averaging, smooth Einstein germ,
   and Derdzinski contradiction.

Scope remains unchanged: this is a conditional analytic bridge for the critical
four-dimensional negative LeBrun/Ishida-LeBrun laboratory, not a solution of the
full all-dimensional Yau Problem 26.

## Files

- Main note: `workspace/notes/step26_weighted_velocity_and_local_flow.md`
- Patched prior note: `workspace/notes/step25_first_exit_formulation.md`
- Fixed-p ledger: `workspace/scripts/step26_fixed_p_defect_velocity.py`
- p=6 ledger: `workspace/scripts/step26_p6_defect_energy_ledger.py`
- Yang B.1 exponent check: `workspace/scripts/step26_yang_b1_instantiation.py`
- TTCS verification: `trace/ttcs/results/step26_ttcs01_verifier1_integration.md`
- Codex tensor report: `workspace/codex_loop/Research_Report.md`
