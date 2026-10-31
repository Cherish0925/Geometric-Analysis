# Step 86: forced OT Bochner superlevels, finite-dimensional drift geometry, and the remaining localization mechanism

Session `S0910A03`, Agent3 / Execute.

> **SUPERSEDED by Step 87** for the forced-case obstruction. The superlevel Caccioppoli
> and combined W energy remain valid derivations, but the resolvent route in Step 87
> replaces the proposed Moser/spectral-gap program and gives a clean universal threshold
> δ* ≈ 0.246 without local iteration. The Fisher information bound in §8 is wrong
> (naive I(t) ≤ N/(2t)+NK/2 fails for large t); see Step 87 §4 for the corrected
> Riccati bound.

> **Correction to Step 85 §7 and its route map.** The proposed ordinary Moser closure was premature. The relevant geometric input is the finite-dimensional tensor
> \[
> \operatorname{Ric}^{4}_{f}=\operatorname{Ric}_{B}-\operatorname{Hess}\sigma-\tfrac12d\sigma\otimes d\sigma,
> \qquad f=-\sigma,
> \]
> not merely an infinite-dimensional drift-Ricci lower bound. In addition, testing the divergence term by \(\eta^2(e-k)_+\) produces an interface term \(-\int\eta^2\langle V,\nabla(e-k)_+\rangle\) that Step 85 omitted. The corrected calculation gives a useful global superlevel integral inequality and normalized local regularity, but it does not yet give the near-sharp ceiling \(e\le6+O(\delta)\).

## 1. Geometric setup and the forcing-defect conversion

On a free, orthogonally transitive \(T^2\)-region write
\[
g=\gamma_B+G_{ab}d\xi^a d\xi^b,
\qquad G=e^\sigma M,
\qquad \det M=1,
\]
where \(U:B\to SL(2,\mathbb R)/SO(2)\cong\mathbb H^2\) is represented by \(M\). Put
\[
E=\operatorname{Ric}_g+3g,
\qquad d\mu=e^\sigma d\operatorname{vol}_{\gamma_B},
\qquad L=e^{-\sigma}\operatorname{div}_{\gamma_B}(e^\sigma\nabla).
\]
Let
\[
\widehat E=G^{-1}E|_{T^2},
\qquad \widehat E_0=\widehat E-\tfrac12\operatorname{tr}(\widehat E)I.
\]
The traceless orbit Ricci equation is
\[
\boxed{
 e^{-\sigma}\operatorname{div}_{\gamma_B}
 \bigl(e^\sigma M^{-1}dM\bigr)=-2\widehat E_0.}
\tag{1.1}
\]
Under the target normalization
\[
|X|_{\mathbb H^2}^2=\tfrac12\operatorname{tr}(X^2)
\quad (X\in\mathfrak{sl}(2)\text{ symmetric}),
\]
the weighted tension \(F=\tau_\sigma(U)\) therefore obeys
\[
\boxed{|F|^2=2\operatorname{tr}(\widehat E_0^2).}
\tag{1.2}
\]
If \(\|E\|_{\mathrm{op}}\le\delta\), the eigenvalues of \(\widehat E_0\) are \(\pm a\) with \(|a|\le\delta\), hence
\[
\boxed{|F|\le2\delta.}
\tag{1.3}
\]
In conformal coordinates \(\gamma_B=e^{2\lambda}(dr^2+dz^2)\), (1.1) becomes
\[
\partial_r(e^\sigma M^{-1}M_r)+
\partial_z(e^\sigma M^{-1}M_z)
=-2e^{2\lambda+\sigma}\widehat E_0.
\tag{1.4}
\]
Thus the large factor in the flat-coordinate source is a density factor. It cancels in the invariant norm relation (1.2); the geometric tension remains \(O(\delta)\).

## 2. The correct finite-dimensional weighted curvature

