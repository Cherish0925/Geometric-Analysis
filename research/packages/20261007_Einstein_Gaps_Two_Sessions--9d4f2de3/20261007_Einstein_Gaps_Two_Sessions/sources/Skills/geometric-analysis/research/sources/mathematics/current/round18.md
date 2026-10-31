# Round 18: global phase modes, twisted operators, and exact-output geometry

22 September 2026.

The three lines now use different objects and reach different conclusions.
The integral argument yields scalar spectral information from actual
monopole intersections. The construction argument solves the complete
local deformation problem on finite-monodromy quotients, including a
specified nonproduct closed manifold. The positive branch obtains local
geometric restrictions on every hypothetical Einstein output on
\(\mathbb{CP}^2\#\mathbb{CP}^2\). A separate fixed-piece example settles
a false unrestricted integral extension, not the pointwise Yau problem.

Round 4 already allowed nonconstant scalar curvature in its integral
gap. Round 17 extended the realizable product-calibration estimate,
not that earlier gap. Nothing in this round changes that history.

## 1. Intersections force a cluster of scalar low modes

The [complete proof](round18_periods.md) begins with actual monopole
classes \(a_0,\ldots,a_n\) having common square
\(A\ge2\chi+3\tau\), \(A>0\). For a negative-mean-scalar metric put
\[
 \kappa=-\bar s/4,\quad
 B=\int s^2-32\pi^2A,\quad
 P=\int|\operatorname{Ric}^{\circ}|^2,\quad
 L=\int(s+4\kappa)^2,\quad
 \epsilon=\frac{B+P+L}{\kappa^2V}.
 \tag{1}
\]
The normalized intersection matrix is \(G_{ij}=a_i\cdot a_j/A\).
Its covariance relative to \(a_0\) is
\[
 \Sigma_{ij}=G_{ij}-G_{0i}G_{0j}\qquad(1\le i,j\le n).
 \tag{2}
\]
If \(\Sigma\) has at least \(r\) eigenvalues at least \(s_0>0\), then
\[
 \boxed{
 \frac{\lambda_r(g)}{\kappa}
       (s_0-160n\sqrt\epsilon)_+
       \le4n\,\frac{B}{\kappa^2V}.}
 \tag{3}
\]
The \(\lambda_r\) are positive scalar-Laplacian eigenvalues, with
multiplicity. In particular, sufficiently small \(\epsilon\) forces
at least \(r\) small eigenvalues.

The global step is not a trace estimate on a degenerating cycle.
Actual determinant curvatures compute the intersection matrix through
wedge integrals on the whole manifold. The bounded calibrating forms
from Round 17 approximately lie in one unoriented Weyl line. Their
smooth pairings have covariance close to (2), and small Dirichlet
energy. Scalar min--max then proves (3). Measurable signs are used
only to estimate the covariance; they are never differentiated.

The same argument gives a joint algebraic restriction: \(G\) lies
within \(24\sqrt\epsilon\), entrywise, of the convex hull of
\(zz^{\mathsf T}\), \(z_i=\pm1\). Pairwise Cauchy--Schwarz alone
would not give this statement.

### A concrete application outside the shear family

Let \(X_d\subset\mathbb{CP}^3\) be a smooth hypersurface, \(d\ge8\)
divisible by four, and
\[
 M_{m,d}=\#_mX_d,\qquad m=2,3,4,\qquad A=m\,d(d-4)^2.
 \tag{4}
\]
The classical Bauer--Furuta input supplies all signed canonical sums.
For one all-positive sum and the \(m\) single-sign reversals,
\[
 \Sigma=4\left(m^{-1}I-m^{-2}\mathbf1\mathbf1^{\mathsf T}\right).
 \tag{5}
\]
It has \(m-1\) positive eigenvalues \(4/m\). Thus
\[
 \epsilon\le(80m^2)^{-2}
 \quad\Longrightarrow\quad
 \boxed{\frac{\lambda_{m-1}(g)}{\kappa}
             \le2m^2\frac{B}{\kappa^2V}.}
 \tag{6}
\]
Actual metrics with \(B,P,L=O_m(1)\) and \(V\asymp A\to\infty\)
exist by a bounded-cost, four-dimensional connected-sum construction
using negative Kähler--Einstein hypersurfaces. This classical
construction makes the spectral application nonvacuous. The conclusion
applies to every sequence with the stated saturation, whether or not
its metrics display the connected-sum necks.

This is the main new deduction from the project's integral estimates:
topological pairing data determine the number of required scalar
slow modes. It does not assert that those modes are impossible.
Scalar-energy saturation is an explicit extra hypothesis; small
relative Ricci error by itself does not supply it. Nor does the
bounded-cost surgery produce small pointwise Ricci error.

## 2. A complete nonlinear test case with genuine monodromy

The [operator and deformation proof](round18_twisted_operator.md)
concerns
\[
 M=(\widetilde B\times F)/G,
 \tag{7}
\]
where both surfaces have curvature \(-3\), \(G\) acts by
orientation-preserving isometries, and its action on \(\widetilde B\)
is free. This is a closed finite-monodromy surface bundle with an
existing exact Einstein quotient metric.

Every tensor on \(M\) lifts to an invariant tensor, so the entire
Round-17 decomposition descends. The retained operator is exactly
one half of flat coefficient-bundle Laplacians over the base and
the orbifold \(F/G\). Values, conormal derivatives and orbifold jets
obey the actual monodromy. All remaining tensor sectors have gap
three and the uniformly perturbed \(L^2\)-to-\(H^2\) inverse.

This closes more than the complementary equation. At each fixed
quotient, the entire true kernel is
\[
 \mathcal T(\widetilde B)^G\oplus\mathcal T(F)^G.
 \tag{8}
\]
Equivariant hyperbolic deformations integrate it. The nonlinear
implicit-function argument therefore describes **all** nearby
normalized Einstein metrics, modulo sufficiently small diffeomorphisms,
as quotients of deformed factors. In a fixed Bianchi slice,
\[
 \inf_{\widehat g\text{ in the local Einstein family}}
 \|g-\widehat g\|_{C^{2,\alpha}}
       \le C(g_0,\alpha)\|\operatorname{Ric}_g+3g\|_{C^{0,\alpha}}.
 \tag{9}
\]
This uses the classical integrable-kernel mechanism, with the complete
kernel and actual transmission problem supplied here. It is not a
new general Einstein stability theorem.

The explicit genus-three hyperelliptic example has
\[
 \chi=8,\quad b_1=4,\quad b_2=14,\quad b_+=b_-=7,
 \tag{10}
\]
and is not diffeomorphic to a product of closed oriented surfaces.
Its kernel has dimension \(16\), rather than the covering product's
\(24\). Two genuine sign-local-system TT channels lose their
constant modes but acquire positive eigenvalues tending to zero
under a separating degeneration. Twisting therefore removes a
kernel without automatically restoring a uniform inverse.

The constants and neighborhood in (9) depend on the fixed geometry.
The finite-monodromy argument does not cover the infinite Dehn-twist
or integer-shear examples: their varying fiber projections and
commutators remain a distinct analytic problem. This round supplies
a fully solved nontrivial comparison case, not an assumed solution
on those other smooth manifolds.

## 3. Restrictions on every Einstein output on the positive test manifold

The [global proof](round18_positive.md) fixes the marked smooth
manifold \(M=\mathbb{CP}^2\#\mathbb{CP}^2\).
For any Einstein metric on \(M\), of any Einstein constant:

- no nonempty open subset is conformally Kähler in either orientation;
- no nonempty open subset is locally a Riemannian product;
- \(W^+\) has three distinct eigenvalues on a dense open set;
  the same holds for \(W^-\), unless the metric is negative
  Einstein and globally self-dual.

The last exception is retained for merely Hermitian geometry; it
does not survive the stronger local conformally-Kähler hypothesis.
The proof combines the absence of an almost complex structure in
either orientation with analyticity and Derdziński's two-eigenvalue
theorem. That theorem explicitly handles Weyl zeros. In the remaining
negative self-dual case, a local conformally-Kähler Einstein metric
would provide a local Killing field, which extends by Nomizu and is
excluded by the compact negative-Ricci Bochner identity.

There is also a precise topological restriction on the discriminant
sets \(Z_\pm\) where a Weyl half has repeated eigenvalues. Each meets
every embedded sphere of odd self-intersection. For a proper
analytic \(Z_\pm\),
\[
                         2\le\dim_{\mathbb R}Z_\pm\le3.
 \tag{11}
\]
Indeed, a simple spectrum on such a sphere would split
\(\Lambda^\pm\) into three trivial real lines, contradicting its
nonzero \(w_2\) there. Stratified transversality then gives the lower
dimension bound.

These are applications of classical structure theory to an actual
positive-input object, not new universal structure theorems. They
exclude retaining an exact conformally-Kähler or product block
unchanged on an open set. They do not exclude perturbing all pieces,
arbitrarily small symmetry breaking, generic-spectrum Einstein
metrics, or the stated negative self-dual possibility. The all-sign
existence question on this smooth manifold remains open here.

## 4. A completed boundary test for unrestricted integral rigidity

The [fixed-piece construction](round18_integral_limits.md) uses
\[
 M_j=N_j\#(S^1\times S^3),
 \tag{12}
\]
where \(N_j\) are growing finite covers of one closed real-hyperbolic
four-manifold. Degree-one Besson--Courtois--Gallot comparison and
Chern--Gauss--Bonnet exclude every Einstein metric on every \(M_j\).

Replacing one fixed-radius ball by a fixed smooth piece gives
uniformly bounded curvature derivatives and a uniform injectivity
lower bound, yet
\[
 \mathcal E(g_j)\to0,\qquad
 \|g_j^{-1}\operatorname{Ric}_{g_j}+3I\|_\infty
                         =c_\infty>0.
 \tag{13}
\]
This complete example settles the unrestricted averaged-integral
variant negatively by a classical argument. Local geometric
regularity cannot prevent dilution by unbounded volume. It neither
settles Yau26's pointwise variant nor contradicts the actual-monopole
theorem with its specified topology budget.

## 5. Research consequence

The independent mathematical questions are now better distinguished.
Multiple actual classes can impose global slow modes, so integral
structure need not stop at a pointwise curvature profile. On a
nontrivial monodromy geometry the full local Einstein equation can
be closed, but eliminating constants is not enough for uniform
thin-limit control. On the positive object, any exact output must
have genuinely different local complex geometry, not merely a
different volume.

The remaining targets are correspondingly concrete: determine when
the phase modes forced by (3) are geometrically compatible with
pointwise pinching; develop the full varying-fiber operator beyond
finite monodromy; and decide the unrestricted Einstein existence
question on the positive filling rather than only its complex
ansatzes. These are separate problems; none is replaced by (13).

No Yau26 sign branch has been resolved in this round. The work does
not assume the conjecture true or false. Classical inputs and new
deductions relative to the project are identified in the proofs;
global originality is not inferred from the independent checks.

See [verification and reproduction](round18_verification.md).
