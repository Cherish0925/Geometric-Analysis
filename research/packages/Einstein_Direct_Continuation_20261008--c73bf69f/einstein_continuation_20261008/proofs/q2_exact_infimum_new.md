# Q2: spherical classes, a surviving zero-Ricci bubble, and an orbifold comparison

Date: 2026-10-08. This note continues the two supplied October 8 manuscripts. It does not determine the unrestricted minimum of `P = integral |Ric^0|^2` on a nonminimal general-type surface. It establishes a concrete topological restriction and, importantly, constructs the actual quotient-bubble channel which that restriction does not eliminate.

## 1. The spherical lattice of a blow-up of an aspherical manifold

**Proposition 1.** Let X be a closed oriented smooth four-manifold with pi_2(X)=0, and put M=X#k CPbar^2. Write E_1,...,E_k for the usual exceptional generators. Every spherical homology class in M lies in their integral span. Consequently, for an embedded oriented sphere S,

\[
[S]=\sum_i n_iE_i,\qquad [S]^2=-\sum_i n_i^2.
\]

**Proof.** The degree-one collapse map c:M->X induces the projection in the integral connected-sum decomposition H_2(M)=H_2(X) direct-sum Z^k. For any map f:S^2->M, c composed with f is nullhomotopic because pi_2(X)=0. Its integral homology class is therefore zero. Thus f_*[S^2] lies in the exceptional summand, whose form is minus the identity. The normal Euler number of an embedded sphere is its homological self-intersection, giving the stated formula. Torsion in H_2(X) causes no change because the projected spherical class is exactly zero, not merely rationally zero.

**Corollary 1.** On X#CPbar^2 there is no embedded sphere of square -2 or +2. A compact core of any nonflat simply connected hyperkahler ALE four-manifold cannot embed in M in either orientation: its ADE exceptional configuration contains a sphere of square -2 in one orientation and +2 in the other.

This is a restriction on actual embedded bubbles. It does not assume a decomposition of all minimizing sequences and does not classify arbitrary Ricci-flat ALE spaces as hyperkahler.

**Proposition 1a (including cyclic quotients).** If X is as above and M=X#CPbar^2, any nonflat Ricci-flat half-conformally-flat ALE four-manifold whose compact core embeds in M must have b_2=0.

**Proof.** Simply connected hyperkahler cores were excluded by Corollary 1. By Wright's Theorem A, a non-simply-connected Ricci-flat ASD ALE space N is a cyclic quotient of a Gibbons-Hawking space. Write d=|pi_1(N)| and r=b_2(N). Its universal cover has d(r+1) centers because Euler characteristic multiplies under the covering. Wright's exact end-group sequence therefore gives

\[
\pi_1(N)=\mathbb Z_d,\qquad
|\Gamma_\infty|=d^2(r+1).
\]

The end group is cyclic as well: Wright makes the quotient Kahler, and Suvaina's Theorem B together with Theorem 2.2 identifies its cyclic quotient singularity at infinity. Thus H_1 of the end has order |Gamma_infinity|, not merely an order dividing it.

The Hopf exact sequence pi_2(N)->H_2(N;Z)->H_2(Z_d;Z)->0 and H_2(Z_d;Z)=0 imply that every integral two-dimensional homology class in N is spherical. Under the embedding into M, its image thus lies in Z E. The definite intersection form of N is nondegenerate, so inclusion is injective on rational H_2: any class mapped to zero would pair trivially with every class already inside N. Hence r<=1. Orientation reversal does not affect this argument (and a positive-definite nonzero form cannot inject into the negative spherical lattice at all).

For clarity, one can compute the determinant in the possible rank-one case without assuming an integral root-lattice classification. Take a compact core with boundary Y=S^3/Gamma. The end-group map pi_1(Y)->pi_1(N) is onto. Since both N and Y are connected, the relative homology sequence gives H_1(N,Y;Z)=0. Poincare-Lefschetz duality then gives H^3(N;Z)=0, so H_2(N;Z) is torsion-free. The relevant sequence is

\[
0\to H_2(N)\xrightarrow{j}H_2(N,Y)
\to H_1(Y)\to H_1(N)\to0.
\]

The torsion subgroup of H_2(N,Y)=H^2(N) has order d, and the free part of j is the intersection matrix Q_N. Therefore

\[
d\,|\det Q_N|=|\ker(H_1(Y)\to H_1(N))|
=|\Gamma_\infty|/d,
\qquad |\det Q_N|=r+1.
\]

