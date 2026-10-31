# Kähler controls for LeBrun equality, Ricci energy, and Einstein defect

This note supplies exact tests for the corrected first scientific line. The
identities below are elementary consequences of classical Kähler geometry,
Hodge theory, and Chern–Weil theory; no priority is claimed. They identify a
missing hypothesis in an Einstein-stability assertion, not a new solution of
Yau26. In particular, closeness of an integral residual does not by itself
give pointwise Ricci pinching, metric compactness, or an exact Einstein metric
on the same smooth manifold.

## 1. Definitions and the exact Kähler decomposition

Let \((M^4,J,g,\omega)\) be a closed connected Kähler surface, with its complex
orientation. Use real Riemannian tensor norms, \(|\omega|^2=2\), and the Weyl
endomorphism norm for which \(|W^+|^2=s^2/24\). Set

\[
 a=c_1(K_M),\quad A=a^2=2\chi(M)+3\tau(M),\quad
 p=(a_g^+)^2,\quad V=\operatorname{Vol}(g),\quad
 \bar s=V^{-1}\int_M s\,d\mu,
\]
\[
 L=\int_M(s-\bar s)^2\,d\mu,\qquad
 P=\int_M|\operatorname{Ric}^{\circ}|^2\,d\mu,\qquad
 R_2=\int_M|\operatorname{Ric}|^2\,d\mu.
\]

Here \(a_g^\pm\) denote harmonic representatives of the two Hodge projections;
the square in \(p\) is the intersection square. Define the LeBrun remainder

\[
 D=\frac1{4\pi^2}\int_M
       \left(\frac{s^2}{24}+\frac12|W^+|^2\right)d\mu-\frac p2.
 \tag{1}
\]

Changing \(a\) to \(-a=c_1(M)\) does not change any formula here. Whenever
LeBrun's polarized monopole hypotheses apply to this canonical pair, this
is his Proposition 4.1 remainder. Its equality set is constant-scalar
Kähler, not just Kähler–Einstein. His Proposition 4.2 and equation (17)
give the associated Ricci-energy identity. These are classical inputs.
[LeBrun, arXiv:math/0003068v1, Propositions 4.1–4.2](https://arxiv.org/pdf/math/0003068).

For every Kähler metric as above, without needing a monopole argument,

\[
 \boxed{
 p=\frac{(a\cdot[\omega])^2}{[\omega]^2}
   =\frac{\bar s^2V}{32\pi^2},\qquad
 p-A=\|a_g^-\|_{L^2}^2\ge0,\qquad
 D=\frac{L}{64\pi^2}.}
 \tag{2}
\]
\[
 \boxed{
 P=8\pi^2(p-A)+\frac L4
   =8\pi^2(p-A)+16\pi^2D,}
 \tag{3}
\]
\[
 \boxed{
 R_2=8\pi^2(2p-A)+\frac L2
    =8\pi^2(2p-A)+32\pi^2D.}
 \tag{4}
\]

### Proof, including the primitive component

The Ricci form \(\rho\) represents \(-2\pi a\), and

\[
 \rho=\frac{s}{4}\omega+\rho_0,
 \qquad *\rho_0=-\rho_0,
 \qquad |\operatorname{Ric}^{\circ}|^2=2|\rho_0|^2.
 \tag{5}
\]

Since \(a\) has type \((1,1)\), its harmonic self-dual component is a multiple
of \(\omega\); its other component is primitive and anti-self-dual. Also
\([\omega]^2=2V\) and
\(\int s\,d\mu=2\int\rho\wedge\omega=-4\pi a\cdot[\omega]\).
This proves the first two identities in (2).

The harmonic representative of \([\rho]\) is

\[
 \rho_H=\frac{\bar s}{4}\omega+\eta,
 \qquad \eta=-2\pi a_g^-.
\]

Write \(\zeta=\rho-\rho_H\). It is exact, so
\(\int\zeta\wedge\zeta=0\), and its two Hodge components have equal squared
\(L^2\) norms. Its self-dual component is
\(\zeta^+=(s-\bar s)\omega/4\), giving

\[
 \|\zeta^-\|_2^2=\|\zeta^+\|_2^2=L/8.
\]

The harmonic form \(\eta\) is orthogonal to the exact form \(\zeta\), and
therefore to \(\zeta^-\). Consequently

\[
 \int|\rho_0|^2=\|\eta+\zeta^-\|_2^2
 =4\pi^2(p-A)+L/8.
\]

Equation (5) proves (3). The Kähler Weyl identity turns (1) into
\(D=\int s^2/(64\pi^2)-p/2=L/(64\pi^2)\). Finally,
\(R_2=P+\int s^2/4\) proves (4).

A separate Chern–Weil check is

\[
 4\pi^2 A=\int\left(2|W^+|^2+\frac{s^2}{24}-\frac12
 |\operatorname{Ric}^{\circ}|^2\right)
 =\frac18\int s^2-\frac P2.
 \tag{6}
\]

Thus \(P=\int s^2/4-8\pi^2A\), consistently with (3).

## 2. A sharp extra condition for integral Einstein stability

Assume \(\bar s<0\), and choose the mean-scalar normalization
\(\kappa=-\bar s/4>0\). Let

\[
 Q_\kappa=\int|\operatorname{Ric}+\kappa g|^2.
\]

Orthogonality of trace and trace-free parts gives the exact identities

\[
 \boxed{Q_\kappa=P+\frac L4
 =8\pi^2(p-A)+32\pi^2D,\qquad
 \kappa^2 V=2\pi^2p.}
 \tag{7}
\]

The relative Einstein defect used in the earlier rounds is

\[
 \mathcal E(g)=\inf_{\lambda\ne0}
 \frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2 V}.
\]

