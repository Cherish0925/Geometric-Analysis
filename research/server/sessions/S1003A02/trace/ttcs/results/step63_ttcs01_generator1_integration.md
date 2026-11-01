# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 63,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step63_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step63_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Research question for the open-range Einstein-gap lower bound on M = X#kCP̄² (X minimal general type, k < A/3). Step 63 (file attached) shows: (i) for every metric and every orthogonal almost complex structure J, the exceptional flux 2π|c1(J)^-| ≥ 2π√k must be carried by J-invariant tracefree Ricci (costing P) or by the ASD frame twist (α∧β)^-; (ii) all rational-cohomology/SW/Chern–Weil constraints are saturated at p = 0 only by configurations made of W⁺ = 0 negative Einstein patches with the Chern numbers of an orientation-reversed fake projective plane, so what is unpriced is the joining / transition between W⁺-carrying Kähler-type regions and twist-carrying W⁺≈0 regions. Develop concrete, provable mechanisms for a 'domain-wall' lower bound: a quantitative estimate showing that a region where the frame twist carries flux 2π, bordered by a region where J is nearly parallel and W⁺ is of Kähler type with s<0, costs P ≥ c·8π² with explicit c>0 (or explain why no such bound can hold, with a construction sketch of a cheap fat transition). Consider: localized Chern–Weil/Gauss–Bonnet on the wall with boundary transgression terms; monotonicity or capacity arguments for the twist energy ∫|(α∧β)^-|² ≤ ∫|∇Ω|⁴/32; the role of the zeros of the Nijenhuis tensor (c2 = 5χ+6τ); comparison with the 2-ended AE neck bound P ≥ 32π²; and whether the competitor X#k\overline{FPP} could have α < 8π²k. State precise inequalities with quantifiers and name what would need to be proved or computed to decide.

## Integrated Scientific Memo

## Domain-wall estimates: what is already provable, and what remains open

Write
\[
P(U)=\int_U|\operatorname{Ric}^{\circ}|^2,\qquad
Q(U)=\int_U\left(4|W^+|^2+\frac{s^2}{12}\right).
\]
The normalization throughout is \(p=P(M)/(8\pi^2)\).

**A positive wall tariff is provable when the interface has controlled Euler–signature transgression.** In particular, an exceptional cap attached along the boundary of a sufficiently small negative Kähler–Einstein ball has an explicit positive tariff, even if its interior transition is fat. AE exceptional bubbles cost at least one unit per exceptional generator; two-ended AE necks cost four units per join.

