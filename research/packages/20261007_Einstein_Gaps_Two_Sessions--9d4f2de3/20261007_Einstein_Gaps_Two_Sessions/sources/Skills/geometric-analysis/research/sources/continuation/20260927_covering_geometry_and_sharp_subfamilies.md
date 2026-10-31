# Local covering geometry, sharp surgery costs, and first-order ALE matching

27 September 2026. Continuation from local commit `46e7efc`.

This manuscript continues the actual-field theory; it does not replace the
frozen research library. The inherited results used here are the bounded
actual-form supplier, the local incompatibility theorem, and the conformal
minimizing-sequence reduction in
[the preceding continuation](20260927_conformal_separation_and_zero_end.md).
The unrestricted integral zero-end problem and the best coefficient on the
balanced blowup/handle family are not assumed solved.

The first connection strengthens base collapse to collapse of **local
universal covers**, then uses verified smoothing inputs to exclude further
approximate geometries. The second determines an exact all-metric infimum
on a real subfamily and removes scalar energy from the remaining chiral
filling criterion. The third excludes a precisely stated global ALE
matching mechanism, retaining the first-order source and then weakening
pointwise decay to finite energy. Classical geometric and gauge inputs
are distinguished from these deductions.

## 1. Local covering volume detects the forbidden curvature mode

Let a closed oriented four-manifold carry a smooth metric with
`|Ric|<=K`, a smooth self-dual two-form `|omega|<=L`, and a constant
`t in [0,1/4]`. Set

\[
 Z_t=|\operatorname{Ric}+g|^2+
 |W^+-t(|\omega|^2 I/3-\omega\otimes\omega)|^2
 +( |\omega|^2-2)^2+|d\omega|^2.                 \tag{1.1}
\]

For a fixed radius rho>0 let

\[
 \pi_x:(\widetilde {B_{4\rho}(x)},\tilde x)
                   \longrightarrow(B_{4\rho}(x),x),\qquad
 w_\rho(x)=\rho^{-4}
       \operatorname{Vol}_{\pi_x^*g}B_\rho(\tilde x)   \tag{1.2}
\]

be the local universal cover with the lifted metric. This is not the
universal cover of the whole manifold and not an exponential chart.

**Theorem 1 (covering-volume fraction).** If G is any measurable set of
centers with `w_rho(x)>=v>0`, then

\[
 \boxed{\frac{\operatorname{Vol}(G)}{V}
                  \le C(K,L,\rho,v)\fint_M Z_t.}      \tag{1.3}
\]

There is no bound on covering multiplicity, diameter, total volume,
sectional curvature, or the base injectivity radius.

**Proof.** The local coercivity argument of the preceding manuscript,
Theorem 6, applies on a ball of any fixed radius. It gives

\[
 \int_{B_{2\rho}(\tilde x)}\pi_x^*Z_t
                  \ge\epsilon(K,L,\rho,v)>0.         \tag{1.4}
\]

Only interior balls are used. Although the covering of an open ball need
not be complete, all balls involved here have a definite buffer from its
metric boundary; geodesics of length at most 2rho starting at the center
stay over B_{2rho}(x). The interior volume comparison, harmonic-coordinate
and compactness arguments are therefore valid. One can also repeat the
proof directly on these buffered balls. On rescaling the radius, the
limiting equation is Ric=-rho^2 g rather than Ric=-g; rho is fixed, its
constant is strictly negative, and the forbidden parameter interval is
rescaled by the same factor. Thus no scale-invariance of the normalized
equation is being presumed.

Let `c_x(theta)` be the cut time on this cover. Polar integration **before
the cover cut time**, followed by Bishop's radial Jacobian upper bound,
gives

\[
 \begin{split}
 \int_{B_{2\rho}(\tilde x)}\pi_x^*Z_t
 &\le C(K,\rho)\int_{S_xM}
       \int_0^{\min\{2\rho,c_x(\theta)\}}
                    s^3Z_t(\exp_x(s\theta))\,ds\,d\theta\\
 &\le C(K,\rho)\int_{S_xM}\int_0^{2\rho}
                    s^3Z_t(\exp_x(s\theta))\,ds\,d\theta .
                                                        \tag{1.5}
 \end{split}
\]

The last inequality drops the cut restriction only after replacing the
Jacobian by its upper bound; it uses nonnegativity of Z. It does not apply
Bishop comparison beyond a conjugate point. The projected geodesic can
cross the cut locus of the base without affecting the argument.

Integrate (1.4)--(1.5) over G and enlarge the nonnegative right side to
all centers. The Liouville measure on the unit tangent bundle is preserved
by the geodesic flow of the **original single metric g**. Hence

\[
 \begin{split}
 \epsilon\operatorname{Vol}(G)
 &\le C(K,\rho)\int_0^{2\rho}s^3
    \int_{SM}Z_t(\exp_x(s\theta))\,d\theta\,d\mu(x)\,ds\\
 &=C(K,\rho)|S^3|\frac{(2\rho)^4}{4}\int_M Z_t.
                                                        \tag{1.6}
 \end{split}
\]

This proves (1.3), with no counting of sheets. QED.

