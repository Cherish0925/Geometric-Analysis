# Step 46 — O10: the admissible finite marked block, the half-order spinor parent, and the non-reset matching law

Session S1003A01, Agent3, Execute.  The calculations are in

- `workspace/scripts/step46_o10_block_matching.py`,
- `workspace/data/step46/o10_block_matching.json`,
- `workspace/data/step46/run.log`.

This note corrects the periodic-cell formulation left at the end of Step 45.  It uses the exact Taub--NUT--AdS metric from that step, the actual positive-spinor Hessian estimate from the inherited endpoint theory, and the full mass-flux identity for the auxiliary negative spinor.  It does not solve density-free O10.  Its result is a mathematically admissible finite-block problem and two necessary matching laws that any concentration escape must satisfy.

## 1. Three fluxes must not be identified

Let \(L=\ell^{1/3}\), so that a TN core of charge \(\ell\) has its normalization/tidal boundary at radius \(R\asymp L\), and a block has four-volume \(\asymp \ell^2=L^6\).

Three different boundary quantities occur.

1. **Geometric circle degree.**  Assume the punctured block carries a globally oriented free circle action and that the proposed face identifications preserve its principal-bundle structure.  A compatible semi-free nut is then the source of one unit of the first Chern class of the free Hopf-circle bundle over the punctured orbit-space block.  If opposite faces of a one-nut block are identified periodically, their oriented contributions cancel while a small sphere around the nut still has degree \(+1\).  Stokes then gives a contradiction.  Such a circle-compatible one-nut cell cannot be genuinely periodic.  The admissible equivariant object is a finite marked block which transmits degree \(+1\) through an actual outer boundary, or a block containing explicitly described compensating nuts, anti-nuts, or bolts.  A uniform neutralizing source would change the curvature equation and is not allowed.  The present O10 estimates do not establish an exact circle action for every competitor; a nonequivariant transition can destroy the orbit-space degree description, in which case its field and geometric cost must be computed rather than called periodic TN matching.

2. **Scalar mass flux.**  For \(m=|v|^2\) and \(q=(\nabla^*\nabla-2)v\), in the convention used in Steps 44--45,
   \[
   \int_{\partial\Omega}\partial_\nu m
     =2\int_\Omega|\nabla v|^2-4\int_\Omega m
       -2\operatorname{Re}\int_\Omega\langle q,v\rangle .       \tag{1.1}
   \]
   This is not a Chern flux and can be small on a finite block even when the circle degree is one.

3. **Actual determinant/field boundary data.**  The monopole connection \(A\), positive spinor \(\Phi\), and cubic torsion \(t_\Phi\in S^-\otimes L\) have their own tangential connection, Chern--Simons/relative-degree, spinor trace, and normal derivative.  The determinant line on a topological nut ball can be trivial even though the geometric Hopf circle has degree one.  The inherited local hyperbolic examples already show that determinant relative charge and torsion index need not agree.  Therefore neither of the first two fluxes substitutes for the actual field transition data.

This distinction is essential: periodic scalar or tensor boundary conditions could cancel (1.1), but they cannot erase the unbalanced geometric circle degree.

## 2. Exact boundary scale of the TNAdS block

Use the exact negative-Einstein continuation
\[
 g_{\ell}=\frac{H}{F}dR^2+HR^2(\sigma_1^2+\sigma_2^2)
       +\ell^2\frac{F}{H}\sigma_3^2,
\quad H=1+\frac\ell R,
\quad F=1+\frac{R(R+2\ell)}3,                                  \tag{2.1}
\]
with \(\operatorname{Ric}=-g\) and \(W^+=0\).  Put
\[
 c=(3/4)^{1/3},\qquad R_L=cL,\qquad \ell=L^3 .                  \tag{2.2}
\]
At the marked outer boundary,
\[
 H-1=c^{-1}L^2,
 \qquad F-1=\frac{c^2}{3}L^2+O(L^4),                            \tag{2.3}
\]
while the leading TN field has
\[
 m=m_*\frac{R}{R+\ell},\qquad
 1-\frac m{m_*}=c^{-1}L^2+O(L^4),                               \tag{2.4}
\]
\[
 |\nabla v|^2=\frac{m_*\ell^2}{(R+\ell)^4}
       =\frac{m_*}{c^4}L^2+O(L^4),
 \qquad \partial_\nu m=O(L).                                   \tag{2.5}
\]
Thus metric and amplitude departures are order \(L^2\), the physical first derivative at the frontier is order \(L\), and the Hopf fibre is still of length \(4\pi\ell(1+O(L^2))\).  The JSON evaluates the limiting coefficients.  At \(L=0.0125\), for example,
\[
 \frac{H-1}{L^2}=1.10064,\quad
 \frac{F-1}{L^2}=0.275255,\quad
 \frac{1-m/m_*}{L^2}=1.10045,
\]
\[
 \frac{\partial_\nu m}{L}=1.91355,\qquad
 \frac{|\nabla v|^2}{L^2}=2.31745.
\]
The boundary is therefore perturbative in the metric and amplitude but not topologically neutral.

