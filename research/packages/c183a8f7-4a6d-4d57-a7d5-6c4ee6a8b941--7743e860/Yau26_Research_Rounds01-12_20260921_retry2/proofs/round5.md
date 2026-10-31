# Yau26: global receivers, construction compatibility, and connector geometry

20 September 2026.

The working question remains whether, in every dimension, one can choose
a Ricci pinching interval depending only on dimension that forces the same
smooth manifold to admit some Einstein metric. The output metric need not
resemble the input. This round investigates three concrete connections to
that question. None settles either unrestricted four-dimensional branch.

## 1. An actual closed-manifold obstruction at the first nonlinear scale

Let \(G_\varepsilon\) be the balanced near-negative-Einstein metrics on
the fixed Dehn-twist surface bundle \(E_D\), with fibre waist
\(\varepsilon\), base waist \(\beta=\varepsilon^2\), and fibre genus
\(p\ge2\). The previous estimate allowed an exact correction to begin at
the scale \(\varepsilon^{3/2}\). The new argument excludes every fixed
multiple of that scale, without assuming symmetry of the correction:

\[
 \boxed{
 \|h_\varepsilon\|_{C^2(G_\varepsilon)}\le C\varepsilon^{3/2}
 \quad\Longrightarrow\quad
 \liminf_{\varepsilon\to0}
 \frac{\delta_-(G_\varepsilon+h_\varepsilon)}{\varepsilon^3}
 \ge\frac1{16\pi^4(p-1)}.}
\]

In particular, there is no exact Einstein metric in this critical ball
for sufficiently small \(\varepsilon\). Any Einstein constant is covered
by constant rescaling: proximity forces that constant to be
\(-1+O(\varepsilon^{3/2})\). The existing three-scalar correction provides
the matching \(O(\varepsilon^3)\) upper order, so the best defect within
each such ball is \(\Theta(\varepsilon^3)\).

The additional mechanism is a **whole-fibre quadratic receiver**. Divide
the actual closed TT pairing by \(\beta\), not by the volume of the
double-thin core. Its mass converges to a hyperbolic cylinder times the
entire finite-area pinched fibre. Arbitrary bounded critical corrections
have ungauged Jacobi limits there. After a bounded gauge change, every
such limit is

\[
 V=\operatorname{sech}^2t\,(aT+bS)+A+J(t)B,
 \qquad J(t)=\arctan(\sinh t),
\]

where \(A,B\) are bounded fibre TT tensors. All trace, mixed, angular and
cusp components are accounted for. A finite-measure ground-state argument
excludes additional horizontal resonances. The full quadratic receiver is

\[
 \frac12\int\langle D^2(\operatorname{Ric}+g)[V,V],Q_*\rangle
       =-\frac\pi8\|B\|_{L^2(F_\infty)}^2\le0.
\]

An exact correction would require the positive value \(1/(2\pi^2)\).
The contradiction uses the global closed detector and tightness of its
measure; it does not assume that an uncomputed exterior response vanishes.

Proof: [closed construction theorem](round5_construction.md).
Independent derivation: [finite-measure classification and receiver](round5_receiver_independent.md).

This is still a neighbourhood theorem. Larger corrections and distant
Einstein metrics on the same \(E_D\) are not excluded.

## 2. Which constructions can actually meet the monopole gap?

For a closed oriented four-manifold put \(T=2\chi+3\tau\). For a set of
actual monopole classes define \(\alpha^2\) as the infimum, over maximal
positive cohomology planes, of their largest projected square. It is at
least the squared convex-hull invariant \(\beta^2\). A special monopole
class has square at least \(T\); ordinary classes cannot all be called
special merely by invoking perturbed transversality.

The previous integral theorem now gives, for all special classes together,

\[
 \mathcal E(g)+\left(\frac{T}{\alpha_{\rm sp}^2}-\frac23\right)_+
       \ge c_*>0,
 \qquad
 \mathcal E(g)=4-
   \frac{(\int s)^2}{\operatorname{Vol}(g)\int|\operatorname{Ric}|^2}.
\]

The constant is independent of the number of classes and the manifold.
This extends the scope beyond a fixed blow-up presentation. Actual
nonzero SW and Bauer--Furuta classes supply the necessary square condition.

More importantly, the two existing construction families can be compared
to this obstruction on their **actual smooth objects**:

* On \(E_D\) and every finite cover, in both orientations,
  \(\alpha_{\rm all}^2=\beta_{\rm all}^2=T=2\chi\). The ratio is one,
  not near \(2/3\). This saturation was already in the source manuscript;
  it rules out improving the comparison by merely adding unknown classes
  or passing to finite covers.
