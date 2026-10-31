# Fixed closed near-Einstein metrics from sheared product blocks

21 September 2026.

## 1. The closed construction

Fix finitely many compact connected oriented surfaces \(B_v\), each with
nonempty boundary and \(\chi(B_v)<0\), and closed oriented surfaces \(F_v\)
of a common genus \(p\ge2\). Pair all boundary components in a connected
graph. The block associated to a vertex is \(B_v\times F_v\).
For each oriented edge, fix a gluing diffeomorphism

\[
\Psi_e:S^1\times F_v\longrightarrow S^1\times F_w,\qquad
(\phi,x)\longmapsto(-\phi+u_e(x),f_e(x)),
\tag{1}
\]

where the circle coordinate has period \(2\pi\),
\(u_e:F_v\to\mathbb R/(2\pi\mathbb Z)\) is smooth and
\(f_e:F_v\to F_w\) is any orientation-preserving diffeomorphism.
The minus sign makes the boundary identification orientation reversing.
Let \(M\) be the resulting fixed closed oriented smooth four-manifold.
There is no condition that the mapping classes of the \(f_e\) have finite
order, commute, or extend over adjacent product blocks.

**Theorem.** The fixed manifold \(M\) carries smooth metrics \(G_\ell\),
\(\ell\downarrow0\), with

\[
\begin{aligned}
\|\operatorname{Ric}_{G_\ell}+3G_\ell\|_{\infty,\mathrm{op}}
&\le C\bigl(|\log\ell|^{-1}+\ell\bigr)\longrightarrow0,\\
\operatorname{Vol}(M,G_\ell)&=\frac{4\pi^2}{9}\chi(M),\\
\|\nabla^j\operatorname{Rm}_{G_\ell}\|_\infty&\le C_j
 \qquad(j\ge0).
\end{aligned}
\tag{2}
\]

The norm in the first line is the endomorphism norm formed using
\(G_\ell\). The same bound, with constants depending on \(j\), holds
for every fixed covariant derivative order of the defect. All gluing
maps, integral shear classes and smooth identifications are fixed.
Constants may depend on these finite data.

Rescaling \(\widehat G_\ell=3G_\ell\) gives the normalization
\(\|\widehat G_\ell^{-1}\operatorname{Ric}_{\widehat G_\ell}+I\|_\infty
\to0\), with \(\operatorname{Vol}(\widehat G_\ell)=4\pi^2\chi(M)\).

The construction uses two separated operations: a slow hyperbolic-metric
path absorbs the possibly infinite-order \(f_e\), and a shrinking circle
suppresses the integral shear. Their supports are disjoint, so no
uncontrolled interaction between them is hidden in (2).

## 2. Exact hyperbolic boundary collars

Fix curvature-\(-3\) metrics \(h_v\) on \(F_v\). Give every \(B_v\) a
curvature-\(-3\) metric \(b_{v,\ell}\) with geodesic boundary circles
of length \(\ell\). Choose these by a fixed pants decomposition with
fixed internal length/twist parameters and all boundary lengths \(\ell\).
The half-collars inside the blocks are disjoint and have the form

\[
dt^2+a_\ell(t)^2d\phi^2,\qquad
a_\ell(t)=\frac{\ell}{2\pi}\cosh(\sqrt3\,t),
\qquad
0\le t<w_\ell,
\tag{3}
\]

where one may use

\[
w_\ell=\frac1{\sqrt3}
\operatorname{arsinh}\!\left(\frac1{\sinh(\sqrt3\,\ell/2)}\right).
\tag{4}
\]

