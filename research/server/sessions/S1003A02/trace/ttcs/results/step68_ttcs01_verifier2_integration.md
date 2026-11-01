# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 68,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step68_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step68_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Read the Step-67 verifier and current §21.11, and state exact replacement mathematics for Theorem 67.K and the product model. Preserve only what is established: Lemma 67.1; moving-line null structure; obstruction P_omega and Xi; corrected Blair-Ianus constants; gauge-reduced ellipticity; finite kernel; conditional c_K>0; cubic metric-displacement remainder and T-N spectral interpretation. Check the proposed product mode independently enough to say whether it bypasses Xi (it is not an ell_2-null direction) and what it establishes about c_K versus 2. Identify any remaining false unconditional wording in §21.11 and give concise corrected statements suitable for insertion.

## Integrated Scientific Memo

## Replacement mathematics for Step 67 and §21.11

Use
\[
q=\|h_a^-\|_2>0,\qquad \widehat h=h_a^-/q,\qquad
\delta=1-\frac{\mathfrak F}{2\pi q},\qquad
L=\frac{P/2-\mathfrak F^2}{4\pi^2},
\]
so that
\[
p=\frac{P}{8\pi^2}=q^2(1-\delta)^2+L.
\]
All quadratic coefficients below are coefficients of \(t^2\), not second derivatives.

### 1. Lemma 67.1 survives

For every **\(g\)-orthogonal**, orientation-compatible \(J\) with \(c_1(J)=a\),
\[
\boxed{2\pi q\,\delta\le (t_J^-,\widehat h)_g.}
\]
This follows directly from
\[
(t_J^-,\widehat h)=2\pi q-\int\langle\Omega_J,B^*\widehat h\rangle,
\qquad |\Omega_J|=\sqrt2.
\]

At the non-KE cscK metric,
\[
B_0=\pi q\,\omega\otimes\widehat h,\qquad
v_0=B_0^*\widehat h=\pi q|\widehat h|^2\omega.
\]
The zero set of a nonzero harmonic form has measure zero. The integral norm \(v\mapsto\int|v|\) is therefore Fréchet differentiable at \(v_0\) in the \(C^0\) topology: split the integral into \(\{|v_0|\le\varepsilon\}\) and its complement. Smooth Hodge dependence then gives differentiability of \(\mathfrak F,\delta,L\) at \(g_0\), without a zero-free hypothesis.

Orthogonalizing \(J_0\) along an arbitrary two-sided metric curve gives torsion \(O(t)\), hence twist flux \(O(t^2)\). The inequality above implies \(D\delta(g_0)=0\). Since \(L\ge0\) and \(L(g_0)=0\), also \(DL(g_0)=0\). Consequently,
\[
\boxed{D(p-q^2)(g_0)=0,\qquad
p-q^2=C_+(g)-|a^+|_g^2.}
\]
Thus every cscK metric is stationary for \(C_+-|c_1^+|_g^2\) on **all Riemannian variations**. At KE metrics, where the normalized deficit is undefined, stationarity follows separately from \(P=|a^-|^2=0\).

The supplied first-variation formulas are consistent:
\[
D\!\int s^2(k)=-2s\int\langle E,k\rangle,\qquad
D\!\int|W^+|^2(k)=-\frac{s}{12}\int\langle E,k\rangle,
\]
\[
D|a^+|^2(k)=-\frac{s}{16\pi^2}\int\langle E,k\rangle=DC_+(k),
\qquad E=\Ric^\circ.
\]
The conformal check requires constant scalar curvature, not Yamabe-minimizing status. An exact literature attribution is not established by the supplied sources.

---

## 2. Theorem 67.K′: the strongest justified replacement

