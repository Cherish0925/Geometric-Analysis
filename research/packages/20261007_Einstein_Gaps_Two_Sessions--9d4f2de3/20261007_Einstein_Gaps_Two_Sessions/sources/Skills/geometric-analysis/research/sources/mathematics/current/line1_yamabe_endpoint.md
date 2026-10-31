# What negative Yamabe normalization preserves—and what it does not

23 September 2026. Pointwise almost-Einstein input admits a uniformly small
scalar-normalizing conformal change in \(C^1\) and normalized \(W^{2,2}\),
without injectivity-radius, Sobolev, or scalar spectral-gap assumptions.
Nevertheless that conformal change need not preserve pointwise Ricci
approximation: the normalized Ricci error can diverge. An explicit
counterexample below occurs on a fixed product of hyperbolic surfaces,
with bounded input sectional curvature and no collapse.

Throughout, \(\Delta=d^*d=-\operatorname{div}\nabla\), and all norms of
\(u\) and its derivatives use the original metric unless indicated.

## 1. A uniform positive result

**Theorem 1.** Let \((M^4,g)\) be closed, connected, and smooth, and suppose
\[
 \|g^{-1}\operatorname{Ric}_g+I\|_{\infty,\mathrm{op}}
 \le\varepsilon\le\frac14.
 \tag{1}
\]
There is a unique positive smooth function \(u\) for which
\(\widehat g=u^2g\) has scalar curvature \(-4\). Put \(e=s_g+4\),
\(V=\operatorname{Vol}(g)\). Then
\[
 1-\varepsilon\le u^2\le1+\varepsilon,
 \qquad \|du\|_\infty\le4\varepsilon,
 \tag{2}
\]
In particular \(\|g^{-1}\widehat g-I\|_\infty\le\varepsilon\) and
\((1-\varepsilon)^2V\le\operatorname{Vol}(\widehat g)
\le(1+\varepsilon)^2V\).
\[
 \int\bigl((u-1)^2+|du|^2+|\nabla^2u|^2\bigr)
 \le\frac38\int e^2\le6\varepsilon^2V.
 \tag{3}
\]
The normalized metric has the integral Einstein-error bound
\[
 \int|\operatorname{Ric}_{\widehat g}+\widehat g|^2_{\widehat g}
 \le\int|\operatorname{Ric}^{\circ}_g|^2_g
 \le4\varepsilon^2V,
 \qquad
 \fint_{\widehat g}|\operatorname{Ric}_{\widehat g}+\widehat g|^2
 \le\frac{4\varepsilon^2}{(1-\varepsilon)^2}.
 \tag{4}
\]
Thus the scalar-normalizing change is \(C^1\)-small, with a second-order
integral estimate. No bound on \(\nabla\operatorname{Ric}\) or full
curvature has been assumed. No monopole assumption is needed.

### Proof of existence, amplitude, and integral estimates

Since \(s_g\le-3\), the conformal Yamabe constant is negative. The
Yamabe theorem gives a negative constant-scalar representative, which can
be uniquely rescaled to scalar curvature \(-4\). Uniqueness also follows
directly: the ratio of two such factors solves
\(6\Delta z-4z+4z^3=0\) on one normalized metric; the maximum and
minimum principles force \(z=1\).

The factor satisfies
\[
 6\Delta u+(-4+e)u+4u^3=0.
 \tag{5}
\]
At its maximum and minimum the signs of \(\Delta u\) give (2)'s
amplitude bound. Write \(v=u-1\) and \(a=4u(u+1)\). Then
\[
 6\Delta v+av=-eu,\qquad
 6\le a\le10,\qquad u\le9/8.
 \tag{6}
\]
Pairing with \(v\) gives
\[
 \|v\|_2\le\frac3{16}\|e\|_2,
 \quad \|dv\|_2^2\le\frac9{256}\|e\|_2^2,
 \quad \|\Delta v\|_2\le\frac12\|e\|_2.
 \tag{7}
\]
The last bound follows by substituting the first one into (6).
Integrated Bochner and \(\operatorname{Ric}\ge-5g/4\) give
\[
 \|\nabla^2v\|_2^2
 =\|\Delta v\|_2^2-\int\operatorname{Ric}(dv,dv)
 \le\frac{301}{1024}\|e\|_2^2.
 \tag{8}
\]
Adding the three bounds proves (3). These are estimates on the original
closed metric, not elliptic estimates in uniformly controlled charts.

