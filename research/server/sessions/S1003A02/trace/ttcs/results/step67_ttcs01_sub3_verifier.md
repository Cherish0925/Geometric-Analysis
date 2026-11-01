# TTCS Independent Branch Record

```json
{
  "step_id": 67,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step67_cK_local_coercivity_at_cscK.md",
    "Sessions/S1003A02/workspace/notes/step66_rank_one_exceptional_ricci_rigidity.md",
    "Sessions/S1003A02/workspace/notes/step65_cell_exceptional_flux_ledger.md",
    "Sessions/S1003A02/workspace/scripts/step67_cK_symbol_check.py",
    "Sessions/S1003A02/workspace/data/step67_cK_symbol_check.json"
  ]
}
```

## Task

Check, as a careful differential geometer, the new results in step67_cK_local_coercivity_at_cscK.md, which sit on the ledger of step65 §1/§7 and step66 (whose §7 corrections are binding). Setting: compact complex surface, cscK metric g0 with Kähler form omega, primitive Ricci form rho0 = 2*pi*h_a^- != 0 (a = c1), unit exceptional harmonic ASD form hhat, ledger p = q^2(1-delta)^2 + L. Verify or correct, with exact reasons: (1) Lemma 67.1: the inequality 2*pi*q*delta <= (t_J^-, hhat) for every class-a orientation-compatible J (from 65.1 and |Omega_J|=sqrt2), the argument that delta and L have zero first variation at cscK, differentiability of 𝔉 at g0 when Z(hhat) is nonempty, and the identity p - q^2 = C_+ - |c1^+|^2_g, hence 'every cscK metric is a critical point of LeBrun's C_+ - |c1^+|^2 on all metrics'. Is this known in the literature (LeBrun's curvature functionals)? Is it consistent with the first variations of int|W+|^2 (Bach tensor of Kähler metrics) and int s^2? (2) Theorem 67.K(A): Koszul division at transversal zeros; the linearized use of Lemma 66.D (div(phi o psi)=psi(delta phi)) to make the Ricci-aligned SD form first-order closed; the J-invariance claim (J-anti-invariant tracefree symmetric tensors = Omega^perp ⊗ Lambda^-); the reference first-order Kähler deformation realizing an arbitrary class change, especially the H^{2,0} directions via the Beltrami differential omega^{-1} theta-bar; Moser; and the Blair–Ianus Hessian argument: int s dmu = 4 pi c1.[omega] - kappa int|nabla omega|^2 on omega-compatible J (check s* - s >= 0 proportional to |nabla omega|^2 and the topological integral of the Hermitian scalar curvature), first variation d(int s)(gdot) = -int<Ric'',gdot>, and Hess E = 2||(nabla omega)'||^2. (3) Theorem 67.K(B): the Douglis–Nirenberg ellipticity of (DF, s', harmonic gauge) with the principal symbol stated (numerically checked in data/step67_cK_symbol_check.json), the Rellich/finite-kernel step, the order-one upper bound d2 <= (2 pi q)^{-1} tau_ref,2 with the reference structure built from J_K on ker l2, and the exact second-order formula 2 pi q d2 = tau_ref,2 - (1/sqrt2) int |w1|^2/|v0|. Identify any gap (e.g. whether the second-order Taylor statement in C^{2,alpha} is legitimate, whether the slice/gauge handling is right, whether K finite-dimensional is correctly used). Return precise corrections and the strongest correct statements.

## Output

# Scientific verification memo

## 1. Lemma 67.1

### 1.1 Flux inequality

