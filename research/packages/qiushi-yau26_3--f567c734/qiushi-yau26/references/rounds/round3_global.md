# A sharp physical-width obstruction for two exact expanding ends

19 September 2026. This note continues `round2_global.md`. Its new result is
an intrinsic distance and signed Ricci-transport obstruction, valid without
torus symmetry. A complete smooth metric family proves sharpness for the
one-sided Ricci hypothesis. The full small-defect twisted-connector question
is not settled.

## 1. The two-boundary index form

Let a complete connected Riemannian manifold of dimension `n+1` have two
ends which, outside a compact set, are exactly

\[
 dt^2+e^{2t}h_\pm,\qquad t\ge0,
\]

where `h_+` and `h_-` are flat metrics on compact connected manifolds.
The outward direction is increasing `t` on each end. Let `N` be the compact
bridge between the sections `t=0`, and let `L` be the distance between its
two boundary components. Equivalently, `L` is their distance in the complete
manifold: an excursion into either attached end cannot shorten a path,
because projection onto its initial section is length nonincreasing.
No lower bound for the size of either boundary is imposed.

Each boundary has outward shape operator `I` and mean curvature `n`.
A shortest joining geodesic `gamma:[0,L] -> N` meets both orthogonally and
has no interior contact with either boundary. Let `e_1,...,e_n` be a parallel
orthonormal normal frame along it. Free-endpoint second variation, with
endpoint curves lying in the boundary sections, gives

