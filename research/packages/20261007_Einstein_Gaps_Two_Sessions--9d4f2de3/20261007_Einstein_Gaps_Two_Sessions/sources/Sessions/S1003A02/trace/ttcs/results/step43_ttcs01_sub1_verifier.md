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

## Scientific verification memo: Step 43

### Overall assessment

The \(W_0\) algebra and the restricted first-jet computation are exact. The main mathematical gap lies between that pointwise almost-Kähler symbol calculation and the displayed global Cotton estimate. Integration by parts yields an exact weak identity involving formal adjoints applied to the torsion tensor, but an estimate of those second-jet expressions by \(\|\mathrm{Rm}\|_2\) has not been derived. Moreover, the monopole direction \(n_\epsilon\) is generally not almost-Kähler: Theorem N uses only its \(\mathcal W_2\) component, while the script imposes \(d(\sqrt2n)=0\) on the entire first jet. Thus the quadratic transport law is presently conditional, and the numerical common-mode coefficient near \(k=A/3\) remains heuristic.

---

## 1. Algebra of \(W_0\)

Put
\[
K_n=\frac13I-n\otimes n,\qquad a=\frac{\rho^2}{4},\qquad W_0=aK_n,
\]
where \(n\) is a unit vector in the three-dimensional Euclidean space \(\Lambda^+\).

### Eigenvalues and norm

Along \(n\),
\[
K_n n=-\frac23n,
\]
while \(K_n=\frac13I\) on \(n^\perp\). Hence
\[
\operatorname{spec}(W_0)
=\left\{-\frac{2a}{3},\frac a3,\frac a3\right\}
=\left\{-\frac{\rho^2}{6},\frac{\rho^2}{12},\frac{\rho^2}{12}\right\}.
\]
Therefore
\[
|W_0|^2=\frac{4a^2}{9}+2\frac{a^2}{9}
=\frac{2a^2}{3}
=\frac{\rho^4}{24}.
\]
These formulas are correct.

### Equal-amplitude mismatch

For unit \(n,m\), with \(c=\langle n,m\rangle\),
\[
K_n-K_m=m\otimes m-n\otimes n,
\]
and
\[
|n\otimes n-m\otimes m|^2=2(1-c^2).
\]
Thus
\[
|aK_n-aK_m|^2=2a^2(1-c^2)
=\frac{\rho^4}{8}\sin^2\theta.
\]
This is also correct.

### Optimized comparison amplitude

Since
\[
|K_m|^2=\frac23,\qquad
\langle K_n,K_m\rangle=c^2-\frac13,
\]
the unconstrained minimizing amplitude is
\[
b_*=\frac{a\langle K_n,K_m\rangle}{|K_m|^2}
=\frac a2(3c^2-1).
\]
After imposing \(b\ge0\),
\[
b_*=\max\left\{0,\frac a2(3c^2-1)\right\}.
\]
Consequently,
\[
\min_{b\ge0}|aK_n-bK_m|^2=
\begin{cases}
\displaystyle
\frac{a^2}{2}(1-c^2)(1+3c^2),&c^2\ge\frac13,\\[5pt]
\displaystyle
\frac{2a^2}{3},&c^2\le\frac13.
\end{cases}
\]
The two branches agree at \(c^2=1/3\). In particular,
\[
|0-W_0|^2=\frac{\rho^4}{24},
\]
which equals \(2/3\) at \(\rho=2\). All constants in §1 of the note are correct.

The phrase “rank-one Weyl tensor” is best replaced by “two-eigenvalue Kähler-type Weyl tensor”: \(W_0\) is not rank one as an endomorphism of \(\Lambda^+\).

---

## 2. Exact divergence identity and tensor normalization

