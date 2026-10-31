# Step 25 — Diagonal blow-up cells: CR pinning at finite cost, face dynamics, and the structure of minimizing sequences

Session S1003A02, Agent2. Conventions: diagonal Bianchi-IX metrics
\(g=dt^2+\sum a_i^2\sigma_i^2\), \(d\sigma_i=2\sigma_j\wedge\sigma_k\) (so \(\sum\sigma_i^2\) is the unit round \(S^3\),
\(\int_{S^3}\sigma_{123}=2\pi^2\)); \(y_i=a_i'/a_i\); costs \(\widehat P=P/(8\pi^2)\), threshold \(1\); the CH end is normalized
to \(\mathrm{Ric}=-6g\), \(a_g=a_h=\sinh t\) (contact plane), \(a_f=\sinh t\cosh t\) (Reeb slot). Compact ACH variables
\((y_f,y_g,y_h,\kappa,q,\zeta)\), \(\kappa=a_f/(a_ga_h)\), \(q=\log(a_g/a_h)\), \(\zeta=1/(a_ga_h)\), as in
`workspace/scripts/ach_projected.py`; the Rossi/neutral variable is
\[
\widetilde\Phi=q+\tfrac14(y_g-y_h)-\zeta\sinh q,
\qquad \rho_\infty=e^{\widetilde\Phi(\infty)}\ \text{on ACH ends},\qquad \widetilde\Phi\equiv0\ \text{on exact CH}.
\]

The question of this note: in the diagonal (SU(2)-invariant diagonal) class
\(\mathscr C_{\rm diag}\) of smooth metrics on \(O(-1)\) that are exactly CH outside a compact set, what can a
minimizing sequence for \(\widehat P\) do, and how is the infimum
\(p^{\rm diag}_{1,0}\le0.99585\) (certified, `Sessions/S1003A01/workspace/data/perp_area/rigorous_x00.03_X64_d16.json`)
related to exact Einstein metrics? By Theorem C and the exact-CH barrier theorem the problem may equivalently be posed
for \(P\) over scalar-\(-24\) diagonal metrics (the Yamabe factor \(u\) is unique, hence \(SU(2)\)-invariant and a function of
\(t\); it lowers \(P\) by \(24\int|\nabla u|^2+3\int(\Delta u/u)^2\)).

## 1. CR pinning: an exact identity and a sharp inequality

**Identity.** For *every* diagonal metric put \(e_i=\mathrm{Ric}(e_i,e_i)+6\) in the orbit directions. Since
\(\mathrm{Ric}_{ii}=-y_i'-y_iS+\mathrm{Pot}_i\) (\(S=\sum y_j\), \(\mathrm{Pot}_i\) the orbit-curvature potentials),
\[
y_i'=6-y_iS+\mathrm{Pot}_i-e_i ,
\]
and differentiating \(\widetilde\Phi\) gives exactly
\[
\widetilde\Phi'=\zeta^2G\;-\;\tfrac14\,(e_g-e_h)=\zeta^2G-\tfrac14\bigl(\mathrm{Ric}^\circ_{gg}-\mathrm{Ric}^\circ_{hh}\bigr), \tag{1.1}
\]
where \(\zeta^2G\) is the Einstein drift polynomial of `ach_phi_drift.py` (no constraint is used). Verified in
`workspace/scripts/cr_pinning_check.py` → `workspace/data/cr_pinning_check.json`: the control part is symbolically
\(-(e_g-e_h)/4\); the free part vanishes on the ACH curve \(E(q)\); CH and H\(^4\) solve the uncontrolled system
exactly; a randomly forced integration reproduces (1.1) to \(7\times10^{-16}\).

**Lemma P (CR pinning).** For any diagonal metric on \([T_0,T_1]\times S^3\), with \(W=a_1a_2a_3\),
\[
\Bigl|\widetilde\Phi(T_1)-\widetilde\Phi(T_0)-\int_{T_0}^{T_1}\zeta^2G\,dt\Bigr|
\le\Bigl(\frac{\widehat P_{[T_0,T_1]}}2\Bigr)^{1/2}\Bigl(\int_{T_0}^{T_1}\frac{dt}{W}\Bigr)^{1/2}. \tag{1.2}
\]
*Proof.* \(P_{[T_0,T_1]}=2\pi^2\int W|\mathrm{Ric}^\circ|^2dt\ge2\pi^2\int W\bigl((\mathrm{Ric}^\circ_{gg})^2+(\mathrm{Ric}^\circ_{hh})^2\bigr)\ge\pi^2\int W(e_g-e_h)^2\);
apply Cauchy–Schwarz to \(\frac14\int(e_g-e_h)\) with weights \(W^{\pm1/2}\) and use \(P=8\pi^2\widehat P\). \(\square\)

**Corollary P1.** If a cell is exactly CH for \(t\ge T_1\) and on \([T,T_1]\) its orbits satisfy \(W\ge c\,e^{4t}/16\) and its
state lies in a cusp block of the Step-15 type (so \(|\int_T^\infty\zeta^2G|\le\delta(T)=\sup_B|G|\,\zeta(T)^2/(2c_B)\); the
verified blocks cover \(q\in[0.70,3.20]\), e.g. \(\sup|G|\le19.58\), \(c_B\ge1.998\) for \(q\in[0.7,0.9]\); **the standard-end block
\(B(K=1,\zeta_0=10^{-2},q\in[-0.3,0.3])\) was verified this step** — all egress/ingress faces pass, \(\zeta\)-decay factor
\(\ge1.99844\), \(q\)-drift \(\le0.0111\), \(\sup_B|G|\le7.354\) — files `workspace/data/ach_block/block_K1_z0.01_q-0.3_0.3.json`,
`workspace/data/ach_block/phidrift_K1_z0.01_q-0.3_0.3.json`), then
\[
\widehat P_{[T,\infty)}\ \ge\ \frac c2\,e^{4T}\bigl(|\widetilde\Phi(T)|-\delta(T)\bigr)_+^2 . \tag{1.3}
\]
(\(\int_T^\infty16e^{-4t}/c=4e^{-4T}/c\).) Thus correcting a Rossi squashing \(\log\rho\) at radius \(T\) costs at least
\(\tfrac12e^{4T}(\log\rho)^2\) in units \(8\pi^2\).

**Sharpness (linear theory).** `workspace/scripts/squash_escape_cost.py` (data `workspace/data/squash_escape_cost.json`)
linearizes the antisymmetric sector \(a_g=Ae^{\theta/2},a_h=Ae^{-\theta/2}\) about CH: \(dz_g=-dz_h=\tfrac12\theta''+(2\coth2t+\operatorname{csch}2t)\theta'+16\frac{\cosh2t-3}{\cosh4t-1}\theta\), \(ds=0\),
kernel \(\{k^{-1},k^{-1}\!\int m\}\), \(k=\tanh^4t\). In Abel form the cost is \(\int w(\psi')^2\), \(\theta=k^{-1}\varphi\),
\(\psi=\varphi'/m\), \(m=(1+\tanh2t)^2e^{-4t}\tanh^7t/\tanh^22t\), \(w=(1+\tanh2t)^4e^{-8t}\sinh^9t/(8\cosh^5t\tanh^42t)\).
For interior data \((\varphi,\psi)(T)\) the minimum cost of reaching exact CH is \((\theta_\infty^{\rm int})^2/G(T)\) with
\(G(T)=\int_T^\infty M^2/w\), \(M(t)=\int_t^\infty m\), where \(\theta^{\rm int}_\infty\) is the conformal-infinity squashing of the
interior linearized Einstein end. Numerically \(e^{-4T}/G(T)=0.6974,0.5283,0.5005,0.50000018\) at \(T=.5,2,4,8\), and
exactly \(m\sim4e^{-4t}\), \(w\sim e^{-4t}/8\), \(G\sim2e^{-4T}\): \(Q_{\min}\sim\frac12C^2e^{4T}\). The constant \(\tfrac12\) of
(1.3) (with \(c=1\)) is therefore asymptotically optimal; the Cauchy–Schwarz equality case is the linear optimizer.

**Meaning.** The CR structure at infinity is not a free boundary datum for finite-cost cells: wherever the orbit volume is
large, the Rossi parameter is frozen at the cost \(\tfrac12e^{4T}(\Delta\log\rho)^2\). In particular the validated
nonstandard Einstein filling of Theorem E (\(\rho_\infty\in[2.1901,2.1925]\)) is *not* a bounded-cost limit of exact-CH
diagonal cells on growing compacta in which the orbits remain in the ACH block: any such cell agreeing with it to
radius \(T\) pays at least \(\approx\tfrac12e^{4T}(0.784)^2\). The "escape to the diagonal Einstein branch" degeneration is
forced to the standard value \(\rho=1\).

## 2. Off-curve excursions at large orbit volume: the conformal-infinity face

The ACH curve \(E(q)=(2,1,1,1,q,0)\) has spectrum \(\{2,0,-2,-4,-6,-8\}\). Since \(\zeta'=-\zeta(y_g+y_h)\), the unstable
manifold of \(E(q)\) lies in the invariant face \(\zeta=0\) (conformal infinity). On the face the \((y,\kappa)\)-system
\[
y_f'=6-y_fS+2\kappa^2,\quad y_{g,h}'=6-y_{g,h}S-2\kappa^2,\quad \kappa'=\kappa(y_f-y_g-y_h),\quad q'=y_g-y_h
\]
does not involve \(q\), with constraint \(y_fy_g+y_gy_h+y_hy_f-6+\kappa^2=0\). Face spectrum at \(E(q)\): \(\{2,0,-4,-6,-8\}\),
unstable vector \((0.8,-0.6,-0.6,1,0)\). `workspace/scripts/face_unstable_fates.py` (data
`workspace/data/face_unstable_fates.json`, \(\varepsilon=10^{-3},10^{-5}\)) integrates both branches:

- \(\kappa\uparrow\): finite-time blow-up (\(t\approx3.4\), resp. \(5.7\)), with \(y_g=y_h\to-\infty\): contact radii collapse at
  finite radius; this is the singular fate.
- \(\kappa\downarrow\): convergence to the real-hyperbolic AH point \(\kappa=0\), \(y_i=\sqrt2\) (the \(K=-2\) H\(^4\) end), which
  is attracting in the face (eigenvalues \(-\sqrt2\) in \(\kappa\), \(-3\sqrt2,-3\sqrt2,-6\sqrt2\) in \(y\)).

Neither branch returns to the ACH curve, and \(q\) is constant along both. Consequently a cell that is in the ACH block at a
radius where \(W\) is large cannot leave the curve and return to the exact standard end through near-Einstein dynamics:
leaving along the unstable direction leads to an AH end or a singularity, and returning requires \(O(1)\) control
where \(\int dt/W\) is tiny, which costs \(\gtrsim W\). The rigorous form needed is a shadowing statement: on intervals
where \(W\ge W_*\), the integrated control is at most \((\widehat P/2)^{1/2}(\int dt/W)^{1/2}\) by the same Cauchy–Schwarz
argument applied to every component of (1.1)-type equations, so the state is a \(\delta\)-pseudo-orbit of the Einstein flow
with \(\delta\to0\) as \(W_*\to\infty\); together with the face phase portrait (no chain from \(E(q)\) back to the curve off the
curve) this excludes large-volume excursions. The face phase portrait is so far established numerically for the
unstable branches; a validated version (or a Lyapunov function on the face) is a bounded computation.

## 3. Structure of diagonal minimizing sequences

Let \(g_j\in\mathscr C_{\rm diag}\) with \(\widehat P(g_j)\to p^{\rm diag}_{1,0}\le0.99585\), CH end normalized to
\(\mathrm{Ric}=-6\), bolt radius \(b_j\). Proved inputs: lower semicontinuity of \(\widehat P=\int\frac W4|z|^2dt\) under local
\(H^2\) convergence of noncollapsed diagonal metrics (control enters the dynamics affinely; \(z\) weakly convergent in
weighted \(L^2\)); Lemma P; Lemma Q′ (an almost-Euclidean neck enclosing the \((-1)\)-class forces
\(\widehat P\ge1-C\varepsilon\)); the bubble inequality \(\widehat P(N)\ge3|\tau+\eta|-2\chi+2/|\Gamma|=1\) for an ALE bubble on
\(O(-1)\) with \(\Gamma=1\); exact-collar Einstein rigidity (no Einstein exact-CH-collar cell).

The alternatives, after passing to a subsequence, are:

1. **Scale-separated bolt concentration** (\(b_j\to0\) with an almost-Euclidean annulus between bolt scale and CH scale):
   excluded, cost \(\ge1-o(1)>p^{\rm diag}_{1,0}\), whatever the inner geometry (Burns-type, Taub-bolt-type, collapsed).
2. **Collapsed connector** (\(b_j\to0\) without an almost-Euclidean annulus; e.g. a Taub-bolt ALF core whose Hopf circle
   stays short up to the CH scale): not excluded. This is the genuine collapse branch of the cell problem.
3. **Large bolt** (\(b_j\to\infty\)): not excluded by a proof. Numerically the cost rises above \(1\) on the area table; the
   rescaled limit would be a cohomogeneity-one metric with a flat bolt plane, and the needed statement is positivity of
   its cost per unit bolt area.
4. **Interior collapse/neck at finite radius**: necks that are almost Euclidean and enclose the bolt are excluded by
   Q′; other degenerate orbits are open.
5. **Large-volume excursion off the ACH curve**: excluded modulo the shadowing lemma and the face phase portrait (§2).
6. **Escape with a nonstandard CR structure**: excluded by Lemma P while the orbits stay in the block.
7. **Noncollapsed convergence** (none of 2–5): local smooth convergence to a complete diagonal \(g_\infty\) on \(O(-1)\)
   with \(\widehat P(g_\infty)\le p^{\rm diag}_{1,0}\); its tail lies in the block, so by Lemma P (uniform in \(j\), since
   \(\int_T^\infty dt/W_j\le4e^{-4T}/c\)) \(\widetilde\Phi_\infty(T)\to0\): \(g_\infty\) has the **standard** CR infinity.

**Theorem D (conditional structure theorem).** Assume the minimizing sequence avoids alternatives 2–4 (uniform bolt
bounds \(0<c\le b_j\le C\) and uniform orbit noncollapse on compact radii) and that its tails beyond a fixed \(T_0\) lie in
the ACH block. Then, granting the truncation lemma below, \(p^{\rm diag}_{1,0}\) is attained by a complete diagonal metric
\(g_\infty\) on \(O(-1)\) asymptotic to the standard CH end, and:

- if \(p^{\rm diag}_{1,0}>0\), \(g_\infty\) is a non-Einstein \(P\)-critical (in the diagonal class) complete cell;
- \(p^{\rm diag}_{1,0}=0\) **if and only if** there is a complete diagonal Einstein ACH metric on \(O(-1)\) with standard CR
  infinity (the "if" direction needs only the truncation lemma; the "only if" direction is the attainment).

*Truncation lemma (needed, sketched).* A complete diagonal metric with finite \(\widehat P\), in the block for \(t\ge T_0\)
with \(\widetilde\Phi\to0\), can be cut off to exact CH with cost change \(\to0\). In block coordinates the physical deviations
from CH are the stable modes of rates \(4,6\) (the rate-\(2\) direction is motion along CH itself, absorbed by matching
the radial origin and CH scale) plus the response to the control, which tends to zero because the local cost tends to
zero; a cut-off on \([R,R+1]\) then changes \(P\) by \(O(W(R)\,\mathrm{dev}(R)^2)=O(e^{4R}e^{-8R})\to0\). For \(P\) (as
opposed to \(J_6\)) no linear boundary term arises, so rate \(>2\) in \(C^2\) suffices. The written proof must make the
rate-2 matching and the forced response precise.

**Consequences for the research line.**

- In the diagonal class, the relation between positive gap, approximation, attained infimum and exact Einstein
  existence reduces (under the stated noncollapse) to one finite-dimensional dynamical question: does the
  one-parameter separatrix family of diagonal Einstein ACH fillings of \(O(-1)\) (bolt radius \(b\), anisotropy at the
  separatrix) ever reach \(\rho_\infty=1\)? The branch data (Step 15) give \(\rho_\infty\ge2.1897\) on
  \(b\in[0.138,400]\), rising to \(5.88\) at \(b=0.138\) and \(\approx1.343b\) at large \(b\), and the \(b=0.8\) fate enumeration
  finds only the mirror pair \(\rho,1/\rho\). A validated proof that \(\rho_\infty(b)\ne1\) for all \(b\) and both bolt-slot
  sectors, with the \(b\to0\) (Taub-bolt/Burns) and \(b\to\infty\) asymptotics handled analytically, would give
  \(p^{\rm diag}_{1,0}>0\) modulo alternatives 2–4.
- The escape branch therefore cannot be used to manufacture zero-cost diagonal cells from Theorem E; Theorem E is
  isolated from the standard-end cell problem in cost.
- The unresolved diagonal alternatives (collapsed connectors, large bolts, non-Euclidean interior necks) are exactly the
  collapse and concentration phenomena the closed problem must also control. The closed problem additionally needs
  actual-field identification of the CH bulk, assignment of several exceptional classes, interaction control, and
  passage from asymptotically-CH components to exact collars.

## 4. Status

Proved this step: identity (1.1) and Lemma P with its sharp linear constant; Corollary P1; the face reduction and its
\(q\)-independence. Numerical: the unstable-face fates. Conditional: Theorem D (needs truncation lemma, shadowing lemma,
and the noncollapse hypotheses). Open and decisive: the collapsed-connector branch, the large-bolt branch, and
\(\rho_\infty\ne1\) along the full diagonal Einstein separatrix family.