## 3. The positive-spinor parent starts at order \(L\)

On the inner TN tangent choose the parallel positive spinor \(e_1\), its parallel complement \(e_2\), and the complex coordinate \(f=x_1+ix_2\) selected by the same hyperkähler complex structure.  With
\[
 \rho_*=\frac43,
 \qquad m_*=\frac{128}{81},
 \qquad a=\frac{\sqrt{m_*}}{2\rho_*}=\frac{\sqrt2}{3},          \tag{3.1}
\]
the affine parent
\[
 \chi=a\,\overline f\,e_2                                     \tag{3.2}
\]
has linearized cubic torsion
\[
 Q_{\Phi_0}\chi=\sqrt{\frac{m_*}{2}}\,d\overline f=v_{\rm TN}.\tag{3.3}
\]
Here \(\Phi_0=\sqrt{\rho_*}e_1\).  In cell coordinates \(X=x/L\), (3.2) is \(L\chi_1(X)\), not \(L^2\chi_1\).  Hence the matched expansion begins
\[
 \boxed{\Phi=\Phi_0+L\chi_1+L^2\chi_2+\cdots .}                \tag{3.4}
\]
Its first physical derivative is order one.  The \(L\)-term is the field information that creates the order-one torsion state; dropping it destroys the tangent one is trying to extend.

The affine parent does not violate the inherited Hessian estimate.  Since \(v=\sqrt{m_*/2}\,d\bar f\),
\[
 |\nabla^2\chi|^2=\frac{2a^2}{m_*}|\nabla v|^2
                 =\frac9{32}|\nabla v|^2.                       \tag{3.5}
\]
Using the exact truncated TN energy,
\[
 \int_{B_R}|\nabla v|^2
 =8\pi^2m_*\ell^2\left(\frac R{R+\ell}\right)^2,
\]
gives the exact parent cost
\[
 \boxed{
 \int_{B_R}|\nabla^2\chi|^2
 =\frac{32\pi^2}{9}\ell^2
       \left(\frac R{R+\ell}\right)^2 .}                       \tag{3.6}
\]
This is exact on the Ricci-flat TN tangent, where the spinor frame is parallel.  On TNAdS it is the leading asymptotic contribution; the positive-spin connection supplies further lower-order/cross terms that have not been evaluated here.  A normalization block has volume \(4\pi^2\ell^2+o(\ell^2)\), so the tangent calculation (3.6) contributes the finite leading density \(8/9+o(1)\).  The core parent is compatible with the known extensive bound
\[
 V^{-1}\int|\nabla_A^2\Phi|^2\le C,                             \tag{3.7}
\]
which uses only the positive-spin curvature block and therefore does not require a bound on \(W^-\).

## 4. Independent cell resets are forbidden by the same Hessian bound

The obstruction is not the intrinsic TN parent (3.6), but resetting its order-one first derivative independently at every cell face.

### Proposition 4.1 (exact one-dimensional jet interpolation)

Among \(u\in H^2([0,L])\) with
\[
 u(0)=u_0,\quad u'(0)=p_0,\quad u(L)=u_1,\quad u'(L)=p_1,
\]
the cubic Hermite interpolant minimizes \(\int_0^L|u''|^2\), and
\[
 \boxed{
 \inf\int_0^L|u''|^2
 =\frac{12}{L^3}
   \left|u_1-u_0-\frac L2(p_0+p_1)\right|^2
  +\frac1L|p_1-p_0|^2 .}                                       \tag{4.1}
\]
This follows by solving \(u^{(4)}=0\) and substituting the unique cubic.  The formula is also checked in the Step-46 script.