Set \(f=-\sigma\), so that \(d\mu=e^{-f}d\operatorname{vol}_{\gamma_B}\) and \(L=\Delta-\nabla f\cdot\nabla\). The four-dimensional Bakry--Émery tensor on the two-dimensional base is
\[
\operatorname{Ric}^{4}_{f}
=\operatorname{Ric}_B+\operatorname{Hess}f-
\frac1{4-2}df\otimes df.
\]
Using the base block of \(E\),
\[
\operatorname{Ric}_B-\operatorname{Hess}\sigma
=-3\gamma_B+\tfrac12d\sigma^2+\tfrac12U^*h_{\mathbb H^2}+E_B,
\]
we obtain the exact cancellation
\[
\boxed{
\operatorname{Ric}^{4}_{f}
=-3\gamma_B+\tfrac12U^*h_{\mathbb H^2}+E_B
\ge-(3+\delta)\gamma_B.}
\tag{2.1}
\]
This is an effective-dimension-four curvature-dimension bound. On buffered base balls of controlled radius it supports normalized local volume comparison, doubling, Poincaré, and \(W^{1,2}\to L^4\) Sobolev estimates. They must be written using averages \(\fint_B\); multiplying \(e^\sigma\) by a small lattice quotient factor cannot change the normalized constants, whereas an unnormalized Sobolev coefficient would scale.

No source retrieved in this Step supplied the exact theorem statement needed for (2.1), so this standard implication remains a source/interface item rather than a new citation in the record. The relevant hypotheses are: a complete smooth buffered ball (or a ball compactly contained in the doubled connector), finite \(N=4\), and a radius bound through \((3+\delta)r^2\). A ball meeting the physical exit additionally needs either a controlled extension or relative boundary estimates.

## 3. Forced Bochner inequality

Let
\[
e=|dU|^2,\qquad
A_{ij}=\langle dU(e_i),dU(e_j)\rangle,
\qquad V(X)=\langle dU(X),F\rangle.
\]
The identity
\[
\langle dU,D\tau_\sigma\rangle
=\operatorname{div}_\sigma V-|F|^2
\]
and the curvature of \(\mathbb H^2\) give
\[
\frac12Le
=|DdU|^2+\operatorname{div}_\sigma V-|F|^2
+Q(A)-3e+\tfrac12|dU(\nabla\sigma)|^2+E_B:A,
\tag{3.1}
\]
where
\[
Q(A)=\tfrac12\operatorname{tr}(A^2)+2\det A
=\tfrac12e^2+\det A\ge\tfrac12e^2.
\]
Since \(E_B:A\ge-\delta e\),
\[
\boxed{
\frac12Le\ge |DdU|^2+\operatorname{div}_\sigma V-|F|^2
+\frac12e^2-(3+\delta)e.}
\tag{3.2}
\]
This weak form is useful precisely because it does not differentiate the Ricci defect.

## 4. Correct superlevel Caccioppoli inequality

Let
\[
u=(e-k)_+,
\]
let \(\eta\) be a Lipschitz cutoff compactly supported in a buffered doubled domain, and set general bounds
\[
|F|\le f_0,
\qquad \|E_B\|_{\mathrm{op}}\le b_0.
\]
The divergence term has the exact expansion
\[
\boxed{
\int\eta^2u\,\operatorname{div}_\sigma V\,d\mu
=-\int\eta^2\langle V,\nabla u\rangle d\mu
-2\int\eta u\langle V,\nabla\eta\rangle d\mu.}
\tag{4.1}
\]
The first term is absent from Step 85 because that Step integrated against \(\eta^2\), not against the superlevel test \(\eta^2u\).

