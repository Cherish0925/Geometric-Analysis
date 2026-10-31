# Route assessment after Step 55

Session: S0910A01. Agent3 / Actuator. Phase: Execute.

## 1. What changed mathematically

Step 55 repaired two substantive interfaces in the restricted four-dimensional Ishida--LeBrun negative-gap route.

### Coupled first-exit variables

The Step 54 first-exit bootstrap had used an evolving unweighted assumption \(|E(t)|\le\delta\).  This is not available for the cutoff flow.  The correct variables are
\[
\Gamma(T)=\max_\alpha\sup_{0\le t\le T}\widehat{\mathcal S}_\alpha(t)H_{2,\alpha}(t)^{1/2},
\qquad
V(T)=\int_0^T\|aE(t)\|_{L^\infty(M,g(t))}\,dt.
\]
The metric comparison is
\[
e^{-2V(T)}g(0)\le g(T)\le e^{2V(T)}g(0),
\]
and in dimension four Sobolev constants are transported by
\[
\widehat{\mathcal S}_\alpha(t)=e^{8V(t)}\mathcal S_\alpha(0).
\]
This removes the unsupported appeal to maintaining Ricci lower bounds under metric drift.  Under \(\Gamma\le\gamma_*\), the local energy inequality is used as
\[
H_2'+cD_2\le C(1+r^{-2})H_2+C\|aE\|_\infty H_2.
\]
The weighted defect endpoint
\[
\|aE(t)\|_\infty\le C_E\delta(r^2/t)^{1/3}
\]
is integrable, giving
\[
V(T)\le {3\over2}C_E\delta\theta^{2/3}r^2
\quad (T\le\theta r^2).
\]
Thus small \(\theta,V_*\), small initial \(\Gamma(0)\), and small initial defect close the paired self-improvement without any evolving unweighted defect bound.

TTCS verified this structure and corrected the displayed sufficient condition for \(V(T)\le V_*/2\): the sharp scale is
\[
\delta\le {V_*\over 3C_E\theta^{2/3}r^2},
\]
while the stronger \(r\)-independent condition is only optional when \(r\le1\).  The note was patched accordingly.

### Shifted \(H_2\) and no \(Y(0)\)

A03 Step57 supplied a term-level shifted-curvature \(H_2\) calculation.  TTCS confirmed its core, with two important qualifications:

1. Its displayed \(C_0=O(\operatorname{Vol})\) must be local:
   \[
   C_{0,\alpha}\le C\int\eta_\alpha^2a\,d\mu\le CH_{2,
\alpha},
   \]
   so it is absorbed into the multiplicative \(H_2\) term.  It is not a full-manifold volume source repeated for each support.
2. The closure must not use \(Y(0)\).  A03 Step58 repaired this with the direct bridge
   \[
   Y=\int\eta^2aF_T^3
   \le C\mathcal S H_2^{1/2}(D_2+r^{-2}H_2)
   =C\gamma(D_2+r^{-2}H_2),
   \]
   followed by spacetime control of \(D_2,Y\) and the curvature endpoint
   \[
   \|aF_T(t)\|_\infty\le C\Gamma/t.
   \]

This is now the correct curvature branch to combine with the Step 55 \((\Gamma,V)\) bootstrap.

## 2. Finite positive-time restart threshold

A03 Step57 showed that the base positive-time block
\[
T,T_1,U_1,C_2\in L_t^\infty L_x^q \quad \forall q<\infty,
\qquad |T|_\infty<\infty,
\]
can be obtained by the Step56 base pair plus Kato and Sobolev.  This is useful, but pointwise curvature does not make the small-cutoff collar ordinary parabolic.  Fixed-coordinate restart still requires finite current-pair estimates and the background connection difference
\[
\bar\nabla=\nabla^{g(\tau)},
\qquad A=\nabla^{g(t)}-\bar\nabla.
\]
The triangular system is
\[
\bar\nabla^m\partial_tA
=g^{-1}*U_{m+1}+P_m(A_0,\ldots,A_{m-1};U_0,\ldots,U_m),
\]
so current bounds through \(U_{s_0}\) give \(A_0,\ldots,A_{s_0-1}\), and then
\[
\bar\nabla^{m+1}g=A_m*g+\text{lower products}.
\]
For the local theorem threshold \(s_0>n/2+4=6\), the minimal integer is \(s_0=7\).  A sufficient finite package is
\[
T_0,\ldots,T_6,
\qquad (U_1,C_2),\ldots,(U_7,C_8).
\]
The highest \(C_9\) terms should appear only as \(\chi C_9\) and be integrated by parts; no independent \(C_9\) bound is required.

## 3. The next exchange actually computed

