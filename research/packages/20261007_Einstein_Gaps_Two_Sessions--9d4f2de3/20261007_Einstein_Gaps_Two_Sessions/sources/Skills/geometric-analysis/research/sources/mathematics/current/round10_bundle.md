# Exact Einstein control families for the harmonic-energy strategy

21 September 2026.

## 1. Result and its precise bearing on the twisted bundles

The proposed bridge was to turn infinite monodromy, two-orientation
monopole bounds and a small relative volume excess into a uniform positive
defect for every exact Einstein metric. The following **actual exact
Einstein family** disproves that bridge without a hypothesis specific to
the zero-signature Dehn-twist bundles.

Fix any nonisotrivial Kodaira fibration
`f_0:S_0 -> B_0`, with fibre genus `p>=2`, base genus `q>=2`, and
signature `tau_0>0`. There are smooth holomorphic surface bundles
`f_m:S_m -> B_m`, `m>=1`, with all the following properties:

- The fibre genus is the same fixed `p`, and the image of the monodromy
  in `Mod(Sigma_p)` is the same infinite subgroup as for `f_0`.
- Both orientations of `S_m` are symplectic and have the actual canonical
  monopole classes needed for the corresponding scalar inequalities.
- There is a smooth metric `G_m` with `Ric_Gm=-G_m`.
- The signatures are the same positive integer `tau_m=2 tau_0`, whereas
  `c_m=chi(S_m)=4(p-1)(2q-2+m)` tends to infinity.

Define the round-9 functional using this bundle projection:

\[
 E_*(G)=\min_{h\in\mathcal T(B)}\frac12\int|df_h|^2,
 \qquad H(G)=4\pi^2\|\mathsf H_G e_B\|_2^2,
 \qquad\Gamma(G)=E_*(G)-H(G),
\]

where `e_B=f^*e(TB)` and `f_h` is the intrinsic harmonic representative
of the projection for the indicated target. Put `V0_m=4pi^2 c_m` and
`v_m=Vol(G_m)/V0_m`. Then the exact formulas are

\[
 \boxed{\quad
 v_m=1+\frac{3\tau_m}{2c_m},\qquad
 E_*(G_m)=V_{0,m},\qquad
 H(G_m)=\frac{V_{0,m}}{v_m},\qquad
 \Gamma(G_m)=V_{0,m}\left(1-\frac1{v_m}\right)>0.
 \quad}                                                       \tag{1}
\]

Consequently

\[
 v_m\longrightarrow1,\qquad
 \frac{\Gamma(G_m)}{V_{0,m}}\longrightarrow0,\qquad
 \frac{\Gamma(G_m)}{\operatorname{Vol}(G_m)}\longrightarrow0,
 \qquad
 \Gamma(G_m)\longrightarrow6\pi^2\tau_m=12\pi^2\tau_0>0.   \tag{2}
\]

Thus a uniform **normalized** gap is impossible on this broader class,
even with fixed fibre genus and fixed monodromy image. An absolute gap
does not vanish in this family. These are different assertions.

Every `S_m` has positive signature and a holomorphic fibration. None is
being identified with the zero-signature `E_D` or `E_full`, whose specified
monodromy is different. The example neither proves nor disproves Einstein
existence on those manifolds. It identifies exactly why replacing their
special structure by merely infinite monodromy and nearly vanishing
signature/Euler ratio loses information essential to a possible proof.

The starting Kodaira fibrations and negative Kähler--Einstein existence
are classical. The calculation below supplies a checkable control family
for the present harmonic/Hodge functional; no priority claim is made.

## 2. A smooth branched base change with fixed signature

