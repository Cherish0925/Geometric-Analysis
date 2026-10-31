# Step 28 — Scale-free saturation control and the revised diagonal structure theorem

Conventions are those of Steps 25–27.  The exact cost is
\[
\widehat P=\frac{P}{8\pi^2}=\int W\,|\operatorname{Ric}^\circ|^2/4\,dt,
\qquad W=a_fa_ga_h.
\]
The purpose of this Step was to turn the remaining collapsed branch into a single executable problem rather than continue pricing the long small-volume neck, and to make Theorem D depend only on the geometric escape mechanisms that remain.

## 1. Independent verification and corrections to Theorem X

Two TTCS verifier branches independently read the Cartan source, the transgression scripts, the data, and the Step-27 theorem note.  The integrated direct derivation is in
`trace/ttcs/results/step28_ttcs01_verifier1_integration.md`.

The substantive theorem is verified.  With
\[
\gamma_i=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},\qquad p_i=a_i',
\]
the long symbolic answer simplifies to
\[
S_0=\sum_i p_i^2-\sum_{\rm cyc}\gamma_i p_jp_k+2\sum_i\gamma_i^2,
\qquad \mathfrak s=S_0-6,
\]
and the algebraic identity
\[
\sum_i\gamma_i^2+\gamma_1\gamma_2\gamma_3=4
\]
gives directly
\[
\mathfrak s'=\frac W2(B_+-B_-).
\]
Here block A is genuinely \(W^+\): its basis consists of the self-dual forms \((e^{01}+e^{23})/\sqrt2\), etc.; on complex hyperbolic space its eigenvalues are \((-4,2,2)\), while the other block vanishes.  Burns has self-dual Kähler form in the same frame orientation, and the exceptional sphere has square \(-1\).  Thus the CH complex orientation and the blow-up orientation agree.

The localized identities are therefore
\[
\widehat P(C)=\Delta\mathfrak b_+
 +\frac1{2\pi^2}\int_C|W^+|^2
 +\frac1{96\pi^2}\int_Cs^2,
\]
\[
\widehat P(C)=\Delta\mathfrak b_-
 +\frac1{2\pi^2}\int_C|W^-|^2
 +\frac1{96\pi^2}\int_Cs^2.
\]
The centre, bolt, CH, Burns and Taub-bolt charge calculations are correct.  In particular Burns realizes \((1,7)\to(2,2)\) with \(\widehat P=1\), and Ricci-flat Taub-bolt realizes \((1,7)\to(-2,2)\) with chiral energies \(3,5\).

Three repairs were inserted in `step27_chiral_transgression_and_small_bolt.md`:

1. the Chern–Weil prefactor is \(4\pi^2(2\chi\pm3\tau)\), not \(8\pi^2(2\chi\pm3\tau)\);
2. `data/chiral_flux.json` stores unshifted \(S_0\), so its raw `bA,bB` become normalized charges only after `bA+6,bB-6`;
3. the limit \((-2,2)\) applies to biaxial or controlled near-biaxial Berger collapse.  Anisotropic collapsed jets contain extra shear contributions and cannot be assigned this charge without further control.

The Corollary-X2 prose was also corrected: for a CH-shaped orbit, subthreshold compatibility requires \(\sinh^4\tau\ge(1-\widehat P)/9\); not every positive radius is allowed.

## 2. Exact scale-free full-control problem

Write
\[
a_f=re^{2\beta/3},\qquad
 a_g=re^{-\beta/3+q/2},\qquad
 a_h=re^{-\beta/3-q/2},\qquad h=\log r.
\]
Let
\[
D=R_{gg}-R_{hh},\quad
E=R_{ff}-\frac{R_{gg}+R_{hh}}2,\quad
H=R_{00}-\frac{R_{ff}+R_{gg}+R_{hh}}3.
\]
Then
\[
\begin{aligned}
D&=-q''-3h'q'+e^{-2h}\mathcal V_D,\\
E&=-\beta''-3h'\beta'+e^{-2h}\mathcal V_E,\\
H&=-2h''-\frac23(\beta')^2-\frac12(q')^2+e^{-2h}\mathcal V_H,
\end{aligned}
\]
with
\[
\begin{aligned}
\mathcal V_D&=8(e^{-4\beta/3}\sinh2q-e^{2\beta/3}\sinh q),\\
\mathcal V_E&=4e^{8\beta/3}-4e^{2\beta/3}\cosh q-8e^{-4\beta/3}\sinh^2q,\\
\mathcal V_H&=\frac23e^{8\beta/3}-\frac83e^{2\beta/3}\cosh q
 +\frac83e^{-4\beta/3}\sinh^2q.
\end{aligned}
\]
The full action is exactly
\[
\widehat P=\int r^3\left(\frac3{16}H^2+\frac16E^2+\frac18D^2\right)dt.
\tag{2.1}
\]
The independent randomized check `scripts/check_shape_control_jax.py` compared these formulas against the exact diagonal Ricci equations at 10,000 random two-jets and found maximum absolute error \(3.98\times10^{-13}\).  A direct full symbolic substitution script was also written but proved too expensive; it timed out rather than producing evidence.

