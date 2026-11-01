# Step 92 — Global route selection after the cusp and supplier corrections

Session S1003A01, Agent1, Explore.

This note re-evaluates the main route after Steps 90–91, Spirit #123, A02 Steps 102/104/105, and independent TTCS generation/verification. It preserves the full Einstein-gap programme. It does not treat one Wahl family, one cusp model, or one Kähler–Einstein endpoint as an exhaustive replacement for the unrestricted questions.

## 0. Binding corrections and retained results

1. A02 Proposition 104.F is withdrawn. The absence of a subgroup \(\mathbb Z^2\subset\pi_1(X)\) excludes only an injective cusp-boundary map. It does not remove cusps whose boundary map has a kernel, and non-virtual-nilpotence does not exclude bounded-curvature collapse. Thus a nonattained \(\mathscr D\to0\) sequence may still involve a finite-volume Einstein domain and a collapsed/cusp complement.

2. A02 Proposition 104.C is withdrawn as an actual-field statement. Filler transfer selects no orbifold spin\(^c\) character. The subgroup \(n\mathbb Z_{n^2}\subset H^2(L(n^2,n-1))\) describes twists extending over \(B_{n,1}\), not all orbifold cone representations. A fixed smooth spin\(^c\) structure has a definite marked boundary restriction, and twisting a spin\(^c\) structure changes the determinant character by twice the line twist.

3. A02 Proposition 104.M is now Question 105.M. A shrinking-filler field limit must start from one genuinely supplied fixed smooth basic/monopole structure, obtain global energy compactness, and identify the limiting equivariant lift and boundary holonomy. An arbitrary extending structure is not thereby basic.

4. Step 91's exact Taub–NUT mean identity is retained as a consistency test for selected averaged balances. It neither constructs the transition fields nor exhausts the integrated consequences of the coupled equations. Corollary 91.3 does not classify a positive-fraction depleted phase: its vanishing-volume hypothesis fails there, the curvature-error term is uncontrolled, and radial truncation need not retain the raw-section Kato payment.

5. The strongest direct quantitative result for \(\alpha\) remains the certified smooth CH cell, with balanced coefficient below \(3.9961512\). The unrestricted lower optimum and Q3 attainment remain open.

## 1. Independent reading of A02 Theorem 105.Q and repairs

Use
\[
C_\pm(g;D)=\frac1{2\pi^2}\int_D|W^\pm|^2+\frac1{96\pi^2}\int_Ds^2,
\qquad
\widehat P(g;D)=\frac1{8\pi^2}\int_D|\operatorname{Ric}^\circ|^2.
\]
Theorem G reads
\[
\widehat P(D)=C_\pm(D)-(2\chi\pm3\tau)(D)+\mathcal Q_\pm(\partial D),
\qquad \mathcal Q_\pm=2\mathcal E\mp3\mathcal H.
\]
If a link is oriented as \(\partial\Omega_\rho\), then the cap has the opposite boundary orientation, so the cap identity is
\[
C_\pm(C_j^{(\rho)})=(2\chi\pm3\tau)(C_j)+\mathcal Q_\pm(L_{j,\rho})+\widehat P(C_j^{(\rho)}).
\]
The plus sign in A02's cap formula is therefore correct.

At each fixed link, \(C^2\) convergence controls \(\eta\): interpolate the boundary metrics on a product cylinder and apply APS; the difference of eta terms equals an integral of the degree-four \(L\)-form, continuous under \(C^2\) convergence. This is fixed-link continuity and does not give uniform eta control as the links collapse.

Under A02's hypotheses (E), define
\[
c_j^\pm(\rho)=\lim_i C_\pm(g_i;C_j^{(\rho)}).
\]
For nested caps, the difference is the nonnegative \(C_\pm\)-energy of the intervening Einstein-domain shell. Hence \(c_j^\pm(\rho)\) decreases to a finite nonnegative iterated limit. This supplies a noncircular proof of existence. If one cap meets several ends, only the limit of the *sum* of the incident link charges follows without further end asymptotics; individual end limits need separate hypotheses.

The volume argument needs the total tail, not equality of one cap with the entire tail. Volume convergence gives
\[
\lim_{\rho\to0}\limsup_i\operatorname{Vol}(C_j^{(\rho)},g_i)=0.
\]
Together with scalar variance convergence, this gives vanishing cap scalar energy. Consequently
\[
c_j^+=\lim_{\rho\to0}\lim_i\frac1{2\pi^2}\int_{C_j^{(\rho)}}|W_i^+|^2,
\qquad
C_+(g_\infty;\Omega)=A-k-\sum_jc_j^+.
\]
These are ordered iterated limits, not an arbitrary diagonal limit.