Nonisotrivial Kodaira fibrations are smooth holomorphic submersions with
connected fibres. Concrete examples with positive signature are provided
by Catanese--Rollenske, including their Example 5.8;
see [*Double Kodaira Fibrations*](https://arxiv.org/pdf/math/0611428).
Such surfaces have `2<c_1^2/c_2<3` and hence positive signature.

Choose `2m` distinct points on `B_0`. A line bundle square root of their
divisor exists: the divisor has even degree and multiplication by two
on the Jacobian is surjective. The associated double cover

\[
 r_m:B_m\longrightarrow B_0
\]

is smooth, connected, and simply branched at those points. It is connected
because a disconnected degree-two cover would be a union of degree-one
maps and could not have simple ramification. Riemann--Hurwitz gives

\[
 q_m=2q-1+m.                                                \tag{3}
\]

Take the fibre product `S_m=S_0 times_(B0) B_m`, with maps
`P_m:S_m->S_0` and `f_m:S_m->B_m`. There is no singularity introduced
by this base change. Near a ramification point, use submersion coordinates
`f_0(z,w)=z` and `r_m(t)=t^2`. The fibre product is parametrized by
`(t,w)`, and `f_m(t,w)=t`; in particular `f_m` is still a holomorphic
submersion. The fibres remain the original connected genus-`p` curves.

The vertical tangent bundle is pulled back exactly:

\[
 T_vS_m\simeq P_m^*T_vS_0.
\]

For any oriented surface bundle over an oriented surface, the tangent
bundle splits as oriented real planes, and

\[
 p_1(TS)=e(T_vS)^2+e_B^2=e(T_vS)^2,
 \qquad 3\tau(S)=\langle e(T_vS)^2,[S]\rangle.
\]

Since `P_m` has degree two, this proves directly

\[
 \tau_m=2\tau_0,
 \qquad c_m=(2-2p)(2-2q_m)=4(p-1)(2q-2+m).                \tag{4}
\]

The signature formula has not incorrectly treated the branched map as
an unramified covering. It uses pullback of the vertical plane bundle;
the base Euler class has square zero on both sides.

In fact `r_m` induces a surjection on fundamental groups. Its image has
finite index dividing its nonzero degree two. If the index were two,
`r_m` would lift to the associated unramified double cover of `B_0`.
That lift is a degree-one holomorphic map of compact curves and hence a
biholomorphism, contradicting the ramification (or (3)). Thus the index
is one. It follows that the pulled-back monodromy has exactly the same
image as the original, not just a possibly smaller infinite image.

## 3. Canonical ampleness, exact metrics, and both orientations

A Kodaira-fibred surface is projective, minimal, and of general type;
see the relative-canonical positivity and surface-fibration results in
[Catanese's review, Sections 3.1--3.2](https://www.mathe8.uni-bayreuth.de/de/team/prof-fabrizio-catanese-old/pdf/156.pdf).
It contains no rational or elliptic curve: any map from such a curve to
the hyperbolic base is constant, and a hyperbolic fibre contains no such
curve. A minimal surface of general type has nef and big canonical
bundle; a curve of canonical degree zero would, by adjunction and the
Hodge index theorem, be a rational `(-2)` curve. Therefore `K_S0` is
ample.

The base-change map has ramification divisor `R_m`, a disjoint union of
fibres of `f_m`, and the canonical bundle formula is

\[
 K_{S_m}=P_m^*K_{S_0}+R_m.                                 \tag{5}
\]

The first term is ample because `P_m` is finite; the second is nef,
being a sum of fibres. Thus `K_Sm` is ample. The negative
Kähler--Einstein existence theorem of Aubin and Yau supplies `G_m`
with `Ric=-G_m`; a primary reference is
[Yau, *On the Ricci Curvature of a Compact Kähler Manifold and the
Complex Monge--Ampère Equation, I*](https://doi.org/10.1002/cpa.3160310304).
Its Kähler form satisfies `[omega_m]=2pi K_Sm`.

Both orientations are symplectic. For example `omega_m` supplies the
complex orientation. If `omega_B` is a positive base area form, then
`omega_m-C f_m^*omega_B` is symplectic with the opposite orientation for
sufficiently large `C`: it is closed, positive on each vertical plane,
and negative on its horizontal complement. This is the usual
surface-bundle construction; see also
[Thurston, *Some Simple Examples of Symplectic Manifolds*](https://www.maths.ed.ac.uk/~v1ranick/papers/thurstonsimple.pdf).

Writing `e=e(T_vS_m)` and `b=e_B`, the canonical classes in the two
orientations are `-e-b` and `-e+b`. Their squares in their respective
orientations are `2c_m+3tau_m` and `2c_m-3tau_m`. Both are positive,
and `b_+>1` in both orientations (certainly for all large `m`). Their
canonical Seiberg--Witten classes therefore give the two corresponding
monopole curvature bounds. The control family is not evading those
bounds by removing reverse symplecticity or entering a `b_+=1` chamber.

## 4. Exact target optimization and Hodge computation

This calculation works for any Kodaira fibration with ample canonical
bundle. Drop the subscript `m`, put `c=chi(S)`, and retain `tau>0`.
The characteristic numbers are

\[
 e^2=3\tau,\qquad b^2=0,\qquad e\cdot b=c,
 \qquad K=-e-b,
 \qquad V=\frac12[\omega]^2=2\pi^2(2c+3\tau).             \tag{6}
\]

### 4.1 Optimization uses the intrinsic harmonic representative

Let `h_0` be the hyperbolic metric in the complex structure of the
holomorphic base. The holomorphic projection
`f:(S,G)->(B,h0)` is harmonic. It is the unique harmonic representative
in its homotopy class, because its fundamental-group image is the
noncyclic surface group. Thus this is not a prescribed nonharmonic
projection substituted for the intrinsic one.

For any marked hyperbolic target `h` and any smooth `u` homotopic to
`f`, the pullback `alpha=u^*omega_h` is a simple two-form. The Kähler
form has comass one, so pointwise

\[
 \frac12|du|^2\,dV_G\ge |\alpha|\,dV_G\ge\alpha\wedge\omega.
\]

The integral of the last term depends only on the homotopy class:

\[
 \int_S\alpha\wedge\omega
 =(-2\pi b)\cdot(-2\pi(e+b))=4\pi^2c=:V_0.              \tag{7}
\]

For the holomorphic projection both pointwise inequalities are equalities.
Therefore

\[
 E_*(G)=V_0.                                               \tag{8}
\]

This optimizes over every marked hyperbolic target, not merely over
maps to the original base structure. No assumption of a Riemannian
submersion or constant dilation is used. A holomorphic map to a curve
is horizontally conformal, but its horizontal dilation can vary along
fibres.

### 4.2 The Hodge term and the positive gap

The harmonic representative `eta=H_G b` has type `(1,1)`. On a Kähler
surface its self-dual part is the constant multiple of `omega`
determined by their cohomological pairing. Since `b^2=0`, the squared
norms of its self-dual and anti-self-dual parts agree. Hence

\[
 \|\eta\|_2^2
 =\frac{2(b\cdot[\omega])^2}{[\omega]^2}
 =\frac{2c^2}{2c+3\tau}
 =\frac c v,
 \qquad v=\frac V{V_0}=1+\frac{3\tau}{2c}.                \tag{9}
\]

Combining (8)--(9) proves (1). It also yields the useful exact form

\[
 \boxed{\quad
 \Gamma(G)=\frac{6\pi^2\tau}{v},\qquad
 V-V_0=6\pi^2\tau.
 \quad}                                                   \tag{10}
\]

The round-9 Bochner/Hodge decomposition applies without change:

\[
 \Gamma(G)=\|d\nu\|_2^2+\frac{1}{2}\|\nabla df\|_2^2,
 \qquad f^*\omega_{h_0}=-2\pi\eta+d\nu.                  \tag{11}
\]

Here the optimized projection is horizontally conformal everywhere,
yet `Gamma(G)>0`. Thus this energy gap is not a horizontal-anisotropy
functional. It measures nonparallelity and the nonharmonic component
of the pulled-back area. The source has infinite monodromy and is not
locally a product, entirely consistently with (11).

For the base-change family (4), equations (10)--(11) give

\[
 \frac1{\operatorname{Vol}(G_m)}
 \left(\|d\nu_m\|_2^2+\frac{1}{2}\|\nabla df_m\|_2^2\right)
 =\frac{v_m-1}{v_m^2}\longrightarrow0.                    \tag{12}
\]

This is a vanishing **average** geometric defect on exact Einstein
manifolds whose monodromy images remain fixed and infinite. No conclusion
about pointwise curvature bounds, injectivity radius, or the location
of the defect is inferred from the average.

## 5. Why an energy upper bound alone still does not close E_D

The examples above have positive signature; the original candidates
have `tau=0`. One must not substitute small `tau/chi` for that exact
identity. Nevertheless a second, purely algebraic observation pinpoints
a remaining issue even in the zero-signature case.

Grant, as an additional hypothetical estimate, the favorable upper
bound `E_*(G)<=V0` for an arbitrary Einstein metric on `E_D`. This bound
has **not** been proved there. The two-orientation scalar inequalities
and the round-9 Hodge/Bochner identities still do not imply a contradiction.

Indeed for any `v>1`, choose the following admissible Hodge-polarization
numbers, with notation from `round9_bundle.md`:

\[
 x=\frac{cv}{2},\quad y=\frac{c}{2v},\quad
 z=\frac c2,\quad w=-\frac c2.                            \tag{13}
\]

They satisfy `z-w=c`, `xy=c^2/4`, and both scalar-monopole bounds have
the same strictly positive slack

\[
 2cv-(x+y+c)=\frac{c(v-1)(3v+1)}{2v}>0.                   \tag{14}
\]

Setting `E_*=V0` gives `H=V0/v` and
`Gamma=V0(1-1/v)>0`, consistent with the exact nonnegative decomposition.
These numbers are **not** claimed to be realized by an Einstein metric
on `E_D`. They demonstrate that the displayed inequalities alone cannot
deduce `Gamma=0`, even after the unproved favorable energy upper bound
is granted. Some additional geometric equality, rather than another
use of those same scalar budgets, is required.

## 6. Consequence for the actual research target

The exact Einstein control family eliminates this proposed general
principle:

> Infinite surface-bundle monodromy, two-orientation monopoles and
> `Vol/(4pi^2 chi)` arbitrarily close to one force a dimension-only
> positive normalized harmonic gap, or force finite monodromy.

It is false even when fibre genus and the infinite monodromy image
are fixed. The construction does not eliminate a theorem using
**exactly** `tau=0`, the particular primitive Dehn-twist extension, or
the representation restrictions established for `E_full`.

For these actual candidates, the unresolved implication remains a
global one: their special smooth topology must force a condition on
the intrinsic harmonic representative or on the Einstein geometry
which the Kodaira examples do not satisfy. A nearly saturated numerical
ratio is not such a condition. Conversely, horizontal conformality
has a real positive model on Kodaira fibrations, so a contradiction from
that property would have to use the candidate's absence of a compatible
complex structure, not Einstein and infinite monodromy alone.

This is a route-discriminating exact construction, not a new Yau26
counterexample and not a proof that all harmonic-map strategies fail.

## 7. Reproduction

Run `qiushi-yau26 env numeric python round10_bundle_check.py`.
The checker verifies the Chern-number, branched-base, volume, Hodge,
gap and limit identities, as well as the zero-signature algebraic
budget example. It does not replace the geometric existence,
calibration or fundamental-group arguments above.
