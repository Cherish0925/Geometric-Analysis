# TTCS Independent Branch Record

```json
{
  "step_id": 42,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step41_symplectic_closure_bolt_layer_and_new_inputs.md",
    "Sessions/S1003A02/workspace/notes/step47_consolidation_two_scale_program.md",
    "Skills/geometric-analysis/research/paper/sections/finite_density_endpoint.tex",
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex",
    "Knowledge/materials/openai-math-20261007/continuation/20261007_openai_math_connections/connections.md"
  ]
}
```

## Task

The active goal is a unified Einstein-gap theory. Compare two central unresolved routes using the supplied exact mathematics, not generic suggestions. Route A is density-free O10 after resetting the actual budget to p: any escape has chi/p→∞, p/V→2/(9pi^2), W-/V→∞; the finite-density proof constructs an actual L^5 section of asymptotically nonzero modulus whose Chern square density stays positive, but W- enters its derivative/second-jet control. Investigate whether the section's zero/phase geometry, a localized Chern transgression, Bianchi identities, or the positive-current mechanism can yield a genuinely new density-independent estimate. State the strongest exact identity or conditional theorem that looks derivable, and identify the precise mathematical quantity still uncontrolled. Route B is O11 after the certified sub-four cell and symplectic closure: generic near-minimizer selection remains valid but the old unit-tariff instability target is false; compare a corrected minimizer-entry/global-comparison route with a diffuse k^2/A transport route. Determine which route presently has the best chance of a major theorem, and formulate a concrete proof object that accommodates the certified construction rather than restoring coefficient four. Do not invent literature or assume compactness/noncollapse.

## Output

## Comparative assessment

The two routes are now at very different mathematical stages.

* **Route A has a sharp density-independent concentration statement within reach.** The finite-density proof can be reorganized so that the total quantity \(W_-/V\) is replaced by one compressed curvature action on the actual opposite-spinor first jet. Any O10 escape must make that compressed action diverge. The zero-set, phase, and current pictures explain where the topology can hide, but by themselves they do not exclude it.
* **Route B has the stronger path to a new Einstein-gap theorem.** The exact saving identities already identify a linear transport demand, near-minimizers can be selected at the smaller \(k^{2}/A\) scale, and one quadratic transport estimate would yield an all-metric lower bound of that order. This is compatible with the certified sub-unit cell and its symplectic perturbations. A full minimizer-entry/global-comparison theorem should combine localized core costs with this diffuse transport law rather than assign unit cost to every exceptional class.

---

# A. Density-free O10: what can be extracted without controlling \(W_-/V\)

Work on the scalar-\(-4\) representative and normalize integrals by
\(\mu_j=d\mu_{g_j}/V_j\). After resetting the actual budget to \(p_j\), an endpoint escape has

\[
\frac{P_j}{V_j}\to0,\qquad
\frac{p_j}{V_j}\to\frac{2}{9\pi^2},\qquad
\frac{a_j^2}{V_j}\to\frac1{6\pi^2},
\qquad
\frac{W^-_j}{V_j}\to\infty.
\]

The strong-current construction, which does not use an Euler-density bound, still supplies

\[
\rho_j\to \rho_*=\frac43,\qquad
|t_j|^2\to m_*=\frac{128}{81},
\]

the determinant-curvature fit

\[
-iF_{\mathcal A_j}=F_{0,j}+r_{F,j},
\qquad |F_{0,j}|\le C,\qquad \|r_{F,j}\|_2\to0,
\]

and the bounded direct resolvent \(v_j\in\Gamma(E_{-,j})\),

\[
(4+\mathcal L_j)v_j=6z_j,\qquad
|v_j|\le6,\qquad |\mathcal L_jv_j|\le48,
\]

with

\[
\|v_j-t_j\|_{H^1}\to0,\qquad
\|D^-_{3\mathcal A_j}v_j\|_2\to0,\qquad
\|(\mathcal L_j-2)v_j\|_2\to0.
\]

The first point at which \(W^-\) is essential is the second-jet estimate for \(v_j\).

## A.1 The precise curvature action that remains uncontrolled

Apply the covariant Hodge–Weitzenböck identity to \(\nabla v_j\). The curvature of \(E_-=S^-\otimes L\) contains \(W^-_j\), while the scalar block, \(W^+_j\), \(\operatorname{Ric}^\circ_j\), and determinant-curvature remainder are bounded or tend to zero in the required normalized \(L^2\) spaces. Using the boundedness of \(v_j\), the interpolation