The LeBrun mixed estimate includes the cap contribution. Put \(C=\sum c_j^+\),
\[
\int_\Omega s^2=96\pi^2x,\qquad \int_\Omega|W^+|^2=2\pi^2y,
\qquad x+y=A-k-C.
\]
The cap union contributes \(12\pi^2C\), while
\[
\int_\Omega(s-\sqrt6|W^+|)^2
\le12\pi^2(\sqrt{8x}+\sqrt y)^2
\le108\pi^2(x+y).
\]
Therefore the constant is correct:
\[
\boxed{9k+8C\le3A.}
\]
In particular this already implies \(k+C\le3A/8\), stronger than the separately quoted \(2A/3\) consequence.

For a circle-fibred Dai–Wei end, with the stated half-normalized signature eta convention,
\[
\mathcal Q_+^\infty=-e+3\operatorname{sign}e.
\]
An \(S^3\)-Hopf cap with \(b_2^-=r\) in the admissible chirality has
\[
c_+=4-r.
\]
If there are \(N\) exceptional caps and additionally \(B\) positive-charge ball caps, the corrected necessary inequality is
\[
\boxed{k+32N+32B\le3A.}
\]
The formula without \(B\) assumes no such ball caps. Four-class caps are not constructed; they are merely not excluded by this transferred estimate.

For the zero-\(c_+\) four-class cap
\[
C_4=\#4\overline{\mathbb{CP}}^{\,2}\setminus B^4,
\qquad (\chi,\tau)=(5,-4),
\]
the other chirality is
\[
\boxed{c_-=20,\qquad \int|W^-|^2\to40\pi^2.}
\]
Thus this cap is not energy-free in total curvature; its scalar, trace-free Ricci, and \(W^+\) energies vanish while \(W^-\) concentrates. A bubble tree is not supplied by (E). Even if simply connected bubbles are hyperkähler and have even lattices, there is no immediate parity contradiction: \(-D_4\subset-I_4\) is an index-two even sublattice. The characteristic vector \((1,1,1,1)\) satisfies \(K^2=\tau=-4\pmod8\), and the closed spin\(^c\) index is zero. Neither \(w_2\), the current eta bookkeeping, nor an untwisted Dirac index excludes the cap.

The first worthwhile cap calculation is therefore not a generic \(w_2\) slogan. It is the marked topology and adiabatic end correction of one actual candidate \(D_4\) ALF core and its complement: verify an embedding, the exact boundary fibration, and whether the inner and outer APS corrections can be joined by a rational-homology cobordism/collapse. A mismatch excludes that model only; a match would create a serious local carrier needing global Einstein-bulk matching.

## 2. Comparison of the strongest new routes

### 2.1 Fixed supplied-field limit on the realized Wahl complement — main route

This route exploits genuinely new global information: an actual embedded rational ball and a fixed complement. It can produce an actual Einstein–field pair on a hypothetical Wahl Einstein orbifold, rather than another class-blind integral estimate.

#### Target theorem WFL

Let \(V=V_{X,\mathbf n,k}\) be a realized Wahl orbifold and \(g\) an orbifold metric. Let \(g_\varepsilon\) be the prescribed smooth metrics obtained by inserting the orientation-matched Ricci-flat Kähler Wahl fillers. Choose a fixed supplied smooth spin\(^c\) structure \(\mathfrak s\) from the finite signed blow-up family after passing to a subsequence, and choose actual solutions \((A_\varepsilon,\Phi_\varepsilon)\) on \((M,g_\varepsilon,\mathfrak s)\). Prove that, modulo gauge, a subsequence converges on the regular part of \(V\) to a nonzero finite-energy solution that extends equivariantly across each quotient point. Identify its orbifold spin\(^c\) lift from the marked restriction of \(\mathfrak s\).

#### Uniform energy and nonconcentration mechanism

Put \(U_\varepsilon=|\Phi_\varepsilon|^2\). The unperturbed SW identities give
\[
4\int|\nabla_{A_\varepsilon}\Phi_\varepsilon|^2
+\int s_\varepsilon U_\varepsilon+\int U_\varepsilon^2=0,
\qquad |F^+_{A_\varepsilon}|^2=U_\varepsilon^2/8.
\]
Hence
\[
\|U_\varepsilon\|_2\le\|s_\varepsilon^-\|_2,
\qquad
\int U_\varepsilon^2=8\int|F_A^+|^2\ge32\pi^2(a_\varepsilon^+)^2.
\]
The sign family allows a subsequence with \((a_\varepsilon^+)^2\ge A\). For the fixed determinant class,
\[
\int|F_A^-|^2=\int|F_A^+|^2-4\pi^2a^2,
\]
so full connection curvature is uniformly \(L^2\)-bounded.