This is the usual collar lemma after scaling. For a precise version,
see [Rupflin--Topping, Appendix A, Lemma A.1](https://arxiv.org/pdf/1605.06691).
The boundary version follows by doubling the hyperbolic surface across
its geodesic boundary.

Put \(L_\ell=w_\ell/2\). In a signed edge collar
\([-L_\ell,L_\ell]\times S^1\times F_v\), use coordinates on the left
and pull right coordinates back by (1). The pullback of the unmodified
right product is

\[
dt^2+a_\ell(t)^2(d\phi+\beta_e)^2+f_e^*h_w,
\qquad
\beta_e=-u_e^*(d\phi).
\tag{5}
\]

The form \(\beta_e\) is a global closed one-form on \(F_v\), with
periods in \(2\pi\mathbb Z\). It need not be exact. The circle-valued
map in (1), not a real-valued primitive of \(\beta_e\), supplies the
actual global endpoint identification.

## 3. Absorbing arbitrary mapping classes

Choose a fixed smooth path \(h_{e,z}\), \(0\le z\le1\), of
curvature-\(-3\) metrics on the marked \(F_v\), with

\[
h_{e,0}=h_v,\qquad h_{e,1}=f_e^*h_w.
\tag{6}
\]

Such paths exist by connectedness of the space of marked hyperbolic
metrics. They can, for example, be constructed by smooth uniformization
of a path of positive definite metrics. Each fixed path and all its
finite-order derivatives have uniform bounds on the compact parameter
interval. No global isotopy from the identity to \(f_e\) is asserted.

Choose a fixed smooth step function \(\zeta\), constant zero and one
near the endpoints of \([0,1]\). On \([-L_\ell,-1]\), set

\[
z(t)=\zeta\!\left(\frac{t+L_\ell}{L_\ell-1}\right),\qquad
g=dt^2+a_\ell(t)^2d\phi^2+h_{e,z(t)}.
\tag{7}
\]

Use \(h_v\) before the transition and \(f_e^*h_w\) afterwards.
There is no connection shear in this region.
For \(S=\tfrac12 h^{-1}\dot h\), \(H=\operatorname{tr}S\), and
\(k=a_\ell'/a_\ell\), the full Ricci defect has blocks

\[
\begin{aligned}
E_{tt}&=-\dot H-\operatorname{tr}(S^2),\\
E_{UU}&=-kH,\qquad U=a_\ell^{-1}\partial_\phi,\\
E_{FF}^{\sharp}&=-D_tS-(k+H)S,\\
E_{tF}&=\operatorname{div}_h S-dH,\\
E_{tU}&=E_{UF}=0,
\end{aligned}
\tag{8}
\]

where \(E=\operatorname{Ric}+3g\) and \(D_tS\) is the covariant
time derivative. These are the complete Gauss--Codazzi blocks,
including the trace terms. The path need not have a common pointwise
area form; therefore no endpoint-changing Moser isotopy is required.

We have \(S,H,\operatorname{div}S,dH=O(L_\ell^{-1})\),
\(\dot H,D_tS=O(L_\ell^{-2})\), and
\(|k|\le\sqrt3\). Hence (8) gives
\(\|E\|_{\mathrm{op}}\le C/L_\ell\).
All metric-path constants refer to a fixed compact family, not to
a family approaching the boundary of fibre Teichmüller space.
The collapsing circle introduces no inverse-\(a_\ell\) loss: coefficients
are independent of \(\phi\), and its connection uses \(k\), not
\(a_\ell^{-1}\) alone.

## 4. Absorbing integral shear at the collapsed throat

Choose a fixed smooth \(z_s(t)\), zero for \(t\le0\), one for \(t\ge1\),
constant on neighborhoods of the endpoints. On this region keep
\(h=f_e^*h_w\) fixed and set

\[
g=dt^2+a_\ell(t)^2\bigl(d\phi+z_s(t)\beta_e\bigr)^2+h.
\tag{9}
\]

Now the circle quotient metric is \(dt^2+h\), its connection is
\(\alpha=z_s\beta_e\), and its curvature is
\(F=z_s'\,dt\wedge\beta_e\).
Let \(b=\beta_e\), \(D=\operatorname{div}_h b\) (divergence of the
dual vector field), \(a=a_\ell\), and \(k=a'/a\).
In the orthonormal splitting \((\partial_t,U,TF)\), the nonzero defect
blocks are

\[
\begin{aligned}
E_{tt}&=-\tfrac12a^2(z_s')^2|b|^2,&
E_{UU}&=\tfrac12a^2(z_s')^2|b|^2,\\
E_{XY}&=-\tfrac12a^2(z_s')^2b(X)b(Y),&
E_{tU}&=\tfrac12a z_s'D,\\
E_{XU}&=-\tfrac12a(z_s''+3kz_s')b(X),&
E_{tX}&=0.
\end{aligned}
\tag{10}
\]

The mixed entries follow from
\(\operatorname{Ric}(X,K)=(2a)^{-1}\nabla^j(a^3F_{Xj})\),
with \(K=\partial_\phi\), then division by \(a\).
The factor \(3k\) cannot be omitted. The horizontal, vertical and
mixed blocks are all in the actual metric.

The off-diagonal part is a single row/column coupling to \(U\).
Consequently

\[
\|E\|_{\mathrm{op}}\le
\frac{a^2(z_s')^2|b|^2}{2}
+\frac a2
\sqrt{(z_s')^2D^2+(z_s''+3kz_s')^2|b|^2}.
\tag{11}
\]

On the fixed interval \(0\le t\le1\), \(a\le C\ell\).
The form \(b\), metric \(h\), and profile are fixed, so this is
\(O(\ell)\). If \(b\) happens to be harmonic, the \(tU\) entry
vanishes, but harmonicity is not needed.
Outside this interval \(F=0\); the local gauge change of circle
coordinate makes (9) an exact hyperbolic product. At the right
endpoint the global change is precisely the circle-valued gluing (1).

## 5. Smooth closed assembly, volume and curvature bounds

Use the product \(b_{v,\ell}+h_v\) outside the disjoint edge collars,
and formulas (7), (9) within each. The fibre path is complete before
the shear starts. At every interface the interpolation profiles are
constant on a neighborhood, so all derivatives match.
On the right side the metric agrees with the actual pullback (5);
there is no replacement of a nontrivial mapping class or integral
shear by an isotopic identity. This constructs a positive smooth
metric on the fixed marked closed \(M\).

The finite number of disjoint active collars gives the maximum of
their error bounds, proving the first line of (2).
The circle shear has determinant one. Although the fibre path need
not preserve its area form pointwise, every \(h_{e,z}\) has the same
total area by Gauss--Bonnet. Integrating each collar over the closed
fibre therefore gives exactly the original product volume.
Thus

\[
\begin{aligned}
\operatorname{Vol}(G_\ell)
&=\sum_v\operatorname{Area}(B_v,b_{v,\ell})
             \operatorname{Area}(F_v,h_v)\\
&=\frac{4\pi^2}{9}\sum_v\chi(B_v)\chi(F_v)
 =\frac{4\pi^2}{9}\chi(M).
\end{aligned}
\tag{12}
\]

The boundaries have zero Euler characteristic, so the last equality
is the ordinary gluing formula. In particular, \(\chi(M)>0\).

In a unit frame on the circle and a fixed finite atlas on each fibre,
the connection coefficients on the path region use only bounded
fibre-family coefficients, \(k\), and \(S\).
On the shear region they additionally use \(a z_s'\beta_e\), its
fixed-order derivatives, and the fixed base connection.
No coefficient depends on the circle coordinate.
Repeated differentiation therefore gives uniform bounds for all
fixed-order curvature derivatives, and retains an \(L_\ell^{-1}\)
or \(\ell\) factor in each defect derivative.
Outside active regions the metric is locally a symmetric product.

There is a stronger local conclusion. Put
\(\varepsilon_\ell=L_\ell^{-1}+\ell\). On each active collar let
\(\mathcal R_0\) be the algebraic curvature tensor of the orthogonal
product of two curvature-\(-3\) planes, using the actual splitting
into the \((t,U)\)-plane and the horizontal fibre plane. If \(P\) is
the projection onto the first plane, then

\[
\begin{aligned}
|\nabla^j(\operatorname{Rm}-\mathcal R_0)|
 &\le C_j\varepsilon_\ell &&(j\ge0),\\
|\nabla^jP|&\le C_j\varepsilon_\ell &&(j\ge1).
\end{aligned}
\tag{13}
\]

In the path region the only mixing of the planes is the shape
operator \(S=O(L_\ell^{-1})\). The difference tensor consists of
the Gauss terms \(S\wedge S\), the normal terms \(D_tS+S^2\),
the circle-fibre terms \(kS\), and the Codazzi derivatives of \(S\).
Their fixed-order derivatives have the same bound.
In the shear region the only extra connection terms are
\(a z_s'\beta_e\); the curvature difference consists of their
first derivatives, their products, and products with the bounded
\(k\) and fibre connection. These are \(O(\ell)\), with the same
fixed-order bounds. The splitting is parallel on the unmodified
product regions. Since \(\mathcal R_0\) is algebraic in the metric
and \(P\), (15) implies the global estimates

\[
-3-C\varepsilon_\ell\le
 \operatorname{sec}_{G_\ell}\le C\varepsilon_\ell,
\qquad
\|\nabla^j\operatorname{Rm}_{G_\ell}\|_\infty
\le C_j\varepsilon_\ell\longrightarrow0
\quad(j\ge1).
\tag{14}
\]

No diameter or injectivity-radius bound follows. In particular,
approximate parallel curvature here does not assert a globally
locally symmetric metric on \(M\).

## 6. Symplectic structures in both orientations

The same closed smooth manifold admits symplectic structures in both
orientations. In fact the construction can be made almost Kähler in
both orientations without changing any of its estimates.

First choose the block area forms \(\omega_v=d\mu_{h_v}\). They have
the same total area. By Moser's argument each \(f_e\) is isotopic
to an \(f'_e\) with \((f'_e)^*\omega_w=\omega_v\).
Replacing an edge gluing by this isotopic gluing does not change the
closed oriented diffeomorphism type: a boundary isotopy extends through
the product collar. The shear function \(u_e\) is retained.
Any metrics or forms constructed with these adjusted gluings can
therefore be pulled back to the original fixed smooth \(M\).

For clarity, there is also an endpoint-fixed version of the
area adjustment of the hyperbolic path. Start with any path \(h_z\)
between the two now area-compatible endpoint metrics, and write
\(\omega_z=d\mu_{h_z}\), \(\omega_0=\omega_1=\omega_v\).
Choose a fixed linear right inverse for \(d\) on the exact two-forms
on the closed fibre, and put

\[
d\sigma_z=\omega_z-\omega_v,\qquad \sigma_0=\sigma_1=0.
\]

For each \(z\), apply Moser's argument in an auxiliary parameter
\(s\in[0,1]\) to
\(\omega_{s,z}=(1-s)\omega_v+s\omega_z\), using
\(\iota_{X_{s,z}}\omega_{s,z}=-\sigma_z\).
All these are positive area forms. Its time-one map \(\psi_z\)
satisfies
\(\psi_z^*\omega_z=\omega_v\); because the vector fields vanish
for \(z=0,1\), both endpoint maps are exactly the identity.
Thus \(\widetilde h_z=\psi_z^*h_z\) is a smooth curvature-\(-3\)
path with the same endpoint metrics and fixed area form \(\omega_v\).
All path bounds remain finite. This auxiliary-parameter construction
avoids assuming that an arbitrary Moser transport around a loop
has identity endpoint.

In the signed collar coordinates the following two-forms now match
the product forms on both incident blocks:

\[
\Omega_\pm
=a_\ell(t)\,dt\wedge\bigl(d\phi+z_s(t)\beta_e\bigr)
 \ \pm\ \omega_v .
\tag{15}
\]

On the preceding metric-path region take \(z_s=0\).
Outside collars use
\(d\mu_{b_{v,\ell}}\pm\omega_v\).
They agree under the actual area-preserving gluing, including its
circle-valued shear. They are closed: \(d\beta_e=0\), the
\(z_s'\) term contains two \(dt\)'s, and the fibre area form is
independent of \(t\). Moreover

\[
\Omega_\pm^2
=\pm2a_\ell\,dt\wedge(d\phi+z_s\beta_e)\wedge\omega_v
\ne0.
\tag{16}
\]

The two signs give the two orientations. With the common-area path,
these forms are compatible with the constructed metric: the horizontal
two-plane and fibre two-plane have their respective metric area forms.
Thus the near-Einstein sequence can also be chosen to carry compatible
almost Kähler structures of both orientations. This is not a claim
that the structures are integrable or that the metric is Einstein.

## 7. Relation to the inherited surface-bundle construction

If every \(f_e\) is the identity, projection to the common \(F\)
survives all gluings. The other factors assemble into the surface
fibre, with boundary rotations encoding multitwist monodromy.
Single-edge examples overlap the earlier \(E_D\) construction after
interchanging the two surface roles. These must not be advertised
as new smooth objects. Fixed isometries generate only finite holonomy
in the isometry group of a closed hyperbolic surface; that case also
requires care before asserting new topology.

The theorem itself allows arbitrary \(f_e\), including pseudo-Anosov
holonomy around graph cycles. The separate topology analysis
examines the self-gluing of \(B_{h,2}\times\Sigma_p\) with nonzero
integral shear and infinite-order \(f\). Its claim of absence of a
surface-bundle structure is not needed for the metric proof above.
This separates the proven construction from the group-theoretic
classification and from the still different question of whether
the resulting smooth manifold admits any Einstein metric.

The metric proof does not assert an Einstein correction or an
all-sign Einstein obstruction. Its advance is a fixed closed input
class with full unweighted Ricci defect tending to zero, rather than
another open-ended connector. The analytic ingredients are familiar
collar and submersion calculations; no literature-priority claim is
made for this assembly.

## 8. Coordinate checks

The accompanying round11_closed_gluing_check.py reconstructs the
Christoffel symbols and Ricci tensor from the coordinate metric. Its
shear test uses
\(h=(dx^2+e^{2x}dy^2)/3\) and \(\beta=dx+dy\), so that
\(\operatorname{div}_h\beta^\sharp=3\ne0\); it checks every entry
of (10), not just the trace. A second hyperbolic-path test uses
\(h_z=(dx^2+e^{2x+2z}dy^2)/3\), with nonzero \(H\), and checks
every entry of (8). Three deliberately incorrect mixed/trace
formulas are rejected. These are local tensor checks; the closed
assembly, fixed marking, estimates and symplectic argument are the
analytic and geometric proofs above.
