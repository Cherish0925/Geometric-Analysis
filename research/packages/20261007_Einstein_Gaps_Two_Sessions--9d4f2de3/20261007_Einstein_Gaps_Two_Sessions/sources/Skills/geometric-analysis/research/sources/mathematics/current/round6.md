# Yau26: a larger repair obstruction and a charged Einstein neck

20 September 2026.

The original question concerns the existence of some Einstein metric on
the same closed smooth manifold, not necessarily close to a near-Einstein
input. This continuation strengthens the closed-bundle analysis, constructs
actual local Einstein geometry for the connector problem, and tests an
entropy argument on a specific orbifold resolution. It does not settle
either unrestricted four-dimensional branch.

## 1. The closed surface bundle: exact repairs require a linear-size change

Let \(G_\varepsilon\) be the original balanced metrics on the fixed
Dehn-twist bundle \(E_D\), with fibre waist \(\varepsilon\), base waist
\(\beta=\varepsilon^2\), and all other hyperbolic moduli fixed. Write
\(\delta_-(g)=\|g^{-1}\operatorname{Ric}_g+I\|_{\infty,\mathrm{op}}\).
There are constants \(c_*,c_1>0\) such that, for small \(\varepsilon\),

\[
 \boxed{
 \|h\|_{C^2(G_\varepsilon)}\le c_*\varepsilon
 \quad\Longrightarrow\quad
 \delta_-(G_\varepsilon+h)\ge c_1\varepsilon^3.}
\]

There is no symmetry or support condition on \(h\). After reducing the
radius by a fixed factor, the ball contains no Einstein metric of any
Einstein constant: proximity forces a negative constant close to minus
one, and constant scaling returns it to the normalization above. The
existing three-scalar correction has size \(O(\varepsilon^2)\) and defect
\(O(\varepsilon^3)\), so the optimal defect **order in this ball** is cubic.

For every \(h_\varepsilon=o(\varepsilon)\) in geometric \(C^2\), the
sharper coefficient is

\[
 \liminf\frac{\delta_-(G_\varepsilon+h_\varepsilon)}{\varepsilon^3}
       \ge\frac1{16\pi^4(p-1)},
\]

where \(p\) is the fibre genus. This enlarges the previous
\(O(\varepsilon^{3/2})\) exclusion neighbourhood to a fixed fraction of
the actual \(O(\varepsilon)\) geometric shear.

### Why a larger conclusion is now possible

The maximum-norm inverse has a genuine degenerating-collar loss. Instead
of trying to eliminate that loss, use the measure selected by the actual
closed TT detector. On the comparison product, this is

\[
 d\nu=\operatorname{sech}t\,dt\,dA_{F_\varepsilon}.
\]

In this measure, the product Einstein operator has a uniform \(H^2\)
inverse modulo its **entire** bounded kernel

\[
 K=\operatorname{sech}^2t\,(aT+bS)+A+J(t)B,
 \qquad J(t)=\arctan(\sinh t),
\]

including all TT tensors \(A,B\) on the actual closed fibre. A first-order
factorization turns the apparently resonant horizontal operator into a
coercive partner. The TT transfer block has an explicit weighted integral
inverse. These estimates use global integration identities, not a uniform
injectivity radius or maximum-norm TT projection.

Every retained kernel direction has nonpositive quadratic receiver:

\[
 \frac12\int\langle D^2(\operatorname{Ric}+g)[K,K],Q\rangle
       =-\frac\pi8\|B\|_{L^2(F_\varepsilon)}^2\le0.
\]

An exact repair would need the opposite sign to cancel the closed source.
Finite-collar cutoffs, actual monodromy, angular modes, and the nonzero
forcing in gauge covariance all contribute controlled errors. No mode is
discarded because it fails to be a global deformation parameter.

Proofs: [weighted inverse](round6_weighted_inverse.md) and
[actual closed-bundle transfer](round6_construction.md).

The remaining difficulty is now specific. For an arbitrary fixed
\(\|h\|=C\varepsilon\), the terms
\(\varepsilon^2\|h\|\), \(\varepsilon\|h\|^2\), and \(\|h\|^3\)
are all of the same order as the source. Further exclusion requires their
combined signed nonlinear contribution and the actual face matching;
merely improving an inverse constant will not suffice. Distant Einstein
metrics on \(E_D\) remain unrestricted.

## 2. Connectors: an actual charged Einstein neck, not compatible scalars

There are explicit analytic data on \(T^3\) that satisfy every Einstein
constraint and produce an actual metric

\[
 \operatorname{Ric}(g)=-3g
 \quad\text{on }(-\tau,\tau)\times T^3,
\]

with a free isometric \(T^2\) action, nonzero conserved twist charge,
a strictly stable minimal central \(T^3\), and two-sided initial outward
expansion. One choice has, on the central slice,

\[
 \tfrac14\le Q\le1,\qquad
 H'=3-Q\ge2,\qquad
 \tfrac{25}{8}\le K(\text{orbit plane})\le\tfrac72.
\]