### Proof of the maximum gradient bound

Rewrite (5) as
\[
 (\Delta+4/3)v=F,
 \qquad F=-eu/6-2v^2-(2/3)v^3,
 \qquad \|F\|_\infty\le2\varepsilon.
 \tag{9}
\]
Here \(|v|\le\varepsilon\) and \(|e|\le4\varepsilon\).
For the heat semigroup \(P_t=e^{-t\Delta}\), Bochner under
\(\operatorname{Ric}\ge-Kg\) gives
\[
 |\nabla P_t f|^2
 \le\frac{K}{1-e^{-2Kt}}
       \bigl(P_t(f^2)-(P_tf)^2\bigr)
 \le\left(K+\frac1{2t}\right)\|f\|_\infty^2.
 \tag{10}
\]
One direct derivation is to differentiate
\(P_s[(P_{t-s}f)^2]\), integrate from \(0\) to \(t\), and use
\(|\nabla P_t f|^2\le e^{2Ks}P_s|\nabla P_{t-s}f|^2\).
The second inequality uses \(1-e^{-x}\ge x/(1+x)\).
The positive-mass resolvent therefore satisfies
\[
 \|\nabla(\Delta+m)^{-1}f\|_\infty
 \le\left(\frac{\sqrt K}{m}+\sqrt{\frac\pi{2m}}\right)\|f\|_\infty.
 \tag{11}
\]
Indeed, integrate \(e^{-mt}\nabla P_tf\) over \(t>0\); the bound
is integrable both at zero and at infinity. With \(K=5/4\) and
\(m=4/3\), the coefficient is
\(3\sqrt5/8+\sqrt{3\pi/8}<2\). Equations (9)–(11) prove (2).

### Proof of the Ricci-energy bound

For a negative Yamabe class, \(\int s_{\widehat g}^2\le\int s_g^2\).
For example, if \(\widehat g_0=z^2g\) has volume one, its Yamabe
constant is
\(Y=\int(6|dz|^2+s_gz^2)\ge-\|s_-\|_2\); hence
\(\int s_{\widehat g}^2=Y^2\le\int s_g^2\).
In four dimensions, \(\int|W^+|^2\) is conformally invariant and
\[
 \int|\operatorname{Ric}^{\circ}|^2
 =4\int|W^+|^2+\frac1{12}\int s^2-8\pi^2(2\chi+3\tau).
 \tag{12}
\]
This is the conformal monotonicity proved in
[`line1_energy_selection.md`](line1_energy_selection.md), Section 4;
the argument is included here to make its lack of monopole assumptions
explicit. Thus the trace-free Ricci energy cannot increase. Since
\(s_{\widehat g}=-4\), this is its full Einstein-error energy.
Finally \(\operatorname{Vol}(\widehat g)\ge(1-\varepsilon)^2V\).
This proves (4). All integrals and averages on the left side of (4)
use \(d\mu_{\widehat g}\), not the input volume measure.
For a nonorientable manifold, apply the curvature-energy argument on its
oriented double cover and divide the integrals by two; uniqueness makes
the scalar-normalizing factor descend. The same estimates therefore hold.

## 2. An actual failure of pointwise Ricci preservation