\[
 0\le \sum_{i=1}^n I(fe_i,fe_i)
 =\int_0^L\{n(f')^2-\operatorname{Ric}(\dot\gamma,\dot\gamma)f^2\}\,ds
      -n\{f(0)^2+f(L)^2\}
\tag{1}
\]

for every smooth real `f`. Both boundary terms have the displayed negative
sign. Indeed the geodesic points inward at its initial endpoint and outward
at its terminal endpoint. Only the traces of the two shape operators are
needed for (1), so the theorem below also applies to boundaries of outward
mean curvature at least `n`.

### Theorem 1: a sharp width bound from the negative Ricci defect

Suppose

\[
 \operatorname{Ric}\ge-(n+\epsilon)g,\qquad \epsilon>0,
 \qquad k=\sqrt{1+\epsilon/n}.
\]

Then

\[
 \boxed{\quad
 k\tanh(kL/2)\ge1,\qquad
 L\ge L_{n}(\epsilon):=
 \frac{2}{k}\operatorname{artanh}(1/k)
 =\frac1k\log\frac{k+1}{k-1}.
 \quad}
\tag{2}
\]

For a smooth attachment to exact ends the inequalities are strict. As
`epsilon -> 0`,

\[
 L_n(\epsilon)=\log(4n/\epsilon)
                  +O(\epsilon|\log\epsilon|).
\tag{3}
\]

If `Ric >= -ng`, no finite bridge is possible.

**Proof.** Apply (1) to

\[
 f(s)=\frac{\cosh(k(s-L/2))}{\cosh(kL/2)}.
\]

It has endpoint values one and satisfies `f''=k^2 f`. Thus

\[
 0\le\sum I(fe_i,fe_i)
 \le n\int_0^L((f')^2+k^2f^2)\,ds-2n
 =2n\{k\tanh(kL/2)-1\}.
\]

Inverting this inequality gives (2). At the exact-end sections
`Ric(dot gamma,dot gamma)=-n`; continuity makes the upper estimate strict
on a small subinterval when `epsilon>0`. With `epsilon=0`, the same
calculation with `k=1` is already contradictory for every finite `L`.
Finally `k-1=epsilon/(2n)+O(epsilon^2)` proves (3). All distances and
curvatures are physical quantities in the given metric. No choice of
coordinates or torus lattice changes them. QED.

For the four-dimensional connector, use `n=3`. The theorem applies whenever
`||Ric+3g||_op <= epsilon`, but actually uses only its negative directional
part. Together with round two, a hypothetical full free-T2 connector family
with vanishing defect must have all three properties:

\[
 \liminf Q_*\ge9\sqrt2-12,\qquad
 H_*\ge\frac{\sqrt{q_*(\epsilon)}}{2\epsilon},\qquad
 L\ge\log(12/\epsilon)+o(1).
\tag{4}
\]

The third statement is new and cannot be read off from `H_*`: the latter
can grow through orbit-area and shape weights even when an unweighted
distance stays bounded. Here `L` is the distance between specified exact
end sections. Moving those sections outward artificially increases `L`;
the useful statement takes the innermost sections at which the prescribed
exact end models start. Bounded bridge width therefore gives a full twisted
Ricci-defect gap, without any bound on the charge transport weights.

## 2. A signed source obstruction along the actual bridge

Write

\[
 E(s)=\operatorname{Ric}(\dot\gamma,\dot\gamma)+n.
\]

Equation (1) is the exact one-dimensional quadratic-form requirement

\[
 \int_0^L\{n(f')^2+(n-E)f^2\}\,ds
 \ge n\{f(0)^2+f(L)^2\}.
\tag{5}
\]

This preserves the sign and location of the negative Ricci source. For
`f(s)=cosh(s-L/2)/cosh(L/2)` it implies

\[
 \boxed{\quad
 \int_0^L[-E(s)]\cosh^2(s-L/2)\,ds
       \ge n(1+e^{-L}).
 \quad}
\tag{6}
\]

In particular a signed cancellation cannot be replaced by an assertion
that only `||E||` is small. Replacing `-E` by its positive part weakens but
preserves the inequality. A directly explicit consequence is

\[
 \epsilon\ge\frac{2n(1+e^{-L})}{L+\sinh L}.
\tag{7}
\]

The optimized estimate (2) is stronger than (7).

There is also a two-moment version. Center the geodesic parameter at zero,
so its interval is `[-L/2,L/2]`, and set

\[
 N_+=\int[-E(s)]e^{2s}ds,\quad
 N_-=\int[-E(s)]e^{-2s}ds,\quad
 N_0=\int[-E(s)]ds.
\]

Applying (5) to every `f=Ae^s+Be^{-s}` says exactly that

\[
 \boxed{
 \begin{pmatrix}
  N_+-2ne^{-L}&N_0-2n\\
  N_0-2n&N_--2ne^{-L}
 \end{pmatrix}\succeq0.}
\tag{8}
\]

Thus both weighted moments must be positive, and their determinant must
be nonnegative. These are necessary conditions on the same geometric
geodesic and the same actual Ricci residual; they are not freely prescribed
Maxwell or horizontal source terms. Formula (8), like (6), requires no
derivatives of the Ricci residual. Taking `A=B` recovers (6).

## 3. Exact smooth metrics show why the Ricci lower bound cannot close the gap

The next construction is a full metric, with all Ricci components computed.
It shows that Theorem 1 is sharp for its one-sided hypothesis. It is not a
small full-Ricci-defect connector.

Fix `n>=2`, `epsilon>0`, `k=sqrt(1+epsilon/n)`, and

\[
 T=\frac1k\operatorname{artanh}(1/k).
\]

Define the continuous Lipschitz odd function

\[
 a_0(t)=
 \begin{cases}
  -1,&t\le-T,\\
  k\tanh(kt),&|t|<T,\\
  1,&t\ge T.
 \end{cases}
\]

Choose any nonnegative even smooth mollifier `phi_eta` of integral one and
support in `[-eta,eta]`, and put `a=a_0*phi_eta`. This is a precise smooth
construction; the standard normalized bump
`exp[-1/(1-(t/eta)^2)]` on `|t|<eta` is one choice. Then

\[
 a(-t)=-a(t),\quad a'\ge0,\quad |a|\le1,\quad
 a(t)=\operatorname{sgn}t\ (|t|\ge T+\eta),\qquad
 a'+a^2\le k^2.
\tag{9}
\]

For the final inequality, `a_0'+a_0^2<=k^2` holds almost everywhere and in
distributions; the clipped continuous slope has no delta in its first
derivative. Convolution and Jensen's inequality give
`a'+a^2 <= (a_0'+a_0^2)*phi_eta <= k^2`.

For an arbitrary flat torus metric `h` and arbitrary constant `c>0`, define

\[
 F(t)=c\exp\left(\int_0^t a(s)ds\right),\qquad
 g=dt^2+F(t)^2h\quad\hbox{on }\mathbb R\times T^n.
\tag{10}
\]

This is smooth and complete. In particular `F>=c`, and the radial direction
has infinite length in both directions. Both ends are exactly expanding
hyperbolic ends for `|t|>=T+eta`. All eigenvalues of Ricci are

\[
 r_t=-n(a'+a^2),\qquad
 r_{\rm torus}=-a'-na^2\quad\hbox{(multiplicity }n\hbox{)},
\tag{11}
\]

and there are no mixed components. By (9),

\[
 r_t\ge-nk^2=-(n+\epsilon),\qquad
 r_{\rm torus}\ge-k^2-(n-1)\ge-nk^2.
\]

The two exact-end sections have distance

\[
 L=2(T+\eta)=L_n(\epsilon)+2\eta.
\tag{12}
\]

Hence (2) is sharp in the limit `eta -> 0`, even among smooth complete
metrics with flat torus ends and a free `T^n` action. Arbitrary `c` and `h`
show that this sharpness does not assume a lower covolume.

However, `a(0)=0` and `a'(0)<=k^2` imply

\[
 \|\operatorname{Ric}+ng\|_{\infty,\rm op}
 \ge n-a'(0)\ge n-1-\epsilon/n.
\tag{13}
\]

For `n=3` this is at least `2-epsilon/3`, not a quantity tending to zero.
The necessary order-one tangential Ricci error is the precise missing
condition in this lower-Ricci escape. This family satisfies full geometric
compatibility, smoothness, completeness, lattice consistency and both exact
ends; it fails the upper half of the desired Ricci interval.

## 4. Relation to the connected-conformal-boundary theorem

The primary source is Cai--Galloway, *Boundaries of zero scalar curvature in
the AdS/CFT correspondence*, [Theorem 1 and Theorem 3](https://www.math.miami.edu/~galloway/papers/zero2.pdf).
Their result requires `Ric>=-ng` and sufficiently fast approach to that same
normalization at conformal infinity. Exact ends satisfy the falloff. Their
two-ended splitting conclusion gives an expanding end and a cusp, rather
than two expanding ends. The zero-error conclusion of Theorem 1 above is a
direct finite-distance proof in the exact-end setting.

For `Ric>=-(n+epsilon)g`, a constant rescaling makes the lower bound `-ng`
but changes the limiting Einstein constant of the exact ends to `-n/k^2`.
It therefore violates the required falloff to `-ng`. The actual family in
Section 3 proves that this is a substantive issue: no argument using only
that lower bound and flat exact ends can yield an epsilon-only gap.

## 5. Scope and verification

`round3_global_check.py` independently computes every coordinate Ricci
component of the four-dimensional warped metric, verifies the index-form
boundary flux, the weighted source identity, the two-moment matrix, the
width inversion and its asymptotic normalization. It also prints numerical
values of the exact distance threshold. The smoothing/Jensen proof and
free-boundary variational argument are analytic proofs, not claims of
computer formalization.

These results add an actual physical-width obstruction and a sharp smooth
geometric limit to the prior twist/charge bounds. They do not give an
unconditional positive two-sided Ricci-defect gap in the full twisted-T2
class. Any further proof must use information absent from a Ricci lower
bound, for example the tangential upper bound coupled to the orbit/charge
equations. No fixed-topology closed gluing or Einstein existence claim is
made.
