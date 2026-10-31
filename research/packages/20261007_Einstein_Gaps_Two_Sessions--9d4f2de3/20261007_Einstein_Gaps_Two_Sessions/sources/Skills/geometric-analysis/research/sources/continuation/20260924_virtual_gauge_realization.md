# Finite-cover gauge supply and Einstein realization on the original manifold

24 September 2026. This note separates the location of the gauge-theoretic
input from the location of the exact Einstein output. The cover may have
arbitrarily large degree and diameter. We compactify the **base**, not the
cover, and do not assume that its monopole class or auxiliary form descends.
The result is a new composition in this project, not a claim of publication
priority or a solution of unrestricted Yau26.

## 1. Statements

All manifolds are closed, connected, smooth and four-dimensional. Ricci uses
tensor norms and Weyl curvature uses Hilbert–Schmidt endomorphism norms.
Write
\[
 \delta=\|\operatorname{Ric}_g^\sharp+I\|_{\infty,\mathrm{op}},
 \qquad r=\fint_M|\operatorname{Ric}_g+g|^2\le4\delta^2.
 \tag{1}
\]
For a finite covering \(\pi:N\to M\) of degree \(d\), set
\(\widetilde g=\pi^*g\), \(\widetilde V=dV\). An **actual conformal
input** on an oriented \(N\) is a specified Spin\(^c\) structure whose
ordinary unperturbed monopole equations are solvable for every metric in
\([\widetilde g]\). The structure is fixed throughout this conformal class.
For such an input in orientation \(\sigma\), define the positive harmonic
projection energy \(p_\sigma\) and
\[
 q_\sigma=\frac{1}{\widetilde V}
 \left\{\frac32\int_N(s^2+12|W^\sigma|^2)
                       -72\pi^2p_\sigma\right\}\ge0.
 \tag{2}
\]
An arbitrary cohomology class, or solvability only at one metric, is not
substituted for this input.

When the base is oriented, the cover is always given the pullback
orientation. In particular this convention fixes the chirality in
Theorem C, not just the signs in a signature formula.

**Theorem A (virtual bilateral realization).** Given \(D,A_0>0\), there
is \(\varepsilon(D,A_0)>0\) such that the following holds. Let \(M\) be
oriented, \(\operatorname{diam}(M,g)\le D\), and let an oriented finite
cover \(N\to M\) have actual conformal inputs in both orientations, with
\[
 p_+,p_->0,\qquad \frac{\max(p_+,p_-)}d\ge A_0,
 \qquad \delta+q_++q_-<\varepsilon(D,A_0).
 \tag{3}
\]
Then the **same smooth base \(M\)** admits an exact metric \(h\) with
\(\operatorname{Ric}_h=-h\), whose universal Riemannian cover is
\(\mathbb H^2_{-1}\times\mathbb H^2_{-1}\).

**Theorem B (one input above a nonorientable base).** The same conclusion
holds when \(M\) is nonorientable and an oriented finite cover has just
one actual input satisfying
\[
                    p/d\ge A_0,\qquad \delta+q<\varepsilon(D,A_0).
 \tag{4}
\]
No regularity of the covering is required in either theorem. Neither its
degree nor its diameter appears in the threshold. There is no homotopy,
class-square-cost, Ricci-derivative, or separate curvature-energy hypothesis.
Global Kähler structures on the base are **not** asserted. The exact
Riemannian output is sufficient for the adopted Yau26 existence question.

**Theorem C (virtual gauge at the Chern boundary).** Let \(M\) be oriented,
\(\operatorname{diam}(M,g)\le D\), and
\[
       A:=2\chi(M)+3\tau(M)=3(2\chi(M)-3\tau(M))>0.
 \tag{5}
\]
Suppose an oriented finite cover of any degree has one actual conformal
input with \(p\ge dA\). There is \(\varepsilon(D)>0\) such that
\(\delta<\varepsilon(D)\) implies that the same smooth base admits a
metric locally isometric to complex hyperbolic two-space, normalized by
\(\operatorname{Ric}_h=-h\) and holomorphic sectional curvature \(-2/3\).
This is a Riemannian quotient conclusion: a global complex structure on
\(M\) need not descend.