With \(\hat h=h_a^-/\|h_a^-\|_2\) and \(q=(h_a^-,\hat h)=\|h_a^-\|_2\), (65.1) gives
\[
(t_J^-,\hat h)
 =2\pi q-\int_M\langle \Omega_J,B^*\hat h\rangle\,d\mu .
\]
Since \(|\Omega_J|=\sqrt2\),
\[
\int_M\langle \Omega_J,B^*\hat h\rangle
 \le \sqrt2\int_M|B^*\hat h|
 =\mathfrak F,
\]
and therefore
\[
(t_J^-,\hat h)\ge 2\pi q-\mathfrak F=2\pi q\,\delta .
\]
This is correct for every orientation-compatible \(J\) homotopic to \(J_0\), hence with \(c_1(J)=a\).

### 1.2 First derivative of \(\mathfrak F\) when \(Z(\hat h)\neq\varnothing\)

At the cscK metric,
\[
B_0=\tfrac12\omega\otimes\rho_0
    =\pi q\,\omega\otimes\hat h,
\qquad
v_0:=B_0^*\hat h
    =\pi q\,|\hat h|^2\omega .
\]
Thus \(Z(v_0)=Z(\hat h)\). A nonzero harmonic form has a measure-zero zero set. For a smooth metric path, \(v_t=B_t^*\hat h_t\) varies continuously in \(C^0\), and dominated convergence gives
\[
\left.\frac d{dt}\right|_0\int |v_t|\,d\mu_t
 =
 \int_{M\setminus Z(\hat h)}
 \left\langle \frac{v_0}{|v_0|},\dot v\right\rangle d\mu
 +\text{volume term}.
\]
The zero set contributes no integral term. Hence the first path derivative of \(\mathfrak F\), and therefore of \(\delta\), exists without the zero-free assumption. In a \(C^{2,\alpha}\) metric neighborhood one can also obtain Fréchet differentiability from
\[
\big||v_0+w|-|v_0|-\langle v_0/|v_0|,w\rangle\big|
 \le 2|w|\,\mathbf 1_{\{|v_0|\le \varepsilon\}}
      +C_\varepsilon |w|^2
\]
and \(\mu\{|v_0|\le\varepsilon\}\to0\).

Second derivatives require more care. At a transverse zero, \(v_0=O(r^2)\) while the first variation orthogonal to \(v_0\) is \(O(r)\), so the usual term
\[
\frac{|\dot v_\perp|^2}{|v_0|}
\]
is locally bounded. Thus the transverse-zero hypothesis is adequate for the quadratic expansion, but the natural target is a weighted \(L^2\) space rather than a globally smooth pointwise bundle map.

### 1.3 Vanishing first derivatives

Since \(L\ge0\) and \(L(g_0)=0\), differentiability along two-sided smooth paths gives \(DL(g_0)=0\).

For a metric path \(g_t\), orthogonalize \(J_0\) with respect to \(g_t\). This preserves its homotopy class. Its intrinsic torsion is \(O(t)\), while the twist \(t_J^-\) is quadratic in that torsion, so
\[
(t_{\hat J_t}^-,\hat h_t)=O(t^2).
\]
The flux inequality gives
\[
\delta(g_t)\le Ct^2 .
\]
Since \(\delta(g_t)\) has a two-sided first derivative, applying this to \(t>0\) and \(t<0\) yields \(D\delta(g_0)=0\).

Consequently,
\[
D(p-q^2)(g_0)=0.
\]

### 1.4 Identification with \(C_+-|c_1^+|^2\)

The chiral Chern–Weil formula gives
\[
p=\frac1{8\pi^2}\int|\operatorname{Ric}^\circ|^2
  =C_+-c_1^2.
\]
Since
\[
c_1^2=|c_1^+|_g^2-|c_1^-|_g^2
\quad\text{and}\quad
q^2=|c_1^-|_g^2,
\]
one obtains exactly
\[
p-q^2=C_+(g)-|c_1^+|_g^2.
\]

Thus every non-KE cscK metric is a critical point of this functional on the full space of Riemannian metrics, not merely on Kähler or constant-scalar variations. The KE case also follows: both
\(\int|\operatorname{Ric}^\circ|^2\) and \(|c_1^-|^2\) vanish there and have zero first derivative.

