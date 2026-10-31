# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 34,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step34_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step34_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Propose high-value next mathematical routes for the ramification-cap interaction problem, beyond repeating the separated-retention argument. Context: Existing certified CH perpendicular blow-up cell gives sub-four coefficient; Step 33 shows the upper law depends on blow-up fraction theta while lower theory depends on sigma=4r+18theta. The r-gap is now localized to ramification neighbourhoods carrying the KE background W^- energy B_Delta. Kähler blow-up cells have exact unit tariff; cheap cells require non-Kähler/paired-field relative rotation. We need genuinely different geometry: compute or bound the cost of a blow-up/handle cell in the exact cusp-closing Calabi KE cap near the elliptic divisor, and then decide what is realizable in actual ramified towers. Please propose concrete, technically plausible routes (analytic, variational, numerical, symbolic, gauge-theoretic, or local model construction) that could decide whether interacting cap cells improve the upper law or whether a localized field/volume estimate enforces retention. Tie each route to the actual formulas and sources, state what first calculation or proof object should be built, and warn against low-value distractions.

## Integrated Scientific Memo

# Ramification-cap interaction: decisive next routes

The open object should be isolated as a **relative cell problem on the exact cusp-closing Calabi cap**, not attacked by another separated-retention argument.

Normalize
\[
\tau=\tau _0u,\qquad X=\sqrt{\tau _0}x,\qquad
Y=\sqrt{\tau _0}y,\qquad \Psi=\tau _0\psi,
\qquad \tau_0=(3c/2)^{1/3}.
\]
Then the cap is the universal metric
\[
g_C=u(dX^2+dY^2)+\frac{du^2}{q(u)}
+q(u)(d\Psi+X\,dY)^2,\qquad
q(u)=\frac23(u^2-u^{-1}),\quad u\ge1,
\]
with \(\Psi\)-period \(2\pi\). The parameter \(c\) disappears from the pointed geometry; ramification enters through the horizontal quotient lattice. Moreover,
\[
|W_C^-|^2=\frac{8}{3u^6},\qquad
\int_C|W_C^-|^2=\frac{8\pi^2}{3}e,
\]
so every degree-\(e\) component carries a universal unit-scale reservoir repeated over divisor area \(2\pi e\).

For a fixed outer collar, define
\[
j_{\rm bu}(N)=
\inf_{\substack{g\ {\rm on}\ N\#\overline{\mathbf{CP}}^2\\
g=g_C\ {\rm on\ an\ outer\ collar}}}
\int_N|\Ric_g+g|^2,
\]
and similarly \(j_{\rm h}(N)\) for a handle. The operative comparisons are
\[
j_{\rm bu}\ \text{vs.}\ 
J_{\rm CH}=8\pi^2(1-\eta_{\rm cert}),
\qquad
j_{\rm h}\ \text{vs.}\ 32\pi^2.
\]
Showing merely \(j_{\rm bu}<8\pi^2\) is insufficient: the certified CH cell is already strictly cheaper.

## 1. Compute the symmetry-breaking spin-two response

A fixed \(SU(2)_L\)-symmetric cell has no linear invariant pairing with
\[
H=W_C^-\in S^2_0\Lambda^-,
\]
but this does not imply quadratic neutrality after optimization over nonsymmetric cores. The correct perturbative expansion is
\[
J(H)=J(0)+\langle H,AH\rangle
-\langle f_H,L^{-1}f_H\rangle+O(|H|^3+|\nabla H||H|^2),
\]
where \(L\) is the DeTurck-fixed Hessian of
\[
D(g)=\int|\Ric_g+g|^2
\]
at a stationary CH-collar cell, and \(f_H\) is the forcing in the spin-two \(S^2_0\Lambda^-\) channel.

### First proof/computation object

Derive the gauge-fixed Jacobi system for spin-two tensor harmonics on the authoritative cell, with:

- regular bolt conditions;
- zero metric and first-jet perturbation at the fixed outer collar;
- the exact ASD cap curvature jet as forcing.

By isotropy, the response should reduce to one coefficient
\[
\kappa_2=\langle H,AH\rangle-\langle f_H,L^{-1}f_H\rangle.
\]

Interpretation:

- \(\kappa_2<0\): weak cap curvature makes the optimized cell cheaper; summing the response against
  \[
  \int |W_C^-|^2=\frac{8\pi^2}{3}e
  \]
  yields an \(O(\Delta)\), hence \(O(rQ)\), upper-law correction.
- \(\kappa_2>0\): the CH cell is perturbatively stable against every weak ASD environment. Any improvement must then be a finite-amplitude near-divisor phenomenon.

The Malchiodi–Malizia biharmonic interpolation provides a useful explicit check. For TT perturbations at the flat metric,
\[
\Ric'(h)=-\frac12\Delta h,\qquad s'(h)=0,
\]
so the principal quadratic part of \(D\) is
\[
D_2(h)=\frac14\int|\Delta h|^2.
\]
Their annular calculation can therefore be redone for \(D\), retaining the scalar channel, rather than inferred from their Weyl-energy theorem. Orientation and chirality for
\(\#\overline{\mathbf{CP}}^2\) must be checked explicitly.

A caveat is essential: the present CH collar lies far into the cap’s CH-like tail, where \(|W^-|\) is exponentially small. Thus this route measures tail sensitivity; it does not decide cells whose core overlaps \(u\approx1\).

## 2. Compute the exact chiral interaction before any large numerical optimization

At the divisor, \(|W_C^-|^2=8/3\). Extract the full \(3\times3\) operator
\[
W_C^-:\Lambda^-\to\Lambda^-
\]
from the existing symbolic curvature computation, including its eigenvectors relative to the complex normal and torus directions. Then evaluate the Gursky–Viaclovsky/Malchiodi–Malizia contraction with the orientation-reversed blow-up model:
\[
W^{\bar M}(p)\circledast W_C(q).
\]

This is a cheap and useful diagnostic because the connected-sum Weyl balance contains
\[
-\frac{4\pi^2}{9}a^4\lambda^2
W^{\bar M}(p)\circledast W_C(q).
\]
A positive contraction identifies a favorable chiral rotation and the alignment a finite-amplitude cell should use. It does **not** by itself prove a lower \(D\)-cost: Weyl-energy decrease can be offset by scalar and Ricci channels. Accordingly, the deliverable is the signed contraction and optimal frame, not a claim about the Einstein-defect tariff.

## 3. Build a finite-amplitude toric cap cell

Near a point of the elliptic divisor, the normal rotation and a divisor translation/rotation give a natural \(T^2\)-invariant local model. Blowing up the point is toric, while a general invariant metric need not be Kähler. Use
\[
g=h_{ab}(z)\,dz^a dz^b+
G_{ij}(z)\bigl(d\phi^i+A^i_a(z)dz^a\bigr)
          \bigl(d\phi^j+A^j_b(z)dz^b\bigr),
\]
on a two-dimensional orbit space.

Rod data should encode:

- the original divisor;
- the exceptional sphere;
- the exact Calabi outer collar.

This class permits the anisotropic core to align with a preferred eigenline of \(W_C^-\), unlike the \(SU(2)_L\)-symmetric family.

### First object

Symbolically reduce
\[
D=P+\frac14\int(s+4)^2
\]
to the orbit space, including:

1. DeTurck gauge terms;
2. smooth rod expansions at the divisor and exceptional rods;
3. exact outer-collar Cauchy data;
4. relative Euler and signature checks.

A practical progression is:

- first solve the quadratic biharmonic interpolation problem using the exact cap jet and the certified core;
- then solve the full fourth-order two-variable Euler system numerically;
- finally convert any favorable numerical profile into a rational/spectral explicit metric and certify it by interval arithmetic.

The decisive certificate is
\[
j_{\rm bu}<J_{\rm CH},
\]
not just \(j_{\rm bu}<8\pi^2\).

The analogous handle problem is potentially more important:
\[
j_{\rm h}<32\pi^2
\]
would introduce an \(r\)-dependent saving even at \(\theta=0\). Mixed blow-up–handle cells should also be compared by **ramification area consumed per unit saving**, since divisor area, not separate \(k,\ell\) counts, is the local resource.

## 4. Reformulate retention as an exact volume inequality

For a ramification region with no topology change and fixed outer collar, Step 38 gives
\[
\Delta_NB=\frac14P_N-\frac1{48}\Delta_NS.
\]
If \(s=-4\),
\[
\boxed{\Delta_NB=\frac14P_N-\frac13\Delta_NV.}
\]
Thus retention is not supplied by APS signature alone; it is equivalent to
\[
\Delta_NV\le \frac34P_N.
\]

With \(k\) blow-ups and \(\ell\) handles inserted in the region, relative Euler and signature bookkeeping instead gives
\[
\Delta B
=10\pi^2k-8\pi^2\ell+\frac14P-\frac1{48}\Delta S.
\]
Under \(s=-4\), define
\[
V_{\rm ren}=\Delta V-30\pi^2k+24\pi^2\ell.
\]
Then
\[
\boxed{\Delta B=\frac14P-\frac13V_{\rm ren}.}
\]
For a general competitor, with
\[
T=\int(s+4),\qquad Z=\int(s+4)^2,\qquad D=P+\frac14Z,
\]
the exact bookkeeping becomes
\[
\Delta B
=10\pi^2k-8\pi^2\ell+\frac14D-\frac13\Delta V
+\frac16T-\frac1{12}Z.
\]
These are the correct diagnostics for every numerical cell: reporting \(D\) alone conceals whether a claimed saving came from favorable ASD depletion or uncontrolled scalar/volume exchange.

### Perturbative retention problem

On constant-scalar variations with fixed collar, define
\[
\Lambda_C=
\sup_{\substack{DR_{g_C}h=0\\h|_{\rm collar}=0}}
\frac{V''(h)}{P''(h)}.
\]
The threshold is \(3/4\):

- \(\Lambda_C>3/4\) gives an explicit infinitesimal depletion mode;
- \(\Lambda_C<3/4\), plus gauge-fixed coercivity, proves local retention for all sufficiently small cap deformations.

Because the cap is cohomogeneity one under its nilpotent symmetries, this generalized eigenproblem separates into Fourier representations on the Heisenberg slices and radial ODEs in \(u\). Start with the translation-invariant ansatz
\[
g=a(u)^2(dX^2+dY^2)+b(u)^2du^2+
c(u)^2(d\Psi+X\,dY)^2.
\]
It cannot create a blow-up, but cheaply tests whether a coherent cap preconditioning can raise \(V_{\rm ren}\) past the \(3P/4\) threshold before surgery.

A bare Lichnerowicz spectral gap is not enough: the relevant Hessian is the constrained \(V''/P''\) problem (or equivalently the Hessian of \(P-\lambda V\)), not simply positivity of \(\Delta_L\).

## 5. Search for a divisor-localized gauge-field calibration

The cap has a natural \(L^2\) ASD representative of the zero section,
\[
F_D=u^{-2}du\wedge(d\Psi+X\,dY)-u^{-1}dX\wedge dY,
\]
up to normalization conventions. Direct symbolic checks should establish:
\[
*F_D=-F_D,\qquad dF_D=0,
\]
its fibre period, its \(L^2\)-norm, and the eigenvalue of \(W_C^-\) on the line it spans.

This gives a concrete target for a relative Weitzenböck identity:
\[
B_N(g)-\frac{8\pi^2}{3}e
+aP_N+bZ_N
=
\int_N(\text{metric squares}+\text{field squares})
+\mathcal Q_{\partial N},
\]
with \(\mathcal Q_{\partial N}=0\) for the canonical cap boundary state.

Two realizations are plausible.

### Relative Spin\(^c\) boundary problem

A level \(u=U\) is a Heisenberg nilmanifold. Compute:

- the canonical Spin\(^c\) boundary state induced by \((g_C,F_D)\);
- the APS Dirac and Chern–Simons boundary terms;
- its continuation through the disk bundle and through an interior blow-up.

The useful result would force a nontrivial interface state, preventing the closed monopole from choosing an arbitrarily cheap trace at the cap boundary.

### Paired-field vortex estimate

For classes \(c\pm E\),
\[
c_1(u)=E,\qquad f_u=\frac{f_+-f_-}{2}.
\]
The topology may be paid by amplitude loss or relative spin-direction rotation. The missing estimate is a covariant vortex inequality controlling both:
\[
\int_N\bigl(|Du|^2+\rho^2|\nabla n|^2+|f_u|^2
+\text{potential}\bigr)\ge v_e.
\]
A key algebraic check is whether the paired identity controls the full \(f_u\), not only \(f_u^+\). The boundary Dirichlet-to-Neumann operator on the nilmanifold should be included, since rotation can otherwise escape into the exterior.

Local Seiberg–Witten amplitude identities alone cannot distinguish CH from the cap: both have \(s=-4\) and the same Kähler \(W^+\) spectrum. This is not evidence that the \(r\)-loss is an artefact; it shows precisely why a **relative boundary state or divisor field** is needed. An isolated symmetric monopole ODE with prescribed CH asymptotics cannot settle this closed relative problem.

## 6. Prove transfer and packing in the actual ramified towers

A local cap result is useful only after two geometric transfer statements.

### Model convergence

For every fixed normalized slab \(1\le u\le U\), prove
\[
\bar\pi_m^*\widehat g_{\beta_m}\longrightarrow g_C
\quad\text{in }C^{q,\alpha}
\]
uniformly over selected ramification components. Biquard–Guenancia provide asymptotic bilipschitz comparison, but a certified curvature-energy cell needs at least \(C^2\), preferably \(C^{4,\alpha}\), control.

A plausible upgrade is:

1. use their bilipschitz comparison and smooth ramified lifting at the divisor;
2. establish a uniform harmonic radius on fixed normalized cap balls;
3. put both Einstein metrics in harmonic-map gauge;
4. bootstrap the elliptic Einstein equation.

### Site count

Show that a degree-\(e_c\) component contains at least
\[
\nu(U,\rho)e_c-O(1)
\]
disjoint normalized balls of radius \(\rho\) inside the slab. Since the divisor area is \(2\pi e_c\), this reduces to a uniform lower bound for the normalized divisor injectivity radius or an explicit lattice-packing estimate. This arithmetic point must be proved; area alone does not exclude thin tori.

If \(n_{\rm bu}\) blow-ups and \(n_{\rm h}\) handles are placed in cap sites, let
\[
\delta_{\rm bu}=\frac{J_{\rm CH}-j_{\rm bu}}{8\pi^2},\qquad
\delta_{\rm h}=\frac{32\pi^2-j_{\rm h}}{32\pi^2}.
\]
Then the separated construction becomes
\[
\frac{D}{8\pi^2Q}
\le
1-\eta_{\rm cert}\theta
-\delta_{\rm bu}\frac{n_{\rm bu}}Q
-4\delta_{\rm h}\frac{n_{\rm h}}Q+o(1),
\]
hence
\[
\frac{\alpha}{h}
\le
4\left(
1-\eta_{\rm cert}\theta
-\delta_{\rm bu}\frac{n_{\rm bu}}Q
-4\delta_{\rm h}\frac{n_{\rm h}}Q
\right)+o(1).
\]
Because total cap area is proportional to \(\Delta=rQ\), packing produces laws such as
\[
\frac{n_{\rm bu}}Q
\sim \min\{\theta,\nu_{\rm bu}r\},
\]
with analogous handle and mixed-cell terms. If the response density is proportional to \(|W_C^-|^2\), summation automatically yields a linear \(r\)-term through \(B_\Delta\).

## Low-value distractions

The following do not decide the problem:

- re-deriving relative signature identities without a volume or field estimate;
- any purely Kähler blow-up ansatz, whose tariff is at least \(8\pi^2\), above the certified CH cost;
- re-optimizing only the \(SU(2)_L\)-symmetric core, which cannot see the spin-two ASD channel;
- invoking strict Weyl-energy subadditivity without quantitatively evaluating \(D\) and the scalar channel;
- treating the entire cap as a small perturbation of CH—the region \(u\approx1\) is finite-amplitude;
- isolated monopole shooting with an artificial asymptotic trace;
- transferring a cell from only \(C^0\) cap comparison;
- assuming \(O(e)\) embedded sites from area without a lattice/injectivity argument.

The most informative sequence of mathematical objects is therefore:

1. the exact \(W_C^-\) eigenstructure and chiral contraction;
2. the spin-two Jacobi/Schur-complement coefficient for the certified cell;
3. the constrained volume–Ricci generalized eigenvalue \(\Lambda_C\);
4. a finite-amplitude toric blow-up/handle cell if perturbation theory is favorable or inconclusive;
5. in parallel, a relative divisor-field Weitzenböck identity;
6. the \(C^2\)-transfer and packing theorem needed to convert any local tariff into an actual \(r\)-dependent tower law.