\[
\fint |\nabla v_j|^4\le C\fint|\nabla^2v_j|^2,
\]

and absorption of the small curvature remainders gives the estimate

\[
\fint\left(|\nabla^2v_j|^2+|\nabla v_j|^4\right)
\le
C\left[
1+
\fint
\bigl(\mathcal Q(W^-_j,\nabla v_j)\bigr)_+
\right],
\tag{A.1}
\]

where \(\mathcal Q(W^-,\nabla v)\) is the explicit curvature-action contraction arising from the commutator on the covector and \(S^-\) slots, and

\[
|\mathcal Q(W^-,\nabla v)|
\le C|W^-|\,|\nabla v|^2.
\tag{A.2}
\]

Thus a convenient sufficient quantity is

\[
\mathfrak W_j
:=
\fint |W^-_j|\,|\nabla v_j|^2.
\tag{A.3}
\]

This is substantially sharper than \(W^-_j/V_j=\fint|W^-_j|^2\). It measures whether the ASD Weyl concentration acts on the particular first jet selected by the actual field equations.

### Conditional density-independent endpoint theorem

A direct replacement of the finite-density Hessian step gives:

> **Conditional theorem.** No O10 endpoint escape can satisfy
> \[
> \sup_j\mathfrak W_j<\infty.
> \tag{A.4}
> \]
> Consequently every such escape must obey
> \[
> \boxed{\fint |W^-_j|\,|\nabla v_j|^2\longrightarrow\infty.}
> \tag{A.5}
> \]
> More precisely, it is enough that the positive part of the compressed action in (A.1) remain bounded.

Indeed, (A.4) and (A.1) provide

\[
\|\nabla^2v_j\|_2+\|\nabla v_j\|_4^2\le C.
\]

The mass-gradient, phase, Dirac-projection, and covariance arguments then proceed exactly as in the finite-density proof. They produce

\[
|\nabla v_j|^2\to2m_*
\quad\text{in measure},
\]

identify the unique surviving complex derivative, and yield the fifth-power section

\[
\sigma_j=\Phi_j\wedge t(v_j)\in\Gamma(L_j^5)
\]

with

\[
|\sigma_j|^2\longrightarrow
\ell_\sigma^2:=4\rho_*m_*^3>0
\quad\text{in normalized measure},
\qquad
\|\nabla_{5\mathcal A_j}\sigma_j\|_2\le C.
\]

The logarithmic line resolvent then gives

\[
\frac{c_1(L_j^5)^2[M_j]}{V_j}\to0,
\]

whereas topology and the actual field equations give

\[
\frac{c_1(L_j^5)^2[M_j]}{V_j}
=
25\frac{a_j^2}{V_j}
\longrightarrow\frac{25}{6\pi^2}.
\]

This proves (A.5). It is a genuine density-independent concentration theorem: any surviving escape must align the diverging ASD Weyl curvature with the actual opposite-spinor derivative.

## A.2 Exact localized phase transgression

The fifth-line construction also gives a precise geometric ledger for where the Chern square must reside.

Let \(K_j=L_j^5\), let \(F_j=-iF_{5\mathcal A_j}\), and let \(s_j\) be a bounded radial cap of \(\sigma_j\), equal to \(\sigma_j\) near \(|\sigma_j|=\ell_\sigma\). On \(\{s_j\ne0\}\), define the phase one-form

\[
\vartheta_j
=
\frac{\operatorname{Im}\langle s_j,\nabla s_j\rangle}
{|s_j|^2}.
\]

Up to the fixed connection-sign convention,

\[
d\vartheta_j=F_j.
\]

Choose \(\chi=\chi(|s_j|)\), equal to zero for
\(|s_j|\le\ell_0\) and one for \(|s_j|\ge\ell_1\), where

\[
0<\ell_0<\ell_1<\ell_\sigma.
\]

Since \(dF_j=0\),

\[
\fint F_j\wedge F_j
=
\fint(1-\chi)F_j\wedge F_j
-
\fint d\chi\wedge\vartheta_j\wedge F_j.
\tag{A.6}
\]

The left side has the fixed asymptotic value

\[
\fint F_j\wedge F_j
=
4\pi^2\frac{c_1(L_j^5)^2}{V_j}
\longrightarrow\frac{50}{3}.
\tag{A.7}
\]

Writing \(F_j=F_{0,j}^{(5)}+e_j\), with
\(|F_{0,j}^{(5)}|\le C\) and \(\|e_j\|_2\to0\), and putting

