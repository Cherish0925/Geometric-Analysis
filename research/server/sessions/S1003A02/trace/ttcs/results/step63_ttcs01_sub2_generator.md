# TTCS Independent Branch Record

```json
{
  "step_id": 63,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md",
    "Sessions/S1003A02/workspace/notes/step62_weyl_channel_reduction.md"
  ]
}
```

## Task

Research question for the open-range Einstein-gap lower bound on M = X#kCP̄² (X minimal general type, k < A/3). Step 63 (file attached) shows: (i) for every metric and every orthogonal almost complex structure J, the exceptional flux 2π|c1(J)^-| ≥ 2π√k must be carried by J-invariant tracefree Ricci (costing P) or by the ASD frame twist (α∧β)^-; (ii) all rational-cohomology/SW/Chern–Weil constraints are saturated at p = 0 only by configurations made of W⁺ = 0 negative Einstein patches with the Chern numbers of an orientation-reversed fake projective plane, so what is unpriced is the joining / transition between W⁺-carrying Kähler-type regions and twist-carrying W⁺≈0 regions. Develop concrete, provable mechanisms for a 'domain-wall' lower bound: a quantitative estimate showing that a region where the frame twist carries flux 2π, bordered by a region where J is nearly parallel and W⁺ is of Kähler type with s<0, costs P ≥ c·8π² with explicit c>0 (or explain why no such bound can hold, with a construction sketch of a cheap fat transition). Consider: localized Chern–Weil/Gauss–Bonnet on the wall with boundary transgression terms; monotonicity or capacity arguments for the twist energy ∫|(α∧β)^-|² ≤ ∫|∇Ω|⁴/32; the role of the zeros of the Nijenhuis tensor (c2 = 5χ+6τ); comparison with the 2-ended AE neck bound P ≥ 32π²; and whether the competitor X#k\overline{FPP} could have α < 8π²k. State precise inequalities with quantifiers and name what would need to be proved or computed to decide.

## Output

The Step-63 frame-twist identity turns the open-range problem into an interface problem. The bulk rational identities — Chern–Weil, Seiberg–Witten sign classes, Yamabe, and the ASD flux identity — admit a zero-cost disconnected limit made of Kähler-type regions and twist-carrying \(W^+=0\) regions. What remains unpriced is the transition layer where the carrier of the exceptional flux changes from the \(J\)-invariant tracefree Ricci channel to the ASD frame-twist channel. A domain-wall lower bound should therefore be formulated as a relative estimate on a compact domain whose interior carries one exceptional period and whose exterior is nearly Kähler.

A useful target statement is the following.

**Domain-wall target.** Let \(e\) be an exceptional class with \(e^2=-1\), and let \(J\) be an orthogonal almost complex structure with \(c_1(J)\cdot e=1\). Write \(\Omega=g(J\cdot,\cdot)\), \(u=\frac14|\nabla\Omega|^2\), and \(t=(\alpha\wedge\beta)^-\). For every \(\varepsilon>0\) there should exist \(\delta>0\) and a universal \(c>0\) such that if a domain \(U\) satisfies

\[
\left|\int_{S_e}\gamma_J-2\pi\right|<\delta,
\]

if outside a core region \(J\) is \(\delta\)-close to parallel and \(W^+\) is \(\delta\)-close to the Kähler eigenvalue form \((s/6)\Omega\) with \(s=-4\), and if inside the core the twist carries the exceptional flux,

\[
\|t\|_{L^2(U_{\rm core})}\ge 2\pi(1-\delta),
\]

then

\[
\int_U |\operatorname{Ric}_0|^2 \;\ge\; 8\pi^2(c-\varepsilon).
\]

The different mechanisms below give concrete ways to obtain such a \(c\), or to discover that no such universal \(c\) exists.

---

## 1. Relative Chern–Weil/Gauss–Bonnet with interface transgression

The most direct representation of the wall price is a localized Chern–Weil identity. For a compact 4-domain \(U\) with separating interface \(\Sigma=\partial U\), the characteristic number \(2\chi+3\tau\) localizes as a bulk density plus an interface transgression term. Schematically,

\[
(2\chi+3\tau)^{\rm rel}_U
=
\frac{1}{8\pi^2}\int_U q(g)
-
{\rm CS}_{2\chi+3\tau}(\Sigma;g),
\]

where \(q(g)\) is the Chern–Weil density for \(2\chi+3\tau\) and \({\rm CS}_{2\chi+3\tau}\) is the associated Chern–Simons transgression 3-form. Since

