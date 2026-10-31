# Step 92 route map: from separator charge control to a tubular-collar problem

> **Step 93 correction.** The backward Maxwell transport from the cusp end
> does not give a length-independent separator bound (TTCS counterexample).
> The self-consistent transport+resolvent thresholds are withdrawn. The
> Koiso OT theorem, forward cusp damping, and Ricci component distinction
> are valid. See `workspace/notes/step93_signed_transport_and_koiso_ot.md`.

## Corrected and established

1. Contracted Gauss is
   \[
   R_\Sigma=-6+D+\mathcal H^2-|II|^2.
   \]
   At the minimal separator, \(R_\Sigma=-6+D-|II|^2\). The Step 91
   positive-curvature interpretation is withdrawn; orbit energy helps supply
   negative scalar curvature. The flat-slice radial barrier remains valid.

2. The minimizing loop gives the full invariant form
   \[
   \int\rho V\phi^2\le\int\rho[(\phi_s)^2+(3-E_{\nu\nu})\phi^2]
   \]
   for every periodic \(\phi\), with
   \(V=\kappa^2+h_\nu^2/2+e_\nu/2+Q\).

3. Conjugating by \(\rho^{-1/2}\) and using both scalar formulas yields
   \[
   \int\mathcal W y^2\le\int[y_s^2+a_\delta y^2],
   \quad
   \mathcal W=3V/4+(h^2+e_s)/8,
   \quad a_\delta=9/2+3\delta/2.
   \]
   This gives unweighted capacity/Birman--Schwinger control. Stability alone
   permits height \(A\sim1/\ell\) on width \(\ell\), with bounded mass.

4. Tangential Maxwell transport couples the same \(h^2+e_s\) cost to changes
   of \(w=\sqrt{2Q}\). Capacity plus Gronwall gives a finite dimensionless
   separator bound \(\sup_CQ\le C_Q(\delta)\), independent of separator length
   and \(\rho\)-oscillation. The current constant is extremely coarse and does
   not tend to zero with \(\delta\).

5. Normal orbit energy is genuinely unbounded even under much stronger local
   hypotheses. Analytic constrained \(T^3\) data can be built with full strict
   stability and \(\sup e_\nu\to\infty\); Koiso then gives exact local analytic
   \(\operatorname{Ric}=-3g\) germs. Their existence widths need not be uniform
   and they do not have complete ends.

## Main negative-side work

The unresolved object is a tubular collar around the stable separator. Normal
Maxwell transport requires a bound on
\[
\int(|h_\nu|+\sqrt{e_\nu})\,dn.
\]
Develop the full Fermi-coordinate free-\(T^2\) equations near \(C\), including
horizontal constraint, Codazzi, orbit equation, and Maxwell source. Seek either:

- a normal flux/energy identity giving a length-independent integral bound;
- a collar \(L^2\) estimate for \(DdU\) with a trace theorem;
- a uniform-distance estimate showing the concentrated Koiso germs cannot
  propagate from the separator to the prescribed ends; or
- a two-variable continuation/gluing construction that turns the already
  realized local concentrated germs into a cylindrical connector.

Do not insert \(\sup_CQ\) for the global \(Q_+=\sup_BQ\) in the old resolvent
argument. Do not infer bounded \(e_\nu\) from bounded tension without collar
geometry and boundary data.

## Complementary lines

- The non-torus \(S^3\)-neck / \(N\#N\) route remains outside this theory.
- Positive-side peer computations now have independent numerical
  cross-reproduction for a restricted inter-node spectral mechanism, including
  same-chirality cancellations and a diagonal-balanced raw margin. They still
  require structural proof and complete Lyapunov--Schmidt/remainder accounting,
  and cannot by themselves exclude all Einstein metrics on the smooth manifold.
- No part of this route settles higher dimensions or justifies Lean
  formalization of Yau 26.

Primary note: `workspace/notes/step92_full_jacobi_maxwell_and_remaining_collar.md`.
