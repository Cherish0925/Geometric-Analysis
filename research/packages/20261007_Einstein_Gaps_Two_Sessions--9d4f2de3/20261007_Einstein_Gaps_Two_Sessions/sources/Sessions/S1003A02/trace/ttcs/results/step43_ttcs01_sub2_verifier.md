# TTCS Independent Branch Record

```json
{
  "step_id": 43,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md",
    "Sessions/S1003A02/workspace/scripts/step43_w0_divergence_symbol.py",
    "Sessions/S1003A02/workspace/data/step43_w0_divergence_symbol.json",
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md",
    "Knowledge/objects/papers/Integrability-conditions-for-almost-Hermitian-and-almost-Kähler-4-manif--88d7522b9e1c--cb27e699ed3d/object.md",
    "Knowledge/objects/papers/Local-rigidity-of-certain-classes-of-almost-Kahler-4-manifolds--c0d51aa8ffb7--68f3db154d35/object.md",
    "Knowledge/objects/papers/Conformal-Kähler-rigidity-of-Einstein-four-manifolds--ee41ec8c511e--4518ab125268/object.md"
  ]
}
```

## Task

Verify the mathematics and scope of the new Step-43 note. Focus on: (i) W0 eigenvalues/norm and equal-amplitude/optimized-amplitude mismatch formulas; (ii) the symbolic claim |delta W0|^2=(a^2/2)|nabla n|^2+(1/3)|nabla a|^2 under the almost-Kähler first-jet condition, including tensor-normalization and whether delta W0 has additional terms; (iii) what can rigorously be concluded from Cotton integration by parts and which assumptions are missing from the schematic R <= (sqrt(P)+||E||+||grad a||)||Rm|| law; (iv) whether the optimization with Theorem N has the stated constants or only scale; (v) the Kirchberg/Sekigawa formula and exact negative-scalar resisting term. Return a corrected theorem/proposition formulation that can safely enter the theorem package, distinguishing proved exact identities, conditional estimates, and heuristics.

## Output

# Step 43 verification: $W_0$ algebra, the divergence symbol, the Cotton law, and the Kirchberg identity

## Summary

- **(i) $W_0$ algebra.** The eigenvalues, norms and both mismatch formulas are exact.
- **(ii) Divergence symbol.** The formula $|\delta W_0|^2=\tfrac{a^2}{2}|\nabla n|^2+\tfrac13|\nabla a|^2$ is exact on the almost-Kähler $\mathcal W_2$ jet. It has a short closed-form proof, given below. The orthogonality of the two summands comes from representation theory and does not survive on the Lee jet.
- **(iii) Cotton law.** The schematic inequality $R\lesssim(\sqrt P+\|E\|+\|\nabla a\|)\|\mathrm{Rm}\|$ is not a consequence of the identities as written. Three things are wrong with it:
  - the $\nabla a$ term has the wrong form;
  - $\|\mathrm{Rm}\|_2$ stands in for a second-jet norm of $n$ that no available estimate controls;
  - the $E$ term is of the same order as the left side in the very common-mode regime the law is meant to describe.
- **(iv) Optimization.** The algebra is correct, but only the scale $k^2/A$ carries content, because $C$ is undetermined.
- **(v) Kirchberg's identity.** The quotations are correct. The note's reading of $Q(J)$ is not. On a closed almost-Kähler manifold, $Q(J)$ becomes purely algebraic in $\mathrm{Ric}_0$ after two integrations by parts. This changes the conclusion: in the almost-Kähler category the resisting term is the non-Kähler-type part $G=W_2^+\oplus W_3^+$ of $W^+$, and the law is linear, not quadratic.

---

## (i) $W_0$ eigenvalues and mismatch formulas

Write $K_n=\tfrac13 I-n\otimes n$. Then:

