# Spirit follow-up to Step 72: scalar supply closes the paired-A1 orbifold branch

This is a proposed dependent corollary for Core to verify and communicate to A02. It combines the actual proofs of A02 Lemma 86.S and Theorem 87.O with the inherited all-metric scalar bound on a smooth general-type blow-up. It does not require an orbifold Seiberg-Witten theorem.

## 1. Transfer the scalar bound to every orbifold metric

Let X be a compact complex-hyperbolic surface in its complex orientation, A=c1^2(X)>0, and

    V_m = X # m(S4/Z2),   k=2m.

Use the established orientation-matched resolution topology M=X#k CPbar2. For any smooth orbifold metric g on V_m, insert scaled Eguchi-Hanson metrics at all 2m singularities. Lemma 86.S proves convergence of the scalar energy, not just continuity of the normalized defect:

    S(g_epsilon) -> S_orb(g),   P(g_epsilon) -> P_orb(g).

Every resulting smooth metric on M satisfies the inherited bound

    S(g_epsilon) >= 32 pi^2 A.

Thus every orbifold metric on V_m satisfies S_orb(g)>=32 pi^2 A. The implication also holds for a hypothetical Ricci-flat orbifold, since scalar-energy convergence does not require R(g)>0; that restriction is needed only for continuity of the normalized quotient.

## 2. A sharp all-orbifold P floor

Theorem 87.O is over ALL metrics on this fixed orbifold topology, not only metrics made by additive connected sum. It gives

    chi_orb = A/3-m,  tau_orb = A/9,
    W := integral (|W+|^2+|W-|^2) >= 4 pi^2 A/3.

The orbifold Chern-Gauss-Bonnet identity, with the same operator norm convention as the Session, is

    P = S/12 + 2W -16 pi^2 chi_orb.

Therefore

    P_orb(g) >= 16 pi^2 m = 8 pi^2 k.                  (1)

More precisely, writing sigma=S-32 pi^2 A>=0 and w=W-4 pi^2 A/3>=0,

    P = 8 pi^2 k + sigma/12 + 2w,
    R = P+S/4 = 8 pi^2(A+k)+sigma/3+2w.               (2)

In particular V_m admits NO Einstein orbifold metric for m>=1, at any scalar sign. This closes the small-k part of this specific architecture as well as the k/A>=1/3 range. The weaker condition k<A/3 previously extracted from positive deficit overlooked the scalar supply inherited from its smooth resolution.

The same argument can be phrased as deficit comparison. Put d=S/24-P/2. A hypothetical Einstein bulk needs

    d=S/24 >= 4 pi^2 A/3,

whereas Theorem 87.O says d<=4 pi^2(A/3-k). These are incompatible for k>0.

## 3. Normalized lower bound without dividing a P floor by an uncontrolled R

From (2), 4P/R is a convex combination of

    4k/(A+k),  1,  4

with respective nonnegative denominator weights 8 pi^2(A+k), sigma/3, and 2w. Since the original defect E(g) is at least 4P/R,

    E_orb(g) >= min{1, 4k/(A+k)}.                     (3)

This is a genuine normalized all-metric lower bound on V_m, unlike dividing (1) by an unknown Ricci energy.

## 4. A matching actual upper construction to check

A short construction should make both (1) and (3) sharp as infima. On the round orbifold O=S4/Z2, choose a regular point p and a positive Green function for its conformal Laplacian. The conformal metric on O minus p is scalar-flat, conformally flat, and has one ordinary AE end, while retaining the two A1 singularities. Its lift to S4 minus the two preimages of p is the conformally-flat two-ended scalar-flat neck. Orbifold Gauss-Bonnet gives

    chi_orb(O minus p)=0,
    0 = -P/(16 pi^2) + 1,
    P=16 pi^2.

Here 1 is the AE end correction; both interior A1 contributions are already included in chi_orb. The end has O(r^-2) metric decay with derivatives, sufficient for standard shrinking insertion at a smooth point of X. Its scalar energy is zero and its Weyl energy is zero. Inserting m disjoint scaled copies, including all cutoff annuli, should give

    S -> 32 pi^2 A,   W -> 4 pi^2 A/3,
    P -> 16 pi^2 m,   V -> V_CH,   integral s -> integral s_CH.

Hence E -> 4k/(A+k). The long round cylinder construction at a regular point of any orbifold supplies E->1. This yields the candidate exact values

    inf_orb P(V_m) = 8 pi^2 k,
    alpha_orb(V_m) = min{1,4k/(A+k)}.

Core should verify the Green-function/end normalization and all gluing details before adopting these equalities. The lower bounds and Einstein exclusion in sections 1--3 do not depend on this upper construction. No attainment or nonattainment statement is claimed.

## 5. Consequence for minimizer configurations, not all smooth metrics

The established smooth Burns/kernel constructions give

    P_*(X#k CPbar2) < 8 pi^2 k

for fixed k>=1 in this category. Thus an energy-equality minimizing configuration with bulk topology V_m and Ricci-flat ALE bubbles cannot realize the smooth P infimum: the orbifold bulk alone costs at least 8 pi^2 k. Positive-P bubbles would only increase the discrepancy. This excludes this particular degeneration architecture from the relevant attainment alternatives, provided the actual configuration has the stated topology and energy equality.

There is no contradiction with the smooth sub-unit tariff. Resolution transfers each orbifold metric to a restricted family of smooth competitors. It does not transfer an orbifold lower bound to all smooth metrics. The strict difference between the two infima records the importance of finite-scale, topology-compatible relaxation already established by the cell constructions.

## 6. Better target for other orbifold topologies

For ANY candidate orbifold V with an orientation-matched Ricci-flat ALE resolution or smoothing equal to the target general-type blow-up, scalar transfer requires

    S_orb(g) >= 32 pi^2 A.

If its deficit upper bound is d_max, then

    P_orb(g) >= (8 pi^2 A/3) - 2 d_max.

An Einstein bulk must have d_max >= 4 pi^2 A/3, not merely d_max>0. Signature supplies the necessary condition

    2 chi_orb(V) - 3 |tau_orb(V)| >= A/3,

using the orbifold signature including its correct link corrections. This does not settle candidates that pass it, but it identifies a genuine necessary global condition before searching for metrics.

A non-Kähler or non-additively constructed metric cannot beat the signature ceiling on the already fixed V_m. Any remaining orbifold route must change the actual orbifold topology, link data, or the degeneration mechanism. ALE filling availability, scalar transfer, smooth resolution type, zero infimum and smooth Einstein existence must remain separate claims.
