# Hyperbolic surgery: quantitative comparison and the monopole bridge

22 September 2026. This note concerns smooth closed oriented four-manifolds,
not the local Einstein repair problem. Its new compatibility conclusion is
that fixed-piece hyperbolic dilution families stay asymptotically on the
`T / A >= 3/4` side for every positive uniform actual-monopole projection
budget `A`, even with metric-dependent choice among all unknown ordinary
monopole classes. Thus their all-sign nonexistence does not connect to the
actual-monopole integral theorem near `2/3`. Sections 1--3 give the complete
comparison inequality, including its Weyl and volume-stability parameters.
Section 4 resolves a dangerous quantifier in a possible stability shortcut.
No topology-independent pointwise Ricci gap is asserted.

## 1. The exact Ricci-box calculation

Let `f:M -> (N,h)` have nonzero degree `D`, where `h` has sectional curvature
`-1`. Put

\[
 H=|D|\chi(N),\quad V_H=|D|\operatorname{Vol}(N,h)
       ={4\pi^2\over3}H,\quad a={\chi(M)\over H}.
\]

Suppose `0 <= delta < 1` and every Ricci eigenvalue is `-3 x_i`, with
`1-delta <= x_i <= 1+delta`. Write `E0=Ric-(s/4)g` and use the
endomorphism norm on the Weyl operator. The Ricci term in Chern--Gauss--Bonnet
is

\[
 Q={s^2\over24}-{ |E_0|^2\over2}
   ={3\over2}\left((\textstyle\sum_i x_i)^2
                                    -3\sum_i x_i^2\right).
 \tag{1}
\]

It is separately concave, so its minimum on the cube occurs at a vertex.
At a vertex with `m` upper endpoints its value is

\[
 Q_m=6\{1+(m-2)\delta+[(m-2)^2-3]\delta^2\}.
 \tag{2}
\]

Comparison of these five expressions gives the exact box minimum

\[
 {Q_{\min}(\delta)\over6}=
 \begin{cases}
 (1-\delta)^2,&0\le\delta\le1/3,\\
 (1-2\delta)(1+\delta),&1/3\le\delta\le1.
 \end{cases}                                                   \tag{3}
\]

The first branch is attained at four lower endpoints; the second at one
upper and three lower endpoints. This is an algebraically optimal bound
from the Ricci interval alone, not an existence statement for a metric
simultaneously saturating the global comparisons.

BCG's degree inequality and Bishop comparison give

\[
 h(g)^4V\ge81V_H,\qquad h(g)\le3\sqrt{1+\delta},\qquad
 \rho:={(1+\delta)^2V\over V_H}\ge1.
 \tag{4}
\]

