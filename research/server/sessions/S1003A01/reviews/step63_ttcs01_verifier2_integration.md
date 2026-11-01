# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 63,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step63_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step63_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check the proposed global consequence for a closed smooth surface contained in the torsion-zero set of a nonzero-scalar Einstein almost-Kähler four-manifold. Verify every bundle/orientation/curvature step: singular DT plus the Step-62 cone implying c=0 and rank-two complex-antilinear DT; J-invariance and orientation of TC; A nonzero and eta=0, W3+ nonzero; W3+ as K_J^{-2}; gamma_J=R(Omega)-a wedge Ja and R(Omega)=(s/4)Omega under Einstein, q=0, eta=0; the resulting Chern-degree contradiction. Also assess the extension to exceptional DT=0 points and the sign/factor deg(K_J^{-2}|C)=s Area/(4 pi). Provide a direct corrected proof if needed, grounded in the supplied AAD primary source.

## Integrated Scientific Memo

## Verification result

The proposed clean-surface obstruction is correct:

> **Proposition.** Let \((M^4,g,J,\Omega)\) be Einstein almost-Kähler, with scalar curvature \(s\neq0\). There is no nonempty compact smooth embedded surface without boundary
> \[
> C\subset Z:=\{\nabla\Omega=0\}
> \]
> on which \(D(\nabla\Omega)\) is everywhere nonzero.

No compactness of \(M\), integrability of \(J\) near \(C\), or completeness of the Step-62 cone as an existence criterion is required. Here “closed surface” must mean **compact without boundary**, not merely a closed subset.

The exceptional-point extension and the normalization
\[
\boxed{\deg(K_J^{-2}|_C)=\frac{s\,\operatorname{Area}_g(C)}{4\pi}}
\]
are also correct when \(TC\) is \(J\)-invariant—for example, when the rank-two locus is dense. Exceptional points do not, on the supplied evidence, yield a further contradiction.

## 1. First jet, kernel, and orientation

Put \(T=\nabla\Omega\). AAD §2.3, equations (21)–(23), gives a smooth local gauge \(\phi\), with \(|\phi|^2=2\), and
\[
T=a\otimes\phi-Ja\otimes J\phi,\qquad |T|^2=4|a|^2.
\]
Thus \(a(p)=0\) at every \(p\in Z\). At such a point,
\[
(DT)_p(X)
=(\nabla_Xa)_p\otimes\phi_p
-J(\nabla_Xa)_p\otimes J\phi_p.
\]
The map
\[
\beta\longmapsto\beta\otimes\phi_p-J\beta\otimes J\phi_p
\]
is injective. Consequently, \(DT_p\) and
\[
L_p:T_pM\longrightarrow T_pM,\qquad
L_p(X)=(\nabla_Xa)_p^\sharp
\]
have the same kernel and rank. Although \(DT_p\) takes values in a larger tensor bundle, its effective rank-four target is identified by this injection; the determinant in Step 62 is the determinant of this effective map \(L_p\), not a determinant of the full tensor-valued map.

Because \(T|_C=0\),
\[
T_pC\subseteq\ker DT_p=\ker L_p.
\]
Hence \(L_p\) is singular. In the Step-62 complex representation,
\[
L_p(z)=cz+B\bar z,\qquad B=S+A,\quad S^T=S,\quad A^T=-A,
\]
and the necessary cone identity and its determinant consequence are
\[
\|A\|^2=8|c|^2+\|S\|^2,
\qquad
\det_{\mathbb R}L_p=9|c|^4+|\det_{\mathbb C}B|^2.
\]
Singularity therefore implies
\[
c=0,\qquad \det_{\mathbb C}B=0.
\]
If \(DT_p\neq0\), then \(B\neq0\), so \(B\) has complex rank one. Thus \(L_p(z)=B\bar z\) is complex-antilinear and has real rank two. Since
\[
L_p(JX)=-JL_p(X),
\]
its kernel is a \(J\)-complex line. The inclusion of the two-dimensional space \(T_pC\) in that kernel is consequently an equality:
\[
\ker DT_p=T_pC.
\]
This proves cleanliness in the sense used in the notes and proves \(J\)-invariance of \(TC\).

Use the \(J\)-orientation on \(C\). For a unit tangent vector \(e\),
\[
\Omega(e,Je)=g(Je,Je)=1,
\]
so
\[
\Omega|_C=dA_g,\qquad \int_C\Omega=\operatorname{Area}_g(C)>0.
\]
No ambient holomorphicity is used.

**Slot-convention caution.** Transposition preserves singularity, rank, and complex-antilinearity, but generally does not preserve the kernel. Thus the tangent-kernel identification should be made with the actual derivative map \(X\mapsto(\nabla_Xa)^\sharp\), as above, rather than justified by saying transposition is irrelevant to every step.