\[
P=4\int |W^+|^2+\frac1{12}\int s^2-8\pi^2(2\chi+3\tau),
\]

one obtains, after subtracting a reference model equal to the phase near \(\Sigma\), a relative identity of the form

\[
\boxed{
\frac{P_U}{8\pi^2}
=
m_U-\frac{4}{3}\kappa_U+\frac{1}{3}\upsilon_U+\Theta_U+E_U .
}
\]

Here:

- \(m_U\) is the exceptional period carried inside \(U\), e.g. \(m_U=1\) for one class;
- \(\kappa_U\) is the relative Weyl deficit, including the interface contribution from \(|W^+|^2\);
- \(\upsilon_U\) is the relative Yamabe excess, including the interface contribution from \(s^2\);
- \(E_U\ge 0\) collects the non-Kähler terms \(2\int|\rho_*''|^2+4\int|W_3^+|^2\) and their general-\(J\) analogues;
- \(\Theta_U\) is the residual interface transgression not absorbed into \(\kappa_U,\upsilon_U\).

The disconnected patch configuration has \(\Theta_U=0\). A thin two-ended asymptotically Euclidean neck gives \(\Theta_U=4\), corresponding to \(P=32\pi^2\). A Burns-type cell gives a value close to \(1\). Thus the open problem is exactly to prove that for a wall separating a nearly Kähler phase from a twist-saturated phase,

\[
\Theta_U+E_U \;\ge\; c>0.
\]

This formulation is useful because it converts the geometric question into a computable Chern–Simons path problem: the two phases determine two interface connections on \(\Sigma\), and \(\Theta_U\) is the action of a path between them. For \(\Sigma\cong S^3\), the relevant path space is a space of \(U(2)\) or \(SO(4)\) connections. The thin neck, the Burns cap, and the putative fake-projective-plane cap are different paths. The minimal action of this path problem is the wall constant.

A precise inequality to prove is therefore:

\[
\boxed{
\Theta_U
\ge
\inf_{\mathcal P(K\to T)}
\mathcal A_{\rm CS}(\mathcal P)
=:c_{\rm CS},
}
\]

where \(\mathcal P(K\to T)\) runs over interface paths from the Kähler-type connection to the twist/ASD connection carrying one exceptional period. If \(c_{\rm CS}>0\), the domain-wall bound follows. The known reference values are

\[
c_{\rm thin\ neck}=4,
\qquad
c_{\rm Burns}\approx 1.
\]

The decisive computation is the actual infimum for the Kähler-to-twist path. If the infimum is positive, one has an explicit wall tariff. If it is zero, a cheap fat transition exists and no universal wall bound can come from rational Chern–Weil data alone.

---

## 2. Weyl-channel efficiency and a concrete \(c=1/3\) mechanism

The global identity from Step 62,

\[
p=k-\frac{4}{3}\kappa+\frac{1}{3}\upsilon,
\qquad
p=\frac{P}{8\pi^2},
\]

allows a particularly transparent wall estimate. Suppose one exceptional class is transferred from the Kähler/Ricci channel to the twist channel. The patch model of Step 63 corresponds approximately to

\[
\kappa=2,
\qquad
\upsilon=5,
\qquad
p=0.
\]

A Kähler or Burns-like initial phase has, to first order, the LeBrun efficiency

\[
\upsilon \approx 4\kappa,
\]

which is the same as the Burns breakeven efficiency \(\eta_B=1/4\). Thus at \(\kappa=1\) one expects

\[
\upsilon(1)\ge 4.
\]

If the twist-transfer interval \(\kappa\in[1,2]\) were traversed with too little additional Yamabe excess, the global algebra would drive \(p\) below any positive tariff. Conversely, a finite-amplitude efficiency estimate gives an explicit wall bound.

A sufficient statement is:

\[
\boxed{
\upsilon(2)-\upsilon(1)\ge 2.
}
\]

Indeed, if \(\upsilon(1)\ge 4\), then \(\upsilon(2)\ge 6\), and hence

\[
p
=
1-\frac{8}{3}+\frac{\upsilon(2)}{3}
=
\frac{\upsilon(2)-5}{3}
\ge
\frac{1}{3}.
\]

Thus the explicit tariff

\[
\boxed{
P\ge \frac{8\pi^2}{3}
}
\]

would follow from the finite-amplitude wall inequality

\[
\upsilon(2)-\upsilon(1)\ge 2.
\]

