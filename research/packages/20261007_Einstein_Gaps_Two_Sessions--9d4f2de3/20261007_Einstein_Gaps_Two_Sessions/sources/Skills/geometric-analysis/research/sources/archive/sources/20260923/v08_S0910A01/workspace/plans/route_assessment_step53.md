# Route assessment after Step 53

## 0. Governing target

The active problem remains Yau Problem 26 in its displayed form: for every dimension \(n\ge2\), decide whether there are dimension-only constants \(c_n<C_n\) such that every closed connected smooth \(n\)-manifold carrying a metric with
\[
 c_ng\le \operatorname{Ric}_g\le C_ng
\]
also carries some smooth Einstein metric, with no sign or proximity condition on the output metric.  The current session still has no full proof, no refutation, and no Lean formalization.  The material below is route control for the strongest active four-dimensional fronts.

## 1. Product-quotient front: bounded §6.9 test

Step 52's Lefschetz scan made the next deformation question sharper: nonzero
\[
 d=\dim H^2(X,T_X^0)=\dim H^0(C_1\times C_2,\Omega^1\otimes K)^G
\]
only means the strong Lee--Park sufficient condition \(H^2(X,T_X^0)=0\) fails.  It does not rule out local smoothing parameters globalizing.

The Strategist suggested testing the smallest nonzero case, BCGP §6.9, rather than sweeping more rows.  I wrote and ran:

- `workspace/scripts/step53_s69_nodes_exact_boundary.py`
- `workspace/data/step53_s69_nodes_exact_boundary.json`
- `workspace/scripts/step53_s69_symmetry_probe.py`
- `workspace/data/step53_s69_symmetry_probe.json`

### 1.1 Exact obstruction dimension

Using exact arithmetic in \(\mathbb Q(\zeta_{60})\), the §6.9 calculation gives
\[
 d_{21}=1,
 \qquad d_{12}=1,
 \qquad d=2.
\]
The stored coefficient vector for the total is `[2,0,...,0]`, so this rechecks the Step 52 floating computation without numerical roots of unity.

### 1.2 Node orbits

BCGP lines 169--171 and 347 state that in this RDP product-quotient classification the number of nodes is \(8-K^2\).  For §6.9, \(K^2=4\), hence four \(A_1\) nodes.

The script reconstructs them from branch stabilizers:

- 240 candidate product fixed pairs before dividing by the diagonal \(S_5\)-action;
- four diagonal orbits, each of size 60;
- all nodes lie over the order-2 branch value of \(C_1/G\);
- two nodes lie over branch value #2 of \(C_2/G\) (order 6) and two over branch value #3 of \(C_2/G\) (order 6).

Thus the local-to-global map has the form
\[
 \beta:\mathbb C^4\longrightarrow H^2(X,T_X^0),\qquad \dim H^2=2,
\]
so
\[
 \dim\ker\beta\ge2.
\]
There are genuine first-order global deformation directions with some nonzero local smoothing data.  A full-support first-order direction exists exactly when \(\ker\beta\) is not contained in the union of the four coordinate hyperplanes.  Dimension counting alone does not decide this.

### 1.3 Symmetry shortcut not available from the presentation

The strict presentation-compatible inner normalizer probe for §6.9 is trivial:

- the only inner automorphism preserving the \(C_1\) branch values with distinct orders \((2,4,5)\), while preserving the order-3 \(C_2\) value and allowing the two order-6 values to exchange, is the identity;
- the induced node action is the identity.

This is **not** a proof that \(\operatorname{Aut}(X)\) is intransitive, because the probe covers only inner automorphisms visible in the displayed \(S_5\) quotient presentation.  It does show that the simple transitivity argument cannot be invoked from the available quotient data.  If this front is pursued, the next mathematical object is the actual boundary map \(\beta\), or dually the residue/evaluation map
\[
 H^0(Y,\Omega^1_Y\otimes K_Y)^G \longrightarrow \bigoplus_{p\in\mathrm{nodes}} T^1_p{}^\vee.
\]

### 1.4 Route value

This front is now bounded.  It clarifies the relation between local approximate Einstein gluing and global complex smoothing, but it should not absorb major effort unless the explicit \(\beta\)-map can be computed efficiently and linked to either a Q-Gorenstein smoothing theorem or the mixed-chirality approximate-metric construction.  The established BCGP §6.7 Einstein-existence theorem remains the durable product-quotient result.

## 2. Direct transported-cutoff flow: status after A03 Step56 and TTCS

A03 Step55 introduced the right variables for an exact cutoff flow:
\[
\partial_tG=-2\beta^2(\operatorname{Ric}_G+G)+\mathcal L_{\beta^2W(G)}G,
\qquad
\partial_t\beta=\beta^2W(G)\cdot D\beta.
\]
With the ODE
\[
\partial_t\varphi=-\beta(t,\varphi)^2W(G)(t,\varphi),
\]
one obtains \(\beta(t,\varphi(t,x))=\chi(x)\) and therefore
\[
 g(t)=\varphi(t)^*G(t),\qquad
 \partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
\]
TTCS confirmed this transported-cutoff identity.

The original Step55 proof was not certified: its arbitrary-order estimate falsely bounded high coefficient derivatives by a fixed low energy.  A03 Step56 repairs the architecture using:

- a doubly regularized system with metric coefficient \(\beta^2+\varepsilon\) and scalar viscosity \(\nu\bar\Delta\beta\);
- a genuine tame product estimate at order \(m\), retaining high coefficient derivatives linearly in \(E_m\);
- a low-order stopping-time bootstrap on a per-datum interval;
- all higher orders on the same per-datum interval;
- smooth \((\varepsilon,\nu)\to(0,0)\) compactness and pullback.