Let
\[
W_0=a\left(\frac13I-n\otimes n\right).
\]
Because \(I_{\Lambda^+}\) is parallel, the complete covariant formula is
\[
(\delta W_0)_{jkl}
=-(\nabla^ia)\,(K_n)_{ij\,kl}
+a\Big[(\nabla^in)_{ij}n_{kl}
+n_{ij}(\nabla^in)_{kl}\Big].
\tag{2.1}
\]
There are no other first-derivative terms. In a normal tangent frame, connection derivatives of the chosen self-dual basis are already represented by \(\nabla n\).

Define
\[
\mathcal A(da)_{jkl}=-(\nabla^ia)(K_n)_{ij\,kl},
\]
and
\[
\mathcal T(\nabla n)_{jkl}
=(\nabla^in)_{ij}n_{kl}
+n_{ij}(\nabla^in)_{kl}.
\]
Then
\[
\delta W_0=\mathcal A(da)+a\,\mathcal T(\nabla n).
\tag{2.2}
\]

### Norm convention used by the script

The script uses
\[
|F|^2=\frac12F_{ij}F_{ij}
\]
for two-forms and
\[
|T|^2=\sum_{j,k<l}T_{jkl}^2
=\frac12\sum_{j,k,l}T_{jkl}^2
\]
for a one-form with values in \(\Lambda^2\). This is the natural bundle norm on \(T^*\otimes\Lambda^2\). With this convention, the basis \(n_1,n_2,n_3\) in the script is orthonormal and \(\omega=\sqrt2\,n\) has \(|\omega|^2=2\).

If a source instead uses the raw component sum \(\sum_{jkl}T_{jkl}^2\), both coefficients below are doubled.

### Restricted almost-Kähler symbol

Under
\[
|n|=1,\qquad d(\sqrt2\,n)=0,
\]
the JSON matrices give
\[
Q_n=2I_4,\qquad Q_c=I_4,\qquad
Q_{da}=\frac13I_4,\qquad Q_{\rm cross}=0.
\]
Hence
\[
|\mathcal T(\nabla n)|^2=\frac12|\nabla n|^2,
\qquad
|\mathcal A(da)|^2=\frac13|da|^2,
\qquad
\langle\mathcal A(da),\mathcal T(\nabla n)\rangle=0,
\]
and therefore
\[
\boxed{
|\delta W_0|^2
=\frac{a^2}{2}|\nabla n|^2+\frac13|da|^2.
}
\tag{2.3}
\]
Equivalently, with \(\omega=\sqrt2n\),
\[
|\delta W_0|^2
=\frac{a^2}{4}|\nabla\omega|^2+\frac13|da|^2.
\]

The polynomial
\[
(2\lambda-1)^4
\]
shows that the generalized eigenvalue of the squared norm forms is \(1/2\). The corresponding singular value, as a norm ratio, is \(1/\sqrt2\), not \(1/2\). The wording in Step 43 should be changed accordingly.

### Why this does not yet apply to the monopole \(n_\epsilon\)

For a general unit self-dual form, \(\nabla n\) has both \(\mathcal W_2\) and Lee/\(\mathcal W_4\) components. The script restricts to the four-dimensional kernel of the closure map, exactly the almost-Kähler \(\mathcal W_2\) subspace. Outside that subspace, (2.3) is replaced by the full quadratic form
\[
|\mathcal A(da)+a\mathcal T(\nabla n)|^2,
\]
which can contain amplitude–Lee mixed terms. The supplied JSON gives no full eight-dimensional torsion Gram matrix. Its rank data
\[
\operatorname{rank}M_{\rm all}=8
\]
for twelve inputs \((da,\nabla n)\) also show that a general norm identity cannot be inferred from the restricted matrices alone.

Thus:

* (2.1)–(2.2) hold for every smooth unit \(n\);
* (2.3) requires \(dn=0\);
* using (2.3) for the Seiberg–Witten directions requires either vanishing Lee component or a separate extension of the symbol calculation with quantified Lee terms.

---

## 3. What Cotton integration by parts actually gives

