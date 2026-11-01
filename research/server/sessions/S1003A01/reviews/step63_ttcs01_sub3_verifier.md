# TTCS Independent Branch Record

```json
{
  "step_id": 63,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/spirit_step62_clean_zero_surface_consequence.md",
    "Sessions/S1003A01/workspace/notes/step63_SU2_nut_and_clean_zero_surface.md",
    "Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Check the proposed global consequence for a closed smooth surface contained in the torsion-zero set of a nonzero-scalar Einstein almost-Kähler four-manifold. Verify every bundle/orientation/curvature step: singular DT plus the Step-62 cone implying c=0 and rank-two complex-antilinear DT; J-invariance and orientation of TC; A nonzero and eta=0, W3+ nonzero; W3+ as K_J^{-2}; gamma_J=R(Omega)-a wedge Ja and R(Omega)=(s/4)Omega under Einstein, q=0, eta=0; the resulting Chern-degree contradiction. Also assess the extension to exceptional DT=0 points and the sign/factor deg(K_J^{-2}|C)=s Area/(4 pi). Provide a direct corrected proof if needed, grounded in the supplied AAD primary source.

## Output

## Scientific verification memo

### Conclusion

The proposed proposition is correct, assuming “closed surface” means a compact embedded surface \(C\) with \(\partial C=\varnothing\). No compactness of the ambient manifold is used.

The bundle identifications, orientation, curvature coefficient, and Chern-degree factor are all consistent with the supplied AAD source and Step 62. In particular,
\[
\deg\!\left(K_J^{-2}|_C\right)=\frac{s\,\operatorname{Area}_g(C)}{4\pi}
\]
has the stated sign and normalization.

---

## 1. From \(T|_C=0\) to the rank-two complex-antilinear first jet

Write \(T=\nabla\Omega\). In an AAD gauge,
\[
T=a\otimes\phi-Ja\otimes J\phi,
\qquad |T|^2=4|a|^2.
\]
At a torsion zero \(p\), \(a(p)=0\). Differentiating at \(p\) gives
\[
(DT)_p(X)
=(\nabla_Xa)\otimes\phi-J(\nabla_Xa)\otimes J\phi.
\]
All terms involving derivatives of \(J,\phi\), or \(J\phi\) are multiplied by \(a(p)\) and therefore vanish. The map
\[
\beta\longmapsto \beta\otimes\phi-J\beta\otimes J\phi
\]
is injective, so \(DT_p\) and \(\nabla a(p)\), represented by the Step-62 map \(Df\), have the same kernel and real rank.

Since \(T\) vanishes identically on \(C\),
\[
T_pC\subseteq\ker(DT_p).
\]
Thus \(DT_p\) is singular. Step 62 writes
\[
f(z)=cz+B\bar z,\qquad B=S+A,\qquad S^T=S,\quad A^T=-A,
\]
with
\[
\|A\|^2=8|c|^2+\|S\|^2
\]
and
\[
\det_{\mathbb R}Df=9|c|^4+|\det_{\mathbb C}B|^2.
\]
Singularity therefore forces
\[
c=0,\qquad \det_{\mathbb C}B=0.
\]

If \(DT_p\neq0\), then \(B\neq0\). Hence \(B\) has complex rank one, and
\[
Df(z)=B\bar z
\]
has real rank two. Its kernel is a complex line because
\[
Df(iz)=B\overline{iz}=-iB\bar z.
\]
Consequently,
\[
\dim_{\mathbb R}\ker DT_p=2.
\]
Since \(T_pC\) is already a two-dimensional subspace of this kernel,
\[
T_pC=\ker DT_p.
\]
Thus \(T_pC\) is \(J\)-invariant at every point of \(C\).

This also proves the stated cleanliness in the definition used in the notes:
\[
\ker DT_p=T_pC,\qquad \operatorname{rank}_{\mathbb R}DT_p=2.
\]

---

## 2. Orientation of \(C\)

The \(J\)-invariance of \(TC\) supplies a canonical orientation. If \(e\) is a unit tangent vector, then \((e,Je)\) is positively oriented and
\[
\Omega(e,Je)=g(Je,Je)=1.
\]
Therefore, with this orientation,
\[
\Omega|_C=dA_g,
\qquad
\int_C\Omega=\operatorname{Area}_g(C)>0.
\]

No integrability of \(J\) in a neighborhood of \(C\) is involved. The induced almost complex structure on the real surface \(C\) is automatically a complex structure, but that fact is not needed for the area identity.

---

## 3. The curvature components \(\eta\) and \(W_3^+\)

With \(c=0\), the cone becomes
\[
\|A\|^2=\|S\|^2.
\]
If \(A=0\), then \(S=0\), hence \(B=0\), contradicting \(DT_p\neq0\). Thus
\[
A\neq0.
\]

The exact Step-62 coframe dictionary gives
\[
|\eta|^2=4|c|^2,
\qquad
\operatorname{tr}V^2=4\|A\|^2,
\]
where \(V\) is the trace-free \(u^\perp\)-block representing \(W_3^+\). It follows that
\[
\eta=0,\qquad W_3^+\neq0
\]
at every point of \(C\).

These conclusions do not depend on the differing \(\eta\)-norm conventions mentioned in Steps 59 and 62, since only vanishing and nonvanishing are used.

---

## 4. The bundle carried by \(W_3^+\)

AAD’s \(U(2)\)-decomposition states that
\[
W_3^+\in\Gamma(K_J^{-2}).
\]
More explicitly, the real rank-two bundle
\[
\llbracket\Lambda_J^{0,2}\rrbracket
\]
is the underlying real bundle of \(K_J^{-1}\), and the symmetric trace-free endomorphisms that anticommute with its complex structure form the complex line
\[
(K_J^{-1})^{\otimes2}=K_J^{-2}.
\]

Since \(W_3^+|_C\) is nowhere zero, it gives a smooth complex trivialization of \(K_J^{-2}|_C\). Therefore
\[
c_1(K_J^{-2}|_C)=0.
\]
Because
\[
c_1(K_J^{-2})=2c_1(M,J),
\]
one obtains
\[
2\langle c_1(M,J),[C]\rangle=0.
\]
Equivalently,
\[
\langle c_1(M,J),[C]\rangle=0.
\]
There is no torsion subtlety here: \(H^2(C;\mathbb Z)\) is torsion-free on every connected oriented closed surface.

---

## 5. Canonical Chern form and the coefficient \(s/4\)

AAD equations (21)–(25) give
\[
\gamma_J=-db=R(\Omega)-a\wedge Ja,
\]
and explicitly identify \(\gamma_J\) as a de Rham representative of
\[
2\pi c_1(M,J).
\]

Along \(C\), \(T=0\), hence \(a=0\), so
\[
\gamma_J|_C=R(\Omega)|_C.
\]

It remains to verify
\[
R(\Omega)=\frac{s}{4}\Omega.
\]

Let
\[
u=\frac{\Omega}{\sqrt2}.
\]
The Step-62 block decomposition is
\[
W^+=
\begin{pmatrix}
r&\eta^T\\
\eta&-\frac r2 I+V
\end{pmatrix}.
\]
At a torsion zero, the almost-Kähler Weitzenböck identity gives
\[
q=|\nabla\Omega|^2=4r-\frac{2s}{3}.
\]
Since \(q=0\),
\[
r=\frac{s}{6}.
\]
This is also the AAD relation \(s^*-s=q\), together with
\[
s^*=\frac{2\kappa+s}{3},\qquad \kappa=6r.
\]

The already established equality \(\eta=0\) says that \(\Omega\) is an eigenform of \(W^+\), so
\[
W^+(\Omega)=\frac{s}{6}\Omega.
\]
For an Einstein metric, the Singer–Thorpe decomposition in the AAD convention gives
\[
R|_{\Lambda^+}=W^++\frac{s}{12}\operatorname{Id}.
\]
Therefore
\[
R(\Omega)
=\left(\frac{s}{6}+\frac{s}{12}\right)\Omega
=\frac{s}{4}\Omega.
\]

This coefficient also agrees with the Kähler–Einstein normalization: if \(\operatorname{Ric}=(s/4)g\), then the Ricci form is \((s/4)\Omega\).

It follows that
\[
2\pi\langle c_1(M,J),[C]\rangle
=\int_C\gamma_J
=\frac{s}{4}\int_C\Omega
=\frac{s}{4}\operatorname{Area}_g(C).
\]
Since \(s\neq0\) and \(C\) has positive area,
\[
\langle c_1(M,J),[C]\rangle\neq0.
\]
This contradicts the trivialization by \(W_3^+|_C\).

Hence no such compact surface \(C\) can exist.

---

## 6. Direct verified formulation

**Proposition.**  
Let \((M^4,g,J,\Omega)\) be Einstein almost-Kähler with scalar curvature \(s\neq0\). Let \(C\subset\{\nabla\Omega=0\}\) be a compact smooth embedded surface with \(\partial C=\varnothing\). If \(D(\nabla\Omega)_p\neq0\) for every \(p\in C\), then a contradiction results.

The proof above works componentwise if \(C\) is disconnected.

If “closed” were intended merely to mean a closed subset of \(M\), compactness would need to be added: the Chern-number pairing and finite area integral used here are properties of compact \(C\).

---

## 7. Exceptional points where \(DT=0\)

Now suppose \(C\subset Z\) is a compact smooth surface and the real-rank-two locus of \(DT\) is dense in \(C\).

At every \(p\in C\), including exceptional points,
\[
T_pC\subseteq\ker DT_p,
\]
so the determinant still vanishes. The sum-of-squares formula still yields
\[
c=0,\qquad \det B=0.
\]
Thus
\[
\eta=0
\]
everywhere on \(C\), without needing a continuity argument.

Moreover, on \(C\),
\[
W_3^+(p)=0
\quad\Longleftrightarrow\quad
DT_p=0.
\]
Indeed:

- \(DT_p=0\) implies \(B=0\), hence \(S=A=0\), so \(W_3^+(p)=0\).
- If \(W_3^+(p)=0\), then \(A=0\). Since \(c=0\), the cone gives \(S=0\), hence \(B=0\) and \(DT_p=0\).

On the dense rank-two locus, \(TC\) is \(J\)-invariant. Since \(TC\) and \(J\) vary continuously, \(TC\) is \(J\)-invariant on all of \(C\). Therefore \(C\) has its \(J\)-orientation and
\[
\Omega|_C=dA_g
\]
everywhere.

The canonical-curvature calculation consequently extends across all exceptional points:
\[
\gamma_J|_C=\frac{s}{4}\Omega|_C.
\]
Hence
\[
\langle c_1(M,J),[C]\rangle
=\frac{s\,\operatorname{Area}_g(C)}{8\pi}.
\]

Since
\[
c_1(K_J^{-2})=2c_1(M,J),
\]
the degree is
\[
\boxed{
\deg(K_J^{-2}|_C)
=\frac{s\,\operatorname{Area}_g(C)}{4\pi}.
}
\]
Thus the factor and sign in the notes are correct. In fact,
\[
\frac{s\,\operatorname{Area}_g(C)}{8\pi}\in\mathbb Z,
\qquad
\frac{s\,\operatorname{Area}_g(C)}{4\pi}\in2\mathbb Z.
\]

Let
\[
E=\{p\in C:DT_p=0\}.
\]
Then \(E\) is exactly the zero set of \(W_3^+|_C\). If \(E\) consists of isolated points, the local winding numbers of this smooth complex-line section satisfy
\[
\sum_{p\in E}\operatorname{wind}_p(W_3^+)
=
\frac{s\,\operatorname{Area}_g(C)}{4\pi}.
\]
When \(s<0\), this sum lies below zero. A smooth section may have local windings of either sign, so the equality by itself is compatible with isolated exceptional points. The supplied AAD identities do not make \(W_3^+|_C\) holomorphic or force zero-or-positive local multiplicities.

For nonisolated \(E\), the precise replacement is the relative Euler class
\[
e\!\left(K_J^{-2}|_C,W_3^+\right)
\in H^2(C,C\setminus E;\mathbb Z).
\]
Its image in \(H^2(C;\mathbb Z)\) is \(c_1(K_J^{-2}|_C)\), and its evaluation on \(C\) is still
\[
\frac{s\,\operatorname{Area}_g(C)}{4\pi}.
\]

Thus the exceptional-point extension in the notes is correct, with the dense rank-two assumption supplying the global \(J\)-invariance of \(TC\), and with the zero set of \(W_3^+|_C\) identified exactly—not merely inclusively—with \(\{DT=0\}\).