For the prescribed Lemma-86.S recovery, there is a cheaper decisive estimate. The annular bound \(|\operatorname{Ric}|=O(1)\), Ricci-flat filler interior, and fixed exterior give \(\sup s^-\le C_g\). The monopole maximum principle gives \(|\Phi_\varepsilon|^2\le C_g\), while a filled radius-\(R\) ball has volume \(O(R^4)\). Hence
\[
\limsup_{\varepsilon\to0}\int_{B_R^{\rm filled}}|\Phi_\varepsilon|^4\le C_gR^4,
\]
which directly proves spinor and \(F_A^+\) nonconcentration. No new global Sobolev estimate is needed.

A logarithmic cutoff remains useful for a later theorem assuming only scalar \(L^2\) control. In that broader setting, localized Weitzenböck gives
\[
\int\eta^2U_\varepsilon^2
\le
\|s_\varepsilon^-\|_{L^2(\operatorname{supp}\eta)}\|U_\varepsilon\|_2
+C\|d\eta\|_4^2\|U_\varepsilon\|_2.
\]
In four dimensions a logarithmic cutoff has
\[
\int|d\eta|^4\lesssim\bigl(\log(r/r_{\rm inner})\bigr)^{-3}\to0.
\]
The explicit filler transfer makes the scalar \(L^2\)-mass on a shrinking outer ball tend to zero. Proving this uniformly on the actual gluing metric would rule out \(L^4\)-spinor concentration at the Wahl point. Combined with the global lower bound, it yields a nonzero regular-part limit. For WFL, the cheapest remaining analytic work is therefore complement gauge compactness plus finite-energy equivariant removal, not the cutoff estimate.

The relevant literature supports components, not the complete theorem: Feehan–Leness gives energy bounds, local compactness, and point removability for smooth PU(2) monopoles; Suwara treats fixed smooth manifolds with rational-homology-sphere boundary and compatible gluing; neither directly proves shrinking Wahl-neck compactness or character identification. The quotient lift and holonomy therefore remain real work.

#### New Einstein–field information after extension

If \(g\) is negative Einstein, normalized by \(s=-\lambda\), then
\[
0\le U\le\lambda,
\qquad
4\int|\nabla_A\Phi|^2=\int U(\lambda-U).
\]
Writing the real determinant curvature as \(\mathcal F=2\pi h_a+d\alpha\), orbifold Hodge theory gives the exact same-field defect
\[
\frac18\int U^2-4\pi^2\|a_g^+\|^2
=
\int|F_A^-|^2-4\pi^2\|a_g^-\|^2
=
\frac12\|d\alpha\|_2^2.
\]
For \(\psi=iF_A^+=iq(\Phi)\), the self-dual Weitzenböck identity retains the direction selected by the actual field:
\[
2\int\langle W^+\psi,\psi\rangle
=
\int|\nabla\psi|^2+\frac{s}{3}\int|\psi|^2
-
\int(|d\psi|^2+|d^*\psi|^2).
\]
This is a genuine entrance to a class-sensitive exact-Einstein relation. It does not yet imply a stronger lower bound; the next theorem would need to control these derivative and harmonic-defect terms or obtain an equivariant index contradiction from the *identified* lift.

The marked affine restriction below is useful for an explicit integer label, but it need not precede the analytic theorem. Relative to a fixed local lift, \(H^2(B\mathbb Z_{n^2};\mathbb Z)\to H^2(L(n^2,n-1);\mathbb Z)\) is an isomorphism, so a fixed marked complement spin\(^c\) structure determines a unique abstract orbifold lift \(\operatorname{res}(\mathfrak s)\). When \(n\) is even, retain the full lift because its determinant loses doubling information.

The cheapest complementary topological calculation is the marked affine restriction
\[
\operatorname{Spin}^c(M)\to\operatorname{Spin}^c(L(n^2,n-1))
\]
for one actual PPS \(k=4\) block, using Kirby/plumbing data and Smith normal form. The reference spin\(^c\) lift and determinant doubling must be recorded. This would replace the withdrawn ad hoc character formula.

### 2.2 Entropy/degree rigidity — potentially profound, presently weaker

