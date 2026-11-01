# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step91_separator_stability_and_barriers.md",
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md",
    "Sessions/S0910A03/workspace/data/step92_jacobi_concentration_models.json",
    "Sessions/S0910A03/workspace/data/step92_weighted_jacobi_transform.json"
  ]
}
```

## Task

The active Yau-26 subproblem is a free T^2-invariant two-ended approximately negative-Einstein connector. At its invariant minimizing separator C, let rho=e^sigma, s be base arclength, V=|II|^2=kappa^2+h_nu^2/2+e_nu/2+Q, h=sigma_s, and e_s=|U_s|^2. The verified formulas are: (i) for every smooth periodic phi, ∫rho V phi^2 <= ∫rho[(phi_s)^2+(3-E_nunu)phi^2]; (ii) R_q=-2h_s-(3/2)h^2-e_s/2; (iii) minimal Gauss R_q=-6+D-V, |D|<=4delta; (iv) Maxwell dq=±2rho * E_mix, with normalized |b|<=2sqrt(2)delta, and Q=(1/2)e^{-3sigma}q^T M^{-1}q; (v) orbit equation tau_sigma(U)=-grad Q+Z, |Z|<=2delta. Develop the strongest mathematically valid interaction among the full Jacobi form, scalar identity, Maxwell transport, and orbit equation. Look especially for a new nonlocal inequality that controls concentration of Q or e_nu on C, or else give an explicit formal/local-data mechanism showing why these equations still permit concentration. Keep all hypotheses and identify exact missing bridge; do not infer a pointwise bound from stability.

## Output

### 1. Exact conjugation of the full Jacobi form

Let \(L_C=\operatorname{Length}_{\gamma_B}(C)\), and choose an orthonormal frame
\((T,V_1,V_2,\nu)\) along the lifted separator. Write
\[
T_E:=E(T,T)+E(V_1,V_1)+E(V_2,V_2),
\qquad D=T_E-E(\nu,\nu).
\]
For an arbitrary smooth periodic \(y\), set
\[
\phi=e^{-\sigma/2}y=\rho^{-1/2}y.
\]
Then
\[
\int_C\rho\,\phi_s^2\,ds
=\int_C\left(y_s^2+\frac12h_s y^2+\frac14h^2y^2\right)ds.
\]
The scalar and Gauss identities give
\[
h_s
=3-\frac D2+\frac V2-\frac34h^2-\frac14e_s.
\]
Substitution into the Jacobi form yields the exact unweighted Schrödinger form
\[
\boxed{
\int_C\left[
y_s^2+
\left(
\frac92-E(\nu,\nu)-\frac D4
-\frac34V-\frac18(h^2+e_s)
\right)y^2
\right]ds\ge0.}
\tag{1}
\]
Equivalently, with
\[
\mathcal W:=\frac34V+\frac18(h^2+e_s),
\qquad
A(s):=\frac92-E(\nu,\nu)-\frac D4,
\]
one has
\[
\int_C\mathcal W y^2\,ds
\le
\int_C\bigl(y_s^2+A(s)y^2\bigr)\,ds.
\tag{2}
\]
The correlation between \(D\) and \(E(\nu,\nu)\) improves the coarse coefficient:
\[
A=\frac92-\frac14T_E-\frac34E(\nu,\nu)
\le a_\delta:=\frac92+\frac32\delta.
\tag{3}
\]
Thus
\[
\boxed{
\int_C\mathcal W y^2\,ds
\le
\int_C\bigl(y_s^2+a_\delta y^2\bigr)\,ds
\quad\text{for every periodic }y.}
\tag{4}
\]

This is stronger than the constant test in two ways: it removes the possibly highly varying weight \(\rho\), and it places \(V,h^2,e_s\) in one common Schrödinger potential.

Taking \(y=1\) and also using the integrated scalar identity gives
\[
\boxed{
\frac54\int_C h^2\,ds+\frac12\int_Ce_s\,ds
\le 9L_C-\int_C T_E\,ds
\le(9+3\delta)L_C.}
\tag{5}
\]
Furthermore,
\[
\int_CV\,ds
=-6L_C+\int_CD\,ds
+\frac32\int_Ch^2\,ds+\frac12\int_Ce_s\,ds,
\]
and optimizing under (5) gives
\[
\boxed{
\int_CV\,ds
\le
\left(\frac{24}{5}+\frac{8}{5}\delta\right)L_C.}
\tag{6}
\]

### 2. A genuine nonlocal concentration inequality

Let
\[
H_\delta=-\partial_s^2+a_\delta
\]
on the periodic circle \(C\). Equation (4) is equivalent to
\[
\boxed{
\left\|
\mathcal W^{1/2}H_\delta^{-1}\mathcal W^{1/2}
\right\|_{L^2\to L^2}\le1.}
\tag{7}
\]
If \(G_\delta(s,t)\) denotes the periodic Green kernel of \(H_\delta\), then
\[
G_\delta(s,t)
=
\frac{
\cosh\!\left(\sqrt{a_\delta}\,
\bigl(L_C/2-d_C(s,t)\bigr)\right)}
{2\sqrt{a_\delta}\sinh(\sqrt{a_\delta}L_C/2)}.
\]
Testing (7) with \(\mathcal W^{1/2}\) gives
\[
\boxed{
\iint_{C\times C}
G_\delta(s,t)\mathcal W(s)\mathcal W(t)\,ds\,dt
\le\int_C\mathcal W\,ds.}
\tag{8}
\]
Since
\[
\mathcal W\ge\frac34Q,
\qquad
\mathcal W\ge\frac38e_\nu,
\]
one separately obtains
\[
\boxed{
\iint G_\delta(s,t)Q(s)Q(t)\,ds\,dt
\le\frac43\int_CQ\,ds,}
\tag{9}
\]
and
\[
\boxed{
\iint G_\delta(s,t)e_\nu(s)e_\nu(t)\,ds\,dt
\le\frac83\int_Ce_\nu\,ds.}
\tag{10}
\]
For example, if \(Q_j\,ds\) converges to an atom of mass \(m\) at \(s_0\), then
\[
m\le
\frac{1}{(3/4)G_\delta(s_0,s_0)}
=
\frac{8\sqrt{a_\delta}}{3}
\tanh\!\left(\frac{\sqrt{a_\delta}L_C}{2}\right).
\tag{11}
\]
Thus arbitrarily thin \(Q\)-spikes can carry only uniformly bounded mass. Equation (11) by itself still permits height proportional to inverse width.

A local version follows from the periodic tent function. For \(0<r\le L_C/2\), let \(I_r\) be the arc \(|s-s_0|\le r/2\). Then
\[
\boxed{
\int_{I_r}\mathcal W\,ds
\le
M_\delta(r):=\frac8r+\frac83a_\delta r.}
\tag{12}
\]
Consequently,
\[
\int_{I_r}Q\,ds\le\frac43M_\delta(r),\qquad
\int_{I_r}e_\nu\,ds\le\frac83M_\delta(r),
\tag{13}
\]
and
\[
\int_{I_r}(h^2+e_s)\,ds\le8M_\delta(r).
\tag{14}
\]
The \(r^{-1}\) term is the one-dimensional capacity scale; it leaves room for \(e_\nu\) height of order \(r^{-1}\).

### 3. Maxwell transport converts the form estimate into a universal separator bound for \(Q\)

Put \(w=\sqrt{2Q}\). Differentiating the invariant expression for \(Q\) and using the Maxwell equation gives, along \(C\),
\[
\left|w_s+\frac32hw\right|
\le\frac12w\sqrt{e_s}+B_\delta,
\qquad B_\delta:=2\sqrt2\,\delta.
\tag{15}
\]
Hence
\[
|w_s|\le c(s)w+B_\delta,
\qquad
c(s):=\frac32|h|+\frac12\sqrt{e_s},
\tag{16}
\]
with
\[
c(s)^2\le\frac52(h^2+e_s).
\tag{17}
\]

Equations (12)–(17) furnish a universal pointwise estimate on \(Q|_C\). An explicit version is as follows. If \(L_C\ge2/\sqrt{a_\delta}\), center the tent at a maximum of \(Q\) and take \(r=a_\delta^{-1/2}\). Then
\[
M_\delta(r)=\frac{32}{3}\sqrt{a_\delta}.
\]
Inside the central arc there is a point \(s_0\) with
\[
Q(s_0)\le\frac{128}{9}a_\delta.
\]
The distance from \(s_0\) to the maximum is at most \(r/2\), while
\[
\int c\,ds\le\sqrt{\frac{320}{3}}.
\]
Gronwall’s inequality therefore gives
\[
\boxed{
\sup_CQ
\le
\frac12
\exp\!\left(2\sqrt{\frac{320}{3}}\right)
\left(
\frac{16}{3}\sqrt{a_\delta}
+\frac{\sqrt2\,\delta}{\sqrt{a_\delta}}
\right)^2.}
\tag{18}
\]

If \(L_C<2/\sqrt{a_\delta}\), use \(y=1\) in (4). There is \(s_0\in C\) with
\[
Q(s_0)\le\frac43a_\delta,
\]
and transport along the shorter arc gives
\[
\boxed{
\sup_CQ
\le
\frac12e^{4\sqrt{10}}
\left(
\sqrt{\frac{8a_\delta}{3}}
+\frac{2\sqrt2\,\delta}{\sqrt{a_\delta}}
\right)^2.}
\tag{19}
\]
Taking the larger right-hand side in (18)–(19) yields a constant depending only on \(\delta\). The numerical size is very coarse, but the mechanism is structural:

* the conjugated Jacobi form controls local \(L^1\) mass of \(Q,h^2,e_s\);
* Maxwell transport forces a high value of \(Q\) to communicate with nearby values through \(h\) and \(U_s\);
* the same local form controls the transport cost.

Thus arbitrary \(Q\)-height on the separator is incompatible with the five displayed relations. This conclusion uses scalar geometry and Maxwell transport in addition to stability.

### 4. The orbit equation still permits arbitrary concentration of \(e_\nu\) at the level of separator jets

There is no analogous first-order transport equation for \(e_\nu=|U_\nu|^2\). The orbit equation is a trace equation:
\[
\nabla_sU_s+\nabla_\nu U_\nu
+\text{terms depending on first jets}
=-\nabla Q+Z.
\tag{20}
\]
Along one curve it determines the second normal jet \(\nabla_\nu U_\nu\); it does not control the first normal jet \(U_\nu\), nor \(\nabla_sU_\nu\).

This can be seen through an explicit formal family satisfying all five displayed relations on \(C\). Fix a circle of length \(L\), and put
\[
m_*:=2\sqrt3\,\tanh\!\left(\frac{\sqrt3L}{2}\right).
\]
Choose \(0<m<m_*\), and smooth bumps
\[
P_\ell(s)=\frac{m}{\ell}\chi(s/\ell),
\qquad
\chi=\eta^2\ge0,\quad \int\chi=1.
\]
For sufficiently small \(\ell\),
\[
-\partial_s^2+3-P_\ell
\]
has quadratic form \(\ge0\). This follows from convergence to the periodic point interaction \(m\delta_0\), whose zero-energy threshold is exactly \(m_*\).

Now prescribe on \(C\)
\[
\rho=1,\quad h=0,\quad E(\nu,\nu)=D=0,
\]
\[
q=Q=b=0,\qquad
\kappa=h_\nu=0,
\]
and
\[
e_\nu=2P_\ell,\qquad
V=P_\ell,\qquad
e_s=12+2P_\ell.
\tag{21}
\]
Then
\[
R_q=-\frac12e_s=-6-P_\ell=-6+D-V,
\]
and the Jacobi form becomes exactly
\[
\int_C P_\ell\phi^2\,ds
\le
\int_C(\phi_s^2+3\phi^2)\,ds.
\]
The Maxwell equation is trivial.

The target jets can also be realized. Choose a closed immersed curve in \(\mathbb H^2\) parameterized with speed
\[
|U_s|=\sqrt{12+2P_\ell},
\]
choose a smooth vector field \(U_\nu\) along it with
\[
|U_\nu|=\sqrt{2P_\ell},
\]
and prescribe the second normal jet so that
\[
\nabla_\nu U_\nu=-\nabla_sU_s
\]
in Fermi coordinates. This realizes \(\tau_\sigma(U)=0\), hence the orbit equation with \(Q=Z=0\).

Therefore
\[
\sup_Ce_\nu
\asymp\ell^{-1}\longrightarrow\infty,
\qquad
\int_Ce_\nu\,ds\longrightarrow2m,
\]
while the full Jacobi form, scalar identity, Gauss identity, Maxwell equation, and orbit equation all hold along the separator. This is a formal first/second-jet construction; extending it to a tubular invariant metric also brings in the remaining reduced horizontal equations and Codazzi–Bianchi relations.

### 5. Exact missing bridge for the two-ended connector

The new estimate controls \(Q\) on \(C\), not
\[
Q_+=\sup_BQ.
\]
Normal Maxwell transport reads
\[
\left|\partial_\nu w+\frac32h_\nu w\right|
\le\frac12w\sqrt{e_\nu}+B_\delta.
\tag{22}
\]
Propagation from \(C\) into the base would require control of
\[
\int_{\text{normal arc}}
\left(|h_\nu|+\sqrt{e_\nu}\right)\,dn.
\tag{23}
\]
The separator form supplies only \(s\)-direction capacity estimates at \(n=0\); it supplies no tubular estimate of (23). The orbit equation cannot provide one because its normal second derivative can absorb arbitrarily concentrated \(U_\nu\).

The missing geometric substance is therefore a collar estimate controlling \(U_\nu\) or \(D_sU_\nu\), such as a two-dimensional Bochner estimate for \(|dU|^2\) with controlled flux on two nearby slices, a Codazzi estimate for the separator’s second fundamental form, or a tubular integral estimate for \(|DdU|^2\). Moreover, the Maxwell source estimate controls \(|b|\) but not \(Db\), so a second-order scalar equation for \(Q\) also requires source regularity not present in the supplied hypotheses.

In summary: the combined Jacobi–scalar–Maxwell system does give a dimensionless pointwise bound for \(Q|_C\) and the Birman–Schwinger inequalities (8)–(10), while \(e_\nu\) can still form arbitrarily high, vanishing-width separator spikes at the level of the displayed equations. The unresolved passage is from separator data to a two-dimensional collar and then to \(Q_+\) on the full base.