More generally,

\[
\upsilon(2)-\upsilon(1)\ge 1+3c
\]

gives

\[
p\ge c.
\]

So the domain-wall problem can be stated in the following sharp form:

**Wall efficiency inequality.** Let \((g_r,J_r)\), \(r\in[0,1]\), be a path of almost-Kähler metrics with \(s=-4\), connecting a Kähler-type phase at \(r=0\) to a twist-saturated phase at \(r=1\). Let \(\kappa(r),\upsilon(r)\) be the cumulative relative Weyl deficit and Yamabe excess. If the path transfers one exceptional flux unit from the Ricci channel to the twist channel, then

\[
\boxed{
\upsilon(1)-\upsilon(0)\ge 5+3c.
}
\]

The Burns first-order calculation gives the infinitesimal version near the Kähler phase. The missing theorem is the finite-amplitude version across the twist-transfer region. A proof would likely require a local Bochner or Weitzenböck estimate relating the growth of \(u=|\nabla\Omega|^2/4\) to scalar overpayment. This route is attractive because it gives an explicit constant, \(c=1/3\), from a simple inequality that is directly testable in cohomogeneity-one models.

---

## 3. Chern–Simons estimate for the canonical \(U(1)\) connection

The canonical Chern connection \(b\) of \(J\) has curvature

\[
\gamma_J=-db=R(\Omega)+\alpha\wedge\beta,
\qquad
[\gamma_J]=2\pi c_1(J).
\]

For one exceptional class \(e\) with \(e^2=-1\),

\[
\int_U \gamma_J\wedge\gamma_J
=
4\pi^2 e^2
=
-4\pi^2.
\]

The interface Chern–Simons invariant

\[
{\rm CS}_\Sigma(b)
=
\frac{1}{4\pi^2}\int_\Sigma b\wedge db
\]

therefore changes by one unit between the two sides of the wall. This gives a Yang–Mills-type lower bound on the total curvature energy of the canonical connection:

\[
\int_U |\gamma_J|^2
\ge
4\pi^2
\left|
\Delta{\rm CS}_\Sigma(b)
\right|.
\]

The difficulty is that \(P\) does not control all of \(|\gamma_J|^2\). In the almost-Kähler identity,

\[
P=
2\|\gamma_J^-\|^2
+
\int u(5u+s)
+
2\int|\rho_*''|^2
+
4\int|W_3^+|^2,
\]

the term \(\int u(5u+s)\) can be sign-indefinite when \(s=-4\), and it is precisely this term that allows the disconnected patch model to have zero total cost. The wall estimate must show that the Chern–Simons action cannot be completely absorbed by the torsion potential while \(u\) moves from \(0\) to \(2/3\).

A precise conditional inequality is:

\[
\boxed{
P_U
\ge
8\pi^2
-
\int_U u(4-5u)_+
-
C\int_U\bigl(|\rho_*''|^2+|W_3^+|^2\bigr).
}
\]

Thus a positive \(c\) follows if one proves the potential absorption estimate

\[
\int_U u(4-5u)_+
\le
4\pi^2(1-2c).
\]

For example, if the wall cannot keep more than half of the torsion potential in the favorable window \(0<u<4/5\), then \(c=1/4\). The required input is a local relation between the change of the Chern–Simons invariant and the torsion density \(u\). The natural object is the relative Chern–Simons functional of \(b\) on the interface \(S^3\). Its critical points are the Burns-type and ASD-type caps. Computing this finite-dimensional functional would give an explicit constant.

---

## 4. Capacity and monotonicity for the twist energy

The twist satisfies

\[
|t|^2=|(\alpha\wedge\beta)^-|^2
\le
\frac{1}{32}|\nabla\Omega|^4.
\]

If a wall separates a region where \(t\approx 0\) from a region where \(t\) carries flux \(2\pi\), then the twist energy must grow across the wall. A capacity estimate gives one way to quantify this.

Let \(\chi\) be a cutoff function with \(\chi=0\) on the nearly Kähler side and \(\chi=1\) near the twist core. Since \(\gamma_J\) is closed and has period \(2\pi\) over the exceptional sphere,

\[
2\pi
=
\int d\chi\wedge\gamma_J
\le
C\|d\chi\|_{L^2}\,\|\gamma_J\|_{L^2}.
\]

Optimizing over \(\chi\) gives

\[
\boxed{
\|\gamma_J\|_{L^2(U_{\rm wall})}^2
\ge
\frac{4\pi^2}{C^2\,{\rm Cap}(U_{\rm wall})},
}
\]

