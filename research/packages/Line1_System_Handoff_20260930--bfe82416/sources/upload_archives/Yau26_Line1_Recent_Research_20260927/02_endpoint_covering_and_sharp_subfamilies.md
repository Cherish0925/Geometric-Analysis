# Endpoint geometry, actual annuli, and sharp subfamilies

Research snapshot: 844e62f7304d9f890914a6a4370ec39291ddc26e.

Complete recent proofs. The first paper's unresolved bounded-Ricci Euler-density case is later addressed in the second paper's Section 3. Neither version proves an unrestricted integral-Ricci endpoint theorem. The handle-only exact infimum is not the balanced-family coefficient.

Read 00_READ_FIRST.md for superseded statements. Each source below is complete and byte-preserved. Original local links remain relative to their source; locate other texts using Volume 6. Formula numbers restart in each source.


---

## Source 1: 20260927_covering_geometry_and_sharp_subfamilies.md

Original path: continuation/20260927_covering_geometry_and_sharp_subfamilies.md

SHA-256: fdbfa874d5611fe54ad75ad00cd0a2f05946777c2598b6d4922abf09df40ad76

BEGIN COMPLETE SOURCE

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


END COMPLETE SOURCE


---

## Source 2: 20260927_local_geometry_and_variational_extrema.md

Original path: continuation/20260927_local_geometry_and_variational_extrema.md

SHA-256: 68abdebe39870e7e984169eb9b434a88b0a974b98da8e10b7effa494e7c1b7e6

BEGIN COMPLETE SOURCE

# Local unwrapping, annular matching, and variational extrema

27 September 2026. Continuation from `cee6c6b`, on the local branch
`local/yau26-variational-global-20260927`. This file extends the
[covering and sharp-subfamily proof](20260927_covering_geometry_and_sharp_subfamilies.md).
It does not replace the frozen manuscripts or create a web-export packet.

The inherited linear small-h order and scalar-variance removal are premises,
not new results here. Curvature norms, actual-class quantifiers and positive
weight solvability have the conventions of the
[conformal continuation](20260927_conformal_separation_and_zero_end.md).
Statements about smooth minimizers below are conditional on attainment;
they do not supply compactness or a minimizer.

## 1. The exact variational problem behind the remaining coefficient

This section gives a usable connection to the classical quadratic-curvature
problem, rather than a new lower bound. Write

\[
 V=\operatorname{Vol}(g),\quad S_1=\int s,\quad S_2=\int s^2,
 \quad R=\int|\operatorname{Ric}|^2,\quad
 P=\int|\operatorname{Ric}^{\circ}|^2.
\]

When R>0, the project defect and its conformally useful companion are

\[
 \mathcal E=4-\frac{S_1^2}{VR},\qquad
 J=\frac{4P}{R}=4-\frac{S_2}{R},\qquad
 \mathcal E-J=\frac{S_2-S_1^2/V}{R}.                 \tag{1.1}
\]

Assume every conformal class has negative Yamabe sign, as follows from
the actual positive-projection input used in I41. In particular R>0 for
every metric. Let alpha=inf_g E<1. The conformal reduction in I41, Section 3,
gives inf_g J=alpha. Consequently the following **sharp positivity threshold**
is an exact reformulation of that infimum:

\[
 \mathcal Q_{\tau_*}(g):=R+\tau_*S_2\ge0\quad
 \hbox{for every smooth }g,\qquad
 \tau_*=-\frac1{4-\alpha}.                            \tag{1.2}
\]

For each tau<tau_* there is a smooth metric for which Q_tau<0. Indeed,
R/S_2=1/(4-J) whenever S_2>0, and a sequence J->alpha approaches the
right-hand side in (1.2). S_2 cannot vanish identically in this negative
Yamabe setting. No minimizer is used in this argument.

Using the project Weyl-operator norm, Chern--Gauss--Bonnet writes the same
functional as

\[
 \mathcal Q_{\tau_*}
 =2\int|W|^2+
   \frac{1-\alpha}{3(4-\alpha)}S_2-16\pi^2\chi.       \tag{1.3}
\]

Thus an optimal defect is equivalent to an optimal positivity parameter
of an existing quadratic curvature functional. This does not imply that
every quadratic critical metric minimizes E, or that known rigidity
theorems apply in the parameter range (-1/3,-1/4).

### 1.1. What smooth attainment would force

**Proposition 1.** In the preceding setting, a smooth metric attaining
alpha<1 has negative constant scalar curvature, satisfies

\[
 \nabla\mathcal Q_{\tau_*}=0,\qquad
 \mathcal Q_{\tau_*}=0,                              \tag{1.4}
\]

and is a global minimizer of Q_tau*. If 0<alpha<1, this metric cannot be
Bach-flat, Kähler for either orientation, or have parallel Ricci tensor.

**Proof.** If E(g)=alpha, then alpha<=J(g)<=E(g)=alpha by (1.1)--(1.2).
The scalar variance is therefore zero. Its constant value is negative
because the conformal class is negative. Equality in (1.2) gives Q_tau*=0;
global nonnegativity implies stationarity and nonnegative second variation.

Here are direct verifications of the structural exclusions. They do not
require a general classification of quadratic critical metrics.

1. If g is Bach-flat, the first variation of the Weyl energy vanishes.
   At constant scalar s, the gradient of S_2 is -2s Ric^circ. The coefficient
   of S_2 in (1.3) is positive for alpha<1. Hence (1.4) gives Ric^circ=0,
   which would give alpha=0. In particular this excludes either
   half-conformally-flat possibility.

2. For a Kähler surface in its complex orientation,
   R=S_2/2-8pi^2(2chi+3tau). Hence, along Kähler variations with the complex
   structure fixed,
   Q_tau*=(1/2+tau_*)S_2-8pi^2(2chi+3tau).
   The tensor h=Ric^circ is an admissible such variation: the associated
   real (1,1)-form is the Ricci form minus (s/4) times the Kähler form,
   and is closed because s is constant. For sufficiently small real t,
   the perturbed form remains positive. Its derivative of S_2 is
   -2s P, nonzero if P>0. Since 1/2+tau_*>0, (1.4) forces P=0.
   Reversing the orientation changes the topological constant but not
   this calculation.

3. If Ric is parallel, put q=|Ric|^2, constant on M. The classical first
   variation of R reduces to -2 Ric^2+(q/2)g. This follows as well by
   varying the parallel factors: Rm(Ric)=Ric^2. Also S_2=s^2V and
   Q_tau*=0 imply q+tau_*s^2=0. Equation (1.4) therefore reduces to
   Ric^2+tau_*s Ric=0. Each nonzero Ricci eigenvalue is q/s.
   If its rank is r, then q=s^2/r and E=4-r. An E-value strictly between
   zero and one is impossible.

These three contradictions prove the proposition. QED.

