# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 42,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step42_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step42_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

The active goal is a unified Einstein-gap theory. Compare two central unresolved routes using the supplied exact mathematics, not generic suggestions. Route A is density-free O10 after resetting the actual budget to p: any escape has chi/p→∞, p/V→2/(9pi^2), W-/V→∞; the finite-density proof constructs an actual L^5 section of asymptotically nonzero modulus whose Chern square density stays positive, but W- enters its derivative/second-jet control. Investigate whether the section's zero/phase geometry, a localized Chern transgression, Bianchi identities, or the positive-current mechanism can yield a genuinely new density-independent estimate. State the strongest exact identity or conditional theorem that looks derivable, and identify the precise mathematical quantity still uncontrolled. Route B is O11 after the certified sub-four cell and symplectic closure: generic near-minimizer selection remains valid but the old unit-tariff instability target is false; compare a corrected minimizer-entry/global-comparison route with a diffuse k^2/A transport route. Determine which route presently has the best chance of a major theorem, and formulate a concrete proof object that accommodates the certified construction rather than restoring coefficient four. Do not invent literature or assume compactness/noncollapse.

## Integrated Scientific Memo

## Integrated assessment

The supplied mathematics supports two firm conclusions.

1. **Route A can already be sharpened to a density-independent necessary concentration theorem, but not to a density-free endpoint gap.** The relevant obstruction is not the total quantity \(W^-/V\), but the action of \(W^-\) on the particular negative-spinor first jet used to construct the \(L^5\)-section.
2. **Route B has the better prospect for a major theorem, specifically through a diffuse quadratic transport estimate at scale \(k^2/A\).** A per-core positive tariff or a restored coefficient four is incompatible with the certified sub-four cell unless a global interaction term is retained. Localized CH coercivity is useful as an entry/localization lemma, but it is not by itself the principal lower-bound mechanism.

Several stronger claims suggested in the branch work require correction: the source does not justify a topological positive lower bound for each noncanonical core, nor does it show that actual near-minimizers admit a core decomposition. Likewise, an \(L^4\)-bound on \(\nabla t(\Phi)\) alone is not a clean sufficient replacement for the missing second-jet bounds; differentiating \(t(z)\) still introduces \(\nabla^2z\). The clean conditional object is instead the compressed \(W^-\)-action controlling the existing resolvent \(v\).

---

# A. Density-free O10

Work on the scalar-\(-4\) representatives with normalized measure
\[
d\mu_j/V_j.
\]
After resetting the finite-density theorem’s budget to the actual conformally invariant projection \(p_j\), every putative endpoint escape satisfies
\[
\frac{\chi(M_j)}{p_j}\to\infty,\qquad
\frac{p_j}{V_j}\to\frac{2}{9\pi^2},\qquad
\frac{a_j^2}{V_j}\to\frac1{6\pi^2},\qquad
\frac{W_j^-}{V_j}\to\infty.
\]
The strong-current input remains valid without the Euler-density bound. In particular,
\[
\rho_j\to\rho_*=\frac43,\qquad |t_j|^2\to m_*=\frac{128}{81},
\]
and
\[
-iF_{\mathcal A_j}=F_{0,j}+r_{F,j},\qquad
|F_{0,j}|\le C,\qquad \|r_{F,j}\|_2\to0.
\]
The bounded direct resolvent
\[
(4+\mathcal L_j)v_j=6z_j,\qquad v_j\in\Gamma(S_j^-\otimes L_j),
\]
still obeys
\[
|v_j|\le6,\qquad
\|v_j-t_j\|_{H^1}\to0,\qquad
\|D^-_{3\mathcal A_j}v_j\|_2\to0,\qquad
\|(\mathcal L_j-2)v_j\|_2\to0.
\]

## A.1 Exact bottleneck: compressed negative-Weyl action

