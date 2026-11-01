# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 67,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step67_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step67_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check, as a careful differential geometer, the new results in step67_cK_local_coercivity_at_cscK.md, which sit on the ledger of step65 §1/§7 and step66 (whose §7 corrections are binding). Setting: compact complex surface, cscK metric g0 with Kähler form omega, primitive Ricci form rho0 = 2*pi*h_a^- != 0 (a = c1), unit exceptional harmonic ASD form hhat, ledger p = q^2(1-delta)^2 + L. Verify or correct, with exact reasons: (1) Lemma 67.1: the inequality 2*pi*q*delta <= (t_J^-, hhat) for every class-a orientation-compatible J (from 65.1 and |Omega_J|=sqrt2), the argument that delta and L have zero first variation at cscK, differentiability of 𝔉 at g0 when Z(hhat) is nonempty, and the identity p - q^2 = C_+ - |c1^+|^2_g, hence 'every cscK metric is a critical point of LeBrun's C_+ - |c1^+|^2 on all metrics'. Is this known in the literature (LeBrun's curvature functionals)? Is it consistent with the first variations of int|W+|^2 (Bach tensor of Kähler metrics) and int s^2? (2) Theorem 67.K(A): Koszul division at transversal zeros; the linearized use of Lemma 66.D (div(phi o psi)=psi(delta phi)) to make the Ricci-aligned SD form first-order closed; the J-invariance claim (J-anti-invariant tracefree symmetric tensors = Omega^perp ⊗ Lambda^-); the reference first-order Kähler deformation realizing an arbitrary class change, especially the H^{2,0} directions via the Beltrami differential omega^{-1} theta-bar; Moser; and the Blair–Ianus Hessian argument: int s dmu = 4 pi c1.[omega] - kappa int|nabla omega|^2 on omega-compatible J (check s* - s >= 0 proportional to |nabla omega|^2 and the topological integral of the Hermitian scalar curvature), first variation d(int s)(gdot) = -int<Ric'',gdot>, and Hess E = 2||(nabla omega)'||^2. (3) Theorem 67.K(B): the Douglis–Nirenberg ellipticity of (DF, s', harmonic gauge) with the principal symbol stated (numerically checked in data/step67_cK_symbol_check.json), the Rellich/finite-kernel step, the order-one upper bound d2 <= (2 pi q)^{-1} tau_ref,2 with the reference structure built from J_K on ker l2, and the exact second-order formula 2 pi q d2 = tau_ref,2 - (1/sqrt2) int |w1|^2/|v0|. Identify any gap (e.g. whether the second-order Taylor statement in C^{2,alpha} is legitimate, whether the slice/gauge handling is right, whether K finite-dimensional is correctly used). Return precise corrections and the strongest correct statements.

## Integrated Scientific Memo

## Verification memo

The ledger normalization in Step 66 §7 is used throughout:
\[
q=\|h_a^-\|_2>0,\qquad \hat h=h_a^-/q,\qquad
\delta=1-\frac{\mathfrak F}{2\pi q},\qquad
L=\frac{P/2-\mathfrak F^2}{4\pi^2}.
\]

**Main conclusions.** Lemma 67.1 is valid, including criticality on all Riemannian variations. The ellipticity and finite-kernel argument in 67.K(B) is valid after a principal-symbol qualification. The principal gap is Step A2: arbitrary \(H^{2,0}\) class changes are not automatically realizable by first-order Kähler deformations. Consequently, full infinitesimal rigidity and coercivity are presently conditional on eliminating this class-changing sector of the aligned kernel. The exact second-order deficit formula is correct; it also clarifies which spectral conclusions survive.

### 1. Lemma 67.1: valid, with the differentiability justification supplied

#### Flux inequality

For a **\(g\)-orthogonal**, orientation-compatible \(J\) with \(c_1(J)=a\), identity 65.1 gives
\[
(t_J^-,\hat h)_g
 =2\pi q-\int_M\langle\Omega_J,B_g^*\hat h\rangle\,d\mu_g.
\]
Because \(|\Omega_J|=\sqrt2\),
\[
\int_M\langle\Omega_J,B_g^*\hat h\rangle
 \le \sqrt2\int_M|B_g^*\hat h|
 =\mathfrak F,
\]
hence
\[
\boxed{2\pi q\,\delta\le(t_J^-,\hat h)_g.}
\]
No positivity assumption on the twist flux or on \(\delta\) is involved. Equality of first Chern classes suffices; homotopy to \(J_0\) is a convenient sufficient condition, not an additional requirement.