## 2. Curvature consequences, with a direct AAD check

With \(c=0\), the cone reads \(\|A\|^2=\|S\|^2\). If \(A=0\), then \(S=0\), contradicting \(B\neq0\). Hence \(A\neq0\).

The exact Step-62 coframe dictionary states
\[
|\eta|^2=4|c|^2,\qquad
\operatorname{tr}V^2=4\|A\|^2,
\]
where \(V\) represents \(W_3^+\). Therefore
\[
\eta=0,\qquad W_3^+\neq0
\]
on \(C\). These statements are independent of the alternative norm convention for \(\eta\).

There is also a direct verification of \(\eta=0\) and the required curvature coefficient using AAD, avoiding the coefficient dictionary. At \(p\in Z\), contraction of the differentiated gauge formula gives
\[
\nabla^*\nabla\Omega
=-(\operatorname{tr}_{\mathbb R}L_p)\phi
+\operatorname{tr}_{\mathbb R}(JL_p)\,J\phi.
\]
For an antilinear \(L_p\), both traces vanish: conjugation by \(J\) sends each of \(L_p\) and \(JL_p\) to its negative. Thus
\[
\nabla^*\nabla\Omega=0\quad\text{on }C.
\]
AAD §2.3, equation (19), is
\[
\frac12\nabla^*\nabla\Omega=\rho_*-\rho,
\qquad \rho_*=R(\Omega).
\]
Einsteinity gives \(\rho=(s/4)\Omega\), hence
\[
\boxed{R(\Omega)=\frac{s}{4}\Omega\quad\text{on }C.}
\]
Its anti-invariant component vanishes, equivalently \(\eta=0\).

The same coefficient follows from the curvature blocks requested in the task. AAD equation (20) gives
\[
q=|\nabla\Omega|^2=s^*-s=\frac{2(\kappa-s)}3.
\]
Since \(q=0\), \(\kappa=s\), or \(r=\kappa/6=s/6\). With \(\eta=0\),
\[
W^+(\Omega)=\frac{s}{6}\Omega.
\]
The Einstein Singer–Thorpe decomposition in AAD §2.2 then gives
\[
R(\Omega)=\left(W^++\frac{s}{12}\mathrm{Id}\right)(\Omega)
=\frac{s}{4}\Omega.
\]
In particular, **\(q=0\) alone determines the Rayleigh value, not the eigenform condition**; the vanishing of \(\eta\) is essential to this block argument.

For nonvanishing of \(W_3^+\), Step-62 Theorem 62.A offers a dictionary-independent check:
\[
|DT|^2=4|W_3^+|_{\mathrm{HS}}^2-12|\eta|^2.
\]
Along \(C\), therefore,
\[
\boxed{|W_3^+|_{\mathrm{HS}}^2=\frac14|DT|^2.}
\]
Thus \(W_3^+\) is nowhere zero under the proposition’s hypothesis.

## 3. Bundle identification and canonical Chern form