Applying the covariant Hodge–Weitzenböck identity to \(\nabla v_j\) gives schematically
\[
\fint\bigl(|\nabla^2v_j|^2+|\nabla v_j|^4\bigr)
\le
C\left[
1+\fint\bigl\langle \mathscr W_j^-\nabla v_j,\nabla v_j\bigr\rangle_+
\right],
\tag{A.1}
\]
after absorbing the scalar, \(W^+\), \(\operatorname{Ric}^\circ\), and determinant-curvature errors already controlled by the endpoint estimates. Here \(\mathscr W^-\) is the explicit representation-theoretic action of \(W^-\) on
\[
T^*M\otimes(S^-\otimes L),
\]
and
\[
\left|\left\langle \mathscr W^-\nabla v,\nabla v\right\rangle\right|
\le C|W^-||\nabla v|^2.
\]
Thus a convenient stronger sufficient quantity is
\[
\mathfrak W_j:=\fint |W_j^-|\,|\nabla v_j|^2.
\tag{A.2}
\]

This identifies a strictly finer obstruction than \(W_j^-/V_j=\fint|W_j^-|^2\): the divergent ASD curvature matters only insofar as it couples to the actual field-selected jet.

### Conditional density-independent endpoint theorem

If
\[
\sup_j\fint
\bigl\langle \mathscr W_j^-\nabla v_j,\nabla v_j\bigr\rangle_+
<\infty,
\tag{A.3}
\]
then no endpoint escape exists.

Indeed, (A.1) supplies
\[
\|\nabla^2v_j\|_2+\|\nabla v_j\|_4^2\le C.
\]
The finite-density proof then proceeds without change:

* the mass equation yields \(\|d|v_j|^2\|_2\to0\);
* the phase identity and the small Dirac residual kill all but one complex first derivative;
* the covariance test gives
  \[
  |\nabla v_j|^2\to2m_*
  \quad\text{in measure};
  \]
* the surviving derivative produces
  \[
  \sigma_j=\Phi_j\wedge t(v_j)\in\Gamma(L_j^5)
  \]
  with
  \[
  |\sigma_j|^2\to4\rho_*m_*^3>0
  \quad\text{in normalized measure},\qquad
  \|\nabla_{5\mathcal A_j}\sigma_j\|_2\le C.
  \]

The logarithmic line-bundle resolvent then forces
\[
\frac{c_1(L_j^5)^2[M_j]}{V_j}\to0,
\]
contradicting
\[
\frac{c_1(L_j^5)^2[M_j]}{V_j}
=25\frac{a_j^2}{V_j}
\to\frac{25}{6\pi^2}.
\]

Consequently every genuine density-free escape must satisfy the exact necessary condition
\[
\boxed{
\fint
\bigl\langle \mathscr W_j^-\nabla v_j,\nabla v_j\bigr\rangle_+
\longrightarrow\infty .
}
\tag{A.4}
\]
In particular, under the stronger absolute-value formulation,
\[
\boxed{
\fint |W_j^-|\,|\nabla v_j|^2\longrightarrow\infty .
}
\tag{A.5}
\]

This is the strongest clean density-independent statement presently derivable from the supplied proof.

## A.2 Localized Chern transgression: where the square survives

Let \(K_j=L_j^5\), \(F_j=-iF_{5\mathcal A_j}\), and let \(s_j\) be a bounded radial cap of the fifth-line section. On \(\{s_j\neq0\}\), define its phase connection
\[
\vartheta_j
=
\frac{\operatorname{Im}\langle s_j,\nabla s_j\rangle}{|s_j|^2},
\qquad d\vartheta_j=F_j
\]
up to the fixed sign convention. Choose \(\chi=\chi(|s_j|)\), vanishing for \(|s_j|\le\ell_0\) and equal to one for \(|s_j|\ge\ell_1\), where
\[
0<\ell_0<\ell_1<\ell_\sigma,\qquad
\ell_\sigma^2=4\rho_*m_*^3.
\]
Since \(dF_j=0\), Stokes gives the exact identity
\[
\fint F_j\wedge F_j
=
\fint(1-\chi)F_j\wedge F_j
-\fint d\chi\wedge\vartheta_j\wedge F_j.
\tag{A.6}
\]
Its left side satisfies
\[
\fint F_j\wedge F_j
=
4\pi^2\frac{c_1(L_j^5)^2[M_j]}{V_j}
\longrightarrow\frac{50}{3}.
\tag{A.7}
\]