TTCS Step53 second verification (`trace/ttcs/results/step53_ttcs02_verifier1_integration.md`) judges this repair mathematically credible as a per-datum existence module, after standard tame and fixed-parameter parabolic details are written.  It also verifies the patched Liouville averaging in Step45: rewriting the upper bound on the exponential-pullback average as an integral over the unit tangent bundle and using geodesic-flow preservation of Liouville measure removes the collapse multiplicity issue.  No injectivity-radius or uniform multiplicity assumption is needed for the upper bound.

### 2.1 Correct scope

The direct flow gives, at best, a **per-datum** smooth branch.  It does not by itself give a sequence-uniform lifespan in a collapsing Ishida--LeBrun family, because curvature/volume budgets do not control fixed-background high Sobolev norms or higher cutoff jets.

The correct interface is:

1. start each datum for its own positive time;
2. run first-exit estimates using only uniform low-order geometric inputs;
3. if a branch threatened to stop before \(\theta r^2\), use positive-time weighted/unweighted continuation to obtain a smooth endpoint and restart;
4. thereby reach the common observation time without requiring uniform initial \(H^s\) bounds.

### 2.2 Remaining analytic load

The restricted Ishida--LeBrun theorem is still not end-to-end complete.  The next load-bearing module is the first-exit/continuation chain on the exact flow:

- prove the unweighted critical curvature energy
  \[
  H_2^\alpha=\int\eta_\alpha^2F_T^2
  \]
  and the \(H_q,Y,J_6\) estimates with constants independent of uncontrolled high cutoff jets;
- handle
  \[
  \nabla^2a=2\,d\chi\otimes d\chi+2\chi\nabla^2\chi
  \]
  by the signed integration-by-parts mechanism rather than assuming pointwise second-cutoff control;
- prove the defect Moser endpoint
  \[
  \|aE(t)\|_\infty\lesssim \delta(r^2/t)^{1/3}
  \]
  and curvature endpoint
  \[
  \|aF_T(t)\|_\infty\lesssim \gamma/t;
  \]
- propagate global defect correctly as
  \[
  Q_{\rm global}(t)=Q_{\rm rest}(0)+\sum_\alpha Q_\alpha(t);
  \]
- prove positive-time continuation from weighted curvature to unweighted collar/high-jet control via the staggered hierarchy
  \[
  T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to\cdots;
  \]
- fix one support-radius convention and ensure the terminal pullback ball stays inside the bounded-curvature plateau.

This analytic module is presently the most consequential near-term route, because completing it would convert the accumulated Seiberg--Witten/Weyl/Derdziński calibration structure into a genuine restricted four-dimensional negative pinching theorem.

## 3. Mixed/reversed product wall after A02 Step57

A02 Step57 gives an important route-control theorem for the genus-two mirror wall \((\Sigma_2\times\Sigma_2)/\langle\iota\times\iota\rangle\): for \(1\le r\le35\), the sign-pattern fillings are simply connected, strict Hitchin--Thorpe, and not Kähler/symplectic in either orientation.

The mechanism is:

- a reversed filling inserts a non-torsion \(+2\)-sphere;
- with \(b_+>1\), adjunction contradicts any nonzero ordinary Seiberg--Witten basic class;
- Taubes would give such a class for symplectic/Kähler structures;
- the same argument applies after orientation reversal because the complementary fillings become \(+2\)-spheres there;
- van Kampen keeps all sign-pattern fillings simply connected, so simplicial-volume and BCG/Sambusetti obstructions are vacuous.

This does **not** prove Einstein nonexistence.  It says something sharper about the hard region: compatible bubbling is holomorphic and lands in known Einstein manifolds, whereas reversed bubbling voids both the known Kähler-existence machines and the known SW/entropy obstruction machines.  The live mixed rows therefore expose the dimension-four noncollapsed Yau-26 problem as at least as hard as Einstein existence/nonexistence for simply connected \(b_+\ge2\) manifolds with no monopole classes.

The approximate-metric side of this wall remains conditional on the Biquard/Ozuch multi-bubble estimate and disjoint noninteraction.  Biquard 2013 §14 is still unretrieved in the group record.  This front is valuable, but it lacks an all-sign Einstein obstruction and should not replace the IL analytic work as the main immediate proof target.

## 4. Current route judgment

The active fronts now have different roles:

1. **Restricted IL negative branch.**  Most developed proof architecture; direct flow start is now credible but first-exit/continuation remains load-bearing.  This is the best near-term target for a rigorous new theorem, though still far from the full dimension-only proposition.
2. **Product-quotient/Campedelli existence.**  Solid existence control: §6.7 BCGP carries a negative Einstein metric; §6.9 has first-order smoothing directions but no transitivity shortcut.  This prevents false counterexamples and gives deformation tools, but is not currently a global forcing route.
3. **Entropy/degree.**  Fixed-target and target-dependent negative gaps; no dimension-only uniformity over varying topology.
4. **Mixed/reversed wall.**  Reveals a genuinely hard non-Kähler simply connected region; currently no Einstein obstruction and approximate metric estimate source still incomplete.
5. **Positive and higher-dimensional branches.**  Still have no analogue of the 4D SW/Weyl/Derdziński or BCG-CGB mechanisms.

The next step should not continue product-quotient table scanning.  The most valuable next mathematical work is to have a Constructor or Critical Reviewer rebuild the first-exit/continuation module on the exact Step56 flow, using the TTCS corrections as the map of the real analytic gaps.  If that module closes, the restricted IL theorem becomes a serious proved result and a platform for judging whether its ideas can be generalized beyond the current geography.  If it fails, the failure should identify the precise missing estimate, which is equally important for choosing between IL, mixed-wall, entropy, or new routes.