### 1.5 Direct Bach-tensor verification

Let \(E=\operatorname{Ric}^\circ\) and let \(h=\dot g\). With the standard Bach convention,
\[
D\int|W^+|^2=-\int\langle \mathrm{Bach},h\rangle,
\qquad
\mathrm{Bach}=\frac{s}{12}E
\]
at a cscK surface. Also
\[
D\int s^2=-2s\int\langle E,h\rangle.
\]
Therefore
\[
DC_+(h)=-\frac{s}{16\pi^2}\int\langle E,h\rangle.
\]

The harmonic representative of \(a=c_1\) is
\[
\frac{\rho}{2\pi}=\frac{s}{8\pi}\omega+\frac{\rho_0}{2\pi}.
\]
The stress-energy variation of its Hodge norm gives
\[
D|c_1^+|^2(h)
 =-\frac{s}{16\pi^2}\int\langle E,h\rangle,
\]
using \(\omega\circ\rho_0=-E\) in the stated conventions. Hence the two first variations agree exactly. This independently verifies Lemma 67.1.

The conformal comment should say only that \(\int s^2\) is stationary at every constant-scalar metric in dimension four. A positive-scalar cscK metric need not be the Yamabe representative of its conformal class.

No supplied source passage states this exact stationary-functional result. It follows directly from standard Kähler Bach and Hodge-variation formulas, so a historical novelty attribution is not presently established.

---

## 2. Theorem 67.K(A)

### 2.1 Linearized aligned tensor and transverse zeros

The tensor entering the division argument is not the raw derivative \(\dot B\). Because the harmonic ASD line moves with \(g\), the correct object is the derivative of the aligned residual,
\[
\dot B_{\mathrm{rel}}
 =\left.\frac d{dt}\right|_0
   \big(B_t-\Phi_0\otimes h_t\big),
\]
after fixed bundle identifications. Equivalently,
\[
\dot B=\dot\Phi\otimes h+\Phi_0\otimes\dot h
\]
when the linearized rank residual vanishes.

