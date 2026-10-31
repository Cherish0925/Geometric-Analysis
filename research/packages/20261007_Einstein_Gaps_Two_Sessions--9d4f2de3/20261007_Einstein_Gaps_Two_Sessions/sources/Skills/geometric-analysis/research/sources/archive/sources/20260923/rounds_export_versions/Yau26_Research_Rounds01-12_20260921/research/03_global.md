# Global Einstein geometry: connectors, closed smooth types, and exact-output constraints

## 1. The global question and its mathematical objects

The global problem is to compare two properties of the **same** closed smooth manifold:
\[
 e_\sigma(M)=\inf_g\|g^{-1}\operatorname{Ric}_g-\sigma I\|_{\infty,\mathrm{op}}=0,
 \qquad
 \mathsf N(M):\ M\text{ admits no Einstein metric}.
\]
The first property is an approximation statement; the second quantifies over every metric, scale, Einstein constant, complex structure, and symmetry class.
The project formulation of Yau26 is equivalent, in each dimension, to \(P_n^+\lor P_n^-\).
A counterexample to one sign is therefore not a counterexample to the entire interval statement.
To disprove that statement it suffices to defeat both signs in one dimension, possibly on different manifolds.
The results below concern predominantly dimension four and the negative branch.

We use \(\operatorname{Ric}=-3g\) for connector calculations and \(\operatorname{Ric}=-g\) for closed-manifold invariants.
If \(\epsilon(g)=\|g^{-1}\operatorname{Ric}_g+3I\|_\infty\), then \(\delta_-(3g)=\epsilon(g)/3\).
For curvature energies, \(|\operatorname{Rm}|_{\mathrm{full}}\) is the full four-index tensor norm; Weyl norms in Chern–Weil formulas are the Hilbert–Schmidt norms on \(\Lambda^2\).
These conventions explain the factors of four in Section 8.

The [inherited global manuscript](../baseline/research/20260916_global.tex) already contained detailed \(E_D\) constructions, their variational analysis, algebraic smoothing on specified complex surfaces, orthogonally transitive torus obstructions, and local charged connector calculations.
It also distinguished a valid local asymptotically hyperbolic flattening estimate from an invalid global gluing argument on a fixed closed graph manifold.
Those are inputs, not discoveries of the twelve rounds.
The developments collected here strengthen the connector theory, construct and identify additional closed smooth types, compute their gauge-theoretic data, and constrain every possible exact Einstein output.
“Additional” means additional to that research baseline; publication priority of the combined results has not been established.

Three families must remain separate throughout.
The original real-hyperbolic extended graph manifolds have a particular global nonexistence theory.
The new surface-product gluings have nonamenable walls and different topology; that nonexistence theory does not transfer by terminology.
The noncompact doubled-cusp metrics test analytic mechanisms but are not themselves closed Yau26 counterexamples.

## 2. Early numerical closure tests and the full charged reduction

### 2.1 Why the existing \(E_D\) inequalities did not decide existence

For the zero-signature surface bundles, put \(V_*=4\pi^2\chi(M)\).
The inherited construction approaches this volume in the \(\operatorname{Ric}=-g\) normalization.
A hypothetical Einstein metric in the previously obtained window has \(V=xV_*\), \(1<x<3\), and
\[
 \int|W^+|^2=\int|W^-|^2=V_*(1-x/3).
\]
Round 1 checked the scalar, mixed scalar–Weyl, and spectral monopole inequalities simultaneously.
Their numerical constraints remain compatible throughout this open interval; in particular
\[
 (4\sqrt{x}+\sqrt{6-2x})^2>36.
\]
The algebraic witnesses in that calculation are curvature data, not metrics.
They show that those inequalities alone do not close the global problem, not that an Einstein metric exists.
Likewise, a uniform exact-Einstein gap above \(2/3\) does not exclude a family with topological ratio \(1\); product Einstein surfaces are an immediate control.

The corresponding connector budget reads
\[
 |2w+12(1-r)|\le 8\epsilon+4\epsilon^2,
 \qquad r=V_{\mathrm{removed}}/V_N,\quad w=\fint_N|W|^2.
\]
A separated budget \(w\ge w_0\), \(r\le1+w_0/6-\kappa\) gives
\(\epsilon\ge\sqrt{1+3\kappa}-1\).
Without that separation, small error permits \(r=1+w/6+o(1)\).
This identified a genuine matching condition rather than a contradiction.
Proofs and algebraic checks: [Round 1 global analysis](../proofs/global.md).

### 2.2 The charge is a physical variable, not a removable coefficient

For a free marked \(T^2\)-action over an oriented surface \(B\), write
\[
 g=\gamma+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\quad
 G=\rho M,\quad \det M=1,\quad dA=f\,d\mu_\gamma.
\]
Here \(\rho=\sqrt{\det G}\) is the physical orbit area density.
Define
\[
 q=\rho Gf=\rho^2Mf,\qquad
 Q=\tfrac12 f^TGf=\tfrac12\rho^{-3}q^TM^{-1}q.
\]
For an exact Einstein metric, the mixed Ricci equation is \(dq=0\).
For an approximate metric it is instead the quantitative equation
\[
 \mathscr B=\rho^{-3/2}M^{-1/2}dq,\qquad
 |\mathscr B|\le2\sqrt2\,\epsilon.
\]
The weights matter: small mixed Ricci error does not mean a uniformly small coordinate derivative of \(q\).
An exact orthogonally transitive open region forces the conserved exact charge to vanish globally.
A merely flat leading conformal boundary does not.

The toral AdS soliton gives an actual counterexample to the latter inference.
For \(V(r)=r^2-m/r\), \(m=a^3\), the exact metric
\[
 \frac{dr^2}{V}+V\,d\theta^2+r^2(dx^2+dy^2),\qquad r\ge a,
\]
has a smooth bolt when the \(\theta\)-period is \(4\pi/(3a)\).
Use the same period for \(x\), and the free torus generated by
\(\partial_x+c\partial_\theta,\partial_y\), with integral \(c\ne0\).
Then \(q=(3cm,0)\), although \(Q\to0\) and the conformal infinity is flat.
The charge is carried by a subleading connection term.
This is a one-ended \(D^2\times T^2\) filling, not a two-ended connector.
Full equations and this example are in [Round 2](../proofs/round2_global.md).

For two exact outward flat hyperbolic ends, the same analysis gives, below the stated orthogonally transitive threshold,
\[
 Q_*\ge q_*(\epsilon),\qquad
 q_*(\epsilon)=\sqrt{3+\epsilon}
   \bigl(\sqrt{54-42\epsilon}-2\sqrt{12-8\epsilon}\bigr)-2\epsilon,
\]
so \(\liminf Q_*\ge9\sqrt2-12>0\).
If \(\mathcal H_*\) is the supremal least weighted transport length to a zero-charge end, with line element
\[
 \left(\frac{\rho(y)}{\rho(x)}\right)^{3/2}
 \|M(x)^{-1/2}M(y)^{1/2}\|\,ds_y,
\]
then \(Q_*\le4\epsilon^2\mathcal H_*^2\).
Consequently \(\mathcal H_*\ge\sqrt{q_*(\epsilon)}/(2\epsilon)\).
This is a genuine escape condition; a uniform defect gap requires a uniform bound on this weighted quantity.

