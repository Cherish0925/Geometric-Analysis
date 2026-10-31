# Step 73: adiabatic anisotropy tails and the remaining core-entry problem

Session: S0910A03. Agent1 / Orchestrator. Explore.

## 1. Scope corrections inherited from Step 72

The exact equation

\[
 \operatorname{div}(e^\sigma\nabla d)=0,
 \qquad d=b-c,
\]

has a valid finite-cylinder rigidity consequence: in the diagonal,
orthogonally-transitive metric

\[
 g=e^{2\phi}(dt^2+dz^2)+e^{2b}dx^2+e^{2c}dy^2,
\]

reflection Neumann data at the inner face and constant Dirichlet data at the
outer face force an exact Einstein solution to have constant `d`.  It does not
exclude small-defect solutions.  For

\[
 E=\operatorname{Ric}+3g
\]

the actual equation is

\[
 \operatorname{div}(e^\sigma\nabla d)
 =-e^{\sigma+2\phi}(E_x-E_y).
\]

The coordinate source is weighted by the geometry, and no inverse estimate
uniform in cylinder length and degeneration was established in Step 72.  The
normal balance supplies a lower length scale in certain endpoint regimes; it
does not supply an upper length bound.  Consequently the earlier
`O(delta log(1/delta))` assertion and the resulting closure of the approximate
`T^2` route are withdrawn.

The equations above also cover only the diagonal orthogonally-transitive
subclass.  They are not equations for every metric with a `T^2` action.

A separate scope correction concerns products.  If a four-dimensional metric
`g_j` is close to positive Einstein scale and `k>=2`, then

\[
 g_j\oplus g_{S^k},\qquad \operatorname{Ric}_{g_{S^k}}=\sigma g_{S^k},
\]

has the same blockwise input defect.  This produces useful examples in higher
dimensions.  It does not reduce an arbitrary higher-dimensional manifold to a
four-dimensional one, and it does not transfer absence of arbitrary Einstein
metrics: an Einstein metric on the product manifold need not split.  Even a
product made from a hypothetical Einstein output on the four-manifold requires
compatible constants, while the target problem does not prescribe the sign of
the output.  Thus the product construction is a family extension, not
`P_4^+ => P_n^+`.

Group message #512 circulated both corrections; A02 acknowledged and repaired
its record in messages #513 and #515.

## 2. Exact expanding-tail calculation

Let

\[
 B=dr^2+e^{2r}dz^2,
\]

and on an interval in `r` set

\[
 g=dr^2+e^{2r}\left[
 dz^2+N^{-2}e^v dx^2+N^{-2}e^{-v}dy^2\right].
\]

Here `v=v(r,z)` and `N` changes only the lattice scale.  The multiply-warped
Ricci equations give, in the orthonormal base and fiber frames,

\[
 E|_B=-\frac12\,dv\otimes dv,
\]

\[
 E_x=-\frac12\left(v_{rr}+3v_r+e^{-2r}v_{zz}\right),
 \qquad
 E_y=+\frac12\left(v_{rr}+3v_r+e^{-2r}v_{zz}\right),
\]

and the base--fiber components vanish.  The base `rz` component is generally
`-v_r v_z/2`; only base--fiber mixed terms vanish.  Hence the exact operator
norm is

\[
 \|E\|_{\mathrm{op}}
 =\frac12\max\left\{
  v_r^2+e^{-2r}v_z^2,
  \left|v_{rr}+3v_r+e^{-2r}v_{zz}\right|
 \right\}.
\]

Take a fixed smooth periodic `v_0` and, for the displayed finite-regularity test, a cutoff whose first two derivatives vanish at its endpoints. For a smooth geometric attachment, replace it by a `C^infty` cutoff constant on endpoint neighborhoods; the estimate is unchanged:

\[
 v(r,z)=\chi\left(\frac{r-r_0}{K}\right)v_0(z),
 \qquad \chi(0)=1,\quad \chi(1)=0.
\]

Then

\[
 \boxed{
 \|\operatorname{Ric}+3g\|_{\mathrm{op},\infty}
 \le C_{v_0,\chi}
 \left(K^{-1}+K^{-2}+e^{-2r_0}\right),
 }
\]

uniformly in `N`.  Thus order-one oscillation in the orbit ratio can be erased
with arbitrarily small full Ricci defect by a sufficiently long transition
placed sufficiently far into an expanding region.

The symbolic substitution into the complete Step-72 Ricci formulas gives zero
residual for all five displayed components.  The numerical script

`workspace/scripts/step73_expanding_tail_verify.py`

writes

`workspace/data/step73_expanding_tail.json`.

For `v_0=sin z`, `r_0=6`, and the quintic smootherstep, the grid-evaluated maxima (not interval-certified continuous suprema) for `K=4,8,16,32,64` are respectively

