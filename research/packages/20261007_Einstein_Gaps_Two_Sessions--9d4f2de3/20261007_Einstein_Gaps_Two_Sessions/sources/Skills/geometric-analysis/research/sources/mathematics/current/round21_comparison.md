# The integral theorem and the classical Einstein obstruction

22 September 2026.

This note fixes the theorem comparison for the first research line. It does
not assert priority over all subsequent literature. The full polarized
extension, including positive-dimensional invariant insertions and the
\(b_+=1\) case, is already proved in [Round 13](round13_chamber.md).
Finite-cover and Pin-minus inputs are already treated in
[Round 14](round14_rigidity.md) and its
[twisted extension](round14_twisted_rigidity.md). These are part of the
current result, not new discoveries in this round.

## 1. The common positive-square setting

Let \(X\) be a closed oriented smooth four-manifold, put
\(T_X=2\chi(X)+3\tau(X)>0\), and assume a spin-c structure has a nonzero
Seiberg–Witten invariant with real first Chern class \(c\). For \(b_+(X)=1\),
the nonzero invariant is required in the small-perturbation chamber.
Allowed insertions are retained. Set

\[
A=c^2\ge T_X>0,\qquad
M=X\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3),
\qquad D=k+4\ell.
\]

The existing integral theorem gives, for every smooth metric,

\[
\mathcal E_M(g)+\left(\frac{T_X-D}{A}-\frac23\right)_+
\ge c_*>0,\qquad
\mathcal E_M(g)=\inf_{\lambda\ne0}
\frac{\int|\operatorname{Ric}_g-\lambda g|^2}
{\lambda^2\operatorname{Vol}_g(M)}.                         \tag{1}
\]

The constant does not depend on \(X,k,\ell,g\). The proof selects a monopole
at the metric's polarization, holds that structure fixed through conformal
rescaling, and uses its projection and square bounds

\[
(a_H^+)^2\ge A,\qquad
a_H^2=A-k\ge T_M=T_X-D.                                  \tag{2}
\]

