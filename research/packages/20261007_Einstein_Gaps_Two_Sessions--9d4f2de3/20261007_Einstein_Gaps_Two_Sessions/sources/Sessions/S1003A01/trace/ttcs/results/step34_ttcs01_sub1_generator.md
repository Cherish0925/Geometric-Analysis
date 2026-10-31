# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md",
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md",
    "Sessions/S1003A01/workspace/data/step33/cusp_closing_Wminus.json",
    "Sessions/S1003A01/workspace/scripts/step33_cusp_closing_Wminus.py",
    "Knowledge/objects/papers/Weyl-energy-and-connected-sums-of-four-manifolds--aac98700a100--c47de95b9e22/object.md",
    "Knowledge/objects/papers/1303.0827-Critical-metrics-on-connected-sums-of-Einstein-four-manifolds--ac8a5635dfbc--5258e72d2de1/object.md",
    "Knowledge/objects/papers/Degenerating-Kähler-Einstein-cones-locally-symmetric-cusps-and-the-Tian--adb04d311c2f--499d8f08a8b4/object.md"
  ]
}
```

## Task

Propose high-value next mathematical routes for the ramification-cap interaction problem, beyond repeating the separated-retention argument. Context: Existing certified CH perpendicular blow-up cell gives sub-four coefficient; Step 33 shows the upper law depends on blow-up fraction theta while lower theory depends on sigma=4r+18theta. The r-gap is now localized to ramification neighbourhoods carrying the KE background W^- energy B_Delta. Kähler blow-up cells have exact unit tariff; cheap cells require non-Kähler/paired-field relative rotation. We need genuinely different geometry: compute or bound the cost of a blow-up/handle cell in the exact cusp-closing Calabi KE cap near the elliptic divisor, and then decide what is realizable in actual ramified towers. Please propose concrete, technically plausible routes (analytic, variational, numerical, symbolic, gauge-theoretic, or local model construction) that could decide whether interacting cap cells improve the upper law or whether a localized field/volume estimate enforces retention. Tie each route to the actual formulas and sources, state what first calculation or proof object should be built, and warn against low-value distractions.

## Output

The ramification interaction is best formulated as a universal local variational problem, rather than as another global Chern–Weil estimate. After setting
\[
\tau=\tau _0u,\qquad X=\sqrt{\tau _0}\,x,\qquad
Y=\sqrt{\tau _0}\,y,\qquad \Psi=\tau _0\psi ,
\quad \tau _0=(3c/2)^{1/3},
\]
the exact Calabi cap becomes
\[
g_{\mathrm C}
=u(dX^2+dY^2)+\frac{du^2}{q(u)}
+q(u)(d\Psi+X\,dY)^2,\qquad
q(u)=\frac23(u^2-u^{-1}),\qquad u\ge1,
\]
with \(\Psi\) of period \(2\pi\). Thus its pointed geometry is universal: \(c\) and the ramification degree occur only through the quotient lattice in \((X,Y)\). Moreover,
\[
|W^-|^2=\frac{8}{3u^6},\qquad
\operatorname{Area}(D)=2\pi e,\qquad
\int_{\mathrm C}|W^-|^2=\frac{8\pi^2}{3}e.
\]
This normalization turns the question into a fixed-model cell problem repeated \(O(e)\) times.

For a compact cap region \(N\) and exact outer collar data from \(g_{\mathrm C}\), define
\[
\mathfrak j_{\rm bu}(N)
=\inf_{\substack{g\text{ on }N\#\overline{\mathbf{CP}}^2\\
g=g_{\mathrm C}\text{ on the outer collar}}}
\int |\operatorname{Ric}_g+g|^2,
\]
and define \(\mathfrak j_{\rm h}(N)\) analogously for an \(S^1\times S^3\) insertion. The comparisons that matter are
\[
\mathfrak j_{\rm bu}\quad\hbox{versus}\quad
J_{\rm CH}=8\pi^2(1-\eta_{\rm cert}),
\qquad
\mathfrak j_{\rm h}\quad\hbox{versus}\quad32\pi^2.
\]
Merely showing \(\mathfrak j_{\rm bu}<8\pi^2\) would not improve the present upper law, because the CH cell already lies below that value.

## 1. Chiral linear response of the cheap CH cell

The least expensive analytic calculation is the response of the existing CH cell to the spin-two ASD curvature channel. A KE background has the same \(R^+\) as CH and differs through
\[
H=W^-\in S^2_0\Lambda^-.
\]
The \(SU(2)_L\)-symmetric cell has no linear invariant pairing with \(H\), but this only says that a fixed symmetric core is blind at first order. Once spin-two deformations of the core are admitted, the optimized response has the Schur-complement form
\[
J(H)=J(0)+\langle H,A H\rangle
-\langle f_H,L^{-1}f_H\rangle+O(|H|^3+|\nabla H|\,|H|^2).
\]
Here \(L\) is the DeTurck-fixed Hessian of
\[
D(g)=\int|\operatorname{Ric}+g|^2
\]
at an optimized CH-collar cell, \(f_H\) is the forcing produced by the ASD background jet, and \(A\) is the direct collar-interpolation term. Isotropy reduces the quadratic response on \(S^2_0\Lambda^-\) to one scalar coefficient, provided the core is fully stationary rather than merely optimized in the current polynomial family.

This calculation can be reduced to coupled radial ODEs. Tensor harmonics on \(S^3\) split the metric perturbation into \(SU(2)_L\) representations; \(H\) occupies the five-dimensional spin-two channel. The first useful object is therefore the gauge-fixed spin-two Jacobi system on the authoritative cell, with regular bolt conditions and zero outer-collar jets. The resulting scalar
\[
\kappa_{\rm spin2}
=\langle H,A H\rangle-\langle f_H,L^{-1}f_H\rangle
\]
distinguishes two geometries:

* \(\kappa_{\rm spin2}<0\) gives a cap-tail cell cheaper than the CH cell. Since \(|W^-|^2\sim u^{-6}\), the excess saving summed over a dilute packing is proportional to
  \[
  \int |W^-|^2=\frac{8\pi^2}{3}e,
  \]
  hence linear in \(\Delta\).
* \(\kappa_{\rm spin2}>0\) shows that the CH cell resists weak ASD environments in every spin-two direction. A finite-amplitude cap core could still behave differently, but the long tail then supplies no \(r\)-dependent saving.

Malchiodi–Malizia provide a useful explicit forcing model. Their biharmonic annulus gives
\[
\Delta\mathcal W
=a^4\left(
C-\frac{4\pi^2}{9}\lambda^2
W^{\bar M}(p)\circledast W^Z(q)
+O(\lambda^2\gamma^2)\right)+\cdots .
\]
For a flat TT perturbation,
\[
\operatorname{Ric}'(h)=-\frac12\Delta h,\qquad s'(h)=0,
\]
so the principal quadratic part of \(D\) is
\[
D_2(h)=\frac14\int|\Delta h|^2.
\]
Thus their explicit biharmonic interpolation can be recalculated for \(D\), not only for \(\mathcal W\). The orientation bookkeeping for
\(\#\overline{\mathbf{CP}}^2\) must be done explicitly: the Weyl theorem by itself does not identify which chiral contraction survives for the desired blow-up topology. The supplied Gursky–Viaclovsky contraction algebra is exactly the right tensor calculation.

This route is especially valuable because it gives either an explicit trial deformation or a spectral coefficient before any expensive four-dimensional optimization.

## 2. A finite-amplitude toric cap cell

The ramification effect may be intrinsically finite-scale. At \(u=1\), the cap is smooth, has \(|W^-|^2=8/3\), and is far from CH. A point on the elliptic divisor has local complex coordinates in which the normal circle and a rotation in the divisor direction generate a \(T^2\)-action. The blow-up of that point remains toric: the local fan inserts the exceptional ray between the two original rays. This permits a genuinely non-Kähler \(T^2\)-invariant cell depending on two quotient variables.

A general invariant metric may be written in Kaluza–Klein form
\[
g=h_{ab}(z)\,dz^a dz^b
+G_{ij}(z)\bigl(d\phi^i+A^i_a(z)\,dz^a\bigr)
                \bigl(d\phi^j+A^j_b(z)\,dz^b\bigr),
\]
where \(z=(z^1,z^2)\) parametrizes the orbit space. Smooth rod conditions encode the divisor and exceptional sphere, while the outer collar is fixed to \(g_{\mathrm C}\). This class is broad enough to leave Kähler geometry and to align an anisotropic core with the distinguished eigendirection of \(W^-\).

The functional is particularly suitable for symbolic reduction:
\[
D=P+\frac14\int(s+4)^2
=2\int|W|^2+\frac13\int s^2
 +2\int s+4V-16\pi^2\chi.
\]
Its Euler equation is a fourth-order elliptic system after DeTurck fixing, with principal part belonging to the same quadratic-curvature family treated by Gursky–Viaclovsky. Reducing this expression to the two-dimensional orbit space gives a practical spectral or finite-element problem.

There are two useful levels.

1. **Explicit interpolation competitor.**  
   Expand the cap metric in normal coordinates at a bolt point, decompose its ASD curvature jet into tensor harmonics, and connect it to the existing perpendicular core through an annulus minimizing the quadratic \(D\)-energy. The Malchiodi–Malizia biharmonic formulas supply the flat leading part; exact cap corrections can be evaluated symbolically.

2. **Full two-variable minimization.**  
   Solve the DeTurck-fixed Euler system in the toric class, with topology encoded by rod vectors. A rational Chebyshev or spline output can then be converted into a smooth explicit metric and enclosed by interval arithmetic, following the present Arb certificate strategy.

The first concrete symbolic object is the exact two-dimensional formula for \(D\) in the toric ansatz, together with regularity expansions at the divisor and exceptional rods. A certified value
\[
\mathfrak j_{\rm bu}<J_{\rm CH}
\]
would immediately produce an \(r\)-dependent upper law. A cap handle can be treated with an \(S^1\)-invariant quotient and two excised bolt-centered regions joined by a tube. The handle comparison is potentially even more consequential:
\[
\mathfrak j_{\rm h}<32\pi^2
\]
would introduce an \(r\)-dependent saving even when \(\theta=0\).

Mixed blow-up–handle cells also belong here. The relevant resource is cap volume or divisor area, not the separate counts \(k\) and \(\ell\); a combined cell may consume less ramification area per unit saving than either pure cell.

## 3. The exact Weyl–volume exchange and a spectral retention problem

For a local replacement agreeing with \(g_{\mathrm C}\) on an outer collar, let \(k\) and \(\ell\) be the numbers of blow-ups and handles placed inside. Relative Euler and signature formulas give
\[
\boxed{
\Delta B
=10\pi^2k-8\pi^2\ell+\frac14P-\frac1{48}\Delta S.
}
\]
If the replacement has \(s=-4\), then
\[
\boxed{
\Delta B
=10\pi^2k-8\pi^2\ell+\frac14P-\frac13\Delta V.
}
\]
Equivalently, with
\[
V_{\rm ren}
=\Delta V-30\pi^2k+24\pi^2\ell,
\]
one has
\[
\boxed{\Delta B=\frac14P-\frac13V_{\rm ren}.}
\]
Thus local ASD retention is exactly
\[
V_{\rm ren}\le \frac34P.
\]
For a general metric, set
\[
T=\int(s+4),\qquad Z=\int(s+4)^2,\qquad D=P+\frac14Z.
\]
Then
\[
\Delta B
=10\pi^2k-8\pi^2\ell
+\frac14D-\frac13\Delta V+\frac16T-\frac1{12}Z.
\]
This is the correct quantity for a numerical cell that is only approximately scalar \(-4\).

A high-value analytic route is the constant-scalar spectral problem around the exact cap. If \(g(t)\) is a compactly supported path with \(s_{g(t)}=-4\), then at the Einstein cap
\[
V'(0)=P'(0)=B'(0)=0,
\qquad
B''(0)=\frac14P''(0)-\frac13V''(0).
\]
The generalized eigenvalue
\[
\Lambda_{\mathrm C}
=\sup_{\substack{h:\,DR_{g_{\mathrm C}}h=0\\
h\text{ vanishes on the outer collar}}}
\frac{V''(h)}{P''(h)}
\]
has the distinguished threshold \(3/4\):

* \(\Lambda_{\mathrm C}>3/4\) produces an explicit ASD-depletion mode on the cap.
* \(\Lambda_{\mathrm C}<3/4\), together with coercivity of the gauge-fixed Hessian, yields local retention for all sufficiently small cap deformations.

Because the cap is Heisenberg-cohomogeneity one, the eigenproblem separates into Fourier representations in \((X,Y,\Psi)\) and radial ODEs in \(u\). The translation-invariant sector is especially inexpensive: a metric
\[
g=a(u)^2(dX^2+dY^2)+b(u)^2du^2+c(u)^2(d\Psi+X\,dY)^2
\]
reduces the scalar equation and \(P,V,B\) to one-dimensional expressions. It cannot create a point blow-up, but it can identify whether coherent cap preconditioning raises \(V_{\rm ren}\) at a favorable rate before a cell is inserted.

A stronger theorem would be a finite-amplitude inequality
\[
V_{\rm ren}\le \frac34P
\]
for all scalar-\(-4\) fillings with the given collar. The relevant source families are the volume functional for fixed-scalar metrics, V-static or Miao–Tam equations, hyperbolic fill-in inequalities, and renormalized-volume identities in Einstein gluing. The cap is not of constant sectional curvature, so an argument using only scalar curvature is unlikely to suffice; the exact KE structure or a localized field has to enter.

## 4. A relative gauge-field calibration tied to the elliptic divisor

The cap carries a canonical \(L^2\) ASD two-form representing the elliptic zero section:
\[
F_D
=u^{-2}du\wedge(d\Psi+X\,dY)-u^{-1}dX\wedge dY.
\]
It satisfies
\[
*F_D=-F_D,\qquad
\frac1{2\pi}\int_{\text{normal fibre}}F_D=1,\qquad
\int |F_D|^2=4\pi^2e.
\]
The Calabi symmetry also makes the line spanned by \(F_D\) invariant under \(W^-\). Computing the signed eigenvalue of \(W^-\) on this line is a short symbolic tensor calculation and should precede any abstract field argument.

This form suggests a localized analogue of LeBrun’s curvature estimate. The ideal identity would have the shape
\[
B_N(g)-\frac{8\pi^2}{3}e
+\mathfrak a\,P_N(g)+\mathfrak b\,Z_N(g)
=\int_N\bigl(\text{field squares}+\text{metric squares}\bigr)
+\mathcal Q_{\rm interface},
\]
where \(\mathcal Q_{\rm interface}=0\) when the canonical cap state is fixed on the outer collar. Equality should reproduce \((g_{\mathrm C},F_D)\).

There are two technically distinct realizations.

### Relative Spin\(^c\) state on the nilmanifold interface

A level set \(u=U\) is a circle bundle over \(T^2\), hence a Heisenberg nilmanifold. The cap determines a canonical Spin\(^c\) state there. The relative invariant of the disk bundle of degree \(-e\), and its behavior under an interior blow-up, can be studied using:

* monopole Floer theory for circle bundles over surfaces;
* Seiberg–Witten equations on Seifert three-manifolds;
* APS Dirac theory on Heisenberg nilmanifolds;
* Taubes-type relative invariants for symplectic cobordisms.

The decisive object is the Chern–Simons–Dirac action of the canonical state and its continuation across the blown-up cap. If the relative invariant forces that state, the global monopole cannot freely choose a low-energy interface trace.

### Paired-field vortex energy

For the sign pair \(c\pm E\), the relative line has
\[
c_1(u)=E,\qquad
f_u=\frac{f_+-f_-}{2}.
\]
Since this line is trivial on the outer collar but has compact interior charge, the paired spin direction must rotate or its amplitude must decrease. On the exact cap, the canonical field has fixed positive amplitude, so the relevant estimate is a covariant vortex inequality of the form
\[
\int_N\left(
|D u|^2+\rho^2|\nabla n|^2+|f_u|^2
+\text{potential terms}\right)
\ge \mathfrak v_e.
\]
The key algebraic issue is whether the paired Seiberg–Witten identity contains enough of the full relative curvature \(f_u\), rather than only its self-dual component. The nilmanifold Dirichlet-to-Neumann operator gives a concrete way to price rotation that tries to escape into the exterior.

The first proof object here is an explicit cap monopole and the complete APS Weitzenböck identity, including every interface Chern–Simons term. An isolated invariant ODE with artificially prescribed CH asymptotics does not supply this relative statement.

## 5. Transfer from the exact cap to the ramified KE towers

Biquard–Guenancia give a bilinear comparison between the conic KE metric and the Calabi model, with ratio tending to one, and the ramified pullback is smooth across \(u=1\). For a fixed cap slab
\[
1\le u\le U,
\]
the needed transfer theorem is
\[
\bar\pi_m^*\widehat g_{\beta_m}
\longrightarrow g_{\mathrm C}
\quad\text{in }C^{q,\alpha}
\]
in normalized cap coordinates, uniformly over the selected ramification components.

There is a plausible elliptic upgrade from their \(C^0\) comparison. Both metrics satisfy \(\operatorname{Ric}=-g\); after passing to harmonic-map gauge, the Einstein equation is elliptic. Bilipschitz control, model noncollapse, and smooth lifting at the divisor give a uniform harmonic radius on fixed normalized balls, after which standard elliptic bootstrapping gives all derivatives. The arithmetic input must also supply embedded balls: the normalized divisor has area \(2\pi e_c\), and its lattice is a finite cover of a fixed cusp lattice, so its systole should not decrease. A maximal separated net then gives at least \(c\,e_c\) disjoint cap sites.

Once local costs are known, the upper coefficient is a packing problem. Write
\[
\delta_{\rm bu}
=\frac{J_{\rm CH}-\mathfrak j_{\rm bu}}{8\pi^2},
\qquad
\delta_{\rm h}
=\frac{32\pi^2-\mathfrak j_{\rm h}}{32\pi^2}.
\]
If \(n_{\rm bu}\) cap blow-ups and \(n_{\rm h}\) cap handles can be placed disjointly, then
\[
\frac{D}{8\pi^2Q}
\le
1-\eta_{\rm cert}\theta
-\delta_{\rm bu}\frac{n_{\rm bu}}{Q}
-4\delta_{\rm h}\frac{n_{\rm h}}{Q}
+o(1),
\]
and hence
\[
\frac{\alpha}{h}
\le
4\left[
1-\eta_{\rm cert}\theta
-\delta_{\rm bu}\frac{n_{\rm bu}}{Q}
-4\delta_{\rm h}\frac{n_{\rm h}}{Q}
\right]+o(1).
\]
Since the available normalized cap area is proportional to
\(\Delta=rQ\), the packing densities turn these ratios into explicit functions of \((r,\theta)\). In the dilute regime one expects terms such as
\[
\delta_{\rm bu}\min\{\theta,\nu_{\rm bu}r\},
\]
with analogous handle and mixed-cell terms. If the excess response is proportional to \(|W^-|^2\), its total sum is automatically proportional to \(B_\Delta\), giving the sought linear \(r\)-law.

## Low-information directions

Several activities would consume substantial effort without deciding the cap interaction.

* Re-deriving the relative signature identity only reproduces the Weyl–volume exchange; the missing sign remains.
* A purely Kähler blow-up ansatz cannot beat \(8\pi^2\), while the current CH cell is already below that value.
* Re-optimizing only the \(SU(2)_L\)-symmetric core cannot see the spin-two ASD channel. The symmetry-breaking harmonic must be present.
* A small-neck theorem giving a strict decrease of Weyl energy does not by itself beat the certified CH cost. The calculation must use \(D\), retain the scalar channel, and reach a quantitative finite-scale value.
* An isolated monopole shooting problem does not determine the closed or relative field state selected by the exterior.
* \(C^0\) model comparison alone does not transfer a certified curvature-energy cell; \(C^2\) control and an embedded-site count are essential.

The highest-yield combination is therefore: spin-two response first, finite-amplitude toric cell second if the response is favorable or inconclusive, and the relative field/volume route in parallel as the mechanism that could force retention for all cap cells.