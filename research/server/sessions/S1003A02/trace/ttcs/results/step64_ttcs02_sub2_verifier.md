# TTCS Independent Branch Record

```json
{
  "step_id": 64,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/trace/ttcs/results/step64_ttcs01_generator1_integration.md",
    "Sessions/S1003A02/workspace/notes/step64_diffuse_twist_AAD_and_SW_zeros.md",
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Independently check the new results proposed by the Step-64 Generator integration, which were not part of the original verifier task. Concentrate on: (i) the exact harmonic-ASD test identity obtained by pairing the second AAD Bianchi equation with eta_h(Z)=nabla_{h(Z)} Omega, including the algebraic contraction, signs, factors, and the constant-s assumption; (ii) the claimed global second-jet estimate ||nabla^2 Omega||_2 + ||nabla Omega||_4^2 <= C||Rm||_2 for every closed almost-Kähler four-manifold—derive it carefully and identify norm/convention dependencies; (iii) the flux inequality (4-6U)||T|| <= ... and exactly what it can establish; and (iv) the regularized Berry/Chern form ledger gamma_delta and the limiting transverse-zero formula, including line-bundle conventions, signs, smoothness through zeros, transition-term order, and Hopf transgression. Separate proved identities from attractive but unproved construction implications. Provide corrected exposable statements.

## Output

# Verification memo: Step-64 Generator integration, items (i)–(iv)

The four items come out as follows:

- **(i)** The harmonic-ASD pairing identity (5)–(8) is correct, and so is the corrected moment identity (9).
- **(ii)** The global second-jet estimate (10) is correct on every closed almost-Kähler four-manifold.
- **(iii)** The flux inequality (13) is correct. However, the exact identity (63.3) forces its right-hand side to be at least comparable to its left-hand side, in every regime with \(U<2/3\). As a norm inequality, (13) therefore cannot produce a lower bound on \(P\) without explicit constants and a cancellation inside \(\mathcal F_h\).
- **(iv)** The regularized ledger (17)–(23) is correct for transverse zeros. Its \(\delta\to0\) limit (20) is exactly the Gauss identity (1) on the punctured manifold, so the new information lives entirely at finite \(\delta\).

Conventions throughout are those of AAD:
- \(\nabla\Omega=a\otimes\phi-Ja\otimes J\phi\), with \(|\Omega|^2=|\phi|^2=2\);
- \(u=|a|^2=|\nabla\Omega|^2/4\) and \(\kappa-s=6u\);
- 2-form inner products use the determinant convention;
- \(t^-:=-(a\wedge Ja)^-\), and \(\gamma_J^-=\rho_0+t^-\).

---

## (i) The harmonic-ASD test of the second AAD equation

### Algebra (5)

Take the frame \(a=e^1\), \(Je_1=e_2\), \(Je_3=e_4\). Then:
- \(Je^1=e^2\) (from \((J\alpha)_X=-\alpha_{JX}\));
- \(\Omega=e^{12}+e^{34}\) and \(a\wedge Ja=e^{12}\);
- \(V_X=e^1(X)\phi-e^2(X)J\phi\);
- \(t^-=-\tfrac12(e^{12}-e^{34})\) and \(|t^-|^2=\tfrac12=u^2/2\).

The ASD basis is \(e^{12}-e^{34}\), \(e^{13}+e^{24}\), \(e^{14}-e^{23}\), using \(*e^{13}=-e^{24}\) and \(*e^{14}=e^{23}\).

| \(h\) | \(h(e_1),h(e_2)\) | \(\sum_i\langle V_{Je_i},V_{h(e_i)}\rangle\) | \(-4\langle t^-,h\rangle\) |
|---|---|---|---|
| \(e^{12}-e^{34}\) | \(e_2,\,-e_1\) | \(\langle -J\phi,-J\phi\rangle+\langle-\phi,-\phi\rangle=4\) | \(4\) |
| \(e^{13}+e^{24}\) | \(e_3,\,e_4\) | \(0\) (since \(V_{e_3}=V_{e_4}=0\)) | \(0\) |
| \(e^{14}-e^{23}\) | \(e_4,\,-e_3\) | \(0\) | \(0\) |

Both sides are linear in \(h\in\Lambda^-\) and invariant under the gauge change \(\phi\mapsto e^{i\theta}\phi\). Hence (5) holds identically.

The structural reason is that \(h\) agrees with \(\pm J\) on \(D^\perp=\operatorname{span}(a^\sharp,Ja^\sharp)\) exactly through its \(\bar\Omega\)-component. This matches (4): \(t^-=\tfrac u2\bar\Omega\), where the opposite structure is \(\bar\Omega=-e^{12}+e^{34}\).

Taking \(h=\rho_0\) in (5) gives \(\sum\langle V_{\rho_0e_i},V_{Je_i}\rangle=-4\langle\rho_0,t^-\rangle\). Contracting AAD (38) with \(V_{Je_i}\), and using \(\sum|V_{Je_i}|^2=4u\), then gives (9) with coefficient \(+4\), confirming the correction of the earlier \(-2\).

### Pairing (6)–(8)

AAD (38) is the \([\![\Lambda^{0,2}]\!]\)-component of (33). Each \(V_{h(e_i)}\) lies in \([\![\Lambda^{0,2}]\!]\), so pairing with (38) is the same as pairing with (33).

The term \(\tfrac16 d(\kappa-s)=du\) is correct. The \(\tfrac\kappa4\) term contributes \(-\kappa\langle t^-,h\rangle=-(s+6u)\langle t^-,h\rangle\) pointwise. This gives the pointwise identity
\[
0=-(s+6u)\langle t^-,h\rangle+f_h,
\]
valid for **every** ASD \(h\), harmonic or not, where \(f_h\) is the integrand of (7).

Two inputs are then needed to reach (6):
- **Harmonicity of \(h\)** replaces \(\int\langle t^-,h\rangle\) by \(\langle\mathsf H^-(t^-),h\rangle\).
- **Constancy of \(s\)** pulls \(s\) outside the integral. If \(s\) is not constant, (6) acquires the extra term \(\int(s-\bar s)\langle t^-,h\rangle\) on the left.

The signs in (7) match (38) term by term, so (8) at \(s=-4\) is correct.

### Status of (i)

(5), (6), (7), (8) and (9) are proved identities for every closed almost-Kähler four-manifold of constant scalar curvature.

---

## (ii) The second-jet estimate (10)

### Derivation

**Step 1: harmonicity.** A closed self-dual form is harmonic, so the Weitzenböck formula gives
\[
\nabla^*\nabla\Omega=2W^+\Omega-\tfrac s3\Omega.
\]
This agrees with AAD (19)–(20), using \(W_2^+(\Omega)=\rho_*''\):
\[
2W^+\Omega-\tfrac s3\Omega=\tfrac{\kappa-s}3\Omega+2\rho_*''=\nabla^*\nabla\Omega.
\]

**Step 2: constant norm.** Since \(|\Omega|^2\) is constant,
\[
|\nabla\Omega|^2=\langle\nabla^*\nabla\Omega,\Omega\rangle=\tfrac23(\kappa-s)=4u.
\]
Hence \(|\nabla\Omega|^2\le C(|W^+|+|s|)\le C|\mathrm{Rm}|\) pointwise, and so \(\|\nabla\Omega\|_4^2\le C\|\mathrm{Rm}\|_2\).

**Step 3: Bourguignon's formula** (AAD (40)) for \(V=\nabla\Omega\), integrated over closed \(M\):
\[
\|\nabla V\|_2^2=\|d^\nabla V\|_2^2+\|\delta^\nabla V\|_2^2-\int\langle V_{\operatorname{Ric}(\cdot)}+R\cdot V,V\rangle .
\]
The three pieces are controlled as follows:
- \(d^\nabla V=[J,R_{X,Y}]\), so \(|d^\nabla V|\le C|\mathrm{Rm}|\).
- \(\delta^\nabla V=\nabla^*\nabla\Omega\), so \(|\delta^\nabla V|\le C|\mathrm{Rm}|\).
- The curvature term is at most \(C\int|\mathrm{Rm}||V|^2\le C\|\mathrm{Rm}\|_2^2\), by Step 2.

### Status and dependencies of (10)

(10) is proved. Its ingredients are:
- a **closed** manifold, needed for integration by parts;
- a **global smooth** harmonic self-dual \(\Omega\) of constant length.

No Gray condition is used. The constant \(C\) is universal in dimension four; it depends only on the conventions \(|\Omega|^2=2\), the determinant inner product on \(\Lambda^2\), and the norm on \(\Lambda^2\)-valued 1-forms. Both sides are scale invariant in dimension four (\(\Omega\) rescales by \(\lambda^2\)).

The estimate does **not** transfer to a normalized spinor direction. Near a zero, \(|\nabla\Omega|\sim r^{-1}\) and \(|\nabla^2\Omega|\sim r^{-2}\), and \(\int r^{-4}\,r^3dr\) diverges.

### Quantitative size

Gauss–Bonnet gives
\[
\int|W|^2+\tfrac{s^2}{24}=8\pi^2\chi+\tfrac12P,
\]
so \(\|\mathrm{Rm}\|_2^2\le 8\pi^2\chi(M)+CP\), with \(\chi(M)=c_2(X)+k\).

Thus (10) bounds \(\|\nabla^2\Omega\|_2\) at the scale \(\sqrt{\chi}\gtrsim\sqrt A\). It does not bound it at the scale \(\sqrt k\). The second-jet obstacle is settled **qualitatively** (no curvature derivative is lost), but the bound is of host size, not flux size.

---

## (iii) The flux inequality (13): what it can and cannot establish

### Derivation of (12) and (13)

**(12).** Each term of (7) is integrated by parts once, which removes every curvature derivative:
- **\(\delta W_3^+\), \(\nabla_{J\cdot}\rho_*''\), and \(A^+\)** (via \(d^\nabla\mathrm{Ric}''\) and \(d\rho=*(J\delta\mathrm{Ric}'')\)): the derivative lands on \(V\circ h\), \(J\) and \(*\). This produces \(|\nabla V||h|+|V||\nabla h|+|V|^2|h|\).
- **\(\rho_0\) and \(\rho_*''\)**: these terms are algebraic, \(\le C|\rho||V|^2|h|\).
- **\(du\)**: this goes through (64.7) with \(\eta=J\xi_h\), and gives the same \(B_h\).

Both (12) and (64.7) are correct. In (64.7), \(\|\mathrm{Ric}''\|_2\le\sqrt P\) and \(\|\rho_0\|_2\le\sqrt{P/2}\).

Scaling is consistent:
- \(F_h\) and \(s\langle T,h\rangle\) both scale as \(\lambda^{-2}\);
- \(B_h\) scales as \(\lambda^{-2}\), since \(\|h\|_\infty\) and \(\|\nabla h\|_4\) do;
- \(E_{\rm AAD}\) is invariant.

**(13).** Write \(\int u\langle t^-,h\rangle=\int u\langle T,h\rangle+\int u\langle r,h\rangle\). Bound the first piece by \(U\|T\|\) and the second by \(U\|r\|\). Inserting this into (8) with \(h=T/\|T\|\) gives (13). It is correct.

### What (13) cannot establish

Combine (13) with Proposition 63.AK at \(s=-4\):
\[
2\|\rho_*''\|^2+4\|W_3^+\|^2=P-2\|\gamma_J^-\|^2+4\!\int\!u-5\!\int\!u^2 .
\]
Three facts enter:
- \(\int u\ge U^{-1}\int u^2\);
- \(\|\gamma_J^-\|\le\sqrt{P/2}+(\tfrac12\int u^2)^{1/2}\);
- \(\int u^2\ge 8\pi^2(k+\Pi)-o(k)\) by (64.3).

For \(P=o(k)\) they give
\[
\boxed{\,2\|\rho_*''\|^2+4\|W_3^+\|^2\ \ge\ \bigl(4/U-6\bigr)\,8\pi^2k-o(k)\,}
\tag{A}
\]
so \(E_{\rm AAD}\ge c\,(4/U-6)^{1/2}\sqrt k\).

Next, \(\|h\|_\infty\ge\mathrm{Vol}^{-1/2}\), and at \(s=-4\), \(\int|\mathrm{Rm}|^2\ge\int s^2/24=\tfrac23\mathrm{Vol}\). Hence
\[
B_h\ge\sqrt{2/3}\quad\text{for every }L^2\text{-normalized }h .
\]

Consequences:
- **Small \(U\).** As \(U\to0\), the right-hand side of (13) is at least \(c\sqrt{k/U}\gg 8\pi\sqrt k\ge\) LHS. Inequality (13) then holds automatically for every almost-Kähler family, whatever the harmonic orientation. This extends the Generator's (14) from the diffuse template to every family with \(U\to0\).
- **\(U\in[U_0,2/3)\).** Both sides are of order \(\sqrt k\), with an unspecified universal \(C\). No conclusion follows without explicit constants.
- **Control by \(P\).** \(E_{\rm AAD}\) is in any case not controlled by \(P\).

### What (13) does establish

- **An exact necessary relation.** Any constant-\(s\) almost-Kähler family must satisfy (13). By (2), with \(\|T\|\ge2\pi\sqrt{k+\Pi}-\sqrt{P/2}\), it must therefore finance
  \[
  CE_{\rm AAD}B_h+6U\|r\|\ \ge\ (4-6U)\bigl(2\pi\sqrt{k+\Pi}-\sqrt{P/2}\bigr).
  \]
- **A computable test functional.** For explicit candidate geometries, \(\mathcal F_h\) can be evaluated directly.
- **The location of any future gap mechanism.** A lower bound on \(P\) through (8) requires showing that the specific contraction \(\mathcal F_h\) is much smaller than \(E_{\rm AAD}B_h\). That is, the financing components of size \(\sqrt{k/U}\) in (A) must be nearly orthogonal to \(\eta_h=V\circ h\). (A) proves that norm bounds can never see this.

### Related objects in §2.3

- **(15)** is correct: the Maxwell stress of \(\Omega+h\) is divergence free, and the pure SD and ASD stresses vanish identically.
- Equivalently, \(H_h=-2\,h\circ J\), the standard identification \(\Lambda^-\cong S^{1,1}_0\). It is transverse-traceless because \(\Omega\) and \(h\) are harmonic.
- **(16)** is correct for a host with \(W^-=0\) and \(s=-4\): \(\nabla^*\nabla h=2W^-h-\tfrac s3h=\tfrac43h\).

---

## (iv) Regularized Berry ledger

### Identification (17)

On \(\{\Phi\ne0\}\), \(\det S^+=\mathbb Cv\otimes(\mathbb Cv)^\perp\), so
\[
\mathrm{Hom}(\mathbb Cv,(\mathbb Cv)^\perp)=L\otimes(\mathbb Cv)^{-2}.
\]
- **Connection.** The projected connection on \(\mathrm{Hom}\) equals the projection of the induced connection on \(\mathrm{End}_0S^+\cong\Lambda^+\otimes\mathbb C\). The \(A\)-part cancels there. On \(\Omega^\perp\cong K_J^{-1}\) this is the Levi-Civita \(b\)-connection, whose curvature is \(\gamma_J\) by (63.1).
- **Curvature sign.** Write \(\langle v,\nabla v\rangle=i\beta'\). Then \(F_{\mathbb Cv}=i\,d\beta'\). With \(F_{\mathcal A}=-if_{\mathcal A}\) and \([f_{\mathcal A}]=2\pi a\), the real curvature is \(f_{\mathcal A}-2d\beta\), where \(\beta=-\beta'=i\langle v,\nabla v\rangle\).
- **Convention dependence.** This uses an inner product linear in the second slot. An antilinear second slot flips the sign of \(\beta\). Separately, the complex orientation of \(\Omega^\perp\) (\(K^{-1}\) versus \(K\)) must be the one for which \(c_1=a\).

### Smoothness and the finite-\(\delta\) identity (18)–(19)

- **\(\beta_\delta\) is smooth.** Since \(\langle\Phi,\nabla\Phi\rangle=\tfrac12d\rho+i\,\mathrm{Im}\), we have \(\rho\beta=-\mathrm{Im}\langle\Phi,\nabla\Phi\rangle\). This is smooth, so \(\beta_\delta\) is a global smooth 1-form and \([\gamma_\delta]=2\pi a\).
- **(18).** This follows from \(d(w\beta)=dw\wedge\beta+w\,d\beta\).
- **Integrability.** Near a transverse zero the integrands of (19) are bounded: \(w|\gamma_J|\sim (r^2/\delta)\,r^{-2}\) and \(|dw||\beta|\sim\delta/(r^2+\delta)^2\). Equation (19) therefore holds as an identity of \(L^1\) integrands.

### Orders of the remainder terms

- **Reservoir term.** \(\int(1-w_\delta)|f^-||h|=O(\delta)\).
- **Transition term.** Substituting \(r^2=\delta x\),
  \[
  \int_{B_R}\frac{\delta\,r^3\,dr}{(r^2+\delta)^2}=\frac\delta2\int_0^{R^2/\delta}\frac{x\,dx}{(1+x)^2}=O\bigl(\delta\log(1/\delta)\bigr).
  \]
  Away from the zeros, \(dw=O(\delta)\). The stated order is correct.

### The limit (20)

- **Dominated convergence.** \(|t^-|\lesssim r^{-2}\in L^1_{\rm loc}(\mathbb R^4)\), which gives (20).
- **Excision check.** On \(M\setminus B_\epsilon\), the sphere integral \(\int_{S_\epsilon}\beta\wedge h=O(\epsilon^{-1}\cdot\epsilon^3)=O(\epsilon^2)\).
- **Content.** (20) is precisely (1), paired with \(h\), for the punctured \(J\). It holds even though \(\|t^-\|_2=\infty\). It does not feed Theorem 63.T, which needs Cauchy–Schwarz in \(L^2\).
- **Price at finite \(\delta\).** Per transverse zero, \(\|w_\delta t^-\|_2^2\approx16\pi^2\log(R/\sqrt\delta)\), while the remainders vanish like \(\delta\log(1/\delta)\). Choosing \(\delta\) relative to the geometry is exactly where the information lies.

### Degenerate zero sets

If \(\rho\) is small but nonzero on a tube around a surface, or vanishes along one, the excision term becomes \(O(1)\) and \(t^-\notin L^1\). The reservoir and transition terms at fixed \(\delta\) then carry order-one flux. The transverse-zero analysis does not cover this regime.

### Transgression (21)–(23)

- **(21).** \(\gamma_J\wedge\gamma_J-f\wedge f=4\,d\beta\wedge d\beta-4\,f\wedge d\beta=4\,d(\beta\wedge d\beta-\beta\wedge f)\). Correct.
- **Integrability of \(\gamma_J\wedge\gamma_J\).** Since \(t=\alpha\wedge\beta\) is decomposable, \(t\wedge t=0\). Hence \(\gamma_J\wedge\gamma_J=R(\Omega)^{\wedge2}+2R(\Omega)\wedge t\) is \(L^1\), even though \(|t^+|^2=|t^-|^2\sim r^{-4}\). This is the precise sense in which the signed quantity is finite.
- **(22).** On the unit \(S^3\), \(\beta=\pm\) the standard contact form, and \(\int\beta\wedge d\beta=2|S^3|=4\pi^2\). The sign of \(\beta\) cancels in \(\beta\wedge d\beta\); the orientation (degree) of \(\Phi/|\Phi|\) sets the sign of \(q_z\). Correct.
- **(23).** \(c_2(S^+)=(a^2-2\chi-3\tau)/4=0\) for the best-sign classes, so \(\sum_zq_z=0\). Correct.

Because \(c_2(S^+)=0\), a nowhere-zero section exists topologically; this is the Wu existence of \(J\). The obstruction is therefore not topological. It is that the SW-selected spinor need not be that section.

---

## Construction statements (§§4–5): identities versus implications

- **The AK family (24).**
  - Exactness is verified: \(|\Omega_\epsilon|^2_{g_\epsilon}=(2+\epsilon^2f)/(1+\epsilon^2f/2)=2\), and SD-ness and closure are conformally invariant.
  - (25) follows from \(\mathrm{Ric}^\circ=-2(\nabla^2w)_0+O(\epsilon^4)\).
  - (26) follows from Bochner with \(\mathrm{Ric}=-g\), and \(\nabla^*\nabla v=2W^+v+\tfrac43v=2v\), since \(W^+=\tfrac13\) on \(\Omega^\perp\).
  - It needs \(p_g(X)\ge1\).
  - It lives on the minimal \(X\) itself. "No exceptional flux" is therefore automatic, and (27) is (1) with \(c_1^-=0\).
  - What it does establish: \(P\sim\epsilon^4\) against \(\int|\nabla\Omega|^2\sim\epsilon^2\) for freely varying AK pairs.
- **The Taub-bolt metric (28)–(32).**
  - The biaxial Ricci formulas pass the round-\(S^3\) test: \(b=a\) gives intrinsic Ricci \(1/(2a^2)\).
  - The bolt condition \(V'(r_b)=1/(2n)\) and the root formula are the standard ones.
  - The asymptotic principal curvatures are \(1/\ell=1/\sqrt3\) for the bolt, against \(1/\sqrt6\) and \(2/\sqrt6\) for complex-hyperbolic spheres at Ricci \(-1\). The mismatch is genuine.
  - (33) is a definition. No connector estimate is proved.
- **(4).** This is exact on \(\{u>0\}\).
  - Approximating \(t^-\approx2\pi h_a^-\) forces the opposite structure \(\bar\Omega\approx\sqrt2\,h_a^-/|h_a^-|\) wherever \(u\) is not small.
  - The Nijenhuis zeros (signed count \(5\chi+6\tau=c_2(X)+2A-k\)) and the zero set of \(h_a^-\) both enter. This is an unresolved compatibility condition for any construction.

---

## Corrected statements suitable for exposition

**Proposition (harmonic test).** Let \((M,g,J,\Omega)\) be closed almost-Kähler with \(s\) constant, and let \(h\) be a harmonic ASD form. Then
\[
s\langle\mathsf H^-(t^-),h\rangle_{L^2}=\mathcal F_h-6\int u\langle t^-,h\rangle,
\]
with \(\mathcal F_h\) as in (7). Without constant \(s\), add \(\int(s-\bar s)\langle t^-,h\rangle\) to the left side. The pointwise form holds for every ASD \(h\).

**Proposition (second jet).** On a closed almost-Kähler four-manifold,
\[
\|\nabla^2\Omega\|_2+\|\nabla\Omega\|_4^2\le C\|\mathrm{Rm}\|_2\le C'\bigl(\chi(M)+P\bigr)^{1/2},
\]
with \(C\) universal. The estimate does not apply to normalized spinor directions with zeros.

**Proposition (flux inequality and its reach).** At \(s=-4\), inequality (13) holds. If \(P=o(k)\) and \(U<2/3\), then (63.3) gives (A), and \(B_h\ge\sqrt{2/3}\). Consequently (13) is automatically satisfied as \(U\to0\). Any lower bound on \(P\) via (8) requires an estimate of \(\mathcal F_h\) that exploits cancellation against \(\eta_h\), rather than norms of \(W_3^+\) and \(\rho_*''\).

**Proposition (relative ledger).** For every smooth \(\Phi\) and every \(\delta>0\), identity (19) holds exactly with smooth \(\gamma_\delta\). If the zeros of \(\Phi\) are isolated and nondegenerate, the remainders are \(O(\delta\log1/\delta)\), and (20) holds with \(t^-\in L^1\setminus L^2\). Moreover:
- \(\gamma_J\wedge\gamma_J\in L^1\);
- \(\int_{M\setminus Z}\gamma_J\wedge\gamma_J=4\pi^2a^2\) up to the oriented sum of Hopf indices \(q_z\);
- \(\sum_zq_z=c_2(S^+)=0\) for best-sign classes.

**Not established by this material:**
- any lower bound on \(P\) or tariff;
- any closed \(P=o(k)\) construction;
- any smooth Levi-Civita realization of (4) carrying the class \(a_\varepsilon\);
- any connector estimate for (33);
- any control of the finite-\(\delta\) reservoir and transition terms for actual SW solutions, including spinors that are small but nonzero near surfaces.