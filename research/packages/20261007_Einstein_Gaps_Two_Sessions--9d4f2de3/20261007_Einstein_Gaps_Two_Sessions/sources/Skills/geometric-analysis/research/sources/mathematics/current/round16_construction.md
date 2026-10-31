# A Maxwell-compatible waist receiver and the necessary exterior response

## 1. The closed geometric setting and the new conclusion

Let \(G_c\) be the optimized, fixed-topology, pure-shear closed family of
`round14_global.md`. Fix one edge with nonzero harmonic shear form \(\beta\)
on a fixed closed hyperbolic surface \((F,h_F)\), where \(K(h_F)=-3\).
On this edge write
\[
 G_c=dt^2+a^2\theta^2+h_F,\qquad
 a=c\cosh(kt),\quad k=\sqrt3,\quad
 \theta=d\phi+z(t)\beta,\quad \phi\in\mathbb R/2\pi\mathbb Z.
                                                               \tag{1}
\]
Set \(f=\operatorname{sech}^2(kt)\), \(\kappa=a'/a\), and use the
actual full-width profile
\[
 z'=I_c^{-1}\eta_R\operatorname{sech}^3(kt),\qquad
 I_c=\int_{\mathbb R}\eta_R\operatorname{sech}^3(kt)dt,
 \qquad z(-\infty)=0.                                      \tag{2}
\]
Here \(\eta_R\) is even, is one on \(|t|\le R-1\), vanishes for
\(|t|\ge R\), and has uniformly bounded derivatives. The collar radius
is \(R=w_c-C_0\), with fixed \(C_0>4\). In particular
\(e^{-kR}\asymp c\), and \(a\asymp1\) on fixed-width end bands.
Every statement below uses these genuine closed metrics, not a scalar Robin
model for an unknown filling.

The original waist test has an \(O(c^2)\) integrated adjoint error in
the interior because varying the waist without varying the connection
violates the linearized Maxwell equation. We remove this term exactly.
The corrected test has interior error \(O(c^3)\); its remaining
\(O(c^2)\) error is confined to the two fixed-width exterior cutoff bands.

Consequently a uniformly small solution of the **full linearized** Einstein
repair equation must produce an end response of at least order \(c\).
For a normalized nonlinear repair of size \(O(c)\), either that end
response survives or the quadratic equation must supply a specified,
positive order-\(c^3\) charge. These assertions impose no symmetry or
gauge on the perturbation. They locate the outstanding response more
precisely; they do not enlarge the already proved \(O(c)\) no-repair radius.

## 2. Re-solving Maxwell while varying the waist

Define
\[
 r_c=\int_{\mathbb R}f z'\,dt,\qquad
 \zeta'=2(f-r_c)z',\qquad \zeta(-\infty)=0.                 \tag{3}
\]
Since \(\int z'=1\), the integral of \(\zeta'\) is zero. Thus
\(\zeta(+\infty)=0\), and \(\zeta\) is supported in \([-R,R]\).
Evenness makes \(\zeta\) odd. For every fixed \(j\),
\[
 |\partial_t^j\zeta(t)|\le C_j\operatorname{sech}^3(kt).
                                                               \tag{4}
\]
For \(j=0\), integrate (3) toward the nearer zero endpoint and use
\(\int_t^\infty\operatorname{sech}^3(ks)ds
\le C\operatorname{sech}^3(kt)\) for \(t\ge0\).
For \(j\ge1\), differentiate (3). Its coefficients, and the cutoff
derivatives appearing in (2), have the required uniform bounds.

Formula (3) has a geometric origin. Write a waist variation in lapse/radius
form as
\[
 N_\tau^2=1+\tau f,\qquad b_\tau^2=a^2(1-\tau f).
\]
The Maxwell density is \(b_\tau^3/N_\tau
=a^3(1-2\tau f)+O(\tau^2)\). Differentiating the solution with the same
endpoint values gives \(\partial_\tau z_\tau|_0=\zeta\).
Where (2) is exactly Maxwell,
\[
 \partial_\tau\bigl((b_\tau^3/N_\tau)z_\tau'\bigr)\big|_0
 =-2r_c a^3z',                                               \tag{5}
\]
which is constant in \(t\). The correction is therefore compatible with
the mixed Einstein equation, not just chosen to alter a scalar projection.

As a check, on the entire infinite throat,
\[
 r_\infty=\frac34,\qquad
 \zeta_\infty(t)=\frac1\pi\operatorname{sech}^3(kt)\tanh(kt).
                                                               \tag{6}
\]
For a sharp finite Maxwell interval, put
\(J_m=\int_{-R}^R\operatorname{sech}^m(kt)dt\) and
\(d_R=\operatorname{sech}^3(kR)\tanh(kR)/(2kJ_3)\). Then
\[
 r=\frac{J_5}{J_3}=\frac34+d_R,\qquad
 \zeta(t)=\frac{\operatorname{sech}^3(kt)\tanh(kt)}{2kJ_3}
              +d_R(1-2z(t)).                                \tag{7}
\]
The second term is necessary to retain both actual endpoint values.

## 3. Exact gauged variation on the sheared core

Choose \(\chi=1\) on \([-R,R]\), zero outside \([-R-1,R+1]\),
with bounded derivatives. Define a globally smooth, trace-free tensor
supported on this collar by
\[
 \widetilde H_c=\chi f(dt^2-a^2\theta^2)+K_c,\qquad
 K_c=a^2\zeta(\theta\otimes\beta+\beta\otimes\theta).
                                                               \tag{8}
\]
Write \(E(g)=\operatorname{Ric}_g+3g\),
\(\mathcal B h=\delta h+\frac12d\operatorname{tr}h\), and
\[
 P=DE+\delta^*\mathcal B=\tfrac12\Delta_L+3.
                                                               \tag{9}
\]
All operators and contractions use \(G_c\), with
\((\delta h)_j=-\nabla^ih_{ij}\). The self-adjoint identity in (9)
holds at the approximate metric as well as at an Einstein metric.

Let \(B(x)=|\beta|_{h_F}^2\). Direct differentiation gives the exact
identities
\[
 \delta\{f(dt^2-a^2\theta^2)\}=0,
 \qquad \delta K_c=a^2\zeta z'B\,dt,
 \qquad \delta\widetilde H_c=-\chi'f\,dt+a^2\zeta z'B\,dt.
                                                               \tag{10}
\]
On \(|t|<R-1\), the Maxwell equation is exact. If \(U\) is the unit
circle vector and \(X,Y\) are horizontal fiber vectors, the nonzero
blocks of \(P\widetilde H_c\) are
\[
\begin{aligned}
 (P\widetilde H_c)_{tt}
  &=a^2\bigl(\tfrac12fz'^2-\kappa\zeta z'\bigr)B,\\
 (P\widetilde H_c)_{UU}
  &=a^2\bigl(-\tfrac32fz'^2+\zeta'z'+\kappa\zeta z'\bigr)B,\\
 (P\widetilde H_c)_{XY}
  &=a^2(fz'^2-z'\zeta')\beta(X)\beta(Y),\\
 (P\widetilde H_c)_{tX}
  &=\tfrac12a^2\zeta z'\,dB(X),\\
 (P\widetilde H_c)_{XU}
  &=a^3\zeta z'^2 B\beta(X).
\end{aligned}                                                 \tag{11}
\]
In particular the mixed block is cubic, not identically zero.

Here is a derivation that retains the coordinate-frame and gauge terms.
The uncorrected waist variation has mixed component \(af'z'\beta\).
The connection variation of \(E\) has mixed component
\[
 -\frac a2(\zeta''+3\kappa\zeta')\beta
       +\frac12a^3\zeta z'^2B\beta.
\]
The first term is \(-af'z'\beta\) by (3) and Maxwell. The second
comes from differentiating the tensor in the fixed, rather than varying,
horizontal frame. The mixed component of
\(\delta^*(a^2\zeta z'B\,dt)\) supplies the other half of the cubic
term. Its remaining contributions are
\[
\begin{aligned}
 (\delta^*\delta K)_{tt}&=a^2z'(\zeta'-\kappa\zeta)B,\\
 (\delta^*\delta K)_{UU}&=\kappa a^2\zeta z'B,\\
 (\delta^*\delta K)_{tX}&=\tfrac12a^2\zeta z'dB(X).
\end{aligned}
\]
Together with the diagonal connection variation and the Round 14 waist
variation these give (11). No bound on an inverse Einstein operator is used.

## 4. The interior improves; the physical ends do not disappear

Let
\[
 \mathcal A_c=\{R\le |t|\le R+1\}
\]
be the two outer tensor-cutoff bands. All constants below depend on fixed
fiber and gluing data but not on \(c\). We claim
\[
\begin{aligned}
 \|\widetilde H_c\|_{L^1}&\le Cc,\\
 \|P\widetilde H_c\|_{L^1(M\setminus\mathcal A_c)}
       +\|\delta\widetilde H_c\|_{L^1(M\setminus\mathcal A_c)}
       &\le Cc^3,\\
 \|P\widetilde H_c\|_{L^1(\mathcal A_c)}
       +\|\delta\widetilde H_c\|_{L^1(\mathcal A_c)}
       &\le Cc^2.                                           \tag{12}
\end{aligned}
\]

On the central region, (4) and (11) imply
\[
 |P\widetilde H_c|\le C(c^2\operatorname{sech}^4(kt)
                             +c^3\operatorname{sech}^6(kt)),
 \qquad |\delta\widetilde H_c|\le Cc^2\operatorname{sech}^4(kt).
                                                               \tag{13}
\]
The volume measure is \(a\,dt\,d\phi\,d\mu_F\); integrating (13)
gives \(O(c^3)\). The waist part of (8) has \(L^1\) norm \(O(c)\),
and its connection part has pointwise norm
\(O(a|\zeta|)=O(c\operatorname{sech}^2(kt))\) and \(L^1\)
norm \(O(c^2)\).

In the Maxwell-cutoff strips \(R-1\le |t|\le R\),
\(a\asymp1\), the connection curvature and all its fixed derivatives
are \(O(c^3)\), \(K_c\) and its first two derivatives are
\(O(c^3)\), and \(f\) and its derivatives are \(O(c^2)\).
In a local circle gauge subtract the constant endpoint connection.
The metric is then \(O(c^3)\) in every fixed derivative from its
hyperbolic product value. The uncut waist tensor is an exact product
kernel; hence its \(P\)-error there is \(O(c^5)\), whereas the
correction contributes \(O(c^3)\). These bounded-volume strips
therefore obey the interior bound in (12).

On \(\mathcal A_c\) the connection is flat and \(K_c=0\).
Only the tensor-cutoff commutator remains. Its size is \(O(c^2)\)
on a bounded-volume set. This proves (12). It also identifies precisely
why correcting Maxwell does not, by itself, produce a global adjoint
kernel with error \(O(c^3)\): the true exterior extension is still missing.

## 5. The signed source and an all-mode end-response theorem

Set \(B_0=\|\beta\|_{L^2(F)}^2>0\). The waist pairing is
\[
 \int_M\langle E(G_c),\chi f(dt^2-a^2\theta^2)\rangle
 =-2\pi c^3B_0
 \frac{\int\eta_R^2\operatorname{sech}^5(kt)dt}{I_c^2}
 =-3kB_0c^3+O(c^6).                                         \tag{14}
\]
The pairing with \(K_c\) vanishes on the exact Maxwell core: the
residual has no mixed circle-fiber component there. On the Maxwell-cutoff
strips both that component and \(K_c\) are \(O(c^3)\).
Thus the complete corrected pairing retains the same leading term:
\[
 \boxed{\int_M\langle E(G_c),\widetilde H_c\rangle
                  =-3kB_0c^3+O(c^6).}                      \tag{15}
\]

For an arbitrary smooth global symmetric tensor \(h\), write
\[
 \eta(h)=\sum_{j=0}^2\|\nabla^jh\|_{L^\infty(G_c)},
 \qquad b(h)=\sum_{j=0}^1
                 \|\nabla^jh\|_{L^\infty(G_c;\mathcal A_c)}.
\]
Integration by parts on the **closed** manifold gives
\[
\begin{aligned}
 \int\langle DE[h],\widetilde H_c\rangle
 &=\int\langle h,P\widetilde H_c\rangle
      -\int\langle\mathcal B h,\delta\widetilde H_c\rangle,\\
 \boxed{\left|\int\langle DE[h],\widetilde H_c\rangle\right|
       \le C\bigl(c^3\eta(h)+c^2b(h)\bigr).}               \tag{16}
\end{aligned}
\]
Both all-mode feedback and the ungauged Bianchi contribution are present.

**Linear end-response theorem.** There are \(\eta_0,b_0,c_0>0\)
such that, if \(0<c<c_0\), \(\eta(h)\le\eta_0\), and
\[
 DE_{G_c}[h]=-E(G_c),
\]
then
\[
 \boxed{b(h)\ge b_0c.}                                     \tag{17}
\]
Indeed (15)--(16) imply
\(3kB_0c^3-O(c^6)\le Cc^3\eta_0+Cc^2b(h)\).
Choose \(\eta_0\) so that the first term on the right is at most
\(kB_0c^3\), then reduce \(c_0\). In particular no uniformly small
linear repair supported away from these ends exists.

This is a conclusion for the actual sheared metric and unrestricted
tensors, rather than the product-sector Dirichlet calculation alone.
It does not say that a geometrically admissible exterior can, or cannot,
supply the response in (17).

## 6. The nonlinear alternatives at the critical repair scale

Uniform curvature control gives the pointwise Taylor estimate
\[
 E(G_c+h)=E(G_c)+DE_{G_c}[h]+Q_c(h),\qquad
 |Q_c(h)|\le C\eta(h)^2                                   \tag{18}
\]
for \(\eta(h)\) smaller than a fixed positive constant.
This is the tensor difference-of-connections estimate; it requires neither
a Sobolev constant nor an injectivity-radius bound. Equations (12),
(15), (16), and (18) imply the necessary inequality for every normalized
Einstein repair \(\operatorname{Ric}_{G_c+h}=-3(G_c+h)\):
\[
 \boxed{3kB_0c^3-O(c^6)
       \le C\bigl(c^3\eta(h)+c^2b(h)+c\eta(h)^2\bigr).}    \tag{19}
\]

There is a sharper statement than the inequality when the exterior response
is smaller than the critical scale. If exact normalized repairs \(h_c\)
satisfied
\[
 \eta(h_c)=O(c),\qquad b(h_c)=o(c),
\]
then (16) is \(o(c^3)\), and the exact equation forces
\[
 \boxed{\lim_{c\to0}c^{-3}
      \int_M\langle Q_c(h_c),\widetilde H_c\rangle
          =3k\|\beta\|_2^2>0.}                            \tag{20}
\]
Such a repair must be driven at leading order by a positive nonlinear
receiver charge. It cannot be explained as a small linear throat response
with negligible end data. Formula (20) does not assert that the required
nonlinear charge is impossible.

The quadratic term \(c\eta^2\) and the end term \(c^2b\) are both
of order \(c^3\) at \(\eta\asymp b\asymp c\). Therefore these
estimates do not justify any larger universal no-repair ball. Round 14's
all-sign Einstein exclusion in the small \(\varepsilon c\) ball remains
valid; (20) is a more precise statement about normalized potential repairs
outside that excluded ball.

## 7. Genuine hyperbolic length variations and product exteriors

The exterior terms are not arbitrary Robin constants. A complementary exact
calculation identifies what genuine hyperbolic product exteriors can do
inside the closed product-block family.

Let the fiber gluings be the identity, with fixed integral shears. Vary one
paired base boundary length \(\ell_e=2\pi c_e\) through hyperbolic
metrics with geodesic boundary, using Fenchel--Nielsen coordinates on the
base pieces and matching the paired lengths. Fix a reference \(c_e>0\)
and keep \(z_e(t)\) fixed in a compact collar available throughout a
small parameter neighborhood. The connection is constant near its ends,
so the same fixed smooth gluing remains valid. No change in smooth topology
or lattice marking is introduced.

The closed volume is
\[
 V_*=\sum_v\operatorname{Area}(B_v)\operatorname{Area}(F),
\]
independent of all base lengths and twists, by Gauss--Bonnet. The exact
connection-energy coefficient is
\[
 q_e(c_e)=\int a_e^3(z_e')^2dt
       =c_e^3\int\cosh^3(kt)(z_e')^2dt.                    \tag{21}
\]
The normalized total scalar curvature of the **whole closed metric** is
\[
 \mathscr S=-12\sqrt{V_*}
       -\frac\pi{\sqrt{V_*}}\sum_e q_e(c_e)\|\beta_e\|_2^2.
\]
Consequently, for every nonzero shear on the varied edge,
\[
 \boxed{\frac{\partial\mathscr S}{\partial\log c_e}
       =-\frac{3\pi}{\sqrt{V_*}}q_e\|\beta_e\|_2^2<0.}    \tag{22}
\]
This includes the actual exterior product blocks; their length dependence
does not generate a missing balancing term. Fiber Hodge-stress balance,
even when realizable, therefore does not make these waist parameters
stationary. The profiles in (21)--(22) are held fixed during differentiation;
these formulas must not be applied without correction to an independently
reoptimized, moving-cutoff profile.

For comparison, on the unsheared local collar the waist kernel has the
exact decomposition
\[
 f(dt^2-a^2d\phi^2)
 =-\tfrac12\partial_{\log c}
          (dt^2+a^2d\phi^2)
       +\mathcal L_X(dt^2+a^2d\phi^2),\qquad
 X=\frac{\tanh(kt)}{2k}\partial_t.                         \tag{23}
\]
Thus this is a genuine length variation together with a radial gauge
change. It is not the pure angular twist gauge described in Round 15.
The vector \(X\) approaches nonzero end values, so simply extending it
by zero is not an exact global gauge argument. Constructing a globally
compatible adjoint extension, with its full Bianchi data and quantitative
norms, is precisely the remaining step if one seeks to remove the last
\(O(c^2)\) term in (12).

The length-coordinate input is classical; a source describing hyperbolic
pants and length/twist parameters is Scott Wolpert's
[Fenchel--Nielsen coordinates](https://www.math.umd.edu/~saw/preprints/WP_sampler.pdf).
The new calculation here is (3), (11)--(20) on the actual sheared geometry,
not the existence of those coordinates.

## 8. Verification and next equation

`round16_construction_check.py` recomputes the connection variation from
coordinate Ricci, computes the divergence directly, and checks all ten
blocks in (11), the endpoint Maxwell correction, its finite and infinite
profiles, and the signed cubic coefficient. It explicitly rejects the
incorrect claim that the corrected mixed block vanishes exactly. The
coordinate model \(h_F=(dx^2+dy^2)/(3y^2)\), \(\beta=dx\) checks a
nonconstant \(|\beta|^2\), including the \(dB\) term. The invariant
formulas and uniform estimates are proved in §§2--6; the finite check is
not a replacement for those arguments or an exterior existence theorem.

The next substantive question is now localized: can the actual exterior
Einstein response supply the order-\(c\) end data in (17), or can the
full quadratic equation supply the positive charge in (20)? Resolving
either requires the real exterior and all-mode equation. Product-family
stationarity, a formal Robin response, or fiber stress cancellation alone
does not settle it.
