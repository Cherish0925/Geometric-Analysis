# Step 92 seed for the tubular-collar continuation

> **Step 93 correction.** The proposed target (6.2)
> \(\int(|h_\nu|+\sqrt{e_\nu})\,dn\) diverges on exact cusps (the
> Strategist identified this). More critically, backward Maxwell
> propagation from a cusp end gives exponentially growing bounds (TTCS
> Step 93 counterexample), not length-independent ones. The signed
> transport \(w(n)\le e^{-3n}w(0)+O(\delta)\) is valid only in the
> forward direction (separator toward cusp). The self-consistent
> thresholds \(\delta^{**}=0.186\) and \(0.210\) are withdrawn.
> Use `workspace/notes/step93_signed_transport_and_koiso_ot.md` for the
> corrected analysis.

This is a research-facing handoff, not an established collar theorem.

Let \(n\) be signed base distance from the invariant minimizing curve \(C\),
let \(s\) be arclength on each nearby curve in a Fermi chart, and write the base
metric locally as
\[
\gamma_B=dn^2+a(n,s)^2ds^2.
\]
At \(n=0\), the lift \(\Sigma\) is minimal, not necessarily totally geodesic.
The separator analysis supplies
\[
V=\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q,
\qquad
\int\rho V\phi^2\le\int\rho[(\phi_s)^2+(3-E_{\nu\nu})\phi^2].
\]
After conjugation,
\[
\mathcal W=\frac34V+\frac18(h^2+e_s)
\]
has one-dimensional capacity control, and tangential Maxwell transport gives a
finite \(\sup_CQ\). Step 92 also constructs fully constrained, fully stable
analytic central data whose Koiso Einstein germs have \(\sup e_\nu\to\infty\).
Thus the unresolved issue is not local realizability of normal orbit energy but
its propagation across a collar of uniform geometric length.

The next derivation should be made in these geometric variables, without
assuming a Gaussian foliation by minimal curves:

1. **Normal Maxwell law.** With \(w=\sqrt{2Q}\), retain
   \[
   |\partial_nw+\tfrac32h_\nu w|
   \le\tfrac12w\sqrt{e_\nu}+2\sqrt2\delta.
   \]
   The quantity that must be bounded is
   \(\int(|h_\nu|+\sqrt{e_\nu})dn\), not merely pointwise separator data.

2. **Orbit-map equation.** In the moving orthonormal frame, expand
   \(\tau_\sigma(U)=-\nabla Q+Z\) into tangential and normal covariant
   derivatives, including the base-curve curvature and the derivatives of
   \(a(n,s)\). It controls the trace of second derivatives, so a first-normal-jet
   estimate requires a genuine energy identity across a collar.

3. **Horizontal/Codazzi equations.** Reuse the verified twist-free kinematics as
   a normalization check:
   \[
   \nabla_nU_s=\nabla_sU_n-uU_s,
   \qquad
   D_sv=h(u-v/2)-\tfrac12\langle U_s,U_n\rangle-E_{ns}.
   \]
   These formulas must be re-derived with connection twist and general Fermi
   geometry rather than copied unchanged. Mixed Ricci simultaneously sources
   Maxwell charge, so the same \(E_{ns}\) cannot be treated as independent in
   the two equations.

4. **Candidate collar energy.** Seek an identity for
   \[
   \int_{C_n}\rho\bigl(|U_n|^2+|\sigma_n|^2+2Q\bigr)ds
   \]
   whose boundary term is controlled by the stable separator form and whose
   bulk terms use the horizontal Einstein equations with favorable sign. The
   Step 90 canonical energy \(e+2Q+3|\nabla\sigma|^2\) is a natural starting
   combination but has a noncoercive large-\(Q\) reaction; the new ingredient
   must be the separator boundary form or a Codazzi flux, not the same pointwise
   reaction estimate.

5. **Concentrated Koiso benchmark.** Use the exact constrained data constructed
   in `workspace/scripts/step92_constrained_spike_koiso.py`: a closed target
   curve with \(|U_s|^2=12+2P\) and vertical Weingarten block perpendicular to
   \(U_s\) gives \(e_\nu=2P\), exact Hamiltonian/momentum constraints, full
   strict stability, and a local analytic Einstein germ. Track how the
   guaranteed analytic radius and the horizontal/normal energies depend on
   spike concentration. Either prove no concentration-independent collar can
   reach the cusp ends, or use these germs as inner data for a two-variable
   boundary-value construction.

The purpose is to decide whether the formal \(e_\nu\)-concentration escape can
extend off the separator. A rederivation must keep base metric factors,
connection curvature, and operator-norm defect normalization explicit.
