# Exact variational values on the closed sheared gluings

21 September 2026.

## 1. Objects, normalization and conclusions

Let \(M=M(h,g;u,f)\) be the self-gluing of
\(F_{h,2}\times\Sigma_g\), where \(h\ge1\), \(g\ge2\),
\(u\ne0\), and \(f\) is orientation preserving, as defined in
`round11_graph_topology.md`. No order condition on \([f]\) is needed
here. The established inputs are:

* \(\chi=4h(g-1)>0\), \(\tau=0\), and \(b_1\ge1\);
* symplectic forms in both orientations, constructed in Section 6 of
  `round11_closed_gluing.md`;
* no Kähler structure on any finite cover, proved in
  `round11_kahler.md`;
* smooth metrics \(g_j=3G_{\ell_j}\) on this fixed closed manifold with

\[
 V_j=V_0:=4\pi^2\chi,
 \qquad
 \delta_j:=\|g_j^{-1}\operatorname{Ric}_{g_j}+I\|_{\infty,\mathrm{op}}
 \longrightarrow0.
 \tag{1}
\]

In either orientation,
\(b_2^\pm=\chi/2-1+b_1\ge2\). Thus no chamber-dependent
\(b^+=1\) assertion is needed. Write
\(E_g=\operatorname{Ric}_g-s_g g/4\). All curvature tensors below
use the full covariant tensor norm; in particular
\(|\operatorname{Rm}|^2=\sum_{i,j,k,l}R_{ijkl}^2\), not the norm of
the curvature operator on \(\Lambda^2\).

**Theorem.** These manifolds satisfy

\[
\begin{aligned}
\sigma(M)&=-8\pi\sqrt\chi,\\
\inf_{\operatorname{Ric}_g\ge-g}\operatorname{Vol}(M,g)
 &=4\pi^2\chi,\\
\inf_g\int_M s_g^2\,d\mu_g&=64\pi^2\chi,\\
\inf_g\int_M|\operatorname{Ric}_g|^2\,d\mu_g&=16\pi^2\chi,\\
\inf_g\int_M|\operatorname{Rm}_g|^2\,d\mu_g&=32\pi^2\chi.
\end{aligned}
\tag{2}
\]

No conformal class realizes the Yamabe invariant \(\sigma(M)\).
The constrained-volume, scalar-energy and Ricci-energy infima are
also not attained. In contrast, attainment of the full-curvature
infimum is **equivalent to existence of some Einstein metric on
\(M\)** and is not decided here.

These values result from applying classical monopole estimates to the
closed construction. They do not assert a new general monopole
inequality or an all-Einstein obstruction.

## 2. The scalar negative-part estimate and its equality case

Choose either symplectic orientation and let \(a\) be the first
Chern class of its associated almost-complex structure, with either
choice of sign. Then

\[
 a^2=2\chi+3\tau=2\chi>0.
 \tag{3}
\]