\[
0.7406712,
0.3563953,
0.1763899,
0.08796675,
0.04395483.
\]

The products `K sup|E|` tend numerically to `2.8125`; analytically, `max|chi'|=15/8`, so the leading fiber eigenvalue gives `(3/2) max|chi'|=45/16=2.8125`. The center oscillation is `2` and the outgoing oscillation is zero. The local calculation is independent of `N`, although fiber lengths, volume, and injectivity radius are not.

The shape operator is

\[
 S=\operatorname{diag}
 \left(1,1+\frac12v_r,1-\frac12v_r\right),
 \qquad H=3,
\]

so

\[
 |S-I|^2=\frac12v_r^2,
 \qquad E_{rr}=-\frac12v_r^2.
\]

Therefore the tail satisfies the normal balance pointwise: its negative normal
defect exactly pays its own shear.  It does not pay the earlier deficit incurred
between a reflection center and an entry face with `H` near `3`.

## 3. A general finite tail-completion lemma

Let `q_s`, `0<=s<=1`, be a smooth path of metrics on a fixed closed
three-manifold and put

\[
 Q=q_s^{-1}\dot q_s,
 \qquad s=\frac{r-r_0}{K},
 \qquad g=dr^2+e^{2a(r)}q_s.
\]

Writing all tangential tensors as endomorphisms with respect to `q_s`, Gaussian
foliation formulas give

\[
 S=a'I+\frac1{2K}Q,
 \qquad
 H=3a'+\frac1{2K}\operatorname{tr}Q,
\]