The needed local coercivity is itself based on a regular harmonic chart
from [Cheeger--Naber](https://arxiv.org/pdf/1406.6534) and the local
incompatibility of negative Einstein ASD almost-Kaehler geometry in
[Armstrong, Theorem 3.3.5](https://johnarmstrongmaths.com/publications/resources/thesis.pdf).
Its proof, including the t>0 Bianchi case, remains in the preceding
manuscript, Section 8. The new step here is the cover-to-base averaging.

For a sequence with uniformly bounded Ricci and amplitude and
`avg Z_t -> 0`, (1.3) implies, for each fixed rho and v, that the fraction
where `w_rho>=v` tends to zero in outer measure. Indeed the continuous
geodesic-average right side of (1.5) is at least epsilon at every such
center, giving a measurable majorant for that level set. Bishop
comparison also bounds w_rho above by a constant depending only on K,rho.
Splitting into `w_rho<v` and its complement yields convergence of the
normalized upper integral, without asserting an unproved measurability
property of the family of covers:

\[
                        \fint_M^{*} w_\rho\longrightarrow0. \tag{1.7}
\]

This is stronger than base collapse. It is not pointwise collapse at every
center and does not produce a sequence realizing such degeneration.

## 2. Actual monopoles and maximal-rank collapse

The inherited actual supplier, for beta>=4 and positive projection p,
gives the SAME bounded form with `L=3 sqrt(2)`, `t=1/beta`, and

\[
 \fint Z_t\le C\left(r_{\rm Ric}+D_\beta/V\right)+o(1),
 \qquad r_{\rm Ric}=\fint|\operatorname{Ric}+g|^2.     \tag{2.1}
\]

The last allowance is freely selectable in the auxiliary construction;
the geometric set G is independent of it. Send that allowance to zero
after applying Theorem 1. No class-square condition or Hessian budget is
needed in this composition. The actual class must remain fixed through
the auxiliary weights required by the supplier.

**Corollary 2.** Under bounded Ricci,

\[
 \frac{\operatorname{Vol}(G)}V
       \le C(K,\rho,v)(r_{\rm Ric}+D_\beta/V),
                          \qquad\beta\ge4.           \tag{2.2}
\]

In particular a fixed positive volume fraction of locally noncollapsed
universal covers gives a uniform forbidden-endpoint gap, even when the
base collapses everywhere. For the original pointwise input
`delta=||Ric^sharp+I||_infinity,op`, `delta<=1/4`, and
`Vol(G)>=vartheta V`, this becomes

\[
             \delta^2+D_\beta/V
                   \ge\epsilon(\rho,v,\vartheta)>0.  \tag{2.3}
\]

There is a checkable topological source of these good covers.
[Naber--Zhang, Proposition 5.9](https://arxiv.org/pdf/1412.1326), printed
pages 53--54, states: under Ric>=-(n-1), local completeness, GH closeness
of B_2(p) to a specified k-dimensional Ricci-limit ball, and

\[
 \operatorname{rank}\operatorname{Image}
       [\pi_1(B_{\delta_0}(p))\longrightarrow\pi_1(B_2(p))]=n-k,
                                                        \tag{2.4}
\]

the radius-1/2 ball in the local universal cover of B_1(p) has a positive
volume lower bound. Their constants depend on the specified limit ball.
At n=4, after scaling a fixed radius R with `R^2 K<=3`, this provides
the cover volume needed in (1.2) with rho=R/4. Indeed the source controls
B_{R/2} in the cover of B_R; relative volume comparison gives a lower
bound for B_{R/4} in that same cover.

Consequently, a positive fraction of points satisfying these uniform
GH/model and maximal fibered-rank conditions yields (2.2)--(2.3). A
zero-end sequence cannot retain a positive fraction of any such fixed
maximal-rank local collapse geometry. If a fixed GH model controls almost
all centers, the maximal-rank fraction tends to zero; it is not enough
for the base to be collapsed. Without uniform model control one must
retain the alternative that the model constants also degenerate.

This uses the **cover-noncollapse** proposition, not the stronger harmonic
radius theorem with its more restrictive model splitting. Neither a
uniform global fundamental group nor global asphericity is asserted to
imply (2.4).

## 3. A diameter-free upper-energy margin with covering geometry

Retain actual `p>=A>0`, put `T_+=A(1-h)`,
`e=integral |Ric|^2/(8 pi^2 A)`, and

\[
 G(h)=\frac{(4+\sqrt{1-3h})^2}{9},\qquad
                        1/4\le h\le1/3.             \tag{3.1}
\]

Suppose a fixed fraction vartheta of centers has `w_rho>=v`.
Then

\[
 \boxed{\delta_-^2+(G(h)-e)_+
                      \ge c(\rho,v,\vartheta)>0.}    \tag{3.2}
\]

This is a direct continuation of the precise scalar-variance calculation
in Section 13 of the preceding manuscript: replace its diameter-derived
gap by (2.3). To make the dependence transparent, decrease the constant
epsilon in (2.3) to at most 1/16. For delta<=1/8 and `(G-e)_+<=1/16`,
that calculation gives

\[
 \delta^2+\inf_{\beta\ge4}D_\beta/V
           \le200\bigl(\delta+\sqrt{(G-e)_+}\bigr).
\]

Thus `c=min{1/64,epsilon^2/80000}` suffices; the two omitted large-error
cases satisfy the same bound immediately. The calculation keeps the
total scalar variance and never replaces a near-Einstein metric by a
Yamabe metric in a pointwise argument. Since geometric noncollapse was
the sole use of diameter and class-square there, neither a diameter bound
nor `a^2>=T_+` nor an absolute `p>=A_0` is needed here.

For exact Ric=-g the stronger inherited optimization gives

\[
                 e\le G(h)-\min\{1,\epsilon\}^2/288. \tag{3.3}
\]

The margin remains positive at h=1/4. It is a new geometric scope for
the energy wall, not a claim that every topology forces its candidates
into the excluded band. In particular, (3.2) does not supply an Einstein
existence theorem from failure of the obstruction.

## 4. Euler density for curvature-regular elliptic metrics

One can already remove the explicit covering premise in a distinct,
classical elliptic class. [Weber, Theorem 1.1](https://nyjm.albany.edu/j/2017/23-64p.pdf)
gives collapse-independent, unnormalized small-energy regularity for
the critical four-metrics specified there, including Einstein metrics,
constant-scalar-curvature Bach-flat metrics and metrics with harmonic
curvature. Here use these explicitly covered classes; "critical" is not
defined to include an arbitrary metric or an arbitrary variational PDE.

Write R_op for the curvature operator, P for integral |Ric^circ|^2, and
Lambda=8 pi^2 chi(M)/V. Four-dimensional Chern--Gauss--Bonnet gives

\[
                  \int|R_{\rm op}|^2=8\pi^2\chi+P.   \tag{4.1}
\]

For such metrics with `|Ric|<=K` and `Lambda<=Lambda_0`, the normalized
total curvature energy is at most Lambda_0+K^2. Fubini and the Bishop
ball-volume upper bound show that, at a fixed sufficiently small radius
R=R(K,Lambda_0), at least half the centers have curvature energy below
Weber's threshold. Its conclusion bounds sectional curvature on a
uniformly smaller ball. The exponential-development averaging theorem
of the preceding manuscript, Section 11, then gives

\[
                   \fint Z_t\ge c(K,L,\Lambda_0)>0.  \tag{4.2}
\]

The proof is exactly the curvature-energy-to-regular-fraction argument
in Section 12 there, with (4.1) replacing the exact-Einstein identity and
Weber replacing Cheeger--Tian. It does not require that the Ricci error
vanish identically. Composing with (2.1) gives the corresponding actual
gap. This is a genuine approximate-input extension, but keeps the stated
elliptic metric restriction. The next section gives a verified smoothing
route beyond that restriction, with a different, uniform local energy
input. It does not replace that input by an averaged Euler-density bound.

### 4.1. Smoothing supplies the covering geometry, without moving the form

**Comparison-metric lemma.** Suppose the original metric g has bounded
Ricci and admits a complete metric h on the same manifold such that

\[
                      a^{-1}h\le g\le ah,
                  \qquad |\sec_h|\le H.              \tag{4.3}
\]

Then there are rho=rho(a,H)>0 and v=v(a)>0 for which EVERY center
satisfies w_rho>=v in (1.2). In particular

\[
                         \fint Z_t\ge c(K,L,a,H)>0.   \tag{4.4}
\]

**Proof.** Use [Cheeger--Fukaya--Gromov, Theorem 1.3 and definition
(1.1.4)--(1.1.5)](https://www.ihes.fr/~gromov/wp-content/uploads/2018/08/384.pdf),
printed pages 331--332, on the complete metric Sh, S=max(1,2H), with
approximation parameter log 2. After rescaling it supplies a metric k,
uniformly equivalent to h within factor 2 and with |sec_k|<=C_0 S.
At every x there is an actual normal cover of an open set V containing
B_s^k(x), s=rho_0/sqrt(S), on which the lifted k-metric has injectivity
radius at least s. This is the covering assertion in the definition of
their round metric, justified on printed page 365; it is not a claim
that an exponential chart is a cover.

Write a'=2a, so `(a')^-1 k<=g<=a' k`. Choose a dimensional d_0 below
rho_0/2 and 1/(2 sqrt(C_0)), and let
`rho=d_0/(8 sqrt(a' S))`. Then `U=B^g_{4rho}(x)` lies inside B_s^k(x).
The universal cover of U maps, by the lifted inclusion, to the supplied
normal cover of V. This map F is a local isometry for the ORIGINAL g.
Its image on B_rho contains the g-radius-rho ball of the normal cover:
every path of g-length less than rho starting at the marked lift projects
into B_rho^g(x), and thus lifts again to the universal cover of U.
Uniqueness of path lifting gives the asserted surjection on the balls.

The normal cover's g-ball contains its k-ball of radius rho/sqrt(a').
This radius is below its injectivity and curvature scales. Rauch
comparison and `dV_g>=(a')^-2 dV_k` give volume at least
`c_4 (a')^-4 rho^4`. The area formula for the surjective local isometry
gives the same lower bound on the universal cover of U. All these balls
have an interior buffer: a finite-length escaping path cannot lie over
an interior limit point of a covering base, by an evenly covered
coordinate neighborhood. Now apply Theorem 1 with G=M. QED.

The metric h is used only to supply covering volume. The supplied form,
its self-duality, the Ricci error, and the curvature deficit are all
evaluated in g. No assertion that these errors are preserved by smoothing
is needed.

**Fixed-scale nonconcentration corollary.** There is a dimensional
epsilon_L>0 such that, for every fixed 0<r<=1, actual metrics satisfying
delta_-<=1/4 and

\[
             \sup_x\int_{B_r^g(x)}|\operatorname{Rm}_g|^2
                              \le\epsilon_L          \tag{4.5}
\]

obey

\[
 \boxed{\delta_-^2+D_\beta/V\ge c(r)>0,
                              \qquad\beta\ge4.}      \tag{4.6}
\]

With the budgets of Section 3 this also gives
`delta_-^2+(G(h)-e)_+>=c'(r)>0` on `1/4<=h<=1/3`.
No diameter, noncollapse, Euler-density, class-square, exact Einstein,
or critical-metric assumption is added. Here Rm is the FULL four-index
tensor: `|Rm|^2=4|R_op|^2`; adjust epsilon_L by four when using the
curvature-operator convention.

To prove this, [Li II](https://arxiv.org/pdf/0911.3104), Theorem 1.1 and
Section 3, provides a definite-time smoothing under (4.5) and a Ricci
bound. Its metric comparison (3.8) is closed in the proof, and at a
fixed positive time it gives (4.3) with a=2 and
`H<=C max(r^-2,K)`. Compose the comparison lemma with the actual supplier
(2.1), and then with Section 3's algebra.

For source precision: the available arXiv v1 states the complete
noncompact theorem, whereas the [published primary
abstract](https://link.springer.com/article/10.1007/s10455-011-9290-0)
explicitly covers compact manifolds. The published full text was not
retrieved. The compact application also follows from the displayed
Section 3 bootstrap with Hamilton's closed initial existence and
extension: when delta_-<=1/4, Chern--Gauss--Bonnet has
`s^2/24-|Ric^circ|^2/2>=1/4`, hence chi>0 and
`integral |Rm|^2>=32 pi^2`. Decrease epsilon_L below this. Condition
(4.5) forces diam(M)>r; run the local Dirichlet-Sobolev bootstrap on
balls at scale r/10, all properly buffered. The finite-radius covering
and energy estimates then apply unchanged. The integrable Ricci bound
`C t^(-2/3)` in that proof gives the factor-two metric comparison by
integrating in time. Only dimensional constants are reduced. Thus the
use of the compact case is explained, not silently quoted from a
noncompact-only statement.

A directly checkable sufficient hypothesis is a local supercritical
curvature budget: for some eta>0,

\[
                \sup_x\int_{B_1(x)}|\operatorname{Rm}|^{2+\eta}
                           \le\Lambda.               \tag{4.7}
\]

Indeed Bishop comparison and Holder give, uniformly at every center,

\[
 \int_{B_r(x)}|\operatorname{Rm}|^2
 \le\Lambda^{2/(2+\eta)}
                [C(K)r^4]^{\eta/(2+\eta)}.           \tag{4.8}
\]

Choose a fixed r making this less than epsilon_L. Thus (4.6) and the
upper wall hold with constants depending on eta,Lambda, without a
pointwise full-curvature bound. Any specified uniform local L2
equiintegrability modulus also suffices.

Conversely, a pointwise near-Einstein actual zero-end sequence must lose
(4.5) at every fixed radius eventually. Choosing radii tending to zero
diagonally gives actual balls carrying at least epsilon_L of full
curvature energy. This is a necessary concentration statement, not a
classification or construction of its possible bubbles.

An averaged bound chi/V controls total L2 energy per volume, not the
supremum over centers in (4.5). Without an elliptic metric equation,
extending Section 4's Euler-density conclusion requires a verified
buffered LOCAL smoothing and covering argument. The abstract of Li I
alone is not used to declare that stronger extension proved.

## 5. Exact all-metric defect on the handle-only family

Let X be a closed complex-hyperbolic surface in its complex orientation,
`A=c1^2(X)=3 chi(X)>0`. Work in the established actual-monopole surgery
class

\[
 M=X\#k\overline{\mathbb {CP}}^{\,2}
           \#\ell(S^1\times S^3),\qquad
 h=(k+4\ell)/A,\qquad
 \theta=h-6k/A=(4\ell-5k)/A.                       \tag{5.1}
\]

The metricwise scalar estimate supplies S>=S_0=32 pi^2 A, where
`S=integral s^2`. Define

\[
 B=\int|W^-|^2,\quad P=\int|\operatorname{Ric}^{\circ}|^2,
 \quad L_s=\int(s-\bar s)^2,\quad R=P+S/4.
\]

These assumptions and the classical gluing construction are the same as
in the preserved complex-hyperbolic application; neither formal classes
nor formal curvature tensors are substituted for actual metrics.

**Proposition 3 (signed scalar--Weyl identity).** If 0<=theta<=1/3, then
for EVERY smooth metric on M,

\[
 \boxed{\mathcal E-\frac{4\theta}{1+\theta}
   =\frac{(1-3\theta)(S-S_0)/3+16B+(1+\theta)L_s}
                {(1+\theta)R}.}                     \tag{5.2}
\]

In particular the elementary all-metric lower bound is

\[
 \mathcal E\ge
 \begin{cases}
 0,&\theta\le0,\\
 4\theta/(1+\theta),&0\le\theta\le1/3,\\
 1,&\theta\ge1/3.
 \end{cases}                                         \tag{5.3}
\]

**Proof.** Signature and the positive Chern--Weil identity give

\[
 \int|W^+|^2=B+12\pi^2(A/9-k),\qquad
 P=4\int|W^+|^2+S/12-8\pi^2(A-k-4\ell).
\]

Hence

\[
 P=S/12+4B+8\pi^2A(\theta-1/3),\qquad
 \mathcal E=(4P+L_s)/R.                              \tag{5.4}
\]

Substitute (5.4) in (5.2). Every numerator term is nonnegative on the
stated theta interval. When theta>=1/3 instead use

\[
 \mathcal E-1=
 \frac{8\pi^2A(3\theta-1)+12B+L_s}{R}\ge0.           \tag{5.5}
\]

R is nonzero by the positive scalar budget. QED.

**Corollary 4 (exact infimum, no restriction to constructed metrics).**
For k=0 and `0<=h=4ell/A<=1/3`,

\[
                  \boxed{\inf_g\mathcal E(g)=\frac{4h}{1+h}.} \tag{5.6}
\]

The lower bound follows from (5.2), now theta=h. For the upper bound,
the classical shrinking-core gluing sequence on this SAME smooth
manifold satisfies

\[
 R\to8\pi^2A(1+h),\quad
 V\to2\pi^2A,\quad \int s\to-8\pi^2A,
\]

so `E=4-(integral s)^2/(VR)` tends to the right side of (5.6).
The use of this classical construction, originating in
[LeBrun's Ricci-energy calculation](https://arxiv.org/abs/math/0003068),
is already detailed in the boundary continuation. This is an exact
calculation of the project functional from classical budgets and
construction, not a new gluing theory or another proof of I40.

If h=0 the complex-hyperbolic metric attains the infimum. If 0<h<1/3,
equality in (5.2) forces S=S_0, B=0 and L_s=0. The actual ordinary
monopole scalar equality then forces a nonzero parallel positive
spinor. For the handle class its square is a^2=A and

\[
                         c_2(S^+)[M]=(a^2-T_+)/4=\ell>0,
\]

contradicting a nowhere-zero section. Thus the infimum in this open
interval is not attained. This argument does NOT infer Einstein from
the cscK equality statement. At h=1/3 the first coefficient in (5.2)
vanishes; the exact identity is `E-1=(12B+L_s)/R`, and attainment is
not decided by the preceding argument.

More generally, along surgery families with 0<h->0 and `k=o(Ah)`, (5.3)
and the same classical upper construction yield

\[
                         \inf_g\mathcal E(g)/h\longrightarrow4. \tag{5.7}
\]

For the balanced tight-window family, however, `k/A=2h/9+O(h^2)`,
so theta=-h/3+O(h^2). Bound (5.3) is then zero. The all-metric linear
gap proved by I40--I41 is not replaced by this classical calculation;
its best coefficient remains genuinely open on that family.

## 6. A chiral blowdown-cap theorem, with no scalar cost on the caps

For an arbitrary metric on M, suppose only the k blowup cores are removed
and replaced by compatible smooth caps, giving

\[
                         N=X\#\ell(S^1\times S^3).
\]

Require a smooth metric g_N equal to g_M on the full common exterior,
including matched collars. All handle geometry is left unchanged. A
smooth extension is not itself an energy bound. Put

\[
 B_N=\int_N|W_N^-|^2,\quad
 K_+=\int_{\mathrm{cores}_M}|W_M^+|^2,\quad
 C_+=\int_{\mathrm{caps}_N}|W_N^+|^2.                 \tag{6.1}
\]

**Theorem 5 (Weyl-only cap cost).** For 0<=h<=1/3, the exact identity is

\[
 \boxed{\mathcal E_M-\frac{4h}{1+h}
  =\frac{(1-3h)(S_M-S_0)/3+16(B_N+K_+-C_+)+(1+h)L_M}
                        {(1+h)R_M}.}                 \tag{6.2}
\]

In particular, under the inherited actual scalar/projection budget,

\[
 \boxed{\mathcal E_M\ge\frac{4h}{1+h}
       -\frac{16C_+}{(1+h)R_M}
       \ge\frac{4h}{1+h}-\frac{2C_+}{\pi^2 A(1+h)^2}.} \tag{6.3}
\]

Neither scalar, Ricci, opposite Weyl nor volume bounds on the caps are
required. The cap metric does not have to solve a gauge or Einstein
equation. The proof uses actual scalar information on M, not on N.

**Proof.** `tau(N)-tau(M)=k`. Subtract the signature formula for the two
closed metrics, cancelling their common exterior. This gives

\[
                 B_M=12\pi^2k+B_N+K_+-C_+.           \tag{6.4}
\]

Substitute this in (5.4), noting theta=h-6k/A. The k terms cancel:

\[
       P_M=8\pi^2Ah+(S_M-S_0)/12+4(B_N+K_+-C_+).
                                                        \tag{6.5}
\]

Using `E=(4P+L)/R` proves (6.2). All its numerator terms except -16C_+
are nonnegative. Finally the classical beta=2 bound gives
`R_M>=8 pi^2 A(1+h)` (equivalently `D_2=36 pi^2 A(e-1-h-2z)>=0`,
where `z=p/A-1>=0`). This proves the second inequality in (6.3). QED.

Along 0<h->0, `C_+=o(Ah)` suffices for `liminf E/h>=4`, without Yamabe reduction
or the tight opposite-chirality window. If compatible caps are ASD,
then C_+=0 and the finite bound is `E>=4h/(1+h)`. This is a conditional
metric theorem: existence of ASD or arbitrarily cheap compatible caps
for all prescribed boundary metrics is not asserted.

The weaker signed condition `C_+<=B_N+K_+` also suffices for the same
finite lower bound. In particular nonzero cap energy is allowed; only
its uncompensated excess matters. Four-dimensional chiral Weyl energy
is conformally invariant. A conformal change of a filling can repair
the conformal factor of its matching collar, but cannot reduce C_+.

For comparison, subtracting positive Chern--Weil instead of signature
would give only

\[
 P_M\ge8\pi^2(k+4\ell)
          -2\int_{\mathrm{caps}_N}(s_N^2/24+2|W_N^+|^2).
\]

Retaining the signature relation removes the entire scalar cap cost.
This is why controlling all curvature of a cap, or also reversing the
handles, is unnecessarily strong for this target.

Two concrete sufficient regimes for (6.3) are:

- Compatible caps with `sum Vol(C_i)||W^+||_infinity,C_i^2=o(Ah)`.
- Small almost-Euclidean boundary collars, in scaled coordinates
  `ell_i^2(delta+q_i)` with `||q_i||C^2<=epsilon_i`, capped by a smooth
  cutoff of q_i. Then `C_+<=C sum epsilon_i^2`; requiring this sum
  to be o(Ah) is enough. For uniformly smooth ambient collars
  `epsilon_i=O(ell_i^2)`, `sum ell_i^4=o(Ah)` suffices. Since k<=Ah,
  a uniform `max ell_i -> 0` implies that condition.

The cutoff statement follows by scaling to the unit ball, extending the
given small collar tensor smoothly to a slightly larger annulus with
uniform C2 control, and setting it to zero in the interior. Curvature is
O(epsilon_i), its squared integral is O(epsilon_i^2), and the
four-dimensional Weyl integral is scale invariant. This construction
requires the stated controlled collars; small total Ricci error alone
does not supply them.

Conversely, along ANY such actual surgery family with 0<h->0, if
`E/h->c<4`, the second inequality of (6.3) forces EVERY compatible
blowdown cap system to satisfy

\[
                \liminf\frac{C_+}{Ah}
                              \ge\frac{\pi^2}{2}(4-c). \tag{6.6}
\]

This is a necessary chiral boundary cost for any improvement below 4,
not a proof that the cost must vanish. No scalar normalization or limit
`R/(8 pi^2 A)->1` is needed for this conclusion.

Equivalently, for any scalar -4 candidate, (5.4) isolates the exact
remaining quantity:

\[
 P-8\pi^2Ah
 =4\left\{\frac{V-2\pi^2 A}{3}
                    +\int|W^-|^2-12\pi^2 k\right\}. \tag{6.7}
\]

Thus the optimal coefficient question asks whether the volume excess
and opposite Weyl energy must pay the blowup cost, up to o(Ah).
It is not a request to eliminate every ordinary-spinor remainder
separately, nor to cap every surgery in the construction.

### 6.1. Exact cost of a prescribed conformal complex-hyperbolic collar

The sufficient filling condition is geometric, not merely topological.
Its cost can be computed exactly for an important full collar germ.
Let a marked cap be a four-ball with prescribed metric on a full boundary
collar, conformal there to the germ of the radius-r ball in complex
hyperbolic two-space with Ric=-g. Preserve the ball's complex orientation
and its boundary marking. Among all smooth positive-definite extensions
of this exact collar metric,

\[
 \boxed{\inf_{g_C}\int_C|W_{g_C}^+|^2
              =\frac23\operatorname{Vol}_{\mathbb{CH}^2}(B_r).} \tag{6.8}
\]

**Proof.** Extend the prescribed positive conformal factor smoothly over
the ball, producing a reference extension g_0 conformal to the complex
hyperbolic metric. There is no derivative bound on this factor. Since
`W^-=0` and `|W^+|^2=s^2/24=2/3` for the reference metric before conformal
change, conformal invariance gives its chiral energy in (6.8).

Define `b(g)=integral_C(|W^+|^2-|W^-|^2)=4 pi^2 integral_C p_1(nabla^g)`.
For any other extension g_C, canonically identify the two orthonormal
frame bundles; the identification is the identity on their common full
collar. The relative Pontryagin transgression has zero boundary value,
so `b(g_C)=b(g_0)`. Consequently

\[
 \int_C|W_{g_C}^+|^2
       =\frac23\operatorname{Vol}_{\mathbb{CH}^2}(B_r)
                      +\int_C|W_{g_C}^-|^2.          \tag{6.9}
\]

The reference extension attains the lower bound. This proof compares
connections on the SAME marked ball; it does not double two inward
collars without checking their normal derivatives. QED.

For several such collars the exact minimum is the sum of (6.8).
Thus a total reference ball volume o(Ah) is sufficient and necessary for
cheap caps of this specified conformal type. Fixed positive radii on
a positive proportion of k comparable to Ah force order-Ah cost for
these prescribed cuts, even if the widths of the prescribed collars
tend to zero. For full collars conformal to a flat round-ball germ,
the same construction gives an exactly conformally flat cap and C_+=0.
An intrinsically round boundary metric alone is not this full-germ
hypothesis: the normal derivatives of the metric also enter the relative
Pontryagin boundary data.

These statements do not assert that alternative cuts through a given
exceptional neighborhood have the same cost. Finding compatible cuts
with sufficiently small uncompensated chiral cost remains part of the
all-metric coefficient problem.

### 6.2. Round induced boundary does not imply a cheap compatible cap

There are smooth metrics on the standard four-ball with the SAME unit
round induced boundary metric for which every full-collar-compatible cap
has arbitrarily large positive chiral energy. Thus the full-germ clause
in Section 6.1 cannot be replaced by intrinsic boundary geometry alone.

Take a coframe on the unit three-sphere with
`d sigma_i=-2 sigma_j wedge sigma_k` cyclically and
`integral sigma_1 sigma_2 sigma_3=2 pi^2`. For t>0 put

\[
 g_t=dr^2+r^2(\sigma_1^2+\sigma_2^2)
        +r^2F(r)^2\sigma_3^2,
 \qquad F(r)=1+t r^2(1-r^2),\quad 0\le r\le1.       \tag{6.10}
\]

This is smooth at the origin: its difference from the Euclidean metric
is a smooth radial polynomial times the square of the smooth one-form
`r^2 sigma_3`. It is positive definite. At r=1 its induced metric is round,
but its outward principal curvatures are `(1,1,1-2t)`.

Here is an explicit normalization check. With orientation
`dr wedge sigma_1 wedge sigma_2 wedge sigma_3`, write G=F+rF'. In the
orthonormal coframe `(dr,r sigma_1,r sigma_2,rF sigma_3)`, the connection is

\[
 \omega_{10}=\sigma_1,\quad\omega_{20}=\sigma_2,
 \quad\omega_{30}=G\sigma_3,\quad
 \omega_{12}=(F^2-2)\sigma_3,\quad
 \omega_{13}=F\sigma_2,\quad\omega_{23}=-F\sigma_1.
\]

Computing `Omega=d omega+omega wedge omega` gives the signed density

\[
 \begin{split}
 (|W^+|^2-|W^-|^2)d\mu
 &= -\tfrac12\operatorname{tr}(\Omega\wedge\Omega)\\
 &=\frac{d}{dr}\{-4(1-F^2)^2-2r^2(F')^2\}
                       \,dr\wedge\sigma_1\wedge\sigma_2\wedge\sigma_3.
                                                        \tag{6.11}
 \end{split}
\]

Since F(0)=F(1)=1 and F'(1)=-2t, its integral is `-16 pi^2 t^2`.
Pull the metric back by a reflection of the ball, retaining the original
orientation of the domain. The reflected metric still induces the round
boundary metric and has signed integral `+16 pi^2 t^2`.

Relative transgression on the marked ball now proves that every metric
matching this reflected FULL collar satisfies

\[
                     \int_C|W^+|^2\ge16\pi^2t^2.    \tag{6.12}
\]

The local obstruction is exact and survives overall rescaling and
conformal changes. It does not obstruct choosing a different cut farther
out, and does not give a metric with E/h<4. In particular it is not a
counterexample to the unresolved all-metric coefficient conjecture.

## 7. Global first-order ALE matching: a finite-energy obstruction

The positive-charge local cores in the preceding continuation solve the
actual weighted equations, but are not global solutions. Here we analyze
a precise global matching limit, retaining its first-order connection
source rather than declaring a twisted Dirac kernel trivial.

**Theorem 6 (first-order ALE matching).** Let (X,h) be a complete one-ended
hyperkaehler ALE four-manifold, with W_h^+=0, nontrivial free end group
`Gamma subset SU(2)_-`, and `H^1(X;R)=0`. Assume the FULL limiting positive
Spin-c connection, including its determinant twist, admits a global
parallel unitary frame. On an exhaustion suppose actual rescaled fields
have

\[
 \epsilon_j^{-1}\operatorname{Ric}^{\circ}(h_j)\longrightarrow0,\quad
 h_j\longrightarrow h,\quad
 D_{h_j,A_j}\Phi_j=0,\quad
 F_{A_j}^{+,h_j}=i\epsilon_j^2 f_j\sigma_{h_j}(\Phi_j),
 \qquad \epsilon_j\downarrow0,                       \tag{7.1}
\]

and compatible global bundle identifications give

\[
 \nabla_j^+=d+\epsilon_jB+o(\epsilon_j),\qquad
 \Phi_j=\Phi_0+\epsilon_j\psi+o(\epsilon_j),\qquad
 \epsilon_j f_j\longrightarrow0.                    \tag{7.2}
\]

All displayed convergence is local, with the weight convergence locally
uniform. The metric convergence is smooth, the connection expansion is
C1, and the spinor expansion is C2. Phi_0 is nonzero
and parallel. B is a global u(2)-valued one-form in the given frame.
Require only

\[
             dB\in L^2(X),\qquad
             U=d\psi+B\Phi_0\text{ bounded on the ALE end}.   \tag{7.3}
\]

Then U=0. In particular the limiting physical cubic torsion

\[
             T=\sum_i c_h(e^i)\Phi_0
                             \otimes(\Phi_0\wedge U_i)        \tag{7.4}
\]

vanishes. Nonzero calibrated exterior torsion cannot occur in this
same global first-order limit. No pointwise decay of B, or growth bound
on the ungauged spinor correction psi, is required.

**Proof.** Split B into real components b_alpha in a constant u(2) basis,
with b_0 central. The background connection is flat, so its first-order
curvature is dB. The first hypothesis in (7.1) makes the FIRST-ORDER
trace-free positive-spinor curvature self-dual as a two-form, while the scaled weighted equation gives
anti-self-dual first-order central curvature:

\[
            (db_\alpha)^-=0\quad(\alpha=1,2,3),
                    \qquad(db_0)^+=0.               \tag{7.5}
\]

We need an ALE primitive fact: a smooth globally exact, L2, self-dual
or anti-self-dual two-form F=db on X vanishes. Lift the end to an exterior
domain in R4 and extend F to R4 as `F_ext=d(chi b)`, where chi vanishes
on a fixed inner neighborhood and equals one far out. This extension
is closed and L2. Euclidean Fourier/Hodge inversion gives

\[
        \beta=d^*\Delta^{-1}F_{\rm ext},\qquad
        d\beta=F_{\rm ext},\quad
        \|\nabla\beta\|_2\le C\|F_{\rm ext}\|_2,
        \quad\beta\in L^4(\mathbb R^4).              \tag{7.6}
\]

The last assertion is homogeneous Euclidean Sobolev, not a uniform
Sobolev premise on a degenerating closed manifold. Average over the
finite end group to obtain a descending primitive. On the end b-beta is
closed and, since `H^1(S^3/Gamma;R)=0`, equals dq. Subtracting d(eta q),
where eta is supported on the end and equals one far out, produces a
global primitive b_tilde in L4 with db_tilde=F. Euclidean and ALE norms
are equivalent there. For radial cutoffs chi_R, the L4 norm of dchi_R
is uniformly bounded, so Stokes and Holder yield

\[
 \left|\int_X\chi_R F\wedge F\right|
 \le C\|\tilde b\|_{L^4(\{R<r<2R\})}
         \|F\|_{L^2(\{R<r<2R\})}\longrightarrow0.   \tag{7.7}
\]

Definite chirality identifies the limit with plus or minus the total
L2 energy. Thus F=0. Apply this fact componentwise to (7.5), obtaining
dB=0. Since H1(X;R)=0, B=dG for a global skew-Hermitian matrix function;
G need not decay or be bounded.

The first-order Dirac equation is
`D_h psi=-sum_i c_h(e^i) B_i Phi_0`. Variation of the principal symbol
multiplies dPhi_0=0; all connection variations have been retained in B.
Therefore

\[
            \psi'=\psi+G\Phi_0,\qquad D_h\psi'=0,
                                    \quad d\psi'=U.  \tag{7.8}
\]

The bounded derivative makes psi' grow at most linearly. Lichnerowicz
in the global parallel frame says its components are scalar harmonic
functions. Every such function with at most linear growth is constant
on this ALE space: blowdowns u(Rx)/R have subsequential harmonic limits
on the Euclidean end cover bounded by C|x|. The origin is removable;
an entire harmonic function of linear growth is affine. The limit
vanishes at the origin and is Gamma-invariant, hence is linear and
Gamma-invariant. A nontrivial group acting freely on S3 has no fixed
vector, so the limit is zero. Every blowdown vanishes, giving u=o(r).
The Ricci-flat interior gradient estimate then gives du=0. Consequently
dpsi'=U=0. QED.

Bounded U can be replaced by bounded limiting physical torsion T and
current `Z=<Phi_0,U>`. The linearized exact Dirac decomposition, with
rho_0=|Phi_0|^2, gives

\[
        0\le2\rho_0^2|U|^2-|T|^2
                         \le4\rho_0|Z|^2.            \tag{7.9}
\]

In particular an exterior with `|T|^2 -> 128/81` and Z->0 cannot be the
exterior of this same global first-order limit. Exact Einstein is NOT
required: for g_j=epsilon_j^2 h_j, covariant Ricci and its trace-free part
are unchanged, but

\[
 |\operatorname{Ric}^{\circ}(h_j)|_{h_j}
       =\epsilon_j^2|\operatorname{Ric}^{\circ}(g_j)|_{g_j}.
                                                        \tag{7.10}
\]

Thus uniformly bounded PHYSICAL Ricci supplies the first condition in
(7.1). It also supplies the canonical weight condition. For the inherited
majorant its exact rescaling is

\[
 \epsilon_j f_{0,j}=\max\left\{
 \sqrt{\max\{-s_{h_j}+\sqrt6|W^+_{h_j}|,3\epsilon_j^2\}},
                 \frac{(-s_{h_j})_+}{4\epsilon_j}\right\}\longrightarrow0,
                                                        \tag{7.10a}
\]

since s_h=O(epsilon^2) and W_h^+ tends to zero locally. Close smooth
majorants preserve this property. With only the trace-free hypothesis
in (7.1), the separate weight limit in (7.2) must be retained: it does
not follow just by ignoring the majorant's scalar branch.

The stronger pointwise conditions
`B=O(r^-1-delta), dB=O(r^-2-delta), psi=O(r)` give a simpler proof by
boundary Stokes and a decaying gauge primitive, but are unnecessary in
the finite-energy version. For the flat complete limit R4 the harmonic
components can be affine, so U and T are constant. A positive simple
torsion zero still cannot persist in a bounded global first-order limit.
The earlier local core has linearly growing rescaled torsion, not this
bounded exterior matching.

The original averaged budgets do NOT yet supply first-order compactness
at scale epsilon, finite total first-order curvature energy, or nonzero
exterior torsion visible in that same limit. Physical curvature of size
epsilon^-1 on an epsilon-ball has only O(epsilon^2) ordinary L2 cost;
that does not bound first-order curvature on an entire expanding end.
Calibration may move to radii R_j->infinity in bubble coordinates.
These limits cannot be interchanged.

The full trivial limiting Spin-c connection is essential. A parallel
frame of the untwisted spin bundle with an unspecified flat determinant
character would not make the correction components Gamma-invariant
scalar functions.

### 7.1. Bare signed degree is not the missing global constraint

For `E_-=S^- tensor L`, the inherited identity is
`c_2(E_-)[M]=(9a^2+T_-)/4`. If the exterior section is nonzero and N
balls contain positive simple torsion zeros, necessarily

\[
                     N=(9a^2+T_-)/4.                 \tag{7.11}
\]

At the zero endpoint this becomes

\[
  N/V=\frac1{8\pi^2V}\int|W^-|^2
                            +\frac5{12\pi^2}+o(1),   \tag{7.12}
\]

which has the sign compatible with positive cores. Conversely, as a
SECTION problem, the relative Euler obstruction is the only one: the
unit-sphere fiber S3 is 2-connected and the exterior has dimension four.
When (7.11) holds, prescribed nonzero boundary germs with these degrees
extend to a nonzero exterior section. This does not make the extension
the cubic torsion of a monopole. It explains why Theorem 6 retains the
actual Dirac and curvature equations rather than only zero counts.

## 8. What these connections decide, and what they do not

The original obstruction mechanism is unchanged: actual fields detect
curvature modes incompatible with the differential equations. This
continuation identifies additional geometric situations in which that
detection remains quantitative, computes an exact value on a genuine
subfamily, and determines which filling/matching information the next
sharpness and endpoint arguments need.

The general zero-end sequence would have to escape both local-cover
control and the verified smoothing classes. The balanced family's
coefficient below 4 would have to pay a definite uncompensated chiral
filling cost for every compatible blowdown. A local positive torsion core
cannot be matched through the finite-energy, bounded-derivative ALE
first-order model of Section 7. None of these necessary conditions is
itself a constructed escaping sequence.

Still unresolved are the unrestricted weak-error zero endpoint, the
balanced family's all-metric optimal coefficient, and the global Einstein
decision on fixed E_D. The proof does not reclassify these as completed
merely because their remaining mechanisms are now more specific. The
new exact subfamily formula and transgression computations retain their
classical-input status; worldwide novelty is a separate literature task.