#### Differentiability when \(\hat h\) has zeros

At the cscK metric,
\[
B_0=\pi q\,\omega\otimes\hat h,\qquad
v_0:=B_0^*\hat h=\pi q|\hat h|^2\omega.
\]
Thus \(Z(v_0)=Z(\hat h)\). A nonzero harmonic form has a measure-zero zero set. Hodge theory gives smooth metric dependence of \(h_a^-\), its normalization, and \(q\), near \(q>0\).

After smooth bundle identifications, the first derivative of the norm integral is therefore
\[
D\!\left(\int|v|\,d\mu\right)_0(k)
 =
 \int_{M\setminus Z(\hat h)}
 \left\langle\frac{v_0}{|v_0|},v'_k\right\rangle\,d\mu
 +\frac12\int_M|v_0|\operatorname{tr}k\,d\mu.
\]
Dominated convergence proves the two-sided path derivative. In fact, the integral norm is Fréchet differentiable here with respect to \(C^0\) perturbations: split into \(\{|v_0|\le\varepsilon\}\), whose measure tends to zero, and its complement, where the norm has a uniformly controlled quadratic remainder. Composing with the \(C^{2,\alpha}\)-smooth map \(g\mapsto v_g\) proves Fréchet differentiability of \(\mathfrak F,\delta,L\) at \(g_0\).

This argument proves first differentiability, not neighborhood smoothness when zeros are present.

#### Vanishing first derivatives

Since \(L\ge0\) and \(L(g_0)=0\),
\[
DL(g_0)=0.
\]
For an arbitrary two-sided metric curve \(g_t\), orthogonalize \(J_0\) to obtain \(\widehat J_t\). Its intrinsic torsion is \(O(t)\), and the frame twist is quadratic in that torsion. Thus
\[
(t_{\widehat J_t}^-,\hat h_t)=O(t^2),\qquad
\delta(g_t)\le Ct^2.
\]
Differentiability and the two signs of \(t\) imply \(D\delta(g_0)=0\).

The exact ledger now yields
\[
p-q^2=q^2(\delta^2-2\delta)+L,\qquad
D(p-q^2)(g_0)=0.
\]

#### Identification with LeBrun’s functional

Gauss–Bonnet and signature give, in the supplied curvature-operator norms,
\[
p=\frac{P}{8\pi^2}
 =\frac1{2\pi^2}\int|W^+|^2
  +\frac1{96\pi^2}\int s^2-(2\chi+3\tau).
\]
For the almost-complex class \(a=c_1(J_0)\), \(a^2=2\chi+3\tau\), while
\[
q^2=|a^-|_g^2=|a^+|_g^2-a^2.
\]
Consequently,
\[
\boxed{p-q^2=C_+(g)-|a^+|_g^2.}
\]

Every cscK metric is therefore a critical point of this functional on the full space of Riemannian metrics. The KE case, excluded from the normalized ledger because \(q=0\), follows separately: both \(P\) and \(|a^-|^2\) vanish there and have zero first derivative.

#### Independent first-variation check

Let \(E=\operatorname{Ric}^\circ\). At a constant-scalar metric,
\[
D\int s^2\,d\mu(k)=-2s\int\langle E,k\rangle\,d\mu.
\]
At a cscK surface the Kähler Bach formula, translated to the supplied operator norm, gives
\[
D\int|W^+|^2\,d\mu(k)
 =-\frac{s}{12}\int\langle E,k\rangle\,d\mu.
\]
Equivalently, in the convention \(D\int|W^+|^2=-\int\langle\mathrm{Bach},k\rangle\), the cscK Bach tensor is \(sE/12\). Other Bach conventions must rescale these two formulas together.