Define
\[
\Psi(e)=\tfrac12e(e-6)-b_0e-f_0^2.
\tag{4.2}
\]
Using \(|V|\le f_0\sqrt e\) and Kato
\[
|\nabla e|\le2\sqrt e\,|DdU|,
\]
the total coefficient of \(\eta^2|\nabla u|^2\) before Young splitting is
\[
a_k(e)=\frac12+\frac{u}{4e}=\frac{3e-k}{4e}
\in[1/2,3/4).
\tag{4.3}
\]
For every \(0<\theta<1\), a nonsingular form of the estimate is
\[
\boxed{
\begin{aligned}
&(1-\theta)\int a_k(e)\eta^2|\nabla u|^2
+\int\eta^2u\Psi(e)\\
&\quad\le
\frac1{4\theta}\int a_k(e)^{-1}
|\eta V-u\nabla\eta|^2
+2\int\eta u\langle V,\nabla\eta\rangle.
\end{aligned}}
\tag{4.4}
\]
A convenient coarser consequence is
\[
\boxed{
\frac14\int\eta^2|\nabla u|^2
+\int\eta^2u\Psi(e)
\le3\int\bigl(\eta^2 f_0^2e+u^2|\nabla\eta|^2\bigr).}
\tag{4.5}
\]
The source on the right is \(f_0^2e\,1_{\{e>k\}}\), not \(f_0^2u\). It remains nonzero as \(u\downarrow0\), which is the analytic cost of a merely \(C^0\)-small tension.

The positive root of \(\Psi\) is
\[
\boxed{k_*=3+b_0+\sqrt{(3+b_0)^2+2f_0^2}.}
\tag{4.6}
\]
If \(u=e-k_*\), then the reaction factorizes exactly as
\[
\boxed{u\Psi(e)=S u^2+\tfrac12u^3,
\qquad S=\sqrt{(3+b_0)^2+2f_0^2}.}
\tag{4.7}
\]
For \(b_0=\delta\) and \(f_0=2\delta\),
\[
k_*=6+2\delta+\frac43\delta^2+O(\delta^3).
\tag{4.8}
\]
All algebraic identities in (4.2)--(4.8), including the forcing norm conversion, are reproduced by `workspace/scripts/step86_forced_caccioppoli_verify.py`; its JSON output has zero residual in every symbolic check.

## 5. What small exit data do give

Suppose the center is smoothly doubled and the exit trace satisfies \(e<k_*\). Then \(u=(e-k_*)_+\) vanishes on the true outer boundary, so one can take \(\eta\equiv1\). Formula (4.4), with a fixed Young split, gives
\[
\boxed{
\frac14\int|\nabla u|^2
+S\int u^2+\frac12\int u^3
\le f_0^2\int_{\{u>0\}}(k_*+u).}
\tag{5.1}
\]
Consequently,
\[
\boxed{
\frac14\int|\nabla u|^2
+\frac S2\int u^2+\frac12\int u^3
\le
\left(f_0^2k_*+\frac{f_0^4}{2S}\right)
\mu(\{u>0\}).}
\tag{5.2}
\]
After division by the superlevel measure, this says that the mean-square and mean-cube excess on its own support are \(O(\delta^2)\) and \(O(\delta^2)\), respectively. It is stronger than a global small-energy statement because the right side scales with the same superlevel set.

It is nevertheless not a pointwise ceiling. A local Moser estimate on a buffered ball has the form
\[
\operatorname*{ess\,sup}_{B_r}u
\le C\left(\fint_{B_{2r}}u^2\right)^{1/2}
+C\,\mathcal F(f_0,k_*,r),
\tag{5.3}
\]
and still needs a normalized local seed. Formula (5.2) does not control \(\fint_{B_{2r}}u^2\) if the superlevel component occupies a tiny fraction of that ball or if a tiny weighted ball contains almost all of a superlevel component. Local normalized inequalities do not by themselves propagate small exit data through a long connector.

## 6. Radius-scale local regularity and why it is not yet the center contradiction

Combining (4.5) with normalized \(CD(-(3+\delta),4)\) local doubling/Sobolev and a De Giorgi superlevel iteration plausibly yields the scale-correct bound
\[
\boxed{
\sup_{B_r}e\le C\bigl(1+\delta+r^{-2}\bigr),}
\tag{6.1}
\]
for \(B_{2r}\) compactly contained in the doubled free-OT domain. TTCS supplied a candidate iteration, but the returned branches disagreed on whether its no-seed version was fully justified; therefore (6.1) is retained here as the strongest supported local regularity target, not promoted beyond the displayed hypotheses without a source-level proof of the nonlinear iteration.

