# Spirit follow-up to Step 74: variational nonattainment and an aspherical root restriction

These are proposed dependent consequences for Core verification. They use the full all-orbifold scalar bound from Theorem 74.A and the actual topology of the compact ball-quotient host. They do not settle unrestricted smooth Einstein existence, smooth P attainment, or the existence of a compact Einstein orbifold for a remaining topology.

## 1. Nonattainment of the paired-A1 P infimum

The Step-74 equality discussion correctly distinguishes equality in the displayed inequalities from criticality. It is true that the equalities alone initially give only

    S=32 pi^2 A,  W-=0,  s<=0,  |W+|^2=s^2/24.

But an actual global P-minimizer would also attain the ALL-METRIC scalar lower bound S>=32 pi^2 A. Therefore it is a critical point of S(g)=integral s_g^2 with respect to every orbifold-smooth variation.

In dimension four take g_t=exp(2t phi)g, with Delta=div grad. Then

    dS/dt at 0 = -12 integral phi Delta s.

Thus Delta s=0. On a compact orbifold with isolated finite-quotient singularities and an orbifold-smooth metric, integration by parts is legitimate (or work equivariantly in uniformizing charts), so s is constant. Since S=32 pi^2 A>0, this constant is nonzero.

For a trace-free variation h, with s constant,

    DS_g[h] = -2s integral <Ric^circ,h>.

It follows that Ric^circ=0 on the regular part and, by orbifold smoothness, everywhere. This contradicts P=8 pi^2 k>0 for k=2m>0.

Hence, under Theorem 74.A's scalar-supply and resolution hypotheses,

    inf_orb P(V_m)=8 pi^2 k is NOT attained for any m>=1.

No Derdzinski classification, Kähler eigenstructure, or orbifold equality case of Seiberg-Witten theory is needed. Equivalently, W-=0 makes the metric Bach-flat, and a nonzero-scalar P-critical Bach-flat metric is Einstein; the scalar-minimum proof is shorter and uses fewer facts.

### Consequences for the normalized defect

For k<A/3, equality in the convex-combination bound forces sigma=w=0 and L_s=0, hence P=8 pi^2k. Therefore alpha_orb is not attained below the wall either.

For k>A/3, Step 74 already proved strict pointwise E>1, so alpha_orb=1 is not attained.

The wall k=A/3 is different. Equality E=1 forces w=0 and L_s=0 but allows sigma>0. Thus attainment there is precisely existence of an orbifold-smooth self-dual metric with nonzero constant scalar curvature (negative by scalar supply), on the given orbifold topology. This argument neither constructs nor excludes such a metric. It is the only remaining normalized-attainment question within this family.

This corrects the strategic implication of the earlier statement 'constant s is not forced for a P-minimizer': constant s is not forced by the norm equalities alone, but it IS forced by minimizing the unconstrained scalar functional. The step should be closed rather than treated as an open search for nonconstant-scalar extremals.

## 2. Spherical classes on a blow-up of an aspherical host

Let X be a compact ball quotient, M=X#k CPbar2, and b:M->X the degree-one blowdown/collapse map. Since X is aspherical, pi2(X)=0. For any sphere map f:S2->M, b composed with f is null-homotopic. Consequently

    b_*[f(S2)]=0 in H2(X;Z).

The kernel of b_* on H2 is exactly the exceptional summand with form -I_k. Every embedded (-2)-sphere therefore has class

    a=sum_i a_i E_i,   sum_i a_i^2=2,

so its free integral class is necessarily

    a= +/-E_i +/-E_j,   i!=j.

This is the D_k root set in the negative diagonal lattice. No Seiberg-Witten adjunction inequality for negative self-intersection is required. Such an inequality, if imported naively, would conflict with the already realized E_i+E_j and E_i-E_j spheres in the paired-EH resolution.

The conclusion applies to ALL embedded spheres, not only holomorphic or symplectic spheres, on this smooth M. It does not automatically apply to nonaspherical general-type hosts or to a different smooth manifold merely homeomorphic to M.

## 3. Consequences for actual Kronheimer plumbings

The compact exceptional set in a Kronheimer ALE filling is a negative ADE plumbing of embedded (-2)-spheres. If its compact truncation embeds in M, the sphere lattice embeds isometrically into -I_k. This follows without a primitivity assumption: the intersection matrix is nonsingular, so the sphere classes remain independent in H2(M).

The root-subsystem restriction can be proved directly by signed support graphs. Each root is e_i-e_j or e_i+e_j after changing overall signs. In a connected coordinate-support component, change coordinate signs so that a spanning tree uses only differences. Reflections in the tree roots generate all differences on its v vertices.

- If every remaining edge is also a difference, the generated root system is A_{v-1}, with rank v-1.
- If an additional plus edge occurs, reflections generate all +/-e_i +/-e_j, giving D_v of rank v. The small coincidences are D_2=A_1+A_1 and D_3=A_3.

Thus a root system contained in the D_k roots has only A and D components, never E6, E7 or E8. A Core proof should spell out the signed-graph/reflection argument or cite the standard root-subsystem classification; the mechanism is elementary and tied to the actual sphere classes.

In particular:

- E6, E7, E8 Kronheimer plumbings cannot embed in X#k CPbar2 for ANY k when X is aspherical.
- A_r with r>=4 requires at least r+1 coordinate directions; it cannot be the single rank-k plumbing carrying all k exceptional directions when k=r. (A3 has the D3 exception.)
- D_r can occupy r coordinates. The genuine D_r candidates surviving the mixed budget at sufficiently large A are not removed by this argument.
- If a collection of ADE sphere lattices spans the entire exceptional Q^k, every connected coordinate-support component must have full rank. Hence only D_v-type components can occur, including D2 and D3 in their small-rank guises. An A_{v-1} component would leave a rational exceptional direction outside the absorbed span.

This does NOT establish smooth realizability of the surviving D_r embeddings. Lattice feasibility, an embedded plumbing with the requisite complement, and an Einstein metric on the contracted bulk are distinct steps. It also does not remove rational-ball fillings, which carry no such sphere basis, or hypothetical b2=1 ALE fillings with an ADE end but without the Kronheimer topology.

## 4. Research consequence

The Step-74 analytic screen and this topological restriction are complementary. The analytic screen permits some high-rank ADE energy budgets; asphericity removes the E cases and the single A_r full-absorption cases on the actual target. This is a sharper reason to concentrate on the surviving D-type and rational-ball/global-bulk problems rather than enlarge the charge catalogue.

The exact paired-A1 law is a completed restricted branch once the stated topology/supplier inputs are checked. Its nonattainment is not Problem 3's desired smooth non-Bach-flat minimizer. Its value for that problem is the exclusion of a definite singular limiting topology below the strict smooth upper bound. The other global targets remain active.
