# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 62,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step62_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step62_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify Theorem 62.A and Corollaries 62.B/62.C in the attached note (closed negative Goldberg problem, four-dimensional Einstein almost-Kahler geometry). Check carefully: (1) the Weitzenbock identity for a harmonic self-dual 2-form of constant length |Omega|^2=2 and q=4<W+u,u>-2s/3; (2) the Derdzinski/Einstein Weitzenbock formula nabla^*nabla W+ = -(s/2)W+ + 6(W+)^2 - 2 tr((W+)^2) Id in the endomorphism normalization where a Kahler surface has W+ spectrum (s/6,-s/12,-s/12) (confirm by testing on Kahler and on the integrated identity int|nabla W+|^2 + (s/2)|W+|^2 - 18 det W+ = 0); (3) the computation at a torsion zero giving |nabla^2 Omega|^2 = 4 trV^2 - 12|eta|^2, including the claim that nabla^2 Omega(p) takes values in Omega^perp inside Lambda^+; (4) the translation into the first-jet parametrization f=cz+(S+A)zbar, the cone ||A||^2=8|c|^2+||S||^2 (using the numerically determined proportionalities |eta|^2=|m_c|^2/8, trV^2=|m_A|^2/4, |m|^2/2=|nabla^2 Omega|^2, Frobenius ratios 4|c|^2:2||A||^2:2||S||^2), and the index bound det_R Df >= 25|c|^4 via |det S|<=||S||^2/2. Assess whether 'every nondegenerate torsion zero has index +1' follows rigorously, and whether the numerical continuation evidence (section 3) is consistent with the cone being the complete first nonlinear compatibility. Point out any sign/normalization error or hidden assumption (e.g. orientation of E, identification of c with eta, whether the S/A split used in the determinant matches the U(2) split used numerically). Also say whether this identity or index law appears to be known (Armstrong, AAD, Kim) as far as the supplied sources show; do not invent literature.

## Integrated Scientific Memo

## Verification result

**Theorem 62.A is correct with the stated conventions. Corollaries 62.B and 62.C also follow rigorously.** The numerical curvature-to-jet proportionalities can be replaced by an explicit exact coframe calculation, supplied below. In particular, **every nondegenerate torsion zero has index \(+1\)** in the complex orientation of \(E=\Lambda^{0,1}\otimes\Lambda^{0,2}\).

The stronger assertion that the cone is the **complete** degree-four compatibility remains numerical evidence, not a proved consequence of the supplied calculations. It is not needed for the index theorem.

### 1. Harmonic-form and Einstein Weyl identities

Use
\[
L:=\nabla^*\nabla=-\operatorname{tr}\nabla^2,
\]
and use the Hilbert–Schmidt norm of \(W^+\) **as an endomorphism of \(\Lambda^+\)**.

For a self-dual two-form,
\[
(d\delta+\delta d)\Omega
=L\Omega-2W^+\Omega+\frac{s}{3}\Omega.
\]
The almost-Kähler form is closed and self-dual, hence harmonic. Thus
\[
L\Omega=2W^+\Omega-\frac{s}{3}\Omega.
\]
The constant-length condition gives
\[
0=\frac12L|\Omega|^2
=\langle L\Omega,\Omega\rangle-|\nabla\Omega|^2.
\]
Consequently, for \(u=\Omega/\sqrt2\),
\[
\boxed{q:=|\nabla\Omega|^2
=4\langle W^+u,u\rangle-\frac{2s}{3}.}
\]
At a torsion zero, \(r:=\langle W^+u,u\rangle=s/6\).

The Einstein–Derdziński identity in this normalization is
\[
\boxed{
LW^+=-\frac{s}{2}W^+
+6(W^+)^2-2\operatorname{tr}\bigl((W^+)^2\bigr)I.
}
\]
Both requested checks agree:

* On a Kähler–Einstein surface,
  \[
  \operatorname{spec}W^+
  =\left(\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right),
  \qquad \operatorname{tr}(W^+)^2=\frac{s^2}{24}.
  \]
  Substitution makes the right-hand side zero on each eigenspace, as required by parallelness of \(W^+\).