Minimizing this quadratic in \(1/\lambda\), with
\(S=\int s<0\), gives \(\lambda=R_2/S\), and hence

\[
 \mathcal E=4-\frac{S^2}{V R_2}
 =\frac{4P+L}{R_2}=\frac{4Q_\kappa}{R_2}
 =\boxed{\frac{4\bigl((p-A)+4D\bigr)}{2p-A+4D}}.
 \tag{8}
\]

The optimizer of this relative functional need not equal \(-\kappa\);
\(-\kappa\) instead minimizes the unnormalized squared residual.

In particular, putting
\(\theta=((p-A)+4D)/p\ge0\), one has

\[
 \frac{Q_\kappa}{\kappa^2V}=4\theta,
 \qquad \mathcal E=\frac{4\theta}{1+\theta}.
 \tag{9}
\]

Thus a sequence of negative-mean Kähler metrics has
\(\mathcal E\to0\) if and only if both

\[
 \frac{p-A}{p}\longrightarrow0,
 \qquad \frac{D}{p}\longrightarrow0.
 \tag{10}
\]

This is an exact integral statement. The extra condition measures the
harmonic primitive canonical component and cannot be dropped.

When \(A>0\), the first condition is equivalently normalized-volume
saturation:

\[
 \frac{\kappa^2V}{2\pi^2 A}=\frac pA\longrightarrow1.
 \tag{11}
\]

At the exact canonical ray \([\omega]=t a\), \(t>0\), one has \(p=A\), and

\[
 P=16\pi^2D,\quad Q_\kappa=32\pi^2D,\quad
 \mathcal E=\frac{16D}{A+4D}.
 \tag{12}
\]

Conversely, under \(\bar s<0\), equality \(p=A\) forces this ray condition,
by (2). Therefore \(D=0\) together with \(p=A\) is equivalent to negative
Kähler–Einstein. Requiring only \(D=0\) gives merely negative cscK.

All of \(P,L,R_2,Q_\kappa,p,D\) are unchanged by constant rescaling in four
dimensions, with \(\kappa\) rescaled accordingly. An averaged curvature
error must be divided by \(\kappa^2\): the dimensionless quantity is
\(Q_\kappa/(\kappa^2V)\), not \(Q_\kappa/V\). Pointwise normalized Ricci
control implies this average control, since

\[
 \frac{Q_\kappa}{\kappa^2V}
 \le4\left(\frac{\|g^{-1}\operatorname{Ric}+\kappa I\|_{\infty,\mathrm{op}}}
 {\kappa}\right)^2.
 \tag{13}
\]

There is no converse in this note without additional regularity hypotheses.

## 3. Unequal negative products: exact failure of a Ricci remainder

Fix closed hyperbolic surfaces of genera \(r,s\ge2\), with curvature \(-1\)
metrics \(h_1,h_2\). For \(\alpha,\beta>0\), put

\[
 g_{\alpha,\beta}=\alpha^{-1}h_1\oplus\beta^{-1}h_2,
 \qquad m=(r-1)(s-1),\qquad A=8m.
\]

These are metrics on one fixed smooth product, with

\[
 V=\frac{16\pi^2m}{\alpha\beta},\quad
 s=-2(\alpha+\beta),\quad
 |\operatorname{Ric}^{\circ}|^2=(\alpha-\beta)^2,\quad D=L=0,
\]
\[
 p=A\frac{(\alpha+\beta)^2}{4\alpha\beta},\qquad
 p-A=A\frac{(\alpha-\beta)^2}{4\alpha\beta},\qquad
 \mathcal E=\frac{2(\alpha-\beta)^2}{\alpha^2+\beta^2}.
 \tag{14}
\]