Assume for this subsection that \(M\) is closed, \(n\) is a global almost-Kähler direction,
\[
d(\sqrt2n)=0,
\]
and \(a\ge a_0>0\). Let
\[
E=W^+-W_0,\qquad
U=\mathcal T(\nabla n).
\]
For constant scalar curvature, write
\[
\delta W^+=\mathcal C(\nabla\operatorname{Ric}^\circ),
\]
where \(\mathcal C\) is the fixed Cotton projection in the chosen convention. From
\[
\delta W_0=\delta W^+-\delta E
\]
and the orthogonality in (2.3), pairing with \(U\) gives the exact identity
\[
\boxed{
\int_M a|U|^2
=
\int_M\langle \mathcal C(\nabla\operatorname{Ric}^\circ),U\rangle
-\int_M\langle\delta E,U\rangle.
}
\tag{3.1}
\]
Since \(|U|^2=\frac12|\nabla n|^2\),
\[
\frac12\int_M a|\nabla n|^2
=
\int_M\langle \operatorname{Ric}^\circ,\mathcal C^*U\rangle
-\int_M\langle E,\delta^*U\rangle,
\tag{3.2}
\]
with signs incorporated into the definitions of the formal adjoints.

Consequently,
\[
\frac{a_0}{2}\int_M|\nabla n|^2
\le
\sqrt P\,\|\mathcal C^*U\|_2
+\|E\|_2\,\|\delta^*U\|_2.
\tag{3.3}
\]
This is the rigorous Cotton output.

### The missing second-jet estimate

To reach
\[
R\lesssim
\bigl(\sqrt P+\|E\|_2\bigr)\|\mathrm{Rm}\|_2,
\]
one still needs an estimate such as
\[
\boxed{
\|\mathcal C^*U\|_2+\|\delta^*U\|_2
\le C_2\|\mathrm{Rm}\|_2.
}
\tag{3.4}
\]
No derivation of (3.4) is present in Step 43 or the supplied script.

At the tensor level,
\[
|\nabla U|
\lesssim |\nabla^2n|+|\nabla n|^2,
\]
so a direct estimate involves quantities such as
\[
\|\nabla^2n\|_2,\qquad \|\nabla n\|_4^2.
\]
Almost-Kähler harmonicity gives a formula for the contracted Hessian
\[
\nabla^*\nabla n=2W^+(n)-\frac{s}{3}n,
\]
but this alone does not produce (3.4). A dedicated Weitzenböck calculation for the particular adjoint contractions, or geometric regularity assumptions controlling the full second jet, is required.

The AAD identities cited in Step 43 apply in the class \(\mathcal{AK}_3\), which includes \(J\)-invariant Ricci curvature and \(W_2^+=0\). They do not provide a general second-jet estimate for arbitrary almost-Kähler structures.

### Role of \(\nabla a\)

Under the exact almost-Kähler symbol, the amplitude term is pointwise orthogonal to \(U\). Pairing with \(U\), rather than \(aU\), removes \(\nabla a\) from (3.1)–(3.3). Thus the displayed term
\[
+\|\nabla a\|_2
\]
in the Step-43 transport law is not obtained from this pairing.

Amplitude derivatives can reappear through:

1. a different choice of test tensor;
2. localization near zero sets or shallow-band interfaces;
3. the Lee component when \(dn\ne0\);
4. an independently assumed second-jet estimate involving \(a\).

An \(L^2\) bound on \(\nabla a\) alone does not control products such as
\[
\nabla a\,\nabla n
\]
in \(L^2\); one needs, for example, \(L^4\)-\(L^4\) or \(L^\infty\)-\(L^2\) control.

### Curvature scale