For a collapsed four-dimensional cell with a controlled collar of width \(\asymp L\), an outer face has three-volume \(\asymp L^5\) (two base directions of size \(L\) and a fibre of size \(\ell=L^3\)), while the cell volume is \(\asymp L^6\).  Work in temporal/parallel gauge along the collar and compare derivatives using one common oriented normal.  If a scalar spinor component is reset to the same value at the two separated cross-sections while retaining the same nonzero normal derivative \(p\), (4.1) gives
\[
 \frac{\int_{\rm cell}|\nabla^2\Phi|^2}{\operatorname{Vol}({\rm cell})}
 \ge \frac{12|p|^2}{L^2}.                                      \tag{4.2}
\]
A macroscopic phase made from such cells violates (3.7) as \(L\to0\).  More generally, if a fraction \(\eta_L\) of cells undergo a fixed-size reset, the global bound forces \(\eta_L=O(L^2)\).  The script gives exactly `reset_energy_density * L^2 = 12` from \(4\) through \(256\) cells.

By contrast, if adjacent Cauchy data are sampled from one coherent macroscopic field, then after a common spin/gauge identification they satisfy in root-mean-square form
\[
 p_1-p_0=O(L),
 \qquad
 u_1-u_0-\frac L2(p_0+p_1)=O(L^2).                              \tag{4.3}
\]
Equation (4.1) then gives bounded Hessian density.  A common affine field has zero interpolation cost; for the smooth test \(u=\sin(2\pi x)\), the discrete Hermite energy converges to
\[
 \int_0^1|u''|^2=\frac{(2\pi)^4}{2}=779.272728272\ldots,        \tag{4.4}
\]
while the reset energy diverges like \(12L^{-2}\).

For the bundle problem, (4.3) is a slow-variation statement for corresponding cross-sections or cell centres separated by distance \(L\), after transition by the actual spin and determinant gauges.  It is not the direct gluing law across a common face: with two outward normals \(\nu_i=-\nu_j\), smooth gluing requires \(\Phi_j=G_{ij}\Phi_i\) and \(\nabla_{\nu_j}\Phi_j=-G_{ij}\nabla_{\nu_i}\Phi_i\), with the analogous gauge law for \(A^{\tan}\) and matching for \(v\).  Equation (4.3) says that the leading affine parents are not independent core parameters.  They must be restrictions of an \(H^1\)-controlled macroscopic first jet
\[
 P=\nabla_A\Phi,
 \qquad c(P)=0,                                                  \tag{4.5}
\]
with TN correctors near the nuts.  The Hessian estimate is used once as this matching constraint; it must not be added again as a new positive action on top of the torsion identities.

## 5. The raw TN field fails the normalized mass equation at leading order

Step 45's wording that the scalar sector is balanced by the Wigner--Seitz radius was too strong.  The radius balances the *desired corrected block* when its final scalar mass flux and its \(q\)-pairing are negligible.  It does not make the uncorrected TN harmonic field solve the normalized resolvent equation; on Ricci-flat TN one already has \((\nabla^*\nabla-2)v=-2v\).  Its continuation to TNAdS is a separate spinorial problem.

For the raw harmonic TN section on the Ricci-flat tangent, truncated at \(R\),
\[
 \Phi_m(R):=\int_{\partial B_R}\partial_\nu m=2E(R),
\]
\[
 E(R)=8\pi^2m_*\ell^2\left(\frac R{R+\ell}\right)^2,
 \qquad M(R)=\frac{16\pi^2}{3}m_*\ell R^3.                     \tag{5.1}
\]
Substituting these exact data into (1.1) shows that this raw profile requires
\[
 \operatorname{Re}\int_{B_R}\langle q,v\rangle
 =\frac12\{2E-4M-\Phi_m\}=-2M.                                 \tag{5.2}
\]
At the exact balance radius \(R(R+\ell)^2=3\ell/4\), one has \(2E=4M\), hence \(\operatorname{Re}\int\langle q,v\rangle=-E\).  At the asymptotic radius \(R=cL\), \(c^3=3/4\),
\[
 \operatorname{Re}\int\langle q,v\rangle=-2M
 =-8\pi^2m_*\ell^2,                                             \tag{5.3}
\]
while \(-E\) differs only by \(O(L^8)\).  This is a leading-order, not negligible, mismatch.  Numerically the pairing coefficient divided by \(\ell^2\) is \(-124.771295\), while the raw TN mass-flux coefficient tends to \(249.54259\).  Cauchy--Schwarz strengthens this to
\[
 \|q_{\rm TN}\|_2^2\ge
 \frac{|\int\langle q_{\rm TN},v_{\rm TN}\rangle|^2}{\int|v_{\rm TN}|^2}
 =4M=16\pi^2m_*L^6,                                             \tag{5.4}
\]
so the raw TN field definitely fails the desired squared-residual scale \(o(L^6)\).