* Pairing with \(W^+\), using \(\operatorname{tr}W^+=0\) and
  \(\operatorname{tr}(W^+)^3=3\det W^+\), gives on a closed manifold
  \[
  \boxed{
  \int_M\left(
  |\nabla W^+|^2+\frac{s}{2}|W^+|^2-18\det W^+
  \right)=0.
  }
  \]
  For the Kähler spectrum, \((s/2)|W^+|^2=18\det W^+=s^3/48\).

There is no sign or coefficient error in these two formulas. The Kähler test alone fixes only the ratio of the linear and quadratic coefficients; it should not be presented as an independent determination of all coefficients.

### 2. The zero identity and the range of the Hessian

At a torsion zero \(p\), write
\[
W^+=
\begin{pmatrix}
r&\eta^T\\
\eta&-\frac r2 I+V
\end{pmatrix},
\qquad r=\frac{s}{6},\qquad \operatorname{tr}V=0.
\]
Then
\[
\langle(W^+)^2u,u\rangle=\frac{s^2}{36}+|\eta|^2,
\]
\[
\operatorname{tr}(W^+)^2
=\frac{s^2}{24}+2|\eta|^2+\operatorname{tr}V^2.
\]
The \(uu\)-entry of the Weyl identity is therefore
\[
\langle(LW^+)u,u\rangle=2|\eta|^2-2\operatorname{tr}V^2.
\]

Although \(\nabla u(p)=0\), one must retain \(Lu(p)\). The product rule gives
\[
Lr(p)=\langle(LW^+)u,u\rangle
+2\langle W^+Lu,u\rangle.
\]
The terms involving \(\nabla u\) vanish at \(p\). Since
\[
Lu=2W^+u-\frac{s}{3}u,
\]
the second term is
\[
2\langle W^+Lu,u\rangle
=4\left(\frac{s^2}{36}+|\eta|^2\right)
-\frac{2s}{3}\frac{s}{6}
=4|\eta|^2.
\]
Thus
\[
Lr(p)=6|\eta|^2-2\operatorname{tr}V^2.
\]
Einstein implies constant \(s\), so
\[
Lq(p)=24|\eta|^2-8\operatorname{tr}V^2.
\]
On the other hand, \(T=\nabla\Omega\) vanishes at \(p\), whence
\[
L|T|^2(p)=-2|\nabla T|^2(p)
=-2|\nabla^2\Omega|^2(p).
\]
Combining these equations proves
\[
\boxed{
|\nabla^2\Omega|^2(p)
=4\operatorname{tr}V^2-12|\eta|^2.
}
\]

The assertion about the range of \(\nabla^2\Omega\) is also exact:

* The Hodge star is parallel, so every \(\nabla_k\nabla_l\Omega\) is self-dual.
* Differentiating \(\langle\nabla_l\Omega,\Omega\rangle=0\) gives
  \[
  \langle\nabla_k\nabla_l\Omega,\Omega\rangle
  =-\langle\nabla_l\Omega,\nabla_k\Omega\rangle,
  \]
  which vanishes at a torsion zero.

Therefore
\[
\boxed{
\nabla_k\nabla_l\Omega(p)\in
\Lambda_p^+\cap\Omega(p)^\perp
\quad\text{for every }k,l.
}
\]
This does **not** assert symmetry in \(k,l\): the curvature commutator may be nonzero. The norm in 62.A is the full sum over ordered pairs.

### 3. Exact curvature-to-jet calculation: removing the numerical gap

The supplied determinant script checks the determinant and real Frobenius formulas. It does **not** check the identification of its \(c,S,A\) with the curvature sectors defined numerically by SVD. That link can be proved directly from the supplied AAD Ricci identities.

