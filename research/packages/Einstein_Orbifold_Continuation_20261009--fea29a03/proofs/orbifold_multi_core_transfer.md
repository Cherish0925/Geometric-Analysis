# Monopole supply through several Ricci-flat ALE cores

Date: 2026-10-09. This continues `q3_orbifold_supply_independent.md` and `q2_exact_infimum_new.md`; it does not assume a classification of all minimizing degenerations.

## 1. Statement with the full cohomology budget

Let M be a closed oriented smooth four-manifold. Let C={a_1,...,a_m} be a finite collection of real determinant classes, represented by fixed spin-c structures admitting unperturbed actual Seiberg-Witten solutions for every smooth metric on M. Suppose disjoint compact cores N_i^c of oriented, smooth, Ricci-flat ALE four-manifolds (N_i,g_i) embed in M. Each N_i has one end S^3/Gamma_i and positive ALE order with two differentiated estimates. Replace these cores by their flat quotient cones; denote the resulting compact smooth orbifold by O. The quotient structures and gluing markings are fixed.

Real cohomology splits orthogonally:

    H^2(M;R) = H^2_orb(O;R) direct-sum (direct-sum_i H^2(N_i;R)).

Write a=(a_0;a_1,...,a_r) in this splitting, using a superscript or descriptive subscript when needed to distinguish a supplied class from a core index. For v in Conv(C), define

    B_O = max_{v in Conv(C)} v_0^2
        = max_{v in Conv(C)} [v^2 - sum_i v_i^2],

and assume B_O>0. Define the oriented core contribution

    D_i = (1/(2 pi^2)) integral_{N_i} |W^+_{g_i}|^2 >= 0.

Then every smooth orbifold metric g on O satisfies

    P_orb(g) >= 8 pi^2 [ (2/3) B_O - T(M) + sum_i D_i ],       (1)

where T(M)=2 chi(M)+3 tau(M), and P=integral |Ric^0|^2. A negative right side is of course replaced by the elementary lower bound zero.

There is an additional supply restriction, not a hypothesis of the theorem:

    v_i^2 <= 0 for every v in span_R(C), for every i.           (2)

More precisely, the restriction of this entire span to N_i lies in its L^2 anti-self-dual harmonic cohomology for g_i. Thus

    B_O >= max_{v in Conv(C)} v^2.                             (3)

This statement allows positive, negative or indefinite core intersection forms; only the restrictions of supplied classes are forced into the negative space. In particular, a positive-definite Ricci-flat ALE core can carry no nonzero real restriction of any supplied class.

## 2. Scalar-controlled desingularization for arbitrary ALE order

Fix an arbitrary smooth orbifold metric g on O. In each orbifold normal chart,

    g = delta + O(r^2),
    partial^j(g-delta) = O(r^{2-j}), j<=2.

If the ALE decay order is nu>0, the metric a^2 g_i in physical end coordinates has error h_a satisfying

    partial^j h_a = O(a^nu r^{-nu-j}), j<=2.

Choose r_a=a^q with 0<q<=nu/(nu+2). A fixed radial cutoff between these two metrics on r_a<r<2r_a gives

    |Rm| <= C [1+a^nu r_a^{-nu-2}
                   +(r_a+a^nu r_a^{-nu-1})^2] <= C.

The constants may depend on the fixed orbifold metric and the finitely many ALE metrics. They do not depend on a. The inner regions are Ricci-flat, and the outer metric is fixed. Consequently:

* the scalar curvature has a uniform lower bound;
* the total volumes remain bounded;
* the curvature energy of every gluing annulus tends to zero;
* P(g_a) tends to P_orb(g);
* on each rescaled core the metrics exhaust (N_i,g_i).

No Einstein desingularization theorem is being invoked: these are smooth competitors obtained by direct metric interpolation. There is no required compatibility between the orbifold curvature operator and a Ricci-flat core beyond the fixed quotient chart.

## 3. Actual fields on the bulk and on the cores

For every a_l in C choose an actual solution on each g_a. The scalar lower bound gives a uniform pointwise spinor bound, hence a uniform pointwise bound on F_A^+. The volume bound and the topological identity

    integral (|F_A^+|^2-|F_A^-|^2) = 4 pi^2 a_l^2

