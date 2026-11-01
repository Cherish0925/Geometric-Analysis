# Step 92 support — fixed-filler scalar control and lossless abelian field transfer

This note responds to the WFL route in `step92_global_route_selection_wahl_field_cap_charge_and_goldberg.md`. It identifies a shorter analytic entrance for the **prescribed** Ricci-flat ALE filler metrics. It does not assert compactness for arbitrary almost-Einstein sequences, a new Einstein obstruction, or an explicit numerical character for the PPS embedding.

Directly inspected input: A02 `workspace/notes/theorem_package_v1.md`, Lemma 86.S, lines 772–774. Its proof gives pointwise bounded Ricci curvature in the cutoff annulus, not merely convergence of scalar integrals.

## 1. The explicit recovery already has a uniform scalar bound

Fix a compact smooth orbifold metric g, a finite set of isolated quotient points, fixed orientation-matched Ricci-flat ALE fillers, and fixed marked end identifications. On a filler use the metric epsilon^2 h. In orbifold normal coordinates glue at rho=epsilon^{tau/(tau+2)}. The scaled C^2 error on the annulus is

eta = O(rho^2 + (epsilon/rho)^tau).

Consequently

|Ric(g_epsilon)| <= C rho^(-2) eta = O(1).

The equality follows from epsilon^tau=rho^{tau+2}. Inside the scaled filler Ric=0 exactly; outside the annulus the metric is the fixed g. Thus, for this family,

sup_M |s(g_epsilon)| <= C_g

uniformly in epsilon. Full Riemann curvature can still blow up in the ALE core; this does not affect the scalar statement. No Einstein assumption on g is required. Constants need not be uniform as the outer metric, the group order, or the filler itself varies.

For unperturbed monopoles with the normalization used in the Step-92 note, the maximum principle gives

U_epsilon=|Phi_epsilon|^2 <= ||s(g_epsilon)^-||_infinity <= C_g.

For a fixed small outer coordinate radius r and epsilon sufficiently small, the filled ball has volume O(r^4). Therefore

integral_{filled B_r} |Phi_epsilon|^4 <= C_g^2 Vol(filled B_r)=O_g(r^4),

and the same estimate holds for the self-dual determinant-curvature energy, up to the factor 1/8. This directly excludes spinor L^4 concentration and F_A^+ energy concentration at the quotient points. A logarithmic W^{1,4} cutoff is useful for a theorem assuming only scalar L^2 control; it is not needed for the prescribed family and should not become its main bottleneck.

## 2. Nonzero limits without a Hodge-limit prerequisite

Choose an actually supplied fixed smooth spin^c structure, or pass to a fixed subsequence from the finite signed family. The integrated Weitzenbock and Chern–Weil identities give

integral U_epsilon^2 <= integral (s_epsilon^-)^2,

integral |F_A|^2 = 2 integral |F_A^+|^2 - 4 pi^2 a^2,

so both the full determinant curvature and the spinor covariant derivative have uniform L^2 bounds. On fixed compact subsets of the regular part, the metric is eventually g. Abelian gauge compactness and local elliptic bootstrapping then give a smooth subsequential monopole limit modulo gauge. A complete proof still has to specify the gauges and the equivariant removable-singularity step.

Nontriviality does not require first computing the Hodge projection in the singular limit. For a signed class on M=X#k CPbar^2 with a^2=A-k>0,

integral U_epsilon^2 = 8 integral |F_A^+|^2 >= 32 pi^2 (a_epsilon^+)^2 >= 32 pi^2 (A-k)>0.

The preceding uniform bound and vanishing filled-ball volumes prevent this mass from disappearing. If the metricwise sign selection ensures (a_epsilon^+)^2>=A, the stronger lower mass bound 32 pi^2 A also survives. This does not identify the boundary character as zero.

## 3. Abstract lift identification need not wait for a coordinate formula

At a Wahl point, let Gamma=Z_(n^2) act on C^2 with the prescribed marking. Relative to its canonical spin^c lift, local orbifold spin^c structures are indexed by characters of Gamma. Restriction of line twists is the isomorphism

H^2(B Gamma;Z) = Z_(n^2) -> H^2(S^3/Gamma;Z) = Z_(n^2).

The spin^c restriction map is the corresponding affine bijection once a reference lift is fixed. Thus a fixed marked spin^c structure on the complement determines a unique local orbifold lift abstractly. The analytic theorem can retain that lift as res(s); its explicit integer character can be computed from the actual PPS embedding in parallel.

The determinant changes by twice the twist. In particular, when the order is even the determinant character alone need not identify the spin^c lift. Extendibility over the smooth rational ball is a different condition: its line-twist image is n Z_(n^2). Gauge transformations do not freely permute these topological lifts. In proving equivariant removal, the extended deck action must be matched to the fixed punctured-chart structure.

For b^+>1, where the signed smooth family is simultaneously genuinely supplied, this can be done for the finite family on the same recovery metrics. For b^+=1, retain the metricwise selection and actual chamber input rather than asserting simultaneous supply. The analytic part is not special to one k=4 coordinate realization.

## 4. Rational-ball topology gives a stronger consequence after removal

Once the finite-energy limit extends to the orbifold with the prescribed lift, the determinant square is unchanged:

a_V^2 = a_M^2.

Reason: both a rational ball and a cone on a rational homology sphere have no rational H^2; the complement identifies H^2(M;R) with H^2(V;R) and preserves the cup pairing. Local isotropy is torsion and is invisible to this rational pairing, but is retained separately in the spin^c lift.

The uniform spinor bound, regular-part smooth convergence and vanishing filled-ball volumes give

lim integral_M |F_{A_epsilon}^+|^2 = integral_V |F_{A_infinity}^+|^2.

Use Chern–Weil on both closed objects:

lim integral_M |F_{A_epsilon}|^2
= 2 integral_V |F_{A_infinity}^+|^2 - 4 pi^2 a_M^2
= integral_V |F_{A_infinity}|^2.

Thus no determinant-curvature L^2 energy is lost in the Wahl fillers or necks. In particular there is no hidden anti-self-dual **abelian** energy defect; this says nothing analogous about the metric's W^- energy. The same integrated Weitzenbock identity, scalar bound and mass convergence give equality of total spinor-gradient energies. These statements require the extension and class identification; they are not substitutes for proving them. They do not give arbitrary higher-derivative estimates.

This sharper output is useful for future Einstein–field comparisons: the fields and their energy stay on the actual bulk instead of an unidentified gauge bubble. It still does not create a new inequality by itself. The Hodge-defect identity and self-dual Weitzenbock formula in Step 92 hold for any such actual field and need additional control to distinguish an Einstein candidate.

## 5. Strategic use

The WFL idea is worth developing because actual field supply is more informative than transferred scalar estimates. Its analytic entrance is cheaper than the proposed serial programme: use the existing scalar control, establish the field limit with its abstract marked lift, and compute explicit PPS characters independently. The next substantial question is then what class-sensitive relation or relative boundary information distinguishes a hypothetical Einstein metric. A proof of WFL alone is enabling progress, not Q1 nonexistence, a pure Einstein gap, or an exhaustive degeneration theorem.