Choose an oriented orthonormal coframe at \(p\) with
\[
\Omega=e^{01}+e^{23},\qquad
\phi=e^{02}-e^{13},\qquad
\psi=J\phi=e^{03}+e^{12}.
\]
All three forms have squared norm \(2\). Take \(Je_0=e_1\), \(Je_2=e_3\), and \(Ja=-a\circ J\). Write
\[
\nabla\Omega=a\otimes\phi-Ja\otimes\psi,
\qquad a(p)=0.
\]
For \(M_{kl}=(\nabla_k a)_l\), differentiation at the zero yields
\[
\nabla_k\nabla_l\Omega
=M_{kl}\phi-(\nabla_kJa)_l\psi,
\]
and hence
\[
|\nabla^2\Omega|^2=4|M|^2.
\]

In the script, \(m\) consists of the **form inner products**
\[
N^\phi_{kl}=\langle\nabla_k\nabla_l\Omega,\phi\rangle,
\qquad
N^\psi_{kl}=\langle\nabla_k\nabla_l\Omega,\psi\rangle.
\]
Thus
\[
N^\phi=2M,\qquad |N^\psi|^2=4|M|^2,
\qquad
\boxed{|m|^2=8|M|^2,\quad |\nabla^2\Omega|^2=\frac12|m|^2.}
\]

For an explicit matching parametrization, encode the metric-dual of \(a\) by
\[
f=(a_0+i a_1,\ a_2+i a_3),\qquad
z=(x_0+i x_1,\ x_2+i x_3).
\]
The first-jet kernel is
\[
f(z)=cz+(S+A)\bar z,\qquad
S^T=S,\qquad
A=\begin{pmatrix}0&a_*\\-a_*&0\end{pmatrix}.
\]
Indeed, at the zero the supplied Ricci identities reduce to
\[
da=-R(\psi),\qquad d(Ja)=-R(\phi).
\]
Einstein makes both right sides self-dual. A direct real-matrix calculation of these two self-duality conditions forces the complex-linear part of \(Df\) to be scalar and leaves the entire antilinear part unrestricted: \(2+8=10\) real dimensions.

Because \(r=s/6\), the transverse scalar part of \(R=W^++sI/12\) cancels:
\[
R(\phi)=\eta_1\Omega+V_{11}\phi+V_{12}\psi,
\]
\[
R(\psi)=\eta_2\Omega+V_{12}\phi+V_{22}\psi.
\]
Writing \(c=c_R+i c_I\), \(a_*=a_R+i a_I\), the exterior derivatives of the linear model are
\[
da=2c_I\Omega-2a_R\phi-2a_I\psi,
\]
\[
d(Ja)=2c_R\Omega+2a_I\phi-2a_R\psi.
\]
The symmetric \(S\)-part contributes zero to both expressions. Comparison gives
\[
\eta=(-2c_R,-2c_I),\qquad
V=
\begin{pmatrix}
-2a_I&2a_R\\
2a_R&2a_I
\end{pmatrix}.
\]
In particular,
\[
\boxed{
|\eta|^2=4|c|^2,\qquad
\operatorname{tr}V^2=8|a_*|^2=4\|A\|^2.
}
\]
Signs or phases of these component formulas change with gauge conventions, but their norms do not.

The real Frobenius identity is
\[
|M|^2=\|Df\|_{\mathbb R}^2
=4|c|^2+2\|A\|^2+2\|S\|^2.
\]
Consequently,
\[
|m_c|^2=32|c|^2,\qquad
|m_A|^2=16\|A\|^2,\qquad
|m_S|^2=16\|S\|^2,
\]
and therefore exactly
\[
\boxed{
|\eta|^2=\frac{|m_c|^2}{8},\qquad
\operatorname{tr}V^2=\frac{|m_A|^2}{4}.
}
\]

This verifies both the constants and the sector matching: within the antilinear part, the joint curvature kernel is precisely the symmetric sector; its Frobenius-orthogonal complement is precisely the antisymmetric sector. Thus the SVD-defined \(S/A\) split in `step62_zero_prolong.py` agrees with the transpose-based split in the determinant calculation, rather than merely sharing its dimensions.

Substituting into 62.A now proves, without floating-point input,
\[
2|m_c|^2-\frac12|m_A|^2+\frac12|m_S|^2=0,
\]
equivalently
\[
\boxed{\|A\|^2=8|c|^2+\|S\|^2.}
\]