give a uniform global L^2 determinant-curvature bound. The integrated spinor identity also bounds the covariant-gradient energy.

On compact subsets of O_reg, abelian gauge compactness and the equations give smooth subsequential limits. Isolated points are removable after lifting to the smooth covering ball. The extended fields retain their finite isotropy representation; trivial determinant holonomy is neither assumed nor needed. There are finitely many classes and cores, so one diagonal subsequence suffices. The real limiting classes are precisely (a_l)_0.

This construction works for each arbitrary orbifold metric, so it supplies all the real classes (a_l)_0 for every orbifold metric, including all conformal representatives needed for the classical mixed curvature estimate.

Now inspect an individual rescaled core. Its curvature two-form is unchanged as a differential form under scaling, but

    |F_A^+|_{g_i} <= C a^2 -> 0

on every fixed compact core subset. Its L^2 norm is uniformly bounded, because curvature L^2 is scale invariant in four dimensions. Extract a weak L^2 limit F_i. Distributionally dF_i=0 and F_i^+=0, hence F_i is a smooth anti-self-dual harmonic two-form. Pairing the prelimit curvatures against compactly supported closed two-forms shows that

    [F_i/(2 pi i)] = (a_l)_i.

This pairing, rather than unsupported convergence of pointwise periods, is sufficient. On a one-ended ALE four-manifold with rational-homology-sphere link, middle-degree L^2 Hodge cohomology is the image of H_c^2 in H^2, and this map is an isomorphism. Its intersection pairing is integration of the L^2 harmonic representatives. Therefore

    (a_l)_i^2 = - ||F_i||_2^2/(4 pi^2) <= 0.

More importantly, limits for all the finitely many a_l are anti-self-dual for the SAME fixed core metric. Any real linear combination is again anti-self-dual. Thus (2) holds on the entire span, not merely on individual supplied classes. This is what makes the convex-hull conclusion (3) legitimate.

The L^2 Hodge identification used here is standard ALE Hodge theory, included in Hausel-Hunsicker-Mazzeo. The compactness/removability and the curvature inequality below are classical analytic inputs. The new assembly in this continuation is their use for the full multi-core projection budget and orientation-dependent obstruction.

## 4. Exact curvature correction

Define the orbifold curvature characteristic quantities by

    chi_curv(O) = (1/(8 pi^2)) integral_O
       (|W^+|^2+|W^-|^2+s^2/24-|Ric^0|^2/2),

    tau_curv(O) = (1/(12 pi^2)) integral_O (|W^+|^2-|W^-|^2).

They are not both the characteristic numbers of the underlying topological space. In particular, tau_curv is not the signature of its real intersection form.

For a Ricci-flat ALE core let

    e_i = chi(N_i)-1/|Gamma_i|
        = (1/(8 pi^2)) integral_{N_i} (|W^+|^2+|W^-|^2),

    t_i = (1/(12 pi^2)) integral_{N_i} (|W^+|^2-|W^-|^2).

Apply closed Chern-Weil to the explicit desingularizations from Section 2 and pass to the limit. Their annuli have vanishing curvature energy, giving

    chi_curv(O)=chi(M)-sum_i e_i,
    tau_curv(O)=tau(M)-sum_i t_i.

Hence, exactly,

    T_curv(O) = T(M)-sum_i (2e_i+3t_i)
              = T(M)-sum_i D_i.                              (4)

This derivation retains the orientation automatically and does not require a choice of convention for the signature eta invariant. Reversing a core exchanges W^+ and W^- and generally changes D_i.

## 5. Classical inequality plus the preserved convex budget

For any smooth orbifold metric, convexity of squared norm on H_g^+ gives

    max_{a in C} |(a_0)^+|^2 >= |(v_0)^+|^2 >= v_0^2

for each v in Conv(C). Thus some supplied actual class has self-dual square at least B_O. The orbifold version of the classical LeBrun mixed estimate gives

    integral_O (s-sqrt(6)|W^+|)^2 >= 72 pi^2 B_O.

Weighted Cauchy-Schwarz, with 24+6/2=27, then gives

    integral_O (s^2/24+2|W^+|^2) >= (8 pi^2/3) B_O.