**Theorem 2.** There is a fixed closed manifold
\(M=\Sigma_1\times\Sigma_2\), with both genera at least two, and
smooth metrics \(g_L\) such that
\[
 \|g_L^{-1}\operatorname{Ric}_{g_L}+I\|_\infty
       =O((\log L)/L)\to0,
 \tag{13}
\]
while their scalar-\(-4\) Yamabe representatives satisfy
\[
 \liminf_{L\to\infty}\frac1{\log L}
 \|\widehat g_L^{-1}\operatorname{Ric}_{\widehat g_L}+I\|_\infty
 \ge\frac23.
 \tag{14}
\]
In particular, the normalized maximum Ricci error tends to infinity.
The input metrics have uniformly bounded sectional curvature, diameter,
and positive injectivity radius and scalar spectral gap. They converge
in \(C^{1,\alpha}\), for every fixed \(0<\alpha<1\), to a fixed
negative Einstein product. Thus none of those geometric controls repairs
the failed endpoint conclusion.

### A smooth two-dimensional bump

Fix hyperbolic metrics \(h_i\) of curvature \(-1\). In an isothermal
coordinate disk about \(p\in\Sigma_1\), choose coordinates with
\(h_1(p)=dx^2+dy^2\). Take a fixed radial smooth cutoff \(\chi\),
equal to one near \(p=(0,0)\), supported inside the disk. Put
\[
 v_L(x,y)=-\frac{\log L}{2L}\,\chi(x,y)\,xy
                 \log(x^2+y^2+e^{-2L}),
 \tag{15}
\]
for \(L>e\), and extend by zero. With \(r^2=x^2+y^2\) and \(b>0\), direct
differentiation gives
\[
 (\partial_x^2+\partial_y^2)
     [xy\log(r^2+b)]
 =4xy\frac{2r^2+3b}{(r^2+b)^2}.
 \tag{16}
\]
Its absolute value is at most four. The function and its first
derivatives are bounded uniformly for \(b=e^{-2L}\); cutoff errors
have fixed support away from the singular point. In two dimensions the
isothermal Laplacian is a smooth fixed multiple of the Euclidean one.
Consequently
\[
 \|v_L\|_{C^1}+\|\Delta_{h_1}v_L\|_\infty=O((\log L)/L),
 \quad \|\nabla_{h_1}^2v_L\|_\infty\le C\log L,
 \quad \nabla_{h_1}^2v_L(p)=(\log L)H,
 \tag{17}
\]
where \(H=dx\otimes dy+dy\otimes dx\). At \(p\), \(dv_L=0\),
so no connection term changes this Hessian. Interpolation gives
\[
 [dv_L]_{C^{0,\alpha}}
 \le C_\alpha\|dv_L\|_\infty^{1-\alpha}
                    \|\nabla^2v_L\|_\infty^\alpha
 \le C_\alpha(\log L)L^{\alpha-1}\longrightarrow0
\]
for every fixed \(\alpha<1\). Thus \(v_L\to0\) in
\(C^{1,\alpha}\) despite the unbounded central Hessian.

### The input Ricci tensor

Set
\[
 g_L=e^{2v_L}h_1+h_2.
 \tag{18}
\]
The first factor's Gaussian curvature is
\(K_L=e^{-2v_L}(-1+\Delta_{h_1}v_L)\); the second has curvature
\(-1\). Thus (17) proves (13). All mixed sectional curvatures vanish,
and the two factor curvatures remain in a fixed negative interval.
This gives uniform sectional-curvature bounds. Bilipschitz convergence
to the fixed product bounds diameter and the scalar spectral gap.
There are no conjugate points on either factor, and lengths of
noncontractible loops are bounded below by bilipschitz comparison;
the product therefore also has a uniform positive injectivity radius.

### Exact scalar normalization exposes the Hessian