Writing \(F_j=F_{0,j}^{(5)}+e_j\), with bounded \(F_{0,j}^{(5)}\) and \(\|e_j\|_2\to0\), and setting
\[
Z_j=\{|s_j|\le\ell_1\},\qquad
T_j=\{\ell_0<|s_j|<\ell_1\},
\]
one obtains
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
When \(|s_j|\to\ell_\sigma\) in measure, \(\mu_j(Z_j)\to0\), so a definite amount of Chern square must remain as transition phase capacity:
\[
\liminf_j\left[
\fint_{T_j}|\nabla s_j|^2+
\|e_j\|_2
\left(\fint_{T_j}|\nabla s_j|^4\right)^{1/2}
\right]>0.
\tag{A.9}
\]

This explains precisely why almost-everywhere nonzero modulus does not trivialize \(L_j^5\): codimension-two zero or phase-transition tubes can have vanishing four-volume while carrying the entire Chern square. The uncontrolled quartic transition term is the transgression-side version of the compressed curvature action in (A.4).

## A.3 Why Bianchi and positive currents do not yet close the estimate

At constant scalar curvature,
\[
\delta W^-=\pm\frac12(d^\nabla\operatorname{Ric}^\circ)^-.
\tag{A.10}
\]
The endpoint controls \(\|\operatorname{Ric}^\circ\|_2\), not
\(\|\nabla\operatorname{Ric}^\circ\|_2\). Integrating the term in (A.1) by parts therefore creates either
\[
\nabla\operatorname{Ric}^\circ*\nabla v*\nabla v
\]
or, after another integration by parts,
\[
\operatorname{Ric}^\circ*\nabla^2v*\nabla v,
\]
which is circular because \(\nabla^2v\) is exactly what (A.1) is intended to control. A useful Bianchi improvement would need a special chiral cancellation for the surviving rank-one jet, not the ordinary divergence identity alone.

The determinant curvature is closed and is of \((1,1)\)-type relative to the almost-complex direction selected by \(\Phi_j\): its self-dual component lies in the fundamental-form line, while its ASD component is primitive \((1,1)\). This is promising input for a current construction, but positivity is not automatic: the fundamental coefficient need not dominate the primitive ASD component on the concentration set.

The positive-current mechanism additionally requires uniform two-dimensional mass and directional/transverse moments, of the form
\[
\mu(B_r)\le Cr^2,\qquad I_r=O(r^4),\qquad N_r=o(r^2),
\]
so that
\[
r^{-3}\sqrt{I_rN_r}\to0.
\]
None of these follows from small \(P/V\) once (A.4) diverges. Even constructing a closed positive current representing \(5a_j\) would not itself contradict
\[
a_j^2/V_j\to1/(6\pi^2);
\]
one would still need an equation forcing its transition capacity or transverse moment to vanish.

Hence the precise unresolved object in Route A is:

\[
\boxed{
\text{the positive compressed }W^-\text{-action on the actual resolvent jet,}
\quad
\fint\langle\mathscr W^-\nabla v,\nabla v\rangle_+,
}
\]
equivalently, on the transgression side, the quartic phase capacity concentrated in the shrinking transition set.

---

# B. O11 after the certified sub-four construction

The certified cell gives
\[
\frac{P_{\rm cell}}{8\pi^2}
\in
[0.995662732753254\ldots,\,
 0.995662732771114\ldots],
\]
and small frame rotations preserve \(P<8\pi^2\) while producing smooth conformally almost-Kähler metrics with nonzero exceptional periods. Therefore:

* coefficient four/unit tariff is false;
* symplecticity and a nowhere-zero self-dual harmonic form do not restore it;
* the \(p^{-2}\) scalar-variance blow-up occurs only in the almost-Kähler conformal representative and cannot be charged to \(P\) of the original metric.

The old instability target
\[
P\le 8\pi^2(1-\epsilon)k
\Longrightarrow
\text{order-}k\text{ descent direction}
\]
cannot be a universal theorem.

## B.1 The exact diffuse scale

For scalar-\(-4\) metrics with actual all-sign fields, the exact field identities give
\[
8\pi^2k-P\le 2R_0,
\qquad
R_0=\mathbb E_\epsilon\int|\nabla n_\epsilon|_{W_2}^2,
\tag{B.1}
\]
while Theorem K gives
\[
8\pi^2k-P
\le
\frac{4\sqrt6}{3}
\int\operatorname{dist}(W^+,\mathcal K).
\tag{B.2}
\]
Thus any order-\(k\) saving demands order-\(k\) field rotation or \(L^1\) departure from the Kähler Weyl orbit.