### 4. Corollary 62.B

The invariant consequences follow directly from 62.A:
\[
\boxed{
\operatorname{tr}V^2
=\frac14|\nabla^2\Omega|^2+3|\eta|^2.
}
\]
Thus:

1. A nonzero first torsion jet forces \(V\ne0\), hence \(A\ne0\). The cone excludes each pure \(c\), pure \(S\), or pure \(A\) jet unless it vanishes.
2. If \(W_3^+=V=0\), then \(\nabla^2\Omega=0\) and \(\eta=0\). “Order at least two” here refers to the torsion section \(T=\nabla\Omega\), not to \(\Omega\).
3. At a zero,
   \[
   |W^+|^2-\frac{s^2}{24}
   =2|\eta|^2+\operatorname{tr}V^2
   =\frac14|\nabla^2\Omega|^2+5|\eta|^2.
   \]
   This is strictly positive whenever the first torsion jet is nonzero.

No numerical sector identification is needed for items 2–3.

### 5. Corollary 62.C: determinant, orientation and degeneracy

For \(f(z)=cz+B\bar z\), \(B=S+A\), complexifying the real Jacobian gives
\[
\begin{pmatrix}cI&B\\ \bar B&\bar cI\end{pmatrix}.
\]
Therefore
\[
\det_{\mathbb R}Df
=\det\bigl(|c|^2I-\bar BB\bigr)
=|c|^4-|c|^2(\|S\|^2-\|A\|^2)+|\det B|^2.
\]
Here \(\bar B\) denotes entrywise conjugation, **not** the adjoint. The identity
\[
\operatorname{tr}(\bar BB)=\|S\|^2-\|A\|^2
\]
uses \(S^T=S\) and \(A^T=-A\).

On the cone,
\[
\det_{\mathbb R}Df=9|c|^4+|\det B|^2.
\]
Since
\[
\det B=\det S+a_*^2,\qquad
|a_*|^2=\frac{\|A\|^2}{2}
=4|c|^2+\frac{\|S\|^2}{2},
\]
and
\[
|\det S|\le\frac{\|S\|^2}{2},
\]
we obtain
\[
|\det B|\ge |a_*|^2-|\det S|\ge4|c|^2.
\]
Hence
\[
\boxed{\det_{\mathbb R}Df\ge25|c|^4.}
\]

For \(c\ne0\), this is strictly positive. For \(c=0\), the determinant is \(|\det B|^2\); **nondegeneracy** makes it strictly positive. Thus the index conclusion does not accidentally require \(c\ne0\).

The relevant orientations must be stated:

* the base is oriented by \(\Omega^2\);
* \(E=\Lambda^{0,1}\otimes\Lambda^{0,2}\) has its complex orientation;
* the coefficient identification with \(a\) is the natural unitary one, possibly followed by conjugation of the entire complex rank-two space.

Unitary identifications preserve real orientation, and conjugation on \(\mathbb C^2\) has determinant \(+1\). The map \(a\mapsto T\) intertwines the complex structures up to an overall sign, so it preserves this real orientation. Transposition of \(M\), and its positive scaling in the script, also leave its determinant sign unchanged. Therefore
\[
\boxed{\operatorname{ind}_p(T)=+1
\quad\text{at every nondegenerate torsion zero}.}
\]

For a nonzero first jet, degeneracy on the cone is exactly
\[
c=0,\qquad \det S=-a_*^2,\qquad
|\det S|=\frac{\|S\|^2}{2}.
\]
The last condition means that \(S\) has equal singular values. These conditions concern the linearization; they do not determine the local degree of a degenerate isolated zero.

### 6. Corrections and limits of the supplied note

**Code normalization.** In `step62_zero_prolong.py`, the returned variable named `Mmat` is \(N^\phi\), not \(\nabla a\):
\[
\texttt{Mmat}=2\nabla a.
\]
The expression `0.5*einsum(NN,PHI)` is already the two-form inner product, because skew-tensor contraction counts each coefficient twice. The docstring’s identification with \(\nabla a\) is off by \(2\). This does not affect determinant signs or the stated \(m\)-norm formulas, but should be corrected.