Even if (6.1) is established, its constant need not lie below the forced center floor
\[
\langle e(0,\cdot)\rangle_\mu\ge12-8\delta.
\tag{6.2}
\]
The \(r^{-2}\) term is genuine. On a Euclidean two-ball, the scalar model
\[
e\equiv H>6,
\qquad V(x)=-\frac{\frac12H(H-6)-f_0^2}{2}x
\tag{6.3}
\]
satisfies
\[
\operatorname{div}V-f_0^2+\tfrac12H(H-6)=0,
\]
and \(|V|\le f_0\sqrt H\) whenever
\[
R\le\frac{2f_0\sqrt H}{\frac12H(H-6)-f_0^2}.
\tag{6.4}
\]
Thus arbitrarily high constant energy is compatible on a sufficiently small ball; a local conclusion must retain a radius or outer-data scale. This is a scalar weak-model obstruction to the *argument*, not a constructed OT connector.

## 7. The actual concentration mechanism

Pointwise Bernstein comparison cannot use only \(|F|\le2\delta\), because (3.1) in nondivergence form contains \(\langle dU,DF\rangle\). Along a target geodesic, a local scalar jet can satisfy
\[
\psi'(0)=A,
\qquad \psi''(0)=0,
\qquad \psi'''(0)=-\tfrac12A^3.
\tag{7.1}
\]
At the center of this jet,
\[
e=A^2,
\qquad \nabla e=0,
\qquad F=0,
\qquad \langle dU,DF\rangle=-\tfrac12e^2,
\tag{7.2}
\]
so the derivative of a small-amplitude tension can cancel the quartic reaction in a layer whose thickness decreases like \(\delta A^{-3}\). This illustrates a realizable local high-frequency forcing mechanism. It has not been embedded into the full coupled OT equations, constraints, reflection, and exit matching.

The precise remaining analytic question is therefore not “does ordinary Moser apply?” It is one of the following equivalent global-localization problems:

1. prove a length-independent Green/resolvent estimate for the massive drift operator on the actual doubled connector that converts (5.2) into a normalized local bound;
2. prove that each connected component of \(\{e>k_*\}\) has enough weighted inradius or volume density to prevent a thin layer;
3. derive additional regularity for \(F=-2\widehat E_0\) from the full coupled OT equations (not merely Bianchi) that excludes \(C^0\)-small, \(C^1\)-large orbit defect layers;
4. or construct a constraint-compatible layer, showing how a small defect actually transports the center energy to the tail.

## 8. A useful exact benchmark: the round cusp has a global spectral gap

For
\[
\gamma_B=dr^2+e^{2r}dz^2,
\qquad \sigma=2r,
\qquad d\mu=e^{3r}dr\,dz,
\]
\[
L=\partial_{rr}+3\partial_r+e^{-2r}\partial_{zz}.
\tag{8.1}
\]
For radial Dirichlet test functions on \([-R,R]\), conjugation \(\phi=e^{-3r/2}y\) gives
\[
\int e^{3r}|\phi_r|^2dr
=\int\left(|y_r|^2+\frac94|y|^2\right)dr.
\tag{8.2}
\]
Hence
\[
\boxed{\lambda_1(-L)\ge\frac94+\frac{\pi^2}{4R^2},}
\tag{8.3}
\]
with the angular energy nonnegative. The gap tends to \(9/4\), rather than zero, as the connector length grows. `workspace/scripts/step86_weighted_cylinder_spectrum.py` records this exact benchmark numerically.

This suggests a more promising next theorem than raw local Moser: derive a comparable weighted spectral or massive-resolvent estimate from the coupled area equation on an approximate connector. A mere \(CD(K,4)\) lower bound does not encode (8.3); the exponential area growth does. If the gap survives the forced coupled geometry, it may propagate the global superlevel estimate (5.2) without a length loss. If it fails, the failure describes the geometric bottleneck or concentration region a construction must exploit.
## 9. A coupled orbit--area energy that may close the spectral circle

The area trace equation gives an additional scalar relation that the local scalar countermodels do not satisfy. If
\[
T=\operatorname{tr}_{\rm orb}E,
\]
then
\[
\boxed{L\sigma=6-T.}
\tag{9.1}
\]
Let \(X=|\nabla\sigma|^2\). The weighted scalar Bochner formula and (2.1) give
\[
\frac12LX
=|\operatorname{Hess}\sigma|^2-3X
+\frac12X^2+\frac12A(\nabla\sigma,\nabla\sigma)
+E_B(\nabla\sigma,\nabla\sigma)
-\langle\nabla\sigma,\nabla T\rangle.
\tag{9.2}
\]
The derivative of the trace defect can be kept in divergence form:
\[
-\langle\nabla\sigma,\nabla T\rangle
=-\operatorname{div}_\sigma(T\nabla\sigma)+T(6-T).
\tag{9.3}
\]
For any \(c>0\), define
\[
W=e+cX,
\qquad J=V-cT\nabla\sigma.
\tag{9.4}
\]
Adding (3.1) and \(c\) times (9.2), retaining all positive Hessian and stress terms, and using \(\|E\|_{\rm op}\le\delta\), yields the coarse but closed structural inequality
\[
\boxed{
\frac12LW\ge \operatorname{div}_\sigma J
+\frac{W^2}{2(1+c)}-(3+\delta)W
-D_c(\delta)+\mathcal P,}
\tag{9.5}
\]
where the exact nonnegative remainder can be taken as
\[
\mathcal P=|DdU|^2+c|\operatorname{Hess}\sigma|^2+\det A
+\frac{1+c}{2}A(\nabla\sigma,\nabla\sigma)
+\frac{c}{2(1+c)}(e-X)^2,
\]
and one may take
\[
D_c(\delta)=12c\delta+4(c+1)\delta^2.
\tag{9.6}
\]
The quadratic coefficient follows from the exact minimization
\[
\frac12e^2+\frac c2X^2
\ge\frac{(e+cX)^2}{2(1+c)}.
\tag{9.7}
\]
Moreover
\[
|J|\le2(1+\sqrt c)\delta\sqrt W.
\tag{9.8}
\]
The vertical eigenvalue relation \(|T|+|F|\le2\delta\) sharpens this to
\[
|J|\le2\delta\max\{1,\sqrt c\}\sqrt W,
\tag{9.8a}
\]
and also improves the coarse constant \(D_c\), though the coarser version is sufficient for the structural argument. The retained Hessian terms additionally imply
\[
|DdU|^2+c|\operatorname{Hess}\sigma|^2
\ge\frac{|\nabla W|^2}{4W}
\quad(W>0).
\tag{9.8b}
\]
For \(c=1/2\), the zero-defect reaction threshold is \(W=9\), while the reflected center still satisfies \(\langle W\rangle\ge\langle e\rangle\ge12\). The perturbed positive root has expansion
\[
k_{1/2}=9+5\delta+\frac89\delta^2+O(\delta^3),
\tag{9.9}
\]
leaving an order-three center gap at \(\delta=0\). This does not by itself defeat the divergence field \(J\), but it incorporates the area equation into the same nonlinear object rather than treating \(e\) on an arbitrary weighted base.

There is also a conditional route from \(W\) to the exact-cusp-type spectral gap. If \(W\le B\), then \(|\nabla\sigma|\le\sqrt{B/c}\), while (9.1) gives \(L\sigma\ge6-2\delta\). For every smooth relatively compact set \(\Omega\), weighted divergence gives
\[
(6-2\delta)\mu(\Omega)
\le\int_{\partial\Omega}\langle\nabla\sigma,\nu\rangle d\mu_{\partial}
\le\sqrt{B/c}\,\mu_{\partial}(\partial\Omega).
\tag{9.10}
\]
Thus, for \(\delta<3\), the **Dirichlet/compact-support** weighted Cheeger constant would obey
\[
h_{\mu,\mathcal D}\ge(6-2\delta)\sqrt{c/B},
\qquad
\lambda^{\rm Dir}_1(-L)\ge\frac{c(6-2\delta)^2}{4B}.
\tag{9.11}
\]
This is not a Neumann spectral lower bound; constants make the Neumann bottom zero. Domains meeting the physical exit must include that face in their weighted perimeter and boundary flux. On a regular superlevel component \(\Omega_t\Subset\mathcal D\), the same argument avoids a global \(B\) and gives the layer estimate
\[
P_\mu(\Omega_t)\ge(6-2\delta)\sqrt{c/t}\,\mu(\Omega_t).
\tag{9.12}
\]
This exposes a nonlinear bootstrap rather than a free spectral assumption: a bound for the combined energy creates a length-independent Dirichlet gap, and the layer estimate (9.12) is available before a global bound. The bootstrap is still circular at the pointwise level: the spectral lower bound decays like \(B^{-1}\), and a coarse scalar model on the cusp can balance an \(O(H^2)\) high plateau by a divergence field of size \(O(\delta\sqrt H)\) in a layer of thickness \(O(\delta H^{-3/2})\). Such a layer has large perimeter-to-volume ratio and does not violate (9.12). It is not yet a genuine OT solution because it need not realize \(A=U^*h\), \(F=-2\widehat E_0\), integrability, constraints, or exit matching. The missing step is to show that the gradient coercivity, layer expansion, target-map integrability, and horizontal Einstein constraints jointly exclude this layer, or to construct all of them compatibly. The algebra is verified in `workspace/scripts/step86_combined_orbit_area_energy.py` and `workspace/data/step86_combined_orbit_area_energy.json`, and independently checked in `trace/ttcs/results/step86_ttcs02_verifier1_integration.md`.


## 10. Boundary and scope

- The reflected center is an interior set only when the metric, \(U\), \(\sigma\), and defect extend smoothly under reflection.
- Interior cutoffs require \(B_{2r}\Subset\Omega^{\mathrm{dbl}}\).
- A ball meeting the exit needs either a controlled extension or \(u=0\) at the exit; otherwise both \(\partial_\nu e\) and \(V(\nu)\) boundary fluxes appear.
- The forcing theorem concerns free, orthogonally transitive \(T^2\)-regions. Approximate twist is not removed by the exact reflection twist argument, and a general graph-manifold metric need not possess OT symmetry.
- Even a universal small-defect obstruction in this class would not settle the negative branch, the positive branch, or Yau 26.

## 11. Reproducible evidence

- `workspace/scripts/step86_forced_caccioppoli_verify.py`
- `workspace/data/step86_forced_caccioppoli_verify.json`
- `workspace/scripts/step86_weighted_cylinder_spectrum.py`
- `workspace/data/step86_weighted_cylinder_spectrum.json`
- `workspace/scripts/step86_combined_orbit_area_energy.py`
- `workspace/data/step86_combined_orbit_area_energy.json`
- `trace/ttcs/results/step86_ttcs01_generator1_integration.md`
- `trace/ttcs/results/step86_ttcs01_verifier1_integration.md`
- `trace/ttcs/results/step86_ttcs02_verifier1_integration.md`

The TTCS branches agreed on the forcing conversion, finite-dimensional curvature tensor, omitted superlevel interface term, natural root \(k_*\), and the insufficiency of an ordinary local Moser statement for a near-sharp ceiling. One generator branch asserted a stronger no-seed local iteration and another asserted a Keller--Osserman closure; the verifier branches rejected a universal near-sharp conclusion from the present inputs. This note retains only the common derivation and marks the stronger local bound as an explicit theorem target.
