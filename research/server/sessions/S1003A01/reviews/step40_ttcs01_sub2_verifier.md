# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step40_harmonic_class_compatibility_and_period_stiffness.md",
    "Sessions/S1003A01/workspace/scripts/step40_harmonic_class_period.py",
    "Sessions/S1003A01/workspace/data/step40/harmonic_class_period.json",
    "Sessions/S1003A01/workspace/scripts/su2_offdiag_hessian.py",
    "Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md",
    "Sessions/S1003A01/workspace/notes/step39_actual_harmonic_zero_test_and_route_comparison.md",
    "Sessions/S1003A01/workspace/scripts/step39_harmonic_zero_profile.py"
  ]
}
```

## Task

Verify the mathematics and numerics of the Step-40 note on harmonic-class compatibility of SU(2)-invariant cell variations for the perpendicular complex-hyperbolic blow-up cell. Check carefully: (a) the self-duality ODE d_t phi = (2/sqrt(det H)) H phi for invariant closed forms d(sum phi_i sigma_i) on g=dt^2+H_ij sigma_i sigma_j with d sigma_i = 2 sigma_j^sigma_k, including orientation and the factor 2; (b) the bolt exponents (0,2,2) for SD and (0,-2,-2) for ASD at a perpendicular bolt H~diag(t^2,b^2,b^2), smoothness conditions for the potential components, and the period formula int_E d(phi_1 sigma_1)=2 pi phi_1(0); (c) the SU(2)-averaging argument that for invariant variations supported in the cell the b^- solvability conditions int<h0, Omega o beta> = 0 collapse to a single exceptional condition, and the claims that the host period angle eta does not move at first order while j>=1 isotypic variations do not move exceptional periods at first order; (d) the Klein-group character localization of the obstruction in the h13 block and the decoupling from diagonal modes (including the exterior mass-null mode); (e) the rotation formula delta phi_1(0)=int theta' Phi dt and the gauge identity; (f) whether the period-stiffness computation DeltaJ = t^2/(2 L^T H^{-1} L) is correctly assembled from the Step-21 Hessians (note the Hessians were computed with a bolt rotation psi*(chi-1) while the period functional uses the isometric psi*chi form; check that this does not change the Hessian or the period functional), and what exactly it establishes (Ritz upper value at second order within the invariant block, floating). (g) Section 1: conformal invariance of the pair class and the claimed extension of inf P = inf J6 to pair classes defined by conditions on Omega. Also judge the interpretation in Section 3: positive exceptional areas available at quadratic cost near the perpendicular cell versus linear Kahler tariff, and what it does and does not imply for Taubes/AKGamma-type lower bounds and for the unrestricted blow-up tariff. Point out any error, missing hypothesis, or overstatement, and give the corrected statement.

## Output

# Verification memo: Step 40 (harmonic-class compatibility and period stiffness of the perpendicular CH cell)

## 0. Summary

The structural analysis in §2 is correct in its main lines:

- the self-duality ODE;
- the indicial exponents;
- the averaging reduction to one condition per cell;
- the Klein-character localization in the \(h_{13}\) block;
- the gauge identity and the rotation formula (up to a sign).

The numerics reproduce what the code computes. Five points change the content of the note:

1. **Factor-2 error in the exceptional period.** The script normalizes the potential of \(2\Omega\), not of \(\Omega=\tfrac12 d(\phi\sigma_f)\). The true period is \(\int_E\Omega=\pi\phi_1(0)\), not \(2\pi\phi_1(0)\). A direct Kähler computation confirms that the comparison slope \(6/\pi\) refers to \(\int_E\) of the Kähler-normalized form. The corrected stiffness is therefore \(K\approx32.35\), i.e. \(\Delta J\approx16.2\,t^2\). The crossover with the Kähler law is \(t\approx0.12\), and the subthreshold band is \(t\lesssim0.017\).
2. **The remainder is \(O(t^4)\), and the Ritz formula needs no Lagrange correction.** The Klein symmetry makes \(t\) odd and \(J\) even in the \(h_{13}\) block. So the remainder is \(O(t^4)\) rather than \(O(t^3)\), and \(t^2/(2L^TH^{-1}L)\) is the exact second-order constrained value with no Lagrange-curvature correction.
3. **Invariant variations leave \(\eta\) fixed exactly.** For invariant variations, constancy of \(\eta\) is an exact nonlinear statement: the host periods are literally unchanged. The reason given ("\(K_X\cdot E=0\)") is not the operative one.
4. **The \(j\ge1\) statement holds only up to global mixing.** "\(j\ge1\) variations never move exceptional periods at first order" is not exact on the closed manifold. It holds up to the non-invariant part of the global harmonic ASD representative of \(PD(E)\) on the cell.
5. **The \(t\neq0\) invariant SD form has no zeros.** It is not "generically lower-dimensional". By SU(2)-invariance and ODE uniqueness the zero set is empty. The deformed glued form is therefore symplectic, and \((|\Omega|_g/\sqrt2)\,g\) is a smooth almost-Kähler metric. This is the strongest consequence of Step 40, and the note misses it.

Details follow.

---

## (a) The self-duality ODE

**Closed invariant forms.** Write an invariant 2-form as \(\sum a_i\,dt\wedge\sigma_i+\sum b_i\,\sigma_j\wedge\sigma_k\) (cyclic). Using \(d\sigma_i=2\sigma_j\wedge\sigma_k\), one finds \(d(b_i\sigma_j\wedge\sigma_k)=b_i'\,dt\wedge\sigma_j\wedge\sigma_k\), because the \(\sigma\)-terms cancel. Also \(d(a_i\,dt\wedge\sigma_i)=-2a_i\,dt\wedge\sigma_j\wedge\sigma_k\). Closedness is therefore \(b_i'=2a_i\), so every invariant closed form is \(d(\sum\phi_i\sigma_i)\) with \(a=\phi'\) and \(b=2\phi\). ✓

**Self-duality for general \(H\).** Split \(\omega=dt\wedge\alpha+\beta\). With orientation \(dt\wedge\mathrm{vol}_3\), \(\star\omega=\omega\) is equivalent to \(\beta=\star_3\alpha\). For the metric \(H_{ij}\sigma_i\sigma_j\),
\[
\star_3\sigma^i=\sqrt{\det H}\,H^{il}\,(\sigma\wedge\sigma)_l .
\]
Hence \(\sqrt{\det H}\,H^{-1}\phi'=2\phi\), that is \(\phi'=2H\phi/\sqrt{\det H}\). It is \(H\), not \(H^{-1}\), and the factor 2 is the structure constant. ✓ The ASD case flips the sign. ✓

**Consistency with Step 39.** On the CH collar, \(a_f=\sinh t\cosh t\) and \(a_g=a_h=\sinh t\). The relation \((a_ga_h)'=2a_f\) reproduces \(\phi'/\phi=2a_f/(a_ga_h)\) with \(\phi=a_ga_h\). It also shows that \(\tfrac12 d(\phi\sigma_f)=a_f\,e^0\wedge\sigma_f+a_ga_h\,\sigma_g\wedge\sigma_h\) is exactly the Kähler form. The orientation used is the one making the Kähler form SD, as required.

## (b) Bolt exponents, regularity, and the period

**Exponents.** Take \(H=\mathrm{diag}(t^2,b^2,b^2)\).

- SD: \(\phi_1'=2t\phi_1/b^2\) gives exponent 0; \(\phi_{2,3}'=2\phi_{2,3}/t\) gives \(t^2\).
- ASD: exponents \(0,-2,-2\).

Both ✓. The ASD regular solution is \(\psi_-=1/\psi_+\). ✓

**Smoothness conditions.** \(\phi_1\) must be even in \(t\) with \(\phi_1(0)\) free. This holds because \(\sigma_2\wedge\sigma_3=\tfrac12 d\sigma_1\) is basic, and \(\phi_1'/t\) is smooth. Under the fibre rotation, \(\sigma_2+i\sigma_3\) has weight 2, so \(\phi_{2,3}=O(t^2)\) is required, and the exponents supply exactly that.

**Regularity beyond the indicial level.** "All three solutions are smooth" is only an indicial statement: resonant coupling through off-diagonal \(H\) could in principle produce \(\log\) terms. A clean argument avoids the issue. Bounded solutions give a bounded closed SD form on the complement of a codimension-2 set. Such a form is a weak solution of \((d+d^*)\omega=0\) across the bolt, so it is smooth by elliptic regularity. This argument should replace the exponent count.

**Period formula.** Fibre integration gives \(2\pi^2=\int_{S^3}\sigma_1\sigma_2\sigma_3=2\pi\int_{S^2}\sigma_2\wedge\sigma_3\), so \(\int_{S^2}\sigma_2\wedge\sigma_3=\pi\). Then \(\int_E d(\phi_1\sigma_1)=2\pi\phi_1(0)\). ✓ (This matches Chern number 1 for the connection \(\sigma_1\).)

**The normalization error.** The note sets \(\Omega=\tfrac12 d(\phi\sigma_f)\) with \(\phi=a_ga_h\), which equals \(x\) on the collar. The script integrates from \(y=(0,0,X)\) and uses `Lt = 2π·ell`. That is the potential of \(2\Omega\). Hence
\[
\int_E\Omega=\pi\phi_1(0),\qquad t_{\rm true}=t_{\rm note}/2 .
\]

## (c) Averaging, \(\eta\), and isotypic sectors

**Equation (2.1).** It is the correct linearization: \((1-\star)\dot\Omega=\dot\star\Omega\), \(\Lambda^-=d^-\Omega^1\oplus\mathcal H^-\), and \(\dot\star\) kills the trace part. There are \(b^-(M)=b^-(X)+k\) conditions.

**Averaging.** With \(h\) and \(\Omega\) both invariant on \(U\), the pairing is linear in \(\beta\), so \(\beta\) may be replaced by its average. The average is an invariant closed ASD form that is bolt-regular, hence equal to \(c\,\beta_E\). Moreover \(c=\int_E\beta/\int_E\beta_E\), because the periods on the translates \(gE\) agree. ✓

The argument uses linearity in \(\beta\) at fixed invariant \(\Omega\). It does not extend to other, non-invariant SD harmonic forms when \(b^+>1\).

**Stronger, nonlinear version.** For any invariant variation supported in the cell, integrate the SD ODE inward from the unchanged collar data. The result is a closed, SD, smooth (by the regularity argument above) form on the whole closed \(M\). Its host periods are exactly those of \(\pi^*\omega_X\), and its class is \(\pi^*[\omega_X]-t\,PD(E)\). So:

- \(\eta\) is unchanged to all orders, not just first order;
- the only effect is the exceptional period, computed exactly by the nonlinear ODE (as the script does).

The operative reason is that the form coincides with the host form outside the cell, or equivalently that \(PD(E)\perp\pi^*H^2(X)\). It is not \(K_X\cdot E=0\). In the A02 split the combination \(\eta+e\) still moves linearly through \(e\sim t\,k/A\).

**The \(j\ge1\) statement needs correction.** On the closed manifold, the first-order change of exceptional period is \(\int\langle h^\circ,\Omega\circ\beta_*\rangle\), where \(\beta_*=\sum_\gamma(\int_E\gamma)\gamma\) is taken over an orthonormal basis of \(\mathcal H^-_g\). The restriction \(\beta_*|_U\) is not SU(2)-invariant, because it solves a global problem involving the non-invariant host. Its \(j\ge1\) part pairs with \(j\ge1\) variations.

Corrected statement:

- \(j\ge1\) variations do not pair with \(\beta_E\);
- their effect on exceptional periods equals the pairing with the non-invariant part of \(\beta_*|_U\);
- that part is generated at the collar, where \(\beta_E\sim e^{-3t}\) is matched to the host.

Conversely, invariant variations do pair, weakly, with host directions \(\gamma\) through \(c(\gamma)\propto\int_E\gamma\). Smooth host ASD forms have no \(j=0\) component near the point, since invariant ASD forms on flat \(\mathbb C^2\) are \(\sim r^{-2}\). Hence these periods arise only from the gluing correction.

The leading host channel is indeed the adjoint isotype: \(\Lambda^-\otimes\mathbb C\cong\Lambda^{1,1}_0\cong\mathfrak{su}(2)_{\mathbb C}\), while \(\Lambda^+\) is SU(2)-trivial. This matches the three invariant SD solutions.

## (d) Klein characters

The right translations by the elements of \(V_4\subset SO(3)\) map the cell (bolt fibration included) to itself and fix diagonal \(H\). They act on \(h_{12},h_{13},h_{23}\) by the three distinct nontrivial characters. ✓

\(\Omega\) carries a character of its own: it changes sign under flips of \(\sigma_3\). Renormalizing to the collar, \(t(\rho h)=\varepsilon_1\varepsilon_3\,t(h)\). The linear functional therefore lives in the character of \(h_{13}\), and the ODE result (2.3) agrees.

Consequences missing from the note:

1. **No Lagrange-curvature term.** In the \(h_{13}\) block \(t\) is odd and \(J\) is even. Also \(t\equiv0\) on the diagonal sector (exactly). So \(\partial^2t/\partial k^2=0\) and \(\partial^2t/\partial d^2=0\). The mixed term \(\partial^2t/\partial d\,\partial k\) is allowed, but it gives \(d=O(t^2)\) and contributes \(O(t^4)\). Thus \(t^2/(2L^TH^{-1}L)\) is the exact second-order constrained minimum. Restricting to the \(h_{13}\) block loses nothing at this order, since the \(h_{12}\), \(h_{23}\) and diagonal blocks have zero Hessian coupling.
2. **Evenness.** \(j(t)=j(-t)\), so \(J(t)=J_0+\tfrac12Kt^2+O(t^4)\).

Decoupling of the mass-null and diagonal modes in the \(J\)-Hessian holds by the character argument, provided the mode is diagonal. It is a second-order statement at a cell whose diagonal gradient vanishes, which is true for the floating optimizer within its basis.

## (e) Rotation formula and gauge identity

**Rotation.** With \(R'=\Theta\), \(\delta H_{13}=H_{11}-H_{33}\) per unit angle; this matches the code's \(R_{02}=-\sin\), \(R_{20}=+\sin\). Then \((\phi_f/\psi_+)'=(\phi_f/\psi_+)\cdot2(H_{33}-H_{11})/\sqrt{\det H}\). Integration by parts with \(\theta(t_c)=0\) and \(\phi_f(0)=0\) gives
\[
\delta\phi_1(0)=-\int_0^{t_c}\theta'\,\Phi\,dt .
\]
The sign should be stated.

**Gauge identity.** \(\int2(H_{11}-H_{33})\phi_f/(\sqrt{\det H}\,\psi_+)=-X\). ✓ Numerically \(10^{-10}\).

**Growth of \(\Phi\).** On the collar \(\psi_+\propto\tanh^2t\) is bounded. So \(\Phi\approx\psi_+(0)\,x\); for example \(5.25=0.041\cdot128\). \(\Phi\) grows like the moment map \(\sinh^2t\), not like the logarithmic Kähler potential.

**Finite-amplitude check.** For an exactly rotated bolt the period is \(2\pi\,\phi(0)\cdot n\) with \(n=R(\psi)e_1\). Bolt smoothness forces \(\phi(0)\perp Re_3\), so the period equals \(2\pi\phi_1(0)/\cos\psi\). The reported deviations (\(5.4\times10^{-8}\) at \(3\times10^{-4}\), \(6.6\times10^{-7}\) at \(10^{-3}\)) are essentially \(\psi^2/2\). The check confirms linearity, but the output component should be \(\phi(0)\cdot n\).

## (f) Assembly of the stiffness

**\(\psi\chi\) versus \(\psi(\chi-1)\).** These satisfy \(R(\psi\chi)=R(\psi)R(\psi(\chi-1))\). With rotation alone the metrics are isometric, so \(J\) is equal. In the period computation only \(\theta'\) enters, provided the collar data are rotated consistently, so \(L\) is identical.

With both rotation and \(k\): Step 21 evaluates \(J(R_{\chi-1}HR^T+K)\), whereas \(R(\psi)\)-conjugating the Step-40 metric gives \(J(R_{\chi-1}HR^T+R^TKR)\). Here \(R^TKR-K\) contains a diagonal \((11,33)\) term of order \(\psi c\). The cross Hessian entries therefore differ by \(\nabla_{\rm diag}J\) applied to that diagonal direction:

- this is zero at an exact critical cell;
- it is of the size of the residual diagonal gradient outside the profile basis for the floating cell.

It is not identically zero by symmetry, since \(\psi c\) has trivial character.

**Bookkeeping.** The coefficient ordering \([c_0,\dots,c_{n-1},\psi]\) matches. The `cheb` used in the Hessian must equal numpy's \(T_0,\dots,T_{n-1}\) for \(L\) and \(H\) to refer to the same basis. That function is not shown, so this is unverified.

**Corrected values** (profile scale, \(t=\int_E\Omega\)):

| Quantity | Note | Corrected |
|---|---|---|
| \(K\) | 8.09 | 32.35 |
| \(\Delta J\) | \(4.04\,t^2\) | \(16.17\,t^2\) |
| \(\Delta J\) in \(\operatorname{Ric}=-g\) scale (\(t_g=6t\)) | \(0.112\,t_g^2\) | \(0.449\,t_g^2\) |
| Crossover with Kähler law | 0.472 | 0.118 (0.120 including the offset \(1-J_0\)) |
| Subthreshold band | \(t\lesssim0.034\) | \(t<\sqrt{(1-J_0)/16.17}\approx0.017\), i.e. \(t_g\lesssim0.10\) |

**Independent check of the slope \(6/\pi\).** For a Kähler cell equal to CH outside a compact set with \(a=\int_E\omega\):

- \(\Delta\!\int s\,dV=-4\pi a\);
- \(\Delta V=-a^2/2\);
- \(\Delta(2\chi+3\tau)=-1\).

The identity \(\int|\mathrm{Ric}^\circ|^2/2=\int s^2/8-4\pi^2(2\chi+3\tau)\) then gives
\[
\Delta\!\int|\mathrm{Ric}^\circ|^2=8\pi^2+48\pi a+72a^2+\tfrac14\!\int e^2 ,
\]
i.e. \(1+6a/\pi+\dots\) in \(8\pi^2\) units. So the Kähler law uses the Kähler-normalized area, confirming the factor-2 mismatch.

**What the computation establishes.** For the floating \(x_0=.038\) cells there are explicit smooth SU(2)-invariant metrics \(g(sc^*)\) with exceptional period \(t(s)=s+O(s^3)\) and
\[
J=J_0+\tfrac12K_{\rm Ritz}t^2+O(t^4).
\]
\(K_{\rm Ritz}\) decreases monotonically with \(n\) (8.0944, 8.0863, 8.0861, before correction), as an upper Ritz value should. The \(O(t^4)\) term is uncontrolled. A finite-amplitude evaluation of \(J\) along \(sc^*\) at \(t\sim0.005\)–\(0.02\) with the Step-21 evaluator would turn this into actual values.

Two qualifications:

- The value is the true second-order stiffness among all variations only if the \(j\ge1\) Hessian is nonnegative modulo gauge, which is still open (Step 21 §2).
- None of this is certified. The Arb-certified profile is \(x_0=.03\).

## (g) §1 conformal invariance

The step is correct: \(\star\) on \(\Lambda^2\) is conformally invariant, and closedness, self-duality, periods, zero set, and the collar identity (after the cutoff factor \(u_R=1\) there) are all preserved. With \(J_6\ge P\) and \(J_6(u^2g)=P(u^2g)\le P(g)\), this gives \(\inf P=\inf J_6\) on each such class.

Hypotheses that should be stated:

- **Existence of \(u\).** Existence and uniqueness of \(u\to1\) rest on \(s<0\) (Step 21, Theorem 2), or on the Step-23 sign-free version, which is not visible here. Uniqueness follows from the maximum principle for the cubic.
- **Which conditions are allowed.** "Conditions on \(\Omega\) alone" must mean conformally invariant ones. Conditions involving \(|\Omega|_g\), such as almost-Kählerness or amplitude pinning, are not preserved, since \(|\Omega|_{u^2g}=u^{-2}|\Omega|_g\).
- **The CH end.** \(\Omega\) is the Kähler form of \(g\), not of \(u^2g\), except on the restored exact collar.

## Interpretation of §3

**The \(t\neq0\) form has no zeros.** An invariant SD form vanishes at \(t>0\) only if \(\phi(t)=0\), which forces \(\phi\equiv0\) by uniqueness for the nonsingular linear ODE. On the bolt its tangential part is \(2\phi_n(0)\,\sigma\wedge\sigma\neq0\). Hence, for every \(t\neq0\) in the family, the glued SD harmonic form \(\Omega_t\) is nowhere zero. It is a symplectic form in the class \(\pi^*[\omega_X]-t\,PD(E)\), and
\[
\hat g_t=\frac{|\Omega_t|_g}{\sqrt2}\,g
\]
is a smooth almost-Kähler metric. The singular Step-28 metric arises only as \(t\to0\), where \(|\Omega_t|\sim t\) on the bolt.

This is consistent with Taubes. The symmetry \(\rho\) maps \(E\mapsto-E\), so the two signs carry \(K=\pi^*K_X\pm E\) with positive area on the corresponding exceptional class. Positivity of the period does not need to be large.

**What follows.** Per cell, sub-tariff cost (\(J<1\)) is compatible with genuinely symplectic configurations, at quadratic cost in the period. Any lower-bound argument that relies on near-minimizers having zero exceptional period, or on the harmonic form having zeros, cannot hold.

The closed smooth AKΓ theorem applies to \((\hat g_t,\Omega_t)\), but it bounds \(\hat g_t\), not \(g_t\). The conformal factor degenerates like \(t\) on each bolt, so \(\hat g_t\) has curvature concentrating at scale \(\sim t\) while \(J(g_t)\) stays near \(J_0\). AKΓ/Taubes information transfers to \(g\) only through an estimate for that conformal factor, which is the missing object.

**What does not follow.**

- \(J\) rises along the family, so there is no improvement of \(J_0\).
- The comparison with the linear Kähler law contrasts two different branches. The non-robustness of the unit tariff was already contained in \(J_0<1\). Step 40 adds that the saving survives into the symplectic regime for \(|t|\lesssim0.017\).
- It says nothing about the unrestricted per-blow-up tariff, which still depends on the non-invariant \(j\ge1\) Hessian and on global host mixing.

The quantities that remain unresolved are:

- the \(j=1\) host-period stiffness;
- the nonlinear \(j(t)\);
- the conformal-factor estimate relating \(\hat g_t\) to \(g_t\).