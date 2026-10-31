# Quantitative near equality for the genuine scalar--Weyl monopole estimate

## 1. Scope and conventions

This note analyzes the exact-boundary family

\[
 M=\Bigl(\#_{j=1}^{m}X_j\Bigr)\#N,\qquad m=2\ \text{or}\ 3,
\]

under the hypotheses used by Ishida--LeBrun to produce all sign monopole
classes.  Put

\[
 A=\sum_j c_1^2(X_j),\qquad
 D=4m-(2\chi+3\tau)(N),\qquad D=A/3,
\]

so that \(T=(2\chi+3\tau)(M)=2A/3\).  The analysis uses only the genuine
estimate

\[
 \int_M(s-\sqrt6|W_+|)^2\,d\mu\ge 72\pi^2(a^+)^2.                 \tag{1}
\]

No pure \(W_+\) lower bound is used.

The proof of (1) is Proposition 3.8 in
`Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md`.
The older conformal proof and its equality statement are Theorem 2.3 and
Proposition 2.4 in
`Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md`.
The sign classes and boundary obstruction are Proposition 10, Corollary 11,
and Theorem D in
`Knowledge/objects/papers/Curvature-Connected-Sums-and-Seiberg-Witten-Theory--7e92a6723434--2ac6d11897c5/object.md`.

Write \(w=|W_+|\) and

\[
 h=s-\sqrt6w,\qquad q=-h.
\]

For the pinched metrics considered below, \(|s+4|\le4\delta\), so \(q>0\)
as soon as \(\delta<1\).  If \(a\) is a monopole class, let \(H_a\) denote
the real harmonic self-dual two-form representing \(a^+\), normalized by

\[
 \int|H_a|^2=(a^+)^2=:p.
\]

The convention for a unitary connection is that \(iF_A\) is real and has
harmonic self-dual part \(2\pi H_a\).

## 2. Exact analytic deficit decomposition

The rescaled Seiberg--Witten equations are

\[
 D_A\Phi=0,\qquad -iF_A^+=f\sigma(\Phi),                         \tag{2}
\]

where \(f>0\).  Set

\[
 \rho=|\Phi|^2,\qquad \psi=2\sqrt2\,\sigma(\Phi),\qquad
 \varphi=\frac32\psi=3\sqrt2\,\sigma(\Phi),\qquad u=|\varphi|.
\]

Thus \(|\psi|=\rho\), \(u=3\rho/2\), and

\[
 f\varphi=3\sqrt2(-iF_A^+).                                     \tag{3}
\]

The following four nonnegative quantities record every differential
inequality in the proof:

\[
\begin{aligned}
 D_{\rm amp}&=2\int|d\rho|^2,\\
 D_{\rm quad}&=\int\left(4\rho|\nabla_A\Phi|^2-|\nabla\psi|^2\right),\\
 D_{\rm Hodge}&=\int\left(|d\psi|^2+|d^*\psi|^2\right),\\
 D_{\rm eig}&=2\int\left[W_+(\psi,\psi)+\sqrt{\frac23}\,w|\psi|^2\right].
                                                                    \tag{4}
\end{aligned}
\]

Here \(D_{\rm amp}\) is the term discarded after multiplying the spinor
Weitzenbock formula by \(\rho\); \(D_{\rm quad}\) is the quadratic-map/Kato
defect; \(D_{\rm Hodge}\) is the self-dual Hodge-Weitzenbock defect; and
\(D_{\rm eig}\) is the sharp trace-free endomorphism defect.  In particular,
the last quantity vanishes precisely where the nonzero \(\psi\) lies in the
lowest eigenspace and the two other eigenvalues coincide.  Put

\[
 D_0=D_{\rm amp}+D_{\rm quad}+D_{\rm Hodge}+D_{\rm eig}.
\]

Keeping the discarded terms in the published proof gives the exact identity

\[
 P_f:=\int(qu^2-fu^3)=\frac{27}{8}D_0.                           \tag{5}
\]

To track the two Holder steps, define

\[
\begin{gathered}
 X_f=\left(\int q^3f^{-2}\right)^{1/3},\quad
 A_f=\left(\int f^4\right)^{1/3},\quad
 Z_f=\int fu^3,\quad C_f=\int f^2u^2,\\
 H_1=X_fZ_f^{2/3}-\int qu^2,\qquad
 H_2=A_fZ_f^{2/3}-C_f.                                          \tag{6}
\end{gathered}
\]

Both \(H_1,H_2\ge0\).  Finally, the harmonic-projection defect is

\[
 J_A=\int|iF_A^+-2\pi H_a|^2,                                  \tag{7}
\]

and orthogonality of the Hodge projection gives

\[
 C_f=18\int|F_A^+|^2=72\pi^2p+18J_A.                            \tag{8}
\]

If

\[
 L_f=A_fX_f^2,
\]

then the entire proof before choosing \(f\) is the exact nonnegative
decomposition

\[
 \boxed{
 L_f-72\pi^2p
 =18J_A+H_2+
 A_f\frac{X_f+Z_f^{1/3}}{Z_f^{2/3}}(P_f+H_1).}                  \tag{9}
\]

This identity is more informative than merely saying that every inequality
is nearly sharp.

### The optimal weight

Take \(f=\sqrt q\).  If this weight is smooth, set

\[
 E=\int q^2,\quad Z=\int fu^3,\quad
 \theta=(Z/E)^{1/3},\quad H=E^{1/3}Z^{2/3}-\int f^2u^2.
\]

Then \(X_f=A_f=E^{1/3}\), the two Holder gaps in (6) are the same
number \(H\), and

\[
 P_f+H=E\theta^2(1-\theta),\qquad 0<\theta\le1.                 \tag{10}
\]

For the scalar--Weyl deficit

\[
 \Delta_a:=E-72\pi^2p,                                         \tag{11}
\]

(9) becomes

\[
 \boxed{
 \Delta_a=18J_A+H+(P_f+H)\frac{1+\theta}{\theta^2}.}            \tag{12}
\]

Consequently

\[
 \boxed{
 J_A\le\frac{\Delta_a}{18},\quad
 P_f\le\frac{\Delta_a}{2},\quad
 H\le\frac{\Delta_a}{3},\quad
 D_0\le\frac{4\Delta_a}{27}.}                                 \tag{13}
\]

Every one of the four terms in (4) is therefore at most
\(4\Delta_a/27\).  Since \(\psi\) is self-dual,
\(D_{\rm Hodge}=2\int|d\psi|^2\), and hence

\[
 \int|d\psi|^2\le\frac{2\Delta_a}{27},\qquad
 \int|d\rho|^2\le\frac{2\Delta_a}{27}.                       \tag{14}
\]

There is also a direct stability estimate for equality in Holder.  With the
probability measure \(d\nu=f^4d\mu/E\) and \(r=u/f\), one has
\(\int r^3d\nu\le\int r^2d\nu\le1\).  The interpolation inequality
\((\int r^2)^2\le(\int r)(\int r^3)\) therefore yields

\[
 \boxed{\int f^2(u-f)^2\le E-\int f^2u^2\le\Delta_a.}           \tag{15}
\]

Combining (3), (7), and (15) gives the unconditional \(L^2\) conclusions

\[
 \boxed{
 \|iF_A^+-2\pi H_a\|_2^2\le\frac{\Delta_a}{18},\qquad
 \|f\varphi+6\sqrt2\pi H_a\|_2^2\le\Delta_a,}                \tag{16}
\]

and

\[
 \boxed{
 \left\||2\pi H_a|-\frac{q}{3\sqrt2}\right\|_2
 \le 2\sqrt{\frac{\Delta_a}{18}}.}                            \tag{17}
\]

In general \(w=|W_+|\) is only Lipschitz at the zero set of \(W_+\), so the
optimal \(f\) need not be smooth.  The rigorous interpretation is to take
smooth positive \(f_k\to\sqrt q\) uniformly and use a rescaled monopole for
each \(f_k\).  Formula (9) is exact for every \(k\), \(L_{f_k}\to E\), and
(13)--(17) hold with \(\Delta_a+o(1)\).  Thus they assert the existence of
arbitrarily close regularized solutions; they do not assert convergence of a
canonical sequence of monopoles.

## 3. Triangle, finite-dimensional Cauchy--Schwarz, and conformal deficits

The mixed estimate is most cleanly obtained from the exact pointwise identity

\[
 27\left(\frac{s^2}{24}+2w^2\right)-(s-\sqrt6w)^2
 =\frac18(s+8\sqrt6w)^2.                                       \tag{18}
\]

To separately expose the triangle and finite-dimensional Cauchy--Schwarz
uses, let

\[
 x=\|s\|_2,\quad y=\|w\|_2,\quad z=\|s-\sqrt6w\|_2
\]

and define

\[
 D_{\rm tri}=(x+\sqrt6y)^2-z^2
 =2\sqrt6\left(xy+\int sw\right)\ge0,                           \tag{19}
\]

\[
 D_{\rm CS}=(x-8\sqrt6y)^2\ge0.                                \tag{20}
\]

The first is the squared triangle/angular deficit, while the second is the
two-dimensional Cauchy--Schwarz ratio deficit.  Direct expansion gives

\[
 \boxed{\int(s+8\sqrt6w)^2=D_{\rm CS}+8D_{\rm tri}.}             \tag{21}
\]

Thus neither algebraic step is hidden inside an unspecified \(o(1)\).

The conformal step used in the equality proof has a weaker quantitative
meaning.  Define

\[
 D_{\rm conf}(g)=E(g)-\inf_{\widehat g\in[g]}E(\widehat g),
 \qquad E(g)=\int(s_g-\sqrt6|W_+(g)|)^2d\mu_g.                  \tag{22}
\]

Middle-degree Hodge theory is conformally invariant, so (1) applies with the
same \(p\) throughout \([g]\).  Hence

\[
 0\le D_{\rm conf}(g)\le\Delta_a.                               \tag{23}
\]

This is only a value-gap estimate.  Without coercivity or a quantitative
Łojasiewicz/second-variation statement it gives no bound on the Euler--Lagrange
residual and no distance to a conformal minimizer.  Exact equality does imply
that \(s-\sqrt6w\) is constant by conformal variation, but near equality alone
does not.

For completeness, the older generalized-Yamabe chain can also be made
additive.  If \(\lambda_1(W_+)=w_{\min}\) and

\[
 G(g)=\int\left|\left(\frac23s+2w_{\min}\right)_-\right|^2,
\]

let \(g_\gamma\) be LeBrun's conformal minimizer.  Then

\[
 \frac49\Delta_a=
 \underbrace{\left(\frac49E-G(g)\right)}_{D_{\rm spectral}}
 +\underbrace{(G(g)-G(g_\gamma))}_{D_{\rm Yamabe}}
 +\underbrace{(G(g_\gamma)-32\pi^2p)}_{D_{\rm mono,old}}.       \tag{24}
\]

All three summands are nonnegative and individually at most
\(4\Delta_a/9\).  The modern rescaled proof above is stronger because it
also resolves the internal spinor and projection errors.

## 4. Exact-boundary control by the Ricci defect

For a metric with

\[
 \|g^{-1}(\operatorname{Ric}+g)\|_{L^\infty}=\delta<1,
\]

set

\[
 S=\frac1{4\pi^2}\int\frac{s^2}{24},\quad
 W=\frac1{4\pi^2}\int2w^2,\quad
 R=\frac1{4\pi^2}\int\frac{|\operatorname{Ric}^\circ|^2}{2},
 \quad I=S+W.
\]

Then

\[
 I-R=\frac{2A}{3},\qquad
 R\le\kappa S,\qquad \kappa=\frac{3\delta^2}{(1-\delta)^2}.     \tag{25}
\]

If \(\kappa<1\),

\[
 0\le R\le R_{\max}:=\frac{(2A/3)\kappa}{1-\kappa}.             \tag{26}
\]

Let the published sign classes be

\[
 a_\epsilon=\sum_j\epsilon_jc_j+\sum_\ell\epsilon_\ell E_\ell.
\]

Writing \(p_\epsilon=(a_\epsilon^+)^2\), sign averaging gives

\[
 \operatorname{Av}_\epsilon p_\epsilon=A+P_{\rm per},\qquad
 P_{\rm per}=\sum_j\|c_j^-\|_2^2+\sum_\ell\|E_\ell^+\|_2^2,
                                                                    \tag{27}
\]

and the mixed estimate gives

\[
 0\le P_{\rm per}\le\frac32R.                                  \tag{28}
\]

Put \(K=E/(72\pi^2)\).  Identity (18) implies

\[
 K\le\frac32I=A+\frac32R.                                      \tag{29}
\]

Choose a sign with \(p_\epsilon\ge\operatorname{Av}p\), hence
\(p_\epsilon\ge A\).  For this selected class,

\[
 \boxed{0\le\Delta_\epsilon=72\pi^2(K-p_\epsilon)
 \le108\pi^2R\le72\pi^2A\frac{\kappa}{1-\kappa}.}             \tag{30}
\]

Equations (13)--(17), (23), and (24) are therefore controlled by the total
boundary defect with the displayed constants.  Averaging instead over all
signs gives the equally useful statement

\[
 \boxed{
 \operatorname{Av}_\epsilon\Delta_\epsilon
 =72\pi^2(K-A-P_{\rm per})\le108\pi^2R.}                        \tag{31}
\]

For the algebraic steps, (18), (27), and \(K\ge A+P_{\rm per}\) give

\[
 \int(s+8\sqrt6w)^2
 \le864\pi^2\left(R-\frac23P_{\rm per}\right)
 \le864\pi^2R.                                                  \tag{32}
\]

Consequently

\[
 \boxed{D_{\rm CS}\le864\pi^2R,\qquad
 D_{\rm tri}\le108\pi^2R.}                                   \tag{33}
\]

In normalized energy variables, (33) is

\[
 \left(\sqrt S-2\sqrt2\sqrt W\right)^2\le9R.                  \tag{34}
\]

Together with \(S+W=2A/3+R\), this proves
\(S\to16A/27\), \(W\to2A/27\) whenever \(R/A\to0\).

The pointwise pinching also gives

\[
 \frac{96\pi^2S}{16(1+\delta)^2}
 \le\operatorname{Vol}(g)\le
 \frac{96\pi^2S}{16(1-\delta)^2},                              \tag{35}
\]

and hence \(\operatorname{Vol}(g)/A\to32\pi^2/9\).

Finally, let \(t=s+8\sqrt6w\).  Since

\[
 q-\frac92=\frac18t-\frac98(s+4),                              \tag{36}
\]

(32) and \(|s+4|\le4\delta\) imply

\[
 \left\|q-\frac92\right\|_2
 \le\frac{3\sqrt6}{2}\pi\sqrt R
      +\frac92\delta\sqrt{\operatorname{Vol}(g)}.              \tag{37}
\]

Thus (17) quantitatively forces the harmonic representative to have nearly
constant norm

\[
 |H_a|\approx c_0:=\frac{3}{4\sqrt2\pi}                         \tag{38}
\]

in \(L^2\), with an explicit error obtained by adding
\((6\sqrt2\pi)^{-1}\|q-9/2\|_2\) to (17) divided by \(2\pi\).

## 5. What uniform Sobolev or harmonic-radius assumptions add

The unconditional conclusions are (14)--(17) and (37): weighted spinor
amplitude, curvature, and harmonic representative are controlled in \(L^2\).
They do **not** imply a pointwise lower bound in dimension four.

If the scale-invariant Sobolev inequality

\[
 \|v\|_4^2\le C_S\left(\|dv\|_2^2+
 \operatorname{Vol}(g)^{-1/2}\|v\|_2^2\right)                  \tag{39}
\]

holds uniformly, (14), (15), and (37) upgrade
\(\rho\to\sqrt2\) from \(L^2\) to \(L^4\).  This is still not a
uniform lower bound: \(W^{1,2}\hookrightarrow L^4\) is critical in four
dimensions and permits small-capacity transition sets.

A clean nonvanishing criterion is the following.  Suppose the harmonic forms
\(H_i\) satisfy, for fixed \(\alpha,L,r_0,v>0\),

\[
 [H_i]_{C^\alpha}\le L,\qquad
 \operatorname{Vol}_{g_i}B_r(x)\ge vr^4\quad(0<r\le r_0),       \tag{40}
\]

and \(\||H_i|-c_0\|_2\to0\).  Then \(\inf|H_i|\ge c_0/2\) for all
large \(i\).  Indeed, a point with \(|H_i|<c_0/2\) would, on a ball of
radius

\[
 r_* =\min\{r_0,(c_0/(4L))^{1/\alpha}\},
\]

force \(\||H_i|-c_0\|_2^2\ge(c_0^2/16)vr_*^4\).

Conditions (40) follow, for example, from a uniform positive
\(C^{2,\alpha}\) harmonic radius and a diameter bound, by standard elliptic
estimates for harmonic forms.  To identify the first Chern class, one also
needs a uniform \(C^0\) upgrade of

\[
 \frac{f_i\varphi_i}{6\sqrt2\pi}+H_i\longrightarrow0.           \tag{41}
\]

If (40)--(41) hold, then \(-H_i\) is symplectic and its self-dual direction
is homotopic through nonzero self-dual forms to the spinor quadratic form.
The determinant-line argument in the equality proof then gives
\(c_1(M,-H_i)=a\).  A uniform harmonic-radius bound plus uniform elliptic
coefficient bounds for (2) is one sufficient way to obtain (41).  A Sobolev
bound alone is not.

There is a particularly transparent compactness theorem.

**Bounded-geometry exclusion theorem.**  Let \(M\) be a fixed
Ishida--LeBrun boundary manifold with \(m=2\) or \(3\), \(A>0\), and
\(D=A/3\).  There is no sequence \(g_i\) satisfying
\(\|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_\infty\to0\) for which, for
some \(\alpha\in(0,1)\),

\[
 \inf_i r_h^{,2,\alpha}(g_i)>0,
 \qquad \sup_i\operatorname{diam}(M,g_i)<\infty.                \tag{42}
\]

Here \(r_h^{2,\alpha}\) is the usual harmonic-coordinate radius with
uniform ellipticity and scaled \(C^{2,\alpha}\) coordinate bounds; thus (42)
contains the compactness hypothesis explicitly.  Cheeger compactness gives,
after diffeomorphisms and a subsequence, a \(C^{2,\beta}\) limit
\(g_\infty\) with \(\operatorname{Ric}(g_\infty)=-g_\infty\).  Chern--Gauss--Bonnet
then gives \(I(g_\infty)=2A/3\).  A sign class has
\((a^+)^2\ge A\), so equality holds in the mixed monopole estimate.  The
published equality theorem makes \(g_\infty\) almost-Kähler; because it is
Einstein it is Kähler--Einstein.  Equivalently, equality would give the
forbidden symplectic structure used in Ishida--LeBrun's strictness argument.
This contradicts the connected-sum topology.

## 6. All sign choices: the Walsh-polarization result

Let \(x_r\) denote the harmonic self-dual representatives of all signed
coordinates: the \(c_j^+\) and the \(E_\ell^+\).  Thus

\[
 H_\epsilon=\sum_r\epsilon_rx_r.
\]

Set

\[
 \mathcal L(x)=\frac{q(x)}{6\sqrt2\pi},\qquad
 \int\mathcal L^2=K.
\]

For each sign choose a regularized rescaled monopole as above.  Equations
(16)--(17) imply

\[
 \left\||H_\epsilon|-\mathcal L\right\|_2^2
 \le\frac{\Delta_\epsilon}{18\pi^2}+o(1).                      \tag{43}
\]

Averaging and using (31),

\[
 \operatorname{Av}_\epsilon
 \left\||H_\epsilon|-\mathcal L\right\|_2^2\le6R+o(1).         \tag{44}
\]

For arbitrary vectors in any inner-product space, Walsh polarization gives

\[
\begin{aligned}
 \operatorname{Av}_\epsilon|H_\epsilon|^2&=\sum_r|x_r|^2,\\
 \operatorname{Av}_\epsilon\epsilon_p\epsilon_q|H_\epsilon|^2
 &=2\langle x_p,x_q\rangle\quad(p\ne q).                       \tag{45}
\end{aligned}
\]

Since \(\|H_\epsilon\|_2^2=p_\epsilon\le K\), (44)--(45) yield the
quantitative, purely geometric conclusions

\[
 \boxed{
 \left\|\sum_r|x_r|^2-\mathcal L^2\right\|_{L^1}
 \le2\sqrt{6KR}+o(1),}                                         \tag{46}
\]

\[
 \boxed{
 \|\langle x_p,x_q\rangle\|_{L^1}
 \le\sqrt{6KR}+o(1)\quad(p\ne q).}                             \tag{47}
\]

Thus simultaneous near saturation forces **spatial orthogonality in
\(L^1\)**.  This conclusion uses no compactness and remains meaningful after
normalization when the topology varies.

It does not by itself force collinearity.  Collinearity comes from the Weyl
eigenline part of the equality proof and requires a spectral hypothesis.  For
example, suppose the lowest eigenvalue of \(W_+\) is simple with
\(\lambda_2-\lambda_1\ge\gamma>0\) and \(f\le F\).  If \(\Pi^\perp\) is
projection away from the lowest eigenline, (4), (13), and (31) give

\[
 \operatorname{Av}_\epsilon\|\Pi^\perp H_\epsilon\|_2^2
 \le 3R+\frac{F^2}{2\gamma}R+o(1).                              \tag{48}
\]

By Walsh averaging, the left side is
\(\sum_r\|\Pi^\perp x_r\|_2^2\).  Hence the coordinate forms are nearly
collinear with the same line.  Combining (47) and (48) shows that their scalar
coefficients along this line have pairwise products tending to zero in
\(L^1\): at almost every good point, at most one canonical summand can carry
the mass.  Equation (46) says that one of them must carry it.  This is exactly
the phase-separation alternative.

If the harmonic forms are precompact in \(C^0\), such phase separation is
impossible on connected \(M\): in the exact limit one harmonic form would
vanish on an open set, hence everywhere by unique continuation, while its
cohomology square is positive.  Without equicontinuity, the transition region
may shrink and no contradiction follows.

The number of sign vertices matters.  On a fixed manifold, nonnegative
average deficit tending to zero implies that every individual sign deficit
tends to zero.  If \(b_2(N)\) or the manifold varies, the cube size grows and
(31) controls only the average; a sparse set of bad signs can remain.  There
is no topology-uniform conclusion that *every* vertex saturates.

## 7. The exact equality chain after compactness

Once compactness supplies an actual equality monopole, (12)--(17) give a
closed self-dual form of nonzero constant length in the lowest Weyl
eigenline, with the two other eigenvalues equal and \(s+s^*<0\) constant.
Convex-hull equality then forces all active projected monopole classes to be
the same harmonic class, hence the same symplectic form and the same first
Chern class.

For clarity, the final Blair/Chern--Weil step is not an inequality hidden in
(12).  For the resulting saturated almost-Kähler form \(\omega\), the Blair
curvature is

\[
\begin{aligned}
 iF_B^+&=\frac{s+s^*}{8}\omega+W^+(\omega)^\perp,\\
 iF_B^-&=\frac{s-s^*}{8}\widehat\omega+\mathring\varrho,
\end{aligned}
\]

and convex alignment makes \(F_B\) harmonic and cohomologous to a multiple
of \(\omega\), so \(F_B^-=0\).  Define

\[
 D_{\rm Ric,J}=\int\left(|\operatorname{Ric}^\circ|^2-
 \frac{(s^*-s)^2}{16}\right)\ge0.
\]

Chern--Gauss--Bonnet and Chern--Weil then give the exact identity

\[
 \int s^*(s^*-s)=4D_{\rm Ric,J}.                                \tag{49}
\]

But saturation implies \(s^*<0\), while
\(s^*-s=|\nabla\omega|^2\ge0\).  The two sides of (49) have opposite signs,
so both vanish: \(\nabla\omega=0\) and
\(\operatorname{Ric}^\circ=0\).  This proves negative
Kähler--Einstein rigidity.

Before a genuine nonvanishing almost-Kähler form has been produced, the
Blair connection and \(D_{\rm Ric,J}\) are not defined.  Therefore the
scalar--Weyl deficit alone does not quantitatively control this final stage.
Claiming otherwise would hide precisely the compactness problem under study.

## 8. Sharp theorem/degeneration dichotomy

The strongest unconditional statement is (30)--(37) and (43)--(47): a
selected sign, and the cube on average, have all analytic proof deficits of
order \(A\delta^2\); the curvature is close to its harmonic projection; the
spinor amplitude is nearly constant in weighted \(L^2\); and the harmonic
sign sums are spatially almost orthogonal.

The bounded-geometry exclusion theorem above shows that a boundary sequence
cannot remain in a compact part of metric space.  Equivalently, every
hypothetical sequence must violate (42): after every subsequence, either

\[
 \inf_M r_h^{2,\alpha}(g_i)\longrightarrow0
 \quad\text{or}\quad
 \operatorname{diam}(M,g_i)\longrightarrow\infty,               \tag{50}
\]

for every proposed pair of uniform bounds.  At the level of monopole forms,
it must also defeat at least one of the explicit upgrades above: uniform
Hölder control/noncollapse, a uniform lowest-eigenline gap, or elliptic
\(C^0\) control of (41).  This leaves a counterexample-compatible mechanism:
canonical harmonic forms localize on different regions, while their
transition/topology-carrying region has collapsing harmonic radius, Weyl
concentration/eigenvalue degeneracy, or escapes down a long end.  The standard
scalar-flat ASD gluing neck cannot realize \(\delta\to0\), and a smooth
noncollapsed blow-up is Ricci-flat, but those facts do not exclude anisotropic
collapse or cusp-like escape.

This is a genuine dichotomy with no implicit compactness assumption: compact
bounded geometry gives a forbidden Kähler--Einstein limit; otherwise (50)
and/or failure of the explicitly listed analytic controls is necessary.

## 9. Audit of `step3_boundary_near_saturation.tex`

The following constants and conclusions are correct:

* \(R\le3\delta^2(1-\delta)^{-2}S\) and (26);
* the period average (27)--(28);
* the completion coefficient \(864\pi^2\);
* \(S\to16A/27\), \(W\to2A/27\),
  \(\operatorname{Vol}/A\to32\pi^2/9\);
* \(\int w^2/(\pi^2A)\to4/27\),
  \(\int|\operatorname{Ric}^\circ|^2/(\pi^2A)\to0\), and
  \(\int|\operatorname{Ric}|^2/(\pi^2A)\to128/9\);
* under the extra hypotheses of Ishida--LeBrun's exact \(\mathcal I_r\)
  theorem, \(\mathcal I_r=32\pi^2A/3\) at \(D=A/3\).

Three qualifications are mathematically necessary.

1. “Every fixed sign vertex saturates” is valid for a fixed manifold (a
   fixed finite cube).  It is not uniform when the topology and cube dimension
   vary.  Only the average statement (31), or a selected maximizing sign
   (30), is uniform.
2. “The period plane asymptotically contains every canonical direction” is
   literally true on a fixed manifold.  For varying \(A\), (28) gives only
   normalized angle control; an absolute norm need not tend to zero.
3. The sentence that *every inequality in the equality chain* is saturated
   should be restricted to the analytic deficits for a selected sign or on
   average.  The Blair/Chern--Weil stage is unavailable until compactness has
   produced an actual nonvanishing almost-Kähler form.

Also, when topology varies, “volume cannot escape” should be read as the
normalized statement \(\operatorname{Vol}/A\to32\pi^2/9\); the unnormalized
volume may diverge with \(A\).

The symbolic identities and normalizations in this note are checked by
`Sessions/S0910A03/workspace/codex_loop/work/verify_deficit_constants.py`.