* For a fixed real-hyperbolic \(A_1\) orbifold resolution, let
  \(B_0=\operatorname{Vol}(\mathcal O)/(6\pi^2)\), in the normalization
  \(\operatorname{Ric}=-g\), and let \(m\) be the number of positive-square
  bolts in the chosen orientation. The actual shrinking-support
  construction gives
  \[
   T=B_0+6m,\qquad
   \alpha_{\rm all}^2\le\tfrac43B_0+m,\qquad
   \frac{T}{\alpha_{\rm all}^2}\ge\frac34
  \]
  whenever the invariant is positive. The bound uses the smooth
  Chern--Weil identity and vanishing \(L^1\) mass of the concentrated Weyl
  tensor, not an assumed bubble-energy formula. Thus even all ordinary
  monopole classes leave this construction a distance at least \(1/12\)
  above the critical ratio.
* Negative-definite connected sums do change that ratio, but the same
  integral theorem then constrains their inputs. If \(X\) is symplectic,
  \(b_+(X)\ge2\), \(A=c_1^2(X)>0\), and \(b_+(N)=0\), the actual
  connected-sum monopole classes give
  \[
   \mathcal E(g)+
    \left(\frac13-\frac{4b_1(N)+b_2(N)}{A}\right)_+\ge c_*.
  \]
  Therefore surgery into the critical nonexistence band cannot preserve
  arbitrarily tight near-Einstein inputs, regardless of the gluing ansatz.

These statements identify a real compatibility barrier: the current
near-Einstein constructions and the critical monopole obstruction do not
automatically combine into a counterexample. The proofs and precise class
hypotheses are in [the rigidity note](round5_rigidity.md). Its connected-sum
input is [Ishida, Proposition 6](https://msp.org/pjm/2012/258-2/pjm-v258-n2-p05-s.pdf).

## 3. A general connector must leave nonpositive sectional curvature

For a complete metric on \(\mathbb R\times T^3\) with two exact outward
hyperbolic ends, nonpositive sectional curvature implies

\[
 \boxed{\|\operatorname{Ric}+3g\|_{\infty,\mathrm{op}}\ge3/2.}
\]

This does not assume an isometric torus action in the interior. Bounded
length loops cannot escape into the expanding ends, so every deck
transformation is semisimple. The classical flat torus theorem supplies
a totally geodesic flat three-plane. On that plane the sum of tangent
Ricci entries equals the normal Ricci entry, incompatible with all four
entries being close to \(-3\).

The threshold is sharp as an infimum: a smooth clipped-and-mollified
warped profile gives actual exact-end metrics with defect tending to
\(3/2\). The same argument yields the sharp threshold
\((d-2)\lambda/d\) in dimension \(d\ge3\), with rank \(d-1\) torus ends
and normalization \(\operatorname{Ric}\approx-\lambda g\).

For the unrestricted twisted \(T^2\) connector, the full equations also
give an exact physical energy budget. With \(Q\) its twist energy,
\(E=\operatorname{Ric}+3g\), and \(E_B,E_V\) the two quotient blocks,

\[
 6V_{\rm ren}=\int(\operatorname{tr}E_V-Q),\qquad
 \int(|W|^2-Q)=
 \int\left[\operatorname{tr}E_B+\tfrac12|E|^2
                               -\tfrac16(\operatorname{tr}E)^2\right].
\]

The two chiral Weyl energies are equal. A defect below one forces a
positive sectional-curvature region and a Weyl peak greater than
\(\sqrt3(1-\epsilon)\). These facts do not yet control the physical
volume supporting that peak. A successful small-defect connector must
combine positive sectional curvature, twisting and possible collapse;
merely extending negatively curved radial profiles cannot suffice.

Proofs: [full connector equations and sharp four-dimensional result](round5_global.md),
[rank argument and sharpness in all dimensions](round5_rank_obstruction.md).

## 4. The next mathematical decisions

For \(E_D\), the surviving receiver kernel consists of integrable-looking
directions. The next task is a quantitative nonlinear modulation theorem,
with the actual global marking and degenerating inverse retained. The
critical-scale exclusion above cannot itself rule out a larger repair.

An [additional closed-tensor test](round5_modulation.md) sharpens this
target. A fibre-neck logarithmic ramp times the global TT detector remains
a fixed distance from every reference parameter tangent plus infinitesimal
gauge, although its linearized residual is \(\Theta(1/|\log\varepsilon|)\).
Thus uniform maximum-norm modulation is false. This is not an escaping
Einstein construction: its residual is much too large at the polynomial
repair scales under study. A controlled fixed-power-logarithmic quotient
inverse would still suffice to improve the exclusion to \(o(\varepsilon)\);
the note states that estimate and the nonlinear parameter requirements
explicitly. They have not yet been proved.

For the graph-manifold strategy, the relevant construction problem now
explicitly requires a positive-sectional-curvature, charged region. The
missing estimate is a relation between its compulsory pointwise size and
its physical volume or matching cost, not another scalar profile satisfying
only a subset of the Ricci equations.

For rigidity, an all-Einstein obstruction for the unmodified construction
objects must use information beyond the numerical monopole band just
tested, or a genuinely different input family must be built. This leaves
both existence and counterexample directions open.

The checks and their exact scope are listed in
[the verification record](round5_verification.md). The arguments are local
research results built on the specified earlier proofs; publication
priority has not been established.