To fix the scalar scale, take \(\alpha=1+t\), \(\beta=1-t\), \(0<t<1\).
Then \(s=-4\), \(\kappa=1\), and

\[
 p=\frac A{1-t^2},\qquad
 V=\frac{2\pi^2 A}{1-t^2},\qquad
 \|g^{-1}\operatorname{Ric}+I\|_{\infty,\mathrm{op}}=t,
 \qquad \mathcal E=\frac{4t^2}{1+t^2}>0.
 \tag{15}
\]

Every such metric is locally symmetric: \(\nabla\operatorname{Rm}=0\), and
its Kähler form is parallel. Its self-dual Weyl spectrum is exactly
\((-2/3,1/3,1/3)\), independent of \(t\). Thus exact LB equality,
constant scalar curvature, a parallel Kähler form, and the exact Kähler
Weyl profile all coexist with nonzero Einstein defect. Fixing any
\(t\in(0,1)\) already refutes every proposed estimate
\(D\ge c\int|\operatorname{Ric}^{\circ}|^2\), \(c>0\), even on this one
nondegenerate smooth metric.

For a different normalization, take \(\alpha=u\), \(\beta=u^{-1}\).
The volume is fixed, while
\(P=16\pi^2m(u-u^{-1})^2\to\infty\) and \(D=0\). This version does not have
a fixed scalar scale or a uniform full-curvature bound. Neither version
is a counterexample to Yau26: the same smooth product also admits its
equal-curvature Einstein metric.

## 4. Minimal Kähler surfaces: sharp energy comparisons

