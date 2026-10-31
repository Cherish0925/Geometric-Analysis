# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 43,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step43_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step43_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematics and scope of the new Step-43 note. Focus on: (i) W0 eigenvalues/norm and equal-amplitude/optimized-amplitude mismatch formulas; (ii) the symbolic claim |delta W0|^2=(a^2/2)|nabla n|^2+(1/3)|nabla a|^2 under the almost-Kähler first-jet condition, including tensor-normalization and whether delta W0 has additional terms; (iii) what can rigorously be concluded from Cotton integration by parts and which assumptions are missing from the schematic R <= (sqrt(P)+||E||+||grad a||)||Rm|| law; (iv) whether the optimization with Theorem N has the stated constants or only scale; (v) the Kirchberg/Sekigawa formula and exact negative-scalar resisting term. Return a corrected theorem/proposition formulation that can safely enter the theorem package, distinguishing proved exact identities, conditional estimates, and heuristics.

## Integrated Scientific Memo

# Verification of Step 43

## Verdict

The following parts are exact and safe:

1. the spectrum and norm of \(W_0\);
2. both mismatch formulas;
3. the restricted almost-Kähler first-jet identity for \(\delta W_0\), with the stated tensor norm;
4. Kirchberg’s two quoted integral identities.

The proposed global Cotton transport inequality and the resulting \(k^2/A\) lower bound are **not proved**. They require an additional second-jet estimate, localization control, and a justified passage from an almost-Kähler jet to the actual monopole direction. The optimization is exact only after assuming a definite quadratic coercive inequality.

A further correction is essential: the characteristic polynomial \((2\lambda-1)^4\) gives a **squared singular value** \(1/2\), hence singular value \(1/\sqrt2\), not \(1/2\).

The stronger claim that Kirchberg’s \(Q(J)\) can already be replaced by a specific algebraic expression in \(\operatorname{Ric}^\circ\) is not established by the supplied sources. It should not enter the package without a complete derivation and normalization check.

---

## 1. Exact \(W_0\) algebra

Let
\[
K_n=\frac13I_{\Lambda^+}-n\otimes n,\qquad |n|=1,\qquad
W_0=aK_n,\qquad a=\frac{\rho^2}{4}.
\]

Since \(K_n n=-\frac23n\) and \(K_n=\frac13 I\) on \(n^\perp\),
\[
\operatorname{spec}(W_0)
=\left(-\frac{2a}{3},\frac a3,\frac a3\right)
=\left(-\frac{\rho^2}{6},\frac{\rho^2}{12},\frac{\rho^2}{12}\right),
\]
and
\[
|W_0|^2=\frac{2a^2}{3}=\frac{\rho^4}{24}.
\]

Thus \(W_0\) should be called a **two-eigenvalue Kähler-type Weyl tensor**, not a rank-one endomorphism of \(\Lambda^+\).

For unit \(n,m\), put \(c=\langle n,m\rangle\). Since
\[
K_n-K_m=m\otimes m-n\otimes n,
\]
one has
\[
|aK_n-aK_m|^2
=2a^2(1-c^2)
=\frac{\rho^4}{8}\sin^2\theta.
\]

Also,
\[
|K_m|^2=\frac23,\qquad
\langle K_n,K_m\rangle=c^2-\frac13.
\]
The unconstrained optimal amplitude is
\[
b_*=\frac{a\langle K_n,K_m\rangle}{|K_m|^2}
=\frac a2(3c^2-1).
\]
After imposing \(b\ge0\),
\[
\min_{b\ge0}|aK_n-bK_m|^2=
\begin{cases}
\displaystyle
\frac{a^2}{2}(1-c^2)(1+3c^2),&c^2\ge\frac13,\\[5pt]
\displaystyle
\frac{2a^2}{3},&c^2\le\frac13.
\end{cases}
\]
The branches agree at \(c^2=1/3\). In particular,
\[
|W_0|^2=\frac{\rho^4}{24},
\]
so the cost of comparison with \(W^+=0\) is \(2/3\) at \(\rho=2\), but tends to zero with \(\rho\).

### Bookkeeping correction