With curvature-operator norms,
\[
\boxed{
\|\mathrm{Rm}\|_2^2=8\pi^2\chi(M)+P.
}
\tag{3.5}
\]
Thus \(\|\mathrm{Rm}\|_2^2\lesssim A+k+P\) follows when \(\chi(M)\lesssim A+k\). For a ball quotient \(X\),
\[
\chi(X)=\frac A3,
\qquad
\chi(X\#k\overline{\mathbf{CP}}^2)=\frac A3+k.
\]
For a general minimal \(X\), the relation between \(\chi(X)\) and \(A=K_X^2\) must be stated separately.

---

## 4. Combination with Theorem N and exact optimization

Define the total \(\mathcal W_2\) energy
\[
R=\mathbb E_\epsilon\int_M
|\nabla n_\epsilon|_{\mathcal W_2}^2.
\]
Theorem N gives
\[
8\pi^2k-P
\le
\frac12\mathbb E_\epsilon\int
\rho_\epsilon^2
|\nabla n_\epsilon|_{\mathcal W_2}^2.
\]
Since \(0\le\rho_\epsilon\le2\),
\[
\boxed{
P\ge 8\pi^2k-2R.
}
\tag{4.1}
\]
This constant is exact when \(R\) denotes the total energy above. If \(R\) includes only a shallow-band region, the omitted contribution must be retained.

Now suppose an independently established transport theorem gives
\[
\boxed{
P\ge\frac{R^2}{\Lambda A}.
}
\tag{4.2}
\]
Put
\[
K=8\pi^2k,\qquad L=\Lambda A.
\]
Minimizing
\[
\max\left\{K-2R,\frac{R^2}{L}\right\}
\]
over \(R\ge0\) yields
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
P\ge
\frac{K^2}{4L}
-\frac{K^3}{8L^2}
+O\!\left(\frac{K^4}{L^3}\right)
=
\frac{16\pi^4k^2}{\Lambda A}
+O\!\left(\frac{k^3}{A^2}\right).
\tag{4.4}
\]
Thus the Step-43 leading coefficient is algebraically correct if its \(C\) denotes \(\Lambda\). If the preceding transport estimate is written
\[
R\le C_T\sqrt{AP},
\]
then \(\Lambda=C_T^2\).

With an error term
\[
R\le C_T\sqrt A\,(\sqrt P+\varepsilon),
\]
the corresponding statement is only
\[
P\ge
\left(
\frac{R}{C_T\sqrt A}-\varepsilon
\right)_+^2.
\tag{4.5}
\]
A lower estimate independent of \(R\) then requires quantitative control of \(\varepsilon\). In particular, uncontrolled \(\|E\|_2\), Lee energy, amplitude localization terms, or zero-set terms prevent the use of (4.2).

The numerical coefficient “around \(1/12\)” at \(k=A/3\) does not follow from the Cotton calculation because \(\Lambda\) has not been determined. It belongs to the formal common-mode model, not to a proved transport theorem.

---

## 5. Kirchberg–Sekigawa identity

In Kirchberg’s normalization, Proposition 4.2 states
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
The exact algebraically adverse term is therefore
\[
-2|\nabla J|^2
\]
in Kirchberg’s norm.

The equivalent Proposition 4.3 formula is
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

The derivative-Ricci term is
\[
Q(J)=2\int_M\langle\varphi,\psi\rangle\,d\mu,
\]
where
\[
\langle\varphi,\psi\rangle
=
\frac14
\left\langle
J\varphi(X^k,X^l),
(\nabla_{X_k}\operatorname{Ric})X_l
-(\nabla_{X_l}\operatorname{Ric})X_k
\right\rangle.
\tag{5.4}
\]
For constant scalar curvature, the alternating derivative in (5.4) is a fixed contraction of the Cotton tensor. Therefore \(Q(J)\) is indeed the same derivative-Ricci source encountered in the Cotton pairing.

Two distinct phenomena should be kept separate:

* The term \((S/2)|\nabla J|^2\) has the adverse sign at \(S=-4\), even when \(Q(J)=0\).
* With only \(P=\|\operatorname{Ric}^\circ\|_2^2\), the term \(Q(J)\) is not controlled because it contains \(\nabla\operatorname{Ric}^\circ\).

Harmonic Weyl curvature implies \(Q(J)=0\), but Kählerness then requires additional Weyl information, such as Kirchberg’s condition
\[
|W_+|^2=\frac{S^2}{6}.
\]