Thus gauge supply may live on a finite cover even when the base does not
admit an almost-complex structure. This does not say that Einstein existence
on an arbitrary cover automatically descends; the proofs instead construct
an exact limit on the original base.

## 2. Eliminate the auxiliary form before descending

Let \(\mathcal K\) be the orthogonal orbit in
\(\operatorname{Sym}_0(\mathbb R^3)\) with eigenvalues
\[
                          (-2/3,1/3,1/3).
 \tag{6}
\]
For a chiral Weyl operator put \(e_\sigma=\operatorname{dist}(W^\sigma,
\mathcal K)^2\). This is a scalar curvature invariant; unlike a chosen
eigenform, it is unchanged by a change of orthonormal frame.

The retained [actual-form theorem](../mathematics/current/line1_composed_application.md),
Section 2, supplies \(\omega\) with, for every arbitrarily small
\(\eta>0\),
\[
 \fint_N\bigl(|W^\sigma-A_\omega|^2+(|\omega|^2-2)^2\bigr)
       \le720\kappa_\sigma+\eta,
 \quad \kappa_\sigma=r+q_\sigma,
 \quad A_\omega=\frac12\left(\frac{|\omega|^2}{3}I-\omega\otimes\omega\right).
 \tag{7}
\]
We shrink the thresholds in Theorems A--C so that each invoked
\(\kappa_\sigma\le1/2880\), as required by that theorem. In a
contradiction sequence this holds for every sufficiently late term.
This zeroth-order statement needs no square-cost or Hessian bound.
For \(u=|\omega|^2\), the eigenvalues of \(A_\omega\) are
\((-u/3,u/6,u/6)\), including at \(u=0\). Consequently
\[
 \operatorname{dist}(A_\omega,\mathcal K)^2=(u-2)^2/6,
 \qquad e_\sigma\le2|W^\sigma-A_\omega|^2+(u-2)^2/3.
\]
Letting the smoothing allowance tend to zero gives
\[
                         \fint_N e_\sigma\le1440\kappa_\sigma.
 \tag{8}
\]
There is no need to descend \(\omega\), choose a global eigenline, or
compare classes on different covers. The only inherited analytic input
here is the actual-form theorem; (8) is its finite-dimensional consequence.

The completed-square scalar–Weyl estimate also gives
\[
 \fint_N(\sqrt6|W^\sigma|-2)^2\le2\kappa_\sigma.
 \tag{9}
\]
For any measurable \(E\subset N\),
\[
 \int_E|W^\sigma|^2\le\frac43\operatorname{Vol}(E)
                                      +\frac23\kappa_\sigma\widetilde V.
 \tag{10}
\]
The factor \(\widetilde V\) cannot be dropped on the cover. It disappears
only after the correct division by the covering degree.

## 3. Descent of energy and spectral error, with no degree loss

For an oriented base and orientation-preserving cover, natural curvature
invariants pull back. Therefore (8) and (10) give on the base
\[
 \fint_M e_\sigma\le1440\kappa_\sigma,\qquad
 \int_E|W^\sigma|^2\le\frac43\operatorname{Vol}(E)
                                      +\frac23\kappa_\sigma V.
 \tag{11}
\]
Here one applies (10) to \(\pi^{-1}E\) and divides both sides by \(d\).
Nothing about a monopole structure being deck-invariant was used.

For nonorientable \(M\), factor any connected oriented covering through
the orientation double cover \(M^{\rm or}\). Its intermediate degree is
\(d/2\). The orientation-reversing involution on \(M^{\rm or}\) is an
isometry and exchanges the two Weyl halves. Thus, with local orientations
used on the base,
\[
 \int_N e_+=\frac d2\int_M(e_++e_-),\qquad
 \int_{\pi^{-1}E}|W^+|^2=\frac d2\int_E|W|^2.
 \tag{12}
\]
The sums in these formulas are globally defined even though their labels
are not. It follows that one input on \(N\) gives
\[
 \fint_M(e_++e_-)\le2880\kappa,\qquad
 \int_E|W|^2\le\frac83\operatorname{Vol}(E)+\frac43\kappa V.
 \tag{13}
\]
This is why Theorem B needs only one gauge input. It is not an assumption
that the original class descends to \(M^{\rm or}\) or to \(M\).