Suppose \(M=X\) is a minimal complex surface of general type, and write
\(A=c_1^2(X)>0\). LeBrun's Theorem 4.3 identifies the absolute Ricci-energy
infimum over all smooth metrics as \(8\pi^2 A\).
[LeBrun, Theorem 4.3](https://arxiv.org/pdf/math/0003068).
For a Kähler metric of negative mean scalar curvature, define

\[
 \Delta=R_2-8\pi^2 A
       =16\pi^2(p-A)+32\pi^2D.
 \tag{16}
\]

Equations (7) and (16) imply

\[
 \boxed{Q_\kappa\le\Delta\le2Q_\kappa,\qquad
 \frac{2\Delta}{R_2}\le\mathcal E\le\frac{4\Delta}{R_2}.}
 \tag{17}
\]

Both constants are sharp. Unequal negative products have \(D=0\) and
\(\Delta=2Q_\kappa\). A small Kähler-potential perturbation of a negative
Kähler–Einstein metric, within its canonical Kähler class and with
nonconstant scalar curvature, has \(p=A\), \(D>0\), and
\(\Delta=Q_\kappa\). Such perturbations exist: a smooth potential outside
the kernel of the scalar-curvature linearization changes scalar curvature
nontrivially, and sufficiently small perturbations preserve positivity.

Thus in this particular minimal Kähler category, approaching the absolute
Ricci-energy infimum does force vanishing relative integral Einstein
defect. It does not establish pointwise or geometric stability.

## 5. Blow-ups: actual minimizing sequences with a positive limiting defect

Let \(X\) be a minimal complex surface of general type and
\(\pi:M\to X\) the complex blow-up at \(k\) distinct points. Write

\[
 A_0=c_1^2(X)>0,\qquad a=c_1(K_M),\qquad
 T=a^2=A_0-k,\qquad
 \Delta=R_2-8\pi^2(A_0+k).
\]

Only actual complex blow-ups are considered here; no Kähler construction
on an additional \(S^1\times S^3\) connected sum is asserted.

For every Kähler class \(\Omega\) on \(M\), put \(u=\pi^*c_1(K_X)\).
The minimal canonical class is nef and big, so \(u\cdot\Omega>0\),
\(u^2=A_0\), and Hodge index gives
\((u\cdot\Omega)^2\ge A_0\Omega^2\). Since
\(a=u+\sum E_i\) and each effective exceptional divisor has
\(E_i\cdot\Omega>0\), one obtains \(a\cdot\Omega>0\) and

\[
 p=\frac{(a\cdot\Omega)^2}{\Omega^2}\ge A_0,
 \qquad \bar s<0.
 \tag{18}
\]

The inequality is strict when \(k>0\). Substituting \(A=T=A_0-k\) in
(3)–(4) yields

\[
 \boxed{\Delta=16\pi^2(p-A_0)+\frac L2
                   =16\pi^2(p-A_0)+32\pi^2D\ge0,}
 \tag{19}
\]
\[
 \boxed{P=8\pi^2k+\frac\Delta2,\qquad
 Q_\kappa=8\pi^2k+\frac\Delta2+\frac L4,}
 \tag{20}
\]
\[
 \boxed{\mathcal E
 =\frac{32\pi^2k+2\Delta+L}{8\pi^2(A_0+k)+\Delta}.}
 \tag{21}
\]

In particular, there is no extra \(L/4\) in the formula for \(P\) in (20).
It has already been included in \(\Delta/2\). Since (19) gives
\(0\le L\le2\Delta\), every Kähler sequence with \(\Delta\to0\) satisfies

\[
 P\to8\pi^2 k,\qquad
 Q_\kappa\to8\pi^2 k,\qquad
 \mathcal E\longrightarrow\frac{4k}{A_0+k}.
 \tag{22}
\]

The scale-aware average and its pointwise consequence are equally explicit:

\[
 \frac{Q_\kappa}{\kappa^2V}\longrightarrow\frac{4k}{A_0},\qquad
 \liminf\frac{\|g^{-1}\operatorname{Ric}+\kappa I\|_{\infty,\mathrm{op}}}
 {\kappa}\ge\sqrt{\frac{k}{A_0}}.
 \tag{22a}
\]

The second statement is only a lower bound, obtained from (13), not an
assertion that the pointwise defect stays bounded or approaches that value.

These limits are realized on fixed smooth blow-ups, not just formally.
For example, take \(X=\Sigma_r\times\Sigma_s\) with its equal-curvature
negative product metric \(\omega_0\). It has no nonzero holomorphic vector
fields. For any distinct blow-up points and positive weights \(b_i\), the
Arezzo–Pacard theorem supplies negative cscK metrics in the classes

\[
 \Omega_\varepsilon=\pi^*[\omega_0]-\varepsilon^2\sum_{i=1}^k b_i E_i
\]

for all sufficiently small positive \(\varepsilon\).
[Arezzo–Pacard, Theorem 1.1](https://perso.pages.math.cnrs.fr/users/frank.pacard/Publications/43.pdf).
The complex surface and the blow-up points stay fixed. Here
\([\omega_0]=t\,c_1(K_X)\), \(t>0\), and direct intersection arithmetic gives

\[
 p_\varepsilon=
 \frac{(t A_0+\varepsilon^2\sum b_i)^2}
 {t^2 A_0-\varepsilon^4\sum b_i^2}\longrightarrow A_0.
 \tag{23}
\]

Since \(L=D=0\) exactly, (19) gives \(\Delta\to0\), whereas (22) gives
a positive limiting Einstein defect whenever \(k>0\). This approaches
the global all-metrics Ricci-energy infimum given by LeBrun's theorem.
It does not approach Einstein in the relative integral sense, and a
fortiori cannot be a sequence with vanishing normalized pointwise Ricci
defect. The obstruction in (22) is a fixed topological contribution,
not scalar variance or failure of LB equality.

## 6. What is inherited and what this calculation clarifies

The identity connecting LB remainder and Ricci-energy excess is already
classical, and is explicitly retained in the first-line correction.
This note does not rebrand it as a new estimate.

[Round 17, §6](round17_integral.md) already distinguishes scalar variance
\(L\), trace-free Ricci energy \(P\), and the mean-normalized volume gap.
Its equation (33) is the first identity in (7). In its notation
\(B=\int s^2-32\pi^2 A\), the Kähler specialization is simply
\(P=B/4\), by (6), while its volume gap is
\(\kappa^2V-2\pi^2 A=2\pi^2(p-A)\). This is not the LB remainder \(D\).

[Round 18](round18_periods.md) uses the separate \(B,P,L\) controls and
does not identify LB equality with Einstein equality.
[Round 21, equation (3) and §5](round21_comparison.md) already separates
the relative defect from absolute Ricci energy. The present formulas
give exact Kähler models for that distinction, including its different
behavior on minimal surfaces and fixed blow-ups.

The precise usable extra hypothesis is control of
\(\|a_g^-\|_2^2=p-a^2\), equivalently canonical-ray or normalized-volume
control in the positive-square setting, in addition to scalar variance.
For a blow-up one must not confuse \(a^2=A_0-k\) with the minimal-model
square \(A_0\): approaching \(p=A_0\) leaves primitive canonical energy
\(p-a^2\to k\), exactly as the actual metrics demonstrate.