AAD §2.1 identifies
\[
\mathcal L:=\bigl(\llbracket\Lambda_J^{0,2}\rrbracket,J\bigr)
\simeq K_J^{-1},
\qquad
(J\psi)(X,Y)=-\psi(JX,Y).
\]
AAD §2.2 explicitly identifies \(W_3^+\) with a section of \(K_J^{-2}\). The sign can also be checked directly: \(W_3^+\) is an antilinear endomorphism of the complex line \(\mathcal L\). In a unit frame \(e\), write \(E(e)=we\). Under \(e'=e^{i\theta}e\),
\[
w'=e^{-2i\theta}w.
\]
This is the coefficient transformation law for a section of \(\mathcal L^{\otimes2}\), not its conjugate. Thus
\[
W_3^+\in\Gamma(K_J^{-2}),\qquad
c_1(K_J^{-2})=2c_1(M,J).
\]
A nowhere-zero smooth section trivializes a complex line bundle; no holomorphicity is needed. Hence
\[
W_3^+|_C\neq0
\quad\Longrightarrow\quad
2\langle c_1(M,J),[C]\rangle=0.
\]

AAD §2.3, equations (24)–(25), gives
\[
db=a\wedge Ja-R(\Omega),\qquad
\gamma_J=-db=R(\Omega)-a\wedge Ja,
\]
and states
\[
[\gamma_J]=2\pi c_1(M,J).
\]
Here \(b\) is a **local** connection form: \(\gamma_J\) is global, but one must not apply Stokes as though \(b\) were globally defined on \(C\).

Since \(a=0\) on \(C\), the preceding curvature calculation yields
\[
\gamma_J|_C=\frac{s}{4}\Omega|_C.
\]
Consequently,
\[
2\pi\langle c_1(M,J),[C]\rangle
=\frac{s}{4}\operatorname{Area}_g(C)\neq0.
\]
This contradicts the trivialization of \(K_J^{-2}|_C\), proving the proposition. The argument applies componentwise.

## 4. What extends across \(DT=0\) points

Let \(C\subset Z\) be any compact smooth surface, and put
\[
E=\{p\in C:DT_p=0\}.
\]

At **every** point of \(C\), tangential vanishing still makes \(L_p\) singular. Thus the cone and determinant imply \(c=0\), whether or not the first jet is nonzero. It follows directly that
\[
\eta=0,\qquad R(\Omega)=\frac{s}{4}\Omega
\quad\text{everywhere on }C,
\]
and
\[
|W_3^+|_{\mathrm{HS}}^2=\frac14|DT|^2.
\]
In particular,
\[
\boxed{\{W_3^+|_C=0\}=E.}
\]
These curvature assertions require no density assumption.

However, \(DT_p=0\) does not itself constrain \(T_pC\) to be \(J\)-invariant. If \(C\setminus E\) is dense, \(J\)-invariance extends from that locus by continuity. Under this assumption—or an independent assumption that \(C\) is \(J\)-invariant—the \(J\)-orientation and area identity hold globally. Therefore
\[
\langle c_1(M,J),[C]\rangle
=\frac{s\,\operatorname{Area}_g(C)}{8\pi},
\]
and
\[
\boxed{\deg(K_J^{-2}|_C)
=2\langle c_1(M,J),[C]\rangle
=\frac{s\,\operatorname{Area}_g(C)}{4\pi}.}
\]
Both the **positive factor** and the **sign determined by \(s\)** are correct in the AAD conventions.

There is a useful topological sharpening. For an embedded \(J\)-invariant surface,
\[
(TM,J)|_C=(TC,J)\oplus(N_C,J),
\]
so
\[
\langle c_1(M,J),[C]\rangle=\chi(C)+C\cdot C.
\]
Hence
\[
\boxed{s\,\operatorname{Area}_g(C)=8\pi\bigl(\chi(C)+C\cdot C\bigr).}
\]
In particular, the degree of \(K_J^{-2}|_C\) is an even integer. For \(s<0\), necessarily \(\chi(C)+C\cdot C<0\).

If \(E\) consists of isolated points, it is finite and the smooth-section index formula gives
\[
\sum_{p\in E}\operatorname{wind}_p(W_3^+|_C)
=\frac{s\,\operatorname{Area}_g(C)}{4\pi}
=2\bigl(\chi(C)+C\cdot C\bigr).
\]
For \(s<0\), at least one local winding must be negative. For nonisolated \(E\), the section defines a localized Euler/first-Chern class supported on \(E\), whose image is \(c_1(K_J^{-2}|_C)\).

## 5. Precise unresolved exceptional-point mechanism

The supplied identities do **not** prove that \(W_3^+|_C\) is holomorphic or that its local windings are nonnegative. Thus its negative degree for \(s<0\) is a constraint, not yet a contradiction.

AAD’s Ricci identities specify the higher-jet object involved. Along \(C\), \(a=0\), \(\kappa=s\), and \(\eta=0\), so the scalar curvature contribution on \(\Omega^\perp\) cancels:
\[
W_3^+(\phi)=-d(Ja),\qquad
W_3^+(J\phi)=-da.
\]
These are ambient two-form identities evaluated at points of \(C\). At \(p\in E\), also \(\nabla a=0\). Consequently, the tangential derivative
\[
T_pC\longrightarrow (K_J^{-2})_p,\qquad
v\longmapsto\nabla_vW_3^+
\]
is determined by an alternating projection of \(\nabla^2a\), equivalently a component of \(\nabla^3\Omega\). If this derivative is invertible, the restricted section’s index is its oriented determinant sign. A complex-linear invertible derivative gives \(+1\); a complex-antilinear invertible derivative gives \(-1\). General real-linear derivatives must be assessed by their determinant, and higher-order isolated zeros by their full leading winding.

AAD Corollary 1 does not immediately determine that sign. Under Einsteinity, its anti-invariant Bianchi equation on \(C\) reduces to
\[
2(\delta W_3^+)_Z^{\prime\prime}
=-\bigl(\nabla_{JZ}\rho_*^{\prime\prime}\bigr)^{\prime\prime}.
\]
Although \(\rho_*^{\prime\prime}=0\) on \(C\), its normal derivatives need not vanish. Moreover, the divergence on the left includes normal derivatives of \(W_3^+\); it is not a tangential \(\bar\partial\)-equation for the restricted section.

The remaining scientific object is therefore the **allowed tangential winding of \(W_3^+\) at higher-order torsion zeros on a smooth zero surface**. A sign restriction requires additional higher-jet compatibility or control of the normal derivative terms. The clean-surface theorem itself is fully proved without that missing information.