Set
\[
d\tau=dt/r,
\quad p=rh',\quad \xi=r\beta',\quad \eta=rq',
\quad (\bar H,\bar E,\bar D)=r^2(H,E,D).
\]
Then, for \(Y=(\beta,q,p,\xi,\eta)\),
\[
\begin{aligned}
\dot\beta&=\xi,&\dot q&=\eta,\\
\dot p&=p^2-\xi^2/3-\eta^2/4+\mathcal V_H/2-\bar H/2,\\
\dot\xi&=-2p\xi+\mathcal V_E-\bar E,\\
\dot\eta&=-2p\eta+\mathcal V_D-\bar D,
\end{aligned}
\tag{2.2}
\]
and
\[
\widehat P=\int\left(\frac3{16}\bar H^2+\frac16\bar E^2+\frac18\bar D^2\right)d\tau.
\tag{2.3}
\]
All absolute scale has disappeared.  This establishes the strategist's central point: the long collapsed neck does not carry a new \(b\)-dependent price.  The decisive object is a scale-one saturation map.

For numerical work, regularize collapse by
\[
x=\beta-q/2=\log(a_f/a_g),\qquad z=e^{-q/3}=(a_h/a_g)^{1/3},
\qquad \chi=\xi-\eta/2.
\]
The Taub-bolt/\(\Lambda\)-Taub-NUT entry ray at a scale-one base radius \(A\) is
\[
I_\varepsilon(A)=\left(
 x=0,
 z=\varepsilon^{1/3},
 p=z(2U+V)/3,
 \chi=0,
 \eta=z(U-V)
\right),
\]
where
\[
U=\sqrt{1+2A^2},\qquad V=\frac{2A^2}{\sqrt{1+2A^2}}.
\]
This retains the first-jet matching and does not enlarge the entry set to arbitrary Berger data.

The target is the nonlinear standard-CR stable set of the uncontrolled Einstein compact flow, on a fixed section such as \(\zeta=10^{-2}\).  It is not characterized by the finite formula \(\widetilde\Phi=0\) alone: one also needs the Hamiltonian constraint, absence of the nonlinear outgoing mode, and limiting \(\Phi_\infty=0\).  The mathematical value is
\[
\mathcal V_{\rm sat}
=\liminf_{\varepsilon\downarrow0}\inf
 \int\left(\frac3{16}\bar H^2+\frac16\bar E^2+\frac18\bar D^2\right)d\tau,
\tag{2.4}
\]
over solutions of (2.2) joining the entry ray to that stable set.

The full derivation, terminal map, Pontryagin equations, Gramian test and Hamilton–Jacobi subsolution inequality are in
`trace/ttcs/results/step28_ttcs01_generator1_integration.md`.  For a lower bound one must keep all three controls.  In particular, for effective shape acceleration \(a=-\bar E+\bar D/2\),
\[
\min_{-\bar E+\bar D/2=a}\left(\bar E^2/6+\bar D^2/8\right)=a^2/8,
\]
so a \(D\)-only model gives the wrong value.

## 3. Pilot optimal control and what it establishes

`scripts/saturation_optimal_control.py` implements (2.2)–(2.3) by Hermite–Simpson collocation and IPOPT.  It uses the regularized potentials, free entry phase \(A\), free duration, and all controls \(\bar H,\bar E,\bar D\).  `scripts/saturation_endpoint_residuals.py` independently maps endpoints back to compact ACH variables and follows their uncontrolled Einstein fate.

The first terminal test deliberately required an exact finite CH orbit.  This is much stronger than standard-CR stable-set membership and, more importantly, it is not scale-consistent with a finite \(\zeta=10^{-2}\) section: the pilot produced costs
\[
3.38823\quad(\varepsilon=.25,N=30),\qquad
3.75033\quad(\varepsilon=.125,N=40),
\]
but the mapped endpoints lie far outside the ACH block and flow to the real-hyperbolic face.  These values do **not** estimate (2.4).

A second test imposed only the Hamiltonian constraint, the linear outgoing covector and \(\widetilde\Phi=0\).  Its nominal cost \(3.37634\) was also rejected: the endpoint's uncontrolled Einstein continuation left the block and became singular.  This computation is useful because it proves that the linear terminal equations are not a substitute for the nonlinear stable manifold.

