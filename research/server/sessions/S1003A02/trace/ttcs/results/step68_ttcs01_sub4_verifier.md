# TTCS Independent Branch Record

```json
{
  "step_id": 68,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/trace/ttcs/results/step67_ttcs01_verifier1_integration.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/step67_cK_local_coercivity_at_cscK.md",
    "Sessions/S1003A02/trace/ttcs/results/step67_ttcs01_sub1_generator.md"
  ]
}
```

## Task

Read the Step-67 verifier and current §21.11, and state exact replacement mathematics for Theorem 67.K and the product model. Preserve only what is established: Lemma 67.1; moving-line null structure; obstruction P_omega and Xi; corrected Blair-Ianus constants; gauge-reduced ellipticity; finite kernel; conditional c_K>0; cubic metric-displacement remainder and T-N spectral interpretation. Check the proposed product mode independently enough to say whether it bypasses Xi (it is not an ell_2-null direction) and what it establishes about c_K versus 2. Identify any remaining false unconditional wording in §21.11 and give concise corrected statements suitable for insertion.

## Output

# Step 67: corrected Theorem 67.K, the product mode, and replacement text for §21.11

## 0. Summary

1. **What survives from Step 67.** Lemma 67.1, the moving-line null structure, the corrected Blair–Ianus constants, gauge-reduced ellipticity and the finite kernel all stand. Positivity \(c_K>0\) holds only conditionally, through the finite-dimensional obstruction \(\Xi\).

2. **The product mode is not \(\ell_2\)-null.** The twisted-Teichmüller mode \(k=fQ\) on \(\Sigma_1\times\Sigma_2\) has \(\ell_2(k)>0\), so it never meets \(\Xi\). It gives an unconditional upper bound for \(c_K\) and an actual strict local decrease of LeBrun's functional.

3. **The constant in Step 67's generator branch is off by a factor 2.** Evaluated directly on the ledger, the twist term is half the size the branch reports. The decrease threshold is \(\mu<|K_1-K_2|\), not \(\mu<2|K_1-K_2|\).

4. **Stronger conclusion than the branch drew.** \(c_K\) has no positive lower bound over product cscK metrics of fixed topology. The local Kähler tariff \(c_K\ge2\) is false on explicit products.

---

## 1. Replacement mathematics for Theorem 67.K