The orbit shape varies around the base circle. The construction is not a
radial flat-slice ansatz. The scalar constraint and every momentum
component were computed directly; analytic existence and constraint
propagation use [Koiso, Proposition 6](https://www.numdam.org/article/ASENS_1981_4_14_4_433_0.pdf).

Free finite fibre quotients collapse a fixed-width piece of this exact
Einstein neck while preserving these local curvature and stability
properties. Thus the required positive-curvature charged region cannot
be excluded by a purely local, cover-independent lower bound for its
physical volume.

A second, complete **one-ended** construction realizes actual charge
removal with small full Ricci error. On \(D^2\times T^2\), put

\[
 g_R=\frac{dr^2}{V_R}+V_Rd\vartheta^2+r^2(dx^2+dy^2),
 \qquad V_R=r^2-\frac{m_R(r)}r,
\]

where \(m_R=1\) up to \(R\), vanishes beyond \(2R\), and changes
smoothly on scale \(R\). Its Ricci-error eigenvalues are exactly

\[
 \frac{m_R''}{2r},\ \frac{m_R''}{2r},\
 \frac{m_R'}{r^2},\ \frac{m_R'}{r^2}.
\]

Hence the complete metric is exactly hyperbolic at the outward end and
has \(\|\operatorname{Ric}+3g\|_\infty=O(R^{-3})\). A marked integral
helical torus action gives nonzero core charge and zero end charge; the
mixed equation is checked as well. Finite quotients can simultaneously
keep the active-region volume bounded, preserve a fixed Weyl peak, and
make its total Weyl energy tend to zero.

These two facts are complementary building blocks, not a gluing theorem.
The complete example has a disk quotient; the desired connector has a
cylinder quotient and two ends. The precise task is to continue the
charged neck into two regions where charge removal and all end data can
be matched with small error, without introducing a cap or singularity.
Proofs and complete equations: [connector note](round6_global.md).

There is also a useful conditional reduction. If the charged cylinder
admits a complete Einstein extension with two controlled asymptotically
hyperbolic ends, its possibly nonflat boundary metrics can be slowly
interpolated to flat metrics on the same marked tori. At distance \(T\),
over length \(L\), the full Ricci error is
\(O(L^{-1}+e^{-2T})\). Thus one need not demand exact hyperbolic ends from
the Einstein extension itself. The analytic neck has a reflection
symmetry reducing compatible continuation to one side. Such a complete
extension is not yet constructed, and the resulting large physical end
sections do not automatically match cusps of a fixed closed manifold.

## 3. A concrete resolution where ordinary entropy cannot decide Einstein existence

Use the central involution of the Davis hyperbolic four-manifold. Its
coarse quotient is simply connected and has 122 isolated A1 points;
these are established in
[Fine--Panov, Lemma 26](https://msp.org/gt/2010/14-3/gt-v14-n3-p08-s.pdf).
Resolve them using the fixed negative EH fillings. The resulting smooth
four-manifold \(M\) has

\[
 \pi_1(M)=1,\quad \chi=196,\quad \tau=-122,
 \quad b_+=36,\quad b_-=158.
\]

The existing marked log-Weyl construction applies to these actual
fillings and gives \(\delta_-(g_a)\to0\) with volume tending to
\(156\pi^2\). Yet every metric on \(M\) has zero ordinary volume
entropy. A degree-one blow-down to the coarse orbifold therefore cannot
transfer the orbifold hyperbolic volume into a BCG entropy lower bound.
The orbifold fundamental group and the smooth resolution fundamental
group are different; resolving kills the local torsion generators.

Nor can one complete this particular example by changing complex
structure: \(\chi+\tau=74\) and \(\chi-\tau=318\), so neither
orientation satisfies the necessary almost-complex parity condition.
Neither statement excludes a general non-Kähler Einstein metric.

The natural branched cover does not repair the entropy proof. Pullback
across its branch spheres produces a normal cone angle \(4\pi\), not a
smooth Einstein metric. A product smoothing at vanishing scale requires
unbounded negative normal curvature. The exact topology, covering and
curvature calculations are in [the entropy note](round6_entropy.md).

This is a specific test object with a genuine near-Einstein input, not an
Einstein counterexample. Its unrestricted Einstein existence remains a
well-defined global question, with two tempting shortcuts now explicitly
excluded.

## 4. What to investigate next

For \(E_D\), study the signed source-order nonlinear terms and the
monodromy constraint at the full linear scale. The weighted estimate
already proved should be reused, not replaced by the false uniform
maximum-norm inverse.

For the connector, use the explicit charged neck as actual initial data,
and the complete charge-removal example as a separate asymptotic model.
Their shared interface data and annular topology are the problem to
solve. Local positive curvature is not itself the obstruction.

For the Davis resolution, seek a constraint on **all** Einstein metrics
of the same smooth type, or an actual existence construction. Ordinary
orbifold-degree entropy transfer and changing complex structure cannot
supply that constraint for this object.

The four executable checks and the independent mathematical review are
listed in [the verification record](round6_verification.md). The results
are local research deductions with the displayed hypotheses; no claim of
publication priority or complete resolution of Yau26 is made.