Kirchberg normalizes endomorphism norms by
\[
|A|_{\mathrm K}^2=\frac14\operatorname{tr}(A^*A)
\]
in dimension four. Hence
\[
|\nabla J|_{\mathrm K}^2
=\frac14|\nabla J|_{\mathrm{tensor}}^2.
\]
The coefficients in (5.1)–(5.3) should not be inserted into the Step-40 normalization without this conversion. The malformed `rac` strings in Step 43 should also be repaired to `\frac`.

---

# Formulations suitable for the theorem package

### Proposition A — algebraic \(W_0\) formulas

For unit \(n,m\in\Lambda^+\), \(a\ge0\), and \(c=\langle n,m\rangle\),
\[
W_0=a\left(\frac13I-n\otimes n\right)
\]
has eigenvalues \((-2a/3,a/3,a/3)\) and norm \(2a^2/3\). Moreover,
\[
|aK_n-aK_m|^2=2a^2(1-c^2),
\]
and
\[
\min_{b\ge0}|aK_n-bK_m|^2=
\begin{cases}
\frac{a^2}{2}(1-c^2)(1+3c^2),&c^2\ge1/3,\\
\frac{2a^2}{3},&c^2\le1/3.
\end{cases}
\]

### Proposition B — almost-Kähler divergence symbol

With the bundle norms used in the script, if \(|n|=1\) and \(d(\sqrt2n)=0\), then
\[
|\delta W_0|^2
=\frac{a^2}{2}|\nabla n|^2+\frac13|da|^2,
\]
and the two summands are orthogonal. The squared singular value of the torsion map is \(1/2\); its singular value is \(1/\sqrt2\).

This proposition does not apply unchanged when \(dn\ne0\).

### Proposition C — exact Cotton pairing

On a closed constant-scalar almost-Kähler four-manifold, with \(a\ge a_0>0\), let \(E=W^+-W_0\) and \(U=\mathcal T(\nabla n)\). Then
\[
\frac12\int a|\nabla n|^2
=
\int\langle\operatorname{Ric}^\circ,\mathcal C^*U\rangle
-\int\langle E,\delta^*U\rangle.
\]
Hence
\[
\frac{a_0}{2}\int|\nabla n|^2
\le
\sqrt P\,\|\mathcal C^*U\|_2
+\|E\|_2\,\|\delta^*U\|_2.
\]

### Conditional transport corollary

If, in addition,
\[
\|\mathcal C^*U\|_2+\|\delta^*U\|_2
\le C_2\|\mathrm{Rm}\|_2,
\]
then
\[
\int|\nabla n|^2
\le
\frac{2C_2}{a_0}
\bigl(\sqrt P+\|E\|_2\bigr)\|\mathrm{Rm}\|_2.
\]
The second-jet estimate displayed above is an explicit assumption; it is not established by the current note.

### Conditional optimization lemma

If \(R\) is the total sign-averaged \(\mathcal W_2\) energy and
\[
P\ge8\pi^2k-2R,\qquad
P\ge\frac{R^2}{\Lambda A},
\]
then
\[
P\ge
\left(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\right)^2,
\]
with leading behavior
\[
P\ge\frac{16\pi^4k^2}{\Lambda A}
+O(k^3/A^2).
\]

### Proposition D — Kirchberg identity at \(S=-4\)

In Kirchberg’s norm convention,
\[
Q(J)+\int
\left(
|\widetilde R|^2
+4|\operatorname{Ric}_\star^-|^2
-2|\nabla J|^2
+|\nabla J|^4
\right)=0,
\]
and \(Q(J)\) is the explicit torsion–Cotton contraction in (5.4).

---

The exact mathematical content of Step 43 is therefore the \(W_0\) algebra, the almost-Kähler divergence symbol, the identification of Cotton as the differential source, and the algebraic optimization lemma. The global quadratic transport estimate, its application to monopole \(\mathcal W_2\) energy, cover-uniform perturbative coercivity, and the numerical common-mode coefficient require additional derivations or assumptions.