**There is not yet a proof, or a valid counterexample, for an unrestricted fat wall on \(X\#k\overline{\mathbf{CP}}^{\,2}\).** Twist energy, phase labels, and Nijenhuis zeros alone do not supply the missing coercivity. Several proposed capacity and Chern–Simons arguments do not define valid localized flux estimates.

### 1. Corrections to the proposed zero-cost configuration

These corrections materially change the interpretation of Step 63.

#### The two-phase model only has nonnegative volumes when \(k\le A/4\)

For the stated model,
\[
V=2\pi^2(A+5k),\qquad V_{\rm ASD}=18\pi^2k.
\]
Consequently,
\[
V_{\rm K}=2\pi^2(A-4k).
\]
Its parameters \(\kappa=2k,\ \upsilon=5k,\ p=0\) are therefore feasible as bulk algebra only for \(k\le A/4\), not throughout \(k<A/3\). At \(k=A/4\), the Kähler phase disappears.

These calculations do not establish that either phase, with the required almost-Kähler structure and interface data, is locally realizable.

#### The disconnected union is not the connected-sum zero-cost model

Let \(Y=\overline{\mathrm{FPP}}\). Then
\[
(2\chi+3\tau)(Y)=3,
\]
whereas each connected sum reduces \(2\chi+3\tau\) by \(4\). Thus
\[
(2\chi+3\tau)(X\sqcup kY)=A+3k,\qquad
(2\chi+3\tau)(X\#kY)=A-k.
\]
This is precisely a difference of \(4k\) units.

If \(X\) has a negative Kähler–Einstein metric normalized by \(s=-4\), and \(Y\) its reversed complex-hyperbolic Einstein metric at the same normalization, the full pieces have
\[
\operatorname{Vol}(X)=2\pi^2 A,\qquad
\operatorname{Vol}(Y)=18\pi^2.
\]
Their disconnected bulk totals give \(\kappa=0,\ \upsilon=9k\), not \((2k,5k)\). Inserting these totals into the *connected-sum* identity gives \(p=4k\).

Thus the formal zero-cost mixture contains a Kähler bulk of volume \(2\pi^2(A-4k)\), not the complete Einstein host \(X\). It has already removed or redistributed host bulk curvature. One cannot identify it with \(X\sqcup kY\) and then regard joining as the only omitted datum.

Moreover, \(\overline{\mathrm{FPP}}\) admits no almost complex structure inducing its reversed orientation: its rank-one negative intersection form cannot contain a class with
\[
c_1^2=2\chi+3\tau=3.
\]
It remains a legitimate ASD Einstein metric competitor, but not a closed almost-Kähler realization of the formal patch.

Finally, the Step-62 implication
\[
p/k\to0\ \Longrightarrow\ \kappa/k\to1
\]
is not justified: \(k-\kappa\) can be negative and cancel \((\upsilon-\kappa)/3\). The formal \((\kappa,\upsilon)=(2k,5k)\) model illustrates exactly this cancellation.

---

## 2. Exact localized Chern–Weil formula

For a compact oriented four-manifold \(U\) with boundary, define the boundary corrections by
\[
8\pi^2\chi(U)
=
\int_U\left(|W|^2-\frac12|\operatorname{Ric}^{\circ}|^2+\frac{s^2}{24}\right)
+\mathcal E_{\partial U},
\]
\[
12\pi^2\tau(U)
=
\int_U\left(|W^+|^2-|W^-|^2\right)
+\mathcal S_{\partial U}.
\]
Here \(\mathcal E\) is the Gauss–Bonnet boundary term; \(\mathcal S\) includes the appropriate signature boundary correction, including the eta contribution when formulated through APS. A bare, unframed local Chern–Simons integral is not generally a substitute for \(\mathcal S\).

Put
\[
\mathfrak b(\partial U)=\mathcal E_{\partial U}+\mathcal S_{\partial U}.
\]
Then
\[
\boxed{
P(U)=Q(U)-8\pi^2(2\chi(U)+3\tau(U))+2\mathfrak b(\partial U).
}
\tag{1}
\]

For
\[
U\cong \left(\#_{j=1}^{m}\overline{\mathbf{CP}}^{\,2}\right)\setminus B^4,
\]
one has \(\chi(U)=m+1,\ \tau(U)=-m\), hence
\[
\boxed{
P(U)=Q(U)+8\pi^2(m-2)+2\mathfrak b(\partial U).
}
\tag{2}
\]
In particular, for every such metric and every \(\delta\ge0\),
\[
\mathfrak b(\partial U)\ge8\pi^2-\delta
\quad\Longrightarrow\quad
\boxed{P(U)\ge8\pi^2m-2\delta.}
\tag{3}
\]

This is a rigorous relative wall estimate. Its input is a geometric boundary invariant, not an assumed relation between twist and Ricci energy.

### An explicit finite-scale theorem: replacement of a Kähler–Einstein ball

Let \(B\) be a smooth ball in a reference metric \(h\), and identify its boundary with that of \(U\). Suppose their oriented boundary data satisfy
\[
|\mathfrak b_g(\partial U)-\mathfrak b_h(\partial B)|\le\delta.
\]
Subtracting (1) for \(U\) and \(B\) gives
\[
P_g(U)
=
8\pi^2m+Q_g(U)-Q_h(B)+P_h(B)
+2\bigl(\mathfrak b_g-\mathfrak b_h\bigr).
\]
Therefore
\[
\boxed{P_g(U)\ge8\pi^2m-Q_h(B)-2\delta.}
\tag{4}
\]

For a negative Kähler–Einstein reference with \(s=-4\),
\[
|W^+|^2=\frac23,\qquad Q_h(B)=4\operatorname{Vol}_h(B),
\]
so
\[
\boxed{
P_g(U)\ge8\pi^2m-4\operatorname{Vol}_h(B)-2\delta.
}
\tag{5}
\]

Matching the induced metric and second fundamental form exactly gives \(\delta=0\). For one exceptional cap,
\[
\operatorname{Vol}_h(B)\le\pi^2,\quad \delta=0
\quad\Longrightarrow\quad
\boxed{P_g(U)\ge \tfrac12\,8\pi^2.}
\tag{6}
\]
More generally, the explicit coefficient is
\[
c=1-\frac{\operatorname{Vol}_h(B)}{2\pi^2m}
-\frac{\delta}{4\pi^2m}.
\]

This theorem permits an arbitrarily complicated or fat interior transition. If an interior core \(C\subset U\) is already known to satisfy \(P(C)\le\varepsilon\), then the actual wall \(U\setminus C\) satisfies the same lower bound minus \(\varepsilon\).

It also explains how an exceptional insertion can save slightly below the unit tariff: it replaces a reference ball with positive \(Q_h(B)\). That saving is bounded by the removed reference bulk and the boundary error.

---

## 3. AE limits give exact tariffs

Assume complete AE metrics with finite curvature energy and sufficient decay for the boundary limits.

### One-ended exceptional bubble

For a single trivial \(S^3\) AE end,
\[
\mathfrak b(S_R^3)\longrightarrow8\pi^2.
\]
Equation (2) yields
\[
\boxed{
P=8\pi^2m+4\int|W^+|^2+\frac1{12}\int s^2
\ge8\pi^2m.
}
\tag{7}
\]
A scalar-flat ASD Burns bubble realizes the \(m=1\) equality.

The same formula applies to a punctured reversed FPP: its puncture has \(\chi=2,\tau=-1\). Thus **a one-ended AE realization of that competitor cannot cost less than \(8\pi^2\)**.

For a bubbling sequence, the corresponding defect-measure lower bound requires convergence on an exhaustion of the complete bubble and lower semicontinuity; topology alone does not assert that such a bubble forms.

### Two-ended neck

Gauss–Bonnet gives, for \(n\) trivial AE ends,
\[
P=2\int|W|^2+\frac1{12}\int s^2+16\pi^2(n-\chi).
\]
For \(S^3\times\mathbb R\),
\[
\boxed{P\ge32\pi^2.}
\tag{8}
\]
This constant is sharp: the conformally flat scalar-flat metric
\[
g=\left(1+\frac{a}{r^2}\right)^2g_{\mathbb R^4},\qquad a>0,
\]
has two AE ends and realizes equality.

For a rotationally symmetric collar
\[
g=dt^2+f(t)^2g_{S^3},
\]
direct computation gives
\[
\boxed{
P=6\pi^2\int
\frac{(f'^2-ff''-1)^2}{f}\,dt.
}
\tag{9}
\]
A longer collar is not automatically cheaper: a nearly cylindrical segment of radius \(f_0\) and length \(L\) contributes approximately \(6\pi^2L/f_0\). Any proposed cheap heteroclinic must satisfy the actual metric equations, not merely interpolate \(u\) and Weyl eigenvalues independently.

---

## 4. What the twist estimate does—and does not—prove

For an arbitrary orthogonal \(J\),
\[
\gamma_J^-=\rho_0^J+t,\qquad t=(\alpha\wedge\beta)^-,
\]
and
\[
\|\rho_0^J\|_2\le\sqrt{P/2},\qquad
\|t\|_2^2\le\frac1{32}\int|\nabla\Omega|^4.
\]

On the closed manifold, for the selected best sign class,
\[
\sqrt{P/2}+\|t\|_2\ge2\pi\sqrt{k+\Pi}.
\]
The exceptional lower bound is not a statement about every possible \(c_1(J)\); it applies to the chosen class and every \(J\) realizing that class.

If a localized twist norm is assumed to carry one unit,
\[
\|t\|_{L^2(U)}\ge2\pi(1-\delta),
\]
then
\[
\boxed{
\int_U|\nabla\Omega|^4\ge128\pi^2(1-\delta)^2.
}
\tag{10}
\]
This is a torsion-energy lower bound, not a Ricci-energy lower bound.

### Local flux requires relative data

A period
\[
\int_{S_e}\gamma_J=2\pi
\]
does not alone imply \(\|\gamma_J^-\|_{L^2(U)}\ge2\pi\). The closed-manifold Hodge argument does not localize without boundary conditions.

One valid localized formulation is to provide an ASD test form \(\zeta\) on \(U\), with \(\|\zeta\|_2=1\), satisfying
\[
\left|\int_U\langle\gamma_J^-,\zeta\rangle\right|\ge2\pi(1-\delta).
\]
Then
\[
\sqrt{P(U)/2}+\|t\|_{L^2(U)}\ge2\pi(1-\delta).
\tag{11}
\]
Constructing such a test from the exceptional topology is itself part of the relative problem.

The proposed expression \(2\pi=\int d\chi\wedge\gamma_J\) is not a four-dimensional flux identity: its integrand is a three-form. Also, \(t\) is generally not closed. Neither a conserved twist current nor the proposed monotonicity law has been established.

### A sufficient coercivity estimate with an explicit constant

Suppose a specified class of walls satisfies
\[
\|t\|_{L^2(U)}\le\sqrt{C\,P(U)}+r,
\qquad r<2\pi(1-\delta).
\tag{12}
\]
Combining with (11),
\[
\boxed{
P(U)\ge
\frac{(2\pi(1-\delta)-r)^2}
{(1/\sqrt2+\sqrt C)^2}.
}
\tag{13}
\]
For \(\delta=r=0\), this is \(P(U)\ge c\,8\pi^2\), with
\[
\boxed{c=\frac1{(1+\sqrt{2C})^2}.}
\]

However, (12) is false for arbitrary \(J\), even on an Einstein metric. For example, an equal-Einstein-constant hyperbolic product
\[
\Sigma_{m+1}\times\Sigma_{n+1}
\]
has \(P=0\). Characteristic classes \(c=2r\,a+2s\,b\) with \(rs=mn\) satisfy the almost-complex Chern-number condition; suitable choices have \(c_g^-\ne0\). An orthogonal representative \(J\) then carries all its ASD Chern flux through twist. One may arrange that \(J\) agrees with the parallel product structure on a small ball. This refutes arbitrary-\(J\) twist coercivity, though not a theorem requiring a genuine ASD inner phase.

For \(J\) obtained from a SW spinor, the unresolved analytic quantity is the **unweighted** critical norm
\[
\int\left|\nabla\frac{\psi}{|\psi|}\right|^4.
\]
The usual weighted spinor-gradient estimates do not supply it near zeros of \(\psi\).

### Critical capacity does not give a universal rotation tension

On a Euclidean annulus, choose parallel orthogonal forms \(\Omega_0,\Omega_1\) of norm \(\sqrt2\), and set
\[
\Omega=\cos\theta(r)\Omega_0+\sin\theta(r)\Omega_1,\qquad
\theta(r)=\frac{\Delta\theta}{L}\log(r/r_0),\quad L=\log(R/r_0).
\]
Then
\[
\boxed{\int|\nabla\Omega|^4=\frac{8\pi^2(\Delta\theta)^4}{L^3}.}
\tag{14}
\]
This tends to zero as \(L\to\infty\), and the one-parameter rotation has \(\alpha\wedge\beta=0\). Changing frames is cheap; transporting a nontrivial relative Chern charge is a different operation.

---

## 5. Nijenhuis zeros: obstruction to exact equality, not yet wall energy

For an almost-Kähler four-manifold,
\[
N_J\in\Gamma(E),\qquad E=T^{1,0}\otimes K_J^{-1},
\]
and
\[
c_2(E)=5\chi+6\tau=c_2(X)+2A-k.
\tag{15}
\]
This excludes a globally nowhere-zero Nijenhuis tensor in the stated range and hence excludes the constant positive-torsion equality configuration.

It does **not** force one charged zero per exceptional summand:

* the number in (15) decreases under blow-up;
* a Kähler exterior has \(N_J\equiv0\) on an open set, not isolated transverse zeros;
* zeros can occur where their amplitudes and associated derivative energies are arbitrarily small unless an additional equation prevents this.

There is a precise relative topological quantity. With a fixed trivialization of \(E|_Y\) and \(N_J\ne0\) on \(Y\),
\[
\widehat N:Y\to S^3
\]
has degree \(d\), and
\[
\boxed{\int_Y|d\widehat N|^3\ge6\sqrt3\,\pi^2|d|.}
\tag{16}
\]
The degree depends on the relative trivialization. To obtain a wall tariff one must prove both:

1. exceptional flux transfer forces a nonzero relative degree;
2. the degree energy is controlled by \(P\), with boundary, torsion-amplitude, and Sobolev constants controlled.

Neither follows from (15). An AAD-derived estimate for \(\nabla N\), together with a trace inequality and a boundary lower bound for \(|N|\), could supply the second implication. It would still need the first.

---

## 6. Why transgression is the decisive missing estimate

For exceptional caps, a particularly economical target is
\[
\boxed{
(8\pi^2-\mathfrak b(\partial U))_+
\le q\,P(U\cup A)+\varepsilon,
}
\tag{17}
\]
where \(A\) is the exterior transition collar and the quantifiers specify the permitted geometry and phase errors. Equation (2) then implies
\[
\boxed{
P(U\cup A)\ge\frac{8\pi^2m-2\varepsilon}{1+2q}.
}
\tag{18}
\]
Every finite uniform \(q\) gives an explicit positive tariff.

Near an AE boundary, or near the boundary of a sufficiently small Kähler–Einstein reference ball, this mechanism is already implemented by (3)–(6). For a general fat interface, (17) is unproved.

Chern–Simons differences alone do not prove (17). They constrain signed curvature integrals, not a positive path action. In the chiral Levi-Civita representation, tracefree Ricci is the wrong-chirality curvature component. A general connection can carry topological charge entirely in the unpenalized chirality. The essential extra restriction is that the connection comes from a metric, with the specified scalar and phase data.

Likewise, the almost-Kähler identity (63.3) cannot be applied to an arbitrary subdomain without its characteristic transgression. A relative canonical \(U(1)\) charge is not automatically
\(\int_U\gamma_J^2=-4\pi^2\); boundary trivializations and boundary terms must first be fixed.

The suggested \(c=1/3\) “finite-amplitude efficiency” argument is therefore only arithmetic conditional on a new inequality. The Burns derivative \(\upsilon\approx4\kappa\) near a particular small insertion does not imply \(\upsilon\ge4\kappa\) at finite amplitude, and a parameter path of metrics does not measure the spatial wall cost. No \(c=1/3\) theorem follows from that calculation.

### A concrete cheap-transition model—and its limitation

Collapsed complex-hyperbolic cusp collars explain why phase labels alone should not have universal tension. In cusp coordinates,
\[
g=dt^2+e^{-2t}(\sigma_1^2+\sigma_2^2)+e^{-4t}\sigma_3^2,
\]
with the nilpotent structure equation \(d\sigma_3\) proportional to \(\sigma_1\wedge\sigma_2\). At depth \(T\), a fixed-length reflected collar can be smoothed while keeping curvature bounded; its volume is \(O(e^{-4T})\). Thus
\[
P_{\rm collar}=O(e^{-4T})\to0.
\tag{19}
\]
Where orientation-compatible cusp identifications exist, the two sides can have Kähler-type and reversed-complex-hyperbolic ASD Weyl phases.

This is a cheap joining mechanism for **collapsed cusp interfaces**, not an exceptional \(S^3\) cap with the prescribed global \(J\)-flux. It does not resolve the requested connected-sum problem. It shows exactly what an unrestricted phase-only theorem overlooks: interface collapse and boundary transgression.

---

## 7. The reversed-FPP competitor and the remaining decision problem

The proved cap estimates do not distinguish \(\overline{\mathbf{CP}}^{\,2}\) from \(\overline{\mathrm{FPP}}\): both punctures have \((\chi,\tau)=(2,-1)\). Consequently:

* one-ended AE bubbles cost at least \(8\pi^2\) each;
* two-ended AE joins cost at least \(32\pi^2\) each;
* attachments replacing small Kähler–Einstein balls obey (5);
* a sub-unit construction must leave these controlled-interface regimes.

Neither the supplied SW inequalities nor the formal bulk model decides
\[
\alpha(X\#k\overline{\mathrm{FPP}})<8\pi^2k.
\]
Any use of a generalized SW blow-up formula for the FPP summand also requires an actual theorem with its hypotheses checked. Equality of rational intersection forms is insufficient.

Two concrete variational objects can decide the issue.

**Exceptional filling problem.** For prescribed boundary metric and second fundamental form \((h,L)\), calculate
\[
I_U(h,L)=\inf\{P_g(U):g|_{\partial U}=h,\ L_g=L\}.
\]
For an exceptional cap, (2) fixes the topological and boundary terms:
\[
I_U(h,L)=8\pi^2(m-2)+2\mathfrak b(h,L)+\inf_g Q_g(U).
\tag{20}
\]
This separates the computable boundary contribution from the genuine metric-filling problem. A biaxial Bianchi IX exceptional bolt with CH-type outer boundary data gives a tractable restricted version, but a reversed FPP cannot be modeled by that symmetric cap merely because its Chern numbers agree.

**Host-plus-filling problem.** Vary the cut surface in the host and the filling simultaneously, including the host deformation cost. This is necessary because a cheap filling obtained by changing \((h,L)\) may simply move the missing cost outside \(U\).

The precise unrestricted theorem still needed is a bound such as (17), or the relative twist coercivity (12), for all near-minimizers with their actual boundary geometry and a canonically selected \(J\). Conversely, a genuine cheap-fat-wall counterexample must exhibit metrics with verified curvature, compatible boundary jets, exceptional topology, and the specified relative flux—not merely an interpolating torsion profile.

**The strongest established advance is (5):**
\[
\boxed{
P(\text{exceptional cap})\ge
8\pi^2m-4\,\operatorname{Vol}(\text{replaced KE ball})
-2\,(\text{boundary-transgression error}).
}
\]
It gives explicit positive constants, covers fat interiors, and isolates the sole remaining escape in this formulation: a large change in host bulk or boundary transgression whose cost has not yet been controlled.