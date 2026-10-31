# Explicit near-Einstein bridges and the geometry of their degeneration

21 September 2026.

The principal result of this continuation is a complete two-ended
approximate Einstein metric with a sharp, explicit global error formula.
It supplies an actual geometric realization of an escape that the exact
connector theorem leaves open. A second construction retains nonzero
circle-bundle topology. Quantitative obstructions and exact Einstein
control families identify which proposed extensions fail and which
information a closed-manifold argument still needs.

Throughout the connector analysis,
\[
\epsilon(g)=\|g^{-1}(\operatorname{Ric}_g+3g)\|_{\infty,\mathrm{op}}.
\]
For the negative branch in the project normalization,
\(\delta_-(3g)=\epsilon(g)/3\). The pointwise operator norm is used
on the whole manifold, not only on compact subsets or in a weighted
space. The new two-ended manifolds are noncompact; this distinction
cannot be removed by rescaling.

## 1. A full geometric realization of vanishing defect

Fix a closed hyperbolic surface \((\Sigma,h_\Sigma)\) with curvature
\(-1\), and a circle coordinate of period \(2\pi\). For
\(0<d<1/2\), let \(y=d\cosh u\). On the fixed manifold
\(\mathbb R\times S^1\times\Sigma\), define
\[
g_d=\frac{1+y}{3+y}\,du^2
 +\frac{y^2(y+3)}{3(y+1)}\,d\phi^2
 +\frac{(1+y)^2}{3}\,h_\Sigma.
\tag{1}
\]
The metric is smooth at its central neck and complete at both
ends. Its two conformal boundary representatives are both
\(d\phi^2+h_\Sigma\), independent of \(d\). The exact Ricci error is
\[
\boxed{\epsilon(g_d)=\frac{d(2d+3)}{(1+d)^2}<3d\longrightarrow0.}
\tag{2}
\]
All fixed covariant derivative orders of curvature remain bounded.
Only the circle radius at the neck collapses, asymptotically as \(d\).

The construction starts from the classical extremal hyperbolic-horizon
Kottler metric. Modifying only its radial coefficient creates a smooth
reflection surface while retaining exact formulas for every Ricci block.
There is also a fixed-cutoff version that equals the exact Kottler
metric on both outer ends. Its global error is \(O(d)\), and its error
region has physical length \(O(\log(1/d))\).

The [full proof](round10_kottler.md) contains the metric, smooth
compactification, all Ricci eigenvalues, the continuous supremum, cutoff
errors and uniform curvature estimates. Two independent symbolic routes
agree: warped-product formulas and direct coordinate Christoffel/Ricci
calculation. The supremum in (2) is proved analytically, not estimated
from a finite sample.

Within the free-circle class, the preceding exact boundary-connectedness
theorem excludes an exact Einstein metric with two conformal ends.
Thus exact exclusion is compatible with arbitrarily small pointwise
defect, even at fixed topology, fixed conformal infinities and bounded
full curvature. This resolves that approximate-versus-exact question
for this class. It does not exclude nonsymmetric Einstein fillings.

The parameter variation is also informative. In fixed \(u\)
coordinates, \(h_d=d\partial_d g_d\) obeys
\[
\|h_d\|_\infty=2,\qquad
\|D(\operatorname{Ric}+3g)_{g_d}h_d\|_\infty<9d.
\]
Its distance from all infinitesimal diffeomorphisms is at least
\(2+d/(d+3)-d/(d+1)\), as follows by integrating on the central
closed geodesic. This is a genuine non-gauge approximate deformation;
it is not a claim about a gauge-fixed or decaying inverse problem.

## 2. Nontrivial circle bundles permit the same kind of escape

