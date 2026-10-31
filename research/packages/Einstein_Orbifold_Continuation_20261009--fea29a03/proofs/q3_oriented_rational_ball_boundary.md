# Q3: orientation-dependent exclusion of rational-ball limits

Date: 9 October 2026.

The target is smooth global attainment of P(g)=integral |Ric^0_g|^2 on a closed manifold which admits no Einstein metric and has negative Yamabe invariant. No attainment theorem is proved here. Two precise conclusions sharpen the singular-boundary problem: the previous reversed-B2 exclusion extends to every finite collection of reversed Ricci-flat half-conformally-flat rational ALE cores; the ordinary orientation occurs in actual sub-Burns competitors on a different, specified Godeaux blowup.

## 1. All reversed rational ALE cores, with their group orders retained

Let M=X#CPbar^2, K^2=A>0, E^2=-1 and K.E=0. Suppose the two classes K+E and K-E have unperturbed SW solutions for every smooth metric, in the same sense used in the previous continuation. Let N_i be finitely many nonflat Ricci-flat anti-self-dual ALE spaces with b2(N_i)=0 and pi1(N_i)=Z_(d_i). Wright's classification gives d_i>=2 and group at infinity of order d_i^2. Set

    delta_i=1-d_i^(-2).

With curvature-operator norms,

    integral_Ni |Rm|^2=8*pi^2*delta_i,
    chi_curv(N_i)=delta_i,
    tau_curv(N_i)=-(2/3)*delta_i,
    T_curv(N_i)=2*chi_curv+3*tau_curv=0.

The equalities for signature and T refer to curvature integrals, not to the ordinary signature of the rational ball, which is zero. Reverse orientation. Then

    T_curv(-N_i)=4*delta_i.

Assume disjoint compact cores -N_i embed in M and replacing each by its asymptotic cone gives a compact orbifold O with the standard isolated quotient charts. The same scalar-controlled smoothing and actual-field transfer proved in the preceding continuation apply at finitely many points. Every smooth orbifold metric on O therefore has the two limiting actual classes K_O+E_O and K_O-E_O; at least one has self-dual square >=A. No simultaneous estimate over all orbifold metrics is required for this statement: one performs the smoothing for each chosen metric and each member of its conformal class.

Real cohomology is unchanged because all removed pieces are rational balls. The topological curvature quantity is

    T_curv(O)=A-1-4*sum_i delta_i.

Consequently the mixed monopole inequality gives the intrinsic bound

    P_orb(g)>=8*pi^2*(1-A/3+4*sum_i delta_i).       (1)

It holds for every smooth orbifold metric g, under the stated actual-field input. In particular, if at least one such core occurs and A<=9, then sum_i delta_i>=3/4 and

    P_orb(g)>=8*pi^2.

Thus a smooth compact orbifold limit of a sequence with limsup P<8*pi^2 cannot be produced by any nonempty collection consisting entirely of these reversed rational cores. More generally, if a strict upper bound is P<8*pi^2*u, a proposed compact limit is excluded whenever

    4*sum_i(1-d_i^(-2))>=u-1+A/3.                (2)

The same bound persists if other ordinary-orientation rational cores are also contracted: their T_curv contribution is zero and their real cohomology is zero. It does not address positive-b2 cores, non-half-conformally-flat Ricci-flat ALE spaces, or partial collapse.

This is an extension of the previous SW-transfer theorem, not a new compactness theorem. Its proof uses the already established transfer; it does not independently certify that analytic argument.

## 2. The opposite orientation is a real geometric alternative

Kazanova, arXiv:1402.0254, Proposition 2.6, constructs a Q-Gorenstein degeneration of a numerical Godeaux surface Y with H1(Y;Z)=Z/4 to a normal surface Z with ample canonical divisor and exactly one Wahl singularity of type 1/4(1,1). Here K_Y^2=1 and p_g(Y)=q(Y)=0. The local smoothing is the rational homology ball B_(2,1), in its ordinary complex orientation.

For specificity her construction is a degree-(8,8) complete intersection in P(1,1,4,4,4), with a free-away-from-the-quotient action yielding the single Wahl point. Proposition 2.6 establishes the smoothing and ampleness; no new algebraic-surface construction is claimed here.

By the orbifold Aubin--Yau theorem Z admits a negative orbifold KE metric h0. Choose a smooth point disjoint from the singular point. Apply the project's strict negative-KE Burns insertion theorem in a small ball about that point, and keep h0 unchanged elsewhere. The resulting one-point blowup orbifold O carries a smooth orbifold metric h with

    q0=P_orb(h)<8*pi^2.

