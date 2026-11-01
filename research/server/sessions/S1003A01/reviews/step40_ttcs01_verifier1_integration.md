# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 40,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step40_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step40_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematics and numerics of the Step-40 note on harmonic-class compatibility of SU(2)-invariant cell variations for the perpendicular complex-hyperbolic blow-up cell. Check carefully: (a) the self-duality ODE d_t phi = (2/sqrt(det H)) H phi for invariant closed forms d(sum phi_i sigma_i) on g=dt^2+H_ij sigma_i sigma_j with d sigma_i = 2 sigma_j^sigma_k, including orientation and the factor 2; (b) the bolt exponents (0,2,2) for SD and (0,-2,-2) for ASD at a perpendicular bolt H~diag(t^2,b^2,b^2), smoothness conditions for the potential components, and the period formula int_E d(phi_1 sigma_1)=2 pi phi_1(0); (c) the SU(2)-averaging argument that for invariant variations supported in the cell the b^- solvability conditions int<h0, Omega o beta> = 0 collapse to a single exceptional condition, and the claims that the host period angle eta does not move at first order while j>=1 isotypic variations do not move exceptional periods at first order; (d) the Klein-group character localization of the obstruction in the h13 block and the decoupling from diagonal modes (including the exterior mass-null mode); (e) the rotation formula delta phi_1(0)=int theta' Phi dt and the gauge identity; (f) whether the period-stiffness computation DeltaJ = t^2/(2 L^T H^{-1} L) is correctly assembled from the Step-21 Hessians (note the Hessians were computed with a bolt rotation psi*(chi-1) while the period functional uses the isometric psi*chi form; check that this does not change the Hessian or the period functional), and what exactly it establishes (Ritz upper value at second order within the invariant block, floating). (g) Section 1: conformal invariance of the pair class and the claimed extension of inf P = inf J6 to pair classes defined by conditions on Omega. Also judge the interpretation in Section 3: positive exceptional areas available at quadratic cost near the perpendicular cell versus linear Kahler tariff, and what it does and does not imply for Taubes/AKGamma-type lower bounds and for the unrestricted blow-up tariff. Point out any error, missing hypothesis, or overstatement, and give the corrected statement.

## Integrated Scientific Memo

# Step-40 verification memo

## Overall verdict

The local SD/ASD ODE, bolt indicial analysis, averaging reduction, \(h_{13}\)-localization, gauge identity, and finite-dimensional stiffness formula are essentially correct. The numerical integration reproduces the quantity coded.

There is, however, a decisive normalization error:

\[
\Omega=\frac12d(\phi_i\sigma_i)
\quad\Longrightarrow\quad
\int_E\Omega=\pi\phi_1(0),
\]

whereas the note and script use \(2\pi\phi_1(0)\). Thus the reported stiffness is for \(2\Omega\), not for the Step-39 Kähler-normalized form. In terms of the actual exceptional area \(t=\int_E\Omega\),

\[
K_{\Omega}\simeq 32.34,\qquad
\Delta J\simeq 16.17\,t^2,
\]

not \(K\simeq8.09\) and \(4.04t^2\). Several interpretive statements also require qualification, especially the global \(j\ge1\) claim and the claim about the zero set for \(t\ne0\).

---

## 1. SD/ASD invariant ODE

On the principal-orbit region, write

\[
F=d\!\left(\sum_i\phi_i\sigma_i\right)
  =dt\wedge \phi_i'\sigma_i+2\phi_i\,\sigma_j\wedge\sigma_k
\]

cyclically. For the orbit metric \(H_{ij}\sigma_i\sigma_j\),

\[
*_3\sigma_i
=\sqrt{\det H}\,(H^{-1})_{ij}\,\sigma_k\wedge\sigma_l.
\]

With orientation

\[
dt\wedge\sigma_1\wedge\sigma_2\wedge\sigma_3>0,
\]

one has \(*_4(dt\wedge\alpha)=*_3\alpha\). Hence \(F=*F\) is equivalent to

\[
\sqrt{\det H}\,H^{-1}\phi'=2\phi,
\]

so

