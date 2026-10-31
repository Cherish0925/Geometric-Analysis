# Independent proof of the intrinsic reversed-rational-ball orbifold bound

The strengthened statement does not need a minimizing sequence or a constant-scalar convergence hypothesis. Let M=X#CPbar² carry both ordinary actual classes a_±=K±E for every smooth metric, with K²=A>0, E²=-1, K.E=0. Let O be the smooth compact orbifold obtained by replacing the specified embedded reversed Eguchi–Hanson quotient rational ball -B₂ by its Z4 cone. Then for every smooth orbifold metric g_0,

    P_orb(g_0) >= 8 pi² (4-A/3).

This is an intrinsic metric-independent lower bound on O, conditional only on the stated actual supply on M and the specified topological replacement. It is not an assertion that all minimizing limits have this topology.

## 1. Uniform scalar lower bound in the explicit desingularization

Use equivariant normal coordinates for g_0 at the orbifold point. On the quotient annulus write g_0=delta+h_0 and the scale-a reversed Ricci-flat ALE model as delta+h_N. For 0<=m<=2,

    |D^m h_0| <= C r^(2-m),
    |D^m h_N| <= C a^4 r^(-4-m).

The latter is the standard order-four Eguchi–Hanson decay, which descends to its free quotient. Set r_a=a^(1/2). With a fixed radial cutoff form

    g_a = delta + chi(r/r_a) h_N + (1-chi(r/r_a)) h_0

on r_a<=r<=2r_a, using the exact ALE metric inside and g_0 outside. On this annulus, both tensors have small C^0 norm and

    |Rm(g_a)| <= C[1+a^4/r_a^6+(r_a+a^4/r_a^5)^2] <= C.

The exact inner metric is Ricci-flat; the outer metric is fixed. Therefore the scalar curvatures have one uniform lower bound, and volumes remain uniformly bounded. The P contribution of the transition annulus tends to zero because its curvature is bounded and its volume is O(r_a^4). Hence P(g_a)->P_orb(g_0), as in the inherited zero-P-loss construction.

The choice r_a=a^(1/2) is important to the supply argument. Merely recording a vanishing total P error at an arbitrary neck scale would not itself provide a scalar lower bound.

## 2. Passage of the actual fields

For each of the two fixed spin^c structures choose actual unperturbed solutions on g_a. The maximum principle gives a uniform pointwise spinor bound from the scalar lower bound. The curvature equation bounds F_A^+ pointwise. Bounded volume and

    integral(|F_A^+|²-|F_A^-|²) = 4 pi² a_±²

then give uniform determinant-curvature L² bounds. The integrated spinor Weitzenböck identity gives a uniform covariant-gradient L² bound. Local gauge compactness and elliptic bootstrapping give smooth limiting solutions on every compact subset of O_reg. Since there are only two classes, a common subsequence can be used.

Lift near the isolated point to the punctured smooth four-ball. The finite-energy abelian connection can be put in W^(1,2) Coulomb gauge, and the bounded spinor has finite covariant energy. The point is removable in the weak equations. For the connection, d*+d+ is elliptic with bounded right side q(Phi), so local W^(1,p) regularity holds for finite p; the Dirac equation and iteration yield smoothness. The finite deck action extends, retaining its spin^c lift and determinant isotropy. One must not replace this extension by a claim of trivial determinant holonomy on the quotient.

Equivalently, for the connection curvature, dF=0 and F+=q(Phi) control the elliptic first-order Hodge system; finite L² prevents a delta source at the point. On the simply connected covering ball the smooth closed curvature has a smooth potential, and the original connection differs by a removable gauge. This gives the same equivariant extension.

This works for each arbitrary smooth orbifold metric, including every member of every orbifold conformal class. There is no extra conformal transfer problem to solve. The resulting local isotropy is allowed to be part of the orbifold spin^c extension; the real classes used below are fixed by the regular-bulk marking. For the classical mixed inequality, their real self-dual projections are invariant under conformal change.

## 3. Real topology and the projection budget

The rational ball and its cone both have H²(-;R)=0, and their common lens-space boundary is a real homology sphere. Mayer–Vietoris, or compactly supported representatives in the common complement, gives an identification of real H² preserving its intersection form. Consequently

    K_O²=A, E_O²=-1, K_O.E_O=0.

For every orbifold metric,

    ((a_+^+)²+(a_-^+)²)/2 = (K_O^+)²+(E_O^+)² >= A.

Thus one actual class has projection square at least A. No convergence of harmonic projections was assumed.

## 4. Local topological correction and mixed estimate

The reversed Ricci-flat quotient has chi=1, group order four, and all its operator curvature energy in W+:

    integral |W+|² = 8 pi²(1-1/4) = 6 pi².

Its Euler curvature contribution is 3/4 and its signature curvature contribution is 1/2. Thus

    chi_orb(O)=chi(M)-3/4,
    tau_curv,orb(O)=tau(M)-1/2,
    T_curv,orb=2chi_orb+3tau_curv,orb=(A-1)-3=A-4.

Here tau_curv is explicitly the signature curvature integral; the signature of the real intersection pairing remains tau(M). Confusing these two quantities would erase the relevant correction.

The classical mixed SW curvature inequality applies to the smooth compact orbifold by its invariant-chart Weitzenböck and conformal proof. Combining it with the all-metric actual supply and Chern–Weil gives

    P_orb >= 8 pi²[(2/3)A - T_curv,orb]
          = 8 pi²(4-A/3).

For A<=9 this is at least 8 pi². Therefore a sequence with limsup P<8 pi² cannot converge smoothly off this specified core to a smooth compact metric on O: nonnegativity and smooth convergence on compact regular subsets imply P_orb(g_0)<=liminf P(g_j).

The conclusion does not exclude partial collapse, different core topology/orientation, or a limit not known to be a smooth compact orbifold. No energy equality for the neck or the original harmonic projections is used.