**Setting.**
- \(g_0\) is cscK with Kähler pair \((J_0,\omega)\), \(\rho_0=2\pi h_a^-\neq0\), \(a=c_1(J_0)\).
- \(\hat h=h_a^-/q\) and \(B_0=\tfrac12\omega\otimes\rho_0=\pi q\,\omega\otimes\hat h\).
- \(\mathcal S\) is the **linear** space
\[
\mathcal S=\{k:\ \beta_{g_0}k=0,\ s_0'(k)\ \text{spatially constant}\}.
\]

**Lemma 67.1 (proved).**
- \(\delta\) and \(L\) are Fréchet differentiable at \(g_0\), with \(D\delta=DL=0\).
- Differentiability holds by dominated convergence even when \(Z(\hat h)\neq\emptyset\). The zero set has measure zero and \(Z(v_0)=Z(\hat h)\).
- Hence \(D\bigl(C_+-|a^+|_g^2\bigr)(g_0)=0\) on all Riemannian metrics, since \(p-q^2=C_+-|a^+|^2_g\).
- Independent check: the Bach variation \(-\tfrac{s}{12}\int\langle E,k\rangle\) and the \(\int s^2\) variation \(-2s\int\langle E,k\rangle\) cancel exactly against \(D|a^+|^2=-\tfrac{s}{16\pi^2}\int\langle E,k\rangle\).
- The KE case (\(q=0\)) follows separately.
- Literature attribution is unresolved from the supplied material.

**Blair–Ianus constants (corrected, form norm \(|\omega|^2=2\)).**
\[
s^*-s=|\nabla\omega|^2,\qquad
\int s\,d\mu=4\pi c_1\cdot[\omega]-\tfrac12E,
\]
\[
DE(k)=2\int\langle\operatorname{Ric}'',k\rangle,\qquad
\operatorname{Hess}E=2\int|(\nabla\omega)'|^2 .
\]
§2 below cross-checks these on an explicit mode.

**Theorem 67.K′.**

**(A) Moving-line null structure.** Assume \(Z(\hat h)\) is empty or transverse, and let \(k\in\mathcal S\) satisfy \(\ell_2(k)=0\).
- The null condition is \(B'=\phi'\otimes h_0+\phi_0\otimes h'\), with bundle motion included. It is not \(B'\in\Lambda^+\otimes\mathbb Rh_0\).
- Row-wise Hadamard division at transverse zeros, linearized Lemma 66.D and \(ds_t=O(t^2)\) give a first-order almost-Kähler pair \((g_0+tk,\Omega_t)\) with:
  - \(\Omega_0=\omega\) and \(d\Omega_t=O(t^2)\);
  - \(\operatorname{Ric}^\circ_t=\Phi_t\circ h_t+O(t^2)\);
  - \((\operatorname{Ric}'')'=0\).
- Define
\[
\mathcal P_\omega:H^{0,1}(T^{1,0})\to H^{0,2},\ [\mu]\mapsto[\mu\lrcorner\omega],
\qquad
\Xi(k)=[\dot\Omega_k]^{0,2}\ \mathrm{mod}\ \operatorname{im}\mathcal P_\omega .
\]
- **If \(\Xi(k)=0\):** subtracting a reference first-order Kähler pair, then applying Moser and the Blair–Ianus Hessian, shows that \(k\) is first-order Kähler.
- Polarization then gives \(d_2(k,\cdot)=0\), so \(k\) lies in the radical of \(d_2\).
- The Beltrami construction \(\mu\propto\omega^{-1}\bar\theta\) is not \(\bar\partial\)-closed in general. On \(C_g\times C_h\) one has \(\mathcal P_\omega=0\) while \(h^{0,2}=gh>0\).

**(B) Finite kernel (unconditional when \(Z(\hat h)=\emptyset\)).**
- The system \((DF,\ s',\ \beta)\) is overdetermined elliptic.
  - The checked matrix is the gauge-reduced symbol. It equals the true augmented symbol after adding multiples of the gauge row.
  - Lower-order Hodge and finite-rank terms do not change the principal symbol.
  - The JSON value 0.148 is sampled, not a certified constant.
- Consequently \(\|k\|_{H^2}\le C(\sqrt{\ell_2(k)}+\|k\|_{L^2})\) on \(\mathcal S\).
- \(K=\ker\ell_2\cap\mathcal S\) is finite-dimensional and smooth, and \(\ell_2\ge c_1\|k-\pi_Kk\|^2_{H^2}\).

**(C) Conditional coercivity.** Assume \(Z(\hat h)=\emptyset\) and \(\Xi|_K=0\).
- Then \(d_2\le C\ell_2\) on \(\mathcal S\), so \(c_K>0\).
- For \(c<c_K\) and \(k\in\mathcal S\):
\[
L(g_0+k)\ge c\,q_0^2\,\delta(g_0+k)-C\|k\|^3_{C^{2,\alpha}} .
\]
- The cubic remainder is in metric displacement. Along a ray with \(d_2>0\) it is \(O(\delta^{3/2})\), not \(O(\delta^2)\).
- \(\delta\) and \(L\) are smooth on a \(C^{2,\alpha}\) neighbourhood but nonlocal. They are not functions of the 2-jet.

**(D) Exact deficit and spectral form.**
- With the moving reference direction, \(w_1=P_{e_0^\perp}v_0'-|v_0|e_0'\) and
\[
2\pi q\,d_2=\tau_{\rm ref,2}-\tfrac1{\sqrt2}\int|w_1|^2/|v_0| .
\]
- Only \(\tau_{\rm ref,2}\) is compact relative to \(\ell_2\). On \(K^\perp\), \(q^2d_2\) is represented by \(A=T-N\), with \(T\) compact and \(N\ge0\) bounded.
- Positive spectrum is discrete. If \(d_2>0\) somewhere, then \(c_K=1/\lambda_{\max}(A)\) and the maximum is attained.

**Second order versus local minimality.**
- The Hessian is \((p-q^2)_2=\ell_2-2q^2d_2\).
- \(c_K\ge2\) is equivalent to second-order minimality on \(\mathcal S\).
- Strict \(c_K<2\) implies actual non-minimality, because \(g_0\) is a \(C^2\) point when \(Z(\hat h)=\emptyset\).

---

## 2. The product mode, checked independently

### 2.1 Setting and the mode

Take \(M=\Sigma_1\times\Sigma_2\) with genera at least 2, \(K_1\neq K_2<0\), and \(r=(K_1-K_2)/2\). Then:
- \(\rho_0=r(\omega_1-\omega_2)\) and \(q=|r|\sqrt{2V}/(2\pi)\);
- \(\hat h=\sigma(\omega_1-\omega_2)/\sqrt{2V}\), with \(\sigma=\operatorname{sign}r\).

Let \(Q\) be a holomorphic quadratic differential on \(\Sigma_1\). Let \(\Delta_2f=\mu f\) with \(\mu>0\). Set \(k=fQ\) on the \(T\Sigma_1\) block.

**Membership in the slice and compatibility.**
- \(\operatorname{tr}k=0\), \(\delta k=f\,\delta_1Q=0\) and \(s'(k)=-K_1f\operatorname{tr}_1Q=0\). So \(k\in\mathcal S\).
- \(k\) is \(J_0\)-anti-invariant, so it is a fixed-\(\omega\) compatible variation.
- With \(A=g_1^{-1}Q\), the realization \(g_t=g_1(e^{tfA}\cdot,\cdot)\oplus g_2\), \(J_t=e^{-tfA}J_1\oplus J_2\) keeps \(\omega=\omega_1+\omega_2\) fixed. The family is exactly almost-Kähler.

### 2.2 Ricci variation

- Using \(\nabla^*\nabla Q=-2K_1Q\) and \(\mathring Rk=-K_1k\), one gets \(\operatorname{Ric}'=(K_1+\mu/2)k\). This agrees with the generator branch.
- The term \(K_1g_{1,t}\) is \(J_t\)-invariant. Hence \(\operatorname{Ric}''_1=(\mu/2)k\), and the \(J_t\)-invariant Ricci form \(K_1\omega_1+K_2\omega_2\) is unchanged. So \(\rho'_{0}=0\).

### 2.3 Moving-line structure, computed exactly

- The splitting stays orthogonal and the area forms are fixed. Therefore \(\omega_1-\omega_2\) remains \(g_t\)-ASD and closed, and \(h_t=h_0\) exactly.
- The tensor \(r(g_{1,t}-g_2)\) equals the aligned comparison \(\omega\circ(\omega_1-\omega_2)\) for \(g_t\), with constant amplitude.
- Hence
\[
\operatorname{Ric}^\circ_t=r(g_{1,t}-g_2)+t\tfrac\mu2 k+O(t^2).
\]
- The residual \(\tfrac\mu2k\) lies in \(\omega^\perp\otimes\hat h^\perp\). Composites \(\sigma\circ h_0\) with \(\sigma\perp\omega\) are mixed-block, while \(k\) is \(\Sigma_1\)-block.
- \(B_0=\tfrac12\omega\otimes\rho_0\) gives \(|B|^2=|\operatorname{Ric}^\circ|^2/4\). Therefore
\[
\boxed{\ell_2(k)=\frac{\mu^2}{32\pi^2}\|k\|_2^2>0 .}
\]
- **The mode is not \(\ell_2\)-null.** Its \(\mu\to0\) limit is a Teichmüller kernel element, which has \(\Xi=0\).

### 2.4 Deficit

- \(k^*\hat h=0\), so \(v_t=v_0+O(t^2)\), \(e_t=\omega/\sqrt2\) is constant, and \(w_1=0\).
- The exact deficit identity with reference \(J_t\) gives \(2\pi q\,d_2=\tau_2\).

### 2.5 Torsion

The only nonzero first-order components are
\[
(\nabla_a\omega)'_{b\beta}=-(\nabla_a\omega)'_{\beta b}
=\tfrac12\bigl[Q_{ab}(\iota_{\nabla f}\omega_2)_\beta-f_\beta(\omega_1Q)_{ba}\bigr].
\]
The two terms are orthogonal. In the form norm this gives
\[
\int|(\nabla\omega)'|^2=\tfrac\mu2\|k\|^2 .
\]

**Cross-check.** This matches the corrected Blair–Ianus Hessian exactly:
\[
\operatorname{Hess}E=2\int\langle(\operatorname{Ric}'')',k\rangle=\mu\|k\|^2=2\int|(\nabla\omega)'|^2 .
\]
With the uncorrected factor 4, the two sides would disagree.

### 2.6 Twist pairing

- Write \(\nabla\Omega=\alpha\otimes\Omega_2+\beta\otimes\Omega_3\). The almost-Kähler condition gives \(\beta=\pm J\alpha\), so \(|\nabla\Omega|^2=4|\alpha|^2\).
- Here \(\alpha\in T^*\Sigma_1\), so \(t^-=\varepsilon|\alpha|^2(\omega_1)^-=\varepsilon|\alpha|^2(\omega_1-\omega_2)/2\). The sign \(\varepsilon=\pm1\) is fixed by the convention \(t=\alpha\wedge\beta\) and is common to both factors.
- Therefore
\[
\tau_2=\frac{\varepsilon\sigma\mu\|k\|^2}{8\sqrt{2V}},\qquad
q^2d_2=\frac{\varepsilon\sigma|r|\mu}{32\pi^2}\|k\|^2 .
\]

### 2.7 Result

\[
\boxed{\;8\pi^2(p-q^2)_2(fQ)=\frac\mu4\bigl(\mu-\varepsilon\sigma|K_1-K_2|\bigr)\|fQ\|^2\;}
\]
The interchanged family \(hQ_2\), with \(\Delta_1h=\lambda h\), carries \(-\varepsilon\sigma\) in place of \(\varepsilon\sigma\). So exactly one family has \(d_2>0\), and for it
\[
\frac{\ell_2}{q^2d_2}=\frac{2\mu}{|K_1-K_2|} .
\]

### 2.8 Comparison with the generator branch

The branch's (7) reads \((\mu/4)(\mu+2(K_1-K_2))\). Its twist term is twice the direct ledger value.

The discrepancy enters at its (5). There \(\int u_2=\mu/4\) comes from the tensor-sum norm \(|df|^2|Q|^2\) of \(\nabla\omega\). The form norm, which is consistent with \(u=|\nabla\Omega|^2/4\), \(s^*-s=|\nabla\omega|^2\) and the Hessian check above, gives half of that.

My evaluation does not use the reduced identity (1). It uses only the ledger definitions, the exact deficit identity and the computed torsion. Which factor carries the decreasing family depends on \(\varepsilon\). I did not fix \(\varepsilon\) independently; the branch places \(Q\) on the more curved factor.

### 2.9 What the mode establishes (independent of \(\Xi\))

**Bound P.** On every product with \(K_1\neq K_2<0\) and genera at least 2,
\[
c_K\le\frac{2\lambda_1(\Sigma_{j})}{|K_1-K_2|}\le\frac{2\max_i\lambda_1(\Sigma_i)}{|K_1-K_2|},
\]
where \(j\) is the factor carrying the eigenfunction of the \(d_2>0\) family. Equivalently, \(\lambda_{\max}(A)\ge|K_1-K_2|/(2\lambda_1(\Sigma_j))\).

**Consequences.**
- If \(\max_i\lambda_1(\Sigma_i)<|K_1-K_2|\), then \(c_K<2\).
- Such products exist. Pinching a separating geodesic sends \(\lambda_1\to0\) at fixed curvature, for example by a Cheeger-constant test function across a thin collar. Pinch on both factors, so the result does not depend on \(\varepsilon\).
- At such a product, the cscK metric is **not a local minimizer** of \(C_+-|c_1^+|^2_g\), even among exactly constant-scalar metrics:
  - The scalar curvature is corrected by an \(O(t^2)\) conformal factor, using the invertible operator \(6\Delta-2s\) with \(s<0\).
  - Since \(D(p-q^2)(g_0)=0\) and the functional is \(C^2\) at zero-free \(g_0\), one gets \(p-q^2=t^2\,8\pi^{-2}\!\cdot\tfrac{1}{8}(\ldots)\); concretely \(p-q^2=t^2(\ell_2-2q^2d_2)+O(t^3)<0\).
- At fixed topology \(\Sigma_g\times\Sigma_h\), \(\inf c_K=0\) over zero-free product cscK metrics. The qualitative constant of (C) has no uniform positive lower bound.
- The necessary condition for \(c_K\ge2\) is \(\lambda_1(\Sigma_j)\ge|K_1-K_2|\), not \(2|K_1-K_2|\).
- Sufficiency is open. It requires the remaining mixed blocks:
  - scalar Hessians \((\nabla^2f)_0\), with \(\|(\nabla^2f)_0\|^2=\tfrac12\lambda(\lambda-2K_i)\|f\|^2\);
  - anti-linear products \(df_\lambda\cdot dg_\mu\);
  - harmonic and coexact one-form blocks.

**Interpretation.**
- The descent direction is non-Kähler and non-aligned (\(\ell_2>0\)).
- The mechanism is order-one exceptional twist against order-two Ricci rotation: \(d_2\propto|K_1-K_2|\mu\) against \(\ell_2\propto\mu^2\).
- It is the \(T\) part of \(A=T-N\) with \(N\)-contribution zero (\(w_1=0\)).
- It does not affect conditional positivity \(c_K>0\), because \(\mu\ge\lambda_1>0\).
- It does not concern \(X\#k\overline{\mathbb{CP}}^2\) directly. It does show that no local Kähler tariff \(p\ge q^2\) holds at all cscK metrics.

---

## 3. Corrected text for §21.11

**Organization, item 2.** Replace "By 67.K(A) they do not bifurcate infinitesimally from cscK" with:

> Under zero-free or transverse \(Z(\hat h)\), an \(\ell_2\)-null direction at cscK induces a first-order almost-Kähler pair with \((\operatorname{Ric}'')'=0\). It is first-order Kähler, and lies in \(\operatorname{rad}d_2\), when \(\Xi(k)=0\). Aligned non-Kähler infinitesimal modes are excluded only on \(\{\Xi=0\}\). On \(C_g\times C_h\), \(\mathcal P_\omega=0\) and \(h^{0,2}=gh\), so \(\Xi\) is not automatically zero.

**Organization, item 3.** Replace the coercivity sentence and "That is open" with:

> For zero-free \(\hat h\), \(K=\ker\ell_2\cap\mathcal S\) is finite-dimensional. Then \(c_K>0\) holds if \(\Xi|_K=0\). The sharp form \(c_K\ge2\), which is equivalent to second-order local minimality of \(C_+-|c_1^+|^2_g\), does not hold in general: on \(\Sigma_1\times\Sigma_2\), \(c_K\le2\lambda_1(\Sigma_j)/|K_1-K_2|\). This bound is \(<2\) and tends to 0 as \(\lambda_1\to0\). On blow-ups the comparison with 2 is open.

**67.1 bullet.** Keep it, but replace the Burns sentence with:

> Where a cscK metric exists on \(X\#k\overline{\mathbb{CP}}^2\), it has \(p-q^2=0\), while Cor. 59.KE gives metrics with \(p<k\le q^2\). On the product cscK metrics of §2 it is not even a local minimizer.

**67.K(A) bullet.** Replace "[P] … Every … ℓ₂(k)=0 is first-order Kähler … H^{2,0} directions use the ∂̄-closed Beltrami ω⁻¹θ̄ … ker ℓ₂ ⊂ rad d₂, the seed alternative does not occur" with statement (A) of §1. Specifically:
- moving-line equation;
- Hadamard division;
- the obstruction \(\mathcal P_\omega,\Xi\);
- constants \(\int s=4\pi c_1\cdot[\omega]-\tfrac12E\), \(DE=2\int\langle\operatorname{Ric}'',k\rangle\), \(\operatorname{Hess}E=2\|(\nabla\omega)'\|^2\);
- the radical conclusion only on \(\{\Xi=0\}\).

**67.K(B) bullet.**
- Replace "If Z(ĥ)=∅, then d₂≤Cℓ₂" with (B) and (C) of §1, so that \(c_K>0\) is conditional on \(\Xi|_K=0\).
- State that the symbol check concerns the gauge-reduced Ricci symbol.
- Replace "This covers Σ₁×Σ₂ with K₁≠K₂" with: "finite kernel holds; Teichmüller, Kähler-class and diffeomorphism modes in \(K\) have \(\Xi=0\); whether \(K\) contains modes with nonzero \((0,2)\) class variation is open."
- Replace "d₂ is compact relative to ℓ₂" with the \(T-N\) statement.
- Replace "smooth functions of the 2-jet" with "smooth nonlocal functionals on a \(C^{2,\alpha}\) neighbourhood".
- Note that the corollary holds on the linear \(\mathcal S\) with cubic displacement remainder.

**Step-67 note, §1.** Replace "\(p\ge q^2[1-(2-c_K)_+\delta]+O(\delta^2)\)" with "\(+O(\|k\|^3_{C^{2,\alpha}})\), generally \(O(\delta^{3/2})\) along rays".

**Open items.** Replace "the value of c_K relative to 2 … finite spectral computation" with:

> Product twisted-Teichmüller modes give \(8\pi^2(p-q^2)_2=\tfrac\mu4(\mu\mp|K_1-K_2|)\|fQ\|^2\). Hence \(c_K<2\) whenever \(\lambda_1\) of the relevant factor is below \(|K_1-K_2|\). Open:
> - the remaining product blocks, needed to decide whether \(c_K\ge2\) when \(\lambda_1\ge|K_1-K_2|\);
> - \(\Xi|_K\) on products;
> - the weighted estimate at transverse \(Z(\hat h)\);
> - the analogue on cscK blow-ups, where \(\hat h\) generically has zeros.

**Generator branch.** Its (7), (8) and (11) carry the factor-2 discrepancy described in §2.8. Its phrase "non-Kähler sub-\(|c_1^-|^2\) branch" should read "descent direction with \(\ell_2>0\)".

---

## 4. Unresolved items

- **The sign \(\varepsilon\).** It decides which factor carries the descending family. One evaluation of \(t=\alpha\wedge\beta\) against identity 65.1 on this mode, for instance with the Step-65 twist code, would fix it. Bound P with \(\max_i\lambda_1\) does not depend on it.

- **\(\Xi|_K\) on products and on blow-ups.** This needs a constrained computation: \(DF=0\), constant \(s'\) and gauge, taken modulo symplectic diffeomorphisms. It is not the unconstrained Blair–Ianus Hessian.

- **Sufficiency of the threshold.** Whether \(\lambda_1\ge|K_1-K_2|\) gives \(c_K\ge2\) on products depends on the remaining small symmetric blocks. Their entries are polynomial in \(\lambda,\mu,K_1,K_2\), using the identities listed in §2.9.