The scalar-profile numbers in the Step-46 JSON must be read with their prefixes.  The TNAdS proper-normal derivative uses \(\sqrt{F/H}\), whereas the exact energy, mass and resolvent pairing just displayed are Ricci-flat TN quantities.  For the same formal scalar profile on TNAdS the scalar flux is \(F\Phi_m^{\rm TN}\); moreover, simply retaining the base one-form \(d\bar f\) gives an angular \(O(L^2)\) correction to its TNAdS norm.  No actual TNAdS negative spinor/resolvent has yet been specified.  Thus (5.3) identifies the leading TN obstruction, not the exact coefficient of a constructed TNAdS field.

Consequently the exact Einstein metric continuation solves only the metric part of the block.  A valid TNAdS field extension must change the torsion-derived auxiliary field throughout the normalization region so that
\[
 \int_{B_L}|q|^2=o(L^6),
 \qquad
 \int_{B_L}|v-t_\Phi|^2+|\nabla(v-t_\Phi)|^2=o(L^6),            \tag{5.5}
\]
and then (for a selected good block)
\[
 \int_{\partial B_L}\partial_\nu |v|^2
 =2\int_{B_L}|\nabla v|^2-4\int_{B_L}|v|^2+o(L^6).             \tag{5.6}
\]
If the corrected energy and mass retain the balance \(2E=4M+o(L^6)\), its scalar mass flux is \(o(L^6)\), even though the geometric circle degree through the same outer boundary remains one.

This is the still-uncomputed field-extension problem.  It cannot be replaced by cutting off the raw TN field.

## 6. The admissible finite marked-block problem

Let \(\mathcal B_L\) be the TNAdS nut region \(0\le R\le R_L\), together with a finite outer transition collar whose free-orbit boundary is \(Y_L\).  Do not identify its outer faces.  Record on \(Y_L\) the degree-one geometric circle fibration.

The unknowns are one actual determinant connection \(A_L\), one positive spinor \(\Phi_L\), and one bounded auxiliary section \(v_L\in S^-\otimes L\), all on the same metric and Spin\(^c\) structure.  The target equations and scales are:

### Interior actual fields
\[
 D^+_{A_L}\Phi_L=0,
 \qquad F_{A_L}^+=2i\sigma(\Phi_L),                              \tag{6.1}
\]
\[
 \Phi_L=\Phi_0+L\chi_1+L^2\chi_2+\cdots,
 \qquad \chi_1\text{ contains }(\sqrt2/3)\overline F e_2,      \tag{6.2}
\]
where \(F=X_1+iX_2\) is the cell-coordinate function; using the physical \(f=x_1+ix_2=L F\) inside \(\chi_1\) would count \(L\) twice.
\[
 t_{\Phi_L}-v_L=o_{H^1}(L^3),
 \qquad (\nabla^*_{3A_L}\nabla_{3A_L}-2)v_L=q_L,
 \qquad \|q_L\|_{L^2}=o(L^3).                                  \tag{6.3}
\]
The powers in (6.3) mean squared errors \(o(L^6)\) per block.  The complete target also requires, on selected good blocks,
\[
 \|D^-_{3A_L}v_L\|_2=o(L^3),
 \qquad \|\mathsf P_{J_+}\nabla v_L\|_2=o(L^3),                 \tag{6.3a}
\]
with the other inherited prolongation residuals at their corresponding scale.  Global normalized estimates do not automatically give these bounds on every block.

### Outer data, not periodicity

After choosing temporal/Coulomb boundary gauge, boundary trace spaces, reference trivializations, a common normal orientation, and elliptic boundary projections for the Dirac part, the output boundary record includes
\[
 \bigl(\Phi_L,\nabla_\nu^{A_L}\Phi_L,
       A_L^{\tan},v_L,\nabla_\nu^{3A_L}v_L\bigr)\big|_{Y_L},   \tag{6.4}
\]
together with

- geometric circle degree \(+1\) through \(Y_L\);
- the scalar mass flux (5.6);
- the determinant relative degree/Chern--Simons datum produced by (6.1);
- the relative index of \(t_{\Phi_L}\), if it is nonzero on \(Y_L\).