The input is the main theorem and Ricci-volume corollary on printed p.734
of [Besson--Courtois--Gallot (1995)](https://www.aimath.org/WWN/entropyrigidity/papers/BessonCourtoisGallot.pdf).
Define the scale-invariant normalized Weyl energy

\[
 \omega={1\over8\pi^2H}\int_M|W|^2.
\]

Chern--Gauss--Bonnet now implies the joint inequality

\[
 \boxed{\quad a\ge\omega+\rho\,b(\delta),\qquad
 b(\delta)=
 \begin{cases}
 [(1-\delta)/(1+\delta)]^2,&0\le\delta\le1/3,\\
 (1-2\delta)/(1+\delta),&1/3\le\delta<1/2.
 \end{cases}\quad}                                           \tag{5}
\]

We use positivity of `b` only for `delta<1/2`. For larger delta, multiplying
a volume lower bound by a negative box minimum reverses its usefulness;
there is no extension of the resulting gap by that argument.

For `0 <= z <= 1` define

\[
 G(z)=
 \begin{cases}
 (1-z)/(2+z),&0\le z\le1/4,\\
 (1-\sqrt z)/(1+\sqrt z),&1/4\le z\le1.
 \end{cases}                                                 \tag{6}
\]

This is the exact inverse of `b` on `[0,1/2]`. If an independent theorem
gives `rho>=1+gamma` and `a-omega` lies in `[0,1+gamma]`, then

\[
 \boxed{\quad \delta\ge
 G\!\left({a-\omega\over1+\gamma}\right).\quad}             \tag{7}
\]

For `delta>=1/2` the bound is automatic. If `a-omega<0`, no metric with
`delta<1/2` satisfies the assumptions. Formula (7) optimizes the algebraic
consequence of the specified three scalar inputs; it does not assert a
sharp geometric infimum.

## 2. What the topology-only inequality does and does not say

For `M_j=N_j#(S^1 x S^3)`, put `H_j=chi(N_j)`. The degree-one collapse
map gives `a_j=1-2/H_j`. For `M=N#N`, its degree-two fold gives
`H=2 chi(N)` and again `a=1-2/H`. The topology-only conclusion, when
`a>=1/4`, is

\[
 \delta\ge {1-\sqrt{1-2/H}\over1+\sqrt{1-2/H}}
          ={1\over2H}+O(H^{-2}).                            \tag{8}
\]

The `N#N` specialization is the inherited `1/(4 chi(N))` asymptotic.
At the algebraic endpoint `chi(M)=0`, the second branch gives the
elementary conclusion `delta>=1/2`.
More generally a fixed number `k` of Euler-loss-two surgeries replaces
`2/H` by `2k/H` wherever such a degree comparison is available.

Nonnegative Ricci curvature is already excluded by (4), since it gives
zero entropy on the universal cover. In particular every nonnegative
Einstein constant is excluded, and positive-normalized relative Ricci
defect cannot be less than one. At negative Einstein normalization,
`delta=0`, (5) contradicts `a<1`. These are all-metrics, all-Einstein-sign
obstructions.

Equality rigidity alone does not replace (8) by a positive constant
independent of `H`. Indeed equality in its derivation would require
simultaneous equality in BCG, the Ricci-box bound, and `W=0`. BCG forces
the Ricci-lower-bound normalization to be hyperbolic, which does not
saturate the opposite corner in (3) when `delta>0`. Thus an individual
metric does not attain the positive threshold. Nonattainment gives no
positive distance of an infimum from that threshold.

There is a useful falsifiable consequence for any hypothetical sequence
with `H_j -> infinity`, `a_j -> 1`, and `delta_j -> 0`:

\[
 1\le\rho_j\le {a_j\over b(\delta_j)}\longrightarrow1,
 \qquad
 0\le\omega_j\le a_j-b(\delta_j)\longrightarrow0.            \tag{9}
\]

The second statement is `integral |W|^2 / H_j -> 0`, not absolute Weyl
energy tending to zero. Even a positive absolute energy cost for each
fixed surgery is compatible with (9). To improve (8) uniformly by this
route requires an extensive estimate such as `omega>=w0>0` or
`rho>=1+gamma0>1`, uniform over the changing topology. A single energy
quantum gives another term of order `1/H_j`.

## 3. The legitimate fixed-target stability improvement

[Bessières--Besson--Courtois--Gallot, Duke 161 (2012)](https://www.math.u-bordeaux.fr/~labessie/bbcg_duke.pdf),
Theorem 1.3, gives a positive relative volume gap for a degree-one map to
a fixed closed hyperbolic target, unless that map is homotopic to a
diffeomorphism. Its constant depends on dimension and target diameter;
no source noncollapse or source diameter bound is an extra assumption.

For the degree-one map `N_j#(S^1 x S^3) -> N_j`, rescale to
`g'=(1+delta)g`. Then `Ric(g')>=-3g'`. The map cannot be homotopic to a
diffeomorphism, already because Euler characteristics differ. Thus

\[
 \rho>1+\gamma(4,\operatorname{diam}N_j),
 \quad
 \delta\ge G\left({1-2/H_j\over
                         1+\gamma(4,\operatorname{diam}N_j)}\right).
 \tag{10}
\]

For one fixed target, this improves the elementary comparison with a
nonexplicit positive amount. For `N#N`, their fixed-target Corollary 1.7
similarly supplies a relative volume gap above `2 Vol(N)` and hence the
same formula with `H=2 chi(N)` and a constant depending on `N`.
This uses the separately stated fixed-degree conclusion of Corollary 1.7;
the failure of a constant uniform in unbounded mapping degree, discussed
next, does not refute that fixed-degree assertion.

The target diameters of unbounded-degree hyperbolic covers cannot remain
bounded: their volumes diverge whereas a hyperbolic ball of bounded radius
has bounded volume. Formula (10) therefore supplies no common positive
constant for this cover family. That is a failure of the available
estimate, not a proof that the actual Ricci infima tend to zero.

## 4. Why composition to a fixed base cannot silently remove the dependence

The printed Theorem 1.6 in the same paper, p.32, states an arbitrary-degree
version with a constant depending only on dimension and target diameter;
its proof is omitted. Taken literally, it would apply after composing
`M_j -> N_j -> N`, and would imply a uniform gap in (10) depending only
on the fixed base `N`. This tempting inference is not used here. Its
uniform-in-degree quantifier conflicts with the following independent
test in even higher dimension. This is a mathematical inconsistency in
that literal reading, not a claim about a published erratum.

Fix a closed real-hyperbolic eight-manifold `X` and an exotic eight-sphere
`Sigma`. The Farrell--Jones construction, as stated by Farrell in
[Farrell--Ontaneda, Theorem 1](https://arxiv.org/pdf/math/0402173), gives,
for `eta_j -> 0`, finite covers `X_j -> X` and metrics `k_j` on
`Y_j=X_j#Sigma` with sectional curvatures in `(-1-eta_j,-1+eta_j)`,
although `Y_j` and `X_j` are not diffeomorphic. The original paper is
Farrell--Jones, JAMS 2 (1989), 899--908, DOI
`10.1090/S0894-0347-1989-1002632-2`; the publisher PDF could not be fetched
in this run. The linked primary-author account supplies precisely the
fixed-base, finite-cover, pinching statement used below.

Here is direct volume control, avoiding an unverified sharp simplicial
volume estimate. Sectional evaluation is an injective linear map on the
finite-dimensional space of algebraic curvature tensors. Norm equivalence
therefore gives

\[
 |\operatorname{Rm}_{k_j}-\operatorname{Rm}_{-1}|\le C_8\eta_j.
\]

The normalized Euler density is a degree-four polynomial of curvature;
at constant curvature `-1` it is `c_8=2/Vol(S^8)>0`. Consequently

\[
 |e(k_j)-c_8|\le C'_8\eta_j.
\]

Since `chi(Y_j)=chi(X_j)=c_8 Vol(X_j)`, Gauss--Bonnet gives, for a
dimension-dependent `C` and small `eta_j`,

\[
 {1\over1+C\eta_j}\le
 {\operatorname{Vol}(Y_j,k_j)\over\operatorname{Vol}(X_j)}
 \le {1\over1-C\eta_j}.                                    \tag{11}
\]

Set `k'_j=(1+eta_j)k_j`; then `Ric(k'_j)>=-7k'_j`, and the volume ratio
still tends to one because volume rescales by `(1+eta_j)^4`. Composing
the connected-sum homeomorphism `Y_j -> X_j` with the cover to `X`
gives degree `d_j` and

\[
 {\operatorname{Vol}(Y_j,k'_j)\over d_j\operatorname{Vol}(X)}
 \longrightarrow1.                                        \tag{12}
\]

If this composite map were homotopic to a smooth covering, its induced
subgroup determines the cover `X_j`; uniqueness of the smooth lifted
structure would make `Y_j` diffeomorphic to `X_j`, a contradiction.
Thus a dimension-and-fixed-base-only version of Theorem 1.6 cannot hold
uniformly in mapping degree as printed. A corrected dependence or a
separate four-dimensional proof is required before using that shortcut.
Nothing in this test constructs a four-dimensional Ricci approximation
or excludes all Einstein metrics on the eight-dimensional examples.

## 5. A quantitative all-monopole separation for the dilution family

Use the actual fixed-piece construction of
[round18_integral_limits.md](round18_integral_limits.md):
`M_j=N_j#(S^1 x S^3)` agrees with the hyperbolic metric outside one fixed
deleted ball `B`, and a single fixed metric `k` on the replacement `K`
supplies the whole modification. Put

\[
 H_j=\chi(N_j),\quad T_j=2\chi(M_j)+3\tau(M_j)=2H_j-4,
 \quad q=-s+\sqrt6|W^+|.
\]

Hyperbolic four-manifolds have signature zero. A connected sum with
`S^1 x S^3` changes neither the intersection form nor its signature.
On the exterior `s=-12`, `W^+=0`, and `q=12`. Therefore

\[
 \int_{M_j}q^2=144\operatorname{Vol}(N_j)+C_q,
 \quad C_q=\int_K(-s_k+\sqrt6|W_k^+|)^2-144\operatorname{Vol}(B),
 \tag{13}
\]

where `C_q` is independent of `j`; it need not be positive. For all
sufficiently large `j`, `b^+(M_j)>=2`, since `tau=0` and
`b_2=H_j-2+2b_1(N_j) -> infinity`.

Let `C(M_j)` be the finite set of all real ordinary monopole classes;
when it is empty, take its maximum projection norm to be zero.
Distinguish the invariant from [round5_rigidity.md](round5_rigidity.md)
from the infimum restricted to actual metric period planes:

\[
 \alpha_{\rm all}^2(M_j)=
 \inf_{P\in\operatorname{Gr}_{b^+}^{+}}
                 \max_{c\in C(M_j)}(c_P^+)^2,
 \qquad
 A_{\rm met}(M_j)=\inf_{g\text{ smooth}}
                 \max_{c\in C(M_j)}(c_g^+)^2.
\]

Every metric period plane is a maximal positive plane, so
`alpha_all^2 <= A_met`. We do not identify these two infima or assume
surjectivity of the metric period map. A number `A_j>0` is a uniform
actual-monopole projection budget if every smooth metric admits some
actual class `c_g` with `(c_g^+)^2>=A_j`. Such a choice may depend on the
metric and need not be continuous. Its defining property directly gives

\[
 A_j\le\inf_g\max_{c\in C(M_j)}(c_g^+)^2=A_{\rm met}(M_j).
 \tag{13a}
\]

The classical conformal-monopole inequality
`72 pi^2 (c_g^+)^2 <= integral q^2` applies to each class for this same
metric; see [LeBrun, Theorem 2.3](https://arxiv.org/pdf/math/0003068).
The square, without positive-part truncation, suffices here and requires
no sign condition on the curvature of `K`. Hence (13) gives

\[
 \boxed{\quad
 \alpha_{\rm all}^2(M_j)\le A_{\rm met}(M_j)
                    \le {8\over3}H_j+c_q,
 \qquad c_q={C_q\over72\pi^2}.
 \quad}                                                     \tag{14}
\]

The same fixed-piece test metric bounds the maximum over all classes,
and hence bounds `A_met` itself, not merely the infimum over all abstract
positive planes. Together with (13a), this covers unknown classes and
arbitrary metric dependence of their selection. It assumes
neither a uniform negative square bound for classes nor an Einstein
metric on `M_j`. If `A_met=0`, there is no positive uniform projection
budget to feed into the integral theorem. Vanishing of `alpha_all^2`
alone would not justify that conclusion.

For every positive uniform budget `A_j`, including `A_met` itself when
positive, sufficiently large `j` therefore satisfies

\[
 \boxed{\quad
 {T_j\over A_j}
 \ge {2H_j-4\over (8/3)H_j+c_q},\qquad
 \liminf_j{T_j\over A_j}\ge{3\over4}.
 \quad}                                                     \tag{15}
\]

With `c_q^+=max(c_q,0)`, the explicit sufficient threshold

\[
 H_j\ge36+{51\over8}c_q^+
 \quad\Longrightarrow\quad
 {T_j\over A_j}\ge{17\over24}
              ={2\over3}+{1\over24}                         \tag{16}
\]

follows by multiplying out the positive denominator. For completeness,
if `v=sum t_i c_i` is a convex combination of classes and `P` is positive,
then `v^2 <= (v_P^+)^2 <= sum t_i(c_{i,P}^+)^2 <= max_i(c_{i,P}^+)^2`.
Thus `beta_all^2<=alpha_all^2<=A_met`, while restricting to special
classes gives `beta_sp^2<=alpha_sp^2<=alpha_all^2<=A_met`. The same
separation applies to all these invariants when positive. This is stronger than merely
observing that the current integral theorem fails to prove a gap on the
family: the numerical invariant itself stays away from its critical band.

The proof also applies to a fixed number `k` of these connected-sum
operations, or to fixed-number connected sums of growing covers joined
by fixed metric connectors. Let `H_j` be the sum of hyperbolic Euler
characteristics and suppose the resulting topology has
`tau=0`, `chi=H_j-2k`. The metric modification contributes a fixed constant
to (13), so

\[
 {T_j\over A_j}
 \ge {2H_j-4k\over(8/3)H_j+c_q},\qquad
 H_j\ge36k+{51\over8}c_q^+
 \ \Longrightarrow\ {T_j\over A_j}\ge17/24.
 \tag{17}
\]

Reversing orientation changes the fixed constant to the one computed
with `W^-`, but not the `3/4` limit or the form of the explicit threshold.
These metrics have a fixed, nonzero maximum Ricci defect. Equations
(14)--(17) are not a construction of decreasing maximum defect. They
show why replacing the missing pointwise estimate by the existing
near-`2/3` actual-monopole argument does not settle these surgery types.

## 6. Precisely what remains testable

A pointwise counterexample from the growing-cover surgery family would
have to provide actual metrics with `delta_j -> 0` and satisfy (9).
A proof of a uniform pointwise obstruction would need an additional
uniform estimate: for example an extensive volume excess, extensive
Weyl cost, or a local surgery obstruction that controls the maximum
defect independently of the ambient hyperbolic volume. Neither the
Ricci-box algebra, an absolute energy quantum, nor equality
nonattainment supplies such an estimate. The known fixed-piece metrics
test the integral quantifier, while (14) tests the monopole-bridge
quantifier; neither decides the outstanding pointwise construction.

`round19_global_gap_check.py` checks the box polynomials, their exact
minimum branches, inversion of (5), and the explicit all-monopole-band
threshold. These are algebraic verifications, not computer proofs of
BCG, stability, or monopole existence.