If r=1, a generator z has square -2 in the ASD orientation. But its ambient image is nE and has square -n^2. This is impossible. The reversed orientation has positive square and is already impossible. Thus r=0.

This completes an exclusion of **all positive-b_2 spaces in Wright's class**, including the finite quotients. It leaves precisely the rational-homology-ball branch of that class. No assertion about Ricci-flat ALE spaces without half-conformal flatness is used.

## 2. A rational-ball bubble survives, even on a single blow-up

Let B_2=D(T^*RP^2), with its symplectic orientation. Its interior N is the free Z_2 quotient of the Eguchi-Hanson space T^*S^2 under the lifted antipodal involution. Equivalently, in the Stenzel complex structure on the smooth quadric, it is the free involution z -> -z. The Eguchi-Hanson/Stenzel metric descends to a complete Ricci-flat ALE metric g_N. The invariants are

\[
\pi_1(N)=\mathbb Z_2,\quad H_2(N;\mathbb Q)=0,\quad
\chi(N)=1,\quad |\Gamma_\infty|=4,
\]
\[
P(N,g_N)=0,\qquad
\int_N|\operatorname{Rm}_{\mathrm{op}}|^2
=8\pi^2(1-1/4)=6\pi^2.
\]

One may identify the end as L(4,1) in the boundary convention compatible with the complex quotient 1/4(1,1). Reversing orientation changes its lens-space orientation, not Ricci curvature or P.

**Proposition 2.** Every M=X#CPbar^2 contains an embedded copy of -B_2, the orientation reversal of B_2. The inclusion homomorphism pi_1(B_2)->pi_1(M) is zero. In particular, torsion-freeness of pi_1(M) does not prohibit this core.

**Proof.** The standard real RP^2 in CP^2 is Lagrangian. Its tubular neighborhood is the disk cotangent bundle B_2, with the orientation just fixed; alternatively it is the complement of a small tubular neighborhood of a nonsingular complex conic. Choose a four-ball in its complement. Reversing orientation embeds -B_2 in CPbar^2 minus that ball, which is the connected-sum piece in M. Its fundamental group maps through the simply connected punctured CPbar^2, so the induced map to pi_1(M) is trivial.

Thus the implication “the ambient fundamental group is torsion-free, hence a non-simply-connected ALE core cannot embed” is false. The finite fundamental group of the core need not inject into the ambient group. This is an explicit example, not a formal group presentation.

## 3. The surviving channel is realizable by smooth metrics

Contract the embedded -B_2 to a single orbifold point with the same spherical-space-form link, obtaining an oriented orbifold O. The complementary smooth region is unchanged. Let g_0 be any smooth orbifold metric on O.

**Proposition 3.** There are smooth metrics g_a on M, a downarrow 0, which converge to g_0 away from the singular point, develop (-N,g_N) as their rescaled bubble, and satisfy

\[
P(g_a)\longrightarrow P_{\mathrm{orb}}(g_0).
\]

Consequently,

\[
P_*(M)\le P_{*,\mathrm{orb}}(O),
\]

where the right side is the infimum over smooth orbifold metrics with this fixed local quotient structure.

**Proof.** In orbifold normal coordinates, g_0=g_euc+O(r^2), with the corresponding differentiated estimates. At infinity the quotient Eguchi-Hanson metric has ALE order four,

\[
g_N=g_{\mathrm{euc}}+O(R^{-4}),\qquad
\partial^j(g_N-g_{\mathrm{euc}})=O(R^{-4-j}),\quad j\le2.
\]

Scale the ALE metric by a^2 and match it to g_0 on an annulus of radius r_a=a^q, with any fixed 0<q<1. In physical coordinates its deviation from the flat cone is O(a^4 r^{-4}). A radial cutoff gives the curvature estimate

\[
|\operatorname{Rm}(g_a)|\le C(1+a^4r_a^{-6})
\]

on the matching annulus. Its volume is O(r_a^4), so its full curvature energy, and hence its P energy, is at most

\[
C\bigl(r_a^4+a^8r_a^{-8}+a^4r_a^{-2}\bigr)\to0.
\]

The ALE interior has identically zero Ricci tensor, while the removed orbifold ball contributes O(r_a^4) to P. Outside the annulus the metrics agree. This proves the P limit. The ratio r_a/a tends to infinity, so the rescaled inserted region exhausts N and the bubble convergence is genuine. Taking the infimum over g_0 proves the variational comparison.

No Einstein gluing or SW solution was assumed for the chosen orbifold bulk. The construction is a geometric competitor, not a minimizing-sequence theorem.