Let
\[
\mathcal S=\{k:\beta_{g_0}k=0,\ s'_0(k)\text{ is spatially constant}\},
\qquad K=\ker\ell_2\cap\mathcal S.
\]
Here \(\mathcal S\) is a **linear constraint space**, not an asserted parametrization of the nonlinear constant-scalar locus.

### (A) Moving-line null structure and conditional rigidity

Assume \(Z(\widehat h)\) is empty or transverse. If \(k\in\mathcal S\) and \(\ell_2(k)=0\), the alignment equation is
\[
\boxed{B'_0=\dot\Phi\otimes h_0+\Phi_0\otimes\dot h,}
\]
with bundle-motion terms included. Raw \(B'_0\) need not lie in \(\Lambda^+\otimes\mathbb Rh_0\).

At transverse zeros, apply division to the residual after subtracting a moving aligned comparison. In normal coordinates \(h=(x_1,x_2,x_3)\), the relations
\[
S_ix_j-S_jx_i=0
\]
give \(S_i=fx_i\) with \(f\) smooth by row-wise Hadamard division. Linearized Lemma 66.D and contracted Bianchi then yield
\[
\Ric^\circ_t=\Phi_t\circ h_t+O(t^2),\qquad
d\Omega_t=O(t^2),\qquad (\Ric'')'_0=0.
\]
The amplitude equation supplies first-order spatial constancy of \(|\Phi_t|\), permitting normalization to \(\Omega_t\).

**Unconditional conclusion:** every null direction induces a first-order almost-Kähler aligned pair with first-order \(J\)-invariant Ricci tensor.

First-order Kählerness requires the class-realization condition. Define
\[
\mathcal P_\omega:
H^{0,1}(T^{1,0}M)\longrightarrow H^{0,2}(M),
\qquad [\mu]\longmapsto[\mu\lrcorner\omega],
\]
and
\[
\boxed{\Xi(k)=[\dot\Omega_k]^{0,2}
\pmod{\operatorname{im}\mathcal P_\omega}.}
\]
A prescribed \((0,2)\) class variation is realizable by a first-order Kähler pair precisely when it lies in \(\operatorname{im}\mathcal P_\omega\). The claimed automatic construction
\(\mu\propto\omega^{-1}\bar\theta\) is invalid: exterior closedness of \(\theta\) does not imply the vector-valued equation \(\bar\partial\mu=0\).

If \(\Xi(k)=0\), subtract such a reference Kähler pair, remove the remaining exact form variation by Moser, and apply Blair–Ianus. In the supplied form norms the correct constants are
\[
s^*-s=|\nabla\omega|^2,\qquad
\int s=4\pi c_1\cdot[\omega]-\frac12E,
\qquad E=\int|\nabla\omega|^2,
\]
\[
DE(k)=2\int\langle\Ric'',k\rangle,\qquad
\operatorname{Hess}E(k,k)=2\int|(\nabla\omega)'_k|^2.
\]
Hence
\[
\boxed{\Xi(k)=0\ \Longrightarrow\
k\text{ is first-order Kähler and }d_2(k,\cdot)=0.}
\]
The radical conclusion uses polarization of the torsion and moving-direction squares; \(d_2(k)=0\) alone would not prove it.

For products of curves of genera at least two,
\[
\boxed{\mathcal P_\omega=0,\qquad h^{0,2}=g_1g_2>0.}
\]
Indeed, \(H^{0,1}(TM)\) consists only of factor deformations because \(H^0(T\Sigma_i)=0\), and their contractions vanish by factor dimension. This refutes arbitrary class realization, but does **not** prove that the constrained kernel contains a mode with \(\Xi\ne0\).

### (B) Unconditional ellipticity and finite kernel under zero-freeness

Assume \(Z(\widehat h)=\varnothing\). The augmented system \((DF,s',\beta)\) has injective principal symbol. The true Ricci symbol is
\[
\sigma_\xi(\Ric')(k)=\frac12\left(
|\xi|^2k+\xi\otimes\xi\,\tr k
-\xi\otimes k(\xi)-k(\xi)\otimes\xi\right),
\]
up to a common Fourier sign. On the Bianchi-symbol kernel it reduces to \(\tfrac12|\xi|^2k\). Thus the numerical matrix checks a **gauge-reduced** symbol, equivalent to the actual augmented symbol after row operations.

Vanishing of that augmented symbol implies
\[
k^\circ=\sigma\circ\widehat h,\quad \sigma\perp\omega,\quad
\tr k=0,\quad(\sigma\circ\widehat h)\xi=0.
\]
Since
\[
(\sigma\circ\widehat h)^2
=\frac14|\sigma|^2|\widehat h|^2\operatorname{Id},
\]
one gets \(k=0\). Hodge-dependent terms are lower-order pseudodifferential terms; amplitude averages are finite rank.

Therefore
\[
\|k\|_{H^2}\le C\bigl(\sqrt{\ell_2(k)}+\|k\|_{L^2}\bigr),
\]
\(K\) is finite-dimensional and smooth, and
\[
\boxed{\ell_2(k)\ge c_1\|k-\pi_Kk\|_{H^2}^2.}
\]
The sampled singular value \(0.148\) is not a certified universal constant. Likewise, the “ungauged kernel consists exactly of Ricci rotations” computation should not be presented as a statement about the unrestricted true Ricci symbol.

### (C) Conditional positive coercivity and its actual remainder

If, additionally,
\[
\boxed{\Xi|_K=0,}
\]
choose first-order Kähler companions linearly on \(K\), realize them through a genuine almost-complex chart, and orthogonalize. With \(\eta=k-\pi_Kk\),
\[
d_2(k)\le\frac{\tau_{\mathrm{ref},2}(k)}{2\pi q}
\le C\|\eta\|_{H^1}^2.
\]
Together with (B), this proves
\[
\boxed{d_2\le C\ell_2,\qquad c_K>0.}
\]

When \(\widehat h\) is zero-free, \(\delta,L\) are smooth **nonlocal** functionals on a \(C^{2,\alpha}\) neighborhood. Thus, for \(0<c<c_K\) and small \(k\in\mathcal S\),
\[
\boxed{L(g_0+k)\ge c q_0^2\delta(g_0+k)
-C\|k\|_{C^{2,\alpha}}^3.}
\]
Replacing \(q_0^2\) by \(q(g_0+k)^2\) changes only the cubic term. Along a fixed ray with \(d_2>0\), the remainder is generally \(O(\delta^{3/2})\), **not** \(O(\delta^2)\).

A corresponding assertion for nearby exactly constant-scalar metrics requires a justified diffeomorphism slice and an \(O(\|k\|^2)\) projection onto the linear constraint space. No nonlinear isolation or remainder-free tariff follows from the theorem above.

### (D) Exact deficit and the correct spectral interpretation

Put
\[
v_t=B_t^*\widehat h_t,\qquad e_t=\Omega_t^{\mathrm{ref}}/\sqrt2,\qquad
w_1=P_{e_0^\perp}v'_0-|v_0|e'_0.
\]
Then
\[
\boxed{2\pi q\,d_2
=\tau_{\mathrm{ref},2}
-\frac1{\sqrt2}\int\frac{|w_1|^2}{|v_0|}.}
\]
The derivative of the **moving reference direction** is essential. At transverse zeros \(w_1=O(|h_0|)\); the integrated expansion requires the zero-neighborhood estimate, not merely a pointwise Taylor formula.

Under the hypotheses of (C), on \(K^\perp\) with the \(\ell_2\)-Hilbert norm, the operator representing \(q^2d_2\) is
\[
\boxed{A=T-N,\qquad T\text{ compact self-adjoint},\quad N\ge0\text{ bounded}.}
\]
The entire pencil is not compact. Its essential spectrum is nonpositive; positive eigenvalues are discrete, of finite multiplicity, and can accumulate only at zero. If \(d_2>0\) somewhere,
\[
\boxed{c_K=\lambda_{\max}(A)^{-1},}
\]
with the maximum attained.

Finally,
\[
(p-q^2)_2=\ell_2-2q^2d_2,
\]
so \(c_K\ge2\) is equivalent to **second-order** minimality on \(\mathcal S\), not actual local minimality without higher-order information.

---

## 3. Product model: corrected coefficient, sign, and explicit Rayleigh quotient

Let
\[
M=\Sigma_1\times\Sigma_2,\qquad K_1\ne K_2<0,\qquad
r=\frac{K_1-K_2}{2},
\]
with
\[
\omega=\omega_1+\omega_2,\qquad \rho_0=r(\omega_1-\omega_2).
\]
Take a real holomorphic quadratic differential \(Q\) on \(\Sigma_1\), regarded as a tracefree Codazzi tensor, and
\[
\Delta_2f=\mu f,\qquad \mu>0,\qquad k=fQ.
\]
Then
\[
\tr k=0,\qquad\delta k=0,\qquad s'(k)=0,
\]
so \(k\in\mathcal S\). The family
\[
g_t=g_1(e^{tfA}\,\cdot,\cdot)\oplus g_2,\qquad A=g_1^{-1}Q,
\]
is fixed-\(\omega\) compatible. Its factor area forms remain fixed.

### Independent checks

The identities
\[
\nabla^*\nabla Q=-2K_1Q,\qquad \mathring Rk=-K_1k
\]
give
\[
\Ric'(k)=\left(K_1+\frac\mu2\right)k,\qquad
(\Ric'')_1=\frac\mu2k.
\]
The moving primitive \(J\)-invariant Ricci form has zero first variation.

The harmonic ASD form \(\omega_1-\omega_2\) remains harmonic exactly along this family, so \(q_t=q_0\). The residual relative to the moving aligned tensor is \(\frac\mu2k\), orthogonal to the aligned ASD line. Using \(|B|^2=|\Ric^\circ|^2/4\),
\[
\boxed{\ell_2(fQ)=\frac{\mu^2}{32\pi^2}\|fQ\|_2^2>0.}
\]
Thus the proposed mode is **not a null direction**, and \(\Xi\) is not evaluated on it.

The torsion computation in form norms gives
\[
|(\nabla\omega)'|^2=\frac12|Q|^2|df|^2,\qquad
\int u_2=\frac\mu8\|fQ\|_2^2.
\]
This also follows from the corrected Blair–Ianus Hessian:
\[
2\int|(\nabla\omega)'|^2
=2\int\langle(\Ric'')_1,k\rangle
=\mu\|k\|_2^2.
\]
The generator’s torsion value is twice too large.

The sign can be fixed without an unresolved twist convention. Write
\[
T_i(t)=\tr_{g_{i,t}}\Ric_{ii}(g_t),\qquad
I=\|fQ\|_2^2.
\]
For the determinant-preserving block family, the horizontal Ricci formula gives
\[
\int (T_2)_2=-\frac14\int|df|^2|Q|^2=-\frac\mu4I.
\]
Blair–Ianus gives \((\int s)_2=-\mu I/4\), hence \(\int(T_1)_2=0\). Expanding \(|\Ric|^2-s^2/4\) therefore yields
\[
P_2=\frac{\mu^2}{4}I
+(K_1-K_2)\left(\int(T_1)_2-\int(T_2)_2\right).
\]
Since \(q\) is constant,
\[
\boxed{
8\pi^2(p-q^2)_2(fQ)
=\frac\mu4\bigl(\mu+K_1-K_2\bigr)\|fQ\|_2^2.
}
\]
This independently fixes both the factor-two correction and which factor descends.

For the exchanged family,
\[
\boxed{
8\pi^2(p-q^2)_2(hQ_2)
=\frac\lambda4\bigl(\lambda+K_2-K_1\bigr)\|hQ_2\|_2^2.
}
\]

### Consequences for \(c_K\)

If \(K_1<K_2\),
\[
q^2d_2(fQ)=\frac{(K_2-K_1)\mu}{64\pi^2}\|fQ\|_2^2>0,
\]
and
\[
\boxed{\frac{\ell_2(fQ)}{q^2d_2(fQ)}
=\frac{2\mu}{K_2-K_1},\qquad
c_K\le\frac{2\lambda_1(\Sigma_2)}{K_2-K_1}.}
\]
Hence descent occurs precisely when
\[
\boxed{0<\mu<K_2-K_1,}
\]
not when \(\mu<2(K_2-K_1)\). The factor-swapped statement applies when \(K_2<K_1\).

For example, \(K_1=-2,K_2=-1\) and \(\lambda_1(\Sigma_2)<1\) give \(c_K<2\). Such surfaces exist by pinching a separating geodesic: a test function nearly constant on the two sides has Rayleigh quotient tending to zero.

At fixed product topology and fixed unequal curvatures, degenerating the relevant factor therefore gives
\[
\boxed{\inf_{\text{product cscK metrics}}c_K=0.}
\]
This asserts absence of a uniform positive lower bound; it does **not** establish positivity at each individual product, which still requires resolving \(\Xi|_K\) or another kernel estimate.

The mode keeps \(\omega\) fixed and has \(w_1=0\). It is a non-Kähler, **non-aligned** descent direction, with \(\ell_2>0\); it does not resolve or contradict the outstanding null-kernel obstruction. At \(\mu=0\), it becomes a genuine Teichmüller Kähler mode.

An \(O(t^2)\) conformal correction makes scalar curvature exactly constant, since \(6\Delta-2s\) is invertible for \(s<0\). Lemma 67.1 ensures that this correction leaves the quadratic coefficient unchanged. Thus these examples are actual local non-minima even among constant-scalar metrics.

The threshold above is only a necessary condition for \(c_K\ge2\) on a fixed product. Its sufficiency requires the remaining scalar-derived and mixed one-form tensor blocks.

---

## 4. Concise insertion text for §21.11

### Replace Organization items 2–3

> **Aligned end.** Under zero-free or transverse \(Z(\widehat h)\), every constant-scalar \(\ell_2\)-null direction induces a first-order almost-Kähler aligned pair with \((\Ric'')'=0\). It is first-order Kähler, and lies in \(\operatorname{rad}d_2\), when its obstruction \(\Xi\) vanishes. The blanket exclusion of infinitesimal non-Kähler aligned modes is not established.
>
> **Kähler end.** Zero-free \(\widehat h\) gives ellipticity, a finite-dimensional kernel \(K\), and coercivity on \(K^\perp\). Positivity \(c_K>0\) follows if \(\Xi|_K=0\). The condition \(c_K\ge2\) is equivalent to second-order minimality of \(C_+-|c_1^+|^2\), but is false in general: twisted-Teichmüller product modes give \(c_K\le2\lambda_1(\Sigma_{\rm less\ curved})/|K_1-K_2|\). The analogous comparison on cscK blow-ups remains unresolved.

### Replace the 67.K(A) and 67.K(B) result bullets

> **67.K(A), corrected.** The null equation follows the moving harmonic ASD line. Division of the relative residual and linearized 66.D give first-order almost-Kähler alignment. Define \(\mathcal P_\omega[\mu]=[\mu\lrcorner\omega]\) and \(\Xi(k)=[\dot\Omega_k]^{0,2}\bmod\operatorname{im}\mathcal P_\omega\). If \(\Xi(k)=0\), Moser and Blair–Ianus imply first-order Kählerness and \(d_2(k,\cdot)=0\). The constants are \(\int s=4\pi c_1\cdot[\omega]-E/2\), \(DE=2\int\langle\Ric'',k\rangle\), and \(\operatorname{Hess}E=2\|(\nabla\omega)'\|_2^2\).
>
> **67.K(B), corrected.** When \(\widehat h\) is zero-free, the actual augmented symbol is injective after gauge reduction; \(K\) is finite-dimensional and \(\ell_2\ge c_1\|k-\pi_Kk\|_{H^2}^2\). If \(\Xi|_K=0\), then \(d_2\le C\ell_2\), \(c_K>0\), and \(L\ge cq_0^2\delta-C'\|k\|_{C^{2,\alpha}}^3\) on the linear constraint space. The spectral operator is \(T-N\), with \(T\) compact and \(N\ge0\) bounded—not a compact pencil.

### Other unconditional wording requiring correction

- **“This covers locally homogeneous products.”** Replace by: finite-kernel ellipticity covers these products; full positive coercivity has not been established because \(\Xi|_K\) is unresolved.
- **“The value against 2 is open.”** Qualify: it is already \(<2\) on the products above; remaining product blocks and blow-up cases remain open.
- **“\(\delta,L\) are functions of the metric 2-jet.”** Replace by: smooth nonlocal \(C^{2,\alpha}\) functionals near a zero-free background.
- **“No infinitesimal seed occurs,” or “no bifurcation/isolation follows.”** Restrict the infinitesimal exclusion to \(\Xi=0\); no nonlinear isolation follows.
- **“Metric deficit is the minimal class-\(a\) twist flux” in 66.J.** The universally established statement is the lower bound. Equality additionally requires a smooth pointwise Ricci-aligned structure **with \(c_1=a\)**; zero-freeness alone does not guarantee that Chern class globally.
- **Restricted tariff \(\delta\le\delta_0\).** State \(\delta_0\le1\) when concluding \(p\ge q^2(1-\delta_0)^2\).
- Keep the constant-scalar reduction explicitly subject to the stated all-conformal-class negativity input.

The remaining scientific objects are precise: the constrained finite-dimensional map \(\Xi\), the elliptic estimate across transverse zeros, and the remaining low product tensor blocks. The explicit product mode settles neither of the first two, but decisively disproves a universal \(c_K\ge2\) and supplies the exact bound \(c_K\le2\lambda_1/|K_1-K_2|\).