**Step-59 versus Step-62 \(\eta\).** Step 62 uses the off-diagonal endomorphism vector, whereas Step 59 explicitly uses a form norm:
\[
|\eta|^2_{\text{Step 59}}=2|\eta|^2_{\text{Step 62}}.
\]
The transverse quantity satisfies
\[
|W_3^+|_{\mathrm{HS}}^2=\operatorname{tr}V^2.
\]
Thus the Step-59 balance, when rewritten in Step-62 notation, has integrand
\[
2|\eta|^2+2\operatorname{tr}V^2+\frac{3q^2}{16}-\frac32q.
\]
These conventions must not be mixed. The note’s identification of the integrated Laplacian calculation with “the familiar AAD torsion balance” is not established term by term in the supplied text; the zero identity itself does not depend on that identification.

**Gibbons–Hawking control.** The supplied GH data have \(\eta=0\), so they test the \(4\operatorname{tr}V^2\) coefficient and the \(A/S\) balance, but cannot test the coefficient \(-12|\eta|^2\) or the \(c\)-to-\(\eta\) normalization. “An independent check of every constant” is therefore too strong. The exact coframe calculation above supplies the missing check.

The GH degeneracy is also consistent directly with the displayed formulas: \(g,\Omega\) depend only on \(x,y\), and their first derivatives vanish at the origin. Consequently \(\nabla_{\partial_\tau}T=\nabla_{\partial_z}T=0\) there, so the first torsion derivative has rank at most two. Finally, `gh_jets` converts symbolic coefficients to floats before evaluating residuals; its numerical zero is not itself a symbolic certificate.

### 7. What the continuation evidence establishes

The section-3 reports are consistent with the cone being the sole quadratic obstruction at degree four:

* the off-cone targets retain residuals;
* doubling \(t\) from \(0.2\) to \(0.4\) multiplies the reported squared residual by about \(14.6\), close to the \(16\) predicted for a quadratic obstruction;
* sampled on-cone targets, including mixed nondegenerate ones and both tested scalar-curvature signs, reach squared residuals near \(10^{-30}\);
* degree four is the appropriate order to detect this identity, since it includes second derivatives of curvature and the Hessian of \(q\).

But the source bundle contains the summarized continuation results, not their raw output files. The displayed solver is floating-point Levenberg–Marquardt; neither failure to converge nor successful sampled convergence proves the universal compatibility statement.

An exact proof of completeness would require elimination of the higher Taylor coefficients, showing that—after accounting for gauge freedom and equation dependencies—the entire degree-four obstruction on the admissible lower jets is precisely a multiple of \(\Phi\), and that \(\Phi=0\) suffices for extension through that order. This must cover the degenerate stratum as well as regular cone points. The assertion that the trace-free part is absorbed by free \(\nabla^2W^+\) does not by itself supply this solvability proof.

No supplied degree-five results resolve higher compatibility, and finite-order compatibility does not construct a formal solution to all orders or an analytic germ. **None of these limitations weakens the index theorem**, which uses only the necessary cone relation.

### 8. Literature and closed-problem scope

The supplied AAD summaries provide the Ricci identities, curvature splitting and balance underlying this derivation. No supplied passage states either the exact torsion-zero identity or the positive-index law. Step 75 contains the unrestricted determinant formula; its negative-index linear models are excluded by the additional Einstein cone, so there is no contradiction.

Step 59 says Armstrong’s full text was unavailable and only metadata had been retrieved. No Kim text or quoted result is supplied. Accordingly, the material does **not** determine whether the identity or index law is already known in the wider literature, and supports no priority claim.

For the closed negative Goldberg problem, the result removes negative-index **nondegenerate** zeros, but does not contradict the positive charge \(5\chi+6\tau\). If all zeros are nondegenerate, their number is exactly that charge. Degenerate zeros, higher-order zeros, and existence of strict negative Einstein almost-Kähler germs with torsion zeros remain unresolved by this calculation. The cancellation of \(s\) is genuine: any obstruction specific to negative scalar curvature requires additional local or global information.