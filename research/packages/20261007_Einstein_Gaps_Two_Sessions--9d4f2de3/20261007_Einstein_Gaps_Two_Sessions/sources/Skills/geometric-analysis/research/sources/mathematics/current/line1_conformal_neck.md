# A conformal-neck counterexample to scalar stability without connectivity

23 September 2026. This note proves a concrete limitation of the first-line
functional-stability program. It first records a valid Ricci/connection
bridge, then constructs metrics for which every energy on its right tends
to zero while scalar variance and relative Einstein defect do not. All
inputs are classical. No literature-priority claim is made.

The example stays on one fixed smooth manifold which already admits
negative Einstein metrics. It is not a counterexample to Yau26.

## 1. The valid non-Kähler bridge, and the missing conclusion

Use the curvature conventions of [Round 17](round17_integral.md) and the
[scalar-band note](line1_scalar_band_remainder.md). Let an actual ordinary
Seiberg–Witten solution have real determinant curvature \(\mathcal F\), with
\([\mathcal F/(2\pi)]=a\). Write

\[
 p=(a_g^+)^2>0,\quad T=2\chi+3\tau,\quad
 P=\int|\operatorname{Ric}^{\circ}|^2,\quad
 B_p=\int s^2-32\pi^2p,
\]
\[
 D=\frac1{4\pi^2}\int\left(\frac{s^2}{24}
                +\frac{|W^+|^2}{2}\right)-\frac p2.
\]

Ordinary SW gives \(B_p\ge0\). Indeed, with \(\rho=|\Phi|^2\), the exact
Round-17 identity refines to

\[
 \boxed{B_p=\|s+\rho\|_2^2+8\|\nabla_A\Phi\|_2^2
 +8\left(\|\mathcal F^-\|_2^2-4\pi^2(p-a^2)\right).}
 \tag{1}
\]

The last parenthesis is nonnegative by Hodge orthogonality. If
\(\mathcal F_H\) is the harmonic representative of \(2\pi a\), exactness of
\(\mathcal F-\mathcal F_H\) equates the squared norms of its two Hodge
components, so (1) also proves

\[
 \|\mathcal F-\mathcal F_H\|_2^2\le B_p/4,
 \qquad \|\nabla_A\Phi\|_2^2\le B_p/8.
 \tag{2}
\]

These are controls of actual determinant curvature and an actual spinor,
not a formal cohomology substitution. They do not assert control of the
connection one-form modulo gauge without an additional elliptic estimate.

Chern–Weil gives the exact non-Kähler identity

\[
 \boxed{P+\frac{B_p}{4}
 =8\pi^2\bigl((p-a^2)+(a^2-T)\bigr)+32\pi^2D.}
 \tag{3}
\]

Consequently small LB defect, small period excess, and small topological
cost really do bound trace-free Ricci energy. If \(a^2\ge T\), all three
terms on the right are nonnegative. This elementary classical consequence
does not, however, bound scalar variance.

There is even a scalar-band estimate for \(B_p\), independent of any
Poincaré constant. Assume \(-S\le s\le-s_0<0\), and the conformal-class SW
solvability used in the scalar-band note. Put \(w=\sqrt6|W^+|\) and
\(t=s+2w\). Its retained defect split gives
\(\int t^2\le288\pi^2D\). Direct algebra gives

\[
 B_p=64\pi^2D+\frac23\int st-\frac13\int t^2,
\]
\[
 \boxed{0\le B_p\le64\pi^2D+8\sqrt2\pi S\sqrt{VD}.}
 \tag{4}
\]

Thus a fixed scalar band and \(D/V\to0\) also control the normalized
energies in (1)–(2). The following example satisfies stronger hypotheses:
\(p=a^2=T\) exactly, and its ordinary scalar defect tends to zero. Scalar
variance nevertheless remains positive.

## 2. Fixed smooth topology and a separating hyperbolic collar

Fix integers \(g_-,g_+\ge1\), \(g=g_-+g_+\), and \(h\ge2\). Set

\[
 M=\Sigma_g\times\Sigma_h,
 \qquad A=8(g-1)(h-1)=2\chi(M)+3\tau(M)>0.
\]

Choose a separating curve in \(\Sigma_g\) whose two sides have genera
\(g_-\) and \(g_+\). Hyperbolic pairs of pants, equivalently
Fenchel–Nielsen coordinates, give curvature \(-1\) metrics \(b_\ell\) on
this fixed marked surface for which this curve is a geodesic of length
\(\ell\downarrow0\). Fix a curvature \(-1\) metric \(h_F\) on \(\Sigma_h\),
and put

\[
 g_\ell=b_\ell\oplus h_F.
\]

