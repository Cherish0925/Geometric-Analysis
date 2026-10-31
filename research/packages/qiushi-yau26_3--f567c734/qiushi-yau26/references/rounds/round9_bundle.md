# Harmonic projection energy on fixed near-Einstein surface bundles

21 September 2026.

## 1. The global question and the result

Let `pi:E -> B` be one of the fixed surface bundles constructed in
`round8_multitwist.md`: the single-twist bundle `E_D`, a disjoint-twist
bundle, or the full-generator bundle `E_full`. Both fibre and base are
closed oriented surfaces of genera `p,q>=2`. Their monodromy contains an
actual single Dehn twist and has infinite image in the mapping class group.
The underlying smooth bundle and its projection are fixed. Put

\[
 c=\chi(E)=4(p-1)(q-1),\qquad V_0=4\pi^2c,
 \qquad b=e_B=\pi^*e(TB).
\]

For a source metric `G` and a marked hyperbolic target `h` on `B`, let
`f_h:(E,G)->(B,h)` be the harmonic representative of `pi`, and define

\[
 \mathcal E_G(h)=\frac12\int_E|df_h|^2\,dV_G,
 \qquad
 H(G)=4\pi^2\|\mathsf H_G b\|_2^2,
 \qquad
 \Gamma(G)=\min_{h\in\mathcal T(B)}\mathcal E_G(h)-H(G).       \tag{1}
\]

The minimum exists for every fixed `G`; a proof retaining the relevant
uniformity is given below. No Einstein hypothesis is needed to define (1).
The result of this note is the following precise distinction.

**Theorem.**

1. Every hypothetical normalized Einstein metric `Ric_G=-G` on these
   bundles satisfies `Gamma(G)>0`.
2. The actual area-preserving slow-twist metrics `G_L` from the inherited
   construction satisfy

   \[
   \boxed{\quad \Gamma(G_L)=0,\qquad
   \operatorname{Vol}(E,G_L)=V_0,\qquad
   \|G_L^{-1}\operatorname{Ric}_{G_L}+I\|_\infty\le C/L.\quad} \tag{2}
   \]

3. If `Ric_G=-G`, write `v=Vol(G)/V0`. The two actual canonical monopole
   classes, in the two orientations, give `v>=1` and

   \[
   \boxed{\quad
   c(\sqrt v-\sqrt{v-1})^2
   \le\|\mathsf H_G b\|_2^2
   \le c(\sqrt v+\sqrt{v-1})^2.\quad}                       \tag{3}
   \]

The same bounds hold for the vertical Euler class. Equation (2) is an
exact variational statement about the actual fixed-topology inputs, not
a numerical limit or a product-topology surrogate. It also identifies a
limitation: the zero set of this functional contains all these approximate
inputs, while any exact Einstein output would lie outside it. There is
no argument that all metrics on the smooth manifold lie in the zero set.
Consequently this is not yet an Einstein nonexistence theorem or a Yau26
branch counterexample.

The metric construction, existence of optimal targets, and the per-target
parallel-map obstruction are already present in the Skill. The addition
here is their quantitative combination into (1)--(3), including the exact
calibration of the actual input family. No global priority claim is made.

## 2. Target optimization is compact for each fixed source

We record a general fact with its proof because its source dependence
is essential here.

**Lemma.** Let `(M,G)` be a fixed closed connected Riemannian manifold
and `a:pi_1(M)->Pi_q` an epimorphism, `q>=2`. The harmonic energy in the
homotopy class determined by `a`, as a function of the marked hyperbolic
target, is proper on Teichmuller space and attains a minimum.