These data are outputs of the block, not freely prescribable simultaneous Dirichlet--Neumann data: the monopole system is first order modulo gauge, while the resolvent equation is second order.  Prescribing only a metric collar or a scalar Neumann value does not prescribe them.  The leading model sizes are \(\Phi-\Phi_0=O(L)\), \(\nabla_\nu\Phi=O(1)\), \(v=O(1)\), and \(\nabla_\nu v=O(L)\); since \(\operatorname{Vol}(Y_L)\asymp L^5\), their boundary \(L^2\) sizes are respectively \(O(L^{7/2})\), \(O(L^{5/2})\), \(O(L^{5/2})\), and \(O(L^{7/2})\).  No analogous scale for \(A^{\tan}\) follows before a boundary gauge and curvature control are fixed.

### Joining law for many blocks

For corresponding cross-sections or cell centres separated by distance \(L\), choose actual spin and determinant transitions \(G_{ij}\).  With derivatives expressed using one common transported normal, the transformed traces must obey the covariant analogue of (4.3):
\[
 \nabla_A\Phi_j-G_{ij}\nabla_A\Phi_i=O(L),
\]
\[
 \Phi_j-G_{ij}\Phi_i
 -\frac L2\bigl(\nabla_\nu^A\Phi_j
              +G_{ij}\nabla_\nu^A\Phi_i\bigr)=O(L^2)            \tag{6.5}
\]
in the summed/root-mean-square sense needed by (3.7).  Across an actual common face the separate smooth-gluing law with opposite outward normals stated after (4.3) applies instead.  Thus the leading parents must join as a coherent macroscopic spinor/gauge jet.  The determinant equation in (6.1) must be solved with these same transitions; inserting a neutralizing curvature background is not an admissible repair.

Finally, so long as the free oriented circle structure persists through the joining region, the transmitted geometric degrees of all finite blocks must reach a genuine macroscopic boundary or be cancelled by explicitly constructed fixed components.  A circle-compatible closed periodic collection of same-sign one-nut blocks is excluded before any PDE solve.  If the circle structure is lost, the transition itself becomes part of the geometric/field construction and its cost remains to be computed.

## 7. What has been established and what the next computation must decide

Established here:

1. Under a globally oriented free circle structure and circle-bundle-preserving face identifications, the Step-45 periodic one-nut Wigner--Seitz problem is topologically inadmissible.  The finite marked block (6.1)--(6.5), or an explicit nonequivariant/compensated transition, is the correct local object.
2. The positive-spinor parent is a half-order term \(L\chi_1\).  Its exact intrinsic TN Hessian density is \(8/9+o(1)\), so the parent itself fits the inherited extensive Hessian bound.
3. Independent order-one jet resets cost at least order \(L^{-2}\) Hessian density.  The leading spinor parents must join through common spin/gauge transitions as one slowly varying macroscopic first jet.
4. The raw TN field has an order-\(\ell^2\) resolvent mismatch (5.3).  The flux radius does not solve the normalized auxiliary equation.  A corrected torsion/resolvent field on the whole block is indispensable.

Still open:

- existence of \((A_L,\Phi_L,v_L)\) satisfying (6.1)--(6.3) uniformly on the moving block;
- whether the determinant-curvature and cubic-torsion equations permit the covariant joining law (6.5);
- whether the corrected scalar mass flux can be made \(o(L^6)\) while geometric degree one is transmitted;
- global cancellation or discharge of the sum of geometric degrees, and matching of the determinant/torsion boundary data.

The next useful PDE calculation is therefore not a periodic one-nut solve.  It is a finite-boundary solve for the exact TNAdS metric with the degree-one outer fibration and prescribed *coherent* leading jet, retaining the \(L\chi_1\) term.  Its decisive outputs are the complete Cauchy map (6.4), the leading pairing in (5.2) after correction, and the determinant/torsion relative boundary invariants.  A nonzero pairing of order \(L^6\) would be a candidate density-free payment; an \(o(L^6)\) corrected block would make the local field escape viable and move the problem to macroscopic degree transport.

A02 reply #822 independently confirms that its metric-only weighted-departure/Palais--Smale work controls neither this boundary degree nor a common leading spin/connection jet.  It identifies the same missing spinor normal-flux and connection Chern--Simons/relative-degree terms.  Thus the field matching problem above is not already contained in a metric atom theorem.