Then \(\operatorname{Ric}_{g_\ell}=-g_\ell\), \(s_{g_\ell}=-4\), and

\[
 V_0=\operatorname{Vol}(g_\ell)
 =16\pi^2(g-1)(h-1)=2\pi^2A.
 \tag{5}
\]

The separating geodesic has an embedded collar

\[
 (-w_\ell,w_\ell)\times(\mathbb R/\mathbb Z),\qquad
 b_\ell=dt^2+\ell^2\cosh^2t\,d\theta^2,
 \quad w_\ell=\operatorname{arsinh}\frac1{\sinh(\ell/2)}\to\infty.
 \tag{6}
\]

This is the classical collar lemma; a primary research reference recalling
it is [Rupflin–Topping, Appendix A, Lemma A.1](https://arxiv.org/pdf/1605.06691).
Only (6), not a convergence theorem for moduli spaces, is needed below.

Cutting at \(t=0\) gives geodesic-boundary hyperbolic surfaces of areas
\(2\pi(2g_\pm-1)\), by Gauss–Bonnet. The corresponding product-side volumes
are therefore exactly

\[
 V_\pm=8\pi^2(2g_\pm-1)(h-1)>0,\qquad V_-+V_+=V_0.
 \tag{7}
\]

## 3. A fixed-width transition and a uniform negative scalar band

Fix unequal positive constants \(c_-,c_+\). Choose a smooth function
\(f:\mathbb R\to\mathbb R\) which equals \(\log c_-\) for \(t\le-R\)
and \(\log c_+\) for \(t\ge R\), and is constant on neighborhoods of those
end intervals. Here \(R<\infty\) is fixed. It can be chosen large enough
that

\[
 6\bigl(\|f''\|_\infty+\|f'\|_\infty+\|f'\|_\infty^2\bigr)\le2.
 \tag{8}
\]

Alternatively fix \(R\) first and choose \(\log(c_+/c_-)\ne0\) sufficiently
small. For \(w_\ell>R\), extend \(f(t)\) to the two complementary sides by
its respective constants; call the resulting smooth function \(f_\ell\)
on \(M\), constant in the fiber direction. Set

\[
 \widehat g_\ell=e^{2f_\ell}g_\ell.
 \tag{9}
\]

Use the Laplacian \(\Delta=\operatorname{div}\nabla\), with nonpositive
spectrum. On the transition region,

\[
 |df_\ell|^2=(f')^2,\qquad
 \Delta f_\ell=f''+\tanh(t)f',\qquad
 \widehat s_\ell=e^{-2f_\ell}
       \left[-4-6\bigl(\Delta f_\ell+|df_\ell|^2\bigr)\right].
 \tag{10}
\]

Writing \(f_{\min},f_{\max}\) for the fixed extrema, (8) implies

\[
 -6e^{-2f_{\min}}\le\widehat s_\ell
 \le-2e^{-2f_{\max}}<0.
 \tag{11}
\]

The support of the derivatives lies in
\(N_\ell=[-R,R]\times S^1\times\Sigma_h\), whose unscaled volume is

\[
 \operatorname{Vol}_{g_\ell}(N_\ell)
 =2\ell\sinh R\,\operatorname{Area}(h_F)=O(\ell).
 \tag{12}
\]

All derivatives of \(f_\ell\) of each fixed order are uniformly bounded:
in the collar frame the coefficients are built from bounded derivatives
of \(\tanh t\) and the fixed function \(f\). Hence the full curvature and
each fixed covariant derivative of curvature of \(\widehat g_\ell\) are
uniformly bounded as well. Volumes are bounded above and away from zero.
Injectivity radius and global connectivity are not uniformly controlled.

## 4. Actual monopole class, exact periods, and exact energy identities

The product almost-complex structures determined by the two oriented
surface metrics are homotopic as \(\ell\) varies. Choose the canonical or
conjugate canonical Spin\(^c\) structure, and write \(a=\pm c_1(K_M)\) for
its real first Chern class. This is one fixed class and one fixed Spin\(^c\)
structure. It has nonzero ordinary SW invariant; \(b_+(M)=1+2gh>1\), so
there is no chamber issue. Thus its unperturbed equations have solutions
for all the metrics in (9), and for every metric conformal to each of them.
The classical Kähler nonvanishing input is recorded in
[LeBrun, Theorem 2](https://arxiv.org/pdf/dg-ga/9412006).

The Kähler form \(\omega_\ell\) of \(g_\ell\) satisfies
\([\omega_\ell]=2\pi c_1(K_M)\). Hodge star on two-forms is unchanged under
the conformal change (9); a closed self-dual form is harmonic for either
metric. Consequently

\[
 \boxed{p_\ell=(a_{\widehat g_\ell}^+)^2=a^2=A=T\quad\text{for every }\ell.}
 \tag{13}
\]

Set

\[
 B_\ell=\int\widehat s_\ell^2\,d\widehat\mu_\ell-32\pi^2A,
 \qquad z_\ell=\Delta f_\ell+|df_\ell|^2.
\]

The conformal factors cancel in the scalar-square integral. Since the
manifold is closed, \(\int\Delta f_\ell=0\), and (10) gives the exact formula

\[
 \boxed{B_\ell=48\int|df_\ell|^2\,d\mu_{g_\ell}
                   +36\int z_\ell^2\,d\mu_{g_\ell}>0.}
 \tag{14}
\]

The strict inequality holds because \(c_-\ne c_+\). By (12),
\(B_\ell=O(\ell)\to0\). This is the ordinary SW scalar defect from
Round 17, not a new weighted defect.

The Weyl-square integral is conformally invariant in dimension four, and
the starting Kähler–Einstein product has
\(\int|W^+|^2=2V_0/3\). Hence the LB defect satisfies the exact identity

\[
 \boxed{D_\ell=\frac{B_\ell}{96\pi^2}\longrightarrow0.}
 \tag{15}
\]

Subtract the Chern–Weil formula for \(g_\ell\) from that for
\(\widehat g_\ell\), keeping this Weyl integral fixed. It gives

\[
 \boxed{P_\ell=\int|\operatorname{Ric}^{\circ}_{\widehat g_\ell}|^2
       =\frac{B_\ell}{12}=8\pi^2D_\ell\longrightarrow0,}
 \tag{16}
\]
\[
 \boxed{R_{2,\ell}=8\pi^2 A+\frac{B_\ell}{3}
                    =8\pi^2 A+32\pi^2D_\ell.}
 \tag{17}
\]

These metrics also approach the absolute Ricci-energy infimum on this
minimal general-type smooth manifold, by
[LeBrun, Theorem 4.3](https://arxiv.org/pdf/math/0003068).

They are genuinely non-Kähler, not merely non-Kähler for the displayed
complex structure. If \(\widehat g_\ell\) were Kähler in the given
orientation, \(|W^+|^2=\widehat s_\ell^2/24\) would force \(B_\ell=0\),
contradicting (14). The same argument applies in the other orientation:
the starting product is Kähler for either orientation and has the same
\(W^-\)-energy. Thus \(\widehat g_\ell\) is not Kähler for either orientation,
although it is conformally Kähler for both.

## 5. The scalar variance and relative defect have positive limits

Define constants

\[
 H_0=V_-+V_+,\qquad H_2=V_-c_-^2+V_+c_+^2,\qquad
 H_4=V_-c_-^4+V_+c_+^4.
 \tag{18}
\]

Outside \(N_\ell\), the scalar is exactly \(-4c_\pm^{-2}\) and the volume
form is \(c_\pm^4d\mu_{g_\ell}\). The transition region has volume
\(O(\ell)\), uniformly bounded scalar, and bounded conformal factor.
Using (7) gives

\[
 \widehat V_\ell\to H_4,\qquad
 \int\widehat s_\ell\,d\widehat\mu_\ell\to-4H_2,\qquad
 \int\widehat s_\ell^2\,d\widehat\mu_\ell\to16H_0.
 \tag{19}
\]

Therefore, with \(L_\ell=\int(\widehat s_\ell-\overline{\widehat s}_\ell)^2\),

\[
 \boxed{L_\ell\longrightarrow
 16\left(H_0-\frac{H_2^2}{H_4}\right)
 =\frac{16V_-V_+(c_-^2-c_+^2)^2}{H_4}>0.}
 \tag{20}
\]

Minimization over nonzero constant Einstein factors gives, as in
[Round 21](round21_comparison.md),

\[
 \mathcal E(\widehat g_\ell)
 =\frac{4P_\ell+L_\ell}{R_{2,\ell}}
 \longrightarrow
 \boxed{4\left[1-
 \frac{(V_-c_-^2+V_+c_+^2)^2}
 {(V_-c_-^4+V_+c_+^4)(V_-+V_+)}\right]}>0.
 \tag{21}
\]

For instance, take \(g_-=g_+=1\), \(h=2\), \(c_-=1\), and
\(c_+=\sqrt2\). The two side volumes are equal and the limiting relative
defect is exactly \(2/5\). A sufficiently wide but fixed transition gives
the negative scalar band (11).

The example can also be globally rescaled to mean scalar \(-4\). Indeed
\(\kappa_\ell=-\overline{\widehat s}_\ell/4\to H_2/H_4>0\), and the metric
\(\kappa_\ell\widehat g_\ell\) has that mean scalar. All energies in
(13)–(21) are unchanged by this constant rescaling; the scalar band remains
uniform. With the mean normalization, the averaged Einstein residual obeys

\[
 \frac{\int|\operatorname{Ric}+\kappa_\ell\widehat g_\ell|^2}
      {\kappa_\ell^2\widehat V_\ell}
 \longrightarrow4\left(\frac{H_0H_4}{H_2^2}-1\right)>0.
 \tag{22}
\]

Thus the failure is not removed by fixing the mean scalar or the volume
scale. The missing information concerns communication between the two
bulk regions.

## 6. The first eigenvalue and the actual SW amplitude

Use \(f_\ell\), after subtracting its \(\widehat g_\ell\)-mean, as a scalar
Rayleigh test. Its Dirichlet energy is

\[
 \int|df_\ell|_{\widehat g_\ell}^2d\widehat\mu_\ell
 =\int e^{2f_\ell}|df_\ell|_{g_\ell}^2d\mu_{g_\ell}=O(\ell),
\]

whereas its variance has a positive limit because its two bulk constants
are unequal. Hence

\[
 \lambda_1(\widehat g_\ell)=O(\ell)\longrightarrow0.
 \tag{23}
\]

There is no conflict with actual SW control. Since \(p=a^2\), the right
side of the ordinary identity (1) is precisely \(B_\ell\to0\). Any ordinary
solution satisfies
\(\|\widehat s_\ell+|\Phi_\ell|^2\|_2\to0\) and
\(\|\nabla_{A_\ell}\Phi_\ell\|_2\to0\), while its amplitude follows the
two different bulk scalar values. Small gradient energy does not force a
single global amplitude across this degenerating bottleneck.

Likewise, the harmonic representative of the canonical class is the same
differential form \(\pm\omega_\ell/(2\pi)\) before and after (9). Its
pointwise norm after conformal scaling is
\(\sqrt2 e^{-2f_\ell}/(2\pi)\), with two different bulk limits, even though
its squared \(L^2\) norm remains exactly \(p=A\). Primitive-class control
fixes a cohomological norm; it does not fix the pointwise amplitude.

## 7. Optional stronger variant: pointwise trace-free Ricci tends to zero

The fixed-window proof already suffices. One may also let
\(R_\ell=\tfrac12\log(1/\ell)\to\infty\), and choose

\[
 f_\ell(t)=\log c_-+
 \log(c_+/c_-)\,\chi(t/R_\ell),
\]

where \(\chi\) is a fixed smooth step equal to zero for inputs at most
\(-1\) and one for inputs at least \(1\). For small \(\ell\), this fits
inside (6). Its transition volume is \(O(\ell e^{R_\ell})=O(\sqrt\ell)\),
and

\[
 \|df_\ell\|_\infty=O(R_\ell^{-1}),\qquad
 \|\nabla^2f_\ell\|_\infty=O(R_\ell^{-1}).
\]

For the Hessian, the collar eigenvalues are \(f''\), \(\tanh(t)f'\), and
two zeros. The conformal trace-free Ricci formula is

\[
 \operatorname{Ric}^{\circ}_{\widehat g_\ell}
 =-2\bigl(\nabla^2f_\ell-df_\ell\otimes df_\ell\bigr)_0.
 \tag{24}
\]

The trace-free operation may be taken with \(g_\ell\), since it is
unchanged under conformal scaling of the metric. The conformal factors
are uniformly bounded above and below, so
\(\|\operatorname{Ric}^{\circ}_{\widehat g_\ell}\|_\infty=O(R_\ell^{-1})\to0\).
The scalar band holds for all sufficiently small \(\ell\). Formula (14)
gives \(B_\ell=O(\sqrt\ell/R_\ell^2)\to0\), and all limits (19)–(22)
remain unchanged. Thus even pointwise convergence of the trace-free Ricci
tensor to zero does not produce one global Einstein factor here.

## 8. Precise consequence and non-consequence

This disproves a uniform estimate tending to zero for scalar variance or
relative Einstein defect based only on LB defect, ordinary SW scalar
defect, period excess, topological cost, a fixed negative scalar band,
bounded volume, and even uniform local curvature bounds. All those inputs
have the required uniform bounds or vanish along this fixed-topology
sequence. A scalar spectral gap or another genuinely global connectivity
hypothesis cannot simply be deleted from the scalar-band stability theorem.

It does not disprove the valid Ricci/connection bridge (1)–(4), the
classical exact equality theorem, or stability under stronger compactness
conditions. Nor is it a Yau26 counterexample: each \(M\) here admits the
original product Einstein metric. Finally, the construction is an explicit
application of classical conformal and hyperbolic geometry; no assertion
is made that this mechanism or its mathematical conclusion is new in the
literature.