The formal common mode distributes a pointwise departure of size \(k/A\) over volume \(\asymp A\), so its quadratic cost is
\[
A(k/A)^2\asymp k^2/A.
\]
It nearly saturates (B.2) when \(k/A\to0\). This makes \(k^2/A\), not \(k\), the natural unrestricted lower scale.

## B.2 Near-minimizer selection already reaches \(k^2/A\)

For a selected metric with \(P-p\le\delta\), the variation remainder gives
\[
|DP[H]|\le C(A\delta)^{1/2},\qquad
D^2P[H,H]\ge-C A^{2/3}\delta^{1/3}
\tag{B.3}
\]
uniformly over the critical derivative budget. Set
\[
\Theta=\frac{k^2}{A}.
\]
Choosing
\[
\delta=o\!\left(
\min\left\{\frac{\Theta^2}{A},\,\frac{\Theta^3}{A^2}\right\}
\right)
\tag{B.4}
\]
gives
\[
|DP[H]|=o(\Theta),\qquad
D^2P[H,H]\ge-o(\Theta).
\tag{B.5}
\]
Since \(\Theta=k^2/A\), the stronger requirement in (B.4) is
\[
\delta=o(k^6/A^5).
\]
Arbitrarily accurate infimum approximation permits this without attainment or compactness. Thus variational selection is not the bottleneck at the diffuse scale.

## B.3 Best concrete proof object: quadratic actual-field transport

The most consequential theorem-shaped target is
\[
\boxed{
R_0^2\le \Lambda A\,P+o(k^2)
}
\tag{B.6}
\]
for selected near-minimizers, with \(\Lambda\) uniform in the specified cover family and \(0<k/A<1/3\).

Combining (B.6) with (B.1) yields
\[
8\pi^2k-P
\le2\sqrt{\Lambda AP+o(k^2)}.
\]
Solving this quadratic inequality gives
\[
\boxed{
P\ge
\left(
\sqrt{\Lambda A+8\pi^2k}
-\sqrt{\Lambda A}
\right)^2
-o(k^2/A).
}
\tag{B.7}
\]
For \(k/A\to0\),
\[
P\ge
\frac{16\pi^4}{\Lambda}\frac{k^2}{A}
-o(k^2/A).
\tag{B.8}
\]
This would provide an all-metric positive gap throughout the open pure-blow-up range, without reviving the false unit tariff.

An equivalent curvature formulation is
\[
\left(
\int\operatorname{dist}(W^+,\mathcal K)
\right)^2
\le \Lambda_{\mathcal K}A\,P+o(k^2),
\tag{B.9}
\]
combined with (B.2). The field version is preferable because it is tied directly to the exact all-sign identities.

A concrete dual realization would be an identity
\[
R_0
=
\mathbb E_\epsilon
\int
\left\langle\operatorname{Ric}^\circ,\mathcal T_gU_\epsilon\right\rangle
+\mathcal R,
\tag{B.10}
\]
with
\[
\mathbb E_\epsilon\|\mathcal T_gU_\epsilon\|_2^2\le\Lambda A,
\qquad
\mathcal R=o(k).
\tag{B.11}
\]
In a Cotton-based construction, \(\mathcal T_gU\) would involve the adjoints \(\mathcal C^*U\) and \(\delta^*U\). The proof must retain explicitly:

* \(E=W^+-W_0\);
* amplitude-gradient terms such as \(\nabla\rho\);
* shallow-band cutoff derivatives;
* core/collar fluxes;
* the distinction between \(R_0\) and \(R_\rho\).

The estimate is noncircular only if the right side of (B.11) is controlled by \(A\), not by \(R_0\), \(P^{-1}\), or an assumed noncollapse constant.

The certified localized cells are compatible with (B.6): for \(k\) separated cells, \(R_0\asymp k\) and \(P\asymp k\), hence
\[
\frac{R_0^2}{AP}\asymp\frac{k}{A}.
\]
Nothing in (B.6) forces a unit cost, vanishing exceptional periods, or bounded scalar variance in the almost-Kähler conformal gauge.