Two progressively stronger stable-set proxies were tried: eigenmode data at \(\zeta=.01\), then backward integration from \(\zeta=10^{-4}\) using the physical stable modes.  The best feasible pilot on the latter proxy at \(\varepsilon=.25,N=50\) has cost about \(4.616\), but the endpoint constraint residual under the independently reconstructed compact variables is still about \(10^{-5}\), and its forward fate drifts to the real-hyperbolic face.  It therefore remains a route-finding computation, not a lower bound and not a certified competitor.  The next computation must parameterize the exact stable manifold by validated backward shooting, rather than impose approximate finite-section formulas inside the optimizer.

The negative result from the pilot is nevertheless sharp enough to change method: no trustworthy evidence of a sub-\(0.99585\) collapsed construction has appeared, but numerical optimization cannot establish positivity.  The branch now asks for either an exact low-cost stable-set connection or a Hamilton–Jacobi/subsolution estimate for (2.2).

## 4. Revised diagonal compactness statement

The chiral identities reorganize the compactness argument.  On every region where orbit shape and \(W\) stay in a compact set, \(\mathfrak b_\pm\) are bounded and the exact annular formulas control the weighted chiral curvature and scalar curvature by \(\widehat P\) plus bounded endpoint flux.  In one dimension, the Ricci combinations enter the second-order state equations affinely; hence finite cost gives local weak \(H^2\) control, and after excluding collapse and shear this upgrades to local compactness.  Bolt regularity fixes the starting charge \((1,7)\), while Theorem T gives exact-CH truncation once a limiting tail enters the verified standard block.

This removes arbitrary a priori "bolt bounds and block tails" from the conceptual statement.  Failure of compactness for a diagonal minimizing sequence can occur only by:

1. small-bolt collapse through the saturation problem (2.4), including anisotropic shear;
2. large-bolt escape;
3. an interior high-shear/volume-bounce path on which a chiral flux falls sufficiently to evade upward-variation bounds;
4. end escape along the conformal-infinity face.

Scale-separated ALE concentration is already excluded sharply by \(\mathfrak b_+\); nonstandard-CR escape in a large-volume ACH block is excluded by Lemma P; ordinary post-Rossi product/ALF collapse is excluded by the Euler flux; exact standard-CR ends are provided by Theorem T after convergence.

**Revised Theorem D.**  Let \(g_j\) be scalar-\(-24\) diagonal exact-CH-ended metrics on \(O(-1)\), with \(\widehat P(g_j)\) approaching the diagonal infimum.  If the four mechanisms above admit positive costs exceeding the available minimizing budget (or are excluded by the corresponding exact flow statement), then a subsequence converges to a complete scalar-\(-24\) standard-CR ACH minimizer; Theorem T identifies its value with the exact-ended infimum.  Therefore
\[
p^{\rm diag}_{1,0}=0
\quad\Longleftrightarrow\quad
\text{there exists a complete diagonal Einstein ACH filling of }O(-1)
\text{ with standard CR infinity},
\]
provided those four branch results hold.  The implication from Einstein existence to zero infimum is already unconditional by Theorem T.  The reverse implication follows from the compactness conclusion and attainment.

This is shorter than the Step-25 form: bounded bolt size, compact noncollapse and block entry are consequences once the actual escape mechanisms are excluded, rather than independent assumptions.

## 5. Closed-manifold transfer

Ge–Jiang's account of Cheeger–Tian shows that collapsed \(\varepsilon\)-regularity uses a pointwise Ricci bound and fails for general critical metrics.  The diagonal chiral identities bypass that input because they are exact one-dimensional transgressions.  The unrestricted closed problem has no such automatic replacement.  Its collapse theorem must therefore use the near-minimizing property itself — for example a field/variational equation generating a pointwise Ricci floor, or an F-structure along which the Euler and signature transgressions can be integrated — rather than invoke regularity theory from critical \(L^2\) control alone.

## 6. Next mathematical work

The high-value continuation is now precise:

* build a validated two-dimensional parameterization of the nonlinear standard-CR Einstein stable set on \(\zeta=.01\), by interval backward shooting from the \(-4,-6\) modes, and couple it to the full-control collocation;
* compute the finite-\(\varepsilon\) value along several decreasing \(\varepsilon\) only after terminal membership is independently verified;
* derive a Hamilton–Jacobi subsolution for the full scale-free system on the residual high-shear domain, using the exact chiral fluxes as state barriers;
* prove large-bolt and face no-return estimates, completing the remaining branches of revised Theorem D.