[Taubes, *The Seiberg--Witten invariants and symplectic forms*,
Math. Res. Lett. 1 (1994), 809--822, Main Theorem](https://doi.org/10.4310/MRL.1994.v1.n6.a15)
gives a nonzero Seiberg--Witten invariant for this class when
\(b^+>1\). For every metric the unperturbed equations therefore
have a solution. One may obtain it as a limit of small generic
perturbations; reducibility is excluded since
\((a_g^+)^2\ge a^2>0\).

Set \(s_-:=\max\{-s,0\}\). The conventions for the monopole
equations, the quadratic map and the Weitzenböck formula are those
in [LeBrun, Section 2, equations (2)--(6)](https://arxiv.org/pdf/math/0003068):
\(|F_A^+|^2=|\Phi|^4/8\) and

\[
 0=\int_M\bigl(4|\nabla_A\Phi|^2+s|\Phi|^2+|\Phi|^4\bigr)\,d\mu.
\]

Consequently

\[
 \int|\Phi|^4
 \le\int s_-|\Phi|^2
 \le\left(\int s_-^2\right)^{1/2}
       \left(\int|\Phi|^4\right)^{1/2}.
\]

The spinor is nonzero. Hodge projection of the determinant curvature
then gives

\[
 \boxed{
 \int_M s_-^2\,d\mu
 \ge\int_M|\Phi|^4\,d\mu
 =8\int_M|F_A^+|^2\,d\mu
 \ge32\pi^2(a_g^+)^2
 \ge64\pi^2\chi.}
 \tag{4}
\]

The last inequality uses
\((a_g^+)^2=a^2+\|a_g^-\|_{L^2}^2\), with the harmonic-form
normalization for the real cohomology class. This argument uses the
negative part, so it does not assume that an arbitrary metric has
nonpositive scalar curvature.

Equality in (4) forces equality in the first integrated inequality.
Thus \(\nabla_A\Phi=0\). Its quadratic two-form is a nonzero
parallel self-dual form of constant length, which defines a parallel
orthogonal complex structure. The metric is Kähler. In particular,
equality is impossible on the present \(M\). The same conclusion
holds if \(\int s^2=64\pi^2\chi\), since
\(\int s^2\ge\int s_-^2\).

## 3. Yamabe invariant and nonattainment

For a conformal class \([g]\), use

\[
 Y([g])=\inf_{v>0}
 \frac{\int_M(6|dv|_g^2+s_gv^2)\,d\mu_g}
      {(\int_Mv^4\,d\mu_g)^{1/2}},
 \qquad \sigma(M)=\sup_{[g]}Y([g]).
\]

The Yamabe theorem supplies a smooth constant-scalar-curvature
minimizer in each class; see
[Schoen, J. Differential Geometry 20 (1984), 479--495](https://math.jhu.edu/~js/Math646/schoen.yamabe.pdf).
Equation (4) excludes nonnegative scalar curvature, so this minimizer
has negative scalar curvature. For it,
\(Y([g])^2=\int s^2\ge64\pi^2\chi\). Therefore

\[
 Y([g])\le-8\pi\sqrt\chi.
 \tag{5}
\]

For the explicit family (1),
\(s_{g_j}\ge-4(1+\delta_j)\). Hölder's inequality, with this
negative lower bound, gives for every positive \(v\)

\[
 \frac{\int(6|dv|^2+s_{g_j}v^2)}{(\int v^4)^{1/2}}
 \ge-4(1+\delta_j)V_0^{1/2}.
\]

Hence \(Y([g_j])\to-8\pi\sqrt\chi\), proving the first value
in (2). If a class attained this supremum, its Yamabe metric would
saturate (4), hence be Kähler. The Kähler obstruction excludes this.
Nonattainment concerns the supremum over conformal classes, not the
existence of the Yamabe minimizer inside any individual class.

## 4. Ricci-lower-bound minimal volume

Let
\(\mathcal V_{\mathrm{Ric}}(M)=
\inf\{\operatorname{Vol}(M,g):\operatorname{Ric}_g\ge-g\}\).
For any admissible metric, \(s_g\ge-4\), so \(s_-^2\le16\).
Combining this with (4) proves

\[
 16\operatorname{Vol}(M,g)
 \ge\int_Ms_-^2\,d\mu_g
 \ge64\pi^2\chi.
 \tag{6}
\]

To attain the infimum as a limit, set
\(\widetilde g_j=(1+\delta_j)g_j\). Constant rescaling leaves
the covariant Ricci tensor unchanged, so

\[
 \operatorname{Ric}_{\widetilde g_j}
 =\operatorname{Ric}_{g_j}
 \ge-(1+\delta_j)g_j=-\widetilde g_j,
 \qquad
 \operatorname{Vol}(\widetilde g_j)
 =(1+\delta_j)^2V_0\longrightarrow V_0.
\]

This proves \(\mathcal V_{\mathrm{Ric}}(M)=V_0\).
If equality were attained in (6), then \(s_-\equiv4\), hence
\(s\equiv-4\). Together with \(\operatorname{Ric}\ge-g\),
this already forces \(\operatorname{Ric}=-g\). Equality in (4)
also forces a Kähler structure, a contradiction.

The identical argument gives
\(\inf_{s_g\ge-4}\operatorname{Vol}(M,g)=V_0\), also unattained.
Replacing \(s_-^2\) by \(s^2\) in the lower-bound argument would
be invalid: a Ricci lower bound does not exclude positive scalar spikes.

## 5. Three curvature energies, two different equality mechanisms

Equation (4) gives the scalar-energy lower bound. For Ricci energy,

\[
 |\operatorname{Ric}|^2=|E|^2+\frac{s^2}{4}
 \quad\Longrightarrow\quad
 \int|\operatorname{Ric}|^2\ge16\pi^2\chi.
 \tag{7}
\]

Along (1), \(s_{g_j}\to-4\) and
\(|\operatorname{Ric}_{g_j}|^2\to4\) uniformly, while the
volumes are exactly \(V_0\). This attains both lower bounds as
limits. Equality for scalar energy would give a Kähler metric.
Equality for Ricci energy would additionally force \(E=0\).
Neither infimum is attained on \(M\).

For the full curvature tensor, the four-dimensional
Chern--Gauss--Bonnet identity is instead

\[
 32\pi^2\chi
 =\int_M\bigl(|\operatorname{Rm}|^2
               -4|\operatorname{Ric}|^2+s^2\bigr)\,d\mu,
\]

or, equivalently,

\[
 \boxed{\int_M|\operatorname{Rm}|^2\,d\mu
        =32\pi^2\chi+4\int_M|E|^2\,d\mu.}
 \tag{8}
\]

The convention agrees with the curvature-operator Chern--Weil
formulas in [LeBrun, equation (1)](https://arxiv.org/pdf/math/0003068)
after multiplying the curvature-operator squared norm by four.
The trace-free projection is orthogonal, so (1) implies
\(|E_{g_j}|^2\le4\delta_j^2\). Fixed volume makes its integral
tend to zero, proving the last infimum in (2).

Equation (8) has equality precisely when \(E=0\). On a connected
four-manifold, the contracted Bianchi identity then makes the scalar
curvature constant. Thus equality is precisely the Einstein condition.
It imposes **no scalar-energy equality** in (4). Accordingly, the
nonattainment conclusions above do not prove nonattainment in (8).

## 6. The remaining Einstein alternative

The fundamental group excludes positive and Ricci-flat Einstein
metrics, as shown in `round11_kahler.md`. Any remaining Einstein
metric can be normalized to \(\operatorname{Ric}=-g\). For such
a metric the results above imply strictly

\[
 \operatorname{Vol}(M,g)>4\pi^2\chi,
 \quad Y([g])=-4\sqrt{\operatorname{Vol}(M,g)}<\sigma(M),
 \quad \int|\operatorname{Rm}|^2=32\pi^2\chi.
 \tag{9}
\]

A negative constant-scalar-curvature metric is the Yamabe minimizer
in its own conformal class. There is no conflict between the strict
Yamabe inequality in (9) and its being Einstein: it need not maximize
the Yamabe invariant over all conformal classes. Likewise it need
not minimize volume among all metrics with \(\operatorname{Ric}\ge-g\).

The smallest even-\(b_1\) example has \(\chi=4\), so
\(\sigma=-16\pi\), \(\mathcal V_{\mathrm{Ric}}=16\pi^2\),
and the three energy infima are respectively
\(256\pi^2,64\pi^2,128\pi^2\). The first two are unattained;
attainment of the third is the remaining global Einstein question.

All these formulas also hold on any connected finite cover, with
its own Euler characteristic. Pullback preserves the symplectic forms
and the uniform defect, multiplies volume and Euler characteristic
by the covering degree, and the virtual Kähler obstruction supplies
the same nonattainment conclusion. The stable-letter homomorphism
has nonzero restriction to every finite-index subgroup, so the cover
still has \(b_1\ge1\) and hence \(b^+>1\).