- **Spectrum.** $K_n$ has spectrum $(-\tfrac23,\tfrac13,\tfrac13)$ and $|K_n|^2=\tfrac23$.
- **Eigenvalues of $W_0$.** With $a=\rho^2/4$, the eigenvalues are $-\rho^2/6$ and $\rho^2/12$ (twice).
- **Norm.** $|W_0|^2=\rho^4/36+2\rho^4/144=\rho^4/24$, in the eigenvalue norm (LeBrun convention: Kähler eigenvalues $s/6,-s/12,-s/12$).
- **Equal amplitudes.** $|K_n-K_m|^2=|mm-nn|^2=2(1-c^2)$, so the mismatch is $2a^2(1-c^2)=\tfrac{\rho^4}{8}\sin^2\theta$. ✓
- **Optimized amplitude.** $\langle K_n,K_m\rangle=c^2-\tfrac13$, so
  $$\min_{b\in\mathbb R}|aK_n-bK_m|^2=a^2\Big[\tfrac23-\tfrac32\big(c^2-\tfrac13\big)^2\Big]=\tfrac{a^2}2(1-c^2)(1+3c^2).$$
  The constraint $b\ge0$ is active exactly when $c^2<\tfrac13$, giving $2a^2/3=\rho^4/24$. ✓
- **Kinetic split.** With Step-40 notation, $K=\int|\zeta|^2/\rho+\tfrac14\int\rho|\nabla n|^2$. ✓

**The "net $|\zeta|^2$ coefficient $8-4/\rho$" ignores the Lee part of the rotation.** The term $\tfrac14\rho|\nabla n|^2$ contains $\rho|v_4|^2=\tfrac12|a+J'b|^2$, which is itself $\zeta$-type and can be as large as $|\zeta|^2/\rho$. The worst-case net coefficient is therefore $8-8/\rho$. This is positive only for $\rho>1$ and equals 4 at $\rho=2$.

The qualitative conclusion (shallow-band saving must ride on $v_2$) survives, but the correct bookkeeping is Theorem N's quadratic form $\rho(|a|^2+5|b|^2-2\langle a,J'b\rangle)$, and the package should quote that rather than $8-4/\rho$.

**Notation collisions affecting readability.** Each of these appears inside Step 43:
- The symbol $a$ means three different things:
  - the amplitude $\rho^2/4$ (Step 43);
  - $d\sqrt\rho$ (Step 40);
  - AAD's torsion 1-form.
- The symbol $\rho$ means both the monopole density $|\Phi|^2$ and Catino–Dameno's eigenvalue ratio $\beta/\alpha$.
- The source has a rendering defect: "rac S2" appears twice in §6, where "\f" of "\frac" was eaten as a form-feed escape.

---

## (ii) The divergence symbol

### Closed-form derivation (independent of the script)

Use the convention $W_{ijkl}=\sum\lambda_r(n_r)_{ij}(n_r)_{kl}$ with $|n_r|_{\rm form}=1$; this matches the script's `Kcomp`. Put $X_j=\sum_i n_{ij}e_i$, so that $|X_j|^2=\tfrac12$. Then

$$\delta(aK_n)=-\iota_{da}K_n-a\,\tau,\qquad \tau:=\delta T=\delta n\otimes n-\sum_j e^j\otimes\nabla_{X_j}n,\qquad T=\nabla n\otimes n+n\otimes\nabla n .$$

Three facts follow:

1. **Cross term in $\tau$ vanishes.** $\langle\delta n\otimes n,\nabla_{X_\cdot}n\rangle=0$, because $\nabla n\perp n$.
2. **Norm of $\tau$.** $\sum_j|\nabla_{X_j}n|^2=\tfrac12|\nabla n|^2$, and $|\delta n|=|dn|$ for self-dual $n$. Hence, for every unit self-dual $n$,
   $$|\tau|^2=|dn|^2+\tfrac12|\nabla n|^2 .$$
3. **Norm of the amplitude term.** $|\iota_X K_n|^2=\tfrac12|X|^2|K_n|^2=\tfrac13|X|^2$.

### Orthogonality of the two summands