This extension of the inherited insertion theorem is local: its entire non-Einstein modification is supported in the selected ordinary chart; the orbifold singularity lies in an unchanged KE region.

The Milnor fiber B_(2,1) admits a Ricci-flat Kähler ALE metric with end model C^2/(1/4(1,1)) and decay order4. This is the ordinary, not reversed, quotient of Eguchi--Hanson. Insert a scaled copy at the Wahl point. Write a for its length scale and match at rho=a^(1/2). The two metric expansions are

    h=delta+O(r^2),
    a^2*g_ALE=delta+O(a^4*r^(-4)),

with two differentiated bounds. On the joining annulus,

    |Rm|<=C*(1+a^4*rho^(-6)),
    integral_annulus |Rm|^2<=C*(rho^4+a^4*rho^(-2)+a^8*rho^(-8))=o(1).

The inserted inner region has P=0. The removed orbifold ball also has P=0, since h equals h0 there. Hence these are genuine smooth metrics on the fixed smooth manifold

    M=Y#CPbar^2,
    P(g_a)->q0<8*pi^2.                           (3)

Their rescaled cores converge to the nonflat Ricci-flat B_(2,1) metric; curvature becomes unbounded in the fixed bulk normalization. The sequence has no smooth global limit with that normalization.

On this same M, A=1 and T=0. The classical monopole bound gives P(g)>=16*pi^2/3 for all smooth g. In particular M has no Einstein metric, and its Yamabe invariant is negative. Thus

    16*pi^2/3<=P_*(M)<=q0<8*pi^2,

while the sublevel below8*pi^2 already contains the degeneration (3). It is not known here that q0 equals P_*(M); this does not prove nonattainment. It proves that changing to this otherwise natural Godeaux candidate does not remove the rational-ball boundary.

## 3. Why (1) and (3) are consistent

The ordinary Ricci-flat ASD rational ball has

    W+=0, P=0, T_curv=0.

Its contraction leaves T_curv(O)=T(M)=0. The transferred monopole bound is therefore only16*pi^2/3 and is consistent with (3). Reversing the same metric makes its6*pi^2 Weyl integral self-dual and changes its T_curv contribution from0 to3. It is this chiral change which produced the preceding exclusion theorem. A statement suppressing orientation would be false.

The project previously used the classical torsion-Z5 Godeaux surface. The present Y has torsionZ4 and is a different smooth candidate. Kazanova's Corollary2.5 explicitly excludes an ample-canonical single1/4(1,1) Wahl degeneration for the torsion-Z5 family. That algebraic exclusion does not exclude an arbitrary smooth rational-ball embedding or a non-Kähler metric degeneration on the Z5 candidate. Its already constructed A1 degeneration also remains available.

## 4. Mathematical consequence for the attainment route

The transferred-field obstruction disposes of an entire orientation class of compact rational-ball limits in the stated low-A range. It cannot dispose of the other class: Section2 realizes that class below the same strict upper bound on a manifold already known to be non-Einstein.

A successful attainment proof still needs a strict comparison against the optimized ordinary-orientation singular problem, a theorem lowering every such singular minimizing configuration by a smoothing, or an independent route to a smooth minimizer. The construction here supplies an actual test case for any proposed theorem of that form. It does not introduce a new research target.

## Primary sources read

1. E. P. Wright, *Quotients of gravitational instantons*, arXiv:1102.2442v2, TheoremA and Section8, https://arxiv.org/pdf/1102.2442 . These give the classification, |Gamma_infinity|=d^2(b2+1), and ALE energy formula.
2. A. Kazanova, *Degenerations of Godeaux surfaces and exceptional vector bundles*, arXiv:1402.0254, Theorem1.2, Proposition2.6 and Corollary2.5, https://arxiv.org/pdf/1402.0254 . This supplies the explicit Z4 degeneration and the distinction from the Z5 family.
3. I. Suvaina, *The Yamabe invariant of a class of symplectic4-manifolds*, arXiv:1410.1236, Proposition2.4, Section3 and proof of Theorem3.4, https://arxiv.org/pdf/1410.1236 . This states the negative orbifold KE input, ordinary Ricci-flat Kähler rational-ball fillings, their order4 asymptotics and the interpolation method. Its ALE existence input is I. Suvaina, *ALE Ricci-flat Kähler metrics and deformations of quotient surface singularities*, Ann. Global Anal. Geom.41(2012),109--123.
4. The project's strict local Burns theorem and the preceding actual-field transfer theorem are inherited inputs, not claimed as literature results or as newly proved here.