\[
Z_j=\{|s_j|\le\ell_1\},
\qquad
T_j=\{\ell_0<|s_j|<\ell_1\},
\]

one obtains directly from (A.6)

\[
\frac{50}{3}+o(1)
\le
C\mu_j(Z_j)
+
C\fint_{T_j}|\nabla s_j|^2
+
C\|e_j\|_2
\left(\fint_{T_j}|\nabla s_j|^4\right)^{1/2}.
\tag{A.8}
\]

Once \(|s_j|\to\ell_\sigma\) in measure, \(\mu_j(Z_j)\to0\). Hence the Chern square forces a definite phase-capacity concentration in the shrinking transition region:

\[
\liminf_j
\left[
\fint_{T_j}|\nabla s_j|^2
+
\|e_j\|_2
\left(\fint_{T_j}|\nabla s_j|^4\right)^{1/2}
\right]>0.
\tag{A.9}
\]

This is the strongest exact zero/phase identity presently visible. It also explains why convergence of the modulus in four-dimensional measure is insufficient: codimension-two zero tubes can have vanishing four-volume while retaining all of \(c_1(K_j)^2\).

## A.3 Why Bianchi does not yet control \(\mathfrak W_j\)

At constant scalar curvature, the differential Bianchi identity has the form

\[
\delta W^-=
\pm\frac12(d^\nabla\operatorname{Ric}^\circ)^-,
\tag{A.10}
\]

with the sign depending on conventions. The endpoint budget gives
\(\|\operatorname{Ric}^\circ\|_2\to0\), but gives no estimate for
\(\nabla\operatorname{Ric}^\circ\).

Trying to integrate the curvature action
\(\mathcal Q(W^-,\nabla v)\) by parts through (A.10) produces either

\[
\nabla\operatorname{Ric}^\circ*\nabla v*\nabla v
\]

or, after another integration by parts,

\[
\operatorname{Ric}^\circ*\nabla^2v*\nabla v.
\]

The latter returns exactly to the second-jet quantity in (A.1). Thus ordinary Bianchi manipulation is circular here. A useful cancellation would have to exploit the special chiral representation of the surviving jet, not merely \(\delta W^-=\frac12d^\nabla\operatorname{Ric}^\circ\).

## A.4 What the positive-current mechanism can and cannot presently supply

Where \(\Phi_j\ne0\), it selects an almost-complex structure \(J_{+,j}\). The real determinant curvature

\[
f_j=-iF_{\mathcal A_j}
\]

is exactly of type \((1,1)\) for this structure:

* \(f_j^+\) lies in the fundamental-form line selected by \(\Phi_j\);
* every ASD two-form lies in the primitive \((1,1)\) summand.

Moreover \(df_j=0\). This gives a natural closed geometric object without first constructing a new form.

Two further ingredients are absent:

1. Pointwise taming requires the fundamental-form coefficient to dominate the primitive ASD component. The available \(L^2\) fit does not provide this domination on the curvature-concentration set.
2. The positive-current closure mechanism needs uniform mass, directional, and transverse estimates such as
   \[
   \mu(B_r)\le Cr^2,\qquad I_r=O(r^4),\qquad N_r=o(r^2),
   \]
   so that \(r^{-3}\sqrt{I_rN_r}\to0\). None follows from small \(P/V\) when the compressed action \(\mathfrak W_j\) diverges.

Even if a closed positive current representing \(5a_j\) were constructed, its pairing with \(a_j\) would naturally be of order \(a_j^2\asymp V_j\), fully consistent with (A.7). To exclude the escape one would need an additional equation forcing that current’s phase capacity or transverse mass to vanish. At present the exact missing quantity remains the compressed ASD curvature action in (A.1), equivalently the transition phase capacity in (A.9).

---

# B. O11: corrected variational and diffuse transport formulations

The certified isolated cell has

\[
\frac{P_{\mathrm{cell}}}{8\pi^2}
\in
[0.995662732753254\ldots,\,
 0.995662732771114\ldots],
\]

and its small frame rotations give smooth exact-collar metrics conformal to almost-Kähler metrics, with nonzero exceptional periods and \(P<8\pi^2\). Therefore no valid instability theorem can assert that every metric with

\[
P<8\pi^2(1-\epsilon)k
\]

admits a descent direction. Such metrics already exist.

The corrected scale is suggested by the exact saving identities. Put

\[
q=8\pi^2k.
\]

For actual all-sign solutions on the scalar-\(-4\) representative,