- **Cross term with $\delta n$.** $\langle\iota_{da}K,\delta n\otimes n\rangle=-\tfrac23\,n(da^\sharp,\delta n^\sharp)$.
- **Cross term with $\nabla_{X_\cdot}n$.** This only sees $U(2)$ components of $\nabla n$ isomorphic to $\Lambda^1$, i.e. the Lee class $\mathcal W_4$. The class $\mathcal W_2\cong[\![\Lambda^{0,1}\otimes\Lambda^{0,2}]\!]$ carries a different $U(1)$ weight, so the Schur pairing with $\Lambda^1$ vanishes.

### Result

$$\boxed{|\delta W_0|^2=\tfrac13|da|^2+a^2\big(|dn|^2+\tfrac12|\nabla n|^2\big)+2a\,\langle\iota_{da}K_n,\tau_{\mathcal W_4}\rangle}$$

On the $\mathcal W_2$ jet ($dn=0$, $\tau_{\mathcal W_4}=0$) this reduces to the script's output: $Q_n=2I$, $Q_c=I$, $Q_{da}=\tfrac13 I$, cross $=0$, and characteristic polynomial $(2\lambda-1)^4$.

**Checks on the script.** Its self-dual basis is correctly oriented ($*e^{02}=e^{31}$). The closure system is the cyclic sum, i.e. the correct $(dn)_{ijk}$ at a geodesic frame. The norm $|\delta W|^2=\sum_{j,\,k<l}$ is the form norm, consistent with $|\nabla n|^2=x^Tx$.

### Is anything missing from $\delta W_0$?

$\delta W_0$ itself has no missing terms: the $I/3$ piece enters through $da\cdot K$.

For the monopole structure, however, $n$ is not almost-Kähler, and the Lee jet adds $a^2|dn|^2$ and the $da\times\mathcal W_4$ cross term. Both are bounded by $C(\rho)|\zeta|^2$ on $\{\rho\ge\rho_0\}$, since $d n=d\psi/\rho-d\rho\wedge\psi/\rho^2$ and $|d\psi|^2=2\rho|b|^2$. They are therefore charged by Theorem N.

### Normalization warnings

- Kirchberg's operator convention gives $W_K=2W_L$ and $|W^+|_K^2=4|W^+|_L^2$.
- His norm $|\nabla J|_K^2=\tfrac1n\sum_k|\nabla_kJ|^2_{HS}$ equals $\delta_L/2$, where $\delta_L=|\nabla\omega|^2$ and $|\omega|^2=2$.
- AAD write $|\nabla\Omega|^2=4|a|^2$ and $\kappa-s=6|a|^2$.

### A structural point about the comparison tensor