For the harmonic representative \(\psi=\rho/(2\pi)\) of \(a\),
\[
D|a^+|^2(k)=\int\langle\psi^+\circ\psi^-,k\rangle\,d\mu.
\]
Using
\[
\psi^+=\frac{s}{8\pi}\omega,\qquad
\psi^-=\frac{\rho_0}{2\pi},\qquad
\omega\circ\rho_0=-E,
\]
one obtains
\[
D|a^+|^2(k)
 =-\frac{s}{16\pi^2}\int\langle E,k\rangle\,d\mu
 =DC_+(k).
\]
The cancellation is exact. Indeed, both
\[
\int s^2-32\pi^2|a^+|^2,\qquad
\int|W^+|^2-\frac{4\pi^2}{3}|a^+|^2
\]
are stationary at cscK metrics.

The supplied materials do not establish whether the combined stationary-functional statement has appeared explicitly in LeBrun’s literature. Its mathematical content follows from classical Bach and Hodge-norm variation formulas; neither a novelty claim nor an exact literature attribution is justified from this bundle.

The conformal check should say “constant-scalar metric,” not “constant-s Yamabe metric”: a positive-scalar cscK metric need not be the Yamabe minimizer.

---

### 2. Part (A): A1 is repairable; A2 contains a genuine gap

#### Moving-line linearization