For reference, the ambient quadratic first-variation formulas and the
constant-scalar trace equation are classical; see
[Catino, Section 2](https://www.mate.polimi.it/wp-content/themes/mymate/send_new.php?file=qdd205&tipo=1).
The passage from the project infimum to the zero level in (1.4) uses I41.
Catino's nonpositive-sectional-curvature theorem assumes tau>=-1/4;
it is not a theorem covering the tau_*<-1/4 case at issue here.

### 1.2. A stationary version and normalization check

For completeness, the same Euler--Lagrange connection holds for any smooth
E-critical metric with S_1<0, without assuming global minimality.
Under g_t=e^{2tf}g and Delta=d*d,

\[
 \dot V=4\int f,\quad \dot S_1=2\int sf,\quad
 \dot S_2=12\int s\Delta f,\quad
 \dot R=4\int s\Delta f.                             \tag{1.5}
\]

The last identity follows from the four-dimensional Weyl/Chern--Gauss--Bonnet
formula, not an assumption of conformal invariance of Ricci energy.
Stationarity of S_1^2/(VR) gives

\[
 \Delta(s-\bar s)-\frac{R}{S_1}(s-\bar s)=0.
\]

Pairing with s-bar s shows s is constant, since R/S_1<0. At this metric,
the full first variation gives

\[
 \nabla R+\frac{2R}{sV}\operatorname{Ric}^{\circ}=0.
\]

It is precisely the critical equation for Q_tau with
tau=-R/(s^2V)=-1/(4-E), and Q_tau=0. Conversely, a negative-csc critical
point of Q_tau at its zero level, with tau<0, is E-critical. This
equivalence is a variational identity, not a new existence theorem.

### 1.3. Consequences for the actual surgery families

For the complex-hyperbolic handle-only family of I44, 0<h<1/3,
alpha=4h/(1+h) and tau_*=-(1+h)/4. Its sharp quadratic inequality is

\[
 R-\frac{1+h}{4}S_2\ge0.                            \tag{1.6}
\]

This is also checked without the variational reduction: the exact I44
signature identity gives

\[
 R-\frac{1+h}{4}S_2
 =\frac{1-3h}{12}(S_2-32\pi^2A)+4\int|W^-|^2\ge0.
\]

I44 already proves nonattainment; (1.6) is not counted as a second sharpness
theorem. On the balanced family, only c h<=alpha<=4h/(1+h) is known.
Proposition 1 says that any smooth attained subunit minimum there would
have to be genuinely non-Kähler, non-Bach-flat and non-parallel-Ricci.
It neither determines alpha nor rules out such a minimizer.

The remaining coefficient-four target has a useful invariant cancellation.
With D=(3/2)S_2+18W_+-72pi^2p and T=A(1-h),

\[
 \frac89D+32\pi^2(p-A)-\Sigma
 =\frac13S_2+16W_+-32\pi^2A
 =4P-32\pi^2Ah.                                    \tag{1.7}
\]

The selected projection p cancels exactly. Thus merely selecting a larger
p, or averaging the same scalar projection inequality over more sign
classes, cannot by itself close this target. Any use of joint actual
classes must supply additional differential information.

## 2. Directional torsion, rather than the size of a selected projection

The cancellation (1.7) identifies a geometric route that is different from
optimizing the old scalar-slack constant. Here the extra input is a genuine
global compatible almost complex structure, not a normalized spinor defined
only off its zeros.

Let g have scalar curvature -4 and let omega be a smooth self-dual fundamental
form with |omega|^2=2. Define its Lee form by d omega=theta wedge omega and put

\[
 \Theta=\int|\theta|^2,\qquad
 \nu=\int\bigl(|\nabla\omega|^2-|\theta|^2\bigr).
\]

The integrand in nu is nonnegative in dimension four. To see this directly,
complete omega locally to quaternionic self-dual forms omega,omega_2,omega_3,
each of norm squared two, and write
nabla omega=a tensor omega_2+b tensor omega_3. Put
alpha=*(a wedge omega_2), beta=*(b wedge omega_3). The two maps defining
alpha and beta are isometries on one-forms. Therefore

\[
 |\nabla\omega|^2=2(|\alpha|^2+|\beta|^2),\qquad
 |\theta|^2=|d\omega|^2=|\alpha+\beta|^2,
\]

and the difference is |alpha-beta|^2. Its vanishing is the Hermitian
intrinsic-torsion condition; equivalently the Nijenhuis tensor is zero.
This last assertion also follows by inserting the same frame into the
definition of N_J. No particular normalization of |N_J| is needed below.

**Proposition 2 (directional energy bound).** Suppose the actual scalar
budget is S_2>=32pi^2A with A>0, and T=2chi+3tau=A(1-h). Then

\[
 \boxed{
 P\ge4V-8\pi^2T-2\nu+2\Theta
                   +\frac{3(\nu-\Theta)^2}{8V}
 \ge8\pi^2Ah-2\nu+2\Theta
                   +\frac{3(\nu-\Theta)^2}{8V}.}       \tag{2.1}
\]

Only the second inequality uses the scalar budget. In particular,
nu=o(Ah) on a normalized low-defect sequence gives the missing coefficient
four lower estimate. More generally, if h_j->0,
R_j/(8pi^2A_j)->1, and E(g_j)/h_j->c<4, then every compatible global
omega_j satisfies

\[
 \liminf_j\frac{\nu_j-\Theta_j}{A_jh_j}
                  \ge\pi^2(4-c).                    \tag{2.2}
\]

**Proof.** Set Q=<W^+ omega,omega>. The integrated self-dual Weitzenboeck
identity and |d omega|^2=|theta|^2 give

\[
 \int Q=-\frac43V+\frac12(\nu-\Theta).
\]

For a trace-free symmetric endomorphism of a three-dimensional Euclidean
space, |W^+|^2>=(3/8)Q^2 when |omega|^2=2. Cauchy--Schwarz therefore yields

\[
 \int|W^+|^2\ge\frac{3}{8V}\left(\int Q\right)^2
 =\frac23V-\frac12(\nu-\Theta)
                  +\frac{3(\nu-\Theta)^2}{32V}.
\]

The chiral Chern--Weil identity is
P=S_2/12+4int|W^+|^2-8pi^2T. Since S_2=16V, substitution proves the
first inequality in (2.1). The scalar budget says V>=2pi^2A, proving the
second. Finally E=J=4P/R on these constant-scalar metrics, so the assumed
limits give P/(Ah)->2pi^2c. Drop the nonnegative square in (2.1) and
rearrange to obtain (2.2). QED.

The Hermitian torsion formula is classical; a primary formula with the same
Lee convention is given in
[On Four Dimensional Hermitian Manifolds, Proposition 3.1](https://dergipark.org.tr/tr/download/article-file/2984722).
The inequalities above are the displayed direct computation from that
four-dimensional decomposition and the scalar/chiral budgets.

### 2.1. An all-Hermitian-metric bound

**Corollary 3.** Suppose that for every conformal class in question there is
the actual scalar input with the same A>0, and T=A(1-h), 0<=h<=1/3.
Every Hermitian metric in the specified orientation satisfies

\[
 \boxed{\mathcal E(g)\ge J(g)\ge\frac{4h}{1+h}.}     \tag{2.3}
\]

**Proof.** The negative Yamabe representative, normalized to scalar -4,
is still Hermitian for the same complex structure. Thus nu=0. Equation
(2.1) implies P>=4V-8pi^2T. The function

\[
 \frac{4(4V-8\pi^2T)}{8V-8\pi^2T}
\]

is increasing in V when T>0, and V>=2pi^2A makes its denominator positive
and its numerator nonnegative. As J=4P/(P+4V) is increasing in P,
this proves J_hat>=4h/(1+h). The exact conformal formula in I41 says
J(g) is a weighted average of J_hat and 1. The bound in (2.3) is at most
one, so it transfers to g. Equation (1.1) completes the proof. QED.

This covers a natural geometric class and uses no Lee-form smallness. It
does not assert that a balanced surgery manifold is Hermitian, or even
almost complex. If a compatible form is supplied only away from spinor
zeros, (2.1) cannot be applied by deleting those zeros and omitting the
boundary terms. Producing a global form with nu=o(Ah), or controlling
the omitted marked-core terms, remains a substantive extra requirement.

For comparison with the classical parameter inequalities, direct expansion
of D_8 gives

\[
 \frac13S_2+16W_+=\frac8{27}D_8+\frac{64}{3}\pi^2p.  \tag{2.4}
\]

D_8>=0 alone reaches only two thirds of the desired 32pi^2A level when
p=A. At the complex-hyperbolic calibration D_8=36pi^2A, not zero.
Accordingly the known non-saturation of D_8 does not automatically
determine the required first-order variation. The new information in
(2.1) is directional differential control, not an increased projection.

### 2.2. The same criterion tolerates isolated projective singularities

The smooth global almost complex hypothesis in Proposition 2 is stronger
than necessary. Its proof holds for any

\[
 \omega\in W^{1,2}(\Lambda^+),\qquad |\omega|^2=2
 \quad\hbox{almost everywhere}.                       \tag{2.5}
\]

Indeed multiplication by omega identifies one-forms with three-forms
isometrically almost everywhere, so d omega=theta wedge omega defines an
L^2 Lee form. The quaternionic-frame calculation is pointwise algebra
on the weak derivative and gives nu>=0. The integrated Weitzenboeck
identity extends by smooth approximation in W^{1,2}; the approximants
need not have constant length. All curvature coefficients are smooth
on the fixed closed manifold, so every term passes to the limit. Thus
(2.1) and (2.2) remain valid with no removed-boundary term.

For example, let a smooth positive spinor have only finitely many
transverse zeros. Away from these zeros its normalized projective
self-dual form has norm squared two. At a transverse zero, |Phi| is
comparable to distance r and |nabla Phi| is bounded. Therefore its
normalized form has |nabla omega|<=C/r. This is square integrable in
four dimensions. The form extends weakly across the point: an annular
cutoff has squared gradient integral O(r^2), tending to zero, and the
form is bounded. Consequently (2.5) holds even if the smooth manifold
has no smooth global almost complex structure.

This removes the isolated-transverse-zero obstruction to **using the
criterion**, not to proving its smallness premise. Actual spinor zero
sets have not been proved to be transverse here. Codimension-two
projective singularities need not have finite W^{1,2} energy. Nor is
nu=o(Ah) a consequence of transversality alone. A weak unit form is not
being promoted to a smooth complex structure.

### 2.3. A completely smooth test with no normalization at its zeros

There is a second version that accepts every nonzero smooth self-dual
two-form omega. Define

\[
 a=\frac12\int|\omega|^2,\quad b=\frac14\int|\omega|^4,
 \quad V_{\rm eff}=\frac{a^2}{b}\le V,\quad
 T_\omega=\int\bigl(|\nabla\omega|^2-2|d\omega|^2\bigr).
\]

On a scalar -4 metric with the same actual budget,

\[
 \boxed{
 P\ge8\pi^2Ah+4(V-2\pi^2A)
   -\frac83(V-V_{\rm eff})-2\frac ab T_\omega
   +\frac{3T_\omega^2}{8b}.}                         \tag{2.6}
\]

To prove this, the Weitzenboeck identity gives
int<W^+omega,omega>=T_omega/2-4a/3. Also
|(omega tensor omega)_0|^2=(2/3)|omega|^4, so Cauchy--Schwarz yields

\[
 \int|W^+|^2\ge\frac3{8b}(T_\omega/2-4a/3)^2
 =\frac23V_{\rm eff}-\frac{a}{2b}T_\omega
                       +\frac{3T_\omega^2}{32b}.
\]

Insert this into chiral Chern--Weil to obtain (2.6). No derivative of
a normalized form occurs. Thus V-V_eff=o(Ah), (T_omega)_+=o(Ah), and
bounded a/b are sufficient for coefficient four on the normalized
low-defect sequences, including forms with arbitrary zeros.

For the ordinary actual unweighted spinor on scalar -4, take
omega=iF_A^+ and rho=|Phi|^2<=4. Then |omega|^2=rho^2/8, so
b<=a and V_eff>=a. If K=int|nabla_A Phi|^2 and
Q=int(4-rho)^2, the ordinary Weitzenboeck identity gives

\[
 V-V_{\rm eff}\le V-a
       =\frac1{16}\int(16-\rho^2)=\frac K2+\frac Q{16}. \tag{2.7}
\]

The existing actual scalar-slack estimates bound these terms at order
Ah, not at o(Ah); they also do not yet give the needed directional
estimate for T_omega. Hence (2.6) explains a precise remaining loss
without claiming that the supplied smooth form already closes it.

### 2.4. Finite defect estimate with a directional cost

If the actual beta=2 budget is also available, then
R>=8pi^2A(1+h), as in I41. Set t_omega=nu-Theta for a unit form in
(2.5). For 0<=h<=1/3, (2.1) and V>=2pi^2A give

\[
 P-4hV\ge4(1-h)(V-2\pi^2A)-2t_\omega
                                    +\frac{3t_\omega^2}{8V}.
\]

Consequently, on the normalized scalar -4 representative,

\[
 \boxed{\mathcal E\ge\frac{4h}{1+h}
 -\frac{[t_\omega-3t_\omega^2/(16V)]_+}
             {\pi^2A(1+h)^2}
 \ge\frac{4h}{1+h}
 -\frac{(\nu-\Theta)_+}{\pi^2A(1+h)^2}.}             \tag{2.8}
\]

Indeed E-4h/(1+h)=4(P-4hV)/[(1+h)R], and the displayed R lower bound
controls the negative part. Thus the sufficient directional condition
is actually (nu-Theta)_+=o(Ah), weaker than nu=o(Ah). Formula (2.8)
is a finite estimate with an independent first-derivative cost; it is
not an estimate asserting that this cost vanishes for the actual
projective form.

For a nonzero smooth form as in Section 2.3, the scale-invariant replacement
for this cost is

\[
 C_\omega=\frac43(V-V_{\rm eff})+\frac abT_\omega
                         -\frac{3T_\omega^2}{16b}.
\]

The identical argument gives

\[
 \boxed{\mathcal E\ge\frac{4h}{1+h}
       -\frac{[C_\omega]_+}{\pi^2A(1+h)^2}.}         \tag{2.9}
\]

Indeed (2.6) gives P-4hV>=4(1-h)(V-2pi^2A)-2C_omega.
Multiplication of omega by a nonzero constant leaves C_omega unchanged.
For the ordinary actual form, harmonic projection gives a>=2pi^2p,
while b<=a and Cauchy--Schwarz give

\[
 1\le a/b\le V/a\le V/(2\pi^2A),\qquad
 V-V_{\rm eff}\le V-2\pi^2p.
\]

Thus a/b tends to one on the normalized low-defect sequences; its
boundedness is not a further premise there. The smallness of the signed
directional cost is still unproved. In particular t_omega itself can be
rewritten by Weitzenboeck as a directional Weyl contraction; the formula
does not secretly supply new differential control of that contraction.

## 3. The bounded-Ricci Euler-density endpoint gap

The previously open bounded-Ricci version of the Euler-density bridge can
be closed using an explicit classical extension that was not used in I43.
The unrestricted weak-Ricci problem is different and remains open.

For a bounded self-dual form define the nonnegative density

\[
 Z_t=|\operatorname{Ric}+g|^2+
 \left|W^+-t\left(\frac{|\omega|^2}{3}I-\omega\otimes\omega\right)\right|^2
 +(|\omega|^2-2)^2+|d\omega|^2,
 \qquad 0\le t\le\tfrac14.                          \tag{3.1}
\]

**Theorem 4.** Let M be a closed oriented smooth four-manifold, omega a
smooth self-dual form, and t a constant in [0,1/4]. Given finite bounds
K,L,Lambda_0, there is c>0 depending only on these bounds such that

\[
 |\operatorname{Ric}|\le K,\quad |\omega|\le L,\quad
 \frac{8\pi^2\chi(M)}{V}\le\Lambda_0
 \quad\Longrightarrow\quad
 \boxed{\fint_M Z_t\ge c(K,L,\Lambda_0)>0.}           \tag{3.2}
\]

No Einstein equation, diameter, volume lower bound, global Sobolev bound,
or all-center small-energy hypothesis is assumed. The Ricci bound is
pointwise and is **not** removed by this theorem.

### 3.1. The precise classical input

[Cheeger--Tian, Theorem 0.8 and Remark 8.22](https://doi.org/10.1090/S0894-0347-05-00511-4)
give the following bounded-Ricci local input. If |Ric|<=K and the
unnormalized curvature L^2 energy on B_r(x), r<=1, is less than a
threshold epsilon_CT(K), an interior neighborhood has uniformly bounded
C^{1,alpha} and W^{2,q} covering geometry. The bounded-Ricci conclusion
is not a pointwise full-curvature estimate. Fix one finite q>4.

The source was checked in full at the relevant printed pages: Theorem 0.8
on p.489, Remark 8.22 on p.515, and the meaning of covering geometry in
Remarks 2.7 and 4.8 on pp.501 and 507. The original article is also
available in this
[institutional course collection](https://www.math.stonybrook.edu/Courses/MAT683/201001/MAT683S10.pdf).
Remark 4.8 is used to interpret the local coverings, not as an
unconditional fixed-scale regularity theorem. The bounded-Ricci use of
Theorem 0.8 together with Remark 8.22 is also made in
[Lott, Section 3.1](https://math.berkeley.edu/~lott/4d3.pdf).

In particular, rescaling by r^{-2} supplies constants a,Q>0, depending
only on K, and a local diffeomorphism

\[
 F_x:B_{\mathbb R^4}(0,ar)\longrightarrow M,\qquad F_x(0)=x,
 \qquad Q^{-1}g_{\rm Euc}\le F_x^*g\le Qg_{\rm Euc}. \tag{3.3}
\]

This is a harmonic coordinate chart upstairs followed by the genuine
covering projection. It need not be injective downstairs. It is a local
isometry for gamma_x=F_x^*g. The fields and their errors remain those of
the original g; no smoothing of the actual equations is asserted.
The chart retains the fixed C^{1,alpha} and W^{2,q} bounds, not only the
ellipticity displayed in (3.3).

### 3.2. Local isometries suffice for the averaging argument

We use the following extension of I43. Suppose that every x in a
measurable set G has a pointed local isometry
F_x:(N_x,gamma_x,z_x)->(M,g,x), with the 4rho ball compactly contained
in N_x and Vol_gamma B_rho(z_x)>=v rho^4, for fixed rho,v>0.
Then

\[
 \frac{\operatorname{Vol}(G)}V
               \le C(K,L,\rho,v)\fint_M Z_t.         \tag{3.4}
\]

Indeed the buffered local coercivity proved in I42--I43 applies upstairs
and gives int_{B_{2rho}(z_x)}F_x^*Z_t>=epsilon(K,L,rho,v)>0.
In polar coordinates, integrate only up to the gamma_x cut time. The
Ricci bound controls the radial Jacobian by C_J(K,rho)s^3. Drop the
cut-time restriction after making this estimate. Projected geodesics
are original-g geodesics, so

\[
 \epsilon\le C_J\int_{S_xM}\int_0^{2\rho}
           s^3 Z_t(\exp_x^g(s\theta))\,ds\,d\theta.  \tag{3.5}
\]

This pointwise lower bound is now expressed without the choice of local
chart. Integrate over G, enlarge to M by nonnegativity, and use invariance
of original-g Liouville measure to obtain

\[
 \epsilon\operatorname{Vol}(G)
 \le C_J|S^3|\frac{(2\rho)^4}{4}\int_M Z_t.
\]

This proves (3.4). Neither the number of sheets nor measurable selection
of a family of charts enters. An exponential map is not declared to be
a covering map by this argument.

For (3.3), take rho=ar/(8sqrt Q). Uniform ellipticity gives
B_{4rho}^{gamma}(0) contained in the Euclidean ball of radius ar/2,
and

\[
 \operatorname{Vol}_{\gamma}B_\rho(0)
                         \ge\omega_4Q^{-4}\rho^4.
\]

Thus the small-energy charts satisfy precisely the buffered hypotheses.

For these charts the local coercivity also has a direct proof, avoiding
any completeness convention for the upstairs domain. If their local
Z_t integrals tend to zero, harmonic coordinates give C^{1,alpha'} and
weak W^{2,q} subsequential convergence on smaller charts. Bounded Ricci
and small L^2 Ric+g imply small L^q Ric+g for every fixed finite q, by
interpolation. The harmonic-coordinate metric equation makes the limit
Einstein and smooth and upgrades convergence to strong interior W^{2,q}.
Interior d+delta estimates give an H^1 bound for the self-dual forms;
Rellich and their L-infinity bound give strong convergence of their
quadratic models. The limit has Ric=-g, a closed self-dual form of squared
length two, and W^+=t(2I/3-omega tensor omega). At t=0 Armstrong's local
ASD Einstein almost-Kaehler obstruction applies. At t>0 the Einstein
Bianchi identity forces the form parallel, hence t=1/2, outside the
interval. This is the same local contradiction as I42, now directly in
the already regular covering charts.

### 3.3. Selecting a positive volume fraction of good centers

In the curvature-operator convention,

\[
 \int|\mathscr R|^2=8\pi^2\chi+P,
 \qquad \fint|\mathscr R|^2\le
 E_*:=1+K^2+\max\{\Lambda_0,0\}.                    \tag{3.6}
\]

For the four-index Riemann tensor the identity is instead
int|Rm|^2=32pi^2chi+4P; changing conventions only changes the local
energy threshold by four. Bishop comparison gives
Vol B_r(y)<=C_B(K)r^4 for r<=1. Therefore Fubini gives

\[
 \fint_M\left(\int_{B_r(x)}|\mathscr R|^2\right)d\mu(x)
                          \le C_B(K)r^4E_*.
\]

Choose

\[
 r=\min\left\{1,
    \left[\frac{\epsilon_{\rm CT}(K)}{2C_B(K)E_*}\right]^{1/4}\right\}.
\]

Markov's inequality shows that
G={x:int_{B_r(x)}|mathscr R|^2<=epsilon_CT(K)} has volume at least V/2.
At every x in G, (3.3) supplies a chart with the same a,Q,rho,v.
Equation (3.4) now proves (3.2). QED.

In contrast to the earlier global Li-II smoothing argument, this proof
does not require every center to be low energy. The exceptional centers
may retain curvature concentration. No pointwise curvature bound is
deduced there or on general bounded-Ricci metrics.

### 3.4. Actual gauge and topology-only ratio inputs

Use the same bounded actual form supplied in I06/I09, with t=1/beta,
beta>=4. Its estimate is
avg Z_t<=C(r_Ric+D_beta/V)+o(1), where
r_Ric=avg|Ric+g|^2. Sending the freely selectable auxiliary allowance
to zero after applying (3.2) gives

\[
 \boxed{r_{\rm Ric}+D_\beta/V\ge c(K,\Lambda_0),
                           \qquad\beta\ge4.}         \tag{3.7}
\]

The actual structure remains fixed through all weights used to supply
that form. No square-cost Hessian theorem is inserted into this
zero/first-order form argument.

An absolute volume premise is unnecessary if p>=A>0 and chi/A<=B.
For r_Ric<=1, the actual scalar estimate and the trace inequality imply

\[
 32\pi^2A\le S_2\le (4+2\sqrt{r_{\rm Ric}})^2V,
 \qquad \frac{8\pi^2\chi}{V}\le9\max\{B,0\}.        \tag{3.8}
\]

For r_Ric>1, nonnegativity of D_beta already gives a fixed gap. Hence
(3.7) holds with c(K,B) under this topological ratio hypothesis.
If delta_-=||Ric^sharp+I||_{infinity,op}<=1/4, the pointwise Ricci bound
is uniform and r_Ric<=4delta_-^2. Thus

\[
 \boxed{\delta_-^2+D_\beta/V\ge c(B)>0,
                              \qquad\beta\ge4.}      \tag{3.9}
\]

In the existing upper-wall setting, retain p>=A>0,
T_+=A(1-h), h in [1/4,1/3], e=R/(8pi^2A), and all actual input
quantifiers of I43. Its unchanged algebra, with
G(h)=(4+sqrt(1-3h))^2/9, now gives

\[
 \boxed{\delta_-^2+(G(h)-e)_+\ge c(B)>0.}             \tag{3.10}
\]

The bounded-diameter premise and the special elliptic-metric premise
of the earlier versions are no longer needed. This is an upper-energy
exclusion, not a claim that topology alone places every candidate near
that upper wall. In particular it is not a full Yau26 existence theorem.

For the actual complex-hyperbolic surgery family,
chi/A=1/3+k/A-2ell/A<=1/3+h<=2/3. Thus its pointwise-input conclusions
above have a uniform constant without any additional Euler-ratio
assumption. This is a direct application, not a new gauge supplier.

Finally, any sequence with bounded Ricci and bounded form amplitude,
t_j in [0,1/4], and avg Z_{t_j}->0 must satisfy

\[
 \frac{8\pi^2\chi(M_j)}{V_j}\longrightarrow+\infty.   \tag{3.11}
\]

Otherwise a subsequence has a finite upper density bound and contradicts
(3.2). The same conclusion holds for the actual input of (3.7). Constants
remain non-effective because the inherited local coercivity is proved
by compactness. No uniform pointwise Ricci bound has been derived from
the original weak integral defect.

### 3.5. The entire finite pencil, with improved zero-end decay

Retain the exact conventions of I07 and I09:

\[
 b_a=\frac{(-a^2)_+}{V},\qquad
 D_\beta=\frac{\beta+1}{\beta}
              \int(s^2+6\beta|W^+|^2)-72\pi^2p,
 \qquad \kappa_\beta=r_{\rm Ric}+D_\beta/V.
\]

In particular the definition of b_a contains no 8pi^2 factor. Under
the actual solvability of I07 and the geometric hypotheses of (3.2),

\[
 \boxed{(1+b_a)\kappa_\beta\ge
 c(K,\Lambda_0)\frac{(\beta-2)^2}{\beta^2},
                      \qquad 2\le\beta<\infty.}     \tag{3.12}
\]

For 2<=beta<=4 the inherited finite-pencil theorem with cutoff L=4
gives (1+b_a)kappa_beta>=c_4(beta-2)^2, hence at least
4c_4(beta-2)^2/beta^2. For beta>=4, use (3.7) and
(beta-2)^2/beta^2<=1. The smaller of these two constants proves (3.12).
If a^2>=T_+, the inherited compact-interval estimate absorbs b_a;
the tail already has no square cost. Thus the factor 1+b_a can be
omitted under that hypothesis. As in (3.8), p>=A and chi/A<=B replace
the Euler-density premise, with constant c(K,B).

For the compactified pencil P_t=tD_{1/t}, including P_0=6int|W^+|^2,
the elementary inequality r+tD/V>=t(r+D/V) gives

\[
 \boxed{(1+b_a)(r_{\rm Ric}+P_t/V)
       \ge c\,t(1-2t)^2,\qquad0\le t\le\tfrac12.}   \tag{3.13}
\]

The previous unrestricted estimate has t^3 instead of t. This improvement
is proved only with the stated pointwise Ricci and Euler-density control.
At t=0 (3.13) itself is trivial; (3.2) is the nontrivial form statement
at that endpoint. No claim of an optimal exponent is made.

### 3.6. The topology itself can supply the missing density budget

The Euler-density condition can be replaced by a topological ratio,
without a preassigned monopole projection. Put T_+=2chi+3tau and
z=avg Z_t. Directly from (3.1) and chiral Chern--Weil,

\[
 \frac{4\pi^2T_+}{V}
  =\frac23+\frac{16t^2}{3}+O_L(\sqrt z+z).          \tag{3.14}
\]

To verify the error, the model tensor has squared norm
(2/3)|omega|^4. Its average differs from 8/3 by O_L(sqrt z), since
||omega|^2-2| has small L2 norm and omega is bounded. The L2 model-fit
error changes avg|W^+|^2 by O_L(sqrt z+z). Also
avg s^2=16+O(sqrt z+z) and avg|Ric^circ|^2<=z.
Insert these into 4pi^2T_+=2int|W^+|^2+S_2/24-P/2.

For z<=epsilon(L) the right side lies in [1/3,4/3]. In particular
T_+>0 and 3pi^2T_+<=V<=12pi^2T_+. Thus, if T_+>0 and chi/T_+<=B,

\[
 \frac{8\pi^2\chi}{V}\le\frac83\max\{B,0\}.
\]

Theorem 4 now gives z>=c(K,L,B)>0, after including the alternative
z>epsilon(L). If T_+<=0, a stronger direct bound is available:
Chern--Weil gives P>=S_2/12, whence

\[
 r_{\rm Ric}=P/V+\fint(s+4)^2/4
 \ge\fint[s^2/12+(s+4)^2/4]
 =1+\tfrac13\fint(s+3)^2\ge1.                      \tag{3.15}
\]

In particular every fixed oriented smooth four-manifold has a
bounded-Ricci, bounded-form endpoint gap, without a diameter condition.
Its constant may depend on its topology. All actual consequences
(3.7), (3.12), and (3.13) hold with the density assumption replaced by
T_+>0 and chi/T_+<=B. This replacement is derived in the small-defect
regime; arbitrary metrics have not been assigned topologically fixed volume.

### 3.7. Uniformity on the full classical general-type surgery family

Let X be any minimal complex surface of general type, A=c_1^2(X)>0,
and M=X#k CPbar^2#ell(S^1 times S^3), with
h=(k+4ell)/A in [0,1/3]. Keep precisely the actual polarized/chamber
supply in I03, including its b_+=1 and loop-insertion quantifiers.
The selected class has a^2=A-k>=T_+=A(1-h), so b_a=0.

The classical Noether inequality A>=2p_g-4 and the identities
chi_h=1-q+p_g, chi(X)=12chi_h-A imply

\[
 \chi(X)\le5A+36,\qquad \chi(X)/A\le41.
\]

Here A is a positive integer and q>=0. These formulas and the full
scope of Noether's inequality are recorded in
[Liedtke, Theorem 2.1](https://arxiv.org/pdf/math/0702548) and
[Bauer--Catanese--Pignatelli, p.5](https://www.mathe8.uni-bayreuth.de/de/team/prof-fabrizio-catanese-old/pdf/101.pdf).
No regularity or ampleness premise is added to X. Surgery gives

\[
 \frac{\chi(M)}A\le41+h<42,\qquad
 \frac{\chi(M)}{T_+}\le\frac{41+h}{1-h}\le62.        \tag{3.16}
\]

Thus the Euler ratio in the preceding theorems is automatic across this
entire classical family, not just complex-hyperbolic bases. For every
metric on it and every finite beta>=2 there is a universal c>0 such that

\[
 \boxed{\delta_-(g)^2+D_\beta(g,a_g)/V
             \ge c\frac{(\beta-2)^2}{\beta^2}.}     \tag{3.17}
\]

Indeed delta_-<=1/4 supplies a universal pointwise Ricci bound and
r_Ric<=4delta_-^2, so use (3.12), (3.16) and b_a=0. If delta_->1/4,
the left side is at least 1/16 and the right-hand parameter factor is
at most one. Reduce c accordingly. The class can be selected separately
for each original metric, but remains fixed through its auxiliary weights.

The upper-wall consequence (3.10), for h in [1/4,1/3], also has a
universal constant across this family. There is no diameter, volume,
base noncollapse or separately imposed Euler budget. Equation (3.17)
uses the pointwise defect delta_-, not the unrestricted integral E;
it therefore does not assert the still-open integral zero-end theorem.

In fact (3.17) extends to all nonnegative surgery counts, with no upper
bound on h. For h>=1/3 the already established I03 obstruction gives
E>=epsilon_0. Since E<=4delta_-^2, the left side of (3.17) is at least
epsilon_0/4, while its parameter factor is at most one. Combining the
two h ranges proves the same universal pointwise pencil inequality on
the entire eligible general-type blowup/handle family. This last step
uses the old critical-band theorem; it is not an additional zero-end
regularity assertion beyond (3.16).

## 4. Actual annular matching without a first-order ALE expansion

This is a separate consequence of the actual prolonged equations. It
does not use Section 3's pointwise Ricci hypothesis, and does not assert
that the original weak-error sequence has an ALE decomposition.

Use the actual fields of I39/I41: Phi in S^+, determinant connection A,
rho=|Phi|^2<=4, P_spin=nabla_A Phi, zeta=<Phi,P_spin>, and the smooth
cubic torsion t_Phi in E_-=S^- tensor L, L=det S^+. Its induced determinant
connection is 3A. For beta>=4 put

\[
 \rho_\beta=\frac23\sqrt{4(1+1/\beta)},\quad
 U_\beta=\frac43(2/\beta-1),\quad
 m_\beta=-U_\beta\rho_\beta^3/2>0,
\]
\[
 S=m_\beta+2\rho^2|P_{\rm spin}|^2,\quad
 d=2\rho^2|P_{\rm spin}|^2-|t_\Phi|^2\ge0,\quad
 \mathcal J=\frac{(S-2m_\beta)^2}{S},\quad
 \mathcal A=(\rho-\rho_\beta)^2+\mathcal J+d,
 \quad \mathcal R=D^-_{3A}t_\Phi.                    \tag{4.1}
\]

The old Dirac algebra gives d<=4rho|zeta|^2. There is no division by
rho or t_Phi in (4.1). Let eta=kappa_beta+epsilon_aux<=1. Under the
unchanged actual supply and a^2>=T_+, the earlier proofs give

\[
 \int\mathcal A\le C\sqrt\eta V,\qquad
 \int|\mathcal R|^{4/3}\le C\eta^{2/3}V,             \tag{4.2}
\]
\[
 \int_B|F_A|^2\le C\operatorname{Vol}(B)
                      +C(\beta^{-1}+\sqrt\eta)V     \tag{4.3}
\]

for every measurable B. The first two statements are from Sections 2
and 8 of the [mixed-current proof](20260927_mixed_current_and_signed_cores.md).
For (4.3), Section 6 of the
[conformal continuation](20260927_conformal_separation_and_zero_end.md)
supplies the anti-self-dual part. The positive part follows from
|F_A^+|^2=f^2rho^2/8, bounded rho, and the actual weight estimate
int(f-sqrt(4(1+1/beta)))^2<=C eta V. Thus (4.3) concerns the full
determinant curvature, not just one chirality.

### 4.1. Which flat quotient holonomies admit both limiting fields?

Let Gamma be a finite subgroup of SO(4) acting freely on S^3, with its
specified orientation and a flat Spin-c lift. Represent Spin^c(4) as

\[
 \{(A_+,A_-)\in U(2)\times U(2):\det A_+=\det A_-\}.
\]

These representations act on S^+ and S^- respectively, not on E_-.
Suppose both S^+ and E_-=S^- tensor det S^+ have a nonzero invariant
vector. Choose these vectors first in their unitary bases, and write
lambda=det A_+=det A_-. Then

\[
 A_+=\operatorname{diag}(1,\lambda),\qquad
 A_-=\operatorname{diag}(\lambda^{-1},\lambda^2),
 \qquad E_-:\operatorname{diag}(1,\lambda^3).        \tag{4.4}
\]

The real Clifford space can be written as
Q(z_1,z_2)=((z_1,-bar z_2),(z_2,bar z_1)). Direct multiplication gives

\[
 A_-Q(z_1,z_2)A_+^{-1}
                   =Q(\lambda^{-1}z_1,\lambda^2z_2). \tag{4.5}
\]

The character lambda is faithful, since lambda=1 acts trivially on the
tangent space. Its image is finite in U(1), so Gamma is cyclic. Its
action is free precisely when its order n is odd: for even n the element
lambda=-1 fixes the second axis. Conversely all these odd cyclic actions
admit (4.4). Thus the oriented quotient types allowing both invariants
are exactly

\[
                         \frac1n(1,-2),\qquad n\text{ odd}.        \tag{4.6}
\]

Here n=1 is the trivial group. For the usual notation 1/n(1,q), let
zeta generate the roots of unity and delta=zeta^{1+q}. The canonical
lift is A_+^0=diag(1,delta), A_-^0=diag(zeta,zeta^q). A character twist
chi gives S^+=chi A_+^0 and E_-=chi^3 delta A_-^0. A positive invariant
forces chi=1 or delta^{-1}; checking the other representation then gives

\[
 q+2=0\pmod n\quad\hbox{or}\quad2q+1=0\pmod n.      \tag{4.7}
\]

They are the two coordinate orders of (4.6). In these cases the permitted
determinant characters are delta and delta^{-1}. In the fixed marking
1/n(1,-2), this is exactly c_1(L)|_{S^3/Gamma}=+1 or -1 in Z/n.
For odd n the determinant class specifies the Spin-c structure, since
multiplication by two is invertible in Z/n. For n=3 the invariant space
in E_- is two-dimensional, but the two allowed determinant classes are
still distinct. Orientation reversal is not an extra permitted change
of marking.

Call a marked group/lift **nonresonant** when it does not admit these
two invariant vectors. In particular every nontrivial Gamma in SU(2)_-
is nonresonant. This definition is an explicit finite representation
condition, not a new analytical assumption hidden in terminology.

The Spin-c presentation is classical; see
[Haydys, Example 121(b)](https://haydys.net/misc/IntroGaugeTheory_LectNotes.pdf).
Equations (4.4)--(4.7) are the direct representation calculation used here.

### 4.2. Quantitative annular obstruction

Let Q_Gamma={1/2<|y|<4}/Gamma carry its flat cone metric h_C.
Fix a finite family of nonresonant marked groups/lifts. There are
delta_0,c_0>0 such that, for an orientation-preserving embedded annulus
iota:Q_Gamma->M and r>0 with

\[
 \|r^{-2}\iota^*g-h_C\|_{C^2}<\delta_0,
\]

the actual fields restricted to that annulus satisfy

\[
 \boxed{c_0\le r^{-4}\int_{\iota Q_\Gamma}\mathcal A
          +\int_{\iota Q_\Gamma}|F_A|^2
          +r^{-8/3}\int_{\iota Q_\Gamma}|\mathcal R|^{4/3}.}       \tag{4.8}
\]

Only the actual Dirac equation, bounded spinor amplitude, and definitions
(4.1) are needed locally. No first-order ALE expansion, finite energy of
such an expansion, or relation between r and a smaller core scale is
assumed. Constants are not asserted uniform in arbitrary quotient order.

**Proof.** If no such constants exist, take annuli with rescaled metrics
h_j->h_C in C^2 and right side tending to zero. Pass to a fixed group,
Spin-c type, and limit beta in the compactification [4,infinity]. Under
homothetic spinor identification transport the physical t_Phi without
changing its amplitude. This field equals r^{-1}t_{Phi,h}, not the cubic
field recomputed at scale h. Hence

\[
 D^+_{h,A}\Phi=0,\qquad
 D^-_{h,3A}\widetilde t=r\mathcal R,
\]

and the three terms in (4.8) become the integrals of A, |F_A|^2,
and |D^-\widetilde t|^{4/3} on the fixed annulus. S in that A still uses
the physical derivative, equivalently r^{-2}|nabla_{h,A}Phi|^2.

The determinant line is torsion on Q_Gamma and admits a flat connection.
There are finitely many flat characters, so choose a subsequence with
one flat reference A_0. Since H^1(Q_Gamma;R)=H^2(Q_Gamma;R)=0,
abelian Neumann Coulomb gauge gives
||A-A_0||_{W^{1,2}}<=C||F_A||_2->0, hence convergence in L^4.
The same holds for the induced twist in E_-. There is no premise that
the original determinant curvature vanishes.

The positive spinors are bounded; their Dirac equation and interior
elliptic estimates give local W^{1,2} bounds. Their squared norms tend
to rho_beta>0 in L^1. For the opposite spinor, first observe

\[
 \mathcal J\ge S-4m_\beta,\qquad
 \int|S-2m_\beta|
      \le\left(\int\mathcal J\int S\right)^{1/2}.
\]

Thus S->2m_beta in L^1 and |widetilde t|^2=S-m_beta-d->m_beta in L^1.
In particular |widetilde t|^2 is uniformly integrable, also for the
varying volume forms. The Dirac estimate and
||(A-A_0)widetilde t||_{4/3}<=||A-A_0||_4||widetilde t||_2 give
local W^{1,4/3} bounds. This embedding into L^2 is critical, not compact.
Instead use subcritical Rellich to obtain almost-everywhere convergence,
then the preceding uniform integrability and Vitali to obtain strong L^2.

Both limits solve their flat Dirac equations and have constant positive
norm. Interior regularity makes them smooth. The flat Lichnerowicz
identity, applied locally to the constant norm, forces both to be
parallel. They therefore give the two holonomy invariants excluded by
the marked nonresonance condition. This contradiction proves (4.8). QED.

The same proof includes a resonant quotient with a forbidden determinant
class. For example, an annulus marked 1/n(1,-2) with odd n and restricted
c_1(L) not equal to either +1 or -1 has the lower bound (4.8).

### 4.3. Packing bounds at the actual physical scales

Suppose the sequence has annuli as above, from a fixed finite marked
nonresonant family, with overlap at most Lambda and radii r_i<=r_max.
Take r_max smaller than a fixed constant depending on this data. Multiply
(4.8) by r_i^4, sum, use (4.2)--(4.3) on the union, and absorb
C r_max^4 sum_i r_i^4. Since Vol(iota_i Q_i)<=C r_i^4, the result is

\[
 \boxed{\frac{\sum_i r_i^4}{V}\le C\Lambda
  [\sqrt\eta+r_{\max}^4(\beta^{-1}+\sqrt\eta)
                         +r_{\max}^{4/3}\eta^{2/3}].}            \tag{4.9}
\]

If each annulus additionally obeys
r_i^{-4}int_{iota_i Q_i}A<=c_0/2, absorb that term in (4.8), multiply
by r_i^{8/3}, and sum instead. One obtains

\[
 \boxed{\frac{\sum_i r_i^{8/3}}V\le C\Lambda
       [\eta^{2/3}+r_{\max}^{8/3}(\beta^{-1}+\sqrt\eta)].}       \tag{4.10}
\]

The determinant contribution has an absorbable part
C r_max^{8/3}sum_i r_i^4<=C r_max^4 sum_i r_i^{8/3}.
Thus no separate local determinant-smallness condition was inserted.

For comparable radii r_i comparable to r and N>=nu V, along
beta->infinity and eta->0 choose r_max comparable to that r. The terms
with beta^{-1}+sqrt eta can then be absorbed. Equation (4.9), followed
by Young's inequality on r^{4/3}eta^{2/3}, gives

\[
 r=O(\eta^{1/8});\qquad
 \text{under individual calibration (4.10), }r=O(\eta^{1/4}).     \tag{4.11}
\]

These are physical annular-scale restrictions. They allow a much smaller
core scale and do not forbid all separation of scales. Positive Chern
charge alone has not been shown to produce nontrivial quotient annuli,
bounded overlap, or individual calibration. The earlier actual smooth
hyperbolic cores have trivial quotient group. The proof therefore does
not settle the unrestricted zero-end gap by itself.

### 4.4. A stronger count for forbidden positive-spinor lifts

If a fixed marked flat lift has no invariant vector in S^+ alone, the
positive-spinor part of the proof already gives

\[
 \boxed{c_1\le r^{-4}\int_{\iota Q_\Gamma}
                 (\rho-\rho_\beta)^2
                         +\int_{\iota Q_\Gamma}|F_A|^2.}        \tag{4.12}
\]

No opposite-spinor residual or torsion calibration is needed. For a
marked 1/n(1,-2), n odd, write the restricted determinant class as
k in Z/n, using the character zeta as generator. The canonical positive
weights are (0,-1); twisting by zeta^a gives weights (a,a-1) and
k=2a-1. Thus a positive invariant is possible exactly when k=+1 or -1.
Every other determinant class satisfies (4.12).

The inherited amplitude estimate is sharper than the combined (4.2):
int(rho-rho_beta)^2<=C eta V. For bounded-overlap annuli from a fixed
finite family of such lifts, (4.3) and (4.12) give

\[
 \frac{\sum_i r_i^4}V\le C\Lambda
            [\eta+r_{\max}^4(\beta^{-1}+\sqrt\eta)]. \tag{4.13}
\]

Consequently comparable positive-density annuli have r=O(eta^{1/4}),
without torsion calibration. More strongly, if each annulus has
r_i^{-4}int(rho-rho_beta)^2<=c_1/2, then int_{annulus}|F_A|^2>=c_1/2.
Summing and applying (4.3) to the union gives

\[
 \boxed{\frac NV\le C\Lambda(\beta^{-1}+\sqrt\eta)}  \tag{4.14}
\]

after absorbing C N r_max^4 for sufficiently small fixed r_max.
This excludes a positive density of these calibrated forbidden lifts
at *any* smaller radii; escape to arbitrarily small scales does not
evade (4.14). Its topological premise is the actual restricted Spin-c
class on the marked annulus, not just the abstract lens-space boundary.

### 4.5. The resonant alternatives solve the actual local equation

The exceptional types in (4.6) are not merely a failure of a representation
test. They admit actual local solutions for which all three right-hand
terms in (4.8) tend to zero. This construction is on punctured quotient
balls; it makes no smooth-filling or closed-manifold assertion.

Take hyperbolic four-space of sectional curvature -1/3 and a cyclic
group of odd order acting about its center by
(z_1,z_2)->(lambda^{-1}z_1,lambda^2z_2), with the lift (4.4).
In rescaled normal coordinates on a fixed covering ball,
h_r=r^{-2}(exp_p(r\,\cdot))^*g=g_Euc+O(r^2) in every fixed smooth norm.
The radial spin identification is equivariant. Start with

\[
 \Phi_r^0=a e_1+r c\overline z_1e_2,\qquad
 a^2=4/3,\quad c=\sqrt2/3.                          \tag{4.15}
\]

This is equivariant because bar z_1 has character lambda. For the fixed
Clifford matrices C_1=I, C_2=diag(i,-i), the physical flat derivatives
are P_1=ce_2 and P_2=-ice_2, hence C_1P_1+C_2P_2=0. Direct substitution
in the cubic formula gives exactly

\[
 t_{\Phi_r^0}=ac(C_1\Phi_r^0-iC_2\Phi_r^0)
                         =2a^2c e_1,
 \qquad |t_{\Phi_r^0}|^2=128/81.                    \tag{4.16}
\]

To solve the actual equations, use the right inverses from Section 15
of the conformal continuation. On the Euclidean covering ball set
T=(d^*,sqrt2 d^+), R_A=T^*G_D, R_D=D^-G_D, where G_D is the Dirichlet
Laplacian inverse. They are right inverses gaining one derivative.
They commute with the finite group. The O(r^2) perturbation to h_r
preserves bounded right inverses, by a Neumann series, in fixed
C^{k,alpha} spaces. In particular no independent incompatible boundary
values for Phi or the connection are prescribed.

For a spinor in a fixed neighborhood of Phi_r^0 put

\[
 \alpha(\Phi)=R_A(0,\sqrt2 r^2\,2i\sigma_{h_r}(\Phi)),
\]
\[
 \mathcal T(\Phi)=\Phi_r^0-R_D\left[
 D_{h_r,A_0}\Phi_r^0+\tfrac12c_{h_r}(\alpha(\Phi))\Phi\right].
\]

The seed Dirac error is O(r^2). On a ball of radius C r^2 about that
seed, this equivariant map has Lipschitz constant O(r^2) and maps the
ball to itself. Its smooth fixed point satisfies
||Phi-Phi_r^0||_{C^k}+||alpha||_{C^k}<=C_k r^2. At physical scale it
therefore solves

\[
 D_A\Phi=0,\qquad F_A^+=2i\sigma_g(\Phi),\qquad
 \operatorname{Ric}_g=-g,\quad W_g^\pm=0.            \tag{4.17}
\]

The actual majorant is f_0=2, since s=-4 and W^+=0. Returning to physical
derivatives gives, uniformly on the covering ball,

\[
 \rho=4/3+O(r^2),\quad t=2a^2c e_1+O(r),\quad
 \zeta=O(r),\quad |F_A|=O(1),\quad\mathcal A=O(r^2).
\]

The last A is its zero-end definition beta=infinity. For finite
beta->infinity use a^2=rho_beta and c^2=m_beta/(4a^4), obtaining the
same estimates. The actual torsion Dirac identity, or just rescaled
C^1 convergence of t, shows that the third term of (4.8) tends to zero.
Thus all terms on that right side vanish on any fixed-ratio annulus.

There is also uniform control across long local necks. Solve on an outer
cover ball of radius 4R with R->0. The errors above are O(R) or O(R^2)
throughout that ball, not errors at a subsequently chosen inner scale.
The actual torsion equation with W^+=0 gives |D_{3A}t|<=C|zeta||P_spin|
=O(R). On every annulus of scale ell<=R, the three normalized losses
in (4.8) are respectively bounded by

\[
 C R^2,\qquad C\ell^4,\qquad C(\ell R)^{4/3}.        \tag{4.18}
\]

They tend to zero uniformly, including ell/R->0. These are actual local
resonant necks with calibrated nonzero torsion. Their center remains a
quotient singularity when n>1; no actual global class, closed solution,
smooth filling, or boundary matching to an external geometry has been
constructed. They establish the necessary exception in the local
matching theorem, not a counterexample to Section 3 or to Yau26.

Both allowed determinant lifts have such examples. For the other lift
twist (4.4) by lambda^{-1}. The positive representation becomes
diag(lambda^{-1},1), and E_- becomes diag(lambda^{-3},1). The seed
a e_2+r c z_1 e_1 is equivariant and Dirac-harmonic; its physical
cubic torsion is -2a^2c e_2. The identical contraction and estimates
apply. Thus neither of the two permitted determinant classes can be
discarded by a stronger local version of (4.12).

## 5. What an escaping bounded-Ricci sequence must carry

The new results give a sharper description of the remaining endpoint
problem. This section is a consequence of I45 and the inherited exact
characteristic identities, not a further independent gap theorem.

Suppose an actual sequence has beta->infinity, eta->0, a^2>=T_+ and
uniform pointwise Ricci bound. Write

\[
 C_+=c_2(S^+)[M]=(a^2-T_+)/4.
\]

Determinant saturation gives C_+/V=O(beta^{-1}+sqrt eta)->0, while
4pi^2T_+/V=2/3+16/(3beta^2)+O(sqrt eta). The exact rank-two formulas are

\[
 c_2(S^-)[M]=\chi+C_+,\qquad
 c_2(S^-\otimes L)[M]=\chi+2T_++9C_+.               \tag{5.1}
\]

Indeed c_2(S^-)=(a^2+2chi-3tau)/4; tensoring by L adds
c_1(S^-)c_1(L)+c_1(L)^2=2a^2. It follows that

\[
 \frac{c_2(S^-\otimes L)[M]-\chi}{V}
   =\frac1{3\pi^2}+\frac8{3\pi^2\beta^2}
                     +9\frac{C_+}{V}+O(\sqrt\eta). \tag{5.2}
\]

By (3.11), chi/V must tend to infinity. Consequently both negative-
chiral bundles have divergent c_2 density, whereas the positive-spinor
bundle has vanishing c_2 density. The determinant twist changes this by
only a finite limiting density 1/(3pi^2); it does not cause the divergence.

Furthermore chi/T_+->infinity and tau/chi->-2/3. Since T_+ is eventually
a positive integer, chi itself tends to infinity. In particular such a
bounded-Ricci endpoint sequence cannot remain on one fixed smooth topology.

Chern--Gauss--Bonnet also makes the curvature location explicit:

\[
 \frac1V\int|W^-|^2-\frac{8\pi^2\chi}{V}
                  =-\frac23-\frac8{3\beta^2}+O(\sqrt\eta).      \tag{5.3}
\]

Here the bounded actual model gives avg|W^+|^2=8/(3beta^2)+O(sqrt eta),
avg s^2=16+O(sqrt eta), and avg|Ric^circ|^2=O(eta).
Thus the remaining bounded-Ricci escape requires unbounded opposite-Weyl
energy density, even while the full determinant curvature density stays
bounded. This explains exactly which curvature block is not paid for by
the existing positive-spinor second-order budget.

None of (5.1)--(5.3) produces individual bubbles, marked quotient annuli,
or their number. If such annuli are identified separately, Section 4
constrains their actual lifts and costs. In particular the local resonant
examples do not by themselves account for these global characteristic
densities. The outstanding global matching problem is not replaced by a
formal count of singularities.


END COMPLETE SOURCE