## 3. Connector restrictions before the general exact theorem

### 3.1 Physical width is forced to diverge

Consider a smooth \((n+1)\)-dimensional bridge between two exact outward ends
\(dt^2+e^{2t}h_\pm\), where \(h_\pm\) are flat compact metrics.
Let \(L\) be the shortest physical distance between the inner exact sections.
The free-endpoint index form, including both second-fundamental-form terms, gives
\[
 0\le\int_0^L\{n(f')^2-\operatorname{Ric}(T,T)f^2\}\,ds
       -n\{f(0)^2+f(L)^2\}.
\]
If \(\operatorname{Ric}\ge-(n+\epsilon)g\), set \(k=\sqrt{1+\epsilon/n}\).
Optimization yields
\[
 k\tanh(kL/2)\ge1,\qquad
 L\ge\frac2k\operatorname{artanh}(1/k)
       \sim\log(4n/\epsilon).
\]
There is no such bridge with \(\operatorname{Ric}\ge-ng\).
For \(E=\operatorname{Ric}(T,T)+n\), a more informative signed form is
\[
 \int_0^L(-E)\cosh^2(s-L/2)\,ds\ge n(1+e^{-L}).
\]
The complete cosh model establishes sharpness for the one-sided Ricci estimate, not for the full Einstein defect.
No torus symmetry is needed here. See [Round 3 width theorem](../proofs/round3_global.md).

### 3.2 Nil curvature does not supply a cheap reversal

For a fixed compact Heisenberg quotient, allow every positive-definite matrix \(G(t)\) in
\(g=dt^2+G_{ij}(t)\sigma^i\sigma^j\), not merely a diagonal ansatz.
Put \(S=\frac12G^{-1}G'\), \(H=\operatorname{tr}S\), \(v=\sqrt{\det G}\), and
\(\mu=\ell^4/(2v^2)\), where \(\ell^2=G(Z,Z)\) for the central direction.
The slice Ricci eigenvalues are \((-\mu,-\mu,\mu)\).
If \(\|\operatorname{Ric}+\lambda g\|_{\mathrm{op}}\le\epsilon\), then
\[
 \mu\le\lambda/3+\epsilon\quad\text{at an interior maximum of }\mu,
 \qquad
 \mu\ge2\lambda-4\epsilon\quad\text{where }H=0.
\]
The complete matrix calculation includes a nonnegative central-mixing contribution.
Thus two expanding ends with \(v\to\infty\) and \(\mu\to0\) force
\(\epsilon\ge\lambda/3\).
In the flat-slice, purely radial connection class, the volume-minimum argument gives the stronger \(\epsilon\ge\lambda/2\).
A finite cover does not turn a Nil quotient into \(T^3\); making its physical bracket small does not alter its fundamental group.
See [Round 4](../proofs/round4_global.md) and its [independent sign check](../proofs/round4_global_all_sign_review.md).

### 3.3 Volume and Weyl accounting remain useful after local no-go results

On a two-ended free-\(T^2\) connector with exact outward flat ends, let \(V_D\) be the physical truncated-core volume and \(A_D\) the sum of its boundary volumes.
The cutoff-independent renormalized quantity satisfies
\[
 V_{\mathrm{ren}}=V_D-A_D/3,\qquad
 6V_{\mathrm{ren}}=\int(\operatorname{tr}E_V-Q).
\]
Hence
\[
 (6-2\epsilon)V_D+\int Q\le2A_D.
\]
With horizontal and vertical Ricci-error blocks \(E_B,E_V\), relative Chern–Gauss–Bonnet gives
\[
 \int(|W|^2-Q)
 =\int\left(\operatorname{tr}E_B+\tfrac12|E|^2-\tfrac16(\operatorname{tr}E)^2\right),
 \qquad \int|W^+|^2=\int|W^-|^2=\tfrac12\int|W|^2.
\]
These are physical four-dimensional integrals, not unweighted integrals over the quotient.
Changing the truncation changes \(A_D\), so it cannot be used as a fixed numerical budget without matching data.

There is also a symmetry-free exclusion in the nonpositive-sectional-curvature sector:
on \(\mathbb R\times T^3\) with two exact outward flat ends and \(\sec\le0\),
\(\|\operatorname{Ric}+3g\|_{\mathrm{op}}\ge3/2\).
Expanding ends keep minimizing representatives of deck transformations in a compact region; the flat-torus theorem then produces a flat three-plane.
The remaining sectional curvatures force the Ricci defect bound.
Warped approximations show sharpness in that sector.
This does not apply after allowing positive sectional curvature. Both results are proved in [Round 5](../proofs/round5_global.md).

## 4. Local extension, spectral measurements, and boundary charge

### 4.1 What the local connector calculations did and did not establish

The charged Einstein equations admit genuine analytic neck germs; local reversal is not prohibited by torus topology alone.
Round 6 further exhibited how expanding physical weights can make charge variation inexpensive in the mixed Ricci equation.
Neither fact supplies a complete connector.
For an already existing asymptotically hyperbolic Einstein end
\[
 g=dt^2+e^{2t}\gamma(t),\qquad
 \gamma(t)=h+O_{C^2}(e^{-2t}),
\]
slow interpolation over length \(L\), starting at \(T\), gives a local flattening cost
\(C(L^{-1}+e^{-2T})\).
That calculation is retained as a local estimate.
The exact free-torus two-ended source assumed by one proposed application is now excluded by Section 5.

Nor does local flattening glue expanding sections into fixed finite-volume hyperbolic cusps.
Coordinate translation cannot change the physical section size.
Keeping a longer original asymptotically hyperbolic core makes its volume diverge, whereas fixed closed four-dimensional topology and sufficiently small \(\|\operatorname{Ric}+3g\|_\infty\) give a Chern–Gauss–Bonnet volume bound.
The previous conditional “\(W\) implies a fixed closed counterexample” argument therefore remains invalid.
See [Round 6 local analysis](../proofs/round6_global.md).

### 4.2 A spectral defect measures where an approximate connector can concentrate

On a complete four-manifold with two smooth asymptotically hyperbolic ends, take the harmonic separator \(u\) with boundary values \(0,1\).
Let \(h=|du|\), \(v=h^{2/3}\), and \(d\nu=v^2dV/\int v^2dV\).
The refined Bochner inequality gives
\[
 \lambda_0+\frac23\int D\,d\nu
 \le2-\frac23\int E(n,n)\,d\nu
 \le2+\frac23\epsilon,
 \quad
 D=|\mathrm{II}^{\circ}|^2+\frac23|\nabla_{\mathrm{level}}\log h|^2.
\]
For the invariant torus reduction, \(D\ge Q\).
Thus a charged exact connector would satisfy \(\lambda_0<2\).
The later nonexistence theorem supersedes that exact existence test, but the inequality remains a quantitative statement for approximate metrics.
A pointwise peak of \(Q\), or a lower bound on its physical support volume, does not by itself bound its \(\nu\)-mass.
Proof and integrability at infinity: [Round 7 spectral analysis](../proofs/round7_spectral.md).

### 4.3 Holonomy distinguishes boundary data from their real lifts

For an exact marked annular torus quotient,
\[
 C(g)=\int_B\rho^{-1}G^{-1}\,d\mu_\gamma,\qquad
 \Delta H=C(g)q,\qquad
 q\cdot\Delta H=2\int_B\rho Q\,d\mu_\gamma.
\]
The capacity matrix \(C(g)\) is finite and positive definite for the stated asymptotically hyperbolic geometry.
Here \(H_\pm=\int A\) are real lifts in one global trivialization.
Equal torus-valued holonomies can differ by an integral relative winding and do not force \(q=0\).
The explicit countermodel in the source is a metric satisfying the mixed equation, not an Einstein filling.

For a free \(T^2\)-invariant conformal boundary, normalize its metric to
\[
 \widehat h=ds^2+M(s)(d\xi+A)^2,\qquad \det M=1.
\]
Then \(R_{\widehat h}=-\frac14\operatorname{tr}(M^{-1}M_s)^2\).
The conformal class has Yamabe sign zero precisely when \(M\) is constant, and negative sign otherwise.
This explained why nonnegative-boundary connectedness theorems did not cover all proposed data.
The corrected holonomy and Yamabe statements are in [Round 8 boundary analysis](../proofs/round8_boundary.md).
The same round's relative-end translation Jacobi fields are actual pullbacks: they are modes in boundary-pointwise-fixed gauge, not new nonisometric moduli.
Its orthogonally transitive, static, half-conformally-flat, and equal-shear exclusions are valid restricted cases now contained in the next theorem; see [Round 8 global analysis](../proofs/round8_global.md).

### 4.4 A stable essential torus is not itself an Einstein obstruction

For the invariant minimal \(T^3\) lifted from a shortest essential loop in the metric \(\rho^2\gamma\), the exact stability operator is
\[
 J_{\mathrm{inv}}\phi=-\rho^{-1}(\rho\phi')'
 +(3-Q-\tfrac32\sigma_n^2-\tfrac12e_n)\phi,\qquad \sigma=\log\rho.
\]
Here \(e_n\) is the normal shape-map energy; the full lowest eigenfunction is invariant by positivity and uniqueness.
A genuine analytic charged Einstein germ satisfies the constraint equations with \(H=0\), \(|\mathrm{II}|^2=Q\), \(R_\Sigma=-6-Q\), and \(1/4\le Q\le1\).
Its stability potential is \(3-Q\ge2\).
Thus incompressibility, charge, and strict stability are locally compatible with the Einstein equation.
Moreover \(dt^2+\cosh^2t\,h\), for the explicit negative-Yamabe torus metric \(h\) in the source, has two smooth conformal ends, \(\operatorname{Ric}\ge-3g\), and spectral bottom \(2\), but is not Einstein.
Amenable covers preserve the spectral bottom; they cannot repair a deficit by themselves.
These tests isolate the need for a genuinely global exact-equation argument.
See [Round 9 separator and covering analysis](../proofs/round9_global.md).

## 5. A full exact theorem: a free circle forces connected conformal infinity

**Theorem.** Let \(\overline M\) be compact and connected, \(\dim M=n+1\ge3\).
Suppose \(g\) is a smooth conformally compact Einstein metric on its interior with \(\operatorname{Ric}_g=-ng\).
If an isometric \(S^1\)-action extends smoothly and freely to all of \(\overline M\), then \(\partial\overline M\) is connected.
The circle bundle need not be trivial, and the conformal boundary need not have nonnegative Yamabe type.

Write the principal-circle reduction globally as
\[
 g=V^2\eta^2+h,\qquad F=d\eta.
\]
The connection form itself need not descend as a global one-form, but \(V,h,F\) do.
The exact Kaluza–Klein identities are
\[
 \operatorname{Ric}_h-V^{-1}\nabla^2V=-nh+\tfrac12V^2F_{ik}F_j{}^k,
 \qquad \Delta_hV/V=n+\tfrac14V^2|F|_{\mathrm{tensor}}^2.
\]
Construct the auxiliary static spacetime
\(\mathbf g=-V^2dt^2+h\) on \(\mathbb R\times(M/S^1)\).
Dropping the connection here is not a claim that the original Riemannian metric remains Einstein.
For a null vector \(Z=aV^{-1}\partial_t+X\), \(|X|_h^2=a^2\), the identities give
\[
 \operatorname{Ric}_{\mathbf g}(Z,Z)
 =V^2\left\{\frac{a^2}{4}|F|_{\mathrm{tensor}}^2
                 +\frac12|\iota_XF|^2\right\}\ge0.
\]
No use of the Maxwell equation or of a global gauge potential is required.

Because the action remains free at conformal infinity, \(\Omega=V^{-1}\) is a boundary defining function.
The optical metric \(k=V^{-2}h\) extends smoothly to the compact quotient.
The conformal completion of the auxiliary spacetime is exactly
\[
 \widehat{\mathbf g}=-dt^2+k.
\]
It is globally hyperbolic with timelike boundary, and each boundary component has a compact spacelike cut.
The boundary noncommunication theorem of [Galloway–Schleich–Witt–Woolgar, Theorem 2](https://arxiv.org/pdf/hep-th/9912119) applies using those cuts.
If there were two boundary components, a path in the connected compact quotient, traversed sufficiently slowly in time, would give a timelike curve between them.
This contradicts noncommunication.
Connected circle fibres preserve the number of boundary components, proving the theorem.

This removes the remaining **exact**, smooth, free-\(T^2\), two-ended asymptotically hyperbolic cylinder from the connector search, including the fully charged case.
It supersedes the corresponding open status in Rounds 6–8.
The dimension restriction is real: \(dr^2+\cosh^2r\,d\phi^2\) is a two-ended hyperbolic cylinder in dimension two.
Fixed points, singular orbits, nonsmooth compactifications, and nonsymmetric fillings are outside the theorem.
Boundary isometries do not automatically extend to the interior; extension theorems with relative-fundamental-group assumptions cannot simply be invoked for disconnected infinity.
Full proof and source-hypothesis verification: [Round 9 connector theorem](../proofs/round9_connector.md).

An independent four-dimensional argument explains the same obstruction within the charged torus equations.
Quotient by a circle with nonzero charge component and use barriers to obtain a stable compact minimal separator \(\Sigma\).
Its Jacobi operator satisfies
\[
 J_\Sigma V=-V\left(
 |\mathrm{II}|^2+\tfrac14V^2|F|_{\mathrm{tensor}}^2
                     +\tfrac12V^2|\iota_nF|^2\right).
\]
Stability tested against \(V\) forces \(F=0\) on \(\Sigma\).
The horizontal curvature component is \(q_1/(\rho G_{11})\), which cannot vanish when that conserved charge is nonzero.
The zero-charge case is orthogonally transitive.
This proof uses stable-separator existence and the full quotient equations, not a positive-Einstein-constant assumption.
See [Round 9 Riemannian proof](../proofs/round9_riemannian.md).

## 6. The approximate problem: necessary escape and actual examples

### 6.1 Separator and optical estimates retain the lost quantitative information

For an approximate marked torus connector, fix a primitive circle vector \(v\), and put
\[
 V_v^2=v^TGv,\qquad q_v=v^Tq,\qquad a_v=\rho V_v.
\]
The mixed equation gives \(|dq_v|\le2\epsilon a_v\).
A stable essential separator loop \(c_v\) satisfies
\[
 \int_{c_v}\frac{q_v^2}{a_v}\le4\epsilon\int_{c_v}a_v.
\]
If \(|q_v(p_0)|\ge q_*>0\), either some \(p\in c_v\) has \(|q_v(p)|\le q_*/2\) and \(d_{a_v^2\gamma}(p_0,p)\ge q_*/(4\epsilon)\), or
\[
 \frac{\int_{c_v}a_v}{\int_{c_v}a_v^{-1}}
       \ge\frac{q_*^2}{16\epsilon}.
\]
This is a charge-leakage versus orbit-size alternative, not conservation of an approximate charge.
No derivative bound on the Ricci error or unmentioned noncollapse enters it.
See [Round 10 invariant escape estimates](../proofs/round10_connector.md).

There is a complementary optical estimate with exact Einstein ends and error supported in a compact core.
Along a shortest optical geodesic joining the totally geodesic boundary components, let \(\Omega=V^{-1}\), \(s\in[0,\ell]\), and
\[
 A=-(n-1)\partial_s^2-\operatorname{Ric}_k(T,T).
\]
The free-boundary index form makes its Neumann ground-state eigenvalue \(\lambda\) nonnegative.
Choose its positive eigenfunction \(f\), and write
\(D=E(U,U)-E(X,X)-Q_{\mathrm{opt}}\), where \(Q_{\mathrm{opt}}\ge0\) is the twist contribution.
The defining-function equation and endpoint slopes \(1,-1\) give the exact identity
\[
 \int_0^\ell\frac{fD}{\Omega}\,ds
 =\lambda\int_0^\ell f\Omega\,ds+(n-1)\{f(0)+f(\ell)\}.
\]
Consequently
\[
 2\epsilon\int_{\mathrm{core}}\frac f\Omega\,ds
 \ge(n-1)\{f(0)+f(\ell)\}
       +\lambda\int f\Omega\,ds+\int\frac{fQ_{\mathrm{opt}}}{\Omega}\,ds.
\]
With \(\max f=1\), the physical core length \(L\) obeys
\(\epsilon L\ge\frac{n-1}{2}\{f(0)+f(\ell)\}\).
Small error therefore forces long physical length or optical ground-state localization.
The endpoint and compact-error hypotheses are part of this statement, not consequences of arbitrary Ricci pinching.
See [Round 10 optical identity](../proofs/round10_optical.md).

### 6.2 Doubled extremal Kottler cusps realize the escape

Let \((\Sigma,h_\Sigma)\) be a closed hyperbolic surface and \(\phi\) have period \(2\pi\).
For \(0<d<1/2\), set \(y=d\cosh u\) on \(\mathbb R\times S^1\times\Sigma\), and define
\[
 g_d=\frac{1+y}{3+y}\,du^2
 +\frac{y^2(y+3)}{3(y+1)}\,d\phi^2
 +\frac{(1+y)^2}{3}\,h_\Sigma.
\]
This is smooth and complete, with two fixed smooth conformal infinities represented by \(d\phi^2+h_\Sigma\).
Its exact Ricci eigenvalue errors are
\[
 -\frac{3d^2}{y(1+y)^2},\qquad
 \frac{d^2(2y+3)}{y(1+y)^2}
 \quad\text{(the latter in all three remaining directions)}.
\]
Thus
\[
 \epsilon(g_d)=\frac{d(2d+3)}{(1+d)^2}<3d.
\]
The central circle collapses, while curvature and each fixed order of its covariant derivatives remain bounded.
A fixed-region cutoff produces exact extremal Kottler ends at cost \(O(d^2)\), preserving the \(O(d)\) global defect.
Its physical error-core length is \(O(\log(1/d))\), so \(\epsilon L\to0\).
The other escape in the optical inequality is therefore essential.

Indeed the rotational Jacobi function is
\[
 w=b/a=\frac{(1+y)^{3/2}}{y\sqrt{y+3}},\qquad Aw=0,
\]
with boundary value \(1\) and zero Neumann derivative.
After normalization by \(w(d)\), the sum of its endpoint values is asymptotic to \(2\sqrt3\,d\).
The exact theorem has no uniform near-Einstein extension in this free-circle class, even with fixed topology, fixed conformal infinities, and bounded curvature.
This does not contradict the torus restrictions: \(\Sigma\) has genus at least two, and the model is not \(\mathbb R\times T^3\).
It is also noncompact, so it is not a closed Yau26 counterexample.
Proof, exact formulas, and independent coordinate Ricci calculation: [Round 10 Kottler family](../proofs/round10_kottler.md).

The variation \(d\,\partial_dg_d\) is an actual non-gauge approximate infinitesimal Einstein deformation.
It has uniformly bounded norm and linearized Einstein residual \(O(d)\).
Its distance from Lie derivatives is bounded below by
\(2+d/(d+3)-d/(d+1)\), by averaging over the central closed geodesic.
This disproves a naive uniform coercive estimate modulo diffeomorphisms, not a specified Bianchi-gauge weighted inverse theorem.
For nontrivial circle bundles over \(\Sigma\), exponential cusp asymptotics give a separate doubling construction with error
\[
 C(a_0^\beta+a_0^2+d^2/a_0^2);
\]
choosing \(d=a_0^2\) makes it small.
The closed-form error above is not asserted for those bundles.
See [Round 10 general cusp doubling](../proofs/round10_cusp_doubling.md).

## 7. Closed surface-product gluings: construction meets new topology

### 7.1 The actual closed objects and approximation

Take compact oriented surfaces \(F_v\) with nonempty boundary and negative Euler characteristic, and a closed surface \(\Sigma_g\), \(g\ge2\).
Glue blocks \(F_v\times\Sigma_g\) across paired boundaries by
\[
 (\phi,x)\longmapsto(-\phi+u_e(x),f_e(x)),
 \qquad [u_e]\in H^1(\Sigma_g;\mathbb Z),\quad f_e\in\operatorname{Diff}^+(\Sigma_g).
\]
The construction accepts arbitrary fixed mapping classes, not only isometries or commuting twists.
Slow fibre-metric variation occupies one long collar region; the shear is switched on separately where the circle is small.
This separation controls the mixed terms that a simultaneous interpolation would have to estimate.
The resulting closed metrics satisfy
\[
 \|\operatorname{Ric}_{G_\ell}+3G_\ell\|_{\mathrm{op}}
 \le C\bigl(|\log\ell|^{-1}+\ell\bigr),\qquad
 \operatorname{Vol}(G_\ell)=4\pi^2\chi(M)/9.
\]
Their sectional curvatures lie in \([-3-o(1),o(1)]\); positive-order curvature derivatives tend to zero.
There is no uniform injectivity-radius or diameter assertion.
Endpoint-fixed Moser normalization yields symplectic forms in both orientations, and the actual metrics can be chosen almost Kähler for both.
The full collar calculation is in [Round 11 closed gluing](../proofs/round11_closed_gluing.md).

Every such closed assembly is aspherical, with
\[
 \chi(M)=(2-2g)\sum_v\chi(F_v)>0,\qquad \tau(M)=0.
\]
Boundary inclusions are injective, so the universal cover is a tree of contractible spaces.
Signature additivity is across whole closed three-manifolds; no corner correction is being suppressed.
A single separating gluing is a transposed \(E_D\)-type surface bundle.
Nevertheless nonzero shear does not extend across a product block: its image of the surface factor has cyclic centralizer, whereas the original surface factor has nonabelian free centralizer.
Thus “already a bundle” and “the gluing is trivial” are different assertions.

### 7.2 A self-gluing which is not a surface bundle

Let \(M=M(h,g;u,f)\) be the self-gluing of \(F_{h,2}\times\Sigma_g\), with \(h\ge1\), \(g\ge2\), \(u\ne0\).
For \(A=\pi_1(F_{h,2})\cong F_{2h+1}\), \(\Gamma=\pi_1(\Sigma_g)\), its group is
\[
 G=\langle A\times\Gamma,t:
 tc_1t^{-1}=c_2^{-1},\
 t\gamma t^{-1}=c_2^{u(\gamma)}f_*(\gamma)\rangle.
\]
If \([f_*]\) has infinite order in \(\operatorname{Out}(\Gamma)\), \(G\) is not surface-by-surface.
To prove this, map it onto a closed hyperbolic surface group with putative surface kernel.
The commuting images of \(A,\Gamma\) cannot both be cyclic, since their kernels would contribute a commuting \(\mathbb Z^2\) in the surface kernel.
If \(A\) has nonabelian image, the shear relation again produces such a \(\mathbb Z^2\).
If \(\Gamma\) has nonabelian image, its restriction must be injective and finite index.
The stable-letter relation then makes a positive power of \(f_*\) inner, a contradiction.
This excludes every oriented surface-bundle structure, not merely the visible projections; it does not exclude one on every finite cover.

An explicit even-\(b_1\) example takes \(h=1,g=2\), primitive \(u\), and mapping-class homology action
\[
 f_*=\operatorname{diag}(H,H),\qquad H=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]
Its integral abelianization is torsion free, and
\((\chi,\tau,b_1,b_2,b^+,b^-)=(4,0,4,10,5,5)\).
A single twist with dual shear gives \((4,0,7,16,8,8)\).
The source contains exact Smith-normal-form checks and the full group argument:
[Round 11 topology](../proofs/round11_graph_topology.md).

These walls have group \(\mathbb Z\times\Pi_g\), which is nonamenable, and the fibre is not infranil.
Consequently neither the real-hyperbolic extended-graph Einstein obstruction nor an infranil-fibre graph theorem applies automatically.
The approximation theorem supplies the \(e_-(M)=0\) half of a possible counterexample, not the other half.

### 7.3 No finite cover is Kähler

For every \(f\), not just infinite-order \(f\), nonzero \(u\) implies that no finite-index subgroup of \(G\) is a compact Kähler group.
The Bass–Serre action is minimal, nonlineal, and has no fixed end.
Its kernel is contained in \(\Gamma\cap\ker u\).
For a hypothetical Kähler finite-index subgroup, the Kähler tree-action theorem supplies a map to a hyperbolic orbifold group whose finitely generated normal kernel \(N\) acts trivially on the tree.
Thus \(N\) lies in a finite-index surface subgroup of \(\Gamma\).
A finitely generated normal subgroup there is trivial or finite index.
Finite index contradicts \(u|_N=0\); triviality would make the Kähler subgroup an orbifold surface group, impossible because it contains \(\mathbb Z^2\).
The finite-index action and kernel statements are proved in [Round 11 Kähler obstruction](../proofs/round11_kahler.md), using the primary tree-action formulation cited there.

Positive Einstein constant is excluded by the infinite fundamental group; Ricci-flatness is excluded because a closed Ricci-nonnegative group is virtually abelian.
Negative Einstein metrics remain possible.
Neither absence of complex structures nor absence of Kähler finite covers is a general negative-Einstein obstruction.

## 8. Exact global invariants, the complete ordinary basic set, and symmetry

### 8.1 Sharp infima with different attainment questions

For \(M(h,g;u,f)\) as above, let \(\chi=\chi(M)\).
Both orientations have \(b^+>1\), and the symplectic canonical square is \(2\chi\).
Taubes theory and the monopole scalar estimate give
\[
 \int s^2\,dV\ge64\pi^2\chi.
\]
The rescaled family \(3G_\ell\) approaches equality with volume \(4\pi^2\chi\) and scalar curvature tending uniformly to \(-4\).
It follows that
\[
 \sigma(M)=-8\pi\sqrt\chi,\qquad
 \inf_{\operatorname{Ric}\ge-g}\operatorname{Vol}=4\pi^2\chi,
\]
\[
 \inf_g\int s^2=64\pi^2\chi,\quad
 \inf_g\int|\operatorname{Ric}|^2=16\pi^2\chi,\quad
 \inf_g\int|\operatorname{Rm}|_{\mathrm{full}}^2=32\pi^2\chi.
\]
For the Ricci-lower-bound volume estimate one uses \(s_-^2\le16\), not an upper bound on \(s^2\) in the presence of positive spikes.
Equality in the first four quantities forces a Kähler equality case, excluded here; these four extremal values are not attained by a metric.
In contrast,
\[
 \int|\operatorname{Rm}|_{\mathrm{full}}^2
 =32\pi^2\chi+4\int|\operatorname{Ric}^{\circ}|^2.
\]
Its infimum is attained **if and only if an Einstein metric exists**.
The nonattainment of the other functionals cannot be transferred to this one.
Any hypothetical normalized negative Einstein metric has volume strictly greater than \(4\pi^2\chi\).
See [Round 11 variational theorem](../proofs/round11_variational.md).

### 8.2 The actual approximation determines all ordinary basic first-Chern classes

The two symplectic structures determine \(TM=E\oplus F\).
Set \(x=e(E)\), \(y=e(F)\), \(a=x+y\), \(b=x-y\); the canonical bundle classes are \(-a,-b\).
A connection on \(E\), pulled back from the first surface and flat on boundary collars, glues across the constant transition \(-I\).
Its Euler form squares to zero, so \(x^2=0\).
Euler and Pontryagin identities give
\[
 y^2=0,\quad xy=\chi,\quad a^2=2\chi,\quad b^2=-2\chi,\quad a\cdot b=0.
\]
All products here use the first orientation; \(b\) is basic in the opposite one.

Put \(Q=2\chi\), and \(A_j=(32\pi^2)^{-1}\int s_{g_j}^2\to Q\).
For every ordinary basic class \(c\), expected dimension gives \(c^2\ge Q\), while the monopole projection estimate gives \((c_{g_j}^+)^2\le A_j\).
Therefore
\[
 c^2=Q,\qquad d(c)=0,\qquad \|c_{g_j}^-\|\to0,\qquad |a\cdot c|\le Q.
\]
Product tori in the block have square zero; adjunction kills all mixed Künneth evaluations of \(c\).
Thus \(c=ta+r\), where \(r\) lies in the kernel of restriction to the cut-open block.
Mayer–Vietoris represents that kernel by neck forms \(\rho(t)dt\wedge\theta\); its intersection form is zero.
Consequently
\[
 a\cdot c=\frac Q2(t+t^{-1}).
\]
The preceding bound forces \(t=\pm1\) and \(a\cdot r=0\).
The symplectic form and \(a\) have proportional restrictions on the neck, so \(r\) also has zero symplectic pairing.
Taubes's strict extremality theorem now forces \(c=\pm a\) **integrally**, including the remaining torsion issue.
The result is
\[
 \mathcal B(M)=\{a,-a\},\qquad \mathcal B(-M)=\{b,-b\}.
\]
This enumerates ordinary basic first-Chern classes, not every monopole class, every Bauer–Furuta invariant, or distinct Spin\(^{c}\) structures with the same Chern class.
The full proof is [Round 12 gauge calculation](../proofs/round12_global.md).

The same scalar-energy sequence and convexity give, in both orientations,
\(\alpha^2(M)=\beta^2(M)=2\chi(M)\) for the period-plane and monopole-convex-hull invariants.
The canonical class supplies the reverse inequality.
Thus the numerical monopole budget is saturated; adding its convex-hull refinement cannot raise this budget.
This is a limitation on a particular obstruction mechanism, not on all gauge-theoretic or geometric arguments.

### 8.3 Every possible Einstein metric must break all local continuous symmetry

For every smooth metric on \(M(h,g;u,f)\), the isometry group of its Riemannian universal cover is discrete.
For every Einstein metric, every germ of a local Killing field is zero.
Both statements persist for arbitrary metrics of the indicated kind on finite covers.

Here is the global mechanism.
An abelian normal subgroup intersects a vertex group trivially, since its projections would be abelian normal subgroups of nonabelian free and closed surface groups.
Every remaining nonidentity element acts hyperbolically on the Bass–Serre tree.
Commutativity produces a common axis, and normality makes it invariant under the entire group, contradicting minimal nonlineal action.
Thus the group has no nontrivial normal abelian subgroup.
A finite product cover is also impossible: a \(1+3\) product has zero Euler characteristic, and a \(2+2\) aspherical product has a Kähler finite cover.
The manifold is therefore smoothly irreducible.

Farb–Weinberger's universal-cover rigidity theorem makes a nondiscrete isometry group locally symmetric under precisely these hypotheses.
In dimension four, real hyperbolic space is excluded by the embedded \(\mathbb Z^2\), and complex hyperbolic or bidisk quotients by the virtual Kähler obstruction.
Euclidean factors are excluded by positive Euler characteristic.
Finally, Einstein analyticity and Nomizu extension turn any nonzero local Killing field into a global Killing field on the complete simply connected cover, contradicting discreteness.
See [Round 12 symmetry theorem](../proofs/round12_symmetry.md), including the finite-cover argument and primary references.

The near-Einstein sequence has local product regions and invariant collars without contradiction: its smooth local symmetries need not analytically continue.
An exact correction on the same manifold must break every such local symmetry.
This gives no positive lower bound on the size of that breaking and does not exclude a distant nonsymmetric Einstein metric.
The complementary collar calculation in [Round 12 repair analysis](../proofs/round12_repair.md) quantifies backreaction within invariant ansätze; it is not a restriction on arbitrary metrics.

## 9. Representation and harmonic-map methods: actual information and controls

### 9.1 Dehn twists can annihilate representation volume

For a single nonseparating twist bundle with fibre genus \(p\) and base genus \(q\), the group is
\(\Pi_p\rtimes\Pi_q\), with monodromy \(D(b)=ba\), \(D(a)=a\), and all other handle generators fixed.
For a target in which nonidentity centralizers are abelian, the commutation and twist relations force the image of \(a\) to be trivial.
The quotient is
\[
 (\Pi_{p-1}*\mathbb Z)\times\Pi_q.
\]
For \(\operatorname{PSL}(2,\mathbb R)^2\), this computes the maximal representation volume as
\[
 16\pi^2(p-2)(q-1).
\]
It is zero when \(p=2\).
For a twist power \(D^k\), the relation gives only \(\rho(a)^k=1\); torsion in the target cannot be ignored.
For torsion-free targets with cyclic nontrivial centralizers, the stronger factorization remains valid and every map to a closed aspherical four-dimensional target has degree zero.
In particular this blocks degree-based entropy comparison with closed strictly negatively curved targets.
Proofs: [Round 8 representation calculation](../proofs/round8_construction.md).

For \(r\) independent twists, the corresponding quotient is
\((\Pi_{p-r}*F_r)\times\Pi_q\), and the maximal product representation volume is
\[
 16\pi^2\max(p-r-1,0)(q-1).
\]
When \(p-r=0\), the \(\Pi_0\) factor is trivial, while \(F_r\) remains; no fundamental class of a sphere is inserted.
Using twists about all standard \(a_i,b_i\), with enough disjoint base collars, gives noncommuting fibre monodromy and forces the rank-one representations to factor through the base.
The product representation volume is then zero.
The slow-interpolation mechanism was inherited; these explicit quotient and representation calculations are the additional result.
See [Round 8 multitwist analysis](../proofs/round8_multitwist.md).

### 9.2 A fixed-source harmonic defect is positive, but not uniformly so by topology alone

For the actual \(E_D\), multitwist, and full-twist bundles, let \(b=\pi^*e(TB)\).
For a source metric \(G\), let \(f_h\) be the harmonic representative into a marked hyperbolic base, and define
\[
 \mathcal E_G(h)=\tfrac12\int|df_h|^2,\qquad
 \mathcal H_G=4\pi^2\|\operatorname{Harm}_G b\|^2,\qquad
 \Gamma(G)=\min_h\mathcal E_G(h)-\mathcal H_G.
\]
The minimum over Teichmüller space is attained for each fixed closed source.
The proof uses fixed-source gradient bounds, bounded generator displacements, and maximal Euler number to prevent degeneration of the target representation.
It does not assume a uniform injectivity radius for all target metrics.

For a hypothetical \(\operatorname{Ric}_G=-G\), write
\(f_h^*\omega=-2\pi\operatorname{Harm}_G b+d\nu\).
Then the exact identity is
\[
 \mathcal E_G(h)-\mathcal H_G
 =\|d\nu\|_2^2+\tfrac12\|\nabla df_h\|_2^2.
\]
Equality makes the harmonic map parallel of rank two and forces the product/finite-monodromy geometry incompatible with the actual infinite twist.
Attainment therefore gives \(\Gamma(G)>0\) for every such fixed Einstein source.
The actual area-preserving approximate family has \(\Gamma=0\).
This is a sharp structural distinction, but no uniform positive separation has been proved.
See [Round 9 harmonic analysis](../proofs/round9_bundle.md).

An exact control family shows why broad normalized separation is false.
Branched base changes of a nonisotrivial Kodaira fibration preserve its infinite monodromy image, keep positive signature fixed, and make Euler characteristic diverge.
Their ample canonical bundles give exact negative Kähler–Einstein metrics.
Writing \(V_0=4\pi^2\chi\) and \(v=1+3\tau/(2\chi)\), their values are
\[
 \mathcal E_*=V_0,\qquad \mathcal H=V_0/v,\qquad
 \Gamma=V_0(1-1/v).
\]
Hence \(v\to1\) and \(\Gamma/\operatorname{Vol}\to0\), although the absolute defect tends to \(6\pi^2\tau>0\).
These have \(\tau>0\), not the zero-signature topology of \(E_D\).
They refute an overbroad normalized gap, not an \(E_D\)-specific theorem.
See [Round 10 exact Kodaira controls](../proofs/round10_bundle.md).

## 10. Davis resolutions: topology, entropy, and the gauge-theoretic boundary

The hyperbolic Davis example has \(\chi=26\) and an involution with \(122\) isolated \(A_1\) points.
For the standard marked resolution with \(m\) positive and \(122-m\) negative exceptional spheres,
\[
 \pi_1(M_m)=1,\quad \chi(M_m)=196,\quad \tau(M_m)=2m-122,
\]
\[
 b^+=36+m,\quad b^-=158-m,\quad 2\chi+3\tau=26+6m.
\]
The actual log-Weyl construction gives \(\delta_-\to0\) and normalized limiting volume \(156\pi^2\).
For the all-negative resolution, ordinary volume entropy and simplicial volume vanish because the smooth manifold is simply connected.
The blowdown to the hyperbolic orbifold is not an ordinary nonzero-degree map to a closed hyperbolic manifold.
Passing to an orbifold cover does not produce the required smooth unbranched cover downstairs.
Branched pullback creates angle \(4\pi\); smoothing its normal disk requires a fixed negative total curvature and is not a cost-free Ricci-controlled repair.
These are concrete failures of the proposed entropy transfer, not a failure of entropy rigidity itself.
See [Round 6 entropy analysis](../proofs/round6_entropy.md).

There remains a valid conditional comparison: an ordinary nonzero-degree map to a closed hyperbolic target with sufficient target volume, together with the monopole–Chern–Weil upper volume bound, can force hyperbolic equality and contradict exceptional spheres.
The Davis resolution does not satisfy that mapping hypothesis.
The topology of the branched upstairs object, including its negative \(2\chi+3\tau\), cannot be used as an Einstein obstruction downstairs.

Concentration in the actual marked resolutions gives
\[
 \int|W^+|^2\longrightarrow12\pi^2m,\qquad
 \int|W^+|\longrightarrow0.
\]
For a monopole class \(a\), this yields \(a^2\le104/3+m\).
A special class with \(a^2\ge26+6m\) is therefore impossible for \(m\ge2\).
For \(m=0\), the only remaining numerical possibility is \(a^2=30\), expected dimension \(1\); for \(m=1\), it is \(a^2=32\), dimension \(0\).
The reversed orientation replaces \(m\) by \(122-m\).
The notes then show vanishing of all ordinary numerical Seiberg–Witten invariants and ordinary absolute \(S^1\)-equivariant Bauer–Furuta invariants in both orientations.
The all-negative Bauer–Furuta conclusion uses the specific remaining stable cohomotopy group; the positive-square-sphere cases also have direct adjunction restrictions.
No conclusion about every conceivable monopole class or family invariant is asserted.
Proof and exact invariant scope: [Round 7 topology and gauge analysis](../proofs/round7_topology.md).

Nonsymplecticity in each marking has a simpler explanation: a positive exceptional sphere invokes adjunction, while the all-negative case has \(b_1=0\), \(b^+=36\), incompatible with an almost-complex structure.
The analogous statement holds after orientation reversal.
The \(61/61\) spin marking has signature and \(\widehat A\)-genus zero, not a nonzero Dirac-index obstruction.
These data explain why familiar obstructions do not yet decide Einstein existence on these concrete approximation objects.

## 11. Nonabelian equations: connection identities, rank issues, and the corrected system

### 11.1 A published auxiliary theorem is not automatic input

Leung's nonabelian Seiberg–Witten uniformization framework supplies conclusions under an additional coupled gauge-field solution.
An ordinary monopole solution does not automatically supply that solution.
The earlier rank-one insertion encountered both a source-dual sign issue and a determinant/trace issue; neither may be removed by terminology.
The original comparison and its explicit missing transfer are recorded in [Round 7 nonabelian analysis](../proofs/round7_rigidity.md).

There are nevertheless useful global connection estimates independent of such an insertion.
For \(V=S_L^-\oplus E\), with its indefinite Hermitian block connection, set
\(\Gamma=\operatorname{diag}(I,-I)\), \(*_\Gamma B=\Gamma(*B)\Gamma\), and let \(Z\) be the trace-free graded-self-dual curvature.
For a line \(K\) in one summand, projection \(P\), total rank \(r\), \(c=c_1(V)\), and \(k=c_1(K)\),
\[
 2\pi\sqrt{\bigl((k-c/r)^+\bigr)^2}
 \le\sqrt{\frac{r-1}{r}}\,\|Z\|_2+2\|DP\|_4^2.
\]
In rank four, when \(b=2k-a\) has \(b^2=T>0\), this reads
\[
 \pi\sqrt T\le\frac{\sqrt3}{2}\|Z\|_2+2\|DP\|_4^2.
\]
A parallel line forces \(\int|Z|^2\ge4\pi^2T/3\), while \(Z=0\) forces \(\int|DP|^4\ge\pi^2T/4\).
Thus a putative solution may require genuine mixing; the estimate does not make a rank-one spinor parallel.
See [Round 8 graded connection estimate](../proofs/round8_nonabelian.md).

For the unshifted equation \(F_A^+=\tau(\phi)\), trace topology also gives
\[
 \sqrt2\,\|R\|_2+\kappa\|\sigma_1^2-\sigma_2^2\|_2
       \ge2\pi\sqrt{(a^+)^2}.
\]
Here \(R=F_A^+-\tau(\phi)\), and \(\sigma_i\) are the singular values of \(\phi\), with normalization constant \(\kappa\) specified in the source.
Full-rank conformal seeds satisfy a Dirac equation and determinant condition but retain a nontrivial curvature residual.
Negative virtual dimension alone does not rule out actual solutions.
The Chern–Weil analysis in the following round separates anti-self-dual curvature energy from rank imbalance rather than presuming either vanishes.
See [Round 9 seeds](../proofs/round9_nonabelian.md) and [Round 10 coupled energies](../proofs/round10_nonabelian.md).

### 11.2 Rank one does not mean reducible

For an everywhere rank-one spinor, write the target as \(R\oplus K\) and
\[
 A=\begin{pmatrix}a&-b^*\\b&c\end{pmatrix}.
\]
The complementary Dirac equation yields
\[
 (b\wedge b^*)^+=\frac{i}{2}|b|^2\omega_M,
\]
where \(\omega_M\) is determined by the source image line.
It does not yield \(b=0\).
Pairing the complementary curvature equation with a closed self-dual form \(\omega\), \(|\omega|^2=2\), gives
\[
 2\pi c_1(K)\cdot[\omega]
 =-\tfrac12\int|b|^2\langle\omega_M,\omega\rangle
       +\int iR_{KK}\wedge\omega.
\]
The sign and topology determine whether mixing is required, excluded, or insufficient.
This corrects the attempted shortcut from rank-one ordinary data to a reducible nonabelian solution.
Full calculation: [Round 11 rank-one analysis](../proofs/round11_rankone.md).

### 11.3 The literal Clifford block ansatz has a different, explicitly derived equation

Round 12 fixes genuine Spin\(^{c}\) bundles \(W^\pm=S_L^\pm\), determinant connection \(C\), target \(E=W^+\), and \(\phi:W^+\to E\).
For \(\Theta_j=\phi c_j\), put
\[
 Q=-\tfrac12(\Theta\wedge\Theta^*)^+,\qquad
 \mathbb D=\begin{pmatrix}\nabla_C^-&\Theta^*/\sqrt2\\
                          \Theta/\sqrt2&A\end{pmatrix}.
\]
Direct Clifford algebra on an Einstein background shows that projective graded anti-self-duality is equivalent to
\[
 D_A\phi=0,\qquad
 F_A^+=Q+\tfrac12\operatorname{tr}(Q)I_E+\tfrac12F_C^+I_E.
\]
The two central terms are essential; this is not the unshifted equation under a harmless change of constants.
The trace identity imposes harmonic projection \(\mathcal H^+(\operatorname{tr}Q)=0\).
If the actual target determinant connection equals \(C\), then \(\operatorname{tr}Q=0\) pointwise, so \(\phi^*\phi\) is scalar and a nonzero rank-one solution is impossible.
This is precisely why an unchanged ordinary monopole insertion fails.

For the trace-free block curvature \(\mathbb F_0\), graded anti-self-duality gives the positive identity
\[
 \int|\mathbb F_0|^2
 =8\pi^2c_2(V)-3\pi^2c_1(V)^2=-12\pi^2\tau(M).
\]
If \(M\) is closed and connected, \(\chi(M)>0\), and \(\tau(M)=0\), a solution of this **corrected literal system** on an Einstein metric exists exactly when the metric has constant negative sectional curvature.
Indeed the connection is projectively flat; the off-diagonal equation makes \(\phi\) parallel.
Rank zero contradicts \(\chi>0\), rank one contradicts the spinor Chern-class discriminant, and rank two forces a scalar polar factor and \(W^+=W^-=0\).
The converse is given by the constant scalar spinor on a negative space form.
The full derivation and normalization tests are in [Round 12 Clifford system](../proofs/round12_uniformization.md).

This classification has **not** been identified with every convention or intended bidisk converse in Leung's published system.
It neither refutes that paper nor proves that the requisite auxiliary fields exist on the new closed manifolds.
For \(M(h,g;u,f)\), the embedded \(\mathbb Z^2\) excludes a real-hyperbolic metric, so any hypothetical Einstein metric has no solution of this corrected auxiliary system.
Without a theorem forcing such a solution, that is not Einstein nonexistence.

A genuine Einstein control makes the distinction concrete.
General Schoen surfaces have ample canonical bundle, \(K^2=16\), \(e=8\), \(\tau=0\), \(q=4\), and negative Kähler–Einstein metrics, but are not locally symmetric.
Their ordinary canonical Seiberg–Witten invariant is nonzero.
Thus “Einstein plus ordinary monopoles plus zero signature” does not imply uniformization.
No claim of nonzero opposite-orientation invariants or of a solution of the above auxiliary system is needed for this control.
See [Round 12 Schoen control](../proofs/round12_control.md).

## 12. What the global line now determines

The exact free-circle conformal-boundary theorem completes a broad connector exclusion that was genuinely open in the early rounds.
The explicit doubled-cusp families then show why that exclusion cannot simply be made uniform for near-Einstein metrics.
The closed surface-product construction moves beyond the original bundle objects, while topology proves virtual non-Kählerness and, with infinite monodromy, absence of any surface-bundle structure.
Its sharp invariants and complete ordinary basic set identify the strength and the exhaustion of several familiar obstruction mechanisms.
The universal-cover theorem gives a global constraint on **every** possible Einstein metric: it must be negative and have no local continuous symmetry anywhere.

These conclusions connect the three research lines without identifying distinct objects or equations.
Rigidity supplies exact exclusions and constraints on equality; construction supplies actual pointwise-small-defect metrics; global topology determines which exact outputs remain possible on their smooth manifolds.
The unresolved issue for \(M(h,g;u,f)\) is a fully nonsymmetric negative Einstein metric, not a missing local torus calculation.
For the Davis resolutions it is an exact metric beyond the tested entropy and ordinary gauge obstructions.
For the nonabelian route it is a genuine auxiliary existence theorem for the correctly specified equations.
None of those questions has been settled by the results above, and no closed Yau26 branch counterexample is claimed.

The associated [coverage table](../coverage/03_global_coverage.tsv) records where each source contribution and review enters this chapter.
Source notes retain the full proofs and experiments; the chapter organizes their current mathematical consequences without replacing them.