The harmonic ASD line varies with the metric. Accordingly, the null condition is **not**
\[
B'\in\Lambda^+\otimes\mathbb Rh.
\]
Writing \(B_0=\phi_0\otimes h_0\), the correct equation is
\[
\boxed{B'=\phi'\otimes h_0+\phi_0\otimes h',}
\]
with bundle-motion terms included in a chosen smooth identification. Division must be applied to the relative residual
\[
S_1=B'-(\phi_0\otimes h_t)'_0,
\]
not to raw \(B'\).

At transverse zeros the use of a linearized residual in \(L^2\) is legitimate, but the manuscript should not describe \(F\) as a globally smooth pointwise bundle map. One can choose a smooth aligned comparison \(B_t^{\rm cmp}=\phi_{0,t}\otimes h_t\) with constant amplitude. Its residual is \(O(t)\) uniformly. Both the rank projection and the amplitude residual are bounded by a constant times this residual, including near zeros. Off \(Z(h_0)\), \(F(g_t)/t\) has its usual pointwise limit; dominated convergence gives its \(L^2\) limit. Hence
\[
\ell_2(k)=\|F'_0k\|_2^2
\]
in this interpretation.

#### Smooth division at transverse zeros

At a transverse zero, the three components of the ASD section can be used as normal coordinates \(x_1,x_2,x_3\). Suppose a smooth row \(S=(S_1,S_2,S_3)\) satisfies
\[
S_i x_j-S_j x_i=0.
\]
Then \(S_i=0\) on \(\{x_i=0\}\), so Hadamard division gives \(S_i=x_i f_i\). The relations imply \(f_i=f_j\) on a dense set and hence everywhere. Therefore \(S=f h\) with \(f\) smooth.

This supplies the claimed smooth coefficient row by row. It is a direct smooth division argument; invoking an unspecified algebraic regular-sequence theorem is unnecessary.

#### Linearized Bianchi and \(J\)-invariance

After absorbing the Ricci-block normalization into \(\Phi_t\), the corrected alignment equation gives
\[
\operatorname{Ric}^\circ_t=\Phi_t\circ h_t+O(t^2)
\]
smoothly. Only first-order constancy of scalar curvature is needed:
\[
ds_t=O(t^2).
\]
Lemma 66.D and contracted Bianchi give
\[
h_t(\delta_t\Phi_t)=O(t^2).
\]
Since \(\delta_0\Phi_0=0\), its first coefficient is
\[
h_0(\delta\Phi)'=0.
\]
The ASD endomorphism \(h_0\) is invertible off its zero set. Smoothness then yields \((\delta\Phi)'=0\) everywhere, hence \((d\Phi)'=0\).

The amplitude equation says that \(|\Phi_t|\) is spatially constant through first order. Normalizing, with sign chosen so that \(\Omega_0=\omega\), gives
\[
d\Omega_t=O(t^2).
\]
Thus every null direction produces a **first-order almost-Kähler aligned pair**.

The representation-theoretic claim is correct:
\[
\operatorname{Sym}^2_0
 \cong(\mathbb R\Omega\otimes\Lambda^-)
       \oplus(\Omega^\perp\otimes\Lambda^-).
\]
The first summand is \(J\)-invariant; the second is \(J\)-anti-invariant. This follows because ASD endomorphisms commute with \(J\), while SD endomorphisms perpendicular to \(\Omega\) anticommute with \(J\). Therefore
\[
(\operatorname{Ric}'')'=0.
\]

These conclusions do not yet prove first-order Kählerness.

#### The \(H^{2,0}\) reference deformation fails

For \(\theta=f\,dz^1\wedge dz^2\), the proposed Beltrami differential
\[
\mu\propto\omega^{-1}\bar\theta
\]
has, in holomorphic normal coordinates,
\[
\mu^1_{\bar2}\propto\bar f,\qquad
\mu^2_{\bar1}\propto-\bar f.
\]
Its vector-valued \(\bar\partial\) contains
\[
(\bar\partial\mu)^1_{\bar1\bar2}\propto
\partial_{\bar1}\bar f,\qquad
(\bar\partial\mu)^2_{\bar1\bar2}\propto
\partial_{\bar2}\bar f,
\]
which need not vanish. Exterior closedness of the top-degree holomorphic form does not imply this vector-valued integrability equation.

The precise obstruction is the map
\[
\boxed{
\mathcal P_\omega:H^{0,1}(T^{1,0}M)\longrightarrow H^{0,2}(M),
\qquad [\mu]\longmapsto[\mu\lrcorner\omega].
}
\]
Up to the sign determined by the Beltrami convention, a prescribed \((0,2)\) class change is realizable by a first-order Kähler pair exactly when it lies in \(\operatorname{im}\mathcal P_\omega\). The linearized type equation gives necessity; solving it modulo an exact form, using Kähler Hodge theory, gives sufficiency. The real \((1,1)\) class change is freely realized by varying the Kähler form at fixed \(J_0\).

This is a live gap on the stated product example. For \(M=C_g\times C_h\), \(g,h\ge2\), and \(\omega=\omega_1+\omega_2\),
\[
H^{0,1}(TM)
 =H^{0,1}(TC_g)\oplus H^{0,1}(TC_h).
\]
There are no mixed summands because \(H^0(TC_g)=H^0(TC_h)=0\). Contracting a factor deformation with the factor Kähler form gives zero by type on that curve. Thus
\[
\mathcal P_\omega=0,\qquad h^{0,2}=gh>0.
\]
This disproves the claimed **arbitrary reference realization**, not the theorem itself: it remains possible that the aligned kernel has no such class-changing modes.

#### Moser and the Blair–Ianus Hessian

Once the class change is realizable, subtract a reference first-order Kähler pair. The remaining \(\dot\Omega\) is exact, say \(d\vartheta\). The vector field
\[
\iota_X\omega=-\vartheta
\]
removes it since \(\mathcal L_X\omega=-d\vartheta\).

The condition \((\operatorname{Ric}'')'=0\) survives subtraction. For a first-order Kähler pair, \((\nabla J)'=0\); differentiating this identity spatially yields the first-order curvature commutation identities and hence \((\operatorname{Ric}'')'=0\). This justification does not require integrating the pair into an actual Kähler family.

With the supplied form norm,
\[
\boxed{s^*-s=|\nabla\omega|^2,}
\]
not \(\tfrac12|\nabla\omega|^2\). Since the Hermitian scalar curvature is \((s+s^*)/2\),
\[
\int\frac{s+s^*}{2}\,d\mu=4\pi c_1\cdot[\omega],
\]
and therefore, for \(E(J)=\int|\nabla\omega|^2\,d\mu\),
\[
\int s\,d\mu=4\pi c_1\cdot[\omega]-\frac12E(J).
\]
On the fixed-\(\omega\) compatible space, metric variations are tracefree and \(J\)-anti-invariant. Thus
\[
D\int s\,d\mu(k)=-\int\langle\operatorname{Ric}'',k\rangle\,d\mu,
\qquad
DE(k)=2\int\langle\operatorname{Ric}'',k\rangle\,d\mu.
\]
At the Kähler point,
\[
\operatorname{Hess}E
 =2\int|(\nabla\omega)'|^2\,d\mu.
\]
If \((\operatorname{Ric}'')'=0\), this Hessian vanishes and so does first-order torsion. The manuscript’s factors \(1/4\) and \(4\) should be replaced by \(1/2\) and \(2\); the rigidity mechanism is unchanged.

**Corrected (A).** Under the stated zero-free or transverse-zero hypothesis, a null direction is first-order Kähler whenever its induced \((0,2)\) class change lies in \(\operatorname{im}\mathcal P_\omega\). This includes \(p_g=0\), surjectivity of \(\mathcal P_\omega\), and directions with no \((0,2)\) class change.

---

### 3. Part (B): ellipticity is valid; coercivity depends on the corrected (A)

#### Principal symbol: what the computation actually checks

Metric dependence of the harmonic representative is nonlocal, but its linearization has order zero: it involves Hodge projections and operators of the form \(dG\delta\) applied to an algebraic expression in \(k\). The amplitude average is finite rank. These terms do not change the second-order principal symbol.

There is one important qualification: the displayed Ricci rows use the **gauge-reduced** Ricci symbol. For unrestricted \(k\), the actual symbol is
\[
\sigma_\xi(\operatorname{Ric}')(k)
 =\frac12\bigl(
 |\xi|^2k+\xi\otimes\xi\,\operatorname{tr}k
 -\xi\otimes k(\xi)-k(\xi)\otimes\xi
 \bigr),
\]
up to the common Fourier sign. On the Bianchi-symbol kernel
\[
k(\xi)=\frac12\xi\,\operatorname{tr}k,
\]
this reduces to \(\tfrac12|\xi|^2k\). Thus the matrix checked by the script is equivalent to the actual augmented symbol after adding suitable multiples of the gauge row. It is not literally the unrestricted Ricci symbol.

At a unit covector, vanishing of the augmented symbol gives
\[
k^\circ=\sigma\circ\hat h,\qquad \sigma\perp\omega.
\]
The gauge row implies \(k(\xi,\xi)=\tau/2\), where \(\tau=\operatorname{tr}k\). The scalar row then gives \(\tau=0\). Hence
\[
(\sigma\circ\hat h)\xi=0.
\]
Because
\[
(\sigma\circ\hat h)^2
 =\frac14|\sigma|^2|\hat h|^2\operatorname{Id},
\]
one obtains \(\sigma=0\) and \(k=0\).

This is a complete analytic proof of injectivity. Uniform ellipticity follows from compactness of the unit parameter space. The JSON’s ranks, residuals, and square ratio corroborate it; the sampled value \(0.14839\) is not a certified universal ellipticity constant.

Strictly, the full operator has an elliptic differential principal part plus lower-order pseudodifferential and finite-rank terms. The Douglis–Nirenberg estimate still applies.

#### Rellich and the finite kernel

Define the linear space precisely as
\[
\mathcal S
 =\{k:\beta_{g_0}k=0,\ s'_0(k)\text{ is spatially constant}\}.
\]
Its constant scalar variation satisfies
\[
s'_0(k)=-V^{-1}\int\langle\operatorname{Ric},k\rangle\,d\mu.
\]
For zero-free \(\hat h\), elliptic estimates therefore give
\[
\|k\|_{H^2}
 \le C\bigl(\sqrt{\ell_2(k)}+\|k\|_{L^2}\bigr).
\]
Rellich compactness proves that
\[
K=\ker\ell_2\cap\mathcal S
\]
is finite-dimensional and smooth. With the \(L^2\)-orthogonal projection,
\[
\boxed{\ell_2(k)\ge c_1\|k-\pi_Kk\|_{H^2}^2.}
\]
This conclusion is unconditional under the zero-free assumption; it does not use A2.

#### Reference structures and the order-one upper bound

Assume every element of \(K\) satisfies the corrected (A). Choose first-order Kähler companions on a basis of \(K\), then extend linearly. A genuine nearby almost-complex structure is obtained by a smooth local chart or retraction, followed by metric orthogonalization; the literal expression \(J_0+\dot J_K\) is only a tangent vector, not an almost-complex structure.

For \(\eta=k-\pi_Kk\), the resulting class-\(a\) reference has
\[
\Theta'_{\rm ref}(k)=\Theta'_\perp(\eta).
\]
Consequently,
\[
\boxed{
d_2(k)\le\frac{\tau_{\rm ref,2}(k)}{2\pi q}
 \le C\|\eta\|_{H^1}^2.
}
\]
The signed twist pairing need not be positive; its absolute value is bounded by \(C\|\Theta'_\perp\eta\|_2^2\), which supplies the displayed upper bound. Combining it with the coercive complement estimate proves
\[
d_2(k)\le C\ell_2(k),\qquad c_K>0.
\]

Thus the presently justified coercivity theorem requires only the finite-dimensional condition
\[
\boxed{
[\dot\Omega_k]^{0,2}\in\operatorname{im}\mathcal P_\omega
\quad\text{for every }k\in K.
}
\]
Surjectivity on all \(H^{0,2}\) is sufficient but stronger than necessary.

---

### 4. Exact second-order deficit and its consequences

Put \(v_t=B_t^*\hat h_t\) and \(e_t=\Omega_t^{\rm ref}/\sqrt2\). The exact identity is
\[
\tau_{\rm ref}-2\pi q_t\delta_t
 =\sqrt2\int\bigl(|v_t|-\langle e_t,v_t\rangle\bigr)\,d\mu_t.
\]
Writing \(v_0=|v_0|e_0\), define
\[
w_1=P_{e_0^\perp}v'_0-|v_0|e'_0.
\]
This is the derivative of the component perpendicular to the **moving reference direction**, not merely \(P_{e_0^\perp}v'_0\). Expansion gives
\[
|v_t|-\langle e_t,v_t\rangle
 =\frac{t^2}{2|v_0|}|w_1|^2+o(t^2),
\]
hence
\[
\boxed{
2\pi q\,d_2
 =\tau_{\rm ref,2}
  -\frac1{\sqrt2}\int\frac{|w_1|^2}{|v_0|}\,d\mu.
}
\]
The coefficient and sign in Step 67 are correct.

At transverse zeros, \(v_0\asymp|h_0|^2\), and the perpendicular component contributed by \(B_0^*h'\) vanishes. Thus \(w_1=O(|h_0|)\), and the displayed quotient is locally bounded. The integrated expansion follows by separating a shrinking tubular neighborhood and estimating the norm gap there; its pointwise expansion alone is not a justification.

Two useful consequences:

* **Radical membership.** For a null direction covered by corrected (A), use its first-order Kähler companion as reference. Both its first-order torsion and \(w_1\) vanish. Polarizing the two quadratic terms proves
  \[
  d_2(k,v)=0\quad\text{for every }v.
  \]
  This repairs the radical claim; \(d_2(k)=0\) alone would not suffice for an indefinite quadratic form. It also works under transverse zeros and does not require the finite-kernel argument of (B).

* **The full deficit is not compact-relative.** The torsion term has order one, but the negative square contains order-two curvature variation. Only the upper, potentially positive contribution is compact-relative to \(\ell_2\). Calling the entire pencil compact is incorrect.

There is nevertheless a stronger spectral conclusion. On \(K^\perp\), with \(\ell_2\) as Hilbert norm, the bounded self-adjoint operator representing \(q^2d_2\) has the form
\[
A=T-N,
\]
where \(T\) is compact and self-adjoint and \(N\ge0\) is bounded. Its essential spectrum is nonpositive. If \(d_2>0\) somewhere, its largest positive eigenvalue is attained, and
\[
c_K=\frac1{\lambda_{\max}(A)}.
\]
Positive eigenvalues are discrete, of finite multiplicity, with possible accumulation only at zero. This establishes attainment of the positive generalized Rayleigh quotient **without** falsely asserting a compact pencil.

---

### 5. Taylor expansion, gauge, and the strength of the local statement

When \(\hat h_0\) is zero-free, \(v_0\) is bounded away from zero. Hodge theory and smooth curvature dependence imply that \(\delta,L\) are smooth functionals on a \(C^{2,\alpha}\) metric neighborhood. They are **not functions only of the metric’s 2-jet**: their harmonic-form dependence is global.

The cubic expansions are legitimate:
\[
\delta(g_0+k)=d_2(k)+O(\|k\|_{C^{2,\alpha}}^3),\qquad
L(g_0+k)=\ell_2(k)+O(\|k\|_{C^{2,\alpha}}^3).
\]
A cubic remainder uses \(C^3\) smoothness or a locally Lipschitz Hessian; \(C^2\) alone gives only \(o(\|k\|^2)\).

Under the condition on \(K\) above, for \(c<c_K\) and \(k\in\mathcal S\),
\[
\boxed{
L(g_0+k)\ge c q_0^2\delta(g_0+k)
 -C\|k\|_{C^{2,\alpha}}^3.
}
\]
Replacing \(q_0^2\) by \(q(g_0+k)^2\) changes only the cubic remainder.

This is an assertion on the **linear** constant-scalar/Bianchi space. It should not be conflated with a parametrization of nearby exactly constant-scalar metrics:

* Their displacement satisfies \(s'_0(k)=\text{constant}+O(\|k\|^2)\), not necessarily the exact linear constraint.
* Bianchi-gauge solvability modulo diffeomorphisms requires justification; “harmonic gauge” is not automatically an unrestricted local slice at every background.
* An Ebin divergence slice is an alternative. Using the actual Ricci symbol, the augmented system remains injective: the divergence row gives \(k(\xi)=0\), the scalar row then gives \(\operatorname{tr}k=0\), and the same alignment argument finishes the proof.
* In a genuine slice, the augmented linear constraint operator is underdetermined elliptic. A bounded projection to its kernel converts the quadratic nonlinear constraint error into an \(O(\|k\|^2)\) correction, preserving the cubic functional estimate. This supplies a concrete route without assuming that the constant-scalar locus is a smooth unobstructed manifold.

The branch proposal of a remainder-free Morse–Bott tariff requires additional results not established here: identification of \(K\) with the tangent space of an actual zero manifold, its integrability, and uniform transverse coercivity. Neither finite-dimensionality nor unobstructed complex deformations alone supplies all of these.

Finally,
\[
(p-q^2)_2=\ell_2-2q^2d_2
\]
is correct, and nonnegativity of this Hessian on \(\mathcal S\) is equivalent to \(c_K\ge2\). This is **second-order minimality**, not actual local minimality without higher-order control. The stated \(O(\delta^2)\) tariff remainder is unsupported. The proved remainder is cubic in metric displacement; along a fixed direction with \(d_2>0\), it is generally \(O(\delta^{3/2})\).

---

### 6. Strongest correct theorem and the remaining mathematical object

The verified conclusions are:

1. **Full-metric stationarity:** every cscK surface metric is critical for \(C_+-|c_1^+|_g^2\).
2. **Aligned infinitesimal structure:** under zero-free or transverse-zero hypotheses, every \(\ell_2\)-null direction induces a first-order almost-Kähler pair with first-order \(J\)-invariant Ricci tensor.
3. **Conditional Kähler rigidity:** that pair is first-order Kähler when its \((0,2)\) class change is in \(\operatorname{im}\mathcal P_\omega\); the direction then belongs to the radical of \(d_2\).
4. **Unconditional finite kernel:** when \(\hat h\) is zero-free, the elliptic estimate and finite-dimensionality of \(K\) hold.
5. **Conditional positive coercivity:** if the class-realizability condition holds on \(K\), then \(c_K>0\), with the cubic local inequality and the attained positive spectral characterization above.

The unresolved obstruction is explicit and finite-dimensional in the zero-free case:
\[
\Xi:K\longrightarrow
H^{0,2}(M)/\operatorname{im}\mathcal P_\omega,
\qquad
k\longmapsto[\dot\Omega_k]^{0,2}.
\]
Proving \(\Xi=0\), or directly controlling the deficit on the modes with \(\Xi\ne0\), would close the missing connection. A mode with nonzero \(\Xi\) must have nonzero first-order torsion, but its existence and the sign of its \(d_2\) have not been established.

On \(C_g\times C_h\), \(\mathcal P_\omega=0\), so the concrete unresolved question is whether the aligned constant-scalar kernel has any nonzero \(H^{0,2}\) class variation. It is a constrained linearized problem involving \(DF=0\), constant \(s'\), and gauge—not merely the unconstrained Blair–Ianus Hessian. Any Fredholm formulation must also quotient symplectic-diffeomorphism directions; otherwise the fixed-\(\omega\) Hessian has an infinite-dimensional gauge kernel.

Accordingly, Step 67’s blanket exclusion of infinitesimal non-Kähler aligned modes, and its claim that zero-free products already satisfy full coercivity, should be replaced by the conditional statements above. No conclusion about nonlinear isolation or absence of higher-order bifurcation follows from the infinitesimal assertions alone.