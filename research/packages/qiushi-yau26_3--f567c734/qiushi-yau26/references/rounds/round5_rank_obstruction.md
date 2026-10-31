# Abelian rank, sectional sign, and a Ricci gap for expanding connectors

20 September 2026. A geometric-group-theory argument removes the torus-action
and radial assumptions from one connector obstruction. Its external input
is the classical flat torus theorem; the Ricci estimate below is its direct
application, not a claim of a new flat torus theorem.

## 1. A rank estimate in any dimension

Let \((M^d,g)\) be complete with nonpositive sectional curvature. Suppose
its deck group contains \(\mathbb Z^k\) acting by semisimple isometries
on the universal cover. A deck action is proper. The
[flat torus theorem, Bridson--Haefliger II.7.1](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bridsonhaefligerx.pdf)
therefore supplies a totally geodesic flat \(\mathbb R^k\). No cocompactness
of \(M\) is required once semisimplicity is established.

Fix \(\lambda>0\), put \(E=\operatorname{Ric}+\lambda g\), and assume
\(\|E\|_{\infty,\mathrm{op}}\le\epsilon\). At a point of the flat, choose
an orthonormal basis tangent to it and a basis of its normal complement.
All tangent sectional curvatures vanish. Consequently

\[
 \operatorname{tr}_{N}\operatorname{Ric}
       -\operatorname{tr}_{T}\operatorname{Ric}
   =2\sum_{a<b,\ a,b\in N}K(e_a,e_b)\le0.
\]

Thus

\[
 \operatorname{tr}_TE-\operatorname{tr}_NE
       \ge(2k-d)\lambda,
 \qquad
 \boxed{\epsilon\ge\frac{(2k-d)_+}{d}\lambda.}
 \tag{1}
\]

This statement is useful when \(k>d/2\). At the equality rank \(k=d/2\)
it gives no positive gap, consistently with products of closed hyperbolic
surfaces. Negative Einstein metrics with nonpositive sectional curvature
can therefore have semisimple abelian rank at most \(d/2\).

## 2. Why the connector deck transformations are semisimple

Now let \(M=\mathbb R\times T^{d-1}\) have an arbitrary smooth complete
metric whose complement of a compact set consists of two exact outward
ends

\[
 dt^2+e^{2t}h_\pm,\qquad t\ge T_0,
\]

where \(h_\pm\) are fixed flat metrics on the actual tori. No isometric
torus action is assumed inside the compact region.

Every nontrivial free homotopy class has a shortest closed geodesic.
Indeed, bounded-length representatives cannot escape to an end. A loop
that reaches the compact region has maximum depth bounded by half its
length plus \(T_0\). A loop contained in an end has a nontrivial torus
projection, so its length is at least \(e^{t_{\min}}\operatorname{sys}(h_\pm)\).
Its radial oscillation is again bounded by half its length. Hence a
minimizing sequence lies in a fixed compact subset. The positive local
injectivity radius there, Arzela--Ascoli, and the usual length minimization
give a nonconstant closed geodesic in the required class.

Under \(K\le0\), each lifted geodesic is an axis of its deck
transformation, and realizes the translation length. Every element of
the full deck group \(\mathbb Z^{d-1}\) is therefore semisimple. Apply
(1) with \(k=d-1\):

\[
 \boxed{K\le0\quad\Longrightarrow\quad
   \|\operatorname{Ric}+\lambda g\|_{\infty,\mathrm{op}}
       \ge\frac{d-2}{d}\lambda.}
 \tag{2}
\]

In dimension four, for the exact-end normalization \(\lambda=3\), this
is the lower bound \(3/2\). Thus a proposed two-ended connector with
Ricci defect tending to zero must have **positive sectional curvature
somewhere**. Adding an arbitrary two-variable twist does not avoid this
conclusion if all sectional curvatures are kept nonpositive. The sharpness
as an infimum holds in every dimension \(d\ge3\), as follows.

### A sharpness family with actual exact ends

Put \(n=d-1\ge2\), take \(\lambda=n\), and define

\[
 k^2=\frac{2n}{n+1},\quad
 a_0(t)=\operatorname{clip}(k\tanh(kt),-1,1),\quad
 a_\eta=\varphi_\eta*a_0,\quad
 F_\eta(t)=c\exp\left(\int_0^t a_\eta(s)\,ds\right),
\]

where \(\varphi_\eta\) is an even nonnegative smooth unit-mass mollifier
supported in \([-\eta,\eta]\). The clipped profile reaches its constants
at a finite time because \(k>1\). Thus
\(g_\eta=dt^2+F_\eta^2h_0\) is smooth, complete, and has two exact
outward hyperbolic ends on the fixed torus lattice \(h_0\).
Their flat end coefficients may vary with \(\eta\). If identical end
coefficients are prescribed across the family, the evenness of
\(F_\eta\) gives the same additive primitive constant at both ends;
choose \(c=c_\eta\) to remove it. This changes no curvature estimate.

The radial and tangential sectional curvatures are
\(-a_\eta'-a_\eta^2\) and \(-a_\eta^2\). For small \(\eta\) they are
nonpositive. Indeed, since \(a_0\) is \(k^2\)-Lipschitz, its variance
under any translated mollifier is at most \(k^4\eta^2\). Convolution
and the variance identity give

\[
 1-k^4\eta^2\le a_\eta'+a_\eta^2\le k^2,
 \qquad
 k^2-nk^4\eta^2\le a_\eta'+n a_\eta^2\le n-1+k^2.
\]

These bounds apply across the smoothed interfaces, not just to the
unclipped core. The normal and tangential Ricci eigenvalues are
\(-n(a_\eta'+a_\eta^2)\) and
\(-(a_\eta'+n a_\eta^2)\). Hence

\[
 \|\operatorname{Ric}(g_\eta)+n g_\eta\|_{\infty,\mathrm{op}}
 \le\frac{n(n-1)}{n+1}+nk^4\eta^2.
\]

Combining this with (2) proves that the infimum within the nonpositively
sectionally curved exact-end connector class is exactly
\(n(n-1)/(n+1)\). Constant rescaling gives the corresponding statement
for \(\lambda>0\), with end sectional curvature \(-\lambda/n\).
For \(n=3\) this is the same sharp family recorded in `round5_global.md`.

## 3. A Weyl concentration that any small-defect connector must contain

Return to dimension four and \(E=\operatorname{Ric}+3g\). At a plane
with sectional curvature \(K\ge0\), the
curvature decomposition is

\[
 K=W_{1212}-1+
       \frac{E_{11}+E_{22}}3-\frac{E_{33}+E_{44}}6.
\]

The error expression has absolute value at most \(\epsilon\). Hence
\(W_{1212}\ge1-\epsilon\). If \(|W|\) denotes the Hilbert--Schmidt norm
of the full Weyl curvature operator on \(\Lambda^2\), then
\(|W_{1212}|\le |W|/\sqrt3\): each self-dual block is a trace-free
symmetric three-by-three matrix and each half of a unit simple two-form
has squared norm one-half. Therefore, when \(\epsilon<1\),

\[
 \boxed{\sup_M|W|\ge\sqrt3(1-\epsilon).}
 \tag{3}
\]

Together with the full twisted Weyl--charge integral identity in
`round5_global.md`, this isolates a specific escape mechanism: a candidate
must create positive sectional curvature and order-one Weyl curvature,
while arranging their integral cost within a potentially collapsed
region. A pointwise peak supplies no lower bound on the volume of that
region. Neither (2) nor (3) is an unrestricted Ricci gap or a contradiction
to the general two-ended construction problem.