## B.4 Role and limitation of minimizer-entry/global comparison

A localized CH coercivity estimate remains an important auxiliary object. In Bianchi/DeTurck gauge on \(\Omega\Subset\Omega_1\), the correct target is
\[
\int_\Omega
\left(
|W^-|^2+|W^+-W^+_{\rm CH}|^2
\right)
+\mathcal V_\Omega
\le
C\left[
\int_{\Omega_1}|\operatorname{Ric}^\circ|^2
+\mathcal B(\Omega_1\setminus\Omega)
\right],
\tag{B.12}
\]
where \(\mathcal V_\Omega\) is the scalar-normalized volume departure after separating its signed boundary flux, and \(\mathcal B\) is an explicit gauge-invariant collar term. This can force order-\(k\) departure into nonperturbative cores or collars.

But (B.12) does not itself give a global lower bound:

* no supplied result says arbitrary near-minimizers enter a CH-close decomposition;
* no branch selection theorem identifies every field on the CH-like bulk;
* collar errors of order \(k^2/A\) are already of leading diffuse size;
* a claimed universal positive cost for each exceptional core would need a new theorem and risks contradicting the observed background interaction.

In particular, the suggested “core Weyl contribution”
\[
\int_{U_i}|W^+-W_{0,\epsilon}|^2\ge c_C>0
\]
does not follow merely from \(E_i^2=-1\). The exact all-sign identities explicitly allow saving through kinetic/Nijenhuis rotation and amplitude depletion. The certified sub-four cell demonstrates that a naive local topological tariff is too rigid.

The correct global-comparison object should therefore allow a split between localized and diffuse charge. Let \(\tau_{\rm CH}(m)\) denote a relative marked-core cost including all Chern–Simons/interface fluxes, normalized so that
\[
\tau_{\rm CH}(1)
\le
8\pi^2\cdot0.995662732771114\ldots.
\]
A compatible hybrid theorem would have the form
\[
\boxed{
p\!\left(X\#k\overline{\mathbb{CP}}^{\,2}\right)
\ge
\inf_{0\le m\le k}
\left\{
\tau_{\rm CH}(m)
+
\left(
\sqrt{\Lambda A+8\pi^2(k-m)}
-\sqrt{\Lambda A}
\right)^2
\right\}
-\varepsilon_{A,k},
}
\tag{B.13}
\]
with
\[
\varepsilon_{A,k}=o(k^2/A)
\]
in the tower regime.

Here \(m\) is the exceptional charge carried by marked localized cores and \(k-m\) is transported diffusely. Formula (B.13) is not presently proved, but it is the correct proof object for a minimizer-entry/global-comparison program because it incorporates, rather than suppresses, the certified sub-unit cell and the diffuse common mode.

---

# Comparative judgment

**Route B’s diffuse quadratic transport route presently has the best chance of a major theorem.**

It has four decisive advantages:

1. Exact identities already convert any saving into a linear transport demand, (B.1)–(B.2).
2. Near-minimizer selection can be made accurate at the \(k^2/A\) scale without attainment, compactness, or noncollapse.
3. The candidate lower law (B.7) is explicit and compatible with both the certified cell and the formal diffuse mode.
4. Its missing content is sharply localized in one noncircular estimate: an \(A^{1/2}\)-controlled dual transport potential, equivalently (B.6) or (B.9).

The minimizer-entry/localized-CH route is valuable as a way to isolate where transport occurs and to define the relative core term in (B.13), but it cannot lead with a per-core tariff. Any global comparison must preserve all interface fluxes to \(o(k^2/A)\), since an \(O(k^2/A)\) error is already of leading order.

Route A has yielded a meaningful theorem-shaped advance:
\[
\fint\langle\mathscr W^-\nabla v,\nabla v\rangle_+\to\infty,
\]
together with the exact phase-transgression identity (A.6)–(A.9). These show that any density-free escape must concentrate ASD curvature precisely on the actual field-selected jet and store the nonzero Chern square in shrinking phase-transition geometry. What remains uncontrolled is exactly that compressed curvature action—or equivalently the quartic phase capacity—not merely the global Weyl density. Bianchi and the currently available positive-current mechanism do not yet control it.