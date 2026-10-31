# Constructing full-rank Dirac and determinant-curvature seeds on the actual surface bundles

21 September 2026.

This note constructs full-rank fields solving the Dirac and
determinant-curvature equations on the actual near-Einstein surface
bundles. It identifies the remaining traceless-curvature equation
and computes the negative deformation index of the full system on
`E=W=S_L^+`. The target determinant connection is allowed to vary;
the background spin-c connection stays fixed and may be harmonic.
The construction is not a solution of the remaining equation and
does not decide Einstein existence on these bundles.

## 1. Equation and normalization-independent algebra

Fix a closed oriented Riemannian four-manifold `X`, a spin-c structure
with determinant `L`, and the prescribed background unitary connection
on `L`. Put

\[
 a=c_1(L),\qquad W=S_L^+,\qquad E=W,\qquad
 \phi\in\Gamma\operatorname{Hom}(W,E).
\]

The unknown `A` is a full unitary connection on `E`. Leung's equations are

\[
 F_A^+=\tau(\phi),\qquad D_A\phi=0.                       \tag{1}
\]

The spinor underlying the Dirac operator has determinant `L^{-1}`;
the bundle on which `A` acts has determinant `L`. The quadratic map
projects the spinor factor to its trace-free part, but does **not**
project the `E` factor to its trace-free part. See the published
[Leung paper, p. 21](https://archive.ymsc.tsinghua.edu.cn/pacm_download/60/582-2000_Leung_NonAbelian_SW_eqt_on_Einstein_mfd_Crelle_Journal.pdf).

Write `Herm_0(W)` for the real rank-three bundle of trace-free Hermitian
endomorphisms. The tensor projection defines a fixed real linear
isomorphism

\[
 \mathcal T:\operatorname{Herm}_0(W)\longrightarrow i\Lambda^+,
 \qquad \operatorname{tr}_E\tau(\phi)
       =\mathcal T\big((\phi^*\phi)_0\big).              \tag{2}
\]

This defines `T` using the actual equation, including its Clifford
identification; it does not assign a sign by comparison with ordinary
Seiberg--Witten notation. Equivariance gives a positive constant
`kappa`, determined by that normalization, such that

\[
 |\operatorname{tr}_E\tau(\phi)|
       =\kappa\,|\sigma_1^2-\sigma_2^2|,                \tag{3}
\]

where `sigma_1,sigma_2` are the singular values of `phi`. Equivalently,
`kappa` is the norm of the trace of the quadratic map of a unit rank-one
homomorphism. In the normalization in which Clifford multiplication
on two-forms has Hilbert--Schmidt norm `|rho(omega)|=2|omega|` and
the tensor projection has coefficient one, `kappa=1/(2 sqrt(2))`.
All statements below are valid with the intrinsic definition (3).

For completeness, contraction of the projected tensor against a
trace-free source matrix `K` gives, up to the fixed source transpose
and Clifford identifications,

\[
                       K\longmapsto\phi K\phi^*.       \tag{4}
\]

In particular this map has real rank three whenever `phi` is invertible.
Taking its target trace gives (2). Neither statement depends on the
overall Clifford sign or a positive rescaling of `phi`.

## 2. Every conformal full-rank field has a curvature residual

For an arbitrary pair, not assumed to solve either equation, set
`R=F_A^+-tau(phi)`. Chern--Weil theory and harmonic projection give

\[
 \boxed{\quad
 \sqrt2\|R\|_2+\kappa\|\sigma_1^2-\sigma_2^2\|_2
       \ \ge\ 2\pi\sqrt{(a^+)^2}.
 \quad}                                                    \tag{5}
\]

Indeed the harmonic self-dual projection of `tr F_A` represents
`-2 pi i a^+`, its norm is `2 pi sqrt((a^+)^2)`, and
`|tr R|<=sqrt(2)|R|`. Apply the triangle inequality and (3).

Consequently a solution must have

\[
 \int_X(\sigma_1^2-\sigma_2^2)^2
       \ge {4\pi^2\over\kappa^2}(a^+)^2.               \tag{6}
\]

In particular, for **every** conformal full-rank field `phi=fU`, with
`f>0` and `U` unitary, and for **every** connection `A`,

\[
 \boxed{\quad\int_X|F_A^+-\tau(fU)|^2
                   \ge 2\pi^2(a^+)^2.\quad}           \tag{7}
\]

There is no parallel-field assumption in (5)--(7). This excludes the
scalar identity ansatz even after changing its connection to solve
the Dirac equation. For the canonical spin-c class on the actual
surface bundles, `a^2=T=2 chi>0` and the metrics of
[round8_multitwist.md](round8_multitwist.md) have volume `2 pi^2 T`.
Thus their averaged residual in (7) is at least one. These are actual
metrics on the same fixed smooth objects, not an algebraic substitute.

If one insists on the induced spin connection and `phi=f Id`, the
Dirac equation itself gives `df=0`: the identity is parallel, and
Clifford multiplication by a nonzero real covector is invertible.
This last restriction disappears when the connection is allowed to vary.

## 3. The Dirac equation has genuine full-rank flexibility

Let `H` be any smooth positive definite Hermitian endomorphism of `W`.
Relative to a reference unitary connection `A_0` on `E`, write `A=A_0+B`.
The Dirac equation is linear and algebraic in `B`:

\[
 D_AH=D_{A_0}H+\mathcal L_H(B),\qquad
 \mathcal L_H(B)=\sum_{j=0}^3 B_jHc_j.                  \tag{8}
\]

Here compatible local spin frames may be chosen so that the right
Clifford matrices are `c_0=I,c_j=i sigma_j`, where `sigma_j` are the
Pauli matrices. Changes of signs, transpose convention, or orthonormal
spin frames do not change the ranks below.

**Lemma 1 (the two connection maps).** At `H=diag(x,y)`, `x,y>0`:

1. `L_H:T* tensor u(2) -> Hom_C(S_L^-,E)` is surjective as a
   real linear map of dimensions `16 -> 8`.
2. Restricted to `T* tensor su(2)`, it is surjective precisely when
   `x!=y`. Its dimensions are then `12 -> 8`, with kernel dimension four.
3. At `x=y`, the traceless-connection map has rank four. In the
   displayed frames its image is the real quaternionic plane
   `span_R{I,i sigma_1,i sigma_2,i sigma_3}`.

**Proof.** Expand `B_j` in the real basis
`iI,i sigma_1,i sigma_2,i sigma_3`, using row-major real and imaginary
matrix entries as target coordinates. The columns numbered
`(0,1,2,3,4,5,8,12)` have determinant

\[
                         -2xy(x^2+y^2)^3\ne0.           \tag{9}
\]

For the traceless basis `i sigma_1,i sigma_2,i sigma_3`, the columns
`(0,1,2,3,4,5,8,11)` have determinant

\[
                         -(x-y)^4(x+y)^4.              \tag{10}
\]

At `x=y`, products of quaternionic matrices stay quaternionic, and
the three `B_0` columns and the product `(i sigma_1)c_1=-I` span that
four-dimensional plane. This also proves the asserted rank drop. The
checker recomputes these minors and ranks exactly. QED.

The frame-invariant smooth right inverse of a surjective bundle map is
`L_H^*(L_H L_H^*)^{-1}`. Therefore (8) has a smooth global solution
`B=-L_H^*(L_H L_H^*)^{-1}D_{A_0}H`. This proves:

**Corollary 2.** Every smooth positive definite `H` is a harmonic
twisted spinor for some unitary connection `A`. The connections solving
this Dirac equation form an affine space modelled on smooth sections
of a real rank-eight kernel bundle.

This is a construction, not a dimension heuristic. It does not solve
the curvature equation and it makes no smallness assertion for its residual.

## 4. Exact full-rank seeds with prescribed determinant curvature

**Theorem 3.** Fix any unitary connection `B` on `L=det E` such that
`F_B^+` is nowhere zero. For any smooth real function `t` satisfying

\[
 t>\big|\mathcal T^{-1}(F_B^+)\big|_{\rm op},
 \qquad H=\left(tI+\mathcal T^{-1}(F_B^+)\right)^{1/2},  \tag{11}
\]

there is a smooth unitary connection `A` on `E` with

\[
 \det A=B,\qquad D_AH=0,\qquad
 \operatorname{tr}(F_A^+-\tau(H))=0.                    \tag{12}
\]

**Proof.** The traceless Hermitian matrix in (11) is nonzero everywhere,
so `H` is positive with distinct eigenvalues at every point. Its square
has exactly the prescribed trace-free part, and (2) proves the trace
equation. Start with any unitary `A_0` inducing `B` on its determinant.
Apply the traceless version of Lemma 1 and its smooth right inverse to
solve (8). The resulting `B`-correction in (8) is traceless, hence does
not change the prescribed determinant connection. QED.

Here the letter `B` in (11)--(12) denotes a line connection; the
connection difference in (8) is an endomorphism-valued one-form, not
that line connection. No identification of the prescribed line
connection with the fixed background spin-c connection is needed.

After this construction the unsolved equation is exactly

\[
 \big(F_{A_H+k}^+-\tau(H)\big)_0=0,
 \qquad k\in\Gamma\ker(\mathcal L_H|_{\mathfrak{su}(2)}).\tag{13}
\]

The kernel here has real rank four. Varying `k` preserves both equations
in (12), but (13) is still a nonlinear curvature PDE. In particular
(12) does not furnish a Leung solution.

If `F_B^+` has zeros, this construction does **not** automatically
extend across them: `H` becomes scalar and the determinant-preserving
map loses half its rank. One then has four real compatibility equations
at the zero and a potentially singular right inverse. The cohomological
condition `(a^+)^2>0` does not imply that `F_B^+` is nowhere zero.

### Application to the actual slow-interpolation metrics

The explicit `G_L` in round8_multitwist.md are almost-Kähler. On an
active collar the two-form

\[
 \omega_L=b(t)\,dt\wedge d\theta+a(u)\,du\wedge ds
\]

is the sum of the base and fibre area forms; the shear preserves the
fibre form. These local expressions glue globally, are closed, and
are compatible with `G_L`. Let `J_L` be their compatible almost-complex
structure. Freezing the interpolation parameter gives a local product
of hyperbolic surfaces, for which `J` is parallel. In the moving
orthonormal frame all deviations have at least one base derivative of
the interpolation parameter. The same bounded-frame calculation as
in round8_multitwist.md gives

\[
 |\nabla J_L|+|\nabla^2J_L|=O(L^{-1}),\qquad
 \operatorname{Rm}_{G_L}=\operatorname{Rm}_{\rm product}+O(L^{-1})
                                                               \tag{14}
\]

pointwise on every active region; both errors vanish outside those
regions. Here the comparison is in the moving frame with its frozen
parameter, not with a single global product metric.

The Hermitian connection
`nabla^J=nabla-(1/2)J(nabla J)` preserves `G_L,J_L`; let `B_L` be its
determinant connection on `det(T^{1,0}X)=K_{J_L}^{-1}`. Its curvature
differs from the product determinant curvature by `O(L^{-1})`, using
(14) and the curvature formula for a change of connection. The product
determinant curvature is `+/- i omega_L`, according to Chern sign, and
is self-dual of norm `sqrt(2)`. Hence

\[
              |F_{B_L}^+|\ge\tfrac12\sqrt2
\]

for all sufficiently large `L`. Theorem 3 applies on these actual fixed
bundles, including the noncommuting-twist family. It gives smooth full-rank
seeds solving Dirac and trace curvature globally. The background
connection on the source determinant may still be chosen harmonic as
Leung requires. No uniform bound on the seed's traceless residual is
asserted: the remaining equation is (13).

## 5. The full equation has a negative, determinant-independent index

Put `T=2 chi+3 tau`. The characteristic identities are

\[
 p_1(\mathfrak{su}(E))=a^2-4c_2(E)=T,\qquad
 c_2(E)=(a^2-T)/4.                                      \tag{15}
\]

The gauge-fixed linearization of (1), modulo the full `U(2)` gauge
group, has the principal symbol of

\[
 (d_A^*+d_A^+)_{\mathfrak u(E)}\ \oplus\ D_A.            \tag{16}
\]

Its lower-order terms, including the quadratic map and spinor in the
gauge action, do not change its index. The ASD part has real index
`-2T-4(1-b_1+b^+)=-2T-2(chi+tau)`. The twisted Dirac index is

\[
\begin{aligned}
 \operatorname{ind}_{\mathbb C}D_A
 &=\int_X\operatorname{ch}(E)e^{-a/2}\widehat A(X)\\
 &=a^2/4-c_2(E)-\tau/4
   =(\chi+\tau)/2.
\end{aligned}                                                   \tag{17}
\]

There is also a geometric check of this cancellation: with the induced
connection on `E=W`, the bundles are
`Hom(W,W)=C plus Lambda^+_C` and `Hom(S_L^-,W)=Lambda^1_C`.
The Dirac symbol is the self-dual de Rham symbol, whose complex index
is `1-b_1+b^+=(chi+tau)/2`. The determinant twist cancels on these
homomorphism bundles.

Consequently the real deformation index is

\[
 \boxed{\quad d_{U(2)}=-5\chi-7\tau.\quad}              \tag{18}
\]

This independently agrees with the full `U(n)` formula in
[Zentner, *What to expect from U(n) Seiberg--Witten monopoles for n>1*,
p. 6](https://arxiv.org/pdf/0803.0023), on substituting `n=2`, source
determinant `-a`, and (15).

For all actual bundles in round8_multitwist.md, `tau=0` and
`chi=4(p-1)(q-1)>0`. Thus `d=-20(p-1)(q-1)`, independently of which
spin-c structure is selected. At every full-rank solution the gauge
stabilizer is trivial, and the cokernel of the gauge-fixed linearization
has real dimension at least `5 chi`. Such a solution cannot be regular.
Negative index is **not** a nonexistence proof at the distinguished
unperturbed equation or on the Einstein locus.

For comparison, deleting the determinant equation and fixing the
determinant connection changes the problem. The `SU(2)`-gauge index of
that PU(2) problem is

\[
              d_{\rm fixed\ det}=-(9\chi+13\tau)/2.     \tag{19}
\]

If one additionally divides by the constant scalar circle, subtract one.
This is the convention used in Feehan--Leness, Proposition 2.28 and its
index calculation, [*PU(2) monopoles I*, pp. 39--40 of the
preprint](https://arxiv.org/pdf/dg-ga/9710032). Their pp. 2--4 explicitly
fix the determinant and project the quadratic term on both factors.
Their compactification and transversality results therefore cannot
be read as an existence theorem for (1).

There is a related exact warning in Zentner's Proposition 2.1:
when the central quadratic coefficient is deformed to zero, taking
the trace fixes the harmonic part of the central perturbation; a
generic central perturbation violates this condition when `b^+>0`.
The resulting deformed moduli space is empty. The broader claim about
vanishing invariants is explicitly conditional on the needed cobordism
theory, and is not assumed here. Nor does the proposition prove
emptiness at the nonzero coefficient and zero perturbation in (1).

Minimizing the squared norm of the two equations also does not force
minimum zero. Equation (7) gives an explicit positive lower bound on
one broad full-rank family, even when its Dirac equation is solved.
For the genuine seeds (12), the unsolved functional is the squared
norm of (13); no topological argument here makes its infimum zero.

## 6. What was and was not obtained

The forward result is a global construction of full-rank seeds satisfying
the Dirac equation and the full determinant-curvature equation on the
actual near-Einstein surface-bundle metrics. Their remaining equation
is displayed in (13), not hidden in an existence claim. The negative
index explains why regular generic moduli spaces do not automatically
supply these distinguished solutions.

No full coupled solution, no correction of the actual `G_L` to an
Einstein metric, and no all-Einstein nonexistence result on `E_D` or
`E_full` is proved. The test program
[round9_nonabelian_check.py](round9_nonabelian_check.py) verifies the
finite-dimensional ranks, trace and polar identities, the
covariantly-closed Clifford injection, and all index substitutions.
It does not prove an analytic existence theorem or independently
verify Leung's projective-flatness theorem.

## Appendix. Parallel-field algebra and an unresolved source transfer

**Proposition 4.** Suppose a pair solves the curvature equation in (1)
and `phi:W->E` is an invertible parallel homomorphism for the source
spin connection and `A`. Then its two singular values are equal,
and `(a^+)^2=0`.

**Proof.** Write `phi=UH` in polar form. Both factors are parallel;
use the unitary target gauge `U^{-1}`. Then `H` is positive and
parallel and `A` is the source connection. If the two eigenvalues
of `H` differ at one point, they are different constants everywhere
on that connected component. Their eigenlines are parallel. Therefore
all curvature endomorphisms of `A`, including `F_A^+`, lie in the
real two-dimensional diagonal algebra `u(1) plus u(1)`.

On the other hand, (4) says that `tau(H):Lambda^+->u(E)` has real
rank three, since `H` is invertible. It cannot equal `F_A^+`, whose
image is in that diagonal algebra. This contradiction proves that
`H=fI`. Equation (2) now gives `tr F_A^+=0`, and harmonic projection
implies `(a^+)^2=0`. QED.

The off-diagonal calculation is particularly transparent in an
eigenframe: the target off-diagonal blocks of the projected tensor
are nonzero multiples of `xy` times the source off-diagonal matrices.
A diagonal curvature cannot contain them. This is not the rank-one
sign comparison left open in round 7.

There is also a direct Clifford calculation worth keeping distinct
from any published connection identification. If the Clifford one-form
`Theta_j=phi c_j` is covariantly closed for precisely these source and
target connections, normal-frame derivatives `X_j=nabla_j phi` obey
`X_i c_j-X_j c_i=0`. Taking `c_0=I` gives `X_j=X_0c_j`; two
anticommuting quaternionic matrices then give `X_0=0`. Thus this
particular covariant-closedness condition implies parallelness.

**Unresolved source compatibility; no moduli-emptiness conclusion.**
The published pp. 26--28 use a parallel full-rank field and a polar
gauge in their equality argument, but retain a nonscalar case leading
to a product of hyperbolic planes. Corollary 1.2 on p. 18 also contains
a converse for the locally symmetric spaces. Applying Proposition 4
to that nonscalar case would eliminate it. This is a substantive
compatibility tension; it cannot be dismissed by saying that the
paper asserts only a necessary implication, nor by an overall sign
change in (4).

What remains to be reconciled is the exact bundle/connection
identification of the parallel field in that equality construction
with the source and target in Proposition 4 and the curvature tensor
projected in (4). The printed `E_L` and `D_{A,L}` notation must not
silently be equated to an untwisted pair while making this transfer.
This note therefore does **not** infer emptiness of the published
canonical-determinant moduli space, exclude its product branch, or
assert an error in the published theorem. The construction in
Theorem 3 and the index calculation do not use that equality theorem
or this unresolved identification.
