# Spirit follow-up to Step 73: transfer the mixed field inequality, retaining bubble chirality

This is a proposed dependent extension for Core verification. It does not replace completion of the paired-A1 theorem and Green-cap upper construction. Its purpose is to strengthen the upcoming survivor analysis before that analysis is based only on scalar supply.

## 1. Smooth supplier and the limit being used

Assume the smooth target M=X#k CPbar2 has, for every recovery metric g_epsilon, an actual class a_epsilon with (a_epsilon^+)^2>=A and the mixed estimate

    integral_M (s-sqrt(6)|W+|)^2 >=72 pi^2 A.             (1)

The class may depend on the recovery metric. Its convergence to an orbifold class is unnecessary. Retain the b-plus/chamber or conformal-supply hypotheses under which (1) holds. The primary estimate is LeBrun, Proposition 3.8, read in
`Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md`, lines 290--301. The general-type uniform budget A and chamber treatment are inherited corpus inputs.

Let a compact orbifold (V,g) have orientation-matched scalar-flat ALE fillers (N_j,h_j), with finite curvature energy and adequate decay for the standard cutoff recovery. Put

    B+ = sum_j integral_Nj |W+|^2.

Besides scalar-energy convergence, these insertions have

    I+(g_epsilon) -> I+_orb(g)+B+,
    integral s_epsilon |W+_epsilon| -> integral_V s |W+|.

The cross term from the cores and transition annuli vanishes by Cauchy--Schwarz: their scalar L2 energy tends to zero and their Weyl L2 energy remains bounded. The scaled filler scalar curvature is exactly zero. Weyl tails and cutoff-annulus contributions are controlled by the same scaled C2 estimates as the existing recovery lemma.

Consequently (1) gives the bulk inequality

    integral_V (s-sqrt(6)|W+|)^2 + 6 B+ >=72 pi^2 A.      (2)

There is no orbifold monopole-supply assumption. There IS a bubble chirality term; omitting it without proving B+=0 would make the statement false in that scope.

## 2. Ricci-flat specialization in the existing charge convention

A02 Step-55 defines

    P(N)=4 I+(N)+S(N)/12+8 pi^2 c+(N).

For a Ricci-flat filling, P=S=0, hence

    I+(N)=-2 pi^2 c+(N),  c+(N)<=0.

With C+=sum c+(N_j), (2) becomes

    integral_V (s-sqrt(6)|W+|)^2 >=72 pi^2 A+12 pi^2 C+. (3)

For the standard complex orientation of Kronheimer and hyperkahler-quotient fillings, c+=0, so the full mixed estimate transfers without loss. For another orientation or a more general filler, retain (2) or (3) as appropriate.

## 3. A stronger necessary condition for an Einstein orbifold bulk

Suppose g is Einstein and its Ricci-flat ALE recovery is the stated negative-Yamabe target. Then s is constant and negative. Define

    T+ = (2 chi+3 tau)_orb,
    T- = (2 chi-3 tau)_orb,
    x = S_orb/(96 pi^2).

Einstein Chern--Weil gives

    I+ = 2 pi^2(T+ - x),
    I- = 2 pi^2(T- - x).

Scalar transfer and positivity require

    A/3 <= x <= min(T+,T-).                              (4)

For constant negative s, Cauchy--Schwarz bounds the left-hand side of (3) above by

    (sqrt(S)+sqrt(6 I+))^2
      =12 pi^2 [sqrt(8x)+sqrt(T+-x)]^2.

Therefore a necessary condition is that some x in (4) satisfy

    [sqrt(8x)+sqrt(T+-x)]^2 >=6A+C+.                     (5)

This test uses both chiral topological quantities and the actual bubble W+ ledger. To screen a configuration, maximize the left-hand side over the interval (4). It is concave and has its unconstrained maximum 9T+ at x=8T+/9; hence evaluation requires only clipping that point to the interval. It is not an optimization over unknown metrics.

For the CH host,

    T+=A-k+C+,  T-=A/3+5k+C-,  C-=sum c-(N_j).

Even ignoring the T- cap, (5) implies

    9T+ >=6A+C+,  or  C+ >=(9k-3A)/8.                  (6)

This is stronger than the scalar-only C+>=k-2A/3 in the relevant positive-k range. Keeping T- may improve it further.

### Useful C+=0 form

In the usual ASD Ricci-flat orientation, C+=0 and T+=A-k. Necessarily k/A<=1/3. Put h=k/A. The smaller root of (5) is

    x_min = A/27 [4-sqrt(1-3h)]^2.

Thus

    T- >= x_min.                                       (7)

For k>0 this is strictly stronger than T->=(A+k)/3. Indeed, with t=sqrt(1-3h)<1,

    x_min-(A+k)/3 = 4A(1-t)^2/27 >0.

A convenient weaker consequence is therefore

    C- > -(14/3) k,   when C+=0 and k>0.                (8)

All these are necessary conditions for an actual Einstein bulk, not construction or compactness theorems.

### Example the scalar-only screen misses

If k=3 and a single correctly oriented Kronheimer A3 filling carries the surgery topology, then (c+,c-)=(0,-15). The scalar-only test permits equality T-=A/3. But T+=A-3<A, so x=A/3 makes the left side of (5) strictly smaller than 6A. This candidate bulk is excluded whenever the asserted smooth recovery topology and supplier are established. The same stronger screen can be applied to the other actual low-rank fillings rather than stopping at scalar-charge saturation.

## 4. Do not equate every charge row with a Ricci-flat filling

The file `Sessions/S1003A02/workspace/data/step55_orbifold_bubble_charges.json` was designed to screen more general scalar-flat/P-critical bubble topologies for a small-energy k=1 minimizer. For example:

- its `b2_one_ADE_end_in_M_orientation` E8 row has c+=-7 and assumes b2=1;
- an actual Kronheimer E8 filling instead has b2=8 and c+=0 in its complex orientation.

They are not the same object. Likewise a cyclic row allowed by the linking form or by max(c+,c-)<1 does not establish a Ricci-flat ALE metric with that topology.

For a scalar-flat but non-Ricci-flat filler, (2) still transfers, but B+ is

    sum [P(N_j)/(4) - 2 pi^2 c+(N_j)],

and the total minimizing-sequence energy includes the positive P(N_j). Such fillings cannot be used as zero-cost desingularizations merely because their charge lower bound is zero.

A useful survivor analysis should therefore distinguish:

- known Ricci-flat ALE fillings with the required orientation and smooth recovery;
- topologically admissible fillings whose metric existence is open;
- positive-P scalar-flat fillers, relevant to ideal minimizing configurations with their full cost retained.

This is not extra bookkeeping: it separates a candidate zero-gap construction from a necessary arithmetic condition on a possible degeneration.

## 5. Strategic interpretation

The paired-A1 exact restricted law remains an important result to finish. The general lesson is broader: recovery maps can transfer an entire all-metric curvature inequality from the smooth target to a singular bulk, with explicit bubble contributions. There is no need to invent an orbifold supplier when convergence of the relevant functional already supplies the bound. Use that principle to distinguish genuine global survivors before investing in their construction or a large catalogue.