where

\[
{\rm Cap}(U_{\rm wall})
=
\inf_\chi \int_{U_{\rm wall}} |d\chi|^2.
\]

If the wall is thin, the capacity is large and the curvature energy is forced. If the wall is fat, the capacity can become smaller, but then the Yamabe excess grows. The coupled estimate should have the form

\[
\boxed{
P_U
\ge
\frac{A}{1+\upsilon_U}
}
\]

for an explicit constant \(A\). Combining this with the scalar contribution \(\upsilon_U/3\) gives

\[
p_U
\ge
\frac{A}{8\pi^2(1+\upsilon_U)}+\frac{\upsilon_U}{3}.
\]

The right-hand side has a positive minimum over \(\upsilon_U\ge0\). For example, if \(A/(8\pi^2)=1\), then

\[
p_U
\ge
\min_{v\ge0}
\left(
\frac{1}{1+v}+\frac{v}{3}
\right)
>0.
\]

The minimum occurs at \(v=\sqrt{3}-1\), giving

\[
p_U\ge 2\sqrt{3}/3-1/3\approx 0.821.
\]

The numerical value is not the main point; the structure is. A capacity-Yamabe coupling gives a positive wall cost even when the transition is spread over a large volume.

What must be proved is a monotonicity or transport inequality for the twist flux. Let \(T(r)\) be the \(L^2\)-norm of \(t\) on the region inside a level set of a normal coordinate \(r\). One wants an estimate of the form

\[
\left|\frac{dT}{dr}\right|
\le
C
\left(
\int_{\Sigma_r}|\operatorname{Ric}_0|^2
\right)^{1/2}
+
C' T(r)^{3/2}.
\]

Integrating from \(T=0\) in the Kähler phase to \(T=2\pi\) in the twist phase would yield

\[
P_U\ge c_{\rm cap}\,8\pi^2.
\]

The constants depend on the capacity of the standard exceptional tube. The round \(S^3\)-tube model is computable explicitly, and the cohomogeneity-one AAD local models provide the natural test geometries.

---

## 5. Nijenhuis zeros as topological wall defects

The Nijenhuis tensor \(N_J\) is a section of

\[
E=T^{1,0}\otimes K_J^{-1},
\]

and

\[
c_2(E)=c_2+2c_1^2=5\chi+6\tau.
\]

