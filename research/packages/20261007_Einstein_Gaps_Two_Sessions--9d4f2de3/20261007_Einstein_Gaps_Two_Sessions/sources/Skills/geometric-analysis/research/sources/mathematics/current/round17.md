# Round 17: integral calibration, product stability, and the positive branch

22 September 2026.

The three investigations in this round concern different mathematical
objects. Integral calibration is developed on arbitrary smooth metrics
with actual monopole solutions; product stability is analyzed on all
closed hyperbolic surface products, including degenerating ones; the
positive branch is tested on the marked resolution
\(\mathbb{CP}^2\#\mathbb{CP}^2\). None requires the particular shear collar
used in Rounds 15–16.

The earlier shear, Maxwell, compact-core and minimal-surface calculations
remain part of the research. They are not a classification of all possible
Einstein metrics, and they are not used as such here.

## 1. Integral rigidity without a constant-scalar assumption

See [the proof](round17_integral.md) and
[the algebra checks](round17_integral_check.py).

Let an actual unperturbed monopole solution have determinant class \(a\),
with \(A=a^2>0\). Write \(s\) for scalar curvature, \(\rho=|\Phi|^2\),
and set
\[
 B=\int s^2-32\pi^2A,\qquad
 P=\int|\operatorname{Ric}_0|^2,\qquad
 L=\int(s+4\kappa)^2,\quad \kappa>0.
\]
The integrated monopole equations give the exact decomposition
\[
 B=\int(s+\rho)^2+8\int|\nabla\Phi|^2+8\int|F^-|^2.
\]
Thus the scalar excess controls spinor variation even when scalar
curvature is not pointwise bounded.

A smooth radial truncation of the quadratic spinor produces a globally
bounded two-form. Its derivative and its departure from the calibrated
amplitude are controlled by \(B\) and \(L\). Inserting its polynomial
Weyl model into the Hodge and Chern–Weil identities gives quantitative
distance to the Kähler Weyl orbit. The argument does not first change
the metric conformally or impose a Sobolev, diameter or injectivity
radius bound.

In particular, suppose \(\tau(M)=0\), \(A=2\chi(M)>0\), and actual
square-\(A\) monopoles are available for both orientations. For the
curvature **operator** \(\mathcal R\), with its Hilbert–Schmidt norm,
\[
 \int\operatorname{dist}(\mathcal R,\mathscr P_\kappa)^2
 \le \frac32P+\frac{39}{4}B+\frac{75}{8}L.
 \tag{1}
\]
Here \(\mathscr P_\kappa\) is the algebraic curvature orbit of the product
of two surfaces of curvature \(-\kappa\). The full covariant
four-tensor norm has a different normalization.

When \(\bar s=-4\kappa\), put \(D=\kappa^2\operatorname{Vol}-2\pi^2A\).
Then \(B=16D+L\), so (1) is equivalently
\[
 \int\operatorname{dist}(\mathcal R,\mathscr P_\kappa)^2
 \le \frac32P+156D+\frac{153}{8}L.
 \tag{2}
\]
For nonconstant scalar curvature \(D\) need not be nonnegative;
the nonnegative quantity supplied by the monopole equations is \(B\).

**What changes.** The constant-scalar calibration estimate from Round 15
now has an arbitrary-scalar version on the original metric. This extends
the class of approximate metrics to which the integral analysis applies.
It is not a new proof that the realizable product orbit is forbidden.
Exact hyperbolic products make the right-hand side vanish and must
remain admissible.

The next global question is whether the almost-parallel forms and the
curvature control can carry information about periods or gluing which
distinguishes a non-product smooth manifold from a genuine Einstein
product. Formula (1), by itself, does not supply that information.

## 2. The complete linear problem on degenerating products

See [the operator analysis](round17_product_operator.md) and
[the independent coordinate checks](round17_product_operator_check.py).

For \(g=g_B+g_F\), where both surfaces have curvature \(-3\), the
Bianchi-gauged Einstein linearization is
\[
 P_g=\tfrac12\nabla^*\nabla-\mathring R.
\]
The complete tensor decomposition identifies two retained channels:
\[
 \mathcal T(B)\otimes L^2(F)
 \quad\oplus\quad
 L^2(B)\otimes\mathcal T(F),
 \tag{3}
\]
where \(\mathcal T\) denotes surface transverse-traceless tensors.
On these channels the operator is one half of the scalar Laplacian
on the opposite surface. On their orthogonal complement its quadratic
form is bounded below by \(3\|h\|_2^2\), uniformly over genus and
injectivity radius.

The exact product spectral decomposition belongs to classical Einstein
deformation theory. Its role here is to specify the entire retained
operator, rather than select a favorable collar component. The proof
also treats persistence of the complementary coercivity under small
metric perturbations and records the feedback term required when the
complement is eliminated.

Degeneration affects more than the exact kernel. Pinching a geodesic
creates a growing number of genuine TT eigenmodes below every fixed
threshold strictly above \(3/8\). This follows from the scalar
half-collar operator, whose conjugated potential tends to \(3/4\),
and the factor \(1/2\) in \(P_g\). Thus even fixed topology does not
justify a fixed-rank reduction retaining that large a spectral gap.
The statement does not rule out a smaller-gap finite reduction.

**What changes.** The remaining analytic problem is now an explicitly
identified low-channel equation with complementary feedback. It is
not an unspecified failure of invertibility, and it is not repaired
by removing only the genuine Teichmüller kernel. Uniform Hilbert-space
control of the complement is not yet a uniform nonlinear maximum-norm
inverse on a glued manifold.

Jäckel's negative-curvature stability theorem is a useful comparison,
not an applicable black box: it requires strictly negative sectional
curvature and exactly hyperbolic thin parts, whereas product metrics
have mixed sectional curvature zero. See
[the primary theorem](https://arxiv.org/html/2502.16692v2).

## 3. An independent positive-branch restriction

See [the global positive-branch analysis](round17_positive.md) and
[its checks](round17_positive_check.py).

For the marked two-pole resolution
\(M=\mathbb{CP}^2\#\mathbb{CP}^2\), the inherited \(A_1\) construction
has metrics \(g_a\) with
\[
 \|\operatorname{Ric}_{g_a}^{\#}-3I\|_\infty\to0,\qquad
 \operatorname{Vol}(g_a)\to\frac{4\pi^2}{3}.
\]
Every positive Einstein metric \(h\) on the same smooth manifold,
normalized by \(\operatorname{Ric}_h=3h\), would instead satisfy
\[
 \operatorname{Vol}(h)<\frac{4\pi^2}{9}.
 \tag{4}
\]
The argument combines Chern–Weil theory with the classical
Gursky–LeBrun half-Weyl energy gap. It is an application of that
theorem, not a newly established general curvature gap. The primary
statement is [Theorem 1 and Corollary 1](https://arxiv.org/pdf/math/9807055).

Indeed, \(\chi=4,\tau=2\) give
\(\int|W^-|^2=4\pi^2-3\operatorname{Vol}(h)\).
The nonzero half-Weyl tensor contributes at least
\(6\operatorname{Vol}(h)\). The vanishing and equality cases are
excluded by the topology of this simply connected positive-definite
manifold.

Consequently the normalized exact metrics, if any exist, have the
diffeomorphism-invariant relative \(C^0\) separation
\[
 \liminf_{a\to0}\quad
 \inf_{\substack{\operatorname{Ric}_h=3h\\ f\in\operatorname{Diff}(M)}}
 \|g_a^{-1}f^*h-I\|_\infty
 \ge 1-\frac1{\sqrt3}.
 \tag{5}
\]
This follows directly from the four-dimensional volume comparison
under a relative pointwise metric bound.

**What changes.** The positive branch now has an explicit restriction
on every normalized positive Einstein output, not merely on an
equivariant repair or an orbifold gluing family. It still permits
positive Einstein metrics of smaller normalized volume, and says
nothing excluding negative or zero Einstein constants.

## 4. Consequences for the research programme

The results have different scopes:

| Result | Metrics covered | Mathematical step supplied | Not supplied |
| --- | --- | --- | --- |
| Arbitrary-scalar calibration | Smooth metrics with the stated actual monopoles | Integral curvature structure on the original metric | Global product coordinates or all-output nonexistence |
| Product operator decomposition and complementary stability | Hyperbolic products and the stated small perturbations | Full identification of the retained channels and a controlled complement | A nonlinear solution on a non-product closed topology |
| Positive output volume separation | All normalized positive Einstein metrics on the marked \(\mathbb{CP}^2\#\mathbb{CP}^2\) | A global numerical and metric separation from the input family | Absence of all Einstein metrics on that manifold |

No new closed near-Einstein construction or all-sign Einstein
nonexistence theorem is claimed in this round. In particular, neither
symbolic verification nor a new estimate converts these results into
a solution of Yau26.

The full problem remains the existence of dimension-only pinching
thresholds for arbitrary allowed smooth manifolds. For the project's
formulation \(Q_n\iff P_n^+\lor P_n^-\), a complete negative answer
requires failure of both signs in one dimension. The witnesses may
have different, or varying, smooth types. A positive answer requires
the relevant universal quantifiers, not just one construction.

The immediate independent problems are now concrete: extract global
information beyond the realizable product calibration; solve the
retained low-channel equation with its actual exterior response;
and decide whether the positive test manifolds admit exact metrics
outside the excluded neighborhood. These are separate mathematical
questions and need not succeed by the same method.