The informal coefficient \(8-4/\rho\) accounts only for the explicit term
\[
K=\int\frac{|\zeta|^2}{\rho}+\frac14\int\rho|\nabla n|^2
\]
before resolving the Lee part of \(\nabla n\). Because the Lee component is itself determined by amplitude/phase data, that sentence should not be used as a definitive net \(\zeta\)-coefficient. The exact safe statement is Theorem N’s nonnegative quadratic form
\[
\rho\bigl(|d\sqrt\rho|^2+5|b|^2-2\langle d\sqrt\rho,J'b\rangle\bigr).
\]

---

## 2. Exact divergence formula and its scope

For any smooth unit section \(n\in\Lambda^+\),
\[
W_0=aK_n,\qquad K_n=\frac13I-n\otimes n.
\]
Since \(I_{\Lambda^+}\) is parallel,
\[
(\delta W_0)_{jkl}
=-(\nabla^ia)(K_n)_{ij\,kl}
+a\Big[(\nabla^in)_{ij}n_{kl}
+n_{ij}(\nabla^in)_{kl}\Big].
\tag{2.1}
\]
Thus, defining
\[
\mathcal A(da)_{jkl}=-(\nabla^ia)(K_n)_{ij\,kl},
\]
and
\[
\mathcal T(\nabla n)_{jkl}
=(\nabla^in)_{ij}n_{kl}
+n_{ij}(\nabla^in)_{kl},
\]
one has the complete first-order identity
\[
\boxed{\delta W_0=\mathcal A(da)+a\,\mathcal T(\nabla n).}
\tag{2.2}
\]
There are no omitted connection terms: in a normal tangent frame, all variation of the self-dual direction is contained in \(\nabla n\).

### Norm convention

The script uses
\[
|F|^2=\frac12\sum_{ij}F_{ij}^2
\]
for two-forms and
\[
|T|^2=\sum_{j,k<l}T_{jkl}^2
=\frac12\sum_{jkl}T_{jkl}^2
\]
for \(T^*\otimes\Lambda^2\). This is the standard induced bundle norm. If raw sums over all \(k,l\) are used instead, every coefficient in the divergence norm is doubled.

### Almost-Kähler first-jet identity

Assume
\[
|n|=1,\qquad d(\sqrt2\,n)=0.
\]
Because \(\sqrt2\) is constant, this is simply \(dn=0\); equivalently, \(\omega=\sqrt2n\) is an almost-Kähler fundamental form at the first-jet level.

The script gives
\[
Q_n=2I_4,\qquad Q_c=I_4,\qquad
Q_{da}=\frac13I_4,\qquad Q_{\rm cross}=0.
\]
Therefore
\[
|\mathcal T(\nabla n)|^2=\frac12|\nabla n|^2,\qquad
|\mathcal A(da)|^2=\frac13|da|^2,
\]
and the two images are orthogonal. Hence
\[
\boxed{
|\delta W_0|^2
=\frac{a^2}{2}|\nabla n|^2+\frac13|da|^2.
}
\tag{2.3}
\]
Equivalently, for \(\omega=\sqrt2n\),
\[
|\delta W_0|^2
=\frac{a^2}{4}|\nabla\omega|^2+\frac13|da|^2.
\]

The generalized characteristic polynomial
\[
(2\lambda-1)^4
\]
says that the ratio of the squared norm forms is \(1/2\). Thus:

\[
\boxed{\text{squared singular value}=1/2,\qquad
\text{singular value}=1/\sqrt2.}
\]

### General unit self-dual directions

For a general unit \(n\), one can write the torsion part more explicitly and obtain
\[
|\mathcal T(\nabla n)|^2
=|dn|^2+\frac12|\nabla n|^2.
\tag{2.4}
\]
However, the amplitude part need not be orthogonal to the full torsion part. Thus the general formula has the form
\[
|\delta W_0|^2
=\frac13|da|^2
+a^2\left(|dn|^2+\frac12|\nabla n|^2\right)
+2a\,\langle\mathcal A(da),\mathcal T_{\mathrm{Lee}}(\nabla n)\rangle.
\tag{2.5}
\]
The cross term vanishes on the almost-Kähler \(\mathcal W_2\) jet but not in general.

This distinction is crucial: the Seiberg–Witten-selected \(n_\epsilon\) in Theorem N generally has both \(\mathcal W_2\) and Lee components. Therefore (2.3) cannot be applied directly to the whole monopole first jet without either:

* proving that the Lee component vanishes;
* retaining the additional terms in (2.5); or
* estimating them through the exact \(\zeta\)/amplitude terms in Theorem N.

---

## 3. What Cotton integration by parts rigorously yields

Assume for the clean global formulation that:

* \(M\) is closed;
* \(s\) is constant;
* \(\omega=\sqrt2n\) is almost-Kähler;
* \(a\ge a_0>0\);
* \(E=W^+-W_0\).

Set
\[
U=\mathcal T(\nabla n).
\]
Then
\[
\delta W_0=\mathcal A(da)+aU,\qquad
\langle\mathcal A(da),U\rangle=0,
\qquad |U|^2=\frac12|\nabla n|^2.
\]
Because
\[
\delta W_0=\delta W^+-\delta E
\]
and constant scalar curvature identifies \(\delta W^+\) with a fixed self-dual Cotton projection \(\mathcal C(\nabla\operatorname{Ric}^\circ)\), pairing with \(U\) gives
\[
\int_M a|U|^2
=
\int_M\langle\mathcal C(\nabla\operatorname{Ric}^\circ),U\rangle
-\int_M\langle\delta E,U\rangle.
\tag{3.1}
\]
After integration by parts,
\[
\boxed{
\frac12\int_M a|\nabla n|^2
=
\int_M\langle\operatorname{Ric}^\circ,\mathcal C^*U\rangle
-\int_M\langle E,\delta^*U\rangle.
}
\tag{3.2}
\]
Consequently,
\[
\boxed{
\frac{a_0}{2}\int_M|\nabla n|^2
\le
\sqrt P\,\|\mathcal C^*U\|_2
+\|E\|_2\,\|\delta^*U\|_2.
}
\tag{3.3}
\]

This is the rigorous Cotton consequence.

### Missing estimate

To deduce the Step-43 schematic law one would need a theorem of the form
\[
\|\mathcal C^*U\|_2+\|\delta^*U\|_2
\le C_2\|\operatorname{Rm}\|_2,
\tag{3.4}
\]
or a localized weighted analogue.

No such estimate is proved in the note or script. Indeed,
\[
\nabla U=\nabla\bigl(\mathcal T(\nabla n)\bigr)
\]
contains
\[
\nabla^2n\quad\text{and}\quad(\nabla n)^2.
\]
Thus one naturally encounters
\[
\|\nabla^2n\|_2,\qquad \|\nabla n\|_4^2.
\]
The harmonic-form Weitzenböck equation controls a contracted Hessian, but does not by itself establish (3.4). A dedicated Weitzenböck estimate for the particular adjoint contractions, or extra bounded-geometry/Sobolev hypotheses, is needed.

The AAD differential identities do not fill this gap in general: they are proved under the additional \(\mathcal{AK}_3\) hypotheses, including \(J\)-invariant Ricci and \(W_2^+=0\).

### Localization and monopole assumptions also missing

For the intended monopole application one must additionally control:

1. cutoffs near \(\{\rho=0\}\) or outside a shallow band;
2. the Lee component of \(\nabla n\);
3. derivatives of the cutoff;
4. products involving \(da\) and the Lee torsion;
5. the discrepancy between total \(\mathcal W_2\) energy and energy restricted to the shallow band;
6. the error \(E=W^+-W_0\).

An \(L^2\) bound on \(da\) alone is insufficient for products such as
\[
|da|\,|\nabla n|;
\]
one needs suitable \(L^\infty\)-\(L^2\), \(L^4\)-\(L^4\), or localized weighted control.

### The displayed \(\|\nabla a\|_2\) term

In the exact almost-Kähler pairing (3.1), the amplitude term is pointwise orthogonal to \(U\), so no \(\|\nabla a\|_2\) term appears. Such a term can arise only from localization, the Lee component, a different test tensor, or an independently postulated second-jet estimate. Therefore
\[
R\lesssim
\bigl(\sqrt P+\|E\|_2+\|\nabla a\|_2\bigr)\|\operatorname{Rm}\|_2
\]
must not be stated as an established consequence of Cotton integration by parts.

### Curvature scale

With the standard four-dimensional curvature norm,
\[
\boxed{
\|\operatorname{Rm}\|_2^2=8\pi^2\chi(M)+P.
}
\tag{3.5}
\]
Thus
\[
\|\operatorname{Rm}\|_2^2\lesssim A+k+P
\]
requires a stated topological estimate \(\chi(M)\lesssim A+k\). For a ball quotient,
\[
\chi(X)=A/3,\qquad
\chi(X\#k\overline{\mathbf{CP}}^2)=A/3+k.
\]
It is not an assumption-free identity for arbitrary \(X\).

---

## 4. Conditional quadratic law and exact optimization

Let
\[
R=\mathbb E_\epsilon\int_M
|\nabla n_\epsilon|_{\mathcal W_2}^2.
\]
Theorem N gives exactly
\[
8\pi^2k-P
\le
\frac12\mathbb E_\epsilon\int_M
\rho_\epsilon^2
|\nabla n_\epsilon|_{\mathcal W_2}^2.
\]
Since \(0\le\rho_\epsilon\le2\),
\[
\boxed{P\ge8\pi^2k-2R.}
\tag{4.1}
\]
This coefficient is exact only when \(R\) denotes the total sign-averaged \(\mathcal W_2\) energy. If \(R\) is restricted to a shallow band, the contribution from the complement must remain.

Suppose, as a separate proved hypothesis, that
\[
\boxed{P\ge\frac{R^2}{\Lambda A}}
\tag{4.2}
\]
for some specified \(\Lambda>0\). Writing
\[
K=8\pi^2k,\qquad L=\Lambda A,
\]
optimization gives
\[
P\ge\min_{R\ge0}
\max\left\{K-2R,\frac{R^2}{L}\right\}.
\]
The crossing point yields
\[
\boxed{
P\ge
K+2L-2\sqrt{L(L+K)}
=
\left(\sqrt{L+K}-\sqrt L\right)^2.
}
\tag{4.3}
\]
For \(K/L\ll1\),
\[
\boxed{
P\ge
\frac{K^2}{4L}-\frac{K^3}{8L^2}
+O\!\left(\frac{K^4}{L^3}\right)
=
\frac{16\pi^4k^2}{\Lambda A}
+O\!\left(\frac{k^3}{A^2}\right).
}
\tag{4.4}
\]

Thus the leading constant in Step 43 is algebraically correct if its \(C\) means \(\Lambda\). If the transport estimate is instead written
\[
R\le C_T\sqrt{AP},
\]
then
\[
\Lambda=C_T^2.
\]

If errors are present, for example
\[
R\le C_T\sqrt A\,(\sqrt P+\varepsilon),
\]
the valid consequence is only
\[
P\ge
\left(
\frac{R}{C_T\sqrt A}-\varepsilon
\right)_+^2.
\tag{4.5}
\]
No positive gap follows unless \(\varepsilon\) is controlled noncircularly relative to \(R/\sqrt A\).

Therefore:

* the **scale** \(k^2/A\) is conditionally correct;
* the exact lower coefficient is unavailable because the transport constant is unavailable;
* the “approximately \(1/12\)” claim at \(k=A/3\) is heuristic and should be removed from the theorem package;
* comparison with the certified \(0.995662733\) cell coefficient is not a comparison of proved constants.

A further structural warning is that in the formal common mode the error \(E=W^+-W_0\) is generally of the same order as the torsion contribution. Treating \(E\) as negligible excludes precisely the regime the quadratic law is intended to model unless a forced Kähler-type component is first separated and handled exactly.

---

## 5. Kirchberg–Sekigawa formula

Kirchberg’s Proposition 4.2 states, in his norm convention,
\[
\boxed{
Q(J)+\int_M
\left(
|\widetilde R|^2
+4|\operatorname{Ric}_\star^-|^2
+\frac S2|\nabla J|^2
+|\nabla J|^4
\right)d\mu=0.
}
\tag{5.1}
\]
At \(S=-4\),
\[
\boxed{
Q(J)+\int_M
\left(
|\widetilde R|^2
+4|\operatorname{Ric}_\star^-|^2
-2|\nabla J|^2
+|\nabla J|^4
\right)d\mu=0.
}
\tag{5.2}
\]
Therefore the exact negative-scalar adverse term is
\[
\boxed{-2|\nabla J|^2}
\]
in Kirchberg’s normalization.

The equivalent Proposition 4.3 identity is
\[
\boxed{
Q(J)+\frac12\int_M
\left(
|\widetilde R|^2
+|\nabla J|^4
+|W_+|^2-\frac{S^2}{6}
\right)d\mu=0.
}
\tag{5.3}
\]

Kirchberg also gives
\[
Q(J)=2\int_M\langle\varphi,\psi\rangle\,d\mu,
\]
where
\[
\boxed{
\langle\varphi,\psi\rangle
=
\frac14\left\langle
J\varphi(X^k,X^l),
(\nabla_{X_k}\operatorname{Ric})X_l
-(\nabla_{X_l}\operatorname{Ric})X_k
\right\rangle.
}
\tag{5.4}
\]
For constant scalar curvature, the alternating derivative of Ricci in (5.4) is a fixed Cotton contraction. Thus it is correct to identify \(Q(J)\) with the same derivative-Ricci source appearing in the Cotton argument.

Two obstructions must nevertheless be distinguished:

1. even if \(Q(J)=0\), the term \((S/2)|\nabla J|^2\) has the adverse sign when \(S<0\);
2. control of \(P=\|\operatorname{Ric}^\circ\|_2^2\) alone does not directly control the displayed derivative-Ricci representation of \(Q(J)\).

Harmonic Weyl curvature implies \(Q(J)=0\), but does not alone imply Kählerness. Kirchberg’s corresponding integrability result also uses the Weyl condition
\[
|W_+|^2=\frac{S^2}{6}.
\]

The proposed further reduction
\[
Q(J)=\int \operatorname{Ric}^\circ *\nabla J*\nabla J
+c\int|\operatorname{Ric}^{\circ,\mathrm{anti}}|^2
\]
and the resulting asserted linear Goldberg estimate are not present in the supplied source and were not derived with checked constants. They remain a possible calculation, not a verified theorem.

Finally, Kirchberg’s norm convention differs from the standard Hilbert–Schmidt tensor norm:
\[
|A|_{\mathrm K}^2=\frac14\operatorname{tr}(A^*A)
\]
in dimension four. The coefficients in (5.1)–(5.3) must therefore not be transferred into Step-40 conventions without conversion.

---

# Corrected theorem-package formulation

## Proposition 43.A — algebra of the model tensor

Let \(n,m\) be unit vectors in \(\Lambda^+\), \(a\ge0\), and
\[
K_n=\frac13I-n\otimes n.
\]
Then
\[
\operatorname{spec}(aK_n)=\left(-\frac{2a}{3},\frac a3,\frac a3\right),
\qquad |aK_n|^2=\frac{2a^2}{3}.
\]
If \(c=\langle n,m\rangle\), then
\[
|aK_n-aK_m|^2=2a^2(1-c^2),
\]
and
\[
\min_{b\ge0}|aK_n-bK_m|^2=
\begin{cases}
\frac{a^2}{2}(1-c^2)(1+3c^2),&c^2\ge1/3,\\[3pt]
\frac{2a^2}{3},&c^2\le1/3.
\end{cases}
\]
For \(a=\rho^2/4\), this gives
\[
\operatorname{spec}(W_0)
=\left(-\frac{\rho^2}{6},\frac{\rho^2}{12},\frac{\rho^2}{12}\right),
\qquad |W_0|^2=\frac{\rho^4}{24}.
\]

## Proposition 43.B — divergence symbol

Let \(n\) be a smooth unit section of \(\Lambda^+\), \(a\) a smooth function, and
\[
W_0=a\left(\frac13I-n\otimes n\right).
\]
Then
\[
\delta W_0=\mathcal A(da)+a\mathcal T(\nabla n)
\]
with \(\mathcal A,\mathcal T\) given by (2.1)–(2.2).

Under the norm
\[
|T|^2=\sum_{j,k<l}T_{jkl}^2,
\]
if \(d(\sqrt2n)=0\), then
\[
\boxed{
|\delta W_0|^2
=\frac13|da|^2+\frac{a^2}{2}|\nabla n|^2,
}
\]
and the amplitude and torsion images are orthogonal. The squared singular value of the torsion map is \(1/2\), and its singular value is \(1/\sqrt2\).

For a general unit \(n\), additional \(dn\) and amplitude–Lee cross terms occur; the restricted formula must not be applied to the full monopole jet without controlling these terms.

## Proposition 43.C — exact Cotton pairing

Let \((M,g,\omega)\) be a closed constant-scalar almost-Kähler four-manifold, write \(\omega=\sqrt2n\), assume \(a\ge a_0>0\), and set
\[
W_0=aK_n,\qquad E=W^+-W_0,\qquad U=\mathcal T(\nabla n).
\]
Then
\[
\frac12\int_M a|\nabla n|^2
=
\int_M\langle\operatorname{Ric}^\circ,\mathcal C^*U\rangle
-\int_M\langle E,\delta^*U\rangle,
\]
and hence
\[
\frac{a_0}{2}\int_M|\nabla n|^2
\le
\sqrt P\,\|\mathcal C^*U\|_2
+\|E\|_2\,\|\delta^*U\|_2.
\]

No estimate replacing the two adjoint norms by \(C\|\operatorname{Rm}\|_2\) is asserted here.

## Conditional Corollary 43.D — transport estimate

Under the hypotheses of Proposition 43.C, suppose additionally that
\[
\|\mathcal C^*U\|_2+\|\delta^*U\|_2
\le C_2\|\operatorname{Rm}\|_2.
\]
Then
\[
\int_M|\nabla n|^2
\le
\frac{2C_2}{a_0}
\bigl(\sqrt P+\|E\|_2\bigr)\|\operatorname{Rm}\|_2.
\]
A localized monopole version requires, as explicit additional hypotheses, control of zero-set and band cutoffs, Lee torsion, amplitude-gradient products, and the discrepancy between full and shallow-band \(\mathcal W_2\) energy.

## Conditional Lemma 43.E — optimization with Theorem N

If
\[
P\ge8\pi^2k-2R
\]
and, independently,
\[
P\ge\frac{R^2}{\Lambda A},
\]
then
\[
\boxed{
P\ge
\left(
\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}
\right)^2.
}
\]
For \(k/A\ll1\),
\[
P\ge
\frac{16\pi^4k^2}{\Lambda A}
+O\!\left(\frac{k^3}{A^2}\right).
\]
This is a conditional scale law, not a presently proved Einstein-gap theorem.

## Proposition 43.F — Kirchberg identity at \(S=-4\)

On a compact almost-Kähler four-manifold, in Kirchberg’s norm convention,
\[
Q(J)+\int_M
\left(
|\widetilde R|^2
+4|\operatorname{Ric}_\star^-|^2
-2|\nabla J|^2
+|\nabla J|^4
\right)d\mu=0,
\]
equivalently,
\[
Q(J)+\frac12\int_M
\left(
|\widetilde R|^2
+|\nabla J|^4
+|W_+|^2-\frac83
\right)d\mu=0.
\]
Moreover \(Q(J)\) is the explicit torsion–derivative-of-Ricci pairing (5.4). No bound of \(Q(J)\) by \(P\) alone is included without an additional proved integration-by-parts identity.

---

## Scope labels for the existing Step-43 claims

### Proved exact identities

- \(W_0\) spectrum and norm.
- Equal-amplitude mismatch.
- Optimized-amplitude mismatch.
- Restricted almost-Kähler divergence symbol.
- Cotton as the differential source.
- Theorem-N inequality \(P\ge8\pi^2k-2R\) for total \(R\).
- Exact optimization formula, conditional on \(P\ge R^2/(\Lambda A)\).
- Kirchberg’s identities and the adverse term \(-2|\nabla J|^2\).

### Conditional estimates

- Any global or localized quadratic Cotton transport inequality.
- \(P\gtrsim R^2/A\).
- A positive fixed-\((X,k)\) gap derived from that law.
- Perturbative KE torsion coercivity, especially cover-uniform coercivity.

### Heuristics only

- the numerical coefficient “around \(1/12\)”;
- comparison of that coefficient with the certified cell coefficient;
- the claim that diffuse common-mode geometry is actually realizable;
- any assertion that \(E\) or \(\nabla a\) is negligible without an independent estimate;
- any algebraic reduction of \(Q(J)\) beyond Kirchberg’s supplied formulas until its constants and norm conventions are fully derived.