Seek a positive scalar-normalizing factor depending only on \(\Sigma_1\).
Its equation, after multiplication by \(e^{2v}\), is
\[
 6\Delta_{h_1}u+(-2+2\Delta_{h_1}v-2e^{2v})u+4e^{2v}u^3=0.
 \tag{19}
\]
The substitution \(u=e^{-v/3}w\) cancels the entire \(\Delta v\)
term and gives
\[
 6\Delta_{h_1}w+4\langle dv,dw\rangle
  +\left(-\frac23|dv|^2-2-2e^{2v}\right)w
  +4e^{4v/3}w^3=0.
 \tag{20}
\]
For fixed \(0<\alpha<1\), the left side is a smooth map from
\(C^{1,\alpha}(\Sigma_1)\times C^{2,\alpha}(\Sigma_1)\) to
\(C^{0,\alpha}(\Sigma_1)\). At \((v,w)=(0,1)\), its derivative
in \(w\) is \(6\Delta_{h_1}+8\), an isomorphism. The implicit
function theorem supplies positive \(w_L\to1\) in \(C^{2,\alpha}\).
Then \(u_L=e^{-v_L/3}w_L\) solves the actual four-dimensional scalar
equation. Uniqueness in Theorem 1 identifies it with the negative
Yamabe factor; no symmetry of a hypothetical factor was assumed.

At \(p\), (17) now gives
\[
 u_L(p)=w_L(p)\to1,\quad du_L(p)=dw_L(p)\to0,\quad
 \nabla_{g_L}^2u_L(p)
 =\nabla_{h_1}^2w_L(p)-\frac{w_L(p)\log L}{3}H.
 \tag{21}
\]
Here the connections of \(g_L\) and the fixed product converge in
\(C^0\), and \(dv_L(p)=0\). The four-dimensional conformal formula
is
\[
 \operatorname{Ric}^{\circ}_{u^2g}
 =\operatorname{Ric}^{\circ}_g
       -2u^{-1}(\nabla_g^2u)^\circ
       +4u^{-2}(du\otimes du)^\circ.
 \tag{22}
\]
The trace-free operation on covariant two-tensors is unchanged by a
conformal rescaling. At \(p\), the background connection is precisely
the fixed product connection because \(v_L(p)=dv_L(p)=0\). Also
\(\Delta v_L(p)=0\), so the input Ricci tensor is exactly
\(-g_L\) there. The first term on the right of (21), extended by zero
on the second factor, tends to zero. Substitution into (22) therefore
gives the covariant-tensor expansion
\[
 (\operatorname{Ric}_{\widehat g_L}+\widehat g_L)(p,y)
       =\frac23(\log L)H+o(1).
\]
The coefficient \(w_L(p)\) cancels against \(u_L(p)^{-1}\).
Raising an index uses \(\widehat g_L(p,y)=w_L(p)^2g_0(p,y)\).
Since \(w_L(p)\to1\) and \(\|H\|_{\rm op}=1\), the pointwise
operator norm divided by \(\log L\) tends to \(2/3\). This proves
(14). If the prefactor \(\log L\) is replaced by one throughout,
the same argument gives the finite endpoint defect \(2/3\); the
slowly growing prefactor establishes the stronger unbounded statement.

## 3. Consequence for the first research line

The counterexample is compatible with all integral results above:
\(\|\nabla^2u_L\|_2\to0\), even though its value at \(p\)
diverges. Each input is a Kähler product on a fixed general-type
surface. For its canonical class the exact Kähler identities give
\(D_{LB}=\int(s-\bar s)^2/(64\pi^2)\to0\) and
\(p-a^2\to0\). Thus the obstruction is not missing monopole data,
negative-square control, or a scalar spectral gap.

This rules out one proposed passage from pointwise input to a convenient
scalar-normalized pointwise input. It does not rule out other corrections:
the limiting product itself is Einstein. The theorem also does not show
that actual weighted-monopole forms must have zeros; that is a different
question and requires its own argument.

Round 14 normalized a specific shear family whose lifted coefficients
had uniform higher-derivative bounds, sufficient for Schauder estimates.
Theorem 1 needs no such bounds, and Theorem 2 explains why its universal
conclusion must stop short of a maximum-norm Hessian or Ricci estimate.
The logarithmic bump is the classical endpoint Laplacian/Hessian
mechanism; the contribution here is its realization inside an actual
Ricci-pinched family and its exact scalar-normalizing equation.

`line1_yamabe_endpoint_check.py` verifies finite differential identities,
norm conventions, and constants. Existence uses the classical negative
Yamabe theorem and the explicitly stated fixed-background implicit
function theorem, not the finite checks.