The Chern-Weil accounting is also exact. Orbifold Euler characteristic is

\[
\chi_{\mathrm{orb}}(O)=\chi(M)-3/4.
\]

Therefore the full curvature limit is

\[
8\pi^2\chi_{\mathrm{orb}}(O)+P(g_0)+6\pi^2
=8\pi^2\chi(M)+P(g_0).
\]

The nonzero 6 pi^2 bubble curvature is compensated by the orbifold Euler correction and produces **no** P charge. This is why an unqualified positive cost per nontrivial bubble fails.

## 4. A useful low-energy exclusion when a scalar budget is available

Suppose now M=X#CPbar^2 is in the original general-type supply range, with A=c_1^2(X)>0, so every metric satisfies S>=32 pi^2 A and T_+=A-1. For a sequence satisfying P(g_j)<=8 pi^2-delta, delta>0, Chern-Weil gives

\[
W_+(g_j)=\frac14P(g_j)-\frac1{48}S(g_j)+2\pi^2(A-1)
\le\frac{4\pi^2A}{3}-\frac\delta4.
\]

The reversed quotient bubble -N has W_+ energy 6 pi^2. Consequently it is excluded from such a sequence whenever A<=9/2. For integer A this covers A<=4. This uses ordinary nonnegative energy lower semicontinuity on exhausting bubble compact sets; no energy identity is required.

The orientation is essential. The unreversed quotient has W_+=0, while the copy naturally embedded in the CPbar^2 summand is the reversed one. One cannot interchange these orientations in the budget.

For the aspherical examples with larger A, the inequality does not exclude the bubble. For the low-A Horikawa/Godeaux examples, the ambient manifold need not have pi_2=0, so Proposition 1 does not eliminate the other ADE channels. These two useful exclusions must not be combined as though they applied to the same unrestricted class.

## 5. An additional global connection, presently conditional

In a compact orbifold limit with this single reversed B_2 bubble, the signature integral of the bulk is tau_orb=tau(M)-1/2. Thus

\[
T_{+,\mathrm{orb}}=A-4.
\]

If actual monopole supply transfers to the bulk with the **same** projected budget p_orb>=A, the classical monopole inequality would give

\[
P_{\mathrm{orb}}\ge8\pi^2\left(\frac23A-(A-4)\right)
=8\pi^2(4-A/3).
\]

For A<=9 this is at least 8 pi^2 and would exclude the channel in a strictly sub-8 pi^2 minimizing sequence. Establishing the actual orbifold solution and projection transfer is indispensable; the inequality is not asserted here from topology alone. The Q3 agent is investigating this precise transfer.

## 6. Relation to the Burns insertion work and present status

The supplied insertion law reads

\[
P(g_\varepsilon)=P(g)+8\pi^2-8\pi^2\varepsilon R_+(\zeta,\zeta)
+4\pi^2\Phi\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2).
\]

Hence relocation of an actual independently detachable Burns component would force R_+<=0 on the bulk. A kernel direction with nonzero tracefree transverse block is then excluded by the negative logarithmic term. This correctly excludes KE-type standard splitting; it does not exclude strictly negative R_+ bulk and cannot remove the zero-P quotient channel constructed above.

No new unrestricted sharp P lower bound or exact general-type P_* has been obtained in this note. The completed mathematical content is the spherical-lattice exclusion, the explicit surviving rational-ball core, its true smooth degeneration with no P loss, and the exact orientation-sensitive low-energy exclusion. They identify which topological argument works and which would fail even for actual smooth metrics.

### Primary sources for the classical components

1. E. P. Wright, *Quotients of gravitational instantons*, arXiv:1102.2442, Theorem A and Corollaries B-C. https://arxiv.org/pdf/1102.2442 . The Ricci-flat ASD classification includes cyclic quotients and explicitly warns that simply connected ambient manifolds do not automatically exclude non-simply-connected bubbles.
2. I. Suvaina, *ALE Ricci-flat Kahler metrics and deformations of quotient surface singularities*, arXiv:1102.2672. https://arxiv.org/pdf/1102.2672 . The ALE quotient/rational-smoothing construction is classical.
3. R. Fintushel and R. Stern, *Six Lectures on Four 4-Manifolds*, Lecture 4, section 1: the complement of a nonsingular conic in CP^2 is the rational ball B_2, a tubular neighborhood of RP^2. https://www.dm.ufscar.br/profs/ebt/history/2010/files/Fintushel.pdf .

The classical examples are not claimed as new. Their assembly here supplies a concrete continuation of the project's missing marked-core analysis.