Let \(P_\ell\to\Sigma\) have fixed Chern number \(\ell\).
An exact Einstein metric with one conformally compact end and one
surface-cusp end can be doubled deep in its cusp. With a fixed connection
\(\theta\) and \(h=h_\Sigma/3\), the central metric is
\[
dt^2+d^2\cosh^2(\sqrt3t)\theta^2+h.
\tag{3}
\]
For \(d\theta=f\,dA_h\), its complete error spectrum is
\[
0,\quad a(t)^2f^2/2,\quad-a(t)^2f^2/2,\quad-a(t)^2f^2/2,
\qquad a(t)=d\cosh(\sqrt3t).
\]
Cut at circle radius \(a_0\), and join to the exact source on collars
of fixed proper width. If the exact cusp has relative covariant
\(C^2\) error \(O(e^{-\beta r})\), the global bound is
\[
\boxed{\epsilon(g_{a_0,d})
\le C\left(a_0^\beta+a_0^2+d^2/a_0^2\right).}
\tag{4}
\]
Taking \(d=a_0^2\) makes every term vanish. Both conformal ends remain
unchanged exact Einstein ends; the smooth manifold is always
\(\mathbb R\times P_\ell\). The relative two-jet estimate uses
bounded connection coefficients in the collapsing frame, not an
injectivity-radius-dependent inverse estimate.

Li--Liu's [Theorem 1.5 and Definition 1.2](https://arxiv.org/html/2605.25462v1)
provide the exact sources for all \(\ell\). Their existence theorem
is the external input; the doubling and its error estimate are the
deduction made here. The [complete argument](round10_cusp_doubling.md)
handles the global connection, fixed bundle identification and all
transition errors. It does not apply unchanged to AH torus or ACH Nil
cusps: their collapsing directions and curvature balance differ.

## 3. Quantitative rigidity and its realized limits

### Optical boundary cost

For a free-circle metric \(g=V^2\eta^2+h\), set
\(k=V^{-2}h\), \(\Omega=V^{-1}\). Along a shortest optical path
between conformal boundaries, let \(f>0\) be the Neumann ground state
of \(- (n-1)\partial_s^2-\operatorname{Ric}_k(T,T)\), normalized
by \(\max f=1\). Under the smooth exact-end assumptions in the
[optical theorem](round10_optical.md), the error-region length \(L\)
satisfies
\[
\epsilon L\ge\frac{n-1}{2}\bigl(f(0)+f(\ell)\bigr).
\tag{5}
\]
The full identity retains a nonnegative ground-state eigenvalue term
and a nonnegative twist term. It measures signed vertical-minus-horizontal
Ricci error, rather than merely scalar curvature.

The explicit family (1) realizes ground-state localization. Here
the eigenvalue is zero and
\[
f(0)+f(\ell)=\frac{2d\sqrt{d+3}}{(1+d)^{3/2}}
\sim2\sqrt3d,
\qquad \epsilon L=O(d\log(1/d))\to0.
\]
Thus (5) cannot yield a uniform gap without additional geometric
control. This is now demonstrated by an actual metric, not just by
the possibility that a constant in the proof might degenerate.

### Variable charge and topological flux

For a marked free \(T^2\) connector, write
\(\rho=\sqrt{\det G}\), \(q=\rho Gf\), and choose a primitive
circle \(v\). Put \(V_v^2=v^{\mathsf T}Gv\),
\(a_v=\rho V_v\), \(q_v=v^{\mathsf T}q\).
The actual mixed Ricci equation and a stable quotient separator give
\[
|dq_v|\le2\epsilon a_v,\qquad
\int_c q_v^2/a_v\le4\epsilon\int_c a_v.
\tag{6}
\]
Therefore a fixed nonzero core charge requires either inverse-error
weighted transport length or divergent separator orbit scale. A small
Ricci error does not conserve the exact Einstein charge.

For a general stable circle-quotient separator with nonzero Chern
number \(m\), a different, genuinely topological estimate is
\[
\epsilon\ge
\frac{\pi^2m^2}{(\int V^2)(\int V^{-4})}.
\tag{7}
\]
The nontrivial bundle construction (3) realizes its allowed escape:
the area stays fixed, \(V=d\) at the center, and the denominator
diverges as \(d^{-2}\). Its positive twist contribution is exactly
balanced by the vertical Ricci error. The [connector proof](round10_connector.md)
keeps variable torus charge and integral Chern number distinct.

## 4. Two controls on the closed surface-bundle strategies

### Infinite monodromy does not give a normalized harmonic gap