The gauge input is the construction in
[LeBrun, Proposition 3.2](https://arxiv.org/pdf/math/0003068), together
with the insertion and chamber details proved in Round 13. The new analytic
input relative to the classical obstruction is the integral calibration
argument of [Round 4](round4_rigidity.md), not an assertion that a strict
inequality by itself has a uniform gap.

The present comparison concerns the positive-square setting. No assertion
about \(T_X=0\) is obtained by dividing by \(T_X\); Ricci-flat examples such as
K3 make that exclusion important.

## 2. Optimize the defect and treat the Ricci-flat case separately

Write

\[
V=\operatorname{Vol}(g),\quad S=\int s,\quad
R_2=\int|\operatorname{Ric}|^2,
\quad P=\int|\operatorname{Ric}^{\circ}|^2,
\quad L=\int(s-S/V)^2.
\]

For \(R_2>0\), minimizing the quadratic in \(x=1/\lambda\) gives

\[
\mathcal E(g)=4-\frac{S^2}{VR_2}=\frac{4P+L}{R_2}.        \tag{3}
\]

If \(S\) is nonzero the minimum occurs at \(\lambda=R_2/S\). If \(S=0\),
the infimum is four and need not be attained. For a Ricci-flat metric the
original definition also gives **four**, not zero. Thus substituting
\(\mathcal E=0\) handles exactly the non-Ricci-flat Einstein case.

In the family above, the polarized scalar monopole estimate gives

\[
\int s_-^2\ge32\pi^2A>0.                                \tag{4}
\]

It rules out Ricci-flat metrics separately. Consequently the final
nonexistence statements do cover every Einstein sign. Formula (3) must not
be applied with a zero denominator or used in place of (4).

## 3. Strict threshold, closed-band formulation, and integral strength

For a minimal general-type complex surface, \(A=T_X=c_1^2(X)\). The theorem
becomes

\[
\mathcal E(g)+(1/3-D/A)_+\ge c_* .                         \tag{5}
\]

An Einstein metric would require \(D/A\le1/3-c_*\). Hence the exact exclusion
is \(D/A>1/3-c_*\). Equality at this last threshold is not excluded by (5)
alone. To write a convenient closed threshold, choose \(\gamma=c_*/2\):

\[
D/A\ge1/3-\gamma
\quad\Longrightarrow\quad
\mathcal E(g)\ge c_*/2\quad\hbox{for all }g.               \tag{6}
\]

This gives both all-sign Einstein nonexistence and

\[
\delta_\sigma(g)\ge\sqrt{c_*/8},\qquad \sigma=\pm1,       \tag{7}
\]

because \(\mathcal E(g)\le4\delta_\sigma(g)^2\). These are consequences of
one main estimate, not three independent discoveries.

LeBrun's classical \(D\ge A/3\) obstruction is recovered in this setting.
The direction of logical implication is

\[
\text{uniform integral gap}\ \Longrightarrow\
\text{exact Einstein obstruction}.
\]

The reverse arrow describes a research ambition, not a valid implication:
strict positivity on each object does not imply a uniform positive lower
bound across objects or degenerating metrics.

## 4. The extra band contains actual smooth manifolds

Inclusion of intervals of real numbers is not by itself enough to show
that more allowable topologies are covered. Here the added interval is
realized. For \(m\ge2\), let

\[
X_m=\Sigma_2\times\Sigma_m,\qquad A_m=8(m-1),\qquad
k_m=\lceil A_m/3\rceil-1.
\]

The product complex surface is minimal of general type. Its canonical
bundle is ample, since each factor has positive-degree canonical bundle.
The Chern-square computation is
\(c_1^2=2(2-2\cdot2)(2-2m)=8(m-1)\). Thus

\[
0<\frac13-\frac{k_m}{A_m}\le\frac1{A_m}\longrightarrow0.  \tag{8}
\]

All these ratios lie below the cited classical threshold, whereas every
sufficiently large \(m\) lies in the band (6). Their Euler characteristics
grow without bound, so this is an infinite collection of distinct
topological types. The stronger threshold therefore adds actual members
of the family, not merely unattained real parameter values.

This argument does not assert that no other literature already obstructs
any of these individual manifolds. It proves strict enlargement relative
to the particular classical threshold under comparison. Since \(c_*\) is
not explicit in the current manuscript, it does not name a numerical
first qualifying \(m\).

There is a useful discrete qualification for \(b_+=1\). For any closed
oriented almost-complex four-manifold in that case,

\[
c_1^2=2\chi+3\tau=9-4b_1-b_2^-\le9.                     \tag{9}
\]

When this square is positive it belongs to \(\{1,\ldots,9\}\). If \(D/A<1/3\),
then

\[
\frac13-\frac DA=\frac{A-3D}{3A}\ge\frac1{27}.           \tag{10}
\]

A small unknown gap constant consequently need not add an exact blow-up
topology in this low-\(b_+\) subfamily. Its critical **integral** conclusion
is nevertheless stronger: at \(A=3,D=1\), for example, (5) gives a uniform
positive defect for every metric. Round 13 already records an actual
simply connected general-type base with these data. This is why the
chamber extension and the uniform-threshold enlargement should not be
conflated.

## 5. Absolute Ricci energy is a different invariant

LeBrun's absolute Ricci-energy theorem computes, for the complex family,

\[
\inf_g\int|\operatorname{Ric}_g|^2=8\pi^2(A+D).
\]

The relative quantity (3) instead controls which fraction of Ricci energy
is due to trace-free Ricci and scalar variation. A lower bound on the
absolute energy does not by itself bound this fraction away from zero.
Conversely (5) does not compute the absolute energy infimum or the minimal
volume results in the same paper. The correct dependency is classical
gauge-theoretic curvature inequalities plus the new integral self-test,
yielding a quantitative strengthening of the Einstein obstruction.

The current proof chain is therefore best presented in four layers:

1. the intrinsic integral calibration theorem;
2. polarized, covered, or twisted gauge inputs with verified square cost;
3. uniform topological-band inequalities for all metrics;
4. exact and pointwise consequences, with their scope and endpoint stated.

The comparison is not a substitute for checking the analytic theorem. This
round's independent calculation and analytic extension are recorded in
[the bounded two-form proof](round21_analytic.md).