Existence of an energy-minimizing harmonic map follows from
[Eells--Sampson, Theorem 11A](https://math.jhu.edu/~js/Math646/eells-sampson.pdf).
The image on fundamental groups is noncyclic; hence the negative-curvature
uniqueness exception in
[Hartman, *On Homotopic Harmonic Maps*](https://math.jhu.edu/~js/Math646/hartman.harmonic.pdf)
does not occur.

For any such harmonic map, Bochner's formula and target sectional
curvature `-1` imply, with `t=|df|^2`,

\[
 \Delta_G t\ge-C_Gt.
\]

On the fixed closed source, the scalar mean-value/Moser estimate gives

\[
 \|df\|_\infty^2\le C'_G\mathcal E_G(h).                  \tag{4}
\]

The constants are source constants. The target injectivity radius is not
used: only its nonpositive curvature enters this estimate.

Suppose a sequence of target energies is bounded. Fix source loops whose
images under `a` are a generating set of `Pi_q`, and lift each harmonic
map equivariantly to `H^2`. Conjugate the target holonomy so that the image
of one fixed source basepoint is `o in H^2`. By (4), the displacement of
`o` by each chosen generator is uniformly bounded. The action of
`PSL(2,R)` on `H^2` is proper with compact point stabilizer, so all generator
matrices lie in fixed compact subsets. A subsequence converges to a surface
group representation.

The Euler number is locally constant on the representation variety and
equals the same maximal value `+(2q-2)` or `-(2q-2)` for this sequence.
Its limit is therefore maximal. By
[Goldman's maximal-Euler characterization](https://www.math.umd.edu/~wmg/TopologicalComponents.pdf),
the limiting representation is again faithful, discrete and cocompact.
The holonomy description of Teichmuller space then gives convergence of
the marked targets. This proves compactness of energy sublevel sets.
Continuity of the minimum energy follows by comparing energies under
smooth, uniformly bilipschitz convergence of marked target metrics; the
maps minimize in the same homotopy class. Properness proves attainment.

The argument does not give a uniform properness estimate as the source
metric degenerates. In particular, it is not permissible to use `C'_G`
as a fixed constant on the slow-twist sequence.

## 3. An exact identity and a positive fixed-source gap

Assume now that `Ric_G=-G`. For any target `h`, put

\[
 t=|df_h|^2,\qquad \alpha_h=f_h^*\omega_h,\qquad
 J=|\alpha_h|,\qquad B_h=\nabla df_h.
\]

The two nonzero singular values of `df_h` give `t=s_1^2+s_2^2` and
`J=s_1s_2`. Both ordered target-curvature terms contribute `J^2`, so

\[
 \frac12\Delta_Gt=|B_h|^2-t+2J^2.                         \tag{5}
\]

Hyperbolic Gauss--Bonnet gives `[omega_h]=-2pi e(TB)`. With
`eta=H_G b`, Hodge decomposition therefore reads

\[
 \alpha_h=-2\pi\eta+d\nu_h,\qquad
 \int J^2=4\pi^2\|\eta\|_2^2+\|d\nu_h\|_2^2.
\]

Integrating (5) yields the exact identity

\[
 \boxed{\quad
 \mathcal E_G(h)-H(G)
 =\|d\nu_h\|_2^2+\frac12\|B_h\|_2^2.\quad}              \tag{6}
\]

It is an additive decomposition into the nonharmonic area-form part
and the failure of the differential to be parallel. It does not identify
either term with horizontal conformality.

If equality held, `B_h=0`. The noncyclic fundamental-group image rules
out constant and parallel rank-one maps, hence `f_h` has rank two
everywhere. Its kernel and orthogonal complement are parallel. The
four-dimensional source is locally a product of two surfaces, each of
curvature `-1`. A parallel rank-two map to a surface of curvature `-1`
has horizontal singular values one: this follows by applying curvature
intertwining to an orthonormal horizontal pair. Thus it is a Riemannian
submersion with totally geodesic fibres and flat horizontal distribution.

Since it is proper and induces the same epimorphism as `pi`, its fibres
are connected. They are closed hyperbolic surfaces; parallel transport
acts by their isometries. That is a finite group, so the outer monodromy
of its fundamental-group extension is finite. The extension is the one
defined by `pi_*`, whose outer monodromy contains an infinite-order Dehn
twist. This contradiction proves strictness of (6) for every target.

Section 2 now strengthens per-target strictness to

\[
 \boxed{\quad \Gamma(G)>0\quad}                          \tag{7}
\]

for each fixed hypothetical Einstein source. Attainment is necessary:
positivity at every target alone would not justify a positive infimum.
This gap may depend on the entire source geometry. The argument has
not produced a lower bound depending only on `p,q`, or on dimension.

## 4. The two-orientation monopole budget

Write `e=e(ker d pi)`. The surface bundles under consideration have
signature zero, and

\[
 e^2=b^2=0,\qquad e\cdot b=c.
\]

They admit symplectic forms in both orientations. The canonical
classes are `-e-b` in the chosen orientation and `-e+b` in the opposite
orientation. Both have positive square `2c` in their own orientation.
Here `b_+>1` in both orientations, so the corresponding canonical
monopole classes and scalar-curvature inequalities apply. The scalar
estimate used is

\[
 \int_Es_G^2\,dV_G\ge32\pi^2(a_G^+)^2,
\]

as in [LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg--Witten
Theory*](https://arxiv.org/pdf/math/0003068). The classes, orientations,
and the absence of a chamber ambiguity are part of this application.

For `Ric=-G`, the scalar curvature is `-4`. Define positive-definite
Hodge-half inner products by

\[
 x=\|e^+\|^2=\|e^-\|^2,\quad
 y=\|b^+\|^2=\|b^-\|^2,\quad
 z=\langle e^+,b^+\rangle,\quad
 w=\langle e^-,b^-\rangle.
\]

Then `z-w=c` and Cauchy--Schwarz gives `xy>=c^2/4`. The two scalar
bounds are

\[
 x+y+2z\le\frac{V}{2\pi^2}=2cv,\qquad
 x+y-2w\le2cv.
\]

Their maximum is equivalent to

\[
 x+y+|z+w|\le c(2v-1).                                   \tag{8}
\]

In particular `v>=1`. Set `S=c(2v-1)`. Since `x+y<=S` and
`xy>=c^2/4`, the quadratic inequality `y(S-y)>=c^2/4` puts `2y`
between `S-sqrt(S^2-c^2)` and `S+sqrt(S^2-c^2)`. As
`||H_G b||^2=2y`, this proves (3); interchange `x,y` for `e`.

The interval is sharp as an algebraic relaxation of these inequalities:
its endpoints have `z=c/2`, `w=-c/2`, `x+y=S`, `xy=c^2/4`.
No assertion is made that an actual Einstein metric realizes every
algebraic endpoint.

Combining (3) and (6) gives, for every target,

\[
 \mathcal E_G(h)\ge
 V_0(\sqrt v-\sqrt{v-1})^2
 +\|d\nu_h\|_2^2+\frac12\|B_h\|_2^2.                   \tag{9}
\]

This is a lower energy budget. It cannot be used as an upper energy
bound or as an assertion that a minimizing map is conformal. An
Einstein-nonexistence argument would need an additional result forcing
`Gamma(G)=0` for arbitrary exact sources, or an incompatible upper
bound. Neither follows from the present monopole estimates.

## 5. The actual approximate inputs attain zero gap

The slow-twist construction uses fixed hyperbolic fibre paths with
the same area form `omega_F`. Every gluing Dehn twist preserves this
form. It therefore defines a global closed vertical two-form on `E`.
This remains true for the full-generator construction: the fibre twist
supports may intersect, but their base interpolation cylinders are
disjoint and each actual transition preserves the same fibre area form.

On an active cylinder the metric is

\[
 G_L=dt^2+b_L(t)^2d\theta^2+h_{\eta(t/L)},\qquad
 \det h_z=\det h_0.
\]

Outside the cylinders it is the hyperbolic product. The projection
to the chosen hyperbolic base metric `h_L` is a Riemannian submersion.
Its fibres are minimal because their area density is independent of
the base coordinate. Hence `pi` is harmonic. Pointwise,

\[
 |d\pi|^2=2,\qquad |\pi^*\omega_{h_L}|=1,
 \qquad \mathcal E_{G_L}(h_L)=V_0.
\]

The area forms are orthogonal complements:

\[
 *_{G_L}\pi^*\omega_{h_L}=\omega_F.
\]

Both forms are closed, so `pi^*omega_{h_L}` is harmonic. It represents
`-2pi b`; consequently `H(G_L)=V0`.

This particular target is already a global energy minimizer over all
marked targets, not just a critical point. Indeed, for any smooth
`f` homotopic to `pi` and any marked hyperbolic `h`,

\[
 \int_Ef^*\omega_h\wedge\omega_F
 =\operatorname{Area}(B,h)\operatorname{Area}(F,h_0)=V_0.
\]

The form `omega_F` has pointwise norm and comass one. Thus

\[
 V_0\le\int_E|f^*\omega_h|
 \le\frac12\int_E|df|^2.
\]

Equality is attained by the projection above. This proves `Gamma(G_L)=0`
exactly, while `delta_-(G_L)<=C/L` was established from the complete
Ricci matrix in the previous round.

There is no contradiction with (6), which assumes the exact Einstein
equation. For `Phi=Ric_G+G`, the full integrated identity is

\[
 \mathcal E_G(h)-H(G)=\|d\nu_h\|_2^2
 +\frac12\|B_h\|_2^2
 +\frac12\int_E\langle\Phi,f_h^*h\rangle.                 \tag{10}
\]

For the actual shear coframe, write `s=Q eta'(t/L)/L` for the shear
coefficient (not scalar curvature). The full Ricci computation gives

\[
 |\nabla d\pi|^2=\frac{s^2}{2},\qquad
 \langle\Phi,\pi^*h_L\rangle=-\frac{s^2}{2},\qquad d\nu=0.
\]

The two terms cancel pointwise in (10). This supplies a concrete
mechanism: small Ricci error compensates the small but nonzero bending
of the harmonic projection, even though its energy is globally minimal.
Target minimization alone therefore cannot eliminate the near-Einstein
error. The inherited inputs already have the optimized target property.

## 6. A fixed projection need not give an unforced moduli equation

This auxiliary example isolates a different proposed bridge. It is
an exact Einstein example, but it has product topology; it does not
purport to be an Einstein metric on the twisted bundles.

Let `F,B` be closed hyperbolic surfaces and `g0=h_F+h_B`. Choose a smooth
function `u` on `F` and a vector field `Z` on `B` supported in a disk.
With `phi_s` its complete flow, set

\[
 \Phi_\varepsilon(x,y)=(x,\phi_{\varepsilon u(x)}(y)),\qquad
 G_\varepsilon=\Phi_\varepsilon^*g_0.
\]

These are exactly Einstein with `Ric=-G_epsilon`, and retain all product
volume and monopole equalities. Yet the induced metric on the fibre
of the original fixed projection is exactly

\[
 h_{\varepsilon,y}=h_F+
 \varepsilon^2|Z|^2(\phi_{\varepsilon u(x)}(y))\,du\otimes du.
                                                               \tag{11}
\]

Choose a nonzero TT tensor `k` on `F` and `u` with
`integral <k,du tensor du> !=0`. Such a choice exists: in a small coordinate
patch where `k^{11}>0`, take `u_N=chi sin(Nx^1)/N`; the leading integral
is positive and the remaining terms tend to zero as `N` increases.
The TT pairing removes conformal and Lie-derivative variations, so it
detects a nonzero Teichmuller tangent `v_u` of `du tensor du`. Uniformizing
the fibre metrics in their marked conformal classes gives

\[
 T_\varepsilon(y)=T_0+
 \varepsilon^2|Z(y)|^2v_u+O(\varepsilon^3).                \tag{12}
\]

This map is nonconstant for sufficiently small nonzero `epsilon` and
has image inside a small strictly convex Weil--Petersson ball. It
cannot solve an unforced weighted harmonic-map equation for any
smooth positive weight and any base metric: compose with a strictly
convex function on that ball, integrate its weighted Laplacian, and
deduce `dT=0`, a contradiction.

Thus an unforced fibre-moduli equation for an arbitrary fixed projection
does not follow from the Einstein equation, even at exact product
volume. A source term omitted in that reduction cannot be bounded solely
by the Einstein defect, which vanishes in this example.

This does **not** refute a statement using the intrinsic harmonic
representative instead. For `G_epsilon` that representative is
`pi composed with Phi_epsilon`, and its fibres recover the parallel
product geometry. The distinction between the chosen projection and
its harmonic representative must remain in any proposed global proof.

## 7. What this resolves and what remains

The target optimization is not the missing step for the actual input
family: it is already solved exactly by calibration. For a hypothetical
Einstein output, the optimized gap is strictly positive and bounded
below for that fixed source; a hypothetical output must leave the
calibrated zero-gap locus. The two-orientation monopole inequalities
give explicit control of the Hodge term but do not force a return to
that locus.

The outstanding bridge is consequently precise: does topology, together
with the unrestricted Einstein equation, force an upper bound on the
optimized projection energy that contradicts (6)--(9), or can an exact
metric occur with positive `Gamma`? Neither a degenerate zero-gap input
sequence nor the target stationarity condition decides this question.
An exact solution far from the constructed metrics is still allowed by
Yau26 and by every result here.

The opposite-orientation monopole input is specific to these bundles;
it is not being asserted for arbitrary four-manifolds. All statements
about exact negative Einstein metrics use normalization `Ric=-G`.
Nonnegative Einstein constants are separately excluded on these
symplectic bundles: the nonzero Seiberg--Witten invariant forbids positive
scalar curvature, and the positive-square canonical class together
with LeBrun's scalar bound forbids scalar curvature identically zero.
No sign remains hidden in the unresolved question.

## 8. Reproduction

Run `qiushi-yau26 env numeric python round9_bundle_check.py` from this
worktree. All 15 exact algebraic checks passed: the two monopole bounds,
their interval and endpoint identities, the energy/Hodge normalization,
the complete near-Einstein error sign, its shear cancellation, and all
entries of the graph-fibre pullback calculation. The full Ricci matrix
used in Section 5 is independently checked by `round8_multitwist_check.py`.
These programs check those formulas, not the analytic compactness,
Hodge theory, or group-monodromy proofs given above.