At a transverse zero, the three local components of \(h\) form a regular sequence. If a smooth vector of components \(S_j\) satisfies
\[
S_jh_k-S_kh_j=0
\]
off the zero set, Koszul exactness gives \(S_j=f h_j\) with \(f\) smooth. Applied separately to the SD components of \(\dot B_{\mathrm{rel}}\), this supplies a smooth \(\dot\Phi\). The manuscript should replace “\(B'_a=f_a h\)” by this moving-line version.

### 2.2 Linearized Bianchi identity

Once
\[
\operatorname{Ric}^\circ_t=\Phi_t\circ h_t+O(t^2),
\]
Lemma 66.D gives
\[
\operatorname{div}_t(\Phi_t\circ h_t)
   =h_t(\delta_t\Phi_t).
\]
Only first-order constancy of scalar curvature is needed:
\[
ds_t=O(t^2),
\]
so contracted Bianchi gives \(h_t(\delta_t\Phi_t)=O(t^2)\). Since a nonzero ASD form acts invertibly on one-forms, the first coefficient of \(\delta_t\Phi_t\) vanishes off \(Z(h)\), and smoothness extends it across \(Z(h)\).

The amplitude equation gives spatial constancy of \(|\Phi_t|\) through first order. Hence
\[
\Omega_t=\sqrt2\,\frac{\Phi_t}{|\Phi_t|}
\]
satisfies \(d\Omega_t=O(t^2)\). Moreover, under
\[
\operatorname{Sym}^2_0
 \cong\Lambda^+\otimes\Lambda^-,
\]
the \(J_t\)-anti-invariant tensors are precisely
\[
\Omega_t^\perp\otimes\Lambda^-.
\]
Thus the aligned rank condition gives
\[
(\operatorname{Ric}'')_t=O(t^2).
\]
This part is sound after the moving-line correction.

### 2.3 The \(H^{2,0}\) reference deformation is not valid in general

The real \((1,1)\) harmonic component
\[
\lambda\omega+H_0
\]
is realized by a first-order Kähler deformation with \(J_0\) fixed. Exact components are removed by the first-order Moser argument. The difficulty is the asserted realization of every \(H^{2,0}\oplus H^{0,2}\) component.

For \(\theta=f\,dz^1\wedge dz^2\), the proposed Beltrami tensor
\[
\mu=\omega^{-1}\bar\theta
\]
has, in holomorphic normal coordinates,
\[
\mu^1_{\bar2}\sim\bar f,\qquad
\mu^2_{\bar1}\sim-\bar f.
\]
Consequently,
\[
(\bar\partial\mu)^1_{\bar1\bar2}
 \sim \partial_{\bar1}\bar f,\qquad
(\bar\partial\mu)^2_{\bar1\bar2}
 \sim \partial_{\bar2}\bar f,
\]
which generally do not vanish. The identity \(d\theta=0\) only controls the fully alternating exterior derivative; it does not imply \(\bar\partial(\omega^{-1}\bar\theta)=0\).

The relevant cohomological map is the polarized Kodaira–Spencer map
\[
\mathcal P_\omega:
H^{0,1}(T^{1,0}M)\longrightarrow H^{0,2}(M),
\qquad
[\mu]\longmapsto[\mu\lrcorner\omega].
\]
An \(H^{0,2}\) class is realizable by a first-order Kähler deformation exactly when it lies in the image of this map. Surjectivity is not automatic for a compact Kähler surface.

Therefore the proof presently establishes:

* every \(\ell_2\)-null direction produces a first-order almost-Kähler aligned pair with \((\operatorname{Ric}'')'=0\);
* it is first-order Kähler when its \(H^{0,2}\) class lies in \(\operatorname{im}\mathcal P_\omega\);
* in particular, this holds when \(H^{0,2}(M)=0\), when \(\mathcal P_\omega\) is surjective, or for class-preserving directions.

Without such an additional hypothesis, part (A), including the assertion about all of \(\ker\ell_2\), is not proved. Any remaining infinitesimal aligned mode is confined to this polarized \(H^{0,2}\) class-changing sector.

### 2.4 Blair–Ianus constants

With the Step-63 convention
\[
u=\frac14|\nabla\omega|^2,
\]
the almost-Kähler identity is
\[
s^*-s=|\nabla\omega|^2,
\]
not \(\frac12|\nabla\omega|^2\). Since
\[
\int\frac{s+s^*}{2}\,d\mu
 =4\pi c_1\cdot[\omega],
\]
one has
\[
\int s\,d\mu
 =4\pi c_1\cdot[\omega]-\frac12E(J),
\qquad
E(J)=\int|\nabla\omega|^2d\mu.
\]
On \(\mathcal J_\omega\),
\[
D\!\left(\int s\,d\mu\right)(\dot g)
 =-\int\langle\operatorname{Ric}'',\dot g\rangle,
\]
so
\[
DE_J(\dot g)
 =2\int\langle\operatorname{Ric}'',\dot g\rangle,
\]
rather than the displayed factor \(4\). At a Kähler structure,
\[
\operatorname{Hess}E(\dot J,\dot J)
 =2\int|(\nabla\omega)'|^2.
\]
The factor correction does not alter the rigidity conclusion once the deformation has been reduced to fixed \(\omega\).

Under the polarized Kodaira–Spencer hypothesis, the resulting \(\ker\ell_2\) directions are in the radical of \(d_2\): their first-order torsion vanishes, and their first-order Ricci-rotation term also vanishes. The latter point should be stated explicitly; \(d_2(k)=0\) alone would not imply radical membership for an indefinite quadratic form.

---

## 3. Theorem 67.K(B)

### 3.1 Principal symbol and ellipticity

For \(\hat h\neq0\), the principal second-order part of \(DF\) comes from the linearized tracefree Ricci tensor. Variation of the harmonic representative \(\hat h_g\) is a global elliptic operator of order at most zero in \(\dot g\), so it does not alter the displayed principal symbol.

The symbol argument is correct. The \(DF\) rows leave
\[
\dot g^\circ=\sigma\circ\hat h,\qquad \sigma\perp\omega.
\]
The harmonic-gauge row gives
\[
(\sigma\circ\hat h)\xi=\frac{\tau}{4}\xi,
\qquad \tau=\operatorname{tr}\dot g,
\]
and the scalar row then gives \(\tau/2=0\). Finally,
\[
(\sigma\circ\hat h)^2
 =\frac14|\sigma|^2|\hat h|^2\operatorname{Id}
\]
forces \(\sigma=0\). Thus the symbol is injective.

The random singular-value computation is corroborative only. Uniform ellipticity follows analytically from injectivity and compactness of the unit \((\hat h/|\hat h|,\xi)\)-parameter space.

Strictly speaking, \(DF\) is not a purely local differential operator because \(\hat h_g\) is determined by global Hodge projection and the amplitude mean is global. It is an elliptic differential principal part plus lower-order pseudodifferential and finite-rank terms. The same Gårding estimate follows.

### 3.2 Finite-dimensional kernel and coercive complement

For \(\dot g\in\mathcal S\),
\[
s'(\dot g)
 =-V^{-1}\int\langle\operatorname{Ric},\dot g\rangle,
\]
so its constant value is controlled by \(\|\dot g\|_{L^2}\). The elliptic estimate therefore has the form
\[
\|\dot g\|_{H^2}
 \le C\big(\sqrt{\ell_2(\dot g)}+\|\dot g\|_{L^2}\big).
\]
Rellich compactness then gives finite-dimensional
\[
K=\ker\ell_2\cap\mathcal S
\]
and, for an \(L^2\)-orthogonal projection \(\pi_K\),
\[
\ell_2(\dot g)
 \ge c\|\dot g-\pi_K\dot g\|_{H^2}^2.
\]
This part is correct.

### 3.3 Reference structures and the dependence on part (A)

If each \(k\in K\) admits a first-order Kähler companion, those companions can be selected linearly: choose them on a basis of the finite-dimensional \(K\) and extend linearly. After projecting or exponentiating to genuine almost-complex structures, orthogonalization gives a smooth class-\(a\) family.

Then
\[
\Theta'(\dot g)
 =\Theta'_\perp(\dot g-\pi_K\dot g),
\]
and the flux inequality gives
\[
2\pi q\,d_2(\dot g)
 \le \tau_{\mathrm{ref},2}(\dot g)
 \le C\|\dot g-\pi_K\dot g\|_{H^1}^2.
\]
Combining this with the \(H^2\) estimate yields
\[
d_2(\dot g)\le C\ell_2(\dot g).
\]

Because the general form of part (A) has the unresolved \(H^{0,2}\) sector, this coercivity conclusion currently holds under the same extra hypothesis on \(K\): every \(K\)-direction must have its class variation in \(\operatorname{im}\mathcal P_\omega\). In particular it holds when \(H^{0,2}=0\) or \(\mathcal P_\omega\) is surjective.

### 3.4 Exact second-order formula

Starting from
\[
\tau_{\mathrm{ref}}
 =2\pi q-\int\langle\Omega^{\mathrm{ref}},v\rangle,
\qquad
2\pi q\,\delta
 =2\pi q-\sqrt2\int|v|,
\]
where \(v=B^*\hat h\), one gets
\[
\tau_{\mathrm{ref}}-2\pi q\,\delta
 =\int\left(\sqrt2|v|-\langle\Omega^{\mathrm{ref}},v\rangle\right).
\]
Writing \(e=\Omega^{\mathrm{ref}}/\sqrt2\) and decomposing the first variation of \(v\) as parallel plus \(w_1\perp e\),
\[
|v_t|-\langle e_t,v_t\rangle
 =\frac{t^2}{2|v_0|}|w_1|^2+O(t^3).
\]
Therefore
\[
2\pi q\,d_2
 =\tau_{\mathrm{ref},2}
  -\frac1{\sqrt2}\int\frac{|w_1|^2}{|v_0|}.
\]
The coefficient is correct.

This gives a one-sided order-one bound on the positive part of \(d_2\). The full quadratic form also contains the order-two term
\[
-\frac1{\sqrt2}\int\frac{|w_1|^2}{|v_0|}.
\]
Thus \(d_2\) itself is not compact relative to \(\ell_2\) in a two-sided quadratic-form sense; rather, its positive values are controlled by the order-one torsion term.

### 3.5 Taylor expansion and slice formulation

When \(Z(\hat h)=\varnothing\), \(v_0\) is bounded away from zero. Curvature depends smoothly on the \(2\)-jet, and the harmonic representative depends smoothly and globally on the metric through elliptic Hodge theory. Hence \(\delta\) and \(L\) are smooth functionals on a \(C^{2,\alpha}\) metric neighborhood, and
\[
L(g_0+h)=\ell_2(h)+O(\|h\|_{C^{2,\alpha}}^3),
\qquad
\delta(g_0+h)=d_2(h)+O(\|h\|_{C^{2,\alpha}}^3).
\]
The manuscript should not call them “functions of the \(2\)-jet”: their harmonic-form dependence is nonlocal.

For \(h\) in the linear slice \(\mathcal S\), the stated estimate follows:
\[
L(g_0+h)
 \ge c\,q_0^2\,\delta(g_0+h)
   -C\|h\|_{C^{2,\alpha}}^3,
\qquad c<c_K.
\]
Replacing \(q_0\) by \(q(g_0+h)\) only changes the cubic remainder.

If the intended statement concerns nearby exactly constant-scalar metrics in an affine Bianchi slice, their displacement \(h\) satisfies
\[
ds'_{g_0}(h)=O(\|h\|^2)
\]
rather than belonging exactly to the linear \(\mathcal S\). The augmented elliptic estimate can absorb this quadratic source and retain a cubic remainder, but that nonlinear-slice argument is not written in Step 67.

Also, the earlier prose
\[
p\ge q^2[1-(2-c_K)_+\delta]+O(\delta^2)
\]
is stronger than the proved Taylor information. The available remainder is cubic in the metric displacement; along a direction with \(d_2>0\) this is typically \(O(\delta^{3/2})\), not \(O(\delta^2)\).

---

## 4. Strongest established formulation

With the corrections above:

1. **Lemma 67.1 is valid**, including criticality on all Riemannian variations. It is independently confirmed by the Bach and Hodge-norm first variations.

2. **The first part of 67.K(A) is valid:** an \(\ell_2\)-null direction produces a first-order aligned almost-Kähler deformation with first-order \(J\)-invariant Ricci tensor.

3. **Full infinitesimal Kähler rigidity holds** when the resulting \(H^{0,2}\) class lies in the image of the polarized Kodaira–Spencer map. This includes \(H^{0,2}=0\), surjectivity of \(\mathcal P_\omega\), and class-preserving directions.

4. **The elliptic and finite-kernel portions of 67.K(B) are valid** for zero-free \(\hat h\).

5. **The coercivity \(d_2\le C\ell_2\), hence \(c_K>0\), is valid** when every direction in \(K\) satisfies the polarized Kodaira–Spencer condition above.

The central unresolved mathematical object is therefore finite-dimensional and explicit: the \(H^{0,2}\) class variation of the aligned kernel \(K\), measured against
\[
\mathcal P_\omega:H^{0,1}(T^{1,0})\to H^{0,2}.
\]
The current argument does not eliminate torsion-bearing aligned modes in the complement of its image.