\[
\boxed{\phi'=\frac{2}{\sqrt{\det H}}H\phi.}
\]

Similarly,

\[
\boxed{\psi'=-\frac{2}{\sqrt{\det H}}H\psi}
\]

for ASD forms. The factor \(2\), the occurrence of \(H\) rather than \(H^{-1}\), and the signs are correct for this orientation. Reversing the four-dimensional orientation exchanges SD and ASD.

Strictly, when \(\phi_1(0)\ne0\), the potential \(\phi_1\sigma_1\) need not extend as a smooth global one-form across the bolt. The two-form \(d(\phi_1\sigma_1)\) does. Thus “every invariant closed form is \(d(\sum\phi_i\sigma_i)\)” should be read on the principal-orbit region, with the usual connection-type singularity of the potential allowed at the bolt.

---

## 2. Bolt behavior, regularity, and period normalization

At a perpendicular bolt,

\[
H=\operatorname{diag}(t^2,b^2,b^2)+O(t^2),\qquad
\sqrt{\det H}=tb^2(1+O(t^2)).
\]

The SD principal system is

\[
\phi_1'=\frac{2t}{b^2}\phi_1+O(t)\phi,\qquad
\phi_2'=\frac2t\phi_2+\cdots,\qquad
\phi_3'=\frac2t\phi_3+\cdots,
\]

giving indicial exponents

\[
\boxed{(0,2,2)}.
\]

Thus bolt-smooth solutions have

\[
\phi_1=c_1+O(t^2),\qquad
\phi_2=t^2(c_2+O(t^2)),\qquad
\phi_3=t^2(c_3+O(t^2)).
\]

The ASD exponents are

\[
\boxed{(0,-2,-2)},
\]

so the regular invariant ASD space is one-dimensional, generated by

\[
\beta_E=d(\psi_-\sigma_1),\qquad
\psi_-=\psi_+^{-1},\qquad
\psi_+'=\frac{2H_{11}}{\sqrt{\det H}}\psi_+.
\]

The smoothness statement requires the standard smooth Bianchi-IX bolt jets, not merely the leading asymptotic \(H\sim\operatorname{diag}(t^2,b^2,b^2)\). Under those jets, the exponent-zero and exponent-two branches extend smoothly.

From

\[
\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2
\]

and fibre period \(2\pi\),

\[
\int_E\sigma_2\wedge\sigma_3=\pi
\]

up to orientation. Therefore

\[
\boxed{\int_Ed(\phi_1\sigma_1)=2\pi\phi_1(0).}
\]

That formula itself is correct. But the Step-39 form is

\[
\Omega=\frac12d(\phi_i\sigma_i),
\]

so its exceptional period is

\[
\boxed{\int_E\Omega=\pi\phi_1(0).}
\]

This factor is forced by the CH collar normalization:

\[
\omega_{CH}=\frac12d(x\sigma_f).
\]

The script sets the collar potential equal to \(X\), hence evolves the \(\phi\) appearing inside \(\frac12d(\phi\sigma)\). Its line

```python
Lt = 2*np.pi*ell_vec
```

therefore computes the period of \(d(\phi\sigma)=2\Omega\).

---

## 3. Fixed-class compatibility and averaging

For a closed manifold and fixed cohomology class, \(\dot\Omega=da\). Differentiating \(*\Omega=\Omega\) gives

\[
(da)^-=\frac12\dot *_h\Omega.
\]

Since the cokernel of \(d^-:\Omega^1\to\Omega^-\) is \(\mathcal H^-_g\), solvability is equivalent to

\[
\int_M\langle \dot *_h\Omega,\beta\rangle\,dV=0
\qquad\forall\beta\in\mathcal H^-_g.
\]

The trace part of \(h\) does not vary the star on two-forms in four dimensions, and this can be written, up to a harmless convention-dependent sign or constant, as

\[
\boxed{
\int_M\langle h^\circ,\Omega\circ\beta\rangle\,dV=0
\quad\forall\beta\in\mathcal H^-_g .
}
\]

For invariant \(h\) supported in an invariant cell \(U\), and invariant background \(\Omega\),

\[
\int_U\langle h^\circ,\Omega\circ\beta\rangle
=
\int_U\langle h^\circ,\Omega\circ\bar\beta\rangle,
\]

where \(\bar\beta\) is the SU(2)-average of \(\beta|_U\). Averaging commutes with \(d\) and \(*\); bolt regularity then gives

\[
\bar\beta=c(\beta)\beta_E,
\qquad
c(\beta)\propto\int_E\beta.
\]

Thus the \(b^-\) compatibility equations reduce, for a single invariant cell variation, to one scalar cell functional:

\[
\boxed{
\int_U\langle h^\circ,\Omega\circ\beta_E\rangle\,dV=0 .
}
\]

For several disjoint exceptional spheres, there is one such local condition per cell; their exceptional directions are independent because the intersection form on their span is \(-I\).

### Host period angle

For an invariant cell deformation with unchanged collar data, the inward SD ODE produces a form equal to the original host form outside the cell. Its cohomology class differs only by an exceptional component. Consequently host-cycle periods are unchanged, and the host angle \(\eta\) is unchanged—not merely at first order but, for this local invariant construction, exactly. Orthogonality \(K_X\cdot E=0\) is consistent with this, but collar-supported localization is the more direct reason.

This does not mean the AK\(\Gamma\) combination \(\eta+e\) is stationary: its exceptional-area term \(e\) changes linearly with \(t\).

### Nontrivial SU(2) isotypes

The note overstates the global conclusion. A \(j\ge1\) cell variation pairs to zero with the invariant local model \(\Omega\circ\beta_E\), and in an isolated SU(2)-equivariant cell boundary-value problem it has no invariant exceptional-period output. On a general closed glued manifold, however, the harmonic ASD representative of the exceptional direction need not restrict to a purely invariant form on the cell. Its non-invariant components can pair with \(j\ge1\) variations.

The corrected statement is:

> Nontrivial isotypes do not couple to the invariant local exceptional mode \(\beta_E\). Their global first-order effect on exceptional periods is controlled by the non-invariant isotypic components of the relevant global ASD harmonic representatives. Therefore complete separation of “\(j=0\) exceptional” and “\(j\ge1\) host” channels has not been proved globally.

---

## 4. Klein characters and localization in \(h_{13}\)

The diagonal cell is fixed by the Klein four-group of sign changes preserving the \(\mathfrak{su}(2)\) brackets. The channels

\[
h_{12},\qquad h_{13},\qquad h_{23}
\]

carry its three distinct nontrivial characters, while diagonal modes carry the trivial character. Hence the Hessian of any invariant functional is block diagonal between these four sectors. In particular:

- the three off-diagonal channels do not couple quadratically;
- no off-diagonal channel couples quadratically to diagonal modes;
- the diagonal exterior mass-null direction has zero Hessian coupling to \(h_{13}\).

Linearizing the SD equation at \(\phi=(0,0,\phi_f)\), an off-diagonal variation has zero first variation of \(\det H\), and only \(\delta H_{13}\) enters the first component. With \(\delta\phi_1(t_c)=0\),

\[
\boxed{
\delta\phi_1(0)
=-\psi_+(0)\int_0^{t_c}
\frac{2\,\delta H_{13}\phi_f}
{\sqrt{\det H}\,\psi_+}\,dt .
}
\]

Thus the local invariant exceptional-period differential lies entirely in the \(h_{13}\) character. The \(h_{12}\) phase mode is period-preserving, and \(h_{23}\) produces only a regular \(\delta\phi_2=O(t^2)\).

These are exact local linear statements. The numerical Hessian block decoupling is additionally floating evidence for the implementation.

---

## 5. Rotation formula and gauge identity

For a rotation in the \(1\)-\(3\) plane with the convention used by the script,

\[
\delta H_{13}=\theta(H_{11}-H_{33}).
\]

Set

\[
\Phi=\psi_+(0)\frac{\phi_f}{\psi_+}.
\]

Then

\[
\Phi'
=
\frac{2(H_{33}-H_{11})}{\sqrt{\det H}}\Phi.
\]

Substitution into the variation formula yields

\[
\delta\phi_1(0)=\int_0^{t_c}\theta\,\Phi'\,dt.
\]

If \(\theta(t_c)=0\) and \(\Phi(0)=0\), integration by parts gives

\[
\boxed{
\delta\phi_1(0)
=-\int_0^{t_c}\theta'(t)\Phi(t)\,dt
}
\]

for the displayed convention. Reversing the exceptional-sphere orientation or the rotation convention changes the sign but not the stiffness. The note’s unsigned “up to orientation sign” statement is harmless for the quadratic calculation, but the fixed convention gives the minus sign.

The gauge identity follows immediately:

\[
\begin{aligned}
\int_0^{t_c}
\frac{2(H_{11}-H_{33})\phi_f}
{\sqrt{\det H}\psi_+}\,dt
&=
-\left[\frac{\phi_f}{\psi_+}\right]_{0}^{t_c}\\
&=-X,
\end{aligned}
\]

using \(\phi_f(0)=0\), \(\phi_f(t_c)=X\), and \(\psi_+(t_c)=1\). The reported relative errors \(1.1\times10^{-10}\) are consistent with this exact identity.

“Constant rotations are gauge” is valid only when the metric, form, collar frame, and gluing identification are rotated together. Holding the collar form rigidly in slot \(3\) while rotating only the metric produces a spurious endpoint contribution.

---

## 6. Hessian parameterization and stiffness

Suppose

\[
J(c)=J_0+\frac12c^THc+o(|c|^2),\qquad
t(c)=L^Tc+o(|c|).
\]

For positive-definite \(H\), minimizing the quadratic term subject to \(L^Tc=t\) gives

\[
c_*=\frac{H^{-1}L}{L^TH^{-1}L}\,t
\]

and

\[
\boxed{
\Delta J_{\mathrm{Ritz}}
=\frac{t^2}{2L^TH^{-1}L}.
}
\]

The linear algebra in the script is correct. The reported “Schur” number is specifically

\[
H_{\psi\psi}-H_{\psi m}H_{mm}^{-1}H_{m\psi},
\]

the cost at fixed bolt-rotation coefficient after relaxing the Chebyshev bump coefficients. It is not the unrelaxed pure-rotation Hessian entry.

### \(\psi\chi\) versus \(\psi(\chi-1)\)

The Hessian uses \(\psi(\chi-1)\), while the period calculation uses \(\psi\chi\). These differ by a global constant rotation. For the rotation-only family they are isometric, so both the geometric Hessian and geometric period differential agree after rotating collar data consistently.

With a simultaneous fixed-frame \(k_{13}\) bump, conjugating by the constant rotation also rotates that bump. The difference first appears as an order-\(\psi c\) diagonal term. Its contribution to the mixed Hessian is the diagonal first variation of \(J\):

- it vanishes at an exact stationary metric;
- for the floating finite-dimensional optimizer it is controlled only to the extent that the omitted diagonal gradient is controlled.

Thus the assembled matrix is properly described as a floating quotient-space Ritz computation at the numerically stationary cell, not as an exact invariant of an independently certified critical metric. No source supplied here verifies the equality of the two mixed parameterizations beyond that stationary-point argument.

### Corrected normalization

The script uses

\[
L_{\mathrm{file}}
=2\pi\,\frac{\partial\phi_1(0)}{\partial c}.
\]

For the actual Step-39 form,

\[
L_{\Omega}
=\pi\,\frac{\partial\phi_1(0)}{\partial c}
=\frac12L_{\mathrm{file}}.
\]

Therefore

\[
K_\Omega
=\frac1{L_\Omega^TH^{-1}L_\Omega}
=4K_{\mathrm{file}}.
\]

The corrected values are:

\[
\begin{array}{c|c|c|c}
(X,n)&K_{\rm file}&K_\Omega&
\Delta J/t^2=K_\Omega/2\\ \hline
(128,16)&8.08848&32.35391&16.17695\\
(512,10)&8.09442&32.37766&16.18883\\
(512,16)&8.08628&32.34513&16.17256\\
(512,24)&8.08611&32.34442&16.17221
\end{array}
\]

Hence, with

\[
t=\int_E\Omega,
\]

the computed finite-dimensional result is

\[
\boxed{\Delta J_{\rm Ritz}\simeq16.17\,t^2.}
\]

Under \(\bar g=6g\), \(\psi=6\Omega\), and

\[
t_g=\int_E\psi=6t,
\]

this becomes

\[
\boxed{\Delta J_{\rm Ritz}\simeq0.4492\,t_g^2.}
\]

If the original \(K\simeq8.09\) is retained, its period variable must be renamed

\[
\widetilde t=\int_E2\Omega=2t;
\]

then \(t_g=3\widetilde t\), not \(6\widetilde t\).

### What the numerics establish

They establish, at floating precision:

- the exact gauge identity to about \(10^{-10}\);
- agreement of selected nonlinear ODE responses with their linearizations;
- stable finite-dimensional stiffness under \(X=128\to512\) and \(n=10,16,24\);
- positivity of the displayed finite matrices and their sampled fixed-period restrictions.

They do **not** establish:

- a rigorous infinite-dimensional invariant minimum;
- coercivity in non-invariant isotypes;
- an Arb-certified stiffness;
- controlled finite-amplitude values along the optimal Ritz combination;
- the unrestricted period-resolved tariff.

The coefficient-space minimum eigenvalues are basis-dependent. Step 21’s generalized eigenvalues are the more meaningful coercivity diagnostics.

By Klein symmetry, the reduced cost is expected to be even in the signed \(h_{13}\) period, so at a genuinely symmetric stationary cell one expects

\[
J(t)=J_0+\frac12K_\Omega t^2+O(t^4),
\]

rather than merely \(O(t^3)\). For the floating implementation, retaining \(o(t^2)\) is the fully safe statement unless the symmetry and smooth reduction are explicitly enforced.

---

## 7. Conformal invariance of pair classes

In four dimensions, \(*\) on two-forms is conformally invariant. Therefore if \(\Omega\) is closed and SD for \(g\), it remains closed and SD—and hence harmonic—for \(u^2g\). Keeping the same differential form preserves:

- its cohomology class;
- all periods;
- its zero set and zero-set topology;
- nonvanishing, if present.

Thus Yamabe normalization preserves pair classes defined solely by such conformally invariant conditions on \(\Omega\).

The equality

\[
\inf_{\mathcal C}P=\inf_{\mathcal C}J_6
\]

follows for a class \(\mathcal C\) provided:

1. every relevant competitor admits the required positive solution \(u\to1\);
2. the decay is sufficient for the conformal identities and cutoff recovery;
3. the recovered exact collar remains in \(\mathcal C\);
4. \(\mathcal C\) is conformally stable.

Indeed \(J_6\ge P\), while Yamabe normalization gives \(J_6(u^2g)=P(u^2g)\le P(g)\), up to the vanishing collar-recovery loss.

The assertion should not be extended to conditions involving \(g\) explicitly, such as

\[
|\Omega|_g^2=2,
\]

almost-Kähler normalization, or metric-dependent amplitude bounds, since

\[
|\Omega|_{u^2g}=u^{-2}|\Omega|_g.
\]

Also, before collar recovery, \(\Omega\) is not the Kähler form of \(u^2g\): the fundamental form of the same almost-complex structure is \(u^2\Omega\). Exact equality with the CH Kähler form is restored only where the cutoff conformal factor equals \(1\).

For an \(m\)-core construction, obtaining total recovery loss \(o(m)\) additionally requires enough geometric room to choose recovery radii without overlap; single-cell decay alone does not guarantee this in a dense arrangement.

Finally, equality of infima does not imply that the displayed \(J_6\) Hessian equals the period-resolved \(P\) Hessian. Conformal relaxation may alter the latter.

---

## 8. Correct interpretation of positive exceptional periods

The corrected quadratic statement is

\[
J(t)\le J_0+16.17\,t^2+o(t^2),
\qquad t=\int_E\Omega,
\]

within the finite-dimensional invariant \(h_{13}\) Ritz family. It shows that the exceptional period is a soft quadratic modulus near the perpendicular non-Kähler cell, unlike the aligned Kähler law

\[
J_{\mathrm{K\ddot ahler}}(t)=1+\frac6\pi t+\cdots.
\]

It does **not** show that positive periods lower the perpendicular-cell cost: the computed coefficient is positive, so \(t=0\) remains a local minimum in that block.

Using the quadratic truncation,

\[
t_{\mathrm{cross}}
=\frac{2(6/\pi)}{K_\Omega}
\approx0.118,
\]

not \(0.472\). Including the offset \(J_0-1\) moves the formal crossing slightly, to about \(0.120\). This is well outside a quantitatively controlled infinitesimal regime, so it is only a comparison of truncated expansions.

Similarly,

\[
t_{\mathrm{threshold}}
\approx
\sqrt{\frac{1-J_0}{16.17}}
\approx0.017
\]

for the \(X=128\) value, corresponding to \(t_g\approx0.10\). Continuity and \(J_0<1\) rigorously imply some nonzero subthreshold interval, but the explicit \(0.017\) requires control of higher-order terms.

### Zero set for \(t\ne0\)

The note’s statement that the zero set becomes “generically lower-dimensional” is too weak for the local invariant family. On every principal orbit, an invariant SD form vanishes iff its potential vector vanishes; uniqueness for the nonsingular first-order ODE would then force the solution to vanish identically, contrary to its nonzero collar value. At the bolt, a nonzero exceptional period gives a nonzero tangential area-form component. Therefore, assuming the inward solution is smooth,

\[
\boxed{t\ne0\quad\Longrightarrow\quad \Omega_t\ \text{is nowhere zero}}
\]

for this invariant cell solution. Since the glued form equals the nonzero host Kähler form outside the cell, the closed glued form is symplectic after choosing the orientation for which \(\Omega_t\wedge\Omega_t>0\).

Equivalently,

\[
\widehat g_t=\frac{|\Omega_t|_g}{\sqrt2}\,g
\]

is a smooth almost-Kähler metric for fixed \(t\ne0\). It degenerates as \(t\to0\) at the bolt, recovering the singular conformal geometry seen in Step 39.

This strengthens the local conclusion, but does not remove the global qualifications below.

### Relation to Taubes and AK\(\Gamma\)

The computation supplies a local symplectic route with positive exceptional area at quadratic \(J_6\)-cost. It does not by itself determine a Taubes- or AK\(\Gamma\)-type lower bound for the original metric because:

- such estimates may apply to the almost-Kähler metric \(\widehat g_t\), not directly to \(g_t\);
- the conformal factor \(|\Omega_t|/\sqrt2\) becomes small near the bolt as \(t\to0\);
- curvature and derivative energies may concentrate in that transition;
- global monopole/canonical-class selection and host-period coupling remain separate inputs.

Thus there is no contradiction between a local quadratic \(J_6(g_t)\) cost and a lower bound whose missing payment is carried by conformal degeneration, form-derivative energy, host-period drift, interface flux, or global field constraints.

### Unrestricted blow-up tariff

The result shows that the aligned Kähler linear area tariff is not a universal local law for non-Kähler cells. It does not determine the unrestricted blow-up tariff. That still requires control of:

- the \(j\ge1\) Hessian and global ASD harmonic representatives;
- simultaneous multi-cell period compatibility;
- nonlinear \(j(t)\) beyond its Hessian;
- global closed-form and field-theoretic constraints;
- possible non-SU(2)-invariant lower-cost directions.

---

## Corrected core statement

For the Step-39 normalization

\[
\Omega=\frac12d(\phi_i\sigma_i),\qquad
t=\int_E\Omega=\pi\phi_1(0),
\]

the perpendicular \(x_0=0.038\) floating cell has, in the finite-dimensional SU(2)-invariant \(h_{13}\) Ritz space,

\[
\boxed{
J(t)=J_0+\frac12K_\Omega t^2+o(t^2),
\qquad K_\Omega\simeq32.34,
}
\]

or

\[
\boxed{\Delta J\simeq16.17\,t^2.}
\]

In the \(\operatorname{Ric}=-g\) normalization, with \(t_g=\int_E6\Omega=6t\),

\[
\boxed{\Delta J\simeq0.4492\,t_g^2.}
\]

This is a floating, fixed-collar, finite-dimensional invariant Ritz upper value. It shows that small nonzero exceptional areas—and in the invariant construction, nowhere-vanishing symplectic forms—are compatible with the perpendicular saving at quadratic local cost. It neither proves the unrestricted stiffness nor fixes the global blow-up tariff.