\[
q-P\le 2R_0,
\qquad
R_0=\mathbb E_\epsilon
\int |\nabla n_\epsilon|_{W_2}^2,
\tag{B.1}
\]

and Theorem K gives

\[
q-P
\le
\frac{4\sqrt6}{3}
\int\operatorname{dist}(W^+,\mathcal K).
\tag{B.2}
\]

Thus an order-\(k\) saving requires an order-\(k\) field rotation or Kähler-orbit departure. The formal common mode spreads this departure over volume \(\asymp A\), paying \(P\asymp k^2/A\).

## B.1 Near-minimizer selection can be sharpened to the diffuse scale

The existing variation remainder gives, for a metric with
\(P-p\le\delta\),

\[
|DP[H]|\le C(A\delta)^{1/2},
\qquad
D^2P[H,H]\ge-C A^{2/3}\delta^{1/3}
\tag{B.3}
\]

uniformly over the critical derivative budget.

Let

\[
\Theta=\frac{k^2}{A}.
\]

Choosing

\[
\delta=o\!\left(
\min\left\{\frac{\Theta^2}{A},
           \frac{\Theta^3}{A^2}\right\}
\right)
\tag{B.4}
\]

produces selected scalar-\(-4\) near-minimizers satisfying

\[
|DP[H]|=o(\Theta),
\qquad
D^2P[H,H]\ge-o(\Theta).
\tag{B.5}
\]

For \(\Theta=k^2/A\), the stronger precision in (B.4) is

\[
\delta=o\!\left(\frac{k^6}{A^5}\right).
\]

This is an exact variational fact and requires neither attainment nor geometric compactness. Hence the existing selection theory is already sensitive enough to test a \(k^2/A\) instability or transport law.

## B.2 The concrete diffuse theorem

The cleanest proof object is the following quadratic actual-field transport estimate on selected near-minimizers:

\[
\boxed{
R_0^2\le \Lambda A\,P+o(k^2),
}
\tag{B.6}
\]

with \(\Lambda\) uniform in the covering family and \(0<k/A<1/3\).

Combining (B.6) with the exact linear identity (B.1) gives

\[
q-P\le 2\sqrt{\Lambda AP+o(k^2)}.
\]

Solving the quadratic inequality yields

\[
\boxed{
P\ge
\left(
\sqrt{\Lambda A+8\pi^2k}
-\sqrt{\Lambda A}
\right)^2
-o\!\left(\frac{k^2}{A}\right).
}
\tag{B.7}
\]

In the tower regime \(k/A\to0\),

\[
P\ge
\frac{16\pi^4}{\Lambda}\frac{k^2}{A}
-o\!\left(\frac{k^2}{A}\right).
\tag{B.8}
\]

This would be a new all-metric Einstein gap throughout the open pure-blow-up range, even though its coefficient is not the old unit tariff.

A corresponding Weyl-orbit formulation is

\[
\left(
\int\operatorname{dist}(W^+,\mathcal K)
\right)^2
\le
\Lambda_{\mathcal K}A\,P+o(k^2),
\tag{B.9}
\]

which combines with (B.2). The field version (B.6) is more tightly connected to the actual sign-family equations.

### Why (B.6) accommodates the certified cells

For \(k\) localized cells, both \(P\) and the required rotation energy are of order \(k\). Hence

\[
\frac{R_0^2}{AP}\asymp\frac{k}{A},
\]

which is small in the covering regime. Thus (B.6) does not price each cell at \(8\pi^2\), does not force zero exceptional periods, and does not use the almost-Kähler conformal representative. The \(p^{-2}\) scalar-variance layer in that representative is therefore irrelevant to (B.6), which is formulated on the original scalar-\(-4\) metric and its actual monopoles.

## B.3 A useful dual object behind the transport estimate

A concrete route to (B.6) is a gauge-invariant transport potential for the shallow-amplitude \(W_2\) rotation. Its desired form is an identity

\[
R_0
=
\mathbb E_\epsilon
\int
\left\langle
\operatorname{Ric}^\circ,
\mathcal T_g U_\epsilon
\right\rangle
+\mathcal R,
\tag{B.10}
\]

where

\[
\mathbb E_\epsilon
\|\mathcal T_gU_\epsilon\|_2^2
\le \Lambda A,
\qquad
\mathcal R=o(k).
\tag{B.11}
\]