The scalar monopole inequality, divided by \(d\), gives in both cases
\[
 32\pi^2A_0\le\frac1d\int_Ns_-^2
                  =\int_Ms_-^2\le16(1+\delta)^2V,
 \qquad V\ge\frac{2\pi^2A_0}{(1+\delta)^2}.
 \tag{14}
\]
Merely \(p>0\) on covers of unbounded degree would not give this lower
bound. The per-sheet budget in (3)–(4) is essential to this proof.

## 4. Compactness occurs on the base

Suppose Theorem A or B fails. Take counterexamples with fixed \(D,A_0\)
and the relevant defect tending to zero. Equation (14), bounded Ricci,
diameter, and Bishop–Gromov comparison give uniform upper and lower total
volume bounds and a uniform local lower volume ratio on the base.
Equations (11) or (13) imply
\[
 \lim_{j\to\infty}\int_{B_{\rho_j}(x_j)}|W_{g_j}|^2=0
                         \quad\hbox{whenever }\rho_j\to0.
 \tag{15}
\]
All constants are independent of the finite covers.

The harmonic-radius argument in
[bilateral realization, Section 3](20260924_bilateral_realization.md)
now applies directly to \((M_j,g_j)\), including an unoriented base:
if the minimum harmonic radius tends to zero, rescale there. Harmonic
coordinates, noncollapse and the metric equation give a complete smooth
Ricci-flat limit, with strong local \(W^{2,p}\) convergence for finite
\(p\). Equation (15) makes its Weyl curvature vanish. A complete flat
limit with Euclidean lower volume growth is Euclidean, contradicting the
normalization of the harmonic radius. This local argument uses no choice
of global orientation and no ALE classification.

There is therefore a uniform harmonic radius. A finite atlas and
subsequence give diffeomorphisms with one fixed smooth **base** \(M_\infty\)
and convergence in \(C^{1,\alpha}\), and strongly in finite \(W^{2,p}\),
to a smooth metric \(h\) with \(\operatorname{Ric}_h=-h\).
This standard argument does not assert convergence of all derivatives of
the approximate metrics. Most importantly, no compactness, bounded degree,
or equivariance theorem for the varying covers has been invoked.

## 5. Exact local geometry, without descending forms

Strong curvature convergence and (11) or (13) imply pointwise on the
smooth limit that both \(W^+\) and \(W^-\) have spectrum (6).
For an Einstein four-metric the chiral Weyl Weitzenböck identity, with
\(\Delta=\operatorname{div}\nabla\), is
\[
 \frac12\Delta|W^\sigma|^2
 =|\nabla W^\sigma|^2+\frac s2|W^\sigma|^2-18\det W^\sigma.
 \tag{16}
\]
Here \(s=-4\), \(|W^\sigma|^2=2/3\) and
\(\det W^\sigma=-2/27\). The last two terms cancel, while the left
side vanishes. Thus both Weyl halves are parallel. Equivalently one may
use Derdziński's local conformal-Kähler theorem with constant Weyl norm.

Their simple eigenlines have local parallel generators of norm \(\sqrt2\),
defining opposite-orientation parallel orthogonal complex structures
\(J_+,J_-\). They commute. The parallel symmetric involution
\(-J_+J_-\) has two rank-two eigenspaces. On the simply connected
universal cover these structures are global; completeness and de Rham
splitting give two complete simply connected surface factors. Each has
Ricci curvature \(-g\), hence Gaussian curvature \(-1\). This proves
the universal-cover conclusion in A and B. Pulling \(h\) back through
the base diffeomorphisms contradicts the chosen counterexamples and proves
the uniform thresholds.

The eigenlines can have sign monodromy on the base. Ignoring it would
incorrectly strengthen the statement to global Kähler existence.

## 6. Proof at the Chern boundary