\[
 \begin{split}
 E_{rr}={}&3-3a''-3(a')^2
 -\frac{a'}K\operatorname{tr}Q
 -\frac1{2K^2}\partial_s\operatorname{tr}Q
 -\frac1{4K^2}\operatorname{tr}(Q^2),
 \end{split}
\]

\[
 \begin{split}
 E_T={}&e^{-2a}\operatorname{Ric}(q_s)^\sharp
 +\left(3-a''-3(a')^2
 -\frac{a'}{2K}\operatorname{tr}Q\right)I\\
 &-\frac{3a'}{2K}Q
 -\frac1{2K^2}\dot Q
 -\frac1{4K^2}(\operatorname{tr}Q)Q,
 \end{split}
\]

and, up to the harmless sign convention for the Gaussian normal,

\[
 E_{r\cdot}=\frac1{2K}
 \left(\operatorname{div}_{q_s}Q-d\operatorname{tr}Q\right).
\]

The norm of the last covector in `g` contains an additional factor `e^{-a}`.
These formulas prove the following useful statement.

**Adiabatic tail completion.** Suppose `q_s` is uniformly positive definite and `q_s`, its inverse, its first two `s`-derivatives, its spatial Ricci tensor, and the spatial derivative of `q_s^{-1} dot q_s` needed for the Codazzi term are uniformly bounded; suppose also that `q_s` is constant near both endpoints and `q_1` is flat.  Choose a cutoff `eta` constant at the endpoints and set

\[
 a'(r)=1-\varepsilon\eta(s),
 \qquad \eta(0)=1,\quad\eta(1)=0.
\]

Then the left endpoint has

\[
 h_0=e^{2a_0}q_0,
 \qquad S_0=(1-\varepsilon)I,
\]

while the right endpoint is an exact flat hyperbolic cusp germ.  Moreover

\[
 \boxed{
 \|\operatorname{Ric}_g+3g\|_{\mathrm{op},\infty}
 \le C\left(
 \varepsilon+K^{-1}+K^{-2}+e^{-2a_0}
 \right),
 }
\]

where `C` depends only on the stated path bounds and `a>=a_0`. If the path preserves its pointwise volume form, `tr Q=0`, the path contribution in the normal component improves from order `K^{-1}` to order `K^{-2}`; the full defect generally remains order `K^{-1}` because of `-3a'Q/(2K)`. Endpoint-stationary paths permit smooth attachment only after all metric jets agree with the adjacent piece.

This lemma is elementary but changes the graph-neck problem.  Once a core has
reached a large, almost umbilic expanding slice, neither nonconstant orbit
anisotropy nor flattening of the intrinsic torus metric is an order-one
obstruction.  Both can be moved through a long region at small Ricci cost.

## 4. The core-entry interface

A sufficient local input for the graph construction is now precise.  Seek a
sequence of metrics `G_j` on `[0,R_j] x T^3` such that

\[
 \|\operatorname{Ric}_{G_j}+3G_j\|_{\mathrm{op},\infty}\to0,
 \qquad S_j(0)=0,
\]

and at `r=R_j`,

\[
 h_j=e^{2a_j}q_j,
 \qquad
 S_j=(1-\varepsilon_j)I+P_j,
\]

with

\[
 e^{-2a_j}\|\operatorname{Ric}(q_j)\|_{\mathrm{op}}\to0,
 \qquad
 \varepsilon_j+\|P_j\|\to0.
\]

These zeroth- and first-order limits are necessary but are not by themselves a
smooth attachment theorem. The `q_j` must admit paths to the required flat cusp
metrics with path bounds controlled relative to `K_j`, and the initial path jet
must realize the core shear: in the above parametrization
`Q_j(0)=2K_jP_j`. One must simultaneously control `Q_j/K_j`,
`(dot Q_j+Q_j^2)/K_j^2`, the scaled Codazzi term, and all higher endpoint jets.
Alternatively, one may strengthen the entry to an exactly umbilic endpoint and
arrange exact jet matching. Under those conditions the tail lemma extends each
core to an exact flat-cusp germ while preserving vanishing maximum Ricci defect.
The lattice parameter can still be chosen independently in the local curvature
estimates, although global collapse quantities depend on it.

The normal equation

\[
 (H-3)'+2(H-3)+|S-I|^2=-E_{rr}
\]

continues to constrain how the core reaches this entry data. The explicit tail
shows that anisotropy removal after entry is feasible; it does not construct the
entry itself.

For an exact core in a CMC, pointwise-volume-preserving foliation gauge—an
additional structural assumption, not an automatic decomposition of every
Gaussian foliation—it is useful to split

\[
 h_r=e^{2a(r)}q_r,
 \qquad
 S=a'I+P,
 \qquad \operatorname{tr}_{q_r}P=0,
 \qquad q_r'=2q_rP.
\]

The exact Einstein equations become

\[
 a''=1-(a')^2-\frac13|P|^2,
\]

\[
 P'+3a'P=e^{-2a}\operatorname{Ric}(q_r)^\circ,
\]

with the Hamilton and momentum constraints

\[
 e^{-2a}R(q_r)+6(1-(a')^2)+|P|^2=0,
 \qquad \operatorname{div}_{q_r}P=0.
\]

At a reflection center these reduce to

\[
 a'(0)=0,
 \quad P(0)=0,
 \quad R(q_0)=-6e^{2a(0)}.
\]

The traceless equation has damping `3a'P` and a curvature source multiplied by `e^{-2a}` once expansion begins. This is genuinely small only if `e^{-2a}|Ric(q_r)|` is controlled; expansion alone does not ensure it. Under that control, a complete negative-Yamabe Einstein half-core, if one exists, would naturally supply the entry interface.
It does not prove such a global continuation: as a Cauchy problem the equations
are elliptic in the tangential variables and contain growing spatial branches.

An exact reflection-symmetric Poincare--Einstein cylinder with negative-Yamabe
`T^3` conformal infinity would be sufficient.  Truncating it far out would give
`a_j -> infinity`, `S_j -> I`; the adiabatic tail would then flatten its
nonconstant boundary anisotropy with vanishing defect.  The Witten--Yau /
Cai--Galloway result used in Step 71 excludes disconnected nonnegative-Yamabe
infinity, including the flat class, but does not exclude negative-Yamabe
infinity.  The source search in this step found the Fredholm boundary-map and
cusp-degeneration framework, but no theorem supplying or excluding the needed
`R x T^3` reflection core.  Fuchsian warped products provide exact two-ended
models when the three-dimensional cross-section itself is negative Einstein;
that seed is unavailable on `T^3`.

## 5. Constraint-preserving computation

The Step-72 system

\[
 (E_{tt}+E_{zz},E_x,E_y)=0
\]

has elliptic principal determinant `2(tau^2+xi^2)^3`, but these three equations
do not by themselves establish

\[
 E_{tt}-E_{zz}=0,
 \qquad E_{tz}=0.
\]

Any boundary-value computation must either solve a full Einstein--DeTurck
system and remove the DeTurck field, or prove propagation of the remaining
Hamilton/momentum components from compatible boundary data.  A spatial block
that converges numerically while leaving these two components large repeats the
failure of the Step-70 BVP.

The next computation should therefore target the core-entry interface, not the
already solved tail.  It should allow the center metric to vary within the
scalar-`-6` class, impose reflection parity, prescribe only compatible far data,
and record all five Ricci components together with the constraints.  The
adiabatic tail provides explicit outgoing data and a quantitative success
interface; it is not a replacement for this full core problem.

## 6. Relation to the full Yau 26 goal

Even a successful graph connector would presently settle only the normalized
negative branch in dimension four, by combining it with a smooth topology known
to exclude every Einstein metric.  The positive branch in the same dimension
would remain necessary under the active formulation, and the product examples
do not settle higher-dimensional quantifiers.  The tail lemma is valuable
because it restores a viable and sharply localized negative construction route,
not because it completes the original proposition.