Cauchy–Schwarz then gives (B.6). In the Cotton formulation, \(\mathcal T_gU\) is built from the adjoint tensors
\(\mathcal C^*U\) and \(\delta^*U\). The terms that must remain explicit are

\[
E=W^+-W_0,\qquad
\nabla\rho,\qquad
\text{shallow-band cutoff derivatives},
\]

together with any core or collar contribution. The essential requirement is that the \(L^2\) norm in (B.11) be controlled by \(A\), not by \(R_0\) or \(P^{-1}\). That is the noncircular content of the transport theorem.

The formal common mode nearly saturates the linear estimate (B.2) and has \(P\asymp k^2/A\), so a dual identity of the form (B.10) has the correct algebraic scale.

---

# C. Corrected minimizer-entry and global comparison

A pure marked-cell theorem is insufficient because a minimizing sequence may distribute exceptional charge through the bulk. Conversely, a purely diffuse theorem does not describe localized cores. The natural unified object is an infimal convolution of localized relative cost and diffuse transport cost.

Let \(\tau_{\mathrm{CH}}(m)\) denote the infimum of the relative Einstein action of a marked \(m\)-charge core with a prescribed complex-hyperbolic outer germ. The relative action must include the Euler/signature Chern–Simons interface flux so that it is additive when the core is glued to the bulk. It must be normalized to reproduce the certified cell value; in particular,

\[
\tau_{\mathrm{CH}}(1)
\le
8\pi^2\cdot0.995662732771114\ldots.
\tag{C.1}
\]

The symplectic rotation construction also gives a sub-\(8\pi^2\) upper value inside the smooth conformally almost-Kähler subclass, though not the same interval enclosure.

A corrected entry/global-comparison theorem would have the form

\[
\boxed{
p(X\#k\overline{\mathbb{CP}}^{\,2})
\ge
\inf_{0\le m\le k}
\left\{
\tau_{\mathrm{CH}}(m)
+
\left(
\sqrt{\Lambda A+8\pi^2(k-m)}
-\sqrt{\Lambda A}
\right)^2
\right\}
-\varepsilon_{A,k},
}
\tag{C.2}
\]

with

\[
\varepsilon_{A,k}
=o(k^2/A)
\]

in the covering regime.

Here:

* \(m\) is the exceptional charge carried by localized marked cores;
* \(k-m\) is the charge transported diffusely through the bulk;
* the interface fluxes cancel in the global relative Chern–Weil identity;
* lack of controlled collars must contribute directly to the diffuse/core cost rather than being excluded by assumption.

For \(k/A\to0\), any linear lower estimate
\(\tau_{\mathrm{CH}}(m)\ge\tau_0m\), \(\tau_0>0\), makes the minimizing branch in (C.2) diffuse to first order, yielding \(k^2/A\). At larger density, localized and mixed branches can compete. The formula therefore contains both the certified isolated-cell geometry and the formal common mode.

The demanding part of this route is the precision: an \(O(k^2/A)\) collar-reduction error is the same size as the diffuse term and does not determine its coefficient. The marked charge identity, all interface transgressions, and the remainder in the global comparison must be resolved to \(o(k^2/A)\).

---

# Overall judgment

On the mathematics presently available, **Route B, specifically the quadratic transport theorem (B.6) for scale-adapted selected near-minimizers, has the best chance of producing a major theorem**.

Its advantages are structural:

1. The exact identities (B.1)–(B.2) already convert geometric saving into a linear transport demand.
2. The selection construction can be sharpened to \(o(k^2/A)\) without attainment, compactness, injectivity-radius control, or noncollapse.
3. The resulting lower law (B.7) is algebraically explicit and compatible with both the certified cell and the formal common mode.
4. The missing object is concentrated in one estimate: an \(A^{1/2}\)-controlled dual transport potential, or an equivalent quadratic estimate for \(R_0\) or Kähler-orbit departure.

Route A also yields an important theorem-shaped output, namely the forced divergence

\[
\fint |W^-|\,|\nabla v|^2\to\infty
\]

and the exact phase-capacity identity (A.8). These substantially sharpen the description of any density-free escape. Yet the remaining phenomenon is a critical curvature concentration on vanishing-volume sets, precisely where zero tubes and closed currents can carry the full Chern square. Bianchi identities return to the same second-jet term, and the available positive-current mechanism requires directional and transverse estimates not supplied by the endpoint budgets.

The strongest unified formulation is therefore the hybrid lower law (C.2): localized sub-unit core costs together with a diffuse quadratic transport cost. It incorporates the certified construction rather than attempting to recover coefficient four.