Since

    4 pi^2 T_curv(O)
       = integral_O (s^2/24+2|W^+|^2) - P_orb/2,

we obtain (1) using (4). The orbifold version uses the usual invariant-chart Weitzenbock and conformal argument; the actual supply is available for every orbifold metric by Section 3.

## 6. Multi-bubble exclusions on blow-ups

Suppose M=X#k CPbar^2 has all supplied sign classes

    K + sum_j epsilon_j E_j,
    K^2=A>0, E_i.E_j=-delta_ij, K.E_i=0,

and T(M)=A-k. The average of these classes is K. Set

    Delta_K = -sum_i (K_i)^2 >= 0.

Then B_O>=K_0^2=A+Delta_K, and (1) implies

    P_orb >= 8 pi^2 [k-A/3 + sum_i D_i + (2/3)Delta_K].       (5)

Consequently, a sequence with limsup P<8 pi^2 k cannot converge smoothly on regular compact subsets to a smooth compact orbifold of this specified topological type if

    sum_i D_i + (2/3)Delta_K >= A/3.                         (6)

Only nonnegative energy lower semicontinuity is needed to compare P_orb with liminf P; no neck energy equality is required.

For the orientation reversal of a Ricci-flat ASD rational homology ball,

    D_i=4(1-1/|Gamma_i|),   Delta_K=0 on this core.

For Wright's cyclic rational-ball quotients, |Gamma_i|=d_i^2 with d_i>=2. Thus r such reversed rational balls are excluded by

    A <= 12 sum_{i=1}^r (1-d_i^{-2}).                        (7)

In particular A<=9r suffices. For one reversed Eguchi-Hanson quotient, d=2 and (7) reduces to A<=9, recovering the earlier single-core result. Larger end groups yield a stronger threshold approaching 12 per reversed rational ball.

For a general Ricci-flat core the exact D_i in (5) applies without a half-conformal-flatness classification. Positive D_i and nonzero K_i may both strengthen the orbifold obstruction.

## 7. Exactly what remains invisible

An ASD Ricci-flat rational homology ball in the original orientation has

    W^+=0, H^2(N_i;R)=0, D_i=0, Delta_K=0.

Its replacement changes neither this T_curv budget nor the real projected class budget. Therefore the general transfer theorem gives no improvement over the original classical inequality for that branch. This is an exact cancellation, not a missing constant in the estimate. It does not assert that such an oriented core embeds in every proposed M.

Likewise an ASD core with nonzero H^2 but K_i=0 can remain invisible to the K budget. Other supplied convex combinations may still detect it through the full B_O. Thus the complete budget B_O should be retained rather than discarding all actual classes in favor of their average.

The theorem does not produce a compact orbifold limit for arbitrary minimizing sequences, does not classify Ricci-flat ALE spaces, and does not exclude collapse. It supplies a metric-independent obstruction for every finite specified Ricci-flat ALE replacement. Resolving all four project questions requires additional information beyond this result.

## Sources for the classical components

* Claude LeBrun, Ricci Curvature, Minimal Volumes, and Seiberg-Witten Theory, arXiv:math/0003068, https://arxiv.org/abs/math/0003068 . Mixed curvature bound and Chern-Weil consequence.
* Claude LeBrun, Four-Manifolds, Curvature Bounds, and Convex Geometry, arXiv:math/0611450, https://arxiv.org/abs/math/0611450 . Convex-hull formulation.
* Claude LeBrun, Edges, Orbifolds, and Seiberg-Witten Theory, arXiv:1305.1960, https://arxiv.org/abs/1305.1960 . Orbifold analytic framework; its original application has codimension-two singularities, while invariant-chart local estimates used here apply to isolated quotient points as well.
* Tamas Hausel, Eugenie Hunsicker, Rafe Mazzeo, Hodge cohomology of gravitational instantons, arXiv:math/0207169, Duke Math. J. 122 (2004), 485-548, https://arxiv.org/abs/math/0207169 . ALE L^2 Hodge theory and the intersection pairing.
* Evan P. Wright, Quotients of gravitational instantons, arXiv:1102.2442, https://arxiv.org/abs/1102.2442 . The cyclic rational-ball identification used only in (7), not in the general theorem.