For Theorem C, covering multiplicativity gives \(T_\pm(N)=dT_\pm(M)\).
Apply the exact balances from
[the Chern-boundary proof](20260924_chern_boundary_realization.md) upstairs:
\[
 \mathfrak D_2+72\pi^2(p-dA)+54\int_N|W^-|^2
                                  =18\int_N|\operatorname{Ric}^{\circ}|^2.
 \tag{17}
\]
Consequently \(q\le72\delta^2\) and
\(\fint_M|W^-|^2\le\delta^2\). Also \(p/d\ge A\ge1\), so (14)
gives a base volume floor independent of \(d\). The \(W^+\) estimate
(11) and the vanishing total \(W^-\) energy give base compactness just
as above. The limit has \(W^-=0\), \(\operatorname{Ric}=-h\), and
\(W^+\) spectrum (6). Equation (16) makes \(W^+\) parallel, so the
universal cover is Kähler–Einstein and Bochner-flat. It is
\(\mathbb{CH}^2\), with holomorphic sectional curvature \(-2/3\).
Again the exact metric is obtained on the base itself.

## 7. A real quotient showing why the stronger input scope matters

Let \(g,h\ge2\) be even. The oriented hyperbolic surfaces \(\Sigma_g\)
and \(\Sigma_h\) can be realized as orientation double covers of closed
nonorientable hyperbolic surfaces. Their free orientation-reversing
isometric involutions are \(\iota_g,\iota_h\). The diagonal action
\((\iota_g,\iota_h)\) on \(N=\Sigma_g\times\Sigma_h\) is free and
orientation-preserving. Put
\[
                M=N/\langle(\iota_g,\iota_h)\rangle.
 \tag{18}
\]
The product metric already descends to an exact negative Einstein metric.
Both orientations on \(N\) have compatible negative KE structures and
their canonical actual monopole inputs. Here
\[
 \chi(M)=2(g-1)(h-1),\quad \tau(M)=0,\quad
 d=2,\quad p_+=p_-=8(g-1)(h-1),\quad q_+=q_-=0.
 \tag{19}
\]
For even \(g,h\), \(\chi(M)+\tau(M)\equiv2\pmod4\). An oriented
almost-complex four-manifold has integral Todd genus
\((\chi+\tau)/4\), so this base admits **no almost-complex structure
in either orientation**. In particular the global KE conclusion of the
base-input bilateral theorem is impossible here, while Theorem A applies.
Small smooth perturbations of the base metric retain the same actual
cover inputs and have small deficits, so the input regime is not confined
to exact equality metrics. The product-cover canonical SW invariants
provide solvability for all metrics, not only the displayed product.

This quotient is a calibration example, not a newly discovered Einstein
manifold. It demonstrates the strict difference between actual gauge
supply on the base and supply on a cover, and why the output must retain
possible holonomy monodromy. A nonorientable example for B is simply the
product of a closed nonorientable hyperbolic surface and an oriented one.

## 8. Relation to the research programme and sources

The added bridge is
\[
 \begin{gathered}
 \text{actual gauge supply on a finite cover}\\
 \Downarrow\\
 \text{degree-normalized curvature information downstairs}\\
 \Downarrow\\
 \text{exact Einstein geometry on the original base}.
 \end{gathered}
\]
The unbounded degree causes no loss because the proof discards the
auxiliary form before descending and uses spectral invariants instead.
It does not assume a gauge class on the base, or silently pull an arbitrary
Einstein metric down a finite covering.

The diameter and small saturation requirements remain genuine. These
statements do not handle the large-diameter shear escape, arbitrary
collapsed input, or arbitrary gauge-free Yau26 input. Nor is the finite
cover allowed to carry an unrelated metric: it must carry \(\pi^*g\).

Primary external inputs are LeBrun's
[monopole curvature inequalities](https://arxiv.org/html/math/0003068)
and Derdziński's
[harmonic-Weyl structure and identities](https://www.numdam.org/article/CM_1983__49_3_405_0.pdf).
The compactness step and actual-form PDE are the explicitly cited retained
proof dependencies. The finite checker validates orbit distances, degree
normalizations, the Weyl cancellation, and the quotient's characteristic
numbers; it does not certify these PDE inputs or worldwide originality.