The new note `workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md` treats the next nontrivial stage \((U_2,C_3)\).  The corrected top structure is
\[
\partial_tU_2
=\operatorname{div}(a\nabla U_2)
+\chi C_4*U+\chi C_3*U_1+\chi C_2*U_2
+C_1*C_3*U+C_2*C_2*U+C_1*C_2*U_1+
\mathcal L_2.
\]
The term \(2\chi C_1*\nabla U_2\) must be combined with \(a\Delta U_2\) as \(\operatorname{div}(a\nabla U_2)\); splitting it produces a \(C_2|U_2|^p\) term without \(C_2\in L^\infty\).

The dangerous top-cutoff exchange from \(\chi C_4*U\) is
\[
I_{31}=\int\chi |C_3|\,|U_1|\,|U_2|^{p-1}.
\]
With \(f=\chi |U_2|^{p/2}\), Hölder exponents \((4,p,4,2p/(p-2))\) for \(p>2\) and \((4,2,4)\) for \(p=2\), plus four-dimensional Sobolev on \(f\), give
\[
I_{31}\le \varepsilon D_{2,p}^U+C_{p,
\varepsilon,\tau}(1+\|C_3\|_p^p+\|U_2\|_p^p).
\]

TTCS found a missing current signed-Hessian term \(\chi C_2*U_2\).  It is now added and treated by
\[
J_2=\int\chi(C_2)_{ij}\mathcal B^{ij}(U_2),
\quad |\mathcal B|\le C|U_2|^p,
\quad |\nabla\mathcal B|\le Cp|U_2|^{p-1}|\nabla U_2|,
\]
so one integration by parts gives
\[
|J_2|\le \varepsilon D_{2,p}^U+C_{p,
\varepsilon}\|C_1\|_\infty^2\|U_2\|_p^p.
\]
The cutoff evolution
\[
\partial_tC_3=C_1*U_2+C_2*U_1+\text{lower}
\]
then closes with the \(U_2\) equation:
\[
{d\over dt}(\|U_2\|_p^p+\|C_3\|_p^p)+cD_{2,p}^U
\le C_{p,\tau}(1+\|U_2\|_p^p+\|C_3\|_p^p).
\]
The same correction applies to the \(T_2\) stage through \(\chi C_2*T_2\).

The structural script `workspace/scripts/step55_finite_restart_threshold_verify.py` now includes checks for the divergence operator, the \(\chi C_2*U_2\) and \(\chi C_2*T_2\) terms, the Hölder exponents, and the finite restart package.  It passes 16/16 and writes `workspace/data/step55_finite_restart_threshold_verify.json`.

## 4. Terminal localization

The terminal local compactness must remain on exponential pullback balls
\[
\mathcal B_\rho(p)\subset T_pM,
\qquad \tilde g_p=(\exp_p)^*g(T),
\]
not on image balls in the collapsed base.  Rauch comparison provides controlled pullback volume and geometry.  The mean density is
\[
A_\rho\Phi(p)=\fint_{\mathcal B_\rho(p)}(\exp_p)^*\Phi\,d\mu_{\tilde g_p},
\]
and the Step53 unit-tangent Liouville argument controls \(\int_{P^{\rm in}}A_\rho\Phi(p)\,dp\) without injectivity of \(\exp_p\).  If the local forbidden-germ step is phrased through smooth compactness, terminal plateau derivative bounds on a smaller pullback ball must be supplied after finite continuation is closed.

## 5. Route value

The restricted IL theorem is now more sharply organized but still not complete.  The remaining proof object is a single coherent proposition combining:

1. A03 Step58's no-\(Y(0)\) curvature branch with the Step55 \((\Gamma,V)\) paired bootstrap;
2. The defect endpoint and local/global \(Q\) propagation in the same paired bootstrap variables;
3. The finite positive-time restart package through \((U_7,C_8)\) and \(T_6\), including proof-level expansion of the general \(k\le7\) signed-Hessian and cutoff-exchange terms;
4. Fixed-background \(A\)-integration to get terminal \(H^{s_0}\) convergence and restart;
5. Terminal pullback-ball derivative bounds for the local forbidden-germ compactness.

This remains the closest path to a genuine restricted four-dimensional negative gap theorem.  It would still not prove or disprove the full Yau 26 proposition, because the positive branch, arbitrary four-dimensional topology, dimensions \(n\ge5\), and Lean formalization remain open.

A02 Step59 is important route context: its H4-dual necessity analysis identifies a hard two-scale weighted matching problem on Eguchi--Hanson bubbles.  That front may distinguish controlled obstruction-classification from wild bubbling, but it is currently a separate analytic problem and does not replace the IL first-exit/restart work.