For \(M=X\#k\overline{\mathbb{CP}}^2\),

\[
5\chi+6\tau
=
c_2(X)+2A-k,
\]

which is positive throughout the open range. A region with \(u=0\) has \(N_J=0\), whereas a twist-saturated region has \(|N_J|^2\sim u>0\). Therefore any wall connecting the two phases must contain zeros or degenerations of \(N_J\).

The appropriate transgression formula is the Mathai–Quillen current identity:

\[
c_2(E)
=
[Z_J]
+
dQ(N_J,\nabla N_J),
\]

where \(Z_J\) is the zero current of \(N_J\). Integrating over a wall \(U\) gives

\[
\int_U c_2(E)
=
\sum_{z\in Z_J\cap U}{\rm ind}(z)
+
\int_{\Sigma} Q(N_J,\nabla N_J).
\]

Because \(|N_J|^2\) is proportional to \(u\), the transgression term is controlled by quantities of the form

\[
\int_U \frac{|\nabla u|^2}{u}
\]

together with curvature terms. A local Weitzenböck formula for \(N_J\) should give

\[
|\nabla N_J|^2
\le
C\left(
|\operatorname{Ric}_0|^2+u^2+|W^+|u
\right).
\]

If each wall-required zero carries a local curvature amount \(c_N\), then

\[
P_U\ge c_N\,8\pi^2.
\]

The decisive local computation is the index density of a zero of \(N_J\) compatible with an exceptional sphere. Armstrong’s relation \(c_1(I)=3c_1(J)\) for a nonintegrable \(J\) with \(N_J\neq0\) suggests that zeros mediate a change of Chern class. If one unit of exceptional flux transfer forces one unit of local Nijenhuis charge, then the wall cost is topological and cannot be removed by thickening the transition. This mechanism is especially important because it sees smooth almost-complex data, not merely rational cohomology.

---

## 6. Comparison with the two-ended AE neck and the fake-projective-plane competitor

The two-ended asymptotically Euclidean neck bound

\[
P\ge 32\pi^2
\]

is the value of the interface functional for a thin Einstein neck. It corresponds to \(p=4\) per join. It is not automatically the minimal wall cost: a fat transition or a Burns-type cap can reduce the price. The certified CH cell, with \(p\approx0.9957\), already shows that the thin-neck value is not sharp for local exceptional insertions.

The serious competitor is a summand \(Y\) with the rational data of an exceptional summand but with an ASD Einstein metric \(h\) satisfying

\[
W_h^+=0,
\qquad
s_h<0,
\qquad
P(h)=0.
\]

An orientation-reversed fake-projective-plane-type piece is the numerical candidate. If one forms

\[
M_Y=X\#kY,
\]

then the disconnected limit again saturates all rational identities. Define

\[
c_Y
=
\lim_{k\to\infty}
\frac{\alpha(X\#kY)}{8\pi^2 k}.
\]

If

\[
c_Y<1,
\]

then the tariff \(8\pi^2k\) for \(X\#k\overline{\mathbb{CP}}^2\) cannot follow from rational Chern–Weil and Seiberg–Witten data alone. It must use smooth information specific to the exceptional summand, such as Taubes’ period constraints and the existence of symplectic \((-1)\)-spheres. If

\[
c_Y=0,
\]

then no positive wall bound can hold for configurations built from such pieces unless the smooth type of the summand enters explicitly.

A cheap fat transition sketch is the following. Remove small balls from the Kähler host \(X\) and from the ASD Einstein piece \(Y\). Insert a cohomogeneity-one collar \(S^3\times[0,L]\) with \(s=-4\), and let \(u(r)\) and the eigenvalues of \(W^+\) solve the AAD local-model ODEs, interpolating between

\[
(u,W^+)=(0,s/6)
\]

and

\[
(u,W^+)=(2/3,0).
\]

As \(L\) grows, the local curvature density can become small if the ODE trajectory follows a low-action path. The remaining cost is the relative Chern–Simons or renormalized-volume functional. The decisive question is whether the heteroclinic action of this ODE is zero or positive. If the minimal action is \(c_F\), then

\[
\alpha(X\#kY)\approx 8\pi^2 k\,c_F.
\]

Thus the fake-projective-plane competitor is not a side issue; it is the cleanest test of whether the wall price is topological/smooth or merely an artifact of a thin-neck model.

---

## 7. Decisive computations and theorem shapes

The following concrete items would decide the domain-wall question.

1. **Finite-amplitude Burns efficiency.** Prove that along any almost-Kähler wall with \(s=-4\) transferring one exceptional flux unit from Ricci to twist,

   \[
   \upsilon(2)-\upsilon(1)\ge 2.
   \]

   This gives \(P\ge 8\pi^2/3\).

2. **Interface Chern–Simons path functional.** For the standard interface \(\Sigma=S^3\), compute

   \[
   c_{\rm CS}
   =
   \inf_{\mathcal P(K\to T)}
   \mathcal A_{\rm CS}(\mathcal P).
   \]

   The values \(4\) for the thin neck and \(\approx1\) for the Burns cap are benchmarks. A positive infimum gives an explicit wall constant.

3. **Twist capacity estimate.** Prove a coupled capacity-Yamabe inequality

   \[
   P_U\ge \frac{A}{1+\upsilon_U}
   \]

   for walls separating Kähler-type and twist-saturated phases. The constant \(A\) is determined by the capacity of the exceptional tube.

4. **Nijenhuis zero charge.** Compute the local index density of zeros of \(N_J\) near an exceptional sphere, and prove a local curvature estimate

   \[
   \int_{B(z)}|\operatorname{Ric}_0|^2\ge c_N\,8\pi^2.
   \]

   If one zero is forced per flux transfer, this gives a topological wall tariff.

5. **Fake-projective-plane gluing.** Solve the cohomogeneity-one gluing ODE between the Kähler host and the ASD Einstein \(Y\) piece. The minimal action gives \(c_Y\). If \(c_Y<1\), the smooth exceptional-sphere structure is essential. If \(c_Y\ge1\), the wall mechanism is robust.

The strongest near-term route is probably the efficiency inequality, because it connects directly to the already established Burns breakeven \(\eta=1/4\) and to the Weyl-channel identity. The most structural route is the interface Chern–Simons functional, because it identifies the wall cost as a genuine transgression invariant. The Nijenhuis-zero route is the one most likely to distinguish \(X\#k\overline{\mathbb{CP}}^2\) from rational-homology competitors such as \(X\#k\overline{\rm FPP}\).