The degree-one map \(V\to X\) is valuable, but the standard Besson–Courtois–Gallot sharp theorem quoted in the corpus applies directly to real-hyperbolic targets, not to an arbitrary non-Kähler source mapping to a complex-hyperbolic surface with the needed sharpness. Kähler-source Toledo/diastatic results do not apply to the necessarily non-Kähler Einstein candidate.

Even granting the usual entropy-degree inequality and normalizing \(\operatorname{Ric}=-3g\), Bishop gives \(h(g)\le3\), whereas the CH\(^2\) entropy is \(2\sqrt2\). The resulting volume bound is only
\[
\operatorname{Vol}(g)\ge\frac{64}{81}\operatorname{Vol}(g_X),
\]
or \(u=\int s^2/(32\pi^2)\ge64A/81\), weaker than the supplied SW scalar bound \(u\ge A\). Thus ordinary entropy comparison adds no quantitative exclusion.

A valuable new theorem would have to be Einstein-specific: equality/strain rigidity for a degree-one map to CH\(^2\), controlling
\[
f^*g_X-\frac{|df|^2}{4}g
\]
strongly enough to force local complex hyperbolicity. No such theorem was found in the current retrieval. This remains a high-impact speculative route, not the next executable main line.

### 2.3 Closed Goldberg endpoint — strong secondary route

Steps 83 and 85 provide a real structural chain:
\[
D=\widehat S^2/16-2\pi^2T_+,
\qquad D=T_{\rm AK}\ge0,
\]
no \(W^+\) or torsion concentration in noncollapsed bounded-diameter AKE degeneration, and the second-order center obstruction
\[
\operatorname{Ob}_2(H_1,\beta_1)=Q_0(\beta_1),
\qquad \|Q_0(\beta)\|_2\ge c_V\|\beta\|_2^2.
\]
The most concrete target remains the one-node quintic: prove a normalized GH neighborhood of the negative-KE orbifold contains no strict AKE metric. The shortest live closure is Step 87's fixed-reduction comparison. Its decisive object is the normalized CSCK harmonic residual \(\rho_0/\zeta_r\), uniformly controlled in Ozuch's weighted source norm and modulated into one fixed Einstein reduction. A degree argument would then force the normal period \(\zeta_r=0\).

This can yield a genuine local closed Goldberg theorem, but it does not decide positive-deficit components, collapse, or the unrestricted Q1/Q2/Q3 problem. It remains the best secondary line if the Wahl field-limit analysis stalls at quotient-holonomy identification.

### 2.4 Zero-charge Hopf cap — exact object, lower immediate reach

The corrected cap theorem gives a sharply posed realization problem with exact energy split. The first calculation should test one actual \(D_4\) ALF core and marked complement, not attempt a universal parity argument. Even success supplies only a local carrier and still needs an Einstein domain and matching. Hence it ranks below WFL and the closed-Goldberg endpoint for immediate programme impact, but it is the best concrete probe of the restored collapse channel.

## 3. Route decision

The main next line is **WFL: fixed supplied-field compactness across the explicit Wahl filler family**, because it connects new global topology to actual fields on one hypothetical Einstein metric and can generate information invisible to all aggregate bounds. Execute should proceed in this order:

1. fix a genuinely supplied smooth spin\(^c\) structure (or a subsequence from the finite signed family) on the prescribed recovery metrics;
2. use the existing uniform scalar bound and maximum principle to prove lossless \(L^4\) spinor and \(F_A^+\) transfer;
3. establish compactness on the complement and finite-energy equivariant removability for the abstract marked lift \(\operatorname{res}(\mathfrak s)\); compute a numerical PPS character in parallel rather than serially;
4. use rational-ball/cone class-square preservation and Chern–Weil to prove lossless full abelian curvature and spinor-gradient transfer;
5. then test the exact Einstein–field identities and relative phase/character data for a new contradiction or rigidity theorem.

In parallel but not as a substitute, retain two bounded alternatives: the Step-87 normalized-residual estimate for a local closed Goldberg theorem, and the marked \(D_4\)-core/end-correction calculation for the zero-charge collapse channel.

External source reading used here: the registered Feehan–Leness compactness/removability source \cite{feehanmonopoles}, Suwara boundary theory \cite{suwara2023low}, Sambusetti's comparison of Einstein/entropy/SW rigidity \cite{sambusetti1998einstein}, and Ozuch's Einstein desingularization work \cite{ozuch2020higher,ozuch2021integrability}. None by itself supplies WFL.

Independent support:
- route generation: `trace/ttcs/results/step92_ttcs01_generator1_integration.md`;
- cap theorem verification: `trace/ttcs/results/step92_ttcs01_verifier1_integration.md`.