$W_0$ fixes the amplitude $\rho^2/4$. The almost-Kähler Weitzenböck formula, however, forces the Kähler-type component to have amplitude $-\kappa/4$, where $\kappa=s+\tfrac32|\nabla\Omega|^2$ (AAD (10); equivalently Step 42's $W^+(u,u)=s/6+\delta/4$). Consequently $E=W^+-W_0$ always contains a piece of size $\asymp|\nabla n|^2$ that is forced, not free.

The clean decomposition is $W^+=W_1^+(\kappa,n)+G$ with $G=W_2^+\oplus W_3^+$. The symbol formula applies to $W_1^+$ with $a=-\kappa/4$. AAD's $\beta=-\tfrac\kappa8a+\lambda\phi(b)-\tfrac12J\phi(d\lambda)$ is exactly this computation in $\mathcal{AK}_3$: the first term is the $\tfrac12$-symbol, the remaining terms are $\delta W_3^+$.

---

## (iii) What the Cotton integration by parts actually gives

### Exact identity

On $U=\{\rho\ge\rho_0\}$ with $\chi\in C^\infty_c(U)$ and $s\equiv-4$, use $\delta W^+=C^+=\tfrac12P_+(d^\nabla\mathrm{Ric}_0)$ and $a\tau=-\delta W^++\delta E-\iota_{da}K$:

$$\int\chi^2a^2|\tau|^2=-\tfrac12\!\int\!\big\langle\mathrm{Ric}_0,(d^\nabla)^*P_+(\chi^2a\tau)\big\rangle+\int\!\langle E,\delta^*(\chi^2a\tau)\rangle-\int\chi^2a\langle\iota_{da}K,\tau_{\mathcal W_4}\rangle .$$

Hence, with $Y:=\|\nabla(\chi^2a\tau)\|_{L^2}$,
$$\tfrac12\int\chi^2a^2|\nabla n|^2_{\mathcal W_2}\le\big(c\sqrt P+\|E\|_{L^2(\operatorname{supp}\chi)}\big)\,Y+C(\rho_0)\|\zeta\|^2_{L^2(U)}.$$

### What separates this from the note's schematic law

1. **Second jet.** $Y$ involves $\nabla^2n$, $\nabla a$ and $\nabla\chi$. Replacing $Y$ by $\|\mathrm{Rm}\|_2$ needs an $L^2$ second-jet estimate. For a harmonic almost-Kähler form, Bochner gives
   $$\|\nabla^2\omega\|_2^2\lesssim\|W^+\|_2^2+\|s\|_2^2+\int|\mathrm{Rm}|\,|\nabla\omega|^2,$$
   and the last term requires $\|\nabla\omega\|_{L^4}$. For the monopole $n=\psi/\rho$, the relevant elliptic system is Seiberg–Witten, degenerate at $\{\rho=0\}$.
2. **The $\nabla a$ term.** It enters as $\|da\|\cdot\|a\tau_{\mathcal W_4}\|$, not $\|\nabla a\|\,\|\mathrm{Rm}\|$, and it vanishes pointwise on the $\mathcal W_2$ jet.
3. **The $E$ term.** In the Step-40 common mode, $E=\mathrm{diag}(x,-x/2,-x/2)$ with $x\approx h/3$, so $\|E\|_2\sim h\sqrt A$. Since $Y\sim\sqrt A$ and the left side is $\sim hA$, $\|E\|Y$ is of the same order as the left side. "$E$ negligible" therefore excludes the regime the law is meant to describe. The forced $W_1$ part of $E$ must be removed exactly (decomposition at the end of (ii)) before any Cauchy–Schwarz step.
4. **Cutoffs.** The cutoff terms near $\{\rho<\rho_0\}$ and the zero set are uncontrolled, and the bound on the lower amplitude $\rho_0$ is not supplied by the identities.

### The $\mathcal{AK}_3$ instance is linear, not quadratic

AAD Lemma 3 (21), integrated over a closed manifold with $s\equiv-4$, gives the exact balance
$$\int|a|^2=\int\Big(\tfrac32|a|^4+2\lambda^2-\mathrm{Ric}_0(a,a)\Big).$$

With $\lambda=0$, i.e. in $\mathcal{AK}_2$, this yields $\int|a|^2(1-\tfrac32|a|^2)\le\|\mathrm{Ric}_0\|_2\|a\|_4^2$. For uniform small torsion this forces $P\gtrsim V$, an order-one cost.

Consistently, AAD Corollary 1 gives $\mathrm{Ric}_0=\tfrac\kappa4(-g^{\mathcal D}+g^{\mathcal D^\perp})$ on $\mathcal{AK}_2$: the proper 3-symmetric "countermodel" has order-one Ricci (eigenvalues $0,0,s/2,s/2$). It shows that pointwise algebraic co-rotation does not force integrability. It does not show that low-$P$ torsion is possible; the escape variable is $\lambda$, i.e. $W_3^+$.

---

## (iv) Optimization with Theorem N

- **Comparison.** Since $\rho\le2$, $\mathcal N\le2R$ with $R=\mathbb E\int|\nabla n|^2_{\mathcal W_2}$. ✓
- **Algebra.** Solving $R^2+2CAR-8\pi^2kCA=0$ gives
  $$P_{\min}=\frac{16\pi^4k^2}{CA}+O\!\Big(\frac{k^3}{C^2A^2}\Big).$$
  This is correct given the quadratic law.
- **What carries content.** $C$ is undetermined (cutoffs, $\rho_0$, the second-jet constant), so only the scale $k^2/A$ means anything.
- **Unsupported comparisons.** The "1/12 at $k=A/3$" has no derivation. Comparing an unknown-constant lower bound with the certified cell coefficient $0.99566$ (an upper bound for a local cell) carries no information.
- **Curvature bound, exact form.** $\|\mathrm{Rm}\|_2^2=8\pi^2\big(\chi(X)+k\big)+c\,P$, with $c$ the normalization factor of $|\mathrm{Ric}_0|^2$. Here $A/3\le\chi(X)\le5A+36$ by Bogomolov–Miyaoka–Yau and Noether. So "$\lesssim A+k+P$" is fine, but the constant depends on $c_2(X)/A$.
- **Positivity of $\alpha(M)$.** The statement "$\alpha(M)>0$ for each fixed $(X,k)$" inherits every hypothesis from (iii) and holds only conditionally.

---

## (v) Kirchberg/Sekigawa: the exact resisting term

**Quotations.** Both quotations match Kirchberg's Propositions 4.2 and 4.3, and $Q(J)=2\int\langle\varphi,\psi\rangle$ matches Lemma 4.3. Combining Proposition 4.3 with Lemmas 2.3–2.4 ($|W^+|^2=6\lambda_K^2+|G|^2$, $|G|^2=|\tilde R^-|^2+8|\mathrm{Ric}_\star^-|^2$, $|\tilde R^+|^2=|\nabla J|^4/2$) gives the exact identity in Kirchberg's norms:
$$\int(-S)|\nabla J|^2=2Q(J)+\int\big(3|\nabla J|^4+|\tilde R^-|^2+|G|^2\big).\tag{K}$$

**$Q(J)$ is algebraic after integration by parts.** Start from $q=(\nabla^2_{kl}\mathrm{Ric})(Je_k,Je_l)$.

1. Integrate by parts twice.
2. Use $\sum_k(\nabla_kJ)e_k=0$, which is $\delta\Omega=0$.
3. Commute $\nabla_l\nabla_k J$ with the Ricci identity.

This gives
$$Q(J)=\int\mathrm{Ric}_{ab}\,(\nabla_lJ)_{ak}(\nabla_kJ)_{bl}+\int\mathrm{Ric}_{ab}J_{ak}\big([R_{lk},J]\big)_{bl}.$$

The pieces then reduce as follows:

- **Scalar part.** It contributes $\tfrac s4\big(\tfrac12|T|^2-(s^*-s)\big)=0$ pointwise, using $s^*-s=\tfrac12|T|^2$. This is also why $Q=0$ for Einstein metrics.
- **$W^\pm$ contractions.** They vanish: a scalar linear in $\mathrm{Ric}_0\in\Lambda^+\otimes\Lambda^-$ and built otherwise from $W^+$, $J$ is not $SU(2)_-$-invariant, and $\Lambda^-\otimes S^2_0\Lambda^-$ contains no trivial summand.
- **$\mathrm{Ric}_0^{\rm inv}$ quadratic term.** It drops out, because that part maps $\Lambda^-$ into $\mathbb R\Omega$, which commutes with $J$. This is consistent with AAD (21), which has no $|\mathrm{Ric}_0|^2$ term.

Hence
$$Q(J)=\int\mathrm{Ric}_0\ast\nabla J\ast\nabla J+c_2\int|\mathrm{Ric}_0^{\rm anti}|^2,\qquad |Q(J)|\le c_1\sqrt P\,\|\nabla J\|_{L^4}^2+c_2P .$$

The constants $c_1,c_2$ remain to be computed. A jet-level symbolic check, in the style of the Step-43 script, should confirm them.

**Consequence for $S\le-s_0<0$.** From (K),
$$s_0\int|\nabla J|^2\le2\int|G|^2+3\int|\nabla J|^4+2c_1\sqrt P\|\nabla J\|_4^2+2c_2P .$$
With $G$ negligible and diffuse torsion $t$, this forces $P\gtrsim\min(s_0tV,\,s_0^2V)$: a linear Goldberg law. The resisting term is therefore not an uncontrolled Cotton pairing. It is the Weyl energy of $G=W_2^+\oplus W_3^+$, which by (K) must satisfy $\int|G|_L^2\gtrsim\tfrac14\int\delta_L$.

**Combination with Step-42 AKΓ.** This is a derived reading; its constants should be rechecked. Assume $s\equiv-4$ and (H$_L$). The exact AKΓ defect contains $\tfrac1{2\pi^2}\int|G|_L^2$, and Blair's $\ell=8V-\int\delta$ gives $2A\theta\le\tfrac1{8\pi^2}\int\delta-\tfrac{(\int\delta)^2}{64\pi^2V}$. Adding (K) produces gain $\ge\tfrac1{8\pi^2}\int\delta-\tfrac{3}{64\pi^2}\int\delta^2-\tfrac{Q}{8\pi^2}$.

The linear torsion terms then cancel exactly. What survives is
$$\frac P{8\pi^2}\ \ge\ k-\frac{1}{128\pi^2}\frac{(\int\delta)^2}{V}-\frac{|Q|}{8\pi^2}+(\text{Jensen defects}),$$
in the uniform case with $A=V/2\pi^2$. So in the almost-Kähler category, torsion is first-order neutral, and the decision sits at second order and in $Q(J)$.

To realize saving, $|G|$ must reach size $\sim|\nabla J|$, not $|\nabla J|^2$. By AAD (13) and (15), this requires the torsion to vary on unit length scales (through $da$, $b$). This is consistent with Theorem N Corollary 3.

**What is absent.** There is no monopole analogue of (K), i.e. one for non-closed $n$ with $\zeta$ terms. That identity is what is needed to transfer this mechanism to the all-metric category of Theorem N.

---

## Formulation for the theorem package

**Proposition 43.1 (exact).** The $W_0$ spectrum and norm, the equal-amplitude mismatch, the optimized-amplitude mismatch, and the kinetic split as in (i). The shallow-band remark should be stated with Theorem N's $\zeta$ form, not $8-4/\rho$.

**Proposition 43.2 (exact, pointwise).** For a unit self-dual $n$ and a function $a$,
$$\delta(aK_n)=-\iota_{da}K_n-a\tau,\qquad |\tau|^2=|dn|^2+\tfrac12|\nabla n|^2 .$$
On the $\mathcal W_2$ jet, $|\delta(aK_n)|^2=\tfrac13|da|^2+\tfrac12a^2|\nabla n|^2$, with orthogonal summands (Schur). On the Lee jet there are additional terms bounded by $C(\rho)|\zeta|^2$.

**Proposition 43.3 (exact inequality).** The weighted Cotton pairing inequality of (iii), with $Y=\|\nabla(\chi^2a\tau)\|_2$ kept explicit.

**Conditional 43.4 (quadratic law).** $P\gtrsim R^2/A$, and hence $P\gtrsim k^2/(CA)$, under the following hypotheses:
- (H1) $\rho\ge\rho_0$ on the rotation region, with cutoff terms controlled;
- (H2) $Y^2\lesssim A$;
- (H3) $\|E-E_{\rm forced}\|_2\,Y=o(R)$, with the forced $W_1$ part removed exactly;
- (H4) $\zeta$ terms are $o(R)$.

The constant is not determined; this is a scale statement only.

**Proposition 43.5 (exact; the constants $c_1,c_2$ need a symbolic check).** On a closed almost-Kähler 4-manifold, identity (K) holds with $Q(J)$ algebraic in $\mathrm{Ric}_0$ as derived in (v). Two corollaries follow:
- a linear Goldberg inequality whose only escape is $\int|G|^2$;
- the $\mathcal{AK}_3$ balance $\int|a|^2=\int(\tfrac32|a|^4+2\lambda^2-\mathrm{Ric}_0(a,a))$ when $s\equiv-4$.

**Remarks (heuristic, to be labelled as such).**
- The $k/A$ per-class tariff.
- The "1/12" coefficient.
- The comparison with the certified cell.
- The first-order neutrality reading of AKΓ combined with (K), which needs its constants rechecked.

The statement in §6–7 of the note that "$Q(J)$ is controlled only by the quadratic Cauchy–Schwarz law" should be replaced by Proposition 43.5.