Branched base changes of a fixed nonisotrivial Kodaira fibration give
actual closed negative Kähler--Einstein surfaces with fixed fibre genus,
the same infinite monodromy image, and fixed positive signature
\(\tau_m=2\tau_0\), but Euler characteristic \(c_m\to\infty\).
Both orientations have the required symplectic monopole classes.

For the intrinsic harmonic/Hodge functional of round 9, put
\(V_0=4\pi^2c_m\), \(v=\operatorname{Vol}/V_0\). Exact calculation
gives
\[
v=1+\frac{3\tau_m}{2c_m},\qquad
E_*=V_0,\qquad H=V_0/v,\qquad \Gamma=V_0(1-1/v).
\]
Consequently \(\Gamma/\operatorname{Vol}\to0\), despite actual
Einstein existence and unchanged infinite monodromy image. The absolute
\(\Gamma\) tends to a positive constant; it does not tend to zero.
The [construction and calibration proof](round10_bundle.md) show why
any proposed argument for the zero-signature Dehn-twist examples must
use their specific structure, not replace it by these weaker conditions.

### Full-rank coupled seeds cannot be repaired by a small final step

For the actual full-target nonabelian curvature equation
\(F_A^+=\tau(\phi)\), Chern--Weil theory gives
\[
\|(F_A^-)_{0}\|_2^2
=8\pi^2c_2(E)+\tfrac12\|\operatorname{tr}F_A^-\|_2^2
 +6\kappa^2\int\det(\phi^*\phi).
\tag{8}
\]
On \(E=\mathbb C\oplus K^{-1}\), \(c_2(E)=0\).
A uniformly full-rank spinor therefore needs definite anti-self-dual
nonabelian curvature energy. The balanced slow-interpolation seeds
from round 9 have small ASD curvature but a nonvanishing averaged
residual in the missing traceless-curvature equation. Small critical
connection and \(L^4\)-spinor changes cannot remove that residual.

The [full calculation](round10_nonabelian.md) also constructs the source
connection with exactly harmonic determinant curvature using an explicit
compact primitive; no uniform inverse Hodge estimate is assumed.
Rank-one seeds remain regular for the Dirac correction, but escape the
determinant obstruction. The full rank-one curvature equation, its
published sign convention, and a connection to arbitrary Einstein
existence are not resolved by this calculation.

## 5. What these results change for Yau26

The strongest gain is constructive: an exact global obstruction now has
explicit arbitrarily accurate approximate geometries on the same
noncompact topology, including nonzero circle-bundle degree. This proves
that bounded curvature and fixed boundary topology do not repair the
missing compactness. The optical identity explains the escape rather
than incorrectly ruling it out.

The closed-manifold step remains different. In particular no proposed
closed completion can retain this global circle isometry while keeping
\(\epsilon<3\). On a closed manifold a Killing field satisfies
\[
\int|\nabla K|^2=\int\operatorname{Ric}(K,K).
\]
Strictly negative Ricci curvature forces \(K=0\). Thus any use of the
new neck in a closed construction must break its symmetry outside the
neck and match genuine exterior data; it cannot simply identify the
two conformal infinities. The earlier fixed-topology volume and global
Einstein-nonexistence requirements also remain in force.

Three consequential questions remain:

1. Can an appropriate shrinking-circle neck be inserted into a closed
   geometry with compatible end data and a genuine all-Einstein
   topological obstruction, without introducing order-one Ricci error?
2. Does the full torus-ended approximate connector problem admit an
   escape compatible with both (5) and (6), or is there a new obstruction
   specific to the flat quotient? The negatively curved surface in
   (1)--(3) cannot simply be replaced by a torus.
3. On the actual zero-signature Dehn-twist bundles, what extra geometric
   identity distinguishes them from the exact Kodaira control family,
   or makes a rank-one gauge-theoretic approach effective?

These are mathematical continuations, not assumed outcomes. Neither
unrestricted four-dimensional sign branch, nor complete Yau26, is
settled here. The classical exact inputs are cited in the proofs;
priority for the derived constructions has not been established.

All work is in this local research repository. Installed Skills, user
Sessions, model settings and services were not changed. Exact calculation
commands and their scope are in [the verification record](round10_verification.md).
